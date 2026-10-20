# Research conversation: I need to understand the format of `literature_map.yaml` files used in the agent-ml-research system. Search for: 1. Any 

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a277383c324df4f8f.jsonl`
- **Structured JSON:** [`04f25b20772ba54e0cc8.json`](../../sessions/04/04f25b20772ba54e0cc8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

46 recorded events

### User

_source line 1 · 2026-05-20T13:52:55.928Z_

I need to understand the format of `literature_map.yaml` files used in the agent-ml-research system. Search for:
1. Any existing `literature_map.yaml` files in other projects under `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/`
2. Any code that reads/writes literature_map.yaml — search in `/home/ubuntu/agent-ml-research/` for "literature_map"
3. Any `add_to_literature_map` function definition

Report the file format (YAML structure) and how papers are represented (what fields: arxiv_id, s2_paper_id, title, etc). Be thorough — search "medium" breadth.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "233a5648-42dc-4022-8512-1e41829dae64",
  "agentId": "a277383c324df4f8f",
  "type": "user",
  "uuid": "bbdacbfa-7c1b-42a6-9ed8-f2f263d0eb6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-20T13:52:57.940Z_

I'll help you understand the format of `literature_map.yaml` files. Let me search for existing files, code that handles them, and relevant function definitions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbdacbfa-7c1b-42a6-9ed8-f2f263d0eb6d",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw1Nj2ybRDHLn4VwfUM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f08cccdb-983c-457a-b6b8-61ca95fafd47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Tdm6kU7W1dxTPH8aaVmPfc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39689,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39689,
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

_source line 3 · 2026-05-20T13:52:58.096Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01W1T5HQfsButZhiisX2LBRy`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects -name \"literature_map.yaml\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f08cccdb-983c-457a-b6b8-61ca95fafd47",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw1Nj2ybRDHLn4VwfUM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f0a9011d-0ac9-43b7-a8fc-4b905c26c89c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Tdm6kU7W1dxTPH8aaVmPfc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39689,
      "cache_read_input_tokens": 0,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 39689
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 118,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 39689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 39689,
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

_source line 4 · 2026-05-20T13:52:58.217Z_

<details><summary>↩ Tool result · `toolu_01W1T5HQfsButZhiisX2LBRy`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0a9011d-0ac9-43b7-a8fc-4b905c26c89c",
  "isSidechain": true,
  "promptId": "233a5648-42dc-4022-8512-1e41829dae64",
  "agentId": "a277383c324df4f8f",
  "type": "user",
  "uuid": "5ccf0865-8d46-4baa-9ffe-03a7f0c87368",
  "sourceToolAssistantUUID": "f0a9011d-0ac9-43b7-a8fc-4b905c26c89c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-20T13:52:59.399Z_

Let me search more broadly for literature_map files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ccf0865-8d46-4baa-9ffe-03a7f0c87368",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw1YVfB4Up34wEJDQuu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2df86318-416b-4273-82bf-0fbb1979fb38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QL5MXKHXnm34cWJgEFZBuY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 972,
      "cache_read_input_tokens": 39689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 972,
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

_source line 6 · 2026-05-20T13:52:59.654Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019NwsyBpLUkJz4FSjnz33LN`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects -name \"*literature*\" -type f 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2df86318-416b-4273-82bf-0fbb1979fb38",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw1YVfB4Up34wEJDQuu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f4ff9466-5770-471b-b27b-3a7be8fad2e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QL5MXKHXnm34cWJgEFZBuY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 972,
      "cache_read_input_tokens": 39689,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 972
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 102,
          "cache_read_input_tokens": 39689,
          "cache_creation_input_tokens": 972,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 972,
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

_source line 7 · 2026-05-20T13:52:59.709Z_

<details><summary>↩ Tool result · `toolu_019NwsyBpLUkJz4FSjnz33LN`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4ff9466-5770-471b-b27b-3a7be8fad2e1",
  "isSidechain": true,
  "promptId": "233a5648-42dc-4022-8512-1e41829dae64",
  "agentId": "a277383c324df4f8f",
  "type": "user",
  "uuid": "70f8f346-0801-4107-a617-9effdf30a219",
  "sourceToolAssistantUUID": "f4ff9466-5770-471b-b27b-3a7be8fad2e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-20T13:53:01.587Z_

Now let me search in the agent-ml-research directory for code that handles literature_map:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70f8f346-0801-4107-a617-9effdf30a219",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw1esPNokY72aiv2eDa",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d5733a92-f30c-4867-a6a1-8538cc5a9c88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JAhdezo9XNiTy5Mxe85RKA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 121,
      "cache_read_input_tokens": 40661,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 121,
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

_source line 9 · 2026-05-20T13:53:01.990Z_

<details open><summary>🔧 Tool call — Grep · `toolu_0157E4YxwE9coJAbBU5KNDqf`</summary>

```json
{
  "pattern": "literature_map",
  "path": "/home/ubuntu/agent-ml-research",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5733a92-f30c-4867-a6a1-8538cc5a9c88",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw1esPNokY72aiv2eDa",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0d40fa36-5192-41c8-b3f5-981d7d4563cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JAhdezo9XNiTy5Mxe85RKA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 121,
      "cache_read_input_tokens": 40661,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 121
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 124,
          "cache_read_input_tokens": 40661,
          "cache_creation_input_tokens": 121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 121,
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

_source line 10 · 2026-05-20T13:53:02.171Z_

<details><summary>↩ Tool result · `toolu_0157E4YxwE9coJAbBU5KNDqf`</summary>

```text
Found 39 files
/home/ubuntu/agent-ml-research/core/tools/distill.py
/home/ubuntu/agent-ml-research/tests/test_distill.py
/home/ubuntu/agent-ml-research/tests/test_progress_edge_cases.py
/home/ubuntu/agent-ml-research/tests/test_distill_progress.py
/home/ubuntu/agent-ml-research/docs/plans/system/PAPER_AUDIT_DISTILL_PROGRESS_CARD_PLAN.md
/home/ubuntu/agent-ml-research/prompts/roles/director.md
/home/ubuntu/agent-ml-research/core/mcp_server.py
/home/ubuntu/agent-ml-research/core/session_claude_md.py
/home/ubuntu/agent-ml-research/core/agents/message_router.py
/home/ubuntu/agent-ml-research/TEST.md
/home/ubuntu/agent-ml-research/PROGRESS.md
/home/ubuntu/agent-ml-research/skills/global/paper-visualization.skill.md
/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md
/home/ubuntu/agent-ml-research/skills/global/paper-plan.skill.md
/home/ubuntu/agent-ml-research/docs/plans/skill-system/PAPER_DISTILLATION_SKILL_PLAN.md
/home/ubuntu/agent-ml-research/core/tools/literature.py
/home/ubuntu/agent-ml-research/core/api/routers/manager_api.py
/home/ubuntu/agent-ml-research/tests/test_semantic_scholar.py
/home/ubuntu/agent-ml-research/tests/test_paper_agent_full_draft_e2e.py
/home/ubuntu/agent-ml-research/tests/test_paper_agent_patch_e2e.py
/home/ubuntu/agent-ml-research/tests/test_paper_agent_reframe_e2e.py
/home/ubuntu/agent-ml-research/tests/test_literature_gap_fill.py
/home/ubuntu/agent-ml-research/tests/test_literature_map.py
/home/ubuntu/agent-ml-research/skills/global/plan-next-experiment.skill.md
/home/ubuntu/agent-ml-research/skills/global/on-experiment-done.skill.md
/home/ubuntu/agent-ml-research/skills/global/competitor-experiment-reference.skill.md
/home/ubuntu/agent-ml-research/skills/global/literature-scan.skill.md
/home/ubuntu/agent-ml-research/prompts/roles/agent.md
/home/ubuntu/agent-ml-research/prompts/roles/paper-agent.md
/home/ubuntu/agent-ml-research/manager/api/distill_runs.py
/home/ubuntu/agent-ml-research/docs/plans/system/LITERATURE_REF+DISK_AWARENESS+HELP_DETAIL.md
/home/ubuntu/agent-ml-research/docs/plans/paper-writing/PAPER_WRITING_AGENT_PLAN.md
/home/ubuntu/agent-ml-research/docs/plans/paper-writing/PAPER_WRITING_NORMS_INTEGRATION_PLAN.md
/home/ubuntu/agent-ml-research/docs/plans/paper-writing/LITERATURE_SYSTEM_IMPROVEMENT_PLAN.md
/home/ubuntu/agent-ml-research/docs/plans/paper-writing/PAPER_SEARCH_INTEGRATION_PLAN.md
/home/ubuntu/agent-ml-research/core/tools/semantic_scholar.py
/home/ubuntu/agent-ml-research/core/tools/architecture.py
/home/ubuntu/agent-ml-research/core/paths.py
/home/ubuntu/agent-ml-research/core/cron_hooks.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d40fa36-5192-41c8-b3f5-981d7d4563cc",
  "isSidechain": true,
  "promptId": "233a5648-42dc-4022-8512-1e41829dae64",
  "agentId": "a277383c324df4f8f",
  "type": "user",
  "uuid": "d36c91e4-8c56-40f5-81fb-4df121387605",
  "sourceToolAssistantUUID": "0d40fa36-5192-41c8-b3f5-981d7d4563cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-20T13:53:03.542Z_

Good! Let me examine the key files. I'll start with the literature.py file and the test file to understand the format:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d36c91e4-8c56-40f5-81fb-4df121387605",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw1qKgncvjC9m3FWUoz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5dc6fa8a-4700-4c19-bb33-6c5c3dd286aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Y47zkkZp9FEiabkEJ88uk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1088,
      "cache_read_input_tokens": 40782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1088,
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

_source line 12 · 2026-05-20T13:53:03.730Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RkHBTyETEgzDnx5SFa2UcL`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/tools/literature.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5dc6fa8a-4700-4c19-bb33-6c5c3dd286aa",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw1qKgncvjC9m3FWUoz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "41c71c30-6d39-44cb-8db2-040dbb66ac02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Y47zkkZp9FEiabkEJ88uk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1088,
      "cache_read_input_tokens": 40782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1088,
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

_source line 13 · 2026-05-20T13:53:03.739Z_

<details><summary>↩ Tool result · `toolu_01RkHBTyETEgzDnx5SFa2UcL`</summary>

```text
1	"""Literature map — persistent, cross-stage knowledge base of papers.
2	
3	The literature_map.yaml is the single source of truth for papers a project
4	accumulates across the Idea → Research → Writing → Review pipeline. Each
5	entry is verified (or marked unverified) and carries enough metadata to
6	generate BibTeX entries and to drive Related Work / citation gap-fill in
7	the Paper Agent's writing pipeline.
8	
9	Two scopes:
10	
11	  - Project-level: ``projects/{project}/literature_map.yaml``
12	      Used during Research and Writing phases.
13	
14	  - Global (Idea phase): ``{WORKSPACE_ROOT}/literature_map.yaml``
15	      Used before a project exists. Each entry carries ``source_idea_id`` so
16	      multiple ideas can coexist. On project creation, matching entries are
17	      seeded into the project map.
18	
19	Design notes:
20	
21	  - Read paths support modes (summary / category:X / competitors / unverified
22	    / bib / full) so day-to-day reads stay token-cheap even when the map has
23	    grown to 40-60 papers.
24	
25	  - Writes hold an exclusive flock + use atomic temp→rename, modeled on
26	    ``core/tools/registry.py`` so the file never tears under concurrent
27	    Worker writes.
28	
29	  - Dedup happens on add: DOI exact match wins; otherwise normalized title
30	    match. Existing entries are merged (new fields fill empty existing
31	    fields) rather than overwritten.
32	"""
33	
34	from __future__ import annotations
35	
36	import fcntl
37	import logging
38	import os
39	import re
40	import tempfile
41	import unicodedata
42	from pathlib import Path
43	from typing import Any, Iterable
44	
45	import yaml
46	
47	from core import paths as _paths
48	from core.tools.result import ToolResult
49	
50	logger = logging.getLogger(__name__)
51	
52	
53	# ---------------------------------------------------------------------------
54	# Constants
55	# ---------------------------------------------------------------------------
56	
57	# Roles a paper can play relative to the project. Used by Related Work drafting
58	# (foundation papers anchor narratives; direct-competitor papers must be cited).
59	VALID_ROLES: frozenset[str] = frozenset(
60	    {"foundation", "direct-competitor", "method-component", "evaluation", "background"}
61	)
62	
63	# Modes for read_literature_map — keep token usage proportional to need.
64	VALID_READ_MODES: frozenset[str] = frozenset(
65	    {"summary", "competitors", "unverified", "bib", "full"}
66	)
67	
68	# Fields kept in summary mode (skips long fields like abstract, relevance).
69	_SUMMARY_FIELDS: tuple[str, ...] = (
70	    "title", "year", "venue", "category", "role", "verified", "bibtex_key",
71	)
72	
73	
74	# ---------------------------------------------------------------------------
75	# Path resolution
76	# ---------------------------------------------------------------------------
77	
78	def get_literature_map_path(project: str | None = None) -> Path:
79	    """Resolve the literature_map.yaml path.
80	
81	    Project name → ``projects/{project}/literature_map.yaml`` (V3 layout).
82	    No project   → ``{WORKSPACE_ROOT}/literature_map.yaml`` (global, idea phase).
83	    """
84	    if project:
85	        p = _paths.resolve_project_file(project, "literature_map.yaml")
86	        p.parent.mkdir(parents=True, exist_ok=True)
87	        return p
88	    return _paths.global_literature_map_path()
89	
90	
91	# ---------------------------------------------------------------------------
92	# Atomic file I/O — modeled on registry._read_modify_write_registry
93	# ---------------------------------------------------------------------------
94	
95	def _empty_map() -> dict:
96	    return {
97	        "meta": {"last_updated": None, "total_papers": 0},
98	        "categories": [],
99	        "papers": {},
100	    }
101	
102	
103	def _read_map(path: Path) -> dict:
104	    """Read literature_map.yaml without a lock (atomic single-syscall read).
105	
106	    Returns a fresh empty skeleton if the file doesn't exist or is unreadable.
107	    Writers use exclusive flock + atomic rename so readers always see a
108	    consistent snapshot.
109	    """
110	    if not path.exists():
111	        return _empty_map()
112	    try:
113	        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
114	    except Exception:
115	        logger.warning("Failed to parse literature_map at %s", path, exc_info=True)
116	        return _empty_map()
117	    if isinstance(data, list):
118	        data = {"papers": data, "meta": {}, "categories": []}
119	    elif not isinstance(data, dict):
120	        logger.warning("literature_map at %s is %s, expected dict — resetting", path, type(data).__name__)
121	        return _empty_map()
122	    data.setdefault("meta", {})
123	    data["meta"].setdefault("last_updated", None)
124	    data["meta"].setdefault("total_papers", 0)
125	    data.setdefault("categories", [])
126	    data.setdefault("papers", {})
127	    return data
128	
129	
130	def _read_modify_write(path: Path, modifier) -> dict:
131	    """Read, apply ``modifier(data)`` in place, atomically write back.
132	
133	    Holds LOCK_EX on a sibling .lock file (not the data file — atomic rename
134	    swaps the inode and would invalidate locks held on it).
135	    """
136	    path.parent.mkdir(parents=True, exist_ok=True)
137	    lock_path = path.with_suffix(".lock")
138	
139	    with open(lock_path, "a+") as lock_f:
140	        fcntl.flock(lock_f, fcntl.LOCK_EX)
141	        try:
142	            data = _read_map(path)
143	            modifier(data)
144	            data["meta"]["total_papers"] = len(data.get("papers", {}))
145	            data["meta"]["last_updated"] = _paths.now_iso()
146	
147	            fd, tmp_path = tempfile.mkstemp(
148	                dir=str(path.parent), prefix=".literature_", suffix=".tmp"
149	            )
150	            try:
151	                with os.fdopen(fd, "w", encoding="utf-8") as tmp_f:
152	                    yaml.dump(
153	                        data, tmp_f,
154	                        default_flow_style=False, allow_unicode=True, sort_keys=False,
155	                    )
156	                    tmp_f.flush()
157	                    os.fsync(tmp_f.fileno())
158	                os.replace(tmp_path, str(path))
159	            except Exception:
160	                if os.path.exists(tmp_path):
161	                    os.unlink(tmp_path)
162	                raise
163	        finally:
164	            fcntl.flock(lock_f, fcntl.LOCK_UN)
165	
166	    return data
167	
168	
169	# ---------------------------------------------------------------------------
170	# Normalization & dedup
171	# ---------------------------------------------------------------------------
172	
173	_PUNCT_RE = re.compile(r"[^\w\s]")
174	_WS_RE = re.compile(r"\s+")
175	
176	
177	def _normalize_title(title: str) -> str:
178	    """Lowercase, strip diacritics + punctuation, collapse whitespace.
179	
180	    Used for fuzzy dedup when two records describe the same paper with
181	    slightly different titles (smart quotes, hyphens, capitalization).
182	    """
183	    if not title:
184	        return ""
185	    s = unicodedata.normalize("NFKD", title)
186	    s = "".join(c for c in s if not unicodedata.combining(c))
187	    s = s.lower()
188	    s = _PUNCT_RE.sub(" ", s)
189	    s = _WS_RE.sub(" ", s).strip()
190	    return s
191	
192	
193	def _normalize_doi(doi: str) -> str:
194	    """Lowercase DOI, strip common prefixes."""
195	    if not doi:
196	        return ""
197	    s = doi.strip().lower()
198	    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
199	        if s.startswith(prefix):
200	            s = s[len(prefix):]
201	            break
202	    return s.strip()
203	
204	
205	def _slugify(s: str, max_len: int = 24) -> str:
206	    """First-word slug — lowercase, alnum only, truncated."""
207	    s = unicodedata.normalize("NFKD", s or "")
208	    s = "".join(c for c in s if not unicodedata.combining(c))
209	    s = re.sub(r"[^a-zA-Z0-9]+", "", s.split()[0] if s.split() else "")
210	    return s.lower()[:max_len]
211	
212	
213	def _generate_bibtex_key(paper: dict) -> str:
214	    """Generate a bibtex key like ``vaswani2017attention``.
215	
216	    Uses the first author's surname + year + the first significant word of
217	    the title. Falls back to ``paper_{hash}`` if metadata is missing.
218	    """
219	    authors = paper.get("authors") or []
220	    first_author = ""
221	    if authors:
222	        raw = authors[0]
223	        if isinstance(raw, str):
224	            # Could be "Vaswani, A." or "Ashish Vaswani"
225	            if "," in raw:
226	                first_author = raw.split(",", 1)[0].strip()
227	            else:
228	                first_author = raw.strip().split()[-1] if raw.strip() else ""
229	    surname = _slugify(first_author)
230	
231	    year = paper.get("year") or ""
232	    year_part = str(year) if year else ""
233	
234	    title = paper.get("title") or ""
235	    # Skip stop words for the title slug
236	    stop = {"a", "an", "the", "on", "in", "of", "for", "and", "or", "is", "to"}
237	    words = [w for w in re.split(r"\W+", title.lower()) if w and w not in stop]
238	    word = _slugify(words[0]) if words else ""
239	
240	    key = f"{surname}{year_part}{word}"
241	    if not key.strip():
242	        import hashlib
243	        h = hashlib.md5(title.encode("utf-8")).hexdigest()[:8]
244	        key = f"paper_{h}"
245	    return key
246	
247	
248	def _find_existing_key(papers: dict, candidate: dict) -> str | None:
249	    """Find a matching paper key in ``papers`` for the candidate dict.
250	
251	    Match order: DOI exact (normalized) → normalized title.
252	    Returns the existing key or None.
253	
254	    bibtex_key collisions are NOT treated as dedup signal — two different
255	    papers can share a naive bibtex_key (e.g. same first author + year), and
256	    we handle that with a suffix at insert time. Real dedup must be content
257	    based.
258	    """
259	    cand_doi = _normalize_doi(candidate.get("doi", ""))
260	    cand_title = _normalize_title(candidate.get("title", ""))
261	
262	    for key, entry in papers.items():
263	        if cand_doi:
264	            entry_doi = _normalize_doi(entry.get("doi", ""))
265	            if entry_doi and entry_doi == cand_doi:
266	                return key
267	        if cand_title:
268	            entry_title = _normalize_title(entry.get("title", ""))
269	            if entry_title and entry_title == cand_title:
270	                return key
271	    return None
272	
273	
274	def _merge_paper(existing: dict, new: dict) -> dict:
275	    """Merge new fields into existing — only fill empty slots, never overwrite.
276	
277	    Verified=True wins over False (a later verification cannot un-verify).
278	    """
279	    merged = dict(existing)
280	    for k, v in new.items():
281	        if v is None or v == "" or v == []:
282	            continue
283	        if k == "verified":
284	            merged["verified"] = bool(existing.get("verified")) or bool(v)
285	            continue
286	        if not merged.get(k):
287	            merged[k] = v
288	    return merged
289	
290	
291	# ---------------------------------------------------------------------------
292	# Public API
293	# ---------------------------------------------------------------------------
294	
295	def read_literature_map(
296	    project: str | None = None,
297	    mode: str = "summary",
298	) -> ToolResult:
299	    """Read the literature map with mode-controlled verbosity.
300	
301	    Args:
302	        project: Project name — None reads the global (idea-phase) map.
303	        mode:
304	          - "summary"        → categories + per-paper {title, year, venue,
305	                                category, role, verified, bibtex_key}
306	          - "category:&lt;key>" → full entries in the named category
307	          - "competitors"    → full entries with role=direct-competitor
308	          - "unverified"     → full entries with verified=False
309	          - "bib"            → list of bibtex_key strings (for citation lookups)
310	          - "full"           → everything (use sparingly — token-heavy)
311	
312	    Returns:
313	        ToolResult.data = {
314	            "categories": [...],
315	            "papers": {key: {...}, ...},
316	            "meta": {"last_updated", "total_papers"},
317	            "mode": &lt;effective mode>,
318	        }
319	    """
320	    path = get_literature_map_path(project)
321	    data = _read_map(path)
322	    papers: dict = data.get("papers", {})
323	    categories: list = data.get("categories", [])
324	
325	    # Category-scoped read: "category:&lt;key>"
326	    if mode.startswith("category:"):
327	        cat_key = mode.split(":", 1)[1].strip()
328	        filtered = {k: v for k, v in papers.items() if v.get("category") == cat_key}
329	        return ToolResult(success=True, data={
330	            "categories": [c for c in categories if c.get("key") == cat_key],
331	            "papers": filtered,
332	            "meta": data.get("meta", {}),
333	            "mode": mode,
334	        })
335	
336	    if mode not in VALID_READ_MODES:
337	        return ToolResult(
338	            success=False,
339	            error=(
340	                f"Unknown mode '{mode}'. Valid: {sorted(VALID_READ_MODES)} "
341	                "or 'category:&lt;key>'."
342	            ),
343	        )
344	
345	    if mode == "summary":
346	        compact = {
347	            k: {f: v.get(f) for f in _SUMMARY_FIELDS if f in v}
348	            for k, v in papers.items()
349	        }
350	        return ToolResult(success=True, data={
351	            "categories": categories,
352	            "papers": compact,
353	            "meta": data.get("meta", {}),
354	            "mode": mode,
355	        })
356	
357	    if mode == "competitors":
358	        filtered = {k: v for k, v in papers.items() if v.get("role") == "direct-competitor"}
359	        return ToolResult(success=True, data={
360	            "categories": categories,
361	            "papers": filtered,
362	            "meta": data.get("meta", {}),
363	            "mode": mode,
364	        })
365	
366	    if mode == "unverified":
367	        filtered = {k: v for k, v in papers.items() if not v.get("verified")}
368	        return ToolResult(success=True, data={
369	            "categories": categories,
370	            "papers": filtered,
371	            "meta": data.get("meta", {}),
372	            "mode": mode,
373	        })
374	
375	    if mode == "bib":
376	        keys = [v.get("bibtex_key") or k for k, v in papers.items()]
377	        return ToolResult(success=True, data={
378	            "bibtex_keys": keys,
379	            "meta": data.get("meta", {}),
380	            "mode": mode,
381	        })
382	
383	    # mode == "full"
384	    return ToolResult(success=True, data={
385	        "categories": categories,
386	        "papers": papers,
387	        "meta": data.get("meta", {}),
388	        "mode": mode,
389	    })
390	
391	
392	def add_to_literature_map(
393	    project: str | None = None,
394	    papers: Iterable[dict] | None = None,
395	    added_by: str = "",
396	) -> ToolResult:
397	    """Add (or merge) one or more papers into the literature map.
398	
399	    Dedup: DOI exact (normalized) → normalized title → bibtex_key collision.
400	    Existing entries are merged field-by-field, never overwritten.
401	
402	    Args:
403	        project: Project name — None writes to the global (idea-phase) map.
404	        papers: Iterable of paper dicts. Recognized fields:
405	                title, authors (list[str]), year, venue, url, doi,
406	                bibtex_key, category, role, relevance, abstract,
407	                semantic_scholar_id, source_idea_id, verified.
408	                Missing bibtex_key is auto-generated.
409	        added_by: Free-form tag for provenance ("paper-research",
410	                  "idea-generator", "user", etc.). Recorded on new entries.
411	
412	    Returns:
413	        ToolResult.data = {
414	            "added": [keys],            # newly inserted
415	            "merged": [keys],           # matched existing, fields merged
416	            "rejected": [{title, reason}],
417	            "total_papers": N,
418	        }
419	    """
420	    if not papers:
421	        return ToolResult(
422	            success=False, error="No papers provided.",
423	        )
424	
425	    paper_list = list(papers)
426	    added: list[str] = []
427	    merged: list[str] = []
428	    rejected: list[dict] = []
429	    now = _paths.now_iso()
430	
431	    def _apply(data: dict) -> None:
432	        existing = data.setdefault("papers", {})
433	        for cand in paper_list:
434	            if not isinstance(cand, dict):
435	                rejected.append({"title": str(cand), "reason": "not a dict"})
436	                continue
437	            title = (cand.get("title") or "").strip()
438	            if not title:
439	                rejected.append({"title": "", "reason": "missing title"})
440	                continue
441	            if cand.get("role") and cand["role"] not in VALID_ROLES:
442	                rejected.append({
443	                    "title": title,
444	                    "reason": f"invalid role '{cand['role']}', valid: {sorted(VALID_ROLES)}",
445	                })
446	                continue
447	
448	            existing_key = _find_existing_key(existing, cand)
449	            if existing_key:
450	                # Merge — fill empty fields, keep verified=True if either is True
451	                existing[existing_key] = _merge_paper(existing[existing_key], cand)
452	                merged.append(existing_key)
453	                continue
454	
455	            # New entry — assign a bibtex_key if missing, dedupe within file
456	            key = cand.get("bibtex_key") or _generate_bibtex_key(cand)
457	            base_key = key
458	            suffix = 1
459	            while key in existing:
460	                suffix += 1
461	                key = f"{base_key}_{suffix}"
462	
463	            entry = {
464	                "title": title,
465	                "authors": cand.get("authors") or [],
466	                "year": cand.get("year"),
467	                "venue": cand.get("venue") or "",
468	                "url": cand.get("url") or "",
469	                "doi": cand.get("doi") or "",
470	                "bibtex_key": key,
471	                "category": cand.get("category") or "",
472	                "role": cand.get("role") or "",
473	                "relevance": cand.get("relevance") or "",
474	                "abstract": cand.get("abstract") or "",
475	                "semantic_scholar_id": cand.get("semantic_scholar_id") or "",
476	                "verified": bool(cand.get("verified", False)),
477	                "added_by": cand.get("added_by") or added_by or "",
478	                "added_at": cand.get("added_at") or now,
479	            }
480	            # Optional source_idea_id (global map only) — keep if present
481	            if cand.get("source_idea_id"):
482	                entry["source_idea_id"] = cand["source_idea_id"]
483	
484	            existing[key] = entry
485	            added.append(key)
486	
487	    data = _read_modify_write(get_literature_map_path(project), _apply)
488	
489	    return ToolResult(success=True, data={
490	        "added": added,
491	        "merged": merged,
492	        "rejected": rejected,
493	        "total_papers": data["meta"]["total_papers"],
494	    })
495	
496	
497	def update_literature_category(
498	    paper_key: str,
499	    project: str | None = None,
500	    category: str | None = None,
501	    role: str | None = None,
502	    relevance: str | None = None,
503	    verified: bool | None = None,
504	) -> ToolResult:
505	    """Update a single paper's classification fields.
506	
507	    Only the fields you pass are changed — others are left intact. This is
508	    the preferred path for "re-classify this paper after reading it" or
509	    "mark verified=true after OpenAlex check" — it's smaller than rewriting
510	    the whole entry via add_to_literature_map.
511	
512	    Args:
513	        paper_key: The YAML key of the paper (e.g. "vaswani2017attention").
514	        project: Project name — None updates the global map.
515	        category: New category key (must match a categories[].key, or empty).
516	        role: New role (must be in VALID_ROLES, or empty to clear).
517	        relevance: One-line relevance description.
518	        verified: Mark verified/unverified (e.g. after OpenAlex check).
519	
520	    Returns:
521	        ToolResult.data = {"paper_key", "updated_fields": {...}}
522	        ToolResult.error if paper_key not found or role/category invalid.
523	    """
524	    if role is not None and role and role not in VALID_ROLES:
525	        return ToolResult(
526	            success=False,
527	            error=f"invalid role '{role}', valid: {sorted(VALID_ROLES)}",
528	        )
529	
530	    updated: dict[str, Any] = {}
531	    not_found = {"miss": False}
532	
533	    def _apply(data: dict) -> None:
534	        papers = data.setdefault("papers", {})
535	        if paper_key not in papers:
536	            not_found["miss"] = True
537	            return
538	        entry = papers[paper_key]
539	        if category is not None:
540	            entry["category"] = category
541	            updated["category"] = category
542	        if role is not None:
543	            entry["role"] = role
544	            updated["role"] = role
545	        if relevance is not None:
546	            entry["relevance"] = relevance
547	            updated["relevance"] = relevance
548	        if verified is not None:
549	            entry["verified"] = bool(verified)
550	            updated["verified"] = bool(verified)
551	
552	    _read_modify_write(get_literature_map_path(project), _apply)
553	
554	    if not_found["miss"]:
555	        return ToolResult(
556	            success=False,
557	            error=f"paper_key '{paper_key}' not found in literature_map",
558	        )
559	    return ToolResult(success=True, data={
560	        "paper_key": paper_key,
561	        "updated_fields": updated,
562	    })
563	
564	
565	def upsert_category(
566	    project: str | None = None,
567	    key: str = "",
568	    name: str = "",
569	    narrative: str = "",
570	) -> ToolResult:
571	    """Add or update a category entry in the categories[] list.
572	
573	    Categories define the Related Work subsection structure. A paper's
574	    ``category`` field references one of these by ``key``.
575	
576	    Args:
577	        project: Project name — None edits the global map.
578	        key: Category slug (e.g. "attention_mechanisms"). Required.
579	        name: Human-readable name (e.g. "Attention Mechanisms"). Required for new.
580	        narrative: One-line description of the category's narrative arc.
581	
582	    Returns:
583	        ToolResult.data = {"key", "action": "added"|"updated"}.
584	    """
585	    if not key:
586	        return ToolResult(success=False, error="key is required")
587	
588	    state = {"action": "added"}
589	
590	    def _apply(data: dict) -> None:
591	        cats = data.setdefault("categories", [])
592	        for c in cats:
593	            if c.get("key") == key:
594	                if name:
595	                    c["name"] = name
596	                if narrative:
597	                    c["narrative"] = narrative
598	                state["action"] = "updated"
599	                return
600	        cats.append({"key": key, "name": name or key, "narrative": narrative})
601	
602	    _read_modify_write(get_literature_map_path(project), _apply)
603	    return ToolResult(success=True, data={"key": key, "action": state["action"]})
604	
605	
606	def seed_literature_map(
607	    project: str,
608	    seed_papers: Iterable[dict],
609	    source_idea_id: str = "",
610	) -> ToolResult:
611	    """Bulk-seed a new project's literature_map from an idea's accumulated papers.
612	
613	    Called by the idea→project bootstrap hook. Each seed paper is added with
614	    ``added_by="idea_generator"`` so downstream consumers can distinguish
615	    seed papers from those discovered during research.
616	
617	    Args:
618	        project: Project name (required — seeding without a project is the
619	                 global map case, handled by add_to_literature_map directly).
620	        seed_papers: Iterable of paper dicts (same schema as add_to_literature_map).
621	        source_idea_id: Idea ID these papers came from. Stamped on entries so
622	                        a future "re-seed from idea" can find them.
623	
624	    Returns:
625	        Same shape as add_to_literature_map.
626	    """
627	    if not project:
628	        return ToolResult(success=False, error="project is required for seed_literature_map")
629	
630	    seeds = []
631	    for p in seed_papers:
632	        if not isinstance(p, dict):
633	            continue
634	        p2 = dict(p)
635	        if source_idea_id:
636	            p2.setdefault("source_idea_id", source_idea_id)
637	        seeds.append(p2)
638	
639	    return add_to_literature_map(
640	        project=project, papers=seeds, added_by="idea_generator",
641	    )
642	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41c71c30-6d39-44cb-8db2-040dbb66ac02",
  "isSidechain": true,
  "promptId": "233a5648-42dc-4022-8512-1e41829dae64",
  "agentId": "a277383c324df4f8f",
  "type": "user",
  "uuid": "09240a96-d090-4624-862e-65b33373b7fc",
  "sourceToolAssistantUUID": "41c71c30-6d39-44cb-8db2-040dbb66ac02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T13:53:04.205Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BM6gTzSEtEe9wjd5DNxzH3`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/tests/test_literature_map.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09240a96-d090-4624-862e-65b33373b7fc",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw1qKgncvjC9m3FWUoz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e00403ec-7c73-4c58-98c1-4493beaa0200",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Y47zkkZp9FEiabkEJ88uk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1088,
      "cache_read_input_tokens": 40782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1088,
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

_source line 15 · 2026-05-20T13:53:04.213Z_

<details><summary>↩ Tool result · `toolu_01BM6gTzSEtEe9wjd5DNxzH3`</summary>

```text
1	"""Unit tests for core/tools/literature.py.
2	
3	Covers CRUD, dedup (DOI / title), cross-stage persistence (global → project seed),
4	and the read-mode taxonomy (summary / category / competitors / unverified / bib / full).
5	"""
6	
7	from __future__ import annotations
8	
9	import yaml
10	
11	import pytest
12	
13	from core import paths
14	from core.tools.literature import (
15	    VALID_READ_MODES,
16	    VALID_ROLES,
17	    _find_existing_key,
18	    _generate_bibtex_key,
19	    _merge_paper,
20	    _normalize_doi,
21	    _normalize_title,
22	    add_to_literature_map,
23	    get_literature_map_path,
24	    read_literature_map,
25	    seed_literature_map,
26	    update_literature_category,
27	    upsert_category,
28	)
29	
30	
31	# ---------------------------------------------------------------------------
32	# Sample papers
33	# ---------------------------------------------------------------------------
34	
35	VASWANI = {
36	    "title": "Attention Is All You Need",
37	    "authors": ["Vaswani, A.", "Shazeer, N."],
38	    "year": 2017,
39	    "venue": "NeurIPS",
40	    "doi": "10.5555/3295222.3295349",
41	    "category": "attention",
42	    "role": "foundation",
43	    "abstract": "We propose a new simple network architecture, the Transformer.",
44	    "verified": True,
45	}
46	
47	BERT = {
48	    "title": "BERT: Pre-training of Deep Bidirectional Transformers",
49	    "authors": ["Devlin, J."],
50	    "year": 2018,
51	    "venue": "NAACL",
52	    "doi": "10.18653/v1/N19-1423",
53	    "category": "pretraining",
54	    "role": "direct-competitor",
55	    "verified": False,
56	}
57	
58	GPT3 = {
59	    "title": "Language Models are Few-Shot Learners",
60	    "authors": ["Brown, T."],
61	    "year": 2020,
62	    "venue": "NeurIPS",
63	    "doi": "",  # no doi available — title dedup path
64	    "category": "pretraining",
65	    "role": "background",
66	}
67	
68	
69	# ---------------------------------------------------------------------------
70	# Path resolution
71	# ---------------------------------------------------------------------------
72	
73	class TestPathResolution:
74	    def test_global_path_no_project(self, workspace):
75	        p = get_literature_map_path()
76	        assert p == paths.global_literature_map_path()
77	
78	    def test_project_path(self, workspace):
79	        p = get_literature_map_path("foo_proj")
80	        # V3 layout: project root, not under agent/
81	        assert p.name == "literature_map.yaml"
82	        assert "foo_proj" in str(p)
83	        assert p.parent.is_dir()  # auto-created
84	
85	
86	# ---------------------------------------------------------------------------
87	# Normalization helpers
88	# ---------------------------------------------------------------------------
89	
90	class TestNormalization:
91	    def test_normalize_title_lowercase_strip_punct(self):
92	        a = _normalize_title("Attention Is All You Need!")
93	        b = _normalize_title("attention is all you need")
94	        assert a == b
95	
96	    def test_normalize_title_strips_diacritics(self):
97	        assert _normalize_title("Résumé") == _normalize_title("Resume")
98	
99	    def test_normalize_title_smart_quotes_and_dashes(self):
100	        a = _normalize_title("Self-Attention’s Power")
101	        b = _normalize_title("self attention s power")
102	        assert a == b
103	
104	    def test_normalize_title_empty(self):
105	        assert _normalize_title("") == ""
106	        assert _normalize_title(None) == ""  # type: ignore[arg-type]
107	
108	    def test_normalize_doi_lowercases_strip_prefix(self):
109	        assert _normalize_doi("https://doi.org/10.1/AbC") == "10.1/abc"
110	        assert _normalize_doi("DOI:10.1/X") == "10.1/x"
111	        assert _normalize_doi("10.1/x") == "10.1/x"
112	        assert _normalize_doi("") == ""
113	
114	
115	# ---------------------------------------------------------------------------
116	# Bibtex key generation
117	# ---------------------------------------------------------------------------
118	
119	class TestBibtexKey:
120	    def test_first_author_year_word(self):
121	        key = _generate_bibtex_key(VASWANI)
122	        assert key == "vaswani2017attention"
123	
124	    def test_skips_stopwords_in_title(self):
125	        # "The Power of X" — first significant word should be "power"
126	        key = _generate_bibtex_key({
127	            "authors": ["Smith, J."],
128	            "year": 2024,
129	            "title": "The Power of Scale",
130	        })
131	        assert key == "smith2024power"
132	
133	    def test_handles_firstname_lastname_format(self):
134	        key = _generate_bibtex_key({
135	            "authors": ["Ashish Vaswani"],
136	            "year": 2017,
137	            "title": "Attention",
138	        })
139	        # Uses last word as surname when no comma
140	        assert key == "vaswani2017attention"
141	
142	    def test_fallback_when_metadata_missing(self):
143	        key = _generate_bibtex_key({"title": "Some Paper"})
144	        # No authors / year → must still produce something stable
145	        assert key  # non-empty
146	        # Falls back to title slug
147	        assert "some" in key or key.startswith("paper_")
148	
149	
150	# ---------------------------------------------------------------------------
151	# Read modes
152	# ---------------------------------------------------------------------------
153	
154	class TestReadModes:
155	    def test_empty_map_returns_skeleton(self, workspace):
156	        r = read_literature_map(mode="summary")
157	        assert r.success
158	        assert r.data["papers"] == {}
159	        assert r.data["categories"] == []
160	        assert r.data["meta"]["total_papers"] == 0
161	
162	    def test_summary_strips_long_fields(self, workspace):
163	        add_to_literature_map(papers=[VASWANI])
164	        r = read_literature_map(mode="summary")
165	        assert r.success
166	        # summary mode drops abstract / relevance
167	        for p in r.data["papers"].values():
168	            assert "abstract" not in p
169	            assert "relevance" not in p
170	            assert "title" in p
171	            assert "verified" in p
172	
173	    def test_full_mode_returns_everything(self, workspace):
174	        add_to_literature_map(papers=[VASWANI])
175	        r = read_literature_map(mode="full")
176	        assert r.success
177	        entry = next(iter(r.data["papers"].values()))
178	        assert entry["abstract"]
179	        assert "added_at" in entry
180	
181	    def test_competitors_mode_filters_role(self, workspace):
182	        add_to_literature_map(papers=[VASWANI, BERT, GPT3])
183	        r = read_literature_map(mode="competitors")
184	        assert r.success
185	        for p in r.data["papers"].values():
186	            assert p["role"] == "direct-competitor"
187	        # BERT is the only direct-competitor
188	        assert len(r.data["papers"]) == 1
189	
190	    def test_unverified_mode_filters_unverified(self, workspace):
191	        add_to_literature_map(papers=[VASWANI, BERT, GPT3])
192	        r = read_literature_map(mode="unverified")
193	        assert r.success
194	        # VASWANI is verified — should NOT be in result
195	        for p in r.data["papers"].values():
196	            assert not p.get("verified")
197	        # BERT (verified=False) and GPT3 (default False)
198	        assert len(r.data["papers"]) == 2
199	
200	    def test_bib_mode_returns_keylist(self, workspace):
201	        add_to_literature_map(papers=[VASWANI, BERT])
202	        r = read_literature_map(mode="bib")
203	        assert r.success
204	        keys = r.data["bibtex_keys"]
205	        assert "vaswani2017attention" in keys
206	        assert any(k.startswith("devlin2018") for k in keys)
207	
208	    def test_category_scoped_read(self, workspace):
209	        add_to_literature_map(papers=[VASWANI, BERT, GPT3])
210	        upsert_category(key="pretraining", name="Pretraining")
211	        r = read_literature_map(mode="category:pretraining")
212	        assert r.success
213	        for p in r.data["papers"].values():
214	            assert p["category"] == "pretraining"
215	        assert len(r.data["papers"]) == 2  # BERT + GPT3
216	
217	    def test_unknown_mode_rejected(self, workspace):
218	        r = read_literature_map(mode="bogus")
219	        assert not r.success
220	        assert "Unknown mode" in r.error
221	
222	
223	# ---------------------------------------------------------------------------
224	# Add / dedup
225	# ---------------------------------------------------------------------------
226	
227	class TestAdd:
228	    def test_add_new_paper_creates_entry(self, workspace):
229	        r = add_to_literature_map(papers=[VASWANI], added_by="paper-research")
230	        assert r.success
231	        assert len(r.data["added"]) == 1
232	        assert r.data["total_papers"] == 1
233	
234	        # added_by + added_at recorded
235	        full = read_literature_map(mode="full").data["papers"]
236	        entry = next(iter(full.values()))
237	        assert entry["added_by"] == "paper-research"
238	        assert entry["added_at"]
239	
240	    def test_dedup_by_doi(self, workspace):
241	        add_to_literature_map(papers=[VASWANI])
242	        # Different title formatting but same DOI → must merge, not add
243	        dup = dict(VASWANI)
244	        dup["title"] = "ATTENTION IS ALL YOU NEED (with caps)"
245	        r = add_to_literature_map(papers=[dup])
246	        assert r.success
247	        assert len(r.data["added"]) == 0
248	        assert len(r.data["merged"]) == 1
249	        assert r.data["total_papers"] == 1
250	
251	    def test_dedup_by_normalized_title(self, workspace):
252	        # GPT3 has no DOI — fall back to title match
253	        add_to_literature_map(papers=[GPT3])
254	        dup = dict(GPT3)
255	        # Add weird punctuation
256	        dup["title"] = "language Models, ARE: Few-Shot Learners!!!"
257	        r = add_to_literature_map(papers=[dup])
258	        assert r.success
259	        assert len(r.data["merged"]) == 1
260	        assert r.data["total_papers"] == 1
261	
262	    def test_merge_fills_empty_fields_only(self, workspace):
263	        # First add with sparse data
264	        sparse = {"title": "Sparse Paper", "year": 2020}
265	        add_to_literature_map(papers=[sparse])
266	        # Then merge in fuller record (same title)
267	        rich = {
268	            "title": "Sparse Paper",
269	            "year": 2099,  # SHOULD NOT overwrite existing 2020
270	            "venue": "ICML",
271	            "authors": ["X, Y."],
272	        }
273	        add_to_literature_map(papers=[rich])
274	        entry = next(iter(read_literature_map(mode="full").data["papers"].values()))
275	        assert entry["year"] == 2020  # preserved
276	        assert entry["venue"] == "ICML"  # filled
277	        assert entry["authors"] == ["X, Y."]
278	
279	    def test_verified_true_wins(self, workspace):
280	        add_to_literature_map(papers=[{"title": "X", "verified": True}])
281	        add_to_literature_map(papers=[{"title": "X", "verified": False}])
282	        entry = next(iter(read_literature_map(mode="full").data["papers"].values()))
283	        assert entry["verified"] is True  # later False does NOT un-verify
284	
285	    def test_bibtex_key_collision_gets_suffix(self, workspace):
286	        # Two papers with same surname + year + first word — produces same key
287	        a = {"title": "Attention One", "authors": ["Vaswani, A."], "year": 2017}
288	        b = {"title": "Attention Two", "authors": ["Vaswani, B."], "year": 2017}
289	        add_to_literature_map(papers=[a])
290	        add_to_literature_map(papers=[b])
291	        full = read_literature_map(mode="full").data["papers"]
292	        keys = sorted(full.keys())
293	        assert "vaswani2017attention" in keys
294	        # Second one should have suffix appended
295	        assert any(k.startswith("vaswani2017attention_") for k in keys)
296	
297	    def test_invalid_role_rejected(self, workspace):
298	        bad = {"title": "Bad", "role": "not-a-real-role"}
299	        r = add_to_literature_map(papers=[bad])
300	        assert r.success  # call itself succeeds
301	        assert len(r.data["added"]) == 0
302	        assert len(r.data["rejected"]) == 1
303	        assert "invalid role" in r.data["rejected"][0]["reason"]
304	
305	    def test_missing_title_rejected(self, workspace):
306	        r = add_to_literature_map(papers=[{"year": 2024}])
307	        assert r.data["rejected"][0]["reason"] == "missing title"
308	
309	    def test_no_papers_error(self, workspace):
310	        r = add_to_literature_map(papers=[])
311	        assert not r.success
312	
313	    def test_non_dict_rejected(self, workspace):
314	        r = add_to_literature_map(papers=["not a dict"])  # type: ignore[list-item]
315	        assert r.data["rejected"][0]["reason"] == "not a dict"
316	
317	    def test_all_valid_roles_accepted(self, workspace):
318	        for role in VALID_ROLES:
319	            r = add_to_literature_map(papers=[{
320	                "title": f"Paper with {role}",
321	                "role": role,
322	            }])
323	            assert r.success
324	            assert len(r.data["added"]) == 1
325	
326	
327	# ---------------------------------------------------------------------------
328	# update_literature_category
329	# ---------------------------------------------------------------------------
330	
331	class TestUpdateCategory:
332	    def test_update_existing(self, workspace):
333	        add_to_literature_map(papers=[VASWANI])
334	        key = next(iter(read_literature_map(mode="full").data["papers"]))
335	        r = update_literature_category(
336	            paper_key=key, category="new_cat", role="background",
337	            relevance="seminal", verified=True,
338	        )
339	        assert r.success
340	        entry = read_literature_map(mode="full").data["papers"][key]
341	        assert entry["category"] == "new_cat"
342	        assert entry["role"] == "background"
343	        assert entry["relevance"] == "seminal"
344	        assert entry["verified"] is True
345	
346	    def test_update_partial_leaves_others_intact(self, workspace):
347	        add_to_literature_map(papers=[VASWANI])
348	        key = next(iter(read_literature_map(mode="full").data["papers"]))
349	        update_literature_category(paper_key=key, verified=False)
350	        entry = read_literature_map(mode="full").data["papers"][key]
351	        # Only verified changed — category/role still original
352	        assert entry["category"] == "attention"
353	        assert entry["role"] == "foundation"
354	        assert entry["verified"] is False
355	
356	    def test_unknown_paper_key_errors(self, workspace):
357	        r = update_literature_category(paper_key="nope", category="x")
358	        assert not r.success
359	        assert "not found" in r.error
360	
361	    def test_invalid_role_rejected(self, workspace):
362	        r = update_literature_category(paper_key="foo", role="bogus")
363	        assert not r.success
364	        assert "invalid role" in r.error
365	
366	
367	# ---------------------------------------------------------------------------
368	# upsert_category
369	# ---------------------------------------------------------------------------
370	
371	class TestUpsertCategory:
372	    def test_adds_new(self, workspace):
373	        r = upsert_category(key="attn", name="Attention", narrative="self-attn line")
374	        assert r.success
375	        assert r.data["action"] == "added"
376	        cats = read_literature_map(mode="full").data["categories"]
377	        assert cats[0]["key"] == "attn"
378	        assert cats[0]["narrative"] == "self-attn line"
379	
380	    def test_updates_existing(self, workspace):
381	        upsert_category(key="attn", name="Attention")
382	        r = upsert_category(key="attn", narrative="updated line")
383	        assert r.success
384	        assert r.data["action"] == "updated"
385	        cats = read_literature_map(mode="full").data["categories"]
386	        # Existing name kept (we only passed narrative the 2nd time)
387	        assert cats[0]["name"] == "Attention"
388	        assert cats[0]["narrative"] == "updated line"
389	        assert len(cats) == 1  # not duplicated
390	
391	    def test_missing_key_errors(self, workspace):
392	        r = upsert_category(key="")
393	        assert not r.success
394	
395	
396	# ---------------------------------------------------------------------------
397	# Cross-stage persistence: global → project seed
398	# ---------------------------------------------------------------------------
399	
400	class TestCrossStagePersistence:
401	    def test_global_and_project_maps_are_separate_files(self, workspace):
402	        add_to_literature_map(papers=[VASWANI])  # global
403	        add_to_literature_map(project="my_proj", papers=[BERT])  # project
404	
405	        global_papers = read_literature_map(mode="full").data["papers"]
406	        proj_papers = read_literature_map(project="my_proj", mode="full").data["papers"]
407	
408	        # Each map sees its own paper, not the other
409	        assert any("attention" in p["title"].lower() for p in global_papers.values())
410	        assert all("bert" not in p["title"].lower() for p in global_papers.values())
411	        assert any("bert" in p["title"].lower() for p in proj_papers.values())
412	
413	    def test_seed_propagates_global_into_project(self, workspace):
414	        # Idea phase — add papers to global with idea_id stamp
415	        add_to_literature_map(papers=[VASWANI, BERT])
416	        global_papers = read_literature_map(mode="full").data["papers"]
417	
418	        # Bootstrap project — seed accumulated papers
419	        seeds = list(global_papers.values())
420	        r = seed_literature_map(
421	            project="my_proj", seed_papers=seeds, source_idea_id="idea_007",
422	        )
423	        assert r.success
424	        assert len(r.data["added"]) == 2
425	
426	        proj = read_literature_map(project="my_proj", mode="full").data["papers"]
427	        # Provenance stamped
428	        for p in proj.values():
429	            assert p.get("added_by") == "idea_generator"
430	            assert p.get("source_idea_id") == "idea_007"
431	
432	    def test_seed_without_project_errors(self, workspace):
433	        r = seed_literature_map(project="", seed_papers=[VASWANI])
434	        assert not r.success
435	
436	    def test_seed_idempotent_on_dup_call(self, workspace):
437	        seed_literature_map(
438	            project="p", seed_papers=[VASWANI], source_idea_id="idea_1",
439	        )
440	        r = seed_literature_map(
441	            project="p", seed_papers=[VASWANI], source_idea_id="idea_1",
442	        )
443	        # Second call merges, not adds
444	        assert r.success
445	        assert len(r.data["added"]) == 0
446	        assert len(r.data["merged"]) == 1
447	
448	    def test_file_persistence_survives_process(self, workspace):
449	        # Write, then read raw yaml from disk to verify atomic write
450	        add_to_literature_map(papers=[VASWANI])
451	        path = get_literature_map_path()
452	        assert path.exists()
453	        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
454	        assert raw["meta"]["total_papers"] == 1
455	        assert raw["papers"]
456	        assert "vaswani2017attention" in raw["papers"]
457	
458	
459	# ---------------------------------------------------------------------------
460	# Internal dedup helpers
461	# ---------------------------------------------------------------------------
462	
463	class TestFindExistingKey:
464	    def test_matches_by_doi_first(self):
465	        papers = {
466	            "x": {"title": "Different Title", "doi": "10.1/x"},
467	        }
468	        # Same DOI, different title — DOI wins
469	        match = _find_existing_key(papers, {"title": "Other", "doi": "10.1/X"})
470	        assert match == "x"
471	
472	    def test_matches_by_title_when_no_doi(self):
473	        papers = {"x": {"title": "Hello World", "doi": ""}}
474	        match = _find_existing_key(papers, {"title": "  hello, World!  "})
475	        assert match == "x"
476	
477	    def test_no_match_returns_none(self):
478	        assert _find_existing_key({}, {"title": "Anything"}) is None
479	        assert _find_existing_key(
480	            {"x": {"title": "A"}}, {"title": "B"},
481	        ) is None
482	
483	
484	class TestMergePaper:
485	    def test_only_fills_empty(self):
486	        out = _merge_paper(
487	            {"year": 2017, "venue": ""},
488	            {"year": 2099, "venue": "ICML", "authors": ["X"]},
489	        )
490	        assert out["year"] == 2017  # not overwritten
491	        assert out["venue"] == "ICML"
492	        assert out["authors"] == ["X"]
493	
494	    def test_verified_or_logic(self):
495	        assert _merge_paper({"verified": True}, {"verified": False})["verified"] is True
496	        assert _merge_paper({"verified": False}, {"verified": True})["verified"] is True
497	        assert _merge_paper({"verified": False}, {"verified": False})["verified"] is False
498	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e00403ec-7c73-4c58-98c1-4493beaa0200",
  "isSidechain": true,
  "promptId": "233a5648-42dc-4022-8512-1e41829dae64",
  "agentId": "a277383c324df4f8f",
  "type": "user",
  "uuid": "d4852b35-f4b4-4bd6-9b2f-22ad979adbd1",
  "sourceToolAssistantUUID": "e00403ec-7c73-4c58-98c1-4493beaa0200",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T13:53:04.403Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Xr27rwvUFuJUyACyqvz6Xk`</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -name \"add_to_literature_map\" -o -type f -exec grep -l \"def add_to_literature_map\" {} \\;"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4852b35-f4b4-4bd6-9b2f-22ad979adbd1",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw1qKgncvjC9m3FWUoz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "502532cf-f320-4ade-a14f-a18742782239",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Y47zkkZp9FEiabkEJ88uk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1088,
      "cache_read_input_tokens": 40782,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1088
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 231,
          "cache_read_input_tokens": 40782,
          "cache_creation_input_tokens": 1088,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1088,
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

_source line 17 · 2026-05-20T13:53:48.587Z_

<details><summary>↩ Tool result · `toolu_01Xr27rwvUFuJUyACyqvz6Xk`</summary>

```text
/home/ubuntu/agent-ml-research/core/tools/literature.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "502532cf-f320-4ade-a14f-a18742782239",
  "isSidechain": true,
  "promptId": "233a5648-42dc-4022-8512-1e41829dae64",
  "agentId": "a277383c324df4f8f",
  "type": "user",
  "uuid": "133bf951-5104-497b-8eda-ac130550156a",
  "sourceToolAssistantUUID": "502532cf-f320-4ade-a14f-a18742782239",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-20T13:53:50.083Z_

Excellent! Let me also check the distill.py file to see how literature_map is used during the distillation process:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "133bf951-5104-497b-8eda-ac130550156a",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw5FnBmKFNGCCPujPhv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f68e36de-3291-4b20-a877-26800c90679d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BMQCSXABctJPs7mCmbnVhB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 14759,
      "cache_read_input_tokens": 41870,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14759,
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

_source line 19 · 2026-05-20T13:53:50.751Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01PsPXfCGwyt977s7gfpFdrm`</summary>

```json
{
  "pattern": "add_to_literature_map|literature_map",
  "path": "/home/ubuntu/agent-ml-research/core/tools/distill.py",
  "output_mode": "content",
  "context": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f68e36de-3291-4b20-a877-26800c90679d",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw5FnBmKFNGCCPujPhv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d824a060-64fe-4b9d-acbf-4343554ae34e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BMQCSXABctJPs7mCmbnVhB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 14759,
      "cache_read_input_tokens": 41870,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14759,
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

_source line 20 · 2026-05-20T13:53:50.765Z_

<details><summary>↩ Tool result · `toolu_01PsPXfCGwyt977s7gfpFdrm`</summary>

```text
107-# ---------------------------------------------------------------------------
108-# Paper collection
109-# ---------------------------------------------------------------------------
110-
111-def _collect_papers(project: str, config: dict) -> list[PaperForDistill]:
112:    """Collect papers from literature_map + Semantic Scholar.
113-
114-    Four-layer collection (by proximity):
115:      1. literature_map.yaml (already curated)
116-      2. S2 keyword search (project description keywords)
117-      3. S2 recommendations (seed from layer 1 paper IDs)
118-      4. Citation graph (references of high-relevance papers)
119-    """
120-    papers: dict[str, PaperForDistill] = {}
121-    max_papers = config.get("max_papers", 25)
122-    year_range = config.get("year_range", 2)
123-    current_year = datetime.now(timezone.utc).year
124-
125:    # Layer 1: literature_map
126:    _collect_from_literature_map(project, papers)
127-
128-    if len(papers) >= max_papers:
129-        return _rank_and_trim(papers, max_papers, current_year, year_range)
130-
131-    # Layer 2: S2 keyword search
--
140-        _collect_from_s2_recommendations(seed_ids[:5], papers, max_papers)
141-
142-    return _rank_and_trim(papers, max_papers, current_year, year_range)
143-
144-
145:def _collect_from_literature_map(
146-    project: str,
147-    papers: dict[str, PaperForDistill],
148-) -> None:
149:    """Read existing literature_map and convert to PaperForDistill entries."""
150:    from core.tools.literature import get_literature_map_path, _read_map
151-
152:    path = get_literature_map_path(project)
153-    lit_map = _read_map(path)
154-
155-    raw_papers = lit_map.get("papers") or {}
156-    if isinstance(raw_papers, list):
157-        items = ((e.get("id") or e.get("title", f"paper_{i}"), e) for i, e in enumerate(raw_papers) if isinstance(e, dict))
--
317-        # Citations
318-        if p.citation_count and p.citation_count > 50:
319-            score += 2.0
320-        elif p.citation_count and p.citation_count > 10:
321-            score += 1.0
322:        # Existing literature_map entries get a bonus
323-        if p.role:
324-            score += 1.0
325-        if p.role == "direct-competitor":
326-            score += 2.0
327-        p.relevance_score = score
--
651-            pass
652-
653-    return result
654-
655-
656:def _backfill_literature_map(project: str, papers: list[PaperForDistill]) -> int:
657:    """Write newly discovered papers back to literature_map."""
658:    from core.tools.literature import add_to_literature_map
659-
660-    new_papers = []
661-    for p in papers:
662:        if not p.role:  # Papers without a role came from S2, not literature_map
663-            new_papers.append({
664-                "title": p.title,
665-                "year": p.year,
666-                "venue": p.venue,
667-                "authors": p.authors,
--
675-            })
676-
677-    if not new_papers:
678-        return 0
679-
680:    result = add_to_literature_map(project, new_papers, added_by="distiller")
681-    if result.success:
682-        added = result.data.get("added", 0) if result.data else 0
683-        return added
684-    return 0
685-
--
801-            success=False, project=project,
802-            error=f"项目 {project} 不存在",
803-        )
804-
805-    # ── 1. Collect papers ──
806:    _log("收集", "从 literature_map + Semantic Scholar 收集论文...")
807-    _patch_card("collecting")
808-    _notify_ops("collecting")
809-
810-    papers = _collect_papers(project, config)
811-    if not papers:
812-        _log("收集", "未找到可供蒸馏的论文")
813-        result = DistillResult(
814-            success=False, project=project,
815:            error="未找到可供蒸馏的论文。请先在 literature_map 中添加论文。",
816-        )
817-        # Always try to notify Director — auto_trigger (bootstrap) needs this
818-        # the most: Director just spawned, sees [PROJECT BOOTSTRAP], and would
819:        # otherwise have no idea literature_map needs filling. _inject_...
820-        # itself handles "Director not found yet" (returns False, no error).
821-        director_notified = _inject_distill_failure_to_director(result)
822-        if director_notified:
823-            _notify_user_of_distill_followup(project, chat_id)
824:            _log("跟进", "已通知 Director 补充 literature_map 后重试")
825:            _patch_card("failed", error="literature_map 为空 → 已通知 Director 补充文献")
826:            _notify_ops("failed", "literature_map 为空 → 已通知 Director")
827-        else:
828-            _patch_card("failed", error="未找到论文")
829-            _notify_ops("failed", "未找到论文")
830-        return result
831-
--
897-            error="Distiller session 完成但未产出 skill 文件",
898-        )
899-        _fire_completion_callback(failure, callback_url)
900-        return failure
901-
902:    # Backfill new papers to literature_map
903:    backfilled = _backfill_literature_map(project, papers)
904-
905-    deep_count = min(len(new_to_analyze), max_deep_read) + len(cached_yamls)
906-    abstract_count = len(papers) - deep_count
907-
908-    result = DistillResult(
--
1057-            "[distill] failed to inject [DISTILL] for project=%s", result.project,
1058-        )
1059-
1060-
1061-def _inject_distill_failure_to_director(result: DistillResult) -> bool:
1062:    """Inject guidance into Director when distill fails due to empty literature_map.
1063-
1064-    Returns True iff the Director session was found and the message was queued.
1065-    """
1066-    try:
1067-        from core.cron_hooks import _find_director_for_project
--
1086-            if idea_brief.exists() else "通过深度文献调研，"
1087-        )
1088-
1089-        message = (
1090-            f"[DISTILL] 蒸馏失败：{result.error}\n\n"
1091:            f"`literature_map.yaml` 是蒸馏的输入源。请{ref_hint}"
1092:            f"用 `add_to_literature_map` 添加 ≥5 篇核心相关论文（含 S2 paper ID 或 arXiv ID），"
1093-            f"填充完毕后通知用户重新触发 `/distill`。"
1094-        )
1095-
1096-        def _silent_reply(reply: str) -> None:
1097-            logger.debug("[distill] Director reply silenced: %s", (reply or "")[:80])
--
1111-        )
1112-        return False
1113-
1114-
1115-def _notify_user_of_distill_followup(project: str, chat_id: str) -> None:
1116:    """Notify A群 that Director was asked to fill literature_map after distill failure."""
1117-    if not chat_id:
1118-        return
1119-    try:
1120-        from core.tools.feishu import send_message
1121-        send_message(
1122-            chat_id=chat_id,
1123-            text=(
1124:                f"📚 {project} 的文献蒸馏暂时无法进行：literature_map 为空。\n"
1125-                f"已请 Director 参考 IDEA_BRIEF 的 key_references + 深度文献调研补充论文，"
1126-                f"完成后会再通知您触发 /distill。"
1127-            ),
1128-        )
1129-    except Exception:
--
1159-# ---------------------------------------------------------------------------
1160-
1161-def distill_papers(project: str, force: bool = False) -> ToolResult:
1162-    """从文献库蒸馏研究方法论和写作范式，生成项目专属 skill。
1163-
1164:    自动收集 literature_map + Semantic Scholar 论文，
1165-    用 Claude 分析后生成/更新 distilled-research 和 distilled-writing skill。
1166-
1167-    Args:
1168-        project: 项目名称
1169-        force: True 则忽略"无新论文"检查，强制重新蒸馏
--
1202-                f"📚 {project} 文献蒸馏完成 (v{result.version})\n"
1203-                f"├ 精读论文：{result.deep_read_count} 篇（全文）"
1204-                f"+ {result.abstract_only_count} 篇（仅摘要）\n"
1205-                f"├ 研究方法论 skill：{result.research_skill_chars} 字\n"
1206-                f"├ 写作范式 skill：{result.writing_skill_chars} 字\n"
1207:                f"└ 新发现论文：{result.new_papers_found} 篇已回写 literature_map"
1208-            ),
1209-        },
1210-    )
1211-
1212-
--
1215-# ---------------------------------------------------------------------------
1216-
1217-def get_distill_status(project: str) -> ToolResult:
1218-    """查看蒸馏状态：最后蒸馏时间、论文数、version。
1219-
1220:    `literature_map_total` 和 `cached_layer1_count` 即使在 never_distilled 时也
1221-    返回真实值——caller 用这两个字段排查"为啥蒸馏跑不动/没产出"，所以不能因为没
1222-    skill 文件就早退。
1223-    """
1224:    from core.tools.literature import get_literature_map_path, _read_map
1225-
1226-    skills_dir = _paths.project_skills_dir(project)
1227-    research_path = skills_dir / "distilled-research.skill.md"
1228-    writing_path = skills_dir / "distilled-writing.skill.md"
1229-    tmp_dir = _distill_tmp_dir(project)
1230-
1231:    lit_path = get_literature_map_path(project)
1232-    lit_map = _read_map(lit_path)
1233:    literature_map_total = len(lit_map.get("papers") or {})
1234-    cached_count = len(list(tmp_dir.glob("*.yaml"))) if tmp_dir.exists() else 0
1235-
1236-    if not research_path.exists() and not writing_path.exists():
1237-        return ToolResult(
1238-            success=True,
1239-            data={
1240-                "status": "never_distilled",
1241-                "project": project,
1242:                "literature_map_total": literature_map_total,
1243-                "cached_layer1_count": cached_count,
1244-            },
1245-        )
1246-
1247-    info: dict[str, Any] = {
1248-        "project": project,
1249-        "status": "distilled",
1250:        "literature_map_total": literature_map_total,
1251-        "cached_layer1_count": cached_count,
1252-    }
1253-
1254-    for label, path in [("research", research_path), ("writing", writing_path)]:
1255-        if path.exists():
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d824a060-64fe-4b9d-acbf-4343554ae34e",
  "isSidechain": true,
  "promptId": "233a5648-42dc-4022-8512-1e41829dae64",
  "agentId": "a277383c324df4f8f",
  "type": "user",
  "uuid": "3c8faca9-7af5-420b-86a9-a581653b7298",
  "sourceToolAssistantUUID": "d824a060-64fe-4b9d-acbf-4343554ae34e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T13:53:50.874Z_

<details open><summary>🔧 Tool call — Read · `toolu_014oDjbbjFcHYJeqK5qtwZkM`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/tools/distill.py",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c8faca9-7af5-420b-86a9-a581653b7298",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw5FnBmKFNGCCPujPhv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "622acc2e-e036-44b9-b48e-6ecf22a8ae2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BMQCSXABctJPs7mCmbnVhB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 14759,
      "cache_read_input_tokens": 41870,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14759
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 233,
          "cache_read_input_tokens": 41870,
          "cache_creation_input_tokens": 14759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14759,
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

_source line 22 · 2026-05-20T13:53:50.881Z_

<details><summary>↩ Tool result · `toolu_014oDjbbjFcHYJeqK5qtwZkM`</summary>

```text
1	"""Paper distillation engine — extract domain knowledge from related papers.
2	
3	Distills research methodology and writing patterns from project-related papers
4	into two project-specific skills:
5	
6	  - ``distilled-research.skill.md`` — baselines, metrics, datasets, trends
7	  - ``distilled-writing.skill.md`` — narrative strategies, structure conventions
8	
9	Two-layer architecture:
10	  Layer 1: Per-paper deep analysis → ``distill_tmp/{paper_key}.yaml``
11	  Layer 2: Cross-paper synthesis → skill files
12	
13	Triggered by:
14	  - ``distill_papers`` MCP tool (Agent/Director)
15	  - ``POST /api/distill/{project}`` HTTP endpoint (Manager → BE)
16	  - ``/distill`` Feishu command (via Manager)
17	"""
18	
19	from __future__ import annotations
20	
21	import asyncio
22	import logging
23	import os
24	import re
25	import shutil
26	from dataclasses import dataclass, field
27	from datetime import datetime, timezone
28	from pathlib import Path
29	from typing import Any
30	
31	import yaml
32	
33	from core import paths as _paths
34	from core.skills.loader import (
35	    load_skills_config,
36	    parse_skill_md,
37	)
38	from core.tools.result import ToolResult
39	
40	logger = logging.getLogger(__name__)
41	
42	
43	# ---------------------------------------------------------------------------
44	# Configuration defaults
45	# ---------------------------------------------------------------------------
46	
47	_DEFAULT_DISTILL_CONFIG: dict[str, Any] = {
48	    "model": "claude-opus-4-6",
49	    "max_papers": 25,
50	    "max_deep_read": 8,
51	    "max_skill_chars": 3000,
52	    "auto_on_bootstrap": True,
53	    "year_range": 2,
54	}
55	
56	
57	def _load_distill_config() -> dict[str, Any]:
58	    """Load distillation config from skills.yaml ``distillation`` section."""
59	    cfg = dict(_DEFAULT_DISTILL_CONFIG)
60	    skills_cfg = load_skills_config()
61	    distill_section = skills_cfg.get("distillation") or {}
62	    if isinstance(distill_section, dict):
63	        cfg.update(distill_section)
64	    return cfg
65	
66	
67	# ---------------------------------------------------------------------------
68	# Data types
69	# ---------------------------------------------------------------------------
70	
71	@dataclass
72	class PaperForDistill:
73	    """Minimal paper metadata for the distillation pipeline."""
74	    paper_key: str
75	    title: str
76	    year: int | None = None
77	    venue: str = ""
78	    authors: list[str] = field(default_factory=list)
79	    abstract: str = ""
80	    citation_count: int | None = None
81	    semantic_scholar_id: str = ""
82	    arxiv_id: str = ""
83	    doi: str = ""
84	    url: str = ""
85	    pdf_url: str = ""
86	    role: str = ""
87	    relevance_score: float = 0.0
88	
89	
90	@dataclass
91	class DistillResult:
92	    """Result of a distillation run."""
93	    success: bool
94	    project: str
95	    version: int = 0
96	    paper_count: int = 0
97	    deep_read_count: int = 0
98	    abstract_only_count: int = 0
99	    new_papers_found: int = 0
100	    research_skill_path: str = ""
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "622acc2e-e036-44b9-b48e-6ecf22a8ae2c",
  "isSidechain": true,
  "promptId": "233a5648-42dc-4022-8512-1e41829dae64",
  "agentId": "a277383c324df4f8f",
  "type": "user",
  "uuid": "c3986e2e-3421-4199-9495-90a31cd3c7db",
  "sourceToolAssistantUUID": "622acc2e-e036-44b9-b48e-6ecf22a8ae2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-20T13:53:52.442Z_

Now let me search for example YAML structure or any sample literature maps in test files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3986e2e-3421-4199-9495-90a31cd3c7db",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw5RfW6C12WW3x622jr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0aa2b708-7062-4aaa-847d-0d59db5ba7bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LFZL1YTCoDaXtQfRsEDJqn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 4641,
      "cache_read_input_tokens": 56629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4641,
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

_source line 24 · 2026-05-20T13:53:52.984Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011SzSWGw5rnLkFBpwGwXrXW`</summary>

```json
{
  "command": "grep -r \"categories:\" /home/ubuntu/agent-ml-research --include=\"*.yaml\" --include=\"*.yml\" | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0aa2b708-7062-4aaa-847d-0d59db5ba7bd",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw5RfW6C12WW3x622jr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "06c4ad09-5696-4e58-9dc7-c6c155036396",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LFZL1YTCoDaXtQfRsEDJqn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 4641,
      "cache_read_input_tokens": 56629,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4641
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 102,
          "cache_read_input_tokens": 56629,
          "cache_creation_input_tokens": 4641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4641,
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

_source line 25 · 2026-05-20T13:53:53.095Z_

<details><summary>↩ Tool result · `toolu_011SzSWGw5rnLkFBpwGwXrXW`</summary>

```text
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/playwright/driver/package/protocol.yml:        categories:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06c4ad09-5696-4e58-9dc7-c6c155036396",
  "isSidechain": true,
  "promptId": "233a5648-42dc-4022-8512-1e41829dae64",
  "agentId": "a277383c324df4f8f",
  "type": "user",
  "uuid": "807250f9-e297-40cb-b612-bc2c2cd25352",
  "sourceToolAssistantUUID": "06c4ad09-5696-4e58-9dc7-c6c155036396",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-20T13:53:55.662Z_

Let me look for example usage in the MCP server:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "807250f9-e297-40cb-b612-bc2c2cd25352",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw5b72c3rqbaPj4W8wu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9177220f-1b88-4401-bf7f-a43a840ec8ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EKUkuvL5Lz4cqhZrsxcuyS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 152,
      "cache_read_input_tokens": 61270,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 152,
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

_source line 27 · 2026-05-20T13:53:56.134Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01CD7RDWiNVg8kpPpY2k7Vch`</summary>

```json
{
  "pattern": "add_to_literature_map|papers:|authors:|venue:",
  "path": "/home/ubuntu/agent-ml-research/core/mcp_server.py",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9177220f-1b88-4401-bf7f-a43a840ec8ec",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw5b72c3rqbaPj4W8wu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5e6d9245-be47-4b36-bed9-857c485c2d31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EKUkuvL5Lz4cqhZrsxcuyS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 152,
      "cache_read_input_tokens": 61270,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 152
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 148,
          "cache_read_input_tokens": 61270,
          "cache_creation_input_tokens": 152,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 152,
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

_source line 28 · 2026-05-20T13:53:56.144Z_

<details><summary>↩ Tool result · `toolu_01CD7RDWiNVg8kpPpY2k7Vch`</summary>

```text
2790-def dream_simulate(
2791-    project: str,
2792-    what_if: list[dict] | None = None,
2793:    venue: str = "",
2794-    focus: str = "",
2795-    review_mode: str = "simple",
2796-    review_visible: bool | None = None,
--
2811-        what_if: Hypothetical experiments to add to ``experiment_plan`` for
2812-            this run only (does NOT mutate the plan file). Each item is
2813-            ``{name, claim, description, estimated_gpu_hours}``.
2814:        venue: Venue slug from venue_registry (e.g. "emnlp-2026", "neurips-2026").
2815-            Leave empty to auto-read from project config.
2816-        focus: Free-form hint biasing the imagined scenarios.
2817-        review_mode: "simple" (1 reviewer) | "full" (2 reviewers roundtable).
--
4807-def request_review_approval(
4808-    project: str,
4809-    paper_title: str = "",
4810:    venue: str = "",
4811-    paper_path: str = "",
4812-    reason: str = "",
4813-    chat_id: str = "",
--
5144-    project: str,
5145-    paper_path: str,
5146-    paper_pdf_path: str,
5147:    venue: str,
5148-    track: str = "",
5149-    deadline: str = "",
5150-    supplementary_paths: str = "",
--
5170-            MUST be the latest version currently being worked on.
5171-        paper_pdf_path: Path to the COMPILED PDF (e.g. "projects/{project}/paper/main.pdf").
5172-            MUST be freshly compiled from paper_path. Run paper_compile_and_check() first.
5173:        venue: Target venue (e.g. "EMNLP 2026", "NeurIPS 2025").
5174-        track: Submission category — fill in based on the target venue's actual terminology.
5175-        deadline: Known deadline (e.g. "2026-06-15"); will be independently verified.
5176-        supplementary_paths: Comma-separated supplementary material paths.
--
5312-def request_external_review(
5313-    project: str,
5314-    paper_pdf_path: str,
5315:    venue: str = "",
5316-    note: str = "",
5317-    chat_id: str = "",
5318-    reminder_hours: int = 8,
--
5330-    Args:
5331-        project: Current project name.
5332-        paper_pdf_path: Path to the paper PDF on the server.
5333:        venue: Target venue (e.g. "EMNLP 2026") — helps user select on paperreview.ai.
5334-        note: Optional note for the user.
5335-        chat_id: Group A chat_id (optional, loads from project config).
5336-        reminder_hours: Hours before auto-reminder (default 8).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e6d9245-be47-4b36-bed9-857c485c2d31",
  "isSidechain": true,
  "promptId": "233a5648-42dc-4022-8512-1e41829dae64",
  "agentId": "a277383c324df4f8f",
  "type": "user",
  "uuid": "d223f1af-12f3-4aa0-b7c9-eb0f05402baa",
  "sourceToolAssistantUUID": "5e6d9245-be47-4b36-bed9-857c485c2d31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-20T13:53:57.448Z_

Let me look at the MCP server for the distill function definition and how papers are passed:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d223f1af-12f3-4aa0-b7c9-eb0f05402baa",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw5pG3ieUsnfxzZt6vG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cef6d8f2-666c-4593-8a6d-5976b96cd320",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WS4aghDcBpQ1rzHt17WZ9m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 950,
      "cache_read_input_tokens": 61422,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 950,
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

_source line 30 · 2026-05-20T13:53:57.753Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QsfT9T6nyvoXMGkGLUASPg`</summary>

```json
{
  "command": "grep -A 30 \"def distill_papers\" /home/ubuntu/agent-ml-research/core/mcp_server.py | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cef6d8f2-666c-4593-8a6d-5976b96cd320",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw5pG3ieUsnfxzZt6vG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1689a57c-b8ff-4f11-8870-89a35a07d011",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WS4aghDcBpQ1rzHt17WZ9m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 950,
      "cache_read_input_tokens": 61422,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 950
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 108,
          "cache_read_input_tokens": 61422,
          "cache_creation_input_tokens": 950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 950,
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

_source line 31 · 2026-05-20T13:53:57.803Z_

<details><summary>↩ Tool result · `toolu_01QsfT9T6nyvoXMGkGLUASPg`</summary>

```text
def distill_papers(project: str, force: bool = False) -> str:
    """从文献库蒸馏研究方法论和写作范式，生成项目专属 skill。

    自动收集 literature_map + Semantic Scholar 论文，
    用 Claude 分析后生成/更新 distilled-research 和 distilled-writing skill。

    异步执行——Distiller Agent session 在后台运行，预计 5-10 分钟。
    蒸馏完成后自动通知。

    Args:
        project: 项目名称
        force: True 则忽略"无新论文"检查，强制重新蒸馏
    """
    from core.tools.distill import distill_papers as _dp
    return _tool_result_to_str(_dp(project, force=force))


@mcp.tool()
def get_distill_status(project: str) -> str:
    """查看蒸馏状态：最后蒸馏时间、论文数、version、新增论文数。

    Args:
        project: 项目名称
    """
    from core.tools.distill import get_distill_status as _gds
    return _tool_result_to_str(_gds(project))


@mcp.tool()
def auto_build_report_facts(project: str) -> str:
    """Regenerate the auto-derived facts block in report.md from registry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1689a57c-b8ff-4f11-8870-89a35a07d011",
  "isSidechain": true,
  "promptId": "233a5648-42dc-4022-8512-1e41829dae64",
  "agentId": "a277383c324df4f8f",
  "type": "user",
  "uuid": "147483db-db20-4567-bcd1-eb335878a187",
  "sourceToolAssistantUUID": "1689a57c-b8ff-4f11-8870-89a35a07d011",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-20T13:53:59.086Z_

Let me check how literature_map is documented elsewhere:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "147483db-db20-4567-bcd1-eb335878a187",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw5wDW5apjK66Mv7YCU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d6cefb8a-d659-43d8-98f5-89c900b7a871",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013VGpziGw6Njao27eE57di8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 497,
      "cache_read_input_tokens": 62372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 497,
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

_source line 33 · 2026-05-20T13:54:00.004Z_

<details open><summary>🔧 Tool call — Grep · `toolu_011zAkracTgCunJfbFVDQ1fQ`</summary>

```json
{
  "pattern": "literature_map\\.yaml|YAML structure|papers:.*authors:|title:.*year:",
  "path": "/home/ubuntu/agent-ml-research/prompts/roles",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6cefb8a-d659-43d8-98f5-89c900b7a871",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw5wDW5apjK66Mv7YCU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b9371ac5-ef4c-4f8e-82b1-ce00ae6e14cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013VGpziGw6Njao27eE57di8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 497,
      "cache_read_input_tokens": 62372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 497,
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

_source line 34 · 2026-05-20T13:54:00.034Z_

<details><summary>↩ Tool result · `toolu_011zAkracTgCunJfbFVDQ1fQ`</summary>

```text
/home/ubuntu/agent-ml-research/prompts/roles/director.md-160-## 文献图谱与蒸馏
/home/ubuntu/agent-ml-research/prompts/roles/director.md-161-
/home/ubuntu/agent-ml-research/prompts/roles/director.md:162:`literature_map.yaml` 是文献蒸馏（`/distill`）的输入源——蒸馏会从中收集同行论文，生成研究方法论和写作范式 skill。**立项初期优先填充**：参考 IDEA_BRIEF.md 的 key_references + 深度调研，用 `add_to_literature_map` 添加 ≥5 篇核心相关论文。填充完毕后通知用户触发 `/distill`。
/home/ubuntu/agent-ml-research/prompts/roles/director.md-163-
/home/ubuntu/agent-ml-research/prompts/roles/director.md-164-## report.md 维护边界（硬约束）
--
/home/ubuntu/agent-ml-research/prompts/roles/paper-agent.md-62-
/home/ubuntu/agent-ml-research/prompts/roles/paper-agent.md-63-**Step 3 — Literature Gap-Fill（按 `literature_strategy.micro_clusters` 串行逐 cluster）**
/home/ubuntu/agent-ml-research/prompts/roles/paper-agent.md:64:- **不从零搜**：先 `read_project_file("literature_map.yaml")`，按 cluster 统计已有 verified 条目数（`papers[*]` 的 `category` 字段对应 `cluster_name`，`verified=true` 才计入）
/home/ubuntu/agent-ml-research/prompts/roles/paper-agent.md-65-- 对每个 cluster 计算缺口 `gap = max(0, target_count - verified_count)`；`gap == 0` 跳过；同时校验 `must_cite` 列表中每篇论文是否已在 map 中（缺失也算 gap，单独标注必查）
/home/ubuntu/agent-ml-research/prompts/roles/paper-agent.md-66-- 串行逐 cluster `spawn_worker(task_type="paper_research", project=..., task_prompt=<下方 Worker 模板>)`——任意时刻最多 1 个活跃 Worker，前一个 cluster `[WORKER DONE]` 才启动下一个
/home/ubuntu/agent-ml-research/prompts/roles/paper-agent.md:67:[Omitted long matching line]
/home/ubuntu/agent-ml-research/prompts/roles/paper-agent.md:68:- Worker 返回后立即重新读 `literature_map.yaml` 确认新增数 ≥ 该 cluster 的 gap；缺额 ≥2 → 派一次补搜 Worker；仍缺 → 汇报 Director（不要静默放过）
/home/ubuntu/agent-ml-research/prompts/roles/paper-agent.md-69-- 全部 cluster 完成后 `verify_references(paper_dir, project=..., skip_online=False)`：传入 `paper_dir` 即 `projects/{project}/paper/`，先做 `.tex` ↔ `.bib` 交叉检查，再走 OpenAlex online 验证
/home/ubuntu/agent-ml-research/prompts/roles/paper-agent.md:70:- **同步 .bib**：派一个 task_type=`paper_research:bib_sync` 的 Worker（不需要 search 能力），让它读 `literature_map.yaml`，把所有 `verified=true` 的条目按 `bibtex_key` 渲染成 BibTeX entry 写入 `projects/{project}/paper/references.bib`。Worker 用 Edit/Write 直接写文件；写入前先备份原 `.bib`（`cp references.bib references.bib.prev`）以便回滚
/home/ubuntu/agent-ml-research/prompts/roles/paper-agent.md-71-- **未验证条目处理**：`verified=false` 的条目不进 `.bib`；如果 Step 4 章节 Worker 引用到了未验证条目，正文中标 `[UNVERIFIED: title]` 占位，由 Step 5 修复
/home/ubuntu/agent-ml-research/prompts/roles/paper-agent.md-72-- 完成后进入 Step 4。任一 cluster 累计失败 ≥2 → 停下来汇报 Director（避免无意义 Worker 烧 token）
--
/home/ubuntu/agent-ml-research/prompts/roles/agent.md-69-## 实验规划参考文献
/home/ubuntu/agent-ml-research/prompts/roles/agent.md-70-
/home/ubuntu/agent-ml-research/prompts/roles/agent.md:71:规划实验方案（写训练命令、选超参、定 baseline、选 evaluation metric）前，先检查 literature_map.yaml 是否有相关 paper。优先参考 `role=direct-competitor` 和 `role=method-component` 的 paper 的实验设置（数据集、metric、baseline、训练超参）。具体做法：
/home/ubuntu/agent-ml-research/prompts/roles/agent.md-72-- 派 Worker 调用 `read_literature_map(mode="competitors")` 获取竞品论文列表
/home/ubuntu/agent-ml-research/prompts/roles/agent.md-73-- 让 Worker 下载/阅读关键竞品论文的实验部分（WebFetch PDF/HTML），提取：数据集、evaluation metric、baseline 方法列表、关键超参（lr、batch_size、epochs、optimizer）
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9371ac5-ef4c-4f8e-82b1-ce00ae6e14cd",
  "isSidechain": true,
  "promptId": "233a5648-42dc-4022-8512-1e41829dae64",
  "agentId": "a277383c324df4f8f",
  "type": "user",
  "uuid": "4d96c570-14a1-474e-934a-56ba5f2faf46",
  "sourceToolAssistantUUID": "b9371ac5-ef4c-4f8e-82b1-ce00ae6e14cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-20T13:54:02.472Z_

Perfect! Now let me check the semantic_scholar.py to see what fields come from S2:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d96c570-14a1-474e-934a-56ba5f2faf46",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw67xAtJfEv362xoPjF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f7502ef6-7071-44d2-bdf4-737b481a9aab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Dt6he9aVoeqhEjiSat6zUg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1846,
      "cache_read_input_tokens": 62869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1846,
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

_source line 36 · 2026-05-20T13:54:02.844Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KVXkKiSgnNU1VKzYPtRbMw`</summary>

```json
{
  "command": "grep -A 20 \"class.*Paper\\|def.*paper\" /home/ubuntu/agent-ml-research/core/tools/semantic_scholar.py | head -60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7502ef6-7071-44d2-bdf4-737b481a9aab",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw67xAtJfEv362xoPjF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4d5c651e-0ae4-4fc0-939f-396b7c440af2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Dt6he9aVoeqhEjiSat6zUg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1846,
      "cache_read_input_tokens": 62869,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1846
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 113,
          "cache_read_input_tokens": 62869,
          "cache_creation_input_tokens": 1846,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1846,
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

_source line 37 · 2026-05-20T13:54:02.897Z_

<details><summary>↩ Tool result · `toolu_01KVXkKiSgnNU1VKzYPtRbMw`</summary>

```text
def _normalize_paper(raw: dict) -> dict:
    """Flatten the S2 paper response into the literature_map dict shape.

    Output fields mirror what literature.add_to_literature_map expects so
    the caller can feed search results straight in. Missing fields become
    empty strings / None.
    """
    if not isinstance(raw, dict):
        return {}

    external_ids = raw.get("externalIds") or {}
    arxiv_id = external_ids.get("ArXiv") or ""
    doi = external_ids.get("DOI") or ""

    authors_raw = raw.get("authors") or []
    authors: list[str] = []
    for a in authors_raw:
        if isinstance(a, dict):
            name = a.get("name") or ""
            if name:
                authors.append(name)
--
def search_papers(
    query: str,
    limit: int = 10,
    year_range: str | None = None,
    fields_of_study: Iterable[str] | None = None,
    fields: Iterable[str] | None = None,
) -> ToolResult:
    """Keyword search against Semantic Scholar.

    Args:
        query: Free-text query (e.g. ``"GPTQ post-training quantization"``).
            Required.
        limit: 1..100 — results requested. Default 10. Values >100 are
            clamped because the API rejects them.
        year_range: Optional filter — ``"2024"`` or ``"2023-2025"``.
            Malformed values are silently dropped.
        fields_of_study: Optional list of S2 study fields to filter on
            (e.g. ``["Computer Science"]``).
        fields: Override the requested field set. Defaults to
            ``_DEFAULT_FIELDS`` (paperId/title/abstract/year/venue/authors/
            citationCount/tldr/externalIds/url).
--
def get_paper_references(
    paper_id: str,
    limit: int = 20,
    fields: Iterable[str] | None = None,
) -> ToolResult:
    """List papers that ``paper_id`` cites (reverse-tracking).

    Args:
        paper_id: S2 paper id, ``DOI:10.x/y``, ``ARXIV:1706.03762``, etc.
            Required.
        limit: 1..1000 — number of references to return. Default 20.
            Values >1000 are clamped to 1000 (S2 hard cap on this endpoint).
        fields: Override the requested field set on the cited papers.

    Returns:
        ToolResult.data = {
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d5c651e-0ae4-4fc0-939f-396b7c440af2",
  "isSidechain": true,
  "promptId": "233a5648-42dc-4022-8512-1e41829dae64",
  "agentId": "a277383c324df4f8f",
  "type": "user",
  "uuid": "0b90308b-28aa-4ad2-b0bb-3b2e1146616a",
  "sourceToolAssistantUUID": "4d5c651e-0ae4-4fc0-939f-396b7c440af2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-20T13:54:04.176Z_

Excellent! Now let me get the complete _normalize_paper function:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b90308b-28aa-4ad2-b0bb-3b2e1146616a",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw6K6PmpWnxczULaubQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e4b5da5e-1a7e-4f75-8717-675fddbb3fd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AbvMbzUjfSvYaDtPRijL98",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 791,
      "cache_read_input_tokens": 64715,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 791,
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

_source line 39 · 2026-05-20T13:54:04.355Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BpxRihVK8L9co8csmKV3PH`</summary>

```json
{
  "command": "grep -A 40 \"def _normalize_paper\" /home/ubuntu/agent-ml-research/core/tools/semantic_scholar.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4b5da5e-1a7e-4f75-8717-675fddbb3fd4",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw6K6PmpWnxczULaubQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3e11d4aa-1954-48fa-ba41-1bcaace656d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AbvMbzUjfSvYaDtPRijL98",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 791,
      "cache_read_input_tokens": 64715,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 791
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 100,
          "cache_read_input_tokens": 64715,
          "cache_creation_input_tokens": 791,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 791,
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

_source line 40 · 2026-05-20T13:54:04.400Z_

<details><summary>↩ Tool result · `toolu_01BpxRihVK8L9co8csmKV3PH`</summary>

```text
def _normalize_paper(raw: dict) -> dict:
    """Flatten the S2 paper response into the literature_map dict shape.

    Output fields mirror what literature.add_to_literature_map expects so
    the caller can feed search results straight in. Missing fields become
    empty strings / None.
    """
    if not isinstance(raw, dict):
        return {}

    external_ids = raw.get("externalIds") or {}
    arxiv_id = external_ids.get("ArXiv") or ""
    doi = external_ids.get("DOI") or ""

    authors_raw = raw.get("authors") or []
    authors: list[str] = []
    for a in authors_raw:
        if isinstance(a, dict):
            name = a.get("name") or ""
            if name:
                authors.append(name)
        elif isinstance(a, str):
            authors.append(a)

    tldr_obj = raw.get("tldr")
    tldr_text = ""
    if isinstance(tldr_obj, dict):
        tldr_text = tldr_obj.get("text") or ""

    venue = raw.get("venue") or ""
    pub_venue = raw.get("publicationVenue")
    if not venue and isinstance(pub_venue, dict):
        venue = pub_venue.get("name") or ""

    open_pdf = raw.get("openAccessPdf")
    pdf_url = ""
    if isinstance(open_pdf, dict):
        pdf_url = open_pdf.get("url") or ""

    return {
        "paper_id": raw.get("paperId") or "",
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e11d4aa-1954-48fa-ba41-1bcaace656d7",
  "isSidechain": true,
  "promptId": "233a5648-42dc-4022-8512-1e41829dae64",
  "agentId": "a277383c324df4f8f",
  "type": "user",
  "uuid": "e2a5f11d-cf00-412d-86f9-c9fe98a96172",
  "sourceToolAssistantUUID": "3e11d4aa-1954-48fa-ba41-1bcaace656d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T13:54:05.591Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012e9fjBRQY8nWiBB3cmczTk`</summary>

```json
{
  "command": "grep -A 60 \"def _normalize_paper\" /home/ubuntu/agent-ml-research/core/tools/semantic_scholar.py | tail -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2a5f11d-cf00-412d-86f9-c9fe98a96172",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw6RNRUCrvXDSrE6S1u",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "293c0131-82f0-4ded-a061-add2053b3851",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FcMhcBdfTgcFZTGHwXy5Eq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 509,
      "cache_read_input_tokens": 65506,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 509
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 65506,
          "cache_creation_input_tokens": 509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 509,
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

_source line 42 · 2026-05-20T13:54:05.643Z_

<details><summary>↩ Tool result · `toolu_012e9fjBRQY8nWiBB3cmczTk`</summary>

```text
    if not venue and isinstance(pub_venue, dict):
        venue = pub_venue.get("name") or ""

    open_pdf = raw.get("openAccessPdf")
    pdf_url = ""
    if isinstance(open_pdf, dict):
        pdf_url = open_pdf.get("url") or ""

    return {
        "paper_id": raw.get("paperId") or "",
        "title": raw.get("title") or "",
        "abstract": raw.get("abstract") or "",
        "year": raw.get("year"),
        "venue": venue,
        "authors": authors,
        "citation_count": raw.get("citationCount"),
        "reference_count": raw.get("referenceCount"),
        "tldr": tldr_text,
        "arxiv_id": arxiv_id,
        "doi": doi,
        "url": raw.get("url") or "",
        "pdf_url": pdf_url,
        # Semantic Scholar paper id, also stored for literature_map dedup.
        "semantic_scholar_id": raw.get("paperId") or "",
    }


def _parse_year_range(year_range: str | None) -> str | None:
    """Validate a ``"YYYY"`` or ``"YYYY-YYYY"`` year filter."""
    if not year_range:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "293c0131-82f0-4ded-a061-add2053b3851",
  "isSidechain": true,
  "promptId": "233a5648-42dc-4022-8512-1e41829dae64",
  "agentId": "a277383c324df4f8f",
  "type": "user",
  "uuid": "d6ed8654-2f78-41a2-8206-76698379acc0",
  "sourceToolAssistantUUID": "293c0131-82f0-4ded-a061-add2053b3851",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-20T13:54:07.225Z_

Perfect! Now let me create a comprehensive summary with an example YAML structure. Let me look at one more thing - the actual YAML output format:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6ed8654-2f78-41a2-8206-76698379acc0",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw6WfuinUAFXo1HSQBm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cb7ac9d6-3198-4893-880f-d81daed0c351",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011Cp1AMEW4gXExAQhJkh7B8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 426,
      "cache_read_input_tokens": 66015,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 426,
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

_source line 44 · 2026-05-20T13:54:07.469Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Lf7mgEo6Ar8eUYJXiDjmE6`</summary>

```json
{
  "command": "grep -B 5 -A 25 \"def upsert_category\" /home/ubuntu/agent-ml-research/core/tools/literature.py | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb7ac9d6-3198-4893-880f-d81daed0c351",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw6WfuinUAFXo1HSQBm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "450e4563-6ffb-48cd-a0de-56d0428b876c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011Cp1AMEW4gXExAQhJkh7B8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 426,
      "cache_read_input_tokens": 66015,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 426
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 124,
          "cache_read_input_tokens": 66015,
          "cache_creation_input_tokens": 426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 426,
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

_source line 45 · 2026-05-20T13:54:07.521Z_

<details><summary>↩ Tool result · `toolu_01Lf7mgEo6Ar8eUYJXiDjmE6`</summary>

```text
        "paper_key": paper_key,
        "updated_fields": updated,
    })


def upsert_category(
    project: str | None = None,
    key: str = "",
    name: str = "",
    narrative: str = "",
) -> ToolResult:
    """Add or update a category entry in the categories[] list.

    Categories define the Related Work subsection structure. A paper's
    ``category`` field references one of these by ``key``.

    Args:
        project: Project name — None edits the global map.
        key: Category slug (e.g. "attention_mechanisms"). Required.
        name: Human-readable name (e.g. "Attention Mechanisms"). Required for new.
        narrative: One-line description of the category's narrative arc.

    Returns:
        ToolResult.data = {"key", "action": "added"|"updated"}.
    """
    if not key:
        return ToolResult(success=False, error="key is required")

    state = {"action": "added"}

    def _apply(data: dict) -> None:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "450e4563-6ffb-48cd-a0de-56d0428b876c",
  "isSidechain": true,
  "promptId": "233a5648-42dc-4022-8512-1e41829dae64",
  "agentId": "a277383c324df4f8f",
  "type": "user",
  "uuid": "355785e0-445d-40bf-8580-d7813d8c64d8",
  "sourceToolAssistantUUID": "450e4563-6ffb-48cd-a0de-56d0428b876c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-20T13:54:28.593Z_

Perfect! Now I have all the information I need. Let me compile a comprehensive report on the `literature_map.yaml` format.

## Summary: literature_map.yaml Format

Based on my thorough search of the agent-ml-research codebase, here's the complete documentation of the `literature_map.yaml` file format:

### File Locations
1. **Project-level**: `projects/{project}/literature_map.yaml` — Used during Research and Writing phases
2. **Global (Idea phase)**: `{WORKSPACE_ROOT}/literature_map.yaml` — Used before a project exists

### Top-Level YAML Structure

```yaml
meta:
  last_updated: "2026-05-20T15:30:00Z"  # ISO 8601 timestamp
  total_papers: N                        # Auto-calculated on write

categories:
  - key: "attention_mechanisms"          # Slug for Related Work subsections
    name: "Attention Mechanisms"         # Human-readable name
    narrative: "Evolution of self-attention architectures"  # Category narrative arc

papers:
  vaswani2017attention:                  # YAML key (bibtex_key or auto-generated)
    # Core metadata fields (always present)
    title: "Attention Is All You Need"
    authors:                             # List[str]
      - "Vaswani, A."
      - "Shazeer, N."
      - "Parmar, N."
    year: 2017                           # Integer or None
    venue: "NeurIPS"                     # Conference/Journal name
    
    # External identifiers (for deduplication)
    doi: "10.5555/3295222.3295349"       # Normalized: lowercase, stripped prefixes
    url: "https://arxiv.org/abs/1706.03762"
    semantic_scholar_id: "paperId"       # S2 API paper ID
    
    # Classification fields (for Related Work organization)
    category: "attention"                # References categories[].key
    role: "foundation"                   # One of: foundation, direct-competitor,
                                         #         method-component, evaluation, background
    relevance: "Foundational transformer architecture"  # One-line relevance description
    
    # Content fields
    abstract: "We propose a new simple network architecture based solely..."
    
    # Verification and provenance
    verified: true                       # Whether entry passed OpenAlex/manual check
    added_by: "paper-research"           # Tag: "paper-research", "idea-generator",
                                         #      "distiller", "user", etc.
    added_at: "2026-05-15T10:20:00Z"     # ISO 8601 timestamp when added
    
    # Optional fields (only present if relevant)
    source_idea_id: "idea_007"           # Links global map entries to idea sources
    bibtex_key: "vaswani2017attention"   # Auto-generated if not provided
```

### Paper Field Definitions

| Field | Type | Required | Auto-Generated | Notes |
|-------|------|----------|---|-------|
| **title** | string | YES | No | Missing title → entry rejected |
| **authors** | list[str] | No | No | Format: "Last, F." or "Firstname Lastname" |
| **year** | int/null | No | No | Publication year |
| **venue** | string | No | No | Conference/Journal name |
| **doi** | string | No | No | Normalized on add: lowercase, stripped `https://doi.org/`, `http://doi.org/`, `doi:` prefixes |
| **url** | string | No | No | Paper URL (arXiv, publisher, etc.) |
| **semantic_scholar_id** | string | No | No | S2 paper ID, used for S2 API calls |
| **category** | string | No | No | Must match a `categories[].key` or empty string |
| **role** | string | No | No | **Valid values only**: `foundation`, `direct-competitor`, `method-component`, `evaluation`, `background` — invalid roles cause rejection |
| **relevance** | string | No | No | Brief description of why this paper is relevant |
| **abstract** | string | No | No | Paper abstract (omitted in summary mode to save tokens) |
| **verified** | bool | No | No | Default: `false`. Set `true` after OpenAlex check or manual verification. Once `true`, merge operations preserve it (cannot be un-verified) |
| **added_by** | string | No | Yes | Provenance tag recorded when added |
| **added_at** | string | No | Yes | ISO 8601 timestamp when added to map |
| **bibtex_key** | string | No | YES | Auto-generated using formula: `{surname}{year}{first_significant_title_word}` (e.g., `vaswani2017attention`). On collision, suffix appended: `vaswani2017attention_2` |
| **source_idea_id** | string | No | No | Global map only — links entries to idea sources for re-seeding |

### Automatic bibtex_key Generation Algorithm
```
bibtex_key = "{first_author_surname}{year}{first_non_stopword_in_title}"
```
- **First author surname**: Extracted from `authors[0]` (handles both "Last, F." and "Firstname Lastname" formats)
- **Year**: From `year` field
- **Title word**: First word in title not in stop words (`a`, `an`, `the`, `on`, `in`, `of`, `for`, `and`, `or`, `is`, `to`)
- **Stop-word example**: "The Power of Scale" → `power` (skips "The")
- **Fallback**: If any part missing, generates `paper_{MD5_hash_of_title[:8]}` (e.g., `paper_a1b2c3d4`)
- **Collision handling**: On duplicate key, auto-appends `_1`, `_2`, etc.

### Deduplication Strategy (On add_to_literature_map)
1. **Priority 1 (DOI exact match)**: Normalized DOI comparison (case-insensitive, stripped prefixes) → **merge** if match found
2. **Priority 2 (Title match)**: Normalized title (lowercase, stripped diacritics & punctuation, collapsed whitespace) → **merge** if match found
3. **No match** → **new entry** with auto-generated bibtex_key + collision suffix

**Merge behavior**: Fill empty fields only (never overwrite existing). Special rule: `verified=true` wins (once verified, cannot be un-verified).

### Read Modes (for token efficiency)

| Mode | Returns | Use Case |
|------|---------|----------|
| `summary` | `{title, year, venue, category, role, verified, bibtex_key}` per paper | Daily dashboard, citation lookups |
| `full` | All fields including `abstract`, `relevance`, `added_by`, `added_at` | Deep review, paper analysis |
| `competitors` | All fields for papers with `role == "direct-competitor"` | Experiment baseline research |
| `unverified` | All fields for papers with `verified == false` | Finding papers needing verification |
| `bib` | List of `bibtex_key` strings only | Bibliography lookups |
| `category:{key}` | All fields for papers with `category == "{key}"` | Related Work gap-fill per subsection |

### Valid Role Values
- **`foundation`**: Seminal papers that establish concepts (e.g., Transformer paper for attention work)
- **`direct-competitor`**: Methods directly competing with your approach (used to identify baselines)
- **`method-component`**: Papers proposing components you use (e.g., a loss function technique)
- **`evaluation`**: Papers establishing benchmarks, datasets, or metrics
- **`background`**: Supporting context papers not directly comparable

### File Operations
- **Atomicity**: Reads are lock-free (snapshot consistent); writes use exclusive flock + atomic temp→rename (never tears under concurrent Worker writes)
- **Auto-fields**: `bibtex_key`, `meta.last_updated`, `meta.total_papers` auto-filled/recalculated on every write
- **Lock file**: Sibling `.lock` file prevents corruption during concurrent writes

### Code References
- **Read/Write functions**: `/home/ubuntu/agent-ml-research/core/tools/literature.py` (lines 392-642)
- **Test fixtures**: `/home/ubuntu/agent-ml-research/tests/test_literature_map.py` (comprehensive examples)
- **Distillation integration**: `/home/ubuntu/agent-ml-research/core/tools/distill.py` (collects papers from literature_map as Layer 1)
- **Semantic Scholar mapping**: `/home/ubuntu/agent-ml-research/core/tools/semantic_scholar.py` (_normalize_paper function)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "355785e0-445d-40bf-8580-d7813d8c64d8",
  "isSidechain": true,
  "agentId": "a277383c324df4f8f",
  "requestId": "req_011CbDw6ei73CfAuu5zFCdTL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "832756fb-6eda-4e62-97b1-3c87e76e97ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01U1d3pGxJWttASGrAvvs1Ug",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 395,
      "cache_read_input_tokens": 66441,
      "output_tokens": 2164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 395
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 2164,
          "cache_read_input_tokens": 66441,
          "cache_creation_input_tokens": 395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 395,
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
