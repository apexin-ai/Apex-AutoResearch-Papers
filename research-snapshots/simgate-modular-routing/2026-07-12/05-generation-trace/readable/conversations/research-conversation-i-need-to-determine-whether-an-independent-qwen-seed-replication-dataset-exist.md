# Research conversation: I need to determine whether an independent Qwen seed replication dataset exists for this research project (simgate-modul

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-abba625f7ac93e545.jsonl`
- **Structured JSON:** [`cc6974785237c2690db5.json`](../../sessions/cc/cc6974785237c2690db5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

34 recorded events

### User

_source line 1 · 2026-05-23T10:43:15.961Z_

I need to determine whether an independent Qwen seed replication dataset exists for this research project (simgate-modular-routing). The paper §3.1 claims "an independent seed replication (N=220) yields DAF = 89.7%" referencing Appendix seed-robustness. But Gemma cross-model also has DAF=89.7%, N=220.

Search in these locations:
1. The registry file at /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/registry.yaml - look for any experiment with "seed" in its name or ID, especially anything like "seed-replication" or "qwen-seed" with N=220
2. The appendix files in /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/ - find the appendix that discusses seed robustness (app:seed-robustness) and read what it actually describes
3. Check main.tex for the seed-robustness appendix content

Report: what exactly does the seed-robustness appendix discuss? Is there a Qwen seed replication with N=220 and DAF=89.7%? Or is this the Gemma cross-model result being mislabeled?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5c9e987c-ae70-4ee6-a464-2d2db13505c8",
  "agentId": "abba625f7ac93e545",
  "type": "user",
  "uuid": "bc9e95f6-b4c3-4ed1-807b-e595943522c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-23T10:43:17.813Z_

I'll help you investigate this. Let me search through the registry, appendix files, and main.tex to determine what the seed-robustness appendix actually contains and whether there's a Qwen seed replication dataset.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc9e95f6-b4c3-4ed1-807b-e595943522c5",
  "isSidechain": true,
  "agentId": "abba625f7ac93e545",
  "requestId": "req_011CbKMyGSdxey1BLVFQhTHg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6fd3296f-ed24-402a-b9a8-28f926444298",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BuwZUFaiQgpVRv1aFrPEgP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33550,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33550,
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

_source line 3 · 2026-05-23T10:43:18.347Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UVqEo4Y5RRs3HTGBtwDSgD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fd3296f-ed24-402a-b9a8-28f926444298",
  "isSidechain": true,
  "agentId": "abba625f7ac93e545",
  "requestId": "req_011CbKMyGSdxey1BLVFQhTHg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "34d6f880-4ee1-4ec0-a3fb-8660f9f89e25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BuwZUFaiQgpVRv1aFrPEgP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33550,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33550,
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

_source line 4 · 2026-05-23T10:43:18.496Z_

<details open><summary>🔧 Tool call — Glob · `toolu_012RWCdmpgzcyf8fr7sCiQ5A`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/*appendix*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34d6f880-4ee1-4ec0-a3fb-8660f9f89e25",
  "isSidechain": true,
  "agentId": "abba625f7ac93e545",
  "requestId": "req_011CbKMyGSdxey1BLVFQhTHg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "682bdb6b-745a-46c1-bc96-dbbd4592c5fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BuwZUFaiQgpVRv1aFrPEgP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33550,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33550,
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

_source line 5 · 2026-05-23T10:43:18.634Z_

<details><summary>↩ Tool result · reported error · `toolu_01UVqEo4Y5RRs3HTGBtwDSgD`</summary>

```text
File content (86395 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34d6f880-4ee1-4ec0-a3fb-8660f9f89e25",
  "isSidechain": true,
  "promptId": "5c9e987c-ae70-4ee6-a464-2d2db13505c8",
  "agentId": "abba625f7ac93e545",
  "type": "user",
  "uuid": "0b31486c-a932-48b8-970c-e65f620511c9",
  "toolUseResult": "Error: File content (86395 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "34d6f880-4ee1-4ec0-a3fb-8660f9f89e25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle"
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T10:43:18.517Z_

<details><summary>↩ Tool result · `toolu_012RWCdmpgzcyf8fr7sCiQ5A`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "682bdb6b-745a-46c1-bc96-dbbd4592c5fb",
  "isSidechain": true,
  "promptId": "5c9e987c-ae70-4ee6-a464-2d2db13505c8",
  "agentId": "abba625f7ac93e545",
  "type": "user",
  "uuid": "b2eb56e1-ab4d-4a9e-99fa-6860f2b117b0",
  "sourceToolAssistantUUID": "682bdb6b-745a-46c1-bc96-dbbd4592c5fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T10:43:18.912Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01SghyDveNnDzki2oN4Bf6nC`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/*seed*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2eb56e1-ab4d-4a9e-99fa-6860f2b117b0",
  "isSidechain": true,
  "agentId": "abba625f7ac93e545",
  "requestId": "req_011CbKMyGSdxey1BLVFQhTHg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "83831715-deed-4708-92b3-bf8ae435e1a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BuwZUFaiQgpVRv1aFrPEgP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33550,
      "cache_read_input_tokens": 0,
      "output_tokens": 347,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 33550
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 347,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 33550,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 33550,
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

_source line 8 · 2026-05-23T10:43:18.923Z_

<details><summary>↩ Tool result · `toolu_01SghyDveNnDzki2oN4Bf6nC`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83831715-deed-4708-92b3-bf8ae435e1a7",
  "isSidechain": true,
  "promptId": "5c9e987c-ae70-4ee6-a464-2d2db13505c8",
  "agentId": "abba625f7ac93e545",
  "type": "user",
  "uuid": "812be463-ac01-4247-ae43-55988701ac16",
  "sourceToolAssistantUUID": "83831715-deed-4708-92b3-bf8ae435e1a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T10:43:18.952Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KXJTC2HY9hVVgxqJpjyDdw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "812be463-ac01-4247-ae43-55988701ac16",
  "isSidechain": true,
  "agentId": "abba625f7ac93e545",
  "requestId": "req_011CbKMyGSdxey1BLVFQhTHg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4d5ff0e9-0f56-4486-87f5-b7f1a2076d1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BuwZUFaiQgpVRv1aFrPEgP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33550,
      "cache_read_input_tokens": 0,
      "output_tokens": 347,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 33550
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 347,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 33550,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 33550,
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

_source line 10 · 2026-05-23T10:43:19.227Z_

<details><summary>↩ Tool result · `toolu_01KXJTC2HY9hVVgxqJpjyDdw`</summary>

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
11	\graphicspath{{figures/}}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{algorithm}
16	\usepackage{algorithmic}
17	\usepackage{tcolorbox}
18	\tcbuselibrary{listings,breakable}
19	
20	\hypersetup{pdfauthor={},pdftitle={}}
21	
22	\title{Death Avoidance as the Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\input{abstract}
30	\input{introduction}
31	\input{method}
32	\input{experiments}
33	\input{related_work}
34	\input{discussion}
35	\input{conclusion}
36	
37	\section*{Limitations}
38	
39	\paragraph{Environmental scope.}
40	Our primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct), though extended validation of representative excluded tasks confirms the pattern (Appendix~\ref{app:extended-validation}). The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\ref{app:penalty}). The 19 excluded task types (63\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface non-death-dominated signal that our current setup does not capture. Cross-environment analyses on MATH and ALFWorld (\S\ref{sec:cross-env}, \S\ref{sec:discussion}) provide preliminary supporting evidence but do not conclusively establish generalization. A Llama-3.1-8B-Instruct cross-model replication (11 task types, $N{=}220$; \S\ref{sec:cross-model}) shows death dominance replicates with direction consistency 10/10 while vulnerability magnitude varies ($+30.0$~pp vs.\ Qwen $+26.5$~pp), though both models are in the 7--8B parameter range; Qwen2.5-72B ($10{\times}$ scale) reduces death rate but does not eliminate death dominance (\S\ref{sec:agent-improvement}); validation beyond 72B remains future work. The 72B probe is limited to a single model without cross-model replication at scale; whether death avoidance remains dominant for frontier models with substantially lower failure rates is an open question. Our quantitative results (DAF $= 90.4\%$, label fractions) are specific to ScienceWorld; the framework's generality claim is methodological (the diagnostic procedure applies to any environment with asymmetric fatal outcomes), not empirical (the specific percentages may differ across environments).
41	
42	\paragraph{Methodological constraints.}
43	Our internal-reasoning baseline uses single-pass ReAct~\citep{react-2023}. Reflexion~\citep{reflexion-2023} reduces death rate from 42.9\% to 31.4\% (\S\ref{sec:agent-improvement}), but more aggressive self-correction or Tree-of-Thought backtracking~\citep{tot-2023} may further reduce internal death rates. Episode-level labels assign a single routing preference to entire episodes, which may be suboptimal for individual steps (particularly those preceding death events). However, of 2{,}040 training steps only 0.3\% exhibit strict directional conflict (step-level oracle opposite to episode label); the remaining apparent mislabeling consists of episode labels applied to steps where neither strategy has a step-level advantage (60.3\% pre-event neutral). The issue is granularity mismatch (applying correct-direction labels to uninformative steps), not directional error. Training on pure-strategy trajectories also introduces distribution shift at deployment~\citep{dagger-2011}. Grounding ablation reduces but does not eliminate the death rate differential (from $+26.6$\,pp to approximately $+8$\,pp; Appendix~\ref{app:grounding-ablation}); a full post-ablation counterfactual decomposition remains important future work. Under mixed-strategy routing with oracle death prediction, switching to deterministic at the step before death could reduce the internal death rate; even under optimistic assumptions (perfect step-level death prediction), a residual gap of ${>}10$~pp between strategies is expected, as fatal trajectories involve cumulative hallucination errors preceding the death event. More broadly, projecting episode-level labels onto 10--50 sequential steps with path-dependent state introduces compounding error: early routing decisions alter the state trajectory, potentially invalidating later labels derived from the episode outcome.
44	
45	\paragraph{Statistical limitations.}
46	Episodes within the same task type are not fully independent because they share environment dynamics, though they use different random seeds. Cluster bootstrap with $K{=}11$ task-type clusters yields wider CIs ($[73.3\%, 100.0\%]$); with $K{=}11$ falling below the $K \geq 20$--$50$ threshold recommended by \citet{cameron-2008,webb-2023}, readers should rely on the non-clustered bootstrap CI ($[81.1\%, 99.0\%]$). A wild cluster bootstrap ($K{=}11$, $p < 0.001$; Appendix~\ref{app:wild-cluster}) and 100\% directional consistency across all 28 death-prone tasks (Appendix~\ref{app:per-task-ci}) mitigate this concern.
47	
48	\paragraph{Pure-strategy upper bound.}
49	Our counterfactual analysis compares pure strategies (always-internal vs.\ always-deterministic). In mixed routing, the router can selectively invoke deterministic mode on high-risk steps, potentially reducing death asymmetry. Thus, DAF${=}90.4\%$ represents an upper bound on death avoidance's contribution to optimized routing; the actual contribution under mixed strategies may be lower.
50	
51	\paragraph{Diagnostic scope.}
52	Our framework is diagnostic rather than prescriptive: it identifies what drives routing decisions but does not optimize the routing policy itself. The framework assumes binary catastrophic failure; environments with graded penalties would require modifying Algorithm~\ref{alg:labeling}'s death-priority rule to a continuous severity weighting. Extending the counterfactual decomposition to prescribe optimal mixed-strategy routing (for example, by combining DAF analysis with online policy learning) is a natural next step.
53	
54	\section*{Ethics Statement}
55	
56	This work uses ScienceWorld \citep{scienceworld-2022}, a publicly available text-based simulation environment, and does not involve human subjects or private data. All evaluation environments (ScienceWorld, ALFWorld, MATH) are released under permissive open-source licenses (Apache 2.0 / MIT). All models used (Qwen2.5 family, Llama-3.1-8B, Gemma-2-9B-it) are publicly available for research use. All language models are accessed via standard APIs or publicly released weights. Experiments were conducted on 2$\times$ NVIDIA RTX 5090 (32GB) and 4$\times$ NVIDIA RTX 6000 PRO (96GB), totaling approximately 200 GPU-hours, comprising ${\sim}$140 hours for episode collection (counterfactual inference across three 7--9B model families plus Qwen2.5-72B backbone scaling, Reflexion and retry baselines, and cross-environment validation on ALFWorld and MATH), ${\sim}$35 hours for router training (LoRA fine-tuning of Qwen3-0.6B/1.7B/4B across 4--8 seeds per scale, including augmentation and ablation variants), and ${\sim}$25 hours for evaluation and analysis. Code and data will be released upon acceptance.
57	
58	\bibliography{references}
59	
60	\appendix
61	
62	\noindent\textbf{Appendix Overview.}
63	\hyperref[app:sci]{A.~Signal Concentration Index} $\cdot$
64	\hyperref[app:labeling]{B.~Labeling Quality Audit} $\cdot$
65	\hyperref[app:per-task]{C.~Per-Task Decomposition} $\cdot$
66	\hyperref[app:correlation]{D.~Correlation Robustness} $\cdot$
67	\hyperref[app:wild-cluster]{E.~Cluster Bootstrap Sensitivity} $\cdot$
68	\hyperref[app:per-task-ci]{F.~Per-Task CIs} $\cdot$
69	\hyperref[app:loto-daf]{G.~Leave-One-Task-Out DAF} $\cdot$
70	\hyperref[app:dose-response]{H.~Dose-Response Breakdown} $\cdot$
71	\hyperref[app:router-details]{I.~Router Training Details} $\cdot$
72	\hyperref[app:seed-robustness]{J.~Seed Robustness} $\cdot$
73	\hyperref[app:penalty]{K.~Penalty Sensitivity} $\cdot$
74	\hyperref[app:cross-env-details]{L.~Cross-Environment Details} $\cdot$
75	\hyperref[app:cross-model]{M.~Cross-Model Verification} $\cdot$
76	\hyperref[app:failure-modes]{N.~Failure Mode Analysis} $\cdot$
77	\hyperref[app:grounding-ablation]{O.~Grounding Ablation} $\cdot$
78	\hyperref[app:ablations]{P.~Ablation Studies} $\cdot$
79	\hyperref[sec:threshold-routing]{Q.~Threshold Routing} $\cdot$
80	\hyperref[app:decision-framework]{R.~Decision Framework} $\cdot$
81	\hyperref[app:extended-validation]{S.~Extended Validation} $\cdot$
82	\hyperref[app:prompt-templates]{T.~Agent Prompt Templates} $\cdot$
83	\hyperref[app:non-death-case-study]{U.~Non-Death Episode Case Study}
84	
85	\section{Signal Concentration Index}
86	\label{app:sci}
87	
88	Let $K$ denote the number of task types and $c_k$ the contribution of task type $k$ to the aggregate routing signal, defined as the fraction of total death-rate differential attributable to task $k$:
89	\begin{equation}
90	    c_k = \frac{n_k \cdot \delta_k}{\sum_{j=1}^{K} n_j \cdot \delta_j}
91	\end{equation}
92	where $n_k$ is the number of episodes and $\delta_k = d_k^{\tt int} - d_k^{\tt det}$ is the per-task death-rate differential. The SCI is the Gini coefficient over $\{c_1, \ldots, c_K\}$:
93	\begin{equation}
94	    \text{SCI} = \frac{\sum_{i=1}^K \sum_{j=1}^K |c_i - c_j|}{2K \sum_{k=1}^K c_k}
95	\end{equation}
96	
97	\section{Labeling Quality Audit}
98	\label{app:labeling}
99	
100	\begin{algorithm}[t]
101	\caption{Episode-Level Counterfactual Labeling}
102	\label{alg:labeling}
103	\begin{algorithmic}[1]
104	\REQUIRE Task instance $t$, computation modes $\mathcal{M} = \{{\tt int}, {\tt det}\}$
105	\ENSURE Label $\ell \in \{{\tt det\text{-}pref}, {\tt int\text{-}pref}, {\tt no\text{-}pref}\}$
106	\FOR{each $m \in \mathcal{M}$}
107	    \STATE Run episode $\tau_m$ with pure-strategy $m$
108	    \STATE Record score $s_m$ and death indicator $d_m$
109	\ENDFOR
110	\IF{$d_{\tt int} = 1$ \AND $d_{\tt det} = 0$}
111	    \STATE $\ell \leftarrow {\tt det\text{-}pref}$ \COMMENT{death asymmetry}
112	\ELSIF{$d_{\tt int} = 0$ \AND $d_{\tt det} = 1$}
113	    \STATE $\ell \leftarrow {\tt int\text{-}pref}$ \COMMENT{death asymmetry}
114	\ELSIF{$d_{\tt int} = d_{\tt det} = 1$}
115	    \STATE $\ell \leftarrow {\tt no\text{-}pref}$ \COMMENT{both dead}
116	\ELSIF{$s_{\tt det} > s_{\tt int}$}
117	    \STATE $\ell \leftarrow {\tt det\text{-}pref}$ \COMMENT{score comparison}
118	\ELSIF{$s_{\tt int} > s_{\tt det}$}
119	    \STATE $\ell \leftarrow {\tt int\text{-}pref}$ \COMMENT{score comparison}
120	\ELSE
121	    \STATE $\ell \leftarrow {\tt no\text{-}pref}$ \COMMENT{tied alive}
122	\ENDIF
123	\RETURN $\ell$
124	\end{algorithmic}
125	\smallskip
126	\noindent\textit{Assumption:} The death-first priority (lines 5--10) is valid when $P$ exceeds the maximum partial score, guaranteeing that a dead episode never outscores a surviving one. ScienceWorld satisfies this ($P{=}100$, max partial score ${=}100$).\\
127	\noindent\textit{Note:} When both strategies die (line 9), we assign \texttt{no\_preference}; in ScienceWorld, death yields a fixed $-100$ regardless of timing, so both-dead episodes contribute no routing signal.
128	\end{algorithm}
129	
130	Note that episode-level labels are used to evaluate step-level predictions, introducing a granularity mismatch rather than independent validation. A potential concern is oracle circularity: whether episode-level labels reflect tie-breaking artifacts rather than genuine computation mode differences. We audit all 245 labels. Of the 150 \texttt{no\_preference} labels (61.2\%), 115 (46.9\%) are both-alive ties and 35 (14.3\%) are both-dead, all excluded from router training. The remaining 95 training labels are entirely genuine: 75 from death asymmetry (70 deterministic-preferred, 5 internal-preferred) and 20 from score comparison with both strategies surviving (16 deterministic-preferred, 4 internal-preferred). Zero labels depend on tie-breaking. Retraining the router using only death-asymmetry labels yields step-level balanced accuracy of 57.3\%, within 1$\sigma$ of the full-label retrain (57.6 $\pm$ 0.5\%, step-level Trainer evaluation); score-comparison labels contribute negligible additional signal. (Step-level metrics are used here for the relative comparison; as shown in \S\ref{sec:router-diagnostic}, absolute generalization to new episodes is near chance.) The 97.4\% step-level tie rate (\S\ref{sec:collection}) further motivates episode-level over step-level labeling.
131	
132	\section{Per-Task Decomposition}
133	\label{app:per-task}
134	We use ScienceWorld v1.2.3~\citep{scienceworld-2022}.
135	We select 11 of ScienceWorld's 30 task types for analysis. Types are excluded when they were used for pipeline development (5 tasks, standard hold-out practice), are taxonomically redundant with a retained family representative (7 tasks), or exhibit near-zero task progress under both strategies (7 tasks, agent capability floor).\footnote{Excluded tasks exhibit even stronger death dominance than included tasks ($\Delta\text{DR} = +38.2$\,pp vs.\ $+28.7$\,pp; Table~\ref{tab:excluded-death}).}
136	
137	\begin{table}[h]
138	\centering
139	\scriptsize
140	\setlength{\tabcolsep}{2.5pt}
141	\begin{tabular}{@{}lrrccc@{}}
142	\toprule
143	Task & $n$ & $\Delta_\text{full}$ & D\%\textsubscript{int} & D\%\textsubscript{det} & D / I / N \\
144	\midrule
145	id-life-stages-1       & 20  & $+47.50$ & 55   & 10   & 9 / 0 / 11  \\
146	lifespan-long          & 25  & $+44.00$ & 56   & 16   & 11 / 1 / 13 \\
147	lifespan-l-then-s      & 20  & $+40.80$ & 45   & 10   & 8 / 1 / 11  \\
148	inclined-plane         & 20  & $+36.00$ & 55   & 20   & 7 / 0 / 13  \\
149	freeze                 & 20  & $+30.50$ & 55   & 25   & 6 / 0 / 14  \\
150	meas-melt-point        & 20  & $+30.05$ & 55   & 25   & 6 / 0 / 14  \\
151	id-life-stages-2       & 20  & $+30.00$ & 50   & 20   & 6 / 0 / 14  \\
152	find-animal            & 20  & $+26.65$ & 50   & 25   & 5 / 0 / 15  \\
153	grow-fruit             & 20  & $+25.10$ & 45   & 20   & 6 / 1 / 13  \\
154	chem-mix               & 20  & $+21.80$ & 45   & 25   & 6 / 2 / 12  \\
155	\midrule
156	find-non-living-thing$^\dagger$ & 40 & $+9.58$ & 0  & 0    & 16 / 4 / 20 \\
157	\midrule
158	\textbf{All (11 tasks)} & \textbf{245} & $\mathbf{+29.60}$ & \textbf{42.9} & \textbf{16.3} & \textbf{86 / 9 / 150} \\
159	\bottomrule
160	\end{tabular}
161	\caption{Per-task decomposition of the death avoidance effect. D\%: death rate for internal (int) and deterministic (det) strategies. D/I/N: episode labels (det-preferred / internal-preferred / no-preference). Sorted by $\Delta_{\text{full}}$ descending. The \textit{All} row is an episode-weighted aggregate across 245 episodes. $\dagger$\,Only task with zero deaths under both strategies; $n{=}40$ because data was collected in two batches, with the second batch adding 20 episodes to increase statistical power for this zero-death outlier.}
162	\label{tab:per-task}
163	\end{table}
164	
165	\paragraph{Task selection and anti-cherry-picking.}
166	Eighteen of the 19 excluded task types (95\%) exhibit death-asymmetric patterns (Table~\ref{tab:excluded-death}): internal-reasoning death rates range from 40\% to 60\% (mean 53.9\%), while deterministic death rates range from 0\% to 40\% (mean 15.8\%), yielding a mean death-rate differential of $+38.2$\,pp, exceeding the $+28.7$\,pp for included tasks. The included subset is thus \emph{less} death-asymmetric than the excluded subset, the opposite of what a cherry-picking hypothesis would predict. The sole exception is \texttt{grow-plant}, an intrinsically safe task with zero deaths under both strategies, paralleling \texttt{find-non-living-thing} in the included set. The 19 excluded tasks fall into three independently motivated categories: five used during pipeline development (standard hold-out practice), seven taxonomically redundant with included family representatives (deduplication), and seven where the 7B backbone achieves near-zero task progress regardless of strategy (agent capability floor). In no case was a task excluded because death dominance was absent. Exclusion is driven by absence of non-death routing signal ($\Delta_{\text{nd}} = 0$ for 53\% of excluded tasks) and standard deduplication practices. \texttt{find-non-living-thing} serves as an internal counterexample: zero deaths under both strategies yet included because it exhibits non-death routing signal ($\Delta_{\text{full}} = +9.58$ entirely from score differences), and deterministic is not always preferred (4 of 20 non-tie labels favor internal).
167	
168	\begin{table}[t]
169	\centering
170	\scriptsize
171	\setlength{\tabcolsep}{2pt}
172	\resizebox{\columnwidth}{!}{%
173	\begin{tabular}{@{}llrcccl@{}}
174	\toprule
175	Task & Grp & $n$ & D\%\textsubscript{int} & D\%\textsubscript{det} & $\Delta$DR & Excl.\ reason \\
176	\midrule
177	boil                          & A & 20 & 50 & 20 & $+30$ & dev set \\
178	change-state-of-matter        & A & 20 & 55 & 15 & $+40$ & dev set \\
179	chem-mix-paint-secondary      & A & 20 & 45 & 10 & $+35$ & dev set \\
180	grow-plant                    & A & 20 &  0 &  0 & $\phantom{+}0$  & dev set \\
181	melt                          & A & 20 & 55 & 15 & $+40$ & dev set \\
182	\midrule
183	chem-mix-paint-tertiary       & B &  5 & 40 & 20 & $+20$ & family redundancy \\
184	find-living-thing             & B &  5 & 60 & 20 & $+40$ & family redundancy \\
185	find-plant                    & B &  5 & 60 &  0 & $+60$ & family redundancy \\
186	inclined-friction-named       & B &  5 & 60 & 20 & $+40$ & family redundancy \\
187	inclined-friction-unnamed     & B &  5 & 60 &  0 & $+60$ & family redundancy \\
188	lifespan-shortest             & B &  5 & 60 & 40 & $+20$ & family redundancy \\
189	measure-melt-known            & B &  5 & 60 &  0 & $+60$ & family redundancy \\
190	\midrule
191	mendelian-known               & C &  5 & 60 & 20 & $+40$ & agent floor \\
192	mendelian-unknown             & C &  5 & 60 & 40 & $+20$ & agent floor \\
193	power-component               & C &  5 & 60 & 20 & $+40$ & agent floor \\
194	power-renewable               & C &  5 & 60 &  0 & $+60$ & agent floor \\
195	test-conductivity             & C &  5 & 60 & 20 & $+40$ & agent floor \\
196	test-conductivity-unknown     & C &  5 & 60 & 20 & $+40$ & agent floor \\
197	use-thermometer               & C &  5 & 60 & 20 & $+40$ & agent floor \\
198	\midrule
199	\textbf{Mean (19 excluded)}   &   &    & \textbf{53.9} & \textbf{15.8} & $\mathbf{+38.2}$ & \\
200	\textit{cf.\ included (11)}   &   &    & \textit{46.5} & \textit{17.8} & $\textit{+28.7}$ & \\
201	\bottomrule
202	\end{tabular}}%
203	\caption{Death-rate analysis of all 19 excluded task types. D\%: death rate (score $\leq -100$). $\Delta$DR = D\%\textsubscript{int} $-$ D\%\textsubscript{det}. 18 of 19 excluded tasks (95\%) exhibit positive death asymmetry ($\Delta$DR $\geq +20$\,pp). Exclusion groups: A = development set (excluded to prevent circular evaluation), B = taxonomically redundant with an included family representative, C = agent-floor tasks (backbone achieves near-zero progress regardless of strategy). The mean $\Delta$DR among excluded tasks ($+38.2$\,pp) exceeds that of included tasks ($+28.7$\,pp), confirming that task selection does not bias toward death-prone tasks. Group B--C estimates are based on $n{=}5$ prescreening episodes per task and should be interpreted as directional evidence rather than precise rate estimates.}
204	\label{tab:excluded-death}
205	\end{table}
206	
207	\section{Correlation Robustness}
208	\label{app:correlation}
209	
210	\begin{figure}[h]
211	\centering
212	\includegraphics[width=0.38\textwidth]{figures/fig1_daf_scatter.pdf}
213	\caption{Per-task scatter: death rate differential (internal $-$ deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). $r = 0.97$ (Spearman's $\rho = 0.986$), $p < 10^{-6}$, $n = 11$ task types. Since $\Delta_{\text{full}} \approx \delta P + \Delta_{\text{nd}}$ with $P$ constant, $r \to 1$ as DAF $\to 1$; the near-perfect correlation is a structural consequence of death dominance, not an independent finding (\S\ref{sec:death-decomp}).}
214	\label{fig:decomposition}
215	\end{figure}
216	
217	The Pearson $r = 0.9698$ reported in \S\ref{sec:death-decomp} is robust across multiple diagnostics. Spearman rank correlation is $\rho = 0.986$ ($p = 2.4 \times 10^{-8}$); the relationship is not driven by outliers or non-linearity. A nonparametric bootstrap (10{,}000 resamples) yields 95\% CI $[0.952, 0.995]$.
218	
219	\begin{table}[h]
220	\centering
221	\small
222	\begin{tabular}{@{}lr@{}}
223	\toprule
224	Task removed & $r_{\text{LOO}}$ \\
225	\midrule
226	id-life-stages-1       & 0.963 \\
227	lifespan-long          & 0.969 \\
228	lifespan-l-then-s      & 0.976 \\
229	inclined-plane         & 0.969 \\
230	freeze                 & 0.971 \\
231	meas-melt-point        & 0.972 \\
232	id-life-stages-2       & 0.972 \\
233	find-animal            & 0.970 \\
234	grow-fruit             & 0.973 \\
235	chem-mix               & 0.969 \\
236	find-non-living-thing  & 0.980 \\
237	\bottomrule
238	\end{tabular}
239	\caption{Leave-one-out Pearson $r$ for the death rate differential vs.\ $\Delta_{\text{full}}$ correlation. Full $r = 0.970$; LOO range $[0.963, 0.980]$. No single task type is a leverage point.}
240	\label{tab:loo}
241	\end{table}
242	
243	\section{Cluster Bootstrap Sensitivity Analysis}
244	\label{app:wild-cluster}
245	
246	With $K{=}11$ task-type clusters, cluster bootstrap falls well below the $K{\geq}20$--50 recommended for reliable inference \citep{cameron-2008,webb-2023}. The narrower CIs obtained reflect known small-sample bias toward underestimation of variance, not tighter inference.
247	
248	Episodes within the same task type share environment dynamics, raising the concern that the effective sample size is closer to $K$ (task types) than $N$ (episodes). We address this with cluster-robust inference treating each task type as a cluster ($K{=}11$, all 11 included task types, 245 episodes).
249	
250	\begin{table}[h]
251	\centering
252	\small
253	\resizebox{\columnwidth}{!}{%
254	\begin{tabular}{@{}lcc@{}}
255	\toprule
256	Method & $p$-value & 95\% CI \\
257	\midrule
258	Cluster-robust $t$-test ($t{=}10.0$, df$=$10) & $< 0.001$ & $[0.73, 1.00]$ \\
259	Wild cluster bootstrap ($B{=}9{,}999$) & $< 0.001$ & $[0.73, 1.00]$ \\
260	Exact permutation ($2{,}048$ perms) & $0.002$ & --- \\
261	Sign test & $< 0.001$ & --- \\
262	\bottomrule
263	\end{tabular}}%
264	\caption{Cluster-level tests of death-rate asymmetry ($K{=}11$ task clusters, 245 episodes). 10 of 11 clusters show internal DR $>$ deterministic DR; the sole exception (\texttt{find-non-living-thing}) has zero deaths under both strategies. Cohen's $d = 3.02$. The exact permutation $p = 0.002$ ($4/2{,}048$) reflects the near-unanimous directional consistency.}
265	\label{tab:wild-cluster}
266	\end{table}
267	
268	\noindent All methods confirm significance with $p < 0.01$, and the 95\% CI $[0.73, 1.00]$ excludes zero by a wide margin. With $K{=}11$ task types, ICC estimation itself carries substantial uncertainty; the high within-task consistency of death patterns (all-or-nothing per task type) suggests high ICC, which explains the CI narrowing under cluster resampling.
269	
270	We retain this analysis for transparency; readers should rely on the non-clustered episode-level bootstrap (\S\ref{sec:death-decomp}) as the primary inference.
271	
272	\section{Per-Task Death Rate Confidence Intervals}
273	\label{app:per-task-ci}
274	
275	We compute bootstrap 95\% CIs for the death-rate differential ($\Delta\text{DR} = \text{DR}_{\text{int}} - \text{DR}_{\text{det}}$) for all 30 ScienceWorld task types. Of 30 tasks, 28 are death-prone (at least one death under either strategy); the remaining 2 (\texttt{grow-plant}, \texttt{find-non-living-thing}) have zero deaths under both strategies.
276	
277	Across all 28 death-prone tasks, internal DR exceeds deterministic DR without exception (100\% directional consistency). The pooled death-rate differential is $+37.3\%$ (95\% CI: $[29.7\%, 44.4\%]$). Fifteen of 28 tasks are individually significant (CI excludes zero); the 13 non-significant tasks all have $n{=}5$ prescreening episodes, where statistical power is insufficient to detect even large effects (e.g., a task with $\Delta\text{DR} = +40$\,pp at $n{=}5$ has a CI of $\pm 43$\,pp). The universal directional consistency, combined with the pooled significance, confirms that death asymmetry is not driven by a subset of outlier tasks.
278	
279	\section{Leave-One-Task-Out DAF Sensitivity}
280	\label{app:loto-daf}
281	
282	\begin{table}[h]
283	\centering
284	\small
285	\caption{Leave-one-task-out DAF sensitivity (penalty-independent label fraction). Among the 10 death-prone tasks, removing any single task changes DAF by at most 3.0\,pp (range: 75.9\%--78.9\%). Removing \emph{Find Non-Living Thing}, the sole death-free task that contributes all 20 score-comparison episodes, raises DAF to 100\% by construction.}
286	\label{tab:loto-daf}
287	\begin{tabular}{lrrr}
288	\toprule
289	Removed Task & $N_\text{rem}$ & DAF (\%) & $\Delta$ (pp) \\
290	\midrule
291	(none, full) & 245 & 78.9 & --- \\
292	\midrule
293	Find Non-Living$^\dagger$ & 205 & 100.0 & +21.1 \\
294	Lifespan Longest & 220 & 75.9 & $-$3.0 \\
295	Life Stages 1 & 225 & 76.7 & $-$2.2 \\
296	Lifespan Long+Short & 225 & 76.7 & $-$2.2 \\
297	Chemistry Mix & 225 & 77.0 & $-$1.9 \\
298	Grow Fruit & 225 & 77.3 & $-$1.7 \\
299	Inclined Plane Angle & 225 & 77.3 & $-$1.7 \\
300	Freeze & 225 & 77.5 & $-$1.4 \\
301	Life Stages 2 & 225 & 77.5 & $-$1.4 \\
302	Melt Pt Unknown & 225 & 77.5 & $-$1.4 \\
303	Find Animal & 225 & 77.8 & $-$1.2 \\
304	\bottomrule
305	\end{tabular}
306	
307	\vspace{2pt}
308	{\footnotesize $^\dagger$Only death-free task; contributes all score-comparison labels. Sorted by $|\Delta|$ descending.}
309	\end{table}
310	
311	\section{Per-Task Dose-Response Breakdown}
312	\label{app:dose-response}
313	
314	Table~\ref{tab:dose-response-detail} reports per-task death rates for Reflexion at $N{=}3$, 4, and 5 on the 10 death-prone tasks ($n{=}20$ episodes per task). Per-task variance is high (up to 25\,pp range for \texttt{measure-melting-point}), but the aggregate smooths to a 2.5\,pp band, confirming that the stabilization conclusion is robust at the aggregate level despite task-level noise. \texttt{freeze} is consistently the hardest task (50--60\% DR across all $N$).
315	
316	\paragraph{Statistical power.} With $n{=}200$ paired episodes, the minimum detectable effect (MDE) is ${\sim}8$~pp ($\alpha = 0.05$, 80\% power). The key $N{=}1{\to}3$ decline ($-13.5$~pp) exceeds this threshold and is well-powered; the stabilization claim ($N{=}3{\to}5$, $+1.0$~pp) is also supported, since a ${\geq}8$~pp improvement would be detected if present.
317	
318	\begin{table}[h]
319	\centering
320	\small
321	\caption{Per-task death rates (\%) for Reflexion at $N{=}3$, 4, 5 on 10 death-prone tasks ($n{=}20$ per task). Aggregate death rates confirm stabilization at $N \geq 3$ (range: $34.0$--$36.5\%$).}
322	\label{tab:dose-response-detail}
323	\begin{tabular}{@{}lrrr@{}}
324	\toprule
325	Task & $N{=}3$ & $N{=}4$ & $N{=}5$ \\
326	\midrule
327	chemistry-mix & 25.0 & 35.0 & 20.0 \\
328	find-animal & 45.0 & 30.0 & 45.0 \\
329	freeze & 50.0 & 50.0 & 60.0 \\
330	grow-fruit & 30.0 & 25.0 & 25.0 \\
331	identify-life-stages-1 & 35.0 & 35.0 & 35.0 \\
332	identify-life-stages-2 & 25.0 & 25.0 & 30.0 \\
333	inclined-plane-angle & 20.0 & 30.0 & 35.0 \\
334	lifespan-longest & 45.0 & 40.0 & 40.0 \\
335	lifespan-long+short & 30.0 & 45.0 & 35.0 \\
336	measure-melting-pt & 35.0 & 50.0 & 25.0 \\
337	\midrule
338	\textbf{Aggregate} & \textbf{34.0} & \textbf{36.5} & \textbf{35.0} \\
339	\bottomrule
340	\end{tabular}
341	\end{table}
342	
343	\section{Router Training Details}
344	\label{app:router-details}
345	
346	We use Qwen3-1.7B for the router to avoid circular dependency with the Qwen2.5-7B data-generating model.
347	
348	With gradient accumulation of 1 (effective batch size 4), routing performance is highly sensitive to the evaluation split; this suggests overfitting to specific train/validation partition boundaries. With gradient accumulation of 8 (effective batch size 32), step-level performance stabilizes across splits (${\sim}54\%$ balanced accuracy). All reported results use gradient accumulation 8.
349	
350	Under step-level evaluation with a fixed data split, cross-seed balanced accuracy ranges from 52.7\% to 58.1\%, but internal recall varies from 51.5\% to 81.8\%, which reflects threshold sensitivity. However, episode-level evaluation reveals that this apparent discrimination does not generalize: balanced accuracy drops to $47.1 \pm 2.2\%$ across 8 cross-split seeds (Appendix~\ref{app:seed-robustness}). Deployed end-to-end, the trained router allocates 97.0\% of episodes to deterministic computation with 17.6\% death rate, and misrouting cost (death from internally-routed episodes) exceeds the benefit of correctly routing rare internal-preferred cases.
351	
352	\paragraph{Evaluation methods.} All results use \emph{generation-based evaluation}: the model generates a routing label as text (\texttt{enable\_thinking=False}), parsed for classification. We evaluate at two granularities: \emph{step-level} (steps from the same episode may appear in both train and validation sets) and \emph{episode-level} (entire episodes held out). Step-level accuracy ($54.1 \pm 5.4\%$) exceeds chance (the router captures some signal), but episode-level accuracy ($47.1 \pm 2.2\%$, below chance) shows this does not generalize to unseen episodes. Paraphrase-based text augmentation (Appendix~\ref{app:seed-robustness}) provides no improvement; real-data scaling remains open. Always-deterministic is trivially near-optimal given DAF $= 90.4\%$. The main text (\S\ref{sec:router-diagnostic}) reports controlled 4-seed results at three scales; the model-size ablation (Appendix~\ref{app:ablations}) provides further detail.
353	
354	\begin{table}[h]
355	\centering
356	\small
357	\resizebox{\columnwidth}{!}{%
358	\begin{tabular}{@{}lcc@{}}
359	\toprule
360	Hyperparameter & Classification Head & Implicit Router \\
361	\midrule
362	Base model & Qwen3-1.7B & Qwen3-1.7B \\
363	Architecture & Linear + LoRA & SFT + LoRA \\
364	LoRA $r$ / $\alpha$ & 16 / 32 & 16 / 32 \\
365	Learning rate & 2e-5 & 2e-4 \\
366	Optimizer & AdamW & AdamW \\
367	Epochs & 3 & 3 \\
368	Batch size (per device) & 4 & 4 \\
369	Gradient accumulation & 8 & 8 \\
370	Warmup ratio & 0.1 & 0.1 \\
371	Weight decay & 0.01 & 0.01 \\
372	Max sequence length & 512 & 512 \\
373	Seeds & \{42\} & \{42, 123, 456, 789\} \\
374	\bottomrule
375	\end{tabular}}
376	\caption{Router training hyperparameters. Both architectures use the same base model with LoRA adaptation. The classification head degenerates across all configurations; the implicit router results are reported as 4-seed mean$\pm$std.}
377	\label{tab:hyperparams}
378	\end{table}
379	
380	\paragraph{Agent inference parameters.}
381	For ScienceWorld, each agent step uses temperature $T{=}0.3$ and maximum generation length of 256 tokens, served via vLLM v0.21.0. Top-$p$ is left at the vLLM default of $1.0$ (no nucleus sampling). For MATH, the agent uses greedy decoding ($T{=}0.0$) with a maximum of 2{,}048 tokens per generation. For ALFWorld, we use $T{=}0.3$ with 256 maximum tokens. All three environments use Qwen2.5-7B-Instruct~\citep{qwen25-2024} as the backbone.
382	
383	\section{Seed Robustness}
384	\label{app:seed-robustness}
385	
386	We assess router generalization at two evaluation granularities: \emph{step-level}, where steps from the same episode may appear in both train and validation sets, and \emph{episode-level}, where entire episodes are held out. Both use cross-split evaluation (seeds $\{42, \ldots, 49\}$, 8 seeds total), where the data partition and training seed both vary. Table~\ref{tab:seed-robustness} reports per-seed results.
387	
388	\begin{table}[h]
389	\centering
390	\small
391	\begin{tabular}{@{}llcc@{}}
392	\toprule
393	Eval.\ Granularity & Seed & Bal.\ Acc.\ (\%) \\
394	\midrule
395	Step-level & 42 & 57.06 \\
396	(same-episode & 43 & 63.99 \\
397	leakage) & 44 & 55.43 \\
398	 & 45 & 56.14 \\
399	 & 46 & 55.45 \\
400	 & 47 & 50.08 \\
401	 & 48 & 48.03 \\
402	 & 49 & 59.30 \\
403	\cmidrule{2-3}
404	 & Mean$\pm$std & $54.1 \pm 5.4$ \\
405	\midrule
406	Episode-level & 42 & 48.1 \\
407	(held-out & 43 & 47.9 \\
408	episodes) & 44 & 49.6 \\
409	 & 45 & 49.4 \\
410	 & 46 & 48.5 \\
411	 & 47 & 43.1 \\
412	 & 48 & 45.4 \\
413	 & 49 & 44.8 \\
414	\cmidrule{2-3}
415	 & Mean$\pm$std & $47.1 \pm 2.2$ \\
416	\midrule
417	\multicolumn{2}{@{}l}{Always-det (= majority-vote)} & 50.0 \\
418	\bottomrule
419	\end{tabular}
420	\caption{Per-seed router performance under cross-split evaluation (8 seeds, generation-based, \texttt{enable\_thinking=False}). Step-level evaluation allows steps from the same episode in both train and validation sets (same-episode leakage). Episode-level evaluation holds out entire episodes; the resulting $47.1 \pm 2.2\%$ is below the 50\% chance baseline. A text augmentation ablation (Table~\ref{tab:text-augmentation}) confirms this failure persists under the current data distribution and augmentation regime.}
421	\label{tab:seed-robustness}
422	\end{table}
423	
424	The contrast between step-level ($54.1 \pm 5.4\%$) and episode-level ($47.1 \pm 2.2\%$) evaluation reveals a generalization gap: the step-level signal likely reflects memorization of episode-specific context (enabled by same-episode leakage) rather than extraction of generalizable routing features. At episode level, the router performs below chance across all 8 seeds (range: 43.1\%--49.6\%). Paraphrase-based text augmentation (Table~\ref{tab:text-augmentation}) from 25\% to 800\% ($32{\times}$ range) provides no improvement, converging to the always-deterministic baseline ($50\%$). Paraphrase augmentation inflates the majority class without generating novel routing patterns; genuine episode-level scaling (collecting more counterfactual pairs) remains an open question. With DAF $= 90.4\%$ and all task types deterministic-majority (86:9 label ratio), always-deterministic trivially solves the episode-level routing problem, leaving the step-level router with no exploitable signal under current architectures.
425	
426	\paragraph{Text augmentation ablation.} To test whether the episode-level generalization failure stems from data scarcity, we vary training set size from 25\% to 800\% of the original via paraphrase-based text augmentation (synonym substitution + template variation on step observations), holding the episode-level validation set fixed. This tests augmentation-based scaling, not genuine episode-level scaling (which would require new counterfactual collections). Table~\ref{tab:text-augmentation} reports the results.
427	
428	\begin{table}[h]
429	\centering
430	\small
431	\begin{tabular}{@{}rccc@{}}
432	\toprule
433	Scale & Samples & Det\% & Ep.\ Bal.\ Acc.\ (\%) \\
434	\midrule
435	25\% & 433 & ${\sim}90$ & $49.5 \pm 0.3$ \\
436	50\% & 867 & ${\sim}90$ & $51.5$ \\
437	100\% & 1{,}735 & 89.6 & $49.9 \pm 0.1$ \\
438	200\% & 3{,}470 & 94.2 & $50.0 \pm 0.0$ \\
439	800\% & 13{,}880 & ${\sim}97.7$ & $51.0 \pm 1.1$ \\
440	\midrule
441	Always-det & --- & --- & 50.0 \\
442	\bottomrule
443	\end{tabular}
444	\caption{Text augmentation ablation: episode-level balanced accuracy across training set sizes (25\%--800\% of original via paraphrase, $32{\times}$ range). Internal recall $= 0.0$ at all scales (complete majority-class collapse). Det\%: fraction of deterministic-preferred labels in training data. The 50\% scale is a single seed; all others report mean$\pm$std across seeds.}
445	\label{tab:text-augmentation}
446	\end{table}
447	
448	All scales hover at ${\sim}50\%$ episode-level balanced accuracy (equivalent to the always-deterministic baseline), with no monotonic improvement as data increases. Augmentation-based scaling provides no improvement at any scale; however, episode-level minority-class diversity remains a potential confound that cannot be resolved without collecting more internal-preferred episodes. The ground-truth internal-preferred rate (9/245 $= 3.7\%$) means collecting 50 internal-preferred episodes would require approximately 1{,}350 paired episodes at current environment dynamics, a $5.5{\times}$ expansion with diminishing return on a $9.6\%$ signal. The failure points to a limitation of the current data distribution: when DAF $= 90.4\%$ and all task types are deterministic-majority (86:9 label ratio), the episode-level routing problem is trivially solved by always choosing deterministic, and the step-level router finds no exploitable signal under the current architecture and data regime.
449	
450	Augmentation disproportionately increases the majority (deterministic) class: Det\% rises from 89.6\% at 100\% to 94.2\% at 200\% and ${\sim}97.7\%$ at 800\%. However, the complete collapse to majority-class prediction (internal recall $= 0.0$) occurs even at the smallest unaugmented scale (25\%, ${\sim}90\%$ det); this is not an augmentation artifact. Balanced accuracy corrects for class imbalance by averaging per-class recall, so the metric itself is not biased by the skew.
451	
452	Decomposition metrics are stable under bootstrap resampling ($B{=}10{,}000$ resamples of the 245-episode dataset): DAF $= 90.4\% \pm 4.2\%$ (95\% CI $[81.1\%, 99.0\%]$); Pearson $r = 0.975 \pm 0.011$ (95\% CI $[0.952, 0.995]$). The death avoidance dominance finding is robust to both resampling and split perturbation.
453	
454	\paragraph{Per-task-type evaluation breakdown.} To test whether the router learns transferable routing strategies or merely task-type classification, we evaluate existing checkpoints (8 seeds) separately on each of the 11 task types. Of the 11 task types, 7 have \emph{all-deterministic} labels (no internal-preferred episodes exist), making balanced accuracy undefined; the router has nothing to learn beyond the trivial always-deterministic default. For the remaining 4 task types where both classes are present, balanced accuracy ranges from 50.0\% to 73.0\%, but this apparent signal does not indicate cross-task-type routing transfer: the router is effectively classifying task types (which correlate with death risk) rather than extracting a generalizable routing strategy. This complements the text augmentation ablation: routing signal does not transfer across task types because the signal \emph{is} the task type, i.e., whether a given task carries death risk. The 4B capacity scaling result (Appendix~\ref{app:ablations}) suggests capacity is one factor, but even 4B's $59.0\%$ episode-level accuracy does not demonstrate cross-task-type transfer.
455	
456	\section{Penalty Sensitivity Analysis}
457	\label{app:penalty}
458	
459	\begin{table}[h]
460	\centering
461	\small
462	\begin{tabular}{@{}rrr@{}}
463	\toprule
464	$P$ & DAF($P$) & 95\% CI \\
465	\midrule
466	0 & 7.4\% & [$-39.4$, $82.5$] \\
467	1 & 14.8\% & [$-28.6$, $89.6$] \\
468	5 & 35.4\% & [$-1.8$, $92.7$] \\
469	10 & 50.4\% & [$18.5$, $93.3$] \\
470	25 & 70.7\% & [$48.0$, $96.3$] \\
471	50 & 82.6\% & [$67.2$, $98.2$] \\
472	100\textsuperscript{*} & 90.4\% & [$81.1$, $99.0$] \\
473	200 & 94.9\% & [$89.9$, $99.5$] \\
474	500 & 97.9\% & [$95.7$, $99.8$] \\
475	\bottomrule
476	\end{tabular}
477	\caption{Sensitivity of DAF to death penalty magnitude $P$. DAF$(P) = 1 - \Delta_{\text{nd}} / \Delta_{\text{full}}(P)$, where $\Delta_{\text{full}}(P) \approx \delta \cdot P + \Delta_{\text{nd}}$, $\delta = 0.2653$ is the death-rate differential, and $\Delta_{\text{nd}} = 2.84$ (strict neither-died filtering). Recomputed from 245 episode-level data; bootstrap 95\% CIs ($B{=}10{,}000$). \textsuperscript{*}Default setting.}
478	\label{tab:penalty-sensitivity}
479	\end{table}
480	
481	The non-death score gap $\Delta_{\text{nd}} = 2.84$ is invariant across penalty levels; it depends only on surviving-episode performance, not on $P$. As $P$ increases, $\Delta_{\text{full}}$ grows ($16.33$ at $P{=}50$, $29.60$ at $P{=}100$, $56.13$ at $P{=}200$) while $\Delta_{\text{nd}}$ remains fixed, mechanically increasing DAF.
482	
483	\paragraph{Mechanism boundary: death specificity.}
484	The $r = 0.97$ correlation between per-task death-rate differential and $\Delta_{\text{full}}$ is specific to catastrophic death (score $= -100$). Broader failure definitions dissolve the correlation entirely: defining ``failure'' as any non-positive score ($T{=}0$) yields $r = -0.13$ ($p = 0.70$), because non-death episodes show near-zero performance differential between strategies ($\Delta_{\text{nd}} = 2.84$). Table~\ref{tab:penalty-correlation} quantifies this specificity across penalty magnitudes.
485	
486	\begin{table}[h]
487	\centering
488	\small
489	\begin{tabular}{@{}rccl@{}}
490	\toprule
491	$P$ & $r$ & $p$ & Sig.\ ($\alpha{=}0.05$) \\
492	\midrule
493	1 & $-0.44$ & $0.178$ & No \\
494	5 & $-0.29$ & $0.382$ & No \\
495	10 & $-0.08$ & $0.813$ & No \\
496	25 & $0.51$ & $0.108$ & No \\
497	50 & $0.86$ & $0.0006$ & Yes \\
498	100\textsuperscript{*} & $0.97$ & $8 \times 10^{-7}$ & Yes \\
499	200 & $0.99$ & $1 \times 10^{-9}$ & Yes \\
500	\bottomrule
501	\end{tabular}
502	\caption{Pearson $r$ between per-task death-rate differential and $\Delta_{\text{full}}(P)$ across penalty magnitudes. The correlation is non-significant at low penalties and emerges at $P \geq 50$, which reflects the transition from non-death-dominated to death-dominated score gaps. \textsuperscript{*}Default ScienceWorld setting.}
503	\label{tab:penalty-correlation}
504	\end{table}
505	
506	This sharpens our central finding: death is not merely the dominant component of routing signal; it is effectively the \emph{only} component that generates differential routing signal in ScienceWorld. At low penalties, the death contribution is small and $\Delta_{\text{full}}$ reduces to $\Delta_{\text{nd}} \approx 2.84$, which is near-uniform across task types ($\text{mean non-death gap} = -1.19$ excluding the \texttt{find-non-living-thing} outlier); consequently, death-rate differential has no predictive power. As $P$ increases, the death term dominates $\Delta_{\text{full}}$, and the correlation sharpens because death rates \emph{are} the performance gap. The DAF values in Table~\ref{tab:penalty-sensitivity} increase monotonically with $P$, but this is a mathematical consequence of the decomposition ($\text{DAF} = \delta P / (\delta P + \Delta_{\text{nd}})$), not evidence of mechanism robustness.
507	
508	\section{Cross-Environment Details}
509	\label{app:cross-env-details}
510	
511	Figure~\ref{fig:signal-reversal} and Table~\ref{tab:cross-env} summarize the label distributions across all three environments.
512	
513	\begin{figure}[h]
514	\centering
515	\includegraphics[width=\columnwidth]{figures/signal_reversal.pdf}
516	\caption{Cross-environment label distributions. ScienceWorld and ALFWorld both show deterministic preference, but through different mechanisms: death avoidance (ScienceWorld) vs.\ information asymmetry from admissible-action access (ALFWorld). MATH shows balanced labels, confirming no routing signal without catastrophic failure.}
517	\label{fig:signal-reversal}
518	\end{figure}
519	
520	\begin{table}[h]
521	\centering
522	\small
523	\resizebox{\columnwidth}{!}{%
524	\begin{tabular}{@{}lccccc@{}}
525	\toprule
526	Environment & $N$ & Det\% & Int\% & NoPref\% & Death? \\
527	\midrule
528	ScienceWorld & 245 & 35.1 & 3.7 & 61.2 & Yes ($-100$) \\
529	MATH & 795 & 7.3 & 8.3 & 84.4 & No \\
530	ALFWorld & 135 & 25.9 & 1.5 & 72.6 & No\textsuperscript{$\dagger$} \\
531	\bottomrule
532	\end{tabular}}
533	\caption{Cross-environment label distribution. ``Deterministic'' denotes qualitatively different computation modes: ScienceWorld = oracle simulator with ground-truth state; MATH = Python code interpreter; ALFWorld = admissible-action enumeration. $\dagger$\,ALFWorld's deterministic advantage stems from information asymmetry, not death avoidance.}
534	\label{tab:cross-env}
535	\end{table}
536	
537	Table~\ref{tab:alfworld-pertask} provides the per-task-type breakdown for ALFWorld. Unlike ScienceWorld, ALFWorld has no death mechanism ($\delta = 0$, DAF $= 0\%$); the entire performance gap $\Delta_{\text{full}}$ reflects information asymmetry from admissible-action access. \texttt{pick\_and\_place} shows the strongest effect ($\Delta = 0.563$, 18 of 32 episodes det-preferred), while \texttt{pick\_two\_obj\_and\_place} shows the weakest ($\Delta = 0.087$), consistent with multi-object tasks requiring more sequential reasoning that admissible actions alone cannot resolve. Only \texttt{pick\_heat\_then\_place} has a 95\% CI crossing zero ($n{=}16$).
538	
539	\begin{table}[h]
540	\centering
541	\scriptsize
542	\setlength{\tabcolsep}{2.5pt}
543	\begin{tabular}{@{}lrcccc@{}}
544	\toprule
545	Task Type & $n$ & Succ\%\textsubscript{int} & Succ\%\textsubscript{det} & D / I / N & $\Delta_{\text{full}}$ \\
546	\midrule
547	pick\_and\_place       & 32 & 0.0  & 56.3 & 18 / 0 / 14 & $+0.563$ \\
548	look\_at\_obj\_in\_light & 13 & 15.4 & 38.5 & 3 / 0 / 10  & $+0.231$ \\
549	pick\_cool\_then\_place & 24 & 0.0  & 16.7 & 4 / 0 / 20  & $+0.167$ \\
550	pick\_clean\_then\_place & 27 & 3.7  & 18.5 & 5 / 1 / 21  & $+0.148$ \\
551	pick\_heat\_then\_place & 16 & 6.3  & 18.8 & 3 / 1 / 12  & $+0.125$ \\
552	pick\_two\_obj\_and\_place & 23 & 0.0 & 8.7  & 2 / 0 / 21  & $+0.087$ \\
553	\midrule
554	\textbf{All (6 types)} & \textbf{135} & \textbf{3.0} & \textbf{27.4} & \textbf{35 / 2 / 98} & $\mathbf{+0.244}$ \\
555	\bottomrule
556	\end{tabular}
557	\caption{Per-task-type decomposition for ALFWorld (135 games, Qwen2.5-7B-Instruct). D/I/N: deterministic-preferred / internal-preferred / no-preference. No death mechanism exists; $\Delta_{\text{full}}$ is driven entirely by information asymmetry from admissible-action access. Sorted by $\Delta_{\text{full}}$ descending.}
558	\label{tab:alfworld-pertask}
559	\end{table}
560	
561	\paragraph{MATH subset composition.}
562	The $N{=}795$ MATH problems span two categories from the MATH test set~\citep{math-2021} (Levels 4--5): Algebra (585, 73.6\%) and Counting \& Probability (210, 26.4\%). The category imbalance reflects the relative sizes in the original test set.
563	
564	\section{Cross-Model Verification}
565	\label{app:cross-model}
566	
567	We replicate the counterfactual analysis with Llama-3.1-8B-Instruct across all 11 task types ($N{=}220$ episode pairs, 20 per type; Table~\ref{tab:cross-model-detail}).
568	The internal strategy dies in $41.4\%$ of episodes versus $11.4\%$ for deterministic (death-rate differential $+30.0$~pp), with 83 deterministic-preferred, 3 internal-preferred (1.4\%, all death-asymmetry reversals), and 134 no-preference labels.
569	Both models exhibit nearly identical internal vulnerability (${\sim}$42\%: Qwen $42.9\%$, Llama $41.4\%$), confirming that death-prone failure is empirically dominated by the task environment rather than model-specific factors. The differential magnitude varies ($+26.5$~pp Qwen, $+30.0$~pp Llama) because deterministic strategy safety is model-dependent ($16.3\%$ vs.\ $11.4\%$), but directional consistency is 100\% (10/10 death-prone tasks in both models).
570	\texttt{identify-life-stages-1} shows cross-model precision matching ($55\%$/$10\%$/$+45$~pp in both models).
571	\texttt{find-non-living-thing} shows zero deaths in both models, consistent with its majority-class answer distribution.
572	
573	\begin{table}[h]
574	\centering
575	\small
576	\resizebox{\columnwidth}{!}{%
577	\begin{tabular}{@{}lrrrl@{}}
578	\toprule
579	Task & Int\% & Det\% & $\Delta$\,pp & D / I / N \\
580	\midrule
581	identify-life-stages-1 & 55 & 10 & +45 & 9 / 0 / 11 \\
582	freeze & 45 & 0 & +45 & 9 / 0 / 11 \\
583	grow-fruit & 45 & 5 & +40 & 8 / 0 / 12 \\
584	identify-life-stages-2 & 45 & 5 & +40 & 8 / 0 / 12 \\
585	measure-melting-point & 50 & 15 & +35 & 9 / 0 / 11 \\
586	lifespan-longest & 35 & 5 & +30 & 7 / 1 / 12 \\
587	lifespan-l-then-s & 50 & 20 & +30 & 6 / 0 / 14 \\
588	chemistry-mix & 45 & 20 & +25 & 5 / 0 / 15 \\
589	inclined-plane & 45 & 20 & +25 & 6 / 0 / 14 \\
590	find-animal & 40 & 25 & +15 & 6 / 2 / 12 \\
591	find-non-living-thing & 0 & 0 & 0 & 10 / 0 / 10 \\
592	\midrule
593	\textbf{Aggregate} & \textbf{41.4} & \textbf{11.4} & \textbf{+30.0} & \textbf{83 / 3 / 134} \\
594	\bottomrule
595	\end{tabular}}%
596	\caption{Per-task Llama-3.1-8B cross-model replication ($N{=}20$ per task). D/I/N: deterministic-preferred / internal-preferred / no-preference. Sorted by $\Delta$ DR descending.}
597	\label{tab:cross-model-detail}
598	\end{table}
599	
600	\paragraph{Cross-model and cross-environment summary.}
601	Table~\ref{tab:cross-model-env} consolidates replication results across model families and environments.
602	
603	\begin{table}[h]
604	\centering
605	\small
606	\resizebox{\columnwidth}{!}{%
607	\begin{tabular}{llcrrrccc}
608	\toprule
609	Model & Environment & $n$ & Int DR & Det DR & $\Delta$DR & DAF & DAF 95\% CI & Signal \\
610	\midrule
611	Qwen2.5-7B & ScienceWorld & 245 & 42.9\% & 16.3\% & +26.5 & 90.4\% & [81.1, 99.0] & death \\
612	Llama-3.1-8B & ScienceWorld & 220 & 41.4\% & 11.4\% & +30.0 & 88.2\% & [80.2, 95.1] & death \\
613	Gemma-2-9B-it & ScienceWorld & 220 & 36.4\% & 14.1\% & +22.3 & 89.7\% & [79.5, 98.4] & death \\
614	Qwen2.5-72B & ScienceWorld & 255 & 30.6\% & 2.75\% & +27.8 & 92.4\% & --- & death \\
615	\midrule
616	Qwen2.5-7B & ALFWorld & 135 & 0\% & 0\% & 0 & 0\% & --- & info-asym \\
617	Llama-3.1-8B & ALFWorld & 135 & 0\% & 0\% & 0 & 0\% & --- & info-asym \\
618	\midrule
619	Qwen2.5-7B & MATH & 795 & N/A & N/A & N/A & N/A & N/A & none \\
620	\bottomrule
621	\end{tabular}}
622	\caption{Cross-model and cross-environment replication summary. \textbf{ScienceWorld}: death dominance replicates across three model families in the 7--9B range and persists under $10{\times}$ scaling (72B); DAF 95\% CIs from non-clustered episode-level bootstrap ($B{=}10{,}000$). \textbf{ALFWorld}: DAF $= 0\%$ (no death mechanism); routing signal arises from information asymmetry. \textbf{MATH}: no routing signal without catastrophic failure. Signal column: diagnosed routing mechanism. DR = death rate. Gemma-2's wider CI reflects one zero-death task type (\texttt{find-non-living-thing}); excluding it yields DAF $= 99.9\%$ $[99.7, 100.0]$.}
623	\label{tab:cross-model-env}
624	\end{table}
625	
626	\section{Failure Mode Analysis}
627	\label{app:failure-modes}
628	
629	All 105 internal-strategy deaths (100\%) are triggered by the same action pattern: \texttt{focus on [object]}. In ScienceWorld, \texttt{focus on} is the answer-submission action (equivalent to ``this is my final answer''); the LLM agent systematically misuses it as a general interaction or exploration command, and applies it to irrelevant targets (rooms, doors, inventory items). Each such execution submits an incorrect answer and triggers the $-100$ death penalty. Within death episodes, both strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$); the internal strategy's higher death count (105 vs.\ 40 for deterministic) reflects how often each strategy enters catastrophic states, not different action selection within those states.
630	
631	Manual inspection identifies four failure categories: (A) no task awareness, where the agent executes \texttt{focus on} without reading the task; (B) task-aware but lacking action grounding, where the agent correctly identifies the objective but cannot map it to valid action primitives; (D) genuine attempts with execution failure; and (E) initial progress wasted by early errors. Category B dominates: agents demonstrate task comprehension but systematically fail to translate it into correct ScienceWorld actions. This taxonomy was produced by a single annotator; no inter-annotator agreement was computed. The categories are intended as qualitative illustrations, not as formal labels with reliability guarantees.
632	\label{tab:death-taxonomy}
633	
634	\paragraph{Representative examples.}
635	\emph{Category A} (no task awareness): In a \texttt{chemistry-mix} episode, the agent immediately executes \texttt{focus on kitchen}, \texttt{focus on door}, \texttt{focus on inventory} without reading the task, dying on the first \texttt{focus on} call. \emph{Category B} (comprehension without grounding): In a \texttt{lifespan-longest-lived} episode, the agent correctly identifies that it must compare animal lifespans and reasons about which animal lives longest, but then executes \texttt{focus on oak tree} (a non-animal object in the room) instead of navigating to find the target animal, triggering death.
636	
637	\paragraph{Action distribution analysis.}
638	Figure~\ref{fig:death-action-dist} shows the action distribution in death versus non-death episodes for the internal strategy; both are dominated by \texttt{connect} actions, with \texttt{focus on} moderately more frequent in death episodes ($5.4\%$ vs.\ $3.4\%$). Crucially, Figure~\ref{fig:death-comparison} reveals that within death episodes, internal and deterministic strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$). The survival gap (105 vs.\ 40 deaths) therefore reflects how often each strategy enters catastrophic states, not how it behaves within those states. Among fatal \texttt{focus on} targets, \texttt{workshop} remains the most frequent (20.0\%), followed by \texttt{inventory} (17.1\%) and \texttt{kitchen} (10.5\%), indicating a systematic object bias rather than random exploration. Figure~\ref{fig:death-timeline} visualizes the temporal pattern: agents execute long sequences of \texttt{connect} actions before a terminal \texttt{focus on} triggers death, typically in the final 1--3 steps.
639	
640	\begin{figure}[h]
641	\centering
642	\includegraphics[width=\columnwidth]{figures/death_action_distribution.pdf}
643	\caption{Action distribution for the internal (LLM) strategy in death ($n{=}105$) vs.\ non-death ($n{=}140$) episodes. Left: full distribution (both dominated by \texttt{connect}). Right: non-\texttt{connect} actions zoomed. \texttt{focus on} is moderately more frequent in death episodes ($5.4\%$ vs.\ $3.4\%$), while non-death episodes show higher rates of observation and object interaction.}
644	\label{fig:death-action-dist}
645	\end{figure}
646	
647	\begin{figure}[h]
648	\centering
649	\includegraphics[width=\columnwidth]{figures/death_action_timeline.pdf}
650	\caption{Step-by-step action sequences for 6 representative death episodes. The fatal \texttt{focus on} action (marked with arrow) consistently appears in the final steps after long \texttt{connect} sequences, and illustrates the ``connect loop $\to$ fatal focus'' pattern. Examples are drawn from the full 30-task dataset for task-type diversity; the pattern is identical in the 11-task analysis subset.}
651	\label{fig:death-timeline}
652	\end{figure}
653	
654	\begin{figure}[h]
655	\centering
656	\includegraphics[width=\columnwidth]{figures/death_action_comparison.pdf}
657	\caption{Non-\texttt{connect} action distribution comparison between internal (left) and deterministic (right) strategies. Within death episodes, both strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$); the internal strategy's higher death count (105 vs.\ 40) reflects more frequent entry into catastrophic states, not different action selection within those states.}
658	\label{fig:death-comparison}
659	\end{figure}
660	
661	\section{Grounding Ablation}
662	\label{app:grounding-ablation}
663	
664	We test whether directly intervening on the dominant death action (\texttt{focus on}) eliminates death vulnerability on the 10 death-prone tasks (baseline 48.0\%, $n{=}200$).
665	
666	\paragraph{Prompt warning.} Adding an explicit system prompt (``use \texttt{focus on} only for final answers'') reduces aggregate death rate to 37.0\% ($\Delta = -11$~pp). Both identification tasks exhibit ironic effects (\texttt{identify-life-stages-1}: 35\%$\to$50\%; \texttt{identify-life-stages-2}: 25\%$\to$70\%), where explicit mention of the dangerous action may have increased its salience.
667	
668	\paragraph{Action-space filtering.} Blocking \texttt{focus on} during the exploration phase yields 379 blocks across 200 episodes with zero leaks and zero passthroughs (the agent never persisted in retrying blocked actions), reducing death rate to 29.0\% ($\Delta = -19$~pp). The zero-passthrough rate suggests \texttt{focus on} use is a shallow behavioral pattern rather than a deliberate strategy.
669	
670	\paragraph{Per-task variation.} Under filtering, \texttt{identify-life-stages} and \texttt{inclined-plane} approach deterministic-level safety (${\sim}$15--20\% DR), while \texttt{chemistry-mix} and \texttt{find-animal} remain at 35--40\%. Residual deaths occur during the answer-submission window, where the filter is inactive and agents submit \texttt{focus on} to incorrect objects.
671	
672	\section{Ablation Studies}
673	\label{app:ablations}
674	
675	\paragraph{Capacity scaling.} We scale the implicit router from Qwen3-0.6B to Qwen3-4B and evaluate at both step and episode level (Table~\ref{tab:capacity}).
676	
677	\begin{table}[h]
678	\centering
679	\small
680	\begin{tabular}{@{}lcc@{}}
681	\toprule
682	Model & Step Bal.\ Acc.\ (\%) & Ep.\ Bal.\ Acc.\ (\%) \\
683	\midrule
684	Qwen3-0.6B & $56.4 \pm 3.5$ & $50.7 \pm 2.6$ \\
685	Qwen3-1.7B & $58.2 \pm 4.0$ & $43.1 \pm 1.0$ \\
686	Qwen3-4B & $59.2 \pm 3.5$ & $\mathbf{59.0 \pm 1.9}$ \\
687	\midrule
688	Always-det & 50.0 & 50.0 \\
689	\bottomrule
690	\end{tabular}
691	\caption{Capacity scaling: step-level and episode-level balanced accuracy (4 seeds, identical configuration across all scales). Step-level accuracy is flat ($56$--$59\%$, within seed variance). At episode level, only 4B breaks the random baseline ($59.0\%$, $p < 0.005$).}
692	\label{tab:capacity}
693	\end{table}
694	
695	Step-level balanced accuracy is flat across scales ($56$--$59\%$, within seed variance); step-level discrimination is not capacity-sensitive. At episode level, only 4B breaks the random baseline ($59.0 \pm 1.9\%$, $p < 0.005$); 0.6B and 1.7B remain at or below chance. The 1.7B model's below-chance episode-level accuracy ($43.1\%$) may reflect overfitting to spurious step-level correlations that anti-correlate with episode outcomes; without per-class confusion matrices at this scale, this remains a hypothesis. The dominant explanation across scales is that death avoidance constitutes a task-type-level binary signal that a step-level router cannot exploit efficiently.
696	
697	\paragraph{Generative router.} A generative routing model trained with explicit routing labels achieves balanced accuracy of 46.7\%, confirming that the routing bottleneck is signal-limited, not architecture-limited.
698	
699	\paragraph{Leave-one-task-type-out routing.} Under leave-one-task-type-out evaluation, blind routing collapses to always-deterministic (balanced accuracy 50.0\%); a keyword-based variant achieves 62.9\% only through task-identity leakage, not genuine routing signal. A guided router evaluated under the same protocol confirms this: without task-type identifiers it achieves chance accuracy (50.0\%), and leaking task names raises this to 62.9\%, confirming that the only learnable routing feature is task-type identity.
700	
701	\paragraph{Death-proximal labeling.} Training a router only on the $k$ steps preceding death events (rather than all steps) also collapses to majority-class prediction (step balanced accuracy 50.0\%, episode balanced accuracy 50.0\%, internal recall 0\%), confirming that the absence of step-level signal is not an artifact of label dilution across long episodes.
702	
703	\paragraph{Reasoning depth.} An ablation comparing chain-of-thought reasoning against direct-answer generation on 6 task types ($n{=}120$ episodes per condition, 6 tasks $\times$ 20 episodes per task) found no significant difference (Mann--Whitney $p > 0.26$, $|d| \leq 0.31$) and near-identical death rates (41.8\% vs.\ 42.5\%); reasoning depth does not meaningfully alter internal-mode outcomes.
704	
705	\section{Threshold Routing Analysis}
706	\label{sec:threshold-routing}
707	
708	Given per-task death risk knowledge, we test whether a simple threshold routing strategy can outperform always-deterministic. For each threshold $t \in [0, 1]$, we route to internal if the per-task internal death rate $\leq t$, otherwise to deterministic, and sweep all thresholds to find the optimal.
709	
710	\begin{table}[h]
711	\centering
712	\small
713	\resizebox{\columnwidth}{!}{%
714	\begin{tabular}{lccc}
715	\toprule
716	Strategy & Mean Score & Death Rate & $\Delta$ vs Det \\
717	\midrule
718	Always-det & $-9.47$ & $0.163$ & $0.00$ \\
719	Optimal threshold ($t{=}0$) & $-11.03$ & $0.155$ & $-1.56$ \\
720	Always-internal & $-39.07$ & $0.429$ & $-29.60$ \\
721	\bottomrule
722	\end{tabular}}
723	\caption{Death-risk threshold routing analysis on 245 episodes. The optimal threshold routes only \texttt{find-non-living-thing} (the sole zero-death task) to internal, with all other tasks routed to deterministic. Bootstrap 95\% CI for the difference: $[-8.87, +5.92]$.}
724	\label{tab:threshold-routing}
725	\end{table}
726	
727	Even with perfect per-task death risk knowledge, threshold routing cannot outperform always-deterministic. The sole zero-death task achieves higher scores under deterministic (+28.5) than internal (+18.9), leaving no room for a beneficial mixed strategy.
728	
729	\section{Practitioner Decision Framework}
730	\label{app:decision-framework}
731	
732	Given a new interactive environment, the following three-stage procedure diagnoses whether learned routing adds value over a fixed deterministic strategy.
733	
734	\paragraph{Stage 1: Pilot collection (${\sim}$50 episodes).}
735	Run pure-internal and pure-deterministic strategies on a representative sample (${\sim}$50 episode pairs). Compute the death-rate differential $\Delta\text{DR} = \text{DR}_{\text{int}} - \text{DR}_{\text{det}}$.
736	
737	\paragraph{Stage 2: Death dominance check.}
738	If $\Delta\text{DR} > 15$~pp, death asymmetry is likely the dominant routing signal. Compute the death-label fraction $f_{\text{death}}$: the proportion of non-tie routing labels where exactly one strategy dies.
739	
740	\paragraph{Stage 3: Decision.}
741	If $f_{\text{death}} > 75\%$, the routing signal is death-dominated; a fixed deterministic strategy will match or exceed any learned router. If $f_{\text{death}} < 50\%$, diverse routing signals may justify a learned router. Between 50\%--75\%, collect additional episodes to reduce estimation noise before committing to router development.
742	
743	\paragraph{Retrospective validation.}
744	All four experimental conditions in this paper are correctly classified:
745	
746	\begin{table}[h]
747	\centering
748	\small
749	\begin{tabular}{@{}lrrll@{}}
750	\toprule
751	Condition & $\Delta$DR & $f_{\text{death}}$ & Prediction & Actual \\
752	\midrule
753	Qwen-7B & +26.5 & 78.9\% & det-fixed & det wins \\
754	Llama-8B & +30.0 & $>$75\% & det-fixed & det wins \\
755	Qwen-72B & +27.8 & $>$75\% & det-fixed & det wins \\
756	MATH & +0.5 & 0\% & router viable & no signal \\
757	\bottomrule
758	\end{tabular}
759	\caption{Retrospective validation of the decision framework. All four conditions are correctly classified (4/4).}
760	\label{tab:decision-framework}
761	\end{table}
762	
763	The framework also predicts the inverted-U relationship between capability and death risk: below ${\sim}$0.5B parameters, agents rarely reach dangerous states (13.3\% death rate in a 15-episode pilot), so $\Delta\text{DR}$ is low and the framework would not recommend fixed-deterministic. Above ${\sim}$7B, agents are capable enough to enter catastrophic states but not capable enough to avoid them, producing high $\Delta\text{DR}$.
764	
765	\paragraph{Threshold calibration.} The thresholds above (15~pp, 75\%, 50\%) are illustrative, derived from ScienceWorld's specific reward structure (binary death penalty $P{=}100$, sparse terminal rewards). Environments with graded penalties, dense rewards, or qualitatively different failure modes may require different thresholds. Practitioners should calibrate these boundaries for their specific environment.
766	
767	\section{Extended Validation of Excluded Tasks}
768	\label{app:extended-validation}
769	
770	To verify that task exclusion does not bias toward death-prone tasks, we collect $n{=}20$ episodes for five representative excluded tasks spanning all exclusion categories (Table~\ref{tab:extended-val}).
771	
772	\begin{table}[h]
773	\centering
774	\small
775	\resizebox{\columnwidth}{!}{%
776	\begin{tabular}{lcrrrrc}
777	\toprule
778	Task & Category & $n$ & Int DR & Det DR & $\Delta$DR & D/I/N \\
779	\midrule
780	boil & dev-set & 20 & 55\% & 25\% & +30\,pp & 6/0/14 \\
781	melt & dev-set & 20 & 45\% & 20\% & +25\,pp & 7/2/11 \\
782	find-living-thing & taxonomic & 20 & 55\% & 15\% & +40\,pp & 10/0/10 \\
783	use-thermometer & agent-floor & 20 & 50\% & 20\% & +30\,pp & 7/1/12 \\
784	power-component & agent-floor & 20 & 50\% & 15\% & +35\,pp & 7/0/13 \\
785	\midrule
786	\textit{Mean (5 tasks)} & & 100 & 51.0\% & 19.0\% & +32.0\,pp & 37/3/60 \\
787	\bottomrule
788	\end{tabular}}
789	\caption{Extended validation ($n{=}20$) of representative excluded task types. All five tasks confirm death asymmetry; mean $\Delta$DR $= +32.0$\,pp is consistent with the $n{=}5$ prescreening estimate for these same tasks (Table~\ref{tab:excluded-death}).}
790	\label{tab:extended-val}
791	\end{table}
792	
793	Notably, the excluded-task aggregate DAF (0.991) exceeds the included-task DAF (0.904; Table~\ref{tab:per-task}), indicating that excluded tasks are \emph{more} death-dominated than included tasks---the opposite of a cherry-picking bias.
794	
795	\section{Agent Prompt Templates}
796	\label{app:prompt-templates}
797	
798	Below we show the complete prompt templates used for agent interaction in ScienceWorld. Both the internal (ReAct) and deterministic strategies share the same system prompt but differ in the user message template.
799	
800	\paragraph{System prompt (shared).} Used for all ScienceWorld agent interactions across both computation modes.
801	
802	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
803	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
804	  left=2mm, right=2mm, top=1mm, bottom=1mm}
805	You are an agent interacting with a ScienceWorld text
806	environment. Your goal is to complete the given task by
807	choosing actions from the available action list.
808	
809	Use the following format for each step:
810	Thought: &lt;your reasoning about what to do next>
811	Action: &lt;exact action string from the valid actions list>
812	
813	Rules:
814	- You MUST choose an action from the valid actions list.
815	  Do not invent actions.
816	- Think step by step about what physical/scientific
817	  process is needed.
818	- Pay attention to the current observation for clues
819	  about object states.
820	\end{tcblisting}
821	
822	\paragraph{Internal (ReAct) user template.} At each step, the agent receives the current observation, valid action list, and recent action history, and must select a single action.
823	
824	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
825	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
826	  left=2mm, right=2mm, top=1mm, bottom=1mm}
827	Current observation:
828	{observation}
829	
830	Valid actions:
831	{valid_actions_str}
832	
833	Previous actions taken: {history_str}
834	
835	Choose your next action.
836	\end{tcblisting}
837	
838	\paragraph{Deterministic candidate generation template.} For the deterministic strategy, the agent generates ranked candidate actions instead of selecting one; these candidates are then evaluated via simulator forking (\S\ref{sec:method}).
839	
840	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
841	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
842	  left=2mm, right=2mm, top=1mm, bottom=1mm}
843	Current observation:
844	{observation}
845	
846	Valid actions:
847	{valid_actions_str}
848	
849	Previous actions taken: {history_str}
850	
851	Generate the top 3 most promising actions from the valid
852	actions list, ranked by how likely they are to make
853	progress on the task. Output exactly 3 actions, one per
854	line, in this format:
855	1. &lt;action>
856	2. &lt;action>
857	3. &lt;action>
858	\end{tcblisting}
859	
860	\paragraph{Reflexion self-reflection prompt.} After a failed episode, the Reflexion agent (\S\ref{sec:agent-improvement}) generates a reflection that is injected into subsequent trial attempts as additional system context.
861	
862	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
863	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
864	  left=2mm, right=2mm, top=1mm, bottom=1mm}
865	You just completed an episode in a ScienceWorld text
866	environment but failed.
867	
868	Task: {task_name}
869	Final score: {final_score}
870	Outcome: {outcome}
871	Number of steps taken: {num_steps}
872	
873	Here is a summary of your actions:
874	{action_summary}
875	
876	Analyze why this episode failed and provide a short
877	strategy for the next attempt. Focus on:
878	1. What went wrong (wrong sequence, missed key step,
879	   dangerous action)?
880	2. What should be done differently next time?
881	
882	Keep your reflection under 200 words.
883	\end{tcblisting}
884	
885	\paragraph{Grounding warning (ablation).} The prompt warning condition in the grounding ablation (Appendix~\ref{app:grounding-ablation}) appends the following to the shared system prompt:
886	
887	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
888	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
889	  left=2mm, right=2mm, top=1mm, bottom=1mm}
890	CRITICAL SAFETY RULE: The 'focus on [object]' action is
891	ONLY for submitting your final answer. Do NOT use
892	'focus on' to examine, inspect, or interact with objects
893	during exploration. Using 'focus on' on the wrong object
894	will cause irreversible failure. Use 'look at',
895	'examine', or 'pick up' instead for exploration.
896	\end{tcblisting}
897	
898	\noindent The key difference between the two computation modes is the user message: the internal strategy asks the LLM to \emph{select} one action (ReAct), while the deterministic strategy asks it to \emph{rank} candidates for simulator evaluation. Both use identical system prompts and identical observation formatting.
899	
900	\section{Non-Death Episode Case Study}
901	\label{app:non-death-case-study}
902	
903	We illustrate the framework's ability to decompose non-death routing signal using \texttt{find-non-living-thing}, the only task type with zero deaths and 100\% non-death labels (\S\ref{sec:death-decomp}). Using Gemma-2-9B-it counterfactual episodes ($N{=}20$), 12 episodes show routing preference (9 deterministic-preferred, 3 internal-preferred), confirming the framework detects bidirectional signal independent of death asymmetry.
904	
905	\paragraph{Deterministic-preferred: knowledge retrieval advantage.}
906	In Episode~3 (det: 67, int: 0), the internal strategy issues nonsensical \texttt{connect} actions for 18 consecutive steps (e.g., ``connect air to outside,'' ``connect axe to door to foundry'') without ever identifying a target object; the deterministic strategy correctly focuses on ``orange'' (+58) and opens the kitchen door (+9). In Episode~17 (det: 58, int: 50), both strategies find a valid non-living thing, but the deterministic strategy selects a higher-scoring object (orange, 58\,pts) versus the internal strategy's choice (fountain, 50\,pts), illustrating that object selection quality creates routing signal even when both strategies succeed.
907	
908	\paragraph{Internal-preferred: semantic reasoning advantage.}
909	In Episode~12 (int: 67, det: 58), the task specifies ``move it to the red box in the living room.'' The deterministic strategy focuses on the red box itself---the destination container, not a separate non-living thing---scoring 58\,pts. The internal strategy correctly distinguishes target from container, choosing ``orange'' (67\,pts). This semantic error demonstrates that deterministic pattern-matching can miss task-structure subtleties that internal reasoning captures.
910	
911	These cases confirm two properties: (1)~the framework captures non-death routing signal when it exists, and (2)~signal flows in both directions---neither strategy uniformly dominates in death-free tasks.
912	
913	\paragraph{Systematic analysis of non-death labels.}
914	All 20 non-death non-tie labels in the primary Qwen2.5-7B analysis originate from \texttt{find-non-living-thing}---the sole death-free task type. In every other task type, non-tie episodes involve at least one strategy dying. We classify the 20 episodes into three error categories:
915	
916	\begin{table}[h]
917	\centering
918	\small
919	\begin{tabular}{@{}lrrr@{}}
920	\toprule
921	Error category & Det-pref & Int-pref & Total \\
922	\midrule
923	Hallucination-induced & 8 & 2 & 10 \\
924	Object selection quality & 6 & 1 & 7 \\
925	Action selection error & 2 & 1 & 3 \\
926	\bottomrule
927	\end{tabular}
928	\caption{Non-death non-tie episode classification. Hallucination-induced: agent's state model is incorrect (e.g., believing \texttt{eat} completes the task). Object selection quality: both strategies succeed but choose different-value objects. Action selection: correct state model but suboptimal action sequences.}
929	\label{tab:non-death-taxonomy}
930	\end{table}
931	
932	\noindent Hallucination-induced errors dominate (50\%), driven by a recurring ``eat before focus'' pattern: the internal strategy consumes the target object (destroying it) before attempting the scoring action (\texttt{focus on}), indicating an incorrect state model that equates eating with task completion (11 of 20 episodes). Object selection quality accounts for 35\%---typically the deterministic strategy selecting ``orange'' (58\,pts) while the internal strategy settles for lower-value objects (``fountain'' or ``picture,'' 50\,pts). The error categories are bidirectional: 2 of 10 hallucination episodes and 1 of 3 action selection episodes are internal-preferred, confirming the framework detects failures in both strategies. Score gaps reflect category severity: hallucination errors produce large gaps ($17$--$67$\,pts, one strategy scores zero) while object selection differences produce small gaps ($8$--$9$\,pts, both strategies functional).
933	
934	\end{document}
935	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d5ff0e9-0f56-4486-87f5-b7f1a2076d1d",
  "isSidechain": true,
  "promptId": "5c9e987c-ae70-4ee6-a464-2d2db13505c8",
  "agentId": "abba625f7ac93e545",
  "type": "user",
  "uuid": "7632900d-8009-4c94-b100-945d7fd78aff",
  "sourceToolAssistantUUID": "4d5ff0e9-0f56-4486-87f5-b7f1a2076d1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-23T10:43:21.673Z_

Let me search for more specific information about Qwen seed replication experiments in the registry and look at the exact section of the Limitations that mentions seed robustness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7632900d-8009-4c94-b100-945d7fd78aff",
  "isSidechain": true,
  "agentId": "abba625f7ac93e545",
  "requestId": "req_011CbKMyVgcapb6ybBirzFjU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2aad9d44-a4a0-4639-8f35-532fe9b1ec7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TCaaVnn8W5cVPRfwSxQoq5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 27088,
      "cache_read_input_tokens": 33550,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27088,
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

_source line 12 · 2026-05-23T10:43:22.413Z_

<details open><summary>🔧 Tool call — Grep · `toolu_0163aVqteB99NfYfdmPrDM67`</summary>

```json
{
  "pattern": "seed.*replication|qwen.*seed|N=220.*DAF.*89|gemma.*89\\.7",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/registry.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2aad9d44-a4a0-4639-8f35-532fe9b1ec7b",
  "isSidechain": true,
  "agentId": "abba625f7ac93e545",
  "requestId": "req_011CbKMyVgcapb6ybBirzFjU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6e51d33b-1aaa-411b-a4db-1704e4a2c2b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TCaaVnn8W5cVPRfwSxQoq5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 27088,
      "cache_read_input_tokens": 33550,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27088,
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

_source line 13 · 2026-05-23T10:43:22.448Z_

<details><summary>↩ Tool result · `toolu_0163aVqteB99NfYfdmPrDM67`</summary>

```text
4939:  seed-123-replication:
4967:      eval_data: 11 ScienceWorld tasks x 20 episodes, seed=123 replication
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e51d33b-1aaa-411b-a4db-1704e4a2c2b1",
  "isSidechain": true,
  "promptId": "5c9e987c-ae70-4ee6-a464-2d2db13505c8",
  "agentId": "abba625f7ac93e545",
  "type": "user",
  "uuid": "3ea391f3-d840-45e7-992c-b04be7b57cde",
  "sourceToolAssistantUUID": "6e51d33b-1aaa-411b-a4db-1704e4a2c2b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-23T10:43:22.869Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UWidUhEv7D34h7vYsBbZF3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/registry.yaml",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ea391f3-d840-45e7-992c-b04be7b57cde",
  "isSidechain": true,
  "agentId": "abba625f7ac93e545",
  "requestId": "req_011CbKMyVgcapb6ybBirzFjU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1380a044-1058-419d-b5b8-b0ef8d63c598",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TCaaVnn8W5cVPRfwSxQoq5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 27088,
      "cache_read_input_tokens": 33550,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27088,
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

_source line 15 · 2026-05-23T10:43:22.884Z_

<details><summary>↩ Tool result · `toolu_01UWidUhEv7D34h7vYsBbZF3`</summary>

```text
1	baseline: null
2	experiments:
3	  alfworld-counterfactual-dryrun:
4	    completed_at: '2026-05-14T13:49:47.760Z'
5	    conclusion: success
6	    created_at: '2026-05-14T13:49:17.349Z'
7	    hypothesis: 'ALFWorld counterfactual pipeline dry-run: internal (no admissible
8	      actions) vs deterministic (with admissible actions). 5 tasks from look_at_obj_in_light
9	      type.'
10	    metrics:
11	      alfworld_version: 0.4.2
12	      all_no_preference: true
13	      det_success: 1
14	      internal_success: 1
15	      n_tasks: 5
16	      pipeline_validated: true
17	      task_type: look_at_obj_in_light
18	      task_types_available: 6
19	      total_games_available: 140
20	    retry_count: 0
21	    spec:
22	      checkpoint_path: src/alfworld_counterfactual.py
23	      command: python src/alfworld_counterfactual.py --n_tasks 5 --task_types look_at_obj_in_light
24	      data_count: 5
25	      data_path: /root/autodl-tmp/alfworld_data/json_2.1.1/valid_seen
26	      log_path: /root/autodl-tmp/simgate-modular-routing/results/alfworld_dryrun/
27	      model_name: Qwen2.5-7B-Instruct
28	      seed: 42
29	      server: westb-13313
30	    status: DONE
31	    updated_at: '2026-05-14T13:49:55.239Z'
32	  alfworld-counterfactual-full:
33	    completed_at: '2026-05-14T17:46:45.653Z'
34	    conclusion: success
35	    created_at: '2026-05-14T13:56:11.695Z'
36	    hypothesis: 'ALFWorld 全量 counterfactual 收集: 135 games, 6 task types. Internal
37	      (no admissible actions) vs Deterministic (with admissible actions). 预计 ~3.5h.
38	      D044: 不承诺纳入论文，看结果决定是否作为 supplementary/future work.'
39	    metrics:
40	      det_preferred: 35
41	      det_preferred_pct: 25.9
42	      det_success_rate: 27.4
43	      internal_preferred: 2
44	      internal_preferred_pct: 1.5
45	      internal_success_rate: 3
46	      n_games: 135
47	      no_preference: 98
48	      no_preference_pct: 72.6
49	    retry_count: 0
50	    spec:
51	      checkpoint_path: /root/autodl-tmp/simgate-modular-routing/results/alfworld_counterfactual/episodes.jsonl
52	      command: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
53	        && CUDA_VISIBLE_DEVICES=1 python src/alfworld_counterfactual.py --n_tasks
54	        140 --output results/alfworld_counterfactual/episodes.jsonl --seed 42
55	      data_count: 140
56	      data_path: /root/autodl-tmp/alfworld_data/json_2.1.1/valid_seen
57	      gpu: cuda:1
58	      log_path: /root/autodl-tmp/simgate-modular-routing/results/alfworld_counterfactual/run.log
59	      model_name: Qwen2.5-7B-Instruct
60	      seed: 42
61	      server: westb-13313
62	      tmux_session: alfworld_cf
63	    status: DONE
64	    updated_at: '2026-05-14T17:46:45.652Z'
65	  gpu0-v6-lifespan:
66	    completed_at: '2026-05-14T04:52:47.621Z'
67	    conclusion: killed
68	    created_at: '2026-05-14T04:19:08.846Z'
69	    hypothesis: GPU0 干净重收 lifespan-longest-lived 全量 20 eps（SLIM_EPISODES=1，从 ep0 开始）。之前数据文件损坏（150GB），已删除后重启。plan-001b
70	      最后 3 个未完成 task 之一。
71	    notes: Director 指令主动终止。lifespan-longest-lived 已收 23 eps（超额3），数据充足。GPU0 释放给 plan-002
72	      dry-run。
73	    retry_count: 0
74	    spec:
75	      account: root
76	      backend: tmux
77	      command: SLIM_EPISODES=1 bash scripts/run_gpu0_v6_lifespan.sh (lifespan-longest-lived
78	        20 eps from ep0)
79	      data_count: 20 episodes
80	      data_path: results/plan_c/lifespan-longest-lived/
81	      gpu:
82	      - cuda:0
83	      gpu_hours: 0.56
84	      log_path: ~/runs/simgate-modular-routing/gpu0-v6-lifespan.log
85	      model_name: Qwen2.5-7B-Instruct
86	      pid: '36874'
87	      seed: default
88	      server: westb-13313
89	      submitted_at: '2026-05-14T04:19:08.547Z'
90	      submitted_via: submit_training_job
91	      wall_clock_seconds: 2019.1
92	    status: DONE
93	    updated_at: '2026-05-14T04:52:49.472Z'
94	  llama-cross-model-expanded:
95	    checkpoint_path: N/A (killed per D056)
96	    completed_at: '2026-05-15T12:33:39.906Z'
97	    conclusion: killed
98	    created_at: '2026-05-15T11:32:13.459Z'
99	    hypothesis: Death avoidance pattern (internal dies more than deterministic) generalizes
100	      across model families. Expanding Llama-3.1-8B from 2 tasks/10 pairs to 7 tasks/35
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1380a044-1058-419d-b5b8-b0ef8d63c598",
  "isSidechain": true,
  "promptId": "5c9e987c-ae70-4ee6-a464-2d2db13505c8",
  "agentId": "abba625f7ac93e545",
  "type": "user",
  "uuid": "342543d7-1dda-446c-bdce-ba34d7f5eec4",
  "sourceToolAssistantUUID": "1380a044-1058-419d-b5b8-b0ef8d63c598",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-23T10:43:23.417Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01YZTc3kbG6wD1cfznnYSvVJ`</summary>

```json
{
  "pattern": "Gemma|cross-model|cross model|N=220",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "342543d7-1dda-446c-bdce-ba34d7f5eec4",
  "isSidechain": true,
  "agentId": "abba625f7ac93e545",
  "requestId": "req_011CbKMyVgcapb6ybBirzFjU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1c23ace6-df58-43f6-a040-c11be0399d63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TCaaVnn8W5cVPRfwSxQoq5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 27088,
      "cache_read_input_tokens": 33550,
      "output_tokens": 402,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 27088
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 402,
          "cache_read_input_tokens": 33550,
          "cache_creation_input_tokens": 27088,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 27088,
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

_source line 17 · 2026-05-23T10:43:23.443Z_

<details><summary>↩ Tool result · `toolu_01YZTc3kbG6wD1cfznnYSvVJ`</summary>

```text
37-\section*{Limitations}
38-
39-\paragraph{Environmental scope.}
40:[Omitted long matching line]
41-
42-\paragraph{Methodological constraints.}
43-[Omitted long context line]
--
53-
54-\section*{Ethics Statement}
55-
56:[Omitted long matching line]
57-
58-\bibliography{references}
59-
--
72-\hyperref[app:seed-robustness]{J.~Seed Robustness} $\cdot$
73-\hyperref[app:penalty]{K.~Penalty Sensitivity} $\cdot$
74-\hyperref[app:cross-env-details]{L.~Cross-Environment Details} $\cdot$
75:\hyperref[app:cross-model]{M.~Cross-Model Verification} $\cdot$
76-\hyperref[app:failure-modes]{N.~Failure Mode Analysis} $\cdot$
77-\hyperref[app:grounding-ablation]{O.~Grounding Ablation} $\cdot$
78-\hyperref[app:ablations]{P.~Ablation Studies} $\cdot$
--
562-The $N{=}795$ MATH problems span two categories from the MATH test set~\citep{math-2021} (Levels 4--5): Algebra (585, 73.6\%) and Counting \& Probability (210, 26.4\%). The category imbalance reflects the relative sizes in the original test set.
563-
564-\section{Cross-Model Verification}
565:\label{app:cross-model}
566-
567:We replicate the counterfactual analysis with Llama-3.1-8B-Instruct across all 11 task types ($N{=}220$ episode pairs, 20 per type; Table~\ref{tab:cross-model-detail}).
568-The internal strategy dies in $41.4\%$ of episodes versus $11.4\%$ for deterministic (death-rate differential $+30.0$~pp), with 83 deterministic-preferred, 3 internal-preferred (1.4\%, all death-asymmetry reversals), and 134 no-preference labels.
569-Both models exhibit nearly identical internal vulnerability (${\sim}$42\%: Qwen $42.9\%$, Llama $41.4\%$), confirming that death-prone failure is empirically dominated by the task environment rather than model-specific factors. The differential magnitude varies ($+26.5$~pp Qwen, $+30.0$~pp Llama) because deterministic strategy safety is model-dependent ($16.3\%$ vs.\ $11.4\%$), but directional consistency is 100\% (10/10 death-prone tasks in both models).
570:\texttt{identify-life-stages-1} shows cross-model precision matching ($55\%$/$10\%$/$+45$~pp in both models).
571-\texttt{find-non-living-thing} shows zero deaths in both models, consistent with its majority-class answer distribution.
572-
573-\begin{table}[h]
--
593-\textbf{Aggregate} & \textbf{41.4} & \textbf{11.4} & \textbf{+30.0} & \textbf{83 / 3 / 134} \\
594-\bottomrule
595-\end{tabular}}%
596:\caption{Per-task Llama-3.1-8B cross-model replication ($N{=}20$ per task). D/I/N: deterministic-preferred / internal-preferred / no-preference. Sorted by $\Delta$ DR descending.}
597:\label{tab:cross-model-detail}
598-\end{table}
599-
600-\paragraph{Cross-model and cross-environment summary.}
601:Table~\ref{tab:cross-model-env} consolidates replication results across model families and environments.
602-
603-\begin{table}[h]
604-\centering
--
610-\midrule
611-Qwen2.5-7B & ScienceWorld & 245 & 42.9\% & 16.3\% & +26.5 & 90.4\% & [81.1, 99.0] & death \\
612-Llama-3.1-8B & ScienceWorld & 220 & 41.4\% & 11.4\% & +30.0 & 88.2\% & [80.2, 95.1] & death \\
613:Gemma-2-9B-it & ScienceWorld & 220 & 36.4\% & 14.1\% & +22.3 & 89.7\% & [79.5, 98.4] & death \\
614-Qwen2.5-72B & ScienceWorld & 255 & 30.6\% & 2.75\% & +27.8 & 92.4\% & --- & death \\
615-\midrule
616-Qwen2.5-7B & ALFWorld & 135 & 0\% & 0\% & 0 & 0\% & --- & info-asym \\
--
619-Qwen2.5-7B & MATH & 795 & N/A & N/A & N/A & N/A & N/A & none \\
620-\bottomrule
621-\end{tabular}}
622:[Omitted long matching line]
623:\label{tab:cross-model-env}
624-\end{table}
625-
626-\section{Failure Mode Analysis}
--
900-\section{Non-Death Episode Case Study}
901-\label{app:non-death-case-study}
902-
903:We illustrate the framework's ability to decompose non-death routing signal using \texttt{find-non-living-thing}, the only task type with zero deaths and 100\% non-death labels (\S\ref{sec:death-decomp}). Using Gemma-2-9B-it counterfactual episodes ($N{=}20$), 12 episodes show routing preference (9 deterministic-preferred, 3 internal-preferred), confirming the framework detects bidirectional signal independent of death asymmetry.
904-
905-\paragraph{Deterministic-preferred: knowledge retrieval advantage.}
906-[Omitted long context line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c23ace6-df58-43f6-a040-c11be0399d63",
  "isSidechain": true,
  "promptId": "5c9e987c-ae70-4ee6-a464-2d2db13505c8",
  "agentId": "abba625f7ac93e545",
  "type": "user",
  "uuid": "e664e6e0-d066-40d2-903a-e928a697eaec",
  "sourceToolAssistantUUID": "1c23ace6-df58-43f6-a040-c11be0399d63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-23T10:43:24.675Z_

Perfect! I found the critical information. Let me verify by looking at the specific section on the Limitations where the claim is made.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e664e6e0-d066-40d2-903a-e928a697eaec",
  "isSidechain": true,
  "agentId": "abba625f7ac93e545",
  "requestId": "req_011CbKMyokoHGG9NCoB2VEkv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ff5355b8-2ff1-4e2c-b22e-ea99bc499a2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BFUazgzUrbTYfqEGUrVRkA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3882,
      "cache_read_input_tokens": 60638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3882,
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

_source line 19 · 2026-05-23T10:43:25.722Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EwjSErA8jZDHUrZCxz2q1j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "offset": 36,
  "limit": 8
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff5355b8-2ff1-4e2c-b22e-ea99bc499a2a",
  "isSidechain": true,
  "agentId": "abba625f7ac93e545",
  "requestId": "req_011CbKMyokoHGG9NCoB2VEkv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5d209219-c41a-431b-a8a4-4678d84095eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BFUazgzUrbTYfqEGUrVRkA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3882,
      "cache_read_input_tokens": 60638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3882,
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

_source line 20 · 2026-05-23T10:43:25.737Z_

<details><summary>↩ Tool result · `toolu_01EwjSErA8jZDHUrZCxz2q1j`</summary>

```text
36	
37	\section*{Limitations}
38	
39	\paragraph{Environmental scope.}
40	Our primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct), though extended validation of representative excluded tasks confirms the pattern (Appendix~\ref{app:extended-validation}). The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\ref{app:penalty}). The 19 excluded task types (63\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface non-death-dominated signal that our current setup does not capture. Cross-environment analyses on MATH and ALFWorld (\S\ref{sec:cross-env}, \S\ref{sec:discussion}) provide preliminary supporting evidence but do not conclusively establish generalization. A Llama-3.1-8B-Instruct cross-model replication (11 task types, $N{=}220$; \S\ref{sec:cross-model}) shows death dominance replicates with direction consistency 10/10 while vulnerability magnitude varies ($+30.0$~pp vs.\ Qwen $+26.5$~pp), though both models are in the 7--8B parameter range; Qwen2.5-72B ($10{\times}$ scale) reduces death rate but does not eliminate death dominance (\S\ref{sec:agent-improvement}); validation beyond 72B remains future work. The 72B probe is limited to a single model without cross-model replication at scale; whether death avoidance remains dominant for frontier models with substantially lower failure rates is an open question. Our quantitative results (DAF $= 90.4\%$, label fractions) are specific to ScienceWorld; the framework's generality claim is methodological (the diagnostic procedure applies to any environment with asymmetric fatal outcomes), not empirical (the specific percentages may differ across environments).
41	
42	\paragraph{Methodological constraints.}
43	Our internal-reasoning baseline uses single-pass ReAct~\citep{react-2023}. Reflexion~\citep{reflexion-2023} reduces death rate from 42.9\% to 31.4\% (\S\ref{sec:agent-improvement}), but more aggressive self-correction or Tree-of-Thought backtracking~\citep{tot-2023} may further reduce internal death rates. Episode-level labels assign a single routing preference to entire episodes, which may be suboptimal for individual steps (particularly those preceding death events). However, of 2{,}040 training steps only 0.3\% exhibit strict directional conflict (step-level oracle opposite to episode label); the remaining apparent mislabeling consists of episode labels applied to steps where neither strategy has a step-level advantage (60.3\% pre-event neutral). The issue is granularity mismatch (applying correct-direction labels to uninformative steps), not directional error. Training on pure-strategy trajectories also introduces distribution shift at deployment~\citep{dagger-2011}. Grounding ablation reduces but does not eliminate the death rate differential (from $+26.6$\,pp to approximately $+8$\,pp; Appendix~\ref{app:grounding-ablation}); a full post-ablation counterfactual decomposition remains important future work. Under mixed-strategy routing with oracle death prediction, switching to deterministic at the step before death could reduce the internal death rate; even under optimistic assumptions (perfect step-level death prediction), a residual gap of ${>}10$~pp between strategies is expected, as fatal trajectories involve cumulative hallucination errors preceding the death event. More broadly, projecting episode-level labels onto 10--50 sequential steps with path-dependent state introduces compounding error: early routing decisions alter the state trajectory, potentially invalidating later labels derived from the episode outcome.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d209219-c41a-431b-a8a4-4678d84095eb",
  "isSidechain": true,
  "promptId": "5c9e987c-ae70-4ee6-a464-2d2db13505c8",
  "agentId": "abba625f7ac93e545",
  "type": "user",
  "uuid": "6f2a53bd-d146-4d09-b49c-024fbfabddc4",
  "sourceToolAssistantUUID": "5d209219-c41a-431b-a8a4-4678d84095eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T10:43:26.148Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016ybNLWP9H4ossvRGuz49nz`</summary>

```json
{
  "command": "grep -n \"independent seed replication\\|seed.*replication\\|89\\.7\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f2a53bd-d146-4d09-b49c-024fbfabddc4",
  "isSidechain": true,
  "agentId": "abba625f7ac93e545",
  "requestId": "req_011CbKMyokoHGG9NCoB2VEkv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a4ff1174-a5a2-40ab-81bd-2a823feab5bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BFUazgzUrbTYfqEGUrVRkA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3882,
      "cache_read_input_tokens": 60638,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3882
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 242,
          "cache_read_input_tokens": 60638,
          "cache_creation_input_tokens": 3882,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3882,
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

_source line 22 · 2026-05-23T10:43:26.329Z_

<details><summary>↩ Tool result · `toolu_016ybNLWP9H4ossvRGuz49nz`</summary>

```text
613:Gemma-2-9B-it & ScienceWorld & 220 & 36.4\% & 14.1\% & +22.3 & 89.7\% & [79.5, 98.4] & death \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4ff1174-a5a2-40ab-81bd-2a823feab5bb",
  "isSidechain": true,
  "promptId": "5c9e987c-ae70-4ee6-a464-2d2db13505c8",
  "agentId": "abba625f7ac93e545",
  "type": "user",
  "uuid": "81126dd8-8fda-427a-b2ce-8740622397de",
  "sourceToolAssistantUUID": "a4ff1174-a5a2-40ab-81bd-2a823feab5bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-23T10:43:27.567Z_

Now let me check the registry more carefully for any Qwen seed replication experiments with those specific metrics:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81126dd8-8fda-427a-b2ce-8740622397de",
  "isSidechain": true,
  "agentId": "abba625f7ac93e545",
  "requestId": "req_011CbKMz24izoZ6DsJ2vNiPw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "98f67622-c6e4-4396-b9cd-1836d82081bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Kziyj3A32deQsz7p6LPojB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1293,
      "cache_read_input_tokens": 64520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1293,
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

_source line 24 · 2026-05-23T10:43:28.714Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EagzqA9BKHeyQTWAERsw8z`</summary>

```json
{
  "command": "grep -A 20 \"seed.*replication\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/registry.yaml | head -60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98f67622-c6e4-4396-b9cd-1836d82081bc",
  "isSidechain": true,
  "agentId": "abba625f7ac93e545",
  "requestId": "req_011CbKMz24izoZ6DsJ2vNiPw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "68163f9e-c4d3-4b2f-9a6d-a3ff39c1923a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Kziyj3A32deQsz7p6LPojB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1293,
      "cache_read_input_tokens": 64520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1293,
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

_source line 25 · 2026-05-23T10:43:28.788Z_

<details><summary>↩ Tool result · `toolu_01EagzqA9BKHeyQTWAERsw8z`</summary>

```text
  seed-123-replication:
    status: DONE
    retry_count: 0
    created_at: '2026-05-18T08:07:59.713Z'
    updated_at: '2026-05-18T11:15:45.495Z'
    hypothesis: seed=123 重复 plan-012-full (seed=42) 的 episode-level counterfactual
      collection，验证 DAF=90.4% 和 death dominance 结论的 seed robustness——若两个 seed 的 DAF
      差异 <5pp 且方向一致，则排除 seed artifact
    parent: seed-robustness-extended
    spec:
      command: 4 GPU parallel episode_level_collection.py
      server: westd-18266
      gpu:
      - cuda:0
      - cuda:1
      - cuda:2
      - cuda:3
      pid: '28559'
      log_path: /root/autodl-tmp/simgate-modular-routing/logs/seed123-gpu0.log
      submitted_at: '2026-05-18T08:09:24.632Z'
      submitted_via: submit_training_job
--
      eval_data: 11 ScienceWorld tasks x 20 episodes, seed=123 replication
      checkpoint_path: /root/autodl-tmp/simgate-modular-routing/results/seed123-plan-c/
      wall_clock_seconds: 11180.9
      gpu_hours: 12.42
    reproduce:
      finished_at: '2026-05-18T11:10:45.100Z'
    extra:
      hook_events:
      - event: on_complete
        action: agent
        ts: '2026-05-18T11:10:49.420475+00:00'
    conclusion: success
    metrics:
      DAF_seed123: 0.8968
      DAF_seed42: 0.9041
      DAF_diff_pp: -0.73
      death_rate_int_seed123: 0.4545
      death_rate_det_seed123: 0.2091
      delta_full_seed123: 27.47
      delta_nd_seed123: 2.83
      pearson_r_seed123: 0.9412
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68163f9e-c4d3-4b2f-9a6d-a3ff39c1923a",
  "isSidechain": true,
  "promptId": "5c9e987c-ae70-4ee6-a464-2d2db13505c8",
  "agentId": "abba625f7ac93e545",
  "type": "user",
  "uuid": "e618273c-9d81-49ee-9fc9-470f9d8c1950",
  "sourceToolAssistantUUID": "68163f9e-c4d3-4b2f-9a6d-a3ff39c1923a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-23T10:43:28.996Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JbgNSkqL6jgPnj9XFwpheY`</summary>

```json
{
  "command": "grep -B 5 -A 15 \"Gemma\\|gemma\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/registry.yaml | head -80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e618273c-9d81-49ee-9fc9-470f9d8c1950",
  "isSidechain": true,
  "agentId": "abba625f7ac93e545",
  "requestId": "req_011CbKMz24izoZ6DsJ2vNiPw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "93f3aa22-4d49-4a7f-8dc4-a764dcd35fc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Kziyj3A32deQsz7p6LPojB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1293,
      "cache_read_input_tokens": 64520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1293,
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

_source line 27 · 2026-05-23T10:43:29.072Z_

<details><summary>↩ Tool result · `toolu_01JbgNSkqL6jgPnj9XFwpheY`</summary>

```text
      data_path: /root/autodl-tmp/alfworld_data/json_2.1.1/valid_seen/
      data_count: 135
      model_name: Meta-Llama-3.1-8B-Instruct
      seed: 42
    metrics:
      status_detail: CRASHED - vLLM EngineCore died when gemma-gpu0 took GPU 0 at
        14:30
      episodes_completed: 1
  gemma-scienceworld-cross-model:
    status: ANALYZING
    retry_count: 0
    created_at: '2026-05-20T05:58:29.798Z'
    updated_at: '2026-05-20T06:31:51.438Z'
    hypothesis: Gemma-2-9B-it on ScienceWorld will show death dominance (DAF > 80%)
      consistent with Qwen2.5-7B (90.4%) and Llama-3.1-8B (88.2%), extending the cross-model-family
      evidence from 2 to 3 independent model families and strengthening the claim
      that death avoidance dominates routing signal regardless of model architecture.
    spec:
      command: bash scripts/run_gemma_gpu0.sh (cuda:0, 6 tasks) + bash scripts/run_gemma_gpu1.sh
        (cuda:1, 5 tasks)
      server: westb-13313
      gpu:
      - cuda:0
      - cuda:1
      data_path: 11 ScienceWorld tasks (10 death-prone + find-non-living-thing)
      data_count: 440
      model_name: gemma-2-9b-it
      seed: 42
      model_path: /root/autodl-tmp/models/gemma-2-9b-it/AI-ModelScope/gemma-2-9b-it
      temperature: 0.3
      max_steps: 30
      episodes_per_task: 20
      strategies: internal,deterministic
      tmux_sessions:
      - gemma-gpu0
      - gemma-gpu1
      checkpoint_source: AI-ModelScope/gemma-2-9b-it (ModelScope)
      eval_data: 11 ScienceWorld tasks × 20 episodes × 2 conditions (always-internal
        + always-deterministic)
  alfworld-llama-counterfactual:
    status: DONE
    retry_count: 0
    created_at: '2026-05-20T07:02:14.431Z'
    updated_at: '2026-05-20T09:22:49.600Z'
    spec:
      command: python src/alfworld_counterfactual.py --model_path /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct
        --output results/alfworld_llama_counterfactual/episodes.jsonl --n_tasks 0
        --gpu_id 0 --seed 42
      server: westb-13313
      data_path: ALFWorld json_2.1.1/valid_seen
      data_count: 0
      model_name: Meta-Llama-3.1-8B-Instruct
--
      episodes_total: 135
      server: westb-13313
      gpu: cuda:0
      note: Registry incorrectly marked DONE/failed at 09:19 UTC but process is alive
        (PID on GPU 0, tmux alfworld_v3). 85/135 eps at 09:20 check.
  gemma-scienceworld-counterfactual:
    status: DONE
    retry_count: 0
    created_at: '2026-05-20T07:02:15.806Z'
    updated_at: '2026-05-20T09:22:51.652Z'
    spec:
      command: bash scripts/run_gemma_all_gpu1.sh (11 tasks × 20 episodes serial)
      server: westb-13313
      data_path: 'ScienceWorld (11 included tasks: identify-life-stages-1,freeze,grow-fruit,identify-life-stages-2,measure-melting-point-unknown-substance,lifespan-longest-lived,lifespan-longest-lived-then-shortest-lived,chemistry-mix,inclined-plane-determine-angle,find-animal,find-non-living-thing)'
      data_count: 0
      model_name: gemma-2-9b-it
      seed: 42
      vllm_config: gpu_memory_utilization=0.85, enforce_eager=True, enable_prefix_caching=False,
        max_model_len=4096
      fixes_applied: sanitize_messages_for_template (system role), enable_prefix_caching=False
        (prevent vLLM EngineCore crash), enforce_eager=True (disable CUDA graphs)
    failure_reason: 'startup recovery: RUNNING with no cron and no server/pid info'
    conclusion: failed
    completed_at: '2026-05-20T09:19:17.090Z'
    metrics:
      status_override: ACTUALLY_STILL_RUNNING
      progress:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93f3aa22-4d49-4a7f-8dc4-a764dcd35fc7",
  "isSidechain": true,
  "promptId": "5c9e987c-ae70-4ee6-a464-2d2db13505c8",
  "agentId": "abba625f7ac93e545",
  "type": "user",
  "uuid": "d2332e49-c2e7-4220-92bf-817fe30b37f4",
  "sourceToolAssistantUUID": "93f3aa22-4d49-4a7f-8dc4-a764dcd35fc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-23T10:43:30.345Z_

Now let me look at what the actual Gemma result is and check if there's any confusion with DAF values:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2332e49-c2e7-4220-92bf-817fe30b37f4",
  "isSidechain": true,
  "agentId": "abba625f7ac93e545",
  "requestId": "req_011CbKMzE4Y7eQEkonHEubB6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fa04dba5-abe0-4bd0-b69c-9b27b426c2b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EJgkmaAQWctryCRUFmCmrG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2158,
      "cache_read_input_tokens": 65813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2158,
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

_source line 29 · 2026-05-23T10:43:31.329Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Faat8RCjtxv7jkvpsx1QCE`</summary>

```json
{
  "command": "grep -B 5 -A 30 \"gemma-scienceworld-counterfactual:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/registry.yaml | tail -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa04dba5-abe0-4bd0-b69c-9b27b426c2b6",
  "isSidechain": true,
  "agentId": "abba625f7ac93e545",
  "requestId": "req_011CbKMzE4Y7eQEkonHEubB6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1e3d612c-46f4-4a6f-bb67-6d319ead72c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EJgkmaAQWctryCRUFmCmrG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2158,
      "cache_read_input_tokens": 65813,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2158
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 138,
          "cache_read_input_tokens": 65813,
          "cache_creation_input_tokens": 2158,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2158,
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

_source line 30 · 2026-05-23T10:43:31.396Z_

<details><summary>↩ Tool result · `toolu_01Faat8RCjtxv7jkvpsx1QCE`</summary>

```text
      episodes_total: 135
      server: westb-13313
      gpu: cuda:0
      note: Registry incorrectly marked DONE/failed at 09:19 UTC but process is alive
        (PID on GPU 0, tmux alfworld_v3). 85/135 eps at 09:20 check.
  gemma-scienceworld-counterfactual:
    status: DONE
    retry_count: 0
    created_at: '2026-05-20T07:02:15.806Z'
    updated_at: '2026-05-20T09:22:51.652Z'
    spec:
      command: bash scripts/run_gemma_all_gpu1.sh (11 tasks × 20 episodes serial)
      server: westb-13313
      data_path: 'ScienceWorld (11 included tasks: identify-life-stages-1,freeze,grow-fruit,identify-life-stages-2,measure-melting-point-unknown-substance,lifespan-longest-lived,lifespan-longest-lived-then-shortest-lived,chemistry-mix,inclined-plane-determine-angle,find-animal,find-non-living-thing)'
      data_count: 0
      model_name: gemma-2-9b-it
      seed: 42
      vllm_config: gpu_memory_utilization=0.85, enforce_eager=True, enable_prefix_caching=False,
        max_model_len=4096
      fixes_applied: sanitize_messages_for_template (system role), enable_prefix_caching=False
        (prevent vLLM EngineCore crash), enforce_eager=True (disable CUDA graphs)
    failure_reason: 'startup recovery: RUNNING with no cron and no server/pid info'
    conclusion: failed
    completed_at: '2026-05-20T09:19:17.090Z'
    metrics:
      status_override: ACTUALLY_STILL_RUNNING
      progress:
        boil: 20/20
        melt: 2/20 (from prior session)
        identify-life-stages-1: 8/20 (currently running)
        remaining_8_tasks: not started
      episodes_completed: 30
      episodes_total: 220
      server: westb-13313
      gpu: cuda:1
      note: Registry incorrectly marked DONE/failed at 09:19 UTC but process is alive
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e3d612c-46f4-4a6f-bb67-6d319ead72c9",
  "isSidechain": true,
  "promptId": "5c9e987c-ae70-4ee6-a464-2d2db13505c8",
  "agentId": "abba625f7ac93e545",
  "type": "user",
  "uuid": "3348afac-d193-481a-ad61-5c098c9f4335",
  "sourceToolAssistantUUID": "1e3d612c-46f4-4a6f-bb67-6d319ead72c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-23T10:43:34.686Z_

Let me search for where the Gemma results were actually analyzed:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3348afac-d193-481a-ad61-5c098c9f4335",
  "isSidechain": true,
  "agentId": "abba625f7ac93e545",
  "requestId": "req_011CbKMzQ53y6fqmAuLc4trM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "297c132c-ae86-4bda-afeb-2f1b25cd60e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UkC6jW8Uvu9Me9xrWjukqR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 751,
      "cache_read_input_tokens": 67971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 751,
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

_source line 32 · 2026-05-23T10:43:34.838Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CCU2LN598jkcNfD9UaerDy`</summary>

```json
{
  "command": "grep -n \"Gemma\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "297c132c-ae86-4bda-afeb-2f1b25cd60e7",
  "isSidechain": true,
  "agentId": "abba625f7ac93e545",
  "requestId": "req_011CbKMzQ53y6fqmAuLc4trM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "69e3644b-0fd5-44cb-9024-9ff1c57d840b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UkC6jW8Uvu9Me9xrWjukqR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 751,
      "cache_read_input_tokens": 67971,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 751
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 115,
          "cache_read_input_tokens": 67971,
          "cache_creation_input_tokens": 751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 751,
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

_source line 33 · 2026-05-23T10:43:34.898Z_

<details><summary>↩ Tool result · `toolu_01CCU2LN598jkcNfD9UaerDy`</summary>

```text
56:This work uses ScienceWorld \citep{scienceworld-2022}, a publicly available text-based simulation environment, and does not involve human subjects or private data. All evaluation environments (ScienceWorld, ALFWorld, MATH) are released under permissive open-source licenses (Apache 2.0 / MIT). All models used (Qwen2.5 family, Llama-3.1-8B, Gemma-2-9B-it) are publicly available for research use. All language models are accessed via standard APIs or publicly released weights. Experiments were conducted on 2$\times$ NVIDIA RTX 5090 (32GB) and 4$\times$ NVIDIA RTX 6000 PRO (96GB), totaling approximately 200 GPU-hours, comprising ${\sim}$140 hours for episode collection (counterfactual inference across three 7--9B model families plus Qwen2.5-72B backbone scaling, Reflexion and retry baselines, and cross-environment validation on ALFWorld and MATH), ${\sim}$35 hours for router training (LoRA fine-tuning of Qwen3-0.6B/1.7B/4B across 4--8 seeds per scale, including augmentation and ablation variants), and ${\sim}$25 hours for evaluation and analysis. Code and data will be released upon acceptance.
613:Gemma-2-9B-it & ScienceWorld & 220 & 36.4\% & 14.1\% & +22.3 & 89.7\% & [79.5, 98.4] & death \\
622:\caption{Cross-model and cross-environment replication summary. \textbf{ScienceWorld}: death dominance replicates across three model families in the 7--9B range and persists under $10{\times}$ scaling (72B); DAF 95\% CIs from non-clustered episode-level bootstrap ($B{=}10{,}000$). \textbf{ALFWorld}: DAF $= 0\%$ (no death mechanism); routing signal arises from information asymmetry. \textbf{MATH}: no routing signal without catastrophic failure. Signal column: diagnosed routing mechanism. DR = death rate. Gemma-2's wider CI reflects one zero-death task type (\texttt{find-non-living-thing}); excluding it yields DAF $= 99.9\%$ $[99.7, 100.0]$.}
903:We illustrate the framework's ability to decompose non-death routing signal using \texttt{find-non-living-thing}, the only task type with zero deaths and 100\% non-death labels (\S\ref{sec:death-decomp}). Using Gemma-2-9B-it counterfactual episodes ($N{=}20$), 12 episodes show routing preference (9 deterministic-preferred, 3 internal-preferred), confirming the framework detects bidirectional signal independent of death asymmetry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69e3644b-0fd5-44cb-9024-9ff1c57d840b",
  "isSidechain": true,
  "promptId": "5c9e987c-ae70-4ee6-a464-2d2db13505c8",
  "agentId": "abba625f7ac93e545",
  "type": "user",
  "uuid": "77d830ce-7615-41f1-91c8-07b19a11ae71",
  "sourceToolAssistantUUID": "69e3644b-0fd5-44cb-9024-9ff1c57d840b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-23T10:43:45.495Z_

Perfect! Now I have the complete picture. Let me create a comprehensive summary of my findings.

## Report: Qwen Seed Replication and Gemma DAF=89.7% Confusion

Based on my investigation of the registry and paper, I have identified a **critical data labeling issue** in §3.1 claim.

### Findings:

**1. What the seed-robustness appendix actually discusses (Appendix J):**
- **NOT** a Qwen seed replication with N=220
- **INSTEAD:** A validation of router generalization across 8 random seeds {42-49} using the QWEN2.5-7B model
- Tests step-level vs episode-level evaluation of the router itself (not the counterfactual)
- Results: Step-level balanced accuracy 54.1±5.4%, Episode-level 47.1±2.2% (below chance)
- Includes text augmentation ablation across 25%-800% training scale
- This is about **router training seed robustness**, not counterfactual collection replication

**2. The misattributed DAF=89.7% with N=220:**
This is **the Gemma-2-9B-it cross-model result**, not a Qwen seed replication:
- Found in Table 14 (Cross-Model Verification table, line 613)
- Gemma-2-9B-it: ScienceWorld, N=220 episodes, DAF = 89.7%, CI [79.5, 98.4]
- Internal death rate: 36.4%, Deterministic: 14.1%, Δ = +22.3pp
- This is model-family replication evidence (third model family after Qwen and Llama)

**3. What actually happened with Qwen seed robustness (REAL Qwen replication):**
Found in registry as `seed-123-replication`:
- **Hypothesis:** Seed robustness validation (seed=123 vs seed=42 for plan-012-full)
- **Status:** DONE (success)
- **Results:**
  - DAF_seed123: 89.68%
  - DAF_seed42: 90.41%
  - DAF difference: -0.73pp (highly consistent)
  - Death rate (seed 123): 45.45% internal, 20.91% deterministic (Δ = +24.54pp)
  - Pearson r (seed 123): 0.9412
- This is the **actual Qwen seed replication** with independent seed collection

### Conclusion:

**The paper has a mislabeling error in §3.1.** The claim "an independent seed replication (N=220) yields DAF = 89.7%" cites Appendix seed-robustness but:
- Appendix J (seed-robustness) does NOT contain any N=220 Qwen result with DAF=89.7%
- Appendix J is about router training seed robustness, not counterfactual replication
- The N=220, DAF=89.7% value is actually Gemma-2-9B-it (found in Table 13, Appendix M: Cross-Model Verification)
- The real Qwen seed replication (seed=123) exists in the registry but is NOT cited and shows DAF=89.68% (not 89.7%)

**The paper likely intended to reference either:**
1. The Qwen seed=123 result (which shows ~89.7% ≈ 89.68%), OR
2. The Gemma result explicitly (which is exactly 89.7%)

But the current cross-reference creates ambiguity and potential confusion between the router's seed robustness (Appendix J) and counterfactual collection replication (the actual seed=123 experiment in registry).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77d830ce-7615-41f1-91c8-07b19a11ae71",
  "isSidechain": true,
  "agentId": "abba625f7ac93e545",
  "requestId": "req_011CbKMzegNsG8LVJQS2Azwx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ade81f4d-55a2-4e0c-bd14-7a7ff4b4d294",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "a0ff0dcc-b9d5-437c-9893-6b9da3108657",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "linked-sauteeing-puzzle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RUqjsZMBiMvNLr6aw2LXAD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 843,
      "cache_read_input_tokens": 68722,
      "output_tokens": 912,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 843
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 912,
          "cache_read_input_tokens": 68722,
          "cache_creation_input_tokens": 843,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 843,
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
