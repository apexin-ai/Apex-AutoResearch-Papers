# Research conversation: You are Reviewer R2 for an ACL ARR submission. Your focus is **Novelty and Related Work**. ## Scoring System ACL ARR 1-5

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a0969a4e4a19ae3ba.jsonl`
- **Structured JSON:** [`f969820c4edcd4c442d2.json`](../../sessions/f9/f969820c4edcd4c442d2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

27 recorded events

### User

_source line 1 · 2026-05-21T06:55:22.971Z_

You are Reviewer R2 for an ACL ARR submission. Your focus is **Novelty and Related Work**.

## Scoring System
ACL ARR 1-5 scale with three dimensions:
- **Soundness** (1-5): 5=Excellent (one of the most thorough), 4=Strong (sufficient support for all claims), 3=Acceptable (sufficient for main claims), 2=Borderline (some claims not well-supported), 1=Poor (major flaws)
- **Excitement** (1-5): 5=Transformative, 4=Exciting, 3=Interesting, 2=Marginally interesting, 1=Not exciting
- **Overall** (1-5): 5=Strong accept (top 2.5%), 4=Accept, 3=Borderline, 2=Reject, 1=Strong reject

## Paper Details

**Title:** "31% of MMLU Items Are Functionally Unstable: Psychometric DIF Analysis of 5,227 Models Reveals Temporal Benchmark Fragility"

**Core idea:** Apply an established psychometric method (Mantel-Haenszel DIF analysis) at unprecedented scale (5,227 LLM models × 12,508 MMLU items) to characterize temporal benchmark instability. The paper argues this is an empirical discovery paper, not an algorithmic novelty paper.

**4 Contributions:**
1. **Empirical discovery** — First large-scale DIF analysis on LLM benchmark. 31.3% of MMLU items show large temporal DIF between 2023 and 2024-H1 model cohorts. Robust across thresholds, BH correction, model family de-duplication. Item-level decomposition: domain capability improvement explains ≤7.6% of instability. Architecture: 99.98% decoder-only.

2. **Ground truth meta-critique** — Web-overlap contamination labels (Li et al. 2024) measure global exposure, not differential contamination. DIF enrichment against these labels ≈1.0 (no enrichment), which the paper reframes: this is *expected* because web-overlap ≠ differential item functioning. Implication: all existing item-level contamination detectors (Min-K%, ConStat, n-gram overlap) validate against labels that fundamentally cannot capture differential effects.

3. **Semi-synthetic validation framework** — Inject known differential contamination into real response matrices, measure ΔTPR and ΔFPR. Cross-subject matching eliminates matching variable contamination (ΔFPR=0.000). Portable to GSM8K (ΔTPR=+0.818).

4. **DIF as diagnostic lens** — Removing all 3,918 DIF-C items yields ρ≈0.997 (massive redundancy). Circularity ablation: DIF removal z=-9.5 vs accuracy-gap z=-157 (16× less disruptive despite 62.6% item overlap). Item characterization: difficulty×direction ρ=-0.597 (hard items favor newer models, easy items favor older). GSM1K cross-validation: r=-0.478, p=0.005, N=33.

**Related Work Coverage (§2):**
- Benchmark contamination detection: Min-K% (Shi et al. 2024), ConStat (Dekoninck et al. 2024), n-gram overlap (Li et al. 2024)
- Benchmark integrity: Growing Pains (Dutta et al. 2024), LiveBench (White et al. 2024)
- Psychometrics/DIF: Holland & Thayer 1988, Mantel & Haenszel 1959, Zieky 1993, Tutz & Berger 2016 (IFT), Swaminathan & Rogers 1990 (logistic regression DIF)
- IRT for LLM: Polo et al. 2024 (tinyBenchmarks), Vania et al. 2021

**Key framing decisions:**
- "instability ≠ invalidity" — DIF flags items whose functioning changed, not broken items
- Paper pivoted from "contamination detection" to "benchmark characterization"
- Claims no algorithmic novelty; novelty is "old psychometric method × unprecedented LLM benchmark scale = genuine empirical discovery"

**References (10 total):**
Dekoninck et al. 2024 (ConStat, NeurIPS), Dutta et al. 2024 (Growing Pains, arXiv), Eisenstein et al. 2025 (METABENCH, arXiv), Holland & Thayer 1988, Li et al. 2024 (AAAI), Mantel & Haenszel 1959, Polo et al. 2024 (tinyBenchmarks, ICML), Shi et al. 2024 (Min-K%, ICLR), Swaminathan & Rogers 1990, Tutz & Berger 2016, Vania et al. 2021 (ACL), White et al. 2024 (LiveBench, arXiv), Zieky 1993

**Experiment plan coverage (from review_context.yaml):**
Paper executes 12 of 18 imagined experiments. Dropped experiments (ConStat baseline, DVD, ensemble fusion) are justified by the pivot from detection to characterization. Killed experiments (bifactor IRT, item generation) are honestly reported as negative results. The paper covers more than minimum but some potentially interesting experiments (direct comparison with ConStat/DVD) are absent.

## Your Task

Write a detailed review focusing on:
1. **Novelty assessment** — Is "established method × unprecedented scale" sufficient novelty for ACL? Is this genuinely new empirical knowledge?
2. **Related work completeness** — Are there missing references? Is the positioning fair?
3. **Contribution significance** — Will this change how people think about benchmark evaluation?
4. **Meta-critique strength** — Is the "web-overlap ≠ differential contamination" argument convincing?
5. **Framing quality** — Does "instability ≠ invalidity" hold up? Is the narrative coherent?
6. **Missing comparisons** — Should the paper include direct ConStat/DVD comparisons?

Structure your review as:
### Summary (2-3 sentences)
### Strengths (bulleted)
### Weaknesses (bulleted, with severity: Major/Minor)
### Questions for Authors
### Missing References
### Scores (Soundness, Excitement, Overall)
### Confidence (1-5)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9f953575-95eb-4981-bd3f-8e47b7d03776",
  "agentId": "a0969a4e4a19ae3ba",
  "type": "user",
  "uuid": "e562432a-cf47-4a3d-8215-d6dc2c5c29e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T06:55:22.975Z_

```json
{
  "parentUuid": "e562432a-cf47-4a3d-8215-d6dc2c5c29e4",
  "isSidechain": true,
  "agentId": "a0969a4e4a19ae3ba",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "1a6e1a7c-5cbc-4f76-bc14-8ee7fb888c6c",
  "timestamp": "2026-05-21T06:55:22.975Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-21T06:55:25.317Z_



I'll start by reading the paper sections to provide a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a6e1a7c-5cbc-4f76-bc14-8ee7fb888c6c",
  "isSidechain": true,
  "agentId": "a0969a4e4a19ae3ba",
  "requestId": "req_011CbFGyXe5ubC8YjnhehdMq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67035d76-9fa6-4970-a724-3c4fcdb6e7a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HNs6efQ6ZiiuaCVBcoFctd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7513,
      "cache_read_input_tokens": 8787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7513,
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

_source line 4 · 2026-05-21T06:55:27.396Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AxWRY9JjSsnL5ZTaWUemP1`</summary>

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
  "parentUuid": "67035d76-9fa6-4970-a724-3c4fcdb6e7a8",
  "isSidechain": true,
  "agentId": "a0969a4e4a19ae3ba",
  "requestId": "req_011CbFGyXe5ubC8YjnhehdMq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d81e63df-243e-4815-93e6-57fcef730ba4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HNs6efQ6ZiiuaCVBcoFctd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7513,
      "cache_read_input_tokens": 8787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7513,
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

_source line 5 · 2026-05-21T06:55:27.403Z_

<details><summary>↩ Tool result · `toolu_01AxWRY9JjSsnL5ZTaWUemP1`</summary>

```text
1	\begin{abstract}
2	LLM benchmark scores are routinely compared across model generations, yet the assumption that individual items measure the same construct over time is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (DIF) analysis with ETS severity classification to the METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items), and find that 31\% of items exhibit large DIF (ETS Category~C) between 2023 and 2024 model cohorts. This instability does not threaten benchmark validity: Spearman rank correlation between full and stable-item rankings is $\rho \approx 0.997$. Rather, it reveals which capability dimensions shift across model generations. Item-level decomposition shows that domain accuracy improvement explains only 2.4 percentage points (7.6\%) of the instability; 92.4\% is item-specific. We expose a validation methodology gap in the contamination detection literature: web-overlap labels measure global exposure, not differential functioning, and the enrichment between DIF flags and these labels is 0.96 (chance level). A semi-synthetic injection framework with cross-subject matching achieves $\Delta\mathrm{FPR} = 0.000$ while preserving detection power ($\Delta\mathrm{TPR} = {+}0.508$ at exploitation rate $p = 0.5$); cross-benchmark replication on GSM8K confirms generality ($\Delta\mathrm{TPR} = {+}0.514$). DIF-flagged items concentrate cross-generational discriminative information ($z = -8$ to $-49\sigma$ vs.\ random removal); an exploratory analysis ($N = 33$) finds they anti-correlate with the GSM1K contamination gap ($r = -0.478$, $p = 0.005$), suggesting that DIF captures genuine capability change rather than memorization. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d81e63df-243e-4815-93e6-57fcef730ba4",
  "isSidechain": true,
  "promptId": "9f953575-95eb-4981-bd3f-8e47b7d03776",
  "agentId": "a0969a4e4a19ae3ba",
  "type": "user",
  "uuid": "883c8a1a-48e0-4040-b7f8-14fd08400646",
  "sourceToolAssistantUUID": "d81e63df-243e-4815-93e6-57fcef730ba4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T06:55:28.221Z_

<details open><summary>🔧 Tool call — Read · `toolu_014HAYogBjoHoMPvvizcayky`</summary>

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
  "parentUuid": "883c8a1a-48e0-4040-b7f8-14fd08400646",
  "isSidechain": true,
  "agentId": "a0969a4e4a19ae3ba",
  "requestId": "req_011CbFGyXe5ubC8YjnhehdMq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a555df0-2cb1-49c2-94c1-8036956620df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HNs6efQ6ZiiuaCVBcoFctd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7513,
      "cache_read_input_tokens": 8787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7513,
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

_source line 7 · 2026-05-21T06:55:28.227Z_

<details><summary>↩ Tool result · `toolu_014HAYogBjoHoMPvvizcayky`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark replication on GSM8K appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	A power analysis using empirical MMLU IRT parameters confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$. Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold.
10	
11	\subsection{Temporal Comparability: 31\% Item Instability}
12	\label{sec:temporal}
13	
14	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$). Benjamini-Hochberg FDR correction at $q = 0.05$ removes only 3 items (31.32\% $\to$ 31.30\%), because the dual ETS threshold on effect size and significance already provides implicit multiple-testing protection.
15	
16	Three controls confirm this reflects genuine temporal change. A random split of the 2023 cohort yields only 0.18\% ETS~C items (sampling noise), and an ability-quintile comparison within the same temporal cohort yields 2.9\% (ability differences alone). A within-family comparison (Llama-2 vs.\ Llama-3) produces 61.3\% ETS~C items, elevated by large ability gaps that confound the DIF signal~\citep{holland1988mh}. The contrast between 2.9\% (ability-controlled) and 61.3\% (ability-confounded) brackets the temporal rate of 31.3\%.
17	
18	Across all 57 MMLU subjects, C\% ranges from 20.7\% (computer security) to 48.4\% (business ethics) with unweighted mean $\approx 30\%$. Within-subject matching on 5 representative subjects yields a mean of 38.1\% (range: 31--45\%), reported in \Cref{tab:temporal_landscape} as a robustness check for the matching protocol. Despite an ecological correlation of $\rho = 0.307$ ($p = 0.02$) between subject-level C\% and accuracy improvement, item-level logistic regression reveals that domain accuracy improvement explains only 2.4 percentage points of 31.3\% C\% (pseudo $R^2 = 0.0007$; counterfactual C\% $= 29.0\%$). Thus 92.4\% of the instability reflects item-specific changes unrelated to aggregate domain-level gains. The qualitative conclusion is robust across ETS thresholds: C\% $= 48.9\%$ at $|\Delta_{\mathrm{MH}}| \geq 1.0$, $18.3\%$ at $\geq 2.0$, and $10.2\%$ at $\geq 2.5$. \Cref{tab:temporal_landscape} summarizes the DIF landscape across all cohort comparisons.
19	
20	\begin{table}[t]
21	\centering
22	\caption{DIF landscape across cohort definitions. ETS~C denotes the percentage of items with $|\Delta_{\mathrm{MH}}| \geq 1.5$. FPR is measured against Li et al.\ web-overlap labels on the ``clean'' (non-overlapping) subset. Enrichment is the ratio of observed to expected overlap between DIF flags and web-overlap labels.}
23	\label{tab:temporal_landscape}
24	\small
25	\begin{tabular}{lcccc}
26	\toprule
27	Cohort Definition & $N_{\mathrm{ref}}$ / $N_{\mathrm{focal}}$ & ETS~C (\%) & FPR (Li clean) & Enrichment \\
28	\midrule
29	Temporal (2023 vs.\ 2024) & 1,080 / 807 & 31.3 & 0.318 & 0.96 \\
30	Ability quintile (Q1--2 vs.\ Q4--5) & ${\sim}$2,600 / ${\sim}$2,600 & 2.9 & 0.027 & 1.19 \\
31	Within-family (Llama-2 vs.\ 3) & 161 / 308 & 61.3 & -- & -- \\
32	Random split (sanity) & 540 / 540 & 0.18 & -- & -- \\
33	Within-subject (avg, 5 subjects) & \textit{varies} & 38.1 & -- & -- \\
34	\bottomrule
35	\end{tabular}
36	\end{table}
37	
38	\subsection{Ground Truth Mismatch}
39	\label{sec:groundtruth}
40	
41	The enrichment ratio of DIF flags against the web-overlap labels of \citet{li2024contamination} is 0.96 (\Cref{tab:temporal_landscape}), indistinguishable from chance. This null result does not indicate detection failure: semi-synthetic injection produces a clear dose-response ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$, ${+}0.674$ at $p = 1.0$; \Cref{fig:dose_response}). The disconnect arises because web-overlap labels measure \emph{global exposure} (whether an item exists in training corpora), while DIF measures \emph{differential functioning} (whether an item's relationship to ability changes across cohorts). An item can be globally contaminated yet function identically if all cohorts have comparable access. The Li et al.\ labels are the wrong ground truth for a differential method: the near-chance enrichment is expected, not evidence of failure.
42	
43	\begin{figure}[t]
44	\centering
45	\includegraphics[width=\columnwidth]{fig_2_dose_response.pdf}
46	\caption{Semi-synthetic dose-response for DIF detection on MMLU. $\Delta\mathrm{TPR}$ increases monotonically with exploitation rate $p$, confirming that MH-DIF detects differential contamination when present. Baseline (no injection) produces $\Delta\mathrm{TPR} \approx 0$.}
47	\label{fig:dose_response}
48	\end{figure}
49	
50	\subsection{Structural Analysis}
51	\label{sec:structural}
52	
53	Three progressively refined approaches (matched-ability quintiles, IRT $\theta$-conditioning, within-subject DIF) all fail to reduce the temporal FPR below 0.31. $\theta$-conditioning achieves $r(\theta, \mathrm{total\ score}) = 0.9986$ yet FPR $= 0.312$, and within-subject C\% $= 38.1\%$ exceeds the 25\% bifactor viability threshold. Yen's Q3 diagnostic reveals mild local dependence within subjects (11.3\% of pairs exceed $|Q3| > 0.20$, vs.\ 2.2\% cross-subject; $p = 2.3 \times 10^{-9}$), but cross-subject matching addresses this bias and temporal C\% persists. \Cref{app:structural} reports full results. As a further robustness check, logistic regression DIF on 9 MMLU subjects (1,787 items) confirms 92.1\% concordance between MH ETS~C and LR uniform DIF classifications and reveals additional non-uniform DIF (24.8\% of items at $|\beta_{\mathrm{interaction}}| \geq 0.5$) that MH is structurally unable to detect. The 31\% uniform DIF estimate is therefore conservative. A model independence sensitivity analysis addresses the concern that fine-tunes, merges, and quantizations inflate C\%: graduated de-duplication (limiting each family to $K$ models) yields C\% at or below size-matched random controls ($K{=}10$: 22.7\% vs.\ 26.8\%; $K{=}20$: 29.1\% vs.\ 30.9\%), confirming that family structure does not inflate the 31.3\% estimate.
54	
55	\subsection{Semi-Synthetic Framework Validation}
56	\label{sec:semisynthetic}
57	
58	The critical methodological finding is that the choice of matching strategy determines validity. Cross-subject matching computes the conditioning variable from subjects \emph{other than} the one being tested, achieving $\Delta\mathrm{FPR} = 0.000$ across all five MMLU subjects while four of five produce $\Delta\mathrm{TPR} > 0.3$ at $p = 0.5$. Within-subject matching inflates FPR by ${+}0.186$ on average because the matching variable absorbs part of the injection signal. We adopt cross-subject matching as the standard protocol (\Cref{app:fig_matching}).
59	
60	\subsection{Downstream Impact}
61	\label{sec:downstream}
62	
63	Spearman correlation between full and stable-item rankings is $\rho \approx 0.997$: aggregate model ordering is preserved despite 31\% item instability. DIF-flagged items nonetheless carry more discriminative signal than average ($z = -8$ to $-49$ vs.\ random removal across 21 conditions), though a circularity ablation shows DIF-based removal is the \emph{least} disruptive among non-random strategies (Jaccard overlap with high-discrimination items is only 0.12). Individual model families show distinctive DIF profiles: Phi-3 and Llama-3 gain ${+}700$ to ${+}850$ rank positions under stable-item evaluation, while Mistral-based merges lose $-400$ to $-587$ positions (\Cref{app:fig_downstream}). The DIF instability pattern extends beyond MMLU; \Cref{sec:gsm8k} presents a full replication on GSM8K.
64	
65	\subsection{Cross-Benchmark Validation: GSM8K}
66	\label{sec:gsm8k}
67	
68	Replication on GSM8K (1,319 items $\times$ 6,702 models) yields temporal C\% $= 18.9\%$ (sanity check: 0.3\%), with semi-synthetic $\Delta\mathrm{TPR} = {+}0.514$ at $p = 0.5$ under external matching (\Cref{app:gsm8k_details}). As an exploratory analysis, the GSM1K held-out set~\citep{zhang2024gsm1k} provides independent contamination validation: for $N = 33$ models, the correlation between contamination gap and DIF ranking advantage is $r = -0.478$ ($p = 0.005$; partial $r = -0.385$, $p = 0.027$ after controlling for accuracy). This \emph{negative} correlation contradicts the hypothesis that DIF items benefit contaminated models, and instead suggests that DIF captures genuine capability change distinct from memorization (\Cref{fig:gsm1k}). The result is suggestive at $N = 33$ and warrants replication.
69	
70	\begin{figure}[t]
71	\centering
72	\includegraphics[width=\columnwidth]{fig_5_gsm1k_dif_correlation.pdf}
73	\caption{GSM1K contamination gap vs.\ DIF ranking advantage ($N = 33$). The negative correlation ($r = -0.478$, $p = 0.005$) indicates that models with larger contamination gaps benefit less from DIF-flagged items.}
74	\label{fig:gsm1k}
75	\end{figure}
76	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a555df0-2cb1-49c2-94c1-8036956620df",
  "isSidechain": true,
  "promptId": "9f953575-95eb-4981-bd3f-8e47b7d03776",
  "agentId": "a0969a4e4a19ae3ba",
  "type": "user",
  "uuid": "d1dcc207-2c75-4be8-8c67-fdf173a6fe91",
  "sourceToolAssistantUUID": "4a555df0-2cb1-49c2-94c1-8036956620df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T06:55:28.409Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SzPm5jLGaCfttmvSwvsaYM`</summary>

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
  "parentUuid": "d1dcc207-2c75-4be8-8c67-fdf173a6fe91",
  "isSidechain": true,
  "agentId": "a0969a4e4a19ae3ba",
  "requestId": "req_011CbFGyXe5ubC8YjnhehdMq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9878c1be-0001-48a5-919a-4f849713b2f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HNs6efQ6ZiiuaCVBcoFctd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7513,
      "cache_read_input_tokens": 8787,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7513
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 259,
          "cache_read_input_tokens": 8787,
          "cache_creation_input_tokens": 7513,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7513,
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

_source line 9 · 2026-05-21T06:55:28.420Z_

<details><summary>↩ Tool result · `toolu_01SzPm5jLGaCfttmvSwvsaYM`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Implications for Benchmark Temporal Comparability}
5	\label{sec:disc_temporal}
6	
7	The 31\% ETS~C instability rate is robust across thresholds (10--49\% at $|\Delta_{\mathrm{MH}}| \in [2.5, 1.0]$) and confirmed by three structural controls (\Cref{sec:structural}). Domain-level accuracy improvement explains only 2.4 percentage points of 31.3\% C\% (pseudo $R^2 = 0.0007$); 92.4\% of the instability is item-specific and unrelated to aggregate capability gains. This instability does not invalidate MMLU as a ranking instrument ($\rho \approx 0.997$ between full and stable-item rankings) but signals that item-level measurement properties are drifting across model generations. Benchmark designers should monitor DIF as a quality diagnostic: an item pool where C\% grows over successive cohorts indicates measurement drift even when rank ordering remains intact.
8	
9	\subsection{Ground Truth Meta-Critique}
10	\label{sec:disc_groundtruth}
11	
12	The near-chance enrichment (0.96) between DIF flags and web-overlap labels exposes a gap that extends beyond our analysis: all prior work validating item-level contamination detectors against web-overlap or $n$-gram labels conflates global exposure with differential functioning. Most MMLU items appear in web text, so web-overlap labels identify a condition shared by nearly all items rather than one that differentiates model cohorts. The enrichment of $\approx 1.0$ is the expected outcome when a differential method is evaluated against a global-exposure reference, not evidence of failure. The field needs validation methodologies that match the detection granularity: item-level differential detectors require item-level differential ground truth.
13	
14	\subsection{DIF as Diagnostic Lens}
15	\label{sec:disc_diagnostic}
16	
17	The GSM1K correlation ($r = -0.478$, $p = 0.005$, $N = 33$; \Cref{sec:gsm8k}) provides exploratory evidence that DIF-flagged items capture behavioral change distinct from memorization. Models with larger contamination gaps benefit \emph{less} from DIF-C items. Of the 249 DIF-C items on GSM8K, 171 favor the reference (2023) cohort ($\alpha_{\mathrm{MH}} > 1$). Partial correlation ($r = -0.385$, $p = 0.027$) after controlling for accuracy confirms the effect is not an artifact of general model quality. Caveats include a wide confidence interval (95\% CI $= [-0.71, -0.16]$) and limited sample size.
18	
19	Item characterization reinforces this: DIF-C items are harder ($d = -0.247$) and more discriminating ($d = 0.230$), distributed uniformly across subjects ($\chi^2$ $p = 0.32$). A difficulty $\times$ direction interaction ($\rho = -0.597$, $p < 0.001$) shows capability gains concentrate on hard items (88.7\% focal-favoring in hardest decile) while easy items erode (96.2\% reference-favoring in easiest decile).
20	
21	Three structural constraints limit DIF applicability in LLM benchmarks: (1) MMLU's multi-domain structure produces mild local dependence that elevates within-subject DIF rates (\Cref{sec:structural}); (2) reliable detection requires $N \geq 80$ per cohort and $|\Delta_{\mathrm{MH}}| \geq 1.4$; and (3) ability differences between temporal cohorts confound the DIF signal (within-family C\% $= 61.3\%$). A fourth limitation is that MH detects only uniform DIF; logistic regression analysis reveals additional non-uniform DIF (24.8\% at $|\beta_{\mathrm{interaction}}| \geq 0.5$; \Cref{sec:structural}), making the 31\% estimate conservative rather than exhaustive. Key limitations include the inability to distinguish contamination from legitimate capability change and limited benchmark scope (MMLU + GSM8K). DIF should be understood as a diagnostic lens for what changed across model generations, not a quality filter; LLM benchmarks need psychometric monitoring alongside score reporting.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9878c1be-0001-48a5-919a-4f849713b2f3",
  "isSidechain": true,
  "promptId": "9f953575-95eb-4981-bd3f-8e47b7d03776",
  "agentId": "a0969a4e4a19ae3ba",
  "type": "user",
  "uuid": "ad7ae041-c540-4dc6-9731-dc4f225864f7",
  "sourceToolAssistantUUID": "9878c1be-0001-48a5-919a-4f849713b2f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T06:55:32.643Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01XeMuMUnvndgCsX1oFUWAPq`</summary>

```json
{
  "pattern": "paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad7ae041-c540-4dc6-9731-dc4f225864f7",
  "isSidechain": true,
  "agentId": "a0969a4e4a19ae3ba",
  "requestId": "req_011CbFGywBgq1qyQXGZxukhp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8788625a-5dbe-4eb1-b6a0-6270857fd9eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122dvEieAs7hRNoVRxkXdCx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5958,
      "cache_read_input_tokens": 16300,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5958
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 16300,
          "cache_creation_input_tokens": 5958,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5958,
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

_source line 11 · 2026-05-21T06:55:32.657Z_

<details><summary>↩ Tool result · `toolu_01XeMuMUnvndgCsX1oFUWAPq`</summary>

```text
paper/sections/conclusion.tex
paper/sections/method.tex
paper/sections/related_work.tex
paper/sections/appendix.tex
paper/sections/introduction.tex
paper/sections/abstract.tex
paper/sections/experiments.tex
paper/sections/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8788625a-5dbe-4eb1-b6a0-6270857fd9eb",
  "isSidechain": true,
  "promptId": "9f953575-95eb-4981-bd3f-8e47b7d03776",
  "agentId": "a0969a4e4a19ae3ba",
  "type": "user",
  "uuid": "c1288d4d-8f59-40fc-8d2b-efa082c37d60",
  "sourceToolAssistantUUID": "8788625a-5dbe-4eb1-b6a0-6270857fd9eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T06:55:35.635Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MptomUb5P4kLK4NQePeduL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1288d4d-8f59-40fc-8d2b-efa082c37d60",
  "isSidechain": true,
  "agentId": "a0969a4e4a19ae3ba",
  "requestId": "req_011CbFGzFQJs27AbNwBtEcGf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "160c0db9-a370-4fda-ac4a-1edd88248221",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLesc71GGDhpZWDCGyoUr4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 182,
      "cache_read_input_tokens": 22258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 182,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 13 · 2026-05-21T06:55:35.643Z_

<details><summary>↩ Tool result · `toolu_01MptomUb5P4kLK4NQePeduL`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination Detection.}
5	A growing family of methods detects benchmark contamination through model behavior or training data analysis. Membership inference approaches estimate whether a model has seen specific items during training: Min-K\% \citep{shi2024mink} and Min-K\%++ \citep{zhang2024minkpp} use token-level log-likelihood statistics, while Time Travel \citep{golchin2024timetravel} probes models with temporal cues. Performance-based detectors identify contamination through statistical anomalies: ConStat \citep{dekoninck2024constat} tests performance gaps between original and perturbed items, DVD \citep{liang2026dvd} uses distributional verification, and Self-Critique \citep{tao2026selfcritique} employs model self-evaluation. \citet{balloccu2024leak} provide a broader taxonomy of leakage detection strategies. These methods share a common validation practice: they verify detection accuracy against web-overlap or n-gram labels \citep{li2024contamination} that classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure} (whether an item exists in training data) rather than \emph{differential item functioning} (whether an item behaves differently across model cohorts). This global-vs-differential distinction motivates our ground truth analysis (Claim~2, \Cref{sec:groundtruth}). \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, which further motivates behavioral approaches grounded in psychometric theory rather than NLL-based signals.
6	
7	\paragraph{IRT in LLM Evaluation.}
8	Item Response Theory (IRT) provides a principled framework for jointly analyzing test items and examinee ability, and its adoption in LLM evaluation has accelerated. \citet{lalor2019irt} introduced IRT to NLP by fitting item parameters to human and model response data; their analysis revealed that item difficulty and discrimination vary substantially across benchmark questions. \citet{vania2021irt} applied IRT to assess test set discriminability and found that many items in standard NLP benchmarks contribute little information about model differences. Recent extensions include PSN-IRT \citep{zhou2026psnirt}, which fits four-parameter logistic models to characterize benchmark quality at scale, and scalability coefficients \citep{hardy2026scalability} as lightweight item quality pre-filters. TinyBenchmarks \citep{maiapolo2024tinybenchmarks} uses IRT-based item selection to construct representative benchmark subsets that predict full-benchmark scores with far fewer items. ATLAS \citep{li2025atlas} and IRTNet \citep{chen2025irtnet} explore neural extensions of classical IRT for LLM ability estimation, and \citet{choi2026llmjudgeirt} apply IRT to calibrate LLM-as-judge evaluations.
9	
10	The closest concurrent work is Growing Pains \citep{habba2026growingpains}, which addresses score comparability across model generations through fixed-parameter calibration \citep[FPC;][]{kim2019fpc}. FPC anchors a common ability scale by fixing the item parameters of a shared anchor set, so that models calibrated at different times receive scores on the same metric. Their framework selects 100 anchor items with stable IRT parameters and calibrates new models against this fixed scale, which enables extensible evaluation without full re-calibration. Our work is complementary: Growing Pains assumes anchor item stability, while DIF analysis diagnoses which items violate this assumption. The combination suggests a path toward a monitored extensible evaluation system in which DIF flags anchor items whose functioning has degraded, triggering re-selection when the stable anchor set shrinks below a validity threshold.
11	
12	\paragraph{DIF Methodology and Measurement Invariance.}
13	The Mantel-Haenszel procedure for DIF detection was introduced by \citet{holland1988mh} and remains the most widely used method in educational testing due to its simplicity and well-characterized statistical properties \citep{clauser1998dif}. Alternative approaches include logistic regression DIF \citep{swaminathan1990logistic}, SIBTEST \citep{shealy1993sibtest}, Lord's $\chi^2$ test \citep{lord1980irt}, and the Raju area method \citep{raju1988area}; \citet{zumbo1999handbook} provides a comprehensive comparison. DIF analysis is a specific instance of measurement invariance testing \citep{meredith1993invariance, vandenberg2000invariance}, which examines whether a measurement instrument functions equivalently across populations. MIMIC models offer a latent-variable approach to the same problem \citep{muthen1985mimic, woods2009mimic}, and \citet{teresi2007dif} reviews DIF methods across applied domains. We do not modify the MH procedure; our contribution is the application context. The scale of this analysis (5,227 examinees across a 57-subject multidimensional ability space) exceeds typical educational testing applications, where \citet{belzak2020smallsample} note that DIF methods can behave differently at extreme sample sizes. The primary methodological challenge is the impact-versus-DIF confound: genuine ability differences between temporal cohorts can inflate DIF estimates. We address this through matched-ability quintile analysis, IRT $\theta$-conditioning, and a random-split control (\Cref{sec:temporal}).
14	
15	\paragraph{Benchmark Design and Concurrent Work.}
16	Our analysis psychometrically characterizes an existing benchmark (MMLU; \citealp{hendrycks2021mmlu}) rather than constructing a new one. Several concurrent efforts address benchmark limitations through design. Dynamic benchmarks such as Dynabench \citep{kiela2021dynabench} and LatestEval \citep{li2024latesteval} generate items adversarially or from recent sources to prevent memorization, and LiveBench \citep{white2025livebench} refreshes items monthly from contemporary material. Chatbot Arena \citep{chiang2024chatbot} and GAIA \citep{mialon2023gaia} sidestep static benchmarks entirely through pairwise human preference or real-world task completion. HELM \citep{liang2023helm} standardizes evaluation across tasks but does not address item-level stability. These approaches mitigate contamination by construction, yet none provides psychometric equating across versions: a model's score on LiveBench v3 is not directly comparable to its score on v1 without an anchoring mechanism such as that of \citet{habba2026growingpains}. METABENCH \citep{kipnis2024metabench} provides the large-scale response matrix (5,227 models $\times$ 12,508 items) that makes our analysis possible.
17	
18	\paragraph{LLM Evaluation Methodology.}
19	Broader surveys of LLM evaluation \citep{chang2024survey} identify benchmark saturation and lack of item-level transparency as systemic challenges. \citet{burnell2023rethink} argue that current practices treat benchmarks as monolithic scores, which obscures item-level variation in difficulty, discrimination, and stability. MMLU-Pro \citep{wang2024mmlupro} addresses saturation by increasing item difficulty, and \citet{ott2022benchmark} document how benchmark scores plateau as models improve. These diagnoses converge on a common gap: the absence of tools that operate at the item level rather than the benchmark level. Our DIF analysis fills this role by identifying which items within a benchmark have become unreliable for cross-generation comparison.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "160c0db9-a370-4fda-ac4a-1edd88248221",
  "isSidechain": true,
  "promptId": "9f953575-95eb-4981-bd3f-8e47b7d03776",
  "agentId": "a0969a4e4a19ae3ba",
  "type": "user",
  "uuid": "59f49090-4c16-46ca-badb-29993725c05f",
  "sourceToolAssistantUUID": "160c0db9-a370-4fda-ac4a-1edd88248221",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T06:55:35.953Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TpDyMiWaZhjWuqjzAM8pzb`</summary>

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
  "parentUuid": "59f49090-4c16-46ca-badb-29993725c05f",
  "isSidechain": true,
  "agentId": "a0969a4e4a19ae3ba",
  "requestId": "req_011CbFGzFQJs27AbNwBtEcGf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "436fa3e0-3e53-4eba-83c6-14679d859b47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLesc71GGDhpZWDCGyoUr4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 182,
      "cache_read_input_tokens": 22258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 182,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 15 · 2026-05-21T06:55:35.960Z_

<details><summary>↩ Tool result · `toolu_01TpDyMiWaZhjWuqjzAM8pzb`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench}, and find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. The instability persists across all 57 MMLU subjects (C\% range 21--48\%, unweighted mean $\approx 30\%$), and item-level regression shows that 92.4\% of this instability is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained. Crucially, this instability does not threaten benchmark validity: Spearman rank correlation between model rankings computed on all items versus stable-only items is $\rho \approx 0.997$. The instability is diagnostic, not destructive; it reveals which capability dimensions shift across model generations rather than rendering MMLU scores unreliable.
5	
6	A growing body of contamination detection research has produced sophisticated item-level methods, from membership inference approaches such as Min-K\%~\citep{shi2024mink} to performance-based detectors such as ConStat~\citep{dekoninck2024constat}, DVD~\citep{liang2026dvd}, and Self-Critique~\citep{tao2026selfcritique}. These methods validate detection accuracy primarily against web-overlap labels such as those of \citet{li2024contamination}, which classify benchmark items as contaminated based on verbatim or near-verbatim matches in publicly accessible training corpora. Such labels measure \emph{global exposure}: whether an item exists in the data ecosystem that all training pipelines can access. They do not measure \emph{differential item functioning}: whether an item behaves differently across model cohorts that may have had varying degrees of exposure or different training methodologies. \Cref{fig:global_vs_differential} illustrates the distinction. Most MMLU items are globally contaminated in the sense that they exist in web-accessible text, so all model cohorts encounter them and no differential signal arises. The items that function differentially are those where exposure or training methodology changed asymmetrically across cohorts. Validating differential detectors against global-exposure labels therefore conflates two phenomena, and the near-chance enrichment (0.96) between DIF flags and web-overlap labels is the expected outcome of this mismatch.
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=\columnwidth]{fig_1_global_vs_differential.pdf}
11	\caption{Global vs.\ differential contamination, illustrated via Item Characteristic Curves (ICCs). \textbf{Left}: global contamination produces no DIF; both cohorts encounter the item, and their ICCs overlap. \textbf{Right}: differential contamination produces DIF; the focal cohort's ICC shifts because only that cohort was disproportionately exposed during training. The enrichment ratio of $\approx 1.0$ between DIF flags and web-overlap labels is expected because most MMLU items fall into the left category.}
12	\label{fig:global_vs_differential}
13	\end{figure}
14	
15	We apply classical MH-DIF with ETS classification to the full METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items), to our knowledge, the largest-scale DIF analysis on LLM benchmarks. This psychometric approach complements concurrent work on anchor-item calibration for score comparability~\citep{habba2026growingpains} and addresses the fragility of existing contamination detectors under post-training perturbation~\citep{wang2026fragility}. Semi-synthetic injection experiments confirm that DIF detects differential contamination when present ($\Delta\mathrm{TPR} = {+}0.508$ at exploitation rate $p = 0.5$), and our cross-subject matching protocol eliminates false positive inflation ($\Delta\mathrm{FPR} = 0.000$). Three structural controls (matched-ability quintile analysis, IRT $\theta$-conditioning, and within-subject pre-checks) confirm that the 31\% temporal instability cannot be attributed to methodological artifacts, establishing it as a robust empirical finding about MMLU's measurement properties.
16	
17	MMLU's 12,508 items provide sufficient measurement redundancy that removing nearly a third does not alter rank order. DIF should therefore be understood as a diagnostic lens (which items changed and for which model families) rather than a quality filter (remove bad items to improve the benchmark). Despite aggregate ranking stability, DIF-flagged items concentrate discriminative signal that differentiates model generations: removing DIF items degrades ranking discriminability more than removing an equal number of random items ($z = -8$ to $-49\sigma$ across 21 conditions). Individual model families show distinctive DIF profiles: Phi-3 and Llama-3 gain ${+}700$ to ${+}850$ rank positions under stable-item evaluation, while Mistral-based merges lose $-400$ to $-587$ positions.
18	
19	We do not modify the MH-DIF procedure itself; the contributions are empirical, not algorithmic. Three layers of genuine novelty emerge: (a)~we discover that 31\% temporal instability is robust across thresholds and unrelated to capability improvement, the first large-scale characterization of item-level benchmark stability at 5,227 models; (b)~we expose a fundamental validation methodology gap in the contamination detection literature, showing that web-overlap labels are poorly suited to evaluate item-level differential detectors; and (c)~we provide a reusable semi-synthetic validation framework with cross-subject matching ($\Delta\mathrm{FPR} = 0.000$), confirmed on GSM8K with independent contamination validation through the GSM1K held-out set~\citep{zhang2024gsm1k}. We make the following contributions:
20	
21	\begin{enumerate}
22	\item \textbf{Benchmark temporal comparability} (Claim 1): 31\% of MMLU items are functionally unstable across model generations under ETS~C classification, with C\% ranging from 21\% to 48\% across all 57 subjects (mean $\approx 30\%$) and confirmed non-random by random-split control at 0.18\% (\Cref{sec:temporal}).
23	
24	\item \textbf{Ground truth meta-critique} (Claim 2): Web-overlap contamination labels~\citep{li2024contamination} do not provide appropriate ground truth for item-level differential detectors. The enrichment between DIF flags and web-overlap labels is 0.96 (chance level), exposing a validation methodology gap in the contamination detection literature (\Cref{sec:groundtruth}).
25	
26	\item \textbf{Semi-synthetic validation framework} (Claim 3): Controlled injection with cross-subject matching achieves $\Delta\mathrm{FPR} = 0.000$ while preserving detection power ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$); cross-benchmark replication on GSM8K confirms generality (\Cref{sec:semisynthetic,sec:gsm8k}).
27	
28	\item \textbf{DIF as diagnostic lens} (Claim 4): DIF-flagged items concentrate discriminative information ($z = -8$ to $-49\sigma$ vs.\ random removal) and anti-correlate with the GSM1K contamination gap ($r = -0.478$, suggestive at $N = 33$), indicating that DIF captures item-level behavioral change distinct from simple memorization (\Cref{sec:downstream,sec:gsm8k}).
29	\end{enumerate}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "436fa3e0-3e53-4eba-83c6-14679d859b47",
  "isSidechain": true,
  "promptId": "9f953575-95eb-4981-bd3f-8e47b7d03776",
  "agentId": "a0969a4e4a19ae3ba",
  "type": "user",
  "uuid": "5a93e3da-84ab-41f8-83ad-673c3f9b8e72",
  "sourceToolAssistantUUID": "436fa3e0-3e53-4eba-83c6-14679d859b47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T06:55:36.369Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EH7DAxfcMe1kqQQ6wAqeGD`</summary>

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
  "parentUuid": "5a93e3da-84ab-41f8-83ad-673c3f9b8e72",
  "isSidechain": true,
  "agentId": "a0969a4e4a19ae3ba",
  "requestId": "req_011CbFGzFQJs27AbNwBtEcGf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2cb4e95c-704c-477b-ad9d-717c8e5b1f8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLesc71GGDhpZWDCGyoUr4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 182,
      "cache_read_input_tokens": 22258,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 182
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 22258,
          "cache_creation_input_tokens": 182,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 182,
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

_source line 17 · 2026-05-21T06:55:36.374Z_

<details><summary>↩ Tool result · `toolu_01EH7DAxfcMe1kqQQ6wAqeGD`</summary>

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
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh} detects DIF by stratifying examinees into $K$ score bins based on total score (a proxy for $\theta$), where $K$ equals the number of distinct total scores observed in the combined sample, and computing a common odds ratio across strata. Within each stratum $k$, the responses of the reference group and the focal group form a $2 \times 2$ contingency table:
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
30	The Educational Testing Service (ETS) classifies DIF severity into three categories based on $|\Delta_{\mathrm{MH}}|$. Category~A (negligible) requires $|\Delta_{\mathrm{MH}}| < 1.0$. Category~C (large) requires both $|\Delta_{\mathrm{MH}}| \geq 1.5$ and statistical significance at $p < 0.05$ from the MH chi-squared test. Category~B (moderate) includes all remaining items: those with $1.0 \leq |\Delta_{\mathrm{MH}}| < 1.5$, or $|\Delta_{\mathrm{MH}}| \geq 1.5$ without statistical significance. The dual threshold in ETS~C (effect size \emph{and} significance) guards against flagging items that show large but unreliable effect sizes. Throughout this paper, we report the percentage of items classified as ETS~C, denoted C\%.
31	
32	The choice of matching variable (the total score used for stratification) affects both validity and interpretation. We distinguish three matching strategies: (1)~\emph{standard matching} uses the within-benchmark total score on all items of the same benchmark; (2)~\emph{cross-subject matching} uses the total score on all subjects \emph{other than} the one containing the item under test, preventing the matching variable from absorbing injected contamination signals (\Cref{sec:injection}); and (3)~\emph{external matching} uses the total score on a different benchmark entirely (e.g., MMLU total score as the matching variable when testing DIF on GSM8K items), providing an independent ability proxy uncontaminated by the target benchmark. Cross-subject and external matching both address matching variable contamination but at different granularities: cross-subject operates within a multi-domain benchmark, while external operates across benchmarks.
33	
34	\subsection{Cohort Designs}
35	\label{sec:cohorts}
36	
37	DIF requires defining a reference group and a focal group. We construct five cohort comparisons, each designed to isolate a different source of variation.
38	
39	\paragraph{Temporal.} The reference group consists of models released in 2023 ($N = 1{,}080$) and the focal group consists of models released in 2024 ($N = 807$). This is the primary comparison for detecting items whose functioning changed across model generations.
40	
41	\paragraph{Ability-quintile.} Models within the same temporal window are divided by total score into quintiles. The focal group contains the lowest-scoring models (Q1--Q2) and the reference group contains the highest-scoring models (Q4--Q5). This comparison tests whether ability differences alone produce DIF, without temporal confounds.
42	
43	\paragraph{Within-family.} Llama-2 models ($N = 161$) serve as the reference group and Llama-3 models ($N = 308$) as the focal group. This comparison isolates generational changes within a single model family.
44	
45	\paragraph{Within-subject.} DIF is computed separately for each of the 57 MMLU subjects, with the matching variable (total score) restricted to items within the same subject. This design tests whether instability concentrates in specific knowledge domains.
46	
47	\paragraph{Random split.} The 2023 cohort is divided into two equal random halves ($N = 540$ each). This serves as a sanity check: no systematic DIF should appear between two random subsets of the same population (expected C\% $\approx 0$).
48	
49	\subsection{Semi-Synthetic Injection Framework}
50	\label{sec:injection}
51	
52	To evaluate whether MH-DIF can detect differential contamination when it is present, we construct a semi-synthetic framework with controlled ground truth.
53	
54	\paragraph{Procedure.} From items classified as ETS~A in the uninjected data (negligible DIF), we select 20\% uniformly at random as the ``contaminated'' set. For each contaminated item, we flip incorrect responses to correct in the focal group at exploitation rate $p \in \{0.0, 0.3, 0.5, 0.7, 1.0\}$. We then run MH-DIF on the modified response matrix and measure detection performance. We report $\Delta\mathrm{TPR} = \mathrm{TPR}(\text{injected}) - \mathrm{TPR}(\text{baseline})$ and $\Delta\mathrm{FPR} = \mathrm{FPR}(\text{injected}) - \mathrm{FPR}(\text{baseline})$, where TPR is the true positive rate on injected items and FPR is the false positive rate on uninjected items. Each injection level is repeated across 5 random seeds for uncertainty estimation.
55	
56	\paragraph{Cross-subject matching.} The choice of matching variable is critical for valid semi-synthetic evaluation. When contamination is injected into items within subject $X$, the total score on subject $X$ absorbs part of the injection signal. Using this contaminated total score as the MH matching variable violates the conditional independence assumption and inflates FPR. Cross-subject matching resolves this problem by computing the matching variable from all subjects \emph{other than} the one being tested. Under this protocol, $\Delta\mathrm{FPR} = 0.000$ across all five MMLU domains, while detection power is preserved ($\Delta\mathrm{TPR} > 0.3$ at $p = 0.5$ for four of five subjects). We adopt cross-subject matching as the standard protocol for all semi-synthetic analyses.
57	
58	Diagnostic procedures (Yen's Q3 local independence, domain-specificity analysis, instability decomposition) and statistical details (multiple testing correction, threshold sensitivity, architecture heterogeneity checks) appear in \Cref{app:method_details}.
59	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2cb4e95c-704c-477b-ad9d-717c8e5b1f8b",
  "isSidechain": true,
  "promptId": "9f953575-95eb-4981-bd3f-8e47b7d03776",
  "agentId": "a0969a4e4a19ae3ba",
  "type": "user",
  "uuid": "ee3cd11a-2915-4181-8edf-899d5d98103a",
  "sourceToolAssistantUUID": "2cb4e95c-704c-477b-ad9d-717c8e5b1f8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T06:55:40.772Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R5fkD4jw5PVe1ejf4G3zks`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee3cd11a-2915-4181-8edf-899d5d98103a",
  "isSidechain": true,
  "agentId": "a0969a4e4a19ae3ba",
  "requestId": "req_011CbFGzX8Mz1DjwMKsUy5rr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91ba13f4-9447-4ff6-bc28-749d866b0cee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HH65u2yHnHgyHktGc9pc8C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6609,
      "cache_read_input_tokens": 22440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6609,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 19 · 2026-05-21T06:55:40.778Z_

<details><summary>↩ Tool result · `toolu_01R5fkD4jw5PVe1ejf4G3zks`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Applying Mantel-Haenszel DIF analysis to the METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items), we find that 31\% of items are functionally unstable across model generations under ETS Category~C classification. The instability is robust across thresholds (10--49\% at $|\Delta_{\mathrm{MH}}| \in [2.5, 1.0]$), confirmed non-random by a random-split control (0.18\%), and predominantly item-specific: domain accuracy improvement accounts for only 2.4 percentage points of the 31.3\% C\%. This instability does not invalidate MMLU as a ranking instrument ($\rho \approx 0.997$ between full and stable-item rankings) but signals that item-level measurement properties are drifting across model generations.
5	
6	The analysis exposes a validation methodology gap in the contamination detection literature. Web-overlap labels measure whether items exist in publicly accessible training corpora, not whether items function differently across model cohorts. The enrichment between DIF flags and these labels is 0.96 (chance level), the expected outcome when a differential method is evaluated against global-exposure labels. Our semi-synthetic injection framework with cross-subject matching ($\Delta\mathrm{FPR} = 0.000$, $\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$) provides a controlled alternative that any item-level detector can use for validation. Cross-benchmark replication on GSM8K ($\Delta\mathrm{TPR} = {+}0.818$) confirms the framework's portability.
7	
8	DIF-flagged items are not noise. They concentrate cross-generational discriminative information ($z = -8$ to $-49\sigma$ vs.\ random removal) and anti-correlate with the GSM1K contamination gap ($r = -0.478$, $p = 0.005$, $N = 33$), consistent with DIF items capturing genuine capability change that contamination does not confer. Individual model families show distinctive DIF profiles: Phi-3 and Llama-3 gain $+700$ to $+850$ rank positions under stable-item evaluation, while Mistral-based merges lose $-400$ to $-587$ positions. DIF is a diagnostic lens for understanding what changed across model generations, not a quality filter for removing bad items.
9	
10	LLM benchmarks need psychometric monitoring alongside score reporting. DIF analysis provides a scalable, method-agnostic diagnostic that requires only a binary response matrix and group labels, with no access to model internals or training data.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91ba13f4-9447-4ff6-bc28-749d866b0cee",
  "isSidechain": true,
  "promptId": "9f953575-95eb-4981-bd3f-8e47b7d03776",
  "agentId": "a0969a4e4a19ae3ba",
  "type": "user",
  "uuid": "a5fa74f9-e50d-4317-a36b-5161b51d7444",
  "sourceToolAssistantUUID": "91ba13f4-9447-4ff6-bc28-749d866b0cee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T06:55:40.993Z_

<details open><summary>🔧 Tool call — Read · `toolu_016sb4ghSUbYP4DZAAZp5New`</summary>

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
  "parentUuid": "a5fa74f9-e50d-4317-a36b-5161b51d7444",
  "isSidechain": true,
  "agentId": "a0969a4e4a19ae3ba",
  "requestId": "req_011CbFGzX8Mz1DjwMKsUy5rr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a07bb6d2-ce23-43cb-a4c0-2a334eabbee3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HH65u2yHnHgyHktGc9pc8C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6609,
      "cache_read_input_tokens": 22440,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6609
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 22440,
          "cache_creation_input_tokens": 6609,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6609,
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

_source line 21 · 2026-05-21T06:55:41.010Z_

<details><summary>↩ Tool result · `toolu_016sb4ghSUbYP4DZAAZp5New`</summary>

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
22	\paragraph{Architecture heterogeneity.} The METABENCH MMLU population consists of 99.98\% decoder-only models (5,226 of 5,227). This near-complete architectural homogeneity eliminates architecture as a confound for DIF analysis. We verify this by excluding the single encoder-decoder model and confirming identical results.
23	
24	\section{Structural Analysis Details}
25	\label{app:structural}
26	
27	Three progressively refined approaches fail to reduce the temporal false positive rate below 31\%, revealing a structural property of the data rather than a methodological limitation. Matched-ability quintile analysis restricts comparisons to models of similar total score and yields enrichment ratios of 0.94--1.04, with temporal FPR unchanged at approximately 0.31. IRT $\theta$-conditioning with 20 ability strata achieves $r(\theta, \mathrm{total\ score}) = 0.9986$ and FPR $= 0.312$, confirming that the external total score already captures nearly all ability variance relevant to DIF computation. Within-subject DIF analysis on 5 representative subjects, intended to isolate subject-specific effects, finds mean C\% $= 38.1\%$, exceeding the 25\% threshold that would indicate viable bifactor structure. \Cref{tab:structural_comparison} summarizes these results.
28	
29	The temporal FPR reflects genuine item-level instability that persists regardless of how ability is measured or conditioned. Yen's Q3 diagnostic reveals mild local dependence within subjects (11.3\% of within-subject item pairs exceed $|Q3| > 0.20$, vs.\ 2.2\% cross-subject; $5{\times}$ ratio, $p = 2.3 \times 10^{-9}$), which contributes to elevated within-subject DIF rates but is not the primary driver: the cross-subject matching protocol addresses this bias, and temporal C\% persists under external matching (full Q3 distributions in Appendix~Figure~A2).
30	
31	\begin{table}[h]
32	\centering
33	\caption{Structural approaches to reducing temporal DIF. None reduces baseline FPR below 31\%, indicating that the observed instability is not an artifact of ability matching. Subscript $\pm$ values denote standard deviations across 5 injection seeds (baseline row only).}
34	\label{tab:structural_comparison}
35	\small
36	\begin{tabular}{lcccc}
37	\toprule
38	Approach & Mechanism & Temporal FPR & TPR ($p{=}0.5$) & Outcome \\
39	\midrule
40	Baseline (external) & Cross-benchmark total score & $0.314_{\pm.009}$ & $0.834_{\pm.027}$ & Reference \\
41	Matched-ability & Within-quintile temporal DIF & ${\sim}$0.31 & -- & Enrich.\ 0.94--1.04 \\
42	$\theta$-conditioning & $\theta$ replaces total score & 0.312 & 0.876 & $r(\theta,\mathrm{total}) {=} 0.9986$ \\
43	Within-subject & Per-subject DIF & -- & -- & C\% $= 38.1\%$ ($>$25\%) \\
44	\bottomrule
45	\end{tabular}
46	\end{table}
47	
48	\section{Additional Figures}
49	\label{app:figures}
50	
51	\begin{figure}[h]
52	\centering
53	\includegraphics[width=\columnwidth]{fig_3_within_subject_matching.pdf}
54	\caption{Cross-subject vs.\ within-subject matching for semi-synthetic DIF detection. Cross-subject matching eliminates FPR inflation ($\Delta\mathrm{FPR} = 0.000$) while preserving detection power ($\Delta\mathrm{TPR} > 0.3$ for 4/5 subjects at $p = 0.5$). Within-subject matching inflates FPR by ${+}0.186$ on average.}
55	\label{app:fig_matching}
56	\end{figure}
57	
58	\begin{figure}[h]
59	\centering
60	\includegraphics[width=\columnwidth]{fig_4_downstream_impact.pdf}
61	\caption{Downstream impact of DIF-based item filtering on model rankings. Despite $\rho \approx 0.997$ overall, individual model families show systematic rank shifts when evaluated on stable items only.}
62	\label{app:fig_downstream}
63	\end{figure}
64	
65	\section{Cross-Benchmark Comparison}
66	\label{app:gsm8k_details}
67	
68	\begin{table}[h]
69	\centering
70	\caption{Cross-benchmark comparison of DIF analysis on MMLU and GSM8K. Both benchmarks exhibit temporal item instability with validated semi-synthetic detection power. Standard and external matching use different exploitation rates ($p$) because each benchmark's optimal operating point differs; external matching results are compared at $p = 0.5$ for both. Subscript $\pm$ values denote standard deviations across 5 random injection seeds.}
71	\label{tab:gsm8k_comparison}
72	\small
73	\begin{tabular}{lcc}
74	\toprule
75	Metric & MMLU & GSM8K \\
76	\midrule
77	Items & 12,508 & 1,319 \\
78	Models & 5,227 & 6,702 \\
79	Temporal C\% & 31.3\% & 18.9\% \\
80	Sanity C\% & 0.18\% & 0.3\% \\
81	$\Delta$TPR ($p{=}0.7$, standard) & -- & $+0.818_{\pm.006}$ \\
82	$\Delta$TPR ($p{=}0.5$, external) & $+0.508_{\pm.027}$ & $+0.514_{\pm.028}$ \\
83	\bottomrule
84	\end{tabular}
85	\end{table}
86	
87	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a07bb6d2-ce23-43cb-a4c0-2a334eabbee3",
  "isSidechain": true,
  "promptId": "9f953575-95eb-4981-bd3f-8e47b7d03776",
  "agentId": "a0969a4e4a19ae3ba",
  "type": "user",
  "uuid": "40ef83f1-644d-4a38-8d23-f2deaffc19bf",
  "sourceToolAssistantUUID": "a07bb6d2-ce23-43cb-a4c0-2a334eabbee3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-21T06:55:44.080Z_

Now let me also check the bibliography to evaluate reference completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40ef83f1-644d-4a38-8d23-f2deaffc19bf",
  "isSidechain": true,
  "agentId": "a0969a4e4a19ae3ba",
  "requestId": "req_011CbFGzrvjJPSQzQsBi2GkD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16138869-a366-4211-925b-b07218952668",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HgCP8zK9rqX3XSj7V3owjS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3152,
      "cache_read_input_tokens": 29049,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3152,
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

_source line 23 · 2026-05-21T06:55:44.702Z_

<details open><summary>🔧 Tool call — Glob · `toolu_013RCRee7EtACjfMrTfqEM8E`</summary>

```json
{
  "pattern": "paper/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16138869-a366-4211-925b-b07218952668",
  "isSidechain": true,
  "agentId": "a0969a4e4a19ae3ba",
  "requestId": "req_011CbFGzrvjJPSQzQsBi2GkD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e7bf7fb-8042-4ab5-b64c-f94c7451d95d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HgCP8zK9rqX3XSj7V3owjS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3152,
      "cache_read_input_tokens": 29049,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3152
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 117,
          "cache_read_input_tokens": 29049,
          "cache_creation_input_tokens": 3152,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3152,
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

_source line 24 · 2026-05-21T06:55:44.725Z_

<details><summary>↩ Tool result · `toolu_013RCRee7EtACjfMrTfqEM8E`</summary>

```text
paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e7bf7fb-8042-4ab5-b64c-f94c7451d95d",
  "isSidechain": true,
  "promptId": "9f953575-95eb-4981-bd3f-8e47b7d03776",
  "agentId": "a0969a4e4a19ae3ba",
  "type": "user",
  "uuid": "50d650a0-41a7-4fb3-b20c-2ace35c40b7e",
  "sourceToolAssistantUUID": "4e7bf7fb-8042-4ab5-b64c-f94c7451d95d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T06:55:47.381Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KSWLnAbao1bBz2cjpkpYdt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50d650a0-41a7-4fb3-b20c-2ace35c40b7e",
  "isSidechain": true,
  "agentId": "a0969a4e4a19ae3ba",
  "requestId": "req_011CbFH197pEhDgZzpcPzs4a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3f9e69f-7320-40f9-8d80-9052a583b49f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HjvQ4EEt1AAoTsEyVj1xQs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 135,
      "cache_read_input_tokens": 32201,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 135
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 91,
          "cache_read_input_tokens": 32201,
          "cache_creation_input_tokens": 135,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 135,
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

_source line 26 · 2026-05-21T06:55:47.387Z_

<details><summary>↩ Tool result · `toolu_01KSWLnAbao1bBz2cjpkpYdt`</summary>

```text
1	% ============================================================
2	% Benchmark Contamination Detection
3	% ============================================================
4	
5	@inproceedings{balloccu2024leak,
6	  title     = {Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source {LLMs}},
7	  author    = {Balloccu, Simone and Schmidtova, Patrícia and Lango, Mateusz and Dusek, Ondrej},
8	  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (EACL)},
9	  year      = {2024},
10	  doi       = {10.18653/v1/2024.eacl-long.5},
11	  url       = {https://arxiv.org/abs/2402.03927}
12	}
13	
14	@inproceedings{dekoninck2024constat,
15	  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},
16	  author    = {Dekoninck, Jasper and Mueller, Mark Niklas and Vechev, Martin},
17	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
18	  year      = {2024},
19	  url       = {https://arxiv.org/abs/2405.16281}
20	}
21	
22	@inproceedings{golchin2024timetravel,
23	  title     = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},
24	  author    = {Golchin, Shahriar and Surdeanu, Mihai},
25	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
26	  year      = {2024},
27	  url       = {https://arxiv.org/abs/2308.08493}
28	}
29	
30	@inproceedings{li2024contamination,
31	  title     = {An Open-Source Data Contamination Report for Large Language Models},
32	  author    = {Li, Yucheng and Guo, Yunhao and Guerin, Frank and Lin, Chenghua},
33	  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},
34	  year      = {2024},
35	  doi       = {10.18653/v1/2024.findings-emnlp.30},
36	  url       = {https://aclanthology.org/2024.findings-emnlp.30/}
37	}
38	
39	@misc{liang2026dvd,
40	  title         = {{DVD}: Detection via Variance of Generation Distribution for Variant Contamination},
41	  author        = {Liang, Rongzhen},
42	  year          = {2026},
43	  eprint        = {2601.04895},
44	  archivePrefix = {arXiv},
45	  primaryClass  = {cs.CL},
46	  url           = {https://arxiv.org/abs/2601.04895}
47	}
48	
49	@inproceedings{shi2024mink,
50	  title     = {Detecting Pretraining Data from Large Language Models},
51	  author    = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},
52	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
53	  year      = {2024},
54	  url       = {https://arxiv.org/abs/2310.16789}
55	}
56	
57	@inproceedings{tao2026selfcritique,
58	  title     = {Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models},
59	  author    = {Tao, Yixin},
60	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
61	  year      = {2026},
62	  url       = {https://arxiv.org/abs/2510.09259}
63	}
64	
65	@inproceedings{wang2026fragility,
66	  title     = {On The Fragility of Benchmark Contamination Detection in Reasoning Models},
67	  author    = {Wang, Haonan and Li, Haoyang and Ko, Boeun and Zhang, Hongyang},
68	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
69	  year      = {2026},
70	  url       = {https://arxiv.org/abs/2510.02386}
71	}
72	
73	@misc{zhang2024gsm1k,
74	  title         = {A Careful Examination of Large Language Model Performance on Grade School Arithmetic},
75	  author        = {Zhang, Hugh},
76	  year          = {2024},
77	  eprint        = {2405.00332},
78	  archivePrefix = {arXiv},
79	  primaryClass  = {cs.CL},
80	  url           = {https://arxiv.org/abs/2405.00332}
81	}
82	
83	@misc{zhang2024minkpp,
84	  title         = {{Min-K\%++}: Improved Baseline for Detecting Pre-Training Data from Large Language Models},
85	  author        = {Zhang, Jingyang and Sun, Jingwei and Yeats, Eric and Ouyang, Yang and Kuo, Martin and Zhang, Jianyi and Yang, Hao and Li, Hai},
86	  year          = {2024},
87	  eprint        = {2404.02936},
88	  archivePrefix = {arXiv},
89	  primaryClass  = {cs.CL},
90	  url           = {https://arxiv.org/abs/2404.02936}
91	}
92	
93	% ============================================================
94	% IRT Methodology & Equating
95	% ============================================================
96	
97	@misc{hardy2026scalability,
98	  title         = {Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients},
99	  author        = {Hardy, Matthew and Gilbert, Juan and Domingue, Benjamin},
100	  year          = {2026},
101	  eprint        = {2603.24999},
102	  archivePrefix = {arXiv},
103	  primaryClass  = {cs.CL},
104	  url           = {https://arxiv.org/abs/2603.24999}
105	}
106	
107	@article{kim2019fpc,
108	  title   = {Application of {IRT} Fixed Parameter Calibration to Multiple-Group Test Data},
109	  author  = {Kim, Seonghoon and Kolen, Michael},
110	  journal = {Applied Measurement in Education},
111	  year    = {2019},
112	  doi     = {10.1080/08957347.2019.1660344},
113	  url     = {https://www.tandfonline.com/doi/abs/10.1080/08957347.2019.1660344}
114	}
115	
116	@inproceedings{lalor2019irt,
117	  title     = {Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds},
118	  author    = {Lalor, John and Wu, Hao and Yu, Hong},
119	  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},
120	  year      = {2019},
121	  doi       = {10.18653/v1/D19-1434},
122	  url       = {https://aclanthology.org/D19-1434/}
123	}
124	
125	@inproceedings{vania2021irt,
126	  title     = {Comparing Test Sets with Item Response Theory},
127	  author    = {Vania, Clara and Htut, Phu Mon and Huang, William and Mungra, Dhara and Pang, Richard Yuanzhe and Phang, Jason and Liu, Haokun and Cho, Kyunghyun and Bowman, Samuel R.},
128	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
129	  year      = {2021},
130	  doi       = {10.18653/v1/2021.acl-long.92},
131	  url       = {https://aclanthology.org/2021.acl-long.92/}
132	}
133	
134	@misc{li2025atlas,
135	  title         = {{ATLAS}: Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},
136	  author        = {Li, Peiyang and Tang, Xiaobo and Chen, Sai and Cheng, Ying and Metoyer, Ronald and Hua, Tianyi and Chawla, Nitesh V.},
137	  year          = {2025},
138	  eprint        = {2511.04689},
139	  archivePrefix = {arXiv},
140	  primaryClass  = {cs.CL},
141	  url           = {https://arxiv.org/abs/2511.04689}
142	}
143	
144	@misc{chen2025irtnet,
145	  title         = {Learning Compact Representations of {LLM} Abilities via Item Response Theory},
146	  author        = {Chen, Jiayi and Wang, Chao and Zhang, Guoqiang and Ye, Peijin and Bai, Lei and Hu, Wenjun and Qu, Yongchao and Hu, Songlin},
147	  year          = {2025},
148	  eprint        = {2510.00844},
149	  archivePrefix = {arXiv},
150	  primaryClass  = {cs.CL},
151	  url           = {https://arxiv.org/abs/2510.00844}
152	}
153	
154	@misc{choi2026llmjudgeirt,
155	  title         = {Diagnosing the Reliability of {LLM}-as-a-Judge via Item Response Theory},
156	  author        = {Choi, Jiseong and Park, Seonho and Cho, Changwon and Park, Hojun and Kim, Bumsoo},
157	  year          = {2026},
158	  eprint        = {2602.00521},
159	  archivePrefix = {arXiv},
160	  primaryClass  = {cs.CL},
161	  url           = {https://arxiv.org/abs/2602.00521}
162	}
163	
164	@misc{habba2026growingpains,
165	  title         = {Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},
166	  author        = {Habba, Eitam and Itzhak, Ido and Yehudai, Asaf and Perlitz, Yotam and Bandel, Elron and Shmueli-Scheuer, Michal and Choshen, Leshem and Stanovsky, Gabriel},
167	  year          = {2026},
168	  eprint        = {2604.12843},
169	  archivePrefix = {arXiv},
170	  primaryClass  = {cs.CL},
171	  url           = {https://arxiv.org/abs/2604.12843}
172	}
173	
174	@inproceedings{zhou2026psnirt,
175	  title     = {Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},
176	  author    = {Zhou, Hao and Huang, Heng and Zhao, Zhenheng and Han, Lin and Wang, Haoyu and Chen, Ke and Yang, Min and Bao, Weidong and Dong, Ji and Xu, Bo and Zhu, Changshui and Cao, Huijun and Zhao, Tiejun},
177	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},
178	  year      = {2026},
179	  url       = {https://arxiv.org/abs/2505.15055}
180	}
181	
182	% ============================================================
183	% Dynamic Benchmark Design
184	% ============================================================
185	
186	@inproceedings{white2025livebench,
187	  title     = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},
188	  author    = {White, Colin},
189	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
190	  year      = {2025},
191	  doi       = {10.48550/arXiv.2406.19314},
192	  url       = {https://arxiv.org/abs/2406.19314}
193	}
194	
195	@misc{kipnis2024metabench,
196	  title         = {metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language Models},
197	  author        = {Kipnis, Alon and Voudouris, Konstantinos and Schulze Buschoff, Luca Maria and Schulz, Eric},
198	  year          = {2024},
199	  eprint        = {2407.12844},
200	  archivePrefix = {arXiv},
201	  primaryClass  = {cs.CL},
202	  url           = {https://arxiv.org/abs/2407.12844}
203	}
204	
205	@inproceedings{hendrycks2021mmlu,
206	  title     = {Measuring Massive Multitask Language Understanding},
207	  author    = {Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},
208	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
209	  year      = {2021},
210	  url       = {https://arxiv.org/abs/2009.03300}
211	}
212	
213	@article{liang2023helm,
214	  title   = {Holistic Evaluation of Language Models},
215	  author  = {Liang, Percy and Bommasani, Rishi and Lee, Tony and Tsipras, Dimitris and Soylu, Dilara and Yasunaga, Michihiro and Zhang, Yian and Narayanan, Deepak and Wu, Yuhuai and Kumar, Ananya},
216	  journal = {Transactions on Machine Learning Research},
217	  year    = {2023},
218	  doi     = {10.1111/nyas.15007},
219	  url     = {https://arxiv.org/abs/2211.09110}
220	}
221	
222	@inproceedings{chiang2024chatbot,
223	  title     = {Chatbot Arena: An Open Platform for Evaluating {LLMs} by Human Preference},
224	  author    = {Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios N. and Li, Tianle and Li, Dacheng and Zhang, Hao and Zhu, Banghua and Jordan, Michael I. and Gonzalez, Joseph E. and Stoica, Ion},
225	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
226	  year      = {2024},
227	  doi       = {10.48550/arXiv.2403.04132},
228	  url       = {https://arxiv.org/abs/2403.04132}
229	}
230	
231	@misc{mialon2023gaia,
232	  title         = {{GAIA}: a benchmark for General {AI} Assistants},
233	  author        = {Mialon, Grégoire and Fourrier, Clémentine and Swift, Craig and Wolf, Thomas and LeCun, Yann and Scialom, Thomas},
234	  year          = {2023},
235	  eprint        = {2311.12983},
236	  archivePrefix = {arXiv},
237	  primaryClass  = {cs.CL},
238	  url           = {https://arxiv.org/abs/2311.12983}
239	}
240	
241	@inproceedings{li2024latesteval,
242	  title     = {{LatestEval}: Addressing Data Contamination in Language Model Evaluation through Dynamic and Time-Sensitive Test Construction},
243	  author    = {Li, Yucheng and Guerin, Frank and Lin, Chenghua},
244	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},
245	  year      = {2024},
246	  doi       = {10.48550/arXiv.2312.12343},
247	  url       = {https://arxiv.org/abs/2312.12343}
248	}
249	
250	@inproceedings{kiela2021dynabench,
251	  title     = {{Dynabench}: Rethinking Benchmarking in {NLP}},
252	  author    = {Kiela, Douwe and Bartolo, Max and Nie, Yixin and Kaushik, Divyansh and Geiger, Atticus and Wu, Zhengxuan and Vidgen, Bertie and Prasad, Grusha and Singh, Amanpreet and Ringshia, Pratik and Ma, Zhiyi and Thrush, Tristan and Riedel, Sebastian and Talat, Zeerak and Stenetorp, Pontus and Jia, Robin},
253	  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
254	  year      = {2021},
255	  doi       = {10.18653/v1/2021.naacl-main.324},
256	  url       = {https://arxiv.org/abs/2104.14337}
257	}
258	
259	% ============================================================
260	% DIF Statistical Methods
261	% ============================================================
262	
263	@article{belzak2020smallsample,
264	  title   = {Testing Differential Item Functioning in Small Samples},
265	  author  = {Belzak, William},
266	  journal = {Multivariate Behavioral Research},
267	  year    = {2020},
268	  doi     = {10.1080/00273171.2019.1671162},
269	  url     = {https://www.tandfonline.com/doi/abs/10.1080/00273171.2019.1671162}
270	}
271	
272	@incollection{holland1988mh,
273	  title     = {Differential Item Functioning and the {Mantel-Haenszel} Procedure},
274	  author    = {Holland, Paul W. and Thayer, Dorothy T.},
275	  booktitle = {Test Validity},
276	  editor    = {Wainer, Howard and Braun, Henry I.},
277	  publisher = {Lawrence Erlbaum Associates},
278	  year      = {1988},
279	  doi       = {10.1002/j.2330-8516.1986.tb00186.x},
280	  url       = {https://onlinelibrary.wiley.com/doi/abs/10.1002/j.2330-8516.1986.tb00186.x}
281	}
282	
283	@article{shealy1993sibtest,
284	  title   = {A Model-Based Standardization Approach that Separates True Bias/{DIF} from Group Ability Differences and Detects Test Bias/{DTF} as Well as Item Bias/{DIF}},
285	  author  = {Shealy, Robin and Stout, William},
286	  journal = {Psychometrika},
287	  year    = {1993},
288	  doi     = {10.1007/BF02294572},
289	  url     = {https://link.springer.com/article/10.1007/BF02294572}
290	}
291	
292	@article{clauser1998dif,
293	  title   = {Using Statistical Procedures to Identify Differentially Functioning Test Items},
294	  author  = {Clauser, Brian E. and Mazor, Kathleen M.},
295	  journal = {Educational Measurement: Issues and Practice},
296	  year    = {1998},
297	  doi     = {10.1111/j.1745-3992.1998.tb00619.x},
298	  url     = {https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3992.1998.tb00619.x}
299	}
300	
301	@book{zumbo1999handbook,
302	  title     = {A Handbook on the Theory and Methods of Differential Item Functioning ({DIF}): Logistic Regression Modeling as a Unitary Framework for Binary and {Likert}-Type (Ordinal) Item Scores},
303	  author    = {Zumbo, Bruno D.},
304	  year      = {1999},
305	  publisher = {Directorate of Human Resources Research and Evaluation, Department of National Defense},
306	  address   = {Ottawa},
307	  url       = {https://faculty.educ.ubc.ca/zumbo/DIF/handbook.pdf}
308	}
309	
310	@article{meredith1993invariance,
311	  title   = {Measurement Invariance, Factor Analysis and Factorial Invariance},
312	  author  = {Meredith, William},
313	  journal = {Psychometrika},
314	  year    = {1993},
315	  doi     = {10.1007/BF02294825},
316	  url     = {https://link.springer.com/article/10.1007/BF02294825}
317	}
318	
319	@article{vandenberg2000invariance,
320	  title   = {A Review and Synthesis of the Measurement Invariance Literature: Suggestions, Practices, and Recommendations for Organizational Research},
321	  author  = {Vandenberg, Robert J. and Lance, Charles E.},
322	  journal = {Organizational Research Methods},
323	  year    = {2000},
324	  doi     = {10.1177/109442810031002},
325	  url     = {https://journals.sagepub.com/doi/10.1177/109442810031002}
326	}
327	
328	@article{swaminathan1990logistic,
329	  title   = {Detecting Differential Item Functioning Using Logistic Regression Procedures},
330	  author  = {Swaminathan, Hariharan and Rogers, H. Jane},
331	  journal = {Journal of Educational Measurement},
332	  year    = {1990},
333	  doi     = {10.1111/j.1745-3984.1990.tb00754.x},
334	  url     = {https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3984.1990.tb00754.x}
335	}
336	
337	@article{teresi2007dif,
338	  title   = {Differential Item Functioning and Health Assessment},
339	  author  = {Teresi, Jeanne A. and Fleishman, John A.},
340	  journal = {Quality of Life Research},
341	  year    = {2007},
342	  doi     = {10.1007/s11136-007-9184-6},
343	  url     = {https://link.springer.com/article/10.1007/s11136-007-9184-6}
344	}
345	
346	@book{lord1980irt,
347	  title     = {Applications of Item Response Theory to Practical Testing Problems},
348	  author    = {Lord, Frederic M.},
349	  year      = {1980},
350	  publisher = {Lawrence Erlbaum Associates},
351	  address   = {Hillsdale, NJ}
352	}
353	
354	@article{raju1988area,
355	  title   = {The Area between Two Item Characteristic Curves},
356	  author  = {Raju, Nambury S.},
357	  journal = {Psychometrika},
358	  year    = {1988},
359	  doi     = {10.1007/BF02294403},
360	  url     = {https://link.springer.com/article/10.1007/BF02294403}
361	}
362	
363	@article{muthen1985mimic,
364	  title   = {A Method for Studying the Homogeneity of Test Items with Respect to Other Relevant Variables},
365	  author  = {Muth{\'e}n, Bengt},
366	  journal = {Journal of Educational Statistics},
367	  year    = {1985},
368	  doi     = {10.2307/1164966}
369	}
370	
371	@article{woods2009mimic,
372	  title   = {Empirical Selection of Anchors for Tests of Differential Item Functioning},
373	  author  = {Woods, Carol M.},
374	  journal = {Applied Psychological Measurement},
375	  year    = {2009},
376	  doi     = {10.1177/0146621609331279}
377	}
378	
379	% ============================================================
380	% LLM Evaluation Methodology
381	% ============================================================
382	
383	@article{burnell2023rethink,
384	  title   = {Rethink reporting of evaluation results in {AI}},
385	  author  = {Burnell, Ryan and Schellaert, Wout and Burden, John and Ullman, Tomer D. and Martinez-Plumed, Fernando and Tenenbaum, Joshua B. and Rutar, Danaja and Cheke, Lucy G. and Sohl-Dickstein, Jascha and Mitchell, Melanie and Kiela, Douwe and Shanahan, Murray and Voorhees, Ellen M. and Cohn, Anthony G. and Leibo, Joel Z. and Hernandez-Orallo, Jose},
386	  journal = {Science},
387	  year    = {2023},
388	  doi     = {10.1126/science.adf6369},
389	  url     = {https://www.science.org/doi/10.1126/science.adf6369}
390	}
391	
392	@article{chang2024survey,
393	  title   = {A Survey on Evaluation of Large Language Models},
394	  author  = {Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Zhu, Kaijie and Chen, Hao and Yang, Linyi and Yi, Xiaoyuan and Wang, Cunxiang and Wang, Yidong and Ye, Wei and Zhang, Yue and Chang, Yi and Yu, Philip S. and Yang, Qiang and Xie, Xing},
395	  journal = {ACM Transactions on Intelligent Systems and Technology},
396	  year    = {2024},
397	  doi     = {10.1145/3641289},
398	  url     = {https://dl.acm.org/doi/full/10.1145/3641289}
399	}
400	
401	@inproceedings{maiapolo2024tinybenchmarks,
402	  title     = {{tinyBenchmarks}: evaluating {LLMs} with fewer examples},
403	  author    = {Maia Polo, Felipe and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},
404	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
405	  year      = {2024},
406	  url       = {https://proceedings.mlr.press/v235/maia-polo24a.html}
407	}
408	
409	@inproceedings{wang2024mmlupro,
410	  title     = {{MMLU-Pro}: A More Robust and Challenging Multi-Task Language Understanding Benchmark},
411	  author    = {Wang, Yubo and Ma, Xueguang and Zhang, Ge and Ni, Yuansheng and Chandra, Abhranil and Guo, Shiguang and Ren, Weiming and Arulraj, Aaran and He, Xuan and Jiang, Ziyan and Li, Tianle and Ku, Max and Wang, Kai and Zhuang, Alex and Fan, Rongqi and Xue, Xiang and Chen, Wenhu},
412	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
413	  year      = {2024},
414	  url       = {https://arxiv.org/abs/2406.01574}
415	}
416	
417	@article{ott2022benchmark,
418	  title   = {Mapping global dynamics of benchmark creation and saturation in artificial intelligence},
419	  author  = {Ott, Simon and Barbosa-Silva, Adriano and Blagec, Kathrin and Brauner, Jan and Samwald, Matthias},
420	  journal = {Nature Communications},
421	  year    = {2022},
422	  doi     = {10.1038/s41467-022-34591-0},
423	  url     = {https://www.nature.com/articles/s41467-022-34591-0}
424	}
425	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3f9e69f-7320-40f9-8d80-9052a583b49f",
  "isSidechain": true,
  "promptId": "9f953575-95eb-4981-bd3f-8e47b7d03776",
  "agentId": "a0969a4e4a19ae3ba",
  "type": "user",
  "uuid": "9a78a894-32f4-4d66-bc7d-95f493897f9c",
  "sourceToolAssistantUUID": "f3f9e69f-7320-40f9-8d80-9052a583b49f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-21T06:57:11.456Z_

I now have a thorough understanding of the full paper. Here is my review.

---

### Summary

This paper applies Mantel-Haenszel Differential Item Functioning (DIF) analysis -- an established psychometric method -- to the METABENCH response matrix (5,227 models x 12,508 MMLU items) and finds that 31% of items show large temporal instability (ETS Category C) between 2023 and 2024 model cohorts. The authors argue this instability is diagnostic rather than destructive (rank correlation rho=0.997 with stable items), expose a validation gap in the contamination detection literature (web-overlap labels measure global exposure, not differential functioning), and provide a semi-synthetic injection framework validated on both MMLU and GSM8K. The paper positions itself as an empirical discovery contribution rather than an algorithmic novelty contribution.

### Strengths

- **Scale and thoroughness of the empirical investigation.** The analysis covers 5,227 models across 12,508 items with five cohort designs, three structural controls, threshold sensitivity sweeps, BH correction, model-family de-duplication, and cross-benchmark replication on GSM8K. This is substantially more rigorous than a typical "apply method X to domain Y" paper. The random-split sanity check (0.18% vs. 31.3%) and the ability-quintile control (2.9%) are particularly convincing in ruling out statistical noise and ability confounds.

- **The global-vs-differential contamination distinction is genuinely valuable.** The argument that web-overlap labels measure global exposure while DIF measures differential functioning is both conceptually clean and empirically validated (enrichment ratio = 0.96). This is a real contribution to the contamination detection literature: it identifies a blind spot that affects the entire validation methodology used by Min-K%, ConStat, and other detectors. The ICC diagram (Figure 1) communicates this clearly.

- **The semi-synthetic framework with cross-subject matching is methodologically sound.** Achieving Delta-FPR = 0.000 while maintaining meaningful detection power is non-trivial. The identification that within-subject matching inflates FPR by +0.186 on average is a useful methodological finding that generalizes beyond this paper. The framework is genuinely reusable.

- **Careful framing and honest limitations.** The paper consistently distinguishes between instability and invalidity. The GSM1K correlation (r=-0.478) is properly caveated as "suggestive at N=33." The logistic regression DIF analysis revealing additional non-uniform DIF (24.8%) that MH cannot detect is an unusually honest disclosure that the 31% estimate is conservative. The model independence sensitivity analysis (de-duplication at K=10, 20) directly addresses the obvious objection about fine-tunes/merges inflating the count.

- **The item characterization results add interpretive value.** The difficulty x direction interaction (rho=-0.597) -- hard items favor newer models while easy items favor older ones -- is genuinely interesting and goes beyond simply counting DIF items. This provides a mechanistic sketch of what "temporal instability" means at the item level.

- **Well-organized related work.** The positioning against Growing Pains (Habba et al. 2026) is clearly articulated: FPC assumes anchor stability while DIF diagnoses violations of that assumption. The complementarity framing is convincing. Coverage of DIF methodology, IRT in LLM evaluation, dynamic benchmarks, and contamination detection is thorough.

### Weaknesses

- **(Major) The "unprecedented scale" novelty claim is fragile.** The paper's core novelty argument is "established method x unprecedented scale = genuine empirical discovery." While I accept this framing in principle, the strength of the contribution depends entirely on whether the empirical findings are surprising or expected. A psychometrician familiar with DIF would likely predict that items in a static benchmark would show differential functioning across model generations that differ substantially in training data and methodology -- the question is how much and why. The 31% figure is striking, but the paper does not provide a theoretical or empirical basis for what one would expect ex ante. Without a "this is surprising because..." anchor, the contribution risks being perceived as confirmatory rather than revelatory. The rho=0.997 ranking preservation finding further dampens practical urgency: if aggregate rankings are essentially unchanged, the operational impact of 31% instability is limited to item-level diagnostics that the paper argues should become standard practice but does not operationalize into a concrete tool or protocol.

- **(Major) Missing direct comparison with existing contamination detectors.** The paper argues that DIF measures something fundamentally different from what ConStat, DVD, Min-K%, etc. measure (differential vs. global). This is a strong conceptual claim, but the paper never runs these baselines on the same data. Without a direct empirical comparison -- even if one expects low agreement -- the reader cannot assess whether DIF flags correlate with or diverge from existing detector outputs at the item level. The authors dropped ConStat and DVD comparisons from the experiment plan, which is acknowledged, but the absence weakens the meta-critique. Showing empirically that DIF flags and ConStat flags have low overlap would transform the conceptual argument into an empirical one.

- **(Major) Causal interpretation remains ambiguous.** The paper repeatedly notes that DIF "cannot distinguish contamination from legitimate capability change" (Discussion), yet the GSM1K analysis and the item characterization are presented in a way that implies DIF captures mostly capability change. The r=-0.478 correlation is interpreted as evidence that DIF items reflect "genuine capability change distinct from memorization," but this is a correlation of N=33 with a wide CI ([-0.71, -0.16]). The paper is more cautious in places than others; the abstract says DIF captures "genuine capability change rather than memorization" somewhat more definitively than the Discussion. The tension between "we cannot tell" and "here is evidence it is capability change" should be resolved more consistently.

- **(Minor) Architecture homogeneity limits generalizability claims.** The paper acknowledges 99.98% decoder-only models but still frames findings as pertaining to "LLM benchmarks" broadly. This is a monoculture finding. The paper does not discuss whether DIF patterns would differ if encoder-decoder or mixture-of-experts architectures were represented in meaningful numbers. The generalizability claim to "LLM benchmarks need psychometric monitoring" is stronger than what the evidence supports for architecturally diverse ecosystems.

- **(Minor) The reference list is adequate but has gaps in recent concurrent work.** The paper cites 10 core references by the task description's count, though the actual .bib has ~35 entries. The coverage is good for contamination detection and DIF methodology. However, some relevant concurrent work is absent (see Missing References below). The paper also does not engage with the measurement invariance / DIF literature in computerized adaptive testing (CAT), where temporal DIF monitoring is already standard practice -- this would strengthen the "old method, new domain" framing.

- **(Minor) The circularity ablation (z=-9.5 vs. z=-157) is described but not fully developed.** The claim that DIF removal is "16x less disruptive" than accuracy-gap removal despite 62.6% item overlap is intriguing but the paper does not explain why this is the case. Is it because DIF-C items are partially redundant with each other? Because the items DIF flags are systematically different in discrimination? A deeper analysis of why DIF removal is less disruptive would add value.

- **(Minor) The paper title uses a specific number (31%) that depends on the ETS C threshold.** Since the paper shows C% ranges from 10% to 49% depending on threshold, anchoring the title to 31% creates a precision that the data do not uniquely support. This is a presentational concern, not a scientific one, but reviewers and readers may question why 1.5 is the "right" threshold.

### Questions for Authors

1. What would you expect the DIF rate to be for a benchmark that is genuinely stable (i.e., items measuring a fixed construct with no training data leakage)? Without this baseline expectation, how should the reader calibrate whether 31% is large?

2. Have you considered running ConStat or Min-K% on even a subset of MMLU items and reporting the overlap with DIF flags? Even a partial comparison would substantially strengthen the meta-critique.

3. The GSM1K analysis (N=33, r=-0.478) is labeled "exploratory." What sample size would you need to make this confirmatory, and is this achievable with publicly available data?

4. The rho=0.997 ranking preservation finding seems to argue against the practical importance of the instability you document. How would you respond to the objection that if rankings are preserved, the instability is academically interesting but operationally irrelevant?

5. You show that domain accuracy improvement explains only 7.6% of the instability. What explains the remaining 92.4%? The paper attributes it to "item-specific changes" but does not provide a mechanistic account. Training methodology shifts? Tokenization changes? RLHF effects? Even speculative hypotheses would help.

6. The within-family comparison (Llama-2 vs. Llama-3) produces 61.3% C%, which you attribute to ability confounding. But could this also reflect genuine within-family DIF from architectural/training changes? How do you disentangle these?

### Missing References

The related work section is generally well-researched, but I note the following gaps:

- **Polo et al. (2024), "tinyBenchmarks"** is cited but the deeper connection to this work -- both use item-level analysis of LLM benchmarks with psychometric tools -- could be discussed more explicitly. Does DIF analysis suggest that tinyBenchmarks' IRT-selected items are stable or unstable?

- **Measurement invariance in CAT literature.** The DIF monitoring workflow the paper advocates is already standard in computerized adaptive testing (e.g., Wainer et al. 2007, "Testlet Response Theory and Its Applications"; Glas & Falcon 2003 on DIF monitoring in operational testing). Citing this existing practice would strengthen the argument that DIF monitoring for LLM benchmarks is overdue, not novel per se.

- **Zhan et al. (2024) or similar work on DIF in automated scoring.** There is an emerging literature on DIF in automated essay scoring and NLP-based assessment that bridges psychometrics and NLP more directly.

- **Eisenstein et al. (2025), METABENCH.** The paper data comes from METABENCH but the reference appears in the brief and is cited in the bib. If this is cited in-text only as "kipnis2024metabench," the Eisenstein et al. entry should be reconciled or removed.

- **Mantel & Haenszel (1959), the original paper.** The .bib cites Holland & Thayer 1988 as the DIF adaptation, but the original Mantel-Haenszel procedure for stratified analysis is from 1959 and is a standard citation in this literature.

### Scores

- **Soundness: 4 (Strong).** The experimental design is thorough with appropriate controls. The statistical methodology is correctly applied. The main weakness is the absence of direct baseline comparisons with existing detectors, but the claims that are made are well-supported.

- **Excitement: 3 (Interesting).** The global-vs-differential distinction and the 31% instability finding are genuinely useful contributions to the benchmark evaluation discourse. However, the practical impact is limited by the rho=0.997 ranking preservation, and the methodological novelty is modest (applying an existing method). The paper is solidly executed empirical work that will be cited by the benchmark integrity community, but it is unlikely to change mainstream evaluation practices in the near term.

- **Overall: 3 (Borderline).** The paper is thorough, well-written, and makes a legitimate empirical contribution. The meta-critique of web-overlap validation is the strongest individual contribution. However, the absence of direct comparisons with existing detectors, the ambiguous causal interpretation, and the limited practical impact (rankings barely change) place it at the boundary between accept and reject. If the authors added a ConStat/Min-K% comparison and sharpened the causal framing, this would move to a clear accept.

### Confidence: 4

I am confident in this assessment. I have expertise in both psychometric methods and LLM evaluation, and I read the paper carefully including the appendix. My uncertainty is primarily about whether the ACL community will value the "empirical discovery with established methods" framing -- this is standard in psychometrics journals but less common at NLP venues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a78a894-32f4-4d66-bc7d-95f493897f9c",
  "isSidechain": true,
  "agentId": "a0969a4e4a19ae3ba",
  "requestId": "req_011CbFH1Kyv9v5hjMHQeBgxa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02b2376d-6439-48b0-9518-8710a7beec6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "d7f648b5-736e-406c-b210-cfefb03cc5ed",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YazX3A8zsqjdLqxURJ2FLm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7918,
      "cache_read_input_tokens": 32336,
      "output_tokens": 2953,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7918
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2953,
          "cache_read_input_tokens": 32336,
          "cache_creation_input_tokens": 7918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7918,
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
