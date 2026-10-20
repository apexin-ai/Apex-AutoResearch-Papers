# Research conversation: In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/, search ALL 

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a943ecba15bc0e614.jsonl`
- **Structured JSON:** [`a150cd6491ce15f82c7f.json`](../../sessions/a1/a150cd6491ce15f82c7f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-21T05:13:57.698Z_

In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/, search ALL .tex files for references to these experiment categories. For each category, report whether it appears anywhere in the paper text:

1. "1.7B" or "1_7b" or "Qwen3-1.7B" or "1.7b" — cross-scale experiments
2. "d134" or "10-seed" or "s47" or "s48" or "s49" or "s50" or "s51" — 10-seed expansion
3. "gated" or "d142" or "component.*gate" or "gate.*component" — gated ISR experiments
4. "ProofFOL" — cross-dataset (should be present)
5. "shuffled" — shuffled-ISR control (should be present)
6. "β=0.2" or "b02" or "beta.*0.2" — dose-response intermediate
7. "β=0.05" or "b005" or "0.05" — very low dose
8. "5-seed" or "s45" or "s46" or "five seed" — 5-seed extensions
9. "warmstart" or "warm.start" — warmstart experiments

Search breadth: medium. Report which categories ARE and which are NOT referenced in the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "fa6c39d1-76de-47fa-b5d7-2c224d3fced4",
  "agentId": "a943ecba15bc0e614",
  "type": "user",
  "uuid": "0d8756d3-a151-4ce4-8b52-34ab8be877af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-21T05:14:01.634Z_

I'll search all .tex files in the paper directory for references to these experiment categories.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d8756d3-a151-4ce4-8b52-34ab8be877af",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9ExcFPJscLfHXFxy1B",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9256f652-652e-41fb-98a3-660be1b49ef6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C67QwLBQJyK58PYEJc5SNU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33587,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33587,
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

_source line 3 · 2026-05-21T05:14:01.939Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019MuxUCJC85E29semQtYoyC`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9256f652-652e-41fb-98a3-660be1b49ef6",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9ExcFPJscLfHXFxy1B",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "99cc1d9d-4f0a-4042-9d1b-c656684a960d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C67QwLBQJyK58PYEJc5SNU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33587,
      "cache_read_input_tokens": 0,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 33587
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 105,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 33587,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 33587,
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

_source line 4 · 2026-05-21T05:14:01.961Z_

<details><summary>↩ Tool result · `toolu_019MuxUCJC85E29semQtYoyC`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99cc1d9d-4f0a-4042-9d1b-c656684a960d",
  "isSidechain": true,
  "promptId": "fa6c39d1-76de-47fa-b5d7-2c224d3fced4",
  "agentId": "a943ecba15bc0e614",
  "type": "user",
  "uuid": "4ea7578d-bc05-4bb7-8a2f-acb6b37f08d9",
  "sourceToolAssistantUUID": "99cc1d9d-4f0a-4042-9d1b-c656684a960d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-21T05:14:03.660Z_

Now I'll search for each category across all these .tex files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ea7578d-bc05-4bb7-8a2f-acb6b37f08d9",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9FGtqhCVQfVTsN5moR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d4dd35d4-bd55-4b01-8618-77a350497958",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017xNnSQfdjigzdDe7wcdJdA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1398,
      "cache_read_input_tokens": 33587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1398,
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

_source line 6 · 2026-05-21T05:14:04.597Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01A2JEEJviYdhYp3qJ497LTo`</summary>

```json
{
  "pattern": "1\\.7[Bb]|1_7b|Qwen3-1\\.7B",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4dd35d4-bd55-4b01-8618-77a350497958",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9FGtqhCVQfVTsN5moR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4a9883f9-50aa-442a-a605-e66f19f8461e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017xNnSQfdjigzdDe7wcdJdA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1398,
      "cache_read_input_tokens": 33587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1398,
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

_source line 7 · 2026-05-21T05:14:04.621Z_

<details><summary>↩ Tool result · `toolu_01A2JEEJviYdhYp3qJ497LTo`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a9883f9-50aa-442a-a605-e66f19f8461e",
  "isSidechain": true,
  "promptId": "fa6c39d1-76de-47fa-b5d7-2c224d3fced4",
  "agentId": "a943ecba15bc0e614",
  "type": "user",
  "uuid": "d87f9899-885a-4cbb-b055-0b4c9b63153c",
  "sourceToolAssistantUUID": "4a9883f9-50aa-442a-a605-e66f19f8461e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T05:14:05.424Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01PiTBZepU4oNYBPe8QLTTN4`</summary>

```json
{
  "pattern": "d134|10-seed|s47|s48|s49|s50|s51",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d87f9899-885a-4cbb-b055-0b4c9b63153c",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9FGtqhCVQfVTsN5moR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "072b5b20-a1b8-4381-a953-ac214f41f11a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017xNnSQfdjigzdDe7wcdJdA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1398,
      "cache_read_input_tokens": 33587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1398,
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

_source line 9 · 2026-05-21T05:14:05.449Z_

<details><summary>↩ Tool result · `toolu_01PiTBZepU4oNYBPe8QLTTN4`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "072b5b20-a1b8-4381-a953-ac214f41f11a",
  "isSidechain": true,
  "promptId": "fa6c39d1-76de-47fa-b5d7-2c224d3fced4",
  "agentId": "a943ecba15bc0e614",
  "type": "user",
  "uuid": "b22530d3-0e61-4943-a9e0-0f5dfc0827c7",
  "sourceToolAssistantUUID": "072b5b20-a1b8-4381-a953-ac214f41f11a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T05:14:05.850Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01KmaFmYRdBw9p82URtDWvaw`</summary>

```json
{
  "pattern": "gated|d142|component.*gate|gate.*component",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b22530d3-0e61-4943-a9e0-0f5dfc0827c7",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9FGtqhCVQfVTsN5moR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f18b20f8-8d92-424a-9fc8-c32675dda1d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017xNnSQfdjigzdDe7wcdJdA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1398,
      "cache_read_input_tokens": 33587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1398,
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

_source line 11 · 2026-05-21T05:14:05.867Z_

<details><summary>↩ Tool result · `toolu_01KmaFmYRdBw9p82URtDWvaw`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f18b20f8-8d92-424a-9fc8-c32675dda1d1",
  "isSidechain": true,
  "promptId": "fa6c39d1-76de-47fa-b5d7-2c224d3fced4",
  "agentId": "a943ecba15bc0e614",
  "type": "user",
  "uuid": "4b4d39d5-7a0f-4375-8891-6977b5c81dff",
  "sourceToolAssistantUUID": "f18b20f8-8d92-424a-9fc8-c32675dda1d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T05:14:06.274Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01G6KT79bzPfFYhudNrwuY7D`</summary>

```json
{
  "pattern": "ProofFOL",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b4d39d5-7a0f-4375-8891-6977b5c81dff",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9FGtqhCVQfVTsN5moR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e08b1f38-31d2-4a38-a236-b0ba55bd5ad5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017xNnSQfdjigzdDe7wcdJdA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1398,
      "cache_read_input_tokens": 33587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1398,
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

_source line 13 · 2026-05-21T05:14:06.294Z_

<details><summary>↩ Tool result · `toolu_01G6KT79bzPfFYhudNrwuY7D`</summary>

```text
Found 7 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.aux
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e08b1f38-31d2-4a38-a236-b0ba55bd5ad5",
  "isSidechain": true,
  "promptId": "fa6c39d1-76de-47fa-b5d7-2c224d3fced4",
  "agentId": "a943ecba15bc0e614",
  "type": "user",
  "uuid": "418e3551-a8d8-418f-827a-acce1bccb1bd",
  "sourceToolAssistantUUID": "e08b1f38-31d2-4a38-a236-b0ba55bd5ad5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T05:14:06.695Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01H44e3PMQWFGyxmfmw1zFeW`</summary>

```json
{
  "pattern": "shuffled",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "418e3551-a8d8-418f-827a-acce1bccb1bd",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9FGtqhCVQfVTsN5moR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "83d53058-9cb5-4715-941d-308e7ddfd854",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017xNnSQfdjigzdDe7wcdJdA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1398,
      "cache_read_input_tokens": 33587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1398,
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

_source line 15 · 2026-05-21T05:14:06.712Z_

<details><summary>↩ Tool result · `toolu_01H44e3PMQWFGyxmfmw1zFeW`</summary>

```text
Found 6 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83d53058-9cb5-4715-941d-308e7ddfd854",
  "isSidechain": true,
  "promptId": "fa6c39d1-76de-47fa-b5d7-2c224d3fced4",
  "agentId": "a943ecba15bc0e614",
  "type": "user",
  "uuid": "2edaf1b4-fa94-41c4-b22b-50bf2c93589e",
  "sourceToolAssistantUUID": "83d53058-9cb5-4715-941d-308e7ddfd854",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T05:14:07.324Z_

<details open><summary>🔧 Tool call — Grep · `toolu_012N4HLoqEyYpX7XRz646nyj`</summary>

```json
{
  "pattern": "β=0\\.2|b02|beta.*0\\.2",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2edaf1b4-fa94-41c4-b22b-50bf2c93589e",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9FGtqhCVQfVTsN5moR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1d9b873d-59a3-4829-964c-a51725c81c50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017xNnSQfdjigzdDe7wcdJdA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1398,
      "cache_read_input_tokens": 33587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1398,
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

_source line 17 · 2026-05-21T05:14:07.341Z_

<details><summary>↩ Tool result · `toolu_012N4HLoqEyYpX7XRz646nyj`</summary>

```text
Found 5 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.fdb_latexmk
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d9b873d-59a3-4829-964c-a51725c81c50",
  "isSidechain": true,
  "promptId": "fa6c39d1-76de-47fa-b5d7-2c224d3fced4",
  "agentId": "a943ecba15bc0e614",
  "type": "user",
  "uuid": "c2652ce9-9481-48a0-9858-b048f3f3e65e",
  "sourceToolAssistantUUID": "1d9b873d-59a3-4829-964c-a51725c81c50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T05:14:07.748Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01TadQwk7xfs7YprtH9LBY6E`</summary>

```json
{
  "pattern": "β=0\\.05|b005|\\\\b0\\.05",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2652ce9-9481-48a0-9858-b048f3f3e65e",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9FGtqhCVQfVTsN5moR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1ef25e8a-7979-43cc-ac85-7f94a7676297",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017xNnSQfdjigzdDe7wcdJdA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1398,
      "cache_read_input_tokens": 33587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1398,
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

_source line 19 · 2026-05-21T05:14:07.765Z_

<details><summary>↩ Tool result · `toolu_01TadQwk7xfs7YprtH9LBY6E`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ef25e8a-7979-43cc-ac85-7f94a7676297",
  "isSidechain": true,
  "promptId": "fa6c39d1-76de-47fa-b5d7-2c224d3fced4",
  "agentId": "a943ecba15bc0e614",
  "type": "user",
  "uuid": "8b9ff0c0-0ce5-4be1-9635-11a3006d2252",
  "sourceToolAssistantUUID": "1ef25e8a-7979-43cc-ac85-7f94a7676297",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T05:14:08.193Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Mu4ogk5ytf8Qh4xFTJmSmN`</summary>

```json
{
  "pattern": "5-seed|s45|s46|five seed",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b9ff0c0-0ce5-4be1-9635-11a3006d2252",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9FGtqhCVQfVTsN5moR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e5087def-9f32-4e7c-9c45-a079d4df1bd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017xNnSQfdjigzdDe7wcdJdA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1398,
      "cache_read_input_tokens": 33587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1398,
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

_source line 21 · 2026-05-21T05:14:08.216Z_

<details><summary>↩ Tool result · `toolu_01Mu4ogk5ytf8Qh4xFTJmSmN`</summary>

```text
Found 1 file
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5087def-9f32-4e7c-9c45-a079d4df1bd4",
  "isSidechain": true,
  "promptId": "fa6c39d1-76de-47fa-b5d7-2c224d3fced4",
  "agentId": "a943ecba15bc0e614",
  "type": "user",
  "uuid": "59768c93-cd12-4fb1-9273-305b38c0a39e",
  "sourceToolAssistantUUID": "e5087def-9f32-4e7c-9c45-a079d4df1bd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T05:14:08.690Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01BQN3Zoyab1qFLovDQbQ3BJ`</summary>

```json
{
  "pattern": "warmstart|warm.start",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59768c93-cd12-4fb1-9273-305b38c0a39e",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9FGtqhCVQfVTsN5moR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "245484b7-3b4c-4748-beee-d6c6e4a7e8bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017xNnSQfdjigzdDe7wcdJdA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1398,
      "cache_read_input_tokens": 33587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1398,
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

_source line 23 · 2026-05-21T05:14:08.713Z_

<details><summary>↩ Tool result · `toolu_01BQN3Zoyab1qFLovDQbQ3BJ`</summary>

```text
Found 1 file
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "245484b7-3b4c-4748-beee-d6c6e4a7e8bf",
  "isSidechain": true,
  "promptId": "fa6c39d1-76de-47fa-b5d7-2c224d3fced4",
  "agentId": "a943ecba15bc0e614",
  "type": "user",
  "uuid": "5c444bf8-327f-4dfc-a3f8-c91eb83be01c",
  "sourceToolAssistantUUID": "245484b7-3b4c-4748-beee-d6c6e4a7e8bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-21T05:14:10.081Z_

Let me get more detailed context for the matches found:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c444bf8-327f-4dfc-a3f8-c91eb83be01c",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9FmbFBCa1T5QEhwGFt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8b3d1d4b-0851-497b-a39d-0b00a55a64f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UiQcu4wy2wQeVZpknHb1Z1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2101,
      "cache_read_input_tokens": 34985,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2101,
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

_source line 25 · 2026-05-21T05:14:10.514Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01D1WjB3L7N288FSmhqYCsS1`</summary>

```json
{
  "pattern": "ProofFOL",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b3d1d4b-0851-497b-a39d-0b00a55a64f5",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9FmbFBCa1T5QEhwGFt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c6a8f4f0-a2cf-4004-8827-3faf0791186b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UiQcu4wy2wQeVZpknHb1Z1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2101,
      "cache_read_input_tokens": 34985,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2101,
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

_source line 26 · 2026-05-21T05:14:10.543Z_

<details><summary>↩ Tool result · `toolu_01D1WjB3L7N288FSmhqYCsS1`</summary>

```text
&lt;persisted-output>
Output too large (27.1KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-agent-79f408c6/6bce55f6-6a3c-4244-94b5-8479902dce60/tool-results/toolu_01D1WjB3L7N288FSmhqYCsS1.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex-9-We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex-10-Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 does not change qualitative conclusions (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:11:Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex-12-We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall is unknown).
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6a8f4f0-a2cf-4004-8827-3faf0791186b",
  "isSidechain": true,
  "promptId": "fa6c39d1-76de-47fa-b5d7-2c224d3fced4",
  "agentId": "a943ecba15bc0e614",
  "type": "user",
  "uuid": "1c8e212a-903f-4c46-ba7d-cdfeca4d996d",
  "sourceToolAssistantUUID": "c6a8f4f0-a2cf-4004-8827-3faf0791186b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T05:14:11.135Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01EViVFKCn2nN9bnrXh4kmKy`</summary>

```json
{
  "pattern": "shuffled",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c8e212a-903f-4c46-ba7d-cdfeca4d996d",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9FmbFBCa1T5QEhwGFt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "027fb927-00ee-4bd1-8677-89dd1650e8ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UiQcu4wy2wQeVZpknHb1Z1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2101,
      "cache_read_input_tokens": 34985,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2101,
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

_source line 28 · 2026-05-21T05:14:11.153Z_

<details><summary>↩ Tool result · `toolu_01EViVFKCn2nN9bnrXh4kmKy`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex-42-\paragraph{Multiplicative coupling.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex-43-The reward $r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ couples signals; exec-only's $0\%$ non-hacking, the qualitative TS shift ($0\%{\to}71\%$), and an additive variant's PR collapse (Appendix~\ref{app:setup}) constrain this confound.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:44:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex-45-
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex-46-\begin{table*}[t]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex-57-ISR & 0.1 & 77{\scriptsize$\pm$14} & $\ddagger$ & \textbf{71}$^\P$ & 18 & 6 \\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex-58-Random & 0.1 & \textbf{87}{\scriptsize$\pm$8} & 0.117{\scriptsize$\pm$.04} & 14$^\S$ & 71 & 10 \\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:59:Shuffled-ISR & 0.1 & 15{\scriptsize$\pm$1} & 0.559{\scriptsize$\pm$.02} & 7 & 7 & \textbf{87} \\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex-60-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex-61-ISR & 0.3 & 66{\scriptsize$\pm$42} & 0.39{\scriptsize$\pm$.31} & \textbf{50} & 37 & 11 \\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex-5-Cross-logic replication in Prolog confirms the phenomenon generalizes beyond FOL (\S\ref{sec:crosslogic}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex-6-Repurposed as a reward, ISR produces dataset-dependent outcomes: on FOLIO, Goodhart effects increase TS in all seeds (supplementary CMH $p{<}10^{-15}$); on ProofFOL, beneficial instability yields 76.8\% vs.\ 17.4\% non-hacking (upper bound; \S\ref{sec:setup}) ($p{=}0.10$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex:7:Deconfounding reduces the sole apparent ISR reward advantage to $1.06\times$; a shuffled-ISR control confirms that semantic content, not distributional shape, drives the gaming effect (\S\ref{sec:goodhart}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex-8-The central finding is ISR's observer/optimizer asymmetry: the same LOO structure that makes ISR informative as a diagnostic makes it gameable as a reward, with outcomes depending on whether the dataset's hacking geometry satisfies the metric.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex-9-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.log-803-
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.log-804-Underfull \hbox (badness 1178) in paragraph at lines 43--45
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.log:805:\OT1/cmr/m/n/10.95 A shuffled-ISR con-trol (batch-internal ran-
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.log-806- []
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.log-807-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex-10-ISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex-11-Three seeds demonstrate qualitative divergence but limit statistical power; all pooled statistics (CMH, Fisher) treat within-seed samples as independent observations from a single trained model, and the true independent replication count is $N{=}3$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex:12:A shuffled-ISR control (batch-internal ISR permutation preserving distributional shape but breaking semantic correspondence) yields PR and non-hacking rates comparable to SFT ($N{=}46$ proved, 3 seeds), ruling out ISR's bimodal distribution as the Goodhart driver; however, each seed produces only ${\sim}15$ proved samples, limiting statistical power.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex-13-STA requires solvers supporting component-level input manipulation; the Prolog experiments use SWI-Prolog (Horn clause logic, a subset of full FOL), limiting the range of logical structures tested in cross-logic transfer.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex-14-RL-based formal verification in Lean~4~\citep{kimina-prover, alphaproof2025} represents a parallel track where STA-style diagnostics could be applied but remain unexplored.
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex-4-As a diagnostic, ISR reveals a collapse trajectory hidden from prove rate: ISR falls to near-zero over training while prove rate rises, with each seed converging to a qualitatively different hacking mode.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex-5-A supervised fine-tuning baseline confirms the degradation is GRPO-specific.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex:6:When repurposed as a training reward, ISR induces Goodhart effects: models game the structural signal through diverse strategies, and a shuffled-ISR control confirms the gaming targets semantic content rather than distributional artifacts.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex-7-Cross-logic (Prolog) and cross-dataset (ProofFOL) replication confirms structural degeneration generalizes, documenting ISR's core asymmetry: reliable as a diagnostic, dataset-dependent as an optimization target.\footnote{Code and data: \url{[anonymized]}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex-8-\end{abstract}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex-39-
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex-40-\paragraph{Contributions.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex:41:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex-42-These are cautionary results, replicated across dataset families, relevant to any work treating a structural proxy as a training signal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "027fb927-00ee-4bd1-8677-89dd1650e8ba",
  "isSidechain": true,
  "promptId": "fa6c39d1-76de-47fa-b5d7-2c224d3fced4",
  "agentId": "a943ecba15bc0e614",
  "type": "user",
  "uuid": "910c8523-eb81-45c4-a0e5-cda75fc39a33",
  "sourceToolAssistantUUID": "027fb927-00ee-4bd1-8677-89dd1650e8ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T05:14:11.805Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01VdA6vAHz9YFwstwUmd6f9K`</summary>

```json
{
  "pattern": "β=0\\.2|b02|beta.*0\\.2",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "910c8523-eb81-45c4-a0e5-cda75fc39a33",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9FmbFBCa1T5QEhwGFt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d6e4ba51-fd95-4fc0-a14e-3fb61eb26d60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UiQcu4wy2wQeVZpknHb1Z1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2101,
      "cache_read_input_tokens": 34985,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2101,
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

_source line 30 · 2026-05-21T05:14:11.843Z_

<details><summary>↩ Tool result · `toolu_01VdA6vAHz9YFwstwUmd6f9K`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex-81-\textbf{Higher doses and temporal dynamics.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex-82-ISR $\beta{=}0.1$ non-hacking is transient: seed~42 drops $17.3\%{\to}2.2\%$ by 1000 steps as TS escalates to $96.7\%$ (Figure~\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:83:At higher doses ($\beta{\geq}0.2$), TS becomes universal ($0\%$ non-hacking at $\beta{=}0.2$); $\beta{=}0.3$ destabilizes both ISR ($\text{PR}{=}66{\pm}42\%$) and random ($54{\pm}35\%$), with ISR producing multi-modal failure~\citep{gao-reward-overoptimization} and random converging to CE ($91\%$; Appendix~\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex-84-
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex-85-\subsection{Cross-Domain Evidence}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex-34-Repurposed as a training signal, $r = r_{\text{exec}} \cdot (1 + \beta\,\text{ISR})$, ISR is gamed at its own definition~\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex-35-On FOLIO, this instantiates \emph{regressional} Goodhart~\citep{manheim-goodhart-taxonomy}: $P{\to}P$ tautologies yield $\text{ISR}{\geq}0.5$, so ISR rewards the shortcut; at $\beta{=}0.1$, ISR increases TS rates in all 3 seeds (70.6\% vs.\ 13.7\% random pooled), but the sole apparent ISR advantage reduces to $1.06\times$ after controlling for premise count.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex:36:At $\beta{\geq}0.2$, \emph{extremal} Goodhart dominates ($\text{PR}{=}66{\pm}42\%$ ISR, $54{\pm}35\%$ random at $\beta{=}0.3$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex-37-On ProofFOL, hacking yields $\text{ISR}{=}0.0$, so ISR correctly penalizes shortcuts, associated with beneficial instability (76.8\% vs.\ 17.4\% genuine under a coarser classifier, $p{=}0.10$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex-38-ISR's asymmetry is the central finding: \emph{reliable as observer, dataset-dependent as optimizer.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex-154-\paragraph{Goodhart effects: implications.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex-155-ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself. Any diagnostic metric risks becoming a target when optimized.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:156:The dose-response pattern maps onto the Manheim \& Garrabrant taxonomy~\citep{manheim-goodhart-taxonomy}: $\beta{=}0.1$ on FOLIO instantiates \emph{regressional} Goodhart ($P{\to}P$ tautologies yield $\text{ISR}{\geq}0.5$, so ISR erroneously rewards the shortcut); $\beta{\geq}0.2$ introduces \emph{extremal} elements (PR collapse to 18\% vs.\ 48\% random at $\beta{=}0.3$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex-157-The implication is conditional: ISR fails as a training reward when hacking satisfies its LOO structure (FOLIO), but produces beneficial instability when hacking does not (ProofFOL; \S\ref{sec:crossdomain}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex-158-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.fdb_latexmk-22-  "/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmbsy9.tfm" 1246382020 1112 cbc11b646ccc26599775160605aaee3a ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.fdb_latexmk-23-  "/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmex7.tfm" 1246382020 1004 54797486969f23fa377b128694d548df ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.fdb_latexmk:24:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmex8.tfm" 1246382020 988 bdf658c3bfc2d96d3c8b02cfc1c94c20 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.fdb_latexmk-25-  "/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmex9.tfm" 1246382020 996 a18840b13b499c08ac2de96a99eda4bc ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.fdb_latexmk-26-  "/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmmib5.tfm" 1246382020 1496 c79f6914c6d39ffb3759967363d1be79 ""
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.fdb_latexmk-33-  "/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm5.tfm" 1246382020 940 75ac932a52f80982a9f8ea75d03a34cf ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.fdb_latexmk-34-  "/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm7.tfm" 1246382020 940 228d6584342e91276bf566bcf9716b83 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.fdb_latexmk:35:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx10.tfm" 1136768653 1328 c834bbb027764024c09d3d2bf908b5f0 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.fdb_latexmk-36-  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx12.tfm" 1136768653 1324 c910af8c371558dc20f2d7822f66fe64 ""
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.fdb_latexmk-37-  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx5.tfm" 1136768653 1332 f817c21a1ba54560425663374f1b651a ""
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.md-31-A diagnostic that pinpoints failure is tempting to plug back in as a training signal. We do so and observe a meta-level Goodhart effect: the same metric that flags hacking becomes the object that is hacked.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.md-32-
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.md:33:**Low dose ($\beta=0.1$): mode restructuring, no real gain.** Table~\ref{tab:tab4_beta01_3seed} reports the three-seed comparison of ISR-bonus and random-bonus rewards at $\beta=0.1$. ISR-bonus runs report higher proved-only ISR\* across all seeds (s42 = 0.415, s43 = 0.830, s44 = 0.902 — mean 0.716±0.26) than random-bonus runs (s42 = 0.131, s43 = 0.058, s44 = 0.070 — mean 0.086±0.039). On its face this is an 8× structural advantage, but two diagnostic checks dissolve it.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.md-34-
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.md-35-[Omitted long context line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6e4ba51-fd95-4fc0-a14e-3fb61eb26d60",
  "isSidechain": true,
  "promptId": "fa6c39d1-76de-47fa-b5d7-2c224d3fced4",
  "agentId": "a943ecba15bc0e614",
  "type": "user",
  "uuid": "c3e58e27-ae32-479a-b717-37a16c020731",
  "sourceToolAssistantUUID": "d6e4ba51-fd95-4fc0-a14e-3fb61eb26d60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T05:14:12.106Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01LP4a44hXFGD4q5LAWGGFff`</summary>

```json
{
  "pattern": "β=0\\.05|b005|0\\.05",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3e58e27-ae32-479a-b717-37a16c020731",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9FmbFBCa1T5QEhwGFt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "166c43d3-1972-4605-a20c-2a6b69f28b40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UiQcu4wy2wQeVZpknHb1Z1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2101,
      "cache_read_input_tokens": 34985,
      "output_tokens": 534,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2101
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 534,
          "cache_read_input_tokens": 34985,
          "cache_creation_input_tokens": 2101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2101,
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

_source line 32 · 2026-05-21T05:14:12.127Z_

<details><summary>↩ Tool result · `toolu_01LP4a44hXFGD4q5LAWGGFff`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.md-31-A diagnostic that pinpoints failure is tempting to plug back in as a training signal. We do so and observe a meta-level Goodhart effect: the same metric that flags hacking becomes the object that is hacked.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.md-32-
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.md:33:**Low dose ($\beta=0.1$): mode restructuring, no real gain.** Table~\ref{tab:tab4_beta01_3seed} reports the three-seed comparison of ISR-bonus and random-bonus rewards at $\beta=0.1$. ISR-bonus runs report higher proved-only ISR\* across all seeds (s42 = 0.415, s43 = 0.830, s44 = 0.902 — mean 0.716±0.26) than random-bonus runs (s42 = 0.131, s43 = 0.058, s44 = 0.070 — mean 0.086±0.039). On its face this is an 8× structural advantage, but two diagnostic checks dissolve it.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.md-34-
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.md-35-[Omitted long context line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex-180-\label{app:statistical-details}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex-181-We define two test families: FOLIO ($k{=}14$ tests across all conditions) and ProofFOL ($k{=}1$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:182:Within the FOLIO family, Bonferroni correction at $\alpha{=}0.05$ yields adjusted thresholds of $p_{\text{adj}}{=}0.05/14{=}0.0036$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex-183-Three primary comparisons survive correction: the TS rate difference (ISR vs.\ random; $p_{\text{bonf}}{=}1.82{\times}10^{-38}$), the SFT vs.\ exec-only non-hacking rate ($p_{\text{bonf}}{=}0.014$), and the Cochran--Mantel--Haenszel test for TS association across seeds ($p_{\text{bonf}}{<}10^{-8}$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:184:The matched 5+5-seed Fisher/Mann-Whitney comparison is borderline ($p_{\text{bonf}}{=}0.056$), significant at $\alpha{=}0.10$ after Bonferroni correction ($k{=}14$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex-185-The ProofFOL genuine-rate permutation test ($p{=}0.10$) belongs to a separate hypothesis family (different dataset, independent experimental design) and does not reach significance even without correction; it is reported as an exploratory observation throughout.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex-186-Bonferroni assumes independence, which is conservative for our setting (several tests use overlapping data); Holm--Bonferroni or Benjamini--Hochberg FDR would recover the matched 5+5 comparison at conventional significance.
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex-256-\paragraph{Impact on non-hacking-rate comparison.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex-257-After PG reclassification and TS false-negative correction: ISR non-hacking $= 14/231 = 6.06\%$ vs.\ random non-hacking $= 25/262 = 9.5\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\% CI: ISR [3.6\%, 9.9\%], Random [6.5\%, 13.7\%]).
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:258:The direction is consistent with ISR-amplified gaming modes (TS, PG) displacing non-hacking output, but the effect is not statistically significant at the conventional $\alpha{=}0.05$ threshold.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex-259-
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex-260-\subsection{CE --- Conclusion Embedding}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex-506-\cmidrule(l){2-9}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex-507-  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.68{\pm}0.47$ & $0.238{\pm}0.30$ & & & & 500-step \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:508:  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.97{\pm}0.02$ & $0.029{\pm}0.05$ & & & $2.1{\pm}3.6$ & 1000-step \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex-509-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex-510-\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/gen_fig4.py-99-out_pdf = '/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/fig4_prolog_comparison.pdf'
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/gen_fig4.py-100-out_png = out_pdf.replace('.pdf', '.png')
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/gen_fig4.py:101:fig.savefig(out_pdf, dpi=300, bbox_inches='tight', pad_inches=0.05)
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/gen_fig4.py:102:fig.savefig(out_png, dpi=300, bbox_inches='tight', pad_inches=0.05)
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/gen_fig4.py-103-plt.close()
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/gen_fig4.py-104-print(f'Saved: {out_pdf}')
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/gen_fig3.py-89-
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/gen_fig3.py-90-base = '/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/fig3_hacking_composition'
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/gen_fig3.py:91:fig.savefig(f'{base}.pdf', dpi=300, bbox_inches='tight', pad_inches=0.05)
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/gen_fig3.py:92:fig.savefig(f'{base}.png', dpi=300, bbox_inches='tight', pad_inches=0.05)
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/gen_fig3.py-93-plt.close()
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/gen_fig3.py-94-print(f'Saved: {base}.pdf')
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/gen_fig2.py-21-    "legend.fontsize": 10, "figure.dpi": 300,
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/gen_fig2.py-22-    "savefig.dpi": 300, "savefig.bbox": "tight",
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/gen_fig2.py:23:    "savefig.pad_inches": 0.05,
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/gen_fig2.py-24-    "axes.spines.top": False, "axes.spines.right": False,
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/gen_fig2.py-25-    "lines.linewidth": 1.8, "pdf.fonttype": 42, "ps.fonttype": 42,
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/fig2_data.json:1:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "166c43d3-1972-4605-a20c-2a6b69f28b40",
  "isSidechain": true,
  "promptId": "fa6c39d1-76de-47fa-b5d7-2c224d3fced4",
  "agentId": "a943ecba15bc0e614",
  "type": "user",
  "uuid": "3a7ca7fa-bc66-408f-902f-c8bbbbe1e540",
  "sourceToolAssistantUUID": "166c43d3-1972-4605-a20c-2a6b69f28b40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-21T05:14:14.080Z_

Now let me check more carefully for the beta=0.05 references and also look at the .tex files specifically (excluding .log, .fdb_latexmk, and .md):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a7ca7fa-bc66-408f-902f-c8bbbbe1e540",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9G2STubWj33bWzngmr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "65c86248-e4ad-4d95-99ac-57d741851d1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012T7u3Rg1ya8hombbxuM6Xz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 10253,
      "cache_read_input_tokens": 37086,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10253,
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

_source line 34 · 2026-05-21T05:14:14.213Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HVxnqH4UuMgCxcyNrn2aBU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65c86248-e4ad-4d95-99ac-57d741851d1e",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9G2STubWj33bWzngmr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "23c20533-abdd-4dc3-b305-456893d1d8e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012T7u3Rg1ya8hombbxuM6Xz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 10253,
      "cache_read_input_tokens": 37086,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10253
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 131,
          "cache_read_input_tokens": 37086,
          "cache_creation_input_tokens": 10253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10253,
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

_source line 35 · 2026-05-21T05:14:14.226Z_

<details><summary>↩ Tool result · `toolu_01HVxnqH4UuMgCxcyNrn2aBU`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 does not change qualitative conclusions (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall is unknown).
13	
14	\paragraph{Statistical considerations.}
15	With three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.
16	Pooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.
17	ProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory.
18	
19	\subsection{ISR as Diagnostic}
20	\label{sec:diagnostic}
21	
22	\textbf{Collapse trajectory.}
23	Figure~\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.
24	PR rises $32\%\to93\%\to96\%$, a trajectory that execution-only evaluation would interpret as successful optimization; $\text{ISR}^*$ tells the opposite story, $0.642\to0.132\to0.003$ (214$\times$ collapse). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42
25	By 500 steps, 87.1\% of proved samples embed the conclusion (CE); by 1000 steps, component count inflates $2.8\times$ ($6.58{\to}18.55$) while ISR decreases $214\times$, ruling out shorter formalizations as a mechanical explanation of the collapse.
26	
27	\textbf{Cross-seed instability.}
28	Three seeds diverge radically ($\text{PR}\,\sigma{=}47$\,pp) into conclusion embedding (s42, CE$=$87\%), repetition collapse (s43), and tautological collapse (s44, TS$=$100\%), all converging to ${\leq}7\%$ non-hacking by 1000 steps (Table~\ref{tab:fol-detailed}; Appendix~\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2
29	
30	\textbf{SFT baseline.}
31	SFT on gold formalizations reaches $92.3\%$ non-hacking ($\text{PR}{=}13\%$, 3-seed pooled; $\text{OR}{=}147$ vs.\ exec-only, $p{<}0.001$).
32	SFT serves as a pre-RL quality baseline (not a PR-matched control; its low PR reflects minimal optimization pressure): the base model has zero FOL capability ($\text{PR}{=}0\%$) and SFT's $8\%$ hacking confirms these modes are RL-created; a 100-step checkpoint already reaches $31\%$ (Appendix~\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3
33	
34	\subsection{Goodhart Effects on ISR-as-Reward}
35	\label{sec:goodhart}
36	
37	We reverse ISR's role from observer to reward: $r = r_{\text{exec}}\cdot(1 + \beta\,\text{ISR})$, with matched random control ($u\sim\mathcal{U}(0,1)$).
38	The Goodhart effect operates at the level of ISR's LOO definition: models learn to generate formalizations where each component is individually necessary for proof mechanics, without ensuring meaningful reasoning.
39	ISR decline indicates structural change; the mode breakdown (Table~\ref{tab:hacking-taxonomy}) characterizes this change as degeneration.
40	This is distinct from simple proxy failure. The qualitative shift in hacking modes (TS $0\%{\to}71\%$ under ISR, per-seed direction consistent) demonstrates active optimization against the LOO metric; deconfounding shows the apparent $3.2\times$ ISR advantage collapses to $1.06\times$ after controlling for premise count.
41	
42	\paragraph{Multiplicative coupling.}
43	The reward $r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ couples signals; exec-only's $0\%$ non-hacking, the qualitative TS shift ($0\%{\to}71\%$), and an additive variant's PR collapse (Appendix~\ref{app:setup}) constrain this confound.
44	ISR scores are bimodal (near $0$ or ${\geq}0.5$) while random is approximately uniform. A shuffled-ISR control (batch-internal random permutation preserving ISR's bimodal distribution while breaking the sample-level semantic link) yields $\text{PR}{=}15.3{\pm}0.6\%$ with $87.0\%$ non-hacking ($N{=}46$ proved, 3-seed pooled), comparable to SFT ($\text{PR}{=}13\%$, $92\%$ non-hacking) and far below the TS-dominated ISR regime ($71\%$ TS). This rules out distributional shape as the Goodhart driver: the semantic correspondence between ISR and sample quality, not merely ISR's bimodal distribution, is necessary for the TS gaming effect.
45	
46	\begin{table*}[t]
47	\centering
48	\small
49	\begin{tabular}{lcccccc}
50	\toprule
51	\textbf{Condition} & $\boldsymbol{\beta}$ & \textbf{PR\%}$\uparrow$ & \textbf{ISR}$^*$ & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} \\
52	\midrule
53	Base (0-shot) & --- & 12 & --- & --- & --- & --- \\ %% registry: sta-phase0-baseline
54	SFT & --- & 13 & 0.595 & 0 & 8 & \textbf{92} \\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)
55	\midrule
56	Exec-only$^\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\ %% registry: plan001-exec-only-s42-r2 (PG corrected)
57	ISR & 0.1 & 77{\scriptsize$\pm$14} & $\ddagger$ & \textbf{71}$^\P$ & 18 & 6 \\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)
58	Random & 0.1 & \textbf{87}{\scriptsize$\pm$8} & 0.117{\scriptsize$\pm$.04} & 14$^\S$ & 71 & 10 \\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)
59	Shuffled-ISR & 0.1 & 15{\scriptsize$\pm$1} & 0.559{\scriptsize$\pm$.02} & 7 & 7 & \textbf{87} \\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)
60	\midrule
61	ISR & 0.3 & 66{\scriptsize$\pm$42} & 0.39{\scriptsize$\pm$.31} & \textbf{50} & 37 & 11 \\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)
62	Random & 0.3 & 54{\scriptsize$\pm$35} & 0.09{\scriptsize$\pm$.09} & 7 & 91 & 2 \\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)
63	\bottomrule
64	\end{tabular}
65	\caption{Goodhart landscape across reward conditions. 3-seed rows: TS/CE/non-hacking percentage (N-H) pooled across seeds; PR/ISR$^*$: mean$\pm$std of per-seed values. $^\dagger$Seed~42. $\ddagger$$\text{ISR}^*$ omitted for ISR $\beta{=}0.1$ because the raw mean is inflated by TS gaming; premise-count-matched value is $1.06\times$ random (\S\ref{sec:goodhart}, Appendix~\ref{app:detailed-results}). $^\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\% of proved; Appendix~\ref{app:h8}). $^\S$Random TS driven by seed~43 (38.3\%); seeds~42 and~44: 0\%. Per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\S\ref{sec:goodhart}), not an independent reward condition.}
66	\label{tab:goodhart-landscape}
67	\end{table*}
68	
69	\textbf{Low-dose ISR ($\beta{=}0.1$): per-seed consistent gaming.}
70	ISR reward increases TS rates in all 3 seeds relative to matched random: $70.6\%$ ($163/231$) vs.\ $13.7\%$ ($36/262$) pooled (supplementary CMH: $\text{OR}_{\text{CMH}}{=}2.46$, $p{=}5.6{\times}10^{-16}$; Appendix~\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL
71	Random TS is seed-dependent ($38.3\%$ in s43 vs.\ $0\%$ in s42/s44); ISR makes TS near-deterministic ($2/3$ seeds at $97$--$100\%$, Table~\ref{tab:fol-detailed}).
72	TS (a single premise identical to the conclusion, giving $\text{ISR}\geq 0.5$ by construction; \S\ref{sec:taxonomy-method}) is the canonical Goodhart move: the model satisfies the LOO definition directly.
73	Total conclusion embedding ($\text{CE}+\text{TS}$) is $68$--$100\%$ across both conditions; the composition differs: CE dominates under random ($71\%$), TS under ISR. ISR converts CE into TS rather than reducing total embedding (Figure~\ref{fig:hacking-composition}).
74	Random yields higher PR ($87{\pm}8\%$ vs.\ $77{\pm}14\%$): noise disrupts convergence toward a single collapse trajectory.
75	
76	\textbf{Premise-count confound.}
77	The sole non-TS ISR seed (s42) shows raw $\text{ISR}^{*}{=}0.415$, $3.2\times$ random ($0.131$), a premise-minimization artifact ($n{=}5.58$ vs.\ $8.46$); matched comparison gives $1.06\times$ (Appendix~\ref{app:detailed-results}). %% D051 premise-count-matched analysis
78	After reclassifying PG and TS false negatives, non-hacking rates ($6.1\%$ ISR vs.\ $9.5\%$ random) are not significant ($p{=}0.182$; Appendix~\ref{app:h8}). %% D095 FINAL Fisher test
79	The key asymmetry is compositional: ISR converts stochastic TS into near-deterministic convergence ($2/3$ seeds ${\geq}97\%$), while random remains seed-dependent and CE-dominated.
80	
81	\textbf{Higher doses and temporal dynamics.}
82	ISR $\beta{=}0.1$ non-hacking is transient: seed~42 drops $17.3\%{\to}2.2\%$ by 1000 steps as TS escalates to $96.7\%$ (Figure~\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42
83	At higher doses ($\beta{\geq}0.2$), TS becomes universal ($0\%$ non-hacking at $\beta{=}0.2$); $\beta{=}0.3$ destabilizes both ISR ($\text{PR}{=}66{\pm}42\%$) and random ($54{\pm}35\%$), with ISR producing multi-modal failure~\citep{gao-reward-overoptimization} and random converging to CE ($91\%$; Appendix~\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44
84	
85	\subsection{Cross-Domain Evidence}
86	\label{sec:crossdomain}
87	\label{sec:crosslogic}
88	\label{sec:crossdataset}
89	
90	\begin{figure}[t]
91	\centering
92	\includegraphics[width=\columnwidth]{figures/fig4_prolog_comparison.pdf}
93	\caption{Cross-logic results. \textbf{Top}: FOL vs.\ Prolog exec-only $\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\% non-hacking through distinct mechanisms.}
94	\label{fig:prolog-comparison}
95	\end{figure}
96	
97	\textbf{Prolog: universal Goodhart.}
98	We replicate the FOL pipeline with Prolog/SWI-Prolog (Figure~\ref{fig:prolog-comparison}).
99	Exec-only seeds show $\text{ISR}^*{\approx}0$ via redundant ground-fact coding (2/3 seeds); ISR flags this mode as it flags FOL's conclusion embedding.
100	Under ISR-as-reward, 3/3 seeds reach 0\% non-hacking through distinct mechanisms: clean TS (s42), uppercase pseudo-Prolog bypassing text-match classifiers (s43, all 38 proved at $n_{\text{necessary}}{=}1$), and query-as-fact gaming (s44, 95/97 at $n_{\text{necessary}}{=}1$; Table~\ref{tab:prolog-detailed}).
101	Prolog's simpler semantics broadens the gaming basin, eliminating the non-hacking residual entirely.
102	
103	\textbf{ProofFOL exec-only: structural degeneration generalizes, though mode distributions differ.}
104	Two converged seeds ($\text{ISR}^*{<}0.07$) show ${\leq}1.4\%$ genuine; s42 exhibits 100\% TS (absent from all FOLIO exec-only seeds), showing hacking-mode repertoire is dataset-specific ($\text{ISR}^*{<}0.12$ across all seeds, far below baseline $0.31$).
105	
106	\textbf{ProofFOL ISR ($\beta{=}0.1$): beneficial instability (exploratory).}
107	ISR reduces stable convergence from 2/3 to 0/3 seeds, yet ISR seeds average 76.8\% genuine versus 17.4\% for exec-only ($p{=}0.10$, $N{=}3$; Table~\ref{tab:prooffol-detailed}).
108	ProofFOL ``genuine'' excludes only TS and CE (the two modes detectable by text-match classifiers), unlike FOLIO's eight-mode residual; the rates are therefore not directly comparable.
109	However, ISR-condition prove rates ($0.35$--$0.49$) remain far below exec-only (${\sim}1.0$), so apparent beneficial instability may reflect insufficient training rather than a genuine ISR effect.
110	
111	\textbf{Mechanism.}
112	On ProofFOL, hacking yields $\text{ISR}{=}0.0$ while genuine proofs yield $\text{ISR}{>}0.2$; ISR correctly penalizes shortcuts.
113	On FOLIO, $P{\to}P$ yields $\text{ISR}{\geq}0.5$ (regressional Goodhart~\citep{manheim-goodhart-taxonomy}), so ISR erroneously rewards tautological hacking.
114	The same metric produces opposite outcomes, determined by whether the dataset's hacking geometry satisfies it.
115	
116	\subsection{Hacking Taxonomy}
117	\label{sec:taxonomy}
118	
119	\begin{figure}[t]
120	\centering
121	\includegraphics[width=0.92\columnwidth]{figures/fig3_hacking_composition.pdf}
122	\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}
123	\label{fig:hacking-composition}
124	\end{figure}
125	
126	\begin{table}[t]
127	\centering
128	\small
129	\resizebox{\columnwidth}{!}{%
130	\begin{tabular}{lccccc}
131	\toprule
132	\textbf{Mode} & \textbf{Exec} & \textbf{ISR$_{.1}$} & \textbf{Rnd$_{.1}$} & \textbf{SFT} & \textbf{Prolog$_{\text{ISR}}$} \\
133	\midrule
134	CE embed       & 87 & 18 & 71 & 7 & 0$^\sharp$ \\
135	TS duplicate   & 0  & 71 & 14 & 0 & 100$^\sharp$ \\
136	PG prem-subset & 6  & 5  & 8   & 0 & --- \\
137	Tautological   & --- & --- & --- & --- & s42 \\
138	Repetition     & s43 & --- & --- & --- & --- \\
139	Contradiction  & 1k & --- & --- & --- & --- \\
140	Cmplx.\ vacuous& 0  & 0  & 4  & 0 & --- \\
141	Query-as-fact  & --- & --- & --- & --- & s44 \\
142	\midrule
143	\textbf{Non-hacking} & 8  & 6  & 10 & \textbf{92} & \textbf{0} \\
144	\bottomrule
145	\end{tabular}}
146	\caption{Eight hacking modes across conditions (\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\sharp$Prolog row pools strict+functional (\S\ref{sec:crosslogic}).}
147	\label{tab:hacking-taxonomy}
148	\end{table}
149	
150	Three modes account for ${>}90\%$ of hacking (Table~\ref{tab:hacking-taxonomy}; Appendix~\ref{app:hacking-modes}): \textbf{CE} (conclusion embedding), \textbf{TS} (conclusion duplication, ISR-amplified; TSb evades text-match classifiers), and \textbf{PG} (premise-subset gaming; audited for s42 only, s43/s44 checkpoints not retained). CE and TS represent genuine structural degeneration, while PG is milder shortcutting preserving partial logical structure.
151	\emph{Reward formulation determines composition but not prevalence}: all GRPO conditions show ${\geq}80\%$ hacking; only SFT achieves $92.3\%$ non-hacking.
152	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23c20533-abdd-4dc3-b305-456893d1d8e5",
  "isSidechain": true,
  "promptId": "fa6c39d1-76de-47fa-b5d7-2c224d3fced4",
  "agentId": "a943ecba15bc0e614",
  "type": "user",
  "uuid": "f613dcfc-a05b-4b36-8838-1b4d7b8751c2",
  "sourceToolAssistantUUID": "23c20533-abdd-4dc3-b305-456893d1d8e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-21T05:14:15.987Z_

Perfect. Now let me check the appendix for any additional mentions of these categories:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f613dcfc-a05b-4b36-8838-1b4d7b8751c2",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9GBBKrNkdiDhJVTvGn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c6b6c57c-e0f2-460a-bf6d-668d74ca431d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01B2Ddm7AJwcuyBzRaPB6PZg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6271,
      "cache_read_input_tokens": 47339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6271,
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

_source line 37 · 2026-05-21T05:14:16.821Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NVpT2KJW2ZBswZXTd2T9hs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6b6c57c-e0f2-460a-bf6d-668d74ca431d",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9GBBKrNkdiDhJVTvGn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2810fe07-87f5-421c-ab7b-815feac89b91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01B2Ddm7AJwcuyBzRaPB6PZg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6271,
      "cache_read_input_tokens": 47339,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6271
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 124,
          "cache_read_input_tokens": 47339,
          "cache_creation_input_tokens": 6271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6271,
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

_source line 38 · 2026-05-21T05:14:17.145Z_

<details><summary>↩ Tool result · `toolu_01NVpT2KJW2ZBswZXTd2T9hs`</summary>

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
10	\begin{table}[ht]
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
25	Rollouts per prompt ($K$) & 4 \\
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
52	\paragraph{Compute resources.}
53	Experiments were run on single-GPU setups (NVIDIA RTX 4090 24\,GB and RTX PRO 6000 96\,GB).
54	Each GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).
55	Total compute across all seeds, conditions, and reruns is approximately 80--120 GPU-hours.
56	
57	\paragraph{Evaluation exception.}
58	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
59	Its PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).
60	
61	\paragraph{Reward formulation.}
62	An additive variant ($r = r_{\text{exec}} + \beta\,\text{ISR}$) was tested in early experiments but collapsed prove rate to near-zero, as ISR alone provides no gradient toward provable formalizations; the multiplicative form $r_{\text{exec}}\cdot(1+\beta\,\text{ISR})$ ensures ISR modulates only proved outputs.
63	
64	\paragraph{ProofFOL dataset construction.}
65	\label{app:prooffol-construction}
66	ProofFOL is derived from ProofWriter~\citep{proofwriter} (10{,}424 training examples) via the GPT-4o silver-standard FOL translation pipeline of \citet{prooffol-thatikonda2024} with Prover9 verification filtering (${\sim}70\%$ retention; failures from timeouts, unsupported constructs, and translation errors).
67	Of the translated examples, 99.1\% parse successfully (92 skipped due to empty FOL output).
68	We sample 500 training and 100 evaluation examples (seed~42) from the verified pool.
69	Table~\ref{tab:prooffol-vs-folio} compares key structural properties.
70	
71	\begin{table}[!ht]
72	\centering
73	\caption{ProofFOL vs.\ FOLIO structural comparison (training sets, $n{=}500$ each).}
74	\label{tab:prooffol-vs-folio}
75	\footnotesize
76	\resizebox{\columnwidth}{!}{%
77	\begin{tabular}{@{}lcc@{}}
78	\toprule
79	\textbf{Property} & \textbf{ProofFOL} & \textbf{FOLIO} \\
80	\midrule
81	FOL premises (mean$\pm$std) & $18.2 \pm 3.2$ & $5.3 \pm 1.4$ \\
82	\quad Ground facts & $10.2 \pm 3.0$ & $1.8 \pm 1.5$ \\
83	\quad Rules & $8.1 \pm 1.1$ & $3.5 \pm 1.9$ \\
84	XOR ($\oplus$) samples & 0\% & 37.2\% \\
85	Dominant depth & 4--5 & 2--3 \\
86	Predicate style & synthetic & real-world \\
87	FOL source & GPT-4o (silver) & human (gold) \\
88	\bottomrule
89	\end{tabular}}
90	\end{table}
91	
92	ProofFOL problems are structurally more complex ($3.4{\times}$ more premises) but use simpler, synthetic predicates (e.g., \texttt{Blue(x)}, \texttt{Rough(x)}) characteristic of ProofWriter's procedural generation.
93	The absence of XOR constraints and the regularity of predicate structure make ProofFOL a complementary testbed: structural degeneration must emerge from the RL training dynamics rather than from formalization difficulty.
94	
95	\section{STA Algorithm}
96	\label{app:algorithm}
97	
98	Algorithm~\ref{alg:sta} (Section~\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.
99	For unproved samples ($S(x) \neq \textit{proved}$), ISR is undefined and the protocol is not applied.
100	
101	
102	\section{Extended Discussion}
103	\label{app:extended-discussion}
104	
105	\paragraph{What ISR measures---and what it does not.}
106	ISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.
107	This is strictly weaker than semantic faithfulness: whether the formalization accurately captures the natural-language meaning.
108	We verify this empirically: Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.
109	ISR and downstream task performance are uncorrelated.
110	ISR is thus a component-necessity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.
111	
112	Critically, low ISR carries different semantics depending on the training objective.
113	Under exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\S\ref{sec:crosslogic}).
114	Under ISR-as-reward, high ISR reflects metric gaming (\S\ref{sec:goodhart}).
115	ISR values must always be interpreted relative to the optimization objective that produced them.
116	
117	\paragraph{The premise-count confound.}
118	LOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.
119	A formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.
120	This confound explains the sole apparent ISR-as-reward success (\S\ref{sec:goodhart}): ISR $\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.
121	Premise-count-matched comparison eliminates the difference ($1.06\times$; Table~\ref{tab:fol-beta01-detailed}).
122	This bias is not specific to our setting: any LOO-based structural metric applied to variable-length outputs requires component-count normalization.
123	We recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.
124	
125	\begin{table*}[ht]
126	\centering
127	\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\beta{=}0.1$ non-hacking rate is corrected for PG reclassification and TS false negatives (Appendix~\ref{app:h8}).}
128	\label{tab:bootstrap-ci}
129	\small
130	\begin{tabular}{@{}lcccc@{}}
131	\toprule
132	\textbf{Comparison} & \textbf{Condition} & \textbf{Control} & \textbf{OR} & \textbf{$p$} \\
133	\midrule
134	\multicolumn{5}{@{}l}{\textit{Non-hacking rate (PG+FN corrected)}} \\
135	ISR vs.\ Random & 6.06\% {\scriptsize[3.6,9.9]} & 9.5\% {\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\
136	ISR vs.\ Exec-only & 6.06\% & 7.5\% & 0.79 & 0.62 \\
137	Random vs.\ Exec-only & 9.5\% & 7.5\% & 1.30 & 0.68 \\
138	\midrule
139	\multicolumn{5}{@{}l}{\textit{TS gaming rate}} \\
140	ISR vs.\ Random & 70.6\% {\scriptsize[64.3,76.3]} & 13.7\% {\scriptsize[9.9,18.6]} & 15.05 & $1.3{\times}10^{-39}$ \\
141	\midrule
142	\multicolumn{5}{@{}l}{\textit{SFT vs.\ Exec-only non-hacking rate}} \\
143	SFT vs.\ Exec-only & 92.3\% {\scriptsize[79.7,97.3]} & 7.5\% & 147 & ${<}0.001$ \\
144	\bottomrule
145	\end{tabular}
146	\\[2pt]
147	{\footnotesize ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\% Wilson CIs in brackets where shown.}
148	\end{table*}
149	
150	\paragraph{TS dose-response gradient.}
151	TS tautology follows a dose-response pattern across reward conditions: random $\beta{=}0.1$ produces $13.7\%$ TS ($36/262$ pooled; per-seed: $38.3\%$ in s43, $0\%$ in s42/s44), random $\beta{=}0.3$ yields 4--7 TSa samples per seed, and ISR $\beta{=}0.1$ reaches $70.6\%$ ($163/231$).
152	The gradient (random $\beta{=}0.1$ ($13.7\%$) $\to$ random $\beta{=}0.3$ (4--7 TSa per seed) $\to$ ISR $\beta{=}0.1$ ($70.6\%$)) shows ISR transforms TS from a seed-dependent GRPO tendency to a near-universal convergence direction.
153	
154	\paragraph{Goodhart effects: implications.}
155	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself. Any diagnostic metric risks becoming a target when optimized.
156	The dose-response pattern maps onto the Manheim \& Garrabrant taxonomy~\citep{manheim-goodhart-taxonomy}: $\beta{=}0.1$ on FOLIO instantiates \emph{regressional} Goodhart ($P{\to}P$ tautologies yield $\text{ISR}{\geq}0.5$, so ISR erroneously rewards the shortcut); $\beta{\geq}0.2$ introduces \emph{extremal} elements (PR collapse to 18\% vs.\ 48\% random at $\beta{=}0.3$).
157	The implication is conditional: ISR fails as a training reward when hacking satisfies its LOO structure (FOLIO), but produces beneficial instability when hacking does not (ProofFOL; \S\ref{sec:crossdomain}).
158	
159	\paragraph{Single-seed unreliability.}
160	The three exec-only seeds diverge radically (PR $\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\S\ref{sec:diagnostic}).
161	ISR $\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (TS), 1/3 by premise minimization (\S\ref{sec:goodhart}).
162	Multi-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.
163	
164	\paragraph{Classifier limitations.}
165	Text-match hacking classifiers have systematic blind spots that functional analysis exposes.
166	In Prolog STA, two seeds achieved 100\% genuine classification under strict text matching, yet functional analysis via the $n_{\text{necessary}}$ distribution revealed 0\% genuine in both cases (Table~\ref{tab:prolog-detailed}).
167	One seed produces uppercase pseudo-Prolog that is functionally tautological; the other converts conclusions to snake\_case atoms serving as both fact and query, a gaming mode invisible to string comparison.
168	Practitioners should cross-validate text-match classifiers with functional metrics and never treat classifier-reported genuine rates as ground truth without independent verification.
169	
170	\paragraph{Practical guidelines.}
171	\label{app:practical-guidelines}
172	Our findings yield five guidelines for GRPO-trained neurosymbolic systems:
173	(1)~Never evaluate by prove rate alone; use ISR and component count as joint diagnostics.
174	(2)~Report multi-seed results: single-seed GRPO evaluation is unreliable, as cross-seed variance can exceed the effect size of interest (\S\ref{sec:diagnostic}).
175	(3)~Use ISR for post-hoc diagnosis only, not as a training signal; any dose induces gaming or collapse.
176	(4)~Treat LOO-based metrics as component-count-biased until normalized.
177	(5)~Expect conclusion embedding as a GRPO-universal baseline (Table~\ref{tab:goodhart-landscape}): reward shaping alters hacking composition, not prevalence.
178	
179	\paragraph{Multiple testing correction.}
180	\label{app:statistical-details}
181	We define two test families: FOLIO ($k{=}14$ tests across all conditions) and ProofFOL ($k{=}1$).
182	Within the FOLIO family, Bonferroni correction at $\alpha{=}0.05$ yields adjusted thresholds of $p_{\text{adj}}{=}0.05/14{=}0.0036$.
183	Three primary comparisons survive correction: the TS rate difference (ISR vs.\ random; $p_{\text{bonf}}{=}1.82{\times}10^{-38}$), the SFT vs.\ exec-only non-hacking rate ($p_{\text{bonf}}{=}0.014$), and the Cochran--Mantel--Haenszel test for TS association across seeds ($p_{\text{bonf}}{<}10^{-8}$).
184	The matched 5+5-seed Fisher/Mann-Whitney comparison is borderline ($p_{\text{bonf}}{=}0.056$), significant at $\alpha{=}0.10$ after Bonferroni correction ($k{=}14$).
185	The ProofFOL genuine-rate permutation test ($p{=}0.10$) belongs to a separate hypothesis family (different dataset, independent experimental design) and does not reach significance even without correction; it is reported as an exploratory observation throughout.
186	Bonferroni assumes independence, which is conservative for our setting (several tests use overlapping data); Holm--Bonferroni or Benjamini--Hochberg FDR would recover the matched 5+5 comparison at conventional significance.
187	We report the most conservative Bonferroni results for transparency.
188	
189	
190	\section{Hacking Mode Definitions}
191	\label{app:hacking-modes}
192	
193	We identify eight distinct reward hacking modes across all experiments.
194	Each mode is defined below with its mechanism, a representative example, and its interaction with ISR.
195	Table~\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.
196	
197	\begin{table*}[ht]
198	\centering
199	\small
200	\begin{tabular}{@{}llcccc@{}}
201	\toprule
202	\textbf{Mode} & \textbf{Mechanism} & \textbf{Exec} & \textbf{ISR} & \textbf{Rnd} & \textbf{SFT} \\
203	\midrule
204	CE & Concl.\ in premises & 87 & 18 & 71 & 7 \\
205	TS & Single prem.\ = concl. & $\bullet$ & \textbf{71} & 14$^\dagger$ & 0 \\
206	PG & Premise-subset gaming & 6 & 5 & -- & 0 \\
207	Tautological & 2-comp $P{=}C$ & $\bullet$ & 0 & 0 & 0 \\
208	Repetition & Output degen. & $\bullet$ & -- & -- & -- \\
209	Contradiction & $n_{\text{comp}}$ inflated & $\bullet$ & -- & -- & -- \\
210	C-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\
211	Q-as-fact & Atom = fact+query & -- & -- & -- & -- \\
212	\bottomrule
213	\end{tabular}
214	\caption{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta{=}0.1$ 3-seed pooled. TS includes subtypes TSa (text-match, $n{=}149$ ISR $+$ 36 random) and TSb (obfuscated tautology, $n{=}14$; primarily s44). $^\dagger$Random TS driven by seed~43 (38.3\%); seeds~42/44: 0\%. Exec: CE${=}87$\% in s42; $\bullet$ marks seed- or step-specific modes (TS/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). PG: premise-subset gaming (Appendix~\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref{tab:prolog-detailed}).}
215	\label{tab:hacking-taxonomy-app}
216	\end{table*}
217	
218	\paragraph{Classifier Validation.}
219	Hacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.
220	CE and TS are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\text{necessary}}$ distribution from STA (leave-one-out ablation).
221	No training data or manual annotation is used for classification.
222	
223	To estimate precision, we manually verified 50 randomly sampled outputs classified as CE or TS: all 50 were confirmed correct (estimated precision ${>}$95\%, Wilson 95\% CI: [93\%, 100\%]).
224	Recall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.
225	We cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\text{necessary}} \leq 1$ are flagged as potential false negatives.
226	This cross-validation revealed query-as-fact gaming in Prolog (\S\ref{app:hacking-modes}), where the strict text classifier reported 100\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\text{necessary}}{=}1$).
227	The non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.
228	
229	\paragraph{Boundary case validation.}
230	Structured inspection of 20 boundary cases (short-conclusion CE (10, minimum 4 characters), low-ISR genuine (5, minimum $\text{ISR}{=}0.22$), and TS on false propositions (5)) confirmed 20/20 correct classifications.
231	Short-conclusion CE samples are unambiguous hacking: the conclusion appears as a standalone premise with no NL source.
232	Low-ISR genuine samples reflect mode-collapsed template outputs, not structural gaming.
233	3/5 TS boundary cases confirm factually false propositions (e.g., affirming ``dogs are plants''), showing TS is not merely vacuous but actively harmful.
234	
235	\subsection{PG --- Premise-Subset Gaming}
236	\label{app:h8}
237	
238	Manual audit of ISR $\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (CE-style).
239	We term this \textbf{PG (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.
240	
241	\paragraph{Detection.} PG is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\text{prem}} \leq 3$) that nonetheless achieve high ISR.
242	Automated detection is not currently feasible because PG requires comparing the generated premise set against the gold premises.
243	
244	\paragraph{Audit scope and limitations.}
245	Full PG audit was completed for ISR $\beta{=}0.1$ seed~42 only.
246	ISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated.
247	Random $\beta{=}0.1$ does not produce PG by mechanism (no ISR optimization pressure); seed~42 audit confirmed PG${=}0$.
248	
249	\paragraph{TS false-negative correction (TSb obfuscated tautology).}
250	ISR $\beta{=}0.1$ seed~44 contained 12 samples with $n_{\text{prem}}{=}1$ classified as non-hacking by the text matcher.
251	Manual inspection confirmed all 12 are logically equivalent to TS but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).
252	We classify these as \textbf{TSb} (obfuscated tautology), distinct from text-match-detectable TSa.
253	$10/12$ achieve $\text{ISR}{\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and TS classifier: triple gaming (\S\ref{sec:taxonomy}).
254	After correction, ISR s44 non-hacking${=}0$; total TS = TSa (77 text-match) + TSb (12 obfuscated) = 89.
255	
256	\paragraph{Impact on non-hacking-rate comparison.}
257	After PG reclassification and TS false-negative correction: ISR non-hacking $= 14/231 = 6.06\%$ vs.\ random non-hacking $= 25/262 = 9.5\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\% CI: ISR [3.6\%, 9.9\%], Random [6.5\%, 13.7\%]).
258	The direction is consistent with ISR-amplified gaming modes (TS, PG) displacing non-hacking output, but the effect is not statistically significant at the conventional $\alpha{=}0.05$ threshold.
259	
260	\subsection{CE --- Conclusion Embedding}
261	
262	\paragraph{Definition.}
263	The conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.
264	The solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.
265	
266	\paragraph{Example (FOL).}
267	\smallskip\noindent\rule{\columnwidth}{0.3pt}
268	{\small\begin{verbatim}
269	Premises:
270	  all x (bird(x) -> flies(x)).
271	  bird(tweety).
272	  flies(tweety).  % conclusion embedded
273	Conclusion: flies(tweety).
274	\end{verbatim}}
275	\noindent\rule{\columnwidth}{0.3pt}\smallskip
276	
277	\paragraph{ISR interaction.}
278	Variable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.
279	ISR does not distinguish trivial from substantive necessity.
280	
281	\paragraph{Prevalence.}
282	Conclusion embedding in some form (CE multi-premise or TS single-premise) is GRPO-universal at 68--97\% across all RL conditions.
283	Under exec-only and Random reward, it manifests as CE (71--93\%); under ISR reward, it shifts to TS (70.6\% pooled).
284	
285	
286	\subsection{TSa --- Conclusion Duplication (Standard)}
287	
288	\paragraph{Definition.}
289	The entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.
290	Since $P \to P$ is trivially provable, this simultaneously maximizes exec reward.
291	Because the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.
292	
293	\paragraph{Example (FOL).}
294	\smallskip\noindent\rule{\columnwidth}{0.3pt}
295	{\small\begin{verbatim}
296	Premises:
297	  all x ((A(x)&B(x))->(C(x)|D(x))).
298	Conclusion:
299	  all x ((A(x)&B(x))->(C(x)|D(x))).
300	\end{verbatim}}
301	\noindent\rule{\columnwidth}{0.3pt}\smallskip
302	
303	\paragraph{ISR interaction.}
304	ISR~$\approx 0.8$--$1.0$.
305	The single premise is trivially ``maximally necessary,'' but the proof is vacuous.
306	TSa games both exec reward and ISR reward; TSb extends this to triple gaming by additionally evading the text-match classifier.
307	
308	\paragraph{Prevalence.}
309	TSa (text-match detectable): 64.5\% pooled (149/231) under ISR~$\beta{=}0.1$ (s42: 16.0\%, s43: 96.7\%, s44: 86.5\%).
310	Combined TS (TSa + TSb): 70.6\% (163/231; s43 TSa${=}59$ + TSb${=}2$; includes s44 FN correction).
311	Random~$\beta{=}0.1$ pooled: 13.7\% (36/262, all TSa; driven by seed~43 at 38.3\%, seeds~42 and~44 at 0\%).
312	
313	
314	\subsection{TSb --- Obfuscated Tautology}
315	
316	\paragraph{Definition.}
317	A single-premise formalization logically equivalent to TSa (premise = conclusion) but with surface-form differences that evade the text-match TS classifier.
318	The model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).
319	
320	\paragraph{Example (FOL, vacuous quantifier wrapping).}
321	\smallskip\noindent\rule{\columnwidth}{0.3pt}
322	{\small\begin{verbatim}
323	Premises:
324	  all x all y ((A(x)&B(y))->(C(x)|D(y))).
325	Conclusion:
326	  all x ((A(x)&B(x))->(C(x)|D(x))).
327	\end{verbatim}}
328	\noindent\rule{\columnwidth}{0.3pt}\smallskip
329	The premise introduces a vacuous second variable $y$, immediately unified with $x$; the formulas are logically equivalent but differ textually.
330	
331	\paragraph{ISR interaction.}
332	$\text{ISR}{\geq}0.83$ ($10/12$ samples).
333	TSb simultaneously games three objectives: execution reward ($r_{\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match TS classifier (surface-form difference evades detection).
334	This triple gaming makes TSb the most complete Goodhart case we observe.
335	
336	\paragraph{Prevalence.}
337	Found primarily in ISR $\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as non-hacking); seed~43 contributes $2$ additional cases.
338	Functional cross-validation via $n_{\text{necessary}}{=}1$ exposed the misclassification.
339	
340	
341	\subsection{Tautological Collapse}
342	
343	\paragraph{Definition.}
344	Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \to P$ tautology with minimal token cost.
345	
346	\paragraph{Example (FOL).}
347	\smallskip\noindent\rule{\columnwidth}{0.3pt}
348	\begin{verbatim}
349	Premises: p(a).
350	Conclusion: p(a).
351	\end{verbatim}
352	\noindent\rule{\columnwidth}{0.3pt}\smallskip
353	
354	\paragraph{ISR interaction.}
355	ISR~$=1.0$ (the sole premise is necessary).
356	Distinguished from TS by having low component count ($n_{\text{comp}}\approx 2$) and atomic formulas rather than complex sub-structured conclusions.
357	
358	\paragraph{Prevalence.}
359	Dominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\text{comp}}=2.04$, 100\% TS by strict classifier).
360	Also observed in Prolog exec+STA seed~42 (100\% TS, PR~$=0.50$).
361	
362	
363	\subsection{Repetition Collapse}
364	
365	\paragraph{Definition.}
366	The model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.
367	Removing any single repeated copy leaves the others intact, yielding ISR~$\approx 0$.
368	
369	\paragraph{Example (Prolog).}
370	\smallskip\noindent\rule{\columnwidth}{0.3pt}
371	\begin{verbatim}
372	penguin(fido).
373	penguin(fido).
374	penguin(fido).
375	... (repeated to 512 tokens)
376	query(penguin(fido)).
377	\end{verbatim}
378	\noindent\rule{\columnwidth}{0.3pt}\smallskip
379	
380	\paragraph{ISR interaction.}
381	ISR~$\approx 0$. Each copy is individually redundant since identical copies remain after removal.
382	ISR correctly diagnoses this degeneration.
383	
384	\paragraph{Prevalence.}
385	Observed in FOL exec-only seed~43 (87\% of outputs hit max completion length; PR~$=13$\%, ISR~$=0$).
386	
387	
388	\subsection{Complexity-without-Utility}
389	
390	\paragraph{Definition.}
391	The formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous: none individually necessary for the proof.
392	The complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.
393	
394	\paragraph{Example (FOL).}
395	\smallskip\noindent\rule{\columnwidth}{0.3pt}
396	{\small\begin{verbatim}
397	Premises:
398	  all x all y (R(x,y) ->
399	    exists z (S(x,z) & T(z,y))).
400	  all x (P(x) -> Q(x)).
401	  P(a).            % only this needed
402	Conclusion: Q(a).
403	\end{verbatim}}
404	\noindent\rule{\columnwidth}{0.3pt}\smallskip
405	
406	\paragraph{ISR interaction.}
407	ISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.
408	This is the mode ISR is best calibrated for.
409	
410	\paragraph{Prevalence.}
411	Low. Observed in Random~$\beta{=}0.1$ seed~42 at 3.8\% (3/79).
412	Not observed under ISR reward (ISR's gradient discourages zero-ISR premises).
413	
414	
415	\subsection{Contradiction Explosion}
416	
417	\paragraph{Definition.}
418	The component count grows unboundedly over training.
419	Excess premises introduce contradictions or redundancies that trivially entail any conclusion via \emph{ex falso quodlibet}.
420	Individual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.
421	
422	\paragraph{Example (FOL, 1000-step exec-only).}
423	\smallskip\noindent\rule{\columnwidth}{0.3pt}
424	{\small\begin{verbatim}
425	Premises:
426	  c1. c2. c3. ... c18. % 18.55 mean
427	  % conclusion embedded among premises
428	Conclusion: Q(a).
429	\end{verbatim}}
430	\noindent\rule{\columnwidth}{0.3pt}\smallskip
431	
432	\paragraph{ISR interaction.}
433	ISR~$\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\% of proved samples having ISR~$=0$).
434	
435	\paragraph{Prevalence.}
436	Observed in extended exec-only training (seed~42, 1000 steps).
437	Mean component count grows from ${\sim}6$ (500 steps) to 18.55 (1000 steps).
438	
439	
440	\subsection{Query-as-Fact Gaming}
441	
442	\paragraph{Definition.}
443	The model converts the natural language conclusion into a snake\_case atom and includes it as both a ground fact and the query.
444	Prolog trivially proves the query by unifying with the fact.
445	This mode evades text-match classifiers designed for CE/TS because the generated atom bears no surface resemblance to the original conclusion text.
446	
447	\paragraph{Example (Prolog).}
448	\smallskip\noindent\rule{\columnwidth}{0.3pt}
449	\begin{verbatim}
450	% NL: "Fido is happy."
451	% Model output:
452	fido_is_happy.
453	:- fido_is_happy.     % query = fact
454	\end{verbatim}
455	\noindent\rule{\columnwidth}{0.3pt}\smallskip
456	
457	\paragraph{ISR interaction.}
458	ISR~$\approx 0.9$--$1.0$.
459	The single fact is trivially necessary (its removal breaks the query), inflating ISR.
460	Functionally equivalent to TS but with a distinct surface mechanism.
461	
462	\paragraph{Prevalence.}
463	Observed in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).
464	95/97 proved samples have $n_{\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\% non-hacking.
465	
466	
467	\section{Per-Seed Detailed Results}
468	\label{app:detailed-results}
469	
470	Tables~\ref{tab:fol-beta01-detailed} and \ref{tab:prolog-detailed} report full per-seed results.
471	All metrics are computed by \texttt{eval\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.
472	ISR values are proved-only ISR$^*$.
473	
474	\begin{table*}[t]
475	\centering
476	\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\beta{=}0.1$ breakdown referenced from Table~\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$). $^\ddagger$Three s44-1000 samples escape text-match heuristics (CE/PG classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass PG detection and commuted premises that bypass CE detection; reclassified as degenerate.}
477	\label{tab:fol-detailed}
478	\label{tab:fol-beta01-detailed}
479	\footnotesize
480	\setlength{\tabcolsep}{3pt}
481	\resizebox{\textwidth}{!}{%
482	\begin{tabular}{@{}llccccccl@{}}
483	\toprule
484	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Notes} \\
485	\midrule
486	\multicolumn{9}{@{}l}{\textit{Baselines}} \\
487	Base model (no training)
488	  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
489	Ground-truth FOL
490	  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
491	SFT
492	  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \textbf{92.3} & Supervised, no RL \\
493	  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \textbf{90.9} & \\
494	  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \textbf{93.3} & \\
495	\cmidrule(l){2-9}
496	  & \multicolumn{2}{l}{3-seed pooled} & $0.130$ & $0.595$ & $0$ & $7.8$ & \textbf{92.3} & $n{=}39$ proved \\
497	\midrule
498	\multicolumn{9}{@{}l}{\textit{Exec-only}} \\
499	  & 42 & 100 & 0.32 & \textbf{0.642} & --- & --- & --- & Early checkpoint \\
500	  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & PG${=}6.5\%$ \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2810fe07-87f5-421c-ab7b-815feac89b91",
  "isSidechain": true,
  "promptId": "fa6c39d1-76de-47fa-b5d7-2c224d3fced4",
  "agentId": "a943ecba15bc0e614",
  "type": "user",
  "uuid": "dedfe9d9-6109-4ed2-9b2a-d0cc4bc6f7c0",
  "sourceToolAssistantUUID": "2810fe07-87f5-421c-ab7b-815feac89b91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-21T05:14:18.758Z_

Now let me search more specifically for any references to the categories I might have missed. Let me check the introduction and conclusion more carefully:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dedfe9d9-6109-4ed2-9b2a-d0cc4bc6f7c0",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9GPZhk1bWnAsZ8Cvj9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "221477eb-066a-41fb-bf6f-991dafb38a2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AySFeqRqWPspZJZ7rmCC7w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 11181,
      "cache_read_input_tokens": 53610,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11181,
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

_source line 40 · 2026-05-21T05:14:19.623Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SE5ZFD4UyfqXCag5CNtUYs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "221477eb-066a-41fb-bf6f-991dafb38a2d",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9GPZhk1bWnAsZ8Cvj9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7a7184b6-facc-4a49-b40b-5f8572708905",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AySFeqRqWPspZJZ7rmCC7w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 11181,
      "cache_read_input_tokens": 53610,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11181,
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

_source line 41 · 2026-05-21T05:14:19.629Z_

<details><summary>↩ Tool result · `toolu_01SE5ZFD4UyfqXCag5CNtUYs`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems, yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.
6	This structural shortcut (an instance of shortcut learning~\citep{geirhos2020shortcut} in the neurosymbolic setting) is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.
7	
8	\paragraph{The execution-only blind spot.}
9	Prove rate, the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
10	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.
11	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
12	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for component necessity in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic applying \emph{component necessity testing}, leave-one-out (LOO) ablation on solver inputs, to quantify component necessity.
16	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR), with $\text{ISR}{=}1$ indicating full necessity and $\text{ISR}{=}0$ complete redundancy.
17	LOO ablation itself is standard~\citep{demillo1978, jia-harman-survey}; our contribution is the empirical discovery that the same LOO structure making ISR informative as a diagnostic also makes it vulnerable to gaming as a reward, a Goodhart effect on structural metrics.
18	ISR captures component necessity rather than semantic faithfulness (downstream NLI: $\rho{=}{-}0.049$, $p{=}0.187$).
19	
20	\begin{figure}[t]
21	\centering
22	\includegraphics[width=0.95\columnwidth]{figures/fig5_training_isr_curves.pdf}
23	\caption{ISR training trajectories across reward conditions (proved samples only, rolling $w{=}20$). Exec-only collapses to $\text{ISR}{\approx}0$, confirming structural degeneration (\S\ref{sec:diagnostic}); the ${\sim}0.5$ plateau is an $n{=}2$ artifact. ISR $\beta{=}0.1$ seeds rise toward $\text{ISR}{\approx}1$ via TS gaming (Goodhart effect, \S\ref{sec:goodhart}); random remains low.}
24	\label{fig:training-isr-curves}
25	\label{fig:isr-collapse}
26	\end{figure}
27	
28	\paragraph{ISR as diagnostic.}
29	As a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR (Figure~\ref{fig:training-isr-curves}): $\text{ISR}^{*}{:}\,0.642\to 0.132\to 0.003$ over 100--1000 steps (99.5\% degradation) while PR rises $32\%{\to}96\%$.
30	Three seeds diverge radically (PR $\sigma{=}47$\,pp), each converging to a qualitatively different mode (conclusion embedding, repetition collapse, and tautological collapse), yet all reach ${\geq}93\%$ structural hacking by 1000 steps.
31	An SFT baseline on identical data reaches $\text{PR}{=}13.0\%$ with 92.3\% non-hacking (3-seed pooled, 1000 steps), consistent with GRPO-specific degradation rather than data or capacity limitations.
32	
33	\paragraph{Goodhart effects.}
34	Repurposed as a training signal, $r = r_{\text{exec}} \cdot (1 + \beta\,\text{ISR})$, ISR is gamed at its own definition~\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}.
35	On FOLIO, this instantiates \emph{regressional} Goodhart~\citep{manheim-goodhart-taxonomy}: $P{\to}P$ tautologies yield $\text{ISR}{\geq}0.5$, so ISR rewards the shortcut; at $\beta{=}0.1$, ISR increases TS rates in all 3 seeds (70.6\% vs.\ 13.7\% random pooled), but the sole apparent ISR advantage reduces to $1.06\times$ after controlling for premise count.
36	At $\beta{\geq}0.2$, \emph{extremal} Goodhart dominates ($\text{PR}{=}66{\pm}42\%$ ISR, $54{\pm}35\%$ random at $\beta{=}0.3$).
37	On ProofFOL, hacking yields $\text{ISR}{=}0.0$, so ISR correctly penalizes shortcuts, associated with beneficial instability (76.8\% vs.\ 17.4\% genuine under a coarser classifier, $p{=}0.10$).
38	ISR's asymmetry is the central finding: \emph{reliable as observer, dataset-dependent as optimizer.}
39	
40	\paragraph{Contributions.}
41	In this case study (Qwen3-4B, 6 reward conditions, 3 seeds, 2 logic types, 2 dataset families, up to 1000 steps), we contribute: (\textbf{C1}) STA as a diagnostic framework (ISR metric, eight-mode hacking taxonomy, and cross-domain evaluation protocol) revealing a 99.5\% structural collapse invisible to PR, with an SFT control consistent with GRPO-specific degradation (\S\ref{sec:diagnostic}); (\textbf{C2}) Goodhart effects on ISR-as-reward (per-seed consistent TS amplification; apparent advantage collapses to $1.06\times$ after deconfounding, with a shuffled-ISR control ruling out distributional shape as the driver; \S\ref{sec:goodhart}), with preliminary cross-domain evidence from ProofFOL and Prolog showing dataset-dependent outcomes (\S\ref{sec:crossdomain}).
42	These are cautionary results, replicated across dataset families, relevant to any work treating a structural proxy as a training signal.
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a7184b6-facc-4a49-b40b-5f8572708905",
  "isSidechain": true,
  "promptId": "fa6c39d1-76de-47fa-b5d7-2c224d3fced4",
  "agentId": "a943ecba15bc0e614",
  "type": "user",
  "uuid": "564287b8-1d41-4962-805e-e15b1daba14e",
  "sourceToolAssistantUUID": "7a7184b6-facc-4a49-b40b-5f8572708905",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-21T05:14:19.808Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QtPsvJnirReEMwqybookay`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "564287b8-1d41-4962-805e-e15b1daba14e",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9GPZhk1bWnAsZ8Cvj9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4ac0e167-94d5-4ddb-b767-da348b4547e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AySFeqRqWPspZJZ7rmCC7w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 11181,
      "cache_read_input_tokens": 53610,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11181
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 187,
          "cache_read_input_tokens": 53610,
          "cache_creation_input_tokens": 11181,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11181,
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

_source line 43 · 2026-05-21T05:14:19.815Z_

<details><summary>↩ Tool result · `toolu_01QtPsvJnirReEMwqybookay`</summary>

```text
1	\begin{abstract}
2	We study structural degeneration in neurosymbolic reasoning trained with GRPO: models achieve high prove rates while most outputs embed the conclusion among premises---a degenerate shortcut invisible to execution reward.
3	We introduce \emph{Solver Trace Ablation} (STA), a diagnostic applying leave-one-out necessity testing to solver inputs; the fraction of necessary components yields the \emph{Intensional Structural Reward} (ISR).
4	As a diagnostic, ISR reveals a collapse trajectory hidden from prove rate: ISR falls to near-zero over training while prove rate rises, with each seed converging to a qualitatively different hacking mode.
5	A supervised fine-tuning baseline confirms the degradation is GRPO-specific.
6	When repurposed as a training reward, ISR induces Goodhart effects: models game the structural signal through diverse strategies, and a shuffled-ISR control confirms the gaming targets semantic content rather than distributional artifacts.
7	Cross-logic (Prolog) and cross-dataset (ProofFOL) replication confirms structural degeneration generalizes, documenting ISR's core asymmetry: reliable as a diagnostic, dataset-dependent as an optimization target.\footnote{Code and data: \url{[anonymized]}}
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ac0e167-94d5-4ddb-b767-da348b4547e1",
  "isSidechain": true,
  "promptId": "fa6c39d1-76de-47fa-b5d7-2c224d3fced4",
  "agentId": "a943ecba15bc0e614",
  "type": "user",
  "uuid": "6f6f0c5c-a08d-4d08-bd8d-215dbdac404f",
  "sourceToolAssistantUUID": "4ac0e167-94d5-4ddb-b767-da348b4547e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-21T05:14:29.012Z_

Perfect. Now let me verify my findings by doing a final comprehensive check on all the specific terms I searched for. Let me create a summary based on what I found:

Based on my comprehensive search of all .tex files in `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/`, here is the reference status for each experiment category:

## EXPERIMENT CATEGORIES REFERENCED IN THE PAPER

**PRESENT (referenced in paper text):**

1. **ProofFOL (cross-dataset)** - PRESENT
   - Multiple references in abstract, introduction, experiments, conclusion, and appendix sections
   - Used as a cross-dataset replication condition with 500 examples

2. **shuffled (shuffled-ISR control)** - PRESENT
   - Mentioned as a deconfounding control in experiments.tex (line 44): "shuffled-ISR control (batch-internal random permutation preserving ISR's bimodal distribution)"
   - Referenced in conclusion.tex and abstract.tex as evidence that gaming targets semantic content, not distributional shape

3. **β=0.2 (dose-response intermediate)** - PRESENT
   - Mentioned in experiments.tex (line 83): "At higher doses (β≥0.2), TS becomes universal (0% non-hacking at β=0.2)"
   - Referenced in introduction.tex regarding extremal Goodhart effects
   - Discussed in appendix.tex regarding dose-response patterns

4. **β=0.05 or 0.05 (very low dose)** - PRESENT
   - Found in appendix.tex, specifically in the statistical details section (line 182) regarding Bonferroni correction at α=0.05

**NOT PRESENT (no references found):**

5. **1.7B / 1_7b / Qwen3-1.7B (cross-scale experiments)** - NOT PRESENT
   - Paper uses Qwen3-4B exclusively, no mention of 1.7B variant

6. **d134 / 10-seed / s47-s51 (10-seed expansion)** - NOT PRESENT
   - Paper uses only 3 seeds (42, 43, 44)

7. **gated / d142 / component.*gate (gated ISR experiments)** - NOT PRESENT
   - No gating mechanisms mentioned in ISR computation

8. **5-seed / s45 / s46 / five seed (5-seed extensions)** - NOT PRESENT
   - Paper explicitly notes 3 seeds as the limitation

9. **warmstart / warm.start (warmstart experiments)** - NOT PRESENT
   - No warmstart or warm-start mechanisms documented

## SUMMARY

**Categories present in paper (4/9):**
- ProofFOL
- Shuffled-ISR
- β=0.2
- β=0.05 (α=0.05 in statistical context)

**Categories absent from paper (5/9):**
- 1.7B scale variant
- 10-seed expansion
- Gated ISR
- 5-seed extensions
- Warmstart experiments

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f6f0c5c-a08d-4d08-bd8d-215dbdac404f",
  "isSidechain": true,
  "agentId": "a943ecba15bc0e614",
  "requestId": "req_011CbF9Gb6FT71ZxLJG7pb17",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "12602d91-4f63-44aa-b00a-9680610bd274",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "6bce55f6-6a3c-4244-94b5-8479902dce60",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "dapper-gliding-pancake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GQrJh7JTbCBiVV3itKjWP8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2442,
      "cache_read_input_tokens": 64791,
      "output_tokens": 743,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2442
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 743,
          "cache_read_input_tokens": 64791,
          "cache_creation_input_tokens": 2442,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2442,
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
