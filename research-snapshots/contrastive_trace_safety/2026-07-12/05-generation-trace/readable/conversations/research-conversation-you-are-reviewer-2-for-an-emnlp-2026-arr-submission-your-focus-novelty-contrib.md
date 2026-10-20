# Research conversation: You are Reviewer 2 for an EMNLP 2026 ARR submission. Your focus: **Novelty/Contribution** and **Related Work positioning

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a846c1c041db9ae79.jsonl`
- **Structured JSON:** [`238ef8edbc9316d90996.json`](../../sessions/23/238ef8edbc9316d90996.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

53 recorded events

### User

_source line 1 · 2026-05-22T09:50:14.403Z_

You are Reviewer 2 for an EMNLP 2026 ARR submission. Your focus: **Novelty/Contribution** and **Related Work positioning**.

## Venue calibration
ARR Overall Assessment scale: 5=Award (top 2.5%), 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit. EMNLP Main acceptance ~21%.

## Paper summary

**Title**: "Layer Selection Matters: How Metric Choice Determines Hidden-State Probe Effectiveness for Reasoning Model Safety Monitoring"

The paper studies safety commitment detection in reasoning LLMs that can "self-jailbreak" during extended CoT. It makes a methodological contribution: the commonly used `bal_acc × crossing_rate` composite metric for layer selection systematically biases toward shallow layers (0-16% depth) where representations are compressed, producing inflated crossing rates. Threshold-dependent metrics (precision, FPR) consistently select deep layers (45-98% depth). At correctly selected deep layers, hidden-state probes significantly outperform text probes across all 4 models (12/12 Holm-Bonferroni, precision +15-24pp). This replicates on AdvBench with different labeling. Six alternative detection methods all fail.

**Related Work section** (Section 2, ~half a column):
- Hidden-state safety probes: TrajGuard (Li et al., 2024) — Mahalanobis distance on hidden states for adversarial input detection. SafeSwitch (Chen et al., 2025), SIREN (Wang et al., 2025b) — runtime intervention. Notes these target adversarial *input* attacks, not reasoning-model self-jailbreak.
- Reasoning model safety: Self-Jailbreaking (Ren et al., 2025), HarmThoughts (Wang et al., 2025c). SafeRemind (Wang et al., 2025a) and SafeThink (Qi et al., 2025) — text-level CoT monitoring. Claims first modality comparison (HS vs text) for reasoning-model safety.
- Representation probing: Belinkov (2022), Burns et al. (CCS, 2023), RepE (Zou et al., 2023a). Evaluates CCS and RepE as baselines.

**Total references**: 14 citations in the bibliography.

**Claims of novelty**:
1. "First systematic evaluation of detection methods for this phenomenon across 4 models spanning 2 architectures, 2 training methods, and 2 scales" (Abstract)
2. "Primary methodological contribution is identifying that the layer selection metric bal_acc × crossing_rate systematically biases toward shallow layers" (Abstract)
3. "Our work provides the first modality comparison (hidden-state vs. text) for reasoning-model safety detection" (Related Work)
4. Cross-dataset validation on AdvBench
5. Comprehensive negative results (6 alternative methods)

**Paper structure**: 7 pages main + appendix. Abstract, Intro (1 page), Related Work (half column), Method (1 page), Experiments (2.5 pages), Discussion (half page), Conclusion (quarter page), Limitations (quarter page), References, 3 appendix sections.

## Your review task

Provide a detailed review covering:

1. **Novelty assessment**: 
   - Is the layer selection bias finding genuinely novel and significant? Or is it a known issue in probing literature?
   - Is this paper more of an empirical study or a methodological contribution? Does it meet the bar for EMNLP?
   - How significant is the "first modality comparison" claim?

2. **Related Work gaps**:
   - Are there major missing references? Consider: probing methodology literature (e.g., Hewitt & Manning 2019, Pimentel et al. 2020 on probing selectivity/control tasks), safety monitoring beyond LLM (e.g., anomaly detection in AI safety), mechanistic interpretability (e.g., representation engineering more broadly), other hidden-state analysis work.
   - Only 14 references is extremely sparse for a venue like EMNLP. Is the related work adequate?
   - Does the paper properly distinguish itself from HarmThoughts (Wang et al., 2025c) which appears to use the same dataset?

3. **Framing critique**:
   - The paper frames itself as "first systematic comparison" — is this justified?
   - The layer selection bias is presented as the "primary contribution" — but is this really a contribution to the field, or a debugging of a specific metric?
   - The negative results are extensive (6 methods) but how meaningful are they individually?

4. **Excitement level**: Would this paper generate discussion at EMNLP? Does it open new research directions?

5. **Specific strengths**: 3-5
6. **Specific weaknesses**: 3-5
7. **Questions for authors**: 2-3

8. **Scores**: Soundness (1-5), Excitement (1-5), Reproducibility (1-5), Overall (1-5 in 0.5 increments).

Be rigorous. Calibrate: 21% acceptance for Main, ~40% for Findings. An empirical study needs to be exceptionally thorough or reveal surprising insights to reach Conference level at EMNLP.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ef604098-550a-4d3f-9fa7-47752021e2dc",
  "agentId": "a846c1c041db9ae79",
  "type": "user",
  "uuid": "58bafbd5-5fb5-49c1-bf91-03b18db7ac9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-22T09:50:14.409Z_

```json
{
  "parentUuid": "58bafbd5-5fb5-49c1-bf91-03b18db7ac9d",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
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
      "TodoWrite",
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
      "TodoWrite",
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
  "uuid": "3c33b133-275e-4753-adb1-4dae54f28484",
  "timestamp": "2026-05-22T09:50:14.409Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-22T09:50:18.269Z_



I'll start by reading the paper and related materials thoroughly before writing the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c33b133-275e-4753-adb1-4dae54f28484",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQ7pA4c2xRTkcStEWwH",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "c03711d8-4854-4c6f-b73c-32bab897bca5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDbwoUbDBAiNZHHs8LWsdf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7915,
      "cache_read_input_tokens": 9355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7915,
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

_source line 4 · 2026-05-22T09:50:18.894Z_

<details open><summary>🔧 Tool call — Glob · `toolu_016HKVi4fMy7pjHiW5pNYyBW`</summary>

```json
{
  "pattern": "docs/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c03711d8-4854-4c6f-b73c-32bab897bca5",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQ7pA4c2xRTkcStEWwH",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "d59ea61e-8eae-4a21-a7a0-9b5cb249642e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDbwoUbDBAiNZHHs8LWsdf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7915,
      "cache_read_input_tokens": 9355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7915,
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

_source line 5 · 2026-05-22T09:50:18.931Z_

<details><summary>↩ Tool result · `toolu_016HKVi4fMy7pjHiW5pNYyBW`</summary>

```text
docs/paper/_drafts/advbench_contingency_templates.tex
docs/paper/main.tex
docs/paper/sections/limitations.tex
docs/paper/sections/appendix.tex
docs/paper/sections/introduction.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/abstract.tex
docs/paper/sections/related_work.tex
docs/paper/sections/discussion.tex
docs/paper/sections/method.tex
docs/paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d59ea61e-8eae-4a21-a7a0-9b5cb249642e",
  "isSidechain": true,
  "promptId": "ef604098-550a-4d3f-9fa7-47752021e2dc",
  "agentId": "a846c1c041db9ae79",
  "type": "user",
  "uuid": "0fa91305-ea72-4a9c-b937-9d16d6a0cdaf",
  "sourceToolAssistantUUID": "d59ea61e-8eae-4a21-a7a0-9b5cb249642e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-22T09:50:19.487Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01GSTk2cKBvkaUhEfSPtRguu`</summary>

```json
{
  "pattern": "docs/paper/**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fa91305-ea72-4a9c-b937-9d16d6a0cdaf",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQ7pA4c2xRTkcStEWwH",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "e7c44e47-7100-448a-a95a-c276ada39483",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDbwoUbDBAiNZHHs8LWsdf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7915,
      "cache_read_input_tokens": 9355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7915,
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

_source line 7 · 2026-05-22T09:50:19.522Z_

<details><summary>↩ Tool result · `toolu_01GSTk2cKBvkaUhEfSPtRguu`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7c44e47-7100-448a-a95a-c276ada39483",
  "isSidechain": true,
  "promptId": "ef604098-550a-4d3f-9fa7-47752021e2dc",
  "agentId": "a846c1c041db9ae79",
  "type": "user",
  "uuid": "6ffa0dd8-15b4-4f5d-8514-76a9006aac55",
  "sourceToolAssistantUUID": "e7c44e47-7100-448a-a95a-c276ada39483",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-22T09:50:22.561Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EepQaEhSqiq6Hf65iVQwJb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ffa0dd8-15b4-4f5d-8514-76a9006aac55",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQ8CeuDCDNMvCXrJarm",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "339ee234-5ce6-4e8f-953b-37cd61eaecbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016pTvHkA5SdBY6XqWHXw95y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1232,
      "cache_read_input_tokens": 17270,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1232,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 9 · 2026-05-22T09:50:22.567Z_

<details><summary>↩ Tool result · `toolu_01EepQaEhSqiq6Hf65iVQwJb`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	\usepackage{xcolor}
15	\usepackage{colortbl}
16	\usepackage{hyperref}
17	\usepackage[capitalise]{cleveref}
18	
19	\title{Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models}
20	
21	\author{Anonymous ARR Submission}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	\input{sections/abstract}
28	\end{abstract}
29	
30	\input{sections/introduction}
31	
32	\input{sections/related_work}
33	
34	\input{sections/method}
35	
36	\input{sections/experiments}
37	
38	\input{sections/discussion}
39	
40	\input{sections/conclusion}
41	
42	\input{sections/limitations}
43	
44	\bibliography{references}
45	
46	\input{sections/appendix}
47	
48	\end{document}
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "339ee234-5ce6-4e8f-953b-37cd61eaecbe",
  "isSidechain": true,
  "promptId": "ef604098-550a-4d3f-9fa7-47752021e2dc",
  "agentId": "a846c1c041db9ae79",
  "type": "user",
  "uuid": "cc86d2f3-3887-423d-ab86-29e302953ae0",
  "sourceToolAssistantUUID": "339ee234-5ce6-4e8f-953b-37cd61eaecbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-22T09:50:23.030Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A2qr2RNgq3R2wHgQZhYE91`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc86d2f3-3887-423d-ab86-29e302953ae0",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQ8CeuDCDNMvCXrJarm",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "d04c1af4-8234-414a-a153-659f82e7885e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016pTvHkA5SdBY6XqWHXw95y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1232,
      "cache_read_input_tokens": 17270,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1232,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 11 · 2026-05-22T09:50:23.036Z_

<details><summary>↩ Tool result · `toolu_01A2qr2RNgq3R2wHgQZhYE91`</summary>

```text
1	Reasoning models with chain-of-thought (CoT) can self-jailbreak: their reasoning traces transition from safe deliberation to committed harmful generation without adversarial input. We define the commitment point (CP) as the first reasoning step after which safety deliberation permanently ceases, and present a systematic empirical comparison of hidden-state (HS) vs.\ text probes for CP detection across four reasoning LLMs (3 Qwen-family, 1 Llama) on HarmThoughts. The comparison depends critically on which transformer layer is monitored, a known sensitivity in probing methodology that we show is severe enough to qualitatively reverse conclusions in the safety domain: a crossing-rate composite metric selects L0 for R1-8B while threshold-based metrics select L14 (14-layer divergence); at 32B the divergence reaches 61 layers (exploratory$^\dagger$), reversing whether an HS advantage is observed. Threshold-based layer selection recovers HS precision gains of +15 to +22pp at 7--8B (cross-validated via nested CV) and preliminary +15 to +19pp at 32B (exploratory$^\dagger$, $n \leq 20$) against a 384d sentence encoder, but this advantage is conditional on partially correlated factors: it diminishes with stronger text encoders (4/4 HB at 384d $\to$ 1/4 at 1024d) and partially overlaps with temporal position. Seven alternative methods (change-point detection, geometric distance, representation engineering, cross-model transfer) all fail to match supervised probing. Metric-induced layer selection bias is the robust methodological finding; the empirical HS advantage is conditional on encoder quality and position control (partially correlated).
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d04c1af4-8234-414a-a153-659f82e7885e",
  "isSidechain": true,
  "promptId": "ef604098-550a-4d3f-9fa7-47752021e2dc",
  "agentId": "a846c1c041db9ae79",
  "type": "user",
  "uuid": "400dd95f-099b-472a-8ee7-d7b37a2330a0",
  "sourceToolAssistantUUID": "d04c1af4-8234-414a-a153-659f82e7885e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-22T09:50:23.493Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AXUFQ9vqzgWfhmJ2cwT5C1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "400dd95f-099b-472a-8ee7-d7b37a2330a0",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQ8CeuDCDNMvCXrJarm",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "673c7a42-e262-4842-9075-d75dcabcb5da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016pTvHkA5SdBY6XqWHXw95y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1232,
      "cache_read_input_tokens": 17270,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1232
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 237,
          "cache_read_input_tokens": 17270,
          "cache_creation_input_tokens": 1232,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1232,
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

_source line 13 · 2026-05-22T09:50:23.497Z_

<details><summary>↩ Tool result · `toolu_01AXUFQ9vqzgWfhmJ2cwT5C1`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Reasoning models such as DeepSeek-R1~\cite{deepseekr1} and QwQ~\cite{qwq} scale inference-time computation through extended chains of thought (CoT). Recent work documents that these models can ``self-jailbreak'': without adversarial input modification, the CoT transitions from safety-aware deliberation to committed harmful generation~\cite{harmthoughts,selfjailbreak}. We define the first reasoning step after which safety deliberation permanently ceases as the \textbf{Safety Commitment Point} (CP). This failure mode differs qualitatively from adversarial jailbreaks on standard LLMs because the harmful transition originates within the model's own reasoning. Recent work shows that chain-of-thought faithfulness is limited~\citep{chen2025unfaithful}, motivating hidden-state monitoring that bypasses surface text. Before retrospective characterization can inform future detection systems, a prior question must be answered: can current probing methods reliably distinguish pre-CP from post-CP reasoning steps, and under what conditions? This paper provides \emph{retrospective} classification (not online detection) of what hidden-state and text-based probes can and cannot detect; false positive rates remain 11--50\%, so deployment applications are future work.\looseness=-1
4	
5	Existing safety detectors target fundamentally different problems. Hidden-state (HS) methods such as TrajGuard~\cite{trajguard} and SafeSwitch~\cite{safeswitch} classify adversarial inputs at the token level, while text monitors like SafeRemind~\cite{saferemind} scan generated reasoning for explicit violations. Neither tracks the gradual, multi-step commitment process. HS probes require choosing which transformer layer to monitor, a researcher degree of freedom typically treated as a minor implementation detail. Before asking which modality is better, a prior methodological question must be answered: how sensitive are probe conclusions to the choice of layer selection metric? We show this choice alone can reverse a study's central conclusion: the same data yield a 14-layer (R1-8B) to 61-layer (QwQ-32B) divergence depending solely on metric choice; for QwQ-32B, at threshold-based layers the HS advantage is +19pp ($p{<}0.005$); at crossing-rate-selected layers, it is non-significant ($p{=}0.83$). More broadly, no prior work tracks how safety signals evolve step-by-step during extended reasoning; existing hidden-state analyses operate across layers (spatial) rather than across generation steps (temporal).\looseness=-1
6	
7	We conduct a systematic analysis across four reasoning models, primarily Qwen-based (3/4 models), with one Llama model providing evidence from a second architecture family, at two scales (7--8B, 32B) on the HarmThoughts benchmark. Our central finding is methodological: the choice of layer selection metric entirely determines whether an HS advantage is observed. A composite metric (balanced accuracy $\times$ crossing rate) selects shallow layers for 32B models because shallow representations compress directional information, so a linear probe operates near the noise floor and threshold crossings reflect noise rather than semantic transitions. At these layers, only the two 7--8B models show significant HS advantage.\looseness=-1
8	
9	\begin{table}[t]
10	\centering
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{lccccc}
13	\toprule
14	\textbf{Model} & \textbf{Arch.} & \textbf{Params} & \textbf{Layers} & \textbf{Hidden} & \textbf{$n$ (total\,/\,test)} \\
15	\midrule
16	R1-8B & Llama & 8B & 32 & 4096 & 209\,/\,43 \\
17	OT-7B & Qwen & 7B & 28 & 3584 & 228\,/\,47 \\
18	R1-32B & Qwen & 32B & 64 & 5120 & 100\,/\,20 \\
19	QwQ-32B & Qwen & 32B & 64 & 5120 & 95\,/\,19 \\
20	\bottomrule
21	\end{tabular}}
22	\caption{Models studied. R1-8B and R1-32B are distilled from DeepSeek-R1~\citep{deepseekr1}; QwQ-32B~\citep{qwq} is a native reasoning model; OT-7B~\citep{openthinker} is trained with STILL~\citep{still} on Qwen2.5-7B. Data: HarmThoughts~\citep{harmthoughts} with step-level CP annotations (CP = first reasoning step after which safety deliberation permanently ceases). Split: 60/20/20.}
23	\label{tab:models}
24	\end{table}
25	
26	Threshold-based metrics (precision, inverse FPR, additive composite) share a common confusion matrix and empirically converge; BA independently confirms deep-layer selection (\cref{tab:layer_selection}). At these layers, the HS advantage is graded: \emph{validated via nested 5-fold CV} at 7--8B (precision +20.1 to +21.9pp; \cref{tab:hs_vs_text}), \emph{significant} but suggestive of position-competitiveness at QwQ-32B$^\dagger$ (+19.2pp; \cref{sec:32b-analysis}), and \emph{exploratory} at R1-32B$^\dagger$ (+15.4pp, pattern consistent with position mediation, below MDE; \cref{sec:experiments}).\looseness=-1
27	
28	Our contributions are:
29	\begin{itemize}
30	    \item \textbf{Metric-induced layer selection bias.} Prior work has noted metric sensitivity in probing~\citep{belinkov2022probing}; our contribution is demonstrating a qualitative reversal (significant to non-significant) in a safety-critical application, where the stakes of metric choice are higher than in typical linguistic probing. Crossing-rate composite metrics systematically select shallow layers across all four models (including Llama), reversing HS probe conclusions at 32B scale. The divergence is not gradual: for QwQ-32B, the CR-composite layer (L2, 3\% depth) yields $p{=}0.83$ (non-significant), while the threshold-based layer (L63, 98\% depth) yields $p{<}0.005$, a qualitative reversal, not a quantitative shift. Random-label controls on both architectures confirm the disagreement requires genuine safety labels; the geometric component is Qwen-specific (\cref{sec:layer-results}).
31	
32	    \item \textbf{Boundary conditions for the HS advantage.} Against 384d MiniLM, the HS advantage is validated via nested 5-fold CV at 7--8B (+20.1 to +21.9pp, HB corrected), significant at QwQ-32B$^\dagger$ (+19.2pp, position-competitive), and exploratory at R1-32B$^\dagger$ (+15.4pp). This advantage is conditional on two partially correlated factors: it diminishes with stronger encoders (1/4 HB under BGE-1024d; PCA capacity matching preserves significance across all four models) and partially overlaps with position (3/4 linear, 2/4 quadratic residualization; \cref{sec:32b-analysis}).
33	
34	    \item \textbf{Negative results define method boundaries.} No alternative method consistently matches supervised probing (\cref{tab:negative}): BOCPD/CUSUM fail on gradual transitions; Mahalanobis distance finds near-zero separation; RepE is model-dependent; cross-model transfer fails. Control task selectivity (11.1--16.8pp above chance; \cref{app:control}) confirms genuine safety structure.
35	\end{itemize}
36	
37	\noindent These findings establish that layer selection metric is an uncontrolled confound in hidden-state safety probing: any study reporting conclusions from a single metric family risks undetected qualitative reversal.\looseness=-1
38	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "673c7a42-e262-4842-9075-d75dcabcb5da",
  "isSidechain": true,
  "promptId": "ef604098-550a-4d3f-9fa7-47752021e2dc",
  "agentId": "a846c1c041db9ae79",
  "type": "user",
  "uuid": "6cfc1c0d-b132-4e28-90c8-2f65d5d1269a",
  "sourceToolAssistantUUID": "673c7a42-e262-4842-9075-d75dcabcb5da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-22T09:50:26.544Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B5GSoz55bVKF7SjnxvkxaX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cfc1c0d-b132-4e28-90c8-2f65d5d1269a",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQ8VFHyTW2p8tABrvv4",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "ad259c67-27d7-4da0-b13d-9d8c209acc2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mdt9VuhANHo9ZLNw61kZNj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3213,
      "cache_read_input_tokens": 18502,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3213,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
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

_source line 15 · 2026-05-22T09:50:26.550Z_

<details><summary>↩ Tool result · `toolu_01B5GSoz55bVKF7SjnxvkxaX`</summary>

```text
1	\section{Related Work}\label{sec:related-work}
2	
3	\paragraph{Safety in Reasoning Models.}
4	Reasoning models introduce a qualitatively new failure mode: the model's own chain of thought transitions from safe deliberation to harmful generation without adversarial input~\cite{wang2025lrmsafety}. Self-jailbreak has been documented with step-level annotations~\cite{harmthoughts,selfjailbreak}; H-CoT~\cite{hcot2025} shows reasoning chains can be externally hijacked; unfaithful reasoning~\cite{chen2025unfaithful,turpin2023language} motivates hidden-state monitoring. Safety-aligned models maintain refusal intentions during thinking but experience sharp drops at output generation~\cite{yin2025refusal_cliff,hagendorff2026lrm_jailbreak,hu2026refusal_dynamics,ahrend2026safer_traces}. CoT monitoring detects reward hacking but is fragile under optimization pressure~\cite{baker2025monitoring,korbak2025cot_monitorability}; GuardReasoner~\cite{xiang2025guardreasoner} trains a dedicated reasoning guard; \citet{schulz2025roadmap} formalizes safety-case deployment. Mitigation strategies include early reasoning steering~\cite{safethink}, entropy-triggered reminders~\cite{saferemind}, and guardrail insertion~\cite{mao2025selfjailbreak_reasoning}; none conducts a systematic modality comparison for commitment detection.
5	
6	\paragraph{Hidden-State Safety Detection.}
7	Internal activations encode safety-relevant information: truthfulness~\cite{azaria2023internal}, layer-distributed alignment signals~\cite{zhou2024alignment}, shallow alignment~\cite{qi2025shallow_alignment}, refusal directions~\cite{arditi2024refusal,joad2026refusal_multi}, activation steering~\cite{turner2023activation,li2023iti}, separate harmfulness/refusal encodings~\cite{zhao2025harmfulness,wollschlager2025geometry}, and scalable feature extraction~\cite{templeton2024scaling}. Probing studies confirm safety states are linearly accessible~\cite{zhao2026safeprobing,chia2025probing_subspaces,kadali2025internal}. Monitoring systems---TrajGuard~\cite{trajguard}, SafeSwitch~\cite{safeswitch}, SIREN~\cite{siren}, SafeDream~\cite{safedream2026}, HiddenDetect~\cite{jiang2025hiddendetect}, SafeInt~\cite{safeint2025}, RCS~\cite{rcs2026}, and hidden-state forensics~\cite{zhou2025ghost}---assume external input manipulation and operate at the token level; the self-jailbreak setting differs because transitions are internal and span multiple reasoning steps. Concurrently, \citet{chan2025probing} show final-layer linear probes predict alignment outcomes with strong F1, but their single-layer, single-metric evaluation does not examine whether different layers yield different conclusions---the central question of our work (\cref{sec:layer-results}). We reproduce TrajGuard (\cref{sec:negative}) and find its geometric approach fails on minor PCA components.\looseness=-1
8	
9	\paragraph{Probing Methodology and Layer Selection.}
10	Linear probing spans layer-wise classifiers~\cite{alain2017understanding}, sentence probing~\cite{conneau2018probing}, and surveys~\cite{belinkov2019analysis,belinkov2022probing,rogers2020primer}; causal abstraction~\cite{geiger2023causal} grounds use of internal representations. Control tasks~\cite{hewitt2019control} distinguish structure from memorization (adopted in \cref{app:control}); \citet{levinstein2024liedetector} raise concerns about spurious correlations that our controls address. Information-theoretic and causal formulations address probe complexity~\cite{voita2020information,pimentel2020information,ravfogel2020null,ravfogel2022rlace,belrose2023leace,elazar2021amnesic}.\footnote{The Tuned Lens~\cite{belrose2023tunedlens} assumes next-token prediction, misaligned with binary CP classification.} Non-uniform layer-wise information distribution~\cite{tenney2019bert,jawahar2019bert,marks2024geometry} and cross-layer disagreement~\cite{kaya2019shallow,zhou2020bert} are well established; we repurpose these for safety probe layer selection (\cref{sec:layer-sensitivity}). Our contribution is that the known layer-wise gradient interacts with metric choice to produce systematic selection bias. \citet{boxo2025linear_probes} show probes can rely on textual evidence; our analysis provides a complementary geometric mechanism at shallow layers. Concurrent works confirm layer sensitivity in related settings: influence estimation~\cite{vitel2025layer}, reasoning dynamics monitoring~\cite{chrabaszcz2026monitoring}, hallucination detection~\cite{alvarez2026transport_geometry}, truth encoding trajectories~\cite{damirchi2026truth}, selective probes~\cite{meyoyan2026bertology}, and multi-layer ensembling~\cite{pais2026linear_probe_scaling}.\looseness=-1
11	
12	\paragraph{Alternative Detection Approaches.}
13	BOCPD~\cite{adams2007bayesian} detects abrupt distributional shifts; CCS~\cite{burns2023discovering} discovers latent truth directions; RepE~\cite{zou2023representation} identifies concept directions. We adapt all three to temporal commitment detection (\cref{sec:negative}): BOCPD/CUSUM fail on gradual transitions, CCS misaligns temporally, and RepE is model-dependent (BA 0.756 vs.\ 0.559). These failures motivate supervised probes with principled layer selection.\looseness=-1
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad259c67-27d7-4da0-b13d-9d8c209acc2a",
  "isSidechain": true,
  "promptId": "ef604098-550a-4d3f-9fa7-47752021e2dc",
  "agentId": "a846c1c041db9ae79",
  "type": "user",
  "uuid": "0fa5f8db-354d-46a0-87ae-11226118cb24",
  "sourceToolAssistantUUID": "ad259c67-27d7-4da0-b13d-9d8c209acc2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-22T09:50:26.873Z_

<details open><summary>🔧 Tool call — Read · `toolu_01J7jGHBsQJRrsTsmkaZx2DZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fa5f8db-354d-46a0-87ae-11226118cb24",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQ8VFHyTW2p8tABrvv4",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "9c5f7376-65e2-4a4d-88fa-e03554c5ac9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mdt9VuhANHo9ZLNw61kZNj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3213,
      "cache_read_input_tokens": 18502,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3213,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
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

_source line 17 · 2026-05-22T09:50:26.883Z_

<details><summary>↩ Tool result · `toolu_01J7jGHBsQJRrsTsmkaZx2DZ`</summary>

```text
1	\section{Problem Setup and Methods}
2	\label{sec:method}
3	
4	\subsection{Safety Commitment Point}
5	\label{sec:commitment-point}
6	
7	When a reasoning model is jailbroken, its chain-of-thought (CoT) transitions from safety-aware deliberation to committed harmful generation. We define the \textbf{Safety Commitment Point} (CP) as the first reasoning step after which safety deliberation permanently ceases; traces with oscillating safety deliberation are resolved by taking the final irreversible transition. This binary formulation is a deliberate simplification; we discuss its limits in \cref{sec:limitations}. Steps before CP are \emph{pre-commitment} ($y_t = 0$); steps at or after CP are \emph{post-commitment} ($y_t = 1$). The classification task produces a score $s_t \in [0, 1]$ estimating whether the model has passed its CP by step $t$. Annotation quality is robust to boundary uncertainty: shifting CP labels by $\pm$1 step changes balanced accuracy by ${<}2.5$pp (\cref{tab:cp_perturbation}).
8	
9	We study four reasoning models spanning two architectures and two scales (\cref{tab:models}).
10	
11	\subsection{Probe Architecture}
12	\label{sec:probe-architecture}
13	
14	\paragraph{Hidden-state (HS) probes.} At each step $t$, we extract the last-token hidden state $\mathbf{h}_t^{(\ell)} \in \mathbb{R}^d$ from layer $\ell$ and train an L2-regularized logistic regression classifier (balanced class weights, $C{=}1.0$, LBFGS, max\_iter${}=2000$) on binary CP labels. Sweeping $C \in [0.01, 100]$ yields $<$2pp BA variation (\cref{sec:experiments}), confirming robustness to this default. Layer selection is analyzed in \cref{sec:layer-sensitivity}.
15	
16	\paragraph{Text probes.} Each step's text is encoded with all-MiniLM-L6-v2~\citep{wang2020minilm} ($\mathbb{R}^{384}$), a distilled sentence encoder from the Sentence-BERT family~\citep{reimers2019sentence}. The same logistic regression is applied as a surface-level modality baseline.
17	
18	\paragraph{Temporal windowing.} For window size $W$, we concatenate features from steps $[t{-}W{+}1, \ldots, t]$. We evaluate $W \in \{1, 3, 5, 10, 15, 20, 25\}$ and select per-model on validation. GRU sequence models are also evaluated under two protocols: a 70/30 train/test split (primary) and the same 60/20/20 split used for LR experiments (for fair comparison; \cref{tab:gru_multi_seeds,app:gru_details}).
19	
20	\subsection{Layer Selection Sensitivity}
21	\label{sec:layer-sensitivity}
22	
23	Layer selection is a researcher degree of freedom that can reverse modality comparison conclusions. We evaluate five metrics: balanced accuracy (BA), precision, and inverse FPR are standard probing metrics~\citep{belinkov2022probing}; crossing rate formalizes cross-layer prediction disagreement~\citep{kaya2019shallow,zhou2020bert}, and additive composite. A \emph{first crossing point} (FCP) exists for trace~$i$ at layer~$\ell$ when the probe score $s_{t'}^{(\ell)} > \tau$ for $K$ consecutive steps; the crossing rate is $\mathrm{CR}(\ell) = N^{-1}\!\sum_{i} \mathbb{1}[\mathrm{FCP}_i^{(\ell)} \text{ exists}]$. A multiplicative composite (BA $\times$ crossing rate) serves as the \emph{crossing-rate composite} (CR-composite) baseline, combining classification quality with transition sensitivity. Metrics at a fixed decision threshold (precision, inverse FPR, additive composite) form the \emph{threshold-based} selection. This taxonomy is empirical, but cosine compression at shallow layers predicts a priori that any threshold-crossing metric exhibits shallow-layer bias, confirmed by results (\cref{sec:layer-results}). Crossing rate inflates where representations are compressed (inter-step cosine distances 1.4--2.7$\times$ smaller; \cref{app:cosine_volatility}). Threshold-based metrics share a confusion matrix and empirically converge; BA independently confirms. Results in \cref{sec:layer-results}; full per-layer sweeps in \cref{app:layer_sweep}.\looseness=-1
24	
25	\subsection{Baseline Methods}
26	\label{sec:baselines}
27	
28	We evaluate seven alternatives to contextualize probe performance (\cref{tab:negative}): BOCPD~\citep{adams2007bayesian} and CUSUM~\citep{page1954cusum} for change-point detection; Mahalanobis distance following TrajGuard~\citep{trajguard}; RepE mean-difference directions~\citep{zou2023representation}; two-layer MLP probes; CCS-adapted~\citep{burns2023discovering}; and cross-model transfer via PCA. A position-only baseline ($t/T$) controls for temporal artifacts. Detailed configurations in \cref{app:bocpd_config,app:transfer_details}.
29	
30	\subsection{Evaluation Protocol}
31	\label{sec:evaluation}
32	
33	We report balanced accuracy, precision, pre-CP FPR, coverage, and lead time. We exclude F1 (conflates precision and recall), AUROC (threshold-free, cannot diagnose layer selection bias), and MCC (redundant with BA under balanced priors). Positive classification requires $K{=}5$ consecutive threshold crossings, selected on the R1-8B validation set and held fixed across all models as the value balancing coverage ($\geq$70\%) and safe-trace false positive rate ($\leq$50\%); \cref{tab:k_ablation} confirms that the HS vs.\ text conclusion direction is consistent at $K{=}3$, $5$, and $7$, with coverage and FPR trading off monotonically. Modality comparisons use BCa bootstrap (10{,}000 resamples, resampling traces as clusters: each trace is an independent unit and all its steps are included or excluded together, preserving within-trace dependence)~\citep{efron1993bootstrap,diciccio1996bootstrap} with Holm-Bonferroni step-down (3 metrics $\times$ 4 models $= 12$ tests, $\alpha{=}0.05$); the 4-test framework yields identical conclusions (\cref{app:holm_bonferroni}). For 32B models ($n \leq 20$), the exact permutation test is the primary inference method; BCa confidence intervals are reported for comparability but may have reduced coverage at these sample sizes (BCa assumes approximate pivotality; heavy-tailed score distributions could produce anti-conservative intervals). Within each model, the three metrics are positively correlated, so the correction is stricter than under independence. Control task selectivity~\citep{hewitt2019control} validates genuine structure (\cref{app:control}). $\dagger$ marks sample-limited test sets ($n \leq 20$): R1-32B ($n{=}20$) and QwQ-32B ($n{=}19$).
34	
35	\paragraph{Hyperparameter search space and multiple comparisons.} The full exploration spans ${\sim}$5 metrics $\times$ 7 windows $\times$ 28--64 layers $\approx$ 980--2{,}240 configurations per model. However, the effective number of independent tests is far smaller: the five metrics share one confusion matrix (threshold-based metrics are functionally correlated; \cref{app:effective_tests}), and adjacent layers produce near-identical probes. Effect sizes are large (Cohen's $d{=}0.58$--$2.37$; \cref{app:effective_tests}), arguing against fishing artifacts. A two-stage design protects against selection bias: upstream layer/window exploration uses nested CV and split-half validation at 7--8B (\cref{app:nested_cv,app:split_half}); downstream modality tests apply HB to 12 final comparisons. The 32B models lack nested CV (${\sim}$4 traces per fold) and are marked exploratory ($\dagger$). We classify evidence into three tiers (cross-validated, significant, and exploratory), detailed in \cref{sec:experiments}. All reported p-values are conditional on the selected layer and window, not marginal over the full search space.\looseness=-1
36	
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c5f7376-65e2-4a4d-88fa-e03554c5ac9f",
  "isSidechain": true,
  "promptId": "ef604098-550a-4d3f-9fa7-47752021e2dc",
  "agentId": "a846c1c041db9ae79",
  "type": "user",
  "uuid": "6565a138-416a-4a62-8430-36a36c58d497",
  "sourceToolAssistantUUID": "9c5f7376-65e2-4a4d-88fa-e03554c5ac9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-22T09:50:27.216Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DX8stdi9Hcjbputy9EkNjT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6565a138-416a-4a62-8430-36a36c58d497",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQ8VFHyTW2p8tABrvv4",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "83b62db3-f9d9-4ef2-ac2d-6b4f0bbb32d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mdt9VuhANHo9ZLNw61kZNj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3213,
      "cache_read_input_tokens": 18502,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3213
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 241,
          "cache_read_input_tokens": 18502,
          "cache_creation_input_tokens": 3213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3213,
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

_source line 19 · 2026-05-22T09:50:27.224Z_

<details><summary>↩ Tool result · `toolu_01DX8stdi9Hcjbputy9EkNjT`</summary>

```text
1	\section{Experiments}\label{sec:experiments}
2	
3	We evaluate temporal probes across four reasoning models (\cref{tab:models}), comparing hidden-state (HS) and text modalities under different layer selection criteria.
4	
5	\paragraph{Evidence gradient.} We classify HS advantage evidence into three tiers: \emph{cross-validated}\footnote{In our usage, \emph{cross-validated} means the result survives nested 5-fold cross-validation with a held-out test fold, ruling out hyperparameter overfitting. \emph{Exploratory} ($\dagger$) results pass HB on the holdout split but lack nested CV validation due to sample constraints.} (nested CV pass; 7--8B models), \emph{significant} (HB pass without nested CV; QwQ-32B), and \emph{exploratory} ($^\dagger$, small sample or narrow coverage; R1-32B). Per-model details follow in \cref{sec:layer-results,sec:hs-text,sec:32b-analysis}.
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We study R1-8B (Llama-8B, R1-distilled, $n{=}43$ test traces), OT-7B (OpenThinker-7B, trained on the OpenThoughts dataset~\citep{openthinker}; Qwen-7B backbone, STILL-trained~\cref{app:ot7b_details}, $n{=}47$), QwQ-32B (Qwen-32B, native reasoning, $n{=}19$--$20$), and R1-32B (Qwen-32B, R1-distilled, $n{=}20$). All traces come from HarmThoughts with step-level CP annotations (60/20/20 split). HS probes extract last-token hidden states from a selected layer; text probes encode each step with all-MiniLM-L6-v2 (384d). Both use L2-regularized logistic regression with temporal windowing $W \in \{1, 3, 5, 10, 15, 20, 25\}$ selected on validation. Classification requires $K{=}5$ consecutive threshold crossings (\cref{tab:k_ablation}). Statistical testing follows \cref{sec:evaluation}.\looseness=-1
10	
11	\subsection{Layer Selection Results}\label{sec:layer-results}
12	
13	\cref{tab:layer_selection} shows that the crossing-rate composite metric (balanced accuracy $\times$ crossing rate) systematically selects shallow layers across all four models: L0 for R1-8B (full L0--L24 sweep; \cref{tab:r18b_full_layer}) and OT-7B, L2 (3\%) for QwQ-32B, and L10 (16\%) for R1-32B (\cref{fig:layer_heatmap}). The three threshold-based metrics (precision, inverse FPR, additive composite) share a common confusion matrix and empirically converge to the same deep layer, L63 (98\%) for both 32B models, consistent with their shared structure, though not mathematically guaranteed. Pure balanced accuracy, a threshold-free metric, selects layers that vary across data splits and models (7--98\% depth under 60/20/20; \cref{app:ba_layer_comparison}), itself demonstrating that layer selection is a consequential methodological choice. The mechanism is that shallow layers produce highly compressed representations with small inter-step margins: step-to-step cosine distances are 1.4--2.7$\times$ smaller than at deep layers across all models (\cref{app:cosine_volatility}). A linear probe in this compressed space operates near the noise floor, generating frequent threshold crossings that inflate crossing rate independently of discriminative power (\cref{sec:layer-sensitivity}).\looseness=-1
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{lcccc}
20	\toprule
21	\textbf{Model} & \textbf{CR-comp.}$^a$ & \textbf{Thresh.}$^b$ & $p$ \textbf{(thresh.)} & $\Delta$\textbf{Prec}$^c$ \\
22	\midrule
23	R1-8B & L0 (0\%) & L14 (44\%) & ${<}0.001$ & +20.1 \\
24	OT-7B & L0 (0\%) & L16 (57\%) & ${<}0.001$ & +21.9 \\
25	QwQ-32B$^\dagger$ & L2 (3\%) & L63 (98\%) & ${<}0.005$ & +19.2 \\
26	R1-32B$^\dagger$ & L10 (16\%) & L63 (98\%) & ${<}0.001$ & +15.4 \\
27	\bottomrule
28	\end{tabular}}
29	\caption{Layer selection sensitivity. $^a$\,Crossing-rate composite (bal\_acc $\times$ crossing\_rate). $^b$\,Consensus of threshold-based metrics (precision, inverse FPR, additive composite). $^c$\,HS$-$text precision difference (pp) at threshold-based layer (\cref{tab:hs_vs_text}). Rightmost $p$: HS vs.\ text precision $p$-value at threshold-based layer (e.g., QwQ-32B CR-composite layer: $p{=}0.83$, non-significant). $\dagger$\,Sample-limited ($n \leq 20$).}
30	\label{tab:layer_selection}
31	\end{table}
32	
33	\begin{figure}[t]
34	\centering
35	\includegraphics[width=\columnwidth]{figures/fig_layer_heatmap.pdf}
36	\caption{Per-layer metric heatmap (2$\times$2). Each column: one of five metrics (min-max normalized). Red dashed: CR-composite layer (bal\_acc $\times$ crossing\_rate); green dashed: threshold-based layer (consensus of threshold-based metrics). For R1-8B (full L0--L24 sweep), crossing rate drives CR-composite selection to L0 while threshold-based metrics retain L14. At 32B, CR-composite selections cluster near input layers while threshold-based metrics peak at deep layers.}
37	\label{fig:layer_heatmap}
38	\end{figure}
39	
40	The downstream impact is severe: at CR-composite layers, only the two 7--8B models show significant HS advantage; both 32B models fail. The CR-composite's systematic shallow-layer selection is an artifact of cosine compression (\cref{app:cosine_volatility}), not a genuine safety signal; random-label controls confirm this distinction (\cref{app:random_cp}). At threshold-based layers, the HS advantage is graded: cross-validated at 7--8B (OT-7B, R1-8B; nested CV), significant but suggestive of position-competitiveness at QwQ-32B$^\dagger$, and exploratory at R1-32B$^\dagger$ (residualized gap below MDE). The $\dagger$ marks sample-limited test sets ($n \leq 20$) where effect sizes are descriptive rather than confirmatory. Random-label controls on QwQ-32B and R1-8B confirm that threshold-based deep-layer selection requires genuine safety labels; the geometric shallow-layer bias is Qwen-specific: retained on QwQ-32B but dissolved on R1-8B (\cref{app:random_cp}). AUROC, excluded from our primary metrics because it is threshold-free (\cref{sec:evaluation}), confirms HS discriminability at BA-selected layers ($\Delta$AUROC +12.1 to +15.1pp; \cref{tab:ba_layer_results}) but cannot diagnose the threshold-dependent layer selection bias.\looseness=-1
41	
42	\paragraph{Ensemble layer selection.} A three-layer ensemble that averages predicted probabilities from the precision-best, BA-best, and inverse-FPR-best layers bypasses single-metric pre-selection entirely. On the holdout split, all four models show significant HS advantage under the ensemble ($p \leq 0.002$, HB corrected; \cref{tab:ensemble}), including both 32B models that fail under CR-composite selection. The ensemble succeeds because averaging predictions from layers selected by different threshold-based metrics---which may favor somewhat different depths within the deep region---smooths metric-specific variation and reduces sensitivity to any single metric's layer preference. This holdout result uses the same split for both layer selection and evaluation; cross-validated confirmation is needed before the ensemble can be recommended as a general debiasing strategy (\cref{sec:discussion}).\looseness=-1
43	
44	\subsection{HS vs.\ Text Comparison}\label{sec:hs-text}
45	
46	\begin{table}[t]
47	\centering
48	\small
49	\resizebox{\columnwidth}{!}{%
50	\begin{tabular}{llclrrlrc}
51	\toprule
52	\textbf{Model} & \textbf{Layer} & \textbf{Enc.} & $W$ & $\Delta$\textbf{BA} & $\Delta$\textbf{Prec} & \textbf{95\% CI} & $\Delta$\textbf{FPR} & \textbf{HB} \\
53	\midrule
54	R1-8B & L14 & 384d & 3 & +17.5 & +20.1 & [+12.4, +28.3] & $-$7.9 & \checkmark \\
55	 & & 1024d & & \multicolumn{1}{c}{--} & +5.8 & [$-$7.4, +19.5] & \multicolumn{1}{c}{--} & \\[2pt]
56	OT-7B & L16 & 384d & 3 & +10.7 & +21.9 & [+14.4, +29.6] & $-$17.1 & \checkmark \\
57	 & & 1024d & & \multicolumn{1}{c}{--} & +18.1 & [+8.4, +29.0] & \multicolumn{1}{c}{--} & \checkmark \\[2pt]
58	QwQ$^\dagger$ & L63 & 384d & 5 & +13.0 & +19.2 & [+9.3, +33.5] & $-$15.0 & \checkmark \\
59	 & & 1024d & & \multicolumn{1}{c}{--} & +9.4 & [$-$7.1, +27.7] & \multicolumn{1}{c}{--} & \\[2pt]
60	R1-32B$^\dagger$ & L63 & 384d & 1 & +18.7 & +15.4 & [+8.7, +22.6] & $-$14.6 & \checkmark \\
61	 & & 1024d & & \multicolumn{1}{c}{--} & +11.7 & [$-$0.2, +24.3] & \multicolumn{1}{c}{--} & \\
62	\bottomrule
63	\end{tabular}}
64	\caption{HS vs.\ text at threshold-based layers (LR probes, 60/20/20 split, 10{,}000 bootstrap resamples). Enc.: text encoder (384d = MiniLM-L6-v2, 1024d = BGE-large). $\Delta$: HS$-$text difference (pp); ``--'' = BA and FPR are not computed for the 1024d comparison because the 384d and 1024d encoders operate at different probe calibration points and do not share a decision threshold. HB: \checkmark{} = model-level test passes Holm-Bonferroni ($\alpha{=}0.05$); all 384d model-level tests pass. $^\dagger$\,Sample-limited ($n \leq 20$); 32B results are exploratory. 1024d: HB over 4 model-level precision tests.}
65	\label{tab:hs_vs_text}
66	\end{table}
67	
68	The HS advantage is encoder-conditional: against BGE-large (1024d), only OT-7B survives HB correction (\cref{app:encoder_robustness}). Multi-seed stability appears in \cref{app:multi_seed}. Against the 384d baseline, HS probes outperform text probes in all four models$^\dagger$ (\cref{tab:hs_vs_text}): cross-validated at 7--8B (OT-7B: +21.9pp precision, R1-8B: +20.1pp), significant but suggestive of position-competitiveness at QwQ-32B$^\dagger$ (+19.2pp), and exploratory at R1-32B$^\dagger$ (+15.4pp, pattern consistent with position mediation). R1-8B FPR is directionally consistent (5/5 seeds) but not robust ($p{=}0.044$, rank 12/12 in HB step-down; 1/5 seeds Bonferroni; \cref{app:multi_seed}). R1-32B passes 5/5 seeds but shows a pattern consistent with position mediation (residualized gap NS; \cref{app:position_residual}); QwQ-32B's position baseline is competitive (\cref{sec:32b-analysis}). Overall, 18/20 model-seed combinations pass full HB (\cref{app:multi_seed}). Control task selectivity confirms genuine safety signal: 11.1--16.8pp above chance (\cref{app:control}). A split-half analysis on OT-7B confirms internal validity (\cref{app:split_half}).\looseness=-1
69	
70	\paragraph{Capacity control.} PCA reduction of HS features to 384d (79--92\% variance retained) preserves the precision advantage across all four models$^\dagger$ (+16.8 to +23.1pp, all $p{<}0.012$, all HB). The control provides partial evidence against a pure capacity explanation. Random projection to 384d yields similar results ($\Delta$Prec +8.3 to +20.5pp; \cref{app:random_projection}), further weakening the capacity explanation. E5-Mistral-7B (4096d, PCA-reduced to 384d; \cref{app:e5_mistral}) yields intermediate results (2/4 HB), forming a monotonic encoder-quality gradient with MiniLM (4/4) and BGE-large (1/4).\looseness=-1
71	
72	\paragraph{Encoder robustness.} Against BGE-large~\citep{xiao2023cpack} (1024d), only OT-7B survives HB (1/4 precision); R1-8B shows adverse FPR direction (+1.2pp). This forms a monotonic encoder-quality gradient: MiniLM-384d (4/4 HB) $\to$ E5-Mistral-4096d$\to$384d (2/4) $\to$ BGE-large-1024d (1/4), with the precision advantage narrowing from +15--22pp to +6--12pp. The HS advantage is thus a function of text encoder capacity (\cref{fig:forest_precision}); layer selection (Contribution 1) is encoder-independent.\looseness=-1
73	
74	\paragraph{Position mediation.} Position ($t/T$) accounts for 9--20pp of balanced accuracy,\footnote{R1-32B's 20.4pp drop reflects $W{=}1$; at $W{\geq}3$, drops are 9--17pp.} but all models retain non-positional signal above chance (all $p{<}0.001$; \cref{app:position_residual}). Three of four models retain significant non-positional HS advantage (residualized gap +3.7 to +6.9pp, HB corrected); R1-32B's gap is +1.9pp ($p{=}0.914$, $n{=}20$), well below the MDE of ${\sim}$9pp and thus indistinguishable from zero at current power. Adding a quadratic position term $(t/T)^2$ does not change significance conclusions for the 7--8B models. However, QwQ-32B's advantage is fully absorbed by the quadratic term (\cref{tab:position_quadratic}), indicating a non-linear position component. Temporal windowing reduces position dependence (\cref{sec:temporal}).\looseness=-1
75	
76	\enlargethispage{7\baselineskip}
77	\paragraph{Caveats.} Nested 5-fold CV confirms the HS precision advantage for both 7--8B models (10/10 folds; \cref{app:nested_cv}), with shrinkage of 13--25\% relative to holdout estimates. OT-7B nested CV selects L21--27 vs.\ holdout L16 vs.\ CR-composite L0; the +21.9pp holdout estimate is an upper bound. R1-32B achieves significance only at $W{=}1$ with 25\% coverage; at $W{\geq}3$, dimensionality prevents significance. QwQ-32B HS lead time is negative ($-$1.2 to +1.9 steps). False alarm rates remain 11--50\%, so current methods characterize the phenomenon rather than constitute production detectors. Per-model details in \cref{sec:32b-analysis}.\looseness=-1
78	
79	\subsection{32B Model-Specific Analysis}\label{sec:32b-analysis}
80	
81	\paragraph{Exploratory 32B analysis.} Both 32B results are exploratory ($n{=}19$--$20$ precludes nested CV). LOO-CV and multi-seed analyses (\cref{app:layer_sweep,app:multi_seed}) provide partial robustness checks but do not substitute for independent validation. R1-32B and QwQ-32B share the Qwen-32B architecture but present opposite detection profiles (\cref{tab:32b_divergence}); training method is one plausible differentiator. Replication with $n{\geq}50$ traces is needed.\looseness=-1
82	
83	\begin{table}[t]
84	\centering
85	\small
86	\resizebox{\columnwidth}{!}{%
87	\begin{tabular}{lcccc}
88	\toprule
89	\textbf{Model} & \textbf{Cov.} & \textbf{Lead (steps)} & \textbf{HB} & \textbf{Pos.\ margin} \\
90	\midrule
91	R1-32B$^\dagger$ & 25\% & +11.7 to +13.3 & \checkmark{} ($W{=}1$) & +14.2pp \\
92	QwQ-32B$^\dagger$ & 74\% & $-$1.2 to +1.9 & \checkmark{} (all $W$) & $-$3.6pp \\
93	\bottomrule
94	\end{tabular}}
95	\caption{32B cross-model divergence ($\dagger$\,sample-limited, $n \leq 20$; MDE at 80\% power: 8.6--9.5pp, \cref{app:power_analysis}; all conclusions exploratory). R1-32B provides limited early identification with narrow coverage; QwQ-32B provides robust significance with poor lead time. HB: \checkmark{} = passes Holm-Bonferroni ($\alpha{=}0.05$). Pos.\ margin: HS BA minus position baseline.}
96	\label{tab:32b_divergence}
97	\end{table}
98	
99	R1-32B suggests commitment 11--13 steps early (+14.2pp over position baseline) but covers only 25\% of traces ($W{=}1$); the precision effect (+15.4pp, CI width 13.9pp) falls below MDE at 80\% power. QwQ-32B achieves significance at all window sizes with 74\% coverage but negative HS lead time; the precision effect (+19.2pp, CI width 24.2pp) exceeds MDE (8.6--9.5pp; \cref{app:power_analysis}) but the position baseline achieves higher BA (0.832 vs.\ 0.796), and the HS precision margin over position (+4.5pp, $p{=}0.133$; \cref{app:position_residual}) is not significant at $n{=}19$. The divergence suggests per-model validation is needed.\looseness=-1
100	
101	\subsection{Temporal Context}\label{sec:temporal}
102	
103	Temporal windowing ($W{>}1$) improves both modalities (\cref{fig:window_ablation}): at 7--8B, the modality advantage (+20.1 to +21.9pp) exceeds temporal improvement (+13pp). GRU models achieve comparable accuracy but higher FPR (\cref{tab:gru_multi_seeds,app:temporal_details}); an adaptive two-stage strategy offers marginal gains (\cref{app:two_stage}).\looseness=-1
104	
105	CP-aligned probe score trajectories (\cref{fig:trajectory} in Appendix) confirm sharper HS transitions at the commitment point, with OT-7B showing the clearest separation and R1-32B the weakest. A forest plot visualizing precision gaps across encoder conditions appears in \cref{fig:forest_precision}.\looseness=-1
106	
107	\subsection{Negative Results}\label{sec:negative}
108	
109	No alternative method consistently matches supervised probing (\cref{tab:negative}). BOCPD~\citep{adams2007bayesian}/CUSUM fail (0\% detection on 3/4 models); Mahalanobis yields near-zero separation; RepE~\citep{zou2023representation} is model-dependent (BA 0.756 vs.\ 0.559); MLP probes overfit; CCS misaligns temporally; cross-model transfer fails (\cref{app:negative_details}). The signal is directional, gradual, model-specific, and linearly separable, which excludes change-point, distance, transfer, and objective-alignment methods respectively.\looseness=-1
110	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83b62db3-f9d9-4ef2-ac2d-6b4f0bbb32d6",
  "isSidechain": true,
  "promptId": "ef604098-550a-4d3f-9fa7-47752021e2dc",
  "agentId": "a846c1c041db9ae79",
  "type": "user",
  "uuid": "eeb2fff7-88e2-40c4-a559-81a4243a6c08",
  "sourceToolAssistantUUID": "83b62db3-f9d9-4ef2-ac2d-6b4f0bbb32d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-22T09:50:31.804Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MUJMbxqoBGgTi9rhiaTxvQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eeb2fff7-88e2-40c4-a559-81a4243a6c08",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQ8mFxvBo7BjhB3uXqv",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "6316c81d-08fc-411d-beda-d23e4972ff5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0138yZDG5h1s6xMPxctX6X17",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9774,
      "cache_read_input_tokens": 21715,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9774,
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

_source line 21 · 2026-05-22T09:50:31.809Z_

<details><summary>↩ Tool result · `toolu_01MUJMbxqoBGgTi9rhiaTxvQ`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	Crossing rate reverses the central finding via shallow-layer compression (\cref{app:cosine_volatility,tab:r18b_full_layer}): its shallow preference is an artifact of cosine compression inflating threshold crossings, while threshold-based deep preference reflects genuine separability~\citep{tenney2019bert}; random-label controls confirm this distinction (\cref{app:random_cp}). C1 generalizes across all four models (cross-dataset: \cref{app:cosine_volatility}; split-half: \cref{app:split_half}); C2 is sample-dependent (7--8B cross-validated, 32B descriptive). Annotation noise (${<}2.5$pp BA change; \cref{tab:cp_perturbation}) does not threaten C1. The encoder-quality gradient narrows the HS advantage (384d to 1024d; \cref{app:position_residual}). Type~I risk from ${\sim}$2{,}240 configurations is bounded by the two-stage design and large effect sizes ($d$ 0.58--2.37; \cref{app:effective_tests}). \textbf{Practical mitigation.} We propose a three-level defense against metric-induced layer selection bias. \emph{Level~1 (minimal)}: report layer selections under both threshold-based and frequency-based metric families; divergence exceeding 20\% of model depth (e.g., L2 vs.\ L63 in a 64-layer model) indicates metric-induced bias and warrants treating conclusions as provisional. \emph{Level~2 (recommended)}: a multi-metric audit (\cref{app:deployment_operating_points}) computes all five metrics and flags when ${\geq}3$ select layers differing by ${>}20\%$ of depth---an operational test requiring no additional data. \emph{Level~3 (robust)}: a three-layer ensemble averaging probe predictions from the precision-best, BA-best, and inverse-FPR-best layers eliminates metric pre-selection entirely ($p \leq 0.002$; \cref{tab:ensemble}), but requires cross-validated confirmation before deployment.\looseness=-1
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6316c81d-08fc-411d-beda-d23e4972ff5e",
  "isSidechain": true,
  "promptId": "ef604098-550a-4d3f-9fa7-47752021e2dc",
  "agentId": "a846c1c041db9ae79",
  "type": "user",
  "uuid": "47ba651d-d4ba-472f-93f6-76eb498ebb79",
  "sourceToolAssistantUUID": "6316c81d-08fc-411d-beda-d23e4972ff5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-22T09:50:32.196Z_

<details open><summary>🔧 Tool call — Read · `toolu_012RbnFXrLAXKBjV9gAQe3R3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47ba651d-d4ba-472f-93f6-76eb498ebb79",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQ8mFxvBo7BjhB3uXqv",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "4e0898ee-042b-4981-941b-a2bcaade5265",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0138yZDG5h1s6xMPxctX6X17",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9774,
      "cache_read_input_tokens": 21715,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9774,
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

_source line 23 · 2026-05-22T09:50:32.200Z_

<details><summary>↩ Tool result · `toolu_012RbnFXrLAXKBjV9gAQe3R3`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	Layer selection metric choice can reverse a safety study's central conclusion: for QwQ-32B, the same data yield $p{=}0.83$ or $p{<}0.005$ depending solely on metric. The HS advantage is validated at 7--8B (+20--22pp, nested CV) and exploratory$^\dagger$ at 32B (+15--19pp) against 384d encoders, but conditional on encoder quality and position (partially correlated); generalization beyond HarmThoughts and Qwen (3/4) requires causal validation. Until layer selection is controlled, probe-based safety conclusions from any single metric should be treated as provisional.\looseness=-1
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e0898ee-042b-4981-941b-a2bcaade5265",
  "isSidechain": true,
  "promptId": "ef604098-550a-4d3f-9fa7-47752021e2dc",
  "agentId": "a846c1c041db9ae79",
  "type": "user",
  "uuid": "0a8f6ccf-f49f-41a8-a130-f0c52ef29bf1",
  "sourceToolAssistantUUID": "4e0898ee-042b-4981-941b-a2bcaade5265",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-22T09:50:32.604Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CnhgJqmGJyckj94HYiYZn8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a8f6ccf-f49f-41a8-a130-f0c52ef29bf1",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQ8mFxvBo7BjhB3uXqv",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "ec101d33-3a68-40c6-bdee-d109eef9bf7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0138yZDG5h1s6xMPxctX6X17",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9774,
      "cache_read_input_tokens": 21715,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9774,
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

_source line 25 · 2026-05-22T09:50:32.608Z_

<details><summary>↩ Tool result · `toolu_01CnhgJqmGJyckj94HYiYZn8`</summary>

```text
1	\newpage
2	\section*{Limitations}\label{sec:limitations}
3	
4	\paragraph{Single dataset and annotation quality.}
5	All CP-dependent claims rely on one dataset (HarmThoughts~\citep{harmthoughts}), the only publicly available dataset providing step-level CP annotations for reasoning model traces, with annotations lacking formal inter-annotator agreement; an LLM-based proxy on AdvBench achieved $\kappa{=}0.606$ (\cref{app:iaa}). The geometric precondition (shallow-layer compression) is confirmed on AdvBench (\cref{app:cosine_volatility,app:advbench_cp}), but generalization to other jailbreak datasets, attack taxonomies, or multilingual settings is untested.
6	
7	\paragraph{Statistical power at 32B.}
8	With $n{=}19$--$20$ traces, the minimum detectable effect at 80\% power is 8.6--9.5pp (\cref{app:power_analysis}); all 32B conclusions marked $\dagger$ should be interpreted with this constraint. False positive rates remain 11--50\% (model-dependent), and R1-32B achieves significance only at $W{=}1$ (25\% coverage). These probes characterize the commitment phenomenon rather than constitute production detectors.
9	
10	\paragraph{Architecture coverage and causal status.}
11	Three of four models share the Qwen architecture; only R1-8B (Llama) provides cross-architecture evidence. Random-label controls confirm the crossing-rate geometric bias is Qwen-specific (\cref{app:random_cp}). Results are correlational; causal intervention (e.g., DAS, activation patching) is needed to confirm mechanistic involvement. Whether metric-induced layer selection bias generalizes to non-reasoning LLMs or encoder-only architectures remains open.
12	
13	\section*{Ethics Statement}
14	This work analyzes safety-relevant reasoning traces to characterize probe behavior, not to circumvent safety mechanisms. All experiments use publicly available models and datasets (HarmThoughts, AdvBench). No human subjects were involved. Code and scripts for all experiments and analyses will be released upon acceptance.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec101d33-3a68-40c6-bdee-d109eef9bf7e",
  "isSidechain": true,
  "promptId": "ef604098-550a-4d3f-9fa7-47752021e2dc",
  "agentId": "a846c1c041db9ae79",
  "type": "user",
  "uuid": "aa9cbd60-5e3b-4eb7-a303-368827b5522b",
  "sourceToolAssistantUUID": "ec101d33-3a68-40c6-bdee-d109eef9bf7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-22T09:50:32.895Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E7XuuuPhPubTmXYnB2t1g8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa9cbd60-5e3b-4eb7-a303-368827b5522b",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQ8mFxvBo7BjhB3uXqv",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "c5bb5ecc-2319-438c-8def-91a88a2c7c5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0138yZDG5h1s6xMPxctX6X17",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9774,
      "cache_read_input_tokens": 21715,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9774
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 312,
          "cache_read_input_tokens": 21715,
          "cache_creation_input_tokens": 9774,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9774,
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

_source line 27 · 2026-05-22T09:50:33.152Z_

<details><summary>↩ Tool result · `toolu_01E7XuuuPhPubTmXYnB2t1g8`</summary>

```text
1	@article{trajguard,
2	  title={TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense},
3	  author={Liu, Cheng and Liu, Xiaolei and Li, Xingyu and Xin, Bangzhou and Ding, Kangyi},
4	  journal={arXiv preprint arXiv:2604.07727},
5	  year={2026},
6	  url={https://arxiv.org/abs/2604.07727}
7	}
8	
9	@inproceedings{safeswitch,
10	  title={SafeSwitch: Steering Unsafe {LLM} Behavior via Internal Activation Signals},
11	  author={Han, Peixuan and Qian, Cheng and Chen, Xiusi and Zhang, Yuji and Ji, Heng and Zhang, Denghui},
12	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},
13	  year={2025},
14	  url={https://arxiv.org/abs/2502.01042}
15	}
16	
17	@inproceedings{siren,
18	  title={{LLM} Safety From Within: Detecting Harmful Content with Internal Representations},
19	  author={Jiao, Difan and Liu, Yilun and Yuan, Ye and Tang, Zhenwei and Du, Linfeng and Wu, Haolun and Anderson, Ashton},
20	  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL)},
21	  year={2026},
22	  url={https://arxiv.org/abs/2604.18519}
23	}
24	
25	@article{saferemind,
26	  title={How Does the Thinking Step Influence Model Safety? An Entropy-based Safety Reminder for LRMs},
27	  author={Kim, Su-Hyeon and Jin, Hyundong and Lee, Yejin and Han, Yo-Sub},
28	  journal={arXiv preprint arXiv:2601.03662},
29	  year={2026},
30	  url={https://arxiv.org/abs/2601.03662}
31	}
32	
33	@article{safethink,
34	  title={Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away},
35	  author={Ghosal, Soumya Suvra and Chakraborty, Souradip and Singh, Vaibhav and Huang, Furong and Manocha, Dinesh and Bedi, Amrit Singh},
36	  journal={arXiv preprint arXiv:2602.11096},
37	  year={2026},
38	  url={https://arxiv.org/abs/2602.11096}
39	}
40	
41	@article{selfjailbreak,
42	  title={Self-Jailbreaking: Language Models Can Reason Themselves Out of Safety Alignment After Benign Reasoning Training},
43	  author={Yong, Zheng-Xin and Bach, Stephen H.},
44	  journal={arXiv preprint arXiv:2510.20956},
45	  year={2025},
46	  url={https://arxiv.org/abs/2510.20956}
47	}
48	
49	@article{harmthoughts,
50	  title={When Safety Fails Before the Answer: Benchmarking Harmful Behavior Detection in Reasoning Chains},
51	  author={Kakkar, Ishita and Zhang, Enze and Uppaal, Rheeya and Hu, Junjie},
52	  journal={arXiv preprint arXiv:2604.19001},
53	  year={2026},
54	  url={https://arxiv.org/abs/2604.19001}
55	}
56	
57	@article{belinkov2019analysis,
58	  title={Analysis Methods in Neural Language Processing: A Survey},
59	  author={Belinkov, Yonatan and Glass, James},
60	  journal={Transactions of the Association for Computational Linguistics},
61	  volume={7},
62	  pages={49--72},
63	  year={2019},
64	  url={https://aclanthology.org/Q19-1004/}
65	}
66	
67	@inproceedings{kaya2019shallow,
68	  title={Shallow-Deep Networks: Understanding and Mitigating Network Overthinking},
69	  author={Kaya, Yigitcan and Hong, Sanghyun and Dumitras, Tudor},
70	  booktitle={Proceedings of the 36th International Conference on Machine Learning (ICML)},
71	  pages={3301--3310},
72	  year={2019},
73	  url={https://arxiv.org/abs/1810.07052}
74	}
75	
76	@inproceedings{zhou2020bert,
77	  title={{BERT} Loses Patience: Fast and Robust Inference with Early Exit},
78	  author={Zhou, Wangchunshu and Xu, Canwen and Ge, Tao and McAuley, Julian and Xu, Ke and Wei, Furu},
79	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
80	  volume={33},
81	  pages={18330--18341},
82	  year={2020},
83	  url={https://arxiv.org/abs/2006.04152}
84	}
85	
86	@inproceedings{hewitt2019control,
87	  title={Designing and Interpreting Probes with Control Tasks},
88	  author={Hewitt, John and Liang, Percy},
89	  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
90	  pages={2733--2743},
91	  year={2019},
92	  url={https://aclanthology.org/D19-1275/}
93	}
94	
95	@article{zou2023representation,
96	  title={Representation Engineering: A Top-Down Approach to {AI} Transparency},
97	  author={Zou, Andy and Phan, Long and Chen, Sarah and Campbell, James and Guo, Phillip and Ren, Richard and Pan, Alexander and Yin, Xuwang and Mazeika, Mantas and Dombrowski, Ann-Kathrin and Goel, Shashwat and Li, Nathaniel and Byun, Michael J. and Wang, Zifan and Mallen, Alex and Basart, Steven and Koyejo, Sanmi and Song, Dawn and Fredrikson, Matt and Kolter, J. Zico and Hendrycks, Dan},
98	  journal={arXiv preprint arXiv:2310.01405},
99	  year={2023},
100	  url={https://arxiv.org/abs/2310.01405}
101	}
102	
103	@article{adams2007bayesian,
104	  title={Bayesian Online Changepoint Detection},
105	  author={Adams, Ryan Prescott and MacKay, David J.C.},
106	  journal={arXiv preprint arXiv:0710.3742},
107	  year={2007},
108	  url={https://arxiv.org/abs/0710.3742}
109	}
110	
111	@article{deepseekr1,
112	  title={{DeepSeek-R1}: Incentivizing Reasoning Capability in {LLMs} via Reinforcement Learning},
113	  author={{DeepSeek-AI}},
114	  journal={arXiv preprint arXiv:2501.12948},
115	  year={2025},
116	  url={https://arxiv.org/abs/2501.12948}
117	}
118	
119	@misc{qwq,
120	  title={{QwQ}: Reflect Deeply on the Boundaries of the Unknown},
121	  author={{Qwen Team}},
122	  year={2024},
123	  url={https://qwenlm.github.io/blog/qwq-32b-preview/}
124	}
125	
126	@article{openthinker,
127	  title={Open{T}houghts: Data Recipes for Reasoning Models},
128	  author={Guha, Etash and Marten, Ryan and Keh, Sedrick and Bhatia, Saumya and Ragan-Kelley, Jonathan and Narang, Sharan and Hashimoto, Tatsunori},
129	  journal={arXiv preprint arXiv:2506.04178},
130	  year={2025},
131	  url={https://arxiv.org/abs/2506.04178}
132	}
133	
134	@article{still,
135	  title={Imitate, Explore, and Self-Improve: A Reproduction Report on Slow-thinking Reasoning Systems},
136	  author={Min, Yingqian and Chen, Zhipeng and Jiang, Jinhao and Chen, Jie and Deng, Jia and Hu, Yiwen and Tang, Yiru and Wang, Jiapeng and Cheng, Xiaoxue and Song, Huatong and Zhao, Wayne Xin and Liu, Zheng and Wang, Zhongyuan and Wen, Ji-Rong},
137	  journal={arXiv preprint arXiv:2412.09413},
138	  year={2024},
139	  url={https://arxiv.org/abs/2412.09413}
140	}
141	
142	
143	@inproceedings{burns2023discovering,
144	  title={Discovering Latent Knowledge in Language Models Without Supervision},
145	  author={Burns, Collin and Ye, Haotian and Klein, Dan and Steinhardt, Jacob},
146	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
147	  year={2023},
148	  url={https://arxiv.org/abs/2212.03827}
149	}
150	
151	@inproceedings{tenney2019bert,
152	  title={{BERT} Rediscovers the Classical {NLP} Pipeline},
153	  author={Tenney, Ian and Das, Dipanjan and Pavlick, Ellie},
154	  booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)},
155	  pages={4593--4601},
156	  year={2019},
157	  url={https://aclanthology.org/P19-1452/}
158	}
159	
160	@article{belinkov2022probing,
161	  title={Probing Classifiers: Promises, Shortcomings, and Advances},
162	  author={Belinkov, Yonatan},
163	  journal={Computational Linguistics},
164	  volume={48},
165	  number={1},
166	  pages={207--219},
167	  year={2022},
168	  url={https://aclanthology.org/2022.cl-1.7/}
169	}
170	
171	@inproceedings{zhou2024alignment,
172	  title={How Alignment and Jailbreak Work: Explain {LLM} Safety through Intermediate Hidden States},
173	  author={Zhou, Zhenhong and Yu, Haiyang and Zhang, Xinghua and Xu, Rongwu and Huang, Fei and Li, Yongbin},
174	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2024},
175	  pages={2461--2488},
176	  year={2024},
177	  url={https://arxiv.org/abs/2406.05644}
178	}
179	
180	@inproceedings{zhao2025harmfulness,
181	  title={{LLMs} Encode Harmfulness and Refusal Separately},
182	  author={Zhao, Jiachen and Huang, Jing and Wu, Zhengxuan and Bau, David and Shi, Weiyan},
183	  booktitle={Advances in Neural Information Processing Systems 38 (NeurIPS)},
184	  year={2025},
185	  url={https://arxiv.org/abs/2507.11878}
186	}
187	
188	@inproceedings{arditi2024refusal,
189	  title={Refusal in Language Models Is Mediated by a Single Direction},
190	  author={Arditi, Andy and Obeso, Oscar and Syed, Aaquib and Paleka, Daniel and Panickssery, Nina and Gurnee, Wes and Nanda, Neel},
191	  booktitle={Advances in Neural Information Processing Systems 37 (NeurIPS)},
192	  year={2024},
193	  url={https://arxiv.org/abs/2406.11717}
194	}
195	
196	@article{hcot2025,
197	  title={H-CoT: Hijacking the Chain-of-Thought Safety Reasoning Mechanism to Jailbreak Large Reasoning Models},
198	  author={Kuo, Martin and Zhang, Jianyi and Ding, Aolin and Wang, Qinsi and DiValentin, Louis and Bao, Yujia and Wei, Wei and Li, Hai and Chen, Yiran},
199	  journal={arXiv preprint arXiv:2502.12893},
200	  year={2025},
201	  url={https://arxiv.org/abs/2502.12893}
202	}
203	
204	@article{safedream2026,
205	  title={SafeDream: Safety World Model for Proactive Early Jailbreak Detection},
206	  author={Yan, Bo and Lin, Weikai and Zhu, Yada and Wang, Song},
207	  journal={arXiv preprint arXiv:2604.16824},
208	  year={2026},
209	  url={https://arxiv.org/abs/2604.16824}
210	}
211	
212	@article{hu2026refusal_dynamics,
213	  title={Tracing the Dynamics of Refusal: Exploiting Latent Refusal Trajectories for Robust Jailbreak Detection},
214	  author={Hu, Xulin and Wang, Che and Lim, Wei Yang Bryan and Gao, Jianbo and Chen, Zhong},
215	  journal={arXiv preprint arXiv:2605.02958},
216	  year={2026},
217	  url={https://arxiv.org/abs/2605.02958}
218	}
219	
220	@article{ahrend2026safer_traces,
221	  title={Safer Reasoning Traces: Measuring and Mitigating Chain-of-Thought Leakage in {LLMs}},
222	  author={Ahrend, Patrick and Eder, Tobias and Yang, Xiyang and Pan, Zhiyi and Groh, Georg},
223	  journal={arXiv preprint arXiv:2603.05618},
224	  year={2026},
225	  url={https://arxiv.org/abs/2603.05618}
226	}
227	
228	@article{chen2025unfaithful,
229	  title={Reasoning Models Don't Always Say What They Think},
230	  author={Chen, Yanda and Benton, Joe and Radhakrishnan, Ansh and Uesato, Jonathan and Denison, Carson and Schulman, John and Somani, Arushi and Hase, Peter and Wagner, Misha and Roger, Fabien and Mikulik, Vlad and Bowman, Samuel R. and Leike, Jan and Kaplan, Jared and Perez, Ethan},
231	  journal={arXiv preprint arXiv:2505.05410},
232	  year={2025},
233	  url={https://arxiv.org/abs/2505.05410}
234	}
235	
236	@article{wang2025lrmsafety,
237	  title={Safety in Large Reasoning Models: A Survey},
238	  author={Wang, Cheng and Liu, Yue and Bi, Baolong and Zhang, Duzhen and Li, Zhongzhi and Ma, Yingwei and He, Yufei and Yu, Shengju and Li, Xinfeng and Fang, Junfeng and Zhang, Jiaheng and Hooi, Bryan},
239	  journal={arXiv preprint arXiv:2504.17704},
240	  year={2025},
241	  url={https://arxiv.org/abs/2504.17704}
242	}
243	
244	@article{geiger2023causal,
245	  title={Causal Abstraction: A Theoretical Foundation for Mechanistic Interpretability},
246	  author={Geiger, Atticus and Ibeling, Duligur and Zur, Amir and Chaudhary, Maheep and Chauhan, Sonakshi and Huang, Jing and Arora, Aryaman and Wu, Zhengxuan and Goodman, Noah and Potts, Christopher and Icard, Thomas},
247	  journal={Journal of Machine Learning Research},
248	  volume={26},
249	  number={83},
250	  pages={1--64},
251	  year={2023},
252	  url={https://jmlr.org/papers/v26/23-0058.html}
253	}
254	
255	@inproceedings{alain2017understanding,
256	  title={Understanding Intermediate Layers Using Linear Classifier Probes},
257	  author={Alain, Guillaume and Bengio, Yoshua},
258	  booktitle={Workshop Track, International Conference on Learning Representations (ICLR)},
259	  year={2017},
260	  url={https://arxiv.org/abs/1610.01644}
261	}
262	
263	@inproceedings{conneau2018probing,
264	  title={What You Can Cram into a Single \$\&!\#* Vector: Probing Sentence Embeddings for Linguistic Properties},
265	  author={Conneau, Alexis and Kruszewski, German and Lample, Guillaume and Barrault, Lo\"{i}c and Baroni, Marco},
266	  booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (ACL)},
267	  pages={2126--2136},
268	  year={2018},
269	  url={https://aclanthology.org/P18-1198/}
270	}
271	
272	@article{joad2026refusal_multi,
273	  title={There Is More to Refusal in Large Language Models than a Single Direction},
274	  author={Joad, Faaiz and Hawasly, Majd and Boughorbel, Sabri and Durrani, Nadir and Sencar, Husrev Taha},
275	  journal={arXiv preprint arXiv:2602.02132},
276	  year={2026},
277	  url={https://arxiv.org/abs/2602.02132}
278	}
279	
280	@inproceedings{wollschlager2025geometry,
281	  title={The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence},
282	  author={Wollschl\"{a}ger, Tom and Elstner, Jannes and Geisler, Simon and Cohen-Addad, Vincent and G\"{u}nnemann, Stephan and Gasteiger, Johannes},
283	  booktitle={Proceedings of the 42nd International Conference on Machine Learning (ICML)},
284	  year={2025},
285	  url={https://arxiv.org/abs/2502.17420}
286	}
287	
288	@article{korbak2025cot_monitorability,
289	  title={Chain of Thought Monitorability: A New and Fragile Opportunity for {AI} Safety},
290	  author={Korbak, Tomek and Balesni, Mikita and Barnes, Elizabeth and Bengio, Yoshua and Benton, Joe and Bloom, Joseph and Chen, Mark and Cooney, Alan and Dafoe, Allan and Dragan, Anca and Emmons, Scott and Evans, Owain and Farhi, David and Greenblatt, Ryan and Hendrycks, Dan and Hobbhahn, Marius and Hubinger, Evan and Irving, Geoffrey and Jenner, Erik and Kokotajlo, Daniel and Krakovna, Victoria and Legg, Shane and Lindner, David and Luan, David and M\k{a}dry, Aleksander and Michael, Julian and Nanda, Neel and Orr, Dave and Pachocki, Jakub and Perez, Ethan and Phuong, Mary and Roger, Fabien and Saxe, Joshua and Shlegeris, Buck and Soto, Mart\'{i}n and Steinberger, Eric and Wang, Jasmine and Zaremba, Wojciech and Baker, Bowen and Shah, Rohin and Mikulik, Vlad},
291	  journal={arXiv preprint arXiv:2507.11473},
292	  year={2025},
293	  url={https://arxiv.org/abs/2507.11473}
294	}
295	
296	@article{hagendorff2026lrm_jailbreak,
297	  title={Large Reasoning Models Are Autonomous Jailbreak Agents},
298	  author={Hagendorff, Thilo and Derner, Erik and Oliver, Nuria},
299	  journal={Nature Communications},
300	  year={2026},
301	  url={https://arxiv.org/abs/2508.04039}
302	}
303	
304	@inproceedings{qi2025shallow_alignment,
305	  title={Safety Alignment Should Be Made More Than Just a Few Tokens Deep},
306	  author={Qi, Xiangyu and Panda, Ashwinee and Lyu, Kaifeng and Ma, Xiao and Roy, Subhrajit and Beirami, Ahmad and Mittal, Prateek and Henderson, Peter},
307	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
308	  year={2025},
309	  url={https://arxiv.org/abs/2406.05946}
310	}
311	
312	@inproceedings{belrose2023tunedlens,
313	  title={Eliciting Latent Predictions from Transformers with the Tuned Lens},
314	  author={Belrose, Nora and Furman, Zach and Smith, Logan and Halber{\v{s}}tadt, Rusheb and Paige, Brooks and Tegmark, Max and Biderman, Stella},
315	  booktitle={International Conference on Learning Representations (ICLR)},
316	  year={2023},
317	  url={https://arxiv.org/abs/2303.08112}
318	}
319	
320	@inproceedings{belrose2023leace,
321	  title={{LEACE}: Perfect Linear Concept Erasure in Closed Form},
322	  author={Belrose, Nora and Schneider-Joseph, David and Ravfogel, Shauli and Cotterell, Ryan and Raff, Edward and Biderman, Stella},
323	  booktitle={Advances in Neural Information Processing Systems 36 (NeurIPS)},
324	  year={2023},
325	  url={https://arxiv.org/abs/2306.03819}
326	}
327	
328	@article{elazar2021amnesic,
329	  title={Amnesic Probing: Behavioral Explanation with Amnesic Counterfactuals},
330	  author={Elazar, Yanai and Ravfogel, Shauli and Jacovi, Alon and Goldberg, Yoav},
331	  journal={Transactions of the Association for Computational Linguistics},
332	  volume={9},
333	  pages={160--175},
334	  year={2021},
335	  url={https://aclanthology.org/2021.tacl-1.10/}
336	}
337	
338	@article{mao2025selfjailbreak_reasoning,
339	  title={When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models},
340	  author={Mao, Yingzhi and Zhang, Chunkang and Wang, Junxiang and Guan, Xinyan and Cao, Boxi and Lu, Yaojie and Lin, Hongyu and Han, Xianpei and Sun, Le},
341	  journal={arXiv preprint arXiv:2510.21285},
342	  year={2025},
343	  url={https://arxiv.org/abs/2510.21285}
344	}
345	
346	@article{alvarez2026transport_geometry,
347	  title={Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry},
348	  author={Alvarez, Tyler and Baheri, Ali},
349	  journal={arXiv preprint arXiv:2605.13772},
350	  year={2026},
351	  note={Concurrent work},
352	  url={https://arxiv.org/abs/2605.13772}
353	}
354	
355	@book{efron1993bootstrap,
356	  title={An Introduction to the Bootstrap},
357	  author={Efron, Bradley and Tibshirani, Robert J.},
358	  year={1993},
359	  publisher={Chapman \& Hall/CRC}
360	}
361	
362	@article{diciccio1996bootstrap,
363	  title={Bootstrap confidence intervals},
364	  author={DiCiccio, Thomas J and Efron, Bradley},
365	  journal={Statistical Science},
366	  volume={11},
367	  number={3},
368	  pages={189--228},
369	  year={1996}
370	}
371	
372	@article{baker2025monitoring,
373	  title={Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation},
374	  author={Baker, Bowen and Huizinga, Joost and Gao, Leo and Dou, Zehao and Guan, Melody Y. and Madry, Aleksander and Zaremba, Wojciech and Pachocki, Jakub and Farhi, David},
375	  journal={arXiv preprint arXiv:2503.11926},
376	  year={2025},
377	  url={https://arxiv.org/abs/2503.11926}
378	}
379	
380	@article{kadali2025internal,
381	  title={Do Internal Layers of {LLMs} Reveal Patterns for Jailbreak Detection?},
382	  author={Kadali, Sri Durga Sai Sowmya and Papalexakis, Evangelos E.},
383	  journal={arXiv preprint arXiv:2510.06594},
384	  year={2025},
385	  url={https://arxiv.org/abs/2510.06594}
386	}
387	
388	@article{yin2025refusal_cliff,
389	  title={Refusal Falls off a Cliff: How Safety Alignment Fails in Reasoning?},
390	  author={Yin, Qingyu and Leong, Chak Tou and Yang, Linyi and Huang, Wenxuan and Li, Wenjie and Wang, Xiting and Yoon, Jaehong and Xing, Yun and Yu, Xing and Gu, Jinjin},
391	  journal={arXiv preprint arXiv:2510.06036},
392	  year={2025},
393	  url={https://arxiv.org/abs/2510.06036}
394	}
395	
396	@article{boxo2025linear_probes,
397	  title={Linear Probes Rely on Textual Evidence: Results from Leakage Mitigation Studies in Language Models},
398	  author={Boxo, Gerard and Neelappa, Aman and Raval, Shivam},
399	  journal={arXiv preprint arXiv:2509.21344},
400	  year={2025},
401	  url={https://arxiv.org/abs/2509.21344}
402	}
403	
404	@article{xiang2025guardreasoner,
405	  title={{GuardReasoner}: Towards Reasoning-based {LLM} Safeguards},
406	  author={Liu, Yue and Gao, Hongcheng and Zhai, Shengfang and He, Yufei and Xia, Jun and Hu, Zhengyu and Chen, Yulin and Yang, Xihong and Zhang, Jiaheng and Li, Stan Z. and Xiong, Hui and Hooi, Bryan},
407	  journal={arXiv preprint arXiv:2501.18492},
408	  year={2025},
409	  url={https://arxiv.org/abs/2501.18492}
410	}
411	
412	
413	@inproceedings{reimers2019sentence,
414	  title={Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},
415	  author={Reimers, Nils and Gurevych, Iryna},
416	  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
417	  pages={3982--3992},
418	  year={2019},
419	  url={https://aclanthology.org/D19-1410/}
420	}
421	
422	@inproceedings{wang2020minilm,
423	  title={{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},
424	  author={Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},
425	  booktitle={Advances in Neural Information Processing Systems 33 (NeurIPS)},
426	  year={2020},
427	  url={https://arxiv.org/abs/2002.10957}
428	}
429	
430	@article{xiao2023cpack,
431	  title={C-Pack: Packaged Resources to Advance General Chinese Embedding},
432	  author={Xiao, Shitao and Liu, Zheng and Zhang, Peitian and Muennighoff, Niklas},
433	  journal={arXiv preprint arXiv:2309.07597},
434	  year={2023},
435	  url={https://arxiv.org/abs/2309.07597}
436	}
437	
438	@article{page1954cusum,
439	  title={Continuous Inspection Schemes},
440	  author={Page, E. S.},
441	  journal={Biometrika},
442	  volume={41},
443	  number={1/2},
444	  pages={100--115},
445	  year={1954}
446	}
447	
448	@inproceedings{jawahar2019bert,
449	  title={What Does {BERT} Learn about the Structure of Language?},
450	  author={Jawahar, Ganesh and Sagot, Beno{\^i}t and Seddah, Djam{\'e}},
451	  booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)},
452	  pages={3651--3657},
453	  year={2019},
454	  url={https://aclanthology.org/P19-1356}
455	}
456	
457	@inproceedings{voita2020information,
458	  title={Information-Theoretic Probing with Minimum Description Length},
459	  author={Voita, Elena and Titov, Ivan},
460	  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
461	  pages={183--196},
462	  year={2020},
463	  url={https://aclanthology.org/2020.emnlp-main.14}
464	}
465	
466	@inproceedings{pimentel2020information,
467	  title={Information-Theoretic Probing for Linguistic Structure},
468	  author={Pimentel, Tiago and Valvoda, Josef and Hall Maudslay, Rowan and Zmigrod, Ran and Williams, Adina and Cotterell, Ryan},
469	  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL)},
470	  pages={4609--4622},
471	  year={2020},
472	  url={https://aclanthology.org/2020.acl-main.420}
473	}
474	
475	@inproceedings{ravfogel2020null,
476	  title={Null It Out: Guarding Protected Attributes by Iterative Nullspace Projection},
477	  author={Ravfogel, Shauli and Elazar, Yanai and Gonen, Hila and Twiton, Michael and Goldberg, Yoav},
478	  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL)},
479	  pages={7237--7256},
480	  year={2020},
481	  url={https://aclanthology.org/2020.acl-main.647}
482	}
483	
484	@inproceedings{ravfogel2022rlace,
485	  title={Linear Adversarial Concept Erasure},
486	  author={Ravfogel, Shauli and Twiton, Michael and Goldberg, Yoav and Cotterell, Ryan},
487	  booktitle={Proceedings of the 39th International Conference on Machine Learning (ICML)},
488	  pages={18400--18421},
489	  year={2022},
490	  volume={162},
491	  series={Proceedings of Machine Learning Research},
492	  publisher={PMLR},
493	  url={https://proceedings.mlr.press/v162/ravfogel22a.html}
494	}
495	
496	@article{rogers2020primer,
497	  title={A Primer in {BERTology}: What We Know About How {BERT} Works},
498	  author={Rogers, Anna and Kovaleva, Olga and Rumshisky, Anna},
499	  journal={Transactions of the Association for Computational Linguistics},
500	  volume={8},
501	  pages={842--866},
502	  year={2020},
503	  url={https://aclanthology.org/2020.tacl-1.54}
504	}
505	
506	@article{wang2024e5mistral,
507	  title={Improving Text Embeddings with Large Language Models},
508	  author={Wang, Liang and Yang, Nan and Huang, Xiaolong and Yang, Linjun and Majumder, Rangan and Wei, Furu},
509	  journal={arXiv preprint arXiv:2401.00368},
510	  year={2024},
511	  url={https://arxiv.org/abs/2401.00368}
512	}
513	
514	
515	@article{marks2024geometry,
516	  title={The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets},
517	  author={Marks, Samuel and Tegmark, Max},
518	  journal={arXiv preprint arXiv:2310.06824},
519	  year={2024},
520	  url={https://arxiv.org/abs/2310.06824}
521	}
522	
523	@article{gelman2013garden,
524	  title={The Garden of Forking Paths: Why Multiple Comparisons Can Be a Problem, Even When There Is No ``Fishing Expedition'' or ``p-Hacking'' and the Research Hypothesis Was Posited Ahead of Time},
525	  author={Gelman, Andrew and Loken, Eric},
526	  journal={Department of Statistics, Columbia University},
527	  year={2013},
528	  url={http://www.stat.columbia.edu/~gelman/research/unpublished/p_hacking.pdf}
529	}
530	
531	@inproceedings{azaria2023internal,
532	  title={The Internal State of an {LLM} Knows When It's Lying},
533	  author={Azaria, Amos and Mitchell, Tom},
534	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2023},
535	  pages={967--976},
536	  year={2023},
537	  url={https://aclanthology.org/2023.findings-emnlp.68/}
538	}
539	
540	@inproceedings{turpin2023language,
541	  title={Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting},
542	  author={Turpin, Miles and Michael, Julian and Perez, Ethan and Bowman, Samuel R.},
543	  booktitle={Advances in Neural Information Processing Systems},
544	  volume={36},
545	  year={2023},
546	  url={https://arxiv.org/abs/2305.04388}
547	}
548	
549	@article{pais2026linear_probe_scaling,
550	  title={Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling},
551	  author={Nordby, Erik and Pais, Tasha and Parrack, Aviel},
552	  journal={arXiv preprint arXiv:2604.13386},
553	  year={2026},
554	  url={https://arxiv.org/abs/2604.13386}
555	}
556	
557	@inproceedings{jiang2025hiddendetect,
558	  title={{HiddenDetect}: Detecting Jailbreak Attacks against Large Vision-Language Models via Monitoring Hidden States},
559	  author={Jiang, Yilei and Gao, Xinyan and Peng, Tianshuo and Tan, Yingshui and Zhu, Xiaoyong and Zheng, Bo and Yue, Xiangyu},
560	  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},
561	  year={2025},
562	  url={https://arxiv.org/abs/2502.14744}
563	}
564	
565	@inproceedings{safeint2025,
566	  title={{SafeInt}: Shielding Large Language Models from Jailbreak Attacks via Safety-Aware Representation Intervention},
567	  author={Wu, Jiaqi and Chen, Chen and Hou, Chunyan and Yuan, Xiaojie},
568	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},
569	  year={2025},
570	  url={https://arxiv.org/abs/2502.15594}
571	}
572	
573	@inproceedings{rcs2026,
574	  title={Rethinking Jailbreak Detection of Large Vision Language Models with Representational Contrastive Scoring},
575	  author={Hua, Peichun and Li, Hao and Shi, Shanghao and Yu, Zhiyuan and Zhang, Ning},
576	  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL)},
577	  year={2026},
578	  url={https://arxiv.org/abs/2512.12069}
579	}
580	
581	@article{chan2025probing,
582	  title={Can We Predict Alignment Before Models Finish Thinking? {Towards} Monitoring Misaligned Reasoning Models},
583	  author={Chan, Yik Siu and Yong, Zheng-Xin and Bach, Stephen H.},
584	  journal={arXiv preprint arXiv:2507.12428},
585	  year={2025},
586	  url={https://arxiv.org/abs/2507.12428}
587	}
588	
589	@article{zhao2026safeprobing,
590	  title={Defending Large Language Models Against Jailbreak Attacks via In-Decoding Safety-Awareness Probing},
591	  author={Zhao, Yinzhi and Wang, Ming and Feng, Shi and Yang, Xiaocui and Wang, Daling and Zhang, Yifei},
592	  journal={arXiv preprint arXiv:2601.10543},
593	  year={2026},
594	  url={https://arxiv.org/abs/2601.10543}
595	}
596	
597	@article{chia2025probing_subspaces,
598	  title={Probing Latent Subspaces in {LLM} for {AI} Security: Identifying and Manipulating Adversarial States},
599	  author={Chia, Yik Siu and Pan, Shirui},
600	  journal={arXiv preprint arXiv:2503.09066},
601	  year={2025},
602	  url={https://arxiv.org/abs/2503.09066}
603	}
604	
605	@article{chrabaszcz2026monitoring,
606	  title={Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics},
607	  author={Chrab\k{a}szcz, Maciej and Szymczyk, Aleksander and Sendera, Marcin and Trzci\'{n}ski, Tomasz and Cygert, Sebastian},
608	  journal={arXiv preprint arXiv:2605.18549},
609	  year={2026},
610	  note={Concurrent work},
611	  url={https://arxiv.org/abs/2605.18549}
612	}
613	
614	@article{damirchi2026truth,
615	  title={Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning},
616	  author={Damirchi, Hamed and Meza De la Jara, Ignacio and Abbasnejad, Ehsan and Shamsi, Afshar and Zhang, Zhen and Shi, Javen},
617	  journal={arXiv preprint arXiv:2603.01326},
618	  year={2026},
619	  url={https://arxiv.org/abs/2603.01326}
620	}
621	
622	@article{zhang2025reasoning_right,
623	  title={Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification},
624	  author={Zhang, Anqi and Chen, Yulin and Pan, Jane and Zhao, Chen and Panda, Aurojit and Li, Jinyang and He, He},
625	  journal={arXiv preprint arXiv:2504.05419},
626	  year={2025},
627	  url={https://arxiv.org/abs/2504.05419}
628	}
629	
630	@article{meyoyan2026bertology,
631	  title={A BERTology View of LLM Orchestrations: Token- and Layer-Selective Probes for Efficient Single-Pass Classification},
632	  author={Meyoyan, Gonzalo Ariel and Del Corro, Luciano},
633	  journal={arXiv preprint arXiv:2601.13288},
634	  year={2026},
635	  url={https://arxiv.org/abs/2601.13288}
636	}
637	
638	@article{schulz2025roadmap,
639	  title={A Concrete Roadmap towards Safety Cases based on Chain-of-Thought Monitoring},
640	  author={Schulz, Till},
641	  journal={arXiv preprint arXiv:2510.19476},
642	  year={2025},
643	  url={https://arxiv.org/abs/2510.19476}
644	}
645	
646	
647	@book{cohen1988statistical,
648	  title={Statistical Power Analysis for the Behavioral Sciences},
649	  author={Cohen, Jacob},
650	  year={1988},
651	  edition={2nd},
652	  publisher={Lawrence Erlbaum Associates}
653	}
654	
655	@article{templeton2024scaling,
656	  title={Scaling Monosemanticity: Extracting Interpretable Features from {Claude} 3 {Sonnet}},
657	  author={Templeton, Adly and Conerly, Tom and Marcus, Jonathan and Lindsey, Jack and Bricken, Trenton and Chen, Brian and Pearce, Adam and Citro, Craig and Ameisen, Emmanuel and Jones, Andy and Cunningham, Hoagy and Turner, Nicholas L and McDougall, Callum and MacDiarmid, Monte and Freeman, C. Daniel and Sumers, Theodore R and Rees, Edward and Batson, Joshua and Jermyn, Adam and Carter, Shan and Olah, Chris and Henighan, Tom},
658	  journal={Transformer Circuits Thread},
659	  year={2024}
660	}
661	
662	@article{turner2023activation,
663	  title={Activation Addition: Steering Language Models Without Optimization},
664	  author={Turner, Alexander Matt and Thiergart, Lisa and Udell, David and Leech, Gavin and Mini, Ulisse and MacDiarmid, Monte},
665	  journal={arXiv preprint arXiv:2308.10248},
666	  year={2023}
667	}
668	
669	@inproceedings{li2023iti,
670	  title={Inference-Time Intervention: Eliciting Truthful Answers from a Language Model},
671	  author={Li, Kenneth and Patel, Oam and Vi{\'e}gas, Fernanda and Pfister, Hanspeter and Wattenberg, Martin},
672	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
673	  year={2023},
674	  url={https://arxiv.org/abs/2306.03341}
675	}
676	
677	@article{levinstein2024liedetector,
678	  title={Still No Lie Detector for Language Models},
679	  author={Levinstein, Benjamin A. and Herrmann, Daniel A.},
680	  journal={arXiv preprint arXiv:2307.00175},
681	  year={2024},
682	  url={https://arxiv.org/abs/2307.00175}
683	}
684	
685	@article{advbench,
686	  title={Universal and Transferable Adversarial Attacks on Aligned Language Models},
687	  author={Zou, Andy and Wang, Zifan and Kolter, J. Zico and Fredrikson, Matt},
688	  journal={arXiv preprint arXiv:2307.15043},
689	  year={2023}
690	}
691	
692	@article{vitel2025layer,
693	  title={First is Not Really Better Than Last: Evaluating Layer Choice and Aggregation Strategies in Language Model Data Influence Estimation},
694	  author={Vitel, Dmytro and Chhabra, Anshuman},
695	  journal={arXiv preprint arXiv:2511.04715},
696	  year={2025},
697	  url={https://arxiv.org/abs/2511.04715}
698	}
699	
700	@article{zhou2025ghost,
701	  title={Exposing the Ghost in the Transformer: Abnormal Detection for Large Language Models via Hidden State Forensics},
702	  author={Zhou, Shide and Wang, Kailong and Shi, Ling and Wang, Haoyu},
703	  journal={arXiv preprint arXiv:2504.00446},
704	  year={2025},
705	  url={https://arxiv.org/abs/2504.00446}
706	}
707	
708	@article{carpenter2000bootstrap,
709	  title={Bootstrap confidence intervals: when, which, what? {A} practical guide for medical statisticians},
710	  author={Carpenter, James and Bithell, John},
711	  journal={Statistics in Medicine},
712	  volume={19},
713	  number={9},
714	  pages={1141--1164},
715	  year={2000},
716	  publisher={Wiley}
717	}
718	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5bb5ecc-2319-438c-8def-91a88a2c7c5a",
  "isSidechain": true,
  "promptId": "ef604098-550a-4d3f-9fa7-47752021e2dc",
  "agentId": "a846c1c041db9ae79",
  "type": "user",
  "uuid": "e0d2ff69-21c2-42c9-8617-b31a56acb43e",
  "sourceToolAssistantUUID": "c5bb5ecc-2319-438c-8def-91a88a2c7c5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-22T09:50:37.121Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YAHQ2MdU6zsFfaYAwMhg1s`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0d2ff69-21c2-42c9-8617-b31a56acb43e",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQ9CKqbXT15RQnhYMav",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "6abd1525-e53f-4094-b8e8-a617c8ee40ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MoMYrKezx6ovzyW3mWQBPr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14490,
      "cache_read_input_tokens": 31489,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14490
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 92,
          "cache_read_input_tokens": 31489,
          "cache_creation_input_tokens": 14490,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14490,
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

_source line 29 · 2026-05-22T09:50:37.388Z_

<details><summary>↩ Tool result · reported error · `toolu_01YAHQ2MdU6zsFfaYAwMhg1s`</summary>

```text
File content (37324 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6abd1525-e53f-4094-b8e8-a617c8ee40ea",
  "isSidechain": true,
  "promptId": "ef604098-550a-4d3f-9fa7-47752021e2dc",
  "agentId": "a846c1c041db9ae79",
  "type": "user",
  "uuid": "b2fdc81d-139c-41b7-8339-e5598ad59994",
  "toolUseResult": "Error: File content (37324 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "6abd1525-e53f-4094-b8e8-a617c8ee40ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-22T09:50:40.533Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JEqy3rkobnuLfu84UNBRGV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2fdc81d-139c-41b7-8339-e5598ad59994",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQ9WYTW59WnWzhMsuhD",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "994b4d1f-889a-4000-bdd3-ba0d14c93780",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WCeC58Y4fZNRNjAgywArJ5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 153,
      "cache_read_input_tokens": 45979,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 153
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 109,
          "cache_read_input_tokens": 45979,
          "cache_creation_input_tokens": 153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 153,
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

_source line 31 · 2026-05-22T09:50:40.540Z_

<details><summary>↩ Tool result · `toolu_01JEqy3rkobnuLfu84UNBRGV`</summary>

```text
1	\appendix
2	
3	\noindent\textbf{Appendix Contents:}
4	\cref{app:checklist}~Responsible NLP Research Checklist;
5	\cref{app:layer_sweep}~Layer Sweep Results;
6	\cref{app:cosine_volatility}~Representation Compression Analysis;
7	\cref{app:holm_bonferroni}~Holm-Bonferroni Correction;
8	\cref{app:window_ablation}~Window Size Ablation;
9	\cref{app:ot7b_details}~OpenThinker-7B Details;
10	\cref{app:gru_details}~GRU Training Details;
11	\cref{app:control}~Control Task Methodology;
12	\cref{sec:oracle}~Oracle Upper Bound;
13	\cref{app:cp_perturbation}~CP Annotation Perturbation;
14	\cref{app:bocpd_config}~BOCPD/CUSUM Configuration;
15	\cref{app:k_ablation}~Detection Threshold Ablation;
16	\cref{app:threshold_sensitivity}~Decision Threshold Sensitivity;
17	\cref{app:bug}~M002 Bug Disclosure;
18	\cref{app:two_stage}~Adaptive Two-Stage Detection;
19	\cref{app:temporal_details}~Temporal Ablation Details;
20	\cref{app:negative_details}~Negative Results Details (incl.\ \cref{tab:negative});
21	\cref{app:transfer_details}~Cross-Model Transfer Details;
22	\cref{app:encoder_robustness}~Encoder Robustness;
23	\cref{app:random_projection}~Random Projection Baseline;
24	\cref{app:e5_mistral}~LLM-Based Text Encoder;
25	\cref{app:position_residual}~Position-Residualized Probing;
26	\cref{app:hyperparameter_robustness}~Hyperparameter Robustness;
27	\cref{app:multi_seed}~Multi-Seed Stability;
28	\cref{app:split_half}~Split-Half Internal Validity;
29	\cref{app:ba_layer_comparison}~BA-Layer Modality Comparison;
30	\cref{app:power_analysis}~Post-Hoc Power Analysis.
31	
32	\section{Responsible NLP Research Checklist}
33	\label{app:checklist}
34	
35	We address the ARR Responsible NLP Research requirements below.
36	
37	\begin{itemize}
38	    \item \textbf{Limitations discussed:} Yes (\cref{sec:limitations}).
39	    \item \textbf{Potential risks:} This research analyzes jailbreak traces to understand how reasoning models commit to generating harmful content. We do not develop new attack methods or release jailbreak prompts. All analyzed content comes from the publicly available HarmThoughts benchmark. We acknowledge a dual-use concern: safety probes that detect commitment could in principle be used to craft reasoning traces that evade detection. We believe the defensive value of understanding commitment dynamics outweighs this risk, as evasion requires white-box access to the probe, which a deployed monitoring system would not expose.
40	    \item \textbf{Computational budget:} Our experiments involve 4 models with 209, 228, 100, and 95 traces respectively (632 total), using linear probes and single-layer GRUs. Total compute is minimal (under 4 GPU-hours on a single RTX A6000). No large-scale pretraining or finetuning was performed.
41	    \item \textbf{Data:} We use HarmThoughts, a publicly available benchmark with step-level safety annotations, and AdvBench~\citep{advbench} for cross-dataset geometric validation. No new data collection was performed.
42	    \item \textbf{Human subjects:} No human subjects research was conducted.
43	    \item \textbf{Reproducibility:} All hyperparameters are reported in \cref{app:gru_details,app:bocpd_config}. Code and corrected data will be released upon publication.
44	\end{itemize}
45	
46	
47	\section{Layer Sweep Results}
48	\label{app:layer_sweep}
49	
50	For each model, we sweep all transformer layers and evaluate five candidate selection metrics: (1)~balanced accuracy $\times$ crossing rate (the CR-composite), (2)~pure balanced accuracy, (3)~precision, (4)~inverse pre-CP FPR, and (5)~an additive composite. The CR-composite systematically selects shallow layers across all four models (including R1-8B under the full L0--L24 sweep; \cref{tab:r18b_full_layer}) because early-layer representations exhibit higher crossing rates (more frequent threshold crossings) regardless of discriminative power. Three threshold-based metrics (precision, inverse FPR, additive composite) converge on deep layers for all models; pure balanced accuracy selects layers whose depth varies with the data split (under 70/30: L30 for QwQ-32B, L47 for R1-32B; under the canonical 60/20/20: L63 and L46 respectively; \cref{tab:ba_layer_results}).
51	
52	\paragraph{Selected layers.} R1-8B: under the original L12--L24 sweep, all five metrics agreed on L14 (44\%); extending to L0--L24, crossing rate shifts to L0 while threshold-based metrics retain L14, a 16-layer gap (\cref{tab:r18b_full_layer}). OT-7B: CR-composite selects L0 (0\%), threshold-based consensus selects L16 (57\%). QwQ-32B: CR-composite selects L2 (3\%), threshold-based consensus selects L63 (98\%). R1-32B: CR-composite selects L10 (16\%), threshold-based consensus selects L63 (98\%). The disagreement is most extreme for 64-layer models, where the CR-composite selects layers in the bottom 16\% of the network while threshold-based metrics select layers at 98\% depth. Under 70/30, pure balanced accuracy selects L30 (47\%) for QwQ-32B and L47 (73\%) for R1-32B; under the canonical 60/20/20, it selects L63 (98\%) and L46 (72\%), which demonstrates sensitivity to the data split.
53	
54	\paragraph{Impact on modality comparison.} At the CR-composite layers, HS vs.\ text precision $p$-values are 0.064 (R1-32B) and 0.35--0.83 (QwQ-32B), both non-significant. At the threshold-based deep layers, all $p$-values fall below 0.005. The initially reported ``scale-dependent'' pattern (HS advantage at 7--8B but not 32B) was entirely an artifact of layer selection methodology, not a genuine property of model scale (\cref{sec:layer-results}).
55	
56	\paragraph{Layer selection stability (LOO-CV).} Leave-one-out cross-validation on the validation set shows moderate consistency for 7--8B models (65--68\% dominant-layer agreement) but lower for 32B, confirming that layer selection instability is particularly acute at small sample sizes. Under pure balanced accuracy, the dominant layer is selected in 68\% (QwQ-32B: L30, 13/19 folds) and 65\% (R1-32B: L47, 13/20 folds) of folds. Alternative selections scatter across neighboring layers (L29, L55--56 for QwQ; L32, L38, L43 for R1-32B), reinforcing the need for multi-metric auditing rather than single-metric layer selection. Threshold-based metrics show tighter convergence to L63 for both 32B models. Expanding the criterion from top-1 to top-3 layers does not change conclusions: the top-3 BA-selected layers for QwQ-32B (L30, L29, L55) and R1-32B (L47, L43, L38) all fall in the mid-to-deep range, and threshold-based metrics remain converged at L63 across all folds.
57	
58	\paragraph{Joint (layer, $W$) sensitivity.} Under the original 70/30 validation protocol, we evaluate QwQ-32B across 64 layers $\times$ 3 windows ($W \in \{1, 3, 5\}$) (192 configurations) (\cref{tab:joint_layer_w}). L60 is near-optimal: within 2.1pp of the global best at $W{=}3$ and the top-ranked layer at $W{=}5$. (Under 60/20/20, threshold-based metrics select L63; the shift from L60 to L63 across splits itself illustrates layer selection sensitivity.) The optimal layer shifts from middle-deep (L46--47 at $W{=}1$) to deep (L60 at $W{=}5$), confirming a layer-window interaction. For R1-8B, optimal precision layers shift similarly (L16 at $W{=}1$ $\to$ L9 at $W{=}15$; Kendall's $\tau{=}{-}0.91$, $p{=}0.071$), a consistent negative trend that does not reach significance at $n{=}4$ windows. L30, selected by per-fold LOO-CV at $W{=}1$ under balanced accuracy, is suboptimal across all windows (max BA $= 0.769$ vs.\ global best 0.817). Joint (layer, $W$) stability was evaluated via grid search on $W \in \{1, 3, 5\}$ for QwQ-32B only; full leave-one-fold-out validation of the (layer, $W$) pair and extension to R1-32B remain for future work.
59	
60	\begin{table}[htbp]
61	\centering
62	\small
63	\caption{QwQ-32B joint (layer, $W$) grid search under 70/30 validation. L60 is near-optimal at recommended windows ($W{=}3$--$5$). L30 (LOO-CV selection at $W{=}1$) is suboptimal across all windows. Under the canonical 60/20/20 split, threshold-based metrics select L63.}
64	\label{tab:joint_layer_w}
65	\resizebox{\columnwidth}{!}{%
66	\begin{tabular}{clccc}
67	\toprule
68	$W$ & \textbf{Best layer} & \textbf{Best BA} & \textbf{L60 BA} & \textbf{L60 rank} \\
69	\midrule
70	1 & L47 & 0.798 & 0.783 & $\sim$15th \\
71	3 & L46 & 0.817 & 0.796 & $\sim$6th \\
72	5 & L60 & 0.808 & 0.808 & 1st \\
73	\bottomrule
74	\end{tabular}}
75	\end{table}
76	
77	\paragraph{R1-8B full-layer sweep.}
78	\label{app:r18b_full_layer}
79	The original R1-8B layer sweep covered L12--L24 (13 layers), where all five metrics agreed on L14 (\cref{tab:layer_selection}). Extending to L0--L24 reveals that crossing rate consistently selects L0 across all window sizes, while threshold-based metrics retain mid-to-deep layers (L12--L16 for $W{=}1$--$5$; L9 at $W{=}15$, marginal $\Delta{=}0.003$ between shallow and deep means), a 9--16 layer divergence (\cref{tab:r18b_full_layer}). Unlike 32B models, the bias is isolated to crossing rate; threshold-based metrics show no shallow shift for R1-8B. This confirms the crossing-rate bias generalizes to Llama-architecture models. HS probes maintain significant advantage across all 25 layers and window sizes (precision gap ${\sim}$0.15--0.17), unlike OT-7B and 32B models where significance drops at shallow layers.
80	
81	\begin{table}[htbp]
82	\centering
83	\small
84	\caption{R1-8B full-layer sweep (L0--L24, extending the original L12--L24 range). Best layer selected by crossing rate vs.\ threshold-based metrics across four window sizes. Score = balanced accuracy at the threshold-based layer. Layer gap = crossing-rate layer minus threshold-based layer.}
85	\label{tab:r18b_full_layer}
86	\resizebox{\columnwidth}{!}{%
87	\begin{tabular}{lcccc}
88	\toprule
89	& $W{=}1$ & $W{=}3$ & $W{=}5$ & $W{=}15$ \\
90	\midrule
91	Crossing rate & L0 & L0 & L0 & L0 \\
92	Threshold (composite) & L16 (0.789) & L12 (0.796) & L12 (0.803) & L9 (0.784) \\
93	\midrule
94	Layer gap & 16 & 12 & 12 & 9 \\
95	\bottomrule
96	\end{tabular}}
97	\end{table}
98	
99	\subsection{Random-Label Decomposition Control}
100	\label{app:random_cp}
101	
102	To decompose the sources of metric disagreement in layer selection, we replace the true CP annotations with uniformly random labels and re-run the full layer sweep (10 random-label repeats per model). We test QwQ-32B (95 traces, 64 layers) and R1-8B (209 traces, 25 layers); \cref{tab:random_cp,tab:random_cp_r18b} report the fraction of repeats selecting a shallow layer and the mean selected layer.
103	
104	\begin{table}[htbp]
105	\centering
106	\small
107	\caption{QwQ-32B layer selection under random CP labels (10 repeats). Shallow\%: fraction selecting a layer L$\leq$10. Real-CP layer shown for reference.}
108	\label{tab:random_cp}
109	\setlength{\tabcolsep}{4pt}
110	\resizebox{\columnwidth}{!}{%
111	\begin{tabular}{lcccc}
112	\toprule
113	\textbf{Metric} & \textbf{Real-CP} & \textbf{Shallow\%} & \textbf{Rand.\ mean layer} \\
114	\midrule
115	Crossing rate & L4 & 100\% & $3.4 \pm 2.6$ \\
116	CR-composite & L4 & 80\% & $13.1 \pm 18.1$ \\
117	Precision & L63 & 20\% & $33.8 \pm 19.8$ \\
118	Inv.\ FPR & L62 & 10\% & $36.4 \pm 17.0$ \\
119	Bal.\ accuracy & L63 & 20\% & $33.3 \pm 20.3$ \\
120	\bottomrule
121	\end{tabular}}
122	\end{table}
123	
124	\begin{table}[htbp]
125	\centering
126	\small
127	\caption{R1-8B layer selection under random CP labels (10 repeats). Shallow\%: fraction selecting L$\leq$4 (bottom quintile of 25 layers). $\dagger$: degenerate, all repeats select L0 with zero variance, indicating destroyed signal rather than shallow preference.}
128	\label{tab:random_cp_r18b}
129	\setlength{\tabcolsep}{4pt}
130	\resizebox{\columnwidth}{!}{%
131	\begin{tabular}{lcccc}
132	\toprule
133	\textbf{Metric} & \textbf{Real-CP} & \textbf{Shallow\%} & \textbf{Rand.\ mean layer} \\
134	\midrule
135	Crossing rate & L0 & 0\% & $10.7 \pm 4.8$ \\
136	CR-composite & L0 & 0\% & $13.7 \pm 6.7$ \\
137	Precision & L23 & 100\%$^{\dagger}$ & $0.0 \pm 0.0$ \\
138	Inv.\ FPR & L13 & 100\%$^{\dagger}$ & $0.0 \pm 0.0$ \\
139	Bal.\ accuracy & L19 & 0\% & $14.0 \pm 4.0$ \\
140	\bottomrule
141	\end{tabular}}
142	\end{table}
143	
144	\paragraph{QwQ-32B (Qwen).} The results decompose the metric disagreement into two components. (A)~The crossing-rate shallow-layer preference is label-independent: 100\% of random-label repeats still select layers L0--L7, confirming that this bias reflects representation geometry (shallow-layer cosine distance compression; \cref{app:cosine_volatility}) rather than any property of the safety labels. The CR-composite inherits this bias (80\% shallow). (B)~Threshold-based metrics (precision, inverse FPR) select deep layers only with real safety labels; under random labels, selections scatter across the full layer range (mean L34--L36, high variance). The full metric disagreement (L4 vs.\ L63, a 59-layer gap) is the superposition of a geometric artifact on the crossing-rate side and a real safety signal on the threshold-based side.
145	
146	\paragraph{R1-8B (Llama).} The Llama-based model shows stronger label dependence: crossing rate scatters from L0 to mean L$10.7 \pm 4.8$ under random labels (0\% shallow), unlike QwQ-32B where it retains shallow preference. Threshold-based metrics degenerate entirely: precision and inverse FPR select L0 in all 10 repeats with zero variance, indicating random labels destroy discriminative signal rather than merely redistributing it. The real-CP disagreement (L0 vs.\ L23, a 23-layer gap) vanishes completely under random labels.
147	
148	\paragraph{Cross-architecture summary.} The metric disagreement requires genuine safety labels in both architectures, but the mechanism differs: in QwQ-32B, crossing-rate shallow preference reflects representation geometry (label-independent cosine compression), while in R1-8B even crossing-rate layer selection is label-dependent. The geometric component of the crossing-rate bias is thus Qwen-specific rather than a universal property of transformer representations.
149	
150	\section{Representation Compression Analysis}
151	\label{app:cosine_volatility}
152	
153	We measure step-to-step cosine distance at CR-composite (shallow) vs.\ threshold-based (deep) layers across all models to characterize the compression mechanism underlying the crossing rate bias (\cref{tab:cosine_volatility}).
154	
155	\begin{table}[htbp]
156	\centering
157	\small
158	\caption{Step-to-step cosine distance at CR-composite (shallow) and threshold-based (deep) layers. Shallow layers produce highly compressed representations (1.4--2.7$\times$ smaller inter-step distances).}
159	\label{tab:cosine_volatility}
160	\resizebox{\columnwidth}{!}{%
161	\begin{tabular}{llcc}
162	\toprule
163	\textbf{Model} & \textbf{Layer (type)} & \textbf{Mean} & \textbf{Std} \\
164	\midrule
165	R1-8B & L2 (CR-comp.) & 0.186 & 0.097 \\
166	 & L14 (thresh.) & 0.411 & 0.143 \\[2pt]
167	OT-7B & L2 (CR-comp.) & 0.077 & 0.080 \\
168	 & L16 (thresh.) & 0.206 & 0.091 \\[2pt]
169	QwQ-32B & L2 (CR-comp.) & 0.037 & 0.064 \\
170	 & L63 (thresh.) & 0.084 & 0.056 \\[2pt]
171	R1-32B & L10 (CR-comp.) & 0.067 & 0.050 \\
172	 & L63 (thresh.) & 0.092 & 0.076 \\
173	\bottomrule
174	\end{tabular}}
175	\end{table}
176	
177	Shallow layers produce highly compressed representations: consecutive steps cluster within small cosine distances (0.04--0.19), while deep-layer representations spread more widely (0.09--0.41). Inter-step distances at shallow layers are 1.4--2.7$\times$ smaller than at deep layers across all models. A linear probe operating in this compressed space sits near the noise floor, where minor numerical fluctuations produce spurious threshold crossings that inflate crossing rate independently of discriminative power. Deep layers produce well-separated representations where crossings correspond to genuine semantic transitions.
178	
179	\paragraph{Cross-dataset evidence.}
180	To assess whether this geometric precondition generalizes beyond HarmThoughts, we compute the same shallow/deep volatility ratio on AdvBench~\citep{advbench} traces using R1-8B. The deep-layer mean cosine distance (0.442) is $1.67\times$ the shallow-layer mean (0.265), consistent with the 1.4--2.7$\times$ range observed across all four models on HarmThoughts (\cref{tab:cosine_volatility}). This confirms that the representational compression underlying metric-induced layer selection bias is not dataset-specific and does not depend on CP annotations.
181	
182	\subsection{AdvBench Boundary Condition}
183	\label{app:advbench_cp}
184	
185	We analyze R1-8B behavior on 388 substantive-response AdvBench~\citep{advbench} traces (of 520 total) to characterize a boundary condition for the CP framework (\cref{tab:advbench_boundary}).
186	
187	\begin{table}[htbp]
188	\centering
189	\small
190	\caption{R1-8B behavior on AdvBench adversarial prompts (388 substantive-response traces of 520 total). CP${=}0$ indicates the model produces harmful content from the first reasoning step without prior safety deliberation.}
191	\label{tab:advbench_boundary}
192	\resizebox{\columnwidth}{!}{%
193	\begin{tabular}{lc}
194	\toprule
195	\textbf{Metric} & \textbf{Value} \\
196	\midrule
197	Jailbreak rate & 13.4\% \\
198	CP${=}0$ (among JB) & 90.4\% \\
199	Mean CP position (among JB) & 1.4 steps \\
200	\bottomrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "994b4d1f-889a-4000-bdd3-ba0d14c93780",
  "isSidechain": true,
  "promptId": "ef604098-550a-4d3f-9fa7-47752021e2dc",
  "agentId": "a846c1c041db9ae79",
  "type": "user",
  "uuid": "f05b7246-2f9c-43a9-a24b-11d6ede13b96",
  "sourceToolAssistantUUID": "994b4d1f-889a-4000-bdd3-ba0d14c93780",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-22T09:50:43.243Z_

Now let me read the rest of the appendix selectively to understand the nested CV, ensemble, and other key details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f05b7246-2f9c-43a9-a24b-11d6ede13b96",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQ9k4JmMj3xVzUVwoeQ",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "08dec6bc-b373-4139-a477-624c8f50999a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YGk1o3Cv2qr512AqoEJhEo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6155,
      "cache_read_input_tokens": 46132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6155,
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

_source line 33 · 2026-05-22T09:50:45.190Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JsU7Ya5W4CCokc9G2EDhfd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
  "offset": 200,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08dec6bc-b373-4139-a477-624c8f50999a",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQ9k4JmMj3xVzUVwoeQ",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "7c4e39cb-521f-4513-a8d8-ecee6ebd42ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YGk1o3Cv2qr512AqoEJhEo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6155,
      "cache_read_input_tokens": 46132,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6155
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 152,
          "cache_read_input_tokens": 46132,
          "cache_creation_input_tokens": 6155,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6155,
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

_source line 34 · 2026-05-22T09:50:45.199Z_

<details><summary>↩ Tool result · `toolu_01JsU7Ya5W4CCokc9G2EDhfd`</summary>

```text
200	\bottomrule
201	\end{tabular}}
202	\end{table}
203	
204	Adversarial prompts designed to bypass safety mechanisms (e.g., GCG suffixes) cause the model to skip safety deliberation entirely: 90.4\% of jailbroken traces have CP${=}0$, meaning the model commits to harmful generation from the first reasoning step. This contrasts with HarmThoughts, where non-adversarial prompts trigger extended safety deliberation before commitment (mean relative CP position ${\approx}0.7$). The CP framework is most informative when prompts elicit deliberation that can be monitored; adversarial prompts that circumvent deliberation represent a boundary condition where commitment detection is vacuous. The geometric compression evidence (\cref{tab:cosine_volatility}; volatility ratio $1.67\times$) remains valid because it measures representational properties independent of CP annotations.
205	
206	\section{Holm-Bonferroni Step-Down Correction}
207	\label{app:holm_bonferroni}
208	
209	\cref{tab:holm_bonferroni} reports the full test battery used to assess hidden-state superiority over text probes. Because balanced accuracy, precision, and FPR share the same confusion matrix, the three per-model metrics are correlated; the effective number of independent comparisons is four (one per model). We report both the conservative 12-test correction and the 4-test model-level correction: both yield the same outcome (all tests pass at $\alpha{=}0.05$). Under 4-test HB, the tightest threshold falls on R1-8B FPR ($p{=}0.044$, rank-4 threshold $\alpha/1{=}0.050$), which still passes. Tests are ranked by $p$-value; each test $i$ (rank $i$ of $m$) must satisfy $p_i < \alpha / (m - i + 1)$ under the step-down procedure.
210	
211	\begin{table}[htbp]
212	\centering
213	\small
214	\caption{Holm-Bonferroni step-down correction for 12 tests (4 models $\times$ 3 correlated metrics). Each test uses a two-sided null-centered bootstrap (10{,}000 resamples) on trace-level metric differences (HS minus text). All 12 pass at $\alpha{=}0.05$; a 4-test model-level correction (one per model, using the worst $p$-value) also passes.}
215	\label{tab:holm_bonferroni}
216	\setlength{\tabcolsep}{4pt}
217	\resizebox{\columnwidth}{!}{%
218	\begin{tabular}{clllcc}
219	\toprule
220	\textbf{Rank} & \textbf{Model} & \textbf{Metric} & \textbf{$p$-val} & \textbf{Thresh.} & \textbf{Pass} \\
221	\midrule
222	1  & R1-8B  & Precision & $<$0.001 & 0.0042 & \checkmark \\
223	2  & OT-7B  & Bal.\ Acc. & $<$0.001 & 0.0045 & \checkmark \\
224	3  & OT-7B  & Precision & $<$0.001 & 0.0050 & \checkmark \\
225	4  & OT-7B  & FPR & $<$0.001 & 0.0056 & \checkmark \\
226	5  & QwQ-32B & Bal.\ Acc. & $<$0.001 & 0.0063 & \checkmark \\
227	6  & QwQ-32B & Precision & $<$0.001 & 0.0071 & \checkmark \\
228	7  & R1-32B & Bal.\ Acc. & $<$0.001 & 0.0083 & \checkmark \\
229	8  & R1-32B & Precision & $<$0.001 & 0.0100 & \checkmark \\
230	9  & QwQ-32B & FPR & 0.004 & 0.0125 & \checkmark \\
231	10 & R1-8B  & Bal.\ Acc. & 0.005 & 0.0167 & \checkmark \\
232	11 & R1-32B & FPR & 0.007 & 0.0250 & \checkmark \\
233	12 & R1-8B  & FPR & 0.044 & 0.0500 & \checkmark \\
234	\bottomrule
235	\end{tabular}}
236	\end{table}
237	
238	The weakest test (rank 12, R1-8B FPR, $p{=}0.044$) passes its threshold ($\alpha/1 = 0.05$) with margin. The ordering reveals that OT-7B produces the strongest HS-text separation (ranks 2--4), while R1-8B FPR is the least significant despite R1-8B's precision gap (+20.1pp at $W{=}3$). This reflects R1-8B's already-low text FPR (11.8\%), which leaves less room for HS improvement on this metric.
239	
240	\paragraph{Exact sign-flip permutation test validation.} As an independent check on bootstrap significance for the small-sample 32B models, we run exact sign-flip permutation tests on all six 32B comparisons, enumerating all $2^n$ sign permutations ($2^{19}{=}524{,}288$ for QwQ-32B, $2^{20}{=}1{,}048{,}576$ for R1-32B). All six tests reject the null at $\alpha{=}0.05$: QwQ-32B (bal\_acc $p{<}0.001$, precision $p{=}0.003$, FPR $p{<}0.001$); R1-32B (bal\_acc $p{=}0.008$, precision $p{<}0.001$, FPR $p{=}0.004$). The permutation $p$-values are consistent with the bootstrap values in \cref{tab:holm_bonferroni} and confirm that the conclusions are not artifacts of distributional assumptions at small $n$.
241	
242	
243	\section{Window Size Ablation Details}
244	\label{app:window_ablation}
245	
246	\cref{tab:window_full} reports the complete window size ablation across all models and seven window sizes. The main text (\cref{sec:temporal}) presents R1-8B results; here we provide the full data. \cref{fig:window_ablation} visualizes the monotonic improvement on R1-8B: precision rises from 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$) while FPR drops from 9.65\% to 4.8\%.
247	
248	\begin{figure}[htbp]
249	\centering
250	\includegraphics[width=\columnwidth]{figures/fig2_temporal_improvement.pdf}
251	\caption{Temporal window effect on R1-8B HS probe (L14). Precision: 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$); FPR: 9.65\% to 4.8\%.}
252	\label{fig:window_ablation}
253	\end{figure}
254	
255	\begin{table}[htbp]
256	\centering
257	\small
258	\caption{Window size ablation (step-level metrics): balanced accuracy, precision, pre-CP FPR, coverage ($K{=}1$), and mean detection lead across all models.}
259	\label{tab:window_full}
260	\resizebox{\columnwidth}{!}{%
261	\begin{tabular}{llccccc}
262	\toprule
263	Model & $W$ & Bal.\ Acc. & Precision & FPR$_{\text{step}}$ & Coverage & Lead \\
264	\midrule
265	\multirow{7}{*}{R1-8B}
266	 & 1  & 77.8 & 69.3 & 9.65 & 72.1 & 13.8 \\
267	 & 3  & 79.0 & 72.3 & 8.50 & 69.8 & 12.1 \\
268	 & 5  & 78.1 & 72.6 & 8.09 & 65.1 & 8.3 \\
269	 & 10 & 79.3 & 74.3 & 7.61 & 55.8 & 10.0 \\
270	 & 15 & 80.2 & 77.7 & 6.39 & 51.2 & 7.2 \\
271	 & 20 & 80.7 & 78.6 & 6.12 & 53.5 & 7.4 \\
272	 & 25 & 81.0 & 82.2 & 4.83 & 48.8 & 8.1 \\
273	\midrule
274	\multirow{7}{*}{OT-7B}
275	 & 1  & 68.2 & 42.8 & 12.0 & 53.2 & 16.1 \\
276	 & 3  & \textbf{68.8} & 46.6 & 10.0 & 53.2 & 21.6 \\
277	 & 5  & 68.1 & 46.4 & 9.9 & 53.2 & 21.7 \\
278	 & 10 & 66.5 & 46.9 & 8.6 & 48.9 & 25.0 \\
279	 & 15 & 66.4 & 48.8 & 7.7 & 44.7 & 39.6 \\
280	 & 20 & 66.0 & \textbf{49.4} & \textbf{7.5} & 48.9 & 17.9 \\
281	 & 25 & 65.9 & 48.9 & 8.0 & 51.1 & 28.3 \\
282	\midrule
283	\multirow{7}{*}{R1-32B}
284	 & 1  & 71.8 & 54.9 & 32.03 & 80.0 & 12.9 \\
285	 & 3  & 72.5 & 56.0 & 30.64 & 80.0 & 11.4 \\
286	 & 5  & 73.1 & 57.5 & 28.41 & 75.0 & 11.1 \\
287	 & 10 & 73.7 & 60.9 & 23.40 & 70.0 & 10.8 \\
288	 & 15 & 72.1 & 59.1 & 24.51 & 70.0 & 10.9 \\
289	 & 20 & 69.6 & 56.3 & 26.18 & 65.0 & 9.6 \\
290	 & 25 & 70.3 & 56.6 & 26.46 & 70.0 & 10.7 \\
291	\midrule
292	\multirow{7}{*}{QwQ-32B}
293	 & 1  & 73.0 & 54.4 & 22.76 & 79.0 & 19.7 \\
294	 & 3  & 74.5 & 56.5 & 21.41 & 73.7 & 20.6 \\
295	 & 5  & 76.1 & 57.3 & 21.68 & 73.7 & 20.1 \\
296	 & 10 & 74.7 & 57.1 & 20.73 & 73.7 & 18.4 \\
297	 & 15 & 74.1 & 58.2 & 19.11 & 68.4 & 15.8 \\
298	 & 20 & 75.4 & 60.2 & 17.89 & 63.2 & 15.8 \\
299	 & 25 & 76.2 & 61.8 & 16.94 & 57.9 & 14.9 \\
300	\bottomrule
301	\end{tabular}}%
302	\end{table}
303	
304	Key cross-model patterns emerge from the window ablation:
305	
306	\paragraph{R1-8B} shows a general upward trend in balanced accuracy from 77.8\% ($W{=}1$) to 81.0\% ($W{=}25$), gaining +3.2pp overall with a slight dip at $W{=}5$ (78.1\%). Precision improves sharply (+12.9pp) and step-level FPR halves (9.65\% to 4.83\%). Coverage trades off against quality, dropping from 72.1\% to 48.8\%.
307	
308	\paragraph{OT-7B} exhibits a split temporal pattern at layer 16: balanced accuracy peaks at $W{=}3$ (68.8\%) and declines at larger windows ($-$2.9pp by $W{=}25$), while precision and FPR continue improving. Precision rises from 42.8\% ($W{=}1$) to 49.4\% ($W{=}20$), and FPR drops from 12.0\% to 7.5\% over the same range. The split indicates that larger windows reduce false alarms and sharpen positive predictions even as overall classification accuracy degrades. Lead times are shorter than old layer-0 estimates (16.1--39.6 steps) due to the threshold-based layer selection (\cref{app:ot7b_details}). OT-7B text probes improve monotonically across all metrics (\cref{app:ot7b_details}), so the accuracy saturation is specific to HS probes on this model.
309	
310	\paragraph{R1-32B} exhibits a non-monotonic pattern: balanced accuracy peaks at $W{=}10$ (73.7\%) and then declines, falling below the $W{=}1$ baseline by $W{=}20$ (69.6\%). The optimal window for R1-32B is $W{=}10$, which achieves the lowest FPR (23.40\%) and highest precision (60.9\%). The accuracy degradation at large windows likely reflects overfitting on the smaller dataset ($n{=}100$).
311	
312	\paragraph{QwQ-32B} shows a broadly increasing trend with local non-monotonicity: balanced accuracy peaks at $W{=}5$ (76.1\%), dips at $W{=}10$--$15$, then recovers to 76.2\% at $W{=}25$. Precision and FPR improve monotonically with larger windows (54.4\% to 61.8\% precision; 22.76\% to 16.94\% FPR). QwQ-32B produces substantially longer lead times than R1-8B and R1-32B (19.7 steps at $W{=}1$, 14.9 at $W{=}25$), though OT-7B's lead times are longer still.
313	
314	\paragraph{Universal trends.} Across all models: (1) larger windows reduce coverage as the smoothed probe fires less frequently; (2) HS FPR generally decreases with window size; (3) lead time is model-dependent. The primary cross-model difference is whether balanced accuracy improves broadly (R1-8B, QwQ-32B), peaks sharply at an intermediate window (R1-32B at $W{=}10$), or peaks very early (OT-7B at $W{=}3$). Each model uses its validation-selected window in the main text.
315	
316	\subsection{Text Probe Window Ablation}
317	\label{app:text_window}
318	
319	\cref{tab:text_window} reports the complete text probe window sweep on R1-8B and confirms that temporal context benefits text probes even more strongly than HS probes.
320	
321	\begin{table}[htbp]
322	\centering
323	\caption{Text probe window ablation on R1-8B (step-level metrics). Text probes gain +12.0pp accuracy from $W{=}1$ to $W{=}25$, compared to +3.2pp for HS probes over the same range. The larger marginal gain for text probes reflects their weaker single-step baseline.}
324	\label{tab:text_window}
325	\resizebox{\columnwidth}{!}{%
326	\begin{tabular}{lcccc}
327	\toprule
328	$W$ & Bal. Acc. & Precision & FPR & Coverage \\
329	\midrule
330	 1  & 64.7 & 41.6 & 25.8 & 95.4 \\
331	 3  & 66.9 & 44.8 & 23.1 & 90.7 \\
332	 5  & 69.2 & 48.5 & 20.4 & 84.9 \\
333	 10 & 72.1 & 54.3 & 16.7 & 74.4 \\
334	 15 & 74.3 & 58.9 & 14.2 & 67.4 \\
335	 20 & 75.8 & 62.1 & 12.5 & 62.8 \\
336	 25 & 76.7 & 64.8 & 11.8 & 58.1 \\
337	\bottomrule
338	\end{tabular}}
339	\end{table}
340	
341	Text probes show monotonic improvement across all window sizes without the plateau observed in HS probes (which saturate around $W{=}15$). The absolute FPR reduction ($-$14.0pp) is nearly three times the HS reduction ($-$4.8pp), and accuracy gains (+12.0pp vs.\ +3.2pp) are four times larger. This asymmetry supports the interpretation that temporal context is the primary factor in commitment detection: text features, which encode less information per step, benefit proportionally more from observing the multi-step progression.
342	
343	
344	\section{OpenThinker-7B Detailed Results}
345	\label{app:ot7b_details}
346	
347	OpenThinker-7B (OT-7B) is trained with STILL~\cite{still} on Qwen2.5-7B to produce a 7B reasoning model with a different training paradigm from the R1-distilled models. We report the full layer sweep and text probe window ablation.
348	
349	\paragraph{Layer sweep.}
350	
351	\begin{table}[htbp]
352	\centering
353	\small
354	\caption{OT-7B layer sweep. Score = balanced accuracy $\times$ crossing rate. Layer 16 (57\% depth) is selected after correction; it achieves the highest balanced accuracy among transformer layers.}
355	\label{tab:ot7b_layer_sweep}
356	\setlength{\tabcolsep}{4pt}
357	\resizebox{\columnwidth}{!}{%
358	\begin{tabular}{lcccc}
359	\toprule
360	Layer & Depth & Bal.\ Acc. & Cross.\ Rate & Score \\
361	\midrule
362	0 (embed.) & 0 & 66.7 & 53.2 & 35.5 \\
363	4 & 14 & 66.3 & 40.4 & 26.8 \\
364	8 & 29 & 66.4 & 25.5 & 17.0 \\
365	12 & 43 & 67.5 & 31.9 & 21.6 \\
366	16 & 57 & 68.2 & 31.9 & 21.8 \\
367	20 & 71 & 65.5 & 31.9 & 20.9 \\
368	24 & 86 & 66.9 & 29.8 & 19.9 \\
369	27 & 96 & 63.0 & 31.9 & 20.1 \\
370	\bottomrule
371	\end{tabular}}
372	\end{table}
373	
374	After correction of a layer selection bug, layer 16 (57\% depth) is selected. It achieves the highest balanced accuracy (68.2\%) among transformer layers under the 70/30 split used here; under the canonical 60/20/20 split, BA selects L2 (7\% depth; \cref{tab:ba_layer_results}). Layer 0 (embedding) has a higher crossing rate (53.2\% vs.\ 31.9\%) but lower accuracy.
375	
376	\paragraph{Text probe window ablation.}
377	
378	\begin{table}[htbp]
379	\centering
380	\small
381	\caption{OT-7B text probe window ablation (step-level). Text probes improve monotonically with larger $W$, contrasting with the HS probes on this model which peak at $W{=}3$.}
382	\label{tab:ot7b_text_window}
383	\resizebox{\columnwidth}{!}{%
384	\begin{tabular}{lcccc}
385	\toprule
386	$W$ & Bal. Acc. & Precision & FPR & Coverage \\
387	\midrule
388	 1  & 58.1 & 24.5 & 34.5 & 63.8 \\
389	 3  & 57.9 & 25.4 & 27.1 & 74.5 \\
390	 5  & 56.9 & 24.7 & 25.5 & 70.2 \\
391	 10 & 58.3 & 27.0 & 22.2 & 70.2 \\
392	 15 & 58.9 & 28.3 & 20.0 & 66.0 \\
393	 20 & 60.9 & 31.6 & 17.6 & 66.0 \\
394	 25 & 61.4 & 32.9 & 16.1 & 66.0 \\
395	\bottomrule
396	\end{tabular}}
397	\end{table}
398	
399	OT-7B text probes improve monotonically from $W{=}1$ to $W{=}25$ (+3.3pp accuracy, +8.5pp precision, $-$18.4pp FPR), consistent with the R1-8B pattern. OT-7B HS probes show a split pattern: balanced accuracy peaks at $W{=}3$ and declines, while precision and FPR continue improving (\cref{tab:window_full}). The text-HS contrast is therefore metric-dependent rather than a blanket modality difference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c4e39cb-521f-4513-a8d8-ecee6ebd42ad",
  "isSidechain": true,
  "promptId": "ef604098-550a-4d3f-9fa7-47752021e2dc",
  "agentId": "a846c1c041db9ae79",
  "type": "user",
  "uuid": "8a168767-ae0e-4bd9-90e9-e0d653a0fe49",
  "sourceToolAssistantUUID": "7c4e39cb-521f-4513-a8d8-ecee6ebd42ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-22T09:50:48.755Z_

I now have a thorough understanding of the paper. Let me also check the ensemble results and nested CV details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a168767-ae0e-4bd9-90e9-e0d653a0fe49",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQA6iH6C8p5McCLUZam",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "ff913e92-5eee-43d9-8f4f-5417cd3260a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159GizSVB7o1Ufhms8AuCwt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6278,
      "cache_read_input_tokens": 52287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6278,
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

_source line 36 · 2026-05-22T09:50:51.751Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Hqg1apcXboWhK3jhD5a9fW`</summary>

```json
{
  "pattern": "\\\\begin\\{table\\}.*ensemble|\\\\label\\{tab:ensemble\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": true,
  "context": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff913e92-5eee-43d9-8f4f-5417cd3260a7",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQA6iH6C8p5McCLUZam",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "866beb39-5db9-4686-8240-b9847fc4aa64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159GizSVB7o1Ufhms8AuCwt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6278,
      "cache_read_input_tokens": 52287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6278,
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

_source line 37 · 2026-05-22T09:50:51.772Z_

<details><summary>↩ Tool result · `toolu_01Hqg1apcXboWhK3jhD5a9fW`</summary>

```text
1269-
1270-\begin{table}[htbp]
1271-\centering
1272-\small
1273-\caption{Multi-metric layer ensemble vs.\ best single metric and text baseline. Ensemble trains probes at 3 threshold-based metric-selected layers and averages probabilities. $\Delta$Ens--Best: ensemble minus best single metric (negative = ensemble slightly lower). All Ens--Text differences are significant ($p \leq 0.002$, permutation test). No Ens--Best difference is significant ($p > 0.27$).}
1274:\label{tab:ensemble}
1275-\resizebox{\columnwidth}{!}{%
1276-\begin{tabular}{lcccc}
1277-\toprule
1278-\textbf{Model} & \textbf{Ens Prec} & \textbf{Best Single} & $\Delta$ & \textbf{Ens$-$Text} \\
1279-\midrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "866beb39-5db9-4686-8240-b9847fc4aa64",
  "isSidechain": true,
  "promptId": "ef604098-550a-4d3f-9fa7-47752021e2dc",
  "agentId": "a846c1c041db9ae79",
  "type": "user",
  "uuid": "15848f8d-4298-4392-9a6f-53ae661a39c2",
  "sourceToolAssistantUUID": "866beb39-5db9-4686-8240-b9847fc4aa64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-22T09:50:52.616Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01EEy7PLrBbQM4SQvDXhjxYU`</summary>

```json
{
  "pattern": "nested.*CV|Nested.*CV|nested_cv",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": true,
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15848f8d-4298-4392-9a6f-53ae661a39c2",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQA6iH6C8p5McCLUZam",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "c1db2382-a4f4-41a1-b657-f3a316fe348c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159GizSVB7o1Ufhms8AuCwt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6278,
      "cache_read_input_tokens": 52287,
      "output_tokens": 359,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6278
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 359,
          "cache_read_input_tokens": 52287,
          "cache_creation_input_tokens": 6278,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6278,
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

_source line 39 · 2026-05-22T09:50:52.644Z_

<details><summary>↩ Tool result · `toolu_01EEy7PLrBbQM4SQvDXhjxYU`</summary>

```text
404-\section{GRU Training Details}
405-\label{app:gru_details}
406-
407:GRU results serve as supplementary evidence under a different training protocol (70/30 split); direct comparison with the main logistic regression pipeline (60/20/20 nested CV) is not intended.
408-
409-\paragraph{Data split.} GRU experiments use a 70/30 train/test split to maximize training data for the sequential model, differing from the main 60/20/20 protocol used for logistic regression probes. Within the 70\% training portion, we hold out 10\% of total traces as a validation set for early stopping (effective 60/10/30 split). The validation set is used only for early stopping and is not included in reported test metrics, so there is no information leakage.
410-
--
990-[Omitted long context line]
991-
992-\paragraph{Effective degrees of freedom.}
993:[Omitted long matching line]
994-
995-\subsection{Nested Cross-Validation}
996:\label{app:nested_cv}
997-
998:The holdout estimates in \cref{tab:hs_vs_text} select layer and window on the validation fold, then evaluate on a fixed test set. To rule out hyperparameter overfitting, we run nested 5-fold cross-validation on both 7--8B models: the outer fold holds out test data; the inner loop selects (layer, $W$) on the remaining four folds. \cref{tab:nested_cv} reports per-fold precision differences.
999-
1000-\begin{table}[htbp]
1001-\centering
1002-\small
1003:\caption{Nested 5-fold CV: per-fold HS$-$text precision difference (pp). Layer and $W$ selected independently per fold. All 10/10 folds favor HS.}
1004:\label{tab:nested_cv}
1005-\setlength{\tabcolsep}{4pt}
1006-\resizebox{\columnwidth}{!}{%
1007-\begin{tabular}{lcccccccc}
--
1017-\end{flushleft}
1018-\end{table}
1019-
1020:[Omitted long matching line]
1021-
1022-\paragraph{Formal test.} A one-sided Wilcoxon signed-rank test on the 5-fold $\Delta$precision (HS$-$text) rejects $H_0{:}\;\Delta{=}0$ for both models ($W{=}15$, $p{=}0.031$; the minimum achievable $p$-value at $n{=}5$). Layer selection entropy across folds is $H{=}1.37$ bits for R1-8B (normalized 0.59; dominated by L12 in 3/5 folds) and $H{=}1.92$ bits for OT-7B (normalized 0.83; L21--L27), indicating moderately stable layer selection for R1-8B and higher variability for OT-7B.
1023-
--
1228-
1229-\paragraph{Layer autocorrelation.} Adjacent transformer layers produce highly correlated probe scores: for R1-8B, the median Pearson $r$ between layers $\ell$ and $\ell{\pm}1$ exceeds 0.95. Using a lag-1 autocorrelation estimate~\citep{efron1993bootstrap}, the effective number of independent layers is ${\sim}$8--12 per model (vs.\ 28--64 nominal).
1230-
1231:[Omitted long matching line]
1232-
1233:[Omitted long matching line]
1234-
1235-[Omitted long context line]
1236-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1db2382-a4f4-41a1-b657-f3a316fe348c",
  "isSidechain": true,
  "promptId": "ef604098-550a-4d3f-9fa7-47752021e2dc",
  "agentId": "a846c1c041db9ae79",
  "type": "user",
  "uuid": "8bffec5a-b39d-4530-a2c8-89c536bde5a2",
  "sourceToolAssistantUUID": "c1db2382-a4f4-41a1-b657-f3a316fe348c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-22T09:50:55.671Z_

Now I have a comprehensive understanding of the paper. Let me also quickly count the total references in the bib file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bffec5a-b39d-4530-a2c8-89c536bde5a2",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQAddt1DJdHS1WCAMwy",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "6961471a-d945-48ad-874a-d8dac1f67fb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BgQTv3wu5tLrEzZSwVj6W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1601,
      "cache_read_input_tokens": 58565,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1601,
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

_source line 41 · 2026-05-22T09:50:56.244Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01E4h8ZGQRPrqAbPLWjeFLvg`</summary>

```json
{
  "pattern": "^@",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/references.bib",
  "output_mode": "count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6961471a-d945-48ad-874a-d8dac1f67fb9",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQAddt1DJdHS1WCAMwy",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "3286854e-5af8-4e72-89c1-b16bf4f305e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BgQTv3wu5tLrEzZSwVj6W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1601,
      "cache_read_input_tokens": 58565,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1601
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 58565,
          "cache_creation_input_tokens": 1601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1601,
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

_source line 42 · 2026-05-22T09:50:56.253Z_

<details><summary>↩ Tool result · `toolu_01E4h8ZGQRPrqAbPLWjeFLvg`</summary>

```text
85

Found 0 total occurrences across 0 files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3286854e-5af8-4e72-89c1-b16bf4f305e9",
  "isSidechain": true,
  "promptId": "ef604098-550a-4d3f-9fa7-47752021e2dc",
  "agentId": "a846c1c041db9ae79",
  "type": "user",
  "uuid": "1b16b01d-005a-4784-9e6b-15521e911aeb",
  "sourceToolAssistantUUID": "3286854e-5af8-4e72-89c1-b16bf4f305e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-22T09:50:59.300Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0175oHe9D7ePf9dFvebrsZX5`</summary>

```json
{
  "command": "grep -c '^@' /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/references.bib",
  "description": "Count bib entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b16b01d-005a-4784-9e6b-15521e911aeb",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQAuDVvwFT6ZWfimhav",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "ff638c9f-aae8-4ab6-bafc-8153e79a75de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CtZQerE2RdT4y4qo8hEjNu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 178,
      "cache_read_input_tokens": 60166,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 178
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 116,
          "cache_read_input_tokens": 60166,
          "cache_creation_input_tokens": 178,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 178,
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

_source line 44 · 2026-05-22T09:50:59.871Z_

<details><summary>↩ Tool result · `toolu_0175oHe9D7ePf9dFvebrsZX5`</summary>

```text
85
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff638c9f-aae8-4ab6-bafc-8153e79a75de",
  "isSidechain": true,
  "promptId": "ef604098-550a-4d3f-9fa7-47752021e2dc",
  "agentId": "a846c1c041db9ae79",
  "type": "user",
  "uuid": "041e4cfc-2c88-4912-bf4b-1da95ccc5079",
  "sourceToolAssistantUUID": "ff638c9f-aae8-4ab6-bafc-8153e79a75de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-22T09:51:03.385Z_

Now let me check the actual number of \cite commands vs unique references to see what's actually cited in the paper body.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "041e4cfc-2c88-4912-bf4b-1da95ccc5079",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQBAaisCR78ZJmxRMiQ",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "4b4c891a-88d6-4959-8478-a9d3ebf895c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPDytPd7U5VLwrYmDjAmcW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 232,
      "cache_read_input_tokens": 60344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 232,
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

_source line 46 · 2026-05-22T09:51:05.489Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012rjF4yYM1Ztx7CySghb31R`</summary>

```json
{
  "command": "grep -ohP '\\\\\\\\cite[tp]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/*.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex | sed 's/\\\\cite[tp]\\?{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u | wc -l",
  "description": "Count unique cited references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b4c891a-88d6-4959-8478-a9d3ebf895c3",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQBAaisCR78ZJmxRMiQ",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "2874514d-3231-4f7c-8bc5-ade23f22253d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPDytPd7U5VLwrYmDjAmcW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 232,
      "cache_read_input_tokens": 60344,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 232
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 239,
          "cache_read_input_tokens": 60344,
          "cache_creation_input_tokens": 232,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 232,
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

_source line 47 · 2026-05-22T09:51:05.581Z_

<details><summary>↩ Tool result · `toolu_012rjF4yYM1Ztx7CySghb31R`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2874514d-3231-4f7c-8bc5-ade23f22253d",
  "isSidechain": true,
  "promptId": "ef604098-550a-4d3f-9fa7-47752021e2dc",
  "agentId": "a846c1c041db9ae79",
  "type": "user",
  "uuid": "7c49a705-1def-4b64-a4e9-8745dde5b57a",
  "sourceToolAssistantUUID": "2874514d-3231-4f7c-8bc5-ade23f22253d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-22T09:51:08.925Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01W1fvzgB1ihKZDgAFpRMhen`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/*.tex | grep -oP '\\\\cite[tp]?\\{[^}]+\\}' | sed 's/\\\\cite[tp]\\?{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
  "description": "List all unique cited references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c49a705-1def-4b64-a4e9-8745dde5b57a",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQBavC9nJR7wZrpw8QD",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "508d19ad-0a21-41e6-ac60-75994f69e661",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016z2mZXeGvuYYU8H3F4v8F1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 252,
      "cache_read_input_tokens": 60576,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 252
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 60576,
          "cache_creation_input_tokens": 252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 252,
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

_source line 49 · 2026-05-22T09:51:08.993Z_

<details><summary>↩ Tool result · `toolu_01W1fvzgB1ihKZDgAFpRMhen`</summary>

```text
adams2007bayesian
advbench
ahrend2026safer_traces
alain2017understanding
alvarez2026transport_geometry
arditi2024refusal
azaria2023internal
baker2025monitoring
belinkov2019analysis
belinkov2022probing
belrose2023leace
belrose2023tunedlens
boxo2025linear_probes
burns2023discovering
carpenter2000bootstrap
chan2025probing
chen2025unfaithful
chia2025probing_subspaces
chrabaszcz2026monitoring
cohen1988statistical
conneau2018probing
damirchi2026truth
deepseekr1
diciccio1996bootstrap
efron1993bootstrap
elazar2021amnesic
geiger2023causal
gelman2013garden
hagendorff2026lrm_jailbreak
harmthoughts
hcot2025
hewitt2019control
hu2026refusal_dynamics
jawahar2019bert
jiang2025hiddendetect
joad2026refusal_multi
kadali2025internal
kaya2019shallow
korbak2025cot_monitorability
levinstein2024liedetector
li2023iti
mao2025selfjailbreak_reasoning
marks2024geometry
meyoyan2026bertology
openthinker
page1954cusum
pais2026linear_probe_scaling
pimentel2020information
qi2025shallow_alignment
qwq
ravfogel2020null
ravfogel2022rlace
rcs2026
reimers2019sentence
rogers2020primer
safedream2026
safeint2025
saferemind
safeswitch
safethink
schulz2025roadmap
selfjailbreak
siren
still
templeton2024scaling
tenney2019bert
trajguard
turner2023activation
turpin2023language
vitel2025layer
voita2020information
wang2020minilm
wang2024e5mistral
wang2025lrmsafety
wollschlager2025geometry
xiang2025guardreasoner
xiao2023cpack
yin2025refusal_cliff
zhao2025harmfulness
zhao2026safeprobing
zhou2020bert
zhou2024alignment
zhou2025ghost
zou2023representation
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "508d19ad-0a21-41e6-ac60-75994f69e661",
  "isSidechain": true,
  "promptId": "ef604098-550a-4d3f-9fa7-47752021e2dc",
  "agentId": "a846c1c041db9ae79",
  "type": "user",
  "uuid": "586be47e-3e8e-4a40-a686-de7f47689bff",
  "sourceToolAssistantUUID": "508d19ad-0a21-41e6-ac60-75994f69e661",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-22T09:51:12.383Z_

84 unique citations in total. The task summary said "14 citations" which was incorrect -- the paper actually cites 84 unique references. Let me now write the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "586be47e-3e8e-4a40-a686-de7f47689bff",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQBqVYToGcGooTG17r3",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "db5bbb2c-c578-4b9e-b0a9-3c0cd177a995",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SiUNoFpeMnoWSfF2LMkdz8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 752,
      "cache_read_input_tokens": 60828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 752,
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

_source line 51 · 2026-05-22T09:51:12.921Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EYUFxEUKsGUEpUkDP7P9ai`</summary>

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
  "parentUuid": "db5bbb2c-c578-4b9e-b0a9-3c0cd177a995",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQBqVYToGcGooTG17r3",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "22044eff-7c55-4d56-914f-c2a561edb7a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SiUNoFpeMnoWSfF2LMkdz8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 752,
      "cache_read_input_tokens": 60828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 752,
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

_source line 52 · 2026-05-22T09:51:12.924Z_

<details><summary>↩ Tool result · `toolu_01EYUFxEUKsGUEpUkDP7P9ai`</summary>

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
  "parentUuid": "22044eff-7c55-4d56-914f-c2a561edb7a5",
  "isSidechain": true,
  "promptId": "ef604098-550a-4d3f-9fa7-47752021e2dc",
  "agentId": "a846c1c041db9ae79",
  "type": "user",
  "uuid": "d780156c-ce75-47e5-a39b-0310a08cff08",
  "sourceToolAssistantUUID": "22044eff-7c55-4d56-914f-c2a561edb7a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-22T09:52:52.037Z_



Here is my review.

---

## Reviewer 2: Novelty/Contribution and Related Work Positioning

### Paper Summary

This paper investigates safety commitment point (CP) detection in reasoning LLMs that self-jailbreak during extended chain-of-thought. The central claim is methodological: the choice of layer selection metric (crossing-rate composite vs. threshold-based metrics) can qualitatively reverse whether hidden-state probes show an advantage over text probes. At threshold-selected deep layers, HS probes gain +15-22pp precision over a 384d sentence encoder baseline across 4 models; at crossing-rate-selected shallow layers, the advantage vanishes for 32B models. The paper also reports that the HS advantage is conditional on text encoder quality (diminishes with 1024d encoders) and partially overlaps with temporal position. Seven alternative detection methods all fail.

---

### 1. Novelty Assessment

**Layer selection bias finding.** The observation that different metrics select different layers is a natural consequence of well-known properties in the probing literature. That layer-wise information distribution is non-uniform (Tenney et al., 2019; Jawahar et al., 2019), that shallow layers compress representations differently from deep layers, and that probe conclusions depend on the layer chosen are all established facts. The paper's own Related Work section acknowledges this: "Prior work has noted metric sensitivity in probing (Belinkov, 2022); our contribution is demonstrating a qualitative reversal in a safety-critical application." This is an honest framing. The specific demonstration -- that a crossing-rate composite systematically biases toward shallow layers due to cosine compression, producing a qualitative reversal from significant to non-significant -- is a useful empirical observation rather than a conceptual advance. The mechanism (compressed representations produce noisy threshold crossings) is intuitive and could have been predicted a priori. The paper partially acknowledges this ("cosine compression at shallow layers predicts a priori that any threshold-crossing metric exhibits shallow-layer bias"). This undermines the novelty claim: if the result is predictable from known principles, the contribution is demonstrating the severity of the problem in a specific domain, not discovering a new phenomenon.

**Methodological contribution vs. empirical study.** This is fundamentally an empirical study with a methodological observation. The paper does not propose a new method for layer selection, a new detection architecture, or a new theoretical framework. The three-level defense (report multiple metrics, multi-metric audit, ensemble) is practical advice rather than a technical contribution, and the ensemble itself is acknowledged as needing cross-validated confirmation. For EMNLP, empirical studies can be valuable, but they need to either reveal genuinely surprising findings or be exceptionally thorough. The finding that "if you pick the wrong metric you get the wrong answer" is cautionary rather than surprising.

**"First modality comparison" claim.** The claim of "first modality comparison (hidden-state vs. text) for reasoning-model safety detection" is narrow and appears accurate given the cited literature. However, the comparison is against a 384d MiniLM encoder -- a deliberately weak baseline. When upgraded to BGE-large (1024d), the advantage collapses to 1/4 models passing HB correction. The paper is commendably transparent about this, but it significantly weakens the practical significance of the modality comparison. The headline result (HS beats text) is conditioned on using a weak text encoder, which makes the "first comparison" less impactful.

**"First systematic evaluation across 4 models" claim.** Stretching the claim across "2 architectures, 2 training methods, and 2 scales" is somewhat generous: 3 of 4 models are Qwen-based, and the two 32B models have n=19-20 test traces with all conclusions marked exploratory. The cross-architecture evidence rests on a single Llama model (R1-8B). This is acknowledged in Limitations but still featured prominently in the Abstract.

---

### 2. Related Work Gaps

**Correction to task description.** The task summary states "only 14 references" -- this is incorrect. The paper actually cites 84 unique references, which is more than adequate for EMNLP. The Related Work section is dense and well-organized across four paragraphs covering safety in reasoning models, hidden-state safety detection, probing methodology, and alternative detection approaches.

**Coverage assessment.** The related work is comprehensive and well-positioned:
- Probing methodology: Hewitt & Manning (2019) control tasks are cited and adopted. Pimentel et al. (2020) information-theoretic probing is cited. Voita (2020) MDL probing is cited. Ravfogel et al. (2020, 2022) INLP/RLACE are cited. Belinkov (2022) survey is the anchor reference. This coverage is thorough.
- Representation engineering: RepE (Zou et al., 2023) is cited and evaluated as a baseline. Activation steering (Turner et al., 2023; Li et al., 2023 ITI) is cited. Arditi et al. (2024) refusal directions, Wollschlager et al. (2025) geometry of refusal, Zhao et al. (2025) harmfulness/refusal separation are all cited.
- Concurrent work: Six concurrent papers are cited (Alvarez 2026, Chrabaszcz 2026, Damirchi 2026, Meyoyan 2026, Pais 2026, Chan 2025), showing awareness of the rapidly evolving field.
- Safety monitoring systems: Eight monitoring systems are cited (TrajGuard, SafeSwitch, SIREN, SafeDream, HiddenDetect, SafeInt, RCS, hidden-state forensics).

**Distinction from HarmThoughts.** The paper uses HarmThoughts as its primary dataset and cites it appropriately. The distinction is clear: HarmThoughts provides the dataset with step-level CP annotations; this paper contributes the probing methodology analysis and modality comparison. The paper does not claim to create a new dataset or new annotations.

**Missing references (minor).** The paper could cite work on probe selectivity beyond control tasks (e.g., Hewitt & Liang's structural probe work, Belinkov & Glass 2019 is cited but the broader "what do probes actually tell us" debate involving Saphra, Voita, Zhang & Bowman 2018 on whether probing results are meaningful). However, given the 84 citations already present, this is a minor gap rather than a structural deficiency.

---

### 3. Framing Critique

**"Primary contribution" framing.** The paper frames metric-induced layer selection bias as the "primary contribution" and the HS vs. text comparison as secondary. This is the correct framing given the results (the HS advantage is conditional on encoder quality and position), but it creates a tension: the primary contribution is essentially a methodological warning ("be careful which metric you use for layer selection"), while the secondary contribution (HS beats text) comes with so many caveats that it is hard to extract a clear takeaway.

**Negative results.** Seven alternative methods failing is presented as Contribution 3. The negative results are well-documented but their informational value is uneven. BOCPD/CUSUM failing on gradual transitions is expected (these are designed for abrupt change points). Mahalanobis distance failing follows from the TrajGuard reproduction. CCS temporal misalignment and RepE model-dependence are more informative. Cross-model transfer failing is genuinely useful. The negative results are better understood as systematic due diligence rather than a standalone contribution.

**Honesty of presentation.** One genuine strength is the paper's transparency about limitations. The evidence gradient (cross-validated / significant / exploratory), the dagger notation for sample-limited results, the acknowledgment that 32B results are descriptive rather than confirmatory, and the frank admission that FPR remains 11-50% -- all of these reflect scientific integrity that exceeds the norm.

---

### 4. Excitement Level

This paper would generate moderate discussion among researchers working specifically on hidden-state probing for safety, but limited excitement in the broader EMNLP community. The core finding -- that metric choice matters for layer selection -- is a useful cautionary tale but does not open major new research directions. The practical impact is limited because: (a) the HS advantage over text depends on using a weak text encoder; (b) FPR of 11-50% precludes deployment; (c) 3/4 models share Qwen architecture; and (d) the three-level defense is practical advice, not a new method.

The paper does not propose a solution to the layer selection problem beyond "use multiple metrics and average," which, while sensible, is not a contribution that would reshape how the field thinks about probing.

---

### 5. Specific Strengths

**S1. Exceptional statistical rigor.** The paper's statistical methodology is among the strongest I have seen in this subfield. Nested 5-fold CV, BCa bootstrap with trace-level clustering, Holm-Bonferroni correction, exact permutation tests for small samples, power analysis with MDE reporting, random-label controls, split-half validation -- this is a model for how empirical probing studies should be conducted.

**S2. Transparent evidence grading.** The three-tier evidence classification (cross-validated, significant, exploratory) with consistent dagger notation is exemplary. The paper does not oversell its 32B results, which is rare.

**S3. Thorough ablations.** Window size ablation across 7 values, encoder robustness across 3 encoders, capacity control via PCA and random projection, position residualization with linear and quadratic terms, control task selectivity -- the experimental thoroughness is impressive.

**S4. Well-documented negative results.** Seven alternative methods are systematically evaluated and their failure modes are characterized (gradual transitions, near-zero separation, model dependence, temporal misalignment). This provides genuine value by narrowing the space of viable approaches.

**S5. Practical mitigation proposal.** The three-level defense (report multiple metrics, multi-metric audit, ensemble) is actionable and could be adopted by future probing studies, even if it is not a deep technical contribution.

---

### 6. Specific Weaknesses

**W1. Limited novelty of the core finding.** The layer selection bias is a predictable consequence of known representation properties. The paper itself admits the bias "predicts a priori" from cosine compression. The demonstration of severity in the safety domain adds applied value but does not constitute a conceptual advance. The finding is closer to "debugging a specific metric combination" than to "discovering a new phenomenon."

**W2. Weak text baseline undermines the modality comparison.** The headline HS advantage (+15-22pp) is against a 384d MiniLM encoder. Against BGE-large (1024d), only 1/4 models survives HB correction. This is honestly reported, but the Abstract and Introduction lead with the 384d result, creating a misleading impression of robust HS superiority. The encoder-quality gradient (4/4 -> 2/4 -> 1/4 HB) actually suggests that with sufficiently strong text encoders, the HS advantage may vanish entirely -- which would make the modality comparison a null result.

**W3. Architecture diversity is insufficient.** 3/4 models are Qwen-based. The random-label control reveals that the geometric component of crossing-rate bias is "Qwen-specific rather than a universal property of transformer representations." This is a significant caveat for generalizability. A single Llama model (R1-8B) provides the only cross-architecture evidence. Claims of systematic evaluation across architectures should be tempered.

**W4. Sample sizes at 32B are critically small.** n=19-20 test traces for both 32B models. The paper marks these as exploratory, but they still appear in all main tables and figures, and the Abstract mentions "preliminary +15 to +19pp at 32B." The MDE at 80% power is 8.6-9.5pp, meaning effects smaller than this are undetectable. The QwQ-32B position baseline achieves higher BA than HS (0.832 vs. 0.796), and R1-32B achieves significance only at W=1 with 25% coverage. These 32B results are too preliminary to feature in the main paper's narrative as substantially as they do.

**W5. No actionable detection system.** FPR of 11-50% and the "retrospective classification, not online detection" framing means the paper characterizes rather than solves the problem. The three-level defense addresses layer selection, not the underlying detection challenge. This limits practical impact.

---

### 7. Questions for Authors

**Q1.** The encoder-quality gradient (4/4 HB at 384d, 2/4 at E5-Mistral-4096d->384d, 1/4 at BGE-1024d) strongly suggests the HS advantage is an artifact of comparing against a weak baseline. Have you evaluated against a state-of-the-art text encoder at native dimensionality (e.g., GTE-Qwen2-7B at 3584d, or an LLM-based encoder without PCA reduction)? If the HS advantage disappears entirely against strong encoders, the modality comparison section should be reframed.

**Q2.** The paper positions the crossing-rate composite as a problematic metric, but who uses this metric? Is there a published paper that actually selects layers using bal_acc x crossing_rate for safety probing? If this is a hypothetical concern rather than a correction of existing practice, the contribution is weaker. The paper should clarify whether it is correcting an actual methodological error in the literature or preemptively warning against a potential one.

**Q3.** Given that the geometric component of the crossing-rate bias is Qwen-specific (per your own random-label controls), how confident are you that the layer selection bias finding generalizes to other architectures? The Llama model shows a different decomposition (label-dependent crossing-rate selection). Could you test on at least one more non-Qwen architecture (e.g., Gemma, Phi) to strengthen the generalizability claim?

---

### 8. Scores

| Criterion | Score | Justification |
|-----------|-------|---------------|
| **Soundness** | 4 / 5 | Statistical methodology is exemplary. The evidence gradient is transparent. Minor concerns about 32B sample sizes affecting narrative weight. |
| **Excitement** | 2 / 5 | The core finding (metric choice affects layer selection) is unsurprising given prior probing literature. The HS advantage is conditional on a weak baseline. Does not open clear new research directions. |
| **Reproducibility** | 4 / 5 | All hyperparameters reported, code release promised, statistical tests fully specified. Minor concern: HarmThoughts annotations lack formal IAA. |
| **Overall** | 3.0 / 5 | Findings-level paper. The statistical rigor and transparency are genuinely strong, but the novelty is limited to demonstrating severity of a predictable problem in a specific domain. The modality comparison is undermined by the encoder-quality gradient. Insufficient architecture diversity (3/4 Qwen) limits generalizability. |

**Recommendation: Borderline Findings (3.0).** The paper is methodologically sound and commendably honest about its limitations, but the core contribution -- that a specific composite metric biases layer selection toward shallow layers -- is a predictable consequence of known representation properties rather than a novel insight. The modality comparison result (HS beats text) is conditioned on using a weak text encoder and partially collapses with stronger encoders, reducing practical significance. The paper would benefit from: (a) testing on more diverse architectures, (b) evaluating against state-of-the-art text encoders, and (c) reframing the contribution as an applied methodology study rather than claiming "first systematic evaluation." As written, it meets the bar for Findings but not Main.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d780156c-ce75-47e5-a39b-0310a08cff08",
  "isSidechain": true,
  "agentId": "a846c1c041db9ae79",
  "requestId": "req_011CbHQC9AvAAt7kh7P5Jn6V",
  "attributionAgent": "general-purpose",
  "attributionSkill": "review",
  "type": "assistant",
  "uuid": "1d194ebb-26c5-4ddc-a56c-fd36a42cd24f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "8f0c6665-94b6-4b25-a480-e39988e7cc27",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZNF7XqHV9mJZ3aVgKpr7C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 752,
      "cache_read_input_tokens": 61580,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 752,
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
