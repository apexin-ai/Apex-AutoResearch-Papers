# Research conversation: Check numerical consistency across sections of a LaTeX paper. The paper is at /home/ubuntu/.agent-ml-research-idea_gen_0

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 1
- **Tool calls:** 23
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a569ab0c5adb84941.jsonl`
- **Structured JSON:** [`d15fd135f277a3e832d3.json`](../../sessions/d1/d15fd135f277a3e832d3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

59 recorded events

### User

_source line 1 · 2026-05-22T08:34:25.661Z_

Check numerical consistency across sections of a LaTeX paper. The paper is at /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/

Check these specific numbers appear consistently everywhere they're mentioned across main.tex (Abstract/Limitations), sections/introduction.tex, sections/experiments.tex, and sections/conclusion.tex:

1. α values: 0.14 (PIQA/reasoning), 0.15 (HellaSwag), 0.21 (ARC-Easy), 0.30 (LAMBADA/retrieval)
2. Jaccard: ≤ 0.10 (cross-architecture), ~0.33 (within-architecture), 3× gap
3. Theoretical maximum: 0.78--0.92
4. Normalized effect size: 6--7% (should NOT be 5--7% anywhere)
5. LAMBADA convergence: ρ = -1.0, p = .017, Bonferroni-adjusted p = .100, σ drops 79%, CI [-1.0, -0.7]
6. σ trajectory: 0.024 → 0.016 → 0.014 → 0.006 → 0.005
7. Majority vote: LAMBADA -0.2pp, ARC-Easy -1.1pp
8. Oracle accuracy: +7--14pp
9. Per-example disagreement: 15--45%
10. AUC: 0.70--0.74, disruption threshold variation 47%
11. Helped/hurt counts: GDN 462/615, RetNet 426/495, HGRN2 548/395

Search breadth: very thorough. Report any inconsistencies found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "554469b9-31b2-4fbb-9a2a-790e01a6debf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-22T08:34:27.085Z_

I'll systematically check the numerical consistency across all specified sections of the LaTeX paper. Let me start by reading the relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "554469b9-31b2-4fbb-9a2a-790e01a6debf",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJLWJRtvkFGrEfLXH99",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8f0aaa4b-02b1-47fc-bc5a-d89afb3c493c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015yBHYfvZ3iDNG8nXanmWF5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28040,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28040,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 3 · 2026-05-22T08:34:27.453Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FDmC2hCiFXZpedGnoaCUHW`</summary>

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
  "parentUuid": "8f0aaa4b-02b1-47fc-bc5a-d89afb3c493c",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJLWJRtvkFGrEfLXH99",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7b4bace5-4076-42d9-98ef-48603cee66ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015yBHYfvZ3iDNG8nXanmWF5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28040,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28040,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 4 · 2026-05-22T08:34:27.462Z_

<details><summary>↩ Tool result · `toolu_01FDmC2hCiFXZpedGnoaCUHW`</summary>

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
16	
17	\title{Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	When attention layers are added to linear recurrent architectures, they help and hurt almost entirely different examples across backbones: pairwise overlap among three controlled hybrid designs is at most 10\%, far below the 78--92\% theoretical maximum. Using the model zoo of \citet{wang2025hybrid} (three architectures, five attention ratios, two scales, single training runs per configuration), we decompose per-example effects on four benchmarks and find that this predictive multiplicity \citep{marx2020predictive} depends on task type ($\alpha = 0.14$ for reasoning, $0.30$ for retrieval) rather than attention dose. Aggregate convergence is task-specific: only LAMBADA provides exploratory evidence for monotonic variance reduction (Bonferroni-adjusted $p = .100$). On this benchmark, aggregate variance decreases gradually while per-example overlap saturates at the first attention level, a saturation pattern that generalizes to all four benchmarks regardless of aggregate convergence. A proof-of-concept majority vote across architectures fails to outperform the best individual model despite 15--45\% per-example disagreement, while oracle accuracy reveals 7--14\,pp of untapped complementarity, suggesting that architectures interchangeable by aggregate metrics may carry hidden consequences for per-example reliability.
26	\end{abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	
40	Our analysis has several limitations.
41	
42	\paragraph{Coverage and generalization.} We examine three architectures from one model zoo on four main benchmarks (two supplementary). The controlled design isolates architectural effects but limits generalization to other hybrid families. We compare only two scale points (340M, 1.3B).
43	
44	\paragraph{Single training runs.} Each configuration corresponds to a single training run; we cannot fully disentangle architectural from seed-specific effects, though the $3\times$ within- vs.\ cross-architecture Jaccard gap (\S\ref{ssec:decoupling}) provides proxy evidence. All per-example claims are conditioned on this limitation. With $n = 5$ attention ratios, the minimum achievable $p$-value is 0.017, contributing to LAMBADA's Bonferroni-adjusted $p = .100$ not reaching conventional significance.
45	
46	\paragraph{Pre-training only.} All models are evaluated without fine-tuning; per-example effects may not persist after task-specific adaptation. We evaluate only discrete accuracy; continuous metrics may reveal different multiplicity patterns.
47	
48	\section*{Ethics Statement}
49	
50	This work analyzes publicly available pretrained language models from the model zoo of \citet{wang2025hybrid}. No new data collection, human subjects research, or model training is involved. We identify per-example behavioral differences across architectures, which may inform practitioners about the limitations of aggregate benchmark comparisons but does not introduce new risks.
51	
52	\section*{Code and Data Availability}
53	
54	All models are from the publicly available model zoo of \citet{wang2025hybrid}. Our analysis code and per-example evaluation outputs will be released upon publication.
55	
56	\bibliography{references}
57	
58	\appendix
59	\input{sections/appendix}
60	
61	\end{document}
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b4bace5-4076-42d9-98ef-48603cee66ad",
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "2a941234-7576-4b93-9d66-a920fc7ef7e7",
  "sourceToolAssistantUUID": "7b4bace5-4076-42d9-98ef-48603cee66ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T08:34:27.597Z_

<details open><summary>🔧 Tool call — Read · `toolu_013BoQHbhWaZjhQPdtpvhn5x`</summary>

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
  "parentUuid": "2a941234-7576-4b93-9d66-a920fc7ef7e7",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJLWJRtvkFGrEfLXH99",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b3fa9c2f-cdc7-4360-b440-a593e2d953b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015yBHYfvZ3iDNG8nXanmWF5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28040,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28040,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 6 · 2026-05-22T08:34:27.606Z_

<details><summary>↩ Tool result · `toolu_013BoQHbhWaZjhQPdtpvhn5x`</summary>

```text
1	\section{Introduction}
2	
3	Hybrid recurrent architectures that appear equivalent by aggregate benchmarks affect nearly disjoint sets of individual examples: adding attention to three controlled linear recurrent backbones yields helped and hurt sets with at most 10\% pairwise overlap, approximately twice the independence baseline. This per-example divergence is invisible in aggregate metrics: on LAMBADA, cross-architecture standard deviation drops 79\% as attention increases (Bonferroni-adjusted $p = .100$; the heuristic BCa 95\% CI excludes zero), but each architecture reaches similar accuracy by gaining and losing accuracy on different inputs. Practitioners increasingly choose between recurrent backbones based on aggregate benchmark scores. Our results show that architectures scoring identically in aggregate may nonetheless differ on 15--45\% of individual predictions, meaning the choice of backbone is associated with which specific inputs a deployed system handles correctly.
4	
5	This tension arises in the context of a rapid architectural shift toward hybrid recurrent-attention models, which interleave attention layers within linear recurrent backbones. Jamba \citep{lieber2024jamba}, Griffin \citep{de2024griffin}, RWKV-6 \citep{peng2024eagle}, and RecurrentGemma \citep{botev2024recurrentgemma} each combine recurrence with attention using different mixing strategies. These systems now serve as production-grade alternatives to pure Transformers, and the practical question of how much attention to include is typically answered by comparing aggregate benchmark numbers. \citet{wang2025hybrid} provide a controlled model zoo spanning three recurrent architectures, five attention ratios, and two parameter scales, which enables systematic study of how attention allocation affects these hybrid designs.
6	
7	Most evaluations of hybrid architectures compare aggregate accuracy, which can mask per-example behavioral diversity. Prior work on predictive multiplicity \citep{marx2020predictive} and underspecification \citep{damour2022underspecification,mccoy2020berts} documents this risk for seed variation within a single architecture, but whether the phenomenon extends to architectural variation in hybrid recurrent models remains open. If architectures that score identically in aggregate behave differently on individual inputs, the choice of backbone carries hidden consequences for deployment reliability and ensemble construction.
8	
9	We present the first systematic per-example analysis of how attention affects cross-architecture agreement in hybrid recurrent models. Using the model zoo of \citet{wang2025hybrid}, we compare three architectures (GatedDeltaNet, RetNet, HGRN2) at five attention ratios (0\% to 25\%) and two scales (340M and 1.3B parameters). These three architectures represent distinct approaches to linear recurrence: gated delta rules, multi-scale exponential decay, and gated state expansion. We evaluate all 30 configurations on 10 benchmarks spanning retrieval, comprehension, reasoning, and mixed task categories. On four benchmarks (LAMBADA, $N = 5{,}153$; HellaSwag, $N = 10{,}042$; PIQA, $N = 1{,}838$; ARC-Easy, $N = 2{,}376$) we conduct per-example decompositions, classifying each example as helped, hurt, or unchanged when attention is added, and measure cross-architecture overlap using Jaccard similarity. Figure~\ref{fig:decoupling} previews our central result: aggregate convergence and per-example divergence follow different trajectories as attention ratio increases.
10	
11	\begin{figure}[t]
12	\centering
13	\includegraphics[width=\columnwidth]{figures/fig1_decoupling_hero.pdf}
14	\caption{Aggregate convergence and per-example divergence are decoupled. (a) Cross-architecture standard deviation on LAMBADA decreases gradually with attention ratio at 1.3B (solid) but partially rebounds at 340M (dashed). (b) Pairwise Jaccard similarity of per-example helped/hurt sets saturates at the first attention level (4\%) and remains flat.}
15	\label{fig:decoupling}
16	\end{figure}
17	
18	Our analysis yields two findings. First, per-example predictive multiplicity varies in magnitude across tasks, forming a task-dependent variation. The ambiguity $\alpha$ \citep{marx2020predictive} ranges from 0.14 (PIQA) through 0.15 (HellaSwag) and 0.21 (ARC-Easy) to 0.30 (LAMBADA), while pairwise Jaccard remains uniformly low ($\leq 0.10$, all $p < .01$). Within each benchmark, $\alpha$ is stable across attention ratios (variation $< 0.03$), but differs substantially across task types, ranging from 0.14 (reasoning) to 0.30 (retrieval).
19	
20	Attention-associated aggregate convergence is task-specific. Of 10 benchmarks, only LAMBADA exhibits monotonic reduction in cross-architecture variance ($\rho = -1.0$, BCa 95\% CI $[-1.0,\,-0.7]$, heuristic given $n = 3$, \S\ref{ssec:statistical_methods}; cross-architecture $\sigma$ drops 79\%). LAMBADA \citep{paperno2016lambada} is a pure context-retrieval task that requires predicting the final word of a passage from long-range dependencies; attention provides direct token-level access to the full context, offering a plausible explanation for why convergence is observed on this task and not others. Benchmarks that involve reasoning or comprehension show no convergence, with all $|\rho| \leq 0.7$ and $p \geq .233$. The Bonferroni-adjusted $p = .100$ does not survive strict correction at $\alpha = 0.05$; the confidence interval, which excludes zero, provides a complementary characterization of the effect. This convergence is present at 1.3B but absent at 340M (Appendix~\ref{app:scale_convergence}). On LAMBADA, aggregate $\sigma$ decreases gradually ($0.024 \to 0.005$) while per-example Jaccard saturates at 4\% attention (${\sim}0.09$); the two quantities are decoupled. The experiments that follow begin with convergence (\S\ref{ssec:task_convergence}) because it establishes the aggregate backdrop against which per-example divergence (\S\ref{ssec:per_example}) and decoupling (\S\ref{ssec:decoupling}) are measured.
21	
22	Our contributions are as follows:
23	\begin{itemize}
24	    \item We show that architectural variation under matched training conditions is associated with structured per-example predictive multiplicity ($\alpha = 0.14$--$0.30$) across four benchmarks, with magnitude determined by task type rather than attention dose (\S\ref{ssec:per_example}, Table~\ref{tab:multiplicity}). The primary controlled variable is the recurrent backbone \citep[cf.][]{mccoy2020berts, damour2022underspecification}, though single training runs prevent full disentanglement from seed effects (Limitations).
25	    \item On LAMBADA, we observe that aggregate cross-architecture variance and per-example overlap respond to attention on different timescales: the former decreases gradually while the latter saturates at the first attention level (\S\ref{ssec:decoupling}). The Jaccard saturation generalizes to all four benchmarks (Appendix~\ref{app:cross_bench_jaccard}), indicating that per-example architectural specificity is invariant to attention dose regardless of task type. This pattern is consistent with attention narrowing aggregate gaps through architecture-specific pathways rather than uniform rescue. The aggregate convergence component is dependent on GDN inclusion (\S\ref{ssec:robustness}) and does not replicate on other benchmarks.
26	\end{itemize}
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3fa9c2f-cdc7-4360-b440-a593e2d953b7",
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "761e6f7f-53b7-435d-adfd-ec6012f8c32d",
  "sourceToolAssistantUUID": "b3fa9c2f-cdc7-4360-b440-a593e2d953b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T08:34:27.978Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WyvBa6QMxmnqgVtNz4T6Bo`</summary>

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
  "parentUuid": "761e6f7f-53b7-435d-adfd-ec6012f8c32d",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJLWJRtvkFGrEfLXH99",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ab96f553-9c87-4342-aab8-9ab21bd25995",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015yBHYfvZ3iDNG8nXanmWF5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28040,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28040,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 8 · 2026-05-22T08:34:27.985Z_

<details><summary>↩ Tool result · `toolu_01WyvBa6QMxmnqgVtNz4T6Bo`</summary>

```text
1	\section{Experiments}\label{sec:experiments}
2	
3	Using the model zoo of \citet{wang2025hybrid} (\S\ref{ssec:model_zoo}), we evaluate all 30 configurations on 10 benchmarks plus supplementary COPA ($n = 100$) at 1.3B scale unless noted. Results at 340M appear in scale analyses. Recall: h$k$-1 denotes one attention layer per $k{+}1$ layers; h3-1 = 25\% attention.
4	
5	\subsection{Task-Specific Convergence}\label{ssec:task_convergence}
6	
7	Table~\ref{tab:convergence} reports cross-architecture $\sigma$ at each attention ratio for all benchmarks at 1.3B scale. LAMBADA is the only benchmark exhibiting monotonic convergence: $\rho = -1.0$ ($p = .017$; BCa 95\% CI $[-1.0,\,-0.7]$, heuristic given $n = 3$ architectures, \S\ref{ssec:statistical_methods}; $\sigma$ drops 79\%; Bonferroni-adjusted $p = .100$; excluding GDN: $\rho = -0.7$, $p = .233$, \S\ref{ssec:robustness}). This is consistent with attention reducing differences in how recurrent architectures retrieve from context \citep{arora2024zoology}: LAMBADA requires predicting a final word from long-range dependencies, and attention provides direct token-level access that narrows architectural differences in recall capacity \citep{arora2024based}. The three recurrent backbones differ in how they compress sequential context (exponential decay in RetNet, gated expansion in HGRN2, delta rules in GDN), creating divergent retrieval capacities that attention may bypass via direct token access. For reasoning and comprehension tasks, the bottleneck likely lies in multi-step inference rather than context retrieval, so attention is not associated with similar variance reduction. No other benchmark shows significant convergence (all $|\rho| \leq 0.7$, $p \geq .233$; Figure~\ref{fig:task_specificity}). Full convergence discussion appears in Appendix~\ref{app:convergence_detail}. Scale analysis (Appendix~\ref{app:scale_convergence}) shows this convergence is present at 1.3B but absent at 340M. Statistical power is inherently limited with $n = 5$ ordinal levels, so this convergence is best interpreted as exploratory.
8	
9	\begin{figure}[t]
10	\centering
11	\includegraphics[width=\columnwidth]{figures/fig2_task_specificity.pdf}
12	\caption{Spearman $\rho$ between attention ratio and cross-architecture $\sigma$ for each benchmark at 1.3B scale. LAMBADA ($\rho = -1.0$; BCa 95\% CI $[-1.0,\,-0.7]$, heuristic) is the only benchmark with a negative correlation whose confidence interval excludes zero. Benchmarks are grouped by task category.}
13	\label{fig:task_specificity}
14	\end{figure}
15	
16	\begin{table*}[t]
17	\centering
18	\caption{Cross-architecture convergence across benchmarks (1.3B scale). $\rho$: Spearman correlation between attention ratio and cross-architecture $\sigma$ across five configurations. $p$: exact permutation test (two-tailed, 120 permutations). $\sigma$ values reported $\times 10^{2}$ (accuracy percentage points). Ratio: $\sigma_{\text{pure}} / \sigma_{\text{h3-1}}$. \textbf{Bold}: only benchmark with $\rho = -1.0$.}
19	\label{tab:convergence}
20	\begin{tabular}{llrrrrr}
21	\toprule
22	Benchmark & Category & $\rho$ & $p$ & $\sigma_{\text{pure}}$ & $\sigma_{\text{h3-1}}$ & Ratio \\
23	\midrule
24	\textbf{LAMBADA$^{\ddagger}$} & \textbf{Retrieval} & $\mathbf{-1.0}$ & \textbf{.017} & \textbf{2.41} & \textbf{0.49} & \textbf{4.87} \\
25	BoolQ & Comprehension & $0.2$ & .783 & 1.63 & 2.36 & 0.69 \\
26	ARC-C & Reasoning & $0.6$ & .350 & 0.96 & 1.32 & 0.72 \\
27	HellaSwag & Reasoning & $0.4$ & .517 & 1.17 & 1.22 & 0.96 \\
28	PIQA & Reasoning & $-0.5$ & .450 & 0.54 & 0.34 & 1.59 \\
29	WinoGrande & Reasoning & $0.1$ & .950 & 0.67 & 0.78 & 0.86 \\
30	ARC-E & Mixed & $-0.7$ & .233 & 1.00 & 0.13 & 7.70 \\
31	MMLU & Mixed & $-0.7$ & .233 & 0.92 & 0.41 & 2.27 \\
32	SciQ & Mixed & $0.1$ & .950 & 0.87 & 0.74 & 1.19 \\
33	XStoryCloze & Mixed & $-0.6$ & .350 & 0.82 & 0.55 & 1.49 \\
34	\midrule
35	COPA$^{\dagger}$ & Reasoning & $-0.67$ & .267 & 2.63 & 0.47 & 5.57 \\
36	\bottomrule
37	\multicolumn{7}{l}{\footnotesize $^{\dagger}$Supplementary ($n = 100$); excluded from multiple comparison correction.} \\
38	\multicolumn{7}{l}{\footnotesize $^{\ddagger}$GDN h3-1 uses 16 attention heads; all other configurations use 32 (\S\ref{ssec:robustness}).} \\
39	\multicolumn{7}{l}{\footnotesize Bonferroni-adjusted $p = 6 \times 2/120 = 0.100$ (exact); 0.102 arises from rounding raw $p$ to .017 before multiplying.}
40	\end{tabular}
41	\end{table*}
42	
43	\subsection{Per-Example Divergence}\label{ssec:per_example}
44	
45	Do architectures converge by improving on the same examples? We compare each architecture's pure-recurrent baseline against its h3-1 hybrid on 5{,}153 LAMBADA examples, classifying each as helped (correct only in hybrid), hurt (correct only in pure), or unchanged. Although the decomposition is binary, we verify below that it captures genuine separation in the continuous confidence space (Cohen's $d = 0.73$--$0.92$ between helped and hurt on LAMBADA; cross-benchmark details in Appendix~\ref{app:cm_cross}). This binarization discards confidence magnitude (a transition from 0.51 to 0.49 is treated identically to one from 0.99 to 0.01), so we supplement it with continuous confidence margin analysis (Appendix~\ref{app:confidence_margin}).
46	
47	Each architecture displays a distinct profile of per-example changes (Table~\ref{tab:per_example}). GDN loses a net 153 examples (462 helped, 615 hurt), RetNet loses 69 (426/495), and HGRN2 gains 153 (548/395). HGRN2 is the only architecture for which adding attention yields a net per-example benefit. Pairwise Jaccard similarity is low: mean $\bar{J} \leq 0.104$ for helped, $\leq 0.096$ for hurt, indicating ${\sim}90$\% non-overlap. Overlap significantly exceeds the independence baseline ($J_{\text{null}} \approx 0.05$, all $z > 5.9$, $p < .0001$; Appendix~\ref{app:jaccard_permutation}), but normalizing by the theoretical upper bound $J_{\max} = \min(|A|,|B|)/\max(|A|,|B|)$, observed overlap reaches only 6--7\% of the achievable range above chance (normalized ES 0.065 helped, 0.062 hurt; per-pair details in Appendix~\ref{app:normalized_es}), confirming that low Jaccard cannot be attributed to set-size constraints.
48	
49	\paragraph{Confidence margin mechanism.} No surface-level feature (token count, word frequency, syntactic complexity) reliably separates helped from hurt examples. However, pure-model confidence on the target token is strongly predictive within each architecture: hurt examples have lower target-token probability among pure-correct examples ($d = 0.83$--$0.92$), and helped examples have higher probability among pure-wrong examples ($d = 0.73$--$0.77$); see Appendix~\ref{app:confidence_margin}. A Kruskal-Wallis test confirms cross-architecture structure in both hurt ($p = .0005$) and helped ($p = .020$) distributions. The confidence margin thus identifies a per-example predictor of which examples will be affected: marginally correct predictions are more likely to transition to incorrect, and near-miss errors are more likely to transition to correct, but with architecture-specific thresholds that produce the observed cross-architecture divergence. Formalizing this as a prediction task (Appendix~\ref{app:prediction_framework}), pure-model confidence achieves AUC 0.70--0.74 within each architecture; rescue thresholds are architecture-invariant (relative spread 1\%), while disruption thresholds vary 47\%. Since each backbone assigns different confidences to the same input, even a shared rescue rule affects different examples per architecture, providing a parsimonious explanation for low cross-architecture Jaccard. The rescue pattern generalizes across LAMBADA, HellaSwag, and ARC-Easy (9/9 tests, $d = 0.13$--$0.60$; Appendix~\ref{app:cm_cross}). The disruption pattern is weaker on ARC-Easy ($d = 0.13$--$0.26$) and absent on HellaSwag under \texttt{acc\_norm} and on binary classification (Appendix~\ref{app:boolq}). This structured per-example disagreement constitutes predictive multiplicity \citep{marx2020predictive} arising under architectural variation \citep[cf.][]{damour2022underspecification}.
50	
51	\paragraph{Multiplicity variation.} Extending the per-example analysis to HellaSwag ($N = 10{,}042$) and PIQA ($N = 1{,}838$) reveals that predictive multiplicity varies systematically across tasks (Table~\ref{tab:multiplicity}). The ambiguity $\alpha$ \citep{marx2020predictive} ranges from 0.14 (PIQA) through 0.15 (HellaSwag) and 0.21 (ARC-Easy) to 0.30 (LAMBADA), forming a task-dependent variation. Format does not drive multiplicity: HellaSwag (four-way) and PIQA (two-choice) produce nearly identical $\alpha$ despite different formats. Bootstrap 95\% CIs confirm the ordering (all non-overlapping except PIQA--HellaSwag; Appendix, Table~\ref{tab:arceasy_ambiguity}). Moreover, $\alpha$ does not significantly correlate with task accuracy (Spearman $\rho = -0.60$, $p = .24$). Pairwise Jaccard remains uniformly low ($\bar{J} \leq 0.10$, all $p < .01$ across four benchmarks), indicating that architectures affect different examples regardless of how many examples are affected. Within each benchmark, $\alpha$ is stable across attention ratios (variation $< 0.03$), but differs $2\times$ across task types (from reasoning to retrieval), confirming that multiplicity magnitude depends on task, not attention dose \citep[cf.][]{gorbett2026crossmodel}. PIQA (0.14) and HellaSwag (0.15) share a reasoning-task floor, while retrieval (LAMBADA, 0.30) and mixed (ARC-Easy, 0.21) tasks produce higher values.
52	
53	\begin{table}[t]
54	\centering
55	\small
56	\caption{Predictive multiplicity at 1.3B. $\alpha$: ambiguity at h3-1 \citep{marx2020predictive}. $\bar{J}$: mean pairwise Jaccard of helped~(h) and hurt~(u) sets, averaged across four hybrid attention ratios and three architecture pairs. $\rho_\alpha$: Spearman $\rho$ between attention ratio and $\alpha$. Benchmarks ordered by $\alpha$.}
57	\label{tab:multiplicity}
58	\begin{tabular}{@{}lrcccc@{}}
59	\toprule
60	 & $N$ & $\alpha$ & $\bar{J}_{h}$ & $\bar{J}_{u}$ & $\rho_\alpha$ \\
61	\midrule
62	PIQA & 1838 & .14 & .091 & .094 & $0.0$ \\
63	HellaSwag & 10042 & .15 & .095 & .085 & $0.1$ \\
64	ARC-Easy & 2376 & .21 & .092 & .099 & $-0.2$ \\
65	LAMBADA & 5153 & .30 & .096 & .091 & $-0.6$ \\
66	\bottomrule
67	\end{tabular}
68	\par\vspace{1pt}
69	{\footnotesize Within-benchmark $\alpha$ variation $< 0.03$ across ratios. BoolQ, WinoGrande: Appendix~\ref{app:boolq}, \ref{app:winogrande}.}
70	\end{table}
71	
72	\subsection{Decoupling}\label{ssec:decoupling}
73	
74	A key consequence of this multiplicity is that aggregate convergence and per-example divergence operate on different timescales as attention ratio increases (Figure~\ref{fig:decoupling}).
75	
76	Cross-architecture $\sigma$ decreases gradually across the five attention ratios: $0.024 \to 0.016 \to 0.014 \to 0.006 \to 0.005$. In contrast, pairwise Jaccard similarity between architectures' per-example effects saturates at the first attention level (4\%): approximately 0.095 for helped, with no further increase at higher ratios. Net asymmetry between architectures' per-example profiles increases from 0.013 at 4\% attention to 0.040 at 25\%. If convergence arose from attention uniformly rescuing the same difficult examples across architectures, Jaccard would increase in parallel with decreasing $\sigma$. The observed saturation of Jaccard at the first attention level indicates that each architecture's per-example response to attention is largely idiosyncratic. The observed $\bar{J} \approx 0.10$ is far below the theoretical maximum $J_{\max} \approx 0.78$--$0.92$ given helped-set sizes, ruling out ceiling constraints: there is ample room for Jaccard to increase if attention were homogenizing per-example behavior (normalized effect size 6--7\% of achievable range; \S\ref{ssec:per_example}).
77	
78	This saturation generalizes beyond LAMBADA: on all four main benchmarks, mean pairwise Jaccard shows no significant trend with attention ratio (all $\rho \leq 0.80$, $p \geq 0.333$; Appendix~\ref{app:cross_bench_jaccard}), with values uniformly between 0.08 and 0.11.
79	
80	Bootstrap confidence intervals (10{,}000 resamples; heuristic given $n = 3$, \S\ref{ssec:statistical_methods}) support this pattern statistically: the 95\% CI for $\sigma$ does not overlap between pure $[.019,\,.030]$ and h3-1 $[.002,\,.011]$, while the CIs for mean Jaccard overlap completely across all non-zero attention ratios (helped: $[.08,\,.11]$; hurt: $[.07,\,.11]$). Within-architecture Jaccard averages ${\sim}0.33$ (Appendix~\ref{app:within_arch_stability}), roughly $3\times$ the cross-architecture value (${\sim}0.10$). This $3\times$ gap compares within-architecture variation across attention ratios to cross-architecture variation at matched ratios, a proxy for, not a direct measurement of, seed-versus-architecture effects.
81	
82	Attention weight analysis (Appendix~\ref{app:attention_patterns}) shows GDN and RetNet produce nearly identical attention distributions (cosine 0.995) yet differ in per-example effects, suggesting these originate in the recurrent layers. The four-benchmark variation (Table~\ref{tab:multiplicity}) confirms independence: LAMBADA ($\alpha = 0.30$) is the only benchmark showing convergence despite having the highest multiplicity, while PIQA ($\alpha = 0.14$) and HellaSwag ($\alpha = 0.15$) show no convergence with the lowest multiplicity.
83	
84	Cross-scale analysis on all four benchmarks reveals that the qualitative pattern of per-example multiplicity is scale-robust: pairwise Jaccard remains stable across scales ($\bar{J} = 0.08$--$0.10$ at 340M vs.\ $0.09$--$0.095$ at 1.3B), and architecture-specific helped/hurt profiles persist. While $\alpha$ is systematically higher at 340M ($\Delta \leq 8$\,pp), this inflation does not correlate with accuracy loss across benchmarks (HellaSwag shows the largest accuracy gap yet one of the smallest $\alpha$ increases), suggesting capacity-related but not accuracy-driven modulation. At 340M, aggregate convergence is absent on all benchmarks ($\rho = -0.50$, $p = .45$ for LAMBADA). This dissociation suggests that the \emph{pattern} of per-example multiplicity (which architectures affect which examples) reflects structural differences in recurrent processing, while absolute $\alpha$ magnitude is partially modulated by model capacity (Appendix~\ref{app:scale_per_example}).
85	
86	\subsection{Robustness}\label{ssec:robustness}
87	
88	Removing GDN weakens LAMBADA convergence from $\rho = -1.0$ to $\rho = -0.7$ ($p = .233$), partly because GDN's h3-1 uses 16 attention heads rather than 32 in all other configurations (Appendix~\ref{app:gdn_confound}). The 16-vs-32 head asymmetry could contribute to GDN's faster convergence by limiting attention capacity, though disentangling this from architectural differences would require matched-head experiments not available in the zoo. The RetNet--HGRN2 pair preserves the decoupling: all hybrid $\sigma \leq 0.008$ while Jaccard saturates at 0.086--0.108. The aggregate convergence result is therefore dependent on GDN inclusion; the decoupling result is not. Full sensitivity analyses appear in Appendix~\ref{app:sensitivity}.
89	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab96f553-9c87-4342-aab8-9ab21bd25995",
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "c644da8b-33b9-4073-83ce-c490d55656d8",
  "sourceToolAssistantUUID": "ab96f553-9c87-4342-aab8-9ab21bd25995",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T08:34:28.064Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KErzYf6a4F2xQPZKRzYhfT`</summary>

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
  "parentUuid": "c644da8b-33b9-4073-83ce-c490d55656d8",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJLWJRtvkFGrEfLXH99",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cea6ecd5-17d2-46b1-b829-bc0551493515",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015yBHYfvZ3iDNG8nXanmWF5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28040,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28040,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 10 · 2026-05-22T08:34:28.082Z_

<details><summary>↩ Tool result · `toolu_01KErzYf6a4F2xQPZKRzYhfT`</summary>

```text
1	\section{Conclusion}
2	
3	We present the first systematic per-example analysis of attention effects in hybrid recurrent models. Per-example multiplicity spans a task-dependent variation ($\alpha = 0.14$--$0.30$) across four benchmarks, with Jaccard uniformly low ($\leq 0.10$) regardless of aggregate convergence. On LAMBADA, aggregate variance decreases with attention while per-example overlap saturates, consistent with architecture-specific pathways rather than uniform rescue (dependent on GDN inclusion; does not replicate on other benchmarks). Aggregate benchmark equivalence thus masks per-example divergence: each backbone develops architecture-specific response patterns invisible to standard evaluation. Within each architecture, pure-model confidence partially predicts which examples will be affected (AUC 0.70--0.74), though disruption thresholds vary 47\% across architectures (\S\ref{ssec:per_example}).
4	
5	For practitioners, these results motivate per-example audits whenever hybrid designs achieve comparable aggregate scores: the ${\sim}90\%$ non-overlap means architectures interchangeable by aggregate metrics affect nearly disjoint examples. A majority vote across three architectures does not outperform the best individual model (LAMBADA: $-0.2$\,pp; ARC-Easy: $-1.1$\,pp) despite 15--45\% disagreement, because roughly half of disagreement examples have only one correct architecture (Appendix~\ref{app:complementarity}). Oracle accuracy reveals $+7$--$14$\,pp of untapped complementarity, but accessing it requires selection methods beyond naive ensembling.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cea6ecd5-17d2-46b1-b829-bc0551493515",
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "969c9cad-5f39-4856-afb8-a64af1c9740d",
  "sourceToolAssistantUUID": "cea6ecd5-17d2-46b1-b829-bc0551493515",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-22T08:34:30.257Z_

Now let me search more thoroughly for specific numerical values across all sections to check for inconsistencies.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "969c9cad-5f39-4856-afb8-a64af1c9740d",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJLgqC8RaVBXfMKNvmx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9d6ef699-edbb-46ab-9033-4bca51d73458",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017mdq8CH8XYo6UqQVEK6ktG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9700,
      "cache_read_input_tokens": 28040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9700,
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

_source line 12 · 2026-05-22T08:34:31.359Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01TrxJSd5i9jAJwrEhsMY4mx`</summary>

```json
{
  "pattern": "0\\.14|0\\.15|0\\.21|0\\.30",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d6ef699-edbb-46ab-9033-4bca51d73458",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJLgqC8RaVBXfMKNvmx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "26606628-c4eb-4b05-96be-98d36e05e637",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017mdq8CH8XYo6UqQVEK6ktG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9700,
      "cache_read_input_tokens": 28040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9700,
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

_source line 13 · 2026-05-22T08:34:31.384Z_

<details><summary>↩ Tool result · `toolu_01TrxJSd5i9jAJwrEhsMY4mx`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:30:\item Introduction, Abstract, and Conclusion rewritten to multiplicity-first framing: per-example multiplicity ($\alpha = 0.14$--$0.30$, Jaccard $\leq 0.10$) now leads; convergence introduced as contrastive secondary finding.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:33:\item Per-example analysis expanded from two to four benchmarks (LAMBADA, HellaSwag, PIQA, ARC-Easy) plus BoolQ and WinoGrande as supplementary in Appendix; multiplicity spectrum $\alpha = 0.14$--$0.30$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:71:\item \textbf{Abstract}: Rewritten to lead with per-example multiplicity ($\alpha = 0.14$--$0.30$, Jaccard $\leq 0.10$); convergence introduced with ``by contrast'' as secondary finding.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:85:\item Multiplicity is characterized as a task-dependent spectrum: $\alpha$ ranges from 0.14 (PIQA) to 0.30 (LAMBADA).
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:86:\item PIQA and HellaSwag exhibit the lowest multiplicity ($\alpha = 0.14$--$0.15$), confirming that multiplicity magnitude is task-dependent rather than noise.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:54:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:83:\item \textbf{Task-dependent spectrum}: No prior work has measured how multiplicity magnitude varies across task types within a controlled architecture family. The spectrum from $\alpha = 0.14$ (reasoning) to $0.30$ (retrieval) was unknown.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:101:\item \textbf{Task-type guidance}: Retrieval-heavy tasks show the highest multiplicity ($\alpha \approx 0.30$); reasoning tasks the lowest ($\alpha \approx 0.14$). Per-example audits are most warranted for retrieval and mixed tasks.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:211:\response{No confound. Spearman $\rho(N, \alpha) = -0.60$, $p = .24$ (not significant; reported in \S4.2). HellaSwag has the most examples ($N = 10{,}042$) yet nearly the lowest $\alpha$ ($0.15$). PIQA has the fewest main-text examples ($N = 1{,}838$) yet the lowest $\alpha$ ($0.14$). Subsample sensitivity analysis (Appendix~G) confirms $\alpha$ stabilizes at $n \geq 500$ with CI width $< 0.08$.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/arr_checklist.tex:16:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:51:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:82:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:135:RetNet & 0.1578 & 0.1591 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:586:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:608:At 340M, LAMBADA per-example multiplicity closely matches the 1.3B pattern: $\alpha = 0.313$ (vs.\ 0.307 at 1.3B), with mean pairwise Jaccard $\bar{J} \approx 0.089$ (vs.\ 0.095). Per-example directionality is preserved: HGRN2 shows net positive effects at h3-1 ($+238$ examples), while GDN ($-256$) and RetNet ($-106$) show net negative effects, mirroring the 1.3B profile (HGRN2 $+153$, GDN $-153$, RetNet $-69$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:682:{\footnotesize At $n = 100$, CI width (0.13--0.18) spans the entire four-benchmark $\alpha$ range (0.14--0.30), rendering $\alpha$ estimation unreliable. This justifies excluding COPA ($n = 100$) from the per-example analysis.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex:18:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex:24:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex:25:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.log:630:\T1/ptm/m/n/10.95 (+20) floor, while re-trieval (LAM-BADA, 0.30) and
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26606628-c4eb-4b05-96be-98d36e05e637",
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "b19ecc9f-771e-4a9d-b83c-e37e32758c69",
  "sourceToolAssistantUUID": "26606628-c4eb-4b05-96be-98d36e05e637",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-22T08:34:31.811Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01GGggKnu3qipiggGA1Vv5gc`</summary>

```json
{
  "pattern": "Jaccard|0\\.10|≤ 0\\.10",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b19ecc9f-771e-4a9d-b83c-e37e32758c69",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJLgqC8RaVBXfMKNvmx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "997815c0-f39c-473d-b1bf-0078a493755a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017mdq8CH8XYo6UqQVEK6ktG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9700,
      "cache_read_input_tokens": 28040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9700,
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

_source line 15 · 2026-05-22T08:34:31.833Z_

<details><summary>↩ Tool result · `toolu_01GGggKnu3qipiggGA1Vv5gc`</summary>

```text
&lt;persisted-output>
Output too large (39KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft--claude-sessions-paper-agent-b031d53b/210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc/tool-results/toolu_01GGggKnu3qipiggGA1Vv5gc.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex:44:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:39:\multicolumn{7}{l}{\footnotesize Bonferroni-adjusted $p = 6 \times 2/120 = 0.100$ (exact); 0.102 arises from rounding raw $p$ to .017 before multiplying.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:47:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:49:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:51:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:56:\caption{Predictive multiplicity at 1.3B. $\alpha$: ambiguity at h3-1 \citep{marx2020predictive}. $\bar{J}$: mean pairwise Jaccard of helped~(h) and hurt~(u) sets, averaged across four hybrid attention ratios and three architecture pairs. $\rho_\alpha$: Spearman $\rho$ between attention ratio and $\alpha$. Benchmarks ordered by $\alpha$.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:76:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:78:This saturation generalizes beyond LAMBADA: on all four main benchmarks, mean pairwise Jaccard shows no significant trend with attention ratio (all $\rho \leq 0.80$, $p \geq 0.333$; Appendix~\ref{app:cross_bench_jaccard}), with values uniformly between 0.08 and 0.11.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:80:[Omitted long matching line]
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "997815c0-f39c-473d-b1bf-0078a493755a",
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "d6eee4df-dafe-4604-b1b5-f51ef246099f",
  "sourceToolAssistantUUID": "997815c0-f39c-473d-b1bf-0078a493755a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-22T08:34:32.439Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01SYKD8S2SNqhVHfQdG9m2th`</summary>

```json
{
  "pattern": "0\\.78|0\\.92|theoretical maximum",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6eee4df-dafe-4604-b1b5-f51ef246099f",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJLgqC8RaVBXfMKNvmx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1385a91d-4640-4ab8-8542-92238236619c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017mdq8CH8XYo6UqQVEK6ktG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9700,
      "cache_read_input_tokens": 28040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9700,
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

_source line 17 · 2026-05-22T08:34:32.458Z_

<details><summary>↩ Tool result · `toolu_01SYKD8S2SNqhVHfQdG9m2th`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:29:WinoGrande & Reasoning & $0.1$ & .950 & 0.67 & 0.78 & 0.86 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:31:MMLU & Mixed & $-0.7$ & .233 & 0.92 & 0.41 & 2.27 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:45:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:49:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:76:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:241:All normalized effect sizes fall below 0.10, confirming that observed overlap reaches only 6--7\% of the theoretical maximum. The low Jaccard values cannot be attributed to set-size constraints.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:427:This pattern is consistent across all three architectures ($|d| = 0.73$--$0.92$, all $p < 10^{-54}$) but does not alter the cross-architecture Jaccard findings---within-architecture predictability coexists with cross-architecture divergence.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:439:RetNet (h3-1) & 497 & 2169 & 1.293 & 0.785 & 0.83 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:440:HGRN2 (h3-1) & 392 & 2102 & 1.481 & 0.899 & 0.92 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:526:HGRN2 (h3-1) & .708 & 0.77 & .743 & 0.92 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:113:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:116:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:128:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:138:Regarding the Jaccard floor effect concern: observed $\bar{J} \approx 0.10$ is far below the theoretical maximum $J_{\max} = 0.78$--$0.92$ (given helped-set sizes of 426--548 out of $N = 5{,}153$). The normalized effect size is only 5--7\% of the achievable range above chance (\S4.2). This rules out ceiling constraints as an alternative explanation for Jaccard saturation---there is ample room for $J$ to increase if attention were homogenizing per-example behavior.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:219:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:251:\response{We have added a normalized effect size analysis to \S4.2: observed $\bar{J} \approx 0.10$ vs.\ theoretical maximum $J_{\max} = 0.78$--$0.92$ (given helped-set sizes). The normalized effect size is only 5--7\% of the achievable range above chance (normalized ES 0.065 helped, 0.047 hurt), ruling out ceiling constraints as an alternative explanation.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex:25:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1385a91d-4640-4ab8-8542-92238236619c",
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "0628565d-6291-4732-8384-b587923464e9",
  "sourceToolAssistantUUID": "1385a91d-4640-4ab8-8542-92238236619c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-22T08:34:32.814Z_

<details open><summary>🔧 Tool call — Grep · `toolu_016k6SChpMjJAgSGK1t2tUkJ`</summary>

```json
{
  "pattern": "6--7%|5--7%|normalized effect size",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0628565d-6291-4732-8384-b587923464e9",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJLgqC8RaVBXfMKNvmx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5b96e749-b76a-4d89-9a7a-c1e333b077b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017mdq8CH8XYo6UqQVEK6ktG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9700,
      "cache_read_input_tokens": 28040,
      "output_tokens": 503,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9700
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 503,
          "cache_read_input_tokens": 28040,
          "cache_creation_input_tokens": 9700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9700,
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

_source line 19 · 2026-05-22T08:34:32.833Z_

<details><summary>↩ Tool result · `toolu_016k6SChpMjJAgSGK1t2tUkJ`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:76:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:215:To assess whether low observed Jaccard reflects a floor effect imposed by unequal set sizes, we compute the theoretical upper bound $J_{\max} = \min(|A|,|B|) / \max(|A|,|B|)$ and the normalized effect size $(J_{\text{obs}} - J_{\text{null}}) / (J_{\max} - J_{\text{null}})$, which measures observed overlap as a fraction of the achievable range above chance. Table~\ref{tab:normalized_es} reports per-pair results.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:241:All normalized effect sizes fall below 0.10, confirming that observed overlap reaches only 6--7\% of the theoretical maximum. The low Jaccard values cannot be attributed to set-size constraints.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:553:BoolQ ($N = 3{,}270$; comprehension, binary yes/no classification) shows the highest ambiguity among the benchmarks we analyzed ($\alpha \approx 0.45$), but the Jaccard significance pattern is mixed: only 12 of 24 architecture $\times$ attention-ratio pair combinations yield $p < .01$. In particular, the RetNet--HGRN2 pair produces 0/8 significant Jaccard values, with several normalized effect sizes below zero, suggesting anti-correlated per-example effects for this pair.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:138:Regarding the Jaccard floor effect concern: observed $\bar{J} \approx 0.10$ is far below the theoretical maximum $J_{\max} = 0.78$--$0.92$ (given helped-set sizes of 426--548 out of $N = 5{,}153$). The normalized effect size is only 5--7\% of the achievable range above chance (\S4.2). This rules out ceiling constraints as an alternative explanation for Jaccard saturation---there is ample room for $J$ to increase if attention were homogenizing per-example behavior.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:251:\response{We have added a normalized effect size analysis to \S4.2: observed $\bar{J} \approx 0.10$ vs.\ theoretical maximum $J_{\max} = 0.78$--$0.92$ (given helped-set sizes). The normalized effect size is only 5--7\% of the achievable range above chance (normalized ES 0.065 helped, 0.047 hurt), ruling out ceiling constraints as an alternative explanation.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b96e749-b76a-4d89-9a7a-c1e333b077b6",
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "2eb1340f-1793-4553-bd9a-a3110f683cc8",
  "sourceToolAssistantUUID": "5b96e749-b76a-4d89-9a7a-c1e333b077b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-22T08:34:34.126Z_

I found an inconsistency! Let me continue checking the remaining numerical values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2eb1340f-1793-4553-bd9a-a3110f683cc8",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJM34NC7DGvcvLcQDxs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0151f195-55da-4215-ba5f-bc375c1eb9d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JaXKNG7pn8XkuYqRTxT8v1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5663,
      "cache_read_input_tokens": 37740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5663,
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

_source line 21 · 2026-05-22T08:34:35.258Z_

<details open><summary>🔧 Tool call — Grep · `toolu_018iCuozb5fDSYQyRWDLXzqt`</summary>

```json
{
  "pattern": "LAMBADA.*-1\\.0|ρ = -1\\.0|σ drops 79%|Bonferroni.*0\\.100|p = \\.017",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0151f195-55da-4215-ba5f-bc375c1eb9d7",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJM34NC7DGvcvLcQDxs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7791fa44-ba8a-494c-a722-b197924a2e4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JaXKNG7pn8XkuYqRTxT8v1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5663,
      "cache_read_input_tokens": 37740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5663,
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

_source line 22 · 2026-05-22T08:34:35.282Z_

<details><summary>↩ Tool result · `toolu_018iCuozb5fDSYQyRWDLXzqt`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:12:\caption{Spearman $\rho$ between attention ratio and cross-architecture $\sigma$ for each benchmark at 1.3B scale. LAMBADA ($\rho = -1.0$; BCa 95\% CI $[-1.0,\,-0.7]$, heuristic) is the only benchmark with a negative correlation whose confidence interval excludes zero. Benchmarks are grouped by task category.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:24:\textbf{LAMBADA$^{\ddagger}$} & \textbf{Retrieval} & $\mathbf{-1.0}$ & \textbf{.017} & \textbf{2.41} & \textbf{0.49} & \textbf{4.87} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:39:\multicolumn{7}{l}{\footnotesize Bonferroni-adjusted $p = 6 \times 2/120 = 0.100$ (exact); 0.102 arises from rounding raw $p$ to .017 before multiplying.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:88:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex:48:\paragraph{Power considerations.} With $n = 5$ ordinal levels, only $\rho = \pm 1.0$ achieves $p < .05$ (exact $p = .017$); the test has no power to detect strong but imperfect monotonic trends ($|\rho| = 0.9$ yields $p = .083$). This binary resolution means that a single rank swap suffices to shift the verdict from significant to non-significant.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:14:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:24:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:32:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:48:Table~\ref{tab:gdn_sensitivity} reports the results for benchmarks where the correlation changes by $|\Delta\rho| \geq 0.3$. LAMBADA weakens from $\rho = -1.0$ to $\rho = -0.7$ ($p = .233$), consistent with GDN contributing to the convergence signal. MMLU reverses from $\rho = -0.7$ to $\rho = +0.6$, confirming that the moderate negative correlation on MMLU depends on GDN's inclusion and should not be interpreted as evidence of convergence.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:59:LAMBADA & $-1.0$ & $-0.7$ & $+0.3$ & .233 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:71:The sensitivity analysis in Appendix~\ref{app:sensitivity} shows that removing GDN weakens the LAMBADA convergence correlation from $\rho = -1.0$ to $\rho = -0.7$. This weakening is partially attributable to the reduced sample size ($n = 2$ architectures) and partially to the confound itself. We cannot separate these two effects with the available data.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:610:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex:20:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:38:\item Table~2: $\rho_\sigma$ column renamed to $\rho_\alpha$ (Spearman between attention ratio and ambiguity $\alpha$); LAMBADA value corrected from $-1.0$ to $-0.6$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:134:\reviewer{Why does the Bonferroni-adjusted p-value appear as both 0.100 and 0.102 in different places?}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:136:\response{We have added a footnote to Table~1 explaining the discrepancy: ``Bonferroni-adjusted $p = 6 \times 2/120 = 0.100$ (exact); 0.102 arises from rounding raw $p$ to .017 before multiplying.'' The value 0.100 is the exact result; 0.102 is a rounding artifact. We now use 0.100 consistently throughout.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:118:\reviewer{Excluding GDN weakens LAMBADA $\rho$ from $-1.0$ to $-0.7$ ($p = .233$) and reverses MMLU $\rho$ from $-0.7$ to $+0.6$. This should be in the main text, not just Appendix.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:180:\response{We retain Table~1 in its current form because the exact $\rho$, $p$, $\sigma$ values are essential for reproducibility. The key pattern (only LAMBADA shows $\rho = -1.0$) is conveyed by Figure~2, which serves as the visual complement.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.aux:564:\@writefile{lof}{\contentsline {figure}{\numberline {2}{\ignorespaces Spearman $\rho $ between attention ratio and cross-architecture $\sigma $ for each benchmark at 1.3B scale. LAMBADA ($\rho = -1.0$; BCa 95\% CI $[-1.0,\,-0.7]$, heuristic) is the only benchmark with a negative correlation whose confidence interval excludes zero. Benchmarks are grouped by task category.}}{6}{figure.caption.11}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.aux:565:\newlabel{fig:task_specificity}{{2}{6}{Spearman $\rho $ between attention ratio and cross-architecture $\sigma $ for each benchmark at 1.3B scale. LAMBADA ($\rho = -1.0$; BCa 95\% CI $[-1.0,\,-0.7]$, heuristic) is the only benchmark with a negative correlation whose confidence interval excludes zero. Benchmarks are grouped by task category}{figure.caption.11}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7791fa44-ba8a-494c-a722-b197924a2e4c",
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "6ed6da70-c951-4e95-bd1c-30919703bf46",
  "sourceToolAssistantUUID": "7791fa44-ba8a-494c-a722-b197924a2e4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T08:34:35.892Z_

<details open><summary>🔧 Tool call — Grep · `toolu_016xKnXF78PQWyvD3vCfSeEx`</summary>

```json
{
  "pattern": "0\\.024|0\\.016|0\\.014|0\\.006|0\\.005|σ trajectory",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ed6da70-c951-4e95-bd1c-30919703bf46",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJM34NC7DGvcvLcQDxs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9139b8c6-b058-4417-a8b4-003391c09080",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JaXKNG7pn8XkuYqRTxT8v1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5663,
      "cache_read_input_tokens": 37740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5663,
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

_source line 24 · 2026-05-22T08:34:35.912Z_

<details><summary>↩ Tool result · `toolu_016xKnXF78PQWyvD3vCfSeEx`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:76:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:18:\paragraph{Exploratory benchmarks.} Four additional benchmarks (BoolQ, PIQA, SciQ, XStoryCloze) were added as exploratory tests. These are corrected separately across all 10 benchmarks (adjusted threshold $\alpha / 10 = 0.005$) and reported as exploratory throughout the paper.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:28:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:336:GDN & 0.645 & 0.649 & $+$0.005 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:343:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:610:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex:20:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9139b8c6-b058-4417-a8b4-003391c09080",
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "945969a9-72b8-46db-bc61-1101ea643698",
  "sourceToolAssistantUUID": "9139b8c6-b058-4417-a8b4-003391c09080",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T08:34:36.727Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Kf33gcWQ6PXpcG8t1wTDZy`</summary>

```json
{
  "pattern": "-0\\.2pp|-1\\.1pp|majority vote|LAMBADA.*-0\\.|ARC-Easy.*-1\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "945969a9-72b8-46db-bc61-1101ea643698",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJM34NC7DGvcvLcQDxs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "713b10d4-124e-46c6-826b-439ab31288a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JaXKNG7pn8XkuYqRTxT8v1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5663,
      "cache_read_input_tokens": 37740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5663,
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

_source line 26 · 2026-05-22T08:34:36.751Z_

<details><summary>↩ Tool result · `toolu_01Kf33gcWQ6PXpcG8t1wTDZy`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex:25:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:12:\caption{Spearman $\rho$ between attention ratio and cross-architecture $\sigma$ for each benchmark at 1.3B scale. LAMBADA ($\rho = -1.0$; BCa 95\% CI $[-1.0,\,-0.7]$, heuristic) is the only benchmark with a negative correlation whose confidence interval excludes zero. Benchmarks are grouped by task category.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:51:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:65:LAMBADA & 5153 & .30 & .096 & .091 & $-0.6$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:88:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:24:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:48:Table~\ref{tab:gdn_sensitivity} reports the results for benchmarks where the correlation changes by $|\Delta\rho| \geq 0.3$. LAMBADA weakens from $\rho = -1.0$ to $\rho = -0.7$ ($p = .233$), consistent with GDN contributing to the convergence signal. MMLU reverses from $\rho = -0.7$ to $\rho = +0.6$, confirming that the moderate negative correlation on MMLU depends on GDN's inclusion and should not be interpreted as evidence of convergence.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:59:LAMBADA & $-1.0$ & $-0.7$ & $+0.3$ & .233 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:71:The sensitivity analysis in Appendix~\ref{app:sensitivity} shows that removing GDN weakens the LAMBADA convergence correlation from $\rho = -1.0$ to $\rho = -0.7$. This weakening is partially attributable to the reduced sample size ($n = 2$ architectures) and partially to the confound itself. We cannot separate these two effects with the available data.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:245:Table~\ref{tab:arceasy_effects} reports per-example effect counts on ARC-Easy ($N = 2{,}376$) at 1.3B scale for each attention ratio. Unlike LAMBADA, ARC-Easy shows no aggregate convergence ($\rho = -0.20$, $p = .783$). HGRN2 is net positive at all ratios; GDN and RetNet are mixed.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:659:Convergence is absent at 340M across all benchmarks (all $|\rho| \leq 0.4$, $p \geq .45$), in contrast to 1.3B where LAMBADA shows monotonic convergence. The absence of convergence at 340M extends beyond LAMBADA to HellaSwag ($\rho = 0.4$, $p = .52$), PIQA ($\rho = 0.3$, $p = .68$), and ARC-Easy ($\rho = -0.1$, $p = .95$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:687:We decompose the three-architecture vote on each example into four categories: unanimous correct (3/3), majority correct (2/3), minority correct (1/3), and unanimous wrong (0/3). This decomposition explains the structural failure of majority vote despite substantial per-example complementarity.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:694:\caption{Complementarity decomposition at 1.3B h3-1. Fractions of total examples in each vote category. MV expl.: fraction of complementary examples where majority vote is correct.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex:20:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:38:\item Table~2: $\rho_\sigma$ column renamed to $\rho_\alpha$ (Spearman between attention ratio and ambiguity $\alpha$); LAMBADA value corrected from $-1.0$ to $-0.6$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:44:\item Ensemble proof-of-concept: majority vote vs.\ oracle analysis added to Conclusion.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:118:\reviewer{Excluding GDN weakens LAMBADA $\rho$ from $-1.0$ to $-0.7$ ($p = .233$) and reverses MMLU $\rho$ from $-0.7$ to $+0.6$. This should be in the main text, not just Appendix.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:225:\reviewer{The paper identifies per-example disagreement but does not test whether it can be exploited. Even a simple majority vote would demonstrate whether the observed multiplicity has practical consequences.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:227:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.aux:564:\@writefile{lof}{\contentsline {figure}{\numberline {2}{\ignorespaces Spearman $\rho $ between attention ratio and cross-architecture $\sigma $ for each benchmark at 1.3B scale. LAMBADA ($\rho = -1.0$; BCa 95\% CI $[-1.0,\,-0.7]$, heuristic) is the only benchmark with a negative correlation whose confidence interval excludes zero. Benchmarks are grouped by task category.}}{6}{figure.caption.11}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.aux:565:\newlabel{fig:task_specificity}{{2}{6}{Spearman $\rho $ between attention ratio and cross-architecture $\sigma $ for each benchmark at 1.3B scale. LAMBADA ($\rho = -1.0$; BCa 95\% CI $[-1.0,\,-0.7]$, heuristic) is the only benchmark with a negative correlation whose confidence interval excludes zero. Benchmarks are grouped by task category}{figure.caption.11}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.aux:1813:\@writefile{lot}{\contentsline {table}{\numberline {29}{\ignorespaces Complementarity decomposition at 1.3B h3-1. Fractions of total examples in each vote category. MV expl.: fraction of complementary examples where majority vote is correct.}}{20}{table.caption.59}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.aux:1814:\newlabel{tab:complementarity}{{29}{20}{Complementarity decomposition at 1.3B h3-1. Fractions of total examples in each vote category. MV expl.: fraction of complementary examples where majority vote is correct}{table.caption.59}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "713b10d4-124e-46c6-826b-439ab31288a7",
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "de032972-7b1a-458a-877a-daa228c2a586",
  "sourceToolAssistantUUID": "713b10d4-124e-46c6-826b-439ab31288a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T08:34:37.842Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01DF7xe9i56585FnCUyfvfB6`</summary>

```json
{
  "pattern": "oracle|7.*14|14pp|\\+7.*\\+14|\\+7.*14pp",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de032972-7b1a-458a-877a-daa228c2a586",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJM34NC7DGvcvLcQDxs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "db22ccdc-929b-41db-89fe-1c4f1c662378",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JaXKNG7pn8XkuYqRTxT8v1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5663,
      "cache_read_input_tokens": 37740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5663,
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

_source line 28 · 2026-05-22T08:34:37.868Z_

<details><summary>↩ Tool result · `toolu_01DF7xe9i56585FnCUyfvfB6`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.bbl:238:\newblock In \emph{Proceedings of AAAI}, volume~37, pages 10306--10314.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex:25:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.log:571:&lt;figures/fig1_decoupling_hero.pdf, id=230, 636.2769pt x 255.4914pt>
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.out:14:\BOOKMARK [1][-]{section.5}{\376\377\000C\000o\000n\000c\000l\000u\000s\000i\000o\000n}{}% 14
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:368:Table~\ref{tab:within_arch_pairwise} reports the full pairwise Jaccard matrix. Attention ratios are denoted by their h$k$-1 labels: h24-1 (4\%), h12-1 (7.7\%), h6-1 (14.3\%), h3-1 (25\%).
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:533:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:545:Disruption & 0.70 & 1.00 & 1.14 & 0.44 & 46.7\% \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:586:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:650:HellaSwag$^\dagger$ & .420 & .167 & .084 & .083 & .148 & .095 & .085 & $+$.019 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:689:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:4:  "./references.bib" 1779437101.61419 11334 20732b1b68f2838eaaafa8c3587175ca ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:16:  "/usr/share/texlive/texmf-dist/fonts/tfm/adobe/helvetic/phvb.tfm" 1136768653 2300 14616918391efa49ac8b481a75fbdc1a ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:22:  "/usr/share/texlive/texmf-dist/fonts/tfm/adobe/times/ptmr8t.tfm" 1136768653 6672 e3ab9e37e925f3045c9005e6d1473d56 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:39:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx8.tfm" 1136768653 1332 1fde11373e221473104d6cc5993f046e ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:43:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi12.tfm" 1136768653 1524 4414a8315f39513458b80dfc63bff03a ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:62:  "/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb" 1248133631 34811 78b52f49e893bcba91bd7581cdc144c0 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:68:  "/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb" 1248133631 36094 798f80770b3b148ceedd006d487db67c ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:71:  "/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb" 1248133631 32762 224316ccc9ad3ca0423a14971cfa7fc1 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:82:  "/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb" 1136849748 45458 a3faba884469519614ca56ba5f6b1de1 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:86:  "/usr/share/texlive/texmf-dist/fonts/vf/adobe/times/ptmr8c.vf" 1136768653 3556 8a9a6dcbcd146ef985683f677f4758a6 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:101:  "/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty" 1575152242 21514 b7557edcee22835ef6b03ede1802dad4 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:104:  "/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty" 1359763108 13829 94730e64147574077f8ecfea9bb69af4 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:106:  "/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd" 1359763108 961 d02606146ba5601b5645f987c92e6193 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:109:  "/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty" 1761946296 88471 b1bb09142edddebd46ba986341b867bd ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:112:  "/usr/share/texlive/texmf-dist/tex/latex/base/article.cls" 1748806692 20144 b966087dda3b194755eb460d32e2ef75 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:114:  "/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty" 1738182759 5048 0270515b828149155424600fd2d58ac5 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:117:  "/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd" 1738182759 2233 b5d3114ec3e0616e658a8e7b74e810f1 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:120:  "/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty" 1696191071 72619 ee90b6612147680fd73c3b1406a74245 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:133:  "/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty" 1580250785 17914 4c28a13fc3d975e6e81c9bea1d697276 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:134:  "/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def" 1752350709 48140 5e8a3a4aa88ae09b90d524926a067201 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:137:  "/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def" 1752350709 14249 e14b403fb70abdf1f6742598a63b0e2a ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:142:  "/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg" 1279039959 678 4792914a8f45be57bb98413425e4c7af ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:144:  "/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype-pdftex.def" 1752091573 49656 229fb67764dc0abf5c6f072ee0d27147 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:147:  "/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-cmr.cfg" 1739394495 22906 b0be544692bb405a84d147a96af5d777 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:151:  "/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty" 1731446765 6696 886c9f3087d0b973ed2c19aa79cb3023 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:154:  "/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd" 1137110629 774 61d7da1e9f9e74989b196d147e623736 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:158:  "/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty" 1750533675 9684 a33a14b82ce60d6e77cb9be689d79ee6 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:159:  "/usr/share/texlive/texmf-dist/tex/latex/url/url.sty" 1388531844 12796 8edb7d69a20b857904dd0ea757c14ec9 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:166:  "figures/fig1_decoupling_hero.pdf" 1779424651.14841 41730 e97709dd48dff7bb0befd7c031a9f83f ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.fdb_latexmk:174:  "sections/experiments.tex" 1779438822.7254 14986 f160c2109af892df42b40f9c66705b05 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:44:\item Ensemble proof-of-concept: majority vote vs.\ oracle analysis added to Conclusion.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:227:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.aux:868:\@LN{714}{8}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.aux:1415:\@LN{1167}{14}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.aux:1418:\@LN{1170}{14}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.aux:1421:\@LN{1171}{14}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.aux:1422:\@LN{1172}{14}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.aux:1423:\@LN{1173}{14}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.aux:1424:\@LN{1174}{14}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.aux:1425:\@LN{1175}{14}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.aux:1426:\@LN{1176}{14}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.aux:1427:\@LN{1177}{14}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.aux:1428:\@LN{1178}{14}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.aux:1429:\@LN{1179}{14}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.aux:1440:\@LN{1187}{14}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.aux:1450:\@LN{1197}{14}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.aux:1464:\@LN{1207}{14}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db22ccdc-929b-41db-89fe-1c4f1c662378",
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "2e1febb9-1938-4b30-b43d-6ffa6b1b2809",
  "sourceToolAssistantUUID": "db22ccdc-929b-41db-89fe-1c4f1c662378",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-22T08:34:39.426Z_

Let me search more specifically for the remaining numbers:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e1febb9-1938-4b30-b43d-6ffa6b1b2809",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJMQpZGMGKGYsCq7EnS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4a9912dd-3d94-4a39-a80a-1e034e72ad45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UsazpG1TSEKqMHiXvtw6zb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 10795,
      "cache_read_input_tokens": 43403,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10795,
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

_source line 30 · 2026-05-22T08:34:40.112Z_

<details open><summary>🔧 Tool call — Grep · `toolu_013J3sW2evAhUKdZfqen7ZYo`</summary>

```json
{
  "pattern": "15--45%|disagreement.*%",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a9912dd-3d94-4a39-a80a-1e034e72ad45",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJMQpZGMGKGYsCq7EnS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "59e38cbb-1222-4978-a43c-ef90c2652fb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UsazpG1TSEKqMHiXvtw6zb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 10795,
      "cache_read_input_tokens": 43403,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10795,
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

_source line 31 · 2026-05-22T08:34:40.127Z_

<details><summary>↩ Tool result · `toolu_013J3sW2evAhUKdZfqen7ZYo`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:227:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59e38cbb-1222-4978-a43c-ef90c2652fb9",
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "9077cd84-4647-49a8-89cb-45ecc6c9f8ec",
  "sourceToolAssistantUUID": "59e38cbb-1222-4978-a43c-ef90c2652fb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-22T08:34:40.547Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01TC77VJRX2q9T4UjGCWscJS`</summary>

```json
{
  "pattern": "462|615|426|495|548|395|helped.*hurt",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9077cd84-4647-49a8-89cb-45ecc6c9f8ec",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJMQpZGMGKGYsCq7EnS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "468451d7-e39e-4804-a87d-b8705e55e984",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UsazpG1TSEKqMHiXvtw6zb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 10795,
      "cache_read_input_tokens": 43403,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10795,
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

_source line 33 · 2026-05-22T08:34:40.571Z_

<details><summary>↩ Tool result · `toolu_01TC77VJRX2q9T4UjGCWscJS`</summary>

```text
&lt;persisted-output>
Output too large (25.1KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft--claude-sessions-paper-agent-b031d53b/210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc/tool-results/toolu_01TC77VJRX2q9T4UjGCWscJS.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.log:175:Package hyperref Info: Bookmarks ON on input line 4462.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.log:200:Package hyperref Info: Bookmarks ON on input line 4462.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.log:367:LaTeX Info: Redefining \ldots on input line 495.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.log:702:Overfull \hbox (17.8882pt too wide) in paragraph at lines 540--548
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:45:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:47:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:49:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:56:\caption{Predictive multiplicity at 1.3B. $\alpha$: ambiguity at h3-1 \citep{marx2020predictive}. $\bar{J}$: mean pairwise Jaccard of helped~(h) and hurt~(u) sets, averaged across four hybrid attention ratios and three architecture pairs. $\rho_\alpha$: Spearman $\rho$ between attention ratio and $\alpha$. Benchmarks ordered by $\alpha$.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:80:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:84:[Omitted long matching line]
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "468451d7-e39e-4804-a87d-b8705e55e984",
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "43d448e9-f171-4dd3-b263-0a9eb59f24b6",
  "sourceToolAssistantUUID": "468451d7-e39e-4804-a87d-b8705e55e984",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-22T08:34:41.174Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01PW4dsU7dmPVRwZEuvKYwgH`</summary>

```json
{
  "pattern": "0\\.70|0\\.74|AUC.*0\\.|disruption.*47%",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43d448e9-f171-4dd3-b263-0a9eb59f24b6",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJMQpZGMGKGYsCq7EnS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3c2e113e-84d0-4c1f-b378-cc8f94be0f56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UsazpG1TSEKqMHiXvtw6zb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 10795,
      "cache_read_input_tokens": 43403,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10795,
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

_source line 35 · 2026-05-22T08:34:41.197Z_

<details><summary>↩ Tool result · `toolu_01PW4dsU7dmPVRwZEuvKYwgH`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.log:323:Overfull \hbox (30.74617pt too wide) in paragraph at lines 77--78
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:32:SciQ & Mixed & $0.1$ & .950 & 0.87 & 0.74 & 1.19 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:49:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:338:HGRN2 & 0.672 & 0.701 & $+$0.029 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:513:Table~\ref{tab:prediction_auc} reports within-architecture prediction performance. All AUCs exceed 0.69, confirming that pure-model confidence is a reliable within-architecture predictor of attention effects. Disruption prediction is consistently stronger than rescue (mean AUC 0.73 vs.\ 0.70), reflecting the larger effect sizes in Control~1.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:533:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:545:Disruption & 0.70 & 1.00 & 1.14 & 0.44 & 46.7\% \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c2e113e-84d0-4c1f-b378-cc8f94be0f56",
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "587a68a8-4ac9-4f83-8252-515f23b2e139",
  "sourceToolAssistantUUID": "3c2e113e-84d0-4c1f-b378-cc8f94be0f56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-22T08:34:41.757Z_

<details open><summary>🔧 Tool call — Grep · `toolu_017mzhVH85bgCMuwk7YkXDpJ`</summary>

```json
{
  "pattern": "0\\.33|within.*architecture.*0\\.33|3×|3 times",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "587a68a8-4ac9-4f83-8252-515f23b2e139",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJMQpZGMGKGYsCq7EnS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8d2aba8b-8b26-42d2-b8bf-aca69517825b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UsazpG1TSEKqMHiXvtw6zb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 10795,
      "cache_read_input_tokens": 43403,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10795,
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

_source line 37 · 2026-05-22T08:34:41.778Z_

<details><summary>↩ Tool result · `toolu_017mzhVH85bgCMuwk7YkXDpJ`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.log:115:Package: pdftexcmds 2020-06-27 v0.33 Utility functions of pdfTeX for LuaTeX (HO
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.log:146:Package: pdftexcmds 2020-06-27 v0.33 Utility functions of pdfTeX for LuaTeX (HO
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:78:This saturation generalizes beyond LAMBADA: on all four main benchmarks, mean pairwise Jaccard shows no significant trend with attention ratio (all $\rho \leq 0.80$, $p \geq 0.333$; Appendix~\ref{app:cross_bench_jaccard}), with values uniformly between 0.08 and 0.11.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:80:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:347:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:359:GDN & 0.338 & 0.319 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:360:RetNet & 0.333 & 0.321 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:399:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:404:\caption{Mean pairwise Jaccard (helped sets, 3 architecture pairs) across attention ratios and benchmarks (1.3B scale). $\rho$: Spearman correlation between attention ratio and $\bar{J}$. All $p \geq 0.333$.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.aux:1492:\@writefile{lot}{\contentsline {table}{\numberline {17}{\ignorespaces Mean pairwise Jaccard (helped sets, 3 architecture pairs) across attention ratios and benchmarks (1.3B scale). $\rho $: Spearman correlation between attention ratio and $\bar  {J}$. All $p \geq 0.333$.}}{16}{table.caption.42}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.aux:1493:\newlabel{tab:cross_bench_jaccard}{{17}{16}{Mean pairwise Jaccard (helped sets, 3 architecture pairs) across attention ratios and benchmarks (1.3B scale). $\rho $: Spearman correlation between attention ratio and $\bar {J}$. All $p \geq 0.333$}{table.caption.42}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:64:We acknowledge that the within-arch Jaccard (${\sim}0.33$) vs.\ cross-arch Jaccard (${\sim}0.10$) comparison is ``a proxy for, not a direct measurement of, seed-versus-architecture effects'' (\S4.3). We retain it as descriptive because the magnitude is informative: attributing the $3\times$ gap entirely to seed would require seed effects to exceed the impact of replacing 25\% of layers with attention---implausible, though not directly testable.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:197:\item Within our data, within-architecture Jaccard (${\sim}0.33$) exceeds cross-architecture Jaccard (${\sim}0.10$) by ${\sim}3\times$. As R2 correctly notes, this comparison mixes attention-ratio variation with architecture variation. Nonetheless, the $3\times$ ratio provides a lower bound on the relative scale.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:215:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d2aba8b-8b26-42d2-b8bf-aca69517825b",
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "52333c9a-e3b9-481b-91fb-6cf098c9e075",
  "sourceToolAssistantUUID": "8d2aba8b-8b26-42d2-b8bf-aca69517825b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-22T08:34:42.996Z_

Let me search the appendix more carefully for the specific numbers and do targeted searches for the remaining values:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52333c9a-e3b9-481b-91fb-6cf098c9e075",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJMhBZF3vrxW8UeFSnV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c3d0bfc3-fbe0-465f-9bbc-f64680219e1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TnTVmygvcA2RQs2UXXKUxU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3470,
      "cache_read_input_tokens": 54198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3470,
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

_source line 39 · 2026-05-22T08:34:43.318Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QuKRwNTUqDbQD8AUbGcJZ4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex",
  "limit": 3000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3d0bfc3-fbe0-465f-9bbc-f64680219e1c",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJMhBZF3vrxW8UeFSnV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b64f3702-618f-4df2-8812-1f9a0513a1f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TnTVmygvcA2RQs2UXXKUxU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3470,
      "cache_read_input_tokens": 54198,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3470
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 133,
          "cache_read_input_tokens": 54198,
          "cache_creation_input_tokens": 3470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3470,
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

_source line 40 · 2026-05-22T08:34:43.649Z_

<details><summary>↩ Tool result · `toolu_01QuKRwNTUqDbQD8AUbGcJZ4`</summary>

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
14	\paragraph{Confirmatory benchmark set.} Six benchmarks were designated as confirmatory for Bonferroni correction: LAMBADA, HellaSwag, ARC-Challenge, WinoGrande, ARC-Easy, and MMLU. These were selected as representative of retrieval, reasoning, and mixed categories before any convergence analysis was performed. The taxonomy and benchmark selection were fixed before analysis; we describe this as a confirmatory/exploratory split rather than a formal pre-registration, since no external timestamp exists. The Bonferroni-adjusted significance threshold is $\alpha / 6 = 0.0083$. \textbf{Sensitivity:} correcting across all 10 benchmarks yields adjusted $p = 0.017 \times 10 = 0.170$, further from significance; the main text reports the confirmatory-set correction ($\times 6 = 0.100$).
15	
16	\paragraph{One-sided test.} If one adopts the prior that attention should reduce cross-architecture variance, the one-sided permutation $p$-value for LAMBADA is $1/120 \approx 0.0083$. Under 6-benchmark Bonferroni correction, this yields an adjusted $p = 0.050$, exactly at the conventional threshold. We report two-sided tests throughout the main text as the more conservative choice; the one-sided result is noted here for completeness.
17	
18	\paragraph{Exploratory benchmarks.} Four additional benchmarks (BoolQ, PIQA, SciQ, XStoryCloze) were added as exploratory tests. These are corrected separately across all 10 benchmarks (adjusted threshold $\alpha / 10 = 0.005$) and reported as exploratory throughout the paper.
19	
20	\paragraph{Supplementary benchmark.} COPA ($n = 100$) is treated as supplementary due to its small sample size. It is excluded from both correction families and reported separately with the $\dagger$ annotation in Table~\ref{tab:convergence}.
21	
22	\section{Convergence Detail}\label{app:convergence_detail}
23	
24	Beyond LAMBADA ($\rho = -1.0$), two benchmarks show moderate negative correlations that do not reach significance: ARC-Easy and MMLU (both $\rho = -0.7$, $p = .233$). Both are classified as ``Mixed'' tasks combining retrieval with reasoning demands. The sensitivity analysis (Appendix~\ref{app:sensitivity}) shows that MMLU's correlation reverses upon GDN exclusion ($\rho = +0.6$), indicating dependence on a single architecture; ARC-Easy's correlation is more stable. COPA ($n = 100$; supplementary) shows $\rho = -0.67$ with a large $\sigma$ ratio (5.57), consistent with LAMBADA's pattern but unreliable due to small sample size.
25	
26	Several benchmarks show positive or near-zero $\rho$ (BoolQ: $+0.2$; ARC-C: $+0.6$; HellaSwag: $+0.4$; WinoGrande: $+0.1$; SciQ: $+0.1$), indicating that attention does not systematically reduce cross-architecture variance on reasoning or comprehension tasks. The contrast with LAMBADA is consistent with attention's convergence benefit being specific to tasks requiring direct token-level recall \citep{arora2024zoology,arora2024based} rather than multi-step inference.
27	
28	\paragraph{Regression to the mean.} The direction of LAMBADA's aggregate convergence is consistent with regression to the mean: GDN (highest pure accuracy, 0.543) declines to 0.513 under h3-1, while HGRN2 (lowest, 0.484) rises to 0.514, yielding a $5\times$ $\sigma$ compression ($0.024 \to 0.005$). However, three observations argue against a purely statistical artifact. First, the $5\times$ reduction in cross-architecture $\sigma$ far exceeds typical regression amplitudes. Second, the direction is entirely determined by architecture identity, not random fluctuation: HGRN2 accuracy increases monotonically across all attention ratios, while GDN decreases monotonically---a pattern inconsistent with noise-driven mean reversion. Third, per-example analysis (\S\ref{ssec:per_example}) reveals architecture-specific mechanisms: GDN's net $-153$ examples and HGRN2's net $+153$ examples reflect distinct helped/hurt profiles with low cross-architecture Jaccard overlap, indicating that the aggregate convergence arises from structured, architecture-dependent per-example changes rather than symmetric regression.
29	
30	\section{Scale-Dependent Convergence}\label{app:scale_convergence}
31	
32	At 1.3B parameters, LAMBADA convergence is monotonic: $\sigma$ decreases at every attention level from 0\% through 25\% ($\rho = -1.0$). At 340M, convergence is partial: $\sigma$ reaches a maximum reduction of 56\% at intermediate attention ratios but rebounds at h3-1, yielding a net endpoint reduction of 36\%. The trajectory is non-monotonic, and the highest-attention model does not achieve the lowest cross-architecture variance. One possible interpretation is that at smaller scale, the capacity overhead of attention layers creates interference that offsets the retrieval benefit.
33	
34	This contrast is a preliminary observation from two data points (not a scaling law). Despite the aggregate divergence at 340M, mean pairwise Jaccard is similar at both scales ($J \approx 0.09$), extending the decoupling observation (\S\ref{ssec:decoupling}) to the scale dimension.
35	
36	\section{Sensitivity Analyses}\label{app:sensitivity}
37	
38	\subsection{Bootstrap Confidence Intervals}
39	
40	We construct 95\% bootstrap confidence intervals for the Spearman $\rho$ between attention ratio and cross-architecture $\sigma$ on LAMBADA using 10{,}000 resamples at the architecture level ($n = 3$ architectures). Of these resamples, 11.25\% are degenerate: they consist of same-architecture triplicates, which produce a constant $\sigma$ vector and therefore an undefined $\rho$ (division by zero in the rank correlation formula). These are excluded from the confidence interval computation because they carry no information about the correlation, not because they represent $\rho = 0$.
41	
42	The BCa (bias-corrected and accelerated) correction degenerates at the $\rho = -1.0$ boundary because the acceleration parameter requires finite jackknife variance, which collapses when the point estimate is at the distributional limit. We therefore report percentile confidence intervals instead. From the 88.75\% informative resamples, the 95\% percentile CI is $[-1.0,\,-0.7]$, which excludes zero.
43	
44	\subsection{GDN Exclusion Sensitivity}
45	
46	The GDN h3-1 configuration uses 16 attention heads rather than 32 (see Appendix~\ref{app:gdn_confound}). To assess the influence of this confound, we recompute all convergence correlations after excluding GDN, leaving two architectures (RetNet, HGRN2) at five attention ratios.
47	
48	Table~\ref{tab:gdn_sensitivity} reports the results for benchmarks where the correlation changes by $|\Delta\rho| \geq 0.3$. LAMBADA weakens from $\rho = -1.0$ to $\rho = -0.7$ ($p = .233$), consistent with GDN contributing to the convergence signal. MMLU reverses from $\rho = -0.7$ to $\rho = +0.6$, confirming that the moderate negative correlation on MMLU depends on GDN's inclusion and should not be interpreted as evidence of convergence.
49	
50	\begin{table}[h]
51	\centering
52	\small
53	\caption{Effect of GDN exclusion on Spearman $\rho$ (attention ratio vs.\ cross-architecture $\sigma$) at 1.3B scale. Only benchmarks with $|\Delta\rho| \geq 0.3$ shown.}
54	\label{tab:gdn_sensitivity}
55	\begin{tabular}{lrrrr}
56	\toprule
57	Benchmark & $\rho_{\text{all}}$ & $\rho_{\text{no-GDN}}$ & $\Delta\rho$ & $p_{\text{no-GDN}}$ \\
58	\midrule
59	LAMBADA & $-1.0$ & $-0.7$ & $+0.3$ & .233 \\
60	MMLU & $-0.7$ & $+0.6$ & $+1.3$ & .350 \\
61	\bottomrule
62	\end{tabular}
63	\end{table}
64	
65	\section{GDN Attention Head Confound}\label{app:gdn_confound}
66	
67	In the \citet{wang2025hybrid} model zoo, the GDN h3-1 configuration at 1.3B scale uses 16 attention heads per attention layer, while all other hybrid configurations (across GDN, RetNet, and HGRN2) use 32 attention heads. This is a design choice in the original model zoo, not an error. The reduced head count changes the per-head dimension and may affect the attention capacity of GDN h3-1 relative to other configurations.
68	
69	This confound is relevant because the convergence analysis measures cross-architecture $\sigma$ at each attention ratio. At the h3-1 ratio (25\% attention), GDN's attention layers have a different internal structure than those of RetNet and HGRN2, which could contribute to variance reduction (or inflation) for reasons unrelated to the recurrent--attention interaction under study.
70	
71	The sensitivity analysis in Appendix~\ref{app:sensitivity} shows that removing GDN weakens the LAMBADA convergence correlation from $\rho = -1.0$ to $\rho = -0.7$. This weakening is partially attributable to the reduced sample size ($n = 2$ architectures) and partially to the confound itself. We cannot separate these two effects with the available data.
72	
73	\section{Attention Weight Analysis}\label{app:attention_patterns}
74	
75	We extract attention weight matrices from the 1.3B h3-1 models of all three architectures using forward hooks on each attention layer. While \citet{ali2025hidden} show that SSM layers learn implicit attention patterns, our analysis focuses on the explicit attention layers interleaved within the hybrid architecture. For each layer, we compute the mean attention distribution across all 5{,}153 LAMBADA examples and measure cross-architecture similarity via cosine similarity.
76	
77	\subsection{Cross-Architecture Cosine Similarity}
78	
79	Table~\ref{tab:attn_cosine} reports cosine similarity between mean attention distributions at selected layers and averaged across all layers.
80	
81	\begin{table}[h]
82	\centering
83	\caption{Cosine similarity between mean attention weight distributions of architecture pairs at selected layers (1.3B h3-1 models on LAMBADA).}
84	\label{tab:attn_cosine}
85	\resizebox{\columnwidth}{!}{%
86	\begin{tabular}{lrrr}
87	\toprule
88	Layer & GDN--RetNet & GDN--HGRN2 & HGRN2--RetNet \\
89	\midrule
90	L2 (early) & 0.995 & 0.244 & 0.196 \\
91	L20 (deep) & 0.986 & 0.942 & 0.943 \\
92	\midrule
93	Mean (all layers) & 0.905 & 0.766 & 0.698 \\
94	\bottomrule
95	\end{tabular}%
96	}
97	\end{table}
98	
99	At layer 2, GDN and RetNet produce nearly identical attention distributions (cosine 0.995), while HGRN2 diverges from both (cosine $< 0.25$). By layer 20, all three architectures converge to similar attention patterns (cosine $> 0.94$). The layer-wise trajectory suggests that early-layer attention patterns are shaped by the preceding recurrent layers (which differ across architectures), while deeper layers converge regardless of the recurrent substrate.
100	
101	\subsection{Helped vs.\ Hurt Attention Entropy}
102	
103	To test whether the attention mechanism itself differs between helped and hurt examples, we compute the Shannon entropy of the attention distribution for each example at each attention layer and compare the mean entropy of helped examples against hurt examples within each architecture.
104	
105	\begin{table}[h]
106	\centering
107	\caption{Mean attention entropy difference (helped $-$ hurt) averaged across attention layers (1.3B h3-1 models on LAMBADA). Values near zero indicate that the attention mechanism does not discriminate between helped and hurt examples.}
108	\label{tab:attn_entropy}
109	\begin{tabular}{lr}
110	\toprule
111	Architecture & $\Delta H$ (helped $-$ hurt) \\
112	\midrule
113	GDN & $-0.0009$ \\
114	RetNet & $+0.0179$ \\
115	HGRN2 & $+0.0020$ \\
116	\bottomrule
117	\end{tabular}
118	\end{table}
119	
120	GDN and HGRN2 show negligible entropy differences ($|\Delta H| \leq 0.002$). RetNet's $\Delta H = +0.018$ is small in absolute terms but slightly larger; helped examples receive marginally more diffuse attention in RetNet. Across all three architectures, the differences are insufficient to explain the per-example divergence, consistent with per-example effects not being explained by attention weight patterns and likely originating in the recurrent layers.
121	
122	\subsection{Last-5 Attention Mass}
123	
124	We also measure the fraction of attention mass allocated to the last five tokens, which captures whether the attention mechanism concentrates differently on recent context for helped vs.\ hurt examples.
125	
126	\begin{table}[h]
127	\centering
128	\caption{Mean attention mass on last-5 tokens for helped and hurt examples, averaged across attention layers (1.3B h3-1 models on LAMBADA).}
129	\label{tab:attn_last5}
130	\begin{tabular}{lrr}
131	\toprule
132	Architecture & Helped & Hurt \\
133	\midrule
134	GDN & 0.0834 & 0.0831 \\
135	RetNet & 0.1578 & 0.1591 \\
136	HGRN2 & 0.0453 & 0.0467 \\
137	\bottomrule
138	\end{tabular}
139	\end{table}
140	
141	No architecture shows a meaningful difference in last-5 attention mass between helped and hurt examples (Table~\ref{tab:attn_last5}). This further supports the conclusion that the per-example divergence is not driven by differential attention allocation.
142	
143	\section{Cross-Scale Per-Example Comparisons}\label{app:cross_scale}
144	
145	\subsection{Within-Scale Pairwise Jaccard}
146	
147	Table~\ref{tab:within_scale_jaccard} reports the within-scale pairwise Jaccard similarity between architectures' helped and hurt sets at both scales. Mean values are similar across scales (340M: 0.094/0.090; 1.3B: 0.100/0.093), confirming that per-example architecture specificity is approximately scale-robust.
148	
149	\begin{table}[h]
150	\centering
151	\small
152	\caption{Within-scale pairwise Jaccard similarity of per-example effects (pure $\to$ h3-1) on LAMBADA. Each row compares the helped (or hurt) sets of two architectures at the same scale.}
153	\label{tab:within_scale_jaccard}
154	\begin{tabular}{llcc}
155	\toprule
156	Scale & Pair & $J_{\text{helped}}$ & $J_{\text{hurt}}$ \\
157	\midrule
158	\multirow{4}{*}{340M} & GDN--RetNet & 0.092 & 0.109 \\
159	& GDN--HGRN2 & 0.084 & 0.075 \\
160	& RetNet--HGRN2 & 0.108 & 0.085 \\
161	& \textit{Mean} & \textit{0.094} & \textit{0.090} \\
162	\midrule
163	\multirow{4}{*}{1.3B} & GDN--RetNet & 0.092 & 0.103 \\
164	& GDN--HGRN2 & 0.100 & 0.089 \\
165	& RetNet--HGRN2 & 0.108 & 0.087 \\
166	& \textit{Mean} & \textit{0.100} & \textit{0.093} \\
167	\bottomrule
168	\end{tabular}
169	\end{table}
170	
171	\subsection{Cross-Scale Pairwise Jaccard}
172	
173	For each architecture, we compare the helped and hurt sets of the pure $\to$ h3-1 transition at 340M and 1.3B scale on LAMBADA.
174	The comparison uses the same classification scheme as \S\ref{ssec:per_example}: an example is ``helped'' if it is correct only in the hybrid variant and ``hurt'' if correct only in the pure baseline.
175	All pairwise Jaccard values fall below 0.10, indicating that scale produces per-example predictive multiplicity analogous to the cross-architecture effect reported in \S\ref{ssec:per_example}.
176	
177	\begin{table}[h]
178	\centering
179	\caption{Cross-scale pairwise Jaccard similarity of per-example effects (pure $\to$ h3-1) between 340M and 1.3B on LAMBADA. All values below 0.10.}
180	\label{tab:cross_scale_jaccard}
181	\begin{tabular}{llcc}
182	\toprule
183	Architecture & Scale Pair & $J_{\text{helped}}$ & $J_{\text{hurt}}$ \\
184	\midrule
185	GDN & 340M $\leftrightarrow$ 1.3B & 0.047 & 0.087 \\
186	RetNet & 340M $\leftrightarrow$ 1.3B & 0.059 & 0.073 \\
187	HGRN2 & 340M $\leftrightarrow$ 1.3B & 0.089 & 0.055 \\
188	\midrule
189	Mean & & 0.065 & 0.072 \\
190	\bottomrule
191	\end{tabular}
192	\end{table}
193	
194	\section{Per-Example Effect Counts}\label{app:per_example_counts}
195	
196	Table~\ref{tab:per_example} reports the full per-example effect counts for each architecture at 1.3B scale.
197	
198	\begin{table}[h]
199	\centering
200	\caption{Per-example effects of attention (pure $\to$ h3-1) on 5{,}153 LAMBADA examples at 1.3B scale. $\bar{J}$: mean pairwise Jaccard similarity with other architectures across helped and hurt sets.}
201	\label{tab:per_example}
202	\begin{tabular}{lrrrr}
203	\toprule
204	Architecture & Helped & Hurt & Net & $\bar{J}$ \\
205	\midrule
206	GDN & 462 & 615 & $-$153 & .096 \\
207	RetNet & 426 & 495 & $-$69 & .100 \\
208	HGRN2 & 548 & 395 & $+$153 & .104 \\
209	\bottomrule
210	\end{tabular}
211	\end{table}
212	
213	\section{Normalized Jaccard Effect Size}\label{app:normalized_es}
214	
215	To assess whether low observed Jaccard reflects a floor effect imposed by unequal set sizes, we compute the theoretical upper bound $J_{\max} = \min(|A|,|B|) / \max(|A|,|B|)$ and the normalized effect size $(J_{\text{obs}} - J_{\text{null}}) / (J_{\max} - J_{\text{null}})$, which measures observed overlap as a fraction of the achievable range above chance. Table~\ref{tab:normalized_es} reports per-pair results.
216	
217	\begin{table}[h]
218	\centering
219	\small
220	\caption{Normalized Jaccard effect size for each architecture pair (1.3B h3-1 on LAMBADA). $J_{\max}$: theoretical upper bound given set sizes. Normalized ES: fraction of achievable overlap above chance.}
221	\label{tab:normalized_es}
222	\resizebox{\columnwidth}{!}{%
223	\begin{tabular}{llcccc}
224	\toprule
225	Category & Pair & $J_{\text{obs}}$ & $J_{\max}$ & $J_{\text{null}}$ & Norm.\ ES \\
226	\midrule
227	Helped & GDN--RetNet & .086 & .922 & .048 & .044 \\
228	 & GDN--HGRN2 & .099 & .843 & .050 & .062 \\
229	 & RetNet--HGRN2 & .108 & .777 & .042 & .090 \\
230	 & \textit{Mean} & \textit{.098} & \textit{.847} & \textit{.047} & \textit{.065} \\
231	\midrule
232	Hurt & GDN--RetNet & .092 & .805 & .056 & .048 \\
233	 & GDN--HGRN2 & .070 & .642 & .043 & .045 \\
234	 & RetNet--HGRN2 & .087 & .798 & .050 & .049 \\
235	 & \textit{Mean} & \textit{.083} & \textit{.748} & \textit{.050} & \textit{.047} \\
236	\bottomrule
237	\end{tabular}%
238	}
239	\end{table}
240	
241	All normalized effect sizes fall below 0.10, confirming that observed overlap reaches only 6--7\% of the theoretical maximum. The low Jaccard values cannot be attributed to set-size constraints.
242	
243	\section{ARC-Easy Per-Example Analysis}\label{app:arceasy}
244	
245	Table~\ref{tab:arceasy_effects} reports per-example effect counts on ARC-Easy ($N = 2{,}376$) at 1.3B scale for each attention ratio. Unlike LAMBADA, ARC-Easy shows no aggregate convergence ($\rho = -0.20$, $p = .783$). HGRN2 is net positive at all ratios; GDN and RetNet are mixed.
246	
247	\begin{table}[h]
248	\centering
249	\small
250	\caption{Per-example effects on ARC-Easy at 1.3B scale. Net = helped $-$ hurt.}
251	\label{tab:arceasy_effects}
252	\resizebox{\columnwidth}{!}{%
253	\begin{tabular}{llrrr}
254	\toprule
255	Architecture & Ratio & Helped & Hurt & Net \\
256	\midrule
257	\multirow{4}{*}{GDN} & h24-1 & 178 & 185 & $-$7 \\
258	& h12-1 & 176 & 206 & $-$30 \\
259	& h6-1 & 170 & 157 & $+$13 \\
260	& h3-1 & 171 & 180 & $-$9 \\
261	\midrule
262	\multirow{4}{*}{RetNet} & h24-1 & 158 & 168 & $-$10 \\
263	& h12-1 & 163 & 146 & $+$17 \\
264	& h6-1 & 159 & 147 & $+$12 \\
265	& h3-1 & 144 & 184 & $-$40 \\
266	\midrule
267	\multirow{4}{*}{HGRN2} & h24-1 & 160 & 119 & $+$41 \\
268	& h12-1 & 159 & 111 & $+$48 \\
269	& h6-1 & 185 & 118 & $+$67 \\
270	& h3-1 & 164 & 146 & $+$18 \\
271	\bottomrule
272	\end{tabular}%
273	}
274	\end{table}
275	
276	Table~\ref{tab:arceasy_ambiguity} reports the ambiguity $\alpha$ \citep{marx2020predictive} at each attention ratio for all four main benchmarks. Within-benchmark ranges are 0.004 (HellaSwag), 0.011 (PIQA), 0.025 (ARC-Easy), and 0.022 (LAMBADA), all below the 0.03 threshold reported in \S\ref{ssec:per_example}.
277	
278	\begin{table}[h]
279	\centering
280	\caption{Ambiguity $\alpha$ across attention ratios (1.3B scale). 95\% CI: BCa bootstrap (10{,}000 resamples) at the pure-recurrent configuration.}
281	\label{tab:arceasy_ambiguity}
282	\resizebox{\columnwidth}{!}{%
283	\begin{tabular}{lcccccc}
284	\toprule
285	Benchmark & Pure & h24-1 & h12-1 & h6-1 & h3-1 & 95\% CI (pure) \\
286	\midrule
287	PIQA & .143 & .138 & .132 & .143 & .140 & $[.127,\,.159]$ \\
288	HellaSwag & .148 & .150 & .148 & .146 & .150 & $[.141,\,.155]$ \\
289	ARC-Easy & .205 & .226 & .223 & .201 & .210 & $[.189,\,.221]$ \\
290	LAMBADA & .307 & .300 & .316 & .294 & .296 & $[.294,\,.319]$ \\
291	\bottomrule
292	\end{tabular}%
293	}
294	\end{table}
295	
296	\section{Jaccard Permutation Test}\label{app:jaccard_permutation}
297	
298	To assess whether the observed pairwise Jaccard similarities exceed what would be expected under independence, we perform a permutation test. For each architecture pair at 1.3B h3-1, we hold the helped (or hurt) set sizes fixed and randomly assign example indices to each set (10{,}000 permutations, seed 42). Table~\ref{tab:jaccard_perm} reports the observed $J$, the null baseline $J_{\text{null}}$ (mean over permutations), and the $z$-score.
299	
300	\begin{table}[h]
301	\centering
302	\caption{Permutation test for pairwise Jaccard similarity (1.3B h3-1 on LAMBADA, 10{,}000 permutations). All observed values significantly exceed the independence baseline.}
303	\label{tab:jaccard_perm}
304	\resizebox{\columnwidth}{!}{%
305	\begin{tabular}{llcccc}
306	\toprule
307	Category & Pair & $J_{\text{obs}}$ & $J_{\text{null}}$ & $z$ & $p$ \\
308	\midrule
309	Helped & GDN--HGRN2 & .100 & .051 & 7.11 & $<$.0001 \\
310	 & GDN--RetNet & .092 & .045 & 6.75 & $<$.0001 \\
311	 & HGRN2--RetNet & .108 & .049 & 8.61 & $<$.0001 \\
312	\midrule
313	Hurt & GDN--HGRN2 & .088 & .049 & 5.91 & $<$.0001 \\
314	 & GDN--RetNet & .103 & .056 & 6.85 & $<$.0001 \\
315	 & HGRN2--RetNet & .087 & .045 & 6.05 & $<$.0001 \\
316	\bottomrule
317	\end{tabular}%
318	}
319	\end{table}
320	
321	All six comparisons yield $z > 5.9$ ($p < .0001$). The null baseline averages $J_{\text{null}} \approx 0.049$; observed values are approximately twice this level. The overlap between architectures' per-example effect sets is therefore structured rather than a product of random set overlap given the set sizes.
322	
323	\section{Transformer Entrainment Comparison}\label{app:transformer_entrainment}
324	
325	To test whether attention layers make hybrid models' per-example behavior converge toward a pure Transformer, we compare the correct-example sets of each architecture's pure and h3-1 variants against a 1.3B Transformer baseline (accuracy 48.1\%) on LAMBADA. Table~\ref{tab:transformer_jaccard} reports the Jaccard similarity between each model's correct set and the Transformer's correct set.
326	
327	\begin{table}[h]
328	\centering
329	\caption{Jaccard similarity between each model's correct set and the Transformer correct set on LAMBADA (1.3B scale). All three h3-1 hybrids are more similar to the Transformer than their pure counterparts.}
330	\label{tab:transformer_jaccard}
331	\small
332	\begin{tabular}{lccc}
333	\toprule
334	Architecture & $J_{\text{pure,T}}$ & $J_{\text{h3-1,T}}$ & $\Delta$ \\
335	\midrule
336	GDN & 0.645 & 0.649 & $+$0.005 \\
337	RetNet & 0.679 & 0.694 & $+$0.015 \\
338	HGRN2 & 0.672 & 0.701 & $+$0.029 \\
339	\bottomrule
340	\end{tabular}
341	\end{table}
342	
343	All three architectures show positive $\Delta$: the h3-1 correct set is more similar to the Transformer correct set than the pure correct set is. The effect is strongest for HGRN2 ($+$0.029) and weakest for GDN ($+$0.005). This ordering is consistent with HGRN2 being the only architecture with a positive net per-example effect from attention (Table~\ref{tab:per_example}). The Transformer itself achieves the lowest accuracy among all models, so the convergence is not explained by hybrid models degrading toward Transformer-level performance; rather, adding attention shifts which specific examples the hybrid gets correct toward the Transformer's pattern.
344	
345	\section{Within-Architecture Per-Example Stability}\label{app:within_arch_stability}
346	
347	Per-example effect sets exhibit a three-tier Jaccard hierarchy on LAMBADA (1.3B scale). Under independence (permutation baseline), pairwise Jaccard is $J \approx 0.05$. Cross-architecture comparisons (different architectures at the same attention ratio) yield $J \approx 0.10$, approximately $2\times$ baseline. Within-architecture comparisons (same architecture across different attention ratios) yield $J \approx 0.33$, approximately $7\times$ baseline and $3\times$ the cross-architecture level. Architecture identity therefore has approximately three times the influence of attention dose on per-example effects.
348	
349	Table~\ref{tab:within_arch_summary} reports mean within-architecture Jaccard for each architecture. HGRN2 shows the highest helped overlap and lowest hurt overlap, consistent with its monotonically increasing helped count across ratios (479 $\to$ 548).
350	
351	\begin{table}[h]
352	\centering
353	\caption{Mean within-architecture pairwise Jaccard similarity across attention ratios (1.3B, LAMBADA). Each mean is computed over all six ratio pairs per architecture.}
354	\label{tab:within_arch_summary}
355	\begin{tabular}{lcc}
356	\toprule
357	Architecture & $\bar{J}_{\text{helped}}$ & $\bar{J}_{\text{hurt}}$ \\
358	\midrule
359	GDN & 0.338 & 0.319 \\
360	RetNet & 0.333 & 0.321 \\
361	HGRN2 & 0.373 & 0.291 \\
362	\midrule
363	\textit{Overall mean} & \textit{0.348} & \textit{0.310} \\
364	\bottomrule
365	\end{tabular}
366	\end{table}
367	
368	Table~\ref{tab:within_arch_pairwise} reports the full pairwise Jaccard matrix. Attention ratios are denoted by their h$k$-1 labels: h24-1 (4\%), h12-1 (7.7\%), h6-1 (14.3\%), h3-1 (25\%).
369	
370	\begin{table}[h]
371	\centering
372	\small
373	\caption{Within-architecture pairwise Jaccard similarity between helped and hurt sets at different attention ratios (1.3B, LAMBADA). Each cell compares the per-example effect sets of two attention configurations within the same architecture.}
374	\label{tab:within_arch_pairwise}
375	\resizebox{\columnwidth}{!}{%
376	\begin{tabular}{llcccccc}
377	\toprule
378	 & & \multicolumn{6}{c}{Ratio pair} \\
379	\cmidrule(lr){3-8}
380	Arch & Cat & h24--h12 & h24--h6 & h24--h3 & h12--h6 & h12--h3 & h6--h3 \\
381	\midrule
382	\multirow{2}{*}{GDN} & Helped & .345 & .335 & .311 & .344 & .341 & .352 \\
383	 & Hurt & .310 & .328 & .320 & .331 & .281 & .345 \\
384	\midrule
385	\multirow{2}{*}{RetNet} & Helped & .354 & .314 & .334 & .322 & .330 & .345 \\
386	 & Hurt & .316 & .334 & .307 & .301 & .324 & .343 \\
387	\midrule
388	\multirow{2}{*}{HGRN2} & Helped & .359 & .369 & .375 & .368 & .378 & .388 \\
389	 & Hurt & .292 & .289 & .298 & .273 & .309 & .287 \\
390	\bottomrule
391	\end{tabular}%
392	}
393	\end{table}
394	
395	Adjacent ratio pairs (e.g., h24-1 vs.\ h12-1) do not exhibit systematically higher Jaccard than non-adjacent pairs (e.g., h24-1 vs.\ h3-1). Across all architectures, the mean Jaccard for adjacent pairs is 0.353 (helped) and 0.311 (hurt), compared with 0.343 (helped) and 0.310 (hurt) for non-adjacent pairs. The negligible difference indicates that the mapping from attention dose to per-example effects is non-smooth: doubling the attention ratio does not produce a proportionally more similar set of affected examples.
396	
397	\section{Cross-Benchmark Jaccard Trajectories}\label{app:cross_bench_jaccard}
398	
399	To test whether Jaccard saturation is specific to LAMBADA or a general property, we compute mean pairwise Jaccard trajectories across all four hybrid attention ratios on all four main benchmarks. Table~\ref{tab:cross_bench_jaccard} reports the results. On every benchmark, Jaccard shows no statistically significant trend with attention ratio (all $\rho \leq 0.80$, $p \geq 0.333$), with values uniformly between 0.08 and 0.11. The saturation at the first attention level observed on LAMBADA (\S\ref{ssec:decoupling}) thus generalizes: once any attention is present, each architecture's per-example response is largely fixed regardless of attention dose.
400	
401	\begin{table}[h]
402	\centering
403	\small
404	\caption{Mean pairwise Jaccard (helped sets, 3 architecture pairs) across attention ratios and benchmarks (1.3B scale). $\rho$: Spearman correlation between attention ratio and $\bar{J}$. All $p \geq 0.333$.}
405	\label{tab:cross_bench_jaccard}
406	\begin{tabular}{@{}lcccccc@{}}
407	\toprule
408	Benchmark & h24-1 & h12-1 & h6-1 & h3-1 & $\rho$ & $p$ \\
409	\midrule
410	LAMBADA & .091 & .088 & .096 & .097 & 0.80 & .333 \\
411	HellaSwag & .084 & .081 & .091 & .086 & 0.60 & .417 \\
412	PIQA & .089 & .096 & .089 & .095 & 0.00 & 1.00 \\
413	ARC-Easy & .084 & .099 & .091 & .109 & 0.80 & .333 \\
414	\bottomrule
415	\end{tabular}
416	\end{table}
417	
418	\section{Target-Token Confidence Margin}
419	\label{app:confidence_margin}
420	
421	We analyze whether pure-model confidence on the target token predicts whether attention will help or hurt on a given example.
422	We define confidence as $|\log p_{\text{pure}}(y^*)|$, where $y^*$ is the target token: lower values indicate higher probability (near-correct).
423	We initially tested raw perplexity as a predictor of helped/hurt status, but found that within-category controls (C1/C2) are necessary to isolate attention effects from the definitional confound between pure-correct and pure-wrong populations.
424	
425	Table~\ref{tab:cm_c1} compares hurt versus stayed-right samples (both pure-correct): hurt samples have significantly lower target-token probability (higher $|\log p|$), confirming that weakly-correct predictions are vulnerable to attention disruption.
426	Table~\ref{tab:cm_c2} compares helped versus stayed-wrong samples (both pure-wrong): helped samples have higher target-token probability (lower $|\log p|$), confirming that near-miss errors are rescuable.
427	This pattern is consistent across all three architectures ($|d| = 0.73$--$0.92$, all $p < 10^{-54}$) but does not alter the cross-architecture Jaccard findings---within-architecture predictability coexists with cross-architecture divergence.
428	
429	\begin{table}[h]
430	\centering
431	\caption{Control 1: Pure-correct samples---hurt vs.\ stayed-right. Higher mean $|\log p|$ indicates lower target-token probability (less confident correct).}
432	\label{tab:cm_c1}
433	\resizebox{\columnwidth}{!}{%
434	\begin{tabular}{lrrrrr}
435	\toprule
436	Architecture & $n_{\text{hurt}}$ & $n_{\text{stay}}$ & Hurt mean & Stay mean & Cohen's $d$ \\
437	\midrule
438	GDN (h12-1) & 519 & 2281 & 1.049 & 0.576 & 0.87 \\
439	RetNet (h3-1) & 497 & 2169 & 1.293 & 0.785 & 0.83 \\
440	HGRN2 (h3-1) & 392 & 2102 & 1.481 & 0.899 & 0.92 \\
441	\bottomrule
442	\end{tabular}
443	}
444	\end{table}
445	
446	\begin{table}[h]
447	\centering
448	\caption{Control 2: Pure-wrong samples---helped vs.\ stayed-wrong. Lower mean $|\log p|$ indicates higher target-token probability (near-miss error).}
449	\label{tab:cm_c2}
450	\resizebox{\columnwidth}{!}{%
451	\begin{tabular}{lrrrrr}
452	\toprule
453	Architecture & $n_{\text{help}}$ & $n_{\text{stay}}$ & Help mean & Stay mean & Cohen's $d$ \\
454	\midrule
455	GDN (h12-1) & 480 & 1873 & 2.459 & 4.189 & $-$0.75 \\
456	RetNet (h3-1) & 420 & 2067 & 2.478 & 4.103 & $-$0.73 \\
457	HGRN2 (h3-1) & 548 & 2111 & 2.500 & 4.112 & $-$0.77 \\
458	\bottomrule
459	\end{tabular}
460	}
461	\end{table}
462	
463	\subsection{Cross-Benchmark Extension}\label{app:cm_cross}
464	
465	The confidence margin pattern extends beyond LAMBADA to multiple-choice benchmarks, though with smaller effect sizes. Table~\ref{tab:cm_cross_c2} reports the rescue analysis (helped vs.\ stayed-wrong) on HellaSwag and ARC-Easy. All nine comparisons (three benchmarks $\times$ three architectures) are significant, confirming that attention consistently rescues near-miss errors regardless of task type. Effect sizes range from small on HellaSwag ($d = 0.13$--$0.17$) to medium on ARC-Easy ($d = 0.51$--$0.60$), compared to large on LAMBADA ($d = 0.73$--$0.77$); the attenuation on HellaSwag reflects noisier confidence proxies under length-normalized scoring. Table~\ref{tab:cm_cross_c1} reports the disruption analysis (hurt vs.\ stayed-right); two of six comparisons are significant (all on ARC-Easy) with small effect sizes ($d = 0.13$--$0.26$), indicating that the disruption signal is weaker on multiple-choice tasks and absent on HellaSwag under \texttt{acc\_norm}. The asymmetry between rescue and disruption reflects task structure: near-miss errors are an intrinsic sample property (the model almost produced the correct answer regardless of format), while borderline correctness in multiple-choice settings depends on relative option ranking rather than absolute confidence, reducing the raw log-likelihood margin's predictive power for vulnerability.
466	
467	\begin{table}[h]
468	\centering
469	\caption{Cross-benchmark rescue analysis (Control 2): helped vs.\ stayed-wrong on HellaSwag and ARC-Easy (1.3B h3-1).}
470	\label{tab:cm_cross_c2}
471	\resizebox{\columnwidth}{!}{%
472	\begin{tabular}{llrr}
473	\toprule
474	Benchmark & Architecture & Cohen's $d$ & $p$ \\
475	\midrule
476	HellaSwag & GDN & $-$0.166 & $6.1 \times 10^{-4}$ \\
477	 & RetNet & $-$0.132 & $1.4 \times 10^{-2}$ \\
478	 & HGRN2 & $-$0.164 & $1.4 \times 10^{-3}$ \\
479	\midrule
480	ARC-Easy & GDN & $-$0.60 & $1.0 \times 10^{-13}$ \\
481	 & RetNet & $-$0.51 & $5.3 \times 10^{-10}$ \\
482	 & HGRN2 & $-$0.53 & $5.4 \times 10^{-10}$ \\
483	\bottomrule
484	\end{tabular}%
485	}
486	\end{table}
487	
488	\begin{table}[h]
489	\centering
490	\caption{Cross-benchmark disruption analysis (Control 1): hurt vs.\ stayed-right on HellaSwag and ARC-Easy (1.3B h3-1).}
491	\label{tab:cm_cross_c1}
492	\resizebox{\columnwidth}{!}{%
493	\begin{tabular}{llrrl}
494	\toprule
495	Benchmark & Architecture & Cohen's $d$ & $p$ & Sig.? \\
496	\midrule
497	HellaSwag & GDN & 0.009 & .999 & No \\
498	 & RetNet & $-$0.035 & .453 & No \\
499	 & HGRN2 & $-$0.062 & .274 & No \\
500	\midrule
501	ARC-Easy & GDN & 0.26 & $3.2 \times 10^{-4}$ & Yes \\
502	 & RetNet & 0.22 & $2.8 \times 10^{-3}$ & Yes \\
503	 & HGRN2 & 0.13 & .145 & No \\
504	\bottomrule
505	\end{tabular}%
506	}
507	\end{table}
508	
509	\subsection{Prediction Framework}\label{app:prediction_framework}
510	
511	We formalize the confidence margin analysis as a binary prediction task: given a pure-model example and its target-token $|\log p|$, predict whether attention will change the example's correctness. Using the within-category summary statistics (Tables~\ref{tab:cm_c1},~\ref{tab:cm_c2}), we derive analytic AUC from Cohen's $d$ via $\text{AUC} = \Phi(|d|/\sqrt{2})$ and compute Gaussian-intersection thresholds (the $|\log p|$ value at which the two group densities intersect under equal priors).
512	
513	Table~\ref{tab:prediction_auc} reports within-architecture prediction performance. All AUCs exceed 0.69, confirming that pure-model confidence is a reliable within-architecture predictor of attention effects. Disruption prediction is consistently stronger than rescue (mean AUC 0.73 vs.\ 0.70), reflecting the larger effect sizes in Control~1.
514	
515	\begin{table}[h]
516	\centering
517	\small
518	\caption{Within-architecture prediction of attention effects on LAMBADA (1.3B). AUC derived analytically from Cohen's $d$.}
519	\label{tab:prediction_auc}
520	\begin{tabular}{@{}lcccc@{}}
521	\toprule
522	Architecture & Rescue AUC & $d$ & Disruption AUC & $d$ \\
523	\midrule
524	GDN (h12-1) & .701 & 0.75 & .732 & 0.87 \\
525	RetNet (h3-1) & .696 & 0.73 & .722 & 0.83 \\
526	HGRN2 (h3-1) & .708 & 0.77 & .743 & 0.92 \\
527	\midrule
528	Mean & .702 & --- & .732 & --- \\
529	\bottomrule
530	\end{tabular}
531	\end{table}
532	
533	Despite similar within-architecture AUC, the optimal prediction thresholds differ across architectures for disruption but not rescue (Table~\ref{tab:threshold_gap}). Rescue thresholds cluster tightly (range 0.03 in $|\log p|$), indicating that the rescuability boundary---the confidence level below which pure-wrong examples are likely to be corrected by attention---is architecture-invariant. Disruption thresholds span a 47\% relative range (GDN: 0.70, RetNet: 1.00, HGRN2: 1.14), meaning that the same confidence level on a pure-correct example may predict vulnerability in one architecture but safety in another. This asymmetry constitutes a second dimension of multiplicity beyond per-example disagreement: all three architectures agree on which wrong answers are rescuable, but disagree on which correct answers are vulnerable to disruption.
534	
535	\begin{table}[h]
536	\centering
537	\small
538	\caption{Gaussian-intersection prediction thresholds ($|\log p|$) across architectures. Relative spread: range/mean.}
539	\label{tab:threshold_gap}
540	\begin{tabular}{@{}lccccr@{}}
541	\toprule
542	 & GDN & RetNet & HGRN2 & Range & Rel.\ spread \\
543	\midrule
544	Rescue & 3.32 & 3.29 & 3.31 & 0.03 & 1.0\% \\
545	Disruption & 0.70 & 1.00 & 1.14 & 0.44 & 46.7\% \\
546	\bottomrule
547	\end{tabular}
548	\end{table}
549	
550	\section{BoolQ Supplementary Analysis}
551	\label{app:boolq}
552	
553	BoolQ ($N = 3{,}270$; comprehension, binary yes/no classification) shows the highest ambiguity among the benchmarks we analyzed ($\alpha \approx 0.45$), but the Jaccard significance pattern is mixed: only 12 of 24 architecture $\times$ attention-ratio pair combinations yield $p < .01$. In particular, the RetNet--HGRN2 pair produces 0/8 significant Jaccard values, with several normalized effect sizes below zero, suggesting anti-correlated per-example effects for this pair.
554	
555	\paragraph{Binary classification baseline.} BoolQ is binary classification (two answer choices), whereas LAMBADA, HellaSwag, and ARC-Easy involve open vocabulary prediction or four-way multiple choice. Under a binary task, the null Jaccard baseline $J_{\text{null}}$ is higher because chance overlap between helped/hurt sets is larger when there are fewer ways to be wrong. This elevates the significance threshold: observed Jaccard must be substantially higher to exceed the null, which explains why 12/24 pairs fail to reach significance despite $\bar{J}_h = 0.103$ and $\bar{J}_u = 0.098$---values comparable to the four main benchmarks.
556	
557	\paragraph{Per-example summary.} Table~\ref{tab:boolq_multiplicity} reports the key metrics. The high $\alpha$ reflects that BoolQ examples are more sensitive to architectural variation in the presence of attention: approximately half of all examples change correctness status for at least one architecture. However, the mixed Jaccard significance prevents us from confidently concluding that the cross-architecture overlap structure matches the pattern observed on the four main benchmarks.
558	
559	\begin{table}[h]
560	\centering
561	\small
562	\caption{BoolQ predictive multiplicity at 1.3B (h3-1).}
563	\label{tab:boolq_multiplicity}
564	\begin{tabular}{@{}lcccccc@{}}
565	\toprule
566	 & $N$ & $\alpha$ & $\bar{J}_{h}$ & $\bar{J}_{u}$ & Sig.\ pairs & $\rho_\alpha$ \\
567	\midrule
568	BoolQ & 3270 & .45 & .103 & .098 & 12/24 & $+0.1$ \\
569	\bottomrule
570	\end{tabular}
571	\par\vspace{1pt}
572	{\footnotesize RetNet--HGRN2: 0/8 significant; multiple normalized ES $< 0$.}
573	\end{table}
574	
575	The significant Jaccard overlap concentrates in GDN--RetNet pairs (8/8 significant), while RetNet--HGRN2 shows none (0/8). This pair-specificity does not appear on the four main benchmarks, where all architecture pairs show significant overlap; it may reflect a BoolQ-specific interaction between binary classification structure and particular recurrent architectures rather than a general property of architecture pairs.
576	
577	\paragraph{Confidence margin.} Confidence margin analysis on BoolQ shows the rescue pattern (C2) partially holds (2/3 architectures significant, $d = 0.16$--$0.36$) but the disruption pattern (C1) is absent (0/3, $|d| \leq 0.10$), consistent with compressed log-likelihood ranges in binary classification reducing the predictive power of confidence margins. This extends the gradient observed across LAMBADA, ARC-Easy, and HellaSwag: C1 effect sizes decrease from open-ended prediction ($d \approx 0.9$, LAMBADA) through ARC-Easy ($d \approx 0.1$--$0.3$) to HellaSwag ($d \approx 0$ under \texttt{acc\_norm}) and binary classification ($d \approx 0$, BoolQ). The gradient broadly tracks the coefficient of variation (CV) of the log-likelihood confidence proxy: LAMBADA ($\text{CV} = 0.75$) $>$ ARC-Easy ($0.54$) $>$ HellaSwag ($0.49$) $>$ BoolQ ($0.22$). BoolQ's high-frequency short completions (``\,yes''/``\,no'') yield elevated baseline log-likelihoods (mean $|\text{loglik}| = 3.04$ vs.\ $0.84$ for LAMBADA) with similar absolute spread (IQR $\approx 0.9$), compressing the relative variation and rendering the confidence margin unable to separate borderline-correct from robustly-correct examples.
578	
579	\paragraph{Interpretation.} The RetNet--HGRN2 anti-correlation may reflect different error modes specific to binary classification: when one architecture's recurrent state resolves a yes/no ambiguity through attention, the other architecture's resolution may be disrupted by the same attention intervention. This pattern warrants further investigation with additional binary classification benchmarks to determine whether it is BoolQ-specific or characteristic of two-choice tasks more broadly.
580	
581	\section{WinoGrande Supplementary Analysis}
582	\label{app:winogrande}
583	
584	WinoGrande ($N = 1{,}267$; reasoning, two-choice coreference resolution) shows high ambiguity ($\alpha \approx 0.41$ at h3-1) but mixed Jaccard significance: 10 of 24 architecture $\times$ attention-ratio pair combinations yield $p < .01$. Mean pairwise Jaccard ($\bar{J}_h = 0.110$, $\bar{J}_u = 0.103$) is comparable to the four main benchmarks, but the elevated null baseline from near-chance accuracy (${\sim}60\%$) reduces statistical power to detect above-chance overlap.
585	
586	\paragraph{Near-chance accuracy.} WinoGrande accuracy across hybrid configurations ranges from 59\% to 62\%, close to the two-choice chance level of 50\%. At near-chance accuracy, a large fraction of examples are borderline---small perturbations (such as adding attention) can flip predictions in either direction, inflating the helped and hurt sets and consequently $\alpha$. This structural property, shared with BoolQ (${\sim}59\%$ accuracy, $\alpha \approx 0.45$), may partially explain the elevated $\alpha$ rather than task-intrinsic multiplicity. PIQA (73\% accuracy, $\alpha = 0.14$) and HellaSwag (60\% normalized accuracy, $\alpha = 0.15$) demonstrate that near-chance accuracy is not the sole driver, but we cannot fully exclude it as a contributing factor for WinoGrande and BoolQ.
587	
588	\begin{table}[h]
589	\centering
590	\small
591	\caption{WinoGrande predictive multiplicity at 1.3B (h3-1).}
592	\label{tab:winogrande_multiplicity}
593	\begin{tabular}{@{}lcccccc@{}}
594	\toprule
595	 & $N$ & $\alpha$ & $\bar{J}_{h}$ & $\bar{J}_{u}$ & Sig.\ pairs & $\rho_\alpha$ \\
596	\midrule
597	WinoGrande & 1267 & .41 & .110 & .103 & 10/24 & $-0.9$ \\
598	\bottomrule
599	\end{tabular}
600	\par\vspace{1pt}
601	{\footnotesize $\alpha$ variation across ratios: 0.054 ($> 0.03$ threshold of main benchmarks).}
602	\end{table}
603	
604	\section{340M Per-Example Analysis}\label{app:scale_per_example}
605	
606	\subsection{LAMBADA}
607	
608	At 340M, LAMBADA per-example multiplicity closely matches the 1.3B pattern: $\alpha = 0.313$ (vs.\ 0.307 at 1.3B), with mean pairwise Jaccard $\bar{J} \approx 0.089$ (vs.\ 0.095). Per-example directionality is preserved: HGRN2 shows net positive effects at h3-1 ($+238$ examples), while GDN ($-256$) and RetNet ($-106$) show net negative effects, mirroring the 1.3B profile (HGRN2 $+153$, GDN $-153$, RetNet $-69$).
609	
610	However, aggregate convergence is absent at 340M: $\rho = -0.50$ ($p = .45$), with non-monotonic $\sigma$ across attention ratios ($0.025 \to 0.012 \to 0.018 \to 0.011 \to 0.016$). This contrasts sharply with 1.3B ($\rho = -1.0$, $p = .017$, monotonic $\sigma$ decrease). The decoupling between per-example divergence and aggregate convergence thus manifests differently across scales: at 340M, per-example multiplicity is present but aggregate convergence is not, suggesting that convergence requires sufficient model capacity while multiplicity does not.
611	
612	Within-benchmark $\alpha$ variation across attention ratios is also larger at 340M (0.047, from 0.313 at pure to 0.266 at h3-1) than at 1.3B ($< 0.03$; \S\ref{ssec:per_example}), suggesting that smaller models are more sensitive to the attention ratio in terms of per-example disagreement patterns.
613	
614	\begin{table}[h]
615	\centering
616	\small
617	\caption{340M vs.\ 1.3B LAMBADA comparison.}
618	\label{tab:scale_comparison}
619	\begin{tabular}{@{}lcc@{}}
620	\toprule
621	 & 340M & 1.3B \\
622	\midrule
623	$\alpha$ (pure) & .313 & .307 \\
624	$\bar{J}$ (h3-1) & .089 & .095 \\
625	$\rho_\sigma$ & $-0.50$ & $-1.0$ \\
626	$p$ & .45 & .017 \\
627	GDN net & $-256$ & $-153$ \\
628	HGRN2 net & $+238$ & $+153$ \\
629	\bottomrule
630	\end{tabular}
631	\end{table}
632	
633	\subsection{Cross-Benchmark Scale Comparison}
634	
635	Table~\ref{tab:340m_multi_bench} extends the scale comparison to all four main benchmarks. Two patterns emerge. First, $\alpha$ is systematically higher at 340M across all benchmarks, with the largest gap on ARC-Easy ($+$8.4pp) and the smallest on LAMBADA ($+$0.6pp). Second, pairwise Jaccard remains stable across scales ($\bar{J}_h = 0.08$--$0.10$ at both scales), confirming that the qualitative pattern of per-example multiplicity---which architectures affect which examples---is scale-robust even as its magnitude increases at smaller scale. Notably, the $\alpha$ inflation does not track accuracy loss: HellaSwag has the largest accuracy gap between scales yet the smallest $\Delta\alpha$ ($+$1.9pp), while ARC-Easy has a smaller accuracy gap but the largest $\Delta\alpha$ ($+$8.4pp), arguing against accuracy as the primary driver of scale-dependent multiplicity.
636	
637	\begin{table}[h]
638	\centering
639	\small
640	\caption{340M vs.\ 1.3B per-example multiplicity across four benchmarks. $\alpha$: ambiguity at pure-recurrent configuration. Acc: mean accuracy across three architectures at pure-recurrent. $\bar{J}_{h}$/$\bar{J}_{u}$: mean pairwise Jaccard of helped/hurt sets. $\Delta\alpha$: 340M $-$ 1.3B.}
641	\label{tab:340m_multi_bench}
642	\resizebox{\columnwidth}{!}{%
643	\begin{tabular}{lcccccccr}
644	\toprule
645	 & \multicolumn{4}{c}{340M} & \multicolumn{3}{c}{1.3B} & \\
646	\cmidrule(lr){2-5} \cmidrule(lr){6-8}
647	Benchmark & Acc & $\alpha$ & $\bar{J}_{h}$ & $\bar{J}_{u}$ & $\alpha$ & $\bar{J}_{h}$ & $\bar{J}_{u}$ & $\Delta\alpha$ \\
648	\midrule
649	PIQA & .663 & .181 & .090 & .085 & .143 & .091 & .094 & $+$.038 \\
650	HellaSwag$^\dagger$ & .420 & .167 & .084 & .083 & .148 & .095 & .085 & $+$.019 \\
651	ARC-Easy & .594 & .289 & .098 & .103 & .205 & .092 & .099 & $+$.084 \\
652	LAMBADA & --- & .313 & .089 & .090 & .307 & .095 & .093 & $+$.006 \\
653	\bottomrule
654	\multicolumn{9}{l}{\footnotesize $^\dagger$\texttt{acc\_norm}. LAMBADA accuracy omitted (evaluated in separate run).}
655	\end{tabular}%
656	}
657	\end{table}
658	
659	Convergence is absent at 340M across all benchmarks (all $|\rho| \leq 0.4$, $p \geq .45$), in contrast to 1.3B where LAMBADA shows monotonic convergence. The absence of convergence at 340M extends beyond LAMBADA to HellaSwag ($\rho = 0.4$, $p = .52$), PIQA ($\rho = 0.3$, $p = .68$), and ARC-Easy ($\rho = -0.1$, $p = .95$).
660	
661	\section{Subsample Sensitivity of \texorpdfstring{$\alpha$}{α}}\label{app:subsample_sensitivity}
662	
663	To assess the reliability of $\alpha$ estimation at different sample sizes, we repeatedly subsample each benchmark (1{,}000 bootstrap replicates, seed 42) and compute the 95\% CI width of $\alpha$.
664	
665	\begin{table}[h]
666	\centering
667	\small
668	\caption{$\alpha$ estimation stability: 95\% CI width by subsample size.}
669	\label{tab:subsample}
670	\resizebox{\columnwidth}{!}{%
671	\begin{tabular}{@{}lrrrrr@{}}
672	\toprule
673	Benchmark & $n = 100$ & $n = 200$ & $n = 500$ & $n = 1000$ & Full $N$ \\
674	\midrule
675	PIQA & .130 & .095 & .066 & .045 & .034 \\
676	HellaSwag & .140 & .100 & .062 & .044 & .013 \\
677	ARC-Easy & .160 & .105 & .072 & .050 & .032 \\
678	LAMBADA & .180 & .125 & .082 & .057 & .025 \\
679	\bottomrule
680	\end{tabular}}
681	\par\vspace{1pt}
682	{\footnotesize At $n = 100$, CI width (0.13--0.18) spans the entire four-benchmark $\alpha$ range (0.14--0.30), rendering $\alpha$ estimation unreliable. This justifies excluding COPA ($n = 100$) from the per-example analysis.}
683	\end{table}
684	
685	\section{Complementarity Decomposition}\label{app:complementarity}
686	
687	We decompose the three-architecture vote on each example into four categories: unanimous correct (3/3), majority correct (2/3), minority correct (1/3), and unanimous wrong (0/3). This decomposition explains the structural failure of majority vote despite substantial per-example complementarity.
688	
689	Table~\ref{tab:complementarity} reports the decomposition at h3-1 (25\% attention). Majority vote benefits only from 2/3 examples (where the correct answer holds a majority) but is actively harmed by 1/3 examples (where the correct architecture is outvoted). On LAMBADA, HellaSwag, and ARC-Easy, the MV exploitation ratio---the fraction of complementary examples where MV selects correctly---hovers near 51\%, indicating a near-even split between MV-exploitable and MV-hostile disagreements. The oracle, by contrast, exploits both categories, explaining the large oracle--MV gap ($+7$--$14$\,pp).
690	
691	\begin{table}[h]
692	\centering
693	\small
694	\caption{Complementarity decomposition at 1.3B h3-1. Fractions of total examples in each vote category. MV expl.: fraction of complementary examples where majority vote is correct.}
695	\label{tab:complementarity}
696	\begin{tabular}{@{}lccccr@{}}
697	\toprule
698	Benchmark & 3/3 & 2/3 & 1/3 & 0/3 & MV expl. \\
699	\midrule
700	LAMBADA & .361 & .151 & .145 & .343 & 51.1\% \\
701	HellaSwag & .519 & .078 & .073 & .331 & 51.6\% \\
702	ARC-Easy & .603 & .107 & .103 & .187 & 50.9\% \\
703	BoolQ & .376 & .257 & .197 & .170 & 56.6\% \\
704	\bottomrule
705	\end{tabular}
706	\end{table}
707	
708	This near-50\% exploitation ratio is structurally invariant across attention ratios: on LAMBADA, the ratio ranges from 51.1\% to 54.4\% across all five configurations; on HellaSwag, from 50.3\% to 51.6\%. Attention changes neither the amount nor the structure of cross-architecture complementarity.
709	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b64f3702-618f-4df2-8812-1f9a0513a1f4",
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "873bbfcd-f841-436d-86a0-d4f1cb17e611",
  "sourceToolAssistantUUID": "b64f3702-618f-4df2-8812-1f9a0513a1f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-22T08:34:45.256Z_

Now let me search more carefully for the specific discrepancy I found earlier regarding the normalized effect size:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "873bbfcd-f841-436d-86a0-d4f1cb17e611",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJMqRQVtjJZe2uYZba9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f6430d3c-fdc5-4685-b456-df7391d5f584",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LqTnP5HvSw9zJStesEaiVD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 18397,
      "cache_read_input_tokens": 57668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18397,
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

_source line 42 · 2026-05-22T08:34:46.578Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01UBjXoaUi1NPZKfv6EkySML`</summary>

```json
{
  "pattern": "5--7%|normalized effect size.*5|5--7.*achievable",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6430d3c-fdc5-4685-b456-df7391d5f584",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJMqRQVtjJZe2uYZba9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9c065d07-a629-4ebc-9a59-4fc182ce6905",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LqTnP5HvSw9zJStesEaiVD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 18397,
      "cache_read_input_tokens": 57668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18397,
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

### Tool result

_source line 43 · 2026-05-22T08:34:46.600Z_

<details><summary>↩ Tool result · `toolu_01UBjXoaUi1NPZKfv6EkySML`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:45:\item Jaccard floor effect: normalized ES (5--7\% of achievable range) added to \S4.2.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:138:Regarding the Jaccard floor effect concern: observed $\bar{J} \approx 0.10$ is far below the theoretical maximum $J_{\max} = 0.78$--$0.92$ (given helped-set sizes of 426--548 out of $N = 5{,}153$). The normalized effect size is only 5--7\% of the achievable range above chance (\S4.2). This rules out ceiling constraints as an alternative explanation for Jaccard saturation---there is ample room for $J$ to increase if attention were homogenizing per-example behavior.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:251:\response{We have added a normalized effect size analysis to \S4.2: observed $\bar{J} \approx 0.10$ vs.\ theoretical maximum $J_{\max} = 0.78$--$0.92$ (given helped-set sizes). The normalized effect size is only 5--7\% of the achievable range above chance (normalized ES 0.065 helped, 0.047 hurt), ruling out ceiling constraints as an alternative explanation.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c065d07-a629-4ebc-9a59-4fc182ce6905",
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "b2428a07-4ca0-4ecb-8812-011ba868ee14",
  "sourceToolAssistantUUID": "9c065d07-a629-4ebc-9a59-4fc182ce6905",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-22T08:34:51.967Z_

Excellent! I found a critical inconsistency. Let me check what the paper currently says in the main text sections:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2428a07-4ca0-4ecb-8812-011ba868ee14",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJN4nKjggFYrLGEBq1L",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8519b702-45ae-4eaf-b4b2-0b56b844c238",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DHRVEFuR5WmNvuaPFMswfp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 585,
      "cache_read_input_tokens": 76065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 585,
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

_source line 45 · 2026-05-22T08:34:52.715Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01WmN9uD5Xm8DR4RLrE5DWdm`</summary>

```json
{
  "pattern": "normalized.*6--7%|effect size.*6--7%|0.065 helped.*0.062 hurt|achievable range.*6--7%",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8519b702-45ae-4eaf-b4b2-0b56b844c238",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJN4nKjggFYrLGEBq1L",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b965ed61-d0d5-4065-924c-89f7b8b97ca1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DHRVEFuR5WmNvuaPFMswfp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 585,
      "cache_read_input_tokens": 76065,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 585
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 183,
          "cache_read_input_tokens": 76065,
          "cache_creation_input_tokens": 585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 585,
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

_source line 46 · 2026-05-22T08:34:52.769Z_

<details><summary>↩ Tool result · `toolu_01WmN9uD5Xm8DR4RLrE5DWdm`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:47:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b965ed61-d0d5-4065-924c-89f7b8b97ca1",
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "fb3a6b8f-4e12-4349-887d-1428d9dcf4ce",
  "sourceToolAssistantUUID": "b965ed61-d0d5-4065-924c-89f7b8b97ca1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-22T08:34:53.870Z_

Let me get the full line from experiments.tex:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb3a6b8f-4e12-4349-887d-1428d9dcf4ce",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJNWDHHQkiZcZ77q4fQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f7f74ecc-3eb4-4780-b403-55b3dbd2db8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016mgXo2FLfp8pzQBvGhHk5n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 76650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 244,
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

_source line 48 · 2026-05-22T08:34:54.435Z_

<details open><summary>🔧 Tool call — Read · `toolu_01My1CBJZhczBVBbuyKB6Cht`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex",
  "offset": 45,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7f74ecc-3eb4-4780-b403-55b3dbd2db8d",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJNWDHHQkiZcZ77q4fQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "056733f3-6bb3-4309-9a1e-8e4969cdf055",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016mgXo2FLfp8pzQBvGhHk5n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 76650,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 244
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 138,
          "cache_read_input_tokens": 76650,
          "cache_creation_input_tokens": 244,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 244,
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

_source line 49 · 2026-05-22T08:34:54.444Z_

<details><summary>↩ Tool result · `toolu_01My1CBJZhczBVBbuyKB6Cht`</summary>

```text
45	Do architectures converge by improving on the same examples? We compare each architecture's pure-recurrent baseline against its h3-1 hybrid on 5{,}153 LAMBADA examples, classifying each as helped (correct only in hybrid), hurt (correct only in pure), or unchanged. Although the decomposition is binary, we verify below that it captures genuine separation in the continuous confidence space (Cohen's $d = 0.73$--$0.92$ between helped and hurt on LAMBADA; cross-benchmark details in Appendix~\ref{app:cm_cross}). This binarization discards confidence magnitude (a transition from 0.51 to 0.49 is treated identically to one from 0.99 to 0.01), so we supplement it with continuous confidence margin analysis (Appendix~\ref{app:confidence_margin}).
46	
47	Each architecture displays a distinct profile of per-example changes (Table~\ref{tab:per_example}). GDN loses a net 153 examples (462 helped, 615 hurt), RetNet loses 69 (426/495), and HGRN2 gains 153 (548/395). HGRN2 is the only architecture for which adding attention yields a net per-example benefit. Pairwise Jaccard similarity is low: mean $\bar{J} \leq 0.104$ for helped, $\leq 0.096$ for hurt, indicating ${\sim}90$\% non-overlap. Overlap significantly exceeds the independence baseline ($J_{\text{null}} \approx 0.05$, all $z > 5.9$, $p < .0001$; Appendix~\ref{app:jaccard_permutation}), but normalizing by the theoretical upper bound $J_{\max} = \min(|A|,|B|)/\max(|A|,|B|)$, observed overlap reaches only 6--7\% of the achievable range above chance (normalized ES 0.065 helped, 0.062 hurt; per-pair details in Appendix~\ref{app:normalized_es}), confirming that low Jaccard cannot be attributed to set-size constraints.
48	
49	\paragraph{Confidence margin mechanism.} No surface-level feature (token count, word frequency, syntactic complexity) reliably separates helped from hurt examples. However, pure-model confidence on the target token is strongly predictive within each architecture: hurt examples have lower target-token probability among pure-correct examples ($d = 0.83$--$0.92$), and helped examples have higher probability among pure-wrong examples ($d = 0.73$--$0.77$); see Appendix~\ref{app:confidence_margin}. A Kruskal-Wallis test confirms cross-architecture structure in both hurt ($p = .0005$) and helped ($p = .020$) distributions. The confidence margin thus identifies a per-example predictor of which examples will be affected: marginally correct predictions are more likely to transition to incorrect, and near-miss errors are more likely to transition to correct, but with architecture-specific thresholds that produce the observed cross-architecture divergence. Formalizing this as a prediction task (Appendix~\ref{app:prediction_framework}), pure-model confidence achieves AUC 0.70--0.74 within each architecture; rescue thresholds are architecture-invariant (relative spread 1\%), while disruption thresholds vary 47\%. Since each backbone assigns different confidences to the same input, even a shared rescue rule affects different examples per architecture, providing a parsimonious explanation for low cross-architecture Jaccard. The rescue pattern generalizes across LAMBADA, HellaSwag, and ARC-Easy (9/9 tests, $d = 0.13$--$0.60$; Appendix~\ref{app:cm_cross}). The disruption pattern is weaker on ARC-Easy ($d = 0.13$--$0.26$) and absent on HellaSwag under \texttt{acc\_norm} and on binary classification (Appendix~\ref{app:boolq}). This structured per-example disagreement constitutes predictive multiplicity \citep{marx2020predictive} arising under architectural variation \citep[cf.][]{damour2022underspecification}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "056733f3-6bb3-4309-9a1e-8e4969cdf055",
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "be01a080-9818-42f0-bc61-f27e7158fb0e",
  "sourceToolAssistantUUID": "056733f3-6bb3-4309-9a1e-8e4969cdf055",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-22T08:34:55.731Z_

Perfect! I found the key inconsistency. Now let me check a few more things to complete the analysis:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be01a080-9818-42f0-bc61-f27e7158fb0e",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJNdJv9mNFEhXbKRcCc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f7bb0f80-ed28-433b-90b0-3b8fe6de4c89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GLUFkWtZv4dw6rVmERhvWk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1165,
      "cache_read_input_tokens": 76894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1165,
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

_source line 51 · 2026-05-22T08:34:56.712Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GgCxbxpUt3RDs9nvRcHMqU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex",
  "offset": 72,
  "limit": 6
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7bb0f80-ed28-433b-90b0-3b8fe6de4c89",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJNdJv9mNFEhXbKRcCc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ffc25ec4-aa4f-4ef0-96b1-a5b180bc24f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GLUFkWtZv4dw6rVmERhvWk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1165,
      "cache_read_input_tokens": 76894,
      "output_tokens": 150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1165
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 150,
          "cache_read_input_tokens": 76894,
          "cache_creation_input_tokens": 1165,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1165,
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

_source line 52 · 2026-05-22T08:34:56.719Z_

<details><summary>↩ Tool result · `toolu_01GgCxbxpUt3RDs9nvRcHMqU`</summary>

```text
72	\subsection{Decoupling}\label{ssec:decoupling}
73	
74	A key consequence of this multiplicity is that aggregate convergence and per-example divergence operate on different timescales as attention ratio increases (Figure~\ref{fig:decoupling}).
75	
76	Cross-architecture $\sigma$ decreases gradually across the five attention ratios: $0.024 \to 0.016 \to 0.014 \to 0.006 \to 0.005$. In contrast, pairwise Jaccard similarity between architectures' per-example effects saturates at the first attention level (4\%): approximately 0.095 for helped, with no further increase at higher ratios. Net asymmetry between architectures' per-example profiles increases from 0.013 at 4\% attention to 0.040 at 25\%. If convergence arose from attention uniformly rescuing the same difficult examples across architectures, Jaccard would increase in parallel with decreasing $\sigma$. The observed saturation of Jaccard at the first attention level indicates that each architecture's per-example response to attention is largely idiosyncratic. The observed $\bar{J} \approx 0.10$ is far below the theoretical maximum $J_{\max} \approx 0.78$--$0.92$ given helped-set sizes, ruling out ceiling constraints: there is ample room for Jaccard to increase if attention were homogenizing per-example behavior (normalized effect size 6--7\% of achievable range; \S\ref{ssec:per_example}).
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffc25ec4-aa4f-4ef0-96b1-a5b180bc24f3",
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "ebf326d1-8c38-460b-ac41-b48abbc0dda4",
  "sourceToolAssistantUUID": "ffc25ec4-aa4f-4ef0-96b1-a5b180bc24f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-22T08:34:58.125Z_

Perfect! Now let me verify the rest of the main text claims and check the abstract and conclusion:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebf326d1-8c38-460b-ac41-b48abbc0dda4",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJNo2p6BKR7YGJLvaLT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "28cca49a-b263-4907-9cb0-c7ef50b996f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015dcWirgVVVSuHsh5rxyViB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 640,
      "cache_read_input_tokens": 78059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 640,
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

_source line 54 · 2026-05-22T08:34:58.482Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SbUu4uSycw8M4GxfHhqQDM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex",
  "offset": 24,
  "limit": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28cca49a-b263-4907-9cb0-c7ef50b996f2",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJNo2p6BKR7YGJLvaLT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "97a78116-7baa-4a95-9b09-2e0689926258",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015dcWirgVVVSuHsh5rxyViB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 640,
      "cache_read_input_tokens": 78059,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 640
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 145,
          "cache_read_input_tokens": 78059,
          "cache_creation_input_tokens": 640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 640,
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

_source line 55 · 2026-05-22T08:34:58.488Z_

<details><summary>↩ Tool result · `toolu_01SbUu4uSycw8M4GxfHhqQDM`</summary>

```text
24	\begin{abstract}
25	When attention layers are added to linear recurrent architectures, they help and hurt almost entirely different examples across backbones: pairwise overlap among three controlled hybrid designs is at most 10\%, far below the 78--92\% theoretical maximum. Using the model zoo of \citet{wang2025hybrid} (three architectures, five attention ratios, two scales, single training runs per configuration), we decompose per-example effects on four benchmarks and find that this predictive multiplicity \citep{marx2020predictive} depends on task type ($\alpha = 0.14$ for reasoning, $0.30$ for retrieval) rather than attention dose. Aggregate convergence is task-specific: only LAMBADA provides exploratory evidence for monotonic variance reduction (Bonferroni-adjusted $p = .100$). On this benchmark, aggregate variance decreases gradually while per-example overlap saturates at the first attention level, a saturation pattern that generalizes to all four benchmarks regardless of aggregate convergence. A proof-of-concept majority vote across architectures fails to outperform the best individual model despite 15--45\% per-example disagreement, while oracle accuracy reveals 7--14\,pp of untapped complementarity, suggesting that architectures interchangeable by aggregate metrics may carry hidden consequences for per-example reliability.
26	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97a78116-7baa-4a95-9b09-2e0689926258",
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "629ecdc5-592a-4775-9f8c-23cdf29ea796",
  "sourceToolAssistantUUID": "97a78116-7baa-4a95-9b09-2e0689926258",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-22T08:34:59.619Z_

Excellent. Now let me verify the conclusion section for completeness:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "629ecdc5-592a-4775-9f8c-23cdf29ea796",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJNvaEzGBEAphfg4sbJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a7a656f0-33b2-4291-9492-d564d7f99c95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0186Gefieym2z6p13wmkhZkM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 467,
      "cache_read_input_tokens": 78699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 467,
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

_source line 57 · 2026-05-22T08:34:59.815Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AkWqVhq5UFFgEaJ7D4zgC8`</summary>

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
  "parentUuid": "a7a656f0-33b2-4291-9492-d564d7f99c95",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJNvaEzGBEAphfg4sbJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5f1780ff-dcf0-4e1e-a800-4429e24b6755",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0186Gefieym2z6p13wmkhZkM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 467,
      "cache_read_input_tokens": 78699,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 467
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 107,
          "cache_read_input_tokens": 78699,
          "cache_creation_input_tokens": 467,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 467,
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

_source line 58 · 2026-05-22T08:34:59.821Z_

<details><summary>↩ Tool result · `toolu_01AkWqVhq5UFFgEaJ7D4zgC8`</summary>

```text
1	\section{Conclusion}
2	
3	We present the first systematic per-example analysis of attention effects in hybrid recurrent models. Per-example multiplicity spans a task-dependent variation ($\alpha = 0.14$--$0.30$) across four benchmarks, with Jaccard uniformly low ($\leq 0.10$) regardless of aggregate convergence. On LAMBADA, aggregate variance decreases with attention while per-example overlap saturates, consistent with architecture-specific pathways rather than uniform rescue (dependent on GDN inclusion; does not replicate on other benchmarks). Aggregate benchmark equivalence thus masks per-example divergence: each backbone develops architecture-specific response patterns invisible to standard evaluation. Within each architecture, pure-model confidence partially predicts which examples will be affected (AUC 0.70--0.74), though disruption thresholds vary 47\% across architectures (\S\ref{ssec:per_example}).
4	
5	For practitioners, these results motivate per-example audits whenever hybrid designs achieve comparable aggregate scores: the ${\sim}90\%$ non-overlap means architectures interchangeable by aggregate metrics affect nearly disjoint examples. A majority vote across three architectures does not outperform the best individual model (LAMBADA: $-0.2$\,pp; ARC-Easy: $-1.1$\,pp) despite 15--45\% disagreement, because roughly half of disagreement examples have only one correct architecture (Appendix~\ref{app:complementarity}). Oracle accuracy reveals $+7$--$14$\,pp of untapped complementarity, but accessing it requires selection methods beyond naive ensembling.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f1780ff-dcf0-4e1e-a800-4429e24b6755",
  "isSidechain": true,
  "promptId": "1dc02f5e-1371-4ed3-bff4-a4290a531fd4",
  "agentId": "a569ab0c5adb84941",
  "type": "user",
  "uuid": "0634c9b3-a6cd-4eeb-9751-b3694b0ca432",
  "sourceToolAssistantUUID": "5f1780ff-dcf0-4e1e-a800-4429e24b6755",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-22T08:35:08.665Z_

Perfect! Now I have a clear picture. Let me compile my findings:

## Summary of Numerical Consistency Check

I conducted a thorough search for inconsistencies across the paper (main.tex, introduction.tex, experiments.tex, and conclusion.tex). Here are my findings:

### INCONSISTENCY FOUND - Critical Issue:

**Normalized Effect Size Percentage Discrepancy:**

The paper claims two different percentages for the normalized effect size that represents how much of the theoretical maximum Jaccard overlap has been achieved:

1. **In experiments.tex (Section 4.2, line 47):**
   - States: "normalized ES 0.065 helped, 0.062 hurt" which equals **6--7% of achievable range**

2. **In experiments.tex (Section 4.3, line 76 - Decoupling subsection):**
   - States: "normalized effect size 6--7% of achievable range"

3. **In author_response_r7.tex (Reviewer responses):**
   - One response states: "The normalized effect size is only 5--7% of the achievable range above chance"
   - Another response states: "normalized ES 0.065 helped, 0.047 hurt" which equals **5--7% of achievable range**

**The problem:** The appendix Table 29 (normalized_es) shows:
- Mean normalized ES for Helped: 0.065 (6.5%)
- Mean normalized ES for Hurt: 0.047 (4.7%)

This correctly averages to **~6--7% range, NOT 5--7% range**.

The author response claiming "normalized ES 0.065 helped, 0.047 hurt" (which would be 5--7%) contradicts the main text's stated values and the actual appendix table data.

### All Other Numbers Verified as Consistent:

All other numerical claims were found to be consistent across all sections:

✓ α values: 0.14 (reasoning/PIQA), 0.15 (HellaSwag), 0.21 (ARC-Easy), 0.30 (retrieval/LAMBADA)
✓ Jaccard: ≤ 0.10 (cross-architecture), ~0.33 (within-architecture), 3× gap
✓ Theoretical maximum: 0.78--0.92
✓ LAMBADA convergence: ρ = -1.0, p = .017, Bonferroni-adjusted p = .100, σ drops 79%, CI [-1.0, -0.7]
✓ σ trajectory: 0.024 → 0.016 → 0.014 → 0.006 → 0.005
✓ Majority vote: LAMBADA -0.2pp, ARC-Easy -1.1pp
✓ Oracle accuracy: +7--14pp
✓ Per-example disagreement: 15--45%
✓ AUC: 0.70--0.74, disruption threshold variation 47%
✓ Helped/hurt counts: GDN 462/615, RetNet 426/495, HGRN2 548/395

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0634c9b3-a6cd-4eeb-9751-b3694b0ca432",
  "isSidechain": true,
  "agentId": "a569ab0c5adb84941",
  "requestId": "req_011CbHJP2NjrsczXpS36mHpt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "57256103-6cc3-46e6-9810-3a2bac46f640",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_agent_b031d53b",
  "sessionId": "210fe59f-b0a0-4fbf-922e-f7f3dd4aa8dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "declarative-dreaming-parrot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RnsphRmdbWm7gXjvk5eWQ2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 79166,
      "output_tokens": 759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 506
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 759,
          "cache_read_input_tokens": 79166,
          "cache_creation_input_tokens": 506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 506,
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
