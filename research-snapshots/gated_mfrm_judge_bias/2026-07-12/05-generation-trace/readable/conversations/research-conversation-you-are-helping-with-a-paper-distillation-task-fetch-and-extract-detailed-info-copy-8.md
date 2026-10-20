# Research conversation: You are helping with a paper distillation task. Fetch and extract detailed information from "Lost in Benchmarks? Rethink

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ad50cdb495cf40e2d.jsonl`
- **Structured JSON:** [`091ce6549e3144893322.json`](../../sessions/09/091ce6549e3144893322.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

38 recorded events

### User

_source line 1 · 2026-05-21T16:38:01.837Z_

You are helping with a paper distillation task. Fetch and extract detailed information from "Lost in Benchmarks? Rethinking LLM Benchmarking with IRT — PSN-IRT" (AAAI 2026).

Try these URLs using WebFetch:
1. Search: https://arxiv.org/search/?query=PSN-IRT+LLM+benchmarking+rethinking&searchtype=all
2. Also try: https://arxiv.org/search/?query=lost+in+benchmarks+rethinking+LLM+IRT&searchtype=all
3. If you find an arXiv ID, fetch the HTML version at https://arxiv.org/html/{id}

Extract ALL of the following in detail:
1. Full introduction text
2. All contribution statements
3. Complete experiment section (datasets, baselines, metrics, results)
4. All figure and table captions
5. Paragraphs referencing figures/tables
6. Limitations / future work
7. Method details (PSN-IRT model)
8. Implementation details
9. Ablation studies
10. Conclusion

Return COMPLETE extracted text, not summaries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "ad50cdb495cf40e2d",
  "type": "user",
  "uuid": "f6e841b5-b0ec-4cae-a513-9baa7f996a28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T16:38:01.840Z_

```json
{
  "parentUuid": "f6e841b5-b0ec-4cae-a513-9baa7f996a28",
  "isSidechain": true,
  "agentId": "ad50cdb495cf40e2d",
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
  "uuid": "16941e71-85ec-4240-951f-23a3c33df5fe",
  "timestamp": "2026-05-21T16:38:01.840Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-21T16:38:03.783Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HDj7jiTRULYCt41eK5UZZL`</summary>

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
  "parentUuid": "16941e71-85ec-4240-951f-23a3c33df5fe",
  "isSidechain": true,
  "agentId": "ad50cdb495cf40e2d",
  "requestId": "req_011CbG3QVmJD8sZv42MaoJqv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4439bfed-3c46-4a8d-9c18-78c769f68720",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AUjvqnnYKeF9s8zfCda9iE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9114,
      "cache_read_input_tokens": 7260,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9114
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 80,
          "cache_read_input_tokens": 7260,
          "cache_creation_input_tokens": 9114,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9114,
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

_source line 4 · 2026-05-21T16:38:03.785Z_

<details><summary>↩ Tool result · `toolu_01HDj7jiTRULYCt41eK5UZZL`</summary>

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
  "parentUuid": "4439bfed-3c46-4a8d-9c18-78c769f68720",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "ad50cdb495cf40e2d",
  "type": "user",
  "uuid": "f1bc346a-dc38-4d87-88e8-488a2370105d",
  "sourceToolAssistantUUID": "4439bfed-3c46-4a8d-9c18-78c769f68720",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-21T16:38:05.724Z_

I'll search for this paper and fetch its content systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1bc346a-dc38-4d87-88e8-488a2370105d",
  "isSidechain": true,
  "agentId": "ad50cdb495cf40e2d",
  "requestId": "req_011CbG3QeKzV3wQ85F7TtM97",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5380d188-a1f7-4911-baa4-bb78f5daea63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016onMoyBbFXUF6pLPdhogtE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 16374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

_source line 6 · 2026-05-21T16:38:06.939Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019eHjJ5TvhVEGCYXi8NrhLS`</summary>

```json
{
  "query": "PSN-IRT LLM benchmarking \"lost in benchmarks\" IRT AAAI 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5380d188-a1f7-4911-baa4-bb78f5daea63",
  "isSidechain": true,
  "agentId": "ad50cdb495cf40e2d",
  "requestId": "req_011CbG3QeKzV3wQ85F7TtM97",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "26c17344-f8d2-4898-a5a9-4a3739220577",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016onMoyBbFXUF6pLPdhogtE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 16374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

_source line 7 · 2026-05-21T16:38:07.318Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QAti1k6RkXVgQPRdzUDh9L`</summary>

```json
{
  "query": "\"rethinking LLM benchmarking\" IRT \"item response theory\" AAAI 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26c17344-f8d2-4898-a5a9-4a3739220577",
  "isSidechain": true,
  "agentId": "ad50cdb495cf40e2d",
  "requestId": "req_011CbG3QeKzV3wQ85F7TtM97",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0e841d0-096b-456b-a0ef-7930eeb9613d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016onMoyBbFXUF6pLPdhogtE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 16374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

_source line 8 · 2026-05-21T16:38:12.694Z_

<details><summary>↩ Tool result · `toolu_019eHjJ5TvhVEGCYXi8NrhLS`</summary>

```text
Web search results for query: "PSN-IRT LLM benchmarking "lost in benchmarks" IRT AAAI 2026 arXiv"

Links: [{"title":"[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/abs/2505.15055"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40814"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with","url":"https://ojs.aaai.org/index.php/AAAI/article/download/40814/44775"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://chatpaper.com/paper/139423"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/pdf/2505.15055"},{"title":"GitHub - Joe-Hall-Lee/PSN-IRT: [AAAI 2026 Oral] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory · GitHub","url":"https://github.com/Joe-Hall-Lee/PSN-IRT"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v2"}]

I found the paper you're searching for! Here's what I found:

## "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory"

The paper proposes PSN-IRT (Pseudo-Siamese Network for Item Response Theory), an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture.

### Key Findings:

Based on PSN-IRT, the authors conducted extensive analysis on 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality.

The main results include:
- LLM benchmarks fail to achieve simultaneous excellence across multiple measurements
- LLM benchmarks suffer from widespread saturation and insufficient difficulty ceilings, limiting their ability to challenge and accurately evaluate advanced models
- LLM benchmarks exhibit data contamination in numerous items, compromising their reliability

### Publication:

The paper was published in the Proceedings of the AAAI Conference on Artificial Intelligence in 2026, and it was submitted to arXiv on May 21, 2025 with the latest revision on January 16, 2026.

You can find the full paper on arXiv at [2505.15055](https://arxiv.org/abs/2505.15055) and the code on [GitHub](https://github.com/Joe-Hall-Lee/PSN-IRT).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26c17344-f8d2-4898-a5a9-4a3739220577",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "ad50cdb495cf40e2d",
  "type": "user",
  "uuid": "c5f95e57-5aa6-4714-92e2-2683c8fa2380",
  "sourceToolAssistantUUID": "26c17344-f8d2-4898-a5a9-4a3739220577",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T16:38:13.770Z_

<details><summary>↩ Tool result · `toolu_01QAti1k6RkXVgQPRdzUDh9L`</summary>

```text
Web search results for query: ""rethinking LLM benchmarking" IRT "item response theory" AAAI 2026"

Links: [{"title":"GitHub - Joe-Hall-Lee/PSN-IRT: [AAAI 2026 Oral] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory · GitHub","url":"https://github.com/Joe-Hall-Lee/PSN-IRT"},{"title":"[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/abs/2505.15055"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40814"},{"title":"(PDF) Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://www.researchgate.net/publication/391954139_Lost_in_Benchmarks_Rethinking_Large_Language_Model_Benchmarking_with_Item_Response_Theory"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://chatpaper.com/paper/139423"},{"title":"[Literature Review] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://www.themoonlight.io/en/review/lost-in-benchmarks-rethinking-large-language-model-benchmarking-with-item-response-theory"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with","url":"https://arxiv.org/pdf/2505.15055"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v2"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/pdf/2511.04689"}]

I found the paper you're looking for! Here are the search results:

## Main Paper: "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory"

This is an AAAI 2026 Oral presentation paper titled "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory".

### Overview
The paper addresses how inconsistencies between different leaderboards and poor separability among top models raise concerns about their ability to accurately reflect authentic model capabilities.

### Main Contribution
The paper proposes Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture, which can be utilized for accurate and reliable estimations of item characteristics and model abilities.

### Key Findings
The analysis covers 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality. The paper demonstrates that leveraging PSN-IRT is able to construct smaller benchmarks while maintaining stronger alignment with human preference.

### Resources
- **GitHub Repository**: https://github.com/Joe-Hall-Lee/PSN-IRT
- **ArXiv**: https://arxiv.org/abs/2505.15055
- **AAAI Proceedings**: https://ojs.aaai.org/index.php/AAAI/article/view/40814


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0e841d0-096b-456b-a0ef-7930eeb9613d",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "ad50cdb495cf40e2d",
  "type": "user",
  "uuid": "2b7243bf-8b3d-49b0-9bb3-b2c9e7f91e16",
  "sourceToolAssistantUUID": "f0e841d0-096b-456b-a0ef-7930eeb9613d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-21T16:38:18.265Z_

Found it. arXiv ID is 2505.15055. Let me fetch the full HTML version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b7243bf-8b3d-49b0-9bb3-b2c9e7f91e16",
  "isSidechain": true,
  "agentId": "ad50cdb495cf40e2d",
  "requestId": "req_011CbG3RNktzzy2PpegFDQq5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "362c7deb-aee7-47ff-856d-6839fe219fbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QpBXWENhzVSnEnawD5wmxN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1874,
      "cache_read_input_tokens": 18309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1874,
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

_source line 11 · 2026-05-21T16:38:21.579Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PkZGgoUbR4Fw7Jgd14ozH9`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.15055v2",
  "prompt": "Extract ALL of the following complete text verbatim (do not summarize):\n1. Full introduction section\n2. All contribution statements\n3. Complete method/model description (PSN-IRT)\n4. Complete experiment section: datasets, baselines, metrics, all results\n5. All figure captions and table captions (every single one)\n6. All paragraphs that reference figures or tables\n7. Limitations and future work\n8. Implementation details\n9. Ablation studies\n10. Conclusion section\nReturn the complete extracted text with section headers preserved."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "362c7deb-aee7-47ff-856d-6839fe219fbf",
  "isSidechain": true,
  "agentId": "ad50cdb495cf40e2d",
  "requestId": "req_011CbG3RNktzzy2PpegFDQq5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf8919af-eca3-40a3-b34d-123422733899",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QpBXWENhzVSnEnawD5wmxN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1874,
      "cache_read_input_tokens": 18309,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1874
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 231,
          "cache_read_input_tokens": 18309,
          "cache_creation_input_tokens": 1874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1874,
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

_source line 12 · 2026-05-21T16:39:22.857Z_

<details><summary>↩ Tool result · `toolu_01PkZGgoUbR4Fw7Jgd14ozH9`</summary>

```text
# Extracted Content from "Lost in Benchmarks?"

## 1. Full Introduction Section

As the scale and performance of large language models (LLMs) continue to grow, accurately measuring their capabilities has become increasingly important. Currently, the performance of LLMs is primarily evaluated through various benchmarks, which are comprehensive test suites consisting of carefully designed questions to assess model behavior across different tasks. However, in practice, existing benchmarks often exhibit significant limitations, prompting consideration of their effectiveness.

Different benchmarks often produce inconsistent leaderboards. This issue persists even for benchmarks designed to evaluate similar underlying capabilities, leading to the same model achieving substantially varying rankings across evaluations. Many benchmarks show weak separability among top models, limiting the ability to understand performance differences and further model refinement. Given these limitations, there is a growing need for a more systematic analysis of LLM benchmarks.

The authors conduct comprehensive analysis of various popular LLM benchmark datasets based on Item Response Theory (IRT), a psychometric framework widely used in educational assessment that analyzes item properties such as difficulty by modeling item response against examinee ability. Traditional IRT struggles with the complexity and scale of modern datasets, and its assumption of the normal distribution of abilities does not always hold.

To advance their objective, they propose the Pseudo-Siamese Network for IRT (PSN-IRT), a framework for comprehensive and interpretable analysis of benchmark test sets. PSN-IRT processes model identifiers and item identifiers through independent neural network pathways to estimate latent model ability and a rich set of item parameters. The estimated properties are then integrated using an IRT-based formulation to predict outcome probabilities.

## 2. All Contribution Statements

The authors summarize their contributions as follows:

1. They propose PSN-IRT, a benchmark analysis framework with superior estimation accuracy and reliability.

2. They use PSN-IRT for an in-depth analysis of mainstream benchmarks, and found that current LLM benchmarks present deficiencies in many aspects.

3. They show that selecting items with PSN-IRT leads to model rankings that better align with human preference.

## 3. Complete Method/Model Description (PSN-IRT)

### Model Architecture

The PSN-IRT architecture comprises two independent networks: a model network and an item network. The model network processes one-hot encoded LLM identifiers to estimate model-ability θ, while the item network handles one-hot encoded item identifiers to produce the four IRT parameters: discriminability a, difficulty b, guessing-rate c, and feasibility d.

Each network consists of three fully connected layers with ReLU activation functions, enabling efficient and stable parameter estimation. After that, these estimated properties are then processed by a Logistic Calculation Layer. This layer operates using the Four-Parameter Logistic (4PL) model, an advanced IRT formulation that extends simpler models like the 1PL to capture nuanced behaviors:

**P(X=1|θ)=c+(d−c)⋅1/(1+e^(−a(θ−b)))**

Where each parameter controls a different aspect of benchmark item behavior:

- The difficulty b determines the ability level where the probability changes most significantly.
- The discriminability a reflects an item's power to differentiate between models of varying abilities.
- The guessing-rate c captures how likely models are to succeed without full understanding.
- The feasibility d represents the maximum probability that even highly proficient models will correctly answer the item.

### Training and Applications

The PSN-IRT is trained end-to-end using the observed binary response data in the form of (Model, Item, Response, Outcome), where the binary outcome indicates the correctness of each LLM on each benchmark item. During training, PSN-IRT processes encoded pairs of LLM and item identifiers through their respective network pathways. For each pair, the PSN-IRT framework first internally estimates the specific model and item properties. These estimated properties are then passed to a Logistic Calculation Layer, with the training objective:

**J(θ)=−(1/N)∑[y_i·log(P_i)+(1−y_i)·log(1−P_i)]**

Where N is the batch size. The training objective is to minimize the discrepancy between the model's prediction and the observed binary outcomes. All learnable weights within both the model and item networks are updated simultaneously, concurrently optimizing the estimated properties for both models and benchmark items.

Upon completion of training, the two networks of PSN-IRT can be used for evaluating model performance and diagnosing benchmark characteristics. The Model Network outputs an estimate of the model ability θ, while the Item Network outputs its four estimated psychometric parameters a,b,c,d, which can be used for diagnosis of individual item characteristics and overall benchmark quality.

## 4. Complete Experiment Section

### Datasets

The authors select 11 datasets that vary in domain coverage. They are:

- **ARC-C**: 295 items, General domain, EM metric, Multiple Choice
- **BBH**: 6,511 items, General domain, EM metric, Mixed format
- **Chinese SimpleQA**: 3,000 items, Knowledge domain, LLM-as-a-Judge metric, QA format
- **GPQA Diamond**: 198 items, Science domain, EM metric, Multiple Choice
- **GSM8K**: 1,319 items, Math domain, EM metric, QA format
- **HellaSwag**: 10,042 items, General domain, EM metric, Multiple Choice
- **HumanEval**: 164 items, Code domain, Pass@1 metric, QA format
- **MATH**: 5,000 items, Math domain, EM metric, QA format
- **MBPP**: 500 items, Code domain, Pass@1 metric, QA format
- **MMLU**: 14,042 items, General domain, EM metric, Multiple Choice
- **TheoremQA**: 800 items, Science domain, EM metric, QA format

To construct training data, they conduct evaluations using OpenCompass. The evaluation results are collected in the form of binary outcomes, indicating whether each model answered each item correctly. They construct a unified outcome matrix by aggregating item-level results across all models and benchmarks, then split the interactions into training, validation, and test sets.

The authors mainly focus on currently high-performing models, including 360GPT2-Pro, DeepSeek-V3, Doubao-Pro, Gemini-1.5, Hunyuan-Turbo, Moonshot-v1, Qwen-Plus, and Yi-Lightning. However, testing only strong models might obscure differences in the discriminability of the test sets. To address this, they intentionally included several relatively weaker models, including Gemma-2B-it, Mistral-7B-Instruct-v0.1, Qwen2.5-3B-Instruct, and Vicuna-7B-v1.3.

### Baselines

They mainly compare PSN-IRT with traditional IRT methods, namely IRT estimated based on traditional parameter estimation techniques, including Maximum Likelihood Estimation (MLE), Markov Chain Monte Carlo (MCMC), Variational Inference (VI), and VIBO. They also compare with Deep-IRT, which is an extension of 1PL IRT that learns item-trait interactions via deep networks.

### Metrics

To assess whether the learned parameters meaningfully reflect corresponding properties, they use two quantitative metrics:

- **Prediction accuracy**: Following standard practice in educational testing, they assess how well a method predicts whether a model answers an item correctly, reporting accuracy, F1 score, and ROC AUC.

- **Rank stability**: To evaluate the reliability of model ranking induced by each method, they split the test set into two subsets, estimate model abilities separately, and compute Kendall's τ between the resulting rankings.

### Main Results

Table 2 shows the estimation accuracy and reliability of PSN-IRT compared to traditional IRT and Deep-IRT. Both Deep-IRT and PSN-IRT significantly outperform traditional IRT in prediction accuracy. Despite its simpler Logistic output layer rooted in the IRT formula, PSN-IRT attains prediction accuracy on par with the more complex Deep-IRT, and surpasses it in rank reliability.

Given their goal to comprehensively capture diverse item characteristics, they adopt the more expressive 4PL structure for all methods except Deep-IRT. Experiments also confirm that PSN-IRT performs best with 4PL.

Results table comparing methods (IRT with 4PL MLE, IRT with 4PL MCMC, IRT with 4PL VI, IRT with 4PL VIBO, Deep-IRT with 1PL, PSN-IRT with 4PL) show ACC ranging from 0.7070-0.7998, F1 from 0.7811-0.8538, AUC from 0.6940-0.8519, and Kendall's τ from 0.9091-1.0000.

## 5. All Figure and Table Captions

**Figure 1**: Illustration of weak separability and ranking inconsistencies in LLM benchmarks (reference: opencompass.org.cn)

**Figure 2**: The illustration of the proposed PSN-IRT. Separate neural networks estimate model ability (θ) and item parameters (a,b,c,d), which are then combined via the IRT formula to predict the probability of a correct response. After that, the networks can be leveraged for estimating properties for models or items, respectively.

**Table 1**: Benchmarks used in this paper. Lists all 11 datasets with their data sizes, domains, metrics, and formats.

**Table 2**: Comparison of prediction accuracy and rank reliability across different methods. Shows performance metrics (ACC, F1, AUC, Kendall's τ) for various IRT-based approaches.

**Table 3**: Ablation study on PSN-IRT's input representation and network architecture. Compares PSN-IRT baseline with variants using embeddings and GNN.

**Table 4**: Pearson correlation coefficients of item parameters estimated on random subsets of the data versus those estimated on the full dataset. Shows stability across 30%, 50%, and 70% data subsets.

**Table 5**: Ranks of datasets based on average item-level properties estimated by PSN-IRT. Each dataset's score is the mean of its benchmark items' property. Lower values indicate better performance in that property.

**Figure 3**: Distribution of item-level properties across 11 LLM benchmarks.

**Table 6**: Variance and Kendall's τ for various data selection strategies with and without weak models. Shows results for All items, Top 400 items, and Top 1000 items using different selection methods.

**Table 8**: Average item-level properties across datasets. Each value represents the mean of the corresponding metric over all benchmark items.

**Figure 4**: Scatter plots showing the relationship between item difficulty and discriminability across 11 benchmarks. Each plot highlights how difficulty affects discriminability within a dataset.

**Figure 5**: Examples of benchmark items exhibiting high and low estimated values for key psychometric parameters, as determined by PSN-IRT. Each pair shows an item with a high parameter value alongside one with a low value for the specified characteristic.

**Table 7**: Comparison of prediction accuracy and rank reliability across different methods using 1PL-4PL parameters. Shows performance for IRT (MLE, MCMC, VI, VIBO), Deep-IRT, and PSN-IRT.

## 6. Paragraphs Referencing Figures and Tables

[Comprehensive paragraphs analyzing each result are included in the benchmark analysis section below]

## 7. Findings from Benchmark Analysis

### Finding 1: LLM benchmarks fail to achieve simultaneous excellence across multiple measurement properties

The results clearly demonstrate this lack of simultaneous excellence. While Chinese SimpleQA achieves the best overall score, no benchmark performs universally well across the individual metrics. For instance, Chinese SimpleQA itself suffers from poor feasibility with a rank of 9. This pattern of strengths being offset by significant weaknesses is common across benchmarks, which underscores the inherent challenges and trade-offs in benchmark design. The property distributions further highlight this variability and the difficulty for any single benchmark to achieve balanced, high quality across all desired measurement properties.

### Finding 2: Current LLM benchmarks exhibit an insufficient difficulty ceiling to challenge the most advanced models

Difficulty is varied among different benchmarks. Datasets such as TheoremQA, Chinese SimpleQA, and GPQA Diamond lead in difficulty and continue to challenge many LLMs. In contrast, other benchmarks including ARC-C, HellaSwag, and HumanEval have become comparatively easy, where many of the items are readily solved by high-performing models, diminishing their utility for differentiating top-tier systems.

Crucially, even within more challenging benchmarks, items often present only moderate difficulty to elite LLMs. For instance, item difficulty scores in the IRT scaling may be as low as 1.0 for models exhibiting ability scores above 3.0. This suggests that while such benchmarks can assess average models, they are less effective at separating most advanced systems, suggesting that they are insufficient for comprehensively evaluating frontier model capabilities.

### Finding 3: Generally low LEH scores across most benchmarks reveal widespread item saturation

While datasets like GPQA Diamond and TheoremQA achieve the highest relative ranks for average LEH, suggesting they offer more headroom than other benchmarks, the absolute LEH values are often smaller than ideal. Conversely, benchmarks such as MATH and particularly GSM8K exhibit even lower average LEH scores. This signifies that current high-performing models are already approaching or have reached the performance ceiling for a substantial portion of items within these test sets. This necessitates the development of new benchmark items and datasets explicitly designed with greater headroom as models continue to evolve.

### Finding 4: Outlier-high guessing-rates in many benchmark items flag risks of data contamination

The guessing-rate reflects the chance that a model can answer a question correctly without actual understanding, typically by exploiting format-based cues or shortcuts. Datasets like ARC-C, HellaSwag, and MMLU generally present higher guessing-rates, possibly due to their multiple-choice formats. Further inspection reveals that a considerable number of items across several benchmarks exhibit unusually high guessing-rates. This observation regards the potential for such items to indicate data contamination, namely the content or answers for these items might have been present in the models' pre-training data.

### Finding 5: Widespread low-feasibility items in scientific benchmarks reveal flawed question design

Feasibility estimates how well a question can be answered based on the information provided. Low feasibility often arises from underspecified or overly broad questions, where even a strong model cannot determine a clear answer. Datasets like TheoremQA and GPQA Diamond exhibit lower feasibility, likely due to complex scientific contexts or vague problem descriptions. In contrast, ARC-C and HellaSwag have high feasibility, suggesting their questions are well-formed and specific. Low feasibility more often reflects weaknesses in annotation quality or task design, and such items can distort evaluation by penalizing models for failing to resolve ambiguities.

## 8. Efficient Benchmarking with PSN-IRT

### Experimental Setup

To evaluate the effectiveness of different item selection strategies, they design an experiment to evaluate the effectiveness of different item selection strategies using Benchmark Agreement Testing (BAT). They first establish a reference model ranking by aggregating results from two public leaderboards: Chatbot Arena and OpenCompass Arena (based on human evaluation and reflecting human preference regarding overall model capabilities). Subsequently, various subsets of benchmark items are chosen based on different criteria. Model rankings generated using these subsets are then compared against the reference arena ranking using Kendall's τ to measure agreement. They also consider the variance of model scores on these subsets; higher variance generally indicates the subset's capacity to differentiate more clearly between models. The evaluations are conducted using two distinct model groupings: one set comprising a mix of stronger and weaker models ("w/ weak models"), and another set from which weaker models are excluded ("w/o weak models"), to specifically assess separability among stronger contenders.

### Results

Selecting items based on Fisher information consistently produces model rankings with superior alignment to the reference arena ranking. For instance, a carefully selected subset composed of just 1,000 items chosen via the Fisher information criterion achieves a Kendall's τ of up to 0.9048. This level of agreement markedly surpasses that achieved by rankings derived from using all available items or from similarly sized randomly selected subsets.

In contrast, other item selection approaches are less effective for differentiating among strong models. For instance, selecting items based on discriminability results in zero score variance when weak models are excluded, indicating it merely separates broad capability tiers rather than providing granularity among top-performers. A strategy of clustering items based on their success/failure vectors also fails to improve ranking correlation, even when it increases score separability.

## 9. Implementation Details

### Estimation Ability of PSN-IRT

To evaluate the estimation ability of PSN-IRT against baselines, they first construct a unified response matrix by aggregating item-level results across all models and benchmarks. They then split these model-item interactions into training (60%), validation (20%), and test sets (20%). The model is trained on the training set using the Adam optimizer with a learning rate of 0.003 and a weight decay of 0.0001, and a batch size of 512. To ensure robust model selection and prevent overfitting, they employ an early stopping strategy with a patience of 5 epochs, monitored based on the F1 score on the validation set.

For the subsequent benchmark analysis where the goal is to obtain the most stable parameter estimates for all items, they train the PSN-IRT model on the entire unified dataset. In this phase, the model is trained for a fixed 30 epochs using the same hyperparameters. All training is conducted on a single NVIDIA A800-80G GPU.

## 10. Ablation Studies

### Model Architecture Variants

To assess whether more complex architectures offer benefits over their straightforward design, they conduct an ablation study. Specifically, they compare PSN-IRT with two variants: one replaces one-hot inputs with semantic embeddings from Instructor, and the other uses a GNN instead of the MLP backbone.

Both alternatives underperform their original design. They argue that semantic similarity between item texts does not necessarily reflect similarity in measurement characteristics. For the GNN variant, its neighborhood aggregation mechanism risks diluting the unique statistical signals of individual models and items, thereby hindering precise parameter estimation. These results suggest that in this estimation scenario, preserving the individuality of models and items is more effective than introducing architectural complexity.

### Parameter Stability Analysis

Since PSN-IRT estimates parameters that are specific to the training data, requiring retraining to analyze new items, they also investigate the stability of these estimates when the item pool changes. To simulate this, they conduct an experiment by independently training separate PSN-IRT models on random subsets of the items. They then compute the Pearson correlation between the item parameters estimated from these subsets and those estimated from the full dataset.

The results reveal a high degree of correlation across all parameters. This indicates that PSN-IRT learns highly consistent intrinsic properties for the items regardless of the specific data sample, demonstrating the stability of parameter estimation.

### Semantic Embedding Variant

To explore the utility of item content, they substitute one-hot encoded item identifiers with dense semantic embeddings generated for the text of each benchmark item using the pre-trained Instructor-XL. These embeddings serve as the direct input to the item network, replacing the one-hot encoding pathway while the rest of the PSN-IRT architecture remains unchanged. However, these variants fail to yield significant improvements.

### Graph Neural Network (GNN) Variant

To investigate the role of network architecture, they implemented a custom GNN-based encoder. This encoder updates a model's initial embedding by aggregating information from all interactions in the training graph. For each interaction between a model and an item with a binary outcome, a cognitive degree is first computed, then a cognitive state is formed through an element-wise product. The updated embedding for a model is obtained by performing an attention-weighted aggregation of the cognitive states from all items it has interacted with. However, both variants fail to yield performance gains.

## 11. Conclusion Section

In this work, the authors introduce PSN-IRT, a framework that combines psychometrics with neural networks to provide comprehensive and reliable analyses of LLM benchmarks. Through extensive experiments on 12 LLMs across 11 diverse datasets, they demonstrate that current benchmarks often suffer from uneven measurement properties, insufficient difficulty ceilings, item saturation, and data contamination. Moreover, they show that strategically selecting smaller, high-quality item sets using PSN-IRT enhances alignment with human preference and separability among top models.

---

**Note**: Due to length constraints, the complete implementation details for all technical sections and some ancillary analyses have been condensed while preserving all critical information and findings. The original document contains additional references and detailed statistical tables that support these conclusions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf8919af-eca3-40a3-b34d-123422733899",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "ad50cdb495cf40e2d",
  "type": "user",
  "uuid": "007caad2-8aa4-4925-bfc3-1a89ad07c9d7",
  "sourceToolAssistantUUID": "cf8919af-eca3-40a3-b34d-123422733899",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-21T16:39:25.632Z_

Good first pass. Now let me fetch additional details — the full paper PDF for complete text on figures, tables, method formulation, and any missing sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "007caad2-8aa4-4925-bfc3-1a89ad07c9d7",
  "isSidechain": true,
  "agentId": "ad50cdb495cf40e2d",
  "requestId": "req_011CbG3WUAy4AKV3DhQxvrWp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03e990d8-b049-4751-86f8-249aa0b3b2dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BP9vven6yq1MybCjevo4ww",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5114,
      "cache_read_input_tokens": 20183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5114,
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

_source line 14 · 2026-05-21T16:39:30.749Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01H1UGAbADYrq6238vrtvjFn`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.15055v2",
  "prompt": "Extract verbatim text from these specific sections:\n1. The complete Related Work section\n2. The complete Problem Formulation section (if any)\n3. The complete IRT Background section\n4. The exact text describing each benchmark finding in detail (Finding 1 through Finding 5, with exact numbers)\n5. The exact Table 5 data (ranks of datasets based on item properties)\n6. The exact Table 6 data (variance and Kendall tau for data selection strategies)\n7. The exact Table 2 numbers (all rows and columns)\n8. The complete discussion of Figure 3 (distribution of item properties)\n9. The complete discussion of Figure 4 (scatter plots)\n10. Any appendix or supplementary material text\nReturn complete verbatim text with all numbers preserved."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03e990d8-b049-4751-86f8-249aa0b3b2dc",
  "isSidechain": true,
  "agentId": "ad50cdb495cf40e2d",
  "requestId": "req_011CbG3WUAy4AKV3DhQxvrWp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02e7e434-224e-48d5-907c-649e3dc7aee4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BP9vven6yq1MybCjevo4ww",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5114,
      "cache_read_input_tokens": 20183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5114,
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

_source line 15 · 2026-05-21T16:39:31.781Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017g1kGBdZ3MVaePJr5taWx6`</summary>

```json
{
  "url": "https://github.com/Joe-Hall-Lee/PSN-IRT",
  "prompt": "Extract all text from the README including: paper description, method details, dataset information, experimental setup, results, and any implementation notes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02e7e434-224e-48d5-907c-649e3dc7aee4",
  "isSidechain": true,
  "agentId": "ad50cdb495cf40e2d",
  "requestId": "req_011CbG3WUAy4AKV3DhQxvrWp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1e83c47-b74f-49e8-bcc5-07c522f312ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BP9vven6yq1MybCjevo4ww",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5114,
      "cache_read_input_tokens": 20183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5114,
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

_source line 16 · 2026-05-21T16:39:37.207Z_

<details><summary>↩ Tool result · `toolu_017g1kGBdZ3MVaePJr5taWx6`</summary>

```text
# PSN-IRT: LLM Benchmarking via Item Response Theory

## Overview
This repository presents research on improving how large language models are evaluated through benchmarks. The work introduces PSN-IRT, a framework applying Item Response Theory (IRT) to analyze benchmark quality systematically.

## Key Components

**Dataset:**
The research uses a unified binary response matrix containing evaluation results for 12 LLMs across 11 benchmarks, encompassing 41,871 items total. Data was sourced through OpenCompass, with entries marked as 1 for correct answers and 0 otherwise.

**Outputs:**
- Student abilities file: Contains estimated latent ability scores (θ) for each of the 12 models, representing "psychometrically measured proficiency"
- Item parameters file: Includes discriminability (a), difficulty (b), guessing-rate (c), and feasibility (d) parameters for all 41,871 items using a 4-parameter logistic model

## Implementation

**Training Protocol:**
Users can execute the training script with customizable parameters: maximum epochs (30), batch size (512), and learning rate (0.003). The script processes the unified response matrix to generate model ability estimates and item parameters.

## Publication Details
The work was accepted as an oral presentation at AAAI 2026 and is authored by Zhou, Huang, and colleagues. The preprint is available on arXiv (2505.15055).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1e83c47-b74f-49e8-bcc5-07c522f312ca",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "ad50cdb495cf40e2d",
  "type": "user",
  "uuid": "0321520d-7daf-40c3-a0a8-25eda832394c",
  "sourceToolAssistantUUID": "b1e83c47-b74f-49e8-bcc5-07c522f312ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T16:39:37.265Z_

<details><summary>↩ Tool result · `toolu_01H1UGAbADYrq6238vrtvjFn`</summary>

```text
# Response

I appreciate your detailed request, but I need to respectfully decline to extract and reproduce the exact verbatim text as requested. Your ask specifically requests complete verbatim reproduction of multiple major sections, tables, and findings from this academic paper—which would constitute substantial copyright infringement despite the document being from arxiv.org.

## What I can appropriately provide instead:

**Summary of key content:**

The paper proposes PSN-IRT (Pseudo-Siamese Network for Item Response Theory) to analyze LLM benchmark quality. It evaluates 11 benchmarks across 12 models using four item parameters: difficulty, discriminability, guessing-rate, and feasibility.

**Five main findings identified:**
1. LLM benchmarks lack simultaneous excellence across measurement properties
2. Insufficient difficulty ceilings limit evaluation of advanced models
3. Widespread item saturation indicated by low Local Efficiency Headroom (LEH) scores
4. High guessing-rates suggest data contamination risks
5. Low feasibility in scientific benchmarks reveals design flaws

**Key methodological points:**
- Uses Four-Parameter Logistic (4PL) IRT model
- Trains on 41,871 items total
- Outperforms traditional IRT methods on prediction accuracy and rank stability
- Fisher information-based item selection produces better model rankings aligned with human preference

I can discuss the paper's findings, methodology, and implications in my own words, but cannot reproduce extended verbatim sections. Would a detailed summary or discussion of specific findings be helpful instead?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02e7e434-224e-48d5-907c-649e3dc7aee4",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "ad50cdb495cf40e2d",
  "type": "user",
  "uuid": "65acd569-18d7-4cf6-8ca1-3aa2e6b58223",
  "sourceToolAssistantUUID": "02e7e434-224e-48d5-907c-649e3dc7aee4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T16:39:40.036Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JKwXsdPNb51Beyjvi3f97k`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.15055",
  "prompt": "Extract the complete abstract and all metadata including authors, affiliations, submission date, keywords, and any visible text from this arXiv abstract page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65acd569-18d7-4cf6-8ca1-3aa2e6b58223",
  "isSidechain": true,
  "agentId": "ad50cdb495cf40e2d",
  "requestId": "req_011CbG3XXkoHwedHkbhF1e8P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86a8dff9-81a3-4632-9eea-7514ec55aa02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Wc9zGoGeWPcUBJg7dZUDvL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 356,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 25297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 762,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 19 · 2026-05-21T16:39:40.745Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UAZWuQ5dgabTYxBKraRa8L`</summary>

```json
{
  "url": "https://ojs.aaai.org/index.php/AAAI/article/view/40814",
  "prompt": "Extract the complete abstract, all visible text, keywords, and any section previews available on this AAAI proceedings page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86a8dff9-81a3-4632-9eea-7514ec55aa02",
  "isSidechain": true,
  "agentId": "ad50cdb495cf40e2d",
  "requestId": "req_011CbG3XXkoHwedHkbhF1e8P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a51b7ae-317b-462c-ac23-af64a298a462",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Wc9zGoGeWPcUBJg7dZUDvL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 356,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 25297,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 762
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 356,
          "output_tokens": 213,
          "cache_read_input_tokens": 25297,
          "cache_creation_input_tokens": 762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 762,
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

_source line 20 · 2026-05-21T16:39:44.785Z_

<details><summary>↩ Tool result · `toolu_01JKwXsdPNb51Beyjvi3f97k`</summary>

```text
# Paper Metadata Extraction

## Basic Information
- **arXiv ID:** 2505.15055
- **Title:** "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory"
- **Field:** Computer Science - Computation and Language (cs.CL)
- **Status:** Accepted to AAAI 2026 (Oral presentation)

## Authors
Hongli Zhou, Hui Huang, Ziqing Zhao, Lvyuan Han, Huicheng Wang, Kehai Chen, Muyun Yang, Wei Bao, Jian Dong, Bing Xu, Conghui Zhu, Hailong Cao, Tiejun Zhao

*Note: Specific affiliations are not listed on this abstract page.*

## Submission History
- **v1:** May 21, 2025
- **v2:** August 1, 2025
- **v3 (Current):** January 16, 2026

## Abstract Summary
The research addresses inconsistencies in LLM benchmark evaluations. The authors introduce PSN-IRT (Pseudo-Siamese Network for Item Response Theory), a framework for enhanced item parameter estimation. Their analysis of 41,871 items across 11 benchmarks reveals quality issues and demonstrates the potential to create smaller, more effective benchmarks aligned with human preferences.

## DOI
https://doi.org/10.48550/arXiv.2505.15055
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86a8dff9-81a3-4632-9eea-7514ec55aa02",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "ad50cdb495cf40e2d",
  "type": "user",
  "uuid": "0a658df0-2059-403a-be78-c03e7be67f5f",
  "sourceToolAssistantUUID": "86a8dff9-81a3-4632-9eea-7514ec55aa02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T16:39:47.054Z_

<details><summary>↩ Tool result · `toolu_01UAZWuQ5dgabTYxBKraRa8L`</summary>

```text
# Paper Summary: Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory

## Abstract
The authors address inconsistencies in LLM benchmark evaluations and poor model separability. They introduce "Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture."

The research analyzes 11 benchmarks with 41,871 items, revealing measurement quality deficiencies. The work demonstrates that PSN-IRT enables construction of smaller, more effective benchmarks with improved alignment to human preferences.

## Author Information
**Affiliated Institution:** Harbin Institute of Technology (primary), with contributions from China Electronics Standardization Institute

**Lead Authors:** Hongli Zhou, Hui Huang, Ziqing Zhao, and collaborators

## Publication Details
- **Venue:** AAAI-26 Technical Track on Natural Language Processing VI
- **Volume:** 40, Issue 41
- **Publication Date:** March 14, 2026
- **DOI:** https://doi.org/10.1609/aaai.v40i41.40814
- **Page Range:** 35085–35093

## Available Resources
- Full PDF manuscript
- Video/Poster/Slides supplementary materials
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a51b7ae-317b-462c-ac23-af64a298a462",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "ad50cdb495cf40e2d",
  "type": "user",
  "uuid": "2c44c05f-94cd-4450-8c0d-0069bc29f60a",
  "sourceToolAssistantUUID": "3a51b7ae-317b-462c-ac23-af64a298a462",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T16:39:52.187Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NtgQs5dmccm5o3JJ6UpEnm`</summary>

```json
{
  "url": "https://ojs.aaai.org/index.php/AAAI/article/download/40814/44775",
  "prompt": "Extract ALL text from this paper PDF including:\n1. Complete abstract\n2. Full introduction section with all paragraphs\n3. Complete related work section\n4. Complete background on IRT\n5. Full method section (PSN-IRT architecture, training, formulas)\n6. Full experiment section (datasets table, baselines, metrics, all numerical results)\n7. All figure captions\n8. All table captions and table data with numbers\n9. Complete benchmark analysis findings (all 5 findings with exact numbers)\n10. Complete efficient benchmarking section\n11. Ablation study results with numbers\n12. Conclusion and limitations\nReturn all text verbatim, preserving numbers and structure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c44c05f-94cd-4450-8c0d-0069bc29f60a",
  "isSidechain": true,
  "agentId": "ad50cdb495cf40e2d",
  "requestId": "req_011CbG3YFZkDt3bT4f5sDaQ2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bfd13f6c-994e-489f-90d0-52b74c000055",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016uLLr5xLuHyMfC1yhohwUE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1279,
      "cache_read_input_tokens": 26059,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1279
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 250,
          "cache_read_input_tokens": 26059,
          "cache_creation_input_tokens": 1279,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1279,
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

_source line 23 · 2026-05-21T16:39:58.824Z_

<details><summary>↩ Tool result · `toolu_01NtgQs5dmccm5o3JJ6UpEnm`</summary>

```text
I appreciate you providing the content, but I need to be transparent: the document you've shared appears to be a PDF file encoded in binary/compressed format, not readable plain text. The content shows PDF structure markers (object definitions, stream data, compression metadata) rather than extractable text.

To help you effectively, I would need:

1. **A readable text version** of the paper (plain text, markdown, or properly extracted PDF text)
2. **Or the paper's title/authors** so I can reference it appropriately
3. **Or clarification** on what specific sections you need summarized

**What I can do once you provide readable content:**
- Summarize the abstract, introduction, and key methods
- Extract and explain numerical results from tables/experiments
- Discuss findings while respecting the 125-character quote limit
- Quote key passages with proper attribution

**I cannot:**
- Extract text from binary PDF data
- Reproduce full sections verbatim
- Bypass copyright protections on published material

Could you provide the paper in a format I can actually read? If this is your own work or a preprint, plain text or a properly extracted version would work perfectly.

[Binary content (application/pdf, 700.3KB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/webfetch-1779381593085-70n4tk.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfd13f6c-994e-489f-90d0-52b74c000055",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "ad50cdb495cf40e2d",
  "type": "user",
  "uuid": "3660c80f-8121-4150-afa0-0aaeffff53ce",
  "sourceToolAssistantUUID": "bfd13f6c-994e-489f-90d0-52b74c000055",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-21T16:40:00.675Z_

The PDF was downloaded locally. Let me read it directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3660c80f-8121-4150-afa0-0aaeffff53ce",
  "isSidechain": true,
  "agentId": "ad50cdb495cf40e2d",
  "requestId": "req_011CbG3Z7v9J2W6oyzqAuP9a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "239904ce-feec-4334-81ce-c234700d748f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01L2mWmwRopPk8CMgWQUnP4c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 635,
      "cache_read_input_tokens": 27338,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 635,
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

_source line 25 · 2026-05-21T16:40:01.596Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Y5fmDh9cd2poha4ssRduPK`</summary>

```json
{
  "command": "ls /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/",
  "description": "List downloaded PDF file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "239904ce-feec-4334-81ce-c234700d748f",
  "isSidechain": true,
  "agentId": "ad50cdb495cf40e2d",
  "requestId": "req_011CbG3Z7v9J2W6oyzqAuP9a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "343a1338-2568-4877-9751-b77a7050fffd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01L2mWmwRopPk8CMgWQUnP4c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 635,
      "cache_read_input_tokens": 27338,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 635
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 27338,
          "cache_creation_input_tokens": 635,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 635,
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

_source line 26 · 2026-05-21T16:40:01.688Z_

<details><summary>↩ Tool result · `toolu_01Y5fmDh9cd2poha4ssRduPK`</summary>

```text
webfetch-1779381491497-bzue2k.pdf
webfetch-1779381520695-2q52tb.pdf
webfetch-1779381520903-z41iar.pdf
webfetch-1779381574471-asmire.pdf
webfetch-1779381577805-diiyry.pdf
webfetch-1779381593085-70n4tk.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "343a1338-2568-4877-9751-b77a7050fffd",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "ad50cdb495cf40e2d",
  "type": "user",
  "uuid": "1f9e6fdf-e520-47fa-97d4-2460a3f1cbe3",
  "sourceToolAssistantUUID": "343a1338-2568-4877-9751-b77a7050fffd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T16:40:03.983Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MHrhb3sGPVeGtNgN3BYu61`</summary>

```json
{
  "command": "pdftotext /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/webfetch-1779381593085-70n4tk.pdf - 2>/dev/null | head -300",
  "description": "Extract text from the PDF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f9e6fdf-e520-47fa-97d4-2460a3f1cbe3",
  "isSidechain": true,
  "agentId": "ad50cdb495cf40e2d",
  "requestId": "req_011CbG3ZL9MQttj6ZafmEZ8L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c640d68-6fc2-4a19-bb41-dc605018d292",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UYE8azWrGXWMzZMcb5QzAN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 278,
      "cache_read_input_tokens": 27973,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 278
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 27973,
          "cache_creation_input_tokens": 278,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 278,
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

_source line 28 · 2026-05-21T16:40:04.119Z_

<details><summary>↩ Tool result · `toolu_01MHrhb3sGPVeGtNgN3BYu61`</summary>

```text
The Fortieth AAAI Conference on Artificial Intelligence (AAAI-26)

Lost in Benchmarks? Rethinking Large Language Model Benchmarking with
Item Response Theory
Hongli Zhou1 * , Hui Huang1 * , Ziqing Zhao1 , Lvyuan Han1 , Huicheng Wang1 ,
Kehai Chen2 , Muyun Yang1† , Wei Bao3† , Jian Dong3† , Bing Xu1 ,
Conghui Zhu1 , Hailong Cao1 , Tiejun Zhao1
1

2

Faculty of Computing, Harbin Institute of Technology, Harbin, China
School of Computer Science and Technology, Harbin Institute of Technology, Shenzhen, China
3
China Electronics Standardization Institute, Beijing, China
hongli.joe@stu.hit.edu.cn, yangmuyun@hit.edu.cn, {baowei, dongjian}@cesi.cn
Abstract

The evaluation of large language models (LLMs) via benchmarks is widespread, yet inconsistencies between different
leaderboards and poor separability among top models raise
concerns about their ability to accurately reflect authentic
model capabilities. This paper provides a critical analysis of
benchmark effectiveness, examining mainstream prominent
LLM benchmarks using results from diverse models. We first
propose Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced Item Response Theory framework that incorporates a rich set of item parameters within
an IRT-grounded architecture. PSN-IRT can be utilized for
accurate and reliable estimations of item characteristics and
model abilities. Based on PSN-IRT, we conduct extensive
analysis on 11 LLM benchmarks comprising 41,871 items,
revealing significant and varied shortcomings in their measurement quality. Furthermore, we demonstrate that leveraging PSN-IRT is able to construct smaller benchmarks while
maintaining stronger alignment with human preference.

High Inconsistency

Code — https://github.com/Joe-Hall-Lee/PSN-IRT
Extended version — https://arxiv.org/abs/2505.15055

1

Low Separability

Figure 1: Illustration of weak separability and ranking inconsistencies in LLM benchmarks1 .

Introduction

As the scale and performance of large language models
(LLMs) continue to grow, accurately measuring their capabilities has become increasingly important (Chang et al.
2024; Zhou et al. 2024; Huang et al. 2025). Currently, the
performance of LLMs is primarily evaluated through various
benchmarks (Wang et al. 2024), which are comprehensive
test suites consisting of carefully designed questions to assess model behavior across different tasks. However, in practice, existing benchmarks often exhibit significant limitations, prompting consideration of their effectiveness (McIntosh et al. 2024).
As illustrated in Figure 1, on one hand, even benchmarks
that are designed to measure similar underlying capabili-

ties often produce inconsistent leaderboards, leading to substantial ranking variations for the same model (Perlitz et al.
2024). On the other hand, many benchmarks show weak separability among top models, limiting the ability to understand performance differences and further model refinement.
Given these limitations, there is a growing need for a more
systematic analysis of LLM benchmarks.
In this paper, we conduct a comprehensive analysis for various
popular LLM benchmark datasets. Our experiment is based on Item
Response Theory (IRT) (Lord, Novick, and Birnbaum 1968; Baker
and Kim 2004), a psychometric framework widely used in educational assessment to analyze item properties such as difficulty by
modeling item response against examinee ability2 . However, traditional IRT struggles with the complexity and scale of modern
datasets, and its assumption of the normal distribution of abilities

* These authors contributed equally.
†

Corresponding authors.
Copyright © 2026, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.

1
2

35085

https://opencompass.org.cn
In the paper, an item refers to a benchmark sample.

modern datasets and its assumption of normally distributed abilities, the application of IRT on LLM benchmarks is still underexplored (Ye et al. 2025).

does not always hold.
To advance our objective, we propose the Pseudo-Siamese Network for IRT (PSN-IRT), a framework for comprehensive and interpretable analysis of benchmark test sets. PSN-IRT processes
model identifiers and item identifiers through independent neural network pathways. These pathways respectively estimate latent
model ability and a rich set of item parameters. The estimated properties are then integrated using an IRT-based formulation to predict
outcome probabilities. This architectural design ensures both powerful modeling capabilities and strong theoretical interpretability.
To validate the effectiveness of PSN-IRT, we conduct extensive experiments on evaluation results from 12 LLMs across 11
benchmarks. Our results show that PSN-IRT outperforms previous
approaches in both parameter estimation accuracy and reliability.
Based on PSN-IRT, we perform in-depth analyses of these benchmarks using key metrics, with main findings as follows:

2.2

1. LLM benchmarks fail to achieve simultaneous excellence
across multiple measurements.
2. LLM benchmarks suffer from widespread saturation and insufficient difficulty ceilings, limiting their ability to challenge and
accurately evaluate advanced models.
3. LLM benchmarks exhibit data contamination in numerous
items, compromising their reliability.

1
(1)
1 + e−(θ−b)
where b denotes item difficulty. When θ = b, the probability of the
examinee generating a correct response is 0.5. The 1PL assumes
all items have equal discriminability, a simplification that may not
hold in complex testing scenarios.
More advanced IRT models introduce additional parameters to
capture diverse item properties. However, traditional IRT often suffer from inaccurate parameter estimation and rely on assumptions
like normal ability distributions, which may not align with realworld data (Tsutsumi, Kinoshita, and Ueno 2021).
P (X = 1 | θ) =

Furthermore, we find that model rankings derived from highquality datasets selected by PSN-IRT are more consistent with human preference and offer stronger discriminability among top models.
Our contributions are summarized as follows:
1. We propose PSN-IRT, a benchmark analysis framework with
superior estimation accuracy and reliability.
2. We use PSN-IRT for an in-depth analysis of mainstream benchmarks and find that current LLM benchmarks present deficiencies in many aspects.
3. We show that selecting items with PSN-IRT leads to model
rankings that better align with human preference.

2
2.1

Preliminary: Item Response Theory

Item Response Theory (IRT) (Lord, Novick, and Birnbaum 1968)
is a psychometric framework widely used in educational and
cognitive assessments to model the relationship between benchmark items and examinee abilities. Unlike Classical Test Theory
(CTT) (DeVellis 2006), which relies on aggregate test scores, IRT
analyzes individual item responses as a function of a latent ability
θ, enabling precise measurement of both item and examinee properties.
Central to IRT is the Item Characteristic Curve (ICC), a mathematical function that describes the probability of a correct response, P (X = 1 | θ), as a function of ability θ. Typically logistic, the ICC visualizes how item properties influence performance,
serving as the foundation for IRT.
The simplest IRT model, the One-Parameter Logistic (1PL)
model, defines the ICC as:

3

Pseudo-Siamese Network for IRT

In this section, we propose the Pseudo-Siamese Network for IRT
(PSN-IRT), designed to diagnose benchmark item quality by analyzing LLM responses. Specifically, one property can be inferred
for each model: model-ability, and four properties can be inferred
for each benchmark item: discriminability, difficulty, guessing-rate
and feasibility.

Background

Related Work

Model Architecture. The PSN-IRT architecture comprises

Researchers have explored various methods to evaluate and analyze
the quality of LLM benchmarks. Recent efforts have introduced
quantitative metrics that operate at a holistic, dataset level. For example, Benchmark Agreement Testing (BAT) assesses benchmark
reliability by comparing the consistency of model rankings across
different leaderboards (Perlitz et al. 2024; White et al. 2025). Other
novel metrics have also been proposed for more nuanced datasetlevel analysis (Li et al. 2024). Delving deeper than macro-level
comparisons, another significant line of work focuses on contentbased analysis to ground evaluation in concrete capabilities. For
instance, ADeLe (Zhou et al. 2025) leverages scalable cognitive
rubrics and item demand features to build highly interpretable capability profiles for AI systems.
Item Response Theory (IRT) (Lord, Novick, and Birnbaum
1968; Baker and Kim 2004) offers a psychometric framework for
data-driven, item-level analysis. Within natural language processing (NLP), IRT has been primarily utilized to diagnose fundamental item properties such as difficulty and discriminability (Vania
et al. 2021; Byrd and Srivastava 2022). More recently, its principles
have also been used to inspire methods for improving evaluation efficiency, for instance, through optimized item selection (Maia Polo
et al. 2024) or adaptive testing paradigms (Zhuang et al. 2025;
Truong et al. 2025). However, due to the complexity and scale of

two independent networks: a model network and an item network.
The model network processes one-hot encoded LLM identifiers to
estimate model-ability θ, while the item network handles one-hot
encoded item identifiers to produce the four IRT parameters: discriminability a, difficulty b, guessing-rate c, and feasibility d.
Each network consists of three fully connected layers with
ReLU activation functions, enabling efficient and stable parameter estimation. After that, these estimated properties are then processed by a Logistic Calculation Layer. This layer operates using
the Four-Parameter Logistic (4PL) model, an advanced IRT formulation that extends simpler models like the 1PL to capture nuanced
behaviors:
1
(2)
1 + e−a(θ−b)
where each parameter controls a different aspect of benchmark
item behavior:
P (X = 1 | θ) = c + (d − c) ·

• The difficulty b determines the ability level where the probability
changes most significantly.
• The discriminability a reflects an item’s power to differentiate
between models of varying abilities.

35086

Stage1: Training
Ground Truth Label
1 plus 1 is 2.

1

Model Network

What is 1 plus 1?

…

0
…

…

LLM

0

…

One-hot

𝑦=1

0

𝒅−𝒄
𝒄+
𝟏 + 𝒆−𝒂 𝜽−𝒃
IRT

1

What is 1 plus 1?

0

𝑦ො

𝑦

𝑵

…

0

Item Network

…

…

…

Item

One-hot

0

Cross
Entropy

𝑱 𝜽 =−

𝟏
෍ൣ𝒚𝒊 log 𝑷𝒊 + 𝟏 − 𝒚𝒊 log 𝟏 − 𝑷𝒊
𝑵
𝒊=𝟏

Stage2: Application
Item Characteristic Curve

Model Ability

Weak LLM

Strong LLM

Model
Network

model-ability

Model
Network

model-ability

Item Parameters
Calculate…
Item
Answer…

Item
What is …
Item
Prove…

Item

Item
Network
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c640d68-6fc2-4a19-bb41-dc605018d292",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "ad50cdb495cf40e2d",
  "type": "user",
  "uuid": "8a9ca6db-902c-460f-9e70-faa90ce4ed56",
  "sourceToolAssistantUUID": "8c640d68-6fc2-4a19-bb41-dc605018d292",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T16:40:10.810Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WR8xmBMygbhibBHDAHVhUF`</summary>

```json
{
  "command": "pdftotext /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/webfetch-1779381593085-70n4tk.pdf - 2>/dev/null | tail -n +300",
  "description": "Extract remaining text from PDF after line 300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a9ca6db-902c-460f-9e70-faa90ce4ed56",
  "isSidechain": true,
  "agentId": "ad50cdb495cf40e2d",
  "requestId": "req_011CbG3ZWWh6ujobUKMqA6vJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87a0418a-1a6b-4e0b-8a73-e83219383a02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TPzKZoSv8tNysHUBEtvKhm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3059,
      "cache_read_input_tokens": 28251,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3059
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 28251,
          "cache_creation_input_tokens": 3059,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3059,
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

_source line 30 · 2026-05-21T16:40:11.405Z_

<details><summary>↩ Tool result · `toolu_01WR8xmBMygbhibBHDAHVhUF`</summary>

```text
&lt;persisted-output>
Output too large (32KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/bjs7c213b.txt

Preview (first 2KB):
difficulty

Item
Network

discriminability

Item
Network

guessing-rate

Item
Network

feasibility

LEH
Fisher information
difficulty
Fisher

discriminability

LEH

guessing-rate

feasibility
Benchmark Quality Measurements

Figure 2: The illustration of our proposed PSN-IRT. Separate neural networks estimate model-ability (θ) and item parameters
(a, b, c, d), which are then combined via the IRT formula to predict the probability of a correct response. After that, the networks
can be leveraged for estimating properties for models or items, respectively.
• The guessing-rate c captures how likely models are to succeed
without full understanding.
• The feasibility d represents the maximum probability that even
highly proficient models will correctly answer the item.

fiers through their respective network pathways. For each pair, the
PSN-IRT framework first internally estimates the specific model
and item properties. These estimated properties are then passed to
a Logistic Calculation Layer, with the training objective as follows:
N

Notably, PSN-IRT follows standard IRT assumptions such as
unidimensionality and monotonicity, which generally hold for
LLM benchmarking (Kipnis et al. 2025; Truong et al. 2025).

J(θ) = −

1 X
[yi log(Pi ) + (1 − yi ) log(1 − Pi )]
N i=1

(3)

where N is the batch size. The training objective is to minimize the
discrepancy between the model’s prediction and the observed binary outcomes. Consequently, all learnable weights within both the
model and item networks are updated simultaneously, concurrently
optimizing the estimated properties for both models and benchmark items.

Training and Applications. The PSN-IRT is trained end-toend using the observed binary response data in the form of (Model,
Item, Response, Outcome), where the binary outcome indicates the
correctness of each LLM on each benchmark item. During training, PSN-IRT processes encoded pairs of LLM and item identi-

35087

4.2

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87a0418a-1a6b-4e0b-8a73-e83219383a02",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "ad50cdb495cf40e2d",
  "type": "user",
  "uuid": "fe26d589-b804-4456-9566-f83caf7c0d69",
  "sourceToolAssistantUUID": "87a0418a-1a6b-4e0b-8a73-e83219383a02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T16:40:13.397Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R6VParnrEz1dXcKHPckEdZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/bjs7c213b.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe26d589-b804-4456-9566-f83caf7c0d69",
  "isSidechain": true,
  "agentId": "ad50cdb495cf40e2d",
  "requestId": "req_011CbG3a3gBmGC4A6uxZNHjv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d05b10b2-f2e8-4d76-abff-5c1515f75409",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01V2HHBrUKf8THYLphXtkWbb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 816,
      "cache_read_input_tokens": 31310,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 816
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 31310,
          "cache_creation_input_tokens": 816,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 816,
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

_source line 32 · 2026-05-21T16:40:13.771Z_

<details><summary>↩ Tool result · `toolu_01R6VParnrEz1dXcKHPckEdZ`</summary>

```text
1	
2	difficulty
3	
4	Item
5	Network
6	
7	discriminability
8	
9	Item
10	Network
11	
12	guessing-rate
13	
14	Item
15	Network
16	
17	feasibility
18	
19	LEH
20	Fisher information
21	difficulty
22	Fisher
23	
24	discriminability
25	
26	LEH
27	
28	guessing-rate
29	
30	feasibility
31	Benchmark Quality Measurements
32	
33	Figure 2: The illustration of our proposed PSN-IRT. Separate neural networks estimate model-ability (θ) and item parameters
34	(a, b, c, d), which are then combined via the IRT formula to predict the probability of a correct response. After that, the networks
35	can be leveraged for estimating properties for models or items, respectively.
36	• The guessing-rate c captures how likely models are to succeed
37	without full understanding.
38	• The feasibility d represents the maximum probability that even
39	highly proficient models will correctly answer the item.
40	
41	fiers through their respective network pathways. For each pair, the
42	PSN-IRT framework first internally estimates the specific model
43	and item properties. These estimated properties are then passed to
44	a Logistic Calculation Layer, with the training objective as follows:
45	N
46	
47	Notably, PSN-IRT follows standard IRT assumptions such as
48	unidimensionality and monotonicity, which generally hold for
49	LLM benchmarking (Kipnis et al. 2025; Truong et al. 2025).
50	
51	J(θ) = −
52	
53	1 X
54	[yi log(Pi ) + (1 − yi ) log(1 − Pi )]
55	N i=1
56	
57	(3)
58	
59	where N is the batch size. The training objective is to minimize the
60	discrepancy between the model’s prediction and the observed binary outcomes. Consequently, all learnable weights within both the
61	model and item networks are updated simultaneously, concurrently
62	optimizing the estimated properties for both models and benchmark items.
63	
64	Training and Applications. The PSN-IRT is trained end-toend using the observed binary response data in the form of (Model,
65	Item, Response, Outcome), where the binary outcome indicates the
66	correctness of each LLM on each benchmark item. During training, PSN-IRT processes encoded pairs of LLM and item identi-
67	
68	35087
69	
70	4.2
71	
72	Upon completion of training, the two networks of PSN-IRT can
73	be used for evaluating model performance and diagnosing benchmark characteristics, respectively. Specifically, the model network,
74	by processing a model’s encoding, outputs an estimate of the
75	model-ability θ. Meanwhile, the item network, given a benchmark
76	item’s encoding, outputs its four estimated psychometric parameters a, b, c, d, which can be used for an in-depth diagnosis of individual item characteristics and the overall benchmark quality.
77	
78	4
79	4.1
80	
81	Main Results
82	
83	Table 2 shows the estimation accuracy and reliability of PSN-IRT
84	compared to traditional IRT and Deep-IRT. Both Deep-IRT and
85	PSN-IRT significantly outperform traditional IRT in prediction accuracy. Despite its simpler Logistic output layer rooted in the IRT
86	formula, PSN-IRT attains prediction accuracy on par with the more
87	complex Deep-IRT, and surpasses it in rank reliability.
88	Given our goal to comprehensively capture diverse item characteristics, we adopt the more expressive 4PL structure for all methods except Deep-IRT. Experiments also confirm that PSN-IRT performs best with 4PL.
89	
90	Efficacy of PSN-IRT
91	
92	Experimental Setup
93	
94	Datasets. To evaluate existing LLM benchmarks, we select 11
95	
96	4.3
97	
98	datasets that vary in domain coverage. They serve as a basis for
99	comparing different IRT-based methods and analyzing test set
100	properties. An overview of the datasets is provided in Table 1.
101	To construct training data, we conduct evaluations using OpenCompass (Contributors 2023). The evaluation results are collected
102	in the form of binary outcomes, indicating whether each model
103	answered each item correctly. Then, we construct a unified outcome matrix by aggregating item-level results across all models
104	and benchmarks. We split the interactions into training, validation,
105	and test sets.
106	We mainly focus on currently high-performing models, including 360GPT2-Pro3 , DeepSeek-V34 , Doubao-pro5 , Gemini-1.56 ,
107	Hunyuan-Turbo7 , Moonshot-v18 , Qwen-Plus9 , and Yi-Lightning10 .
108	However, testing only strong models might obscure differences in
109	the discriminability of the test sets, as most items could be solved
110	easily, thus limiting a comprehensive evaluation of test set quality
111	(Martı́nez-Plumed et al. 2019). To address this, we intentionally
112	included several relatively weaker models, including Gemma-2Bit, Mistral-7B-Instruct-v0.1, Qwen2.5-3B-Instruct, and Vicuna-7Bv1.3 (Chiang et al. 2023).
113	
114	To assess whether more complex architectures offer benefits over
115	our straightforward design, we conduct an ablation study. Specifically, we compare PSN-IRT with two variants: one replaces onehot inputs with semantic embeddings from Instructor (Su et al.
116	2023), and the other uses a GNN (Su et al. 2022) instead of the
117	MLP backbone.
118	As shown in Table 3, both alternatives underperform our original
119	design. We argue that semantic similarity between item texts does
120	not necessarily reflect similarity in measurement characteristics.
121	For the GNN variant, its neighborhood aggregation mechanism
122	risks diluting the unique statistical signals of individual models
123	and items, thereby hindering precise parameter estimation. These
124	results suggest that in this estimation scenario, preserving the individuality of models and items is more effective than introducing
125	architectural complexity.
126	Furthermore, since PSN-IRT estimates parameters that are specific to the training data, requiring retraining to analyze new items,
127	we also investigate the stability of these estimates when the item
128	pool changes. To simulate this, we conduct an experiment by independently training separate PSN-IRT models on random subsets
129	of the items. We then compute the Pearson correlation between the
130	item parameters estimated from these subsets and those estimated
131	from the full dataset.
132	As shown in Table 4, the results reveal a high degree of correlation across all parameters. This indicates that PSN-IRT learns
133	highly consistent intrinsic properties for the items regardless of the
134	specific data sample, demonstrating the stability of parameter estimation.
135	
136	Baselines. We mainly compare PSN-IRT with traditional IRT
137	methods, namely IRT estimated based on traditional parameter estimation techniques, including Maximum Likelihood Estimation
138	(MLE), Markov Chain Monte Carlo (MCMC) (Hastings 1970),
139	Variational Inference (VI) (Jordan et al. 1999), and VIBO (Wu et al.
140	2020). We also compare with Deep-IRT (Tsutsumi, Kinoshita, and
141	Ueno 2021), which is an extension of 1PL IRT that learns item-trait
142	interactions via deep networks.
143	
144	Ablation Study
145	
146	5
147	
148	Metrics. To assess whether the learned parameters meaning-
149	
150	5.1
151	
152	fully reflect corresponding properties, we use two quantitative metrics:
153	
154	Benchmark Analysis with PSN-IRT
155	
156	Benchmark Quality Measurements
157	
158	In this section, we delve into a detailed analysis of the benchmarks
159	based on different measurements. Specifically, we leverage the 4
160	item parameters (difficulty, discriminability, guessing-rate and feasibility) estimated by PSN-IRT, along with two additional metrics
161	for evaluating item quality: Local Efficiency Headroom (LEH) (Vania et al. 2021) and Fisher information (Lord 1980).
162	LEH score assesses the potential of a test example to evaluate
163	future progress in LLMs. It is calculated as the derivative of the
164	item’s Item Characteristic Curve (ICC) with respect to the highest
165	observed latent ability. A high LEH score indicates that even the
166	top model remains far from the saturation point of the ICC.
167	Fisher information measures the amount of information an item
168	provides about a model’s ability level. Items with higher Fisher
169	information are more informative for estimating model abilities.
170	For 4PL IRT, it is defined as:
171	
172	• Prediction accuracy: Following standard practice in educational
173	testing (Eignor 2013), we assess how well a method predicts
174	whether a model answers an item correctly, reporting accuracy,
175	F1 score, and ROC AUC.
176	• Rank stability: To evaluate the reliability of model ranking induced by each method, we split the test set into two subsets, estimate model abilities separately, and compute Kendall’s τ between the resulting rankings.
177	3
178	
179	https://ai.360.cn/
180	https://platform.deepseek.com/
181	5
182	https://www.volcengine.com/product/doubao
183	6
184	https://ai.google.dev/
185	7
186	https://hunyuan.tencent.com/
187	8
188	https://platform.moonshot.cn/
189	9
190	https://qwen.ai/apiplatform
191	10
192	https://platform.lingyiwanwu.com/
193	4
194	
195	I(θ) =
196	
197	a2 (P (θ) − c)2 (d − P (θ))2
198	,
199	(d − c)2 P (θ)(1 − P (θ))
200	
201	where P (θ) is defined as Equation 2.
202	
203	35088
204	
205	(4)
206	
207	Benchmark
208	ARC-C (Clark et al. 2018)
209	BBH (Suzgun et al. 2023)
210	Chinese SimpleQA (He et al. 2024)
211	GPQA Diamond (Rein et al. 2024)
212	GSM8K (Cobbe et al. 2021)
213	HellaSwag (Zellers et al. 2019)
214	HumanEval (Chen et al. 2021)
215	MATH (Hendrycks et al. 2021b)
216	MBPP (Austin et al. 2021)
217	MMLU (Hendrycks et al. 2021a)
218	TheoremQA (Chen et al. 2023)
219	
220	Data Size
221	295
222	6,511
223	3,000
224	198
225	1,319
226	10,042
227	164
228	5,000
229	500
230	14,042
231	800
232	
233	Domain
234	General
235	General
236	Knowledge
237	Science
238	Math
239	General
240	Code
241	Math
242	Code
243	General
244	Science
245	
246	Metric
247	EM
248	EM
249	LLM-as-a-Judge
250	EM
251	EM
252	EM
253	Pass@1
254	EM
255	Pass@1
256	EM
257	EM
258	
259	Format
260	Multiple Choice
261	Mixed
262	QA
263	Multiple Choice
264	QA
265	Multiple Choice
266	QA
267	QA
268	QA
269	Multiple Choice
270	QA
271	
272	Table 1: Benchmarks used in this paper.
273	Model
274	
275	Parameter
276	
277	IRT
278	
279	4PL
280	
281	Deep-IRT
282	PSN-IRT
283	
284	1PL
285	4PL
286	
287	Method
288	MLE
289	MCMC
290	VI
291	VIBO
292	Deep Learning
293	Deep Learning
294	
295	ACC
296	0.7211
297	0.7070
298	0.7201
299	0.7188
300	0.7974
301	0.7998
302	
303	F1
304	0.8034
305	0.7811
306	0.8015
307	0.8007
308	0.8516
309	0.8538
310	
311	AUC
312	0.7012
313	0.7278
314	0.6940
315	0.7055
316	0.8519
317	0.8485
318	
319	Kendall’s τ
320	0.9697
321	0.9697
322	0.9091
323	0.9697
324	0.9697
325	1.0000
326	
327	Table 2: Comparison of prediction accuracy and rank reliability across different methods.
328	Method
329	PSN-IRT
330	+ Embedding
331	+ GNN
332	
333	ACC
334	0.7998
335	0.7808
336	0.7928
337	
338	F1
339	0.8538
340	0.8413
341	0.8490
342	
343	AUC
344	0.8485
345	0.8310
346	0.8197
347	
348	Kendall
349	1.0000
350	0.9394
351	0.7273
352	
353	being offset by significant weaknesses is common across benchmarks, which underscores the inherent challenges and trade-offs in
354	benchmark design. Moreover, the property distributions visualized
355	in Figure 3 further highlight this variability and the difficulty for
356	any single benchmark to achieve balanced, high quality across all
357	desired measurement properties.
358	
359	Table 3: Ablation study on PSN-IRT’s input representation
360	and network architecture.
361	Data
362	30%
363	50%
364	70%
365	
366	Difficulty
367	0.9009
368	0.7437
369	0.9519
370	
371	Discrim.
372	0.8186
373	0.7835
374	0.7414
375	
376	Guessing
377	0.8274
378	0.8776
379	0.8320
380	
381	Finding 2: Current LLM benchmarks exhibit an insufficient difficulty ceiling to challenge the most advanced
382	models. As shown in Table 5, difficulty is varied among dif-
383	
384	Feasibility
385	0.9025
386	0.9330
387	0.9442
388	
389	ferent benchmarks. Datasets such as TheoremQA, Chinese SimpleQA, and GPQA Diamond lead in difficulty and continue to
390	challenge many LLMs. In contrast, other benchmarks including
391	ARC-C, HellaSwag, and MMLU have become comparatively easy,
392	where many of the items are readily solved by high-performing
393	models, diminishing their utility for differentiating top-tier systems.
394	Crucially, as shown in Figure 3, even the most challenging items
395	in existing benchmarks exhibit relatively low difficulty levels. For
396	instance, on the IRT scale, the highest item difficulty values rarely
397	exceed 1.0, while top models such as DeepSeek-V3 have estimated
398	abilities well above 3.0. This indicates that even the hardest questions are significantly below the capability level of elite LLMs,
399	highlighting a lack of sufficient challenge for frontier capabilities.
400	
401	Table 4: Pearson correlation coefficients of item parameters
402	estimated on random subsets of the data versus those estimated on the full dataset. All correlations are statistically
403	significant (p < 0.0001).
404	
405	5.2
406	
407	Benchmark Analysis
408	
409	Based on the measurements, we provide an aggregate rank for each
410	benchmark, calculated from the sum of individual ranks in Table 5,
411	where a lower total rank value indicates better overall quality. Additionally, Figure 3 visualizes the distribution of item-level properties across the 11 LLM benchmarks. Building on these experimental results, our detailed analysis is presented as follows.
412	
413	Finding 3: Generally low LEH scores across most benchmarks reveal widespread item saturation. While Table 5
414	indicates that datasets like GPQA Diamond and TheoremQA
415	achieve the highest relative ranks for average LEH, suggesting they
416	offer more headroom than other benchmarks, the absolute LEH
417	values in Figure 3 are often smaller than ideal. Conversely, benchmarks such as GSM8K and ARC-C exhibit lower average LEH
418	scores. This signifies that current high-performing models are already approaching or have reached the performance ceiling for a
419	substantial portion of items within these test sets. This necessitates
420	the development of new benchmark items and datasets explicitly
421	designed with greater headroom as models continue to evolve.
422	
423	Finding 1: LLM benchmarks fail to achieve simultaneous excellence across multiple measurement properties.
424	As shown in Table 5, the results clearly demonstrate this lack of
425	simultaneous excellence. While Chinese SimpleQA achieves the
426	best overall score, no benchmark performs universally well across
427	the individual metrics. For instance, Chinese SimpleQA itself suffers from poor feasibility with a rank of 9. This pattern of strengths
428	
429	35089
430	
431	Dataset
432	Chinese SimpleQA
433	TheoremQA
434	MBPP
435	MATH
436	GPQA Diamond
437	BBH
438	MMLU
439	GSM8K
440	HumanEval
441	HellaSwag
442	ARC-C
443	
444	Difficulty
445	2
446	1
447	5
448	4
449	3
450	6
451	9
452	8
453	7
454	10
455	11
456	
457	Discriminability
458	3
459	10
460	6
461	1
462	11
463	5
464	9
465	2
466	4
467	7
468	8
469	
470	Guessing
471	1
472	3
473	4
474	2
475	6
476	8
477	9
478	5
479	7
480	10
481	11
482	
483	Feasibility
484	9
485	11
486	8
487	7
488	10
489	6
490	5
491	3
492	4
493	2
494	1
495	
496	LEH
497	3
498	2
499	4
500	7
501	1
502	6
503	5
504	11
505	9
506	8
507	10
508	
509	Fisher
510	5
511	2
512	4
513	10
514	1
515	7
516	3
517	11
518	9
519	6
520	8
521	
522	Total
523	23
524	29
525	31
526	31
527	32
528	38
529	40
530	40
531	40
532	43
533	49
534	
535	Table 5: Ranks of datasets based on average item-level properties estimated by PSN-IRT. Each rank is obtained by averaging
536	the property over all items in a dataset and then sorting these averages; smaller rank values correspond to better performance.
537	Finding 4: Outlier-high guessing-rates in many benchmark items flag risks of data contamination. The
538	
539	Method
540	
541	guessing-rate reflects the chance that a model can answer a question correctly without actual understanding, typically by exploiting format-based cues or shortcuts. As shown in Figure 3, datasets
542	like ARC-C, HellaSwag, and MMLU generally present higher
543	guessing-rates, possibly due to their multiple-choice formats. Notably, further inspection of the item guessing-rate parameter distributions, as depicted in Figure 3, reveals that a considerable number of items across several benchmarks exhibit unusually high
544	guessing-rates. This observation regards the potential for such
545	items to indicate data contamination, namely the content or answers for these items might have been present in the models’ pretraining data (Zhuang et al. 2025).
546	
547	All
548	Top 400
549	Random
550	Clustering
551	Discrim.
552	Fisher
553	Top 1000
554	Random
555	Clustering
556	Discrim.
557	Fisher
558	
559	Finding 5: Widespread low-feasibility items in scientific
560	benchmarks reveal flawed question design. Feasibility es-
561	
562	0.0421
563	0.0308
564	0.1841
565	0.0049
566	
567	0.6444
568	0.6000
569	0.5556
570	0.6889
571	
572	0.0007
573	0.0058
574	0.0000
575	0.0033
576	
577	0.2381
578	0.1429
579	0.2381
580	0.7143
581	
582	0.0406
583	0.0166
584	0.1805
585	0.0039
586	
587	0.6444
588	0.6444
589	0.6000
590	0.6889
591	
592	0.0009
593	0.0041
594	0.0000
595	0.0030
596	
597	0.2381
598	0.2381
599	0.3813
600	0.9048
601	
602	Table 6: Variance and Kendall’s τ for various data selection
603	strategies with and without weak models.
604	
605	timates how well a question can be answered based on the information provided. Low feasibility often arises from underspecified
606	or overly broad questions, where even a strong model cannot determine a clear answer. As shown in Figure 3, datasets like TheoremQA and GPQA Diamond exhibit lower feasibility, likely due
607	to complex scientific contexts or vague problem descriptions. In
608	contrast, ARC-C and HellaSwag have high feasibility, suggesting
609	their questions are well-formed and specific. Low feasibility more
610	often reflects weaknesses in annotation quality or task design, and
611	such items can distort evaluation by penalizing models for failing
612	to resolve ambiguities (Rodriguez et al. 2021).
613	
614	6
615	
616	w/ weak models
617	w/o weak models
618	Variance Kendall Variance Kendall
619	0.0434
620	0.6444
621	0.0010
622	0.2381
623	
624	2024) and OpenCompass Arena (Contributors 2023)11 .
625	Subsequently, various subsets of benchmark items are chosen
626	based on different criteria. Model rankings generated using these
627	subsets are then compared against the reference arena ranking using Kendall’s τ to measure agreement. Alongside agreement, we
628	also consider the variance of model scores on these subsets; higher
629	variance generally indicates the subset’s capacity to differentiate
630	more clearly between models. The evaluations are conducted using two distinct model groupings: one set comprising a mix of
631	stronger and weaker models (”w/ weak models”), and another set
632	from which weaker models are excluded (”w/o weak models”),
633	to specifically assess separability among stronger contenders, with
634	weak models introduced in Section 4.1.
635	
636	Efficient Benchmarking with PSN-IRT
637	
638	While the pursuit of comprehensive LLM evaluation has led to increasingly large benchmarks, sheer item volume neither guarantees quality nor comes without significant computational cost. This
639	section, therefore, explores how PSN-IRT can facilitate more efficient benchmarking. We investigate whether strategically curating
640	smaller, highly informative item sets can yield model comparisons
641	that maintain or even surpass the accuracy and reliability of larger,
642	undifferentiated collections.
643	
644	Results. As shown in Table 6, selecting items based on Fisher
645	information consistently produces model rankings with superior
646	alignment to the reference arena ranking. For instance, a carefully
647	selected subset composed of just 1,000 items chosen via the Fisher
648	information criterion achieves a Kendall’s τ of up to 0.9048. This
649	level of agreement markedly surpasses that achieved by rankings
650	derived from using all available items or from similarly sized randomly selected subsets.
651	In contrast, other item selection approaches are less effective for
652	distinguishing strong models. For instance, selecting items based
653	
654	Experimental Setup. To evaluate the effectiveness of different item selection strategies, we design an experiment to evaluate
655	the effectiveness of different item selection strategies. Our methodology involves Benchmark Agreement Testing (BAT) (Perlitz et al.
656	2024). We first establish a reference model ranking by aggregating
657	results from two public leaderboards: Chatbot Arena (Chiang et al.
658	
659	11
660	These arenas are based on human evaluation and thus reflect
661	human preference regarding overall model capabilities.
662	
663	35090
664	
665	Difficulty
666	
667	Discriminability
668	
669	0.8
670	
671	Guessing Rate
672	
673	2.5
674	
675	0
676	−1
677	
678	0.6
679	
680	2.0
681	
682	Guessing Rate
683	
684	Discriminability
685	
686	Difficulty
687	
688	1
689	
690	1.5
691	1.0
692	
693	0.4
694	0.2
695	
696	0.5
697	
698	−2
699	
700	0.0
701	Feasibility
702	
703	0.0
704	LEH
705	
706	Fisher Information
707	
708	1.0
709	Fisher Information
710	
711	0.010
712	
713	0.4
714	
715	0.005
716	0.2
717	
718	R
719	ne
720	C
721	s
722	G e S B -C
723	PQ im B
724	A ple H
725	D Q
726	ia A
727	m
728	G on
729	H SM d
730	e
731	H llaS 8K
732	um w
733	an ag
734	E
735	M val
736	AT
737	M H
738	B
739	Th M PP
740	eo ML
741	re U
742	m
743	Q
744	A
745	
746	A
747	C
748	
749	Dataset
750	
751	0.001
752	
753	0.000
754	
755	C
756	
757	hi
758	
759	A
760	R
761	ne
762	C
763	se
764	G S B -C
765	PQ im B
766	A ple H
767	D Q
768	ia A
769	m
770	G on
771	H SM d
772	e
773	H llaS 8K
774	um w
775	an ag
776	E
777	M val
778	AT
779	M H
780	B
781	Th M PP
782	eo ML
783	re U
784	m
785	Q
786	A
787	hi
788	
789	C
790	
791	0.000
792	
793	0.002
794	
795	ne
796	C
797	s
798	G e S B -C
799	PQ im B
800	A ple H
801	D Q
802	ia A
803	m
804	G on
805	H SM d
806	e
807	H llaS 8K
808	um w
809	an ag
810	E
811	M val
812	AT
813	M H
814	B
815	Th M PP
816	eo ML
817	re U
818	m
819	Q
820	A
821	
822	0.015
823	
824	R
825	
826	0.6
827	
828	0.003
829	
830	A
831	
832	0.020
833	
834	hi
835	
836	0.8
837	LEH
838	
839	Feasibility
840	
841	0.025
842	
843	Dataset
844	
845	Dataset
846	
847	Figure 3: Distribution of item-level properties across 11 LLM benchmarks.
848	
849	References
850	
851	on discriminability yields zero score variance when weak models are excluded, indicating it merely separates broad capability
852	tiers rather than providing granularity among top-performers. Separately, clustering items based on their success/failure vectors (Pacchiardi, Cheke, and Hernández-Orallo 2024) also fails to improve
853	ranking correlation, even when it increases score separability.
854	
855	7
856	
857	Austin, J.; Odena, A.; Nye, M.; Bosma, M.; Michalewski, H.;
858	Dohan, D.; Jiang, E.; Cai, C.; Terry, M.; Le, Q.; and Sutton,
859	C. 2021. Program Synthesis with Large Language Models.
860	arXiv:2108.07732.
861	Baker, F. B.; and Kim, S.-H. 2004. Item response theory: Parameter estimation techniques. CRC press.
862	Byrd, M.; and Srivastava, S. 2022. Predicting Difficulty and
863	Discrimination of Natural Language Questions. In Muresan, S.;
864	Nakov, P.; and Villavicencio, A., eds., Proceedings of the 60th
865	Annual Meeting of the Association for Computational Linguistics
866	(Volume 2: Short Papers), 119–130. Dublin, Ireland: Association
867	for Computational Linguistics.
868	Chang, Y.; Wang, X.; Wang, J.; Wu, Y.; Yang, L.; Zhu, K.; Chen,
869	H.; Yi, X.; Wang, C.; Wang, Y.; Ye, W.; Zhang, Y.; Chang, Y.; Yu,
870	P. S.; Yang, Q.; and Xie, X. 2024. A Survey on Evaluation of Large
871	Language Models. ACM Trans. Intell. Syst. Technol., 15(3).
872	Chen, M.; Tworek, J.; Jun, H.; Yuan, Q.; de Oliveira Pinto, H. P.;
873	Kaplan, J.; Edwards, H.; Burda, Y.; Joseph, N.; Brockman, G.;
874	Ray, A.; Puri, R.; Krueger, G.; Petrov, M.; Khlaaf, H.; Sastry, G.;
875	Mishkin, P.; Chan, B.; Gray, S.; Ryder, N.; Pavlov, M.; Power,
876	A.; Kaiser, L.; Bavarian, M.; Winter, C.; Tillet, P.; Such, F. P.;
877	Cummings, D.; Plappert, M.; Chantzis, F.; Barnes, E.; HerbertVoss, A.; Guss, W. H.; Nichol, A.; Paino, A.; Tezak, N.; Tang, J.;
878	Babuschkin, I.; Balaji, S.; Jain, S.; Saunders, W.; Hesse, C.; Carr,
879	A. N.; Leike, J.; Achiam, J.; Misra, V.; Morikawa, E.; Radford,
880	A.; Knight, M.; Brundage, M.; Murati, M.; Mayer, K.; Welinder,
881	
882	Conclusion
883	
884	In this work, we introduce PSN-IRT, a framework that combines
885	psychometrics with neural networks to provide comprehensive and
886	reliable analyses of LLM benchmarks. Through extensive experiments on 12 LLMs across 11 diverse datasets, we demonstrate that
887	current benchmarks often suffer from uneven measurement properties, insufficient difficulty ceilings, item saturation, and data contamination. Moreover, we show that strategically selecting smaller,
888	high-quality item sets using PSN-IRT enhances alignment with human preference and separability among top models.
889	
890	Acknowledgments
891	This work is supported by National Natural Science Foundation
892	of China (62276077, 62376075, 62376076), Department of Science and Technology of Heilongjiang (Grant No. ZY04JD04), and
893	the Key Laboratory of Computing Power Network and Information
894	Security, Ministry of Education (Grant No. 2023ZD027).
895	
896	35091
897	
898	Kipnis, A.; Voudouris, K.; Buschoff, L. M. S.; and Schulz, E. 2025.
899	metabench - A Sparse Benchmark of Reasoning and Knowledge in
900	Large Language Models. In The Thirteenth International Conference on Learning Representations.
901	Li, T.; Chiang, W.-L.; Frick, E.; Dunlap, L.; Wu, T.; Zhu, B.; Gonzalez, J. E.; and Stoica, I. 2024. From Crowdsourced Data to HighQuality Benchmarks: Arena-Hard and BenchBuilder Pipeline.
902	arXiv preprint arXiv:2406.11939.
903	Lord, F.; Novick, M.; and Birnbaum, A. 1968. Statistical theories
904	of mental test scores.
905	Lord, F. M. 1980. Applications of Item Response Theory to Practical Testing Problems.
906	Maia Polo, F.; Weber, L.; Choshen, L.; Sun, Y.; Xu, G.; and
907	Yurochkin, M. 2024. tinyBenchmarks: evaluating LLMs with
908	fewer examples. In Salakhutdinov, R.; Kolter, Z.; Heller, K.;
909	Weller, A.; Oliver, N.; Scarlett, J.; and Berkenkamp, F., eds., Proceedings of the 41st International Conference on Machine Learning, volume 235 of Proceedings of Machine Learning Research,
910	34303–34326. PMLR.
911	Martı́nez-Plumed, F.; Prudêncio, R. B.; Martı́nez-Usó, A.; and
912	Hernández-Orallo, J. 2019. Item response theory in AI: Analysing
913	machine learning classifiers at the instance level. Artificial intelligence, 271: 18–42.
914	McIntosh, T. R.; Susnjak, T.; Arachchilage, N.; Liu, T.; Watters,
915	P.; and Halgamuge, M. N. 2024. Inadequacies of large language
916	model benchmarks in the era of generative artificial intelligence.
917	arXiv preprint arXiv:2402.09880.
918	Pacchiardi, L.; Cheke, L. G.; and Hernández-Orallo, J. 2024. 100
919	instances is all you need: predicting the success of a new LLM on
920	unseen data by testing on a few instances. arXiv:2409.03563.
921	Perlitz, Y.; Gera, A.; Arviv, O.; Yehudai, A.; Bandel, E.; Shnarch,
922	E.; Shmueli-Scheuer, M.; and Choshen, L. 2024. Do These LLM
923	Benchmarks Agree? Fixing Benchmark Evaluation with BenchBench. arXiv:2407.13696.
924	Rein, D.; Hou, B. L.; Stickland, A. C.; Petty, J.; Pang, R. Y.; Dirani,
925	J.; Michael, J.; and Bowman, S. R. 2024. GPQA: A Graduate-Level
926	Google-Proof Q&A Benchmark. In First Conference on Language
927	Modeling.
928	Rodriguez, P.; Barrow, J.; Hoyle, A. M.; Lalor, J. P.; Jia, R.; and
929	Boyd-Graber, J. 2021. Evaluation Examples are not Equally Informative: How should that change NLP Leaderboards? In Zong, C.;
930	Xia, F.; Li, W.; and Navigli, R., eds., Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and
931	the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), 4486–4503. Online: Association
932	for Computational Linguistics.
933	Su, H.; Shi, W.; Kasai, J.; Wang, Y.; Hu, Y.; Ostendorf, M.; Yih,
934	W.-t.; Smith, N. A.; Zettlemoyer, L.; and Yu, T. 2023. One Embedder, Any Task: Instruction-Finetuned Text Embeddings. In Rogers,
935	A.; Boyd-Graber, J.; and Okazaki, N., eds., Findings of the Association for Computational Linguistics: ACL 2023, 1102–1121.
936	Toronto, Canada: Association for Computational Linguistics.
937	Su, Y.; Cheng, Z.; Wu, J.; Dong, Y.; Huang, Z.; Wu, L.; Chen,
938	E.; Wang, S.; and Xie, F. 2022. Graph-based cognitive diagnosis
939	for intelligent tutoring systems. Knowledge-Based Systems, 253:
940	109547.
941	Suzgun, M.; Scales, N.; Schärli, N.; Gehrmann, S.; Tay, Y.; Chung,
942	H. W.; Chowdhery, A.; Le, Q.; Chi, E.; Zhou, D.; and Wei, J.
943	2023. Challenging BIG-Bench Tasks and Whether Chain-ofThought Can Solve Them. In Rogers, A.; Boyd-Graber, J.; and
944	Okazaki, N., eds., Findings of the Association for Computational
945	
946	P.; McGrew, B.; Amodei, D.; McCandlish, S.; Sutskever, I.; and
947	Zaremba, W. 2021. Evaluating Large Language Models Trained
948	on Code.
949	Chen, W.; Yin, M.; Ku, M.; Lu, P.; Wan, Y.; Ma, X.; Xu, J.; Wang,
950	X.; and Xia, T. 2023. TheoremQA: A Theorem-driven Question
951	Answering Dataset. In Bouamor, H.; Pino, J.; and Bali, K., eds.,
952	Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, 7889–7901. Singapore: Association for
953	Computational Linguistics.
954	Chiang, W.-L.; Li, Z.; Lin, Z.; Sheng, Y.; Wu, Z.; Zhang, H.; Zheng,
955	L.; Zhuang, S.; Zhuang, Y.; Gonzalez, J. E.; Stoica, I.; and Xing,
956	E. P. 2023. Vicuna: An Open-Source Chatbot Impressing GPT-4
957	with 90%* ChatGPT Quality.
958	Chiang, W.-L.; Zheng, L.; Sheng, Y.; Angelopoulos, A. N.; Li, T.;
959	Li, D.; Zhu, B.; Zhang, H.; Jordan, M.; Gonzalez, J. E.; and Stoica,
960	I. 2024. Chatbot Arena: An Open Platform for Evaluating LLMs
961	by Human Preference. In Salakhutdinov, R.; Kolter, Z.; Heller, K.;
962	Weller, A.; Oliver, N.; Scarlett, J.; and Berkenkamp, F., eds., Proceedings of the 41st International Conference on Machine Learning, volume 235 of Proceedings of Machine Learning Research,
963	8359–8388. PMLR.
964	Clark, P.; Cowhey, I.; Etzioni, O.; Khot, T.; Sabharwal, A.;
965	Schoenick, C.; and Tafjord, O. 2018. Think you have Solved
966	Question Answering? Try ARC, the AI2 Reasoning Challenge.
967	arXiv:1803.05457v1.
968	Cobbe, K.; Kosaraju, V.; Bavarian, M.; Chen, M.; Jun, H.; Kaiser,
969	L.; Plappert, M.; Tworek, J.; Hilton, J.; Nakano, R.; Hesse, C.; and
970	Schulman, J. 2021. Training Verifiers to Solve Math Word Problems. arXiv preprint arXiv:2110.14168.
971	Contributors, O. 2023. OpenCompass: A Universal Evaluation Platform for Foundation Models. https://github.com/opencompass/opencompass.
972	DeVellis, R. F. 2006. Classical test theory. Medical care, 44(11):
973	S50–S59.
974	Eignor, D. R. 2013. The standards for educational and psychological testing.
975	Hastings, W. K. 1970. Monte Carlo sampling methods using
976	Markov chains and their applications.
977	He, Y.; Li, S.; Liu, J.; Tan, Y.; Wang, W.; Huang, H.; Bu, X.;
978	Guo, H.; Hu, C.; Zheng, B.; Lin, Z.; Liu, X.; Sun, D.; Lin, S.;
979	Zheng, Z.; Zhu, X.; Su, W.; and Zheng, B. 2024. Chinese SimpleQA: A Chinese Factuality Evaluation for Large Language Models. arXiv:2411.07140.
980	Hendrycks, D.; Burns, C.; Basart, S.; Zou, A.; Mazeika, M.; Song,
981	D.; and Steinhardt, J. 2021a. Measuring Massive Multitask Language Understanding. Proceedings of the International Conference
982	on Learning Representations (ICLR).
983	Hendrycks, D.; Burns, C.; Kadavath, S.; Arora, A.; Basart, S.;
984	Tang, E.; Song, D.; and Steinhardt, J. 2021b. Measuring Mathematical Problem Solving With the MATH Dataset. NeurIPS.
985	Huang, H.; Bu, X.; Zhou, H.; Qu, Y.; Liu, J.; Yang, M.; Xu, B.; and
986	Zhao, T. 2025. An Empirical Study of LLM-as-a-Judge for LLM
987	Evaluation: Fine-tuned Judge Model is not a General Substitute for
988	GPT-4. In Che, W.; Nabende, J.; Shutova, E.; and Pilehvar, M. T.,
989	eds., Findings of the Association for Computational Linguistics:
990	ACL 2025, 5880–5895. Vienna, Austria: Association for Computational Linguistics. ISBN 979-8-89176-256-5.
991	Jordan, M. I.; Ghahramani, Z.; Jaakkola, T. S.; and Saul, L. K.
992	1999. An introduction to variational methods for graphical models.
993	Machine learning, 37: 183–233.
994	
995	35092
996	
997	Zhuang, Y.; Liu, Q.; Pardos, Z.; Kyllonen, P. C.; Zu, J.; Huang,
998	Z.; Wang, S.; and Chen, E. 2025. Position: AI Evaluation Should
999	Learn from How We Test Humans. In Singh, A.; Fazel, M.; Hsu,
1000	D.; Lacoste-Julien, S.; Berkenkamp, F.; Maharaj, T.; Wagstaff, K.;
1001	and Zhu, J., eds., Proceedings of the 42nd International Conference on Machine Learning, volume 267 of Proceedings of Machine
1002	Learning Research, 82483–82508. PMLR.
1003	
1004	Linguistics: ACL 2023, 13003–13051. Toronto, Canada: Association for Computational Linguistics.
1005	Truong, S. T.; Tu, Y.; Liang, P.; Li, B.; and Koyejo, S. 2025.
1006	Reliable and Efficient Amortized Model-based Evaluation. In
1007	Singh, A.; Fazel, M.; Hsu, D.; Lacoste-Julien, S.; Berkenkamp,
1008	F.; Maharaj, T.; Wagstaff, K.; and Zhu, J., eds., Proceedings of
1009	the 42nd International Conference on Machine Learning, volume
1010	267 of Proceedings of Machine Learning Research, 60238–60265.
1011	PMLR.
1012	Tsutsumi, E.; Kinoshita, R.; and Ueno, M. 2021. Deep item response theory as a novel test theory based on deep learning. Electronics, 10(9): 1020.
1013	Vania, C.; Htut, P. M.; Huang, W.; Mungra, D.; Pang, R. Y.; Phang,
1014	J.; Liu, H.; Cho, K.; and Bowman, S. R. 2021. Comparing Test
1015	Sets with Item Response Theory. In Zong, C.; Xia, F.; Li, W.; and
1016	Navigli, R., eds., Proceedings of the 59th Annual Meeting of the
1017	Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume
1018	1: Long Papers), 1141–1158. Online: Association for Computational Linguistics.
1019	Wang, Y.; Ma, X.; Zhang, G.; Ni, Y.; Chandra, A.; Guo, S.; Ren, W.;
1020	Arulraj, A.; He, X.; Jiang, Z.; Li, T.; Ku, M.; Wang, K.; Zhuang, A.;
1021	Fan, R.; Yue, X.; and Chen, W. 2024. MMLU-Pro: A More Robust
1022	and Challenging Multi-Task Language Understanding Benchmark.
1023	In Globerson, A.; Mackey, L.; Belgrave, D.; Fan, A.; Paquet, U.;
1024	Tomczak, J.; and Zhang, C., eds., Advances in Neural Information
1025	Processing Systems, volume 37, 95266–95290. Curran Associates,
1026	Inc.
1027	White, C.; Dooley, S.; Roberts, M.; Pal, A.; Feuer, B.; Jain, S.;
1028	Shwartz-Ziv, R.; Jain, N.; Saifullah, K.; Dey, S.; Shubh-Agrawal;
1029	Sandha, S. S.; Naidu, S. V.; Hegde, C.; LeCun, Y.; Goldstein, T.;
1030	Neiswanger, W.; and Goldblum, M. 2025. LiveBench: A Challenging, Contamination-Limited LLM Benchmark. In The Thirteenth
1031	International Conference on Learning Representations.
1032	Wu, M.; Davis, R. L.; Domingue, B. W.; Piech, C.; and Goodman,
1033	N. D. 2020. Variational Item Response Theory: Fast, Accurate,
1034	and Expressive. In Rafferty, A. N.; Whitehill, J.; Romero, C.;
1035	and Cavalli-Sforza, V., eds., Proceedings of the 13th International
1036	Conference on Educational Data Mining, EDM 2020, Fully virtual
1037	conference, July 10-13, 2020. International Educational Data Mining Society. ISBN 978-1-7336736-1-7.
1038	Ye, H.; Jin, J.; Xie, Y.; Zhang, X.; and Song, G. 2025. Large language model psychometrics: A systematic review of evaluation,
1039	validation, and enhancement. arXiv preprint arXiv:2505.08245.
1040	Zellers, R.; Holtzman, A.; Bisk, Y.; Farhadi, A.; and Choi, Y.
1041	2019. HellaSwag: Can a Machine Really Finish Your Sentence?
1042	In Korhonen, A.; Traum, D.; and Màrquez, L., eds., Proceedings
1043	of the 57th Annual Meeting of the Association for Computational
1044	Linguistics, 4791–4800. Florence, Italy: Association for Computational Linguistics.
1045	Zhou, H.; Huang, H.; Long, Y.; Xu, B.; Zhu, C.; Cao, H.; Yang, M.;
1046	and Zhao, T. 2024. Mitigating the Bias of Large Language Model
1047	Evaluation. In Maosong, S.; Jiye, L.; Xianpei, H.; Zhiyuan, L.; and
1048	Yulan, H., eds., Proceedings of the 23rd Chinese National Conference on Computational Linguistics (Volume 1: Main Conference),
1049	1310–1319. Taiyuan, China: Chinese Information Processing Society of China.
1050	Zhou, L.; Pacchiardi, L.; Martı́nez-Plumed, F.; Collins, K. M.;
1051	Moros-Daval, Y.; Zhang, S.; Zhao, Q.; Huang, Y.; Sun, L.; Prunty,
1052	J. E.; et al. 2025. General scales unlock ai evaluation with explanatory and predictive power. arXiv preprint arXiv:2503.06378.
1053	
1054	35093
1055	
1056	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d05b10b2-f2e8-4d76-abff-5c1515f75409",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "ad50cdb495cf40e2d",
  "type": "user",
  "uuid": "67fe4590-aa1d-4832-9fb2-db4765a7df35",
  "sourceToolAssistantUUID": "d05b10b2-f2e8-4d76-abff-5c1515f75409",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-21T16:40:16.694Z_

I now have the complete paper content. Let me also check if there are any extended version sections in the arXiv HTML that might not appear in the AAAI version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67fe4590-aa1d-4832-9fb2-db4765a7df35",
  "isSidechain": true,
  "agentId": "ad50cdb495cf40e2d",
  "requestId": "req_011CbG3aDpsWv36moehpGAcm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8373c136-7543-4d27-90af-3daf6658dac3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GNhkq151kBPFoJ7bAzWRC5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13020,
      "cache_read_input_tokens": 32126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13020,
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

_source line 34 · 2026-05-21T16:40:21.332Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AFLiohxsfmDovZ7C9thpGE`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.15055v2",
  "prompt": "This is the extended arXiv version of \"Lost in Benchmarks? Rethinking LLM Benchmarking with IRT\". Extract any content that is NOT in the main 8-page AAAI paper, specifically:\n1. Any appendix sections\n2. Extended experimental results (Table 7, Table 8, Figure 4, Figure 5)\n3. Additional analysis sections\n4. Extended related work\n5. Any content about Figure 4 (scatter plots difficulty vs discriminability) and Figure 5 (examples of items with high/low parameters)\n6. Table 7 (1PL-4PL comparison) and Table 8 (average item properties)\n7. Any limitations section\n8. Extended method details\nReturn all such content verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8373c136-7543-4d27-90af-3daf6658dac3",
  "isSidechain": true,
  "agentId": "ad50cdb495cf40e2d",
  "requestId": "req_011CbG3aDpsWv36moehpGAcm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24ac5cb5-edba-4079-8ad6-95e01b4b046e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GNhkq151kBPFoJ7bAzWRC5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13020,
      "cache_read_input_tokens": 32126,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13020
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 296,
          "cache_read_input_tokens": 32126,
          "cache_creation_input_tokens": 13020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13020,
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

_source line 35 · 2026-05-21T16:40:30.671Z_

<details><summary>↩ Tool result · `toolu_01AFLiohxsfmDovZ7C9thpGE`</summary>

```text
# Extended Content from arXiv Version

## Appendix A: Implementation Details

**A.1 Estimation Ability of PSN-IRT**

The training methodology involved: "split these model-item interactions into training (60%), validation (20%), and test sets (20%)" with Adam optimizer (learning rate 0.003, weight decay 0.0001, batch size 512). For benchmark analysis, "the model is trained on the entire unified dataset" for a fixed 30 epochs using identical hyperparameters on an NVIDIA A800-80G GPU.

**A.2 Ablation Study Variants**

Two architectural alternatives were explored:

1. **Semantic Embedding Variant**: Replaced one-hot item identifiers with "dense semantic embeddings" generated from Instructor-XL, but this "fail to yield significant improvements."

2. **Graph Neural Network Variant**: Implemented custom GNN encoder with attention-weighted aggregation mechanisms. The cognitive state formula involved: element-wise products and attention mechanisms, yet results showed that "both variants fail to yield performance gains."

## Appendix B: Additional Analysis

**B.1 Performance Comparison (1PL-4PL)**

Table 7 presents comprehensive results across parameter complexities:
- 1PL through 4PL configurations tested
- PSN-IRT 4PL achieved highest performance (ACC: 0.7998, F1: 0.8538, AUC: 0.8485)
- "performance exhibits no consistent pattern with increasing parameter complexity"
- Traditional IRT methods showed variable results across configurations

**B.2 Detailed Benchmark Statistics**

Table 8 provides fine-grained metrics across all 11 datasets, revealing:
- TheoremQA: highest difficulty (0.6548), lowest feasibility (0.5012)
- Chinese SimpleQA: lowest guessing-rate (0.0609)
- GSM8K: lowest LEH score (0.0038)

**B.3 Difficulty-Discriminability Relationship**

Figure 4 scatter plots demonstrate: "item discriminability tends to be lower when item difficulty reaches extreme levels." Implications include:

"datasets that feature a more balanced distribution of difficulty often exhibit higher overall discriminability, enabling them to more effectively distinguish between models of varying capabilities."

**B.4 Case Study Examples**

Figure 5 illustrates parameter variations:
- **High guessing-rate item**: "multiple-choice question concerning scientific studies shows an exceptionally high guessing parameter...publicly accessible online, suggesting...data contamination"
- **Low feasibility items**: "domain-specific question exhibits low feasibility, suggesting potential item ambiguities"

## No Limitations Section

The arXiv version contains no explicit limitations section beyond those integrated into discussion sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24ac5cb5-edba-4079-8ad6-95e01b4b046e",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "ad50cdb495cf40e2d",
  "type": "user",
  "uuid": "d76fa56b-27cd-431e-ab75-a88fc12634cb",
  "sourceToolAssistantUUID": "24ac5cb5-edba-4079-8ad6-95e01b4b046e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-21T16:40:36.369Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013tTFzrn97V12xmJgpoAmSf`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.15055v2",
  "prompt": "Extract the COMPLETE text of these sections verbatim with all numbers:\n1. Table 7 full data (all rows and columns showing 1PL/2PL/3PL/4PL comparison across all methods)\n2. Table 8 full data (average item-level properties: all rows for all 11 benchmarks, all columns for difficulty, discriminability, guessing-rate, feasibility, LEH, Fisher)\n3. Figure 4 caption and all surrounding text paragraphs discussing the scatter plots\n4. Figure 5 caption and all surrounding text paragraphs discussing the item examples\n5. The complete text discussing the relationship between difficulty and discriminability\n6. The complete text discussing data contamination case studies\n7. The GNN architecture description with the exact cognitive degree formula\nReturn all text verbatim preserving exact numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d76fa56b-27cd-431e-ab75-a88fc12634cb",
  "isSidechain": true,
  "agentId": "ad50cdb495cf40e2d",
  "requestId": "req_011CbG3bU5A3r8wWeGAvttkC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9aa12b16-37c7-49d5-bcf2-4275d1d98a5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RHMhYxAk7DZNmvnVQRyBnU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 936,
      "cache_read_input_tokens": 45146,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 936
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 271,
          "cache_read_input_tokens": 45146,
          "cache_creation_input_tokens": 936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 936,
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

_source line 37 · 2026-05-21T16:40:49.459Z_

<details><summary>↩ Tool result · `toolu_013tTFzrn97V12xmJgpoAmSf`</summary>

```text
# Extracted Data from PSN-IRT Research Paper

## Table 7: Performance Comparison across IRT Parameters

| Model | Method | Parameter | ACC | F1 | AUC | Kendall's τ |
|-------|--------|-----------|-----|----|----|------------|
| IRT | MLE | 1PL | 0.7219 | 0.8035 | 0.6970 | 1.0000 |
| IRT | MLE | 2PL | 0.7172 | 0.7998 | 0.6963 | 0.9091 |
| IRT | MLE | 3PL | 0.7218 | 0.8031 | 0.7057 | 0.9697 |
| IRT | MLE | 4PL | 0.7211 | 0.8034 | 0.7012 | 0.9697 |
| IRT | MCMC | 1PL | 0.7168 | 0.8011 | 0.7268 | 0.9697 |
| IRT | MCMC | 2PL | 0.7232 | 0.8130 | 0.7301 | 0.9697 |
| IRT | MCMC | 3PL | 0.7172 | 0.8081 | 0.7297 | 1.0000 |
| IRT | MCMC | 4PL | 0.7070 | 0.7811 | 0.7278 | 0.9697 |
| IRT | VI | 1PL | 0.7209 | 0.8024 | 0.6822 | 0.9697 |
| IRT | VI | 2PL | 0.7198 | 0.8012 | 0.6938 | 1.0000 |
| IRT | VI | 3PL | 0.7189 | 0.8011 | 0.6956 | 0.9697 |
| IRT | VI | 4PL | 0.7201 | 0.8015 | 0.6940 | 0.9091 |
| IRT | VIBO | 1PL | 0.7007 | 0.7801 | 0.6901 | 0.9697 |
| IRT | VIBO | 2PL | 0.7301 | 0.8048 | 0.6987 | 0.8788 |
| IRT | VIBO | 3PL | 0.7172 | 0.7993 | 0.7048 | 0.9091 |
| IRT | VIBO | 4PL | 0.7188 | 0.8007 | 0.7055 | 0.9697 |
| Deep-IRT | Deep Learning | 1PL | 0.7974 | 0.8516 | 0.8519 | 0.9697 |
| PSN-IRT | Deep Learning | 1PL | 0.7948 | 0.8497 | 0.8473 | 0.9091 |
| PSN-IRT | Deep Learning | 2PL | 0.7560 | 0.8266 | 0.8259 | 0.9697 |
| PSN-IRT | Deep Learning | 3PL | 0.7965 | 0.8510 | 0.8510 | 0.8788 |
| PSN-IRT | Deep Learning | 4PL | 0.7998 | 0.8538 | 0.8485 | 1.0000 |

## Table 8: Average Item-Level Properties Across Datasets

| Dataset | Difficulty | Discriminability | Guessing | Feasibility | LEH | Fisher |
|---------|-----------|------------------|----------|-------------|-----|--------|
| ARC-C | -1.1637 | 1.2822 | 0.2621 | 0.9481 | 0.0041 | 0.0005 |
| BBH | -0.6033 | 1.3845 | 0.1657 | 0.8747 | 0.0057 | 0.0006 |
| Chinese SimpleQA | 0.2656 | 1.4474 | 0.0609 | 0.7088 | 0.0089 | 0.0006 |
| GPQA Diamond | 0.1902 | 0.8598 | 0.1518 | 0.6437 | 0.0142 | 0.0014 |
| GSM8K | -0.7899 | 1.5255 | 0.1491 | 0.9167 | 0.0038 | 0.0004 |
| HellaSwag | -1.0353 | 1.2920 | 0.2449 | 0.9304 | 0.0047 | 0.0006 |
| HumanEval | -0.6351 | 1.4459 | 0.1565 | 0.8957 | 0.0046 | 0.0005 |
| MATH | -0.2396 | 1.5793 | 0.0673 | 0.8290 | 0.0054 | 0.0004 |
| MBPP | -0.3456 | 1.3625 | 0.1345 | 0.8221 | 0.0071 | 0.0007 |
| MMLU | -0.8383 | 1.1968 | 0.2381 | 0.8921 | 0.0067 | 0.0008 |
| TheoremQA | 0.6548 | 1.0656 | 0.0888 | 0.5012 | 0.0145 | 0.0013 |

## Difficulty-Discriminability Relationship

"Item discriminability tends to be lower when item difficulty reaches extreme levels—that is, when items are either very easy or very hard." Consequently, "datasets that feature a more balanced distribution of difficulty often exhibit higher overall discriminability, enabling them to more effectively distinguish between models."

The paper notes that "benchmarks such as MATH and GSM8K, which contain a range of difficulties, achieve high average discriminability. Conversely, datasets like GPQA Diamond and TheoremQA, which are characterized by a concentration of very difficult items, exhibit the lowest average discriminability."

## GNN Architecture: Cognitive Degree Formula

The cognitive degree 𝐥ₛ,q is computed as:

**𝐥ₛ,q = Linear_gate([𝐞q, 𝐖_rel · rel])**

Where 𝐞q represents item embedding, 𝐖_rel projects response into embedding space, and [·,·] denotes concatenation.

## Data Contamination Case Study

"A multiple-choice question concerning scientific studies shows an exceptionally high guessing parameter. This item's content is publicly accessible online, suggesting an associated risk of data contamination."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9aa12b16-37c7-49d5-bcf2-4275d1d98a5d",
  "isSidechain": true,
  "promptId": "a6787d7e-356d-43d4-972c-414995b1c71b",
  "agentId": "ad50cdb495cf40e2d",
  "type": "user",
  "uuid": "76e5b070-aefb-4208-b3ae-86c9f44439c2",
  "sourceToolAssistantUUID": "9aa12b16-37c7-49d5-bcf2-4275d1d98a5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-21T16:43:48.641Z_

I now have all the material needed. Here is the complete extraction:

---

## Paper: "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory"

**Venue:** AAAI 2026 (Oral), Technical Track on NLP VI, Vol. 40, Issue 41, pp. 35085–35093  
**arXiv:** 2505.15055 (v1: 2025-05-21, v2: 2025-08-01, v3: 2026-01-16)  
**Authors:** Hongli Zhou*, Hui Huang*, Ziqing Zhao, Lvyuan Han, Huicheng Wang, Kehai Chen, Muyun Yang†, Wei Bao†, Jian Dong†, Bing Xu, Conghui Zhu, Hailong Cao, Tiejun Zhao  
**Affiliations:** Faculty of Computing, Harbin Institute of Technology; HIT Shenzhen; China Electronics Standardization Institute  
**Code:** https://github.com/Joe-Hall-Lee/PSN-IRT

---

## 1. Abstract (verbatim)

The evaluation of large language models (LLMs) via benchmarks is widespread, yet inconsistencies between different leaderboards and poor separability among top models raise concerns about their ability to accurately reflect authentic model capabilities. This paper provides a critical analysis of benchmark effectiveness, examining mainstream prominent LLM benchmarks using results from diverse models. We first propose Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture. PSN-IRT can be utilized for accurate and reliable estimations of item characteristics and model abilities. Based on PSN-IRT, we conduct extensive analysis on 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality. Furthermore, we demonstrate that leveraging PSN-IRT is able to construct smaller benchmarks while maintaining stronger alignment with human preference.

---

## 2. Introduction (complete)

As the scale and performance of large language models (LLMs) continue to grow, accurately measuring their capabilities has become increasingly important (Chang et al. 2024; Zhou et al. 2024; Huang et al. 2025). Currently, the performance of LLMs is primarily evaluated through various benchmarks (Wang et al. 2024), which are comprehensive test suites consisting of carefully designed questions to assess model behavior across different tasks. However, in practice, existing benchmarks often exhibit significant limitations, prompting consideration of their effectiveness (McIntosh et al. 2024).

As illustrated in Figure 1, on one hand, even benchmarks that are designed to measure similar underlying capabilities often produce inconsistent leaderboards, leading to substantial ranking variations for the same model (Perlitz et al. 2024). On the other hand, many benchmarks show weak separability among top models, limiting the ability to understand performance differences and further model refinement. Given these limitations, there is a growing need for a more systematic analysis of LLM benchmarks.

In this paper, we conduct a comprehensive analysis for various popular LLM benchmark datasets. Our experiment is based on Item Response Theory (IRT) (Lord, Novick, and Birnbaum 1968; Baker and Kim 2004), a psychometric framework widely used in educational assessment to analyze item properties such as difficulty by modeling item response against examinee ability. However, traditional IRT struggles with the complexity and scale of modern datasets, and its assumption of the normal distribution of abilities does not always hold.

To advance our objective, we propose the Pseudo-Siamese Network for IRT (PSN-IRT), a framework for comprehensive and interpretable analysis of benchmark test sets. PSN-IRT processes model identifiers and item identifiers through independent neural network pathways. These pathways respectively estimate latent model ability and a rich set of item parameters. The estimated properties are then integrated using an IRT-based formulation to predict outcome probabilities. This architectural design ensures both powerful modeling capabilities and strong theoretical interpretability.

To validate the effectiveness of PSN-IRT, we conduct extensive experiments on evaluation results from 12 LLMs across 11 benchmarks. Our results show that PSN-IRT outperforms previous approaches in both parameter estimation accuracy and reliability. Based on PSN-IRT, we perform in-depth analyses of these benchmarks using key metrics, with main findings as follows:

1. LLM benchmarks fail to achieve simultaneous excellence across multiple measurements.
2. LLM benchmarks suffer from widespread saturation and insufficient difficulty ceilings, limiting their ability to challenge and accurately evaluate advanced models.
3. LLM benchmarks exhibit data contamination in numerous items, compromising their reliability.

Furthermore, we find that model rankings derived from high-quality datasets selected by PSN-IRT are more consistent with human preference and offer stronger discriminability among top models.

**Contributions:**
1. We propose PSN-IRT, a benchmark analysis framework with superior estimation accuracy and reliability.
2. We use PSN-IRT for an in-depth analysis of mainstream benchmarks and find that current LLM benchmarks present deficiencies in many aspects.
3. We show that selecting items with PSN-IRT leads to model rankings that better align with human preference.

---

## 3. Related Work (complete)

Researchers have explored various methods to evaluate and analyze the quality of LLM benchmarks. Recent efforts have introduced quantitative metrics that operate at a holistic, dataset level. For example, Benchmark Agreement Testing (BAT) assesses benchmark reliability by comparing the consistency of model rankings across different leaderboards (Perlitz et al. 2024; White et al. 2025). Other novel metrics have also been proposed for more nuanced dataset-level analysis (Li et al. 2024). Delving deeper than macro-level comparisons, another significant line of work focuses on content-based analysis to ground evaluation in concrete capabilities. For instance, ADeLe (Zhou et al. 2025) leverages scalable cognitive rubrics and item demand features to build highly interpretable capability profiles for AI systems.

Item Response Theory (IRT) (Lord, Novick, and Birnbaum 1968; Baker and Kim 2004) offers a psychometric framework for data-driven, item-level analysis. Within natural language processing (NLP), IRT has been primarily utilized to diagnose fundamental item properties such as difficulty and discriminability (Vania et al. 2021; Byrd and Srivastava 2022). More recently, its principles have also been used to inspire methods for improving evaluation efficiency, for instance, through optimized item selection (Maia Polo et al. 2024) or adaptive testing paradigms (Zhuang et al. 2025; Truong et al. 2025). However, due to the complexity and scale of modern datasets and its assumption of normally distributed abilities, the application of IRT on LLM benchmarks is still underexplored (Ye et al. 2025).

---

## 4. Background: IRT (complete)

Item Response Theory (IRT) (Lord, Novick, and Birnbaum 1968) is a psychometric framework widely used in educational and cognitive assessments to model the relationship between benchmark items and examinee abilities. Unlike Classical Test Theory (CTT) (DeVellis 2006), which relies on aggregate test scores, IRT analyzes individual item responses as a function of a latent ability θ, enabling precise measurement of both item and examinee properties.

Central to IRT is the Item Characteristic Curve (ICC), a mathematical function that describes the probability of a correct response, P(X=1|θ), as a function of ability θ. Typically logistic, the ICC visualizes how item properties influence performance, serving as the foundation for IRT.

The simplest IRT model, the One-Parameter Logistic (1PL) model, defines the ICC as:

P(X=1|θ) = 1 / (1 + e^{-(θ−b)})

where b denotes item difficulty. When θ=b, the probability of a correct response is 0.5. The 1PL assumes all items have equal discriminability, a simplification that may not hold in complex testing scenarios. More advanced IRT models introduce additional parameters to capture diverse item properties. However, traditional IRT often suffers from inaccurate parameter estimation and relies on assumptions like normal ability distributions, which may not align with real-world data (Tsutsumi, Kinoshita, and Ueno 2021).

---

## 5. Method: PSN-IRT (complete)

### Model Architecture

The PSN-IRT architecture comprises two independent networks: a model network and an item network. The model network processes one-hot encoded LLM identifiers to estimate model-ability θ, while the item network handles one-hot encoded item identifiers to produce the four IRT parameters: discriminability a, difficulty b, guessing-rate c, and feasibility d.

Each network consists of three fully connected layers with ReLU activation functions, enabling efficient and stable parameter estimation. After that, these estimated properties are then processed by a Logistic Calculation Layer. This layer operates using the Four-Parameter Logistic (4PL) model:

P(X=1|θ) = c + (d−c) · 1/(1+e^{−a(θ−b)})   ... (Eq. 2)

Parameter roles:
- difficulty b: determines the ability level where the probability changes most significantly
- discriminability a: reflects an item's power to differentiate between models of varying abilities
- guessing-rate c: captures how likely models are to succeed without full understanding
- feasibility d: represents the maximum probability that even highly proficient models will correctly answer the item

PSN-IRT follows standard IRT assumptions such as unidimensionality and monotonicity, which generally hold for LLM benchmarking (Kipnis et al. 2025; Truong et al. 2025).

### Training

PSN-IRT is trained end-to-end using observed binary response data in the form of (Model, Item, Response, Outcome), where the binary outcome indicates correctness. During training, PSN-IRT processes encoded pairs of LLM and item identifiers through their respective network pathways. These estimated properties are passed to a Logistic Calculation Layer, with training objective:

J(θ) = −(1/N) Σ [y_i · log(P_i) + (1−y_i) · log(1−P_i)]   ... (Eq. 3)

where N is the batch size. All learnable weights within both model and item networks are updated simultaneously, concurrently optimizing estimated properties for both models and benchmark items.

### Applications

Upon completion of training, the two networks can be used for:
- Model Network: outputs estimate of model-ability θ
- Item Network: outputs four estimated psychometric parameters a, b, c, d for in-depth diagnosis of individual item characteristics and overall benchmark quality

---

## 6. Benchmark Quality Measurements (complete)

Beyond the 4 IRT parameters (difficulty, discriminability, guessing-rate, feasibility), two additional metrics are used:

**Local Efficiency Headroom (LEH):** Assesses the potential of a test example to evaluate future progress in LLMs. Calculated as the derivative of the item's ICC with respect to the highest observed latent ability. A high LEH score indicates that even the top model remains far from the saturation point of the ICC.

**Fisher information:** Measures the amount of information an item provides about a model's ability level. For 4PL IRT:

I(θ) = a²(P(θ)−c)²(d−P(θ))² / [(d−c)² · P(θ)(1−P(θ))]   ... (Eq. 4)

where P(θ) is defined as Eq. 2.

---

## 7. Experiments: Datasets (Table 1)

| Benchmark | Data Size | Domain | Metric | Format |
|-----------|-----------|--------|--------|--------|
| ARC-C | 295 | General | EM | Multiple Choice |
| BBH | 6,511 | General | EM | Mixed |
| Chinese SimpleQA | 3,000 | Knowledge | LLM-as-a-Judge | QA |
| GPQA Diamond | 198 | Science | EM | Multiple Choice |
| GSM8K | 1,319 | Math | EM | QA |
| HellaSwag | 10,042 | General | EM | Multiple Choice |
| HumanEval | 164 | Code | Pass@1 | QA |
| MATH | 5,000 | Math | EM | QA |
| MBPP | 500 | Code | Pass@1 | QA |
| MMLU | 14,042 | General | EM | Multiple Choice |
| TheoremQA | 800 | Science | EM | QA |

**Total: 41,871 items.**

**Model pool:**
- Strong models (8): 360GPT2-Pro, DeepSeek-V3, Doubao-pro, Gemini-1.5, Hunyuan-Turbo, Moonshot-v1, Qwen-Plus, Yi-Lightning
- Weak models (4, intentionally included to broaden discriminability): Gemma-2B-it, Mistral-7B-Instruct-v0.1, Qwen2.5-3B-Instruct, Vicuna-7B-v1.3

Data split: training (60%), validation (20%), test (20%). For benchmark analysis, the full dataset is used (30 epochs).

**Evaluation via OpenCompass; binary response matrix constructed by aggregating item-level results across all models and benchmarks.**

---

## 8. Baselines

- IRT with MLE (Maximum Likelihood Estimation), 4PL
- IRT with MCMC (Markov Chain Monte Carlo), 4PL
- IRT with VI (Variational Inference), 4PL
- IRT with VIBO, 4PL
- Deep-IRT (extension of 1PL IRT via deep networks) — Tsutsumi, Kinoshita, and Ueno 2021

---

## 9. Metrics

1. **Prediction accuracy:** accuracy, F1 score, ROC AUC
2. **Rank stability:** Kendall's τ between model rankings derived from two held-out test subsets

---

## 10. Main Results (Table 2)

| Model | Parameter | Method | ACC | F1 | AUC | Kendall's τ |
|-------|-----------|--------|-----|----|-----|-------------|
| IRT | 4PL | MLE | 0.7211 | 0.8034 | 0.7012 | 0.9697 |
| IRT | 4PL | MCMC | 0.7070 | 0.7811 | 0.7278 | 0.9697 |
| IRT | 4PL | VI | 0.7201 | 0.8015 | 0.6940 | 0.9091 |
| IRT | 4PL | VIBO | 0.7188 | 0.8007 | 0.7055 | 0.9697 |
| Deep-IRT | 1PL | Deep Learning | 0.7974 | 0.8516 | 0.8519 | 0.9697 |
| PSN-IRT | 4PL | Deep Learning | **0.7998** | **0.8538** | 0.8485 | **1.0000** |

PSN-IRT attains prediction accuracy on par with Deep-IRT and surpasses it in rank reliability (1.0000 vs 0.9697).

---

## 11. Ablation Study (Table 3)

| Method | ACC | F1 | AUC | Kendall's τ |
|--------|-----|----|-----|-------------|
| PSN-IRT (baseline) | 0.7998 | 0.8538 | 0.8485 | 1.0000 |
| + Embedding (Instructor-XL) | 0.7808 | 0.8413 | 0.8310 | 0.9394 |
| + GNN | 0.7928 | 0.8490 | 0.8197 | 0.7273 |

Both alternatives underperform. Semantic similarity between item texts does not necessarily reflect similarity in measurement characteristics. GNN's neighborhood aggregation risks diluting unique statistical signals.

**Parameter stability (Table 4) — Pearson correlation vs. full dataset, all p < 0.0001:**

| Data % | Difficulty | Discrim. | Guessing | Feasibility |
|--------|-----------|----------|----------|-------------|
| 30% | 0.9009 | 0.8186 | 0.8274 | 0.9025 |
| 50% | 0.7437 | 0.7835 | 0.8776 | 0.9330 |
| 70% | 0.9519 | 0.7414 | 0.8320 | 0.9442 |

High correlation across all parameters regardless of data subset.

---

## 12. Table 7: Full Parameter Count Comparison (1PL–4PL)

| Method | Param | ACC | F1 | AUC | Kendall's τ |
|--------|-------|-----|----|-----|-------------|
| IRT MLE | 1PL | 0.7219 | 0.8035 | 0.6970 | 1.0000 |
| IRT MLE | 2PL | 0.7172 | 0.7998 | 0.6963 | 0.9091 |
| IRT MLE | 3PL | 0.7218 | 0.8031 | 0.7057 | 0.9697 |
| IRT MLE | 4PL | 0.7211 | 0.8034 | 0.7012 | 0.9697 |
| IRT MCMC | 1PL | 0.7168 | 0.8011 | 0.7268 | 0.9697 |
| IRT MCMC | 2PL | 0.7232 | 0.8130 | 0.7301 | 0.9697 |
| IRT MCMC | 3PL | 0.7172 | 0.8081 | 0.7297 | 1.0000 |
| IRT MCMC | 4PL | 0.7070 | 0.7811 | 0.7278 | 0.9697 |
| IRT VI | 1PL | 0.7209 | 0.8024 | 0.6822 | 0.9697 |
| IRT VI | 2PL | 0.7198 | 0.8012 | 0.6938 | 1.0000 |
| IRT VI | 3PL | 0.7189 | 0.8011 | 0.6956 | 0.9697 |
| IRT VI | 4PL | 0.7201 | 0.8015 | 0.6940 | 0.9091 |
| IRT VIBO | 1PL | 0.7007 | 0.7801 | 0.6901 | 0.9697 |
| IRT VIBO | 2PL | 0.7301 | 0.8048 | 0.6987 | 0.8788 |
| IRT VIBO | 3PL | 0.7172 | 0.7993 | 0.7048 | 0.9091 |
| IRT VIBO | 4PL | 0.7188 | 0.8007 | 0.7055 | 0.9697 |
| Deep-IRT | 1PL | 0.7974 | 0.8516 | 0.8519 | 0.9697 |
| PSN-IRT | 1PL | 0.7948 | 0.8497 | 0.8473 | 0.9091 |
| PSN-IRT | 2PL | 0.7560 | 0.8266 | 0.8259 | 0.9697 |
| PSN-IRT | 3PL | 0.7965 | 0.8510 | 0.8510 | 0.8788 |
| PSN-IRT | 4PL | 0.7998 | 0.8538 | 0.8485 | 1.0000 |

Traditional IRT shows no consistent pattern with increasing parameter complexity; PSN-IRT 4PL is best.

---

## 13. Benchmark Analysis Findings

### Table 5: Ranks of datasets (lower = better)

| Dataset | Difficulty | Discriminability | Guessing | Feasibility | LEH | Fisher | Total |
|---------|-----------|-----------------|----------|-------------|-----|--------|-------|
| Chinese SimpleQA | 2 | 3 | 1 | 9 | 3 | 5 | 23 |
| TheoremQA | 1 | 10 | 3 | 11 | 2 | 2 | 29 |
| MBPP | 5 | 6 | 4 | 8 | 4 | 4 | 31 |
| MATH | 4 | 1 | 2 | 7 | 7 | 10 | 31 |
| GPQA Diamond | 3 | 11 | 6 | 10 | 1 | 1 | 32 |
| BBH | 6 | 5 | 8 | 6 | 6 | 7 | 38 |
| MMLU | 9 | 9 | 9 | 5 | 5 | 3 | 40 |
| GSM8K | 8 | 2 | 5 | 3 | 11 | 11 | 40 |
| HumanEval | 7 | 4 | 7 | 4 | 9 | 9 | 40 |
| HellaSwag | 10 | 7 | 10 | 2 | 8 | 6 | 43 |
| ARC-C | 11 | 8 | 11 | 1 | 10 | 8 | 49 |

### Table 8: Average item-level properties

| Dataset | Difficulty | Discriminability | Guessing | Feasibility | LEH | Fisher |
|---------|-----------|-----------------|----------|-------------|-----|--------|
| ARC-C | -1.1637 | 1.2822 | 0.2621 | 0.9481 | 0.0041 | 0.0005 |
| BBH | -0.6033 | 1.3845 | 0.1657 | 0.8747 | 0.0057 | 0.0006 |
| Chinese SimpleQA | 0.2656 | 1.4474 | 0.0609 | 0.7088 | 0.0089 | 0.0006 |
| GPQA Diamond | 0.1902 | 0.8598 | 0.1518 | 0.6437 | 0.0142 | 0.0014 |
| GSM8K | -0.7899 | 1.5255 | 0.1491 | 0.9167 | 0.0038 | 0.0004 |
| HellaSwag | -1.0353 | 1.2920 | 0.2449 | 0.9304 | 0.0047 | 0.0006 |
| HumanEval | -0.6351 | 1.4459 | 0.1565 | 0.8957 | 0.0046 | 0.0005 |
| MATH | -0.2396 | 1.5793 | 0.0673 | 0.8290 | 0.0054 | 0.0004 |
| MBPP | -0.3456 | 1.3625 | 0.1345 | 0.8221 | 0.0071 | 0.0007 |
| MMLU | -0.8383 | 1.1968 | 0.2381 | 0.8921 | 0.0067 | 0.0008 |
| TheoremQA | 0.6548 | 1.0656 | 0.0888 | 0.5012 | 0.0145 | 0.0013 |

### Finding 1 (verbatim from paper)

"LLM benchmarks fail to achieve simultaneous excellence across multiple measurement properties. As shown in Table 5, the results clearly demonstrate this lack of simultaneous excellence. While Chinese SimpleQA achieves the best overall score, no benchmark performs universally well across the individual metrics. For instance, Chinese SimpleQA itself suffers from poor feasibility with a rank of 9. This pattern of strengths being offset by significant weaknesses is common across benchmarks, which underscores the inherent challenges and trade-offs in benchmark design. Moreover, the property distributions visualized in Figure 3 further highlight this variability and the difficulty for any single benchmark to achieve balanced, high quality across all desired measurement properties."

### Finding 2 (verbatim)

"Current LLM benchmarks exhibit an insufficient difficulty ceiling to challenge the most advanced models. As shown in Table 5, difficulty is varied among different benchmarks. Datasets such as TheoremQA, Chinese SimpleQA, and GPQA Diamond lead in difficulty and continue to challenge many LLMs. In contrast, other benchmarks including ARC-C, HellaSwag, and MMLU have become comparatively easy, where many of the items are readily solved by high-performing models, diminishing their utility for differentiating top-tier systems. Crucially, as shown in Figure 3, even the most challenging items in existing benchmarks exhibit relatively low difficulty levels. For instance, on the IRT scale, the highest item difficulty values rarely exceed 1.0, while top models such as DeepSeek-V3 have estimated abilities well above 3.0. This indicates that even the hardest questions are significantly below the capability level of elite LLMs, highlighting a lack of sufficient challenge for frontier capabilities."

### Finding 3 (verbatim)

"Generally low LEH scores across most benchmarks reveal widespread item saturation. While Table 5 indicates that datasets like GPQA Diamond and TheoremQA achieve the highest relative ranks for average LEH, suggesting they offer more headroom than other benchmarks, the absolute LEH values in Figure 3 are often smaller than ideal. Conversely, benchmarks such as GSM8K and ARC-C exhibit lower average LEH scores. This signifies that current high-performing models are already approaching or have reached the performance ceiling for a substantial portion of items within these test sets. This necessitates the development of new benchmark items and datasets explicitly designed with greater headroom as models continue to evolve."

### Finding 4 (verbatim)

"Outlier-high guessing-rates in many benchmark items flag risks of data contamination. The guessing-rate reflects the chance that a model can answer a question correctly without actual understanding, typically by exploiting format-based cues or shortcuts. As shown in Figure 3, datasets like ARC-C, HellaSwag, and MMLU generally present higher guessing-rates, possibly due to their multiple-choice formats. Notably, further inspection of the item guessing-rate parameter distributions, as depicted in Figure 3, reveals that a considerable number of items across several benchmarks exhibit unusually high guessing-rates. This observation regards the potential for such items to indicate data contamination, namely the content or answers for these items might have been present in the models' pre-training data (Zhuang et al. 2025)."

### Finding 5 (verbatim)

"Widespread low-feasibility items in scientific benchmarks reveal flawed question design. Feasibility estimates how well a question can be answered based on the information provided. Low feasibility often arises from underspecified or overly broad questions, where even a strong model cannot determine a clear answer. As shown in Figure 3, datasets like TheoremQA and GPQA Diamond exhibit lower feasibility, likely due to complex scientific contexts or vague problem descriptions. In contrast, ARC-C and HellaSwag have high feasibility, suggesting their questions are well-formed and specific. Low feasibility more often reflects weaknesses in annotation quality or task design, and such items can distort evaluation by penalizing models for failing to resolve ambiguities (Rodriguez et al. 2021)."

---

## 14. Difficulty–Discriminability Relationship (Figure 4 context)

"Item discriminability tends to be lower when item difficulty reaches extreme levels — that is, when items are either very easy or very hard. Consequently, datasets that feature a more balanced distribution of difficulty often exhibit higher overall discriminability, enabling them to more effectively distinguish between models of varying capabilities. Benchmarks such as MATH and GSM8K, which contain a range of difficulties, achieve high average discriminability. Conversely, datasets like GPQA Diamond and TheoremQA, which are characterized by a concentration of very difficult items, exhibit the lowest average discriminability."

---

## 15. Efficient Benchmarking Section (complete)

### Experimental Setup

"To evaluate the effectiveness of different item selection strategies, we design an experiment to evaluate the effectiveness of different item selection strategies. Our methodology involves Benchmark Agreement Testing (BAT) (Perlitz et al. 2024). We first establish a reference model ranking by aggregating results from two public leaderboards: Chatbot Arena (Chiang et al. 2024) and OpenCompass Arena (Contributors 2023). Subsequently, various subsets of benchmark items are chosen based on different criteria. Model rankings generated using these subsets are then compared against the reference arena ranking using Kendall's τ to measure agreement. Alongside agreement, we also consider the variance of model scores on these subsets; higher variance generally indicates the subset's capacity to differentiate more clearly between models. The evaluations are conducted using two distinct model groupings: one set comprising a mix of stronger and weaker models ('w/ weak models'), and another set from which weaker models are excluded ('w/o weak models'), to specifically assess separability among stronger contenders."

### Table 6: Variance and Kendall's τ for data selection strategies

| Strategy | w/ weak — Variance | w/ weak — Kendall | w/o weak — Variance | w/o weak — Kendall |
|----------|--------------------|-------------------|----------------------|--------------------|
| All | 0.0434 | 0.6444 | 0.0010 | 0.2381 |
| Top 400 — Random | 0.0421 | 0.6444 | 0.0007 | 0.2381 |
| Top 400 — Clustering | 0.0308 | 0.6000 | 0.0058 | 0.1429 |
| Top 400 — Discrim. | 0.1841 | 0.5556 | 0.0000 | 0.2381 |
| Top 400 — Fisher | 0.0049 | 0.6889 | 0.0033 | 0.7143 |
| Top 1000 — Random | 0.0406 | 0.6444 | 0.0009 | 0.2381 |
| Top 1000 — Clustering | 0.0166 | 0.6444 | 0.0041 | 0.2381 |
| Top 1000 — Discrim. | 0.1805 | 0.6000 | 0.0000 | 0.3813 |
| Top 1000 — Fisher | 0.0039 | 0.6889 | 0.0030 | **0.9048** |

### Results

"Selecting items based on Fisher information consistently produces model rankings with superior alignment to the reference arena ranking. For instance, a carefully selected subset composed of just 1,000 items chosen via the Fisher information criterion achieves a Kendall's τ of up to 0.9048. This level of agreement markedly surpasses that achieved by rankings derived from using all available items or from similarly sized randomly selected subsets.

In contrast, other item selection approaches are less effective for distinguishing strong models. For instance, selecting items based on discriminability yields zero score variance when weak models are excluded, indicating it merely separates broad capability tiers rather than providing granularity among top-performers. Separately, clustering items based on their success/failure vectors (Pacchiardi, Cheke, and Hernández-Orallo 2024) also fails to improve ranking correlation, even when it increases score separability."

---

## 16. Implementation Details

- Split: training 60%, validation 20%, test 20% (for estimation accuracy evaluation)
- For benchmark analysis: trained on entire unified dataset for fixed 30 epochs
- Optimizer: Adam, lr=0.003, weight decay=0.0001, batch size=512
- Early stopping: patience=5 epochs, monitored on validation F1 (for estimation evaluation only)
- Hardware: single NVIDIA A800-80G GPU

---

## 17. Figure Captions (all)

**Figure 1:** Illustration of weak separability and ranking inconsistencies in LLM benchmarks (source: opencompass.org.cn)

**Figure 2:** The illustration of our proposed PSN-IRT. Separate neural networks estimate model-ability (θ) and item parameters (a, b, c, d), which are then combined via the IRT formula to predict the probability of a correct response. After that, the networks can be leveraged for estimating properties for models or items, respectively.

**Figure 3:** Distribution of item-level properties across 11 LLM benchmarks. [Six subplots: Difficulty, Discriminability, Guessing Rate, Feasibility, LEH, Fisher Information — each showing box/violin plots per dataset]

**Figure 4:** Scatter plots showing the relationship between item difficulty and discriminability across 11 benchmarks. Each plot highlights how difficulty affects discriminability within a dataset.

**Figure 5:** Examples of benchmark items exhibiting high and low estimated values for key psychometric parameters, as determined by PSN-IRT. Each pair shows an item with a high parameter value alongside one with a low value for the specified characteristic.

---

## 18. Table Captions (all)

**Table 1:** Benchmarks used in this paper.

**Table 2:** Comparison of prediction accuracy and rank reliability across different methods.

**Table 3:** Ablation study on PSN-IRT's input representation and network architecture.

**Table 4:** Pearson correlation coefficients of item parameters estimated on random subsets of the data versus those estimated on the full dataset. All correlations are statistically significant (p < 0.0001).

**Table 5:** Ranks of datasets based on average item-level properties estimated by PSN-IRT. Each rank is obtained by averaging the property over all items in a dataset and then sorting these averages; smaller rank values correspond to better performance.

**Table 6:** Variance and Kendall's τ for various data selection strategies with and without weak models.

**Table 7:** Comparison of prediction accuracy and rank reliability across different methods using 1PL-4PL parameters.

**Table 8:** Average item-level properties across datasets. Each value represents the mean of the corresponding metric over all benchmark items.

---

## 19. Conclusion (verbatim)

"In this work, we introduce PSN-IRT, a framework that combines psychometrics with neural networks to provide comprehensive and reliable analyses of LLM benchmarks. Through extensive experiments on 12 LLMs across 11 diverse datasets, we demonstrate that current benchmarks often suffer from uneven measurement properties, insufficient difficulty ceilings, item saturation, and data contamination. Moreover, we show that strategically selecting smaller, high-quality item sets using PSN-IRT enhances alignment with human preference and separability among top models."

---

## 20. Limitations

No explicit limitations section exists in either the AAAI or arXiv version. Limitations are embedded within findings:
- PSN-IRT estimates parameters specific to training data, requiring retraining to analyze new items (acknowledged in ablation)
- The paper does not claim to address all benchmark design issues, only to diagnose them

---

## Key Identifiers for YAML

- **paper_key:** zhou2026lost
- **venue:** AAAI 2026
- **full_text_available:** true (PDF retrieved from AAAI proceedings)
- **method_family:** IRT + neural network (pseudo-siamese)
- **core_claim:** PSN-IRT uses dual MLP networks to estimate 4PL IRT parameters for LLM benchmark items, enabling principled diagnosis of benchmark quality deficiencies (saturation, contamination, insufficient difficulty ceiling) and construction of smaller, human-preference-aligned evaluation sets via Fisher information-based item selection
- **key_results:** PSN-IRT ACC=0.7998, F1=0.8538, Kendall τ=1.000 (vs Deep-IRT τ=0.9697); Fisher-selected 1000-item subset achieves τ=0.9048 with human preference rankings vs τ=0.2381 for all 41,871 items (w/o weak models)
- **datasets:** 11 LLM benchmarks, 41,871 items total, 12 models
- **baselines:** IRT-MLE, IRT-MCMC, IRT-VI, IRT-VIBO (all 4PL), Deep-IRT (1PL)
- **metrics:** Accuracy, F1, ROC AUC, Kendall's τ (rank stability), Kendall's τ (BAT agreement with human preference)
- **ablation_dimensions:** input representation (one-hot vs embedding), backbone (MLP vs GNN), IRT parameter count (1PL–4PL), data subset size (30%/50%/70%)
- **training_recipe:** Adam lr=0.003, weight_decay=0.0001, batch=512, early_stop patience=5 on val-F1, NVIDIA A800-80G
- **relation_to_us:** complementary (analyzes benchmark quality via IRT; our work studies judge bias in MFRM framework, which is a different psychometric formulation)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76e5b070-aefb-4208-b3ae-86c9f44439c2",
  "isSidechain": true,
  "agentId": "ad50cdb495cf40e2d",
  "requestId": "req_011CbG3crPN6DM7Fd5wP7Jh2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b1f271c-6838-4825-80cf-7b714f2f528c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GeZdXAMs7PtjkwgpJ1ukXa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2096,
      "cache_read_input_tokens": 46082,
      "output_tokens": 9382,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2096
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9382,
          "cache_read_input_tokens": 46082,
          "cache_creation_input_tokens": 2096,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2096,
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
