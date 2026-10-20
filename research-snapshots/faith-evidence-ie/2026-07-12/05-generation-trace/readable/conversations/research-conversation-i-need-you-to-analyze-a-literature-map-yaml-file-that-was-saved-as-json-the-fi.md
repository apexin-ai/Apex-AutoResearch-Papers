# Research conversation: I need you to analyze a literature_map.yaml file that was saved as JSON. The file is at: /home/ubuntu/.claude-account-1/

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a4b1818a3cd108cba.jsonl`
- **Structured JSON:** [`73f7ff621f9c0b6970de.json`](../../sessions/73/73f7ff621f9c0b6970de.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

34 recorded events

### User

_source line 1 · 2026-05-18T20:13:40.722Z_

I need you to analyze a literature_map.yaml file that was saved as JSON. The file is at:
/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/d1967b82-9b64-485b-8419-ac1a11ebeb1d/tool-results/mcp-agent-ml-research-read_project_file-1779135207105.txt

It's JSON with schema: {result: string} where result contains the YAML content as a string.

I need you to find:

1. **All papers with role "direct-competitor"** — list their title, venue, year, and any notes about rejection sampling / selection strategy ablations.

2. **All papers that discuss rejection sampling, RSFT, or scored/random selection strategies** — regardless of role. Look for keywords like "rejection sampling", "RSFT", "best-of-n", "scored selection", "random selection", "selection strategy" in titles, abstracts, notes, or relevance fields.

3. **All papers that discuss GRPO (Group Relative Policy Optimization)** or reinforcement learning for IE/NLP structured tasks — look for "GRPO", "group relative policy", "reinforcement learning" + "information extraction" or "relation extraction".

4. **All papers about learning curves or training dynamics of RL methods on NLP tasks**.

For each found paper, extract: title, venue, year, role, and the relevant text snippet that matched.

Please be thorough — read the full content, don't just sample. Report your findings in a structured format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "00163f99-7857-4276-afc6-24e9276d86ac",
  "agentId": "a4b1818a3cd108cba",
  "type": "user",
  "uuid": "4f7bad8e-f60a-4864-a201-b6f5df88fcea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T20:13:40.728Z_

```json
{
  "parentUuid": "4f7bad8e-f60a-4864-a201-b6f5df88fcea",
  "isSidechain": true,
  "agentId": "a4b1818a3cd108cba",
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
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
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
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "d03076e1-2199-474f-9807-2bb83bcdba7d",
  "timestamp": "2026-05-18T20:13:40.728Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T20:13:43.284Z_



I'll start by reading the file to get the full content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d03076e1-2199-474f-9807-2bb83bcdba7d",
  "isSidechain": true,
  "agentId": "a4b1818a3cd108cba",
  "requestId": "req_011CbAeRXnB1vZmCT1UJRP7W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9ec5a4a-954f-4f63-a5d4-2b2fc176c75e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SLLG3puWgWp1tN11iFbVtY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15968,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15968,
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

_source line 4 · 2026-05-18T20:13:44.010Z_

<details open><summary>🔧 Tool call — Read · `toolu_0111Ygga9RMeEGNneTCerf6t`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/d1967b82-9b64-485b-8419-ac1a11ebeb1d/tool-results/mcp-agent-ml-research-read_project_file-1779135207105.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9ec5a4a-954f-4f63-a5d4-2b2fc176c75e",
  "isSidechain": true,
  "agentId": "a4b1818a3cd108cba",
  "requestId": "req_011CbAeRXnB1vZmCT1UJRP7W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c33574a7-a5e0-4fe4-9d23-7598830bfa26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SLLG3puWgWp1tN11iFbVtY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15968,
      "cache_read_input_tokens": 0,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15968
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 158,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15968,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15968,
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

_source line 5 · 2026-05-18T20:13:44.311Z_

<details><summary>↩ Tool result · reported error · `toolu_0111Ygga9RMeEGNneTCerf6t`</summary>

```text
File content (51633 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c33574a7-a5e0-4fe4-9d23-7598830bfa26",
  "isSidechain": true,
  "promptId": "00163f99-7857-4276-afc6-24e9276d86ac",
  "agentId": "a4b1818a3cd108cba",
  "type": "user",
  "uuid": "0da33c88-ea19-420a-9f6f-b243c5aefc6f",
  "toolUseResult": "Error: File content (51633 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "c33574a7-a5e0-4fe4-9d23-7598830bfa26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-18T20:13:46.551Z_

The file is very large. Let me read it in chunks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0da33c88-ea19-420a-9f6f-b243c5aefc6f",
  "isSidechain": true,
  "agentId": "a4b1818a3cd108cba",
  "requestId": "req_011CbAeRo3SpkMVPfQXdTK2E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00e1a466-d00e-418b-a973-8644f6a08d23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8jygvFFzEjqLFtpvQs3ub",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1060,
      "cache_read_input_tokens": 15968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1060,
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

_source line 7 · 2026-05-18T20:13:47.502Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Bt7eWgNNx6dKhDQcGfssSg`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/d1967b82-9b64-485b-8419-ac1a11ebeb1d/tool-results/mcp-agent-ml-research-read_project_file-1779135207105.txt",
  "limit": 500,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00e1a466-d00e-418b-a973-8644f6a08d23",
  "isSidechain": true,
  "agentId": "a4b1818a3cd108cba",
  "requestId": "req_011CbAeRo3SpkMVPfQXdTK2E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9aece30a-aa3e-46d0-b227-8c6c988abd14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8jygvFFzEjqLFtpvQs3ub",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1060,
      "cache_read_input_tokens": 15968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1060,
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

_source line 8 · 2026-05-18T20:13:48.028Z_

<details><summary>↩ Tool result · reported error · `toolu_01Bt7eWgNNx6dKhDQcGfssSg`</summary>

```text
File content (51633 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9aece30a-aa3e-46d0-b227-8c6c988abd14",
  "isSidechain": true,
  "promptId": "00163f99-7857-4276-afc6-24e9276d86ac",
  "agentId": "a4b1818a3cd108cba",
  "type": "user",
  "uuid": "aa66836f-0822-4081-9fb4-3a78944c7aea",
  "toolUseResult": "Error: File content (51633 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "9aece30a-aa3e-46d0-b227-8c6c988abd14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T20:13:48.942Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Dvv46TASWPMrwNLaAqCBeo`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/d1967b82-9b64-485b-8419-ac1a11ebeb1d/tool-results/mcp-agent-ml-research-read_project_file-1779135207105.txt",
  "limit": 500,
  "offset": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa66836f-0822-4081-9fb4-3a78944c7aea",
  "isSidechain": true,
  "agentId": "a4b1818a3cd108cba",
  "requestId": "req_011CbAeRo3SpkMVPfQXdTK2E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2451ca8-d3a3-4686-8337-6441c6bf9978",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8jygvFFzEjqLFtpvQs3ub",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1060,
      "cache_read_input_tokens": 15968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1060,
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

_source line 10 · 2026-05-18T20:13:48.953Z_

<details><summary>↩ Tool result · `toolu_01Dvv46TASWPMrwNLaAqCBeo`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (500). The file has 1 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2451ca8-d3a3-4686-8337-6441c6bf9978",
  "isSidechain": true,
  "promptId": "00163f99-7857-4276-afc6-24e9276d86ac",
  "agentId": "a4b1818a3cd108cba",
  "type": "user",
  "uuid": "c7b98bfa-0b8c-45dc-987b-80c3e16e2696",
  "sourceToolAssistantUUID": "a2451ca8-d3a3-4686-8337-6441c6bf9978",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T20:13:49.887Z_

<details open><summary>🔧 Tool call — Read · `toolu_012N2DKuYfsfpPZ2yZiikJB2`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/d1967b82-9b64-485b-8419-ac1a11ebeb1d/tool-results/mcp-agent-ml-research-read_project_file-1779135207105.txt",
  "limit": 500,
  "offset": 1000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7b98bfa-0b8c-45dc-987b-80c3e16e2696",
  "isSidechain": true,
  "agentId": "a4b1818a3cd108cba",
  "requestId": "req_011CbAeRo3SpkMVPfQXdTK2E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1d23fac-4c71-4109-8008-7c843ea0b384",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8jygvFFzEjqLFtpvQs3ub",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1060,
      "cache_read_input_tokens": 15968,
      "output_tokens": 521,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1060
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 521,
          "cache_read_input_tokens": 15968,
          "cache_creation_input_tokens": 1060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1060,
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

_source line 12 · 2026-05-18T20:13:49.894Z_

<details><summary>↩ Tool result · `toolu_012N2DKuYfsfpPZ2yZiikJB2`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1000). The file has 1 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1d23fac-4c71-4109-8008-7c843ea0b384",
  "isSidechain": true,
  "promptId": "00163f99-7857-4276-afc6-24e9276d86ac",
  "agentId": "a4b1818a3cd108cba",
  "type": "user",
  "uuid": "f47b54d7-54b2-4cb5-9ece-71891648fa88",
  "sourceToolAssistantUUID": "a1d23fac-4c71-4109-8008-7c843ea0b384",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-18T20:13:52.909Z_

The file is a single very long line (JSON). Let me use grep to search for relevant content and also use bash to parse it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f47b54d7-54b2-4cb5-9ece-71891648fa88",
  "isSidechain": true,
  "agentId": "a4b1818a3cd108cba",
  "requestId": "req_011CbAeSDJx6tLEMmyVXmXc1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "865a8800-7397-438a-a984-8d0f5d599595",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3eUCdFGVe6AkeF8E5ZUpw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 696,
      "cache_read_input_tokens": 17028,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 696,
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

_source line 14 · 2026-05-18T20:13:53.817Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Q7TnfG2UzBPGqmkZ1cBm1P`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/d1967b82-9b64-485b-8419-ac1a11ebeb1d/tool-results/mcp-agent-ml-research-read_project_file-1779135207105.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "865a8800-7397-438a-a984-8d0f5d599595",
  "isSidechain": true,
  "agentId": "a4b1818a3cd108cba",
  "requestId": "req_011CbAeSDJx6tLEMmyVXmXc1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19a3be49-b199-403f-87a3-7f1eeef806b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3eUCdFGVe6AkeF8E5ZUpw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 696,
      "cache_read_input_tokens": 17028,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 696
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 17028,
          "cache_creation_input_tokens": 696,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 696,
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

_source line 15 · 2026-05-18T20:13:53.988Z_

<details><summary>↩ Tool result · `toolu_01Q7TnfG2UzBPGqmkZ1cBm1P`</summary>

```text
143567 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/d1967b82-9b64-485b-8419-ac1a11ebeb1d/tool-results/mcp-agent-ml-research-read_project_file-1779135207105.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19a3be49-b199-403f-87a3-7f1eeef806b0",
  "isSidechain": true,
  "promptId": "00163f99-7857-4276-afc6-24e9276d86ac",
  "agentId": "a4b1818a3cd108cba",
  "type": "user",
  "uuid": "c095376b-6d5f-4e9d-aef4-5eaf9e0e79ac",
  "sourceToolAssistantUUID": "19a3be49-b199-403f-87a3-7f1eeef806b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-18T20:14:01.238Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LfXPuLgnh1CrnD59LLkrGD`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/d1967b82-9b64-485b-8419-ac1a11ebeb1d/tool-results && python3 -c \"\nimport json, yaml\n\nwith open('mcp-agent-ml-research-read_project_file-1779135207105.txt', 'r') as f:\n    data = json.load(f)\n\nyaml_content = data['result']\nlit_map = yaml.safe_load(yaml_content)\n\n# Save parsed data for further analysis\nimport json as j\nwith open('/tmp/lit_map_parsed.json', 'w') as f:\n    j.dump(lit_map, f, indent=2, ensure_ascii=False)\n\n# Show structure\nif isinstance(lit_map, dict):\n    print('Top-level keys:', list(lit_map.keys()))\n    for k, v in lit_map.items():\n        if isinstance(v, list):\n            print(f'  {k}: {len(v)} items')\n        elif isinstance(v, dict):\n            print(f'  {k}: dict with keys {list(v.keys())[:5]}...')\n        else:\n            print(f'  {k}: {type(v).__name__}')\nelif isinstance(lit_map, list):\n    print(f'Top-level: list with {len(lit_map)} items')\n    if lit_map:\n        print('First item keys:', list(lit_map[0].keys()) if isinstance(lit_map[0], dict) else type(lit_map[0]))\n\"\n",
  "description": "Parse JSON/YAML file and inspect structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c095376b-6d5f-4e9d-aef4-5eaf9e0e79ac",
  "isSidechain": true,
  "agentId": "a4b1818a3cd108cba",
  "requestId": "req_011CbAeSWS67dh3wE78pyVu8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05153d41-ac20-4a48-8c63-136a92fd309e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N1gyMaGdCXHrtc8LuGDA8m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 300,
      "cache_read_input_tokens": 17724,
      "output_tokens": 487,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 300
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 487,
          "cache_read_input_tokens": 17724,
          "cache_creation_input_tokens": 300,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 300,
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

_source line 17 · 2026-05-18T20:14:01.507Z_

<details><summary>↩ Tool result · `toolu_01LfXPuLgnh1CrnD59LLkrGD`</summary>

```text
Top-level keys: ['success', 'data', 'error', 'metadata']
  success: bool
  data: dict with keys ['path', 'content', 'total_chars', 'truncated']...
  error: NoneType
  metadata: dict with keys []...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05153d41-ac20-4a48-8c63-136a92fd309e",
  "isSidechain": true,
  "promptId": "00163f99-7857-4276-afc6-24e9276d86ac",
  "agentId": "a4b1818a3cd108cba",
  "type": "user",
  "uuid": "2c4814a4-4267-4c86-9a12-110d07f63cfc",
  "sourceToolAssistantUUID": "05153d41-ac20-4a48-8c63-136a92fd309e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T20:14:07.430Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0163syAeYu4TcSWXA5kEWcaE`</summary>

```json
{
  "command": "python3 -c \"\nimport json, yaml\n\nwith open('/tmp/lit_map_parsed.json', 'r') as f:\n    data = json.load(f)\n\nyaml_str = data['data']['content']\nlit_map = yaml.safe_load(yaml_str)\n\n# Save the actual literature map\nwith open('/tmp/lit_map_actual.json', 'w') as f:\n    json.dump(lit_map, f, indent=2, ensure_ascii=False)\n\nif isinstance(lit_map, dict):\n    print('Literature map keys:', list(lit_map.keys()))\n    for k, v in lit_map.items():\n        if isinstance(v, list):\n            print(f'  {k}: {len(v)} items')\n            if v and isinstance(v[0], dict):\n                print(f'    Sample keys: {list(v[0].keys())}')\n        else:\n            print(f'  {k}: {type(v).__name__} = {str(v)[:100]}')\nelif isinstance(lit_map, list):\n    print(f'List with {len(lit_map)} items')\n\"\n",
  "description": "Parse the actual YAML content from the nested structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c4814a4-4267-4c86-9a12-110d07f63cfc",
  "isSidechain": true,
  "agentId": "a4b1818a3cd108cba",
  "requestId": "req_011CbAeT4brRDasBwGS5z1Rw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c70f1fc-bdc2-40d8-97f9-ea284b38c5d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4U9JmVbioe17fxw9hiVPY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 565,
      "cache_read_input_tokens": 18024,
      "output_tokens": 356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 565
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 356,
          "cache_read_input_tokens": 18024,
          "cache_creation_input_tokens": 565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 565,
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

_source line 19 · 2026-05-18T20:14:07.773Z_

<details><summary>↩ Tool result · `toolu_0163syAeYu4TcSWXA5kEWcaE`</summary>

```text
Literature map keys: ['papers']
  papers: 142 items
    Sample keys: ['title', 'authors', 'year', 'venue', 'url', 'category', 'role', 'key_finding', 'relevance_to_ced_stabilizer']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c70f1fc-bdc2-40d8-97f9-ea284b38c5d0",
  "isSidechain": true,
  "promptId": "00163f99-7857-4276-afc6-24e9276d86ac",
  "agentId": "a4b1818a3cd108cba",
  "type": "user",
  "uuid": "7ad96536-f1b9-4e92-911f-6a241c5e0c7e",
  "sourceToolAssistantUUID": "3c70f1fc-bdc2-40d8-97f9-ea284b38c5d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-18T20:14:10.066Z_

Good, 142 papers. Now let me run the four targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ad96536-f1b9-4e92-911f-6a241c5e0c7e",
  "isSidechain": true,
  "agentId": "a4b1818a3cd108cba",
  "requestId": "req_011CbAeTXSPTQeGnNm5q7E3m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69c4645e-aebe-4db6-9ecd-1a50316974e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uh32gxaBmbA9nym7PSt8X1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 537,
      "cache_read_input_tokens": 18589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 537,
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

_source line 21 · 2026-05-18T20:14:18.601Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FCMekuHNnaVy1FkrdpbuzZ`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/lit_map_actual.json', 'r') as f:\n    lit_map = json.load(f)\n\npapers = lit_map['papers']\n\n# ============================================================\n# 1. All papers with role \"direct-competitor\"\n# ============================================================\nprint(\"=\" * 80)\nprint(\"CATEGORY 1: Papers with role='direct-competitor'\")\nprint(\"=\" * 80)\n\ncompetitors = [p for p in papers if p.get('role') == 'direct-competitor']\nfor i, p in enumerate(competitors, 1):\n    print(f\"\\n--- Paper {i} ---\")\n    print(f\"  Title: {p.get('title')}\")\n    print(f\"  Venue: {p.get('venue')}\")\n    print(f\"  Year: {p.get('year')}\")\n    print(f\"  Role: {p.get('role')}\")\n    print(f\"  Category: {p.get('category')}\")\n    kf = p.get('key_finding', '')\n    rel = p.get('relevance_to_ced_stabilizer', '')\n    # Check for rejection sampling / selection strategy content\n    all_text = json.dumps(p, ensure_ascii=False).lower()\n    has_rejection = any(kw in all_text for kw in ['rejection sampling', 'rsft', 'best-of-n', 'scored selection', 'random selection', 'selection strategy'])\n    print(f\"  Key finding: {kf}\")\n    print(f\"  Relevance: {rel}\")\n    if has_rejection:\n        print(f\"  ** Contains rejection sampling / selection strategy keywords **\")\n\nprint(f\"\\nTotal direct-competitors: {len(competitors)}\")\n\nPYEOF\n",
  "description": "Find all direct-competitor papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69c4645e-aebe-4db6-9ecd-1a50316974e2",
  "isSidechain": true,
  "agentId": "a4b1818a3cd108cba",
  "requestId": "req_011CbAeTXSPTQeGnNm5q7E3m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "efcfed4a-3ade-4636-a4c1-9e3152bb226d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uh32gxaBmbA9nym7PSt8X1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 537,
      "cache_read_input_tokens": 18589,
      "output_tokens": 527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 537
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 527,
          "cache_read_input_tokens": 18589,
          "cache_creation_input_tokens": 537,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 537,
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

_source line 22 · 2026-05-18T20:14:18.724Z_

<details><summary>↩ Tool result · `toolu_01FCMekuHNnaVy1FkrdpbuzZ`</summary>

```text
================================================================================
CATEGORY 1: Papers with role='direct-competitor'
================================================================================

--- Paper 1 ---
  Title: DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction
  Venue: EACL 2023
  Year: 2023
  Role: direct-competitor
  Category: evidence_based_docre
  Key finding: 用 evidence 信息作为监督信号引导 DocRE 系统的 attention module 关注 evidence sentences。 提出 evidence retrieval (ER) self-training 策略，在无 evidence 标注的大规模数据上自动生成 silver evidence 训练 ER。DocRED 上 RE 和 ER 均达 SOTA。 解决了 evidence retrieval 的两大问题：高内存消耗和标注有限。

  Relevance: 

--- Paper 2 ---
  Title: CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction
  Venue: arXiv 2504.06529
  Year: 2025
  Role: direct-competitor
  Category: evidence_based_docre
  Key finding: 用 attentional graph-based 架构捕捉同文档内语义相似实体对间的协作模式。 文档转化为 bipartite graph（entity pair nodes + sentence nodes）， 三子图：Entity Pair 子图建模协作、Entity Pair-Sentence 子图捕捉语义关系、 Sentence 子图辅助共指推理。在 DocRED 上 evidence retrieval 和 RE 均有提升。

  Relevance: 

--- Paper 3 ---
  Title: QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs
  Venue: arXiv 2510.11696
  Year: 2025
  Role: direct-competitor
  Category: lora_qlora_artifacts
  Key finding: 标准量化引入静态确定性噪声，对 RL 后期训练不利。但精确控制的量化噪声 可通过增加 policy entropy 促进探索。Adaptive Quantization Noise (AQN) 机制 动态调整噪声。结合 NVFP4 + LoRA 实现 1.5x rollout 加速。 首次在单张 H100 上实现 32B LLM 的 RL 训练。

  Relevance: 

--- Paper 4 ---
  Title: ReasoningNER: A Reasoning Paradigm for Named Entity Recognition
  Venue: arXiv 2511.11978
  Year: 2025
  Role: direct-competitor
  Category: grpo_nlp_applications
  Key finding: 三阶段 NER 框架：CoT Generation → CoT Tuning → GRPO Reasoning Enhancement。 用 composite reward（entity F1 + format compliance）训练 GRPO policy。 ReasoningNER-8B 零样本超 GPT-4 12.3 F1、超 DeepSeek-R1-32B 8.4 F1， 1.7B 版本超 DeepSeek-R1-8B 10.5 F1。

  Relevance: 
  ** Contains rejection sampling / selection strategy keywords **

--- Paper 5 ---
  Title: OREO: Offline Reinforcement Learning for LLM Multi-Step Reasoning
  Venue: arXiv 2412.16145
  Year: 2024
  Role: direct-competitor
  Category: rsft_offline_rl
  Key finding: 基于 maximum entropy RL 的 offline 方法，联合学习 policy model 和 value function， 优化 soft Bellman Equation。无需 paired preference data， 实现更好的 credit assignment。学到的 value function 可免费引导 test-time tree search。 在 GSM8K、MATH、ALFWorld 上超越现有 offline 方法。

  Relevance: 
  ** Contains rejection sampling / selection strategy keywords **

Total direct-competitors: 5
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "efcfed4a-3ade-4636-a4c1-9e3152bb226d",
  "isSidechain": true,
  "promptId": "00163f99-7857-4276-afc6-24e9276d86ac",
  "agentId": "a4b1818a3cd108cba",
  "type": "user",
  "uuid": "2387ee94-0a08-46b0-9d1b-b54b6bb0eddd",
  "sourceToolAssistantUUID": "efcfed4a-3ade-4636-a4c1-9e3152bb226d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T20:14:27.882Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011K33EYrChtkYYcHKVk3A4R`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/lit_map_actual.json', 'r') as f:\n    lit_map = json.load(f)\n\npapers = lit_map['papers']\n\n# ============================================================\n# 2. Papers discussing rejection sampling, RSFT, scored/random selection\n# ============================================================\nprint(\"=\" * 80)\nprint(\"CATEGORY 2: Papers discussing rejection sampling / RSFT / selection strategies\")\nprint(\"=\" * 80)\n\nkeywords = ['rejection sampling', 'rsft', 'best-of-n', 'best of n', 'scored selection', \n            'random selection', 'selection strategy', 'reject sampling']\n\nresults = []\nfor p in papers:\n    all_text = json.dumps(p, ensure_ascii=False).lower()\n    matched_kws = [kw for kw in keywords if kw in all_text]\n    if matched_kws:\n        results.append((p, matched_kws))\n\nfor i, (p, kws) in enumerate(results, 1):\n    print(f\"\\n--- Paper {i} ---\")\n    print(f\"  Title: {p.get('title')}\")\n    print(f\"  Venue: {p.get('venue')}\")\n    print(f\"  Year: {p.get('year')}\")\n    print(f\"  Role: {p.get('role')}\")\n    print(f\"  Category: {p.get('category')}\")\n    print(f\"  Matched keywords: {kws}\")\n    print(f\"  Key finding: {p.get('key_finding', '')}\")\n    print(f\"  Relevance: {p.get('relevance_to_ced_stabilizer', '')}\")\n\nprint(f\"\\nTotal matches: {len(results)}\")\n\nPYEOF\n",
  "description": "Find papers about rejection sampling / RSFT / selection strategies"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2387ee94-0a08-46b0-9d1b-b54b6bb0eddd",
  "isSidechain": true,
  "agentId": "a4b1818a3cd108cba",
  "requestId": "req_011CbAeULDyg9MoVpUDKdxZC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d724979-0ff3-494d-8c6d-79e364021c60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017vMiJjRQMTm4aTd81W4Q6o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1600,
      "cache_read_input_tokens": 19126,
      "output_tokens": 523,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1600
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 523,
          "cache_read_input_tokens": 19126,
          "cache_creation_input_tokens": 1600,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1600,
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

_source line 24 · 2026-05-18T20:14:28.012Z_

<details><summary>↩ Tool result · `toolu_011K33EYrChtkYYcHKVk3A4R`</summary>

```text
================================================================================
CATEGORY 2: Papers discussing rejection sampling / RSFT / selection strategies
================================================================================

--- Paper 1 ---
  Title: A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce
  Venue: arXiv 2504.11343
  Year: 2025
  Role: key_theoretical_support
  Category: rsft_methodology
  Matched keywords: ['rejection sampling', 'rsft']
  Key finding: RAFT（简单 rejection sampling baseline）在数学推理上与 GRPO/PPO 表现相当。 消融实验表明 GRPO 的主要优势来自丢弃全错 prompt 而非 reward normalization。 提出 Reinforce-Rej，在 RAFT 基础上过滤全对和全错 sample。 关键洞察：GRPO 和 RAFT 的核心区别在于负样本处理——GRPO 混合正负样本训练， RAFT 只用正样本，但 RAFT 仍能达到相当性能，说明 rejection sampling 的简单性被低估了。

  Relevance: 

--- Paper 2 ---
  Title: Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning (TrajFusion)
  Venue: arXiv 2602.04391
  Year: 2026
  Role: method_component
  Category: rsft_methodology
  Matched keywords: ['rejection sampling', 'rsft']
  Key finding: 传统 RSFT 只用正确轨迹，丢弃错误轨迹。TrajFusion 将错误和正确轨迹交替拼接， 显式建模试错推理过程，在困难数学问题上显著超越标准 RFT。

  Relevance: 

--- Paper 3 ---
  Title: Rejection Sampling Based Fine Tuning Secretly Performs PPO
  Venue: ICML 2025
  Year: 2025
  Role: theoretical_support
  Category: rsft_methodology
  Matched keywords: ['rejection sampling', 'rsft']
  Key finding: 建立 RSFT 与 PPO 之间的理论联系：rejection sampling fine-tuning 在特定条件下隐式执行 PPO with marginal KL constraints。

  Relevance: 

--- Paper 4 ---
  Title: R1-RE: Cross-Domain Relation Extraction with RLVR
  Venue: arXiv 2507.04642
  Year: 2025
  Role: direct_competitor
  Category: rl_for_ie
  Matched keywords: ['rsft']
  Key finding: 首个将 RLVR（GRPO + verifiable reward）用于关系抽取的框架。 将 RE 重构为推理任务，R1-RE-7B 在跨域 OOD 准确率约 70%，媲美 GPT-4o。 Reward 设计：format reward (+1/-3) + metric reward (+2/-1.5)，先验证格式再加准确度。 triplet extraction 用 F1-based reward（entity weight=1, triplet weight=3）。 未报告 catastrophic forgetting——GRPO 训练后在 MATH-500/IFEval/GPQA 上性能不降反升， 说明句子级 RE 的简单 reward 结构足以稳定 GRPO 训练。

  Relevance: 

--- Paper 5 ---
  Title: MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with RL
  Venue: arXiv 2603.09478
  Year: 2026
  Role: related_method
  Category: rl_for_ie
  Matched keywords: ['rsft']
  Key finding: 多模态 RE 中用 GRPO + Progressive Sample-Mixing Strategy 优化 LVLM 推理能力。 两阶段训练：SFT cold-start + GRPO RL。

  Relevance: 

--- Paper 6 ---
  Title: REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support
  Venue: EMNLP 2025 Findings
  Year: 2025
  Role: related_method
  Category: rl_for_ie
  Matched keywords: ['rsft']
  Key finding: 将强化学习推理优化用于事件论元抽取，结合关系感知支持。 不同于 DocRE 但同属 IE 领域的 RL 应用。

  Relevance: 

--- Paper 7 ---
  Title: Adaptive Reinforcement Learning Planning: Harnessing LLMs for Complex Information Extraction
  Venue: arXiv 2406.11455
  Year: 2024
  Role: background
  Category: rl_for_ie
  Matched keywords: ['rsft']
  Key finding: 将 LLM 顺序抽取建模为 MDP，用 DDQN 训练 decision module 自适应选择实体抽取顺序，提升复杂 IE 性能。

  Relevance: 

--- Paper 8 ---
  Title: Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning
  Venue: ICML 2026
  Year: 2025
  Role: background
  Category: rl_for_ie
  Matched keywords: ['rsft']
  Key finding: 用端到端 RL 优化 GraphRAG agent 的多轮检索-推理循环， 包含 knowledge hypergraph construction（n-ary relation extraction）。

  Relevance: 

--- Paper 9 ---
  Title: RelPrior: Relation as a Prior - A Novel Paradigm for LLM-based Document-level Relation Extraction
  Venue: arXiv 2511.08143
  Year: 2025
  Role: key_baseline
  Category: llm_docre
  Matched keywords: ['rsft']
  Key finding: 用 binary relation 作为先验过滤无关实体对，再用 predefined relation 匹配实体， 避免 LLM 在 DocRE 中被无关实体对分散注意力。 在 DocRED/Re-DocRED 上超越现有纯 LLM-based DocRE 方法。

  Relevance: 

--- Paper 10 ---
  Title: LMRC: LLM with Relation Classifier for Document-Level Relation Extraction
  Venue: arXiv 2408.13889
  Year: 2024
  Role: related_method
  Category: llm_docre
  Matched keywords: ['rsft']
  Key finding: 两阶段方法：先用 attention-based classifier 过滤 NA 实体对（RCP）， 再用 LLM 在精简候选空间中做多分类（RC）。 注意：LMRC 依赖 BERT-based classifier 作为预筛选，非纯 LLM 方法。

  Relevance: 

--- Paper 11 ---
  Title: Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction
  Venue: NLPCC 2025
  Year: 2025
  Role: related_method
  Category: llm_docre
  Matched keywords: ['rsft']
  Key finding: 用频繁模式挖掘 + MCTS 搜索逻辑规则，转化为 prompt 约束 LLM 输出， 再用 CoT 验证过滤不满足规则的 triple。 在 DWIE、DocRED、Re-DocRED 上声称超越现有 LLM 方法和规则框架。 具体 F1 未公开获取（Springer 付费墙），但声称超越 AutoRE 等 LLM baseline。

  Relevance: 

--- Paper 12 ---
  Title: GLiDRE: Generalist Lightweight model for Document-level Relation Extraction
  Venue: arXiv 2508.00757
  Year: 2025
  Role: background
  Category: llm_docre
  Matched keywords: ['rsft']
  Key finding: 基于 dual-encoder 的轻量级零/少样本 DocRE 模型， 预训练于 136K 文档的大规模 RE 数据。 fully supervised Re-DocRED test F1=77.83，但这是 encoder-based 非 LLM generative。 zero-shot Re-DocRED test F1=17.32（超越 LLaMA 3.3 70B 和 Mistral-Small 24B）。

  Relevance: 

--- Paper 13 ---
  Title: AutoRE: Document-Level Relation Extraction with Large Language Models
  Venue: arXiv 2403.14888
  Year: 2024
  Role: background
  Category: llm_docre
  Matched keywords: ['rsft']
  Key finding: RHF（Relation-Head-Facts）范式用 Mistral-7B + QLoRA 做端到端 DocRE。 关键设计：先抽 relation，再抽 head entity，最后抽 fact triple。

  Relevance: 

--- Paper 14 ---
  Title: ADELIE: Aligning Large Language Models on Information Extraction
  Venue: EMNLP 2024
  Year: 2024
  Role: key_baseline
  Category: llm_ie_alignment
  Matched keywords: ['rejection sampling', 'rsft']
  Key finding: 构建 IEInstruct 高质量 IE alignment 语料库，用 SFT + DPO 训练 ADELIE。 支持 closed/open/on-demand IE 三种模式。 基于 LLaMA-2-7B/LLaMA-3.2-3B/Qwen2.5-1.5B，在多个 held-out IE dataset 上达 SOTA。

  Relevance: 

--- Paper 15 ---
  Title: Evidence-aware Document-level Relation Extraction
  Venue: CIKM 2022
  Year: 2022
  Role: background
  Category: evidence_based_docre
  Matched keywords: ['rsft']
  Key finding: 将 evidence sentence selection 建模为序列决策问题， 用 RL 机制选择支撑关系的 evidence sentences。 在 DocRED 上验证 evidence-aware 方法的有效性。

  Relevance: 

--- Paper 16 ---
  Title: ReasoningNER: A Reasoning Paradigm for Named Entity Recognition
  Venue: arXiv 2511.11978
  Year: 2025
  Role: direct-competitor
  Category: grpo_nlp_applications
  Matched keywords: ['rsft']
  Key finding: 三阶段 NER 框架：CoT Generation → CoT Tuning → GRPO Reasoning Enhancement。 用 composite reward（entity F1 + format compliance）训练 GRPO policy。 ReasoningNER-8B 零样本超 GPT-4 12.3 F1、超 DeepSeek-R1-32B 8.4 F1， 1.7B 版本超 DeepSeek-R1-8B 10.5 F1。

  Relevance: 

--- Paper 17 ---
  Title: Posterior-GRPO: Rewarding Reasoning Processes in Code Generation
  Venue: arXiv 2508.05170
  Year: 2025
  Role: method-component
  Category: grpo_nlp_applications
  Matched keywords: ['rejection sampling', 'rsft']
  Key finding: 在代码生成中仅对成功输出的推理过程施加 process-based reward（条件 reward）， 有效抑制 reward hacking——模型不能通过错误推理碰巧生成正确代码来获得高 reward。 通过将 reward 条件化于最终正确性，对齐内部推理与代码正确性。

  Relevance: 

--- Paper 18 ---
  Title: OREO: Offline Reinforcement Learning for LLM Multi-Step Reasoning
  Venue: arXiv 2412.16145
  Year: 2024
  Role: direct-competitor
  Category: rsft_offline_rl
  Matched keywords: ['rsft']
  Key finding: 基于 maximum entropy RL 的 offline 方法，联合学习 policy model 和 value function， 优化 soft Bellman Equation。无需 paired preference data， 实现更好的 credit assignment。学到的 value function 可免费引导 test-time tree search。 在 GSM8K、MATH、ALFWorld 上超越现有 offline 方法。

  Relevance: 

--- Paper 19 ---
  Title: PCL-Reasoner-V1.5: Advancing Math Reasoning with Offline Reinforcement Learning
  Venue: arXiv 2601.14716
  Year: 2026
  Role: key_evidence
  Category: rsft_offline_rl
  Matched keywords: ['rsft']
  Key finding: 基于 Qwen2.5-32B 的数学推理模型。核心创新是 offline RL 方法， 在训练稳定性和效率上优于 GRPO 等 online RL。 AIME 2024 平均 90.9%，AIME 2025 平均 85.6%， 在 Qwen2.5-32B post-training 中达 SOTA。

  Relevance: 

--- Paper 20 ---
  Title: RS-DPO: A Hybrid Rejection Sampling and Direct Preference Optimization Method for Alignment of Large Language Models
  Venue: NAACL 2024 Findings
  Year: 2024
  Role: method-component
  Category: rsft_offline_rl
  Matched keywords: ['rejection sampling', 'rsft']
  Key finding: 系统性结合 rejection sampling 和 DPO。从 SFT 模型采样 k 个 response per prompt， 根据 reward 分布识别 contrastive pairs，用 DPO 对齐。 在有限资源环境下有效微调 LLM，超越独立的 RS、PPO 和 DPO。

  Relevance: 

--- Paper 21 ---
  Title: RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment
  Venue: TMLR 2024
  Year: 2024
  Role: background
  Category: rsft_offline_rl
  Matched keywords: ['rejection sampling', 'rsft']
  Key finding: RAFT 是 rejection sampling fine-tuning 的标准化框架：迭代式 generate → rank → filter → SFT。 每轮生成 n 个 response，用 reward model 排序，取 top-k 做 SFT。 在文本生成和对话上验证有效性，提供了 RSFT 的 canonical 实现。

  Relevance: 

--- Paper 22 ---
  Title: RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs
  Venue: arXiv 2508.16546
  Year: 2025
  Role: supporting_evidence
  Category: grpo_structured
  Matched keywords: ['rsft']
  Key finding: RL-FT 可恢复 SFT 导致的大部分 OOD 性能损失，但当 SFT 造成严重 overfitting 时 RL 无法完全恢复。 OOD 性能退化和恢复主要与 singular vector 方向旋转相关，而非 singular value 变化。 恢复 top 20% singular values 对应方向可恢复 70-80% OOD 性能。

  Relevance: 

--- Paper 23 ---
  Title: Is Best-of-N the Best of Them? Coverage, Scaling, and Optimality in Inference-Time Alignment
  Venue: ICML 2025
  Year: 2025
  Role: key_baseline
  Category: inference_time_reranking
  Matched keywords: ['best-of-n']
  Key finding: Best-of-N sampling provably suffers from reward hacking when N is large. 提出 InferenceTimePessimism 算法，通过 pessimism in the face of uncertainty 实现 scaling-monotonic 性能（性能不随 N 增大而退化）。 强调 pre-trained policy 对高质量 response 的 coverage 是 BoN 成功的关键。

  Relevance: 

--- Paper 24 ---
  Title: Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models
  Venue: ICLR 2025
  Year: 2024
  Role: method_component
  Category: inference_time_reranking
  Matched keywords: ['rsft', 'best-of-n']
  Key finding: 提出 inference-aware fine-tuning 范式：训练时直接优化 BoN inference 策略的性能。 设计 imitation learning 和 RL 方法克服 BoN 中不可微的 argmax 操作。 BoN-aware 模型隐式学习 exploration-exploitation meta-strategy， 交替生成最优 response 和多样性 response。

  Relevance: 

--- Paper 25 ---
  Title: Evaluation of Best-of-N Sampling Strategies for Language Model Alignment
  Venue: TMLR 2025
  Year: 2025
  Role: evaluation
  Category: inference_time_reranking
  Matched keywords: ['best-of-n']
  Key finding: 系统评估 BoN 采样的 reward hacking 问题。 提出 Stochastic Regularized BoN (SRBoN) 有理论保证的方法。 发现简单的 Sentence Length Regularized BoN 也能获得 comparable 性能。

  Relevance: 

--- Paper 26 ---
  Title: Regularized Best-of-N Sampling with Minimum Bayes Risk Objective for Language Model Alignment
  Venue: NAACL 2025
  Year: 2024
  Role: related_method
  Category: inference_time_reranking
  Matched keywords: ['best-of-n']
  Key finding: MBR-BoN：用 Minimum Bayes Risk 目标作为 proximity regularizer 缓解 reward hacking。 MBR 目标量化 response 与 reference policy 的接近程度。 在 AlpacaFarm 和 hh-rlhf 上优于 vanilla BoN 和 MBR decoding。

  Relevance: 

--- Paper 27 ---
  Title: AdaSTaR: Adaptive Data Sampling for Training Self-Taught Reasoners
  Venue: NeurIPS 2025
  Year: 2025
  Role: related_method
  Category: rsft_methodology
  Matched keywords: ['rsft']
  Key finding: RFT/RSFT 的随机数据采样导致训练不均衡——已解决的样本被过度训练，困难样本训练不足。 AdaSTaR 引入两个自适应采样原则：(1) diversity sampling 促进均衡， (2) curriculum sampling 根据模型能力动态调整数据难度。 在 6 个 benchmark 全部取得最优，训练 FLOPs 平均减少 58.6%。

  Relevance: 

--- Paper 28 ---
  Title: RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning
  Venue: arXiv 2601.09253
  Year: 2026
  Role: direct_competitor
  Category: rsft_methodology
  Matched keywords: ['rsft']
  Key finding: RSFT 的 hard rejection 丢弃大量计算昂贵的负样本。 RIFT 保留所有轨迹，用标量 reward 重新加权 loss， 正 reward 样本鼓励正确行为，负 reward 样本提供反向梯度。 引入 stabilized loss 解决 naive reward integration 的训练坍塌问题。

  Relevance: 

--- Paper 29 ---
  Title: Document-Level Relation Extraction with Adaptive Focal Loss and Knowledge Distillation
  Venue: Findings of ACL 2022
  Year: 2022
  Role: background
  Category: knowledge_distillation_docre
  Matched keywords: ['rejection sampling', 'rsft']
  Key finding: KD-DocRE：用 axial attention 学习 entity pair 间依赖关系， adaptive focal loss 解决类别不均衡，knowledge distillation 弥合 人工标注和远程监督数据的差异。DocRED leaderboard 上超越前 SOTA 1.36 F1。

  Relevance: 

--- Paper 30 ---
  Title: Document-level Relation Extraction with Progressive Self-distillation
  Venue: ACM TOIS 2024
  Year: 2024
  Role: related_method
  Category: knowledge_distillation_docre
  Matched keywords: ['rsft']
  Key finding: PSD：online self-knowledge distillation 用过去预测作为 soft labels， 无需额外 teacher model，单次训练即可完成。 渐进式 soft label 平滑 hard label 的噪声，提升 DocRE 性能。

  Relevance: 

--- Paper 31 ---
  Title: STaR: Bootstrapping Reasoning With Reasoning
  Venue: NeurIPS 2022
  Year: 2022
  Role: method_component
  Category: self_training_bootstrapping
  Matched keywords: ['rsft']
  Key finding: Self-Taught Reasoner：迭代式 bootstrapping——生成 rationale 回答问题， 答对的保留，答错的用 rationalization（给正确答案生成事后 rationale）补充， 然后 fine-tune 模型。循环迭代使模型逐渐学会更难的推理。

  Relevance: 

--- Paper 32 ---
  Title: Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models
  Venue: ICML 2024
  Year: 2024
  Role: related_method
  Category: self_training_bootstrapping
  Matched keywords: ['rsft']
  Key finding: SPIN：LLM 通过 self-play 机制与自身过去版本对弈来提升—— 区分自身生成的 response 和 human-annotated response。 全局最优在 LLM policy 与目标分布对齐时达到。 性能超越 DPO + GPT-4 偏好数据。

  Relevance: 

Total matches: 32
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d724979-0ff3-494d-8c6d-79e364021c60",
  "isSidechain": true,
  "promptId": "00163f99-7857-4276-afc6-24e9276d86ac",
  "agentId": "a4b1818a3cd108cba",
  "type": "user",
  "uuid": "79a3a314-a27a-4365-b8b3-2a0195409a03",
  "sourceToolAssistantUUID": "2d724979-0ff3-494d-8c6d-79e364021c60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T20:14:39.005Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01T1wjRcE7M319yHScAzgEy8`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/lit_map_actual.json', 'r') as f:\n    lit_map = json.load(f)\n\npapers = lit_map['papers']\n\n# ============================================================\n# 3. Papers discussing GRPO or RL for IE/NLP structured tasks\n# ============================================================\nprint(\"=\" * 80)\nprint(\"CATEGORY 3: Papers about GRPO / RL for IE/NLP structured tasks\")\nprint(\"=\" * 80)\n\nkeywords_grpo = ['grpo', 'group relative policy']\nkeywords_rl_ie = ['reinforcement learning']\nkeywords_ie = ['information extraction', 'relation extraction', 'named entity', 'event extraction', 'ner']\n\nresults = []\nfor p in papers:\n    all_text = json.dumps(p, ensure_ascii=False).lower()\n    \n    has_grpo = any(kw in all_text for kw in keywords_grpo)\n    has_rl = any(kw in all_text for kw in keywords_rl_ie)\n    has_ie = any(kw in all_text for kw in keywords_ie)\n    \n    if has_grpo or (has_rl and has_ie):\n        matched = []\n        if has_grpo: matched.append('GRPO')\n        if has_rl: matched.append('RL')\n        if has_ie: matched.append('IE/NLP-structured')\n        results.append((p, matched))\n\nfor i, (p, tags) in enumerate(results, 1):\n    print(f\"\\n--- Paper {i} ---\")\n    print(f\"  Title: {p.get('title')}\")\n    print(f\"  Venue: {p.get('venue')}\")\n    print(f\"  Year: {p.get('year')}\")\n    print(f\"  Role: {p.get('role')}\")\n    print(f\"  Category: {p.get('category')}\")\n    print(f\"  Matched tags: {tags}\")\n    print(f\"  Key finding: {p.get('key_finding', '')}\")\n    print(f\"  Relevance: {p.get('relevance_to_ced_stabilizer', '')}\")\n\nprint(f\"\\nTotal matches: {len(results)}\")\n\nPYEOF\n",
  "description": "Find papers about GRPO or RL for IE/NLP structured tasks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79a3a314-a27a-4365-b8b3-2a0195409a03",
  "isSidechain": true,
  "agentId": "a4b1818a3cd108cba",
  "requestId": "req_011CbAeV1yA2oMwdwMQtGhXp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c33ef3a-f254-4cf7-88b2-5da6d8683c37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RXAgSZCko9LHkJZpc71Ha1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6655,
      "cache_read_input_tokens": 20726,
      "output_tokens": 655,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6655
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 655,
          "cache_read_input_tokens": 20726,
          "cache_creation_input_tokens": 6655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6655,
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

_source line 26 · 2026-05-18T20:14:39.153Z_

<details><summary>↩ Tool result · `toolu_01T1wjRcE7M319yHScAzgEy8`</summary>

```text
&lt;persisted-output>
Output too large (29.5KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/d1967b82-9b64-485b-8419-ac1a11ebeb1d/tool-results/bwxf07j11.txt

Preview (first 2KB):
================================================================================
CATEGORY 3: Papers about GRPO / RL for IE/NLP structured tasks
================================================================================

--- Paper 1 ---
  Title: GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization
  Venue: ICML 2026
  Year: 2025
  Role: closest_prior_work
  Category: reward_diversity
  Matched tags: ['GRPO']
  Key finding: 直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值， 降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合， 保留多 reward 的相对差异，显著提升训练稳定性。

  Relevance: 最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality）， GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。 但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。


--- Paper 2 ---
  Title: DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs
  Venue: arXiv 2505.09655
  Year: 2025
  Role: related_method
  Category: reward_diversity
  Matched tags: ['GRPO']
  Key finding: GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。 DRA 用子模互信息（SMI）对 reward 加权，给多样性高的 completion 更大权重， 等价于 Inverse Propensity Scoring 去偏，防止 policy 坍缩到先验模式。

  Relevance: DRA 通过后处理 reward 注入多样性信号；CED 的 reward 本身就内含对比结构自然提供 diversity 信号。 机制互补但来源不同——CED 是 reward design 层面，DRA 是 optimization 层面。


--- Paper 3 ---
  Title: DAPO: An Open-Source LLM Reinforcement Learning System at Scale
  Venue: NeurIPS 2025
  Year: 2025
  Role: key_baseline
  Category: mode_collapse_prevention
  Matched tags: ['GRPO', 'RL']
  Key finding: Naive GRPO 存在 entropy collapse（policy 熵快速下降→输出同质化）。 根因：clipping 不对称性——概率 0.01 的 token 最多增到 0.012，而概率 0.9 的 token 可达 1.08， 低概率 token 难以增长，抑制探索。DAPO 提出 Clip-Higher（εhigh=0.28 > εlow=0.2） 为低概率 token 留更大增长空间，加 Dynamic Sampling 过滤 accuracy=0 或 1 的 prompt （这些 prompt 产生零梯度，降低有效 batch size）。在 AIME 2024 达 50 分超越 DeepSeek-R1-Zero。

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c33ef3a-f254-4cf7-88b2-5da6d8683c37",
  "isSidechain": true,
  "promptId": "00163f99-7857-4276-afc6-24e9276d86ac",
  "agentId": "a4b1818a3cd108cba",
  "type": "user",
  "uuid": "71ee16b6-d7f1-4c91-ae70-5acf85498abb",
  "sourceToolAssistantUUID": "5c33ef3a-f254-4cf7-88b2-5da6d8683c37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T20:14:41.706Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ng5dPAUkkUKj12Q6B1gVaw`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/d1967b82-9b64-485b-8419-ac1a11ebeb1d/tool-results/bwxf07j11.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71ee16b6-d7f1-4c91-ae70-5acf85498abb",
  "isSidechain": true,
  "agentId": "a4b1818a3cd108cba",
  "requestId": "req_011CbAeVqYcwvjYuD1WsPvYH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59e0b099-3c9f-4dca-99b0-c20ac1e9b348",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019NcxFjMw66dvS6qZgeb9bC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1707,
      "cache_read_input_tokens": 27381,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1707
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 130,
          "cache_read_input_tokens": 27381,
          "cache_creation_input_tokens": 1707,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1707,
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

_source line 28 · 2026-05-18T20:14:41.724Z_

<details><summary>↩ Tool result · `toolu_01Ng5dPAUkkUKj12Q6B1gVaw`</summary>

```text
1	================================================================================
2	CATEGORY 3: Papers about GRPO / RL for IE/NLP structured tasks
3	================================================================================
4	
5	--- Paper 1 ---
6	  Title: GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization
7	  Venue: ICML 2026
8	  Year: 2025
9	  Role: closest_prior_work
10	  Category: reward_diversity
11	  Matched tags: ['GRPO']
12	  Key finding: 直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值， 降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合， 保留多 reward 的相对差异，显著提升训练稳定性。
13	
14	  Relevance: 最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality）， GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。 但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。
15	
16	
17	--- Paper 2 ---
18	  Title: DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs
19	  Venue: arXiv 2505.09655
20	  Year: 2025
21	  Role: related_method
22	  Category: reward_diversity
23	  Matched tags: ['GRPO']
24	  Key finding: GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。 DRA 用子模互信息（SMI）对 reward 加权，给多样性高的 completion 更大权重， 等价于 Inverse Propensity Scoring 去偏，防止 policy 坍缩到先验模式。
25	
26	  Relevance: DRA 通过后处理 reward 注入多样性信号；CED 的 reward 本身就内含对比结构自然提供 diversity 信号。 机制互补但来源不同——CED 是 reward design 层面，DRA 是 optimization 层面。
27	
28	
29	--- Paper 3 ---
30	  Title: DAPO: An Open-Source LLM Reinforcement Learning System at Scale
31	  Venue: NeurIPS 2025
32	  Year: 2025
33	  Role: key_baseline
34	  Category: mode_collapse_prevention
35	  Matched tags: ['GRPO', 'RL']
36	  Key finding: Naive GRPO 存在 entropy collapse（policy 熵快速下降→输出同质化）。 根因：clipping 不对称性——概率 0.01 的 token 最多增到 0.012，而概率 0.9 的 token 可达 1.08， 低概率 token 难以增长，抑制探索。DAPO 提出 Clip-Higher（εhigh=0.28 > εlow=0.2） 为低概率 token 留更大增长空间，加 Dynamic Sampling 过滤 accuracy=0 或 1 的 prompt （这些 prompt 产生零梯度，降低有效 batch size）。在 AIME 2024 达 50 分超越 DeepSeek-R1-Zero。
37	
38	  Relevance: DAPO 从 optimization 技巧角度解决 entropy collapse。CED reward 从 reward design 层面 防止 mode collapse——evidence quality 维度确保 reward 组内有足够 variance， 不会出现 all-same-reward 的零梯度 prompt。DAPO 的 Dynamic Sampling 过滤 accuracy=0/1 prompt 与我们观察到的 frac_zero_std→0.8 现象本质相同：extraction-only reward 下大量 prompt 产生零 advantage，CED 从源头（reward 设计）而非后处理（过滤）解决这个问题。
39	
40	
41	--- Paper 4 ---
42	  Title: Dr. GRPO: Removing Optimization Bias in GRPO
43	  Venue: COLM 2025
44	  Year: 2025
45	  Role: related_analysis
46	  Category: mode_collapse_prevention
47	  Matched tags: ['GRPO']
48	  Key finding: GRPO 的 std 归一化引入两个 bias：(1) difficulty bias——std(r) 归一化对低 variance 组 （全对/全错）给予过高 advantage 权重，trivial question 主导训练信号； (2) length bias——per-token loss 的 1/|o_i| 项使长的错误回答被 under-penalize。 当 std(r)→0 时 advantage 爆炸或未定义，梯度数值不稳定。 Dr. GRPO 移除 std 归一化，用无偏 Monte Carlo advantage：Ã = R(q,o_i) - mean(R)。
49	
50	  Relevance: 与我们的实验发现高度一致：extraction-only reward 下 frac_zero_std→0.8 正是 Dr. GRPO 分析的 difficulty bias 极端情况——大量 prompt 的所有 rollout 得到相同 F1， std→0 导致 advantage 异常。CED 通过增加 reward 维度天然维持 reward_std>0， 从 reward 设计而非算法修改角度避免了 Dr. GRPO 发现的 bias。
51	
52	
53	--- Paper 5 ---
54	  Title: DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO
55	  Venue: arXiv 2512.21514
56	  Year: 2025
57	  Role: parallel_work
58	  Category: mode_collapse_prevention
59	  Matched tags: ['GRPO', 'IE/NLP-structured']
60	  Key finding: 图像生成中 GRPO 后期输出同质化。distributional reward modeling（谱聚类+exploratory reward） 和 structure-aware regularization 实现 13-18% 语义多样性提升。
61	
62	  Relevance: 跨域验证了 GRPO mode collapse 的普遍性，distributional reward 思路与 CED 精神相近—— 都是通过 reward 层面结构化信号维持输出多样性。
63	
64	
65	--- Paper 6 ---
66	  Title: Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients
67	  Venue: arXiv 2601.23135
68	  Year: 2025
69	  Role: theoretical_support
70	  Category: mode_collapse_prevention
71	  Matched tags: ['GRPO']
72	  Key finding: GRPO 的 reward_std 归一化在温和条件下提供严格优于未归一化 REINFORCE 的收敛速率， 收益由 prompt 间平均 reward std 刻画。
73	
74	  Relevance: 直接理论支撑：reward_std 越大收敛越好。CED 通过 evidence quality 维度维持高 reward_std， 从该理论看 CED 的稳定性优势是 reward_std 维持带来的收敛速率优势。
75	
76	
77	--- Paper 7 ---
78	  Title: Improving Reinforcement Learning from Human Feedback Using Contrastive Rewards
79	  Venue: arXiv 2403.07708
80	  Year: 2024
81	  Role: closest_contrastive_precedent
82	  Category: contrastive_reward
83	  Matched tags: ['GRPO', 'RL']
84	  Key finding: 两步机制：(1) 离线采样 baseline response；(2) 用 baseline 计算 contrastive reward 作为 PPO 的 penalty 项。效果：惩罚 reward uncertainty、根据任务难度自适应校准、 减少 PPO 中的 variance。在 TL;DR 和 HH-RLHF 上持续优于标准 RLHF。
85	
86	  Relevance: 最接近的对比 reward 先例。关键差异：(1) 它是对 learned RM 输出的后处理对比， CED 是 reward function 本身就是对比判别（evidence vs. corrupted evidence）； (2) 它在 PPO 中验证，CED 在 GRPO 中验证； (3) 它是 domain-agnostic penalty，CED 是 task-specific faithfulness signal。 stabilizing 机制相通但实现路径根本不同。
87	
88	
89	--- Paper 8 ---
90	  Title: A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce
91	  Venue: arXiv 2504.11343
92	  Year: 2025
93	  Role: key_theoretical_support
94	  Category: rsft_methodology
95	  Matched tags: ['GRPO']
96	  Key finding: RAFT（简单 rejection sampling baseline）在数学推理上与 GRPO/PPO 表现相当。 消融实验表明 GRPO 的主要优势来自丢弃全错 prompt 而非 reward normalization。 提出 Reinforce-Rej，在 RAFT 基础上过滤全对和全错 sample。 关键洞察：GRPO 和 RAFT 的核心区别在于负样本处理——GRPO 混合正负样本训练， RAFT 只用正样本，但 RAFT 仍能达到相当性能，说明 rejection sampling 的简单性被低估了。
97	
98	  Relevance: 
99	
100	--- Paper 9 ---
101	  Title: Rejection Sampling Based Fine Tuning Secretly Performs PPO
102	  Venue: ICML 2025
103	  Year: 2025
104	  Role: theoretical_support
105	  Category: rsft_methodology
106	  Matched tags: ['GRPO']
107	  Key finding: 建立 RSFT 与 PPO 之间的理论联系：rejection sampling fine-tuning 在特定条件下隐式执行 PPO with marginal KL constraints。
108	
109	  Relevance: 
110	
111	--- Paper 10 ---
112	  Title: R1-RE: Cross-Domain Relation Extraction with RLVR
113	  Venue: arXiv 2507.04642
114	  Year: 2025
115	  Role: direct_competitor
116	  Category: rl_for_ie
117	  Matched tags: ['GRPO', 'IE/NLP-structured']
118	  Key finding: 首个将 RLVR（GRPO + verifiable reward）用于关系抽取的框架。 将 RE 重构为推理任务，R1-RE-7B 在跨域 OOD 准确率约 70%，媲美 GPT-4o。 Reward 设计：format reward (+1/-3) + metric reward (+2/-1.5)，先验证格式再加准确度。 triplet extraction 用 F1-based reward（entity weight=1, triplet weight=3）。 未报告 catastrophic forgetting——GRPO 训练后在 MATH-500/IFEval/GPQA 上性能不降反升， 说明句子级 RE 的简单 reward 结构足以稳定 GRPO 训练。
119	
120	  Relevance: 
121	
122	--- Paper 11 ---
123	  Title: MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with RL
124	  Venue: arXiv 2603.09478
125	  Year: 2026
126	  Role: related_method
127	  Category: rl_for_ie
128	  Matched tags: ['GRPO', 'IE/NLP-structured']
129	  Key finding: 多模态 RE 中用 GRPO + Progressive Sample-Mixing Strategy 优化 LVLM 推理能力。 两阶段训练：SFT cold-start + GRPO RL。
130	
131	  Relevance: 
132	
133	--- Paper 12 ---
134	  Title: Adaptive Reinforcement Learning Planning: Harnessing LLMs for Complex Information Extraction
135	  Venue: arXiv 2406.11455
136	  Year: 2024
137	  Role: background
138	  Category: rl_for_ie
139	  Matched tags: ['RL', 'IE/NLP-structured']
140	  Key finding: 将 LLM 顺序抽取建模为 MDP，用 DDQN 训练 decision module 自适应选择实体抽取顺序，提升复杂 IE 性能。
141	
142	  Relevance: 
143	
144	--- Paper 13 ---
145	  Title: Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning
146	  Venue: ICML 2026
147	  Year: 2025
148	  Role: background
149	  Category: rl_for_ie
150	  Matched tags: ['RL', 'IE/NLP-structured']
151	  Key finding: 用端到端 RL 优化 GraphRAG agent 的多轮检索-推理循环， 包含 knowledge hypergraph construction（n-ary relation extraction）。
152	
153	  Relevance: 
154	
155	--- Paper 14 ---
156	  Title: EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models
157	  Venue: arXiv 2603.19532
158	  Year: 2026
159	  Role: closest_competitor
160	  Category: evidence_grounded_rl
161	  Matched tags: ['GRPO', 'IE/NLP-structured']
162	  Key finding: 用 GRPO 同时优化 grounding（evidence entailment）和 correctness（答案准确性）。 在 cardiac diagnosis（Llama-3.2-3B）上 F1@3 从 37.0→54.5，grounding 从 47.6→78.2， hallucination 降 5 倍。在 legal reasoning（Llama-3.1-8B）上 faithfulness 从 32.8%→67.6%。 核心：证据一致性 reward 不牺牲 task accuracy 的前提下大幅提升 faithfulness。
163	
164	  Relevance: 
165	
166	--- Paper 15 ---
167	  Title: MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems
168	  Venue: arXiv 2509.22047
169	  Year: 2025
170	  Role: related_method
171	  Category: multi_objective_grpo
172	  Matched tags: ['GRPO']
173	  Key finding: GRPO 在多目标设置下易发生 reward hacking——只优化一个目标而牺牲其他目标。 MO-GRPO 用 variance-based normalization 自动平衡多个 reward function 的权重， 在多臂赌博机、控制、机器翻译、指令遵从四个域上实现稳定学习。
174	
175	  Relevance: 
176	
177	--- Paper 16 ---
178	  Title: Multi-Objective and Mixed-Reward Reinforcement Learning via Reward-Decorrelated Policy Optimization
179	  Venue: arXiv 2605.13641
180	  Year: 2026
181	  Role: related_method
182	  Category: multi_objective_grpo
183	  Matched tags: ['GRPO', 'RL']
184	  Key finding: GRPO 聚合 mixed-reward 时直接求和再归一化会淹没弱信号 reward 维度。 RDPO 用 Magnitude-Aware Quantile normalization + Mahalanobis whitening 去相关 reward 子空间，改善 LLM post-training 的多目标平衡。
185	
186	  Relevance: 
187	
188	--- Paper 17 ---
189	  Title: GRPO is Secretly a Process Reward Model
190	  Venue: under review at ICML 2026
191	  Year: 2025
192	  Role: theoretical_insight
193	  Category: grpo_theory
194	  Matched tags: ['GRPO', 'IE/NLP-structured']
195	  Key finding: 证明 GRPO + ORM 在特定条件下等价于 PRM-aware RL objective。 提出 λ-GRPO 修正 GRPO 在不均匀 process step 上的 deficiency， 在 downstream reasoning 上超越标准 GRPO 且训练更快收敛。
196	
197	  Relevance: 
198	
199	--- Paper 18 ---
200	  Title: Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges
201	  Venue: arXiv 2604.13602
202	  Year: 2026
203	  Role: theoretical_framework
204	  Category: grpo_theory
205	  Matched tags: ['GRPO']
206	  Key finding: 提出 Proxy Compression Hypothesis (PCH)：reward hacking 源于 objective compression、 optimization amplification、evaluator-policy co-adaptation 三者交互。 识别了 perception-reasoning decoupling 作为多模态中 reward hacking 的表现之一。
207	
208	  Relevance: 
209	
210	--- Paper 19 ---
211	  Title: Defeating the Training-Inference Mismatch via FP16
212	  Venue: arXiv 2510.26788
213	  Year: 2025
214	  Role: key_evidence
215	  Category: training_precision_rl
216	  Matched tags: ['GRPO']
217	  Key finding: BF16 在 RL fine-tuning 中引入大的 rounding error 导致 training-inference 不一致， BF16 训练常在 150-600 步崩溃。仅切换到 FP16 即可消除不一致， 提供更稳定训练、更快收敛和更优性能，只需改几行代码。
218	
219	  Relevance: 
220	
221	--- Paper 20 ---
222	  Title: R²GRPO: Better LLMs for Scientific Information Extraction with MimicSFT and Relevance and Rule-induced GRPO
223	  Venue: arXiv 2505.22068
224	  Year: 2025
225	  Role: related_method
226	  Category: rl_for_ie
227	  Matched tags: ['GRPO', 'IE/NLP-structured']
228	  Key finding: 两阶段方法：MimicSFT（structured reasoning template，无需高质量 CoT 数据） + R²GRPO（relevance reward + rule-mining reward）， 在科学信息抽取 RE benchmark 上超越 baseline LLM 和 specialized supervised model。
229	
230	  Relevance: 
231	
232	--- Paper 21 ---
233	  Title: ADELIE: Aligning Large Language Models on Information Extraction
234	  Venue: EMNLP 2024
235	  Year: 2024
236	  Role: key_baseline
237	  Category: llm_ie_alignment
238	  Matched tags: ['GRPO', 'IE/NLP-structured']
239	  Key finding: 构建 IEInstruct 高质量 IE alignment 语料库，用 SFT + DPO 训练 ADELIE。 支持 closed/open/on-demand IE 三种模式。 基于 LLaMA-2-7B/LLaMA-3.2-3B/Qwen2.5-1.5B，在多个 held-out IE dataset 上达 SOTA。
240	
241	  Relevance: 
242	
243	--- Paper 22 ---
244	  Title: Evidence-aware Document-level Relation Extraction
245	  Venue: CIKM 2022
246	  Year: 2022
247	  Role: background
248	  Category: evidence_based_docre
249	  Matched tags: ['GRPO', 'IE/NLP-structured']
250	  Key finding: 将 evidence sentence selection 建模为序列决策问题， 用 RL 机制选择支撑关系的 evidence sentences。 在 DocRED 上验证 evidence-aware 方法的有效性。
251	
252	  Relevance: 
253	
254	--- Paper 23 ---
255	  Title: LoRA vs Full Fine-tuning: An Illusion of Equivalence
256	  Venue: arXiv 2410.21228
257	  Year: 2024
258	  Role: key_evidence
259	  Category: lora_qlora_artifacts
260	  Matched tags: ['GRPO']
261	  Key finding: LoRA 和 full fine-tuning 产生结构上根本不同的权重矩阵。LoRA 引入 intruder dimensions—— 奇异值分解中出现新的高秩奇异向量（与预训练权重高度不相似）。Full fine-tuning 不会。 LoRA 的 forgetting 几乎全部集中在 intruder dimensions。 缩小 intruder dimensions 的奇异值可显著恢复预训练分布建模能力， 同时仅微小影响下游任务性能。
262	
263	  Relevance: 
264	
265	--- Paper 24 ---
266	  Title: The Impact of LoRA on the Emergence of Clusters in Transformers
267	  Venue: arXiv 2402.15415
268	  Year: 2024
269	  Role: theoretical_support
270	  Category: lora_qlora_artifacts
271	  Matched tags: ['GRPO']
272	  Key finding: 用 mean-field self-attention toy model 研究 LoRA fine-tuning 的 forgetting 机制。 LoRA 作为低秩扰动作用于交互粒子系统（tokens）。 发现关于扰动范数和 Transformer 深度的 phase transition： 超过某个阈值后从 non-forgetting 转变为 forgetting behavior。 理论上界 time-to-deviation 与扰动大小和谱特性相关。
273	
274	  Relevance: 
275	
276	--- Paper 25 ---
277	  Title: The Impact of Quantization on Large Reasoning Model Reinforcement Learning
278	  Venue: NeurIPS 2025 Workshop (Efficient Reasoning)
279	  Year: 2025
280	  Role: key_evidence
281	  Category: lora_qlora_artifacts
282	  Matched tags: ['GRPO', 'RL']
283	  Key finding: 系统评估量化对 LRM RL 训练的影响。发现 quantization-aware RL training 反而损害学习过程，PTQ 和 QLoRA 表现更好。 post-RL 量化模型和 quantization-aware RL 模型在推理性能上存在显著差距。
284	
285	  Relevance: 
286	
287	--- Paper 26 ---
288	  Title: ReasoningNER: A Reasoning Paradigm for Named Entity Recognition
289	  Venue: arXiv 2511.11978
290	  Year: 2025
291	  Role: direct-competitor
292	  Category: grpo_nlp_applications
293	  Matched tags: ['GRPO', 'IE/NLP-structured']
294	  Key finding: 三阶段 NER 框架：CoT Generation → CoT Tuning → GRPO Reasoning Enhancement。 用 composite reward（entity F1 + format compliance）训练 GRPO policy。 ReasoningNER-8B 零样本超 GPT-4 12.3 F1、超 DeepSeek-R1-32B 8.4 F1， 1.7B 版本超 DeepSeek-R1-8B 10.5 F1。
295	
296	  Relevance: 
297	
298	--- Paper 27 ---
299	  Title: Posterior-GRPO: Rewarding Reasoning Processes in Code Generation
300	  Venue: arXiv 2508.05170
301	  Year: 2025
302	  Role: method-component
303	  Category: grpo_nlp_applications
304	  Matched tags: ['GRPO', 'IE/NLP-structured']
305	  Key finding: 在代码生成中仅对成功输出的推理过程施加 process-based reward（条件 reward）， 有效抑制 reward hacking——模型不能通过错误推理碰巧生成正确代码来获得高 reward。 通过将 reward 条件化于最终正确性，对齐内部推理与代码正确性。
306	
307	  Relevance: 
308	
309	--- Paper 28 ---
310	  Title: PCL-Reasoner-V1.5: Advancing Math Reasoning with Offline Reinforcement Learning
311	  Venue: arXiv 2601.14716
312	  Year: 2026
313	  Role: key_evidence
314	  Category: rsft_offline_rl
315	  Matched tags: ['GRPO', 'RL', 'IE/NLP-structured']
316	  Key finding: 基于 Qwen2.5-32B 的数学推理模型。核心创新是 offline RL 方法， 在训练稳定性和效率上优于 GRPO 等 online RL。 AIME 2024 平均 90.9%，AIME 2025 平均 85.6%， 在 Qwen2.5-32B post-training 中达 SOTA。
317	
318	  Relevance: 
319	
320	--- Paper 29 ---
321	  Title: GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models
322	  Venue: EMNLP 2025
323	  Year: 2025
324	  Role: related_method
325	  Category: grpo_structured
326	  Matched tags: ['GRPO', 'RL', 'IE/NLP-structured']
327	  Key finding: 增强 GRPO：(1) length-regularized rewards 鼓励简洁性； (2) 对错误解的显式惩罚提升精度； (3) difficulty-aware advantage reweighting 增强泛化。 解决 GRPO 的 reward sparsity、verbosity 和难度忽视问题。
328	
329	  Relevance: 
330	
331	--- Paper 30 ---
332	  Title: E-GRPO: Entity-Aware Reward for Group Relative Policy Optimization
333	  Venue: ICLR 2026
334	  Year: 2025
335	  Role: closest_prior_work
336	  Category: grpo_structured
337	  Matched tags: ['GRPO']
338	  Key finding: 提出 entity-aware reward function，对 negative samples 基于 entity match rate 给 partial credit。 利用 ground-truth entities 作为 factual correctness 的 proxy， 区分 "near-miss"（中间推理正确但最终答案错误）和完全失败。
339	
340	  Relevance: 
341	
342	--- Paper 31 ---
343	  Title: RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs
344	  Venue: arXiv 2508.16546
345	  Year: 2025
346	  Role: supporting_evidence
347	  Category: grpo_structured
348	  Matched tags: ['GRPO', 'RL']
349	  Key finding: RL-FT 可恢复 SFT 导致的大部分 OOD 性能损失，但当 SFT 造成严重 overfitting 时 RL 无法完全恢复。 OOD 性能退化和恢复主要与 singular vector 方向旋转相关，而非 singular value 变化。 恢复 top 20% singular values 对应方向可恢复 70-80% OOD 性能。
350	
351	  Relevance: 
352	
353	--- Paper 32 ---
354	  Title: Aligning Instruction-Tuned LLMs for Event Extraction with Multi-objective Reinforcement Learning
355	  Venue: Springer 2025
356	  Year: 2025
357	  Role: related_method
358	  Category: grpo_structured
359	  Matched tags: ['GRPO', 'RL', 'IE/NLP-structured']
360	  Key finding: 将多目标强化学习应用于事件抽取，在 instruction-tuned LLM 基础上用 RL 优化抽取性能。 证明 RL 在 IE 任务中可以有效提升 LLM 的结构化输出质量。
361	
362	  Relevance: 
363	
364	--- Paper 33 ---
365	  Title: How Much is Too Much? Exploring LoRA Rank Trade-offs for Retaining Knowledge and Domain Robustness
366	  Venue: IJCNLP-AACL 2025
367	  Year: 2025
368	  Role: supporting_evidence
369	  Category: qlora_fft_gap
370	  Matched tags: ['GRPO', 'IE/NLP-structured']
371	  Key finding: 中等 rank (r=32-64) 在表征能力和稳定性之间达到最佳平衡。 LoRA 在某些推理任务上可与 full fine-tuning 媲美甚至超越。 跨域评估时 LoRA-tuned 模型展现出 robust generalization， 表明 LoRA 学习的是可迁移的抽象技能而非记忆领域特定事实。
372	
373	  Relevance: 
374	
375	--- Paper 34 ---
376	  Title: RandLoRA: Full-rank Parameter-Efficient Fine-tuning of Large Models
377	  Venue: ICLR 2025
378	  Year: 2025
379	  Role: related_method
380	  Category: qlora_fft_gap
381	  Matched tags: ['GRPO', 'IE/NLP-structured']
382	  Key finding: 通过学习 fixed random matrices 的 diagonal scaling 实现 full-rank 更新， 保持参数效率同时突破 low-rank 限制。 在 vision-language 任务上显著缩小甚至消除 standard fine-tuning 与 LoRA 的性能差距。
383	
384	  Relevance: 
385	
386	--- Paper 35 ---
387	  Title: Ortho-LoRA: Disentangling Task Conflicts in Multi-Task LoRA via Orthogonal Gradient Projection
388	  Venue: arXiv 2601.09684
389	  Year: 2026
390	  Role: related_method
391	  Category: mtl_ie_tradeoff
392	  Matched tags: ['GRPO', 'IE/NLP-structured']
393	  Key finding: 针对 LoRA 的 bipartite 结构设计 gradient projection 方法。 动态将冲突任务梯度投影到彼此的正交补空间，在 LoRA 固有子空间内解决冲突。 解决 multi-task LoRA 中的 negative transfer 问题。
394	
395	  Relevance: 
396	
397	--- Paper 36 ---
398	  Title: Proactive Gradient Conflict Mitigation in Multi-Task Learning: A Sparse Training Perspective
399	  Venue: arXiv 2411.18615
400	  Year: 2024
401	  Role: supporting_evidence
402	  Category: mtl_ie_tradeoff
403	  Matched tags: ['GRPO']
404	  Key finding: 从 Sparse Training 角度缓解 gradient conflict： 选择原始模型参数子集同时学习多任务，冻结其余参数。 将高维空间优化问题转为低维问题，限制每个任务的 gradient update 影响范围。 可与 gradient manipulation 技术结合进一步提升效果。
405	
406	  Relevance: 
407	
408	--- Paper 37 ---
409	  Title: PrefixNLI: Detecting Factual Inconsistencies as Soon as They Arise
410	  Venue: arXiv 2511.01359
411	  Year: 2025
412	  Role: method_component
413	  Category: faithfulness_nli
414	  Matched tags: ['GRPO']
415	  Key finding: 将 NLI 从完整句子推广到任意文本前缀，训练 MiniTruePrefixes 模型。 在 prefix-level entailment 上超越 baseline NLI 模型 5-14 F1。 集成到 controlled decoding 框架后，LLaMA-3.2-3B 匹配 8B 模型的 faithfulness。
416	
417	  Relevance: 
418	
419	--- Paper 38 ---
420	  Title: COREX: Document-level Relation Extraction Framework with Consistent Two-Hop Reasoning and Evidence Sentence Prediction
421	  Venue: IEEE IJCNN 2024
422	  Year: 2024
423	  Role: direct_competitor
424	  Category: evidence_based_docre
425	  Matched tags: ['GRPO', 'IE/NLP-structured']
426	  Key finding: 提出高效 two-hop reasoning 表示，由 evidence prediction 和 RE 联合监督。 修正 Adaptive Focal Loss 解决类别不均衡。 Weighted Fusion Layer 优化 evidence 利用。
427	
428	  Relevance: 
429	
430	--- Paper 39 ---
431	  Title: Accurate and Efficient Fine-Tuning of Quantized Large Language Models Through Optimal Balance in Adaptation
432	  Venue: TACL 2025
433	  Year: 2024
434	  Role: related_analysis
435	  Category: lora_qlora_artifacts
436	  Matched tags: ['GRPO']
437	  Key finding: 识别量化 LLM + LoRA 的不平衡问题：adapter 输入输出过于复杂而有效可训练性不足，导致欠拟合。 Q-BLoRA 简化 adapter 输入输出同时增大 rank 缓解欠拟合。 QA-BLoRA 进一步支持低精度部署。
438	
439	  Relevance: 
440	
441	--- Paper 40 ---
442	  Title: CLoQ: Enhancing Fine-Tuning of Quantized LLMs via Calibrated LoRA Initialization
443	  Venue: arXiv 2501.18475
444	  Year: 2025
445	  Role: related_method
446	  Category: lora_qlora_artifacts
447	  Matched tags: ['GRPO']
448	  Key finding: QLoRA 中量化误差影响 LoRA 训练。CLoQ 用校准数据集最小化原始 LLM 与量化+LoRA 版本的 逐层差异，闭式构造最优 LoRA 初始化，无需反向传播。 在 ultra low-bit 宽度下显著优于现有方法。
449	
450	  Relevance: 
451	
452	--- Paper 41 ---
453	  Title: ESTR-DocRE: an evidence-supervised transformer reasoning framework for document-level relation extraction
454	  Venue: Journal of King Saud University - Computer and Information Sciences (Springer)
455	  Year: 2025
456	  Role: direct_competitor
457	  Category: evidence_supervised_docre
458	  Matched tags: ['GRPO', 'IE/NLP-structured']
459	  Key finding: 统一 evidence awareness 和 cross-entity logical reasoning。ESRM 模块通过 adaptive relevance scoring 提取关键 evidence sentences 并用 multi-head attention 融合 entity representations；TDRM 模块 构建 entity pair joint representations 并通过 transformer 实现跨 pair 信息交换支持 multi-hop reasoning。 四个 DocRE benchmark 上一致优于 strong baselines。
460	
461	  Relevance: 
462	
463	--- Paper 42 ---
464	  Title: QuRL: Efficient Reinforcement Learning with Quantized Rollout
465	  Venue: ICLR 2026
466	  Year: 2026
467	  Role: related_method
468	  Category: quantization_rl_stability
469	  Matched tags: ['GRPO', 'RL']
470	  Key finding: 量化 rollout 加速 RL 训练（rollout 占总训练时间 70%）。提出 Adaptive Clipping Range (ACR) 动态调整 clipping ratio 缓解 full-precision actor 与 quantized actor 之间的 policy ratio 偏移， 防止长期训练崩溃。INT8/FP8 量化实现 20-80% rollout 加速。 关键发现：decoupled PPO objective 在长 horizon 下导致 training collapse， 表现为 quantized actor 和 full-precision actor 之间 divergence 指数增长。
471	
472	  Relevance: 
473	
474	--- Paper 43 ---
475	  Title: QaRL: Rollout-Aligned Quantization-Aware RL for Fast and Stable Training under Training-Inference Mismatch
476	  Venue: arXiv 2604.07853
477	  Year: 2026
478	  Role: related_method
479	  Category: quantization_rl_stability
480	  Matched tags: ['GRPO', 'IE/NLP-structured']
481	  Key finding: 量化 rollout 中 long-form responses 产生 repetitive garbled tokens (error tokens)。 QaRL 用 TBPO (Trust-Band Policy Optimization) 的 sequence-level dual clipping 约束更新在 trust region 内。 Qwen3-30B-A3B MoE 上比 quantized-rollout baseline 高 +5.5。
482	
483	  Relevance: 
484	
485	--- Paper 44 ---
486	  Title: Parameter-Efficient Continual Fine-Tuning: A Survey
487	  Venue: arXiv 2504.13822
488	  Year: 2025
489	  Role: background
490	  Category: peft_forgetting
491	  Matched tags: ['GRPO']
492	  Key finding: 系统综述 PECFT 方法如何在参数高效微调下缓解 catastrophic forgetting。 PEFT 冻结大部分参数保留旧任务知识，但连续微调多任务仍有 forgetting 问题。 CL-Plugins 等方法结合 adapter modules 和 continual learning 策略。
493	
494	  Relevance: 
495	
496	--- Paper 45 ---
497	  Title: From Verifiable Dot to Reward Chain: Harnessing Verifiable Reference-based Rewards for Reinforcement Learning of Open-ended Generation (RLVRR)
498	  Venue: ICLR 2026
499	  Year: 2026
500	  Role: method_component
501	  Category: rlvr_general_domains
502	  Matched tags: ['RL', 'IE/NLP-structured']
503	  Key finding: RLVRR 从 high-quality references 中提取 ordered linguistic signals（reward chain）， 分解为 content（关键词确定性验证）和 style（LLM-based 风格验证）两个维度。 在 10+ benchmarks 上大幅超越 10× 数据的 SFT 和先进 reward models。
504	
505	  Relevance: 
506	
507	--- Paper 46 ---
508	  Title: FP8-RL: A Practical and Stable Low-Precision Stack for LLM Reinforcement Learning
509	  Venue: arXiv 2601.18150
510	  Year: 2026
511	  Role: related_method
512	  Category: quantization_rl_stability
513	  Matched tags: ['GRPO', 'RL']
514	  Key finding: FP8 RL 训练中 policy weights 每步变化需重复量化同步，低精度 rollout 偏离高精度 policy 导致 train-inference mismatch 和训练不稳定。MoE 架构中精度差异导致 expert routing 不一致， routing inconsistencies 随训练累积使 mismatch KL 逐渐增大。 通过 importance-sampling-based rollout correction 缓解，实现 44% rollout 加速。
515	
516	  Relevance: 
517	
518	--- Paper 47 ---
519	  Title: Jet-RL: Enabling On-Policy FP8 Reinforcement Learning with Unified Training and Rollout Precision Flow
520	  Venue: arXiv 2601.14243
521	  Year: 2026
522	  Role: related_method
523	  Category: quantization_rl_stability
524	  Matched tags: ['GRPO', 'RL']
525	  Key finding: BF16-train + FP8-rollout 策略导致严重训练不稳定和灾难性准确率崩溃（catastrophic accuracy collapse）， 根因是 off-policy 性质引入的训练-推理数值 mismatch。统一 FP8 精度消除此差异， 实现 41% training 加速和 16% 端到端加速，同时维持稳定收敛。
526	
527	  Relevance: 
528	
529	--- Paper 48 ---
530	  Title: BitRL: Reinforcement Learning with 1-bit Quantized Language Models for Resource-Constrained Edge Deployment
531	  Venue: arXiv 2604.24273
532	  Year: 2026
533	  Role: background
534	  Category: quantization_rl_stability
535	  Matched tags: ['GRPO', 'RL']
536	  Key finding: 首个系统性框架将 1-bit 量化 LLM（BitNet b1.58，三值权重）与 RL 结合。 理论分析将三值量化建模为 structured parameter perturbation，推导 quantized policy gradient 的收敛界。 揭示极端量化下 exploration-stability 的 trade-off——极低精度限制探索能力但保持训练稳定。 维持 85-98% 的 task performance。
537	
538	  Relevance: 
539	
540	--- Paper 49 ---
541	  Title: Imbalanced Gradients in RL Post-Training of Multi-Task LLMs
542	  Venue: Findings of EACL 2026
543	  Year: 2025
544	  Role: closest_prior_work
545	  Category: multi_task_rl_gradient_imbalance
546	  Matched tags: ['GRPO', 'IE/NLP-structured']
547	  Key finding: 多任务 RL post-training 中某些任务产生显著更大的梯度，偏置更新方向。 大梯度任务不一定获得更大学习收益——gradient magnitude 与 performance improvement 不相关。 常见训练统计量（reward, advantage, token length）无法解释此不平衡， 暗示不平衡源于 inherent task differences。
548	
549	  Relevance: 
550	
551	--- Paper 50 ---
552	  Title: Stabilizing Reinforcement Learning with LLMs: Formulation and Practices
553	  Venue: arXiv 2512.01374
554	  Year: 2025
555	  Role: theoretical_support
556	  Category: quantization_rl_stability
557	  Matched tags: ['GRPO', 'RL']
558	  Key finding: 通过一阶近似证明 sequence-level reward 可用 surrogate token-level objective 优化， 但前提是 training-inference discrepancy 和 policy staleness 最小化。 Token-level importance sampling 是校正 train-inference 差异的必要组件——移除后训练崩溃。 30B MoE 模型上数十万 GPU 小时的实验验证。
559	
560	  Relevance: 
561	
562	Total matches: 50
563	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59e0b099-3c9f-4dca-99b0-c20ac1e9b348",
  "isSidechain": true,
  "promptId": "00163f99-7857-4276-afc6-24e9276d86ac",
  "agentId": "a4b1818a3cd108cba",
  "type": "user",
  "uuid": "ac64647b-5181-4741-a6a4-7f13ac9e5752",
  "sourceToolAssistantUUID": "59e0b099-3c9f-4dca-99b0-c20ac1e9b348",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T20:14:54.445Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Gqkr28xMbJRfUcHFsiNH7q`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/lit_map_actual.json', 'r') as f:\n    lit_map = json.load(f)\n\npapers = lit_map['papers']\n\n# ============================================================\n# 4. Papers about learning curves or training dynamics of RL methods on NLP tasks\n# ============================================================\nprint(\"=\" * 80)\nprint(\"CATEGORY 4: Papers about learning curves / training dynamics of RL for NLP\")\nprint(\"=\" * 80)\n\nkeywords = ['learning curve', 'training dynamic', 'training dynamics', 'convergence', \n            'entropy collapse', 'mode collapse', 'reward hacking', 'training stability',\n            'training instability', 'training collapse', 'gradient dynamics',\n            'reward std', 'reward variance', 'advantage variance', 'frac_zero',\n            'phase transition', 'early training', 'training progression']\n\nresults = []\nfor p in papers:\n    all_text = json.dumps(p, ensure_ascii=False).lower()\n    # Also require some RL or NLP context\n    has_rl_context = any(kw in all_text for kw in ['grpo', 'reinforcement', 'rl ', 'ppo', 'rlhf', 'rlvr', 'policy optimization'])\n    \n    matched_kws = [kw for kw in keywords if kw in all_text]\n    if matched_kws and has_rl_context:\n        results.append((p, matched_kws))\n\nfor i, (p, kws) in enumerate(results, 1):\n    print(f\"\\n--- Paper {i} ---\")\n    print(f\"  Title: {p.get('title')}\")\n    print(f\"  Venue: {p.get('venue')}\")\n    print(f\"  Year: {p.get('year')}\")\n    print(f\"  Role: {p.get('role')}\")\n    print(f\"  Category: {p.get('category')}\")\n    print(f\"  Matched keywords: {kws}\")\n    print(f\"  Key finding: {p.get('key_finding', '')}\")\n    print(f\"  Relevance: {p.get('relevance_to_ced_stabilizer', '')}\")\n\nprint(f\"\\nTotal matches: {len(results)}\")\n\nPYEOF\n",
  "description": "Find papers about learning curves / training dynamics of RL for NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac64647b-5181-4741-a6a4-7f13ac9e5752",
  "isSidechain": true,
  "agentId": "a4b1818a3cd108cba",
  "requestId": "req_011CbAeW2iLALWrrTRbeAGU2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "357aaf2a-43ad-4612-8f39-07acdaef2b2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QRgZbpimyNvyYcuW2YyxzD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12473,
      "cache_read_input_tokens": 29088,
      "output_tokens": 662,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12473
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 662,
          "cache_read_input_tokens": 29088,
          "cache_creation_input_tokens": 12473,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12473,
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

_source line 30 · 2026-05-18T20:14:54.539Z_

<details><summary>↩ Tool result · `toolu_01Gqkr28xMbJRfUcHFsiNH7q`</summary>

```text
================================================================================
CATEGORY 4: Papers about learning curves / training dynamics of RL for NLP
================================================================================

--- Paper 1 ---
  Title: Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards
  Venue: arXiv 2511.03710
  Year: 2025
  Role: theoretical_support
  Category: reward_diversity
  Matched keywords: ['reward variance']
  Key finding: RLVR 中 per-prompt 均值 baseline 在低 generation 数下估计不准导致高 variance 梯度。 用 James-Stein shrinkage 混合 per-prompt 和 cross-prompt 均值， 构造可证明更低 variance 的 policy gradient estimator。

  Relevance: 理论支持：reward variance 对 gradient estimation 质量至关重要。 CED 的额外 reward 维度提供更丰富的 per-group variance，间接起到 variance 维持效果。


--- Paper 2 ---
  Title: Reward Shaping to Mitigate Reward Hacking in RLHF
  Venue: arXiv 2502.18770
  Year: 2025
  Role: background
  Category: reward_diversity
  Matched keywords: ['reward hacking']
  Key finding: RL reward 应有界且先快速增长后缓慢收敛。系统研究 reward shaping 原则， 好的 reward 形状能抑制 reward hacking 并提升训练稳定性。

  Relevance: CED reward 的 0-1 对比判别结构天然满足有界性， 且 evidence quality 的渐进提升符合"先快后慢"的 reward shaping 原则。


--- Paper 3 ---
  Title: DAPO: An Open-Source LLM Reinforcement Learning System at Scale
  Venue: NeurIPS 2025
  Year: 2025
  Role: key_baseline
  Category: mode_collapse_prevention
  Matched keywords: ['entropy collapse', 'mode collapse', 'frac_zero']
  Key finding: Naive GRPO 存在 entropy collapse（policy 熵快速下降→输出同质化）。 根因：clipping 不对称性——概率 0.01 的 token 最多增到 0.012，而概率 0.9 的 token 可达 1.08， 低概率 token 难以增长，抑制探索。DAPO 提出 Clip-Higher（εhigh=0.28 > εlow=0.2） 为低概率 token 留更大增长空间，加 Dynamic Sampling 过滤 accuracy=0 或 1 的 prompt （这些 prompt 产生零梯度，降低有效 batch size）。在 AIME 2024 达 50 分超越 DeepSeek-R1-Zero。

  Relevance: DAPO 从 optimization 技巧角度解决 entropy collapse。CED reward 从 reward design 层面 防止 mode collapse——evidence quality 维度确保 reward 组内有足够 variance， 不会出现 all-same-reward 的零梯度 prompt。DAPO 的 Dynamic Sampling 过滤 accuracy=0/1 prompt 与我们观察到的 frac_zero_std→0.8 现象本质相同：extraction-only reward 下大量 prompt 产生零 advantage，CED 从源头（reward 设计）而非后处理（过滤）解决这个问题。


--- Paper 4 ---
  Title: Dr. GRPO: Removing Optimization Bias in GRPO
  Venue: COLM 2025
  Year: 2025
  Role: related_analysis
  Category: mode_collapse_prevention
  Matched keywords: ['frac_zero']
  Key finding: GRPO 的 std 归一化引入两个 bias：(1) difficulty bias——std(r) 归一化对低 variance 组 （全对/全错）给予过高 advantage 权重，trivial question 主导训练信号； (2) length bias——per-token loss 的 1/|o_i| 项使长的错误回答被 under-penalize。 当 std(r)→0 时 advantage 爆炸或未定义，梯度数值不稳定。 Dr. GRPO 移除 std 归一化，用无偏 Monte Carlo advantage：Ã = R(q,o_i) - mean(R)。

  Relevance: 与我们的实验发现高度一致：extraction-only reward 下 frac_zero_std→0.8 正是 Dr. GRPO 分析的 difficulty bias 极端情况——大量 prompt 的所有 rollout 得到相同 F1， std→0 导致 advantage 异常。CED 通过增加 reward 维度天然维持 reward_std>0， 从 reward 设计而非算法修改角度避免了 Dr. GRPO 发现的 bias。


--- Paper 5 ---
  Title: GVPO: Group Variance Policy Optimization for LLM Post-Training
  Venue: NeurIPS 2025
  Year: 2025
  Role: alternative_framework
  Category: mode_collapse_prevention
  Matched keywords: ['reward variance']
  Key finding: 将 KL 约束 reward 最大化的解析解直接嵌入梯度权重， variance 项自然平衡 exploration 与 exploitation，维持适度 entropy。

  Relevance: GVPO 的 variance 项机制与 CED 维持 reward variance 的效果功能类似， 但 GVPO 是算法层面 implicit regularization，CED 是 reward 层面 explicit structure。


--- Paper 6 ---
  Title: DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO
  Venue: arXiv 2512.21514
  Year: 2025
  Role: parallel_work
  Category: mode_collapse_prevention
  Matched keywords: ['mode collapse']
  Key finding: 图像生成中 GRPO 后期输出同质化。distributional reward modeling（谱聚类+exploratory reward） 和 structure-aware regularization 实现 13-18% 语义多样性提升。

  Relevance: 跨域验证了 GRPO mode collapse 的普遍性，distributional reward 思路与 CED 精神相近—— 都是通过 reward 层面结构化信号维持输出多样性。


--- Paper 7 ---
  Title: Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients
  Venue: arXiv 2601.23135
  Year: 2025
  Role: theoretical_support
  Category: mode_collapse_prevention
  Matched keywords: ['reward std']
  Key finding: GRPO 的 reward_std 归一化在温和条件下提供严格优于未归一化 REINFORCE 的收敛速率， 收益由 prompt 间平均 reward std 刻画。

  Relevance: 直接理论支撑：reward_std 越大收敛越好。CED 通过 evidence quality 维度维持高 reward_std， 从该理论看 CED 的稳定性优势是 reward_std 维持带来的收敛速率优势。


--- Paper 8 ---
  Title: R1-RE: Cross-Domain Relation Extraction with RLVR
  Venue: arXiv 2507.04642
  Year: 2025
  Role: direct_competitor
  Category: rl_for_ie
  Matched keywords: ['reward variance', 'frac_zero']
  Key finding: 首个将 RLVR（GRPO + verifiable reward）用于关系抽取的框架。 将 RE 重构为推理任务，R1-RE-7B 在跨域 OOD 准确率约 70%，媲美 GPT-4o。 Reward 设计：format reward (+1/-3) + metric reward (+2/-1.5)，先验证格式再加准确度。 triplet extraction 用 F1-based reward（entity weight=1, triplet weight=3）。 未报告 catastrophic forgetting——GRPO 训练后在 MATH-500/IFEval/GPQA 上性能不降反升， 说明句子级 RE 的简单 reward 结构足以稳定 GRPO 训练。

  Relevance: 

--- Paper 9 ---
  Title: MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems
  Venue: arXiv 2509.22047
  Year: 2025
  Role: related_method
  Category: multi_objective_grpo
  Matched keywords: ['reward hacking']
  Key finding: GRPO 在多目标设置下易发生 reward hacking——只优化一个目标而牺牲其他目标。 MO-GRPO 用 variance-based normalization 自动平衡多个 reward function 的权重， 在多臂赌博机、控制、机器翻译、指令遵从四个域上实现稳定学习。

  Relevance: 

--- Paper 10 ---
  Title: Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges
  Venue: arXiv 2604.13602
  Year: 2026
  Role: theoretical_framework
  Category: grpo_theory
  Matched keywords: ['reward hacking']
  Key finding: 提出 Proxy Compression Hypothesis (PCH)：reward hacking 源于 objective compression、 optimization amplification、evaluator-policy co-adaptation 三者交互。 识别了 perception-reasoning decoupling 作为多模态中 reward hacking 的表现之一。

  Relevance: 

--- Paper 11 ---
  Title: The Impact of LoRA on the Emergence of Clusters in Transformers
  Venue: arXiv 2402.15415
  Year: 2024
  Role: theoretical_support
  Category: lora_qlora_artifacts
  Matched keywords: ['phase transition']
  Key finding: 用 mean-field self-attention toy model 研究 LoRA fine-tuning 的 forgetting 机制。 LoRA 作为低秩扰动作用于交互粒子系统（tokens）。 发现关于扰动范数和 Transformer 深度的 phase transition： 超过某个阈值后从 non-forgetting 转变为 forgetting behavior。 理论上界 time-to-deviation 与扰动大小和谱特性相关。

  Relevance: 

--- Paper 12 ---
  Title: ReasoningNER: A Reasoning Paradigm for Named Entity Recognition
  Venue: arXiv 2511.11978
  Year: 2025
  Role: direct-competitor
  Category: grpo_nlp_applications
  Matched keywords: ['reward variance']
  Key finding: 三阶段 NER 框架：CoT Generation → CoT Tuning → GRPO Reasoning Enhancement。 用 composite reward（entity F1 + format compliance）训练 GRPO policy。 ReasoningNER-8B 零样本超 GPT-4 12.3 F1、超 DeepSeek-R1-32B 8.4 F1， 1.7B 版本超 DeepSeek-R1-8B 10.5 F1。

  Relevance: 

--- Paper 13 ---
  Title: Posterior-GRPO: Rewarding Reasoning Processes in Code Generation
  Venue: arXiv 2508.05170
  Year: 2025
  Role: method-component
  Category: grpo_nlp_applications
  Matched keywords: ['reward hacking']
  Key finding: 在代码生成中仅对成功输出的推理过程施加 process-based reward（条件 reward）， 有效抑制 reward hacking——模型不能通过错误推理碰巧生成正确代码来获得高 reward。 通过将 reward 条件化于最终正确性，对齐内部推理与代码正确性。

  Relevance: 

--- Paper 14 ---
  Title: Regularized Best-of-N Sampling with Minimum Bayes Risk Objective for Language Model Alignment
  Venue: NAACL 2025
  Year: 2024
  Role: related_method
  Category: inference_time_reranking
  Matched keywords: ['reward hacking']
  Key finding: MBR-BoN：用 Minimum Bayes Risk 目标作为 proximity regularizer 缓解 reward hacking。 MBR 目标量化 response 与 reference policy 的接近程度。 在 AlpacaFarm 和 hh-rlhf 上优于 vanilla BoN 和 MBR decoding。

  Relevance: 

--- Paper 15 ---
  Title: QuRL: Efficient Reinforcement Learning with Quantized Rollout
  Venue: ICLR 2026
  Year: 2026
  Role: related_method
  Category: quantization_rl_stability
  Matched keywords: ['training collapse']
  Key finding: 量化 rollout 加速 RL 训练（rollout 占总训练时间 70%）。提出 Adaptive Clipping Range (ACR) 动态调整 clipping ratio 缓解 full-precision actor 与 quantized actor 之间的 policy ratio 偏移， 防止长期训练崩溃。INT8/FP8 量化实现 20-80% rollout 加速。 关键发现：decoupled PPO objective 在长 horizon 下导致 training collapse， 表现为 quantized actor 和 full-precision actor 之间 divergence 指数增长。

  Relevance: 

--- Paper 16 ---
  Title: Reinforcement Fine-Tuning Naturally Mitigates Forgetting in Continual Post-Training
  Venue: arXiv 2507.05386
  Year: 2025
  Role: related_analysis
  Category: rl_vs_forgetting
  Matched keywords: ['reward variance']
  Key finding: 对比 SFT 和 RFT：SFT 导致 catastrophic forgetting，而 RFT 的梯度更新被 reward variance 自然缩放，形成 data-dependent regularizer 保护已有知识。 Qwen2.5-VL-7B-Instruct 上 7 个多模态任务验证。 还提出 rollout-based instance filtering 提升 RFT 稳定性和效率。

  Relevance: 

--- Paper 17 ---
  Title: The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking
  Venue: ICML 2025
  Year: 2025
  Role: related_method
  Category: reward_hacking_diagnostics
  Matched keywords: ['reward hacking']
  Key finding: 发现 Energy Loss Phenomenon：LLM 最后一层的 energy loss（L1 norm 差值）在 RL 训练中 持续增加，过度增加标志 reward hacking。理论证明 energy loss 增加降低 contextual relevance 上界。 提出 EPPO（Energy loss-aware PPO）在 reward 计算中惩罚 energy loss 增加。 EPPO 可解释为 entropy-regularized RL。

  Relevance: 

Total matches: 17
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "357aaf2a-43ad-4612-8f39-07acdaef2b2e",
  "isSidechain": true,
  "promptId": "00163f99-7857-4276-afc6-24e9276d86ac",
  "agentId": "a4b1818a3cd108cba",
  "type": "user",
  "uuid": "9cf9e5f6-aa22-433c-aa60-7c7474a91b38",
  "sourceToolAssistantUUID": "357aaf2a-43ad-4612-8f39-07acdaef2b2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-18T20:14:58.804Z_

Now let me also check for a few papers that may have been missed, specifically looking for "REAR" and "EvidenceRL" which appeared as direct competitors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cf9e5f6-aa22-433c-aa60-7c7474a91b38",
  "isSidechain": true,
  "agentId": "a4b1818a3cd108cba",
  "requestId": "req_011CbAeWyJiwJSrftEBJ3NXK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d50130b0-a4b8-4202-9167-30c10dbb3f43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dr1mi1XRiys4JqaLG7W5qq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4844,
      "cache_read_input_tokens": 41561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4844,
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

_source line 32 · 2026-05-18T20:15:06.238Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012fcKNF2ozh81CnqEqvZUNf`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/lit_map_actual.json', 'r') as f:\n    lit_map = json.load(f)\n\npapers = lit_map['papers']\n\n# Get all distinct roles and categories\nroles = set()\ncategories = set()\nfor p in papers:\n    roles.add(p.get('role', 'N/A'))\n    categories.add(p.get('category', 'N/A'))\n\nprint(\"All roles:\", sorted(roles))\nprint()\nprint(\"All categories:\", sorted(categories))\nprint()\n\n# Find papers with role containing \"competitor\" (case insensitive)\nprint(\"\\n--- Papers with 'competitor' in role ---\")\nfor p in papers:\n    role = str(p.get('role', '')).lower()\n    if 'competitor' in role or 'closest' in role:\n        print(f\"  [{p.get('role')}] {p.get('title')} ({p.get('venue')}, {p.get('year')})\")\n        print(f\"    Category: {p.get('category')}\")\n\n# Also find the R1-RE paper's full details since it was listed as direct_competitor (underscore)\nprint(\"\\n--- Papers with role 'direct_competitor' (underscore variant) ---\")\nfor p in papers:\n    if p.get('role') == 'direct_competitor':\n        print(f\"  Title: {p.get('title')}\")\n        print(f\"  Venue: {p.get('venue')}\")\n        print(f\"  Year: {p.get('year')}\")\n        print(f\"  Category: {p.get('category')}\")\n        print(f\"  Key finding: {p.get('key_finding', '')[:200]}\")\n        print()\n\nPYEOF\n",
  "description": "Get all roles/categories and find all competitor-type papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d50130b0-a4b8-4202-9167-30c10dbb3f43",
  "isSidechain": true,
  "agentId": "a4b1818a3cd108cba",
  "requestId": "req_011CbAeWyJiwJSrftEBJ3NXK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a624d51-4703-402d-bd51-7d4836c99b0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dr1mi1XRiys4JqaLG7W5qq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4844,
      "cache_read_input_tokens": 41561,
      "output_tokens": 554,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4844
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 554,
          "cache_read_input_tokens": 41561,
          "cache_creation_input_tokens": 4844,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4844,
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

_source line 33 · 2026-05-18T20:15:06.395Z_

<details><summary>↩ Tool result · `toolu_012fcKNF2ozh81CnqEqvZUNf`</summary>

```text
All roles: ['alternative_framework', 'background', 'background_survey', 'closest_competitor', 'closest_contrastive_precedent', 'closest_docre_precedent', 'closest_prior_work', 'comprehensive_survey', 'conceptual_support', 'dataset_revision', 'direct-competitor', 'direct_competitor', 'empirical_evidence', 'empirical_support', 'evaluation', 'evaluation_framework', 'evaluation_method', 'formal_framework', 'foundational_dataset', 'key_baseline', 'key_conceptual_framework', 'key_evidence', 'key_theoretical_support', 'method-component', 'method_component', 'methodological_precedent', 'parallel_work', 'related_analysis', 'related_method', 'supporting_evidence', 'survey', 'theoretical_foundation', 'theoretical_framework', 'theoretical_insight', 'theoretical_support']

All categories: ['contrastive_reward', 'docre_foundational', 'evaluation_generative_re', 'evidence_based_docre', 'evidence_cost_generative_ie', 'evidence_docre', 'evidence_generation_tradeoff', 'evidence_grounded_rl', 'evidence_reward', 'evidence_supervised_docre', 'faithfulness_accuracy_tradeoff', 'faithfulness_benchmark', 'faithfulness_cost', 'faithfulness_decay', 'faithfulness_nli', 'faithfulness_structured', 'grpo_nlp_applications', 'grpo_structured', 'grpo_theory', 'inference_time_reranking', 'knowledge_distillation_docre', 'latent_vs_explicit_reasoning', 'llm_docre', 'llm_ie_alignment', 'lora_qlora_artifacts', 'mode_collapse_prevention', 'mtl_ie_tradeoff', 'multi_objective_grpo', 'multi_objective_rl', 'multi_task_lora_decoupling', 'multi_task_rl_gradient_imbalance', 'negative_transfer', 'peft_forgetting', 'qlora_fft_gap', 'quantization_rl_stability', 'reranking_verification_bridge', 'reward_diversity', 'reward_hacking_diagnostics', 'rl_for_ie', 'rl_vs_forgetting', 'rlvr_general_domains', 'rsft_methodology', 'rsft_offline_rl', 'self_training_bootstrapping', 'survey', 'training_precision_rl', 'unfaithful_reasoning']


--- Papers with 'competitor' in role ---
  [closest_prior_work] GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (ICML 2026, 2025)
    Category: reward_diversity
  [closest_contrastive_precedent] Improving Reinforcement Learning from Human Feedback Using Contrastive Rewards (arXiv 2403.07708, 2024)
    Category: contrastive_reward
  [direct_competitor] R1-RE: Cross-Domain Relation Extraction with RLVR (arXiv 2507.04642, 2025)
    Category: rl_for_ie
  [closest_docre_precedent] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion (ACL Findings 2022, 2022)
    Category: evidence_generation_tradeoff
  [closest_competitor] EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models (arXiv 2603.19532, 2026)
    Category: evidence_grounded_rl
  [direct-competitor] DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction (EACL 2023, 2023)
    Category: evidence_based_docre
  [direct-competitor] CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction (arXiv 2504.06529, 2025)
    Category: evidence_based_docre
  [direct-competitor] QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs (arXiv 2510.11696, 2025)
    Category: lora_qlora_artifacts
  [direct-competitor] ReasoningNER: A Reasoning Paradigm for Named Entity Recognition (arXiv 2511.11978, 2025)
    Category: grpo_nlp_applications
  [direct-competitor] OREO: Offline Reinforcement Learning for LLM Multi-Step Reasoning (arXiv 2412.16145, 2024)
    Category: rsft_offline_rl
  [closest_prior_work] E-GRPO: Entity-Aware Reward for Group Relative Policy Optimization (ICLR 2026, 2025)
    Category: grpo_structured
  [closest_prior_work] C-LoRAE: Collaborative Multi-LoRA Experts with Achievement-based Multi-Tasks Loss for Unified Multimodal Information Extraction (arXiv 2505.06303, 2025)
    Category: mtl_ie_tradeoff
  [direct_competitor] RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning (arXiv 2601.09253, 2026)
    Category: rsft_methodology
  [direct_competitor] DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning (ICML 2025, 2025)
    Category: llm_docre
  [direct_competitor] COREX: Document-level Relation Extraction Framework with Consistent Two-Hop Reasoning and Evidence Sentence Prediction (IEEE IJCNN 2024, 2024)
    Category: evidence_based_docre
  [direct_competitor] ESTR-DocRE: an evidence-supervised transformer reasoning framework for document-level relation extraction (Journal of King Saud University - Computer and Information Sciences (Springer), 2025)
    Category: evidence_supervised_docre
  [closest_prior_work] Imbalanced Gradients in RL Post-Training of Multi-Task LLMs (Findings of EACL 2026, 2025)
    Category: multi_task_rl_gradient_imbalance
  [direct_competitor] It Takes Two Flints to Make a Fire: Multitask Learning of Neural Relation and Explanation Classifiers (Computational Linguistics, Vol. 49, Issue 1, 2023)
    Category: evidence_cost_generative_ie
  [direct_competitor] Entity and Evidence Guided Relation Extraction for DocRED (RepL4NLP @ ACL 2021, 2021)
    Category: evidence_cost_generative_ie
  [direct_competitor] SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction (NAACL 2022, 2022)
    Category: evidence_supervised_docre

--- Papers with role 'direct_competitor' (underscore variant) ---
  Title: R1-RE: Cross-Domain Relation Extraction with RLVR
  Venue: arXiv 2507.04642
  Year: 2025
  Category: rl_for_ie
  Key finding: 首个将 RLVR（GRPO + verifiable reward）用于关系抽取的框架。 将 RE 重构为推理任务，R1-RE-7B 在跨域 OOD 准确率约 70%，媲美 GPT-4o。 Reward 设计：format reward (+1/-3) + metric reward (+2/-1.5)，先验证格式再加准确度。 triplet extraction 用 F1-based rewar

  Title: RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning
  Venue: arXiv 2601.09253
  Year: 2026
  Category: rsft_methodology
  Key finding: RSFT 的 hard rejection 丢弃大量计算昂贵的负样本。 RIFT 保留所有轨迹，用标量 reward 重新加权 loss， 正 reward 样本鼓励正确行为，负 reward 样本提供反向梯度。 引入 stabilized loss 解决 naive reward integration 的训练坍塌问题。


  Title: DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning
  Venue: ICML 2025
  Year: 2025
  Category: llm_docre
  Key finding: 构建 Document-level Knowledge Graph 捕获实体间结构信息， 结合 Sentence-level Semantic RAG 检索相关上下文语义信息。 设计 hybrid-prompt tuning 方法在 LLM 上集成结构和语义理解。


  Title: COREX: Document-level Relation Extraction Framework with Consistent Two-Hop Reasoning and Evidence Sentence Prediction
  Venue: IEEE IJCNN 2024
  Year: 2024
  Category: evidence_based_docre
  Key finding: 提出高效 two-hop reasoning 表示，由 evidence prediction 和 RE 联合监督。 修正 Adaptive Focal Loss 解决类别不均衡。 Weighted Fusion Layer 优化 evidence 利用。


  Title: ESTR-DocRE: an evidence-supervised transformer reasoning framework for document-level relation extraction
  Venue: Journal of King Saud University - Computer and Information Sciences (Springer)
  Year: 2025
  Category: evidence_supervised_docre
  Key finding: 统一 evidence awareness 和 cross-entity logical reasoning。ESRM 模块通过 adaptive relevance scoring 提取关键 evidence sentences 并用 multi-head attention 融合 entity representations；TDRM 模块 构建 entity pair joint repre

  Title: It Takes Two Flints to Make a Fire: Multitask Learning of Neural Relation and Explanation Classifiers
  Venue: Computational Linguistics, Vol. 49, Issue 1
  Year: 2023
  Category: evidence_cost_generative_ie
  Key finding: Joint training of relation classifier + explanation sequence labeler (extractive rationale)。 Joint training 不仅不损害 RE，反而提升 ~4% F1 on CoNLL04。 Explanation classifier 操作在 extractive features 上，保证 faithfu

  Title: Entity and Evidence Guided Relation Extraction for DocRED
  Venue: RepL4NLP @ ACL 2021
  Year: 2021
  Category: evidence_cost_generative_ie
  Key finding: E2GRE: DocRE 上首个 joint evidence prediction + relation extraction 框架。 利用 entity-guided input 和 pretrained LM attention 作为 evidence 特征。 Joint training 在 RE 和 evidence prediction 上均有增益，达到 DocRED leaderbo

  Title: SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction
  Venue: NAACL 2022
  Year: 2022
  Category: evidence_supervised_docre
  Key finding: 通过 supervising intermediate steps（evidence retrieval）来提升 DocRE。 两阶段 evidence retrieval：pooled evidence retrieval 区分有/无 supporting sentences 的 entity pairs， fine-grained evidence retrieval 为每个 relation
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a624d51-4703-402d-bd51-7d4836c99b0a",
  "isSidechain": true,
  "promptId": "00163f99-7857-4276-afc6-24e9276d86ac",
  "agentId": "a4b1818a3cd108cba",
  "type": "user",
  "uuid": "2dee7dec-37be-4dee-af31-f6d70b996291",
  "sourceToolAssistantUUID": "7a624d51-4703-402d-bd51-7d4836c99b0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-18T20:16:34.033Z_

Now I have all the data. Let me compile the complete findings.

---

## Complete Analysis Results

### CATEGORY 1: Papers with role "direct-competitor" (or "direct_competitor")

The literature map uses two variants: `direct-competitor` (hyphen) and `direct_competitor` (underscore). Combined, there are **13 direct competitor papers**:

| # | Title | Venue | Year | Category | Notes on rejection sampling / selection strategy |
|---|-------|-------|------|----------|--------------------------------------------------|
| 1 | **DREEAM**: Guiding Attention with Evidence for Improving Document-Level Relation Extraction | EACL 2023 | 2023 | evidence_based_docre | None |
| 2 | **CDER**: Collaborative Evidence Retrieval for Document-level Relation Extraction | arXiv 2504.06529 | 2025 | evidence_based_docre | None |
| 3 | **QeRL**: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs | arXiv 2510.11696 | 2025 | lora_qlora_artifacts | None |
| 4 | **ReasoningNER**: A Reasoning Paradigm for Named Entity Recognition | arXiv 2511.11978 | 2025 | grpo_nlp_applications | Contains "reward variance" keyword in broader text (GRPO composite reward design) but no explicit rejection sampling ablation |
| 5 | **OREO**: Offline Reinforcement Learning for LLM Multi-Step Reasoning | arXiv 2412.16145 | 2024 | rsft_offline_rl | Mentions RSFT context (offline RL vs RSFT comparison) |
| 6 | **R1-RE**: Cross-Domain Relation Extraction with RLVR | arXiv 2507.04642 | 2025 | rl_for_ie | RSFT context (GRPO + verifiable reward for RE); F1-based reward design but no selection strategy ablation reported |
| 7 | **RIFT**: Repurposing Negative Samples via Reward-Informed Fine-Tuning | arXiv 2601.09253 | 2026 | rsft_methodology | Directly about RSFT's limitations (hard rejection discards negative samples); proposes reward-informed reweighting instead |
| 8 | **DocKS-RAG**: Optimizing Document-Level RE through LLM-Enhanced Hybrid Prompt Tuning | ICML 2025 | 2025 | llm_docre | None |
| 9 | **COREX**: Document-level RE with Consistent Two-Hop Reasoning and Evidence Sentence Prediction | IEEE IJCNN 2024 | 2024 | evidence_based_docre | None |
| 10 | **ESTR-DocRE**: Evidence-supervised Transformer Reasoning Framework for DocRE | J. King Saud Univ. (Springer) | 2025 | evidence_supervised_docre | None |
| 11 | **It Takes Two Flints to Make a Fire**: Multitask Learning of Neural Relation and Explanation Classifiers | Computational Linguistics 49(1) | 2023 | evidence_cost_generative_ie | None |
| 12 | **Entity and Evidence Guided Relation Extraction for DocRED** (E2GRE) | RepL4NLP @ ACL 2021 | 2021 | evidence_cost_generative_ie | None |
| 13 | **SAIS**: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction | NAACL 2022 | 2022 | evidence_supervised_docre | None |

Additionally, several papers have `closest_prior_work` or `closest_competitor` roles:
- **GDPO** (ICML 2026) -- closest_prior_work, reward_diversity
- **E-GRPO** (ICLR 2026) -- closest_prior_work, grpo_structured
- **EvidenceRL** (arXiv 2603.19532, 2026) -- closest_competitor, evidence_grounded_rl
- **Improving RLHF Using Contrastive Rewards** (arXiv 2403.07708, 2024) -- closest_contrastive_precedent
- **Eider** (ACL Findings 2022) -- closest_docre_precedent
- **C-LoRAE** (arXiv 2505.06303, 2025) -- closest_prior_work, mtl_ie_tradeoff
- **Imbalanced Gradients in RL Post-Training** (Findings of EACL 2026) -- closest_prior_work

---

### CATEGORY 2: Papers discussing rejection sampling / RSFT / scored-random selection strategies

**32 papers** matched. The most directly relevant ones:

**Core RSFT methodology papers:**
1. **A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce** (arXiv 2504.11343, 2025) -- role: key_theoretical_support. Key insight: RAFT (simple rejection sampling) matches GRPO/PPO in math reasoning. GRPO's advantage mainly comes from discarding all-wrong prompts, not reward normalization. Proposes Reinforce-Rej filtering all-correct and all-wrong samples.
2. **Beyond Rejection Sampling: Trajectory Fusion (TrajFusion)** (arXiv 2602.04391, 2026) -- role: method_component. Traditional RSFT discards wrong trajectories; TrajFusion interleaves error and correct trajectories.
3. **Rejection Sampling Based Fine Tuning Secretly Performs PPO** (ICML 2025, 2025) -- role: theoretical_support. Establishes theoretical equivalence between RSFT and PPO under marginal KL constraints.
4. **RAFT: Reward rAnked FineTuning** (TMLR 2024, 2024) -- role: background. Canonical RSFT framework: iterative generate-rank-filter-SFT.
5. **RS-DPO: Hybrid Rejection Sampling and DPO** (NAACL 2024 Findings, 2024) -- role: method-component. Systematically combines rejection sampling with DPO using reward-based contrastive pair selection.
6. **RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning** (arXiv 2601.09253, 2026) -- role: direct_competitor. Addresses RSFT's waste of negative samples through reward-weighted loss.
7. **AdaSTaR: Adaptive Data Sampling for Training Self-Taught Reasoners** (NeurIPS 2025, 2025) -- role: related_method. RSFT's random sampling leads to training imbalance; proposes diversity + curriculum sampling, reducing FLOPs by 58.6%.

**Best-of-N papers:**
8. **Is Best-of-N the Best of Them?** (ICML 2025, 2025) -- role: key_baseline. BoN suffers from reward hacking at large N; proposes InferenceTimePessimism.
9. **Inference-Aware Fine-Tuning for Best-of-N** (ICLR 2025, 2024) -- role: method_component. Trains model to optimize BoN inference performance; learns exploration-exploitation meta-strategy.
10. **Evaluation of Best-of-N Sampling Strategies** (TMLR 2025, 2025) -- role: evaluation. Systematic BoN evaluation; proposes Stochastic Regularized BoN.
11. **Regularized Best-of-N with MBR Objective** (NAACL 2025, 2024) -- role: related_method. MBR-BoN uses Minimum Bayes Risk as proximity regularizer.

The remaining 21 papers mention RSFT tangentially in their broader context (e.g., LLM-based DocRE methods, IE alignment, knowledge distillation for DocRE, self-training).

---

### CATEGORY 3: Papers about GRPO or RL for IE/NLP structured tasks

**50 papers** matched. Organized by sub-theme:

**GRPO for IE specifically (most relevant):**
1. **R1-RE** (arXiv 2507.04642, 2025) -- direct_competitor. First RLVR (GRPO + verifiable reward) for relation extraction. F1-based reward design.
2. **ReasoningNER** (arXiv 2511.11978, 2025) -- direct-competitor. GRPO for NER with composite reward (entity F1 + format compliance).
3. **R2GRPO** (arXiv 2505.22068, 2025) -- related_method. MimicSFT + relevance/rule-mining reward GRPO for scientific IE.
4. **MORE-R1** (arXiv 2603.09478, 2026) -- related_method. GRPO for multimodal RE with progressive sample-mixing.
5. **REAR** (EMNLP 2025 Findings) -- related_method. RL reasoning optimization for event argument extraction.
6. **Aligning Instruction-Tuned LLMs for Event Extraction with Multi-objective RL** (Springer 2025) -- related_method.
7. **EvidenceRL** (arXiv 2603.19532, 2026) -- closest_competitor. GRPO optimizing both grounding (evidence entailment) and correctness. F1@3 from 37.0->54.5, grounding from 47.6->78.2. Hallucination reduced 5x.

**GRPO stability / mode collapse / reward design:**
8. **GDPO** (ICML 2026) -- closest_prior_work. Multi-reward GRPO normalization collapse; per-reward independent normalization.
9. **DRA-GRPO** (arXiv 2505.09655, 2025) -- Diversity-aware reward adjustment using submodular mutual information.
10. **DAPO** (NeurIPS 2025) -- key_baseline. Entropy collapse diagnosis; Clip-Higher + Dynamic Sampling.
11. **Dr. GRPO** (COLM 2025) -- Difficulty bias from std normalization; proposes unbiased Monte Carlo advantage.
12. **DiverseGRPO** (arXiv 2512.21514, 2025) -- Mode collapse in image generation GRPO.
13. **Why GRPO Needs Normalization** (arXiv 2601.23135, 2025) -- reward_std drives convergence rate.
14. **GVPO** (NeurIPS 2025) -- Variance-based exploration-exploitation balance.
15. **E-GRPO** (ICLR 2026) -- closest_prior_work. Entity-aware reward giving partial credit to near-miss negative samples.
16. **GRPO-LEAD** (EMNLP 2025) -- Length-regularized rewards + difficulty-aware advantage reweighting.

**Multi-objective GRPO:**
17. **MO-GRPO** (arXiv 2509.22047, 2025) -- Reward hacking in multi-objective GRPO; variance-based normalization.
18. **RDPO** (arXiv 2605.13641, 2026) -- Decorrelated reward subspace optimization.

**GRPO theory:**
19. **GRPO is Secretly a Process Reward Model** (under review ICML 2026) -- GRPO + ORM equivalence to PRM-aware RL; lambda-GRPO.
20. **Reward Hacking in the Era of Large Models** (arXiv 2604.13602, 2026) -- Proxy Compression Hypothesis.

**Contrastive reward for RL:**
21. **Improving RLHF Using Contrastive Rewards** (arXiv 2403.07708, 2024) -- closest_contrastive_precedent. Offline baseline response for contrastive penalty in PPO.

**RL training stability / quantization:**
22-31. Multiple papers on quantization-aware RL (QuRL, QaRL, FP8-RL, Jet-RL, BitRL), training precision (FP16 vs BF16), stabilization formulations.

**Multi-task RL / gradient imbalance:**
32. **Imbalanced Gradients in RL Post-Training of Multi-Task LLMs** (Findings of EACL 2026) -- closest_prior_work. Gradient magnitude vs performance improvement uncorrelated.

Plus ~18 more papers in supporting roles (LoRA theory, PEFT, self-training, ADELIE, etc.)

---

### CATEGORY 4: Papers about learning curves / training dynamics of RL for NLP

**17 papers** matched. The most directly relevant:

1. **DAPO** (NeurIPS 2025) -- Entropy collapse dynamics; frac_zero prompt filtering. "accuracy=0 or 1 prompts produce zero gradients, reducing effective batch size."
2. **Dr. GRPO** (COLM 2025) -- std(r)->0 causes advantage explosion; frac_zero_std->0.8 under extraction-only reward.
3. **Why GRPO Needs Normalization** (arXiv 2601.23135, 2025) -- reward_std governs convergence rate; higher reward_std = faster convergence.
4. **Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards** (arXiv 2511.03710, 2025) -- Per-prompt mean baseline inaccurate at low generation count; James-Stein shrinkage reduces gradient variance.
5. **GVPO** (NeurIPS 2025) -- Variance term naturally balances exploration/exploitation, maintaining moderate entropy.
6. **DiverseGRPO** (arXiv 2512.21514, 2025) -- GRPO output homogenization in later training stages.
7. **Reward Shaping to Mitigate Reward Hacking** (arXiv 2502.18770, 2025) -- Reward should be bounded, fast-growing then slow-converging.
8. **R1-RE** (arXiv 2507.04642, 2025) -- No catastrophic forgetting after GRPO training on sentence-level RE; performance on MATH-500/IFEval/GPQA maintained or improved.
9. **Reinforcement Fine-Tuning Naturally Mitigates Forgetting** (arXiv 2507.05386, 2025) -- RFT gradients scaled by reward variance act as data-dependent regularizer.
10. **The Energy Loss Phenomenon in RLHF** (ICML 2025) -- L1 norm divergence in last layer increases during RL training; excessive increase signals reward hacking.
11. **Defeating the Training-Inference Mismatch via FP16** (arXiv 2510.26788, 2025) -- BF16 causes collapse at 150-600 steps in RL fine-tuning.
12. **QuRL** (ICLR 2026) -- Quantized actor divergence grows exponentially causing training collapse in long-horizon RL.
13. **RL Is Neither a Panacea Nor a Mirage** (arXiv 2508.16546, 2025) -- RL-FT recovers most OOD performance loss from SFT; recovery correlates with singular vector direction rotation.
14. **The Impact of LoRA on Cluster Emergence** (arXiv 2402.15415, 2024) -- Phase transition from non-forgetting to forgetting as perturbation norm increases.
15. **Posterior-GRPO** (arXiv 2508.05170, 2025) -- Conditional reward suppresses reward hacking dynamics.
16. **MO-GRPO** (arXiv 2509.22047, 2025) -- Multi-objective reward hacking dynamics.
17. **Regularized BoN with MBR** (NAACL 2025, 2024) -- Reward hacking dynamics in BoN scaling.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dee7dec-37be-4dee-af31-f6d70b996291",
  "isSidechain": true,
  "agentId": "a4b1818a3cd108cba",
  "requestId": "req_011CbAeXr5RaoxsBJhYuWebo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "607d3c90-5b99-4931-944c-e83e5881e712",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Wo8nDJp2y9nsi1pkdpcDX",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3508,
      "cache_read_input_tokens": 46405,
      "output_tokens": 4019,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3508
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4019,
          "cache_read_input_tokens": 46405,
          "cache_creation_input_tokens": 3508,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3508,
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
