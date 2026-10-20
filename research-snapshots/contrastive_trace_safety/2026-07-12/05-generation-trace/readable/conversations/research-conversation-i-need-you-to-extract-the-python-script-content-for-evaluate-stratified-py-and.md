# Research conversation: I need you to extract the Python script content for `evaluate_stratified.py` and `analyze_stratified.py` from a worker c

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a244b0313f96edf04.jsonl`
- **Structured JSON:** [`3c22eb96bb418c7504a9.json`](../../sessions/3c/3c22eb96bb418c7504a9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

23 recorded events

### User

_source line 1 · 2026-05-15T07:54:39.108Z_

I need you to extract the Python script content for `evaluate_stratified.py` and `analyze_stratified.py` from a worker chat log. These scripts were created during a previous worker session but weren't persisted to the server.

The chat log is at: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/worker_code_plan005-stratified-prep_20260515T050005.jsonl`

This is a JSONL file where each line is a JSON object with assistant messages that may contain tool_use calls (like ssh_execute) that wrote these scripts to the server. Look for the actual Python source code content of both scripts.

Also check the spec file for the expected interface:
`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_005/report/plan005_stratification_spec.md`

Return the FULL source code of both scripts (evaluate_stratified.py and analyze_stratified.py) exactly as they were written. If you can't find them in the chat log, check if there's a local copy anywhere in the project directory tree.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "658d2eb0-8593-44d8-a0a6-011e29c3e29c",
  "agentId": "a244b0313f96edf04",
  "type": "user",
  "uuid": "45849d27-9ecc-4a9b-9153-4b6e82d13334",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "953f15f8-e655-48b5-a31c-751a817178ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T07:54:39.113Z_

```json
{
  "parentUuid": "45849d27-9ecc-4a9b-9153-4b6e82d13334",
  "isSidechain": true,
  "agentId": "a244b0313f96edf04",
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
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__update_registry"
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
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "ce87b32c-16fc-49a7-a383-0151ed25e55f",
  "timestamp": "2026-05-15T07:54:39.113Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "953f15f8-e655-48b5-a31c-751a817178ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T07:54:41.694Z_



I'll start by reading the chat log and the spec file in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce87b32c-16fc-49a7-a383-0151ed25e55f",
  "isSidechain": true,
  "agentId": "a244b0313f96edf04",
  "requestId": "req_011Cb3zeBGoYepwKm33uYn3v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad6d50b2-3dc4-4300-b320-5c498dd1437a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "953f15f8-e655-48b5-a31c-751a817178ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1gGBhrZuwJV4GnKWRPMfP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14370,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14370,
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

_source line 4 · 2026-05-15T07:54:42.745Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01L6gGamg6d2R8LS3kezYjSq`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/worker_code_plan005-stratified-prep_20260515T050005.jsonl",
  "description": "Count lines in the JSONL chat log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad6d50b2-3dc4-4300-b320-5c498dd1437a",
  "isSidechain": true,
  "agentId": "a244b0313f96edf04",
  "requestId": "req_011Cb3zeBGoYepwKm33uYn3v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf40556f-687f-4d44-9f7b-a97d19af80e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "953f15f8-e655-48b5-a31c-751a817178ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1gGBhrZuwJV4GnKWRPMfP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14370,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14370,
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

_source line 5 · 2026-05-15T07:54:42.796Z_

<details><summary>↩ Tool result · `toolu_01L6gGamg6d2R8LS3kezYjSq`</summary>

```text
101 /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/worker_code_plan005-stratified-prep_20260515T050005.jsonl
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf40556f-687f-4d44-9f7b-a97d19af80e7",
  "isSidechain": true,
  "promptId": "658d2eb0-8593-44d8-a0a6-011e29c3e29c",
  "agentId": "a244b0313f96edf04",
  "type": "user",
  "uuid": "c8f6dfbe-17ce-4eb7-82e7-fa82f5e9e95b",
  "sourceToolAssistantUUID": "cf40556f-687f-4d44-9f7b-a97d19af80e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "953f15f8-e655-48b5-a31c-751a817178ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T07:54:43.673Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GxRYEZ3UD9KB2DkCAyafgM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_005/report/plan005_stratification_spec.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8f6dfbe-17ce-4eb7-82e7-fa82f5e9e95b",
  "isSidechain": true,
  "agentId": "a244b0313f96edf04",
  "requestId": "req_011Cb3zeBGoYepwKm33uYn3v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "069d84c0-88f7-4ff2-bf3b-831125bf6ec5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "953f15f8-e655-48b5-a31c-751a817178ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1gGBhrZuwJV4GnKWRPMfP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14370,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14370,
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

_source line 7 · 2026-05-15T07:54:43.680Z_

<details><summary>↩ Tool result · `toolu_01GxRYEZ3UD9KB2DkCAyafgM`</summary>

````text
1	# Plan 005: Stratified Analysis Specification
2	
3	## Pipeline
4	
5	Three-stage pipeline, stages 1 & 3 are CPU-only:
6	
7	1. **`prepare_stratification_index.py`** (CPU, DONE) — parses all.jsonl → `stratification_index.json`
8	2. **`evaluate_stratified.py`** (GPU, awaiting M2 checkpoints) — per-query eval with pool_size control
9	3. **`analyze_stratified.py`** (CPU) — stratification + bootstrap CI + plots
10	
11	## 5 Stratification Dimensions
12	
13	| # | Dimension | Bins | Source | Method |
14	|---|-----------|------|--------|--------|
15	| 1 | Repo size (file count) | small (<50), medium (50-200), large (200+) | `stratification_index.json` → `repo_file_count` | Fixed thresholds (matches BM25 overlap analysis) |
16	| 2 | Eval pool size | Quartiles | Per-query eval output → `pool_size` | Data-driven quartiles |
17	| 3 | Query-positive similarity | Quartiles | Per-query eval output → `query_pos_sim` | Data-driven quartiles |
18	| 4 | Structural data availability | Binary: with_structural / no_structural | `stratification_index.json` → `has_structural` | Binary (34.3% with / 65.7% without) |
19	| 5 | Negative difficulty | Quartiles of mean neg cosine sim | Per-query eval output → `mean_neg_sim` | Data-driven quartiles |
20	
21	## Pool Size Control (D038)
22	
23	`evaluate_stratified.py` accepts `--pool-sizes 50,100,200,500` to test strategy ranking stability across pool sizes. Each pool size produces a separate per-query JSONL. Analysis is run independently per pool size.
24	
25	Padding strategy: when a query has fewer candidates than target pool_size, pad with global distractors from other queries in the same val set (same as `eval_p2b_pooled.py`).
26	
27	## Data Sources
28	
29	- **M1 metadata**: `/root/autodl-tmp/structfuse/stratification_index.json` (19MB, 44,173 instances, 123 repos)
30	- **Val data**: `/root/autodl-tmp/structfuse/full_m2_training_data/val_{strategy}_s{seed}.jsonl` (2,980 queries each)
31	- **Checkpoints**: `/root/autodl-tmp/structfuse/checkpoints/m2_full_{encoder}/{strategy}_s{seed}/`
32	
33	## Per-query Output Schema
34	
35	```json
36	{
37	  "query_id": "instance_id::file_path",
38	  "instance_id": "repo.commit.mutation__hash",
39	  "gold_rank": 0,
40	  "pool_size": 50,
41	  "query_pos_sim": 0.712345,
42	  "mean_neg_sim": 0.351234,
43	  "max_neg_sim": 0.581234,
44	  "hit_at_1": true,
45	  "hit_at_5": true,
46	  "hit_at_10": true
47	}
48	```
49	
50	## Analysis Outputs
51	
52	- `stratified_results.json` — full results with bootstrap 95% CIs per stratum
53	- `stratified_results.csv` — flat table for easy import
54	- `stratified_{dimension}.pdf` — bar charts: R@1 per strategy (left), delta vs random (right)
55	- Weighted aggregate delta per dimension (accounts for stratum sizes)
56	
57	## Execution Plan
58	
59	When M2 checkpoints are ready:
60	
61	```bash
62	# Stage 2: per-query eval (GPU, ~30min per run × 18 runs)
63	for encoder in qwen starcoder; do
64	  for strategy in random embedding_distance dataflow_aware; do
65	    for seed in 42 43 44; do
66	      python evaluate_stratified.py \
67	        --ckpt-dir /root/autodl-tmp/structfuse/checkpoints/m2_full_${encoder}/${strategy}_s${seed} \
68	        --model-name /root/autodl-tmp/structfuse/models/${model_path} \
69	        --val-file /root/autodl-tmp/structfuse/full_m2_training_data/val_${strategy}_s${seed}.jsonl \
70	        --pool-sizes 50 \
71	        --output-dir /root/structfuse/results/stratified/per_query \
72	        --tag ${encoder}_${strategy}_s${seed}
73	    done
74	  done
75	done
76	
77	# Stage 3: analysis (CPU, <1min)
78	python analyze_stratified.py \
79	  --results-dir /root/structfuse/results/stratified/per_query \
80	  --index-file /root/autodl-tmp/structfuse/stratification_index.json \
81	  --strategies random,embedding_distance,dataflow_aware \
82	  --encoder qwen --seeds 42,43,44 --pool-size 50 \
83	  --output-dir /root/structfuse/results/stratified
84	```
85	
86	## Verification
87	
88	- [x] `prepare_stratification_index.py` — completed, 44,173 instances indexed
89	- [x] `evaluate_stratified.py --dry-run` — passed (2,980 queries, multi-pool-size)
90	- [x] `analyze_stratified.py --dry-run` — passed (5 dimensions, JSON+CSV+5 PDFs)
91	- [ ] Real eval — awaiting M2 checkpoints
92	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "069d84c0-88f7-4ff2-bf3b-831125bf6ec5",
  "isSidechain": true,
  "promptId": "658d2eb0-8593-44d8-a0a6-011e29c3e29c",
  "agentId": "a244b0313f96edf04",
  "type": "user",
  "uuid": "72380042-d14e-4530-ad40-567e886540db",
  "sourceToolAssistantUUID": "069d84c0-88f7-4ff2-bf3b-831125bf6ec5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "953f15f8-e655-48b5-a31c-751a817178ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T07:54:44.126Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011xYEqXrr7ada5PRaLZP7Zi`</summary>

```json
{
  "pattern": "**/evaluate_stratified.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72380042-d14e-4530-ad40-567e886540db",
  "isSidechain": true,
  "agentId": "a244b0313f96edf04",
  "requestId": "req_011Cb3zeBGoYepwKm33uYn3v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3bcf76d-9bac-4d32-924a-79a78188eb8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "953f15f8-e655-48b5-a31c-751a817178ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1gGBhrZuwJV4GnKWRPMfP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14370,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14370,
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

_source line 9 · 2026-05-15T07:54:44.139Z_

<details><summary>↩ Tool result · `toolu_011xYEqXrr7ada5PRaLZP7Zi`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3bcf76d-9bac-4d32-924a-79a78188eb8e",
  "isSidechain": true,
  "promptId": "658d2eb0-8593-44d8-a0a6-011e29c3e29c",
  "agentId": "a244b0313f96edf04",
  "type": "user",
  "uuid": "327db6c1-dd71-4dc3-a105-6bc0646c521c",
  "sourceToolAssistantUUID": "f3bcf76d-9bac-4d32-924a-79a78188eb8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "953f15f8-e655-48b5-a31c-751a817178ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T07:54:44.477Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019YoeAoeKkgqXnP3pGev7fZ`</summary>

```json
{
  "pattern": "**/analyze_stratified.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "327db6c1-dd71-4dc3-a105-6bc0646c521c",
  "isSidechain": true,
  "agentId": "a244b0313f96edf04",
  "requestId": "req_011Cb3zeBGoYepwKm33uYn3v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc8904fd-c7ab-4ca3-b5ef-078d899a31ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "953f15f8-e655-48b5-a31c-751a817178ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1gGBhrZuwJV4GnKWRPMfP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14370,
      "cache_read_input_tokens": 0,
      "output_tokens": 401,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14370
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 401,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 14370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14370,
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

_source line 11 · 2026-05-15T07:54:44.499Z_

<details><summary>↩ Tool result · `toolu_019YoeAoeKkgqXnP3pGev7fZ`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc8904fd-c7ab-4ca3-b5ef-078d899a31ad",
  "isSidechain": true,
  "promptId": "658d2eb0-8593-44d8-a0a6-011e29c3e29c",
  "agentId": "a244b0313f96edf04",
  "type": "user",
  "uuid": "4e01c528-1bc4-47f7-89b2-d89bec35b15d",
  "sourceToolAssistantUUID": "bc8904fd-c7ab-4ca3-b5ef-078d899a31ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "953f15f8-e655-48b5-a31c-751a817178ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-15T07:54:47.538Z_

No local copies found. Let me search the JSONL chat log for the script contents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e01c528-1bc4-47f7-89b2-d89bec35b15d",
  "isSidechain": true,
  "agentId": "a244b0313f96edf04",
  "requestId": "req_011Cb3zeaCCP4GEGQRK6ZiMT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c69c92b-d35f-4293-a1ff-10130913406b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "953f15f8-e655-48b5-a31c-751a817178ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016mjQmSWC5JjE4CgtC82iFP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2955,
      "cache_read_input_tokens": 14370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2955,
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

_source line 13 · 2026-05-15T07:54:48.437Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01FXw3uK7dzXRHvTq2dd63xu`</summary>

```json
{
  "pattern": "evaluate_stratified\\.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/worker_code_plan005-stratified-prep_20260515T050005.jsonl",
  "output_mode": "content",
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c69c92b-d35f-4293-a1ff-10130913406b",
  "isSidechain": true,
  "agentId": "a244b0313f96edf04",
  "requestId": "req_011Cb3zeaCCP4GEGQRK6ZiMT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a26619ba-0b41-4ef1-9db5-2f91c93bd16a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "953f15f8-e655-48b5-a31c-751a817178ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016mjQmSWC5JjE4CgtC82iFP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2955,
      "cache_read_input_tokens": 14370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2955,
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

_source line 14 · 2026-05-15T07:54:48.459Z_

<details><summary>↩ Tool result · `toolu_01FXw3uK7dzXRHvTq2dd63xu`</summary>

```text
63:[Omitted long matching line]
64:{"ts": "2026-05-15T05:09:54.789503+00:00", "role": "tool_result", "session": "worker_code_plan005-stratified-prep_20260515T050005", "text": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"evaluate_stratified.py written OK\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}", "tool": "mcp__agent-ml-research__ssh_execute", "elapsed_ms": 0}
91:[Omitted long matching line]
97:[Omitted long matching line]
101:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a26619ba-0b41-4ef1-9db5-2f91c93bd16a",
  "isSidechain": true,
  "promptId": "658d2eb0-8593-44d8-a0a6-011e29c3e29c",
  "agentId": "a244b0313f96edf04",
  "type": "user",
  "uuid": "35953db3-a795-4ea0-b2ff-7959afbdfc4d",
  "sourceToolAssistantUUID": "a26619ba-0b41-4ef1-9db5-2f91c93bd16a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "953f15f8-e655-48b5-a31c-751a817178ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T07:54:49.397Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01XEwMTSpias2nnjnEQvw6MA`</summary>

```json
{
  "pattern": "analyze_stratified\\.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/worker_code_plan005-stratified-prep_20260515T050005.jsonl",
  "output_mode": "content",
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35953db3-a795-4ea0-b2ff-7959afbdfc4d",
  "isSidechain": true,
  "agentId": "a244b0313f96edf04",
  "requestId": "req_011Cb3zeaCCP4GEGQRK6ZiMT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48941102-e45e-4423-a2fa-8930f24b263a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "953f15f8-e655-48b5-a31c-751a817178ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016mjQmSWC5JjE4CgtC82iFP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2955,
      "cache_read_input_tokens": 14370,
      "output_tokens": 333,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2955
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 333,
          "cache_read_input_tokens": 14370,
          "cache_creation_input_tokens": 2955,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2955,
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

_source line 16 · 2026-05-15T07:54:49.409Z_

<details><summary>↩ Tool result · `toolu_01XEwMTSpias2nnjnEQvw6MA`</summary>

```text
28:[Omitted long matching line]
63:[Omitted long matching line]
65:[Omitted long matching line]
66:{"ts": "2026-05-15T05:09:54.790023+00:00", "role": "tool_result", "session": "worker_code_plan005-stratified-prep_20260515T050005", "text": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"analyze_stratified.py written OK\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}", "tool": "mcp__agent-ml-research__ssh_execute", "elapsed_ms": 0}
85:[Omitted long matching line]
86:[Omitted long matching line]
87:[Omitted long matching line]
89:[Omitted long matching line]
97:[Omitted long matching line]
101:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48941102-e45e-4423-a2fa-8930f24b263a",
  "isSidechain": true,
  "promptId": "658d2eb0-8593-44d8-a0a6-011e29c3e29c",
  "agentId": "a244b0313f96edf04",
  "type": "user",
  "uuid": "c0ad263b-86fd-4be2-a5d2-00ad8936ea38",
  "sourceToolAssistantUUID": "48941102-e45e-4423-a2fa-8930f24b263a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "953f15f8-e655-48b5-a31c-751a817178ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-15T07:54:52.396Z_

The scripts were written on line 63 (which contains both). Let me read that line to extract the full content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0ad263b-86fd-4be2-a5d2-00ad8936ea38",
  "isSidechain": true,
  "agentId": "a244b0313f96edf04",
  "requestId": "req_011Cb3zew9X2PFGmJa6YPNMT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "334e365f-49c0-4481-af80-e770b10197b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "953f15f8-e655-48b5-a31c-751a817178ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KfHE26PF9UDLvzihQkdkKC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 17325,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 896,
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

_source line 18 · 2026-05-15T07:54:53.215Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ESJSTPJGkZbEcJNUZ9yyNd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/worker_code_plan005-stratified-prep_20260515T050005.jsonl",
  "offset": 62,
  "limit": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "334e365f-49c0-4481-af80-e770b10197b3",
  "isSidechain": true,
  "agentId": "a244b0313f96edf04",
  "requestId": "req_011Cb3zew9X2PFGmJa6YPNMT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d69465c8-b8fb-49ea-a691-735887454794",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "953f15f8-e655-48b5-a31c-751a817178ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KfHE26PF9UDLvzihQkdkKC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 17325,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 896
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 17325,
          "cache_creation_input_tokens": 896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 896,
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

_source line 19 · 2026-05-15T07:54:53.221Z_

<details><summary>↩ Tool result · `toolu_01ESJSTPJGkZbEcJNUZ9yyNd`</summary>

```text
62	{"ts": "2026-05-15T05:09:54.789126+00:00", "role": "tool_result", "session": "worker_code_plan005-stratified-prep_20260515T050005", "text": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"prepare_stratification_index.py written OK\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}", "tool": "mcp__agent-ml-research__ssh_execute", "elapsed_ms": 0}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d69465c8-b8fb-49ea-a691-735887454794",
  "isSidechain": true,
  "promptId": "658d2eb0-8593-44d8-a0a6-011e29c3e29c",
  "agentId": "a244b0313f96edf04",
  "type": "user",
  "uuid": "63c4953b-3950-494b-aa78-1bac01588ced",
  "sourceToolAssistantUUID": "d69465c8-b8fb-49ea-a691-735887454794",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "953f15f8-e655-48b5-a31c-751a817178ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-15T07:54:57.641Z_

That line was a tool result. The actual script content would be in the assistant message with the ssh_execute tool_use call. Let me look at the lines around 63 more carefully, and also check what's on line 63 itself (the file uses 1-based indexing in the grep output but 0-based offset in Read).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63c4953b-3950-494b-aa78-1bac01588ced",
  "isSidechain": true,
  "agentId": "a244b0313f96edf04",
  "requestId": "req_011Cb3zfDXGDN96D2q5NaCws",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27beb438-f5a3-4cbe-9a57-222faf12c4e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "953f15f8-e655-48b5-a31c-751a817178ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ZMQsFKZJsUGRvkexANpxV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 469,
      "cache_read_input_tokens": 18221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 469,
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

_source line 21 · 2026-05-15T07:54:58.226Z_

<details open><summary>🔧 Tool call — Read · `toolu_015uX33RSu5aYqPjzCKUeXfU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/worker_code_plan005-stratified-prep_20260515T050005.jsonl",
  "offset": 62,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27beb438-f5a3-4cbe-9a57-222faf12c4e2",
  "isSidechain": true,
  "agentId": "a244b0313f96edf04",
  "requestId": "req_011Cb3zfDXGDN96D2q5NaCws",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e44ca124-d1be-4d6c-8848-87c010cfa608",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "953f15f8-e655-48b5-a31c-751a817178ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ZMQsFKZJsUGRvkexANpxV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 469,
      "cache_read_input_tokens": 18221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 469,
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

_source line 22 · 2026-05-15T07:54:58.503Z_

<details><summary>↩ Tool result · `toolu_015uX33RSu5aYqPjzCKUeXfU`</summary>

```text
62	{"ts": "2026-05-15T05:09:54.789126+00:00", "role": "tool_result", "session": "worker_code_plan005-stratified-prep_20260515T050005", "text": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"prepare_stratification_index.py written OK\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}", "tool": "mcp__agent-ml-research__ssh_execute", "elapsed_ms": 0}
63	{"ts": "2026-05-15T05:09:54.789284+00:00", "role": "tool", "session": "worker_code_plan005-stratified-prep_20260515T050005", "text": "called mcp__agent-ml-research__ssh_execute", "tool": "mcp__agent-ml-research__ssh_execute", "tool_args": {"server": "bjb1-42106", "command": "cat > /root/structfuse/scripts/evaluate_stratified.py << 'PYEOF'\n\"\"\"Per-query evaluation for stratified analysis (plan_005).\n\nEvaluates M2 checkpoints and records per-query results including gold rank,\ncosine similarities, and pool sizes. Supports multiple pool sizes (D038).\n\nOutputs per-query JSONL for downstream analyze_stratified.py.\n\nUsage:\n    # Real eval (GPU):\n    python evaluate_stratified.py \\\n        --ckpt-dir /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42 \\\n        --model-name /root/autodl-tmp/structfuse/models/Qwen2.5-Coder-3B \\\n        --val-file /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl \\\n        --pool-sizes 50 \\\n        --output-dir /root/structfuse/results/stratified/per_query \\\n        --tag qwen_random_s42\n\n    # Dry-run (no GPU):\n    python evaluate_stratified.py --dry-run \\\n        --val-file /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl \\\n        --output-dir /root/structfuse/results/stratified/per_query \\\n        --tag dryrun_random_s42\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport random\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\n\n\ndef _extract_instance_id(query_id: str) -> str:\n    return query_id.split(\"::\")[0]\n\n\ndef _load_val_data(val_path: str) -> list:\n    samples = []\n    with open(val_path) as f:\n        for line in f:\n            if line.strip():\n                samples.append(json.loads(line))\n    return samples\n\n\ndef _build_global_pool(samples: list) -> dict:\n    pool = {}\n    for s in samples:\n        ct = s.get(\"candidate_tokens\", {})\n        for cid, text in ct.items():\n            if text and cid not in pool:\n                pool[cid] = text\n        pid = s.get(\"pos_id\")\n        pt = s.get(\"pos_tokens\")\n        if pid and pt:\n            pool[pid] = pt\n    return pool\n\n\ndef evaluate_real(samples, global_pool, global_ids, ckpt_dir, model_name,\n                  device, max_seq_len, pool_size, eval_seed):\n    import torch\n    import torch.nn.functional as F\n    from transformers import AutoTokenizer\n\n    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / \"training\"))\n    from contrastive_model import StructFuseEncoder\n\n    tokenizer = AutoTokenizer.from_pretrained(ckpt_dir, trust_remote_code=True)\n    config_path = Path(ckpt_dir) / \"training_config.json\"\n    with open(config_path) as f:\n        cfg = json.load(f)\n\n    model = StructFuseEncoder(\n        model_name=model_name,\n        proj_dim=cfg.get(\"proj_dim\", 256),\n        use_lora=cfg.get(\"use_lora\", True),\n        lora_r=cfg.get(\"lora_r\", 16),\n        use_fusion_head=cfg.get(\"use_fusion_head\", False),\n    )\n    state_dict = torch.load(Path(ckpt_dir) / \"model.pt\", map_location=\"cpu\")\n    result = model.load_state_dict(state_dict, strict=False)\n    assert not result.missing_keys, f\"Missing keys: {result.missing_keys}\"\n    model = model.to(device).eval()\n\n    def encode_batch(texts, batch_size=16):\n        all_embs = []\n        for i in range(0, len(texts), batch_size):\n            bt = texts[i:i+batch_size]\n            enc = tokenizer(bt, truncation=True, max_length=max_seq_len,\n                            padding=True, return_tensors=\"pt\")\n            enc = {k: v.to(device) for k, v in enc.items()}\n            with torch.no_grad():\n                emb = model.encode(enc[\"input_ids\"], enc[\"attention_mask\"])\n            all_embs.append(emb.cpu())\n        return torch.cat(all_embs, dim=0)\n\n    rng = random.Random(eval_seed)\n    results = []\n    target_negs = pool_size - 1\n\n    for idx, s in enumerate(samples):\n        query_id = s.get(\"query_id\", \"\")\n        query_text = s[\"query_tokens\"]\n        pos_text = s[\"pos_tokens\"]\n        pos_id = s.get(\"pos_id\", \"\")\n\n        cand_ids = s.get(\"neg_candidates\", [])\n        cand_tokens = s.get(\"candidate_tokens\", {})\n        neg_texts = [(cid, cand_tokens[cid]) for cid in cand_ids\n                     if cid in cand_tokens and cand_tokens[cid]]\n\n        if len(neg_texts) < target_negs:\n            used = {cid for cid, _ in neg_texts} | {pos_id, query_id}\n            avail = [g for g in global_ids if g not in used]\n            rng.shuffle(avail)\n            for gid in avail:\n                if len(neg_texts) >= target_negs:\n                    break\n                neg_texts.append((gid, global_pool[gid]))\n\n        if len(neg_texts) > target_negs:\n            rng.shuffle(neg_texts)\n            neg_texts = neg_texts[:target_negs]\n\n        if not neg_texts:\n            continue\n\n        pool_texts = [pos_text] + [t for _, t in neg_texts]\n        query_emb = encode_batch([query_text])\n        pool_embs = encode_batch(pool_texts)\n\n        sims = F.cosine_similarity(query_emb, pool_embs, dim=1)\n        ranking = sims.argsort(descending=True)\n        gold_rank = (ranking == 0).nonzero(as_tuple=True)[0].item()\n\n        query_pos_sim = float(sims[0])\n        neg_sims = sims[1:].numpy()\n\n        results.append({\n            \"query_id\": query_id,\n            \"instance_id\": _extract_instance_id(query_id),\n            \"gold_rank\": gold_rank,\n            \"pool_size\": len(pool_texts),\n            \"query_pos_sim\": round(query_pos_sim, 6),\n            \"mean_neg_sim\": round(float(neg_sims.mean()), 6) if len(neg_sims) > 0 else 0.0,\n            \"max_neg_sim\": round(float(neg_sims.max()), 6) if len(neg_sims) > 0 else 0.0,\n            \"hit_at_1\": gold_rank < 1,\n            \"hit_at_5\": gold_rank < 5,\n            \"hit_at_10\": gold_rank < 10,\n        })\n\n        if (idx + 1) % 200 == 0:\n            r1_so_far = sum(r[\"hit_at_1\"] for r in results) / len(results)\n            print(f\"  [{idx+1}/{len(samples)}] running R@1={r1_so_far:.4f}\", flush=True)\n\n    return results\n\n\ndef evaluate_dryrun(samples, pool_size, eval_seed):\n    rng = np.random.RandomState(eval_seed)\n    results = []\n    for s in samples:\n        query_id = s.get(\"query_id\", \"\")\n        n_negs = min(len(s.get(\"neg_candidates\", [])), pool_size - 1)\n        if n_negs < 1:\n            n_negs = pool_size - 1\n        actual_pool = n_negs + 1\n\n        gold_rank = rng.choice(actual_pool)\n        qp_sim = rng.normal(0.6, 0.15)\n        mn_sim = rng.normal(0.35, 0.1)\n\n        results.append({\n            \"query_id\": query_id,\n            \"instance_id\": _extract_instance_id(query_id),\n            \"gold_rank\": int(gold_rank),\n            \"pool_size\": actual_pool,\n            \"query_pos_sim\": round(float(np.clip(qp_sim, -1, 1)), 6),\n            \"mean_neg_sim\": round(float(np.clip(mn_sim, -1, 1)), 6),\n            \"max_neg_sim\": round(float(np.clip(mn_sim + 0.15, -1, 1)), 6),\n            \"hit_at_1\": int(gold_rank) < 1,\n            \"hit_at_5\": int(gold_rank) < 5,\n            \"hit_at_10\": int(gold_rank) < 10,\n        })\n    return results\n\n\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument(\"--ckpt-dir\", default=None)\n    parser.add_argument(\"--model-name\", default=None)\n    parser.add_argument(\"--val-file\", required=True)\n    parser.add_argument(\"--pool-sizes\", default=\"50\", help=\"Comma-separated pool sizes\")\n    parser.add_argument(\"--output-dir\", required=True)\n    parser.add_argument(\"--tag\", required=True, help=\"e.g., qwen_random_s42\")\n    parser.add_argument(\"--max-seq-length\", type=int, default=2048)\n    parser.add_argument(\"--device\", default=\"cuda:0\")\n    parser.add_argument(\"--eval-seed\", type=int, default=42)\n    parser.add_argument(\"--dry-run\", action=\"store_true\")\n    args = parser.parse_args()\n\n    pool_sizes = [int(x) for x in args.pool_sizes.split(\",\")]\n    print(f\"Loading val data from {args.val_file}\", flush=True)\n    samples = _load_val_data(args.val_file)\n    print(f\"  {len(samples)} samples loaded\", flush=True)\n\n    if not args.dry_run:\n        global_pool = _build_global_pool(samples)\n        global_ids = list(global_pool.keys())\n        print(f\"  global distractor pool: {len(global_ids)} files\", flush=True)\n\n    out_dir = Path(args.output_dir)\n    out_dir.mkdir(parents=True, exist_ok=True)\n\n    for ps in pool_sizes:\n        print(f\"\\n{'='*50}\", flush=True)\n        print(f\"Evaluating pool_size={ps} tag={args.tag} {'[DRY-RUN]' if args.dry_run else ''}\", flush=True)\n        print(f\"{'='*50}\", flush=True)\n\n        if args.dry_run:\n            results = evaluate_dryrun(samples, ps, args.eval_seed)\n        else:\n            results = evaluate_real(\n                samples, global_pool, global_ids,\n                args.ckpt_dir, args.model_name, args.device,\n                args.max_seq_length, ps, args.eval_seed,\n            )\n\n        total = len(results)\n        r1 = sum(r[\"hit_at_1\"] for r in results) / max(total, 1)\n        r5 = sum(r[\"hit_at_5\"] for r in results) / max(total, 1)\n        r10 = sum(r[\"hit_at_10\"] for r in results) / max(total, 1)\n\n        print(f\"\\nAggregate: R@1={r1:.4f} R@5={r5:.4f} R@10={r10:.4f} (n={total})\", flush=True)\n\n        out_path = out_dir / f\"per_query_{args.tag}_p{ps}.jsonl\"\n        with open(out_path, \"w\") as f:\n            for r in results:\n                f.write(json.dumps(r, ensure_ascii=False) + \"\\n\")\n        print(f\"Saved: {out_path}\", flush=True)\n\n        summary = {\n            \"tag\": args.tag,\n            \"pool_size\": ps,\n            \"total\": total,\n            \"recall_at_1\": round(r1, 4),\n            \"recall_at_5\": round(r5, 4),\n            \"recall_at_10\": round(r10, 4),\n            \"dry_run\": args.dry_run,\n        }\n        sum_path = out_dir / f\"summary_{args.tag}_p{ps}.json\"\n        with open(sum_path, \"w\") as f:\n            json.dump(summary, f, indent=2)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"evaluate_stratified.py written OK\"", "account": "root"}}
64	{"ts": "2026-05-15T05:09:54.789503+00:00", "role": "tool_result", "session": "worker_code_plan005-stratified-prep_20260515T050005", "text": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"evaluate_stratified.py written OK\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}", "tool": "mcp__agent-ml-research__ssh_execute", "elapsed_ms": 0}
65	{"ts": "2026-05-15T05:09:54.789730+00:00", "role": "tool", "session": "worker_code_plan005-stratified-prep_20260515T050005", "text": "called mcp__agent-ml-research__ssh_execute", "tool": "mcp__agent-ml-research__ssh_execute", "tool_args": {"server": "bjb1-42106", "command": "cat > /root/structfuse/scripts/analyze_stratified.py << 'PYEOF'\n\"\"\"Stratified analysis of M2 results (plan_005).\n\nJoins per-query eval results with M1 metadata, groups by 5 stratification\ndimensions, and computes per-stratum R@1 deltas with bootstrap CIs.\n\n5 strata:\n  1. Repo size (small/medium/large)\n  2. Actual eval pool size (quartiles)\n  3. Query-positive similarity (quartiles)\n  4. Structural data availability (has_structural / no_structural)\n  5. Negative difficulty (quartiles of mean_neg_sim)\n\nOutputs: JSON summary, CSV table, PDF plots.\n\nUsage:\n    python analyze_stratified.py \\\n        --results-dir /root/structfuse/results/stratified/per_query \\\n        --index-file /root/autodl-tmp/structfuse/stratification_index.json \\\n        --strategies random,embedding_distance,dataflow_aware \\\n        --encoder qwen --seeds 42,43,44 --pool-size 50 \\\n        --output-dir /root/structfuse/results/stratified\n\n    # Dry-run (uses whatever per_query files exist, or generates mock):\n    python analyze_stratified.py --dry-run \\\n        --output-dir /root/structfuse/results/stratified\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport sys\nfrom collections import defaultdict\nfrom pathlib import Path\n\nimport numpy as np\n\nREPO_SIZE_BINS = {\n    \"small (<50)\": (0, 50),\n    \"medium (50-200)\": (50, 201),\n    \"large (200+)\": (201, float(\"inf\")),\n}\n\n\ndef load_per_query(results_dir, encoder, strategy, seed, pool_size):\n    tag = f\"{encoder}_{strategy}_s{seed}\"\n    path = Path(results_dir) / f\"per_query_{tag}_p{pool_size}.jsonl\"\n    if not path.exists():\n        return None\n    records = []\n    with open(path) as f:\n        for line in f:\n            if line.strip():\n                records.append(json.loads(line))\n    return records\n\n\ndef load_index(index_path):\n    with open(index_path) as f:\n        return json.load(f)\n\n\ndef quartile_bins(values):\n    if not values:\n        return {}\n    arr = np.array(values)\n    q25, q50, q75 = np.percentile(arr, [25, 50, 75])\n    return {\n        \"Q1 (lowest)\": (float(\"-inf\"), q25),\n        \"Q2\": (q25, q50),\n        \"Q3\": (q50, q75),\n        \"Q4 (highest)\": (q75, float(\"inf\")),\n    }\n\n\ndef assign_bin(val, bins):\n    for name, (lo, hi) in bins.items():\n        if lo <= val < hi:\n            return name\n    return list(bins.keys())[-1]\n\n\ndef bootstrap_ci(values, n_boot=2000, ci=0.95, seed=42):\n    rng = np.random.RandomState(seed)\n    arr = np.array(values, dtype=float)\n    n = len(arr)\n    if n < 2:\n        m = float(arr.mean()) if n > 0 else 0.0\n        return {\"mean\": m, \"ci_lower\": m, \"ci_upper\": m, \"n\": n}\n    means = np.array([rng.choice(arr, size=n, replace=True).mean() for _ in range(n_boot)])\n    alpha = (1 - ci) / 2\n    lo, hi = np.percentile(means, [100 * alpha, 100 * (1 - alpha)])\n    return {\n        \"mean\": round(float(arr.mean()), 6),\n        \"ci_lower\": round(float(lo), 6),\n        \"ci_upper\": round(float(hi), 6),\n        \"n\": n,\n    }\n\n\ndef compute_stratum_metrics(records, strategies, baseline=\"random\"):\n    per_strategy = defaultdict(list)\n    for r in records:\n        per_strategy[r[\"strategy\"]].append(r[\"hit_at_1\"])\n\n    result = {}\n    for s in strategies:\n        vals = per_strategy.get(s, [])\n        result[s] = bootstrap_ci(vals)\n\n    if baseline in result and result[baseline][\"n\"] > 0:\n        base_mean = result[baseline][\"mean\"]\n        for s in strategies:\n            if s != baseline and s in result:\n                result[f\"delta_{s}_vs_{baseline}\"] = round(\n                    result[s][\"mean\"] - base_mean, 6)\n\n    return result\n\n\ndef run_analysis(all_records, index, strategies, baseline=\"random\"):\n    inst_meta = index.get(\"instances\", {})\n\n    for r in all_records:\n        iid = r[\"instance_id\"]\n        meta = inst_meta.get(iid, {})\n        r[\"repo\"] = meta.get(\"repo\", \"unknown\")\n        r[\"repo_file_count\"] = meta.get(\"repo_file_count\", 0)\n        r[\"has_structural\"] = meta.get(\"has_structural\", False)\n        r[\"has_z\"] = meta.get(\"has_z\", False)\n        r[\"extraction_method\"] = meta.get(\"extraction_method\", \"none\")\n\n    # Compute quartile bins from data\n    pool_sizes = [r[\"pool_size\"] for r in all_records]\n    qp_sims = [r[\"query_pos_sim\"] for r in all_records]\n    neg_diffs = [r[\"mean_neg_sim\"] for r in all_records]\n\n    pool_bins = quartile_bins(pool_sizes)\n    sim_bins = quartile_bins(qp_sims)\n    diff_bins = quartile_bins(neg_diffs)\n\n    strata_defs = {\n        \"repo_size\": {\n            \"field\": \"repo_file_count\",\n            \"bins\": REPO_SIZE_BINS,\n            \"type\": \"fixed\",\n        },\n        \"pool_size\": {\n            \"field\": \"pool_size\",\n            \"bins\": pool_bins,\n            \"type\": \"quartile\",\n        },\n        \"query_pos_similarity\": {\n            \"field\": \"query_pos_sim\",\n            \"bins\": sim_bins,\n            \"type\": \"quartile\",\n        },\n        \"structural_availability\": {\n            \"field\": \"has_structural\",\n            \"bins\": {\"with_structural\": True, \"no_structural\": False},\n            \"type\": \"binary\",\n        },\n        \"neg_difficulty\": {\n            \"field\": \"mean_neg_sim\",\n            \"bins\": diff_bins,\n            \"type\": \"quartile\",\n        },\n    }\n\n    results = {}\n    for dim_name, dim_def in strata_defs.items():\n        dim_results = {}\n        field = dim_def[\"field\"]\n        bins = dim_def[\"bins\"]\n        dim_type = dim_def[\"type\"]\n\n        if dim_type == \"binary\":\n            grouped = defaultdict(list)\n            for r in all_records:\n                val = r.get(field, False)\n                for bname, bval in bins.items():\n                    if val == bval:\n                        grouped[bname].append(r)\n                        break\n        else:\n            grouped = defaultdict(list)\n            for r in all_records:\n                val = r.get(field, 0)\n                bname = assign_bin(val, bins)\n                grouped[bname].append(r)\n\n        for bname, brecs in sorted(grouped.items()):\n            metrics = compute_stratum_metrics(brecs, strategies, baseline)\n            metrics[\"count\"] = len(brecs)\n            dim_results[bname] = metrics\n\n        # Weighted aggregate delta\n        total_n = sum(m[\"count\"] for m in dim_results.values())\n        for s in strategies:\n            if s == baseline:\n                continue\n            delta_key = f\"delta_{s}_vs_{baseline}\"\n            weighted_sum = 0\n            for bname, m in dim_results.items():\n                d = m.get(delta_key, 0) or 0\n                w = m[\"count\"] / max(total_n, 1)\n                weighted_sum += d * w\n            dim_results[f\"weighted_{delta_key}\"] = round(weighted_sum, 6)\n\n        results[dim_name] = {\n            \"bins\": {k: str(v) for k, v in bins.items()},\n            \"strata\": dim_results,\n        }\n\n    return results\n\n\ndef generate_csv(results, output_path):\n    lines = [\"dimension,stratum,count,strategy,r@1_mean,r@1_ci_lower,r@1_ci_upper\"]\n    for dim, data in results.items():\n        for bname, metrics in data[\"strata\"].items():\n            if isinstance(metrics, dict) and \"count\" in metrics:\n                count = metrics[\"count\"]\n                for key, val in metrics.items():\n                    if isinstance(val, dict) and \"mean\" in val:\n                        lines.append(\n                            f\"{dim},{bname},{count},{key},\"\n                            f\"{val['mean']:.4f},{val['ci_lower']:.4f},{val['ci_upper']:.4f}\"\n                        )\n    with open(output_path, \"w\") as f:\n        f.write(\"\\n\".join(lines) + \"\\n\")\n\n\ndef generate_plots(results, strategies, baseline, output_dir):\n    try:\n        import matplotlib\n        matplotlib.use(\"Agg\")\n        import matplotlib.pyplot as plt\n    except ImportError:\n        print(\"WARNING: matplotlib not available, skipping plots\", flush=True)\n        return\n\n    for dim, data in results.items():\n        strata = data[\"strata\"]\n        bin_names = [b for b in strata if isinstance(strata[b], dict) and \"count\" in strata[b]]\n        if not bin_names:\n            continue\n\n        fig, axes = plt.subplots(1, 2, figsize=(14, 5))\n\n        # Left: R@1 per strategy per stratum\n        ax = axes[0]\n        x = np.arange(len(bin_names))\n        width = 0.8 / len(strategies)\n        for i, s in enumerate(strategies):\n            means = []\n            errs_lo = []\n            errs_hi = []\n            for b in bin_names:\n                m = strata[b].get(s, {})\n                mean = m.get(\"mean\", 0)\n                ci_lo = m.get(\"ci_lower\", mean)\n                ci_hi = m.get(\"ci_upper\", mean)\n                means.append(mean)\n                errs_lo.append(mean - ci_lo)\n                errs_hi.append(ci_hi - mean)\n            ax.bar(x + i * width, means, width, label=s,\n                   yerr=[errs_lo, errs_hi], capsize=3)\n        ax.set_xticks(x + width * (len(strategies) - 1) / 2)\n        ax.set_xticklabels(bin_names, rotation=30, ha=\"right\", fontsize=8)\n        ax.set_ylabel(\"R@1\")\n        ax.set_title(f\"R@1 by {dim}\")\n        ax.legend(fontsize=7)\n\n        # Right: Delta vs baseline per stratum\n        ax = axes[1]\n        for i, s in enumerate(strategies):\n            if s == baseline:\n                continue\n            deltas = []\n            for b in bin_names:\n                dk = f\"delta_{s}_vs_{baseline}\"\n                deltas.append(strata[b].get(dk, 0) or 0)\n            ax.bar(x + i * width, deltas, width, label=f\"{s} - {baseline}\")\n        ax.axhline(0, color=\"black\", linewidth=0.5)\n        ax.set_xticks(x + width * (len(strategies) - 1) / 2)\n        ax.set_xticklabels(bin_names, rotation=30, ha=\"right\", fontsize=8)\n        ax.set_ylabel(\"Delta R@1\")\n        ax.set_title(f\"Delta vs {baseline} by {dim}\")\n        ax.legend(fontsize=7)\n\n        plt.tight_layout()\n        fig_path = Path(output_dir) / f\"stratified_{dim}.pdf\"\n        plt.savefig(fig_path, dpi=150, bbox_inches=\"tight\")\n        plt.close()\n        print(f\"  Plot saved: {fig_path}\", flush=True)\n\n\ndef generate_dryrun_data(results_dir, strategies, seeds, pool_size, n_queries=500):\n    rng = np.random.RandomState(2026)\n    Path(results_dir).mkdir(parents=True, exist_ok=True)\n\n    repos = [f\"repo_{i}\" for i in range(20)]\n    for strategy in strategies:\n        for seed in seeds:\n            tag = f\"dryrun_{strategy}_s{seed}\"\n            path = Path(results_dir) / f\"per_query_{tag}_p{pool_size}.jsonl\"\n            if path.exists():\n                continue\n\n            base_r1 = {\"random\": 0.42, \"embedding_distance\": 0.48,\n                       \"dataflow_aware\": 0.51, \"bm25\": 0.45}\n            p_hit = base_r1.get(strategy, 0.45) + rng.normal(0, 0.02)\n\n            with open(path, \"w\") as f:\n                for i in range(n_queries):\n                    repo = rng.choice(repos)\n                    iid = f\"{repo}.{rng.randint(1000, 9999)}.func__{i:04d}\"\n                    hit = rng.random() < p_hit\n                    gold_rank = 0 if hit else rng.randint(1, pool_size)\n                    rec = {\n                        \"query_id\": f\"{iid}::src/file_{i}.py\",\n                        \"instance_id\": iid,\n                        \"gold_rank\": int(gold_rank),\n                        \"pool_size\": pool_size,\n                        \"query_pos_sim\": round(float(rng.normal(0.6, 0.15)), 6),\n                        \"mean_neg_sim\": round(float(rng.normal(0.35, 0.1)), 6),\n                        \"max_neg_sim\": round(float(rng.normal(0.5, 0.1)), 6),\n                        \"hit_at_1\": hit,\n                        \"hit_at_5\": int(gold_rank) < 5,\n                        \"hit_at_10\": int(gold_rank) < 10,\n                    }\n                    f.write(json.dumps(rec) + \"\\n\")\n\n    # Also generate mock index\n    index_path = Path(results_dir).parent / \"mock_stratification_index.json\"\n    if not index_path.exists():\n        instances = {}\n        for strategy in strategies:\n            seed = seeds[0]\n            tag = f\"dryrun_{strategy}_s{seed}\"\n            path = Path(results_dir) / f\"per_query_{tag}_p{pool_size}.jsonl\"\n            with open(path) as f2:\n                for line in f2:\n                    r = json.loads(line)\n                    iid = r[\"instance_id\"]\n                    if iid not in instances:\n                        repo = iid.split(\".\")[0]\n                        instances[iid] = {\n                            \"repo\": repo,\n                            \"repo_file_count\": rng.randint(10, 500),\n                            \"has_structural\": bool(rng.random() < 0.34),\n                            \"has_z\": bool(rng.random() < 0.78),\n                            \"extraction_method\": rng.choice([\"codeql\", \"beniget\", \"none\"]),\n                        }\n        mock_index = {\n            \"instances\": instances,\n            \"repo_stats\": {},\n            \"summary\": {\"note\": \"mock data for dry-run\"},\n        }\n        with open(index_path, \"w\") as f2:\n            json.dump(mock_index, f2, indent=1)\n        print(f\"  Mock index written: {index_path}\", flush=True)\n\n    return str(index_path)\n\n\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument(\"--results-dir\", default=None,\n                        help=\"Dir with per_query_*.jsonl files\")\n    parser.add_argument(\"--index-file\", default=None,\n                        help=\"stratification_index.json from prepare_stratification_index.py\")\n    parser.add_argument(\"--strategies\", default=\"random,embedding_distance,dataflow_aware\")\n    parser.add_argument(\"--baseline\", default=\"random\")\n    parser.add_argument(\"--encoder\", default=\"qwen\")\n    parser.add_argument(\"--seeds\", default=\"42,43,44\")\n    parser.add_argument(\"--pool-size\", type=int, default=50)\n    parser.add_argument(\"--output-dir\", required=True)\n    parser.add_argument(\"--dry-run\", action=\"store_true\")\n    parser.add_argument(\"--bootstrap-iter\", type=int, default=2000)\n    args = parser.parse_args()\n\n    strategies = args.strategies.split(\",\")\n    seeds = [int(s) for s in args.seeds.split(\",\")]\n    out_dir = Path(args.output_dir)\n    out_dir.mkdir(parents=True, exist_ok=True)\n\n    tag_prefix = \"dryrun\" if args.dry_run else args.encoder\n\n    if args.dry_run:\n        results_dir = str(out_dir / \"per_query\")\n        print(\"Generating dry-run mock data...\", flush=True)\n        index_path = generate_dryrun_data(results_dir, strategies, seeds, args.pool_size)\n    else:\n        results_dir = args.results_dir\n        index_path = args.index_file\n\n    if not results_dir or not index_path:\n        print(\"ERROR: --results-dir and --index-file required in real mode\", file=sys.stderr)\n        sys.exit(1)\n\n    print(f\"Loading index from {index_path}\", flush=True)\n    index = load_index(index_path)\n    inst_count = len(index.get(\"instances\", {}))\n    print(f\"  {inst_count} instances in index\", flush=True)\n\n    # Load all per-query results\n    all_records = []\n    loaded = 0\n    for strategy in strategies:\n        for seed in seeds:\n            tag = f\"{tag_prefix}_{strategy}_s{seed}\"\n            recs = load_per_query(results_dir, tag_prefix, strategy, seed, args.pool_size)\n            if recs is None:\n                print(f\"  WARN: missing {tag} pool={args.pool_size}\", flush=True)\n                continue\n            for r in recs:\n                r[\"strategy\"] = strategy\n                r[\"seed\"] = seed\n            all_records.extend(recs)\n            loaded += 1\n            print(f\"  Loaded {tag}: {len(recs)} queries\", flush=True)\n\n    print(f\"\\nTotal: {len(all_records)} records from {loaded} runs\", flush=True)\n\n    if not all_records:\n        print(\"ERROR: no data loaded\", file=sys.stderr)\n        sys.exit(1)\n\n    # Run analysis\n    print(\"\\nRunning stratified analysis...\", flush=True)\n    results = run_analysis(all_records, index, strategies, args.baseline)\n\n    # Print summary\n    for dim, data in results.items():\n        print(f\"\\n{'='*60}\", flush=True)\n        print(f\"Dimension: {dim}\", flush=True)\n        print(f\"{'='*60}\", flush=True)\n        strata = data[\"strata\"]\n        for bname, metrics in sorted(strata.items()):\n            if isinstance(metrics, dict) and \"count\" in metrics:\n                parts = [f\"  {bname} (n={metrics['count']})\"]\n                for s in strategies:\n                    m = metrics.get(s, {})\n                    if isinstance(m, dict) and \"mean\" in m:\n                        parts.append(f\"  {s}: {m['mean']:.4f} [{m['ci_lower']:.4f}, {m['ci_upper']:.4f}]\")\n                for s in strategies:\n                    if s != args.baseline:\n                        dk = f\"delta_{s}_vs_{args.baseline}\"\n                        d = metrics.get(dk)\n                        if d is not None:\n                            parts.append(f\"  {dk}: {d:+.4f}\")\n                print(\"\\n\".join(parts), flush=True)\n            elif isinstance(metrics, (int, float)):\n                print(f\"  {bname}: {metrics}\", flush=True)\n\n    # Save outputs\n    suffix = \"_dryrun\" if args.dry_run else \"\"\n\n    json_path = out_dir / f\"stratified_results{suffix}.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(results, f, indent=2, ensure_ascii=False)\n    print(f\"\\nJSON saved: {json_path}\", flush=True)\n\n    csv_path = out_dir / f\"stratified_results{suffix}.csv\"\n    generate_csv(results, csv_path)\n    print(f\"CSV saved: {csv_path}\", flush=True)\n\n    generate_plots(results, strategies, args.baseline, out_dir)\n\n    print(\"\\nDone.\", flush=True)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"analyze_stratified.py written OK\"", "account": "root"}}
66	{"ts": "2026-05-15T05:09:54.790023+00:00", "role": "tool_result", "session": "worker_code_plan005-stratified-prep_20260515T050005", "text": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"analyze_stratified.py written OK\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}", "tool": "mcp__agent-ml-research__ssh_execute", "elapsed_ms": 0}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e44ca124-d1be-4d6c-8848-87c010cfa608",
  "isSidechain": true,
  "promptId": "658d2eb0-8593-44d8-a0a6-011e29c3e29c",
  "agentId": "a244b0313f96edf04",
  "type": "user",
  "uuid": "8a0d9c8f-86e4-4c0d-ad36-be7b52d18c4c",
  "sourceToolAssistantUUID": "e44ca124-d1be-4d6c-8848-87c010cfa608",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "953f15f8-e655-48b5-a31c-751a817178ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-15T07:56:47.972Z_

I found both scripts in the chat log. Here are the full source codes, extracted from the `ssh_execute` tool calls on lines 63 and 65 of the JSONL file.

---

## `evaluate_stratified.py`

```python
"""Per-query evaluation for stratified analysis (plan_005).

Evaluates M2 checkpoints and records per-query results including gold rank,
cosine similarities, and pool sizes. Supports multiple pool sizes (D038).

Outputs per-query JSONL for downstream analyze_stratified.py.

Usage:
    # Real eval (GPU):
    python evaluate_stratified.py \
        --ckpt-dir /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42 \
        --model-name /root/autodl-tmp/structfuse/models/Qwen2.5-Coder-3B \
        --val-file /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl \
        --pool-sizes 50 \
        --output-dir /root/structfuse/results/stratified/per_query \
        --tag qwen_random_s42

    # Dry-run (no GPU):
    python evaluate_stratified.py --dry-run \
        --val-file /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl \
        --output-dir /root/structfuse/results/stratified/per_query \
        --tag dryrun_random_s42
"""

import argparse
import json
import os
import random
import sys
from pathlib import Path

import numpy as np


def _extract_instance_id(query_id: str) -> str:
    return query_id.split("::")[0]


def _load_val_data(val_path: str) -> list:
    samples = []
    with open(val_path) as f:
        for line in f:
            if line.strip():
                samples.append(json.loads(line))
    return samples


def _build_global_pool(samples: list) -> dict:
    pool = {}
    for s in samples:
        ct = s.get("candidate_tokens", {})
        for cid, text in ct.items():
            if text and cid not in pool:
                pool[cid] = text
        pid = s.get("pos_id")
        pt = s.get("pos_tokens")
        if pid and pt:
            pool[pid] = pt
    return pool


def evaluate_real(samples, global_pool, global_ids, ckpt_dir, model_name,
                  device, max_seq_len, pool_size, eval_seed):
    import torch
    import torch.nn.functional as F
    from transformers import AutoTokenizer

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "training"))
    from contrastive_model import StructFuseEncoder

    tokenizer = AutoTokenizer.from_pretrained(ckpt_dir, trust_remote_code=True)
    config_path = Path(ckpt_dir) / "training_config.json"
    with open(config_path) as f:
        cfg = json.load(f)

    model = StructFuseEncoder(
        model_name=model_name,
        proj_dim=cfg.get("proj_dim", 256),
        use_lora=cfg.get("use_lora", True),
        lora_r=cfg.get("lora_r", 16),
        use_fusion_head=cfg.get("use_fusion_head", False),
    )
    state_dict = torch.load(Path(ckpt_dir) / "model.pt", map_location="cpu")
    result = model.load_state_dict(state_dict, strict=False)
    assert not result.missing_keys, f"Missing keys: {result.missing_keys}"
    model = model.to(device).eval()

    def encode_batch(texts, batch_size=16):
        all_embs = []
        for i in range(0, len(texts), batch_size):
            bt = texts[i:i+batch_size]
            enc = tokenizer(bt, truncation=True, max_length=max_seq_len,
                            padding=True, return_tensors="pt")
            enc = {k: v.to(device) for k, v in enc.items()}
            with torch.no_grad():
                emb = model.encode(enc["input_ids"], enc["attention_mask"])
            all_embs.append(emb.cpu())
        return torch.cat(all_embs, dim=0)

    rng = random.Random(eval_seed)
    results = []
    target_negs = pool_size - 1

    for idx, s in enumerate(samples):
        query_id = s.get("query_id", "")
        query_text = s["query_tokens"]
        pos_text = s["pos_tokens"]
        pos_id = s.get("pos_id", "")

        cand_ids = s.get("neg_candidates", [])
        cand_tokens = s.get("candidate_tokens", {})
        neg_texts = [(cid, cand_tokens[cid]) for cid in cand_ids
                     if cid in cand_tokens and cand_tokens[cid]]

        if len(neg_texts) < target_negs:
            used = {cid for cid, _ in neg_texts} | {pos_id, query_id}
            avail = [g for g in global_ids if g not in used]
            rng.shuffle(avail)
            for gid in avail:
                if len(neg_texts) >= target_negs:
                    break
                neg_texts.append((gid, global_pool[gid]))

        if len(neg_texts) > target_negs:
            rng.shuffle(neg_texts)
            neg_texts = neg_texts[:target_negs]

        if not neg_texts:
            continue

        pool_texts = [pos_text] + [t for _, t in neg_texts]
        query_emb = encode_batch([query_text])
        pool_embs = encode_batch(pool_texts)

        sims = F.cosine_similarity(query_emb, pool_embs, dim=1)
        ranking = sims.argsort(descending=True)
        gold_rank = (ranking == 0).nonzero(as_tuple=True)[0].item()

        query_pos_sim = float(sims[0])
        neg_sims = sims[1:].numpy()

        results.append({
            "query_id": query_id,
            "instance_id": _extract_instance_id(query_id),
            "gold_rank": gold_rank,
            "pool_size": len(pool_texts),
            "query_pos_sim": round(query_pos_sim, 6),
            "mean_neg_sim": round(float(neg_sims.mean()), 6) if len(neg_sims) > 0 else 0.0,
            "max_neg_sim": round(float(neg_sims.max()), 6) if len(neg_sims) > 0 else 0.0,
            "hit_at_1": gold_rank < 1,
            "hit_at_5": gold_rank < 5,
            "hit_at_10": gold_rank < 10,
        })

        if (idx + 1) % 200 == 0:
            r1_so_far = sum(r["hit_at_1"] for r in results) / len(results)
            print(f"  [{idx+1}/{len(samples)}] running R@1={r1_so_far:.4f}", flush=True)

    return results


def evaluate_dryrun(samples, pool_size, eval_seed):
    rng = np.random.RandomState(eval_seed)
    results = []
    for s in samples:
        query_id = s.get("query_id", "")
        n_negs = min(len(s.get("neg_candidates", [])), pool_size - 1)
        if n_negs < 1:
            n_negs = pool_size - 1
        actual_pool = n_negs + 1

        gold_rank = rng.choice(actual_pool)
        qp_sim = rng.normal(0.6, 0.15)
        mn_sim = rng.normal(0.35, 0.1)

        results.append({
            "query_id": query_id,
            "instance_id": _extract_instance_id(query_id),
            "gold_rank": int(gold_rank),
            "pool_size": actual_pool,
            "query_pos_sim": round(float(np.clip(qp_sim, -1, 1)), 6),
            "mean_neg_sim": round(float(np.clip(mn_sim, -1, 1)), 6),
            "max_neg_sim": round(float(np.clip(mn_sim + 0.15, -1, 1)), 6),
            "hit_at_1": int(gold_rank) < 1,
            "hit_at_5": int(gold_rank) < 5,
            "hit_at_10": int(gold_rank) < 10,
        })
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckpt-dir", default=None)
    parser.add_argument("--model-name", default=None)
    parser.add_argument("--val-file", required=True)
    parser.add_argument("--pool-sizes", default="50", help="Comma-separated pool sizes")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--tag", required=True, help="e.g., qwen_random_s42")
    parser.add_argument("--max-seq-length", type=int, default=2048)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--eval-seed", type=int, default=42)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    pool_sizes = [int(x) for x in args.pool_sizes.split(",")]
    print(f"Loading val data from {args.val_file}", flush=True)
    samples = _load_val_data(args.val_file)
    print(f"  {len(samples)} samples loaded", flush=True)

    if not args.dry_run:
        global_pool = _build_global_pool(samples)
        global_ids = list(global_pool.keys())
        print(f"  global distractor pool: {len(global_ids)} files", flush=True)

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    for ps in pool_sizes:
        print(f"\n{'='*50}", flush=True)
        print(f"Evaluating pool_size={ps} tag={args.tag} {'[DRY-RUN]' if args.dry_run else ''}", flush=True)
        print(f"{'='*50}", flush=True)

        if args.dry_run:
            results = evaluate_dryrun(samples, ps, args.eval_seed)
        else:
            results = evaluate_real(
                samples, global_pool, global_ids,
                args.ckpt_dir, args.model_name, args.device,
                args.max_seq_length, ps, args.eval_seed,
            )

        total = len(results)
        r1 = sum(r["hit_at_1"] for r in results) / max(total, 1)
        r5 = sum(r["hit_at_5"] for r in results) / max(total, 1)
        r10 = sum(r["hit_at_10"] for r in results) / max(total, 1)

        print(f"\nAggregate: R@1={r1:.4f} R@5={r5:.4f} R@10={r10:.4f} (n={total})", flush=True)

        out_path = out_dir / f"per_query_{args.tag}_p{ps}.jsonl"
        with open(out_path, "w") as f:
            for r in results:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"Saved: {out_path}", flush=True)

        summary = {
            "tag": args.tag,
            "pool_size": ps,
            "total": total,
            "recall_at_1": round(r1, 4),
            "recall_at_5": round(r5, 4),
            "recall_at_10": round(r10, 4),
            "dry_run": args.dry_run,
        }
        sum_path = out_dir / f"summary_{args.tag}_p{ps}.json"
        with open(sum_path, "w") as f:
            json.dump(summary, f, indent=2)


if __name__ == "__main__":
    main()
```

---

## `analyze_stratified.py`

```python
"""Stratified analysis of M2 results (plan_005).

Joins per-query eval results with M1 metadata, groups by 5 stratification
dimensions, and computes per-stratum R@1 deltas with bootstrap CIs.

5 strata:
  1. Repo size (small/medium/large)
  2. Actual eval pool size (quartiles)
  3. Query-positive similarity (quartiles)
  4. Structural data availability (has_structural / no_structural)
  5. Negative difficulty (quartiles of mean_neg_sim)

Outputs: JSON summary, CSV table, PDF plots.

Usage:
    python analyze_stratified.py \
        --results-dir /root/structfuse/results/stratified/per_query \
        --index-file /root/autodl-tmp/structfuse/stratification_index.json \
        --strategies random,embedding_distance,dataflow_aware \
        --encoder qwen --seeds 42,43,44 --pool-size 50 \
        --output-dir /root/structfuse/results/stratified

    # Dry-run (uses whatever per_query files exist, or generates mock):
    python analyze_stratified.py --dry-run \
        --output-dir /root/structfuse/results/stratified
"""

import argparse
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

REPO_SIZE_BINS = {
    "small (<50)": (0, 50),
    "medium (50-200)": (50, 201),
    "large (200+)": (201, float("inf")),
}


def load_per_query(results_dir, encoder, strategy, seed, pool_size):
    tag = f"{encoder}_{strategy}_s{seed}"
    path = Path(results_dir) / f"per_query_{tag}_p{pool_size}.jsonl"
    if not path.exists():
        return None
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return records


def load_index(index_path):
    with open(index_path) as f:
        return json.load(f)


def quartile_bins(values):
    if not values:
        return {}
    arr = np.array(values)
    q25, q50, q75 = np.percentile(arr, [25, 50, 75])
    return {
        "Q1 (lowest)": (float("-inf"), q25),
        "Q2": (q25, q50),
        "Q3": (q50, q75),
        "Q4 (highest)": (q75, float("inf")),
    }


def assign_bin(val, bins):
    for name, (lo, hi) in bins.items():
        if lo <= val < hi:
            return name
    return list(bins.keys())[-1]


def bootstrap_ci(values, n_boot=2000, ci=0.95, seed=42):
    rng = np.random.RandomState(seed)
    arr = np.array(values, dtype=float)
    n = len(arr)
    if n < 2:
        m = float(arr.mean()) if n > 0 else 0.0
        return {"mean": m, "ci_lower": m, "ci_upper": m, "n": n}
    means = np.array([rng.choice(arr, size=n, replace=True).mean() for _ in range(n_boot)])
    alpha = (1 - ci) / 2
    lo, hi = np.percentile(means, [100 * alpha, 100 * (1 - alpha)])
    return {
        "mean": round(float(arr.mean()), 6),
        "ci_lower": round(float(lo), 6),
        "ci_upper": round(float(hi), 6),
        "n": n,
    }


def compute_stratum_metrics(records, strategies, baseline="random"):
    per_strategy = defaultdict(list)
    for r in records:
        per_strategy[r["strategy"]].append(r["hit_at_1"])

    result = {}
    for s in strategies:
        vals = per_strategy.get(s, [])
        result[s] = bootstrap_ci(vals)

    if baseline in result and result[baseline]["n"] > 0:
        base_mean = result[baseline]["mean"]
        for s in strategies:
            if s != baseline and s in result:
                result[f"delta_{s}_vs_{baseline}"] = round(
                    result[s]["mean"] - base_mean, 6)

    return result


def run_analysis(all_records, index, strategies, baseline="random"):
    inst_meta = index.get("instances", {})

    for r in all_records:
        iid = r["instance_id"]
        meta = inst_meta.get(iid, {})
        r["repo"] = meta.get("repo", "unknown")
        r["repo_file_count"] = meta.get("repo_file_count", 0)
        r["has_structural"] = meta.get("has_structural", False)
        r["has_z"] = meta.get("has_z", False)
        r["extraction_method"] = meta.get("extraction_method", "none")

    # Compute quartile bins from data
    pool_sizes = [r["pool_size"] for r in all_records]
    qp_sims = [r["query_pos_sim"] for r in all_records]
    neg_diffs = [r["mean_neg_sim"] for r in all_records]

    pool_bins = quartile_bins(pool_sizes)
    sim_bins = quartile_bins(qp_sims)
    diff_bins = quartile_bins(neg_diffs)

    strata_defs = {
        "repo_size": {
            "field": "repo_file_count",
            "bins": REPO_SIZE_BINS,
            "type": "fixed",
        },
        "pool_size": {
            "field": "pool_size",
            "bins": pool_bins,
            "type": "quartile",
        },
        "query_pos_similarity": {
            "field": "query_pos_sim",
            "bins": sim_bins,
            "type": "quartile",
        },
        "structural_availability": {
            "field": "has_structural",
            "bins": {"with_structural": True, "no_structural": False},
            "type": "binary",
        },
        "neg_difficulty": {
            "field": "mean_neg_sim",
            "bins": diff_bins,
            "type": "quartile",
        },
    }

    results = {}
    for dim_name, dim_def in strata_defs.items():
        dim_results = {}
        field = dim_def["field"]
        bins = dim_def["bins"]
        dim_type = dim_def["type"]

        if dim_type == "binary":
            grouped = defaultdict(list)
            for r in all_records:
                val = r.get(field, False)
                for bname, bval in bins.items():
                    if val == bval:
                        grouped[bname].append(r)
                        break
        else:
            grouped = defaultdict(list)
            for r in all_records:
                val = r.get(field, 0)
                bname = assign_bin(val, bins)
                grouped[bname].append(r)

        for bname, brecs in sorted(grouped.items()):
            metrics = compute_stratum_metrics(brecs, strategies, baseline)
            metrics["count"] = len(brecs)
            dim_results[bname] = metrics

        # Weighted aggregate delta
        total_n = sum(m["count"] for m in dim_results.values())
        for s in strategies:
            if s == baseline:
                continue
            delta_key = f"delta_{s}_vs_{baseline}"
            weighted_sum = 0
            for bname, m in dim_results.items():
                d = m.get(delta_key, 0) or 0
                w = m["count"] / max(total_n, 1)
                weighted_sum += d * w
            dim_results[f"weighted_{delta_key}"] = round(weighted_sum, 6)

        results[dim_name] = {
            "bins": {k: str(v) for k, v in bins.items()},
            "strata": dim_results,
        }

    return results


def generate_csv(results, output_path):
    lines = ["dimension,stratum,count,strategy,r@1_mean,r@1_ci_lower,r@1_ci_upper"]
    for dim, data in results.items():
        for bname, metrics in data["strata"].items():
            if isinstance(metrics, dict) and "count" in metrics:
                count = metrics["count"]
                for key, val in metrics.items():
                    if isinstance(val, dict) and "mean" in val:
                        lines.append(
                            f"{dim},{bname},{count},{key},"
                            f"{val['mean']:.4f},{val['ci_lower']:.4f},{val['ci_upper']:.4f}"
                        )
    with open(output_path, "w") as f:
        f.write("\n".join(lines) + "\n")


def generate_plots(results, strategies, baseline, output_dir):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("WARNING: matplotlib not available, skipping plots", flush=True)
        return

    for dim, data in results.items():
        strata = data["strata"]
        bin_names = [b for b in strata if isinstance(strata[b], dict) and "count" in strata[b]]
        if not bin_names:
            continue

        fig, axes = plt.subplots(1, 2, figsize=(14, 5))

        # Left: R@1 per strategy per stratum
        ax = axes[0]
        x = np.arange(len(bin_names))
        width = 0.8 / len(strategies)
        for i, s in enumerate(strategies):
            means = []
            errs_lo = []
            errs_hi = []
            for b in bin_names:
                m = strata[b].get(s, {})
                mean = m.get("mean", 0)
                ci_lo = m.get("ci_lower", mean)
                ci_hi = m.get("ci_upper", mean)
                means.append(mean)
                errs_lo.append(mean - ci_lo)
                errs_hi.append(ci_hi - mean)
            ax.bar(x + i * width, means, width, label=s,
                   yerr=[errs_lo, errs_hi], capsize=3)
        ax.set_xticks(x + width * (len(strategies) - 1) / 2)
        ax.set_xticklabels(bin_names, rotation=30, ha="right", fontsize=8)
        ax.set_ylabel("R@1")
        ax.set_title(f"R@1 by {dim}")
        ax.legend(fontsize=7)

        # Right: Delta vs baseline per stratum
        ax = axes[1]
        for i, s in enumerate(strategies):
            if s == baseline:
                continue
            deltas = []
            for b in bin_names:
                dk = f"delta_{s}_vs_{baseline}"
                deltas.append(strata[b].get(dk, 0) or 0)
            ax.bar(x + i * width, deltas, width, label=f"{s} - {baseline}")
        ax.axhline(0, color="black", linewidth=0.5)
        ax.set_xticks(x + width * (len(strategies) - 1) / 2)
        ax.set_xticklabels(bin_names, rotation=30, ha="right", fontsize=8)
        ax.set_ylabel("Delta R@1")
        ax.set_title(f"Delta vs {baseline} by {dim}")
        ax.legend(fontsize=7)

        plt.tight_layout()
        fig_path = Path(output_dir) / f"stratified_{dim}.pdf"
        plt.savefig(fig_path, dpi=150, bbox_inches="tight")
        plt.close()
        print(f"  Plot saved: {fig_path}", flush=True)


def generate_dryrun_data(results_dir, strategies, seeds, pool_size, n_queries=500):
    rng = np.random.RandomState(2026)
    Path(results_dir).mkdir(parents=True, exist_ok=True)

    repos = [f"repo_{i}" for i in range(20)]
    for strategy in strategies:
        for seed in seeds:
            tag = f"dryrun_{strategy}_s{seed}"
            path = Path(results_dir) / f"per_query_{tag}_p{pool_size}.jsonl"
            if path.exists():
                continue

            base_r1 = {"random": 0.42, "embedding_distance": 0.48,
                       "dataflow_aware": 0.51, "bm25": 0.45}
            p_hit = base_r1.get(strategy, 0.45) + rng.normal(0, 0.02)

            with open(path, "w") as f:
                for i in range(n_queries):
                    repo = rng.choice(repos)
                    iid = f"{repo}.{rng.randint(1000, 9999)}.func__{i:04d}"
                    hit = rng.random() < p_hit
                    gold_rank = 0 if hit else rng.randint(1, pool_size)
                    rec = {
                        "query_id": f"{iid}::src/file_{i}.py",
                        "instance_id": iid,
                        "gold_rank": int(gold_rank),
                        "pool_size": pool_size,
                        "query_pos_sim": round(float(rng.normal(0.6, 0.15)), 6),
                        "mean_neg_sim": round(float(rng.normal(0.35, 0.1)), 6),
                        "max_neg_sim": round(float(rng.normal(0.5, 0.1)), 6),
                        "hit_at_1": hit,
                        "hit_at_5": int(gold_rank) < 5,
                        "hit_at_10": int(gold_rank) < 10,
                    }
                    f.write(json.dumps(rec) + "\n")

    # Also generate mock index
    index_path = Path(results_dir).parent / "mock_stratification_index.json"
    if not index_path.exists():
        instances = {}
        for strategy in strategies:
            seed = seeds[0]
            tag = f"dryrun_{strategy}_s{seed}"
            path = Path(results_dir) / f"per_query_{tag}_p{pool_size}.jsonl"
            with open(path) as f2:
                for line in f2:
                    r = json.loads(line)
                    iid = r["instance_id"]
                    if iid not in instances:
                        repo = iid.split(".")[0]
                        instances[iid] = {
                            "repo": repo,
                            "repo_file_count": rng.randint(10, 500),
                            "has_structural": bool(rng.random() < 0.34),
                            "has_z": bool(rng.random() < 0.78),
                            "extraction_method": rng.choice(["codeql", "beniget", "none"]),
                        }
        mock_index = {
            "instances": instances,
            "repo_stats": {},
            "summary": {"note": "mock data for dry-run"},
        }
        with open(index_path, "w") as f2:
            json.dump(mock_index, f2, indent=1)
        print(f"  Mock index written: {index_path}", flush=True)

    return str(index_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", default=None,
                        help="Dir with per_query_*.jsonl files")
    parser.add_argument("--index-file", default=None,
                        help="stratification_index.json from prepare_stratification_index.py")
    parser.add_argument("--strategies", default="random,embedding_distance,dataflow_aware")
    parser.add_argument("--baseline", default="random")
    parser.add_argument("--encoder", default="qwen")
    parser.add_argument("--seeds", default="42,43,44")
    parser.add_argument("--pool-size", type=int, default=50)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--bootstrap-iter", type=int, default=2000)
    args = parser.parse_args()

    strategies = args.strategies.split(",")
    seeds = [int(s) for s in args.seeds.split(",")]
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    tag_prefix = "dryrun" if args.dry_run else args.encoder

    if args.dry_run:
        results_dir = str(out_dir / "per_query")
        print("Generating dry-run mock data...", flush=True)
        index_path = generate_dryrun_data(results_dir, strategies, seeds, args.pool_size)
    else:
        results_dir = args.results_dir
        index_path = args.index_file

    if not results_dir or not index_path:
        print("ERROR: --results-dir and --index-file required in real mode", file=sys.stderr)
        sys.exit(1)

    print(f"Loading index from {index_path}", flush=True)
    index = load_index(index_path)
    inst_count = len(index.get("instances", {}))
    print(f"  {inst_count} instances in index", flush=True)

    # Load all per-query results
    all_records = []
    loaded = 0
    for strategy in strategies:
        for seed in seeds:
            tag = f"{tag_prefix}_{strategy}_s{seed}"
            recs = load_per_query(results_dir, tag_prefix, strategy, seed, args.pool_size)
            if recs is None:
                print(f"  WARN: missing {tag} pool={args.pool_size}", flush=True)
                continue
            for r in recs:
                r["strategy"] = strategy
                r["seed"] = seed
            all_records.extend(recs)
            loaded += 1
            print(f"  Loaded {tag}: {len(recs)} queries", flush=True)

    print(f"\nTotal: {len(all_records)} records from {loaded} runs", flush=True)

    if not all_records:
        print("ERROR: no data loaded", file=sys.stderr)
        sys.exit(1)

    # Run analysis
    print("\nRunning stratified analysis...", flush=True)
    results = run_analysis(all_records, index, strategies, args.baseline)

    # Print summary
    for dim, data in results.items():
        print(f"\n{'='*60}", flush=True)
        print(f"Dimension: {dim}", flush=True)
        print(f"{'='*60}", flush=True)
        strata = data["strata"]
        for bname, metrics in sorted(strata.items()):
            if isinstance(metrics, dict) and "count" in metrics:
                parts = [f"  {bname} (n={metrics['count']})"]
                for s in strategies:
                    m = metrics.get(s, {})
                    if isinstance(m, dict) and "mean" in m:
                        parts.append(f"  {s}: {m['mean']:.4f} [{m['ci_lower']:.4f}, {m['ci_upper']:.4f}]")
                for s in strategies:
                    if s != args.baseline:
                        dk = f"delta_{s}_vs_{args.baseline}"
                        d = metrics.get(dk)
                        if d is not None:
                            parts.append(f"  {dk}: {d:+.4f}")
                print("\n".join(parts), flush=True)
            elif isinstance(metrics, (int, float)):
                print(f"  {bname}: {metrics}", flush=True)

    # Save outputs
    suffix = "_dryrun" if args.dry_run else ""

    json_path = out_dir / f"stratified_results{suffix}.json"
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nJSON saved: {json_path}", flush=True)

    csv_path = out_dir / f"stratified_results{suffix}.csv"
    generate_csv(results, csv_path)
    print(f"CSV saved: {csv_path}", flush=True)

    generate_plots(results, strategies, args.baseline, out_dir)

    print("\nDone.", flush=True)


if __name__ == "__main__":
    main()
```

---

Both scripts were extracted from JSONL lines 63 and 65 respectively of the chat log at `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/worker_code_plan005-stratified-prep_20260515T050005.jsonl`. They were originally written to `/root/structfuse/scripts/evaluate_stratified.py` and `/root/structfuse/scripts/analyze_stratified.py` on remote server `bjb1-42106`. Both dry-run verifications passed per the spec at `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_005/report/plan005_stratification_spec.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a0d9c8f-86e4-4c0d-ad36-be7b52d18c4c",
  "isSidechain": true,
  "agentId": "a244b0313f96edf04",
  "requestId": "req_011Cb3zfbrBq5omtLE1ntdt5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2843b1e3-eb24-487b-ae32-1e798a27274e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "953f15f8-e655-48b5-a31c-751a817178ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BxL7712tDqg8S9GKPPMm8d",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10850,
      "cache_read_input_tokens": 18690,
      "output_tokens": 9035,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10850
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9035,
          "cache_read_input_tokens": 18690,
          "cache_creation_input_tokens": 10850,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10850,
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
