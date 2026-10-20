# Research conversation: In the directory /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp, find any JSON files containing n=2000

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a9576db012ac53ecf.jsonl`
- **Structured JSON:** [`4d05d663593ccfca5e94.json`](../../sessions/4d/4d05d663593ccfca5e94.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

37 recorded events

### User

_source line 1 · 2026-05-22T16:26:44.100Z_

In the directory /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp, find any JSON files containing n=2000 bootstrap per-direction probe accuracy results. Specifically look for files like:
- probe_results_bootstrap_n2000.json
- Any files in data/llama31/ or data/qwen3/ directories with "n2000" or "bootstrap" in the name

Read the content of any matching files to find per-direction balanced accuracy means (EN→EN, ZH→ZH, EN→ZH, ZH→EN). Report the exact numbers found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7b01965c-4d4b-490d-8578-864ad14179c8",
  "agentId": "a9576db012ac53ecf",
  "type": "user",
  "uuid": "ef533ef0-3771-48b9-9579-35e3d6d08d5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-22T16:26:46.455Z_

I'll help you find and read those JSON files. Let me search for files matching the patterns you mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef533ef0-3771-48b9-9579-35e3d6d08d5c",
  "isSidechain": true,
  "agentId": "a9576db012ac53ecf",
  "requestId": "req_011CbHvMTawVA6NUgdnxkhqU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c97d6735-9fb8-4fd7-9bcc-f0d8b07ceb3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0173BxgrHa8FZjgSnnnDHCcK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27746,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27746,
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

_source line 3 · 2026-05-22T16:26:46.901Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01LjQ5qaNuCaGigYhzgtz1L2`</summary>

```json
{
  "pattern": "**/probe_results_bootstrap_n2000.json",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c97d6735-9fb8-4fd7-9bcc-f0d8b07ceb3d",
  "isSidechain": true,
  "agentId": "a9576db012ac53ecf",
  "requestId": "req_011CbHvMTawVA6NUgdnxkhqU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "733fefc8-c8cc-4113-96b5-dea5ca63dca3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0173BxgrHa8FZjgSnnnDHCcK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27746,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27746,
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

_source line 4 · 2026-05-22T16:26:47.046Z_

<details><summary>↩ Tool result · `toolu_01LjQ5qaNuCaGigYhzgtz1L2`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "733fefc8-c8cc-4113-96b5-dea5ca63dca3",
  "isSidechain": true,
  "promptId": "7b01965c-4d4b-490d-8578-864ad14179c8",
  "agentId": "a9576db012ac53ecf",
  "type": "user",
  "uuid": "43edbad4-a6cd-4bc9-a6b8-7be2d40a7a13",
  "sourceToolAssistantUUID": "733fefc8-c8cc-4113-96b5-dea5ca63dca3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T16:26:47.101Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01FR22mVz9aLpgP1aWU7m9HD`</summary>

```json
{
  "pattern": "**/data/llama31/**/*n2000*.json",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43edbad4-a6cd-4bc9-a6b8-7be2d40a7a13",
  "isSidechain": true,
  "agentId": "a9576db012ac53ecf",
  "requestId": "req_011CbHvMTawVA6NUgdnxkhqU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6da2ea62-d077-4025-bbb8-30f2b249b25c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0173BxgrHa8FZjgSnnnDHCcK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27746,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27746,
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

_source line 6 · 2026-05-22T16:26:47.199Z_

<details><summary>↩ Tool result · `toolu_01FR22mVz9aLpgP1aWU7m9HD`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6da2ea62-d077-4025-bbb8-30f2b249b25c",
  "isSidechain": true,
  "promptId": "7b01965c-4d4b-490d-8578-864ad14179c8",
  "agentId": "a9576db012ac53ecf",
  "type": "user",
  "uuid": "7f01bfcb-3108-44dc-ba6f-ca38a56bfad2",
  "sourceToolAssistantUUID": "6da2ea62-d077-4025-bbb8-30f2b249b25c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T16:26:50.278Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Cvg9WDpqyZCQcd4BpSGPDm`</summary>

```json
{
  "pattern": "**/data/qwen3/**/*n2000*.json",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f01bfcb-3108-44dc-ba6f-ca38a56bfad2",
  "isSidechain": true,
  "agentId": "a9576db012ac53ecf",
  "requestId": "req_011CbHvMTawVA6NUgdnxkhqU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "376843ab-22e1-4fbb-8822-d4155c5bd88e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0173BxgrHa8FZjgSnnnDHCcK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27746,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27746,
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

_source line 8 · 2026-05-22T16:26:50.370Z_

<details><summary>↩ Tool result · `toolu_01Cvg9WDpqyZCQcd4BpSGPDm`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "376843ab-22e1-4fbb-8822-d4155c5bd88e",
  "isSidechain": true,
  "promptId": "7b01965c-4d4b-490d-8578-864ad14179c8",
  "agentId": "a9576db012ac53ecf",
  "type": "user",
  "uuid": "900910f1-2179-432b-934f-1ae515484693",
  "sourceToolAssistantUUID": "376843ab-22e1-4fbb-8822-d4155c5bd88e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T16:26:50.493Z_

<details open><summary>🔧 Tool call — Glob · `toolu_012EF9yQiUUShaqaY2T64wbB`</summary>

```json
{
  "pattern": "**/data/llama31/**/*bootstrap*.json",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "900910f1-2179-432b-934f-1ae515484693",
  "isSidechain": true,
  "agentId": "a9576db012ac53ecf",
  "requestId": "req_011CbHvMTawVA6NUgdnxkhqU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9f67ab68-6ad7-466b-96c7-b6ebf696458d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0173BxgrHa8FZjgSnnnDHCcK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27746,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27746,
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

_source line 10 · 2026-05-22T16:26:50.583Z_

<details><summary>↩ Tool result · `toolu_012EF9yQiUUShaqaY2T64wbB`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f67ab68-6ad7-466b-96c7-b6ebf696458d",
  "isSidechain": true,
  "promptId": "7b01965c-4d4b-490d-8578-864ad14179c8",
  "agentId": "a9576db012ac53ecf",
  "type": "user",
  "uuid": "c3b6962f-d5fd-4c22-8755-2624f8dc266b",
  "sourceToolAssistantUUID": "9f67ab68-6ad7-466b-96c7-b6ebf696458d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T16:26:50.665Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01ESGgMAxCwjATAZ6P5eZ4Ui`</summary>

```json
{
  "pattern": "**/data/qwen3/**/*bootstrap*.json",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3b6962f-d5fd-4c22-8755-2624f8dc266b",
  "isSidechain": true,
  "agentId": "a9576db012ac53ecf",
  "requestId": "req_011CbHvMTawVA6NUgdnxkhqU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9b5391c3-f02f-4807-8162-3445659264bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0173BxgrHa8FZjgSnnnDHCcK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27746,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27746,
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

_source line 12 · 2026-05-22T16:26:50.772Z_

<details><summary>↩ Tool result · `toolu_01ESGgMAxCwjATAZ6P5eZ4Ui`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b5391c3-f02f-4807-8162-3445659264bf",
  "isSidechain": true,
  "promptId": "7b01965c-4d4b-490d-8578-864ad14179c8",
  "agentId": "a9576db012ac53ecf",
  "type": "user",
  "uuid": "7d8da065-2cd7-4236-8f81-34c369a03fa3",
  "sourceToolAssistantUUID": "9b5391c3-f02f-4807-8162-3445659264bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-22T16:26:52.493Z_

Let me try broader searches to find the data directories and any JSON files they might contain.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d8da065-2cd7-4236-8f81-34c369a03fa3",
  "isSidechain": true,
  "agentId": "a9576db012ac53ecf",
  "requestId": "req_011CbHvMxDsiYFR6nffHVuwE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "341e561a-d3af-4bd0-9566-e2fb24fee195",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SUuTPKNzvSYDLtdu1Vno9R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 27746,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1461,
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

_source line 14 · 2026-05-22T16:26:53.367Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JR3Rvec6ZPQsAV7UFjDw7F`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp -type d -name \"llama31\" -o -type d -name \"qwen3\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "341e561a-d3af-4bd0-9566-e2fb24fee195",
  "isSidechain": true,
  "agentId": "a9576db012ac53ecf",
  "requestId": "req_011CbHvMxDsiYFR6nffHVuwE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "50dab704-d103-4acd-8256-eae291487944",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SUuTPKNzvSYDLtdu1Vno9R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 27746,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1461,
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

_source line 15 · 2026-05-22T16:26:53.629Z_

<details><summary>↩ Tool result · `toolu_01JR3Rvec6ZPQsAV7UFjDw7F`</summary>

```text
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/transformers/models/qwen3
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50dab704-d103-4acd-8256-eae291487944",
  "isSidechain": true,
  "promptId": "7b01965c-4d4b-490d-8578-864ad14179c8",
  "agentId": "a9576db012ac53ecf",
  "type": "user",
  "uuid": "43978a6f-f590-49c3-b01c-288d5dc8f781",
  "sourceToolAssistantUUID": "50dab704-d103-4acd-8256-eae291487944",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-22T16:26:53.770Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UVTpPbQFyX4r4Mt9VRfhNX`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp -name \"*bootstrap*.json\" -o -name \"*n2000*.json\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43978a6f-f590-49c3-b01c-288d5dc8f781",
  "isSidechain": true,
  "agentId": "a9576db012ac53ecf",
  "requestId": "req_011CbHvMxDsiYFR6nffHVuwE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cb3b04f9-f992-4e83-a61e-9f088c0242bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SUuTPKNzvSYDLtdu1Vno9R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 27746,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1461,
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

_source line 17 · 2026-05-22T16:26:53.940Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DknEtveDiYPjwhNY3zMz6r`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp -type f -name \"*.json\" 2>/dev/null | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb3b04f9-f992-4e83-a61e-9f088c0242bb",
  "isSidechain": true,
  "agentId": "a9576db012ac53ecf",
  "requestId": "req_011CbHvMxDsiYFR6nffHVuwE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f9c3a053-6d84-4ea5-a362-618bbc2bfc83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SUuTPKNzvSYDLtdu1Vno9R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 27746,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1461
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 295,
          "cache_read_input_tokens": 27746,
          "cache_creation_input_tokens": 1461,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1461,
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

_source line 18 · 2026-05-22T16:26:53.975Z_

<details><summary>↩ Tool result · `toolu_01UVTpPbQFyX4r4Mt9VRfhNX`</summary>

```text
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_cpu_llama-bootstrap-n2000-restart_20260522T135606_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_analysis_bootstrap-n2000-check_20260522T045940_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_infra_kill-old-bootstrap_20260522T071227_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_cpu_c3-mlp-bootstrap-fix_20260522T083245_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_cpu_bootstrap-n2000-restart_20260522T065238_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_cpu_bootstrap-n2000-optimized_20260522T081516_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_analysis_bootstrap-n2000-111_20260522T041909_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_infra_wait_bootstrap100_bash_20260521T230652_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_infra_bootstrap-speed-diagnosis_20260522T080912_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_code_bootstrap_100_and_comet_20260521T230033_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_infra_verify_bootstrap100_files_20260521T234207_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_infra_collect_bootstrap100_results_20260521T230533_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_cpu_c3-mlp-bootstrap_20260522T080853_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_code_bootstrap_asymmetry_20260521T210858_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_code_bootstrap_seed_probe_20260521T224419_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/checkpoints/bootstrap_n2000_111_ALLOCATED_20260522T050439.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/checkpoints/bootstrap_n2000_111_RUNNING_20260522T050447.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/checkpoints/bootstrap_n2000_111_QUEUED_20260522T050434.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/checkpoints/bootstrap_n2000_111_DONE_20260522T151146.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb3b04f9-f992-4e83-a61e-9f088c0242bb",
  "isSidechain": true,
  "promptId": "7b01965c-4d4b-490d-8578-864ad14179c8",
  "agentId": "a9576db012ac53ecf",
  "type": "user",
  "uuid": "9ea7598e-2147-4fbf-a8c2-167dc1fbaf61",
  "sourceToolAssistantUUID": "cb3b04f9-f992-4e83-a61e-9f088c0242bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-22T16:26:54.117Z_

<details><summary>↩ Tool result · `toolu_01DknEtveDiYPjwhNY3zMz6r`</summary>

```text
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_code_restore_probe_results_20260521T224344_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_gpu_gemma-steering-L17-check_20260522T141653_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_cpu_llama-bootstrap-n2000-restart_20260522T135606_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_analysis_bootstrap-n2000-check_20260522T045940_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_code_multi_seed_probes_20260521T212426_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_infra_kill-old-bootstrap_20260522T071227_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_gpu_qwen-L14-steering-urgent_20260522T141636_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_gpu_qwen-L14-cuda1-restart_20260522T143601_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_infra_gemma-download-102-retry_20260522T013639_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_infra_comet-diagnose-restart_20260522T021144_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_paper_writing_abstract_20260522T160256_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_infra_fix_path_bug_urgent_20260521T234337_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_code_fix_bugs_and_rerun_both_20260521T211425_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_research_comet_dep_strategy_20260521T162628_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_infra_kill-comet-launch-steering_20260522T082111_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_cpu_c3-mlp-bootstrap-fix_20260522T083245_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_code_gemma-adaptation-102_20260522T030538_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_code_probe_balanced_acc_20260521T195241_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_cpu_bootstrap-n2000-restart_20260522T065238_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_analysis_steering-llama-results-107_20260522T112421_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_infra_download_instruct_models_20260521T150835_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_infra_gpu_status_check_20260521T200811_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_infra_qwen_zh_translate_20260521T165208_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_infra_urgent-status-check-3items_20260522T150851_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_infra_comprehensive-status-check_20260522T064705_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_gpu_steering-qwen-L23-107_20260522T125514_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_paper_writing_method_20260522T145638_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_data_extract_probe_results_20260522T132102_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_infra_urgent_status_and_push_20260521T185653_result.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_infra_llama_en_activations_v2_20260521T163247_result.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9c3a053-6d84-4ea5-a362-618bbc2bfc83",
  "isSidechain": true,
  "promptId": "7b01965c-4d4b-490d-8578-864ad14179c8",
  "agentId": "a9576db012ac53ecf",
  "type": "user",
  "uuid": "5ae958a9-c20e-403d-84fa-024c097ca4f5",
  "sourceToolAssistantUUID": "f9c3a053-6d84-4ea5-a362-618bbc2bfc83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-22T16:26:55.599Z_

Good! I found some checkpoint files. Let me search more specifically for probe results in the data directory:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ae958a9-c20e-403d-84fa-024c097ca4f5",
  "isSidechain": true,
  "agentId": "a9576db012ac53ecf",
  "requestId": "req_011CbHvNC5opUoREGAYsFewh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "35fe7f12-c7aa-4465-a644-1c6fcd9b7c68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016hrHVhjKqXJ2UsWPC5gkZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3183,
      "cache_read_input_tokens": 29207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3183,
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

_source line 21 · 2026-05-22T16:26:56.027Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WDvBytMkvQbTXRYfZeouyC`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp -type d -name \"data\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35fe7f12-c7aa-4465-a644-1c6fcd9b7c68",
  "isSidechain": true,
  "agentId": "a9576db012ac53ecf",
  "requestId": "req_011CbHvNC5opUoREGAYsFewh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a25ef03f-cbfd-4865-82ee-a3747d805e67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016hrHVhjKqXJ2UsWPC5gkZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3183,
      "cache_read_input_tokens": 29207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3183,
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

_source line 22 · 2026-05-22T16:26:56.171Z_

<details><summary>↩ Tool result · `toolu_01WDvBytMkvQbTXRYfZeouyC`</summary>

```text
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/_project/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/steering_107/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/numpy/typing/tests/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/numpy/core/tests/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/numpy/random/tests/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/numpy/lib/tests/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/joblib/test/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/pyarrow/tests/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/sklearn/datasets/tests/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/sklearn/datasets/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/transformers/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/torch/distributed/elastic/utils/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/torch/testing/_internal/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/torch/include/torch/csrc/api/include/torch/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/torch/utils/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/sympy/utilities/mathml/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/scipy/ndimage/tests/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/scipy/linalg/tests/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/scipy/special/tests/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/scipy/sparse/tests/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/scipy/stats/tests/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/scipy/interpolate/tests/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/scipy/io/tests/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/scipy/io/arff/tests/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/scipy/io/matlab/tests/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/scipy/spatial/tests/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/mvp_probe_v1/data
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/mvp_probe_llama_v1/data
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a25ef03f-cbfd-4865-82ee-a3747d805e67",
  "isSidechain": true,
  "promptId": "7b01965c-4d4b-490d-8578-864ad14179c8",
  "agentId": "a9576db012ac53ecf",
  "type": "user",
  "uuid": "65aa7e5b-f35f-44a5-86cd-73522599e702",
  "sourceToolAssistantUUID": "a25ef03f-cbfd-4865-82ee-a3747d805e67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T16:26:56.510Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TyqxkBaYUZzGkMVcp7DRhj`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp -path \"*/data/*\" -name \"*probe*\" -type f 2>/dev/null | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65aa7e5b-f35f-44a5-86cd-73522599e702",
  "isSidechain": true,
  "agentId": "a9576db012ac53ecf",
  "requestId": "req_011CbHvNC5opUoREGAYsFewh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "847f65ee-8536-4244-9f52-6f4103af5776",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016hrHVhjKqXJ2UsWPC5gkZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3183,
      "cache_read_input_tokens": 29207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3183,
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

_source line 24 · 2026-05-22T16:26:56.638Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DLDCoYKmXQnAY57o31W69e`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/ 2>/dev/null | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "847f65ee-8536-4244-9f52-6f4103af5776",
  "isSidechain": true,
  "agentId": "a9576db012ac53ecf",
  "requestId": "req_011CbHvNC5opUoREGAYsFewh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e598deee-f0fb-4c57-9e95-96fa1e2cb898",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016hrHVhjKqXJ2UsWPC5gkZC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3183,
      "cache_read_input_tokens": 29207,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3183
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 272,
          "cache_read_input_tokens": 29207,
          "cache_creation_input_tokens": 3183,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3183,
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

_source line 25 · 2026-05-22T16:26:56.678Z_

<details><summary>↩ Tool result · `toolu_01TyqxkBaYUZzGkMVcp7DRhj`</summary>

```text
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/data/llama31_probe_results.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/data/qwen3_probe_results.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/_project/data/llama31_probe_results.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/_project/data/layerwise_probe_curves.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/_project/data/qwen3_probe_results.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "847f65ee-8536-4244-9f52-6f4103af5776",
  "isSidechain": true,
  "promptId": "7b01965c-4d4b-490d-8578-864ad14179c8",
  "agentId": "a9576db012ac53ecf",
  "type": "user",
  "uuid": "fb92df97-e2e0-408f-80fd-383364e9967a",
  "sourceToolAssistantUUID": "847f65ee-8536-4244-9f52-6f4103af5776",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T16:26:56.719Z_

<details><summary>↩ Tool result · `toolu_01DLDCoYKmXQnAY57o31W69e`</summary>

```text
total 248
drwxr-xr-x 9 ubuntu ubuntu  4096 May 22 16:23 .
drwxrwxr-x 5 ubuntu ubuntu  4096 May 21 12:08 ..
drwxr-xr-x 3 ubuntu ubuntu  4096 May 21 11:58 .claude
-rw-r--r-- 1 ubuntu ubuntu 14423 May 22 16:25 AGENTS.md
-rw-r--r-- 1 ubuntu ubuntu     0 May 21 11:59 ROADMAP.lock
-rw------- 1 ubuntu ubuntu  2787 May 22 13:22 ROADMAP.md
drwxr-xr-x 9 ubuntu ubuntu  4096 May 22 16:14 artifacts
drwxr-xr-x 2 ubuntu ubuntu 20480 May 22 15:59 checkpoints
drwxr-xr-x 2 ubuntu ubuntu  4096 May 22 13:29 data
-rw-r--r-- 1 ubuntu ubuntu     0 May 21 12:00 decisions.lock
-rw------- 1 ubuntu ubuntu 12102 May 22 13:22 decisions.yaml
drwxr-xr-x 4 ubuntu ubuntu  4096 May 21 11:46 docs
-rwxr-xr-x 1 ubuntu ubuntu     0 May 21 11:46 dream_registry.lock
-rw------- 1 ubuntu ubuntu  1001 May 22 03:37 dream_registry.yaml
-rw-r--r-- 1 ubuntu ubuntu  1006 May 22 03:37 dream_registry.yaml.bak
-rw-r--r-- 1 ubuntu ubuntu 11300 May 22 03:53 experiment_plan.yaml
drwxr-xr-x 3 ubuntu ubuntu  4096 May 22 13:04 figures
-rw-r--r-- 1 ubuntu ubuntu     0 May 21 12:04 literature_map.lock
-rw------- 1 ubuntu ubuntu 20156 May 22 14:07 literature_map.yaml
drwxr-xr-x 4 ubuntu ubuntu  4096 May 21 12:02 logs
-rw-r--r-- 1 ubuntu ubuntu  3615 May 22 13:32 memory.md
-rw-r--r-- 1 ubuntu ubuntu     0 May 21 12:10 mistakes.lock
-rw------- 1 ubuntu ubuntu 11101 May 22 08:47 mistakes.yaml
-rw-r--r-- 1 ubuntu ubuntu 12761 May 22 13:23 paper_framing.md
-rw-r--r-- 1 ubuntu ubuntu     0 May 22 14:50 paper_provenance.lock
-rw------- 1 ubuntu ubuntu 10944 May 22 16:23 paper_provenance.yaml
-rw-r--r-- 1 ubuntu ubuntu     0 May 21 13:16 registry.lock
-rw------- 1 ubuntu ubuntu 56929 May 22 15:59 registry.yaml
-rw-r--r-- 1 ubuntu ubuntu  2578 May 22 15:59 report.md
-rwxr-xr-x 1 ubuntu ubuntu     0 May 21 11:58 study_status.lock
-rw-r--r-- 1 ubuntu ubuntu 14550 May 22 13:25 writing_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e598deee-f0fb-4c57-9e95-96fa1e2cb898",
  "isSidechain": true,
  "promptId": "7b01965c-4d4b-490d-8578-864ad14179c8",
  "agentId": "a9576db012ac53ecf",
  "type": "user",
  "uuid": "eb394f83-3475-41fd-8035-06ffe16869e5",
  "sourceToolAssistantUUID": "e598deee-f0fb-4c57-9e95-96fa1e2cb898",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-22T16:26:58.523Z_

Great! I found the probe results files. Now let me search for the bootstrap n2000 specific files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb394f83-3475-41fd-8035-06ffe16869e5",
  "isSidechain": true,
  "agentId": "a9576db012ac53ecf",
  "requestId": "req_011CbHvNPCYY2pXCrakymmet",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1e1576ff-e88d-47e1-9f6d-ed2a19b36bbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01U7fVST5C18hkFFfiVHw5U4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3023,
      "cache_read_input_tokens": 32390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3023,
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

_source line 28 · 2026-05-22T16:26:59.088Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01S7Gk8vjMaRA1HiyoGBwAb4`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/data -type f -name \"*.json\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e1576ff-e88d-47e1-9f6d-ed2a19b36bbc",
  "isSidechain": true,
  "agentId": "a9576db012ac53ecf",
  "requestId": "req_011CbHvNPCYY2pXCrakymmet",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "567a2398-ce68-47f5-a8ed-6eea4c2da203",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01U7fVST5C18hkFFfiVHw5U4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3023,
      "cache_read_input_tokens": 32390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3023,
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

_source line 29 · 2026-05-22T16:26:59.138Z_

<details><summary>↩ Tool result · `toolu_01S7Gk8vjMaRA1HiyoGBwAb4`</summary>

```text
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/data/llama31_probe_results.json
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/data/qwen3_probe_results.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "567a2398-ce68-47f5-a8ed-6eea4c2da203",
  "isSidechain": true,
  "promptId": "7b01965c-4d4b-490d-8578-864ad14179c8",
  "agentId": "a9576db012ac53ecf",
  "type": "user",
  "uuid": "c45223ee-1429-4b9c-bcc7-4a30c89711ba",
  "sourceToolAssistantUUID": "567a2398-ce68-47f5-a8ed-6eea4c2da203",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-22T16:26:59.174Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FTBXSpdtppGQm7q3F2VfyD`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/data/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c45223ee-1429-4b9c-bcc7-4a30c89711ba",
  "isSidechain": true,
  "agentId": "a9576db012ac53ecf",
  "requestId": "req_011CbHvNPCYY2pXCrakymmet",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "41e0a135-d369-4c1d-9a03-ec44ee2bf029",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01U7fVST5C18hkFFfiVHw5U4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3023,
      "cache_read_input_tokens": 32390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3023,
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

_source line 31 · 2026-05-22T16:26:59.235Z_

<details><summary>↩ Tool result · `toolu_01FTBXSpdtppGQm7q3F2VfyD`</summary>

```text
total 136
drwxr-xr-x 2 ubuntu ubuntu  4096 May 22 13:29 .
drwxr-xr-x 9 ubuntu ubuntu  4096 May 22 16:23 ..
-rw-r--r-- 1 ubuntu ubuntu 62153 May 22 13:29 llama31_probe_results.json
-rw-r--r-- 1 ubuntu ubuntu 62052 May 22 13:29 qwen3_probe_results.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41e0a135-d369-4c1d-9a03-ec44ee2bf029",
  "isSidechain": true,
  "promptId": "7b01965c-4d4b-490d-8578-864ad14179c8",
  "agentId": "a9576db012ac53ecf",
  "type": "user",
  "uuid": "a5c89d1e-c33e-45a7-bcdd-faf8d547d0e1",
  "sourceToolAssistantUUID": "41e0a135-d369-4c1d-9a03-ec44ee2bf029",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-22T16:27:00.773Z_

Perfect! Now let me read these files to find the bootstrap n2000 results:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5c89d1e-c33e-45a7-bcdd-faf8d547d0e1",
  "isSidechain": true,
  "agentId": "a9576db012ac53ecf",
  "requestId": "req_011CbHvNZxTAGmp5GRAgk4X7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9a26a59b-a3ef-466c-b5c0-cabb23243b42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013v6N3SkQakY2HtJ9pA8DU8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 453,
      "cache_read_input_tokens": 35413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 453,
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

_source line 33 · 2026-05-22T16:27:00.987Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UD1dshNFo4Cs8Xrv9WR3BB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/data/llama31_probe_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a26a59b-a3ef-466c-b5c0-cabb23243b42",
  "isSidechain": true,
  "agentId": "a9576db012ac53ecf",
  "requestId": "req_011CbHvNZxTAGmp5GRAgk4X7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "25db9050-f268-421a-b4de-3af00cd874e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013v6N3SkQakY2HtJ9pA8DU8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 453,
      "cache_read_input_tokens": 35413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 453,
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

_source line 34 · 2026-05-22T16:27:01.127Z_

<details open><summary>🔧 Tool call — Read · `toolu_01D4NwWhnAJyCUgW3LRLEvC9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/data/qwen3_probe_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25db9050-f268-421a-b4de-3af00cd874e1",
  "isSidechain": true,
  "agentId": "a9576db012ac53ecf",
  "requestId": "req_011CbHvNZxTAGmp5GRAgk4X7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bcfeee24-1d92-4743-bb7b-78bfd1f0a056",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013v6N3SkQakY2HtJ9pA8DU8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 453,
      "cache_read_input_tokens": 35413,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 453
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 180,
          "cache_read_input_tokens": 35413,
          "cache_creation_input_tokens": 453,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 453,
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

_source line 35 · 2026-05-22T16:27:01.251Z_

<details><summary>↩ Tool result · `toolu_01UD1dshNFo4Cs8Xrv9WR3BB`</summary>

```text
1	{
2	  "mode": "bootstrap",
3	  "n_bootstrap": 100,
4	  "num_layers": 32,
5	  "directions": {
6	    "EN\u2192EN": {
7	      "direction": "EN\u2192EN",
8	      "n_bootstrap": 100,
9	      "balanced_accuracy_mean": 0.771,
10	      "balanced_accuracy_std": 0.0119,
11	      "f1_mean": 0.7678,
12	      "f1_std": 0.014,
13	      "peak_layers": [
14	        10,
15	        19,
16	        26,
17	        22,
18	        20,
19	        18,
20	        27,
21	        28,
22	        16,
23	        13,
24	        16,
25	        13,
26	        19,
27	        26,
28	        12,
29	        18,
30	        19,
31	        19,
32	        19,
33	        16,
34	        25,
35	        18,
36	        27,
37	        19,
38	        10,
39	        18,
40	        29,
41	        18,
42	        20,
43	        13,
44	        25,
45	        18,
46	        22,
47	        17,
48	        31,
49	        17,
50	        20,
51	        13,
52	        13,
53	        18,
54	        30,
55	        13,
56	        22,
57	        17,
58	        22,
59	        28,
60	        15,
61	        28,
62	        13,
63	        12,
64	        27,
65	        22,
66	        13,
67	        23,
68	        16,
69	        12,
70	        20,
71	        13,
72	        18,
73	        16,
74	        19,
75	        13,
76	        16,
77	        13,
78	        12,
79	        22,
80	        19,
81	        29,
82	        10,
83	        16,
84	        12,
85	        26,
86	        16,
87	        23,
88	        13,
89	        28,
90	        17,
91	        22,
92	        28,
93	        13,
94	        12,
95	        22,
96	        29,
97	        14,
98	        18,
99	        13,
100	        13,
101	        16,
102	        11,
103	        13,
104	        18,
105	        20,
106	        17,
107	        18,
108	        16,
109	        21,
110	        22,
111	        19,
112	        20,
113	        26
114	      ],
115	      "per_bootstrap": [
116	        {
117	          "balanced_accuracy": 0.7647,
118	          "accuracy": 0.7647,
119	          "f1": 0.7576,
120	          "peak_layer": 10
121	        },
122	        {
123	          "balanced_accuracy": 0.7721,
124	          "accuracy": 0.7721,
125	          "f1": 0.7634,
126	          "peak_layer": 19
127	        },
128	        {
129	          "balanced_accuracy": 0.7684,
130	          "accuracy": 0.7684,
131	          "f1": 0.7726,
132	          "peak_layer": 26
133	        },
134	        {
135	          "balanced_accuracy": 0.7941,
136	          "accuracy": 0.7941,
137	          "f1": 0.7926,
138	          "peak_layer": 22
139	        },
140	        {
141	          "balanced_accuracy": 0.7757,
142	          "accuracy": 0.7757,
143	          "f1": 0.7663,
144	          "peak_layer": 20
145	        },
146	        {
147	          "balanced_accuracy": 0.7721,
148	          "accuracy": 0.7721,
149	          "f1": 0.7669,
150	          "peak_layer": 18
151	        },
152	        {
153	          "balanced_accuracy": 0.7757,
154	          "accuracy": 0.7757,
155	          "f1": 0.7749,
156	          "peak_layer": 27
157	        },
158	        {
159	          "balanced_accuracy": 0.7721,
160	          "accuracy": 0.7721,
161	          "f1": 0.7669,
162	          "peak_layer": 28
163	        },
164	        {
165	          "balanced_accuracy": 0.7868,
166	          "accuracy": 0.7868,
167	          "f1": 0.7786,
168	          "peak_layer": 16
169	        },
170	        {
171	          "balanced_accuracy": 0.7757,
172	          "accuracy": 0.7757,
173	          "f1": 0.7749,
174	          "peak_layer": 13
175	        },
176	        {
177	          "balanced_accuracy": 0.761,
178	          "accuracy": 0.761,
179	          "f1": 0.7529,
180	          "peak_layer": 16
181	        },
182	        {
183	          "balanced_accuracy": 0.7574,
184	          "accuracy": 0.7574,
185	          "f1": 0.766,
186	          "peak_layer": 13
187	        },
188	        {
189	          "balanced_accuracy": 0.761,
190	          "accuracy": 0.761,
191	          "f1": 0.7547,
192	          "peak_layer": 19
193	        },
194	        {
195	          "balanced_accuracy": 0.7757,
196	          "accuracy": 0.7757,
197	          "f1": 0.7814,
198	          "peak_layer": 26
199	        },
200	        {
201	          "balanced_accuracy": 0.7794,
202	          "accuracy": 0.7794,
203	          "f1": 0.7761,
204	          "peak_layer": 12
205	        },
206	        {
207	          "balanced_accuracy": 0.761,
208	          "accuracy": 0.761,
209	          "f1": 0.7584,
210	          "peak_layer": 18
211	        },
212	        {
213	          "balanced_accuracy": 0.7647,
214	          "accuracy": 0.7647,
215	          "f1": 0.7664,
216	          "peak_layer": 19
217	        },
218	        {
219	          "balanced_accuracy": 0.7831,
220	          "accuracy": 0.7831,
221	          "f1": 0.7739,
222	          "peak_layer": 19
223	        },
224	        {
225	          "balanced_accuracy": 0.7941,
226	          "accuracy": 0.7941,
227	          "f1": 0.7971,
228	          "peak_layer": 19
229	        },
230	        {
231	          "balanced_accuracy": 0.7647,
232	          "accuracy": 0.7647,
233	          "f1": 0.7612,
234	          "peak_layer": 16
235	        },
236	        {
237	          "balanced_accuracy": 0.7904,
238	          "accuracy": 0.7904,
239	          "f1": 0.7927,
240	          "peak_layer": 25
241	        },
242	        {
243	          "balanced_accuracy": 0.7794,
244	          "accuracy": 0.7794,
245	          "f1": 0.7761,
246	          "peak_layer": 18
247	        },
248	        {
249	          "balanced_accuracy": 0.7647,
250	          "accuracy": 0.7647,
251	          "f1": 0.7681,
252	          "peak_layer": 27
253	        },
254	        {
255	          "balanced_accuracy": 0.761,
256	          "accuracy": 0.761,
257	          "f1": 0.749,
258	          "peak_layer": 19
259	        },
260	        {
261	          "balanced_accuracy": 0.7426,
262	          "accuracy": 0.7426,
263	          "f1": 0.7445,
264	          "peak_layer": 10
265	        },
266	        {
267	          "balanced_accuracy": 0.8015,
268	          "accuracy": 0.8015,
269	          "f1": 0.8015,
270	          "peak_layer": 18
271	        },
272	        {
273	          "balanced_accuracy": 0.7941,
274	          "accuracy": 0.7941,
275	          "f1": 0.7971,
276	          "peak_layer": 29
277	        },
278	        {
279	          "balanced_accuracy": 0.761,
280	          "accuracy": 0.761,
281	          "f1": 0.7547,
282	          "peak_layer": 18
283	        },
284	        {
285	          "balanced_accuracy": 0.7721,
286	          "accuracy": 0.7721,
287	          "f1": 0.7634,
288	          "peak_layer": 20
289	        },
290	        {
291	          "balanced_accuracy": 0.7537,
292	          "accuracy": 0.7537,
293	          "f1": 0.7491,
294	          "peak_layer": 13
295	        },
296	        {
297	          "balanced_accuracy": 0.7831,
298	          "accuracy": 0.7831,
299	          "f1": 0.7839,
300	          "peak_layer": 25
301	        },
302	        {
303	          "balanced_accuracy": 0.7794,
304	          "accuracy": 0.7794,
305	          "f1": 0.7581,
306	          "peak_layer": 18
307	        },
308	        {
309	          "balanced_accuracy": 0.7684,
310	          "accuracy": 0.7684,
311	          "f1": 0.7675,
312	          "peak_layer": 22
313	        },
314	        {
315	          "balanced_accuracy": 0.7794,
316	          "accuracy": 0.7794,
317	          "f1": 0.7826,
318	          "peak_layer": 17
319	        },
320	        {
321	          "balanced_accuracy": 0.7574,
322	          "accuracy": 0.7574,
323	          "f1": 0.75,
324	          "peak_layer": 31
325	        },
326	        {
327	          "balanced_accuracy": 0.7574,
328	          "accuracy": 0.7574,
329	          "f1": 0.75,
330	          "peak_layer": 17
331	        },
332	        {
333	          "balanced_accuracy": 0.7757,
334	          "accuracy": 0.7757,
335	          "f1": 0.7663,
336	          "peak_layer": 20
337	        },
338	        {
339	          "balanced_accuracy": 0.7757,
340	          "accuracy": 0.7757,
341	          "f1": 0.7715,
342	          "peak_layer": 13
343	        },
344	        {
345	          "balanced_accuracy": 0.7647,
346	          "accuracy": 0.7647,
347	          "f1": 0.7714,
348	          "peak_layer": 13
349	        },
350	        {
351	          "balanced_accuracy": 0.7537,
352	          "accuracy": 0.7537,
353	          "f1": 0.7452,
354	          "peak_layer": 18
355	        },
356	        {
357	          "balanced_accuracy": 0.7831,
358	          "accuracy": 0.7831,
359	          "f1": 0.7774,
360	          "peak_layer": 30
361	        },
362	        {
363	          "balanced_accuracy": 0.7537,
364	          "accuracy": 0.7537,
365	          "f1": 0.7472,
366	          "peak_layer": 13
367	        },
368	        {
369	          "balanced_accuracy": 0.7537,
370	          "accuracy": 0.7537,
371	          "f1": 0.7546,
372	          "peak_layer": 22
373	        },
374	        {
375	          "balanced_accuracy": 0.7647,
376	          "accuracy": 0.7647,
377	          "f1": 0.7557,
378	          "peak_layer": 17
379	        },
380	        {
381	          "balanced_accuracy": 0.7684,
382	          "accuracy": 0.7684,
383	          "f1": 0.7605,
384	          "peak_layer": 22
385	        },
386	        {
387	          "balanced_accuracy": 0.7831,
388	          "accuracy": 0.7831,
389	          "f1": 0.7915,
390	          "peak_layer": 28
391	        },
392	        {
393	          "balanced_accuracy": 0.7868,
394	          "accuracy": 0.7868,
395	          "f1": 0.782,
396	          "peak_layer": 15
397	        },
398	        {
399	          "balanced_accuracy": 0.7904,
400	          "accuracy": 0.7904,
401	          "f1": 0.7957,
402	          "peak_layer": 28
403	        },
404	        {
405	          "balanced_accuracy": 0.7721,
406	          "accuracy": 0.7721,
407	          "f1": 0.7786,
408	          "peak_layer": 13
409	        },
410	        {
411	          "balanced_accuracy": 0.7794,
412	          "accuracy": 0.7794,
413	          "f1": 0.7692,
414	          "peak_layer": 12
415	        },
416	        {
417	          "balanced_accuracy": 0.7831,
418	          "accuracy": 0.7831,
419	          "f1": 0.7807,
420	          "peak_layer": 27
421	        },
422	        {
423	          "balanced_accuracy": 0.7868,
424	          "accuracy": 0.7868,
425	          "f1": 0.7836,
426	          "peak_layer": 22
427	        },
428	        {
429	          "balanced_accuracy": 0.7831,
430	          "accuracy": 0.7831,
431	          "f1": 0.7823,
432	          "peak_layer": 13
433	        },
434	        {
435	          "balanced_accuracy": 0.7721,
436	          "accuracy": 0.7721,
437	          "f1": 0.777,
438	          "peak_layer": 23
439	        },
440	        {
441	          "balanced_accuracy": 0.7794,
442	          "accuracy": 0.7794,
443	          "f1": 0.7778,
444	          "peak_layer": 16
445	        },
446	        {
447	          "balanced_accuracy": 0.7684,
448	          "accuracy": 0.7684,
449	          "f1": 0.7605,
450	          "peak_layer": 12
451	        },
452	        {
453	          "balanced_accuracy": 0.7684,
454	          "accuracy": 0.7684,
455	          "f1": 0.7692,
456	          "peak_layer": 20
457	        },
458	        {
459	          "balanced_accuracy": 0.7647,
460	          "accuracy": 0.7647,
461	          "f1": 0.763,
462	          "peak_layer": 13
463	        },
464	        {
465	          "balanced_accuracy": 0.7794,
466	          "accuracy": 0.7794,
467	          "f1": 0.7727,
468	          "peak_layer": 18
469	        },
470	        {
471	          "balanced_accuracy": 0.7757,
472	          "accuracy": 0.7757,
473	          "f1": 0.7589,
474	          "peak_layer": 16
475	        },
476	        {
477	          "balanced_accuracy": 0.7647,
478	          "accuracy": 0.7647,
479	          "f1": 0.7576,
480	          "peak_layer": 19
481	        },
482	        {
483	          "balanced_accuracy": 0.7537,
484	          "accuracy": 0.7537,
485	          "f1": 0.7472,
486	          "peak_layer": 13
487	        },
488	        {
489	          "balanced_accuracy": 0.7684,
490	          "accuracy": 0.7684,
491	          "f1": 0.7658,
492	          "peak_layer": 16
493	        },
494	        {
495	          "balanced_accuracy": 0.7684,
496	          "accuracy": 0.7684,
497	          "f1": 0.7709,
498	          "peak_layer": 13
499	        },
500	        {
501	          "balanced_accuracy": 0.7868,
502	          "accuracy": 0.7868,
503	          "f1": 0.7852,
504	          "peak_layer": 12
505	        },
506	        {
507	          "balanced_accuracy": 0.7684,
508	          "accuracy": 0.7684,
509	          "f1": 0.7568,
510	          "peak_layer": 22
511	        },
512	        {
513	          "balanced_accuracy": 0.7757,
514	          "accuracy": 0.7757,
515	          "f1": 0.7681,
516	          "peak_layer": 19
517	        },
518	        {
519	          "balanced_accuracy": 0.7794,
520	          "accuracy": 0.7794,
521	          "f1": 0.7857,
522	          "peak_layer": 29
523	        },
524	        {
525	          "balanced_accuracy": 0.7463,
526	          "accuracy": 0.7463,
527	          "f1": 0.7416,
528	          "peak_layer": 10
529	        },
530	        {
531	          "balanced_accuracy": 0.7684,
532	          "accuracy": 0.7684,
533	          "f1": 0.7586,
534	          "peak_layer": 16
535	        },
536	        {
537	          "balanced_accuracy": 0.7757,
538	          "accuracy": 0.7757,
539	          "f1": 0.7798,
540	          "peak_layer": 12
541	        },
542	        {
543	          "balanced_accuracy": 0.7684,
544	          "accuracy": 0.7684,
545	          "f1": 0.7742,
546	          "peak_layer": 26
547	        },
548	        {
549	          "balanced_accuracy": 0.7426,
550	          "accuracy": 0.7426,
551	          "f1": 0.7348,
552	          "peak_layer": 16
553	        },
554	        {
555	          "balanced_accuracy": 0.7721,
556	          "accuracy": 0.7721,
557	          "f1": 0.777,
558	          "peak_layer": 23
559	        },
560	        {
561	          "balanced_accuracy": 0.7794,
562	          "accuracy": 0.7794,
563	          "f1": 0.7727,
564	          "peak_layer": 13
565	        },
566	        {
567	          "balanced_accuracy": 0.761,
568	          "accuracy": 0.761,
569	          "f1": 0.7566,
570	          "peak_layer": 28
571	        },
572	        {
573	          "balanced_accuracy": 0.7721,
574	          "accuracy": 0.7721,
575	          "f1": 0.7634,
576	          "peak_layer": 17
577	        },
578	        {
579	          "balanced_accuracy": 0.7904,
580	          "accuracy": 0.7904,
581	          "f1": 0.7957,
582	          "peak_layer": 22
583	        },
584	        {
585	          "balanced_accuracy": 0.7684,
586	          "accuracy": 0.7684,
587	          "f1": 0.7675,
588	          "peak_layer": 28
589	        },
590	        {
591	          "balanced_accuracy": 0.7574,
592	          "accuracy": 0.7574,
593	          "f1": 0.7537,
594	          "peak_layer": 13
595	        },
596	        {
597	          "balanced_accuracy": 0.7537,
598	          "accuracy": 0.7537,
599	          "f1": 0.7433,
600	          "peak_layer": 12
601	        },
602	        {
603	          "balanced_accuracy": 0.7904,
604	          "accuracy": 0.7904,
605	          "f1": 0.7897,
606	          "peak_layer": 22
607	        },
608	        {
609	          "balanced_accuracy": 0.7574,
610	          "accuracy": 0.7574,
611	          "f1": 0.7574,
612	          "peak_layer": 29
613	        },
614	        {
615	          "balanced_accuracy": 0.7647,
616	          "accuracy": 0.7647,
617	          "f1": 0.7594,
618	          "peak_layer": 14
619	        },
620	        {
621	          "balanced_accuracy": 0.7721,
622	          "accuracy": 0.7721,
623	          "f1": 0.7634,
624	          "peak_layer": 18
625	        },
626	        {
627	          "balanced_accuracy": 0.7684,
628	          "accuracy": 0.7684,
629	          "f1": 0.7605,
630	          "peak_layer": 13
631	        },
632	        {
633	          "balanced_accuracy": 0.761,
634	          "accuracy": 0.761,
635	          "f1": 0.7636,
636	          "peak_layer": 13
637	        },
638	        {
639	          "balanced_accuracy": 0.7757,
640	          "accuracy": 0.7757,
641	          "f1": 0.7698,
642	          "peak_layer": 16
643	        },
644	        {
645	          "balanced_accuracy": 0.7684,
646	          "accuracy": 0.7684,
647	          "f1": 0.7726,
648	          "peak_layer": 11
649	        },
650	        {
651	          "balanced_accuracy": 0.761,
652	          "accuracy": 0.761,
653	          "f1": 0.7584,
654	          "peak_layer": 13
655	        },
656	        {
657	          "balanced_accuracy": 0.7831,
658	          "accuracy": 0.7831,
659	          "f1": 0.7739,
660	          "peak_layer": 18
661	        },
662	        {
663	          "balanced_accuracy": 0.7684,
664	          "accuracy": 0.7684,
665	          "f1": 0.7658,
666	          "peak_layer": 20
667	        },
668	        {
669	          "balanced_accuracy": 0.7684,
670	          "accuracy": 0.7684,
671	          "f1": 0.7549,
672	          "peak_layer": 17
673	        },
674	        {
675	          "balanced_accuracy": 0.7684,
676	          "accuracy": 0.7684,
677	          "f1": 0.7658,
678	          "peak_layer": 18
679	        },
680	        {
681	          "balanced_accuracy": 0.7537,
682	          "accuracy": 0.7537,
683	          "f1": 0.7452,
684	          "peak_layer": 16
685	        },
686	        {
687	          "balanced_accuracy": 0.7904,
688	          "accuracy": 0.7904,
689	          "f1": 0.7897,
690	          "peak_layer": 21
691	        },
692	        {
693	          "balanced_accuracy": 0.761,
694	          "accuracy": 0.761,
695	          "f1": 0.767,
696	          "peak_layer": 22
697	        },
698	        {
699	          "balanced_accuracy": 0.7684,
700	          "accuracy": 0.7684,
701	          "f1": 0.7568,
702	          "peak_layer": 19
703	        },
704	        {
705	          "balanced_accuracy": 0.7647,
706	          "accuracy": 0.7647,
707	          "f1": 0.763,
708	          "peak_layer": 20
709	        },
710	        {
711	          "balanced_accuracy": 0.761,
712	          "accuracy": 0.761,
713	          "f1": 0.7636,
714	          "peak_layer": 26
715	        }
716	      ]
717	    },
718	    "ZH\u2192ZH": {
719	      "direction": "ZH\u2192ZH",
720	      "n_bootstrap": 100,
721	      "balanced_accuracy_mean": 0.7124,
722	      "balanced_accuracy_std": 0.0127,
723	      "f1_mean": 0.7135,
724	      "f1_std": 0.0138,
725	      "peak_layers": [
726	        10,
727	        13,
728	        21,
729	        13,
730	        22,
731	        9,
732	        16,
733	        12,
734	        21,
735	        19,
736	        12,
737	        13,
738	        13,
739	        26,
740	        15,
741	        15,
742	        14,
743	        14,
744	        15,
745	        16,
746	        13,
747	        6,
748	        23,
749	        10,
750	        25,
751	        17,
752	        28,
753	        13,
754	        16,
755	        13,
756	        13,
757	        10,
758	        13,
759	        6,
760	        13,
761	        23,
762	        13,
763	        20,
764	        13,
765	        13,
766	        14,
767	        14,
768	        13,
769	        23,
770	        23,
771	        16,
772	        13,
773	        16,
774	        13,
775	        13,
776	        19,
777	        11,
778	        15,
779	        14,
780	        7,
781	        16,
782	        10,
783	        16,
784	        20,
785	        16,
786	        13,
787	        22,
788	        22,
789	        15,
790	        13,
791	        19,
792	        10,
793	        13,
794	        21,
795	        16,
796	        16,
797	        15,
798	        14,
799	        13,
800	        8,
801	        13,
802	        21,
803	        19,
804	        10,
805	        21,
806	        13,
807	        13,
808	        13,
809	        23,
810	        16,
811	        13,
812	        12,
813	        16,
814	        16,
815	        22,
816	        21,
817	        16,
818	        13,
819	        10,
820	        25,
821	        22,
822	        13,
823	        19,
824	        22,
825	        13
826	      ],
827	      "per_bootstrap": [
828	        {
829	          "balanced_accuracy": 0.7022,
830	          "accuracy": 0.7022,
831	          "f1": 0.7055,
832	          "peak_layer": 10
833	        },
834	        {
835	          "balanced_accuracy": 0.7169,
836	          "accuracy": 0.7169,
837	          "f1": 0.7159,
838	          "peak_layer": 13
839	        },
840	        {
841	          "balanced_accuracy": 0.6875,
842	          "accuracy": 0.6875,
843	          "f1": 0.6909,
844	          "peak_layer": 21
845	        },
846	        {
847	          "balanced_accuracy": 0.7022,
848	          "accuracy": 0.7022,
849	          "f1": 0.7097,
850	          "peak_layer": 13
851	        },
852	        {
853	          "balanced_accuracy": 0.7206,
854	          "accuracy": 0.7206,
855	          "f1": 0.7143,
856	          "peak_layer": 22
857	        },
858	        {
859	          "balanced_accuracy": 0.6985,
860	          "accuracy": 0.6985,
861	          "f1": 0.6963,
862	          "peak_layer": 9
863	        },
864	        {
865	          "balanced_accuracy": 0.7096,
866	          "accuracy": 0.7096,
867	          "f1": 0.6973,
868	          "peak_layer": 16
869	        },
870	        {
871	          "balanced_accuracy": 0.7022,
872	          "accuracy": 0.7022,
873	          "f1": 0.7011,
874	          "peak_layer": 12
875	        },
876	        {
877	          "balanced_accuracy": 0.7243,
878	          "accuracy": 0.7243,
879	          "f1": 0.7292,
880	          "peak_layer": 21
881	        },
882	        {
883	          "balanced_accuracy": 0.7169,
884	          "accuracy": 0.7169,
885	          "f1": 0.705,
886	          "peak_layer": 19
887	        },
888	        {
889	          "balanced_accuracy": 0.7059,
890	          "accuracy": 0.7059,
891	          "f1": 0.708,
892	          "peak_layer": 12
893	        },
894	        {
895	          "balanced_accuracy": 0.7169,
896	          "accuracy": 0.7169,
897	          "f1": 0.7279,
898	          "peak_layer": 13
899	        },
900	        {
901	          "balanced_accuracy": 0.7132,
902	          "accuracy": 0.7132,
903	          "f1": 0.7111,
904	          "peak_layer": 13
905	        },
906	        {
907	          "balanced_accuracy": 0.7243,
908	          "accuracy": 0.7243,
909	          "f1": 0.735,
910	          "peak_layer": 26
911	        },
912	        {
913	          "balanced_accuracy": 0.6912,
914	          "accuracy": 0.6912,
915	          "f1": 0.6842,
916	          "peak_layer": 15
917	        },
918	        {
919	          "balanced_accuracy": 0.7022,
920	          "accuracy": 0.7022,
921	          "f1": 0.7076,
922	          "peak_layer": 15
923	        },
924	        {
925	          "balanced_accuracy": 0.6949,
926	          "accuracy": 0.6949,
927	          "f1": 0.7046,
928	          "peak_layer": 14
929	        },
930	        {
931	          "balanced_accuracy": 0.7096,
932	          "accuracy": 0.7096,
933	          "f1": 0.7208,
934	          "peak_layer": 14
935	        },
936	        {
937	          "balanced_accuracy": 0.7426,
938	          "accuracy": 0.7426,
939	          "f1": 0.7388,
940	          "peak_layer": 15
941	        },
942	        {
943	          "balanced_accuracy": 0.6949,
944	          "accuracy": 0.6949,
945	          "f1": 0.6891,
946	          "peak_layer": 16
947	        },
948	        {
949	          "balanced_accuracy": 0.7059,
950	          "accuracy": 0.7059,
951	          "f1": 0.7059,
952	          "peak_layer": 13
953	        },
954	        {
955	          "balanced_accuracy": 0.7243,
956	          "accuracy": 0.7243,
957	          "f1": 0.744,
958	          "peak_layer": 6
959	        },
960	        {
961	          "balanced_accuracy": 0.739,
962	          "accuracy": 0.739,
963	          "f1": 0.7321,
964	          "peak_layer": 23
965	        },
966	        {
967	          "balanced_accuracy": 0.7096,
968	          "accuracy": 0.7096,
969	          "f1": 0.7189,
970	          "peak_layer": 10
971	        },
972	        {
973	          "balanced_accuracy": 0.7059,
974	          "accuracy": 0.7059,
975	          "f1": 0.6992,
976	          "peak_layer": 25
977	        },
978	        {
979	          "balanced_accuracy": 0.739,
980	          "accuracy": 0.739,
981	          "f1": 0.7399,
982	          "peak_layer": 17
983	        },
984	        {
985	          "balanced_accuracy": 0.7022,
986	          "accuracy": 0.7022,
987	          "f1": 0.7178,
988	          "peak_layer": 28
989	        },
990	        {
991	          "balanced_accuracy": 0.7059,
992	          "accuracy": 0.7059,
993	          "f1": 0.7059,
994	          "peak_layer": 13
995	        },
996	        {
997	          "balanced_accuracy": 0.7169,
998	          "accuracy": 0.7169,
999	          "f1": 0.72,
1000	          "peak_layer": 16
1001	        },
1002	        {
1003	          "balanced_accuracy": 0.6985,
1004	          "accuracy": 0.6985,
1005	          "f1": 0.7007,
1006	          "peak_layer": 13
1007	        },
1008	        {
1009	          "balanced_accuracy": 0.7169,
1010	          "accuracy": 0.7169,
1011	          "f1": 0.72,
1012	          "peak_layer": 13
1013	        },
1014	        {
1015	          "balanced_accuracy": 0.6801,
1016	          "accuracy": 0.6801,
1017	          "f1": 0.679,
1018	          "peak_layer": 10
1019	        },
1020	        {
1021	          "balanced_accuracy": 0.6985,
1022	          "accuracy": 0.6985,
1023	          "f1": 0.705,
1024	          "peak_layer": 13
1025	        },
1026	        {
1027	          "balanced_accuracy": 0.7096,
1028	          "accuracy": 0.7096,
1029	          "f1": 0.6996,
1030	          "peak_layer": 6
1031	        },
1032	        {
1033	          "balanced_accuracy": 0.7169,
1034	          "accuracy": 0.7169,
1035	          "f1": 0.722,
1036	          "peak_layer": 13
1037	        },
1038	        {
1039	          "balanced_accuracy": 0.7279,
1040	          "accuracy": 0.7279,
1041	          "f1": 0.7338,
1042	          "peak_layer": 23
1043	        },
1044	        {
1045	          "balanced_accuracy": 0.7096,
1046	          "accuracy": 0.7096,
1047	          "f1": 0.7085,
1048	          "peak_layer": 13
1049	        },
1050	        {
1051	          "balanced_accuracy": 0.7022,
1052	          "accuracy": 0.7022,
1053	          "f1": 0.6966,
1054	          "peak_layer": 20
1055	        },
1056	        {
1057	          "balanced_accuracy": 0.7096,
1058	          "accuracy": 0.7096,
1059	          "f1": 0.7019,
1060	          "peak_layer": 13
1061	        },
1062	        {
1063	          "balanced_accuracy": 0.7059,
1064	          "accuracy": 0.7059,
1065	          "f1": 0.7037,
1066	          "peak_layer": 13
1067	        },
1068	        {
1069	          "balanced_accuracy": 0.7206,
1070	          "accuracy": 0.7206,
1071	          "f1": 0.7143,
1072	          "peak_layer": 14
1073	        },
1074	        {
1075	          "balanced_accuracy": 0.7243,
1076	          "accuracy": 0.7243,
1077	          "f1": 0.717,
1078	          "peak_layer": 14
1079	        },
1080	        {
1081	          "balanced_accuracy": 0.6912,
1082	          "accuracy": 0.6912,
1083	          "f1": 0.6719,
1084	          "peak_layer": 13
1085	        },
1086	        {
1087	          "balanced_accuracy": 0.7059,
1088	          "accuracy": 0.7059,
1089	          "f1": 0.7101,
1090	          "peak_layer": 23
1091	        },
1092	        {
1093	          "balanced_accuracy": 0.7243,
1094	          "accuracy": 0.7243,
1095	          "f1": 0.7232,
1096	          "peak_layer": 23
1097	        },
1098	        {
1099	          "balanced_accuracy": 0.7243,
1100	          "accuracy": 0.7243,
1101	          "f1": 0.7273,
1102	          "peak_layer": 16
1103	        },
1104	        {
1105	          "balanced_accuracy": 0.7059,
1106	          "accuracy": 0.7059,
1107	          "f1": 0.7143,
1108	          "peak_layer": 13
1109	        },
1110	        {
1111	          "balanced_accuracy": 0.7059,
1112	          "accuracy": 0.7059,
1113	          "f1": 0.697,
1114	          "peak_layer": 16
1115	        },
1116	        {
1117	          "balanced_accuracy": 0.7279,
1118	          "accuracy": 0.7279,
1119	          "f1": 0.7259,
1120	          "peak_layer": 13
1121	        },
1122	        {
1123	          "balanced_accuracy": 0.7243,
1124	          "accuracy": 0.7243,
1125	          "f1": 0.7253,
1126	          "peak_layer": 13
1127	        },
1128	        {
1129	          "balanced_accuracy": 0.7096,
1130	          "accuracy": 0.7096,
1131	          "f1": 0.7041,
1132	          "peak_layer": 19
1133	        },
1134	        {
1135	          "balanced_accuracy": 0.7059,
1136	          "accuracy": 0.7059,
1137	          "f1": 0.7101,
1138	          "peak_layer": 11
1139	        },
1140	        {
1141	          "balanced_accuracy": 0.7059,
1142	          "accuracy": 0.7059,
1143	          "f1": 0.7101,
1144	          "peak_layer": 15
1145	        },
1146	        {
1147	          "balanced_accuracy": 0.7353,
1148	          "accuracy": 0.7353,
1149	          "f1": 0.7534,
1150	          "peak_layer": 14
1151	        },
1152	        {
1153	          "balanced_accuracy": 0.7059,
1154	          "accuracy": 0.7059,
1155	          "f1": 0.7059,
1156	          "peak_layer": 7
1157	        },
1158	        {
1159	          "balanced_accuracy": 0.7279,
1160	          "accuracy": 0.7279,
1161	          "f1": 0.7259,
1162	          "peak_layer": 16
1163	        },
1164	        {
1165	          "balanced_accuracy": 0.7132,
1166	          "accuracy": 0.7132,
1167	          "f1": 0.7153,
1168	          "peak_layer": 10
1169	        },
1170	        {
1171	          "balanced_accuracy": 0.7059,
1172	          "accuracy": 0.7059,
1173	          "f1": 0.6992,
1174	          "peak_layer": 16
1175	        },
1176	        {
1177	          "balanced_accuracy": 0.7022,
1178	          "accuracy": 0.7022,
1179	          "f1": 0.7033,
1180	          "peak_layer": 20
1181	        },
1182	        {
1183	          "balanced_accuracy": 0.7132,
1184	          "accuracy": 0.7132,
1185	          "f1": 0.7068,
1186	          "peak_layer": 16
1187	        },
1188	        {
1189	          "balanced_accuracy": 0.7096,
1190	          "accuracy": 0.7096,
1191	          "f1": 0.7168,
1192	          "peak_layer": 13
1193	        },
1194	        {
1195	          "balanced_accuracy": 0.7132,
1196	          "accuracy": 0.7132,
1197	          "f1": 0.7234,
1198	          "peak_layer": 22
1199	        },
1200	        {
1201	          "balanced_accuracy": 0.6838,
1202	          "accuracy": 0.6838,
1203	          "f1": 0.6972,
1204	          "peak_layer": 22
1205	        },
1206	        {
1207	          "balanced_accuracy": 0.7206,
1208	          "accuracy": 0.7206,
1209	          "f1": 0.7206,
1210	          "peak_layer": 15
1211	        },
1212	        {
1213	          "balanced_accuracy": 0.7206,
1214	          "accuracy": 0.7206,
1215	          "f1": 0.7143,
1216	          "peak_layer": 13
1217	        },
1218	        {
1219	          "balanced_accuracy": 0.7096,
1220	          "accuracy": 0.7096,
1221	          "f1": 0.7148,
1222	          "peak_layer": 19
1223	        },
1224	        {
1225	          "balanced_accuracy": 0.7169,
1226	          "accuracy": 0.7169,
1227	          "f1": 0.7179,
1228	          "peak_layer": 10
1229	        },
1230	        {
1231	          "balanced_accuracy": 0.7022,
1232	          "accuracy": 0.7022,
1233	          "f1": 0.7011,
1234	          "peak_layer": 13
1235	        },
1236	        {
1237	          "balanced_accuracy": 0.7132,
1238	          "accuracy": 0.7132,
1239	          "f1": 0.7153,
1240	          "peak_layer": 21
1241	        },
1242	        {
1243	          "balanced_accuracy": 0.7353,
1244	          "accuracy": 0.7353,
1245	          "f1": 0.7353,
1246	          "peak_layer": 16
1247	        },
1248	        {
1249	          "balanced_accuracy": 0.7169,
1250	          "accuracy": 0.7169,
1251	          "f1": 0.724,
1252	          "peak_layer": 16
1253	        },
1254	        {
1255	          "balanced_accuracy": 0.7279,
1256	          "accuracy": 0.7279,
1257	          "f1": 0.7299,
1258	          "peak_layer": 15
1259	        },
1260	        {
1261	          "balanced_accuracy": 0.7022,
1262	          "accuracy": 0.7022,
1263	          "f1": 0.7097,
1264	          "peak_layer": 14
1265	        },
1266	        {
1267	          "balanced_accuracy": 0.7279,
1268	          "accuracy": 0.7279,
1269	          "f1": 0.7299,
1270	          "peak_layer": 13
1271	        },
1272	        {
1273	          "balanced_accuracy": 0.6912,
1274	          "accuracy": 0.6912,
1275	          "f1": 0.6957,
1276	          "peak_layer": 8
1277	        },
1278	        {
1279	          "balanced_accuracy": 0.739,
1280	          "accuracy": 0.739,
1281	          "f1": 0.738,
1282	          "peak_layer": 13
1283	        },
1284	        {
1285	          "balanced_accuracy": 0.7132,
1286	          "accuracy": 0.7132,
1287	          "f1": 0.7214,
1288	          "peak_layer": 21
1289	        },
1290	        {
1291	          "balanced_accuracy": 0.7169,
1292	          "accuracy": 0.7169,
1293	          "f1": 0.72,
1294	          "peak_layer": 19
1295	        },
1296	        {
1297	          "balanced_accuracy": 0.7096,
1298	          "accuracy": 0.7096,
1299	          "f1": 0.7106,
1300	          "peak_layer": 10
1301	        },
1302	        {
1303	          "balanced_accuracy": 0.7059,
1304	          "accuracy": 0.7059,
1305	          "f1": 0.7163,
1306	          "peak_layer": 21
1307	        },
1308	        {
1309	          "balanced_accuracy": 0.7096,
1310	          "accuracy": 0.7096,
1311	          "f1": 0.7063,
1312	          "peak_layer": 13
1313	        },
1314	        {
1315	          "balanced_accuracy": 0.7279,
1316	          "accuracy": 0.7279,
1317	          "f1": 0.7197,
1318	          "peak_layer": 13
1319	        },
1320	        {
1321	          "balanced_accuracy": 0.7243,
1322	          "accuracy": 0.7243,
1323	          "f1": 0.7126,
1324	          "peak_layer": 13
1325	        },
1326	        {
1327	          "balanced_accuracy": 0.7022,
1328	          "accuracy": 0.7022,
1329	          "f1": 0.7117,
1330	          "peak_layer": 23
1331	        },
1332	        {
1333	          "balanced_accuracy": 0.7243,
1334	          "accuracy": 0.7243,
1335	          "f1": 0.7232,
1336	          "peak_layer": 16
1337	        },
1338	        {
1339	          "balanced_accuracy": 0.7206,
1340	          "accuracy": 0.7206,
1341	          "f1": 0.7246,
1342	          "peak_layer": 13
1343	        },
1344	        {
1345	          "balanced_accuracy": 0.6985,
1346	          "accuracy": 0.6985,
1347	          "f1": 0.7007,
1348	          "peak_layer": 12
1349	        },
1350	        {
1351	          "balanced_accuracy": 0.7243,
1352	          "accuracy": 0.7243,
1353	          "f1": 0.7292,
1354	          "peak_layer": 16
1355	        },
1356	        {
1357	          "balanced_accuracy": 0.7353,
1358	          "accuracy": 0.7353,
1359	          "f1": 0.7231,
1360	          "peak_layer": 16
1361	        },
1362	        {
1363	          "balanced_accuracy": 0.7096,
1364	          "accuracy": 0.7096,
1365	          "f1": 0.7106,
1366	          "peak_layer": 22
1367	        },
1368	        {
1369	          "balanced_accuracy": 0.7096,
1370	          "accuracy": 0.7096,
1371	          "f1": 0.7085,
1372	          "peak_layer": 21
1373	        },
1374	        {
1375	          "balanced_accuracy": 0.7059,
1376	          "accuracy": 0.7059,
1377	          "f1": 0.7059,
1378	          "peak_layer": 16
1379	        },
1380	        {
1381	          "balanced_accuracy": 0.7132,
1382	          "accuracy": 0.7132,
1383	          "f1": 0.7132,
1384	          "peak_layer": 13
1385	        },
1386	        {
1387	          "balanced_accuracy": 0.7059,
1388	          "accuracy": 0.7059,
1389	          "f1": 0.7163,
1390	          "peak_layer": 10
1391	        },
1392	        {
1393	          "balanced_accuracy": 0.7132,
1394	          "accuracy": 0.7132,
1395	          "f1": 0.7234,
1396	          "peak_layer": 25
1397	        },
1398	        {
1399	          "balanced_accuracy": 0.7132,
1400	          "accuracy": 0.7132,
1401	          "f1": 0.7132,
1402	          "peak_layer": 22
1403	        },
1404	        {
1405	          "balanced_accuracy": 0.7243,
1406	          "accuracy": 0.7243,
1407	          "f1": 0.7212,
1408	          "peak_layer": 13
1409	        },
1410	        {
1411	          "balanced_accuracy": 0.6985,
1412	          "accuracy": 0.6985,
1413	          "f1": 0.7007,
1414	          "peak_layer": 19
1415	        },
1416	        {
1417	          "balanced_accuracy": 0.6912,
1418	          "accuracy": 0.6912,
1419	          "f1": 0.7,
1420	          "peak_layer": 22
1421	        },
1422	        {
1423	          "balanced_accuracy": 0.7316,
1424	          "accuracy": 0.7316,
1425	          "f1": 0.7306,
1426	          "peak_layer": 13
1427	        }
1428	      ]
1429	    },
1430	    "EN\u2192ZH": {
1431	      "direction": "EN\u2192ZH",
1432	      "n_bootstrap": 100,
1433	      "balanced_accuracy_mean": 0.6405,
1434	      "balanced_accuracy_std": 0.0245,
1435	      "f1_mean": 0.6747,
1436	      "f1_std": 0.0435,
1437	      "peak_layers": [
1438	        5,
1439	        17,
1440	        6,
1441	        13,
1442	        17,
1443	        5,
1444	        13,
1445	        5,
1446	        13,
1447	        13,
1448	        20,
1449	        13,
1450	        17,
1451	        12,
1452	        17,
1453	        13,
1454	        13,
1455	        13,
1456	        13,
1457	        6,
1458	        13,
1459	        7,
1460	        13,
1461	        27,
1462	        17,
1463	        19,
1464	        13,
1465	        24,
1466	        28,
1467	        17,
1468	        13,
1469	        6,
1470	        15,
1471	        13,
1472	        27,
1473	        23,
1474	        13,
1475	        15,
1476	        12,
1477	        20,
1478	        6,
1479	        6,
1480	        17,
1481	        13,
1482	        13,
1483	        5,
1484	        13,
1485	        6,
1486	        19,
1487	        13,
1488	        13,
1489	        11,
1490	        17,
1491	        13,
1492	        6,
1493	        15,
1494	        5,
1495	        5,
1496	        17,
1497	        13,
1498	        16,
1499	        5,
1500	        6,
1501	        13,
1502	        5,
1503	        13,
1504	        13,
1505	        6,
1506	        20,
1507	        30,
1508	        14,
1509	        5,
1510	        17,
1511	        27,
1512	        29,
1513	        19,
1514	        5,
1515	        23,
1516	        22,
1517	        16,
1518	        27,
1519	        11,
1520	        30,
1521	        6,
1522	        25,
1523	        20,
1524	        13,
1525	        20,
1526	        13,
1527	        17,
1528	        23,
1529	        13,
1530	        17,
1531	        5,
1532	        14,
1533	        5,
1534	        6,
1535	        17,
1536	        19,
1537	        6
1538	      ],
1539	      "per_bootstrap": [
1540	        {
1541	          "balanced_accuracy": 0.6544,
1542	          "accuracy": 0.6544,
1543	          "f1": 0.7134,
1544	          "peak_layer": 5
1545	        },
1546	        {
1547	          "balanced_accuracy": 0.6397,
1548	          "accuracy": 0.6397,
1549	          "f1": 0.6711,
1550	          "peak_layer": 17
1551	        },
1552	        {
1553	          "balanced_accuracy": 0.636,
1554	          "accuracy": 0.636,
1555	          "f1": 0.6775,
1556	          "peak_layer": 6
1557	        },
1558	        {
1559	          "balanced_accuracy": 0.6434,
1560	          "accuracy": 0.6434,
1561	          "f1": 0.7122,
1562	          "peak_layer": 13
1563	        },
1564	        {
1565	          "balanced_accuracy": 0.6103,
1566	          "accuracy": 0.6103,
1567	          "f1": 0.6443,
1568	          "peak_layer": 17
1569	        },
1570	        {
1571	          "balanced_accuracy": 0.6507,
1572	          "accuracy": 0.6507,
1573	          "f1": 0.6619,
1574	          "peak_layer": 5
1575	        },
1576	        {
1577	          "balanced_accuracy": 0.6544,
1578	          "accuracy": 0.6544,
1579	          "f1": 0.7219,
1580	          "peak_layer": 13
1581	        },
1582	        {
1583	          "balanced_accuracy": 0.6397,
1584	          "accuracy": 0.6397,
1585	          "f1": 0.6316,
1586	          "peak_layer": 5
1587	        },
1588	        {
1589	          "balanced_accuracy": 0.6801,
1590	          "accuracy": 0.6801,
1591	          "f1": 0.7273,
1592	          "peak_layer": 13
1593	        },
1594	        {
1595	          "balanced_accuracy": 0.6618,
1596	          "accuracy": 0.6618,
1597	          "f1": 0.7125,
1598	          "peak_layer": 13
1599	        },
1600	        {
1601	          "balanced_accuracy": 0.6324,
1602	          "accuracy": 0.6324,
1603	          "f1": 0.6552,
1604	          "peak_layer": 20
1605	        },
1606	        {
1607	          "balanced_accuracy": 0.6654,
1608	          "accuracy": 0.6654,
1609	          "f1": 0.6762,
1610	          "peak_layer": 13
1611	        },
1612	        {
1613	          "balanced_accuracy": 0.6434,
1614	          "accuracy": 0.6434,
1615	          "f1": 0.6523,
1616	          "peak_layer": 17
1617	        },
1618	        {
1619	          "balanced_accuracy": 0.6507,
1620	          "accuracy": 0.6507,
1621	          "f1": 0.7112,
1622	          "peak_layer": 12
1623	        },
1624	        {
1625	          "balanced_accuracy": 0.5993,
1626	          "accuracy": 0.5993,
1627	          "f1": 0.6964,
1628	          "peak_layer": 17
1629	        },
1630	        {
1631	          "balanced_accuracy": 0.6765,
1632	          "accuracy": 0.6765,
1633	          "f1": 0.7233,
1634	          "peak_layer": 13
1635	        },
1636	        {
1637	          "balanced_accuracy": 0.6765,
1638	          "accuracy": 0.6765,
1639	          "f1": 0.7365,
1640	          "peak_layer": 13
1641	        },
1642	        {
1643	          "balanced_accuracy": 0.6213,
1644	          "accuracy": 0.6213,
1645	          "f1": 0.7082,
1646	          "peak_layer": 13
1647	        },
1648	        {
1649	          "balanced_accuracy": 0.6434,
1650	          "accuracy": 0.6434,
1651	          "f1": 0.7172,
1652	          "peak_layer": 13
1653	        },
1654	        {
1655	          "balanced_accuracy": 0.6029,
1656	          "accuracy": 0.6029,
1657	          "f1": 0.6707,
1658	          "peak_layer": 6
1659	        },
1660	        {
1661	          "balanced_accuracy": 0.6397,
1662	          "accuracy": 0.6397,
1663	          "f1": 0.7083,
1664	          "peak_layer": 13
1665	        },
1666	        {
1667	          "balanced_accuracy": 0.5662,
1668	          "accuracy": 0.5662,
1669	          "f1": 0.5391,
1670	          "peak_layer": 7
1671	        },
1672	        {
1673	          "balanced_accuracy": 0.6213,
1674	          "accuracy": 0.6213,
1675	          "f1": 0.7099,
1676	          "peak_layer": 13
1677	        },
1678	        {
1679	          "balanced_accuracy": 0.636,
1680	          "accuracy": 0.636,
1681	          "f1": 0.5438,
1682	          "peak_layer": 27
1683	        },
1684	        {
1685	          "balanced_accuracy": 0.6434,
1686	          "accuracy": 0.6434,
1687	          "f1": 0.6756,
1688	          "peak_layer": 17
1689	        },
1690	        {
1691	          "balanced_accuracy": 0.6544,
1692	          "accuracy": 0.6544,
1693	          "f1": 0.6357,
1694	          "peak_layer": 19
1695	        },
1696	        {
1697	          "balanced_accuracy": 0.6949,
1698	          "accuracy": 0.6949,
1699	          "f1": 0.7414,
1700	          "peak_layer": 13
1701	        },
1702	        {
1703	          "balanced_accuracy": 0.6029,
1704	          "accuracy": 0.6029,
1705	          "f1": 0.6424,
1706	          "peak_layer": 24
1707	        },
1708	        {
1709	          "balanced_accuracy": 0.6397,
1710	          "accuracy": 0.6397,
1711	          "f1": 0.6573,
1712	          "peak_layer": 28
1713	        },
1714	        {
1715	          "balanced_accuracy": 0.614,
1716	          "accuracy": 0.614,
1717	          "f1": 0.6182,
1718	          "peak_layer": 17
1719	        },
1720	        {
1721	          "balanced_accuracy": 0.6618,
1722	          "accuracy": 0.6618,
1723	          "f1": 0.7294,
1724	          "peak_layer": 13
1725	        },
1726	        {
1727	          "balanced_accuracy": 0.614,
1728	          "accuracy": 0.614,
1729	          "f1": 0.7009,
1730	          "peak_layer": 6
1731	        },
1732	        {
1733	          "balanced_accuracy": 0.636,
1734	          "accuracy": 0.636,
1735	          "f1": 0.6426,
1736	          "peak_layer": 15
1737	        },
1738	        {
1739	          "balanced_accuracy": 0.6875,
1740	          "accuracy": 0.6875,
1741	          "f1": 0.7195,
1742	          "peak_layer": 13
1743	        },
1744	        {
1745	          "balanced_accuracy": 0.5993,
1746	          "accuracy": 0.5993,
1747	          "f1": 0.654,
1748	          "peak_layer": 27
1749	        },
1750	        {
1751	          "balanced_accuracy": 0.636,
1752	          "accuracy": 0.636,
1753	          "f1": 0.6897,
1754	          "peak_layer": 23
1755	        },
1756	        {
1757	          "balanced_accuracy": 0.6912,
1758	          "accuracy": 0.6912,
1759	          "f1": 0.7423,
1760	          "peak_layer": 13
1761	        },
1762	        {
1763	          "balanced_accuracy": 0.614,
1764	          "accuracy": 0.614,
1765	          "f1": 0.6974,
1766	          "peak_layer": 15
1767	        },
1768	        {
1769	          "balanced_accuracy": 0.6728,
1770	          "accuracy": 0.6728,
1771	          "f1": 0.712,
1772	          "peak_layer": 12
1773	        },
1774	        {
1775	          "balanced_accuracy": 0.6654,
1776	          "accuracy": 0.6654,
1777	          "f1": 0.6486,
1778	          "peak_layer": 20
1779	        },
1780	        {
1781	          "balanced_accuracy": 0.6434,
1782	          "accuracy": 0.6434,
1783	          "f1": 0.6473,
1784	          "peak_layer": 6
1785	        },
1786	        {
1787	          "balanced_accuracy": 0.625,
1788	          "accuracy": 0.625,
1789	          "f1": 0.6792,
1790	          "peak_layer": 6
1791	        },
1792	        {
1793	          "balanced_accuracy": 0.6434,
1794	          "accuracy": 0.6434,
1795	          "f1": 0.6921,
1796	          "peak_layer": 17
1797	        },
1798	        {
1799	          "balanced_accuracy": 0.636,
1800	          "accuracy": 0.636,
1801	          "f1": 0.7097,
1802	          "peak_layer": 13
1803	        },
1804	        {
1805	          "balanced_accuracy": 0.6397,
1806	          "accuracy": 0.6397,
1807	          "f1": 0.7048,
1808	          "peak_layer": 13
1809	        },
1810	        {
1811	          "balanced_accuracy": 0.636,
1812	          "accuracy": 0.636,
1813	          "f1": 0.6574,
1814	          "peak_layer": 5
1815	        },
1816	        {
1817	          "balanced_accuracy": 0.6765,
1818	          "accuracy": 0.6765,
1819	          "f1": 0.6857,
1820	          "peak_layer": 13
1821	        },
1822	        {
1823	          "balanced_accuracy": 0.6176,
1824	          "accuracy": 0.6176,
1825	          "f1": 0.6463,
1826	          "peak_layer": 6
1827	        },
1828	        {
1829	          "balanced_accuracy": 0.6471,
1830	          "accuracy": 0.6471,
1831	          "f1": 0.6336,
1832	          "peak_layer": 19
1833	        },
1834	        {
1835	          "balanced_accuracy": 0.6471,
1836	          "accuracy": 0.6471,
1837	          "f1": 0.7209,
1838	          "peak_layer": 13
1839	        },
1840	        {
1841	          "balanced_accuracy": 0.6728,
1842	          "accuracy": 0.6728,
1843	          "f1": 0.7327,
1844	          "peak_layer": 13
1845	        },
1846	        {
1847	          "balanced_accuracy": 0.6507,
1848	          "accuracy": 0.6507,
1849	          "f1": 0.6468,
1850	          "peak_layer": 11
1851	        },
1852	        {
1853	          "balanced_accuracy": 0.6287,
1854	          "accuracy": 0.6287,
1855	          "f1": 0.6553,
1856	          "peak_layer": 17
1857	        },
1858	        {
1859	          "balanced_accuracy": 0.6507,
1860	          "accuracy": 0.6507,
1861	          "f1": 0.7246,
1862	          "peak_layer": 13
1863	        },
1864	        {
1865	          "balanced_accuracy": 0.6544,
1866	          "accuracy": 0.6544,
1867	          "f1": 0.6594,
1868	          "peak_layer": 6
1869	        },
1870	        {
1871	          "balanced_accuracy": 0.6507,
1872	          "accuracy": 0.6507,
1873	          "f1": 0.7112,
1874	          "peak_layer": 15
1875	        },
1876	        {
1877	          "balanced_accuracy": 0.6213,
1878	          "accuracy": 0.6213,
1879	          "f1": 0.6023,
1880	          "peak_layer": 5
1881	        },
1882	        {
1883	          "balanced_accuracy": 0.6544,
1884	          "accuracy": 0.6544,
1885	          "f1": 0.6908,
1886	          "peak_layer": 5
1887	        },
1888	        {
1889	          "balanced_accuracy": 0.6324,
1890	          "accuracy": 0.6324,
1891	          "f1": 0.6575,
1892	          "peak_layer": 17
1893	        },
1894	        {
1895	          "balanced_accuracy": 0.6949,
1896	          "accuracy": 0.6949,
1897	          "f1": 0.7167,
1898	          "peak_layer": 13
1899	        },
1900	        {
1901	          "balanced_accuracy": 0.6287,
1902	          "accuracy": 0.6287,
1903	          "f1": 0.6967,
1904	          "peak_layer": 16
1905	        },
1906	        {
1907	          "balanced_accuracy": 0.6434,
1908	          "accuracy": 0.6434,
1909	          "f1": 0.7015,
1910	          "peak_layer": 5
1911	        },
1912	        {
1913	          "balanced_accuracy": 0.625,
1914	          "accuracy": 0.625,
1915	          "f1": 0.7,
1916	          "peak_layer": 6
1917	        },
1918	        {
1919	          "balanced_accuracy": 0.6985,
1920	          "accuracy": 0.6985,
1921	          "f1": 0.7438,
1922	          "peak_layer": 13
1923	        },
1924	        {
1925	          "balanced_accuracy": 0.6654,
1926	          "accuracy": 0.6654,
1927	          "f1": 0.6286,
1928	          "peak_layer": 5
1929	        },
1930	        {
1931	          "balanced_accuracy": 0.636,
1932	          "accuracy": 0.636,
1933	          "f1": 0.713,
1934	          "peak_layer": 13
1935	        },
1936	        {
1937	          "balanced_accuracy": 0.6434,
1938	          "accuracy": 0.6434,
1939	          "f1": 0.7122,
1940	          "peak_layer": 13
1941	        },
1942	        {
1943	          "balanced_accuracy": 0.6397,
1944	          "accuracy": 0.6397,
1945	          "f1": 0.608,
1946	          "peak_layer": 6
1947	        },
1948	        {
1949	          "balanced_accuracy": 0.6618,
1950	          "accuracy": 0.6618,
1951	          "f1": 0.6406,
1952	          "peak_layer": 20
1953	        },
1954	        {
1955	          "balanced_accuracy": 0.6066,
1956	          "accuracy": 0.6066,
1957	          "f1": 0.6646,
1958	          "peak_layer": 30
1959	        },
1960	        {
1961	          "balanced_accuracy": 0.6507,
1962	          "accuracy": 0.6507,
1963	          "f1": 0.7164,
1964	          "peak_layer": 14
1965	        },
1966	        {
1967	          "balanced_accuracy": 0.6618,
1968	          "accuracy": 0.6618,
1969	          "f1": 0.6068,
1970	          "peak_layer": 5
1971	        },
1972	        {
1973	          "balanced_accuracy": 0.6176,
1974	          "accuracy": 0.6176,
1975	          "f1": 0.5357,
1976	          "peak_layer": 17
1977	        },
1978	        {
1979	          "balanced_accuracy": 0.6287,
1980	          "accuracy": 0.6287,
1981	          "f1": 0.6354,
1982	          "peak_layer": 27
1983	        },
1984	        {
1985	          "balanced_accuracy": 0.614,
1986	          "accuracy": 0.614,
1987	          "f1": 0.6688,
1988	          "peak_layer": 29
1989	        },
1990	        {
1991	          "balanced_accuracy": 0.6029,
1992	          "accuracy": 0.6029,
1993	          "f1": 0.6087,
1994	          "peak_layer": 19
1995	        },
1996	        {
1997	          "balanced_accuracy": 0.6213,
1998	          "accuracy": 0.6213,
1999	          "f1": 0.6084,
2000	          "peak_layer": 5
2001	        },
2002	        {
2003	          "balanced_accuracy": 0.6765,
2004	          "accuracy": 0.6765,
2005	          "f1": 0.7067,
2006	          "peak_layer": 23
2007	        },
2008	        {
2009	          "balanced_accuracy": 0.6581,
2010	          "accuracy": 0.6581,
2011	          "f1": 0.6353,
2012	          "peak_layer": 22
2013	        },
2014	        {
2015	          "balanced_accuracy": 0.625,
2016	          "accuracy": 0.625,
2017	          "f1": 0.7052,
2018	          "peak_layer": 16
2019	        },
2020	        {
2021	          "balanced_accuracy": 0.6287,
2022	          "accuracy": 0.6287,
2023	          "f1": 0.6599,
2024	          "peak_layer": 27
2025	        },
2026	        {
2027	          "balanced_accuracy": 0.6287,
2028	          "accuracy": 0.6287,
2029	          "f1": 0.6814,
2030	          "peak_layer": 11
2031	        },
2032	        {
2033	          "balanced_accuracy": 0.6213,
2034	          "accuracy": 0.6213,
2035	          "f1": 0.6709,
2036	          "peak_layer": 30
2037	        },
2038	        {
2039	          "balanced_accuracy": 0.636,
2040	          "accuracy": 0.636,
2041	          "f1": 0.6837,
2042	          "peak_layer": 6
2043	        },
2044	        {
2045	          "balanced_accuracy": 0.6103,
2046	          "accuracy": 0.6103,
2047	          "f1": 0.6103,
2048	          "peak_layer": 25
2049	        },
2050	        {
2051	          "balanced_accuracy": 0.6287,
2052	          "accuracy": 0.6287,
2053	          "f1": 0.6406,
2054	          "peak_layer": 20
2055	        },
2056	        {
2057	          "balanced_accuracy": 0.5993,
2058	          "accuracy": 0.5993,
2059	          "f1": 0.7078,
2060	          "peak_layer": 13
2061	        },
2062	        {
2063	          "balanced_accuracy": 0.6397,
2064	          "accuracy": 0.6397,
2065	          "f1": 0.6776,
2066	          "peak_layer": 20
2067	        },
2068	        {
2069	          "balanced_accuracy": 0.625,
2070	          "accuracy": 0.625,
2071	          "f1": 0.7086,
2072	          "peak_layer": 13
2073	        },
2074	        {
2075	          "balanced_accuracy": 0.6471,
2076	          "accuracy": 0.6471,
2077	          "f1": 0.6336,
2078	          "peak_layer": 17
2079	        },
2080	        {
2081	          "balanced_accuracy": 0.6434,
2082	          "accuracy": 0.6434,
2083	          "f1": 0.6921,
2084	          "peak_layer": 23
2085	        },
2086	        {
2087	          "balanced_accuracy": 0.6507,
2088	          "accuracy": 0.6507,
2089	          "f1": 0.7164,
2090	          "peak_layer": 13
2091	        },
2092	        {
2093	          "balanced_accuracy": 0.6471,
2094	          "accuracy": 0.6471,
2095	          "f1": 0.7055,
2096	          "peak_layer": 17
2097	        },
2098	        {
2099	          "balanced_accuracy": 0.6176,
2100	          "accuracy": 0.6176,
2101	          "f1": 0.6119,
2102	          "peak_layer": 5
2103	        },
2104	        {
2105	          "balanced_accuracy": 0.625,
2106	          "accuracy": 0.625,
2107	          "f1": 0.6852,
2108	          "peak_layer": 14
2109	        },
2110	        {
2111	          "balanced_accuracy": 0.6507,
2112	          "accuracy": 0.6507,
2113	          "f1": 0.669,
2114	          "peak_layer": 5
2115	        },
2116	        {
2117	          "balanced_accuracy": 0.6838,
2118	          "accuracy": 0.6838,
2119	          "f1": 0.6532,
2120	          "peak_layer": 6
2121	        },
2122	        {
2123	          "balanced_accuracy": 0.614,
2124	          "accuracy": 0.614,
2125	          "f1": 0.6903,
2126	          "peak_layer": 17
2127	        },
2128	        {
2129	          "balanced_accuracy": 0.5956,
2130	          "accuracy": 0.5956,
2131	          "f1": 0.6284,
2132	          "peak_layer": 19
2133	        },
2134	        {
2135	          "balanced_accuracy": 0.6581,
2136	          "accuracy": 0.6581,
2137	          "f1": 0.7066,
2138	          "peak_layer": 6
2139	        }
2140	      ]
2141	    },
2142	    "ZH\u2192EN": {
2143	      "direction": "ZH\u2192EN",
2144	      "n_bootstrap": 100,
2145	      "balanced_accuracy_mean": 0.7127,
2146	      "balanced_accuracy_std": 0.027,
2147	      "f1_mean": 0.7282,
2148	      "f1_std": 0.0352,
2149	      "peak_layers": [
2150	        9,
2151	        16,
2152	        14,
2153	        14,
2154	        9,
2155	        1,
2156	        25,
2157	        14,
2158	        24,
2159	        5,
2160	        15,
2161	        16,
2162	        15,
2163	        9,
2164	        7,
2165	        16,
2166	        15,
2167	        9,
2168	        15,
2169	        18,
2170	        15,
2171	        23,
2172	        23,
2173	        17,
2174	        15,
2175	        9,
2176	        12,
2177	        15,
2178	        15,
2179	        9,
2180	        15,
2181	        15,
2182	        9,
2183	        15,
2184	        9,
2185	        1,
2186	        16,
2187	        15,
2188	        17,
2189	        15,
2190	        21,
2191	        15,
2192	        16,
2193	        25,
2194	        15,
2195	        9,
2196	        15,
2197	        18,
2198	        15,
2199	        15,
2200	        16,
2201	        17,
2202	        15,
2203	        9,
2204	        23,
2205	        14,
2206	        25,
2207	        9,
2208	        16,
2209	        15,
2210	        9,
2211	        15,
2212	        20,
2213	        15,
2214	        9,
2215	        16,
2216	        15,
2217	        0,
2218	        9,
2219	        11,
2220	        17,
2221	        20,
2222	        15,
2223	        7,
2224	        20,
2225	        13,
2226	        13,
2227	        9,
2228	        15,
2229	        15,
2230	        19,
2231	        11,
2232	        5,
2233	        9,
2234	        17,
2235	        14,
2236	        3,
2237	        17,
2238	        15,
2239	        15,
2240	        21,
2241	        9,
2242	        9,
2243	        24,
2244	        17,
2245	        15,
2246	        15,
2247	        5,
2248	        12,
2249	        19
2250	      ],
2251	      "per_bootstrap": [
2252	        {
2253	          "balanced_accuracy": 0.7059,
2254	          "accuracy": 0.7059,
2255	          "f1": 0.708,
2256	          "peak_layer": 9
2257	        },
2258	        {
2259	          "balanced_accuracy": 0.7353,
2260	          "accuracy": 0.7353,
2261	          "f1": 0.7632,
2262	          "peak_layer": 16
2263	        },
2264	        {
2265	          "balanced_accuracy": 0.7537,
2266	          "accuracy": 0.7537,
2267	          "f1": 0.7729,
2268	          "peak_layer": 14
2269	        },
2270	        {
2271	          "balanced_accuracy": 0.6691,
2272	          "accuracy": 0.6691,
2273	          "f1": 0.7384,
2274	          "peak_layer": 14
2275	        },
2276	        {
2277	          "balanced_accuracy": 0.7206,
2278	          "accuracy": 0.7206,
2279	          "f1": 0.6833,
2280	          "peak_layer": 9
2281	        },
2282	        {
2283	          "balanced_accuracy": 0.6618,
2284	          "accuracy": 0.6618,
2285	          "f1": 0.7229,
2286	          "peak_layer": 1
2287	        },
2288	        {
2289	          "balanced_accuracy": 0.7096,
2290	          "accuracy": 0.7096,
2291	          "f1": 0.7443,
2292	          "peak_layer": 25
2293	        },
2294	        {
2295	          "balanced_accuracy": 0.7059,
2296	          "accuracy": 0.7059,
2297	          "f1": 0.6992,
2298	          "peak_layer": 14
2299	        },
2300	        {
2301	          "balanced_accuracy": 0.6985,
2302	          "accuracy": 0.6985,
2303	          "f1": 0.732,
2304	          "peak_layer": 24
2305	        },
2306	        {
2307	          "balanced_accuracy": 0.7316,
2308	          "accuracy": 0.7316,
2309	          "f1": 0.7181,
2310	          "peak_layer": 5
2311	        },
2312	        {
2313	          "balanced_accuracy": 0.7426,
2314	          "accuracy": 0.7426,
2315	          "f1": 0.7445,
2316	          "peak_layer": 15
2317	        },
2318	        {
2319	          "balanced_accuracy": 0.7096,
2320	          "accuracy": 0.7096,
2321	          "f1": 0.746,
2322	          "peak_layer": 16
2323	        },
2324	        {
2325	          "balanced_accuracy": 0.6765,
2326	          "accuracy": 0.6765,
2327	          "f1": 0.7349,
2328	          "peak_layer": 15
2329	        },
2330	        {
2331	          "balanced_accuracy": 0.7243,
2332	          "accuracy": 0.7243,
2333	          "f1": 0.6964,
2334	          "peak_layer": 9
2335	        },
2336	        {
2337	          "balanced_accuracy": 0.7206,
2338	          "accuracy": 0.7206,
2339	          "f1": 0.745,
2340	          "peak_layer": 7
2341	        },
2342	        {
2343	          "balanced_accuracy": 0.7169,
2344	          "accuracy": 0.7169,
2345	          "f1": 0.7524,
2346	          "peak_layer": 16
2347	        },
2348	        {
2349	          "balanced_accuracy": 0.6728,
2350	          "accuracy": 0.6728,
2351	          "f1": 0.742,
2352	          "peak_layer": 15
2353	        },
2354	        {
2355	          "balanced_accuracy": 0.6949,
2356	          "accuracy": 0.6949,
2357	          "f1": 0.7186,
2358	          "peak_layer": 9
2359	        },
2360	        {
2361	          "balanced_accuracy": 0.7574,
2362	          "accuracy": 0.7574,
2363	          "f1": 0.7724,
2364	          "peak_layer": 15
2365	        },
2366	        {
2367	          "balanced_accuracy": 0.6875,
2368	          "accuracy": 0.6875,
2369	          "f1": 0.7478,
2370	          "peak_layer": 18
2371	        },
2372	        {
2373	          "balanced_accuracy": 0.7022,
2374	          "accuracy": 0.7022,
2375	          "f1": 0.7158,
2376	          "peak_layer": 15
2377	        },
2378	        {
2379	          "balanced_accuracy": 0.7096,
2380	          "accuracy": 0.7096,
2381	          "f1": 0.7375,
2382	          "peak_layer": 23
2383	        },
2384	        {
2385	          "balanced_accuracy": 0.6507,
2386	          "accuracy": 0.6507,
2387	          "f1": 0.713,
2388	          "peak_layer": 23
2389	        },
2390	        {
2391	          "balanced_accuracy": 0.7537,
2392	          "accuracy": 0.7537,
2393	          "f1": 0.7265,
2394	          "peak_layer": 17
2395	        },
2396	        {
2397	          "balanced_accuracy": 0.7096,
2398	          "accuracy": 0.7096,
2399	          "f1": 0.7539,
2400	          "peak_layer": 15
2401	        },
2402	        {
2403	          "balanced_accuracy": 0.7022,
2404	          "accuracy": 0.7022,
2405	          "f1": 0.7158,
2406	          "peak_layer": 9
2407	        },
2408	        {
2409	          "balanced_accuracy": 0.7059,
2410	          "accuracy": 0.7059,
2411	          "f1": 0.685,
2412	          "peak_layer": 12
2413	        },
2414	        {
2415	          "balanced_accuracy": 0.7132,
2416	          "accuracy": 0.7132,
2417	          "f1": 0.7562,
2418	          "peak_layer": 15
2419	        },
2420	        {
2421	          "balanced_accuracy": 0.7537,
2422	          "accuracy": 0.7537,
2423	          "f1": 0.7666,
2424	          "peak_layer": 15
2425	        },
2426	        {
2427	          "balanced_accuracy": 0.7426,
2428	          "accuracy": 0.7426,
2429	          "f1": 0.7328,
2430	          "peak_layer": 9
2431	        },
2432	        {
2433	          "balanced_accuracy": 0.739,
2434	          "accuracy": 0.739,
2435	          "f1": 0.7593,
2436	          "peak_layer": 15
2437	        },
2438	        {
2439	          "balanced_accuracy": 0.7059,
2440	          "accuracy": 0.7059,
2441	          "f1": 0.75,
2442	          "peak_layer": 15
2443	        },
2444	        {
2445	          "balanced_accuracy": 0.7426,
2446	          "accuracy": 0.7426,
2447	          "f1": 0.7388,
2448	          "peak_layer": 9
2449	        },
2450	        {
2451	          "balanced_accuracy": 0.7059,
2452	          "accuracy": 0.7059,
2453	          "f1": 0.7368,
2454	          "peak_layer": 15
2455	        },
2456	        {
2457	          "balanced_accuracy": 0.7353,
2458	          "accuracy": 0.7353,
2459	          "f1": 0.7447,
2460	          "peak_layer": 9
2461	        },
2462	        {
2463	          "balanced_accuracy": 0.6471,
2464	          "accuracy": 0.6471,
2465	          "f1": 0.619,
2466	          "peak_layer": 1
2467	        },
2468	        {
2469	          "balanced_accuracy": 0.739,
2470	          "accuracy": 0.739,
2471	          "f1": 0.7171,
2472	          "peak_layer": 16
2473	        },
2474	        {
2475	          "balanced_accuracy": 0.6985,
2476	          "accuracy": 0.6985,
2477	          "f1": 0.7453,
2478	          "peak_layer": 15
2479	        },
2480	        {
2481	          "balanced_accuracy": 0.7096,
2482	          "accuracy": 0.7096,
2483	          "f1": 0.7427,
2484	          "peak_layer": 17
2485	        },
2486	        {
2487	          "balanced_accuracy": 0.6985,
2488	          "accuracy": 0.6985,
2489	          "f1": 0.7421,
2490	          "peak_layer": 15
2491	        },
2492	        {
2493	          "balanced_accuracy": 0.6875,
2494	          "accuracy": 0.6875,
2495	          "f1": 0.7284,
2496	          "peak_layer": 21
2497	        },
2498	        {
2499	          "balanced_accuracy": 0.6949,
2500	          "accuracy": 0.6949,
2501	          "f1": 0.7446,
2502	          "peak_layer": 15
2503	        },
2504	        {
2505	          "balanced_accuracy": 0.7463,
2506	          "accuracy": 0.7463,
2507	          "f1": 0.7596,
2508	          "peak_layer": 16
2509	        },
2510	        {
2511	          "balanced_accuracy": 0.6654,
2512	          "accuracy": 0.6654,
2513	          "f1": 0.7093,
2514	          "peak_layer": 25
2515	        },
2516	        {
2517	          "balanced_accuracy": 0.7059,
2518	          "accuracy": 0.7059,
2519	          "f1": 0.7516,
2520	          "peak_layer": 15
2521	        },
2522	        {
2523	          "balanced_accuracy": 0.7279,
2524	          "accuracy": 0.7279,
2525	          "f1": 0.7413,
2526	          "peak_layer": 9
2527	        },
2528	        {
2529	          "balanced_accuracy": 0.7831,
2530	          "accuracy": 0.7831,
2531	          "f1": 0.779,
2532	          "peak_layer": 15
2533	        },
2534	        {
2535	          "balanced_accuracy": 0.7022,
2536	          "accuracy": 0.7022,
2537	          "f1": 0.7344,
2538	          "peak_layer": 18
2539	        },
2540	        {
2541	          "balanced_accuracy": 0.7279,
2542	          "accuracy": 0.7279,
2543	          "f1": 0.7357,
2544	          "peak_layer": 15
2545	        },
2546	        {
2547	          "balanced_accuracy": 0.739,
2548	          "accuracy": 0.739,
2549	          "f1": 0.7788,
2550	          "peak_layer": 15
2551	        },
2552	        {
2553	          "balanced_accuracy": 0.7426,
2554	          "accuracy": 0.7426,
2555	          "f1": 0.7482,
2556	          "peak_layer": 16
2557	        },
2558	        {
2559	          "balanced_accuracy": 0.7132,
2560	          "accuracy": 0.7132,
2561	          "f1": 0.7329,
2562	          "peak_layer": 17
2563	        },
2564	        {
2565	          "balanced_accuracy": 0.7059,
2566	          "accuracy": 0.7059,
2567	          "f1": 0.7531,
2568	          "peak_layer": 15
2569	        },
2570	        {
2571	          "balanced_accuracy": 0.7022,
2572	          "accuracy": 0.7022,
2573	          "f1": 0.7538,
2574	          "peak_layer": 9
2575	        },
2576	        {
2577	          "balanced_accuracy": 0.7022,
2578	          "accuracy": 0.7022,
2579	          "f1": 0.7273,
2580	          "peak_layer": 23
2581	        },
2582	        {
2583	          "balanced_accuracy": 0.739,
2584	          "accuracy": 0.739,
2585	          "f1": 0.738,
2586	          "peak_layer": 14
2587	        },
2588	        {
2589	          "balanced_accuracy": 0.6801,
2590	          "accuracy": 0.6801,
2591	          "f1": 0.7031,
2592	          "peak_layer": 25
2593	        },
2594	        {
2595	          "balanced_accuracy": 0.7243,
2596	          "accuracy": 0.7243,
2597	          "f1": 0.7292,
2598	          "peak_layer": 9
2599	        },
2600	        {
2601	          "balanced_accuracy": 0.7279,
2602	          "accuracy": 0.7279,
2603	          "f1": 0.7087,
2604	          "peak_layer": 16
2605	        },
2606	        {
2607	          "balanced_accuracy": 0.7316,
2608	          "accuracy": 0.7316,
2609	          "f1": 0.7224,
2610	          "peak_layer": 15
2611	        },
2612	        {
2613	          "balanced_accuracy": 0.7096,
2614	          "accuracy": 0.7096,
2615	          "f1": 0.658,
2616	          "peak_layer": 9
2617	        },
2618	        {
2619	          "balanced_accuracy": 0.7243,
2620	          "accuracy": 0.7243,
2621	          "f1": 0.7525,
2622	          "peak_layer": 15
2623	        },
2624	        {
2625	          "balanced_accuracy": 0.7353,
2626	          "accuracy": 0.7353,
2627	          "f1": 0.7483,
2628	          "peak_layer": 20
2629	        },
2630	        {
2631	          "balanced_accuracy": 0.7537,
2632	          "accuracy": 0.7537,
2633	          "f1": 0.7832,
2634	          "peak_layer": 15
2635	        },
2636	        {
2637	          "balanced_accuracy": 0.7169,
2638	          "accuracy": 0.7169,
2639	          "f1": 0.7116,
2640	          "peak_layer": 9
2641	        },
2642	        {
2643	          "balanced_accuracy": 0.7721,
2644	          "accuracy": 0.7721,
2645	          "f1": 0.7891,
2646	          "peak_layer": 16
2647	        },
2648	        {
2649	          "balanced_accuracy": 0.6985,
2650	          "accuracy": 0.6985,
2651	          "f1": 0.7485,
2652	          "peak_layer": 15
2653	        },
2654	        {
2655	          "balanced_accuracy": 0.6728,
2656	          "accuracy": 0.6728,
2657	          "f1": 0.6367,
2658	          "peak_layer": 0
2659	        },
2660	        {
2661	          "balanced_accuracy": 0.6618,
2662	          "accuracy": 0.6618,
2663	          "f1": 0.6828,
2664	          "peak_layer": 9
2665	        },
2666	        {
2667	          "balanced_accuracy": 0.7206,
2668	          "accuracy": 0.7206,
2669	          "f1": 0.7031,
2670	          "peak_layer": 11
2671	        },
2672	        {
2673	          "balanced_accuracy": 0.7463,
2674	          "accuracy": 0.7463,
2675	          "f1": 0.7612,
2676	          "peak_layer": 17
2677	        },
2678	        {
2679	          "balanced_accuracy": 0.6875,
2680	          "accuracy": 0.6875,
2681	          "f1": 0.6718,
2682	          "peak_layer": 20
2683	        },
2684	        {
2685	          "balanced_accuracy": 0.7353,
2686	          "accuracy": 0.7353,
2687	          "f1": 0.7252,
2688	          "peak_layer": 15
2689	        },
2690	        {
2691	          "balanced_accuracy": 0.6507,
2692	          "accuracy": 0.6507,
2693	          "f1": 0.5887,
2694	          "peak_layer": 7
2695	        },
2696	        {
2697	          "balanced_accuracy": 0.6801,
2698	          "accuracy": 0.6801,
2699	          "f1": 0.7307,
2700	          "peak_layer": 20
2701	        },
2702	        {
2703	          "balanced_accuracy": 0.6985,
2704	          "accuracy": 0.6985,
2705	          "f1": 0.7092,
2706	          "peak_layer": 13
2707	        },
2708	        {
2709	          "balanced_accuracy": 0.6875,
2710	          "accuracy": 0.6875,
2711	          "f1": 0.7099,
2712	          "peak_layer": 13
2713	        },
2714	        {
2715	          "balanced_accuracy": 0.7279,
2716	          "accuracy": 0.7279,
2717	          "f1": 0.7299,
2718	          "peak_layer": 9
2719	        },
2720	        {
2721	          "balanced_accuracy": 0.7426,
2722	          "accuracy": 0.7426,
2723	          "f1": 0.7482,
2724	          "peak_layer": 15
2725	        },
2726	        {
2727	          "balanced_accuracy": 0.7132,
2728	          "accuracy": 0.7132,
2729	          "f1": 0.7045,
2730	          "peak_layer": 15
2731	        },
2732	        {
2733	          "balanced_accuracy": 0.7279,
2734	          "accuracy": 0.7279,
2735	          "f1": 0.7643,
2736	          "peak_layer": 19
2737	        },
2738	        {
2739	          "balanced_accuracy": 0.7096,
2740	          "accuracy": 0.7096,
2741	          "f1": 0.6853,
2742	          "peak_layer": 11
2743	        },
2744	        {
2745	          "balanced_accuracy": 0.7132,
2746	          "accuracy": 0.7132,
2747	          "f1": 0.6953,
2748	          "peak_layer": 5
2749	        },
2750	        {
2751	          "balanced_accuracy": 0.6949,
2752	          "accuracy": 0.6949,
2753	          "f1": 0.7128,
2754	          "peak_layer": 9
2755	        },
2756	        {
2757	          "balanced_accuracy": 0.75,
2758	          "accuracy": 0.75,
2759	          "f1": 0.7622,
2760	          "peak_layer": 17
2761	        },
2762	        {
2763	          "balanced_accuracy": 0.6912,
2764	          "accuracy": 0.6912,
2765	          "f1": 0.7273,
2766	          "peak_layer": 14
2767	        },
2768	        {
2769	          "balanced_accuracy": 0.6654,
2770	          "accuracy": 0.6654,
2771	          "f1": 0.6224,
2772	          "peak_layer": 3
2773	        },
2774	        {
2775	          "balanced_accuracy": 0.7279,
2776	          "accuracy": 0.7279,
2777	          "f1": 0.7566,
2778	          "peak_layer": 17
2779	        },
2780	        {
2781	          "balanced_accuracy": 0.6912,
2782	          "accuracy": 0.6912,
2783	          "f1": 0.7407,
2784	          "peak_layer": 15
2785	        },
2786	        {
2787	          "balanced_accuracy": 0.7463,
2788	          "accuracy": 0.7463,
2789	          "f1": 0.7661,
2790	          "peak_layer": 15
2791	        },
2792	        {
2793	          "balanced_accuracy": 0.7132,
2794	          "accuracy": 0.7132,
2795	          "f1": 0.7292,
2796	          "peak_layer": 21
2797	        },
2798	        {
2799	          "balanced_accuracy": 0.7022,
2800	          "accuracy": 0.7022,
2801	          "f1": 0.7011,
2802	          "peak_layer": 9
2803	        },
2804	        {
2805	          "balanced_accuracy": 0.6912,
2806	          "accuracy": 0.6912,
2807	          "f1": 0.6471,
2808	          "peak_layer": 9
2809	        },
2810	        {
2811	          "balanced_accuracy": 0.7022,
2812	          "accuracy": 0.7022,
2813	          "f1": 0.7273,
2814	          "peak_layer": 24
2815	        },
2816	        {
2817	          "balanced_accuracy": 0.7316,
2818	          "accuracy": 0.7316,
2819	          "f1": 0.7542,
2820	          "peak_layer": 17
2821	        },
2822	        {
2823	          "balanced_accuracy": 0.7243,
2824	          "accuracy": 0.7243,
2825	          "f1": 0.7678,
2826	          "peak_layer": 15
2827	        },
2828	        {
2829	          "balanced_accuracy": 0.7279,
2830	          "accuracy": 0.7279,
2831	          "f1": 0.7132,
2832	          "peak_layer": 15
2833	        },
2834	        {
2835	          "balanced_accuracy": 0.6912,
2836	          "accuracy": 0.6912,
2837	          "f1": 0.7181,
2838	          "peak_layer": 5
2839	        },
2840	        {
2841	          "balanced_accuracy": 0.6949,
2842	          "accuracy": 0.6949,
2843	          "f1": 0.7046,
2844	          "peak_layer": 12
2845	        },
2846	        {
2847	          "balanced_accuracy": 0.7316,
2848	          "accuracy": 0.7316,
2849	          "f1": 0.7712,
2850	          "peak_layer": 19
2851	        }
2852	      ]
2853	    }
2854	  }
2855	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25db9050-f268-421a-b4de-3af00cd874e1",
  "isSidechain": true,
  "promptId": "7b01965c-4d4b-490d-8578-864ad14179c8",
  "agentId": "a9576db012ac53ecf",
  "type": "user",
  "uuid": "0fee80ec-fc97-4fdf-a634-d07484e0a319",
  "sourceToolAssistantUUID": "25db9050-f268-421a-b4de-3af00cd874e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-22T16:27:01.405Z_

<details><summary>↩ Tool result · `toolu_01D4NwWhnAJyCUgW3LRLEvC9`</summary>

```text
1	{
2	  "mode": "bootstrap",
3	  "n_bootstrap": 100,
4	  "num_layers": 36,
5	  "directions": {
6	    "EN→EN": {
7	      "direction": "EN→EN",
8	      "n_bootstrap": 100,
9	      "balanced_accuracy_mean": 0.7528,
10	      "balanced_accuracy_std": 0.0168,
11	      "f1_mean": 0.7499,
12	      "f1_std": 0.0183,
13	      "peak_layers": [
14	        20,
15	        18,
16	        20,
17	        16,
18	        21,
19	        11,
20	        21,
21	        18,
22	        5,
23	        17,
24	        18,
25	        24,
26	        14,
27	        19,
28	        22,
29	        19,
30	        18,
31	        13,
32	        22,
33	        10,
34	        17,
35	        22,
36	        17,
37	        18,
38	        15,
39	        23,
40	        17,
41	        22,
42	        12,
43	        19,
44	        19,
45	        16,
46	        18,
47	        14,
48	        19,
49	        15,
50	        23,
51	        7,
52	        23,
53	        12,
54	        16,
55	        18,
56	        16,
57	        24,
58	        24,
59	        15,
60	        22,
61	        19,
62	        18,
63	        28,
64	        12,
65	        15,
66	        23,
67	        15,
68	        13,
69	        12,
70	        18,
71	        7,
72	        19,
73	        22,
74	        21,
75	        23,
76	        22,
77	        18,
78	        22,
79	        15,
80	        16,
81	        23,
82	        18,
83	        18,
84	        19,
85	        18,
86	        23,
87	        19,
88	        15,
89	        15,
90	        18,
91	        23,
92	        15,
93	        18,
94	        16,
95	        15,
96	        18,
97	        23,
98	        23,
99	        18,
100	        16,
101	        18,
102	        8,
103	        20,
104	        17,
105	        16,
106	        26,
107	        15,
108	        20,
109	        15,
110	        35,
111	        18,
112	        12,
113	        24
114	      ],
115	      "per_bootstrap": [
116	        {
117	          "balanced_accuracy": 0.744,
118	          "accuracy": 0.744,
119	          "f1": 0.744,
120	          "peak_layer": 20
121	        },
122	        {
123	          "balanced_accuracy": 0.7917,
124	          "accuracy": 0.7917,
125	          "f1": 0.7917,
126	          "peak_layer": 18
127	        },
128	        {
129	          "balanced_accuracy": 0.7381,
130	          "accuracy": 0.7381,
131	          "f1": 0.7381,
132	          "peak_layer": 20
133	        },
134	        {
135	          "balanced_accuracy": 0.7381,
136	          "accuracy": 0.7381,
137	          "f1": 0.7381,
138	          "peak_layer": 16
139	        },
140	        {
141	          "balanced_accuracy": 0.7738,
142	          "accuracy": 0.7738,
143	          "f1": 0.7738,
144	          "peak_layer": 21
145	        },
146	        {
147	          "balanced_accuracy": 0.756,
148	          "accuracy": 0.756,
149	          "f1": 0.756,
150	          "peak_layer": 11
151	        },
152	        {
153	          "balanced_accuracy": 0.7679,
154	          "accuracy": 0.7679,
155	          "f1": 0.7679,
156	          "peak_layer": 21
157	        },
158	        {
159	          "balanced_accuracy": 0.7738,
160	          "accuracy": 0.7738,
161	          "f1": 0.7738,
162	          "peak_layer": 18
163	        },
164	        {
165	          "balanced_accuracy": 0.7202,
166	          "accuracy": 0.7202,
167	          "f1": 0.7202,
168	          "peak_layer": 5
169	        },
170	        {
171	          "balanced_accuracy": 0.756,
172	          "accuracy": 0.756,
173	          "f1": 0.756,
174	          "peak_layer": 17
175	        },
176	        {
177	          "balanced_accuracy": 0.7202,
178	          "accuracy": 0.7202,
179	          "f1": 0.7202,
180	          "peak_layer": 18
181	        },
182	        {
183	          "balanced_accuracy": 0.7381,
184	          "accuracy": 0.7381,
185	          "f1": 0.7381,
186	          "peak_layer": 24
187	        },
188	        {
189	          "balanced_accuracy": 0.75,
190	          "accuracy": 0.75,
191	          "f1": 0.75,
192	          "peak_layer": 14
193	        },
194	        {
195	          "balanced_accuracy": 0.7679,
196	          "accuracy": 0.7679,
197	          "f1": 0.7679,
198	          "peak_layer": 19
199	        },
200	        {
201	          "balanced_accuracy": 0.7857,
202	          "accuracy": 0.7857,
203	          "f1": 0.7857,
204	          "peak_layer": 22
205	        },
206	        {
207	          "balanced_accuracy": 0.756,
208	          "accuracy": 0.756,
209	          "f1": 0.756,
210	          "peak_layer": 19
211	        },
212	        {
213	          "balanced_accuracy": 0.7381,
214	          "accuracy": 0.7381,
215	          "f1": 0.7381,
216	          "peak_layer": 18
217	        },
218	        {
219	          "balanced_accuracy": 0.7619,
220	          "accuracy": 0.7619,
221	          "f1": 0.7619,
222	          "peak_layer": 13
223	        },
224	        {
225	          "balanced_accuracy": 0.756,
226	          "accuracy": 0.756,
227	          "f1": 0.756,
228	          "peak_layer": 22
229	        },
230	        {
231	          "balanced_accuracy": 0.75,
232	          "accuracy": 0.75,
233	          "f1": 0.75,
234	          "peak_layer": 10
235	        },
236	        {
237	          "balanced_accuracy": 0.7321,
238	          "accuracy": 0.7321,
239	          "f1": 0.7321,
240	          "peak_layer": 17
241	        },
242	        {
243	          "balanced_accuracy": 0.75,
244	          "accuracy": 0.75,
245	          "f1": 0.75,
246	          "peak_layer": 22
247	        },
248	        {
249	          "balanced_accuracy": 0.7738,
250	          "accuracy": 0.7738,
251	          "f1": 0.7738,
252	          "peak_layer": 17
253	        },
254	        {
255	          "balanced_accuracy": 0.75,
256	          "accuracy": 0.75,
257	          "f1": 0.75,
258	          "peak_layer": 18
259	        },
260	        {
261	          "balanced_accuracy": 0.7262,
262	          "accuracy": 0.7262,
263	          "f1": 0.7262,
264	          "peak_layer": 15
265	        },
266	        {
267	          "balanced_accuracy": 0.744,
268	          "accuracy": 0.744,
269	          "f1": 0.744,
270	          "peak_layer": 23
271	        },
272	        {
273	          "balanced_accuracy": 0.7738,
274	          "accuracy": 0.7738,
275	          "f1": 0.7738,
276	          "peak_layer": 17
277	        },
278	        {
279	          "balanced_accuracy": 0.75,
280	          "accuracy": 0.75,
281	          "f1": 0.75,
282	          "peak_layer": 22
283	        },
284	        {
285	          "balanced_accuracy": 0.75,
286	          "accuracy": 0.75,
287	          "f1": 0.75,
288	          "peak_layer": 12
289	        },
290	        {
291	          "balanced_accuracy": 0.7679,
292	          "accuracy": 0.7679,
293	          "f1": 0.7679,
294	          "peak_layer": 19
295	        },
296	        {
297	          "balanced_accuracy": 0.756,
298	          "accuracy": 0.756,
299	          "f1": 0.756,
300	          "peak_layer": 19
301	        },
302	        {
303	          "balanced_accuracy": 0.75,
304	          "accuracy": 0.75,
305	          "f1": 0.75,
306	          "peak_layer": 16
307	        },
308	        {
309	          "balanced_accuracy": 0.744,
310	          "accuracy": 0.744,
311	          "f1": 0.744,
312	          "peak_layer": 18
313	        },
314	        {
315	          "balanced_accuracy": 0.744,
316	          "accuracy": 0.744,
317	          "f1": 0.744,
318	          "peak_layer": 14
319	        },
320	        {
321	          "balanced_accuracy": 0.7857,
322	          "accuracy": 0.7857,
323	          "f1": 0.7857,
324	          "peak_layer": 19
325	        },
326	        {
327	          "balanced_accuracy": 0.7679,
328	          "accuracy": 0.7679,
329	          "f1": 0.7679,
330	          "peak_layer": 15
331	        },
332	        {
333	          "balanced_accuracy": 0.7381,
334	          "accuracy": 0.7381,
335	          "f1": 0.7381,
336	          "peak_layer": 23
337	        },
338	        {
339	          "balanced_accuracy": 0.7798,
340	          "accuracy": 0.7798,
341	          "f1": 0.7798,
342	          "peak_layer": 7
343	        },
344	        {
345	          "balanced_accuracy": 0.7381,
346	          "accuracy": 0.7381,
347	          "f1": 0.7381,
348	          "peak_layer": 23
349	        },
350	        {
351	          "balanced_accuracy": 0.7679,
352	          "accuracy": 0.7679,
353	          "f1": 0.7679,
354	          "peak_layer": 12
355	        },
356	        {
357	          "balanced_accuracy": 0.756,
358	          "accuracy": 0.756,
359	          "f1": 0.756,
360	          "peak_layer": 16
361	        },
362	        {
363	          "balanced_accuracy": 0.744,
364	          "accuracy": 0.744,
365	          "f1": 0.744,
366	          "peak_layer": 18
367	        },
368	        {
369	          "balanced_accuracy": 0.7381,
370	          "accuracy": 0.7381,
371	          "f1": 0.7381,
372	          "peak_layer": 16
373	        },
374	        {
375	          "balanced_accuracy": 0.7679,
376	          "accuracy": 0.7679,
377	          "f1": 0.7679,
378	          "peak_layer": 24
379	        },
380	        {
381	          "balanced_accuracy": 0.7381,
382	          "accuracy": 0.7381,
383	          "f1": 0.7381,
384	          "peak_layer": 24
385	        },
386	        {
387	          "balanced_accuracy": 0.75,
388	          "accuracy": 0.75,
389	          "f1": 0.75,
390	          "peak_layer": 15
391	        },
392	        {
393	          "balanced_accuracy": 0.7619,
394	          "accuracy": 0.7619,
395	          "f1": 0.7619,
396	          "peak_layer": 22
397	        },
398	        {
399	          "balanced_accuracy": 0.7976,
400	          "accuracy": 0.7976,
401	          "f1": 0.7976,
402	          "peak_layer": 19
403	        },
404	        {
405	          "balanced_accuracy": 0.744,
406	          "accuracy": 0.744,
407	          "f1": 0.744,
408	          "peak_layer": 18
409	        },
410	        {
411	          "balanced_accuracy": 0.7321,
412	          "accuracy": 0.7321,
413	          "f1": 0.7321,
414	          "peak_layer": 28
415	        },
416	        {
417	          "balanced_accuracy": 0.7202,
418	          "accuracy": 0.7202,
419	          "f1": 0.7202,
420	          "peak_layer": 12
421	        },
422	        {
423	          "balanced_accuracy": 0.7619,
424	          "accuracy": 0.7619,
425	          "f1": 0.7619,
426	          "peak_layer": 15
427	        },
428	        {
429	          "balanced_accuracy": 0.756,
430	          "accuracy": 0.756,
431	          "f1": 0.756,
432	          "peak_layer": 23
433	        },
434	        {
435	          "balanced_accuracy": 0.7262,
436	          "accuracy": 0.7262,
437	          "f1": 0.7262,
438	          "peak_layer": 15
439	        },
440	        {
441	          "balanced_accuracy": 0.7381,
442	          "accuracy": 0.7381,
443	          "f1": 0.7381,
444	          "peak_layer": 13
445	        },
446	        {
447	          "balanced_accuracy": 0.75,
448	          "accuracy": 0.75,
449	          "f1": 0.75,
450	          "peak_layer": 12
451	        },
452	        {
453	          "balanced_accuracy": 0.744,
454	          "accuracy": 0.744,
455	          "f1": 0.744,
456	          "peak_layer": 18
457	        },
458	        {
459	          "balanced_accuracy": 0.744,
460	          "accuracy": 0.744,
461	          "f1": 0.744,
462	          "peak_layer": 7
463	        },
464	        {
465	          "balanced_accuracy": 0.7738,
466	          "accuracy": 0.7738,
467	          "f1": 0.7738,
468	          "peak_layer": 19
469	        },
470	        {
471	          "balanced_accuracy": 0.7619,
472	          "accuracy": 0.7619,
473	          "f1": 0.7619,
474	          "peak_layer": 22
475	        },
476	        {
477	          "balanced_accuracy": 0.7381,
478	          "accuracy": 0.7381,
479	          "f1": 0.7381,
480	          "peak_layer": 21
481	        },
482	        {
483	          "balanced_accuracy": 0.75,
484	          "accuracy": 0.75,
485	          "f1": 0.75,
486	          "peak_layer": 23
487	        },
488	        {
489	          "balanced_accuracy": 0.7381,
490	          "accuracy": 0.7381,
491	          "f1": 0.7381,
492	          "peak_layer": 22
493	        },
494	        {
495	          "balanced_accuracy": 0.7619,
496	          "accuracy": 0.7619,
497	          "f1": 0.7619,
498	          "peak_layer": 18
499	        },
500	        {
501	          "balanced_accuracy": 0.744,
502	          "accuracy": 0.744,
503	          "f1": 0.744,
504	          "peak_layer": 22
505	        },
506	        {
507	          "balanced_accuracy": 0.756,
508	          "accuracy": 0.756,
509	          "f1": 0.756,
510	          "peak_layer": 15
511	        },
512	        {
513	          "balanced_accuracy": 0.75,
514	          "accuracy": 0.75,
515	          "f1": 0.75,
516	          "peak_layer": 16
517	        },
518	        {
519	          "balanced_accuracy": 0.7679,
520	          "accuracy": 0.7679,
521	          "f1": 0.7679,
522	          "peak_layer": 23
523	        },
524	        {
525	          "balanced_accuracy": 0.7738,
526	          "accuracy": 0.7738,
527	          "f1": 0.7738,
528	          "peak_layer": 18
529	        },
530	        {
531	          "balanced_accuracy": 0.7679,
532	          "accuracy": 0.7679,
533	          "f1": 0.7679,
534	          "peak_layer": 18
535	        },
536	        {
537	          "balanced_accuracy": 0.7679,
538	          "accuracy": 0.7679,
539	          "f1": 0.7679,
540	          "peak_layer": 19
541	        },
542	        {
543	          "balanced_accuracy": 0.75,
544	          "accuracy": 0.75,
545	          "f1": 0.75,
546	          "peak_layer": 18
547	        },
548	        {
549	          "balanced_accuracy": 0.7619,
550	          "accuracy": 0.7619,
551	          "f1": 0.7619,
552	          "peak_layer": 23
553	        },
554	        {
555	          "balanced_accuracy": 0.7619,
556	          "accuracy": 0.7619,
557	          "f1": 0.7619,
558	          "peak_layer": 19
559	        },
560	        {
561	          "balanced_accuracy": 0.7321,
562	          "accuracy": 0.7321,
563	          "f1": 0.7321,
564	          "peak_layer": 15
565	        },
566	        {
567	          "balanced_accuracy": 0.744,
568	          "accuracy": 0.744,
569	          "f1": 0.744,
570	          "peak_layer": 15
571	        },
572	        {
573	          "balanced_accuracy": 0.7321,
574	          "accuracy": 0.7321,
575	          "f1": 0.7321,
576	          "peak_layer": 18
577	        },
578	        {
579	          "balanced_accuracy": 0.756,
580	          "accuracy": 0.756,
581	          "f1": 0.756,
582	          "peak_layer": 23
583	        },
584	        {
585	          "balanced_accuracy": 0.7381,
586	          "accuracy": 0.7381,
587	          "f1": 0.7381,
588	          "peak_layer": 15
589	        },
590	        {
591	          "balanced_accuracy": 0.756,
592	          "accuracy": 0.756,
593	          "f1": 0.756,
594	          "peak_layer": 18
595	        },
596	        {
597	          "balanced_accuracy": 0.7321,
598	          "accuracy": 0.7321,
599	          "f1": 0.7321,
600	          "peak_layer": 16
601	        },
602	        {
603	          "balanced_accuracy": 0.7798,
604	          "accuracy": 0.7798,
605	          "f1": 0.7798,
606	          "peak_layer": 15
607	        },
608	        {
609	          "balanced_accuracy": 0.7619,
610	          "accuracy": 0.7619,
611	          "f1": 0.7619,
612	          "peak_layer": 18
613	        },
614	        {
615	          "balanced_accuracy": 0.7321,
616	          "accuracy": 0.7321,
617	          "f1": 0.7321,
618	          "peak_layer": 23
619	        },
620	        {
621	          "balanced_accuracy": 0.756,
622	          "accuracy": 0.756,
623	          "f1": 0.756,
624	          "peak_layer": 23
625	        },
626	        {
627	          "balanced_accuracy": 0.7619,
628	          "accuracy": 0.7619,
629	          "f1": 0.7619,
630	          "peak_layer": 18
631	        },
632	        {
633	          "balanced_accuracy": 0.7738,
634	          "accuracy": 0.7738,
635	          "f1": 0.7738,
636	          "peak_layer": 16
637	        },
638	        {
639	          "balanced_accuracy": 0.7738,
640	          "accuracy": 0.7738,
641	          "f1": 0.7738,
642	          "peak_layer": 18
643	        },
644	        {
645	          "balanced_accuracy": 0.7619,
646	          "accuracy": 0.7619,
647	          "f1": 0.7619,
648	          "peak_layer": 8
649	        },
650	        {
651	          "balanced_accuracy": 0.7321,
652	          "accuracy": 0.7321,
653	          "f1": 0.7321,
654	          "peak_layer": 20
655	        },
656	        {
657	          "balanced_accuracy": 0.744,
658	          "accuracy": 0.744,
659	          "f1": 0.744,
660	          "peak_layer": 17
661	        },
662	        {
663	          "balanced_accuracy": 0.75,
664	          "accuracy": 0.75,
665	          "f1": 0.75,
666	          "peak_layer": 16
667	        },
668	        {
669	          "balanced_accuracy": 0.7679,
670	          "accuracy": 0.7679,
671	          "f1": 0.7679,
672	          "peak_layer": 26
673	        },
674	        {
675	          "balanced_accuracy": 0.7679,
676	          "accuracy": 0.7679,
677	          "f1": 0.7679,
678	          "peak_layer": 15
679	        },
680	        {
681	          "balanced_accuracy": 0.7381,
682	          "accuracy": 0.7381,
683	          "f1": 0.7381,
684	          "peak_layer": 20
685	        },
686	        {
687	          "balanced_accuracy": 0.7202,
688	          "accuracy": 0.7202,
689	          "f1": 0.7202,
690	          "peak_layer": 15
691	        },
692	        {
693	          "balanced_accuracy": 0.7321,
694	          "accuracy": 0.7321,
695	          "f1": 0.7321,
696	          "peak_layer": 35
697	        },
698	        {
699	          "balanced_accuracy": 0.7857,
700	          "accuracy": 0.7857,
701	          "f1": 0.7857,
702	          "peak_layer": 18
703	        },
704	        {
705	          "balanced_accuracy": 0.7381,
706	          "accuracy": 0.7381,
707	          "f1": 0.7381,
708	          "peak_layer": 12
709	        },
710	        {
711	          "balanced_accuracy": 0.744,
712	          "accuracy": 0.744,
713	          "f1": 0.744,
714	          "peak_layer": 24
715	        }
716	      ]
717	    },
718	    "ZH→ZH": {
719	      "direction": "ZH→ZH",
720	      "n_bootstrap": 100,
721	      "balanced_accuracy_mean": 0.7162,
722	      "balanced_accuracy_std": 0.0179,
723	      "f1_mean": 0.7216,
724	      "f1_std": 0.0215,
725	      "peak_layers": [
726	        17,
727	        21,
728	        13,
729	        21,
730	        14,
731	        22,
732	        16,
733	        23,
734	        6,
735	        21,
736	        21,
737	        19,
738	        21,
739	        23,
740	        23,
741	        21,
742	        20,
743	        15,
744	        13,
745	        19,
746	        16,
747	        21,
748	        14,
749	        21,
750	        17,
751	        23,
752	        20,
753	        21,
754	        17,
755	        14,
756	        21,
757	        14,
758	        27,
759	        19,
760	        18,
761	        6,
762	        14,
763	        18,
764	        21,
765	        23,
766	        13,
767	        21,
768	        23,
769	        17,
770	        17,
771	        21,
772	        18,
773	        23,
774	        21,
775	        23,
776	        35,
777	        21,
778	        21,
779	        21,
780	        6,
781	        17,
782	        30,
783	        19,
784	        23,
785	        7,
786	        6,
787	        23,
788	        21,
789	        17,
790	        23,
791	        21,
792	        14,
793	        23,
794	        22,
795	        14,
796	        16,
797	        21,
798	        23,
799	        18,
800	        35,
801	        21,
802	        7,
803	        34,
804	        6,
805	        21,
806	        22,
807	        6,
808	        23,
809	        27,
810	        23,
811	        21,
812	        17,
813	        23,
814	        4,
815	        21,
816	        17,
817	        6,
818	        28,
819	        14,
820	        7,
821	        21,
822	        16,
823	        14,
824	        14,
825	        23
826	      ],
827	      "per_bootstrap": [
828	        {
829	          "balanced_accuracy": 0.7143,
830	          "accuracy": 0.7143,
831	          "f1": 0.7143,
832	          "peak_layer": 17
833	        },
834	        {
835	          "balanced_accuracy": 0.7143,
836	          "accuracy": 0.7143,
837	          "f1": 0.7143,
838	          "peak_layer": 21
839	        },
840	        {
841	          "balanced_accuracy": 0.7262,
842	          "accuracy": 0.7262,
843	          "f1": 0.7262,
844	          "peak_layer": 13
845	        },
846	        {
847	          "balanced_accuracy": 0.7143,
848	          "accuracy": 0.7143,
849	          "f1": 0.7143,
850	          "peak_layer": 21
851	        },
852	        {
853	          "balanced_accuracy": 0.7024,
854	          "accuracy": 0.7024,
855	          "f1": 0.7024,
856	          "peak_layer": 14
857	        },
858	        {
859	          "balanced_accuracy": 0.7321,
860	          "accuracy": 0.7321,
861	          "f1": 0.7321,
862	          "peak_layer": 22
863	        },
864	        {
865	          "balanced_accuracy": 0.744,
866	          "accuracy": 0.744,
867	          "f1": 0.744,
868	          "peak_layer": 16
869	        },
870	        {
871	          "balanced_accuracy": 0.7024,
872	          "accuracy": 0.7024,
873	          "f1": 0.7024,
874	          "peak_layer": 23
875	        },
876	        {
877	          "balanced_accuracy": 0.6905,
878	          "accuracy": 0.6905,
879	          "f1": 0.6905,
880	          "peak_layer": 6
881	        },
882	        {
883	          "balanced_accuracy": 0.7738,
884	          "accuracy": 0.7738,
885	          "f1": 0.7738,
886	          "peak_layer": 21
887	        },
888	        {
889	          "balanced_accuracy": 0.7024,
890	          "accuracy": 0.7024,
891	          "f1": 0.7024,
892	          "peak_layer": 21
893	        },
894	        {
895	          "balanced_accuracy": 0.6964,
896	          "accuracy": 0.6964,
897	          "f1": 0.6964,
898	          "peak_layer": 19
899	        },
900	        {
901	          "balanced_accuracy": 0.7083,
902	          "accuracy": 0.7083,
903	          "f1": 0.7083,
904	          "peak_layer": 21
905	        },
906	        {
907	          "balanced_accuracy": 0.7202,
908	          "accuracy": 0.7202,
909	          "f1": 0.7202,
910	          "peak_layer": 23
911	        },
912	        {
913	          "balanced_accuracy": 0.756,
914	          "accuracy": 0.756,
915	          "f1": 0.756,
916	          "peak_layer": 23
917	        },
918	        {
919	          "balanced_accuracy": 0.7202,
920	          "accuracy": 0.7202,
921	          "f1": 0.7202,
922	          "peak_layer": 21
923	        },
924	        {
925	          "balanced_accuracy": 0.7024,
926	          "accuracy": 0.7024,
927	          "f1": 0.7024,
928	          "peak_layer": 20
929	        },
930	        {
931	          "balanced_accuracy": 0.7202,
932	          "accuracy": 0.7202,
933	          "f1": 0.7202,
934	          "peak_layer": 15
935	        },
936	        {
937	          "balanced_accuracy": 0.6845,
938	          "accuracy": 0.6845,
939	          "f1": 0.6845,
940	          "peak_layer": 13
941	        },
942	        {
943	          "balanced_accuracy": 0.7143,
944	          "accuracy": 0.7143,
945	          "f1": 0.7143,
946	          "peak_layer": 19
947	        },
948	        {
949	          "balanced_accuracy": 0.6905,
950	          "accuracy": 0.6905,
951	          "f1": 0.6905,
952	          "peak_layer": 16
953	        },
954	        {
955	          "balanced_accuracy": 0.6964,
956	          "accuracy": 0.6964,
957	          "f1": 0.6964,
958	          "peak_layer": 21
959	        },
960	        {
961	          "balanced_accuracy": 0.6845,
962	          "accuracy": 0.6845,
963	          "f1": 0.6845,
964	          "peak_layer": 14
965	        },
966	        {
967	          "balanced_accuracy": 0.7083,
968	          "accuracy": 0.7083,
969	          "f1": 0.7083,
970	          "peak_layer": 21
971	        },
972	        {
973	          "balanced_accuracy": 0.7202,
974	          "accuracy": 0.7202,
975	          "f1": 0.7202,
976	          "peak_layer": 17
977	        },
978	        {
979	          "balanced_accuracy": 0.7202,
980	          "accuracy": 0.7202,
981	          "f1": 0.7202,
982	          "peak_layer": 23
983	        },
984	        {
985	          "balanced_accuracy": 0.7262,
986	          "accuracy": 0.7262,
987	          "f1": 0.7262,
988	          "peak_layer": 20
989	        },
990	        {
991	          "balanced_accuracy": 0.7381,
992	          "accuracy": 0.7381,
993	          "f1": 0.7381,
994	          "peak_layer": 21
995	        },
996	        {
997	          "balanced_accuracy": 0.7202,
998	          "accuracy": 0.7202,
999	          "f1": 0.7202,
1000	          "peak_layer": 17
1001	        },
1002	        {
1003	          "balanced_accuracy": 0.7262,
1004	          "accuracy": 0.7262,
1005	          "f1": 0.7262,
1006	          "peak_layer": 14
1007	        },
1008	        {
1009	          "balanced_accuracy": 0.7262,
1010	          "accuracy": 0.7262,
1011	          "f1": 0.7262,
1012	          "peak_layer": 21
1013	        },
1014	        {
1015	          "balanced_accuracy": 0.7619,
1016	          "accuracy": 0.7619,
1017	          "f1": 0.7619,
1018	          "peak_layer": 14
1019	        },
1020	        {
1021	          "balanced_accuracy": 0.6964,
1022	          "accuracy": 0.6964,
1023	          "f1": 0.6964,
1024	          "peak_layer": 27
1025	        },
1026	        {
1027	          "balanced_accuracy": 0.7262,
1028	          "accuracy": 0.7262,
1029	          "f1": 0.7262,
1030	          "peak_layer": 19
1031	        },
1032	        {
1033	          "balanced_accuracy": 0.6905,
1034	          "accuracy": 0.6905,
1035	          "f1": 0.6905,
1036	          "peak_layer": 18
1037	        },
1038	        {
1039	          "balanced_accuracy": 0.7143,
1040	          "accuracy": 0.7143,
1041	          "f1": 0.7143,
1042	          "peak_layer": 6
1043	        },
1044	        {
1045	          "balanced_accuracy": 0.7083,
1046	          "accuracy": 0.7083,
1047	          "f1": 0.7083,
1048	          "peak_layer": 14
1049	        },
1050	        {
1051	          "balanced_accuracy": 0.7024,
1052	          "accuracy": 0.7024,
1053	          "f1": 0.7024,
1054	          "peak_layer": 18
1055	        },
1056	        {
1057	          "balanced_accuracy": 0.7262,
1058	          "accuracy": 0.7262,
1059	          "f1": 0.7262,
1060	          "peak_layer": 21
1061	        },
1062	        {
1063	          "balanced_accuracy": 0.7262,
1064	          "accuracy": 0.7262,
1065	          "f1": 0.7262,
1066	          "peak_layer": 23
1067	        },
1068	        {
1069	          "balanced_accuracy": 0.7143,
1070	          "accuracy": 0.7143,
1071	          "f1": 0.7143,
1072	          "peak_layer": 13
1073	        },
1074	        {
1075	          "balanced_accuracy": 0.7262,
1076	          "accuracy": 0.7262,
1077	          "f1": 0.7262,
1078	          "peak_layer": 21
1079	        },
1080	        {
1081	          "balanced_accuracy": 0.7143,
1082	          "accuracy": 0.7143,
1083	          "f1": 0.7143,
1084	          "peak_layer": 23
1085	        },
1086	        {
1087	          "balanced_accuracy": 0.6964,
1088	          "accuracy": 0.6964,
1089	          "f1": 0.6964,
1090	          "peak_layer": 17
1091	        },
1092	        {
1093	          "balanced_accuracy": 0.7024,
1094	          "accuracy": 0.7024,
1095	          "f1": 0.7024,
1096	          "peak_layer": 17
1097	        },
1098	        {
1099	          "balanced_accuracy": 0.7202,
1100	          "accuracy": 0.7202,
1101	          "f1": 0.7202,
1102	          "peak_layer": 21
1103	        },
1104	        {
1105	          "balanced_accuracy": 0.7321,
1106	          "accuracy": 0.7321,
1107	          "f1": 0.7321,
1108	          "peak_layer": 18
1109	        },
1110	        {
1111	          "balanced_accuracy": 0.7202,
1112	          "accuracy": 0.7202,
1113	          "f1": 0.7202,
1114	          "peak_layer": 23
1115	        },
1116	        {
1117	          "balanced_accuracy": 0.6845,
1118	          "accuracy": 0.6845,
1119	          "f1": 0.6845,
1120	          "peak_layer": 21
1121	        },
1122	        {
1123	          "balanced_accuracy": 0.7143,
1124	          "accuracy": 0.7143,
1125	          "f1": 0.7143,
1126	          "peak_layer": 23
1127	        },
1128	        {
1129	          "balanced_accuracy": 0.6905,
1130	          "accuracy": 0.6905,
1131	          "f1": 0.6905,
1132	          "peak_layer": 35
1133	        },
1134	        {
1135	          "balanced_accuracy": 0.7321,
1136	          "accuracy": 0.7321,
1137	          "f1": 0.7321,
1138	          "peak_layer": 21
1139	        },
1140	        {
1141	          "balanced_accuracy": 0.7202,
1142	          "accuracy": 0.7202,
1143	          "f1": 0.7202,
1144	          "peak_layer": 21
1145	        },
1146	        {
1147	          "balanced_accuracy": 0.7143,
1148	          "accuracy": 0.7143,
1149	          "f1": 0.7143,
1150	          "peak_layer": 21
1151	        },
1152	        {
1153	          "balanced_accuracy": 0.6845,
1154	          "accuracy": 0.6845,
1155	          "f1": 0.6845,
1156	          "peak_layer": 6
1157	        },
1158	        {
1159	          "balanced_accuracy": 0.7321,
1160	          "accuracy": 0.7321,
1161	          "f1": 0.7321,
1162	          "peak_layer": 17
1163	        },
1164	        {
1165	          "balanced_accuracy": 0.6845,
1166	          "accuracy": 0.6845,
1167	          "f1": 0.6845,
1168	          "peak_layer": 30
1169	        },
1170	        {
1171	          "balanced_accuracy": 0.7143,
1172	          "accuracy": 0.7143,
1173	          "f1": 0.7143,
1174	          "peak_layer": 19
1175	        },
1176	        {
1177	          "balanced_accuracy": 0.7262,
1178	          "accuracy": 0.7262,
1179	          "f1": 0.7262,
1180	          "peak_layer": 23
1181	        },
1182	        {
1183	          "balanced_accuracy": 0.7202,
1184	          "accuracy": 0.7202,
1185	          "f1": 0.7202,
1186	          "peak_layer": 7
1187	        },
1188	        {
1189	          "balanced_accuracy": 0.7024,
1190	          "accuracy": 0.7024,
1191	          "f1": 0.7024,
1192	          "peak_layer": 6
1193	        },
1194	        {
1195	          "balanced_accuracy": 0.7381,
1196	          "accuracy": 0.7381,
1197	          "f1": 0.7381,
1198	          "peak_layer": 23
1199	        },
1200	        {
1201	          "balanced_accuracy": 0.7262,
1202	          "accuracy": 0.7262,
1203	          "f1": 0.7262,
1204	          "peak_layer": 21
1205	        },
1206	        {
1207	          "balanced_accuracy": 0.7083,
1208	          "accuracy": 0.7083,
1209	          "f1": 0.7083,
1210	          "peak_layer": 17
1211	        },
1212	        {
1213	          "balanced_accuracy": 0.7321,
1214	          "accuracy": 0.7321,
1215	          "f1": 0.7321,
1216	          "peak_layer": 23
1217	        },
1218	        {
1219	          "balanced_accuracy": 0.744,
1220	          "accuracy": 0.744,
1221	          "f1": 0.744,
1222	          "peak_layer": 21
1223	        },
1224	        {
1225	          "balanced_accuracy": 0.7143,
1226	          "accuracy": 0.7143,
1227	          "f1": 0.7143,
1228	          "peak_layer": 14
1229	        },
1230	        {
1231	          "balanced_accuracy": 0.7321,
1232	          "accuracy": 0.7321,
1233	          "f1": 0.7321,
1234	          "peak_layer": 23
1235	        },
1236	        {
1237	          "balanced_accuracy": 0.7321,
1238	          "accuracy": 0.7321,
1239	          "f1": 0.7321,
1240	          "peak_layer": 22
1241	        },
1242	        {
1243	          "balanced_accuracy": 0.7262,
1244	          "accuracy": 0.7262,
1245	          "f1": 0.7262,
1246	          "peak_layer": 14
1247	        },
1248	        {
1249	          "balanced_accuracy": 0.7381,
1250	          "accuracy": 0.7381,
1251	          "f1": 0.7381,
1252	          "peak_layer": 16
1253	        },
1254	        {
1255	          "balanced_accuracy": 0.7262,
1256	          "accuracy": 0.7262,
1257	          "f1": 0.7262,
1258	          "peak_layer": 21
1259	        },
1260	        {
1261	          "balanced_accuracy": 0.6786,
1262	          "accuracy": 0.6786,
1263	          "f1": 0.6786,
1264	          "peak_layer": 23
1265	        },
1266	        {
1267	          "balanced_accuracy": 0.7262,
1268	          "accuracy": 0.7262,
1269	          "f1": 0.7262,
1270	          "peak_layer": 18
1271	        },
1272	        {
1273	          "balanced_accuracy": 0.6845,
1274	          "accuracy": 0.6845,
1275	          "f1": 0.6845,
1276	          "peak_layer": 35
1277	        },
1278	        {
1279	          "balanced_accuracy": 0.7083,
1280	          "accuracy": 0.7083,
1281	          "f1": 0.7083,
1282	          "peak_layer": 21
1283	        },
1284	        {
1285	          "balanced_accuracy": 0.7262,
1286	          "accuracy": 0.7262,
1287	          "f1": 0.7262,
1288	          "peak_layer": 7
1289	        },
1290	        {
1291	          "balanced_accuracy": 0.7143,
1292	          "accuracy": 0.7143,
1293	          "f1": 0.7143,
1294	          "peak_layer": 34
1295	        },
1296	        {
1297	          "balanced_accuracy": 0.7143,
1298	          "accuracy": 0.7143,
1299	          "f1": 0.7143,
1300	          "peak_layer": 6
1301	        },
1302	        {
1303	          "balanced_accuracy": 0.7083,
1304	          "accuracy": 0.7083,
1305	          "f1": 0.7083,
1306	          "peak_layer": 21
1307	        },
1308	        {
1309	          "balanced_accuracy": 0.7262,
1310	          "accuracy": 0.7262,
1311	          "f1": 0.7262,
1312	          "peak_layer": 22
1313	        },
1314	        {
1315	          "balanced_accuracy": 0.7024,
1316	          "accuracy": 0.7024,
1317	          "f1": 0.7024,
1318	          "peak_layer": 6
1319	        },
1320	        {
1321	          "balanced_accuracy": 0.7381,
1322	          "accuracy": 0.7381,
1323	          "f1": 0.7381,
1324	          "peak_layer": 23
1325	        },
1326	        {
1327	          "balanced_accuracy": 0.6905,
1328	          "accuracy": 0.6905,
1329	          "f1": 0.6905,
1330	          "peak_layer": 27
1331	        },
1332	        {
1333	          "balanced_accuracy": 0.6964,
1334	          "accuracy": 0.6964,
1335	          "f1": 0.6964,
1336	          "peak_layer": 23
1337	        },
1338	        {
1339	          "balanced_accuracy": 0.6964,
1340	          "accuracy": 0.6964,
1341	          "f1": 0.6964,
1342	          "peak_layer": 21
1343	        },
1344	        {
1345	          "balanced_accuracy": 0.7202,
1346	          "accuracy": 0.7202,
1347	          "f1": 0.7202,
1348	          "peak_layer": 17
1349	        },
1350	        {
1351	          "balanced_accuracy": 0.7262,
1352	          "accuracy": 0.7262,
1353	          "f1": 0.7262,
1354	          "peak_layer": 23
1355	        },
1356	        {
1357	          "balanced_accuracy": 0.7143,
1358	          "accuracy": 0.7143,
1359	          "f1": 0.7143,
1360	          "peak_layer": 4
1361	        },
1362	        {
1363	          "balanced_accuracy": 0.7262,
1364	          "accuracy": 0.7262,
1365	          "f1": 0.7262,
1366	          "peak_layer": 21
1367	        },
1368	        {
1369	          "balanced_accuracy": 0.744,
1370	          "accuracy": 0.744,
1371	          "f1": 0.744,
1372	          "peak_layer": 17
1373	        },
1374	        {
1375	          "balanced_accuracy": 0.7202,
1376	          "accuracy": 0.7202,
1377	          "f1": 0.7202,
1378	          "peak_layer": 6
1379	        },
1380	        {
1381	          "balanced_accuracy": 0.744,
1382	          "accuracy": 0.744,
1383	          "f1": 0.744,
1384	          "peak_layer": 28
1385	        },
1386	        {
1387	          "balanced_accuracy": 0.7262,
1388	          "accuracy": 0.7262,
1389	          "f1": 0.7262,
1390	          "peak_layer": 14
1391	        },
1392	        {
1393	          "balanced_accuracy": 0.7202,
1394	          "accuracy": 0.7202,
1395	          "f1": 0.7202,
1396	          "peak_layer": 7
1397	        },
1398	        {
1399	          "balanced_accuracy": 0.7262,
1400	          "accuracy": 0.7262,
1401	          "f1": 0.7262,
1402	          "peak_layer": 21
1403	        },
1404	        {
1405	          "balanced_accuracy": 0.7083,
1406	          "accuracy": 0.7083,
1407	          "f1": 0.7083,
1408	          "peak_layer": 16
1409	        },
1410	        {
1411	          "balanced_accuracy": 0.7143,
1412	          "accuracy": 0.7143,
1413	          "f1": 0.7143,
1414	          "peak_layer": 14
1415	        },
1416	        {
1417	          "balanced_accuracy": 0.6845,
1418	          "accuracy": 0.6845,
1419	          "f1": 0.6845,
1420	          "peak_layer": 14
1421	        },
1422	        {
1423	          "balanced_accuracy": 0.7202,
1424	          "accuracy": 0.7202,
1425	          "f1": 0.7202,
1426	          "peak_layer": 23
1427	        }
1428	      ]
1429	    },
1430	    "EN→ZH": {
1431	      "direction": "EN→ZH",
1432	      "n_bootstrap": 100,
1433	      "balanced_accuracy_mean": 0.6496,
1434	      "balanced_accuracy_std": 0.0273,
1435	      "f1_mean": 0.6556,
1436	      "f1_std": 0.0472,
1437	      "peak_layers": [
1438	        22,
1439	        33,
1440	        23,
1441	        22,
1442	        22,
1443	        18,
1444	        18,
1445	        22,
1446	        21,
1447	        32,
1448	        16,
1449	        22,
1450	        24,
1451	        18,
1452	        22,
1453	        25,
1454	        19,
1455	        22,
1456	        28,
1457	        22,
1458	        21,
1459	        18,
1460	        21,
1461	        18,
1462	        24,
1463	        22,
1464	        22,
1465	        22,
1466	        23,
1467	        23,
1468	        18,
1469	        21,
1470	        18,
1471	        18,
1472	        22,
1473	        21,
1474	        22,
1475	        27,
1476	        18,
1477	        21,
1478	        21,
1479	        26,
1480	        17,
1481	        22,
1482	        18,
1483	        22,
1484	        22,
1485	        18,
1486	        22,
1487	        22,
1488	        33,
1489	        22,
1490	        22,
1491	        22,
1492	        28,
1493	        33,
1494	        22,
1495	        23,
1496	        22,
1497	        24,
1498	        22,
1499	        23,
1500	        24,
1501	        25,
1502	        21,
1503	        21,
1504	        22,
1505	        22,
1506	        22,
1507	        24,
1508	        26,
1509	        10,
1510	        25,
1511	        18,
1512	        27,
1513	        18,
1514	        25,
1515	        28,
1516	        22,
1517	        18,
1518	        22,
1519	        27,
1520	        25,
1521	        20,
1522	        21,
1523	        21,
1524	        18,
1525	        21,
1526	        22,
1527	        31,
1528	        22,
1529	        24,
1530	        18,
1531	        21,
1532	        21,
1533	        21,
1534	        24,
1535	        22,
1536	        21,
1537	        23
1538	      ],
1539	      "per_bootstrap": [
1540	        {
1541	          "balanced_accuracy": 0.6607,
1542	          "accuracy": 0.6607,
1543	          "f1": 0.6607,
1544	          "peak_layer": 22
1545	        },
1546	        {
1547	          "balanced_accuracy": 0.619,
1548	          "accuracy": 0.619,
1549	          "f1": 0.619,
1550	          "peak_layer": 33
1551	        },
1552	        {
1553	          "balanced_accuracy": 0.6488,
1554	          "accuracy": 0.6488,
1555	          "f1": 0.6488,
1556	          "peak_layer": 23
1557	        },
1558	        {
1559	          "balanced_accuracy": 0.631,
1560	          "accuracy": 0.631,
1561	          "f1": 0.631,
1562	          "peak_layer": 22
1563	        },
1564	        {
1565	          "balanced_accuracy": 0.6786,
1566	          "accuracy": 0.6786,
1567	          "f1": 0.6786,
1568	          "peak_layer": 22
1569	        },
1570	        {
1571	          "balanced_accuracy": 0.6786,
1572	          "accuracy": 0.6786,
1573	          "f1": 0.6786,
1574	          "peak_layer": 18
1575	        },
1576	        {
1577	          "balanced_accuracy": 0.6667,
1578	          "accuracy": 0.6667,
1579	          "f1": 0.6667,
1580	          "peak_layer": 18
1581	        },
1582	        {
1583	          "balanced_accuracy": 0.6786,
1584	          "accuracy": 0.6786,
1585	          "f1": 0.6786,
1586	          "peak_layer": 22
1587	        },
1588	        {
1589	          "balanced_accuracy": 0.6131,
1590	          "accuracy": 0.6131,
1591	          "f1": 0.6131,
1592	          "peak_layer": 21
1593	        },
1594	        {
1595	          "balanced_accuracy": 0.619,
1596	          "accuracy": 0.619,
1597	          "f1": 0.619,
1598	          "peak_layer": 32
1599	        },
1600	        {
1601	          "balanced_accuracy": 0.631,
1602	          "accuracy": 0.631,
1603	          "f1": 0.631,
1604	          "peak_layer": 16
1605	        },
1606	        {
1607	          "balanced_accuracy": 0.7083,
1608	          "accuracy": 0.7083,
1609	          "f1": 0.7083,
1610	          "peak_layer": 22
1611	        },
1612	        {
1613	          "balanced_accuracy": 0.6667,
1614	          "accuracy": 0.6667,
1615	          "f1": 0.6667,
1616	          "peak_layer": 24
1617	        },
1618	        {
1619	          "balanced_accuracy": 0.6607,
1620	          "accuracy": 0.6607,
1621	          "f1": 0.6607,
1622	          "peak_layer": 18
1623	        },
1624	        {
1625	          "balanced_accuracy": 0.6845,
1626	          "accuracy": 0.6845,
1627	          "f1": 0.6845,
1628	          "peak_layer": 22
1629	        },
1630	        {
1631	          "balanced_accuracy": 0.6369,
1632	          "accuracy": 0.6369,
1633	          "f1": 0.6369,
1634	          "peak_layer": 25
1635	        },
1636	        {
1637	          "balanced_accuracy": 0.6726,
1638	          "accuracy": 0.6726,
1639	          "f1": 0.6726,
1640	          "peak_layer": 19
1641	        },
1642	        {
1643	          "balanced_accuracy": 0.6905,
1644	          "accuracy": 0.6905,
1645	          "f1": 0.6905,
1646	          "peak_layer": 22
1647	        },
1648	        {
1649	          "balanced_accuracy": 0.6369,
1650	          "accuracy": 0.6369,
1651	          "f1": 0.6369,
1652	          "peak_layer": 28
1653	        },
1654	        {
1655	          "balanced_accuracy": 0.6548,
1656	          "accuracy": 0.6548,
1657	          "f1": 0.6548,
1658	          "peak_layer": 22
1659	        },
1660	        {
1661	          "balanced_accuracy": 0.5893,
1662	          "accuracy": 0.5893,
1663	          "f1": 0.5893,
1664	          "peak_layer": 21
1665	        },
1666	        {
1667	          "balanced_accuracy": 0.6548,
1668	          "accuracy": 0.6548,
1669	          "f1": 0.6548,
1670	          "peak_layer": 18
1671	        },
1672	        {
1673	          "balanced_accuracy": 0.6369,
1674	          "accuracy": 0.6369,
1675	          "f1": 0.6369,
1676	          "peak_layer": 21
1677	        },
1678	        {
1679	          "balanced_accuracy": 0.6667,
1680	          "accuracy": 0.6667,
1681	          "f1": 0.6667,
1682	          "peak_layer": 18
1683	        },
1684	        {
1685	          "balanced_accuracy": 0.6786,
1686	          "accuracy": 0.6786,
1687	          "f1": 0.6786,
1688	          "peak_layer": 24
1689	        },
1690	        {
1691	          "balanced_accuracy": 0.619,
1692	          "accuracy": 0.619,
1693	          "f1": 0.619,
1694	          "peak_layer": 22
1695	        },
1696	        {
1697	          "balanced_accuracy": 0.6786,
1698	          "accuracy": 0.6786,
1699	          "f1": 0.6786,
1700	          "peak_layer": 22
1701	        },
1702	        {
1703	          "balanced_accuracy": 0.7202,
1704	          "accuracy": 0.7202,
1705	          "f1": 0.7202,
1706	          "peak_layer": 22
1707	        },
1708	        {
1709	          "balanced_accuracy": 0.6369,
1710	          "accuracy": 0.6369,
1711	          "f1": 0.6369,
1712	          "peak_layer": 23
1713	        },
1714	        {
1715	          "balanced_accuracy": 0.6726,
1716	          "accuracy": 0.6726,
1717	          "f1": 0.6726,
1718	          "peak_layer": 23
1719	        },
1720	        {
1721	          "balanced_accuracy": 0.625,
1722	          "accuracy": 0.625,
1723	          "f1": 0.625,
1724	          "peak_layer": 18
1725	        },
1726	        {
1727	          "balanced_accuracy": 0.6726,
1728	          "accuracy": 0.6726,
1729	          "f1": 0.6726,
1730	          "peak_layer": 21
1731	        },
1732	        {
1733	          "balanced_accuracy": 0.6488,
1734	          "accuracy": 0.6488,
1735	          "f1": 0.6488,
1736	          "peak_layer": 18
1737	        },
1738	        {
1739	          "balanced_accuracy": 0.6607,
1740	          "accuracy": 0.6607,
1741	          "f1": 0.6607,
1742	          "peak_layer": 18
1743	        },
1744	        {
1745	          "balanced_accuracy": 0.6548,
1746	          "accuracy": 0.6548,
1747	          "f1": 0.6548,
1748	          "peak_layer": 22
1749	        },
1750	        {
1751	          "balanced_accuracy": 0.6607,
1752	          "accuracy": 0.6607,
1753	          "f1": 0.6607,
1754	          "peak_layer": 21
1755	        },
1756	        {
1757	          "balanced_accuracy": 0.7024,
1758	          "accuracy": 0.7024,
1759	          "f1": 0.7024,
1760	          "peak_layer": 22
1761	        },
1762	        {
1763	          "balanced_accuracy": 0.6131,
1764	          "accuracy": 0.6131,
1765	          "f1": 0.6131,
1766	          "peak_layer": 27
1767	        },
1768	        {
1769	          "balanced_accuracy": 0.6667,
1770	          "accuracy": 0.6667,
1771	          "f1": 0.6667,
1772	          "peak_layer": 18
1773	        },
1774	        {
1775	          "balanced_accuracy": 0.6429,
1776	          "accuracy": 0.6429,
1777	          "f1": 0.6429,
1778	          "peak_layer": 21
1779	        },
1780	        {
1781	          "balanced_accuracy": 0.631,
1782	          "accuracy": 0.631,
1783	          "f1": 0.631,
1784	          "peak_layer": 21
1785	        },
1786	        {
1787	          "balanced_accuracy": 0.6429,
1788	          "accuracy": 0.6429,
1789	          "f1": 0.6429,
1790	          "peak_layer": 26
1791	        },
1792	        {
1793	          "balanced_accuracy": 0.625,
1794	          "accuracy": 0.625,
1795	          "f1": 0.625,
1796	          "peak_layer": 17
1797	        },
1798	        {
1799	          "balanced_accuracy": 0.6548,
1800	          "accuracy": 0.6548,
1801	          "f1": 0.6548,
1802	          "peak_layer": 22
1803	        },
1804	        {
1805	          "balanced_accuracy": 0.6131,
1806	          "accuracy": 0.6131,
1807	          "f1": 0.6131,
1808	          "peak_layer": 18
1809	        },
1810	        {
1811	          "balanced_accuracy": 0.6607,
1812	          "accuracy": 0.6607,
1813	          "f1": 0.6607,
1814	          "peak_layer": 22
1815	        },
1816	        {
1817	          "balanced_accuracy": 0.6607,
1818	          "accuracy": 0.6607,
1819	          "f1": 0.6607,
1820	          "peak_layer": 22
1821	        },
1822	        {
1823	          "balanced_accuracy": 0.6726,
1824	          "accuracy": 0.6726,
1825	          "f1": 0.6726,
1826	          "peak_layer": 18
1827	        },
1828	        {
1829	          "balanced_accuracy": 0.619,
1830	          "accuracy": 0.619,
1831	          "f1": 0.619,
1832	          "peak_layer": 22
1833	        },
1834	        {
1835	          "balanced_accuracy": 0.6548,
1836	          "accuracy": 0.6548,
1837	          "f1": 0.6548,
1838	          "peak_layer": 22
1839	        },
1840	        {
1841	          "balanced_accuracy": 0.6369,
1842	          "accuracy": 0.6369,
1843	          "f1": 0.6369,
1844	          "peak_layer": 33
1845	        },
1846	        {
1847	          "balanced_accuracy": 0.6012,
1848	          "accuracy": 0.6012,
1849	          "f1": 0.6012,
1850	          "peak_layer": 22
1851	        },
1852	        {
1853	          "balanced_accuracy": 0.6667,
1854	          "accuracy": 0.6667,
1855	          "f1": 0.6667,
1856	          "peak_layer": 22
1857	        },
1858	        {
1859	          "balanced_accuracy": 0.5952,
1860	          "accuracy": 0.5952,
1861	          "f1": 0.5952,
1862	          "peak_layer": 22
1863	        },
1864	        {
1865	          "balanced_accuracy": 0.6369,
1866	          "accuracy": 0.6369,
1867	          "f1": 0.6369,
1868	          "peak_layer": 28
1869	        },
1870	        {
1871	          "balanced_accuracy": 0.6369,
1872	          "accuracy": 0.6369,
1873	          "f1": 0.6369,
1874	          "peak_layer": 33
1875	        },
1876	        {
1877	          "balanced_accuracy": 0.619,
1878	          "accuracy": 0.619,
1879	          "f1": 0.619,
1880	          "peak_layer": 22
1881	        },
1882	        {
1883	          "balanced_accuracy": 0.6786,
1884	          "accuracy": 0.6786,
1885	          "f1": 0.6786,
1886	          "peak_layer": 23
1887	        },
1888	        {
1889	          "balanced_accuracy": 0.6786,
1890	          "accuracy": 0.6786,
1891	          "f1": 0.6786,
1892	          "peak_layer": 22
1893	        },
1894	        {
1895	          "balanced_accuracy": 0.6369,
1896	          "accuracy": 0.6369,
1897	          "f1": 0.6369,
1898	          "peak_layer": 24
1899	        },
1900	        {
1901	          "balanced_accuracy": 0.6548,
1902	          "accuracy": 0.6548,
1903	          "f1": 0.6548,
1904	          "peak_layer": 22
1905	        },
1906	        {
1907	          "balanced_accuracy": 0.6726,
1908	          "accuracy": 0.6726,
1909	          "f1": 0.6726,
1910	          "peak_layer": 23
1911	        },
1912	        {
1913	          "balanced_accuracy": 0.6429,
1914	          "accuracy": 0.6429,
1915	          "f1": 0.6429,
1916	          "peak_layer": 24
1917	        },
1918	        {
1919	          "balanced_accuracy": 0.6726,
1920	          "accuracy": 0.6726,
1921	          "f1": 0.6726,
1922	          "peak_layer": 25
1923	        },
1924	        {
1925	          "balanced_accuracy": 0.6607,
1926	          "accuracy": 0.6607,
1927	          "f1": 0.6607,
1928	          "peak_layer": 21
1929	        },
1930	        {
1931	          "balanced_accuracy": 0.6131,
1932	          "accuracy": 0.6131,
1933	          "f1": 0.6131,
1934	          "peak_layer": 21
1935	        },
1936	        {
1937	          "balanced_accuracy": 0.6369,
1938	          "accuracy": 0.6369,
1939	          "f1": 0.6369,
1940	          "peak_layer": 22
1941	        },
1942	        {
1943	          "balanced_accuracy": 0.7083,
1944	          "accuracy": 0.7083,
1945	          "f1": 0.7083,
1946	          "peak_layer": 22
1947	        },
1948	        {
1949	          "balanced_accuracy": 0.6667,
1950	          "accuracy": 0.6667,
1951	          "f1": 0.6667,
1952	          "peak_layer": 22
1953	        },
1954	        {
1955	          "balanced_accuracy": 0.6607,
1956	          "accuracy": 0.6607,
1957	          "f1": 0.6607,
1958	          "peak_layer": 24
1959	        },
1960	        {
1961	          "balanced_accuracy": 0.6667,
1962	          "accuracy": 0.6667,
1963	          "f1": 0.6667,
1964	          "peak_layer": 26
1965	        },
1966	        {
1967	          "balanced_accuracy": 0.625,
1968	          "accuracy": 0.625,
1969	          "f1": 0.625,
1970	          "peak_layer": 10
1971	        },
1972	        {
1973	          "balanced_accuracy": 0.5833,
1974	          "accuracy": 0.5833,
1975	          "f1": 0.5833,
1976	          "peak_layer": 25
1977	        },
1978	        {
1979	          "balanced_accuracy": 0.631,
1980	          "accuracy": 0.631,
1981	          "f1": 0.631,
1982	          "peak_layer": 18
1983	        },
1984	        {
1985	          "balanced_accuracy": 0.6369,
1986	          "accuracy": 0.6369,
1987	          "f1": 0.6369,
1988	          "peak_layer": 27
1989	        },
1990	        {
1991	          "balanced_accuracy": 0.6488,
1992	          "accuracy": 0.6488,
1993	          "f1": 0.6488,
1994	          "peak_layer": 18
1995	        },
1996	        {
1997	          "balanced_accuracy": 0.625,
1998	          "accuracy": 0.625,
1999	          "f1": 0.625,
2000	          "peak_layer": 25
2001	        },
2002	        {
2003	          "balanced_accuracy": 0.6429,
2004	          "accuracy": 0.6429,
2005	          "f1": 0.6429,
2006	          "peak_layer": 28
2007	        },
2008	        {
2009	          "balanced_accuracy": 0.6071,
2010	          "accuracy": 0.6071,
2011	          "f1": 0.6071,
2012	          "peak_layer": 22
2013	        },
2014	        {
2015	          "balanced_accuracy": 0.6607,
2016	          "accuracy": 0.6607,
2017	          "f1": 0.6607,
2018	          "peak_layer": 18
2019	        },
2020	        {
2021	          "balanced_accuracy": 0.6369,
2022	          "accuracy": 0.6369,
2023	          "f1": 0.6369,
2024	          "peak_layer": 22
2025	        },
2026	        {
2027	          "balanced_accuracy": 0.6548,
2028	          "accuracy": 0.6548,
2029	          "f1": 0.6548,
2030	          "peak_layer": 27
2031	        },
2032	        {
2033	          "balanced_accuracy": 0.6429,
2034	          "accuracy": 0.6429,
2035	          "f1": 0.6429,
2036	          "peak_layer": 25
2037	        },
2038	        {
2039	          "balanced_accuracy": 0.6131,
2040	          "accuracy": 0.6131,
2041	          "f1": 0.6131,
2042	          "peak_layer": 20
2043	        },
2044	        {
2045	          "balanced_accuracy": 0.619,
2046	          "accuracy": 0.619,
2047	          "f1": 0.619,
2048	          "peak_layer": 21
2049	        },
2050	        {
2051	          "balanced_accuracy": 0.6488,
2052	          "accuracy": 0.6488,
2053	          "f1": 0.6488,
2054	          "peak_layer": 21
2055	        },
2056	        {
2057	          "balanced_accuracy": 0.631,
2058	          "accuracy": 0.631,
2059	          "f1": 0.631,
2060	          "peak_layer": 18
2061	        },
2062	        {
2063	          "balanced_accuracy": 0.6488,
2064	          "accuracy": 0.6488,
2065	          "f1": 0.6488,
2066	          "peak_layer": 21
2067	        },
2068	        {
2069	          "balanced_accuracy": 0.7321,
2070	          "accuracy": 0.7321,
2071	          "f1": 0.7321,
2072	          "peak_layer": 22
2073	        },
2074	        {
2075	          "balanced_accuracy": 0.6369,
2076	          "accuracy": 0.6369,
2077	          "f1": 0.6369,
2078	          "peak_layer": 31
2079	        },
2080	        {
2081	          "balanced_accuracy": 0.6607,
2082	          "accuracy": 0.6607,
2083	          "f1": 0.6607,
2084	          "peak_layer": 22
2085	        },
2086	        {
2087	          "balanced_accuracy": 0.6429,
2088	          "accuracy": 0.6429,
2089	          "f1": 0.6429,
2090	          "peak_layer": 24
2091	        },
2092	        {
2093	          "balanced_accuracy": 0.6786,
2094	          "accuracy": 0.6786,
2095	          "f1": 0.6786,
2096	          "peak_layer": 18
2097	        },
2098	        {
2099	          "balanced_accuracy": 0.6964,
2100	          "accuracy": 0.6964,
2101	          "f1": 0.6964,
2102	          "peak_layer": 21
2103	        },
2104	        {
2105	          "balanced_accuracy": 0.6548,
2106	          "accuracy": 0.6548,
2107	          "f1": 0.6548,
2108	          "peak_layer": 21
2109	        },
2110	        {
2111	          "balanced_accuracy": 0.6369,
2112	          "accuracy": 0.6369,
2113	          "f1": 0.6369,
2114	          "peak_layer": 21
2115	        },
2116	        {
2117	          "balanced_accuracy": 0.6429,
2118	          "accuracy": 0.6429,
2119	          "f1": 0.6429,
2120	          "peak_layer": 24
2121	        },
2122	        {
2123	          "balanced_accuracy": 0.6429,
2124	          "accuracy": 0.6429,
2125	          "f1": 0.6429,
2126	          "peak_layer": 22
2127	        },
2128	        {
2129	          "balanced_accuracy": 0.6369,
2130	          "accuracy": 0.6369,
2131	          "f1": 0.6369,
2132	          "peak_layer": 21
2133	        },
2134	        {
2135	          "balanced_accuracy": 0.631,
2136	          "accuracy": 0.631,
2137	          "f1": 0.631,
2138	          "peak_layer": 23
2139	        }
2140	      ]
2141	    },
2142	    "ZH→EN": {
2143	      "direction": "ZH→EN",
2144	      "n_bootstrap": 100,
2145	      "balanced_accuracy_mean": 0.7215,
2146	      "balanced_accuracy_std": 0.0256,
2147	      "f1_mean": 0.711,
2148	      "f1_std": 0.0464,
2149	      "peak_layers": [
2150	        21,
2151	        20,
2152	        24,
2153	        19,
2154	        15,
2155	        23,
2156	        26,
2157	        21,
2158	        19,
2159	        25,
2160	        23,
2161	        21,
2162	        19,
2163	        23,
2164	        18,
2165	        19,
2166	        19,
2167	        19,
2168	        19,
2169	        21,
2170	        19,
2171	        19,
2172	        21,
2173	        15,
2174	        18,
2175	        21,
2176	        23,
2177	        15,
2178	        19,
2179	        23,
2180	        24,
2181	        21,
2182	        23,
2183	        22,
2184	        18,
2185	        16,
2186	        21,
2187	        16,
2188	        18,
2189	        24,
2190	        19,
2191	        23,
2192	        18,
2193	        23,
2194	        21,
2195	        18,
2196	        25,
2197	        22,
2198	        18,
2199	        19,
2200	        20,
2201	        22,
2202	        18,
2203	        25,
2204	        21,
2205	        15,
2206	        17,
2207	        16,
2208	        25,
2209	        21,
2210	        23,
2211	        21,
2212	        15,
2213	        16,
2214	        19,
2215	        21,
2216	        23,
2217	        24,
2218	        23,
2219	        23,
2220	        25,
2221	        17,
2222	        18,
2223	        18,
2224	        20,
2225	        21,
2226	        23,
2227	        25,
2228	        12,
2229	        13,
2230	        24,
2231	        18,
2232	        19,
2233	        23,
2234	        25,
2235	        21,
2236	        18,
2237	        17,
2238	        20,
2239	        1,
2240	        18,
2241	        20,
2242	        24,
2243	        18,
2244	        21,
2245	        19,
2246	        21,
2247	        14,
2248	        18,
2249	        22
2250	      ],
2251	      "per_bootstrap": [
2252	        {
2253	          "balanced_accuracy": 0.7381,
2254	          "accuracy": 0.7381,
2255	          "f1": 0.7381,
2256	          "peak_layer": 21
2257	        },
2258	        {
2259	          "balanced_accuracy": 0.7619,
2260	          "accuracy": 0.7619,
2261	          "f1": 0.7619,
2262	          "peak_layer": 20
2263	        },
2264	        {
2265	          "balanced_accuracy": 0.7202,
2266	          "accuracy": 0.7202,
2267	          "f1": 0.7202,
2268	          "peak_layer": 24
2269	        },
2270	        {
2271	          "balanced_accuracy": 0.7619,
2272	          "accuracy": 0.7619,
2273	          "f1": 0.7619,
2274	          "peak_layer": 19
2275	        },
2276	        {
2277	          "balanced_accuracy": 0.7381,
2278	          "accuracy": 0.7381,
2279	          "f1": 0.7381,
2280	          "peak_layer": 15
2281	        },
2282	        {
2283	          "balanced_accuracy": 0.75,
2284	          "accuracy": 0.75,
2285	          "f1": 0.75,
2286	          "peak_layer": 23
2287	        },
2288	        {
2289	          "balanced_accuracy": 0.756,
2290	          "accuracy": 0.756,
2291	          "f1": 0.756,
2292	          "peak_layer": 26
2293	        },
2294	        {
2295	          "balanced_accuracy": 0.6845,
2296	          "accuracy": 0.6845,
2297	          "f1": 0.6845,
2298	          "peak_layer": 21
2299	        },
2300	        {
2301	          "balanced_accuracy": 0.6905,
2302	          "accuracy": 0.6905,
2303	          "f1": 0.6905,
2304	          "peak_layer": 19
2305	        },
2306	        {
2307	          "balanced_accuracy": 0.744,
2308	          "accuracy": 0.744,
2309	          "f1": 0.744,
2310	          "peak_layer": 25
2311	        },
2312	        {
2313	          "balanced_accuracy": 0.744,
2314	          "accuracy": 0.744,
2315	          "f1": 0.744,
2316	          "peak_layer": 23
2317	        },
2318	        {
2319	          "balanced_accuracy": 0.6845,
2320	          "accuracy": 0.6845,
2321	          "f1": 0.6845,
2322	          "peak_layer": 21
2323	        },
2324	        {
2325	          "balanced_accuracy": 0.744,
2326	          "accuracy": 0.744,
2327	          "f1": 0.744,
2328	          "peak_layer": 19
2329	        },
2330	        {
2331	          "balanced_accuracy": 0.7083,
2332	          "accuracy": 0.7083,
2333	          "f1": 0.7083,
2334	          "peak_layer": 23
2335	        },
2336	        {
2337	          "balanced_accuracy": 0.756,
2338	          "accuracy": 0.756,
2339	          "f1": 0.756,
2340	          "peak_layer": 18
2341	        },
2342	        {
2343	          "balanced_accuracy": 0.7381,
2344	          "accuracy": 0.7381,
2345	          "f1": 0.7381,
2346	          "peak_layer": 19
2347	        },
2348	        {
2349	          "balanced_accuracy": 0.7321,
2350	          "accuracy": 0.7321,
2351	          "f1": 0.7321,
2352	          "peak_layer": 19
2353	        },
2354	        {
2355	          "balanced_accuracy": 0.7321,
2356	          "accuracy": 0.7321,
2357	          "f1": 0.7321,
2358	          "peak_layer": 19
2359	        },
2360	        {
2361	          "balanced_accuracy": 0.6905,
2362	          "accuracy": 0.6905,
2363	          "f1": 0.6905,
2364	          "peak_layer": 19
2365	        },
2366	        {
2367	          "balanced_accuracy": 0.744,
2368	          "accuracy": 0.744,
2369	          "f1": 0.744,
2370	          "peak_layer": 21
2371	        },
2372	        {
2373	          "balanced_accuracy": 0.7083,
2374	          "accuracy": 0.7083,
2375	          "f1": 0.7083,
2376	          "peak_layer": 19
2377	        },
2378	        {
2379	          "balanced_accuracy": 0.7024,
2380	          "accuracy": 0.7024,
2381	          "f1": 0.7024,
2382	          "peak_layer": 19
2383	        },
2384	        {
2385	          "balanced_accuracy": 0.6964,
2386	          "accuracy": 0.6964,
2387	          "f1": 0.6964,
2388	          "peak_layer": 21
2389	        },
2390	        {
2391	          "balanced_accuracy": 0.7262,
2392	          "accuracy": 0.7262,
2393	          "f1": 0.7262,
2394	          "peak_layer": 15
2395	        },
2396	        {
2397	          "balanced_accuracy": 0.7143,
2398	          "accuracy": 0.7143,
2399	          "f1": 0.7143,
2400	          "peak_layer": 18
2401	        },
2402	        {
2403	          "balanced_accuracy": 0.7321,
2404	          "accuracy": 0.7321,
2405	          "f1": 0.7321,
2406	          "peak_layer": 21
2407	        },
2408	        {
2409	          "balanced_accuracy": 0.6667,
2410	          "accuracy": 0.6667,
2411	          "f1": 0.6667,
2412	          "peak_layer": 23
2413	        },
2414	        {
2415	          "balanced_accuracy": 0.7262,
2416	          "accuracy": 0.7262,
2417	          "f1": 0.7262,
2418	          "peak_layer": 15
2419	        },
2420	        {
2421	          "balanced_accuracy": 0.744,
2422	          "accuracy": 0.744,
2423	          "f1": 0.744,
2424	          "peak_layer": 19
2425	        },
2426	        {
2427	          "balanced_accuracy": 0.7024,
2428	          "accuracy": 0.7024,
2429	          "f1": 0.7024,
2430	          "peak_layer": 23
2431	        },
2432	        {
2433	          "balanced_accuracy": 0.6786,
2434	          "accuracy": 0.6786,
2435	          "f1": 0.6786,
2436	          "peak_layer": 24
2437	        },
2438	        {
2439	          "balanced_accuracy": 0.7381,
2440	          "accuracy": 0.7381,
2441	          "f1": 0.7381,
2442	          "peak_layer": 21
2443	        },
2444	        {
2445	          "balanced_accuracy": 0.7321,
2446	          "accuracy": 0.7321,
2447	          "f1": 0.7321,
2448	          "peak_layer": 23
2449	        },
2450	        {
2451	          "balanced_accuracy": 0.7143,
2452	          "accuracy": 0.7143,
2453	          "f1": 0.7143,
2454	          "peak_layer": 22
2455	        },
2456	        {
2457	          "balanced_accuracy": 0.7262,
2458	          "accuracy": 0.7262,
2459	          "f1": 0.7262,
2460	          "peak_layer": 18
2461	        },
2462	        {
2463	          "balanced_accuracy": 0.7143,
2464	          "accuracy": 0.7143,
2465	          "f1": 0.7143,
2466	          "peak_layer": 16
2467	        },
2468	        {
2469	          "balanced_accuracy": 0.7202,
2470	          "accuracy": 0.7202,
2471	          "f1": 0.7202,
2472	          "peak_layer": 21
2473	        },
2474	        {
2475	          "balanced_accuracy": 0.7381,
2476	          "accuracy": 0.7381,
2477	          "f1": 0.7381,
2478	          "peak_layer": 16
2479	        },
2480	        {
2481	          "balanced_accuracy": 0.75,
2482	          "accuracy": 0.75,
2483	          "f1": 0.75,
2484	          "peak_layer": 18
2485	        },
2486	        {
2487	          "balanced_accuracy": 0.6726,
2488	          "accuracy": 0.6726,
2489	          "f1": 0.6726,
2490	          "peak_layer": 24
2491	        },
2492	        {
2493	          "balanced_accuracy": 0.7619,
2494	          "accuracy": 0.7619,
2495	          "f1": 0.7619,
2496	          "peak_layer": 19
2497	        },
2498	        {
2499	          "balanced_accuracy": 0.7143,
2500	          "accuracy": 0.7143,
2501	          "f1": 0.7143,
2502	          "peak_layer": 23
2503	        },
2504	        {
2505	          "balanced_accuracy": 0.7738,
2506	          "accuracy": 0.7738,
2507	          "f1": 0.7738,
2508	          "peak_layer": 18
2509	        },
2510	        {
2511	          "balanced_accuracy": 0.7143,
2512	          "accuracy": 0.7143,
2513	          "f1": 0.7143,
2514	          "peak_layer": 23
2515	        },
2516	        {
2517	          "balanced_accuracy": 0.6845,
2518	          "accuracy": 0.6845,
2519	          "f1": 0.6845,
2520	          "peak_layer": 21
2521	        },
2522	        {
2523	          "balanced_accuracy": 0.7262,
2524	          "accuracy": 0.7262,
2525	          "f1": 0.7262,
2526	          "peak_layer": 18
2527	        },
2528	        {
2529	          "balanced_accuracy": 0.7321,
2530	          "accuracy": 0.7321,
2531	          "f1": 0.7321,
2532	          "peak_layer": 25
2533	        },
2534	        {
2535	          "balanced_accuracy": 0.75,
2536	          "accuracy": 0.75,
2537	          "f1": 0.75,
2538	          "peak_layer": 22
2539	        },
2540	        {
2541	          "balanced_accuracy": 0.744,
2542	          "accuracy": 0.744,
2543	          "f1": 0.744,
2544	          "peak_layer": 18
2545	        },
2546	        {
2547	          "balanced_accuracy": 0.756,
2548	          "accuracy": 0.756,
2549	          "f1": 0.756,
2550	          "peak_layer": 19
2551	        },
2552	        {
2553	          "balanced_accuracy": 0.6667,
2554	          "accuracy": 0.6667,
2555	          "f1": 0.6667,
2556	          "peak_layer": 20
2557	        },
2558	        {
2559	          "balanced_accuracy": 0.7321,
2560	          "accuracy": 0.7321,
2561	          "f1": 0.7321,
2562	          "peak_layer": 22
2563	        },
2564	        {
2565	          "balanced_accuracy": 0.6964,
2566	          "accuracy": 0.6964,
2567	          "f1": 0.6964,
2568	          "peak_layer": 18
2569	        },
2570	        {
2571	          "balanced_accuracy": 0.7321,
2572	          "accuracy": 0.7321,
2573	          "f1": 0.7321,
2574	          "peak_layer": 25
2575	        },
2576	        {
2577	          "balanced_accuracy": 0.7262,
2578	          "accuracy": 0.7262,
2579	          "f1": 0.7262,
2580	          "peak_layer": 21
2581	        },
2582	        {
2583	          "balanced_accuracy": 0.75,
2584	          "accuracy": 0.75,
2585	          "f1": 0.75,
2586	          "peak_layer": 15
2587	        },
2588	        {
2589	          "balanced_accuracy": 0.6964,
2590	          "accuracy": 0.6964,
2591	          "f1": 0.6964,
2592	          "peak_layer": 17
2593	        },
2594	        {
2595	          "balanced_accuracy": 0.75,
2596	          "accuracy": 0.75,
2597	          "f1": 0.75,
2598	          "peak_layer": 16
2599	        },
2600	        {
2601	          "balanced_accuracy": 0.6667,
2602	          "accuracy": 0.6667,
2603	          "f1": 0.6667,
2604	          "peak_layer": 25
2605	        },
2606	        {
2607	          "balanced_accuracy": 0.7381,
2608	          "accuracy": 0.7381,
2609	          "f1": 0.7381,
2610	          "peak_layer": 21
2611	        },
2612	        {
2613	          "balanced_accuracy": 0.756,
2614	          "accuracy": 0.756,
2615	          "f1": 0.756,
2616	          "peak_layer": 23
2617	        },
2618	        {
2619	          "balanced_accuracy": 0.7083,
2620	          "accuracy": 0.7083,
2621	          "f1": 0.7083,
2622	          "peak_layer": 21
2623	        },
2624	        {
2625	          "balanced_accuracy": 0.7202,
2626	          "accuracy": 0.7202,
2627	          "f1": 0.7202,
2628	          "peak_layer": 15
2629	        },
2630	        {
2631	          "balanced_accuracy": 0.7202,
2632	          "accuracy": 0.7202,
2633	          "f1": 0.7202,
2634	          "peak_layer": 16
2635	        },
2636	        {
2637	          "balanced_accuracy": 0.7202,
2638	          "accuracy": 0.7202,
2639	          "f1": 0.7202,
2640	          "peak_layer": 19
2641	        },
2642	        {
2643	          "balanced_accuracy": 0.6964,
2644	          "accuracy": 0.6964,
2645	          "f1": 0.6964,
2646	          "peak_layer": 21
2647	        },
2648	        {
2649	          "balanced_accuracy": 0.7202,
2650	          "accuracy": 0.7202,
2651	          "f1": 0.7202,
2652	          "peak_layer": 23
2653	        },
2654	        {
2655	          "balanced_accuracy": 0.75,
2656	          "accuracy": 0.75,
2657	          "f1": 0.75,
2658	          "peak_layer": 24
2659	        },
2660	        {
2661	          "balanced_accuracy": 0.7381,
2662	          "accuracy": 0.7381,
2663	          "f1": 0.7381,
2664	          "peak_layer": 23
2665	        },
2666	        {
2667	          "balanced_accuracy": 0.6786,
2668	          "accuracy": 0.6786,
2669	          "f1": 0.6786,
2670	          "peak_layer": 23
2671	        },
2672	        {
2673	          "balanced_accuracy": 0.6905,
2674	          "accuracy": 0.6905,
2675	          "f1": 0.6905,
2676	          "peak_layer": 25
2677	        },
2678	        {
2679	          "balanced_accuracy": 0.7262,
2680	          "accuracy": 0.7262,
2681	          "f1": 0.7262,
2682	          "peak_layer": 17
2683	        },
2684	        {
2685	          "balanced_accuracy": 0.7143,
2686	          "accuracy": 0.7143,
2687	          "f1": 0.7143,
2688	          "peak_layer": 18
2689	        },
2690	        {
2691	          "balanced_accuracy": 0.7143,
2692	          "accuracy": 0.7143,
2693	          "f1": 0.7143,
2694	          "peak_layer": 18
2695	        },
2696	        {
2697	          "balanced_accuracy": 0.7143,
2698	          "accuracy": 0.7143,
2699	          "f1": 0.7143,
2700	          "peak_layer": 20
2701	        },
2702	        {
2703	          "balanced_accuracy": 0.7143,
2704	          "accuracy": 0.7143,
2705	          "f1": 0.7143,
2706	          "peak_layer": 21
2707	        },
2708	        {
2709	          "balanced_accuracy": 0.7024,
2710	          "accuracy": 0.7024,
2711	          "f1": 0.7024,
2712	          "peak_layer": 23
2713	        },
2714	        {
2715	          "balanced_accuracy": 0.7024,
2716	          "accuracy": 0.7024,
2717	          "f1": 0.7024,
2718	          "peak_layer": 25
2719	        },
2720	        {
2721	          "balanced_accuracy": 0.6726,
2722	          "accuracy": 0.6726,
2723	          "f1": 0.6726,
2724	          "peak_layer": 12
2725	        },
2726	        {
2727	          "balanced_accuracy": 0.7143,
2728	          "accuracy": 0.7143,
2729	          "f1": 0.7143,
2730	          "peak_layer": 13
2731	        },
2732	        {
2733	          "balanced_accuracy": 0.6905,
2734	          "accuracy": 0.6905,
2735	          "f1": 0.6905,
2736	          "peak_layer": 24
2737	        },
2738	        {
2739	          "balanced_accuracy": 0.7619,
2740	          "accuracy": 0.7619,
2741	          "f1": 0.7619,
2742	          "peak_layer": 18
2743	        },
2744	        {
2745	          "balanced_accuracy": 0.7143,
2746	          "accuracy": 0.7143,
2747	          "f1": 0.7143,
2748	          "peak_layer": 19
2749	        },
2750	        {
2751	          "balanced_accuracy": 0.6964,
2752	          "accuracy": 0.6964,
2753	          "f1": 0.6964,
2754	          "peak_layer": 23
2755	        },
2756	        {
2757	          "balanced_accuracy": 0.7262,
2758	          "accuracy": 0.7262,
2759	          "f1": 0.7262,
2760	          "peak_layer": 25
2761	        },
2762	        {
2763	          "balanced_accuracy": 0.7024,
2764	          "accuracy": 0.7024,
2765	          "f1": 0.7024,
2766	          "peak_layer": 21
2767	        },
2768	        {
2769	          "balanced_accuracy": 0.744,
2770	          "accuracy": 0.744,
2771	          "f1": 0.744,
2772	          "peak_layer": 18
2773	        },
2774	        {
2775	          "balanced_accuracy": 0.7083,
2776	          "accuracy": 0.7083,
2777	          "f1": 0.7083,
2778	          "peak_layer": 17
2779	        },
2780	        {
2781	          "balanced_accuracy": 0.6964,
2782	          "accuracy": 0.6964,
2783	          "f1": 0.6964,
2784	          "peak_layer": 20
2785	        },
2786	        {
2787	          "balanced_accuracy": 0.6845,
2788	          "accuracy": 0.6845,
2789	          "f1": 0.6845,
2790	          "peak_layer": 1
2791	        },
2792	        {
2793	          "balanced_accuracy": 0.75,
2794	          "accuracy": 0.75,
2795	          "f1": 0.75,
2796	          "peak_layer": 18
2797	        },
2798	        {
2799	          "balanced_accuracy": 0.744,
2800	          "accuracy": 0.744,
2801	          "f1": 0.744,
2802	          "peak_layer": 20
2803	        },
2804	        {
2805	          "balanced_accuracy": 0.7381,
2806	          "accuracy": 0.7381,
2807	          "f1": 0.7381,
2808	          "peak_layer": 24
2809	        },
2810	        {
2811	          "balanced_accuracy": 0.7321,
2812	          "accuracy": 0.7321,
2813	          "f1": 0.7321,
2814	          "peak_layer": 18
2815	        },
2816	        {
2817	          "balanced_accuracy": 0.7143,
2818	          "accuracy": 0.7143,
2819	          "f1": 0.7143,
2820	          "peak_layer": 21
2821	        },
2822	        {
2823	          "balanced_accuracy": 0.7619,
2824	          "accuracy": 0.7619,
2825	          "f1": 0.7619,
2826	          "peak_layer": 19
2827	        },
2828	        {
2829	          "balanced_accuracy": 0.7083,
2830	          "accuracy": 0.7083,
2831	          "f1": 0.7083,
2832	          "peak_layer": 21
2833	        },
2834	        {
2835	          "balanced_accuracy": 0.7202,
2836	          "accuracy": 0.7202,
2837	          "f1": 0.7202,
2838	          "peak_layer": 14
2839	        },
2840	        {
2841	          "balanced_accuracy": 0.7619,
2842	          "accuracy": 0.7619,
2843	          "f1": 0.7619,
2844	          "peak_layer": 18
2845	        },
2846	        {
2847	          "balanced_accuracy": 0.6845,
2848	          "accuracy": 0.6845,
2849	          "f1": 0.6845,
2850	          "peak_layer": 22
2851	        }
2852	      ]
2853	    }
2854	  }
2855	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcfeee24-1d92-4743-bb7b-78bfd1f0a056",
  "isSidechain": true,
  "promptId": "7b01965c-4d4b-490d-8578-864ad14179c8",
  "agentId": "a9576db012ac53ecf",
  "type": "user",
  "uuid": "701f2503-fb8c-4352-a894-10b5bb2c2148",
  "sourceToolAssistantUUID": "bcfeee24-1d92-4743-bb7b-78bfd1f0a056",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-22T16:27:07.085Z_

Perfect! I found the bootstrap probe results files and have extracted the per-direction balanced accuracy means. Here are the exact numbers from the JSON files:

## LLAMA-3.1 Bootstrap Results (n=100 bootstrap samples)
File: `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/data/llama31_probe_results.json`

**Per-direction balanced accuracy means:**
- EN→EN: 0.771
- ZH→ZH: 0.7124
- EN→ZH: 0.6405
- ZH→EN: 0.7127

## Qwen-3 Bootstrap Results (n=100 bootstrap samples)
File: `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/data/qwen3_probe_results.json`

**Per-direction balanced accuracy means:**
- EN→EN: 0.7528
- ZH→ZH: 0.7162
- EN→ZH: 0.6496
- ZH→EN: 0.7215

**Note:** These files contain bootstrap mode results with n_bootstrap=100 (not n=2000 as initially requested). Both files are comprehensive probe result datasets that include 100 bootstrap samples per direction, with the summary statistics (means and standard deviations) computed across those samples.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "701f2503-fb8c-4352-a894-10b5bb2c2148",
  "isSidechain": true,
  "agentId": "a9576db012ac53ecf",
  "requestId": "req_011CbHvNjHXeSgqqDmSNjcL9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b70065b0-9ddc-4108-b85c-34b6303879c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CEZKGBRNVYLkqasHvA2ZG8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 60126,
      "cache_read_input_tokens": 35866,
      "output_tokens": 328,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 60126
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 328,
          "cache_read_input_tokens": 35866,
          "cache_creation_input_tokens": 60126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 60126,
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
