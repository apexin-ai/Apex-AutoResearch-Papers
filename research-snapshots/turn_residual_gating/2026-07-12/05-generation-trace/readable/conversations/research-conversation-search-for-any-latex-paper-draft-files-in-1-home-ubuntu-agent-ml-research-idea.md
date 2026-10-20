# Research conversation: Search for any LaTeX paper draft files in: 1. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_ga

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a15415a71738e1c47.jsonl`
- **Structured JSON:** [`b61c35b7836a7ba0c5a4.json`](../../sessions/b6/b61c35b7836a7ba0c5a4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-19T14:45:21.561Z_

Search for any LaTeX paper draft files in:
1. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/ (local workspace, recursively)
2. Also check if there's a paper/ directory or any .tex files

I need to find if there's an actual paper draft that contains "Eq.3" or the gating equation. Look for .tex files, paper directories, or draft documents. Report paths and whether any contain equation definitions for the gating mechanism.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a15e1f25-f380-4a76-9d77-88873bcc9e37",
  "agentId": "a15415a71738e1c47",
  "type": "user",
  "uuid": "8aca5eb4-d300-44cd-8215-f1a2ab482873",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-19T14:45:22.729Z_

I'll search for LaTeX paper draft files in the workspace and check for equation definitions related to the gating mechanism.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8aca5eb4-d300-44cd-8215-f1a2ab482873",
  "isSidechain": true,
  "agentId": "a15415a71738e1c47",
  "requestId": "req_011CbC7CLUKK7EaYo8gnasPZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9f185494-ac2a-46f3-bee6-375f4331ea72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PUJfgQESuiSaMqVD427GND",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 543,
      "cache_read_input_tokens": 20533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 543,
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

_source line 3 · 2026-05-19T14:45:23.161Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019Bjjo3MJktnLS89v9QGjcr`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f185494-ac2a-46f3-bee6-375f4331ea72",
  "isSidechain": true,
  "agentId": "a15415a71738e1c47",
  "requestId": "req_011CbC7CLUKK7EaYo8gnasPZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "45e9769c-6484-48d6-bac2-216f31c9522b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PUJfgQESuiSaMqVD427GND",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 543,
      "cache_read_input_tokens": 20533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 543,
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

_source line 4 · 2026-05-19T14:45:23.178Z_

<details><summary>↩ Tool result · `toolu_019Bjjo3MJktnLS89v9QGjcr`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45e9769c-6484-48d6-bac2-216f31c9522b",
  "isSidechain": true,
  "promptId": "a15e1f25-f380-4a76-9d77-88873bcc9e37",
  "agentId": "a15415a71738e1c47",
  "type": "user",
  "uuid": "eae93abb-ca19-4a7c-a25a-f214ad496075",
  "sourceToolAssistantUUID": "45e9769c-6484-48d6-bac2-216f31c9522b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T14:45:23.378Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01GETVwZpz33mT22k9TKF985`</summary>

```json
{
  "pattern": "**/paper/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eae93abb-ca19-4a7c-a25a-f214ad496075",
  "isSidechain": true,
  "agentId": "a15415a71738e1c47",
  "requestId": "req_011CbC7CLUKK7EaYo8gnasPZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "41fc18cc-1798-44c9-a8fa-0da9af5c025a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PUJfgQESuiSaMqVD427GND",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 543,
      "cache_read_input_tokens": 20533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 543,
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

_source line 6 · 2026-05-19T14:45:23.397Z_

<details><summary>↩ Tool result · `toolu_01GETVwZpz33mT22k9TKF985`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/paper/method_section_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41fc18cc-1798-44c9-a8fa-0da9af5c025a",
  "isSidechain": true,
  "promptId": "a15e1f25-f380-4a76-9d77-88873bcc9e37",
  "agentId": "a15415a71738e1c47",
  "type": "user",
  "uuid": "405f2ed4-cf37-4610-a6cd-cf0792e9a2cd",
  "sourceToolAssistantUUID": "41fc18cc-1798-44c9-a8fa-0da9af5c025a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T14:45:23.794Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01KMhBCi95tTwNjn6Ebf3aCE`</summary>

```json
{
  "pattern": "**/*draft*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "405f2ed4-cf37-4610-a6cd-cf0792e9a2cd",
  "isSidechain": true,
  "agentId": "a15415a71738e1c47",
  "requestId": "req_011CbC7CLUKK7EaYo8gnasPZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4a0fa0ba-2a8b-4175-bf80-0d49bc9a9143",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PUJfgQESuiSaMqVD427GND",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 543,
      "cache_read_input_tokens": 20533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 543,
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

_source line 8 · 2026-05-19T14:45:23.808Z_

<details><summary>↩ Tool result · `toolu_01KMhBCi95tTwNjn6Ebf3aCE`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/workers/worker_paper_method_section_draft_20260518T201248.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/workers/worker_paper_method_section_draft_20260518T201248_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/paper/method_section_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a0fa0ba-2a8b-4175-bf80-0d49bc9a9143",
  "isSidechain": true,
  "promptId": "a15e1f25-f380-4a76-9d77-88873bcc9e37",
  "agentId": "a15415a71738e1c47",
  "type": "user",
  "uuid": "d650b31f-c72c-4737-9a7f-48ed43e640f5",
  "sourceToolAssistantUUID": "4a0fa0ba-2a8b-4175-bf80-0d49bc9a9143",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T14:45:23.997Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013G9rqr285P3LkBz7rAaPXC`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating -type f \\( -name \"*.pdf\" -o -name \"*.tex\" -o -name \"*.md\" \\) 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d650b31f-c72c-4737-9a7f-48ed43e640f5",
  "isSidechain": true,
  "agentId": "a15415a71738e1c47",
  "requestId": "req_011CbC7CLUKK7EaYo8gnasPZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4a930ad1-b1ea-4d6b-aafd-94589e51ccf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PUJfgQESuiSaMqVD427GND",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 543,
      "cache_read_input_tokens": 20533,
      "output_tokens": 393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 543
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 393,
          "cache_read_input_tokens": 20533,
          "cache_creation_input_tokens": 543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 543,
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

_source line 10 · 2026-05-19T14:45:24.170Z_

<details><summary>↩ Tool result · `toolu_013G9rqr285P3LkBz7rAaPXC`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/IDEA_BRIEF.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/task_context/director.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/task_context/reviewer.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/memory.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/agent_6fa6dcc1/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/agent_6fa6dcc1/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/agent_a30dcb00/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/agent_a30dcb00/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/agent_ef0e3231/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/agent_ef0e3231/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/agent_9ef19f60/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/agent_9ef19f60/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/intermediate/diagnose_gar_loss_results.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a930ad1-b1ea-4d6b-aafd-94589e51ccf9",
  "isSidechain": true,
  "promptId": "a15e1f25-f380-4a76-9d77-88873bcc9e37",
  "agentId": "a15415a71738e1c47",
  "type": "user",
  "uuid": "361339cf-7b00-4055-bcf7-6827f8b3ee7a",
  "sourceToolAssistantUUID": "4a930ad1-b1ea-4d6b-aafd-94589e51ccf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-19T14:45:27.157Z_

Great! I found LaTeX files. Now let me search for "Eq.3" and the gating equation in these files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "361339cf-7b00-4055-bcf7-6827f8b3ee7a",
  "isSidechain": true,
  "agentId": "a15415a71738e1c47",
  "requestId": "req_011CbC7CXdnDYLaGUnkQyoWL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fb7654cc-6e18-4d0c-b15e-a40d7382b35d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Np2WFENEUMVy5SczVVXV86",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2542,
      "cache_read_input_tokens": 21076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2542,
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

_source line 12 · 2026-05-19T14:45:27.767Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Fc7qRTPoqiNBJyeg4KGDfC`</summary>

```json
{
  "pattern": "Eq\\.?3|equation.*gat|gating.*equation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb7654cc-6e18-4d0c-b15e-a40d7382b35d",
  "isSidechain": true,
  "agentId": "a15415a71738e1c47",
  "requestId": "req_011CbC7CXdnDYLaGUnkQyoWL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0885ced8-4af1-42bb-b6c1-38a160324978",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Np2WFENEUMVy5SczVVXV86",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2542,
      "cache_read_input_tokens": 21076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2542,
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

_source line 13 · 2026-05-19T14:45:27.800Z_

<details><summary>↩ Tool result · `toolu_01Fc7qRTPoqiNBJyeg4KGDfC`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/logs/paper_agent_worst.log:12:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/logs/paper_agent_worst.log:13:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/logs/phase2_median_attempt0.log:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/logs/review_best.log:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/logs/review_best.log:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/logs/review_best.log:16:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/logs/review_best.log:56:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/logs/review_best.log:66:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/logs/review_best.log:128:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/logs/review_best.log:151:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/logs/paper_agent_median.log:19:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/logs/paper_agent_median.log:20:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/logs/paper_agent_median.log:31:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/logs/paper_agent_median.log:33:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/logs/phase2_best_attempt0.log:54:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/logs/paper_agent_best.log:16:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/logs/paper_agent_best.log:17:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0885ced8-4af1-42bb-b6c1-38a160324978",
  "isSidechain": true,
  "promptId": "a15e1f25-f380-4a76-9d77-88873bcc9e37",
  "agentId": "a15415a71738e1c47",
  "type": "user",
  "uuid": "1ef430a8-60e9-4b17-97e9-0bb0bf987ba9",
  "sourceToolAssistantUUID": "0885ced8-4af1-42bb-b6c1-38a160324978",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T14:45:28.203Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BFj1cgJfbmdVZsX8GfErJM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/paper/method_section_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ef430a8-60e9-4b17-97e9-0bb0bf987ba9",
  "isSidechain": true,
  "agentId": "a15415a71738e1c47",
  "requestId": "req_011CbC7CXdnDYLaGUnkQyoWL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "30776da3-6958-415c-82bc-4a797941afa1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Np2WFENEUMVy5SczVVXV86",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2542,
      "cache_read_input_tokens": 21076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2542,
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

_source line 15 · 2026-05-19T14:45:28.210Z_

<details><summary>↩ Tool result · `toolu_01BFj1cgJfbmdVZsX8GfErJM`</summary>

```text
1	# 3. Method
2	
3	## 3.1 Problem Setup
4	
5	Consider a multi-turn dialogue sequence $\mathbf{x} = [s, u_1, a_1, u_2, a_2, \ldots, u_T, a_T]$, where $s$ denotes the system prompt, and $u_t$, $a_t$ represent the user and assistant turns at round $t$. We define the **goal token set** $\mathcal{G}$ as the token positions corresponding to the system prompt $s$ and the first user query $u_1$, which together specify the task objective for the conversation.
6	
7	For a query position $q$ and goal set $\mathcal{G}$, the Goal Attention Ratio (GAR) measures how much attention the model allocates to goal-specifying tokens:
8	
9	$$\text{GAR}(q, \mathcal{G}) = \frac{1}{LH} \sum_{l=1}^{L} \sum_{h=1}^{H} \sum_{g \in \mathcal{G}} \alpha_l^h(q, g)$$
10	
11	where $\alpha_l^h(q, g)$ is the softmax attention weight from position $q$ to position $g$ at layer $l$, head $h$, and $L$, $H$ are the total number of layers and attention heads. In practice, we evaluate GAR at the last token of each assistant turn $a_t$, as this position aggregates the model's contextual state for the next prediction.
12	
13	Dongre et al. (2026) established that GAR decays by 27-48% over 50 turns across 12 LLM families. Their residual stream probes further reveal that goal information persists in hidden representations (probe AUC $\geq 0.98$) even after attention to goal tokens has collapsed. The model retains goal knowledge in its residual stream but progressively fails to access it through the attention mechanism. This dissociation between information retention and attention loss motivates an intervention at the residual pathway rather than at the attention computation itself.
14	
15	
16	## 3.2 ThreadGate Architecture
17	
18	ThreadGate inserts a lightweight gating module at each transformer layer's residual connection. For layer $l$, let $f_l(\cdot)$ denote the combined self-attention and feed-forward transformation. The standard residual update $\mathbf{x}_l = \mathbf{x}_{l-1} + f_l(\mathbf{x}_{l-1})$ is replaced by:
19	
20	$$\mathbf{x}_l = \mathbf{x}_{l-1} + g_l \cdot f_l(\mathbf{x}_{l-1}), \quad g_l \in (0, 1)$$
21	
22	where $g_l$ is a scalar gate value produced by a learned gate network $\phi_l$. Each layer has its own gate network, and $g_l$ varies across token positions: $g_l^{(i)}$ denotes the gate value for position $i$ at layer $l$. When $g_l \approx 1$, the layer operates normally; when $g_l < 1$, its residual contribution is attenuated.
23	
24	**Gate Network.** Each gate network $\phi_l$ accepts two inputs: (1) the hidden state $\mathbf{x}_{l-1} \in \mathbb{R}^d$ at the current position, and (2) a turn feature embedding. A down-projection $W_{\text{down}} \in \mathbb{R}^{d \times r}$ first reduces the hidden state to dimension $r$. The turn features are embedded into a vector $\mathbf{e} \in \mathbb{R}^{d_t}$ through a TurnEmbedding module (described below). The gate value is then:
25	
26	$$g_l = \sigma\!\Big(W_2 \, \text{ReLU}\!\big(W_1 [\mathbf{x}_{l-1} W_{\text{down}};\; \mathbf{e}]\big) + b\Big)$$
27	
28	where $W_1 \in \mathbb{R}^{(r + d_t) \times d_h}$, $W_2 \in \mathbb{R}^{d_h \times 1}$, $\sigma$ is the sigmoid function, and $[\cdot\,;\,\cdot]$ denotes concatenation. We set $r = 16$, $d_h = 64$, and $d_t = 16$. The output bias $b$ is initialized to 1.5, so $\sigma(b) \approx 0.82$ at initialization. This warm start ensures the gated model behaves nearly identically to the original LLM at the onset of training.
29	
30	**TurnEmbedding.** This module encodes the structural position of each token within the multi-turn dialogue. For each token position $i$, we compute two discrete features: (1) *turn distance* $d_i$, the number of tokens since the nearest turn boundary marker (\texttt{<|im\_start|>} or \texttt{<|im\_end|>}), and (2) *turn index* $t_i$, the ordinal index of the dialogue turn that contains position $i$. Both features are capped at 32 and mapped through learned embedding tables:
31	
32	$$\mathbf{e}_i = [\text{Embed}_{\text{dist}}(d_i);\; \text{Embed}_{\text{turn}}(t_i)]$$
33	
34	where $\text{Embed}_{\text{dist}}, \text{Embed}_{\text{turn}} \in \mathbb{R}^{33 \times 8}$. The resulting 16-dimensional vector allows the gate to condition on dialogue structure (how far the current token is from a turn boundary, which turn it belongs to) without encoding turn content.
35	
36	**Integration with Frozen LLM.** The base LLM (Qwen2.5-7B-Instruct) remains frozen throughout training. LoRA adapters (rank 16, $\alpha = 32$) are attached to the query and value projections to preserve language modeling capacity, while the gate networks and TurnEmbedding are trained jointly. The gating mechanism is implemented via forward hooks registered on each transformer layer: after a layer computes its output, the hook extracts the residual update $f_l(\mathbf{x}_{l-1}) = \mathbf{x}_l - \mathbf{x}_{l-1}$ and scales it by $g_l$ before the result passes to the next layer. A single TurnEmbedding module is shared across all layers.
37	
38	**Parameter Overhead.** Each gate network contains approximately 60K parameters, dominated by the $d \times r$ down-projection. Across all 28 layers, the total gate parameter count is ~1.67M, or roughly 0.02% of the 7.6B base model. The shared TurnEmbedding adds 528 parameters. This minimal footprint makes ThreadGate a practical plug-in for pretrained LLMs.
39	
40	
41	## 3.3 Training Objective
42	
43	The total training loss combines three terms:
44	
45	$$\mathcal{L} = \mathcal{L}_{\text{NTP}} + \lambda_{\text{gar}} \cdot \mathcal{L}_{\text{GAR}} + \lambda_{\text{div}} \cdot \mathcal{L}_{\text{div}}$$
46	
47	with $\lambda_{\text{gar}} = 1.0$ and $\lambda_{\text{div}} = 1.0$.
48	
49	**Next-Token Prediction Loss.** $\mathcal{L}_{\text{NTP}}$ is the standard cross-entropy loss computed only over assistant tokens. Tokens in the system prompt and user turns are masked (label set to $-100$), so the model is trained exclusively to produce assistant responses. This preserves the natural training signal of multi-turn dialogue.
50	
51	**GAR Regularization Loss.** We use a bidirectional mean squared error (MSE) loss that pulls the mean GAR toward a target value $\tau$:
52	
53	$$\mathcal{L}_{\text{GAR}} = \left(\overline{\text{GAR}} - \tau\right)^2$$
54	
55	where $\overline{\text{GAR}} = \frac{1}{T} \sum_{t=1}^{T} \text{GAR}(q_t, \mathcal{G})$ is the mean GAR across assistant turns (with $q_t$ the last token of turn $a_t$), and $\tau = 0.5$.
56	
57	The choice of MSE over a monotonic reward (e.g., $\mathcal{L} = -\overline{\text{GAR}}$) is deliberate. A monotonic signal pushes gates toward identity ($g_l \to 1$ everywhere), which maximizes GAR trivially by removing all gating. The bidirectional MSE penalty resists this collapse: when $\overline{\text{GAR}} > \tau$, the gradient reverses and penalizes further GAR increase. This keeps the gates in a functionally meaningful regime where they can selectively modulate layers rather than uniformly pass through all residual updates.
58	
59	**Differentiable GAR Computation.** To backpropagate through $\mathcal{L}_{\text{GAR}}$, we register forward hooks on the self-attention modules to capture attention weight tensors before detachment. The model runs with eager attention (not FlashAttention) during training so that per-head attention matrices remain in the computation graph. The GAR value is then computed by indexing into these attention matrices at the goal and query positions, and the gradient flows from $\mathcal{L}_{\text{GAR}}$ through the attention weights to the gate parameters.
60	
61	**Gate Diversity Loss.** Without explicit regularization, gate values across layers can converge to a uniform scalar, which collapses the per-layer structure that ThreadGate is designed to learn. We add a diversity term:
62	
63	$$\mathcal{L}_{\text{div}} = \text{ReLU}\!\left(\sigma_{\min} - \text{std}(\bar{g}_1, \ldots, \bar{g}_L)\right)$$
64	
65	where $\bar{g}_l = \frac{1}{N} \sum_{i=1}^{N} g_l^{(i)}$ is the mean gate value at layer $l$ across all $N$ token positions in the sequence, and $\sigma_{\min} = 0.05$. This loss activates only when the standard deviation of layer-averaged gates falls below the threshold. When the gates already exhibit sufficient variation across layers, $\mathcal{L}_{\text{div}} = 0$ and imposes no gradient. The ReLU formulation provides a soft floor on diversity without over-constraining the learned gate profile.
66	
67	
68	## 3.4 Uniform Gate Baseline
69	
70	To isolate the contribution of turn-aware conditioning, we introduce a Uniform Gate ablation baseline. This variant shares the same architecture and training objective as ThreadGate, with one modification: the TurnEmbedding output is replaced by a single learned constant vector $\mathbf{c} \in \mathbb{R}^{d_t}$, broadcast identically to all token positions. The Uniform Gate can still learn layer-specific gating patterns through the hidden-state-dependent pathway of its gate network, but it cannot condition gate values on turn structure. Any performance gap between ThreadGate and the Uniform Gate therefore isolates the value of turn boundary information in the gating decision.
71	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30776da3-6958-415c-82bc-4a797941afa1",
  "isSidechain": true,
  "promptId": "a15e1f25-f380-4a76-9d77-88873bcc9e37",
  "agentId": "a15415a71738e1c47",
  "type": "user",
  "uuid": "a959ad78-76ad-4582-85f7-4dda31b6f395",
  "sourceToolAssistantUUID": "30776da3-6958-415c-82bc-4a797941afa1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T14:45:28.885Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PwU7jyZQHQPJXboMX2HT3b`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a959ad78-76ad-4582-85f7-4dda31b6f395",
  "isSidechain": true,
  "agentId": "a15415a71738e1c47",
  "requestId": "req_011CbC7CXdnDYLaGUnkQyoWL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3e1de52b-a293-4811-899d-884dd591e132",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Np2WFENEUMVy5SczVVXV86",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2542,
      "cache_read_input_tokens": 21076,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2542
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 326,
          "cache_read_input_tokens": 21076,
          "cache_creation_input_tokens": 2542,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2542,
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

_source line 17 · 2026-05-19T14:45:29.218Z_

<details><summary>↩ Tool result · `toolu_01PwU7jyZQHQPJXboMX2HT3b`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{booktabs}
4	\usepackage{amsmath}
5	\usepackage{amssymb}
6	\usepackage{hyperref}
7	\usepackage{xcolor}
8	\usepackage{multirow}
9	\usepackage{array}
10	\usepackage{float}
11	
12	\hypersetup{colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue}
13	
14	\newcommand{\gar}{\textsc{GAR}}
15	\newcommand{\tg}{\textsc{ThreadGate}}
16	\newcommand{\ug}{\textsc{UniformGate}}
17	
18	\title{Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation:\\A Mechanistic Analysis}
19	\author{Anonymous}
20	\date{}
21	
22	\begin{document}
23	\maketitle
24	
25	% ============================================================
26	\begin{abstract}
27	% ============================================================
28	Multi-turn dialogue performance in large language models degrades as conversations grow longer.
29	Recent work by Dongre et al.\ quantified this through the Goal Attention Ratio (\gar{}), showing that attention to goal-relevant tokens drops by 27--48\% over extended conversations, while residual stream probes reveal that goal information persists (AUC up to 0.98).
30	This creates a natural hypothesis: a learnable gate on the residual connection should recover goal attention.
31	We implement this hypothesis as \tg{}, a per-layer gating module trained with joint next-token prediction (NTP) and \gar{} objectives.
32	\tg{} successfully optimizes \gar{} during training ($0.02 \to 0.48$), but this improvement completely fails to transfer to inference (\gar{}$= 0.016$, a $30\times$ gap).
33	We identify three coupled failure mechanisms: (1)~NTP gradients dominate gate parameters (magnitude ratio $7.8$--$14.2\times$), causing gates to learn \emph{reversed} turn conditioning; (2)~the resulting $30\times$ training--inference \gar{} gap reflects a structural distribution shift from teacher-forcing to autoregressive generation; (3)~at inference time, gates attenuate residual updates by only 2--7\%, far too weak to redirect attention.
34	Four-way ablation (\tg{} vs.\ Uniform Gate vs.\ LoRA-only vs.\ Base) on two architecture families (Qwen-2.5-7B, Llama-3.1-8B) confirms that gating provides zero incremental contribution.
35	A downstream instruction-retention task correlates strongly with \gar{} ($r = 0.89$), validating \gar{} as a behavioral proxy.
36	Our results demonstrate that auxiliary attention losses optimized under teacher-forcing face a fundamental generalization barrier, with implications for all attention steering methods.
37	\end{abstract}
38	
39	% ============================================================
40	\section{Introduction}
41	\label{sec:intro}
42	% ============================================================
43	
44	Large language models increasingly serve as multi-turn conversational agents, yet their performance degrades as dialogues extend beyond the first few turns.
45	Users report that models ``forget'' system-prompt instructions, lose track of conversation goals, and produce increasingly generic responses in later turns.
46	This degradation has practical consequences for deployment in customer service, tutoring, and collaborative writing, where conversations routinely span tens of turns.
47	
48	Dongre et al.~\cite{dongre2026} provided the first systematic quantification of this phenomenon through the Goal Attention Ratio (\gar{}), measuring the fraction of attention that response tokens allocate to goal-relevant tokens in the system prompt.
49	Across 12 model families, they observed \gar{} drops of 27--48\% over 50 turns.
50	Crucially, their residual stream probing experiments revealed that goal information \emph{persists} in the residual stream (linear probe AUC up to 0.98) even as the attention channel closes.
51	This dissociation---information present but inaccessible via attention---suggests a natural intervention point: if goal information exists in the residual stream, a learnable gate on the residual connection should be able to modulate information flow and recover goal attention.
52	
53	We implement this hypothesis as \tg{}, a lightweight per-layer scalar gate inserted at the residual connection of each transformer layer, trained jointly with NTP and \gar{} objectives.
54	After systematic exploration of seven loss configurations across four design families (cumulative, maximize, smooth saturation, and MSE-target), we find that \tg{} with MSE + gate divergence regularization achieves strong training convergence, raising \gar{} from 0.02 to 0.48.
55	However, this training success \emph{completely fails} to transfer to autoregressive inference: inference \gar{} remains at 0.016, a $30\times$ gap.
56	
57	Our central contribution is a mechanistic analysis of \emph{why} this transfer fails.
58	We identify three coupled failure mechanisms: (1)~NTP loss dominates gate gradients by $7.8$--$14.2\times$ in magnitude, causing gates to learn reversed turn conditioning (suppressing at early turns where \gar{} is high, becoming passive at late turns where intervention is needed); (2)~teacher-forcing training creates a fundamental distribution shift: attention patterns optimized on gold contexts do not generalize to model-generated contexts; (3)~at inference time, gates attenuate residual updates by only 2--7\%, effectively acting as identity operations.
59	Four-way ablation on Qwen-2.5-7B and cross-model validation on Llama-3.1-8B confirm that the gating mechanism provides zero incremental benefit beyond LoRA fine-tuning alone.
60	
61	Our contributions are:
62	\begin{enumerate}
63	    \item \textbf{Quantitative evidence of teacher-forcing distribution shift}: the first measurement of how teacher-forcing$\to$generation distribution mismatch destroys auxiliary attention loss generalization ($30\times$ \gar{} gap), with implications for all attention steering methods trained under teacher-forcing.
64	    \item \textbf{Layer-wise quantification of NTP--\gar{} gradient conflict}: NTP gradients oppose \gar{} gradients on gate parameters across 84--93\% of layers, with $12.8$--$14.2\times$ magnitude dominance, causing reversed turn conditioning.
65	    \item \textbf{Systematic ablation and negative baseline}: seven loss configurations, four-way ablation isolating turn conditioning (\tg{} vs.\ \ug{}) and gating itself (\tg{} vs.\ LoRA-only), providing a principled negative baseline for future work.
66	    \item \textbf{Cross-model validation}: Qwen-2.5-7B and Llama-3.1-8B independently exhibit the same three-stage failure chain, ruling out architecture-specific explanations.
67	\end{enumerate}
68	
69	% ============================================================
70	\section{Related Work}
71	\label{sec:related}
72	% ============================================================
73	
74	\paragraph{Multi-turn dialogue degradation.}
75	The phenomenon that LLM performance degrades over extended conversations has been documented in multiple settings.
76	Lost-in-the-middle effects~\cite{liu2024lost} show that models struggle to attend to information in long contexts.
77	Dongre et al.~\cite{dongre2026} formalized this for multi-turn dialogue through \gar{}, demonstrating systematic attention decay across 12 model families and finding that residual stream probes retain goal information even as attention fails.
78	
79	\paragraph{Residual gating and adaptive computation.}
80	Learnable gates on residual connections have been explored in several contexts.
81	LayerDrop~\cite{fan2020layerdrop} and early exit mechanisms~\cite{schuster2022confident} use gating to control computation depth.
82	Mixture-of-depths~\cite{raposo2024mixture} applies per-token gating to skip layers selectively.
83	Our work differs in applying residual gating specifically to steer attention toward goal tokens, with the gate trained via an auxiliary \gar{} loss.
84	
85	\paragraph{Attention steering and intervention.}
86	Methods for directing attention include attention supervision~\cite{liu2016attention}, attention masking, and activation patching from mechanistic interpretability~\cite{vig2020investigating}.
87	Inference-time intervention (ITI)~\cite{li2024inference} modifies activations at specific layers during generation.
88	Our negative results suggest that training-time attention steering via auxiliary losses faces fundamental limitations that inference-time methods may circumvent.
89	
90	\paragraph{Exposure bias and teacher-forcing mismatch.}
91	The discrepancy between teacher-forced training and autoregressive inference is well studied~\cite{ranzato2016sequence,bengio2015scheduled}.
92	Scheduled sampling~\cite{bengio2015scheduled} and sequence-level training~\cite{ranzato2016sequence} address generation quality degradation.
93	Our work reveals a new consequence of this mismatch: auxiliary attention losses optimized under teacher-forcing fail to generalize, which existing exposure bias literature has not analyzed.
94	
95	% ============================================================
96	\section{Background}
97	\label{sec:background}
98	% ============================================================
99	
100	\subsection{Goal Attention Ratio}
101	
102	Following Dongre et al.~\cite{dongre2026}, we define the Goal Attention Ratio (\gar{}) as the fraction of attention weight that response tokens allocate to goal-relevant tokens.
103	For a response token $r$ at layer $l$ with head $h$, the per-position \gar{} is:
104	\begin{equation}
105	    \text{GAR}(r, l, h) = \sum_{g \in \mathcal{G}} \alpha_{r,g}^{(l,h)}
106	\end{equation}
107	where $\mathcal{G}$ is the set of goal token positions and $\alpha_{r,g}^{(l,h)}$ is the attention weight from $r$ to $g$.
108	The aggregate \gar{} averages over all response tokens, layers, and heads.
109	
110	We use two operational definitions: \textbf{GAR-Dongre}, where $\mathcal{G}$ is restricted to system prompt task tokens and response tokens include all assistant tokens (for comparability with Dongre et al.), and \textbf{GAR-ours}, where $\mathcal{G}$ includes the system prompt and first user query, with response tokens restricted to the last token of each assistant turn (used as the training signal for richer goal coverage and more stable gradients).
111	
112	\subsection{Residual Stream Persistence}
113	
114	Dongre et al.\ demonstrated that linear probes trained on residual stream activations achieve AUC up to 0.98 for classifying whether goal information is present, even at late turns where \gar{} has dropped substantially.
115	This dissociation---goal information persisting in the residual stream despite attention channel closure---motivates our intervention: if the information is there but attention cannot access it, modulating the residual connection should help the model recover access.
116	
117	% ============================================================
118	\section{Method}
119	\label{sec:method}
120	% ============================================================
121	
122	\subsection{ThreadGate Architecture}
123	
124	\tg{} inserts a learnable scalar gate $g_l \in [0, 1]$ at the residual connection of each transformer layer $l$.
125	The standard residual update
126	\begin{equation}
127	    \mathbf{x}_{l+1} = \mathbf{x}_l + f_l(\mathbf{x}_l)
128	\end{equation}
129	becomes
130	\begin{equation}
131	    \mathbf{x}_{l+1} = g_l \cdot \mathbf{x}_l + f_l(\mathbf{x}_l)
132	\end{equation}
133	where $f_l$ is the sub-layer transformation (self-attention or FFN) and $g_l = \sigma(w_l)$ with $w_l$ a learned parameter and $\sigma$ the sigmoid function.
134	When $g_l = 1$, the gate is identity (no intervention); as $g_l \to 0$, the gate suppresses the residual stream, forcing the model to rely more on the current layer's computation.
135	
136	The gate is combined with LoRA adapters~\cite{hu2022lora} on the attention projection matrices ($W_Q, W_K, W_V, W_O$) with rank 16, enabling the model to jointly learn modified attention patterns and residual modulation.
137	
138	\subsection{Training Objective}
139	
140	After exploring seven configurations across four loss design families, we arrived at the MSE + gate divergence formulation (v7):
141	\begin{equation}
142	    \mathcal{L} = \mathcal{L}_{\text{NTP}} + \lambda \cdot \mathcal{L}_{\text{GAR}} + \beta \cdot \mathcal{L}_{\text{div}}
143	\end{equation}
144	where $\mathcal{L}_{\text{NTP}}$ is the standard next-token prediction loss,
145	\begin{equation}
146	    \mathcal{L}_{\text{GAR}} = \text{MSE}\big(\text{GAR}_{\text{current}},\; \text{GAR}_{\text{target}}\big)
147	\end{equation}
148	is a bidirectional MSE loss that pushes \gar{} toward a target value (derived from the per-conversation maximum), and
149	\begin{equation}
150	    \mathcal{L}_{\text{div}} = -\text{Var}(\{g_l\}_{l=1}^{L})
151	\end{equation}
152	is a gate divergence regularizer that prevents all gates from collapsing to the same value.
153	
154	The MSE formulation was critical: earlier designs using cumulative (v1--v2), maximize (v3--v5), and smooth saturation (v6) objectives all failed to achieve stable training convergence.
155	The bidirectional MSE enables the loss to both increase \gar{} when too low and decrease it when overshooting, providing stable gradients throughout training.
156	
157	\subsection{Training Setup}
158	
159	We train on the UltraChat dataset (first 8,000 conversations), using conversations with $\geq$10 turns.
160	Training runs for 3 epochs with AdamW optimizer, learning rate $2 \times 10^{-5}$, and batch size 1 with gradient accumulation.
161	The primary model is Qwen-2.5-7B-Instruct (28 layers); cross-model validation uses Llama-3.1-8B-Instruct (32 layers).
162	
163	\subsection{Ablation Models}
164	
165	We compare four configurations to isolate the contribution of each component:
166	\begin{itemize}
167	    \item \textbf{\tg{}}: Per-layer learned gates + LoRA + NTP + \gar{} loss (full model).
168	    \item \textbf{\ug{}}: Fixed uniform gate (same value across all layers, no turn conditioning) + LoRA + NTP + \gar{} loss. Isolates whether turn-selective gating matters.
169	    \item \textbf{LoRA-only}: LoRA adapters + NTP loss only (gate fixed at 1.0). Isolates whether the gating mechanism adds value beyond LoRA fine-tuning.
170	    \item \textbf{Base}: Unmodified pretrained model. Establishes the \gar{} floor.
171	\end{itemize}
172	
173	% ============================================================
174	\section{Experiments}
175	\label{sec:experiments}
176	% ============================================================
177	
178	\subsection{Training Dynamics}
179	
180	\tg{} v7 exhibits a characteristic three-phase training trajectory: (A)~an initial plateau phase (steps 0--90) where \gar{} remains near the baseline ($\sim$0.02), (B)~a rapid phase transition (steps 90--144) where \gar{} climbs sharply, and (C)~convergence at \gar{}$\approx 0.48$ on Qwen and $\approx 0.42$ on Llama.
181	NTP loss converges to $0.896$ (Qwen) and $0.910$ (Llama), comparable to LoRA-only baselines ($0.948$ and $0.908$ respectively), indicating that the \gar{} auxiliary loss does not substantially harm language modeling.
182	
183	\subsection{Main Results: Four-Way Evaluation (Qwen-2.5-7B)}
184	\label{sec:main-results}
185	
186	Table~\ref{tab:heldout-eval} presents the four-way evaluation on 50 held-out UltraChat conversations (indices $\geq$8000, disjoint from training).
187	We report mid-turn \gar{} (averaged over turns 4--10, where degradation is most severe) under both the Dongre and our definitions, along with perplexity (PPL) and NTP loss.
188	
189	\begin{table}[H]
190	\centering
191	\caption{Held-out evaluation on 50 unseen UltraChat conversations (Qwen-2.5-7B). Mid-turn \gar{} averages over turns 4--10.}
192	\label{tab:heldout-eval}
193	\begin{tabular}{lcccc}
194	\toprule
195	\textbf{Model} & \textbf{GAR-D mid} & \textbf{GAR-O mid} & \textbf{PPL} & \textbf{NTP} \\
196	\midrule
197	Base       & 0.004 & 0.011 & 4.35 & 1.43 \\
198	\tg{}      & 0.015 & 0.013 & 2.71 & 0.96 \\
199	\ug{}      & 0.012 & 0.012 & 2.69 & 0.95 \\
200	LoRA-only  & 0.014 & 0.013 & 2.70 & 0.96 \\
201	\bottomrule
202	\end{tabular}
203	\end{table}
204	
205	The results reveal that \tg{} provides \emph{no meaningful improvement} over LoRA-only: the \gar{}-Dongre difference is $+0.001$ (within noise), and PPL is virtually identical ($2.71$ vs.\ $2.70$).
206	\ug{} performs comparably, indicating that turn-selective conditioning adds nothing.
207	All three fine-tuned models improve substantially over the base model in both PPL and NTP loss, but this improvement is entirely attributable to LoRA fine-tuning, not gating.
208	
209	The training--inference gap is stark: training \gar{} reaches 0.48, but inference \gar{} is only 0.015---a $32\times$ gap on held-out data.
210	
211	\subsection{Robustness: Held-Out vs.\ Standard Evaluation}
212	
213	Table~\ref{tab:heldout-consistency} compares the held-out evaluation (50 conversations) with the standard evaluation (5 fixed conversations) to verify that our findings are not artifacts of evaluation data selection.
214	
215	\begin{table}[H]
216	\centering
217	\caption{Consistency between standard (5 convs) and held-out (50 convs) evaluation.}
218	\label{tab:heldout-consistency}
219	\begin{tabular}{lccc}
220	\toprule
221	\textbf{Metric} & \textbf{Standard} & \textbf{Held-out} & \textbf{$\Delta$} \\
222	\midrule
223	TG Dongre mid \gar{}     & 0.016 & 0.015 & $-0.001$ \\
224	LoRA Dongre mid \gar{}    & 0.014 & 0.014 & $+0.000$ \\
225	TG $-$ LoRA gap           & $+0.002$ & $+0.001$ & $-0.001$ \\
226	Gap ratio (train/infer)   & $30\times$ & $32\times$ & $+2\times$ \\
227	Base Dongre mid \gar{}    & 0.003 & 0.004 & $+0.001$ \\
228	\bottomrule
229	\end{tabular}
230	\end{table}
231	
232	All metrics are consistent within $\pm 0.001$ \gar{} and $\pm 2\times$ gap ratio, confirming that the negative findings are robust to evaluation data.
233	The larger held-out sample narrows confidence intervals and strengthens the statistical basis for the ``gating provides zero benefit'' conclusion.
234	
235	\subsection{Cross-Model Validation: Llama-3.1-8B}
236	\label{sec:cross-model}
237	
238	To rule out architecture-specific explanations, we replicate the full experimental pipeline on Llama-3.1-8B-Instruct, which differs from Qwen-2.5-7B in attention mechanism (GQA with 32 query / 8 KV heads vs.\ MHA with 28 heads), RoPE implementation, and pre-training data.
239	
240	\paragraph{Phase 1: Baseline \gar{} degradation.}
241	Table~\ref{tab:phase1-crossmodel} compares per-turn \gar{} between the two base models.
242	
243	\begin{table}[H]
244	\centering
245	\caption{Per-turn \gar{}-Dongre comparison between base models. Both exhibit severe monotonic degradation.}
246	\label{tab:phase1-crossmodel}
247	\begin{tabular}{lcc}
248	\toprule
249	\textbf{Turn} & \textbf{Qwen-2.5-7B} & \textbf{Llama-3.1-8B} \\
250	\midrule
251	T1  & 0.042 & 0.039 \\
252	T2  & 0.024 & 0.022 \\
253	T3  & 0.022 & 0.020 \\
254	T4  & 0.013 & 0.011 \\
255	T5  & 0.013 & 0.012 \\
256	T6  & 0.009 & 0.007 \\
257	T7  & 0.008 & 0.006 \\
258	T8  & 0.008 & 0.007 \\
259	T9  & 0.016 & 0.013 \\
260	T10 & 0.006 & 0.005 \\
261	\midrule
262	Mid avg       & 0.012 & 0.010 \\
263	Relative drop & 70.8\% & 74.5\% \\
264	\bottomrule
265	\end{tabular}
266	\end{table}
267	
268	Both architectures exhibit severe \gar{} degradation ($70.8\%$ and $74.5\%$ respectively), confirming that attention decay is a general property of autoregressive transformers, not specific to Qwen.
269	
270	\paragraph{ThreadGate training on Llama-3.1-8B.}
271	Table~\ref{tab:llama-training} compares \tg{} v7 training outcomes across the two architectures.
272	
273	\begin{table}[H]
274	\centering
275	\caption{\tg{} v7 training comparison across architectures. Both achieve training convergence but fail at inference.}
276	\label{tab:llama-training}
277	\begin{tabular}{lcc}
278	\toprule
279	\textbf{Metric} & \textbf{Qwen-2.5-7B} & \textbf{Llama-3.1-8B} \\
280	\midrule
281	Num layers        & 28       & 32 \\
282	Attention type    & MHA (28h) & GQA (32q/8kv) \\
283	Training \gar{} peak & 0.48  & 0.42 \\
284	Convergence step  & gs144    & gs170 \\
285	Final gate mean   & 0.934    & 0.941 \\
286	Final NTP loss    & 0.896    & 0.910 \\
287	Inference Dongre \gar{} & 0.016 & 0.012 \\
288	Gap ratio         & $30\times$ & $35\times$ \\
289	Reversed layers   & 27/28 (96\%) & 26/32 (81\%) \\
290	\bottomrule
291	\end{tabular}
292	\end{table}
293	
294	Llama-3.1-8B replicates the full failure chain: training convergence (\gar{}~$=0.42$) $\to$ inference collapse (\gar{}~$=0.012$, $35\times$ gap) $\to$ gate reversal (81\% of layers).
295	The slightly larger gap ratio ($35\times$ vs.\ $30\times$) is consistent with GQA's reduced per-head capacity for indirect attention modulation.
296	
297	\paragraph{Gate profile reversal on Llama.}
298	Table~\ref{tab:llama-gate-reversal} shows the five most severely reversed layers, where gates are more suppressive at early turns (where \gar{} is naturally high and intervention is unnecessary) than at late turns (where intervention is needed).
299	
300	\begin{table}[H]
301	\centering
302	\caption{Llama-3.1-8B: top-5 reversed gate layers. Correct behavior would show Turn1 gate $>$ Turn21 gate.}
303	\label{tab:llama-gate-reversal}
304	\begin{tabular}{lccc}
305	\toprule
306	\textbf{Layer} & \textbf{Turn1 gate} & \textbf{Turn21 gate} & \textbf{Diff} \\
307	\midrule
308	L25 & 0.782 & 0.976 & $-0.194$ \\
309	L16 & 0.761 & 0.935 & $-0.174$ \\
310	L8  & 0.831 & 0.952 & $-0.121$ \\
311	L12 & 0.845 & 0.961 & $-0.116$ \\
312	L5  & 0.868 & 0.973 & $-0.105$ \\
313	\bottomrule
314	\end{tabular}
315	\end{table}
316	
317	All listed layers show negative differences, meaning gates become \emph{more passive} at later turns---the opposite of what is needed to counteract \gar{} degradation.
318	
319	\paragraph{LoRA-only baseline on Llama.}
320	Table~\ref{tab:lora-crossmodel} confirms that LoRA-only training proceeds normally on both architectures, establishing a clean baseline.
321	
322	\begin{table}[H]
323	\centering
324	\caption{LoRA-only training comparison. Both models converge to similar NTP loss levels.}
325	\label{tab:lora-crossmodel}
326	\begin{tabular}{lcc}
327	\toprule
328	\textbf{Metric} & \textbf{Qwen-2.5-7B} & \textbf{Llama-3.1-8B} \\
329	\midrule
330	Epochs          & 3     & 3 \\
331	Final NTP loss  & 0.948 & 0.908 \\
332	Training time   & 5.7h  & 6.2h \\
333	LoRA size       & 20MB  & 20MB \\
334	\bottomrule
335	\end{tabular}
336	\end{table}
337	
338	\paragraph{Three-way evaluation on Llama.}
339	Table~\ref{tab:llama-eval} presents the Llama-3.1-8B evaluation (Uniform Gate omitted since Qwen already demonstrated UG $\approx$ TG $\approx$ LoRA-only).
340	
341	\begin{table}[H]
342	\centering
343	\caption{Llama-3.1-8B three-way evaluation. Gating provides zero incremental benefit.}
344	\label{tab:llama-eval}
345	\begin{tabular}{lcccc}
346	\toprule
347	\textbf{Model} & \textbf{GAR-D mid} & \textbf{GAR-O mid} & \textbf{PPL} & \textbf{NTP} \\
348	\midrule
349	Base      & 0.003 & 0.009 & 4.51 & 1.46 \\
350	\tg{}     & 0.012 & 0.011 & 2.78 & 0.92 \\
351	LoRA-only & 0.013 & 0.012 & 2.76 & 0.91 \\
352	\bottomrule
353	\end{tabular}
354	\end{table}
355	
356	\paragraph{Cross-model summary.}
357	Table~\ref{tab:crossmodel-summary} consolidates the gating contribution across both architectures.
358	
359	\begin{table}[H]
360	\centering
361	\caption{Cross-model gating contribution summary. Neither architecture benefits from gating.}
362	\label{tab:crossmodel-summary}
363	\begin{tabular}{lcc}
364	\toprule
365	\textbf{Metric} & \textbf{Qwen-2.5-7B} & \textbf{Llama-3.1-8B} \\
366	\midrule
367	TG Dongre \gar{}    & 0.016 & 0.012 \\
368	LoRA Dongre \gar{}  & 0.014 & 0.013 \\
369	TG $-$ LoRA         & $+0.002$ & $-0.001$ \\
370	Gap ratio           & $30\times$ & $35\times$ \\
371	Gating benefit      & none & none \\
372	\bottomrule
373	\end{tabular}
374	\end{table}
375	
376	The TG $-$ LoRA difference is $+0.002$ on Qwen and $-0.001$ on Llama, both within noise ($\pm 0.003$).
377	Two independent architecture families converge on the same conclusion: gating provides zero incremental benefit.
378	
379	\subsection{Downstream Task Validation}
380	\label{sec:downstream}
381	
382	To validate that \gar{} reflects actual behavioral degradation, we design an instruction-retention task: the system prompt contains a format instruction (e.g., ``end every reply with [DONE]''), and we measure compliance across 10 turns over 5 instructions $\times$ 10 conversations each.
383	
384	\begin{table}[H]
385	\centering
386	\caption{Instruction compliance rate by turn (Qwen-2.5-7B). All models show similar degradation; \tg{} provides no benefit.}
387	\label{tab:compliance}
388	\begin{tabular}{lcccc}
389	\toprule
390	\textbf{Turn} & \textbf{Base} & \textbf{TG} & \textbf{LoRA} & \textbf{Base \gar{}} \\
391	\midrule
392	T1  & 0.82 & 0.84 & 0.84 & 0.042 \\
393	T2  & 0.74 & 0.76 & 0.75 & 0.024 \\
394	T3  & 0.68 & 0.69 & 0.68 & 0.022 \\
395	T4  & 0.62 & 0.63 & 0.62 & 0.013 \\
396	T5  & 0.56 & 0.57 & 0.56 & 0.013 \\
397	T6  & 0.50 & 0.51 & 0.50 & 0.009 \\
398	T7  & 0.44 & 0.45 & 0.44 & 0.008 \\
399	T8  & 0.40 & 0.42 & 0.41 & 0.008 \\
400	T9  & 0.38 & 0.39 & 0.38 & 0.016 \\
401	T10 & 0.34 & 0.36 & 0.35 & 0.006 \\
402	\bottomrule
403	\end{tabular}
404	\end{table}
405	
406	Compliance drops from $\sim$82--84\% at turn 1 to $\sim$34--36\% at turn 10 across all models ($\sim$57--59\% relative drop), paralleling the \gar{} degradation pattern ($\sim$71\% drop).
407	\tg{} and LoRA-only differ by only $\sim$1 percentage point, consistent with the \gar{} results.
408	
409	\begin{table}[H]
410	\centering
411	\caption{Pearson correlation between \gar{} and instruction compliance across turns.}
412	\label{tab:compliance-corr}
413	\begin{tabular}{lcc}
414	\toprule
415	\textbf{Model} & \textbf{Pearson $r$} & \textbf{$p$-value} \\
416	\midrule
417	Base      & 0.89 & $<0.001$ \\
418	\tg{}     & 0.87 & $<0.001$ \\
419	LoRA-only & 0.88 & $<0.001$ \\
420	\bottomrule
421	\end{tabular}
422	\end{table}
423	
424	The strong correlation ($r = 0.87$--$0.89$, $p < 0.001$) validates \gar{} as a meaningful behavioral proxy: models that attend less to goal tokens produce fewer instruction-compliant responses.
425	This is a preliminary behavioral validation rather than a comprehensive downstream evaluation, but it establishes that \gar{} degradation has real functional consequences.
426	
427	% ============================================================
428	\section{Analysis}
429	\label{sec:analysis}
430	% ============================================================
431	
432	\subsection{NTP--\gar{} Gradient Conflict}
433	\label{sec:gradient-conflict}
434	
435	To understand \emph{why} gates learn reversed turn conditioning, we analyze the gradient conflict between NTP and \gar{} losses on gate parameters.
436	At three checkpoints during Qwen-2.5-7B training, we perform independent backward passes for each loss and measure the cosine similarity and magnitude ratio of their gradients on gate parameters across all layers.
437	
438	\begin{table}[H]
439	\centering
440	\caption{Per-epoch gradient conflict statistics (Qwen-2.5-7B). Negative cosine similarity indicates opposing gradient directions.}
441	\label{tab:gradient-epoch}
442	\begin{tabular}{lccccc}
443	\toprule
444	\textbf{Checkpoint} & \textbf{Mean $\cos$} & \textbf{Std} & \textbf{Layers $\cos < 0$} & \textbf{Mean mag} & \textbf{Max mag} \\
445	\midrule
446	Epoch 0 (gs 1000) & $-0.087$ & 0.042 & 22/28 & $7.8\times$ & $12.1\times$ \\
447	Epoch 1 (gs 2000) & $-0.062$ & 0.038 & 24/28 & $11.3\times$ & $16.8\times$ \\
448	Epoch 2 (gs 3000) & $-0.045$ & 0.035 & 26/28 & $14.2\times$ & $19.1\times$ \\
449	\bottomrule
450	\end{tabular}
451	\end{table}
452	
453	Cosine similarity is consistently negative across all checkpoints, indicating that NTP and \gar{} gradients push gate parameters in opposing directions.
454	NTP gradients push gates toward 1.0 (identity, preserving the residual stream for next-token prediction), while \gar{} gradients push gates toward 0 (suppressing the residual stream to force attention redistribution).
455	The magnitude ratio grows monotonically from $7.8\times$ to $14.2\times$, reflecting that as training progresses and \gar{} approaches its target, the \gar{} loss gradient shrinks (MSE gradient $\to 0$ near target) while NTP gradient magnitude remains stable.
456	This means NTP increasingly dominates gate learning in later training, precisely when gates should be consolidating their turn-selective behavior.
457	
458	Table~\ref{tab:gradient-layer} provides a per-layer breakdown at epoch 2, revealing that the strongest conflict occurs at layers where gates have deviated most from identity.
459	
460	\begin{table}[H]
461	\centering
462	\caption{Per-layer gradient conflict at Epoch 2 (Qwen-2.5-7B). Layers with lowest gate values (most deviation from identity) show strongest conflict.}
463	\label{tab:gradient-layer}
464	\begin{tabular}{lccccc}
465	\toprule
466	\textbf{Layer} & \textbf{$\cos$ sim} & \textbf{NTP grad} & \textbf{GAR grad} & \textbf{Mag ratio} & \textbf{Gate mean} \\
467	\midrule
468	L3  & $-0.131$ & $2.4\text{e-}3$ & $1.3\text{e-}4$ & $18.5\times$ & 0.801 \\
469	L4  & $-0.124$ & $2.6\text{e-}3$ & $1.4\text{e-}4$ & $18.6\times$ & 0.789 \\
470	L12 & $-0.098$ & $1.8\text{e-}3$ & $1.2\text{e-}4$ & $15.0\times$ & 0.847 \\
471	L14 & $-0.105$ & $2.0\text{e-}3$ & $1.1\text{e-}4$ & $18.2\times$ & 0.928 \\
472	L23 & $-0.072$ & $1.5\text{e-}3$ & $9.8\text{e-}5$ & $15.3\times$ & 0.979 \\
473	L27 & $-0.018$ & $8.2\text{e-}4$ & $1.6\text{e-}4$ & $5.1\times$ & 0.988 \\
474	\bottomrule
475	\end{tabular}
476	\end{table}
477	
478	L3 and L4 show the strongest conflict ($\cos < -0.12$, mag ratio $> 18\times$) and the lowest gate values (0.789--0.801), farthest from identity.
479	These are precisely the layers where NTP exerts the strongest corrective force to push gates back toward 1.0.
480	Upper layers (L27) show weaker conflict because their gates are already near identity (0.988) and contribute little to either loss.
481	
482	\paragraph{Cross-model gradient conflict.}
483	Table~\ref{tab:gradient-crossmodel} confirms that the gradient conflict pattern replicates on Llama-3.1-8B.
484	
485	\begin{table}[H]
486	\centering
487	\caption{Cross-model gradient conflict comparison (Epoch 2). Both architectures show opposing NTP--\gar{} gradients.}
488	\label{tab:gradient-crossmodel}
489	\begin{tabular}{lcc}
490	\toprule
491	\textbf{Metric} & \textbf{Qwen-2.5-7B} & \textbf{Llama-3.1-8B} \\
492	\midrule
493	Mean $\cos$ sim     & $-0.045$ & $-0.058$ \\
494	Std $\cos$ sim      & 0.035    & 0.038 \\
495	Layers $\cos < 0$   & 26/28 (93\%) & 27/32 (84\%) \\
496	Mean mag ratio      & $14.2\times$ & $12.8\times$ \\
497	Max mag ratio       & $19.1\times$ & $18.5\times$ \\
498	\bottomrule
499	\end{tabular}
500	\end{table}
501	
502	Both architectures exhibit negative cosine similarity across $>$80\% of layers with magnitude ratios $>$12$\times$, confirming that gradient conflict is a property of joint NTP + auxiliary attention loss optimization, not of specific model architectures.
503	
504	\subsection{Attention Pattern Analysis}
505	\label{sec:attention-analysis}
506	
507	If gating were effective at inference time, we would expect \tg{} to show increased attention to goal tokens compared to the base model, particularly at later turns.
508	Table~\ref{tab:attention} measures goal attention across four model variants on three standard conversations, averaged across all 28 layers.
509	
510	\begin{table}[H]
511	\centering
512	\caption{Goal attention statistics across models (Qwen-2.5-7B). Differences between models are within noise.}
513	\label{tab:attention}
514	\begin{tabular}{lccccc}
515	\toprule
516	\textbf{Model} & \textbf{Mean} & \textbf{T1} & \textbf{T10} & \textbf{Decay} & \textbf{Peak} \\
517	\midrule
518	Base      & 0.0136 & 0.0312 & 0.0039 & 87.5\% & L1 \\
519	\tg{}     & 0.0148 & 0.0328 & 0.0052 & 84.2\% & L1 \\
520	\ug{}     & 0.0141 & 0.0318 & 0.0046 & 85.6\% & L1 \\
521	LoRA-only & 0.0143 & 0.0321 & 0.0048 & 85.1\% & L2 \\
522	\bottomrule
523	\end{tabular}
524	\end{table}
525	
526	The four models are virtually indistinguishable: \tg{}'s mean goal attention (0.0148) exceeds the base model by only 0.0012 ($\sim$8.8\%), well within noise.
527	All models exhibit 84--88\% decay from T1 to T10, with nearly identical decay curves.
528	Goal attention concentrates in the first few layers (L0--L4) and last few layers (L24--L27), with 2--3 specialized heads per layer carrying $>$80\% of goal attention.
529	
530	This confirms our mechanistic explanation: at inference time, gates with mean values of 0.93--0.98 attenuate the residual stream by only 2--7\%, far below the threshold needed to shift attention distributions through the softmax nonlinearity.
531	The gating mechanism is effectively an identity operation during inference.
532	
533	% ============================================================
534	\section{Discussion}
535	\label{sec:discussion}
536	% ============================================================
537	
538	\subsection{The Distribution Shift Barrier}
539	
540	Our results point to a fundamental barrier facing all auxiliary attention losses trained under teacher-forcing.
541	During training, the model conditions on gold (human-written) context: attention patterns are optimized for a specific distribution of preceding tokens.
542	At inference, the model conditions on its own generated tokens, which follow a different distribution---especially in later turns where generation errors compound.
543	The $30$--$35\times$ \gar{} gap we observe is not a gating-specific failure; it reflects this structural mismatch.
544	
545	This insight generalizes beyond residual gating.
546	Dongre et al.~\cite{dongre2026} reported that goal re-injection (a complementary intervention strategy) also failed.
547	Two independent intervention approaches---operating on different architectural components (residual connections vs.\ input representations)---both fail at the same generalization barrier.
548	This convergent failure strongly suggests that the barrier is fundamental to teacher-forcing optimization of attention-related objectives.
549	
550	\subsection{Why Gradient Competition Prevents Correct Gate Learning}
551	
552	The gate reversal phenomenon (NF1) has a clear mechanistic explanation.
553	NTP loss has a direct, strong gradient path to gate parameters: reducing $g_l$ attenuates the residual stream, immediately increasing NTP loss because the skip connection carries essential information.
554	\gar{} loss has only an indirect, weak path: changing $g_l$ modifies the input to subsequent layers, which must propagate through multiple attention and FFN transformations before affecting the attention distribution that \gar{} measures.
555	
556	At late turns---where \gar{} degradation is worst and intervention is most needed---NTP gradients are largest (because generation is hardest), while \gar{} gradients are smallest (because the MSE loss is already near its target under teacher-forcing).
557	This creates a perverse dynamic: gates become most passive exactly where they should be most active.
558	
559	\subsection{Implications for Attention Steering Methods}
560	
561	Our findings have three implications for the broader attention steering literature:
562	
563	\begin{enumerate}
564	    \item \textbf{Training-time attention supervision is insufficient.} Any method that optimizes attention-related objectives under teacher-forcing will face the same distribution shift. This includes attention supervision losses, attention-guided training, and auxiliary attention prediction objectives.
565	
566	    \item \textbf{Inference-time intervention may be necessary.} Methods that operate at inference time---such as activation patching, inference-time intervention~\cite{li2024inference}, or attention-guided decoding---bypass the training--inference distribution mismatch entirely, as they modify the actual inference computation rather than hoping that training-time patterns generalize.
567	
568	    \item \textbf{Exposure bias mitigation could help.} Techniques developed for the standard exposure bias problem---scheduled sampling~\cite{bengio2015scheduled}, sequence-level training~\cite{ranzato2016sequence}---could potentially be adapted to auxiliary attention losses, training the model under its own generated context rather than gold context.
569	\end{enumerate}
570	
571	\subsection{Limitations}
572	
573	Our study has several limitations.
574	First, we evaluate on 7--8B parameter models; scaling behavior at larger model sizes is unknown.
575	Second, our downstream task evaluation (instruction retention) is preliminary; comprehensive evaluation across diverse tasks would strengthen the behavioral validation.
576	Third, we do not explore all possible gating architectures---vector gates, attention-conditioned gates, or gates with separate optimization schedules might behave differently, though the fundamental distribution shift barrier would likely remain.
577	Fourth, while the $30$--$35\times$ gap strongly suggests a distribution shift explanation, we do not have a formal proof that no training-time objective can overcome this gap.
578	
579	% ============================================================
580	\section{Conclusion}
581	\label{sec:conclusion}
582	% ============================================================
583	
584	We investigated whether lightweight residual gating can address multi-turn attention degradation in LLMs.
585	Despite principled design motivation (residual stream persistence of goal information), systematic loss engineering (seven configurations across four design families), and successful training convergence (\gar{}: $0.02 \to 0.48$), gating \emph{completely fails} at inference ($30$--$35\times$ \gar{} gap).
586	Mechanistic analysis reveals three coupled failure modes: NTP--\gar{} gradient competition ($7.8$--$14.2\times$ magnitude dominance causing gate reversal in $>$80\% of layers), teacher-forcing$\to$generation distribution shift destroying learned attention patterns, and insufficient inference-time gate modulation (2--7\% residual attenuation).
587	Cross-model validation on Qwen-2.5-7B and Llama-3.1-8B confirms these findings are architecture-independent.
588	
589	Our central message is not that gating failed, but \emph{why} it failed: teacher-forcing distribution shift is a structural barrier for all auxiliary attention losses.
590	We hope this analysis redirects effort toward inference-time attention intervention and exposure-bias-aware training of attention objectives.
591	
592	% ============================================================
593	% References
594	% ============================================================
595	\begin{thebibliography}{20}
596	
597	\bibitem{dongre2026}
598	Dongre, A., et al.
599	\newblock Goal attention degradation in multi-turn dialogue: Measurement and analysis across model families.
600	\newblock In \emph{Proceedings of ACL}, 2026.
601	
602	\bibitem{liu2024lost}
603	Liu, N.~F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., and Liang, P.
604	\newblock Lost in the middle: How language models use long contexts.
605	\newblock \emph{Transactions of the ACL}, 2024.
606	
607	\bibitem{fan2020layerdrop}
608	Fan, A., Grave, E., and Joulin, A.
609	\newblock Reducing transformer depth on demand with structured dropout.
610	\newblock In \emph{Proceedings of ICLR}, 2020.
611	
612	\bibitem{schuster2022confident}
613	Schuster, T., Fisch, A., Jaakkola, T., and Barzilay, R.
614	\newblock Confident adaptive language modeling.
615	\newblock In \emph{Proceedings of NeurIPS}, 2022.
616	
617	\bibitem{raposo2024mixture}
618	Raposo, D., Ritter, S., Richards, B., Lillicrap, T., Humphreys, P.~C., and Santoro, A.
619	\newblock Mixture-of-depths: Dynamically allocating compute in transformer-based language models.
620	\newblock \emph{arXiv preprint arXiv:2404.02258}, 2024.
621	
622	\bibitem{liu2016attention}
623	Liu, L., Utiyama, M., Finch, A., and Sumita, E.
624	\newblock Neural machine translation with supervised attention.
625	\newblock In \emph{Proceedings of COLING}, 2016.
626	
627	\bibitem{vig2020investigating}
628	Vig, J., Gehrmann, S., Belinkov, Y., Qian, S., Nishi, D., Zhang, Y., Patel, Y., Luo, J., and Rush, A.~M.
629	\newblock Investigating gender bias in language models using causal mediation analysis.
630	\newblock In \emph{Proceedings of NeurIPS}, 2020.
631	
632	\bibitem{li2024inference}
633	Li, K., Patel, O., Vi{\'e}gas, F., Pfister, H., and Wattenberg, M.
634	\newblock Inference-time intervention: Eliciting truthful answers from a language model.
635	\newblock In \emph{Proceedings of NeurIPS}, 2024.
636	
637	\bibitem{hu2022lora}
638	Hu, E.~J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L., and Chen, W.
639	\newblock LoRA: Low-rank adaptation of large language models.
640	\newblock In \emph{Proceedings of ICLR}, 2022.
641	
642	\bibitem{ranzato2016sequence}
643	Ranzato, M., Chopra, S., Auli, M., and Zaremba, W.
644	\newblock Sequence level training with recurrent neural networks.
645	\newblock In \emph{Proceedings of ICLR}, 2016.
646	
647	\bibitem{bengio2015scheduled}
648	Bengio, S., Vinyals, O., Jaitly, N., and Shazeer, N.
649	\newblock Scheduled sampling for sequence prediction with recurrent neural networks.
650	\newblock In \emph{Proceedings of NeurIPS}, 2015.
651	
652	\end{thebibliography}
653	
654	\end{document}
655	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e1de52b-a293-4811-899d-884dd591e132",
  "isSidechain": true,
  "promptId": "a15e1f25-f380-4a76-9d77-88873bcc9e37",
  "agentId": "a15415a71738e1c47",
  "type": "user",
  "uuid": "f3ea4af7-2186-4e92-9f24-48fda4add802",
  "sourceToolAssistantUUID": "3e1de52b-a293-4811-899d-884dd591e132",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-19T14:45:32.121Z_

Perfect! I found comprehensive paper drafts. Now let me check the median and worst versions to see if there are differences in the equation definitions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3ea4af7-2186-4e92-9f24-48fda4add802",
  "isSidechain": true,
  "agentId": "a15415a71738e1c47",
  "requestId": "req_011CbC7CuEJ9LwHYA1HRn7w3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "122d881e-0a72-414b-b39b-359e85d13d78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PmH9zA271bzycQLoQwkMP6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 18385,
      "cache_read_input_tokens": 23618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18385,
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

_source line 19 · 2026-05-19T14:45:33.209Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ScisFKSJzajAg8uo8p71jY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/median/paper.tex",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "122d881e-0a72-414b-b39b-359e85d13d78",
  "isSidechain": true,
  "agentId": "a15415a71738e1c47",
  "requestId": "req_011CbC7CuEJ9LwHYA1HRn7w3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "da03dbb6-4840-440b-a798-f87037125f2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PmH9zA271bzycQLoQwkMP6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 18385,
      "cache_read_input_tokens": 23618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18385,
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

_source line 20 · 2026-05-19T14:45:33.216Z_

<details><summary>↩ Tool result · `toolu_01ScisFKSJzajAg8uo8p71jY`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{natbib}
12	\usepackage{hyperref}
13	\renewcommand{\citep}{\citealp}
14	\newcommand{\citet}[1]{\citeauthor{#1}~(\citeyear{#1})}
15	
16	\title{Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation:\\A Mechanistic Analysis}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	\begin{abstract}
24	Large Language Models (LLMs) suffer from progressive attention degradation in multi-turn dialogue: the Goal Attention Ratio (GAR), which measures how much attention response tokens allocate to goal-relevant tokens, drops by over 70\% across conversation turns. Prior work shows that goal information persists in the residual stream even as the attention channel closes, suggesting that a learnable gate on residual connections could recover goal attention. We test this hypothesis through ThreadGate, a per-layer gating module jointly trained with next-token prediction (NTP) and GAR objectives. ThreadGate successfully raises GAR from 0.02 to 0.48 during training, but this improvement fails to transfer to inference (GAR = 0.022 on held-out data), producing an order-of-magnitude gap of $\sim$22$\times$. We trace this failure to a distribution shift between teacher-forced training and autoregressive generation: attention patterns optimized under gold contexts do not generalize when the model conditions on its own outputs. Two amplifying mechanisms further explain the failure: (1) NTP gradients dominate gate parameters by 8--14$\times$ in magnitude, causing gates to learn a reversed turn conditioning pattern, and (2) at inference, gates attenuate residual updates by only 2--7\%, producing near-identity transformations. Four-way ablation confirms that gating provides zero statistically significant incremental benefit over LoRA-only fine-tuning, with partial cross-model replication on Llama-3.1-8B. These findings indicate that auxiliary attention losses optimized under teacher-forcing face a fundamental generalization barrier, suggesting that future work should explore inference-time interventions or exposure bias mitigation.
25	\end{abstract}
26	
27	\section{Introduction}
28	
29	Multi-turn dialogue is a core use case for LLMs, yet model performance degrades as conversations grow longer. Users report that chatbots ``forget'' system instructions, lose coherence with earlier context, and produce increasingly generic responses in extended interactions. \citet{dongre2026} formalized this degradation through the Goal Attention Ratio (GAR), showing that attention to goal-relevant tokens drops by 27--48\% over 50 turns across 12 models. Their analysis further revealed a striking asymmetry: while the attention channel progressively closes, linear probes on the residual stream maintain AUC scores up to 0.98, indicating that goal information \emph{persists} in the model's hidden states but becomes inaccessible through the attention mechanism.
30	
31	This asymmetry creates a natural hypothesis. If goal information survives in the residual stream but attention fails to retrieve it, then a learnable gate on the residual connection should be able to modulate the information flow and restore goal attention. Per-layer residual gating is well-studied in the context of adaptive computation depth \cite{wang2022skipnet,raposo2024mixture} and has shown success in selectively controlling information flow through transformer layers. Combined with an auxiliary GAR loss that directly optimizes for goal attention, this approach represents the most direct architectural response to the diagnosed failure mode.
32	
33	We implement this hypothesis as ThreadGate, a per-layer scalar gating module trained with a joint NTP and GAR objective. Through systematic exploration of four loss families across seven training configurations, we identify MSE-based GAR targeting with gate diversity regularization as the only design that achieves stable training convergence. ThreadGate successfully optimizes GAR during training (0.02 $\to$ 0.48), confirming that the loss design is sound and the gating mechanism has sufficient capacity.
34	
35	However, this training success completely fails to transfer to inference. On held-out evaluation data, ThreadGate achieves a GAR of only 0.022, producing an order-of-magnitude gap ($\sim$22$\times$) between training and inference. Four-way ablation comparing ThreadGate, Uniform Gate, LoRA-only fine-tuning, and the base model reveals that gating provides zero statistically significant incremental benefit: ThreadGate's inference GAR exceeds LoRA-only by just 0.004 ($p > 0.1$), while perplexity remains equivalent (2.81 vs.\ 2.82).
36	
37	Our central finding is that teacher-forcing training creates a distribution shift that fundamentally undermines auxiliary attention losses. During training, the model optimizes attention patterns conditioned on gold (human-written) contexts. At inference, it conditions on its own generated outputs, whose distribution differs systematically from the training distribution. This shift renders the learned attention patterns ineffective. We identify two amplifying mechanisms: NTP gradients dominate gate parameters by 8--14$\times$ in magnitude (causing reversed turn conditioning where gates become passive precisely at late turns where intervention is most needed), and gates converge to near-identity transformations (2--7\% attenuation) that are too weak to shift attention patterns at inference time.
38	
39	Partial cross-model replication on Llama-3.1-8B confirms the qualitative pattern: the training-inference gap persists ($\sim$12$\times$) and gating again provides no significant benefit over LoRA-only training. Combined with the independent failure of goal re-injection reported by \citet{dongre2026}, these results provide convergent evidence that auxiliary attention losses optimized under teacher-forcing face a strong empirical generalization barrier.
40	
41	Our contributions are:
42	\begin{enumerate}
43	\item \textbf{Quantitative evidence of teacher-forcing distribution shift for attention steering.} We provide the first measurement of how the training-to-inference distribution shift destroys auxiliary attention loss generalization, documenting an order-of-magnitude GAR gap that persists on held-out data ($\sim$22$\times$ for Qwen-2.5-7B, $\sim$12$\times$ for Llama-3.1-8B).
44	\item \textbf{Layer-wise quantification of NTP-GAR gradient competition.} We show that NTP gradients dominate gate parameters and cause reversed turn conditioning, providing a mechanistic explanation for why gates fail to learn useful attention interventions.
45	\item \textbf{Systematic gating intervention with principled ablation.} We explore four loss families across seven configurations and conduct four-way ablation isolating the contribution of turn conditioning (ThreadGate vs.\ Uniform Gate) and gating itself (ThreadGate vs.\ LoRA-only).
46	\item \textbf{Partial cross-model validation} on Llama-3.1-8B (GQA architecture) confirms the failure mode generalizes beyond a single model, with architectural differences in attention head sharing providing additional analytical insight.
47	\end{enumerate}
48	
49	\section{Related Work}
50	
51	\paragraph{Multi-turn dialogue degradation.}
52	Performance degradation in extended conversations has been documented across multiple dimensions, including coherence loss \cite{zhang2024dialogueconsistency}, instruction forgetting \cite{chen2025instructionfollow}, and context utilization decline \cite{liu2024lost}. \citet{dongre2026} provided the first mechanistic account through GAR analysis, showing that attention to goal tokens systematically decreases while residual stream probes maintain high accuracy. Their attempt at goal re-injection through attention heads (Appendix H) also failed, foreshadowing the structural difficulty we characterize in this work.
53	
54	\paragraph{Residual gating and adaptive depth.}
55	Learnable gates on residual connections have been explored for adaptive computation. SkipNet \cite{wang2022skipnet} uses binary gates for layer skipping, while Mixture of Depths \cite{raposo2024mixture} applies per-token routing decisions. LayerDrop \cite{fan2020layerdrop} regularizes by randomly dropping layers during training. Our work differs in applying residual gating not for efficiency but for attention steering, with the gate trained to modulate residual flow in service of an auxiliary GAR objective.
56	
57	\paragraph{Attention steering and intervention.}
58	Auxiliary attention losses have been used to encourage specific attention patterns \cite{strubell2018linguistically,deshpande2024gatedattention}. Inference-time attention intervention methods modify attention weights directly during generation \cite{li2024inferencetime,turner2024activationsteering}. Our findings suggest that training-time approaches face a distribution shift barrier that inference-time methods may avoid. The exposure bias literature \cite{ranzato2016sequence,bengio2015scheduled} has established that teacher-forcing creates distributional mismatch for generation quality; we extend this insight to show that auxiliary attention losses are particularly vulnerable to this mismatch.
59	
60	\section{Background}
61	
62	\paragraph{Goal Attention Ratio.}
63	Following \citet{dongre2026}, we define the Goal Attention Ratio (GAR) as the fraction of attention that response tokens allocate to goal-relevant tokens. Specifically, for a response token $r$ at layer $\ell$ and head $h$, the per-token GAR is:
64	\begin{equation}
65	\text{GAR}(r, \ell, h) = \sum_{g \in \mathcal{G}} \alpha^{(\ell,h)}_{r,g}
66	\end{equation}
67	where $\mathcal{G}$ is the set of goal tokens (system prompt task tokens in the Dongre formulation) and $\alpha^{(\ell,h)}_{r,g}$ is the attention weight from $r$ to $g$. The GAR is averaged across response tokens, layers, and heads to produce a scalar per conversation turn.
68	
69	We use two GAR variants: \textbf{GAR-Dongre} (goal tokens = system prompt task tokens, response tokens = all response tokens) for comparability with prior work, and \textbf{GAR-ours} (goal tokens = system prompt + first user query, response tokens = last token per assistant turn) as the training signal. Both variants show the same qualitative degradation pattern, and the training-inference gap is consistent across definitions.
70	
71	\paragraph{Residual stream persistence.}
72	\citet{dongre2026} trained linear probes on the residual stream at each layer and found that goal information remains highly recoverable (AUC up to 0.98) even at late turns where GAR has dropped to near zero. This decoupling between attention-based access and residual-based availability motivates our gating approach: if the information exists in the residual stream, gating the residual connection should be able to control how much of it flows into subsequent attention computations.
73	
74	\section{Method}
75	
76	\subsection{ThreadGate Architecture}
77	
78	ThreadGate adds a learnable scalar gate $g_\ell \in (0, 1)$ to each transformer layer $\ell$. The standard residual connection $\mathbf{x}_{\ell+1} = \mathbf{x}_\ell + f_\ell(\mathbf{x}_\ell)$ is modified to:
79	\begin{equation}
80	\mathbf{x}_{\ell+1} = g_\ell \cdot \mathbf{x}_\ell + f_\ell(\mathbf{x}_\ell)
81	\end{equation}
82	where $f_\ell$ is the output of the attention and feed-forward sub-layers at layer $\ell$. The gate is parameterized via sigmoid: $g_\ell = \sigma(w_\ell)$, with $w_\ell$ initialized to 3.0 (corresponding to $g_\ell \approx 0.95$) to preserve the pre-trained model's behavior at initialization. All other model parameters are fine-tuned through LoRA \cite{hu2022lora} with rank 16 on query and value projections.
83	
84	\subsection{Training Objective}
85	
86	The training loss combines next-token prediction with an MSE-based GAR target and gate diversity regularization:
87	\begin{equation}
88	\mathcal{L} = \mathcal{L}_{\text{NTP}} + \lambda_{\text{GAR}} \cdot \mathcal{L}_{\text{GAR}} + \lambda_{\text{div}} \cdot \mathcal{L}_{\text{div}}
89	\end{equation}
90	
91	The GAR loss uses a symmetric MSE formulation that penalizes both under- and over-shooting a target GAR value $\tau$:
92	\begin{equation}
93	\mathcal{L}_{\text{GAR}} = \frac{1}{T} \sum_{t=1}^{T} (\text{GAR}_t - \tau)^2
94	\end{equation}
95	where $\text{GAR}_t$ is the computed GAR at turn $t$ and $\tau$ is a turn-dependent target derived from the base model's turn-1 GAR. The gate diversity loss $\mathcal{L}_{\text{div}} = -\text{Var}(\{g_\ell\}_{\ell=1}^{L})$ encourages gates to develop layer-specific behavior rather than collapsing to a uniform value.
96	
97	\subsection{Loss Design Evolution}
98	
99	We explored four loss families across seven configurations before arriving at the MSE+gate\_div design (v7):
100	\begin{itemize}
101	\item \textbf{Cumulative (v1--v2):} Directly maximize cumulative GAR across turns. Failed due to unbounded gradients and training instability.
102	\item \textbf{Maximize (v3--v5):} Various formulations to maximize per-turn GAR. Achieved partial training progress but oscillated without convergence.
103	\item \textbf{Smooth saturation (v6):} Saturating loss to bound gradients. Converged but to a suboptimal GAR plateau.
104	\item \textbf{MSE target (v7):} Symmetric MSE toward a target value with gate diversity. The only design achieving stable convergence to GAR $\approx$ 0.48.
105	\end{itemize}
106	
107	\subsection{Ablation Variants}
108	
109	To isolate the contribution of different components, we train four model variants:
110	\begin{itemize}
111	\item \textbf{ThreadGate (TG):} Per-layer learned gates + LoRA + NTP + GAR loss.
112	\item \textbf{Uniform Gate (UG):} Single shared gate (no per-layer conditioning) + LoRA + NTP + GAR loss.
113	\item \textbf{LoRA-only:} Standard LoRA fine-tuning with NTP loss only. No gates, no GAR loss. Gate fixed at 1.0 (identity).
114	\item \textbf{Base:} Pre-trained model without any fine-tuning.
115	\end{itemize}
116	
117	The comparison TG vs.\ UG isolates the value of per-layer turn conditioning. The comparison TG vs.\ LoRA-only isolates whether gating (with its auxiliary GAR loss) provides any benefit beyond standard fine-tuning.
118	
119	\section{Experiments}
120	
121	\subsection{Setup}
122	
123	\paragraph{Models.} Our primary experiments use Qwen-2.5-7B (28 layers, multi-head attention with 28 heads). Cross-model validation uses Llama-3.1-8B (32 layers, grouped-query attention with 8 KV heads shared across 32 query heads).
124	
125	\paragraph{Data.} We fine-tune on a subset of UltraChat multi-turn dialogues. Training uses indices 0--7999 (1,060 dialogues after filtering for $\geq$10 turns). Held-out evaluation uses 50 dialogues sampled from indices $\geq$8000, ensuring no overlap with training data.
126	
127	\paragraph{Training.} All models are trained for 3 epochs with learning rate $2 \times 10^{-5}$, batch size 4, gradient accumulation 2, and LoRA rank 16 on Q/V projections. ThreadGate and Uniform Gate additionally optimize the GAR loss with $\lambda_{\text{GAR}} = 0.1$ and $\lambda_{\text{div}} = 0.01$.
128	
129	\paragraph{Evaluation metrics.} We report GAR-Dongre (for comparability with prior work), GAR-ours (matching the training signal), and perplexity (PPL) on the held-out set. GAR is computed under both teacher-forcing (gold context) and autoregressive inference.
130	
131	\subsection{Main Results: Qwen-2.5-7B}
132	
133	Table~\ref{tab:main_results} presents the four-way evaluation on held-out data. The central finding is that gating provides no statistically significant benefit over LoRA-only fine-tuning on any metric.
134	
135	\begin{table}[t]
136	\centering
137	\caption{Held-out evaluation on Qwen-2.5-7B. GAR-Dongre and GAR-ours are mid-turn averages (turns 2--10) under autoregressive inference. PPL is response perplexity. ThreadGate training GAR-ours reaches 0.462, but inference GAR-Dongre drops to 0.022 ($\sim$22$\times$ gap). The difference between ThreadGate and LoRA-only is not statistically significant on any metric.}
138	\label{tab:main_results}
139	\small
140	\begin{tabular}{lccc}
141	\toprule
142	\textbf{Model} & \textbf{GAR-Dongre} $\uparrow$ & \textbf{GAR-ours} $\uparrow$ & \textbf{PPL} $\downarrow$ \\
143	\midrule
144	Base & 0.005 & 0.012 & 4.38 \\
145	ThreadGate & 0.022 & 0.462 & 2.81 \\
146	Uniform Gate & 0.018 & 0.456 & 2.79 \\
147	LoRA-only & 0.018 & 0.458 & 2.82 \\
148	\midrule
149	TG $-$ LoRA & +0.004 (ns) & +0.004 & $-$0.01 \\
150	\bottomrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da03dbb6-4840-440b-a798-f87037125f2b",
  "isSidechain": true,
  "promptId": "a15e1f25-f380-4a76-9d77-88873bcc9e37",
  "agentId": "a15415a71738e1c47",
  "type": "user",
  "uuid": "5f55ad73-baa5-4c45-914d-319e15fe72e3",
  "sourceToolAssistantUUID": "da03dbb6-4840-440b-a798-f87037125f2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T14:45:33.415Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SP3dZAAdxHc4qajBiW5DU5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.tex",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f55ad73-baa5-4c45-914d-319e15fe72e3",
  "isSidechain": true,
  "agentId": "a15415a71738e1c47",
  "requestId": "req_011CbC7CuEJ9LwHYA1HRn7w3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6992cdec-06a4-4cc2-bc2f-04dd7f0499b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PmH9zA271bzycQLoQwkMP6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 18385,
      "cache_read_input_tokens": 23618,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18385
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 251,
          "cache_read_input_tokens": 23618,
          "cache_creation_input_tokens": 18385,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18385,
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

_source line 22 · 2026-05-19T14:45:33.420Z_

<details><summary>↩ Tool result · `toolu_01SP3dZAAdxHc4qajBiW5DU5`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{multirow}
8	\usepackage{hyperref}
9	\usepackage[margin=2.5cm]{geometry}
10	\usepackage{natbib}
11	\usepackage{xcolor}
12	
13	\title{Failure Mode Taxonomy of Residual Gating for Multi-Turn Attention Recovery:\\A Mechanistic Case Study under Next-Token Prediction Dominance}
14	
15	\author{Anonymous}
16	\date{}
17	
18	\begin{document}
19	\maketitle
20	
21	% =========================================================================
22	\begin{abstract}
23	Multi-turn dialogue performance in large language models degrades as conversations lengthen, with goal attention ratio (GAR) declining by 48--71\% across architectures. Prior work shows that goal-relevant information persists in the residual stream even as the attention channel closes, motivating residual gating as an architectural intervention. We implement ThreadGate, a per-layer gating module trained jointly with next-token prediction (NTP) and GAR objectives, and conduct a systematic study spanning seven loss configurations (v1--v7) and four-way ablation (ThreadGate / Uniform Gate / LoRA-only / Base). On Qwen-2.5-7B, ThreadGate achieves 0.48 training GAR but only 0.032 at inference on held-out data, revealing a 15$\times$ training-inference gap that persists across evaluation sets. Four-way ablation shows ThreadGate provides only marginal, non-significant improvement over LoRA-only ($\Delta$=0.010, $p$=0.08). Cross-architecture analysis on Llama-3.1-8B reveals architecture-dependent susceptibility: GAR degradation is milder (48\% vs.\ 71\%), the training-inference gap shrinks to 2.4$\times$, and gate reversal affects only 34\% of layers versus 96\% in Qwen. NTP gradient magnitude dominates GAR gradients by 3--6$\times$, though directional conflict is noisy and architecture-dependent. Downstream instruction retention correlates weakly with GAR ($r$=0.31, $p$=0.18), suggesting GAR captures only part of the multi-turn degradation phenomenon. We contribute a failure mode taxonomy---reverse turn conditioning, training-inference distribution shift, and insufficient gate intervention---and discuss implications for auxiliary attention losses optimized under teacher forcing.
24	\end{abstract}
25	
26	% =========================================================================
27	\section{Introduction}
28	
29	Large language models exhibit systematic performance degradation in multi-turn dialogue as conversation length increases \citep{dongre2026gar}. This degradation manifests across multiple dimensions: instruction following accuracy drops, goal-relevant information receives progressively less attention, and response quality declines. Dongre et al.\ quantify this through the Goal Attention Ratio (GAR), documenting 27--48\% drops over extended conversations across twelve models, while their residual stream probes reveal that goal information persists (AUC up to 0.98) even as the attention channel closes.
30	
31	This creates a natural hypothesis: if goal information remains in the residual stream but attention fails to access it, a learnable gate on the residual connection should recover it. We test this hypothesis through ThreadGate, a per-layer gating module that modulates residual stream updates based on learned attention steering signals, trained jointly with NTP and GAR objectives.
32	
33	Our investigation yields a detailed taxonomy of failure modes rather than a clean negative result. On Qwen-2.5-7B, ThreadGate successfully optimizes GAR during training (0.02$\to$0.48), but on held-out conversations the training-inference gap is 15$\times$, with inference GAR reaching only 0.032. Four-way ablation (ThreadGate vs.\ Uniform Gate vs.\ LoRA-only vs.\ Base) reveals that gating provides marginal, statistically non-significant improvement over LoRA adaptation alone. We identify three coupled failure mechanisms: (1) \textbf{reverse turn conditioning}---NTP gradients push gates toward identity, causing 96\% of layers to suppress intervention where it is most needed; (2) \textbf{training-inference distribution shift}---attention patterns learned under teacher forcing do not transfer to autoregressive generation; (3) \textbf{insufficient intervention magnitude}---gates attenuate residual updates by only 2--7\% at inference.
34	
35	Cross-architecture analysis on Llama-3.1-8B reveals that both the severity of GAR degradation and the effectiveness of gating are architecture-dependent. Llama-3 exhibits milder GAR decay (48\% vs.\ 71\%), a much smaller training-inference gap (2.4$\times$), and gate reversal in only 34\% of layers. These differences challenge any universality claim but reinforce the value of architecture-specific mechanistic analysis.
36	
37	Our contributions are: (1) a detailed failure mode taxonomy of residual gating under NTP dominance, grounded in a systematic design space exploration (v1--v7) and four-way ablation; (2) quantitative evidence that teacher-forcing distribution shift degrades auxiliary attention loss generalization, with gap magnitudes of 2.4--15$\times$ depending on architecture; (3) cross-architecture comparison revealing architecture-dependent susceptibility to multi-turn attention degradation; (4) a downstream sanity check establishing the partial but imperfect correspondence between GAR and instruction retention.
38	
39	% =========================================================================
40	\section{Related Work}
41	
42	\paragraph{Multi-turn dialogue degradation.}
43	Performance degradation in extended conversations has been documented across model families \citep{dongre2026gar}. Attention dilution, where goal-relevant tokens receive progressively less attention as context grows, is one proposed mechanism. Dongre et al.\ introduce GAR as a quantitative measure and show that goal information persists in residual streams despite attention channel closure.
44	
45	\paragraph{Residual gating and adaptive computation.}
46	Gating mechanisms on residual connections have been explored for adaptive depth \citep{elbayad2020depth}, mixture of experts \citep{shazeer2017moe}, and layer-selective computation. Our work applies per-layer scalar gating specifically to steer attention toward goal tokens, differing from prior work in objective (attention recovery rather than efficiency).
47	
48	\paragraph{Attention steering and intervention.}
49	Methods for steering attention include attention supervision \citep{liu2016attn}, auxiliary attention losses, and inference-time intervention \citep{li2023iti}. Our work connects to the exposure bias literature \citep{ranzato2016sequence, bengio2015scheduled}: teacher-forcing creates distributional mismatch between training and inference, which we show specifically disrupts auxiliary attention loss generalization.
50	
51	% =========================================================================
52	\section{Background}
53	
54	\subsection{Goal Attention Ratio}
55	
56	Following Dongre et al., we define the Goal Attention Ratio (GAR) as the fraction of attention mass allocated to goal-relevant tokens. Let $\mathcal{G}$ denote the set of goal token positions (system prompt task tokens) and $\alpha_{i,j}^{(l,h)}$ denote the attention weight from position $i$ to position $j$ at layer $l$, head $h$. GAR-Dongre is:
57	\begin{equation}
58	\text{GAR}(i) = \frac{1}{L \cdot H} \sum_{l,h} \sum_{j \in \mathcal{G}} \alpha_{i,j}^{(l,h)}
59	\end{equation}
60	where response token positions $i$ are averaged. We report GAR at mid-conversation turns following Dongre et al.'s protocol.
61	
62	We also define GAR-Ours, which extends goal tokens to include the first user query and uses last-token-per-turn as response positions for more stable measurement. Both definitions yield consistent results in our experiments.
63	
64	\subsection{Residual Stream Persistence}
65	
66	Dongre et al.\ demonstrate via linear probes that goal-relevant information persists in the residual stream (AUC$=$0.98) even when attention to goal tokens drops substantially. This persistence motivates our intervention: if information is present but attention fails to route it, modulating the residual connection should help.
67	
68	% =========================================================================
69	\section{Method}
70	
71	\subsection{ThreadGate Architecture}
72	
73	ThreadGate introduces a learnable scalar gate $g_l \in (0,1)$ at each transformer layer $l$. The gated residual update becomes:
74	\begin{equation}
75	\mathbf{x}_{l+1} = \mathbf{x}_l + g_l \cdot f_l(\mathbf{x}_l)
76	\end{equation}
77	where $f_l$ is the standard transformer block output. Each $g_l$ is parameterized as $g_l = \sigma(w_l)$ with learnable scalar $w_l$, initialized such that $g_l \approx 1$ (identity initialization). The model backbone is augmented with LoRA adapters (rank 16) for efficient fine-tuning.
78	
79	\subsection{Loss Design Space: v1--v7}
80	
81	We explore seven loss configurations spanning four loss families:
82	
83	\begin{itemize}
84	\item \textbf{v1--v2 (Cumulative)}: Direct GAR maximization via cumulative attention reward. Failed to converge---GAR remained near baseline.
85	\item \textbf{v3--v5 (Maximize)}: Direct GAR maximization with different normalization schemes. Unstable training dynamics.
86	\item \textbf{v6 (Smooth saturation)}: Saturating reward to prevent attention collapse. Partial convergence.
87	\item \textbf{v7 (MSE target + gate divergence)}: $\mathcal{L} = \mathcal{L}_{\text{NTP}} + \lambda_1 \mathcal{L}_{\text{MSE}} + \lambda_2 \mathcal{L}_{\text{gate\_div}}$, where $\mathcal{L}_{\text{MSE}}$ targets a GAR value and $\mathcal{L}_{\text{gate\_div}}$ encourages gate diversity. \textbf{Only configuration achieving training convergence.}
88	\end{itemize}
89	
90	The v7 joint loss balances NTP quality preservation with GAR optimization. The MSE component provides a stable gradient signal by targeting a specific GAR value rather than unbounded maximization, while gate divergence regularization prevents gates from collapsing to uniform values.
91	
92	\subsection{Training Setup}
93	
94	We train on UltraChat multi-turn conversations (3 epochs, conversations with index $<$8000). Qwen-2.5-7B and Llama-3.1-8B serve as base models. LoRA rank is 16 for all configurations. Four-way ablation: ThreadGate (v7), Uniform Gate (UG, shared gate across layers), LoRA-only (no gating), and Base (no fine-tuning).
95	
96	% =========================================================================
97	\section{Experiments}
98	
99	\subsection{Qwen-2.5-7B: Four-Way Ablation on Held-Out Data}
100	
101	We evaluate all four configurations on 50 held-out UltraChat conversations (index$\geq$8000) unseen during training. Table~\ref{tab:heldout_4way} presents the results.
102	
103	\begin{table}[h]
104	\centering
105	\caption{Four-way evaluation on held-out conversations ($n$=50, UltraChat idx$\geq$8000). Recovery (pp) = GAR improvement over Base in percentage points $\times$100.}
106	\label{tab:heldout_4way}
107	\begin{tabular}{lcccc}
108	\toprule
109	Model & GAR-D mid & GAR-O mid & PPL & Recovery \\
110	\midrule
111	Base       & 0.0028 & 0.0095 & 4.35 & -- \\
112	TG (v7)    & 0.032  & 0.038  & 2.71 & 2.92 \\
113	UG         & 0.029  & 0.035  & 2.68 & 2.62 \\
114	LoRA-only  & 0.022  & 0.028  & 2.69 & 1.92 \\
115	\bottomrule
116	\end{tabular}
117	\end{table}
118	
119	All fine-tuned models substantially improve over Base in both GAR and PPL, but the differences \emph{among} fine-tuned models are small. ThreadGate achieves the highest GAR (0.032 Dongre, 0.038 Ours) but the advantage over LoRA-only is marginal ($\Delta$=0.010 Dongre, $p$=0.08 paired $t$-test). Uniform Gate performs between TG and LoRA-only. PPL is comparable across fine-tuned variants (2.68--2.71), indicating no meaningful NTP quality penalty from gating.
120	
121	\subsection{Training-Inference GAR Gap}
122	
123	Table~\ref{tab:gap} compares the training-inference GAR gap across evaluation sets.
124	
125	\begin{table}[h]
126	\centering
127	\caption{Training-inference GAR gap: original evaluation set vs.\ held-out.}
128	\label{tab:gap}
129	\begin{tabular}{lccc}
130	\toprule
131	Eval set & Training GAR & Inference GAR (TG-D) & Gap ratio \\
132	\midrule
133	Original ($n$=5)   & 0.48 & 0.0157 & 30.6$\times$ \\
134	Held-out ($n$=50)  & 0.48 & 0.032  & 15.0$\times$ \\
135	\bottomrule
136	\end{tabular}
137	\end{table}
138	
139	The original 30$\times$ gap shrinks to 15$\times$ on held-out data, indicating that the original evaluation set underestimated inference GAR due to limited sample size and potential topic distribution effects. The 15$\times$ gap remains substantial: attention patterns learned under teacher forcing transfer poorly to autoregressive generation, but the magnitude is less dramatic than initially observed. We report the 15$\times$ held-out figure as our primary estimate.
140	
141	\subsection{Llama-3.1-8B: GAR Degradation Diagnosis}
142	
143	To assess cross-architecture generality, we first measure baseline GAR degradation on Llama-3.1-8B (Table~\ref{tab:llama_diag}).
144	
145	\begin{table}[h]
146	\centering
147	\caption{Llama-3.1-8B GAR degradation across 10 turns ($n$=5 conversations).}
148	\label{tab:llama_diag}
149	\begin{tabular}{ccc}
150	\toprule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6992cdec-06a4-4cc2-bc2f-04dd7f0499b2",
  "isSidechain": true,
  "promptId": "a15e1f25-f380-4a76-9d77-88873bcc9e37",
  "agentId": "a15415a71738e1c47",
  "type": "user",
  "uuid": "4956f906-d3df-4bce-8224-9e9520098c51",
  "sourceToolAssistantUUID": "6992cdec-06a4-4cc2-bc2f-04dd7f0499b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-19T14:45:35.883Z_

Now let me search for specific equation references to understand the gating mechanism equations better.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4956f906-d3df-4bce-8224-9e9520098c51",
  "isSidechain": true,
  "agentId": "a15415a71738e1c47",
  "requestId": "req_011CbC7DDFWdGJcsZbrpELvH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0827f430-30bf-44a9-83ae-701676f97292",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UCDvdq9ubnEKM51sbaojts",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9159,
      "cache_read_input_tokens": 42003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9159,
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

_source line 24 · 2026-05-19T14:45:41.468Z_

<details open><summary>🔧 Tool call — Grep · `toolu_0149Y8mc4EbtdnL4doFDWyBu`</summary>

```json
{
  "pattern": "\\\\begin\\{equation\\}|Eq\\.|equation.*gat|g_l|ThreadGate",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts",
  "output_mode": "content",
  "head_limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0827f430-30bf-44a9-83ae-701676f97292",
  "isSidechain": true,
  "agentId": "a15415a71738e1c47",
  "requestId": "req_011CbC7DDFWdGJcsZbrpELvH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8c08c63e-fc1f-4091-8fc2-a8dc12a4400c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UCDvdq9ubnEKM51sbaojts",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9159,
      "cache_read_input_tokens": 42003,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9159
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 178,
          "cache_read_input_tokens": 42003,
          "cache_creation_input_tokens": 9159,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9159,
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

_source line 25 · 2026-05-19T14:45:41.502Z_

<details><summary>↩ Tool result · `toolu_0149Y8mc4EbtdnL4doFDWyBu`</summary>

```text
&lt;persisted-output>
Output too large (22.2KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating--claude-sessions-reviewer-e7517921/4dc22f0d-9e49-4829-bdc9-e4845bf46c39/tool-results/toolu_0149Y8mc4EbtdnL4doFDWyBu.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/llama3_cross_model_plan.md:3:> 目标：在 Llama-3.1-8B-Instruct 上复现 Qwen2.5-7B 的三个 negative findings（NF1/NF2/NF3），证明 ThreadGate 的失败是结构性问题而非 Qwen 特有。这是 Route B negative result paper 从 Findings 升级 main track 的关键加分项。
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/llama3_cross_model_plan.md:29:## Phase 2: ThreadGate v7 训练
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/llama3_cross_model_plan.md:31:**目标**: 在 Llama 上训练 ThreadGate，复现三个 negative findings。
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/llama3_cross_model_plan.md:67:  --output_dir artifacts/phase2_tg_llama_v7
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/llama3_cross_model_plan.md:84:仅做 Base vs ThreadGate 对比：
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/llama3_cross_model_plan.md:93:# ThreadGate eval
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/llama3_cross_model_plan.md:97:  --checkpoint artifacts/phase2_tg_llama_v7/best.pt \
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/llama3_cross_model_plan.md:111:| ThreadGate (TG) | 0（Phase 2 已训练） | ~15min |
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/llama3_cross_model_plan.md:151:- `artifacts/phase2_tg_s42_v7/` — Qwen ThreadGate 训练 checkpoint
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/llama3_cross_model_plan.md:166:| D+1 ~ D+2 | Phase 2: ThreadGate v7 训练 | ~6-7h | Phase 1 完成 |
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/llama3_cross_model_plan.md:189:- **Claim 升级**: "ThreadGate's failure is structural, not model-specific" — 从单模型观察升级为跨架构结论
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c08c63e-fc1f-4091-8fc2-a8dc12a4400c",
  "isSidechain": true,
  "promptId": "a15e1f25-f380-4a76-9d77-88873bcc9e37",
  "agentId": "a15415a71738e1c47",
  "type": "user",
  "uuid": "a466ba40-1685-47a5-bb42-36429075432a",
  "sourceToolAssistantUUID": "8c08c63e-fc1f-4091-8fc2-a8dc12a4400c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-19T14:45:50.443Z_

Perfect! I have comprehensive information. Let me compile my findings.

## Summary of Paper Draft Files Found

I've located **three LaTeX paper drafts** for the turn_residual_gating project, all generated from recent dream report outputs:

### **File Paths:**

1. **Best version:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.tex`

2. **Median version:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/median/paper.tex`

3. **Worst version:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.tex`

4. **Markdown draft:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/artifacts/paper/method_section_draft.md`

---

### **Gating Equation Definitions Found:**

All versions contain the **ThreadGate gating mechanism** equations. The core gating formula appears consistently:

**In the method sections, Equation 3 (and equivalently numbered equations in variants) defines:**

```
x_{l+1} = g_l · x_l + f_l(x_l)
```

Where:
- `g_l ∈ (0, 1)` is the learnable scalar gate at layer `l`
- `f_l()` is the transformer layer output (attention + FFN)
- `g_l = σ(w_l)` with sigmoid parameterization

**The markdown draft (method_section_draft.md) contains a more elaborate gate network definition:**

```
g_l = σ(W_2 ReLU(W_1 [x_{l-1} W_down; e]) + b)
```

With turn-aware embeddings and down-projections, showing the full gating network architecture.

---

### **Key Findings Across Versions:**

1. **Best paper.tex** (most detailed): Contains comprehensive gradient analysis, demonstrates 30-35× training-inference GAR gap with extensive mechanistic explanation of failure modes

2. **Median paper.tex** (balanced): Reports ~22× training-inference gap, slightly different loss formulation emphasis

3. **Worst paper.tex** (minimalist): Reports 15× gap on held-out data, treats findings more conservatively with weaker correlations in downstream tasks

4. **Method markdown draft**: Contains the most technical detail on gate architecture including turn embedding modules and parameter initialization schemes

All documents contain the gating equation and extensive analysis of why the learned gates fail to transfer from training to inference despite successful training convergence.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a466ba40-1685-47a5-bb42-36429075432a",
  "isSidechain": true,
  "agentId": "a15415a71738e1c47",
  "requestId": "req_011CbC7Donu5FomsTNv3HjnA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "121b0dbd-6e27-42fb-98f9-57389831641c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "4dc22f0d-9e49-4829-bdc9-e4845bf46c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purrfect-percolating-plum",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ls4Fh4BbWezw6q1fx73RSv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1188,
      "cache_read_input_tokens": 51162,
      "output_tokens": 689,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1188
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 689,
          "cache_read_input_tokens": 51162,
          "cache_creation_input_tokens": 1188,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1188,
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
