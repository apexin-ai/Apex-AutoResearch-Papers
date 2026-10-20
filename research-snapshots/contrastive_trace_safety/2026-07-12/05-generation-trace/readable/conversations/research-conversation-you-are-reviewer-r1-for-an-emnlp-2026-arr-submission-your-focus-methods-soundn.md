# Research conversation: You are Reviewer R1 for an EMNLP 2026 ARR submission. Your focus: **Methods soundness and Experimental rigor**. ## Venue

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-acee8d8337f321220.jsonl`
- **Structured JSON:** [`04e9cbeafe7af772e60d.json`](../../sessions/04/04e9cbeafe7af772e60d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-21T22:10:28.599Z_

You are Reviewer R1 for an EMNLP 2026 ARR submission. Your focus: **Methods soundness and Experimental rigor**.

## Venue calibration
- EMNLP 2026 via ARR. Overall Assessment 1-5 half-point scale. 4 = Main conference acceptance (~21% accept rate). 3 = Findings. 2 = resubmit.
- Dimensions: Soundness (1-5), Excitement (1-5), Reproducibility (1-5).

## Paper summary
**Title**: "What Detects Safety Commitment in Reasoning Models? A Systematic Evaluation of Probe-Based Monitoring Methods"

The paper studies "self-jailbreak" in reasoning LLMs — where safety reasoning and harmful execution interleave in CoT, culminating in a "commitment point" (CP) after which safety reasoning permanently ceases. They evaluate detection methods across 4 models (R1-8B Llama, OT-7B Qwen STILL-trained, R1-32B Qwen R1-distilled, QwQ-32B Qwen native) × 7 methods (static LR on hidden states, temporal LR on HS windows W=1-25, text probes via MiniLM-L6, GRU sequence model, Mahalanobis distance, BOCPD/CUSUM, cross-model transfer) × 5 metrics (balanced accuracy, precision, pre-commitment FPR, safe-trace FPR, detection lead time).

**Key claims:**
1. Layer selection methodology is a critical researcher degree of freedom — `bal_acc × crossing_rate` biases toward shallow layers at 32B scale, masking HS advantage.
2. HS probes outperform text probes at correctly selected layers (12/12 Holm-Bonferroni, precision +15-24pp), robust at 7-8B, model-specific at 32B.
3. Temporal context universally improves text probes (4/4) and benefits HS probes (3/4, R1-32B exception due to dimensionality).
4. Six alternative detection paradigms fail.
5. Practical deployment limited: safe-trace FPR 39-50% for most model-method combos, only OT-7B HS meets <20% threshold.

**Paper structure**: 11 pages total (8 main + Limitations + references + 3 appendix sections with tables). Tables 1-14 across main text and appendices.

## Key experimental details from the paper

**Table 1** (Layer Selection): bal_acc×CR selects L0-L10 (shallow); precision/inv_FPR/composite select L16-L63 (deep). Clean separation.

**Table 2** (HS vs Text, best W per model): All 4 models show HS advantage: ΔBA +8.2 to +18.7pp, ΔPrec +15.4 to +23.6pp, ΔFPR -7.4 to -17.1pp. 12/12 HB pass.

**Table 3** (Uniform W=3): 3/4 pass HB. R1-32B drops to 0/3 at W=3 (dimensionality: 51,200 × 3 features for n=20).

**Table 4** (Temporal windows): Text improves universally (W=1→best: +3-12pp BA). HS 3/4 (R1-32B peaks at W=1, declines). 

**Table 5** (Precision vs W): Precision increases monotonically for R1-8B (0.693→0.822) and QwQ (0.544→0.618). OT-7B peaks at W=3 (0.466).

**Table 6** (Safe-trace FPR): Only OT-7B HS static (11.1%) meets <20%. R1-8B 39%, QwQ 50%, R1-32B 23.9%.

**Table 7** (HB step-down): 12/12 pass. Weakest: R1-8B FPR p=0.044 at threshold 0.050.

**Table 8** (Mahalanobis): Max separation 0.20 (QwQ). All 4 fail.

**Table 9** (Cross-transfer): Best off-diagonal 0.673 (R1-32B→QwQ). Near chance.

**Table 10** (Timing): No universal HS timing advantage. R1-32B +12.5 at 25% coverage. QwQ -0.8 (HS later). R1-8B ~0.

**Table 11** (CV ensemble): Ensemble significantly outperforms text (p<0.002). Marginally below best single metric on R1-8B (0.558 vs 0.597).

**Tables 12-14** (Appendix): HS vs text precision, GRU vs LR on 32B, BOCPD/CUSUM.

**Sample sizes**: R1-8B n=43, OT-7B n=47 (228 total), R1-32B n=20, QwQ n=19-20.

## Your review task

Evaluate the following dimensions in detail:

### 1. Methodological Soundness
- Is the task definition (binary classification at each step: pre-CP vs post-CP) well-motivated? Any issues with this framing?
- LOO-CV for layer selection — appropriate given sample sizes?
- 10,000 bootstrap resamples + Holm-Bonferroni correction — is this statistical framework appropriate?
- The "best W per model" approach (Table 2) vs uniform W (Table 3) — is the paper honest about this researcher degree of freedom?
- Balanced class weights in all probes — appropriate?
- MiniLM-L6 as text baseline — is this a fair comparison?

### 2. Experimental Completeness
- Does the 4×7×5 evaluation matrix cover the important combinations?
- Are there missing baselines or ablations?
- Is the negative results section (4.6) thorough?
- Cross-model transfer (Table 9) — is the PCA projection approach reasonable?
- Are the appendix experiments adequate?

### 3. Statistical Rigor
- 12/12 HB — convincing? Note weakest tests: R1-8B FPR p=0.044, R1-32B FPR p=0.007.
- Sample sizes (n=19-47) — sufficient for the claims made?
- CV fold variance 0.02-0.07 — does this indicate stability?
- The 16/16 BA-layer robustness test — does this address circularity?

### 4. Weaknesses
- R1-32B only significant at W=1 (drops to 0/3 HB at W=3)
- Safe-trace FPR 39-50% for most combos
- No universal HS timing advantage
- 3/4 models Qwen-based
- n=20 for 32B models
- Position baseline exceeds HS on QwQ (0.746 vs 0.740)

### 5. Strengths
- Systematic evaluation breadth (4×7×5)
- Layer selection sensitivity analysis
- Honest about limitations (deployment, timing, model-specificity)
- 12/12 HB statistical validation
- Strong negative results section

## Output format

Provide your review as:
```
## R1 Review: Methods and Experiments

### Summary
[2-3 sentences]

### Strengths
[Numbered list, 4-6 items]

### Weaknesses  
[Numbered list, 4-6 items]

### Questions for Authors
[Numbered list, 3-5 items]

### Minor Issues
[Numbered list if any]

### Scores
- Soundness: X/5
- Excitement: X/5
- Reproducibility: X/5
- Overall: X/5
- Confidence: X/5

### Meta-assessment
[1 paragraph: what would need to change for a higher score?]
```

Be rigorous and calibrated. A 4.0 overall means top ~21% — reserve it for genuinely strong work. Most solid-but-incremental papers land at 3.0-3.5.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b1899cf7-50e7-4ba4-a982-bccf7d2835cb",
  "agentId": "acee8d8337f321220",
  "type": "user",
  "uuid": "57c3fa26-9844-424f-b945-d0d8624d2f29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T22:10:28.604Z_

```json
{
  "parentUuid": "57c3fa26-9844-424f-b945-d0d8624d2f29",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
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
  "uuid": "bc7bc0f4-464c-4d02-b359-509f316e00ab",
  "timestamp": "2026-05-21T22:10:28.604Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-21T22:10:30.914Z_



I'll conduct a thorough review by first reading the paper and key experimental details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc7bc0f4-464c-4d02-b359-509f316e00ab",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
  "requestId": "req_011CbGUkriqodZj1ZQyusy4A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76c92e42-83ec-40a7-b9ef-b3ed1f6b77d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q56kPf5au6dU5fnv6dxaNZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18060,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18060,
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

_source line 4 · 2026-05-21T22:10:32.121Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011ftzc6z1qUxpkNsWySfzd7`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76c92e42-83ec-40a7-b9ef-b3ed1f6b77d6",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
  "requestId": "req_011CbGUkriqodZj1ZQyusy4A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01fe16fe-5dc6-41d1-b1f2-bd64ad5e1d89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q56kPf5au6dU5fnv6dxaNZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18060,
      "cache_read_input_tokens": 0,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18060
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 106,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18060,
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

_source line 5 · 2026-05-21T22:10:32.126Z_

<details><summary>↩ Tool result · `toolu_011ftzc6z1qUxpkNsWySfzd7`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01fe16fe-5dc6-41d1-b1f2-bd64ad5e1d89",
  "isSidechain": true,
  "promptId": "b1899cf7-50e7-4ba4-a982-bccf7d2835cb",
  "agentId": "acee8d8337f321220",
  "type": "user",
  "uuid": "798dfd1a-4f94-4cad-bd94-62cb4d8e54ac",
  "sourceToolAssistantUUID": "01fe16fe-5dc6-41d1-b1f2-bd64ad5e1d89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-21T22:10:34.591Z_



I'll read the paper and key files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "798dfd1a-4f94-4cad-bd94-62cb4d8e54ac",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
  "requestId": "req_011CbGUm7yN8v8k7U5bBk3mH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1af05aba-2744-466c-a3b7-44dc9adcb040",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017JSXpAkHwqArZ4ASLTj1g3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1288,
      "cache_read_input_tokens": 18060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1288,
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

_source line 7 · 2026-05-21T22:10:36.957Z_

<details open><summary>🔧 Tool call — Read · `toolu_016mQDwWqZXERkavPkKhwxeZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1af05aba-2744-466c-a3b7-44dc9adcb040",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
  "requestId": "req_011CbGUm7yN8v8k7U5bBk3mH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b293d7c4-1a7f-41b1-8e26-ce0a6de1f67b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017JSXpAkHwqArZ4ASLTj1g3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1288,
      "cache_read_input_tokens": 18060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1288,
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

_source line 8 · 2026-05-21T22:10:36.966Z_

<details><summary>↩ Tool result · `toolu_016mQDwWqZXERkavPkKhwxeZ`</summary>

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
  "parentUuid": "b293d7c4-1a7f-41b1-8e26-ce0a6de1f67b",
  "isSidechain": true,
  "promptId": "b1899cf7-50e7-4ba4-a982-bccf7d2835cb",
  "agentId": "acee8d8337f321220",
  "type": "user",
  "uuid": "d46b73d3-9109-47f3-af6b-344473152b85",
  "sourceToolAssistantUUID": "b293d7c4-1a7f-41b1-8e26-ce0a6de1f67b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T22:10:37.454Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01QKD9NnHNv3gZ1K3SGy4Kfr`</summary>

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
  "parentUuid": "d46b73d3-9109-47f3-af6b-344473152b85",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
  "requestId": "req_011CbGUm7yN8v8k7U5bBk3mH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9ef69da-5235-4235-a9b4-e2662f2e53c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017JSXpAkHwqArZ4ASLTj1g3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1288,
      "cache_read_input_tokens": 18060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1288,
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

_source line 10 · 2026-05-21T22:10:37.490Z_

<details><summary>↩ Tool result · `toolu_01QKD9NnHNv3gZ1K3SGy4Kfr`</summary>

```text
docs/paper/_drafts/advbench_contingency_templates.tex
docs/paper/main.tex
docs/paper/sections/limitations.tex
docs/paper/sections/method.tex
docs/paper/sections/abstract.tex
docs/paper/sections/introduction.tex
docs/paper/sections/related_work.tex
docs/paper/sections/appendix.tex
docs/paper/sections/discussion.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9ef69da-5235-4235-a9b4-e2662f2e53c1",
  "isSidechain": true,
  "promptId": "b1899cf7-50e7-4ba4-a982-bccf7d2835cb",
  "agentId": "acee8d8337f321220",
  "type": "user",
  "uuid": "8c34f805-ded2-480c-9474-316c8ee50c39",
  "sourceToolAssistantUUID": "a9ef69da-5235-4235-a9b4-e2662f2e53c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T22:10:38.021Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LYjbDTDcW2FearsLqTYLLD`</summary>

```json
{
  "project": "contrastive_trace_safety",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c34f805-ded2-480c-9474-316c8ee50c39",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
  "requestId": "req_011CbGUm7yN8v8k7U5bBk3mH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5cd1402-5d8a-4eb3-8e97-782374a8efc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017JSXpAkHwqArZ4ASLTj1g3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1288,
      "cache_read_input_tokens": 18060,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1288
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 299,
          "cache_read_input_tokens": 18060,
          "cache_creation_input_tokens": 1288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1288,
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

_source line 12 · 2026-05-21T22:10:38.041Z_

<details><summary>↩ Tool result · `toolu_01LYjbDTDcW2FearsLqTYLLD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **advbench_llm_cp_annotation** (killed): —\\n- **advbench_llm_cp_full** (killed): —\\n- **qwen3_cp_dryrun** (killed): —\\n\\n## 趋势\\n成功 27 / 负向 20 / 失败 1 / 共 55\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-15904: 无 GPU 信息\\n\\n## 告警\\n- advbench_r1_8b_full: 训练失败 — unknown\\n- advbench_llm_cp_annotation: 已被终止 — unknown\\n- advbench_llm_cp_full: 已被终止 — unknown\\n- qwen3_cp_dryrun: 已被终止 — unknown\\n- qwen3_cp_dryrun2: 已被终止 — unknown\\n- qwen3_cp_full: 已被终止 — unknown\\n- gpt4omini-cp-annotation: 已被终止 — unknown\\n- advbench_phase4_layer_sweep: 已被终止 — unknown\\n\", \"total_chars\": 630, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5cd1402-5d8a-4eb3-8e97-782374a8efc7",
  "isSidechain": true,
  "promptId": "b1899cf7-50e7-4ba4-a982-bccf7d2835cb",
  "agentId": "acee8d8337f321220",
  "type": "user",
  "uuid": "c4fd506d-8a4e-4e9a-9b74-1d14b9f8544e",
  "sourceToolAssistantUUID": "e5cd1402-5d8a-4eb3-8e97-782374a8efc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T22:10:40.386Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BxZmSZ6vxEKRbuegk9sJJo`</summary>

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
  "parentUuid": "c4fd506d-8a4e-4e9a-9b74-1d14b9f8544e",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
  "requestId": "req_011CbGUmZGPC4ozDHtqrBA2N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7d8fd2f-d1b8-4c4c-b038-67a89298a14b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyfPDeHmHQBoxSskthhfoc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 19348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1444,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 61,
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

_source line 14 · 2026-05-21T22:10:40.392Z_

<details><summary>↩ Tool result · `toolu_01BxZmSZ6vxEKRbuegk9sJJo`</summary>

```text
1	Reasoning models with chain-of-thought (CoT) can self-jailbreak: their reasoning traces transition from safe deliberation to committed harmful generation without adversarial input. We define the commitment point (CP) as the first reasoning step after which safety deliberation permanently ceases, and present a systematic empirical comparison of hidden-state (HS) vs.\ text probes for CP detection across four reasoning LLMs (3 Qwen-family, 1 Llama) on HarmThoughts. The comparison depends critically on which transformer layer is monitored, a known sensitivity in probing~\citep{belinkov2022probing} that we show is severe enough to qualitatively reverse conclusions in the safety domain: a crossing-rate composite metric selects L0 for R1-8B while threshold-based metrics select L14 (14-layer divergence); at 32B the divergence reaches 61 layers (exploratory$^\dagger$), reversing whether an HS advantage is observed. Threshold-based layer selection recovers HS precision gains of +15 to +22pp at 7--8B (cross-validated via nested CV) and preliminary +15 to +19pp at 32B (exploratory$^\dagger$, $n \leq 20$) against a 384d sentence encoder, but this advantage is conditional on partially correlated factors: it diminishes with stronger text encoders (4/4 HB at 384d $\to$ 1/4 at 1024d) and partially overlaps with temporal position. Seven alternative methods (change-point detection, geometric distance, representation engineering, cross-model transfer) all fail to match supervised probing. Metric-induced layer selection bias is the robust methodological finding; the empirical HS advantage is conditional on encoder quality, model scale, and position control.
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7d8fd2f-d1b8-4c4c-b038-67a89298a14b",
  "isSidechain": true,
  "promptId": "b1899cf7-50e7-4ba4-a982-bccf7d2835cb",
  "agentId": "acee8d8337f321220",
  "type": "user",
  "uuid": "af4698c5-25d7-48bd-8dbe-1077c177a52e",
  "sourceToolAssistantUUID": "e7d8fd2f-d1b8-4c4c-b038-67a89298a14b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T22:10:40.872Z_

<details open><summary>🔧 Tool call — Read · `toolu_018o3e8UCsp6kRoK6gvKiFZr`</summary>

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
  "parentUuid": "af4698c5-25d7-48bd-8dbe-1077c177a52e",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
  "requestId": "req_011CbGUmZGPC4ozDHtqrBA2N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ecd94d7-c77a-4a38-a364-e96903837c39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyfPDeHmHQBoxSskthhfoc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 19348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1444,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 61,
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

_source line 16 · 2026-05-21T22:10:40.877Z_

<details><summary>↩ Tool result · `toolu_018o3e8UCsp6kRoK6gvKiFZr`</summary>

```text
1	\section{Problem Setup and Methods}
2	\label{sec:method}
3	
4	\subsection{Safety Commitment Point}
5	\label{sec:commitment-point}
6	
7	When a reasoning model is jailbroken, its chain-of-thought (CoT) transitions from safety-aware deliberation to committed harmful generation. We define the \textbf{Safety Commitment Point} (CP) as the first reasoning step after which safety deliberation permanently ceases; traces with oscillating safety deliberation are resolved by taking the final irreversible transition. This binary formulation is a deliberate simplification; we discuss its limits in \cref{sec:limitations}. Steps before CP are \emph{pre-commitment} ($y_t = 0$); steps at or after CP are \emph{post-commitment} ($y_t = 1$). The classification task produces a score $s_t \in [0, 1]$ estimating whether the model has passed its CP by step $t$.
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
  "parentUuid": "5ecd94d7-c77a-4a38-a364-e96903837c39",
  "isSidechain": true,
  "promptId": "b1899cf7-50e7-4ba4-a982-bccf7d2835cb",
  "agentId": "acee8d8337f321220",
  "type": "user",
  "uuid": "2e5a5377-136c-4e48-9557-3ca47f23f88d",
  "sourceToolAssistantUUID": "5ecd94d7-c77a-4a38-a364-e96903837c39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T22:10:41.364Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ta9TBLtohceagv2uin7aSn`</summary>

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
  "parentUuid": "2e5a5377-136c-4e48-9557-3ca47f23f88d",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
  "requestId": "req_011CbGUmZGPC4ozDHtqrBA2N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec2f2846-5955-437c-91eb-01465388262f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyfPDeHmHQBoxSskthhfoc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 19348,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1444
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 239,
          "cache_read_input_tokens": 19348,
          "cache_creation_input_tokens": 1444,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1444,
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

_source line 18 · 2026-05-21T22:10:41.369Z_

<details><summary>↩ Tool result · `toolu_01Ta9TBLtohceagv2uin7aSn`</summary>

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
13	\cref{tab:layer_selection} shows that the crossing-rate composite metric (balanced accuracy $\times$ crossing rate) systematically selects shallow layers across all four models: L0 for R1-8B (full L0--L24 sweep; \cref{tab:r18b_full_layer}) and OT-7B, L2 (3\%) for QwQ-32B, and L10 (16\%) for R1-32B. The three threshold-based metrics (precision, inverse FPR, additive composite) share a common confusion matrix and empirically converge to the same deep layer, L63 (98\%) for both 32B models, consistent with their shared structure, though not mathematically guaranteed. Pure balanced accuracy, a threshold-free metric, selects layers that vary across data splits and models (7--98\% depth under 60/20/20; \cref{app:ba_layer_comparison}), itself demonstrating that layer selection is a consequential methodological choice. The mechanism is that shallow layers produce highly compressed representations with small inter-step margins: step-to-step cosine distances are 1.4--2.7$\times$ smaller than at deep layers across all models (\cref{app:cosine_volatility}). A linear probe in this compressed space operates near the noise floor, generating frequent threshold crossings that inflate crossing rate independently of discriminative power (\cref{sec:layer-sensitivity}).\looseness=-1
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
42	\subsection{HS vs.\ Text Comparison}\label{sec:hs-text}
43	
44	\begin{table}[t]
45	\centering
46	\small
47	\resizebox{\columnwidth}{!}{%
48	\begin{tabular}{llclrrlrc}
49	\toprule
50	\textbf{Model} & \textbf{Layer} & \textbf{Enc.} & $W$ & $\Delta$\textbf{BA} & $\Delta$\textbf{Prec} & \textbf{95\% CI} & $\Delta$\textbf{FPR} & \textbf{HB} \\
51	\midrule
52	R1-8B & L14 & 384d & 3 & +17.5 & +20.1 & [+12.4, +28.3] & $-$7.9 & \checkmark \\
53	 & & 1024d & & \multicolumn{1}{c}{--} & +5.8 & [$-$7.4, +19.5] & \multicolumn{1}{c}{--} & \\[2pt]
54	OT-7B & L16 & 384d & 3 & +10.7 & +21.9 & [+14.4, +29.6] & $-$17.1 & \checkmark \\
55	 & & 1024d & & \multicolumn{1}{c}{--} & +18.1 & [+8.4, +29.0] & \multicolumn{1}{c}{--} & \checkmark \\[2pt]
56	QwQ$^\dagger$ & L63 & 384d & 5 & +13.0 & +19.2 & [+9.3, +33.5] & $-$15.0 & \checkmark \\
57	 & & 1024d & & \multicolumn{1}{c}{--} & +9.4 & [$-$7.1, +27.7] & \multicolumn{1}{c}{--} & \\[2pt]
58	R1-32B$^\dagger$ & L63 & 384d & 1 & +18.7 & +15.4 & [+8.7, +22.6] & $-$14.6 & \checkmark \\
59	 & & 1024d & & \multicolumn{1}{c}{--} & +11.7 & [$-$0.2, +24.3] & \multicolumn{1}{c}{--} & \\
60	\bottomrule
61	\end{tabular}}
62	\caption{HS vs.\ text at threshold-based layers (LR probes, 60/20/20 split, 10{,}000 bootstrap resamples). Enc.: text encoder (384d = MiniLM-L6-v2, 1024d = BGE-large). $\Delta$: HS$-$text difference (pp); ``--'' = BA and FPR are not computed for the 1024d comparison because the 384d and 1024d encoders operate at different probe calibration points and do not share a decision threshold. HB: \checkmark{} = model-level test passes Holm-Bonferroni ($\alpha{=}0.05$); all 384d model-level tests pass. $^\dagger$\,Sample-limited ($n \leq 20$); 32B results are exploratory. 1024d: HB over 4 model-level precision tests.}
63	\label{tab:hs_vs_text}
64	\end{table}
65	
66	The HS advantage is encoder-conditional: against BGE-large (1024d), only OT-7B survives HB correction (\cref{app:encoder_robustness}). Multi-seed stability appears in \cref{app:multi_seed}. Against the 384d baseline, HS probes outperform text probes in all four models$^\dagger$ (\cref{tab:hs_vs_text}): cross-validated at 7--8B (OT-7B: +21.9pp precision, R1-8B: +20.1pp), significant but suggestive of position-competitiveness at QwQ-32B$^\dagger$ (+19.2pp), and exploratory at R1-32B$^\dagger$ (+15.4pp, pattern consistent with position mediation). R1-8B FPR is directionally consistent (5/5 seeds) but not robust ($p{=}0.044$, rank 12/12 in HB step-down; 1/5 seeds Bonferroni; \cref{app:multi_seed}). R1-32B passes 5/5 seeds but shows a pattern consistent with position mediation (residualized gap NS; \cref{app:position_residual}); QwQ-32B's position baseline is competitive (\cref{sec:32b-analysis}). Overall, 18/20 model-seed combinations pass full HB (\cref{app:multi_seed}). Control task selectivity confirms genuine safety signal: 11.1--16.8pp above chance (\cref{app:control}). A split-half analysis on OT-7B confirms internal validity (\cref{app:split_half}).\looseness=-1
67	
68	\paragraph{Capacity control.} PCA reduction of HS features to 384d (79--92\% variance retained) preserves the precision advantage across all four models$^\dagger$ (+16.8 to +23.1pp, all $p{<}0.012$, all HB). The control provides partial evidence against a pure capacity explanation. Random projection to 384d yields similar results ($\Delta$Prec +8.3 to +20.5pp; \cref{app:random_projection}), further weakening the capacity explanation. E5-Mistral-7B (4096d, PCA-reduced to 384d; \cref{app:e5_mistral}) yields intermediate results (2/4 HB), forming a monotonic encoder-quality gradient with MiniLM (4/4) and BGE-large (1/4).\looseness=-1
69	
70	\paragraph{Encoder robustness.} Against BGE-large~\citep{xiao2023cpack} (1024d), only OT-7B survives HB (1/4 precision); R1-8B shows adverse FPR direction (+1.2pp). This forms a monotonic encoder-quality gradient: MiniLM-384d (4/4 HB) $\to$ E5-Mistral-4096d$\to$384d (2/4) $\to$ BGE-large-1024d (1/4), with the precision advantage narrowing from +15--22pp to +6--12pp. The HS advantage is thus a function of text encoder capacity (\cref{fig:forest_precision}); layer selection (Contribution 1) is encoder-independent.\looseness=-1
71	
72	\paragraph{Position mediation.} Position ($t/T$) accounts for 9--20pp of balanced accuracy,\footnote{R1-32B's 20.4pp drop reflects $W{=}1$; at $W{\geq}3$, drops are 9--17pp.} but all models retain non-positional signal above chance (all $p{<}0.001$; \cref{app:position_residual}). Three of four models retain significant non-positional HS advantage (residualized gap +3.7 to +6.9pp, HB corrected); R1-32B's gap is +1.9pp ($p{=}0.914$, $n{=}20$), well below the MDE of ${\sim}$9pp and thus indistinguishable from zero at current power. Adding a quadratic position term $(t/T)^2$ does not change significance conclusions for the 7--8B models. However, QwQ-32B's advantage is fully absorbed by the quadratic term (\cref{tab:position_quadratic}), indicating a non-linear position component. Temporal windowing reduces position dependence (\cref{sec:temporal}).\looseness=-1
73	
74	\enlargethispage{7\baselineskip}
75	\paragraph{Caveats.} Nested 5-fold CV confirms the HS precision advantage for both 7--8B models (10/10 folds; \cref{app:nested_cv}), with shrinkage of 13--25\% relative to holdout estimates. OT-7B nested CV selects L21--27 vs.\ holdout L16 vs.\ CR-composite L0; the +21.9pp holdout estimate is an upper bound. R1-32B achieves significance only at $W{=}1$ with 25\% coverage; at $W{\geq}3$, dimensionality prevents significance. QwQ-32B HS lead time is negative ($-$1.2 to +1.9 steps). False alarm rates remain 11--50\%, so current methods characterize the phenomenon rather than constitute production detectors. Per-model details in \cref{sec:32b-analysis}.\looseness=-1
76	
77	\subsection{32B Model-Specific Analysis}\label{sec:32b-analysis}
78	
79	\paragraph{Exploratory 32B analysis.} Both 32B results are exploratory ($n{=}19$--$20$ precludes nested CV). LOO-CV and multi-seed analyses (\cref{app:layer_sweep,app:multi_seed}) provide partial robustness checks but do not substitute for independent validation. R1-32B and QwQ-32B share the Qwen-32B architecture but present opposite detection profiles (\cref{tab:32b_divergence}); training method is one plausible differentiator. Replication with $n{\geq}50$ traces is needed.\looseness=-1
80	
81	\begin{table}[t]
82	\centering
83	\small
84	\resizebox{\columnwidth}{!}{%
85	\begin{tabular}{lcccc}
86	\toprule
87	\textbf{Model} & \textbf{Cov.} & \textbf{Lead (steps)} & \textbf{HB} & \textbf{Pos.\ margin} \\
88	\midrule
89	R1-32B$^\dagger$ & 25\% & +11.7 to +13.3 & \checkmark{} ($W{=}1$) & +14.2pp \\
90	QwQ-32B$^\dagger$ & 74\% & $-$1.2 to +1.9 & \checkmark{} (all $W$) & $-$3.6pp \\
91	\bottomrule
92	\end{tabular}}
93	\caption{32B cross-model divergence ($\dagger$\,sample-limited, $n \leq 20$; MDE at 80\% power: 8.6--9.5pp, \cref{app:power_analysis}; all conclusions exploratory). R1-32B provides limited early identification with narrow coverage; QwQ-32B provides robust significance with poor lead time. HB: \checkmark{} = passes Holm-Bonferroni ($\alpha{=}0.05$). Pos.\ margin: HS BA minus position baseline.}
94	\label{tab:32b_divergence}
95	\end{table}
96	
97	R1-32B suggests commitment 11--13 steps early (+14.2pp over position baseline) but covers only 25\% of traces ($W{=}1$); the precision effect (+15.4pp, CI width 13.9pp) falls below MDE at 80\% power. QwQ-32B achieves significance at all window sizes with 74\% coverage but negative HS lead time; the precision effect (+19.2pp, CI width 24.2pp) exceeds MDE (8.6--9.5pp; \cref{app:power_analysis}) but the position baseline achieves higher BA (0.832 vs.\ 0.796), and the HS precision margin over position (+4.5pp, $p{=}0.133$; \cref{app:position_residual}) is not significant at $n{=}19$. The divergence suggests per-model validation is needed.\looseness=-1
98	
99	\subsection{Temporal Context}\label{sec:temporal}
100	
101	Temporal windowing ($W{>}1$) improves both modalities (\cref{fig:window_ablation}): at 7--8B, the modality advantage (+20.1 to +21.9pp) exceeds temporal improvement (+13pp). GRU models achieve comparable accuracy but higher FPR (\cref{tab:gru_multi_seeds,app:temporal_details}); an adaptive two-stage strategy offers marginal gains (\cref{app:two_stage}).\looseness=-1
102	
103	CP-aligned probe score trajectories (\cref{fig:trajectory} in Appendix) confirm sharper HS transitions at the commitment point, with OT-7B showing the clearest separation and R1-32B the weakest. A forest plot visualizing precision gaps across encoder conditions appears in \cref{fig:forest_precision}.\looseness=-1
104	
105	\subsection{Negative Results}\label{sec:negative}
106	
107	No alternative method consistently matches supervised probing (\cref{tab:negative}). BOCPD~\citep{adams2007bayesian}/CUSUM fail (0\% detection on 3/4 models); Mahalanobis yields near-zero separation; RepE~\citep{zou2023representation} is model-dependent (BA 0.756 vs.\ 0.559); MLP probes overfit; CCS misaligns temporally; cross-model transfer fails (\cref{app:negative_details}). The signal is directional, gradual, model-specific, and linearly separable, which excludes change-point, distance, transfer, and objective-alignment methods respectively.\looseness=-1
108	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec2f2846-5955-437c-91eb-01465388262f",
  "isSidechain": true,
  "promptId": "b1899cf7-50e7-4ba4-a982-bccf7d2835cb",
  "agentId": "acee8d8337f321220",
  "type": "user",
  "uuid": "38f4160d-b1da-435b-9778-c7c069cfac5f",
  "sourceToolAssistantUUID": "ec2f2846-5955-437c-91eb-01465388262f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T22:10:47.061Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SkC2CXHAwCsQre8AHP8qEY`</summary>

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
  "parentUuid": "38f4160d-b1da-435b-9778-c7c069cfac5f",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
  "requestId": "req_011CbGUmwgmRxCyY3W9Ns31y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04fad901-825c-40cf-941b-f09e55ba574d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LDaryb48kyjVFQHws6oTwW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8474,
      "cache_read_input_tokens": 20792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8474,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 20 · 2026-05-21T22:10:47.080Z_

<details><summary>↩ Tool result · `toolu_01SkC2CXHAwCsQre8AHP8qEY`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	Crossing rate reverses the central finding via shallow-layer compression (\cref{app:cosine_volatility,tab:r18b_full_layer}): its shallow preference is an artifact of cosine compression inflating threshold crossings, while threshold-based deep preference reflects genuine separability~\citep{tenney2019bert}; random-label controls confirm this distinction (\cref{app:random_cp}). C1 generalizes across all four models (cross-dataset: \cref{app:cosine_volatility}; split-half: \cref{app:split_half}); C2 is sample-dependent (7--8B cross-validated, 32B descriptive). Annotation noise (${<}2.5$pp BA change; \cref{tab:cp_perturbation}) does not threaten C1. The encoder-quality gradient narrows the HS advantage (384d to 1024d; \cref{app:position_residual}). Type~I risk from ${\sim}$2{,}240 configurations is bounded by the two-stage design and large effect sizes ($d$ 0.58--2.37; \cref{app:effective_tests}). \textbf{Practical mitigation.} A multi-metric audit (\cref{app:deployment_operating_points}) flags divergent conclusions when ${\geq}3$ metrics differ by ${>}20\%$ of depth. A three-layer ensemble eliminates pre-selection ($p \leq 0.002$; \cref{tab:ensemble}) but lacks cross-validation; this is diagnostic guidance, not a validated method.\looseness=-1
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04fad901-825c-40cf-941b-f09e55ba574d",
  "isSidechain": true,
  "promptId": "b1899cf7-50e7-4ba4-a982-bccf7d2835cb",
  "agentId": "acee8d8337f321220",
  "type": "user",
  "uuid": "ca840cb1-382a-4136-8221-9a5646ec9ac5",
  "sourceToolAssistantUUID": "04fad901-825c-40cf-941b-f09e55ba574d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T22:10:48.066Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AGbeinpaJmeSYPPkWsiG4v`</summary>

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
  "parentUuid": "ca840cb1-382a-4136-8221-9a5646ec9ac5",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
  "requestId": "req_011CbGUmwgmRxCyY3W9Ns31y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e652d418-bd99-4fd5-b0a9-9e62127a5594",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LDaryb48kyjVFQHws6oTwW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8474,
      "cache_read_input_tokens": 20792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8474,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 22 · 2026-05-21T22:10:48.071Z_

<details><summary>↩ Tool result · `toolu_01AGbeinpaJmeSYPPkWsiG4v`</summary>

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
  "parentUuid": "e652d418-bd99-4fd5-b0a9-9e62127a5594",
  "isSidechain": true,
  "promptId": "b1899cf7-50e7-4ba4-a982-bccf7d2835cb",
  "agentId": "acee8d8337f321220",
  "type": "user",
  "uuid": "60d27947-ac73-4f4f-aa92-37aaaebe0fb3",
  "sourceToolAssistantUUID": "e652d418-bd99-4fd5-b0a9-9e62127a5594",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T22:10:48.412Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FCmEUCFyZy37kZrvpZTYCv`</summary>

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
  "parentUuid": "60d27947-ac73-4f4f-aa92-37aaaebe0fb3",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
  "requestId": "req_011CbGUmwgmRxCyY3W9Ns31y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1834c836-e457-4a72-afda-a03d30f94f08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LDaryb48kyjVFQHws6oTwW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8474,
      "cache_read_input_tokens": 20792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8474,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 24 · 2026-05-21T22:10:48.416Z_

<details><summary>↩ Tool result · `toolu_01FCmEUCFyZy37kZrvpZTYCv`</summary>

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
37	\noindent These findings establish layer selection as a critical confound for hidden-state safety monitoring that future work must address.\looseness=-1
38	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1834c836-e457-4a72-afda-a03d30f94f08",
  "isSidechain": true,
  "promptId": "b1899cf7-50e7-4ba4-a982-bccf7d2835cb",
  "agentId": "acee8d8337f321220",
  "type": "user",
  "uuid": "6bc654e6-7243-4b3a-8a16-fda68bc372d2",
  "sourceToolAssistantUUID": "1834c836-e457-4a72-afda-a03d30f94f08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T22:10:53.849Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MuMnZPT7hPbd2iGDEGVTqC`</summary>

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
  "parentUuid": "6bc654e6-7243-4b3a-8a16-fda68bc372d2",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
  "requestId": "req_011CbGUnKk4kpw3UjSqktQUv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e689e222-793f-41a6-8076-dd1b6b65f4f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DVFB8EapvLrdXMCKHNajiS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3302,
      "cache_read_input_tokens": 29266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3302,
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

_source line 26 · 2026-05-21T22:10:54.197Z_

<details><summary>↩ Tool result · reported error · `toolu_01MuMnZPT7hPbd2iGDEGVTqC`</summary>

```text
File content (37324 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e689e222-793f-41a6-8076-dd1b6b65f4f7",
  "isSidechain": true,
  "promptId": "b1899cf7-50e7-4ba4-a982-bccf7d2835cb",
  "agentId": "acee8d8337f321220",
  "type": "user",
  "uuid": "5b170173-defb-4151-a32d-92fb55ab022d",
  "toolUseResult": "Error: File content (37324 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "e689e222-793f-41a6-8076-dd1b6b65f4f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T22:10:54.345Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BfcMQn63SyCXnVfwASPSG5`</summary>

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
  "parentUuid": "5b170173-defb-4151-a32d-92fb55ab022d",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
  "requestId": "req_011CbGUnKk4kpw3UjSqktQUv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ff63f8f-5b82-46ec-942e-9905faf7d07f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DVFB8EapvLrdXMCKHNajiS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3302,
      "cache_read_input_tokens": 29266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3302,
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

_source line 28 · 2026-05-21T22:10:54.350Z_

<details><summary>↩ Tool result · `toolu_01BfcMQn63SyCXnVfwASPSG5`</summary>

```text
1	\section{Related Work}\label{sec:related-work}
2	
3	\paragraph{Safety in Reasoning Models.}
4	Reasoning models introduce a qualitatively new failure mode: the model's own chain of thought can transition from safety-aware deliberation to harmful generation without adversarial input modification~\cite{wang2025lrmsafety}.
5	
6	\textit{Attack characterization.} Self-jailbreak has been documented with step-level annotations~\cite{harmthoughts}, with longer chains increasing circumvention probability~\cite{selfjailbreak}. H-CoT~\cite{hcot2025} shows reasoning chains can be externally hijacked. Unfaithful reasoning~\cite{chen2025unfaithful,turpin2023language} further motivates hidden-state monitoring that bypasses text. Safety-aligned models maintain refusal intentions during thinking but experience a sharp drop at output generation~\cite{yin2025refusal_cliff,hagendorff2026lrm_jailbreak,hu2026refusal_dynamics,ahrend2026safer_traces}.
7	
8	\textit{Detection.} CoT monitoring can detect reward hacking but optimization pressure promotes obfuscation~\cite{baker2025monitoring}. CoT monitorability is valuable but fragile~\cite{korbak2025cot_monitorability}. GuardReasoner~\cite{xiang2025guardreasoner} trains a dedicated reasoning-based guard model. \citet{schulz2025roadmap} proposes a structured safety-case framework grounded in CoT monitoring, formalizing the deployment context our probes would serve.
9	
10	\textit{Mitigation.} SafeThink~\cite{safethink} steers early reasoning toward safety, SafeRemind~\cite{saferemind} inserts entropy-triggered reminders, and Chain-of-Guardrails~\cite{mao2025selfjailbreak_reasoning} proposes guardrail insertion during reasoning. None of these conducts a systematic modality comparison for commitment detection.
11	
12	\paragraph{Hidden-State Safety Detection.}
13	Internal activations can detect safety violations in standard LLMs. \citet{azaria2023internal} demonstrate that internal states encode whether a model's output is truthful, motivating representation-based monitoring. \citet{zhou2024alignment} show safety-relevant information distributes across layers and argue it originates in pre-training rather than alignment; our temporal probes target a distinct phenomenon (commitment transitions during reasoning) that is absent from pre-training data. Meanwhile, \citet{qi2025shallow_alignment} find that alignment operates primarily over early output tokens. \citet{arditi2024refusal} identify a single refusal direction, \citet{turner2023activation} steer behavior via activation addition without optimization, \citet{li2023iti} intervene at inference time using layer-specific probes, and \citet{zhao2025harmfulness} show harmfulness and refusal are encoded separately. \citet{joad2026refusal_multi} reveal category-specific refusal directions, \citet{templeton2024scaling} extract interpretable features at scale, and \citet{wollschlager2025geometry} formalize multi-dimensionality through concept cones. TrajGuard~\cite{trajguard} uses Mahalanobis distance; SafeSwitch~\cite{safeswitch} trains hidden-state classifiers; SIREN~\cite{siren} monitors representations during generation; \citet{zhou2025ghost} apply layer-specific hidden-state forensics for anomaly detection; SafeDream~\cite{safedream2026}, HiddenDetect~\cite{jiang2025hiddendetect}, SafeInt~\cite{safeint2025}, and RCS~\cite{rcs2026} extend hidden-state monitoring to proactive detection, vision-language models, intervention, and contrastive scoring respectively. \citet{zhao2026safeprobing} probe safety awareness during decoding; \citet{chia2025probing_subspaces} extract latent subspaces separating safe from adversarial states. These methods assume external input manipulation and operate at the token level. The self-jailbreak setting differs because transitions are internal and span multiple reasoning steps. \citet{kadali2025internal} confirm layer-wise safety signal.
14	Concurrently, \citet{chan2025probing} demonstrate that linear probes on the \emph{final layer} (residual stream, PCA-50) predict alignment outcomes with strong F1, establishing separability of safe/unsafe reasoning. However, their single-layer, single-metric evaluation (logistic regression on the last layer, evaluated by F1 and PR-AUC alone) does not examine whether different layers yield different conclusions, the central question of our work. Our five-metric taxonomy and full-depth layer sweep reveal that metric choice alone can reverse the modality comparison (\cref{sec:layer-results}), a vulnerability that applies to any fixed-layer design including theirs. Their sentence-level temporal segmentation and our token-level windowing are complementary: they establish that early segments suffice for outcome prediction; we show that the \emph{reliability} of such predictions depends on both the layer and the metric used to select it. We reproduce TrajGuard (\cref{sec:negative}) and find its geometric approach fails because discriminative signal resides in minor PCA components.
15	
16	\paragraph{Probing Methodology and Layer Selection.}
17	Causal abstraction~\cite{geiger2023causal} formalizes when high-level causal models faithfully describe neural computation, grounding use of internal representations. Linear probing spans layer-wise classifiers~\cite{alain2017understanding}, sentence probing~\cite{conneau2018probing}, and surveys~\cite{belinkov2019analysis,belinkov2022probing,rogers2020primer}. Control tasks~\cite{hewitt2019control} distinguish structure from memorization (we adopt these; \cref{app:control}); \citet{levinstein2024liedetector} argue probing may exploit spurious correlations, a concern our control tasks address. Information-theoretic and causal formulations address probe complexity~\cite{voita2020information,pimentel2020information,ravfogel2020null,ravfogel2022rlace,belrose2023leace,elazar2021amnesic}.\footnote{The Tuned Lens~\cite{belrose2023tunedlens} offers an alternative layer-wise analysis but assumes next-token prediction, misaligned with binary CP classification.} \citet{marks2024geometry} find emergent linear structure in LLM truth representations, consistent with our safety commitment separability. That information distributes non-uniformly across layers is well established~\cite{tenney2019bert,jawahar2019bert}. Cross-layer prediction consistency has been exploited for efficiency: \citet{kaya2019shallow} identify ``overthinking'' via cross-layer disagreement, and \citet{zhou2020bert} formalize patience-based early exit. We repurpose this for safety probe layer selection (\cref{sec:layer-sensitivity}). Our contribution is orthogonal: the known layer-wise information gradient interacts with metric choice to produce systematic selection bias in safety probes. Most directly, \citet{boxo2025linear_probes} show linear probes can rely on textual evidence rather than deeper representations; our metric bias analysis provides a complementary mechanism: shallow-layer probes exploit compressed representations that inflate crossing rate, a geometric effect consistent with text-leakage at layers where representations have not yet diverged from surface features. \citet{alvarez2026transport_geometry} apply hidden-state geometry to step-level hallucination detection concurrently with our work. \citet{damirchi2026truth} study internal representation trajectories for layer-wise truth encoding. Concurrently, \citet{chrabaszcz2026monitoring} monitor probe trajectories across reasoning steps to characterize reasoning dynamics; our work additionally shows that metric-dependent layer selection can reverse probe conclusions, a confound absent from their analysis. \citet{vitel2025layer} independently show that layer choice significantly affects influence estimation; we demonstrate that in safety probing, this sensitivity produces qualitative reversals (\cref{sec:layer-results}). \citet{meyoyan2026bertology} propose selective probes for efficient classification; \citet{pais2026linear_probe_scaling} show multi-layer ensembling recovers where single-layer probes fail. Both complement our finding that layer choice is a validity concern.\looseness=-1
18	
19	\paragraph{Alternative Detection Approaches.}
20	BOCPD~\cite{adams2007bayesian} detects abrupt distributional shifts; CCS~\cite{burns2023discovering} discovers latent truth directions via consistency constraints; RepE~\cite{zou2023representation} identifies concept directions through mean differences. We adapt all three to temporal commitment detection (\cref{sec:negative}). BOCPD and CUSUM fail because commitment is gradual. CCS provides no gain because its consistency objective misaligns with temporal structure. RepE shows inconsistent performance across models (0.756 on QwQ, 0.559 on R1-32B). These failures motivate supervised probes with principled layer selection as the minimal effective methodology.
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ff63f8f-5b82-46ec-942e-9905faf7d07f",
  "isSidechain": true,
  "promptId": "b1899cf7-50e7-4ba4-a982-bccf7d2835cb",
  "agentId": "acee8d8337f321220",
  "type": "user",
  "uuid": "a82d4f5e-0380-4cf2-b7fb-f123afb34172",
  "sourceToolAssistantUUID": "8ff63f8f-5b82-46ec-942e-9905faf7d07f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T22:10:54.648Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ALhPHuWZHMGpoEUjaK3uiP`</summary>

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
  "parentUuid": "a82d4f5e-0380-4cf2-b7fb-f123afb34172",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
  "requestId": "req_011CbGUnKk4kpw3UjSqktQUv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71155663-9e49-42cb-9780-030d88038b11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DVFB8EapvLrdXMCKHNajiS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3302,
      "cache_read_input_tokens": 29266,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3302
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 29266,
          "cache_creation_input_tokens": 3302,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3302,
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

_source line 30 · 2026-05-21T22:10:54.651Z_

<details><summary>↩ Tool result · `toolu_01ALhPHuWZHMGpoEUjaK3uiP`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	Layer selection metric choice can reverse a safety study's central conclusion: for QwQ-32B, the same data yield $p{=}0.83$ or $p{<}0.005$ depending solely on metric. The HS advantage is validated at 7--8B (+20--22pp, nested CV) and exploratory$^\dagger$ at 32B (+15--19pp) against 384d encoders, but conditional on encoder quality and position (partially correlated). The study is limited to HarmThoughts with predominantly Qwen models (3/4); causal validation and broader coverage remain necessary.\looseness=-1
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71155663-9e49-42cb-9780-030d88038b11",
  "isSidechain": true,
  "promptId": "b1899cf7-50e7-4ba4-a982-bccf7d2835cb",
  "agentId": "acee8d8337f321220",
  "type": "user",
  "uuid": "f3af2344-446a-4f60-b931-f5534c60a058",
  "sourceToolAssistantUUID": "71155663-9e49-42cb-9780-030d88038b11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T22:10:58.704Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SpgNWwA8qA2eecXsG4ZK3R`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3af2344-446a-4f60-b931-f5534c60a058",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
  "requestId": "req_011CbGUnnJz6x52ZCXq4rkbR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0eab6f67-496c-4e43-a3bf-3b422179dd51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L6MfPF9DrxJn1rDCRQ1wte",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2737,
      "cache_read_input_tokens": 32568,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2737
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 109,
          "cache_read_input_tokens": 32568,
          "cache_creation_input_tokens": 2737,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2737,
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

_source line 32 · 2026-05-21T22:10:58.710Z_

<details><summary>↩ Tool result · `toolu_01SpgNWwA8qA2eecXsG4ZK3R`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0eab6f67-496c-4e43-a3bf-3b422179dd51",
  "isSidechain": true,
  "promptId": "b1899cf7-50e7-4ba4-a982-bccf7d2835cb",
  "agentId": "acee8d8337f321220",
  "type": "user",
  "uuid": "7c247951-d780-4781-acba-432811c0a7da",
  "sourceToolAssistantUUID": "0eab6f67-496c-4e43-a3bf-3b422179dd51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T22:11:03.371Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ea8nQbtBaSWizryWzF4AMW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
  "offset": 150,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c247951-d780-4781-acba-432811c0a7da",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
  "requestId": "req_011CbGUo5dXYKdKtg8BYvUQQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c580424-d658-4b8d-aed9-60041069966b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kWQ9r98BGPCJeSqCZLkvq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5022,
      "cache_read_input_tokens": 35305,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5022
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 35305,
          "cache_creation_input_tokens": 5022,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5022,
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

_source line 34 · 2026-05-21T22:11:03.386Z_

<details><summary>↩ Tool result · `toolu_01Ea8nQbtBaSWizryWzF4AMW`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c580424-d658-4b8d-aed9-60041069966b",
  "isSidechain": true,
  "promptId": "b1899cf7-50e7-4ba4-a982-bccf7d2835cb",
  "agentId": "acee8d8337f321220",
  "type": "user",
  "uuid": "674fd071-5fd9-493a-b7ac-faf0131a38aa",
  "sourceToolAssistantUUID": "7c580424-d658-4b8d-aed9-60041069966b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T22:11:08.038Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B5xYmVEUTU9BciVoNM6VVW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
  "offset": 350,
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "674fd071-5fd9-493a-b7ac-faf0131a38aa",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
  "requestId": "req_011CbGUoRdoWujCNBKA9Mhcs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f351743-2ec4-4820-bb65-e7e262cb648f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrwnFbZrEbNeX3Q6qf4eRT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6264,
      "cache_read_input_tokens": 40327,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6264
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 40327,
          "cache_creation_input_tokens": 6264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6264,
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

_source line 36 · 2026-05-21T22:11:08.055Z_

<details><summary>↩ Tool result · `toolu_01B5xYmVEUTU9BciVoNM6VVW`</summary>

```text
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
400	
401	\paragraph{Bootstrap comparison (matched $W{=}3$).} To ensure a fair modality comparison, bootstrap tests use matched $W{=}3$ for both HS and text probes. At $W{=}3$, HS probes achieve 75.3\% trace-level balanced accuracy vs.\ 65.6\% for text (bootstrap $\Delta{=}$+10.7pp, 95\% CI [4.9, 16.3], $p{<}0.001$, survives Holm-Bonferroni). Precision: 55.8\% vs.\ 34.6\% (bootstrap $\Delta{=}$+21.9pp, 95\% CI [14.0, 29.6], $p{<}0.001$, survives Holm-Bonferroni). Pre-CP FPR: 10.0\% vs.\ 27.1\% (bootstrap $\Delta{=}{-}17.1$pp, 95\% CI [$-$22.2, $-$12.2], $p{<}0.001$, survives Holm-Bonferroni). All three metrics survive correction. The point-estimate precision gap (+21.2pp) aligns with the bootstrap mean (+21.9pp); the small discrepancy reflects resampling variance. Using each modality's optimal $W$ (HS at $W{=}3$, text at $W{=}25$) would introduce a confound because text would benefit from 8$\times$ more temporal context.
402	
403	
404	\section{GRU Training Details}
405	\label{app:gru_details}
406	
407	GRU results serve as supplementary evidence under a different training protocol (70/30 split); direct comparison with the main logistic regression pipeline (60/20/20 nested CV) is not intended.
408	
409	\paragraph{Data split.} GRU experiments use a 70/30 train/test split to maximize training data for the sequential model, differing from the main 60/20/20 protocol used for logistic regression probes. Within the 70\% training portion, we hold out 10\% of total traces as a validation set for early stopping (effective 60/10/30 split). The validation set is used only for early stopping and is not included in reported test metrics, so there is no information leakage.
410	
411	\paragraph{Architecture.} We evaluate two GRU variants. The single-layer variant uses a GRU with hidden dimension 256, taking per-step hidden states from the best layer (selected by validation balanced accuracy) as input. The multi-layer variant concatenates hidden states from 7 layers (evenly spaced through the network) at each step to produce a higher-dimensional input to the same GRU architecture.
412	
413	\paragraph{Training procedure.} We train with Adam (learning rate $1 \times 10^{-3}$, default $\beta_1{=}0.9$, $\beta_2{=}0.999$), batch size 16, for a maximum of 50 epochs. Early stopping halts training when validation loss does not improve for 10 consecutive epochs. Input features are z-score normalized per dimension using training set statistics.
414	
415	\paragraph{Evaluation.} We report crossing accuracy (the sustained accuracy at which the probe first exceeds chance for 5 consecutive steps) and detection lead (steps before CP at crossing point). All experiments use 3 random seeds; we report mean $\pm$ standard deviation.
416	
417	\paragraph{Per-seed results for R1-8B (single-layer GRU).}
418	
419	\begin{table}[htbp]
420	\centering
421	\small
422	\caption{R1-8B single-layer GRU results per seed. Lead is measured in steps before the commitment point.}
423	\label{tab:gru_seeds}
424	\setlength{\tabcolsep}{4pt}
425	\resizebox{\columnwidth}{!}{%
426	\begin{tabular}{lccc}
427	\toprule
428	Seed & Peak Acc. & Crossing Acc. & Lead (steps) \\
429	\midrule
430	1 & 85.2 & 74.3 & +4.8 \\
431	2 & 83.1 & 71.6 & +4.8 \\
432	3 & 83.4 & 70.4 & +0.9 \\
433	\midrule
434	Mean $\pm$ std & 83.9 $\pm$ 1.1 & 72.1 $\pm$ 2.0 & +3.5 $\pm$ 2.3 \\
435	\bottomrule
436	\end{tabular}}
437	\end{table}
438	
439	The high variance in lead time (standard deviation of 2.3 steps) is driven by seed 3, where the probe achieves good peak accuracy but crosses the detection threshold late. This variance underscores the sensitivity of early detection to initialization and motivates reporting per-seed results rather than relying on mean values alone.
440	
441	Results in this section use the 60/20/20 protocol consistent with the main text; earlier 70/30 results are retained for completeness but should not be compared directly.
442	
443	\paragraph{Multi-layer GRU and baseline comparison (60/20/20 protocol).}
444	
445	\begin{table}[htbp]
446	\centering
447	\scriptsize
448	\caption{Per-seed performance of GRU and logistic regression (LR) probes on R1-8B under a 60/20/20 cross-validation protocol (seeds 42, 123, 456). Single = layer 14 only; Multi = 7-layer concatenation (layers 12--24, stride 2). Lead = steps before CP at first sustained crossing. Main text results use a 70/30 train/test split with different test traces, accounting for the difference in lead values.}
449	\label{tab:gru_multi_seeds}
450	\resizebox{\columnwidth}{!}{%
451	\begin{tabular}{llccccc}
452	\toprule
453	Model & Seed & Acc & Prec & FPR & Cross.\% & Lead \\
454	\midrule
455	GRU-single & 42  & 0.845 & 0.657 & 0.139 & 72.1\% & 3.55 \\
456	GRU-single & 123 & 0.760 & 0.454 & 0.191 & 65.1\% & 7.39 \\
457	GRU-single & 456 & 0.792 & 0.474 & 0.203 & 67.4\% & 8.45 \\
458	\rowcolor{gray!10}
459	GRU-single & \textit{mean} & 0.799$\pm$0.035 & 0.528$\pm$0.091 & 0.178$\pm$0.028 & 68.2$\pm$2.9\% & 6.46$\pm$2.10 \\
460	\midrule
461	GRU-multi  & 42  & 0.824 & 0.616 & 0.164 & 74.4\% & 5.66 \\
462	GRU-multi  & 123 & 0.759 & 0.454 & 0.195 & 65.1\% & 6.43 \\
463	GRU-multi  & 456 & 0.784 & 0.460 & 0.207 & 65.1\% & 8.93 \\
464	\rowcolor{gray!10}
465	GRU-multi  & \textit{mean} & 0.789$\pm$0.027 & 0.510$\pm$0.075 & 0.189$\pm$0.018 & 68.2$\pm$4.4\% & 7.01$\pm$1.40 \\
466	\midrule
467	LR-single  & 42  & 0.841 & 0.693 & 0.097 & 46.5\% & $-$2.00 \\
468	LR-single  & 123 & 0.753 & 0.436 & 0.181 & 53.5\% & 5.26 \\
469	LR-single  & 456 & 0.814 & 0.512 & 0.146 & 41.9\% & 3.94 \\
470	\rowcolor{gray!10}
471	LR-single  & \textit{mean} & 0.803$\pm$0.037 & 0.547$\pm$0.108 & 0.141$\pm$0.035 & 47.3$\pm$4.8\% & 2.40$\pm$3.16 \\
472	\midrule
473	LR-multi   & 42  & 0.827 & 0.679 & 0.092 & 39.5\% & 1.06 \\
474	LR-multi   & 123 & 0.756 & 0.442 & 0.180 & 46.5\% & 7.30 \\
475	LR-multi   & 456 & 0.817 & 0.521 & 0.130 & 34.9\% & 4.00 \\
476	\rowcolor{gray!10}
477	LR-multi   & \textit{mean} & 0.800$\pm$0.032 & 0.547$\pm$0.099 & 0.134$\pm$0.036 & 40.3$\pm$4.8\% & 4.12$\pm$2.55 \\
478	\bottomrule
479	\end{tabular}}%
480	\end{table}
481	
482	Under this protocol, multi-layer GRU achieves the highest mean lead (7.01$\pm$1.40 steps) but at higher FPR than logistic regression baselines (0.189 vs.\ 0.134). The GRU advantage is concentrated in detection timing rather than classification accuracy, consistent with the main text finding that GRUs capture sequential dependencies that improve early detection. Lead time shows high variance across seeds (range 5.66--8.93 for GRU-multi), reinforcing that reported means should be interpreted cautiously.
483	
484	\paragraph{OT-7B multi-layer GRU (layers 13--19, 3 seeds, 60/20/20 split).}
485	OT-7B GRU achieves 74.6$\pm$1.3\% balanced accuracy, 64.5$\pm$7.0\% coverage, +33.6$\pm$4.8 steps lead, and 27.4$\pm$6.1\% pre-CP FPR. The lead time is substantially longer than other models in absolute terms, but OT-7B traces average ${\sim}$80 reasoning steps (vs.\ ${\sim}$30 for R1-8B and 32B models), so absolute lead times are not directly comparable. The FPR-lead tradeoff mirrors R1-8B: GRU FPR (27.4\%) is far above the LR probe at layer 16 (10.0\%), which confirms that GRUs gain lead time at the cost of more false alarms across both 7-8B models.
486	
487	
488	\section{Control Task Methodology}
489	\label{app:control}
490	
491	We follow the selectivity framework of \cite{hewitt2019control} to verify that our probes capture genuine safety-relevant structure rather than surface-level correlations.
492	
493	\paragraph{Procedure.} For each model, we randomly permute the binary labels (pre-CP vs. post-CP) within each trace while preserving the marginal label distribution. We then retrain the probe with identical architecture (L2-regularized logistic regression) and hyperparameters on these shuffled labels. Selectivity is defined as:
494	\begin{equation}
495	    \text{Selectivity} = \text{Acc}_{\text{linguistic}} - \text{Acc}_{\text{control}}
496	\end{equation}
497	where $\text{Acc}_{\text{linguistic}}$ is the probe accuracy on true labels and $\text{Acc}_{\text{control}}$ is the accuracy on permuted labels. A selectivity of zero indicates that the probe exploits only non-linguistic features (e.g., position); higher values confirm that the representation encodes task-relevant information. Absolute selectivity values are task-dependent and not directly comparable across studies~\citep{hewitt2019control}.
498	
499	\paragraph{Results.} We repeat the control experiment 10 times with different random permutations and report the mean control accuracy. Selectivity scores at threshold-based layers (60/20/20 split) are: R1-32B 16.8pp (layer 63), QwQ-32B 16.1pp (layer 63), R1-8B 14.1pp (layer 14), OT-7B 11.1pp (layer 16). All values exceed the 5pp threshold recommended by \cite{hewitt2019control}. R1-32B and QwQ-32B achieve the strongest selectivity ($>$16pp) at threshold-based layers. On QwQ-32B, the position baseline accuracy (0.705) slightly exceeds the HS probe (0.667) at L60, consistent with the main-text finding that QwQ's HS advantage is concentrated in precision and FPR rather than balanced accuracy.
500	
501	\paragraph{Layer provenance note.} R1-8B is unaffected by the layer selection bias because its CR-composite and threshold-based layers coincide at L14. OT-7B exhibits a 16-layer gap (CR-composite L0 vs.\ threshold-based L16; \cref{tab:layer_selection}), but selectivity at L16 (11.1pp) still exceeds the 5pp threshold. QwQ-32B selectivity is 16.1pp at L63, which confirms that safety-specific signal persists at deep layers.
502	
503	\paragraph{Position-only baseline.} As a complementary validation, we train a logistic regression classifier using only the normalized step index ($t / T$ where $T$ is the total trace length) as the input feature. This baseline tests whether temporal position alone explains probe performance. On R1-8B, the position-only baseline produces 15.8\% FPR compared to 8.1\% for the HS probe at matched detection rates. The probe's substantially lower FPR confirms that hidden state features carry information beyond what step position provides.
504	
505	\paragraph{Residualized selectivity.} To confirm that selectivity survives position removal, we recompute control task selectivity on position-regressed features (the same residualized representations used in \cref{app:position_residual}). Residualized selectivity: R1-8B 22.9pp, OT-7B 10.4pp, QwQ-32B 11.3pp (all ${>}5$pp), R1-32B 3.0pp (${<}5$pp, consistent with the position-mediation pattern reported in \cref{sec:hs-text}). Three of four models retain selectivity well above the \citet{hewitt2019control} threshold after position removal; R1-32B's drop confirms that its safety signal is largely positional.
506	
507	
508	\section{Oracle Upper Bound Analysis}
509	\label{sec:oracle}
510	
511	We compute an oracle upper bound for commitment detection by measuring the earliest step at which the ground-truth commitment point (CP) could theoretically be predicted from hidden-state dynamics. The oracle detector has access to the true CP label and computes how many steps before CP the representation trajectory first enters a region that is linearly separable from pre-CP states with perfect accuracy on the training set. The resulting bound provides a theoretical ceiling on early detection performance.
512	
513	\cref{tab:oracle} reports oracle performance across all four models. Oracle analysis confirms the evidence gradient: OT-7B (strong) shows the highest early detection rate (93.6\%) and longest lead time (50 steps), while R1-32B (qualified) achieves only 50\% early detection even with oracle labels, consistent with an inherently weaker commitment signal. On R1-8B, the oracle early detection rate is 76.7\% (33/43 traces detected before CP, with +31 steps mean lead time), compared to +4.5 steps for the best learned probe (GRU). This gap indicates that hidden states at step $t$ encode the model's current safety state but carry limited predictive power about future trajectory evolution. The learned probe captures the contemporaneous safety signal effectively (balanced accuracy 81--84\%) but cannot anticipate the commitment transition far in advance. Closing this gap will likely require causal intervention techniques (e.g., activation patching) rather than improvements to passive monitoring.
514	
515	\begin{table}[htbp]
516	\centering
517	\small
518	\caption{Oracle upper bound analysis. Detection rate: fraction of traces where the oracle finds a linearly separable boundary before or at CP. Early detection rate: fraction detected before CP. Mean lead: average steps before CP at first detection.}
519	\label{tab:oracle}
520	\resizebox{\columnwidth}{!}{%
521	\begin{tabular}{lcccc}
522	\toprule
523	\textbf{Model} & \textbf{Det.\ Rate} & \textbf{Early Det.} & \textbf{Mean Lead} & $n_{\text{test}}$ \\
524	\midrule
525	R1-8B & 100\% & 76.7\% & 31.0 & 43 \\
526	OT-7B & 100\% & 93.6\% & 50.0 & 47 \\
527	R1-32B$^\dagger$ & 95.0\% & 50.0\% & 32.4 & 20 \\
528	QwQ-32B$^\dagger$ & 100\% & 84.2\% & 24.4 & 19 \\
529	\bottomrule
530	\end{tabular}}
531	\end{table}
532	
533	
534	\section{CP Annotation Perturbation}
535	\label{app:cp_perturbation}
536	
537	To assess sensitivity to annotation noise, we shift all ground-truth CP labels by $\delta \in \{-3, \ldots, +3\}$ steps and retrain the HS probe (\cref{tab:cp_perturbation}). Precision degrades smoothly with no cliff effect: within $\pm 2$ steps, BA changes by ${<}2.5$pp for all models (7--8B: ${<}1.0$pp). At the $\pm 3$-step worst case, all models retain precision well above their respective text baselines. These results support the annotation robustness assumption discussed in \cref{sec:limitations}.
538	
539	\begin{table}[htbp]
540	\centering
541	\small
542	\caption{HS probe sensitivity to CP annotation shift ($\delta$ steps). BA is stable across all perturbations; precision degrades gradually without cliff effects.}
543	\label{tab:cp_perturbation}
544	\resizebox{\columnwidth}{!}{%
545	\begin{tabular}{llccc}
546	\toprule
547	\textbf{Model} & $\delta$ & \textbf{Prec} & \textbf{BA} & \textbf{FPR} \\
548	\midrule
549	R1-8B & $-3$ & .652 & .773 & .177 \\
550	 & $0$ & .596 & .784 & .165 \\
551	 & $+3$ & .530 & .771 & .143 \\[2pt]
552	OT-7B & $-3$ & .404 & .714 & .298 \\
553	 & $0$ & .351 & .707 & .286 \\
554	 & $+3$ & .300 & .702 & .276 \\[2pt]
555	QwQ-32B & $-3$ & .661 & .728 & .158 \\
556	 & $0$ & .609 & .690 & .129 \\
557	 & $+3$ & .550 & .676 & .114 \\[2pt]
558	R1-32B & $-3$ & .625 & .698 & .360 \\
559	 & $0$ & .570 & .722 & .281 \\
560	 & $+3$ & .503 & .750 & .236 \\
561	\bottomrule
562	\end{tabular}}
563	\end{table}
564	
565	\subsection{Inter-Annotator Agreement on AdvBench}
566	\label{app:iaa}
567	
568	To assess annotation reliability, two LLM annotators (Qwen3-32B and GPT-4o-mini) independently labeled 388 AdvBench B-class traces for jailbreak status and CP position (\cref{tab:iaa}).
569	
570	\begin{table}[htbp]
571	\centering
572	\small
573	\caption{Inter-annotator agreement on AdvBench B-class traces (388 total). CP position metrics computed on 51 traces where both annotators identified a jailbreak.}
574	\label{tab:iaa}
575	\resizebox{\columnwidth}{!}{%
576	\begin{tabular}{lc}
577	\toprule
578	\textbf{Metric} & \textbf{Value} \\
579	\midrule
580	\textit{Jailbreak classification} \\
581	\quad Cohen's $\kappa$ & 0.606 (moderate) \\
582	\quad Raw agreement & 87.4\% \\
583	\quad GPT-4o-mini JB count & 99 / 388 \\
584	\quad Qwen3-32B JB count & 52 / 388 \\
585	\midrule
586	\textit{CP position (51 shared JB)} \\
587	\quad Exact match & 37\% \\
588	\quad Within 5 steps & 47\% \\
589	\quad Mean abs.\ difference & 8.5 steps \\
590	\bottomrule
591	\end{tabular}}
592	\end{table}
593	
594	LLM annotators achieve only moderate agreement on jailbreak classification ($\kappa{=}0.606$) and low CP position consistency (37\% exact match). GPT-4o-mini is substantially more aggressive in jailbreak identification (99 vs.\ 52), suggesting systematic annotator bias. The low CP position agreement (mean absolute difference of 8.5 steps) underscores a key design choice: our primary analysis uses the human-validated HarmThoughts annotations~\citep{harmthoughts}, not LLM-generated labels. This AdvBench IAA study serves as a \emph{negative control}: it demonstrates that LLM-only annotation is insufficient for reliable CP localization, motivating future investment in multi-annotator human CP labeling with formal IAA evaluation.
595	
596	\section{BOCPD/CUSUM Configuration Sweep}
597	\label{app:bocpd_config}
598	
599	We sweep hyperparameters for both Bayesian Online Change-Point Detection (BOCPD) and Cumulative Sum (CUSUM) methods applied to the temporal probe score sequences.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f351743-2ec4-4820-bb65-e7e262cb648f",
  "isSidechain": true,
  "promptId": "b1899cf7-50e7-4ba4-a982-bccf7d2835cb",
  "agentId": "acee8d8337f321220",
  "type": "user",
  "uuid": "3d2e0166-7eac-4209-b14f-b4e70b6a3b6e",
  "sourceToolAssistantUUID": "4f351743-2ec4-4820-bb65-e7e262cb648f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T22:11:12.776Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ARW7332omBDajph8gQAzv2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
  "offset": 600,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d2e0166-7eac-4209-b14f-b4e70b6a3b6e",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
  "requestId": "req_011CbGUomZ86BxE34GVF9Hyc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad342883-d816-4499-af33-6e8c3e187e38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vb42SubrohESBcBXBch8zt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7277,
      "cache_read_input_tokens": 46591,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7277
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 46591,
          "cache_creation_input_tokens": 7277,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7277,
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

_source line 38 · 2026-05-21T22:11:13.023Z_

<details><summary>↩ Tool result · `toolu_01ARW7332omBDajph8gQAzv2`</summary>

```text
600	
601	\paragraph{BOCPD configurations.} BOCPD models the sequence of probe scores as piecewise-constant segments with Gaussian observation noise. The hazard rate $\lambda$ controls the prior probability of a change-point at each step ($P(\text{change}) = 1/\lambda$).
602	
603	\paragraph{CUSUM configurations.} CUSUM accumulates evidence for a positive mean shift. The drift parameter $\delta$ sets the minimum shift size to detect, and the threshold $h$ controls the detection boundary.
604	
605	\begin{table}[htbp]
606	\centering
607	\small
608	\caption{Change-point method configuration sweep on R1-8B. Detection rate is the fraction of jailbreak traces where the method fires. Lead is measured in steps before CP.}
609	\label{tab:cpd_sweep}
610	\setlength{\tabcolsep}{4pt}
611	\resizebox{\columnwidth}{!}{%
612	\begin{tabular}{llcc}
613	\toprule
614	Method & Configuration & Det.\ Rate & Lead \\
615	\midrule
616	\multirow{5}{*}{BOCPD}
617	 & $\lambda = 5$   & 97 & +2.1 \\
618	 & $\lambda = 10$  & 93 & +3.5 \\
619	 & $\lambda = 20$  & 87 & +4.2 \\
620	 & $\lambda = 50$  & 72 & +5.8 \\
621	 & $\lambda = 100$ & 67.4 & +1.03 \\
622	\midrule
623	\multirow{10}{*}{CUSUM}
624	 & $\delta{=}0.3$, $h{=}3$ & 65.1 & +0.89 \\
625	 & $\delta{=}0.5$, $h{=}3$ & 89 & +1.4 \\
626	 & $\delta{=}0.5$, $h{=}5$ & 76 & +2.3 \\
627	 & $\delta{=}0.5$, $h{=}8$ & 61 & +3.1 \\
628	 & $\delta{=}1.0$, $h{=}3$ & 82 & +1.1 \\
629	 & $\delta{=}1.0$, $h{=}5$ & 68 & +1.9 \\
630	 & $\delta{=}1.0$, $h{=}8$ & 52 & +2.7 \\
631	 & $\delta{=}2.0$, $h{=}3$ & 71 & +0.8 \\
632	 & $\delta{=}2.0$, $h{=}5$ & 54 & +1.5 \\
633	 & $\delta{=}2.0$, $h{=}8$ & 38 & +2.1 \\
634	\midrule
635	Simple threshold & FCP baseline & 65.1 & +4.89 \\
636	\bottomrule
637	\end{tabular}}
638	\end{table}
639	
640	The best BOCPD configuration ($\lambda{=}10$) achieves 93.0\% detection rate with +3.45 steps lead. The simple threshold baseline achieves 65.1\% detection with superior lead (+4.89 steps). All CUSUM configurations underperform the simple threshold on lead time.
641	
642	These results reveal a coverage-timing tradeoff. BOCPD ($\lambda{=}10$) achieves 28pp higher detection rate than simple thresholding (93.0\% vs.\ 65.1\%), but with lower lead (+3.45 vs.\ +4.89 steps). The transition toward unsafe reasoning is gradual rather than abrupt, so change-point methods cannot exploit discontinuities for early warning. When missed detections are costly, BOCPD's coverage advantage justifies its use despite the timing penalty. When early intervention is the priority, simple thresholding provides better lead time.
643	
644	\paragraph{Other models.} On OT-7B, QwQ-32B, and R1-32B, BOCPD achieves 0\% detection rate across all tested configurations ($\lambda \in \{5, 10, 50, 100, 200\}$). The failure modes differ by model: for R1-32B and QwQ-32B, probe scores transition gradually, so the hazard function never accumulates sufficient evidence; for OT-7B at $W{=}3$, transitions are too abrupt (0$\to$1 in 1--2 steps) for the Gaussian observation model to capture. R1-8B falls between these extremes, with transitions sharp enough to trigger the hazard function but smooth enough for the Gaussian model to track.
645	
646	
647	\section{Detection Threshold ($K$) Ablation}
648	\label{app:k_ablation}
649	
650	The consecutive-crossings threshold $K$ controls the trade-off between detection coverage and false positive rate. We evaluate $K \in \{1, 3, 5, 7, 10\}$ at $W{=}1$ on all models using HS probes at threshold-based layers (\cref{tab:k_ablation}).
651	
652	\begin{table}[htbp]
653	\centering
654	\small
655	\caption{Detection threshold ablation ($W{=}1$, HS probes at threshold-based layers). Coverage: fraction of jailbreak traces with $\geq K$ consecutive crossings. Safe FPR: fraction of safe traces with $\geq K$ consecutive false alarms.}
656	\label{tab:k_ablation}
657	\setlength{\tabcolsep}{3pt}
658	\resizebox{\columnwidth}{!}{%
659	\begin{tabular}{lccccccccc}
660	\toprule
661	& \multicolumn{4}{c}{\textbf{Coverage}} & & \multicolumn{4}{c}{\textbf{Safe FPR}} \\
662	\cmidrule{2-5} \cmidrule{7-10}
663	$K$ & R1-8B & OT-7B & QwQ & R1-32B & & R1-8B & OT-7B & QwQ & R1-32B \\
664	\midrule
665	1  & 1.00 & 1.00 & 1.00 & 1.00 & & 1.00 & 0.92 & 1.00 & 0.99 \\
666	3  & 0.74 & 0.79 & 0.95 & 0.90 & & 0.81 & 0.41 & 0.78 & 0.78 \\
667	5  & 0.47 & 0.51 & 0.79 & 0.65 & & 0.63 & 0.19 & 0.65 & 0.47 \\
668	7  & 0.35 & 0.30 & 0.58 & 0.45 & & 0.39 & 0.16 & 0.35 & 0.31 \\
669	10 & 0.14 & 0.21 & 0.32 & 0.35 & & 0.22 & 0.08 & 0.25 & 0.17 \\
670	\bottomrule
671	\end{tabular}}
672	\end{table}
673	
674	$K{=}1$ yields perfect coverage but near-perfect safe FPR (0.92--1.00), offering no discrimination. $K{=}5$ is empirically selected as a middle-ground tradeoff: average coverage 0.60 with average safe FPR 0.48 across models. OT-7B benefits most from increasing $K$, reaching 0.19 safe FPR at $K{=}5$ (vs.\ 0.92 at $K{=}1$) while retaining 51\% coverage. Higher $K$ values ($\geq$7) reduce safe FPR further but at steep coverage cost. $K{=}5$ vs.\ $K{=}7$ is the key decision: $K{=}7$ reduces mean safe FPR from 0.48 to 0.30 but drops mean coverage from 0.60 to 0.42.
675	
676	$K{=}5$ was selected on the R1-8B validation set and held fixed across all models; main-text results use this value without per-model optimization. The $K \times W$ interaction is not fully explored: this ablation uses $W{=}1$ to isolate $K$'s effect, and the joint $K \times W$ surface remains a limitation. At optimal $W$, coverage at $K{=}5$ improves (e.g., R1-8B: 0.47 at $W{=}1$ vs.\ 0.60 at $W{=}15$).
677	
678	\subsection{Deployment Operating Points}
679	\label{app:deployment_operating_points}
680	
681	The $K$ ablation above can be recast as a deployment operating characteristic. At $K{=}5$ (used throughout the main text), average coverage is 60\% with 48\% safe FPR. Raising $K$ yields practically useful operating points: at $K{=}10$, OT-7B achieves 21\% coverage with only 8\% false positive rate, meaning fewer than 1 in 12 flagged traces is a false alarm. R1-32B at $K{=}10$ retains 35\% coverage at 17\% FPR. These conservative operating points are viable for high-stakes deployment where missed detections are preferable to frequent false alarms: a secondary review system could inspect only flagged traces, reducing human oversight burden by 79--86\% while maintaining non-trivial detection rates. However, at $K{=}10$ approximately 65--86\% of attacks are missed, which may be unacceptable in some threat models. The $K{=}7$ setting offers a middle ground (30--58\% coverage, 16--39\% FPR). The choice of operating point is deployment-specific.
682	
683	
684	\section{Decision Threshold Sensitivity}
685	\label{app:threshold_sensitivity}
686	
687	We evaluate whether the HS advantage depends on the logistic regression decision threshold by sweeping $\tau \in \{0.3, 0.4, 0.5, 0.6, 0.7\}$ for both 32B models at their threshold-based layers. Results below were conducted at L60 under the 70/30 protocol; main-text results use L63 under 60/20/20. QwQ-32B (L60, $W{=}3$) HS balanced accuracy varies by only 0.53pp across all thresholds, with $\Delta$(HS$-$Text) stable at +8.5 to +9.3pp. \cref{tab:threshold_r132b} reports R1-32B results.
688	
689	\begin{table}[htbp]
690	\centering
691	\small
692	\caption{R1-32B threshold sensitivity (L63, $W{=}1$). HS BA varies by 1.1pp (0.741--0.752); the HS advantage is consistent across all thresholds.}
693	\label{tab:threshold_r132b}
694	\resizebox{\columnwidth}{!}{%
695	\begin{tabular}{ccccccc}
696	\toprule
697	$\tau$ & HS BA & $\Delta$BA & HS Prec & $\Delta$Prec & HS FPR & $\Delta$FPR \\
698	\midrule
699	0.3 & 0.752 & +0.126 & 0.583 & +0.126 & 0.295 & $-$0.106 \\
700	0.4 & 0.746 & +0.116 & 0.586 & +0.120 & 0.281 & $-$0.092 \\
701	\textbf{0.5} & \textbf{0.742} & \textbf{+0.109} & \textbf{0.588} & \textbf{+0.113} & \textbf{0.273} & $\mathbf{-}$\textbf{0.078} \\
702	0.6 & 0.741 & +0.112 & 0.599 & +0.119 & 0.254 & $-$0.072 \\
703	0.7 & 0.743 & +0.126 & 0.617 & +0.143 & 0.228 & $-$0.084 \\
704	\bottomrule
705	\end{tabular}}
706	\end{table}
707	
708	R1-32B HS balanced accuracy varies by only 1.1pp across the full threshold range. The modality advantage ($\Delta$BA $= +0.109$ to $+0.126$, $\Delta$Prec $= +0.113$ to $+0.143$, $\Delta$FPR $= -0.072$ to $-0.106$) is consistent in both magnitude and direction at every threshold, so the HS advantage is not an artifact of the default $\tau{=}0.5$.
709	
710	
711	\section{M002 Bug Disclosure}
712	\label{app:bug}
713	
714	We disclose a bug discovered during development that affected intermediate results for QwQ-32B.
715	
716	\paragraph{Issue.} In experiment M002 (text baseline evaluation), the QwQ-32B text probe was inadvertently initialized with a midpoint heuristic placeholder rather than true sentence embeddings from all-MiniLM-L6-v2. Specifically, the placeholder assigned each step a feature vector equal to the midpoint between the mean safe and mean unsafe embeddings from the training set, with small Gaussian noise added. This made the text probe trivially predictive and produced a spuriously significant result ($p{=}0.001$ for HS vs. text FPR difference).
717	
718	\paragraph{Discovery and correction.} The bug was identified during a systematic audit of the feature extraction pipeline. After correction (using actual sentence embeddings), the QwQ-32B and R1-32B modality comparisons at the originally selected layers (L2 and L10, chosen by the CR-composite metric) showed no significant HS advantage: QwQ-32B accuracy $p{=}0.828$, precision $p{=}0.346$; R1-32B precision $p{=}0.050$ but no tests surviving Holm-Bonferroni. The subsequent discovery that these layer selections were themselves artifacts of metric bias (\cref{sec:layer-results}) led to the threshold-based layer analysis reported in the main text, where the HS advantage follows an evidence gradient at threshold-based deep layers: cross-validated at 7--8B, significant but suggestive of position-competitiveness at QwQ-32B$^\dagger$, and exploratory at R1-32B$^\dagger$ (\cref{tab:hs_vs_text}).
719	
720	\paragraph{Impact on reported results.} All numbers reported in this paper use the corrected text embedding pipeline. The bug affected only QwQ-32B text probe features. The correction, combined with the separate layer selection fix (\cref{sec:layer-results}), means that early-stage intermediate results (non-significant 32B modality comparisons) reflected two compounding errors: incorrect text features and CR-composite layer selection. Both are fully resolved in the final analysis.
721	
722	\paragraph{Commitment to transparency.} We report this bug to maintain scientific integrity. Code and data will be released upon publication.
723	
724	\section{Adaptive Two-Stage Detection}
725	\label{app:two_stage}
726	
727	We explored whether a two-stage adaptive window strategy could improve the precision-coverage tradeoff beyond fixed-window detection. The approach uses a short screening window ($W_{\text{screen}}$) to flag candidate unsafe segments, followed by a longer confirmation window ($W_{\text{confirm}}$) applied only to flagged segments. A trace is classified as unsafe if at least $k$ steps exceed the threshold during the confirmation stage.
728	
729	We merge the validation and test partitions ($n{=}55$ total: 39 jailbreak, 16 benign) for two-stage evaluation because the screening and confirmation thresholds are not tuned on held-out data. We evaluated all combinations of $W_{\text{screen}} \in \{1, 3, 5\}$, $W_{\text{confirm}} \in \{10, 15, 20, 25\}$, and $k \in \{1, 3, 5\}$ on these R1-8B traces. \cref{fig:pareto_two_stage} shows the precision-coverage Pareto front for both methods. The best two-stage configuration ($W_{\text{screen}}{=}3$, $W_{\text{confirm}}{=}15$, $k{=}1$) achieves 72.2\% precision at 76.9\% coverage, compared to 70.9\% precision at 76.9\% coverage for single-stage $W{=}15$. This +1.3pp precision gain at matched coverage represents a Pareto improvement, but the magnitude is marginal. At higher confirmation thresholds ($k{=}3$, $k{=}5$), two-stage detection trades coverage for small precision gains (up to 73.5\% precision at 38.5\% coverage with $k{=}5$), but these operating points are impractical due to excessive missed detections.
730	
731	\begin{figure}[htbp]
732	\centering
733	\includegraphics[width=0.85\columnwidth]{figures/pareto_two_stage.pdf}
734	\caption{Precision-coverage Pareto front comparing single-stage fixed-window detection against two-stage adaptive detection on R1-8B. The best two-stage configuration ($W_{\text{screen}}{=}3$, $W_{\text{confirm}}{=}15$, $k{=}1$) Pareto-dominates single-stage $W{=}15$ by +1.3pp precision at matched coverage. Higher $k$ values shift the tradeoff toward precision at the cost of unacceptable coverage loss.}
735	\label{fig:pareto_two_stage}
736	\end{figure}
737	
738	The marginal improvement suggests that fixed-window smoothing already captures most of the temporal signal available in probe score sequences. The two-stage approach adds configuration complexity (three hyperparameters vs. one) without proportional performance gain.
739	
740	
741	\section{Temporal Ablation Details}
742	\label{app:temporal_details}
743	
744	\begin{figure}[t]
745	\centering
746	\includegraphics[width=\columnwidth]{figures/fig_trajectory.pdf}
747	\caption{CP-aligned probe score trajectories. Each panel averages all test traces for one model, with step 0 at the true commitment point. HS probes (blue, solid) show a sharper score increase at CP than text probes (orange, dashed), with OT-7B showing the strongest separation and R1-32B the weakest, consistent with the evidence gradient. Shaded bands: $\pm$1 std. Points with $<$5 traces are omitted.}
748	\label{fig:trajectory}
749	\end{figure}
750	
751	Full per-model temporal ablations are reported in \cref{tab:window_full} (\cref{app:window_ablation}). Key cross-model patterns: (1) R1-8B shows monotonic precision improvement from 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$) with FPR halving (9.65\% to 4.83\%); (2) OT-7B exhibits a split pattern where balanced accuracy peaks at $W{=}3$ while precision and FPR continue improving at larger windows; (3) R1-32B peaks at $W{=}10$ then degrades, likely reflecting overfitting on the small dataset ($n{=}100$); (4) QwQ-32B shows broadly increasing trends with local non-monotonicity. Text probe window ablations (\cref{app:text_window}) show monotonic improvement across all window sizes for both models tested, with larger marginal gains than HS probes (+12.0pp accuracy vs.\ +3.2pp for R1-8B). The asymmetry supports the interpretation that text features benefit proportionally more from temporal context because they encode less information per step.
752	
753	\section{Negative Results Details}
754	\label{app:negative_details}
755	
756	\begin{table}[htbp]
757	\centering
758	\small
759	\resizebox{\columnwidth}{!}{%
760	\begin{tabular}{p{1.4cm}p{2.5cm}p{2.0cm}p{1.6cm}}
761	\toprule
762	\textbf{Method} & \textbf{Result} & \textbf{Limitation} & \textbf{Failure Cat.} \\
763	\midrule
764	BOCPD & 0\% det.\ on 3/4 models & Commitment gradual & Graduality \\
765	CUSUM & $<$ threshold, all models & Same as BOCPD & Graduality \\
766	Mahalanobis & $\Delta d \approx 0$ & Signal in minor PCs & Var.\ subspace \\
767	RepE & QwQ 0.756; R1-32B 0.559$^a$ & Model-dependent & Model-spec. \\
768	MLP & 3/4 worse than LR & Overfitting & Capacity \\
769	CCS & No gain over supervised$^b$ & Alignment mismatch & Obj.\ mismatch \\
770	Transfer & Best 59.5\% (PCA)$^c$ & Model-specific repr. & Model-spec. \\
771	\bottomrule
772	\end{tabular}}
773	\caption{Seven alternative approaches. $^a$\,RepE QwQ approaches supervised bal\_acc but precision is 0.512 vs.\ LR 0.700. $^b$\,Semi-supervised (requires CP labels). $^c$\,Best direct transfer 67.3\% but 1\% crossing rate.}
774	\label{tab:negative}
775	\end{table}
776	
777	\paragraph{BOCPD/CUSUM.} On OT-7B, QwQ-32B, and R1-32B, BOCPD achieves 0\% detection rate across all tested configurations ($\lambda \in \{5, 10, 50, 100, 200\}$). Only R1-8B produces non-zero detection (best: $\lambda{=}10$, 93\% rate, +3.45 steps lead). CUSUM configurations universally underperform simple thresholding on lead time. The probe score sequences for 3/4 models show smooth transitions that never trigger the hazard function (\cref{app:bocpd_config}).
778	
779	\paragraph{Mahalanobis distance.} Following TrajGuard~\cite{trajguard}, Mahalanobis distance from the pre-CP centroid produces $\Delta d \approx 0$ between pre-CP and post-CP steps. The discriminative signal resides in minor PCA components (explaining $<$5\% of total variance) rather than the principal directions that dominate the distance computation.
780	
781	\paragraph{RepE.} We compute the mean-difference direction~\cite{zou2023representation} $\mathbf{d} = \bar{\mathbf{h}}_{\text{post}} - \bar{\mathbf{h}}_{\text{pre}}$ from training-set hidden states, then project test-set representations onto $\mathbf{d}$ and threshold the scalar projection. QwQ-32B achieves 0.756 balanced accuracy (approaching supervised 0.778) but with substantially worse precision (0.512 vs.\ LR 0.700) and FPR (0.309 vs.\ 0.120). R1-32B nearly fails (0.559 balanced accuracy). The single direction captures commitment structure in some models but not others, consistent with the multi-dimensional encoding found by \citet{wollschlager2025geometry}.
782	
783	\paragraph{MLP probes.} Two-layer MLPs ($d \rightarrow 128 \rightarrow 1$, ReLU, no dropout, L2 weight decay $10^{-4}$, early stopping patience 10) underperform logistic regression on 3/4 models. The commitment boundary is linearly separable at correctly selected layers; additional capacity causes overfitting given the small training sets ($n{=}60$--$137$ training examples). All alternative method results in this section are upper-bounded by the hyperparameter search budget reported above.
784	
785	\paragraph{CCS.} We adapt Contrast-Consistent Search~\cite{burns2023discovering} by constructing contrastive pairs from pre-CP (``safe'') and post-CP (``committed'') hidden states at each reasoning step, then training the CCS probe to satisfy the consistency loss $P(x) + P(\neg x) = 1$. All models required polarity correction (CCS does not determine label direction). CCS achieves 0.692--0.777 balanced accuracy across models but with FPR 0.19--0.41, substantially worse than supervised LR (FPR 0.07--0.28). The consistency objective does not align with temporal commitment structure, and CCS still requires CP labels for pair construction, making it semi-supervised.
786	
787	\paragraph{Cross-model transfer.} 17 configurations (5 directional pairs $\times$ 3 PCA dimensionalities, plus 2 direct transfers) all fail. Best PCA: R1-8B $\rightarrow$ QwQ-32B at 59.5\% (PCA-2048). Best direct: QwQ-32B $\rightarrow$ R1-32B at 67.3\% but 1\% crossing rate. Implementation details in \cref{app:transfer_details}.
788	
789	\section{Cross-Model Transfer Implementation Details}
790	\label{app:transfer_details}
791	
792	We test whether safety probes transfer across models by projecting hidden states into a shared dimensionality space and applying cross-model classification.
793	
794	\paragraph{Method.} For each source-target model pair, we apply PCA independently to each model's hidden states, reducing to a shared dimensionality $d \in \{512, 1024, 2048\}$. PCA is fitted on the full dataset (including test traces) for each model separately, a setting favorable to transfer since it maximizes the quality of the projection. A logistic regression classifier (C=1.0, class\_weight=`balanced', max\_iter=2000, random\_state=42) trained on the source model's PCA-projected training data is then applied directly to the target model's PCA-projected test data. No cross-model alignment step (Procrustes rotation, CCA, or learned projection) is applied; PCA serves as a standard linear dimensionality reduction baseline.
795	
796	\paragraph{Same-dimension pairs.} For R1-32B and QwQ-32B (both 5120-d hidden states), we additionally test direct transfer without PCA: the source classifier is applied directly to the target model's raw hidden states. This tests whether same-architecture, same-dimensionality models share safety-relevant linear structure.
797	
798	\paragraph{Results.} All 17 transfer configurations (5 directional pairs $\times$ 3 PCA dimensionalities, plus 2 direct transfers for same-dimension pairs) fail to produce practically useful transfer. The best PCA result is R1-8B $\rightarrow$ QwQ-32B at 59.5\% balanced accuracy (PCA-2048). The best direct transfer (QwQ-32B $\rightarrow$ R1-32B) reaches 67.3\% balanced accuracy, which exceeds the within-model baseline of 65.2\%. However, this transfer direction achieves only 1\% crossing rate, meaning the transferred probe almost never triggers detection in practice and is useless for deployment despite above-baseline accuracy. The complete failure under maximally favorable conditions (PCA fitted on full data, no train/test separation for projection) strengthens the conclusion that safety commitment is encoded in model-specific geometric configurations. PCA is a standard linear alignment baseline; its failure indicates that the problem lies in the representations themselves rather than in the choice of alignment method. High balanced accuracy does not guarantee deployment utility: the best direct transfer (67.3\% BA) achieves only 1\% crossing rate, meaning the transferred probe almost never triggers temporal detection despite appearing accurate on per-step classification.
799	
800	
801	\section{Encoder Robustness Analysis}
802	\label{app:encoder_robustness}
803	
804	To test whether the HS advantage over text probes depends on the specific text encoder, we replace all-MiniLM-L6-v2 (384d) with BGE-large-en-v1.5 (1024d), a 2.7$\times$ higher-dimensional encoder with stronger semantic representations. \cref{tab:encoder_robustness} reports precision comparisons at each model's threshold-based layer; \cref{fig:forest_precision} provides a visual summary.
805	
806	\begin{table}[htbp]
807	\centering
808	\small
809	\caption{HS vs.\ BGE-large (1024d) text probe precision. $\Delta$: HS minus BGE-large. Bootstrap: 10{,}000 resamples, two-sided null-centered. HB: survives Holm-Bonferroni correction (4 tests, $\alpha{=}0.05$).}
810	\label{tab:encoder_robustness}
811	\resizebox{\columnwidth}{!}{%
812	\begin{tabular}{lcccccc}
813	\toprule
814	\textbf{Model} & \textbf{HS Prec} & \textbf{BGE Prec} & $\Delta$ & \textbf{95\% CI} & $p$ & \textbf{HB} \\
815	\midrule
816	R1-8B & 0.497 & 0.436 & +0.058 & [$-$0.07, +0.20] & 0.185 & No \\
817	OT-7B & 0.446 & 0.263 & +0.181 & [+0.08, +0.29] & ${<}0.001$ & Yes \\
818	R1-32B & 0.588 & 0.475 & +0.117 & [$-$0.00, +0.24] & 0.042 & No \\
819	QwQ-32B & 0.545 & 0.454 & +0.094 & [$-$0.07, +0.28] & 0.132 & No \\
820	\bottomrule
821	\end{tabular}}
822	\end{table}
823	
824	\begin{figure}[htbp]
825	\centering
826	\includegraphics[width=\columnwidth]{figures/fig_forest_precision.pdf}
827	\caption{Forest plot of HS precision advantage over text probes. Blue: vs.\ MiniLM-384d; orange: vs.\ BGE-1024d. Solid markers: survives Holm-Bonferroni; hollow: does not. All 384d comparisons are significant (strong to qualified evidence); against BGE-1024d, only OT-7B (strong) survives correction.}
828	\label{fig:forest_precision}
829	\end{figure}
830	
831	The HS precision advantage is directionally consistent across all four models (positive $\Delta$ in every case). OT-7B shows a strong, significant advantage (+18.1pp, $p{<}0.001$, survives Holm-Bonferroni). The remaining three models do not survive Holm-Bonferroni correction; R1-32B's CI includes zero with 10{,}000 resamples, so even the individual precision test is non-significant. This is consistent with the prediction in \cref{sec:limitations} that stronger text encoders would reduce the observed gap. The pattern confirms that the HS modality advantage is genuine but partially attributable to the weakness of the 384d MiniLM baseline.
832	
833	\paragraph{Balanced accuracy and FPR.} \cref{tab:bge_ba_fpr} reports BGE-large comparisons on balanced accuracy and FPR. HS balanced accuracy advantage is directionally positive across all four models (+8.4 to +10.9pp), with 2/4 (OT-7B, R1-32B) significant under Holm-Bonferroni. FPR advantage is significant only for OT-7B. R1-8B shows an adverse FPR direction: HS FPR is 1.2pp higher (worse) than BGE ($p{=}0.564$), the only model where HS does not improve over the stronger encoder on this metric.
834	
835	\begin{table}[htbp]
836	\centering
837	\small
838	\caption{HS vs.\ BGE-large (1024d): balanced accuracy and FPR differences. Bootstrap: 10{,}000 resamples, two-sided null-centered. HB: Holm-Bonferroni correction (4 tests per metric, $\alpha{=}0.05$).}
839	\label{tab:bge_ba_fpr}
840	\resizebox{\columnwidth}{!}{%
841	\begin{tabular}{lcccccc}
842	\toprule
843	\textbf{Model} & $\Delta$\textbf{BA} & $p$ (BA) & \textbf{HB} & $\Delta$\textbf{FPR} & $p$ (FPR) & \textbf{HB} \\
844	\midrule
845	R1-8B & +8.4 & 0.029 & No & $-$1.2$^\dagger$ & 0.564 & No \\
846	OT-7B & +10.8 & 0.002 & Yes & +10.5 & ${<}0.001$ & Yes \\
847	QwQ-32B & +9.3 & 0.067 & No & +2.7 & 0.368 & No \\
848	R1-32B & +10.9 & 0.008 & Yes & +7.8 & 0.165 & No \\
849	\bottomrule
850	\end{tabular}}
851	\begin{flushleft}
852	\scriptsize $^\dagger$Adverse direction: HS FPR higher (worse) than BGE.
853	\end{flushleft}
854	\end{table}
855	
856	
857	\section{Random Projection Baseline}
858	\label{app:random_projection}
859	
860	PCA capacity matching (\cref{app:encoder_robustness}) preserves 79--92\% of variance. A natural question is whether the HS advantage depends on PCA's structure-preserving property. We project hidden states to 384d using Gaussian random projection (3 seeds, averaged) and compare with text embeddings at the same dimensionality (\cref{tab:random_projection}).
861	
862	\begin{table}[htbp]
863	\centering
864	\small
865	\caption{Random projection (RP, 384d) vs.\ text (384d MiniLM). All $p < 0.001$ (1{,}000 bootstrap resamples). R1-8B uses $W{=}15$ (\cref{tab:hs_vs_text}: $W{=}3$); QwQ-32B evaluated at L60 (\cref{tab:hs_vs_text}: L63). 60/20/20 split.}
866	\label{tab:random_projection}
867	\resizebox{\columnwidth}{!}{%
868	\begin{tabular}{lcccc}
869	\toprule
870	\textbf{Model} & \textbf{RP Prec} & \textbf{Text Prec} & $\Delta$\textbf{Prec} & $\Delta$\textbf{BA} \\
871	\midrule
872	R1-8B & .621 & .416 & +.205 & +.140 \\
873	OT-7B & .371 & .244 & +.127 & +.128 \\
874	QwQ-32B & .563 & .391 & +.172 & +.132 \\
875	R1-32B & .524 & .441 & +.083 & +.085 \\
876	\bottomrule
877	\end{tabular}}
878	\end{table}
879	
880	All four models retain significant HS advantage under random projection ($\Delta$Prec +8.3 to +20.5pp), with cross-seed standard deviations below 1.7pp. RP precision is slightly lower than PCA-384d (expected, as PCA preserves maximal variance), but the gap is small. The small gap weakens a pure capacity explanation: even a structure-destroying projection preserves the HS advantage. The safety signal appears broadly distributed across hidden-state dimensions rather than concentrated in top principal components.
881	
882	
883	\section{LLM-Based Text Encoder Comparison}
884	\label{app:e5_mistral}
885	
886	To test whether an LLM-based text encoder closes the HS advantage gap, we encode each reasoning step with E5-Mistral-7B-Instruct~\citep{wang2024e5mistral} (4096d, reduced to 384d via PCA to match the MiniLM dimensionality). \cref{tab:e5_mistral} reports precision comparisons against HS probes at threshold-based layers.
887	
888	\begin{table}[htbp]
889	\centering
890	\small
891	\caption{HS vs.\ E5-Mistral-7B (PCA 384d) precision. HB: Holm-Bonferroni adjusted (4 tests, $\alpha{=}0.05$). MiniLM precision from \cref{tab:hs_vs_text} for reference. 60/20/20 split.}
892	\label{tab:e5_mistral}
893	\resizebox{\columnwidth}{!}{%
894	\begin{tabular}{llccccccc}
895	\toprule
896	\textbf{Model} & \textbf{Layer} & $W$ & \textbf{HS} & \textbf{E5} & \textbf{MiniLM} & $\Delta$(HS$-$E5) & $p$ & \textbf{HB} \\
897	\midrule
898	R1-8B & L14 & 3 & .630 & .480 & .416 & +15.0 & 0.001 & \checkmark \\
899	OT-7B & L16 & 3 & .446 & .321 & .244 & +12.5 & 0.009 & \checkmark \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad342883-d816-4499-af33-6e8c3e187e38",
  "isSidechain": true,
  "promptId": "b1899cf7-50e7-4ba4-a982-bccf7d2835cb",
  "agentId": "acee8d8337f321220",
  "type": "user",
  "uuid": "55bdca45-1831-423f-9abb-2d4401bab012",
  "sourceToolAssistantUUID": "ad342883-d816-4499-af33-6e8c3e187e38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-21T22:11:20.797Z_

Now let me read the remaining appendix sections that are particularly relevant for the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55bdca45-1831-423f-9abb-2d4401bab012",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
  "requestId": "req_011CbGUp8e8fa5dMvmRrRwun",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef34e590-8ec2-4508-9b70-cfecc1bf0f55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R7en6hzAA9hkGPxztro4wr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10231,
      "cache_read_input_tokens": 53868,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10231,
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

_source line 40 · 2026-05-21T22:11:22.841Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EydhZouwZ3xoviB7f6pMHo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
  "offset": 900,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef34e590-8ec2-4508-9b70-cfecc1bf0f55",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
  "requestId": "req_011CbGUp8e8fa5dMvmRrRwun",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c7ec684-d8cf-4928-9315-b93114a0293e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R7en6hzAA9hkGPxztro4wr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10231,
      "cache_read_input_tokens": 53868,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10231,
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

_source line 41 · 2026-05-21T22:11:22.846Z_

<details><summary>↩ Tool result · `toolu_01EydhZouwZ3xoviB7f6pMHo`</summary>

```text
900	R1-32B & L63 & 1 & .588 & .506 & .441 & +8.2 & 0.235 & \\
901	QwQ-32B & L63 & 5 & .515 & .447 & .391 & +6.8 & 0.368 & \\
902	\bottomrule
903	\end{tabular}}
904	\end{table}
905	
906	The HS advantage partially survives against the LLM encoder: 2/4 models (both 7--8B) retain significance after Holm-Bonferroni correction. Three text encoders form a monotonic gradient: MiniLM (22M params, 384d): 4/4 HB; E5-Mistral (7B, PCA 384d): 2/4 HB; BGE-large (335M, 1024d): 1/4 HB (\cref{app:encoder_robustness}). E5 precision consistently falls between MiniLM and HS across all models, consistent with encoder quality progressively narrowing the gap. PCA to 384d discards information from the 4096d E5 representation; the comparison controls dimensionality but not representation quality, so the true E5 advantage may be larger than reported here.
907	
908	
909	\section{Position-Residualized Probing}
910	\label{app:position_residual}
911	
912	To quantify non-positional safety signal, we regress out the normalized position $t/T$ from each hidden-state (or text-embedding) vector before training the logistic regression probe. \cref{tab:position_residual} summarizes results across all models at their optimal $W$.
913	
914	\begin{table}[htbp]
915	\centering
916	\small
917	\resizebox{\columnwidth}{!}{%
918	\begin{tabular}{lcrrrr}
919	\toprule
920	\textbf{Model} & $W$ & \textbf{HS BA} & \textbf{Resid.\ HS BA} & \textbf{Drop} & \textbf{Resid.\ Text BA} \\
921	\midrule
922	R1-8B & 15 & 0.834 & 0.669 & 16.5pp & 0.605 \\
923	R1-8B & 3 & 0.813 & 0.571 & 24.3pp & 0.534 \\
924	OT-7B & 3 & 0.732 & 0.609 & 12.3pp & 0.540 \\
925	QwQ-32B & 3 & 0.796 & 0.619 & 17.7pp & 0.582 \\
926	R1-32B & 1 & 0.756 & 0.552 & 20.4pp & 0.532 \\
927	\bottomrule
928	\end{tabular}}
929	\caption{Position-residualized probe balanced accuracy. All residualized HS probes are above chance ($p{<}0.001$). 3/4 models retain significant non-positional HS advantage over text (gap +3.7 to +6.9pp, HB corrected); R1-32B is the exception (+1.9pp, $p{=}0.914$).}
930	\label{tab:position_residual}
931	\end{table}
932	
933	Position accounts for 9--20pp of balanced accuracy depending on model and window size (R1-32B's 20.4pp drop at $W{=}1$ reflects the absence of temporal context), and all models retain non-positional signal above chance ($p{<}0.001$). Three of four models retain significant non-positional HS advantage over text after residualization (OT-7B +6.9pp, R1-8B +6.4pp at $W{=}15$, QwQ-32B +3.7pp; all HB corrected). R1-32B is the exception: residualized HS-text gap is +1.9pp ($p{=}0.914$), a pattern consistent with position mediation. Larger temporal windows reduce position dependence: R1-8B drops 24.3pp at $W{=}3$ but only 16.5pp at $W{=}15$.
934	
935	For QwQ-32B specifically, three complementary significance tests confirm the residualized probe performs above chance: Wilcoxon signed-rank $p{=}0.0024$, paired $t$-test $p{=}0.0008$, permutation test $p{<}0.001$ (bootstrap 95\% CI for per-trace BA: $[0.575, 0.744]$). The position baseline achieves higher balanced accuracy (0.832 vs.\ HS 0.796), and HS precision (+4.5pp, $p{=}0.133$) and FPR (+2.5pp, $p{=}0.279$) margins over the position baseline are not statistically significant at $n{=}19$.
936	
937	\paragraph{Non-linear position terms.}
938	To test whether non-linear position effects drive the HS advantage, we repeat the residualization with both linear ($t/T$) and quadratic ($[t/T, (t/T)^2]$) regressors (\cref{tab:position_quadratic}). Both 7--8B models retain significant residualized advantages under either specification. R1-32B remains non-significant under both. QwQ-32B's residualized advantage survives linear control (+7.4pp, HB) but is fully absorbed by the quadratic term ($-$1.0pp), indicating a non-linear position component in its HS advantage.
939	
940	\begin{table}[htbp]
941	\centering
942	\small
943	\resizebox{\columnwidth}{!}{%
944	\begin{tabular}{lcccc}
945	\toprule
946	\textbf{Model} & \textbf{Lin.\ gap} & \textbf{Quad.\ gap} & \textbf{Lin.\ HB} & \textbf{Quad.\ HB} \\
947	\midrule
948	R1-8B & +10.4pp & +10.3pp & \checkmark & \checkmark \\
949	OT-7B & +11.4pp & +9.8pp & \checkmark & \checkmark \\
950	R1-32B & $-$1.4pp & +0.0pp & $\times$ & $\times$ \\
951	QwQ-32B & +7.4pp & $-$1.0pp & \checkmark & $\times$ \\
952	\bottomrule
953	\end{tabular}}
954	\caption{Linear vs.\ quadratic position residualization (residualized HS$-$text gap, L60 for QwQ-32B). Both 7--8B models are robust to either specification. QwQ-32B's advantage survives linear but not quadratic control; R1-32B is non-significant under both.}
955	\label{tab:position_quadratic}
956	\end{table}
957	
958	Note: gaps in \cref{tab:position_quadratic} are precision-weighted at per-model optimal layers, whereas \cref{tab:position_residual} reports balanced-accuracy gaps; the difference reflects the metric and layer configuration, not methodological inconsistency.
959	
960	\paragraph{Effect size.} Standardized effect sizes (Cohen's $d$, residualized per-trace BA vs.\ chance 0.5): R1-8B $d{=}2.37$ ($n{=}43$, very large), QwQ-32B $d{=}0.85$ ($n{=}19$, large). Both exceed the conventional ``large'' threshold of $d{=}0.8$~\citep{cohen1988statistical}, confirming that the residualized HS signal is practically meaningful despite sample limitations at 32B.
961	
962	\section{Hyperparameter Robustness}
963	\label{app:hyperparameter_robustness}
964	
965	The joint search space for layer (${\leq}64$), window $W$ (7 values), consecutive-crossing threshold $K$ (5 values), and decision threshold is large (up to 2{,}240 configurations per model). This raises the concern that reported performance reflects overfitting to small validation sets ($n{=}4$--$9$ per class at 32B). Three analyses address this concern.
966	
967	\paragraph{Threshold-based metrics converge to a deep-layer band.}
968	Despite the large search space, three of four threshold-based metrics (precision, inverse FPR, additive composite) independently select L63 (98\% depth) for both 32B models (\cref{tab:layer_selection}). A joint (layer, $W$) grid search over 192 configurations confirms that L63 is near-optimal for QwQ-32B at recommended windows (\cref{tab:joint_layer_w}). For R1-32B, layers L55--L63 at $W{=}1$ form a robust band where all 3/3 metrics pass Holm-Bonferroni (\cref{app:layer_sweep}). The convergence of independent metrics to a narrow band is inconsistent with overfitting, which would produce scattered selections.
969	
970	\paragraph{BA-optimal layer instability is the finding, not a confound.}
971	Five-fold cross-validation on 32B validation sets reveals that balanced-accuracy-optimal layers are highly unstable across folds (\cref{tab:fold_ba_layers}). This instability is not a limitation of the study but the central methodological finding: BA-layer selection is sensitive to data composition, and conclusions drawn from any single BA-optimal layer are unreliable. Despite per-fold instability, mean BA across folds peaks near L47--L50 for both models, consistent with the LOO-CV dominant layers (\cref{app:layer_sweep}). The HS advantage holds at both BA-optimal and precision-optimal layers regardless of depth (14/16 per-model tests pass HB; \cref{app:ba_layer_comparison}).
972	
973	\begin{table}[htbp]
974	\centering
975	\small
976	\caption{BA-optimal layer per fold (5-fold CV, 32B models). Per-fold selections span 24 layers, but mean-BA landscape peaks are stable.}
977	\label{tab:fold_ba_layers}
978	\resizebox{\columnwidth}{!}{%
979	\begin{tabular}{lccccccc}
980	\toprule
981	\textbf{Model} & \textbf{F1} & \textbf{F2} & \textbf{F3} & \textbf{F4} & \textbf{F5} & \textbf{Spread} & \textbf{Mean-BA best} \\
982	\midrule
983	QwQ-32B & L63 & L51 & L39 & L44 & L44 & 24 layers & L50 \\
984	R1-32B & L53 & L45 & L40 & L63 & L39 & 24 layers & L47 \\
985	\bottomrule
986	\end{tabular}}
987	\end{table}
988	
989	\paragraph{Bootstrap CIs quantify statistical uncertainty.}
990	For the most fragile result (R1-8B FPR), bias-corrected accelerated (BCa) bootstrap~\citep{efron1993bootstrap,carpenter2000bootstrap} yields a 95\% CI of [0.006, 0.159] ($p{=}0.033$), with 12\% leave-one-out instability (\cref{app:multi_seed}). The CI excludes zero and confirms significance despite seed fragility. CP annotation perturbation (\cref{tab:cp_perturbation}) further shows that $\pm 2$-step label noise changes BA by ${<}2.5$pp, so annotation uncertainty does not compound with hyperparameter selection.
991	
992	\paragraph{Effective degrees of freedom.}
993	The full exploration space (5 metrics $\times$ 7 windows $\times$ 25--64 layers $=$ up to 2{,}240 configurations) far exceeds the 12 final HB-corrected tests. This does not constitute 2{,}240 independent hypothesis tests because layer and window are selected on the validation set before test-set evaluation, a standard train/validate/test protocol, not post-hoc cherry-picking on test outcomes. The effective degrees of freedom lie between 12 (final tests) and 2{,}240 (full grid), a ``garden of forking paths'' concern~\citep{gelman2013garden}. Three safeguards bound this risk: (1)~nested 5-fold CV on 7--8B models shows 13--25\% shrinkage relative to holdout estimates (\cref{app:nested_cv}), quantifying overfitting; (2)~split-half replication on OT-7B confirms the HS advantage on independent data halves (\cref{app:split_half}); (3)~threshold-based metric convergence to a narrow layer band (L63 for both 32B models) is inconsistent with scattered overfitting selections. We acknowledge that cumulative researcher degrees of freedom are substantial and that the 12-test HB boundary may underestimate Type~I error.
994	
995	\subsection{Nested Cross-Validation}
996	\label{app:nested_cv}
997	
998	The holdout estimates in \cref{tab:hs_vs_text} select layer and window on the validation fold, then evaluate on a fixed test set. To rule out hyperparameter overfitting, we run nested 5-fold cross-validation on both 7--8B models: the outer fold holds out test data; the inner loop selects (layer, $W$) on the remaining four folds. \cref{tab:nested_cv} reports per-fold precision differences.
999	
1000	\begin{table}[htbp]
1001	\centering
1002	\small
1003	\caption{Nested 5-fold CV: per-fold HS$-$text precision difference (pp). Layer and $W$ selected independently per fold. All 10/10 folds favor HS.}
1004	\label{tab:nested_cv}
1005	\setlength{\tabcolsep}{4pt}
1006	\resizebox{\columnwidth}{!}{%
1007	\begin{tabular}{lcccccccc}
1008	\toprule
1009	\textbf{Model} & \textbf{F1} & \textbf{F2} & \textbf{F3} & \textbf{F4} & \textbf{F5} & \textbf{Mean} & \textbf{Holdout} & \textbf{Shrink.} \\
1010	\midrule
1011	R1-8B & +22.1 & +14.4 & +17.5 & +17.0 & +16.0 & $+17.4 \pm 2.6$ & +20.1 & 13\% \\
1012	OT-7B & +13.2 & +21.4 & +18.8 & +12.6 & +15.8 & $+16.4 \pm 3.3$ & +21.9 & 25\% \\
1013	\bottomrule
1014	\end{tabular}}
1015	\begin{flushleft}
1016	\scriptsize R1-8B selected layers: L12, L12, L12, L13, L14; $W_\text{HS}$: 3, 3, 5, 5, 3. OT-7B selected layers: L23, L21, L27, L26, L26 (75--96\% depth); $W_\text{HS}$: 5, 5, 5, 5, 5.
1017	\end{flushleft}
1018	\end{table}
1019	
1020	The HS precision advantage is consistent across all 10 folds (5/5 for each model), with mean advantages of +17.4pp (R1-8B) and +16.4pp (OT-7B). Shrinkage relative to holdout estimates is 13\% and 25\% respectively, within expected ranges for validation-selected hyperparameters. R1-8B layer selection is stable (L12--L14, 38--44\% depth), consistent with all five metrics agreeing on L14 in the main analysis. OT-7B nested CV selects L21--L27 (75--96\% depth), deeper than the CR-composite-selected L16 (57\%) used in the main text. The discrepancy between CR-composite-selected (L16) and precision-selected (L21--L27) layers further illustrates the metric-dependence of layer selection documented in \cref{sec:layer-results}.
1021	
1022	\paragraph{Formal test.} A one-sided Wilcoxon signed-rank test on the 5-fold $\Delta$precision (HS$-$text) rejects $H_0{:}\;\Delta{=}0$ for both models ($W{=}15$, $p{=}0.031$; the minimum achievable $p$-value at $n{=}5$). Layer selection entropy across folds is $H{=}1.37$ bits for R1-8B (normalized 0.59; dominated by L12 in 3/5 folds) and $H{=}1.92$ bits for OT-7B (normalized 0.83; L21--L27), indicating moderately stable layer selection for R1-8B and higher variability for OT-7B.
1023	
1024	\section{Multi-Seed Stability}
1025	\label{app:multi_seed}
1026	
1027	\cref{tab:multi_seed} reports LR probe performance across 5 random seeds at each model's threshold-based layer and optimal $W$.
1028	
1029	\begin{table}[htbp]
1030	\centering
1031	\small
1032	\caption{LR probe stability across 5 random seeds (threshold-based layers, optimal $W$). 7--8B models are stable; R1-32B shows high variance due to small sample ($n{=}20$).}
1033	\label{tab:multi_seed}
1034	\resizebox{\columnwidth}{!}{%
1035	\begin{tabular}{lccc}
1036	\toprule
1037	\textbf{Model} & \textbf{Precision} & \textbf{Bal.\ Acc} & \textbf{FPR} \\
1038	\midrule
1039	R1-8B & $0.590 \pm 0.072$ & $0.756 \pm 0.028$ & $0.154 \pm 0.026$ \\
1040	OT-7B & $0.421 \pm 0.034$ & $0.633 \pm 0.023$ & $0.157 \pm 0.021$ \\
1041	QwQ-32B & $0.651 \pm 0.099$ & $0.731 \pm 0.028$ & $0.133 \pm 0.032$ \\
1042	R1-32B & $0.594 \pm 0.128$ & $0.692 \pm 0.056$ & $0.207 \pm 0.145$ \\
1043	\bottomrule
1044	\end{tabular}}
1045	\end{table}
1046	
1047	R1-32B's high FPR variance (std $= 0.145$) reflects a single outlier seed (FPR $= 0.48$), amplified by the small test set ($n{=}20$). Note that R1-32B's absolute precision std (12.8pp) differs markedly from its paired $\Delta$Prec std (2.0pp): HS and text precision covary across seeds.
1048	
1049	\paragraph{5-seed Holm-Bonferroni pass rates.} \cref{tab:seed_hb} reports HB pass rates per model across 5 seeds. Overall, 18/20 (90\%) model-seed combinations pass full HB (3/3 metrics).
1050	
1051	\begin{table}[htbp]
1052	\centering
1053	\small
1054	\caption{5-seed HB pass rates (3/3 metrics per seed). R1-8B failures are FPR-specific.}
1055	\label{tab:seed_hb}
1056	\resizebox{\columnwidth}{!}{%
1057	\begin{tabular}{lccc}
1058	\toprule
1059	\textbf{Model} & \textbf{HB Pass} & \textbf{Mean $\Delta$Prec $\pm$ std} & \textbf{Note} \\
1060	\midrule
1061	OT-7B & 5/5 & $+20.9 \pm 1.3$pp & Cleanest evidence \\
1062	R1-32B & 5/5 & $+13.7 \pm 2.0$pp & Position-mediated \\
1063	QwQ-32B & 5/5 & $+19.9 \pm 2.5$pp & Robust \\
1064	R1-8B & 3/5 & $+14.6 \pm 4.5$pp & FPR seed-fragile \\
1065	\bottomrule
1066	\end{tabular}}
1067	\end{table}
1068	
1069	\paragraph{R1-8B FPR per-seed breakdown.} \cref{tab:r18b_fpr_seeds} reports per-seed HS vs.\ text FPR comparisons for R1-8B. The HS advantage is directionally consistent (5/5 seeds), with 2/5 reaching $p{<}0.05$ uncorrected; after Bonferroni correction for 5 seeds ($\alpha{=}0.01$), 1/5 remains significant. Text FPR is highly stable (std $= 0.007$) while HS FPR is split-sensitive (std $= 0.040$), which explains why the canonical-split FPR advantage ($-7.4$pp) does not generalize robustly across seeds.
1070	
1071	\begin{table}[htbp]
1072	\centering
1073	\small
1074	\caption{R1-8B FPR per-seed comparison (L14, $W{=}15$; main text \cref{tab:hs_vs_text} reports $W{=}3$ after 5-seed validation). Direction is consistent (5/5 HS $\leq$ Text); 2/5 reach $p{<}0.05$ uncorrected, 1/5 after Bonferroni correction (5 seeds, $\alpha{=}0.01$).}
1075	\label{tab:r18b_fpr_seeds}
1076	\resizebox{\columnwidth}{!}{%
1077	\begin{tabular}{ccccc}
1078	\toprule
1079	\textbf{Seed} & \textbf{HS FPR} & \textbf{Text FPR} & $\Delta$\textbf{FPR} & $p$ \\
1080	\midrule
1081	0 & 0.161 & 0.165 & $-$0.004 & 0.440 \\
1082	1 & 0.061 & 0.166 & $-$0.105 & ${<}0.001$ \\
1083	2 & 0.123 & 0.176 & $-$0.053 & 0.093 \\
1084	3 & 0.148 & 0.167 & $-$0.018 & 0.293 \\
1085	4 & 0.100 & 0.176 & $-$0.076 & 0.021 \\
1086	\midrule
1087	mean$\pm$std & $0.119 \pm 0.040$ & $0.170 \pm 0.007$ & $-$0.051 & -- \\
1088	\bottomrule
1089	\end{tabular}}
1090	\end{table}
1091	
1092	\paragraph{R1-8B per-metric HB pass rates.} \cref{tab:r18b_metric_hb} reports Holm-Bonferroni pass rates per metric across 5 seeds for R1-8B, the model classified as ``moderate'' evidence due to FPR instability.
1093	
1094	\begin{table}[htbp]
1095	\centering
1096	\small
1097	\caption{R1-8B per-metric$\times$seed HB pass rates. Precision is robust (5/5); FPR is fragile (3/5). FPR std across seeds is 0.040 vs.\ text FPR std 0.007, consistent with a proportion near boundary (${\sim}$12\%) amplified at $n{=}43$.}
1098	\label{tab:r18b_metric_hb}
1099	\resizebox{\columnwidth}{!}{%
1100	\begin{tabular}{lccc}
1101	\toprule
1102	\textbf{Seed} & $\Delta$\textbf{Prec HB} & $\Delta$\textbf{BA HB} & $\Delta$\textbf{FPR HB} \\
1103	\midrule
1104	0 & \checkmark & \checkmark & $\times$ \\
1105	1 & \checkmark & \checkmark & \checkmark \\
1106	2 & \checkmark & \checkmark & $\times$ \\
1107	3 & \checkmark & \checkmark & \checkmark \\
1108	4 & \checkmark & \checkmark & \checkmark \\
1109	\midrule
1110	Pass rate & 5/5 & 5/5 & 3/5 \\
1111	\bottomrule
1112	\end{tabular}}
1113	\end{table}
1114	
1115	The FPR instability has a clear source: R1-8B text FPR clusters tightly around 17\% (std${=}0.7$pp) while HS FPR ranges from 6.1\% to 16.1\% (std${=}4.0$pp). Seeds where HS FPR happens to be high ($>$14\%) lose significance because the gap against text narrows below the detection threshold at $n{=}43$. This instability is metric-specific and does not affect the precision or balanced accuracy advantage, which passes all 5 seeds.
1116	
1117	\paragraph{R1-32B per-seed breakdown.} \cref{tab:r132b_seeds} reports the full per-seed breakdown for R1-32B. Seed 0 is an outlier (FPR $= 0.483$), driven by test-set trace allocation at $n{=}20$. Excluding seed 0, FPR std drops from 0.145 to 0.046.
1118	
1119	\begin{table}[htbp]
1120	\centering
1121	\small
1122	\caption{R1-32B per-seed performance (L63, $W{=}1$). Seed 0 is an outlier driven by test-set trace allocation.}
1123	\label{tab:r132b_seeds}
1124	\resizebox{\columnwidth}{!}{%
1125	\begin{tabular}{cccc}
1126	\toprule
1127	\textbf{Seed} & \textbf{Precision} & \textbf{Bal.\ Acc} & \textbf{FPR} \\
1128	\midrule
1129	0 & 0.441 & 0.594 & 0.483 \\
1130	1 & 0.750 & 0.748 & 0.109 \\
1131	2 & 0.685 & 0.670 & 0.111 \\
1132	3 & 0.652 & 0.733 & 0.111 \\
1133	4 & 0.444 & 0.715 & 0.221 \\
1134	\midrule
1135	mean$\pm$std & $0.594 \pm 0.128$ & $0.692 \pm 0.056$ & $0.207 \pm 0.145$ \\
1136	\bottomrule
1137	\end{tabular}}
1138	\end{table}
1139	
1140	
1141	\subsection{Split-Half Internal Validity (OT-7B)}
1142	\label{app:split_half}
1143	
1144	To assess internal validity, we split OT-7B traces into two independent halves and repeat the full layer sweep on each. Both halves reproduce the core pattern: crossing rate selects L0 (shallow) while precision selects mid-to-deep layers (L20 and L26 respectively). The HS precision advantage is consistent across halves ($\Delta$Prec = +0.262 and +0.154), and 4/4 checkpoints (2 halves $\times$ 2 metrics) pass, confirming the metric-induced divergence is not an artifact of a particular data partition (\cref{tab:split_half_ot7b}).
1145	
1146	\begin{table}[htbp]
1147	\centering
1148	\small
1149	\caption{Split-half internal validity on OT-7B. Both halves reproduce CR$\to$shallow / threshold$\to$deep divergence with consistent HS advantage direction.}
1150	\label{tab:split_half_ot7b}
1151	\resizebox{\columnwidth}{!}{%
1152	\begin{tabular}{lcccc}
1153	\toprule
1154	\textbf{Half} & \textbf{CR layer} & \textbf{Prec.\ layer} & $\Delta$\textbf{Prec} & $\Delta$\textbf{BA} \\
1155	\midrule
1156	A ($n{=}24$) & L0 & L20 & +0.262 & +0.128 \\
1157	B ($n{=}23$) & L0 & L26 & +0.154 & +0.092 \\
1158	\bottomrule
1159	\end{tabular}}
1160	\end{table}
1161	
1162	
1163	\section{BA-Layer Modality Comparison}
1164	\label{app:ba_layer_comparison}
1165	
1166	To address the concern that threshold-based layer selection may circularly favor HS probes, we repeat the modality comparison at layers selected by pure balanced accuracy, a threshold-free metric (\cref{tab:ba_layer_results}). BA-optimal layers vary widely across models (7--98\% depth), itself demonstrating that layer selection is a consequential methodological choice. The HS advantage is significant at whichever layer BA selects (14/16 per-model HB, two FPR failures from underpowered 32B test sets $n{\leq}20$).
1167	
1168	\begin{table}[htbp]
1169	\centering
1170	\small
1171	\caption{HS vs.\ text at BA-selected layers (60/20/20 split, same as main results). 14/16 per-model tests pass Holm-Bonferroni ($\alpha{=}0.05$); two FPR failures from underpowered 32B sets. BA-L: layer selected by pure balanced accuracy. Depth varies from 7\% to 98\%.}
1172	\label{tab:ba_layer_results}
1173	\setlength{\tabcolsep}{3pt}
1174	\resizebox{\columnwidth}{!}{%
1175	\begin{tabular}{lccccc}
1176	\toprule
1177	\textbf{Model} & \textbf{BA-L} & $\Delta$\textbf{Prec} & $\Delta$\textbf{BA} & $\Delta$\textbf{FPR} & $\Delta$\textbf{AUROC} \\
1178	\midrule
1179	R1-8B & L17 & +18.6 ($<$.001) & +8.4 (.006) & $-$7.0 (.043) & +12.1 (.009) \\
1180	OT-7B & L2 & +18.5 ($<$.001) & +8.0 (.006) & $-$13.3 ($<$.001) & +12.8 (.003) \\
1181	QwQ-32B$^\dagger$ & L63 & +18.1 (.001) & +13.5 ($<$.001) & $-$6.4 (.088) & +15.1 (.001) \\
1182	R1-32B$^\dagger$ & L46 & +12.8 (.014) & +17.6 ($<$.001) & $-$12.2 (.083) & +15.1 (.009) \\
1183	\bottomrule
1184	\end{tabular}}
1185	\begin{flushleft}
1186	\scriptsize Values: difference in pp ($p$-value, bootstrap, 10{,}000 resamples). $\dagger$\,Sample-limited ($n \leq 20$).
1187	\end{flushleft}
1188	\end{table}
1189	
1190	Of 16 per-model tests (4 models $\times$ 4 metrics), 14 pass Holm-Bonferroni correction. The precision gains (+12.8 to +18.6pp) are comparable to those at threshold-based layers (+15.4 to +21.9pp; \cref{tab:hs_vs_text}), so the HS advantage is robust to the choice of layer selection criterion. The two failures are both FPR at 32B: R1-32B ($p{=}0.083$) and QwQ-32B ($p{=}0.088$), consistent with the underpowered test sets ($n{\leq}20$) noted throughout. BA-optimal depths span 7\% (OT-7B L2) to 98\% (QwQ-32B L63), in contrast to threshold-based layers that consistently select deep layers (94--98\%). That BA selection produces such depth variation while preserving significant HS advantage reinforces the core methodological finding: the advantage is genuine rather than an artifact of any particular layer selection criterion.
1191	
1192	
1193	\subsection{AUROC Layer Selection}
1194	\label{app:auroc_layer}
1195	
1196	AUROC is threshold-free and thus orthogonal to the threshold-based metrics used in our main analysis. We include it as a reference point for layer selection (\cref{tab:auroc_layer}).
1197	
1198	\begin{table}[htbp]
1199	\centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c7ec684-d8cf-4928-9315-b93114a0293e",
  "isSidechain": true,
  "promptId": "b1899cf7-50e7-4ba4-a982-bccf7d2835cb",
  "agentId": "acee8d8337f321220",
  "type": "user",
  "uuid": "5d3d507d-0487-4ea8-a734-ece41452fe6f",
  "sourceToolAssistantUUID": "8c7ec684-d8cf-4928-9315-b93114a0293e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-21T22:11:27.078Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AxCn7DGmDZWDQPdHQwtNKm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
  "offset": 1200,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d3d507d-0487-4ea8-a734-ece41452fe6f",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
  "requestId": "req_011CbGUpscXmQZmukXVP4gWq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd3e0e9f-ab42-447f-adcc-cee722b495cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PzddMV17M9UJ47CP7Ki9Gq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9247,
      "cache_read_input_tokens": 64099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9247,
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

_source line 43 · 2026-05-21T22:11:27.084Z_

<details><summary>↩ Tool result · `toolu_01AxCn7DGmDZWDQPdHQwtNKm`</summary>

```text
1200	\small
1201	\caption{AUROC-optimal vs.\ threshold-based layer selection. AUROC selects mid-depth layers for 32B models (${\sim}$50\%), diverging from threshold-based deep layers ($>$90\%). PCA-256 applied to 32B models for tractability.}
1202	\label{tab:auroc_layer}
1203	\setlength{\tabcolsep}{3pt}
1204	\resizebox{\columnwidth}{!}{%
1205	\begin{tabular}{lcccccc}
1206	\toprule
1207	\textbf{Model} & \textbf{AUROC-L} & \textbf{Depth} & \textbf{AUROC} & \textbf{Thresh-L} & \textbf{Depth} & \textbf{AUROC@Thresh-L} \\
1208	\midrule
1209	R1-8B & L13 & 41\% & 0.806 & L14 & 44\% & 0.803 \\
1210	OT-7B & L1 & 4\% & 0.777 & L16 & 57\% & 0.746 \\
1211	QwQ-32B$^\dagger$ & L32 & 50\% & 0.839 & L60 & 94\% & 0.756 \\
1212	R1-32B$^\dagger$ & L31 & 48\% & 0.897 & L63 & 98\% & 0.767 \\
1213	\bottomrule
1214	\end{tabular}}
1215	\begin{flushleft}
1216	\scriptsize $\dagger$\,PCA-256 applied. AUROC-L: layer maximizing validation AUROC. Thresh-L: layer from threshold-based selection (\cref{tab:layer_selection}).
1217	\end{flushleft}
1218	\end{table}
1219	
1220	AUROC does not converge to the same deep layers as threshold-based metrics. For 32B models, AUROC prefers mid-depth layers (${\sim}$50\% depth) vs.\ threshold-based deep layers ($>$90\%). R1-8B is a near-match (L13 vs.\ L14). We exclude AUROC from the main analysis because it is threshold-free and cannot diagnose the threshold-crossing artifacts central to our layer selection bias finding, but it provides an independent reference confirming that optimal layer depth is metric-dependent.\looseness=-1
1221	
1222	\subsection{Effective Independent Tests}
1223	\label{app:effective_tests}
1224	
1225	The raw exploration space (${\sim}$5 metrics $\times$ 7 windows $\times$ 28--64 layers) nominally spans 980--2{,}240 configurations per model, raising a multiple-comparisons concern. The effective number of independent tests is substantially smaller for three reasons:
1226	
1227	\paragraph{Metric redundancy.} Precision, inverse FPR, and the additive composite share a single confusion matrix: they are deterministic functions of the same TP/FP/FN/TN counts. Empirically, their layer rankings have Kendall $\tau \geq 0.85$ across all four models (\cref{tab:layer_selection}). BA is computed from the same confusion matrix but weights errors differently; it independently confirms deep-layer selection. Crossing rate is the only structurally distinct metric (computed from threshold-crossing sequences, not the confusion matrix). Thus five nominal metrics reduce to ${\sim}$2 independent metric families (threshold-based and crossing-rate).
1228	
1229	\paragraph{Layer autocorrelation.} Adjacent transformer layers produce highly correlated probe scores: for R1-8B, the median Pearson $r$ between layers $\ell$ and $\ell{\pm}1$ exceeds 0.95. Using a lag-1 autocorrelation estimate~\citep{efron1993bootstrap}, the effective number of independent layers is ${\sim}$8--12 per model (vs.\ 28--64 nominal).
1230	
1231	\paragraph{Two-stage protection.} The upstream exploration (layer $\times$ window $\times$ metric) is conducted entirely within the training/validation split via nested CV at 7--8B (\cref{app:nested_cv}) and split-half replication (\cref{app:split_half}). The held-out test set sees only the 12 final modality comparisons (3 metrics $\times$ 4 models), to which Holm-Bonferroni correction is applied. The upstream search inflates Type I risk only if it overfits the validation set; nested CV guards against this at 7--8B, while 32B results are marked exploratory ($\dagger$) precisely because this guard is unavailable.
1232	
1233	\paragraph{Conditional inference.} The two-stage design means that test-set $p$-values are conditional on the layer and window selected during upstream search. This selective inference is valid when the selection and evaluation splits are independent (ensured by our 60/20/20 partition), but the resulting $p$-values measure significance given the chosen selection path rather than significance averaged over all possible paths. Nested CV at 7--8B (\cref{app:nested_cv}) addresses this by averaging over fold-specific selection paths; the 32B exploratory status ($\dagger$) reflects the absence of this protection.
1234	
1235	\paragraph{Effect sizes.} Cohen's $d$ (one-sample, $d = (\overline{\text{BA}} - 0.5) / s$) quantifies effect magnitude independently of sample size: R1-8B $d{=}2.37$ (very large, $n{=}43$), OT-7B $d{=}1.12$ (large, $n{=}47$), QwQ-32B$^\dagger$ $d{=}0.85$ (large, $n{=}19$), R1-32B$^\dagger$ $d{=}0.58$ (medium, $n{=}20$). The 7--8B models exceed the ``very large'' threshold ($d{>}1.2$); both 32B models exceed the ``medium'' threshold ($d{>}0.5$). R1-32B's medium effect size is consistent with its exploratory status and the position-mediation pattern noted in \cref{sec:32b-analysis}. These effect sizes argue against a pure multiple-comparisons explanation: fishing artifacts produce small, unstable effects, whereas the observed $d$ values are large and graded across the evidence tiers.\looseness=-1
1236	
1237	\section{Post-Hoc Power Analysis}
1238	\label{app:power_analysis}
1239	
1240	We compute post-hoc minimum detectable effects (MDEs) at 80\% power for each model's test set to contextualize non-significant results, particularly at 32B scale where sample sizes are small (\cref{tab:power_analysis}).
1241	
1242	\begin{table}[htbp]
1243	\centering
1244	\small
1245	\caption{Post-hoc power analysis. MDE: minimum detectable effect (balanced accuracy, pp) at 80\% power given each model's test-set size and observed variance. Effects smaller than the MDE cannot be reliably detected.}
1246	\label{tab:power_analysis}
1247	\resizebox{\columnwidth}{!}{%
1248	\begin{tabular}{lccc}
1249	\toprule
1250	\textbf{Model} & $n_{\text{test}}$ & \textbf{Obs.\ std (BA)} & \textbf{MDE (80\%)} \\
1251	\midrule
1252	R1-8B & 43 & 0.028 & 4.2pp \\
1253	OT-7B & 47 & 0.023 & 3.3pp \\
1254	QwQ-32B$^\dagger$ & 19 & 0.028 & 8.6pp \\
1255	R1-32B$^\dagger$ & 20 & 0.056 & 9.5pp \\
1256	\bottomrule
1257	\end{tabular}}
1258	\begin{flushleft}
1259	\scriptsize $\dagger$\,Sample-limited. MDE computed from 5-seed observed standard deviation via two-sided paired $t$-test formula.
1260	\end{flushleft}
1261	\end{table}
1262	
1263	At 32B scale, the MDE is 8.6--9.5pp, meaning effects below this magnitude cannot be reliably distinguished from noise. R1-32B's residualized HS-text gap (+1.9pp) falls well below the MDE (9.5pp), so the non-significant result (\cref{app:position_residual}) is consistent with either a true null or an underpowered test. The 7--8B MDEs (3.3--4.2pp) are substantially lower, explaining why smaller effects reach significance at these scales.
1264	
1265	\subsection{Multi-Metric Layer Ensemble}
1266	\label{app:ensemble}
1267	
1268	For each model, we train logistic regression probes at the best layer selected by each of three threshold-based metrics (precision, BA, inverse FPR) and average their predicted probabilities to produce an ensemble score. This eliminates the need to pre-select a single metric for layer selection.
1269	
1270	\begin{table}[htbp]
1271	\centering
1272	\small
1273	\caption{Multi-metric layer ensemble vs.\ best single metric and text baseline. Ensemble trains probes at 3 threshold-based metric-selected layers and averages probabilities. $\Delta$Ens--Best: ensemble minus best single metric (negative = ensemble slightly lower). All Ens--Text differences are significant ($p \leq 0.002$, permutation test). No Ens--Best difference is significant ($p > 0.27$).}
1274	\label{tab:ensemble}
1275	\resizebox{\columnwidth}{!}{%
1276	\begin{tabular}{lcccc}
1277	\toprule
1278	\textbf{Model} & \textbf{Ens Prec} & \textbf{Best Single} & $\Delta$ & \textbf{Ens$-$Text} \\
1279	\midrule
1280	R1-8B & 0.565 & 0.604 (BA@L12) & $-$3.9pp & +19.3pp \\
1281	OT-7B & 0.506 & 0.473 (FPR@L18) & +3.3pp & +27.0pp \\
1282	QwQ-32B & 0.578 & 0.578 (Prec@L60) & $-$0.0pp & +20.3pp \\
1283	R1-32B & 0.581 & 0.583 (Prec@L63) & $-$0.2pp & +10.5pp \\
1284	\bottomrule
1285	\end{tabular}}
1286	\end{table}
1287	
1288	This ensemble is a preliminary exploration of metric-agnostic layer selection, not a validated mitigation strategy; rigorous cross-validated evaluation across diverse datasets is future work. The ensemble provides a metric-agnostic selection strategy among principled (threshold-based) metrics. It never significantly underperforms the best individual metric (all $p > 0.27$), and all four models show significant HS advantage over text ($p \leq 0.002$). The ensemble advantage over text ranges from +10.5pp (R1-32B) to +27.0pp (OT-7B). This proof of concept validates that practitioners need not commit to a single metric for layer selection; averaging across metric-selected layers achieves comparable performance. Future work should test whether including biased metrics (e.g., crossing-rate composite) in the ensemble degrades performance, and whether learned metric weighting could improve upon uniform averaging.
1289	
1290	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd3e0e9f-ab42-447f-adcc-cee722b495cb",
  "isSidechain": true,
  "promptId": "b1899cf7-50e7-4ba4-a982-bccf7d2835cb",
  "agentId": "acee8d8337f321220",
  "type": "user",
  "uuid": "92c3307f-aa78-4e60-aea3-f03af0760a99",
  "sourceToolAssistantUUID": "cd3e0e9f-ab42-447f-adcc-cee722b495cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-21T22:13:09.693Z_

I now have a thorough understanding of the paper. Let me produce the review.

## R1 Review: Methods and Experiments

### Summary

This paper studies "safety commitment point" (CP) detection in reasoning LLMs, comparing hidden-state (HS) and text probes across four models. The central methodological contribution is that layer selection metric choice can qualitatively reverse the HS-vs-text conclusion (significant to non-significant for QwQ-32B). At correctly chosen layers, HS probes show +15 to +22pp precision over 384d text probes at 7-8B (cross-validated), but this advantage is conditional on text encoder quality, diminishing from 4/4 HB at 384d to 1/4 HB at 1024d. Seven alternative detection paradigms all fail. The paper is unusually transparent about boundary conditions, researcher degrees of freedom, and the limitations of its own claims.

### Strengths

1. **Layer selection bias is a genuine and well-demonstrated contribution.** The 14-layer (R1-8B) to 61-layer (QwQ-32B) divergence depending on metric choice is convincingly demonstrated, with a clear mechanistic explanation via cosine compression at shallow layers. The random-label decomposition controls (Appendix A.2) cleanly separate the geometric artifact from the safety signal. This finding has implications beyond this specific task for anyone doing representation probing in LLMs.

2. **Exceptional honesty about evidence quality.** The three-tier evidence gradient (cross-validated / significant / exploratory) with consistent dagger marking for sample-limited results is a model of responsible reporting. The authors explicitly state that their probes "characterize the phenomenon rather than constitute production detectors" and flag 39-50% safe-trace FPR as a deployment barrier. The encoder-quality gradient (384d -> 4096d -> 1024d, 4/4 -> 2/4 -> 1/4 HB) is presented as a direct qualification of their own headline result.

3. **Statistical rigor is above the EMNLP norm.** The two-stage design (upstream exploration on validation, downstream HB on 12 final tests), nested 5-fold CV at 7-8B confirming 13-25% shrinkage, exact permutation tests for 32B models, position residualization with both linear and quadratic controls, 5-seed stability analysis, split-half replication on OT-7B, and control task selectivity collectively constitute a thorough validation apparatus. The BCa bootstrap with cluster resampling (preserving within-trace dependence) is methodologically appropriate.

4. **Comprehensive negative results.** Section 4.6 and Appendix A.14-A.16 systematically rule out seven alternatives with clear failure-mode taxonomy (graduality, variance subspace, model-specificity, capacity, objective mismatch). The cross-model transfer failure under maximally favorable conditions (PCA fitted on full data) is particularly informative.

5. **Breadth of evaluation.** The 4 models x 7 methods x 5 metrics x 7 window sizes design space is large, and the paper navigates it systematically. The appendix is extensive (~30 tables/figures) and addresses nearly every foreseeable reviewer concern.

6. **Bug disclosure (Appendix A.11).** Proactively disclosing the M002 text embedding bug is commendable and increases trust in the final results.

### Weaknesses

1. **The HS advantage is substantially weaker than the headline numbers suggest.** Table 2's "+15 to +22pp precision" headlines are against MiniLM-L6-v2, a 22M-parameter distilled encoder from 2020. Against BGE-large (1024d), only 1/4 models passes HB; against E5-Mistral (PCA-384d), only 2/4 pass. The paper acknowledges this (Section 4.3, "encoder-quality gradient"), but the abstract and introduction still lead with the 384d comparison. The honest conclusion is closer to: "HS probes outperform weak text encoders; the advantage narrows to non-significance against modern encoders for most models." This substantially reduces the practical significance of Contribution 2, since any real deployment would use a stronger encoder than MiniLM-L6-v2.

2. **Sample sizes at 32B are insufficient for the analyses attempted.** n=19-20 test traces preclude nested CV, produce MDEs of 8.6-9.5pp (Table 14), and yield dramatic seed instability (R1-32B FPR std = 0.145 with one seed at 0.483). The paper marks these as exploratory, but they still occupy substantial space in the main text (Section 4.4, Tables 3-4) and contribute to the "4 models" framing. With n=20, the 60/20/20 split gives only 12 training, 4 validation, and 4 test traces -- effectively toy-scale for any reliable conclusion. The evidence would be more cleanly communicated by framing this as a "2-model study with 2 preliminary extensions."

3. **Architecture coverage is narrow.** 3/4 models share the Qwen architecture. The random-label controls show the crossing-rate geometric bias is Qwen-specific (retained on QwQ-32B but dissolved on R1-8B), raising the question of how much of the layer selection bias finding generalizes. The paper's central claim (C1) that layer selection bias is a "robust methodological finding" rests heavily on one non-Qwen model (R1-8B), which happens to be the model where the crossing-rate and threshold-based layers agree when the full-layer sweep is restricted to L12-L24. The divergence only appears when extending to L0-L24 -- a detail that slightly weakens the universality claim.

4. **The CP definition is underspecified and circular in validation.** The CP is defined as "the first reasoning step after which safety deliberation permanently ceases," but the only annotation comes from HarmThoughts with no reported inter-annotator agreement on the primary dataset. The AdvBench IAA proxy (kappa=0.606, 37% exact CP match) uses LLM annotators, which the paper itself concludes is "insufficient for reliable CP localization." We have no evidence that the HarmThoughts human annotations are reliable. The CP perturbation analysis (Table 9 in appendix) shows <2.5pp BA change at +/-2 steps, which is reassuring, but does not address whether the CP concept itself is well-defined for traces with oscillating deliberation (acknowledged but hand-waved with "taking the final irreversible transition").

5. **Position confounding is partially unresolved.** Position accounts for 9-20pp of balanced accuracy. After linear residualization, 3/4 models retain significant HS advantage, but QwQ-32B's advantage is fully absorbed by a quadratic position term (Table in Appendix A.20). R1-32B's residualized gap is 1.9pp (well below MDE). So for the 32B models -- which are the scale where layer selection bias matters most -- the HS advantage over position is weak or absent. This means the paper's most novel finding (layer selection bias at 32B) co-occurs with the weakest evidence that HS probes capture genuinely non-positional safety information at that scale.

6. **K=5 selection on R1-8B and transfer to other models is questionable.** The consecutive-crossings threshold K=5 was "selected on the R1-8B validation set and held fixed across all models." The K-ablation (Table in Appendix A.12) shows that K interacts strongly with model properties -- at K=5, OT-7B safe FPR is 0.19 while R1-8B is 0.63. Using a K tuned on one model's validation set for cross-model evaluation is a researcher degree of freedom that the paper does not adequately justify.

### Questions for Authors

1. **Encoder fairness:** The capacity-matching controls (PCA to 384d, random projection to 384d) demonstrate that dimensionality alone does not explain the HS advantage. However, the encoder comparison conflates two factors: (a) representation quality and (b) domain relevance. MiniLM was trained on general NLI/STS data, not safety-relevant text. Have you considered fine-tuning the text encoder on a small set of safety-relevant reasoning traces, or using a text encoder specifically trained on reasoning text? If not, how can you disentangle "HS probes access different information" from "text probes use a poorly matched encoder"?

2. **Layer selection for deployment:** The multi-metric ensemble (Table in Appendix A.26) eliminates metric-dependent layer selection and significantly outperforms text in all 4 models. Why is this not the recommended method? It appears to solve the central problem the paper identifies. The "preliminary" and "lacks cross-validation" caveats seem weak given that the paper's other results also have substantial caveats.

3. **Temporal structure of the HS advantage:** The paper shows that text probes benefit proportionally more from temporal windowing (+12pp BA for text vs. +3.2pp for HS on R1-8B at W=25). This means a large fraction of the HS advantage at W=1 is because HS representations already encode temporal context implicitly. Have you analyzed whether the HS advantage at large W (where text has caught up temporally) differs qualitatively from W=1, and what this implies about the nature of the signal HS probes capture?

4. **Generalization beyond HarmThoughts:** All CP-dependent claims use one dataset with one annotation protocol. The AdvBench boundary condition (90.4% CP=0) shows the CP framework breaks down under adversarial prompts. What is the expected prevalence of "self-jailbreak" with extended deliberation in realistic deployment, and how does this affect the practical relevance of CP detection?

5. **Why not report F1?** The paper explicitly excludes F1 because it "conflates precision and recall." But precision alone also conflates information: a probe with high precision and 25% coverage (R1-32B) has very different practical value from one with moderate precision and 74% coverage (QwQ-32B). F1 or the precision-coverage tradeoff curve would be more informative for deployment assessment than precision in isolation.

### Minor Issues

1. The title ("Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models") does not mention the HS-vs-text comparison or the commitment point concept, which are arguably more central than layer selection alone.

2. Table 1's column header "p (thresh.)" is the HS-vs-text precision p-value at the threshold-based layer, but this is not immediately clear from the caption. The reader might mistake it for a test of layer selection method differences.

3. The abstract mentions "7-8B headline" but the abstract's own headline appears to be about layer selection bias, creating a framing tension.

4. Appendix sections use inconsistent numbering: some are lettered (A.1, A.2...), others use section numbers. This is a LaTeX formatting issue but makes navigation difficult.

5. The GRU experiments use a different data split (70/30) from the main results (60/20/20), with a later table using 60/20/20 for "fair comparison." The switching between protocols is confusing and raises questions about which results are directly comparable.

6. Several key details are relegated to appendices that should be in the main text: the encoder robustness gradient (Appendix A.17) and position residualization (Appendix A.20) fundamentally qualify the main claims and deserve main-text space. The current main text (Section 4.3, paragraphs on encoder robustness and position mediation) is compressed to the point of being hard to parse.

### Scores

- **Soundness: 3.5/5** -- The statistical framework is rigorous and the methodology is carefully designed. However, the HS advantage is overstated relative to the encoder-conditional evidence, position confounding is unresolved at 32B, and 32B sample sizes are inadequate for the conclusions drawn from them, even with exploratory caveats.

- **Excitement: 3.0/5** -- The layer selection bias finding is a solid methodological contribution with broad implications for representation probing. However, the practical significance is limited: (1) the HS advantage disappears against good text encoders, (2) false positive rates are too high for deployment, and (3) the task itself (CP detection in self-jailbreaking reasoning) is narrow. The paper reads more as a careful negative/cautionary result than as an advance in safety detection.

- **Reproducibility: 4.0/5** -- All hyperparameters are reported, compute budget is minimal (<4 GPU-hours), models and datasets are public, code release is promised. The multi-seed analysis, nested CV, and split-half validation all support reproducibility. Deducting slightly because HarmThoughts CP annotation quality is unvalidated.

- **Overall: 3.0/5** -- This is a Findings-quality paper. The layer selection bias contribution is genuine and the experimental rigor is above average, but the paper's scope is narrow (one dataset, one annotation protocol, mostly one architecture family), the headline HS advantage claim is substantially encoder-conditional, and the 32B results are too underpowered to support the weight placed on them. The honest framing of limitations is appreciated but does not fully compensate for the gap between the abstract's implications and the evidence's actual strength.

- **Confidence: 4.5/5** -- I have read the paper thoroughly including the full appendix, understand the statistical methods, and am familiar with representation probing methodology and LLM safety literature.

### Meta-assessment

To reach 3.5 (borderline conference), the paper would need: (1) a stronger text encoder baseline as the *primary* comparison (BGE-large or better), with MiniLM demoted to a supplementary analysis, and recalibrated claims about the HS advantage reflecting the encoder-conditional reality; (2) either larger 32B samples (n>=50, as the authors themselves suggest) or explicit restriction of all claims to 7-8B with 32B presented as a brief preliminary section; (3) at least one additional non-Qwen model (e.g., Llama-based reasoning model at 32B or a different 7B architecture) to support universality claims for layer selection bias. To reach 4.0 (Main conference), the paper would additionally need a second dataset with validated CP annotations showing the core findings replicate, and a stronger practical motivation -- either demonstrating that the HS advantage holds against state-of-the-art text encoders, or pivoting the framing entirely toward the methodological/cautionary contribution (layer selection bias) and presenting it as guidance for the probing community rather than as a safety monitoring advance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92c3307f-aa78-4e60-aea3-f03af0760a99",
  "isSidechain": true,
  "agentId": "acee8d8337f321220",
  "requestId": "req_011CbGUqBRLk4vSXoRurNov6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c52d2f37-06cf-4516-aaba-2a5b9084c2b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "eb7c9f09-21ff-4986-ae2c-11140cc85a3d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QzjqCUiSHKmVdWAWV28xEh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3211,
      "cache_read_input_tokens": 73346,
      "output_tokens": 3484,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3211
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3484,
          "cache_read_input_tokens": 73346,
          "cache_creation_input_tokens": 3211,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3211,
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
