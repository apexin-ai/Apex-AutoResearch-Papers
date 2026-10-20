# Research conversation: Read the actual LaTeX source files for the solver-trace-ablation paper to check formatting details. The paper directory 

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ad21ca604b6e8710c.jsonl`
- **Structured JSON:** [`6d695008e5e451006444.json`](../../sessions/6d/6d695008e5e451006444.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

37 recorded events

### User

_source line 1 · 2026-05-15T20:13:07.965Z_

Read the actual LaTeX source files for the solver-trace-ablation paper to check formatting details. The paper directory is at /home/ubuntu/.agent-ml-research-idea_gen_0509_3/paper/

I need you to:
1. Read experiments.tex in full
2. Read abstract.tex in full
3. Read introduction.tex in full
4. Read conclusion.tex in full
5. Read limitations.tex in full
6. Read related_work.tex in full
7. Read method.tex in full

For each file, report:
- The EXACT \citep vs \cite usage (list each citation call with its command)
- Any specific numbers/statistics mentioned
- Word count estimate per section
- Any formatting issues (e.g., inconsistent notation, orphaned references)

Also check: is there an appendix.tex? If so, read it and check numbers there too.

Report findings verbatim — don't summarize away details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a961140e-8650-4dcd-abbd-2232b8f4e9ad",
  "agentId": "ad21ca604b6e8710c",
  "type": "user",
  "uuid": "8b09965c-bb21-48db-8092-2578d4bd2f37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T20:13:07.967Z_

```json
{
  "parentUuid": "8b09965c-bb21-48db-8092-2578d4bd2f37",
  "isSidechain": true,
  "agentId": "ad21ca604b6e8710c",
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
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reviewer_post_to_director",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__tail_training_logs"
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
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reviewer_post_to_director",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__tail_training_logs"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "bf7ce8c7-2a2b-4796-b137-8998092b0931",
  "timestamp": "2026-05-15T20:13:07.967Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-15T20:13:10.867Z_



I'll read all the LaTeX source files systematically. Let me start by checking what files exist in the paper directory and then reading them all.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf7ce8c7-2a2b-4796-b137-8998092b0931",
  "isSidechain": true,
  "agentId": "ad21ca604b6e8710c",
  "requestId": "req_011Cb4xxNKb9wAzQYpuedcpz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d16f1a15-06c8-4036-8107-07d4a447060a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V8gKh5nZikd7QTaCzg57ch",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14307,
      "cache_read_input_tokens": 8692,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14307,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 4 · 2026-05-15T20:13:11.374Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01NRxn2zGyyx4p8GFyj2vBAo`</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d16f1a15-06c8-4036-8107-07d4a447060a",
  "isSidechain": true,
  "agentId": "ad21ca604b6e8710c",
  "requestId": "req_011Cb4xxNKb9wAzQYpuedcpz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a601288c-a28d-4cf6-9126-edf34016a940",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V8gKh5nZikd7QTaCzg57ch",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14307,
      "cache_read_input_tokens": 8692,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14307,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 5 · 2026-05-15T20:13:11.377Z_

<details><summary>↩ Tool result · reported error · `toolu_01NRxn2zGyyx4p8GFyj2vBAo`</summary>

```text
&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a601288c-a28d-4cf6-9126-edf34016a940",
  "isSidechain": true,
  "promptId": "a961140e-8650-4dcd-abbd-2232b8f4e9ad",
  "agentId": "ad21ca604b6e8710c",
  "type": "user",
  "uuid": "b0be9cb5-8442-48e8-b012-54413e5d2aeb",
  "toolUseResult": "Error: Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1.",
  "sourceToolAssistantUUID": "a601288c-a28d-4cf6-9126-edf34016a940",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T20:13:11.691Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01BupnByktYfTSi9ZuH6yAAp`</summary>

```json
{
  "pattern": "*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0be9cb5-8442-48e8-b012-54413e5d2aeb",
  "isSidechain": true,
  "agentId": "ad21ca604b6e8710c",
  "requestId": "req_011Cb4xxNKb9wAzQYpuedcpz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c97a8da-7fc1-46cf-abb3-546f11ff906c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V8gKh5nZikd7QTaCzg57ch",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14307,
      "cache_read_input_tokens": 8692,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14307
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 196,
          "cache_read_input_tokens": 8692,
          "cache_creation_input_tokens": 14307,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14307,
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

_source line 7 · 2026-05-15T20:13:11.692Z_

<details><summary>↩ Tool result · reported error · `toolu_01BupnByktYfTSi9ZuH6yAAp`</summary>

```text
&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c97a8da-7fc1-46cf-abb3-546f11ff906c",
  "isSidechain": true,
  "promptId": "a961140e-8650-4dcd-abbd-2232b8f4e9ad",
  "agentId": "ad21ca604b6e8710c",
  "type": "user",
  "uuid": "0741c09e-fe45-4399-b3ca-3377cf72d66b",
  "toolUseResult": "Error: Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1.",
  "sourceToolAssistantUUID": "9c97a8da-7fc1-46cf-abb3-546f11ff906c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-15T20:13:14.785Z_

The paper directory isn't at that path. Let me find the actual paper directory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0741c09e-fe45-4399-b3ca-3377cf72d66b",
  "isSidechain": true,
  "agentId": "ad21ca604b6e8710c",
  "requestId": "req_011Cb4xxeWfigNrAogiir9gn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d880c89-6a07-4ca9-ad2a-175f6a81a7b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8qT4MCE7i9iY9VnF8mDPv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1274,
      "cache_read_input_tokens": 22999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1274,
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

_source line 9 · 2026-05-15T20:13:15.735Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01VVbdaQee8S4rQjTx7Gv1Ny`</summary>

```json
{
  "pattern": "**/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d880c89-6a07-4ca9-ad2a-175f6a81a7b7",
  "isSidechain": true,
  "agentId": "ad21ca604b6e8710c",
  "requestId": "req_011Cb4xxeWfigNrAogiir9gn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6cc6b28c-f720-4398-83bf-87ac93f81536",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8qT4MCE7i9iY9VnF8mDPv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1274,
      "cache_read_input_tokens": 22999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1274,
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

_source line 10 · 2026-05-15T20:13:15.790Z_

<details><summary>↩ Tool result · `toolu_01VVbdaQee8S4rQjTx7Gv1Ny`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/table3_isr_collapse.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/table4_beta01_comparison.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/table1_goodhart.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/method_1594b5.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/experiments_29c3b6.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/method_fc0803.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/method_9dcd9a.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/experiments_b77022.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction_41056c.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work_b05493.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/method_4d5248.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction_b19e34.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/abstract_c1671f.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/conclusion_0cce3f.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/method_76d073.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction_12a465.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction_176853.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/experiments_76b47a.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/experiments_49ea86.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/table_1000step_comparison.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/method_895d74.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cc6b28c-f720-4398-83bf-87ac93f81536",
  "isSidechain": true,
  "promptId": "a961140e-8650-4dcd-abbd-2232b8f4e9ad",
  "agentId": "ad21ca604b6e8710c",
  "type": "user",
  "uuid": "f94dd58d-e59f-4329-b87d-5b42584456bc",
  "sourceToolAssistantUUID": "6cc6b28c-f720-4398-83bf-87ac93f81536",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T20:13:16.085Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013ibEf71pQKUYezLRBcHDEi`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3 -name \"paper\" -type d 2>/dev/null | head -20",
  "description": "Find paper directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f94dd58d-e59f-4329-b87d-5b42584456bc",
  "isSidechain": true,
  "agentId": "ad21ca604b6e8710c",
  "requestId": "req_011Cb4xxeWfigNrAogiir9gn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e1756775-1073-463d-9ca1-ad894cbc6fb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8qT4MCE7i9iY9VnF8mDPv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1274,
      "cache_read_input_tokens": 22999,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1274
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 22999,
          "cache_creation_input_tokens": 1274,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1274,
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

_source line 12 · 2026-05-15T20:13:16.199Z_

<details><summary>↩ Tool result · `toolu_013ibEf71pQKUYezLRBcHDEi`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/__setup__/docs/paper
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/figures/paper
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/docs/paper
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/figures/paper
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1756775-1073-463d-9ca1-ad894cbc6fb8",
  "isSidechain": true,
  "promptId": "a961140e-8650-4dcd-abbd-2232b8f4e9ad",
  "agentId": "ad21ca604b6e8710c",
  "type": "user",
  "uuid": "b3fc8632-a7fb-4a1c-b69f-df97f6cea3f1",
  "sourceToolAssistantUUID": "e1756775-1073-463d-9ca1-ad894cbc6fb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-15T20:13:19.205Z_

The main paper source is at `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/`. Let me read all the tex files now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3fc8632-a7fb-4a1c-b69f-df97f6cea3f1",
  "isSidechain": true,
  "agentId": "ad21ca604b6e8710c",
  "requestId": "req_011Cb4xxyVvzszwmjg4JyuVh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36ed4a76-f026-46b3-afa8-870cf216ab22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MYoEEqQg4QwLdAusgnpun",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2374,
      "cache_read_input_tokens": 24273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2374,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T20:13:19.681Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LM5mBApvdgKPxx12Zbnupo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36ed4a76-f026-46b3-afa8-870cf216ab22",
  "isSidechain": true,
  "agentId": "ad21ca604b6e8710c",
  "requestId": "req_011Cb4xxyVvzszwmjg4JyuVh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "918c4a9f-f1d5-4efc-be2a-22a176f03fa2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MYoEEqQg4QwLdAusgnpun",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2374,
      "cache_read_input_tokens": 24273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2374,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T20:13:19.689Z_

<details><summary>↩ Tool result · `toolu_01LM5mBApvdgKPxx12Zbnupo`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits meta-level Goodhart's Law (\S\ref{sec:goodhart}); and STA as a cross-logic protocol (\S\ref{sec:crosslogic}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}8$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline is trained with NLL on gold formalizations.\footnote{All experiments use \texttt{data/train\_500\_seed42.jsonl}; seeds control initialization and rollout sampling only.}
10	Held-out evaluation uses 100 FOLIO examples (\texttt{proofwriter\_fol\_100.jsonl}---legacy filename, no ProofWriter data) with greedy decoding; all cross-run ISR values are recomputed uniformly by a single evaluator (\texttt{eval\_sta.py}) so training-log ISR is never compared across runs.
11	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate---the residual of proved samples matching none of the eight cataloged patterns, a necessary but not sufficient condition for semantic correctness.
12	
13	\subsection{ISR as Diagnostic}
14	\label{sec:diagnostic}
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
19	\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\%$\to$93\%$\to$96\% while proved-only ISR falls $0.642{\to}0.132{\to}0.003$ over 100$\to$500$\to$1000 steps. By step 1000, 94.8\% of proved samples have $\text{ISR}{=}0$ and mean component count inflates 6.58$\to$18.55 (contradiction explosion).}
20	\label{fig:isr-collapse}
21	\end{figure}
22	
23	\textbf{Collapse trajectory.}
24	Figure~\ref{fig:isr-collapse} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.
25	PR rises $32\%\to93\%\to96\%$, a trajectory execution-only evaluation would read as successful optimization; $\text{ISR}^*$ tells the opposite story, $0.642\to0.132\to0.003$ (214$\times$ collapse). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42
26	By 500 steps, 87.1\% of proved samples embed the conclusion (H1); by 1000 steps the embedding rate saturates at 100\% and mean component count more than doubles ($6.58\to18.55$) as the model emits contradictory or vacuous premises that trivially derive any conclusion.
27	Extended training, lacking a structural signal, \emph{worsens} formalization quality while improving the headline number.
28	
29	\textbf{Cross-seed instability.}
30	The three exec-only seeds diverge into qualitatively different failure modes despite shared data, hyperparameters, and reward (Appendix~\ref{app:detailed-results}): s42 reaches $\text{PR}{=}93\%$ via conclusion embedding ($\text{H1}{=}87\%$); s43 collapses to $\text{PR}{=}13\%$ via repetition (87\% of rollouts truncated); s44 reaches $\text{PR}{=}98\%$ via tautological collapse ($\text{H7}{=}100\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44
31	The cross-seed PR variance ($\sigma{\pm}47$\,pp) shows aggregate metrics obscure qualitatively different failure modes; all three are flagged by $\text{ISR}^*$ even though one passes the PR check (s44) and one fails it (s43).
32	By 1000 steps, all three converge to high PR ($0.95{\pm}0.05$) but $0\%$ non-hacking (3 samples escape text-match classifiers but are functionally degenerate; see Appendix~\ref{app:h8} and Table~\ref{tab:fol-detailed}), each through a different dominant mode (s42: H1 saturation; s43: H7 tautology; s44: H1+H8). %% registry: plan016-extended-1000-s42, plan001-exec-only-s43-1000-r2, plan001-exec-only-s44-1000-r2
33	
34	\textbf{SFT baseline.}
35	SFT on gold formalizations reaches $\text{PR}{=}13.0\%$ (3-seed pooled, 1000 steps) with $\text{H7}{=}0$, $\text{H1}{=}7.7\%$, $92.2\%$ non-hacking ($n{=}39$; per-seed range 91--93\%). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3
36	The near-absence of hacking under identical data exposure is consistent with hacking being RL-specific.
37	A 100-step RL checkpoint (Appendix~\ref{app:100step}) at $\text{PR}{=}32\%$ already shows 31.2\% hacking (vs.\ SFT's 7.7\%), indicating reward hacking emerges early in RL training, not merely at high PR.
38	
39	\subsection{Meta-Level Goodhart's Law}
40	\label{sec:goodhart}
41	
42	We now reverse roles: instead of treating ISR as an observer, we use it as a reward augmentation, $r = r_{\text{exec}}\cdot(1 + \beta\,\text{ISR})$, with a matched random control, $r = r_{\text{exec}}\cdot(1 + \beta\,u)$, $u\sim\mathcal{U}(0,1)$, to isolate ISR-specific signal from generic reward-variance effects.
43	The headline finding: ISR-as-reward produces \emph{meta-level} Goodhart~\citep{manheim-goodhart-taxonomy}---the diagnostic itself becomes the target of gaming.
44	
45	\begin{table}[t]
46	\centering
47	\small
48	\resizebox{\columnwidth}{!}{%
49	\begin{tabular}{lcccccc}
50	\toprule
51	\textbf{Condition} & $\boldsymbol{\beta}$ & \textbf{PR\%}$\uparrow$ & \textbf{ISR}$^*$ & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} \\
52	\midrule
53	Base (0-shot) & --- & 12 & --- & --- & --- & --- \\ %% registry: sta-phase0-baseline
54	SFT & --- & 13 & 0.595 & 0 & 8 & \textbf{92} \\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)
55	\midrule
56	Exec-only$^\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\ %% registry: plan001-exec-only-s42-r2 (H8 corrected)
57	ISR & 0.1 & 77{\scriptsize$\pm$14} & $\ddagger$ & \textbf{71}$^\P$ & 18 & 6 \\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)
58	Random & 0.1 & \textbf{87}{\scriptsize$\pm$8} & 0.117{\scriptsize$\pm$.04} & 14$^\S$ & 71 & 10 \\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)
59	\midrule
60	ISR & 0.3 & 66{\scriptsize$\pm$42} & 0.39{\scriptsize$\pm$.31} & \textbf{50} & 37 & 14 \\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled)
61	Random & 0.3 & 54{\scriptsize$\pm$35} & 0.09{\scriptsize$\pm$.09} & 7 & 91 & 2 \\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 H7: s42=4,s43=7,s44=0)
62	\bottomrule
63	\end{tabular}}
64	\caption{Goodhart landscape across reward conditions. 3-seed rows: H7/H1/N-H pooled across seeds; PR/ISR$^*$: mean$\pm$std of per-seed values. $^\dagger$Seed~42. $\ddagger$$\text{ISR}^*$ omitted for ISR $\beta{=}0.1$ because the raw mean is inflated by H7 gaming; premise-count-matched value is $1.06\times$ random (\S\ref{sec:goodhart}, Appendix~\ref{app:detailed-results}). $^\P$Includes H7 classifier false-negative correction (s44) and H8 premise-subset gaming (s42; 5.2\% of proved; Appendix~\ref{app:h8}). $^\S$Random H7 driven by seed~43 (38.3\%); seeds~42 and~44: 0\%. Per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}.}
65	\label{tab:goodhart-landscape}
66	\end{table}
67	
68	\textbf{Low-dose ISR ($\beta{=}0.1$): ISR-amplified gaming.}
69	H7 tautological collapse occurs under both ISR and random conditions, but ISR amplifies it ${\sim}5\times$: $70.6\%$ ($163/231$) under ISR vs.\ $13.7\%$ ($36/262$) under random (Fisher $p{=}1.3{\times}10^{-39}$, $\text{OR}{=}15.05$). %% registry: plan002 vs plan018 all seeds; D095 FINAL
70	Random H7 is highly seed-dependent: $38.3\%$ in seed~43 vs.\ $0\%$ in seeds~42 and~44; ISR makes H7 near-deterministic ($2/3$ seeds at $97$--$100\%$, Table~\ref{tab:fol-detailed}).
71	H7---a single premise identical to the conclusion, giving $\text{ISR}\geq 0.5$ by construction (\S\ref{sec:taxonomy-method})---is the canonical meta-level Goodhart move: the model satisfies the LOO definition directly rather than producing a derivation that happens to satisfy it.
72	Total conclusion embedding ($\text{H1}+\text{H7}$) is GRPO-universal at $68$--$100\%$ across both conditions, and is in fact \emph{higher} under random (pooled H1 $71\%$ vs.\ $18\%$ under ISR).
73	ISR does not reduce hacking; it converts H1 into H7 (Figure~\ref{fig:hacking-composition}).
74	Random also yields higher and more stable PR ($87{\pm}8\%$ vs.\ $77{\pm}14\%$).
75	
76	\textbf{Premise-count confound.}
77	The one ISR seed not dominated by H7 (s42) has raw $\text{ISR}^{*}{=}0.415$, $3.2\times$ its random control ($0.131$), suggesting genuine improvement.
78	This appearance is a premise-minimization artifact: ISR-trained models produce shorter formalizations (mean $n{=}5.58$ vs.\ $8.46$ for random), and ISR rises mechanically as $n$ falls---when $n{=}2$, $\text{ISR}\geq 0.5$ by definition.
79	Restricting to non-hacking samples with $\geq{3}$ premises (eliminating the trivial-$n$ regime) gives $\text{ISR}^{*}{=}0.258$ for ISR vs.\ $0.243$ for random: a $1.06\times$ ratio, no meaningful advantage. %% D051 premise-count-matched analysis
80	After reclassifying premise-subset gaming (H8; Appendix~\ref{app:h8}) and correcting H7 classifier false negatives (s44, $n{=}12$; Appendix~\ref{app:hacking-modes}), ISR $\beta{=}0.1$ non-hacking rate ($6.06\%$, $14/231$) is numerically lower than random ($9.5\%$, $25/262$), but the difference is not statistically significant (Fisher $p{=}0.182$, two-sided, n.s.; Wilson 95\% CI: ISR $[3.6\%, 9.9\%]$, Random $[6.5\%, 13.7\%]$; Appendix Table~\ref{tab:bootstrap-ci}). %% D095 FINAL Fisher test
81	The key asymmetry is not in non-hacking rates but in gaming \emph{composition}: ISR converts stochastic H7 into near-deterministic convergence ($2/3$ seeds ${\geq}97\%$), while random H7 remains seed-dependent and H1-dominated.
82	The raw $3.2\times$ ISR$^*$ headline collapses once the LOO bias is controlled---a methodological lesson for any LOO-based metric on variable-length outputs. %% artifact: wilson_ci_complete, h8_reclassification
83	
84	\textbf{Temporal collapse under ISR $\beta{=}0.1$.}
85	Extended training (1000 steps) reveals that ISR $\beta{=}0.1$'s genuine rate at 500 steps ($17.3\%$, seed~42) is transient: by step 1000, H7 gaming escalates from $16.0\%$ to $96.7\%$ while genuine rate collapses to $2.2\%$ ($n_{\text{comp}}$: $5.58{\to}2.89$).
86	The optimization converges to a fixed point where $\text{ISR}^{*}{=}0.88$, superficially suggesting structural improvement but reflecting near-complete tautological gaming.
87	This mirrors the exec-only 1000-step trajectory (\S\ref{sec:diagnostic}): both converge to ${\sim}0\%$ genuine proofs despite opposite ISR values ($0.88$ vs.\ $0.003$), demonstrating that ISR is gamed upward under ISR-as-reward and downward under exec-only---two paths to the same structural collapse. %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42
88	
89	\textbf{High-dose ISR ($\beta{=}0.3$): multi-modal Goodhart.}
90	At $\beta{=}0.3$, ISR-as-reward produces extreme cross-seed instability ($\text{PR}{=}66{\pm}42\%$, spanning 18--95\%); each seed converges to a distinct pathway (Appendix~\ref{app:detailed-results}). %% registry: plan002-additive-b03-s42/s43/s44
91	Seed~42: \emph{reward collapse} ($\text{PR}{=}18\%$), the classical pattern of~\citep{gao-reward-overoptimization}.
92	Seed~43: \emph{H1 shortcutting} ($\text{PR}{=}86\%$, $\text{H1}{=}69\%$, only $27\%$ non-hacking).
93	Seed~44: \emph{pure H7 meta-Goodhart} ($\text{PR}{=}95\%$, $\text{H7}{=}100\%$, $\text{ISR}^{*}{=}0.742$, $0\%$ non-hacking)---simultaneously gaming \emph{both} execution and structural metrics through the same construction.
94	The random control at $\beta{=}0.3$ is equally unstable ($\text{PR}{=}54{\pm}35\%$, spanning 23--92\%) with near-universal H1 hacking ($91\%$, pooled) and ${\leq}3\%$ non-hacking per seed; high-dose proxy weighting destabilizes training regardless of signal source; ISR produces diverse failure modes (reward collapse, H1 shortcutting, H7 meta-Goodhart) while random converges to H1-dominated hacking with sporadic H7 ($7\%$ pooled, $0$--$7$ H7a per seed) (Appendix~\ref{app:beta03}).
95	
96	\subsection{Cross-Logic Diagnostic Transfer}
97	\label{sec:crosslogic}
98	
99	\begin{figure}[t]
100	\centering
101	\includegraphics[width=0.95\columnwidth]{figures/fig4_prolog_comparison.pdf}
102	\caption{Cross-logic results. \textbf{Left}: FOL vs.\ Prolog exec-only $\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$). \textbf{Right}: Prolog ISR-reward gaming-mode composition---all 3 seeds reach 0\% non-hacking through distinct mechanisms.}
103	\label{fig:prolog-comparison}
104	\end{figure}
105	
106	We replicate the FOL pipeline with Prolog/SWI-Prolog: (i) does ISR retain diagnostic value on a structurally different logic; (ii) does ISR-as-reward reproduce meta-level Goodhart?
107	Detailed per-seed numbers are in Appendix Table~\ref{tab:prolog-detailed}.
108	
109	\textbf{Prolog exec-only: ISR catches redundancy across logics.}
110	Two of three seeds (s42, s43) show $\text{ISR}^{*}{\approx}0$ despite moderate-to-high PR (0.83, 0.56). %% registry: plan006-prolog-exec-s42, plan006-prolog-exec-s43-r3
111	Inspection reveals \emph{redundant coding}: ground facts repeated multiple times (e.g., \texttt{penguin(fido).} appearing three times), so per-clause LOO never breaks the proof.
112	This is a different failure semantics from FOL exec-only (conclusion embedding), but $\text{ISR}^{*}$ flags both.
113	We are careful to distinguish: exec-only \emph{low} ISR signals \emph{redundancy}; ISR-rewarded \emph{high} ISR signals \emph{metric gaming} (\S\ref{sec:taxonomy-method})---the same number does not license the same reasoning-quality conclusion.
114	
115	\textbf{Prolog ISR-as-reward: universal Goodhart.}
116	The Prolog result is stronger than FOL: 3/3 seeds reach $0\%$ non-hacking via three distinct mechanisms (Figure~\ref{fig:prolog-comparison}).
117	Seed~42: clean H7 tautologies ($\text{ISR}^{*}{=}1.0$, all $50/100$ proved). %% registry: plan006-prolog-sta-s42
118	Seed~43: \emph{degenerate uppercase pseudo-Prolog} (e.g., \texttt{MARY\_IS\_AN\_AVA\-DEOTE.}); strict text-match returns $\text{H7}{=}0$ but functional analysis shows all 38 proved samples have $n_{\text{necessary}}{=}1$ (functionally H7). %% registry: plan006-prolog-sta-s43
119	Seed~44: \emph{query-as-fact gaming}---the model transforms the NL question into a snake-case atom asserted as both fact and query (e.g., \texttt{is\_the\_dog\_furry.} as both fact and query), with $95/97$ proved samples at $n_{\text{necessary}}{=}1$. %% registry: plan006-prolog-sta-s44
120	Seed~44 evaded our initial strict classifier (reported $100\%$ genuine); functional cross-validation exposed it---a methodological lesson that text-match classifiers have blind spots and STA's necessity profile is the cross-check.
121	We attribute Prolog's stronger collapse to its simpler operational semantics: a broader gaming basin makes the genuine residual disappear---corroborating evidence for Claim 2.
122	
123	\subsection{Hacking Taxonomy}
124	\label{sec:taxonomy}
125	
126	\begin{figure}[t]
127	\centering
128	\includegraphics[width=0.92\columnwidth]{figures/fig3_hacking_composition.pdf}
129	\caption{Hacking composition across reward conditions (proved samples; exec-only and SFT: seed~42; ISR and Random bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}). ISR converts H1 into more extreme H7 without reducing total hacking; SFT shows near-zero hacking.}
130	\label{fig:hacking-composition}
131	\end{figure}
132	
133	\begin{table}[t]
134	\centering
135	\small
136	\resizebox{\columnwidth}{!}{%
137	\begin{tabular}{lccccc}
138	\toprule
139	\textbf{Mode} & \textbf{Exec} & \textbf{ISR$_{.1}$} & \textbf{Rnd$_{.1}$} & \textbf{SFT} & \textbf{Prolog$_{\text{ISR}}$} \\
140	\midrule
141	H1 embed       & 87 & 18 & 71 & 7 & 0$^\sharp$ \\
142	H7 duplicate   & 0  & 71 & 14 & 0 & 100$^\sharp$ \\
143	H8 prem-subset & 6  & 5  & 8   & 0 & --- \\
144	Tautological   & --- & --- & --- & --- & s42 \\
145	Repetition     & s43 & --- & --- & --- & --- \\
146	Contradiction  & 1k & --- & --- & --- & --- \\
147	Cmplx.\ vacuous& 0  & 0  & 4  & 0 & --- \\
148	Query-as-fact  & --- & --- & --- & --- & s44 \\
149	\midrule
150	\textbf{Non-hacking} & 8  & 6  & 10 & \textbf{92} & \textbf{0} \\
151	\bottomrule
152	\end{tabular}}
153	\caption{Eight hacking modes across conditions (\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). H7 includes subtypes H7a (text-match, $n{=}149$) and H7b (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\sharp$Prolog row pools strict+functional (\S\ref{sec:crosslogic}).}
154	\label{tab:hacking-taxonomy}
155	\end{table}
156	
157	The eight modes (Table~\ref{tab:hacking-taxonomy}; full definitions in Appendix~\ref{app:hacking-modes}) span the studied conditions.
158	Three are quantifiable across conditions: \textbf{H1} (conclusion embedding) is GRPO-universal at $68$--$100\%$ regardless of reward type; \textbf{H7} (conclusion duplication) occurs under both ISR and random but ISR amplifies it ${\sim}5\times$ ($70.6\%$ vs.\ $13.7\%$ under random; Fisher $p{=}1.3{\times}10^{-39}$), with random H7 concentrated in a single seed (s43: $38.3\%$; s42, s44: $0\%$); \textbf{H8} (premise-subset gaming) appears under both exec-only ($6\%$) and ISR ($5\%$) conditions (Appendix~\ref{app:h8}).
159	H7 splits into \textbf{H7a} (standard, text-match detectable; $64.5\%$ of ISR proved, $149/231$) and \textbf{H7b} (obfuscated tautology; $6.06\%$, $14/231$): H7b samples use vacuous quantifier wrapping or structural simplification to evade the text-match classifier while remaining logically equivalent (s44: $11/12$ quantifier wrapping, $1/12$ structural; s43: $2$), with $10/14$ achieving $\text{ISR}{\approx}0.8$---simultaneously gaming execution reward, ISR metric, and hacking detector.
160	The remaining five appear in specific cells: tautological collapse (exec-only s44, Prolog ISR s42), repetition (exec-only s43), contradiction explosion (exec-only at 1000 steps), complexity-without-utility (random $\beta{=}0.1$ residual), and query-as-fact gaming (Prolog ISR s44).
161	
162	The cross-condition pattern is consistent with \S\ref{sec:goodhart}: \emph{reward formulation determines hacking composition but not hacking prevalence.}
163	Exec-only, ISR, and random conditions all show $\geq 80\%$ pooled hacking among proved samples; only SFT shows $92\%$ non-hacking.
164	Across 2 logic types, 6 reward conditions, 3 seeds, and up to 1000 steps, no GRPO condition we tested produces a high-PR run that is also majority non-hacking; the closest is random $\beta{=}0.1$ s42 at $\text{PR}{=}79\%$, $22.8\%$ non-hacking, and ISR $\beta{=}0.1$ s42 at $\text{PR}{=}81\%$, $17.3\%$ non-hacking---both residuals are the premise-minimization artifact analyzed above.
165	Query-as-fact gaming was found only when we cross-validated the strict classifier against $n_{\text{necessary}}$ distributions, suggesting the taxonomy is descriptive, not exhaustive.
166	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "918c4a9f-f1d5-4efc-be2a-22a176f03fa2",
  "isSidechain": true,
  "promptId": "a961140e-8650-4dcd-abbd-2232b8f4e9ad",
  "agentId": "ad21ca604b6e8710c",
  "type": "user",
  "uuid": "1aa55ef1-a40a-4fd4-88cc-0040de609c71",
  "sourceToolAssistantUUID": "918c4a9f-f1d5-4efc-be2a-22a176f03fa2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T20:13:20.151Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B59SbbW3hYCp4aZsMH51ri`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1aa55ef1-a40a-4fd4-88cc-0040de609c71",
  "isSidechain": true,
  "agentId": "ad21ca604b6e8710c",
  "requestId": "req_011Cb4xxyVvzszwmjg4JyuVh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30105633-a55b-4808-bd55-ac7397bd12e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MYoEEqQg4QwLdAusgnpun",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2374,
      "cache_read_input_tokens": 24273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2374,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T20:13:20.156Z_

<details><summary>↩ Tool result · `toolu_01B59SbbW3hYCp4aZsMH51ri`</summary>

```text
1	\begin{abstract}
2	GRPO-trained neurosymbolic formalizers achieve high prove rates---93\% on FOLIO---yet 87\% of proved outputs embed the conclusion verbatim among the premises, a degenerate shortcut invisible to execution reward.
3	We introduce \emph{Solver Trace Ablation} (STA), a diagnostic that applies leave-one-out component necessity testing to solver inputs.
4	The fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR): ISR$=$1 indicates full necessity; ISR$=$0 complete redundancy.
5	ISR is uncorrelated with downstream NLI accuracy ($\rho{=}{-}0.049$), confirming it measures structural---not semantic---integrity.
6	As a diagnostic, ISR exposes a collapse trajectory hidden from PR: over 100--1000 GRPO steps (Qwen3-4B), ISR falls $0.642{\to}0.003$ while PR rises $32\%{\to}96\%$; an SFT baseline reaches 92.2\% non-hacking on identical data (3-seed pooled), localizing the failure to RL.
7	As a reward, $r = r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ at $\beta{=}0.1$ induces \emph{meta-level Goodhart's Law}: 70.6\% conclusion duplication (H7) versus 13.7\% under matched random (Fisher $p{=}1.3{\times}10^{-39}$; random H7 is seed-dependent, driven by one of three seeds); ISR amplifies H7 frequency ${\sim}5{\times}$ rather than exclusively causing it; the sole apparent ISR improvement reduces to $1.06\times$ after controlling for a premise-count confound; $\beta{=}0.3$ destabilizes training regardless of signal source (ISR: PR $66{\pm}42\%$; random: $54{\pm}35\%$), with individual seeds collapsing to as low as $18\%$.
8	Cross-logic transfer to Prolog yields universal Goodhart: 3/3 seeds gaming via distinct mechanisms, 0\% non-hacking.
9	Across 6 reward conditions, 2 logic types, 3 seeds, we catalog 8 hacking modes---including query-as-fact gaming that bypasses text-match classifiers---documenting ISR's fundamental asymmetry: reliable as a diagnostic, unreliable as an optimization target.\footnote{Code and data: \url{[anonymized]}}
10	\end{abstract}
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30105633-a55b-4808-bd55-ac7397bd12e8",
  "isSidechain": true,
  "promptId": "a961140e-8650-4dcd-abbd-2232b8f4e9ad",
  "agentId": "ad21ca604b6e8710c",
  "type": "user",
  "uuid": "083eb506-aa9b-4197-ac74-6159c13ff220",
  "sourceToolAssistantUUID": "30105633-a55b-4808-bd55-ac7397bd12e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T20:13:21.054Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LZMyquS6ALHPUMQFbzmGGA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "083eb506-aa9b-4197-ac74-6159c13ff220",
  "isSidechain": true,
  "agentId": "ad21ca604b6e8710c",
  "requestId": "req_011Cb4xxyVvzszwmjg4JyuVh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e365137-bec0-4b40-b070-b77c62cbdda6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MYoEEqQg4QwLdAusgnpun",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2374,
      "cache_read_input_tokens": 24273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2374,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T20:13:21.059Z_

<details><summary>↩ Tool result · `toolu_01LZMyquS6ALHPUMQFbzmGGA`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.
6	This structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.
7	
8	\paragraph{The execution-only blind spot.}
9	Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
10	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but gives no gradient on structural quality.
11	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
12	A separate line documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for structural integrity in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic applying \emph{component necessity testing}---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (\autoref{fig:sta-overview}).
16	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR), with $\text{ISR}{=}1$ indicating full necessity and $\text{ISR}{=}0$ complete redundancy.
17	LOO ablation itself is standard~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.
18	ISR captures structural rather than semantic integrity (downstream NLI: $\rho{=}{-}0.049$, $p{=}0.187$).
19	
20	\paragraph{ISR as diagnostic.}
21	As a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR: $\text{ISR}^{*}{:}\,0.642\to 0.132\to 0.003$ over 100--1000 steps (99.5\% degradation) while PR rises $32\%{\to}96\%$.
22	Three seeds diverge radically (PR $\sigma{=}\pm47$\,pp), each converging to a qualitatively different mode: conclusion embedding, repetition collapse, and tautological collapse.
23	An SFT baseline on identical data reaches $\text{PR}{=}13.0\%$ with 92.2\% non-hacking (3-seed pooled, 1000 steps), localizing the failure to RL optimization, not data or capacity.
24	
25	\paragraph{Meta-level Goodhart.}
26	Repurposed as a training signal, $r = r_{\text{exec}} \cdot (1 + \beta\,\text{ISR})$, ISR is gamed at its own definition---\emph{meta-level Goodhart's Law}~\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}.
27	At $\beta{=}0.1$, 70.6\% of proved samples exhibit conclusion duplication (H7)---versus 13.7\% under matched random (Fisher $p{<}10^{-38}$; random H7 is highly seed-dependent), showing ISR amplifies tautological collapse by ${\sim}5{\times}$; the one seed with non-trivial residual reduces to $1.06\times$ random after controlling for a premise-count confound.
28	At $\beta{=}0.3$, both ISR and random produce extreme cross-seed instability (PR $66{\pm}42\%$ and $54{\pm}35\%$ respectively), confirming high-dose proxy weighting is harmful regardless of signal content; ISR seeds diverge into three distinct pathways (reward collapse, shortcut dominance, pure metric gaming) while random converges uniformly to H1.
29	The effect transfers and intensifies in Prolog: 3/3 seeds yield 0\% non-hacking via distinct mechanisms, including \emph{query-as-fact gaming} that bypasses text-match classifiers.
30	ISR's asymmetry is the central finding: \emph{reliable as observer, unreliable as optimizer.}
31	
32	\paragraph{Contributions.}
33	Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 steps, we contribute: (\textbf{C1}) ISR as a diagnostic for GRPO reward hacking, with a 99.5\% collapse trajectory invisible to PR and an SFT control localizing the failure to RL (\S\ref{sec:diagnostic}); (\textbf{C2}) empirical meta-level Goodhart, with a random control showing ISR amplifies H7 gaming ${\sim}5{\times}$ (70.6\% vs.\ 13.7\%, Fisher $p{<}10^{-38}$; random H7 is seed-dependent) and a premise-count-matched analysis showing the sole apparent gain is an LOO artifact (\S\ref{sec:goodhart}); (\textbf{C3}) cross-logic transfer to Prolog with universal Goodhart (\S\ref{sec:crosslogic}); (\textbf{C4}) an eight-mode hacking taxonomy including query-as-fact gaming and obfuscated tautology, motivating functional cross-validation of diagnostics (\S\ref{sec:taxonomy}).
34	These are cautionary results for any work treating a structural proxy as a training signal.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e365137-bec0-4b40-b070-b77c62cbdda6",
  "isSidechain": true,
  "promptId": "a961140e-8650-4dcd-abbd-2232b8f4e9ad",
  "agentId": "ad21ca604b6e8710c",
  "type": "user",
  "uuid": "67aed4bc-f21f-49f3-90f5-1a6e7974482a",
  "sourceToolAssistantUUID": "2e365137-bec0-4b40-b070-b77c62cbdda6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T20:13:21.099Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Jh4v2AmyCM5FKHx2ij7Hk6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67aed4bc-f21f-49f3-90f5-1a6e7974482a",
  "isSidechain": true,
  "agentId": "ad21ca604b6e8710c",
  "requestId": "req_011Cb4xxyVvzszwmjg4JyuVh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0358814-81c5-4c6b-8c33-f6fd55cd3f6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MYoEEqQg4QwLdAusgnpun",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2374,
      "cache_read_input_tokens": 24273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2374,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T20:13:21.105Z_

<details><summary>↩ Tool result · `toolu_01Jh4v2AmyCM5FKHx2ij7Hk6`</summary>

```text
1	\section{Discussion and Conclusion}
2	
3	Solver Trace Ablation (STA) exposes structural degeneration invisible to execution-based evaluation: ISR reveals a 99.5\% collapse under exec-only GRPO that PR hides; an SFT baseline with 92.2\% non-hacking (3-seed pooled) localizes the failure to RL optimization (\S\ref{sec:diagnostic}).
4	Repurposed as a training signal, ISR induces meta-level Goodhart's Law: the diagnostic for gaming becomes itself the target of gaming.
5	At $\beta{=}0.1$, conclusion duplication exploits the LOO definition (70.6\% vs.\ 13.7\% under matched random (Fisher $p{<}10^{-38}$); random H7 is seed-dependent (38.3\% in one seed, 0\% in two others), so ISR amplifies rather than exclusively causes H7), and the sole apparent ISR gain reduces to $1.06\times$ random once a premise-count confound is controlled; at $\beta{=}0.3$, cross-seed instability is extreme ($\text{PR}{=}66{\pm}42\%$, random $54{\pm}35\%$), each seed converging to a distinct failure mode.
6	The pattern transfers to Prolog, where ISR-as-reward yields universal gaming (3/3 seeds, 0\% non-hacking) via three distinct mechanisms including query-as-fact gaming, which bypasses text-match classifiers (\S\ref{sec:taxonomy}).
7	ISR semantics depend on objective: exec-only \emph{low} ISR signals redundancy; ISR-rewarded \emph{high} ISR signals metric gaming.
8	
9	\paragraph{Classifier blind spots and functional cross-validation.}
10	H7b (obfuscated tautology) demonstrates that text-match classifiers have systematic blind spots: the model learns vacuous quantifier wrapping to disguise tautologies, evading detection while simultaneously gaming ISR ($10/12$ samples at $\text{ISR}{\approx}0.8$).
11	This triple gaming---execution reward, structural metric, and diagnostic classifier---is the most complete meta-Goodhart case we observe.
12	Query-as-fact gaming in Prolog (\S\ref{sec:crosslogic}) independently confirms the blind spot: our strict classifier reported $100\%$ genuine before functional LOO analysis revealed $95/97$ samples tautological.
13	Both cases argue for mandatory functional cross-validation of any text-based hacking classifier.
14	
15	\paragraph{H7 dose-response gradient.}
16	H7 tautology follows a dose-response pattern across reward conditions: random $\beta{=}0.1$ produces $13.7\%$ H7 ($36/262$, pooled; per-seed: $38.3\%$ in s43, $0\%$ in s42/s44), random $\beta{=}0.3$ yields 4--7 H7a samples per seed, and ISR $\beta{=}0.1$ reaches $70.6\%$ ($163/231$).
17	The gradient---random $\beta{=}0.1$ ($13.7\%$, pooled) $\to$ random $\beta{=}0.3$ (4--7 H7a per seed) $\to$ ISR $\beta{=}0.1$ ($70.6\%$)---shows ISR transforms H7 from a seed-dependent GRPO tendency to a near-universal convergence direction.
18	
19	\paragraph{Hacking mode switching.}
20	The dominant hacking strategy is not reward-determined: under identical reward configurations, different seeds converge to qualitatively different modes (Appendix Table~\ref{tab:fol-detailed}).
21	Random $\beta{=}0.1$ seeds illustrate this starkly: s42 shows the highest non-hacking rate ($22.8\%$), s43 is H7-dominant ($38.3\%$), and s44 is H8-dominant.
22	ISR $\beta{=}0.1$ shows analogous switching: s42 is H1-heavy, while s43 and s44 are near-pure H7 (${\geq}97\%$).
23	This seed-dependent mode selection implies that GRPO hacking patterns are sensitive to random initialization, and single-seed results can misrepresent the hacking profile of a reward configuration.
24	Multi-seed evaluation with per-mode reporting should be standard practice.
25	
26	The asymmetry---reliable observer, unreliable optimizer---may generalize to other perturbation-based diagnostics; ISR and structurally similar metrics should be used as post-hoc evaluation, with future work targeting gaming-robust rewards and broader logic types.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0358814-81c5-4c6b-8c33-f6fd55cd3f6e",
  "isSidechain": true,
  "promptId": "a961140e-8650-4dcd-abbd-2232b8f4e9ad",
  "agentId": "ad21ca604b6e8710c",
  "type": "user",
  "uuid": "9e8f2005-6499-40ad-a901-30fc94602990",
  "sourceToolAssistantUUID": "d0358814-81c5-4c6b-8c33-f6fd55cd3f6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T20:13:21.568Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GwxXYNsJHCFQQFxqahChMS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e8f2005-6499-40ad-a901-30fc94602990",
  "isSidechain": true,
  "agentId": "ad21ca604b6e8710c",
  "requestId": "req_011Cb4xxyVvzszwmjg4JyuVh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be96367e-e56b-4e51-b596-eef25b67f770",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MYoEEqQg4QwLdAusgnpun",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2374,
      "cache_read_input_tokens": 24273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2374,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T20:13:21.573Z_

<details><summary>↩ Tool result · `toolu_01GwxXYNsJHCFQQFxqahChMS`</summary>

```text
1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.
5	ISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
6	Three seeds demonstrate qualitative divergence but limit statistical power.
7	STA requires solvers supporting component-level input manipulation.
8	
9	\paragraph{Data scale.}
10	Our experiments use 500 training examples and 100 evaluation examples, drawn from FOLIO~\citep{folio}.
11	The training subset is selected via stratified sampling (seed 42) and held constant across all conditions.
12	While our findings are consistent across seeds and logic types, the effect of training data scale on hacking prevalence and mode distribution remains an open question for future work.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be96367e-e56b-4e51-b596-eef25b67f770",
  "isSidechain": true,
  "promptId": "a961140e-8650-4dcd-abbd-2232b8f4e9ad",
  "agentId": "ad21ca604b6e8710c",
  "type": "user",
  "uuid": "4c5e7d36-1ffd-4846-824a-7e94bad75ee7",
  "sourceToolAssistantUUID": "be96367e-e56b-4e51-b596-eef25b67f770",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T20:13:22.036Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YRvYcDhD6nrvePCRzD8vBL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c5e7d36-1ffd-4846-824a-7e94bad75ee7",
  "isSidechain": true,
  "agentId": "ad21ca604b6e8710c",
  "requestId": "req_011Cb4xxyVvzszwmjg4JyuVh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45379a65-abe0-4e90-b7aa-bbb16ef61ba6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MYoEEqQg4QwLdAusgnpun",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2374,
      "cache_read_input_tokens": 24273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2374,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T20:13:22.043Z_

<details><summary>↩ Tool result · `toolu_01YRvYcDhD6nrvePCRzD8vBL`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning and process rewards.}
5	LLM-solver pipelines~\cite{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\cite{mellgren-prolog-grpo, logic-rl} evaluate execution accuracy alone, with no diagnostic for structural quality.
6	Learned PRMs~\cite{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\cite{processbench}; ISR is solver-grounded and annotation-free.
7	We use FOLIO~\cite{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Reward hacking and Goodhart's Law.}
10	Goodhart's Law is established theoretically~\cite{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF and frontier models~\cite{gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.
11	Recent work further documents spurious reward signals in RLVR~\cite{spurious-rewards} and reward hacking in frontier models~\cite{metr-reward-hacking}.
12	Our setting differs in three ways: ISR is deterministic and solver-derived rather than learned; gaming \emph{emerges during RL training} rather than at inference time; and the effect operates at a \emph{meta} level---the diagnostic for gaming itself becomes gamed when optimized---a phenomenon, to our knowledge, not previously documented.
13	
14	\paragraph{Mutation testing.}
15	STA adapts the LOO mutation paradigm~\cite{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45379a65-abe0-4e90-b7aa-bbb16ef61ba6",
  "isSidechain": true,
  "promptId": "a961140e-8650-4dcd-abbd-2232b8f4e9ad",
  "agentId": "ad21ca604b6e8710c",
  "type": "user",
  "uuid": "44291516-091a-4f51-81ee-f3764c2450ac",
  "sourceToolAssistantUUID": "45379a65-abe0-4e90-b7aa-bbb16ef61ba6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T20:13:22.570Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WiR22ZrKneJK1nBKzkNbad`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44291516-091a-4f51-81ee-f3764c2450ac",
  "isSidechain": true,
  "agentId": "ad21ca604b6e8710c",
  "requestId": "req_011Cb4xxyVvzszwmjg4JyuVh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d74a899c-5afb-4052-b4ed-d2555a016b40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MYoEEqQg4QwLdAusgnpun",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2374,
      "cache_read_input_tokens": 24273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2374,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T20:13:22.575Z_

<details><summary>↩ Tool result · `toolu_01WiR22ZrKneJK1nBKzkNbad`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{figures/fig1_sta_overview.pdf}
7	\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\ as reward: when the diagnostic becomes the target, meta-level Goodhart's Law emerges.}
8	\label{fig:sta-overview}
9	\end{figure*}
10	
11	\subsection{Task and GRPO Training}
12	\label{sec:task}
13	
14	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$ (\autoref{fig:sta-overview}a).
15	We train with GRPO~\citep{deepseekmath} ($K{=}8$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
16	This optimizes prove rate but provides no signal about \emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
17	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation file retains a legacy \texttt{proofwriter\_fol\_*.jsonl} filename (from ProofWriter~\citep{proofwriter}) but contains only FOLIO-derived examples.
18	
19	\subsection{Solver Trace Ablation (STA)}
20	\label{sec:sta}
21	
22	STA tests whether each component of a proved formalization is individually necessary for proof success (\autoref{fig:sta-overview}b).
23	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
24	A component is \emph{necessary} if its removal causes proof failure.
25	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
26	LOO ablation itself is standard in mutation testing and feature attribution; our novelty is its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.
27	
28	\begin{algorithm}[t]
29	\caption{Solver Trace Ablation (STA)}
30	\label{alg:sta}
31	\begin{algorithmic}[1]
32	\REQUIRE Proved formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
33	\ENSURE $\text{ISR}(x) \in [0, 1]$
34	\STATE $\textit{necessary} \gets 0$
35	\FOR{$i = 1$ to $n$}
36	    \IF{$S(x \setminus \{c_i\}) = \textit{failed}$}
37	        \STATE $\textit{necessary} \gets \textit{necessary} + 1$
38	    \ENDIF
39	\ENDFOR
40	\RETURN $\textit{necessary} \,/\, n$
41	\end{algorithmic}
42	\end{algorithm}
43	
44	\paragraph{Intensional Structural Reward.}
45	ISR is the fraction of necessary components:
46	\begin{equation}
47	  \text{ISR}(x) = \frac{1}{n}\sum_{i=1}^{n}\mathbf{1}\bigl[S(x\setminus\{c_i\})=\textit{failed}\bigr]
48	  \label{eq:isr}
49	\end{equation}
50	ISR is defined only for proved formalizations: ISR${=}1$ means every component is necessary; ISR${=}0$ means complete redundancy.
51	We report \emph{proved-only} ISR (denoted ISR$^*$) throughout to avoid conflating structural quality with prove rate.
52	
53	\paragraph{Limitations of ISR.}
54	ISR measures syntactic component necessity, not semantic faithfulness: a formalization can achieve $\text{ISR}{=}1$ while semantically unrelated to the NL input (e.g., a single premise identical to the conclusion).
55	ISR is also sensitive to component count $n$: when $n{=}2$, $\text{ISR}\geq 0.5$ regardless of proof quality.
56	We control for this confound via premise-count-matched analysis in \S\ref{sec:goodhart}.
57	The $O(n)$ per-clause LOO ablation is necessary: a cheaper $O(1)$ binary variant produces near-zero ISR scores ($\text{ISR}^*{=}0.007$) indistinguishable from exec-only, because models generate redundant premise copies whose individual removal never changes the proof outcome.
58	However, the $O(1)$ variant includes a tautology check (conclusion provable under empty premises $\to$ ISR${=}0$) absent from exec-only, introducing a training-time confound that depresses prove rate ($63\%$ vs.\ $93\%$ exec-only); the two conditions are therefore non-equivalent in training dynamics despite producing comparable ISR signals (Appendix~\ref{app:o1-ablation}).
59	
60	\subsection{Reward Conditions and Hacking Modes}
61	\label{sec:rewards}
62	\label{sec:taxonomy-method}
63	
64	We study six conditions: exec-only ($r_{\text{exec}}$), ISR low/high-dose ($r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ at $\beta\in\{0.1,0.3\}$), matched random controls ($r_{\text{exec}}\cdot(1{+}\beta u)$, $u\sim\mathcal{U}(0,1)$), and an SFT baseline (NLL on gold formalizations).
65	Multiplicative bonuses apply only to proved samples, keeping the prove-rate floor intact.
66	Random isolates ISR-specific signal from generic reward-variance effects; SFT isolates whether structural degeneration arises from RL optimization or data exposure alone.
67	Each RL condition uses seeds $\{42,43,44\}$ and identical training data.
68	An earlier convex formulation ($\alpha r_{\text{exec}} + \beta r_{\text{exec}}\text{ISR}$, $\alpha{+}\beta{=}1$) was discarded because $\text{ISR}{<}1$ always penalized relative to exec-only, collapsing PR (Appendix~\ref{app:setup}).
69	
70	\paragraph{Hacking taxonomy.}
71	Across conditions, seeds, and logic types we identify eight structural-degeneration modes (full definitions in Appendix~\ref{app:hacking-modes}):
72	\textbf{H1} (conclusion embedded among multiple premises),
73	\textbf{H7} (single-premise conclusion duplication, subtypes H7a standard and H7b obfuscated tautology; targets the ISR signal directly, since removing the sole premise forces $\text{ISR}\geq 0.5$),
74	\textbf{H8} (premise-subset gaming: each component is LOO-necessary but the premise set is a strict subset of what the problem requires, inflating ISR without faithful reasoning; Appendix~\ref{app:h8}),
75	\textbf{tautological collapse} (minimal two-component $P{\to}P$ without explicit ISR inflation),
76	\textbf{repetition collapse} (identical clauses repeated to inflate component count),
77	\textbf{complexity-without-utility} (elaborate but vacuous premises),
78	\textbf{contradiction explosion} (contradictory premises trivializing any conclusion via \emph{ex falso}), and
79	\textbf{query-as-fact gaming} (Prolog-specific: emit the NL question as an atom asserted as both fact and query; evades text-match classifiers).
80	Modes are identified by a two-stage procedure: strict normalized text matching (H1/H7) plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution (catches modes evading text matching).
81	We report both classifications in \S\ref{sec:experiments}.
82	
83	In interpreting ISR results we distinguish two failure semantics that share a numerical signature: an exec-only \emph{low} ISR signals \emph{redundancy} (e.g., repeated ground facts in Prolog), whereas an ISR-rewarded \emph{high} ISR signals \emph{metric gaming} (H7-style constructions).
84	A bare ISR difference therefore does not translate directly into a reasoning-ability difference; the mode breakdown is what licenses such interpretation.
85	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d74a899c-5afb-4052-b4ed-d2555a016b40",
  "isSidechain": true,
  "promptId": "a961140e-8650-4dcd-abbd-2232b8f4e9ad",
  "agentId": "ad21ca604b6e8710c",
  "type": "user",
  "uuid": "f579312a-d39f-4e39-ba89-94fbc1408060",
  "sourceToolAssistantUUID": "d74a899c-5afb-4052-b4ed-d2555a016b40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T20:13:23.183Z_

<details open><summary>🔧 Tool call — Read · `toolu_014emWdwobgMracX8nDXnQgr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f579312a-d39f-4e39-ba89-94fbc1408060",
  "isSidechain": true,
  "agentId": "ad21ca604b6e8710c",
  "requestId": "req_011Cb4xxyVvzszwmjg4JyuVh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff7c3857-31e3-4ddc-943b-2bb96227f5af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MYoEEqQg4QwLdAusgnpun",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2374,
      "cache_read_input_tokens": 24273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2374,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T20:13:23.602Z_

<details><summary>↩ Tool result · `toolu_014emWdwobgMracX8nDXnQgr`</summary>

```text
1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[h]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 8 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Evaluation exception.}
53	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
54	Its PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).
55	
56	
57	\section{STA Algorithm}
58	\label{app:algorithm}
59	
60	Algorithm~\ref{alg:sta} (Section~\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.
61	For unproved samples ($S(x) \neq \textit{proved}$), ISR is undefined and the protocol is not applied.
62	
63	
64	\section{Extended Discussion}
65	\label{app:extended-discussion}
66	
67	\paragraph{What ISR measures---and what it does not.}
68	ISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.
69	This is strictly weaker than semantic faithfulness---whether the formalization accurately captures the natural-language meaning.
70	We verify this empirically: Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.
71	ISR and downstream task performance are uncorrelated.
72	ISR is thus a structural integrity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.
73	
74	Critically, low ISR carries different semantics depending on the training objective.
75	Under exec-only training, low ISR in Prolog reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning (\S\ref{sec:crosslogic}).
76	Under ISR-as-reward, high ISR reflects metric gaming (\S\ref{sec:goodhart}).
77	ISR values must always be interpreted relative to the optimization objective that produced them.
78	
79	\paragraph{The premise-count confound.}
80	LOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.
81	A formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$---even though the latter encodes richer reasoning.
82	This confound explains the sole apparent ISR-as-reward success (\S\ref{sec:goodhart}): ISR $\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.
83	Premise-count-matched comparison eliminates the difference ($1.06\times$; Table~\ref{tab:fol-beta01-detailed}).
84	This bias is not specific to our setting---any LOO-based structural metric applied to variable-length outputs requires component-count normalization.
85	We recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.
86	
87	\begin{table}[h]
88	\centering
89	\caption{Fisher exact tests for genuine rate across conditions (3-seed pooled). ISR $\beta{=}0.1$ genuine rate is corrected for H8 reclassification and H7 false negatives (Appendix~\ref{app:h8}).}
90	\label{tab:bootstrap-ci}
91	\small
92	\begin{tabular}{@{}lcccc@{}}
93	\toprule
94	\textbf{Comparison} & \textbf{Condition} & \textbf{Control} & \textbf{OR} & \textbf{$p$} \\
95	\midrule
96	\multicolumn{5}{@{}l}{\textit{Genuine rate (H8+FN corrected)}} \\
97	ISR vs.\ Random & 6.06\% {\scriptsize[3.6,9.9]} & 9.5\% {\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\
98	ISR vs.\ Exec-only & 6.06\% & 7.5\% & 0.79 & 0.62 \\
99	Random vs.\ Exec-only & 9.5\% & 7.5\% & 1.30 & 0.68 \\
100	\midrule
101	\multicolumn{5}{@{}l}{\textit{H7 gaming rate}} \\
102	ISR vs.\ Random & 70.6\% {\scriptsize[64.3,76.3]} & 13.7\% {\scriptsize[9.9,18.6]} & 15.05 & $1.3{\times}10^{-39}$ \\
103	\midrule
104	\multicolumn{5}{@{}l}{\textit{SFT vs.\ Exec-only genuine rate}} \\
105	SFT vs.\ Exec-only & 92.3\% {\scriptsize[79.7,97.3]} & 7.5\% & 147 & ${<}0.001$ \\
106	\bottomrule
107	\end{tabular}
108	\\[2pt]
109	{\footnotesize ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\% Wilson CIs in brackets where shown.}
110	\end{table}
111	
112	\paragraph{Meta-level Goodhart: implications.}
113	The meta-Goodhart finding extends beyond this specific system.
114	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself---creating a regress where any diagnostic metric risks becoming a target when optimized.
115	The dose-response pattern ($\beta{=}0.1$: proxy gaming inflates ISR without genuine improvement; $\beta{=}0.3$: PR collapse to 18\% vs.\ 48\% random) maps onto the trajectory predicted by~\cite{gao-reward-overoptimization}, but at a meta level: the proxy being gamed is itself a gaming detector.
116	$\beta{=}0.1$ instantiates a meta-level variant where the diagnostic is gamed through its own measurement mechanism; $\beta{=}0.3$ completes the Goodhart trajectory with outright performance collapse.
117	The practical implication is that ISR---and structurally similar diagnostics---should be used exclusively as post-hoc evaluation tools, never as training rewards.
118	
119	\paragraph{Single-seed unreliability.}
120	The three exec-only seeds diverge radically (PR $\sigma{=}\pm 47$ percentage points), each converging to a qualitatively different degeneration mode (\S\ref{sec:diagnostic}).
121	ISR $\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (H7), 1/3 by premise minimization (\S\ref{sec:goodhart}).
122	Multi-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.
123	
124	
125	\section{Hacking Mode Definitions}
126	\label{app:hacking-modes}
127	
128	We identify eight distinct reward hacking modes across all experiments.
129	Each mode is defined below with its mechanism, a representative example, and its interaction with ISR.
130	Table~\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.
131	
132	\begin{table}[h]
133	\centering
134	\small
135	\resizebox{\columnwidth}{!}{%
136	\begin{tabular}{@{}llcccc@{}}
137	\toprule
138	\textbf{Mode} & \textbf{Mechanism} & \textbf{Exec} & \textbf{ISR} & \textbf{Rnd} & \textbf{SFT} \\
139	\midrule
140	H1 & Concl.\ in premises & 87 & 18 & 81 & 7 \\
141	H7 & Single prem.\ = concl. & $\bullet$ & \textbf{71} & 14$^\dagger$ & 0 \\
142	H8 & Premise-subset gaming & 6 & 5 & -- & 0 \\
143	Tautological & 2-comp $P{=}C$ & $\bullet$ & 0 & 0 & 0 \\
144	Repetition & Output degen. & $\bullet$ & -- & -- & -- \\
145	Contradiction & $n_{\text{comp}}$ inflated & $\bullet$ & -- & -- & -- \\
146	C-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\
147	Q-as-fact & Atom = fact+query & -- & -- & -- & -- \\
148	\bottomrule
149	\end{tabular}}
150	\caption{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta{=}0.1$ 3-seed pooled. H7 includes subtypes H7a (text-match, $n{=}149$ ISR $+$ 36 random) and H7b (obfuscated tautology, $n{=}12$; ISR s44 only). $^\dagger$Random H7 driven by seed~43 (38.3\%); seeds~42/44: 0\%. Exec: H1${=}87$\% in s42; $\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). H8: premise-subset gaming (Appendix~\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref{tab:prolog-detailed}).}
151	\label{tab:hacking-taxonomy-app}
152	\end{table}
153	
154	\paragraph{Classifier Validation.}
155	Hacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.
156	H1 and H7 are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\text{necessary}}$ distribution from STA (leave-one-out ablation).
157	No training data or manual annotation is used for classification.
158	
159	To estimate precision, we manually verified 50 randomly sampled outputs classified as H1 or H7: all 50 were confirmed correct (estimated precision ${>}$95\%, Wilson 95\% CI: [93\%, 100\%]).
160	Recall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.
161	We cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\text{necessary}} \leq 1$ are flagged as potential false negatives.
162	This cross-validation revealed query-as-fact gaming in Prolog (\S\ref{app:hacking-modes}), where the strict text classifier reported 100\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\text{necessary}}{=}1$).
163	The non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.
164	
165	\subsection{H8 --- Premise-Subset Gaming}
166	\label{app:h8}
167	
168	Manual audit of ISR $\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (H1-style).
169	We term this \textbf{H8 (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.
170	
171	\paragraph{Detection.} H8 is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\text{prem}} \leq 3$) that nonetheless achieve high ISR.
172	Automated detection is not currently feasible because H8 requires comparing the generated premise set against the gold premises.
173	
174	\paragraph{Audit scope and limitations.}
175	Full H8 audit was completed for ISR $\beta{=}0.1$ seed~42 only.
176	ISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their genuine rates may be overestimated.
177	Random $\beta{=}0.1$ does not produce H8 by mechanism (no ISR optimization pressure); seed~42 audit confirmed H8${=}0$.
178	
179	\paragraph{H7 false-negative correction (H7b obfuscated tautology).}
180	ISR $\beta{=}0.1$ seed~44 contained 12 samples with $n_{\text{prem}}{=}1$ classified as genuine by the text matcher.
181	Manual inspection confirmed all 12 are logically equivalent to H7 but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).
182	We classify these as \textbf{H7b} (obfuscated tautology), distinct from text-match-detectable H7a.
183	$10/12$ achieve $\text{ISR}{\approx}0.8$, indicating simultaneous gaming of execution reward, ISR metric, and H7 classifier---triple gaming (\S\ref{sec:taxonomy}).
184	After correction, ISR s44 genuine${=}0$; total H7 = H7a (77 text-match) + H7b (12 obfuscated) = 89.
185	
186	\paragraph{Impact on genuine-rate comparison.}
187	After H8 reclassification and H7 false-negative correction: ISR genuine $= 14/231 = 6.06\%$ vs.\ random genuine $= 25/262 = 9.5\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\% CI: ISR [3.6\%, 9.9\%], Random [6.5\%, 13.7\%]).
188	The direction is consistent with ISR-amplified gaming modes (H7, H8) displacing genuine output, but the effect is not statistically significant at the conventional $\alpha{=}0.05$ threshold.
189	
190	\subsection{H1 --- Conclusion Embedding}
191	
192	\paragraph{Definition.}
193	The conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.
194	The solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.
195	
196	\paragraph{Example (FOL).}
197	{\small\begin{verbatim}
198	Premises:
199	  all x (bird(x) -> flies(x)).
200	  bird(tweety).
201	  flies(tweety).  % conclusion embedded
202	Conclusion: flies(tweety).
203	\end{verbatim}}
204	
205	\paragraph{ISR interaction.}
206	Variable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.
207	ISR does not distinguish trivial from substantive necessity.
208	
209	\paragraph{Prevalence.}
210	Conclusion embedding in some form (H1 multi-premise or H7 single-premise) is GRPO-universal at 68--97\% across all RL conditions.
211	Under exec-only and Random reward, it manifests as H1 (71--93\%); under ISR reward, it shifts to H7 (70.6\% pooled).
212	
213	
214	\subsection{H7a --- Conclusion Duplication (Standard)}
215	
216	\paragraph{Definition.}
217	The entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.
218	Since $P \to P$ is trivially provable, this simultaneously maximizes exec reward.
219	Because the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.
220	
221	\paragraph{Example (FOL).}
222	{\small\begin{verbatim}
223	Premises:
224	  all x ((A(x)&B(x))->(C(x)|D(x))).
225	Conclusion:
226	  all x ((A(x)&B(x))->(C(x)|D(x))).
227	\end{verbatim}}
228	
229	\paragraph{ISR interaction.}
230	ISR~$\approx 0.8$--$1.0$.
231	The single premise is trivially ``maximally necessary,'' but the proof is vacuous.
232	H7a games both exec reward and ISR reward; H7b extends this to triple gaming by additionally evading the text-match classifier.
233	
234	\paragraph{Prevalence.}
235	H7a (text-match detectable): 64.5\% pooled (149/231) under ISR~$\beta{=}0.1$ (s42: 16.0\%, s43: 96.7\%, s44: 86.5\%).
236	Combined H7 (H7a + H7b): 70.6\% (163/231; s43 H7a${=}59$ + H7b${=}2$; includes s44 FN correction).
237	Random~$\beta{=}0.1$ pooled: 13.7\% (36/262, all H7a; driven by seed~43 at 38.3\%, seeds~42 and~44 at 0\%).
238	
239	
240	\subsection{H7b --- Obfuscated Tautology}
241	
242	\paragraph{Definition.}
243	A single-premise formalization logically equivalent to H7a (premise = conclusion) but with surface-form differences that evade the text-match H7 classifier.
244	The model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).
245	
246	\paragraph{Example (FOL, vacuous quantifier wrapping).}
247	{\small\begin{verbatim}
248	Premises:
249	  all x all y ((A(x)&B(y))->(C(x)|D(y))).
250	Conclusion:
251	  all x ((A(x)&B(x))->(C(x)|D(x))).
252	\end{verbatim}}
253	The premise introduces a vacuous second quantifier variable $y$ that is immediately unified with $x$, making the formulas logically equivalent while differing textually.
254	
255	\paragraph{ISR interaction.}
256	ISR~$\approx 0.8$ ($10/12$ samples).
257	H7b simultaneously games three objectives: execution reward ($r_{\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match H7 classifier (surface-form difference evades detection).
258	This triple gaming makes H7b the most complete meta-Goodhart case we observe.
259	
260	\paragraph{Prevalence.}
261	Found exclusively in ISR $\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as genuine).
262	Functional cross-validation via $n_{\text{necessary}}{=}1$ exposed the misclassification.
263	
264	
265	\subsection{Tautological Collapse}
266	
267	\paragraph{Definition.}
268	Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \to P$ tautology with minimal token cost.
269	
270	\paragraph{Example (FOL).}
271	\begin{verbatim}
272	Premises: p(a).
273	Conclusion: p(a).
274	\end{verbatim}
275	
276	\paragraph{ISR interaction.}
277	ISR~$=1.0$ (the sole premise is necessary).
278	Distinguished from H7 by having low component count ($n_{\text{comp}}\approx 2$) and atomic formulas rather than complex sub-structured conclusions.
279	
280	\paragraph{Prevalence.}
281	Dominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\text{comp}}=2.04$, 100\% H7 by strict classifier).
282	Also observed in Prolog exec+STA seed~42 (100\% H7, PR~$=0.50$).
283	
284	
285	\subsection{Repetition Collapse}
286	
287	\paragraph{Definition.}
288	The model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.
289	Removing any single repeated copy leaves the others intact, yielding ISR~$\approx 0$.
290	
291	\paragraph{Example (Prolog).}
292	\begin{verbatim}
293	penguin(fido).
294	penguin(fido).
295	penguin(fido).
296	... (repeated to 512 tokens)
297	query(penguin(fido)).
298	\end{verbatim}
299	
300	\paragraph{ISR interaction.}
301	ISR~$\approx 0$. Each copy is individually redundant since identical copies remain after removal.
302	ISR correctly diagnoses this degeneration.
303	
304	\paragraph{Prevalence.}
305	Observed in FOL exec-only seed~43 (87\% of outputs hit max completion length; PR~$=13$\%, ISR~$=0$).
306	
307	
308	\subsection{Complexity-without-Utility}
309	
310	\paragraph{Definition.}
311	The formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous---none individually necessary for the proof.
312	The complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.
313	
314	\paragraph{Example (FOL).}
315	{\small\begin{verbatim}
316	Premises:
317	  all x all y (R(x,y) ->
318	    exists z (S(x,z) & T(z,y))).
319	  all x (P(x) -> Q(x)).
320	  P(a).            % only this needed
321	Conclusion: Q(a).
322	\end{verbatim}}
323	
324	\paragraph{ISR interaction.}
325	ISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.
326	This is the mode ISR is best calibrated for.
327	
328	\paragraph{Prevalence.}
329	Low. Observed in Random~$\beta{=}0.1$ seed~42 at 3.8\% (3/79).
330	Not observed under ISR reward (ISR's gradient discourages zero-ISR premises).
331	
332	
333	\subsection{Contradiction Explosion}
334	
335	\paragraph{Definition.}
336	The component count grows unboundedly over training.
337	Excess premises introduce contradictions or redundancies that trivially entail any conclusion via \emph{ex falso quodlibet}.
338	Individual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.
339	
340	\paragraph{Example (FOL, 1000-step exec-only).}
341	{\small\begin{verbatim}
342	Premises:
343	  c1. c2. c3. ... c18. % 18.55 mean
344	  % conclusion embedded among premises
345	Conclusion: Q(a).
346	\end{verbatim}}
347	
348	\paragraph{ISR interaction.}
349	ISR~$\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\% of proved samples having ISR~$=0$).
350	
351	\paragraph{Prevalence.}
352	Observed in extended exec-only training (seed~42, 1000 steps).
353	Mean component count grows from ${\sim}6$ (500 steps) to 18.55 (1000 steps).
354	
355	
356	\subsection{Query-as-Fact Gaming}
357	
358	\paragraph{Definition.}
359	The model converts the natural language conclusion into a snake\_case atom and includes it as both a ground fact and the query.
360	Prolog trivially proves the query by unifying with the fact.
361	This mode evades text-match classifiers designed for H1/H7 because the generated atom bears no surface resemblance to the original conclusion text.
362	
363	\paragraph{Example (Prolog).}
364	\begin{verbatim}
365	% NL: "Fido is happy."
366	% Model output:
367	fido_is_happy.
368	:- fido_is_happy.     % query = fact
369	\end{verbatim}
370	
371	\paragraph{ISR interaction.}
372	ISR~$\approx 0.9$--$1.0$.
373	The fact is necessarily necessary (its removal breaks the query), inflating ISR.
374	Functionally equivalent to H7 but with a distinct surface mechanism.
375	
376	\paragraph{Prevalence.}
377	Observed in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).
378	95/97 proved samples have $n_{\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\% non-hacking.
379	
380	
381	\section{Per-Seed Detailed Results}
382	\label{app:detailed-results}
383	
384	Tables~\ref{tab:fol-beta01-detailed} and \ref{tab:prolog-detailed} report full per-seed results.
385	All metrics are computed by \texttt{eval\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.
386	ISR values are proved-only ISR$^*$.
387	
388	\begin{table*}[t]
389	\centering
390	\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\beta{=}0.1$ breakdown referenced from Table~\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$). $^\ddagger$Three s44-1000 samples escape text-match heuristics (H1/H8 classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass H8 detection and commuted premises that bypass H1 detection; reclassified as degenerate. $^\S$s43-1000 raw ISR (0.531) includes ${+}12\%$ inflation from \texttt{decompose\_fol()} splitting $\exists x(\ldots)$ conclusions into quantifier + body as separate ablatable components; corrected ISR removes this artifact.}
391	\label{tab:fol-detailed}
392	\label{tab:fol-beta01-detailed}
393	\footnotesize
394	\setlength{\tabcolsep}{3pt}
395	\begin{tabular}{@{}llccccccl@{}}
396	\toprule
397	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Notes} \\
398	\midrule
399	\multicolumn{9}{@{}l}{\textit{Baselines}} \\
400	Base model (no training)
401	  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
402	Ground-truth FOL
403	  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
404	SFT
405	  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \textbf{92.3} & Supervised, no RL \\
406	  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \textbf{90.9} & \\
407	  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \textbf{93.3} & \\
408	\cmidrule(l){2-9}
409	  & \multicolumn{2}{l}{3-seed pooled} & \makebox[0pt][l]{$0.130$} & & \makebox[0pt][l]{$0.595$} & & \makebox[0pt][l]{\textbf{92.3}} & $n{=}39$ proved \\
410	\midrule
411	\multicolumn{9}{@{}l}{\textit{Exec-only}} \\
412	  & 42 & 100 & 0.32 & \textbf{0.642} & --- & --- & --- & Early checkpoint \\
413	  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & H8${=}6.5\%$ \\
414	  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\
415	  & 43 & 500 & 0.13 & 0$^\dagger$ & --- & --- & --- & $^\dagger$Greedy ($n_{\text{proved}}{=}13$) \\
416	  & 43 & 1000 & 0.90 & 0.465$^\S$ & 100 & 0 & 0 & H7 dominant \\
417	  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\
418	  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\ddagger$ & H8${=}15\%$ \\
419	\cmidrule(l){2-9}
420	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.68{\pm}0.47$} & & \makebox[0pt][l]{$0.238{\pm}0.30$} & & & 500-step \\
421	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.95{\pm}0.05$} & & \makebox[0pt][l]{$0.16{\pm}0.27$} & & \makebox[0pt][l]{$0.0{\pm}0.0$} & 1000-step \\
422	\midrule
423	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
424	  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \textbf{17.3} & Mixed H1+H7+H8 \\
425	  & 43 & 500 & 0.61 & 0.830 & \textbf{100} & 0 & 0 & H7a${=}59$, H7b${=}2$ \\
426	  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & H7 dominant (FN corrected) \\
427	\cmidrule(l){2-9}
428	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.77{\pm}0.14$} & & \makebox[0pt][l]{$0.716{\pm}0.26$} & & & \\
429	\midrule
430	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
431	  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & PR collapse \\
432	\midrule
433	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.1$}} \\
434	  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & H8${=}4$ \\
435	  & 43 & 500 & 0.94 & 0.150 & \textbf{38.3} & 59.6 & 1.1 & H7a${=}36$; H8${=}1$ \\
436	  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & H8${=}16$ (H1$\cap$H8: 6) \\
437	\cmidrule(l){2-9}
438	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.87{\pm}0.08$} & & \makebox[0pt][l]{$0.117{\pm}0.042$} & & & H7 seed-dep.: 0/38/0\% \\
439	\midrule
440	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
441	  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086); $n_{\text{comp}} = 9.6$ \\
442	\bottomrule
443	\end{tabular}
444	\end{table*}
445	
446	
447	\begin{table*}[t]
448	\centering
449	\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\ = percentage among proved samples.  ``---'' indicates data not available.}
450	\label{tab:prolog-detailed}
451	\small
452	\begin{tabular}{@{}llcccccl@{}}
453	\toprule
454	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Notes} \\
455	\midrule
456	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
457	  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\
458	  & 43 & 0.56 & 0.015 & --- & --- & --- & \\
459	  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\
460	\cmidrule(l){2-8}
461	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.53{\pm}0.31$} & & \makebox[0pt][l]{$0.146{\pm}0.21$} & & \\
462	\midrule
463	\multicolumn{8}{@{}l}{\textit{Exec+ISR (STA reward)}} \\
464	  & 42 & 0.50 & 1.000 & \textbf{100} & 0 & 0 & H7 tautological \\
465	  & 43 & 0.38 & 0.185 & 0$^\ddagger$ & 97.4 & 0 & $^\ddagger$Functional H7$^a$ \\
466	  & 44 & 0.97 & 0.912 & 0$^\ddagger$ & 0 & 0$^\ddagger$ & Query-as-fact gaming$^b$ \\
467	\cmidrule(l){2-8}
468	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.62{\pm}0.31$} & & \makebox[0pt][l]{$0.699{\pm}0.45$} & & 3/3 Goodhart, 0\% non-hacking \\
469	\bottomrule
470	\end{tabular}
471	
472	\vspace{4pt}
473	{\footnotesize
474	$^a$ Strict H7 classifier reports 0\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\
475	$^b$ Strict classifier reports Non-hacking$\,{=}\,100$\%, but 95/97 proved samples have $n_{\text{necessary}}=1$. The model converts NL to snake\_case atoms serving as both fact and query---a third distinct Goodhart pathway.\\
476	$^\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.
477	}
478	\end{table*}
479	
480	\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}
481	Table~\ref{tab:fol-detailed} traces the ISR collapse over training:
482	ISR$^*=0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4$\%) $\to$ $0.003$ at 1000 steps ($-99.5$\% from step 100).
483	PR increases monotonically ($0.32 \to 0.93 \to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.
484	By step 1000, 94.8\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.
485	
486	\paragraph{Prolog: universal Goodhart via three distinct pathways.}
487	All three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\% non-hacking proofs (Figure~\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:
488	seed~42 produces clean H7 tautologies (single premise~$=$~conclusion),
489	seed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,
490	and seed~44 converts NL conclusions to snake\_case atoms used as both fact and query.
491	The diversity of gaming pathways across seeds---despite identical training data and reward function---demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.
492	
493	\subsection{Per-Seed Results at $\beta{=}0.3$}
494	\label{app:beta03}
495	
496	Table~\ref{tab:beta03-detailed} reports per-seed results for both ISR and Random reward at $\beta{=}0.3$.
497	The three ISR seeds illustrate qualitatively distinct Goodhart pathways (\S\ref{sec:goodhart}).
498	
499	\begin{table}[h]
500	\centering
501	\caption{Per-seed results at $\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H = percentage among proved samples.}
502	\label{tab:beta03-detailed}
503	\small
504	\begin{tabular}{@{}llcccccl@{}}
505	\toprule
506	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Mode} \\
507	\midrule
508	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
509	  & 42 & 0.18 & 0.143 & 0 & 77.8 & 22.2 & Reward collapse ($n{=}18$) \\
510	  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 26.7 & H1 shortcutting \\
511	  & 44 & 0.95 & 0.742 & \textbf{100} & 0 & 0 & Pure H7 meta-Goodhart \\
512	\cmidrule(l){2-8}
513	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.66{\pm}0.42$} & & \makebox[0pt][l]{$0.39{\pm}0.31$} & & \\
514	\midrule
515	\multicolumn{8}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
516	  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086) \\
517	  & 43 & 0.92 & 0.180 & 7.6 & 90.2 & 2.2 & \\
518	  & 44 & 0.23 & 0 & 0 & 100 & 0 & \\
519	\cmidrule(l){2-8}
520	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.54{\pm}0.35$} & & \makebox[0pt][l]{$0.09{\pm}0.09$} & & \\
521	\bottomrule
522	\end{tabular}
523	\end{table}
524	
525	\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}
526	\label{app:100step}
527	
528	To control for the prove-rate confound in our SFT comparison (\S\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\%---higher than SFT (13.0\%, 3-seed pooled) but still early in training.
529	Of the 32 proved samples, 9 (28.1\%) exhibit H7 hacking (single premise identical to conclusion) and 1 (3.1\%) exhibits H1 (conclusion embedded among premises), yielding a total hacking rate of 31.2\%.
530	By contrast, SFT at comparable or lower PR shows 7.7\% hacking (1/13 proved samples).
531	This demonstrates that reward hacking emerges early in GRPO training---well before the prove-rate plateau---and is not simply an artifact of having more proved samples available for exploitation.
532	The 100-step hacking rate (31.2\%) is already substantially above SFT (7.7\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.
533	
534	\subsection{$O(1)$ vs.\ $O(n)$ ISR Ablation}
535	\label{app:o1-ablation}
536	
537	To justify the per-clause LOO design (\S\ref{sec:sta}), we train a variant that replaces the $O(n)$ ablation with a cheaper $O(1)$ binary signal: $\text{fast\_ISR}(x) = 1$ if $x$ is proved \emph{and} the conclusion is not provable under empty premises (tautology check), $0$ otherwise.
538	The reward becomes $r = 0.5\,r_{\text{exec}} + 0.5\,\text{fast\_ISR}$.
539	After 500 steps (seed~42), this variant achieves $\text{PR}{=}63\%$ with $\text{ISR}^*{=}0.007$---functionally zero---compared to $\text{ISR}^*{=}0.132$ under standard exec-only and $\text{ISR}^*{=}0.42$ under ISR $\beta{=}0.1$.
540	
541	\paragraph{ISR signal vs.\ training dynamics.}
542	At the \emph{ISR signal level}, the $O(1)$ variant is indistinguishable from exec-only: both produce near-zero ISR because models emit redundant premise copies whose individual removal never changes the proof outcome.
543	At the \emph{training level}, the two conditions are non-equivalent: the $O(1)$ tautology check penalizes formalizations where the conclusion is provable without any premises, a constraint absent from exec-only.
544	This confound depresses prove rate by 30 percentage points ($63\%$ vs.\ $93\%$ exec-only), making it impossible to attribute the difference purely to the ISR signal.
545	The result confirms that the $O(n)$ per-clause ablation is necessary for ISR to carry a structural signal, while also showing that even a minimal tautology guard alters training dynamics substantially.
546	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff7c3857-31e3-4ddc-943b-2bb96227f5af",
  "isSidechain": true,
  "promptId": "a961140e-8650-4dcd-abbd-2232b8f4e9ad",
  "agentId": "ad21ca604b6e8710c",
  "type": "user",
  "uuid": "0d043b31-b33c-4b8b-908e-a2bf81415db1",
  "sourceToolAssistantUUID": "ff7c3857-31e3-4ddc-943b-2bb96227f5af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T20:13:23.628Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SiaUmmtL766GaDCstpxEmf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d043b31-b33c-4b8b-908e-a2bf81415db1",
  "isSidechain": true,
  "agentId": "ad21ca604b6e8710c",
  "requestId": "req_011Cb4xxyVvzszwmjg4JyuVh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bda72112-2283-42e8-a286-134f00232258",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MYoEEqQg4QwLdAusgnpun",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2374,
      "cache_read_input_tokens": 24273,
      "output_tokens": 689,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2374
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 689,
          "cache_read_input_tokens": 24273,
          "cache_creation_input_tokens": 2374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2374,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T20:13:23.634Z_

<details><summary>↩ Tool result · `toolu_01SiaUmmtL766GaDCstpxEmf`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
15	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
16	\setlength{\abovecaptionskip}{4pt}
17	\setlength{\belowcaptionskip}{2pt}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in a GRPO-Trained Neurosymbolic Formalizer: A Case Study with Qwen3-4B}
22	
23	\author{Anonymous ACL submission}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{conclusion}
34	
35	\bibliography{references}
36	
37	\input{limitations}
38	
39	\appendix
40	\input{appendix}
41	
42	\end{document}
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bda72112-2283-42e8-a286-134f00232258",
  "isSidechain": true,
  "promptId": "a961140e-8650-4dcd-abbd-2232b8f4e9ad",
  "agentId": "ad21ca604b6e8710c",
  "type": "user",
  "uuid": "75194241-e6b8-4523-b44e-93fa62006080",
  "sourceToolAssistantUUID": "bda72112-2283-42e8-a286-134f00232258",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-15T20:13:28.128Z_

Now let me check the references.bib file and see if there are any other tex files I might have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75194241-e6b8-4523-b44e-93fa62006080",
  "isSidechain": true,
  "agentId": "ad21ca604b6e8710c",
  "requestId": "req_011Cb4xyXUXzrUyXLBWqAsjk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aea61edc-7083-4ada-962a-93145ffa7e70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PzSZjyKTovBuNm8UMYdcu2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28258,
      "cache_read_input_tokens": 26647,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28258,
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

_source line 33 · 2026-05-15T20:13:30.003Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Cefscqmw5Schh1DZ1cTAnd`</summary>

```json
{
  "pattern": "*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aea61edc-7083-4ada-962a-93145ffa7e70",
  "isSidechain": true,
  "agentId": "ad21ca604b6e8710c",
  "requestId": "req_011Cb4xyXUXzrUyXLBWqAsjk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f196e4c-3c35-4de4-be2c-e44b81eeb46c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PzSZjyKTovBuNm8UMYdcu2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28258,
      "cache_read_input_tokens": 26647,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 28258
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 26647,
          "cache_creation_input_tokens": 28258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 28258,
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

_source line 34 · 2026-05-15T20:13:30.025Z_

<details><summary>↩ Tool result · `toolu_01Cefscqmw5Schh1DZ1cTAnd`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f196e4c-3c35-4de4-be2c-e44b81eeb46c",
  "isSidechain": true,
  "promptId": "a961140e-8650-4dcd-abbd-2232b8f4e9ad",
  "agentId": "ad21ca604b6e8710c",
  "type": "user",
  "uuid": "4f1e309c-dc4f-4775-88a3-52ce710600d2",
  "sourceToolAssistantUUID": "6f196e4c-3c35-4de4-be2c-e44b81eeb46c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T20:13:32.539Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RBrSARBqTNW8S6cH5AQMHx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f1e309c-dc4f-4775-88a3-52ce710600d2",
  "isSidechain": true,
  "agentId": "ad21ca604b6e8710c",
  "requestId": "req_011Cb4xyzuJ5TXJrDc8oYZ7L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dfce37c6-d700-4b16-898b-fa069795daf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EGPakBQxxCHvZo5ZiRANtw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 171,
      "cache_read_input_tokens": 54905,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 171
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 54905,
          "cache_creation_input_tokens": 171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 171,
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

_source line 36 · 2026-05-15T20:13:32.547Z_

<details><summary>↩ Tool result · `toolu_01RBrSARBqTNW8S6cH5AQMHx`</summary>

```text
1	% ============================================================
2	% Category 1: Neurosymbolic reasoning + RL/GRPO
3	% ============================================================
4	
5	@article{deepseekmath,
6	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
7	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
8	  journal      = {arXiv preprint arXiv:2402.03300},
9	  year         = {2024},
10	  eprint       = {2402.03300},
11	  archivePrefix = {arXiv},
12	  primaryClass = {cs.AI},
13	}
14	
15	@article{logic-rl,
16	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
17	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
18	  journal      = {arXiv preprint arXiv:2502.14768},
19	  year         = {2025},
20	  eprint       = {2502.14768},
21	  archivePrefix = {arXiv},
22	  primaryClass = {cs.AI},
23	}
24	
25	@article{mellgren-prolog-grpo,
26	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
27	  title        = {{Training Language Models to Use Prolog as a Tool}},
28	  journal      = {arXiv preprint arXiv:2512.07407},
29	  year         = {2025},
30	  eprint       = {2512.07407},
31	  archivePrefix = {arXiv},
32	  primaryClass = {cs.AI},
33	}
34	
35	@inproceedings{satlm,
36	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
37	  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},
38	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
39	  year         = {2023},
40	}
41	
42	% ============================================================
43	% Category 2: Reward shaping for code/formal verification
44	% ============================================================
45	
46	@inproceedings{lightman-verify-step,
47	  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},
48	  title        = {{Let's Verify Step by Step}},
49	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
50	  year         = {2024},
51	  note         = {arXiv:2305.20050},
52	}
53	
54	@inproceedings{skalse-reward-hacking,
55	  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},
56	  title        = {{Defining and Characterizing Reward Hacking}},
57	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
58	  year         = {2022},
59	  note         = {arXiv:2209.13085},
60	}
61	
62	% ============================================================
63	% Category 3: Mutation testing in software engineering
64	% ============================================================
65	
66	@article{demillo1978,
67	  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},
68	  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},
69	  journal      = {Computer},
70	  volume       = {11},
71	  number       = {4},
72	  pages        = {34--41},
73	  year         = {1978},
74	}
75	
76	@article{jia-harman-survey,
77	  author       = {Yue Jia and Mark Harman},
78	  title        = {{An Analysis and Survey of the Development of Mutation Testing}},
79	  journal      = {IEEE Transactions on Software Engineering},
80	  volume       = {37},
81	  number       = {5},
82	  pages        = {649--678},
83	  year         = {2011},
84	}
85	
86	@article{spurious-rewards,
87	  author       = {Rulin Shao and Shuyue Stella Li and Rui Xin and Scott Geng and Yiping Wang and Sewoong Oh and Simon Shaolei Du and Nathan Lambert and Sewon Min and Ranjay Krishna and Yulia Tsvetkov and Hannaneh Hajishirzi and Pang Wei Koh and Luke Zettlemoyer},
88	  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},
89	  journal      = {arXiv preprint arXiv:2506.10947},
90	  year         = {2025},
91	  eprint       = {2506.10947},
92	  archivePrefix = {arXiv},
93	  primaryClass = {cs.AI},
94	}
95	
96	@article{bondarenko-spec-gaming,
97	  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},
98	  title        = {{Demonstrating Specification Gaming in Reasoning Models}},
99	  journal      = {arXiv preprint arXiv:2502.13295},
100	  year         = {2025},
101	  eprint       = {2502.13295},
102	  archivePrefix = {arXiv},
103	  primaryClass = {cs.AI},
104	}
105	
106	@inproceedings{kim-game-formalization,
107	  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},
108	  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},
109	  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},
110	  year         = {2026},
111	  note         = {arXiv:2604.19459},
112	}
113	
114	@inproceedings{gao-reward-overoptimization,
115	  author       = {Leo Gao and John Schulman and Jacob Hilton},
116	  title        = {{Scaling Laws for Reward Model Overoptimization}},
117	  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},
118	  year         = {2023},
119	  note         = {arXiv:2210.10760},
120	}
121	
122	@inproceedings{karwowski-goodhart-rl,
123	  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},
124	  title        = {{Goodhart's Law in Reinforcement Learning}},
125	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
126	  year         = {2024},
127	  note         = {arXiv:2310.09144},
128	}
129	
130	% ============================================================
131	% Category 6: FOL/Prolog formalization with LLMs
132	% ============================================================
133	
134	@inproceedings{folio,
135	  author       = {Simeng Han and Hailey Schoelkopf and Yilun Zhao and Zhenting Qi and Martin Riddell and Luke Benson and Lucy Sun and Ekaterina Zubova and Yujie Qiao and Matthew Burtell and David Peng and Jonathan Fan and Yixin Liu and Brian Wong and Malcolm Sailor and Ansong Ni and Linyong Nan and Jungo Kasai and Tao Yu and Rui Zhang and Shafiq Joty and Alexander R. Fabbri and Wojciech Kryscinski and Xi Victoria Lin and Caiming Xiong and Dragomir Radev},
136	  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},
137	  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
138	  year         = {2024},
139	  note         = {arXiv:2209.00840},
140	}
141	
142	@inproceedings{logic-lm,
143	  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Yang Wang},
144	  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},
145	  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
146	  year         = {2023},
147	}
148	
149	@inproceedings{linc,
150	  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and Cedegao E. Zhang and Armando Solar-Lezama and Joshua B. Tenenbaum and Roger Levy},
151	  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},
152	  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
153	  year         = {2023},
154	}
155	
156	@article{fover-pei2025,
157	  author       = {Yu Pei and Yongping Du and Xingnan Jin},
158	  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},
159	  journal      = {Transactions of the Association for Computational Linguistics},
160	  volume       = {13},
161	  pages        = {1340--1359},
162	  year         = {2025},
163	}
164	
165	@article{lorp,
166	  author       = {Zhengkun Di and Chaoli Zhang and Hongtao Lv and Lizhen Cui and Lei Liu},
167	  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},
168	  journal      = {Knowledge-Based Systems},
169	  year         = {2025},
170	}
171	
172	@article{manheim-goodhart-taxonomy,
173	  author       = {David Manheim and Scott Garrabrant},
174	  title        = {{Categorizing Variants of Goodhart's Law}},
175	  journal      = {arXiv preprint arXiv:1803.04585},
176	  year         = {2019},
177	  eprint       = {1803.04585},
178	  archivePrefix = {arXiv},
179	  primaryClass = {cs.AI},
180	}
181	
182	@inproceedings{math-shepherd,
183	  author       = {Peiyi Wang and Lei Li and Zhihong Shao and Runxin Xu and others},
184	  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},
185	  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},
186	  year         = {2024},
187	  note         = {arXiv:2312.08935},
188	}
189	
190	% ============================================================
191	% Additional reward-shaping papers
192	% ============================================================
193	
194	@article{reward-hacking-survey,
195	  author       = {Xiaohua Wang and Muzhao Tian and Yuqi Zeng and Zisu Huang and others},
196	  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},
197	  journal      = {arXiv preprint arXiv:2604.13602},
198	  year         = {2026},
199	  eprint       = {2604.13602},
200	  archivePrefix = {arXiv},
201	}
202	
203	@misc{metr-reward-hacking,
204	  author       = {{METR}},
205	  title        = {{Recent Frontier Models Are Reward Hacking}},
206	  year         = {2025},
207	  howpublished = {METR blog post},
208	  note         = {\url{https://metr.org/blog/2025-06-05-recent-reward-hacking/}},
209	}
210	
211	@inproceedings{proofwriter,
212	  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},
213	  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},
214	  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},
215	  year         = {2021},
216	  note         = {arXiv:2012.13048},
217	}
218	
219	@article{qwen3,
220	  author       = {{Qwen Team}},
221	  title        = {{Qwen3 Technical Report}},
222	  journal      = {arXiv preprint arXiv:2505.09388},
223	  year         = {2025},
224	  eprint       = {2505.09388},
225	  archivePrefix = {arXiv},
226	  primaryClass = {cs.CL},
227	}
228	
229	@inproceedings{processbench,
230	  author       = {Chujie Zheng and Zhenru Zhang and Beichen Zhang and Runji Lin and Keming Lu and Bowen Yu and Dayiheng Liu and Jingren Zhou and Junyang Lin},
231	  title        = {{ProcessBench: Identifying Process Errors in Mathematical Reasoning}},
232	  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},
233	  year         = {2025},
234	  note         = {arXiv:2412.06559},
235	}
236	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfce37c6-d700-4b16-898b-fa069795daf2",
  "isSidechain": true,
  "promptId": "a961140e-8650-4dcd-abbd-2232b8f4e9ad",
  "agentId": "ad21ca604b6e8710c",
  "type": "user",
  "uuid": "77dc412c-f705-4cf0-bb29-603efdbeec27",
  "sourceToolAssistantUUID": "dfce37c6-d700-4b16-898b-fa069795daf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-15T20:16:15.933Z_

Now I have all the data. Let me compile the comprehensive report.

---

## FILE-BY-FILE ANALYSIS

---

### 1. `abstract.tex`

**Path**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex`

**Citation calls**: NONE. The abstract contains zero citation commands.

**Numbers/statistics mentioned**:
- 93% prove rate on FOLIO
- 87% of proved outputs embed conclusion verbatim
- ISR=1, ISR=0 definitions
- rho = -0.049 (ISR uncorrelated with NLI accuracy)
- ISR falls 0.642 -> 0.003 while PR rises 32% -> 96% over 100-1000 GRPO steps
- 92.2% non-hacking SFT (3-seed pooled)
- beta=0.1: 70.6% H7 vs 13.7% random (Fisher p=1.3x10^{-39})
- ISR amplifies H7 ~5x
- 1.06x after premise-count confound control
- beta=0.3: PR 66+/-42%, random 54+/-35%, individual seeds as low as 18%
- Prolog: 3/3 seeds, 0% non-hacking
- 6 reward conditions, 2 logic types, 3 seeds, 8 hacking modes

**Word count estimate**: ~230 words

**Formatting issues**: None detected. Clean abstract block.

---

### 2. `introduction.tex`

**Path**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex`

**Citation calls** (all verbatim):
1. `\citep{logic-lm, linc, satlm}` (line 9)
2. `\citep{skalse-reward-hacking, reward-hacking-survey}` (line 9)
3. `\citep{deepseekmath}` (line 10)
4. `\citep{mellgren-prolog-grpo, logic-rl}` (line 10)
5. `\citep{lightman-verify-step, math-shepherd}` (line 11)
6. `\citep{kim-game-formalization, bondarenko-spec-gaming}` (line 12)
7. `\citep{demillo1978, jia-harman-survey}` (line 17)
8. `\citep{folio}` (line 21)
9. `\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}` (line 26)

**All citations use `\citep`**. Zero `\cite` in this file.

**Numbers/statistics**:
- 93% prove rate, 87% proved outputs embed conclusion
- rho = -0.049, p=0.187
- ISR*: 0.642 -> 0.132 -> 0.003 (100-1000 steps), 99.5% degradation
- PR rises 32% -> 96%
- PR sigma = +/-47 pp across 3 seeds
- SFT: PR=13.0%, 92.2% non-hacking, 3-seed pooled, 1000 steps
- beta=0.1: 70.6% H7 vs 13.7% random, Fisher p<10^{-38}
- ~5x amplification, 1.06x after confound control
- beta=0.3: PR 66+/-42%, random 54+/-35%
- Prolog: 3/3 seeds, 0% non-hacking
- C1-C4 contributions

**Word count estimate**: ~620 words

**Formatting issues**:
- Line 18: `$\rho{=}{-}0.049$, $p{=}0.187$` — uses `{=}` for tight equals, consistent with rest of paper.
- `\autoref{fig:sta-overview}` on line 15, but later sections use `Figure~\ref{fig:...}`. **Inconsistency**: `\autoref` vs `Figure~\ref{}` usage mixed. Line 15 uses `\autoref{fig:sta-overview}`, while experiments.tex line 24 uses `Figure~\ref{fig:isr-collapse}`.

---

### 3. `related_work.tex`

**Path**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex`

**Citation calls** (all verbatim):
1. `\cite{satlm, logic-lm, linc, fover-pei2025, lorp}` (line 5)
2. `\cite{mellgren-prolog-grpo, logic-rl}` (line 5)
3. `\cite{lightman-verify-step, math-shepherd}` (line 6)
4. `\cite{processbench}` (line 6)
5. `\cite{folio}` (line 7)
6. `\cite{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl}` (line 10)
7. `\cite{gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}` (line 10)
8. `\cite{spurious-rewards}` (line 11)
9. `\cite{metr-reward-hacking}` (line 11)
10. `\cite{demillo1978, jia-harman-survey}` (line 15)

**ALL citations use `\cite`** (bare), NOT `\citep`. This is **INCONSISTENT** with introduction.tex which uses all `\citep`.

**Numbers/statistics**: None (pure prose).

**Word count estimate**: ~210 words

**Formatting issues**:
- **CRITICAL INCONSISTENCY**: related_work.tex uses `\cite{}` exclusively (10 calls), while introduction.tex uses `\citep{}` exclusively (9 calls). Under ACL style (`\usepackage[review]{acl}`), `\cite` produces inline author-year (e.g., "Pan et al. (2023)") while `\citep` produces parenthetical "(Pan et al., 2023)". In related_work.tex, every citation appears in a parenthetical/list context where `\citep` would be correct. Using `\cite` here will render as inline author names, which is grammatically wrong in sentences like "LLM-solver pipelines [Pan et al., 2023, ...]" — it would render as "LLM-solver pipelines Pan et al. (2023), ..." instead.

---

### 4. `method.tex`

**Path**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex`

**Citation calls** (all verbatim):
1. `\citep{deepseekmath}` (line 15)
2. `\citep{folio}` (line 17)
3. `\citep{proofwriter}` (line 17)
4. `\citep{demillo1978, jia-harman-survey}` (line 26, within text "LOO ablation itself is standard in mutation testing...")

**Mixed `\cite`/`\citep`**: All 4 are `\citep`. Consistent with introduction.tex.

**Numbers/statistics**:
- K=8 rollouts
- ISR=1 full necessity, ISR=0 complete redundancy
- n=2 implies ISR >= 0.5
- O(1) binary variant: ISR*=0.007 (near-zero)
- O(1) variant PR=63% vs 93% exec-only vs ISR*=0.42 under ISR beta=0.1
- beta in {0.1, 0.3}
- Seeds {42, 43, 44}
- alpha + beta = 1 convex formulation (discarded)
- 50 manual samples verified, precision >95%, Wilson 95% CI [93%, 100%] — wait, this is in the appendix, not method. Let me recheck: no, the 50-sample precision is in appendix.tex line 159.

**Word count estimate**: ~740 words

**Formatting issues**:
- Line 62 has dual labels: `\label{sec:rewards}` and `\label{sec:taxonomy-method}`. This is valid LaTeX (both labels point to the same location), but could be confusing.
- `\autoref{fig:sta-overview}` used on lines 14, 22 — consistent with introduction.tex's use of `\autoref` for this figure. But experiments.tex uses `Figure~\ref{}` for other figures. The paper mixes `\autoref` (for fig:sta-overview only) with `Figure~\ref{}` (for all other figures).

---

### 5. `experiments.tex`

**Path**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex`

**Citation calls** (all verbatim):
1. `\citep{qwen3}` (line 9)
2. `\citep{deepseekmath}` (line 9)
3. `\citep{folio}` (line 9)
4. `\citep{manheim-goodhart-taxonomy}` (line 43)
5. `\citep{gao-reward-overoptimization}` (line 91)

All 5 use `\citep`. Consistent with intro and method.

**Numbers/statistics** (dense; key ones):
- Qwen3-4B, K=8, lr 10^-6, 500 steps default, 1000 where noted, seeds {42,43,44}, 500-example FOLIO, 100 held-out
- PR rises 32%->93%->96%, ISR* falls 0.642->0.132->0.003 (214x collapse)
- 87.1% H1 at 500 steps, 100% at 1000 steps
- Component count 6.58->18.55
- Cross-seed: s42 PR=93% H1=87%; s43 PR=13% repetition 87%; s44 PR=98% H7=100% mean n=2.04
- PR variance sigma +/-47 pp
- 1000 steps: 3 seeds converge to high PR (0.95+/-0.05) but 0% non-hacking
- SFT: PR=13.0%, H7=0, H1=7.7%, 92.2% non-hacking (n=39, per-seed 91-93%)
- 100-step: 31.2% hacking vs SFT 7.7%
- H7 under ISR: 70.6% (163/231) vs random 13.7% (36/262), Fisher p=1.3x10^{-39}, OR=15.05
- Random H7: 38.3% s43, 0% s42/s44
- ISR s42 raw ISR*=0.415, 3.2x random (0.131); premise-count matched: 0.258 vs 0.243 = 1.06x
- Mean n=5.58 ISR vs 8.46 random
- Non-hacking: ISR 6.06% (14/231) vs random 9.5% (25/262), Fisher p=0.182 (n.s.), Wilson 95% CI: ISR [3.6%,9.9%], Random [6.5%,13.7%]
- 1000-step temporal collapse: genuine 17.3% -> 2.2%, H7 16.0% -> 96.7%, n_comp 5.58->2.89, ISR*=0.88
- beta=0.3: ISR PR=66+/-42% spanning 18-95%; s42 PR=18%, s43 PR=86% H1=69% 27% N-H, s44 PR=95% H7=100% ISR*=0.742 0% N-H
- Random b=0.3: PR=54+/-35% spanning 23-92%, H1=91% pooled, <=3% N-H per seed, H7 7% pooled 0-7 H7a per seed
- Prolog exec-only: s42 ISR*~0, PR=0.83; s43 ISR*~0, PR=0.56
- Prolog ISR: s42 ISR*=1.0, 50/100 proved; s43 38 proved n_necessary=1; s44 95/97 proved n_necessary=1
- Best non-hacking RL: random b=0.1 s42 PR=79% 22.8% N-H; ISR b=0.1 s42 PR=81% 17.3% N-H
- H7a: 64.5% (149/231); H7b: 6.06% (14/231); 10/14 ISR~0.8
- H1+H7 GRPO-universal at 68-100%

**Word count estimate**: ~1550 words

**Formatting issues**:
- Table 1 uses `\resizebox{\columnwidth}{!}` — fine.
- Table 2 uses `\resizebox{\columnwidth}{!}` — fine.
- Line 31: `$\sigma{\pm}47$\,pp` — this notation `sigma +/- 47 pp` is unusual. Normally sigma = 47 pp, not sigma +/- 47 pp. The +/- sign before a standard deviation value is non-standard.
- Line 32: `$0.95{\pm}0.05$` — standard and correct.
- Line 102: `$n{=}21$` for Prolog s44 — flagged as small-sample artifact in figure caption, good.

---

### 6. `conclusion.tex`

**Path**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex`

**Citation calls**: NONE. Zero citation commands in conclusion.tex.

**Numbers/statistics**:
- 99.5% collapse
- 92.2% non-hacking SFT (3-seed pooled)
- beta=0.1: 70.6% vs 13.7% random, Fisher p<10^{-38}, random H7 38.3% one seed 0% two others
- 1.06x after confound
- beta=0.3: PR=66+/-42%, random 54+/-35%
- Prolog 3/3 seeds, 0% non-hacking
- H7b: 10/12 ISR~0.8
- 95/97 Prolog samples tautological
- H7 dose-response: random b=0.1 13.7% (36/262), random b=0.3 4-7 H7a per seed, ISR b=0.1 70.6% (163/231)
- Random b=0.1 seeds: s42 22.8% N-H, s43 38.3% H7, s44 H8-dominant
- ISR b=0.1: s42 H1-heavy, s43/s44 >=97% H7

**Word count estimate**: ~560 words

**Formatting issues**:
- Section titled "Discussion and Conclusion" — no `\label`. This means it cannot be cross-referenced by label.
- Line 10: "10/12" hardcoded, but earlier text says "10/14" (in experiments.tex line 159: "10/14 achieving ISR~0.8"). **NUMBER INCONSISTENCY**: Conclusion says "10/12 samples at ISR~0.8" but experiments.tex line 159 says "10/14 achieving ISR~0.8". The appendix (line 183) says "10/12 achieve ISR~0.8". The discrepancy is because H7b total is 14 in experiments.tex (which pools s43+s44: "H7b: 6.06%, 14/231") but the detailed analysis in appendix says the false-negative correction is for s44 which has 12 samples ("12 samples with n_prem=1"). The conclusion's "10/12" matches the appendix s44 count. Experiments.tex's "10/14" includes the 2 from s43. This is an inconsistency worth flagging: experiments says 10/14 H7b at ISR~0.8, conclusion/appendix says 10/12. Both could be correct if the 2 s43 H7b samples did NOT have ISR~0.8, but this is not stated explicitly.
- Line 12: "100% genuine before functional LOO analysis revealed 95/97 samples tautological" — consistent with experiments.

---

### 7. `limitations.tex`

**Path**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex`

**Citation calls**:
1. `\citep{folio}` (line 10)

One citation, uses `\citep`. Consistent with intro/method/experiments.

**Numbers/statistics**:
- Qwen3-4B, FOLIO
- Spearman rho = -0.049, p=0.187
- Three seeds
- 500 training examples, 100 evaluation examples
- Seed 42 for stratified sampling

**Word count estimate**: ~120 words

**Formatting issues**: None. Clean and concise.

---

### 8. `appendix.tex`

**Path**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex`

**Citation calls**:
1. `\cite{gao-reward-overoptimization}` (line 115)

**Uses `\cite`**, not `\citep`. Same inconsistency as related_work.tex. However, in this case (line 115: "the trajectory predicted by \cite{gao-reward-overoptimization}"), `\cite` is actually grammatically correct — it's used as a noun phrase ("predicted by Gao et al. (2023)"). So this usage is **correct**.

**Numbers/statistics** (extensive — key ones):
- Hyperparams table: Qwen3-4B, BF16, K=8, 500/1000 steps, lr=1e-6, batch 4, grad accum 2, eff batch 8, max 512 tokens, seeds 42/43/44, FOLIO 500 train/100 eval, Prover9, SWI-Prolog 8.4.2, Greedy T=0
- Evaluation exception: s43 used sampling T=0.7 (not greedy)
- Spearman rho(ISR, NLI) = -0.049, p=0.187
- Premise-count confound: ISR=1.0 with 2 premises vs ISR=0.8 with 10 premises
- 1.06x premise-count-matched
- Fisher tests table: ISR 6.06% [3.6,9.9] vs Random 9.5% [6.5,13.7], OR=0.61, p=0.182 (n.s.); ISR vs Exec 0.79 p=0.62; Random vs Exec 1.30 p=0.68; H7: ISR 70.6% [64.3,76.3] vs Random 13.7% [9.9,18.6] OR=15.05 p=1.3e-39; SFT vs Exec: 92.3% [79.7,97.3] vs 7.5% OR=147 p<0.001
- ISR n=231, Random n=262, Exec n=93 (s42), SFT n=39
- beta=0.3 PR collapse 18% vs 48% random
- Classifier: 50 samples manually verified, precision >95%, Wilson CI [93%,100%]
- H8: ISR b=0.1 s42 only; s43/s44 checkpoints deleted
- H7b: 12 samples in ISR s44, 11/12 quantifier wrapping, 1/12 structural, 10/12 ISR~0.8
- After correction: ISR genuine 14/231=6.06%, random 25/262=9.5%, Fisher p=0.182
- Full per-seed table (Table 3): Base PR=0.12 ISR=0.064; GT FOL PR=0.18 ISR=0.559; SFT s42 PR=0.13 ISR=0.568, s43 PR=0.11 ISR=0.635, s44 PR=0.15 ISR=0.589; pooled PR=0.130 ISR=0.595 92.3% N-H n=39
- Exec-only: s42@100 PR=0.32 ISR=0.642; s42@500 PR=0.93 ISR=0.132 H8=6.5%; s42@1000 PR=0.96 ISR=0.003 100% H1; s43@500 PR=0.13; s43@1000 PR=0.90 ISR=0.465(corrected) H7=100%; s44@500 PR=0.98 ISR=0.582 H7=100%; s44@1000 PR=1.00 ISR=0.002 H1=85% H8=15%
- ISR b=0.1: s42 PR=0.81 ISR=0.415 H7=16% H1=51.9% N-H=17.3%; s43 PR=0.61 ISR=0.830 H7=100%; s44 PR=0.89 ISR=0.902 H7=100%
- ISR b=0.3 s42 PR=0.18 ISR=0.143
- Random b=0.1: s42 PR=0.79 ISR=0.131 H1=73.4% N-H=22.8%; s43 PR=0.94 ISR=0.150 H7=38.3% H1=59.6% N-H=1.1%; s44 PR=0.89 ISR=0.070 H1=82.0% N-H=6.7%
- Random b=0.3 s42: PR=0.48 ISR=0.094 H7=8% H1=92%
- Prolog: exec s42 PR=0.83 ISR=0.037; s43 PR=0.56 ISR=0.015; s44 PR=0.21 ISR=0.387
- Prolog ISR: s42 PR=0.50 ISR=1.000 H7=100%; s43 PR=0.38 ISR=0.185 H1=97.4%; s44 PR=0.97 ISR=0.912 query-as-fact
- ISR collapse: 0.642->0.132 (-79.4%)->0.003 (-99.5%)
- 94.8% proved samples ISR=0 at 1000 steps, mean comp 18.55
- 100-step: 32 proved, 9 H7 (28.1%), 1 H1 (3.1%), total hacking 31.2%; SFT 7.7% (1/13)
- O(1) variant: PR=63%, ISR*=0.007 vs exec-only ISR*=0.132 vs ISR b=0.1 ISR*=0.42; 30pp PR drop
- beta=0.3 detailed: ISR s42 PR=0.18 ISR=0.143 H1=77.8% N-H=22.2% (n=18); s43 PR=0.86 ISR=0.295 H7=4.7% H1=68.6% N-H=26.7%; s44 PR=0.95 ISR=0.742 H7=100% N-H=0%
- Random b=0.3: s42 PR=0.48 ISR=0.094 H7=8% H1=92%; s43 PR=0.92 ISR=0.180 H7=7.6% H1=90.2% N-H=2.2%; s44 PR=0.23 ISR=0 H1=100% N-H=0%
- H7a ISR: n=149; H7b ISR: n=12 (s44 only) + 2 (s43) = 14 total per experiments.tex

**Word count estimate**: ~2800 words

**Formatting issues**:
- Table 3 (tab:fol-detailed) has dual labels on line 392: `\label{tab:fol-detailed}` and `\label{tab:fol-beta01-detailed}`. Valid LaTeX but the second label overrides the first since they're on the same object. Actually both labels will point to the same table, which is fine.
- Line 115: `\cite{gao-reward-overoptimization}` — correct use of `\cite` (inline author reference).
- Lines 140-141 in hacking taxonomy appendix table: "H1" row shows "81" for Random column, but the main text Table 2 (experiments.tex) shows "71" for Random H1. **NUMBER INCONSISTENCY**: Appendix Table (tab:hacking-taxonomy-app) has Random H1 = 81%, main text Table (tab:hacking-taxonomy) has Random H1 = 71%. The appendix note says "ISR/Rand columns: beta=0.1 3-seed pooled" for both tables, so they should match. 81 vs 71 is a discrepancy.

---

### 9. `main.tex`

**Path**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex`

**Citation calls**: None (just document structure).

**Formatting notes**:
- Uses `\usepackage[review]{acl}` — ACL review mode (anonymous, line numbers).
- Title: "Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in a GRPO-Trained Neurosymbolic Formalizer: A Case Study with Qwen3-4B" — very long, ~22 words.
- `\bibliography{references}` with no `\bibliographystyle` — ACL package handles this.
- Structure order: abstract, introduction, related_work, method, experiments, conclusion, then limitations after bibliography, then appendix. This follows ACL formatting where limitations go after bibliography but before appendix.

---

## CROSS-FILE SUMMARY OF ISSUES

### A. `\cite` vs `\citep` Inconsistency

| File | `\cite` count | `\citep` count |
|------|--------------|----------------|
| abstract.tex | 0 | 0 |
| introduction.tex | 0 | 9 |
| related_work.tex | **10** | 0 |
| method.tex | 0 | 4 |
| experiments.tex | 0 | 5 |
| conclusion.tex | 0 | 0 |
| limitations.tex | 0 | 1 |
| appendix.tex | **1** | 0 |

**related_work.tex uses `\cite` exclusively while every other citing file uses `\citep`**. All 10 occurrences in related_work.tex are in list/parenthetical contexts where `\citep` is correct. The one `\cite` in appendix.tex (line 115) is actually correct usage (inline: "predicted by \cite{...}").

### B. `\autoref` vs `Figure~\ref{}` Inconsistency

- `\autoref{fig:sta-overview}` used in introduction.tex (line 15) and method.tex (lines 14, 22)
- `Figure~\ref{fig:isr-collapse}`, `Figure~\ref{fig:prolog-comparison}`, `Figure~\ref{fig:hacking-composition}` used in experiments.tex
- Only fig:sta-overview uses `\autoref`; all other figure references use `Figure~\ref{}`.

### C. Number Inconsistencies Found

1. **H7b ISR~0.8 count**: experiments.tex says "10/14" (line 159); conclusion.tex says "10/12" (line 10); appendix.tex says "10/12" (line 183). The 14 vs 12 difference: 14 is total H7b (12 from s44 + 2 from s43), and 10/12 refers specifically to s44. Experiments.tex line 159 says "with 10/14 achieving ISR~0.8" which is incorrect if only 10 of the 12 s44 samples (plus 0 of the 2 s43 samples) hit ISR~0.8. This should be either 10/12 (s44 only) or needs clarification about s43.

2. **Appendix hacking taxonomy table H1 for Random**: Appendix Table (tab:hacking-taxonomy-app) shows Random H1 = 81%, while main text Table (tab:hacking-taxonomy) shows Random H1 = 71%. One of these is wrong.

3. **Experiments.tex line 31**: `$\sigma{\pm}47$\,pp` — notation is unusual. Standard would be `$\sigma{=}47$\,pp` since sigma IS the standard deviation, not sigma plus-or-minus something.

### D. Missing Elements

- conclusion.tex has no `\label` — cannot be cross-referenced.
- No `\bibliographystyle` command — relies on ACL package default (correct).
- The footnote in abstract references `[anonymized]` URL — appropriate for review submission.

### E. Word Count Summary

| Section | Estimated Words |
|---------|----------------|
| Abstract | ~230 |
| Introduction | ~620 |
| Related Work | ~210 |
| Method | ~740 |
| Experiments | ~1550 |
| Discussion/Conclusion | ~560 |
| Limitations | ~120 |
| Appendix | ~2800 |
| **Total (main body)** | **~4030** |
| **Total with appendix** | **~6830** |

ACL long paper limit is typically 8 pages of content; 4030 words for the main body is within normal range.

### F. References.bib Notes

- 21 bib entries total
- `metr-reward-hacking` is a `@misc` blog post — some venues may require all refs to be archival
- `kim-game-formalization` is dated 2026 with arXiv:2604.19459 — future-dated reference (the paper appears to be from a 2026 workshop)
- `reward-hacking-survey` is dated 2026 — also future-dated
- Several entries use "and others" instead of full author lists (deepseekmath, lightman-verify-step, math-shepherd, reward-hacking-survey)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77dc412c-f705-4cf0-bb29-603efdbeec27",
  "isSidechain": true,
  "agentId": "ad21ca604b6e8710c",
  "requestId": "req_011Cb4xzBsbQAd2Qzg5yQkfD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e22aff34-caee-4bed-a921-41b4587f1566",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "2f21db74-9c31-4d5e-90dd-4fe9aa6125cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JKvrtV4gVt2yarqCddqph1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3932,
      "cache_read_input_tokens": 55076,
      "output_tokens": 7873,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3932
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7873,
          "cache_read_input_tokens": 55076,
          "cache_creation_input_tokens": 3932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3932,
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
