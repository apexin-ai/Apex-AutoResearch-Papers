# Research conversation: You are helping with a paper distillation task. Fetch and extract detailed information from "CyclicJudge: Mitigating Jud

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a744e5363d82fb6b7.jsonl`
- **Structured JSON:** [`0846e90b5bcf5849504b.json`](../../sessions/08/0846e90b5bcf5849504b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

40 recorded events

### User

_source line 1 · 2026-05-21T16:38:13.933Z_

You are helping with a paper distillation task. Fetch and extract detailed information from "CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation" (arXiv 2026).

Try these URLs using WebFetch:
1. Search: https://arxiv.org/search/?query=CyclicJudge+mitigating+judge+bias+LLM&searchtype=all
2. Also try: https://arxiv.org/search/?query=CyclicJudge+bias+evaluation&searchtype=all
3. If you find an arXiv ID, fetch https://arxiv.org/html/{id}

Extract ALL of the following in detail:
1. Full introduction text
2. All contribution statements
3. Complete experiment section
4. All figure and table captions
5. Paragraphs referencing figures/tables
6. Limitations / future work
7. Method details
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
  "agentId": "a744e5363d82fb6b7",
  "type": "user",
  "uuid": "3e058474-ab7c-4e57-8e2b-18784a1b5101",
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

_source line 2 · 2026-05-21T16:38:13.936Z_

```json
{
  "parentUuid": "3e058474-ab7c-4e57-8e2b-18784a1b5101",
  "isSidechain": true,
  "agentId": "a744e5363d82fb6b7",
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
  "uuid": "34c6d5c0-39b3-447d-ad88-fc7c9c869b42",
  "timestamp": "2026-05-21T16:38:13.936Z",
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

_source line 3 · 2026-05-21T16:38:18.138Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Wx8t7HKBwH77sqXHKRecjY`</summary>

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
  "parentUuid": "34c6d5c0-39b3-447d-ad88-fc7c9c869b42",
  "isSidechain": true,
  "agentId": "a744e5363d82fb6b7",
  "requestId": "req_011CbG3RPTKKJKXqT3XJqBJd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c230d66-b53f-46b3-b442-31278c621245",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01YBwvuHbduAKczv5rT2qhpS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9083,
      "cache_read_input_tokens": 7260,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9083
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 80,
          "cache_read_input_tokens": 7260,
          "cache_creation_input_tokens": 9083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9083,
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

_source line 4 · 2026-05-21T16:38:18.141Z_

<details><summary>↩ Tool result · `toolu_01Wx8t7HKBwH77sqXHKRecjY`</summary>

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
  "parentUuid": "2c230d66-b53f-46b3-b442-31278c621245",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "a744e5363d82fb6b7",
  "type": "user",
  "uuid": "5978dafe-6a9d-41f2-8519-20398cdee764",
  "sourceToolAssistantUUID": "2c230d66-b53f-46b3-b442-31278c621245",
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

_source line 5 · 2026-05-21T16:38:20.351Z_

I'll search for the CyclicJudge paper and fetch its full content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5978dafe-6a9d-41f2-8519-20398cdee764",
  "isSidechain": true,
  "agentId": "a744e5363d82fb6b7",
  "requestId": "req_011CbG3Rhfgqf6U7gknDdTue",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ca4b47d-933c-48f7-b51a-417371fb12ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TNrQu273uNnN1FumVRsJnE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 16343,
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

_source line 6 · 2026-05-21T16:38:21.712Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VzaBvCAWAoSv8WXCtkwZiX`</summary>

```json
{
  "query": "CyclicJudge mitigating judge bias LLM-based evaluation arXiv 2026",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ca4b47d-933c-48f7-b51a-417371fb12ec",
  "isSidechain": true,
  "agentId": "a744e5363d82fb6b7",
  "requestId": "req_011CbG3Rhfgqf6U7gknDdTue",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "117ba7be-a691-4bb7-905a-7231b6ff89e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TNrQu273uNnN1FumVRsJnE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 16343,
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

_source line 7 · 2026-05-21T16:38:23.186Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01X2WN6GvVyHaBayYwE6Ty34`</summary>

```json
{
  "url": "https://arxiv.org/search/?query=CyclicJudge+mitigating+judge+bias+LLM&searchtype=all",
  "prompt": "Find all arXiv paper IDs and titles related to CyclicJudge, judge bias, LLM evaluation. Return the full list of results with arXiv IDs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "117ba7be-a691-4bb7-905a-7231b6ff89e6",
  "isSidechain": true,
  "agentId": "a744e5363d82fb6b7",
  "requestId": "req_011CbG3Rhfgqf6U7gknDdTue",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e256acd-b4ee-4d89-b20d-77cfb613c97a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TNrQu273uNnN1FumVRsJnE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 16343,
      "output_tokens": 241,
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
          "output_tokens": 241,
          "cache_read_input_tokens": 16343,
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

_source line 8 · 2026-05-21T16:38:27.098Z_

<details><summary>↩ Tool result · `toolu_01X2WN6GvVyHaBayYwE6Ty34`</summary>

```text
# arXiv Search Results for CyclicJudge

Based on the search results provided, there is **1 paper** related to CyclicJudge and judge bias in LLM evaluation:

## Paper Details

**arXiv ID:** 2603.01865

**Title:** "CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation"

**Authors:** Ziyi Zhu, Olivier Tieleman, Alexey Bukhtiyarov, Jinghong Chen

**Category:** cs.CL (Computation and Language)

**Key Concept:** The paper addresses systematic biases in LLM-as-judge evaluation by introducing a round-robin judge assignment strategy. According to the abstract, "CyclicJudge, a round-robin assignment of judges to scenarios, is demonstrated to be the optimal strategy" for maintaining evaluation reliability while managing computational costs.

**Announcement Date:** March 2026 (originally announced); v1 submitted March 2, 2026; updated May 4, 2026

This appears to be the only result matching your search criteria in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e256acd-b4ee-4d89-b20d-77cfb613c97a",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "a744e5363d82fb6b7",
  "type": "user",
  "uuid": "157b465a-df72-4e3a-925d-f3d78b161aa3",
  "sourceToolAssistantUUID": "7e256acd-b4ee-4d89-b20d-77cfb613c97a",
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

_source line 9 · 2026-05-21T16:38:28.735Z_

<details><summary>↩ Tool result · `toolu_01VzaBvCAWAoSv8WXCtkwZiX`</summary>

```text
Web search results for query: "CyclicJudge mitigating judge bias LLM-based evaluation arXiv 2026"

Links: [{"title":"CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation","url":"https://arxiv.org/pdf/2603.01865"},{"title":"[2603.01865] CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation","url":"https://arxiv.org/abs/2603.01865"},{"title":"CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation","url":"https://arxiv.org/html/2603.01865"},{"title":"Mitigating the Bias of Large Language Model Evaluation","url":"https://arxiv.org/pdf/2409.16788"},{"title":"[2510.12462] Evaluating and Mitigating LLM-as-a-judge Bias in Communication Systems","url":"https://arxiv.org/abs/2510.12462"}]

I found the paper! Here are the key findings from the CyclicJudge research:

## CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation

The paper addresses systematic biases in LLM-as-judge evaluation, which has become standard practice for open-ended model assessment. 

**The Problem:**
Judge biases are often similar in magnitude to the model differences that benchmarks are designed to detect, resulting in unreliable rankings when single-judge evaluations are used. LLM judges exhibit systematic biases including lenient or strict tendencies, position, verbosity, and self-preference effects.

**The Solution:**
The work introduces a variance decomposition that partitions benchmark score variance into scenario, generation, judge, and residual components. Based on this analysis, CyclicJudge, a round-robin assignment of judges to scenarios, is demonstrated to be the optimal strategy for a fixed judge-call budget.

**Key Advantages:**
CyclicJudge eliminates bias precisely while requiring each judge only once per cycle, matching the cost of single-judge evaluation. Empirical results on MT-Bench and MindEval validate the effectiveness of CyclicJudge as predicted, across both general-purpose and domain-specific evaluation settings.

The paper was submitted on March 2, 2026 and authored by researchers from Slingshot AI and the University of Cambridge.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "117ba7be-a691-4bb7-905a-7231b6ff89e6",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "a744e5363d82fb6b7",
  "type": "user",
  "uuid": "05b63195-71bb-492f-9f9b-f968428be9d3",
  "sourceToolAssistantUUID": "117ba7be-a691-4bb7-905a-7231b6ff89e6",
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

_source line 10 · 2026-05-21T16:38:38.333Z_

The arXiv ID is 2603.01865. Now fetching the full HTML version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05b63195-71bb-492f-9f9b-f968428be9d3",
  "isSidechain": true,
  "agentId": "a744e5363d82fb6b7",
  "requestId": "req_011CbG3SUk5sDwBkz4EaV8zq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd9a5301-86e3-4307-9cbc-b2ab88633980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0155SYbgWpLJSTd1vuPVZ4v3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 292,
      "cache_creation_input_tokens": 874,
      "cache_read_input_tokens": 18278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 874,
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

_source line 11 · 2026-05-21T16:38:42.195Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SgiQCXi9oRVuwWArMJYhbZ`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.01865",
  "prompt": "Extract ALL of the following in COMPLETE, VERBATIM text (no summarization):\n1. Full introduction section (every paragraph)\n2. All contribution statements (usually at the end of the introduction)\n3. Complete method/approach section (every paragraph)\n4. Complete experiment section (every paragraph, every number)\n5. All figure captions (exact text)\n6. All table captions (exact text)\n7. All paragraphs that reference figures or tables\n8. Limitations and future work sections\n9. All ablation study text\n10. Complete conclusion section\nReturn the raw extracted text preserving structure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd9a5301-86e3-4307-9cbc-b2ab88633980",
  "isSidechain": true,
  "agentId": "a744e5363d82fb6b7",
  "requestId": "req_011CbG3SUk5sDwBkz4EaV8zq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6dafed8-d3dd-4eeb-90da-191b12f9b804",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0155SYbgWpLJSTd1vuPVZ4v3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 292,
      "cache_creation_input_tokens": 874,
      "cache_read_input_tokens": 18278,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 874
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 292,
          "output_tokens": 239,
          "cache_read_input_tokens": 18278,
          "cache_creation_input_tokens": 874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 874,
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

_source line 12 · 2026-05-21T16:39:06.745Z_

<details><summary>↩ Tool result · `toolu_01SgiQCXi9oRVuwWArMJYhbZ`</summary>

```text
# CyclicJudge Paper: Key Content Extraction

## 1. Introduction Section

"LLM-as-judge evaluation has become the de facto standard for open-ended model assessment" with systematic biases including "position, verbosity, and self-preference effects." The paper notes that "systematic bias does not average away across more scenarios or generations: reducing them requires aggregating across multiple judges."

The authors treat "the mean score of a diverse K_tot-judge panel as the reference for evaluation; our goal is to recover this panel mean efficiently."

## 2. Contribution Statements

Three main contributions are presented:

1. "A mixed-effects model that decomposes benchmark variance into random noise and panel-relative judge offsets, showing they require fundamentally different remedies"

2. "A proof that round-robin cycling achieves lower variance than alternative strategies: it cancels the panel-relative offsets exactly while maximizing generation diversity at any budget"

3. "Empirical results on MT-Bench and MindEval validating the effectiveness of CyclicJudge as predicted, across both general-purpose and domain-specific evaluation settings"

## 3. Methodology Section

### Model Specification

The scoring model is: X_ijℓ = μ_θ + α_i + β_ij + γ_ℓ + ε_ijℓ

Where:
- μ_θ: "panel-mean estimand for model θ—the average score the K_tot-judge panel would assign in expectation, with random noise removed"
- α_i: "scenario effect—how much individual scenario difficulty varies for model θ"
- β_ij: "generation effect—variability from stochastic decoding"
- γ_ℓ: "judge offset relative to the panel mean—a fixed constant for each judge"
- ε_ijℓ: "residual—captures judge-level noise and all interaction terms"

"The random effects (α,β,ε) are mutually independent with finite second moments; no distributional assumptions (e.g. Gaussianity) are needed."

### Variance Decomposition

"Var(X̄) = [σ²_α/n + σ²_β/nm + σ²_ε/nmK] + [σ²_γ/K · (K_tot-K)/(K_tot-1)]"

"Each noise term shrinks with more data at or above its hierarchy level. The bias term V_γ responds only to K and vanishes exactly at K=K_tot."

### Allocation Strategies

**Strategy A (All judges):** "Use all K_tot judges for each of m=B/K_tot generations"
Result: V_A(B) = (K_tot·σ²_β + σ²_ε)/(nB)

**Strategy B (Random single):** "Use m=B generations, each scored by one randomly sampled judge"
Result: V_B(B) = (σ²_β + σ²_γ + σ²_ε)/(nB)

**Strategy C (CyclicJudge):** "Use m=B generations, assigning judge j mod K_tot to generation j"
Result: V_C(B) = (σ²_β + σ²_ε)/(nB)

"CyclicJudge achieves lower variance everywhere on both benchmarks, and predictions match empirical results precisely."

## 4. Experiments Section

### Domain and Data

**MT-Bench:** "general-purpose multi-turn conversational benchmark with 80 two-turn questions spanning 8 categories, scored on a 1–10 scale per turn (averaged)"

**MindEval:** "domain-specific benchmark for multi-turn mental health support with 50 scenarios and composite scores on a 1–5 scale covering empathy, safety, and clinical appropriateness"

Five models evaluated: Qwen 2.5 7B, Llama 3.3 70B, GPT-5.2, Gemini 3 Flash, Claude Sonnet 4.6

### Judge Bias Estimates

"On MT-Bench at the default operating point (m=1, K=1), the top-ranked model changes with every judge, with Qwen ranking itself first despite being last by consensus, a pattern consistent with the self-preference bias"

"Judge variance σ̂²_γ ranges from 0.34 to 0.95 across models. Since competitive models on current leaderboards are routinely separated by <0.5 points, single-judge evaluation can easily reverse rankings."

### Variance Components

**MT-Bench findings:** "scenario variance σ̂²_α is the largest per-observation component"

"Generation variance σ̂²_β drops with capability, consistent with the observation that stronger models produce more deterministic outputs"

"The judge offset variance σ̂²_γ remains substantial for all models, accounting for >>94% of benchmark variance at the default operating point"

**MindEval findings:** "Both scenario and generation variance are markedly lower. Scenario variance σ̂²_α drops by one to two orders of magnitude because all MindEval scenarios evaluate the same rubrics"

"The judge offset variance remains the dominant component throughout, exceeding both scenario and generation variance by an order of magnitude"

### Strategy Comparison

"At B=5, switching from random to cycling cuts variance by ∼27–40% across models on MT-Bench"

"The optimal strategy among the two alternatives depends on the sign of (K_tot−1)σ²_β−σ²_γ: all-judges wins when σ²_γ/σ²_β > K_tot−1 = 4"

"CyclicJudge outperforms both alternatives regardless of this ratio."

## 5. Figure/Table Information

### Figure 1 Caption
"Benchmark score variance Var(X̄) vs. per-scenario budget for three strategies: all judges (A), random single judge (B), and CyclicJudge (C)"

### Table 1 Caption
"Mean score ± 95% CI at the default operating point (m=1, K=1). Bold: highest score per judge column. Underline: second highest"

### Table 2 Caption
"Per-observation variance component estimates"

### Table 3 Caption
"Variance component estimates. Per-observation variances and their contribution to Var(X̄) at the default operating point (m=1, K=1)"

## 6. Limitations Section

**Panel-mean reference:** "Our analysis treats the mean score of the K_tot-judge panel as the reference for evaluation... Biases shared across the panel members are absorbed into μ_θ and propagate into the panel mean"

**Linear model approximation:** "LLM-as-judge scores are in fact bounded ordinal variables, so the linear model can produce boundary artifacts and heteroscedastic residuals near the scale endpoints"

**Judge pool size:** "Our judge pool of K_tot=5 limits exploration of larger panels"

**Scenario exchangeability:** "assumes scenarios are interchangeable draws from the dataset; in practice, some scenarios may be more informative than others"

**Balanced design assumption:** "allocation analysis assumes a balanced design in which every scenario receives the same number of judge calls"

**Uniform cost assumption:** "Our budget analysis treats all judge calls as equal cost; in practice, judges vary widely in price and latency"

## 7. Conclusion Section

"We show that CyclicJudge, a round-robin assignment of judges to items, resolves this tension... by recovering the panel-mean score exactly while maximizing generation diversity."

"Three main findings: (1) Systematic judge offsets dominate benchmark score variance at default operating points. (2) Random noise components decrease with model capability and multi-turn evaluation, but the panel-relative offset variance does not. (3) CyclicJudge achieves the lowest variance among all allocation strategies at every budget level"

"The method requires no model-specific tuning and maintains the same per-item cost as single-judge evaluation, providing practitioners with a cost-neutral drop-in replacement"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6dafed8-d3dd-4eeb-90da-191b12f9b804",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "a744e5363d82fb6b7",
  "type": "user",
  "uuid": "c04da211-52ed-4e5b-a382-9e3d139e610b",
  "sourceToolAssistantUUID": "c6dafed8-d3dd-4eeb-90da-191b12f9b804",
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

_source line 13 · 2026-05-21T16:39:18.433Z_

The WebFetch returned a summarized version. Let me fetch the raw HTML directly to get verbatim text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c04da211-52ed-4e5b-a382-9e3d139e610b",
  "isSidechain": true,
  "agentId": "a744e5363d82fb6b7",
  "requestId": "req_011CbG3VHJLqf7ArAGUafMdX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9fe56c2-32de-470d-a246-f8a6d2e15351",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0119vFV918czFAAbGD6uSqBi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2441,
      "cache_read_input_tokens": 19152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2441,
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

_source line 14 · 2026-05-21T16:39:19.627Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018aVB4F7k13Zuka9GeHSyVU`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.01865",
  "prompt": "Return the complete abstract, author list, submission date, and any visible metadata. Return verbatim text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9fe56c2-32de-470d-a246-f8a6d2e15351",
  "isSidechain": true,
  "agentId": "a744e5363d82fb6b7",
  "requestId": "req_011CbG3VHJLqf7ArAGUafMdX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd7e3c52-93e7-470e-be59-1678482026a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0119vFV918czFAAbGD6uSqBi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2441,
      "cache_read_input_tokens": 19152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2441,
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

_source line 15 · 2026-05-21T16:39:20.878Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HjeRQNNp4Ro621sJdBibgV`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.01865v2",
  "prompt": "Return ALL text from this paper verbatim, including every section: introduction, related work, method, experiments, results, ablation, conclusion, limitations. Do not summarize. Return complete raw text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd7e3c52-93e7-470e-be59-1678482026a0",
  "isSidechain": true,
  "agentId": "a744e5363d82fb6b7",
  "requestId": "req_011CbG3VHJLqf7ArAGUafMdX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6e258a5-ca87-40f6-92fd-e2069471873b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0119vFV918czFAAbGD6uSqBi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2441,
      "cache_read_input_tokens": 19152,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2441
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 19152,
          "cache_creation_input_tokens": 2441,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2441,
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

_source line 16 · 2026-05-21T16:39:24.105Z_

<details><summary>↩ Tool result · `toolu_018aVB4F7k13Zuka9GeHSyVU`</summary>

```text
# CyclicJudge Paper Information

**Title:** CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation

**Authors:** Ziyi Zhu, Olivier Tieleman, Alexey Bukhtiyarov, Jinghong Chen

**Submission Date:** March 2, 2026 (v1)

**Last Revision:** May 4, 2026 (v3)

**arXiv Identifier:** 2603.01865

**Subject Area:** Computer Science - Computation and Language (cs.CL)

---

## Abstract

The paper addresses systematic biases in language model evaluation. The authors present a variance decomposition framework and propose CyclicJudge, which "is demonstrated to be the optimal strategy for a fixed judge panel and judge-call budget: the score recovers the panel mean exactly while matching the cost of single-judge evaluation." Validation occurs through testing on MT-Bench and MindEval across both general and domain-specific contexts.

---

## License

Creative Commons Attribution 4.0 International (CC BY 4.0)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd7e3c52-93e7-470e-be59-1678482026a0",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "a744e5363d82fb6b7",
  "type": "user",
  "uuid": "e2b89b0d-7976-45fa-9e17-fc0c209cd75d",
  "sourceToolAssistantUUID": "dd7e3c52-93e7-470e-be59-1678482026a0",
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

_source line 17 · 2026-05-21T16:39:28.397Z_

<details><summary>↩ Tool result · `toolu_01HjeRQNNp4Ro621sJdBibgV`</summary>

```text
# Summary of CyclicJudge Research Paper

## Core Contribution

This paper addresses systematic bias in LLM-based evaluation by proposing **CyclicJudge**, a round-robin judge assignment strategy. The authors demonstrate that judge bias is a persistent problem that cannot be eliminated through additional scenarios or generations alone.

## Key Technical Innovation

The paper develops a **variance decomposition** separating benchmark score variance into four components:
- Scenario effects
- Generation variability  
- Judge bias (fixed, not random)
- Residual noise

As stated: "Systematic bias does not average away. Adding more test scenarios or regenerating responses reduces random noise but leaves judge bias intact."

## Why CyclicJudge Works

The round-robin approach achieves three objectives simultaneously:
1. **Eliminates bias exactly** through balanced judge rotation
2. **Maximizes generation diversity** compared to using all judges per generation
3. **Maintains single-judge evaluation cost** while delivering multi-judge robustness

## Empirical Validation

Testing on MT-Bench (general-purpose) and MindEval (domain-specific mental health) revealed:
- Judge bias dominates variance at typical operating points (>94% on MT-Bench)
- Single-judge rankings can reverse across different judges
- CyclicJudge outperforms alternative strategies consistently across both benchmarks

## Practical Implication

"CyclicJudge achieves the lowest variance among all allocation strategies at every budget level, regardless of the model's variance profile" while requiring no model-specific tuning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6e258a5-ca87-40f6-92fd-e2069471873b",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "a744e5363d82fb6b7",
  "type": "user",
  "uuid": "6b599d33-4242-4861-b244-7af65c2d105d",
  "sourceToolAssistantUUID": "c6e258a5-ca87-40f6-92fd-e2069471873b",
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

_source line 18 · 2026-05-21T16:39:30.393Z_

The HTML fetch is being summarized. Let me try fetching specific sections directly from the HTML.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b599d33-4242-4861-b244-7af65c2d105d",
  "isSidechain": true,
  "agentId": "a744e5363d82fb6b7",
  "requestId": "req_011CbG3WsnY8ZUm4WZCFN84g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2e343df-5392-46a0-804e-8bacae958697",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013cwew5u8FyzsSvJTJx8Bn2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 904,
      "cache_read_input_tokens": 21593,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 904,
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

_source line 19 · 2026-05-21T16:39:33.654Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Fu1naumLCew5vW7xG4WdaQ`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.01865",
  "prompt": "This is a research paper HTML page. I need you to copy-paste the VERBATIM text of every section. Do NOT summarize or paraphrase anything. Copy the exact wording from:\n- The abstract (exact text)\n- Section 1 (Introduction) - every single paragraph word for word\n- Section 2 (any related work or background)\n- Section 3 (method/model specification) - every equation description and paragraph\nReturn the raw text exactly as written in the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2e343df-5392-46a0-804e-8bacae958697",
  "isSidechain": true,
  "agentId": "a744e5363d82fb6b7",
  "requestId": "req_011CbG3WsnY8ZUm4WZCFN84g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0bd560cd-b699-4734-ae57-ff35de3f992c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013cwew5u8FyzsSvJTJx8Bn2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 904,
      "cache_read_input_tokens": 21593,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 904,
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

_source line 20 · 2026-05-21T16:39:34.441Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015DU1B7WwbH1454CQEUTJHA`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2603.01865",
  "prompt": "Extract ALL text from this PDF verbatim. Return every section in full: abstract, introduction, related work, method, experiments, results, limitations, conclusion. Do not summarize. Return complete text of every paragraph."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bd560cd-b699-4734-ae57-ff35de3f992c",
  "isSidechain": true,
  "agentId": "a744e5363d82fb6b7",
  "requestId": "req_011CbG3WsnY8ZUm4WZCFN84g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a77ae58a-686b-4fec-82aa-78ae414a7f1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013cwew5u8FyzsSvJTJx8Bn2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 904,
      "cache_read_input_tokens": 21593,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 904
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 320,
          "cache_read_input_tokens": 21593,
          "cache_creation_input_tokens": 904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 904,
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

_source line 21 · 2026-05-21T16:39:40.500Z_

<details><summary>↩ Tool result · `toolu_01Fu1naumLCew5vW7xG4WdaQ`</summary>

```text
# Summary of CyclicJudge Paper

## Core Contribution

The paper introduces **CyclicJudge**, a round-robin judge assignment strategy for LLM-based evaluation that mitigates systematic judge bias without increasing computational cost.

## Key Problem

As stated in the abstract: "judges exhibit systematic biases that cannot be averaged out by increasing the number of scenarios or generations. These biases are often similar in magnitude to the model differences that benchmarks are designed to detect."

## Main Innovation

The authors develop a variance decomposition separating benchmark score variance into four components: scenario, generation, judge, and residual. They prove that "CyclicJudge, a round-robin assignment of judges to scenarios, is demonstrated to be the optimal strategy for a fixed judge panel and judge-call budget: the score recovers the panel mean exactly while matching the cost of single-judge evaluation."

## Methodology Highlights

The model specification treats each score as: μ + scenario effect + generation effect + judge offset + residual noise. Critically, the judge offset γ represents "panel-relative" bias—deviation from the panel's average tendency rather than absolute truth.

Three allocation strategies are compared:
- **Strategy A**: All judges per generation
- **Strategy B**: Random single judge per generation  
- **Strategy C**: CyclicJudge (round-robin cycling)

The mathematical analysis shows CyclicJudge achieves lower variance than both alternatives at any budget level.

## Empirical Validation

Testing on MT-Bench and MindEval confirms predictions. On MT-Bench, switching from random to cycling "cuts variance by approximately 27–40% across models."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0bd560cd-b699-4734-ae57-ff35de3f992c",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "a744e5363d82fb6b7",
  "type": "user",
  "uuid": "86b8fce2-8ad6-4f53-89b9-a8705cda0b42",
  "sourceToolAssistantUUID": "0bd560cd-b699-4734-ae57-ff35de3f992c",
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

_source line 22 · 2026-05-21T16:39:40.839Z_

<details><summary>↩ Tool result · `toolu_015DU1B7WwbH1454CQEUTJHA`</summary>

```text
I appreciate your request, but I need to clarify what I can do here.

The content you've provided appears to be a PDF file in raw binary format (the PDF object structure), not readable text. The document metadata indicates this is "CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation" by Zhu et al.

**I cannot extract the full verbatim text** because:

1. The actual text content is compressed/encoded within the PDF stream objects (objects 65, 137, 162, 169, 195, 232, 237, 240, 243, 251, 258)
2. These streams use FlateDecode compression, requiring decompression to read
3. Extracting and reproducing the complete paper text would constitute reproducing a substantial copyrighted academic work

**What I can do instead:**

- **Summarize the paper's contributions:** CyclicJudge appears to address judge bias in LLM-based evaluation through an efficient methodology
- **Quote specific passages** (under 125 characters) if you paste readable text
- **Discuss the methodology** based on visible metadata and structure
- **Direct you to the source:** The paper is available at arxiv.org/abs/2603.01865v3

If you have access to the readable PDF text and want specific sections analyzed or quoted, please paste those sections and I'm happy to help while respecting copyright limits.

[Binary content (application/pdf, 461.9KB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/webfetch-1779381574471-asmire.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a77ae58a-686b-4fec-82aa-78ae414a7f1c",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "a744e5363d82fb6b7",
  "type": "user",
  "uuid": "33f0b6e7-1e86-4d81-8596-c6b5eda5da4c",
  "sourceToolAssistantUUID": "a77ae58a-686b-4fec-82aa-78ae414a7f1c",
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

_source line 23 · 2026-05-21T16:39:43.281Z_

A PDF was saved locally. Let me read it, and also try fetching specific HTML subsections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33f0b6e7-1e86-4d81-8596-c6b5eda5da4c",
  "isSidechain": true,
  "agentId": "a744e5363d82fb6b7",
  "requestId": "req_011CbG3XnzanmKGfFQgYDWBf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd568002-6039-4f56-8d99-80f907c53c13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TnrEvSDcSA2oXWitVJpCjw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1191,
      "cache_read_input_tokens": 22497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1191,
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

_source line 24 · 2026-05-21T16:39:45.151Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AWCGZQPXQXLTmwX2JgF4tQ`</summary>

```json
{
  "command": "ls /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/ 2>/dev/null && echo \"---\" && file /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/*.pdf 2>/dev/null",
  "description": "List saved PDF file and check its type"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd568002-6039-4f56-8d99-80f907c53c13",
  "isSidechain": true,
  "agentId": "a744e5363d82fb6b7",
  "requestId": "req_011CbG3XnzanmKGfFQgYDWBf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8009fcb3-5d7b-46f9-9b0d-26b001aa9c43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TnrEvSDcSA2oXWitVJpCjw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1191,
      "cache_read_input_tokens": 22497,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1191
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 284,
          "cache_read_input_tokens": 22497,
          "cache_creation_input_tokens": 1191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1191,
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

_source line 25 · 2026-05-21T16:39:45.262Z_

<details><summary>↩ Tool result · `toolu_01AWCGZQPXQXLTmwX2JgF4tQ`</summary>

```text
webfetch-1779381491497-bzue2k.pdf
webfetch-1779381520695-2q52tb.pdf
webfetch-1779381520903-z41iar.pdf
webfetch-1779381574471-asmire.pdf
webfetch-1779381577805-diiyry.pdf
---
/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/webfetch-1779381491497-bzue2k.pdf: PDF document, version 1.6 (zip deflate encoded)
/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/webfetch-1779381520695-2q52tb.pdf: PDF document, version 1.5, 2 page(s)
/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/webfetch-1779381520903-z41iar.pdf: PDF document, version 1.7, 12 page(s)
/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/webfetch-1779381574471-asmire.pdf: PDF document, version 1.7, 15 page(s)
/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/webfetch-1779381577805-diiyry.pdf: PDF document, version 1.7, 6 page(s)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8009fcb3-5d7b-46f9-9b0d-26b001aa9c43",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "a744e5363d82fb6b7",
  "type": "user",
  "uuid": "511d0899-b9bb-4e2b-bbf0-4fdb7fe8372f",
  "sourceToolAssistantUUID": "8009fcb3-5d7b-46f9-9b0d-26b001aa9c43",
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

_source line 26 · 2026-05-21T16:39:50.138Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01YGFs91zNNn7y4Y6yF6Lqfc`</summary>

```json
{
  "command": "which pdftotext && pdftotext /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/webfetch-1779381574471-asmire.pdf - 2>/dev/null | head -300",
  "description": "Extract text from the 15-page PDF (likely the full paper)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "511d0899-b9bb-4e2b-bbf0-4fdb7fe8372f",
  "isSidechain": true,
  "agentId": "a744e5363d82fb6b7",
  "requestId": "req_011CbG3Y815XPYhBM7M15Txs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1ee0b5e-3b56-4e10-b2a5-629e96a94fad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01U77zdiQb11zs8hNGwVuZuG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 959,
      "cache_read_input_tokens": 23688,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 959
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 200,
          "cache_read_input_tokens": 23688,
          "cache_creation_input_tokens": 959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 959,
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

_source line 27 · 2026-05-21T16:39:50.246Z_

<details><summary>↩ Tool result · `toolu_01YGFs91zNNn7y4Y6yF6Lqfc`</summary>

```text
/usr/bin/pdftotext
CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation
Ziyi Zhu1 , Olivier Tieleman1 , Alexey Bukhtiyarov1 , Jinghong Chen2
1
Slingshot AI 2 Department of Engineering, University of Cambridge
Correspondence: ziyi@slingshotai.com

arXiv:2603.01865v3 [cs.CL] 4 May 2026

Abstract

judge panel as the reference for evaluation; our
goal is to recover this panel mean efficiently.
We show that CyclicJudge, a round-robin assignment of judges to items, resolves this tension.
To establish this formally, we develop a variance
decomposition rooted in generalizability theory
(Brennan, 2001; Shavelson and Webb, 1991) that
separates benchmark score variance into scenario,
generation, judge, and residual components. Our
contributions are:

LLM-as-judge evaluation has become standard practice for open-ended model assessment; however, judges exhibit systematic biases that cannot be averaged out by increasing the number of scenarios or generations.
These biases are often similar in magnitude
to the model differences that benchmarks are
designed to detect, resulting in unreliable rankings when single-judge evaluations are used.
We introduce a variance decomposition that
partitions benchmark score variance into scenario, generation, judge, and residual components. Based on this analysis, CyclicJudge, a
round-robin assignment of judges to scenarios,
is demonstrated to be the optimal strategy for
a fixed judge panel and judge-call budget: the
score recovers the panel mean exactly while
matching the cost of single-judge evaluation.
Empirical results on MT-Bench and MindEval validate the effectiveness of CyclicJudge
as predicted, across both general-purpose and
domain-specific evaluation settings.

1

1. A mixed-effects model that decomposes benchmark variance into random noise and panelrelative judge offsets, showing they require fundamentally different remedies (§3.1–3.2).
2. A proof that round-robin cycling achieves lower
variance than alternative strategies: it cancels
the panel-relative offsets exactly while maximizing generation diversity at any budget (§3.3).
3. Empirical results on MT-Bench and MindEval validating the effectiveness of CyclicJudge
as predicted, across both general-purpose and
domain-specific evaluation settings (§4).

Introduction

2

LLM-as-judge evaluation has become the de facto
standard for open-ended model assessment (Zheng
et al., 2023). A growing body of work indicates
that LLM judges are systematically biased: some
models are consistently lenient, others strict, with
additional position, verbosity, and self-preference
effects (Zheng et al., 2023; Shi et al., 2024; Wang
et al., 2024). A standard Analysis of Variance
(ANOVA; Fisher, 1925) on our data confirms that
judge main effect is highly significant (§4.2).
Crucially, systematic bias does not average away
across more scenarios or generations: reducing
them requires aggregating across multiple judges.
Yet running every judge on every item multiplies
evaluation cost by the panel size and sacrifices generation diversity at a fixed budget. Throughout this
work, we treat the mean score of a diverse Ktot -

Related Work

LLM judge biases and multi-judge approaches.
LLM judges exhibit systematic position bias (Wang
et al., 2024; Shi et al., 2024), length bias (Dubois
et al., 2024), self-preference (Wataoka et al., 2024),
and cognitive biases (Koo et al., 2024); we refer
readers to Gu et al. (2024) for a comprehensive
survey. Multi-judge panels mitigate these biases
by averaging over diverse judge tendencies (Verga
et al., 2024), while psychometric reliability analyses further demonstrate that single-judge evaluations yield insufficiently stable scores (Schroeder
and Wood-Doughty, 2024).
Benchmark reliability and generation variance.
Madaan et al. (2025) empirically quantifies variance across hundreds of models and benchmarks,
1

and Alvarado Gonzalez et al. (2025) shows via
ANOVA that unrepeated evaluations frequently produce rank inversions across benchmark subcategories. Zhang et al. (2025) proposes a hierarchical
model decomposing variance into within-prompt
and between-prompt components, and Mizrahi et al.
(2024) shows that prompt paraphrasing alone can
reverse model rankings. Our work extends this line
by further separating systematic judge bias from
random noise.

the panel reference, not from absolute truth: bias
shared by all panel members is absorbed into µθ .
iid

• εijℓ ∼ (0, σε2 ): residual—captures judge-level
noise and all interaction terms; we discuss these
modeling choices in Appendix I.
The random effects (α, β, ε) are mutually independent with finite second moments; no distributional
assumptions (e.g. Gaussianity) are needed. The n
scenarios and K judges are each drawn by simple
random sampling without replacement, independently of each other and of all random effects.

Budget-constrained evaluation. Saha et al.
(2026) frames judge selection as a multi-armed
bandit problem, Luettgau et al. (2025) applies hierarchical Bayesian partial pooling in low-data
regimes, and Miller (2024) derives standard errors
and power formulas for benchmark scores; Dorner
et al. (2025) further establishes fundamental scaling limits on the accuracy gains from additional
judge queries.

3

Methodology

3.1

Model Specification

3.2

The benchmark
score is the grand mean X̄ =
1 P
i,j,ℓ Xijℓ , which decomposes as X̄ = µθ +
nmK
ᾱ+ β̄ + γ̄ + ε̄, where each bar denotes a hierarchical
sample mean.
Proposition 1 (Variance decomposition).
Var(X̄) =

σβ2
σγ2 Ktot − K
σα2
σε2
+
+
+
·
nm
−1
{z nmK} |K K
|n
{ztot
}
random noise

Consider evaluating model θ on n scenarios from a
dataset D of N total scenarios, with m independent
generations per scenario, each scored by K judges
drawn from a pool of Ktot . The same K judges
score every scenario–generation cell (a crossed design). We model each score as:
Xijℓ = µθ + αi + βij + γℓ + εijℓ

Variance Decomposition

Vγ : judge bias

(2)
Each noise term shrinks with more data at or
above its hierarchy level. The bias term Vγ responds only to K and vanishes exactly at K = Ktot .
The proof uses the law of total variance, conditioning on the judge selection, combined with a finite
population correction for sampling K from Ktot
centered bias values (Appendix C).

(1)

where i ∈ {1, . . . , n} indexes scenarios, j ∈
{1, . . . , m} indexes generations within scenario i,
and ℓ indexes the K selected judges. Each term
has a distinct source:

3.3

Allocation Strategies

Given a per-scenario budget of B judge calls, the
design question is how to allocate judges across
generations. The scenario term σα2 /n is fixed once
scenarios are chosen; we compare three strategies
for the remaining variance.

• µθ : panel-mean estimand for model θ—the average score the Ktot -judge panel would assign in
expectation, with random noise removed.

Strategy A: All judges per generation. Use all
Ktot judges for each of m = B/Ktot generations.
The mean of all judge offsets is zero (γ̄ = 0):

iid

• αi ∼ (0, σα2 ): scenario effect—how much individual scenario difficulty varies for model θ. A
dataset whose scenarios all test the same aspects
of model θ equally has σα2 = 0.

VA (B) =

iid

• βij ∼ (0, σβ2 ): generation effect—variability
from stochastic decoding. σβ2 is model-specific;
a deterministic model has σβ2 = 0.

Ktot σβ2 + σε2
nB

(3)

Strategy B: Random single judge per generation. Use m = B generations, each scored by
one randomly sampled judge. Random judge selection injects the panel-relative offset as additional
sampling noise:

• γℓ : judge offset relative to the panel mean—a
fixed constant
P tot for each judge, with centering constraint K
ℓ=1 γℓ = 0 and population dispersion
−1 P
2
2
σγ = Ktot
ℓ γℓ . γℓ measures deviation from

VB (B) =
2

σβ2 + σγ2 + σε2
nB

(4)

Table 1: Mean score ± 95% CI at the default operating
point (m=1, K=1). Bold: highest score per judge
column. Underline: second highest.

Strategy C: CyclicJudge (round-robin). Use
m = B generations, assigning judge j mod Ktot
to generation j. Each judge appears equally often,
so the panel-relative offsets sum to zero (γ̄ = 0):
VC (B) =

σβ2 + σε2
nB

(a) MT-Bench (1–10 scale, n=80)
Judge

(5)

With one generation per scenario (m = 1), the
same variance and offset cancellation is achieved
by cycling judges across scenarios instead. In this
case scenarios should be shuffled before assignment to avoid confounding the cycle with any latent
ordering of the dataset.

Experiments

4.1

Domain and Data

Llama

GPT

Gemini

Claude

Gemini
GPT
Claude
Llama
Qwen

8.02±.16
7.91±.16
7.96±.17
7.87±.18
8.02±.15

8.98±.08
8.81±.11
9.06±.06
8.71±.11
8.39±.16

8.20±.12
8.67±.12
7.91±.13
6.90±.20
6.09±.20

9.88±.06
9.71±.11
9.62±.12
8.58±.25
7.16±.27

8.68±.10
8.49±.13
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1ee0b5e-3b56-4e10-b2a5-629e96a94fad",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "a744e5363d82fb6b7",
  "type": "user",
  "uuid": "8b292c7d-e314-4540-96b0-997242be809d",
  "sourceToolAssistantUUID": "f1ee0b5e-3b56-4e10-b2a5-629e96a94fad",
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

_source line 28 · 2026-05-21T16:39:56.539Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NcTBs91HCzieaYqrPn9zrE`</summary>

```json
{
  "command": "pdftotext /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/webfetch-1779381574471-asmire.pdf - 2>/dev/null | tail -n +300 | head -400",
  "description": "Extract remaining text from PDF pages 3 onwards"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b292c7d-e314-4540-96b0-997242be809d",
  "isSidechain": true,
  "agentId": "a744e5363d82fb6b7",
  "requestId": "req_011CbG3YVCHf4gRyZFUEFjMv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a288bf71-6d02-482d-bdc6-ed6980c4b5c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DumsKbdbdChxK2dKaDV3VM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2879,
      "cache_read_input_tokens": 24647,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2879
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 24647,
          "cache_creation_input_tokens": 2879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2879,
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

_source line 29 · 2026-05-21T16:39:56.711Z_

<details><summary>↩ Tool result · `toolu_01NcTBs91HCzieaYqrPn9zrE`</summary>

```text
8.49±.13
8.52±.13
7.26±.22
5.99±.23

Judge
Model

Qwen

Llama

GPT

Gemini

Claude

Claude
GPT
Gemini
Llama
Qwen

3.86±.08
4.04±.09
3.90±.08
3.70±.07
3.26±.12

4.67±.07
4.51±.07
4.49±.06
4.29±.05
3.38±.21

4.05±.06
3.76±.09
3.63±.05
3.16±.06
2.32±.08

4.72±.06
3.95±.16
3.91±.12
3.00±.10
1.69±.08

4.84±.04
3.39±.15
3.31±.08
2.85±.06
1.74±.05

a subject crossed with K judges. On both benchmarks, the judge main effect is highly significant
(p < 0.001 in all cases; see Appendix H).
Table 1 demonstrates that single-judge evaluation produces unreliable rankings. On MTBench at the default operating point (m=1, K=1),
the top-ranked model changes with every judge,
with Qwen ranking itself first despite being last
by consensus, a pattern consistent with the selfpreference bias documented by Wataoka et al.
(2024). The per-observation variance estimates
(Table 2) confirm this quantitatively: judge variance σ̂γ2 ranges from 0.34 to 0.95 across models.
Since competitive models on current leaderboards
are routinely separated by < 0.5 points (Chiang
et al., 2024), single-judge evaluation can easily reverse rankings. On MindEval, rankings are also
notably more stable across single judges: four of
five produce an identical ordering. Two plausible factors include: domain-specific rubrics may
leave less room for stylistic self-preference, and the
markedly lower scenario and generation variance
on MindEval (§4.3) compresses the absolute size
of any model-dependent fluctuations.

We validate our approach on two benchmarks:
MT-Bench (Zheng et al., 2023) is a generalpurpose multi-turn conversational benchmark with
80 two-turn questions spanning 8 categories, scored
on a 1–10 scale per turn (averaged).
MindEval (Pombal et al., 2025) is a domainspecific benchmark for multi-turn mental health
support with 50 scenarios and composite scores
on a 1–5 scale covering empathy, safety, and clinical appropriateness. Each scenario simulates a full
10-turn therapeutic session with a synthetic patient.
For both benchmarks, we evaluate five models—
Qwen 2.5 7B Instruct (Yang et al., 2024), Llama
3.3 70B Instruct (Grattafiori et al., 2024), GPT-5.2,
Gemini 3 Flash, and Claude Sonnet 4.6, which also
serve as judges in a symmetric design. MT-Bench
uses m=10 generations per scenario (4,000 scores
per model); MindEval uses m=5 (1,250 scores
per model). We follow the default judge decoding
hyperparameters from reference (Appendix J).
4.2

Qwen

(b) MindEval (1–5 scale, n=50)

Advantage of CyclicJudge. Direct comparison
(Appendix E) shows VC ≤ min(VA , VB ) for all B,
with gaps of O(1/B), so CyclicJudge’s advantage
is largest at small budgets of judge calls. The ranking of A vs. B depends on whether (Ktot −1)σβ2 ≷
σγ2 : all judges beat random only when judge bias is
large relative to generation variance.

4

Model

4.3

Variance Components

Table 2 reports the per-observation variance component estimates via crossed ANOVA (see Appendix D). On MT-Bench, scenario variance σ̂α2
is the largest per-observation component; maximizing the number of distinct scenarios always reduces
total variance (Appendix F). Generation variance

Judge Bias Estimates

As a complementary omnibus check on the mixedeffects decomposition (§3.1), we test whether judge
identity has a significant effect using a two-way
ANOVA, treating each scenario–generation pair as
3

Var(benchmark score)

Table 2: Per-observation variance component estimates.
(a) MT-Bench (n=80)
Qwen

Llama

GPT

Gemini

Claude

σ̂α2 (scenario)
σ̂β2 (generation)
σ̂γ2 (judge)
σ̂ε2 (residual)

1.530
0.266
0.947
1.486

0.882
0.238
0.503
1.130

0.634
0.076
0.339
0.564

0.408
0.000
0.435
0.661

0.393
0.000
0.427
0.830

Qwen

Llama

GPT

Gemini

Claude

σ̂α2 (scenario)
σ̂β2 (generation)
σ̂γ2 (judge)
σ̂ε2 (residual)

0.034
0.100
0.523
0.159

0.014
0.019
0.280
0.069

0.021
0.047
0.132
0.207

0.015
0.016
0.150
0.103

0.005
0.002
0.155
0.061

Gemini 3 Flash Claude Sonnet 4.6

10 3
10 4
20

40

20

Qwen 2.5 7B

40

20

40

Budget per scenario
Random 1 judge

Llama 3.3 70B

20

40

20

40

Cycle 5 judges

GPT-5.2

Gemini 3 Flash Claude Sonnet 4.6

10 3
10 4
10

20

10
All 5 judges

20

10

20

Budget per scenario
Random 1 judge

10

20

10

20

Cycle 5 judges

(b) MindEval (1–5 scale, n=50, mmax =5)

Figure 1: Benchmark score variance Var(X̄) vs. perscenario budget for three strategies: all judges (A), random single judge (B), and CyclicJudge (C).

σ̂β2 drops with capability, consistent with the observation that stronger models produce more deterministic outputs. As frontier models increasingly
rely on RL post-training, generation variance may
shrink further (Matsutani et al., 2025). The judge
offset variance σ̂γ2 remains substantial for all models, accounting for >94% of benchmark variance
at the default operating point (see Appendix B).
On MindEval, both scenario and generation variance are markedly lower. Scenario variance σ̂α2
drops by one to two orders of magnitude because
all MindEval scenarios evaluate the same rubrics
across different user profiles, so difficulty varies far
less than on MT-Bench. Generation variance is similarly suppressed: each MindEval generation is a
full 10-turn therapeutic session, so per-response decoding randomness averages out over many turns.
The judge offset variance remains the dominant
component throughout, exceeding both scenario
and generation variance by an order of magnitude.
4.4

GPT-5.2

(a) MT-Bench (1–10 scale, n=80, mmax =10)

(b) MindEval (n=50)
Component

Llama 3.3 70B

All 5 judges

Var(benchmark score)

Component

Qwen 2.5 7B

Gemini and Claude (σ̂β2 ≈ 0), all-judges converges
to CyclicJudge. On MindEval, the ratio exceeds
the threshold for nearly every model, so all-judges
consistently outperforms random. The driver is not
a larger judge offset variance, but rather a sharply
lower generation variance σ̂β2 . Meanwhile, judges’
disagreement over subjective clinical criteria keeps
σ̂γ2 substantial relative to σ̂β2 . CyclicJudge outperforms both alternatives regardless of this ratio.

5

Conclusion

We develop a variance decomposition for LLM-asjudge evaluation that separates systematic betweenjudge offsets from random noise and use it to derive CyclicJudge, a round-robin judge assignment
strategy. Our analysis and experiments on both
a general-purpose benchmark (MT-Bench) and a
domain-specific clinical benchmark (MindEval)
yield three main findings: (1) Systematic judge offsets dominate benchmark score variance at default
operating points. (2) Random noise components
decrease with model capability and multi-turn evaluation, but the panel-relative offset variance does
not. (3) CyclicJudge achieves the lowest variance
among all allocation strategies at every budget level,
regardless of the model’s variance profile, by recovering the panel-mean score exactly while maximizing generation diversity. The method requires
no model-specific tuning and maintains the same
per-item cost as single-judge evaluation, providing
practitioners with a cost-neutral drop-in replacement for more reliable LLM evaluation.

Strategy Comparison

Figure 1 validates the three allocation strategies
via 5,000 subsampling repetitions at each budget
level on both benchmarks. Markers show empirical
variance; dashed lines show exact predictions from
empirical pool variances (Appendix G). CyclicJudge achieves lower variance everywhere on both
benchmarks, and predictions match empirical results precisely. At B=5, switching from random to
cycling cuts variance by ∼27–40% across models
on MT-Bench.
The optimal strategy among the two alternatives
depends on the sign of (Ktot −1)σβ2 −σγ2 : all-judges
wins when σγ2 /σβ2 > Ktot −1 = 4. On MT-Bench,
this ratio is below the threshold for Qwen (3.6) and
Llama (2.1), so random judging is preferable; for
4

Limitations

judges vary widely in price and latency. A costweighted allocation that accounts for per-model
pricing and inference speed would be needed for
real deployment decisions.

Panel-mean reference. Our analysis treats the
mean score of the Ktot -judge panel as the reference
for evaluation. A diverse panel drawn from disjoint
model families typically correlates more strongly
with human judgments than any single judge (Verga
et al., 2024), but the panel means is not a substitute
for absolute ground truth. Biases shared across the
panel members are absorbed into µθ and propagate
into the panel mean. CyclicJudge addresses the
within-panel offsets between individual judges, not
biases that all panel members share; calibrating the
panel itself against human or expert references is
complementary work.

References
Miguel Angel Alvarado Gonzalez, Michelle Bruno Hernandez, Miguel Angel Peñaloza Perez, Bruno
Lopez Orozco, Jesus Tadeo Cruz Soto, and Sandra
Malagon. 2025. Do repetitions matter? strengthening reliability in LLM evaluations. Preprint,
arXiv:2509.24086.
Robert L. Brennan. 2001. Generalizability Theory.
Springer, New York.
Wei-Lin Chiang, Lianmin Zheng, Ying Sheng, Anastasios Nikolas Angelopoulos, Tianle Li, Dacheng Li,
Hao Zhang, Banghua Zhu, Michael Jordan, Joseph E.
Gonzalez, and Ion Stoica. 2024. Chatbot arena: An
open platform for evaluating LLMs by human preference. In Proceedings of the 41st International Conference on Machine Learning.

Linear model approximation. Our variance
decomposition assumes a linear random effects
model, which treats scores as unbounded and continuous. LLM-as-judge scores are in fact bounded
ordinal variables, so the linear model can produce
boundary artifacts and heteroscedastic residuals
near the scale endpoints. A generalized linear
mixed model (GLMM), such as a cumulative-link
mixed model, would properly account for the ordinal, bounded nature of the responses. However,
GLMMs do not yield the closed-form variance decomposition that our allocation analysis relies on.
We therefore retain the linear approximation, noting that it remains reasonable when the scale range
is large relative to the observed score dispersion, as
in our benchmarks.

Florian E. Dorner, Vivian Y. Nastl, and Moritz Hardt.
2025. Limits to scalable evaluation at the frontier:
LLM as judge won’t beat twice the data. In International Conference on Learning Representations.
Yann Dubois, Balázs Galambosi, Percy Liang, and Tatsunori B. Hashimoto. 2024. Length-controlled AlpacaEval: A simple way to debias automatic evaluators. Preprint, arXiv:2404.04475.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a288bf71-6d02-482d-bdc6-ed6980c4b5c4",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "a744e5363d82fb6b7",
  "type": "user",
  "uuid": "c680f39d-290f-40f4-bf82-ecb75d7b59d9",
  "sourceToolAssistantUUID": "a288bf71-6d02-482d-bdc6-ed6980c4b5c4",
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

_source line 30 · 2026-05-21T16:40:03.108Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Wqy5qrm57t2x9U67qxLQJm`</summary>

```json
{
  "command": "pdftotext /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/webfetch-1779381574471-asmire.pdf - 2>/dev/null | tail -n +700 | head -400",
  "description": "Extract remaining text from PDF - appendices and references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c680f39d-290f-40f4-bf82-ecb75d7b59d9",
  "isSidechain": true,
  "agentId": "a744e5363d82fb6b7",
  "requestId": "req_011CbG3YxrgizhJyJvFtdcaH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9bc4458a-b4ab-406a-a401-3477c552bea3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DeLeafGV63dguDfp9Qsph2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3505,
      "cache_read_input_tokens": 27526,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3505
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 27526,
          "cache_creation_input_tokens": 3505,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3505,
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

_source line 31 · 2026-05-21T16:40:03.397Z_

<details><summary>↩ Tool result · `toolu_01Wqy5qrm57t2x9U67qxLQJm`</summary>

```text
Ronald A. Fisher. 1925. Statistical Methods for Research Workers. Oliver and Boyd, Edinburgh.

Judge pool size. Our judge pool of Ktot = 5
limits exploration of larger panels. While the theoretical results generalize to arbitrary K, empirical
validation with larger and more diverse judge pools
would strengthen the practical recommendations.

Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri,
Abhinav Pandey, Abhishek Kadian, Ahmad AlDahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, Amy Yang, Angela Fan, Anirudh
Goyal, Anthony Hartshorn, Aobo Yang, Archi Mitra, Archie Sravankumar, Artem Korenev, Arthur
Hinsvark, and 537 others. 2024. The Llama 3 herd
of models. Preprint, arXiv:2407.21783.

Scenario exchangeability. The “maximize scenarios” recommendation assumes scenarios are interchangeable draws from the dataset; in practice,
some scenarios may be more informative than others, and item-selection methods (Maia Polo et al.,
2024) could alter the tradeoff.

Jiawei Gu, Xuhui Jiang, Zhichao Shi, Hexiang Tan, Xuehao Zhai, Chengjin Xu, Yinghan Li, Jie Liu, Yiwen
Li, Yicheng Shen, Jian Jiang, Shengyao Guo, and
Pengjun Xie. 2024. A survey on LLM-as-a-judge.
Preprint, arXiv:2411.15594.
Ryan Koo, Minhwa Lee, Vipul Raheja, Jong Inn Park,
Zae Myung Kim, and Dongyeop Kang. 2024. Benchmarking cognitive biases in large language models as
evaluators. In Findings of the Association for Computational Linguistics: ACL 2024.

Balanced design assumption. The allocation
analysis assumes a balanced design in which every
scenario receives the same number of judge calls.
Extensions to adaptive or sequential designs remain
future work.

Lennart Luettgau, Alexander Coppock, Yves Dubois,
Christopher Summerfield, and Cozmin Ududec.
2025. HiBayES: A hierarchical Bayesian modeling framework for AI evaluation statistics. Preprint,
arXiv:2505.05602.

Uniform cost assumption. Our budget analysis treats all judge calls as equal cost; in practice,
5

Lovish Madaan, Samarth Singh, Rylan Schaeffer, Andrew Poulton, Sanmi Koyejo, Pontus Stenetorp, Sharan Narang, and Dieuwke Hupkes. 2025. Quantifying variance in evaluation benchmarks. In International Conference on Learning Representations.

Koki Wataoka, Tsubasa Takahashi, and Ryokan Ri.
2024. Self-preference bias in LLM-as-a-judge.
Preprint, arXiv:2410.21819.
An Yang, Baosong Yang, Beichen Zhang, Binyuan
Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian
Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jingren Zhou, Junyang Lin, Kai Dang, and
24 others. 2024. Qwen2.5 technical report. Preprint,
arXiv:2412.15115.

Felipe Maia Polo, Lucas Weber, Leshem Choshen,
Yuekai Sun, Gongjun Xu, and Mikhail Yurochkin.
2024. tinyBenchmarks: Evaluating LLMs with fewer
examples. In Proceedings of the 41st International
Conference on Machine Learning.
Kohsei Matsutani, Shota Takashiro, Gouki Minegishi,
Takeshi Kojima, Yusuke Iwasawa, and Yutaka
Matsuo. 2025. RL squeezes, SFT expands: A
comparative study of reasoning LLMs. Preprint,
arXiv:2509.21128.

Yifan Zhang, Dingwen Cai, and Xingjian Chen. 2025.
Beyond the singular: Revealing the value of multiple generations in benchmark evaluation. Preprint,
arXiv:2502.08943.
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan
Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin,
Zhuohan Li, Dacheng Li, Eric P. Xing, Hao Zhang,
Joseph E. Gonzalez, and Ion Stoica. 2023. Judging
LLM-as-a-judge with MT-Bench and Chatbot Arena.
In Advances in Neural Information Processing Systems, volume 36.

Evan Miller. 2024. Adding error bars to evals: A
statistical approach to language model evaluations.
Preprint, arXiv:2411.00640.
Moran Mizrahi, Guy Kaplan, Dan Malkin, Rotem Dror,
Dafna Shahaf, and Gabriel Stanovsky. 2024. State of
what art? A call for multi-prompt LLM evaluation.
Transactions of the Association for Computational
Linguistics, 12.

A

Judge Bias Estimates

Figure 2 shows the estimated per-judge bias for
each judge–model pair on both benchmarks. A
pronounced self-preference is visible along the diagonal: on MindEval, Claude Sonnet 4.6’s self-bias
of +0.412 is the only positive entry in its otherwise
uniformly negative row, and Qwen 2.5 7B’s selfbias is the largest in its row on both benchmarks.
Judge temperament is not stable across benchmarks: Gemini 3 Flash is the most lenient judge on
MT-Bench (all biases positive), yet becomes one
of the harshest on MindEval, suggesting that judge
personality is benchmark-dependent rather than an
intrinsic model property. On MT-Bench, strictness
correlates with model capability: the two strongest
models by consensus (GPT-5.2 and Claude) are
the most uniformly negative judges, while the two
weakest (Qwen and Llama) are the most lenient.
Finally, the harshest judge–model interactions concentrate on capability-mismatched pairs: GPT-5.2
and Claude penalize Qwen by over one full scale
point on MT-Bench, while their biases toward each
other are an order of magnitude smaller.

José Pombal, Maya D’Eon, Nuno M. Guerreiro, Pedro Henrique Martins, António Farinhas, and Ricardo
Rei. 2025. MindEval: Benchmarking language models on multi-turn mental health support. Preprint,
arXiv:2511.18491.
Aadirupa Saha, Aniket Wagde, and Branislav Kveton. 2026. LLM-as-judge on a budget. Preprint,
arXiv:2602.15481.
Kayla Schroeder and Zach Wood-Doughty. 2024. Can
you trust LLM judgments? reliability of LLM-as-ajudge. Preprint, arXiv:2412.12509.
Shayle R. Searle, George Casella, and Charles E. McCulloch. 1992. Variance Components. Wiley, New
York.
Richard J. Shavelson and Noreen M. Webb. 1991. Generalizability Theory: A Primer. Sage Publications,
Newbury Park, CA.
Lin Shi, Chiyu Ma, Wenhua Liang, Xingjian Diao, Weicheng Ma, and Soroush Vosoughi. 2024. Judging
the judges: A systematic study of position bias in
pairwise comparison with LLM-as-a-judge. Preprint,
arXiv:2406.07791.
Pat Verga, Sebastian Hofstatter, Sophia Althammer, Yixuan Su, Aleksandra Leontiadis, Gautier Izacard, and
Fabio Petroni. 2024. Replacing judges with juries:
Evaluating LLM generations with a panel of diverse
models. Preprint, arXiv:2404.18796.

B

Variance Component Estimates

Table 3 reports the full variance component estimates. The generation variance entries σ̂β2 = 0.000
(Gemini and Claude on MT-Bench) arise because
the method-of-moments estimator σ̂β2 = (MSG −
MSW )/K (Appendix D) can return a negative
value when the between-generation mean square

Peiyi Wang, Lei Li, Liang Chen, Dawei Zhu, Binghuai
Lin, Yunbo Cao, Qi Liu, Tianyu Liu, and Zhifang Sui.
2024. Large language models are not fair evaluators.
In Proceedings of the 62nd Annual Meeting of the
Association for Computational Linguistics.

6

Table 3: Variance component estimates.
Perobservation variances and their contribution to Var(X̄)
at the default operating point (m=1, K=1).

1.0

Llama 3.3 70B +1.257 +0.848 +0.091 +0.224 +0.446

0.5

GPT-5.2 -1.040 -0.962 -0.044 -0.550 -0.707

0.0

Gemini 3 Flash +0.032 +0.711 +0.991 +1.132 +1.003

0.5

4.6

1.0

on
n

et

las
h

2

3F

mi

ud
eS

ni

GP

T-5
.

70
B

3.3

ma

Cla

Ge

Lla

Qw
en

2.5

7B

Claude Sonnet 4.6 -1.136 -0.607 -0.230 -0.071 -0.092

(a) MT-Bench (n=80)

Judge bias

Judge model

Qwen 2.5 7B +0.887 +0.009 -0.808 -0.735 -0.650

Evaluated model
(a) MT-Bench

Llama 3.3 70B +0.904 +0.891 +0.580 +0.641 +0.239
GPT-5.2 -0.159 -0.239 -0.169 -0.219 -0.377
Gemini 3 Flash -0.786 -0.399 +0.021 +0.061 +0.293

0.25
0.00

0.25
0.50
0.75

.6

h

Llama

GPT

Gemini

Claude

7.13

7.87

8.72

8.75

8.61

Per-observation variance
σ̂α2 (scenario)
1.530
σ̂β2 (generation)
0.266
σ̂γ2 (judge)
0.947
σ̂ε2 (residual)
1.486

0.882
0.238
0.503
1.130

0.634
0.076
0.339
0.564

0.408
0.000
0.435
0.661

0.393
0.000
0.427
0.830

Contribution to Var(X̄) (×10−3 )
σ̂α2 /n
19.13
11.03
σ̂β2 /nm
3.33
2.97
σ̂γ2 · FPC/K
946.50 502.50
σ̂ε2 /nmK
18.57
14.12

7.92
0.94
339.00
7.05

5.11
0.00
435.40
8.27

4.92
0.00
426.60
10.38

(b) MindEval (n=50)

0.50

t4
ne

on

eS

ud
Cla

Ge

mi

ni

3F

las

2
T-5
.

70
B

GP

3.3

ma

Lla

Qw

en

2.5

7B

Claude Sonnet 4.6 -0.739 -0.551 -0.536 -0.536 +0.412

Qwen

µ̂θ (mean score)

0.75

Judge bias

Judge model

Qwen 2.5 7B +0.780 +0.298 +0.104 +0.053 -0.566

Component

Evaluated model

Component

Qwen

Llama

GPT

Gemini

Claude

µ̂θ (mean score)

2.478

3.400

3.931

3.846

4.431
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bc4458a-b4ab-406a-a401-3477c552bea3",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "a744e5363d82fb6b7",
  "type": "user",
  "uuid": "9737a53e-ad5f-472f-851d-f890e6680cf5",
  "sourceToolAssistantUUID": "9bc4458a-b4ab-406a-a401-3477c552bea3",
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

_source line 32 · 2026-05-21T16:40:09.564Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01V7sjqsztFGsnc8Wbp49kNW`</summary>

```json
{
  "command": "pdftotext /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/webfetch-1779381574471-asmire.pdf - 2>/dev/null | tail -n +1100 | head -500",
  "description": "Extract appendices from the PDF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9737a53e-ad5f-472f-851d-f890e6680cf5",
  "isSidechain": true,
  "agentId": "a744e5363d82fb6b7",
  "requestId": "req_011CbG3ZTVsWnXYa5yiwqVDc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbc7ac3c-9a76-4a52-93c9-40886a3315eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Ugo4pSNb5Q3o23Hwfsc8rc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3580,
      "cache_read_input_tokens": 31031,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3580
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 31031,
          "cache_creation_input_tokens": 3580,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3580,
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

_source line 33 · 2026-05-21T16:40:09.734Z_

<details><summary>↩ Tool result · `toolu_01V7sjqsztFGsnc8Wbp49kNW`</summary>

```text
Per-observation variance
σ̂α2 (scenario)
0.034
0.100
σ̂β2 (generation)
σ̂γ2 (judge)
0.523
σ̂ε2 (residual)
0.159

0.014
0.019
0.280
0.069

0.021
0.047
0.132
0.207

0.015
0.016
0.150
0.103

0.005
0.002
0.155
0.061

Contribution to Var(X̄) (×10−3 )
0.67
0.28
σ̂α2 /n
σ̂β2 /nm
2.01
0.38
σ̂γ2 · FPC/K
522.50 280.20
σ̂ε2 /nmK
3.18
1.37

0.43
0.93
132.00
4.14

0.29
0.31
150.20
2.05

0.09
0.04
154.80
1.23

(b) MindEval

Figure 2: Estimated judge biases γ̂ℓ = X̄··ℓ − X̄··· for
each judge–model pair.

judges:

is smaller than the residual mean square. Because
a variance is non-negative by definition, negative
estimates are set to zero—the standard truncation
convention for ANOVA-based variance component
estimation (Searle et al., 1992). These zeros, therefore, indicate that generation-to-generation variability is negligible relative to residual noise for
these models, not that it is exactly absent.

X̄ij· =

C

The judge bias mean γ̄ is the same for every
(i, j) cell because the same SJ evaluates all cells
(crossed design).

1 X
Xijℓ
K
ℓ∈SJ

= µθ + αi + βij +

1 X
1 X
γℓ +
εijℓ
K
K
ℓ∈S
ℓ∈S
| {z J } | {zJ }
γ̄

ε̄ij

(6)

Proof of Proposition 1

We prove the variance decomposition in three steps:
(1) grand mean decomposition, (2) law of total
variance, and (3) finite population correction for
judge bias.

Average over m generations within scenario i.
m

1 X
1 X
X̄i·· = µθ + αi +
βij +γ̄ +
εijℓ
m
mK
j=1
j,ℓ
| {z }
|
{z
}

Step 1: Grand mean decomposition. Starting
from Xijℓ = µθ + αi + βij + γℓ + εijℓ , we average
hierarchically.
Average over K judges within generation (i, j).
The terms µθ , αi , and βij are constant across

β̄i

ε̄i·

(7)
7

For i ̸= j, the joint selection probability is
Pr(Zi =1, Zj =1) = Pk(k−1)
(P −1) , giving:

Average over n scenarios.
n

1X
1 X
X̄ = µθ + γ̄ +
αi +
βij
n
nm
i=1
i,j
| {z } | {z }
ᾱ

+

Cov(Zi , Zj ) = E[Zi Zj ] − E[Zi ] E[Zj ]
k(P −k)
k2
k(k−1)
− 2 =− 2
P (P −1) P
P (P −1)
(14)
P
Since T =
i Zi ai and the ai are constants,
expanding the variance gives:
=

β̄

1 X
εijℓ
nmK
i,j,ℓ
{z
}
|

(8)

ε̄

Step 2: Law of total variance. Let S denote the
judge selection. By the law of total variance:



Var(X̄) = E Var(X̄ | S) +Var E[X̄ | S] (9)

Var(T )
=

Var(X̄ | S) =

n

+

σβ2
nm

+

σε2
nmK

a2i Var(Zi ) + 2

X

i=1

Conditioning on S:
Term (I): Conditional variance. Given S, the
bias γ̄ is a constant. The remaining randomness
comes from ᾱ, β̄, ε̄, which are means of mutually
independent zero-mean random variables:
σα2

P
X

ai aj Cov(Zi , Zj )

i<j

X
k(P −k) X 2
k(P −k)
=
ai − 2
·2
ai aj
2
P
P (P −1)
i

i<j

(15)
each factor. By definition,
PWe2 now simplify
2 . For the cross-term, the centering
a
=
P
σ
i i
Pa
constraint i ai = 0 implies:
X 2 X
X
0=
ai =
a2i + 2
ai aj

(10)

This does not depend on S, so E[Var(X̄ | S)]
equals the same expression.
Term (II): Variance of conditional mean. Since
E[αi ] = E[βij ] = E[εijℓ ] = 0:

E[X̄ | S] = µθ +γ̄ =⇒ Var E[X̄ | S] = Var(γ̄)
(11)

i

i

i<j

X
=⇒ 2
ai aj = −P σa2

(16)

i<j

Substituting both identities into (15) (the two
negatives in the second term yield a positive contribution):

Step 3: Finite population correction. γ̄ is a sample mean of K values drawn without replacement
from the centered population {γ1 , . . . , γKtot }.

k(P −k)
k(P −k)
· P σa2 + 2
· P σa2
2
P
P (P −1)
k(P −k) σa2
=
(17)
P −1

Var(T ) =

Lemma 2 (Finite P
population correction). Let
2 =
a1 , . .P
. , aP satisfy
i ai = 0 with σa
P −1 i a2i . If S is a simple random sample of
size k drawn without replacement:
!
1X
σ2 P − k
Var
ai = a ·
(12)
k
k P −1

Finally, dividing by k 2 :
Var(āS ) =

Var(T )
σa2 P −k
=
·
k2
k P −1

(18)

i∈S

The FPC factor equals 1 when k = 1 and 0 when
k = P (offsets cancel exactly). Applying to judge
biases (aℓ = γℓ , P = Ktot , k = K):

Proof. Define indicator variables Zi ∈ {0, 1} for
i = 1, . . . , P , where Zi = 1 if and only if element
i is selected
PP in the sample S. The sample sum is
T =
i=1 Zi ai , and the sample mean is āS =
T /k.
Under simple random sampling without replacement (SRSWOR) of size k from P elements, each
element is selected with probability Pr(Zi = 1) =
k/P , so:


k
k
k(P −k)
Var(Zi ) =
1−
=
(13)
P
P
P2

σγ2 Ktot − K
Var(γ̄) =
·
K Ktot − 1

(19)

Combining Terms (I) and (II) completes the
proof.

D

Estimation of Variance Components

Because judges are crossed (not nested), we use a
crossed ANOVA.
8

Residual noise. The residual mean square estimates σε2 :

Strategy B: Random single judge per generation.
Budget B = m, each generation scored by ℓj ∼
Uniform({1, . . . , Ktot }). Per-scenario mean:

σ̂ε2 = MSW
P
=

2
i,j,ℓ (Xijℓ − X̄ij· − X̄··ℓ + X̄··· )

(nm − 1)(K − 1)

X̄i = µθ + αi +

(20)

j

Generation variance. The between-generation
mean square:
X
K
MSG =
(X̄ij· − X̄i·· )2
(21)
n(m − 1)

Each term in the sum is independent with variance
σβ2 + σγ2 + σε2 :
VB =

i,j

with E[MSG ] = σε2 + Kσβ2 . Judge bias drops out
because the same judges evaluate every generation
within a scenario.

with E[MSS ] = σε2 + Kσβ2 + mK σα2 .

(23)
(24)

m

K

j=1

ℓ=1

Judge bias. We estimate γ̂ℓ = X̄··ℓ − X̄··· and
compute:
σ̂ 2 Ktot − 1
1 X 2
σ̂γ2 =
γ̂ℓ − ε ·
(25)
Ktot
nm
Ktot

VA − VC =
VB − V C =

ℓ

Allocation Strategy Derivations
VA − V B =

We derive the benchmark score variance for each
strategy. The n scenarios are fixed, so σα2 /n contributes a constant offset and is excluded.

F

(Ktot − 1)σβ2
nB

≥0

σγ2
≥0
nB
(Ktot − 1)σβ2 − σγ2
nB

(32)
(33)
(34)

Scenario Coverage

The strategies above fix n and optimize the perscenario budget. A complementary question is how
to split a total generation budget Bgen = nm between scenarios and generations per scenario. Under cycling, substituting n = Bgen /m into Eq. 5
gives:

Strategy A: All Ktot judges per generation.
Budget B = mKtot , so m = B/Ktot . Per-scenario
mean:
1 X
1 X
βij +
γℓ
X̄i = µθ + αi +
m
Ktot
j
ℓ
| {z }
=0

1 X
εijℓ
+
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbc7ac3c-9a76-4a52-93c9-40886a3315eb",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "a744e5363d82fb6b7",
  "type": "user",
  "uuid": "ac7eae1c-8148-4c87-9998-8612b7ee09dc",
  "sourceToolAssistantUUID": "fbc7ac3c-9a76-4a52-93c9-40886a3315eb",
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

_source line 34 · 2026-05-21T16:40:16.748Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0172gaBMXcWVxDQyUkjHGhUF`</summary>

```json
{
  "command": "pdftotext /home/ubuntu/.claire-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/webfetch-1779381574471-asmire.pdf - 2>/dev/null | tail -n +1600 | head -400 || pdftotext /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/webfetch-1779381574471-asmire.pdf - 2>/dev/null | tail -n +1600 | head -400",
  "description": "Extract remaining appendix sections from PDF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac7eae1c-8148-4c87-9998-8612b7ee09dc",
  "isSidechain": true,
  "agentId": "a744e5363d82fb6b7",
  "requestId": "req_011CbG3ZvY4mwGrY8oGP6K7h",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7b63240-4182-4751-afb7-64c65b46d0dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011BgyZ51rNLHabs9WQ4bmAJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3051,
      "cache_read_input_tokens": 34611,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3051
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 318,
          "cache_read_input_tokens": 34611,
          "cache_creation_input_tokens": 3051,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3051,
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

_source line 35 · 2026-05-21T16:40:16.925Z_

<details><summary>↩ Tool result · `toolu_0172gaBMXcWVxDQyUkjHGhUF`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7b63240-4182-4751-afb7-64c65b46d0dc",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "a744e5363d82fb6b7",
  "type": "user",
  "uuid": "2a6e53d5-f3d4-440e-888a-062721ba1d8c",
  "sourceToolAssistantUUID": "f7b63240-4182-4751-afb7-64c65b46d0dc",
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

_source line 36 · 2026-05-21T16:40:19.563Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018jbzq92PrVxoxLcZfKeCAv`</summary>

```json
{
  "command": "pdftotext /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/webfetch-1779381574471-asmire.pdf - 2>/dev/null | wc -l",
  "description": "Check total line count of extracted PDF text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a6e53d5-f3d4-440e-888a-062721ba1d8c",
  "isSidechain": true,
  "agentId": "a744e5363d82fb6b7",
  "requestId": "req_011CbG3aTVehE5eTBzajfdpb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65a5146c-b43b-40be-a80a-9fc002c2905b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LALZxxTvpRycTnCz7gXL82",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 336,
      "cache_read_input_tokens": 37662,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 336
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 37662,
          "cache_creation_input_tokens": 336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 336,
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

_source line 37 · 2026-05-21T16:40:19.732Z_

<details><summary>↩ Tool result · `toolu_018jbzq92PrVxoxLcZfKeCAv`</summary>

```text
1869
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65a5146c-b43b-40be-a80a-9fc002c2905b",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "a744e5363d82fb6b7",
  "type": "user",
  "uuid": "1088c426-27ab-4387-8884-1f9ad18adb06",
  "sourceToolAssistantUUID": "65a5146c-b43b-40be-a80a-9fc002c2905b",
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

_source line 38 · 2026-05-21T16:40:22.360Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014VxF3Zop7b7jjScvqBKt2B`</summary>

```json
{
  "command": "pdftotext /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/webfetch-1779381574471-asmire.pdf - 2>/dev/null | sed -n '1600,1869p'",
  "description": "Extract final section of PDF text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1088c426-27ab-4387-8884-1f9ad18adb06",
  "isSidechain": true,
  "agentId": "a744e5363d82fb6b7",
  "requestId": "req_011CbG3afH51YJh7XDiSBbP4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82b002ac-255c-4fd7-a0e7-ad1b329f238f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Kgrp61MSjeXabn24CC74LW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 203,
      "cache_read_input_tokens": 37998,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 203
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 37998,
          "cache_creation_input_tokens": 203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 203,
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

_source line 39 · 2026-05-21T16:40:22.539Z_

<details><summary>↩ Tool result · `toolu_014VxF3Zop7b7jjScvqBKt2B`</summary>

```text
mKtot

(30)

The residuals for different j are independent with
variance σε2 :
σβ2 + σε2
VC =
(31)
nB
Pairwise comparisons. Direct subtraction
yields:

Method-of-moments estimators.
σ̂α2 = (MSS − MSG )/(mK)

(29)

nB

tot
1 X
1 X
γj mod Ktot =
γℓ = 0
m
Ktot

i

σ̂β2 = (MSG − MSW )/K

σβ2 + σγ2 + σε2

Strategy C: Round-robin cycling. Budget B =
m (multiple of Ktot ), generation j scored by judge
j mod Ktot . Each judge appears m/Ktot times, so
the panel-relative offsets average to zero:

Scenario variance. The between-scenario mean
square:
mK X
MSS =
(X̄i·· − X̄··· )2
(22)
n−1

E


1 X
βij + γℓj + εijℓj (28)
m

VC (Bgen , m) =

(26)

m σα2 + σβ2 + σε2
Bgen

(35)

j,ℓ

This is linear in m with positive slope σα2 /Bgen ,
so variance is minimized at m = 1, maximizing
the number of distinct scenarios up to the dataset
size N . The same monotonicity holds for Strategies A and B. Once the scenario pool is exhausted
(n = N ), excess budget should go to additional
generations.

The judge offsets sum to zero by the centering
constraint, so the score equals the panel-mean estimand. The benchmark variance from generation
and residual noise:
!
2
Ktot σβ2 + σε2
1 σβ
σε2
VA =
+
=
(27)
n m
mKtot
nB
9

G

Table 4: ANOVA F -statistic for the judge main effect.
All p < 0.001.

Exact Bootstrap Predictions

The allocation formulas in §3.3 assume infinitepopulation generation draws. When validating
via bootstrap subsampling from a finite pool of
mmax observed generations, we compute exact predictions using the empirical pool variances. For
all three strategies, the subsampling observations
within each scenario are i.i.d. draws from the relevant pool, so V (B) = C/(nB) where C is the
pool variance.

Model
Qwen 2.5 7B
Llama 3.3 70B
GPT-5.2
Gemini 3 Flash
Claude Sonnet 4.6

Strategy A. Each draw is a generation-level
mean X̄ig· , with m = B/Ktot draws per scenario.
The pool variance is:
1X 1 X
(X̄ig· − X̄i·· )2 (36)
CA = Ktot ·
n
mmax g

I

Strategy B. Each draw is a single cell Xigℓ with
generation and judge chosen uniformly at random,
with m = B draws per scenario:
X
1X
1
CB =
(Xigℓ − X̄i·· )2 (37)
n
mmax Ktot

638.2
445.8
601.7
659.2
514.9

1029.5
1280.1
200.1
458.0
788.9

Omitted Interactions

Scenario–generation. Because generations are
nested within scenarios rather than crossed with
them, there is no separable scenario–generation interaction: any such effect is already confounded
with the generation main effect βij , which captures
all within-scenario generation variability by construction.

g,ℓ

Strategy C. Each judge ℓ gets B/Ktot independent draws from its column; the per-scenario mean
averages these Ktot independent sub-means. The
relevant pool variance is the within-column generation variance:
1 X 1 X
CC =
(Xigℓ − X̄i·ℓ )2 (38)
nKtot
mmax g

Scenario–judge. This interaction captures the extent to which a judge’s bias varies across scenarios
(e.g., a judge being lenient on reasoning tasks but
strict on creative ones). It is in principle estimable,
but explicitly modeling it would add n(Ktot −1)
parameters and complicate the closed-form variance decomposition without changing the allocation analysis: the interaction enters only through
the per-cell residual variance, which our empirical
predictions (§4) already capture without parametric
assumptions on its structure.

i,ℓ

These empirical constants converge to the population formulas (Eqs. 3–5) as mmax → ∞, but
for finite mmax they account for the bias in plugin variance estimates (the (mmax −1)/mmax correction) and the fact that the crossed ANOVA residual
uses global judge centering while CC uses withinscenario-judge centering.

H

MindEval
F (4, 996)

A full factorial design with three facets (scenario,
generation, judge) has 23 = 8 terms: a grand mean,
three main effects, three two-way interactions, and
one three-way interaction. Our model (Eq. 1) retains the grand mean and three main effects, absorbing all interaction terms into the residual εijℓ .
We enumerate each omitted interaction below.

i

i

MT-Bench
F (4, 3196)

ANOVA F -Test for Judge Effects

We test for a systematic judge effect using a twoway crossed ANOVA that treats each scenario–
generation pair as a subject crossed with
PKK judges.
The judge sum of squares SSJ = N ℓ=1 (X̄··ℓ −
X̄··· )2 (where N = nm) is compared to the
residual SSR = SST − SSJ − SSS , yielding
F = MSJ /MSR with K−1 and (N −1)(K−1)
degrees of freedom. The p-value is the survival function of the F -distribution, computed via
scipy.stats.f.sf. Table 4 reports results for
both benchmarks; in all cases, the null hypothesis
of no judge effect is rejected at p < 0.001.

Generation–judge. This interaction reflects
judge-specific reactions to particular generation artifacts (e.g., one judge penalizing verbose outputs
more than another). Since generations are independent stochastic draws, this term is exchangeable
across j and acts as additional i.i.d. noise on each
cell, making it naturally absorbed into σε2 .

J

Judge Hyperparameter Settings

For all judge calls we follow the default decoding
hyperparameters specified by the MT-Bench and
10

MindEval reference implementations, summarized
in Table 5. For models in our judge pool that fall
outside the original API tables of either reference
implementation (e.g., Gemini 3 Flash and Claude
Sonnet 4.6 for MT-Bench), we apply the closest
equivalent setting supported by the provider.
Table 5: Default judge decoding hyperparameters used
by each benchmark’s reference implementation.

Parameter

Default

MT-Bench
temperature
max_tokens (OpenAI)
max_tokens (Anthropic)

0
2048
1024

MindEval
judge_template_version
max_completion_tokens
reasoning_effort

v0_1
16,000
high

Effect of hyperparameters. Decoding hyperparameters such as temperature, top-p, and reasoning
effort primarily control the within-judge stochasticity of a single scoring call. In the model of Eq. 1,
this stochasticity is absorbed into the residual εijℓ ,
contributing to σε2 . The systematic offset γℓ , by
contrast, is a property of the judge model itself, not
of how its outputs are sampled. Increasing temperature would inflate σε2 but, to first order, leave γℓ
and σγ2 unchanged. At the default operating point,
the judge-offset contribution exceeds the residual
contribution by roughly two orders of magnitude
on both benchmarks (Table 3). Reasonable perturbations of the decoding hyperparameters can only
shift σε2 within a window that is much smaller than
σγ2 , so the qualitative ranking of allocation strategies in §3.3 and Figure 1 is robust to this choice.

11
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82b002ac-255c-4fd7-a0e7-ad1b329f238f",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "a744e5363d82fb6b7",
  "type": "user",
  "uuid": "b84f8b96-6ddd-4717-b62c-7624b474d7fc",
  "sourceToolAssistantUUID": "82b002ac-255c-4fd7-a0e7-ad1b329f238f",
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

_source line 40 · 2026-05-21T16:43:30.829Z_

I now have the complete text of the paper. Here is all extracted content:

---

## CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation

**arXiv:** 2603.01865v3 (submitted March 2, 2026; updated May 4, 2026)
**Authors:** Ziyi Zhu¹, Olivier Tieleman¹, Alexey Bukhtiyarov¹, Jinghong Chen²
**Affiliations:** ¹Slingshot AI, ²Department of Engineering, University of Cambridge
**Correspondence:** ziyi@slingshotai.com

---

## Abstract (verbatim)

LLM-as-judge evaluation has become standard practice for open-ended model assessment; however, judges exhibit systematic biases that cannot be averaged out by increasing the number of scenarios or generations. These biases are often similar in magnitude to the model differences that benchmarks are designed to detect, resulting in unreliable rankings when single-judge evaluations are used. We introduce a variance decomposition that partitions benchmark score variance into scenario, generation, judge, and residual components. Based on this analysis, CyclicJudge, a round-robin assignment of judges to scenarios, is demonstrated to be the optimal strategy for a fixed judge panel and judge-call budget: the score recovers the panel mean exactly while matching the cost of single-judge evaluation. Empirical results on MT-Bench and MindEval validate the effectiveness of CyclicJudge as predicted, across both general-purpose and domain-specific evaluation settings.

---

## Section 1: Introduction (verbatim)

LLM-as-judge evaluation has become the de facto standard for open-ended model assessment (Zheng et al., 2023). A growing body of work indicates that LLM judges are systematically biased: some models are consistently lenient, others strict, with additional position, verbosity, and self-preference effects (Zheng et al., 2023; Shi et al., 2024; Wang et al., 2024). A standard Analysis of Variance (ANOVA; Fisher, 1925) on our data confirms that judge main effect is highly significant (§4.2).

Crucially, systematic bias does not average away across more scenarios or generations: reducing them requires aggregating across multiple judges. Yet running every judge on every item multiplies evaluation cost by the panel size and sacrifices generation diversity at a fixed budget. Throughout this work, we treat the mean score of a diverse K_tot-judge panel as the reference for evaluation; our goal is to recover this panel mean efficiently.

We show that CyclicJudge, a round-robin assignment of judges to items, resolves this tension. To establish this formally, we develop a variance decomposition rooted in generalizability theory (Brennan, 2001; Shavelson and Webb, 1991) that separates benchmark score variance into scenario, generation, judge, and residual components.

**Our contributions are:**

1. A mixed-effects model that decomposes benchmark variance into random noise and panel-relative judge offsets, showing they require fundamentally different remedies (§3.1–3.2).
2. A proof that round-robin cycling achieves lower variance than alternative strategies: it cancels the panel-relative offsets exactly while maximizing generation diversity at any budget (§3.3).
3. Empirical results on MT-Bench and MindEval validating the effectiveness of CyclicJudge as predicted, across both general-purpose and domain-specific evaluation settings (§4).

---

## Section 2: Related Work (verbatim)

**LLM judge biases and multi-judge approaches.** LLM judges exhibit systematic position bias (Wang et al., 2024; Shi et al., 2024), length bias (Dubois et al., 2024), self-preference (Wataoka et al., 2024), and cognitive biases (Koo et al., 2024); we refer readers to Gu et al. (2024) for a comprehensive survey. Multi-judge panels mitigate these biases by averaging over diverse judge tendencies (Verga et al., 2024), while psychometric reliability analyses further demonstrate that single-judge evaluations yield insufficiently stable scores (Schroeder and Wood-Doughty, 2024).

**Benchmark reliability and generation variance.** Madaan et al. (2025) empirically quantifies variance across hundreds of models and benchmarks, and Alvarado Gonzalez et al. (2025) shows via ANOVA that unrepeated evaluations frequently produce rank inversions across benchmark subcategories. Zhang et al. (2025) proposes a hierarchical model decomposing variance into within-prompt and between-prompt components, and Mizrahi et al. (2024) shows that prompt paraphrasing alone can reverse model rankings. Our work extends this line by further separating systematic judge bias from random noise.

**Budget-constrained evaluation.** Saha et al. (2026) frames judge selection as a multi-armed bandit problem, Luettgau et al. (2025) applies hierarchical Bayesian partial pooling in low-data regimes, and Miller (2024) derives standard errors and power formulas for benchmark scores; Dorner et al. (2025) further establishes fundamental scaling limits on the accuracy gains from additional judge queries.

---

## Section 3: Methodology (verbatim)

### 3.1 Model Specification

Consider evaluating model θ on n scenarios from a dataset D of N total scenarios, with m independent generations per scenario, each scored by K judges drawn from a pool of K_tot. The same K judges score every scenario–generation cell (a crossed design). We model each score as:

**X_ijℓ = μ_θ + α_i + β_ij + γ_ℓ + ε_ijℓ** (Eq. 1)

where i ∈ {1, …, n} indexes scenarios, j ∈ {1, …, m} indexes generations within scenario i, and ℓ indexes the K selected judges. Each term has a distinct source:

- **μ_θ**: panel-mean estimand for model θ—the average score the K_tot-judge panel would assign in expectation, with random noise removed.
- **α_i ~ iid (0, σ_α²)**: scenario effect—how much individual scenario difficulty varies for model θ. A dataset whose scenarios all test the same aspects of model θ equally has σ_α² = 0.
- **β_ij ~ iid (0, σ_β²)**: generation effect—variability from stochastic decoding. σ_β² is model-specific; a deterministic model has σ_β² = 0.
- **γ_ℓ**: judge offset relative to the panel mean—a fixed constant for each judge, with centering constraint Σγ_ℓ = 0 and population dispersion σ_γ² = K_tot⁻¹ Σ γ_ℓ². γ_ℓ measures deviation from the panel reference, not from absolute truth: bias shared by all panel members is absorbed into μ_θ.
- **ε_ijℓ ~ iid (0, σ_ε²)**: residual—captures judge-level noise and all interaction terms.

The random effects (α, β, ε) are mutually independent with finite second moments; no distributional assumptions (e.g. Gaussianity) are needed. The n scenarios and K judges are each drawn by simple random sampling without replacement, independently of each other and of all random effects.

### 3.2 Variance Decomposition

The benchmark score is the grand mean X̄ = (1/nmK) Σ X_ijℓ, which decomposes as X̄ = μ_θ + ᾱ + β̄ + γ̄ + ε̄.

**Proposition 1 (Variance decomposition):**

Var(X̄) = [σ_α²/n + σ_β²/nm + σ_ε²/nmK] + [σ_γ²/K · (K_tot − K)/(K_tot − 1)]
           |___________ random noise ____________|   |________ V_γ: judge bias ________|   (Eq. 2)

Each noise term shrinks with more data at or above its hierarchy level. The bias term V_γ responds only to K and vanishes exactly at K = K_tot. The proof uses the law of total variance, conditioning on the judge selection, combined with a finite population correction for sampling K from K_tot centered bias values (Appendix C).

### 3.3 Allocation Strategies

Given a per-scenario budget of B judge calls, the design question is how to allocate judges across generations. The scenario term σ_α²/n is fixed once scenarios are chosen; we compare three strategies for the remaining variance.

**Strategy A: All judges per generation.** Use all K_tot judges for each of m = B/K_tot generations. The mean of all judge offsets is zero (γ̄ = 0):

V_A(B) = (K_tot σ_β² + σ_ε²) / nB   (Eq. 3)

**Strategy B: Random single judge per generation.** Use m = B generations, each scored by one randomly sampled judge. Random judge selection injects the panel-relative offset as additional sampling noise:

V_B(B) = (σ_β² + σ_γ² + σ_ε²) / nB   (Eq. 4)

**Strategy C: CyclicJudge (round-robin).** Use m = B generations, assigning judge j mod K_tot to generation j. Each judge appears equally often, so the panel-relative offsets sum to zero (γ̄ = 0):

V_C(B) = (σ_β² + σ_ε²) / nB   (Eq. 5)

With one generation per scenario (m = 1), the same variance and offset cancellation is achieved by cycling judges across scenarios instead. In this case scenarios should be shuffled before assignment to avoid confounding the cycle with any latent ordering of the dataset.

**Advantage of CyclicJudge.** Direct comparison (Appendix E) shows V_C ≤ min(V_A, V_B) for all B, with gaps of O(1/B), so CyclicJudge's advantage is largest at small budgets of judge calls. The ranking of A vs. B depends on whether (K_tot − 1)σ_β² ≷ σ_γ²: all judges beat random only when judge bias is large relative to generation variance.

---

## Section 4: Experiments (verbatim)

### 4.1 Domain and Data

We validate our approach on two benchmarks:

**MT-Bench** (Zheng et al., 2023) is a general-purpose multi-turn conversational benchmark with 80 two-turn questions spanning 8 categories, scored on a 1–10 scale per turn (averaged).

**MindEval** (Pombal et al., 2025) is a domain-specific benchmark for multi-turn mental health support with 50 scenarios and composite scores on a 1–5 scale covering empathy, safety, and clinical appropriateness. Each scenario simulates a full 10-turn therapeutic session with a synthetic patient.

For both benchmarks, we evaluate five models—Qwen 2.5 7B Instruct (Yang et al., 2024), Llama 3.3 70B Instruct (Grattafiori et al., 2024), GPT-5.2, Gemini 3 Flash, and Claude Sonnet 4.6, which also serve as judges in a symmetric design. MT-Bench uses m=10 generations per scenario (4,000 scores per model); MindEval uses m=5 (1,250 scores per model). We follow the default judge decoding hyperparameters from reference (Appendix J).

### 4.2 Judge Bias Estimates

As a complementary omnibus check on the mixed-effects decomposition (§3.1), we test whether judge identity has a significant effect using a two-way ANOVA, treating each scenario–generation pair as a subject crossed with K judges. On both benchmarks, the judge main effect is highly significant (p < 0.001 in all cases; see Appendix H).

Table 1 demonstrates that single-judge evaluation produces unreliable rankings. On MT-Bench at the default operating point (m=1, K=1), the top-ranked model changes with every judge, with Qwen ranking itself first despite being last by consensus, a pattern consistent with the self-preference bias documented by Wataoka et al. (2024). The per-observation variance estimates (Table 2) confirm this quantitatively: judge variance σ̂_γ² ranges from 0.34 to 0.95 across models. Since competitive models on current leaderboards are routinely separated by < 0.5 points (Chiang et al., 2024), single-judge evaluation can easily reverse rankings. On MindEval, rankings are also notably more stable across single judges: four of five produce an identical ordering. Two plausible factors include: domain-specific rubrics may leave less room for stylistic self-preference, and the markedly lower scenario and generation variance on MindEval (§4.3) compresses the absolute size of any model-dependent fluctuations.

### 4.3 Variance Components

Table 2 reports the per-observation variance component estimates via crossed ANOVA (see Appendix D). On MT-Bench, scenario variance σ̂_α² is the largest per-observation component; maximizing the number of distinct scenarios always reduces total variance (Appendix F). Generation variance σ̂_β² drops with capability, consistent with the observation that stronger models produce more deterministic outputs. As frontier models increasingly rely on RL post-training, generation variance may shrink further (Matsutani et al., 2025). The judge offset variance σ̂_γ² remains substantial for all models, accounting for >94% of benchmark variance at the default operating point (see Appendix B).

On MindEval, both scenario and generation variance are markedly lower. Scenario variance σ̂_α² drops by one to two orders of magnitude because all MindEval scenarios evaluate the same rubrics across different user profiles, so difficulty varies far less than on MT-Bench. Generation variance is similarly suppressed: each MindEval generation is a full 10-turn therapeutic session, so per-response decoding randomness averages out over many turns. The judge offset variance remains the dominant component throughout, exceeding both scenario and generation variance by an order of magnitude.

### 4.4 Strategy Comparison

Figure 1 validates the three allocation strategies via 5,000 subsampling repetitions at each budget level on both benchmarks. Markers show empirical variance; dashed lines show exact predictions from empirical pool variances (Appendix G). CyclicJudge achieves lower variance everywhere on both benchmarks, and predictions match empirical results precisely. At B=5, switching from random to cycling cuts variance by ~27–40% across models on MT-Bench.

The optimal strategy among the two alternatives depends on the sign of (K_tot − 1)σ_β² − σ_γ²: all-judges wins when σ_γ²/σ_β² > K_tot − 1 = 4. On MT-Bench, this ratio is below the threshold for Qwen (3.6) and Llama (2.1), so random judging is preferable; for Gemini and Claude (σ̂_β² ≈ 0), all-judges converges to CyclicJudge. On MindEval, the ratio exceeds the threshold for nearly every model, so all-judges consistently outperforms random. The driver is not a larger judge offset variance, but rather a sharply lower generation variance σ̂_β². Meanwhile, judges' disagreement over subjective clinical criteria keeps σ̂_γ² substantial relative to σ̂_β². CyclicJudge outperforms both alternatives regardless of this ratio.

---

## Section 5: Conclusion (verbatim)

We develop a variance decomposition for LLM-as-judge evaluation that separates systematic between-judge offsets from random noise and use it to derive CyclicJudge, a round-robin judge assignment strategy. Our analysis and experiments on both a general-purpose benchmark (MT-Bench) and a domain-specific clinical benchmark (MindEval) yield three main findings: (1) Systematic judge offsets dominate benchmark score variance at default operating points. (2) Random noise components decrease with model capability and multi-turn evaluation, but the panel-relative offset variance does not. (3) CyclicJudge achieves the lowest variance among all allocation strategies at every budget level, regardless of the model's variance profile, by recovering the panel-mean score exactly while maximizing generation diversity. The method requires no model-specific tuning and maintains the same per-item cost as single-judge evaluation, providing practitioners with a cost-neutral drop-in replacement for more reliable LLM evaluation.

---

## Limitations (verbatim)

**Panel-mean reference.** Our analysis treats the mean score of the K_tot-judge panel as the reference for evaluation. A diverse panel drawn from disjoint model families typically correlates more strongly with human judgments than any single judge (Verga et al., 2024), but the panel mean is not a substitute for absolute ground truth. Biases shared across the panel members are absorbed into μ_θ and propagate into the panel mean. CyclicJudge addresses the within-panel offsets between individual judges, not biases that all panel members share; calibrating the panel itself against human or expert references is complementary work.

**Linear model approximation.** Our variance decomposition assumes a linear random effects model, which treats scores as unbounded and continuous. LLM-as-judge scores are in fact bounded ordinal variables, so the linear model can produce boundary artifacts and heteroscedastic residuals near the scale endpoints. A generalized linear mixed model (GLMM), such as a cumulative-link mixed model, would properly account for the ordinal, bounded nature of the responses. However, GLMMs do not yield the closed-form variance decomposition that our allocation analysis relies on. We therefore retain the linear approximation, noting that it remains reasonable when the scale range is large relative to the observed score dispersion, as in our benchmarks.

**Judge pool size.** Our judge pool of K_tot = 5 limits exploration of larger panels. While the theoretical results generalize to arbitrary K, empirical validation with larger and more diverse judge pools would strengthen the practical recommendations.

**Scenario exchangeability.** The "maximize scenarios" recommendation assumes scenarios are interchangeable draws from the dataset; in practice, some scenarios may be more informative than others, and item-selection methods (Maia Polo et al., 2024) could alter the tradeoff.

**Balanced design assumption.** The allocation analysis assumes a balanced design in which every scenario receives the same number of judge calls. Extensions to adaptive or sequential designs remain future work.

**Uniform cost assumption.** Our budget analysis treats all judge calls as equal cost; in practice, judges vary widely in price and latency. A cost-weighted allocation that accounts for per-model pricing and inference speed would be needed for real deployment decisions.

---

## Figure and Table Captions (verbatim)

**Figure 1:** Benchmark score variance Var(X̄) vs. per-scenario budget for three strategies: all judges (A), random single judge (B), and CyclicJudge (C). [Two panels: (a) MT-Bench (1–10 scale, n=80, m_max=10); (b) MindEval (1–5 scale, n=50, m_max=5). Five subplots per panel, one per model: Qwen 2.5 7B, Llama 3.3 70B, GPT-5.2, Gemini 3 Flash, Claude Sonnet 4.6. Markers show empirical variance; dashed lines show exact predictions.]

**Figure 2:** Estimated judge biases γ̂_ℓ = X̄_··ℓ − X̄_··· for each judge–model pair. [Heatmap panels: (a) MT-Bench; (b) MindEval. Rows = judge models, columns = evaluated models.]

**Table 1:** Mean score ± 95% CI at the default operating point (m=1, K=1). Bold: highest score per judge column. Underline: second highest.
- Panel (a): MT-Bench (1–10 scale, n=80) — 5×5 matrix of judge × model
- Panel (b): MindEval (1–5 scale, n=50) — 5×5 matrix of judge × model

**Table 2:** Per-observation variance component estimates.
- Panel (a): MT-Bench (n=80) — rows: σ̂_α², σ̂_β², σ̂_γ², σ̂_ε²; columns: Qwen, Llama, GPT, Gemini, Claude
- Panel (b): MindEval (n=50)

**Table 3:** Variance component estimates. Per-observation variances and their contribution to Var(X̄) at the default operating point (m=1, K=1).
- Panel (a): MT-Bench — per-observation variance + contribution to Var(X̄) (×10⁻³)
- Panel (b): MindEval — same structure

**Table 4:** ANOVA F-statistic for the judge main effect. All p < 0.001.
- MT-Bench F(4, 3196): Qwen 638.2, Llama 445.8, GPT 601.7, Gemini 659.2, Claude 514.9
- MindEval F(4, 996): Qwen 1029.5, Llama 1280.1, GPT 200.1, Gemini 458.0, Claude 788.9

**Table 5:** Default judge decoding hyperparameters used by each benchmark's reference implementation.
- MT-Bench: temperature=0, max_tokens (OpenAI)=2048, max_tokens (Anthropic)=1024
- MindEval: judge_template_version=v0_1, max_completion_tokens=16,000, reasoning_effort=high

---

## Key Numerical Results

**Table 1a — MT-Bench mean scores (m=1, K=1):**

| Judge\Model | Qwen | Llama | GPT | Gemini | Claude |
|---|---|---|---|---|---|
| Gemini | 8.02±.16 | 7.91±.16 | 7.96±.17 | 7.87±.18 | 8.02±.15 |
| GPT | 8.98±.08 | 8.81±.11 | 9.06±.06 | 8.71±.11 | 8.39±.16 |
| Claude | 8.20±.12 | 8.67±.12 | 7.91±.13 | 6.90±.20 | 6.09±.20 |
| Llama | 9.88±.06 | 9.71±.11 | 9.62±.12 | 8.58±.25 | 7.16±.27 |
| Qwen | 8.68±.10 | 8.49±.13 | 8.52±.13 | 7.26±.22 | 5.99±.23 |

**Panel mean (μ̂_θ) MT-Bench:** Qwen 7.13, Llama 7.87, GPT 8.72, Gemini 8.75, Claude 8.61

**Table 1b — MindEval mean scores:**

| Judge\Model | Qwen | Llama | GPT | Gemini | Claude |
|---|---|---|---|---|---|
| Claude | 3.86±.08 | 4.04±.09 | 3.90±.08 | 3.70±.07 | 3.26±.12 |
| GPT | 4.67±.07 | 4.51±.07 | 4.49±.06 | 4.29±.05 | 3.38±.21 |
| Gemini | 4.05±.06 | 3.76±.09 | 3.63±.05 | 3.16±.06 | 2.32±.08 |
| Llama | 4.72±.06 | 3.95±.16 | 3.91±.12 | 3.00±.10 | 1.69±.08 |
| Qwen | 4.84±.04 | 3.39±.15 | 3.31±.08 | 2.85±.06 | 1.74±.05 |

**Panel mean (μ̂_θ) MindEval:** Qwen 2.478, Llama 3.400, GPT 3.931, Gemini 3.846, Claude 4.431

**Table 2a — MT-Bench variance components:**

| Component | Qwen | Llama | GPT | Gemini | Claude |
|---|---|---|---|---|---|
| σ̂_α² (scenario) | 1.530 | 0.882 | 0.634 | 0.408 | 0.393 |
| σ̂_β² (generation) | 0.266 | 0.238 | 0.076 | 0.000 | 0.000 |
| σ̂_γ² (judge) | 0.947 | 0.503 | 0.339 | 0.435 | 0.427 |
| σ̂_ε² (residual) | 1.486 | 1.130 | 0.564 | 0.661 | 0.830 |

**Table 2b — MindEval variance components:**

| Component | Qwen | Llama | GPT | Gemini | Claude |
|---|---|---|---|---|---|
| σ̂_α² (scenario) | 0.034 | 0.014 | 0.021 | 0.015 | 0.005 |
| σ̂_β² (generation) | 0.100 | 0.019 | 0.047 | 0.016 | 0.002 |
| σ̂_γ² (judge) | 0.523 | 0.280 | 0.132 | 0.150 | 0.155 |
| σ̂_ε² (residual) | 0.159 | 0.069 | 0.207 | 0.103 | 0.061 |

**Table 3a — MT-Bench contribution to Var(X̄) (×10⁻³) at default operating point:**

| Component | Qwen | Llama | GPT | Gemini | Claude |
|---|---|---|---|---|---|
| σ̂_α²/n | 19.13 | 11.03 | 7.92 | 5.11 | 4.92 |
| σ̂_β²/nm | 3.33 | 2.97 | 0.94 | 0.00 | 0.00 |
| σ̂_γ²·FPC/K | 946.50 | 502.50 | 339.00 | 435.40 | 426.60 |
| σ̂_ε²/nmK | 18.57 | 14.12 | 7.05 | 8.27 | 10.38 |

**Table 3b — MindEval contribution to Var(X̄) (×10⁻³):**

| Component | Qwen | Llama | GPT | Gemini | Claude |
|---|---|---|---|---|---|
| σ̂_α²/n | 0.67 | 0.28 | 0.43 | 0.29 | 0.09 |
| σ̂_β²/nm | 2.01 | 0.38 | 0.93 | 0.31 | 0.04 |
| σ̂_γ²·FPC/K | 522.50 | 280.20 | 132.00 | 150.20 | 154.80 |
| σ̂_ε²/nmK | 3.18 | 1.37 | 4.14 | 2.05 | 1.23 |

---

## Appendix A: Judge Bias Estimates (verbatim)

Figure 2 shows the estimated per-judge bias for each judge–model pair on both benchmarks. A pronounced self-preference is visible along the diagonal: on MindEval, Claude Sonnet 4.6's self-bias of +0.412 is the only positive entry in its otherwise uniformly negative row, and Qwen 2.5 7B's self-bias is the largest in its row on both benchmarks. Judge temperament is not stable across benchmarks: Gemini 3 Flash is the most lenient judge on MT-Bench (all biases positive), yet becomes one of the harshest on MindEval, suggesting that judge personality is benchmark-dependent rather than an intrinsic model property. On MT-Bench, strictness correlates with model capability: the two strongest models by consensus (GPT-5.2 and Claude) are the most uniformly negative judges, while the two weakest (Qwen and Llama) are the most lenient. Finally, the harshest judge–model interactions concentrate on capability-mismatched pairs: GPT-5.2 and Claude penalize Qwen by over one full scale point on MT-Bench, while their biases toward each other are an order of magnitude smaller.

**Judge bias matrix (MT-Bench):**

| Judge\Model | Qwen | Llama | GPT | Gemini | Claude |
|---|---|---|---|---|---|
| Qwen 2.5 7B | +0.887 | +0.009 | -0.808 | -0.735 | -0.650 |
| Llama 3.3 70B | +1.257 | +0.848 | +0.091 | +0.224 | +0.446 |
| GPT-5.2 | -1.040 | -0.962 | -0.044 | -0.550 | -0.707 |
| Gemini 3 Flash | +0.032 | +0.711 | +0.991 | +1.132 | +1.003 |
| Claude Sonnet 4.6 | -1.136 | -0.607 | -0.230 | -0.071 | -0.092 |

**Judge bias matrix (MindEval):**

| Judge\Model | Qwen | Llama | GPT | Gemini | Claude |
|---|---|---|---|---|---|
| Qwen 2.5 7B | +0.780 | +0.298 | +0.104 | +0.053 | -0.566 |
| Llama 3.3 70B | +0.904 | +0.891 | +0.580 | +0.641 | +0.239 |
| GPT-5.2 | -0.159 | -0.239 | -0.169 | -0.219 | -0.377 |
| Gemini 3 Flash | -0.786 | -0.399 | +0.021 | +0.061 | +0.293 |
| Claude Sonnet 4.6 | -0.739 | -0.551 | -0.536 | -0.536 | +0.412 |

---

## Appendix B: Variance at Default Operating Point

The judge-offset contribution (σ̂_γ²·FPC/K) accounts for >94% of benchmark variance at the default operating point (m=1, K=1) on MT-Bench. Specifically: for Qwen, 946.50/(946.50+19.13+3.33+18.57) ≈ 96.6%.

---

## Appendix C: Proof of Proposition 1 (Variance Decomposition)

The proof proceeds in three steps: (1) grand mean decomposition, (2) law of total variance, (3) finite population correction.

**Step 1 — Grand mean decomposition:** Starting from X_ijℓ = μ_θ + α_i + β_ij + γ_ℓ + ε_ijℓ, average hierarchically: first over K judges within generation (i,j) — gives X̄_ij· = μ_θ + α_i + β_ij + γ̄ + ε̄_ij; then over m generations within scenario i — gives X̄_i·· = μ_θ + α_i + β̄_i + γ̄ + ε̄_i·; then over n scenarios — gives X̄ = μ_θ + γ̄ + ᾱ + β̄ + ε̄.

**Step 2 — Law of total variance:** Let S denote the judge selection. Var(X̄) = E[Var(X̄|S)] + Var(E[X̄|S]). Given S, γ̄ is constant → Var(X̄|S) = σ_α²/n + σ_β²/nm + σ_ε²/nmK (does not depend on S). E[X̄|S] = μ_θ + γ̄ → Var(E[X̄|S]) = Var(γ̄).

**Step 3 — Finite population correction (Lemma 2):** For a simple random sample of size k from P elements with centering constraint Σa_i = 0 and σ_a² = P⁻¹ Σa_i²: Var(āS) = (σ_a²/k) · (P−k)/(P−1). Applying to judge biases (a_ℓ = γ_ℓ, P = K_tot, k = K): Var(γ̄) = (σ_γ²/K) · (K_tot − K)/(K_tot − 1).

---

## Appendix D: Estimation of Variance Components

Method-of-moments estimators using crossed ANOVA:
- **σ̂_ε² = MSW** (residual mean square)
- **σ̂_β² = (MSG − MSW)/K** (between-generation mean square, can be negative → truncated to 0)
- **σ̂_α² = (MSS − MSG)/(mK)** (between-scenario mean square)
- **σ̂_γ² = (1/K_tot) Σ γ̂_ℓ² − σ̂_ε² · (K_tot−1)/(nm·K_tot)**

where γ̂_ℓ = X̄_··ℓ − X̄_···.

Zero-truncation note: negative estimates of σ̂_β² (Gemini and Claude on MT-Bench) are set to zero per standard convention—indicates generation-to-generation variability is negligible relative to residual noise.

---

## Appendix E: Allocation Strategy Derivations (Pairwise comparisons)

- V_A − V_C = (K_tot − 1)σ_β² / nB ≥ 0
- V_B − V_C = σ_γ² / nB ≥ 0
- V_A − V_B = [(K_tot − 1)σ_β² − σ_γ²] / nB (sign depends on data)

---

## Appendix F: Scenario Coverage

Under cycling, variance as function of m with total budget B_gen = nm:

V_C(B_gen, m) = m(σ_α² + σ_β² + σ_ε²) / B_gen   (Eq. 35)

This is linear in m with positive slope σ_α²/B_gen, so variance is minimized at m=1, maximizing the number of distinct scenarios up to dataset size N. Once the scenario pool is exhausted (n=N), excess budget should go to additional generations.

---

## Appendix G: Exact Bootstrap Predictions

For finite pool of m_max observed generations, exact predictions use empirical pool variances:
- Strategy A: C_A = K_tot · (1/n) Σ_i [(1/m_max) Σ_g (X̄_ig· − X̄_i··)²]
- Strategy B: C_B = (1/n) Σ_i [(1/(m_max K_tot)) Σ_{g,ℓ} (X_igℓ − X̄_i··)²]
- Strategy C: C_C = (1/(nK_tot)) Σ_{i,ℓ} [(1/m_max) Σ_g (X_igℓ − X̄_i·ℓ)²]

---

## Appendix H: ANOVA F-Test for Judge Effects

Two-way crossed ANOVA, F = MSJ/MSR with K−1 and (N−1)(K−1) degrees of freedom.

| Model | MT-Bench F(4,3196) | MindEval F(4,996) |
|---|---|---|
| Qwen 2.5 7B | 638.2 | 1029.5 |
| Llama 3.3 70B | 445.8 | 1280.1 |
| GPT-5.2 | 601.7 | 200.1 |
| Gemini 3 Flash | 659.2 | 458.0 |
| Claude Sonnet 4.6 | 514.9 | 788.9 |

All p < 0.001.

---

## Appendix I: Omitted Interactions

The model retains grand mean and three main effects, absorbing all interaction terms into residual ε_ijℓ:

- **Scenario–generation:** Generations nested within scenarios, confounded with β_ij by construction.
- **Scenario–judge:** Estimable in principle (n(K_tot−1) additional parameters) but enters only through per-cell residual variance, already captured empirically in §4.
- **Generation–judge:** Exchangeable across j, acts as additional i.i.d. noise, absorbed into σ_ε².

---

## Appendix J: Judge Hyperparameter Settings

**MT-Bench:** temperature=0, max_tokens (OpenAI)=2048, max_tokens (Anthropic)=1024.
**MindEval:** judge_template_version=v0_1, max_completion_tokens=16,000, reasoning_effort=high.

For models outside original API tables (Gemini 3 Flash and Claude Sonnet 4.6 for MT-Bench), closest equivalent setting supported by provider is applied.

Effect of hyperparameters: Decoding hyperparameters control within-judge stochasticity, absorbed into residual ε_ijℓ → contributes to σ_ε². The systematic offset γ_ℓ is a property of the judge model itself, not sampling. Increasing temperature would inflate σ_ε² but, to first order, leave γ_ℓ and σ_γ² unchanged. At the default operating point, judge-offset contribution exceeds residual contribution by roughly two orders of magnitude on both benchmarks. Reasonable perturbations of decoding hyperparameters can only shift σ_ε² within a window much smaller than σ_γ², so the qualitative ranking of allocation strategies is robust to this choice.

---

**Source paper:** [2603.01865] CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation — https://arxiv.org/abs/2603.01865

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b84f8b96-6ddd-4717-b62c-7624b474d7fc",
  "isSidechain": true,
  "agentId": "a744e5363d82fb6b7",
  "requestId": "req_011CbG3asJ8WAUhdDPMPvec6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06b9ce38-388b-4c59-88e3-c71cacaa96ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RSGTMQhoe2MdvVT7L4zXbb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2301,
      "cache_read_input_tokens": 38201,
      "output_tokens": 9855,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2301
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9855,
          "cache_read_input_tokens": 38201,
          "cache_creation_input_tokens": 2301,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2301,
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
