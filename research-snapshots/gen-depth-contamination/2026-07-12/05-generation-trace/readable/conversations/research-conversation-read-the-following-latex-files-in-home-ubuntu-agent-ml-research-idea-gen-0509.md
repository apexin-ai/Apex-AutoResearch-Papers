# Research conversation: Read the following LaTeX files in /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a8deb1249dd0a8798.jsonl`
- **Structured JSON:** [`de2af243fd05c0c01361.json`](../../sessions/de/de2af243fd05c0c01361.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

17 recorded events

### User

_source line 1 · 2026-05-22T21:21:44.454Z_

Read the following LaTeX files in /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/ and return their FULL contents:
1. introduction.tex
2. related_work.tex
3. method.tex
4. experiments_c1.tex
5. experiments_c3.tex
6. discussion.tex
7. conclusion.tex

I need the complete text of each file. Return the contents with the filename as a header before each file's contents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bed57f34-927e-4cb2-bd8a-b1a329fa1fbe",
  "agentId": "a8deb1249dd0a8798",
  "type": "user",
  "uuid": "6f910976-dbab-4218-9d55-5b24f684e246",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-22T21:21:45.534Z_

I'll read all seven LaTeX files from the specified directory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f910976-dbab-4218-9d55-5b24f684e246",
  "isSidechain": true,
  "agentId": "a8deb1249dd0a8798",
  "requestId": "req_011CbJJrDu3QDf9yb7QjkxJG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c4aed8bc-88d5-4577-bab4-bc1c7e96876a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015yc3KopAaTUV11o47MM9kc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19301,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19301,
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

_source line 3 · 2026-05-22T21:21:45.891Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DPdKYUQie32DdUydjuu5GD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4aed8bc-88d5-4577-bab4-bc1c7e96876a",
  "isSidechain": true,
  "agentId": "a8deb1249dd0a8798",
  "requestId": "req_011CbJJrDu3QDf9yb7QjkxJG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "78757045-328e-4768-9494-bf851b859edd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015yc3KopAaTUV11o47MM9kc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19301,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19301,
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

_source line 4 · 2026-05-22T21:21:45.897Z_

<details><summary>↩ Tool result · `toolu_01DPdKYUQie32DdUydjuu5GD`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
5	Estimates suggest that a substantial fraction of online text is machine-generated~\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.
6	When models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
7	This degradation arises in both \emph{retrain-chains} (iteratively training on model outputs) and \emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\ref{sec:extended_limitations}).
8	Yet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.
9	
10	This gap cuts across three communities: binary detectors~\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\ref{sec:binary_confidence}); membership inference~\cite{zawalski2026codec} addresses a different question; the model collapse literature~\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool; and data selection methods~\cite{xie2023dsir, tirumala2023d4, drayson2025} ignore recursive depth.
11	No existing method estimates how many rounds of recursive generation a text has undergone.
12	
13	The Data Processing Inequality guarantees that information degrades monotonically across generations, motivating a finite discrimination boundary $\Kstar$.
14	We empirically measure a lower bound $\Kempirical$ on the discrimination boundary (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistical features and an Ordinal Binary Decomposition (OBD) LightGBM classifier.
15	We operationalize $\Kempirical$ as the deepest $k \geq 1$ where the pairwise $\auc_{k-1,k}$ exceeds $\theta = 0.60$ (Section~\ref{sec:formulation}).
16	
17	Our contributions:
18	\begin{enumerate}[label=(\alph*),nosep]
19	  \item \textbf{$\Kempirical$ as a measurement tool} across 10 model configurations (6 families, 1B--8B) and 4 decoding strategies ($p \leq 0.002$; Section~\ref{sec:kstar_boundary}):
20	  For web text, $\Kempirical \leq 2$ regardless of family or scale; $\Kempirical \leq 3$ universally.
21	  $\Kempirical$ establishes binary sufficiency for web text by measurement (not assumption), reveals domain-dependent variation (arXiv $\Kempirical{=}3$), and quantifies boundary sensitivity to threshold, scorer, and model scale.
22	  Both supervised OBD and zero-shot LLMs fail beyond $\Kempirical$ (McNemar $p > 0.05$; Section~\ref{sec:why_kstar}).
23	  \item \textbf{Domain dependence of $\Kempirical$}: general web text (C4, Wikipedia) yields $\Kempirical{=}2$, while structured academic text (arXiv) yields $\Kempirical{=}3$, consistent across model families (Section~\ref{sec:cross_domain}).
24	  \item \textbf{Model-free cross-model transfer}: 15 statistical features enable 80--100\% accuracy retention with scorer-invariant feature rankings ($\rho > 0.90$), supporting model-agnostic depth estimation without retraining; $\Kempirical$ agreement holds across scorers for strong-signal configurations (Section~\ref{sec:transfer}).
25	\end{enumerate}
26	
27	\noindent As a consistency check, $\Kempirical{=}2$ correctly predicts the strategy ordering for web-text filtering: binary curation minimizes degradation most effectively (MMLU $0.5941$ vs.\ base $0.6018$; Section~\ref{sec:filtering}).
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78757045-328e-4768-9494-bf851b859edd",
  "isSidechain": true,
  "promptId": "bed57f34-927e-4cb2-bd8a-b1a329fa1fbe",
  "agentId": "a8deb1249dd0a8798",
  "type": "user",
  "uuid": "1b12c07b-17f4-4084-8a49-f75a52e2aec5",
  "sourceToolAssistantUUID": "78757045-328e-4768-9494-bf851b859edd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T21:21:45.963Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B6ehJoJAfUV7d78jXW23tk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b12c07b-17f4-4084-8a49-f75a52e2aec5",
  "isSidechain": true,
  "agentId": "a8deb1249dd0a8798",
  "requestId": "req_011CbJJrDu3QDf9yb7QjkxJG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0cac4f15-950c-42d3-82f7-063a714fdf88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015yc3KopAaTUV11o47MM9kc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19301,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19301,
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

_source line 6 · 2026-05-22T21:21:45.967Z_

<details><summary>↩ Tool result · `toolu_01B6ehJoJAfUV7d78jXW23tk`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and recursive degradation.}
5	Iterative training on model outputs causes tail-distribution degradation~\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong, fu2025theoretical}, diversity contraction~\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, wang2025unveiling}.
6	Our prompt-chain operates in the replace regime~\cite{kazdan2025collapse}, making $\Kempirical = 2$ a conservative lower bound.
7	This literature characterizes macro dynamics but provides no per-text depth estimation, the gap we address.
8	
9	\paragraph{Beyond binary detection.}
10	Binary detectors~\cite{mitchell2023detectgpt, bao2024fast, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate.
11	Recent work extends beyond binary labels to collaboration degree~\cite{cheng2025beyond}, contamination hierarchies~\cite{mehta2025beyond}, and multigenerator benchmarks~\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\cite{hao2025rewrite}; CoDeC~\cite{zawalski2026codec} addresses contamination via membership inference.
12	None estimates recursive generation depth.
13	
14	\paragraph{Data selection and curation.}
15	DSIR~\cite{xie2023dsir}, D4~\cite{tirumala2023d4}, and DoReMi~\cite{xie2023doremi} are depth-agnostic; Drayson et al.~\cite{drayson2025} combined binary detection with importance resampling, a special case when $\Kstar = 1$.
16	
17	\paragraph{Ordinal classification and probing.}
18	Our OBD classifier follows Frank \& Hall's~\cite{frank2001ordinal} binary decomposition; our neural probe extends probing~\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0cac4f15-950c-42d3-82f7-063a714fdf88",
  "isSidechain": true,
  "promptId": "bed57f34-927e-4cb2-bd8a-b1a329fa1fbe",
  "agentId": "a8deb1249dd0a8798",
  "type": "user",
  "uuid": "76e8e865-80a1-4408-acb1-85d50f1d9dde",
  "sourceToolAssistantUUID": "0cac4f15-950c-42d3-82f7-063a714fdf88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T21:21:46.384Z_

<details open><summary>🔧 Tool call — Read · `toolu_014ovdVSuJs2CU1Hj7e5zgen`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76e8e865-80a1-4408-acb1-85d50f1d9dde",
  "isSidechain": true,
  "agentId": "a8deb1249dd0a8798",
  "requestId": "req_011CbJJrDu3QDf9yb7QjkxJG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "df5cfcdd-8cc4-400c-9352-b9f1f065e038",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015yc3KopAaTUV11o47MM9kc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19301,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19301,
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

_source line 8 · 2026-05-22T21:21:46.388Z_

<details><summary>↩ Tool result · `toolu_014ovdVSuJs2CU1Hj7e5zgen`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/pipeline.pdf}
7	\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\delta$ to produce a depth chain. Corpus-level statistical features are fed to the OBD-LightGBM classifier for depth prediction.}
8	\label{fig:pipeline}
9	\end{figure*}
10	
11	\subsection{Problem Formulation}
12	\label{sec:formulation}
13	
14	A generation operator $G_\delta$ (LLM + decoding strategy $\delta$) produces successive generations $X \to Y_1 \to \cdots \to Y_K$, where $Y_k = G_\delta(Y_{k-1})$ and $Y_0 \triangleq X$ (Figure~\ref{fig:pipeline}).
15	This sequence forms a Markov chain.
16	By the Data Processing Inequality, $I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0$: mutual information with the seed text degrades monotonically.
17	Together with Markov chain convergence, this provides heuristic motivation for expecting $\auc_{k-1,k}$ to decrease with $k$, though AUC and mutual information are not formally equivalent; the actual saturation depth must therefore be measured empirically.
18	
19	We define the operational lower bound:
20	\begin{equation}
21	  \Kempirical = \max\!\bigl\{k \!\geq\! 1 : \auc_{j-1,j} > \theta,\;\forall\, j \!\leq\! k\bigr\},
22	  \label{eq:kstar}
23	\end{equation}
24	which requires all pairs up to depth $k$ to exceed the threshold (the $\forall j$ constraint is naturally satisfied because $\auc_{k-1,k}$ decreases monotonically above $\theta$ across all tested configurations; Table~\ref{tab:kstar_ci}).
25	The theoretical upper bound $\Ktheory$ (the true maximum discriminable depth given optimal features) is not directly estimated in this work.
26	Since any specific classifier on a feature subset achieves AUC at most equal to the Bayes-optimal classifier on all features, $\Kempirical \leq \Ktheory$ follows directly.
27	The DPI separately motivates the empirical observation that $\auc_{k-1,k}$ decreases with $k$, though AUC is not a monotone function of MI (as noted above).
28	Here $\auc_{k-1,k}$ is the point-estimate pairwise AUC and $\theta = 0.60$ is a reference operating point motivated by Cohen's small-effect-size convention ($h \approx 0.20$\footnote{$h = 2\arcsin\!\sqrt{0.60} - 2\arcsin\!\sqrt{0.50} \approx 0.2014$, a ``small'' effect size by Cohen's (1988) convention.}; justified below).
29	Bootstrap 95\% CIs (1{,}000 resamples) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\theta$ and non-boundary-pair CI upper bounds fall below $\theta$ (Section~\ref{sec:kstar_boundary}).
30	
31	\paragraph{Threshold justification.}
32	$\theta{=}0.60$ is a reference operating point supported by three independent lines of evidence.
33	First, Cohen's $h \approx 0.20$, a conventional small-effect-size boundary.
34	Second, a 10{,}000-iteration permutation test yields a 95th-percentile null of ${<}\,0.55$ ($p < 0.002$ for all boundary comparisons).
35	Third, the conclusion $\Kempirical{=}2$ is insensitive to the exact threshold: 1v2 AUC values cluster at $0.61$--$0.70$ while 2v3 values cluster at $0.55$--$0.59$, a ${\sim}$5--11\,pp discontinuity; only at extremes does $\Kempirical$ shift ($\theta{=}0.55$: $\Kempirical{=}3$ for two Qwen configurations; $\theta{=}0.70$: $\Kempirical{=}1$ across all).
36	Figure~\ref{fig:kstar_theta} provides the full sensitivity surface across $\theta \in [0.55, 0.70]$, enabling practitioners to select $\theta$ according to their false-positive tolerance.
37	The downstream filtering evaluation (Section~\ref{sec:filtering}) uses the OBD classifier without re-optimizing $\theta$, avoiding circularity.
38	
39	\subsection{Features and Classifier}
40	\label{sec:features}
41	
42	Each document is characterized by a 15-dimensional feature vector spanning four groups: \emph{surprisal moments} (mean, std, skewness, kurtosis; 4~dims), \emph{surprisal derivatives} (mean and std of first- and second-order differences, plus first-order skewness; 5~dims), \emph{vocabulary diversity} (type-token ratio, hapax legomena ratio, self-BLEU; 3~dims), and \emph{frequency tail statistics} (frequency kurtosis, entropy, rare token fraction; 3~dims).
43	All features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\ref{tab:s5_features}, Appendix).
44	Self-BLEU is computed within each CV fold using only same-fold, same-depth reference samples to prevent leakage; it ranks \#1 in 1/8 conditions (greedy decoding) but is absent from the top-3 in all 7 others.
45	Removing self-BLEU reduces mean $\auc_{1v2}$ by $< 1$\,pp across all models (14D $\Kempirical = 2$ for all 4 configurations); in deployment where reference corpora are unavailable, self-BLEU can be replaced with corpus-level self-similarity or omitted entirely, leaving 14 features (surprisal statistics, TTR, hapax ratio, frequency tail) that require no external reference and retain full $\Kempirical$.
46	Hand-crafted features enable cross-generator transfer without retraining and permit attribution of discriminative power to specific text properties.
47	
48	We use \emph{Ordinal Binary Decomposition} (OBD), decomposing the $(K{+}1)$-class problem into $K$ cumulative binary sub-classifiers, each estimating $P(\text{depth} > k \mid \mathbf{x})$ via LightGBM (hyperparameters in Table~\ref{tab:s6_lgbm_params}).
49	OBD achieves lower MAE than multiclass LightGBM (e.g., 0.984 vs.\ 1.016 on Qwen-rewrite) while maintaining superior pairwise $\auc$ (mean 0.6095 vs.\ 0.4883 for ordinal logistic regression).
50	
51	\subsection{Experimental Setup}
52	\label{sec:experimental_setup}
53	
54	We evaluate six configurations spanning three model families (Table~\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Qwen2.5-1.5B (base, continuation), Qwen2.5-7B (continuation), Pythia-1.4B and OLMo-1B (continuation).
55	Each uses 5{,}000 C4 seeds truncated to 256 tokens, recursively generated for $K{=}5$ iterations (30{,}000 documents per configuration).
56	Default decoding: nucleus $p{=}0.95$, $T{=}1.0$; decoding ablation covers greedy, $T{=}0.7$, and $T{=}1.2$.
57	Continuation mode truncates seeds to 128 tokens and extends to 256; rewrite mode paraphrases the full text.
58	Evaluation: 5-fold GroupKFold cross-validation grouped by seed document; pairwise $\auc$ as primary metric.
59	
60	\begin{table}[t]
61	\centering
62	\small
63	\caption{Experimental configurations for depth-chain generation. \textbf{Config}: shorthand identifier; \textbf{Model}: architecture and parameter count; \textbf{Mode}: generation strategy (continuation or rewrite); $N$: number of seed documents per depth level.}
64	\label{tab:setup}
65	\begin{tabular}{llcc}
66	\toprule
67	\textbf{Config} & \textbf{Model} & \textbf{Mode} & $N$ \\
68	\midrule
69	Qwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite & 5{,}000 \\
70	Qwen-cont & Qwen2.5-1.5B-Instruct & Continuation & 5{,}000 \\
71	Qwen-base & Qwen2.5-1.5B          & Continuation & 5{,}000 \\
72	Pythia    & Pythia-1.4B            & Continuation & 5{,}000 \\
73	OLMo      & OLMo-1B               & Continuation & 5{,}000 \\
74	Qwen-7B   & Qwen2.5-7B            & Continuation & 5{,}000 \\
75	\bottomrule
76	\end{tabular}
77	\end{table}
78	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df5cfcdd-8cc4-400c-9352-b9f1f065e038",
  "isSidechain": true,
  "promptId": "bed57f34-927e-4cb2-bd8a-b1a329fa1fbe",
  "agentId": "a8deb1249dd0a8798",
  "type": "user",
  "uuid": "0c33893b-53a2-4a10-9111-d1173955a63b",
  "sourceToolAssistantUUID": "df5cfcdd-8cc4-400c-9352-b9f1f065e038",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T21:21:46.599Z_

<details open><summary>🔧 Tool call — Read · `toolu_018ehR8EUeTYJU1gskui8eP2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c33893b-53a2-4a10-9111-d1173955a63b",
  "isSidechain": true,
  "agentId": "a8deb1249dd0a8798",
  "requestId": "req_011CbJJrDu3QDf9yb7QjkxJG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f7361588-c01e-4826-a289-3c6cab46f940",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015yc3KopAaTUV11o47MM9kc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19301,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19301,
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

_source line 10 · 2026-05-22T21:21:46.603Z_

<details><summary>↩ Tool result · `toolu_018ehR8EUeTYJU1gskui8eP2`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on ten model configurations spanning six architecture families:
5	Pythia-1.4B, Pythia-6.9B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, LLaMA-3.1-8B, Mistral-7B, and Gemma-2-2B, all in continuation mode except where noted.
6	All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).
7	
8	%% ====================================================================
9	\subsection{$\Kempirical \leq 2$ Across Model Configurations (C4)}
10	\label{sec:kstar_boundary}
11	
12	\begin{table*}[t]
13	\centering
14	\small
15	\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
16	$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.
17	Extended results (all models) in Table~\ref{tab:kstar_ci_extended}.}
18	\label{tab:kstar_ci}
19	\begin{tabular}{lcccccccccc}
20	\toprule
21	 & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
22	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
23	 & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
24	\midrule
25	0v1 & .9956 & & .9932 & & .9860 & & .9971 & & .9638 & [.961,\,.967] \\
26	1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .5080 & [.496,\,.519] & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
27	2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .4973 & [.486,\,.509] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] \\
28	3v4 & .5435 & & .5152 & & .5024\rlap{$^\S$} & & .5409 & & .5276 & \\
29	4v5 & .5340 & & .5136 & & .4942 & & .5141 & & .5085 & \\
30	\bottomrule
31	\multicolumn{11}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all 1v2 comparisons shown.} \\
32	\multicolumn{11}{l}{\footnotesize $^\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.} \\
33	\multicolumn{11}{l}{\footnotesize $^\S$OLMo 2v3 (0.497) $<$ 3v4 (0.502): non-monotonic reversal within noise ($\Delta = 0.005$).} \\
34	\multicolumn{11}{l}{\footnotesize Full results for all 10 configurations (including Qwen-7B, Qwen-base, Gemma-2-2B, and Pythia-6.9B) are provided in Table~\ref{tab:kstar_ci_extended}.}
35	\end{tabular}
36	\end{table*}
37	
38	\begin{figure}[t]
39	\centering
40	\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
41	\caption{Pairwise $\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed); shaded bands show bootstrap 95\% confidence intervals. The horizontal dashed line marks $\theta = 0.60$.}
42	\label{fig:auc_decay}
43	\end{figure}
44	
45	Table~\ref{tab:kstar_ci} and Figure~\ref{fig:auc_decay} show $\Kempirical \leq 2$ across all 10 model configurations: 6/10 configurations yield $\Kempirical{=}2$ (Qwen with 4 configs, LLaMA-8B, and Pythia-1.4B, spanning three of six families) (1v2 $\auc$ range: 0.6112--0.6955; all CI lower bounds $> \theta$; permutation $p < 0.001$), while OLMo-1B, Mistral-7B, Pythia-6.9B, and Gemma-2-2B yield $\Kempirical{=}1$ (1v2 $\auc$: 0.508, 0.594, 0.596, and 0.598, all below $\theta$; Section~\ref{sec:boundary_cases}).
46	Under Bonferroni correction for 10 simultaneous comparisons (99.5\% CIs), four of six boundary configurations retain CI lower bounds above $\theta$; the two most marginal cases, Qwen-continuation (nominal CI lower bound 0.602) and LLaMA-8B (0.603), fall below the widened interval.
47	Both retain point estimates above $\theta$ and uncorrected CI lower bounds above $\theta$; the near-misses reflect narrow effect sizes rather than classification failure.
48	By architecture family: Qwen (4/4) and LLaMA (1/1) yield $\Kempirical{\geq}2$ at nominal significance; OLMo (1/1), Mistral (1/1), and Gemma (1/1) yield $\Kempirical{=}1$; Pythia exhibits a scale-dependent split (1.4B: $\Kempirical{=}2$, 6.9B: $\Kempirical{=}1$).
49	LLaMA-3.1-8B confirms $\Kempirical{=}2$ (0v1 $\auc = 0.9225$, 1v2 $\auc = 0.6123\;[0.603,\,0.622]$; CI lower bound above $\theta$; Table~\ref{tab:kstar_ci_extended}).
50	All four decoding strategies likewise yield $\Kempirical{=}2$ (Table~\ref{tab:s2_decoding}).
51	The 1v2 spread due to generation mode ($\Delta = 8.4$\,pp within Qwen) exceeds the spread across $\Kempirical{=}2$ continuation models ($\Delta = 4.3$\,pp).
52	
53	\paragraph{Scale and instruction-tuning invariance.}
54	$\Kempirical{=}2$ persists from 1.5B through 8B: Qwen-7B (1v2 $\auc = 0.6168$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\auc = 0.6123$) both exceed $\theta$, despite progressively reduced 0v1 signal (0.9638 and 0.9225 vs.\ $> 0.99$ at $\leq$1.5B).
55	A base-vs.-instruct ablation at 1.5B likewise yields $\Kempirical = 2$ (1v2 $\auc = 0.626$), confirming the boundary is not an instruction-tuning artifact.
56	
57	\begin{figure*}[t]
58	\centering
59	\includegraphics[width=0.75\textwidth]{figures/fig_kstar_theta.pdf}
60	\caption{$\Kempirical(\theta)$ sensitivity curve for six configurations. $\Kempirical$: maximum discriminable depth; $\theta$: AUC decision threshold. Five of six configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (dashed line); OLMo yields $\Kempirical{=}1$. At $\theta{=}0.70$, all drop to $\Kempirical{=}1$.}
61	\label{fig:kstar_theta}
62	\end{figure*}
63	
64	The raw AUC gap between adjacent generations provides a threshold-free continuous measure of discriminability; Figure~\ref{fig:kstar_theta} displays the full sensitivity surface across $\theta \in [0.55, 0.70]$, allowing practitioners to read off $\Kempirical$ at any desired effect-size threshold.
65	Five of six configurations yield $\Kempirical = 2$ within $\theta \in [0.51, 0.61]$ (OLMo: $\Kempirical = 1$ throughout); at $\theta{=}0.55$, two Qwen configurations reach $\Kempirical = 3$; at $\theta{=}0.70$, all drop to $\Kempirical = 1$.
66	All four decoding strategies likewise yield $\Kempirical = 2$ at $\theta{=}0.60$ (1v2 $\auc \in [0.687, 0.704]$; Table~\ref{tab:s2_decoding}).
67	
68	%% ====================================================================
69	\subsection{Cross-Model Transfer}
70	\label{sec:transfer}
71	
72	\begin{figure}[t]
73	\centering
74	\includegraphics[width=\columnwidth]{figures/fig3_transfer_heatmap.pdf}
75	\caption{Cross-model transfer heatmap. Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by in-domain accuracy (retention rate). Pythia$\leftrightarrow$OLMo: 90--92\%; Qwen-rewrite$\to$continuation: 61--63\%.}
76	\label{fig:transfer_heatmap}
77	\end{figure}
78	
79	Continuation-mode classifiers transfer well across generators (Figure~\ref{fig:transfer_heatmap}; full matrix in Table~\ref{tab:s1_transfer}): Pythia$\leftrightarrow$OLMo retains 90--92\%, Qwen-cont$\leftrightarrow$Pythia 84--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\% (0v1 cross-model $\auc > 0.96$ for all pairs).
80	Qwen-rewrite classifiers transfer poorly (61--63\%), confirming reliance on mode-specific artifacts rather than generalizable depth features.
81	
82	\paragraph{Cross-scorer validation.}
83	Replacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\rho > 0.90$) but attenuates absolute discriminability at the boundary (Table~\ref{tab:crossscorer}).
84	Feature ranking independence is a strong result: the same features dominate under all scorers.
85	$\Kempirical$ agreement, however, is signal-strength dependent: Qwen-rewrite (strong signal, 1v2 $\auc = 0.696$) retains $\Kempirical{=}2$ under all scorers, but Qwen-continuation (marginal, 1v2 $\auc = 0.611$, only 0.011 above $\theta$) drops to $\Kempirical{=}1$ (Pythia: $0.5923$; OLMo: $0.5858$).
86	A three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair; Table~\ref{tab:anova_crossscorer}) confirms a statistically significant but modest Scorer main effect ($\eta^2_p{=}.166$, $p < .001$) and a significant Generator$\times$Scorer interaction ($\eta^2_p{=}.146$), indicating that absolute AUC values are scorer-dependent even when $\Kempirical$ classifications largely agree.
87	
88	%% ====================================================================
89	\subsection{Feature Ordering and Generation Mode}
90	\label{sec:feature_degradation}
91	\label{sec:generation_mode}
92	
93	Among continuation-mode models, single-feature $\auc$ rankings are highly correlated ($\rho \geq 0.85$; Table~\ref{tab:top_features}).
94	The top-3 features (\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}) are shared across all three families, revealing that autoregressive generation progressively damps surprisal variability.
95	Qwen-rewrite diverges (\texttt{freq\_entropy} dominates), consistent with its poor cross-model transfer (61--63\%).
96	Within Qwen, rewrite yields 1v2 $\auc = 0.6955$ vs.\ continuation's $0.6112$ ($\Delta = +8.4$\,pp); continuation mode is therefore recommended as the canonical condition.
97	
98	%% ====================================================================
99	\subsection{Neural Probe}
100	\label{sec:neural_probe}
101	
102	Replacing the 15D features with frozen encoder hidden states (MLP probe; Table~\ref{tab:neural_probe_crossmodel}), Qwen achieves $\Kempirical^{\text{neural}} = 3$ (2v3 $\auc = 0.6159$), while Pythia remains at $\Kempirical^{\text{neural}} = 2$ ($\auc_{2v3} = 0.5963$); OLMo yields $\Kempirical^{\text{neural}} = 1$ (1v2 $\auc = 0.5054$, consistent with its 15D boundary).
103	We hypothesize that the Qwen-only elevation reflects self-familiarity artifacts, consistent with the poor transfer observed in Section~\ref{sec:transfer}; the 15D features yield $\Kempirical = 2$ for most families (OLMo: $\Kempirical = 1$).
104	
105	\noindent\begin{minipage}{\columnwidth}
106	\centering
107	\footnotesize
108	\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\ $d{+}1$ text. $\Kempirical^{\text{neural}}$: maximum depth where AUC exceeds $\theta = 0.60$.}
109	\label{tab:neural_probe_crossmodel}
110	\resizebox{\columnwidth}{!}{%
111	\begin{tabular}{lccc}
112	\toprule
113	\textbf{Model} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & $\Kempirical^{\text{neural}}$ \\
114	\midrule
115	Qwen-1.5B  & 0.6159 & $[0.610,\,0.622]$ & 3 \\
116	Pythia-1.4B & 0.5963 & $[0.589,\,0.603]$ & 2 \\
117	OLMo-1B    & 0.5056 & $[0.497,\,0.516]$ & 1\rlap{$^\dagger$} \\
118	\bottomrule
119	\multicolumn{4}{l}{\footnotesize $^\dagger$OLMo 1v2 $\auc = 0.5054$ (below $\theta$); $\Kempirical^{\text{neural}} = 1$.}
120	\end{tabular}}
121	\end{minipage}
122	
123	%% ====================================================================
124	\subsection{Cross-Domain Variation}
125	\label{sec:cross_domain}
126	
127	The preceding experiments use C4 (general web text).
128	To test domain dependence, we evaluate on Wikipedia ($n{=}5{,}000$) and arXiv abstracts ($n{=}2{,}200$) using two model families.
129	Wikipedia yields $\Kempirical{=}2$ (1v2 $\auc = 0.623$, 2v3 $\auc = 0.571$), matching the C4 baseline.
130	Both Qwen-1.5B and Pythia-1.4B yield $\Kempirical{=}3$ for arXiv (Table~\ref{tab:domain_kstar}): 2v3 $\auc = 0.644\;[0.628,\,0.658]$ and $0.655\;[0.640,\,0.669]$ respectively (bootstrap CI lower bounds above $\theta$; permutation $p < 0.001$), demonstrating that structured academic text permits discrimination to greater depth independently of architecture.
131	The elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4), as formulaic structure amplifies deviation from domain norms.
132	
133	\begin{table}[t]
134	\centering
135	\footnotesize
136	\caption{Cross-domain $\Kempirical$ comparison. Rows: generator model and text domain (C4, Wikipedia, arXiv). $\Kempirical{=}3$ for arXiv indicates structured text preserves discriminability to greater depth.}
137	\label{tab:domain_kstar}
138	\begin{tabular}{llccc}
139	\toprule
140	\textbf{Domain} & \textbf{Model} & \textbf{1v2 $\auc$} & \textbf{2v3 $\auc$} & $\Kempirical$ \\
141	\midrule
142	arXiv & Qwen-1.5B  & 0.858 & 0.6436 & 3 \\
143	arXiv & Pythia-1.4B & 0.805 & 0.6545 & 3 \\
144	C4    & Qwen-1.5B  & 0.63  & 0.56   & 2 \\
145	Wikipedia & Qwen-1.5B & 0.62 & 0.55 & 2 \\
146	\bottomrule
147	\end{tabular}
148	\end{table}
149	
150	\paragraph{Robustness.}
151	\label{sec:robustness}
152	$\Kempirical{=}2$ holds across segment lengths of 128, 256, and 512 tokens (Table~\ref{tab:s11_length_ablation}); at 512 tokens the 1v2 CI lower bound falls marginally below $\theta$ but 2v3 remains well below $\theta$ at all lengths ($\leq 0.572$).
153	Seed robustness testing (seed $= 123$ vs.\ primary $= 42$; Table~\ref{tab:seed_robustness}) confirms $\Kempirical$ stability in 2/3 configurations; the one marginal shift (Qwen-Wikipedia $\Kempirical{=}2 \to 3$, 2v3 $\auc = 0.607$) has one of five folds below $\theta$.
154	The ${\pm}9$\,pp absolute AUC variation across seeds strengthens the case for threshold-based $\Kempirical$ over raw AUC comparisons.
155	
156	%% ====================================================================
157	\subsection{Binary Detector Confidence}
158	\label{sec:binary_confidence}
159	
160	Binary detectors (DivEye~\cite{basani2026diveye}, Binoculars~\cite{hans2024binoculars}) show moderate rank correlations with depth ($|\rho| = 0.06$--$0.46$; Table~\ref{tab:s9_binary_spearman}) but fail as depth proxies: 6-class accuracy is at or below chance ($\leq 0.199$ vs.\ 0.167 baseline), pairwise $\auc$ yields $\Kempirical^{\text{binary}} \leq 1$, and multiple conditions exhibit non-monotonic AUC at deeper pairs.
161	The observed correlation is an artifact of 0v1 separation rather than fine-grained depth signal.
162	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7361588-c01e-4826-a289-3c6cab46f940",
  "isSidechain": true,
  "promptId": "bed57f34-927e-4cb2-bd8a-b1a329fa1fbe",
  "agentId": "a8deb1249dd0a8798",
  "type": "user",
  "uuid": "c6638290-306f-487e-86c2-3461829ece8e",
  "sourceToolAssistantUUID": "f7361588-c01e-4826-a289-3c6cab46f940",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T21:21:46.843Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BdZy463nZM4mAKEg3MsJLj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6638290-306f-487e-86c2-3461829ece8e",
  "isSidechain": true,
  "agentId": "a8deb1249dd0a8798",
  "requestId": "req_011CbJJrDu3QDf9yb7QjkxJG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7d87d724-3891-4a6c-9924-5c440b80e61d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015yc3KopAaTUV11o47MM9kc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19301,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19301,
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

_source line 12 · 2026-05-22T21:21:46.848Z_

<details><summary>↩ Tool result · `toolu_01BdZy463nZM4mAKEg3MsJLj`</summary>

```text
1	\section{Consistency Check: $\Kstar$-Guided Filtering}
2	\label{sec:filtering}
3	
4	$\Kempirical = 2$ makes a falsifiable prediction: binary curation should suffice, and graduated performance should converge toward binary as the decay steepness increases.
5	We test this as a consistency check on the boundary measurement, not as an independent contribution.
6	We compare six strategies on 30{,}000 documents (depths 0--5): (i)~\textbf{no-filter}, (ii)~\textbf{binary-ours} ($w = 1 - P(\text{synthetic})$ from 15D LightGBM), (iii)~\textbf{binary-Drayson}~\citep{drayson2025}, (iv)~\textbf{graduated} ($w = \exp(-\alpha \cdot \hat{d})$, $\alpha \in \{0.1,\ldots,0.9\}$), (v)~\textbf{surprisal} (retain above median), and (vi)~\textbf{DSIR}~\citep{xie2023dsir}.
7	We fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\alpha_{\text{LoRA}}{=}16$) for 3 epochs on MMLU and HellaSwag across 5 seeds (51 total runs; this 100\% synthetic setting is an upper bound~\cite{shumailov2024collapse, dohmatob2024model}).
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Downstream task performance (MMLU, HellaSwag) under six data-filtering strategies. Binary-ours uses the 15D LightGBM depth classifier; Graduated applies exponentially decaying weights $w = \exp(-\alpha \hat{d})$. Mean $\pm$ std over 5 seeds. Full $\alpha$ sweep in Appendix~\ref{sec:extended_limitations}.}
13	\label{tab:tab_filtering_main}
14	\resizebox{\columnwidth}{!}{\input{tables/tab_filtering_main}}
15	\end{table}
16	
17	Binary-ours minimizes MMLU degradation most effectively (Table~\ref{tab:tab_filtering_main}), reducing the gap from $-$1.53\,pp (no-filter) to $-$0.77\,pp (${\sim}$50\% reduction; $p_{\text{corr}} < 0.05$ vs.\ all alternatives).
18	These effects are measured in a 100\% synthetic upper-bound setting; real-world contamination ratios are typically lower, and effect sizes would scale accordingly.
19	The strategy ordering is interpretable through $\Kempirical$: binary filtering exploits the one reliable boundary (0v1), while graduated strategies assign weights to depths 2--5 based on near-random classifier outputs, injecting noise.
20	Graduated filtering converges monotonically toward binary: at $\alpha{=}0.9$, it matches binary-ours on HellaSwag exactly ($\Delta = 0$, $p_{\text{corr}} = 1.00$) but remains significantly worse on MMLU ($p_{\text{corr}} = 0.011$).
21	DSIR is indistinguishable from no-filter, confirming that depth-aware features are necessary for curation in recursively contaminated corpora (Figure~\ref{fig:filtering_strategies} in Appendix).
22	At realistic contamination ratios ($\leq$50\%), all filtering strategies converge ($p > 0.12$), consistent with the one-wash laundering finding that depth-aware curation offers marginal benefit when $\Kempirical{=}2$ (Appendix~\ref{sec:dose_response}).
23	For $\Kempirical{=}1$ configurations, depth-aware curation reduces to standard binary filtering, consistent with $\Kempirical{=}1$ implying no exploitable depth signal beyond the 0v1 boundary.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d87d724-3891-4a6c-9924-5c440b80e61d",
  "isSidechain": true,
  "promptId": "bed57f34-927e-4cb2-bd8a-b1a329fa1fbe",
  "agentId": "a8deb1249dd0a8798",
  "type": "user",
  "uuid": "33509a4b-6bad-4174-b73b-493f6c93ae8c",
  "sourceToolAssistantUUID": "7d87d724-3891-4a6c-9924-5c440b80e61d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T21:21:47.020Z_

<details open><summary>🔧 Tool call — Read · `toolu_016cHR5HYiGuURz2zi8TvGHz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33509a4b-6bad-4174-b73b-493f6c93ae8c",
  "isSidechain": true,
  "agentId": "a8deb1249dd0a8798",
  "requestId": "req_011CbJJrDu3QDf9yb7QjkxJG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c25d43d1-f6a8-4db1-80dd-2f41642ba105",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015yc3KopAaTUV11o47MM9kc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19301,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19301,
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

_source line 14 · 2026-05-22T21:21:47.025Z_

<details><summary>↩ Tool result · `toolu_016cHR5HYiGuURz2zi8TvGHz`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	\label{sec:why_kstar}
4	\label{sec:one_wash}
5	\label{sec:negative_graduated}
6	\label{sec:repr_dependence}
7	\label{sec:boundary_cases}
8	\label{sec:length_confound}
9	
10	\paragraph{One-wash laundering (web text).}
11	For general web text, $\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\auc \geq 0.92$), 1v2 drops by ${\sim}$30\,pp, and 2v3 falls below $\theta$.
12	A single generation pass renders text indistinguishable from multiply recycled content, limiting depth-aware curation to a binary boundary.
13	Converging evidence supports a data-intrinsic interpretation: OBD achieves 96\% depth-0 recall but only 14--22\% for depths 2--4; frontier LLMs show 8--38\% (McNemar $p > 0.05$ vs.\ OBD; Table~\ref{tab:s3_llm_zeroshot}).
14	
15	\paragraph{Representation dependence.}
16	$\Kempirical$ is representation-dependent: frozen Qwen embeddings yield $\Kempirical^{\text{neural}} = 3$, while Pythia yields $\Kempirical^{\text{neural}} = 2$ and OLMo yields $\Kempirical^{\text{neural}} = 1$, consistent with its 15D boundary (Table~\ref{tab:neural_probe_crossmodel}).
17	The 15D features trade one depth level of sensitivity for cross-model consistency (6/10 configurations $\Kempirical{=}2$), making them the preferred operational choice.
18	Feature rankings are scorer-independent ($\rho > 0.90$); $\Kempirical$ agreement is scorer-independent for strong-signal configurations (e.g., Qwen-rewrite retains $\Kempirical{=}2$ under all scorers) but scorer-sensitive at marginal boundaries (Qwen-continuation drops to $\Kempirical{=}1$; length confound ruled out in Appendix~\ref{sec:extended_limitations}).
19	ANOVA confirms this layered pattern: Scorer explains modest variance ($\eta^2_p{=}.166$) with a significant Generator$\times$Scorer interaction ($\eta^2_p{=}.146$; Table~\ref{tab:anova_crossscorer}).
20	
21	\paragraph{Domain dependence of $\Kempirical$.}
22	Web text (C4, Wikipedia) consistently yields $\Kempirical{=}2$, while structured academic text (arXiv) yields $\Kempirical{=}3$ across two independent model families (Qwen-1.5B and Pythia-1.4B; Section~\ref{sec:cross_domain}).
23	The elevated arXiv signal reflects formulaic structure: citation patterns, mathematical notation, and section conventions create larger per-generation distributional shifts (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4), making contamination trackable to greater depth.
24	Wikipedia matches C4 at $\Kempirical{=}2$ (1v2 $\auc = 0.623$, 2v3 $\auc = 0.571$), consistent with its general-purpose prose lacking domain-specific structural markers.
25	This domain dependence implies that corpus curators should calibrate depth-aware filtering to source characteristics rather than assuming a universal boundary.
26	
27	\paragraph{Cross-model transfer.}
28	Continuation-mode classifiers transfer well across generators (80--92\% retention; Figure~\ref{fig:transfer_heatmap}), enabling portable depth estimation on corpora from unknown models without retraining.
29	The poor transfer from rewrite-mode classifiers (61--63\%) isolates generation mode, rather than architecture family, as the primary axis of distributional variation.
30	
31	\paragraph{Prompt-chain scope and retrain-chain gap.}
32	Retrain-chain experiments (Pythia-1.4B LoRA) yield $\Kempirical{\geq}4$ (1v2 $\auc = 0.9484$, 3v4 $= 0.7982$), far exceeding the prompt-chain boundary of $\Kempirical{=}2$, because each retrain generation also modifies model parameters, introducing cumulative adaptation artifacts absent from text-only recycling.
33	Prompt-chain $\Kempirical$ isolates text-intrinsic degradation, the operationally relevant quantity for data curation pipelines; our conclusions do not directly transfer to retrain-chain (model collapse) settings.
34	
35	\paragraph{Boundary cases and scale effect.}
36	$\Kempirical{=}1$ configurations cluster at 1v2 $\auc$ 0.508--0.598, well separated from the $\Kempirical{=}2$ range (0.611--0.696); $\Kempirical{=}1$ is not a classifier failure but a text property, as these models produce first-generation output so human-like that statistical features cannot distinguish depth~1 from depth~2.
37	That $\Kempirical \in \{1, 2\}$ for all web text configurations is the core empirical result; larger models reduce 0v1 JSD (0.077 at 8B vs.\ 0.15--0.27 at $\leq$1.5B), suggesting 13B+ may increasingly yield $\Kempirical{=}1$.
38	The $\Kempirical{=}1$ vs.\ $\Kempirical{=}2$ distinction has a direct curation consequence: $\Kempirical{=}1$ generators erase depth signal in one pass, leaving only the binary 0v1 boundary available for filtering.
39	
40	\paragraph{Decoding strategy as confound.}
41	Greedy decoding inflates depth separability: Pythia-6.9B yields $\Kempirical{=}2$ under greedy but $\Kempirical{=}1$ under nucleus sampling ($p{=}0.95$), with the borderline 1v2 score (2 of 5 folds above $\theta$) illustrating that the boundary is continuous rather than a cliff (Table~\ref{tab:s10_pythia_decoding}).
42	Practitioners should calibrate $\theta$ to their application-specific tolerance (Figure~\ref{fig:kstar_theta}).
43	
44	\paragraph{What $\Kempirical$ reveals.}
45	As a measurement tool, $\Kempirical$ establishes why binary detection suffices for web text (depth${>}1$ is invisible to statistical features), identifies domains where finer strategies are viable (arXiv $\Kempirical{=}3$), and quantifies how scale, scorer, and threshold jointly shape the boundary.
46	The OBD framework provides a reproducible, low-cost depth estimation protocol requiring only corpus-level statistical features, unlike detection methods that need API access or model weights.
47	Even when the practical outcome remains binary filtering, $\Kempirical$ grounds this choice in measurement rather than heuristic assumption.
48	$\Kempirical$ also serves as a monitoring metric for tracking how the discrimination boundary shifts as model scale increases; future work may explore scorer-ensemble strategies to improve cross-scorer robustness at marginal boundaries.
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c25d43d1-f6a8-4db1-80dd-2f41642ba105",
  "isSidechain": true,
  "promptId": "bed57f34-927e-4cb2-bd8a-b1a329fa1fbe",
  "agentId": "a8deb1249dd0a8798",
  "type": "user",
  "uuid": "b68181e1-7e20-4030-8808-eadf84cbdb83",
  "sourceToolAssistantUUID": "c25d43d1-f6a8-4db1-80dd-2f41642ba105",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T21:21:47.148Z_

<details open><summary>🔧 Tool call — Read · `toolu_0192y1ZbArLRXE53bTNWaJZD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b68181e1-7e20-4030-8808-eadf84cbdb83",
  "isSidechain": true,
  "agentId": "a8deb1249dd0a8798",
  "requestId": "req_011CbJJrDu3QDf9yb7QjkxJG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6be0f198-61ed-467c-96fa-5ba7f3428362",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015yc3KopAaTUV11o47MM9kc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19301,
      "cache_read_input_tokens": 0,
      "output_tokens": 536,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19301
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 536,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 19301,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19301,
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

_source line 16 · 2026-05-22T21:21:47.152Z_

<details><summary>↩ Tool result · `toolu_0192y1ZbArLRXE53bTNWaJZD`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We measure a lower bound on the generational depth discrimination boundary $\Kempirical$ for prompt-chain recursive synthetic text.
5	For general web text, $\Kempirical \leq 2$ regardless of model family or scale (six architecture families, 1B--8B, $\theta{=}0.60$); across all ten configurations, $\Kempirical \leq 3$, with structured academic text (arXiv) reaching $\Kempirical{=}3$ across two independent architectures.
6	This one-wash laundering effect concentrates all exploitable signal at the 0v1 boundary, and the consistency check confirms that binary curation most effectively minimizes MMLU degradation ($-$0.77\,pp vs.\ $-$1.53\,pp for no-filter).
7	For structured domains where $\Kempirical{=}3$, graduated strategies can exploit one additional depth level, so corpus curators should calibrate filtering to the source domain.
8	The 15 statistical features enable deployment across generators without retraining (80--92\% accuracy retention, $\rho > 0.90$), supporting model-agnostic depth estimation for corpora where the generating model is unknown.
9	Under Bonferroni correction for 10 simultaneous comparisons, four of six $\Kempirical{=}2$ configurations retain significance at the 99.5\% level; the remaining two marginal cases preserve point estimates above $\theta$.
10	$\Kempirical$ converts a continuous AUC decay surface into a discrete operating boundary grounded in the Data Processing Inequality, providing a principled basis for curation decisions that replaces heuristic assumptions about synthetic text recyclability.
11	Several directions remain open: tracking $\Kempirical$ as model scale surpasses 13B, where our scale analysis suggests the boundary may shift toward $\Kempirical{=}1$; bridging the prompt-chain and retrain-chain boundaries, given the substantially higher $\Kempirical{\geq}4$ observed under parameter retraining; and extending depth estimation to additional structured domains and multilingual text.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6be0f198-61ed-467c-96fa-5ba7f3428362",
  "isSidechain": true,
  "promptId": "bed57f34-927e-4cb2-bd8a-b1a329fa1fbe",
  "agentId": "a8deb1249dd0a8798",
  "type": "user",
  "uuid": "da914727-ce8a-42b1-8272-f0c2099ba18a",
  "sourceToolAssistantUUID": "6be0f198-61ed-467c-96fa-5ba7f3428362",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-22T21:23:58.134Z_

# introduction.tex

\section{Introduction}
\label{sec:introduction}

Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
Estimates suggest that a substantial fraction of online text is machine-generated~\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.
When models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
This degradation arises in both \emph{retrain-chains} (iteratively training on model outputs) and \emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\ref{sec:extended_limitations}).
Yet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.

This gap cuts across three communities: binary detectors~\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\ref{sec:binary_confidence}); membership inference~\cite{zawalski2026codec} addresses a different question; the model collapse literature~\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool; and data selection methods~\cite{xie2023dsir, tirumala2023d4, drayson2025} ignore recursive depth.
No existing method estimates how many rounds of recursive generation a text has undergone.

The Data Processing Inequality guarantees that information degrades monotonically across generations, motivating a finite discrimination boundary $\Kstar$.
We empirically measure a lower bound $\Kempirical$ on the discrimination boundary (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistical features and an Ordinal Binary Decomposition (OBD) LightGBM classifier.
We operationalize $\Kempirical$ as the deepest $k \geq 1$ where the pairwise $\auc_{k-1,k}$ exceeds $\theta = 0.60$ (Section~\ref{sec:formulation}).

Our contributions:
\begin{enumerate}[label=(\alph*),nosep]
  \item \textbf{$\Kempirical$ as a measurement tool} across 10 model configurations (6 families, 1B--8B) and 4 decoding strategies ($p \leq 0.002$; Section~\ref{sec:kstar_boundary}):
  For web text, $\Kempirical \leq 2$ regardless of family or scale; $\Kempirical \leq 3$ universally.
  $\Kempirical$ establishes binary sufficiency for web text by measurement (not assumption), reveals domain-dependent variation (arXiv $\Kempirical{=}3$), and quantifies boundary sensitivity to threshold, scorer, and model scale.
  Both supervised OBD and zero-shot LLMs fail beyond $\Kempirical$ (McNemar $p > 0.05$; Section~\ref{sec:why_kstar}).
  \item \textbf{Domain dependence of $\Kempirical$}: general web text (C4, Wikipedia) yields $\Kempirical{=}2$, while structured academic text (arXiv) yields $\Kempirical{=}3$, consistent across model families (Section~\ref{sec:cross_domain}).
  \item \textbf{Model-free cross-model transfer}: 15 statistical features enable 80--100\% accuracy retention with scorer-invariant feature rankings ($\rho > 0.90$), supporting model-agnostic depth estimation without retraining; $\Kempirical$ agreement holds across scorers for strong-signal configurations (Section~\ref{sec:transfer}).
\end{enumerate}

\noindent As a consistency check, $\Kempirical{=}2$ correctly predicts the strategy ordering for web-text filtering: binary curation minimizes degradation most effectively (MMLU $0.5941$ vs.\ base $0.6018$; Section~\ref{sec:filtering}).

---

# related_work.tex

\section{Related Work}
\label{sec:related_work}

\paragraph{Model collapse and recursive degradation.}
Iterative training on model outputs causes tail-distribution degradation~\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong, fu2025theoretical}, diversity contraction~\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, wang2025unveiling}.
Our prompt-chain operates in the replace regime~\cite{kazdan2025collapse}, making $\Kempirical = 2$ a conservative lower bound.
This literature characterizes macro dynamics but provides no per-text depth estimation, the gap we address.

\paragraph{Beyond binary detection.}
Binary detectors~\cite{mitchell2023detectgpt, bao2024fast, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate.
Recent work extends beyond binary labels to collaboration degree~\cite{cheng2025beyond}, contamination hierarchies~\cite{mehta2025beyond}, and multigenerator benchmarks~\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\cite{hao2025rewrite}; CoDeC~\cite{zawalski2026codec} addresses contamination via membership inference.
None estimates recursive generation depth.

\paragraph{Data selection and curation.}
DSIR~\cite{xie2023dsir}, D4~\cite{tirumala2023d4}, and DoReMi~\cite{xie2023doremi} are depth-agnostic; Drayson et al.~\cite{drayson2025} combined binary detection with importance resampling, a special case when $\Kstar = 1$.

\paragraph{Ordinal classification and probing.}
Our OBD classifier follows Frank \& Hall's~\cite{frank2001ordinal} binary decomposition; our neural probe extends probing~\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.

---

# method.tex

\section{Method}
\label{sec:method}

\begin{figure*}[t]
\centering
\includegraphics[width=\textwidth]{figures/pipeline.pdf}
\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\delta$ to produce a depth chain. Corpus-level statistical features are fed to the OBD-LightGBM classifier for depth prediction.}
\label{fig:pipeline}
\end{figure*}

\subsection{Problem Formulation}
\label{sec:formulation}

A generation operator $G_\delta$ (LLM + decoding strategy $\delta$) produces successive generations $X \to Y_1 \to \cdots \to Y_K$, where $Y_k = G_\delta(Y_{k-1})$ and $Y_0 \triangleq X$ (Figure~\ref{fig:pipeline}).
This sequence forms a Markov chain.
By the Data Processing Inequality, $I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0$: mutual information with the seed text degrades monotonically.
Together with Markov chain convergence, this provides heuristic motivation for expecting $\auc_{k-1,k}$ to decrease with $k$, though AUC and mutual information are not formally equivalent; the actual saturation depth must therefore be measured empirically.

We define the operational lower bound:
\begin{equation}
  \Kempirical = \max\!\bigl\{k \!\geq\! 1 : \auc_{j-1,j} > \theta,\;\forall\, j \!\leq\! k\bigr\},
  \label{eq:kstar}
\end{equation}
which requires all pairs up to depth $k$ to exceed the threshold (the $\forall j$ constraint is naturally satisfied because $\auc_{k-1,k}$ decreases monotonically above $\theta$ across all tested configurations; Table~\ref{tab:kstar_ci}).
The theoretical upper bound $\Ktheory$ (the true maximum discriminable depth given optimal features) is not directly estimated in this work.
Since any specific classifier on a feature subset achieves AUC at most equal to the Bayes-optimal classifier on all features, $\Kempirical \leq \Ktheory$ follows directly.
The DPI separately motivates the empirical observation that $\auc_{k-1,k}$ decreases with $k$, though AUC is not a monotone function of MI (as noted above).
Here $\auc_{k-1,k}$ is the point-estimate pairwise AUC and $\theta = 0.60$ is a reference operating point motivated by Cohen's small-effect-size convention ($h \approx 0.20$\footnote{$h = 2\arcsin\!\sqrt{0.60} - 2\arcsin\!\sqrt{0.50} \approx 0.2014$, a ``small'' effect size by Cohen's (1988) convention.}; justified below).
Bootstrap 95\% CIs (1{,}000 resamples) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\theta$ and non-boundary-pair CI upper bounds fall below $\theta$ (Section~\ref{sec:kstar_boundary}).

\paragraph{Threshold justification.}
$\theta{=}0.60$ is a reference operating point supported by three independent lines of evidence.
First, Cohen's $h \approx 0.20$, a conventional small-effect-size boundary.
Second, a 10{,}000-iteration permutation test yields a 95th-percentile null of ${<}\,0.55$ ($p < 0.002$ for all boundary comparisons).
Third, the conclusion $\Kempirical{=}2$ is insensitive to the exact threshold: 1v2 AUC values cluster at $0.61$--$0.70$ while 2v3 values cluster at $0.55$--$0.59$, a ${\sim}$5--11\,pp discontinuity; only at extremes does $\Kempirical$ shift ($\theta{=}0.55$: $\Kempirical{=}3$ for two Qwen configurations; $\theta{=}0.70$: $\Kempirical{=}1$ across all).
Figure~\ref{fig:kstar_theta} provides the full sensitivity surface across $\theta \in [0.55, 0.70]$, enabling practitioners to select $\theta$ according to their false-positive tolerance.
The downstream filtering evaluation (Section~\ref{sec:filtering}) uses the OBD classifier without re-optimizing $\theta$, avoiding circularity.

\subsection{Features and Classifier}
\label{sec:features}

Each document is characterized by a 15-dimensional feature vector spanning four groups: \emph{surprisal moments} (mean, std, skewness, kurtosis; 4~dims), \emph{surprisal derivatives} (mean and std of first- and second-order differences, plus first-order skewness; 5~dims), \emph{vocabulary diversity} (type-token ratio, hapax legomena ratio, self-BLEU; 3~dims), and \emph{frequency tail statistics} (frequency kurtosis, entropy, rare token fraction; 3~dims).
All features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\ref{tab:s5_features}, Appendix).
Self-BLEU is computed within each CV fold using only same-fold, same-depth reference samples to prevent leakage; it ranks \#1 in 1/8 conditions (greedy decoding) but is absent from the top-3 in all 7 others.
Removing self-BLEU reduces mean $\auc_{1v2}$ by $< 1$\,pp across all models (14D $\Kempirical = 2$ for all 4 configurations); in deployment where reference corpora are unavailable, self-BLEU can be replaced with corpus-level self-similarity or omitted entirely, leaving 14 features (surprisal statistics, TTR, hapax ratio, frequency tail) that require no external reference and retain full $\Kempirical$.
Hand-crafted features enable cross-generator transfer without retraining and permit attribution of discriminative power to specific text properties.

We use \emph{Ordinal Binary Decomposition} (OBD), decomposing the $(K{+}1)$-class problem into $K$ cumulative binary sub-classifiers, each estimating $P(\text{depth} > k \mid \mathbf{x})$ via LightGBM (hyperparameters in Table~\ref{tab:s6_lgbm_params}).
OBD achieves lower MAE than multiclass LightGBM (e.g., 0.984 vs.\ 1.016 on Qwen-rewrite) while maintaining superior pairwise $\auc$ (mean 0.6095 vs.\ 0.4883 for ordinal logistic regression).

\subsection{Experimental Setup}
\label{sec:experimental_setup}

We evaluate six configurations spanning three model families (Table~\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Qwen2.5-1.5B (base, continuation), Qwen2.5-7B (continuation), Pythia-1.4B and OLMo-1B (continuation).
Each uses 5{,}000 C4 seeds truncated to 256 tokens, recursively generated for $K{=}5$ iterations (30{,}000 documents per configuration).
Default decoding: nucleus $p{=}0.95$, $T{=}1.0$; decoding ablation covers greedy, $T{=}0.7$, and $T{=}1.2$.
Continuation mode truncates seeds to 128 tokens and extends to 256; rewrite mode paraphrases the full text.
Evaluation: 5-fold GroupKFold cross-validation grouped by seed document; pairwise $\auc$ as primary metric.

\begin{table}[t]
\centering
\small
\caption{Experimental configurations for depth-chain generation. \textbf{Config}: shorthand identifier; \textbf{Model}: architecture and parameter count; \textbf{Mode}: generation strategy (continuation or rewrite); $N$: number of seed documents per depth level.}
\label{tab:setup}
\begin{tabular}{llcc}
\toprule
\textbf{Config} & \textbf{Model} & \textbf{Mode} & $N$ \\
\midrule
Qwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite & 5{,}000 \\
Qwen-cont & Qwen2.5-1.5B-Instruct & Continuation & 5{,}000 \\
Qwen-base & Qwen2.5-1.5B          & Continuation & 5{,}000 \\
Pythia    & Pythia-1.4B            & Continuation & 5{,}000 \\
OLMo      & OLMo-1B               & Continuation & 5{,}000 \\
Qwen-7B   & Qwen2.5-7B            & Continuation & 5{,}000 \\
\bottomrule
\end{tabular}
\end{table}

---

# experiments_c1.tex

\section{Experiments}
\label{sec:experiments}

We evaluate generational depth estimation on ten model configurations spanning six architecture families:
Pythia-1.4B, Pythia-6.9B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, LLaMA-3.1-8B, Mistral-7B, and Gemma-2-2B, all in continuation mode except where noted.
All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).

%% ====================================================================
\subsection{$\Kempirical \leq 2$ Across Model Configurations (C4)}
\label{sec:kstar_boundary}

\begin{table*}[t]
\centering
\small
\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.
Extended results (all models) in Table~\ref{tab:kstar_ci_extended}.}
\label{tab:kstar_ci}
\begin{tabular}{lcccccccccc}
\toprule
 & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
 & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
\midrule
0v1 & .9956 & & .9932 & & .9860 & & .9971 & & .9638 & [.961,\,.967] \\
1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .5080 & [.496,\,.519] & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .4973 & [.486,\,.509] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] \\
3v4 & .5435 & & .5152 & & .5024\rlap{$^\S$} & & .5409 & & .5276 & \\
4v5 & .5340 & & .5136 & & .4942 & & .5141 & & .5085 & \\
\bottomrule
\multicolumn{11}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all 1v2 comparisons shown.} \\
\multicolumn{11}{l}{\footnotesize $^\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.} \\
\multicolumn{11}{l}{\footnotesize $^\S$OLMo 2v3 (0.497) $<$ 3v4 (0.502): non-monotonic reversal within noise ($\Delta = 0.005$).} \\
\multicolumn{11}{l}{\footnotesize Full results for all 10 configurations (including Qwen-7B, Qwen-base, Gemma-2-2B, and Pythia-6.9B) are provided in Table~\ref{tab:kstar_ci_extended}.}
\end{tabular}
\end{table*}

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
\caption{Pairwise $\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed); shaded bands show bootstrap 95\% confidence intervals. The horizontal dashed line marks $\theta = 0.60$.}
\label{fig:auc_decay}
\end{figure}

Table~\ref{tab:kstar_ci} and Figure~\ref{fig:auc_decay} show $\Kempirical \leq 2$ across all 10 model configurations: 6/10 configurations yield $\Kempirical{=}2$ (Qwen with 4 configs, LLaMA-8B, and Pythia-1.4B, spanning three of six families) (1v2 $\auc$ range: 0.6112--0.6955; all CI lower bounds $> \theta$; permutation $p < 0.001$), while OLMo-1B, Mistral-7B, Pythia-6.9B, and Gemma-2-2B yield $\Kempirical{=}1$ (1v2 $\auc$: 0.508, 0.594, 0.596, and 0.598, all below $\theta$; Section~\ref{sec:boundary_cases}).
Under Bonferroni correction for 10 simultaneous comparisons (99.5\% CIs), four of six boundary configurations retain CI lower bounds above $\theta$; the two most marginal cases, Qwen-continuation (nominal CI lower bound 0.602) and LLaMA-8B (0.603), fall below the widened interval.
Both retain point estimates above $\theta$ and uncorrected CI lower bounds above $\theta$; the near-misses reflect narrow effect sizes rather than classification failure.
By architecture family: Qwen (4/4) and LLaMA (1/1) yield $\Kempirical{\geq}2$ at nominal significance; OLMo (1/1), Mistral (1/1), and Gemma (1/1) yield $\Kempirical{=}1$; Pythia exhibits a scale-dependent split (1.4B: $\Kempirical{=}2$, 6.9B: $\Kempirical{=}1$).
LLaMA-3.1-8B confirms $\Kempirical{=}2$ (0v1 $\auc = 0.9225$, 1v2 $\auc = 0.6123\;[0.603,\,0.622]$; CI lower bound above $\theta$; Table~\ref{tab:kstar_ci_extended}).
All four decoding strategies likewise yield $\Kempirical{=}2$ (Table~\ref{tab:s2_decoding}).
The 1v2 spread due to generation mode ($\Delta = 8.4$\,pp within Qwen) exceeds the spread across $\Kempirical{=}2$ continuation models ($\Delta = 4.3$\,pp).

\paragraph{Scale and instruction-tuning invariance.}
$\Kempirical{=}2$ persists from 1.5B through 8B: Qwen-7B (1v2 $\auc = 0.6168$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\auc = 0.6123$) both exceed $\theta$, despite progressively reduced 0v1 signal (0.9638 and 0.9225 vs.\ $> 0.99$ at $\leq$1.5B).
A base-vs.-instruct ablation at 1.5B likewise yields $\Kempirical = 2$ (1v2 $\auc = 0.626$), confirming the boundary is not an instruction-tuning artifact.

\begin{figure*}[t]
\centering
\includegraphics[width=0.75\textwidth]{figures/fig_kstar_theta.pdf}
\caption{$\Kempirical(\theta)$ sensitivity curve for six configurations. $\Kempirical$: maximum discriminable depth; $\theta$: AUC decision threshold. Five of six configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (dashed line); OLMo yields $\Kempirical{=}1$. At $\theta{=}0.70$, all drop to $\Kempirical{=}1$.}
\label{fig:kstar_theta}
\end{figure*}

The raw AUC gap between adjacent generations provides a threshold-free continuous measure of discriminability; Figure~\ref{fig:kstar_theta} displays the full sensitivity surface across $\theta \in [0.55, 0.70]$, allowing practitioners to read off $\Kempirical$ at any desired effect-size threshold.
Five of six configurations yield $\Kempirical = 2$ within $\theta \in [0.51, 0.61]$ (OLMo: $\Kempirical = 1$ throughout); at $\theta{=}0.55$, two Qwen configurations reach $\Kempirical = 3$; at $\theta{=}0.70$, all drop to $\Kempirical = 1$.
All four decoding strategies likewise yield $\Kempirical = 2$ at $\theta{=}0.60$ (1v2 $\auc \in [0.687, 0.704]$; Table~\ref{tab:s2_decoding}).

%% ====================================================================
\subsection{Cross-Model Transfer}
\label{sec:transfer}

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{figures/fig3_transfer_heatmap.pdf}
\caption{Cross-model transfer heatmap. Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, retention rate. Pythia$\leftrightarrow$OLMo: 90--92\%; Qwen-rewrite$\to$continuation: 61--63\%.}
\label{fig:transfer_heatmap}
\end{figure}

Continuation-mode classifiers transfer well across generators (Figure~\ref{fig:transfer_heatmap}; full matrix in Table~\ref{tab:s1_transfer}): Pythia$\leftrightarrow$OLMo retains 90--92\%, Qwen-cont$\leftrightarrow$Pythia 84--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\% (0v1 cross-model $\auc > 0.96$ for all pairs).
Qwen-rewrite classifiers transfer poorly (61--63\%), confirming reliance on mode-specific artifacts rather than generalizable depth features.

\paragraph{Cross-scorer validation.}
Replacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\rho > 0.90$) but attenuates absolute discriminability at the boundary (Table~\ref{tab:crossscorer}).
Feature ranking independence is a strong result: the same features dominate under all scorers.
$\Kempirical$ agreement, however, is signal-strength dependent: Qwen-rewrite (strong signal, 1v2 $\auc = 0.696$) retains $\Kempirical{=}2$ under all scorers, but Qwen-continuation (marginal, 1v2 $\auc = 0.611$, only 0.011 above $\theta$) drops to $\Kempirical{=}1$ (Pythia: $0.5923$; OLMo: $0.5858$).
A three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair; Table~\ref{tab:anova_crossscorer}) confirms a statistically significant but modest Scorer main effect ($\eta^2_p{=}.166$, $p < .001$) and a significant Generator$\times$Scorer interaction ($\eta^2_p{=}.146$), indicating that absolute AUC values are scorer-dependent even when $\Kempirical$ classifications largely agree.

%% ====================================================================
\subsection{Feature Ordering and Generation Mode}
\label{sec:feature_degradation}
\label{sec:generation_mode}

Among continuation-mode models, single-feature $\auc$ rankings are highly correlated ($\rho \geq 0.85$; Table~\ref{tab:top_features}).
The top-3 features (\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}) are shared across all three families, revealing that autoregressive generation progressively damps surprisal variability.
Qwen-rewrite diverges (\texttt{freq\_entropy} dominates), consistent with its poor cross-model transfer (61--63\%).
Within Qwen, rewrite yields 1v2 $\auc = 0.6955$ vs.\ continuation's $0.6112$ ($\Delta = +8.4$\,pp); continuation mode is therefore recommended as the canonical condition.

%% ====================================================================
\subsection{Neural Probe}
\label{sec:neural_probe}

Replacing the 15D features with frozen encoder hidden states (MLP probe; Table~\ref{tab:neural_probe_crossmodel}), Qwen achieves $\Kempirical^{\text{neural}} = 3$ (2v3 $\auc = 0.6159$), while Pythia remains at $\Kempirical^{\text{neural}} = 2$ ($\auc_{2v3} = 0.5963$); OLMo yields $\Kempirical^{\text{neural}} = 1$ (1v2 $\auc = 0.5054$, consistent with its 15D boundary).
We hypothesize that the Qwen-only elevation reflects self-familiarity artifacts, consistent with the poor transfer observed in Section~\ref{sec:transfer}; the 15D features yield $\Kempirical = 2$ for most families (OLMo: $\Kempirical = 1$).

\noindent\begin{minipage}{\columnwidth}
\centering
\footnotesize
\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\ $d{+}1$ text. $\Kempirical^{\text{neural}}$: maximum depth where AUC exceeds $\theta = 0.60$.}
\label{tab:neural_probe_crossmodel}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{lccc}
\toprule
\textbf{Model} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & $\Kempirical^{\text{neural}}$ \\
\midrule
Qwen-1.5B  & 0.6159 & $[0.610,\,0.622]$ & 3 \\
Pythia-1.4B & 0.5963 & $[0.589,\,0.603]$ & 2 \\
OLMo-1B    & 0.5056 & $[0.497,\,0.516]$ & 1\rlap{$^\dagger$} \\
\bottomrule
\multicolumn{4}{l}{\footnotesize $^\dagger$OLMo 1v2 $\auc = 0.5054$ (below $\theta$); $\Kempirical^{\text{neural}} = 1$.}
\end{tabular}}
\end{minipage}

%% ====================================================================
\subsection{Cross-Domain Variation}
\label{sec:cross_domain}

The preceding experiments use C4 (general web text).
To test domain dependence, we evaluate on Wikipedia ($n{=}5{,}000$) and arXiv abstracts ($n{=}2{,}200$) using two model families.
Wikipedia yields $\Kempirical{=}2$ (1v2 $\auc = 0.623$, 2v3 $\auc = 0.571$), matching the C4 baseline.
Both Qwen-1.5B and Pythia-1.4B yield $\Kempirical{=}3$ for arXiv (Table~\ref{tab:domain_kstar}): 2v3 $\auc = 0.644\;[0.628,\,0.658]$ and $0.655\;[0.640,\,0.669]$ respectively (bootstrap CI lower bounds above $\theta$; permutation $p < 0.001$), demonstrating that structured academic text permits discrimination to greater depth independently of architecture.
The elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4), as formulaic structure amplifies deviation from domain norms.

\begin{table}[t]
\centering
\footnotesize
\caption{Cross-domain $\Kempirical$ comparison. Rows: generator model and text domain (C4, Wikipedia, arXiv). $\Kempirical{=}3$ for arXiv indicates structured text preserves discriminability to greater depth.}
\label{tab:domain_kstar}
\begin{tabular}{llccc}
\toprule
\textbf{Domain} & \textbf{Model} & \textbf{1v2 $\auc$} & \textbf{2v3 $\auc$} & $\Kempirical$ \\
\midrule
arXiv & Qwen-1.5B  & 0.858 & 0.6436 & 3 \\
arXiv & Pythia-1.4B & 0.805 & 0.6545 & 3 \\
C4    & Qwen-1.5B  & 0.63  & 0.56   & 2 \\
Wikipedia & Qwen-1.5B & 0.62 & 0.55 & 2 \\
\bottomrule
\end{tabular}
\end{table}

\paragraph{Robustness.}
\label{sec:robustness}
$\Kempirical{=}2$ holds across segment lengths of 128, 256, and 512 tokens (Table~\ref{tab:s11_length_ablation}); at 512 tokens the 1v2 CI lower bound falls marginally below $\theta$ but 2v3 remains well below $\theta$ at all lengths ($\leq 0.572$).
Seed robustness testing (seed $= 123$ vs.\ primary $= 42$; Table~\ref{tab:seed_robustness}) confirms $\Kempirical$ stability in 2/3 configurations; the one marginal shift (Qwen-Wikipedia $\Kempirical{=}2 \to 3$, 2v3 $\auc = 0.607$) has one of five folds below $\theta$.
The ${\pm}9$\,pp absolute AUC variation across seeds strengthens the case for threshold-based $\Kempirical$ over raw AUC comparisons.

%% ====================================================================
\subsection{Binary Detector Confidence}
\label{sec:binary_confidence}

Binary detectors (DivEye~\cite{basani2026diveye}, Binoculars~\cite{hans2024binoculars}) show moderate rank correlations with depth ($|\rho| = 0.06$--$0.46$; Table~\ref{tab:s9_binary_spearman}) but fail as depth proxies: 6-class accuracy is at or below chance ($\leq 0.199$ vs.\ 0.167 baseline), pairwise $\auc$ yields $\Kempirical^{\text{binary}} \leq 1$, and multiple conditions exhibit non-monotonic AUC at deeper pairs.
The observed correlation is an artifact of 0v1 separation rather than fine-grained depth signal.

---

# experiments_c3.tex

\section{Consistency Check: $\Kstar$-Guided Filtering}
\label{sec:filtering}

$\Kempirical = 2$ makes a falsifiable prediction: binary curation should suffice, and graduated performance should converge toward binary as the decay steepness increases.
We test this as a consistency check on the boundary measurement, not as an independent contribution.
We compare six strategies on 30{,}000 documents (depths 0--5): (i)~\textbf{no-filter}, (ii)~\textbf{binary-ours} ($w = 1 - P(\text{synthetic})$ from 15D LightGBM), (iii)~\textbf{binary-Drayson}~\citep{drayson2025}, (iv)~\textbf{graduated} ($w = \exp(-\alpha \cdot \hat{d})$, $\alpha \in \{0.1,\ldots,0.9\}$), (v)~\textbf{surprisal} (retain above median), and (vi)~\textbf{DSIR}~\citep{xie2023dsir}.
We fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\alpha_{\text{LoRA}}{=}16$) for 3 epochs on MMLU and HellaSwag across 5 seeds (51 total runs; this 100\% synthetic setting is an upper bound~\cite{shumailov2024collapse, dohmatob2024model}).

\begin{table}[t]
\centering
\small
\caption{Downstream task performance (MMLU, HellaSwag) under six data-filtering strategies. Binary-ours uses the 15D LightGBM depth classifier; Graduated applies exponentially decaying weights $w = \exp(-\alpha \hat{d})$. Mean $\pm$ std over 5 seeds. Full $\alpha$ sweep in Appendix~\ref{sec:extended_limitations}.}
\label{tab:tab_filtering_main}
\resizebox{\columnwidth}{!}{\input{tables/tab_filtering_main}}
\end{table}

Binary-ours minimizes MMLU degradation most effectively (Table~\ref{tab:tab_filtering_main}), reducing the gap from $-$1.53\,pp (no-filter) to $-$0.77\,pp (${\sim}$50\% reduction; $p_{\text{corr}} < 0.05$ vs.\ all alternatives).
These effects are measured in a 100\% synthetic upper-bound setting; real-world contamination ratios are typically lower, and effect sizes would scale accordingly.
The strategy ordering is interpretable through $\Kempirical$: binary filtering exploits the one reliable boundary (0v1), while graduated strategies assign weights to depths 2--5 based on near-random classifier outputs, injecting noise.
Graduated filtering converges monotonically toward binary: at $\alpha{=}0.9$, it matches binary-ours on HellaSwag exactly ($\Delta = 0$, $p_{\text{corr}} = 1.00$) but remains significantly worse on MMLU ($p_{\text{corr}} = 0.011$).
DSIR is indistinguishable from no-filter, confirming that depth-aware features are necessary for curation in recursively contaminated corpora (Figure~\ref{fig:filtering_strategies} in Appendix).
At realistic contamination ratios ($\leq$50\%), all filtering strategies converge ($p > 0.12$), consistent with the one-wash laundering finding that depth-aware curation offers marginal benefit when $\Kempirical{=}2$ (Appendix~\ref{sec:dose_response}).
For $\Kempirical{=}1$ configurations, depth-aware curation reduces to standard binary filtering, consistent with $\Kempirical{=}1$ implying no exploitable depth signal beyond the 0v1 boundary.

---

# discussion.tex

\section{Discussion}
\label{sec:discussion}
\label{sec:why_kstar}
\label{sec:one_wash}
\label{sec:negative_graduated}
\label{sec:repr_dependence}
\label{sec:boundary_cases}
\label{sec:length_confound}

\paragraph{One-wash laundering (web text).}
For general web text, $\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\auc \geq 0.92$), 1v2 drops by ${\sim}$30\,pp, and 2v3 falls below $\theta$.
A single generation pass renders text indistinguishable from multiply recycled content, limiting depth-aware curation to a binary boundary.
Converging evidence supports a data-intrinsic interpretation: OBD achieves 96\% depth-0 recall but only 14--22\% for depths 2--4; frontier LLMs show 8--38\% (McNemar $p > 0.05$ vs.\ OBD; Table~\ref{tab:s3_llm_zeroshot}).

\paragraph{Representation dependence.}
$\Kempirical$ is representation-dependent: frozen Qwen embeddings yield $\Kempirical^{\text{neural}} = 3$, while Pythia yields $\Kempirical^{\text{neural}} = 2$ and OLMo yields $\Kempirical^{\text{neural}} = 1$, consistent with its 15D boundary (Table~\ref{tab:neural_probe_crossmodel}).
The 15D features trade one depth level of sensitivity for cross-model consistency (6/10 configurations $\Kempirical{=}2$), making them the preferred operational choice.
Feature rankings are scorer-independent ($\rho > 0.90$); $\Kempirical$ agreement is scorer-independent for strong-signal configurations (e.g., Qwen-rewrite retains $\Kempirical{=}2$ under all scorers) but scorer-sensitive at marginal boundaries (Qwen-continuation drops to $\Kempirical{=}1$; length confound ruled out in Appendix~\ref{sec:extended_limitations}).
ANOVA confirms this layered pattern: Scorer explains modest variance ($\eta^2_p{=}.166$) with a significant Generator$\times$Scorer interaction ($\eta^2_p{=}.146$; Table~\ref{tab:anova_crossscorer}).

\paragraph{Domain dependence of $\Kempirical$.}
Web text (C4, Wikipedia) consistently yields $\Kempirical{=}2$, while structured academic text (arXiv) yields $\Kempirical{=}3$ across two independent model families (Qwen-1.5B and Pythia-1.4B; Section~\ref{sec:cross_domain}).
The elevated arXiv signal reflects formulaic structure: citation patterns, mathematical notation, and section conventions create larger per-generation distributional shifts (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4), making contamination trackable to greater depth.
Wikipedia matches C4 at $\Kempirical{=}2$ (1v2 $\auc = 0.623$, 2v3 $\auc = 0.571$), consistent with its general-purpose prose lacking domain-specific structural markers.
This domain dependence implies that corpus curators should calibrate depth-aware filtering to source characteristics rather than assuming a universal boundary.

\paragraph{Cross-model transfer.}
Continuation-mode classifiers transfer well across generators (80--92\% retention; Figure~\ref{fig:transfer_heatmap}), enabling portable depth estimation on corpora from unknown models without retraining.
The poor transfer from rewrite-mode classifiers (61--63\%) isolates generation mode, rather than architecture family, as the primary axis of distributional variation.

\paragraph{Prompt-chain scope and retrain-chain gap.}
Retrain-chain experiments (Pythia-1.4B LoRA) yield $\Kempirical{\geq}4$ (1v2 $\auc = 0.9484$, 3v4 $= 0.7982$), far exceeding the prompt-chain boundary of $\Kempirical{=}2$, because each retrain generation also modifies model parameters, introducing cumulative adaptation artifacts absent from text-only recycling.
Prompt-chain $\Kempirical$ isolates text-intrinsic degradation, the operationally relevant quantity for data curation pipelines; our conclusions do not directly transfer to retrain-chain (model collapse) settings.

\paragraph{Boundary cases and scale effect.}
$\Kempirical{=}1$ configurations cluster at 1v2 $\auc$ 0.508--0.598, well separated from the $\Kempirical{=}2$ range (0.611--0.696); $\Kempirical{=}1$ is not a classifier failure but a text property, as these models produce first-generation output so human-like that statistical features cannot distinguish depth~1 from depth~2.
That $\Kempirical \in \{1, 2\}$ for all web text configurations is the core empirical result; larger models reduce 0v1 JSD (0.077 at 8B vs.\ 0.15--0.27 at $\leq$1.5B), suggesting 13B+ may increasingly yield $\Kempirical{=}1$.
The $\Kempirical{=}1$ vs.\ $\Kempirical{=}2$ distinction has a direct curation consequence: $\Kempirical{=}1$ generators erase depth signal in one pass, leaving only the binary 0v1 boundary available for filtering.

\paragraph{Decoding strategy as confound.}
Greedy decoding inflates depth separability: Pythia-6.9B yields $\Kempirical{=}2$ under greedy but $\Kempirical{=}1$ under nucleus sampling ($p{=}0.95$), with the borderline 1v2 score (2 of 5 folds above $\theta$) illustrating that the boundary is continuous rather than a cliff (Table~\ref{tab:s10_pythia_decoding}).
Practitioners should calibrate $\theta$ to their application-specific tolerance (Figure~\ref{fig:kstar_theta}).

\paragraph{What $\Kempirical$ reveals.}
As a measurement tool, $\Kempirical$ establishes why binary detection suffices for web text (depth${>}1$ is invisible to statistical features), identifies domains where finer strategies are viable (arXiv $\Kempirical{=}3$), and quantifies how scale, scorer, and threshold jointly shape the boundary.
The OBD framework provides a reproducible, low-cost depth estimation protocol requiring only corpus-level statistical features, unlike detection methods that need API access or model weights.
Even when the practical outcome remains binary filtering, $\Kempirical$ grounds this choice in measurement rather than heuristic assumption.
$\Kempirical$ also serves as a monitoring metric for tracking how the discrimination boundary shifts as model scale increases; future work may explore scorer-ensemble strategies to improve cross-scorer robustness at marginal boundaries.

---

# conclusion.tex

\section{Conclusion}
\label{sec:conclusion}

We measure a lower bound on the generational depth discrimination boundary $\Kempirical$ for prompt-chain recursive synthetic text.
For general web text, $\Kempirical \leq 2$ regardless of model family or scale (six architecture families, 1B--8B, $\theta{=}0.60$); across all ten configurations, $\Kempirical \leq 3$, with structured academic text (arXiv) reaching $\Kempirical{=}3$ across two independent architectures.
This one-wash laundering effect concentrates all exploitable signal at the 0v1 boundary, and the consistency check confirms that binary curation most effectively minimizes MMLU degradation ($-$0.77\,pp vs.\ $-$1.53\,pp for no-filter).
For structured domains where $\Kempirical{=}3$, graduated strategies can exploit one additional depth level, so corpus curators should calibrate filtering to the source domain.
The 15 statistical features enable deployment across generators without retraining (80--92\% accuracy retention, $\rho > 0.90$), supporting model-agnostic depth estimation for corpora where the generating model is unknown.
Under Bonferroni correction for 10 simultaneous comparisons, four of six $\Kempirical{=}2$ configurations retain significance at the 99.5\% level; the remaining two marginal cases preserve point estimates above $\theta$.
$\Kempirical$ converts a continuous AUC decay surface into a discrete operating boundary grounded in the Data Processing Inequality, providing a principled basis for curation decisions that replaces heuristic assumptions about synthetic text recyclability.
Several directions remain open: tracking $\Kempirical$ as model scale surpasses 13B, where our scale analysis suggests the boundary may shift toward $\Kempirical{=}1$; bridging the prompt-chain and retrain-chain boundaries, given the substantially higher $\Kempirical{\geq}4$ observed under parameter retraining; and extending depth estimation to additional structured domains and multilingual text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da914727-ce8a-42b1-8272-f0c2099ba18a",
  "isSidechain": true,
  "agentId": "a8deb1249dd0a8798",
  "requestId": "req_011CbJJrRhhPSnRfV9FxNX5f",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8b9cfe4a-9cf1-4717-a9c6-c1dc8c03fe05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01A3GkrME9o9kN2AXw5VMLQs",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 14858,
      "cache_read_input_tokens": 19301,
      "output_tokens": 12567,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14858
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 12567,
          "cache_read_input_tokens": 19301,
          "cache_creation_input_tokens": 14858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14858,
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
