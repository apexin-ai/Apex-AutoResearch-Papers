# Research conversation: I need the correct bibliographic information for two papers to add to a LaTeX references.bib file: 1. **LEVER** - "LEVER

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a029c75b89731eed2.jsonl`
- **Structured JSON:** [`b841ef5a71556cbd0555.json`](../../sessions/b8/b841ef5a71556cbd0555.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

15 recorded events

### User

_source line 1 · 2026-05-15T22:03:13.538Z_

I need the correct bibliographic information for two papers to add to a LaTeX references.bib file:

1. **LEVER** - "LEVER: Learning to Verify Language-to-Code Generation with Execution" - This is about learned code verification. I believe it's by Ansong Ni et al., published at ICML 2023 or NeurIPS 2023.

2. **CodeT** - "CodeT: Code Generation with Generated Tests" - About using generated tests as a dual execution agreement for code generation. I believe it's by Bei Chen et al., published at ICLR 2023.

Please use WebSearch to verify the exact:
- Title
- Authors (at least first 3-4 authors)
- Venue/journal
- Year
- arXiv ID if available

Report the results concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8f5c528d-983f-4d95-953b-b91429522e05",
  "agentId": "a029c75b89731eed2",
  "type": "user",
  "uuid": "47909ed5-c01a-447d-8ec5-f56cd01d9ac2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "02554f3d-2969-4b95-9219-eaa71f5a8008",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T22:03:13.545Z_

```json
{
  "parentUuid": "47909ed5-c01a-447d-8ec5-f56cd01d9ac2",
  "isSidechain": true,
  "agentId": "a029c75b89731eed2",
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
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "7d499896-fe3a-4d59-9258-34dbeb88ee8d",
  "timestamp": "2026-05-15T22:03:13.545Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "02554f3d-2969-4b95-9219-eaa71f5a8008",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-15T22:03:16.770Z_



I'll search for both papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d499896-fe3a-4d59-9258-34dbeb88ee8d",
  "isSidechain": true,
  "agentId": "a029c75b89731eed2",
  "requestId": "req_011Cb57MHzxbvyZmNv6cnjec",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d42e616-c90c-4189-953a-f54866a6bbe7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "02554f3d-2969-4b95-9219-eaa71f5a8008",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BKXQD1t85xKxJLdAH9VM92",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14850,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14850,
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

_source line 4 · 2026-05-15T22:03:17.098Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NVskABDHMD5avarcq3SykP`</summary>

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
  "parentUuid": "2d42e616-c90c-4189-953a-f54866a6bbe7",
  "isSidechain": true,
  "agentId": "a029c75b89731eed2",
  "requestId": "req_011Cb57MHzxbvyZmNv6cnjec",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3f9fa92-312d-49eb-a30d-3aabb7c583da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "02554f3d-2969-4b95-9219-eaa71f5a8008",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BKXQD1t85xKxJLdAH9VM92",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14850,
      "cache_read_input_tokens": 0,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14850
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 86,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 14850,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14850,
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

_source line 5 · 2026-05-15T22:03:17.130Z_

<details><summary>↩ Tool result · `toolu_01NVskABDHMD5avarcq3SykP`</summary>

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
  "parentUuid": "c3f9fa92-312d-49eb-a30d-3aabb7c583da",
  "isSidechain": true,
  "promptId": "8f5c528d-983f-4d95-953b-b91429522e05",
  "agentId": "a029c75b89731eed2",
  "type": "user",
  "uuid": "ff69f448-974c-4e7f-83b3-696343d0fd86",
  "sourceToolAssistantUUID": "c3f9fa92-312d-49eb-a30d-3aabb7c583da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "02554f3d-2969-4b95-9219-eaa71f5a8008",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T22:03:20.276Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GTT7oCcDE26wZem56QrySw`</summary>

```json
{
  "query": "LEVER Learning to Verify Language-to-Code Generation with Execution Ansong Ni paper venue year arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff69f448-974c-4e7f-83b3-696343d0fd86",
  "isSidechain": true,
  "agentId": "a029c75b89731eed2",
  "requestId": "req_011Cb57Ma8ZqMu7Do9euDKJp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8ae2ef0-770b-40b6-8c3c-f0eb397f4b6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "02554f3d-2969-4b95-9219-eaa71f5a8008",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016u6LH1GRjsLcuiqURZ4rTv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 14850,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1450,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
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

_source line 7 · 2026-05-15T22:03:20.407Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NBHZQ3Nda4SJUyTAAtYSdg`</summary>

```json
{
  "query": "CodeT Code Generation with Generated Tests Bei Chen paper venue year arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8ae2ef0-770b-40b6-8c3c-f0eb397f4b6d",
  "isSidechain": true,
  "agentId": "a029c75b89731eed2",
  "requestId": "req_011Cb57Ma8ZqMu7Do9euDKJp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7005147-90e5-4ff6-8215-db3c847f89e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "02554f3d-2969-4b95-9219-eaa71f5a8008",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016u6LH1GRjsLcuiqURZ4rTv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 14850,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1450
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 127,
          "cache_read_input_tokens": 14850,
          "cache_creation_input_tokens": 1450,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1450,
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

_source line 8 · 2026-05-15T22:03:24.662Z_

<details><summary>↩ Tool result · `toolu_01NBHZQ3Nda4SJUyTAAtYSdg`</summary>

```text
Web search results for query: "CodeT Code Generation with Generated Tests Bei Chen paper venue year arXiv"

Links: [{"title":"[2207.10397] CodeT: Code Generation with Generated Tests","url":"https://arxiv.org/abs/2207.10397"},{"title":"[2207.10397v2] CodeT: Code Generation with Generated Tests","url":"https://arxiv.org/abs/2207.10397v2"},{"title":"[PDF] CodeT: Code Generation with Generated Tests | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CodeT:-Code-Generation-with-Generated-Tests-Chen-Zhang/876eb375cb7b365475040046df669c039ad54202"},{"title":"CodeT: Code Generation with Generated Tests - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv220710397C/abstract"},{"title":"CODET: CODE GENERATION WITH GENERATED TESTS","url":"https://openreview.net/pdf?id=ktrw68Cmu9c"},{"title":"CODET: CODE GENERATION WITH GENERATED TESTS","url":"https://arxiv.org/pdf/2207.10397"},{"title":"Paper page - CodeT: Code Generation with Generated Tests","url":"https://huggingface.co/papers/2207.10397"},{"title":"CodeT: Code Generation with Generated Tests · Machine Learning for Big Code and Naturalness","url":"https://ml4code.github.io/publications/chen2022codet/"},{"title":"CodeT: Code Generation with Generated Tests | OpenReview","url":"https://openreview.net/forum?id=ktrw68Cmu9c"},{"title":"(PDF) CodeT: Code Generation with Generated Tests","url":"https://www.researchgate.net/publication/362173423_CodeT_Code_Generation_with_Generated_Tests"}]

Based on the search results, here's the information about the CodeT paper:

**Paper Title:** CodeT: Code Generation with Generated Tests

**Author:** Bei Chen

**Year:** 2022 (July 21, 2022)

**Venue:** The paper was submitted to ICLR

**ArXiv Identifier:** 2207.10397

The paper proposes a method that leverages pre-trained language models to automatically generate test cases for code samples, helping to select the best code solution from multiple candidates generated by language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7005147-90e5-4ff6-8215-db3c847f89e9",
  "isSidechain": true,
  "promptId": "8f5c528d-983f-4d95-953b-b91429522e05",
  "agentId": "a029c75b89731eed2",
  "type": "user",
  "uuid": "2333fe60-10ea-49e4-b8c2-581631f710e8",
  "sourceToolAssistantUUID": "c7005147-90e5-4ff6-8215-db3c847f89e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "02554f3d-2969-4b95-9219-eaa71f5a8008",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T22:03:24.826Z_

<details><summary>↩ Tool result · `toolu_01GTT7oCcDE26wZem56QrySw`</summary>

```text
Web search results for query: "LEVER Learning to Verify Language-to-Code Generation with Execution Ansong Ni paper venue year arXiv"

Links: [{"title":"[2302.08468] LEVER: Learning to Verify Language-to-Code Generation with Execution","url":"https://arxiv.org/abs/2302.08468"},{"title":"LEVER: Learning to Verify Language-to-Code Generation with Execution","url":"https://proceedings.mlr.press/v202/ni23b.html"},{"title":"GitHub - niansong1996/lever: Code for paper \"LEVER: Learning to Verifiy Language-to-Code Generation with Execution\" (ICML'23)","url":"https://github.com/niansong1996/lever"},{"title":"[2302.08468v3] LEVER: Learning to Verify Language-to-Code Generation with Execution","url":"http://arxiv.org/abs/2302.08468v3"},{"title":"LEVER: Learning to Verify Language-to-Code Generation with Execution","url":"https://openreview.net/pdf?id=Gj3zN9zs4v"},{"title":"LEVER: Learning to Verify Language-to-Code Generation with Execution - Paper Detail","url":"https://deeplearn.org/arxiv/408448/lever:-learning-to-verify-language-to-code-generation-with-execution"},{"title":"[PDF] LEVER: Learning to Verify Language-to-Code Generation with Execution | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LEVER:-Learning-to-Verify-Language-to-Code-with-Ni-Iyer/59fe7cb560651281cfc5db6b8940da0e3ba9dea6"},{"title":"Ansong Ni, Srini Iyer, Dragomir Radev, Veselin Stoyanov, Wen-tau Yih, Sida Wang, Xi Lin · LEVER: Learning to Verify Language-to-Code Generation with Execution","url":"https://slideslive.com/39002838/lever-learning-to-verify-languagetocode-generation-with-execution"},{"title":"learning to verify language-to-code generation with execution","url":"https://dl.acm.org/doi/10.5555/3618408.3619494"},{"title":"LEVER: Learning to Verify Language-to-Code Generation with Execution | alphaXiv","url":"https://www.alphaxiv.org/resources/2302.08468v3"}]

Based on the search results, here is the information about the LEVER paper:

**Paper:** LEVER: Learning to Verify Language-to-Code Generation with Execution

**Authors:** Ansong Ni, Srini Iyer, Dragomir Radev, Ves Stoyanov, Wen-tau Yih, Sida I. Wang, Xi Victoria Lin

**Venue:** Proceedings of the 40th International Conference on Machine Learning

**Year:** 2023

**arXiv:** arXiv paper 2302.08468

The paper was first submitted to arXiv on February 16, 2023, with final versions updated through September 1, 2023.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8ae2ef0-770b-40b6-8c3c-f0eb397f4b6d",
  "isSidechain": true,
  "promptId": "8f5c528d-983f-4d95-953b-b91429522e05",
  "agentId": "a029c75b89731eed2",
  "type": "user",
  "uuid": "c10a2f47-4dc4-43b1-94e7-f0f558d03cb4",
  "sourceToolAssistantUUID": "d8ae2ef0-770b-40b6-8c3c-f0eb397f4b6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "02554f3d-2969-4b95-9219-eaa71f5a8008",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-15T22:03:27.802Z_

Let me get the full author list for CodeT and confirm the exact venue.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c10a2f47-4dc4-43b1-94e7-f0f558d03cb4",
  "isSidechain": true,
  "agentId": "a029c75b89731eed2",
  "requestId": "req_011Cb57N8Gr3TBFDe3LcN4oX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "197ba476-1004-443b-9cc8-5bf6512b3de9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "02554f3d-2969-4b95-9219-eaa71f5a8008",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtHgTuomn2FMVhGq3ArQCz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 624,
      "cache_creation_input_tokens": 956,
      "cache_read_input_tokens": 16300,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 956,
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

_source line 11 · 2026-05-15T22:03:28.398Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KF5pyw2CHujhk5n9omzrHm`</summary>

```json
{
  "query": "CodeT \"Bei Chen\" \"Fengji Zhang\" ICLR 2023 full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "197ba476-1004-443b-9cc8-5bf6512b3de9",
  "isSidechain": true,
  "agentId": "a029c75b89731eed2",
  "requestId": "req_011Cb57N8Gr3TBFDe3LcN4oX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6792639e-e3d7-451b-98b8-38165c65abf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "02554f3d-2969-4b95-9219-eaa71f5a8008",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtHgTuomn2FMVhGq3ArQCz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 624,
      "cache_creation_input_tokens": 956,
      "cache_read_input_tokens": 16300,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 956
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 624,
          "output_tokens": 92,
          "cache_read_input_tokens": 16300,
          "cache_creation_input_tokens": 956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 956,
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

_source line 12 · 2026-05-15T22:03:33.475Z_

<details><summary>↩ Tool result · `toolu_01KF5pyw2CHujhk5n9omzrHm`</summary>

```text
Web search results for query: "CodeT "Bei Chen" "Fengji Zhang" ICLR 2023 full author list"

Links: [{"title":"[PDF] RepoCoder: Repository-Level Code Completion Through Iterative Retrieval and Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RepoCoder:-Repository-Level-Code-Completion-Through-Zhang-Chen/af5c7848417882012203ac21399977ebda695a2b"},{"title":"ICLR Poster CodeT: Code Generation with Generated Tests","url":"https://iclr.cc/virtual/2023/poster/12011"},{"title":"[PDF] CodeT: Code Generation with Generated Tests | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CodeT:-Code-Generation-with-Generated-Tests-Chen-Zhang/876eb375cb7b365475040046df669c039ad54202"},{"title":"CodeT: Code Generation with Generated Tests | OpenReview","url":"https://openreview.net/forum?id=ktrw68Cmu9c"},{"title":"(PDF) CodeT: Code Generation with Generated Tests","url":"https://www.researchgate.net/publication/362173423_CodeT_Code_Generation_with_Generated_Tests"},{"title":"R $$^2$$ ComSync: improving code-comment synchronization with in-context learning and reranking | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-025-10800-4"},{"title":"Chen Wang","url":"https://cwchenwang.github.io/"},{"title":"11th ICLR 2023: Kigali, Rwanda","url":"https://dblp.org/db/conf/iclr/iclr2023.html"},{"title":"Paper Digest: ICLR 2023 Highlights – Resources | Paper Digest","url":"https://resources.paperdigest.org/2023/02/iclr-2023-highlights/"},{"title":"2023 Program Committee","url":"https://iclr.cc/Conferences/2023/ProgramCommittee"}]

Based on the search results, the full author list for CodeT is: Bei Chen, Fengji Zhang, A. Nguyen, Daoguang Zan, Zeqi Lin, Jian-Guang Lou, and Weizhu Chen. 

However, it appears there may be some confusion in your query. CodeT was published to ArXiv in 2022, not ICLR 2023. The paper you may be thinking of that was presented at ICLR 2023 is RepoCoder, which has authors Fengji Zhang, B. Chen, Yue Zhang, Jin Liu, Daoguang Zan, Yi Mao, Jian-Guang Lou, and Weizhu Chen.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6792639e-e3d7-451b-98b8-38165c65abf2",
  "isSidechain": true,
  "promptId": "8f5c528d-983f-4d95-953b-b91429522e05",
  "agentId": "a029c75b89731eed2",
  "type": "user",
  "uuid": "ecb08c77-6e7c-4aeb-ace2-3726760ad344",
  "sourceToolAssistantUUID": "6792639e-e3d7-451b-98b8-38165c65abf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "02554f3d-2969-4b95-9219-eaa71f5a8008",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T22:03:36.988Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012DZxfMf6eczKwgaWEgHghz`</summary>

```json
{
  "query": "site:openreview.net \"CodeT: Code Generation with Generated Tests\" authors ICLR 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecb08c77-6e7c-4aeb-ace2-3726760ad344",
  "isSidechain": true,
  "agentId": "a029c75b89731eed2",
  "requestId": "req_011Cb57NmN2bGvDS53k5MKA7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f04639f-2567-4520-bcd1-38ea1dcb728f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "02554f3d-2969-4b95-9219-eaa71f5a8008",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TbTz4PZpNP9HxoxnpRnMv1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 17256,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1451
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 17256,
          "cache_creation_input_tokens": 1451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1451,
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

_source line 14 · 2026-05-15T22:03:41.858Z_

<details><summary>↩ Tool result · `toolu_012DZxfMf6eczKwgaWEgHghz`</summary>

```text
Web search results for query: "site:openreview.net "CodeT: Code Generation with Generated Tests" authors ICLR 2023"

Links: [{"title":"CodeT: Code Generation with Generated Tests | OpenReview","url":"https://openreview.net/forum?id=ktrw68Cmu9c"},{"title":"ICLR Poster CodeT: Code Generation with Generated Tests","url":"https://iclr.cc/virtual/2023/poster/12011"},{"title":"[2207.10397] CodeT: Code Generation with Generated Tests","url":"https://arxiv.org/abs/2207.10397"},{"title":"CodeT: Code Generation with Generated Tests. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/1cd39ba64167b95c2c2f6057325314664"},{"title":"1. CodeT: Code Generation with Generated Tests - Presented by Sang-Ki Ko (23/1/4) - YouTube","url":"https://www.youtube.com/watch?v=0peY5Mds3c8"},{"title":"CodeT: Code Generation with Generated Tests [Quick Review]","url":"https://liner.com/review/codet-code-generation-with-generated-tests"},{"title":"(PDF) CodeT: Code Generation with Generated Tests","url":"https://www.researchgate.net/publication/362173423_CodeT_Code_Generation_with_Generated_Tests"},{"title":"Bei Chen, Fengji Zhang, Anh Nguyen, Daoguang Zan, Zeqi Lin, Jian-Guang Lou, Weizhu Chen · CodeT: Code Generation with Generated Tests","url":"https://slideslive.com/38999057/codet-code-generation-with-generated-tests"},{"title":"[PDF] CodeT: Code Generation with Generated Tests | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CodeT:-Code-Generation-with-Generated-Tests-Chen-Zhang/876eb375cb7b365475040046df669c039ad54202"},{"title":"CodeT: Code Generation with Generated Tests · Machine Learning for Big Code and Naturalness","url":"https://ml4code.github.io/publications/chen2022codet/"}]

I found the paper you're looking for! Here's the information from the OpenReview page:

**Title:** CodeT: Code Generation with Generated Tests (ICLR 2023 poster)

**Authors:** Bei Chen, Fengji Zhang, Anh Nguyen, Daoguang Zan, Zeqi Lin, Jian-Guang Lou, and Weizhu Chen

**OpenReview Link:** https://openreview.net/forum?id=ktrw68Cmu9c

**Summary:** The paper proposes CodeT, a novel method that leverages pre-trained language models to automatically generate test cases for code samples, reducing human effort and increasing test coverage. The authors conducted comprehensive experiments on four benchmarks (HumanEval, MBPP, APPS, and CodeContests) using five different pre-trained language models, showing that CodeT significantly improves code solution selection performance.

**Key Result:** CodeT improves the pass@1 metric on HumanEval to 65.8%, representing an 18.8% absolute improvement over code-davinci-002 and more than 20% over previous state-of-the-art results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f04639f-2567-4520-bcd1-38ea1dcb728f",
  "isSidechain": true,
  "promptId": "8f5c528d-983f-4d95-953b-b91429522e05",
  "agentId": "a029c75b89731eed2",
  "type": "user",
  "uuid": "49e81493-2a88-4097-bb20-50e146ba2ba5",
  "sourceToolAssistantUUID": "7f04639f-2567-4520-bcd1-38ea1dcb728f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "02554f3d-2969-4b95-9219-eaa71f5a8008",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-15T22:03:48.701Z_

Here are the verified bibliographic details for both papers:

---

**1. LEVER**

- **Title:** LEVER: Learning to Verify Language-to-Code Generation with Execution
- **Authors:** Ansong Ni, Srini Iyer, Dragomir Radev, Veselin Stoyanov, Wen-tau Yih, Sida I. Wang, Xi Victoria Lin
- **Venue:** ICML 2023 (Proceedings of the 40th International Conference on Machine Learning)
- **Year:** 2023
- **arXiv ID:** 2302.08468

---

**2. CodeT**

- **Title:** CodeT: Code Generation with Generated Tests
- **Authors:** Bei Chen, Fengji Zhang, Anh Nguyen, Daoguang Zan, Zeqi Lin, Jian-Guang Lou, Weizhu Chen
- **Venue:** ICLR 2023 (poster)
- **Year:** 2023
- **arXiv ID:** 2207.10397

---

Both your guesses were correct: LEVER is ICML 2023, and CodeT is ICLR 2023.

Sources:
- [LEVER on arXiv](https://arxiv.org/abs/2302.08468)
- [LEVER in ICML proceedings](https://proceedings.mlr.press/v202/ni23b.html)
- [CodeT on OpenReview](https://openreview.net/forum?id=ktrw68Cmu9c)
- [CodeT on arXiv](https://arxiv.org/abs/2207.10397)
- [CodeT ICLR 2023 poster page](https://iclr.cc/virtual/2023/poster/12011)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49e81493-2a88-4097-bb20-50e146ba2ba5",
  "isSidechain": true,
  "agentId": "a029c75b89731eed2",
  "requestId": "req_011Cb57PPWf3MEhNpqMHvjh8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95706b73-37bf-4230-bb81-357d61fba583",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "02554f3d-2969-4b95-9219-eaa71f5a8008",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D9a8V6LCBvrMzV5AjHuTa8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 923,
      "cache_read_input_tokens": 18707,
      "output_tokens": 436,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 923
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 436,
          "cache_read_input_tokens": 18707,
          "cache_creation_input_tokens": 923,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 923,
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
