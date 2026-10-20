# Research conversation: I need to verify the exact publication details of several papers for a bibliography. Use WebSearch to find the correct a

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a25497bf4e929bce1.jsonl`
- **Structured JSON:** [`39302b89bc7cd625f619.json`](../../sessions/39/39302b89bc7cd625f619.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

36 recorded events

### User

_source line 1 · 2026-05-15T03:14:04.503Z_

I need to verify the exact publication details of several papers for a bibliography. Use WebSearch to find the correct arXiv IDs, conference venues, and author lists for each. Report the full citation info (authors, title, venue, year, arXiv ID if available).

1. CodeBERT (Feng et al., 2020) — code-NL pre-training with contrastive learning
2. UniXcoder (Guo et al., 2022) — unified cross-modal code representation
3. CodeSage (Zhang et al., 2024) — code representation learning (likely from Salesforce)
4. SCodeR or CodeContrastNet — recent contrastive learning for code search (2023-2024)
5. StarCoder2 (Lozhkov et al., 2024) — the model we use as encoder

For each, I need: full author list (at least first 3 + et al.), exact title, venue (conference/journal or arXiv), year, and arXiv ID.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a25497bf4e929bce1",
  "type": "user",
  "uuid": "e03fd9b4-739d-42a5-b03e-5792298bad65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T03:14:04.507Z_

```json
{
  "parentUuid": "e03fd9b4-739d-42a5-b03e-5792298bad65",
  "isSidechain": true,
  "agentId": "a25497bf4e929bce1",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
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
  "uuid": "00ab6fa8-706b-414d-acce-ba3aadf39def",
  "timestamp": "2026-05-15T03:14:04.507Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T03:14:07.236Z_



I'll search for each paper's publication details. Let me fetch the WebSearch tool first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00ab6fa8-706b-414d-acce-ba3aadf39def",
  "isSidechain": true,
  "agentId": "a25497bf4e929bce1",
  "requestId": "req_011Cb3dFDknhEP6SEGyDjzaq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad1ffa05-6983-4730-97bc-167f5d717a56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0126ijHo3xHJpB1q13YaAwag",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13318,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13318,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 4 · 2026-05-15T03:14:07.366Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014vghacENPAFWY8vEovQWMH`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad1ffa05-6983-4730-97bc-167f5d717a56",
  "isSidechain": true,
  "agentId": "a25497bf4e929bce1",
  "requestId": "req_011Cb3dFDknhEP6SEGyDjzaq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4079b30c-171e-4b52-adf2-3d4be59dda04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0126ijHo3xHJpB1q13YaAwag",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13318,
      "cache_read_input_tokens": 0,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13318
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 96,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 13318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13318,
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

_source line 5 · 2026-05-15T03:14:07.369Z_

<details><summary>↩ Tool result · `toolu_014vghacENPAFWY8vEovQWMH`</summary>

````text
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
  "parentUuid": "4079b30c-171e-4b52-adf2-3d4be59dda04",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a25497bf4e929bce1",
  "type": "user",
  "uuid": "55bfd302-c5fd-4886-bbdd-f46fe25d8358",
  "sourceToolAssistantUUID": "4079b30c-171e-4b52-adf2-3d4be59dda04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-15T03:14:09.646Z_



Now let me search for all five papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55bfd302-c5fd-4886-bbdd-f46fe25d8358",
  "isSidechain": true,
  "agentId": "a25497bf4e929bce1",
  "requestId": "req_011Cb3dFSJqhkgQehX3HZf37",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e237f8ee-736e-4919-9bc2-a3388adfde82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvYWFqZ47STvKtJRyt2du6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 13318,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1460,
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

_source line 7 · 2026-05-15T03:14:10.731Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GjshQphRtJ3az3WaM3nqM7`</summary>

```json
{
  "query": "CodeBERT Feng 2020 arXiv paper code pre-training bimodal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e237f8ee-736e-4919-9bc2-a3388adfde82",
  "isSidechain": true,
  "agentId": "a25497bf4e929bce1",
  "requestId": "req_011Cb3dFSJqhkgQehX3HZf37",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1da7a848-2f00-4bb9-8ade-b3c4fde1241d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvYWFqZ47STvKtJRyt2du6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 13318,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1460,
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

_source line 8 · 2026-05-15T03:14:11.145Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017NG6GpqZMcuu1H6D92PBfT`</summary>

```json
{
  "query": "UniXcoder Guo 2022 arXiv unified cross-modal code representation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1da7a848-2f00-4bb9-8ade-b3c4fde1241d",
  "isSidechain": true,
  "agentId": "a25497bf4e929bce1",
  "requestId": "req_011Cb3dFSJqhkgQehX3HZf37",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90757847-5326-4f12-ae7a-8c50642373c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvYWFqZ47STvKtJRyt2du6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 13318,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1460,
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

_source line 9 · 2026-05-15T03:14:11.149Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WJY5TwdTDVtyCe5qMFL75r`</summary>

```json
{
  "query": "CodeSage Zhang 2024 Salesforce code representation learning arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90757847-5326-4f12-ae7a-8c50642373c4",
  "isSidechain": true,
  "agentId": "a25497bf4e929bce1",
  "requestId": "req_011Cb3dFSJqhkgQehX3HZf37",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c47e82f-42b6-4982-943a-a3b4688f8f3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvYWFqZ47STvKtJRyt2du6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 13318,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1460,
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

_source line 10 · 2026-05-15T03:14:11.612Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vz5iCSqGibMRvnsjC9PZB3`</summary>

```json
{
  "query": "SCodeR contrastive learning code search 2023 2024 arXiv paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c47e82f-42b6-4982-943a-a3b4688f8f3d",
  "isSidechain": true,
  "agentId": "a25497bf4e929bce1",
  "requestId": "req_011Cb3dFSJqhkgQehX3HZf37",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5fc04dc-c0ed-4da9-93e5-e166286d99bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvYWFqZ47STvKtJRyt2du6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 13318,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1460,
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

_source line 11 · 2026-05-15T03:14:12.055Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012hVQa6RHfrvsjdeVM4pXnf`</summary>

```json
{
  "query": "StarCoder2 Lozhkov 2024 arXiv paper BigCode"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5fc04dc-c0ed-4da9-93e5-e166286d99bd",
  "isSidechain": true,
  "agentId": "a25497bf4e929bce1",
  "requestId": "req_011Cb3dFSJqhkgQehX3HZf37",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4381b6b1-8fff-440a-913a-0803a1cdf52e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvYWFqZ47STvKtJRyt2du6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 13318,
      "output_tokens": 297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1460
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 297,
          "cache_read_input_tokens": 13318,
          "cache_creation_input_tokens": 1460,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1460,
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

_source line 12 · 2026-05-15T03:14:16.691Z_

<details><summary>↩ Tool result · `toolu_017NG6GpqZMcuu1H6D92PBfT`</summary>

```text
Web search results for query: "UniXcoder Guo 2022 arXiv unified cross-modal code representation"

Links: [{"title":"[2203.03850] UniXcoder: Unified Cross-Modal Pre-training for Code Representation","url":"https://arxiv.org/abs/2203.03850"},{"title":"[2203.03850v1] UniXcoder: Unified Cross-Modal Pre-training for Code Representation","url":"https://arxiv.org/abs/2203.03850v1"},{"title":"Paper page - UniXcoder: Unified Cross-Modal Pre-training for Code Representation","url":"https://huggingface.co/papers/2203.03850"},{"title":"UniXcoder: Unified Cross-Modal Pre-training for Code Representation - ACL Anthology","url":"https://aclanthology.org/2022.acl-long.499/"},{"title":"CodeBERT/UniXcoder/README.md at master · microsoft/CodeBERT","url":"https://github.com/microsoft/CodeBERT/blob/master/UniXcoder/README.md"},{"title":"UniXcoder: Unified Cross-Modal Pre-training for Code Representation","url":"https://www.catalyzex.com/paper/arxiv:2203.03850"},{"title":"[PDF] UniXcoder: Unified Cross-Modal Pre-training for Code Representation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/UniXcoder:-Unified-Cross-Modal-Pre-training-for-Guo-Lu/4b27f18bff43d605805c92696a979714ced0b805"},{"title":"microsoft/unixcoder-base · Hugging Face","url":"https://huggingface.co/microsoft/unixcoder-base"},{"title":"UniXcoder: Unified Cross-Modal Pre-training for Code Representation","url":"https://www.mendeley.com/catalogue/7bb497ba-a8bd-3eca-9440-1bc6d55c2e30/"},{"title":"UniXcoder: Unified Cross-Modal Pre-training for Code Representation · Machine Learning for Big Code and Naturalness","url":"https://ml4code.github.io/publications/guo2022unixcoder/"}]

I found comprehensive information about the UniXcoder paper. Here's what the search results show:

## Overview

UniXcoder is a unified cross-modal pre-trained model for programming language. The paper was authored by Daya Guo and 5 other authors, and it was published on March 8, 2022 on arXiv as paper 2203.03850.

## Key Technical Details

The model utilizes mask attention matrices with prefix adapters to control the behavior of the model and leverages cross-modal contents like AST and code comment to enhance code representation.

To encode AST that is represented as a tree in parallel, the authors propose a one-to-one mapping method to transform AST in a sequence structure that retains all structural information from the tree. Additionally, they propose to utilize multi-modal contents to learn representation of code fragment with contrastive learning, and then align representations among programming languages using a cross-modal generation task.

## Evaluation

The researchers evaluated UniXcoder on five code-related tasks over nine datasets and constructed a dataset for a new task called zero-shot code-to-code search. Results show that the model achieves state-of-the-art performance on most tasks and analysis reveals that comment and AST can both enhance UniXcoder.

The paper was also published at ACL 2022 (the 60th Annual Meeting of the Association for Computational Linguistics).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90757847-5326-4f12-ae7a-8c50642373c4",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a25497bf4e929bce1",
  "type": "user",
  "uuid": "e90bb906-8071-4eec-9c03-86494cdfd345",
  "sourceToolAssistantUUID": "90757847-5326-4f12-ae7a-8c50642373c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T03:14:17.741Z_

<details><summary>↩ Tool result · `toolu_012hVQa6RHfrvsjdeVM4pXnf`</summary>

```text
Web search results for query: "StarCoder2 Lozhkov 2024 arXiv paper BigCode"

Links: [{"title":"[2402.19173] StarCoder 2 and The Stack v2: The Next Generation","url":"https://arxiv.org/abs/2402.19173"},{"title":"Paper page - StarCoder 2 and The Stack v2: The Next Generation","url":"https://huggingface.co/papers/2402.19173"},{"title":"[2402.19173v1] StarCoder 2 and The Stack v2: The Next Generation","url":"https://arxiv.org/abs/2402.19173v1"},{"title":"StarCoder 2 and The Stack v2: The Next Generation | ServiceNow AI Research","url":"https://www.servicenow.com/research/publication/anton-lozhkov-star-arxiv2024.html"},{"title":"[PDF] StarCoder 2 and The Stack v2: The Next Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/StarCoder-2-and-The-Stack-v2:-The-Next-Generation-Lozhkov-Li/18e7ab056c16928d8f9539509a4b366889106d97"},{"title":"bigcode/starcoder2-15b · Hugging Face","url":"https://huggingface.co/bigcode/starcoder2-15b"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Starcoder+2+and+the+stack+v2:+The+next+generation&amp=&author=Anton+Lozhkov&amp=&author=Raymond+Li&amp=&author=Loubna+Ben+Allal&amp=&author=Federico+Cassano&amp=&author=Joel+Lamy-Poirier&amp=&author=Nouamane+Tazi&amp=&author=Ao+Tang&amp=&author=Dmytro+Pykhtar&amp=&author=Jiawei+Liu&amp=&author=Yuxiang+Wei&amp=&publication_year=2024"},{"title":"StarCoder 2 and The Stack v2: The Next Generation","url":"https://ccs.neu.edu/~arjunguha/main/papers/lozhkov-starcoder-stack-2.html"},{"title":"StarCoder2 and The Stack v2: The Next Generation","url":"https://arxiv.org/pdf/2402.19173"},{"title":"StarCoder 2 and The Stack v2: The Next Generation | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2402.19173"}]

I found the paper you're looking for! The BigCode project, an open-scientific collaboration focused on the responsible development of Large Language Models for Code (Code LLMs), introduces StarCoder2, with a paper authored by Anton Lozhkov and 65 other authors.

**Paper Details:**
- **Title:** StarCoder 2 and The Stack v2: The Next Generation
- **arXiv ID:** 2402.19173
- **Publication Date:** February 29, 2024
- **URL:** https://arxiv.org/abs/2402.19173

**Key Contributions:**

The paper builds The Stack v2 in partnership with Software Heritage (SWH) on top of their source code archive, alongside the SWH repositories spanning 619 programming languages, carefully selecting other high-quality data sources such as GitHub pull requests, Kaggle notebooks, and code documentation.

StarCoder2 models are trained with 3B, 7B, and 15B parameters on 3.3 to 4.3 trillion tokens and thoroughly evaluated on a comprehensive set of Code LLM benchmarks.

**Performance:**

The large model, StarCoder2-15B, significantly outperforms other models of comparable size and matches or outperforms CodeLlama-34B, a model more than twice its size.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4381b6b1-8fff-440a-913a-0803a1cdf52e",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a25497bf4e929bce1",
  "type": "user",
  "uuid": "9fd007e2-f0ff-4dd0-bcc3-da3e371b0e24",
  "sourceToolAssistantUUID": "4381b6b1-8fff-440a-913a-0803a1cdf52e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T03:14:17.899Z_

<details><summary>↩ Tool result · `toolu_01GjshQphRtJ3az3WaM3nqM7`</summary>

```text
Web search results for query: "CodeBERT Feng 2020 arXiv paper code pre-training bimodal"

Links: [{"title":"[2002.08155] CodeBERT: A Pre-Trained Model for Programming and Natural Languages","url":"https://arxiv.org/abs/2002.08155"},{"title":"CodeBERT: A Pre-Trained Model for Programming and Natural Languages - ACL Anthology","url":"https://aclanthology.org/2020.findings-emnlp.139/"},{"title":"[PDF] CodeBERT: A Pre-Trained Model for Programming and Natural Languages | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CodeBERT:-A-Pre-Trained-Model-for-Programming-and-Feng-Guo/0fe2636446cd686830da3d971b31a004d6094b3c"},{"title":"(Open Access) CodeBERT: A Pre-Trained Model for Programming and Natural Languages (2020) | Zhangyin Feng | 1802 Citations","url":"https://scispace.com/papers/codebert-a-pre-trained-model-for-programming-and-natural-3n356pkmc3"},{"title":"CodePrompt: Improving Source Code-Related Classification with Knowledge Features through Prompt Learning","url":"https://arxiv.org/html/2401.05544v1"},{"title":"CodeBERT: A Pre-Trained Model for Programming and Natural Languages - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200208155F/abstract"},{"title":"CodeBERT: Bimodal Pre-trained Model for Code","url":"https://www.emergentmind.com/topics/codebert"},{"title":"graphcodebert: pre-training code represen","url":"https://arxiv.org/pdf/2009.08366"},{"title":"CodeBERT: A Pre-Trained Model for Programming and Natural Languages","url":"https://arxiv.org/pdf/2002.08155"},{"title":"[2009.08366] GraphCodeBERT: Pre-training Code Representations with Data Flow","url":"https://ar5iv.labs.arxiv.org/html/2009.08366"}]

I found the paper you're looking for. Here's what I discovered:

CodeBERT was submitted to arXiv on February 19, 2020, with multiple revisions up to September 18, 2020.

**Key Details:**

CodeBERT is a bimodal pre-trained model for programming language (PL) and natural language (NL) that learns general-purpose representations supporting downstream NL-PL applications such as natural language code search and code documentation generation.

**Architecture and Training:**

CodeBERT uses a Transformer-based neural architecture and is trained with a hybrid objective function incorporating the pre-training task of replaced token detection, which detects plausible alternatives sampled from generators.

The training enables utilization of both bimodal data of NL-PL pairs and unimodal data, where the former provides input tokens for model training while the latter helps learn better generators.

**Performance:**

CodeBERT achieves state-of-the-art performance on both natural language code search and code documentation generation tasks.

**Paper Details:**

The paper was authored by Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Linjun Shou, Bing Qin, Ting Liu, Daxin Jiang, and Ming Zhou. The arXiv identifier is **2002.08155**.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1da7a848-2f00-4bb9-8ade-b3c4fde1241d",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a25497bf4e929bce1",
  "type": "user",
  "uuid": "9339aba1-fbda-49a8-b696-e02796622223",
  "sourceToolAssistantUUID": "1da7a848-2f00-4bb9-8ade-b3c4fde1241d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T03:14:18.811Z_

<details><summary>↩ Tool result · `toolu_01Vz5iCSqGibMRvnsjC9PZB3`</summary>

```text
Web search results for query: "SCodeR contrastive learning code search 2023 2024 arXiv paper"

Links: [{"title":"CoCoSoDa: Effective Contrastive Learning for Code Search","url":"https://arxiv.org/pdf/2204.03293"},{"title":"SCodeSearcher: soft contrastive learning for code search | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-024-10603-z"},{"title":"[2204.03293] CoCoSoDa: Effective Contrastive Learning for Code Search","url":"https://arxiv.org/abs/2204.03293"},{"title":"[2204.03293v3] CoCoSoDa: Effective Contrastive Learning for Code Search","url":"https://arxiv.org/abs/2204.03293v3"},{"title":"Contrastive Prompt Learning-based Code Search based on Interaction Matrix","url":"https://arxiv.org/html/2310.06342"},{"title":"CodeRetriever: Large-scale Contrastive Pre-training for Code Search","url":"https://arxiv.org/pdf/2201.10866"},{"title":"[2007.04973] Contrastive Code Representation Learning","url":"https://arxiv.org/abs/2007.04973"},{"title":"Contrastive Code Representation Learning","url":"https://parasj.github.io/contracode/"},{"title":"[2204.03293v2] Enhancing Semantic Code Search with Multimodal Contrastive Learning and Soft Data Augmentation","url":"https://arxiv.org/abs/2204.03293v2"},{"title":"Enhancing Semantic Code Search with Multimodal Contrastive","url":"https://arxiv.org/pdf/2204.03293v2"}]

Based on my search results, I couldn't find a paper specifically titled "SCodeR" from 2023-2024 on arXiv. However, I found several highly relevant papers on contrastive learning for code search from that timeframe:

## Most Relevant Finding:

Several pre-training methods based on contrastive learning such as Corder, Code-MVP, CodeRetriver, SynCoBERT, and CoCoSoDa have been proposed to obtain better code representations. One of the most prominent recent papers is **CoCoSoDa**, which was published in February 2023.

### CoCoSoDa Paper Details:

CoCoSoDa effectively utilizes contrastive learning for code search via two key factors in contrastive learning: data augmentation and negative samples. More specifically:

- Soft data augmentation dynamically masks or replaces some tokens with their types for input sequences to generate positive samples, and momentum mechanism is used to generate large and consistent representations of negative samples in a mini-batch through maintaining a queue

- CoCoSoDa outperforms 14 baselines and especially exceeds CodeBERT, GraphCodeBERT, and UniXcoder by 13.3%, 10.5%, and 5.9% on average MRR scores, respectively

**arXiv ID:** 2204.03293

If you're specifically looking for a paper titled "SCodeR," it's possible it may be known by a different name on arXiv or may not yet be published. Would you like me to search with different keywords?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5fc04dc-c0ed-4da9-93e5-e166286d99bd",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a25497bf4e929bce1",
  "type": "user",
  "uuid": "43cfe628-a821-43b1-88ec-3479033c7a43",
  "sourceToolAssistantUUID": "e5fc04dc-c0ed-4da9-93e5-e166286d99bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T03:14:20.203Z_

<details><summary>↩ Tool result · `toolu_01WJY5TwdTDVtyCe5qMFL75r`</summary>

```text
Web search results for query: "CodeSage Zhang 2024 Salesforce code representation learning arXiv"

Links: [{"title":"GitHub - amazon-science/CodeSage: CodeSage: Code Representation Learning At Scale (ICLR 2024) · GitHub","url":"https://github.com/amazon-science/CodeSage"},{"title":"CodeSage/README.md at main · amazon-science/CodeSage","url":"https://github.com/amazon-science/CodeSage/blob/main/README.md"},{"title":"Code Representation Learning at Scale","url":"https://arxiv.org/html/2402.01935v1"},{"title":"Code Representation Learning At Scale - Academic Homepage","url":"https://wasiahmad.github.io/publications/41_codesage/"},{"title":"CODE REPRESENTATION LEARNING AT SCALE | OpenReview","url":"https://openreview.net/forum?id=vfzRRjumpX&noteId=h1UOsh4eVQ"},{"title":"[2402.01935] Code Representation Learning At Scale","url":"https://arxiv.org/abs/2402.01935"},{"title":"Publications | Salesforce AI Research","url":"https://www.salesforceairesearch.com/publications"},{"title":"Deep learning for code generation: a survey","url":"http://scis.scichina.com/en/2024/191101.pdf"},{"title":"CodeSAM: Source Code Representation Learning by Infusing Self-Attention with Multi-Code-View Graphs","url":"https://arxiv.org/html/2411.14611v1"},{"title":"A Survey on Large Language Models for Code Generation","url":"https://arxiv.org/html/2406.00515v2"}]

Based on the search results, I found information about CodeSage. However, I should clarify that CodeSage was developed by researchers including Dejiao Zhang, Wasi Uddin Ahmad, Ming Tan, Hantian Ding, Ramesh Nallapati, Dan Roth, Xiaofei Ma, and Bing Xiang, and it was published by Amazon Science, not Salesforce.

CodeSage is an ICLR 2024 paper on "Code Representation Learning At Scale". CodeSage is a bidirectional encoder representation model for source code that is pretrained using a two-stage training scheme with a large amount of customized pretraining data.

In the first training stage, the bidirectional encoders are trained via identifier deobfuscation and MLM (Masked Language Modeling), and in the second stage, the researchers leverage (text, code) pairs for bimodal contrastive learning. Three bidirectional encoder representation models were trained: CodeSage-small (130M), CodeSage-base (356M), and CodeSage-large (1.3B).

The corresponding arXiv paper can be found at arXiv paper 2402.01935, submitted on February 2, 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c47e82f-42b6-4982-943a-a3b4688f8f3d",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a25497bf4e929bce1",
  "type": "user",
  "uuid": "cb6822b9-3714-4d1e-9f88-c1f5548d9321",
  "sourceToolAssistantUUID": "9c47e82f-42b6-4982-943a-a3b4688f8f3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-15T03:14:23.505Z_

Now let me get the full author lists for CodeSage and StarCoder2, and search more specifically for "SCodeR" or "CodeRetriever" and "CodeContrastNet".

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb6822b9-3714-4d1e-9f88-c1f5548d9321",
  "isSidechain": true,
  "agentId": "a25497bf4e929bce1",
  "requestId": "req_011Cb3dGNyhdgsHwuE2reu3W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a600807-8bbe-4f1e-bcc1-54383dec7bbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012m55Ea5vbt3jFJ8q8itjvf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1867,
      "cache_creation_input_tokens": 2888,
      "cache_read_input_tokens": 14778,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2888,
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

_source line 18 · 2026-05-15T03:14:24.680Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mdnzjb6azg6aPbtsEpTxKc`</summary>

```json
{
  "query": "arxiv 2402.01935 CodeSage full author list Zhang Ahmad"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a600807-8bbe-4f1e-bcc1-54383dec7bbd",
  "isSidechain": true,
  "agentId": "a25497bf4e929bce1",
  "requestId": "req_011Cb3dGNyhdgsHwuE2reu3W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "318455fe-76ef-4d8a-b01a-5e92285fc487",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012m55Ea5vbt3jFJ8q8itjvf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1867,
      "cache_creation_input_tokens": 2888,
      "cache_read_input_tokens": 14778,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2888,
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

_source line 19 · 2026-05-15T03:14:25.162Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018KLs7a19irsArJzKgnuSWd`</summary>

```json
{
  "query": "StarCoder2 2402.19173 full author list first authors Lozhkov Li Ben Allal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "318455fe-76ef-4d8a-b01a-5e92285fc487",
  "isSidechain": true,
  "agentId": "a25497bf4e929bce1",
  "requestId": "req_011Cb3dGNyhdgsHwuE2reu3W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "474526fb-a835-4b8a-a08b-6cae6852e4c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012m55Ea5vbt3jFJ8q8itjvf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1867,
      "cache_creation_input_tokens": 2888,
      "cache_read_input_tokens": 14778,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2888,
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

_source line 20 · 2026-05-15T03:14:25.642Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VCm3wyAtmuWuXoGCqnYgsZ`</summary>

```json
{
  "query": "\"CodeContrastNet\" code contrastive learning paper arXiv 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "474526fb-a835-4b8a-a08b-6cae6852e4c4",
  "isSidechain": true,
  "agentId": "a25497bf4e929bce1",
  "requestId": "req_011Cb3dGNyhdgsHwuE2reu3W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63cc9fc9-bb65-423e-b2ad-ad3a3b834c0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012m55Ea5vbt3jFJ8q8itjvf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1867,
      "cache_creation_input_tokens": 2888,
      "cache_read_input_tokens": 14778,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2888,
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

_source line 21 · 2026-05-15T03:14:26.149Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011GCgq5WAbaKv5vFN9HUDLK`</summary>

```json
{
  "query": "\"SCodeR\" code retrieval contrastive pre-training arXiv paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63cc9fc9-bb65-423e-b2ad-ad3a3b834c0f",
  "isSidechain": true,
  "agentId": "a25497bf4e929bce1",
  "requestId": "req_011Cb3dGNyhdgsHwuE2reu3W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f9218c1-99e8-4462-83ac-bfc1ec986abe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012m55Ea5vbt3jFJ8q8itjvf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1867,
      "cache_creation_input_tokens": 2888,
      "cache_read_input_tokens": 14778,
      "output_tokens": 277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2888
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1867,
          "output_tokens": 277,
          "cache_read_input_tokens": 14778,
          "cache_creation_input_tokens": 2888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2888,
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

_source line 22 · 2026-05-15T03:14:28.451Z_

<details><summary>↩ Tool result · `toolu_01Mdnzjb6azg6aPbtsEpTxKc`</summary>

```text
Web search results for query: "arxiv 2402.01935 CodeSage full author list Zhang Ahmad"

Links: [{"title":"[2402.01935] Code Representation Learning At Scale","url":"https://arxiv.org/abs/2402.01935"},{"title":"Code Representation Learning at Scale","url":"https://arxiv.org/html/2402.01935"},{"title":"CodeSage/README.md at main · amazon-science/CodeSage","url":"https://github.com/amazon-science/CodeSage/blob/main/README.md"},{"title":"codesage/codesage-large-v2 · Hugging Face","url":"https://huggingface.co/codesage/codesage-large-v2"},{"title":"arXiv:2402.01935v1 [cs.CL] 2 Feb 2024","url":"https://arxiv.org/pdf/2402.01935"},{"title":"GitHub - amazon-science/CodeSage: CodeSage: Code Representation Learning At Scale (ICLR 2024) · GitHub","url":"https://github.com/amazon-science/CodeSage"},{"title":"Computer Vision and Pattern Recognition Feb 2024","url":"https://www.arxiv.org/list/cs.CV/2024-02?skip=75&show=1000"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=885&show=1000"},{"title":"Computer Science May 2024","url":"https://www.arxiv.org/list/cs/2024-05?skip=8350&show=2000"},{"title":"Computer Science Jul 2024","url":"https://arxiv.org/list/cs/2024-07?skip=3475&show=2000"}]

Based on the search results, I found the full author list for arxiv paper 2402.01935 (CodeSage):

The authors are: Dejiao Zhang, Wasi Uddin Ahmad, Ming Tan, Hantian Ding, Ramesh Nallapati, Dan Roth, Xiaofei Ma, and Bing Xiang (with Dejiao Zhang and Wasi Uddin Ahmad indicating equal contribution).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "318455fe-76ef-4d8a-b01a-5e92285fc487",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a25497bf4e929bce1",
  "type": "user",
  "uuid": "b467698d-d011-4039-a901-3b89b9b67abf",
  "sourceToolAssistantUUID": "318455fe-76ef-4d8a-b01a-5e92285fc487",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T03:14:30.885Z_

<details><summary>↩ Tool result · `toolu_01VCm3wyAtmuWuXoGCqnYgsZ`</summary>

```text
Web search results for query: ""CodeContrastNet" code contrastive learning paper arXiv 2023 2024"

Links: [{"title":"[2007.04973] Contrastive Code Representation Learning","url":"https://arxiv.org/abs/2007.04973"},{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning","url":"https://arxiv.org/pdf/2301.09072"},{"title":"Contrastive Code Representation Learning","url":"https://parasj.github.io/contracode/"},{"title":"[2305.09269] ContrastNet: A Contrastive Learning Framework for Few-Shot Text Classification","url":"https://arxiv.org/abs/2305.09269"},{"title":"GitHub - parasj/contracode: Contrastive Code Representation Learning: functionality-based JavaScript embeddings through self-supervised learning","url":"https://github.com/parasj/contracode"},{"title":"[2007.04973] Contrastive Code Representation Learning","url":"https://ar5iv.labs.arxiv.org/html/2007.04973"},{"title":"[2301.09072] ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning","url":"https://arxiv.org/abs/2301.09072"},{"title":"ContrastNet: Unsupervised Feature Learning by Autoencoder and Prototypical Contrastive Learning for Hyperspectral Imagery Classification","url":"https://arxiv.org/html/2203.07000"},{"title":"[2007.04973v3] Contrastive Code Representation Learning","url":"https://arxiv.org/abs/2007.04973v3"},{"title":"CoCoSoDa: Effective Contrastive Learning for Code Search","url":"https://arxiv.org/pdf/2204.03293"}]

I searched for "CodeContrastNet" but the results don't show a paper with that exact name. Instead, the search returned related work on code contrastive learning published on arXiv in 2023-2024, such as:

1. **ContraCode** (2020): ContraCode is a contrastive pre-training approach that learns code functionality by pre-training a neural network to identify functionally similar variants of a program among many non-equivalent distractors.

2. **ContraBERT** (2023): ContraBERT aims to improve the robustness of pre-trained code models via contrastive learning.

3. **CoCoSoDa** (2022): Another contrastive learning approach for code search.

It appears that "CodeContrastNet" may not exist as a published paper on arXiv, or it may be known by a different name. Could you provide additional details about the paper you're looking for, such as:
- The authors' names
- A more specific description of the methodology
- An alternative title or acronym
- The specific problem it addresses

This would help me locate the exact paper you're interested in.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63cc9fc9-bb65-423e-b2ad-ad3a3b834c0f",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a25497bf4e929bce1",
  "type": "user",
  "uuid": "3fced9c3-aa2f-477e-b892-708189407d83",
  "sourceToolAssistantUUID": "63cc9fc9-bb65-423e-b2ad-ad3a3b834c0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T03:14:31.685Z_

<details><summary>↩ Tool result · `toolu_011GCgq5WAbaKv5vFN9HUDLK`</summary>

```text
Web search results for query: ""SCodeR" code retrieval contrastive pre-training arXiv paper"

Links: [{"title":"CodeRetriever: Large-scale Contrastive Pre-training for Code Search","url":"https://arxiv.org/pdf/2201.10866"},{"title":"[2210.09597] Soft-Labeled Contrastive Pre-training for Function-level Code Representation","url":"https://arxiv.org/abs/2210.09597"},{"title":"Self-Supervised Contrastive Learning for Code Retrieval and","url":"https://arxiv.org/pdf/2009.02731"},{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning","url":"https://arxiv.org/pdf/2301.09072"},{"title":"[2201.10005] Text and Code Embeddings by Contrastive Pre-Training","url":"https://ar5iv.labs.arxiv.org/html/2201.10005"},{"title":"Text and Code Embeddings by Contrastive Pre-Training","url":"https://cdn.openai.com/papers/Text_and_Code_Embeddings_by_Contrastive_Pre_Training.pdf"},{"title":"Contrastive Prompt Learning-based Code Search based on Interaction Matrix","url":"https://arxiv.org/html/2310.06342"},{"title":"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search - ACL Anthology","url":"https://aclanthology.org/2022.emnlp-main.187/"},{"title":"SCodeSearcher: soft contrastive learning for code search | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-024-10603-z"},{"title":"[2009.02731] Self-Supervised Contrastive Learning for Code Retrieval and Summarization via Semantic-Preserving Transformations","url":"https://arxiv.org/abs/2009.02731"}]

Based on the search results, I found the paper you're looking for:

**SCodeR** is a soft-labeled contrastive pre-training framework with two positive sample construction methods to learn function-level code representation.

The soft-labeled contrastive pre-training can obtain fine-grained soft-labels through an iterative adversarial manner and use them to learn better code representation.

To capture semantic information from code, SCodeR utilizes code comments and abstract syntax sub-trees of the code to build positive samples. The paper was published on arXiv on October 26, 2022, and shows that SCodeR achieves state-of-the-art performance on four code-related tasks over seven datasets.

The full arXiv citation is: **arXiv:2210.09597** - "Soft-Labeled Contrastive Pre-training for Function-level Code Representation" by Xiaonan Li and 7 other authors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f9218c1-99e8-4462-83ac-bfc1ec986abe",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a25497bf4e929bce1",
  "type": "user",
  "uuid": "d64de3b3-2983-43dc-afc8-25253f3433c5",
  "sourceToolAssistantUUID": "8f9218c1-99e8-4462-83ac-bfc1ec986abe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T03:14:33.707Z_

<details><summary>↩ Tool result · `toolu_018KLs7a19irsArJzKgnuSWd`</summary>

```text
Web search results for query: "StarCoder2 2402.19173 full author list first authors Lozhkov Li Ben Allal"

Links: [{"title":"[2402.19173] StarCoder 2 and The Stack v2: The Next Generation","url":"https://arxiv.org/abs/2402.19173"},{"title":"Paper page - StarCoder 2 and The Stack v2: The Next Generation","url":"https://huggingface.co/papers/2402.19173"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Starcoder+2+and+the+stack+v2:+The+next+generation&amp=&author=Anton+Lozhkov&amp=&author=Raymond+Li&amp=&author=Loubna+Ben+Allal&amp=&author=Federico+Cassano&amp=&author=Joel+Lamy-Poirier&amp=&author=Nouamane+Tazi&amp=&author=Ao+Tang&amp=&author=Dmytro+Pykhtar&amp=&author=Jiawei+Liu&amp=&author=Yuxiang+Wei&amp=&publication_year=2024"},{"title":"[2402.19173v1] StarCoder 2 and The Stack v2: The Next Generation","url":"https://arxiv.org/abs/2402.19173v1"},{"title":"StarCoder 2 and The Stack v2: The Next Generation | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2402.19173"},{"title":"StarCoder2 and The Stack v2: The Next Generation","url":"https://arxiv.org/pdf/2402.19173"},{"title":"[PDF] StarCoder 2 and The Stack v2: The Next Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/StarCoder-2-and-The-Stack-v2:-The-Next-Generation-Lozhkov-Li/18e7ab056c16928d8f9539509a4b366889106d97"},{"title":"StarCoder 2 and The Stack v2: The Next Generation","url":"https://ccs.neu.edu/~arjunguha/main/papers/lozhkov-starcoder-stack-2.html"},{"title":"StarCoder 2 and The Stack v2: The Next Generation (2024) | Anton Lozhkov | 88 Citations","url":"https://scispace.com/papers/starcoder-2-and-the-stack-v2-the-next-generation-5g4bpswa9q"},{"title":"[2402.19173] \\emojidizzyStarCoder 2 and The Stack v2: The Next Generation","url":"https://ar5iv.labs.arxiv.org/html/2402.19173"}]

Based on the search results, here is the full author list for the StarCoder2 paper (arXiv 2402.19173):

Anton Lozhkov, Raymond Li, Loubna Ben Allal, Federico Cassano, Joel Lamy-Poirier, Nouamane Tazi, Ao Tang, Dmytro Pykhtar, Jiawei Liu, Yuxiang Wei, Tianyang Liu, Max Tian, Denis Kocetkov, Arthur Zucker, Younes Belkada, Zijian Wang, Qian Liu, Dmitry Abulkhanov, Indraneil Paul, Zhuang Li, Wen-Ding Li, Megan Risdal, Jia Li, Jian Zhu, Terry Yue Zhuo, Evgenii Zheltonozhskii, Nii Osae Osae Dade, Wenhao Yu, Lucas Krauß, Naman Jain, Yixuan Su, Xuanli He, Manan Dey, Edoardo Abati, Yekun Chai, Niklas Muennighoff, Xiangru Tang, Muhtasham Oblokulov, Christopher Akiki, Marc Marone, Chenghao Mou, Mayank Mishra, Alex Gu, Binyuan Hui, Tri Dao, Armel Zebaze, Olivier Dehaene, Nicolas Patry, Canwen Xu, Julian McAuley, Han Hu, Torsten Scholak, Sebastien Paquet, Jennifer Robinson, Carolyn Jane Anderson, Nicolas Chapados, Mostofa Patwary, Nima Tajbakhsh, Yacine Jernite, Carlos Muñoz Ferrandis, Lingming Zhang, Sean Hughes, Thomas Wolf, Arjun Guha, Leandro von Werra, Harm de Vries


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "474526fb-a835-4b8a-a08b-6cae6852e4c4",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a25497bf4e929bce1",
  "type": "user",
  "uuid": "340b5af6-e073-41a4-8321-cd21a8a4910d",
  "sourceToolAssistantUUID": "474526fb-a835-4b8a-a08b-6cae6852e4c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-15T03:14:36.344Z_

Let me get the full author list for the SCodeR paper, and also search for CodeRetriever which is another strong candidate for "contrastive learning for code search."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "340b5af6-e073-41a4-8321-cd21a8a4910d",
  "isSidechain": true,
  "agentId": "a25497bf4e929bce1",
  "requestId": "req_011Cb3dHNe92e4f4EgSfU9YX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0fa1932-fb33-4308-87fd-8e610c1d1dba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019gdKRHuLtuCuC7tE96ftkQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1515,
      "cache_creation_input_tokens": 4067,
      "cache_read_input_tokens": 17666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4067,
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

_source line 27 · 2026-05-15T03:14:37.010Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017PHQL33LoQq2fMMBiTLJFB`</summary>

```json
{
  "query": "arxiv 2210.09597 SCodeR \"Soft-Labeled Contrastive Pre-training\" full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0fa1932-fb33-4308-87fd-8e610c1d1dba",
  "isSidechain": true,
  "agentId": "a25497bf4e929bce1",
  "requestId": "req_011Cb3dHNe92e4f4EgSfU9YX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aacaa7c7-6feb-4098-a073-6dbd5cfb6ae3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019gdKRHuLtuCuC7tE96ftkQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1515,
      "cache_creation_input_tokens": 4067,
      "cache_read_input_tokens": 17666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4067,
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

_source line 28 · 2026-05-15T03:14:38.102Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VpVXToEBAUBvideKVxSY93`</summary>

```json
{
  "query": "CodeRetriever 2201.10866 \"Large-scale Contrastive Pre-training for Code Search\" authors venue EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aacaa7c7-6feb-4098-a073-6dbd5cfb6ae3",
  "isSidechain": true,
  "agentId": "a25497bf4e929bce1",
  "requestId": "req_011Cb3dHNe92e4f4EgSfU9YX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb88b688-0ced-4bf7-b9d6-913f58b6c39b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019gdKRHuLtuCuC7tE96ftkQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1515,
      "cache_creation_input_tokens": 4067,
      "cache_read_input_tokens": 17666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4067,
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

_source line 29 · 2026-05-15T03:14:38.680Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01462Uzqzi8NgTNAtj8EaVj7`</summary>

```json
{
  "query": "CodeBERT Feng 2020 EMNLP Findings full author list venue confirmation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb88b688-0ced-4bf7-b9d6-913f58b6c39b",
  "isSidechain": true,
  "agentId": "a25497bf4e929bce1",
  "requestId": "req_011Cb3dHNe92e4f4EgSfU9YX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d08118f3-c7f0-46e3-9398-cc2637ae2f65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019gdKRHuLtuCuC7tE96ftkQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1515,
      "cache_creation_input_tokens": 4067,
      "cache_read_input_tokens": 17666,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4067
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1515,
          "output_tokens": 241,
          "cache_read_input_tokens": 17666,
          "cache_creation_input_tokens": 4067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4067,
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

_source line 30 · 2026-05-15T03:14:40.409Z_

<details><summary>↩ Tool result · `toolu_017PHQL33LoQq2fMMBiTLJFB`</summary>

```text
Web search results for query: "arxiv 2210.09597 SCodeR "Soft-Labeled Contrastive Pre-training" full author list"

Links: [{"title":"[2210.09597] Soft-Labeled Contrastive Pre-training for Function-level Code Representation","url":"https://arxiv.org/abs/2210.09597"},{"title":"[2210.09597] Soft-Labeled Contrastive Pre-training for Function-level Code Representation","url":"https://arxiv-export1.library.cornell.edu/abs/2210.09597"},{"title":"Soft-Labeled Contrastive Pre-Training for Function-Level Code Representation - ACL Anthology","url":"https://aclanthology.org/2022.findings-emnlp.9/"},{"title":"Soft-Labeled Contrastive Pre-Training for Function-Level Code Representation - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/soft-labeled-contrastive-pre-training-for-function-level-code-representation/"},{"title":"Supervised Contrastive Learning Prannay Khosla ∗ Google Research","url":"https://proceedings.neurips.cc/paper/2020/file/d89a66c7c80a29b1bdbab0f2a1a94af8-Paper.pdf"},{"title":"Text and Code Embeddings by Contrastive Pre-Training","url":"https://cdn.openai.com/papers/Text_and_Code_Embeddings_by_Contrastive_Pre_Training.pdf"},{"title":"[2210.08901v1] Contrastive Language-Image Pre-Training with Knowledge Graphs","url":"https://arxiv.org/abs/2210.08901v1"},{"title":"[2210.09304] Non-Contrastive Learning Meets Language-Image Pre-Training","url":"https://arxiv.org/abs/2210.09304"},{"title":"Self-supervised Segment Contrastive Learning for Medical Document Representation | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-031-66538-7_31"},{"title":"Multi-Label Guided Soft Contrastive Learning for Efficient Earth Observation Pretraining | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/multi-label-guided-soft-contrastive-learning-efficient"}]

The full author list for arxiv 2210.09597 "Soft-Labeled Contrastive Pre-training for Function-level Code Representation" is: Xiaonan Li, Daya Guo, Yeyun Gong, Yun Lin, Yelong Shen, Xipeng Qiu, Daxin Jiang, Weizhu Chen, and Nan Duan.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aacaa7c7-6feb-4098-a073-6dbd5cfb6ae3",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a25497bf4e929bce1",
  "type": "user",
  "uuid": "78ca755a-8f7c-48bf-88cc-998cba25d521",
  "sourceToolAssistantUUID": "aacaa7c7-6feb-4098-a073-6dbd5cfb6ae3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T03:14:43.491Z_

<details><summary>↩ Tool result · `toolu_01462Uzqzi8NgTNAtj8EaVj7`</summary>

```text
Web search results for query: "CodeBERT Feng 2020 EMNLP Findings full author list venue confirmation"

Links: [{"title":"CodeBERT: A Pre-Trained Model for Programming and Natural Languages - ACL Anthology","url":"https://aclanthology.org/2020.findings-emnlp.139/"},{"title":"[PDF] CodeBERT: A Pre-Trained Model for Programming and Natural Languages | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CodeBERT:-A-Pre-Trained-Model-for-Programming-and-Feng-Guo/0fe2636446cd686830da3d971b31a004d6094b3c"},{"title":"(PDF) CodeBERT: A Pre-Trained Model for Programming and Natural Languages","url":"https://www.researchgate.net/publication/347233117_CodeBERT_A_Pre-Trained_Model_for_Programming_and_Natural_Languages"},{"title":"CodeBERT: A Pre-Trained Model for Programming and Natural Languages. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/29076fe9174f63526293a77a4c20994f"},{"title":"[2002.08155] CodeBERT: A Pre-Trained Model for Programming and Natural Languages","url":"https://arxiv.org/abs/2002.08155"},{"title":"Feng, Z., Guo, D., Tang, D., Duan, N., Feng, X., Gong, M., et al. (2020) Codebert A Pre-Trained Model for Programming and Natural Languages. Findings of the Association for Computational Linguistics EMNLP 2020, November 2020, 1536-1547. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3859473"},{"title":"CodeBERT: A Pre-Trained Model for Programming and ...","url":"https://aclanthology.org/2020.findings-emnlp.139.pdf"},{"title":"dblp: CodeBERT: A Pre-Trained Model for Programming and Natural Languages.","url":"https://dblp.org/rec/conf/emnlp/FengGTDFGS0LJZ20.html"},{"title":"On the transferability of pre-trained language models for low-resource programming languages | Proceedings of the 30th IEEE/ACM International Conference on Program Comprehension","url":"https://dl.acm.org/doi/10.1145/3524610.3527917"},{"title":"EMNLP2020: CodeBERT: A Pre-Trained Model for Programming and Natural Languages","url":"https://virtual.2020.emnlp.org/paper_findings.139.html"}]

Based on the search results, here is the information you requested:

**Full Author List:**
Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Linjun Shou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou

**Venue Confirmation:**
Findings of the Association for Computational Linguistics: EMNLP 2020

The paper was published in 2020 and appears on pages 1536-1547 of the proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d08118f3-c7f0-46e3-9398-cc2637ae2f65",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a25497bf4e929bce1",
  "type": "user",
  "uuid": "31c33709-1f41-43dc-9688-b0f0ca3190f5",
  "sourceToolAssistantUUID": "d08118f3-c7f0-46e3-9398-cc2637ae2f65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T03:14:44.037Z_

<details><summary>↩ Tool result · `toolu_01VpVXToEBAUBvideKVxSY93`</summary>

```text
Web search results for query: "CodeRetriever 2201.10866 "Large-scale Contrastive Pre-training for Code Search" authors venue EMNLP"

Links: [{"title":"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search - ACL Anthology","url":"https://aclanthology.org/2022.emnlp-main.187/"},{"title":"CodeRetriever: Large-scale Contrastive Pre-training for Code Search","url":"https://arxiv.org/pdf/2201.10866"},{"title":"[2201.10866] CodeRetriever: Unimodal and Bimodal Contrastive Learning for Code Search","url":"https://arxiv.org/abs/2201.10866"},{"title":"CodeRetriever: Unimodal and Bimodal Contrastive Learning for Code Search - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv220110866L/abstract"},{"title":"Large-scale Contrastive Pre-training for Code Search","url":"https://aclanthology.org/2022.emnlp-main.187.pdf"},{"title":"CodeRetriever: Unimodal and Bimodal Cont...","url":"https://axi.lims.ac.uk/paper/2201.10866"},{"title":"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search. - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/coderetriever-a-large-scale-contrastive-pre-training-method-for-code-search/"},{"title":"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search | Request PDF","url":"https://www.researchgate.net/publication/372922877_CodeRetriever_A_Large_Scale_Contrastive_Pre-Training_Method_for_Code_Search"},{"title":"CodeRetriever: Unimodal and Bimodal Contrastive Learning for Code Search | OpenReview","url":"https://openreview.net/forum?id=Jqxi0yHcghg"},{"title":"CodeRetriever: Unimodal and Bimodal Contrastive Learning","url":"https://www.catalyzex.com/paper/coderetriever-unimodal-and-bimodal"}]

Based on the search results, here's the information about the CodeRetriever paper (arXiv:2201.10866):

**Paper Title:** CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search

**Authors:** Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, and Nan Duan

**Venue:** Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, pages 2898–2910, Abu Dhabi, United Arab Emirates

**Summary:** The paper proposes the CodeRetriever model, which learns function-level code semantic representations through large-scale code-text contrastive pre-training using both unimodal and bimodal contrastive learning schemes. CodeRetriever achieves state-of-the-art results on eleven domain/language-specific code search tasks with six programming languages across different code granularities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb88b688-0ced-4bf7-b9d6-913f58b6c39b",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a25497bf4e929bce1",
  "type": "user",
  "uuid": "ab03ee22-e6b5-4eff-9ddd-bc38d18ff960",
  "sourceToolAssistantUUID": "fb88b688-0ced-4bf7-b9d6-913f58b6c39b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-15T03:14:47.096Z_

Let me also confirm the UniXcoder author list and the SCodeR venue.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab03ee22-e6b5-4eff-9ddd-bc38d18ff960",
  "isSidechain": true,
  "agentId": "a25497bf4e929bce1",
  "requestId": "req_011Cb3dJ8nUjjmno2ZVub8ep",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0086f7d5-63cc-4e3f-9136-a0da79bf1a78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EK91FXp4wePEHmZ4yMy8DX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 882,
      "cache_creation_input_tokens": 3387,
      "cache_read_input_tokens": 21733,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3387,
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

_source line 34 · 2026-05-15T03:14:47.433Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vw411dKs7p7M9KbGpQgSv5`</summary>

```json
{
  "query": "UniXcoder ACL 2022 full author list Guo Lu Ren"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0086f7d5-63cc-4e3f-9136-a0da79bf1a78",
  "isSidechain": true,
  "agentId": "a25497bf4e929bce1",
  "requestId": "req_011Cb3dJ8nUjjmno2ZVub8ep",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c65e83c-f1bf-4803-8b26-4a1469c50338",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EK91FXp4wePEHmZ4yMy8DX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 882,
      "cache_creation_input_tokens": 3387,
      "cache_read_input_tokens": 21733,
      "output_tokens": 90,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3387
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 882,
          "output_tokens": 90,
          "cache_read_input_tokens": 21733,
          "cache_creation_input_tokens": 3387,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3387,
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

_source line 35 · 2026-05-15T03:14:51.213Z_

<details><summary>↩ Tool result · `toolu_01Vw411dKs7p7M9KbGpQgSv5`</summary>

```text
Web search results for query: "UniXcoder ACL 2022 full author list Guo Lu Ren"

Links: [{"title":"UniXcoder: Unified Cross-Modal Pre-training for Code Representation - ACL Anthology","url":"https://aclanthology.org/2022.acl-long.499/"},{"title":"UniXcoder: Unified Cross-Modal Pr... preview & related info | Mendeley","url":"https://www.mendeley.com/catalogue/7bb497ba-a8bd-3eca-9440-1bc6d55c2e30/"},{"title":"Aclanthology","url":"https://aclanthology.org/2022.acl-long.499.bib"},{"title":"[2203.03850] UniXcoder: Unified Cross-Modal Pre-training for Code Representation","url":"https://arxiv.org/abs/2203.03850"},{"title":"UniXcoder: Unified Cross-Modal Pre-training for Code Representation","url":"https://aclanthology.org/2022.acl-long.499.xml"},{"title":"UniXcoder: Unified Cross-Modal Pre-training for Code Representation [Quick Review]","url":"https://liner.com/review/unixcoder-unified-crossmodal-pretraining-for-code-representation"},{"title":"UniXcoder: Unified Cross-Modal Pre-training for Code Representation | Request PDF","url":"https://www.researchgate.net/publication/361068902_UniXcoder_Unified_Cross-Modal_Pre-training_for_Code_Representation"},{"title":"List of accepted papers - ACL 2022","url":"https://www.2022.aclweb.org/papers"},{"title":"UniXcoder: Unified Cross-Modal Pre-training for Code Representation","url":"https://bibbase.org/network/publication/guo-lu-duan-wang-zhou-yin-unixcoderunifiedcrossmodalpretrainingforcoderepresentation-2022"},{"title":"ACL 2022: Dublin, Ireland","url":"https://dblp.org/db/conf/acl/acl2022-1.html"}]

Based on the search results, the full author list for the UniXcoder paper presented at ACL 2022 is: Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, and Jian Yin. The paper was published in the Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 7212–7225, Dublin, Ireland.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c65e83c-f1bf-4803-8b26-4a1469c50338",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a25497bf4e929bce1",
  "type": "user",
  "uuid": "fc2b0ded-e319-409a-bc85-2f3d11dd6559",
  "sourceToolAssistantUUID": "7c65e83c-f1bf-4803-8b26-4a1469c50338",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-15T03:15:14.030Z_

Here are the verified citation details for all five papers:

---

**1. CodeBERT**

- **Authors:** Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Linjun Shou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou
- **Title:** CodeBERT: A Pre-Trained Model for Programming and Natural Languages
- **Venue:** Findings of the Association for Computational Linguistics: EMNLP 2020, pages 1536–1547
- **Year:** 2020
- **arXiv ID:** 2002.08155

Note: The paper uses bimodal pre-training (MLM + replaced token detection) on NL-PL pairs, not contrastive learning per se. If your bibliography describes it as "contrastive learning," you may want to revise that characterization.

---

**2. UniXcoder**

- **Authors:** Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin
- **Title:** UniXcoder: Unified Cross-Modal Pre-training for Code Representation
- **Venue:** Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL 2022), Volume 1: Long Papers, pages 7212–7225, Dublin, Ireland
- **Year:** 2022
- **arXiv ID:** 2203.03850

---

**3. CodeSage**

- **Authors:** Dejiao Zhang\*, Wasi Uddin Ahmad\*, Ming Tan, Hantian Ding, Ramesh Nallapati, Dan Roth, Xiaofei Ma, Bing Xiang (\* equal contribution)
- **Title:** Code Representation Learning At Scale
- **Venue:** ICLR 2024 (The Twelfth International Conference on Learning Representations)
- **Year:** 2024
- **arXiv ID:** 2402.01935

Important correction: CodeSage is from **Amazon Science**, not Salesforce.

---

**4. SCodeR / CodeRetriever / CodeContrastNet**

Neither "SCodeR" nor "CodeContrastNet" exists as a standalone published paper. The two closest matches for "recent contrastive learning for code search" are:

**(a) SCodeR** — This name refers to the method in:
- **Authors:** Xiaonan Li, Daya Guo, Yeyun Gong, Yun Lin, Yelong Shen, Xipeng Qiu, Daxin Jiang, Weizhu Chen, Nan Duan
- **Title:** Soft-Labeled Contrastive Pre-training for Function-level Code Representation
- **Venue:** Findings of EMNLP 2022
- **Year:** 2022
- **arXiv ID:** 2210.09597

**(b) CodeRetriever** — A closely related paper by overlapping authors:
- **Authors:** Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan
- **Title:** CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search
- **Venue:** EMNLP 2022 (main conference), pages 2898–2910, Abu Dhabi
- **Year:** 2022
- **arXiv ID:** 2201.10866

"CodeContrastNet" does not appear to be a real paper. If your bibliography references it, it may be a hallucinated citation that should be replaced with one of the above.

---

**5. StarCoder2**

- **Authors:** Anton Lozhkov, Raymond Li, Loubna Ben Allal, Federico Cassano, Joel Lamy-Poirier, Nouamane Tazi, Ao Tang, Dmytro Pykhtar, Jiawei Liu, Yuxiang Wei, et al. (66 authors total, BigCode collaboration)
- **Title:** StarCoder 2 and The Stack v2: The Next Generation
- **Venue:** arXiv preprint (no peer-reviewed venue as of this date)
- **Year:** 2024
- **arXiv ID:** 2402.19173

---

Sources:
- [CodeBERT - arXiv](https://arxiv.org/abs/2002.08155)
- [CodeBERT - ACL Anthology](https://aclanthology.org/2020.findings-emnlp.139/)
- [UniXcoder - arXiv](https://arxiv.org/abs/2203.03850)
- [UniXcoder - ACL Anthology](https://aclanthology.org/2022.acl-long.499/)
- [CodeSage - arXiv](https://arxiv.org/abs/2402.01935)
- [CodeSage - GitHub](https://github.com/amazon-science/CodeSage)
- [SCodeR - arXiv](https://arxiv.org/abs/2210.09597)
- [SCodeR - ACL Anthology](https://aclanthology.org/2022.findings-emnlp.9/)
- [CodeRetriever - arXiv](https://arxiv.org/abs/2201.10866)
- [CodeRetriever - ACL Anthology](https://aclanthology.org/2022.emnlp-main.187/)
- [StarCoder2 - arXiv](https://arxiv.org/abs/2402.19173)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc2b0ded-e319-409a-bc85-2f3d11dd6559",
  "isSidechain": true,
  "agentId": "a25497bf4e929bce1",
  "requestId": "req_011Cb3dJgibyqHbJwb4Qsg4S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9dc6d804-94e4-429d-a12b-fc93aaf613c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQGGm4GdSiARVA4iSWVxxy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1642,
      "cache_read_input_tokens": 25120,
      "output_tokens": 1416,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1642
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1416,
          "cache_read_input_tokens": 25120,
          "cache_creation_input_tokens": 1642,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1642,
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
