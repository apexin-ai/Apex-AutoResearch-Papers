# Research conversation: Search for the open-source code availability of "Preference Leakage", a method related to LLM judge contamination. Perfo

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a66baf991dc2e0c2b.jsonl`
- **Structured JSON:** [`42bdbac6269fed13cc80.json`](../../sessions/42/42bdbac6269fed13cc80.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

45 recorded events

### User

_source line 1 · 2026-05-21T20:53:02.731Z_

Search for the open-source code availability of "Preference Leakage", a method related to LLM judge contamination.

Perform these web searches and report findings:
1. Search "preference leakage LLM judge github"
2. Search "preference leakage contamination ICLR 2026"
3. Search "preference leakage benchmark contamination LLM code"
4. Search "preference leakage evaluation bias open source"

For each search, report the top results. I need to know:
- Is there an open-source repo? If so, what's the URL?
- What license does it use?
- How is the code quality (well-documented, clean, etc.)?
- How complex would it be to integrate into an evaluation pipeline?
- If no code exists, how complex would reimplementation be based on the paper?

Be thorough - check arxiv pages for code links too. Report all URLs you find.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "a66baf991dc2e0c2b",
  "type": "user",
  "uuid": "ffd3b22b-691a-4e83-9cd3-866e61be628e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T20:53:02.733Z_

```json
{
  "parentUuid": "ffd3b22b-691a-4e83-9cd3-866e61be628e",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
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
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "64278237-499b-4dfb-97fb-352f0da47b7a",
  "timestamp": "2026-05-21T20:53:02.733Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-21T20:53:05.393Z_



I'll perform all four web searches in parallel to find information about "Preference Leakage" code availability.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64278237-499b-4dfb-97fb-352f0da47b7a",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNrPedhZ3snASMBoS7j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9525b4af-c1dc-460f-9f73-7fd7c0ba3941",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6G2CcGhdnoAKBDbgaxZms",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6730,
      "cache_read_input_tokens": 7329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6730,
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

_source line 4 · 2026-05-21T20:53:05.400Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ei2mztbpH9eTea5eUrPX26`</summary>

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
  "parentUuid": "9525b4af-c1dc-460f-9f73-7fd7c0ba3941",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNrPedhZ3snASMBoS7j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "468df18f-5db5-4a9e-945f-04acef7497ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6G2CcGhdnoAKBDbgaxZms",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6730,
      "cache_read_input_tokens": 7329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6730,
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

_source line 5 · 2026-05-21T20:53:05.403Z_

<details><summary>↩ Tool result · `toolu_01Ei2mztbpH9eTea5eUrPX26`</summary>

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
  "parentUuid": "468df18f-5db5-4a9e-945f-04acef7497ec",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "a66baf991dc2e0c2b",
  "type": "user",
  "uuid": "9e5bfbea-6c01-4db6-a1bf-5105b298aef7",
  "sourceToolAssistantUUID": "468df18f-5db5-4a9e-945f-04acef7497ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-21T20:53:08.072Z_



Now let me run all four searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e5bfbea-6c01-4db6-a1bf-5105b298aef7",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNrbp7g6keytLsBQXus",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a9574de-6c9b-4231-ab1c-e62de852ee9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQoXJ6kUxv4j7gbMjEMzAQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1465,
      "cache_read_input_tokens": 14059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1465,
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

_source line 7 · 2026-05-21T20:53:08.627Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HFAydb1rHEEkxTRdngdjrm`</summary>

```json
{
  "query": "preference leakage LLM judge github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a9574de-6c9b-4231-ab1c-e62de852ee9c",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNrbp7g6keytLsBQXus",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7474d9e8-0ca3-4106-8bb0-d9d131f463ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQoXJ6kUxv4j7gbMjEMzAQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1465,
      "cache_read_input_tokens": 14059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1465,
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

_source line 8 · 2026-05-21T20:53:09.058Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KGYP6XpHoLQHDTFehM7eMx`</summary>

```json
{
  "query": "preference leakage contamination ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7474d9e8-0ca3-4106-8bb0-d9d131f463ca",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNrbp7g6keytLsBQXus",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8046bd13-d5d1-4332-b687-60ec7b297290",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQoXJ6kUxv4j7gbMjEMzAQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1465,
      "cache_read_input_tokens": 14059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1465,
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

_source line 9 · 2026-05-21T20:53:09.106Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lq4PRNskKbrZCPBfzyd7A4`</summary>

```json
{
  "query": "preference leakage benchmark contamination LLM code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8046bd13-d5d1-4332-b687-60ec7b297290",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNrbp7g6keytLsBQXus",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a44c3c8-d5d9-4810-b6a0-cafefa6d0131",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQoXJ6kUxv4j7gbMjEMzAQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1465,
      "cache_read_input_tokens": 14059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1465,
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

_source line 10 · 2026-05-21T20:53:09.268Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UHFxRbZKDV6HYLqFdM5Mwq`</summary>

```json
{
  "query": "preference leakage evaluation bias open source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a44c3c8-d5d9-4810-b6a0-cafefa6d0131",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNrbp7g6keytLsBQXus",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7843935f-a230-44d2-9dd6-587f39dbe858",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQoXJ6kUxv4j7gbMjEMzAQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1465,
      "cache_read_input_tokens": 14059,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1465
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 14059,
          "cache_creation_input_tokens": 1465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1465,
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

_source line 11 · 2026-05-21T20:53:14.133Z_

<details><summary>↩ Tool result · `toolu_01HFAydb1rHEEkxTRdngdjrm`</summary>

```text
Web search results for query: "preference leakage LLM judge github"

Links: [{"title":"ICML Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://icml.cc/virtual/2025/51017"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge | OpenReview","url":"https://openreview.net/forum?id=grIvSXVJ65"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/pdf/2502.01534"},{"title":"[2502.01534] Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/abs/2502.01534"},{"title":"Paper page - Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://huggingface.co/papers/2502.01534"},{"title":"(PDF) Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://www.researchgate.net/publication/388685541_Preference_Leakage_A_Contamination_Problem_in_LLM-as-a-judge"},{"title":"GitHub - David-Li0406/Preference-Leakage","url":"https://github.com/David-Li0406/Preference-Leakage"},{"title":"GitHub - llm-as-a-judge/Awesome-LLM-as-a-judge · GitHub","url":"https://github.com/llm-as-a-judge/Awesome-LLM-as-a-judge"},{"title":"GitHub - toininoi/preference-leakage","url":"https://github.com/toininoi/preference-leakage"}]

Based on the search results, here's what I found about preference leakage in LLM judges:

## Overview

Preference leakage is a contamination problem in LLM-as-a-judge caused by the relatedness between the synthetic data generators and LLM-based evaluators. Preference leakage is a widespread and challenging problem in the area of LLM-as-a-judge.

## Key Details

Three common relatednesses between the data generator LLM and the judge LLM are: being the same model, having an inheritance relationship, and belonging to the same model family. Research empirically confirms the bias of judges towards their related student models caused by preference leakage across multiple LLM baselines and benchmarks.

## GitHub Repository

All codes and data are released at: https://github.com/David-Li0406/Preference-Leakage, with additional LLM-as-a-judge resources available at https://llm-as-a-judge.github.io/.

This appears to be a recent paper from 2025 that highlights an important issue in how LLMs are used to evaluate other LLM outputs, particularly when there's a relationship between the model generating the data and the model evaluating it.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7474d9e8-0ca3-4106-8bb0-d9d131f463ca",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "a66baf991dc2e0c2b",
  "type": "user",
  "uuid": "3ddce231-a0bb-4754-9bdc-df64ab0fc692",
  "sourceToolAssistantUUID": "7474d9e8-0ca3-4106-8bb0-d9d131f463ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T20:53:15.377Z_

<details><summary>↩ Tool result · `toolu_01KGYP6XpHoLQHDTFehM7eMx`</summary>

```text
Web search results for query: "preference leakage contamination ICLR 2026"

Links: [{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge | OpenReview","url":"https://openreview.net/forum?id=grIvSXVJ65"},{"title":"Preference Leakage: A Contamination Problem in LLM-as- ...","url":"https://arxiv.org/pdf/2502.01534"},{"title":"[Paper Note] Preference Leakage: A Contamination Problem in LLM-as-a-judge - 📚 AI Paper Notes","url":"https://en.papernotes.org/ICLR2026/llm_evaluation/preference_leakage_a_contamination_problem_in_llm-as-a-judge/"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge [Quick Review]","url":"https://liner.com/review/preference-leakage-a-contamination-problem-in-llmasajudge"},{"title":"Dawei Li✈️ICLR2026 on X: \"Something we also observed in our Preference Leakage paper (now accepted by ICLR 2026). And we went one step further to reveal the leakage and contamination problem caused by these traits transmitting: https://t.co/NNOw7tvd6l\" / X","url":"https://x.com/Dawei_Li_ASU/status/2044931299836903711"},{"title":"LLM-as-a-judge","url":"https://llm-as-a-judge.github.io/"},{"title":"ICLR Poster Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://iclr.cc/virtual/2026/poster/10008112"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/html/2502.01534v3"},{"title":"[2502.01534] Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/abs/2502.01534"}]

Based on the search results, here's what I found about "preference leakage contamination" at ICLR 2026:

## Overview

Preference leakage is a contamination problem in LLM-as-a-judge caused by the relatedness between the synthetic data generators and LLM-based evaluators.

## The Problem

Large Language Models (LLMs) as judges and LLM-based data synthesis have emerged as two fundamental LLM-driven data annotation methods in model development. While their combination significantly enhances the efficiency of model training and evaluation, little attention has been given to the potential contamination brought by this new model development paradigm.

## Key Findings

The paper defines three common relatednesses between the data generator LLM and the judge LLM: being the same model, having an inheritance relationship, and belonging to the same model family.

Preference leakage, along with the resulting bias, is widespread in supervised fine-tuning (SFT) when the data generator and evaluator are the same. Additionally, smaller student models cause even more bias from judge LLMs, with the smallest models exhibiting the highest preference leakage scores.

## Authors

The paper was authored by Dawei Li, Renliang Sun, Yue Huang, Ming Zhong, Bohan Jiang, Jiawei Han, Xiangliang Zhang, Wei Wang, and Huan Liu from institutions including Arizona State University, UCLA, University of Notre Dame, and University of Illinois Urbana-Champaign.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8046bd13-d5d1-4332-b687-60ec7b297290",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "a66baf991dc2e0c2b",
  "type": "user",
  "uuid": "e2f8513a-2ec5-4400-8f23-323edfa0b78b",
  "sourceToolAssistantUUID": "8046bd13-d5d1-4332-b687-60ec7b297290",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T20:53:16.482Z_

<details><summary>↩ Tool result · `toolu_01Lq4PRNskKbrZCPBfzyd7A4`</summary>

```text
Web search results for query: "preference leakage benchmark contamination LLM code"

Links: [{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge [Quick Review]","url":"https://liner.com/review/preference-leakage-a-contamination-problem-in-llmasajudge"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/html/2502.01534v3"},{"title":"(PDF) Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://www.researchgate.net/publication/388685541_Preference_Leakage_A_Contamination_Problem_in_LLM-as-a-judge"},{"title":"ICLR Poster Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://iclr.cc/virtual/2026/poster/10008112"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge | Pap…","url":"https://www.opentrain.ai/papers/preference-leakage-a-contamination-problem-in-llm-as-a-judge--arxiv-2502.01534/"},{"title":"[2502.01534] Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/abs/2502.01534"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge | OpenReview","url":"https://openreview.net/forum?id=grIvSXVJ65"},{"title":"Preference Leakage: A Contamination Problem in LLM-as- ...","url":"https://arxiv.org/pdf/2502.01534"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://howiehwong.github.io/preference_leakage.pdf"}]

Based on the search results, here's what I found about preference leakage, benchmark contamination, and LLMs:

## Overview

Preference leakage is formally introduced as a contamination issue stemming from the relatedness between data generator and judge LLMs. This issue arises when the LLMs used for data generation and evaluation are closely related, causing the preference of the LLM evaluators to leak to the student models through synthetic data and thus inflating the evaluation score.

## Types of Relatedness

Three common relatednesses are defined between the data generator LLM and the judge LLM: being the same model, having an inheritance relationship, and belonging to the same model family.

## Key Findings

Through extensive experiments, bias of judges towards their related student models caused by preference leakage has been confirmed across multiple LLM baselines and benchmarks. Preference leakage is a pervasive and real-world problem that is harder to detect compared to previously identified biases in LLM-as-a-judge scenarios.

## Real-World Impact

When examining two widely used LLM-as-a-judge leaderboards (AlpacaEval 2.0 and Arena-Hard), several candidate models distilled from GPT-4 or other GPT-series models appear across all these leaderboards and benchmarks, suggesting that preference leakage is a pervasive issue in these datasets.

## Code and Resources

The researchers released all codes and data at: https://github.com/David-Li0406/Preference-Leakage.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a44c3c8-d5d9-4810-b6a0-cafefa6d0131",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "a66baf991dc2e0c2b",
  "type": "user",
  "uuid": "d88a2dd3-3de1-4d82-8a48-9647dcb8174c",
  "sourceToolAssistantUUID": "0a44c3c8-d5d9-4810-b6a0-cafefa6d0131",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T20:53:17.112Z_

<details><summary>↩ Tool result · `toolu_01UHFxRbZKDV6HYLqFdM5Mwq`</summary>

```text
Web search results for query: "preference leakage evaluation bias open source"

Links: [{"title":"Preference Leakage: A Contamination Problem in LLM-as- ...","url":"https://arxiv.org/pdf/2502.01534"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/html/2502.01534v3"},{"title":"Preference Leakage: A Data Contamination Problem in Large Language Models","url":"https://www.getaiverse.com/post/datenkontamination-bei-large-language-models-das-problem-des-preference-leakage"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://openreview.net/pdf?id=gW6NT2IuME"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://howiehwong.github.io/preference_leakage.pdf"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge | OpenReview","url":"https://openreview.net/forum?id=grIvSXVJ65"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge | Pap…","url":"https://www.opentrain.ai/papers/preference-leakage-a-contamination-problem-in-llm-as-a-judge--arxiv-2502.01534/"},{"title":"[2502.01534] Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/abs/2502.01534"}]

Based on the search results, here's what I found about preference leakage, evaluation bias, and open source:

## Preference Leakage Overview

Preference leakage is a contamination problem in LLM-as-a-judge caused by the relatedness between the synthetic data generators and LLM-based evaluators. It describes a contamination problem that arises when the LLM that generates the data is related to the LLM that subsequently evaluates this data, where the models can be identical, one can be derived from the other, or both can belong to the same model family, creating a risk that the evaluating LLM develops an implicit preference for the data generated by the related model.

## The Problem

Studies have shown that preference leakage leads to a systematic preference for related models, with this bias occurring across different LLM base models and benchmarks and making objective performance evaluation difficult. Preference leakage is a pervasive and real-world problem that is harder to detect compared to previously identified biases in LLM-as-a-judge scenarios.

## Mitigation Strategies

A straightforward baseline refines evaluation instructions to explicitly warn against self-preference, encouraging the evaluator to remain impartial and judge outputs solely on content quality and relevance. Chain-of-Thought augments the evaluation prompt by encouraging the model to articulate an explicit step-by-step reasoning process prior to producing its final decision, thereby reducing unconscious style matching. Paraphrasing reduces lexical and stylistic overlap between the evaluator and candidate outputs by paraphrasing prompts or responses before evaluation, mitigating familiarity-driven bias.

## Open Source Resources

The code and data are released at https://github.com/David-Li0406/Preference-Leakage.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7843935f-a230-44d2-9dd6-587f39dbe858",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "a66baf991dc2e0c2b",
  "type": "user",
  "uuid": "1c823e78-2d84-4e84-9897-386f444c55e8",
  "sourceToolAssistantUUID": "7843935f-a230-44d2-9dd6-587f39dbe858",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-21T20:53:20.375Z_

Now let me check the GitHub repos directly to assess code quality, license, and structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c823e78-2d84-4e84-9897-386f444c55e8",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNsTKRTJAQ2bbxcrypL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96348e70-f6c6-4202-b4ce-68e1dd91fedb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NtW2JQSiqKXFrhE4NMFQYy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3776,
      "cache_read_input_tokens": 15524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3776,
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

_source line 16 · 2026-05-21T20:53:20.906Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0138YyS7WRKGf5nqsMJtwFjv`</summary>

```json
{
  "query": "site:github.com David-Li0406/Preference-Leakage README license"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96348e70-f6c6-4202-b4ce-68e1dd91fedb",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNsTKRTJAQ2bbxcrypL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f9e37bd-1fce-43e0-9f0c-a078906b0c76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NtW2JQSiqKXFrhE4NMFQYy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3776,
      "cache_read_input_tokens": 15524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3776,
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

_source line 17 · 2026-05-21T20:53:21.382Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E3kgyZv5kPgqCCEJbPJESt`</summary>

```json
{
  "query": "site:github.com toininoi/preference-leakage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f9e37bd-1fce-43e0-9f0c-a078906b0c76",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNsTKRTJAQ2bbxcrypL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de096a0d-9b1f-42a7-87a2-6ef41f3d930d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NtW2JQSiqKXFrhE4NMFQYy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3776,
      "cache_read_input_tokens": 15524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3776,
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

_source line 18 · 2026-05-21T20:53:21.675Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UNxchoq8bHPW273A2V9Eje`</summary>

```json
{
  "query": "arxiv 2502.01534 preference leakage code repository supplementary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de096a0d-9b1f-42a7-87a2-6ef41f3d930d",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNsTKRTJAQ2bbxcrypL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e48afa7-0c68-4468-a14f-e8a88c8df971",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NtW2JQSiqKXFrhE4NMFQYy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3776,
      "cache_read_input_tokens": 15524,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3776
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 15524,
          "cache_creation_input_tokens": 3776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3776,
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

_source line 19 · 2026-05-21T20:53:24.709Z_

<details><summary>↩ Tool result · `toolu_0138YyS7WRKGf5nqsMJtwFjv`</summary>

```text
Web search results for query: "site:github.com David-Li0406/Preference-Leakage README license"

Links: [{"title":"GitHub - David-Li0406/Preference-Leakage","url":"https://github.com/David-Li0406/Preference-Leakage"},{"title":"DALK/README.md at main · David-Li0406/DALK","url":"https://github.com/David-Li0406/DALK/blob/main/README.md"},{"title":"GitHub - David-Li0406/READ: Code for NAACL 2024 findings paper: READ: Improving Relation Extraction from an ADversarial Perspective · GitHub","url":"https://github.com/David-Li0406/READ"},{"title":"GitHub - David-Li0406/SMoA","url":"https://github.com/David-Li0406/SMoA"},{"title":"GitHub - David-Li0406/DALK","url":"https://github.com/David-Li0406/DALK"},{"title":"spdx-tutorial/README.md at master · david-a-wheeler/spdx-tutorial","url":"https://github.com/david-a-wheeler/spdx-tutorial/blob/master/README.md"},{"title":"GitHub - David-Li0406/Judgment-Detection","url":"https://github.com/David-Li0406/Judgment-Detection"},{"title":"GitHub - David-Li0406/Script-based-Character-Understanding","url":"https://github.com/David-Li0406/Script-based-Character-Understanding"},{"title":"license-gate/README.md at main · DevLeoko/license-gate","url":"https://github.com/DevLeoko/license-gate/blob/main/README.md"},{"title":"preference/README.md at master · kaneplusplus/preference","url":"https://github.com/kaneplusplus/preference/blob/master/README.md"}]

Based on the search results, I found the Preference-Leakage repository, which is the official repository of the paper "Preference Leakage: A Contamination Problem in LLM-as-a-judge". 

However, the search results do not contain specific information about the README content or the license for the David-Li0406/Preference-Leakage repository. The first search result links to the repository page but only shows partial content about the project's datasets and analysis tools. To get the full README and license information, you would need to visit the repository directly at https://github.com/David-Li0406/Preference-Leakage.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f9e37bd-1fce-43e0-9f0c-a078906b0c76",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "a66baf991dc2e0c2b",
  "type": "user",
  "uuid": "26bbfc46-1bca-40ff-b05a-bc7c9e25fdec",
  "sourceToolAssistantUUID": "0f9e37bd-1fce-43e0-9f0c-a078906b0c76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T20:53:26.077Z_

<details><summary>↩ Tool result · `toolu_01E3kgyZv5kPgqCCEJbPJESt`</summary>

```text
Web search results for query: "site:github.com toininoi/preference-leakage"

Links: [{"title":"GitHub - toininoi/preference-leakage","url":"https://github.com/toininoi/preference-leakage"},{"title":"GitHub - David-Li0406/Preference-Leakage","url":"https://github.com/David-Li0406/Preference-Leakage"},{"title":"GitHub - llm-as-a-judge/Awesome-LLM-as-a-judge · GitHub","url":"https://github.com/llm-as-a-judge/Awesome-LLM-as-a-judge"},{"title":"HTTP Background Request preference · Issue #1943 · arkenfox/user.js","url":"https://github.com/arkenfox/user.js/issues/1943"},{"title":"GitHub - gnipping/Awesome-ML-SP-Papers: A curated list of Meachine learning Security & Privacy papers published in security top-4 conferences (IEEE S&P, ACM CCS, USENIX Security and NDSS). · GitHub","url":"https://github.com/gnipping/Awesome-ML-SP-Papers"},{"title":"GitHub - chengyh23/PrivAct: PrivAct: Internalizing Contextual Privacy Preservation via Multi-Agent Preference Training · GitHub","url":"https://github.com/chengyh23/PrivAct"},{"title":"GitHub - Ed1sonChen/DailyArxiv · GitHub","url":"https://github.com/Ed1sonChen/DailyArxiv"},{"title":"GitHub - wechto/paper: Reading List","url":"https://github.com/wechto/paper"},{"title":"GitHub - Privatris/AgentLeak: AgentLeak: Open benchmark for privacy leakage in LLM agents — 7 channels, multi-agent, multi-framework.","url":"https://github.com/Privatris/AgentLeak"},{"title":"GitHub - stratosphereips/awesome-ml-privacy-attacks: An awesome list of papers on privacy attacks against machine learning · GitHub","url":"https://github.com/stratosphereips/awesome-ml-privacy-attacks"}]

Based on the search results, I found the GitHub repository you were looking for:

The official repository of the paper "Preference Leakage: A Contamination Problem in LLM-as-a-judge" is located at `https://github.com/toininoi/preference-leakage`.

The repository addresses preference leakage, a contamination problem in LLM-as-a-judge caused by the relatedness between the synthetic data generators and LLM-based evaluators. The repository includes resources such as the MTBench dataset used to analyze model preferences, model outputs, and judgment results.

The repository contains code and resources related to training student models and conducting evaluations on datasets like AlpacaEval and Arena Hard.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de096a0d-9b1f-42a7-87a2-6ef41f3d930d",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "a66baf991dc2e0c2b",
  "type": "user",
  "uuid": "95c2513c-07cc-42d7-a274-30dfa036e079",
  "sourceToolAssistantUUID": "de096a0d-9b1f-42a7-87a2-6ef41f3d930d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T20:53:27.487Z_

<details><summary>↩ Tool result · `toolu_01UNxchoq8bHPW273A2V9Eje`</summary>

```text
Web search results for query: "arxiv 2502.01534 preference leakage code repository supplementary"

Links: [{"title":"[2502.01534] Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/abs/2502.01534"},{"title":"[2502.01534v1] Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/abs/2502.01534v1"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge | Pap…","url":"https://www.opentrain.ai/papers/preference-leakage-a-contamination-problem-in-llm-as-a-judge--arxiv-2502.01534/"},{"title":"Preference Leakage: A Contamination Problem in LLM-as- ...","url":"https://arxiv.org/pdf/2502.01534"},{"title":"GitHub - David-Li0406/Preference-Leakage","url":"https://github.com/David-Li0406/Preference-Leakage"},{"title":"Paper page - Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://huggingface.co/papers/2502.01534"},{"title":"On the Impacts of Contexts on Repository-Level Code Generation","url":"https://arxiv.org/html/2406.11927v3"},{"title":"Data leakage detection in machine learning code: transfer learning, active learning, or low-shot prompting?","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11935776/"}]

Based on the search results, I found information about the arXiv paper 2502.01534 and its code repository:

## Paper Information

The paper "Preference Leakage: A Contamination Problem in LLM-as-a-judge" exposes a contamination problem in LLM-as-a-judge caused by the relatedness between the synthetic data generators and LLM-based evaluators. The paper was published as a conference paper at ICLR 2026.

## Code Repository

The official code repository is available at GitHub (David-Li0406/Preference-Leakage), which corresponds to the GitHub link: https://github.com/David-Li0406/Preference-Leakage

The search results show the arXiv abstract page, the PDF, and the GitHub repository, but they don't appear to contain specific information about supplementary materials in the search results. You may want to check the GitHub repository directly or the arXiv PDF for supplementary information and code details.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e48afa7-0c68-4468-a14f-e8a88c8df971",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "a66baf991dc2e0c2b",
  "type": "user",
  "uuid": "130a337d-fa47-4324-9959-85c44c05d2a7",
  "sourceToolAssistantUUID": "6e48afa7-0c68-4468-a14f-e8a88c8df971",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-21T20:53:30.101Z_

Let me now fetch the actual GitHub repo pages to inspect code structure, license, and documentation quality.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "130a337d-fa47-4324-9959-85c44c05d2a7",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNtDUWQ5K2JcEKX2R5T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17cb9677-fd55-47fa-801f-a945cf0820e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CG32YeuBaVWAGon9vroBdL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2304,
      "cache_read_input_tokens": 19300,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2304,
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

_source line 23 · 2026-05-21T20:53:30.602Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GgHDzdczkWMZMvGW7Y4QdU`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17cb9677-fd55-47fa-801f-a945cf0820e2",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNtDUWQ5K2JcEKX2R5T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b54b7e6-d272-4733-8f99-3b6b54d94a45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CG32YeuBaVWAGon9vroBdL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2304,
      "cache_read_input_tokens": 19300,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2304
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 97,
          "cache_read_input_tokens": 19300,
          "cache_creation_input_tokens": 2304,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2304,
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

_source line 24 · 2026-05-21T20:53:30.605Z_

<details><summary>↩ Tool result · `toolu_01GgHDzdczkWMZMvGW7Y4QdU`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b54b7e6-d272-4733-8f99-3b6b54d94a45",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "a66baf991dc2e0c2b",
  "type": "user",
  "uuid": "354c0947-a9a4-4f55-a55a-cc404320406f",
  "sourceToolAssistantUUID": "7b54b7e6-d272-4733-8f99-3b6b54d94a45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T20:53:34.387Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BjQNmjHViB1VCAGSmxdjy3`</summary>

```json
{
  "url": "https://github.com/David-Li0406/Preference-Leakage",
  "prompt": "Extract the full README content, repository structure (directories and key files), license information, number of stars, last commit date, and any setup/installation instructions. Also note if there are requirements.txt, setup.py, or similar dependency files."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "354c0947-a9a4-4f55-a55a-cc404320406f",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNtSy7jMToDzX98MD8k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a19e84e-bd76-476c-91fc-94f71df3df47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QFTEKiQrJYZkRwhB6684TT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 616,
      "cache_read_input_tokens": 21604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 616,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 67,
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

_source line 26 · 2026-05-21T20:53:35.377Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PKfG9dnAcnJckaEV42mFBD`</summary>

```json
{
  "url": "https://github.com/toininoi/preference-leakage",
  "prompt": "Extract the full README content, repository structure (directories and key files), license information, number of stars, last commit date, and any setup/installation instructions. Is this the official repo or a fork?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a19e84e-bd76-476c-91fc-94f71df3df47",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNtSy7jMToDzX98MD8k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f259ac6-abb9-4ee0-beda-6219b65f99da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QFTEKiQrJYZkRwhB6684TT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 616,
      "cache_read_input_tokens": 21604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 616,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 67,
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

_source line 27 · 2026-05-21T20:53:36.454Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Q2fw8V4963Ff6EcVRniJ3R`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.01534",
  "prompt": "Extract all information about this paper: title, authors, abstract, any links to code/data repositories, conference acceptance information, and any supplementary material links."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f259ac6-abb9-4ee0-beda-6219b65f99da",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNtSy7jMToDzX98MD8k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50af437b-2664-42ba-b01a-8ad4a052a20a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QFTEKiQrJYZkRwhB6684TT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 616,
      "cache_read_input_tokens": 21604,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 616
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 340,
          "cache_read_input_tokens": 21604,
          "cache_creation_input_tokens": 616,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 616,
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

_source line 28 · 2026-05-21T20:53:40.776Z_

<details><summary>↩ Tool result · `toolu_01BjQNmjHViB1VCAGSmxdjy3`</summary>

````text
# Repository Summary: Preference-Leakage

## Overview
This repository contains research code for the paper "Preference Leakage: A Contamination Problem in LLM-as-a-judge" (arxiv.org/abs/2502.01534). The work investigates contamination issues arising when combining LLM-based data synthesis with LLM-as-judge evaluation systems.

## Repository Structure
```
Preference-Leakage/
├── analysis/          # Analysis scripts and results
├── config/            # Configuration files
├── evaluation/        # Evaluation frameworks (Arena-Hard, AlpacaEval 2.0)
├── resource/          # Resource files and figures
├── training/          # Model training scripts
├── README.md          # Main documentation
└── utils.py           # Utility functions
```

## Key Statistics
- **Stars:** 55
- **Forks:** 3
- **Language Distribution:** Jupyter Notebook (82.2%), Python (17.0%), Other (0.8%)

## Setup & Installation

**Environment Setup:**
```
conda create -n pl python==3.10
conda activate pl
pip install -r requirements.txt
```

**Critical Dependencies:**
- deepspeed=0.14.4
- flash-attn=2.3.6
- llamafactory=0.9.1.dev0
- transformers=4.48.1
- vllm=0.6.1.post1+cu118

## Key Models & Data
- Primary model: Mistral-7B-v0.1
- Datasets sourced from UltraFeedback
- All experimental data available via [Google Drive link provided in README]

## Acknowledgments
The repository acknowledges derivative work from LLaMA-Factory, AlpacaEval, and Arena-Hard projects.

## License Information
No explicit license declaration visible in provided content.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a19e84e-bd76-476c-91fc-94f71df3df47",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "a66baf991dc2e0c2b",
  "type": "user",
  "uuid": "d97dac4f-b6b1-4901-afcc-353e68c52dd2",
  "sourceToolAssistantUUID": "5a19e84e-bd76-476c-91fc-94f71df3df47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-21T20:53:41.126Z_

<details><summary>↩ Tool result · `toolu_01PKfG9dnAcnJckaEV42mFBD`</summary>

````text
# Repository Analysis: toininoi/preference-leakage

## Repository Status
**This is a fork**, not the official repository. It was forked from [David-Li0406/Preference-Leakage](https://github.com/David-Li0406/Preference-Leakage).

## Repository Metrics
- **Stars**: 0
- **Forks**: 0
- **Last Commit**: 9 commits total (specific date not displayed)
- **Primary Languages**: Jupyter Notebook (82.2%), Python (17.0%)

## Directory Structure
```
preference-leakage/
├── analysis/
├── config/
├── evaluation/
├── resource/
├── training/
├── README.md
└── utils.py
```

## License Information
No license information is provided in the visible content.

## Setup Instructions
The repository requires:
- Python 3.10 via conda environment
- Key packages: deepspeed (0.14.4), flash-attn (2.3.6), llamafactory (0.9.2.dev0), transformers (4.48.1), vllm (0.6.1.post1+cu118)
- Mistral-7B-v0.1 model access
- API keys for GPT-4o, Gemini-1.5-flash, and LLaMA-3.3-70B

## Project Overview
This repository implements research on "Preference Leakage: A Contamination Problem in LLM-as-a-judge," examining how synthetic data generators and LLM evaluators create evaluation biases. The work includes training scripts, evaluation benchmarks (Arena-Hard, AlpacaEval 2.0), and analysis tools for detecting preference leakage patterns.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f259ac6-abb9-4ee0-beda-6219b65f99da",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "a66baf991dc2e0c2b",
  "type": "user",
  "uuid": "2e18b28a-f568-4c4d-b405-d92447b36908",
  "sourceToolAssistantUUID": "3f259ac6-abb9-4ee0-beda-6219b65f99da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T20:53:41.387Z_

<details><summary>↩ Tool result · `toolu_01Q2fw8V4963Ff6EcVRniJ3R`</summary>

```text
# Paper Information Extraction

## Title
Preference Leakage: A Contamination Problem in LLM-as-a-judge

## Authors
Dawei Li, Renliang Sun, Yue Huang, Ming Zhong, Bohan Jiang, Jiawei Han, Xiangliang Zhang, Wei Wang, Huan Liu

## Abstract Summary
The paper identifies a contamination issue in LLM-based evaluation systems. The researchers examine what happens when the same or related language models generate synthetic training data and then evaluate that data. They define three types of relationships between generator and evaluator models and demonstrate empirically that judges exhibit "preference leakage"—bias toward related student models. The team notes this problem is "harder to detect compared to previously identified biases" in LLM judging scenarios.

## Conference Acceptance
Accepted by ICLR 2026

## Code & Data Repository
Available at: https://github.com/David-Li0406/Preference-Leakage

## Paper Access Links
- PDF: Available at `/pdf/2502.01534`
- HTML (experimental version): Available at `/html/2502.01534v3`
- TeX Source: Available at `/src/2502.01534`

## Submission History
- v1: February 3, 2025
- v2: May 24, 2025
- v3: March 4, 2026

## DOI
https://doi.org/10.48550/arXiv.2502.01534

## License
Creative Commons BY 4.0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50af437b-2664-42ba-b01a-8ad4a052a20a",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "a66baf991dc2e0c2b",
  "type": "user",
  "uuid": "bf9e8721-db55-4fa7-bd8f-235f91af9b25",
  "sourceToolAssistantUUID": "50af437b-2664-42ba-b01a-8ad4a052a20a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-21T20:53:43.757Z_

Now let me inspect the actual code structure more closely to assess quality and integration complexity.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf9e8721-db55-4fa7-bd8f-235f91af9b25",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNuEw6GnFBTmYZjA1Qg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "450b419c-7411-4bc1-a22a-155a817c70d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmpnuZe4xNQ1C6CNksRmM2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1647,
      "cache_read_input_tokens": 22220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1647,
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

_source line 32 · 2026-05-21T20:53:45.235Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01StM5MZyiH6uc411Ww977ZP`</summary>

```json
{
  "url": "https://github.com/David-Li0406/Preference-Leakage/tree/main/analysis",
  "prompt": "List all files in this directory. What scripts or notebooks are here? What do they do based on filenames?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "450b419c-7411-4bc1-a22a-155a817c70d2",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNuEw6GnFBTmYZjA1Qg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b2983a32-dcc3-4ec8-9d52-c2c91417aad3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmpnuZe4xNQ1C6CNksRmM2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1647,
      "cache_read_input_tokens": 22220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1647,
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

_source line 33 · 2026-05-21T20:53:46.161Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JekRKW7q1wXa35dE7oH2qE`</summary>

```json
{
  "url": "https://github.com/David-Li0406/Preference-Leakage/tree/main/evaluation",
  "prompt": "List all files and subdirectories. What evaluation frameworks are included? How are they structured?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2983a32-dcc3-4ec8-9d52-c2c91417aad3",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNuEw6GnFBTmYZjA1Qg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "070b8bf4-1b86-4698-8d3d-1cf17d555463",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmpnuZe4xNQ1C6CNksRmM2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1647,
      "cache_read_input_tokens": 22220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1647,
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

_source line 34 · 2026-05-21T20:53:47.215Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VFftynyEwWvMdebM5MUWHD`</summary>

```json
{
  "url": "https://github.com/David-Li0406/Preference-Leakage/tree/main/training",
  "prompt": "List all files and subdirectories. What training scripts are available? What frameworks do they use?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "070b8bf4-1b86-4698-8d3d-1cf17d555463",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNuEw6GnFBTmYZjA1Qg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7aa2a74f-49bf-4d46-aae5-0ed67b559b3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmpnuZe4xNQ1C6CNksRmM2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1647,
      "cache_read_input_tokens": 22220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1647,
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

_source line 35 · 2026-05-21T20:53:47.917Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Fu6vnxHWf1vz3Z848nYuYw`</summary>

```json
{
  "url": "https://github.com/David-Li0406/Preference-Leakage/blob/main/utils.py",
  "prompt": "Show the full content of this utils.py file. What functions does it contain? How well documented is the code?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7aa2a74f-49bf-4d46-aae5-0ed67b559b3e",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNuEw6GnFBTmYZjA1Qg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dd357b6-584f-4b29-b48e-34823339b0ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmpnuZe4xNQ1C6CNksRmM2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1647,
      "cache_read_input_tokens": 22220,
      "output_tokens": 427,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1647
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 427,
          "cache_read_input_tokens": 22220,
          "cache_creation_input_tokens": 1647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1647,
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

_source line 36 · 2026-05-21T20:53:49.619Z_

<details><summary>↩ Tool result · `toolu_01StM5MZyiH6uc411Ww977ZP`</summary>

```text
# Files in the `/analysis` Directory

## Subdirectories
- **dataset_categorization** - Folder for dataset categorization work
- **demonstration** - Folder containing demonstrations
- **rationale_categorization** - Folder for rationale categorization work

## Python Scripts
- **alpacaEval.py** - Evaluation script for AlpacaEval benchmark
- **alpacaEval_icl.py** - AlpacaEval with in-context learning
- **bert_recognition.py** - BERT model for recognition tasks
- **correlation.py** - Statistical correlation analysis
- **dataset_categorize.py** - Categorizes datasets
- **llama_analysis.py** - Analysis script for Llama models
- **parse_arenahard.py** - Parses ArenaHard benchmark data
- **rationale_categorize.py** - Categorizes rationales
- **self_recognition_pairwise.py** - Pairwise self-recognition analysis
- **student_recognition.py** - Student model recognition

## Shell Scripts
- **run_alpacaEval.sh** - Executes AlpacaEval evaluation
- **run_rationale_categorize.sh** - Runs rationale categorization
- **self_recognition_pairwise.sh** - Executes pairwise recognition

## Data Files
- **alpacaeval_raw.txt** - Raw AlpacaEval results
- **chatbot_arena_raw.txt** - Raw Chatbot Arena data

This collection appears focused on analyzing model preferences and performance across multiple benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2983a32-dcc3-4ec8-9d52-c2c91417aad3",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "a66baf991dc2e0c2b",
  "type": "user",
  "uuid": "7face991-ba12-4216-be21-e6679c42e7ce",
  "sourceToolAssistantUUID": "b2983a32-dcc3-4ec8-9d52-c2c91417aad3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-21T20:53:49.873Z_

<details><summary>↩ Tool result · `toolu_01VFftynyEwWvMdebM5MUWHD`</summary>

```text
# Training Scripts in Preference-Leakage Repository

## Available Training Scripts

The `/training` directory contains six shell scripts:

1. **train_sft.sh** - Supervised Fine-Tuning
2. **train_dpo.sh** - Direct Preference Optimization
3. **train_human.sh** - Human preference-based training
4. **train_inherit.sh** - Inheritance-based training
5. **train_mix.sh** - Mixed training approach
6. **train_additional.sh** - Additional training methods

## Framework Information

The webpage content provided does not include details about which specific machine learning frameworks (PyTorch, TensorFlow, etc.) these scripts utilize. To determine the frameworks used, you would need to examine the actual script contents within the repository files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7aa2a74f-49bf-4d46-aae5-0ed67b559b3e",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "a66baf991dc2e0c2b",
  "type": "user",
  "uuid": "fc127b56-c265-42fd-9aee-494ec523fd77",
  "sourceToolAssistantUUID": "7aa2a74f-49bf-4d46-aae5-0ed67b559b3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T20:53:50.009Z_

<details><summary>↩ Tool result · `toolu_01JekRKW7q1wXa35dE7oH2qE`</summary>

```text
# Preference-Leakage Evaluation Directory Structure

Based on the GitHub page content, the evaluation directory contains the following subdirectories:

1. **Alpaca_Eval2** - An evaluation framework folder
2. **Arena_Hard** - Another evaluation framework folder

## Structure Overview

The page indicates "View all files" is available, suggesting there may be additional items not fully displayed in the provided content. The directory is organized as a straightforward folder structure under `/evaluation/` in the main branch of the Preference-Leakage repository.

## Key Observation

The content shows only two explicitly named evaluation frameworks in the visible portion of the directory listing. The "View all files" link suggests the complete list extends beyond what's shown in this page excerpt, so there are likely additional evaluation frameworks or files present that aren't visible in the provided screenshot.

Both frameworks appear to be prominent benchmarking/evaluation suites commonly used in AI model assessment contexts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "070b8bf4-1b86-4698-8d3d-1cf17d555463",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "a66baf991dc2e0c2b",
  "type": "user",
  "uuid": "26c0027b-4fc9-4a43-a8c0-4a28c38eab5c",
  "sourceToolAssistantUUID": "070b8bf4-1b86-4698-8d3d-1cf17d555463",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-21T20:53:52.140Z_

<details><summary>↩ Tool result · `toolu_01Fu6vnxHWf1vz3Z848nYuYw`</summary>

```text
# Analysis of utils.py

## Functions Contained

The file includes four main generation functions:

1. **`generate_together()`** - Calls the Together API with retry logic (exponential backoff: 1s to 32s)
2. **`generate_openai()`** - Interfaces with OpenAI's chat completion endpoint
3. **`generate_gemini()`** - Uses Google's Generative AI with safety settings disabled
4. **`generate_vllm()`** - Handles vLLM model completions

Additionally, there's a `safe` list defining Gemini safety filter overrides.

## Documentation Quality

The code is **poorly documented**. Observations:

- **No docstrings** - Functions lack descriptions of purpose, parameters, or return values
- **Minimal comments** - Only a single debug comment present
- **Unclear naming** - The `safe` variable is misleadingly named given it disables all safety filters with `"BLOCK_NONE"`
- **No inline explanations** - Complex retry logic lacks rationale
- **Missing API details** - No notes about rate limits or error handling strategies

The code appears functional but would benefit significantly from comprehensive docstrings and explanatory comments for maintainability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dd357b6-584f-4b29-b48e-34823339b0ce",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "a66baf991dc2e0c2b",
  "type": "user",
  "uuid": "6aaef787-d735-49a0-8019-462c31028056",
  "sourceToolAssistantUUID": "8dd357b6-584f-4b29-b48e-34823339b0ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-21T20:53:55.002Z_

Let me also check the requirements.txt and the README more closely for the preference leakage score computation methodology.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6aaef787-d735-49a0-8019-462c31028056",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNv2u59d78xu1hVhbYp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac35389d-31cb-435a-a18a-5aa2dd1e6614",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015eeuomFB2oSWcQ4nkYu8Me",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1571,
      "cache_read_input_tokens": 23867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1571,
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

_source line 41 · 2026-05-21T20:53:57.462Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BMYJeMBLVHrwHeMpx2ykFn`</summary>

```json
{
  "url": "https://github.com/David-Li0406/Preference-Leakage/blob/main/README.md",
  "prompt": "Extract the FULL README content. I need: 1) The complete step-by-step pipeline described, 2) All commands and configuration details, 3) How the preference leakage score is computed, 4) What benchmarks are used, 5) What models are needed, 6) Any Google Drive or external data links, 7) License information if mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac35389d-31cb-435a-a18a-5aa2dd1e6614",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNv2u59d78xu1hVhbYp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3fedda9c-561a-4656-84b3-25c5710ef1f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015eeuomFB2oSWcQ4nkYu8Me",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1571,
      "cache_read_input_tokens": 23867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1571,
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

_source line 42 · 2026-05-21T20:53:57.884Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FqvQm9ctp5di1dzYMgWzw7`</summary>

```json
{
  "url": "https://github.com/David-Li0406/Preference-Leakage/blob/main/config",
  "prompt": "List all configuration files. What do they configure? What parameters are exposed?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fedda9c-561a-4656-84b3-25c5710ef1f2",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNv2u59d78xu1hVhbYp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13748c4b-1885-4daa-8961-26e46fc9bdab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015eeuomFB2oSWcQ4nkYu8Me",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1571,
      "cache_read_input_tokens": 23867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1571,
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

_source line 43 · 2026-05-21T20:54:02.337Z_

<details><summary>↩ Tool result · `toolu_01FqvQm9ctp5di1dzYMgWzw7`</summary>

```text
# Configuration Files in Preference-Leakage Repository

Based on the GitHub page content provided, I can identify the configuration directory structure, though the specific contents of individual files aren't detailed in the webpage.

## Configuration Subdirectories

The `/config` directory contains these folders:
- **additional**
- **dpo** (Direct Preference Optimization)
- **inherit**
- **mix**
- **mix_synthetic**
- **sft** (Supervised Fine-Tuning)

## Configuration File

- **ds_z3_config.json** - A DeepSpeed configuration file

## Parameters Exposed

Unfortunately, the webpage content doesn't display the actual configuration parameters within these files. To determine what specific parameters are exposed and what they configure, you would need to:

1. Navigate into each subdirectory on GitHub
2. Open the individual JSON/YAML files
3. Review the DeepSpeed documentation for ds_z3_config.json settings

The directory names suggest these configurations likely manage different training approaches (supervised fine-tuning, direct preference optimization, mixed strategies, and data handling), but the exact parameters cannot be confirmed from this page view alone.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13748c4b-1885-4daa-8961-26e46fc9bdab",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "a66baf991dc2e0c2b",
  "type": "user",
  "uuid": "0a4aae10-1d07-40e4-a2a4-6aebba71d446",
  "sourceToolAssistantUUID": "13748c4b-1885-4daa-8961-26e46fc9bdab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T20:54:05.539Z_

<details><summary>↩ Tool result · `toolu_01BMYJeMBLVHrwHeMpx2ykFn`</summary>

```text
# Preference Leakage Repository Summary

## Overview
This is the official repository for a research paper examining "preference leakage," a contamination problem occurring when LLM-based evaluators assess models trained on synthetically generated data from related sources.

## Complete Pipeline

### 1. **Setup Requirements**
The environment uses Python 3.10 with key dependencies: DeepSpeed 0.14.4, Flash-Attention 2.3.6, LLaMA-Factory 0.9.2.dev0, Transformers 4.48.1, and VLLM 0.6.1. External API access is required for GPT-4o, Gemini-1.5-flash, and LLaMA-3.3-70B.

### 2. **Models & Data**
- **Primary Model**: Mistral-7B-v0.1 for main experiments
- **Data Source**: Google Drive folder containing UltraFeedback samples, synthetic datasets, and benchmark outputs
- **Benchmarks**: Arena-Hard and AlpacaEval 2.0 for evaluation

## Step-by-Step Execution

**Main Experiment**:
1. Train student models: `bash training/train_sft.sh`
2. Judge on Arena-Hard: inference → judgment → result parsing
3. Judge on AlpacaEval 2.0: generate outputs → run judge → extract win-rates

**Preference Leakage Score Calculation**:
The repository references "the equation in our paper" but provides no explicit formula in this README—users must calculate based on methodology described in the full paper.

**Additional Experiments**: Testing various model sizes, inheritance chains, learning methods (DPO, ICL), data mixing ratios, and recognition analyses.

## Benchmarks Used
- **Arena-Hard**: Auto-evaluated using GPT-4
- **AlpacaEval 2.0**: Length-controlled win-rate metrics

## External Resources
Data available at: Google Drive folder (link provided in repository)

## License & Attribution
No explicit license statement appears in this README. The project acknowledges borrowing from LLaMA-Factory, AlpacaEval, and Arena-Hard repositories.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fedda9c-561a-4656-84b3-25c5710ef1f2",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "a66baf991dc2e0c2b",
  "type": "user",
  "uuid": "ad6e15c7-56b2-4615-81ed-8646f7d7a4e8",
  "sourceToolAssistantUUID": "3fedda9c-561a-4656-84b3-25c5710ef1f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-21T20:54:43.987Z_

Now I have enough information to compile a comprehensive report.

---

## Preference Leakage -- Open-Source Code Availability Report

### Paper Identity

- **Title**: "Preference Leakage: A Contamination Problem in LLM-as-a-judge"
- **Authors**: Dawei Li, Renliang Sun, Yue Huang, Ming Zhong, Bohan Jiang, Jiawei Han, Xiangliang Zhang, Wei Wang, Huan Liu (ASU, UCLA, Notre Dame, UIUC)
- **ArXiv**: [2502.01534](https://arxiv.org/abs/2502.01534) (v1: Feb 2025, v3: Mar 2026)
- **Venue**: Accepted at **ICLR 2026** (poster)
- **ArXiv License**: CC-BY 4.0

---

### 1. Open-Source Repositories Found

**Official repo**: [https://github.com/David-Li0406/Preference-Leakage](https://github.com/David-Li0406/Preference-Leakage)
- 55 stars, 3 forks
- Languages: Jupyter Notebook (82.2%), Python (17.0%)
- **No explicit software license** declared in the repo (the CC-BY 4.0 on arXiv covers the paper, not necessarily the code)

**Fork** (not official): [https://github.com/toininoi/preference-leakage](https://github.com/toininoi/preference-leakage)
- 0 stars, identical structure, no additional contributions visible

---

### 2. Repository Structure & Code Quality

```
Preference-Leakage/
├── analysis/              # ~12 Python scripts + shell scripts + raw data
│   ├── alpacaEval.py, alpacaEval_icl.py
│   ├── bert_recognition.py, correlation.py
│   ├── self_recognition_pairwise.py, student_recognition.py
│   ├── parse_arenahard.py, llama_analysis.py
│   └── dataset_categorization/, demonstration/, rationale_categorization/
├── config/                # DeepSpeed + LLaMA-Factory configs
│   ├── ds_z3_config.json
│   └── sft/, dpo/, inherit/, mix/, mix_synthetic/, additional/
├── evaluation/
│   ├── Alpaca_Eval2/
│   └── Arena_Hard/
├── training/              # 6 shell scripts
│   ├── train_sft.sh, train_dpo.sh, train_human.sh
│   ├── train_inherit.sh, train_mix.sh, train_additional.sh
├── resource/              # Figures
├── utils.py               # 4 API wrapper functions (Together, OpenAI, Gemini, vLLM)
└── README.md
```

**Code quality assessment: Medium-low.**
- **No docstrings** in Python files; minimal comments
- `utils.py` has 4 bare API wrapper functions with no documentation
- Analysis scripts appear functional but lack explanation
- The bulk of "code" is Jupyter notebooks (82% of repo), which are harder to integrate
- Training scripts are shell wrappers around LLaMA-Factory
- No unit tests, no CI/CD
- README describes the pipeline at a high level but omits the preference leakage score formula (defers to the paper)

**Dependencies**:
- Python 3.10, DeepSpeed 0.14.4, flash-attn 2.3.6, LLaMA-Factory 0.9.1-0.9.2.dev0, transformers 4.48.1, vLLM 0.6.1.post1+cu118
- External API keys needed: GPT-4o, Gemini-1.5-flash, LLaMA-3.3-70B (for judge models)
- Base model: Mistral-7B-v0.1
- Data: UltraFeedback samples hosted on Google Drive

---

### 3. Integration Complexity Assessment

**If integrating the existing repo into an evaluation pipeline:**

- **Medium-high complexity.** The repo is structured as a full end-to-end experiment reproduction pipeline (train student models -> generate outputs -> run judges -> compute scores), not as a reusable library or tool.
- No pip-installable package, no clean API, no modular preference-leakage-score function.
- The evaluation components wrap Arena-Hard and AlpacaEval 2.0 -- these are well-known frameworks, but the wrapping code would need adaptation.
- Heavy external dependencies: requires running vLLM inference, calling multiple commercial APIs, and training models with LLaMA-Factory + DeepSpeed.
- The preference leakage score computation is embedded in analysis notebooks/scripts, not exposed as a standalone function.

**If reimplementing from the paper:**

- **Medium complexity.** The core methodology is conceptually straightforward:
  1. Train student models on synthetic data from a generator LLM (SFT/DPO)
  2. Evaluate student outputs using a judge LLM on Arena-Hard / AlpacaEval 2.0
  3. Compute preference leakage score = difference in judge scores when the judge is related vs. unrelated to the generator
  4. Three relatedness types: same model, inheritance, same family
- The metric itself is a delta of win-rates, which is simple to compute once you have the judge outputs.
- The expensive part is the experimental matrix: training multiple student models x multiple generators x multiple judges x multiple benchmarks.
- Reimplementing just the **detection/measurement** component (without the full training pipeline) would be straightforward -- you mainly need a judge evaluation harness and the score delta computation.

---

### 4. Summary

| Aspect | Status |
|--------|--------|
| Open-source repo exists? | Yes -- [David-Li0406/Preference-Leakage](https://github.com/David-Li0406/Preference-Leakage) |
| License | **None declared** on repo; paper is CC-BY 4.0 |
| Code quality | Medium-low: functional but poorly documented, mostly notebooks |
| Reusable as library? | No -- experiment reproduction scripts, not a library |
| Integration complexity | Medium-high for full pipeline; low-medium for just the metric |
| Reimplementation complexity | Medium overall; low if only measuring the leakage score |

The main value of the repo is the **pre-computed data and model outputs** (hosted on Google Drive), which could save significant compute if you want to validate or extend their results. The code itself would need substantial refactoring to serve as a reusable component in another pipeline.

Sources:
- [Official GitHub Repository](https://github.com/David-Li0406/Preference-Leakage)
- [ArXiv Paper (2502.01534)](https://arxiv.org/abs/2502.01534)
- [OpenReview Page](https://openreview.net/forum?id=grIvSXVJ65)
- [ICLR 2026 Virtual Poster](https://iclr.cc/virtual/2026/poster/10008112)
- [HuggingFace Paper Page](https://huggingface.co/papers/2502.01534)
- [Fork: toininoi/preference-leakage](https://github.com/toininoi/preference-leakage)
- [LLM-as-a-judge Resource Hub](https://llm-as-a-judge.github.io/)
- [Author Tweet Confirming ICLR 2026 Acceptance](https://x.com/Dawei_Li_ASU/status/2044931299836903711)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad6e15c7-56b2-4615-81ed-8646f7d7a4e8",
  "isSidechain": true,
  "agentId": "a66baf991dc2e0c2b",
  "requestId": "req_011CbGNw29TU73Fos2cHdyhG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db2c4381-8fb8-4131-8fef-e55e09251386",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QqgUEK1yfqQoPqftCzbooy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 286,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 25438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 829,
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
