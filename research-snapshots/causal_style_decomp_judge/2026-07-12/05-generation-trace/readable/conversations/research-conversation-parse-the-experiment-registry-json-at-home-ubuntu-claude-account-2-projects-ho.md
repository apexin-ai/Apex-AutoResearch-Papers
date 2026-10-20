# Research conversation: Parse the experiment registry JSON at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a5fd80952fb015e5f.jsonl`
- **Structured JSON:** [`7578df1f2ec1798c0b79.json`](../../sessions/75/7578df1f2ec1798c0b79.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

38 recorded events

### User

_source line 1 · 2026-05-25T19:42:52.875Z_

Parse the experiment registry JSON at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge/34b1c8fb-c53e-47b8-bef7-53d80c2bd748/tool-results/mcp-agent-ml-research-read_registry-1779738159356.txt

This file has schema: {result: string}. The "result" field is itself a JSON string that needs to be parsed.

I need ALL experiment entries with their metrics. For each experiment, extract:
- exp_id
- name/description
- status
- metrics (all of them - especially BT win probabilities, p-values, Cohen's d, GEE ORs, etc.)
- conclusion

Report ALL experiments and ALL their metrics verbatim. Do not summarize or skip any. This is for a data audit so completeness is critical.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8842f241-92c6-4951-b177-588e67a11a5d",
  "agentId": "a5fd80952fb015e5f",
  "type": "user",
  "uuid": "ee22dc35-2ec7-42ec-bfda-acec548d1339",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-25T19:42:52.879Z_

```json
{
  "parentUuid": "ee22dc35-2ec7-42ec-bfda-acec548d1339",
  "isSidechain": true,
  "agentId": "a5fd80952fb015e5f",
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
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
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
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "40f83e39-abba-4ab0-ba8b-80b46fe5f674",
  "timestamp": "2026-05-25T19:42:52.879Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-25T19:42:55.820Z_



I'll read the file first, then parse it thoroughly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40f83e39-abba-4ab0-ba8b-80b46fe5f674",
  "isSidechain": true,
  "agentId": "a5fd80952fb015e5f",
  "requestId": "req_011CbPrjj7kPgmnRMMgrtHbp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01fb5504-aa84-4e8b-913e-1e7e1adcdc2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GkNsrEXVTrEvNK4YdsWD2u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15227,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15227,
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

_source line 4 · 2026-05-25T19:42:56.748Z_

<details open><summary>🔧 Tool call — Read · `toolu_017Xj9DUkeNCkZyztdM9ZLV5`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge/34b1c8fb-c53e-47b8-bef7-53d80c2bd748/tool-results/mcp-agent-ml-research-read_registry-1779738159356.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01fb5504-aa84-4e8b-913e-1e7e1adcdc2f",
  "isSidechain": true,
  "agentId": "a5fd80952fb015e5f",
  "requestId": "req_011CbPrjj7kPgmnRMMgrtHbp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07210a94-95e5-4226-aaec-ecb5432da123",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GkNsrEXVTrEvNK4YdsWD2u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15227,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15227,
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

### Tool result

_source line 5 · 2026-05-25T19:42:57.044Z_

<details><summary>↩ Tool result · reported error · `toolu_017Xj9DUkeNCkZyztdM9ZLV5`</summary>

```text
File content (37750 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07210a94-95e5-4226-aaec-ecb5432da123",
  "isSidechain": true,
  "promptId": "8842f241-92c6-4951-b177-588e67a11a5d",
  "agentId": "a5fd80952fb015e5f",
  "type": "user",
  "uuid": "82bddc29-6ed7-4a93-ab5f-2f35651607ea",
  "toolUseResult": "Error: File content (37750 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "07210a94-95e5-4226-aaec-ecb5432da123",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-25T19:42:59.401Z_

The file is large. Let me read it in chunks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82bddc29-6ed7-4a93-ab5f-2f35651607ea",
  "isSidechain": true,
  "agentId": "a5fd80952fb015e5f",
  "requestId": "req_011CbPrk2yYLGpwTN25Cuv1x",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4bfe9adb-d713-4b04-8fa9-4a8bdf536697",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ueoc9FhkZnS2ectc1Cujbm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 15227,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1063,
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

_source line 7 · 2026-05-25T19:43:00.443Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QzDLBsvEsqpM6VSmfbMnVF`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge/34b1c8fb-c53e-47b8-bef7-53d80c2bd748/tool-results/mcp-agent-ml-research-read_registry-1779738159356.txt",
  "limit": 500,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bfe9adb-d713-4b04-8fa9-4a8bdf536697",
  "isSidechain": true,
  "agentId": "a5fd80952fb015e5f",
  "requestId": "req_011CbPrk2yYLGpwTN25Cuv1x",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "727de452-4d91-41b4-99b1-5adbbf331e7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ueoc9FhkZnS2ectc1Cujbm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 15227,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1063
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 15227,
          "cache_creation_input_tokens": 1063,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1063,
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

_source line 8 · 2026-05-25T19:43:00.720Z_

<details><summary>↩ Tool result · reported error · `toolu_01QzDLBsvEsqpM6VSmfbMnVF`</summary>

```text
File content (37750 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "727de452-4d91-41b4-99b1-5adbbf331e7f",
  "isSidechain": true,
  "promptId": "8842f241-92c6-4951-b177-588e67a11a5d",
  "agentId": "a5fd80952fb015e5f",
  "type": "user",
  "uuid": "a320bff3-9353-4d3a-a7c8-f9350626038e",
  "toolUseResult": "Error: File content (37750 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "727de452-4d91-41b4-99b1-5adbbf331e7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T19:43:08.592Z_

<details open><summary>🔧 Tool call — Read · `toolu_013DRgVGb4GkhjpQ8QNShkpD`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge/34b1c8fb-c53e-47b8-bef7-53d80c2bd748/tool-results/mcp-agent-ml-research-read_registry-1779738159356.txt",
  "limit": 200,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a320bff3-9353-4d3a-a7c8-f9350626038e",
  "isSidechain": true,
  "agentId": "a5fd80952fb015e5f",
  "requestId": "req_011CbPrkK2wAuNEqJxtR6YGV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7540f168-957e-4b83-a365-e5b1d2547829",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTViw8tRPxZMgEuVTtYbFV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 255,
      "cache_read_input_tokens": 16290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 255,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 10 · 2026-05-25T19:43:08.863Z_

<details><summary>↩ Tool result · reported error · `toolu_013DRgVGb4GkhjpQ8QNShkpD`</summary>

```text
File content (37750 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7540f168-957e-4b83-a365-e5b1d2547829",
  "isSidechain": true,
  "promptId": "8842f241-92c6-4951-b177-588e67a11a5d",
  "agentId": "a5fd80952fb015e5f",
  "type": "user",
  "uuid": "1f585f5b-4f39-4b41-ae96-690ba5e04d5a",
  "toolUseResult": "Error: File content (37750 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "7540f168-957e-4b83-a365-e5b1d2547829",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T19:43:12.594Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GGeEDr6Z1cGCrTi1yLS8U9`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge/34b1c8fb-c53e-47b8-bef7-53d80c2bd748/tool-results/mcp-agent-ml-research-read_registry-1779738159356.txt",
  "limit": 100,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f585f5b-4f39-4b41-ae96-690ba5e04d5a",
  "isSidechain": true,
  "agentId": "a5fd80952fb015e5f",
  "requestId": "req_011CbPrkuWMspmYPADyQy4o1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b208cd2-c4b6-4339-ba6b-bb74d4bf443e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01543ygEeS8TtmMZ1KPRJLWZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 242,
      "cache_read_input_tokens": 16545,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 242
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 16545,
          "cache_creation_input_tokens": 242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 242,
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

_source line 12 · 2026-05-25T19:43:12.893Z_

<details><summary>↩ Tool result · reported error · `toolu_01GGeEDr6Z1cGCrTi1yLS8U9`</summary>

```text
File content (37750 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b208cd2-c4b6-4339-ba6b-bb74d4bf443e",
  "isSidechain": true,
  "promptId": "8842f241-92c6-4951-b177-588e67a11a5d",
  "agentId": "a5fd80952fb015e5f",
  "type": "user",
  "uuid": "dbabaf63-0e12-4ad0-a0f8-a8cd65d5aaab",
  "toolUseResult": "Error: File content (37750 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "9b208cd2-c4b6-4339-ba6b-bb74d4bf443e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T19:43:15.914Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014aKyiA9GCH7sNdvdrnvdxq`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge/34b1c8fb-c53e-47b8-bef7-53d80c2bd748/tool-results/mcp-agent-ml-research-read_registry-1779738159356.txt",
  "description": "Count lines in the registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbabaf63-0e12-4ad0-a0f8-a8cd65d5aaab",
  "isSidechain": true,
  "agentId": "a5fd80952fb015e5f",
  "requestId": "req_011CbPrmCgUKkHU3TWMgAFks",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b9800cb-5c8a-425d-af69-44c70319d45c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qk8DuBHy13CuhN4CqHriAL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 242,
      "cache_read_input_tokens": 16787,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 242
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 16787,
          "cache_creation_input_tokens": 242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 242,
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

_source line 14 · 2026-05-25T19:43:16.078Z_

<details><summary>↩ Tool result · `toolu_014aKyiA9GCH7sNdvdrnvdxq`</summary>

```text
0 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge/34b1c8fb-c53e-47b8-bef7-53d80c2bd748/tool-results/mcp-agent-ml-research-read_registry-1779738159356.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b9800cb-5c8a-425d-af69-44c70319d45c",
  "isSidechain": true,
  "promptId": "8842f241-92c6-4951-b177-588e67a11a5d",
  "agentId": "a5fd80952fb015e5f",
  "type": "user",
  "uuid": "1c8d8e79-7804-4e58-a335-3feadd24ae7a",
  "sourceToolAssistantUUID": "3b9800cb-5c8a-425d-af69-44c70319d45c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-25T19:43:18.399Z_

It's a single-line file. Let me use bash to parse it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c8d8e79-7804-4e58-a335-3feadd24ae7a",
  "isSidechain": true,
  "agentId": "a5fd80952fb015e5f",
  "requestId": "req_011CbPrmSJmW95XoyLGgQV3E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c5cd911-92d3-4ba2-b19a-773cba143cc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FLhFTJVtGrtKqqPkYwBQh1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 281,
      "cache_read_input_tokens": 17029,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 281,
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

_source line 16 · 2026-05-25T19:43:19.523Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TikFbw754MyMaR89TQSqyJ`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge/34b1c8fb-c53e-47b8-bef7-53d80c2bd748/tool-results/mcp-agent-ml-research-read_registry-1779738159356.txt",
  "description": "Get file size in bytes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c5cd911-92d3-4ba2-b19a-773cba143cc0",
  "isSidechain": true,
  "agentId": "a5fd80952fb015e5f",
  "requestId": "req_011CbPrmSJmW95XoyLGgQV3E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7020d3b9-8106-4beb-a12d-f53abae71408",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FLhFTJVtGrtKqqPkYwBQh1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 281,
      "cache_read_input_tokens": 17029,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 281,
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

_source line 17 · 2026-05-25T19:43:19.587Z_

<details><summary>↩ Tool result · `toolu_01TikFbw754MyMaR89TQSqyJ`</summary>

```text
92131 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge/34b1c8fb-c53e-47b8-bef7-53d80c2bd748/tool-results/mcp-agent-ml-research-read_registry-1779738159356.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7020d3b9-8106-4beb-a12d-f53abae71408",
  "isSidechain": true,
  "promptId": "8842f241-92c6-4951-b177-588e67a11a5d",
  "agentId": "a5fd80952fb015e5f",
  "type": "user",
  "uuid": "854be5da-5e40-4452-b622-ed35fe476860",
  "sourceToolAssistantUUID": "7020d3b9-8106-4beb-a12d-f53abae71408",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-25T19:43:27.066Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01USXeNFu1xLrW3BQ2wQLuka`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge/34b1c8fb-c53e-47b8-bef7-53d80c2bd748/tool-results/mcp-agent-ml-research-read_registry-1779738159356.txt', 'r') as f:\n    raw = json.load(f)\n\n# The outer structure has a 'result' field that is itself a JSON string\nresult_str = raw['result']\nregistry = json.loads(result_str)\n\n# Show top-level keys\nprint('Top-level type:', type(registry))\nif isinstance(registry, dict):\n    print('Top-level keys:', list(registry.keys()))\n    # Check if experiments is a key\n    if 'experiments' in registry:\n        exps = registry['experiments']\n        print(f'Number of experiments: {len(exps)}')\n        # Print first experiment keys to understand structure\n        if exps:\n            first = exps[0] if isinstance(exps, list) else list(exps.values())[0]\n            print('First experiment keys:', list(first.keys()) if isinstance(first, dict) else type(first))\n    else:\n        for k, v in registry.items():\n            print(f'  {k}: type={type(v).__name__}, preview={str(v)[:200]}')\nelif isinstance(registry, list):\n    print(f'List length: {len(registry)}')\n    if registry:\n        print('First item keys:', list(registry[0].keys()) if isinstance(registry[0], dict) else type(registry[0]))\n\"\n",
  "description": "Parse the JSON structure and understand its schema"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "854be5da-5e40-4452-b622-ed35fe476860",
  "isSidechain": true,
  "agentId": "a5fd80952fb015e5f",
  "requestId": "req_011CbPrmheW1CpP7EUJEGmVy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73bd4855-ddd2-4b0c-a96d-f752ca0cf7b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018nEAfVjaVDYC8xFNWugaG5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 298,
      "cache_read_input_tokens": 17310,
      "output_tokens": 502,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 298
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 502,
          "cache_read_input_tokens": 17310,
          "cache_creation_input_tokens": 298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 298,
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

_source line 19 · 2026-05-25T19:43:27.171Z_

<details><summary>↩ Tool result · `toolu_01USXeNFu1xLrW3BQ2wQLuka`</summary>

```text
Top-level type: &lt;class 'dict'>
Top-level keys: ['success', 'data', 'error', 'metadata']
  success: type=bool, preview=True
  data: type=dict, preview={'experiments': {'llama70b_crossbench': {'status': 'DONE', 'retry_count': 0, 'created_at': '2026-05-24T08:17:29.390Z', 'updated_at': '2026-05-24T08:27:23.918Z', 'hypothesis': 'Llama-70B on AlpacaEval 
  error: type=NoneType, preview=None
  metadata: type=dict, preview={'elapsed_seconds': 0.466}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73bd4855-ddd2-4b0c-a96d-f752ca0cf7b1",
  "isSidechain": true,
  "promptId": "8842f241-92c6-4951-b177-588e67a11a5d",
  "agentId": "a5fd80952fb015e5f",
  "type": "user",
  "uuid": "7cb13fe7-b056-488e-bdfb-aa925b257dc6",
  "sourceToolAssistantUUID": "73bd4855-ddd2-4b0c-a96d-f752ca0cf7b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-25T19:43:31.408Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PSwVRPwAEhDjBvHTTJcnEx`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge/34b1c8fb-c53e-47b8-bef7-53d80c2bd748/tool-results/mcp-agent-ml-research-read_registry-1779738159356.txt', 'r') as f:\n    raw = json.load(f)\n\nresult_str = raw['result']\nregistry = json.loads(result_str)\nexperiments = registry['data']['experiments']\n\nprint(f'Total experiments: {len(experiments)}')\nprint('Experiment IDs:', list(experiments.keys()))\n\"\n",
  "description": "List all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cb13fe7-b056-488e-bdfb-aa925b257dc6",
  "isSidechain": true,
  "agentId": "a5fd80952fb015e5f",
  "requestId": "req_011CbPrnFkJ8LZhbzcm3zxmN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa33b4ac-ecd6-4c73-9e49-e6cafb91175e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NLkYvkuv3N2FgKmVg4imwm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 797,
      "cache_read_input_tokens": 17608,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 797
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 257,
          "cache_read_input_tokens": 17608,
          "cache_creation_input_tokens": 797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 797,
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

_source line 21 · 2026-05-25T19:43:31.515Z_

<details><summary>↩ Tool result · `toolu_01PSwVRPwAEhDjBvHTTJcnEx`</summary>

```text
Total experiments: 58
Experiment IDs: ['llama70b_crossbench', 'formality_llama_rewriter', 'formality_scaled_n300', 'verbosity_scaled_n355', 'register_100_cf', 'gemini_flash_fourth_judge', 'llama70b_register', 'llama70b_debiased', 'crossbench_alpacaeval_verbosity', 'llama70b_third_judge', 'finegrained_likert_100pt', 'gpt4o_rewriter_verbosity', 'gpt4o_rewriter_formality', 'debiased_verbosity_gpt4o', 'nli_threshold_sweep', 'bootstrap_attenuation', 'cf_vs_dr_gpt4o', 'double_rewrite_placebo_gpt4o', 'double_rewrite_placebo_qwen32b', 'cf_vs_dr_qwen32b', 'cross_axis_gradient', 'nli_gate_ablation', 'verbosity_7method_sensitivity', 'nli_gate_full_validation', 'originality_minimal_subset', 'bt_model_diagnostics', 'claude_tost_equivalence', 'nli_fn_selection_bias', 'nli_gate_spotcheck', 'gate_comparison', 'exp-006', 'alpacaeval_verbosity_qwen32b', 'correction_poc', 'claude_verbosity', 'claude_formality', 'gpt4o_alpacaeval', 'gpt4o_mtbench', 'qwen32b_register', 'gpt4o_register', 'gpt4o_verbosity', 'qwen32b_verbosity', 'qwen32b_formality', 'exp016_bradley_terry', 'verbosity_32b', 'exp-016', 'exp-015', 'exp015_clmm', 'exp013_nli_validation', 'exp-013', 'register_pilot', 'exp014_logistic_decomposition', 'exp012_consistency_bias', 'exp011_nli_sensitivity', 'exp010_binarized_likert', 'tone_pilot', 'pairwise_32b', 'mvp_32b_ate', 'mvp_8b_ate']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa33b4ac-ecd6-4c73-9e49-e6cafb91175e",
  "isSidechain": true,
  "promptId": "8842f241-92c6-4951-b177-588e67a11a5d",
  "agentId": "a5fd80952fb015e5f",
  "type": "user",
  "uuid": "8f456a2b-9ce4-42ae-a2d4-5ab0c67ea7f3",
  "sourceToolAssistantUUID": "aa33b4ac-ecd6-4c73-9e49-e6cafb91175e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-25T19:43:34.160Z_

58 experiments. Let me dump them all with full metrics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f456a2b-9ce4-42ae-a2d4-5ab0c67ea7f3",
  "isSidechain": true,
  "agentId": "a5fd80952fb015e5f",
  "requestId": "req_011CbPrnaKkXr6jjRusQsGgJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d15ab3e-9fb2-4be8-887a-d8f52a695701",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F3NSLtaQ8ecPqAQJriJqkp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 18405,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 853,
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

_source line 23 · 2026-05-25T19:43:38.331Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EgbDHboYQyVMkcVFAS68Ve`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge/34b1c8fb-c53e-47b8-bef7-53d80c2bd748/tool-results/mcp-agent-ml-research-read_registry-1779738159356.txt', 'r') as f:\n    raw = json.load(f)\n\nresult_str = raw['result']\nregistry = json.loads(result_str)\nexperiments = registry['data']['experiments']\n\n# Print each experiment fully\nfor i, (exp_id, exp) in enumerate(experiments.items()):\n    print(f\"{'='*80}\")\n    print(f\"EXPERIMENT {i+1}/{len(experiments)}: {exp_id}\")\n    print(f\"{'='*80}\")\n    for k, v in exp.items():\n        if k == 'metrics' and isinstance(v, dict):\n            print(f\"  metrics:\")\n            for mk, mv in v.items():\n                print(f\"    {mk}: {json.dumps(mv) if isinstance(mv, (dict, list)) else mv}\")\n        elif k == 'conclusion':\n            print(f\"  conclusion: {v}\")\n        elif isinstance(v, dict):\n            print(f\"  {k}:\")\n            for sk, sv in v.items():\n                print(f\"    {sk}: {json.dumps(sv) if isinstance(sv, (dict, list)) else sv}\")\n        else:\n            print(f\"  {k}: {v}\")\n    print()\nPYEOF\n",
  "description": "Dump all experiments with full details",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d15ab3e-9fb2-4be8-887a-d8f52a695701",
  "isSidechain": true,
  "agentId": "a5fd80952fb015e5f",
  "requestId": "req_011CbPrnaKkXr6jjRusQsGgJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e75087c5-25fe-4021-88f6-1643c7b30721",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F3NSLtaQ8ecPqAQJriJqkp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 18405,
      "output_tokens": 519,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 853
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 519,
          "cache_read_input_tokens": 18405,
          "cache_creation_input_tokens": 853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 853,
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

_source line 24 · 2026-05-25T19:43:38.464Z_

<details><summary>↩ Tool result · `toolu_01EgbDHboYQyVMkcVFAS68Ve`</summary>

```text
&lt;persisted-output>
Output too large (92.2KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge/34b1c8fb-c53e-47b8-bef7-53d80c2bd748/tool-results/b4l3pk2r8.txt

Preview (first 2KB):
================================================================================
EXPERIMENT 1/58: llama70b_crossbench
================================================================================
  status: DONE
  retry_count: 0
  created_at: 2026-05-24T08:17:29.390Z
  updated_at: 2026-05-24T08:27:23.918Z
  hypothesis: Llama-70B on AlpacaEval and MT-Bench cross-benchmark pairs will show stronger style bias than on LLMBar (consistent with other judges showing benchmark-dependent effect sizes), confirming style sensitivity generalizes across benchmarks. Effect-size gradient predicts Blindspot disappears at large effects (BT>80%).
  spec:
    command: python3 /root/causal_style_decomp_judge/analysis/llama70b_crossbench_scoring.py
    server: westb-29275
    data_path: /root/causal_style_decomp_judge/data/verified_{alpacaeval,alpacaeval_verbosity,mtbench}.jsonl
    data_count: 280
    model_name: Llama-3.3-70B-Instruct
    seed: 42
  checkpoint_path: /root/causal_style_decomp_judge/data/llama70b_crossbench_summary.json
  log_path: /tmp/llama70b_crossbench.log
  metrics:
    alpacaeval_formality: {"n": 47, "bt_pct": 95.7, "bt_ci": [89.4, 100], "bt_p": 1.6e-11, "likert_d": 0.211, "likert_wilcoxon_p": 0.0124, "gee_style_or": "degenerate", "gee_orig_or": "degenerate", "blindspot": false}
    alpacaeval_verbosity: {"n": 66, "bt_pct": 97, "bt_ci": [92.4, 100], "bt_p": 6e-17, "likert_d": 0.297, "likert_wilcoxon_p": 0.0002, "gee_style_or": 0.54, "gee_orig_or": 0.54, "blindspot": false}
    mtbench_formality: {"n": 36, "bt_pct": 91.7, "bt_ci": [80.6, 100], "bt_p": 2.3e-07, "likert_d": 0.234, "likert_wilcoxon_p": 0.0029, "gee_style_or": 32.68, "gee_orig_or": 0.89, "blindspot": false}
    mtbench_verbosity: MISSING_DATA
    comparison_llmbar_formality: {"bt_pct": 69.5, "blindspot": true}
    comparison_llmbar_verbosity: {"bt_pct": 73.5, "blindspot": true}
  conclusion: success
  completed_at: 2026-05-24T08:25:07.239Z

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e75087c5-25fe-4021-88f6-1643c7b30721",
  "isSidechain": true,
  "promptId": "8842f241-92c6-4951-b177-588e67a11a5d",
  "agentId": "a5fd80952fb015e5f",
  "type": "user",
  "uuid": "00afaa3e-3918-43f4-9f70-267f8277cc30",
  "sourceToolAssistantUUID": "e75087c5-25fe-4021-88f6-1643c7b30721",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-25T19:43:41.297Z_

The output is too large for the preview. Let me read it in chunks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00afaa3e-3918-43f4-9f70-267f8277cc30",
  "isSidechain": true,
  "agentId": "a5fd80952fb015e5f",
  "requestId": "req_011CbPro62gaN3eXa82Rqutz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9aed00f-102b-453b-bf10-f6fa0d476117",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NvM9QZqbFb4zjfbiJQyqnT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 19258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1420,
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

_source line 26 · 2026-05-25T19:43:42.010Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VGuoEK1n7fUKGu5WWCjQ8V`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge/34b1c8fb-c53e-47b8-bef7-53d80c2bd748/tool-results/b4l3pk2r8.txt",
  "limit": 300,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9aed00f-102b-453b-bf10-f6fa0d476117",
  "isSidechain": true,
  "agentId": "a5fd80952fb015e5f",
  "requestId": "req_011CbPro62gaN3eXa82Rqutz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0545884f-ce3b-4412-acff-e0db5f17f0f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NvM9QZqbFb4zjfbiJQyqnT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 19258,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1420
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 188,
          "cache_read_input_tokens": 19258,
          "cache_creation_input_tokens": 1420,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1420,
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

_source line 27 · 2026-05-25T19:43:42.017Z_

<details><summary>↩ Tool result · `toolu_01VGuoEK1n7fUKGu5WWCjQ8V`</summary>

```text
0	================================================================================
1	EXPERIMENT 1/58: llama70b_crossbench
2	================================================================================
3	  status: DONE
4	  retry_count: 0
5	  created_at: 2026-05-24T08:17:29.390Z
6	  updated_at: 2026-05-24T08:27:23.918Z
7	  hypothesis: Llama-70B on AlpacaEval and MT-Bench cross-benchmark pairs will show stronger style bias than on LLMBar (consistent with other judges showing benchmark-dependent effect sizes), confirming style sensitivity generalizes across benchmarks. Effect-size gradient predicts Blindspot disappears at large effects (BT>80%).
8	  spec:
9	    command: python3 /root/causal_style_decomp_judge/analysis/llama70b_crossbench_scoring.py
10	    server: westb-29275
11	    data_path: /root/causal_style_decomp_judge/data/verified_{alpacaeval,alpacaeval_verbosity,mtbench}.jsonl
12	    data_count: 280
13	    model_name: Llama-3.3-70B-Instruct
14	    seed: 42
15	  checkpoint_path: /root/causal_style_decomp_judge/data/llama70b_crossbench_summary.json
16	  log_path: /tmp/llama70b_crossbench.log
17	  metrics:
18	    alpacaeval_formality: {"n": 47, "bt_pct": 95.7, "bt_ci": [89.4, 100], "bt_p": 1.6e-11, "likert_d": 0.211, "likert_wilcoxon_p": 0.0124, "gee_style_or": "degenerate", "gee_orig_or": "degenerate", "blindspot": false}
19	    alpacaeval_verbosity: {"n": 66, "bt_pct": 97, "bt_ci": [92.4, 100], "bt_p": 6e-17, "likert_d": 0.297, "likert_wilcoxon_p": 0.0002, "gee_style_or": 0.54, "gee_orig_or": 0.54, "blindspot": false}
20	    mtbench_formality: {"n": 36, "bt_pct": 91.7, "bt_ci": [80.6, 100], "bt_p": 2.3e-07, "likert_d": 0.234, "likert_wilcoxon_p": 0.0029, "gee_style_or": 32.68, "gee_orig_or": 0.89, "blindspot": false}
21	    mtbench_verbosity: MISSING_DATA
22	    comparison_llmbar_formality: {"bt_pct": 69.5, "blindspot": true}
23	    comparison_llmbar_verbosity: {"bt_pct": 73.5, "blindspot": true}
24	  conclusion: success
25	  completed_at: 2026-05-24T08:25:07.239Z
26	
27	================================================================================
28	EXPERIMENT 2/58: formality_llama_rewriter
29	================================================================================
30	  status: DONE
31	  retry_count: 0
32	  created_at: 2026-05-24T06:22:32.105Z
33	  updated_at: 2026-05-24T07:40:40.018Z
34	  hypothesis: Qwen3-32B judge's formality bias is rewriter-independent: using Llama-3.3-70B-Instruct instead of Qwen3-32B as the RATE counterfactual rewriter will reproduce significant pairwise preference for formal style (BT p<0.05), confirming the bias originates in the judge, not the rewriter.
35	  spec:
36	    command: python analysis/analyze_llama_rewriter_formality.py
37	    server: westb-29275
38	    data_path: /root/causal_style_decomp_judge/data/
39	    data_count: 100
40	    model_name: Llama-3.3-70B-Instruct (rewriter) + Qwen3-32B (judge)
41	    seed: 42
42	  log_path: /root/causal_style_decomp_judge/data/llama_rewriter_formality_results.json
43	  checkpoint_path: N/A (analysis-only experiment)
44	  conclusion: success
45	  metrics:
46	    bt_p_formal: 0.711
47	    bt_ci: [0.643, 0.775]
48	    bt_p_value: 0.0001
49	    gee_style_or: 4.4403
50	    gee_style_p: 1.3e-05
51	    gee_orig_or: 5.7474
52	    likert_ate: 0.02
53	    likert_cohen_d: 0.013
54	    likert_wilcoxon_p: 0.687723
55	    blindspot: True
56	    nli_pass_rate: 0.79
57	    n_total: 100
58	    n_nli_pass: 79
59	    baseline_delta_pp: 4.6
60	    baseline_ci_overlap: True
61	  completed_at: 2026-05-24T07:40:40.018Z
62	
63	================================================================================
64	EXPERIMENT 3/58: formality_scaled_n300
65	================================================================================
66	  status: DONE
67	  retry_count: 0
68	  created_at: 2026-05-24T06:22:29.057Z
69	  updated_at: 2026-05-24T07:12:06.139Z
70	  hypothesis: Llama-70B scoring of the existing n=355 formality scaled data will replicate the formality Blindspot pattern seen with Qwen3-32B (BT ~67%, Likert NS), providing cross-judge validation at scale. GEE Style OR will show small-sample shrinkage similar to Qwen3 (4.20→2.15).
71	  spec:
72	    command: pairwise_scoring.py + judge_scoring.py + analyze_scaled_formality_llama70b.py
73	    server: westb-29275
74	    data_path: /root/causal_style_decomp_judge/data/verified_scaled_formality.jsonl
75	    data_count: 355
76	    model_name: Llama-3.3-70B-Instruct (judge)
77	    seed: 42
78	    checkpoint_path: /root/causal_style_decomp_judge/data/scored_scaled_formality_llama70b.jsonl
79	    log_path: /tmp/likert_llama70b.log
80	  conclusion: success
81	  completed_at: 2026-05-24T07:06:00.039Z
82	  metrics:
83	    judge: Llama-3.3-70B-Instruct
84	    axis: formality
85	    n: 355
86	    bt_p_formal: 0.725
87	    bt_ci: [0.691, 0.759]
88	    bt_p_value: 0.0001
89	    consistent_win_rate: 0.881
90	    n_consistent: 202
91	    likert_d: 0.048
92	    likert_wilcoxon_p: 0.026
93	    tie_rate: 0.715
94	    blindspot: False
95	    note: CORRECTED: Worker reported 88.1% which was consistent-pair win rate, not BT. Actual BT=72.5%. LLMBar subset (n=89): BT=74.4%, Likert NS (Blindspot YES). Non-LLMBar subset: BT=69.9%, Likert sig.
96	
97	================================================================================
98	EXPERIMENT 4/58: verbosity_scaled_n355
99	================================================================================
100	  status: DONE
101	  retry_count: 0
102	  created_at: 2026-05-23T09:57:40.068Z
103	  updated_at: 2026-05-23T12:57:27.131Z
104	  hypothesis: Verbosity Style OR at n=355 will shrink from n=86 estimates (8.21-13.10) to projected range 4-6.5 due to small-sample upward bias, mirroring the formality shrinkage pattern (4.20→2.15). Likert ATE will remain NS, confirming the Blindspot is robust to increased sample size for verbosity axis.
105	  spec:
106	    command: Phase 1: counterfactual_gen --axis verbosity (400 pairs) → Phase 2: content_verification → Phase 3: judge_scoring + pairwise_scoring (5 judges) → Phase 4: GEE decomposition
107	    server: westb-29275
108	    data_path: data/scaled_verbosity_input.jsonl
109	    data_count: 400
110	    model_name: Qwen3-32B (rewriter+judge), Llama-70B, GPT-4o, Gemini, Claude
111	    seed: 42
112	    gpu: 0,1 (Qwen3-32B), 2,3 (Llama-70B)
113	    checkpoint_path: data/scored_scaled_verbosity_*.jsonl + data/pairwise_results_scaled_verbosity_*.jsonl (10 files on server)
114	    log_path: artifacts/verbosity_n355_analysis.json
115	  metrics:
116	    n_samples: 330
117	    n_judges: 5
118	    qwen32b: {"bt_p_verbose": 0.733, "bt_ci": [0.696, 0.77], "sign_p": 0, "likert_d": 0.149, "likert_wilcoxon_p": 0.0006, "likert_ttest_p": 0.007, "gee_intercept_or": 3.83, "gee_orig_or": 0.52, "gee_orig_p": 0.001, "ntc": 0.881, "blindspot": false, "note": "Likert now significant at n=355"}
119	    llama70b: {"bt_p_verbose": 0.759, "bt_ci": [0.722, 0.793], "sign_p": 0, "likert_d": 0.16, "likert_wilcoxon_p": 0.0001, "likert_ttest_p": 0.004, "gee_intercept_or": 4.01, "gee_orig_or": 0.61, "gee_orig_p": 0.013, "ntc": 0.896, "blindspot": false, "note": "Likert now significant at n=355"}
120	    gpt54: {"bt_p_verbose": 0.59, "bt_ci": [0.544, 0.635], "sign_p": 0.0002, "likert_d": -0.026, "likert_wilcoxon_p": 0.813, "likert_ttest_p": 0.635, "gee_intercept_or": 1.06, "gee_orig_or": 1.96, "gee_orig_p": 0.0005, "ntc": 0.867, "blindspot": true, "note": "Originality-dominated, minimal style bias"}
121	    gemini: {"bt_p_verbose": 0.678, "bt_ci": [0.638, 0.717], "sign_p": 0, "likert_d": 0.087, "likert_wilcoxon_p": 0.021, "likert_ttest_p": 0.114, "gee_intercept_or": 2.52, "gee_orig_or": 0.69, "gee_orig_p": 0.046, "ntc": 0.876, "blindspot": true, "note": "Borderline Likert \u2014 Wilcoxon sig but t-test NS"}
122	    claude: {"bt_p_verbose": 0.608, "bt_ci": [0.567, 0.649], "sign_p": 1e-06, "likert_d": 0.032, "likert_wilcoxon_p": 0.317, "likert_ttest_p": 0.561, "gee_intercept_or": 1.22, "gee_orig_or": 1.69, "gee_orig_p": 0.002, "ntc": 0.938, "blindspot": true, "note": "Originality bias, minimal style bias"}
123	    gee_shrinkage: {"qwen_n86_style_or": 13.1, "qwen_n355_intercept_or": 3.83, "shrinkage_pct": 70.8, "llama_n86_style_or": 8.21, "llama_n355_intercept_or": 4.01, "shrinkage_pct_llama": 51.2}
124	  conclusion: success
125	  completed_at: 2026-05-23T12:57:27.131Z
126	
127	================================================================================
128	EXPERIMENT 5/58: register_100_cf
129	================================================================================
130	  status: DONE
131	  retry_count: 0
132	  created_at: 2026-05-21T01:13:19.928Z
133	  updated_at: 2026-05-22T00:34:04.155Z
134	  spec:
135	    command: counterfactual_gen.py --axis register + content_verification.py --axis register (NLI-only) + scoring (pending API)
136	    server: westb-29275
137	    data_path: /root/causal_style_decomp_judge/data/counterfactuals_register.jsonl
138	    data_count: 100
139	    model_name: Qwen3-32B (counterfactual) + DeBERTa-v3-large (NLI gate)
140	    seed: 42
141	    checkpoint_path: data/verified_register.jsonl
142	    log_path: logs/workers/worker_code_register_counterfactual_gen_100_20260521T004113.log
143	  hypothesis: Register axis (academic/conversational) produces detectable style bias in GPT-4o judge comparable to formality axis, with pairwise win rate >= 60% and p < 0.05, demonstrating axis-dependent bias generalizes beyond formality
144	  metrics:
145	    n_generated: 100
146	    cf_nli_mean: 0.941
147	    cf_bertscore_mean: 0.8589
148	    cf_nli_pass_rate: 0.94
149	    cf_gating: NLI-only (threshold 0.90)
150	    dr_nli_mean: 0.8208
151	    dr_bertscore_mean: 0.8477
152	    dr_pass_rate: 0.81
153	    output_file: data/verified_register.jsonl
154	    artifact_id: art_20260521_227674
155	    pipeline_status: verification DONE, scoring BLOCKED (API 402)
156	  conclusion: killed
157	  completed_at: 2026-05-22T00:34:04.155Z
158	
159	================================================================================
160	EXPERIMENT 6/58: gemini_flash_fourth_judge
161	================================================================================
162	  status: DONE
163	  retry_count: 0
164	  created_at: 2026-05-21T22:04:28.393Z
165	  updated_at: 2026-05-21T22:36:06.643Z
166	  hypothesis: Gemini Flash as a fourth judge will also exhibit style blindspot (BT-significant but Likert-NS) on formality and verbosity axes, consistent with GPT-4o, Qwen-32B, and Claude judges, confirming the blindspot is judge-universal rather than model-specific.
167	  spec:
168	    command: OPENROUTER_KEY=*** GEMINI_MODEL=google/gemini-2.5-flash python csd_pipeline/gemini_flash_scoring.py
169	    server: westb-29275
170	    data_path: /root/causal_style_decomp_judge/data/
171	    data_count: 174
172	    model_name: google/gemini-2.5-flash
173	    seed: 42
174	  checkpoint_path: /root/causal_style_decomp_judge/data/gemini_flash_fourth_judge.json
175	  log_path: /tmp/gemini_flash.log
176	  metrics:
177	    formality: {"bt_pct": 57.4, "bt_ci": [50, 64.2], "bt_p": 0.0306, "likert_ate": -0.239, "likert_d": -0.082, "likert_p": 0.3088, "gee_style_or": 1.64, "gee_style_ci": [0.91, 2.98], "gee_style_p": 0.1008, "gee_orig_or": 2.51, "gee_orig_ci": [1.39, 4.54], "gee_orig_p": 0.0024, "blindspot": true, "regime": "Orig-Dominated"}
178	    verbosity: {"bt_pct": 70.8, "bt_ci": [63.7, 77.2], "bt_p": 0, "likert_ate": 0.151, "likert_d": 0.051, "likert_p": 0.3697, "gee_style_or": 8.98, "gee_style_ci": [3.68, 21.94], "gee_style_p": 0, "gee_orig_or": 0.46, "gee_orig_ci": [0.2, 1.04], "gee_orig_p": 0.0614, "blindspot": true, "regime": "Pure Style"}
179	  conclusion: success
180	  completed_at: 2026-05-21T22:21:47.119Z
181	
182	================================================================================
183	EXPERIMENT 7/58: llama70b_register
184	================================================================================
185	  status: DONE
186	  retry_count: 0
187	  created_at: 2026-05-21T17:05:28.925Z
188	  updated_at: 2026-05-21T17:07:54.079Z
189	  hypothesis: Llama-70B register axis shows weak style bias (~55% BT, consistent with GPT-4o 57% and Qwen3-32B 55.3%), confirming register as originality-dominated across three independent judge architectures
190	  spec:
191	    command: python csd_pipeline/llama70b_register_scoring.py
192	    server: westb-29275
193	    data_path: data/verified_register.jsonl
194	    data_count: 94
195	    model_name: Llama-3.3-70B-Instruct
196	    seed: 42
197	    gpu: 2,3
198	    note: Pairwise + Likert scoring for register axis via vLLM port 8003
199	    checkpoint_path: data/llama70b_register_summary.json
200	    log_path: /tmp/llama70b_register.log
201	  conclusion: success
202	  completed_at: 2026-05-21T17:07:51.781Z
203	  metrics:
204	    bt_p_academic: 0.635
205	    bt_ci: [0.555, 0.712]
206	    bt_p_val: 0.0014
207	    likert_ate: 0.054
208	    likert_d: 0.024
209	    likert_ttest_p: 0.69
210	    likert_tie_rate: 0.688
211	    gee_style_or: 3.33
212	    gee_style_p: 0.0003
213	    gee_orig_or: 3.07
214	    gee_orig_p: 0.0008
215	    blindspot: True
216	    regime: Mixed
217	
218	================================================================================
219	EXPERIMENT 8/58: llama70b_debiased
220	================================================================================
221	  status: DONE
222	  retry_count: 0
223	  created_at: 2026-05-21T16:52:24.716Z
224	  updated_at: 2026-05-21T16:53:31.510Z
225	  hypothesis: Llama-70B correction resistance follows the same axis-dependent pattern as GPT-4o/Qwen3-32B: debiased prompts reduce but do not eliminate style bias, with verbosity more amenable to correction than formality, confirming bias persistence is model-independent
226	  spec:
227	    command: python csd_pipeline/llama70b_debiased.py
228	    server: westb-29275
229	    data_path: verified_32b.jsonl (88 formality) + verified_verbosity.jsonl (86 verbosity)
230	    data_count: 174 NLI-pass pairs total
231	    model_name: Llama-3.3-70B-Instruct
232	    seed: 42
233	    gpu: cuda:2,3 (vLLM port 8003)
234	    pid: 173017
235	    checkpoint_path: /root/causal_style_decomp_judge/data/debiased_llama70b_summary.json
236	    log_path: /root/causal_style_decomp_judge/logs/llama70b_debiased.log
237	  conclusion: success
238	  metrics:
239	    formality: {"baseline_bt": 69.5, "debiased_bt": 64.3, "debiased_ci": [57.3, 71], "debiased_p": 0.0001, "reduction_pp": -5.2, "reduction_pct": 26.7, "still_significant": true}
240	    verbosity: {"baseline_bt": 73.5, "debiased_bt": 66.9, "debiased_ci": [58.9, 74.4], "debiased_p": 0.0001, "reduction_pp": -6.6, "reduction_pct": 28.1, "still_significant": true}
241	    all_still_significant: True
242	  completed_at: 2026-05-21T16:53:31.510Z
243	
244	================================================================================
245	EXPERIMENT 9/58: crossbench_alpacaeval_verbosity
246	================================================================================
247	  status: DONE
248	  retry_count: 0
249	  created_at: 2026-05-21T16:52:26.420Z
250	  updated_at: 2026-05-21T16:52:40.971Z
251	  hypothesis: AlpacaEval verbosity bias is strong enough (BT ~84%) that even Likert detects it, confirming the effect-size gradient: Blindspot occurs at small-to-medium effects (d<0.15) but not at large effects (d>0.3)
252	  conclusion: success
253	  metrics:
254	    bt_p_verbose: 84.1
255	    bt_ci: [77.4, 90.2]
256	    bt_p: 0.0001
257	    likert_ate: 0.732
258	    likert_d: 0.407
259	    likert_p: 0.000414
260	    tie_rate: 0.244
261	    blindspot: False
262	    n_pairs: 82
263	  spec:
264	    command: alpacaeval_qwen32b_scoring.py (previously completed)
265	    server: westb-29275
266	    data_path: /root/causal_style_decomp_judge/data/verified_alpacaeval_verbosity.jsonl
267	    data_count: 82 NLI-pass pairs
268	    model_name: Qwen3-32B
269	    seed: 42
270	    checkpoint_path: /root/causal_style_decomp_judge/data/pairwise_results_alpacaeval_verbosity_qwen32b.jsonl
271	    log_path: N/A (pre-existing data)
272	  completed_at: 2026-05-21T16:52:40.971Z
273	
274	================================================================================
275	EXPERIMENT 10/58: llama70b_third_judge
276	================================================================================
277	  status: DONE
278	  retry_count: 0
279	  created_at: 2026-05-21T15:58:29.292Z
280	  updated_at: 2026-05-21T16:01:06.337Z
281	  hypothesis: Llama-3.3-70B as third independent judge architecture confirms the Likert Blindspot: BT pairwise detects style bias (formality + verbosity) with p<0.05 while Likert scoring shows no significant difference, replicating the pattern found with GPT-4o and Qwen3-32B judges
282	  plan_id: llama70b_third_judge
283	  spec:
284	    command: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/causal_style_decomp_judge && python csd_pipeline/llama70b_scoring.py
285	    server: westb-29275
286	    data_path: /root/causal_style_decomp_judge/data/verified_32b.jsonl + verified_verbosity.jsonl
287	    data_count: 88 formality + 86 verbosity NLI-pass pairs
288	    model_name: Llama-3.3-70B-Instruct
289	    seed: 42
290	    gpu: cuda:2,3
291	    vllm_port: 8003
292	    checkpoint_path: /root/causal_style_decomp_judge/data/llama70b_third_judge.json
293	    log_path: /root/causal_style_decomp_judge/logs/llama70b_scoring.log
294	  conclusion: success
295	  metrics:
296	    formality: {"bt_p_formal": 0.695, "bt_ci": [0.619, 0.765], "bt_p": 0.0001, "likert_ate": 0.023, "likert_p": 0.8458, "likert_d": 0.01, "likert_tie_rate": 0.727, "gee_style_or": 4.81, "gee_style_p": 0.0001, "gee_orig_or": 3.12, "gee_orig_p": 0.0007, "blindspot": true}
297	    verbosity: {"bt_p_verbose": 0.735, "bt_ci": [0.655, 0.809], "bt_p": 0.0001, "likert_ate": 0.047, "likert_p": 0.7524, "likert_d": 0.02, "likert_tie_rate": 0.616, "gee_style_or": 8.21, "gee_style_p": 0.0001, "gee_orig_or": 0.38, "gee_orig_p": 0.0196, "blindspot": true}
298	    blindspot_both_axes: True
299	    third_judge_confirms: True
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0545884f-ce3b-4412-acff-e0db5f17f0f5",
  "isSidechain": true,
  "promptId": "8842f241-92c6-4951-b177-588e67a11a5d",
  "agentId": "a5fd80952fb015e5f",
  "type": "user",
  "uuid": "2120d77a-fd1d-4083-ae04-649440426e12",
  "sourceToolAssistantUUID": "0545884f-ce3b-4412-acff-e0db5f17f0f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-25T19:43:47.511Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XLRLAET3AEPQTMVe5Tkb9Q`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge/34b1c8fb-c53e-47b8-bef7-53d80c2bd748/tool-results/b4l3pk2r8.txt",
  "limit": 300,
  "offset": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2120d77a-fd1d-4083-ae04-649440426e12",
  "isSidechain": true,
  "agentId": "a5fd80952fb015e5f",
  "requestId": "req_011CbProMRtJxvg32XdCQ5qK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6872d894-6631-4b36-bca1-127d726cd4dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfprDGjr8jqz2oNhmacXkf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7414,
      "cache_read_input_tokens": 20678,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7414
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 20678,
          "cache_creation_input_tokens": 7414,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7414,
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

_source line 29 · 2026-05-25T19:43:47.517Z_

<details><summary>↩ Tool result · `toolu_01XLRLAET3AEPQTMVe5Tkb9Q`</summary>

```text
300	    third_judge_confirms: True
301	  completed_at: 2026-05-21T16:01:06.337Z
302	
303	================================================================================
304	EXPERIMENT 11/58: finegrained_likert_100pt
305	================================================================================
306	  status: DONE
307	  retry_count: 0
308	  created_at: 2026-05-21T15:42:30.686Z
309	  updated_at: 2026-05-21T15:50:03.483Z
310	  hypothesis: The Likert Blindspot is NOT a scale granularity artifact: even a 100-point continuous scale (0-100) should fail to detect the style bias that pairwise BT detects, because the blindspot stems from absolute-vs-relative evaluation paradigm differences, not insufficient scale resolution
311	  spec:
312	    command: /root/miniconda3/bin/python csd_pipeline/finegrained_likert_100pt.py
313	    server: westb-29275
314	    data_path: data/verified_32b.jsonl + data/verified_verbosity.jsonl
315	    data_count: 88 formality + 86 verbosity NLI-pass pairs
316	    model_name: GPT-4o (via proxy)
317	    seed: 42
318	    checkpoint_path: data/finegrained_likert_100pt.json
319	    log_path: /tmp/finegrained_likert.log
320	    metrics: {"formality": {"n": 88, "ate": -0.625, "cohens_d": -0.0376, "t_p": 0.725, "wilcoxon_p": 0.9, "tie_rate": 0.659, "mean_style": 52.5, "mean_plain": 53.12, "blindspot": true}, "verbosity": {"n": 86, "ate": 2.849, "cohens_d": 0.1709, "t_p": 0.117, "wilcoxon_p": 0.067, "tie_rate": 0.512, "mean_style": 53.08, "mean_plain": 50.23, "blindspot": true}, "both_axes_blindspot": true, "conclusion": "100-point scale cannot detect style bias that BT detects \u2014 Blindspot is absolute-vs-relative paradigm difference, not granularity artifact"}
321	  conclusion: success
322	  completed_at: 2026-05-21T15:50:03.483Z
323	
324	================================================================================
325	EXPERIMENT 12/58: gpt4o_rewriter_verbosity
326	================================================================================
327	  status: DONE
328	  retry_count: 0
329	  created_at: 2026-05-21T09:11:53.204Z
330	  updated_at: 2026-05-21T15:40:01.391Z
331	  hypothesis: Verbosity style bias is rewriter-independent: GPT-4o rewriter + Qwen3-32B judge should produce BT probability statistically equivalent to Qwen3-32B rewriter + Qwen3-32B judge, confirming the measured verbosity bias reflects judge behavior not rewriter artifacts
332	  conclusion: success
333	  metrics:
334	    cf_generated: 100
335	    nli_pass: 81
336	    nli_rate: 0.81
337	    bt: {"p_verbose": 0.735, "ci": [0.654, 0.809], "p_value": 0.0001}
338	    likert: {"ate": 0, "p": 0.8384, "d": 0, "tie_rate": 0.469}
339	    gee: {"style_or": 10.17, "style_p": 0.0001, "orig_or": 1.61, "orig_p": 0.3143}
340	    blindspot: True
341	    vs_baseline: {"qwen32b_bt": 0.773, "delta_pp": -3.8, "ci_overlap": true, "note": "GPT-4o rewriter gives 73.5% vs Qwen3-32B rewriter 77.3%, CIs overlap \u2192 rewriter-independent"}
342	  spec:
343	    command: python gpt4o_rewriter_verbosity.py
344	    server: westb-29275
345	    data_path: data/verified_verbosity.jsonl + GPT-4o rewritten CFs
346	    data_count: 81
347	    model_name: GPT-4o (rewriter) + Qwen3-32B (judge)
348	    seed: 42
349	    checkpoint_path: N/A (API scoring)
350	    log_path: data/gpt4o_rewriter_verbosity_results.json
351	  completed_at: 2026-05-21T09:12:15.361Z
352	
353	================================================================================
354	EXPERIMENT 13/58: gpt4o_rewriter_formality
355	================================================================================
356	  status: DONE
357	  retry_count: 0
358	  created_at: 2026-05-21T10:46:15.195Z
359	  updated_at: 2026-05-21T15:39:14.228Z
360	  hypothesis: Style bias detected by RATE is rewriter-independent: switching from Qwen3-32B rewriter to GPT-4o rewriter should produce statistically equivalent BT probability for formality axis, proving the measured bias reflects judge behavior not rewriter artifacts
361	  spec:
362	    command: python csd_pipeline/gpt4o_rewriter_formality_scoring.py
363	    server: westb-29275
364	    data_path: data/mvp_samples.jsonl + GPT-4o rewritten CFs
365	    data_count: 90
366	    model_name: GPT-4o (rewriter) + Qwen3-32B (judge)
367	    seed: 42
368	    checkpoint_path: N/A (API scoring)
369	    log_path: data/gpt4o_rewriter_formality_results.json
370	  conclusion: success
371	  metrics:
372	    cf_generated: 100
373	    nli_pass: 90
374	    nli_rate: 0.9
375	    bt: {"p_formal": 0.644, "ci": [0.561, 0.728], "p_value": 0.0006, "n_pairs": 90, "n_comparisons": 180, "method": "ALL NLI-pass pairs (fixed from consistent-only bug)"}
376	    gee: {"style_or": 9.48, "style_p": 0.0001, "orig_or": 12.76, "orig_p": 0.0001, "note": "Fixed: was 24.47/39.27 with consistent-only filter (near-separation artifact)"}
377	    likert: {"ate": -0.189, "p": 0.1835, "d": -0.081, "tie_rate": 0.489, "mean_formal": 5.511, "mean_casual": 5.7}
378	    blindspot: True
379	    vs_baseline: {"qwen32b_bt": 0.665, "delta_pp": -2.1, "ci_overlap": true, "note": "GPT-4o rewriter 64.4% vs Qwen3-32B rewriter 66.5%, baseline falls within CI [56.1%, 72.8%] \u2192 rewriter-independent"}
380	    bug_fix: {"original_bt": 0.697, "original_gee_style_or": 24.47, "original_gee_orig_or": 39.27, "original_n_pairs": 66, "fix": "Used ALL 90 NLI-pass pairs for BT/GEE instead of consistent-only 66. \u00a73.3 requires all observations.", "fix_script": "csd_pipeline/fix_formality_rewriter_bt.py"}
381	  completed_at: 2026-05-21T10:46:56.474Z
382	
383	================================================================================
384	EXPERIMENT 14/58: debiased_verbosity_gpt4o
385	================================================================================
386	  status: DONE
387	  retry_count: 0
388	  created_at: 2026-05-21T15:36:47.030Z
389	  updated_at: 2026-05-21T15:37:07.076Z
390	  hypothesis: Debiased prompt intervention for verbosity axis on GPT-4o should show partial but insufficient bias reduction, consistent with formality results showing style bias is deeper than prompt-level — but verbosity may be more amenable to prompt-level correction than formality since the debiasing instruction can explicitly reference length/detail
391	  spec:
392	    command: /root/miniconda3/bin/python csd_pipeline/debiased_verbosity_gpt4o.py
393	    server: westb-29275
394	    data_path: data/verified_verbosity.jsonl
395	    data_count: 86 NLI-pass pairs
396	    model_name: GPT-4o (via proxy)
397	    seed: 42
398	    checkpoint_path: data/pairwise_results_debiased_gpt4o_verbosity.jsonl
399	    log_path: /tmp/debiased_verbosity.log
400	    metrics: {"original_p_verbose": "76.0% [69.7, 83.5], p=0.0001", "debiased_p_verbose": "62.9% [54.5, 70.9], p=0.0016", "reduction_pp": "-13.1pp (50.4% of bias eliminated)", "still_significant": true, "valid_pairs": 83, "consistent_pairs": 54, "n_comparisons": 167, "neither_count": "~5 pairs (3 retries each)"}
401	  conclusion: success
402	  completed_at: 2026-05-21T15:37:07.076Z
403	
404	================================================================================
405	EXPERIMENT 15/58: nli_threshold_sweep
406	================================================================================
407	  status: DONE
408	  retry_count: 0
409	  created_at: 2026-05-21T15:26:18.221Z
410	  updated_at: 2026-05-21T15:26:50.643Z
411	  hypothesis: BT-detected style bias is robust to NLI threshold choice: sweeping from 0.50 to 0.98 should show stable BT probability and consistent significance across all 4 axis×judge combinations, proving the finding is not an artifact of a specific threshold cutoff
412	  spec:
413	    command: /root/miniconda3/bin/python /tmp/nli_threshold_sweep.py /root/causal_style_decomp_judge
414	    server: westb-29275
415	    data_path: data/pairwise_results_{qwen32b_formality,32b,qwen32b_verbosity,gpt4o_verbosity}.jsonl
416	    data_count: 100 pairs × 4 combos
417	    model_name: CPU analysis (choix BT + bootstrap)
418	    seed: 42
419	    checkpoint_path: data/nli_threshold_sweep.json
420	    log_path: data/nli_threshold_sweep.json
421	    metrics: {"total_significant": "44/44 (100%)", "formality_qwen32b_bt_range": "0.648-0.665", "formality_gpt4o_bt_range": "0.614-0.642", "verbosity_qwen32b_bt_range": "0.765-0.773", "verbosity_gpt4o_bt_range": "0.752-0.769", "all_p_values": "\u22640.002", "max_bt_delta_across_thresholds": "~3pp"}
422	  conclusion: success
423	  completed_at: 2026-05-21T15:26:50.643Z
424	
425	================================================================================
426	EXPERIMENT 16/58: bootstrap_attenuation
427	================================================================================
428	  status: DONE
429	  retry_count: 0
430	  created_at: 2026-05-21T15:17:13.754Z
431	  updated_at: 2026-05-21T15:18:19.510Z
432	  hypothesis: Bootstrap subsampling of Likert data shows Cohen's d remains near zero across all sample sizes (n=50-355), demonstrating measurement attenuation rather than power gap — Likert fundamentally cannot detect style bias regardless of sample size
433	  conclusion: success
434	  spec:
435	    command: python /tmp/bootstrap_attenuation.py
436	    server: westb-29275
437	    data_path: data/scored_scaled_formality_qwen32b.jsonl + data/scored_qwen32b_verbosity.jsonl + data/scored_gpt4o_verbosity.jsonl
438	    data_count: 527
439	    model_name: Statistical analysis (numpy bootstrap)
440	    seed: 42
441	    checkpoint_path: data/bootstrap_attenuation.json
442	    log_path: data/bootstrap_attenuation.json
443	  completed_at: 2026-05-21T15:18:07.145Z
444	  metrics:
445	    formality_qwen32b: {"file": "scored_scaled_formality_qwen32b.jsonl", "n": 355, "full_d": -0.017, "curve": {"n50": {"d_median": -0.017, "ci": [-0.308, 0.262]}, "n100": {"d_median": -0.015, "ci": [-0.219, 0.176]}, "n150": {"d_median": -0.019, "ci": [-0.179, 0.145]}, "n200": {"d_median": -0.016, "ci": [-0.157, 0.119]}, "n250": {"d_median": -0.018, "ci": [-0.144, 0.107]}, "n300": {"d_median": -0.018, "ci": [-0.131, 0.095]}, "n355": {"d_median": -0.017, "ci": [-0.123, 0.087]}}, "interpretation": "SMOKING GUN: d_median flat at ~-0.017 across ALL n. CI narrows but always includes 0. Measurement attenuation confirmed."}
446	    verbosity_qwen32b: {"file": "scored_qwen32b_verbosity.jsonl", "n": 86, "full_d": 0.146, "curve": {"n30": {"d_median": 0.169, "ci": [-0.195, 0.595]}, "n50": {"d_median": 0.157, "ci": [-0.119, 0.494]}, "n70": {"d_median": 0.155, "ci": [-0.085, 0.443]}, "n86": {"d_median": 0.153, "ci": [-0.067, 0.416]}}, "interpretation": "d stable at ~0.15 (below small-effect threshold 0.2). CI always includes 0. Even at n=1000 would not detect."}
447	    verbosity_gpt4o: {"file": "scored_gpt4o_verbosity.jsonl", "n": 86, "full_d": 0.19, "curve": {"n30": {"d_median": 0.205, "ci": [-0.161, 0.618]}, "n50": {"d_median": 0.198, "ci": [-0.085, 0.53]}, "n70": {"d_median": 0.197, "ci": [-0.048, 0.472]}, "n86": {"d_median": 0.197, "ci": [-0.022, 0.446]}}, "interpretation": "d stable at ~0.19-0.20 (borderline small). CI includes 0 at all n. BT detects 76.0% (massive), Likert sees d=0.19 (trivial)."}
448	    formality_gpt4o: {"note": "Only 20 NLI-pass pairs available from scored_alpacaeval_gpt4o.jsonl. Single point: d_median=-0.20, CI=[-0.72, 0.24]. Insufficient for curve."}
449	    summary: 3/4 combinations computed. Formality×Qwen3-32B (n=355) is the definitive result: d≈0 flat across all subsample sizes = measurement attenuation, not power gap. BT detects 66.5% (p<0.0001) on same data where Likert d=-0.017.
450	
451	================================================================================
452	EXPERIMENT 17/58: cf_vs_dr_gpt4o
453	================================================================================
454	  status: DONE
455	  retry_count: 0
456	  created_at: 2026-05-21T13:37:04.042Z
457	  updated_at: 2026-05-21T15:01:43.024Z
458	  hypothesis: Comparing counterfactual (style-changed + artifact) vs double-rewrite (original-style + artifact) with GPT-4o judge isolates pure style effect by controlling for rewriting artifact. CF win rate significantly different from 50% proves style bias exists beyond rewriting artifact (MF1 critical defense).
459	  parent: double_rewrite_placebo_gpt4o
460	  spec:
461	    command: python csd_pipeline/cf_vs_dr_comparison_gpt4o.py
462	    server: westb-29275
463	    data_path: data/verified_32b.jsonl + data/verified_verbosity.jsonl
464	    data_count: 124
465	    model_name: GPT-4o (judge via API)
466	    seed: 42
467	    checkpoint_path: N/A - excluded from paper
468	    log_path: westb-29275:/root/csd_pipeline/data/cf_vs_dr_gpt4o.json
469	    checkpoint_source: double_rewrite_placebo_gpt4o
470	    eval_data: data/verified_32b.jsonl + data/verified_verbosity.jsonl
471	  conclusion: negative
472	  metrics:
473	    judge: GPT-4o
474	    comparison: counterfactual vs double_rewrite
475	    formality: {"n_pairs": 81, "n_consistent": 53, "consistency": 0.654, "cf_win_rate": 0.151, "ci": [0.057, 0.246], "p_value": 0, "interpretation": "DR strongly preferred over CF"}
476	    verbosity: {"note": "awaiting final result from worker, pattern matches Qwen3-32B"}
477	  completed_at: 2026-05-21T15:01:43.024Z
478	
479	================================================================================
480	EXPERIMENT 18/58: double_rewrite_placebo_gpt4o
481	================================================================================
482	  status: DONE
483	  retry_count: 0
484	  created_at: 2026-05-21T13:35:56.950Z
485	  updated_at: 2026-05-21T14:13:21.694Z
486	  hypothesis: Pairwise comparison of original vs double-rewrite (same style, only rewriting artifact difference) yields BT ≈ 50% with GPT-4o judge, proving pairwise format does not amplify rewriting artifacts (MF1 defense)
487	  spec:
488	    command: python csd_pipeline/double_rewrite_placebo.py (GPT-4o judge via API)
489	    server: westb-29275
490	    data_path: data/verified_32b.jsonl + data/verified_verbosity.jsonl
491	    data_count: 124
492	    model_name: GPT-4o (judge via API)
493	    seed: 42
494	    checkpoint_path: N/A
495	    log_path: data/double_rewrite_placebo_gpt4o.json
496	  conclusion: negative
497	  metrics:
498	    judge: GPT-4o
499	    comparison: original vs double_rewrite
500	    method: BT (choix.ilsr_pairwise) + pair-level bootstrap 10000 seed=42, ALL pairs including inconsistent
501	    formality: {"n_pairs": 81, "bt_p_original": 0.4177, "ci": [0.3418, 0.5], "p_value": 0.0368, "sign_test_rate": 0.3488, "sign_test_n": "15/43", "sign_test_p": 0.066, "note": "Sign test NS (p=0.066) but BT significant (p=0.037) \u2014 BT uses more data"}
502	    verbosity: {"n_pairs": 43, "bt_p_original": 0.1668, "ci": [0.0835, 0.262], "p_value": 0, "sign_test_rate": 0.0625, "sign_test_n": "2/32", "sign_test_p": 0}
503	    conclusion: Rewriting artifact confirmed. GPT-4o formality BT borderline (p=0.037), verbosity extreme. BT more powerful than sign test (recovers signal from inconsistent pairs).
504	  completed_at: 2026-05-21T13:36:30.437Z
505	
506	================================================================================
507	EXPERIMENT 19/58: double_rewrite_placebo_qwen32b
508	================================================================================
509	  status: DONE
510	  retry_count: 0
511	  created_at: 2026-05-21T13:32:17.445Z
512	  updated_at: 2026-05-21T14:13:20.472Z
513	  hypothesis: Pairwise comparison of original vs double-rewrite (same style, only rewriting artifact difference) yields BT ≈ 50%, proving pairwise format does not amplify rewriting artifacts (MF1 defense)
514	  spec:
515	    command: python csd_pipeline/double_rewrite_placebo.py (Qwen3-32B judge)
516	    server: westb-29275
517	    data_path: data/verified_32b.jsonl + data/verified_verbosity.jsonl
518	    data_count: 124
519	    model_name: Qwen3-32B (judge via vLLM)
520	    seed: 42
521	    checkpoint_path: N/A
522	    log_path: data/double_rewrite_placebo_qwen32b.json
523	  conclusion: negative
524	  metrics:
525	    judge: Qwen3-32B
526	    comparison: original vs double_rewrite
527	    method: BT (choix.ilsr_pairwise) + pair-level bootstrap 10000 seed=42, ALL pairs including inconsistent
528	    formality: {"n_pairs": 81, "bt_p_original": 0.3766, "ci": [0.3025, 0.4506], "p_value": 0.0006, "sign_test_rate": 0.2727, "sign_test_n": "12/44", "sign_test_p": 0.0037}
529	    verbosity: {"n_pairs": 43, "bt_p_original": 0.0816, "ci": [0.0351, 0.1397], "p_value": 0, "sign_test_rate": 0, "sign_test_n": "0/36", "sign_test_p": 0}
530	    conclusion: Rewriting artifact confirmed. Judges prefer DR over original, especially for verbosity. BT uses all pairs (matching main experiment methodology).
531	  completed_at: 2026-05-21T13:35:25.634Z
532	
533	================================================================================
534	EXPERIMENT 20/58: cf_vs_dr_qwen32b
535	================================================================================
536	  status: DONE
537	  retry_count: 0
538	  created_at: 2026-05-21T13:37:03.554Z
539	  updated_at: 2026-05-21T13:54:28.362Z
540	  hypothesis: Comparing counterfactual (style-changed + artifact) vs double-rewrite (original-style + artifact) isolates pure style effect by controlling for rewriting artifact. CF win rate significantly different from 50% proves style bias exists beyond rewriting artifact (MF1 critical defense).
541	  parent: double_rewrite_placebo_qwen32b
542	  spec:
543	    command: python csd_pipeline/cf_vs_dr_comparison.py (Qwen3-32B judge)
544	    server: westb-29275
545	    data_path: data/verified_32b.jsonl + data/verified_verbosity.jsonl
546	    data_count: 124
547	    model_name: Qwen3-32B (judge via vLLM)
548	    seed: 42
549	    checkpoint_path: N/A
550	    log_path: data/cf_vs_dr_qwen32b.json
551	    checkpoint_source: double_rewrite_placebo_qwen32b
552	    eval_data: data/verified_32b.jsonl + data/verified_verbosity.jsonl
553	  conclusion: negative
554	  metrics:
555	    judge: Qwen3-32B
556	    comparison: counterfactual vs double_rewrite
557	    formality: {"n_pairs": 81, "n_consistent": 55, "consistency": 0.679, "cf_win_rate": 0.2, "ci": [0.109, 0.309], "p_value": 9e-06, "interpretation": "DR preferred over CF \u2014 both style effect and extra artifact compound in DR's favor"}
558	    verbosity: {"n_pairs": 43, "n_consistent": 39, "consistency": 0.907, "cf_win_rate": 0.333, "ci": [0.18, 0.487], "p_value": 0.053, "interpretation": "DR marginally preferred (p=0.053) \u2014 artifact and style effects partially cancel in mixed-direction pairs"}
559	  completed_at: 2026-05-21T13:54:28.362Z
560	
561	================================================================================
562	EXPERIMENT 21/58: cross_axis_gradient
563	================================================================================
564	  status: DONE
565	  retry_count: 0
566	  created_at: 2026-05-21T13:30:37.151Z
567	  updated_at: 2026-05-21T13:31:22.748Z
568	  hypothesis: NLI rejection rate serves as manipulation invasiveness proxy, with axes ordered register < formality < verbosity matching the gradient in BT and GEE Style OR (qualitative argument)
569	  spec:
570	    command: python csd_pipeline/nli_ablation_cross_axis.py
571	    server: westb-29275
572	    data_path: data/verified_32b.jsonl + verified_verbosity.jsonl + verified_register.jsonl
573	    data_count: 300
574	    model_name: Descriptive statistics only
575	    seed: 42
576	    checkpoint_path: N/A
577	    log_path: data/cross_axis_gradient.json
578	  conclusion: success
579	  metrics:
580	    axes: [{"axis": "register", "nli_rejection_rate": 0.06, "bt": 0.553, "likert_d": 0.069, "gee_style_or": 1.91}, {"axis": "formality", "nli_rejection_rate": 0.12, "bt": 0.665, "likert_d": 0.012, "gee_style_or": 4.2}, {"axis": "verbosity", "nli_rejection_rate": 0.14, "bt": 0.773, "likert_d": -0.146, "gee_style_or": 13.1}]
581	    note: Qualitative gradient: register < formality < verbosity. Higher NLI rejection = more invasive manipulation = stronger detected bias.
582	  completed_at: 2026-05-21T13:31:22.748Z
583	
584	================================================================================
585	EXPERIMENT 22/58: nli_gate_ablation
586	================================================================================
587	  status: DONE
588	  retry_count: 0
589	  created_at: 2026-05-21T13:30:35.825Z
590	  updated_at: 2026-05-21T13:31:22.271Z
591	  hypothesis: NLI gate filters content-contaminated pairs without introducing systematic bias — NLI-pass BT ≈ all-pairs BT, and NLI-fail pairs show reversed or attenuated effects (bounding analysis)
592	  spec:
593	    command: python csd_pipeline/nli_ablation_cross_axis.py
594	    server: westb-29275
595	    data_path: data/pairwise_results_qwen32b_*.jsonl + data/verified_*.jsonl
596	    data_count: 200
597	    model_name: choix BT + bootstrap
598	    seed: 42
599	    checkpoint_path: N/A
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6872d894-6631-4b36-bca1-127d726cd4dd",
  "isSidechain": true,
  "promptId": "8842f241-92c6-4951-b177-588e67a11a5d",
  "agentId": "a5fd80952fb015e5f",
  "type": "user",
  "uuid": "bb620813-fed4-4ba7-aa46-b1b5d9dcdfa0",
  "sourceToolAssistantUUID": "6872d894-6631-4b36-bca1-127d726cd4dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-25T19:43:53.258Z_

<details open><summary>🔧 Tool call — Read · `toolu_013WepxKhjfZwD9HVfugNK67`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge/34b1c8fb-c53e-47b8-bef7-53d80c2bd748/tool-results/b4l3pk2r8.txt",
  "limit": 300,
  "offset": 600
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb620813-fed4-4ba7-aa46-b1b5d9dcdfa0",
  "isSidechain": true,
  "agentId": "a5fd80952fb015e5f",
  "requestId": "req_011CbProm2i2x8qs5BuX4fGg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7640fe99-4b2a-492b-91d6-cfcd0d51db8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTmfi9AgzQD7TnHiRE9mZN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7733,
      "cache_read_input_tokens": 28092,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7733
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 28092,
          "cache_creation_input_tokens": 7733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7733,
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

_source line 31 · 2026-05-25T19:43:53.276Z_

<details><summary>↩ Tool result · `toolu_013WepxKhjfZwD9HVfugNK67`</summary>

```text
600	    log_path: data/nli_gate_ablation.json
601	  conclusion: success
602	  metrics:
603	    formality: {"nli_pass": {"n": 88, "bt": 0.665, "ci": [0.585, 0.739], "p": 0.0001}, "nli_fail": {"n": 12, "bt": 0.417, "ci": [0.167, 0.666], "p": 0.69, "note": "REVERSED - no formal preference in contaminated pairs"}, "all": {"n": 100, "bt": 0.635, "ci": [0.56, 0.705], "p": 0.0001}}
604	    verbosity: {"nli_pass": {"n": 86, "bt": 0.773, "ci": [0.703, 0.843], "p": 0.0001}, "nli_fail": {"n": 14, "bt": 0.75, "ci": [0.536, 0.928], "p": 0.006, "note": "Still significant - verbosity bias persists even in NLI-fail"}, "all": {"n": 100, "bt": 0.77, "ci": [0.7, 0.835], "p": 0.0001}}
605	    interpretation: Formality: NLI gate correctly filters contaminated pairs (NLI-fail BT reverses to 41.7%). Verbosity: bias so strong it persists in NLI-fail (75.0%). All-pairs BT close to NLI-pass BT for both axes.
606	  completed_at: 2026-05-21T13:31:22.271Z
607	
608	================================================================================
609	EXPERIMENT 23/58: verbosity_7method_sensitivity
610	================================================================================
611	  status: DONE
612	  retry_count: 0
613	  created_at: 2026-05-21T13:09:57.524Z
614	  updated_at: 2026-05-21T13:10:23.178Z
615	  hypothesis: All 6 Likert-based statistical methods fail to detect verbosity bias (p>0.05) while Bradley-Terry detects it (77.3%, p<0.001), replicating the formality attenuation pattern on verbosity axis (addresses SF5)
616	  spec:
617	    command: python csd_pipeline/verbosity_7method_sensitivity.py
618	    server: westb-29275
619	    data_path: data/scored_qwen32b_verbosity.jsonl + data/pairwise_results_qwen32b_verbosity.jsonl
620	    data_count: 86
621	    model_name: Statistical analysis (scipy, statsmodels, choix)
622	    seed: 42
623	    checkpoint_path: N/A
624	    log_path: data/verbosity_7method_sensitivity.json
625	  conclusion: success
626	  metrics:
627	    n_pairs: 86
628	    axis: verbosity
629	    judge: Qwen3-32B
630	    benchmark: LLMBar
631	    methods: {"paired_ttest": {"t": 0.5163, "p": 0.607, "d": 0.056, "significant": false}, "mann_whitney": {"U": 3868, "p": 0.578, "r": -0.046, "significant": false}, "ordinal_logistic": {"coef": 0.1592, "p": 0.575, "OR": 1.173, "significant": false}, "cohens_d": {"d": 0.036, "threshold": 0.2, "significant": false}, "binarized_chi2": {"chi2": 1.5512, "p": 0.213, "OR": 2.162, "significant": false}, "likert_ate": {"ate": 0.0581, "p": 0.691, "d": 0.056, "ci": [-0.16, 0.27], "significant": false}, "bradley_terry": {"p_verbose": 0.7732, "p_value": 0.0001, "ci": [0.703, 0.843], "significant": true}}
632	    summary: 6/6 Likert methods NS, only BT detects. Replicates formality attenuation pattern.
633	  completed_at: 2026-05-21T13:10:23.178Z
634	
635	================================================================================
636	EXPERIMENT 24/58: nli_gate_full_validation
637	================================================================================
638	  status: DONE
639	  retry_count: 0
640	  created_at: 2026-05-21T12:16:02.325Z
641	  updated_at: 2026-05-21T12:16:36.565Z
642	  hypothesis: Full-coverage GPT-4o independent validation of NLI gate decisions across all 200 pairs confirms gate reliability, with high pass precision and conservative fail behavior (addresses W-MF1)
643	  spec:
644	    command: python csd_pipeline/nli_gate_full_validation.py
645	    server: westb-29275
646	    data_path: data/verified_32b.jsonl + data/verified_verbosity.jsonl
647	    data_count: 200
648	    model_name: GPT-4o (evaluator) + DeBERTa-v3-large (NLI gate)
649	    seed: 42
650	    checkpoint_path: N/A
651	    log_path: data/nli_gate_full_validation.json
652	  conclusion: success
653	  metrics:
654	    total_evaluated: 200
655	    per_axis: {"formality": {"n": 100, "agreement": 0.88, "kappa": 0.47, "base_rate_pass": 0.88, "pass_precision": 0.921, "fail_recall": 0.583}, "verbosity": {"n": 100, "agreement": 0.79, "kappa": 0.31, "base_rate_pass": 0.86, "pass_precision": 0.826, "fail_recall": 0.571}}
656	    overall: {"n": 200, "agreement": 0.835, "kappa": 0.38, "base_rate_pass": 0.87, "pass_precision": 0.874, "fail_recall": 0.577, "confusion": {"tp": 152, "fp": 22, "tn": 15, "fn": 11}}
657	    vs_spotcheck: {"spotcheck_agreement": 0.65, "full_agreement": 0.835, "delta_pp": 18.5, "note": "Spot-check used 50/50 stratified sampling (inflating disagreement); full data has 87% pass rate, pulling overall agreement up via high pass precision"}
658	    interpretation: NLI gate is reliable for pass decisions (precision 87-92%). Low fail recall (58%) means gate over-rejects — GPT-4o considers ~42% of NLI-fail pairs as actually preserving content. This confirms gate is CONSERVATIVE, consistent with NLI FN selection bias analysis.
659	  completed_at: 2026-05-21T12:16:36.566Z
660	
661	================================================================================
662	EXPERIMENT 25/58: originality_minimal_subset
663	================================================================================
664	  status: DONE
665	  retry_count: 0
666	  created_at: 2026-05-21T12:05:15.868Z
667	  updated_at: 2026-05-21T12:08:31.944Z
668	  hypothesis: Style effect in BT remains stable when restricting to originality-balanced pairs (Likert score tied between original and counterfactual), confirming style bias is not driven by originality confound (addresses W-MF3)
669	  spec:
670	    command: python csd_pipeline/originality_minimal_subset.py
671	    server: westb-29275
672	    data_path: data/pairwise_results_32b.jsonl + data/scored_32b.jsonl + verbosity equivalents
673	    data_count: 174
674	    model_name: choix BT + bootstrap
675	    seed: 42
676	    checkpoint_path: N/A
677	    log_path: data/originality_minimal_subset.json
678	  conclusion: success
679	  metrics:
680	    formality: {"full": {"n": 88, "bt": 0.6647, "ci": [0.585, 0.739]}, "likert_balanced": {"n": 55, "bt": 0.6727, "ci_note": "bootstrap CI from script", "method": "Pairs where Likert score(original) == Likert score(counterfactual)"}, "delta_likert_vs_full": 0.008, "delta_ci": [-0.1103, 0.1261], "conclusion": "BT stable on originality-balanced subset (\u0394=+0.008, CI includes 0)", "fix": "Corrected PAIRWISE_F from pairwise_results_32b.jsonl to pairwise_results_qwen32b_formality.jsonl"}
681	    verbosity: {"full": {"n": 86, "bt": 0.7732, "ci": [0.703, 0.843]}, "likert_balanced": {"n": 50, "bt": 0.7599, "method": "Pairs where Likert score(original) == Likert score(counterfactual)"}, "delta_likert_vs_full": -0.0133, "delta_ci": [-0.133, 0.1032], "conclusion": "BT stable on originality-balanced subset (\u0394=-0.013, CI includes 0)"}
682	    note: FIXED: formality now uses correct pairwise file (pairwise_results_qwen32b_formality.jsonl). Full BT matches canonical 0.665.
683	  completed_at: 2026-05-21T12:05:41.868Z
684	
685	================================================================================
686	EXPERIMENT 26/58: bt_model_diagnostics
687	================================================================================
688	  status: DONE
689	  retry_count: 0
690	  created_at: 2026-05-21T12:04:20.388Z
691	  updated_at: 2026-05-21T12:04:52.866Z
692	  hypothesis: BT model adequately fits the pairwise data (GoF non-significant) and stratified BT by originality direction reveals whether style effect is confounded with originality preference (addresses W-MF2)
693	  parent: qwen32b_formality
694	  spec:
695	    command: python csd_pipeline/bt_model_diagnostics.py
696	    server: westb-29275
697	    data_path: data/pairwise_results_32b.jsonl + data/pairwise_results_qwen32b_verbosity.jsonl
698	    data_count: 200
699	    model_name: choix BT + scipy chi2/Fisher
700	    seed: 42
701	    checkpoint_path: N/A
702	    log_path: data/bt_model_diagnostics.json
703	    checkpoint_source: qwen32b_formality + qwen32b_verbosity pairwise results
704	    eval_data: Consistent pairs from pairwise results (formality n=46, verbosity n=63)
705	  conclusion: success
706	  metrics:
707	    gof: {"formality": {"deviance": 52.8, "df": 45, "p_value": 0.198, "n_consistent": 46, "bt_prob": 0.739}, "verbosity": {"deviance": 47.96, "df": 62, "p_value": 0.905, "n_consistent": 63, "bt_prob": 0.873}}
708	    stratified_bt: {"formality": {"orig_is_formal": {"n": 27, "bt": 0.889, "ci": [0.778, 1], "wins": 24}, "orig_is_casual": {"n": 19, "bt": 0.526, "ci": [0.316, 0.737], "wins": 10}, "fisher_p": 0.015, "chi2_p": 0.006, "note": "Significant direction difference: orig_is_formal 88.9% vs orig_is_casual 52.6%. Confirms originality confound in formality (consistent with GEE decomposition)."}, "verbosity": {"orig_is_verbose": {"n": 29, "bt": 0.828, "ci": [0.69, 0.966], "wins": 24}, "orig_is_concise": {"n": 34, "bt": 0.912, "ci": [0.794, 1], "wins": 31}, "fisher_p": 0.453, "chi2_p": 0.317, "note": "No significant direction difference. Both directions strongly prefer verbose \u2192 pure style bias confirmed."}}
709	  completed_at: 2026-05-21T12:04:52.866Z
710	
711	================================================================================
712	EXPERIMENT 27/58: claude_tost_equivalence
713	================================================================================
714	  status: DONE
715	  retry_count: 0
716	  created_at: 2026-05-21T12:03:21.852Z
717	  updated_at: 2026-05-21T12:03:53.897Z
718	  hypothesis: Claude Sonnet 4 BT results are statistically equivalent to chance (P=0.5) within ±10pp margin using TOST, formally confirming no style bias as negative control (addresses W-SF4)
719	  spec:
720	    command: python csd_pipeline/claude_tost_equivalence.py
721	    server: westb-29275
722	    data_path: Claude BT bootstrap results
723	    data_count: 174
724	    model_name: Statistical analysis only (scipy)
725	    seed: 42
726	    checkpoint_path: N/A
727	    log_path: data/claude_tost_equivalence.json
728	  conclusion: negative
729	  metrics:
730	    equivalence_margin: 0.1
731	    formality: {"p_hat": 0.562, "n": 88, "se": 0.0375, "tost_p": 0.155, "ci_90": [0.5, 0.624], "upper_test_p": 0.155, "lower_test_p": 0, "equivalence_confirmed": false, "note": "90% CI upper bound 0.624 > 0.60 margin"}
732	    verbosity: {"p_hat": 0.541, "n": 86, "se": 0.0401, "tost_p": 0.07, "ci_90": [0.475, 0.607], "upper_test_p": 0.07, "lower_test_p": 0, "equivalence_confirmed": false, "note": "90% CI upper bound 0.607 > 0.60 margin, marginal"}
733	    conclusion: Equivalence NOT confirmed at Δ=0.10 — underpowered (n≈87), not evidence of bias. Both upper tests fail: formality p=0.155, verbosity p=0.070. If Δ=0.15, both would confirm equivalence.
734	    method: TOST for proportions (Lakens 2017), SE from pair-level bootstrap
735	  completed_at: 2026-05-21T12:03:53.897Z
736	
737	================================================================================
738	EXPERIMENT 28/58: nli_fn_selection_bias
739	================================================================================
740	  status: DONE
741	  retry_count: 0
742	  created_at: 2026-05-21T10:40:38.454Z
743	  updated_at: 2026-05-21T10:47:10.010Z
744	  hypothesis: NLI gate may systematically filter pairs with larger style changes, potentially underestimating the true bias effect — if so, reported effects are conservative lower bounds (addresses R3-W8)
745	  conclusion: success
746	  metrics:
747	    formality: {"n_total": 355, "n_pass": 323, "n_fail": 32, "pass_rate": 0.91, "significant_metrics": "2/7 (BLEU p=0.018 d=-0.46, TF-IDF p=0.002 d=-0.62)", "norm_lev_p": 0.23, "bleu_pass": 0.361, "bleu_fail": 0.235, "tfidf_pass": 0.69, "tfidf_fail": 0.558, "conclusion": "CONSERVATIVE: fail pairs have larger style changes (lower BLEU/TF-IDF)"}
748	    verbosity: {"n_total": 100, "n_pass": 39, "n_fail": 61, "pass_rate": 0.39, "significant_metrics": "5/7", "norm_lev_pass": 0.528, "norm_lev_fail": 0.69, "norm_lev_d": 0.788, "tfidf_pass": 0.675, "tfidf_fail": 0.491, "tfidf_d": -0.815, "conclusion": "STRONGLY CONSERVATIVE: 5/7 significant, TF-IDF d=-0.815 large effect"}
749	    register: {"n_total": 100, "n_pass": 80, "n_fail": 20, "pass_rate": 0.8, "significant_metrics": "0/7", "conclusion": "No significant bias detected (but n_fail=20 underpowered)"}
750	    overall_conclusion: Gate selection is conservative across all axes. Measured effects are lower bounds. Verbosity strongest signal (d=0.815 large).
751	    artifacts: ["artifacts/nli_fn_bias/nli_fn_bias_formality.png", "artifacts/nli_fn_bias/nli_fn_bias_verbosity.png", "artifacts/nli_fn_bias/nli_fn_bias_register.png"]
752	  spec:
753	    command: python nli_fn_selection_bias.py
754	    server: westb-29275
755	    data_path: data/ (formality + verbosity pipeline outputs)
756	    data_count: 455
757	    model_name: Analysis only (Levenshtein, Jaccard, Flesch)
758	    seed: 42
759	    checkpoint_path: N/A
760	    log_path: csd_pipeline/nli_fn_selection_bias.py output
761	  completed_at: 2026-05-21T10:41:09.789Z
762	
763	================================================================================
764	EXPERIMENT 29/58: nli_gate_spotcheck
765	================================================================================
766	  status: DONE
767	  retry_count: 0
768	  created_at: 2026-05-21T10:18:55.907Z
769	  updated_at: 2026-05-21T10:40:56.025Z
770	  hypothesis: GPT-4o independent evaluation agrees with NLI gate pass/fail decisions at high rate, demonstrating NLI gate validity is not an artifact of same-model-family evaluation (addresses R3-W1 concern about evaluator-producer confound in gate validation)
771	  conclusion: success
772	  metrics:
773	    total_samples: 100
774	    pass_samples: 50
775	    fail_samples: 50
776	    overall_agreement: 0.65
777	    cohens_kappa: 0.3
778	    kappa_ci: [0.153, 0.456]
779	    pass_agreement: 0.94
780	    fail_agreement: 0.36
781	    disagreement_pattern: {"nli_fail_gpt_pass": 32, "nli_pass_gpt_fail": 3}
782	    per_axis: {"formality": {"agreement": 0.771, "kappa": 0.241, "n": 48}, "verbosity": {"agreement": 0.618, "kappa": 0.294, "n": 34}, "register": {"agreement": 0.389, "kappa": 0.092, "n": 18}}
783	    note: NLI gate is conservative, not rubber-stamp. 94% pass agreement. 32/35 disagreements are NLI over-reject (fail but GPT-4o says pass). Kappa=0.30 inflated by 50/50 stratified sampling; real-data agreement much higher given 88% pass rate.
784	  spec:
785	    command: python nli_gate_gpt4o_spotcheck.py
786	    server: westb-29275
787	    data_path: data/ (formality+verbosity+register NLI outputs)
788	    data_count: 100
789	    model_name: GPT-4o (evaluator) + DeBERTa-v3-large (NLI)
790	    seed: 42
791	    checkpoint_path: N/A
792	    log_path: artifacts/reanalysis_outputs/nli_gate_gpt4o_spotcheck.json
793	  completed_at: 2026-05-21T10:39:23.633Z
794	
795	================================================================================
796	EXPERIMENT 30/58: gate_comparison
797	================================================================================
798	  status: DONE
799	  retry_count: 0
800	  created_at: 2026-05-21T10:38:32.232Z
801	  updated_at: 2026-05-21T10:39:32.612Z
802	  hypothesis: Direction-aware NLI gate does not introduce systematic bias compared to strict bidirectional gate — the extra ~21% pairs admitted by direction-aware gating have consistent BT direction with the strict-filtered subset (addresses R3-W2)
803	  conclusion: success
804	  metrics:
805	    formality: {"strict": {"n": 88, "bt": 0.6647, "ci": [0.5852, 0.7386], "p": 0.0001}, "direction_aware": {"n": 97, "bt": 0.634, "ci": [0.5567, 0.7061], "p": 0.0001}, "extra_only": {"n": 9, "bt": 0.3337}, "delta": -0.0307, "delta_ci": [-0.0651, -0.0018], "significant": true, "note": "Formality pipeline already uses strict gate (min). Extra 9 pairs lean casual. Moot for paper."}
806	    verbosity: {"strict": {"n": 65, "bt": 0.7845, "ci": [0.7076, 0.8537], "p": 0.0001}, "direction_aware": {"n": 86, "bt": 0.7732, "ci": [0.7034, 0.8429], "p": 0.0001}, "extra_only": {"n": 21, "bt": 0.7379}, "delta": -0.0113, "delta_ci": [-0.0564, 0.0296], "significant": false, "note": "No systematic difference. Extra 21 pairs consistent with overall direction (73.8% vs 77.3%)."}
807	  spec:
808	    command: python gate_comparison_bt.py
809	    server: westb-29275
810	    data_path: data/ (formality + verbosity NLI outputs)
811	    data_count: 200
812	    model_name: DeBERTa-v3-large (NLI) + choix (BT)
813	    seed: 42
814	    checkpoint_path: N/A
815	    log_path: csd_pipeline/gate_comparison_bt.py output
816	  completed_at: 2026-05-21T10:39:32.612Z
817	
818	================================================================================
819	EXPERIMENT 31/58: exp-006
820	================================================================================
821	  status: DONE
822	  retry_count: 0
823	  created_at: 2026-05-21T05:57:42.107Z
824	  updated_at: 2026-05-21T09:08:50.683Z
825	  metrics:
826	    n_total: 400
827	    nli_pass: 355
828	    nli_rate: 0.888
829	    bt: {"p_formal": 0.675, "ci": [0.637, 0.713], "ci_width_pp": 7.6, "p_value": 0.0001}
830	    likert: {"ate": -0.059, "p": 0.5999, "d": -0.025, "tie_rate": 0.434, "mean_formal": 6.58, "mean_casual": 6.64}
831	    gee: {"style_or": 2.15, "style_ci": [1.46, 3.16], "style_p": 0.0001, "orig_or": 4.99, "orig_ci": [3.4, 7.34], "orig_p": 0.0001}
832	    blindspot: True
833	    consistency: 0.654
834	    vs_n100: {"bt_delta": "+1.0pp (67.5 vs 66.5)", "ci_improvement": "2x narrower (7.6pp vs 15.4pp)"}
835	  hypothesis: Scaling formality counterfactual generation from 100 to 400 pairs enables cross-benchmark validation (AlpacaEval/MT-Bench) and increases statistical power for detecting smaller effect sizes
836	  spec:
837	    command: counterfactual_gen.py --axis formality --n 400 via vLLM Qwen3-32B tp=1 port 8002
838	    server: westb-29275
839	    data_path: /root/causal_style_decomp_judge/data/scaled_formality_input.jsonl
840	    data_count: 400
841	    model_name: Qwen3-32B (counterfactual generator via vLLM)
842	    seed: 42
843	    checkpoint_path: /root/causal_style_decomp_judge/data/counterfactuals_scaled_formality.jsonl
844	    log_path: /root/causal_style_decomp_judge/logs/
845	  conclusion: success
846	  completed_at: 2026-05-21T07:45:18.441Z
847	
848	================================================================================
849	EXPERIMENT 32/58: alpacaeval_verbosity_qwen32b
850	================================================================================
851	  status: DONE
852	  retry_count: 0
853	  created_at: 2026-05-21T09:02:00.454Z
854	  updated_at: 2026-05-21T09:02:30.481Z
855	  hypothesis: Qwen3-32B shows verbosity Blindspot on AlpacaEval benchmark (pairwise detects verbosity bias that Likert misses), extending verbosity findings to a second benchmark
856	  metrics:
857	    bt: {"p_verbose": 0.841, "ci": [0.774, 0.902], "p_value": 0.0001}
858	    likert: {"ate": 0.732, "p": 0.0003, "d": 0.375, "tie_rate": 0.244, "mean_verbose": 7.32, "mean_concise": 6.59}
859	    gee: {"style_or": 28.64, "style_ci": [9.16, 89.56], "style_p": 0.0001, "orig_or": 0.18, "orig_ci": [0.06, 0.54], "orig_p": 0.0024}
860	    blindspot: False
861	    n_pairs: 82
862	    consistency: 0.829
863	    note: NOT Blindspot: Likert p=0.0003 also significant. Effect is so strong (d=0.375) that even Likert detects it. GEE Style OR=28.64 is massive.
864	  conclusion: success
865	  spec:
866	    command: python alpacaeval_qwen32b_scoring.py --axis verbosity
867	    server: westb-29275
868	    data_path: data/counterfactuals_alpacaeval_verbosity.jsonl
869	    data_count: 82
870	    model_name: Qwen3-32B
871	    seed: 42
872	    checkpoint_path: N/A (API scoring via local vLLM)
873	    log_path: data/alpacaeval_verbosity_qwen32b_results.json
874	  completed_at: 2026-05-21T09:02:30.481Z
875	
876	================================================================================
877	EXPERIMENT 33/58: correction_poc
878	================================================================================
879	  status: DONE
880	  retry_count: 0
881	  created_at: 2026-05-21T09:00:50.949Z
882	  updated_at: 2026-05-21T09:01:23.388Z
883	  hypothesis: Explicit style-awareness debiasing instructions in judge prompts can eliminate or substantially reduce formality style bias, providing a simple correction mechanism (C4 claim test)
884	  spec:
885	    command: python correction_poc.py
886	    server: westb-29275
887	    data_path: data/verified_formality.jsonl
888	    data_count: 88
889	    model_name: Qwen3-32B + GPT-4o
890	    seed: 42
891	    checkpoint_path: N/A (API scoring)
892	    log_path: data/pairwise_results_debiased_qwen32b_formality.jsonl + data/pairwise_results_debiased_gpt4o_formality.jsonl
893	  conclusion: negative
894	  metrics:
895	    qwen32b: {"original": {"p_formal": 0.665, "ci": [0.585, 0.739], "p_value": 0.0001}, "debiased": {"p_formal": 0.608, "ci": [0.534, 0.682], "p_value": 0.0023}, "reduction_pp": 5.7, "reduction_pct": 34.5}
896	    gpt4o: {"original": {"p_formal": 0.63, "ci": [0.557, 0.703], "p_value": 0.0004}, "debiased": {"p_formal": 0.626, "ci": [0.559, 0.693], "p_value": 0.0001}, "reduction_pp": 0.4, "reduction_pct": 3.1, "neither_count": 5}
897	    conclusion: Debiased prompt ineffective. Qwen3-32B: -5.7pp but still p=0.002. GPT-4o: -0.4pp, no change. Style bias persists despite explicit debiasing instructions.
898	  completed_at: 2026-05-21T09:01:23.388Z
899	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7640fe99-4b2a-492b-91d6-cfcd0d51db8a",
  "isSidechain": true,
  "promptId": "8842f241-92c6-4951-b177-588e67a11a5d",
  "agentId": "a5fd80952fb015e5f",
  "type": "user",
  "uuid": "7457ba62-d284-4642-b9e8-1eb321cb92ed",
  "sourceToolAssistantUUID": "7640fe99-4b2a-492b-91d6-cfcd0d51db8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-25T19:43:58.591Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DE34RLMEcaUPwitSTL9UE7`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge/34b1c8fb-c53e-47b8-bef7-53d80c2bd748/tool-results/b4l3pk2r8.txt",
  "limit": 300,
  "offset": 900
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7457ba62-d284-4642-b9e8-1eb321cb92ed",
  "isSidechain": true,
  "agentId": "a5fd80952fb015e5f",
  "requestId": "req_011CbPrpBbpfZHFK4KwxjyS7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37d7828d-b594-4ff3-9db9-e32e8eae7eb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GGTLQDnDL2vKnGRhcMxmZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8174,
      "cache_read_input_tokens": 35825,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8174,
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

_source line 33 · 2026-05-25T19:43:58.598Z_

<details><summary>↩ Tool result · `toolu_01DE34RLMEcaUPwitSTL9UE7`</summary>

```text
900	================================================================================
901	EXPERIMENT 34/58: claude_verbosity
902	================================================================================
903	  status: DONE
904	  retry_count: 0
905	  created_at: 2026-05-21T08:47:10.568Z
906	  updated_at: 2026-05-21T08:58:22.005Z
907	  hypothesis: Claude Sonnet 4 shows verbosity style bias similar to GPT-4o (OR=10-13) and Qwen3-32B, confirming verbosity bias is model-independent
908	  conclusion: negative
909	  metrics:
910	    bt: {"p_verbose": 0.541, "ci": [0.459, 0.616], "p_value": 0.284}
911	    likert: {"ate": -0.081, "p": 0.7427, "d": -0.039, "tie_rate": 0.674}
912	    gee: {"style_or": 1.52, "style_p": 0.2858, "orig_or": 0.8, "orig_p": 0.5626}
913	    blindspot: False
914	    n_pairs: 86
915	  spec:
916	    command: python claude_judge_scoring.py --axis verbosity
917	    server: westb-29275
918	    data_path: data/verified_verbosity.jsonl
919	    data_count: 86
920	    model_name: claude-sonnet-4-20250514
921	    seed: 42
922	    checkpoint_path: N/A (API scoring)
923	    log_path: data/claude_verbosity_results.json
924	  completed_at: 2026-05-21T08:58:22.005Z
925	
926	================================================================================
927	EXPERIMENT 35/58: claude_formality
928	================================================================================
929	  status: DONE
930	  retry_count: 0
931	  created_at: 2026-05-21T08:47:10.069Z
932	  updated_at: 2026-05-21T08:58:20.986Z
933	  hypothesis: Claude Sonnet 4 shows similar formality style bias as GPT-4o and Qwen3-32B, with pairwise detecting bias that Likert misses, confirming Blindspot is cross-model
934	  conclusion: negative
935	  metrics:
936	    bt: {"p_formal": 0.562, "ci": [0.489, 0.636], "p_value": 0.0912}
937	    likert: {"ate": -0.045, "p": 0.7207, "d": -0.021, "tie_rate": 0.682}
938	    gee: {"style_or": 1.47, "style_p": 0.2757, "orig_or": 6.66, "orig_p": 0.0001}
939	    blindspot: False
940	    n_pairs: 88
941	  spec:
942	    command: python claude_judge_scoring.py --axis formality
943	    server: westb-29275
944	    data_path: data/verified_formality.jsonl
945	    data_count: 88
946	    model_name: claude-sonnet-4-20250514
947	    seed: 42
948	    checkpoint_path: N/A (API scoring)
949	    log_path: data/claude_formality_results.json
950	  completed_at: 2026-05-21T08:58:20.986Z
951	
952	================================================================================
953	EXPERIMENT 36/58: gpt4o_alpacaeval
954	================================================================================
955	  status: DONE
956	  retry_count: 0
957	  created_at: 2026-05-21T08:47:11.684Z
958	  updated_at: 2026-05-21T08:58:20.046Z
959	  hypothesis: GPT-4o shows formality Blindspot on AlpacaEval benchmark (pairwise detects bias, Likert misses it), confirming cross-benchmark generalizability
960	  metrics:
961	    bt: {"p_formal": 0.727, "ci": [0.663, 0.785], "p_value": 0.0001}
962	    likert: {"ate": 0.128, "p": 0.1704, "d": 0.148, "tie_rate": 0.663}
963	    gee: {"style_or": 4.91, "style_p": 0.0001, "orig_or": 1.99, "orig_p": 0.0356}
964	    blindspot: True
965	    n_pairs: 86
966	  conclusion: success
967	  spec:
968	    command: python gpt4o_crossbenchmark_scoring.py --benchmark alpacaeval
969	    server: westb-29275
970	    data_path: data/counterfactuals_alpacaeval_formality.jsonl
971	    data_count: 86
972	    model_name: gpt-4o
973	    seed: 42
974	    checkpoint_path: N/A (API scoring)
975	    log_path: data/gpt4o_alpacaeval_formality_results.json
976	  completed_at: 2026-05-21T08:58:20.046Z
977	
978	================================================================================
979	EXPERIMENT 37/58: gpt4o_mtbench
980	================================================================================
981	  status: DONE
982	  retry_count: 0
983	  created_at: 2026-05-21T08:47:12.182Z
984	  updated_at: 2026-05-21T08:58:18.609Z
985	  hypothesis: GPT-4o shows formality Blindspot on MT-Bench benchmark, confirming cross-benchmark generalizability beyond LLMBar and AlpacaEval
986	  metrics:
987	    bt: {"p_formal": 0.692, "ci": [0.623, 0.753], "p_value": 0.0001}
988	    likert: {"ate": 0.164, "p": 0.0163, "d": 0.167, "tie_rate": 0.699}
989	    gee: {"style_or": 2.28, "style_p": 0.1055, "orig_or": 6.24, "orig_p": 0.0005}
990	    blindspot: False
991	    n_pairs: 73
992	    note: Likert also significant p=0.016 but d=0.167 small; BT much stronger p<0.0001. NOT Blindspot because Likert is also significant.
993	  conclusion: success
994	  spec:
995	    command: python gpt4o_crossbenchmark_scoring.py --benchmark mtbench
996	    server: westb-29275
997	    data_path: data/counterfactuals_mtbench_formality.jsonl
998	    data_count: 73
999	    model_name: gpt-4o
1000	    seed: 42
1001	    checkpoint_path: N/A (API scoring)
1002	    log_path: data/gpt4o_mtbench_formality_results.json
1003	  completed_at: 2026-05-21T08:58:18.609Z
1004	
1005	================================================================================
1006	EXPERIMENT 38/58: qwen32b_register
1007	================================================================================
1008	  status: DONE
1009	  retry_count: 0
1010	  created_at: 2026-05-21T04:24:08.776Z
1011	  updated_at: 2026-05-21T05:56:18.529Z
1012	  hypothesis: Qwen3-32B judge shows register (academic/conversational) bias in pairwise comparison while Likert fails to detect it, extending Blindspot to a third style axis
1013	  spec:
1014	    command: pairwise_scoring.py + judge_scoring.py via vLLM Qwen3-32B local (tp=2, port 8000)
1015	    server: westb-29275
1016	    data_path: /root/causal_style_decomp_judge/data/verified_register.jsonl
1017	    data_count: 94
1018	    model_name: Qwen3-32B (local judge via vLLM)
1019	    seed: 42
1020	    checkpoint_path: data/pairwise_results_qwen32b_register.jsonl
1021	    log_path: data/scored_qwen32b_register.jsonl
1022	  conclusion: success
1023	  metrics:
1024	    pairwise: {"consistency_rate": 0.6, "academic_win_rate": 0.593, "sign_test_p": 0.22, "wilson_ci": [0.46, 0.713]}
1025	    likert: {"ate": 0.074, "p": 0.505, "cohens_d": 0.069, "tie_rate": 0.638}
1026	    direction: {"academic_to_conv_orig_pref": 0.893, "academic_to_conv_p": 2.7e-05, "conv_to_academic_orig_pref": 0.312, "conv_to_academic_p": 0.05}
1027	    blindspot_confirmed: False
1028	    bt: {"p_academic_wins": 0.553, "bootstrap_ci": [0.479, 0.628], "bootstrap_p": 0.0763, "bootstrap_method": "pair-level (10000 iterations, seed=42)", "n_pairs": 94, "n_comparisons": 188}
1029	    gee_decomposition: {"academic_or": 1.9053, "academic_ci": [1.01, 3.58], "academic_p": 0.0455, "originality_or": 5.7181, "originality_p": 0.0001, "note": "Register significant after controlling for originality bias (OR=1.91 p=0.046). Originality dominant (OR=5.72)."}
1030	    status_note: BT P(academic)=55.3% [47.9%, 62.8%] p=0.076 (NS). GEE academic OR=1.91 p=0.046 (significant after controlling originality). Originality dominant.
1031	  completed_at: 2026-05-21T04:39:54.506Z
1032	
1033	================================================================================
1034	EXPERIMENT 39/58: gpt4o_register
1035	================================================================================
1036	  status: DONE
1037	  retry_count: 0
1038	  created_at: 2026-05-21T05:28:11.858Z
1039	  updated_at: 2026-05-21T05:33:18.995Z
1040	  hypothesis: GPT-4o judge shows register (academic/conversational) bias detectable via pairwise but not Likert, extending Blindspot to register axis with GPT-4o and enabling cross-model GEE decomposition comparison
1041	  spec:
1042	    command: pairwise_scoring.py + judge_scoring.py via GPT-4o OpenRouter API
1043	    server: westb-29275
1044	    data_path: /root/causal_style_decomp_judge/data/verified_register.jsonl
1045	    data_count: 100
1046	    model_name: GPT-4o (OpenRouter via http://47.94.22.126/v1)
1047	    seed: 42
1048	    checkpoint_path: data/pairwise_results_gpt4o_register.jsonl
1049	    log_path: data/scored_gpt4o_register.jsonl
1050	  conclusion: success
1051	  metrics:
1052	    pairwise: {"academic_win_rate": 0.633, "sign_test_p": 0.085}
1053	    likert: {"ate": 0, "p_wilcoxon": 0.7849, "cohens_d": 0, "tie_rate": 0.6489}
1054	    bt: {"p_academic_wins": 0.5699, "bootstrap_ci": [0.5, 0.6398], "bootstrap_p": 0.04, "bootstrap_method": "pair-level (10000 iterations, seed=42)"}
1055	    gee_decomposition: {"academic_or": 1.8759, "academic_p": 0.0285, "originality_or": 2.2098, "originality_p": 0.0058, "note": "Style marginally significant (OR=1.88 p=0.03), originality stronger (OR=2.21 p=0.006). Pattern consistent with Qwen3-32B register."}
1056	    blindspot_confirmed: True
1057	    status_note: BT P(academic)=57.0% [50.0%, 64.0%] p=0.04; Likert ATE=0 p=0.78 (Blindspot confirmed). GEE academic OR=1.88 p=0.03, orig OR=2.21 p=0.006.
1058	  completed_at: 2026-05-21T05:29:01.095Z
1059	
1060	================================================================================
1061	EXPERIMENT 40/58: gpt4o_verbosity
1062	================================================================================
1063	  status: DONE
1064	  retry_count: 0
1065	  created_at: 2026-05-21T05:28:11.348Z
1066	  updated_at: 2026-05-21T05:33:15.238Z
1067	  hypothesis: GPT-4o judge shows verbosity bias in pairwise comparison while Likert fails to detect it, extending Blindspot confirmation to GPT-4o × verbosity cell and enabling cross-model comparison with Qwen3-32B
1068	  spec:
1069	    command: pairwise_scoring.py + judge_scoring.py via GPT-4o OpenRouter API
1070	    server: westb-29275
1071	    data_path: /root/causal_style_decomp_judge/data/verified_verbosity.jsonl
1072	    data_count: 100
1073	    model_name: GPT-4o (OpenRouter via http://47.94.22.126/v1)
1074	    seed: 42
1075	    checkpoint_path: data/pairwise_results_gpt4o_verbosity.jsonl
1076	    log_path: data/scored_gpt4o_verbosity.jsonl
1077	  conclusion: success
1078	  metrics:
1079	    pairwise: {"verbose_win_rate": 0.863, "sign_test_p": 1e-06, "wilson_ci": [0.766, 0.924]}
1080	    likert: {"ate": 0.1163, "p_wilcoxon": 0.4033, "cohens_d": 0.078, "tie_rate": 0.5814}
1081	    bt: {"p_verbose_wins": 0.7602, "bootstrap_ci": [0.6881, 0.8283], "bootstrap_p": 0.0001, "bootstrap_method": "pair-level (10000 iterations, seed=42)"}
1082	    gee_decomposition: {"verbose_or": 10.9719, "verbose_p": 0.0001, "originality_or": 0.4373, "originality_p": 0.0514, "note": "Pure style bias (OR=10.97 p<0.0001). Originality not significant and in opposite direction (OR=0.44)."}
1083	    blindspot_confirmed: True
1084	    status_note: BT P(verbose)=76.0% [68.8%, 82.8%] p=0.0001; Likert ATE=+0.12 p=0.40 (Blindspot confirmed). GEE verbose OR=10.97 p<0.0001, orig OR=0.44 ns.
1085	  completed_at: 2026-05-21T05:29:00.698Z
1086	
1087	================================================================================
1088	EXPERIMENT 41/58: qwen32b_verbosity
1089	================================================================================
1090	  status: DONE
1091	  retry_count: 0
1092	  created_at: 2026-05-21T04:24:03.744Z
1093	  updated_at: 2026-05-21T05:06:43.883Z
1094	  hypothesis: Qwen3-32B judge shows verbosity bias in pairwise comparison (verbose win rate >60%, p<0.05) while Likert scoring fails to detect it, extending Blindspot finding to verbosity axis
1095	  spec:
1096	    command: pairwise_scoring.py + judge_scoring.py via vLLM Qwen3-32B local (tp=2, port 8000)
1097	    server: westb-29275
1098	    data_path: /root/causal_style_decomp_judge/data/verified_verbosity.jsonl
1099	    data_count: 86
1100	    model_name: Qwen3-32B (local judge via vLLM)
1101	    seed: 42
1102	    checkpoint_path: data/pairwise_results_qwen32b_verbosity.jsonl
1103	    log_path: data/scored_qwen32b_verbosity.jsonl
1104	  conclusion: success
1105	  metrics:
1106	    pairwise: {"consistency_rate": 0.74, "verbose_win_rate": 0.873, "sign_test_p": 1e-06, "wilson_ci": [0.769, 0.934]}
1107	    likert: {"ate": -0.151, "p": 0.179, "cohens_d": -0.146, "tie_rate": 0.581}
1108	    direction: {"verbose_to_concise_orig_pref": 0.806, "verbose_to_concise_p": 0.000878, "concise_to_verbose_rewrite_pref": 0.907, "concise_to_verbose_p": 1e-06}
1109	    note: Strongest bias: 87.3% verbose win (p<10⁻⁶) but Likert p=0.179. Both directions prefer verbose content (not originality bias).
1110	    blindspot_confirmed: True
1111	    bt: {"p_verbose_wins": 0.7732, "bootstrap_ci": [0.7034, 0.8429], "bootstrap_p": 0.0001, "bootstrap_method": "pair-level (10000 iterations, seed=42)"}
1112	    gee_decomposition: {"verbose_or": 13.1, "verbose_ci": [5.62, 30.55], "verbose_p": 2.6e-09, "originality_or": 0.49, "originality_ci": [0.21, 1.14], "originality_p": 0.096, "note": "Verbosity bias entirely style-driven (OR=13.10 p<10\u207b\u2079). Originality non-significant and in opposite direction (OR=0.49)."}
1113	    status_note: BT P(verbose)=77.3% [70.3%, 84.3%] p<0.0001; GEE verbose OR=13.10 p<10⁻⁹, originality OR=0.49 ns. Purest style bias across all cells.
1114	  completed_at: 2026-05-21T04:39:53.961Z
1115	
1116	================================================================================
1117	EXPERIMENT 42/58: qwen32b_formality
1118	================================================================================
1119	  status: DONE
1120	  retry_count: 0
1121	  created_at: 2026-05-21T04:24:01.452Z
1122	  updated_at: 2026-05-21T04:43:06.759Z
1123	  hypothesis: Qwen3-32B as local judge will show similar formality bias pattern to GPT-4o (significant pairwise, non-significant Likert), confirming the Likert Blindspot is cross-model and not GPT-4o-specific
1124	  spec:
1125	    command: pairwise_scoring.py + judge_scoring.py via vLLM Qwen3-32B local (tp=2, port 8000)
1126	    server: westb-29275
1127	    data_path: /root/causal_style_decomp_judge/data/verified_32b.jsonl
1128	    data_count: 88
1129	    model_name: Qwen3-32B (local judge via vLLM)
1130	    seed: 42
1131	    checkpoint_path: data/pairwise_results_qwen32b_formality.jsonl
1132	    log_path: data/scored_qwen32b_formality.jsonl
1133	  conclusion: success
1134	  metrics:
1135	    pairwise: {"consistency_rate": 0.65, "formal_win_rate": 0.764, "sign_test_p": 0.000114, "wilson_ci": [0.637, 0.856]}
1136	    likert: {"ate": 0.011, "p": 0.908, "cohens_d": 0.012, "tie_rate": 0.727}
1137	    direction: {"formal_to_casual_win": 0.814, "formal_to_casual_p": 4.2e-05, "casual_to_formal_win": 0.5, "casual_to_formal_p": 1}
1138	    vs_gpt4o: pairwise 76.4% vs 63.0% (stronger); Likert both non-sig (p=0.908 vs p=0.332)
1139	    blindspot_confirmed: True
1140	    bt: {"p_formal_wins": 0.6647, "bootstrap_ci": [0.5852, 0.7386], "bootstrap_p": 0.0001, "bootstrap_method": "pair-level (10000 iterations, seed=42)"}
1141	    gee_decomposition: {"formal_or": 4.2008, "formal_p": 0.0002, "originality_or": 4.7041, "originality_p": 0.0001, "note": "Both effects strong and nearly equal magnitude; casual\u2192formal at 50% confirms originality confound"}
1142	    status_note: BT P(formal)=66.5% [58.5%, 73.9%] p<0.0001; GEE formal OR=4.20 p=0.0002, originality OR=4.70 p<0.0001
1143	  completed_at: 2026-05-21T04:39:53.009Z
1144	
1145	================================================================================
1146	EXPERIMENT 43/58: exp016_bradley_terry
1147	================================================================================
1148	  status: DONE
1149	  retry_count: 0
1150	  created_at: 2026-05-21T02:32:58.075Z
1151	  updated_at: 2026-05-21T03:29:34.811Z
1152	  spec:
1153	    command: python csd_pipeline/exp016_bradley_terry.py
1154	    server: westb-29275
1155	    data_path: /root/causal_style_decomp_judge/data/pairwise_results_32b.jsonl
1156	    data_count: 197
1157	    model_name: choix BT + bootstrap
1158	    seed: 42
1159	    checkpoint_path: N/A (reanalysis)
1160	    log_path: csd_pipeline/exp016_bradley_terry.py
1161	  hypothesis: Bradley-Terry model on ALL pairwise data (no consistency filtering) will confirm formal preference is significant, validating the sign test result and showing the effect is robust to inclusion of position-inconsistent pairs
1162	  metrics:
1163	    primary_nli_filtered: {"n_pairs": 88, "n_comparisons": 173, "p_formal_wins": 0.63, "bootstrap_ci": [0.5575, 0.7028], "bootstrap_p": 0.0004, "bootstrap_method": "pair-level (2000 iterations, seed=42)", "ci_excludes_50": true}
1164	    robustness_all_data: {"n_pairs": 100, "n_comparisons": 197, "p_formal_wins": 0.6091, "bootstrap_ci": [0.5381, 0.6784], "bootstrap_p": 0.001, "bootstrap_method": "pair-level (2000 iterations, seed=42)", "ci_excludes_50": true}
1165	    comparison_level_reference: {"all_data_ci": [0.5381, 0.6751], "nli_filtered_ci": [0.5607, 0.6994], "note": "Pair-level CIs ~2-5% wider than comparison-level, conclusions unchanged"}
1166	    comparison_to_sign_test: BT NLI-filtered 63.0% [55.8-70.3%] p<0.001 vs sign test 69.1% [56.0-79.7%] p=0.006
1167	  conclusion: success
1168	  completed_at: 2026-05-21T02:33:14.569Z
1169	
1170	================================================================================
1171	EXPERIMENT 44/58: verbosity_32b
1172	================================================================================
1173	  status: DONE
1174	  retry_count: 0
1175	  created_at: 2026-05-20T18:20:44.306Z
1176	  updated_at: 2026-05-21T03:21:39.924Z
1177	  hypothesis: Verbosity axis (verbose/concise) produces stronger style bias signal than formality in GPT-4o judge: pairwise win rate ≥60% with p<0.05 and/or Likert corrected ATE with d≥0.3, because verbose responses contain more surface-level detail that judges may conflate with thoroughness
1178	  parent: pairwise_32b
1179	  spec:
1180	    command: counterfactual_gen --axis verbosity + content_verification + judge_scoring + pairwise_scoring + ate_analysis
1181	    server: westb-29275
1182	    data_path: /root/causal_style_decomp_judge/data/counterfactuals_verbosity.jsonl
1183	    data_count: 100
1184	    model_name: Qwen3-32B (counterfactual) + GPT-4o (judge)
1185	    seed: 42
1186	    checkpoint_source: Qwen3-32B vLLM serve
1187	    eval_data: LLMBar adversarial 100 samples
1188	  checkpoint_path: /root/causal_style_decomp_judge/data/verified_verbosity.jsonl
1189	  log_path: /root/causal_style_decomp_judge/data/
1190	  metrics:
1191	    n: 100
1192	    h1_nli_pass_rate: 0.65
1193	    nli_mean: 0.6544
1194	    bertscore_pass_rate: 0.27
1195	    bertscore_mean: 0.7522
1196	    both_pass: 0.22
1197	    dr_nli_mean: 0.4847
1198	    dr_bertscore_mean: 0.7199
1199	    dr_pass_rate: 0.04
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37d7828d-b594-4ff3-9db9-e32e8eae7eb7",
  "isSidechain": true,
  "promptId": "8842f241-92c6-4951-b177-588e67a11a5d",
  "agentId": "a5fd80952fb015e5f",
  "type": "user",
  "uuid": "e87ca931-0d87-4c5d-a23a-7517b60d29f6",
  "sourceToolAssistantUUID": "37d7828d-b594-4ff3-9db9-e32e8eae7eb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-25T19:44:03.905Z_

<details open><summary>🔧 Tool call — Read · `toolu_015TpgRKqkbQczsTXYviJkiW`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge/34b1c8fb-c53e-47b8-bef7-53d80c2bd748/tool-results/b4l3pk2r8.txt",
  "limit": 300,
  "offset": 1200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e87ca931-0d87-4c5d-a23a-7517b60d29f6",
  "isSidechain": true,
  "agentId": "a5fd80952fb015e5f",
  "requestId": "req_011CbPrpanqLa3JdFtUGmQkw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bcc0b179-e236-4d9f-a763-ff056a7a7884",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vhu99dtmj5gn1Aow8ozVyQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7383,
      "cache_read_input_tokens": 43999,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7383
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 43999,
          "cache_creation_input_tokens": 7383,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7383,
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

_source line 35 · 2026-05-25T19:44:03.911Z_

<details><summary>↩ Tool result · `toolu_015TpgRKqkbQczsTXYviJkiW`</summary>

```text
1200	    stopped_at: scoring
1201	    stop_reason: API 402 Insufficient balance
1202	    v2_direction_aware_nli: {"nli_ge90": 0.86, "nli_ge80": 0.86, "nli_ge95": 0.83, "forward_n": 46, "forward_nli_mean": 0.9476, "backward_n": 54, "backward_nli_mean": 0.8267, "nli_only_pass_rate_at_090": 0.86, "h1_status": "PASS (86% >= 80%)", "pipeline_blocked_at": "scoring (API 402, D013 approved NLI-only gate)"}
1203	    status_note: H1 PASS (direction-aware NLI 86%). Scoring/H2 deferred to separate experiment when API available.
1204	  conclusion: success
1205	  completed_at: 2026-05-20T21:13:31.070Z
1206	
1207	================================================================================
1208	EXPERIMENT 45/58: exp-016
1209	================================================================================
1210	  status: DONE
1211	  retry_count: 0
1212	  created_at: 2026-05-21T02:30:50.899Z
1213	  updated_at: 2026-05-21T03:21:32.758Z
1214	  hypothesis: Bradley-Terry model on all pairwise comparisons (without consistency filtering) will confirm formal style preference, validating the sign test result with a parametric approach
1215	  spec:
1216	    command: python3 csd_pipeline/exp016_bradley_terry.py
1217	    server: westb-29275
1218	    data_path: data/pairwise_results_32b.jsonl
1219	    data_count: 100
1220	    model_name: n/a
1221	    seed: 42
1222	  metrics:
1223	    DUPLICATE: canonical entry is exp016_bradley_terry. This entry should be ignored.
1224	  conclusion: killed
1225	  log_path: csd_pipeline/exp016_bradley_terry.py
1226	  checkpoint_path: n/a
1227	  completed_at: 2026-05-21T02:31:32.935Z
1228	
1229	================================================================================
1230	EXPERIMENT 46/58: exp-015
1231	================================================================================
1232	  status: DONE
1233	  retry_count: 0
1234	  created_at: 2026-05-21T02:30:49.225Z
1235	  updated_at: 2026-05-21T03:21:31.803Z
1236	  hypothesis: Ordinal regression (CLMM proxy) on Likert scores will fail to detect formality style effect, confirming the Blindspot that pointwise scoring is insensitive to style bias
1237	  spec:
1238	    command: python3 csd_pipeline/exp015_clmm_analysis.py
1239	    server: westb-29275
1240	    data_path: data/scored_32b.jsonl
1241	    data_count: 88
1242	    model_name: n/a
1243	    seed: 0
1244	  metrics:
1245	    DUPLICATE: canonical entry is exp015_clmm. This entry should be ignored.
1246	  conclusion: killed
1247	  log_path: csd_pipeline/exp015_clmm_analysis.py
1248	  checkpoint_path: n/a
1249	  completed_at: 2026-05-21T02:31:32.630Z
1250	
1251	================================================================================
1252	EXPERIMENT 47/58: exp015_clmm
1253	================================================================================
1254	  status: DONE
1255	  retry_count: 0
1256	  created_at: 2026-05-21T02:32:56.750Z
1257	  updated_at: 2026-05-21T02:33:08.624Z
1258	  spec:
1259	    command: python csd_pipeline/exp015_clmm_analysis.py
1260	    server: westb-29275
1261	    data_path: /root/causal_style_decomp_judge/experiments/mvp_32b_ate/scored_32b.jsonl
1262	    data_count: 88
1263	    model_name: statsmodels OrderedModel + GEE + scipy Wilcoxon
1264	    seed: 42
1265	    checkpoint_path: N/A (reanalysis)
1266	    log_path: csd_pipeline/exp015_clmm_analysis.py
1267	  hypothesis: Ordinal regression (CLMM) respecting Likert measurement level will also fail to detect formality effect (p>0.05), confirming that the Likert Blindspot is not an artifact of treating ordinal data as continuous
1268	  metrics:
1269	    ordinal_regression: {"is_formal_coef": -0.079, "is_formal_p": 0.769, "is_formal_ci": [-0.6, 0.45]}
1270	    gee_paired: {"is_formal_coef": -0.084, "is_formal_p": 0.587, "is_formal_ci": [-0.39, 0.22]}
1271	    wilcoxon: {"p": 0.905}
1272	    n_pairs: 88
1273	    n_ties: 55
1274	    tie_rate: 0.625
1275	    conclusion_note: All three methods (ordinal LR, GEE, Wilcoxon) confirm Likert Blindspot: p=0.77/0.59/0.91. 62.5% ties eliminate statistical power.
1276	  conclusion: success
1277	  completed_at: 2026-05-21T02:33:08.624Z
1278	
1279	================================================================================
1280	EXPERIMENT 48/58: exp013_nli_validation
1281	================================================================================
1282	  status: DONE
1283	  retry_count: 0
1284	  created_at: 2026-05-21T01:01:55.339Z
1285	  updated_at: 2026-05-21T01:13:48.712Z
1286	  spec:
1287	    command: python exp013_nli_validation.py --data verified_32b.jsonl + counterfactuals_32b.jsonl --model Qwen3-32B via vLLM port 8001
1288	    server: westb-29275
1289	    data_path: /root/causal_style_decomp_judge/data/verified_32b.jsonl + counterfactuals_32b.jsonl
1290	    data_count: 100
1291	    model_name: Qwen3-32B (LLM-as-annotator) + DeBERTa-v3-large (NLI gate)
1292	    seed: 42
1293	    checkpoint_path: N/A (reanalysis)
1294	    log_path: csd_pipeline/exp013_nli_validation.py
1295	  hypothesis: NLI gate (DeBERTa-v3-large, threshold 0.90) decisions are reliable proxies for human content-preservation judgments, achieving Cohen's kappa >= 0.6 with LLM-as-annotator (Qwen3-32B)
1296	  metrics:
1297	    cohens_kappa: 0.4304
1298	    pabak: 0.82
1299	    gwet_ac1: 0.8934
1300	    agreement_rate: 0.91
1301	    n_samples: 100
1302	    n_nli_pass: 88
1303	    n_nli_fail: 12
1304	    precision: 0.989
1305	    recall: 0.916
1306	    confusion_matrix: {"nli_pass_llm_yes": 87, "nli_pass_llm_no": 1, "nli_fail_llm_yes": 8, "nli_fail_llm_no": 4}
1307	    direction_bias: {"overall_f2c_ratio": 0.59, "nli_fail_f2c_ratio": 0.75, "fn_f2c_ratio": 0.75, "fisher_or": 0.44, "fisher_p": 0.35, "binomial_fn_p": 0.295, "conclusion": "not significant (all p>0.20, n=8/12 too small)"}
1308	    kappa_paradox_note: kappa=0.43 vs PABAK=0.82 vs AC1=0.89 — classic prevalence paradox (Feinstein & Cicchetti 1990, Gwet 2008). Base rate 88:12 skew depresses kappa despite 91% raw agreement.
1309	    interpretation: NLI gate is precision-oriented conservative filter. AC1=0.89 confirms strong agreement. No significant direction bias in FN.
1310	    method: LLM-as-annotator validation (Qwen3-32B)
1311	  conclusion: success
1312	  completed_at: 2026-05-21T01:02:07.941Z
1313	
1314	================================================================================
1315	EXPERIMENT 49/58: exp-013
1316	================================================================================
1317	  status: DONE
1318	  retry_count: 0
1319	  created_at: 2026-05-21T00:59:40.588Z
1320	  updated_at: 2026-05-21T01:05:22.718Z
1321	  hypothesis: NLI gate (DeBERTa-v3-large, threshold 0.90) decisions are reliable proxies for human content-preservation judgments, achieving Cohen's kappa >= 0.6 with LLM-as-annotator (Qwen3-32B)
1322	  spec:
1323	    command: python csd_pipeline/exp013_nli_validation.py --port 8001
1324	    server: westb-29275
1325	    data_path: /root/causal_style_decomp_judge/data/verified_32b.jsonl
1326	    data_count: 100
1327	    model_name: Qwen3-32B (LLM-as-annotator) + DeBERTa-v3-large (NLI gate)
1328	    seed: 0
1329	  checkpoint_path: /root/causal_style_decomp_judge/artifacts/reanalysis_outputs/exp013_nli_validation.csv
1330	  log_path: /tmp/exp013.log
1331	  conclusion: killed
1332	  completed_at: 2026-05-21T01:00:22.508Z
1333	  metrics:
1334	    DUPLICATE: canonical entry is exp013_nli_validation. This entry should be ignored.
1335	
1336	================================================================================
1337	EXPERIMENT 50/58: register_pilot
1338	================================================================================
1339	  status: DONE
1340	  retry_count: 0
1341	  created_at: 2026-05-21T00:14:47.268Z
1342	  updated_at: 2026-05-21T00:19:42.234Z
1343	  hypothesis: Register axis (academic/conversational) RATE counterfactuals preserve content (NLI+BERTScore pass rate ≥80%) and register is independent from formality (agreement ≤95%), making it a viable third axis alongside formality and verbosity
1344	  metrics:
1345	    n_samples: 20
1346	    cf_pass_rate_joint: 0.2
1347	    cf_pass_rate_nli_only: 0.95
1348	    cf_pass_rate_bs_only: 0.2
1349	    nli_cf_mean: high (19/20 ≥ 0.90)
1350	    bertscore_cf_mean: 0.8458
1351	    bertscore_threshold: 0.92
1352	    register_formality_agreement: 0.5
1353	    bs_sweep_0.80: 0.75
1354	    bs_sweep_0.84: 0.6
1355	    bs_sweep_0.88: 0.4
1356	    bs_sweep_0.92: 0.2
1357	    conclusion_note: FAIL with joint gate (20%), PASS with NLI-only (95%). BERTScore sole bottleneck. Register-Formality 50% = orthogonal.
1358	  spec:
1359	    checkpoint_path: N/A (pilot)
1360	    log_path: logs/workers/worker_ops_register_pilot_20260520T233206.log
1361	  conclusion: negative
1362	  completed_at: 2026-05-21T00:19:42.234Z
1363	
1364	================================================================================
1365	EXPERIMENT 51/58: exp014_logistic_decomposition
1366	================================================================================
1367	  status: DONE
1368	  retry_count: 0
1369	  created_at: 2026-05-20T23:56:26.706Z
1370	  updated_at: 2026-05-21T00:19:41.292Z
1371	  hypothesis: The observed 69.1% formal win rate in pairwise comparison is primarily driven by original-preference bias rather than genuine formality effect, and logistic regression decomposition will show formality coefficient is non-significant after controlling for original preference
1372	  metrics:
1373	    method_note: CORRECTED: pair-level bootstrap + GEE (fixes independence violation)
1374	    pair_bootstrap: {"formal_effect_coef": 0.7928, "formal_effect_OR": 2.2095, "formal_effect_OR_ci": [1.228, 4.305], "formal_effect_p": 0.0121, "original_effect_coef": 0.5958, "original_effect_OR": 1.8145, "original_effect_OR_ci": [0.976, 3.369], "original_effect_p": 0.0643}
1375	    gee_exchangeable: {"formal_effect_coef": 0.7931, "formal_effect_OR": 2.2103, "formal_effect_OR_ci": [1.21, 4.038], "formal_effect_p": 0.0099, "original_effect_coef": 0.5973, "original_effect_OR": 1.8172, "original_effect_OR_ci": [0.995, 3.319], "original_effect_p": 0.052}
1376	    direction_subset: {"formal_to_casual_win_rate": 0.788, "formal_to_casual_p": 0.001319, "casual_to_formal_win_rate": 0.545, "casual_to_formal_p": 0.831812}
1377	    intercept_position_bias: -0.5851
1378	    n_pairs: 98
1379	    n_observations: 196
1380	    old_observation_bootstrap_note: SUPERSEDED: old p=0.011/0.048 used observation-level bootstrap, understated SE
1381	  spec:
1382	    checkpoint_path: N/A (reanalysis)
1383	    log_path: artifacts/csd_pipeline/exp014_logistic_decomposition.py
1384	  conclusion: success
1385	  completed_at: 2026-05-21T00:19:41.292Z
1386	
1387	================================================================================
1388	EXPERIMENT 52/58: exp012_consistency_bias
1389	================================================================================
1390	  status: DONE
1391	  retry_count: 0
1392	  created_at: 2026-05-20T23:56:26.226Z
1393	  updated_at: 2026-05-21T00:19:40.352Z
1394	  hypothesis: The consistency filter (discarding 43% of pairs) introduces systematic selection bias by preferentially retaining pairs with higher NLI/BERTScore or different text characteristics, biasing downstream analysis
1395	  metrics:
1396	    consistent_n: 55
1397	    inconsistent_n: 43
1398	    consistency_rate: 0.561
1399	    nli_mwu_p: 0.824
1400	    bertscore_mwu_p: 0.12
1401	    orig_length_mwu_p: 0.137
1402	    length_diff_mwu_p: 0.715
1403	    nli_ks_p: 0.68
1404	    conclusion_note: No systematic bias detected in consistency filter (all p>0.12)
1405	  spec:
1406	    checkpoint_path: N/A (reanalysis)
1407	    log_path: artifacts/csd_pipeline/exp012_consistency_bias.py
1408	  conclusion: success
1409	  completed_at: 2026-05-21T00:19:40.352Z
1410	
1411	================================================================================
1412	EXPERIMENT 53/58: exp011_nli_sensitivity
1413	================================================================================
1414	  status: DONE
1415	  retry_count: 0
1416	  created_at: 2026-05-20T23:56:25.254Z
1417	  updated_at: 2026-05-21T00:19:39.371Z
1418	  hypothesis: The 0.90 NLI threshold is on a cliff edge where small changes dramatically affect pass rate and downstream pairwise results, making our findings threshold-dependent rather than robust
1419	  metrics:
1420	    formality_pass_rate_0.70: 0.89
1421	    formality_pass_rate_0.90: 0.88
1422	    formality_pass_rate_0.95: 0.85
1423	    pw_win_rate_0.70: 0.723
1424	    pw_win_rate_0.90: 0.739
1425	    pw_p_0.70: 0.0031
1426	    pw_p_0.90: 0.0016
1427	    nli_mean: 0.8956
1428	    nli_std: 0.2792
1429	    tone_pass_rate_0.70: 0.65
1430	    conclusion_note: NLI bimodal distribution, 0.90 NOT on cliff edge, pairwise results robust across all thresholds
1431	  spec:
1432	    checkpoint_path: N/A (reanalysis)
1433	    log_path: artifacts/csd_pipeline/exp011_nli_sensitivity.py
1434	  conclusion: success
1435	  completed_at: 2026-05-21T00:19:39.371Z
1436	
1437	================================================================================
1438	EXPERIMENT 54/58: exp010_binarized_likert
1439	================================================================================
1440	  status: DONE
1441	  retry_count: 0
1442	  created_at: 2026-05-20T23:46:24.180Z
1443	  updated_at: 2026-05-20T23:46:47.575Z
1444	  hypothesis: Likert-vs-Pairwise sensitivity gap is due to measurement structure (forced choice eliminates ties) not statistical test choice; binarized Likert with sign test will remain non-significant (p>0.05) while pairwise sign test is significant (p=0.006), because 1-10 integer Likert produces excessive ties that mask the signal
1445	  parent: pairwise_32b
1446	  conclusion: success
1447	  spec:
1448	    command: exp010_binarized_likert.py --input-file data/scored_32b.jsonl --axis formality
1449	    server: westb-29275
1450	    data_path: /root/causal_style_decomp_judge/data/scored_32b.jsonl
1451	    data_count: 100
1452	    model_name: reanalysis (no model)
1453	    seed: 42
1454	    checkpoint_path: /root/causal_style_decomp_judge/data/exp010_results/exp010_binarized_likert.csv
1455	    log_path: /root/causal_style_decomp_judge/data/exp010_results/
1456	  completed_at: 2026-05-20T23:46:47.575Z
1457	
1458	================================================================================
1459	EXPERIMENT 55/58: tone_pilot
1460	================================================================================
1461	  status: DONE
1462	  retry_count: 0
1463	  created_at: 2026-05-20T23:28:10.374Z
1464	  updated_at: 2026-05-20T23:28:38.580Z
1465	  hypothesis: Tone axis (assertive/hedging) RATE counterfactuals preserve content (NLI+BERTScore pass rate ≥80%) because tone changes only modify epistemic hedging markers without altering factual claims, making it a viable third axis alongside formality
1466	  parent: pairwise_32b
1467	  conclusion: negative
1468	  spec:
1469	    command: counterfactual_gen --axis tone (20 samples) + content_verification --axis tone
1470	    server: westb-29275
1471	    data_path: /root/causal_style_decomp_judge/data/counterfactuals_tone_pilot.jsonl
1472	    data_count: 20
1473	    model_name: Qwen3-32B (counterfactual) + deberta-v3-large (NLI)
1474	    seed: 42
1475	    checkpoint_path: /root/causal_style_decomp_judge/data/verified_tone_pilot.jsonl
1476	    log_path: /root/causal_style_decomp_judge/data/
1477	  completed_at: 2026-05-20T23:28:30.685Z
1478	  metrics:
1479	    n: 20
1480	    detection_split: {"assertive": 13, "hedging": 7}
1481	    nli_cf_pass_rate: 0.65
1482	    bertscore_cf_pass_rate: 0.6
1483	    both_pass_rate: 0.45
1484	    nli_cf_mean: 0.7039
1485	    nli_cf_std: 0.4208
1486	    bertscore_cf_mean: 0.9201
1487	    nli_dr_mean: 0.8841
1488	    bertscore_dr_mean: 0.9164
1489	    by_tone: {"assertive": {"n": 13, "both_pass": 0.385, "nli_cf_mean": 0.6559}, "hedging": {"n": 7, "both_pass": 0.571, "nli_cf_mean": 0.793}}
1490	    failure_mode: assertive→hedging changes epistemic commitment, NLI correctly detects non-entailment (6/20 catastrophic NLI<0.01)
1491	
1492	================================================================================
1493	EXPERIMENT 56/58: pairwise_32b
1494	================================================================================
1495	  status: DONE
1496	  retry_count: 0
1497	  created_at: 2026-05-20T18:12:44.351Z
1498	  updated_at: 2026-05-20T18:15:49.470Z
1499	  hypothesis: Likert 1-10 integer granularity masks a real formality preference in GPT-4o; position-controlled pairwise comparison (more sensitive measurement) reveals significant formal win rate >55% where Likert ATE was non-significant
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcc0b179-e236-4d9f-a763-ff056a7a7884",
  "isSidechain": true,
  "promptId": "8842f241-92c6-4951-b177-588e67a11a5d",
  "agentId": "a5fd80952fb015e5f",
  "type": "user",
  "uuid": "57c46506-8290-454a-9b7a-8dd58e1c0905",
  "sourceToolAssistantUUID": "bcc0b179-e236-4d9f-a763-ff056a7a7884",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-25T19:44:09.689Z_

<details open><summary>🔧 Tool call — Read · `toolu_01J9yjH6wsQD6CFLTYm73MQF`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge/34b1c8fb-c53e-47b8-bef7-53d80c2bd748/tool-results/b4l3pk2r8.txt",
  "limit": 300,
  "offset": 1500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57c46506-8290-454a-9b7a-8dd58e1c0905",
  "isSidechain": true,
  "agentId": "a5fd80952fb015e5f",
  "requestId": "req_011CbPrpy4HX2aTQKXBfbVX1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13183b55-0ae1-45b4-8f32-c2a46d673c3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MhDja5FjLAeUQWTKuS7aSP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6357,
      "cache_read_input_tokens": 51382,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6357
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 51382,
          "cache_creation_input_tokens": 6357,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6357,
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

_source line 37 · 2026-05-25T19:44:09.694Z_

<details><summary>↩ Tool result · `toolu_01J9yjH6wsQD6CFLTYm73MQF`</summary>

```text
1500	  parent: mvp_32b_ate
1501	  spec:
1502	    command: python pairwise_scoring.py --input-file /root/causal_style_decomp_judge/data/verified_32b.jsonl --output-file /root/causal_style_decomp_judge/data/pairwise_results_32b.jsonl --model gpt-4o --base-url http://47.94.22.126/v1 --max-concurrent 5 --rate-limit 60
1503	    server: westb-29275
1504	    data_path: /root/causal_style_decomp_judge/data/verified_32b.jsonl
1505	    data_count: 100
1506	    model_name: GPT-4o (judge, pairwise)
1507	    seed: 42
1508	    checkpoint_source: 32B counterfactuals from mvp_32b_ate
1509	    eval_data: LLMBar adversarial 100 samples with 32B RATE counterfactuals
1510	  checkpoint_path: /root/causal_style_decomp_judge/data/pairwise_results_32b.jsonl
1511	  log_path: /root/causal_style_decomp_judge/data/
1512	  metrics:
1513	    n_total: 100
1514	    n_valid_both_trials: 98
1515	    n_consistent: 55
1516	    n_ties_inconsistent: 43
1517	    consistency_rate: 0.5612
1518	    formal_wins: 38
1519	    casual_wins: 17
1520	    formal_win_rate: 0.6909
1521	    wilson_ci_lo: 0.5597
1522	    wilson_ci_hi: 0.7972
1523	    sign_test_p: 0.006456
1524	    position_bias_trial1_A: 0.5306
1525	    position_bias_trial2_A: 0.551
1526	    position_bias_overall_A: 0.5408
1527	    dir_formal_orig_n: 33
1528	    dir_formal_orig_formal_wins: 26
1529	    dir_formal_orig_win_rate: 0.7879
1530	    dir_formal_orig_p: 0.001145
1531	    dir_casual_orig_n: 22
1532	    dir_casual_orig_formal_wins: 12
1533	    dir_casual_orig_win_rate: 0.5455
1534	    dir_casual_orig_p: 0.8318
1535	    nli_ge90_n: 46
1536	    nli_ge90_formal_wins: 34
1537	    nli_ge90_win_rate: 0.7391
1538	    nli_ge90_p: 0.001537
1539	  conclusion: success
1540	  completed_at: 2026-05-20T18:15:49.470Z
1541	
1542	================================================================================
1543	EXPERIMENT 57/58: mvp_32b_ate
1544	================================================================================
1545	  status: DONE
1546	  retry_count: 0
1547	  created_at: 2026-05-20T17:29:57.801Z
1548	  updated_at: 2026-05-20T17:30:35.462Z
1549	  hypothesis: Qwen3-32B (stronger instruction following than 8B) produces higher-fidelity RATE counterfactuals with lower rewrite bias, revealing significant formality premium (ATE>0.3, d>0.3) in GPT-4o judge scores that was masked by 8B rewrite noise
1550	  parent: mvp_8b_ate
1551	  spec:
1552	    command: full 32B pipeline: counterfactual_gen + content_verification + judge_scoring + ate_analysis --sensitivity
1553	    server: westb-29275
1554	    data_path: /root/causal_style_decomp_judge/data/scored_32b.jsonl
1555	    data_count: 100
1556	    model_name: Qwen3-32B (counterfactual) + GPT-4o (judge)
1557	    seed: 42
1558	    checkpoint_source: Qwen3-32B vLLM serve + GPT-4o judge
1559	    eval_data: LLMBar adversarial 100 samples
1560	  conclusion: negative
1561	  metrics:
1562	    n: 100
1563	    n_primary: 88
1564	    h1_nli_pass_rate: 0.88
1565	    nli_mean: 0.8956
1566	    raw_ate: -0.1023
1567	    raw_se: 0.149
1568	    raw_p: 0.4944
1569	    raw_cohens_d: -0.0731
1570	    rewrite_bias: -0.2045
1571	    corrected_ate: 0.1023
1572	    corrected_se: 0.1048
1573	    corrected_p: 0.3318
1574	    corrected_cohens_d: 0.104
1575	    rate_ratio: -1
1576	    dir_formal_to_casual_ate: 0.14
1577	    dir_formal_to_casual_p: 0.332
1578	    dir_casual_to_formal_ate: 0.0526
1579	    dir_casual_to_formal_p: 0.7365
1580	    sens2_corrected_ate: 0.0959
1581	    sens2_corrected_p: 0.3633
1582	    all_corrected_ate: 0.1
1583	    all_corrected_p: 0.2995
1584	  checkpoint_path: /root/causal_style_decomp_judge/data/ate_results_32b/
1585	  log_path: /root/causal_style_decomp_judge/data/
1586	  completed_at: 2026-05-20T17:30:35.462Z
1587	
1588	================================================================================
1589	EXPERIMENT 58/58: mvp_8b_ate
1590	================================================================================
1591	  status: DONE
1592	  retry_count: 0
1593	  created_at: 2026-05-20T14:43:38.410Z
1594	  updated_at: 2026-05-20T14:44:21.033Z
1595	  spec:
1596	    command: python artifacts/csd_pipeline/ate_analysis.py --input-file data/scored.jsonl --output-dir data/ --alpha 0.05
1597	    server: westb-29275
1598	    data_path: /root/causal_style_decomp_judge/data/scored.jsonl
1599	    data_count: 100
1600	    model_name: Qwen3-8B (counterfactual) + GPT-4o (judge)
1601	    seed: 42
1602	    hypothesis: Binary style counterfactuals (formality axis) via Qwen3-8B RATE double-rewrite reveal significant ATE in GPT-4o judge scores, with formal text receiving higher scores
1603	  conclusion: negative
1604	  metrics:
1605	    n: 100
1606	    h1_nli_pass_rate: 0.95
1607	    raw_ate: -0.08
1608	    raw_se: 0.1161
1609	    raw_p: 0.4923
1610	    raw_cohens_d: -0.0689
1611	    rewrite_bias: -0.2
1612	    corrected_ate: 0.12
1613	    corrected_se: 0.1028
1614	    corrected_p: 0.2458
1615	    corrected_cohens_d: 0.1168
1616	    rate_ratio: -1.5
1617	    dir_formal_to_casual_ate: 0.0645
1618	    dir_formal_to_casual_p: 0.5679
1619	    dir_casual_to_formal_ate: 0.2105
1620	    dir_casual_to_formal_p: 0.2997
1621	    strat_nli90_ate: 0.1263
1622	    strat_nli90_p: 0.2459
1623	    strat_nli90_n: 95
1624	  checkpoint_path: /root/causal_style_decomp_judge/data/ate_summary.csv
1625	  log_path: /root/causal_style_decomp_judge/data/
1626	  hypothesis: Qwen3-8B RATE double-rewrite on formality axis produces content-preserving counterfactuals (NLI≥0.90) that reveal significant formality premium (ATE>0.3, d>0.3) in GPT-4o judge scores, indicating style bias independent of content quality
1627	  completed_at: 2026-05-20T14:44:21.033Z
1628	
1629	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13183b55-0ae1-45b4-8f32-c2a46d673c3d",
  "isSidechain": true,
  "promptId": "8842f241-92c6-4951-b177-588e67a11a5d",
  "agentId": "a5fd80952fb015e5f",
  "type": "user",
  "uuid": "fdb5a1b8-fea2-4264-9aa1-99906a7fde48",
  "sourceToolAssistantUUID": "13183b55-0ae1-45b4-8f32-c2a46d673c3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-25T19:50:05.335Z_

That covers all 58 experiments. Here is the complete audit of every experiment entry with all metrics verbatim.

---

## Complete Experiment Registry Audit — 58 Experiments

### EXPERIMENT 1: `llama70b_crossbench`
- **Status:** DONE
- **Hypothesis:** Llama-70B on AlpacaEval and MT-Bench cross-benchmark pairs will show stronger style bias than on LLMBar (consistent with other judges showing benchmark-dependent effect sizes), confirming style sensitivity generalizes across benchmarks. Effect-size gradient predicts Blindspot disappears at large effects (BT>80%).
- **Metrics:**
  - `alpacaeval_formality`: n=47, bt_pct=95.7, bt_ci=[89.4, 100], bt_p=1.6e-11, likert_d=0.211, likert_wilcoxon_p=0.0124, gee_style_or="degenerate", gee_orig_or="degenerate", blindspot=false
  - `alpacaeval_verbosity`: n=66, bt_pct=97, bt_ci=[92.4, 100], bt_p=6e-17, likert_d=0.297, likert_wilcoxon_p=0.0002, gee_style_or=0.54, gee_orig_or=0.54, blindspot=false
  - `mtbench_formality`: n=36, bt_pct=91.7, bt_ci=[80.6, 100], bt_p=2.3e-07, likert_d=0.234, likert_wilcoxon_p=0.0029, gee_style_or=32.68, gee_orig_or=0.89, blindspot=false
  - `mtbench_verbosity`: MISSING_DATA
  - `comparison_llmbar_formality`: bt_pct=69.5, blindspot=true
  - `comparison_llmbar_verbosity`: bt_pct=73.5, blindspot=true
- **Conclusion:** success

### EXPERIMENT 2: `formality_llama_rewriter`
- **Status:** DONE
- **Hypothesis:** Qwen3-32B judge's formality bias is rewriter-independent: using Llama-3.3-70B-Instruct instead of Qwen3-32B as the RATE counterfactual rewriter will reproduce significant pairwise preference for formal style (BT p<0.05), confirming the bias originates in the judge, not the rewriter.
- **Metrics:**
  - bt_p_formal: 0.711
  - bt_ci: [0.643, 0.775]
  - bt_p_value: 0.0001
  - gee_style_or: 4.4403
  - gee_style_p: 1.3e-05
  - gee_orig_or: 5.7474
  - likert_ate: 0.02
  - likert_cohen_d: 0.013
  - likert_wilcoxon_p: 0.687723
  - blindspot: True
  - nli_pass_rate: 0.79
  - n_total: 100
  - n_nli_pass: 79
  - baseline_delta_pp: 4.6
  - baseline_ci_overlap: True
- **Conclusion:** success

### EXPERIMENT 3: `formality_scaled_n300`
- **Status:** DONE
- **Hypothesis:** Llama-70B scoring of the existing n=355 formality scaled data will replicate the formality Blindspot pattern seen with Qwen3-32B (BT ~67%, Likert NS), providing cross-judge validation at scale. GEE Style OR will show small-sample shrinkage similar to Qwen3 (4.20→2.15).
- **Metrics:**
  - judge: Llama-3.3-70B-Instruct
  - axis: formality
  - n: 355
  - bt_p_formal: 0.725
  - bt_ci: [0.691, 0.759]
  - bt_p_value: 0.0001
  - consistent_win_rate: 0.881
  - n_consistent: 202
  - likert_d: 0.048
  - likert_wilcoxon_p: 0.026
  - tie_rate: 0.715
  - blindspot: False
  - note: "CORRECTED: Worker reported 88.1% which was consistent-pair win rate, not BT. Actual BT=72.5%. LLMBar subset (n=89): BT=74.4%, Likert NS (Blindspot YES). Non-LLMBar subset: BT=69.9%, Likert sig."
- **Conclusion:** success

### EXPERIMENT 4: `verbosity_scaled_n355`
- **Status:** DONE
- **Hypothesis:** Verbosity Style OR at n=355 will shrink from n=86 estimates (8.21-13.10) to projected range 4-6.5 due to small-sample upward bias, mirroring the formality shrinkage pattern (4.20→2.15). Likert ATE will remain NS, confirming the Blindspot is robust to increased sample size for verbosity axis.
- **Metrics:**
  - n_samples: 330
  - n_judges: 5
  - `qwen32b`: bt_p_verbose=0.733, bt_ci=[0.696, 0.77], sign_p=0, likert_d=0.149, likert_wilcoxon_p=0.0006, likert_ttest_p=0.007, gee_intercept_or=3.83, gee_orig_or=0.52, gee_orig_p=0.001, ntc=0.881, blindspot=false, note="Likert now significant at n=355"
  - `llama70b`: bt_p_verbose=0.759, bt_ci=[0.722, 0.793], sign_p=0, likert_d=0.16, likert_wilcoxon_p=0.0001, likert_ttest_p=0.004, gee_intercept_or=4.01, gee_orig_or=0.61, gee_orig_p=0.013, ntc=0.896, blindspot=false, note="Likert now significant at n=355"
  - `gpt54`: bt_p_verbose=0.59, bt_ci=[0.544, 0.635], sign_p=0.0002, likert_d=-0.026, likert_wilcoxon_p=0.813, likert_ttest_p=0.635, gee_intercept_or=1.06, gee_orig_or=1.96, gee_orig_p=0.0005, ntc=0.867, blindspot=true, note="Originality-dominated, minimal style bias"
  - `gemini`: bt_p_verbose=0.678, bt_ci=[0.638, 0.717], sign_p=0, likert_d=0.087, likert_wilcoxon_p=0.021, likert_ttest_p=0.114, gee_intercept_or=2.52, gee_orig_or=0.69, gee_orig_p=0.046, ntc=0.876, blindspot=true, note="Borderline Likert — Wilcoxon sig but t-test NS"
  - `claude`: bt_p_verbose=0.608, bt_ci=[0.567, 0.649], sign_p=1e-06, likert_d=0.032, likert_wilcoxon_p=0.317, likert_ttest_p=0.561, gee_intercept_or=1.22, gee_orig_or=1.69, gee_orig_p=0.002, ntc=0.938, blindspot=true, note="Originality bias, minimal style bias"
  - `gee_shrinkage`: qwen_n86_style_or=13.1, qwen_n355_intercept_or=3.83, shrinkage_pct=70.8, llama_n86_style_or=8.21, llama_n355_intercept_or=4.01, shrinkage_pct_llama=51.2
- **Conclusion:** success

### EXPERIMENT 5: `register_100_cf`
- **Status:** DONE
- **Hypothesis:** Register axis (academic/conversational) produces detectable style bias in GPT-4o judge comparable to formality axis, with pairwise win rate >= 60% and p < 0.05, demonstrating axis-dependent bias generalizes beyond formality
- **Metrics:**
  - n_generated: 100
  - cf_nli_mean: 0.941
  - cf_bertscore_mean: 0.8589
  - cf_nli_pass_rate: 0.94
  - cf_gating: NLI-only (threshold 0.90)
  - dr_nli_mean: 0.8208
  - dr_bertscore_mean: 0.8477
  - dr_pass_rate: 0.81
  - output_file: data/verified_register.jsonl
  - artifact_id: art_20260521_227674
  - pipeline_status: verification DONE, scoring BLOCKED (API 402)
- **Conclusion:** killed

### EXPERIMENT 6: `gemini_flash_fourth_judge`
- **Status:** DONE
- **Hypothesis:** Gemini Flash as a fourth judge will also exhibit style blindspot (BT-significant but Likert-NS) on formality and verbosity axes, consistent with GPT-4o, Qwen-32B, and Claude judges, confirming the blindspot is judge-universal rather than model-specific.
- **Metrics:**
  - `formality`: bt_pct=57.4, bt_ci=[50, 64.2], bt_p=0.0306, likert_ate=-0.239, likert_d=-0.082, likert_p=0.3088, gee_style_or=1.64, gee_style_ci=[0.91, 2.98], gee_style_p=0.1008, gee_orig_or=2.51, gee_orig_ci=[1.39, 4.54], gee_orig_p=0.0024, blindspot=true, regime="Orig-Dominated"
  - `verbosity`: bt_pct=70.8, bt_ci=[63.7, 77.2], bt_p=0, likert_ate=0.151, likert_d=0.051, likert_p=0.3697, gee_style_or=8.98, gee_style_ci=[3.68, 21.94], gee_style_p=0, gee_orig_or=0.46, gee_orig_ci=[0.2, 1.04], gee_orig_p=0.0614, blindspot=true, regime="Pure Style"
- **Conclusion:** success

### EXPERIMENT 7: `llama70b_register`
- **Status:** DONE
- **Hypothesis:** Llama-70B register axis shows weak style bias (~55% BT, consistent with GPT-4o 57% and Qwen3-32B 55.3%), confirming register as originality-dominated across three independent judge architectures
- **Metrics:**
  - bt_p_academic: 0.635
  - bt_ci: [0.555, 0.712]
  - bt_p_val: 0.0014
  - likert_ate: 0.054
  - likert_d: 0.024
  - likert_ttest_p: 0.69
  - likert_tie_rate: 0.688
  - gee_style_or: 3.33
  - gee_style_p: 0.0003
  - gee_orig_or: 3.07
  - gee_orig_p: 0.0008
  - blindspot: True
  - regime: Mixed
- **Conclusion:** success

### EXPERIMENT 8: `llama70b_debiased`
- **Status:** DONE
- **Hypothesis:** Llama-70B correction resistance follows the same axis-dependent pattern as GPT-4o/Qwen3-32B: debiased prompts reduce but do not eliminate style bias, with verbosity more amenable to correction than formality, confirming bias persistence is model-independent
- **Metrics:**
  - `formality`: baseline_bt=69.5, debiased_bt=64.3, debiased_ci=[57.3, 71], debiased_p=0.0001, reduction_pp=-5.2, reduction_pct=26.7, still_significant=true
  - `verbosity`: baseline_bt=73.5, debiased_bt=66.9, debiased_ci=[58.9, 74.4], debiased_p=0.0001, reduction_pp=-6.6, reduction_pct=28.1, still_significant=true
  - all_still_significant: True
- **Conclusion:** success

### EXPERIMENT 9: `crossbench_alpacaeval_verbosity`
- **Status:** DONE
- **Hypothesis:** AlpacaEval verbosity bias is strong enough (BT ~84%) that even Likert detects it, confirming the effect-size gradient: Blindspot occurs at small-to-medium effects (d<0.15) but not at large effects (d>0.3)
- **Metrics:**
  - bt_p_verbose: 84.1
  - bt_ci: [77.4, 90.2]
  - bt_p: 0.0001
  - likert_ate: 0.732
  - likert_d: 0.407
  - likert_p: 0.000414
  - tie_rate: 0.244
  - blindspot: False
  - n_pairs: 82
- **Conclusion:** success

### EXPERIMENT 10: `llama70b_third_judge`
- **Status:** DONE
- **Hypothesis:** Llama-3.3-70B as third independent judge architecture confirms the Likert Blindspot: BT pairwise detects style bias (formality + verbosity) with p<0.05 while Likert scoring shows no significant difference, replicating the pattern found with GPT-4o and Qwen3-32B judges
- **Metrics:**
  - `formality`: bt_p_formal=0.695, bt_ci=[0.619, 0.765], bt_p=0.0001, likert_ate=0.023, likert_p=0.8458, likert_d=0.01, likert_tie_rate=0.727, gee_style_or=4.81, gee_style_p=0.0001, gee_orig_or=3.12, gee_orig_p=0.0007, blindspot=true
  - `verbosity`: bt_p_verbose=0.735, bt_ci=[0.655, 0.809], bt_p=0.0001, likert_ate=0.047, likert_p=0.7524, likert_d=0.02, likert_tie_rate=0.616, gee_style_or=8.21, gee_style_p=0.0001, gee_orig_or=0.38, gee_orig_p=0.0196, blindspot=true
  - blindspot_both_axes: True
  - third_judge_confirms: True
- **Conclusion:** success

### EXPERIMENT 11: `finegrained_likert_100pt`
- **Status:** DONE
- **Hypothesis:** The Likert Blindspot is NOT a scale granularity artifact: even a 100-point continuous scale (0-100) should fail to detect the style bias that pairwise BT detects, because the blindspot stems from absolute-vs-relative evaluation paradigm differences, not insufficient scale resolution
- **Metrics (nested in spec):**
  - `formality`: n=88, ate=-0.625, cohens_d=-0.0376, t_p=0.725, wilcoxon_p=0.9, tie_rate=0.659, mean_style=52.5, mean_plain=53.12, blindspot=true
  - `verbosity`: n=86, ate=2.849, cohens_d=0.1709, t_p=0.117, wilcoxon_p=0.067, tie_rate=0.512, mean_style=53.08, mean_plain=50.23, blindspot=true
  - both_axes_blindspot: true
  - conclusion: "100-point scale cannot detect style bias that BT detects — Blindspot is absolute-vs-relative paradigm difference, not granularity artifact"
- **Conclusion:** success

### EXPERIMENT 12: `gpt4o_rewriter_verbosity`
- **Status:** DONE
- **Hypothesis:** Verbosity style bias is rewriter-independent: GPT-4o rewriter + Qwen3-32B judge should produce BT probability statistically equivalent to Qwen3-32B rewriter + Qwen3-32B judge, confirming the measured verbosity bias reflects judge behavior not rewriter artifacts
- **Metrics:**
  - cf_generated: 100
  - nli_pass: 81
  - nli_rate: 0.81
  - bt: p_verbose=0.735, ci=[0.654, 0.809], p_value=0.0001
  - likert: ate=0, p=0.8384, d=0, tie_rate=0.469
  - gee: style_or=10.17, style_p=0.0001, orig_or=1.61, orig_p=0.3143
  - blindspot: True
  - vs_baseline: qwen32b_bt=0.773, delta_pp=-3.8, ci_overlap=true, note="GPT-4o rewriter gives 73.5% vs Qwen3-32B rewriter 77.3%, CIs overlap → rewriter-independent"
- **Conclusion:** success

### EXPERIMENT 13: `gpt4o_rewriter_formality`
- **Status:** DONE
- **Hypothesis:** Style bias detected by RATE is rewriter-independent: switching from Qwen3-32B rewriter to GPT-4o rewriter should produce statistically equivalent BT probability for formality axis, proving the measured bias reflects judge behavior not rewriter artifacts
- **Metrics:**
  - cf_generated: 100
  - nli_pass: 90
  - nli_rate: 0.9
  - bt: p_formal=0.644, ci=[0.561, 0.728], p_value=0.0006, n_pairs=90, n_comparisons=180, method="ALL NLI-pass pairs (fixed from consistent-only bug)"
  - gee: style_or=9.48, style_p=0.0001, orig_or=12.76, orig_p=0.0001, note="Fixed: was 24.47/39.27 with consistent-only filter (near-separation artifact)"
  - likert: ate=-0.189, p=0.1835, d=-0.081, tie_rate=0.489, mean_formal=5.511, mean_casual=5.7
  - blindspot: True
  - vs_baseline: qwen32b_bt=0.665, delta_pp=-2.1, ci_overlap=true, note="GPT-4o rewriter 64.4% vs Qwen3-32B rewriter 66.5%, baseline falls within CI [56.1%, 72.8%] → rewriter-independent"
  - bug_fix: original_bt=0.697, original_gee_style_or=24.47, original_gee_orig_or=39.27, original_n_pairs=66, fix="Used ALL 90 NLI-pass pairs for BT/GEE instead of consistent-only 66. §3.3 requires all observations.", fix_script="csd_pipeline/fix_formality_rewriter_bt.py"
- **Conclusion:** success

### EXPERIMENT 14: `debiased_verbosity_gpt4o`
- **Status:** DONE
- **Hypothesis:** Debiased prompt intervention for verbosity axis on GPT-4o should show partial but insufficient bias reduction, consistent with formality results showing style bias is deeper than prompt-level
- **Metrics (nested in spec):**
  - original_p_verbose: "76.0% [69.7, 83.5], p=0.0001"
  - debiased_p_verbose: "62.9% [54.5, 70.9], p=0.0016"
  - reduction_pp: "-13.1pp (50.4% of bias eliminated)"
  - still_significant: true
  - valid_pairs: 83
  - consistent_pairs: 54
  - n_comparisons: 167
  - neither_count: "~5 pairs (3 retries each)"
- **Conclusion:** success

### EXPERIMENT 15: `nli_threshold_sweep`
- **Status:** DONE
- **Hypothesis:** BT-detected style bias is robust to NLI threshold choice: sweeping from 0.50 to 0.98 should show stable BT probability and consistent significance across all 4 axis×judge combinations
- **Metrics (nested in spec):**
  - total_significant: "44/44 (100%)"
  - formality_qwen32b_bt_range: "0.648-0.665"
  - formality_gpt4o_bt_range: "0.614-0.642"
  - verbosity_qwen32b_bt_range: "0.765-0.773"
  - verbosity_gpt4o_bt_range: "0.752-0.769"
  - all_p_values: "≤0.002"
  - max_bt_delta_across_thresholds: "~3pp"
- **Conclusion:** success

### EXPERIMENT 16: `bootstrap_attenuation`
- **Status:** DONE
- **Hypothesis:** Bootstrap subsampling of Likert data shows Cohen's d remains near zero across all sample sizes (n=50-355), demonstrating measurement attenuation rather than power gap
- **Metrics:**
  - `formality_qwen32b`: file="scored_scaled_formality_qwen32b.jsonl", n=355, full_d=-0.017, curve={n50: d_median=-0.017 ci=[-0.308, 0.262], n100: d_median=-0.015 ci=[-0.219, 0.176], n150: d_median=-0.019 ci=[-0.179, 0.145], n200: d_median=-0.016 ci=[-0.157, 0.119], n250: d_median=-0.018 ci=[-0.144, 0.107], n300: d_median=-0.018 ci=[-0.131, 0.095], n355: d_median=-0.017 ci=[-0.123, 0.087]}, interpretation="SMOKING GUN: d_median flat at ~-0.017 across ALL n. CI narrows but always includes 0. Measurement attenuation confirmed."
  - `verbosity_qwen32b`: file="scored_qwen32b_verbosity.jsonl", n=86, full_d=0.146, curve={n30: d_median=0.169 ci=[-0.195, 0.595], n50: d_median=0.157 ci=[-0.119, 0.494], n70: d_median=0.155 ci=[-0.085, 0.443], n86: d_median=0.153 ci=[-0.067, 0.416]}, interpretation="d stable at ~0.15 (below small-effect threshold 0.2). CI always includes 0. Even at n=1000 would not detect."
  - `verbosity_gpt4o`: file="scored_gpt4o_verbosity.jsonl", n=86, full_d=0.19, curve={n30: d_median=0.205 ci=[-0.161, 0.618], n50: d_median=0.198 ci=[-0.085, 0.53], n70: d_median=0.197 ci=[-0.048, 0.472], n86: d_median=0.197 ci=[-0.022, 0.446]}, interpretation="d stable at ~0.19-0.20 (borderline small). CI includes 0 at all n. BT detects 76.0% (massive), Likert sees d=0.19 (trivial)."
  - `formality_gpt4o`: note="Only 20 NLI-pass pairs available from scored_alpacaeval_gpt4o.jsonl. Single point: d_median=-0.20, CI=[-0.72, 0.24]. Insufficient for curve."
  - summary: "3/4 combinations computed. Formality×Qwen3-32B (n=355) is the definitive result: d≈0 flat across all subsample sizes = measurement attenuation, not power gap. BT detects 66.5% (p<0.0001) on same data where Likert d=-0.017."
- **Conclusion:** success

### EXPERIMENT 17: `cf_vs_dr_gpt4o`
- **Status:** DONE
- **Hypothesis:** Comparing counterfactual (style-changed + artifact) vs double-rewrite (original-style + artifact) with GPT-4o judge isolates pure style effect by controlling for rewriting artifact.
- **Metrics:**
  - judge: GPT-4o
  - comparison: counterfactual vs double_rewrite
  - `formality`: n_pairs=81, n_consistent=53, consistency=0.654, cf_win_rate=0.151, ci=[0.057, 0.246], p_value=0, interpretation="DR strongly preferred over CF"
  - `verbosity`: note="awaiting final result from worker, pattern matches Qwen3-32B"
- **Conclusion:** negative

### EXPERIMENT 18: `double_rewrite_placebo_gpt4o`
- **Status:** DONE
- **Hypothesis:** Pairwise comparison of original vs double-rewrite (same style, only rewriting artifact difference) yields BT ≈ 50% with GPT-4o judge, proving pairwise format does not amplify rewriting artifacts (MF1 defense)
- **Metrics:**
  - judge: GPT-4o
  - comparison: original vs double_rewrite
  - method: BT (choix.ilsr_pairwise) + pair-level bootstrap 10000 seed=42, ALL pairs including inconsistent
  - `formality`: n_pairs=81, bt_p_original=0.4177, ci=[0.3418, 0.5], p_value=0.0368, sign_test_rate=0.3488, sign_test_n="15/43", sign_test_p=0.066, note="Sign test NS (p=0.066) but BT significant (p=0.037) — BT uses more data"
  - `verbosity`: n_pairs=43, bt_p_original=0.1668, ci=[0.0835, 0.262], p_value=0, sign_test_rate=0.0625, sign_test_n="2/32", sign_test_p=0
  - conclusion: "Rewriting artifact confirmed. GPT-4o formality BT borderline (p=0.037), verbosity extreme. BT more powerful than sign test (recovers signal from inconsistent pairs)."
- **Conclusion:** negative

### EXPERIMENT 19: `double_rewrite_placebo_qwen32b`
- **Status:** DONE
- **Hypothesis:** Pairwise comparison of original vs double-rewrite (same style, only rewriting artifact difference) yields BT ≈ 50%, proving pairwise format does not amplify rewriting artifacts (MF1 defense)
- **Metrics:**
  - judge: Qwen3-32B
  - comparison: original vs double_rewrite
  - method: BT (choix.ilsr_pairwise) + pair-level bootstrap 10000 seed=42, ALL pairs including inconsistent
  - `formality`: n_pairs=81, bt_p_original=0.3766, ci=[0.3025, 0.4506], p_value=0.0006, sign_test_rate=0.2727, sign_test_n="12/44", sign_test_p=0.0037
  - `verbosity`: n_pairs=43, bt_p_original=0.0816, ci=[0.0351, 0.1397], p_value=0, sign_test_rate=0, sign_test_n="0/36", sign_test_p=0
  - conclusion: "Rewriting artifact confirmed. Judges prefer DR over original, especially for verbosity. BT uses all pairs (matching main experiment methodology)."
- **Conclusion:** negative

### EXPERIMENT 20: `cf_vs_dr_qwen32b`
- **Status:** DONE
- **Hypothesis:** Comparing counterfactual (style-changed + artifact) vs double-rewrite (original-style + artifact) isolates pure style effect by controlling for rewriting artifact.
- **Metrics:**
  - judge: Qwen3-32B
  - comparison: counterfactual vs double_rewrite
  - `formality`: n_pairs=81, n_consistent=55, consistency=0.679, cf_win_rate=0.2, ci=[0.109, 0.309], p_value=9e-06, interpretation="DR preferred over CF — both style effect and extra artifact compound in DR's favor"
  - `verbosity`: n_pairs=43, n_consistent=39, consistency=0.907, cf_win_rate=0.333, ci=[0.18, 0.487], p_value=0.053, interpretation="DR marginally preferred (p=0.053) — artifact and style effects partially cancel in mixed-direction pairs"
- **Conclusion:** negative

### EXPERIMENT 21: `cross_axis_gradient`
- **Status:** DONE
- **Hypothesis:** NLI rejection rate serves as manipulation invasiveness proxy, with axes ordered register < formality < verbosity matching the gradient in BT and GEE Style OR
- **Metrics:**
  - axes: [
    - {axis: "register", nli_rejection_rate: 0.06, bt: 0.553, likert_d: 0.069, gee_style_or: 1.91},
    - {axis: "formality", nli_rejection_rate: 0.12, bt: 0.665, likert_d: 0.012, gee_style_or: 4.2},
    - {axis: "verbosity", nli_rejection_rate: 0.14, bt: 0.773, likert_d: -0.146, gee_style_or: 13.1}
  ]
  - note: "Qualitative gradient: register < formality < verbosity. Higher NLI rejection = more invasive manipulation = stronger detected bias."
- **Conclusion:** success

### EXPERIMENT 22: `nli_gate_ablation`
- **Status:** DONE
- **Hypothesis:** NLI gate filters content-contaminated pairs without introducing systematic bias
- **Metrics:**
  - `formality`: nli_pass={n=88, bt=0.665, ci=[0.585, 0.739], p=0.0001}, nli_fail={n=12, bt=0.417, ci=[0.167, 0.666], p=0.69, note="REVERSED - no formal preference in contaminated pairs"}, all={n=100, bt=0.635, ci=[0.56, 0.705], p=0.0001}
  - `verbosity`: nli_pass={n=86, bt=0.773, ci=[0.703, 0.843], p=0.0001}, nli_fail={n=14, bt=0.75, ci=[0.536, 0.928], p=0.006, note="Still significant - verbosity bias persists even in NLI-fail"}, all={n=100, bt=0.77, ci=[0.7, 0.835], p=0.0001}
  - interpretation: "Formality: NLI gate correctly filters contaminated pairs (NLI-fail BT reverses to 41.7%). Verbosity: bias so strong it persists in NLI-fail (75.0%). All-pairs BT close to NLI-pass BT for both axes."
- **Conclusion:** success

### EXPERIMENT 23: `verbosity_7method_sensitivity`
- **Status:** DONE
- **Hypothesis:** All 6 Likert-based statistical methods fail to detect verbosity bias while Bradley-Terry detects it
- **Metrics:**
  - n_pairs: 86, axis: verbosity, judge: Qwen3-32B, benchmark: LLMBar
  - methods:
    - paired_ttest: t=0.5163, p=0.607, d=0.056, significant=false
    - mann_whitney: U=3868, p=0.578, r=-0.046, significant=false
    - ordinal_logistic: coef=0.1592, p=0.575, OR=1.173, significant=false
    - cohens_d: d=0.036, threshold=0.2, significant=false
    - binarized_chi2: chi2=1.5512, p=0.213, OR=2.162, significant=false
    - likert_ate: ate=0.0581, p=0.691, d=0.056, ci=[-0.16, 0.27], significant=false
    - bradley_terry: p_verbose=0.7732, p_value=0.0001, ci=[0.703, 0.843], significant=true
  - summary: "6/6 Likert methods NS, only BT detects. Replicates formality attenuation pattern."
- **Conclusion:** success

### EXPERIMENT 24: `nli_gate_full_validation`
- **Status:** DONE
- **Hypothesis:** Full-coverage GPT-4o independent validation of NLI gate decisions across all 200 pairs confirms gate reliability
- **Metrics:**
  - total_evaluated: 200
  - per_axis: formality={n=100, agreement=0.88, kappa=0.47, base_rate_pass=0.88, pass_precision=0.921, fail_recall=0.583}, verbosity={n=100, agreement=0.79, kappa=0.31, base_rate_pass=0.86, pass_precision=0.826, fail_recall=0.571}
  - overall: n=200, agreement=0.835, kappa=0.38, base_rate_pass=0.87, pass_precision=0.874, fail_recall=0.577, confusion={tp=152, fp=22, tn=15, fn=11}
  - vs_spotcheck: spotcheck_agreement=0.65, full_agreement=0.835, delta_pp=18.5, note="Spot-check used 50/50 stratified sampling (inflating disagreement); full data has 87% pass rate, pulling overall agreement up via high pass precision"
  - interpretation: "NLI gate is reliable for pass decisions (precision 87-92%). Low fail recall (58%) means gate over-rejects — GPT-4o considers ~42% of NLI-fail pairs as actually preserving content. This confirms gate is CONSERVATIVE."
- **Conclusion:** success

### EXPERIMENT 25: `originality_minimal_subset`
- **Status:** DONE
- **Hypothesis:** Style effect in BT remains stable when restricting to originality-balanced pairs
- **Metrics:**
  - `formality`: full={n=88, bt=0.6647, ci=[0.585, 0.739]}, likert_balanced={n=55, bt=0.6727, ci_note="bootstrap CI from script", method="Pairs where Likert score(original) == Likert score(counterfactual)"}, delta_likert_vs_full=0.008, delta_ci=[-0.1103, 0.1261], conclusion="BT stable on originality-balanced subset (Δ=+0.008, CI includes 0)", fix="Corrected PAIRWISE_F from pairwise_results_32b.jsonl to pairwise_results_qwen32b_formality.jsonl"
  - `verbosity`: full={n=86, bt=0.7732, ci=[0.703, 0.843]}, likert_balanced={n=50, bt=0.7599, method="Pairs where Likert score(original) == Likert score(counterfactual)"}, delta_likert_vs_full=-0.0133, delta_ci=[-0.133, 0.1032], conclusion="BT stable on originality-balanced subset (Δ=-0.013, CI includes 0)"
  - note: "FIXED: formality now uses correct pairwise file (pairwise_results_qwen32b_formality.jsonl). Full BT matches canonical 0.665."
- **Conclusion:** success

### EXPERIMENT 26: `bt_model_diagnostics`
- **Status:** DONE
- **Hypothesis:** BT model adequately fits the pairwise data (GoF non-significant) and stratified BT by originality direction reveals whether style effect is confounded with originality preference
- **Metrics:**
  - gof: formality={deviance=52.8, df=45, p_value=0.198, n_consistent=46, bt_prob=0.739}, verbosity={deviance=47.96, df=62, p_value=0.905, n_consistent=63, bt_prob=0.873}
  - stratified_bt:
    - formality: orig_is_formal={n=27, bt=0.889, ci=[0.778, 1], wins=24}, orig_is_casual={n=19, bt=0.526, ci=[0.316, 0.737], wins=10}, fisher_p=0.015, chi2_p=0.006, note="Significant direction difference: orig_is_formal 88.9% vs orig_is_casual 52.6%. Confirms originality confound in formality (consistent with GEE decomposition)."
    - verbosity: orig_is_verbose={n=29, bt=0.828, ci=[0.69, 0.966], wins=24}, orig_is_concise={n=34, bt=0.912, ci=[0.794, 1], wins=31}, fisher_p=0.453, chi2_p=0.317, note="No significant direction difference. Both directions strongly prefer verbose → pure style bias confirmed."
- **Conclusion:** success

### EXPERIMENT 27: `claude_tost_equivalence`
- **Status:** DONE
- **Hypothesis:** Claude Sonnet 4 BT results are statistically equivalent to chance (P=0.5) within ±10pp margin using TOST
- **Metrics:**
  - equivalence_margin: 0.1
  - `formality`: p_hat=0.562, n=88, se=0.0375, tost_p=0.155, ci_90=[0.5, 0.624], upper_test_p=0.155, lower_test_p=0, equivalence_confirmed=false, note="90% CI upper bound 0.624 > 0.60 margin"
  - `verbosity`: p_hat=0.541, n=86, se=0.0401, tost_p=0.07, ci_90=[0.475, 0.607], upper_test_p=0.07, lower_test_p=0, equivalence_confirmed=false, note="90% CI upper bound 0.607 > 0.60 margin, marginal"
  - conclusion: "Equivalence NOT confirmed at Δ=0.10 — underpowered (n≈87), not evidence of bias. Both upper tests fail: formality p=0.155, verbosity p=0.070. If Δ=0.15, both would confirm equivalence."
  - method: "TOST for proportions (Lakens 2017), SE from pair-level bootstrap"
- **Conclusion:** negative

### EXPERIMENT 28: `nli_fn_selection_bias`
- **Status:** DONE
- **Hypothesis:** NLI gate may systematically filter pairs with larger style changes, potentially underestimating the true bias effect
- **Metrics:**
  - `formality`: n_total=355, n_pass=323, n_fail=32, pass_rate=0.91, significant_metrics="2/7 (BLEU p=0.018 d=-0.46, TF-IDF p=0.002 d=-0.62)", norm_lev_p=0.23, bleu_pass=0.361, bleu_fail=0.235, tfidf_pass=0.69, tfidf_fail=0.558, conclusion="CONSERVATIVE: fail pairs have larger style changes (lower BLEU/TF-IDF)"
  - `verbosity`: n_total=100, n_pass=39, n_fail=61, pass_rate=0.39, significant_metrics="5/7", norm_lev_pass=0.528, norm_lev_fail=0.69, norm_lev_d=0.788, tfidf_pass=0.675, tfidf_fail=0.491, tfidf_d=-0.815, conclusion="STRONGLY CONSERVATIVE: 5/7 significant, TF-IDF d=-0.815 large effect"
  - `register`: n_total=100, n_pass=80, n_fail=20, pass_rate=0.8, significant_metrics="0/7", conclusion="No significant bias detected (but n_fail=20 underpowered)"
  - overall_conclusion: "Gate selection is conservative across all axes. Measured effects are lower bounds. Verbosity strongest signal (d=0.815 large)."
  - artifacts: ["artifacts/nli_fn_bias/nli_fn_bias_formality.png", "artifacts/nli_fn_bias/nli_fn_bias_verbosity.png", "artifacts/nli_fn_bias/nli_fn_bias_register.png"]
- **Conclusion:** success

### EXPERIMENT 29: `nli_gate_spotcheck`
- **Status:** DONE
- **Hypothesis:** GPT-4o independent evaluation agrees with NLI gate pass/fail decisions at high rate
- **Metrics:**
  - total_samples: 100, pass_samples: 50, fail_samples: 50
  - overall_agreement: 0.65
  - cohens_kappa: 0.3
  - kappa_ci: [0.153, 0.456]
  - pass_agreement: 0.94
  - fail_agreement: 0.36
  - disagreement_pattern: nli_fail_gpt_pass=32, nli_pass_gpt_fail=3
  - per_axis: formality={agreement=0.771, kappa=0.241, n=48}, verbosity={agreement=0.618, kappa=0.294, n=34}, register={agreement=0.389, kappa=0.092, n=18}
  - note: "NLI gate is conservative, not rubber-stamp. 94% pass agreement. 32/35 disagreements are NLI over-reject (fail but GPT-4o says pass). Kappa=0.30 inflated by 50/50 stratified sampling; real-data agreement much higher given 88% pass rate."
- **Conclusion:** success

### EXPERIMENT 30: `gate_comparison`
- **Status:** DONE
- **Hypothesis:** Direction-aware NLI gate does not introduce systematic bias compared to strict bidirectional gate
- **Metrics:**
  - `formality`: strict={n=88, bt=0.6647, ci=[0.5852, 0.7386], p=0.0001}, direction_aware={n=97, bt=0.634, ci=[0.5567, 0.7061], p=0.0001}, extra_only={n=9, bt=0.3337}, delta=-0.0307, delta_ci=[-0.0651, -0.0018], significant=true, note="Formality pipeline already uses strict gate (min). Extra 9 pairs lean casual. Moot for paper."
  - `verbosity`: strict={n=65, bt=0.7845, ci=[0.7076, 0.8537], p=0.0001}, direction_aware={n=86, bt=0.7732, ci=[0.7034, 0.8429], p=0.0001}, extra_only={n=21, bt=0.7379}, delta=-0.0113, delta_ci=[-0.0564, 0.0296], significant=false, note="No systematic difference. Extra 21 pairs consistent with overall direction (73.8% vs 77.3%)."
- **Conclusion:** success

### EXPERIMENT 31: `exp-006`
- **Status:** DONE
- **Hypothesis:** Scaling formality counterfactual generation from 100 to 400 pairs enables cross-benchmark validation and increases statistical power
- **Metrics:**
  - n_total: 400
  - nli_pass: 355
  - nli_rate: 0.888
  - bt: p_formal=0.675, ci=[0.637, 0.713], ci_width_pp=7.6, p_value=0.0001
  - likert: ate=-0.059, p=0.5999, d=-0.025, tie_rate=0.434, mean_formal=6.58, mean_casual=6.64
  - gee: style_or=2.15, style_ci=[1.46, 3.16], style_p=0.0001, orig_or=4.99, orig_ci=[3.4, 7.34], orig_p=0.0001
  - blindspot: True
  - consistency: 0.654
  - vs_n100: bt_delta="+1.0pp (67.5 vs 66.5)", ci_improvement="2x narrower (7.6pp vs 15.4pp)"
- **Conclusion:** success

### EXPERIMENT 32: `alpacaeval_verbosity_qwen32b`
- **Status:** DONE
- **Hypothesis:** Qwen3-32B shows verbosity Blindspot on AlpacaEval benchmark
- **Metrics:**
  - bt: p_verbose=0.841, ci=[0.774, 0.902], p_value=0.0001
  - likert: ate=0.732, p=0.0003, d=0.375, tie_rate=0.244, mean_verbose=7.32, mean_concise=6.59
  - gee: style_or=28.64, style_ci=[9.16, 89.56], style_p=0.0001, orig_or=0.18, orig_ci=[0.06, 0.54], orig_p=0.0024
  - blindspot: False
  - n_pairs: 82
  - consistency: 0.829
  - note: "NOT Blindspot: Likert p=0.0003 also significant. Effect is so strong (d=0.375) that even Likert detects it. GEE Style OR=28.64 is massive."
- **Conclusion:** success

### EXPERIMENT 33: `correction_poc`
- **Status:** DONE
- **Hypothesis:** Explicit style-awareness debiasing instructions in judge prompts can eliminate or substantially reduce formality style bias
- **Metrics:**
  - `qwen32b`: original={p_formal=0.665, ci=[0.585, 0.739], p_value=0.0001}, debiased={p_formal=0.608, ci=[0.534, 0.682], p_value=0.0023}, reduction_pp=5.7, reduction_pct=34.5
  - `gpt4o`: original={p_formal=0.63, ci=[0.557, 0.703], p_value=0.0004}, debiased={p_formal=0.626, ci=[0.559, 0.693], p_value=0.0001}, reduction_pp=0.4, reduction_pct=3.1, neither_count=5
  - conclusion: "Debiased prompt ineffective. Qwen3-32B: -5.7pp but still p=0.002. GPT-4o: -0.4pp, no change. Style bias persists despite explicit debiasing instructions."
- **Conclusion:** negative

### EXPERIMENT 34: `claude_verbosity`
- **Status:** DONE
- **Hypothesis:** Claude Sonnet 4 shows verbosity style bias similar to GPT-4o (OR=10-13) and Qwen3-32B
- **Metrics:**
  - bt: p_verbose=0.541, ci=[0.459, 0.616], p_value=0.284
  - likert: ate=-0.081, p=0.7427, d=-0.039, tie_rate=0.674
  - gee: style_or=1.52, style_p=0.2858, orig_or=0.8, orig_p=0.5626
  - blindspot: False
  - n_pairs: 86
- **Conclusion:** negative

### EXPERIMENT 35: `claude_formality`
- **Status:** DONE
- **Hypothesis:** Claude Sonnet 4 shows similar formality style bias as GPT-4o and Qwen3-32B
- **Metrics:**
  - bt: p_formal=0.562, ci=[0.489, 0.636], p_value=0.0912
  - likert: ate=-0.045, p=0.7207, d=-0.021, tie_rate=0.682
  - gee: style_or=1.47, style_p=0.2757, orig_or=6.66, orig_p=0.0001
  - blindspot: False
  - n_pairs: 88
- **Conclusion:** negative

### EXPERIMENT 36: `gpt4o_alpacaeval`
- **Status:** DONE
- **Hypothesis:** GPT-4o shows formality Blindspot on AlpacaEval benchmark
- **Metrics:**
  - bt: p_formal=0.727, ci=[0.663, 0.785], p_value=0.0001
  - likert: ate=0.128, p=0.1704, d=0.148, tie_rate=0.663
  - gee: style_or=4.91, style_p=0.0001, orig_or=1.99, orig_p=0.0356
  - blindspot: True
  - n_pairs: 86
- **Conclusion:** success

### EXPERIMENT 37: `gpt4o_mtbench`
- **Status:** DONE
- **Hypothesis:** GPT-4o shows formality Blindspot on MT-Bench benchmark
- **Metrics:**
  - bt: p_formal=0.692, ci=[0.623, 0.753], p_value=0.0001
  - likert: ate=0.164, p=0.0163, d=0.167, tie_rate=0.699
  - gee: style_or=2.28, style_p=0.1055, orig_or=6.24, orig_p=0.0005
  - blindspot: False
  - n_pairs: 73
  - note: "Likert also significant p=0.016 but d=0.167 small; BT much stronger p<0.0001. NOT Blindspot because Likert is also significant."
- **Conclusion:** success

### EXPERIMENT 38: `qwen32b_register`
- **Status:** DONE
- **Hypothesis:** Qwen3-32B judge shows register (academic/conversational) bias in pairwise comparison while Likert fails to detect it
- **Metrics:**
  - pairwise: consistency_rate=0.6, academic_win_rate=0.593, sign_test_p=0.22, wilson_ci=[0.46, 0.713]
  - likert: ate=0.074, p=0.505, cohens_d=0.069, tie_rate=0.638
  - direction: academic_to_conv_orig_pref=0.893, academic_to_conv_p=2.7e-05, conv_to_academic_orig_pref=0.312, conv_to_academic_p=0.05
  - blindspot_confirmed: False
  - bt: p_academic_wins=0.553, bootstrap_ci=[0.479, 0.628], bootstrap_p=0.0763, bootstrap_method="pair-level (10000 iterations, seed=42)", n_pairs=94, n_comparisons=188
  - gee_decomposition: academic_or=1.9053, academic_ci=[1.01, 3.58], academic_p=0.0455, originality_or=5.7181, originality_p=0.0001, note="Register significant after controlling for originality bias (OR=1.91 p=0.046). Originality dominant (OR=5.72)."
  - status_note: "BT P(academic)=55.3% [47.9%, 62.8%] p=0.076 (NS). GEE academic OR=1.91 p=0.046 (significant after controlling originality). Originality dominant."
- **Conclusion:** success

### EXPERIMENT 39: `gpt4o_register`
- **Status:** DONE
- **Hypothesis:** GPT-4o judge shows register (academic/conversational) bias detectable via pairwise but not Likert
- **Metrics:**
  - pairwise: academic_win_rate=0.633, sign_test_p=0.085
  - likert: ate=0, p_wilcoxon=0.7849, cohens_d=0, tie_rate=0.6489
  - bt: p_academic_wins=0.5699, bootstrap_ci=[0.5, 0.6398], bootstrap_p=0.04, bootstrap_method="pair-level (10000 iterations, seed=42)"
  - gee_decomposition: academic_or=1.8759, academic_p=0.0285, originality_or=2.2098, originality_p=0.0058, note="Style marginally significant (OR=1.88 p=0.03), originality stronger (OR=2.21 p=0.006). Pattern consistent with Qwen3-32B register."
  - blindspot_confirmed: True
  - status_note: "BT P(academic)=57.0% [50.0%, 64.0%] p=0.04; Likert ATE=0 p=0.78 (Blindspot confirmed). GEE academic OR=1.88 p=0.03, orig OR=2.21 p=0.006."
- **Conclusion:** success

### EXPERIMENT 40: `gpt4o_verbosity`
- **Status:** DONE
- **Hypothesis:** GPT-4o judge shows verbosity bias in pairwise comparison while Likert fails to detect it
- **Metrics:**
  - pairwise: verbose_win_rate=0.863, sign_test_p=1e-06, wilson_ci=[0.766, 0.924]
  - likert: ate=0.1163, p_wilcoxon=0.4033, cohens_d=0.078, tie_rate=0.5814
  - bt: p_verbose_wins=0.7602, bootstrap_ci=[0.6881, 0.8283], bootstrap_p=0.0001, bootstrap_method="pair-level (10000 iterations, seed=42)"
  - gee_decomposition: verbose_or=10.9719, verbose_p=0.0001, originality_or=0.4373, originality_p=0.0514, note="Pure style bias (OR=10.97 p<0.0001). Originality not significant and in opposite direction (OR=0.44)."
  - blindspot_confirmed: True
  - status_note: "BT P(verbose)=76.0% [68.8%, 82.8%] p=0.0001; Likert ATE=+0.12 p=0.40 (Blindspot confirmed). GEE verbose OR=10.97 p<0.0001, orig OR=0.44 ns."
- **Conclusion:** success

### EXPERIMENT 41: `qwen32b_verbosity`
- **Status:** DONE
- **Hypothesis:** Qwen3-32B judge shows verbosity bias in pairwise comparison (verbose win rate >60%, p<0.05) while Likert scoring fails to detect it
- **Metrics:**
  - pairwise: consistency_rate=0.74, verbose_win_rate=0.873, sign_test_p=1e-06, wilson_ci=[0.769, 0.934]
  - likert: ate=-0.151, p=0.179, cohens_d=-0.146, tie_rate=0.581
  - direction: verbose_to_concise_orig_pref=0.806, verbose_to_concise_p=0.000878, concise_to_verbose_rewrite_pref=0.907, concise_to_verbose_p=1e-06
  - note: "Strongest bias: 87.3% verbose win (p<10⁻⁶) but Likert p=0.179. Both directions prefer verbose content (not originality bias)."
  - blindspot_confirmed: True
  - bt: p_verbose_wins=0.7732, bootstrap_ci=[0.7034, 0.8429], bootstrap_p=0.0001, bootstrap_method="pair-level (10000 iterations, seed=42)"
  - gee_decomposition: verbose_or=13.1, verbose_ci=[5.62, 30.55], verbose_p=2.6e-09, originality_or=0.49, originality_ci=[0.21, 1.14], originality_p=0.096, note="Verbosity bias entirely style-driven (OR=13.10 p<10⁻⁹). Originality non-significant and in opposite direction (OR=0.49)."
  - status_note: "BT P(verbose)=77.3% [70.3%, 84.3%] p<0.0001; GEE verbose OR=13.10 p<10⁻⁹, originality OR=0.49 ns. Purest style bias across all cells."
- **Conclusion:** success

### EXPERIMENT 42: `qwen32b_formality`
- **Status:** DONE
- **Hypothesis:** Qwen3-32B as local judge will show similar formality bias pattern to GPT-4o
- **Metrics:**
  - pairwise: consistency_rate=0.65, formal_win_rate=0.764, sign_test_p=0.000114, wilson_ci=[0.637, 0.856]
  - likert: ate=0.011, p=0.908, cohens_d=0.012, tie_rate=0.727
  - direction: formal_to_casual_win=0.814, formal_to_casual_p=4.2e-05, casual_to_formal_win=0.5, casual_to_formal_p=1
  - vs_gpt4o: "pairwise 76.4% vs 63.0% (stronger); Likert both non-sig (p=0.908 vs p=0.332)"
  - blindspot_confirmed: True
  - bt: p_formal_wins=0.6647, bootstrap_ci=[0.5852, 0.7386], bootstrap_p=0.0001, bootstrap_method="pair-level (10000 iterations, seed=42)"
  - gee_decomposition: formal_or=4.2008, formal_p=0.0002, originality_or=4.7041, originality_p=0.0001, note="Both effects strong and nearly equal magnitude; casual→formal at 50% confirms originality confound"
  - status_note: "BT P(formal)=66.5% [58.5%, 73.9%] p<0.0001; GEE formal OR=4.20 p=0.0002, originality OR=4.70 p<0.0001"
- **Conclusion:** success

### EXPERIMENT 43: `exp016_bradley_terry`
- **Status:** DONE
- **Hypothesis:** Bradley-Terry model on ALL pairwise data (no consistency filtering) will confirm formal preference is significant
- **Metrics:**
  - primary_nli_filtered: n_pairs=88, n_comparisons=173, p_formal_wins=0.63, bootstrap_ci=[0.5575, 0.7028], bootstrap_p=0.0004, bootstrap_method="pair-level (2000 iterations, seed=42)", ci_excludes_50=true
  - robustness_all_data: n_pairs=100, n_comparisons=197, p_formal_wins=0.6091, bootstrap_ci=[0.5381, 0.6784], bootstrap_p=0.001, bootstrap_method="pair-level (2000 iterations, seed=42)", ci_excludes_50=true
  - comparison_level_reference: all_data_ci=[0.5381, 0.6751], nli_filtered_ci=[0.5607, 0.6994], note="Pair-level CIs ~2-5% wider than comparison-level, conclusions unchanged"
  - comparison_to_sign_test: "BT NLI-filtered 63.0% [55.8-70.3%] p<0.001 vs sign test 69.1% [56.0-79.7%] p=0.006"
- **Conclusion:** success

### EXPERIMENT 44: `verbosity_32b`
- **Status:** DONE
- **Hypothesis:** Verbosity axis (verbose/concise) produces stronger style bias signal than formality in GPT-4o judge
- **Metrics:**
  - n: 100
  - h1_nli_pass_rate: 0.65
  - nli_mean: 0.6544
  - bertscore_pass_rate: 0.27
  - bertscore_mean: 0.7522
  - both_pass: 0.22
  - dr_nli_mean: 0.4847
  - dr_bertscore_mean: 0.7199
  - dr_pass_rate: 0.04
  - stopped_at: scoring
  - stop_reason: "API 402 Insufficient balance"
  - v2_direction_aware_nli: nli_ge90=0.86, nli_ge80=0.86, nli_ge95=0.83, forward_n=46, forward_nli_mean=0.9476, backward_n=54, backward_nli_mean=0.8267, nli_only_pass_rate_at_090=0.86, h1_status="PASS (86% >= 80%)", pipeline_blocked_at="scoring (API 402, D013 approved NLI-only gate)"
  - status_note: "H1 PASS (direction-aware NLI 86%). Scoring/H2 deferred to separate experiment when API available."
- **Conclusion:** success

### EXPERIMENT 45: `exp-016` (DUPLICATE)
- **Status:** DONE
- **Metrics:** DUPLICATE: canonical entry is exp016_bradley_terry. This entry should be ignored.
- **Conclusion:** killed

### EXPERIMENT 46: `exp-015` (DUPLICATE)
- **Status:** DONE
- **Metrics:** DUPLICATE: canonical entry is exp015_clmm. This entry should be ignored.
- **Conclusion:** killed

### EXPERIMENT 47: `exp015_clmm`
- **Status:** DONE
- **Hypothesis:** Ordinal regression (CLMM) respecting Likert measurement level will also fail to detect formality effect (p>0.05), confirming that the Likert Blindspot is not an artifact of treating ordinal data as continuous
- **Metrics:**
  - ordinal_regression: is_formal_coef=-0.079, is_formal_p=0.769, is_formal_ci=[-0.6, 0.45]
  - gee_paired: is_formal_coef=-0.084, is_formal_p=0.587, is_formal_ci=[-0.39, 0.22]
  - wilcoxon: p=0.905
  - n_pairs: 88
  - n_ties: 55
  - tie_rate: 0.625
  - conclusion_note: "All three methods (ordinal LR, GEE, Wilcoxon) confirm Likert Blindspot: p=0.77/0.59/0.91. 62.5% ties eliminate statistical power."
- **Conclusion:** success

### EXPERIMENT 48: `exp013_nli_validation`
- **Status:** DONE
- **Hypothesis:** NLI gate (DeBERTa-v3-large, threshold 0.90) decisions are reliable proxies for human content-preservation judgments, achieving Cohen's kappa >= 0.6 with LLM-as-annotator (Qwen3-32B)
- **Metrics:**
  - cohens_kappa: 0.4304
  - pabak: 0.82
  - gwet_ac1: 0.8934
  - agreement_rate: 0.91
  - n_samples: 100
  - n_nli_pass: 88
  - n_nli_fail: 12
  - precision: 0.989
  - recall: 0.916
  - confusion_matrix: nli_pass_llm_yes=87, nli_pass_llm_no=1, nli_fail_llm_yes=8, nli_fail_llm_no=4
  - direction_bias: overall_f2c_ratio=0.59, nli_fail_f2c_ratio=0.75, fn_f2c_ratio=0.75, fisher_or=0.44, fisher_p=0.35, binomial_fn_p=0.295, conclusion="not significant (all p>0.20, n=8/12 too small)"
  - kappa_paradox_note: "kappa=0.43 vs PABAK=0.82 vs AC1=0.89 — classic prevalence paradox (Feinstein & Cicchetti 1990, Gwet 2008). Base rate 88:12 skew depresses kappa despite 91% raw agreement."
  - interpretation: "NLI gate is precision-oriented conservative filter. AC1=0.89 confirms strong agreement. No significant direction bias in FN."
  - method: "LLM-as-annotator validation (Qwen3-32B)"
- **Conclusion:** success

### EXPERIMENT 49: `exp-013` (DUPLICATE)
- **Status:** DONE
- **Metrics:** DUPLICATE: canonical entry is exp013_nli_validation. This entry should be ignored.
- **Conclusion:** killed

### EXPERIMENT 50: `register_pilot`
- **Status:** DONE
- **Hypothesis:** Register axis (academic/conversational) RATE counterfactuals preserve content (NLI+BERTScore pass rate >=80%) and register is independent from formality (agreement <=95%)
- **Metrics:**
  - n_samples: 20
  - cf_pass_rate_joint: 0.2
  - cf_pass_rate_nli_only: 0.95
  - cf_pass_rate_bs_only: 0.2
  - nli_cf_mean: high (19/20 >= 0.90)
  - bertscore_cf_mean: 0.8458
  - bertscore_threshold: 0.92
  - register_formality_agreement: 0.5
  - bs_sweep_0.80: 0.75
  - bs_sweep_0.84: 0.6
  - bs_sweep_0.88: 0.4
  - bs_sweep_0.92: 0.2
  - conclusion_note: "FAIL with joint gate (20%), PASS with NLI-only (95%). BERTScore sole bottleneck. Register-Formality 50% = orthogonal."
- **Conclusion:** negative

### EXPERIMENT 51: `exp014_logistic_decomposition`
- **Status:** DONE
- **Hypothesis:** The observed 69.1% formal win rate in pairwise comparison is primarily driven by original-preference bias rather than genuine formality effect
- **Metrics:**
  - method_note: "CORRECTED: pair-level bootstrap + GEE (fixes independence violation)"
  - pair_bootstrap: formal_effect_coef=0.7928, formal_effect_OR=2.2095, formal_effect_OR_ci=[1.228, 4.305], formal_effect_p=0.0121, original_effect_coef=0.5958, original_effect_OR=1.8145, original_effect_OR_ci=[0.976, 3.369], original_effect_p=0.0643
  - gee_exchangeable: formal_effect_coef=0.7931, formal_effect_OR=2.2103, formal_effect_OR_ci=[1.21, 4.038], formal_effect_p=0.0099, original_effect_coef=0.5973, original_effect_OR=1.8172, original_effect_OR_ci=[0.995, 3.319], original_effect_p=0.052
  - direction_subset: formal_to_casual_win_rate=0.788, formal_to_casual_p=0.001319, casual_to_formal_win_rate=0.545, casual_to_formal_p=0.831812
  - intercept_position_bias: -0.5851
  - n_pairs: 98
  - n_observations: 196
  - old_observation_bootstrap_note: "SUPERSEDED: old p=0.011/0.048 used observation-level bootstrap, understated SE"
- **Conclusion:** success

### EXPERIMENT 52: `exp012_consistency_bias`
- **Status:** DONE
- **Hypothesis:** The consistency filter (discarding 43% of pairs) introduces systematic selection bias
- **Metrics:**
  - consistent_n: 55
  - inconsistent_n: 43
  - consistency_rate: 0.561
  - nli_mwu_p: 0.824
  - bertscore_mwu_p: 0.12
  - orig_length_mwu_p: 0.137
  - length_diff_mwu_p: 0.715
  - nli_ks_p: 0.68
  - conclusion_note: "No systematic bias detected in consistency filter (all p>0.12)"
- **Conclusion:** success

### EXPERIMENT 53: `exp011_nli_sensitivity`
- **Status:** DONE
- **Hypothesis:** The 0.90 NLI threshold is on a cliff edge where small changes dramatically affect pass rate and downstream pairwise results
- **Metrics:**
  - formality_pass_rate_0.70: 0.89
  - formality_pass_rate_0.90: 0.88
  - formality_pass_rate_0.95: 0.85
  - pw_win_rate_0.70: 0.723
  - pw_win_rate_0.90: 0.739
  - pw_p_0.70: 0.0031
  - pw_p_0.90: 0.0016
  - nli_mean: 0.8956
  - nli_std: 0.2792
  - tone_pass_rate_0.70: 0.65
  - conclusion_note: "NLI bimodal distribution, 0.90 NOT on cliff edge, pairwise results robust across all thresholds"
- **Conclusion:** success

### EXPERIMENT 54: `exp010_binarized_likert`
- **Status:** DONE
- **Hypothesis:** Likert-vs-Pairwise sensitivity gap is due to measurement structure (forced choice eliminates ties) not statistical test choice; binarized Likert with sign test will remain non-significant
- **Conclusion:** success
- **Metrics:** Not explicitly listed in the entry beyond the hypothesis (data in checkpoint file `/root/causal_style_decomp_judge/data/exp010_results/exp010_binarized_likert.csv`)

### EXPERIMENT 55: `tone_pilot`
- **Status:** DONE
- **Hypothesis:** Tone axis (assertive/hedging) RATE counterfactuals preserve content (NLI+BERTScore pass rate >=80%)
- **Metrics:**
  - n: 20
  - detection_split: assertive=13, hedging=7
  - nli_cf_pass_rate: 0.65
  - bertscore_cf_pass_rate: 0.6
  - both_pass_rate: 0.45
  - nli_cf_mean: 0.7039
  - nli_cf_std: 0.4208
  - bertscore_cf_mean: 0.9201
  - nli_dr_mean: 0.8841
  - bertscore_dr_mean: 0.9164
  - by_tone: assertive={n=13, both_pass=0.385, nli_cf_mean=0.6559}, hedging={n=7, both_pass=0.571, nli_cf_mean=0.793}
  - failure_mode: "assertive→hedging changes epistemic commitment, NLI correctly detects non-entailment (6/20 catastrophic NLI<0.01)"
- **Conclusion:** negative

### EXPERIMENT 56: `pairwise_32b`
- **Status:** DONE
- **Hypothesis:** Likert 1-10 integer granularity masks a real formality preference in GPT-4o; position-controlled pairwise comparison reveals significant formal win rate >55% where Likert ATE was non-significant
- **Metrics:**
  - n_total: 100
  - n_valid_both_trials: 98
  - n_consistent: 55
  - n_ties_inconsistent: 43
  - consistency_rate: 0.5612
  - formal_wins: 38
  - casual_wins: 17
  - formal_win_rate: 0.6909
  - wilson_ci_lo: 0.5597
  - wilson_ci_hi: 0.7972
  - sign_test_p: 0.006456
  - position_bias_trial1_A: 0.5306
  - position_bias_trial2_A: 0.551
  - position_bias_overall_A: 0.5408
  - dir_formal_orig_n: 33
  - dir_formal_orig_formal_wins: 26
  - dir_formal_orig_win_rate: 0.7879
  - dir_formal_orig_p: 0.001145
  - dir_casual_orig_n: 22
  - dir_casual_orig_formal_wins: 12
  - dir_casual_orig_win_rate: 0.5455
  - dir_casual_orig_p: 0.8318
  - nli_ge90_n: 46
  - nli_ge90_formal_wins: 34
  - nli_ge90_win_rate: 0.7391
  - nli_ge90_p: 0.001537
- **Conclusion:** success

### EXPERIMENT 57: `mvp_32b_ate`
- **Status:** DONE
- **Hypothesis:** Qwen3-32B (stronger instruction following than 8B) produces higher-fidelity RATE counterfactuals with lower rewrite bias, revealing significant formality premium
- **Metrics:**
  - n: 100
  - n_primary: 88
  - h1_nli_pass_rate: 0.88
  - nli_mean: 0.8956
  - raw_ate: -0.1023
  - raw_se: 0.149
  - raw_p: 0.4944
  - raw_cohens_d: -0.0731
  - rewrite_bias: -0.2045
  - corrected_ate: 0.1023
  - corrected_se: 0.1048
  - corrected_p: 0.3318
  - corrected_cohens_d: 0.104
  - rate_ratio: -1
  - dir_formal_to_casual_ate: 0.14
  - dir_formal_to_casual_p: 0.332
  - dir_casual_to_formal_ate: 0.0526
  - dir_casual_to_formal_p: 0.7365
  - sens2_corrected_ate: 0.0959
  - sens2_corrected_p: 0.3633
  - all_corrected_ate: 0.1
  - all_corrected_p: 0.2995
- **Conclusion:** negative

### EXPERIMENT 58: `mvp_8b_ate`
- **Status:** DONE
- **Hypothesis:** Binary style counterfactuals (formality axis) via Qwen3-8B RATE double-rewrite reveal significant ATE in GPT-4o judge scores, with formal text receiving higher scores
- **Metrics:**
  - n: 100
  - h1_nli_pass_rate: 0.95
  - raw_ate: -0.08
  - raw_se: 0.1161
  - raw_p: 0.4923
  - raw_cohens_d: -0.0689
  - rewrite_bias: -0.2
  - corrected_ate: 0.12
  - corrected_se: 0.1028
  - corrected_p: 0.2458
  - corrected_cohens_d: 0.1168
  - rate_ratio: -1.5
  - dir_formal_to_casual_ate: 0.0645
  - dir_formal_to_casual_p: 0.5679
  - dir_casual_to_formal_ate: 0.2105
  - dir_casual_to_formal_p: 0.2997
  - strat_nli90_ate: 0.1263
  - strat_nli90_p: 0.2459
  - strat_nli90_n: 95
- **Conclusion:** negative

---

### Summary Statistics
- **Total experiments:** 58
- **3 duplicates** (exp-016, exp-015, exp-013) marked as "should be ignored" pointing to canonical entries
- **Conclusion breakdown:** success=36, negative=13, killed=6 (3 duplicates + register_100_cf + 2 others)
- **Experiments with blindspot=True:** llama70b_third_judge (both axes), gemini_flash_fourth_judge (both axes), qwen32b_formality, qwen32b_verbosity, gpt4o_verbosity, gpt4o_register, exp-006, formality_llama_rewriter, gpt4o_rewriter_verbosity, gpt4o_rewriter_formality, gpt4o_alpacaeval, llama70b_register, finegrained_likert_100pt (both axes)
- **Experiments with blindspot=False:** llama70b_crossbench (AlpacaEval/MTBench — effects too strong), crossbench_alpacaeval_verbosity (d=0.407 too strong), claude_formality, claude_verbosity (no bias detected at all), alpacaeval_verbosity_qwen32b (effect too strong), gpt4o_mtbench (Likert also significant)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdb5a1b8-fea2-4264-9aa1-99906a7fde48",
  "isSidechain": true,
  "agentId": "a5fd80952fb015e5f",
  "requestId": "req_011CbPrqPnKoGibfw4SGW8Mn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e55fd200-4f3b-4dfa-808b-71d72f675ed1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "sessionId": "34b1c8fb-c53e-47b8-bef7-53d80c2bd748",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y1zthmwFJvhKnBdCg85x9X",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2671,
      "cache_read_input_tokens": 57739,
      "output_tokens": 20073,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2671
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 20073,
          "cache_read_input_tokens": 57739,
          "cache_creation_input_tokens": 2671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2671,
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
