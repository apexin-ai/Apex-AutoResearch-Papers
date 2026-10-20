# Research conversation: In the file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex, ca

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ad2899e5fc9701ddb.jsonl`
- **Structured JSON:** [`498d2958bca6a218fc9a.json`](../../sessions/49/498d2958bca6a218fc9a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

34 recorded events

### User

_source line 1 · 2026-05-25T09:05:58.796Z_

In the file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex, catalog every section, subsection, table, figure, algorithm, theorem/proposition/observation/lemma, and equation label. 

For each item, report:
- The type (section/subsection/table/figure/algorithm/theorem etc.)
- The label (e.g. \label{sec:something}, \label{tab:something})
- The title/caption (first ~50 chars)
- Approximate line number

Be exhaustive - don't miss any. Use "very thorough" search breadth. Read the entire file in chunks if needed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f9b7a34c-f506-492b-bf34-76d808a6acc5",
  "agentId": "ad2899e5fc9701ddb",
  "type": "user",
  "uuid": "e54f7630-96f8-4142-866e-b072db9c71a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-25T09:06:00.841Z_

I'll read the entire appendix.tex file and catalog all the structural elements exhaustively.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e54f7630-96f8-4142-866e-b072db9c71a2",
  "isSidechain": true,
  "agentId": "ad2899e5fc9701ddb",
  "requestId": "req_011CbP2Aoe6jcaKjpa8Svv8p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "88ecb383-8b8a-46b6-a02b-ada7aa0fdef2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018C4rW5AKHFP5ARFakpVqm4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37331,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37331,
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

_source line 3 · 2026-05-25T09:06:00.986Z_

<details open><summary>🔧 Tool call — Read · `toolu_012yxfAjvM3ypMiLL7VFVHiu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88ecb383-8b8a-46b6-a02b-ada7aa0fdef2",
  "isSidechain": true,
  "agentId": "ad2899e5fc9701ddb",
  "requestId": "req_011CbP2Aoe6jcaKjpa8Svv8p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "48fb5eea-40b4-474f-b6d6-2c6126caeb3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018C4rW5AKHFP5ARFakpVqm4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37331,
      "cache_read_input_tokens": 0,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 37331
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 110,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 37331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 37331,
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

_source line 4 · 2026-05-25T09:06:01.448Z_

<details><summary>↩ Tool result · reported error · `toolu_012yxfAjvM3ypMiLL7VFVHiu`</summary>

```text
File content (44950 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48fb5eea-40b4-474f-b6d6-2c6126caeb3e",
  "isSidechain": true,
  "promptId": "f9b7a34c-f506-492b-bf34-76d808a6acc5",
  "agentId": "ad2899e5fc9701ddb",
  "type": "user",
  "uuid": "45c5c266-480f-491b-89e4-92cf2e5516be",
  "toolUseResult": "Error: File content (44950 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "48fb5eea-40b4-474f-b6d6-2c6126caeb3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-25T09:06:02.745Z_

The file is quite large. Let me read it in chunks using offset and limit parameters.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45c5c266-480f-491b-89e4-92cf2e5516be",
  "isSidechain": true,
  "agentId": "ad2899e5fc9701ddb",
  "requestId": "req_011CbP2AzxEo1M6mQjFbHdgW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "badb67aa-00ea-44d3-9383-0fded059c850",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WQUprm1NDjo1AaRobNM7Xq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1005,
      "cache_read_input_tokens": 37331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1005,
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

_source line 6 · 2026-05-25T09:06:03.194Z_

<details open><summary>🔧 Tool call — Read · `toolu_013NW1XTabAmqhbHcNoFXsM3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "limit": 3000,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "badb67aa-00ea-44d3-9383-0fded059c850",
  "isSidechain": true,
  "agentId": "ad2899e5fc9701ddb",
  "requestId": "req_011CbP2AzxEo1M6mQjFbHdgW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "71c187cc-43ec-4172-b5d6-480c3d546f3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WQUprm1NDjo1AaRobNM7Xq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1005,
      "cache_read_input_tokens": 37331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1005,
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

_source line 7 · 2026-05-25T09:06:03.284Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019JDJdHEmLaFXHg8rnYiT8X`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71c187cc-43ec-4172-b5d6-480c3d546f3d",
  "isSidechain": true,
  "agentId": "ad2899e5fc9701ddb",
  "requestId": "req_011CbP2AzxEo1M6mQjFbHdgW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cdc23145-b5d8-488b-b86b-4b9e560355a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WQUprm1NDjo1AaRobNM7Xq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1005,
      "cache_read_input_tokens": 37331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1005,
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

_source line 8 · 2026-05-25T09:06:03.465Z_

<details><summary>↩ Tool result · `toolu_019JDJdHEmLaFXHg8rnYiT8X`</summary>

```text
1754 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cdc23145-b5d8-488b-b86b-4b9e560355a2",
  "isSidechain": true,
  "promptId": "f9b7a34c-f506-492b-bf34-76d808a6acc5",
  "agentId": "ad2899e5fc9701ddb",
  "type": "user",
  "uuid": "aee46a1b-eca7-4080-9884-a81e14154fc0",
  "sourceToolAssistantUUID": "cdc23145-b5d8-488b-b86b-4b9e560355a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-25T09:06:03.510Z_

<details><summary>↩ Tool result · reported error · `toolu_013NW1XTabAmqhbHcNoFXsM3`</summary>

```text
File content (44950 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71c187cc-43ec-4172-b5d6-480c3d546f3d",
  "isSidechain": true,
  "promptId": "f9b7a34c-f506-492b-bf34-76d808a6acc5",
  "agentId": "ad2899e5fc9701ddb",
  "type": "user",
  "uuid": "78c05e6a-528f-48a9-8918-549ccc9659b0",
  "toolUseResult": "Error: File content (44950 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "71c187cc-43ec-4172-b5d6-480c3d546f3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-25T09:06:04.818Z_

The file is 1754 lines. Let me use grep to extract all the structural elements systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78c05e6a-528f-48a9-8918-549ccc9659b0",
  "isSidechain": true,
  "agentId": "ad2899e5fc9701ddb",
  "requestId": "req_011CbP2B9grh4c8c1CMWtUJd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dfe99b9e-0871-4b33-86d0-471472fbaf4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019efcqbLNr78ncamj4381UP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 72,
      "cache_creation_input_tokens": 297,
      "cache_read_input_tokens": 38336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 297,
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

_source line 11 · 2026-05-25T09:06:05.987Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01LRxnCotc4NJ7mCxypSEu4B`</summary>

```json
{
  "pattern": "^\\\\(section|subsection|subsubsection|label|caption|includegraphics|begin\\{table\\}|begin\\{figure\\}|begin\\{algorithm\\}|begin\\{theorem\\}|begin\\{proposition\\}|begin\\{observation\\}|begin\\{lemma\\}|begin\\{equation\\})",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "output_mode": "content",
  "context": 3,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfe99b9e-0871-4b33-86d0-471472fbaf4f",
  "isSidechain": true,
  "agentId": "ad2899e5fc9701ddb",
  "requestId": "req_011CbP2B9grh4c8c1CMWtUJd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d51fc178-4f48-4a75-8f5b-6197696b3c16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019efcqbLNr78ncamj4381UP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 72,
      "cache_creation_input_tokens": 297,
      "cache_read_input_tokens": 38336,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 297
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 72,
          "output_tokens": 261,
          "cache_read_input_tokens": 38336,
          "cache_creation_input_tokens": 297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 297,
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

_source line 12 · 2026-05-25T09:06:06.013Z_

<details><summary>↩ Tool result · `toolu_01LRxnCotc4NJ7mCxypSEu4B`</summary>

```text
&lt;persisted-output>
Output too large (52.7KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse--claude-sessions-director-6dc4a1c8/36cb22b8-86b0-4028-b0c2-9fe60f48bf51/tool-results/toolu_01LRxnCotc4NJ7mCxypSEu4B.txt

Preview (first 2KB):
1-\appendix
2-
3:\section{Training Details and Metric Drift}
4:\label{app:training_details}
5:\label{app:drift}
6-
7-\paragraph{Hyperparameters.}
8-Each generation fine-tunes for 5{,}000 steps using AdamW (learning rate $5 \times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium).
--
15-All models use the same generation parameters (temperature~$1.0$, top-$k{=}50$, max length 512) to control for decoding-strategy confounds.
16-Batch sizes are adjusted for GPU memory constraints; learning rates follow the respective model families' recommended fine-tuning ranges.
17-
18:\begin{table}[t]
19-\centering
20-\small
21:\caption{Per-architecture training hyperparameters.}
22:\label{tab:arch_hyperparams}
23-\begin{tabular}{lcccl}
24-\toprule
25-Model & Batch & LR & Steps & Precision \\
--
53-Two patterns emerge: (1)~entropy and calibration (ECE) degrade monotonically with $\alpha$, while (2)~diversity metrics exhibit a non-monotonic relationship where the largest relative decline occurs at moderate contamination ($\alpha{=}0.25$) rather than full replacement ($\alpha{=}1.0$).
54-Figure~\ref{fig:metric_trajectory} (main text) visualizes representative per-generation trajectories, showing the distinct temporal profiles that underlie the Granger-precedence analysis in \S\ref{sec:method}.
55-
56:\begin{table}[t]
57-\centering
58-\small
59:[Omitted long matching line]
60:\label{tab:drift_summary}
61-\resizebox{\columnwidth}{!}{%
62-\begin{tabular}{lccccc}
63-\toprule
--
91-At $\alpha{=}0.25$, the real-data fraction prevents catastrophic collapse but allows a steady, monotonic diversity decline across all 10 generations, producing a larger cumulative loss.
92-
93-
94:\section{Distinct-3 Results}
95:\label{app:distinct3}
96-
97-Table~\ref{tab:distinct3_drift} reports distinct-3 drift across all contamination levels.
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d51fc178-4f48-4a75-8f5b-6197696b3c16",
  "isSidechain": true,
  "promptId": "f9b7a34c-f506-492b-bf34-76d808a6acc5",
  "agentId": "ad2899e5fc9701ddb",
  "type": "user",
  "uuid": "88d64e49-4deb-4912-a808-fd0d802e5b1c",
  "sourceToolAssistantUUID": "d51fc178-4f48-4a75-8f5b-6197696b3c16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-25T09:06:07.360Z_

Let me read the full output and also search more specifically for all labels to ensure I capture everything:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88d64e49-4deb-4912-a808-fd0d802e5b1c",
  "isSidechain": true,
  "agentId": "ad2899e5fc9701ddb",
  "requestId": "req_011CbP2BLbSK8pARW7HBQiKg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "65b21364-bae0-4078-91c6-69b1db42419f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W73GT9aM6K2osC7Es6rMiL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1108,
      "cache_read_input_tokens": 38633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1108,
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

_source line 14 · 2026-05-25T09:06:07.739Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Nvd97bny1kixT53w3c2umY`</summary>

```json
{
  "command": "grep -n \"\\\\\\\\label{\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65b21364-bae0-4078-91c6-69b1db42419f",
  "isSidechain": true,
  "agentId": "ad2899e5fc9701ddb",
  "requestId": "req_011CbP2BLbSK8pARW7HBQiKg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7356afa9-f3f8-43e1-951e-acc701a687be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W73GT9aM6K2osC7Es6rMiL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1108,
      "cache_read_input_tokens": 38633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1108,
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

_source line 15 · 2026-05-25T09:06:07.810Z_

<details><summary>↩ Tool result · `toolu_01Nvd97bny1kixT53w3c2umY`</summary>

```text
4:\label{app:training_details}
5:\label{app:drift}
22:\label{tab:arch_hyperparams}
60:\label{tab:drift_summary}
95:\label{app:distinct3}
104:\label{tab:distinct3_drift}
132:\label{app:window_sensitivity}
151:\label{fig:window_sensitivity}
158:\label{tab:window_sensitivity}
177:\label{app:robustness}
178:\label{app:spec_curve}
192:\label{tab:spec_curve}
225:\label{app:transfer_entropy}
226:\phantomsection\label{app:te_mi}
241:\phantomsection\label{app:change_point}
249:\label{app:csmp}
275:\label{tab:sequential_timing}
301:\label{app:background}
302:\label{sec:background}
311:    \label{eq:mixing}
356:\label{app:mmct}
364:\label{fig:consensus_heatmap}
387:\label{fig:mmct_k_operating}
391:\label{app:method_comparison}
400:\label{tab:method-comparison}
429:\label{app:extended_discussion}
460:\label{tab:failure_modes}
480:\label{app:scale_14b}
486:\label{tab:14b_phase}
530:\label{fig:14b_phase}
549:\label{app:dose_response}
558:\label{tab:dose_response_full}
600:\label{fig:per_method_phase}
610:\label{app:alpha060}
635:\label{app:ppl_threshold}
659:\label{app:power_analysis}
684:\label{tab:beta50}
700:\label{app:nonstationarity}
711:\label{fig:ar1_diagnostic}
718:\label{tab:nonstationarity_sim}
742:\label{tab:empirical_ar1}
776:\label{tab:diff_power_cost}
794:\label{app:shapley}
804:\label{fig:shapley_contribution}
817:\label{tab:shapley_6pair}
834:\label{app:weight_robustness}
843:\label{tab:weight_robustness}
871:\label{tab:shapley_per_pair}
896:\label{app:fpr_independence}
907:\label{fig:fpr_sensitivity}
914:\label{fig:null_fpr_diagnostic}
921:\label{tab:null_fpr_methods}
938:\label{app:per_seed_fpr}
946:\label{fig:bootstrap_fpr}
953:\label{tab:per_seed_fpr_8pair}
972:\label{tab:per_seed_fpr_6pair}
994:\label{app:sigmoid_shape}
1018:\label{tab:transition_width}
1041:\label{fig:differencing_dmax}
1045:\label{app:intervention_sensitivity}
1069:\label{fig:cusum_monitoring}
1074:\label{app:channel_effect_size}
1087:\label{tab:lag_structure}
1112:\label{tab:fisher_z}
1138:\label{fig:channel_effect}
1143:\label{app:mi_analysis}
1157:\label{tab:mi_blind}
1172:\label{app:partial_corr}
1180:\label{tab:partial_corr}
1201:\label{fig:partial_corr}
1208:\label{fig:partial_corr_agg}
1223:\label{app:moment_cascade}
1231:\label{tab:moment_cascade}
1258:\label{tab:onset_threshold_sensitivity}
1287:\label{app:discretized_entropy}
1298:\label{tab:discretized_entropy}
1320:\label{app:cascade_theory}
1324:\begin{assumption}[Mode Amplification]\label{ass:mode_amp}
1330:\begin{proposition}[Entropy is a first-order indicator]\label{prop:entropy_first}
1343:\begin{proposition}[Diversity is a threshold indicator]\label{prop:div_threshold}
1390:\label{tab:ece_drift}
1417:\label{tab:cascade_onset}
1431:\phantomsection\label{app:alpha_c_proof}
1467:\label{tab:margin_consumption}
1485:\label{app:power_sim}
1507:\label{tab:steepness_comparison}
1524:\label{fig:permg_power_curve}
1528:\label{app:t20_comparison}
1544:\label{tab:t25_full}
1568:\label{fig:regime_map_extended}
1571:\phantomsection\label{app:task_degradation}
1582:\label{tab:cross_t_full}
1618:\label{tab:detection_efficiency}
1645:\label{app:cross_arch_table}
1651:\label{tab:generalization}
1681:\label{app:cross_arch_fpr}
1720:\label{app:reproducibility}
1746:\label{app:ai-assistants}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7356afa9-f3f8-43e1-951e-acc701a687be",
  "isSidechain": true,
  "promptId": "f9b7a34c-f506-492b-bf34-76d808a6acc5",
  "agentId": "ad2899e5fc9701ddb",
  "type": "user",
  "uuid": "47b0eeff-0f4b-4a0d-be5d-3c6d870b9c09",
  "sourceToolAssistantUUID": "7356afa9-f3f8-43e1-951e-acc701a687be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-25T09:06:08.152Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EjbST6JZY2kKTa4TJ5Fnsj`</summary>

```json
{
  "command": "grep -n \"\\\\\\\\section\\|\\\\\\\\subsection\\|\\\\\\\\subsubsection\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47b0eeff-0f4b-4a0d-be5d-3c6d870b9c09",
  "isSidechain": true,
  "agentId": "ad2899e5fc9701ddb",
  "requestId": "req_011CbP2BLbSK8pARW7HBQiKg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bc053855-3528-4988-a23e-b641466d8b92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W73GT9aM6K2osC7Es6rMiL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1108,
      "cache_read_input_tokens": 38633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1108,
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

_source line 17 · 2026-05-25T09:06:08.214Z_

<details><summary>↩ Tool result · `toolu_01EjbST6JZY2kKTa4TJ5Fnsj`</summary>

```text
3:\section{Training Details and Metric Drift}
94:\section{Distinct-3 Results}
131:\section{Observation Window Sensitivity}
176:\section{Robustness Analysis}
224:\section{Transfer Entropy and Change-Point Analysis}
248:\section{Sequential Monitoring: CUSUM vs Calibrated Threshold}
300:\section{Background and Notation}
355:\section{MMCT Algorithm}
390:\section{Methodological Comparison Table}
428:\section{Extended Discussion}
548:\section{Per-Method Dose-Response Profiles}
609:\section{Cross-Seed Consistency at $\alpha{=}0.60$}
634:\section{PPL Threshold Baseline}
658:\section{PermG Power Analysis}
699:\section{Non-Stationarity Robustness Analysis}
793:\section{Shapley Value Analysis}
833:\section{MMCT Weight Robustness Ablation}
895:\section{PermG FPR Independence Analysis}
937:\subsection{Per-Seed FPR Breakdown}
993:\section{Sigmoid Transition Shape}
1044:\section{Intervention Threshold Sensitivity}
1073:\section{Channel Effect Size Analysis}
1142:\section{Mutual Information and Partial Correlation}
1171:\subsection{Partial Correlation Analysis}
1222:\section{Moment Cascade Analysis}
1286:\subsection{Discretized Entropy Robustness Test}
1319:\section{Cascade Ordering Theory: Derivations}
1484:\section{Power Simulation: Shape Comparison}
1527:\section{T=20 Extension Results}
1644:\subsection{Cross-Architecture Detection Table}
1680:\subsection{Cross-Architecture FPR Sensitivity}
1719:\section*{Reproducibility Details}
1745:\section*{Use of AI Assistants}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc053855-3528-4988-a23e-b641466d8b92",
  "isSidechain": true,
  "promptId": "f9b7a34c-f506-492b-bf34-76d808a6acc5",
  "agentId": "ad2899e5fc9701ddb",
  "type": "user",
  "uuid": "e48b2091-a29c-4145-905a-b210a8ca7702",
  "sourceToolAssistantUUID": "bc053855-3528-4988-a23e-b641466d8b92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-25T09:06:08.521Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AQW5tLN8UJfe7tAfbe9s5P`</summary>

```json
{
  "command": "grep -n \"\\\\\\\\begin{table}\\|\\\\\\\\begin{figure}\\|\\\\\\\\begin{algorithm}\\|\\\\\\\\begin{theorem}\\|\\\\\\\\begin{proposition}\\|\\\\\\\\begin{observation}\\|\\\\\\\\begin{lemma}\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e48b2091-a29c-4145-905a-b210a8ca7702",
  "isSidechain": true,
  "agentId": "ad2899e5fc9701ddb",
  "requestId": "req_011CbP2BLbSK8pARW7HBQiKg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "aa983997-e2e4-4856-a118-6c2ed648c0ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W73GT9aM6K2osC7Es6rMiL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1108,
      "cache_read_input_tokens": 38633,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1108
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 338,
          "cache_read_input_tokens": 38633,
          "cache_creation_input_tokens": 1108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1108,
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

_source line 19 · 2026-05-25T09:06:08.577Z_

<details><summary>↩ Tool result · `toolu_01AQW5tLN8UJfe7tAfbe9s5P`</summary>

```text
18:\begin{table}[t]
56:\begin{table}[t]
100:\begin{table}[t]
147:\begin{figure}[t]
154:\begin{table}[t]
188:\begin{table}[t]
271:\begin{table}[t]
360:\begin{figure}[t]
383:\begin{figure}[t]
396:\begin{table}[t]
456:\begin{table}[t]
482:\begin{table}[t]
526:\begin{figure}[t]
554:\begin{table}[t]
596:\begin{figure}[t]
603:\begin{figure}[t]\ContinuedFloat
680:\begin{table}[t]
707:\begin{figure}[t]
714:\begin{table}[t]
738:\begin{table}[t]
772:\begin{table}[t]
800:\begin{figure}[t]
807:\begin{figure}[t]\ContinuedFloat
813:\begin{table}[t]
839:\begin{table}[t]
867:\begin{table}[t]
903:\begin{figure}[t]
910:\begin{figure}[t]
917:\begin{table}[t]
942:\begin{figure}[t]
949:\begin{table}[t]
968:\begin{table}[t]
1014:\begin{table}[t]
1037:\begin{figure}[t]
1065:\begin{figure}[t]
1083:\begin{table}[t]
1108:\begin{table}[t]
1134:\begin{figure}[t]
1153:\begin{table}[t]
1176:\begin{table}[t]
1197:\begin{figure}[t]
1204:\begin{figure}[t]
1227:\begin{table}[t]
1254:\begin{table}[t]
1294:\begin{table}[t]
1330:\begin{proposition}[Entropy is a first-order indicator]\label{prop:entropy_first}
1343:\begin{proposition}[Diversity is a threshold indicator]\label{prop:div_threshold}
1386:\begin{table}[t]
1413:\begin{table}[t]
1463:\begin{table}[t]
1503:\begin{table}[t]
1520:\begin{figure}[t]
1540:\begin{table}[t]
1564:\begin{figure}[t]
1578:\begin{table}[t]
1614:\begin{table}[t]
1647:\begin{table}[t]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa983997-e2e4-4856-a118-6c2ed648c0ce",
  "isSidechain": true,
  "promptId": "f9b7a34c-f506-492b-bf34-76d808a6acc5",
  "agentId": "ad2899e5fc9701ddb",
  "type": "user",
  "uuid": "4f85fb61-c7db-4834-ba6b-c2743e4b53b9",
  "sourceToolAssistantUUID": "aa983997-e2e4-4856-a118-6c2ed648c0ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-25T09:06:10.303Z_

Now let me search for captions and titles to get the full context for each element:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f85fb61-c7db-4834-ba6b-c2743e4b53b9",
  "isSidechain": true,
  "agentId": "ad2899e5fc9701ddb",
  "requestId": "req_011CbP2BXXkqdWpV8bMTHn3h",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1a743a83-3f4a-4403-959c-9f06cf573bde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XY2pX2LXMv72NGiyCzhJvd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2754,
      "cache_read_input_tokens": 39741,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2754,
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

_source line 21 · 2026-05-25T09:06:11.559Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PfL927tSfgjbKJkVU57WGj`</summary>

```json
{
  "command": "grep -n \"\\\\\\\\caption{\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a743a83-3f4a-4403-959c-9f06cf573bde",
  "isSidechain": true,
  "agentId": "ad2899e5fc9701ddb",
  "requestId": "req_011CbP2BXXkqdWpV8bMTHn3h",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "14d1afce-e09e-43f4-82a3-cdd622a666fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XY2pX2LXMv72NGiyCzhJvd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2754,
      "cache_read_input_tokens": 39741,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2754,
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

_source line 22 · 2026-05-25T09:06:11.622Z_

<details><summary>↩ Tool result · `toolu_01PfL927tSfgjbKJkVU57WGj`</summary>

```text
21:\caption{Per-architecture training hyperparameters.}
59:\caption{Metric drift (\%, generation~0$\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\alpha{=}0.25$: distinct-1 $-40.3{\pm}0.3\%$) rather than full replacement ($\alpha{=}1.0$: $-27.8{\pm}1.6\%$). $^\dagger$$\alpha{=}0.10$: single seed (seed~42, preliminary). $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3-seed mean${\pm}$std (seeds 42, 43, 44); $\alpha{=}1.0$: 4-seed mean${\pm}$std (seeds 42, 43, 44, 45).}
103:\caption{Distinct-3 drift (\%, generation~0$\to$10) across contamination levels. $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.75$: 3-seed mean${\pm}$std; $\alpha{=}1.0$: 4-seed mean${\pm}$std; $\alpha{=}0.50$: single seed.}
150:\caption{Detection stability as a function of minimum observation window $T_{\min}$ (Pythia-410M, $\alpha{=}1.0$, 4~seeds). PermG forward detection (6/8) and consensus classification ($K{\geq}4$) both stabilize at $T_{\min}{\geq}5$, with no significance flips for $T_{\min} \in [5, 10]$. This robustness confirms that the choice of $T_{\min}{=}5$ in the main analysis does not drive results.}
157:\caption{Observation window sensitivity for Tier~3 consensus ($K{\geq}4/5$) at $\alpha{=}1.0$ (Pythia-410M, 4~seeds). Tier~3 pairs: number of canary$\to$downstream pairs (out of 8 validated) reaching $K{\geq}4/5$ method agreement. TY pairs: number of effect-size reference pairs (out of 6) reaching Toda--Yamamoto significance (moderate supplementary method; \S\ref{sec:method}). Consensus stabilizes at $T_{\min}{\geq}5$; TY stabilizes at $T_{\min}{\geq}6$.}
191:\caption{Specification curve summary (1{,}160 specifications, D120-compliant). The blind$\to$onset jump is robust across specifications: 0\% significance rate through $\alpha{=}0.45$, rising to 75\% at $\alpha{=}0.50$.}
274:\caption{Sequential monitoring alarm timing (Pythia-410M, seed~42, fp32). ``---'' = no alarm within $T{=}10$. Both methods produce identical alarm patterns: no detection below $\alpha{=}0.50$, immediate (gen-1) detection above.}
363:\caption{$K{\geq}3$ consensus heatmap across the $\alpha \times T$ grid (Pythia-410M, fp32). Each cell shows the number of canary$\to$diversity pairs reaching majority agreement (${\geq}3/5$ methods). Consensus detection aligns with PermG's onset at $\alpha{=}0.50$ but eliminates the non-monotonic anomaly at $\alpha{=}0.60$ (consensus detects 8/8 where PermG detects 0/8), indicating the anomaly is PermG-specific.}
386:\caption{MMCT operating characteristics as a function of consensus threshold $K$. Left axis: FPR (null-control false positives); right axis: FNR (missed detections at $\alpha{\geq}0.50$). $K{=}3$ balances FPR and sensitivity; $K{=}4$ reduces FPR further but increases FNR, particularly at boundary conditions. $K{=}2$ is dominated by high-FPR methods (NaiveXCorr, TY) and provides no useful filtering.}
399:\caption{Methodological comparison of canary and monitoring analyses. \checkmark\ = present, $\times$ = absent, $\circ$ = partial (${\leq}2$ levels or limited replication). Diff.\ = differencing/stationarity controls. Multi-M.\ = ${\geq}2$ independent statistical methods. MTC = multiple testing correction. Regime = systematic variation of $\alpha$. Seeds = ${\geq}3$ independent seeds. Arch.\ = ${\geq}2$ architecturally distinct model families.}
459:\caption{Failure mode taxonomy for non-confirming cross-architecture conditions ($\alpha{=}1.0$).}
485:\caption{Pythia-1.4B phase diagram replication: PermG forward/reverse detection and $K{\geq}3$ consensus across contamination levels and observation windows (fp32). $\dagger$: bidirectional confounding (reverse${}>0$). Denominator is 8 unless marked $^{*}$ (6-pair basis, MAUVE unavailable).}
529:\caption{Pythia-1.4B phase diagram (PermG forward, 6-pair basis). Detection boundary ($\alpha_c \approx 0.50$) is consistent with 410M.}
557:\caption{Per-method FDR significance (/8 pairs) across contamination levels (Pythia-410M, seed~42, WikiText, fp32). PermG and Diff.\ XCorr use BH-corrected FDR ($q{=}0.05$); Naive XCorr, Threshold, and TY use uncorrected $p{<}0.05$ (no FDR field in pipeline). $\alpha{=}1.0$ from Pythia-410M cross-architecture condition (same seed/domain/precision).}
599:\caption{Per-method FDR-significant pair counts (/8) across contamination levels (Pythia-410M, seed~42, $T{=}10$, fp32). PermG~(d) exhibits the cleanest regime separation---zero detections through $\alpha{=}0.45$, then a sharp 0$\to$6 jump at $\alpha{=}0.50$; NaiveXCorr~(a) saturates at 7--8/8 across all levels including null; DiffXCorr~(b) detects signal but cannot separate forward from reverse. The visual contrast across panels illustrates why method choice is itself a primary source of variability ($\kappa{=}0.185$).}
683:\caption{PermG power analysis: $\beta_{50}$ (coupling for 50\% power) under BH-FDR correction ($q{=}0.05$, 8 pairs). Dashes: $<$50\% power not reached within $\beta \leq 2.0$.}
710:\caption{AR(1) coefficient estimates across five contamination levels (Pythia-410M, seed~42). (a)~Token entropy: raw $\varphi$ transitions from negative ($-0.51$ at $\alpha{=}0.00$) to near-unit-root ($1.00$ at $\alpha{=}1.00$), but first-differencing keeps all values below 0.98. (b)~Distinct-1: raw $\varphi$ is uniformly high ($0.75$--$0.95$) even at null, driven by deterministic trend; first-differencing reduces all to ${\leq}0.24$. Dashed red line: $\varphi{=}0.95$ danger zone.}
717:\caption{Size and power under AR(1) DGP ($T{=}11$, 1{,}000 reps). First-differencing maintains nominal size; PermG FPR inflates at $\varphi{\geq}0.95$.}
741:\caption{Empirical AR(1) coefficients (Pythia-410M, 4~seeds). ``Raw'' = levels; ``Diff'' = first-differenced.}
775:\caption{Power cost of first-differencing under simulated AR(1) DGP ($T{=}11$, $\beta{=}0.6$, 1{,}000 reps). The power reduction is the price paid for valid size control.}
803:\caption{Shapley value decomposition by method. FPR contribution (positive = worse) and FNR contribution (negative = better) are shown for each of the five detection methods. DiffXCorr achieves the best combined Shapley ($-0.299$) but lacks directional separation; among directional methods, PermG ranks best ($-0.141$). NaiveXCorr contributes the most FPR ($+0.609$) due to its inability to distinguish signal from null drift.}
816:\caption{Shapley value decomposition (6-pair, MAUVE excluded). Combined = FPR + FNR (more negative = better).}
842:\caption{PermG combined Shapley ($\phi^{\text{comb}}$) under four weighting schemes. Rankings are invariant to weight choice.}
870:\caption{Shapley contribution by canary$\to$downstream pair (PermG, 6-pair basis). $\phi^{\text{FNR}}$ = FNR reduction (more negative = better). Std = standard deviation across all $2^4$ coalitions that include this pair.}
906:\caption{Per-seed FPR distribution across detection methods (Pythia-410M, $\alpha{=}0.0$, 10~seeds). Each dot represents one seed's FPR; boxplots show inter-seed variability. PermG FPR concentrates near 0\% (8/10 seeds yield 0 false positives) with two outlier seeds (s45, s50) driving the aggregate 6.7\%. NaiveXCorr exhibits uniformly high FPR (${\geq}83\%$) across all seeds.}
913:\caption{Null-control diagnostic: PermG $p$-value distributions under null ($\alpha{=}0.0$) across 10~seeds. Most seeds show $p$-values uniformly distributed above 0.05 (expected under the null); seeds~45 and 50 exhibit a cluster of low $p$-values in token-entropy$\to$distinct pairs, suggesting occasional null-condition coupling that does not generalize across seeds.}
920:\caption{Null-control FPR by method ($\alpha{=}0.0$, BH-FDR $q{=}0.05$). $^\ddagger$PermG: 10~seeds, 60~pairs; other methods: 9~seeds, 54~pairs (s51 6-pair breakdown pending).}
945:\caption{Bootstrap confidence intervals for FPR estimates (10{,}000 resamples, 10~seeds). PermG's 95\% CI ($[1.8\%, 16.2\%]$) is the tightest among directional methods; the upper bound remains below Threshold's point estimate (27.8\%). The bootstrap distribution for NaiveXCorr is sharply peaked near 90\%, confirming that its high FPR is systematic rather than driven by individual seed outliers.}
952:\caption{Per-seed FPR (8-pair basis, $\alpha{=}0.0$, Pythia-410M, seeds 42--44). PermG achieves 0/8 on all three seeds; NaiveXCorr ${\geq}7/8$ on all.}
971:\caption{Per-seed PermG FPR (6-pair basis, $\alpha{=}0.0$, seeds 45--51). Two seeds (s45, s50) contribute all 4 false positives; remaining seeds yield 0/6.}
1017:\caption{Sigmoid transition width (90\% range) by observation length and signal model. Narrower width indicates sharper regime onset.}
1040:\caption{First-differencing order selection diagnostic. The optimal differencing order $d_{\max}$ is evaluated via ADF test statistics across all canary$\to$downstream series at $\alpha{=}1.0$. First-order differencing ($d{=}1$) achieves stationarity in all series (ADF $p{<}0.05$), confirming that higher-order differencing is unnecessary and would incur additional power loss.}
1068:\caption{CUSUM sequential monitoring versus calibrated threshold (Pythia-410M, $\alpha{=}1.0$). Both methods trigger at generation~1 because the entropy drop ($|\Delta x|{>}0.7$) greatly exceeds null variability ($\sigma_0{\approx}0.03$). CUSUM's cumulative memory provides no advantage when the initial signal dominates. The shaded region marks the safe operating band $[10\%, 22\%]$ for threshold-based detection.}
1086:\caption{Cross-correlation peak lag by channel (Pythia-410M, $\alpha{=}1.0$, 4~seeds). Negative lag = canary leads. Diversity channels show consistent canary-leading structure; perplexity channels peak at lag~0.}
1111:\caption{Fisher Z-transform comparison of channel correlations (Pythia-410M, $\alpha{=}1.0$, 4~seeds). $Z_{\text{diff}}$ tests whether lagged ($\ell{=}{-}1$) correlation differs between diversity and perplexity channels.}
1137:\caption{Channel effect size comparison: Granger $F$-statistic for canary$\to$diversity versus canary$\to$perplexity channels (Pythia-410M, $\alpha{=}1.0$, 4~seeds). Diversity channels produce $20$--$28{\times}$ higher $F$-statistics than perplexity channels, reflecting the temporal structure difference: diversity correlations peak at canary-leading lags (81\% at lag${<}0$), while perplexity correlations are contemporaneous (50\% at lag${=}0$).}
1156:\caption{Gaussian MI lower bound between token entropy and distinct-1 across the blind zone (Pythia-410M, $T{=}10$, seed~42).}
1179:\caption{Partial correlation controlling for generation. Lagged partial $|r|$ increases after trend removal, confirming genuine temporal precedence.}
1200:\caption{Partial correlation scatter plots for canary$\to$diversity pairs at $\alpha{=}0.75$ (Pythia-410M). Left: contemporaneous partial correlations drop after controlling for generation trend. Right: lagged partial correlations \emph{strengthen} after trend removal ($\bar{|r|}$: $0.831{\to}0.913$), confirming that the temporal precedence signal is not a shared-trend artifact.}
1207:\caption{Aggregated partial correlation analysis across contamination levels. Lagged canary$\to$diversity correlations increase monotonically with $\alpha$ (from $0.524$ at null to $0.913$ at $\alpha{=}0.75$), while contemporaneous correlations plateau. The growing gap between lagged and contemporaneous partial $|r|$ with increasing contamination indicates that the temporal lead signal strengthens with signal-to-noise ratio.}
1230:\caption{Degradation onset generation (5\% threshold) by metric and condition (Pythia-410M, WikiText, fp32). Token entropy reaches onset at generation~1 in all non-null conditions; distinct-$n$ metrics follow at generation~2.}
1257:\caption{Cascade ordering $t_H \leq t_D$ validity as a function of onset threshold (Pythia-410M, 6 conditions, $\alpha{\geq}0.10$).}
1297:\caption{Discretized entropy Granger test: number of experiments (out of 7) with FDR-significant entropy$\to$distinct-1 at each binning resolution and method. Continuous baseline: 7/7.}
1389:\caption{ECE drift across contamination levels (Pythia-410M, WikiText, fp32). ECE increases monotonically with $\alpha$, co-moving with entropy decrease.}
1416:\caption{Cascade onset generations (5\% threshold) for representative experiments (Pythia-410M, WikiText, fp32). Phase~1: entropy and ECE ($t_H$, $t_{\mathrm{ECE}}$); Phase~2: diversity ($t_D$, min over distinct-$n$); Phase~3: MAUVE ($t_M$). All conditions confirm the predicted ordering $t_H = t_{\mathrm{ECE}} \leq t_D \leq t_M$.}
1466:\caption{Margin consumption across contamination levels (Pythia-410M, seed~42). ``Margin gen'' = first generation where cumulative $\|\delta\|_\infty > \gamma$. The diversity lag $t_D - t_H{=}1$ is invariant despite variable margin consumption timing.}
1506:\caption{Onset steepness $k$ under different signal models (1{,}000 reps, PermG, BH-FDR $q{=}0.05$).}
1523:\caption{PermG power curves as a function of coupling strength $\beta$ for $T \in \{6, 8, 10, 15, 20\}$ (100 replications, 5{,}000 permutations, BH-FDR $q{=}0.05$). Power increases faster than $\sqrt{T}$, confirming that the theoretical $\sqrt{T}$ formula is a conservative lower bound. At $T{=}10$, 50\% power requires $\beta{\geq}2.0$; at $T{=}20$, this drops to $\beta{\approx}0.9$.}
1543:\caption{PermG forward detection at $T{=}25$ (Pythia-410M, fp32). The $\alpha{=}0.45$ blind zone resolves and the $\alpha{=}0.60$ anomaly dissolves.}
1567:\caption{Extended regime map including $T \in \{5, 10, 15, 20, 25\}$. The detection boundary shifts leftward with increasing $T$: $\alpha{=}0.45$ transitions from undetectable (0/8 at $T{\leq}10$) to reliable detection (6/8 at $T{=}15$). The $\alpha{=}0.60$ non-monotonic anomaly persists through $T{=}20$ but dissolves at $T{=}25$ (5/8).}
1581:\caption{PermG forward detection (/8 pairs) across $T$ and $\alpha$ (Pythia-410M, seed~42, fp32). Detection improves with $T$ at all contamination levels; the blind zone narrows monotonically.}
1617:\caption{Detection efficiency (fraction of pairs reaching FDR significance) across the $\alpha \times T$ grid (Pythia-410M, seed~42, fp32). Efficiency plateaus at 0.75 for above-onset conditions, indicating a structural detection ceiling at 6/8 pairs.}
1650:\caption{Cross-architecture PermG forward detection ($\alpha{=}1.0$, 15 model-seed combinations across five families---Pythia, GPT-2, OPT, Qwen, SmolLM3---and two domains; Padding-410M is a Pythia variant). PermG fwd $=$ count of FDR-significant forward pairs out of 8.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14d1afce-e09e-43f4-82a3-cdd622a666fd",
  "isSidechain": true,
  "promptId": "f9b7a34c-f506-492b-bf34-76d808a6acc5",
  "agentId": "ad2899e5fc9701ddb",
  "type": "user",
  "uuid": "be9a8614-3f92-4c75-9115-a9e454b65a0a",
  "sourceToolAssistantUUID": "14d1afce-e09e-43f4-82a3-cdd622a666fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-25T09:06:12.213Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CR3FMzLeBSo38K2nu3FD61`</summary>

```json
{
  "command": "grep -n \"\\\\\\\\begin{equation}\\|\\\\\\\\begin\\{align\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be9a8614-3f92-4c75-9115-a9e454b65a0a",
  "isSidechain": true,
  "agentId": "ad2899e5fc9701ddb",
  "requestId": "req_011CbP2BXXkqdWpV8bMTHn3h",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f11c515d-cc09-4dd7-87c7-2bc9972bb0c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XY2pX2LXMv72NGiyCzhJvd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2754,
      "cache_read_input_tokens": 39741,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2754
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 207,
          "cache_read_input_tokens": 39741,
          "cache_creation_input_tokens": 2754,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2754,
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

_source line 24 · 2026-05-25T09:06:12.280Z_

<details><summary>↩ Tool result · reported error · `toolu_01CR3FMzLeBSo38K2nu3FD61`</summary>

```text
Exit code 2
grep: Unmatched \{
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f11c515d-cc09-4dd7-87c7-2bc9972bb0c1",
  "isSidechain": true,
  "promptId": "f9b7a34c-f506-492b-bf34-76d808a6acc5",
  "agentId": "ad2899e5fc9701ddb",
  "type": "user",
  "uuid": "d6ca8bb0-851b-4643-b674-9f5fa9564b22",
  "toolUseResult": "Error: Exit code 2\ngrep: Unmatched \\{",
  "sourceToolAssistantUUID": "f11c515d-cc09-4dd7-87c7-2bc9972bb0c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-25T09:06:13.390Z_

Let me fix the regex:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6ca8bb0-851b-4643-b674-9f5fa9564b22",
  "isSidechain": true,
  "agentId": "ad2899e5fc9701ddb",
  "requestId": "req_011CbP2BoFK53exrsXhvn1UT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "86cb13bd-2b3e-46ab-85dd-bbd450457099",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AwfddZq2ZWZNhvsVoAWxED",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 5166,
      "cache_read_input_tokens": 42495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5166,
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

_source line 26 · 2026-05-25T09:06:14.532Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01F1V79a9hTicPX7wZSK2eaQ`</summary>

```json
{
  "command": "grep -n \"\\\\\\\\begin{equation}\\|\\\\\\\\begin{align}\\|\\\\\\\\begin{assumption}\\|\\\\\\\\begin{proposition}\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86cb13bd-2b3e-46ab-85dd-bbd450457099",
  "isSidechain": true,
  "agentId": "ad2899e5fc9701ddb",
  "requestId": "req_011CbP2BoFK53exrsXhvn1UT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "55ff42dd-c2c8-4d89-8bdc-d22e8ca6e397",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AwfddZq2ZWZNhvsVoAWxED",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 5166,
      "cache_read_input_tokens": 42495,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5166
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 127,
          "cache_read_input_tokens": 42495,
          "cache_creation_input_tokens": 5166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5166,
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

_source line 27 · 2026-05-25T09:06:14.602Z_

<details><summary>↩ Tool result · `toolu_01F1V79a9hTicPX7wZSK2eaQ`</summary>

```text
309:\begin{equation}
1324:\begin{assumption}[Mode Amplification]\label{ass:mode_amp}
1330:\begin{proposition}[Entropy is a first-order indicator]\label{prop:entropy_first}
1343:\begin{proposition}[Diversity is a threshold indicator]\label{prop:div_threshold}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55ff42dd-c2c8-4d89-8bdc-d22e8ca6e397",
  "isSidechain": true,
  "promptId": "f9b7a34c-f506-492b-bf34-76d808a6acc5",
  "agentId": "ad2899e5fc9701ddb",
  "type": "user",
  "uuid": "9b0e827e-81f9-4e97-9b6c-63819d0d375b",
  "sourceToolAssistantUUID": "55ff42dd-c2c8-4d89-8bdc-d22e8ca6e397",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-25T09:06:16.176Z_

Now let me read the file in smaller chunks to get the exact captions and context. Let me start systematically:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b0e827e-81f9-4e97-9b6c-63819d0d375b",
  "isSidechain": true,
  "agentId": "ad2899e5fc9701ddb",
  "requestId": "req_011CbP2ByCr6vRazaiyZbHjy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3aac6fe6-83ba-4d16-809b-5f7e30142cb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HZHCe4yaCyd4JMQkfoLqxj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 218,
      "cache_read_input_tokens": 47661,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 218,
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

_source line 29 · 2026-05-25T09:06:16.443Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EZdK1enJng7HMW6qTmbS3A`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "limit": 800,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3aac6fe6-83ba-4d16-809b-5f7e30142cb0",
  "isSidechain": true,
  "agentId": "ad2899e5fc9701ddb",
  "requestId": "req_011CbP2ByCr6vRazaiyZbHjy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0eee7902-4b59-45d0-afb7-a2d913282ffa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HZHCe4yaCyd4JMQkfoLqxj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 218,
      "cache_read_input_tokens": 47661,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 218
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 149,
          "cache_read_input_tokens": 47661,
          "cache_creation_input_tokens": 218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 218,
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

_source line 30 · 2026-05-25T09:06:16.772Z_

<details><summary>↩ Tool result · `toolu_01EZdK1enJng7HMW6qTmbS3A`</summary>

```text
0	\appendix
1	
2	\section{Training Details and Metric Drift}
3	\label{app:training_details}
4	\label{app:drift}
5	
6	\paragraph{Hyperparameters.}
7	Each generation fine-tunes for 5{,}000 steps using AdamW (learning rate $5 \times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium).
8	Generation uses temperature $1.0$, top-$k{=}50$, max length 512 tokens, producing 5{,}000 samples per generation from 5{,}000-sample subsets of WikiText-103.
9	Canary metrics: token entropy $H(p_\theta | \text{context})$ over 1{,}000 held-out samples; ECE with 15 bins.
10	Additional downstream metrics (distinct-3, effective rank, Self-BLEU) appear in subsequent appendix sections.
11	
12	\paragraph{Architecture-specific training.}
13	Table~\ref{tab:arch_hyperparams} reports training hyperparameters for each architecture in the cross-architecture evaluation (\S\ref{sec:generalization}).
14	All models use the same generation parameters (temperature~$1.0$, top-$k{=}50$, max length 512) to control for decoding-strategy confounds.
15	Batch sizes are adjusted for GPU memory constraints; learning rates follow the respective model families' recommended fine-tuning ranges.
16	
17	\begin{table}[t]
18	\centering
19	\small
20	\caption{Per-architecture training hyperparameters.}
21	\label{tab:arch_hyperparams}
22	\begin{tabular}{lcccl}
23	\toprule
24	Model & Batch & LR & Steps & Precision \\
25	\midrule
26	Pythia-410M & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
27	Pythia-1.4B & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
28	Pythia-6.9B & 2 & $2{\times}10^{-5}$ & 5{,}000 & bf16 \\
29	GPT-2-medium & 32 & $5{\times}10^{-5}$ & 5{,}000 & fp32/bf16 \\
30	OPT-1.3B & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
31	Qwen3.5-0.8B & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
32	SmolLM3-3B & 4 & $2{\times}10^{-5}$ & 5{,}000 & fp32 \\
33	\bottomrule
34	\end{tabular}
35	\end{table}
36	
37	\paragraph{Metric computation details.}
38	Token entropy is computed as $H(p_\theta | x) = -\sum_{v} p_\theta(v|x) \log_2 p_\theta(v|x)$, averaged over 1{,}000 held-out WikiText-103 samples using greedy teacher-forcing (no sampling stochasticity).
39	ECE uses 15 equal-width bins on the confidence axis $c(x) = \max_v p_\theta(v|x)$, following the standard definition~\citep{naeini2015obtaining}:
40	$\mathrm{ECE} = \sum_{b=1}^{B} \frac{|b|}{N} |\mathrm{acc}(b) - \mathrm{conf}(b)|$.
41	Distinct-$n$ ($n \in \{1, 2, 3\}$) is the ratio of unique $n$-grams to total $n$-grams across all 5{,}000 generated samples per generation, following~\citet{li2016diversity}.
42	Perplexity is computed on a fixed 1{,}000-sample held-out split (disjoint from training and generation prompts).
43	
44	\paragraph{Seed and replication structure.}
45	The primary experiments use seeds 42, 43, 44 (3-seed cohort) for the phase diagram ($T{=}10$, 13 $\alpha$ levels).
46	Seed 45 is added for $\alpha{=}1.0$ experiments (4-seed).
47	Extended FPR analysis uses seeds 45--51 (6-pair basis, excluding MAUVE) for a total of 10 distinct seeds.
48	Cross-$T$ extensions ($T{=}15$, $20$, $25$) use the same seed set as the corresponding $\alpha$ condition.
49	
50	\paragraph{Metric drift.}
51	Table~\ref{tab:drift_summary} reports the relative change in each metric from generation~0 to generation~10 across six contamination levels.
52	Two patterns emerge: (1)~entropy and calibration (ECE) degrade monotonically with $\alpha$, while (2)~diversity metrics exhibit a non-monotonic relationship where the largest relative decline occurs at moderate contamination ($\alpha{=}0.25$) rather than full replacement ($\alpha{=}1.0$).
53	Figure~\ref{fig:metric_trajectory} (main text) visualizes representative per-generation trajectories, showing the distinct temporal profiles that underlie the Granger-precedence analysis in \S\ref{sec:method}.
54	
55	\begin{table}[t]
56	\centering
57	\small
58	\caption{Metric drift (\%, generation~0$\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\alpha{=}0.25$: distinct-1 $-40.3{\pm}0.3\%$) rather than full replacement ($\alpha{=}1.0$: $-27.8{\pm}1.6\%$). $^\dagger$$\alpha{=}0.10$: single seed (seed~42, preliminary). $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3-seed mean${\pm}$std (seeds 42, 43, 44); $\alpha{=}1.0$: 4-seed mean${\pm}$std (seeds 42, 43, 44, 45).}
59	\label{tab:drift_summary}
60	\resizebox{\columnwidth}{!}{%
61	\begin{tabular}{lccccc}
62	\toprule
63	$\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\
64	\midrule
65	0.00 & $-4.6{\pm}0.4$ & $+37.6{\pm}14$ & $-14.1{\pm}0.4$ & $-9.6{\pm}0.4$ & $-20.6{\pm}1.0$ \\
66	0.10$^\dagger$ & $-5.3$ & $+57$ & $-39.6$ & $-56.4$ & $-21.0$ \\
67	0.25 & $-4.7{\pm}0.5$ & $+81.8{\pm}15.9$ & $-40.3{\pm}0.3$ & $-56.4{\pm}0.7$ & $-18.1{\pm}0.8$ \\
68	0.50 & $-18.0{\pm}0.5$ & $+822.6{\pm}18.3$ & $-37.1{\pm}0.4$ & $-50.4{\pm}1.0$ & $+21.0{\pm}0.1$ \\
69	0.75 & $-27.6{\pm}0.2$ & $+1791{\pm}18$ & $-32.3{\pm}0.5$ & $-41.0{\pm}1.0$ & $+182.6{\pm}0.7$ \\
70	1.00 & $-60.8{\pm}1.2$ & $+3780{\pm}30$ & $-27.8{\pm}1.6$ & $-34.0{\pm}3.3$ & $+3674{\pm}45$ \\
71	\bottomrule
72	\end{tabular}}
73	\end{table}
74	
75	\paragraph{Data pipeline.}
76	Each generation follows a fixed protocol: (1)~sample 5{,}000 prompts from WikiText-103 (first 32 tokens of random paragraphs); (2)~generate 512-token continuations using the current model $M_t$ with temperature~$1.0$, top-$k{=}50$; (3)~mix $\alpha$ fraction of generated text with $(1{-}\alpha)$ fraction of fresh WikiText-103 samples; (4)~fine-tune from the \emph{previous generation's} checkpoint (not from pretrained $M_0$).
77	Step~(4) produces iterative collapse by accumulating distributional biases across generations, distinct from single-generation fine-tuning drift.
78	The ``replace'' paradigm (step~3) means each generation trains on a completely fresh synthetic pool---there is no accumulation of earlier-generation synthetic data within the training set.
79	
80	\paragraph{Null-condition drift interpretation.}
81	At $\alpha{=}0.0$ (Table~\ref{tab:drift_summary}), all metrics exhibit non-trivial drift despite zero synthetic contamination: distinct-1 drops $14.1\%$, entropy drops $4.6\%$, and perplexity \emph{improves} by $20.6\%$.
82	This null drift reflects iterated fine-tuning on a fixed corpus: the model progressively memorizes WikiText-103, narrowing its effective vocabulary (lower distinct-$n$, lower entropy) while fitting the held-out distribution better (lower PPL).
83	The distinction between null drift and contamination-induced collapse is critical: our detection framework specifically tests whether canary metrics \emph{temporally precede} downstream metrics, not whether drift exists.
84	Null drift produces shared downward trends but without the temporal structure (lag) that Granger testing requires.
85	
86	\paragraph{Non-monotonic diversity-contamination relationship.}
87	A counterintuitive finding in Table~\ref{tab:drift_summary}: diversity loss is \emph{largest} at $\alpha{=}0.25$ (distinct-1: $-40.3\%$) and \emph{smallest} at $\alpha{=}1.0$ ($-27.8\%$).
88	This non-monotonicity arises because at high $\alpha$, the model collapses rapidly into a few dominant modes (by gen~3--4), after which diversity stabilizes near a floor.
89	The gen-0$\to$10 relative decline is smaller because the trajectory is concave (fast initial drop, then plateau).
90	At $\alpha{=}0.25$, the real-data fraction prevents catastrophic collapse but allows a steady, monotonic diversity decline across all 10 generations, producing a larger cumulative loss.
91	
92	
93	\section{Distinct-3 Results}
94	\label{app:distinct3}
95	
96	Table~\ref{tab:distinct3_drift} reports distinct-3 drift across all contamination levels.
97	Distinct-3 exhibits the largest absolute decline among diversity metrics at low contamination ($-58.9{\pm}0.9\%$ at $\alpha{=}0.25$) but attenuates at higher levels ($-30.5\%$ at $\alpha{=}1.0$), consistent with the diversity--calibration dissociation discussed in \S\ref{sec:discussion}.
98	
99	\begin{table}[t]
100	\centering
101	\small
102	\caption{Distinct-3 drift (\%, generation~0$\to$10) across contamination levels. $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.75$: 3-seed mean${\pm}$std; $\alpha{=}1.0$: 4-seed mean${\pm}$std; $\alpha{=}0.50$: single seed.}
103	\label{tab:distinct3_drift}
104	\begin{tabular}{lc}
105	\toprule
106	$\alpha$ & Distinct-3 drift (\%) \\
107	\midrule
108	0.00 & $-4.4{\pm}0.5$ \\
109	0.25 & $-58.9{\pm}0.9$ \\
110	0.50 & $-52.4$ \\
111	0.75 & $-38.6{\pm}1.3$ \\
112	1.00 & $-30.5{\pm}4.0$ \\
113	\bottomrule
114	\end{tabular}
115	\end{table}
116	
117	Distinct-3 exhibits higher lag instability than distinct-1/2 (bimodal lag distribution, std${>}1.5$ vs.\ ${<}0.5$ generations), reflecting its lower signal-to-noise ratio at 512-token generation length.
118	
119	\paragraph{Non-monotonic attenuation.}
120	The inverted-U shape of diversity loss (peaking at $\alpha{=}0.25$--$0.50$, attenuating at $\alpha{=}1.0$) is consistent across all three distinct-$n$ metrics.
121	At low contamination, diversity loss reflects fine-tuning drift amplified by weak synthetic contamination, which narrows the vocabulary without triggering the catastrophic mode collapse that dominates at high $\alpha$.
122	At $\alpha{=}1.0$, the model collapses into a small set of high-frequency modes quickly (by gen~3--4), after which diversity stabilizes at a low floor; the relative decline from gen-0 is therefore smaller because the trajectory is concave rather than linear.
123	
124	\paragraph{Granger detectability of distinct-3.}
125	Despite its large magnitude, distinct-3 drift is less Granger-detectable than distinct-1/2 because of its higher temporal noise.
126	PermG detection rates at $\alpha{=}1.0$: entropy$\to$distinct-1 achieves 6/8 across all seeds; entropy$\to$distinct-3 achieves only 4/8, with 2 seeds failing due to lag instability (bimodal lag distribution shifting the peak between lag~$-1$ and lag~$-2$ across seeds).
127	This motivates our focus on distinct-1 and distinct-2 as the primary downstream metrics in the main text.
128	
129	
130	\section{Observation Window Sensitivity}
131	\label{app:window_sensitivity}
132	
133	Consensus classification stabilizes at $T_{\min}{\geq}5$ (Table~\ref{tab:window_sensitivity}): all six effect-size reference pairs reach $K{\geq}4/5$ agreement at every window from $T_{\min}{=}5$ through $T_{\min}{=}10$.
134	
135	\paragraph{Per-method stability.}
136	At $\alpha{=}1.0$ (Pythia-410M, 4~seeds), we evaluate detection stability as $T_{\min}$ varies from 5 to 10 (i.e., using only generations $T_{\min}$ through $T{=}10$).
137	NaiveXCorr, DiffXCorr, ThresholdOnset, and PermG all maintain 6/6 validated pairs at every window length, confirming complete invariance to the observation start point.
138	Toda--Yamamoto shows the most variability: 3/6 at $T_{\min}{=}5$, rising to 6/6 at $T_{\min}{=}7$, then fluctuating between 3/6 and 6/6 at $T_{\min}{=}8$--$10$.
139	This instability reflects TY's higher sensitivity to degrees of freedom in short series (each 1-generation reduction removes ${\sim}10\%$ of available data at $T{=}10$).
140	
141	\paragraph{Implications for deployment.}
142	The stability result has a practical implication: a monitoring system need not wait for a full $T{=}10$ observation window before running detection.
143	As few as 6 data points ($T_{\min}{=}5$) suffice for reliable consensus-based detection at high contamination ($\alpha{=}1.0$), though the detection boundary $\alpha_c$ at shorter windows remains above $\alpha{=}0.50$ (insufficient power at $T{=}5$ for onset-level contamination).
144	The minimum requirement for Granger-type tests is $T_{\min}{\geq}5$ (below which degrees of freedom are insufficient for lag-1 regression with 2~parameters).
145	
146	\begin{figure}[t]
147	\centering
148	\includegraphics[width=\columnwidth]{figures/fig_window_sensitivity.pdf}
149	\caption{Detection stability as a function of minimum observation window $T_{\min}$ (Pythia-410M, $\alpha{=}1.0$, 4~seeds). PermG forward detection (6/8) and consensus classification ($K{\geq}4$) both stabilize at $T_{\min}{\geq}5$, with no significance flips for $T_{\min} \in [5, 10]$. This robustness confirms that the choice of $T_{\min}{=}5$ in the main analysis does not drive results.}
150	\label{fig:window_sensitivity}
151	\end{figure}
152	
153	\begin{table}[t]
154	\centering
155	\small
156	\caption{Observation window sensitivity for Tier~3 consensus ($K{\geq}4/5$) at $\alpha{=}1.0$ (Pythia-410M, 4~seeds). Tier~3 pairs: number of canary$\to$downstream pairs (out of 8 validated) reaching $K{\geq}4/5$ method agreement. TY pairs: number of effect-size reference pairs (out of 6) reaching Toda--Yamamoto significance (moderate supplementary method; \S\ref{sec:method}). Consensus stabilizes at $T_{\min}{\geq}5$; TY stabilizes at $T_{\min}{\geq}6$.}
157	\label{tab:window_sensitivity}
158	\resizebox{\columnwidth}{!}{%
159	\begin{tabular}{lccccccccc}
160	\toprule
161	& \multicolumn{8}{c}{Minimum observation window $T_{\min}$} \\
162	\cmidrule(lr){2-9}
163	& 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\
164	\midrule
165	Tier~3 pairs (/8)    & $\dagger$ & $\dagger$ & 6 & 6 & 6 & 6 & 6 & 6 \\
166	TY pairs$^\S$ (/6)   & $\dagger$ & $\dagger$ & 3--6 & 3--6 & 3--6 & 3--6 & 3--6 & 6 \\
167	Stable               & ---       & ---       & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark \\
168	\bottomrule
169	\multicolumn{9}{l}{\footnotesize $\dagger$~Insufficient degrees of freedom for Granger-type tests ($<6$ data points).} \\
170	\multicolumn{9}{l}{\footnotesize $^\S$~TY directional assignment under verification.}
171	\end{tabular}}
172	\end{table}
173	
174	\FloatBarrier
175	\section{Robustness Analysis}
176	\label{app:robustness}
177	\label{app:spec_curve}
178	
179	\paragraph{Permutation count and FDR sensitivity.}
180	PermG $p$-values are stable between 5{,}000 and 10{,}000 permutations (max $|\Delta p|{=}0.010$, 0/24 significance flips at $\alpha{=}0.75$).
181	Treatment/null separation is robust to FDR threshold choice: at $q{=}0.05$, 4/36 null pairs vs.\ 19/24 treatment pairs reach significance; at $q{=}0.10$, null rejections rise to 8/36.
182	At the onset boundary ($\alpha{=}0.45$), minimum FDR-corrected $p$-values ($0.059$--$0.091$) are consistent with a continuous power transition rather than binary absence of signal.
183	
184	\paragraph{Specification curve.}
185	We construct 1{,}160 specifications from 13 contamination levels, 4~seeds, and 8 canary$\to$downstream pairs (all PermG, $n_\text{perm}{=}5{,}000$, BH FDR $q{=}0.05$).
186	
187	\begin{table}[t]
188	\centering
189	\small
190	\caption{Specification curve summary (1{,}160 specifications, D120-compliant). The blind$\to$onset jump is robust across specifications: 0\% significance rate through $\alpha{=}0.45$, rising to 75\% at $\alpha{=}0.50$.}
191	\label{tab:spec_curve}
192	\begin{tabular}{lc}
193	\toprule
194	Metric & Value \\
195	\midrule
196	Total specifications & 1{,}160 \\
197	Significant (FDR $q{<}0.05$) & 536 (46.2\%) \\
198	\midrule
199	\emph{By regime} & \\
200	\quad Blind ($\alpha \leq 0.45$) & 0\% \\
201	\quad Onset ($\alpha{=}0.50$) & 75\% \\
202	\quad Detection ($\alpha \geq 0.75$) & 62--75\% \\
203	\bottomrule
204	\end{tabular}
205	\end{table}
206	
207	The blind$\to$onset jump holds across the vast majority of specifications (Figure~\ref{fig:spec_curve}, main text).
208	
209	\paragraph{Specification decomposition.}
210	Within the 536 significant specifications (46.2\% of 1{,}160), the detection rate varies by canary$\to$downstream pair:
211	entropy$\to$distinct-1 and entropy$\to$distinct-2 are the most consistently detectable (significant in 75\% of above-onset specifications), while ECE$\to$perplexity is never significant (0\%, consistent with the first-differencing result in \S\ref{sec:regime}).
212	MAUVE-paired specifications show intermediate rates (50\% at $\alpha{=}1.0$, 0\% at $\alpha{=}0.50$), reflecting MAUVE's floor saturation at 1.4B scale.
213	
214	\paragraph{Cross-seed invariance.}
215	The specification curve's most notable feature is the \emph{absence} of seed-dependent specifications: no specification is significant at one seed but non-significant at another within the same $(\alpha, \text{pair})$ cell for $\alpha \in \{0.50, 0.75, 1.0\}$.
216	This uniformity (Fisher exact: $p = 3.45 \times 10^{-11}$ for the 0/8$\to$6/8 transition) provides the strongest evidence that the detection onset is a property of the data-generating process rather than a particular random initialization.
217	
218	\paragraph{Alternative FDR thresholds.}
219	Repeating the specification curve at $q{=}0.10$ increases significant specifications from 46.2\% to 53.8\%, with the additional detections concentrated at $\alpha{=}0.45$ (4 specifications cross from non-significant to significant) and $\alpha{=}0.60$ (2 specifications).
220	At $q{=}0.01$, the rate drops to 38.4\%, losing detections at $\alpha{=}0.50$ (onset boundary becomes less reliable).
221	The blind$\to$onset jump persists at all three thresholds, confirming structural robustness.
222	
223	\section{Transfer Entropy and Change-Point Analysis}
224	\label{app:transfer_entropy}
225	\phantomsection\label{app:te_mi}
226	
227	Transfer entropy (TE; \citealp{schreiber2000measuring}; 3-bin discretization, $n{=}5{,}000$ permutations) yields 0/192 BH-corrected significant pairs across all conditions, confirming that nonparametric information-theoretic methods lack power at $T{=}11$.
228	A KNN-based TE estimator ($k{=}5$) shows forward-dominant TE fraction increasing monotonically with $\alpha$ (4/8 at $\alpha{=}0.25$ to 8/8 at $\alpha{=}1.0$), but this does not reach statistical significance after FDR correction.
229	
230	\paragraph{Symbolic transfer entropy.}
231	Symbolic TE~\citep{staniek2008symbolic} using Bandt--Pompe ordinal patterns ($m{=}2$, lag${=}1$, 500 circular-shift surrogates, $p{<}0.05$) provides a complementary view.
232	At the $\alpha{=}0.60$ sync-dip where PermG detects 0/8, symbolic TE detects forward causation in 4/6 pairs ($p{<}0.001$): MAUVE-channel TE${=}0.539$ at $T{=}10$ and $0.496$ at $T{=}15$; distinct-1-channel TE${=}0.122$ at $T{=}20$.
233	Positive controls where PermG succeeds (6/8) yield 0/6 significant symbolic TE pairs (TE values 0.000--0.379, all $p{>}0.14$), and baseline conditions ($T{=}5$, $\alpha{=}0.50$) yield 0/2 significant (TE${=}0.000$--$0.189$, $p{=}1.000$).
234	This pattern---symbolic TE detecting signal precisely where PermG fails---suggests the sync-dip reflects compressed temporal lag rather than absent coupling: ordinal-pattern methods capture contemporaneous co-movement that Granger's lag-based framework misses.
235	
236	\paragraph{Conditional Granger analysis.}
237	To test whether ECE confounds the entropy$\to$diversity relationship, we run conditional Granger tests controlling for ECE when testing entropy$\to$diversity and vice versa.
238	Conditioning on ECE does not eliminate entropy's predictive contribution, consistent with the ECE co-movement argument (Appendix~\ref{app:cascade_theory}): both metrics respond to the same underlying mode amplification, but entropy provides the earliest signal.
239	
240	\phantomsection\label{app:change_point}
241	\paragraph{Change-point detection.}
242	Max-split change-point tests ($n{=}5{,}000$ bootstrap) yield 66.7\% FPR under null control (12/18, $\alpha{=}0.00$), precluding use as a standalone detector.
243	However, the temporal ordering of change-points reverses between null and treatment: under null, downstream metrics break first (gen~2) before canary (gen~4--8); under treatment ($\alpha{\geq}0.75$), canary breaks first (gen~1) before downstream (gen~2--4).
244	This ordering reversal shifts monotonically with $\alpha$, consistent with the Granger-precedence analysis.
245	
246	
247	\section{Sequential Monitoring: CUSUM vs Calibrated Threshold}
248	\label{app:csmp}
249	
250	CUSUM sequential testing~\citep{page1954continuous} calibrated against $\alpha{=}0.0$ null control (FAR${=}$0\%) produces identical alarm times as a simple $2\sigma$ threshold at all tested operating points: both trigger at generation~1 for $\alpha{\geq}0.50$.
251	The equivalence arises because the generation-0$\to$1 entropy drop ($|\Delta x|{>}0.7$) greatly exceeds null variability ($\sigma_0{\approx}0.03$); CUSUM's cumulative memory provides no advantage when the initial shift dominates.
252	
253	\paragraph{Operating characteristics.}
254	We evaluate both methods across the full contamination range:
255	\begin{itemize}
256	\item $\alpha{=}0.00$--$0.45$: neither method triggers within $T{=}10$ generations (entropy drift ${\leq}5.3\%$, within null variability band).
257	\item $\alpha{=}0.50$: both trigger at generation~1 (entropy drop $18.0{\pm}0.5\%$, exceeding $2\sigma$ and CUSUM threshold simultaneously).
258	\item $\alpha{=}0.75$--$1.0$: both trigger at generation~1 (entropy drop $27.6$--$60.8\%$).
259	\end{itemize}
260	The regime structure of CUSUM/threshold monitoring thus recapitulates the PermG blind zone: no detection below $\alpha{=}0.50$ at $T{=}10$, immediate detection above.
261	The critical difference is that these methods detect \emph{deviation from baseline}, not \emph{temporal precedence}---they cannot distinguish whether entropy leads or lags diversity without additional directional analysis.
262	
263	\paragraph{Practical implications.}
264	For production monitoring where establishing Granger precedence is unnecessary, a calibrated entropy threshold ($[10\%, 22\%]$; Appendix~\ref{app:intervention_sensitivity}) provides a simple, zero-cost alarm.
265	CUSUM adds value only when the signal emerges gradually across multiple generations (e.g., at contamination levels near $\alpha_c$ where the generation-0$\to$1 drop is small); in our setting, the large initial entropy shift renders CUSUM's cumulative advantage moot.
266	
267	\paragraph{Detection timing comparison.}
268	Table~\ref{tab:sequential_timing} compares alarm generation for CUSUM and calibrated threshold across the full contamination range.
269	
270	\begin{table}[t]
271	\centering
272	\small
273	\caption{Sequential monitoring alarm timing (Pythia-410M, seed~42, fp32). ``---'' = no alarm within $T{=}10$. Both methods produce identical alarm patterns: no detection below $\alpha{=}0.50$, immediate (gen-1) detection above.}
274	\label{tab:sequential_timing}
275	\begin{tabular}{lccl}
276	\toprule
277	$\alpha$ & CUSUM alarm & Threshold alarm & Entropy drop (\%) \\
278	\midrule
279	0.00 & --- & --- & $-4.6$ \\
280	0.10 & --- & --- & $-5.3$ \\
281	0.25 & --- & --- & $-4.7$ \\
282	0.45 & --- & --- & $-5.1$ \\
283	0.50 & gen-1 & gen-1 & $-18.0$ \\
284	0.60 & gen-1 & gen-1 & $-28.5$ \\
285	0.75 & gen-1 & gen-1 & $-27.6$ \\
286	1.00 & gen-1 & gen-1 & $-60.8$ \\
287	\bottomrule
288	\end{tabular}
289	\end{table}
290	
291	The binary alarm pattern (no alarm below $\alpha{=}0.50$, immediate alarm above) mirrors PermG's regime structure, confirming that the blind zone is a property of the data-generating process rather than the detection method.
292	However, sequential monitoring methods cannot distinguish between causal temporal precedence and synchronous co-movement---a system relying solely on CUSUM would flag $\alpha{=}0.50$ contamination but could not determine whether entropy decline \emph{causes} or merely \emph{accompanies} diversity loss.
293	
294	\paragraph{False alarm rate calibration.}
295	Under null control ($\alpha{=}0.0$), neither method triggers false alarms at any threshold within the safe operating band $[10\%, 22\%]$, yielding FAR${=}0\%$ across all 3 null-condition seeds.
296	At thresholds below 7.5\%, both methods produce false alarms at gen-3 ($\alpha{=}0.0$ entropy drift: $-4.6\%$ approaches the threshold), giving FAR${=}100\%$.
297	This calibration sensitivity motivates a two-threshold deployment strategy: use the lenient bound ($10\%$) for early warning and the strict bound ($22\%$) for confirmed alarm, with the gap serving as a monitoring zone requiring additional diagnostic tests (e.g., Granger analysis) before triggering intervention.
298	
299	\section{Background and Notation}
300	\label{app:background}
301	\label{sec:background}
302	
303	This section establishes the formal setup and notation used throughout the paper.
304	
305	\paragraph{Iterative training loop.}
306	Let $M_0$ denote a pretrained language model and $\mathcal{D}_\text{real}$ a fixed corpus of human-written text.
307	At each generation $t \geq 1$, the model $M_{t-1}$ generates a synthetic corpus $\mathcal{D}_\text{synth}^{(t-1)}$, and the next-generation model $M_t$ is fine-tuned on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data:
308	\begin{equation}
309	    \mathcal{D}_\text{train}^{(t)} = \alpha \cdot \mathcal{D}_\text{synth}^{(t-1)} \;+\; (1{-}\alpha) \cdot \mathcal{D}_\text{real}, \quad \alpha \in [0, 1].
310	    \label{eq:mixing}
311	\end{equation}
312	At $\alpha{=}1.0$, this reduces to the full-replacement paradigm of \citet{shumailov2024curse}.
313	
314	\paragraph{Metric families.}
315	\emph{Canary metrics}: token entropy ($H(p_\theta | \text{context})$ on held-out samples) and expected calibration error (ECE).
316	\emph{Downstream metrics}: distinct-$n$ ($n \in \{1, 2, 3\}$)~\citep{li2016diversity} and perplexity.
317	Each metric produces a time series of $T{+}1$ observations.
318	
319	\paragraph{Lead-lag testing.}
320	Given canary series $X$ and downstream series $Y$, the central question is whether changes in $X$ temporally precede changes in $Y$, requiring directionality and confounder control beyond simple correlation.
321	We employ five methods spanning permissive to conservative: naive cross-correlation, differenced cross-correlation, threshold onset detection, permutation Granger causality~\citep{shojaie2022granger}, and Toda--Yamamoto Granger causality~\citep{toda1995statistical}.
322	
323	\paragraph{Method details.}
324	\emph{Naive cross-correlation (NaiveXCorr)} computes Pearson $r$ between $X_{t}$ and $Y_{t+\ell}$ at lag $\ell \in [-5, 5]$; significance at any lag below uncorrected $p{<}0.05$ counts as detection.
325	This method is permissive because it ignores shared trends and applies no multiplicity correction.
326	\emph{Differenced cross-correlation (DiffXCorr)} applies the same procedure to first-differenced series $\Delta X_t = X_t - X_{t-1}$, controlling for common trends but remaining bidirectional (cannot distinguish $X \to Y$ from $Y \to X$).
327	\emph{Threshold onset detection} identifies the first generation where each metric crosses a $3\sigma$ threshold below its generation-0 value (where $\sigma$ is the null-control standard deviation); detection is declared if canary onset strictly precedes downstream onset.
328	\emph{Permutation Granger causality (PermG)} tests whether lagged $X$ values improve prediction of $Y$ beyond $Y$'s own history, using 5{,}000 temporal permutations to construct a nonparametric null distribution, followed by BH-FDR correction at $q{=}0.05$ across 8 metric pairs.
329	\emph{Toda--Yamamoto (TY)} augments a VAR model with $d_{\max}$ extra lags to handle potential non-stationarity, then tests the original lag coefficients via Wald test.
330	
331	\paragraph{PermG implementation details.}
332	The permutation Granger procedure operates as follows:
333	(1)~First-difference both series: $\Delta X_t = X_t - X_{t-1}$, $\Delta Y_t = Y_t - Y_{t-1}$.
334	(2)~Fit unrestricted model: $\Delta Y_t = a_0 + \sum_{j=1}^{L} a_j \Delta Y_{t-j} + \sum_{j=1}^{L} b_j \Delta X_{t-j} + \epsilon_t$ (max lag $L{=}5$).
335	(3)~Fit restricted model: $\Delta Y_t = a_0 + \sum_{j=1}^{L} a_j \Delta Y_{t-j} + \epsilon_t$.
336	(4)~Compute observed $F$-statistic from the residual sum of squares reduction.
337	(5)~Generate 5{,}000 null realizations by randomly permuting the temporal order of $\Delta X$, re-fitting unrestricted model each time.
338	(6)~$p$-value $= (\text{count}(F_{\text{perm}} \geq F_{\text{obs}}) + 1) / (n_{\text{perm}} + 1)$ following~\citet{phipson2010permutation}.
339	The permutation scheme destroys temporal structure in $X$ while preserving its marginal distribution, providing an exact null for the hypothesis ``past $X$ does not improve prediction of $Y$.''
340	Lag selection uses AIC with maximum $L{=}5$ (constrained by $T{-}2L \geq 3$ degrees of freedom at $T{=}11$).
341	
342	\paragraph{Direction checking.}
343	For each significant pair, we additionally test the reverse direction ($Y \to X$).
344	A pair is classified as ``forward-only'' if $X \to Y$ is significant and $Y \to X$ is not; ``bidirectional'' if both are significant; and ``reverse-only'' if only $Y \to X$ is significant.
345	Forward-only pairs provide the strongest evidence for temporal precedence.
346	In the main analysis, we report forward detection counts; bidirectional pairs are flagged in the failure mode taxonomy (\S\ref{sec:generalization}).
347	
348	\paragraph{Multiple testing structure.}
349	At each contamination level and seed, we test 8 canary$\to$downstream pairs (2 canary $\times$ 4 downstream metrics; MAUVE is a 9th pair included in some analyses).
350	BH-FDR correction at $q{=}0.05$ is applied within each $(\alpha, \text{seed}, \text{method})$ family of 8 tests, yielding corrected $p$-values $p_{\mathrm{fdr}}$.
351	We do not correct across $\alpha$ levels or seeds, as these represent genuinely different conditions rather than multiple looks at the same hypothesis.
352	The 8-pair correction is conservative relative to per-family error rate control: BH-FDR at $q{=}0.05$ guarantees that at most 5\% of rejected hypotheses are false discoveries, averaging across the 8 tests within each family.
353	
354	\section{MMCT Algorithm}
355	\label{app:mmct}
356	
357	\noindent\emph{See Algorithm~\ref{alg:mmct} in the main text (\S\ref{sec:mmct}) for the full MMCT pseudocode and design rationale.}
358	
359	\begin{figure}[t]
360	\centering
361	\includegraphics[width=\columnwidth]{figures/consensus_heatmap.pdf}
362	\caption{$K{\geq}3$ consensus heatmap across the $\alpha \times T$ grid (Pythia-410M, fp32). Each cell shows the number of canary$\to$diversity pairs reaching majority agreement (${\geq}3/5$ methods). Consensus detection aligns with PermG's onset at $\alpha{=}0.50$ but eliminates the non-monotonic anomaly at $\alpha{=}0.60$ (consensus detects 8/8 where PermG detects 0/8), indicating the anomaly is PermG-specific.}
363	\label{fig:consensus_heatmap}
364	\end{figure}
365	
366	\paragraph{MMCT design rationale.}
367	The MMCT consensus approach is motivated by the observation that no single method achieves both low FPR and high detection rate across all contamination levels.
368	PermG has the lowest FPR (6.7\%) but misses the $\alpha{=}0.60$ regime; DiffXCorr detects everywhere but cannot establish directionality; NaiveXCorr's 94.4\% FPR makes it unsuitable as a standalone detector.
369	By requiring $K{\geq}3$ methods to agree, MMCT effectively requires that at least one conservative method (PermG or DiffXCorr) participates in the consensus, filtering out detections driven solely by permissive methods.
370	
371	\paragraph{FPR-inverse weighting design.}
372	The weight $w_k = 1/\max(\widehat{\mathrm{FPR}}_k, \epsilon)$ ensures that methods with lower empirical FPR have proportionally higher influence on the consensus score.
373	The floor $\epsilon{=}0.01$ prevents division by zero for methods with 0\% FPR (none in our case).
374	Under this scheme, PermG's weight ($w{=}14.9$) dominates NaiveXCorr's ($w{=}1.06$) by $14{\times}$: a detection requires PermG agreement unless ${\geq}4$ other methods agree without it.
375	The empirical null distribution (step~7 of Algorithm~\ref{alg:mmct}) avoids parametric assumptions that would be unreliable for our short ($T{=}5$--$25$), non-stationary series.
376	
377	\paragraph{Sensitivity to $K$.}
378	Table~\ref{tab:mmct_k_operating} (main text) reports operating characteristics for $K \in \{2, 3, 4, 5\}$.
379	The $K{=}3$ threshold represents a Pareto-optimal operating point: decreasing to $K{=}2$ raises FPR from 10.0\% to 38.9\% with modest TPR gain ($66.7\% \to 85.4\%$ at $\alpha{=}0.50$); increasing to $K{=}4$ eliminates false positives ($0\%$) but drops TPR to ${\leq}25\%$ across all conditions.
380	At $K{=}5$ (unanimity), the expected detection rate is below 5\% everywhere---only achievable when all five methods, including the 94\%-FPR NaiveXCorr, agree.
381	
382	\begin{figure}[t]
383	\centering
384	\includegraphics[width=\columnwidth]{figures/fig_mmct_k_operating.pdf}
385	\caption{MMCT operating characteristics as a function of consensus threshold $K$. Left axis: FPR (null-control false positives); right axis: FNR (missed detections at $\alpha{\geq}0.50$). $K{=}3$ balances FPR and sensitivity; $K{=}4$ reduces FPR further but increases FNR, particularly at boundary conditions. $K{=}2$ is dominated by high-FPR methods (NaiveXCorr, TY) and provides no useful filtering.}
386	\label{fig:mmct_k_operating}
387	\end{figure}
388	
389	\section{Methodological Comparison Table}
390	\label{app:method_comparison}
391	
392	Table~\ref{tab:method-comparison} summarizes the methodological coverage of existing canary and monitoring analyses across the diagnostic dimensions identified in \S\ref{sec:method}.
393	No prior work combines all six dimensions.
394	
395	\begin{table}[t]
396	\centering
397	\small
398	\caption{Methodological comparison of canary and monitoring analyses. \checkmark\ = present, $\times$ = absent, $\circ$ = partial (${\leq}2$ levels or limited replication). Diff.\ = differencing/stationarity controls. Multi-M.\ = ${\geq}2$ independent statistical methods. MTC = multiple testing correction. Regime = systematic variation of $\alpha$. Seeds = ${\geq}3$ independent seeds. Arch.\ = ${\geq}2$ architecturally distinct model families.}
399	\label{tab:method-comparison}
400	\resizebox{\columnwidth}{!}{%
401	\begin{tabular}{lccccccl}
402	\toprule
403	Work & Diff. & Multi-M. & MTC & Regime & Seeds & Arch. & Metrics \\
404	\midrule
405	\citet{shumailov2024curse}     & $\times$   & $\times$   & $\times$   & $\circ$    & \checkmark & \checkmark & PPL \\
406	\citet{du2025scales}           & $\times$   & $\times$   & \checkmark & \checkmark & \checkmark & $\times$   & ECE, Acc, Dist-$n$ \\
407	\citet{gambetta2024surplexity} & $\times$   & $\times$   & $\times$   & \checkmark & \checkmark & \checkmark & Surplexity, Ent \\
408	SIGMA~\citep{sigma2026spectral} & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & Spectral \\
409	DCES~\citep{dces2026counter}    & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & \checkmark & ECE, Ent, PPL \\
410	\midrule
411	\textbf{Ours}                  & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & Ent, ECE, PPL, Dist-$n$ \\
412	\bottomrule
413	\end{tabular}%
414	}
415	\end{table}
416	
417	\paragraph{Dimension justification.}
418	The six diagnostic dimensions in Table~\ref{tab:method-comparison} are motivated by known failure modes in time-series causal inference:
419	\emph{Differencing} controls spurious regression when both series share a deterministic trend~\citep{granger1974spurious}---without it, any two monotonically declining series will appear correlated.
420	\emph{Multi-method comparison} addresses the method sensitivity documented in \S\ref{sec:mmct}: a single method's conclusion may reflect its assumptions rather than the data.
421	\emph{Multiple testing correction} is necessary because each contamination level generates 8 metric pairs; uncorrected testing at $p{<}0.05$ expects ${\sim}0.4$ false positives per condition.
422	\emph{Regime variation} is required to map the detection landscape rather than reporting a single operating point.
423	\emph{Seed replication} distinguishes signal from initialization artifacts.
424	\emph{Cross-architecture evaluation} tests whether findings are specific to one model family or reflect general properties of iterative collapse.
425	Among existing works, \citet{du2025scales} comes closest (4/6 dimensions) but omits differencing and multi-method analysis, both of which our results show are critical.
426	
427	\section{Extended Discussion}
428	\label{app:extended_discussion}
429	
430	\paragraph{Calibration scope.}
431	All calibration results are specific to our setup (Pythia-410M, WikiText-103, $T{=}10$).
432	On C4 at $\alpha{=}0.50$, PermG reverse reaches 7/8 (seed-dependent: s43 1/8), indicating directional asymmetry should be verified per domain.
433	Token entropy ($H(p_\theta|\text{context})$ on held-out data) and perplexity ($\exp(H_\text{cross})$ on generated text) co-move synchronously, explaining why first-differencing eliminates canary$\to$perplexity but preserves canary$\to$diversity.
434	
435	\paragraph{Alternative explanations for the blind zone.}
436	Three mechanisms could explain why detection fails below $\alpha_c$:
437	\emph{(1)~Signal absence}: at low $\alpha$, the real-data fraction dominates, and the model's distributional shift is too small to generate temporal structure detectable by any linear method.
438	\emph{(2)~Power limitation}: the signal exists but falls below PermG's detection threshold at $T{=}10$ (supported by the $T{=}20$ result showing 5/8 at $\alpha{=}0.45$).
439	\emph{(3)~Contemporaneous coupling}: at low $\alpha$, entropy and diversity respond simultaneously rather than sequentially, eliminating the lag that Granger tests require.
440	The MI analysis (Appendix~\ref{app:mi_analysis}) favors explanation~(2): coupling between entropy and diversity exists throughout the blind zone ($\hat{I}_G > 0$ at all $\alpha$), and the cross-$T$ results confirm that longer observation resolves detection at $\alpha{=}0.45$.
441	However, explanation~(3) may contribute at very low $\alpha$ (${\leq}0.10$), where the contamination signal is minimal and both metrics drift primarily due to fine-tuning.
442	
443	\paragraph{Entropy as a measurement artifact.}
444	A potential concern is that entropy's ``leading'' behavior reflects measurement sensitivity rather than a genuine temporal cascade: entropy is a continuous quantity computed from the full probability distribution, while distinct-$n$ is a discrete count computed from a finite sample.
445	Entropy can therefore respond to arbitrarily small distributional shifts that leave the token-level generation unchanged.
446	We note three counterarguments:
447	(1)~The ECE co-movement result confirms that calibration---a separate measurement---also shifts at gen-1, suggesting the signal is real.
448	(2)~First-differencing preserves the canary$\to$diversity relationship while eliminating canary$\to$perplexity, which would not occur if the signal were purely a measurement artifact.
449	(3)~The intervention experiment demonstrates that acting on the entropy signal at gen-1 produces a measurably different outcome (64\% lower peak perplexity), confirming functional relevance.
450	Nonetheless, the possibility that entropy's sensitivity partly reflects measurement properties rather than causal priority cannot be fully excluded without mechanistic analysis.
451	
452	\paragraph{Cross-architecture failure mode analysis.}
453	The four non-confirming conditions in the cross-architecture evaluation each isolate a distinct assumption violation:
454	
455	\begin{table}[t]
456	\centering
457	\small
458	\caption{Failure mode taxonomy for non-confirming cross-architecture conditions ($\alpha{=}1.0$).}
459	\label{tab:failure_modes}
460	\resizebox{\columnwidth}{!}{%
461	\begin{tabular}{llll}
462	\toprule
463	Condition & PermG & Failure mode & Root cause \\
464	\midrule
465	GPT-2 bf16 & 0/8 & Precision & bf16 noise masks signal \\
466	GPT-2 s43 & 6/8 both & Bidirectional & No directional separation \\
467	Pythia-1.4B s42 & 2/8 & Seed & Initialization-dependent \\
468	SmolLM3-3B & 3/8 & Decoupling & Entropy non-monotonic \\
469	\bottomrule
470	\end{tabular}}
471	\end{table}
472	
473	The precision failure (GPT-2 bf16) is actionable: switching to fp32 resolves detection (0/8$\to$6/8) with no change to the underlying collapse dynamics.
474	The bidirectional failure (GPT-2 s43) is more fundamental: it indicates that for some model-seed combinations, the entropy-diversity temporal structure is symmetric, preventing directional assignment.
475	The seed dependence (Pythia-1.4B s42 vs.\ s43: 2/8 vs.\ 6/8) highlights the fragility of directional testing in short series.
476	The entropy decoupling (SmolLM3-3B: entropy 0/4, ECE 3/4) directly violates the cascade ordering assumption, suggesting that SmolLM3's architecture produces a qualitatively different collapse trajectory.
477	
478	\paragraph{Scale verification (Pythia-1.4B).}
479	\label{app:scale_14b}
480	
481	\begin{table}[t]
482	\centering
483	\small
484	\caption{Pythia-1.4B phase diagram replication: PermG forward/reverse detection and $K{\geq}3$ consensus across contamination levels and observation windows (fp32). $\dagger$: bidirectional confounding (reverse${}>0$). Denominator is 8 unless marked $^{*}$ (6-pair basis, MAUVE unavailable).}
485	\label{tab:14b_phase}
486	\begin{tabular}{@{}llcccc@{}}
487	\toprule
488	$T$ & $\alpha$ & Seed & Fwd & Rev & $K{\geq}3$ \\
489	\midrule
490	10 & 0.45 & 42 & 0/8 & 0/8 & 0/8 \\
491	   &      & 43 & 1/8 & 0/8 & 2/8 \\
492	   &      & 44 & 0/6$^{*}$ & 0/6$^{*}$ & 0/6$^{*}$ \\
493	\cmidrule(l){2-6}
494	   & 0.50 & 42 & 4/8 & 2/8$^{\dagger}$ & 3/8 \\
495	   &      & 43 & 6/6$^{*}$ & 0/6$^{*}$ & 1/6$^{*}$ \\
496	   &      & 44 & 6/6$^{*}$ & 0/6$^{*}$ & 0/6$^{*}$ \\
497	\cmidrule(l){2-6}
498	   & 0.60 & 42 & 4/8 & 0/8 & 3/8 \\
499	   &      & 43 & 4/8 & 6/8$^{\dagger}$ & 3/8 \\
500	   &      & 44 & 6/6$^{*}$ & 0/6$^{*}$ & 5/6$^{*}$ \\
501	\cmidrule(l){2-6}
502	   & 0.75 & 42 & 5/8 & 0/8 & 5/8 \\
503	   &      & 43 & 6/8 & 5/8$^{\dagger}$ & 5/8 \\
504	   &      & 44 & 6/6$^{*}$ & 0/6$^{*}$ & 6/6$^{*}$ \\
505	\midrule
506	15 & 0.45 & 42 & 3/8 & 0/8 & 4/8 \\
507	   &      & 43 & 5/6$^{*}$ & 3/6$^{*\dagger}$ & 3/6$^{*}$ \\
508	\cmidrule(l){2-6}
509	   & 0.50 & 42 & 3/8 & 0/8 & 2/8 \\
510	   &      & 43 & 3/6$^{*}$ & 0/6$^{*}$ & 3/6$^{*}$ \\
511	\cmidrule(l){2-6}
512	   & 0.60 & 42 & 6/8 & 0/8 & 6/8 \\
513	   &      & 43 & 6/6$^{*}$ & 3/6$^{*\dagger}$ & 6/6$^{*}$ \\
514	\cmidrule(l){2-6}
515	   & 0.75 & 42 & 6/8 & 0/8 & 6/8 \\
516	   &      & 43 & 6/6$^{*}$ & 0/6$^{*}$ & 6/6$^{*}$ \\
517	\bottomrule
518	\end{tabular}
519	\end{table}
520	
521	Phase-diagram structure is qualitatively preserved at 1.4B (Table~\ref{tab:14b_phase}; Figure~\ref{fig:14b_phase}): detection boundary at $\alpha_c{\approx}0.50$, cross-$T$ improvement at 3/4 $\alpha$ values ($\alpha{=}0.45$: $0/6{\to}5/6$).
522	The 410M sync-dip does not reproduce at 1.4B (4/6 at $\alpha{=}0.60$, $T{=}10$).
523	Bidirectional confounding is seed-specific: s43 shows reverse significance at $\alpha{=}0.60$ (6/8) and $\alpha{=}0.75$ (5/8) for $T{=}10$, while s42 maintains 0 reverse across all conditions.
524	
525	\begin{figure}[t]
526	\centering
527	\includegraphics[width=\columnwidth]{figures/fig_14b_phase.pdf}
528	\caption{Pythia-1.4B phase diagram (PermG forward, 6-pair basis). Detection boundary ($\alpha_c \approx 0.50$) is consistent with 410M.}
529	\label{fig:14b_phase}
530	\end{figure}
531	
532	\paragraph{Scale effects on detection topology.}
533	Three scale-dependent effects emerge from comparing 410M and 1.4B:
534	\begin{enumerate}
535	\item \emph{Sync-dip suppression}: The $\alpha{=}0.60$ non-monotonic anomaly is absent at 1.4B (4/6--6/6 vs.\ 0/8 at 410M), suggesting that larger models maintain wider entropy-diversity temporal separation, preventing the lag compression that produces the dip.
536	\item \emph{Seed variability amplification}: Cross-seed detection variance is higher at 1.4B (s42: 2/8 vs.\ s43: 6/8 at $\alpha{=}1.0$) than at 410M (6/8 across all seeds), possibly reflecting the larger model's richer attractor landscape.
537	\item \emph{Domain transfer}: Pythia-1.4B on C4 yields 8/8 PermG forward detection ($K{\geq}3{=}8/8$) compared to 2--6/8 on WikiText, indicating that domain characteristics (vocabulary coverage, topic diversity) interact with scale to affect detection sensitivity.
538	\end{enumerate}
539	
540	\paragraph{Intervention at 1.4B.}
541	Predictive cessation replicates at 1.4B: entropy drops $51.9\%$ ($2.946 \to 1.418$) at gen-1, triggering intervention.
542	Peak PPL rises from $19.68$ to $65.37$ (a $232\%$ increase, vs.\ $112\%$ at 410M), but recovery is faster (gen-2 PPL${=}17.44$, below the gen-0 baseline).
543	The larger entropy drop at 1.4B ($51.9\%$ vs.\ $40.7\%$) reflects stronger mode amplification at scale, consistent with the theoretical prediction that higher-capacity models amplify dominant modes more aggressively~\citep{shumailov2024curse}.
544	
545	
546	\FloatBarrier
547	\section{Per-Method Dose-Response Profiles}
548	\label{app:dose_response}
549	
550	Table~\ref{tab:dose_response_full} reports FDR significance counts (/8 validated pairs) for all five detection methods across 12 contamination levels (seed~42, Pythia-410M, WikiText, fp32).
551	PermG exhibits a sharp 0$\to$6 jump at $\alpha{=}0.50$ with a return to 0 at $\alpha{=}0.55$--$0.60$ (non-monotonic dip), while other methods show diffuse profiles: naive cross-correlation saturates at 7--8/8 across all levels including the null, and Toda--Yamamoto fluctuates without a clear onset.
552	
553	\begin{table}[t]
554	\centering
555	\small
556	\caption{Per-method FDR significance (/8 pairs) across contamination levels (Pythia-410M, seed~42, WikiText, fp32). PermG and Diff.\ XCorr use BH-corrected FDR ($q{=}0.05$); Naive XCorr, Threshold, and TY use uncorrected $p{<}0.05$ (no FDR field in pipeline). $\alpha{=}1.0$ from Pythia-410M cross-architecture condition (same seed/domain/precision).}
557	\label{tab:dose_response_full}
558	\resizebox{\columnwidth}{!}{%
559	\begin{tabular}{lccccc}
560	\toprule
561	$\alpha$ & Naive & Diff.\ XCorr & Threshold & PermG & TY$^\S$ \\
562	\midrule
563	0.00 & 8 & 4 & 3 & \textbf{0} & 1 \\
564	0.10 & 7 & 6 & 0 & \textbf{0} & 0 \\
565	0.25 & 8 & 3 & 0 & \textbf{0} & 2 \\
566	0.30 & 8 & 4 & 0 & \textbf{0} & 3 \\
567	0.35 & 8 & 4 & 0 & \textbf{0} & 1 \\
568	0.40 & 8 & 3 & 0 & \textbf{0} & 4 \\
569	0.45 & 8 & 6 & 0 & \textbf{0} & 1 \\
570	0.50 & 8 & 7 & 4 & \textbf{6} & 3 \\
571	0.55 & 8 & 8 & 0 & \textbf{0} & 1 \\
572	0.60 & 8 & 6 & 0 & \textbf{0} & 0 \\
573	0.75 & 7 & 6 & 0 & \textbf{6} & 3 \\
574	1.00 & 8 & 6 & 2 & \textbf{6} & 1 \\
575	\bottomrule
576	\multicolumn{6}{l}{\footnotesize $^\S$TY directional assignment under verification; column retained for completeness.} \\
577	\end{tabular}}
578	\end{table}
579	
580	PermG's dose-response profile most cleanly separates detection regimes: 0/8 at null, sharp 0$\to$6 onset at $\alpha{=}0.50$, non-monotonic dip at $\alpha{=}0.55$--$0.60$.
581	Naive monitoring baselines (PPL-slope, variance-threshold) fire at $\alpha{=}0.0$ (FPR 67--100\%) because fine-tuning drift is indistinguishable from contamination without directional testing.
582	
583	\paragraph{Method-specific observations.}
584	\emph{NaiveXCorr} saturates at 7--8/8 at every $\alpha$ including null, making it useless for regime discrimination---its FPR (94.4\%) means it would declare detection in 19 out of 20 null-control runs.
585	\emph{DiffXCorr} shows the highest detection rate at $\alpha{\geq}0.50$ (6--8/8) but maintains 4/8 at null, yielding FPR${=}37.5\%$.
586	Its bidirectional nature (significant in both forward and reverse) prevents causal attribution but confirms the presence of coupling.
587	\emph{Threshold onset} is highly specific (3/8 at null) but insensitive (0/8 at $\alpha{=}0.10$--$0.45$ and $\alpha{=}0.55$--$0.75$), detecting only when the generation-1 entropy drop is unambiguously large.
588	\emph{Toda--Yamamoto} fluctuates between 0/8 and 4/8 across all $\alpha$ levels with no clear dose-response structure, reflecting its poor finite-sample properties at $T{=}10$.
589	
590	\paragraph{Inter-method agreement.}
591	Cohen's $\kappa$ between all method pairs ranges from $-0.04$ (NaiveXCorr vs.\ Threshold, near-random disagreement) to $0.42$ (PermG vs.\ DiffXCorr, moderate agreement above onset).
592	The low overall $\kappa{=}0.185$ across all five methods reflects the fundamental tension: permissive methods detect everywhere (including null), conservative methods detect rarely, and moderate methods disagree about boundary cases.
593	This motivates the MMCT consensus approach (\S\ref{sec:mmct}), which aggregates information from all methods while weighting by empirical reliability.
594	
595	\begin{figure}[t]
596	\centering
597	\includegraphics[width=\columnwidth]{figures/fig_per_method_phase_top.pdf}
598	\caption{Per-method FDR-significant pair counts (/8) across contamination levels (Pythia-410M, seed~42, $T{=}10$, fp32). PermG~(d) exhibits the cleanest regime separation---zero detections through $\alpha{=}0.45$, then a sharp 0$\to$6 jump at $\alpha{=}0.50$; NaiveXCorr~(a) saturates at 7--8/8 across all levels including null; DiffXCorr~(b) detects signal but cannot separate forward from reverse. The visual contrast across panels illustrates why method choice is itself a primary source of variability ($\kappa{=}0.185$).}
599	\label{fig:per_method_phase}
600	\end{figure}
601	
602	\begin{figure}[t]\ContinuedFloat
603	\centering
604	\includegraphics[width=\columnwidth]{figures/fig_per_method_phase_bottom.pdf}
605	\caption[]{(\textit{continued})}
606	\end{figure}
607	
608	\section{Cross-Seed Consistency at $\alpha{=}0.60$}
609	\label{app:alpha060}
610	
611	The non-monotonic detection gap at $\alpha{=}0.60$ (\S\ref{sec:dose_response}) is consistent across seeds: PermG yields 0/8 FDR-significant forward pairs for both seed~42 (v4 recompilation) and seed~43.
612	An earlier pipeline version (v3, seed~42) reported 3/8; the discrepancy is resolved by the d120 recompilation that corrected FPR calibration.
613	
614	\paragraph{Detailed metrics at $\alpha{=}0.60$.}
615	Despite PermG non-detection, metric drift at $\alpha{=}0.60$ is substantial: token entropy $-28.5\%$ (gen-0: $3.234$, gen-10: $2.311$), ECE $+1561\%$ ($0.0108 \to 0.179$), perplexity $+92.3\%$ ($26.95 \to 51.83$).
616	Raw (pre-FDR) $p$-values are marginal: ECE$\to$distinct-1 $p{=}0.034$, ECE$\to$distinct-2 $p{=}0.047$---both would pass at uncorrected $\alpha{=}0.05$ but fail BH-FDR correction ($q{=}0.05$, 8 simultaneous tests).
617	This indicates that the signal exists but falls below the corrected significance threshold, consistent with the temporal-compression interpretation.
618	
619	\paragraph{Cross-$T$ behavior.}
620	The sync-dip at $\alpha{=}0.60$ persists across observation windows: $T{=}5$: 0/8; $T{=}10$: 0/8 (both s42, s43); $T{=}15$: 0/8 (s42); $T{=}20$: 0/8 (s42), 3/8 (s43, partial dissolution).
621	Full dissolution occurs only at $T{=}25$: PermG 5/8 (s42), $K{\geq}3$ consensus 6/8.
622	The pattern---persistent non-detection for $T{\leq}20$, resolution at $T{=}25$---is consistent with $\sqrt{T}$ power accumulation eventually resolving a compressed (but non-zero) temporal lag.
623	
624	\paragraph{Scale dependence.}
625	Pythia-1.4B does \emph{not} exhibit the sync-dip at $\alpha{=}0.60$: PermG detects 4/8 (s42) and 4/6 (s43) at $T{=}10$, rising to 6/8 and 6/6 at $T{=}15$.
626	This scale-dependence suggests the phenomenon is architecture-specific: at larger scale, the entropy-diversity lag may be structurally wider (more capacity $\to$ slower mode collapse propagation), preventing the temporal compression that produces the dip at 410M.
627	
628	\paragraph{Sigmoid fit impact.}
629	The sigmoid fit excluding $\alpha{=}0.60$ yields $k{=}5.66$, $\alpha_c{=}0.765$, $R^2{=}0.286$; including it degrades $R^2$ to 0.205 and shifts $\alpha_c$ rightward by 0.058, confirming the point is a genuine outlier rather than noise.
630	Predicted detection probability at $\alpha{=}0.60$ under the sigmoid model is $P(\mathrm{det}){=}0.282$, far below the observed 0/8 (0.00), indicating the anomaly cannot be explained by smooth dose-response variation.
631	
632	\FloatBarrier
633	\section{PPL Threshold Baseline}
634	\label{app:ppl_threshold}
635	
636	A reviewer asked whether a naive perplexity threshold could match entropy's detection timing.
637	We evaluate thresholds at $+10\%$, $+25\%$, $+50\%$, $+100\%$, $+150\%$, and $+200\%$ above the generation-0 baseline PPL (26.95).
638	
639	\paragraph{Threshold-by-threshold results.}
640	The PPL trajectory at $\alpha{=}1.0$ (Pythia-410M, s42) evolves rapidly: gen-0${=}26.95$, gen-1${=}57.42$ ($+113.1\%$), gen-2${=}162.15$ ($+501.9\%$), gen-3${=}279.17$, gen-5${=}508.85$, gen-10${=}1017.81$.
641	All thresholds from $+10\%$ through $+100\%$ trigger at generation~1, because the gen-0$\to$gen-1 jump ($+113.1\%$) exceeds them all.
642	Thresholds at $+150\%$ and $+200\%$ delay triggering to generation~2 (PPL${=}162.15$ exceeds both).
643	
644	\paragraph{Comparison with entropy.}
645	Entropy's advantage over PPL monitoring is operational rather than temporal at $\alpha{=}1.0$:
646	\begin{enumerate}
647	\item \emph{Zero cost}: entropy is computed from the model's output distribution during generation---no held-out evaluation set or separate forward pass required.
648	\item \emph{Direct signal}: entropy detects distributional narrowing (mode collapse) directly; PPL detects its downstream consequence (degraded generalization).
649	\item \emph{Regime sensitivity}: at lower contamination ($\alpha{=}0.50$), entropy drops $18.0\%$ at gen-1 while PPL rises only $21.0\%$ over 10~generations---a PPL threshold calibrated for $\alpha{=}1.0$ would miss $\alpha{=}0.50$ entirely.
650	\end{enumerate}
651	
652	\paragraph{When PPL monitoring suffices.}
653	For production systems where $\alpha$ is expected to be high (e.g., known synthetic data pipelines), a PPL threshold at $+50\%$ provides equivalent detection timing to entropy with the added benefit of measuring a directly user-relevant quantity (generation quality).
654	The operational cost difference becomes relevant only for online monitoring at scale, where computing held-out PPL on every generation adds latency and requires maintaining a clean reference set.
655	
656	
657	\section{PermG Power Analysis}
658	\label{app:power_analysis}
659	
660	We simulate PermG power under a bivariate DGP with linear coupling $\beta$ ($T \in \{6,\ldots,20\}$, 100 replications, 5{,}000 permutations, BH FDR $q{=}0.05$).
661	At $T{=}10$, $\beta_{50}{=}2.0$ (50\% power requires strong coupling); at $T{=}20$, $\beta_{50}$ drops to 0.9 (Table~\ref{tab:beta50}).
662	Power grows faster than $\sqrt{T}$, so the $\sqrt{T}$ formula in \S\ref{sec:theory} is a conservative lower bound.
663	FPR under FDR correction remains ${\leq}2\%$ across all $T$.
664	
665	\paragraph{Detailed power values.}
666	Selected FDR-corrected power levels illustrate the gain from longer observation: at $\beta{=}1.0$, power rises from 0.17 ($T{=}10$) to 0.30 ($T{=}15$) to 0.66 ($T{=}20$); at $\beta{=}2.0$, from 0.51 ($T{=}10$) to 0.92 ($T{=}15$) to 0.98 ($T{=}20$).
667	Raw FPR (before FDR correction) is higher but still controlled: $T{=}6$: 1\%, $T{=}8$: 6\%, $T{=}10$: 9\%, $T{=}15$: 6\%, $T{=}20$: 5\%.
668	The non-monotonic raw FPR peak at $T{=}10$ reflects the discrete-sample properties of permutation tests at small $T$; FDR correction absorbs this variation.
669	
670	\paragraph{$\sqrt{T}$ scaling product.}
671	If power scaled exactly as $\sqrt{T}$, the product $\beta_{50} \cdot \sqrt{T}$ would be constant.
672	Observed values: $T{=}8$: 5.09; $T{=}10$: 6.32; $T{=}15$: 4.65; $T{=}20$: 4.02.
673	The downward trend indicates that power grows faster than $\sqrt{T}$---each additional generation contributes more information than a simple $\sqrt{T}$ model predicts, likely because the cumulative signal (not just instantaneous SNR) drives detection in Granger-type tests.
674	
675	\paragraph{Toda--Yamamoto bootstrap comparison.}
676	TY bootstrap power simulations (200 reps, same DGP) yield substantially lower power at comparable $T$: $T{=}10$ power${=}0.205$ (vs.\ PermG 0.51 at $\beta{=}2.0$), $T{=}20$ power${=}0.409$, with Type~I error rate 8.1\% (above nominal).
677	TY's $d$-augmented lag structure wastes degrees of freedom in short series, explaining its inferior power-FPR tradeoff relative to PermG.
678	
679	\begin{table}[t]
680	\centering
681	\small
682	\caption{PermG power analysis: $\beta_{50}$ (coupling for 50\% power) under BH-FDR correction ($q{=}0.05$, 8 pairs). Dashes: $<$50\% power not reached within $\beta \leq 2.0$.}
683	\label{tab:beta50}
684	\begin{tabular}{lcccc}
685	\toprule
686	$T$ & $\beta_{50}$ & $\beta_{50} \cdot \sqrt{T}$ & FPR (raw) & FPR (FDR) \\
687	\midrule
688	6  & ---  & ---  & 1\% & 0\% \\
689	8  & ---  & ---  & 6\% & 2\% \\
690	10 & 2.0  & 6.32 & 9\% & 2\% \\
691	15 & 1.2  & 4.65 & 6\% & 2\% \\
692	20 & 0.9  & 4.02 & 5\% & 1\% \\
693	\bottomrule
694	\end{tabular}
695	\end{table}
696	
697	
698	\section{Non-Stationarity Robustness Analysis}
699	\label{app:nonstationarity}
700	
701	Monte Carlo simulation (AR(1) DGP, $T{=}11$, 1{,}000 reps) shows PermG FPR inflates to ${\sim}10\%$ under strong non-stationarity ($\varphi{\geq}0.95$), while first-differencing maintains proper size ($4.2$--$6.6\%$) at the cost of reduced power (Table~\ref{tab:nonstationarity_sim}).
702	Our pipeline applies first-differencing before permutation testing, combining both advantages.
703	Under null conditions ($\alpha{=}0.0$), token entropy exhibits $\varphi{=}-0.51$ (far from the danger zone); first-differencing reduces distinct-1's high raw $\varphi$ ($0.81$--$0.97$, reflecting deterministic trend) to $-0.14$--$0.44$.
704	Our empirical FPR of 4/60 (6.7\%) confirms adequate size control.
705	
706	\begin{figure}[t]
707	\centering
708	\includegraphics[width=\columnwidth]{figures/fig_ar1_diagnostic.pdf}
709	\caption{AR(1) coefficient estimates across five contamination levels (Pythia-410M, seed~42). (a)~Token entropy: raw $\varphi$ transitions from negative ($-0.51$ at $\alpha{=}0.00$) to near-unit-root ($1.00$ at $\alpha{=}1.00$), but first-differencing keeps all values below 0.98. (b)~Distinct-1: raw $\varphi$ is uniformly high ($0.75$--$0.95$) even at null, driven by deterministic trend; first-differencing reduces all to ${\leq}0.24$. Dashed red line: $\varphi{=}0.95$ danger zone.}
710	\label{fig:ar1_diagnostic}
711	\end{figure}
712	
713	\begin{table}[t]
714	\centering
715	\small
716	\caption{Size and power under AR(1) DGP ($T{=}11$, 1{,}000 reps). First-differencing maintains nominal size; PermG FPR inflates at $\varphi{\geq}0.95$.}
717	\label{tab:nonstationarity_sim}
718	\resizebox{\columnwidth}{!}{%
719	\begin{tabular}{lcccccc}
720	\toprule
721	& \multicolumn{3}{c}{Size (\%, $\beta{=}0$)} & \multicolumn{3}{c}{Power (\%, $\beta{=}0.6$)} \\
722	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
723	$\varphi$ & Raw GC & First-Diff & PermG & Raw GC & First-Diff & PermG \\
724	\midrule
725	0.50 & 6.4 & 6.6 & 6.8 & 37.7 & 17.7 & 36.8 \\
726	0.95 & 10.0 & 5.9 & 9.5 & 44.3 & 28.7 & 41.5 \\
727	0.99 & 11.2 & 4.2 & 10.7 & 46.4 & 24.6 & 41.7 \\
728	\bottomrule
729	\end{tabular}}
730	\end{table}
731	
732	\paragraph{Empirical AR(1) coefficients.}
733	Table~\ref{tab:empirical_ar1} reports estimated AR(1) coefficients for all metric series under null ($\alpha{=}0.0$) and treatment ($\alpha{=}1.0$) conditions.
734	Under the null, all metrics exhibit $|\varphi| < 0.60$ in raw levels and $|\varphi| < 0.30$ after first-differencing, well within the safe zone.
735	Under treatment, raw distinct-$n$ series reach $\varphi{=}0.81$--$0.97$ (near unit root), but first-differencing reduces these to $\varphi{=}-0.14$--$0.44$---confirming that the deterministic trend, not stochastic persistence, drives the high raw autocorrelation.
736	
737	\begin{table}[t]
738	\centering
739	\small
740	\caption{Empirical AR(1) coefficients (Pythia-410M, 4~seeds). ``Raw'' = levels; ``Diff'' = first-differenced.}
741	\label{tab:empirical_ar1}
742	\resizebox{\columnwidth}{!}{%
743	\begin{tabular}{lcccc}
744	\toprule
745	& \multicolumn{2}{c}{$\alpha{=}0.0$} & \multicolumn{2}{c}{$\alpha{=}1.0$} \\
746	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
747	Metric & Raw $\varphi$ & Diff $\varphi$ & Raw $\varphi$ & Diff $\varphi$ \\
748	\midrule
749	Token entropy & $-0.51$ & $-0.28$ & $0.72$ & $0.15$ \\
750	ECE & $0.31$ & $-0.15$ & $0.95$ & $0.38$ \\
751	Distinct-1 & $0.55$ & $0.12$ & $0.97$ & $0.44$ \\
752	Distinct-2 & $0.48$ & $0.08$ & $0.95$ & $0.31$ \\
753	Perplexity & $0.42$ & $-0.22$ & $0.93$ & $-0.14$ \\
754	\bottomrule
755	\end{tabular}}
756	\end{table}
757	
758	\paragraph{ADF test results.}
759	Augmented Dickey--Fuller tests on first-differenced series reject the unit root hypothesis at $p{<}0.05$ in all 40 series (5~metrics $\times$ 4~seeds $\times$ 2~conditions), confirming that first-order differencing ($d{=}1$) is sufficient and higher-order differencing ($d{\geq}2$) would unnecessarily reduce power (Figure~\ref{fig:differencing_dmax}).
760	
761	\paragraph{Why not KPSS?}
762	We use ADF (null: unit root) rather than KPSS (null: stationarity) because ADF is more conservative for our purpose: rejecting the unit-root null provides positive evidence of stationarity, while KPSS's failure to reject would only indicate insufficient evidence against stationarity.
763	In the short-series regime ($T{\leq}25$), KPSS has limited power; ADF's rejection at $p{<}0.05$ across all differenced series provides stronger evidence.
764	
765	\paragraph{Power cost of first-differencing.}
766	First-differencing eliminates spurious regression but reduces effective power by discarding level information (Table~\ref{tab:diff_power_cost}).
767	Under the AR(1) DGP ($\varphi{=}0.50$, $\beta{=}0.6$), first-differenced PermG achieves 17.7\% power versus 36.8\% for raw PermG---a 52\% relative power reduction.
768	At $\varphi{=}0.95$ the cost narrows (28.7\% vs.\ 41.5\%, 31\% reduction) because the stronger persistence makes the raw test less reliable (inflated FPR).
769	Our pipeline accepts this power cost as a necessary tradeoff: at the empirical autocorrelation levels observed in treatment series ($\varphi{=}0.72$--$0.97$ in raw levels), raw Granger testing would produce ${\sim}10\%$ FPR, invalidating the detection framework.
770	
771	\begin{table}[t]
772	\centering
773	\small
774	\caption{Power cost of first-differencing under simulated AR(1) DGP ($T{=}11$, $\beta{=}0.6$, 1{,}000 reps). The power reduction is the price paid for valid size control.}
775	\label{tab:diff_power_cost}
776	\begin{tabular}{lcccc}
777	\toprule
778	$\varphi$ & Raw power & Diff power & Reduction & Raw FPR \\
779	\midrule
780	0.50 & 36.8\% & 17.7\% & 52\% & 6.8\% \\
781	0.95 & 41.5\% & 28.7\% & 31\% & 9.5\% \\
782	0.99 & 41.7\% & 24.6\% & 41\% & 10.7\% \\
783	\bottomrule
784	\end{tabular}
785	\end{table}
786	
787	The practical consequence: at $T{=}10$, the differencing-induced power loss is the primary bottleneck for detecting weak contamination ($\alpha < 0.50$).
788	Extending observation to $T{=}20$ more than compensates: differenced power at $T{=}20$ exceeds raw power at $T{=}10$ for $\varphi \leq 0.95$, providing both valid size control and superior detection sensitivity.
789	This explains the large detection gains observed in the $T{=}20$ extension (\S\ref{app:t20_comparison}).
790	
791	\FloatBarrier
792	\section{Shapley Value Analysis}
793	\label{app:shapley}
794	
795	Shapley values~\citep{shapley1953value} computed over all $2^5{=}32$ coalitions quantify each method's marginal contribution to FPR and FNR (Table~\ref{tab:shapley_6pair}).
796	DiffXCorr achieves the best combined Shapley ($-0.299$) but cannot separate forward from reverse; among directional methods, PermG ranks best ($-0.141$).
797	The 8-pair variant (including MAUVE) yields identical rankings.
798	
799	\begin{figure}[t]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0eee7902-4b59-45d0-afb7-a2d913282ffa",
  "isSidechain": true,
  "promptId": "f9b7a34c-f506-492b-bf34-76d808a6acc5",
  "agentId": "ad2899e5fc9701ddb",
  "type": "user",
  "uuid": "2a739ff9-c20c-469c-a8d4-f66c3f08a29a",
  "sourceToolAssistantUUID": "0eee7902-4b59-45d0-afb7-a2d913282ffa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-25T09:06:19.489Z_

Let me continue reading the rest of the file systematically:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a739ff9-c20c-469c-a8d4-f66c3f08a29a",
  "isSidechain": true,
  "agentId": "ad2899e5fc9701ddb",
  "requestId": "req_011CbP2C8ed7fXs68ZagQeNJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "48ca05f1-b915-4f18-941e-5045c3e40870",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Wi8ar14mVf5K45527mc6jb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 23640,
      "cache_read_input_tokens": 47879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23640,
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

_source line 32 · 2026-05-25T09:06:20.485Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BG3YrGrYCgKUgkyTr1q3v3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "limit": 2000,
  "offset": 800
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48ca05f1-b915-4f18-941e-5045c3e40870",
  "isSidechain": true,
  "agentId": "ad2899e5fc9701ddb",
  "requestId": "req_011CbP2C8ed7fXs68ZagQeNJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "eafd53fb-f5f3-4d17-9352-ba80e4f693fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Wi8ar14mVf5K45527mc6jb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 23640,
      "cache_read_input_tokens": 47879,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 23640
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 138,
          "cache_read_input_tokens": 47879,
          "cache_creation_input_tokens": 23640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 23640,
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

_source line 33 · 2026-05-25T09:06:20.795Z_

<details><summary>↩ Tool result · `toolu_01BG3YrGrYCgKUgkyTr1q3v3`</summary>

```text
800	\begin{figure}[t]
801	\centering
802	\includegraphics[width=\columnwidth]{figures/fig_shapley_contribution_top.pdf}
803	\caption{Shapley value decomposition by method. FPR contribution (positive = worse) and FNR contribution (negative = better) are shown for each of the five detection methods. DiffXCorr achieves the best combined Shapley ($-0.299$) but lacks directional separation; among directional methods, PermG ranks best ($-0.141$). NaiveXCorr contributes the most FPR ($+0.609$) due to its inability to distinguish signal from null drift.}
804	\label{fig:shapley_contribution}
805	\end{figure}
806	
807	\begin{figure}[t]\ContinuedFloat
808	\centering
809	\includegraphics[width=\columnwidth]{figures/fig_shapley_contribution_bottom.pdf}
810	\caption[]{(\textit{continued})}
811	\end{figure}
812	
813	\begin{table}[t]
814	\centering
815	\small
816	\caption{Shapley value decomposition (6-pair, MAUVE excluded). Combined = FPR + FNR (more negative = better).}
817	\label{tab:shapley_6pair}
818	\begin{tabular}{lccc}
819	\toprule
820	Method & $\phi^{\text{FPR}}$ & $\phi^{\text{FNR}}$ & $\phi^{\text{comb}}$ \\
821	\midrule
822	Naive XCorr          & $+0.609$ & $-0.419$ & $+0.190$ \\
823	\textbf{Diff.\ XCorr}& $\mathbf{+0.007}$ & $\mathbf{-0.306}$ & $\mathbf{-0.299}$ \\
824	Threshold ($3\sigma$) & $+0.111$ & $-0.027$ & $+0.084$ \\
825	Perm.\ Granger       & $+0.039$ & $-0.180$ & $-0.141$ \\
826	Toda--Yamamoto       & $+0.150$ & $-0.069$ & $+0.082$ \\
827	\bottomrule
828	\end{tabular}
829	\end{table}
830	
831	
832	\FloatBarrier
833	\section{MMCT Weight Robustness Ablation}
834	\label{app:weight_robustness}
835	
836	PermG ranks first among directional methods under all four weighting schemes tested (equal, cap-5, cap-10, FPR-inverse cap-100), confirming the ranking is not an artifact of the weighting scheme.
837	Cap-10 and cap-100 yield identical values (consensus threshold saturates), and equal weighting still gives PermG the best combined Shapley ($-0.152$) among directional methods.
838	
839	\begin{table}[t]
840	\centering
841	\small
842	\caption{PermG combined Shapley ($\phi^{\text{comb}}$) under four weighting schemes. Rankings are invariant to weight choice.}
843	\label{tab:weight_robustness}
844	\begin{tabular}{lcccc}
845	\toprule
846	Method & Equal & Cap-5 & Cap-10 & FPR-inv \\
847	\midrule
848	PermG & $-0.152$ & $-0.148$ & $-0.141$ & $-0.141$ \\
849	DiffXCorr & $-0.285$ & $-0.291$ & $-0.299$ & $-0.299$ \\
850	Threshold & $+0.078$ & $+0.081$ & $+0.084$ & $+0.084$ \\
851	TY & $+0.088$ & $+0.084$ & $+0.082$ & $+0.082$ \\
852	NaiveXCorr & $+0.195$ & $+0.192$ & $+0.190$ & $+0.190$ \\
853	\bottomrule
854	\end{tabular}
855	\end{table}
856	
857	\paragraph{Interpretation.}
858	The FPR-inverse weighting scheme (\S\ref{sec:mmct}) penalizes high-FPR methods by assigning weight $w_k = 1/\max(\widehat{\mathrm{FPR}}_k, \epsilon)$.
859	Under this scheme, NaiveXCorr (FPR${=}94.4\%$) receives weight $w{=}1.06$, while PermG (FPR${=}6.7\%$) receives $w{=}14.9$---a $14{\times}$ differential.
860	Equal weighting gives all methods identical influence, which reduces PermG's advantage but does not change its ranking among directional methods.
861	The invariance across weighting schemes (Table~\ref{tab:weight_robustness}) confirms that PermG's superiority reflects genuine detection properties rather than favorable weighting.
862	
863	\paragraph{Per-pair contribution variability.}
864	Marginal contributions vary substantially across canary$\to$downstream pairs (Table~\ref{tab:shapley_per_pair}).
865	Token entropy$\to$distinct-1 produces the most consistent positive contribution across coalitions (std${=}0.021$), while ECE$\to$perplexity shows the highest variance (std${=}0.089$), reflecting the contemporaneous coupling issue (\S\ref{app:channel_effect_size}).
866	
867	\begin{table}[t]
868	\centering
869	\small
870	\caption{Shapley contribution by canary$\to$downstream pair (PermG, 6-pair basis). $\phi^{\text{FNR}}$ = FNR reduction (more negative = better). Std = standard deviation across all $2^4$ coalitions that include this pair.}
871	\label{tab:shapley_per_pair}
872	\begin{tabular}{lcc}
873	\toprule
874	Pair & Mean $\phi^{\text{FNR}}$ & Std \\
875	\midrule
876	Entropy$\to$Distinct-1 & $-0.042$ & 0.021 \\
877	Entropy$\to$Distinct-2 & $-0.038$ & 0.024 \\
878	ECE$\to$Distinct-1 & $-0.035$ & 0.031 \\
879	ECE$\to$Distinct-2 & $-0.031$ & 0.028 \\
880	Entropy$\to$PPL & $-0.002$ & 0.067 \\
881	ECE$\to$PPL & $-0.001$ & 0.089 \\
882	\bottomrule
883	\end{tabular}
884	\end{table}
885	
886	The four diversity-channel pairs collectively account for 96.2\% of PermG's total FNR reduction, while the two perplexity-channel pairs contribute only 3.8\%---consistent with the channel effect size analysis (\S\ref{app:channel_effect_size}) showing that perplexity channels lack the temporal lead structure required for Granger detection.
887	This concentration motivates a practical simplification: for deployment scenarios where computational cost matters, testing only the four diversity-channel pairs sacrifices less than 4\% of detection sensitivity while halving the multiple testing burden (4~tests instead of 8, reducing the FDR correction penalty).
888	
889	\paragraph{Coalition stability.}
890	PermG's marginal contribution is stable across coalition sizes: when added to a 1-method coalition, its average combined Shapley is $-0.138$ (SE${=}0.015$); when added to a 4-method coalition, $-0.144$ (SE${=}0.008$).
891	The near-zero variation ($\Delta{=}0.006$) confirms that PermG's value is complementary rather than redundant---it provides directional information that no other single method duplicates.
892	DiffXCorr shows the opposite pattern: its marginal contribution \emph{decreases} from $-0.312$ (1-method coalition) to $-0.281$ (4-method coalition) as it becomes partially redundant with NaiveXCorr (both test correlation, differing only in preprocessing).
893	
894	
895	\section{PermG FPR Independence Analysis}
896	\label{app:fpr_independence}
897	
898	Table~\ref{tab:null_fpr_methods} reports null-control FPR across nine seeds (54 pairs, 6-pair basis); a tenth seed (s51) yields 0~PermG FP, giving pooled 4/60${=}$6.7\% (CI $[1.8\%, 16.2\%]$).
899	All four FP occur in te$\to$distinct pairs in seeds~45/50 (8/10 seeds yield 0~FP).
900	$K{\geq}3$ consensus produces 6/60 FP (10.0\%), of which PermG contributes to only 2.
901	At $T{=}15$, PermG FPR drops to 0/12 (0\%).
902	
903	\begin{figure}[t]
904	\centering
905	\includegraphics[width=\columnwidth]{figures/fig_fpr_sensitivity.pdf}
906	\caption{Per-seed FPR distribution across detection methods (Pythia-410M, $\alpha{=}0.0$, 10~seeds). Each dot represents one seed's FPR; boxplots show inter-seed variability. PermG FPR concentrates near 0\% (8/10 seeds yield 0 false positives) with two outlier seeds (s45, s50) driving the aggregate 6.7\%. NaiveXCorr exhibits uniformly high FPR (${\geq}83\%$) across all seeds.}
907	\label{fig:fpr_sensitivity}
908	\end{figure}
909	
910	\begin{figure}[t]
911	\centering
912	\includegraphics[width=\columnwidth]{figures/fig_null_fpr_diagnostic.pdf}
913	\caption{Null-control diagnostic: PermG $p$-value distributions under null ($\alpha{=}0.0$) across 10~seeds. Most seeds show $p$-values uniformly distributed above 0.05 (expected under the null); seeds~45 and 50 exhibit a cluster of low $p$-values in token-entropy$\to$distinct pairs, suggesting occasional null-condition coupling that does not generalize across seeds.}
914	\label{fig:null_fpr_diagnostic}
915	\end{figure}
916	
917	\begin{table}[t]
918	\centering
919	\small
920	\caption{Null-control FPR by method ($\alpha{=}0.0$, BH-FDR $q{=}0.05$). $^\ddagger$PermG: 10~seeds, 60~pairs; other methods: 9~seeds, 54~pairs (s51 6-pair breakdown pending).}
921	\label{tab:null_fpr_methods}
922	\resizebox{\columnwidth}{!}{%
923	\begin{tabular}{llrr}
924	\toprule
925	Method & Criterion & Rejections & FPR (\%) \\
926	\midrule
927	\textbf{Perm.\ Granger}$^\ddagger$ & \textbf{BH-FDR} & \textbf{4/60} & \textbf{6.7} \\
928	Diff.\ XCorr$^\dagger$ & BH-FDR & 8/54 & 14.8 \\
929	Threshold & $3\sigma$ (det.) & 13/54 & 24.1 \\
930	Toda--Yamamoto & BH-FDR & 18/54 & 33.3 \\
931	Naive XCorr & uncorr. & 51/54 & 94.4 \\
932	\bottomrule
933	\multicolumn{4}{l}{\footnotesize $^\dagger$Bidirectional; cannot separate forward from reverse.} \\
934	\end{tabular}}
935	\end{table}
936	
937	\subsection{Per-Seed FPR Breakdown}
938	\label{app:per_seed_fpr}
939	
940	Table~\ref{tab:per_seed_fpr_8pair} reports FPR on a per-seed, per-method basis for the original 3-seed cohort (s42, s43, s44; 8-pair basis including MAUVE), while Table~\ref{tab:per_seed_fpr_6pair} extends to the 6-seed expansion (s45--s51; 6-pair basis excluding MAUVE).
941	
942	\begin{figure}[t]
943	\centering
944	\includegraphics[width=\columnwidth]{figures/fig_bootstrap_fpr.pdf}
945	\caption{Bootstrap confidence intervals for FPR estimates (10{,}000 resamples, 10~seeds). PermG's 95\% CI ($[1.8\%, 16.2\%]$) is the tightest among directional methods; the upper bound remains below Threshold's point estimate (27.8\%). The bootstrap distribution for NaiveXCorr is sharply peaked near 90\%, confirming that its high FPR is systematic rather than driven by individual seed outliers.}
946	\label{fig:bootstrap_fpr}
947	\end{figure}
948	
949	\begin{table}[t]
950	\centering
951	\small
952	\caption{Per-seed FPR (8-pair basis, $\alpha{=}0.0$, Pythia-410M, seeds 42--44). PermG achieves 0/8 on all three seeds; NaiveXCorr ${\geq}7/8$ on all.}
953	\label{tab:per_seed_fpr_8pair}
954	\resizebox{\columnwidth}{!}{%
955	\begin{tabular}{lccccc}
956	\toprule
957	Seed & PermG & DiffXCorr & Threshold & TY & NaiveXCorr \\
958	\midrule
959	42 & 0/8 & 4/8 & 3/8 & 2/8 & 8/8 \\
960	43 & 0/8 & 2/8 & 1/8 & 2/8 & 7/8 \\
961	44 & 0/8 & 3/8 & 2/8 & 0/8 & 7/8 \\
962	\midrule
963	Pooled & 0.0\% & 37.5\% & 25.0\% & 16.7\% & 91.7\% \\
964	\bottomrule
965	\end{tabular}}
966	\end{table}
967	
968	\begin{table}[t]
969	\centering
970	\small
971	\caption{Per-seed PermG FPR (6-pair basis, $\alpha{=}0.0$, seeds 45--51). Two seeds (s45, s50) contribute all 4 false positives; remaining seeds yield 0/6.}
972	\label{tab:per_seed_fpr_6pair}
973	\begin{tabular}{lccl}
974	\toprule
975	Seed & PermG fwd & $K{\geq}3$ & Affected pairs \\
976	\midrule
977	45 & 2/6 & 0/6 & te$\to$d1, te$\to$d2 \\
978	46 & 0/6 & 1/6 & --- \\
979	47 & 0/6 & 0/6 & --- \\
980	48 & 0/6 & 0/6 & --- \\
981	49 & 0/6 & 0/6 & --- \\
982	50 & 2/6 & 2/6 & te$\to$d1, te$\to$d2 \\
983	51 & 0/6 & 0/6 & --- \\
984	\bottomrule
985	\end{tabular}
986	\end{table}
987	
988	The concentration of false positives in token-entropy$\to$distinct pairs at seeds~45 and 50 suggests stochastic null-condition coupling in these specific initializations rather than a systematic calibration failure.
989	$K{\geq}3$ consensus FPR on the 6-pair basis is 6/36${=}$16.7\%; of these 6 false positives, only 2 include PermG (both at s50)---the remaining 4 are driven by high-FPR methods (NaiveXCorr $+$ Threshold $+$ TY) reaching consensus without PermG participation.
990	This decomposition clarifies why $K{\geq}3$ FPR exceeds standalone PermG FPR: the consensus mechanism aggregates false positives from multiple methods rather than filtering them.
991	
992	\FloatBarrier
993	\section{Sigmoid Transition Shape}
994	\label{app:sigmoid_shape}
995	
996	Sigmoid regression on the original 13-point $T{=}10$ grid yields $\alpha_c = 0.483 \pm 0.006$ but $k = 478 \pm 475$ ($\mathrm{SE}(k) \approx k$), indicating that the coarse grid cannot constrain the transition shape.
997	Dense $\alpha$ sampling (17~values at $T{=}10$) resolves this ambiguity: formal likelihood-ratio testing strongly favors a smooth sigmoid over a literal step function ($\Delta\mathrm{AIC}{=}-110$), with fitted steepness $k{=}15.7$ (95\% CI $[9.4, 28.2]$).
998	The transition is steep but finite-width, not a literal discontinuity.
999	This observed steepness exceeds what smooth signal models predict: VAR(1) simulations under H0 (linear, $k{=}6.1$) and H0$'$ (concave, $k{=}4.9$) produce onset sigmoids with $k{=}4.9$--$6.1$ (\S\ref{app:power_sim}), yielding steepness ratios $k_{\mathrm{obs}} / k_{\mathrm{H0}} \approx 2.6$--$3.2$ (CI lower bound ratio ${\approx}2$).
1000	
1001	\paragraph{Combined $T{=}10 + T{=}20$ fit.}
1002	Fitting a single sigmoid to both $T$ values yields $k{=}279.3$ (SE${=}527.6$), $\alpha_c{=}0.451$, $y_{\max}{=}0.75$, AIC${=}79.86$.
1003	The 90\% transition width narrows from $[0.478, 0.487]$ (width$=0.0092$) at $T{=}10$ alone to $[0.443, 0.459]$ (width$=0.0158$) in the combined fit---a leftward shift of $\alpha_c$ by $0.031$ reflecting the $T{=}20$ data's detection at $\alpha{=}0.45$.
1004	The combined $k$ drops by 41.6\% relative to $T{=}10$-only, confirming that the transition appears broader when viewed across observation lengths (different $T$ values yield different effective detection thresholds).
1005	We ultimately do not report the combined sigmoid in the main text because $\alpha{=}0.45$ yields contradictory counts (0/8 at $T{=}10$ vs.\ 5/8 at $T{=}20$), reflecting genuine power dependence rather than a single dose-response curve.
1006	
1007	\paragraph{Alternative functional forms.}
1008	Probit and sigmoid fits produce identical AIC (32.99 at $T{=}10$, 79.86 combined), as expected given that both are sigmoidal CDFs differing only in tail behavior.
1009	A generalized logistic ($+1$ parameter for asymmetry $\nu$) adds $+2$ AIC penalty without improving fit, confirming that a symmetric sigmoid is sufficient.
1010	
1011	\paragraph{Transition width characterization.}
1012	The 90\% transition width---the $\alpha$ range over which detection probability rises from 5\% to 95\%---quantifies the sharpness of the regime boundary (Table~\ref{tab:transition_width}).
1013	
1014	\begin{table}[t]
1015	\centering
1016	\small
1017	\caption{Sigmoid transition width (90\% range) by observation length and signal model. Narrower width indicates sharper regime onset.}
1018	\label{tab:transition_width}
1019	\begin{tabular}{lccc}
1020	\toprule
1021	Setting & Width ($\Delta\alpha$) & $\alpha_c$ & $k$ \\
1022	\midrule
1023	$T{=}10$ observed (13-pt) & 0.009 & 0.483 & 478 \\
1024	$T{=}10$ dense (17-pt) & 0.028 & 0.481 & 15.7 \\
1025	$T{=}10{+}20$ combined & 0.016 & 0.451 & 279 \\
1026	H0 linear simulation & 0.072 & 0.507 & 6.1 \\
1027	H0$'$ concave simulation & 0.090 & 0.521 & 4.9 \\
1028	\bottomrule
1029	\end{tabular}
1030	\end{table}
1031	
1032	The dense-sampling transition width ($\Delta\alpha{=}0.028$, corresponding to $\alpha \in [0.467, 0.495]$) is ${\sim}3{\times}$ narrower than smooth-model predictions (0.072--0.090), confirming the anomalous sharpness.
1033	In practical terms, a difference of $\Delta\alpha{=}0.03$ in contamination fraction determines whether detection is impossible (0\%) or reliable (75\%)---this represents approximately 150 additional synthetic samples out of 5{,}000.
1034	The narrow transition has implications for monitoring systems: slight increases in synthetic data fraction near the boundary produce large changes in detectability, creating a ``cliff effect'' where monitoring transitions from false security to reliable alarm with minimal change in the underlying contamination level.
1035	A system operating at $\alpha{=}0.47$ (undetectable) and drifting to $\alpha{=}0.50$ (detectable) would experience an abrupt shift from zero alarm rate to 75\% alarm rate---a three percentage-point contamination increase produces a qualitative change in monitoring behavior.
1036	
1037	\begin{figure}[t]
1038	\centering
1039	\includegraphics[width=\columnwidth]{figures/differencing_dmax.pdf}
1040	\caption{First-differencing order selection diagnostic. The optimal differencing order $d_{\max}$ is evaluated via ADF test statistics across all canary$\to$downstream series at $\alpha{=}1.0$. First-order differencing ($d{=}1$) achieves stationarity in all series (ADF $p{<}0.05$), confirming that higher-order differencing is unnecessary and would incur additional power loss.}
1041	\label{fig:differencing_dmax}
1042	\end{figure}
1043	
1044	\section{Intervention Threshold Sensitivity}
1045	\label{app:intervention_sensitivity}
1046	
1047	At $\alpha{=}1.0$, all five tested thresholds (5\%--25\%) trigger at generation~1 (entropy drop 40.7\%$\gg$threshold), producing identical outcomes (peak PPL 57.0, final PPL 21.3).
1048	The safe operating band is $[10\%, 22\%]$: below 7.5\% triggers false alarms on $\alpha{=}0.0$ drift; above 22.4\% misses $\alpha{=}0.50$.
1049	
1050	\paragraph{Cross-seed and cross-scale replication.}
1051	The predictive cessation result replicates on seed~43 (bf16 precision): trigger at gen-1 with a milder entropy drop ($-22.5\%$ vs.\ $-40.7\%$ in fp32), peak PPL${=}24.65$ (lower due to bf16 dampening).
1052	On Pythia-1.4B (s42, fp32): trigger at gen-1, entropy drop $-51.9\%$ ($2.946 \to 1.418$), peak PPL spike from $19.68$ to $65.37$, recovery by gen-2 (PPL${=}17.44$), final PPL at gen-10${=}17.6$.
1053	ECE follows the same pattern: $0.007 \to 0.281$ at the spike, recovering to $0.017$ post-intervention.
1054	
1055	\paragraph{Alpha=0.75 predictive intervention.}
1056	At $\alpha{=}0.75$ (fp32, v4 pipeline), predictive cessation also triggers at gen-1, with recovery by gen-2.
1057	Post-intervention PermG detection reaches 6/8 forward, $K{\geq}4{=}6/8$, confirming that the intervention preserves the statistical detection signal while preventing perplexity degradation.
1058	Entropy drift post-intervention is only $-5.7\%$ over 10~generations (vs.\ $-27.6\%$ without intervention), consistent with the generation-1 trigger halting the collapse cascade before downstream metrics respond.
1059	
1060	\paragraph{No-intervention baseline comparison.}
1061	Without intervention at $\alpha{=}1.0$: gen-10 PPL${=}1003.73$, distinct-1${=}0.0704$.
1062	With predictive cessation: gen-10 PPL${=}21.29$, distinct-1${=}0.0844$ ($+19.9\%$ higher diversity).
1063	The intervention reduces peak perplexity by 64\% ($56.99$ vs.\ $157.09$ reactive) and preserves substantially more lexical diversity, though neither intervention strategy fully prevents the initial diversity loss at gen-1.
1064	
1065	\begin{figure}[t]
1066	\centering
1067	\includegraphics[width=\columnwidth]{figures/fig_cusum_monitoring.pdf}
1068	\caption{CUSUM sequential monitoring versus calibrated threshold (Pythia-410M, $\alpha{=}1.0$). Both methods trigger at generation~1 because the entropy drop ($|\Delta x|{>}0.7$) greatly exceeds null variability ($\sigma_0{\approx}0.03$). CUSUM's cumulative memory provides no advantage when the initial signal dominates. The shaded region marks the safe operating band $[10\%, 22\%]$ for threshold-based detection.}
1069	\label{fig:cusum_monitoring}
1070	\end{figure}
1071	
1072	
1073	\section{Channel Effect Size Analysis}
1074	\label{app:channel_effect_size}
1075	
1076	First-differencing retains comparable $|r|$ for both diversity (0.952) and perplexity (1.00) channels, ruling out selective power loss.
1077	The Granger $F$-statistic asymmetry ($20$--$28{\times}$ higher for diversity) reflects temporal structure: diversity channels peak at canary-leading lags (81\% at lag${<}0$, median $-1$), while perplexity peaks at lag${=}0$ (contemporaneous co-movement).
1078	Granger tests correctly assign low $F$ to contemporaneous relationships.
1079	
1080	\paragraph{Lag structure decomposition.}
1081	Table~\ref{tab:lag_structure} reports the cross-correlation peak lag for each canary$\to$downstream channel, illustrating the structural difference that drives Granger detectability.
1082	
1083	\begin{table}[t]
1084	\centering
1085	\small
1086	\caption{Cross-correlation peak lag by channel (Pythia-410M, $\alpha{=}1.0$, 4~seeds). Negative lag = canary leads. Diversity channels show consistent canary-leading structure; perplexity channels peak at lag~0.}
1087	\label{tab:lag_structure}
1088	\begin{tabular}{lccl}
1089	\toprule
1090	Channel & Peak lag & $|r|$ at peak & Structure \\
1091	\midrule
1092	Entropy$\to$Dist-1 & $-1$ & 0.96 & canary leads \\
1093	Entropy$\to$Dist-2 & $-1$ & 0.95 & canary leads \\
1094	ECE$\to$Dist-1 & $-1$ & 0.94 & canary leads \\
1095	ECE$\to$Dist-2 & $-1$ & 0.93 & canary leads \\
1096	Entropy$\to$PPL & $0$ & 0.99 & contemporaneous \\
1097	ECE$\to$PPL & $0$ & 0.98 & contemporaneous \\
1098	\bottomrule
1099	\end{tabular}
1100	\end{table}
1101	
1102	The contemporaneous co-movement of canary$\to$perplexity explains why Granger tests fail ($F{\approx}0$, $p{=}0.99$ after differencing): perplexity and entropy respond to the same underlying distributional shift at the same time step, so neither provides predictive improvement over the other's own history.
1103	This is not a limitation of the test but a correct inference---perplexity is not ``downstream'' of entropy in the temporal sense.
1104	
1105	\paragraph{Fisher Z-transform comparison.}
1106	To formally test whether diversity and perplexity channels differ in lagged correlation magnitude, we apply the Fisher Z-transform to peak cross-correlation coefficients (Table~\ref{tab:fisher_z}).
1107	
1108	\begin{table}[t]
1109	\centering
1110	\small
1111	\caption{Fisher Z-transform comparison of channel correlations (Pythia-410M, $\alpha{=}1.0$, 4~seeds). $Z_{\text{diff}}$ tests whether lagged ($\ell{=}{-}1$) correlation differs between diversity and perplexity channels.}
1112	\label{tab:fisher_z}
1113	\begin{tabular}{lcccc}
1114	\toprule
1115	Comparison & $r_{\text{div}}$ & $r_{\text{ppl}}$ & $Z_{\text{diff}}$ & $p$ \\
1116	\midrule
1117	\emph{Lag${=}0$ (contemp.)} \\
1118	\quad Entropy$\to$ & 0.955 & 0.990 & $-2.13$ & 0.033 \\
1119	\quad ECE$\to$ & 0.935 & 0.980 & $-2.41$ & 0.016 \\
1120	\midrule
1121	\emph{Lag${=}{-}1$ (canary leads)} \\
1122	\quad Entropy$\to$ & 0.952 & 0.812 & $+3.67$ & ${<}0.001$ \\
1123	\quad ECE$\to$ & 0.941 & 0.795 & $+3.89$ & ${<}0.001$ \\
1124	\bottomrule
1125	\end{tabular}
1126	\end{table}
1127	
1128	At lag${=}0$ (contemporaneous), perplexity channels show \emph{higher} correlation than diversity channels ($r{=}0.990$ vs.\ $0.955$, $Z{=}-2.13$, $p{=}0.033$), reflecting the synchronous entropy-perplexity coupling.
1129	At lag${=}-1$ (canary leading by one generation), the pattern reverses decisively: diversity channels achieve $r{=}0.952$ vs.\ perplexity's $r{=}0.812$ ($Z{=}3.67$, $p{<}0.001$).
1130	This reversal explains the Granger $F$-statistic asymmetry: perplexity channels do not have weaker coupling overall, but their coupling is \emph{contemporaneous rather than lagged}.
1131	A Granger test measures whether \emph{past} values of $X$ predict \emph{current} $Y$ beyond $Y$'s own history; contemporaneous coupling produces zero improvement, hence $F \approx 0$.
1132	The Fisher Z analysis confirms that the canary$\to$perplexity non-detection is a correct statistical inference about temporal structure rather than a power limitation.
1133	
1134	\begin{figure}[t]
1135	\centering
1136	\includegraphics[width=\columnwidth]{figures/fig_channel_effect.pdf}
1137	\caption{Channel effect size comparison: Granger $F$-statistic for canary$\to$diversity versus canary$\to$perplexity channels (Pythia-410M, $\alpha{=}1.0$, 4~seeds). Diversity channels produce $20$--$28{\times}$ higher $F$-statistics than perplexity channels, reflecting the temporal structure difference: diversity correlations peak at canary-leading lags (81\% at lag${<}0$), while perplexity correlations are contemporaneous (50\% at lag${=}0$).}
1138	\label{fig:channel_effect}
1139	\end{figure}
1140	
1141	
1142	\section{Mutual Information and Partial Correlation}
1143	\label{app:mi_analysis}
1144	
1145	Gaussian MI lower bound ($\hat{I}_G = -\frac{1}{2}\log_2(1{-}r^2)$) between token entropy and distinct-$n$ remains positive throughout the blind zone (0.010--0.141~bits), confirming coupling exists below PermG's detection threshold.
1146	No discontinuity at $\alpha_c$: detection onset reflects power accumulation, not an information transition.
1147	
1148	\paragraph{MI across the blind zone.}
1149	Table~\ref{tab:mi_blind} reports Gaussian MI between token entropy and distinct-1 at each contamination level below $\alpha_c$.
1150	MI increases monotonically with $\alpha$, confirming that the entropy--diversity coupling strengthens continuously across the blind$\to$detection boundary.
1151	The detection onset at $\alpha_c$ therefore reflects a power threshold (sufficient signal-to-noise for PermG to detect the coupling) rather than a qualitative change in the underlying statistical relationship.
1152	
1153	\begin{table}[t]
1154	\centering
1155	\small
1156	\caption{Gaussian MI lower bound between token entropy and distinct-1 across the blind zone (Pythia-410M, $T{=}10$, seed~42).}
1157	\label{tab:mi_blind}
1158	\begin{tabular}{lcc}
1159	\toprule
1160	$\alpha$ & $\hat{I}_G$ (bits) & PermG \\
1161	\midrule
1162	0.00 & 0.010 & 0/8 \\
1163	0.10 & 0.025 & 0/8 \\
1164	0.25 & 0.048 & 0/8 \\
1165	0.45 & 0.141 & 0/8 \\
1166	0.50 & 0.312 & 6/8 \\
1167	\bottomrule
1168	\end{tabular}
1169	\end{table}
1170	
1171	\subsection{Partial Correlation Analysis}
1172	\label{app:partial_corr}
1173	
1174	Partial correlations controlling for generation number (Table~\ref{tab:partial_corr}) show that contemporaneous associations drop after trend removal ($\bar{|r|}$: $0.590{\to}0.381$ at $\alpha{=}0.50$), while lagged correlations \emph{strengthen} ($0.759{\to}0.841$), with 35/36 detection-condition pairs retaining significance.
1175	
1176	\begin{table}[t]
1177	\centering
1178	\small
1179	\caption{Partial correlation controlling for generation. Lagged partial $|r|$ increases after trend removal, confirming genuine temporal precedence.}
1180	\label{tab:partial_corr}
1181	\resizebox{\columnwidth}{!}{%
1182	\begin{tabular}{@{}l cc cc cc cc@{}}
1183	\toprule
1184	& \multicolumn{4}{c}{Contemporaneous} & \multicolumn{4}{c}{Lagged (canary$_{t-1}$)} \\
1185	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
1186	& \multicolumn{2}{c}{Zero-order} & \multicolumn{2}{c}{Partial} & \multicolumn{2}{c}{Zero-order} & \multicolumn{2}{c}{Partial} \\
1187	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7} \cmidrule(lr){8-9}
1188	$\alpha$ & $\bar{|r|}$ & Sig. & $\bar{|r|}$ & Sig. & $\bar{|r|}$ & Sig. & $\bar{|r|}$ & Sig. \\
1189	\midrule
1190	0.00 & 0.414 & 3/18 & 0.323 & 0/18 & 0.563 & 8/18 & 0.524 & 9/18 \\
1191	0.50 & 0.590 & 9/18 & 0.381 & 2/18 & 0.759 & 12/18 & 0.841 & 17/18 \\
1192	0.75 & 0.636 & 9/18 & 0.521 & 3/18 & 0.831 & 17/18 & 0.913 & 18/18 \\
1193	\bottomrule
1194	\end{tabular}}
1195	\end{table}
1196	
1197	\begin{figure}[t]
1198	\centering
1199	\includegraphics[width=\columnwidth]{figures/fig_partial_correlation.pdf}
1200	\caption{Partial correlation scatter plots for canary$\to$diversity pairs at $\alpha{=}0.75$ (Pythia-410M). Left: contemporaneous partial correlations drop after controlling for generation trend. Right: lagged partial correlations \emph{strengthen} after trend removal ($\bar{|r|}$: $0.831{\to}0.913$), confirming that the temporal precedence signal is not a shared-trend artifact.}
1201	\label{fig:partial_corr}
1202	\end{figure}
1203	
1204	\begin{figure}[t]
1205	\centering
1206	\includegraphics[width=\columnwidth]{figures/fig_partial_correlation_agg.pdf}
1207	\caption{Aggregated partial correlation analysis across contamination levels. Lagged canary$\to$diversity correlations increase monotonically with $\alpha$ (from $0.524$ at null to $0.913$ at $\alpha{=}0.75$), while contemporaneous correlations plateau. The growing gap between lagged and contemporaneous partial $|r|$ with increasing contamination indicates that the temporal lead signal strengthens with signal-to-noise ratio.}
1208	\label{fig:partial_corr_agg}
1209	\end{figure}
1210	
1211	\paragraph{Interpretation.}
1212	The partial correlation analysis serves two purposes:
1213	(1)~It confirms that the canary$\to$diversity temporal precedence is not driven by a shared trend (generation number): removing the linear trend \emph{strengthens} rather than eliminates the lagged association.
1214	(2)~It shows that the temporal signal grows with contamination level: at $\alpha{=}0.00$, lagged partial $|r|{=}0.524$ (marginal significance); at $\alpha{=}0.75$, lagged partial $|r|{=}0.913$ (universal significance, 18/18).
1215	This monotonic growth parallels the MI analysis and confirms that the blind-zone boundary reflects statistical power rather than a qualitative transition in the coupling structure.
1216	
1217	\paragraph{Null behavior.}
1218	At $\alpha{=}0.00$, 9/18 lagged pairs reach significance despite no synthetic contamination, reflecting fine-tuning drift coupling: both entropy and diversity decline during pure fine-tuning (Table~\ref{tab:drift_summary}), creating a weak temporal association.
1219	These null-condition correlations are substantially weaker than treatment-condition correlations ($0.524$ vs.\ $0.913$), and the 9/18 significance rate is consistent with the expected false positive rate under weak coupling (mid-range $p$-values cluster near the significance boundary).
1220	
1221	
1222	\section{Moment Cascade Analysis}
1223	\label{app:moment_cascade}
1224	
1225	Onset (5\% threshold) occurs at generation~1 for entropy in all 6 conditions and at generation~2 for distinct-$n$ in all 18 pairwise comparisons (Table~\ref{tab:moment_cascade}; Figure~\ref{fig:cascade_onset}, main text).
1226	
1227	\begin{table}[t]
1228	\centering
1229	\small
1230	\caption{Degradation onset generation (5\% threshold) by metric and condition (Pythia-410M, WikiText, fp32). Token entropy reaches onset at generation~1 in all non-null conditions; distinct-$n$ metrics follow at generation~2.}
1231	\label{tab:moment_cascade}
1232	\resizebox{\columnwidth}{!}{%
1233	\begin{tabular}{llcccccc}
1234	\toprule
1235	Seed & $\alpha$ & Entropy & Dist-1 & Dist-2 & Dist-3 & ECE & PPL \\
1236	\midrule
1237	42 & 0.10 & 1 & 2 & 2 & 2 & 2 & --- \\
1238	42 & 0.50 & 1 & 2 & 2 & 2 & 1 & 4 \\
1239	42 & 0.75 & 1 & 2 & 2 & 2 & 1 & 1 \\
1240	43 & 0.25 & 1 & 2 & 2 & 2 & 4 & --- \\
1241	43 & 0.50 & 1 & 2 & 2 & 2 & 1 & 4 \\
1242	43 & 0.75 & 1 & 2 & 2 & 2 & 1 & 1 \\
1243	\bottomrule
1244	\multicolumn{8}{l}{\footnotesize ---: onset not reached within $T{=}10$ generations.} \\
1245	\end{tabular}}
1246	\end{table}
1247	
1248	
1249	ECE shows onset at generation~1 at $\alpha{\geq}0.50$; perplexity never reaches 5\% onset at low contamination ($\alpha{\leq}0.25$).
1250	
1251	\paragraph{Onset threshold sensitivity.}
1252	Table~\ref{tab:onset_threshold_sensitivity} examines how the cascade ordering result depends on the choice of onset threshold (5\%, 10\%, 15\%, 20\%).
1253	
1254	\begin{table}[t]
1255	\centering
1256	\small
1257	\caption{Cascade ordering $t_H \leq t_D$ validity as a function of onset threshold (Pythia-410M, 6 conditions, $\alpha{\geq}0.10$).}
1258	\label{tab:onset_threshold_sensitivity}
1259	\begin{tabular}{lccc}
1260	\toprule
1261	Threshold & $t_H \leq t_D$ & $t_H = t_D$ & $t_H > t_D$ \\
1262	\midrule
1263	5\% & 6/6 & 0/6 & 0/6 \\
1264	10\% & 6/6 & 0/6 & 0/6 \\
1265	15\% & 5/6 & 1/6 & 0/6 \\
1266	20\% & 4/6 & 2/6 & 0/6 \\
1267	\bottomrule
1268	\end{tabular}
1269	\end{table}
1270	
1271	At all thresholds, the ordering $t_H \leq t_D$ is never violated ($t_H > t_D$ in 0/24 cells).
1272	At the strictest threshold (5\%), entropy precedes diversity by exactly one generation in all 6 conditions.
1273	At relaxed thresholds (${\geq}15\%$), some conditions show simultaneous onset ($t_H = t_D$), because the larger threshold absorbs the diversity lag---consistent with the margin condition in Observation~\ref{prop:div_lag}.
1274	
1275	\paragraph{MAUVE cascade position.}
1276	MAUVE~\citep{pillutla2021mauve} onset occurs at generation~2--3, consistently after distinct-$n$ onset (gen-2), establishing a three-phase cascade: $\{H, \mathrm{ECE}\} \to \mathrm{Dist}\text{-}n \to \mathrm{MAUVE}$.
1277	MAUVE's later onset reflects its distributional-comparison nature: it measures the divergence between generated and reference text distributions, which requires substantial lexical collapse before the divergence exceeds the detection threshold.
1278	At $\alpha{=}1.0$, MAUVE floor saturation (${\sim}0.033$) occurs by gen-3--4, after which it becomes uninformative (constant series).
1279	
1280	\paragraph{Perplexity irregularity.}
1281	Perplexity onset is condition-dependent rather than cascade-ordered: at $\alpha{=}0.50$ (s42), PPL onset occurs at gen-4 (delayed relative to entropy gen-1 and diversity gen-2); at $\alpha{=}0.75$, PPL onset is gen-1 (contemporaneous with entropy).
1282	This irregularity is consistent with the first-differencing result: PPL is not temporally downstream of entropy in the Granger sense.
1283	Instead, PPL responds to a different aspect of collapse (cross-entropy on held-out data) that can accelerate or decelerate independently of the entropy-diversity cascade.
1284	
1285	
1286	\subsection{Discretized Entropy Robustness Test}
1287	\label{app:discretized_entropy}
1288	
1289	A potential concern is that PermG may exploit the continuous resolution of token entropy relative to the discrete-valued distinct-$n$ metrics, producing spurious Granger precedence.
1290	We test this by binning continuous entropy into discrete levels and re-running the permutation Granger test.
1291	
1292	For each of 7~experiments at $\alpha{=}1.0$ (spanning Pythia-410M, GPT-2-medium, OPT-1.3B, and Pythia-1.4B), we discretize the entropy time series using equal-width and equal-frequency binning at 5, 10, 15, and 20~bins, then apply the same PermG test (5{,}000 permutations, first-differenced, max lag~1) on binned entropy$\to$distinct-1.
1293	
1294	\begin{table}[t]
1295	\centering
1296	\small
1297	\caption{Discretized entropy Granger test: number of experiments (out of 7) with FDR-significant entropy$\to$distinct-1 at each binning resolution and method. Continuous baseline: 7/7.}
1298	\label{tab:discretized_entropy}
1299	\begin{tabular}{@{}lcc@{}}
1300	\toprule
1301	Bins & Equal-width & Equal-freq \\
1302	\midrule
1303	20 & 7/7 & 7/7 \\
1304	15 & 6/7 & 7/7 \\
1305	10 & 5/7 & 1/7 \\
1306	5  & 3/7 & 0/7 \\
1307	\bottomrule
1308	\end{tabular}
1309	\end{table}
1310	
1311	At ${\geq}15$~bins, Granger precedence is largely preserved (6--7/7) regardless of binning method (Table~\ref{tab:discretized_entropy}).
1312	Signal degradation occurs only at extreme coarsening (${\leq}10$~bins), where equal-frequency binning is particularly destructive because entropy trajectories are right-skewed (sharp generation~0--2 drop followed by a plateau); equal-frequency bins compress the informative early decline into a single bin.
1313	The Pythia-410M reference case retains significance down to 5~equal-width bins ($p{=}0.035$) but loses it under 5~equal-frequency bins ($p{=}0.700$).
1314	
1315	These results confirm that the temporal precedence finding is not solely attributable to continuous measurement resolution: even moderate discretization (${\geq}15$~levels, well below the effective resolution of distinct-$n$) preserves the signal across all tested architectures, though extreme quantization (${\leq}5$~bins) can eliminate it.
1316	
1317	
1318	\FloatBarrier
1319	\section{Cascade Ordering Theory: Derivations}
1320	\label{app:cascade_theory}
1321	
1322	This section provides the full derivations for Observation~\ref{thm:entropy_leads} and Observation~\ref{prop:div_lag} from \S\ref{sec:cascade}, plus supporting results.
1323	
1324	\begin{assumption}[Mode Amplification]\label{ass:mode_amp}
1325	The training map $\mathcal{T}$ redistributes probability mass from low-probability to high-probability tokens: there exists a threshold $\bar{p}$ such that $\mathcal{T}(p)_i > p_i \Rightarrow p_i \geq \bar{p}$ and $\mathcal{T}(p)_j < p_j \Rightarrow p_j \leq \bar{p}$.
1326	\end{assumption}
1327	
1328	This captures the standard finite-capacity approximation effect: MLE on finite samples from a peaked distribution amplifies modes and suppresses the tail~\citep{shumailov2024curse,dohmatob2024tale}.
1329	
1330	\begin{proposition}[Entropy is a first-order indicator]\label{prop:entropy_first}
1331	Let $p \in \Delta^{V-1}$ and $\delta = \alpha(\mathcal{T}(p) - p)$ be a mode-amplifying perturbation with $\sum_i \delta_i = 0$. Then $\Delta H = H(p+\delta) - H(p) = -\sum_i \delta_i \log p_i + O(\|\delta\|^2) < 0$.
1332	\end{proposition}
1333	
1334	\begin{proof}
1335	Taylor-expanding $H$ around $p$:
1336	$H(p+\delta) = H(p) - \sum_i \delta_i \log p_i - \sum_i \delta_i - \frac{1}{2}\sum_i \delta_i^2/p_i + O(\|\delta\|^3)$.
1337	Since $\sum_i \delta_i = 0$: $\Delta H = -\sum_i \delta_i \log p_i - \frac{1}{2}\sum_i \delta_i^2/p_i + O(\|\delta\|^3)$.
1338	Under mode amplification, tokens gaining mass ($\delta_i > 0$) have $p_i \geq \bar{p}$ (hence $\log p_i \geq \log \bar{p}$) and tokens losing mass ($\delta_j < 0$) have $p_j \leq \bar{p}$ (hence $\log p_j \leq \log \bar{p}$).
1339	Writing $m = \sum_{i:\delta_i > 0} \delta_i$: $-\sum_i \delta_i \log p_i = -m[\overline{\log p}^{+} - \overline{\log p}^{-}] < 0$, where $\overline{\log p}^{\pm}$ are the $|\delta|$-weighted means over gaining/losing tokens.
1340	The second-order Fisher information term $-\frac{1}{2}\sum_i \delta_i^2/p_i$ is always negative, reinforcing the decrease.
1341	\end{proof}
1342	
1343	\begin{proposition}[Diversity is a threshold indicator]\label{prop:div_threshold}
1344	Define the $\epsilon$-effective support $S_\epsilon(p) = |\{i \in [V]: p_i > \epsilon\}|$, where $\epsilon \approx c/N$ is the generation threshold for sample size $N$.
1345	Under the same perturbation $\delta$: $\Delta S_\epsilon = -|\{i: p_i > \epsilon \text{ and } p_i + \delta_i \leq \epsilon\}|$.
1346	This equals zero whenever $\|\delta\|_\infty < \gamma(p,\epsilon) := \min_{i: p_i > \epsilon}(p_i - \epsilon)$.
1347	\end{proposition}
1348	
1349	\begin{proof}
1350	Token $i$ exits the effective support iff $p_i > \epsilon$ and $p_i + \delta_i \leq \epsilon$, requiring $|\delta_i| \geq p_i - \epsilon$.
1351	If $\|\delta\|_\infty < \gamma$, no token satisfies this condition.
1352	\end{proof}
1353	
1354	\medskip
1355	\noindent\textbf{Derivations from the propositions above.}
1356	
1357	\paragraph{Derivation of Observation~\ref{thm:entropy_leads}.}
1358	\emph{Part (a):} Take any mode-amplifying $\delta$ with $\|\delta\|_\infty < \gamma(p,\epsilon)$.
1359	By Proposition~\ref{prop:div_threshold}, $\Delta S_\epsilon = 0$.
1360	By Proposition~\ref{prop:entropy_first}, $\Delta H < 0$.
1361	Such $\delta$ exists for all $\alpha < \gamma / \max_i |\mathcal{T}(p)_i - p_i|$.
1362	\emph{Part (b):} If $\Delta S_\epsilon < 0$, some token $k$ has $p_k > \epsilon$ but $p_k + \delta_k \leq \epsilon$, so $\delta_k < 0$.
1363	Under mode amplification, this implies $p_k \leq \bar{p}$; the total mass transferred to high-probability tokens ensures $\overline{\log p}^+ > \overline{\log p}^-$.
1364	By Proposition~\ref{prop:entropy_first}, $\Delta H < 0$. $\square$
1365	
1366	\paragraph{Derivation of Observation~\ref{prop:div_lag}.}
1367	By the margin condition, at every generation $s \leq t_H$ the perturbation norm $\alpha\|\mathcal{T}(p_s) - p_s\|_\infty$ is less than $\gamma(p_s, \epsilon)$.
1368	By Proposition~\ref{prop:div_threshold}, no token exits the effective support at any $s \leq t_H$, so $\Delta S_\epsilon = 0$ for all $s \leq t_H$.
1369	Since time is discrete, $t_D \geq t_H + 1$. $\square$
1370	
1371	\medskip
1372	\noindent\textbf{ECE co-movement and empirical validation.}
1373	
1374	\paragraph{ECE co-movement (qualitative argument).}
1375	Under conditional mode amplification (peakier $q_\theta(\cdot|x)$ at each generation), per-token conditional entropy $h(x) = H(q_\theta(\cdot|x))$ decreases while confidence $c(x) = \max_y q_\theta(y|x) \geq \exp(-h(x))$ increases.
1376	Averaging: $\bar{H}_t$ decreases, $C_t$ increases.
1377	With accuracy approximately stationary in early collapse ($A_t \approx A_0$), $\Delta\mathrm{ECE} \approx \Delta C_t > 0$ whenever $\Delta\bar{H}_t < 0$.
1378	This argument establishes the direction of co-movement; the quantitative relationship depends on distribution geometry.
1379	$\bar{H}_t$ denotes mean conditional entropy $\mathbb{E}_{x \sim p_{\text{eval}}}[h(x)]$, which differs from the marginal entropy $H_t = -\sum_i p_t(i)\log p_t(i)$ used in Observation~\ref{thm:entropy_leads}; under mode amplification, both decrease monotonically, so the cascade ordering is consistent across both formulations.
1380	
1381	\paragraph{Empirical ECE drift across contamination levels.}
1382	ECE co-movement with entropy is monotonic across all tested $\alpha$ values (Table~\ref{tab:ece_drift}).
1383	At $\alpha{=}0.25$, ECE increases by $+79.2\%$ while entropy decreases by $-4.7\%$---the asymmetry in magnitude reflects ECE's nonlinear dependence on confidence via the $\max$ operator.
1384	At $\alpha{=}1.0$, ECE drift reaches $+3762$--$3821\%$ ($0.0108 \to 0.417$--$0.424$ across seeds), the largest proportional change among all tracked metrics.
1385	
1386	\begin{table}[t]
1387	\centering
1388	\small
1389	\caption{ECE drift across contamination levels (Pythia-410M, WikiText, fp32). ECE increases monotonically with $\alpha$, co-moving with entropy decrease.}
1390	\label{tab:ece_drift}
1391	\begin{tabular}{lccc}
1392	\toprule
1393	$\alpha$ & ECE gen-0 & ECE gen-10 & Drift (\%) \\
1394	\midrule
1395	0.00 & 0.0108 & $0.015{\pm}0.002$ & $+37.6{\pm}14$ \\
1396	0.25 & 0.0108 & $0.019{\pm}0.002$ & $+79.2{\pm}15.9$ \\
1397	0.50 & 0.0108 & $0.087{\pm}0.002$ & $+703{\pm}18$ \\
1398	0.60 & 0.0108 & 0.179 & $+1561$ \\
1399	0.75 & 0.0108 & $0.215{\pm}0.002$ & $+1885{\pm}18$ \\
1400	1.00 & 0.0108 & $0.421{\pm}0.004$ & $+3792{\pm}30$ \\
1401	\bottomrule
1402	\end{tabular}
1403	\end{table}
1404	
1405	ECE onset timing (5\% threshold) at $\alpha{\geq}0.50$ is generation~1, coinciding with entropy onset---consistent with the qualitative argument above that $\Delta\mathrm{ECE} > 0$ whenever $\Delta\bar{H} < 0$.
1406	At $\alpha{=}0.25$, ECE onset delays to generation~4 (seed~43), reflecting the weaker mode amplification signal at low contamination.
1407	At 1.4B scale, ECE follows the same pattern: gen-0 values are lower ($0.007$--$0.008$) but gen-10 values track collapse severity monotonically ($0.145$ at $\alpha{=}0.45$ to $0.268$ at $\alpha{=}0.75$).
1408	
1409	\paragraph{Empirical support for cascade ordering.}
1410	Cascade ordering $t_H \leq t_D$ holds in 14/15 experiments at $\alpha \geq 0.30$ (GPT-2-medium s43: bidirectional).
1411	Table~\ref{tab:cascade_onset} reports onset generations for representative conditions.
1412	
1413	\begin{table}[t]
1414	\centering
1415	\small
1416	\caption{Cascade onset generations (5\% threshold) for representative experiments (Pythia-410M, WikiText, fp32). Phase~1: entropy and ECE ($t_H$, $t_{\mathrm{ECE}}$); Phase~2: diversity ($t_D$, min over distinct-$n$); Phase~3: MAUVE ($t_M$). All conditions confirm the predicted ordering $t_H = t_{\mathrm{ECE}} \leq t_D \leq t_M$.}
1417	\label{tab:cascade_onset}
1418	\begin{tabular}{llcccc}
1419	\toprule
1420	Seed & $\alpha$ & $t_H$ & $t_{\mathrm{ECE}}$ & $t_D$ & $t_M$ \\
1421	\midrule
1422	42 & 0.50 & 1 & 1 & 2 & 3 \\
1423	43 & 0.50 & 1 & 1 & 2 & 2 \\
1424	42 & 0.75 & 1 & 1 & 2 & 3 \\
1425	43 & 0.75 & 1 & 1 & 2 & 2 \\
1426	\bottomrule
1427	\end{tabular}
1428	\end{table}
1429	
1430	
1431	\phantomsection\label{app:alpha_c_proof}
1432	\paragraph{Justification of the empirical boundary model.}
1433	At the detection threshold, $\mathrm{Power}(\alpha_c, T) = \pi^*$.
1434	Since $\alpha_c$ lies below the non-monotonic dip region ($\alpha_c < 0.55$), the signal model applies directly.
1435	From the power function $\mathrm{Power} = \Phi(S(\alpha) \cdot \sqrt{T} / \sigma)$, setting $S(\alpha_c) \cdot \sqrt{T} / \sigma = z^*$ and substituting the signal model $S(\alpha) = c\,\alpha^\beta$ yields $c\,\alpha_c^\beta = z^* \sigma / \sqrt{T}$.
1436	Solving: $\alpha_c(T) = (z^* \sigma / c)^{1/\beta} \cdot T^{-1/(2\beta)}$, giving the stated form with exponent $\gamma = 1/(2\beta)$.
1437	
1438	\paragraph{Calibration and consistency.}
1439	Fitting $P(\mathrm{det}|\alpha,T) = \Phi(A \cdot \alpha^\beta \cdot \sqrt{T} - z_0)$ to $T \in \{10, 20\}$ yields $\beta{=}0.24$, $\alpha_\infty{=}0$.
1440	Held-out test ($T \in \{5, 15\}$): MAE${=}0.106$, 95\% CI coverage 6/6.
1441	Leave-one-$T$-out CV (15 cells, sync-dip excluded): MAE${=}0.037$, coverage 15/15.
1442	Profile likelihood yields $\hat{\beta}{=}0.66$ (CI $[0.24, 0.78]$); the wide interval reflects a flat surface.
1443	
1444	\paragraph{Worked example.}
1445	At $\alpha{=}0.50$, $T{=}10$ (seed~42): entropy drops from $3.234$ to $2.649$ at gen-1 ($-18.1\%$), while distinct-1 remains at $0.0968$ (unchanged from gen-0).
1446	At gen-2, distinct-1 drops to $0.0812$ ($-16.1\%$).
1447	The mode amplification perturbation $\delta = 0.50 \cdot (\mathcal{T}(p_0) - p_0)$ satisfies $\|\delta\|_\infty < \gamma(p_0, \epsilon)$ at gen-0 (entropy responds, diversity does not), but at gen-1 the accumulated shift $p_1 = p_0 + \delta$ produces $\|\delta_1\|_\infty > \gamma(p_1, \epsilon)$, causing tokens to exit the effective support and triggering distinct-1 decline.
1448	The one-generation lag is thus explained by the margin condition in Observation~\ref{prop:div_lag}: the margin $\gamma$ is consumed by the gen-0$\to$1 perturbation, and the gen-1$\to$2 perturbation pushes tokens below the generation threshold $\epsilon$.
1449	
1450	\paragraph{Boundary model limitations.}
1451	The empirical boundary $\alpha_c(T) = A \cdot T^{-\gamma}$ is fitted to 3--4 data points ($T \in \{5, 10, 15, 20\}$) with 3 free parameters ($A$, $\gamma$, and the sub-linear signal exponent $\beta$).
1452	This parametric flexibility means the model can accommodate a wide range of decay shapes, and the $\gamma$ CI ($[0.64, 2.08]$) cannot distinguish sub-linear from super-linear decay.
1453	The boundary should therefore be interpreted as a descriptive summary of the observed pattern rather than a predictive model.
1454	Extrapolation beyond $T{=}25$ or below $\alpha{=}0.25$ is not supported by the data.
1455	The qualitative conclusion---detection improves with longer observation---is robust and does not depend on the specific $\gamma$ value.
1456	
1457	\paragraph{Sensitivity to the generation threshold $\epsilon$.}
1458	Observation~\ref{thm:entropy_leads} depends on the margin $\gamma(p, \epsilon)$, which in turn depends on the generation threshold $\epsilon \approx c/N$.
1459	Increasing the generation sample size $N$ (from 5{,}000 to 10{,}000) reduces $\epsilon$ by half, widening the margin and extending the entropy-only phase.
1460	In our experiments ($N{=}5{,}000$, effective $\epsilon \approx 2 \times 10^{-4}$), the margin is consumed after one generation at $\alpha{\geq}0.50$, producing the observed $t_D - t_H = 1$ lag.
1461	At lower contamination ($\alpha{=}0.25$), the smaller perturbation preserves the margin longer: the cumulative perturbation does not exceed $\gamma$ until gen-2--3 (Table~\ref{tab:margin_consumption}), explaining the wider entropy-diversity lag at low $\alpha$.
1462	
1463	\begin{table}[t]
1464	\centering
1465	\small
1466	\caption{Margin consumption across contamination levels (Pythia-410M, seed~42). ``Margin gen'' = first generation where cumulative $\|\delta\|_\infty > \gamma$. The diversity lag $t_D - t_H{=}1$ is invariant despite variable margin consumption timing.}
1467	\label{tab:margin_consumption}
1468	\begin{tabular}{lccc}
1469	\toprule
1470	$\alpha$ & $\gamma(p_0, \epsilon)$ & Margin gen & $t_D - t_H$ \\
1471	\midrule
1472	0.10 & $2.3 \times 10^{-3}$ & 3 & 1 \\
1473	0.25 & $2.3 \times 10^{-3}$ & 2 & 1 \\
1474	0.50 & $2.3 \times 10^{-3}$ & 1 & 1 \\
1475	0.75 & $2.3 \times 10^{-3}$ & 1 & 1 \\
1476	1.00 & $2.3 \times 10^{-3}$ & 1 & 1 \\
1477	\bottomrule
1478	\end{tabular}
1479	\end{table}
1480	
1481	The invariant $t_D - t_H = 1$ across all $\alpha$ levels (despite variable margin consumption timing) reflects the discrete-time nature of the experiment: even when the margin is consumed within a single generation, the diversity response cannot manifest until the next generation's samples are drawn.
1482	This suggests that continuous-time monitoring (within-generation token-level tracking) could reveal a finer-grained cascade with $\Delta t < 1$ generation, but our current experimental design cannot resolve sub-generation dynamics.
1483	
1484	\section{Power Simulation: Shape Comparison}
1485	\label{app:power_sim}
1486	
1487	Simulated PermG detection under linear (H0), concave (H0$'$), and step (H1) signal models (1{,}000 reps, $n_\text{perm}{=}1{,}000$, BH-FDR $q{=}0.05$).
1488	Smooth models produce onset steepness $k{=}4.9$--$6.1$; the observed $k{=}15.7$ is ${\approx}3{\times}$ higher.
1489	The scaling exponent alone cannot distinguish smooth from step boundaries (H0$'$ $\gamma{=}1.87$ vs.\ observed $\gamma{=}2.08$).
1490	The 6/8 detection ceiling reflects MAUVE floor saturation, not signal limitations.
1491	
1492	\paragraph{Signal model specifications.}
1493	\emph{H0 (linear)}: $S(\alpha) = c \cdot \alpha$, where $c$ is calibrated to produce 50\% detection at $\alpha{=}0.50$, $T{=}10$.
1494	\emph{H0$'$ (concave)}: $S(\alpha) = c \cdot \alpha^{0.5}$, capturing sub-linear signal growth as mode amplification saturates.
1495	\emph{H1 (step)}: $S(\alpha) = 0$ for $\alpha < \alpha_c$, $S(\alpha) = c$ for $\alpha \geq \alpha_c$, representing a genuine phase transition.
1496	The simulated DGP generates bivariate time series $(X_t, Y_t)$ with $Y_t = \beta X_{t-1} + \epsilon_t$ (lag-1 coupling); $\beta$ is set to produce the target $S(\alpha)$ at each contamination level.
1497	
1498	\paragraph{Onset steepness comparison.}
1499	Table~\ref{tab:steepness_comparison} reports fitted sigmoid steepness $k$ for each signal model.
1500	The observed $k{=}15.7$ (CI $[9.4, 28.2]$) exceeds all smooth-model predictions, with the lower CI bound ($k{=}9.4$) still ${\sim}2{\times}$ higher than the smoothest model (H0$'$: $k{=}4.9$).
1501	This excess steepness is consistent with---but does not prove---a genuine discontinuity in the signal structure at $\alpha_c$.
1502	
1503	\begin{table}[t]
1504	\centering
1505	\small
1506	\caption{Onset steepness $k$ under different signal models (1{,}000 reps, PermG, BH-FDR $q{=}0.05$).}
1507	\label{tab:steepness_comparison}
1508	\begin{tabular}{lccc}
1509	\toprule
1510	Model & $k$ & $\gamma$ & $k_{\mathrm{obs}}/k$ \\
1511	\midrule
1512	H0 (linear) & 6.1 & 2.08 & 2.6 \\
1513	H0$'$ (concave) & 4.9 & 1.87 & 3.2 \\
1514	H1 (step) & $\infty$ & --- & --- \\
1515	Observed & 15.7 & 2.08 & 1.0 \\
1516	\bottomrule
1517	\end{tabular}
1518	\end{table}
1519	
1520	\begin{figure}[t]
1521	\centering
1522	\includegraphics[width=\columnwidth]{figures/permg_power_curve.pdf}
1523	\caption{PermG power curves as a function of coupling strength $\beta$ for $T \in \{6, 8, 10, 15, 20\}$ (100 replications, 5{,}000 permutations, BH-FDR $q{=}0.05$). Power increases faster than $\sqrt{T}$, confirming that the theoretical $\sqrt{T}$ formula is a conservative lower bound. At $T{=}10$, 50\% power requires $\beta{\geq}2.0$; at $T{=}20$, this drops to $\beta{\approx}0.9$.}
1524	\label{fig:permg_power_curve}
1525	\end{figure}
1526	
1527	\section{T=20 Extension Results}
1528	\label{app:t20_comparison}
1529	
1530	At $\alpha{\geq}0.50$, PermG counts are consistent across $T{=}10$ and $T{=}20$ (6/8 at both), confirming signal-structure determination.
1531	At $\alpha{=}0.45$, the shift from 0/8 ($T{=}10$) to 5/8 ($T{=}20$) supports power-limited (Model~B) over structurally-undetectable (Model~A), lowering $\alpha_c$ below 0.45.
1532	The $\alpha{=}0.60$ dip persists at $T{=}20$ but dissolves at $T{=}25$ (5/8), confirming $\sqrt{T}$ power scaling eventually overcomes it.
1533	Directional selectivity is consistent: forward 6/8, reverse 0/8 at $\alpha \in \{0.50, 0.75, 1.0\}$ across all tested $T$.
1534	
1535	\paragraph{Full $T{=}25$ results.}
1536	Table~\ref{tab:t25_full} reports PermG forward detection counts at $T{=}25$ across contamination levels.
1537	Two key transitions emerge: (1)~$\alpha{=}0.45$ reaches 6/8 (dual-seed: s42 and s43 both 6/8), confirming that the blind-zone boundary has shifted below $\alpha{=}0.45$ at this observation length; (2)~the $\alpha{=}0.60$ sync-dip dissolves (5/8 at $T{=}25$ vs.\ 0/8 at $T{\leq}20$), with $K{\geq}3$ consensus reaching 6/8.
1538	The 6/8 detection ceiling at $\alpha{=}0.45$, $0.50$, $0.75$ matches the ceiling at shorter $T$, suggesting that 2/8 pairs are structurally non-detectable (likely MAUVE-related; MAUVE floor saturation at ${\sim}0.033$ produces near-constant series).
1539	
1540	\begin{table}[t]
1541	\centering
1542	\small
1543	\caption{PermG forward detection at $T{=}25$ (Pythia-410M, fp32). The $\alpha{=}0.45$ blind zone resolves and the $\alpha{=}0.60$ anomaly dissolves.}
1544	\label{tab:t25_full}
1545	\begin{tabular}{lccc}
1546	\toprule
1547	$\alpha$ & PermG fwd & $K{\geq}3$ & Note \\
1548	\midrule
1549	0.45 (s42) & 6/8 & 6/8 & blind$\to$detection \\
1550	0.45 (s43) & 6/8 & 6/8 & cross-seed confirmed \\
1551	0.50 (s42) & 6/8 & 6/8 & stable (matches $T{=}10$) \\
1552	0.60 (s42) & 5/8 & 6/8 & dip dissolves \\
1553	0.75 (s42) & 6/8 & 6/8 & stable \\
1554	0.75 (s43) & 6/8 & 6/8 & cross-seed confirmed \\
1555	\bottomrule
1556	\end{tabular}
1557	\end{table}
1558	
1559	\paragraph{$\alpha{=}0.25$ at extended $T$.}
1560	An unexpected result at $T{=}20$: PermG detects 3/8 at $\alpha{=}0.25$, where $T{=}10$ yields 0/8.
1561	This partial detection at very low contamination suggests that the blind zone is not absolute but power-limited: with sufficient observation length, even weak contamination signals may become detectable.
1562	However, 3/8 falls below the 6/8 reliability threshold we use for confirmed detection, and the result awaits multi-seed replication.
1563	
1564	\begin{figure}[t]
1565	\centering
1566	\includegraphics[width=\columnwidth]{figures/regime_map.pdf}
1567	\caption{Extended regime map including $T \in \{5, 10, 15, 20, 25\}$. The detection boundary shifts leftward with increasing $T$: $\alpha{=}0.45$ transitions from undetectable (0/8 at $T{\leq}10$) to reliable detection (6/8 at $T{=}15$). The $\alpha{=}0.60$ non-monotonic anomaly persists through $T{=}20$ but dissolves at $T{=}25$ (5/8).}
1568	\label{fig:regime_map_extended}
1569	\end{figure}
1570	
1571	\phantomsection\label{app:task_degradation}
1572	\paragraph{Task degradation.}
1573	End-of-training perplexity (gen~10, Pythia-410M, s42) improves at $\alpha{=}0.05$ (20.8 vs.\ 26.6 baseline, mild augmentation effect) but degrades sharply between $\alpha{=}0.50$ (31.3) and $0.52$ (41.1), aligning with PermG detection onset.
1574	
1575	\paragraph{Comprehensive cross-$T$ comparison.}
1576	Table~\ref{tab:cross_t_full} consolidates PermG forward detection across all tested observation windows, providing a complete view of the detection landscape evolution.
1577	
1578	\begin{table}[t]
1579	\centering
1580	\small
1581	\caption{PermG forward detection (/8 pairs) across $T$ and $\alpha$ (Pythia-410M, seed~42, fp32). Detection improves with $T$ at all contamination levels; the blind zone narrows monotonically.}
1582	\label{tab:cross_t_full}
1583	\begin{tabular}{lccccc}
1584	\toprule
1585	$\alpha$ & $T{=}5$ & $T{=}10$ & $T{=}15$ & $T{=}20$ & $T{=}25$ \\
1586	\midrule
1587	0.25 & 0/8 & 0/8 & --- & 3/8 & --- \\
1588	0.45 & 0/8 & 0/8 & 6/8 & 5/8 & 6/8 \\
1589	0.50 & 0/8 & 6/8 & 6/8 & 6/8 & 6/8 \\
1590	0.60 & 0/8 & 0/8 & 0/8 & 0/8 & 5/8 \\
1591	0.75 & 0/8 & 6/8 & 6/8 & 6/8 & 6/8 \\
1592	1.00 & 0/8 & 6/8 & 6/8 & 6/8 & 6/8 \\
1593	\bottomrule
1594	\multicolumn{6}{l}{\footnotesize ---: not tested at this combination.}
1595	\end{tabular}
1596	\end{table}
1597	
1598	Key observations from Table~\ref{tab:cross_t_full}:
1599	\begin{enumerate}
1600	\item $T{=}5$ yields 0/8 across all $\alpha$ levels---insufficient degrees of freedom for PermG detection.
1601	\item The 6/8 ceiling at $\alpha \in \{0.50, 0.75, 1.0\}$ is invariant across $T{=}10$--$25$, confirming signal-structure determination.
1602	\item $\alpha{=}0.45$ traverses the full blind$\to$detection boundary: 0/8 at $T{\leq}10$, 6/8 at $T{=}15$, stable thereafter.
1603	\item $\alpha{=}0.60$ is the only condition requiring $T{=}25$ for detection, with all shorter windows yielding 0/8.
1604	\item $\alpha{=}0.25$ at $T{=}20$ (3/8) is the only sub-threshold result, suggesting that very low contamination may eventually become detectable with sufficiently long observation.
1605	\end{enumerate}
1606	
1607	\paragraph{Directional consistency.}
1608	Across all conditions with ${\geq}6/8$ forward detection, reverse detection remains at 0/8 (with the exception of Pythia-1.4B s43 at $\alpha{\geq}0.60$; \S\ref{app:scale_14b}).
1609	This directional selectivity confirms that the forward-only constraint is not an artifact of a single $T$ value but reflects the genuine temporal asymmetry of the entropy-diversity cascade.
1610	
1611	\paragraph{Detection efficiency metrics.}
1612	Table~\ref{tab:detection_efficiency} reports detection efficiency---defined as the fraction of FDR-significant pairs out of 8---across observation windows, providing a normalized summary of the detection landscape.
1613	
1614	\begin{table}[t]
1615	\centering
1616	\small
1617	\caption{Detection efficiency (fraction of pairs reaching FDR significance) across the $\alpha \times T$ grid (Pythia-410M, seed~42, fp32). Efficiency plateaus at 0.75 for above-onset conditions, indicating a structural detection ceiling at 6/8 pairs.}
1618	\label{tab:detection_efficiency}
1619	\begin{tabular}{lcccc}
1620	\toprule
1621	$\alpha$ & $T{=}10$ & $T{=}15$ & $T{=}20$ & $T{=}25$ \\
1622	\midrule
1623	0.25 & 0.00 & --- & 0.375 & --- \\
1624	0.45 & 0.00 & 0.75 & 0.625 & 0.75 \\
1625	0.50 & 0.75 & 0.75 & 0.75 & 0.75 \\
1626	0.60 & 0.00 & 0.00 & 0.00 & 0.625 \\
1627	0.75 & 0.75 & 0.75 & 0.75 & 0.75 \\
1628	1.00 & 0.75 & 0.75 & 0.75 & 0.75 \\
1629	\bottomrule
1630	\multicolumn{5}{l}{\footnotesize ---: not tested at this combination.}
1631	\end{tabular}
1632	\end{table}
1633	
1634	The 0.75 plateau (6/8 pairs) is remarkably consistent across all conditions above the detection boundary, regardless of $T$ or $\alpha$.
1635	The 2/8 pairs that never reach significance involve MAUVE (floor saturation at ${\sim}0.033$ producing near-constant series) and perplexity (contemporaneous coupling; \S\ref{app:channel_effect_size}).
1636	This structural ceiling has practical implications: extending observation beyond $T{=}10$ at high contamination ($\alpha{\geq}0.50$) provides no additional detection power---the benefit of longer observation is concentrated in the boundary region ($\alpha \in [0.45, 0.60]$).
1637	
1638	\paragraph{Information gain per additional generation.}
1639	The marginal value of each additional generation varies by region.
1640	At $\alpha{=}0.45$, extending from $T{=}10$ to $T{=}15$ produces $+6$ newly significant pairs (information gain rate: $1.2$ pairs/gen); from $T{=}15$ to $T{=}20$, the rate drops to $-0.2$ pairs/gen (slight regression, likely noise).
1641	At $\alpha{=}0.60$ (sync-dip), the marginal value is zero through $T{=}20$ (0 new pairs across 10 additional generations) before producing $+5$ pairs in the $T{=}20{\to}25$ window (rate: $1.0$ pairs/gen).
1642	This non-uniform marginal return implies that a fixed-$T$ deployment strategy is suboptimal: adaptive monitoring that continues observation only when marginal information gain exceeds a threshold would reduce computational cost by 40--60\% without sacrificing detection reliability at high-$\alpha$ operating points.
1643	
1644	\subsection{Cross-Architecture Detection Table}
1645	\label{app:cross_arch_table}
1646	
1647	\begin{table}[t]
1648	\centering
1649	\small
1650	\caption{Cross-architecture PermG forward detection ($\alpha{=}1.0$, 15 model-seed combinations across five families---Pythia, GPT-2, OPT, Qwen, SmolLM3---and two domains; Padding-410M is a Pythia variant). PermG fwd $=$ count of FDR-significant forward pairs out of 8.}
1651	\label{tab:generalization}
1652	\resizebox{\columnwidth}{!}{%
1653	\begin{tabular}{lrcl}
1654	\toprule
1655	Model & Params & Domain & PermG fwd \\
1656	\midrule
1657	Pythia-410M    & 410M & Wiki & \textbf{6/8} \\
1658	Pythia-1.4B    & 1.4B & Wiki & 2--6/8$^\dagger$ \\
1659	Pythia-6.9B    & 6.9B & Wiki & \textbf{7/8}$^*$ \\
1660	\addlinespace
1661	GPT-2-medium   & 345M & Wiki & \textbf{6/8}$^\S$ \\
1662	\addlinespace
1663	OPT-1.3B       & 1.3B & Wiki & \textbf{6/8} \\
1664	\addlinespace
1665	Qwen3.5-0.8B   & 0.8B & Wiki & \textbf{8/8} \\
1666	SmolLM3-3B     & 3.0B & Wiki & 3/8$^\ddagger$ \\
1667	Padding-410M   & 410M & Wiki & \textbf{6/8} \\
1668	\addlinespace
1669	Pythia-1B      & 1.0B & C4   & \textbf{8/8} \\
1670	Pythia-1.4B    & 1.4B & C4   & \textbf{8/8} \\
1671	\bottomrule
1672	\multicolumn{4}{l}{\footnotesize $^\dagger$Seed-dep.\ (s42: 2/8, s43: 6/8); 8-pair incl.\ MAUVE} \\
1673	\multicolumn{4}{l}{\footnotesize \phantom{$^\dagger$}(floor ${\sim}0.033$ at 1.4B; 6-pair in Table~\ref{tab:14b_phase}). $^*$bf16. $^\ddagger$ECE-only (ent.\ 0/4).} \\
1674	\multicolumn{4}{l}{\footnotesize $^\S$s42 fp32: 6/8 fwd, 0 rev; s43: 6/8 both; bf16: 0/8.} \\
1675	\multicolumn{4}{l}{\footnotesize 2 seeds each for Pythia-410M/1.4B, GPT-2, OPT, Pythia-1B C4.} \\
1676	\end{tabular}%
1677	}
1678	\end{table}
1679	
1680	\subsection{Cross-Architecture FPR Sensitivity}
1681	\label{app:cross_arch_fpr}
1682	
1683	GPT-2-medium null-condition PermG FPR is 50\% (6/12 pooled, 2~seeds), dramatically higher than Pythia-410M (6.7\%), driven by ${\sim}4{\times}$ stronger null drift (entropy $-20.5\%$ vs.\ $-4.9\%$; distinct-3 $-35.8\%$ vs.\ $-4.9\%$).
1684	$K{\geq}3$ consensus maintains 0\% FPR (0/12) on GPT-2-medium, providing some protection, but standalone PermG requires architecture-specific null calibration.
1685	
1686	The cross-architecture detection heatmap is shown in Figure~\ref{fig:cross_arch_heatmap} (main text).
1687	
1688	\paragraph{GPT-2-medium: precision sensitivity.}
1689	GPT-2-medium at fp32 (seed~42) achieves 6/8 forward detection with 0/8 reverse, matching the Pythia-410M profile.
1690	Switching to bf16 drops detection to 0/8 without changing the underlying collapse dynamics (distinct-1 drift: $-28.4\%$ in both precisions).
1691	The mechanism is quantization noise masking the entropy signal: bf16 entropy time series exhibit ${\sim}2{\times}$ higher inter-generation variance than fp32, pushing PermG $p$-values from $p{<}0.01$ (fp32) to $p{>}0.20$ (bf16).
1692	This failure mode is fully resolved by using fp32 precision; architectures with native bf16 training (e.g., SmolLM3) require separate investigation.
1693	
1694	\paragraph{GPT-2-medium: seed-specific bidirectionality.}
1695	At seed~43, GPT-2-medium detects 6/8 in \emph{both} forward and reverse directions, preventing directional assignment.
1696	This bidirectionality is absent at seed~42 (6/8 forward, 0/8 reverse) and does not appear for any Pythia seed, suggesting it reflects GPT-2's specific learned dynamics rather than a general property of iterative collapse.
1697	Possible explanations include: (1)~GPT-2's attention patterns create feedback loops where diversity changes instantaneously feed back into entropy through the generation process; (2)~seed~43 produces a collapse trajectory where the entropy-diversity lag is below PermG's temporal resolution.
1698	
1699	\paragraph{SmolLM3-3B: entropy decoupling.}
1700	SmolLM3-3B achieves only 3/8 detection, with all significant pairs involving ECE rather than entropy (entropy: 0/4; ECE: 3/4).
1701	This violates the cascade ordering assumption (Observation~\ref{thm:entropy_leads}): in 3/8 conditions, entropy does not monotonically decrease across generations, exhibiting a recovery pattern between gen-3 and gen-5 before resuming decline.
1702	The non-monotonic entropy trajectory breaks the mode amplification assumption underlying the cascade ordering, suggesting that SmolLM3's architecture (likely due to its different attention mechanism or training objective) produces qualitatively different collapse dynamics.
1703	
1704	\paragraph{Domain effects: WikiText vs.\ C4.}
1705	C4-domain experiments (Pythia-1B and Pythia-1.4B) achieve uniformly higher detection rates (8/8) than their WikiText counterparts (6/8 and 2--6/8 respectively).
1706	This domain advantage may reflect C4's greater vocabulary diversity (broader token distribution $\to$ larger effective support $S_\epsilon$), which increases the margin $\gamma$ and produces a cleaner cascade ordering.
1707	Alternatively, WikiText's specialized vocabulary (encyclopedia-style text) may create mode amplification patterns that compress the entropy-diversity lag.
1708	
1709	\paragraph{Deployment recommendations.}
1710	Based on the cross-architecture results, we recommend:
1711	\begin{enumerate}
1712	\item Run null-control calibration on each target architecture before deployment (GPT-2 FPR: 50\% without calibration).
1713	\item Use fp32 precision for the detection pipeline even if training uses mixed precision.
1714	\item Apply $K{\geq}3$ consensus to reduce architecture-specific FPR inflation (0/12 on GPT-2 vs.\ 50\% standalone PermG).
1715	\item Verify monotonic entropy decline on the target architecture; non-monotonic cases (SmolLM3-3B) require ECE-based detection.
1716	\end{enumerate}
1717	
1718	\FloatBarrier
1719	\section*{Reproducibility Details}
1720	\label{app:reproducibility}
1721	
1722	\paragraph{Compute requirements.}
1723	Each Pythia-410M experiment (10 generations $\times$ 5{,}000 training steps $+$ 5{,}000 generation samples) requires approximately 4 GPU-hours on a single NVIDIA A100 (40GB).
1724	The full experimental matrix (13 $\alpha$ levels $\times$ 4~seeds $\times$ 5 observation windows $+$ cross-architecture) required approximately 800 GPU-hours total.
1725	Statistical analysis (permutation testing, Shapley computation, specification curves) runs on CPU in under 2 hours for the complete dataset.
1726	
1727	\paragraph{Software versions.}
1728	PyTorch 2.1.0, Transformers 4.36.0, Python 3.10.
1729	All experiments use deterministic mode (\texttt{torch.use\_deterministic\_algorithms(True)}) except generation (stochastic sampling), ensuring that training trajectories are reproducible given the same seed.
1730	
1731	\paragraph{Key implementation choices.}
1732	Several implementation decisions affect reproducibility:
1733	\begin{itemize}
1734	\item \emph{Checkpoint strategy}: each generation fine-tunes from the previous generation's checkpoint (not from pretrained $M_0$), implementing true iterative collapse rather than independent fine-tuning.
1735	\item \emph{Generation prompts}: the same 5{,}000 prompt set (sampled once per experiment) is used across all generations within a run, controlling for prompt-selection variance.
1736	\item \emph{Metric computation}: all metrics are computed on the same held-out set across generations; distinct-$n$ uses the full 5{,}000 generated samples (not a subsample).
1737	\item \emph{Pipeline versioning}: results in this paper use the d120 pipeline version, which corrected FPR calibration errors present in earlier versions (d103, d061). The d120 recompilation changed PermG detection at $\alpha{=}0.60$ from 3/8 (v3) to 0/8 (v4, reported).
1738	\end{itemize}
1739	
1740	\paragraph{Data availability.}
1741	WikiText-103~\citep{merity2017pointer} is publicly available.
1742	Synthetic data generated during experiments is not released (too large), but the generation scripts are included in the code release.
1743	All statistical analysis code, including the five detection methods, MMCT consensus, and specification curve construction, will be released upon acceptance.
1744	
1745	\section*{Use of AI Assistants}
1746	\label{app:ai-assistants}
1747	
1748	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
1749	\begin{itemize}
1750	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
1751	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting LaTeX.
1752	    \item \textbf{Literature:} summarizing related papers to inform related-work section.
1753	\end{itemize}
1754	
1755	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eafd53fb-f5f3-4d17-9352-ba80e4f693fd",
  "isSidechain": true,
  "promptId": "f9b7a34c-f506-492b-bf34-76d808a6acc5",
  "agentId": "ad2899e5fc9701ddb",
  "type": "user",
  "uuid": "86039d1f-5d47-4a0c-93fc-954342c95f19",
  "sourceToolAssistantUUID": "eafd53fb-f5f3-4d17-9352-ba80e4f693fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-25T09:06:49.701Z_

Perfect! I now have the entire file. Let me create a comprehensive catalog of all structural elements.

## Comprehensive Catalog of Structural Elements in appendix.tex

### SECTIONS

1. **Training Details and Metric Drift** | `app:training_details`, `app:drift` | Lines 3-91
2. **Distinct-3 Results** | `app:distinct3` | Lines 93-127
3. **Observation Window Sensitivity** | `app:window_sensitivity` | Lines 131-172
4. **Robustness Analysis** | `app:robustness`, `app:spec_curve` | Lines 176-221
5. **Transfer Entropy and Change-Point Analysis** | `app:transfer_entropy`, `app:te_mi` | Lines 223-244
6. **Sequential Monitoring: CUSUM vs Calibrated Threshold** | `app:csmp` | Lines 248-297
7. **Background and Notation** | `app:background`, `sec:background` | Lines 300-353
8. **MMCT Algorithm** | `app:mmct` | Lines 355-387
9. **Methodological Comparison Table** | `app:method_comparison` | Lines 390-425
10. **Extended Discussion** | `app:extended_discussion` | Lines 429-476
11. **Per-Method Dose-Response Profiles** | `app:dose_response` | Lines 548-606
12. **Cross-Seed Consistency at α=0.60** | `app:alpha060` | Lines 609-631
13. **PPL Threshold Baseline** | `app:ppl_threshold` | Lines 634-654
14. **PermG Power Analysis** | `app:power_analysis` | Lines 658-695
15. **Non-Stationarity Robustness Analysis** | `app:nonstationarity` | Lines 699-789
16. **Shapley Value Analysis** | `app:shapley` | Lines 793-830
17. **MMCT Weight Robustness Ablation** | `app:weight_robustness` | Lines 833-892
18. **PermG FPR Independence Analysis** | `app:fpr_independence` | Lines 896-990
19. **Sigmoid Transition Shape** | `app:sigmoid_shape` | Lines 993-1035
20. **Intervention Threshold Sensitivity** | `app:intervention_sensitivity` | Lines 1045-1070
21. **Channel Effect Size Analysis** | `app:channel_effect_size` | Lines 1073-1139
22. **Mutual Information and Partial Correlation** | `app:mi_analysis` | Lines 1143-1219
23. **Moment Cascade Analysis** | `app:moment_cascade` | Lines 1222-1283
24. **Cascade Ordering Theory: Derivations** | `app:cascade_theory` | Lines 1319-1482
25. **Power Simulation: Shape Comparison** | `app:power_sim` | Lines 1485-1525
26. **T=20 Extension Results** | `app:t20_comparison` | Lines 1528-1642
27. **Reproducibility Details** (section*) | `app:reproducibility` | Lines 1719-1743
28. **Use of AI Assistants** (section*) | `app:ai-assistants` | Lines 1745-1754

### SUBSECTIONS

1. **Per-Seed FPR Breakdown** | `app:per_seed_fpr` | Line 937
2. **Partial Correlation Analysis** | `app:partial_corr` | Line 1171
3. **Discretized Entropy Robustness Test** | `app:discretized_entropy` | Line 1286
4. **Cross-Architecture Detection Table** | `app:cross_arch_table` | Line 1644
5. **Cross-Architecture FPR Sensitivity** | `app:cross_arch_fpr` | Line 1680

### TABLES

1. **Per-architecture training hyperparameters** | `tab:arch_hyperparams` | Line 22 | "Per-architecture training hyperparameters"
2. **Metric drift summary** | `tab:drift_summary` | Line 60 | "Metric drift (%, generation 0→10) for Pythia-410M across..."
3. **Distinct-3 drift** | `tab:distinct3_drift` | Line 104 | "Distinct-3 drift (%, generation 0→10) across contamination..."
4. **Observation window sensitivity** | `tab:window_sensitivity` | Line 158 | "Observation window sensitivity for Tier 3 consensus..."
5. **Specification curve summary** | `tab:spec_curve` | Line 192 | "Specification curve summary (1,160 specifications, D120...)"
6. **Sequential monitoring alarm timing** | `tab:sequential_timing` | Line 274 | "Sequential monitoring alarm timing (Pythia-410M, seed..."
7. **Methodological comparison** | `tab:method-comparison` | Line 400 | "Methodological comparison of canary and monitoring analy..."
8. **Failure mode taxonomy** | `tab:failure_modes` | Line 459 | "Failure mode taxonomy for non-confirming cross-architec..."
9. **Pythia-1.4B phase diagram** | `tab:14b_phase` | Line 486 | "Pythia-1.4B phase diagram replication: PermG forward/..."
10. **Per-method dose-response full** | `tab:dose_response_full` | Line 557 | "Per-method FDR significance (/8 pairs) across contaminat..."
11. **Shapley value decomposition** | `tab:shapley_6pair` | Line 817 | "Shapley value decomposition (6-pair, MAUVE excluded)"
12. **MMCT weight robustness** | `tab:weight_robustness` | Line 843 | "PermG combined Shapley under four weighting schemes"
13. **Shapley per-pair contribution** | `tab:shapley_per_pair` | Line 871 | "Shapley contribution by canary→downstream pair (PermG...)"
14. **Null-control FPR methods** | `tab:null_fpr_methods` | Line 921 | "Null-control FPR by method (α=0.0, BH-FDR q=0.05)"
15. **Per-seed FPR 8-pair basis** | `tab:per_seed_fpr_8pair` | Line 953 | "Per-seed FPR (8-pair basis, α=0.0, Pythia-410M, seeds..."
16. **Per-seed FPR 6-pair basis** | `tab:per_seed_fpr_6pair` | Line 972 | "Per-seed PermG FPR (6-pair basis, α=0.0, seeds 45-51)"
17. **Sigmoid transition width** | `tab:transition_width` | Line 1018 | "Sigmoid transition width (90% range) by observation..."
18. **Lag structure** | `tab:lag_structure` | Line 1087 | "Cross-correlation peak lag by channel (Pythia-410M...)"
19. **Fisher Z-transform comparison** | `tab:fisher_z` | Line 1112 | "Fisher Z-transform comparison of channel correlations..."
20. **Partial correlation table** | `tab:partial_corr` | Line 1180 | "Partial correlation controlling for generation"
21. **Moment cascade** | `tab:moment_cascade` | Line 1231 | "Degradation onset generation (5% threshold) by metric..."
22. **Onset threshold sensitivity** | `tab:onset_threshold_sensitivity` | Line 1258 | "Cascade ordering $t_H ≤ t_D$ validity as a function..."
23. **Discretized entropy** | `tab:discretized_entropy` | Line 1298 | "Discretized entropy Granger test: number of experiments..."
24. **ECE drift** | `tab:ece_drift` | Line 1390 | "ECE drift across contamination levels (Pythia-410M...)"
25. **Cascade onset** | `tab:cascade_onset` | Line 1417 | "Cascade onset generations (5% threshold) for represent..."
26. **Margin consumption** | `tab:margin_consumption` | Line 1467 | "Margin consumption across contamination levels..."
27. **Steepness comparison** | `tab:steepness_comparison` | Line 1507 | "Onset steepness k under different signal models..."
28. **T=25 full results** | `tab:t25_full` | Line 1544 | "PermG forward detection at T=25 (Pythia-410M, fp32)"
29. **Cross-T full comparison** | `tab:cross_t_full` | Line 1582 | "PermG forward detection (/8 pairs) across T and α..."
30. **Detection efficiency** | `tab:detection_efficiency` | Line 1618 | "Detection efficiency (fraction of pairs reaching FDR...)"
31. **Cross-architecture generalization** | `tab:generalization` | Line 1651 | "Cross-architecture PermG forward detection (α=1.0...)"
32. **Nonstationarity simulation** | `tab:nonstationarity_sim` | Line 717 | "Size and power under AR(1) DGP (T=11, 1,000 reps)"
33. **Empirical AR(1) coefficients** | `tab:empirical_ar1` | Line 741 | "Empirical AR(1) coefficients (Pythia-410M, 4 seeds)"
34. **Differencing power cost** | `tab:diff_power_cost` | Line 776 | "Power cost of first-differencing under simulated AR(1...)"
35. **PermG power analysis beta50** | `tab:beta50` | Line 684 | "PermG power analysis: β₅₀ (coupling for 50% power)..."
36. **MI blind zone** | `tab:mi_blind` | Line 1157 | "Gaussian MI lower bound between token entropy and..."

### FIGURES

1. **Window sensitivity figure** | `fig:window_sensitivity` | Line 150 | "Detection stability as a function of minimum observ..."
2. **Consensus heatmap** | `fig:consensus_heatmap` | Line 363 | "K≥3 consensus heatmap across the α × T grid..."
3. **MMCT K operating characteristics** | `fig:mmct_k_operating` | Line 386 | "MMCT operating characteristics as a function of cons..."
4. **Shapley contribution top** | `fig:shapley_contribution` | Line 804 | "Shapley value decomposition by method"
5. **Shapley contribution bottom (continued)** | | Line 810 | (Continued figure)
6. **FPR sensitivity** | `fig:fpr_sensitivity` | Line 906 | "Per-seed FPR distribution across detection methods..."
7. **Null FPR diagnostic** | `fig:null_fpr_diagnostic` | Line 913 | "Null-control diagnostic: PermG p-value distributions..."
8. **Bootstrap FPR** | `fig:bootstrap_fpr` | Line 946 | "Bootstrap confidence intervals for FPR estimates..."
9. **Per-method phase top** | `fig:per_method_phase` | Line 599 | "Per-method FDR-significant pair counts (/8) across..."
10. **Per-method phase bottom (continued)** | | Line 605 | (Continued figure)
11. **AR(1) diagnostic** | `fig:ar1_diagnostic` | Line 710 | "AR(1) coefficient estimates across five contamination..."
12. **14B phase diagram** | `fig:14b_phase` | Line 529 | "Pythia-1.4B phase diagram (PermG forward, 6-pair basis)"
13. **Differencing order selection** | `fig:differencing_dmax` | Line 1041 | "First-differencing order selection diagnostic"
14. **CUSUM monitoring** | `fig:cusum_monitoring` | Line 1069 | "CUSUM sequential monitoring versus calibrated threshold..."
15. **Channel effect** | `fig:channel_effect` | Line 1138 | "Channel effect size comparison: Granger F-statistic..."
16. **Partial correlation scatter plots** | `fig:partial_corr` | Line 1201 | "Partial correlation scatter plots for canary→diversity..."
17. **Partial correlation aggregated** | `fig:partial_corr_agg` | Line 1208 | "Aggregated partial correlation analysis across conta..."
18. **PermG power curve** | `fig:permg_power_curve` | Line 1524 | "PermG power curves as a function of coupling strength..."
19. **Regime map extended** | `fig:regime_map_extended` | Line 1568 | "Extended regime map including T ∈ {5, 10, 15, 20, 25}"

### THEOREMS/PROPOSITIONS

1. **Assumption: Mode Amplification** | `ass:mode_amp` | Line 1324 | "Mode Amplification"
2. **Proposition: Entropy is first-order indicator** | `prop:entropy_first` | Line 1330 | "Entropy is a first-order indicator"
3. **Proposition: Diversity is threshold indicator** | `prop:div_threshold` | Line 1343 | "Diversity is a threshold indicator"

### EQUATIONS

1. **Mixing equation** | `eq:mixing` | Line 310 | "D_train = α·D_synth + (1-α)·D_real"

### FLOATS WITH CONTINUED FLOAT

- **Shapley contribution figure** (lines 800-811): Top and bottom panels with ContinuedFloat
- **Per-method phase figure** (lines 596-606): Top and bottom panels with ContinuedFloat

---

**Total Count Summary:**
- Sections: 28 (including 2 section*)
- Subsections: 5
- Tables: 36
- Figures: 19
- Theorems/Propositions/Assumptions: 3
- Equations: 1
- **Total labeled elements: 92**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86039d1f-5d47-4a0c-93fc-954342c95f19",
  "isSidechain": true,
  "agentId": "ad2899e5fc9701ddb",
  "requestId": "req_011CbP2CReKgqADkqFY71bed",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8311a21e-e924-4a5a-bda3-3dbbc6d61173",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AxZ86D7syXX6Ufjg4Dvg1q",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 26156,
      "cache_read_input_tokens": 71519,
      "output_tokens": 3528,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 26156
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 3528,
          "cache_read_input_tokens": 71519,
          "cache_creation_input_tokens": 26156,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 26156,
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
