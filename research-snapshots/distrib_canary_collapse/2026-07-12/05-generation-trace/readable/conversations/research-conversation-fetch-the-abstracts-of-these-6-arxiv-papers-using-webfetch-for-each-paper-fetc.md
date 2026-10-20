# Research conversation: Fetch the abstracts of these 6 arXiv papers using WebFetch. For each paper, fetch the abstract page (https://arxiv.org/a

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-abf8146c3d9c749fd.jsonl`
- **Structured JSON:** [`03e6b96a9d8bf2412058.json`](../../sessions/03/03e6b96a9d8bf2412058.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

18 recorded events

### User

_source line 1 · 2026-05-20T15:01:21.478Z_

Fetch the abstracts of these 6 arXiv papers using WebFetch. For each paper, fetch the abstract page (https://arxiv.org/abs/XXXX.XXXXX) and extract: title, authors, abstract text, any mentioned baselines/methods, metrics, and datasets.

1. https://arxiv.org/abs/2510.05133 - "Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios"
2. https://arxiv.org/abs/2410.12341 - "Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI"
3. https://arxiv.org/abs/2601.03385 - "SIGMA: Scalable Spectral Insights for LLM Model Collapse"
4. https://arxiv.org/abs/2305.17493 - "The Curse of Recursion: Training on Generated Data Makes Models Forget" (Nature 2024) - note: this might also be at a different arxiv ID, use WebSearch if needed
5. https://arxiv.org/abs/1510.03055 - "A Diversity-Promoting Objective Function for Neural Conversation Models" (NAACL 2016)
6. https://arxiv.org/abs/2110.09348 - "Understanding Dimensional Collapse in Contrastive Self-supervised Learning" (ICLR 2022)

For each paper, report the full abstract and any baselines/metrics/datasets mentioned. Use WebSearch if any URL doesn't work to find the correct arXiv link.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "abf8146c3d9c749fd",
  "type": "user",
  "uuid": "c34bce8e-0282-408e-b173-d56b73cbf58f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T15:01:21.482Z_

```json
{
  "parentUuid": "c34bce8e-0282-408e-b173-d56b73cbf58f",
  "isSidechain": true,
  "agentId": "abf8146c3d9c749fd",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "6f751a25-8af2-4fbd-9292-3ec2d01bf850",
  "timestamp": "2026-05-20T15:01:21.482Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 3 · 2026-05-20T15:01:23.736Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0171C7CNMtHeQCRKDWT9Yy3W`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f751a25-8af2-4fbd-9292-3ec2d01bf850",
  "isSidechain": true,
  "agentId": "abf8146c3d9c749fd",
  "requestId": "req_011CbE2E1hSNuNKkovM6kkzm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06f9a747-5679-4399-a777-1376e038efb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019AsQPtJUcSRDCiFuSM4JFW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9172,
      "cache_read_input_tokens": 8155,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9172
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 80,
          "cache_read_input_tokens": 8155,
          "cache_creation_input_tokens": 9172,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9172,
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

_source line 4 · 2026-05-20T15:01:23.740Z_

<details><summary>↩ Tool result · `toolu_0171C7CNMtHeQCRKDWT9Yy3W`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06f9a747-5679-4399-a777-1376e038efb1",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "abf8146c3d9c749fd",
  "type": "user",
  "uuid": "f7d7b742-170b-457b-b28a-d068fe7881dd",
  "sourceToolAssistantUUID": "06f9a747-5679-4399-a777-1376e038efb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-20T15:01:25.960Z_

I'll fetch all 6 papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7d7b742-170b-457b-b28a-d068fe7881dd",
  "isSidechain": true,
  "agentId": "abf8146c3d9c749fd",
  "requestId": "req_011CbE2EBU4N1Xm3fdyPwFtj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ddf4f158-5a78-4582-914e-c47be28ac228",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015igDd6pL1KQEEpg7nY2PrQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 17327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

_source line 6 · 2026-05-20T15:01:27.387Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01F9JhqU8b6N5K1g59mnKR2V`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.05133",
  "prompt": "Extract the full title, authors, abstract text, and any mentioned baselines/methods, metrics, and datasets."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddf4f158-5a78-4582-914e-c47be28ac228",
  "isSidechain": true,
  "agentId": "abf8146c3d9c749fd",
  "requestId": "req_011CbE2EBU4N1Xm3fdyPwFtj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5eb88681-05e8-4741-984f-bdfd2177d643",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015igDd6pL1KQEEpg7nY2PrQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 17327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

_source line 7 · 2026-05-20T15:01:28.589Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NcoZJnZ5F9BdMWA47Sna9b`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.12341",
  "prompt": "Extract the full title, authors, abstract text, and any mentioned baselines/methods, metrics, and datasets."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5eb88681-05e8-4741-984f-bdfd2177d643",
  "isSidechain": true,
  "agentId": "abf8146c3d9c749fd",
  "requestId": "req_011CbE2EBU4N1Xm3fdyPwFtj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6084820-d834-4fcd-b25f-b7fb9a041c97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015igDd6pL1KQEEpg7nY2PrQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 17327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

_source line 8 · 2026-05-20T15:01:29.153Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CTkt87qCxEbv9zRMN5g6ry`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.03385",
  "prompt": "Extract the full title, authors, abstract text, and any mentioned baselines/methods, metrics, and datasets."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6084820-d834-4fcd-b25f-b7fb9a041c97",
  "isSidechain": true,
  "agentId": "abf8146c3d9c749fd",
  "requestId": "req_011CbE2EBU4N1Xm3fdyPwFtj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a763dbe-63a6-44ab-b9b4-cd2f2bc3fac3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015igDd6pL1KQEEpg7nY2PrQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 17327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

_source line 9 · 2026-05-20T15:01:30.640Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VYb8pd6qHcAZGSTNet9xFh`</summary>

```json
{
  "url": "https://arxiv.org/abs/2305.17493",
  "prompt": "Extract the full title, authors, abstract text, and any mentioned baselines/methods, metrics, and datasets."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a763dbe-63a6-44ab-b9b4-cd2f2bc3fac3",
  "isSidechain": true,
  "agentId": "abf8146c3d9c749fd",
  "requestId": "req_011CbE2EBU4N1Xm3fdyPwFtj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a5cd35a-ebad-4bb9-92ed-d0233bb4cb62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015igDd6pL1KQEEpg7nY2PrQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 17327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

_source line 10 · 2026-05-20T15:01:30.868Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M11WJZ7ikEun4vmyXKg3Ar`</summary>

```json
{
  "url": "https://arxiv.org/abs/1510.03055",
  "prompt": "Extract the full title, authors, abstract text, and any mentioned baselines/methods, metrics, and datasets."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a5cd35a-ebad-4bb9-92ed-d0233bb4cb62",
  "isSidechain": true,
  "agentId": "abf8146c3d9c749fd",
  "requestId": "req_011CbE2EBU4N1Xm3fdyPwFtj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7cd0b13-0b9d-41c0-baa4-aecc8b1fd852",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015igDd6pL1KQEEpg7nY2PrQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 17327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

_source line 11 · 2026-05-20T15:01:31.158Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Lvq1evS77tTE6t8eTpmhbJ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2110.09348",
  "prompt": "Extract the full title, authors, abstract text, and any mentioned baselines/methods, metrics, and datasets."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7cd0b13-0b9d-41c0-baa4-aecc8b1fd852",
  "isSidechain": true,
  "agentId": "abf8146c3d9c749fd",
  "requestId": "req_011CbE2EBU4N1Xm3fdyPwFtj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10fe78c3-3efc-42e0-a035-811c231c0b5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015igDd6pL1KQEEpg7nY2PrQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 17327,
      "output_tokens": 551,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1935
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 551,
          "cache_read_input_tokens": 17327,
          "cache_creation_input_tokens": 1935,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1935,
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

_source line 12 · 2026-05-20T15:01:32.230Z_

<details><summary>↩ Tool result · `toolu_01F9JhqU8b6N5K1g59mnKR2V`</summary>

```text
# Paper Summary

**Full Title:** "Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios"

**Authors:** Y. Du, G. Wu, G. Tang, W. Wang, Q. Fan

**Abstract:**
The research examines how synthetic data proportions influence model performance across different scales. Using the Pythia model suite (410M-12B parameters) on five tasks, researchers evaluated models trained with synthetic-to-external data ratios from 0-50% over 1-3 iterations. Key findings indicate that "models maintain stable performance with up to 20% synthetic data, but degradation accelerates beyond 30%." Larger models demonstrated greater robustness than smaller ones. The study notes that "calibration degradation precedes accuracy loss," serving as an early warning indicator. Reasoning tasks showed faster degradation than retrieval tasks. The research validates existing systems like STaR and Self-Instruct operating safely within identified parameters.

**Baselines/Methods:**
- Pythia model suite (410M-12B parameters)
- STaR and Self-Instruct systems
- Comparison with Shumailov et al.'s model collapse findings

**Metrics:**
- Model performance accuracy
- Calibration measures
- Output characteristics

**Datasets:**
Five diverse tasks (specific names not detailed in the abstract)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5eb88681-05e8-4741-984f-bdfd2177d643",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "abf8146c3d9c749fd",
  "type": "user",
  "uuid": "65331044-1fdc-444a-ac59-217296caab3f",
  "sourceToolAssistantUUID": "5eb88681-05e8-4741-984f-bdfd2177d643",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T15:01:33.219Z_

<details><summary>↩ Tool result · `toolu_01NcoZJnZ5F9BdMWA47Sna9b`</summary>

```text
# Paper Extraction Summary

**Title:** "Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI"

**Authors:** Daniele Gambetta, Gizem Gezici, Fosca Giannotti, Dino Pedreschi, Alistair Knott, Luca Pappalardo

**Abstract Summary:**
The paper addresses model collapse—"a progressive loss of performance and diversity across generations"—that occurs when generative AI models train on their own outputs. Rather than requiring distinction between human and AI-generated data, the authors introduce "surplexity" as a measure of surprise. They propose filtering training data by high surplexity to preserve model performance and diversity. The approach connects to the Free Energy Principle from cognitive science.

**Key Methods/Baselines Mentioned:**
- Proposed approach: surplexity-based filtering (no human/AI-generated distinction needed)
- Comparison baseline: human-data filtering methods

**Metrics:**
- Model collapse characterization via next-token probability distributions
- Distributional skewedness reduction

**Datasets:**
The abstract references "datasets and models" but does not specify particular dataset names.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6084820-d834-4fcd-b25f-b7fb9a041c97",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "abf8146c3d9c749fd",
  "type": "user",
  "uuid": "79cdec70-f37c-4219-ad22-02da5cb7821c",
  "sourceToolAssistantUUID": "c6084820-d834-4fcd-b25f-b7fb9a041c97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T15:01:33.924Z_

<details><summary>↩ Tool result · `toolu_01CTkt87qCxEbv9zRMN5g6ry`</summary>

```text
# Paper Summary

**Full Title:** SIGMA: Scalable Spectral Insights for LLM Model Collapse

**Authors:** Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue

**Abstract:**
The paper addresses "model collapse"—a degradation process occurring when recursive training on synthetic data causes "a contraction of distributional variance and representational quality." The authors introduce SIGMA, a framework using spectral analysis of embedding Gram matrices to quantify and predict collapse onset. The method derives deterministic and stochastic bounds on matrix spectra, enabling "scalable estimation of these bounds, making the framework applicable to large-scale foundation models." SIGMA aims to track representation space contraction and monitor recursive training pipeline health.

**Key Methods/Frameworks:**
- SIGMA (Spectral Inequalities for Gram Matrix Analysis)
- Spectral analysis via embedding Gram matrix bounds
- Deterministic and stochastic formulations for scalability

**Metrics:**
- Spectral bounds on embedding Gram matrices
- Representation space contraction measurements

**Datasets/Baselines:**
No specific datasets or baseline models are mentioned in the abstract or metadata provided.

**Paper Status:** Submitted January 6, 2026; last revised March 23, 2026 (Version 3)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a763dbe-63a6-44ab-b9b4-cd2f2bc3fac3",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "abf8146c3d9c749fd",
  "type": "user",
  "uuid": "462f9757-a31d-49a2-8a98-767a35f60c7f",
  "sourceToolAssistantUUID": "8a763dbe-63a6-44ab-b9b4-cd2f2bc3fac3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T15:01:34.504Z_

<details><summary>↩ Tool result · `toolu_01Lvq1evS77tTE6t8eTpmhbJ`</summary>

```text
# Paper Summary

**Full Title:** "Understanding Dimensional Collapse in Contrastive Self-supervised Learning"

**Authors:** Li Jing, Pascal Vincent, Yann LeCun, Yuandong Tian

**Abstract:**
The researchers investigate how embedding vectors in contrastive learning can suffer from "dimensional collapse," where representations span only a lower-dimensional subspace rather than utilizing the full embedding space. They reveal the underlying dynamics causing this phenomenon and propose DirectCLR, a novel method that "directly optimizes the representation space without relying on an explicit trainable projector." Their approach demonstrates improved performance compared to SimCLR with a linear projector when evaluated on ImageNet.

**Key Method:** DirectCLR

**Baseline/Comparison Method:** SimCLR (with trainable linear projector)

**Dataset:** ImageNet

**Publication:** ICLR 2022 (International Conference on Learning Representations)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10fe78c3-3efc-42e0-a035-811c231c0b5b",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "abf8146c3d9c749fd",
  "type": "user",
  "uuid": "4720816c-90bd-48a8-873c-a34b4ed8f995",
  "sourceToolAssistantUUID": "10fe78c3-3efc-42e0-a035-811c231c0b5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T15:01:34.697Z_

<details><summary>↩ Tool result · `toolu_01VYb8pd6qHcAZGSTNet9xFh`</summary>

```text
# Paper Summary

## Title
"The Curse of Recursion: Training on Generated Data Makes Models Forget"

## Authors
Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson

## Abstract
The paper investigates the consequences of training generative models on content they themselves have produced. The researchers demonstrate that "use of model-generated content in training causes irreversible defects in the resulting models, where tails of the original content distribution disappear." They introduce the concept of "Model Collapse" and show its occurrence across various architectures including Variational Autoencoders, Gaussian Mixture Models, and large language models. The authors argue this phenomenon is significant for the sustainability of web-based training data in an era where LLM-generated content becomes prevalent online.

## Baselines/Methods
- Variational Autoencoders (VAE)
- Gaussian Mixture Models (GMM)
- Large Language Models (LLMs)

## Metrics
The paper references loss of distribution tails and model degradation as key measures of Model Collapse, though specific metric names are not detailed in the abstract.

## Datasets
No specific datasets are mentioned in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a5cd35a-ebad-4bb9-92ed-d0233bb4cb62",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "abf8146c3d9c749fd",
  "type": "user",
  "uuid": "5d269b89-a1d9-4bae-910a-20e48d36a639",
  "sourceToolAssistantUUID": "0a5cd35a-ebad-4bb9-92ed-d0233bb4cb62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T15:01:35.110Z_

<details><summary>↩ Tool result · `toolu_01M11WJZ7ikEun4vmyXKg3Ar`</summary>

```text
# Paper Summary

**Full Title:** "A Diversity-Promoting Objective Function for Neural Conversation Models"

**Authors:** Jiwei Li, Michel Galley, Chris Brockett, Jianfeng Gao, Bill Dolan

**Abstract:** The paper addresses a fundamental limitation in sequence-to-sequence models for dialogue generation. The authors note that "Sequence-to-sequence neural network models for generation of conversational responses tend to generate safe, commonplace responses (e.g., 'I don't know') regardless of the input." They contend that standard maximum likelihood training is problematic for this task and propose using Maximum Mutual Information (MMI) as an alternative objective function instead.

**Key Contributions:**
- Proposed MMI objective function for neural conversation models
- The approach produced "more diverse, interesting, and appropriate responses"

**Evaluation Metrics & Results:**
- BLEU score improvements on two conversational datasets
- Human evaluation assessments

**Datasets:** Two conversational datasets (specific names not detailed in the abstract)

**Publication:** Proceedings of NAACL 2016

**Note:** The page does not explicitly list baseline methods or provide detailed dataset names in the visible content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7cd0b13-0b9d-41c0-baa4-aecc8b1fd852",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "abf8146c3d9c749fd",
  "type": "user",
  "uuid": "e0262099-3ff1-4ef2-b9b8-0cf0f335f85c",
  "sourceToolAssistantUUID": "a7cd0b13-0b9d-41c0-baa4-aecc8b1fd852",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-20T15:01:51.973Z_

All 6 fetches succeeded. Here are the results:

---

**Paper 1: 2510.05133**
Title: "Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios"
Authors: Y. Du, G. Wu, G. Tang, W. Wang, Q. Fan

Abstract: Examines how synthetic data proportions influence model performance across scales. Using the Pythia model suite (410M–12B parameters) on five tasks, models were trained with synthetic-to-external ratios from 0–50% over 1–3 iterations. Key findings: models maintain stable performance with up to 20% synthetic data, but degradation accelerates beyond 30%. Larger models are more robust. Calibration degradation precedes accuracy loss (early warning indicator). Reasoning tasks degrade faster than retrieval tasks. Validates STaR and Self-Instruct operating safely within identified parameters.

- Baselines/Methods: Pythia model suite, STaR, Self-Instruct, Shumailov et al.'s model collapse
- Metrics: accuracy, calibration measures
- Datasets: five diverse tasks (unspecified in abstract)

---

**Paper 2: 2410.12341**
Title: "Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI"
Authors: Daniele Gambetta, Gizem Gezici, Fosca Giannotti, Dino Pedreschi, Alistair Knott, Luca Pappalardo

Abstract: Addresses model collapse—a progressive loss of performance and diversity across generations when generative models train on their own outputs. Instead of requiring distinction between human and AI-generated data, the paper introduces "surplexity" (a surprise-based measure). Filtering training data by high surplexity preserves performance and diversity. Connects to the Free Energy Principle from cognitive science.

- Baselines/Methods: surplexity-based filtering vs. human-data filtering methods
- Metrics: next-token probability distributions, distributional skewedness
- Datasets: not specified in abstract

---

**Paper 3: 2601.03385**
Title: "SIGMA: Scalable Spectral Insights for LLM Model Collapse"
Authors: Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue
(Submitted Jan 6 2026; revised Mar 23 2026)

Abstract: Addresses model collapse as a degradation process from recursive synthetic-data training, causing "contraction of distributional variance and representational quality." Introduces SIGMA, a framework using spectral analysis of embedding Gram matrices to quantify and predict collapse onset. Derives deterministic and stochastic bounds on matrix spectra, enabling scalable estimation applicable to large-scale foundation models. Tracks representation space contraction and monitors recursive training pipeline health.

- Baselines/Methods: SIGMA (Spectral Inequalities for Gram Matrix Analysis)
- Metrics: spectral bounds on embedding Gram matrices, representation space contraction
- Datasets: not specified in abstract

---

**Paper 4: 2305.17493**
Title: "The Curse of Recursion: Training on Generated Data Makes Models Forget"
Authors: Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson

Abstract: Investigates consequences of training generative models on their own outputs. Demonstrates that model-generated content in training causes "irreversible defects in the resulting models, where tails of the original content distribution disappear." Introduces the concept of "Model Collapse" and shows its occurrence across VAEs, Gaussian Mixture Models, and LLMs. Argues this is significant for sustainability of web-based training data as LLM-generated content proliferates online.

- Baselines/Methods: Variational Autoencoders (VAE), Gaussian Mixture Models (GMM), LLMs
- Metrics: loss of distribution tails, model degradation
- Datasets: not specified in abstract

---

**Paper 5: 1510.03055**
Title: "A Diversity-Promoting Objective Function for Neural Conversation Models"
Authors: Jiwei Li, Michel Galley, Chris Brockett, Jianfeng Gao, Bill Dolan
(NAACL 2016)

Abstract: Addresses the tendency of seq2seq dialogue models to generate "safe, commonplace responses (e.g., 'I don't know') regardless of the input." Argues standard maximum likelihood training is problematic, and proposes Maximum Mutual Information (MMI) as an alternative objective. Produces more diverse, interesting, and appropriate responses.

- Baselines/Methods: seq2seq with MLE baseline vs. proposed MMI objective
- Metrics: BLEU score, human evaluation
- Datasets: two conversational datasets (unspecified in abstract)

---

**Paper 6: 2110.09348**
Title: "Understanding Dimensional Collapse in Contrastive Self-supervised Learning"
Authors: Li Jing, Pascal Vincent, Yann LeCun, Yuandong Tian
(ICLR 2022)

Abstract: Investigates how embedding vectors in contrastive learning suffer from "dimensional collapse"—representations spanning only a lower-dimensional subspace. Reveals underlying dynamics and proposes DirectCLR, which "directly optimizes the representation space without relying on an explicit trainable projector." Outperforms SimCLR with a linear projector on ImageNet.

- Baselines/Methods: SimCLR (linear projector)
- Metrics: ImageNet classification accuracy
- Datasets: ImageNet

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0262099-3ff1-4ef2-b9b8-0cf0f335f85c",
  "isSidechain": true,
  "agentId": "abf8146c3d9c749fd",
  "requestId": "req_011CbE2F1ucw6TJoDHDmpPPW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd5fe51a-3b24-4510-85fc-083e020267ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JCn856qpEAATe2KaQ9LyyG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 236,
      "cache_creation_input_tokens": 2132,
      "cache_read_input_tokens": 19262,
      "output_tokens": 1368,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2132
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 236,
          "output_tokens": 1368,
          "cache_read_input_tokens": 19262,
          "cache_creation_input_tokens": 2132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2132,
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
