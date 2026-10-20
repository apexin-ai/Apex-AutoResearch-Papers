# Research conversation: I need to read the LaTeX source files for a paper review. The paper is at /home/ubuntu/.agent-ml-research-idea_gen_0520_

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ab47b7a11c46d59e1.jsonl`
- **Structured JSON:** [`e3931995d39601b60080.json`](../../sessions/e3/e3931995d39601b60080.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

17 recorded events

### User

_source line 1 · 2026-05-22T10:20:56.138Z_

I need to read the LaTeX source files for a paper review. The paper is at /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/

Read the following files completely and report their full contents:
1. sections/method.tex
2. sections/experiments.tex  
3. sections/discussion.tex
4. sections/limitations.tex
5. sections/appendix.tex
6. sections/abstract.tex
7. sections/introduction.tex

These are in /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/

Report all precise numbers, formulas, statistical tests, confidence intervals, sample sizes, and any claims made. I need the exact text for a thorough peer review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f90137fe-a99e-4ab9-b8fe-8a63993956e8",
  "agentId": "ab47b7a11c46d59e1",
  "type": "user",
  "uuid": "4a338b2c-27b2-4e1b-b3de-83a55ab5fbae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "1e821804-de94-461a-97da-c43c5977bbe1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-22T10:20:57.699Z_

I'll read all the LaTeX source files you specified for your peer review. Let me fetch them all in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a338b2c-27b2-4e1b-b3de-83a55ab5fbae",
  "isSidechain": true,
  "agentId": "ab47b7a11c46d59e1",
  "requestId": "req_011CbHSTaHfiC5eHRvFwNo36",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ebec3daa-2fb1-4971-9a84-2e0ab3c9ebb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "1e821804-de94-461a-97da-c43c5977bbe1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013vCvoD3TjKQrNi3WBg8GYr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18088,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18088,
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

_source line 3 · 2026-05-22T10:20:57.985Z_

<details open><summary>🔧 Tool call — Read · `toolu_015pxzfiUDnLzRgDsnfRKd5R`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebec3daa-2fb1-4971-9a84-2e0ab3c9ebb2",
  "isSidechain": true,
  "agentId": "ab47b7a11c46d59e1",
  "requestId": "req_011CbHSTaHfiC5eHRvFwNo36",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bb9033d2-f633-415d-8a61-7d560756e680",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "1e821804-de94-461a-97da-c43c5977bbe1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013vCvoD3TjKQrNi3WBg8GYr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18088,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18088,
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

_source line 4 · 2026-05-22T10:20:57.995Z_

<details><summary>↩ Tool result · `toolu_015pxzfiUDnLzRgDsnfRKd5R`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh} detects DIF by stratifying examinees into $K$ score bins based on total score (a proxy for $\theta$) and computing a common odds ratio across strata. We use $K = 5$ equiprobable strata (quintile-based binning) following ETS recommended practice for large-scale assessments~\citep{donoghue1993mh,clauser1998dif}. Within each stratum $k$, the responses of the reference group and the focal group form a $2 \times 2$ contingency table:
17	
18	\begin{equation}
19	\label{eq:mh}
20	\alpha_{\mathrm{MH}} = \frac{\displaystyle\sum_{k=1}^{K} A_k D_k \,/\, T_k}{\displaystyle\sum_{k=1}^{K} B_k C_k \,/\, T_k}\,,
21	\end{equation}
22	
23	\noindent where $A_k$ and $B_k$ are the number of correct and incorrect responses in the reference group for stratum $k$, $C_k$ and $D_k$ are the corresponding counts for the focal group, and $T_k$ is the total number of examinees in stratum $k$. Under the null hypothesis of no DIF, $\alpha_{\mathrm{MH}} = 1$. The log odds ratio is converted to the ETS delta scale:
24	
25	\begin{equation}
26	\label{eq:delta}
27	\Delta_{\mathrm{MH}} = -2.35 \ln(\alpha_{\mathrm{MH}})\,.
28	\end{equation}
29	
30	The Educational Testing Service (ETS) classifies DIF severity into three categories based on $|\Delta_{\mathrm{MH}}|$. Category~A (negligible) requires $|\Delta_{\mathrm{MH}}| < 1.0$. Category~C (large) requires both $|\Delta_{\mathrm{MH}}| \geq 1.5$ and statistical significance at $p < 0.05$ from the MH chi-squared test. Category~B (moderate) includes all remaining items: those with $1.0 \leq |\Delta_{\mathrm{MH}}| < 1.5$, or $|\Delta_{\mathrm{MH}}| \geq 1.5$ without statistical significance. The dual threshold in ETS~C (effect size \emph{and} significance) guards against flagging items that show large but unreliable effect sizes. Throughout this paper, we report the percentage of items classified as ETS~C, denoted C\%. For example, if 2024 models consistently outperform 2023 models on a formal-logic item \emph{after controlling for overall ability}, the pooled odds ratio $\alpha_{\mathrm{MH}} = 0.42$ yields $\Delta_{\mathrm{MH}} = -2.35 \ln(0.42) = 2.04$, classified as ETS~C ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.001$).
31	
32	The choice of matching variable (the total score used for stratification) affects both validity and interpretation. We distinguish three matching strategies: (1)~\emph{standard matching} uses the within-benchmark total score on all items of the same benchmark; (2)~\emph{cross-subject matching}, adapting purified subtest matching~\citep{swaminathan1990logistic} to the LLM multi-subject setting, uses the total score on all subjects \emph{other than} the one containing the item under test, preventing the matching variable from absorbing injected contamination signals (\Cref{sec:injection}); and (3)~\emph{external matching} uses the total score on a different benchmark entirely (e.g., MMLU total score as the matching variable when testing DIF on GSM8K items), providing an independent ability proxy uncontaminated by the target benchmark. Cross-subject and external matching both address matching variable contamination but at different granularities: cross-subject operates within a multi-domain benchmark, while external operates across benchmarks. Total score matching is sufficient: IRT $\theta$ correlates at $r = 0.9986$ with total scores (\Cref{sec:structural}).
33	
34	\paragraph{LLM-specific challenges.} Applying MH-DIF to LLMs introduces assumptions absent in educational testing. First, models trained on overlapping corpora violate local independence; permutation simulation (1,000 iterations $\times$ 8 subjects, Q3 $= 4.6$--$34.2\%$) confirms LD-attributable FPR inflation $< 0.001$ pp under cross-subject matching with ETS~C (\Cref{app:method_details}). Second, fine-tuned variants and merges within model families are not independent examinees; graduated de-duplication shows family structure does not inflate C\% (\Cref{sec:structural}). Third, the ability distribution is non-normal (bimodal from base vs.\ instruction-tuned models), motivating quintile-based rather than parametric stratification. Fourth, MMLU's 57 subjects span multiple latent dimensions, while MH assumes unidimensionality; cross-subject matching and within-subject DIF checks address this (\Cref{sec:structural}). MH-DIF is non-parametric and does not assume a specific IRT model. Unlike standard purified MH that conditions on total test score, we match on cross-subject total score to avoid criterion contamination when target-subject items themselves may be compromised---an adaptation specific to multi-domain LLM benchmarks where subjects may be differentially affected.
35	
36	\subsection{Cohort Designs}
37	\label{sec:cohorts}
38	
39	We construct five cohort comparisons: (1)~\emph{Temporal}: 2023 ($N = 1{,}080$) vs.\ 2024 ($N = 807$) models, the primary comparison; (2)~\emph{Ability-quintile}: Q1--Q2 vs.\ Q4--Q5 within the same temporal window, testing whether ability differences alone produce DIF; (3)~\emph{Within-family}: Llama-2 ($N = 161$) vs.\ Llama-3 ($N = 308$), isolating generational changes within a single family; (4)~\emph{Within-subject}: per-subject DIF to test domain concentration; and (5)~\emph{Random split}: two random halves of the 2023 cohort ($N = 540$ each) as a sanity check.
40	
41	\subsection{Semi-Synthetic Injection Framework}
42	\label{sec:injection}
43	
44	To evaluate whether MH-DIF can detect differential contamination when it is present, we construct a semi-synthetic framework with controlled ground truth.
45	
46	\paragraph{Procedure.} From items classified as ETS~A in the uninjected data (negligible DIF), we select 20\% uniformly at random as the ``contaminated'' set. For each contaminated item, we flip incorrect responses to correct in the focal group at exploitation rate $p \in \{0.0, 0.3, 0.5, 0.7, 1.0\}$. We then run MH-DIF on the modified response matrix and measure detection performance. We report $\Delta\mathrm{TPR} = \mathrm{TPR}(\text{injected}) - \mathrm{TPR}(\text{baseline})$ and $\Delta\mathrm{FPR} = \mathrm{FPR}(\text{injected}) - \mathrm{FPR}(\text{baseline})$, where TPR is the true positive rate on injected items and FPR is the false positive rate on uninjected items. Each injection level is repeated across 5 random seeds for uncertainty estimation. Because binary response flipping represents a worst-case uniform exploitation pattern, reported $\Delta\mathrm{TPR}$ values constitute upper-bound estimates of detection sensitivity under more realistic contamination scenarios.
47	
48	\paragraph{Cross-subject matching.} The choice of matching variable is critical for valid semi-synthetic evaluation. When contamination is injected into items within subject $X$, the total score on subject $X$ absorbs part of the injection signal. Using this contaminated total score as the MH matching variable violates the conditional independence assumption and inflates FPR. Cross-subject matching resolves this by computing the matching variable from all subjects \emph{other than} the one being tested.
49	
50	\paragraph{Remark (Zero FPR under single-subject matching).}
51	\label{prop:fpr}
52	Let $M_i^{(-s)} = \sum_{j \notin s} Y_{ij}$ be the matching variable for examinee $i$ on focal subject $s$. Under single-subject injection (contamination confined to subject $s$), the tested item belongs to $s$ and does not contribute to $M_i^{(-s)}$; injecting contamination into $s$ leaves $M_i^{(-s)}$ unchanged. Therefore $\Delta\mathrm{FPR} = 0$ by construction.
53	
54	When contamination spans multiple subjects simultaneously, $M_i^{(-s)}$ may absorb signal from other contaminated subjects, potentially inflating FPR. Empirically, this guarantee extends to multi-domain contamination affecting $\leq$9\% of subjects ($k \leq 5$), with graceful degradation beyond this boundary (\Cref{sec:semisynthetic}).
55	
56	Empirically, $\Delta\mathrm{FPR} = 0.000$ across all five MMLU domains (bootstrap 95\% CI $= [0.000, 0.000]$). $\Delta\mathrm{FPR} = 0$ is a constructive guarantee of the matching strategy, independent of injection realism, whereas $\Delta\mathrm{TPR}$ constitutes an upper-bound estimate. We adopt cross-subject matching as the standard protocol.
57	
58	Diagnostic procedures (Yen's Q3 local independence, domain-specificity analysis, DIF decomposition) and statistical details (multiple testing correction, threshold sensitivity, architecture heterogeneity checks) appear in \Cref{app:method_details}.
59	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb9033d2-f633-415d-8a61-7d560756e680",
  "isSidechain": true,
  "promptId": "f90137fe-a99e-4ab9-b8fe-8a63993956e8",
  "agentId": "ab47b7a11c46d59e1",
  "type": "user",
  "uuid": "b65700c5-edfe-4531-a677-8ff3678bc12c",
  "sourceToolAssistantUUID": "bb9033d2-f633-415d-8a61-7d560756e680",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "1e821804-de94-461a-97da-c43c5977bbe1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T10:20:58.350Z_

<details open><summary>🔧 Tool call — Read · `toolu_014xAkgxCLcnPKyTtgtYv7Ka`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b65700c5-edfe-4531-a677-8ff3678bc12c",
  "isSidechain": true,
  "agentId": "ab47b7a11c46d59e1",
  "requestId": "req_011CbHSTaHfiC5eHRvFwNo36",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "942d6c3b-a506-46d5-ad98-6b54d0f493c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "1e821804-de94-461a-97da-c43c5977bbe1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013vCvoD3TjKQrNi3WBg8GYr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18088,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18088,
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

_source line 6 · 2026-05-22T10:20:58.356Z_

<details><summary>↩ Tool result · `toolu_014xAkgxCLcnPKyTtgtYv7Ka`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	\looseness=-1
10	As approximate parametric bounds, a Monte Carlo power analysis (1,000 replications per condition) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$; 14,042 MMLU items) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$ (details in \Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold. Power varies substantially with item discrimination: TPR ranges from 0.40 at $a = 0.5$ to 0.95 at $a = 2.0$; the gap between TPR at mean $a$ (0.87) and the aggregate TPR (0.68) quantifies the power cost of parameter heterogeneity, consistent with Jensen's inequality (\Cref{app:power_sensitivity}).
11	
12	\subsection{Temporal Comparability: 31\% Measurement Instability}
13	\label{sec:temporal}
14	
15	\looseness=-1
16	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; 95\% bootstrap CI: [29.4\%, 38.1\%], $B = 1{,}000$ model-level resamples; rightward asymmetry reflects heavy-tailed C\% from subjects exceeding 40\%; family-level cluster bootstrap over 29 families with $\geq$3 members yields a wider CI of $[26.7\%, 53.2\%]$, $3.1\times$ the model-level width, confirming robustness under within-family dependence). Leave-one-family-out analysis confirms that no single non-dominant family drives the signal ($|\Delta\mathrm{C\%}| \leq 2.93$\,pp; \Cref{tab:lofo}). Benjamini-Hochberg FDR correction at $q = 0.05$ removes only 3 items (31.32\% $\to$ 31.30\%), because the dual ETS threshold already provides implicit multiple-testing protection.
17	
18	\looseness=-1
19	Three controls confirm this reflects genuine temporal change. A random split of the 2023 cohort yields only 0.18\% ETS~C items (sampling noise), and an ability-quintile comparison within the same temporal cohort yields 2.9\% (ability differences alone). A within-family comparison (Llama-2 vs.\ Llama-3) produces 61.3\% ETS~C items, elevated by large ability gaps~\citep{holland1988mh}. The temporal cohort ability gap is negligible: Cohen's $d = -0.17$ with 76.4\% distributional overlap. Under 1:1 nearest-neighbor matching on total score ($N = 638$ per group, 5 seeds), C\% $= 28.9\% \pm 0.1\%$, confirming at most $\sim$2.4~pp is attributable to ability mismatch. Permutation tests confirm ($p < 0.01$; \Cref{app:method_details}).
20	
21	\looseness=-1
22	Across all 57 subjects, C\% ranges from 20.7\% to 48.4\% (mean $\approx 30\%$; \Cref{tab:temporal_landscape}). DIF rates are domain-invariant (Kruskal-Wallis $p = 0.78$), but DIF \emph{direction} exhibits domain dependence: STEM items favor 2024 models (55.4\%), Humanities favor 2023 (64.4\%). Item-level regression shows 92.4\% of the DIF signal is item-specific (pseudo $R^2 = 0.0007$). A Simpson's paradox confirms that DIF is associated with item properties rather than aggregate accuracy gains: domain accuracy positively predicts DIF at the aggregate level ($\mathrm{OR} = 1.55$, $p = 0.001$) but reverses after controlling for item difficulty and discrimination ($\mathrm{OR} = 0.73$, $p = 0.030$). A difficulty--direction interaction emerges ($\rho = -0.597$): 2024 models gain on hard items while showing relative erosion on easy ones. The conclusion is robust across thresholds ($18.3\%$ at $|\Delta_{\mathrm{MH}}| \geq 2.0$, $10.2\%$ at $\geq 2.5$).
23	
24	\begin{table}[t]
25	\centering
26	\caption{DIF landscape across cohort definitions. ETS~C denotes the percentage of items with $|\Delta_{\mathrm{MH}}| \geq 1.5$. C\% (web-clean) is the DIF-C flagging rate among items classified as web-clean by \citet{li2024contamination}. Enrichment is the ratio of observed to expected overlap between DIF flags and web-overlap labels. Dashes indicate comparisons where Li et al.\ labels are not applicable.}
27	\label{tab:temporal_landscape}
28	\small
29	\resizebox{\columnwidth}{!}{%
30	\begin{tabular}{lcccc}
31	\toprule
32	Cohort Definition & $N_{\mathrm{ref}}$ / $N_{\mathrm{focal}}$ & C\% & C\% (web-clean) & Enrich. \\
33	\midrule
34	Temporal (2023 vs.\ 2024) & 1,080 / 807 & 31.3 & 0.318 & 0.964 \\
35	Ability quintile (Q1--2 vs.\ Q4--5) & ${\sim}$2,600 / ${\sim}$2,600 & 2.9 & 0.027 & 1.19 \\
36	Within-family (Llama-2 vs.\ 3) & 161 / 308 & 61.3 & -- & -- \\
37	Random split (sanity) & 540 / 540 & 0.18 & -- & -- \\
38	Within-subject (avg, 5 subj.) & \textit{varies} & 38.1 & -- & -- \\
39	\bottomrule
40	\end{tabular}}
41	\end{table}
42	
43	\subsection{Ground Truth Mismatch}
44	\label{sec:groundtruth}
45	
46	\looseness=-1
47	Direct comparison of DIF flags against the web-overlap labels of \citet{li2024contamination} on 9,229 annotated items confirms that the two methods capture orthogonal signals. The enrichment ratio is 0.964 (\Cref{tab:temporal_landscape}): DIF-C rates are 30.7\% among web-contaminated items and 31.8\% among clean items. Association tests yield $\phi = 0.012$, $\chi^2 = 1.28$ ($p = 0.258$), and OR $= 1.05$ [0.96, 1.15]; the Jaccard index between flagged sets is 0.206. This near-independence holds across contamination subtypes (input-only enrichment $= 0.986$, input-and-label $= 0.960$). The null result does not indicate detection failure: semi-synthetic injection produces a clear dose-response ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \Cref{fig:dose_response}). The disconnect arises because web-overlap labels measure \emph{global exposure} (whether an item exists in training corpora), while DIF measures \emph{differential functioning} (whether an item's relationship to ability changes across cohorts). The Li et al.\ labels are the wrong ground truth for a differential method. 
48	\begin{figure}[t]
49	\centering
50	\includegraphics[width=\columnwidth]{fig_2_dose_response.pdf}
51	\caption{Semi-synthetic dose-response for DIF detection on MMLU. $\Delta\mathrm{TPR}$ increases monotonically with exploitation rate $p$, confirming that MH-DIF is sensitive to differential item behavior when present. Baseline (no injection) produces $\Delta\mathrm{TPR} \approx 0$.}
52	\label{fig:dose_response}
53	\end{figure}
54	
55	\subsection{Structural Analysis}
56	\label{sec:structural}
57	
58	\looseness=-1
59	Three structural controls fail to reduce temporal C\% below 31\% (\Cref{tab:structural_comparison}): matched-ability quintiles, IRT $\theta$-conditioning ($r(\theta, \mathrm{total\ score}) = 0.9986$), and within-subject DIF (C\% $= 38.1\%$). The elevated within-subject rate partly reflects local dependence: 11.3\% of within-subject item pairs exceed $|Q3| > 0.20$ vs.\ 2.2\% cross-subject, confirming that cross-subject C\% $= 31.3\%$ is the more conservative estimate. Logistic regression DIF confirms 92.1\% concordance with MH and reveals additional non-uniform DIF (24.8\%), making 31\% conservative. Graduated de-duplication reduces C\% moderately ($K{=}10$: 22.7\%; $K{=}20$: 29.1\%), confounded with statistical power reduction from smaller $N$; even $K{=}10$ exceeds the random-split baseline by ${>}100\times$. Ability-matched analysis reduces Llama-2 vs.\ Llama-3 C\% from 61.3\% to $28.3\%$ and temporal C\% from 31.3\% to $28.9\%$---consistent matched values ($\sim$28--29\%) despite vastly different unmatched rates, suggesting genuine item-level DIF accounts for $\sim$28--29\% of items. Six alternative explanations were tested; none reduces C\% below $\sim$28\% (\Cref{app:structural}).
60	
61	\begin{table}[t]
62	\centering
63	\caption{Structural approaches to reducing temporal DIF. None reduces temporal C\% below 31\%, indicating that the observed instability is not an artifact of ability matching.}
64	\label{tab:structural_comparison}
65	\small
66	\resizebox{\columnwidth}{!}{%
67	\begin{tabular}{lcccc}
68	\toprule
69	Approach & Mechanism & Temp.\ C\% & TPR ($p{=}0.5$) & Outcome \\
70	\midrule
71	Baseline (ext.) & Cross-bench.\ total score & $0.314_{\pm.009}$ & $0.834_{\pm.027}$ & Reference \\
72	Matched-ability & Within-quintile temp.\ DIF & ${\sim}$0.31 & -- & Enrich.\ 0.94--1.04 \\
73	$\theta$-cond. & $\theta$ replaces total score & 0.312 & 0.876 & $r(\theta,\mathrm{total}) {=} 0.9986$ \\
74	Within-subject & Per-subject DIF & -- & -- & C\% $= 38.1\%$ ($>$25\%) \\
75	\bottomrule
76	\end{tabular}}
77	\end{table}
78	
79	\subsection{Semi-Synthetic Framework Validation}
80	\label{sec:semisynthetic}
81	
82	\looseness=-1
83	Cross-subject matching achieves $\Delta\mathrm{FPR} = 0.000$ across all five MMLU subjects (4/5 with $\Delta\mathrm{TPR} > 0.3$ at $p = 0.5$, upper-bound estimate under uniform binary flipping; \Cref{sec:injection}), while within-subject matching inflates FPR by ${+}0.186$ on average. Multi-subject injection ($k \in \{1, 3, 5, 10, 20\}$ subjects, 5 random draws each) confirms robustness: $\Delta\mathrm{FPR} < 0.007$ for $k \leq 5$ ($\leq$9\% of domains); at $k = 10$ (18\%), $\Delta\mathrm{FPR}$ rises to 0.026--0.069, marking the boundary of matching variable integrity (\Cref{app:method_details,app:fig_matching}).
84	
85	\subsection{Downstream Impact}
86	\label{sec:downstream}
87	
88	\looseness=-1
89	Stable-item ranks are preserved across all six benchmarks ($\rho = 0.997$, $\tau = 0.958$; flip rate $\leq 2.8\%$; \Cref{tab:cross_benchmark}) despite substantial measurement instability. DIF-flagged items concentrate discriminative signal ($z = -8$ to $-49$ vs.\ random removal; circularity ablation in \Cref{app:fig_downstream}). Model families show distinctive DIF profiles: Llama-3 derivatives ($n = 315$) gain ${+}53$ median rank positions, while Mistral derivatives ($n = 619$) lose $35$ (\Cref{app:fig_downstream}). Among the 200 most displaced models (top 3.8\% by $|\Delta\mathrm{rank}|$; full-sample pairwise flip rate $= 2.0\%$), 33.6\% of pairwise rankings reverse---Qwen1.5-14B-Chat's 610-position lead over mistral-7b-dpo-v6 reverses to a 501-position deficit on stable items. Removing C-flagged items disproportionately disadvantages 2024 models (cohort gap $= 96.2$ positions, $40\times$ random removal; $p < 0.001$), confirming concentrated inter-generational signal in DIF items.
90	
91	\subsection{Cross-Benchmark Validation}
92	\label{sec:gsm8k}
93	
94	\looseness=-1
95	Temporal DIF extends across all six METABENCH benchmarks (\Cref{tab:cross_benchmark}). C\% ranges from 17.9\% (HellaSwag~\citep{zellers2019hellaswag}) to 31.3\% (MMLU). Knowledge/reasoning benchmarks (WinoGrande~\citep{sakaguchi2021winogrande}, TruthfulQA~\citep{lin2022truthfulqa}, ARC~\citep{clark2018arc}) show C\% $= 26.9$--$31.3\%$ versus $17.9$--$18.9\%$ for procedural ones, consistent with knowledge-intensive items being more sensitive to training data composition shifts.
96	
97	\begin{table}[t]
98	\centering
99	\caption{Temporal DIF across six METABENCH benchmarks. C\% = ETS~C items ($|\Delta_{\mathrm{MH}}| \geq 1.5$) between 2023 and 2024 cohorts; $\rho$/$\tau$ = Spearman/Kendall correlation between full and stable-item rankings; Flip = pairwise rank-flip rate; Ratio = C\%/Rand.\ C\%, with baseline varying by benchmark. All six show substantial DIF (45--174$\times$ above random baseline), with knowledge/reasoning benchmarks exhibiting higher C\% than procedural ones.}
100	\label{tab:cross_benchmark}
101	\small
102	\resizebox{\columnwidth}{!}{%
103	\begin{tabular}{lrrrrrrl}
104	\toprule
105	Benchmark & Items & C\% & $\rho$ & $\tau$ & Flip\% & Rand.\ C\% & Ratio \\
106	\midrule
107	MMLU & 12{,}508 & 31.3 & 0.9965 & 0.9600 & 2.00 & 0.18 & 174$\times$ \\
108	WinoGrande & 1{,}267 & 30.3 & 0.9943 & 0.9432 & 2.84 & 0.32 & 95$\times$ \\
109	TruthfulQA & 817 & 29.7 & 0.9971 & 0.9586 & 2.07 & 0.37 & 80$\times$ \\
110	ARC & 1{,}172 & 26.9 & 0.9962 & 0.9538 & 2.31 & 0.60 & 45$\times$ \\
111	GSM8K & 1{,}319 & 18.9 & 0.9993 & 0.9843 & 0.78 & 0.30 & 63$\times$ \\
112	HellaSwag & 10{,}042 & 17.9 & 0.9986 & 0.9722 & 1.39 & 0.28 & 64$\times$ \\
113	\bottomrule
114	\end{tabular}}
115	\end{table}
116	
117	On GSM8K, semi-synthetic injection confirms detection power ($\Delta\mathrm{TPR} = {+}0.514$ at $p = 0.5$; \Cref{app:gsm8k_details}); an exploratory GSM1K analysis is consistent with DIF capturing capability change distinct from memorization ($r = -0.478$, $p = 0.005$; \Cref{app:fig_gsm1k}). DIF remains substantial within a 6-month window (2023-H2 vs.\ 2024-H1: MMLU C\% $= 34.35\%$).
118	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "942d6c3b-a506-46d5-ad98-6b54d0f493c2",
  "isSidechain": true,
  "promptId": "f90137fe-a99e-4ab9-b8fe-8a63993956e8",
  "agentId": "ab47b7a11c46d59e1",
  "type": "user",
  "uuid": "573dd70c-d134-4f9d-80c3-30ced0864cc2",
  "sourceToolAssistantUUID": "942d6c3b-a506-46d5-ad98-6b54d0f493c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "1e821804-de94-461a-97da-c43c5977bbe1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T10:20:58.577Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VPeu8qwd3CLAHUnwkSEhvU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "573dd70c-d134-4f9d-80c3-30ced0864cc2",
  "isSidechain": true,
  "agentId": "ab47b7a11c46d59e1",
  "requestId": "req_011CbHSTaHfiC5eHRvFwNo36",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dd9df944-a8b1-4c16-a567-8b3abb52295c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "1e821804-de94-461a-97da-c43c5977bbe1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013vCvoD3TjKQrNi3WBg8GYr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18088,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18088,
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

_source line 8 · 2026-05-22T10:20:58.590Z_

<details><summary>↩ Tool result · `toolu_01VPeu8qwd3CLAHUnwkSEhvU`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	\enlargethispage{2\baselineskip}
4	
5	\subsection{Implications for Benchmark Temporal Comparability}
6	\label{sec:disc_temporal}
7	
8	\looseness=-1
9	Temporal DIF decomposes benchmark differences into impact (ability differences removed by matching, $\sim$2.4~pp), DIF (item-level differences after ability control, $\sim$28--29\% floor, 92.4\% item-specific), and attribution (contamination, capability evolution, or methodology shifts---underdetermined without training data).
10	
11	\subsection{Ground Truth Meta-Critique}
12	\label{sec:disc_groundtruth}
13	
14	\looseness=-1
15	The near-independence between DIF flags and web-overlap labels (\Cref{sec:groundtruth}) reflects a category error: web-overlap measures global exposure while DIF measures differential functioning. Semi-synthetic dose-response confirms detection works when present; the disconnect is in the ground truth.
16	
17	\subsection{Recommended DIF Audit Protocol}
18	\label{sec:disc_protocol}
19	
20	\looseness=-1
21	Item-level properties do not reliably predict DIF susceptibility (AUROC $= 0.60$; \Cref{app:predictive}), confirming that post-hoc monitoring cannot be replaced by pre-screening.
22	We propose temporal MH-DIF whenever $\geq$500 models accumulate, with $\rho$-degradation-grounded action levels (\Cref{app:fig_rho_degradation}):
23	(1)~\emph{Monitor} (C\% $< 15\%$): report C\% in release notes.
24	(2)~\emph{Flag} ($15$--$25\%$): report stable-item rankings as sensitivity analysis alongside full rankings.
25	(3)~\emph{Act} (C\% $\geq 25\%$): review flagged items for differential-performance-associated content characteristics; report stable-item rankings as primary metric; use DIF pre-screening to identify stable anchors for equating~\citep{kolen2014equating,habba2026growingpains}.
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd9df944-a8b1-4c16-a567-8b3abb52295c",
  "isSidechain": true,
  "promptId": "f90137fe-a99e-4ab9-b8fe-8a63993956e8",
  "agentId": "ab47b7a11c46d59e1",
  "type": "user",
  "uuid": "6794eea0-24fc-4cfd-8087-b44b1e088b7d",
  "sourceToolAssistantUUID": "dd9df944-a8b1-4c16-a567-8b3abb52295c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "1e821804-de94-461a-97da-c43c5977bbe1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T10:20:58.772Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MvxcSQi5YaqJNL5GRwXRnb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6794eea0-24fc-4cfd-8087-b44b1e088b7d",
  "isSidechain": true,
  "agentId": "ab47b7a11c46d59e1",
  "requestId": "req_011CbHSTaHfiC5eHRvFwNo36",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "90b43770-d58e-43e9-b4f1-152e962e9333",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "1e821804-de94-461a-97da-c43c5977bbe1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013vCvoD3TjKQrNi3WBg8GYr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18088,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18088,
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

_source line 10 · 2026-05-22T10:20:58.777Z_

<details><summary>↩ Tool result · `toolu_01MvxcSQi5YaqJNL5GRwXRnb`</summary>

```text
1	\section*{Limitations}
2	
3	\paragraph{Methodological scope.}
4	MH-DIF detects only uniform DIF; logistic regression reveals an additional 24.8\% non-uniform DIF, making 31\% conservative. More fundamentally, DIF detects \emph{that} items function differently but cannot determine \emph{why}---the signal may reflect contamination, capability change, or training methodology shifts. A definitive causal decomposition remains out of reach without access to model training data. The semi-synthetic framework uses binary response flipping (incorrect $\to$ correct) to simulate differential contamination, representing a worst-case uniform exploitation pattern. Real-world contamination involves partial memorization, reasoning shortcuts, and format-specific advantages; detection power under such realistic patterns is untested. The moderate $\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$ reflects sensitivity to severe differential behavior; the framework's primary methodological contribution---cross-subject matching achieving $\Delta\mathrm{FPR} = 0.000$---is a matching strategy property independent of injection realism.
5	
6	\paragraph{Examinee non-independence.}
7	The MH $\chi^2$ test assumes independent examinees, yet LLMs sharing base models, training data, or architectures violate this assumption. Empirical mitigations partially address this: permutation simulation bounds LD-attributable FPR inflation to ${<}0.001$~pp, and graduated de-duplication ($K{=}20$: C\% $= 29.1\%$) shows family structure does not inflate results. \citet{french2010hierarchical} show that MH maintains nominal size under moderate clustering in educational settings, consistent with our empirical findings; however, the extreme relatedness of some LLM families (e.g., hundreds of Llama-2 fine-tunes) exceeds the clustering levels studied in that work. Cluster bootstrap resampling at the family level (29 families with $\geq$3 members, 1{,}882 models, $B = 1{,}000$) yields a 95\% CI of $[26.7\%, 53.2\%]$, $3.1\times$ wider than the model-level CI $[29.4\%, 38.1\%]$, partly because LLM families are cohort-specific (no family spans both 2023 and 2024), so resampling families simultaneously varies the reference/focal composition. Despite this conservative bound, the lower bound far exceeds the random-split baseline (0.18\%), confirming robustness to within-family dependence.
8	
9	\paragraph{Matching boundary and sample size.}
10	Cross-subject matching assumes contamination affects a minority of domains; when contamination spans ${>}10$ subjects (${>}18\%$ of MMLU), $\Delta\mathrm{FPR}$ rises to 0.026--0.069. Model-level bootstrap may underestimate CI width due to within-family correlation; family-level cluster bootstrap (preceding paragraph) confirms robustness despite a $3.1\times$ wider CI. The GSM1K correlation analysis ($N = 33$) has limited statistical power and is exploratory.
11	
12	\paragraph{Generalizability.}
13	All six benchmarks use multiple-choice or binary scoring; generalizability to open-ended generation (e.g., AlpacaEval), coding (e.g., HumanEval), or partial-credit benchmarks is untested and would require polytomous DIF methods. Temporal cohorts are defined by calendar year, a coarse grouping; finer-grained definitions (e.g., by training data cutoff or alignment method) might reveal more targeted patterns. All models are drawn from the Open LLM Leaderboard; generalizability to closed-source models cannot be assessed.
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90b43770-d58e-43e9-b4f1-152e962e9333",
  "isSidechain": true,
  "promptId": "f90137fe-a99e-4ab9-b8fe-8a63993956e8",
  "agentId": "ab47b7a11c46d59e1",
  "type": "user",
  "uuid": "8096f6e1-1991-4c34-b42e-2e43f9c37835",
  "sourceToolAssistantUUID": "90b43770-d58e-43e9-b4f1-152e962e9333",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "1e821804-de94-461a-97da-c43c5977bbe1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T10:20:59.107Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SbATnUC5j8YhZ3Agz6QkDN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8096f6e1-1991-4c34-b42e-2e43f9c37835",
  "isSidechain": true,
  "agentId": "ab47b7a11c46d59e1",
  "requestId": "req_011CbHSTaHfiC5eHRvFwNo36",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "73b12458-33da-401b-8a57-0fefd96cdbbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "1e821804-de94-461a-97da-c43c5977bbe1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013vCvoD3TjKQrNi3WBg8GYr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18088,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18088,
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

_source line 12 · 2026-05-22T10:20:59.113Z_

<details><summary>↩ Tool result · `toolu_01SbATnUC5j8YhZ3Agz6QkDN`</summary>

```text
1	\section{Method Details}
2	\label{app:method_details}
3	
4	\subsection{Diagnostics}
5	\label{app:diagnostics}
6	
7	Three diagnostic procedures complement the primary DIF analysis.
8	
9	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
10	
11	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
12	
13	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
14	
15	\subsection{Statistical Considerations}
16	\label{app:statistical}
17	
18	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini-Hochberg FDR correction at $q = 0.05$. The random-split sanity check provides an empirical estimate of the false positive rate under the null hypothesis.
19	
20	\paragraph{Threshold sensitivity.} We report results across a range of DIF thresholds ($|\Delta_{\mathrm{MH}}| \in \{1.0, 1.5, 2.0, 2.5\}$) to verify that qualitative conclusions do not depend on the specific ETS~C cutoff. The standard threshold of $|\Delta_{\mathrm{MH}}| \geq 1.5$ corresponds to the ETS~C definition used throughout the paper.
21	
22	\paragraph{IRT model fit.} For transparency, we report that the MMLU response matrix shows poor fit to a unidimensional 2PL model (expected for a 57-subject multidimensional benchmark). This does not affect MH-DIF validity, which relies only on total score stratification rather than parametric IRT assumptions.
23	
24	\paragraph{Architecture heterogeneity.} The METABENCH MMLU population consists of 99.98\% decoder-only models (5,226 of 5,227). This near-complete architectural homogeneity eliminates architecture as a confound for DIF analysis. We verify this by excluding the single encoder-decoder model and confirming identical results.
25	
26	\paragraph{Power sensitivity to item discrimination.}
27	\label{app:power_sensitivity}
28	The Monte Carlo power analysis in \Cref{sec:validation} uses average 2PL parameters ($\bar{a} = 1.2$, $\bar{b} = -0.84$). \Cref{tab:power_sensitivity} reports TPR as a function of discrimination $a$ (other parameters at their means, $N = 80$ per cohort, $|\Delta_b| = 1.4$, 1,000 replications). TPR increases monotonically from 0.40 ($a = 0.5$) to 0.95 ($a = 2.0$); FPR remains below 0.04 throughout. The MMLU item pool shows substantial heterogeneity: $a$ ranges from 0.006 to 2.657 (SD $= 0.54$, IQR $= [0.75, 1.64]$). The aggregate TPR of 0.68 from Phase~2 reflects this full distribution, while TPR at mean $a \approx 1.2$ is 0.87---the gap is consistent with Jensen's inequality applied to the concave TPR($a$) function. Although 2PL fit is poor for MMLU's multidimensional structure, the power analysis serves as one leg of a triangulation: parametric estimates (TPR $= 0.68$--$0.80$) are validated by empirical semi-synthetic injection ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \Cref{sec:semisynthetic}), confirming adequate detection power regardless of parametric assumptions.
29	
30	\begin{table}[h]
31	\centering
32	\caption{Power sensitivity to item discrimination. TPR = true positive rate for ETS~C detection ($|\Delta_{\mathrm{MH}}| \geq 1.5$) at $N = 80$ per cohort, $|\Delta_b| = 1.4$, 1,000 replications.}
33	\label{tab:power_sensitivity}
34	\small
35	\begin{tabular}{rccc}
36	\toprule
37	$a$ & TPR & 95\% CI & FPR \\
38	\midrule
39	0.5 & 0.398 & [0.20, 0.60] & 0.033 \\
40	0.8 & 0.683 & [0.45, 0.90] & 0.036 \\
41	1.0 & 0.808 & [0.60, 0.95] & 0.038 \\
42	1.2 ($\approx \bar{a}$) & 0.874 & [0.70, 1.00] & 0.038 \\
43	1.5 & 0.930 & [0.80, 1.00] & 0.038 \\
44	2.0 & 0.949 & [0.80, 1.00] & 0.037 \\
45	\bottomrule
46	\end{tabular}
47	\end{table}
48	
49	\paragraph{Logistic regression specification.} The Simpson's paradox analysis (\Cref{sec:temporal}) uses binary logistic regression with DIF-C classification as the dependent variable, domain-level accuracy change (2024 minus 2023 mean accuracy) as the primary predictor, and item difficulty (proportion correct) and IRT discrimination (point-biserial correlation) as controls. The interaction between domain accuracy change and item difficulty is included. Non-uniform DIF detection (\Cref{sec:structural}) uses logistic regression with a group $\times$ ability interaction term; a significant interaction ($p < 0.05$) indicates non-uniform DIF.
50	
51	\section{Structural Analysis Details}
52	\label{app:structural}
53	
54	Three progressively refined approaches fail to reduce the temporal false positive rate below 31\%, revealing a structural property of the data rather than a methodological limitation. Matched-ability quintile analysis restricts comparisons to models of similar total score and yields enrichment ratios of 0.94--1.04, with temporal FPR unchanged at approximately 0.31. IRT $\theta$-conditioning with 20 ability strata achieves $r(\theta, \mathrm{total\ score}) = 0.9986$ and FPR $= 0.312$, confirming that the external total score already captures nearly all ability variance relevant to DIF computation. Within-subject DIF analysis on 5 representative subjects, intended to isolate subject-specific effects, finds mean C\% $= 38.1\%$, exceeding the 25\% threshold that would indicate viable bifactor structure. \Cref{tab:structural_comparison} summarizes these results.
55	
56	The temporal FPR reflects genuine item-level instability that persists regardless of how ability is measured or conditioned. Yen's Q3 diagnostic reveals mild local dependence within subjects (11.3\% of within-subject item pairs exceed $|Q3| > 0.20$, vs.\ 2.2\% cross-subject; $5{\times}$ ratio, $p = 2.3 \times 10^{-9}$), which contributes to elevated within-subject DIF rates but is not the primary driver: the cross-subject matching protocol addresses this bias, and temporal C\% persists under external matching (full Q3 distributions available in the supplementary material).
57	
58	\begin{table}[h]
59	\centering
60	\caption{Multi-subject injection robustness. $k$ = number of simultaneously contaminated subjects (out of 57); values are mean $\pm$ SD across 5 random subject draws at exploitation rate $p = 0.5$.}
61	\label{tab:multi_subject_injection}
62	\small
63	\begin{tabular}{rcc}
64	\toprule
65	$k$ & $\Delta\mathrm{FPR}$ & $\Delta\mathrm{TPR}$ \\
66	\midrule
67	1 & $0.000_{\pm.000}$ & $0.371_{\pm.048}$ \\
68	3 & $0.003_{\pm.002}$ & $0.385_{\pm.031}$ \\
69	5 & $0.007_{\pm.003}$ & $0.392_{\pm.027}$ \\
70	10 & $0.047_{\pm.022}$ & $0.401_{\pm.024}$ \\
71	20 & $0.069_{\pm.018}$ & $0.410_{\pm.020}$ \\
72	\bottomrule
73	\end{tabular}
74	\end{table}
75	
76	\begin{table}[h]
77	\centering
78	\caption{Leave-one-family-out (LOFO) robustness on MMLU. Removing non-dominant families ($\leq$15\% of their cohort) changes C\% by at most 2.93\,pp. Larger shifts from removing Mistral or Llama-3 reflect both their outsized cohort share ($>$39\%) and reduced MH statistical power from smaller remaining samples. Stratification uses total test score for computational efficiency; cross-subject matching yields identical baseline C\%.}
79	\label{tab:lofo}
80	\small
81	\begin{tabular}{lrrr}
82	\toprule
83	Family & $N$ removed & Cohort share & C\% (LOFO) \\
84	\midrule
85	\emph{Full sample} & --- & --- & 31.32 \\
86	Mistral & 547 & 51\% ref & 22.47 \\
87	Llama-3 & 315 & 39\% foc & 24.06 \\
88	Mixtral & 120 & 15\% foc & 34.26 \\
89	Llama-2 & 161 & 15\% ref & 31.48 \\
90	Solar & 91 & 11\% foc & 31.01 \\
91	\bottomrule
92	\end{tabular}
93	\end{table}
94	
95	\section{Cross-Benchmark Comparison}
96	\label{app:gsm8k_details}
97	
98	\begin{table}[h]
99	\centering
100	\caption{Cross-benchmark comparison of DIF analysis on MMLU and GSM8K. Both benchmarks exhibit temporal measurement instability with validated semi-synthetic detection power. Standard and external matching use different exploitation rates ($p$) because each benchmark's optimal operating point differs; external matching results are compared at $p = 0.5$ for both. Subscript $\pm$ values denote standard deviations across 5 random injection seeds.}
101	\label{tab:gsm8k_comparison}
102	\small
103	\begin{tabular}{lcc}
104	\toprule
105	Metric & MMLU & GSM8K \\
106	\midrule
107	Items & 12,508 & 1,319 \\
108	Models & 5,227 & 6,702 \\
109	Temporal C\% & 31.3\% & 18.9\% \\
110	Sanity C\% & 0.18\% & 0.3\% \\
111	$\Delta$TPR ($p{=}0.7$, standard) & -- & $+0.818_{\pm.006}$ \\
112	$\Delta$TPR ($p{=}0.5$, external) & $+0.508_{\pm.027}$ & $+0.514_{\pm.028}$ \\
113	\bottomrule
114	\end{tabular}
115	\end{table}
116	
117	\section{Additional Figures}
118	\label{app:figures}
119	
120	\begin{figure}[h]
121	\centering
122	\includegraphics[width=\columnwidth]{fig_3_within_subject_matching.pdf}
123	\caption{Cross-subject vs.\ within-subject matching for semi-synthetic DIF detection. Cross-subject matching eliminates FPR inflation ($\Delta\mathrm{FPR} = 0.000$) while preserving detection power ($\Delta\mathrm{TPR} > 0.3$ for 4/5 subjects at $p = 0.5$). Within-subject matching inflates FPR by ${+}0.186$ on average.}
124	\label{app:fig_matching}
125	\end{figure}
126	
127	\begin{figure}[h]
128	\centering
129	\includegraphics[width=\columnwidth]{fig_4_downstream_impact.pdf}
130	\caption{Downstream impact of DIF-based item filtering on model rankings. Despite $\rho \approx 0.997$ overall, individual model families show systematic rank shifts when evaluated on stable items only.}
131	\label{app:fig_downstream}
132	\end{figure}
133	
134	\begin{figure}[h]
135	\centering
136	\includegraphics[width=\columnwidth]{fig_5_gsm1k_dif_correlation.pdf}
137	\caption{GSM1K contamination gap vs.\ DIF ranking advantage ($N = 33$). The negative correlation ($r = -0.478$, $p = 0.005$) indicates that models with larger contamination gaps benefit less from DIF-flagged items.}
138	\label{app:fig_gsm1k}
139	\end{figure}
140	
141	\begin{figure}[h]
142	\centering
143	\includegraphics[width=\columnwidth]{fig_A3_rho_degradation.pdf}
144	\caption{Ranking degradation under DIF-ordered vs.\ random item removal across six benchmarks. DIF-ordered removal (orange) consistently degrades $\rho$ faster than random removal (blue band = mean $\pm$ 1 SD, 20 seeds). Vertical dashed lines mark the Monitor/Flag (15\%) and Flag/Act (25\%) thresholds from \Cref{sec:disc_protocol}.}
145	\label{app:fig_rho_degradation}
146	\end{figure}
147	
148	\section{Item-Property Predictive Analysis}
149	\label{app:predictive}
150	
151	To test whether DIF susceptibility is a fixed item property, we trained logistic regression and LightGBM classifiers to predict ETS~C classification from 17 leak-free features: ref-cohort difficulty and discrimination, 11 text features (question/option length, vocabulary metrics), subject metadata, and web-overlap labels~\citep{li2024contamination}. Features were computed exclusively from the reference (2023) cohort to prevent information leakage from the focal cohort. Five-fold subject-stratified cross-validation (no within-subject train/test overlap) yielded AUROC $= 0.603 \pm 0.020$ (LR) and $0.599 \pm 0.026$ (LightGBM)---near chance. Web-overlap labels contributed negligibly (SHAP $< 0.015$), independently confirming the DIF--contamination orthogonality reported in \Cref{sec:groundtruth}. These results indicate that temporal DIF reflects emergent cohort--item interactions rather than fixed item defects, motivating post-hoc monitoring over pre-screening.
152	
153	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73b12458-33da-401b-8a57-0fefd96cdbbc",
  "isSidechain": true,
  "promptId": "f90137fe-a99e-4ab9-b8fe-8a63993956e8",
  "agentId": "ab47b7a11c46d59e1",
  "type": "user",
  "uuid": "90f4c65e-10e4-47a5-a1c5-f4833545878a",
  "sourceToolAssistantUUID": "73b12458-33da-401b-8a57-0fefd96cdbbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "1e821804-de94-461a-97da-c43c5977bbe1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T10:20:59.193Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VHetHLsMckijBufDkW6xPi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90f4c65e-10e4-47a5-a1c5-f4833545878a",
  "isSidechain": true,
  "agentId": "ab47b7a11c46d59e1",
  "requestId": "req_011CbHSTaHfiC5eHRvFwNo36",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e0830711-8b5a-4950-9299-fd5e2197d91c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "1e821804-de94-461a-97da-c43c5977bbe1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013vCvoD3TjKQrNi3WBg8GYr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18088,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18088,
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

_source line 14 · 2026-05-22T10:20:59.200Z_

<details><summary>↩ Tool result · `toolu_01VHetHLsMckijBufDkW6xPi`</summary>

```text
1	\begin{abstract}
2	LLM benchmark scores are routinely compared across model generations, yet whether individual items measure the same construct over time is rarely tested---and existing contamination detectors validate against ground truth that conflates global exposure with differential functioning. We develop a semi-synthetic injection framework with cross-subject matching that achieves zero false positive inflation under single-subject contamination ($\Delta\mathrm{FPR} = 0.000$) while preserving detection power under worst-case uniform injection ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$), and show that web-overlap contamination labels are near-independent of Mantel-Haenszel Differential Item Functioning (DIF) flags (enrichment $\approx 0.96$)---exposing a category error in prevailing validation methodology. Applying MH-DIF with ETS severity classification to six METABENCH benchmarks (5,227 models, 27,125 items), we find 17.9--31.3\% of items exhibit large temporal DIF (ETS~C) between 2023 and 2024 cohorts, with knowledge/reasoning benchmarks more affected (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$). This does not threaten aggregate ranking validity ($\rho \approx 0.997$, $\tau \approx 0.958$), but specific model families show concentrated rank shifts (Llama-3: ${+}53$ median positions, Mistral: $-35$) and 2.0\% of pairwise rankings reverse. Item-level decomposition shows 92.4\% of the signal is item-specific; DIF-flagged items concentrate discriminative information ($z = -8$ to $-49$) with a difficulty--direction interaction ($\rho = -0.597$): gains on hard items, erosion on easy ones. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0830711-8b5a-4950-9299-fd5e2197d91c",
  "isSidechain": true,
  "promptId": "f90137fe-a99e-4ab9-b8fe-8a63993956e8",
  "agentId": "ab47b7a11c46d59e1",
  "type": "user",
  "uuid": "33b0d46c-887a-411f-a3f2-03bc9917f4bf",
  "sourceToolAssistantUUID": "e0830711-8b5a-4950-9299-fd5e2197d91c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "1e821804-de94-461a-97da-c43c5977bbe1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T10:20:59.405Z_

<details open><summary>🔧 Tool call — Read · `toolu_0184w8NY5NiQuaKqAHSgF1n1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33b0d46c-887a-411f-a3f2-03bc9917f4bf",
  "isSidechain": true,
  "agentId": "ab47b7a11c46d59e1",
  "requestId": "req_011CbHSTaHfiC5eHRvFwNo36",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "089fd2df-9c58-46ac-bc32-94629a75dc8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "1e821804-de94-461a-97da-c43c5977bbe1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013vCvoD3TjKQrNi3WBg8GYr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18088,
      "cache_read_input_tokens": 0,
      "output_tokens": 568,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18088
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 568,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18088,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18088,
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

_source line 16 · 2026-05-22T10:20:59.433Z_

<details><summary>↩ Tool result · `toolu_0184w8NY5NiQuaKqAHSgF1n1`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} and find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. This pattern persists across all 57 MMLU subjects (C\% range 21--48\%, unweighted mean $\approx 30\%$), and item-level regression shows that 92.4\% of the DIF signal is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained. Crucially, this measurement instability does not threaten benchmark validity: Spearman rank correlation between model rankings computed on all items versus stable-only items is $\rho \approx 0.997$. The instability is diagnostic, not destructive; it reveals which capability dimensions shift across model generations rather than rendering MMLU scores unreliable.
5	
6	A growing body of contamination detection research has produced sophisticated item-level methods, from membership inference~\citep{shi2024mink} to performance-based detectors~\citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique}. These methods validate detection accuracy primarily against web-overlap labels such as those of \citet{li2024contamination}, which classify benchmark items as contaminated based on verbatim or near-verbatim matches in publicly accessible training corpora. Such labels measure \emph{global exposure}: whether an item exists in the data ecosystem that all training pipelines can access. They do not measure \emph{differential item functioning}: whether an item behaves differently across model cohorts that may have had varying degrees of exposure or different training methodologies. \Cref{fig:global_vs_differential} illustrates the distinction. Most MMLU items are globally contaminated in the sense that they exist in web-accessible text, so all model cohorts encounter them and no differential signal arises. The items that function differentially are those where exposure or training methodology changed asymmetrically across cohorts. Validating differential detectors against global-exposure labels therefore conflates two phenomena. Direct comparison confirms near-independence between the two flag sets (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$), consistent across contamination subtypes.
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=\columnwidth]{fig_1_global_vs_differential.pdf}
11	\caption{Global vs.\ differential contamination, illustrated via Item Characteristic Curves (ICCs). \textbf{Left}: global contamination produces no DIF; both cohorts encounter the item, and their ICCs overlap. \textbf{Right}: differential contamination produces DIF; the focal cohort's ICC shifts because only that cohort was disproportionately exposed during training. The enrichment ratio of $\approx 1.0$ between DIF flags and web-overlap labels is expected because most MMLU items fall into the left category.}
12	\label{fig:global_vs_differential}
13	\end{figure}
14	
15	We apply classical MH-DIF with ETS classification to the full METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items), to our knowledge, the largest-scale DIF analysis on LLM benchmarks. This psychometric approach complements concurrent work on anchor-item calibration for score comparability~\citep{habba2026growingpains} and addresses the fragility of existing contamination detectors under post-training perturbation~\citep{wang2026fragility}. Semi-synthetic injection experiments confirm that MH-DIF is sensitive to differential item behavior when present ($\Delta\mathrm{TPR} = {+}0.508$ at exploitation rate $p = 0.5$), and our cross-subject matching protocol eliminates false positive inflation ($\Delta\mathrm{FPR} = 0.000$). Three structural controls (matched-ability quintile analysis, IRT $\theta$-conditioning, and within-subject pre-checks) confirm that the approximately 31\% temporal DIF rate cannot be attributed to methodological artifacts, establishing it as a robust empirical finding about LLM benchmark measurement properties, replicated across all six METABENCH benchmarks (\Cref{sec:gsm8k}). MH-DIF detects \emph{that} items function differently across cohorts, not \emph{why}---the signal may reflect contamination, capability change, or training methodology shifts.
16	
17	MMLU's 12,508 items provide sufficient measurement redundancy that removing nearly a third does not alter rank order ($\rho \approx 0.997$). DIF should therefore be understood as a diagnostic lens rather than a quality filter: DIF-flagged items concentrate discriminative signal ($z = -8$ to $-49$ vs.\ random removal), and model families show distinctive DIF profiles (Llama-3 gains ${+}53$ median rank positions, Mistral loses $35$).
18	
19	Our contributions are methodological and empirical, not algorithmic:
20	
21	\begin{enumerate}
22	\item \textbf{Ground truth meta-critique}: Web-overlap contamination labels~\citep{li2024contamination} do not provide appropriate ground truth for item-level differential detectors. Direct empirical comparison on 9,229 items shows near-independence (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$), exposing a validation methodology gap (\Cref{sec:groundtruth}).
23	
24	\item \textbf{Semi-synthetic validation framework}: Controlled injection with cross-subject matching achieves $\Delta\mathrm{FPR} = 0.000$ under single-subject contamination while preserving detection power ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$); cross-benchmark replication on GSM8K confirms generality (\Cref{sec:semisynthetic,sec:gsm8k}).
25	
26	\item \textbf{Temporal measurement instability at scale}: Approximately 31\% of MMLU items exhibit differential functioning across model generations under ETS~C classification; replication across all six METABENCH benchmarks yields C\% $= 17.9$--$31.3\%$, with knowledge/reasoning benchmarks showing higher DIF rates than procedural ones (\Cref{sec:temporal,sec:gsm8k,sec:downstream}).
27	\end{enumerate}
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "089fd2df-9c58-46ac-bc32-94629a75dc8d",
  "isSidechain": true,
  "promptId": "f90137fe-a99e-4ab9-b8fe-8a63993956e8",
  "agentId": "ab47b7a11c46d59e1",
  "type": "user",
  "uuid": "efc06e5b-71ed-4586-abd5-ddb7946d00dd",
  "sourceToolAssistantUUID": "089fd2df-9c58-46ac-bc32-94629a75dc8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "1e821804-de94-461a-97da-c43c5977bbe1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-22T10:21:58.147Z_

I have retrieved all seven LaTeX source files. Here is a comprehensive report of the paper's key technical content for your peer review:

## ABSTRACT

**Dataset & Sample**: 5,227 models evaluated on 12,508 MMLU items; 27,125 items across six METABENCH benchmarks
**Primary Finding**: 17.9--31.3% of items exhibit large temporal DIF (ETS Category C) between 2023 and 2024 cohorts
**Key Statistics**: 
- Knowledge/reasoning benchmarks: C% ≥ 26.9% (MMLU 31.3%, WinoGrande 30.3%, TruthfulQA 29.7%, ARC 26.9%)
- Procedural benchmarks: C% ≤ 18.9% (GSM8K 18.9%, HellaSwag 17.9%)
- Item-specific signal: 92.4% of DIF signal is item-specific
- Rank correlation preserved: ρ ≈ 0.997, τ ≈ 0.958
- Pairwise rank reversals: 2.0% of model pairs flip rankings
- Semi-synthetic validation: ΔTPr = +0.508 at p = 0.5; ΔFPr = 0.000
- Web-overlap independence: enrichment ≈ 0.96

## INTRODUCTION

**Cohort Sizes**: 
- 2023: N = 1,080 models
- 2024: N = 807 models
**Primary Finding**: 31% of MMLU items receive ETS Category C classification (|ΔMH| ≥ 1.5, p < 0.05)
**Sanity Check**: Random split within 2023 cohort = 0.18% ETS C items
**Range**: C% across 57 MMLU subjects: 21--48% (unweighted mean ≈ 30%)
**Item-Specificity**: 92.4% of DIF signal is item-specific, not attributable to aggregate domain-level accuracy gains

**Ground Truth Meta-Critique**:
- Web-overlap enrichment ratio: 0.964 (DIF-C rates: 30.7% contaminated, 31.8% clean items)
- Jaccard index: 0.206
- φ = 0.012; χ² = 1.28 (p = 0.258); OR = 1.05 [0.96, 1.15]
- Input-only enrichment: 0.986; Input-and-label: 0.960

**Temporal Comparability Assumption**: Validates that MMLU measures the same construct across model cohorts

## METHOD

**Data Structure**: 
- METABENCH response matrix: 5,227 models × 12,508 MMLU items
- MMLU: 57 subjects grouped into 5 broad domains (STEM, Humanities, Social Sciences, Other, mixed)
- Web-contamination labels: 9,229 of 12,508 items (73.8% coverage)

**Mantel-Haenszel DIF Procedure**:
- K = 5 equiprobable strata (quintile-based binning) following ETS recommended practice
- Formula: α_MH = (Σ A_k D_k / T_k) / (Σ B_k C_k / T_k)
- ETS Delta Scale: Δ_MH = -2.35 ln(α_MH)
- ETS Classification:
  * Category A (negligible): |Δ_MH| < 1.0
  * Category B (moderate): 1.0 ≤ |Δ_MH| < 1.5, or |Δ_MH| ≥ 1.5 without significance
  * Category C (large): |Δ_MH| ≥ 1.5 AND p < 0.05 (MH chi-squared test)

**Example Calculation**: 
- Odds ratio α_MH = 0.42 → Δ_MH = -2.35 ln(0.42) = 2.04 (classified as ETS C)

**Matching Strategies**: 
1. Standard matching: within-benchmark total score
2. Cross-subject matching: total score excluding target subject (addresses matching variable contamination)
3. External matching: total score on different benchmark

**IRT Correlation**: θ correlates with total scores at r = 0.9986

**LLM-Specific Challenges**:
- Local independence: Permutation simulation (1,000 iterations × 8 subjects, Q3 = 4.6--34.2%) confirms LD-attributable FPR inflation < 0.001 pp under cross-subject matching with ETS C
- Non-independence of fine-tuned variants: Graduated de-duplication shows family structure does not inflate C%
- Non-normal ability distribution: Bimodal from base vs. instruction-tuned models
- Multidimensionality: 57 subjects span multiple latent dimensions

**Cohort Designs** (5 comparisons):
1. Temporal: 2023 (N = 1,080) vs. 2024 (N = 807)
2. Ability-quintile: Q1--Q2 vs. Q4--Q5 within same temporal window
3. Within-family: Llama-2 (N = 161) vs. Llama-3 (N = 308)
4. Within-subject: per-subject DIF
5. Random split: two random halves of 2023 cohort (N = 540 each)

**Semi-Synthetic Injection Framework**:
- Selection: 20% of ETS A items uniformly at random
- Exploitation rates: p ∈ {0.0, 0.3, 0.5, 0.7, 1.0}
- Metrics: ΔTPR = TPR(injected) - TPR(baseline); ΔFPR = FPR(injected) - FPR(baseline)
- Replicates: 5 random seeds per injection level
- Cross-subject matching achieves: ΔFPR = 0.000 (bootstrap 95% CI = [0.000, 0.000])
- Multi-domain robustness: ΔFPR = 0 for k ≤ 5 subjects (~9% of domains); degrades gracefully at k > 5

## EXPERIMENTS

**Power Analysis** (Monte Carlo, 1,000 replications):
- Empirical parameters: ā = 1.2, b̄ = -0.84 (from 14,042 MMLU items)
- At N ≥ 80 per cohort: TPR = 0.68--0.80, FPR = 0.036--0.042, AUC = 0.93--0.94 for |ΔMH| ≥ 1.4
- TPR by discrimination: ranges from 0.40 (a=0.5) to 0.95 (a=2.0); mean a (0.87) vs. aggregate TPR (0.68) gap consistent with Jensen's inequality

**Temporal Comparability Results** (2023 vs 2024):
- **Primary Finding**: 31.3% ETS C items (95% bootstrap CI: [29.4%, 38.1%]; family-level cluster bootstrap: [26.7%, 53.2%])
- Family-level CI is 3.1× wider than model-level, confirming robustness under within-family dependence
- Leave-one-family-out: No single family drives signal (|ΔC%| ≤ 2.93 pp)
- Benjamini-Hochberg FDR (q = 0.05): Removes only 3 items (31.32% → 31.30%)

**Control Tests**:
- Random split (2023 cohort): 0.18% ETS C
- Ability-quintile (Q1--Q2 vs Q4--Q5): 2.9% ETS C
- Within-family (Llama-2 vs. Llama-3): 61.3% ETS C
- Ability gap: Cohen's d = -0.17 with 76.4% distributional overlap
- 1:1 nearest-neighbor matching: C% = 28.9% ± 0.1% (N = 638 per group, 5 seeds)
- Permutation tests: p < 0.01

**Across 57 Subjects**:
- C% range: 20.7% to 48.4% (mean ≈ 30%)
- Domain-invariance: Kruskal-Wallis p = 0.78
- STEM items: 55.4% favor 2024 models
- Humanities items: 64.4% favor 2023 models
- Item-level regression R² = 0.0007 (92.4% item-specific)
- Simpson's paradox: Domain accuracy effect reverses after controlling for item properties (OR = 1.55, p = 0.001 → OR = 0.73, p = 0.030)
- Difficulty-direction interaction: ρ = -0.597 (2024 gains on hard items, erosion on easy ones)
- Threshold robustness: 18.3% at |ΔMH| ≥ 2.0; 10.2% at ≥ 2.5

**Table 1 (Temporal Landscape)**:
| Cohort | N_ref / N_focal | C% | C% (web-clean) | Enrichment |
|--------|-----------------|-------|----------------|------------|
| Temporal | 1,080 / 807 | 31.3 | 0.318 | 0.964 |
| Ability Q1-2 vs Q4-5 | ~2,600 / ~2,600 | 2.9 | 0.027 | 1.19 |
| Llama-2 vs Llama-3 | 161 / 308 | 61.3 | -- | -- |
| Random split | 540 / 540 | 0.18 | -- | -- |
| Within-subject avg | varies | 38.1 | -- | -- |

**Ground Truth Mismatch**:
- Direct comparison (9,229 annotated items):
  * DIF-C rates: 30.7% among contaminated, 31.8% among clean
  * φ = 0.012, χ² = 1.28 (p = 0.258), OR = 1.05 [0.96, 1.15]
  * Jaccard index: 0.206
  * Input-only: 0.986; Input-and-label: 0.960
  * Semi-synthetic dose-response: ΔTPR = +0.508 at p = 0.5

**Structural Analysis**:
- Matched-ability quintiles: No reduction below 31%
- IRT θ-conditioning (r = 0.9986): C% = 0.312
- Within-subject DIF: C% = 38.1% (elevated by local dependence)
- Local dependence within-subject: 11.3% of pairs exceed |Q3| > 0.20 vs. 2.2% cross-subject
- Logistic regression DIF: 92.1% concordance with MH; 24.8% additional non-uniform DIF
- Graduated de-duplication: K=10: 22.7%, K=20: 29.1% (confounded with power reduction)
- Ability-matched analysis: 28.3% (Llama-2 vs. 3), 28.9% (temporal)
- Consistent matched values (~28--29%) across different comparisons suggest genuine item-level DIF

**Semi-Synthetic Validation**:
- Cross-subject matching: ΔFPR = 0.000 across all 5 MMLU subjects
- 4/5 subjects with ΔTPR > 0.3 at p = 0.5
- Within-subject matching: FPR inflation of +0.186 on average
- Multi-subject injection robustness:
  * k ≤ 5 (≤9% domains): ΔFPR < 0.007
  * k = 10 (18%): ΔFPR = 0.026--0.069
  * Marks boundary of matching variable integrity

**Downstream Impact**:
- Stable-item rank correlation: ρ = 0.997, τ = 0.958
- Flip rate: ≤ 2.8% across benchmarks
- DIF-flagged items concentrate discriminative signal (z = -8 to -49 vs. random removal)
- Model family shifts:
  * Llama-3 derivatives (n = 315): +53 median rank positions
  * Mistral derivatives (n = 619): -35 median rank positions
- Top 200 displaced models (3.8% by |Δrank|):
  * 33.6% of pairwise rankings reverse
  * Example: Qwen1.5-14B-Chat: 610-position lead → 501-position deficit
- Removing C-flagged items: 96.2-position cohort gap (40× random removal, p < 0.001)

**Cross-Benchmark Validation**:
**Table 2 (6 Benchmarks)**:
| Benchmark | Items | C% | ρ | τ | Flip% | Random C% | Ratio |
|-----------|-------|-------|--------|--------|---------|----------|----------|
| MMLU | 12,508 | 31.3 | 0.9965 | 0.9600 | 2.00 | 0.18 | 174× |
| WinoGrande | 1,267 | 30.3 | 0.9943 | 0.9432 | 2.84 | 0.32 | 95× |
| TruthfulQA | 817 | 29.7 | 0.9971 | 0.9586 | 2.07 | 0.37 | 80× |
| ARC | 1,172 | 26.9 | 0.9962 | 0.9538 | 2.31 | 0.60 | 45× |
| GSM8K | 1,319 | 18.9 | 0.9993 | 0.9843 | 0.78 | 0.30 | 63× |
| HellaSwag | 10,042 | 17.9 | 0.9986 | 0.9722 | 1.39 | 0.28 | 64× |

**GSM8K Details**:
- Semi-synthetic injection: ΔTPR = +0.514 at p = 0.5
- GSM1K correlation: r = -0.478 (p = 0.005) (exploratory, N = 33)
- 6-month window: MMLU C% = 34.35% (2023-H2 vs. 2024-H1)

## DISCUSSION

**Temporal DIF Decomposition**:
- Impact (ability differences): ~2.4 pp
- DIF (item-level): ~28--29% floor
- Item-specificity: 92.4%
- Attribution: Underdetermined without training data (contamination, capability evolution, methodology shifts)

**Ground Truth Critique**:
- Web-overlap measures global exposure; DIF measures differential functioning
- Semi-synthetic dose-response confirms detection works when present
- Disconnect is in ground truth, not method

**Recommended DIF Audit Protocol** (whenever ≥500 models accumulate):
1. **Monitor** (C% < 15%): Report C% in release notes
2. **Flag** (15--25%): Report stable-item rankings as sensitivity analysis
3. **Act** (C% ≥ 25%): Review flagged items; report stable-item rankings as primary metric; use DIF pre-screening for equating anchors

**Item Property Predictability**:
- AUROC = 0.60 (logistic regression) and 0.599 (LightGBM)
- Conclusion: Post-hoc monitoring needed, not pre-screening

## LIMITATIONS

**Methodological Scope**:
- MH-DIF detects only uniform DIF (24.8% additional non-uniform DIF via logistic regression)
- DIF indicates *that* items differ, not *why*
- Semi-synthetic uses binary response flipping (worst-case pattern)
- Moderate ΔTPR = +0.508 at p = 0.5 reflects sensitivity to severe differential behavior

**Examinee Non-Independence**:
- Assumption violated by LLMs sharing base models/training data
- Empirical mitigations: Permutation FPR inflation < 0.001 pp; graduated de-duplication K=20: C% = 29.1%
- Cluster bootstrap family-level (29 families, 1,882 models, B = 1,000): 95% CI [26.7%, 53.2%] (3.1× wider than model-level)
- Lower bound still far exceeds random-split baseline (0.18%)

**Matching Boundary**:
- Cross-subject matching assumes contamination affects minority of domains
- Breaks down when contamination spans > 10 subjects (> 18% MMLU): ΔFPR = 0.026--0.069
- GSM1K analysis: N = 33, limited power (exploratory)

**Generalizability**:
- Only open-ended generation, coding, partial-credit benchmarks untested
- Temporal cohorts by calendar year (coarse grouping)
- Models from Open LLM Leaderboard only (closed-source generalizability unknown)

## APPENDIX

**Power Sensitivity to Item Discrimination** (Table at app:power_sensitivity):
| a | TPR | 95% CI | FPR |
|---|-----|--------|-----|
| 0.5 | 0.398 | [0.20, 0.60] | 0.033 |
| 0.8 | 0.683 | [0.45, 0.90] | 0.036 |
| 1.0 | 0.808 | [0.60, 0.95] | 0.038 |
| 1.2 (≈ā) | 0.874 | [0.70, 1.00] | 0.038 |
| 1.5 | 0.930 | [0.80, 1.00] | 0.038 |
| 2.0 | 0.949 | [0.80, 1.00] | 0.037 |

**Diagnostics**:
- Yen's Q3 threshold: |Q3| > 0.20
- Spearman correlation: Subject-level C% vs. accuracy improvement
- Logistic regression: DIF-C classification prediction with domain-level accuracy controls

**Multiple Testing**:
- ETS C dual threshold provides implicit control
- Benjamini-Hochberg FDR at q = 0.05: Removes only 3 items
- Random-split provides empirical FPR estimate

**Threshold Sensitivity**:
- |ΔMH| ∈ {1.0, 1.5, 2.0, 2.5}
- Standard threshold: |ΔMH| ≥ 1.5 (ETS C)

**IRT Fit**:
- MMLU shows poor fit to unidimensional 2PL (expected for 57-subject benchmark)
- Does not affect MH-DIF validity

**Architecture Homogeneity**:
- 99.98% decoder-only (5,226 of 5,227 models)
- Single encoder-decoder model excluded; results identical

**Logistic Regression Specifications**:
- Simpson's paradox: DIF-C ~ domain accuracy + difficulty + discrimination + interaction
- Non-uniform DIF: Group × ability interaction (p < 0.05)

**Structural Details**:
- Matched-ability quintiles: Enrichment 0.94--1.04
- IRT θ-conditioning with 20 strata: r(θ, total score) = 0.9986, C% = 0.312
- Within-subject DIF (5 subjects): Mean C% = 38.1%
- Yen's Q3: 11.3% within-subject pairs > 0.20; 2.2% cross-subject (5× ratio, p = 2.3 × 10⁻⁹)

**Multi-Subject Injection** (Table):
| k | ΔFPR | ΔTPR |
|---|-------|-------|
| 1 | 0.000±0.000 | 0.371±0.048 |
| 3 | 0.003±0.002 | 0.385±0.031 |
| 5 | 0.007±0.003 | 0.392±0.027 |
| 10 | 0.047±0.022 | 0.401±0.024 |
| 20 | 0.069±0.018 | 0.410±0.020 |

**Leave-One-Family-Out** (LOFO):
| Family | N removed | Cohort share | C% (LOFO) |
|--------|-----------|--------------|----------|
| Full sample | -- | -- | 31.32 |
| Mistral | 547 | 51% ref | 22.47 |
| Llama-3 | 315 | 39% focal | 24.06 |
| Mixtral | 120 | 15% focal | 34.26 |
| Llama-2 | 161 | 15% ref | 31.48 |
| Solar | 91 | 11% focal | 31.01 |

**Cross-Benchmark (MMLU vs GSM8K)**:
| Metric | MMLU | GSM8K |
|--------|------|-------|
| Items | 12,508 | 1,319 |
| Models | 5,227 | 6,702 |
| Temporal C% | 31.3% | 18.9% |
| Sanity C% | 0.18% | 0.3% |
| ΔTPR (p=0.7, standard) | -- | +0.818±0.006 |
| ΔTPR (p=0.5, external) | +0.508±0.027 | +0.514±0.028 |

**Item-Property Predictive Analysis**:
- 17 leak-free features (logistic regression + LightGBM)
- Cross-validation: Subject-stratified, 5-fold
- AUROC: 0.603 ± 0.020 (LR), 0.599 ± 0.026 (LightGBM)
- Web-overlap contribution: SHAP < 0.015
- Conclusion: Emergent cohort-item interactions, not fixed defects

This comprehensive extraction captures all numerical findings, statistical tests, confidence intervals, sample sizes, and claims essential for a thorough peer review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efc06e5b-71ed-4586-abd5-ddb7946d00dd",
  "isSidechain": true,
  "agentId": "ab47b7a11c46d59e1",
  "requestId": "req_011CbHSTpQV3r1E4vCptKgex",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "02ffc55d-ccef-4928-bc4f-750e5508a19b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "1e821804-de94-461a-97da-c43c5977bbe1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HEiAXRUtD1jedsj83X4etd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 17685,
      "cache_read_input_tokens": 18088,
      "output_tokens": 5767,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17685
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 5767,
          "cache_read_input_tokens": 18088,
          "cache_creation_input_tokens": 17685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17685,
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
