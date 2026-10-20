# Research conversation: You are Reviewer 1 (R1) for an ICLR submission. Your focus areas are **Methods** and **Experiments**. Produce a detailed

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a722f1afaa51a1652.jsonl`
- **Structured JSON:** [`8cc50d86f32695e6ee0d.json`](../../sessions/8c/8cc50d86f32695e6ee0d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

49 recorded events

### User

_source line 1 · 2026-05-21T05:31:50.547Z_

You are Reviewer 1 (R1) for an ICLR submission. Your focus areas are **Methods** and **Experiments**. Produce a detailed, rigorous review.

## Venue & Scoring
ICLR, 1-10 scale: 10=Strong Accept, 8=Accept, 6=Marginally Above threshold, 5=Marginally Below threshold, 3=Reject, 1=Strong Reject.

## Paper Summary
Title: "Empirical Characterization of Measurement Stability in LLM Benchmarks: Challenges and an Open Framework"

The paper applies Differential Item Functioning (DIF) analysis from psychometrics to METABENCH MMLU (5,227 models × 12,508 items). Key contributions:
1. Applies both Mantel-Haenszel (MH) and SIBTEST to find ≥18-31% of MMLU items exhibit functionally unstable measurement properties across model generations.
2. Proposes a semi-synthetic validation framework (ΔTPR methodology) with cross-subject matching that eliminates FPR inflation (ΔFPR=0.000).
3. Shows instability doesn't threaten ranking validity (ρ≈0.997 between full and stable-only rankings).
4. Ground-truth meta-critique: web-overlap/n-gram labels measure global exposure, not differential contamination — they can't validate item-level differential detectors.
5. Compares DIF against ConStat perturbation testing, DVD generation variance, Item-Focused Trees, and multi-signal ensemble fusion.
6. Reports extensive negative results: bifactor IRT equating fails (CFI=0.72, TLI=0.69), LLM item generation fails all metrics, RL robustness underpowered (N=13), Bayesian cumulative DIF insufficient gain, ensemble doesn't beat best single signal.
7. Provides a practitioner's guide.

## Detailed Paper Content

**Section 3 (Method):**
- §3.1 MH-DIF: Stratifies models by total score, computes α_MH and Δ_MH = -2.35 ln(α_MH). ETS classification: A (negligible, |Δ|<1.0), B (moderate, 1.0≤|Δ|<1.5), C (large, |Δ|≥1.5). MH detects only uniform DIF.
- §3.2 SIBTEST: Partitions items into studied/matching subtests, detects both uniform and non-uniform (crossing) DIF. Threshold: β̂ ≥ 0.088.
- §3.3 Semi-Synthetic Validation: Injects differential contamination (flip incorrect→correct with exploitation rate p∈[0,1]) into real METABENCH response matrix. Measures ΔTPR(p)=TPR(p)-TPR(0). Cross-subject matching: conditions MH on total score across other subjects to eliminate matching-variable contamination. ΔFPR measures false-positive inflation.
- §3.4 Alternative Methods: ConStat (237 reformulated items, semantic similarity=0.91), DVD (500 items, 12 models, 50 responses/item, temperature 0.7), Item-Focused Trees (release date as continuous covariate).

**Section 4 (Experiments):**
- §4.1 Temporal DIF on MMLU: MH flags 31.3% as ETS C. SIBTEST flags 44.7%. Jaccard overlap only 0.48. Random-split sanity: C%=0.18%. Ability-stratified: C%=2.9%. Within-family (Llama-2 vs Llama-3): 61.3%. Architecture stratification: 99.98% decoder-only, removing 1 non-decoder model changes nothing. IRT fit remains poor (CFI=0.41, RMSEA=0.089, 97.8-98.1% models |Lz|>2).
- §4.2 Ground-Truth Meta-Critique: DIF enrichment against Li et al. clean labels ≈0.96. This is expected because web-overlap measures global, not differential exposure.
- §4.3 Semi-Synthetic Validation: ΔTPR increases monotonically from 0.222 (p=0.3) to 0.674 (p=1.0). ΔFPR=0.000 across all conditions. Within-subject matching inflates FPR by +0.186. Paper acknowledges binary flip is simplification (Table 5: signal type, response pattern, item correlation, effect gradient all HIGH/MEDIUM mismatch with real contamination).
- §4.4 GSM8K Replication: C%=18.9% (standard temporal), 47.4% (external), 0.3% (sanity). ΔTPR=+0.818 (standard). DIF-C items systematically harder (mean difficulty 0.38 vs 0.61, p<0.001) — difficulty confound acknowledged.
- §4.5 Downstream Impact: ρ≈0.997 (ranking redundancy). Circularity ablation: DIF removal z=-9.5 (least disruptive non-random strategy). DIF-discrimination overlap Jaccard=0.12. Graceful degradation: critical threshold ∼23%, but DIF flag rate is 31% — tension acknowledged.
- §4.6 Alternative Methods: ConStat AUROC 0.78 (non-RL) vs DIF 0.73, FPR 0.067 vs 0.314 — ConStat better on non-RL. DVD AUROC 0.69 (verbatim), 0.58 (variant), bimodal only 23%. IFT: FPR 0.088, TPR 0.59 vs MH 0.68, overfitting CV gap 0.12, 8/12 splits unstable. Ensemble: weighted AUROC 0.76 < ConStat alone 0.78, DeLong p=0.38, CV fold variance 0.034, 3/8 configs exceed FPR 0.10.
- §5.1 Negative Results: RL robustness (N=13, AUROC 0.82→0.64, bootstrap CI [0.41,0.84], TOST p=0.31). Bifactor IRT (CFI=0.72, TLI=0.69, failed convergence, score equivalence fails at all levels). LLM item generation (all 6 metrics FAIL). Bayesian cumulative DIF (power 0.63 at 4 admins vs 0.70 target, prior miscalibration compounds).
- §5.2 Key Limitations: IRT misspecification (98% |Lz|>2), no ground truth, temporal confounding, scalability of alternatives.

## Experiment Design Reference
The paper covers all 13 planned experiments from the design document. No planned experiment is missing from the paper.

## Your Task
Produce a thorough review focused on:
1. **Methodological soundness**: Are the methods (MH, SIBTEST, ΔTPR framework, cross-subject matching) correctly applied? Are statistical tests appropriate?
2. **Experimental rigor**: Are experiments well-designed? Are controls adequate? Are conclusions supported by the data?
3. **Internal consistency**: Do the results across experiments tell a coherent story?
4. **Weaknesses in methods/experiments**: What are the critical methodological gaps?

Your review must include:
- Summary (2-3 sentences)
- Strengths (bulleted list)
- Weaknesses (bulleted list, with severity: major/minor)
- Questions for Authors (numbered list)
- Scores: Soundness (1-4), Presentation (1-4), Contribution (1-4), Overall (1-10), Confidence (1-5)
- One paragraph justification of overall score

Be rigorous but fair. Do not mention any tier designation. Evaluate the paper on its own merits.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "a722f1afaa51a1652",
  "type": "user",
  "uuid": "5218e634-5a5b-48e4-b2ce-15850a93ac5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T05:31:50.552Z_

```json
{
  "parentUuid": "5218e634-5a5b-48e4-b2ce-15850a93ac5d",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
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
  "uuid": "7bb12c6d-3f81-4747-b6fb-bcf9ea2b6b31",
  "timestamp": "2026-05-21T05:31:50.552Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-21T05:31:53.389Z_



I'll read the paper to produce a thorough review. Let me start by examining the full manuscript.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bb12c6d-3f81-4747-b6fb-bcf9ea2b6b31",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAc3NSvhMtT9tjpWgv2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad86edc6-6b66-433d-b08d-d812e1a2c2ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LPDDKJhS1st3jc8cn7UAAF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16431,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16431,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 4 · 2026-05-21T05:31:55.975Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0131PkkaQ9wapMsVbFVpw2YV`</summary>

```json
{
  "pattern": "paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad86edc6-6b66-433d-b08d-d812e1a2c2ec",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAc3NSvhMtT9tjpWgv2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bcc9db9f-714e-4a2a-b3f3-804f156eebd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LPDDKJhS1st3jc8cn7UAAF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16431,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16431,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 5 · 2026-05-21T05:31:55.993Z_

<details><summary>↩ Tool result · `toolu_0131PkkaQ9wapMsVbFVpw2YV`</summary>

```text
paper/math_commands.tex
paper/main.tex
paper/sections/introduction.tex
paper/sections/related_work.tex
paper/sections/discussion.tex
paper/sections/abstract.tex
paper/sections/conclusion.tex
paper/sections/appendix.tex
paper/sections/method.tex
paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcc9db9f-714e-4a2a-b3f3-804f156eebd7",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "a722f1afaa51a1652",
  "type": "user",
  "uuid": "d1857b61-bea6-49ef-85e5-04b632d6f520",
  "sourceToolAssistantUUID": "bcc9db9f-714e-4a2a-b3f3-804f156eebd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T05:31:56.067Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01PFhe1cLuYCFdLcUrxX3PxM`</summary>

```json
{
  "pattern": "paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1857b61-bea6-49ef-85e5-04b632d6f520",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAc3NSvhMtT9tjpWgv2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "634c1e87-750c-4bc0-8031-9bf81b81139c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LPDDKJhS1st3jc8cn7UAAF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16431,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16431,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 7 · 2026-05-21T05:31:56.085Z_

<details><summary>↩ Tool result · `toolu_01PFhe1cLuYCFdLcUrxX3PxM`</summary>

```text
paper/math_commands.tex
paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "634c1e87-750c-4bc0-8031-9bf81b81139c",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "a722f1afaa51a1652",
  "type": "user",
  "uuid": "d9857474-a4f8-4d94-b730-70a7a101a0f4",
  "sourceToolAssistantUUID": "634c1e87-750c-4bc0-8031-9bf81b81139c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T05:32:03.103Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Rcki3K6SoQPopFaSoejNzd`</summary>

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
  "parentUuid": "d9857474-a4f8-4d94-b730-70a7a101a0f4",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAcTCQYTp3LWr2SxeXq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3bf870f8-c38f-4eeb-8685-4ee795bf053d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D51cngDjZB94PVskhhUxUh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 16431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1204,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 9 · 2026-05-21T05:32:03.115Z_

<details><summary>↩ Tool result · `toolu_01Rcki3K6SoQPopFaSoejNzd`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, a semi-synthetic validation framework, diagnostic checks, and statistical controls.
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
  "parentUuid": "3bf870f8-c38f-4eeb-8685-4ee795bf053d",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "a722f1afaa51a1652",
  "type": "user",
  "uuid": "2b269b8e-5722-4e83-acda-32790623ac32",
  "sourceToolAssistantUUID": "3bf870f8-c38f-4eeb-8685-4ee795bf053d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T05:32:03.635Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BLpAT4or3e5EH87sU4ubyH`</summary>

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
  "parentUuid": "2b269b8e-5722-4e83-acda-32790623ac32",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAcTCQYTp3LWr2SxeXq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b49f8c0e-2c7c-4e76-9787-3e3bd43ddc32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D51cngDjZB94PVskhhUxUh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 16431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1204,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 11 · 2026-05-21T05:32:03.642Z_

<details><summary>↩ Tool result · `toolu_01BLpAT4or3e5EH87sU4ubyH`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark replication on GSM8K appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	To confirm that MH-DIF detects differential item functioning at the sample sizes available in METABENCH, we conduct a power analysis using empirical MMLU IRT parameters. We simulate item response matrices where a controlled subset of items has injected DIF of varying magnitude ($|\Delta_{\mathrm{MH}}| \geq 1.4$) and evaluate ETS~C classification across sample sizes $N \in \{40, 80, 160, 320\}$ per cohort. At $N \geq 80$, ETS~C achieves true positive rates of 0.68--0.80 with false positive rates of 0.036--0.042 and AUC of 0.93--0.94. The temporal cohort sizes in our analysis ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold, and statistical power is not a limiting factor for the results reported below. Full simulation results with confidence intervals appear in Appendix~Table~A1.
10	
11	\subsection{Temporal Comparability: 31\% Item Instability}
12	\label{sec:temporal}
13	
14	The central finding of this paper is that a substantial fraction of MMLU items behave differently across model generations. Comparing models released in 2023 ($N = 1{,}080$) against models released in 2024 ($N = 807$), 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$). Applying Benjamini-Hochberg FDR correction at $q = 0.05$ reduces this from 31.32\% to 31.30\%, removing only 3 items. The minimal impact of FDR correction reflects the fact that the ETS classification system imposes a dual threshold on both effect size and statistical significance, which already provides implicit multiple-testing protection. In absolute terms, nearly one in three MMLU items exhibits a large shift in its statistical relationship to overall model ability between the two cohort periods.
15	
16	Three controls confirm this reflects genuine temporal change. A random split of the 2023 cohort yields only 0.18\% ETS~C items (sampling noise), and an ability-quintile comparison within the same temporal cohort yields 2.9\% (ability differences alone). A within-family comparison (Llama-2 vs.\ Llama-3) produces 61.3\% ETS~C items, elevated by large ability gaps that confound the DIF signal~\citep{holland1988mh}. The contrast between 2.9\% (ability-controlled) and 61.3\% (ability-confounded) brackets the temporal rate of 31.3\%.
17	
18	Within-subject analysis yields an average of 38.1\% ETS~C items across all five MMLU domains (range: 31--45\%). Despite an ecological correlation of $\rho = 0.307$ ($p = 0.02$) between subject-level C\% and accuracy improvement, item-level logistic regression reveals that domain accuracy improvement explains only 2.4 percentage points of 31.3\% C\% (pseudo $R^2 = 0.0007$; counterfactual C\% $= 29.0\%$). Thus 92.4\% of the instability reflects item-specific changes unrelated to aggregate domain-level gains. The qualitative conclusion is robust across ETS thresholds: C\% $= 48.9\%$ at $|\Delta_{\mathrm{MH}}| \geq 1.0$, $18.3\%$ at $\geq 2.0$, and $10.2\%$ at $\geq 2.5$. \Cref{tab:temporal_landscape} summarizes the DIF landscape across all cohort comparisons.
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
53	Three progressively refined approaches (matched-ability quintiles, IRT $\theta$-conditioning, within-subject DIF) all fail to reduce the temporal FPR below 0.31. $\theta$-conditioning achieves $r(\theta, \mathrm{total\ score}) = 0.9986$ yet FPR $= 0.312$, and within-subject C\% $= 38.1\%$ exceeds the 25\% bifactor viability threshold. Yen's Q3 diagnostic reveals mild local dependence within subjects (11.3\% of pairs exceed $|Q3| > 0.20$, vs.\ 2.2\% cross-subject; $p = 2.3 \times 10^{-9}$), but cross-subject matching addresses this bias and temporal C\% persists. \Cref{app:structural} reports full results.
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
68	Replication on GSM8K (1,319 items $\times$ 6,702 models) yields temporal C\% $= 18.9\%$ (sanity check: 0.3\%), with semi-synthetic $\Delta\mathrm{TPR} = {+}0.818$ at $p = 0.7$ (\Cref{app:gsm8k_details}). The GSM1K held-out set~\citep{zhang2024gsm1k} provides independent contamination validation: for $N = 33$ models, the correlation between contamination gap and DIF ranking advantage is $r = -0.478$ ($p = 0.005$; partial $r = -0.385$, $p = 0.027$ after controlling for accuracy). This \emph{negative} correlation contradicts the hypothesis that DIF items benefit contaminated models, and instead suggests that DIF captures genuine capability change distinct from memorization (\Cref{fig:gsm1k}). The result is suggestive at $N = 33$ and warrants replication.
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
  "parentUuid": "b49f8c0e-2c7c-4e76-9787-3e3bd43ddc32",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "a722f1afaa51a1652",
  "type": "user",
  "uuid": "bbc9d29b-7174-4886-b8c1-ad2bb3e12169",
  "sourceToolAssistantUUID": "b49f8c0e-2c7c-4e76-9787-3e3bd43ddc32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T05:32:03.962Z_

<details open><summary>🔧 Tool call — Read · `toolu_013ze1Br2GFTS8aSmrsTwGvB`</summary>

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
  "parentUuid": "bbc9d29b-7174-4886-b8c1-ad2bb3e12169",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAcTCQYTp3LWr2SxeXq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e9047aa-92a8-40cd-8930-807b5fe0a7e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D51cngDjZB94PVskhhUxUh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 16431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1204,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 13 · 2026-05-21T05:32:03.967Z_

<details><summary>↩ Tool result · `toolu_013ze1Br2GFTS8aSmrsTwGvB`</summary>

```text
1	\begin{abstract}
2	LLM benchmark scores are routinely compared across model generations, yet the assumption that individual items measure the same construct over time is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (DIF) analysis with ETS severity classification to the METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items), and find that 31\% of items exhibit large DIF (ETS Category~C) between 2023 and 2024 model cohorts. This instability does not threaten benchmark validity: Spearman rank correlation between full and stable-item rankings is $\rho \approx 0.997$. Rather, it reveals which capability dimensions shift across model generations. Item-level decomposition shows that domain accuracy improvement explains only 2.4 percentage points (7.6\%) of the instability; 92.4\% is item-specific. We expose a validation methodology gap in the contamination detection literature: web-overlap labels measure global exposure, not differential functioning, and the enrichment between DIF flags and these labels is 0.96 (chance level). A semi-synthetic injection framework with cross-subject matching achieves $\Delta\mathrm{FPR} = 0.000$ while preserving detection power ($\Delta\mathrm{TPR} = {+}0.508$ at exploitation rate $p = 0.5$); cross-benchmark replication on GSM8K confirms generality ($\Delta\mathrm{TPR} = {+}0.818$). DIF-flagged items concentrate cross-generational discriminative information ($z = -8$ to $-49\sigma$ vs.\ random removal) and anti-correlate with the GSM1K contamination gap ($r = -0.478$, $p = 0.005$, $N = 33$), suggesting that DIF captures genuine capability change rather than memorization. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e9047aa-92a8-40cd-8930-807b5fe0a7e7",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "a722f1afaa51a1652",
  "type": "user",
  "uuid": "0bba8acf-5db1-4df9-a9ad-a1c83b689d85",
  "sourceToolAssistantUUID": "1e9047aa-92a8-40cd-8930-807b5fe0a7e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T05:32:04.431Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C9UbAwehq4yj5e5R67Uhei`</summary>

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
  "parentUuid": "0bba8acf-5db1-4df9-a9ad-a1c83b689d85",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAcTCQYTp3LWr2SxeXq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27a993ab-7867-4ebb-a920-5aa7462370ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D51cngDjZB94PVskhhUxUh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 16431,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1204
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 317,
          "cache_read_input_tokens": 16431,
          "cache_creation_input_tokens": 1204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1204,
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

_source line 15 · 2026-05-21T05:32:04.436Z_

<details><summary>↩ Tool result · `toolu_01C9UbAwehq4yj5e5R67Uhei`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. Applying Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench}, we find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. The instability persists within every MMLU subject domain, with domain-level C\% ranging from 31\% to 45\% (mean 38.1\%), and item-level regression shows that 92.4\% of this instability is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained. Crucially, this instability does not threaten benchmark validity: Spearman rank correlation between model rankings computed on all items versus stable-only items is $\rho \approx 0.997$. The instability is diagnostic, not destructive; it reveals which capability dimensions shift across model generations rather than rendering MMLU scores unreliable.
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
15	We apply classical MH-DIF with ETS classification to the full METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date. This psychometric approach complements concurrent work on anchor-item calibration for score comparability~\citep{habba2026growingpains} and addresses the fragility of existing contamination detectors under post-training perturbation~\citep{wang2026fragility}. Semi-synthetic injection experiments confirm that DIF detects differential contamination when present ($\Delta\mathrm{TPR} = {+}0.508$ at exploitation rate $p = 0.5$), and our cross-subject matching protocol eliminates false positive inflation ($\Delta\mathrm{FPR} = 0.000$). Three structural controls (matched-ability quintile analysis, IRT $\theta$-conditioning, and within-subject pre-checks) confirm that the 31\% temporal instability cannot be attributed to methodological artifacts, establishing it as a robust empirical finding about MMLU's measurement properties.
16	
17	MMLU's 12,508 items provide sufficient measurement redundancy that removing nearly a third does not alter rank order. DIF should therefore be understood as a diagnostic lens (which items changed and for which model families) rather than a quality filter (remove bad items to improve the benchmark). Despite aggregate ranking stability, DIF-flagged items concentrate discriminative signal that differentiates model generations: removing DIF items degrades ranking discriminability more than removing an equal number of random items ($z = -8$ to $-49\sigma$ across 21 conditions). Individual model families show distinctive DIF profiles: Phi-3 and Llama-3 gain ${+}700$ to ${+}850$ rank positions under stable-item evaluation, while Mistral-based merges lose $-400$ to $-587$ positions.
18	
19	We do not modify the MH-DIF procedure itself; the contributions are empirical, not algorithmic. Three layers of genuine novelty emerge: (a)~we discover that 31\% temporal instability is robust across thresholds and unrelated to capability improvement, the first large-scale characterization of item-level benchmark stability at 5,227 models; (b)~we expose a fundamental validation methodology gap in the contamination detection literature, showing that web-overlap labels cannot serve as ground truth for item-level differential detectors; and (c)~we provide a reusable semi-synthetic validation framework with cross-subject matching ($\Delta\mathrm{FPR} = 0.000$), confirmed on GSM8K with independent contamination validation through the GSM1K held-out set~\citep{zhang2024gsm1k}. We make the following contributions:
20	
21	\begin{enumerate}
22	\item \textbf{Benchmark temporal comparability} (Claim 1): 31\% of MMLU items are functionally unstable across model generations under ETS~C classification, with the instability persisting within every subject domain (mean C\% $= 38.1\%$) and confirmed non-random by random-split control at 0.18\% (\Cref{sec:temporal}).
23	
24	\item \textbf{Ground truth meta-critique} (Claim 2): Web-overlap contamination labels~\citep{li2024contamination} cannot evaluate item-level differential detectors. The enrichment between DIF flags and web-overlap labels is 0.96 (chance level), exposing a validation methodology gap in the contamination detection literature (\Cref{sec:groundtruth}).
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
  "parentUuid": "27a993ab-7867-4ebb-a920-5aa7462370ca",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "a722f1afaa51a1652",
  "type": "user",
  "uuid": "18795268-13a9-4b54-8c06-e6f61cd35030",
  "sourceToolAssistantUUID": "27a993ab-7867-4ebb-a920-5aa7462370ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T05:32:08.840Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UNXghA9TEf9zE1ez7vU7HN`</summary>

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
  "parentUuid": "18795268-13a9-4b54-8c06-e6f61cd35030",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAd4wyQUA9imj9GDJei",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bab7a0e1-f95c-4871-a74f-6f0f728abf8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9ih8zrGzVWfi9GALaxBWu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8407,
      "cache_read_input_tokens": 17635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8407,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 17 · 2026-05-21T05:32:08.845Z_

<details><summary>↩ Tool result · `toolu_01UNXghA9TEf9zE1ez7vU7HN`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Implications for Benchmark Temporal Comparability}
5	\label{sec:disc_temporal}
6	
7	The 31\% ETS~C instability rate is robust across thresholds (10\% at $|\Delta_{\mathrm{MH}}| \geq 2.5$, rising to 49\% at $\geq 1.0$), and three structural controls (\Cref{sec:structural}) confirm it is not a methodological artifact. This means that cross-generation MMLU score comparisons carry uncontrolled item-level variance: nearly one in three items functions differently depending on when the evaluated model was trained. The instability decomposition (\Cref{sec:temporal}) sharpens this interpretation. Domain-level accuracy improvement explains only 2.4 percentage points of the 31.3\% C\% (pseudo $R^2 = 0.0007$), so 92.4\% of the instability is unrelated to aggregate capability gains. The items that change are not simply the ones that newer models answer correctly because they are better at a domain; instead, they change in item-specific ways that domain-level trends do not predict.
8	
9	This instability does not invalidate MMLU as a ranking instrument. Spearman $\rho \approx 0.997$ between full and stable-item rankings confirms that aggregate model ordering is preserved. The instability is diagnostic, not destructive: it identifies which measurement units shift across model generations without rendering the overall score unreliable. Benchmark designers should therefore consider monitoring DIF as a quality diagnostic alongside accuracy metrics. An item pool where C\% grows over successive model cohorts signals that the benchmark's measurement properties are drifting, even if rank ordering remains intact.
10	
11	\subsection{Ground Truth Meta-Critique}
12	\label{sec:disc_groundtruth}
13	
14	The near-chance enrichment (0.96) between DIF flags and web-overlap labels raises a question that extends beyond our specific analysis. All prior work that validates item-level contamination detectors against web-overlap or $n$-gram labels faces the same methodological gap: these labels measure whether an item exists in publicly accessible training corpora, not whether exposure differentially affects model behavior. Global exposure is a property of the data ecosystem; differential functioning is a property of how model cohorts interact with individual items. Most MMLU items are globally contaminated in the sense that they appear in web text, so web-overlap labels identify a condition shared by nearly all items rather than one that differentiates model cohorts. Validating differential detectors against such labels conflates two distinct phenomena.
15	
16	This observation constitutes a meta-contribution to the contamination detection literature. The enrichment ratio of $\approx 1.0$ is not evidence that DIF fails; it is the expected outcome when a differential method is evaluated against a global-exposure reference. Semi-synthetic injection confirms that DIF detects differential contamination when present ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \Cref{sec:semisynthetic}). The field needs validation methodologies that match the granularity of the detection task: item-level differential detectors require item-level differential ground truth, not item-level global-exposure labels.
17	
18	\subsection{DIF as Diagnostic Lens}
19	\label{sec:disc_diagnostic}
20	
21	\paragraph{Capability diagnostic.} The GSM1K correlation ($r = -0.478$, $p = 0.005$, $N = 33$; \Cref{sec:gsm8k}) provides evidence that DIF-flagged items capture behavioral change distinct from memorization. Models with larger contamination gaps (higher GSM8K minus GSM1K accuracy) benefit \emph{less} from DIF-C items, the opposite of what a pure memorization account would predict. Of the 249 focal-favoring DIF-C items, 171 have discrimination $\alpha < 1$, and the negative correlation concentrates in this low-discrimination subset. This pattern suggests that contamination produces a ``shallow'' performance boost on items that DIF does not flag, while DIF-C items capture genuine capability differences that contamination does not confer. Partial correlation ($r = -0.385$, $p = 0.027$) after controlling for overall accuracy confirms that the effect is not an artifact of general model quality. Several caveats apply: the confidence interval is wide (95\% CI $= [-0.71, -0.16]$), item difficulty as a confound is not fully excluded, and $N = 33$ limits generalizability. This result is suggestive and warrants replication with larger model populations.
22	
23	\paragraph{Structural constraints on DIF applicability.} Systematic experimentation reveals three structural constraints that jointly limit DIF utility in LLM benchmarks. First, 1D IRT model fit is imperfect: MMLU's multi-domain structure produces mild local dependence (11.3\% of within-subject item pairs exceed $|Q3| > 0.20$; \Cref{sec:structural}), which elevates within-subject DIF rates relative to cross-subject baselines. Second, the power analysis (\Cref{sec:validation}) establishes minimum requirements of $N \geq 80$ per cohort and $|\Delta_{\mathrm{MH}}| \geq 1.4$ for reliable detection. Benchmarks with small model populations or modest effect sizes will lack statistical power for DIF analysis. Third, ability differences between temporal cohorts confound the DIF signal: the within-family comparison (Llama-2 vs.\ Llama-3) produces 61.3\% C\%, elevated above the 31.3\% temporal rate by the large ability gap between model generations. These are structural constraints revealed by our experimentation, not fundamental impossibilities. Higher-level methods (MIMIC models, propensity-score matching, multidimensional IRT) may address individual constraints, and their investigation on LLM benchmark data is a natural next step.
24	
25	\subsection{Limitations}
26	\label{sec:disc_limitations}
27	
28	\paragraph{(a) Ecological vs.\ item-level decomposition.} The ecological correlation between subject-level C\% and accuracy improvement is $\rho = 0.307$ ($p = 0.02$), but item-level decomposition shows that domain improvement explains only 2.4 percentage points (7.6\%) of 31.3\% C\%. The remaining 92.4\% cannot be fully attributed to contamination; other sources of capability change (training methodology, data composition, optimization procedures) may contribute, and our analysis does not isolate these factors.
29	
30	\paragraph{(b) Instability attribution.} The 31\% C\% measures items that function differently across cohorts, but the method does not distinguish contamination from legitimate capability change. DIF identifies \emph{that} items changed, not \emph{why}. The semi-synthetic framework validates detection power for one specific mechanism (differential exposure), but real-world instability likely reflects multiple interacting causes.
31	
32	\paragraph{(c) Semi-synthetic injection fidelity.} The injection procedure flips incorrect responses to correct at a specified rate, simulating an idealized contamination scenario. Real contamination may manifest as partial knowledge, format memorization, or selective retrieval rather than wholesale answer flipping. The gap between our injection model and realistic contamination mechanisms is unknown.
33	
34	\paragraph{(d) Benchmark scope.} The primary analysis covers MMLU with cross-benchmark validation on GSM8K (\Cref{sec:gsm8k}). GSM8K replication confirms framework portability and provides the GSM1K contamination correlation ($N = 33$), but full temporal DIF characterization on diverse benchmarks (code generation, long-form reasoning, multimodal tasks) has not been conducted. The GSM1K sample ($N = 33$) produces wide confidence intervals that limit the precision of the negative correlation estimate.
35	
36	\paragraph{(e) Cross-subject baseline false positive rate.} The cross-subject matching protocol achieves $\Delta\mathrm{FPR} = 0.000$ for injected contamination but does not reduce the baseline temporal FPR of 33--53\% across subjects. This rate is stable across injection levels, confirming it reflects genuine temporal instability rather than methodological error, but it means that a large fraction of flagged items in temporal comparisons are not attributable to the specific contamination mechanism under test.
37	
38	\paragraph{(f) RL model robustness.} Reinforcement learning from human feedback may alter item-level response patterns in ways that differ from pretraining-based contamination. The theoretical motivation for DIF robustness to RL (RL modifies the ability distribution rather than item parameters) is plausible but empirically unvalidated with adequate sample size: METABENCH contains only $N = 13$ models with documented reasoning-RL training.
39	
40	\paragraph{(g) Model family coverage.} Downstream impact analysis is limited to families with $N \geq 20$ models (Llama, Mistral, Qwen, Phi). Among the top 50 rank movers, 49 of 50 belong to the ``unknown'' family category in METABENCH, precluding interpretation of what training choices produce large rank shifts.
41	
42	\paragraph{(h) Future directions.} Cross-benchmark generalization to code, multimodal, and long-form reasoning benchmarks would test DIF applicability beyond factual knowledge tasks. RL model cohorts with adequate $N$ would enable empirical validation of the RL robustness hypothesis. MIMIC models and propensity-score matching could address the ability confounding that the current MH-DIF framework does not fully resolve.
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bab7a0e1-f95c-4871-a74f-6f0f728abf8b",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "a722f1afaa51a1652",
  "type": "user",
  "uuid": "6cf55f27-9611-4b64-bda8-9b69d7d2d1ea",
  "sourceToolAssistantUUID": "bab7a0e1-f95c-4871-a74f-6f0f728abf8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T05:32:09.802Z_

<details open><summary>🔧 Tool call — Read · `toolu_017sdfwCqbbybxniPxnHqb7X`</summary>

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
  "parentUuid": "6cf55f27-9611-4b64-bda8-9b69d7d2d1ea",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAd4wyQUA9imj9GDJei",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff640313-4830-4452-807e-d676f7f95bd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9ih8zrGzVWfi9GALaxBWu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8407,
      "cache_read_input_tokens": 17635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8407,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 19 · 2026-05-21T05:32:09.807Z_

<details><summary>↩ Tool result · `toolu_017sdfwCqbbybxniPxnHqb7X`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination Detection.}
5	A growing family of methods detects benchmark contamination through model behavior or training data analysis. Membership inference approaches estimate whether a model has seen specific items during training: Min-K\% \citep{shi2024mink} and Min-K\%++ \citep{zhang2024minkpp} use token-level log-likelihood statistics, while Time Travel \citep{golchin2024timetravel} probes models with temporal cues. Performance-based detectors identify contamination through statistical anomalies: ConStat \citep{dekoninck2024constat} tests performance gaps between original and perturbed items, DVD \citep{liang2026dvd} uses distributional verification, and Self-Critique \citep{tao2026selfcritique} employs model self-evaluation. \citet{balloccu2024leak} provide a broader taxonomy of leakage detection strategies. These methods share a common validation practice: they verify detection accuracy against web-overlap or n-gram labels \citep{li2024contamination} that classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure} (whether an item exists in training data) rather than \emph{differential item functioning} (whether an item behaves differently across model cohorts). This distinction is central to our Claim~2 (\Cref{sec:groundtruth}): web-overlap labels cannot serve as ground truth for differential detectors, because most benchmark items are globally exposed to all model cohorts. \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, which further motivates behavioral approaches grounded in psychometric theory rather than NLL-based signals.
6	
7	\paragraph{IRT in LLM Evaluation.}
8	Item Response Theory (IRT) provides a principled framework for jointly analyzing test items and examinee ability, and its adoption in LLM evaluation has accelerated. \citet{lalor2019irt} introduced IRT to NLP by fitting item parameters to human and model response data; their analysis revealed that item difficulty and discrimination vary substantially across benchmark questions. \citet{vania2021irt} applied IRT to assess test set discriminability and found that many items in standard NLP benchmarks contribute little information about model differences. Recent extensions include PSN-IRT \citep{zhou2026psnirt}, which fits four-parameter logistic models to characterize benchmark quality at scale, and scalability coefficients \citep{hardy2026scalability} as lightweight item quality pre-filters. TinyBenchmarks \citep{maiapolo2024tinybenchmarks} uses IRT-based item selection to construct representative benchmark subsets that predict full-benchmark scores with far fewer items. ATLAS \citep{li2025atlas} and IRTNet \citep{chen2025irtnet} explore neural extensions of classical IRT for LLM ability estimation, and \citet{choi2026llmjudgeirt} apply IRT to calibrate LLM-as-judge evaluations.
9	
10	The closest concurrent work is Growing Pains \citep{habba2026growingpains}, which addresses score comparability across model generations through fixed-parameter calibration \citep[FPC;][]{kim2019fpc}. FPC anchors a common ability scale by fixing the item parameters of a shared anchor set, so that models calibrated at different times receive scores on the same metric. Their framework selects 100 anchor items with stable IRT parameters and calibrates new models against this fixed scale, which enables extensible evaluation without full re-calibration. Our work is complementary: Growing Pains assumes anchor item stability, while DIF analysis diagnoses which items violate this assumption. The combination yields a monitored extensible evaluation system: DIF flags anchor items whose functioning has degraded, and the calibration framework triggers re-selection when the stable anchor set shrinks below a validity threshold.
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
  "parentUuid": "ff640313-4830-4452-807e-d676f7f95bd8",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "a722f1afaa51a1652",
  "type": "user",
  "uuid": "f58fe886-a078-46f6-8902-6e687581d968",
  "sourceToolAssistantUUID": "ff640313-4830-4452-807e-d676f7f95bd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T05:32:10.188Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SUehGrqgvav42qtqHzfsVN`</summary>

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
  "parentUuid": "f58fe886-a078-46f6-8902-6e687581d968",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAd4wyQUA9imj9GDJei",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af87194d-8157-4ab0-aef6-8e6fc62c1d99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9ih8zrGzVWfi9GALaxBWu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8407,
      "cache_read_input_tokens": 17635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8407,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 21 · 2026-05-21T05:32:10.193Z_

<details><summary>↩ Tool result · `toolu_01SUehGrqgvav42qtqHzfsVN`</summary>

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
  "parentUuid": "af87194d-8157-4ab0-aef6-8e6fc62c1d99",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "a722f1afaa51a1652",
  "type": "user",
  "uuid": "4873258d-ee42-4cf7-8dff-5712c557f352",
  "sourceToolAssistantUUID": "af87194d-8157-4ab0-aef6-8e6fc62c1d99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T05:32:10.473Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AkG3wpmjeraUJLUyCyyq77`</summary>

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
  "parentUuid": "4873258d-ee42-4cf7-8dff-5712c557f352",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAd4wyQUA9imj9GDJei",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a52dc5e9-0e31-49e4-a048-df843a92c1c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9ih8zrGzVWfi9GALaxBWu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8407,
      "cache_read_input_tokens": 17635,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8407
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 320,
          "cache_read_input_tokens": 17635,
          "cache_creation_input_tokens": 8407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8407,
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

_source line 23 · 2026-05-21T05:32:10.478Z_

<details><summary>↩ Tool result · `toolu_01AkG3wpmjeraUJLUyCyyq77`</summary>

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
27	Three progressively refined approaches fail to reduce the temporal false positive rate below 31\%, revealing a structural property of the data rather than a methodological limitation. Matched-ability quintile analysis restricts comparisons to models of similar total score and yields enrichment ratios of 0.94--1.04, with temporal FPR unchanged at approximately 0.31. IRT $\theta$-conditioning with 20 ability strata achieves $r(\theta, \mathrm{total\ score}) = 0.9986$ and FPR $= 0.312$, confirming that the external total score already captures nearly all ability variance relevant to DIF computation. Within-subject DIF analysis, intended to isolate subject-specific effects, finds C\% $= 38.1\%$ across subjects, exceeding the 25\% threshold that would indicate viable bifactor structure. \Cref{tab:structural_comparison} summarizes these results.
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
87	\section{Limitations}
88	\label{app:limitations}
89	
90	\paragraph{(a) Ecological vs.\ item-level decomposition.} The ecological correlation between subject-level C\% and accuracy improvement is $\rho = 0.307$ ($p = 0.02$), but item-level decomposition shows that domain improvement explains only 2.4 percentage points (7.6\%) of 31.3\% C\%. The remaining 92.4\% cannot be fully attributed to contamination; other sources of capability change (training methodology, data composition, optimization procedures) may contribute, and our analysis does not isolate these factors.
91	
92	\paragraph{(b) Instability attribution.} The 31\% C\% measures items that function differently across cohorts, but the method does not distinguish contamination from legitimate capability change. DIF identifies \emph{that} items changed, not \emph{why}. The semi-synthetic framework validates detection power for one specific mechanism (differential exposure), but real-world instability likely reflects multiple interacting causes.
93	
94	\paragraph{(c) Semi-synthetic injection fidelity.} The injection procedure flips incorrect responses to correct at a specified rate, simulating an idealized contamination scenario. Real contamination may manifest as partial knowledge, format memorization, or selective retrieval rather than wholesale answer flipping. The gap between our injection model and realistic contamination mechanisms is unknown.
95	
96	\paragraph{(d) Benchmark scope.} The primary analysis covers MMLU with cross-benchmark validation on GSM8K (\Cref{sec:gsm8k}). GSM8K replication confirms framework portability and provides the GSM1K contamination correlation ($N = 33$), but full temporal DIF characterization on diverse benchmarks (code generation, long-form reasoning, multimodal tasks) has not been conducted. The GSM1K sample ($N = 33$) produces wide confidence intervals that limit the precision of the negative correlation estimate.
97	
98	\paragraph{(e) Cross-subject baseline false positive rate.} The cross-subject matching protocol achieves $\Delta\mathrm{FPR} = 0.000$ for injected contamination but does not reduce the baseline temporal FPR of 33--53\% across subjects. This rate is stable across injection levels, confirming it reflects genuine temporal instability rather than methodological error, but it means that a large fraction of flagged items in temporal comparisons are not attributable to the specific contamination mechanism under test.
99	
100	\paragraph{(f) RL model robustness.} Reinforcement learning from human feedback may alter item-level response patterns in ways that differ from pretraining-based contamination. The theoretical motivation for DIF robustness to RL (RL modifies the ability distribution rather than item parameters) is plausible but empirically unvalidated with adequate sample size: METABENCH contains only $N = 13$ models with documented reasoning-RL training.
101	
102	\paragraph{(g) Model family coverage.} Downstream impact analysis is limited to families with $N \geq 20$ models (Llama, Mistral, Qwen, Phi). Among the top 50 rank movers, 49 of 50 belong to the ``unknown'' family category in METABENCH, precluding interpretation of what training choices produce large rank shifts.
103	
104	\paragraph{(h) Future directions.} Cross-benchmark generalization to code, multimodal, and long-form reasoning benchmarks would test DIF applicability beyond factual knowledge tasks. RL model cohorts with adequate $N$ would enable empirical validation of the RL robustness hypothesis. MIMIC models and propensity-score matching could address the ability confounding that the current MH-DIF framework does not fully resolve.
105	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a52dc5e9-0e31-49e4-a048-df843a92c1c0",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "a722f1afaa51a1652",
  "type": "user",
  "uuid": "54634439-4eb0-4c04-abfd-2e61789b261b",
  "sourceToolAssistantUUID": "a52dc5e9-0e31-49e4-a048-df843a92c1c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-21T05:32:13.802Z_

Now let me also review the main.tex to understand the overall structure and any additional content referenced.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54634439-4eb0-4c04-abfd-2e61789b261b",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAdWswbCLvk6xC7DkMb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "492d36ba-8674-4eea-abe2-bc0e672acccf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018kE2F8S7Pvt8utKfsaSpro",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8452,
      "cache_read_input_tokens": 26042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8452,
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

_source line 25 · 2026-05-21T05:32:15.522Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MRRPYAiYHu1qUx3J1sf7ss`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "492d36ba-8674-4eea-abe2-bc0e672acccf",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAdWswbCLvk6xC7DkMb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f19e5fce-317b-4878-b0cd-756a262b5ed8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018kE2F8S7Pvt8utKfsaSpro",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8452,
      "cache_read_input_tokens": 26042,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8452
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 111,
          "cache_read_input_tokens": 26042,
          "cache_creation_input_tokens": 8452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8452,
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

_source line 26 · 2026-05-21T05:32:15.533Z_

<details><summary>↩ Tool result · `toolu_01MRRPYAiYHu1qUx3J1sf7ss`</summary>

```text
1	\documentclass{article}
2	\usepackage{iclr2026_conference,times}
3	\input{math_commands.tex}
4	
5	\usepackage{hyperref}
6	\usepackage{url}
7	\usepackage{booktabs}
8	\usepackage{graphicx}
9	\usepackage{xcolor}
10	\usepackage{microtype}
11	\usepackage{multirow}
12	\usepackage{subcaption}
13	\usepackage{cleveref}
14	
15	\graphicspath{{../figures/paper/}}
16	
17	\title{Psychometric Instability of LLM Benchmarks:\\Differential Item Functioning Reveals 31\% of MMLU Items\\Behave Differently Across Model Generations}
18	
19	%\iclrfinalcopy
20	
21	\newcommand{\fix}{\marginpar{FIX}}
22	\newcommand{\new}{\marginpar{NEW}}
23	
24	\begin{document}
25	
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\bibliography{references}
37	\bibliographystyle{iclr2026_conference}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f19e5fce-317b-4878-b0cd-756a262b5ed8",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "a722f1afaa51a1652",
  "type": "user",
  "uuid": "3a5c6737-722f-4f9d-b506-5219ece6bd2b",
  "sourceToolAssistantUUID": "f19e5fce-317b-4878-b0cd-756a262b5ed8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-21T05:32:19.862Z_

Now let me check the appendix more carefully for the additional experiments mentioned in the summary (SIBTEST, alternative methods, negative results, etc.).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a5c6737-722f-4f9d-b506-5219ece6bd2b",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAdtBc2KWdA2Nc8rM2w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "587f2bf8-d6a0-4af0-b50f-5f4e63c4a698",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DYiNZ5FRspFET7n7Uz1CGE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 544,
      "cache_read_input_tokens": 34494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 544,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 28 · 2026-05-21T05:32:20.268Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DNk6StFsya94YZ1dnExsG6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex",
  "offset": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "587f2bf8-d6a0-4af0-b50f-5f4e63c4a698",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAdtBc2KWdA2Nc8rM2w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4600df7-e9b1-4601-91f8-6405d3a705c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DYiNZ5FRspFET7n7Uz1CGE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 544,
      "cache_read_input_tokens": 34494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 544,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 29 · 2026-05-21T05:32:20.273Z_

<details><summary>↩ Tool result · `toolu_01DNk6StFsya94YZ1dnExsG6`</summary>

```text
100	\paragraph{(f) RL model robustness.} Reinforcement learning from human feedback may alter item-level response patterns in ways that differ from pretraining-based contamination. The theoretical motivation for DIF robustness to RL (RL modifies the ability distribution rather than item parameters) is plausible but empirically unvalidated with adequate sample size: METABENCH contains only $N = 13$ models with documented reasoning-RL training.
101	
102	\paragraph{(g) Model family coverage.} Downstream impact analysis is limited to families with $N \geq 20$ models (Llama, Mistral, Qwen, Phi). Among the top 50 rank movers, 49 of 50 belong to the ``unknown'' family category in METABENCH, precluding interpretation of what training choices produce large rank shifts.
103	
104	\paragraph{(h) Future directions.} Cross-benchmark generalization to code, multimodal, and long-form reasoning benchmarks would test DIF applicability beyond factual knowledge tasks. RL model cohorts with adequate $N$ would enable empirical validation of the RL robustness hypothesis. MIMIC models and propensity-score matching could address the ability confounding that the current MH-DIF framework does not fully resolve.
105	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4600df7-e9b1-4601-91f8-6405d3a705c5",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "a722f1afaa51a1652",
  "type": "user",
  "uuid": "84bd5ba0-8cc5-4449-a9e1-dbc1a0045375",
  "sourceToolAssistantUUID": "a4600df7-e9b1-4601-91f8-6405d3a705c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-21T05:32:23.355Z_

Now let me check whether the SIBTEST, alternative methods comparison, negative results, and other experiments from the summary appear elsewhere in the paper or were only planned but not included.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84bd5ba0-8cc5-4449-a9e1-dbc1a0045375",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAeEpKrnBcEesdoZJwg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99b915e9-937b-414d-85f6-a58437212397",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TPZMaSAQMydcBP686N4mBo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 457,
      "cache_read_input_tokens": 35038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 457,
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

_source line 31 · 2026-05-21T05:32:24.274Z_

<details open><summary>🔧 Tool call — Grep · `toolu_013m8Un1qBMqDRKjZkHfUzUL`</summary>

```json
{
  "pattern": "SIBTEST",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99b915e9-937b-414d-85f6-a58437212397",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAeEpKrnBcEesdoZJwg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19a640d2-7fe2-4f46-aeb1-d40d05e43807",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TPZMaSAQMydcBP686N4mBo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 457,
      "cache_read_input_tokens": 35038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 457,
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

_source line 32 · 2026-05-21T05:32:24.294Z_

<details><summary>↩ Tool result · `toolu_013m8Un1qBMqDRKjZkHfUzUL`</summary>

```text
paper/sections/related_work.tex:13:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19a640d2-7fe2-4f46-aeb1-d40d05e43807",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "a722f1afaa51a1652",
  "type": "user",
  "uuid": "15ad84a2-5b5b-4b6e-85eb-e4e9f61ae634",
  "sourceToolAssistantUUID": "19a640d2-7fe2-4f46-aeb1-d40d05e43807",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T05:32:25.534Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01BVzyMFDxJDdnSvUCSBwo7P`</summary>

```json
{
  "pattern": "ConStat|DVD|Item-Focused|ensemble|negative result|bifactor",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15ad84a2-5b5b-4b6e-85eb-e4e9f61ae634",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAeEpKrnBcEesdoZJwg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12a7e4fe-094c-47cc-9791-152280e5eed3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TPZMaSAQMydcBP686N4mBo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 457,
      "cache_read_input_tokens": 35038,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 457
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 281,
          "cache_read_input_tokens": 35038,
          "cache_creation_input_tokens": 457,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 457,
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

_source line 34 · 2026-05-21T05:32:25.554Z_

<details><summary>↩ Tool result · `toolu_01BVzyMFDxJDdnSvUCSBwo7P`</summary>

```text
paper/main.bbl:86:\newblock {ConStat}: Performance-based contamination detection in large
paper/main.bbl:210:\newblock {DVD}: Detection via variance of generation distribution for variant
paper/sections/related_work.tex:5:[Omitted long matching line]
paper/sections/experiments.tex:53:[Omitted long matching line]
paper/sections/appendix.tex:27:[Omitted long matching line]
paper/sections/introduction.tex:6:[Omitted long matching line]
paper/references.bib:15:  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},
paper/references.bib:40:  title         = {{DVD}: Detection via Variance of Generation Distribution for Variant Contamination},
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12a7e4fe-094c-47cc-9791-152280e5eed3",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "a722f1afaa51a1652",
  "type": "user",
  "uuid": "b1de3d93-97df-4da2-8f92-4154555f5cda",
  "sourceToolAssistantUUID": "12a7e4fe-094c-47cc-9791-152280e5eed3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-21T05:32:29.593Z_

The paper references ConStat and DVD but only in Related Work and Introduction. The detailed SIBTEST analysis, alternative methods comparison (Section 4.6), negative results (Section 5.1), and several other experiments described in the summary do not appear in the actual paper text. Let me verify this is the case -- the summary mentions sections that don't exist in the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1de3d93-97df-4da2-8f92-4154555f5cda",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAedt9wZkFZv6CNsyHV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "931f918a-8769-4f60-99fa-5d58e4354820",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012WaAobfNQ13FEAWCzjhUmk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 545,
      "cache_read_input_tokens": 35495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 545,
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

_source line 36 · 2026-05-21T05:32:31.073Z_

<details open><summary>🔧 Tool call — Grep · `toolu_015hFKFrNmS4SebwEUbyUDFR`</summary>

```json
{
  "pattern": "\\\\subsection|\\\\section",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "931f918a-8769-4f60-99fa-5d58e4354820",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAedt9wZkFZv6CNsyHV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a959dc67-7f86-4b72-9ece-9ad872f92c0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012WaAobfNQ13FEAWCzjhUmk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 545,
      "cache_read_input_tokens": 35495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 545,
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

_source line 37 · 2026-05-21T05:32:31.085Z_

<details><summary>↩ Tool result · `toolu_015hFKFrNmS4SebwEUbyUDFR`</summary>

```text
1:\section{Experiments}
6:\subsection{Validation: DIF Detection Power}
11:\subsection{Temporal Comparability: 31\% Item Instability}
38:\subsection{Ground Truth Mismatch}
50:\subsection{Structural Analysis}
55:\subsection{Semi-Synthetic Framework Validation}
60:\subsection{Downstream Impact}
65:\subsection{Cross-Benchmark Validation: GSM8K}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a959dc67-7f86-4b72-9ece-9ad872f92c0a",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "a722f1afaa51a1652",
  "type": "user",
  "uuid": "2fca3554-91c6-42c8-83ed-96d6ef71dadd",
  "sourceToolAssistantUUID": "a959dc67-7f86-4b72-9ece-9ad872f92c0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T05:32:31.627Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01NRoSnKyDdTEPvY16awKKiC`</summary>

```json
{
  "pattern": "\\\\subsection|\\\\section",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fca3554-91c6-42c8-83ed-96d6ef71dadd",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAedt9wZkFZv6CNsyHV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cbb326a7-8f33-4145-b127-df6716bf9df1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012WaAobfNQ13FEAWCzjhUmk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 545,
      "cache_read_input_tokens": 35495,
      "output_tokens": 327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 545
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 327,
          "cache_read_input_tokens": 35495,
          "cache_creation_input_tokens": 545,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 545,
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

_source line 39 · 2026-05-21T05:32:31.641Z_

<details><summary>↩ Tool result · `toolu_01NRoSnKyDdTEPvY16awKKiC`</summary>

```text
1:\section{Discussion}
4:\subsection{Implications for Benchmark Temporal Comparability}
11:\subsection{Ground Truth Meta-Critique}
18:\subsection{DIF as Diagnostic Lens}
25:\subsection{Limitations}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cbb326a7-8f33-4145-b127-df6716bf9df1",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "a722f1afaa51a1652",
  "type": "user",
  "uuid": "c969ca12-f216-42d7-8512-d831189e1cf5",
  "sourceToolAssistantUUID": "cbb326a7-8f33-4145-b127-df6716bf9df1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-21T05:32:34.803Z_

Now I have a thorough understanding of the paper. Let me also check the artifacts directory for any supplementary experimental results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c969ca12-f216-42d7-8512-d831189e1cf5",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAf52VZ6HJ86vmQfQnj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "330b4e2c-1c6a-4779-a605-0dd295559654",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjMqbHfCLC8phi4iMf525S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 552,
      "cache_read_input_tokens": 36040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 552,
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

_source line 41 · 2026-05-21T05:32:35.742Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01U5MJ7H4jHN6KrnfmUA8dmW`</summary>

```json
{
  "pattern": "artifacts/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "330b4e2c-1c6a-4779-a605-0dd295559654",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAf52VZ6HJ86vmQfQnj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebc15ee1-1f5d-464a-9961-73c15dafe3cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjMqbHfCLC8phi4iMf525S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 552,
      "cache_read_input_tokens": 36040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 552,
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

_source line 42 · 2026-05-21T05:32:35.768Z_

<details><summary>↩ Tool result · `toolu_01U5MJ7H4jHN6KrnfmUA8dmW`</summary>

```text
artifacts/metabench_data/benchmark-data/gsm8k_prompts.csv
artifacts/metabench_data/benchmark-data/hellaswag_prompts.csv
artifacts/metabench_data/benchmark-data/truthfulqa_prompts.csv
artifacts/metabench_data/benchmark-data/arc_prompts.csv
artifacts/metabench_data/benchmark-data/arc.csv
artifacts/metabench_data/benchmark-data/gsm8k.csv
artifacts/metabench_data/benchmark-data/hellaswag.csv
artifacts/metabench_data/benchmark-data/truthfulqa.csv
artifacts/metabench_data/benchmark-data/winogrande.csv
artifacts/metabench_data/benchmark-data/mmlu_abstract_algebra_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_abstract_algebra.csv
artifacts/metabench_data/benchmark-data/mmlu_anatomy_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_astronomy_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_anatomy.csv
artifacts/metabench_data/benchmark-data/mmlu_business_ethics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_astronomy.csv
artifacts/metabench_data/benchmark-data/mmlu_business_ethics.csv
artifacts/metabench_data/benchmark-data/mmlu_clinical_knowledge_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_clinical_knowledge.csv
artifacts/metabench_data/benchmark-data/mmlu_college_biology_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_college_chemistry_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_college_biology.csv
artifacts/metabench_data/benchmark-data/mmlu_college_chemistry.csv
artifacts/metabench_data/benchmark-data/mmlu_college_computer_science_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_college_computer_science.csv
artifacts/metabench_data/benchmark-data/mmlu_college_mathematics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_college_medicine_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_college_mathematics.csv
artifacts/metabench_data/benchmark-data/mmlu_college_physics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_college_medicine.csv
artifacts/metabench_data/benchmark-data/mmlu_college_physics.csv
artifacts/metabench_data/benchmark-data/mmlu_computer_security_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_computer_security.csv
artifacts/metabench_data/benchmark-data/mmlu_electrical_engineering_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_electrical_engineering.csv
artifacts/metabench_data/benchmark-data/mmlu_global_facts_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_global_facts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_chemistry_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_chemistry.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_computer_science_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_computer_science.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_european_history_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_european_history.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_geography_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_geography.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_macroeconomics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_macroeconomics.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_mathematics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_mathematics.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_physics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_physics.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_psychology_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_psychology.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_us_history_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_us_history.csv
artifacts/metabench_data/benchmark-data/mmlu_human_sexuality_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_human_sexuality.csv
artifacts/metabench_data/benchmark-data/mmlu_international_law_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_international_law.csv
artifacts/metabench_data/benchmark-data/mmlu_logical_fallacies_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_logical_fallacies.csv
artifacts/metabench_data/benchmark-data/mmlu_machine_learning_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_machine_learning.csv
artifacts/metabench_data/benchmark-data/mmlu_management_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_management.csv
artifacts/metabench_data/benchmark-data/mmlu_marketing_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_marketing.csv
artifacts/metabench_data/benchmark-data/mmlu_medical_genetics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_medical_genetics.csv
artifacts/metabench_data/benchmark-data/mmlu_miscellaneous_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_moral_disputes_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_miscellaneous.csv
artifacts/metabench_data/benchmark-data/mmlu_moral_disputes.csv
artifacts/metabench_data/benchmark-data/mmlu_moral_scenarios_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_moral_scenarios.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_accounting_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_accounting.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_law_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_law.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_medicine_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_medicine.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_psychology_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_psychology.csv
artifacts/metabench_data/benchmark-data/mmlu_public_relations_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_public_relations.csv
artifacts/metabench_data/benchmark-data/mmlu_security_studies_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_security_studies.csv
artifacts/metabench_data/benchmark-data/mmlu_us_foreign_policy_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_us_foreign_policy.csv
artifacts/metabench_data/benchmark-data/mmlu_virology_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_virology.csv
artifacts/metabench_data/benchmark-data/mmlu_world_religions_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_world_religions.csv
artifacts/metabench_data/benchmark-data/mmlu_econometrics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_econometrics.csv
artifacts/metabench_data/benchmark-data/mmlu_elementary_mathematics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_elementary_mathematics.csv
artifacts/metabench_data/benchmark-data/mmlu_conceptual_physics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_conceptual_physics.csv
artifacts/metabench_data/benchmark-data/mmlu_formal_logic_prompts.csv
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebc15ee1-1f5d-464a-9961-73c15dafe3cc",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "a722f1afaa51a1652",
  "type": "user",
  "uuid": "bc312f08-7dda-4398-b64b-fa1946797fe2",
  "sourceToolAssistantUUID": "ebc15ee1-1f5d-464a-9961-73c15dafe3cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-21T05:32:41.673Z_

I have now read all sections of the paper in detail. Let me now submit the review via the MCP tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc312f08-7dda-4398-b64b-fa1946797fe2",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAfPG78auHDCq8YwkTb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "390c14ae-f9cc-453e-a24f-e8e42effa61c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113YPLHyDqz8SDSPSQhhxtq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2429,
      "cache_read_input_tokens": 36592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2429,
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

_source line 44 · 2026-05-21T05:32:42.703Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Fz569ziPRCRKyNx6UfV1oE`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "390c14ae-f9cc-453e-a24f-e8e42effa61c",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAfPG78auHDCq8YwkTb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8a34c6f-f86a-4d13-87eb-3b38e5d2d2dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113YPLHyDqz8SDSPSQhhxtq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2429,
      "cache_read_input_tokens": 36592,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2429
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 114,
          "cache_read_input_tokens": 36592,
          "cache_creation_input_tokens": 2429,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2429,
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

_source line 45 · 2026-05-21T05:32:42.706Z_

<details><summary>↩ Tool result · `toolu_01Fz569ziPRCRKyNx6UfV1oE`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__submit_dream_review_report"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8a34c6f-f86a-4d13-87eb-3b38e5d2d2dd",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "a722f1afaa51a1652",
  "type": "user",
  "uuid": "c8c88564-231c-49bb-ab3f-c19fb6557ef8",
  "sourceToolAssistantUUID": "f8a34c6f-f86a-4d13-87eb-3b38e5d2d2dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-21T05:34:17.609Z_



Here is my review.

---

## ICLR Review: "Psychometric Instability of LLM Benchmarks: Differential Item Functioning Reveals 31% of MMLU Items Behave Differently Across Model Generations"

### Summary

This paper applies Mantel-Haenszel Differential Item Functioning (DIF) analysis from educational psychometrics to the METABENCH MMLU response matrix (5,227 models x 12,508 items), finding that 31% of items exhibit large DIF (ETS Category C) between 2023 and 2024 model cohorts. The authors argue this instability is diagnostic rather than destructive (rank correlation rho=0.997), expose a validation methodology gap in contamination detection (web-overlap labels measure global exposure, not differential functioning), and propose a semi-synthetic injection framework with cross-subject matching that eliminates false positive inflation.

### Strengths

- **Scale and data leverage.** The analysis operates on a uniquely large response matrix (5,227 models x 12,508 items), far exceeding typical educational testing applications. This scale lends credibility to the statistical findings and makes the 31% instability rate difficult to dismiss as noise, especially given the 0.18% random-split control.

- **Well-designed controls.** The battery of control conditions (random split, ability-quintile, within-family, architecture check) is thorough and methodologically sound. The random-split sanity check at 0.18% is particularly convincing as a null baseline, and the ability-quintile comparison at 2.9% effectively brackets the temporal signal.

- **Cross-subject matching is a genuine methodological insight.** The observation that within-subject matching inflates FPR by +0.186 because the matching variable absorbs injected signal, and the solution of conditioning on scores from other subjects, is a clean and well-motivated contribution. The resulting Delta-FPR = 0.000 is a strong validation result.

- **Ground truth meta-critique is well-argued.** The distinction between global exposure and differential functioning is conceptually precise and important. The argument that enrichment ~1.0 is the *expected* outcome when evaluating a differential detector against global-exposure labels is logically sound and has implications beyond this paper.

- **Honest about limitations.** The paper is unusually candid about what it cannot show: DIF identifies *that* items changed, not *why*; the semi-synthetic injection is a simplification; the GSM1K correlation is suggestive at N=33; the RL robustness claim is underpowered. This transparency is commendable.

- **Item-level decomposition.** The finding that domain accuracy improvement explains only 2.4 percentage points of the 31.3% C% (pseudo R^2 = 0.0007) is a valuable quantitative decomposition that rules out a simple "models got better at certain subjects" explanation.

- **Cross-benchmark replication.** The GSM8K replication (C% = 18.9%, sanity 0.3%, Delta-TPR = +0.818) demonstrates the framework is not MMLU-specific.

### Weaknesses

- **(Major) The temporal confound is insufficiently addressed.** The paper's central comparison (2023 vs. 2024 models) conflates at least three sources of variation: (1) differential data exposure/contamination, (2) genuine capability change from architectural and training improvements, and (3) shifts in the model population composition (e.g., different families, sizes, quantization levels entering the leaderboard). The ability-quintile control at 2.9% is presented as evidence that ability differences alone do not produce DIF, but this control operates within a single temporal window and cannot separate sources (1)-(3) when they co-occur across time. The within-family comparison (Llama-2 vs. Llama-3 at 61.3%) actually undermines the paper's narrative because it shows that genuine generational improvement within a single family produces *more* DIF than the temporal split, suggesting much of the 31% may reflect legitimate capability evolution rather than anything pathological. The paper acknowledges this ("elevated by large ability gaps that confound the DIF signal") but does not resolve it. This is the most fundamental interpretive limitation: we cannot tell whether the 31% instability is a measurement problem or simply a reflection of the fact that models genuinely changed.

- **(Major) The "instability" framing is potentially misleading.** DIF in educational testing is problematic because it indicates item bias -- items that unfairly advantage one demographic group after controlling for ability. In the LLM setting, "instability" is reframed as items that function differently across model generations. But if models genuinely acquired new capabilities (e.g., better chain-of-thought reasoning that helps on specific items), then differential item functioning is the *expected* and *desirable* outcome of progress, not evidence of measurement instability. The paper partially addresses this (rho=0.997 shows rankings are preserved, and the framing shifts to "diagnostic lens"), but the title and abstract still lead with "instability" language that implies something is wrong with the benchmark. The disconnect between the alarming headline (31% unstable) and the benign downstream impact (rho=0.997) suggests the finding may be less consequential than presented.

- **(Major) The semi-synthetic injection model has low ecological validity.** Flipping incorrect responses to correct at a uniform rate simulates an extreme and idealized contamination scenario. Real contamination operates through partial memorization, format priming, or selective retrieval -- mechanisms that produce graded, heterogeneous effects across items and models. The paper acknowledges this (Table 5 in the summary mentions HIGH/MEDIUM mismatch across multiple dimensions), but the validation framework's credibility rests entirely on this injection procedure. The Delta-FPR = 0.000 result is reassuring but may not hold under more realistic contamination models that produce correlated effects across items within a subject.

- **(Major) IRT model misspecification undermines the psychometric framing.** The paper reports that 97.8-98.1% of models have |Lz| > 2 (severe person misfit), CFI = 0.41, and RMSEA = 0.089 for the IRT model. These fit statistics indicate catastrophic misfit -- far worse than acceptable thresholds in psychometrics. The MH procedure does not require IRT model fit per se, but the paper's broader psychometric framing (discussing measurement properties, latent traits, item functioning) implicitly assumes that a unidimensional latent trait meaningfully characterizes these models. If 98% of models are misfitting, the "latent trait" theta is not capturing what models are doing, and the entire conceptual apparatus of "conditioning on ability" becomes questionable. The paper should either abandon the psychometric interpretation or confront the misfit directly.

- **(Minor) The paper described in the summary and the paper as written diverge substantially.** The summary references SIBTEST analysis, alternative method comparisons (ConStat, DVD, Item-Focused Trees), ensemble fusion, negative results (bifactor IRT equating, LLM item generation, Bayesian cumulative DIF), and a practitioner's guide -- none of which appear in the actual manuscript. Either the paper is incomplete or the summary describes planned work not yet written. This makes it difficult to evaluate several claimed contributions. I evaluate only what appears in the manuscript.

- **(Minor) The GSM1K correlation is over-interpreted.** At N=33, r=-0.478 has a 95% CI of [-0.71, -0.16] -- this spans from a strong to a weak effect. The paper appropriately calls it "suggestive," but it features prominently in the abstract, introduction, and conclusion as support for "DIF captures genuine capability change rather than memorization." This claim is not well-supported at this sample size, especially given the difficulty confound the paper acknowledges but does not resolve (DIF-C items are systematically harder, mean difficulty 0.38 vs 0.61).

- **(Minor) The Spearman rho=0.997 result weakens the practical motivation.** If removing 31% of items changes nothing about model rankings, then the instability is operationally irrelevant for the primary use case of benchmarks (ranking models). The paper reframes DIF as a "diagnostic lens," but the diagnostic value is never concretely demonstrated -- what actionable information does knowing which items have DIF provide to a practitioner? The paper does not show that DIF analysis leads to better benchmarks, better model selection, or better understanding of model capabilities in any concrete way.

- **(Minor) Missing comparison with simpler alternatives.** The paper does not compare DIF detection against simpler item-level statistics such as changes in item difficulty (p-value) across cohorts. If the item difficulty shift between 2023 and 2024 models correlates highly with DIF flags, then the psychometric machinery adds complexity without additional insight. This comparison would help establish whether the MH-DIF procedure provides information beyond what a naive difficulty-change analysis would yield.

- **(Minor) The circularity concern is not fully resolved.** DIF flags items that behave differently across cohorts. Removing those items and showing rho=0.997 could be circular if the DIF items are precisely those on which cohorts differ -- removing them mechanically reduces inter-cohort variance while preserving intra-cohort variance, producing high correlation by construction. The circularity ablation (z=-9.5, least disruptive non-random strategy) partially addresses this but does not fully resolve whether the high rho is a property of MMLU's redundancy or a property of DIF selecting non-informative items.

### Questions for Authors

1. What percentage of items show a simple difficulty shift (change in proportion correct) of comparable magnitude to the DIF effect sizes you observe? How does a naive "flag items whose difficulty changed by more than X" compare to MH-DIF in your semi-synthetic injection experiments?

2. The within-family comparison (Llama-2 vs. Llama-3) at 61.3% C% suggests that genuine capability improvement within a single lineage produces more DIF than your temporal split. How do you distinguish measurement instability from measurement sensitivity to genuine capability change?

3. Given that 98% of models show severe person-fit misfit (|Lz| > 2), what is the justification for interpreting the MH stratification (which conditions on total score as a proxy for theta) as meaningfully "controlling for ability"? Could the MH procedure be detecting differences in the multidimensional ability profile rather than item-level instability?

4. The cross-subject matching achieves Delta-FPR = 0.000, but the baseline temporal FPR remains at 31-53%. If you interpret the baseline FPR as "genuine temporal instability," how do you distinguish this from systematic differences in ability profiles across cohorts that the cross-subject total score does not capture?

5. What concrete, actionable recommendation follows from knowing that 31% of MMLU items have DIF? The paper frames DIF as a "diagnostic lens," but the diagnosis does not lead to a demonstrated remedy or improved evaluation practice.

6. The paper mentions that SIBTEST flags 44.7% of items with Jaccard overlap of only 0.48 with MH flags. Since SIBTEST detects both uniform and non-uniform DIF, does the low overlap suggest substantial non-uniform DIF that MH misses? What are the implications for the 31% headline number?

7. Could you provide the distribution of Delta-MH values rather than just the percentage exceeding the ETS-C threshold? A histogram would clarify whether the 31% represents a discrete population of unstable items or a tail of a continuous distribution.

### Scores

- **Soundness:** 2/4 -- The MH-DIF application is technically correct, but the interpretive framework is undermined by catastrophic IRT misfit, unresolved temporal confounding, and the gap between "differential item functioning" in the educational testing sense and what it means when applied to models that genuinely changed capabilities across generations.

- **Presentation:** 3/4 -- The paper is clearly written with well-organized sections and transparent limitations. The distinction between global and differential contamination is effectively communicated. Some over-reliance on the 31% headline number without sufficient nuance about what it means.

- **Contribution:** 2/4 -- The empirical finding (31% instability) is interesting but its practical significance is unclear given rho=0.997. The ground truth meta-critique is a genuine conceptual contribution. The semi-synthetic framework is useful but narrowly validated. The manuscript as written is missing several experiments referenced in the abstract/summary (SIBTEST comparison, alternative methods, negative results).

- **Overall:** 5/10

- **Confidence:** 4/5 -- I have strong familiarity with DIF methodology, IRT, and LLM evaluation. I am less certain about some specific details of the METABENCH dataset.

### Justification

The paper presents a large-scale empirical application of a well-established psychometric technique (MH-DIF) to LLM benchmarks, producing the finding that 31% of MMLU items exhibit differential functioning across model generations. The controls are well-designed, the ground truth meta-critique is conceptually valuable, and the cross-subject matching protocol is a genuine methodological contribution. However, the paper faces a fundamental interpretive challenge it does not resolve: differential item functioning in educational testing signals item bias (a measurement problem), but in the LLM setting it may simply reflect the fact that models changed in non-uniform ways across items (a measurement *success*). The catastrophic IRT misfit (98% of models with |Lz| > 2) undermines the psychometric conceptual apparatus, and the near-perfect rank correlation (rho=0.997) after removing DIF items makes the practical significance unclear. The semi-synthetic injection framework, while clean, validates only an idealized contamination mechanism. The manuscript as written is also missing several experiments described in the summary (SIBTEST analysis, alternative method comparisons, negative results), making it difficult to evaluate the full contribution. The paper is marginally below the acceptance threshold: the empirical observation is solid, but the interpretation and practical implications need strengthening.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8c88564-231c-49bb-ab3f-c19fb6557ef8",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAftZj2fFtQ9vZCpULd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f96f2020-06e2-41dd-9a52-97d0174c920e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NZaWwXBoT9yWEDE5bGn6Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 738,
      "cache_read_input_tokens": 39021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 738,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 47 · 2026-05-21T05:34:43.619Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01AGBrz2yxKvSVxENnMmGwrR`</summary>

```json
{
  "report": "# R1 Review: Methods & Experiments Focus\n\n## ICLR Review: \"Psychometric Instability of LLM Benchmarks: Differential Item Functioning Reveals 31% of MMLU Items Behave Differently Across Model Generations\"\n\n### Summary\n\nThis paper applies Mantel-Haenszel Differential Item Functioning (DIF) analysis from educational psychometrics to the METABENCH MMLU response matrix (5,227 models x 12,508 items), finding that 31% of items exhibit large DIF (ETS Category C) between 2023 and 2024 model cohorts. The authors argue this instability is diagnostic rather than destructive (rank correlation rho=0.997), expose a validation methodology gap in contamination detection (web-overlap labels measure global exposure, not differential functioning), and propose a semi-synthetic injection framework with cross-subject matching that eliminates false positive inflation.\n\n### Strengths\n\n- **Scale and data leverage.** The analysis operates on a uniquely large response matrix (5,227 models x 12,508 items), far exceeding typical educational testing applications. This scale lends credibility to the statistical findings and makes the 31% instability rate difficult to dismiss as noise, especially given the 0.18% random-split control.\n\n- **Well-designed controls.** The battery of control conditions (random split, ability-quintile, within-family, architecture check) is thorough and methodologically sound. The random-split sanity check at 0.18% is particularly convincing as a null baseline, and the ability-quintile comparison at 2.9% effectively brackets the temporal signal.\n\n- **Cross-subject matching is a genuine methodological insight.** The observation that within-subject matching inflates FPR by +0.186 because the matching variable absorbs injected signal, and the solution of conditioning on scores from other subjects, is a clean and well-motivated contribution. The resulting Delta-FPR = 0.000 is a strong validation result.\n\n- **Ground truth meta-critique is well-argued.** The distinction between global exposure and differential functioning is conceptually precise and important. The argument that enrichment ~1.0 is the *expected* outcome when evaluating a differential detector against global-exposure labels is logically sound and has implications beyond this paper.\n\n- **Honest about limitations.** The paper is unusually candid about what it cannot show: DIF identifies *that* items changed, not *why*; the semi-synthetic injection is a simplification; the GSM1K correlation is suggestive at N=33; the RL robustness claim is underpowered. This transparency is commendable.\n\n- **Item-level decomposition.** The finding that domain accuracy improvement explains only 2.4 percentage points of the 31.3% C% (pseudo R^2 = 0.0007) is a valuable quantitative decomposition that rules out a simple \"models got better at certain subjects\" explanation.\n\n- **Cross-benchmark replication.** The GSM8K replication (C% = 18.9%, sanity 0.3%, Delta-TPR = +0.818) demonstrates the framework is not MMLU-specific.\n\n### Weaknesses\n\n- **(Major) The temporal confound is insufficiently addressed.** The paper's central comparison (2023 vs. 2024 models) conflates at least three sources of variation: (1) differential data exposure/contamination, (2) genuine capability change from architectural and training improvements, and (3) shifts in the model population composition (e.g., different families, sizes, quantization levels entering the leaderboard). The ability-quintile control at 2.9% is presented as evidence that ability differences alone do not produce DIF, but this control operates within a single temporal window and cannot separate sources (1)-(3) when they co-occur across time. The within-family comparison (Llama-2 vs. Llama-3 at 61.3%) actually undermines the paper's narrative because it shows that genuine generational improvement within a single family produces *more* DIF than the temporal split, suggesting much of the 31% may reflect legitimate capability evolution rather than anything pathological. The paper acknowledges this (\"elevated by large ability gaps that confound the DIF signal\") but does not resolve it. This is the most fundamental interpretive limitation: we cannot tell whether the 31% instability is a measurement problem or simply a reflection of the fact that models genuinely changed.\n\n- **(Major) The \"instability\" framing is potentially misleading.** DIF in educational testing is problematic because it indicates item bias -- items that unfairly advantage one demographic group after controlling for ability. In the LLM setting, \"instability\" is reframed as items that function differently across model generations. But if models genuinely acquired new capabilities (e.g., better chain-of-thought reasoning that helps on specific items), then differential item functioning is the *expected* and *desirable* outcome of progress, not evidence of measurement instability. The paper partially addresses this (rho=0.997 shows rankings are preserved, and the framing shifts to \"diagnostic lens\"), but the title and abstract still lead with \"instability\" language that implies something is wrong with the benchmark. The disconnect between the alarming headline (31% unstable) and the benign downstream impact (rho=0.997) suggests the finding may be less consequential than presented.\n\n- **(Major) The semi-synthetic injection model has low ecological validity.** Flipping incorrect responses to correct at a uniform rate simulates an extreme and idealized contamination scenario. Real contamination operates through partial memorization, format priming, or selective retrieval -- mechanisms that produce graded, heterogeneous effects across items and models. The paper acknowledges this (HIGH/MEDIUM mismatch across multiple dimensions), but the validation framework's credibility rests entirely on this injection procedure. The Delta-FPR = 0.000 result is reassuring but may not hold under more realistic contamination models that produce correlated effects across items within a subject.\n\n- **(Major) IRT model misspecification undermines the psychometric framing.** The paper reports that 97.8-98.1% of models have |Lz| > 2 (severe person misfit), CFI = 0.41, and RMSEA = 0.089 for the IRT model. These fit statistics indicate catastrophic misfit -- far worse than acceptable thresholds in psychometrics. The MH procedure does not require IRT model fit per se, but the paper's broader psychometric framing (discussing measurement properties, latent traits, item functioning) implicitly assumes that a unidimensional latent trait meaningfully characterizes these models. If 98% of models are misfitting, the \"latent trait\" theta is not capturing what models are doing, and the entire conceptual apparatus of \"conditioning on ability\" becomes questionable. The paper should either abandon the psychometric interpretation or confront the misfit directly.\n\n- **(Minor) The paper described in the summary and the paper as written diverge substantially.** The summary references SIBTEST analysis, alternative method comparisons (ConStat, DVD, Item-Focused Trees), ensemble fusion, negative results (bifactor IRT equating, LLM item generation, Bayesian cumulative DIF), and a practitioner's guide -- none of which appear in the actual manuscript. Either the paper is incomplete or the summary describes planned work not yet written. This makes it difficult to evaluate several claimed contributions. I evaluate only what appears in the manuscript.\n\n- **(Minor) The GSM1K correlation is over-interpreted.** At N=33, r=-0.478 has a 95% CI of [-0.71, -0.16] -- this spans from a strong to a weak effect. The paper appropriately calls it \"suggestive,\" but it features prominently in the abstract, introduction, and conclusion as support for \"DIF captures genuine capability change rather than memorization.\" This claim is not well-supported at this sample size, especially given the difficulty confound the paper acknowledges but does not resolve (DIF-C items are systematically harder, mean difficulty 0.38 vs 0.61).\n\n- **(Minor) The Spearman rho=0.997 result weakens the practical motivation.** If removing 31% of items changes nothing about model rankings, then the instability is operationally irrelevant for the primary use case of benchmarks (ranking models). The paper reframes DIF as a \"diagnostic lens,\" but the diagnostic value is never concretely demonstrated -- what actionable information does knowing which items have DIF provide to a practitioner? The paper does not show that DIF analysis leads to better benchmarks, better model selection, or better understanding of model capabilities in any concrete way.\n\n- **(Minor) Missing comparison with simpler alternatives.** The paper does not compare DIF detection against simpler item-level statistics such as changes in item difficulty (p-value) across cohorts. If the item difficulty shift between 2023 and 2024 models correlates highly with DIF flags, then the psychometric machinery adds complexity without additional insight. This comparison would help establish whether the MH-DIF procedure provides information beyond what a naive difficulty-change analysis would yield.\n\n- **(Minor) The circularity concern is not fully resolved.** DIF flags items that behave differently across cohorts. Removing those items and showing rho=0.997 could be circular if the DIF items are precisely those on which cohorts differ -- removing them mechanically reduces inter-cohort variance while preserving intra-cohort variance, producing high correlation by construction. The circularity ablation (z=-9.5, least disruptive non-random strategy) partially addresses this but does not fully resolve whether the high rho is a property of MMLU's redundancy or a property of DIF selecting non-informative items.\n\n### Questions for Authors\n\n1. What percentage of items show a simple difficulty shift (change in proportion correct) of comparable magnitude to the DIF effect sizes you observe? How does a naive \"flag items whose difficulty changed by more than X\" compare to MH-DIF in your semi-synthetic injection experiments?\n\n2. The within-family comparison (Llama-2 vs. Llama-3) at 61.3% C% suggests that genuine capability improvement within a single lineage produces more DIF than your temporal split. How do you distinguish measurement instability from measurement sensitivity to genuine capability change?\n\n3. Given that 98% of models show severe person-fit misfit (|Lz| > 2), what is the justification for interpreting the MH stratification (which conditions on total score as a proxy for theta) as meaningfully \"controlling for ability\"? Could the MH procedure be detecting differences in the multidimensional ability profile rather than item-level instability?\n\n4. The cross-subject matching achieves Delta-FPR = 0.000, but the baseline temporal FPR remains at 31-53%. If you interpret the baseline FPR as \"genuine temporal instability,\" how do you distinguish this from systematic differences in ability profiles across cohorts that the cross-subject total score does not capture?\n\n5. What concrete, actionable recommendation follows from knowing that 31% of MMLU items have DIF? The paper frames DIF as a \"diagnostic lens,\" but the diagnosis does not lead to a demonstrated remedy or improved evaluation practice.\n\n6. The paper mentions that SIBTEST flags 44.7% of items with Jaccard overlap of only 0.48 with MH flags. Since SIBTEST detects both uniform and non-uniform DIF, does the low overlap suggest substantial non-uniform DIF that MH misses? What are the implications for the 31% headline number?\n\n7. Could you provide the distribution of Delta-MH values rather than just the percentage exceeding the ETS-C threshold? A histogram would clarify whether the 31% represents a discrete population of unstable items or a tail of a continuous distribution.\n\n### Scores\n\n- **Soundness:** 2/4 -- The MH-DIF application is technically correct, but the interpretive framework is undermined by catastrophic IRT misfit, unresolved temporal confounding, and the gap between \"differential item functioning\" in the educational testing sense and what it means when applied to models that genuinely changed capabilities across generations.\n\n- **Presentation:** 3/4 -- The paper is clearly written with well-organized sections and transparent limitations. The distinction between global and differential contamination is effectively communicated. Some over-reliance on the 31% headline number without sufficient nuance about what it means.\n\n- **Contribution:** 2/4 -- The empirical finding (31% instability) is interesting but its practical significance is unclear given rho=0.997. The ground truth meta-critique is a genuine conceptual contribution. The semi-synthetic framework is useful but narrowly validated. The manuscript as written is missing several experiments referenced in the summary (SIBTEST comparison, alternative methods, negative results).\n\n- **Overall:** 5/10\n\n- **Confidence:** 4/5 -- I have strong familiarity with DIF methodology, IRT, and LLM evaluation. I am less certain about some specific details of the METABENCH dataset.\n\n### Justification\n\nThe paper presents a large-scale empirical application of a well-established psychometric technique (MH-DIF) to LLM benchmarks, producing the finding that 31% of MMLU items exhibit differential functioning across model generations. The controls are well-designed, the ground truth meta-critique is conceptually valuable, and the cross-subject matching protocol is a genuine methodological contribution. However, the paper faces a fundamental interpretive challenge it does not resolve: differential item functioning in educational testing signals item bias (a measurement problem), but in the LLM setting it may simply reflect the fact that models changed in non-uniform ways across items (a measurement *success*). The catastrophic IRT misfit (98% of models with |Lz| > 2) undermines the psychometric conceptual apparatus, and the near-perfect rank correlation (rho=0.997) after removing DIF items makes the practical significance unclear. The semi-synthetic injection framework, while clean, validates only an idealized contamination mechanism. The manuscript as written is also missing several experiments described in the summary (SIBTEST analysis, alternative method comparisons, negative results), making it difficult to evaluate the full contribution. The paper is marginally below the acceptance threshold: the empirical observation is solid, but the interpretation and practical implications need strengthening.",
  "project": "irt_equated_bench_regen",
  "tier": "best",
  "dream_id": "dream_review",
  "overall_score": "5 - Marginally Below Threshold"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f96f2020-06e2-41dd-9a52-97d0174c920e",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAftZj2fFtQ9vZCpULd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f240e3c-6700-49d5-8486-a34343ac0d3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NZaWwXBoT9yWEDE5bGn6Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 738,
      "cache_read_input_tokens": 39021,
      "output_tokens": 6705,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 738
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6705,
          "cache_read_input_tokens": 39021,
          "cache_creation_input_tokens": 738,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 738,
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

_source line 48 · 2026-05-21T05:34:47.923Z_

<details><summary>↩ Tool result · `toolu_01AGBrz2yxKvSVxENnMmGwrR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_review/best/review_report.md\", \"dream_id\": \"dream_review\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f240e3c-6700-49d5-8486-a34343ac0d3f",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "a722f1afaa51a1652",
  "type": "user",
  "uuid": "96a528f5-eb85-41a4-9cf4-66063dc52a86",
  "sourceToolAssistantUUID": "4f240e3c-6700-49d5-8486-a34343ac0d3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-21T05:34:59.184Z_

Review submitted. Here is a summary of the key findings:

**Overall Score: 5/10 (Marginally Below Threshold)**

**Core strengths:** Unprecedented scale (5,227 models x 12,508 items), well-designed control conditions (random split at 0.18% is a strong null baseline), the cross-subject matching protocol is a genuine methodological contribution (Delta-FPR = 0.000), and the ground truth meta-critique (global vs. differential contamination) is conceptually valuable with implications beyond this paper.

**Critical weaknesses identified:**

1. **Temporal confound unresolved.** The 31% instability cannot be separated from legitimate capability evolution. The within-family comparison (Llama-2 vs. Llama-3 at 61.3%) actually suggests genuine progress produces *more* DIF, undermining the "instability" interpretation.

2. **Misleading framing.** DIF in educational testing signals item bias; in the LLM setting it may simply reflect that models changed non-uniformly across items -- which is expected and desirable. The alarming 31% headline is undercut by rho=0.997 ranking preservation.

3. **Low ecological validity of injection framework.** Binary response flipping does not model real contamination mechanisms (partial memorization, format priming, selective retrieval).

4. **Catastrophic IRT misfit** (98% of models with |Lz| > 2, CFI=0.41) undermines the psychometric conceptual apparatus the paper depends on.

5. **Manuscript appears incomplete.** SIBTEST analysis, alternative method comparisons, negative results, and practitioner's guide referenced in the summary are absent from the paper text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96a528f5-eb85-41a4-9cf4-66063dc52a86",
  "isSidechain": true,
  "agentId": "a722f1afaa51a1652",
  "requestId": "req_011CbFAq7mUVZugLq1sm7Fbb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17126736-c32d-401d-9d50-c08864f24305",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RG468evUYFVyMgs1VVcxrf",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6829,
      "cache_read_input_tokens": 39759,
      "output_tokens": 395,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6829
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 395,
          "cache_read_input_tokens": 39759,
          "cache_creation_input_tokens": 6829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6829,
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
