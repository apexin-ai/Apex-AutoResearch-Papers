# Research conversation: I need to fill out the ARR Responsible NLP Checklist for a paper. Please read the following files and report back their 

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aa0c4d7f41c26a15c.jsonl`
- **Structured JSON:** [`c26b667bf11cc13759bd.json`](../../sessions/c2/c26b667bf11cc13759bd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

21 recorded events

### User

_source line 1 · 2026-05-23T15:30:11.812Z_

I need to fill out the ARR Responsible NLP Checklist for a paper. Please read the following files and report back their key content:

1. /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex — Look for: \section{Limitations}, any ethics/risks discussion, any AI assistant disclosure, what sections are included via \input
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex — Look for: model zoo description (sizes, datasets cited), evaluation setup (lm-evaluation-harness version), hyperparameters, any license discussion
3. /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex — Look for: what artifacts are used/created, citations to model zoo creators
4. /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex — Look for: any limitations or risks mentioned
5. /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex — Skim for content

For each file, report the section numbers/labels and key content relevant to: model sizes, compute budget, datasets used, evaluation tools, licenses, PII, human subjects, AI assistants, limitations section location and content, statistical methods used.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "42028348-629d-494c-9ba6-5ed1efbe2bc1",
  "agentId": "aa0c4d7f41c26a15c",
  "type": "user",
  "uuid": "7394e893-c8f1-450a-82ee-bc9bd339b482",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "a02ce5b1-88a8-4060-9e99-0b93ad72b89c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-juggling-wozniak"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-23T15:30:13.404Z_

I'll read all those files to extract the key information for your ARR Responsible NLP Checklist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7394e893-c8f1-450a-82ee-bc9bd339b482",
  "isSidechain": true,
  "agentId": "aa0c4d7f41c26a15c",
  "requestId": "req_011CbKjrJx4TUukME28GUmex",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "918e16c0-59c5-4a10-bfa7-6292d623458a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "a02ce5b1-88a8-4060-9e99-0b93ad72b89c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-juggling-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WzqX8wdjrXjnqT7ekCcz93",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39918,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39918,
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

_source line 3 · 2026-05-23T15:30:13.829Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JW1SqG9YhCgqMTPLigtk7b`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "918e16c0-59c5-4a10-bfa7-6292d623458a",
  "isSidechain": true,
  "agentId": "aa0c4d7f41c26a15c",
  "requestId": "req_011CbKjrJx4TUukME28GUmex",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b0f9d803-c9ec-4687-9ae8-53dc8d5477fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "a02ce5b1-88a8-4060-9e99-0b93ad72b89c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-juggling-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WzqX8wdjrXjnqT7ekCcz93",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39918,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39918,
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

_source line 4 · 2026-05-23T15:30:13.847Z_

<details><summary>↩ Tool result · `toolu_01JW1SqG9YhCgqMTPLigtk7b`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	\usepackage{caption}
17	
18	\title{Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\begin{abstract}
26	Practitioners select among hybrid linear recurrent architectures using aggregate benchmarks, but these scores can mask per-example consequences. Across three controlled designs, adding attention affects substantially different examples per architecture (Jaccard $\approx$ 0.10, approximately twice the independence baseline); validation across five architectures and ten pairwise comparisons confirms this on all four benchmarks (all $p < .01$). Using the model zoo of \citet{wang2025hybrid} (three architectures, five attention ratios, two scales), we decompose per-example effects and find that this predictive multiplicity \citep{marx2020predictive} depends on task type ($\alpha = 0.14$--$0.30$) more than attention dose. Aggregate trends do not reach statistical significance ($n = 5$; Bonferroni-adjusted $p = .170$), yet per-example overlap saturates at 4\% attention and remains flat across all four benchmarks. Majority vote fails to exploit this complementarity, confirming that configurations interchangeable by aggregate metrics carry hidden per-example consequences. Confidence-informed routing extracts 36\% of oracle complementarity on LAMBADA ($+5.3$\,pp vs.\ majority vote), suggesting these differences are partially actionable.
27	\end{abstract}
28	
29	\input{sections/introduction}
30	
31	\input{sections/related_work}
32	
33	\input{sections/method}
34	
35	\input{sections/experiments}
36	
37	\input{sections/conclusion}
38	
39	\section*{Limitations}
40	
41	\paragraph{Single training runs.} Each configuration corresponds to a single training run, so we cannot fully disentangle architectural from seed-specific effects. The $3\times$ within- vs.\ cross-architecture Jaccard gap and Pythia 70M seed calibration (within-seed $J$ is 2.7--4.3$\times$ higher; Appendix~\ref{app:seed_calibration}) provide proxy evidence, and the consistency of significant Jaccard across all 40 architecture--benchmark combinations (all $p < .01$) would be unlikely under seed noise alone. With $n = 5$ attention ratios, the minimum achievable $p$ is 0.017, so LAMBADA's Bonferroni-adjusted $p = .170$ does not reach conventional significance.
42	
43	\paragraph{Coverage.} We examine three primary architectures (plus two extended) from one model zoo, four main benchmarks, and two scale points. Generalization to Mamba, RWKV, other hybrid families, and generation tasks remains open. Results at larger scales (e.g., 7B+) may differ, particularly as attention mechanisms become more expressive with increased capacity.
44	
45	\paragraph{Pre-training only.} All evaluations use pretrained checkpoints without fine-tuning; per-example effects may not persist after task-specific adaptation.
46	
47	\section*{Code and Data Availability}
48	
49	All models are from the publicly available model zoo of \citet{wang2025hybrid}. Our analysis code and per-example evaluation outputs will be released upon publication.
50	
51	\bibliography{references}
52	
53	\appendix
54	\input{sections/appendix}
55	
56	\end{document}
57	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0f9d803-c9ec-4687-9ae8-53dc8d5477fa",
  "isSidechain": true,
  "promptId": "42028348-629d-494c-9ba6-5ed1efbe2bc1",
  "agentId": "aa0c4d7f41c26a15c",
  "type": "user",
  "uuid": "33421c9b-1409-4bcd-8089-3ea6299f473a",
  "sourceToolAssistantUUID": "b0f9d803-c9ec-4687-9ae8-53dc8d5477fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "a02ce5b1-88a8-4060-9e99-0b93ad72b89c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-juggling-wozniak"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T15:30:13.876Z_

<details open><summary>🔧 Tool call — Read · `toolu_013nokWDfUuG6fj7QZfDNQQL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33421c9b-1409-4bcd-8089-3ea6299f473a",
  "isSidechain": true,
  "agentId": "aa0c4d7f41c26a15c",
  "requestId": "req_011CbKjrJx4TUukME28GUmex",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c45888ac-e593-4772-9681-7d29d4a7ceed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "a02ce5b1-88a8-4060-9e99-0b93ad72b89c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-juggling-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WzqX8wdjrXjnqT7ekCcz93",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39918,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39918,
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

_source line 6 · 2026-05-23T15:30:13.884Z_

<details><summary>↩ Tool result · `toolu_013nokWDfUuG6fj7QZfDNQQL`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	We describe the model configurations, evaluation benchmarks, and analytical framework used to measure how attention affects cross-architecture agreement at both aggregate and per-example levels.
4	
5	\subsection{Model Zoo}\label{ssec:model_zoo}
6	
7	We use the pretrained model zoo of \citet{wang2025hybrid}, which provides controlled comparisons across architectures and attention ratios. The zoo contains three linear recurrent architectures: GatedDeltaNet \citep{yang2024gateddeltanet}, RetNet \citep{sun2023retnet}, and HGRN2 \citep{qin2024hgrn2}. These three architectures represent distinct approaches to linear recurrence: GatedDeltaNet uses gated delta rules, RetNet uses multi-scale exponential decay, and HGRN2 uses gated linear recurrence with state expansion. Each architecture is trained at five attention ratios: 0\% (pure recurrent), 4\%, 7.7\%, 14.3\%, and 25\%. We adopt the h$k$-1 notation from the original work, where one attention layer is interleaved per every $k{+}1$ total layers: h3-1 corresponds to 25\% attention, h6-1 to 14.3\%, h12-1 to 7.7\%, and h24-1 to 4\%. All configurations are available at two scales: 340M and 1.3B parameters. Within each scale, all models share identical training data, tokenizer, and hyperparameters; they differ only in architecture and attention configuration. This controlled design isolates the effect of attention from confounds such as training data or optimization differences. The zoo also includes a Transformer baseline (pure attention) at both scales.
8	
9	\subsection{Task Taxonomy}\label{ssec:task_taxonomy}
10	
11	We evaluate on 10 benchmarks grouped into four categories defined by the primary cognitive demand of each task. This taxonomy (informal; not pre-registered) was fixed prior to analysis following established distinctions in the hybrid architecture literature \citep{arora2024zoology} (see Appendix~\ref{app:benchmark_details} for the confirmatory/exploratory split), not derived post hoc from observed results. The categories test whether the effect of attention on cross-architecture variance depends on task type.
12	
13	\begin{itemize}
14	    \item \textbf{Retrieval}: LAMBADA \citep{paperno2016lambada}, which requires predicting a final word from long-range context without reasoning or world knowledge.
15	    \item \textbf{Comprehension}: BoolQ, a reading comprehension task with yes/no answers.
16	    \item \textbf{Reasoning}: HellaSwag, ARC-Challenge \citep{clark2018arc}, WinoGrande, and PIQA. COPA ($n = 100$) is supplementary; its small sample renders $\alpha$ unreliable (Appendix~\ref{app:subsample_sensitivity}).
17	    \item \textbf{Mixed}: ARC-Easy, MMLU, SciQ, and XStoryCloze, which combine retrieval, comprehension, and reasoning demands.
18	\end{itemize}
19	
20	LAMBADA is the only free-form generation benchmark in our evaluation; its higher $\alpha$ (0.30 vs.\ 0.14--0.21 for multiple-choice tasks) may partly reflect the larger answer space inherent to open-ended prediction. However, within multiple-choice tasks, format (two-way vs.\ four-way) does not predict $\alpha$ (\S\ref{ssec:per_example}).
21	
22	All evaluations use lm-evaluation-harness v0.4.x \citep{gao2024lmeval} with default prompts and greedy decoding; accuracy serves as the primary metric for all benchmarks. Bootstrap analyses use random seed 42 throughout.
23	
24	\subsection{Convergence Metrics}\label{ssec:convergence_metrics}
25	
26	We quantify cross-architecture agreement as a function of attention ratio. For each benchmark and attention ratio, we compute the cross-architecture standard deviation $\sigma$ over the three architectures' accuracy scores. To measure the relationship between attention and convergence, we compute the Spearman rank correlation $\rho$ between attention ratio rank and $\sigma$ across the five attention configurations ($n = 5$). A negative $\rho$ indicates that higher attention ratios are associated with lower cross-architecture variance.
27	
28	We also report the convergence ratio $\sigma_{\text{pure}} / \sigma_{\text{h3-1}}$, defined as the standard deviation under the pure-recurrent configuration divided by that under the highest attention ratio (25\%). Values greater than 1 indicate that higher attention ratios are associated with lower cross-architecture variance.
29	
30	\subsection{Per-Example Decomposition}\label{ssec:per_example_decomposition}
31	
32	To move beyond aggregate metrics, we decompose performance changes at the individual-example level on four benchmarks spanning three task categories: LAMBADA (5{,}153 examples; retrieval), HellaSwag (10{,}042; reasoning), PIQA (1{,}838; reasoning, two-choice), and ARC-Easy (2{,}376; mixed). HellaSwag uses normalized accuracy (acc\_norm) as the per-example correctness criterion. Supplementary analyses on BoolQ (3{,}270; comprehension) and WinoGrande (1{,}267; reasoning, two-choice) appear in Appendix~\ref{app:boolq} and \ref{app:winogrande}. For each architecture, we compare the pure-recurrent baseline against its h3-1 hybrid (25\% attention), which maximizes the contrast between recurrent and hybrid modes; \S\ref{ssec:per_example} confirms that $\alpha$ is stable across intermediate ratios (variation $< 0.03$). We classify each example into one of three categories:
33	
34	\begin{itemize}
35	    \item \textbf{Helped}: correct in the hybrid but incorrect in the pure model.
36	    \item \textbf{Hurt}: correct in the pure model but incorrect in the hybrid.
37	    \item \textbf{Unchanged}: both models agree (both correct or both incorrect).
38	\end{itemize}
39	
40	The net effect for each architecture is $|\text{helped}| - |\text{hurt}|$. A positive net effect means more examples transition to correct than to incorrect when attention is added; a negative net effect means the opposite.
41	
42	To measure cross-architecture overlap in per-example effects, we compute the pairwise Jaccard similarity $J = |A \cap B| / |A \cup B|$ between the helped sets of two architectures and, separately, between their hurt sets. $J = 1$ indicates identical sets; $J = 0$ indicates no overlap. Low $J$ values would indicate that different architectures are affected on different subsets of examples, which would constitute per-example divergence even when aggregate performance converges. On $K$-choice tasks, binarization collapses $K{-}1$ wrong answers into a single ``incorrect'' category, potentially counting architectures as agreeing (both wrong) when they select different wrong answers. This conservative bias strengthens the multiplicity claim: true per-example divergence may exceed what binary Jaccard captures. Conversely, on $K$-choice tasks, binarization may overestimate hurt-set agreement when two architectures both transition from correct to incorrect but select different wrong answers. Appendix~\ref{app:continuous_jaccard} confirms that results are robust under continuous Jaccard similarity, mitigating concerns about information loss from binarization.
43	
44	\subsection{Statistical Methods}\label{ssec:statistical_methods}
45	
46	All statistical tests are two-tailed. We use exact permutation tests for Spearman $\rho$ ($5! = 120$ permutations). With $n = 5$, only $|\rho| = 1.0$ achieves $p < .05$ ($p = .017$); all Spearman-based inferences are therefore descriptive and exploratory. We apply Bonferroni correction across all 10 benchmarks (adjusted threshold $\alpha / 10 = 0.005$). Bootstrap 95\% BCa confidence intervals use 10{,}000 resamples; with $n = 3$ architectures, these are heuristic indicators of effect direction. Within-architecture comparisons use Mann-Whitney U; cross-architecture comparisons use Kruskal-Wallis. Attention weight analysis extracts per-layer cosine similarity and Shannon entropy via forward hooks (Appendix~\ref{app:attention_patterns}).
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c45888ac-e593-4772-9681-7d29d4a7ceed",
  "isSidechain": true,
  "promptId": "42028348-629d-494c-9ba6-5ed1efbe2bc1",
  "agentId": "aa0c4d7f41c26a15c",
  "type": "user",
  "uuid": "8430e3e1-020d-4436-80fa-cd77a4c7445c",
  "sourceToolAssistantUUID": "c45888ac-e593-4772-9681-7d29d4a7ceed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "a02ce5b1-88a8-4060-9e99-0b93ad72b89c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-juggling-wozniak"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T15:30:14.617Z_

<details open><summary>🔧 Tool call — Read · `toolu_012raDgJtNqT5xr26H3D4aNh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8430e3e1-020d-4436-80fa-cd77a4c7445c",
  "isSidechain": true,
  "agentId": "aa0c4d7f41c26a15c",
  "requestId": "req_011CbKjrJx4TUukME28GUmex",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "173834b8-80c0-4b8a-b97f-5576b9eccbf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "a02ce5b1-88a8-4060-9e99-0b93ad72b89c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-juggling-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WzqX8wdjrXjnqT7ekCcz93",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39918,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39918,
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

_source line 8 · 2026-05-23T15:30:14.640Z_

<details><summary>↩ Tool result · `toolu_012raDgJtNqT5xr26H3D4aNh`</summary>

```text
1	\section{Introduction}
2	
3	Hybrid recurrent architectures that appear equivalent by aggregate benchmarks affect largely non-overlapping sets of individual examples: adding attention to three controlled linear recurrent backbones yields helped and hurt sets with at most 10\% pairwise overlap, approximately twice the independence baseline. This per-example divergence is invisible in aggregate metrics: aggregate cross-architecture variance decreases on some benchmarks as attention ratio increases, but each architecture reaches similar accuracy by gaining and losing accuracy on different inputs. Practitioners increasingly choose between recurrent backbones based on aggregate benchmark scores. Across all ten pairwise comparisons among five architectures, overlap in per-example effects remains below 14\% (all $p < .01$), meaning the choice of backbone is associated with which specific inputs a deployed system handles correctly.
4	
5	This tension arises in the context of a rapid architectural shift toward hybrid recurrent-attention models, which interleave attention layers within linear recurrent backbones. Jamba \citep{lieber2024jamba}, Griffin \citep{de2024griffin}, RWKV-6 \citep{peng2024eagle}, and RecurrentGemma \citep{botev2024recurrentgemma} each combine recurrence with attention using different mixing strategies. These systems now serve as production-grade alternatives to pure Transformers, and the practical question of how much attention to include is typically answered by comparing aggregate benchmark numbers. \citet{wang2025hybrid} provide a controlled model zoo spanning three recurrent architectures, five attention ratios, and two parameter scales, which enables systematic study of how attention allocation affects these hybrid designs.
6	
7	Most evaluations of hybrid architectures compare aggregate accuracy, which can mask per-example behavioral diversity. Prior work on predictive multiplicity \citep{marx2020predictive} and underspecification \citep{damour2022underspecification,mccoy2020berts} documents this risk for seed variation within a single architecture, but whether the phenomenon extends to architectural variation in hybrid recurrent models remains open. If architectures that score identically in aggregate behave differently on individual inputs, the choice of backbone carries hidden consequences for deployment reliability and ensemble construction.
8	
9	We present the first systematic per-example analysis of how attention affects cross-architecture agreement in hybrid recurrent models. Using the model zoo of \citet{wang2025hybrid}, we compare three architectures (GatedDeltaNet, RetNet, HGRN2) at five attention ratios (0\% to 25\%) and two scales (340M and 1.3B parameters). These three architectures represent distinct approaches to linear recurrence: gated delta rules, multi-scale exponential decay, and gated state expansion. We evaluate all 30 configurations on 10 benchmarks spanning retrieval, comprehension, reasoning, and mixed task categories. On four benchmarks (LAMBADA, $N = 5{,}153$; HellaSwag, $N = 10{,}042$; PIQA, $N = 1{,}838$; ARC-Easy, $N = 2{,}376$) we conduct per-example decompositions, classifying each example as helped, hurt, or unchanged when attention is added, and measure cross-architecture overlap using Jaccard similarity. Figure~\ref{fig:decoupling} previews our central result: aggregate variance reduction and per-example overlap follow different trajectories as attention ratio increases.
10	
11	\begin{figure}[t]
12	\centering
13	\includegraphics[width=\columnwidth]{figures/fig1_decoupling_hero.pdf}
14	\caption{Aggregate convergence and per-example divergence are decoupled (helped: correct only with attention; hurt: correct only without). (a) Cross-architecture standard deviation on LAMBADA decreases with attention ratio at 1.3B (solid; Bonferroni-adjusted $p = .170$, non-significant) but partially rebounds at 340M (dashed). (b) Cross-architecture pairwise Jaccard similarity of per-example helped/hurt sets saturates at the first attention level (4\%) and remains flat. Shaded bands are illustrative ($n = 3$).}
15	\label{fig:decoupling}
16	\end{figure}
17	
18	Our analysis yields two findings. First, per-example predictive multiplicity varies in magnitude across tasks, forming a task-dependent variation. The ambiguity $\alpha$ \citep{marx2020predictive} ranges from 0.14 (PIQA) through 0.15 (HellaSwag) and 0.21 (ARC-Easy) to 0.30 (LAMBADA), while pairwise Jaccard remains uniformly low ($\leq 0.10$, all $p < .01$). Within each benchmark, $\alpha$ is stable across attention ratios (variation $< 0.03$), but differs substantially across task types, ranging from 0.14 (reasoning) to 0.30 (retrieval).
19	
20	Aggregate variance reduction is task-specific and exploratory: of 10 benchmarks, only LAMBADA shows monotonic variance reduction ($\rho = -1.0$, Bonferroni-adjusted $p = .170$; observed at 1.3B, absent at 340M). Yet on this benchmark, per-example Jaccard saturates at the first attention level while aggregate variance continues to decrease (\S\ref{ssec:decoupling}).
21	
22	Our contributions are as follows:
23	\begin{itemize}
24	    \item We show that architectural variation---a source of multiplicity not previously characterized at the per-example level---produces structured per-example predictive multiplicity ($\alpha = 0.14$--$0.30$) across four benchmarks, with magnitude determined by task type rather than attention dose (\S\ref{ssec:per_example}, Table~\ref{tab:multiplicity}). Extended validation across five architectures confirms the pattern: all ten pairwise Jaccard values remain $\leq 0.14$ across four benchmarks (all $p < .01$; Appendix~\ref{app:extended_arch}). The primary controlled variable is the recurrent backbone \citep[cf.][]{mccoy2020berts, damour2022underspecification}, though single training runs prevent full disentanglement from seed effects (Limitations).
25	    \item Per-example Jaccard saturates at the first attention level (4\%) across all four benchmarks and shows no further increase at higher ratios, while aggregate variance shows a non-significant decreasing pattern on LAMBADA (\S\ref{ssec:decoupling}; Appendix~\ref{app:cross_bench_jaccard}). This immediate saturation indicates that minimal attention suffices to establish the full pattern of configuration-specific per-example effects; additional attention narrows aggregate gaps without homogenizing which examples each architecture affects. The aggregate convergence component is dependent on GDN inclusion (\S\ref{ssec:robustness}) and does not replicate on other benchmarks.
26	\end{itemize}
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "173834b8-80c0-4b8a-b97f-5576b9eccbf5",
  "isSidechain": true,
  "promptId": "42028348-629d-494c-9ba6-5ed1efbe2bc1",
  "agentId": "aa0c4d7f41c26a15c",
  "type": "user",
  "uuid": "6b993c41-9ee4-4a54-b958-cdd9d64856c6",
  "sourceToolAssistantUUID": "173834b8-80c0-4b8a-b97f-5576b9eccbf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "a02ce5b1-88a8-4060-9e99-0b93ad72b89c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-juggling-wozniak"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T15:30:14.749Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KjZ4KSgNgQQgrYSqAzBVFj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b993c41-9ee4-4a54-b958-cdd9d64856c6",
  "isSidechain": true,
  "agentId": "aa0c4d7f41c26a15c",
  "requestId": "req_011CbKjrJx4TUukME28GUmex",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "22440b88-a5cd-4653-875b-982dcbedad81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "a02ce5b1-88a8-4060-9e99-0b93ad72b89c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-juggling-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WzqX8wdjrXjnqT7ekCcz93",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39918,
      "cache_read_input_tokens": 0,
      "output_tokens": 416,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 39918
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 416,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 39918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 39918,
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

_source line 10 · 2026-05-23T15:30:14.757Z_

<details><summary>↩ Tool result · `toolu_01KjZ4KSgNgQQgrYSqAzBVFj`</summary>

```text
1	\section{Conclusion}
2	
3	Per-example multiplicity in hybrid recurrent models varies by task ($\alpha = 0.14$--$0.30$), with Jaccard uniformly low ($\leq 0.10$) even as aggregate variance decreases on LAMBADA (non-significant; Table~\ref{tab:convergence}) (dependent on GDN inclusion; \S\ref{ssec:robustness}); five-architecture validation confirms this across four benchmarks (all $J \leq 0.14$, $p < .01$; Appendix~\ref{app:extended_arch}). Pure-model confidence partially predicts affected examples (AUC 0.70--0.74; \S\ref{ssec:per_example}).
4	
5	At the 340M--1.3B scales studied here, two implications for practitioners follow from the ${\sim}90\%$ non-overlap: (1) $\alpha > 0.2$ warrants per-example audit before architecture substitution, as multiplicity at this level means $>$20\% of examples change outcome; (2) low-Jaccard pairs maximize ensemble complementarity---majority vote fails despite 15--30\% disagreement, but oracle accuracy reveals $+7$--$14$\,pp of untapped gain. Preliminary results suggest rescue-threshold routing may partially exploit this complementarity on high-$\alpha$ tasks ($+5.3$\,pp on LAMBADA; \S\ref{ssec:per_example}), but further validation across tasks and scales is needed.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22440b88-a5cd-4653-875b-982dcbedad81",
  "isSidechain": true,
  "promptId": "42028348-629d-494c-9ba6-5ed1efbe2bc1",
  "agentId": "aa0c4d7f41c26a15c",
  "type": "user",
  "uuid": "f66c140d-1830-4793-ac32-a7c7e79f44e1",
  "sourceToolAssistantUUID": "22440b88-a5cd-4653-875b-982dcbedad81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "a02ce5b1-88a8-4060-9e99-0b93ad72b89c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-juggling-wozniak"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T15:30:14.772Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T4XWxAFgyYG6qCpBLe3Tiw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f66c140d-1830-4793-ac32-a7c7e79f44e1",
  "isSidechain": true,
  "agentId": "aa0c4d7f41c26a15c",
  "requestId": "req_011CbKjrJx4TUukME28GUmex",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6fe6da71-3762-45cd-a56a-0df739f1ca94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "a02ce5b1-88a8-4060-9e99-0b93ad72b89c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-juggling-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WzqX8wdjrXjnqT7ekCcz93",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39918,
      "cache_read_input_tokens": 0,
      "output_tokens": 416,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 39918
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 416,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 39918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 39918,
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

_source line 12 · 2026-05-23T15:30:14.785Z_

<details><summary>↩ Tool result · `toolu_01T4XWxAFgyYG6qCpBLe3Tiw`</summary>

```text
1	\section{Related Work}
2	
3	\paragraph{Hybrid Recurrent Architectures.}
4	The design space for combining attention with recurrence spans layer-level interleaving \citep[Jamba;][]{lieber2024jamba}, local attention pairing \citep[Griffin, RecurrentGemma;][]{de2024griffin,botev2024recurrentgemma}, matrix-valued recurrence \citep[RWKV-6;][]{peng2024eagle}, within-head mixing \citep[Hymba;][]{dong2024hymba}, and unbounded-context hybrid SSMs \citep[Samba;][]{ren2024samba}. H3 \citep{fu2023hungry} and Hyena \citep{poli2023hyena} establish early design points in the hybrid space with gated convolutions and subquadratic operators. Mamba-2 \citep{dao2024mamba2} establishes a duality between structured state spaces and attention; Mamba-3 \citep{lahoti2026mamba3} extends the design further, while \citet{ali2025hidden} reveal implicit attention within Mamba. Comparative evaluations confirm that hybrids outperform pure Transformers and SSMs at scale \citep{waleffe2024empirical}, and that even one attention layer enables content-based routing \citep{basu2026routing}. Recent theoretical work establishes a provable expressiveness hierarchy between hybrid and pure linear attention \citep{ye2026provable}, providing formal grounding for the architectural differences we characterize at the per-example level. \citet{wang2025hybrid} provide the controlled model zoo we use, holding training conditions constant while varying architecture and attention ratio.
5	
6	\paragraph{Linear Recurrent Models.}
7	Our three recurrent backbones represent distinct gating strategies within the linear recurrence family: RetNet \citep{sun2023retnet} uses multi-scale exponential decay, HGRN2 \citep{qin2024hgrn2} applies gated state expansion, and GatedDeltaNet \citep{yang2024gateddeltanet} combines gated updates with delta rules. These descend from S4 \citep{gu2022s4} and Mamba \citep{gu2024mamba}, which introduced structured state spaces and input-dependent selection, respectively, and connect to linear attention \citep{katharopoulos2020transformers} through the state-space--attention duality of Mamba-2.
8	
9	\paragraph{Underspecification and Predictive Multiplicity.}
10	\citet{damour2022underspecification} formalized underspecification: equivalent aggregate performance can mask per-prediction divergence. Concrete NLP instances include seed-dependent BERT disagreement \citep{mccoy2020berts,sellam2022multiberts,dodge2020finetuning} and the four-phase convergence pattern of autoregressive LMs \citep{fehlauer2025convergence}. \citet{marx2020predictive} introduced predictive multiplicity as a complementary lens (extending prediction churn; \citealt{milanifard2016launch}), showing that near-optimal models produce conflicting per-example predictions; extensions address probabilistic classification \citep{watson2023predictive}, Rashomon capacity \citep{hsu2022rashomon}, reconciliation \citep{du2025reconciling,haghighat2026resolving}, and cross-model disagreement as a correctness signal \citep{gorbett2026crossmodel}. \citet{swayamdipta2020dataset} characterize examples via training dynamics (variability across epochs); our decomposition operates at deployment time across architectures with no training signal. \citet{niven2019probing} show that benchmark artifacts can inflate per-example agreement; our cross-benchmark variation ($\alpha = 0.14$--$0.30$) suggests the patterns we observe are not driven by a single artifact type. \citet{fort2019deep} provide a loss landscape perspective on deep ensembles, showing that diverse architectures explore distinct modes and produce disagreement on individual predictions; standard ensemble diversity measures \citep{kuncheva2003measures}, including the Q-statistic \citep{brown2005diversity}, quantify such disagreement; Jaccard similarity is one instance. \citet{black2022model} survey the model multiplicity landscape, \citet{ganesh2025systemizing} systemize sources of arbitrariness, and \citet{cooper2024arbitrariness} connect predictive arbitrariness to fairness. These studies attribute divergence to initialization noise or the near-optimal set within a single architecture. Whereas Rashomon-set analyses \citep{fisher2019all,semenova2022existence,jain2025allocation} examine variation among near-optimal models within a single hypothesis class, we study variation across architectural families under matched training conditions. We extend this line of work to a new source of variation, the recurrent backbone itself, showing that architectural variation is associated with per-example multiplicity that varies systematically by task type. Unlike ensemble diversity, which is designed into the system, the per-example divergence we observe emerges from architectural choice without explicit diversification. The observation that aggregate-level associations can diverge from individual-level patterns is a well-known statistical phenomenon (ecological fallacy; \citealt{robinson1950ecological}). Our decoupling finding (\S\ref{ssec:decoupling}) is a specific instance: aggregate variance decreases while per-example overlap remains flat. The contribution lies not in the conceptual observation but in its quantitative characterization across architectures and task types.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fe6da71-3762-45cd-a56a-0df739f1ca94",
  "isSidechain": true,
  "promptId": "42028348-629d-494c-9ba6-5ed1efbe2bc1",
  "agentId": "aa0c4d7f41c26a15c",
  "type": "user",
  "uuid": "f642e8bd-e5b2-413d-9fdb-3ca72c8acf5b",
  "sourceToolAssistantUUID": "6fe6da71-3762-45cd-a56a-0df739f1ca94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "a02ce5b1-88a8-4060-9e99-0b93ad72b89c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-juggling-wozniak"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-23T15:30:16.204Z_

Now let me check if there are any additional sections, appendices, or related materials:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f642e8bd-e5b2-413d-9fdb-3ca72c8acf5b",
  "isSidechain": true,
  "agentId": "aa0c4d7f41c26a15c",
  "requestId": "req_011CbKjrXsweXdVUCju9DDpu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bd7ae283-bdf5-4105-88c4-6c2d303c024d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "a02ce5b1-88a8-4060-9e99-0b93ad72b89c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-juggling-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UBhCfnKF348qjkadVKoc4L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7929,
      "cache_read_input_tokens": 39918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7929,
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

_source line 14 · 2026-05-23T15:30:16.993Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KHH7uqVMszvXaNGFTpH8qj`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper -name \"*.tex\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd7ae283-bdf5-4105-88c4-6c2d303c024d",
  "isSidechain": true,
  "agentId": "aa0c4d7f41c26a15c",
  "requestId": "req_011CbKjrXsweXdVUCju9DDpu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c2031a05-3b29-4e3a-bb3e-c3e7172d2ae6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "a02ce5b1-88a8-4060-9e99-0b93ad72b89c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-juggling-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UBhCfnKF348qjkadVKoc4L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7929,
      "cache_read_input_tokens": 39918,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7929
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 114,
          "cache_read_input_tokens": 39918,
          "cache_creation_input_tokens": 7929,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7929,
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

_source line 15 · 2026-05-23T15:30:17.154Z_

<details><summary>↩ Tool result · `toolu_01KHH7uqVMszvXaNGFTpH8qj`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/arr_checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2031a05-3b29-4e3a-bb3e-c3e7172d2ae6",
  "isSidechain": true,
  "promptId": "42028348-629d-494c-9ba6-5ed1efbe2bc1",
  "agentId": "aa0c4d7f41c26a15c",
  "type": "user",
  "uuid": "9c1f785e-35b7-4c94-8dc6-538015ae9ea0",
  "sourceToolAssistantUUID": "c2031a05-3b29-4e3a-bb3e-c3e7172d2ae6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "a02ce5b1-88a8-4060-9e99-0b93ad72b89c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-juggling-wozniak"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-23T15:30:18.475Z_

Let me also check the experiments section and appendix for additional details on evaluation setup:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c1f785e-35b7-4c94-8dc6-538015ae9ea0",
  "isSidechain": true,
  "agentId": "aa0c4d7f41c26a15c",
  "requestId": "req_011CbKjrhj2NdJFnZQmRncM4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f816ae87-7649-4329-b3ad-1273bef6bb94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "a02ce5b1-88a8-4060-9e99-0b93ad72b89c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-juggling-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QmVhFPmryhb5C1cCtnQv13",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 540,
      "cache_read_input_tokens": 47847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 540,
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

_source line 17 · 2026-05-23T15:30:18.907Z_

<details open><summary>🔧 Tool call — Read · `toolu_013FbbwqWXciDiXdmYfv9iFU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f816ae87-7649-4329-b3ad-1273bef6bb94",
  "isSidechain": true,
  "agentId": "aa0c4d7f41c26a15c",
  "requestId": "req_011CbKjrhj2NdJFnZQmRncM4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cbf8be6d-2432-4501-89c2-1ffff6ffa8f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "a02ce5b1-88a8-4060-9e99-0b93ad72b89c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-juggling-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QmVhFPmryhb5C1cCtnQv13",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 540,
      "cache_read_input_tokens": 47847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 540,
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

_source line 18 · 2026-05-23T15:30:18.915Z_

<details><summary>↩ Tool result · `toolu_013FbbwqWXciDiXdmYfv9iFU`</summary>

```text
1	\section{Experiments}\label{sec:experiments}
2	
3	Using the model zoo of \citet{wang2025hybrid} (\S\ref{ssec:model_zoo}), we evaluate all 30 configurations on 10 benchmarks plus supplementary COPA ($n = 100$) at 1.3B scale unless noted. Results at 340M appear in scale analyses. Recall: h$k$-1 denotes one attention layer per $k{+}1$ layers; h3-1 = 25\% attention.
4	
5	\begin{table*}[t]
6	\centering
7	\caption{Cross-architecture convergence across benchmarks (1.3B scale). $\rho$: Spearman correlation between attention ratio and cross-architecture standard deviation $\sigma$ across five configurations. $p$: exact permutation test (two-tailed, 120 permutations). $\sigma$ values reported $\times 10^{2}$ (accuracy percentage points). Ratio: $\sigma_{\text{pure}} / \sigma_{\text{h3-1}}$. \textbf{Bold}: only benchmark with $\rho = -1.0$. HellaSwag evaluated using normalized accuracy (acc\_norm), the standard metric for this benchmark.}
8	\label{tab:convergence}
9	\begin{tabular}{llrrrrr}
10	\toprule
11	Benchmark & Category & $\rho$ & $p$ & $\sigma_{\text{pure}}$ & $\sigma_{\text{h3-1}}$ & Ratio \\
12	\midrule
13	\textbf{LAMBADA$^{\ddagger}$} & \textbf{Retrieval} & $\mathbf{-1.0}$ & \textbf{.017} & \textbf{2.41} & \textbf{0.49} & \textbf{4.87} \\
14	\quad\emph{(excl.\ GDN)} & & $-0.7$ & .233 & --- & --- & --- \\
15	BoolQ & Comprehension & $0.2$ & .783 & 1.63 & 2.36 & 0.69 \\
16	ARC-C & Reasoning & $0.6$ & .350 & 0.96 & 1.32 & 0.72 \\
17	HellaSwag & Reasoning & $0.4$ & .517 & 1.17 & 1.22 & 0.96 \\
18	PIQA & Reasoning & $-0.5$ & .450 & 0.54 & 0.34 & 1.59 \\
19	WinoGrande & Reasoning & $0.1$ & .950 & 0.67 & 0.78 & 0.86 \\
20	ARC-E & Mixed & $-0.7$ & .233 & 1.00 & 0.13 & 7.70 \\
21	MMLU & Mixed & $-0.7$ & .233 & 0.92 & 0.41 & 2.27 \\
22	SciQ & Mixed & $0.1$ & .950 & 0.87 & 0.74 & 1.19 \\
23	XStoryCloze & Mixed & $-0.6$ & .350 & 0.82 & 0.55 & 1.49 \\
24	\midrule
25	COPA$^{\dagger}$ & Reasoning & $-0.67$ & .267 & 2.63 & 0.47 & 5.57 \\
26	\bottomrule
27	\multicolumn{7}{l}{\footnotesize $^{\dagger}$Supplementary ($n = 100$); excluded from multiple comparison correction.} \\
28	\multicolumn{7}{l}{\footnotesize $^{\ddagger}$GDN h3-1 uses 16 attention heads; all other configurations use 32 (\S\ref{ssec:robustness}).} \\
29	\multicolumn{7}{@{}p{\textwidth}@{}}{\footnotesize Bonferroni-adjusted $p = .017 \times 10 = .170$ (all-10-benchmark correction). \textbf{Power is limited: only $|\rho| = 1.0$ achieves $p < .05$ at $n = 5$.}}
30	\end{tabular}
31	\end{table*}
32	
33	\subsection{Per-Example Divergence}\label{ssec:per_example}
34	
35	Do architectures converge by improving on the same examples? We compare each architecture's pure-recurrent baseline against its h3-1 hybrid on 5{,}153 LAMBADA examples, classifying each as helped (correct only in hybrid), hurt (correct only in pure), or unchanged. Although the decomposition is binary, we verify below that it captures genuine separation in the continuous confidence space (Cohen's $d = 0.73$--$0.92$ between helped and hurt on LAMBADA; cross-benchmark details in Appendix~\ref{app:cm_cross}). This binarization discards confidence magnitude (a transition from 0.51 to 0.49 is treated identically to one from 0.99 to 0.01), so we supplement it with continuous confidence margin analysis (Appendix~\ref{app:confidence_margin}) and verify that low Jaccard persists under continuous thresholds (Appendix~\ref{app:continuous_jaccard}).
36	
37	Each architecture displays a distinct profile of per-example changes. GDN loses a net 153 examples (462 helped, 615 hurt), RetNet loses 69 (426/495), and HGRN2 gains 153 (548/395). HGRN2 is the only architecture for which adding attention yields a net per-example benefit. Pairwise Jaccard similarity is low: mean $\bar{J} \leq 0.10$, indicating ${\sim}90$\% non-overlap. Overlap significantly exceeds the independence baseline ($J_{\text{null}} \approx 0.05$, all $z > 5.9$, $p < .0001$; Appendix~\ref{app:jaccard_permutation}), but normalizing by $J_{\max}$, observed overlap reaches only 6--7\% of the achievable range above chance (Appendix~\ref{app:normalized_es}), confirming that low Jaccard cannot be attributed to set-size constraints.
38	
39	\paragraph{Confidence margin predictor.} Pure-model confidence on the target token predicts which examples will be affected (AUC 0.70--0.74; Appendix~\ref{app:confidence_margin}): rescue thresholds are architecture-invariant (1\% spread) but disruption thresholds vary 47\%, explaining cross-architecture Jaccard divergence (Appendix~\ref{app:prediction_framework}). Calibration differences account for less than half the threshold spread (Appendix~\ref{app:calibration}). The rescue pattern generalizes across three benchmarks ($d = 0.13$--$0.60$; Appendix~\ref{app:cm_cross}); disruption is weaker on reasoning tasks (Appendix~\ref{app:boolq}). This structured disagreement constitutes predictive multiplicity \citep{marx2020predictive} under architectural variation \citep[cf.][]{damour2022underspecification}.
40	
41	\paragraph{Confidence-based routing.} As an illustrative case study, the rescue-threshold asymmetry suggests a practical routing strategy: for each example, select the architecture whose pure-model confidence best predicts successful rescue. On LAMBADA, rescue-threshold routing achieves 56.2\% accuracy versus 50.9\% for majority vote ($+5.3$\,pp, SD $= 0.8$\,pp across 10 splits), extracting 36\% of the oracle gap (oracle = 65.5\%). On ARC-Easy, gains are modest ($+1.0$\,pp, SD $= 0.9$\,pp); on HellaSwag and PIQA, routing provides no benefit. We note that confidence-weighted majority vote and other ensemble strategies may provide comparable or superior gains; systematic comparison is left to future work. Using 10-repeat 50/50 cross-validated splits, routing works when multiplicity is high ($\alpha = 0.30$, LAMBADA) and a clear rescue-threshold signal exists, but fails when multiplicity is low ($\alpha = 0.14$, PIQA).
42	
43	\paragraph{Multiplicity variation.} Extending the per-example analysis to HellaSwag ($N = 10{,}042$) and PIQA ($N = 1{,}838$) reveals that predictive multiplicity varies systematically across tasks (Table~\ref{tab:multiplicity}). The ambiguity $\alpha$ \citep{marx2020predictive} ranges from 0.14 (PIQA) through 0.15 (HellaSwag) and 0.21 (ARC-Easy) to 0.30 (LAMBADA), forming a task-dependent variation. Format does not drive multiplicity: HellaSwag (four-way) and PIQA (two-choice) produce nearly identical $\alpha$ despite different formats. Bootstrap 95\% CIs confirm the ordering (all non-overlapping except PIQA--HellaSwag; Appendix, Table~\ref{tab:arceasy_ambiguity}). Moreover, $\alpha$ does not significantly correlate with task accuracy (Spearman $\rho = -0.60$, $p = .24$). Pairwise Jaccard remains uniformly low ($\bar{J} \leq 0.10$, all $p < .01$ across four benchmarks), indicating that architectures affect different examples regardless of how many examples are affected. Within each benchmark, $\alpha$ is stable across attention ratios (variation $< 0.03$), but differs $2\times$ across task types (from reasoning to retrieval), confirming that multiplicity magnitude depends on task, not attention dose \citep[cf.][]{gorbett2026crossmodel}. PIQA (0.14) and HellaSwag (0.15) share a reasoning-task floor, while retrieval (LAMBADA, 0.30) and mixed (ARC-Easy, 0.21) tasks produce higher values.
44	
45	\begin{table}[t]
46	\centering
47	\small
48	\caption{Predictive multiplicity at 1.3B. $\alpha$: ambiguity at h3-1 \citep{marx2020predictive}. $\bar{J}$: mean pairwise Jaccard of helped~(h) and hurt~(u) sets, averaged across four hybrid attention ratios and three architecture pairs. $\rho_\alpha$: Spearman $\rho$ between attention ratio and $\alpha$. Benchmarks ordered by $\alpha$.}
49	\label{tab:multiplicity}
50	\begin{tabular}{@{}lrcccc@{}}
51	\toprule
52	 & $N$ & $\alpha$ & $\bar{J}_{h}$ & $\bar{J}_{u}$ & $\rho_\alpha$ \\
53	\midrule
54	PIQA & 1838 & .14 & .091 & .094 & $0.0$ \\
55	HellaSwag & 10042 & .15 & .095 & .085 & $0.1$ \\
56	ARC-Easy & 2376 & .21 & .092 & .099 & $-0.2$ \\
57	LAMBADA & 5153 & .30 & .096 & .091 & $-0.6$ \\
58	\bottomrule
59	\end{tabular}
60	\par\vspace{1pt}
61	{\footnotesize Within-benchmark $\alpha$ variation $< 0.03$ across ratios. BoolQ, WinoGrande: Appendix~\ref{app:boolq}, \ref{app:winogrande}.}
62	\end{table}
63	
64	\subsection{Aggregate Trends and Per-Example Independence}\label{ssec:decoupling}
65	
66	The per-example findings above raise a natural question: when aggregate metrics converge, does this reflect agreement on the same examples? Table~\ref{tab:convergence} provides context. Only LAMBADA shows a monotonically decreasing variance pattern ($\rho = -1.0$, Bonferroni-adjusted $p = .170$; excluding GDN, whose h3-1 uses 16 rather than 32 attention heads: $\rho = -0.7$, $p = .233$; observed at 1.3B, absent at 340M; Appendix~\ref{app:convergence_detail}, Figure~\ref{fig:task_specificity}). This is a suggestive but underpowered secondary observation ($n = 5$; the test has negligible power for $|\rho| < 1.0$). Given the limited statistical power, non-significant correlations on other benchmarks should not be interpreted as absence of association. LAMBADA relies purely on in-context retrieval without external knowledge or multi-step reasoning, making it the task most directly aligned with attention's role in context access---a plausible explanation for why convergence is strongest here.
67	
68	\begin{figure}[t]
69	\centering
70	\includegraphics[width=\columnwidth]{figures/fig2_task_specificity.pdf}
71	\caption{Spearman $\rho$ between attention ratio and cross-architecture $\sigma$ for each benchmark at 1.3B scale. LAMBADA ($\rho = -1.0$; BCa 95\% CI $[-1.0,\,-0.7]$, heuristic) is the only benchmark with a negative correlation whose confidence interval excludes zero. Benchmarks are grouped by task category. Bootstrap CI is heuristic given $n = 3$ architectures.}
72	\label{fig:task_specificity}
73	\end{figure}
74	
75	\begin{figure*}[t]
76	\centering
77	\includegraphics[width=\textwidth]{figures/jaccard_heatmap_5arch.pdf}
78	\caption{Pairwise Jaccard heatmap across five architectures (340M, h3-1), where helped (hurt) examples are those correct only with (without) attention. Upper triangle: $J_{\text{helped}}$; lower triangle: $J_{\text{hurt}}$. All values $\leq 0.14$, all permutation tests $p \leq .002$. HellaSwag and PIQA results in Appendix~\ref{app:extended_arch}.}
79	\label{fig:jaccard_heatmap_5arch}
80	\end{figure*}
81	
82	Even on LAMBADA, the answer is no. Aggregate variance decreases while per-example overlap remains constant as attention ratio increases (Figure~\ref{fig:decoupling}).
83	
84	Cross-architecture $\sigma$ decreases from 0.024 (pure) to 0.005 (h3-1) (Bonferroni-adjusted $p = .170$; non-significant), while pairwise Jaccard saturates (i.e., remains at a low plateau with no further increase) at the first attention level ($\bar{J} \approx 0.095$)---indicating that each architecture's per-example response to attention is largely idiosyncratic. The observed $\bar{J}$ reaches only 6--7\% of the achievable range above chance ($J_{\max} \approx 0.78$--$0.92$), ruling out ceiling constraints (\S\ref{ssec:per_example}).
85	
86	This saturation generalizes beyond LAMBADA (Figure~\ref{fig:jaccard_saturation}): on all four main benchmarks, mean pairwise Jaccard shows no significant trend with attention ratio (all $\rho \leq 0.80$, $p \geq 0.333$), with values uniformly between 0.08 and 0.11.
87	
88	\begin{figure}[t]
89	\centering
90	\includegraphics[width=\columnwidth]{figures/fig4_jaccard_saturation.pdf}
91	\caption{Cross-benchmark Jaccard saturation. Mean pairwise $\bar{J}$ (averaged over helped and hurt sets) remains flat across attention ratios on all four benchmarks (all $\rho \leq 0.80$, $p \geq .333$), confirming that per-example divergence saturates immediately regardless of task type.}
92	\label{fig:jaccard_saturation}
93	\end{figure}
94	
95	Bootstrap 95\% CIs confirm non-overlapping $\sigma$ between pure and h3-1 but completely overlapping Jaccard across all hybrid ratios (\S\ref{ssec:statistical_methods}). Figure~\ref{fig:jaccard_hierarchy} shows a three-tier Jaccard hierarchy: independence baseline (${\sim}0.05$), cross-architecture (${\sim}0.10$, $2\times$ baseline), and within-architecture (${\sim}0.33$, $3\times$ cross-architecture; Appendix~\ref{app:within_arch_stability}). Pythia 70M seed calibration produces a comparable within-seed level ($J = 0.27$--$0.39$; Appendix~\ref{app:seed_calibration}), consistent with architecture-driven divergence, though matched multi-seed experiments would be needed for definitive evidence.
96	
97	\begin{figure}[t]
98	\centering
99	\includegraphics[width=\columnwidth]{figures/fig_jaccard_hierarchy.pdf}
100	\caption{Jaccard hierarchy on LAMBADA (1.3B). Cross-architecture overlap ($\bar{J} \approx 0.09$) is $2\times$ the independence baseline but only one-third of within-architecture overlap ($\bar{J} \approx 0.33$). Pythia 70M within-seed Jaccard (different scale) falls at a comparable level. Error bars show the helped--hurt range.}
101	\label{fig:jaccard_hierarchy}
102	\end{figure}
103	
104	Attention weight analysis (Appendix~\ref{app:attention_patterns}) shows GDN and RetNet produce nearly identical attention distributions (cosine 0.995) yet differ in per-example effects, suggesting these originate in the recurrent layers. The four-benchmark variation (Table~\ref{tab:multiplicity}) confirms independence: LAMBADA ($\alpha = 0.30$) is the only benchmark showing variance reduction despite having the highest multiplicity, while PIQA ($\alpha = 0.14$) and HellaSwag ($\alpha = 0.15$) show no variance reduction with the lowest multiplicity.
105	
106	Cross-scale analysis confirms scale-robustness: pairwise Jaccard is stable ($\bar{J} = 0.08$--$0.10$ at both scales), though $\alpha$ is systematically higher at 340M ($\Delta \leq 8$\,pp). At 340M, aggregate variance reduction is absent ($\rho = -0.50$, $p = .45$), suggesting that the \emph{pattern} of multiplicity reflects structural differences while absolute magnitude is modulated by capacity (Appendix~\ref{app:scale_per_example}). Future work with additional architectures or attention ratios could employ mixed-effects models to improve statistical power beyond the $n = 5$ rank-based tests used here.
107	
108	\subsection{Robustness}\label{ssec:robustness}
109	
110	Removing GDN weakens the LAMBADA variance reduction pattern ($\rho = -0.7$, $p = .233$) and reverses MMLU's ($\rho = +0.6$), both driven by GDN's 16-head configuration (vs.\ 32 in others; Appendix~\ref{app:gdn_confound}). The RetNet--HGRN2 pair preserves decoupling ($\sigma \leq 0.008$, $J = 0.086$--$0.108$). The aggregate variance pattern is therefore dependent on GDN inclusion; the decoupling result is not. Five-architecture validation at 340M (GLA, DeltaNet added) confirms $J \leq 0.14$ across all ten pairs and four benchmarks (all $p < .01$; Figure~\ref{fig:jaccard_heatmap_5arch}; Appendix~\ref{app:extended_arch}). Three-architecture results are stable across both 340M and 1.3B scales (Jaccard $\approx$ 0.08--0.10), providing indirect support for scale robustness. Full sensitivity analyses appear in Appendix~\ref{app:sensitivity}.
111	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cbf8be6d-2432-4501-89c2-1ffff6ffa8f5",
  "isSidechain": true,
  "promptId": "42028348-629d-494c-9ba6-5ed1efbe2bc1",
  "agentId": "aa0c4d7f41c26a15c",
  "type": "user",
  "uuid": "9c81bb38-48ab-4be1-82b3-9d2316ef8f92",
  "sourceToolAssistantUUID": "cbf8be6d-2432-4501-89c2-1ffff6ffa8f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "a02ce5b1-88a8-4060-9e99-0b93ad72b89c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-juggling-wozniak"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T15:30:19.062Z_

<details open><summary>🔧 Tool call — Read · `toolu_019YMibnKCZBMAur3KGMRbCV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c81bb38-48ab-4be1-82b3-9d2316ef8f92",
  "isSidechain": true,
  "agentId": "aa0c4d7f41c26a15c",
  "requestId": "req_011CbKjrhj2NdJFnZQmRncM4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b222c678-f987-4cf0-986c-d3a46f013365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "a02ce5b1-88a8-4060-9e99-0b93ad72b89c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-juggling-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QmVhFPmryhb5C1cCtnQv13",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 540,
      "cache_read_input_tokens": 47847,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 540
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 186,
          "cache_read_input_tokens": 47847,
          "cache_creation_input_tokens": 540,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 540,
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

_source line 20 · 2026-05-23T15:30:19.307Z_

<details><summary>↩ Tool result · `toolu_019YMibnKCZBMAur3KGMRbCV`</summary>

```text
1	% Appendix sections for the paper.
2	
3	\section{Confirmatory and Exploratory Analyses}\label{app:benchmark_details}
4	
5	The task taxonomy used in \S\ref{ssec:task_taxonomy} was defined prior to running any convergence analyses. Each benchmark was assigned to exactly one of four categories based on the primary cognitive demand of the task:
6	
7	\begin{itemize}
8	    \item \textbf{Retrieval}: tasks requiring prediction from long-range context without multi-step reasoning (LAMBADA).
9	    \item \textbf{Comprehension}: reading comprehension with explicit passage support (BoolQ).
10	    \item \textbf{Reasoning}: tasks requiring commonsense inference or multi-step reasoning (HellaSwag, ARC-Challenge, WinoGrande, PIQA).
11	    \item \textbf{Mixed}: tasks combining retrieval, comprehension, and reasoning demands (ARC-Easy, MMLU, SciQ, XStoryCloze).
12	\end{itemize}
13	
14	\paragraph{Confirmatory benchmark set.} Six benchmarks were designated as confirmatory for Bonferroni correction: LAMBADA, HellaSwag, ARC-Challenge, WinoGrande, ARC-Easy, and MMLU. These were selected as representative of retrieval, reasoning, and mixed categories before any convergence analysis was performed. The taxonomy and benchmark selection were fixed before analysis as an informal pre-analysis plan; we describe this as a confirmatory/exploratory split rather than a formal pre-registration, since no external timestamp exists. The main text applies the more conservative all-10-benchmark correction (Bonferroni-adjusted $p = .017 \times 10 = .170$). \textbf{Sensitivity:} correcting across only the six confirmatory benchmarks yields adjusted $p = .017 \times 6 = .100$, still above conventional significance.
15	
16	\paragraph{One-sided test.} If one adopts the prior that attention should reduce cross-architecture variance, the one-sided permutation $p$-value for LAMBADA is $1/120 \approx 0.0083$. Under 10-benchmark Bonferroni correction, this yields an adjusted $p = 0.083$, above the conventional threshold. We report two-sided tests throughout the main text as the more conservative choice; the one-sided result is noted here for completeness.
17	
18	\paragraph{Exploratory benchmarks.} Four additional benchmarks (BoolQ, PIQA, SciQ, XStoryCloze) were added as exploratory tests. All benchmarks share the same 10-benchmark correction (adjusted threshold $\alpha / 10 = 0.005$) and the four exploratory benchmarks are labeled as such throughout the paper. The all-10 Bonferroni correction reported in the main text is the only correction used for inference; the exploratory 6-benchmark subset correction in this appendix is provided for transparency.
19	
20	\paragraph{Supplementary benchmark.} COPA ($n = 100$) is treated as supplementary due to its small sample size. It is excluded from both correction families and reported separately with the $\dagger$ annotation in Table~\ref{tab:convergence}.
21	
22	\section{Convergence Detail}\label{app:convergence_detail}
23	
24	% Figure moved to main text (\S\ref{ssec:decoupling}).
25	
26	Beyond LAMBADA ($\rho = -1.0$), two benchmarks show moderate negative correlations that do not reach significance: ARC-Easy and MMLU (both $\rho = -0.7$, $p = .233$). Both are classified as ``Mixed'' tasks combining retrieval with reasoning demands. The sensitivity analysis (Appendix~\ref{app:sensitivity}) shows that MMLU's correlation reverses upon GDN exclusion ($\rho = +0.6$), indicating dependence on a single architecture; ARC-Easy's correlation is more stable. COPA ($n = 100$; supplementary) shows $\rho = -0.67$ with a large $\sigma$ ratio (5.57), consistent with LAMBADA's pattern but unreliable due to small sample size.
27	
28	Several benchmarks show positive or near-zero $\rho$ (BoolQ: $+0.2$; ARC-C: $+0.6$; HellaSwag: $+0.4$; WinoGrande: $+0.1$; SciQ: $+0.1$), indicating that attention does not systematically reduce cross-architecture variance on reasoning or comprehension tasks. The contrast with LAMBADA is consistent with attention's convergence benefit being specific to tasks requiring direct token-level recall \citep{arora2024zoology,arora2024based} rather than multi-step inference.
29	
30	\paragraph{Regression to the mean.} The direction of LAMBADA's aggregate convergence is consistent with regression to the mean: GDN (highest pure accuracy, 0.543) declines to 0.513 under h3-1, while HGRN2 (lowest, 0.484) rises to 0.514, yielding a $5\times$ $\sigma$ compression ($0.024 \to 0.005$). However, three observations argue against a purely statistical artifact. First, the $5\times$ reduction in cross-architecture $\sigma$ far exceeds typical regression amplitudes. Second, the direction is entirely determined by architecture identity, not random fluctuation: HGRN2 accuracy increases monotonically across all attention ratios, while GDN decreases monotonically---a pattern inconsistent with noise-driven mean reversion. Third, per-example analysis (\S\ref{ssec:per_example}) reveals architecture-specific patterns: GDN's net $-153$ examples and HGRN2's net $+153$ examples reflect distinct helped/hurt profiles with low cross-architecture Jaccard overlap, indicating that the aggregate convergence arises from structured, architecture-dependent per-example changes rather than symmetric regression.
31	
32	\section{Scale-Dependent Convergence}\label{app:scale_convergence}
33	
34	At 1.3B parameters, LAMBADA convergence is monotonic: $\sigma$ decreases at every attention level from 0\% through 25\% ($\rho = -1.0$). At 340M, convergence is partial: $\sigma$ reaches a maximum reduction of 56\% at intermediate attention ratios but rebounds at h3-1, yielding a net endpoint reduction of 36\%. The trajectory is non-monotonic, and the highest-attention model does not achieve the lowest cross-architecture variance. One possible interpretation is that at smaller scale, the capacity overhead of attention layers creates interference that offsets the retrieval benefit.
35	
36	This contrast is a preliminary observation from two data points (not a scaling law). Despite the aggregate divergence at 340M, mean pairwise Jaccard is similar at both scales ($J \approx 0.09$), extending the decoupling observation (\S\ref{ssec:decoupling}) to the scale dimension.
37	
38	\section{Sensitivity Analyses}\label{app:sensitivity}
39	
40	\subsection{Bootstrap Confidence Intervals}
41	
42	We construct 95\% bootstrap confidence intervals for the Spearman $\rho$ between attention ratio and cross-architecture $\sigma$ on LAMBADA using 10{,}000 resamples at the architecture level ($n = 3$ architectures). Of these resamples, 11.25\% are degenerate: they consist of same-architecture triplicates, which produce a constant $\sigma$ vector and therefore an undefined $\rho$ (division by zero in the rank correlation formula). These are excluded from the confidence interval computation because they carry no information about the correlation, not because they represent $\rho = 0$.
43	
44	The BCa (bias-corrected and accelerated) correction degenerates at the $\rho = -1.0$ boundary because the acceleration parameter requires finite jackknife variance, which collapses when the point estimate is at the distributional limit. We therefore report percentile confidence intervals instead. From the 88.75\% informative resamples, the 95\% percentile CI is $[-1.0,\,-0.7]$, which excludes zero.
45	
46	\subsection{GDN Exclusion Sensitivity}
47	
48	The GDN h3-1 configuration uses 16 attention heads rather than 32 (see Appendix~\ref{app:gdn_confound}). To assess the influence of this confound, we recompute all convergence correlations after excluding GDN, leaving two architectures (RetNet, HGRN2) at five attention ratios.
49	
50	Table~\ref{tab:gdn_sensitivity} reports the results for benchmarks where the correlation changes by $|\Delta\rho| \geq 0.3$. LAMBADA weakens from $\rho = -1.0$ to $\rho = -0.7$ ($p = .233$), consistent with GDN contributing to the convergence signal. MMLU reverses from $\rho = -0.7$ to $\rho = +0.6$, confirming that the moderate negative correlation on MMLU depends on GDN's inclusion and should not be interpreted as evidence of convergence.
51	
52	\begin{table}[ht]
53	\centering
54	\small
55	\caption{Effect of GDN exclusion on Spearman $\rho$ (attention ratio vs.\ cross-architecture $\sigma$) at 1.3B scale. Only benchmarks with $|\Delta\rho| \geq 0.3$ shown.}
56	\label{tab:gdn_sensitivity}
57	\begin{tabular}{lrrrr}
58	\toprule
59	Benchmark & $\rho_{\text{all}}$ & $\rho_{\text{no-GDN}}$ & $\Delta\rho$ & $p_{\text{no-GDN}}$ \\
60	\midrule
61	LAMBADA & $-1.0$ & $-0.7$ & $+0.3$ & .233 \\
62	MMLU & $-0.7$ & $+0.6$ & $+1.3$ & .350 \\
63	\bottomrule
64	\end{tabular}
65	\end{table}
66	
67	\section{GDN Attention Head Confound}\label{app:gdn_confound}
68	
69	In the \citet{wang2025hybrid} model zoo, the GDN h3-1 configuration at 1.3B scale uses 16 attention heads per attention layer, while all other hybrid configurations (across GDN, RetNet, and HGRN2) use 32 attention heads. This is a design choice in the original model zoo, not an error. The reduced head count changes the per-head dimension and may affect the attention capacity of GDN h3-1 relative to other configurations.
70	
71	This confound is relevant because the convergence analysis measures cross-architecture $\sigma$ at each attention ratio. At the h3-1 ratio (25\% attention), GDN's attention layers have a different internal structure than those of RetNet and HGRN2, which could contribute to variance reduction (or inflation) for reasons unrelated to the recurrent--attention interaction under study.
72	
73	The sensitivity analysis in Appendix~\ref{app:sensitivity} shows that removing GDN weakens the LAMBADA convergence correlation from $\rho = -1.0$ to $\rho = -0.7$. This weakening is partially attributable to the reduced sample size ($n = 2$ architectures) and partially to the confound itself. We cannot separate these two effects with the available data.
74	
75	\section{Attention Weight Analysis}\label{app:attention_patterns}
76	
77	We extract attention weight matrices from the 1.3B h3-1 models of all three architectures using forward hooks on each attention layer. While \citet{ali2025hidden} show that SSM layers learn implicit attention patterns, our analysis focuses on the explicit attention layers interleaved within the hybrid architecture. For each layer, we compute the mean attention distribution across all 5{,}153 LAMBADA examples and measure cross-architecture similarity via cosine similarity.
78	
79	\subsection{Cross-Architecture Cosine Similarity}
80	
81	Table~\ref{tab:attn_cosine} reports cosine similarity between mean attention distributions at selected layers and averaged across all layers.
82	
83	\begin{table}[ht]
84	\centering
85	\caption{Cosine similarity between mean attention weight distributions of architecture pairs at selected layers (1.3B h3-1 models on LAMBADA).}
86	\label{tab:attn_cosine}
87	\resizebox{\columnwidth}{!}{%
88	\begin{tabular}{lrrr}
89	\toprule
90	Layer & GDN--RetNet & GDN--HGRN2 & HGRN2--RetNet \\
91	\midrule
92	L2 (early) & 0.995 & 0.244 & 0.196 \\
93	L20 (deep) & 0.986 & 0.942 & 0.943 \\
94	\midrule
95	Mean (all layers) & 0.905 & 0.766 & 0.698 \\
96	\bottomrule
97	\end{tabular}%
98	}
99	\end{table}
100	
101	At layer 2, GDN and RetNet produce nearly identical attention distributions (cosine 0.995), while HGRN2 diverges from both (cosine $< 0.25$). By layer 20, all three architectures converge to similar attention patterns (cosine $> 0.94$). The layer-wise trajectory suggests that early-layer attention patterns are shaped by the preceding recurrent layers (which differ across architectures), while deeper layers converge regardless of the recurrent substrate.
102	
103	\subsection{Helped vs.\ Hurt Attention Entropy}
104	
105	To test whether the attention mechanism itself differs between helped and hurt examples, we compute the Shannon entropy of the attention distribution for each example at each attention layer and compare the mean entropy of helped examples against hurt examples within each architecture.
106	
107	\begin{table}[ht]
108	\centering
109	\caption{Mean attention entropy difference (helped $-$ hurt) averaged across attention layers (1.3B h3-1 models on LAMBADA). Values near zero indicate that the attention mechanism does not discriminate between helped and hurt examples.}
110	\label{tab:attn_entropy}
111	\begin{tabular}{lr}
112	\toprule
113	Architecture & $\Delta H$ (helped $-$ hurt) \\
114	\midrule
115	GDN & $-0.0009$ \\
116	RetNet & $+0.0179$ \\
117	HGRN2 & $+0.0020$ \\
118	\bottomrule
119	\end{tabular}
120	\end{table}
121	
122	GDN and HGRN2 show negligible entropy differences ($|\Delta H| \leq 0.002$). RetNet's $\Delta H = +0.018$ is small in absolute terms but slightly larger; helped examples receive marginally more diffuse attention in RetNet. Across all three architectures, the differences are insufficient to explain the per-example divergence, consistent with per-example effects not being explained by attention weight patterns and likely originating in the recurrent layers.
123	
124	\subsection{Last-5 Attention Mass}
125	
126	We also measure the fraction of attention mass allocated to the last five tokens, which captures whether the attention mechanism concentrates differently on recent context for helped vs.\ hurt examples.
127	
128	\begin{table}[ht]
129	\centering
130	\caption{Mean attention mass on last-5 tokens for helped and hurt examples, averaged across attention layers (1.3B h3-1 models on LAMBADA).}
131	\label{tab:attn_last5}
132	\begin{tabular}{lrr}
133	\toprule
134	Architecture & Helped & Hurt \\
135	\midrule
136	GDN & 0.0834 & 0.0831 \\
137	RetNet & 0.1578 & 0.1591 \\
138	HGRN2 & 0.0453 & 0.0467 \\
139	\bottomrule
140	\end{tabular}
141	\end{table}
142	
143	No architecture shows a meaningful difference in last-5 attention mass between helped and hurt examples (Table~\ref{tab:attn_last5}). This further supports the conclusion that the per-example divergence is not driven by differential attention allocation.
144	
145	\section{Cross-Scale Per-Example Comparisons}\label{app:cross_scale}
146	
147	\subsection{Within-Scale Pairwise Jaccard}
148	
149	Table~\ref{tab:within_scale_jaccard} reports the within-scale pairwise Jaccard similarity between architectures' helped and hurt sets at both scales. Mean values are similar across scales (340M: 0.094/0.090; 1.3B: 0.100/0.093), confirming that per-example architecture specificity is approximately scale-robust.
150	
151	\begin{table}[ht]
152	\centering
153	\small
154	\caption{Within-scale pairwise Jaccard similarity of per-example effects (pure $\to$ h3-1) on LAMBADA. Each row compares the helped (or hurt) sets of two architectures at the same scale.}
155	\label{tab:within_scale_jaccard}
156	\begin{tabular}{llcc}
157	\toprule
158	Scale & Pair & $J_{\text{helped}}$ & $J_{\text{hurt}}$ \\
159	\midrule
160	\multirow{4}{*}{340M} & GDN--RetNet & 0.092 & 0.109 \\
161	& GDN--HGRN2 & 0.084 & 0.075 \\
162	& RetNet--HGRN2 & 0.108 & 0.085 \\
163	& \textit{Mean} & \textit{0.094} & \textit{0.090} \\
164	\midrule
165	\multirow{4}{*}{1.3B} & GDN--RetNet & 0.092 & 0.103 \\
166	& GDN--HGRN2 & 0.100 & 0.089 \\
167	& RetNet--HGRN2 & 0.108 & 0.087 \\
168	& \textit{Mean} & \textit{0.100} & \textit{0.093} \\
169	\bottomrule
170	\end{tabular}
171	\end{table}
172	
173	\subsection{Cross-Scale Pairwise Jaccard}
174	
175	For each architecture, we compare the helped and hurt sets of the pure $\to$ h3-1 transition at 340M and 1.3B scale on LAMBADA.
176	The comparison uses the same classification scheme as \S\ref{ssec:per_example}: an example is ``helped'' if it is correct only in the hybrid variant and ``hurt'' if correct only in the pure baseline.
177	All pairwise Jaccard values fall below 0.10, indicating that scale produces per-example predictive multiplicity analogous to the cross-architecture effect reported in \S\ref{ssec:per_example}.
178	
179	\begin{table}[ht]
180	\centering
181	\caption{Cross-scale pairwise Jaccard similarity of per-example effects (pure $\to$ h3-1) between 340M and 1.3B on LAMBADA. All values below 0.10.}
182	\label{tab:cross_scale_jaccard}
183	\begin{tabular}{llcc}
184	\toprule
185	Architecture & Scale Pair & $J_{\text{helped}}$ & $J_{\text{hurt}}$ \\
186	\midrule
187	GDN & 340M $\leftrightarrow$ 1.3B & 0.047 & 0.087 \\
188	RetNet & 340M $\leftrightarrow$ 1.3B & 0.059 & 0.073 \\
189	HGRN2 & 340M $\leftrightarrow$ 1.3B & 0.089 & 0.055 \\
190	\midrule
191	Mean & & 0.065 & 0.072 \\
192	\bottomrule
193	\end{tabular}
194	\end{table}
195	
196	\section{Per-Example Effect Counts}\label{app:per_example_counts}
197	
198	Table~\ref{tab:per_example} reports the full per-example effect counts for each architecture at 1.3B scale.
199	
200	\begin{table}[ht]
201	\centering
202	\caption{Per-example effects of attention (pure $\to$ h3-1) on 5{,}153 LAMBADA examples at 1.3B scale. $\bar{J}$: mean pairwise Jaccard similarity with other architectures across helped and hurt sets.}
203	\label{tab:per_example}
204	\begin{tabular}{lrrrr}
205	\toprule
206	Architecture & Helped & Hurt & Net & $\bar{J}$ \\
207	\midrule
208	GDN & 462 & 615 & $-$153 & .096 \\
209	RetNet & 426 & 495 & $-$69 & .100 \\
210	HGRN2 & 548 & 395 & $+$153 & .104 \\
211	\bottomrule
212	\end{tabular}
213	\end{table}
214	
215	\section{Normalized Jaccard Effect Size}\label{app:normalized_es}
216	
217	To assess whether low observed Jaccard reflects a floor effect imposed by unequal set sizes, we compute the theoretical upper bound $J_{\max} = \min(|A|,|B|) / \max(|A|,|B|)$ and the normalized effect size $(J_{\text{obs}} - J_{\text{null}}) / (J_{\max} - J_{\text{null}})$, which measures observed overlap as a fraction of the achievable range above chance. Table~\ref{tab:normalized_es} reports per-pair results.
218	
219	\begin{table}[ht]
220	\centering
221	\small
222	\caption{Normalized Jaccard effect size for each architecture pair (1.3B h3-1 on LAMBADA). $J_{\max}$: theoretical upper bound given set sizes. Normalized ES: fraction of achievable overlap above chance.}
223	\label{tab:normalized_es}
224	\resizebox{\columnwidth}{!}{%
225	\begin{tabular}{llcccc}
226	\toprule
227	Category & Pair & $J_{\text{obs}}$ & $J_{\max}$ & $J_{\text{null}}$ & Norm.\ ES \\
228	\midrule
229	Helped & GDN--RetNet & .086 & .922 & .048 & .044 \\
230	 & GDN--HGRN2 & .099 & .843 & .050 & .062 \\
231	 & RetNet--HGRN2 & .108 & .777 & .042 & .090 \\
232	 & \textit{Mean} & \textit{.098} & \textit{.847} & \textit{.047} & \textit{.065} \\
233	\midrule
234	Hurt & GDN--RetNet & .092 & .805 & .056 & .048 \\
235	 & GDN--HGRN2 & .070 & .642 & .043 & .045 \\
236	 & RetNet--HGRN2 & .087 & .798 & .050 & .049 \\
237	 & \textit{Mean} & \textit{.083} & \textit{.748} & \textit{.050} & \textit{.047} \\
238	\bottomrule
239	\end{tabular}%
240	}
241	\end{table}
242	
243	All normalized effect sizes fall below 0.10, confirming that observed overlap reaches only 6--7\% of the theoretical maximum. The low Jaccard values cannot be attributed to set-size constraints.
244	
245	\section{ARC-Easy Per-Example Analysis}\label{app:arceasy}
246	
247	Table~\ref{tab:arceasy_effects} reports per-example effect counts on ARC-Easy ($N = 2{,}376$) at 1.3B scale for each attention ratio. Unlike LAMBADA, ARC-Easy shows no aggregate convergence ($\rho = -0.20$, $p = .783$). HGRN2 is net positive at all ratios; GDN and RetNet are mixed.
248	
249	\begin{table}[ht]
250	\centering
251	\small
252	\caption{Per-example effects on ARC-Easy at 1.3B scale. Net = helped $-$ hurt.}
253	\label{tab:arceasy_effects}
254	\resizebox{\columnwidth}{!}{%
255	\begin{tabular}{llrrr}
256	\toprule
257	Architecture & Ratio & Helped & Hurt & Net \\
258	\midrule
259	\multirow{4}{*}{GDN} & h24-1 & 178 & 185 & $-$7 \\
260	& h12-1 & 176 & 206 & $-$30 \\
261	& h6-1 & 170 & 157 & $+$13 \\
262	& h3-1 & 171 & 180 & $-$9 \\
263	\midrule
264	\multirow{4}{*}{RetNet} & h24-1 & 158 & 168 & $-$10 \\
265	& h12-1 & 163 & 146 & $+$17 \\
266	& h6-1 & 159 & 147 & $+$12 \\
267	& h3-1 & 144 & 184 & $-$40 \\
268	\midrule
269	\multirow{4}{*}{HGRN2} & h24-1 & 160 & 119 & $+$41 \\
270	& h12-1 & 159 & 111 & $+$48 \\
271	& h6-1 & 185 & 118 & $+$67 \\
272	& h3-1 & 164 & 146 & $+$18 \\
273	\bottomrule
274	\end{tabular}%
275	}
276	\end{table}
277	
278	Table~\ref{tab:arceasy_ambiguity} reports the ambiguity $\alpha$ \citep{marx2020predictive} at each attention ratio for all four main benchmarks. Within-benchmark ranges are 0.004 (HellaSwag), 0.011 (PIQA), 0.025 (ARC-Easy), and 0.022 (LAMBADA), all below the 0.03 threshold reported in \S\ref{ssec:per_example}.
279	
280	\begin{table}[ht]
281	\centering
282	\caption{Ambiguity $\alpha$ across attention ratios (1.3B scale). 95\% CI: BCa bootstrap (10{,}000 resamples) at the pure-recurrent configuration.}
283	\label{tab:arceasy_ambiguity}
284	\resizebox{\columnwidth}{!}{%
285	\begin{tabular}{lcccccc}
286	\toprule
287	Benchmark & Pure & h24-1 & h12-1 & h6-1 & h3-1 & 95\% CI (pure) \\
288	\midrule
289	PIQA & .143 & .138 & .132 & .143 & .140 & $[.127,\,.159]$ \\
290	HellaSwag & .148 & .150 & .148 & .146 & .150 & $[.141,\,.155]$ \\
291	ARC-Easy & .205 & .226 & .223 & .201 & .210 & $[.189,\,.221]$ \\
292	LAMBADA & .307 & .300 & .316 & .294 & .296 & $[.294,\,.319]$ \\
293	\bottomrule
294	\end{tabular}%
295	}
296	\end{table}
297	
298	\section{Jaccard Permutation Test}\label{app:jaccard_permutation}
299	
300	To assess whether the observed pairwise Jaccard similarities exceed what would be expected under independence, we perform a permutation test. For each architecture pair at 1.3B h3-1, we hold the helped (or hurt) set sizes fixed and randomly assign example indices to each set (10{,}000 permutations, seed 42). Table~\ref{tab:jaccard_perm} reports the observed $J$, the null baseline $J_{\text{null}}$ (mean over permutations), and the $z$-score.
301	
302	\begin{table}[ht]
303	\centering
304	\caption{Permutation test for pairwise Jaccard similarity (1.3B h3-1 on LAMBADA, 10{,}000 permutations). All observed values significantly exceed the independence baseline.}
305	\label{tab:jaccard_perm}
306	\resizebox{\columnwidth}{!}{%
307	\begin{tabular}{llcccc}
308	\toprule
309	Category & Pair & $J_{\text{obs}}$ & $J_{\text{null}}$ & $z$ & $p$ \\
310	\midrule
311	Helped & GDN--HGRN2 & .100 & .051 & 7.11 & $<$.0001 \\
312	 & GDN--RetNet & .092 & .045 & 6.75 & $<$.0001 \\
313	 & HGRN2--RetNet & .108 & .049 & 8.61 & $<$.0001 \\
314	\midrule
315	Hurt & GDN--HGRN2 & .088 & .049 & 5.91 & $<$.0001 \\
316	 & GDN--RetNet & .103 & .056 & 6.85 & $<$.0001 \\
317	 & HGRN2--RetNet & .087 & .045 & 6.05 & $<$.0001 \\
318	\bottomrule
319	\end{tabular}%
320	}
321	\end{table}
322	
323	All six comparisons yield $z > 5.9$ ($p < .0001$). The null baseline averages $J_{\text{null}} \approx 0.049$; observed values are approximately twice this level. The overlap between architectures' per-example effect sets is therefore structured rather than a product of random set overlap given the set sizes.
324	
325	\section{Transformer Entrainment Comparison}\label{app:transformer_entrainment}
326	
327	To test whether attention layers make hybrid models' per-example behavior converge toward a pure Transformer, we compare the correct-example sets of each architecture's pure and h3-1 variants against a 1.3B Transformer baseline (accuracy 48.1\%) on LAMBADA. Table~\ref{tab:transformer_jaccard} reports the Jaccard similarity between each model's correct set and the Transformer's correct set.
328	
329	\begin{table}[ht]
330	\centering
331	\caption{Jaccard similarity between each model's correct set and the Transformer correct set on LAMBADA (1.3B scale). All three h3-1 hybrids are more similar to the Transformer than their pure counterparts.}
332	\label{tab:transformer_jaccard}
333	\small
334	\begin{tabular}{lccc}
335	\toprule
336	Architecture & $J_{\text{pure,T}}$ & $J_{\text{h3-1,T}}$ & $\Delta$ \\
337	\midrule
338	GDN & 0.645 & 0.649 & $+$0.005 \\
339	RetNet & 0.679 & 0.694 & $+$0.015 \\
340	HGRN2 & 0.672 & 0.701 & $+$0.029 \\
341	\bottomrule
342	\end{tabular}
343	\end{table}
344	
345	All three architectures show positive $\Delta$: the h3-1 correct set is more similar to the Transformer correct set than the pure correct set is. The effect is strongest for HGRN2 ($+$0.029) and weakest for GDN ($+$0.005). This ordering is consistent with HGRN2 being the only architecture with a positive net per-example effect from attention (Table~\ref{tab:per_example}). The Transformer itself achieves the lowest accuracy among all models, so the convergence is not explained by hybrid models degrading toward Transformer-level performance; rather, adding attention shifts which specific examples the hybrid gets correct toward the Transformer's pattern.
346	
347	\section{Within-Architecture Per-Example Stability}\label{app:within_arch_stability}
348	
349	Per-example effect sets exhibit a three-tier Jaccard hierarchy on LAMBADA (1.3B scale). Under independence (permutation baseline), pairwise Jaccard is $J \approx 0.05$. Cross-architecture comparisons (different architectures at the same attention ratio) yield $J \approx 0.10$, approximately $2\times$ baseline. Within-architecture comparisons (same architecture across different attention ratios) yield $J \approx 0.33$, approximately $7\times$ baseline and $3\times$ the cross-architecture level. Architecture identity therefore has approximately three times the influence of attention dose on per-example effects.
350	
351	Table~\ref{tab:within_arch_summary} reports mean within-architecture Jaccard for each architecture. HGRN2 shows the highest helped overlap and lowest hurt overlap, consistent with its monotonically increasing helped count across ratios (479 $\to$ 548).
352	
353	\begin{table}[ht]
354	\centering
355	\caption{Mean within-architecture pairwise Jaccard similarity across attention ratios (1.3B, LAMBADA). Each mean is computed over all six ratio pairs per architecture.}
356	\label{tab:within_arch_summary}
357	\begin{tabular}{lcc}
358	\toprule
359	Architecture & $\bar{J}_{\text{helped}}$ & $\bar{J}_{\text{hurt}}$ \\
360	\midrule
361	GDN & 0.338 & 0.319 \\
362	RetNet & 0.333 & 0.321 \\
363	HGRN2 & 0.373 & 0.291 \\
364	\midrule
365	\textit{Overall mean} & \textit{0.348} & \textit{0.310} \\
366	\bottomrule
367	\end{tabular}
368	\end{table}
369	
370	Table~\ref{tab:within_arch_pairwise} reports the full pairwise Jaccard matrix. Attention ratios are denoted by their h$k$-1 labels: h24-1 (4\%), h12-1 (7.7\%), h6-1 (14.3\%), h3-1 (25\%).
371	
372	\begin{table}[ht]
373	\centering
374	\small
375	\caption{Within-architecture pairwise Jaccard similarity between helped and hurt sets at different attention ratios (1.3B, LAMBADA). Each cell compares the per-example effect sets of two attention configurations within the same architecture.}
376	\label{tab:within_arch_pairwise}
377	\resizebox{\columnwidth}{!}{%
378	\begin{tabular}{llcccccc}
379	\toprule
380	 & & \multicolumn{6}{c}{Ratio pair} \\
381	\cmidrule(lr){3-8}
382	Arch & Cat & h24--h12 & h24--h6 & h24--h3 & h12--h6 & h12--h3 & h6--h3 \\
383	\midrule
384	\multirow{2}{*}{GDN} & Helped & .345 & .335 & .311 & .344 & .341 & .352 \\
385	 & Hurt & .310 & .328 & .320 & .331 & .281 & .345 \\
386	\midrule
387	\multirow{2}{*}{RetNet} & Helped & .354 & .314 & .334 & .322 & .330 & .345 \\
388	 & Hurt & .316 & .334 & .307 & .301 & .324 & .343 \\
389	\midrule
390	\multirow{2}{*}{HGRN2} & Helped & .359 & .369 & .375 & .368 & .378 & .388 \\
391	 & Hurt & .292 & .289 & .298 & .273 & .309 & .287 \\
392	\bottomrule
393	\end{tabular}%
394	}
395	\end{table}
396	
397	Adjacent ratio pairs (e.g., h24-1 vs.\ h12-1) do not exhibit systematically higher Jaccard than non-adjacent pairs (e.g., h24-1 vs.\ h3-1). Across all architectures, the mean Jaccard for adjacent pairs is 0.353 (helped) and 0.311 (hurt), compared with 0.343 (helped) and 0.310 (hurt) for non-adjacent pairs. The negligible difference indicates that the mapping from attention dose to per-example effects is non-smooth: doubling the attention ratio does not produce a proportionally more similar set of affected examples.
398	
399	\section{Cross-Benchmark Jaccard Trajectories}\label{app:cross_bench_jaccard}
400	
401	To test whether Jaccard saturation is specific to LAMBADA or a general property, we compute mean pairwise Jaccard trajectories across all four hybrid attention ratios on all four main benchmarks. Table~\ref{tab:cross_bench_jaccard} reports the results. On every benchmark, Jaccard shows no statistically significant trend with attention ratio (all $\rho \leq 0.80$, $p \geq 0.333$), with values uniformly between 0.08 and 0.11. The saturation at the first attention level observed on LAMBADA (\S\ref{ssec:decoupling}) thus generalizes: once any attention is present, each architecture's per-example response is largely fixed regardless of attention dose.
402	
403	\begin{table}[ht]
404	\centering
405	\small
406	\caption{Mean pairwise Jaccard (helped sets, 3 architecture pairs) across attention ratios and benchmarks (1.3B scale). $\rho$: Spearman correlation between attention ratio and $\bar{J}$. All $p \geq 0.333$.}
407	\label{tab:cross_bench_jaccard}
408	\begin{tabular}{@{}lcccccc@{}}
409	\toprule
410	Benchmark & h24-1 & h12-1 & h6-1 & h3-1 & $\rho$ & $p$ \\
411	\midrule
412	LAMBADA & .091 & .088 & .096 & .097 & 0.80 & .333 \\
413	HellaSwag & .084 & .081 & .091 & .086 & 0.60 & .417 \\
414	PIQA & .089 & .096 & .089 & .095 & 0.00 & 1.00 \\
415	ARC-Easy & .084 & .099 & .091 & .109 & 0.80 & .333 \\
416	\bottomrule
417	\end{tabular}
418	\end{table}
419	
420	\section{Continuous-Threshold Jaccard Analysis}\label{app:continuous_jaccard}
421	
422	The main text binarizes per-example effects at the correctness boundary. To verify that low cross-architecture Jaccard is not an artifact of this binarization, we compute Jaccard similarity using a continuous confidence threshold $\tau$: two architectures' effect sets are defined as the examples whose target-token $|\log p|$ changes by more than $\tau$ when attention is added. On LAMBADA, mean pairwise Jaccard decreases monotonically from 0.26 ($\tau = 0.00$, any change) to 0.05 ($\tau = 0.30$, large changes only). ARC-Easy and PIQA show the same monotonic decrease. The binary threshold ($\tau = 0$, correctness flip) thus represents the upper end of cross-architecture overlap; restricting to confident transitions further reduces agreement, confirming that low Jaccard is robust to the choice of binarization threshold.
423	
424	\section{Target-Token Confidence Margin}
425	\label{app:confidence_margin}
426	
427	We analyze whether pure-model confidence on the target token predicts whether attention will help or hurt on a given example.
428	We define confidence as $|\log p_{\text{pure}}(y^*)|$, where $y^*$ is the target token: lower values indicate higher probability (near-correct).
429	We initially tested raw perplexity as a predictor of helped/hurt status, but found that within-category controls (C1/C2) are necessary to isolate attention effects from the definitional confound between pure-correct and pure-wrong populations.
430	
431	Table~\ref{tab:cm_c1} compares hurt versus stayed-right samples (both pure-correct): hurt samples have significantly lower target-token probability (higher $|\log p|$), confirming that weakly-correct predictions are vulnerable to attention disruption.
432	Table~\ref{tab:cm_c2} compares helped versus stayed-wrong samples (both pure-wrong): helped samples have higher target-token probability (lower $|\log p|$), confirming that near-miss errors are rescuable.
433	This pattern is consistent across all three architectures ($|d| = 0.73$--$0.92$, all $p < 10^{-54}$) but does not alter the cross-architecture Jaccard findings---within-architecture predictability coexists with cross-architecture divergence.
434	
435	\begin{table}[ht]
436	\centering
437	\caption{Control 1: Pure-correct samples---hurt vs.\ stayed-right. Higher mean $|\log p|$ indicates lower target-token probability (less confident correct).}
438	\label{tab:cm_c1}
439	\resizebox{\columnwidth}{!}{%
440	\begin{tabular}{lrrrrr}
441	\toprule
442	Architecture & $n_{\text{hurt}}$ & $n_{\text{stay}}$ & Hurt mean & Stay mean & Cohen's $d$ \\
443	\midrule
444	GDN (h12-1) & 519 & 2281 & 1.049 & 0.576 & 0.87 \\
445	RetNet (h3-1) & 497 & 2169 & 1.293 & 0.785 & 0.83 \\
446	HGRN2 (h3-1) & 392 & 2102 & 1.481 & 0.899 & 0.92 \\
447	\bottomrule
448	\end{tabular}
449	}
450	\end{table}
451	
452	\begin{table}[ht]
453	\centering
454	\caption{Control 2: Pure-wrong samples---helped vs.\ stayed-wrong. Lower mean $|\log p|$ indicates higher target-token probability (near-miss error).}
455	\label{tab:cm_c2}
456	\resizebox{\columnwidth}{!}{%
457	\begin{tabular}{lrrrrr}
458	\toprule
459	Architecture & $n_{\text{help}}$ & $n_{\text{stay}}$ & Help mean & Stay mean & Cohen's $d$ \\
460	\midrule
461	GDN (h12-1) & 480 & 1873 & 2.459 & 4.189 & $-$0.75 \\
462	RetNet (h3-1) & 420 & 2067 & 2.478 & 4.103 & $-$0.73 \\
463	HGRN2 (h3-1) & 548 & 2111 & 2.500 & 4.112 & $-$0.77 \\
464	\bottomrule
465	\end{tabular}
466	}
467	\end{table}
468	
469	\subsection{Cross-Benchmark Extension}\label{app:cm_cross}
470	
471	The confidence margin pattern extends beyond LAMBADA to multiple-choice benchmarks, though with smaller effect sizes. Table~\ref{tab:cm_cross_c2} reports the rescue analysis (helped vs.\ stayed-wrong) on HellaSwag and ARC-Easy. All nine comparisons (three benchmarks $\times$ three architectures) are significant, confirming that attention consistently rescues near-miss errors regardless of task type. Effect sizes range from small on HellaSwag ($d = 0.13$--$0.17$) to medium on ARC-Easy ($d = 0.51$--$0.60$), compared to large on LAMBADA ($d = 0.73$--$0.77$); the attenuation on HellaSwag reflects noisier confidence proxies under length-normalized scoring. Table~\ref{tab:cm_cross_c1} reports the disruption analysis (hurt vs.\ stayed-right); two of six comparisons are significant (all on ARC-Easy) with small effect sizes ($d = 0.13$--$0.26$), indicating that the disruption signal is weaker on multiple-choice tasks and absent on HellaSwag under \texttt{acc\_norm}. The asymmetry between rescue and disruption reflects task structure: near-miss errors are an intrinsic sample property (the model almost produced the correct answer regardless of format), while borderline correctness in multiple-choice settings depends on relative option ranking rather than absolute confidence, reducing the raw log-likelihood margin's predictive power for vulnerability.
472	
473	\begin{table}[ht]
474	\centering
475	\caption{Cross-benchmark rescue analysis (Control 2): helped vs.\ stayed-wrong on HellaSwag and ARC-Easy (1.3B h3-1).}
476	\label{tab:cm_cross_c2}
477	\resizebox{\columnwidth}{!}{%
478	\begin{tabular}{llrr}
479	\toprule
480	Benchmark & Architecture & Cohen's $d$ & $p$ \\
481	\midrule
482	HellaSwag & GDN & $-$0.166 & $6.1 \times 10^{-4}$ \\
483	 & RetNet & $-$0.132 & $1.4 \times 10^{-2}$ \\
484	 & HGRN2 & $-$0.164 & $1.4 \times 10^{-3}$ \\
485	\midrule
486	ARC-Easy & GDN & $-$0.60 & $1.0 \times 10^{-13}$ \\
487	 & RetNet & $-$0.51 & $5.3 \times 10^{-10}$ \\
488	 & HGRN2 & $-$0.53 & $5.4 \times 10^{-10}$ \\
489	\bottomrule
490	\end{tabular}%
491	}
492	\end{table}
493	
494	\begin{table}[ht]
495	\centering
496	\caption{Cross-benchmark disruption analysis (Control 1): hurt vs.\ stayed-right on HellaSwag and ARC-Easy (1.3B h3-1).}
497	\label{tab:cm_cross_c1}
498	\resizebox{\columnwidth}{!}{%
499	\begin{tabular}{llrrl}
500	\toprule
501	Benchmark & Architecture & Cohen's $d$ & $p$ & Sig.? \\
502	\midrule
503	HellaSwag & GDN & 0.009 & .999 & No \\
504	 & RetNet & $-$0.035 & .453 & No \\
505	 & HGRN2 & $-$0.062 & .274 & No \\
506	\midrule
507	ARC-Easy & GDN & 0.26 & $3.2 \times 10^{-4}$ & Yes \\
508	 & RetNet & 0.22 & $2.8 \times 10^{-3}$ & Yes \\
509	 & HGRN2 & 0.13 & .145 & No \\
510	\bottomrule
511	\end{tabular}%
512	}
513	\end{table}
514	
515	\subsection{Prediction Framework}\label{app:prediction_framework}
516	
517	We formalize the confidence margin analysis as a binary prediction task: given a pure-model example and its target-token $|\log p|$, predict whether attention will change the example's correctness. Using the within-category summary statistics (Tables~\ref{tab:cm_c1},~\ref{tab:cm_c2}), we derive analytic AUC from Cohen's $d$ via $\text{AUC} = \Phi(|d|/\sqrt{2})$ and compute Gaussian-intersection thresholds (the $|\log p|$ value at which the two group densities intersect under equal priors).
518	
519	Table~\ref{tab:prediction_auc} reports within-architecture prediction performance. All AUCs exceed 0.69, confirming that pure-model confidence is a reliable within-architecture predictor of attention effects. Disruption prediction is consistently stronger than rescue (mean AUC 0.73 vs.\ 0.70), reflecting the larger effect sizes in Control~1.
520	
521	\begin{table}[ht]
522	\centering
523	\small
524	\caption{Within-architecture prediction of attention effects on LAMBADA (1.3B). AUC$_p$: parametric (from Cohen's $d$); AUC$_e$: empirical (non-parametric).}
525	\label{tab:prediction_auc}
526	\begin{tabular}{@{}lcccccc@{}}
527	\toprule
528	Architecture & \multicolumn{3}{c}{Rescue} & \multicolumn{3}{c}{Disruption} \\
529	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
530	 & AUC$_p$ & AUC$_e$ & $d$ & AUC$_p$ & AUC$_e$ & $d$ \\
531	\midrule
532	GDN (h12-1) & .701 & .756 & 0.75 & .732 & .742 & 0.87 \\
533	RetNet (h3-1) & .696 & .754 & 0.73 & .722 & .735 & 0.83 \\
534	HGRN2 (h3-1) & .708 & .765 & 0.77 & .743 & .748 & 0.92 \\
535	\midrule
536	Mean & .702 & .758 & --- & .732 & .742 & --- \\
537	\bottomrule
538	\end{tabular}
539	\end{table}
540	
541	\paragraph{Normality verification.} We verify the normality assumption underlying the parametric AUC estimate by computing empirical (non-parametric) AUC directly from the data. For disruption prediction, empirical AUC values (0.73--0.75) differ from parametric estimates by less than 2\%, confirming that the normality assumption is adequate. For rescue prediction, empirical AUC values (0.76) exceed parametric estimates (0.70--0.71) by approximately 7\%, indicating mild right-skew in the $|\log p|$ distribution. The parametric estimate is therefore conservative (understates predictive power), and the main-text AUC range of 0.70--0.74 represents a lower bound.
542	
543	Despite similar within-architecture AUC, the optimal prediction thresholds differ across architectures for disruption but not rescue (Table~\ref{tab:threshold_gap}). Rescue thresholds cluster tightly (range 0.03 in $|\log p|$), indicating that the rescuability boundary---the confidence level below which pure-wrong examples are likely to be corrected by attention---is architecture-invariant. Disruption thresholds span a 47\% relative range (GDN: 0.70, RetNet: 1.00, HGRN2: 1.14), meaning that the same confidence level on a pure-correct example may predict vulnerability in one architecture but safety in another. This asymmetry constitutes a second dimension of multiplicity beyond per-example disagreement: all three architectures agree on which wrong answers are rescuable, but disagree on which correct answers are vulnerable to disruption.
544	
545	\begin{table}[ht]
546	\centering
547	\small
548	\caption{Gaussian-intersection prediction thresholds ($|\log p|$) across architectures. Relative spread: range/mean.}
549	\label{tab:threshold_gap}
550	\begin{tabular}{@{}lccccr@{}}
551	\toprule
552	 & GDN & RetNet & HGRN2 & Range & Rel.\ spread \\
553	\midrule
554	Rescue & 3.32 & 3.29 & 3.31 & 0.03 & 1.0\% \\
555	Disruption & 0.70 & 1.00 & 1.14 & 0.44 & 46.7\% \\
556	\bottomrule
557	\end{tabular}
558	\end{table}
559	
560	\section{Calibration Analysis}\label{app:calibration}
561	
562	Cross-architecture disruption threshold variation (\S\ref{ssec:per_example}) could in principle arise from calibration differences rather than genuine differences in per-example processing. We compute expected calibration error (ECE; \citealt{guo2017calibration}) for each architecture's h3-1 model on LAMBADA using 15 equal-width bins. ECE values are similar: GDN 0.222, RetNet 0.224, HGRN2 0.235. The cross-architecture ECE spread (17\%, computed as range/mean) is less than half the disruption threshold spread (47\%; Table~\ref{tab:threshold_gap}), indicating that calibration differences are insufficient to account for the observed threshold divergence. Rescue thresholds, which show only 1\% cross-architecture spread, are consistent with near-identical calibration in the low-confidence regime.
563	
564	\section{BoolQ Supplementary Analysis}
565	\label{app:boolq}
566	
567	BoolQ ($N = 3{,}270$; comprehension, binary yes/no classification) shows the highest ambiguity among the benchmarks we analyzed ($\alpha \approx 0.45$), but the Jaccard significance pattern is mixed: only 12 of 24 architecture $\times$ attention-ratio pair combinations yield $p < .01$. In particular, the RetNet--HGRN2 pair produces 0/8 significant Jaccard values, with several normalized effect sizes below zero, suggesting anti-correlated per-example effects for this pair.
568	
569	\paragraph{Binary classification baseline.} BoolQ is binary classification (two answer choices), whereas LAMBADA, HellaSwag, and ARC-Easy involve open vocabulary prediction or four-way multiple choice. Under a binary task, the null Jaccard baseline $J_{\text{null}}$ is higher because chance overlap between helped/hurt sets is larger when there are fewer ways to be wrong. This elevates the significance threshold: observed Jaccard must be substantially higher to exceed the null, which explains why 12/24 pairs fail to reach significance despite $\bar{J}_h = 0.103$ and $\bar{J}_u = 0.098$---values comparable to the four main benchmarks.
570	
571	\paragraph{Per-example summary.} Table~\ref{tab:boolq_multiplicity} reports the key metrics. The high $\alpha$ reflects that BoolQ examples are more sensitive to architectural variation in the presence of attention: approximately half of all examples change correctness status for at least one architecture. However, the mixed Jaccard significance prevents us from confidently concluding that the cross-architecture overlap structure matches the pattern observed on the four main benchmarks.
572	
573	\begin{table}[ht]
574	\centering
575	\small
576	\caption{BoolQ predictive multiplicity at 1.3B (h3-1).}
577	\label{tab:boolq_multiplicity}
578	\begin{tabular}{@{}lcccccc@{}}
579	\toprule
580	 & $N$ & $\alpha$ & $\bar{J}_{h}$ & $\bar{J}_{u}$ & Sig.\ pairs & $\rho_\alpha$ \\
581	\midrule
582	BoolQ & 3270 & .45 & .103 & .098 & 12/24 & $+0.1$ \\
583	\bottomrule
584	\end{tabular}
585	\par\vspace{1pt}
586	{\footnotesize RetNet--HGRN2: 0/8 significant; multiple normalized ES $< 0$.}
587	\end{table}
588	
589	The significant Jaccard overlap concentrates in GDN--RetNet pairs (8/8 significant), while RetNet--HGRN2 shows none (0/8). This pair-specificity does not appear on the four main benchmarks, where all architecture pairs show significant overlap; it may reflect a BoolQ-specific interaction between binary classification structure and particular recurrent architectures rather than a general property of architecture pairs.
590	
591	\paragraph{Confidence margin.} Confidence margin analysis on BoolQ shows the rescue pattern (C2) partially holds (2/3 architectures significant, $d = 0.16$--$0.36$) but the disruption pattern (C1) is absent (0/3, $|d| \leq 0.10$), consistent with compressed log-likelihood ranges in binary classification reducing the predictive power of confidence margins. This extends the gradient observed across LAMBADA, ARC-Easy, and HellaSwag: C1 effect sizes decrease from open-ended prediction ($d \approx 0.9$, LAMBADA) through ARC-Easy ($d \approx 0.1$--$0.3$) to HellaSwag ($d \approx 0$ under \texttt{acc\_norm}) and binary classification ($d \approx 0$, BoolQ). The gradient broadly tracks the coefficient of variation (CV) of the log-likelihood confidence proxy: LAMBADA ($\text{CV} = 0.75$) $>$ ARC-Easy ($0.54$) $>$ HellaSwag ($0.49$) $>$ BoolQ ($0.22$). BoolQ's high-frequency short completions (``\,yes''/``\,no'') yield elevated baseline log-likelihoods (mean $|\text{loglik}| = 3.04$ vs.\ $0.84$ for LAMBADA) with similar absolute spread (IQR $\approx 0.9$), compressing the relative variation and rendering the confidence margin unable to separate borderline-correct from robustly-correct examples.
592	
593	\paragraph{Interpretation.} The RetNet--HGRN2 anti-correlation may reflect different error modes specific to binary classification: when one architecture's recurrent state resolves a yes/no ambiguity through attention, the other architecture's resolution may be disrupted by the same attention intervention. This pattern warrants further investigation with additional binary classification benchmarks to determine whether it is BoolQ-specific or characteristic of two-choice tasks more broadly.
594	
595	\section{WinoGrande Supplementary Analysis}
596	\label{app:winogrande}
597	
598	WinoGrande ($N = 1{,}267$; reasoning, two-choice coreference resolution) shows high ambiguity ($\alpha \approx 0.41$ at h3-1) but mixed Jaccard significance: 10 of 24 architecture $\times$ attention-ratio pair combinations yield $p < .01$. Mean pairwise Jaccard ($\bar{J}_h = 0.110$, $\bar{J}_u = 0.103$) is comparable to the four main benchmarks, but the elevated null baseline from near-chance accuracy (${\sim}60\%$) reduces statistical power to detect above-chance overlap.
599	
600	\paragraph{Near-chance accuracy.} WinoGrande accuracy across hybrid configurations ranges from 59\% to 62\%, close to the two-choice chance level of 50\%. At near-chance accuracy, a large fraction of examples are borderline---small perturbations (such as adding attention) can flip predictions in either direction, inflating the helped and hurt sets and consequently $\alpha$. This structural property, shared with BoolQ (${\sim}59\%$ accuracy, $\alpha \approx 0.45$), may partially explain the elevated $\alpha$ rather than task-intrinsic multiplicity. PIQA (73\% accuracy, $\alpha = 0.14$) and HellaSwag (60\% normalized accuracy, $\alpha = 0.15$) demonstrate that near-chance accuracy is not the sole driver, but we cannot fully exclude it as a contributing factor for WinoGrande and BoolQ.
601	
602	\begin{table}[ht]
603	\centering
604	\small
605	\caption{WinoGrande predictive multiplicity at 1.3B (h3-1).}
606	\label{tab:winogrande_multiplicity}
607	\begin{tabular}{@{}lcccccc@{}}
608	\toprule
609	 & $N$ & $\alpha$ & $\bar{J}_{h}$ & $\bar{J}_{u}$ & Sig.\ pairs & $\rho_\alpha$ \\
610	\midrule
611	WinoGrande & 1267 & .41 & .110 & .103 & 10/24 & $-0.9$ \\
612	\bottomrule
613	\end{tabular}
614	\par\vspace{1pt}
615	{\footnotesize $\alpha$ variation across ratios: 0.054 ($> 0.03$ threshold of main benchmarks).}
616	\end{table}
617	
618	\section{340M Per-Example Analysis}\label{app:scale_per_example}
619	
620	\subsection{LAMBADA}
621	
622	At 340M, LAMBADA per-example multiplicity closely matches the 1.3B pattern: $\alpha = 0.313$ (vs.\ 0.307 at 1.3B), with mean pairwise Jaccard $\bar{J} \approx 0.089$ (vs.\ 0.095). Per-example directionality is preserved: HGRN2 shows net positive effects at h3-1 ($+238$ examples), while GDN ($-256$) and RetNet ($-106$) show net negative effects, mirroring the 1.3B profile (HGRN2 $+153$, GDN $-153$, RetNet $-69$).
623	
624	However, aggregate convergence is absent at 340M: $\rho = -0.50$ ($p = .45$), with non-monotonic $\sigma$ across attention ratios ($0.025 \to 0.012 \to 0.018 \to 0.011 \to 0.016$). This contrasts sharply with 1.3B ($\rho = -1.0$, $p = .017$, monotonic $\sigma$ decrease). The decoupling between per-example divergence and aggregate convergence thus manifests differently across scales: at 340M, per-example multiplicity is present but aggregate convergence is not, suggesting that convergence requires sufficient model capacity while multiplicity does not.
625	
626	Within-benchmark $\alpha$ variation across attention ratios is also larger at 340M (0.047, from 0.313 at pure to 0.266 at h3-1) than at 1.3B ($< 0.03$; \S\ref{ssec:per_example}), suggesting that smaller models are more sensitive to the attention ratio in terms of per-example disagreement patterns.
627	
628	\begin{table}[ht]
629	\centering
630	\small
631	\caption{340M vs.\ 1.3B LAMBADA comparison.}
632	\label{tab:scale_comparison}
633	\begin{tabular}{@{}lcc@{}}
634	\toprule
635	 & 340M & 1.3B \\
636	\midrule
637	$\alpha$ (pure) & .313 & .307 \\
638	$\bar{J}$ (h3-1) & .089 & .095 \\
639	$\rho_\sigma$ & $-0.50$ & $-1.0$ \\
640	$p$ & .45 & .017 \\
641	GDN net & $-256$ & $-153$ \\
642	HGRN2 net & $+238$ & $+153$ \\
643	\bottomrule
644	\end{tabular}
645	\end{table}
646	
647	\subsection{Cross-Benchmark Scale Comparison}
648	
649	Table~\ref{tab:340m_multi_bench} extends the scale comparison to all four main benchmarks. Two patterns emerge. First, $\alpha$ is systematically higher at 340M across all benchmarks, with the largest gap on ARC-Easy ($+$8.4pp) and the smallest on LAMBADA ($+$0.6pp). Second, pairwise Jaccard remains stable across scales ($\bar{J}_h = 0.08$--$0.10$ at both scales), confirming that the qualitative pattern of per-example multiplicity---which architectures affect which examples---is scale-robust even as its magnitude increases at smaller scale. Notably, the $\alpha$ inflation does not track accuracy loss: HellaSwag has the largest accuracy gap between scales yet the smallest $\Delta\alpha$ ($+$1.9pp), while ARC-Easy has a smaller accuracy gap but the largest $\Delta\alpha$ ($+$8.4pp), arguing against accuracy as the primary driver of scale-dependent multiplicity.
650	
651	\begin{table}[ht]
652	\centering
653	\small
654	\caption{340M vs.\ 1.3B per-example multiplicity across four benchmarks. $\alpha$: ambiguity at pure-recurrent configuration. Acc: mean accuracy across three architectures at pure-recurrent. $\bar{J}_{h}$/$\bar{J}_{u}$: mean pairwise Jaccard of helped/hurt sets. $\Delta\alpha$: 340M $-$ 1.3B.}
655	\label{tab:340m_multi_bench}
656	\resizebox{\columnwidth}{!}{%
657	\begin{tabular}{lcccccccr}
658	\toprule
659	 & \multicolumn{4}{c}{340M} & \multicolumn{3}{c}{1.3B} & \\
660	\cmidrule(lr){2-5} \cmidrule(lr){6-8}
661	Benchmark & Acc & $\alpha$ & $\bar{J}_{h}$ & $\bar{J}_{u}$ & $\alpha$ & $\bar{J}_{h}$ & $\bar{J}_{u}$ & $\Delta\alpha$ \\
662	\midrule
663	PIQA & .663 & .181 & .090 & .085 & .143 & .091 & .094 & $+$.038 \\
664	HellaSwag$^\dagger$ & .420 & .167 & .084 & .083 & .148 & .095 & .085 & $+$.019 \\
665	ARC-Easy & .594 & .289 & .098 & .103 & .205 & .092 & .099 & $+$.084 \\
666	LAMBADA & --- & .313 & .089 & .090 & .307 & .095 & .093 & $+$.006 \\
667	\bottomrule
668	\multicolumn{9}{l}{\footnotesize $^\dagger$\texttt{acc\_norm}. LAMBADA accuracy omitted (evaluated in separate run).}
669	\end{tabular}%
670	}
671	\end{table}
672	
673	Convergence is absent at 340M across all benchmarks (all $|\rho| \leq 0.4$, $p \geq .45$), in contrast to 1.3B where LAMBADA shows monotonic convergence. The absence of convergence at 340M extends beyond LAMBADA to HellaSwag ($\rho = 0.4$, $p = .52$), PIQA ($\rho = 0.3$, $p = .68$), and ARC-Easy ($\rho = -0.1$, $p = .95$).
674	
675	\section{Subsample Sensitivity of \texorpdfstring{$\alpha$}{α}}\label{app:subsample_sensitivity}
676	
677	To assess the reliability of $\alpha$ estimation at different sample sizes, we repeatedly subsample each benchmark (1{,}000 bootstrap replicates, seed 42) and compute the 95\% CI width of $\alpha$.
678	
679	\begin{table}[ht]
680	\centering
681	\small
682	\caption{$\alpha$ estimation stability: 95\% CI width by subsample size.}
683	\label{tab:subsample}
684	\resizebox{\columnwidth}{!}{%
685	\begin{tabular}{@{}lrrrrr@{}}
686	\toprule
687	Benchmark & $n = 100$ & $n = 200$ & $n = 500$ & $n = 1000$ & Full $N$ \\
688	\midrule
689	PIQA & .130 & .095 & .066 & .045 & .034 \\
690	HellaSwag & .140 & .100 & .062 & .044 & .013 \\
691	ARC-Easy & .160 & .105 & .072 & .050 & .032 \\
692	LAMBADA & .180 & .125 & .082 & .057 & .025 \\
693	\bottomrule
694	\end{tabular}}
695	\par\vspace{1pt}
696	{\footnotesize At $n = 100$, CI width (0.13--0.18) spans the entire four-benchmark $\alpha$ range (0.14--0.30), rendering $\alpha$ estimation unreliable. This justifies excluding COPA ($n = 100$) from the per-example analysis.}
697	\end{table}
698	
699	\section{Complementarity Decomposition}\label{app:complementarity}
700	
701	We decompose the three-architecture vote on each example into four categories: unanimous correct (3/3), majority correct (2/3), minority correct (1/3), and unanimous wrong (0/3). This decomposition explains the structural failure of majority vote despite substantial per-example complementarity.
702	
703	Table~\ref{tab:complementarity} reports the decomposition at h3-1 (25\% attention). Majority vote benefits only from 2/3 examples (where the correct answer holds a majority) but is actively harmed by 1/3 examples (where the correct architecture is outvoted). On LAMBADA, HellaSwag, and ARC-Easy, the MV exploitation ratio---the fraction of complementary examples where MV selects correctly---hovers near 51\%, indicating a near-even split between MV-exploitable and MV-hostile disagreements. The oracle, by contrast, exploits both categories, explaining the large oracle--MV gap ($+7$--$14$\,pp).
704	
705	\begin{table}[ht]
706	\centering
707	\small
708	\caption{Complementarity decomposition at 1.3B h3-1. Fractions of total examples in each vote category. MV expl.: fraction of complementary examples where majority vote is correct.}
709	\label{tab:complementarity}
710	\begin{tabular}{@{}lccccr@{}}
711	\toprule
712	Benchmark & 3/3 & 2/3 & 1/3 & 0/3 & MV expl. \\
713	\midrule
714	LAMBADA & .361 & .151 & .145 & .343 & 51.1\% \\
715	HellaSwag & .519 & .078 & .073 & .331 & 51.6\% \\
716	ARC-Easy & .603 & .107 & .103 & .187 & 50.9\% \\
717	BoolQ & .376 & .257 & .197 & .170 & 56.6\% \\
718	\bottomrule
719	\end{tabular}
720	\end{table}
721	
722	This near-50\% exploitation ratio is structurally invariant across attention ratios: on LAMBADA, the ratio ranges from 51.1\% to 54.4\% across all five configurations; on HellaSwag, from 50.3\% to 51.6\%. Attention changes neither the amount nor the structure of cross-architecture complementarity.
723	
724	\section{Seed-Variation Calibration}\label{app:seed_calibration}
725	
726	To contextualize the $3\times$ within- vs.\ cross-architecture Jaccard gap (\S\ref{ssec:decoupling}), we compare against within-seed variation using the Pythia 70M \citep{biderman2023pythia} PolyPythias models \citep{vanderwal2025polypythias}, which provide 9 individually trained seeds of the same architecture.
727	
728	On LAMBADA ($N = 5{,}153$), within-seed mean Jaccard is $\bar{J}_h = 0.273$ (helped) and $\bar{J}_u = 0.393$ (hurt), compared to our cross-architecture reference $J \approx 0.10$. On ARC-Easy ($N = 2{,}376$), within-seed $\bar{J}_h = 0.312$ and $\bar{J}_u = 0.354$, versus cross-architecture $J \approx 0.092$. Within-seed ambiguity is $\alpha = 0.36$ (LAMBADA) and $\alpha = 0.49$ (ARC-Easy), compared to cross-architecture $\alpha = 0.30$ and $0.21$ respectively.
729	
730	Seeds thus produce comparable or higher amounts of per-example disagreement ($\alpha$) but on more overlapping examples (higher $J$). Cross-architecture variation produces per-example effects on less overlapping examples (lower $J$), consistent with architecture-driven divergence producing qualitatively different per-example patterns than seed noise. The within-seed Jaccard is 2.7--4.3$\times$ higher than cross-architecture Jaccard across both benchmarks.
731	
732	Three caveats qualify this comparison. First, scale mismatch: Pythia 70M is $5\times$ smaller than our smallest models (340M); attempts to use Pythia 410M failed repeatedly. Second, architecture family: Pythia is a standard Transformer, not a hybrid recurrent architecture, so this is a cross-family reference point rather than a matched control. Third, accuracy regime: Pythia 70M accuracy (LAMBADA 0.17--0.23, ARC-Easy ${\sim}$0.38) is far below our models (${\sim}$0.50, ${\sim}$0.72), and Jaccard is affected by base rates; the 2.7--4.3$\times$ ratio may differ at accuracy regimes closer to our main experiments. These limitations restrict the comparison to a reference point for seed-variation magnitude rather than definitive evidence for architecture-driven effects.
733	
734	\section{Extended Architecture Validation (Five Architectures)}\label{app:extended_arch}
735	
736	To test whether the low cross-architecture Jaccard pattern generalizes beyond the three primary architectures, we extend the analysis to include two additional architectures from the same model zoo: GLA (Gated Linear Attention) and DeltaNet, yielding ten pairwise comparisons. Both are available only at 340M; all results below use the h3-1 (25\% attention) configuration.
737	
738	\begin{center}
739	\small
740	\captionof{table}{Pairwise Jaccard similarity across five architectures (340M, h3-1). All 40 permutation tests yield $p \leq .002$ ($z = 3.49$--$12.21$).}
741	\label{tab:extended_arch_jaccard}
742	\begin{tabular}{@{}llcc@{}}
743	\toprule
744	Benchmark & Pair & $J_h$ & $J_u$ \\
745	\midrule
746	\multirow{11}{*}{LAMBADA} & GDN--RetNet & .128 & .121 \\
747	 & GDN--HGRN2 & .123 & .083 \\
748	 & GDN--GLA & .124 & .100 \\
749	 & GDN--DeltaNet & .115 & .100 \\
750	 & RetNet--HGRN2 & .108 & .083 \\
751	 & RetNet--GLA & .123 & .107 \\
752	 & RetNet--DeltaNet & .115 & .096 \\
753	 & HGRN2--GLA & .127 & .086 \\
754	 & HGRN2--DeltaNet & .125 & .090 \\
755	 & GLA--DeltaNet & .134 & .081 \\
756	 & \textit{Mean} & \textit{.122} & \textit{.095} \\
757	\midrule
758	\multirow{11}{*}{ARC-Easy} & GDN--RetNet & .089 & .114 \\
759	 & GDN--HGRN2 & .122 & .105 \\
760	 & GDN--GLA & .114 & .106 \\
761	 & GDN--DeltaNet & .084 & .102 \\
762	 & RetNet--HGRN2 & .087 & .115 \\
763	 & RetNet--GLA & .112 & .110 \\
764	 & RetNet--DeltaNet & .138 & .123 \\
765	 & HGRN2--GLA & .098 & .087 \\
766	 & HGRN2--DeltaNet & .109 & .088 \\
767	 & GLA--DeltaNet & .129 & .098 \\
768	 & \textit{Mean} & \textit{.108} & \textit{.105} \\
769	\bottomrule
770	\end{tabular}
771	\end{center}
772	
773	% Figure moved to main text (\S\ref{ssec:robustness})
774	
775	All pairwise Jaccard values remain $\leq 0.14$, consistent with the three-architecture results at 1.3B (Table~\ref{tab:per_example}). The seven new pairs involving GLA and DeltaNet show no systematic difference from the original three pairs (Mann-Whitney $p > .3$ for both helped and hurt), indicating that the low-overlap pattern is not specific to the original architecture triple. A sixth architecture (HGRN; \citealp{qin2023hierarchically}) is also available in the zoo but excluded from the main analysis: its substantially lower baseline accuracy on LAMBADA (0.263 vs.\ 0.32--0.38 for the other five) mechanically inflates helped-set sizes and Jaccard values. All 15 six-architecture permutation tests nonetheless remain significant ($z \geq 2.9$, $p \leq .006$). The same pattern holds on HellaSwag ($N = 10{,}042$) and PIQA ($N = 1{,}838$): all 20 additional pairwise tests yield $p < .01$ with mean $J_{\text{helped}} \leq 0.10$. Full four-benchmark and six-architecture data are included in our code release.
776	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b222c678-f987-4cf0-986c-d3a46f013365",
  "isSidechain": true,
  "promptId": "42028348-629d-494c-9ba6-5ed1efbe2bc1",
  "agentId": "aa0c4d7f41c26a15c",
  "type": "user",
  "uuid": "3ba09301-fece-4c9f-b4c2-5dd16b6d42e9",
  "sourceToolAssistantUUID": "b222c678-f987-4cf0-986c-d3a46f013365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "a02ce5b1-88a8-4060-9e99-0b93ad72b89c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-juggling-wozniak"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-23T15:30:43.533Z_

Perfect. Now I have all the key information. Let me compile the findings for your ARR Responsible NLP Checklist:

---

## ARR Responsible NLP Checklist — Key Content Summary

### 1. **Model Zoo & Sizes**
- **Model Zoo Source**: Wang et al. (2025) hybrid architecture zoo
- **Architectures**: 3 primary architectures (GatedDeltaNet, RetNet, HGRN2) plus 2 extended (GLA, DeltaNet)
- **Model Scales**: 340M and 1.3B parameters
- **Attention Ratios**: 5 configurations (0%, 4%, 7.7%, 14.3%, 25%)
- **Transformer baseline**: 1.3B pure attention baseline included for comparison
- **Total Configurations**: 30 (3 architectures × 5 attention ratios × 2 scales)
- **License/Attribution**: All models from publicly available zoo; analysis code and per-example evaluation outputs will be released upon publication

### 2. **Datasets & Benchmarks (10 main + 1 supplementary)**
**Four Categories by Cognitive Demand:**
- **Retrieval**: LAMBADA (5,153 examples)
- **Comprehension**: BoolQ (3,270 examples)
- **Reasoning**: HellaSwag (10,042), ARC-Challenge, WinoGrande (1,267), PIQA (1,838), COPA (100, supplementary)
- **Mixed**: ARC-Easy (2,376), MMLU, SciQ, XStoryCloze

**Evaluation Framework:**
- All evaluations use **lm-evaluation-harness v0.4.x** with default prompts and greedy decoding
- Accuracy is the primary metric (HellaSwag uses acc_norm; normalized accuracy)
- Bootstrap analyses use random seed 42

### 3. **Hyperparameters & Training Details**
- All configurations share **identical training data, tokenizer, and optimization** within each scale
- Differ only in **architecture and attention configuration**
- Controlled design isolates attention effects from confounds
- Single training runs per configuration (acknowledged limitation)
- No fine-tuning; all evaluations use **pretrained checkpoints only**

### 4. **Evaluation Tools & Statistical Methods**
**Primary Methods:**
- **Spearman rank correlation** ($\rho$) between attention ratio and cross-architecture standard deviation
- **Exact permutation tests** for Spearman $\rho$ (120 permutations; $n=5$)
- **Bonferroni correction** across 10 benchmarks (adjusted threshold α/10 = 0.005)
- **Bootstrap 95% BCa confidence intervals** using 10,000 resamples
- **Mann-Whitney U tests** (within-architecture), **Kruskal-Wallis** (cross-architecture)

**Per-Example Analysis:**
- **Jaccard similarity** ($J = |A ∩ B| / |A ∪ B|$) for helped/hurt set overlap
- **Predictive multiplicity metric** ($\alpha$, from Marx et al. 2020)
- Binary classification: helped (correct only with attention), hurt (correct only without), unchanged
- Permutation tests for Jaccard significance (10,000 permutations)
- **Continuous confidence margin analysis** with Cohen's $d$ effect sizes (0.73–0.92 on LAMBADA)
- AUC prediction framework for attention effects (AUC 0.70–0.74)

**Confidence Analysis:**
- Target-token log-probability ($|\log p|$) as confidence proxy
- Gaussian-intersection thresholds for prediction
- Expected Calibration Error (ECE) computed with 15 equal-width bins
- Cross-entropy and calibration differences between architectures

**Note on Power**: With $n=5$ attention ratios, minimum achievable $p=0.017$. LAMBADA's Bonferroni-adjusted $p=.170$ does not reach conventional significance; described as exploratory.

### 5. **Limitations Section** (main.tex, lines 39–46)
Three key limitations explicitly acknowledged:
1. **Single training runs**: Each config is one run; cannot fully disentangle architectural from seed-specific effects. Proxy evidence from Pythia 70M seed calibration (within-seed $J$ is 2.7–4.3× higher) and consistency across 40 architecture–benchmark combinations (all $p < .01$).
2. **Coverage**: Three primary architectures, four main benchmarks, two scale points. Generalization to Mamba, RWKV, and generation tasks remains open. Larger scales (7B+) may differ.
3. **Pre-training only**: All evaluations use pretrained checkpoints; per-example effects may not persist after fine-tuning.

### 6. **Ethics, Risks & AI Assistant Disclosure**
**Limitations Section explicitly addresses:**
- No human subjects involved
- No PII in benchmarks (standard public benchmarks: LAMBADA, BoolQ, HellaSwag, ARC, PIQA, WinoGrande, MMLU, SciQ, XStoryCloze, COPA)
- No new datasets collected
- No AI assistant disclosure in paper (paper written by human authors)
- Risk discussion: Per-example multiplicity ($\alpha = 0.14–0.30$) warrants per-example audits before architecture substitution in deployed systems

**Computational Cost:**
- Models are relatively modest (340M–1.3B), well within standard academic compute
- No explicit compute budget stated in paper
- Evaluation uses lm-evaluation-harness (standard, efficient framework)

### 7. **Code & Reproducibility**
**Statement** (main.tex, lines 47–49):
"All models are from the publicly available model zoo of \citet{wang2025hybrid}. Our analysis code and per-example evaluation outputs will be released upon publication."

**Sections Included via \input**:
- sections/introduction
- sections/related_work
- sections/method
- sections/experiments
- sections/conclusion
- sections/appendix

### 8. **Related Work & Citations** (sections/related_work.tex)
Key references supporting methodology:
- **Predictive Multiplicity**: Marx et al. (2020), Damour et al. (2022 – underspecification)
- **Architectural Comparison**: McCoy et al. (2020 – BERT disagreement), Sellam et al. (2022 – MultiBERT)
- **Ensemble Diversity**: Fort et al. (2019 – loss landscapes), Kuncheva (2003 – diversity measures)
- **Rashomon Sets & Model Multiplicity**: Fisher et al. (2019), Black et al. (2022)
- **Ecological Fallacy**: Robinson (1950)

### 9. **Reproducibility Checklist Items**
- **Code**: Will be released upon publication
- **Data**: All benchmarks are publicly available; standard versions via lm-evaluation-harness
- **Models**: Publicly available from Wang et al. (2025) zoo
- **Random seeds**: Reported (seed 42 for bootstrap and permutation tests)
- **Hyperparameters**: Fully specified (Table 1, Method section)
- **Statistical power**: Explicitly acknowledged as limited ($n=5$; minimum $p=0.017$)
- **Sensitivity analyses**: Extensive (GDN exclusion, scale effects, subsampling, continuous Jaccard, etc.)

---

**Key Takeaway for ARR Checklist:**
This is a **methodologically rigorous paper** with strong reproducibility practices. All models/data are public, statistical methods are pre-specified (informal pre-analysis plan noted), and limitations are thoroughly disclosed. The main ethical consideration is **deployment risk**: the finding that architectures with identical aggregate performance affect ~90% non-overlapping sets of examples warrants per-example audits before production use ($\alpha > 0.2$).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ba09301-fece-4c9f-b4c2-5dd16b6d42e9",
  "isSidechain": true,
  "agentId": "aa0c4d7f41c26a15c",
  "requestId": "req_011CbKjrrwQeJxeff2h3iC1Z",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "badbf63a-d9ec-43a6-8342-a6315fa6a8a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "a02ce5b1-88a8-4060-9e99-0b93ad72b89c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-juggling-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019cc51yqe7itmaJqsRbPfUm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 26549,
      "cache_read_input_tokens": 48387,
      "output_tokens": 1912,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 26549
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1912,
          "cache_read_input_tokens": 48387,
          "cache_creation_input_tokens": 26549,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 26549,
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
