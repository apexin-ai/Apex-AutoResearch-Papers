# Research conversation: Use WebSearch to find the paper "Seddik et al. 2024" related to model collapse or synthetic data training. The likely ti

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a63c74b398248d91b.jsonl`
- **Structured JSON:** [`9837ca4be3c1b13e31dc.json`](../../sessions/98/9837ca4be3c1b13e31dc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-23T04:23:50.090Z_

Use WebSearch to find the paper "Seddik et al. 2024" related to model collapse or synthetic data training. The likely title is "How Bad is Training on Synthetic Data? A Statistical Analysis" or similar.

Search queries to try:
1. "Seddik 2024 training synthetic data statistical analysis"
2. "Seddik model collapse synthetic data 2024"

For the paper you find, report:
- Exact title
- All authors
- Venue/journal and year
- arXiv ID if available
- A BibTeX entry
- Brief description of what the paper is about and whether it's relevant to spectral collapse / model collapse in recursive LLM training

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6d5a3b42-48f6-4d72-9d8d-293aeffbae34",
  "agentId": "a63c74b398248d91b",
  "type": "user",
  "uuid": "3168b051-29a3-485f-97ad-567e440faea6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "sessionId": "faebf5a1-083e-4ce1-9cc8-886f18725684",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-23T04:23:50.096Z_

```json
{
  "parentUuid": "3168b051-29a3-485f-97ad-567e440faea6",
  "isSidechain": true,
  "agentId": "a63c74b398248d91b",
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
  "uuid": "3ec9bf32-dc4e-456b-a948-93005829c1fc",
  "timestamp": "2026-05-23T04:23:50.096Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "sessionId": "faebf5a1-083e-4ce1-9cc8-886f18725684",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-23T04:23:52.470Z_



I'll search for this paper using WebSearch.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ec9bf32-dc4e-456b-a948-93005829c1fc",
  "isSidechain": true,
  "agentId": "a63c74b398248d91b",
  "requestId": "req_011CbJs35sdCbzMVX5R4Cb4z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0cb83631-2bb7-4226-9050-6ed09796b44c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "sessionId": "faebf5a1-083e-4ce1-9cc8-886f18725684",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JHSRUiEYaBXx2nVHfeDwjL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15513,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15513,
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

_source line 4 · 2026-05-23T04:23:52.612Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GqNgjEHbcKmQGRFAjpNiE5`</summary>

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
  "parentUuid": "0cb83631-2bb7-4226-9050-6ed09796b44c",
  "isSidechain": true,
  "agentId": "a63c74b398248d91b",
  "requestId": "req_011CbJs35sdCbzMVX5R4Cb4z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "918ac2f8-d230-49d8-b8a6-41d4b2f76eb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "sessionId": "faebf5a1-083e-4ce1-9cc8-886f18725684",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JHSRUiEYaBXx2nVHfeDwjL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15513,
      "cache_read_input_tokens": 0,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15513
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 87,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15513,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15513,
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

_source line 5 · 2026-05-23T04:23:52.616Z_

<details><summary>↩ Tool result · `toolu_01GqNgjEHbcKmQGRFAjpNiE5`</summary>

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
  "parentUuid": "918ac2f8-d230-49d8-b8a6-41d4b2f76eb5",
  "isSidechain": true,
  "promptId": "6d5a3b42-48f6-4d72-9d8d-293aeffbae34",
  "agentId": "a63c74b398248d91b",
  "type": "user",
  "uuid": "6591e295-001f-474a-b476-25118efb7f0f",
  "sourceToolAssistantUUID": "918ac2f8-d230-49d8-b8a6-41d4b2f76eb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "sessionId": "faebf5a1-083e-4ce1-9cc8-886f18725684",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-23T04:23:54.818Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BaCnoc9NXGPXWTHZmUvWWj`</summary>

```json
{
  "query": "Seddik 2024 training synthetic data statistical analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6591e295-001f-474a-b476-25118efb7f0f",
  "isSidechain": true,
  "agentId": "a63c74b398248d91b",
  "requestId": "req_011CbJs3GuQ2BBPNUotgoTsm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e830d6fd-a8ad-4888-bb30-5c5afc15e31d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "sessionId": "faebf5a1-083e-4ce1-9cc8-886f18725684",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxjZkhRDgEsEiRtVhwGzHR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 15513,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 7 · 2026-05-23T04:23:55.242Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KvyMnPGfGBNYdpGA8iXEP5`</summary>

```json
{
  "query": "Seddik model collapse synthetic data 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e830d6fd-a8ad-4888-bb30-5c5afc15e31d",
  "isSidechain": true,
  "agentId": "a63c74b398248d91b",
  "requestId": "req_011CbJs3GuQ2BBPNUotgoTsm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0fccca5-efe9-4cc9-bd58-7fafceb3900a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "sessionId": "faebf5a1-083e-4ce1-9cc8-886f18725684",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxjZkhRDgEsEiRtVhwGzHR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 15513,
      "output_tokens": 110,
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
          "input_tokens": 3,
          "output_tokens": 110,
          "cache_read_input_tokens": 15513,
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

_source line 8 · 2026-05-23T04:24:00.833Z_

<details><summary>↩ Tool result · `toolu_01KvyMnPGfGBNYdpGA8iXEP5`</summary>

```text
Web search results for query: "Seddik model collapse synthetic data 2024"

Links: [{"title":"MAXIMIZING THE POTENTIAL OF SYNTHETIC DATA","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7416573f05b50beac6d0aef3abc805c0-Paper-Conference.pdf"},{"title":"Strong Model Collapse","url":"https://arxiv.org/html/2410.04840v1"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"},{"title":"Maximizing the Potential of Synthetic Data: Insights from Random Matrix Theory","url":"https://arxiv.org/html/2410.08942v1"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"[2404.05090] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/abs/2404.05090"},{"title":"Strong Model Collapse Elvis Dohmatob1 e.dohmatob@meta.com Yunzhen Feng1,2,∗","url":"https://arxiv.org/pdf/2410.04840"},{"title":"Position: Model Collapse Does Not Mean What You Think Anonymous Author(s)","url":"https://openreview.net/pdf?id=ygfzWIGDN8"},{"title":"A Note on Shumailov et al. (2024): `AI Models Collapse When Trained on   Recursively Generated Data'","url":"https://arxiv.org/pdf/2410.12954"}]

Based on the search results, here's what I found about Seddik's work on model collapse and synthetic data from 2024:

## Overview

Seddik et al. (2024) investigated model collapse in recursive training settings, where new models are trained on data generated by previous models.

## Key Findings

Recursive training on purely synthetic data inevitably leads to performance degradation. However, mixing real and synthetic data can attenuate model collapse, though the proportion of real data must remain high to maintain model performance.

Seddik et al. (2024) analyze the mixing of discrete original and synthetic data, and provide upper bounds on the amount of synthetic data that can be included to avoid model collapse.

## Definition of Model Collapse

The phenomenon of model collapse refers to the deterioration in performance that occurs when new models are trained on synthetic data generated from previously trained models. This recursive training loop makes the tails of the original distribution disappear, thereby making future-generation models forget about the initial (real) distribution.

The published work is titled "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse" by Mohamed El Amine Seddik and colleagues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0fccca5-efe9-4cc9-bd58-7fafceb3900a",
  "isSidechain": true,
  "promptId": "6d5a3b42-48f6-4d72-9d8d-293aeffbae34",
  "agentId": "a63c74b398248d91b",
  "type": "user",
  "uuid": "276e9c30-fa4d-4077-96b8-492c29caf6c5",
  "sourceToolAssistantUUID": "c0fccca5-efe9-4cc9-bd58-7fafceb3900a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "sessionId": "faebf5a1-083e-4ce1-9cc8-886f18725684",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-23T04:24:02.456Z_

<details><summary>↩ Tool result · `toolu_01BaCnoc9NXGPXWTHZmUvWWj`</summary>

```text
Web search results for query: "Seddik 2024 training synthetic data statistical analysis"

Links: [{"title":"Maximizing the Potential of Synthetic Data: Insights from Random Matrix Theory","url":"https://arxiv.org/html/2410.08942v1"},{"title":"[PDF] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | Semantic Scholar","url":"https://www.semanticscholar.org/paper/How-Bad-is-Training-on-Synthetic-Data-A-Statistical-Seddik-Chen/1f71820adfe5eaa344494b1158cbe46ca2d00fc3"},{"title":"MAXIMIZING THE POTENTIAL OF SYNTHETIC DATA","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7416573f05b50beac6d0aef3abc805c0-Paper-Conference.pdf"},{"title":"[2404.05090] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/abs/2404.05090"},{"title":"arXiv:2410.04840v2 [cs.LG] 8 Oct 2024","url":"https://arxiv.org/pdf/2410.04840"},{"title":"[2410.08942] Maximizing the Potential of Synthetic Data: Insights from Random Matrix Theory","url":"https://arxiv.org/abs/2410.08942"},{"title":"Maximizing the Potential of Synthetic Data: Insights from Random Matrix   Theory","url":"https://arxiv.org/pdf/2410.08942"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"Maximizing the Potential of Synthetic Data: Insights from Random Matrix Theory | OpenReview","url":"https://openreview.net/forum?id=I9Dsq0cVo9"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of   Language Model Collapse","url":"https://arxiv.org/pdf/2404.05090"}]

Based on the search results, I found relevant information about Seddik et al.'s 2024 work on training with synthetic data:

## Key Research

Seddik et al. (2024) published research titled "How bad is training on synthetic data? a statistical analysis of language model collapse." The authors include Mohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, and Merouane Debbah.

## Main Findings

The research addresses the phenomenon of model collapse in language models. Model collapse refers to the deterioration in performance that occurs when new models are trained on synthetic data generated from previously trained models, where the recursive training loop makes the tails of the original distribution disappear, thereby making future-generation models forget about the initial (real) distribution.

The study demonstrates that model collapse cannot be avoided when training solely on synthetic data. However, when mixing both real and synthetic data, the researchers provide an estimate of a maximal amount of synthetic data below which model collapse can eventually be avoided.

The work characterizes the distribution shift in synthetic data generated with a language model as the number of generations increases, using a linear Softmax classifier for next-token prediction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e830d6fd-a8ad-4888-bb30-5c5afc15e31d",
  "isSidechain": true,
  "promptId": "6d5a3b42-48f6-4d72-9d8d-293aeffbae34",
  "agentId": "a63c74b398248d91b",
  "type": "user",
  "uuid": "fcda5c99-698d-4277-9942-422aa7cf340c",
  "sourceToolAssistantUUID": "e830d6fd-a8ad-4888-bb30-5c5afc15e31d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "sessionId": "faebf5a1-083e-4ce1-9cc8-886f18725684",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-23T04:24:04.600Z_

Now let me get the exact details from the arXiv page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcda5c99-698d-4277-9942-422aa7cf340c",
  "isSidechain": true,
  "agentId": "a63c74b398248d91b",
  "requestId": "req_011CbJs3zgrkV9oDLLtV7Hkp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca27b16b-b070-423b-a924-81d10080ec4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "sessionId": "faebf5a1-083e-4ce1-9cc8-886f18725684",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014sqL8Qo38PkpdScADWkXzH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 781,
      "cache_creation_input_tokens": 994,
      "cache_read_input_tokens": 16964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 994,
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

_source line 11 · 2026-05-23T04:24:04.890Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CWkE7JX5soEwmiTAfrKb4t`</summary>

```json
{
  "query": "arxiv 2404.05090 \"How Bad is Training on Synthetic Data\" authors venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca27b16b-b070-423b-a924-81d10080ec4a",
  "isSidechain": true,
  "agentId": "a63c74b398248d91b",
  "requestId": "req_011CbJs3zgrkV9oDLLtV7Hkp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7aaee28-542f-4ea9-bac2-2a388c687c05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "sessionId": "faebf5a1-083e-4ce1-9cc8-886f18725684",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014sqL8Qo38PkpdScADWkXzH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 781,
      "cache_creation_input_tokens": 994,
      "cache_read_input_tokens": 16964,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 994
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 781,
          "output_tokens": 87,
          "cache_read_input_tokens": 16964,
          "cache_creation_input_tokens": 994,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 994,
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

_source line 12 · 2026-05-23T04:24:08.224Z_

<details><summary>↩ Tool result · `toolu_01CWkE7JX5soEwmiTAfrKb4t`</summary>

```text
Web search results for query: "arxiv 2404.05090 "How Bad is Training on Synthetic Data" authors venue"

Links: [{"title":"[2404.05090] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/abs/2404.05090"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis","url":"https://arxiv.org/pdf/2404.05090"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/html/2404.05090v1"},{"title":"[PDF] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | Semantic Scholar","url":"https://www.semanticscholar.org/paper/How-Bad-is-Training-on-Synthetic-Data-A-Statistical-Seddik-Chen/1f71820adfe5eaa344494b1158cbe46ca2d00fc3"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | alphaXiv","url":"https://www.alphaxiv.org/resources/2404.05090v1"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240405090E/abstract"}]

Based on the search results, here is the information about arxiv 2404.05090:

**Title:** How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse

**Authors:** Mohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, Merouane Debbah

**Venue:** ArXiv

**Submission Date:** Submitted on 7 Apr 2024

The paper addresses the phenomenon of model collapse, which occurs when new models are trained on synthetic data generated from previously trained models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7aaee28-542f-4ea9-bac2-2a388c687c05",
  "isSidechain": true,
  "promptId": "6d5a3b42-48f6-4d72-9d8d-293aeffbae34",
  "agentId": "a63c74b398248d91b",
  "type": "user",
  "uuid": "0b7a7819-1b17-4f6a-a570-c8ad10daf6d8",
  "sourceToolAssistantUUID": "f7aaee28-542f-4ea9-bac2-2a388c687c05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "sessionId": "faebf5a1-083e-4ce1-9cc8-886f18725684",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T04:24:11.205Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F5UDhHg7Y2wu3KHHdXzdzi`</summary>

```json
{
  "query": "\"How Bad is Training on Synthetic Data\" Seddik ICML NeurIPS ICLR 2024 2025 accepted conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b7a7819-1b17-4f6a-a570-c8ad10daf6d8",
  "isSidechain": true,
  "agentId": "a63c74b398248d91b",
  "requestId": "req_011CbJs4RKSdMWmfHnaDRYwb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "851173f8-02aa-43c1-ad78-13a3650e8093",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "sessionId": "faebf5a1-083e-4ce1-9cc8-886f18725684",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ZDLSL6nt67Ua7Equu6jMJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1382,
      "cache_read_input_tokens": 17958,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1382
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 85,
          "cache_read_input_tokens": 17958,
          "cache_creation_input_tokens": 1382,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1382,
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

_source line 14 · 2026-05-23T04:24:19.072Z_

<details><summary>↩ Tool result · `toolu_01F5UDhHg7Y2wu3KHHdXzdzi`</summary>

```text
Web search results for query: ""How Bad is Training on Synthetic Data" Seddik ICML NeurIPS ICLR 2024 2025 accepted conference"

Links: [{"title":"GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub","url":"https://github.com/pengr/LLM-Synthetic-Data"},{"title":"[2404.05090] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/abs/2404.05090"},{"title":"[PDF] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | Semantic Scholar","url":"https://www.semanticscholar.org/paper/How-Bad-is-Training-on-Synthetic-Data-A-Statistical-Seddik-Chen/1f71820adfe5eaa344494b1158cbe46ca2d00fc3"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of   Language Model Collapse","url":"https://arxiv.org/pdf/2404.05090"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/html/2404.05090v1"},{"title":"Maximizing the Potential of Synthetic Data: Insights from Random Matrix   Theory","url":"https://arxiv.org/pdf/2410.08942"},{"title":"How bad is training on synthetic data? A statistical analysis of language model collapse | OpenReview","url":"https://openreview.net/forum?id=t3z6UlV09o"},{"title":"Does Training on Synthetic Data Make Models Less Robust?","url":"https://arxiv.org/pdf/2502.07164"}]

Based on the search results, I found information about the paper "How Bad is Training on Synthetic Data?" by Seddik and colleagues:

## Paper Details

The paper is titled "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse" by Mohamed El Amine Seddik and 4 other authors. The co-authors are Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, and Merouane Debbah.

## Key Findings

The paper addresses the phenomenon of model collapse, which refers to the deterioration in performance that occurs when new models are trained on synthetic data generated from previously trained models.

The paper demonstrates that model collapse cannot be avoided when training solely on synthetic data. However, when mixing both real and synthetic data, the authors provide an estimate of a maximal amount of synthetic data below which model collapse can eventually be avoided.

## Conference Status

The paper was posted on arXiv on April 7, 2024 (arXiv:2404.05090). However, the search results do not explicitly indicate acceptance at ICML, NeurIPS, or ICLR for 2024 or 2025. The paper is referenced in academic discussions and OpenReview, but specific conference acceptance information was not found in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "851173f8-02aa-43c1-ad78-13a3650e8093",
  "isSidechain": true,
  "promptId": "6d5a3b42-48f6-4d72-9d8d-293aeffbae34",
  "agentId": "a63c74b398248d91b",
  "type": "user",
  "uuid": "d5360130-a970-4166-9422-6f3fea5bc3d4",
  "sourceToolAssistantUUID": "851173f8-02aa-43c1-ad78-13a3650e8093",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "sessionId": "faebf5a1-083e-4ce1-9cc8-886f18725684",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-23T04:24:21.164Z_

Let me check the OpenReview page for venue information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5360130-a970-4166-9422-6f3fea5bc3d4",
  "isSidechain": true,
  "agentId": "a63c74b398248d91b",
  "requestId": "req_011CbJs5DjD7VthTgPARviTj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e760842-63b9-4dfb-8ba8-e9bbe32548c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "sessionId": "faebf5a1-083e-4ce1-9cc8-886f18725684",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ja5WthETsg85s9NnXWh3N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 19340,
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

_source line 16 · 2026-05-23T04:24:21.611Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ftk8o1FNo41Dih2EXVKY5k`</summary>

```json
{
  "query": "site:openreview.net \"How bad is training on synthetic data\" Seddik"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e760842-63b9-4dfb-8ba8-e9bbe32548c5",
  "isSidechain": true,
  "agentId": "a63c74b398248d91b",
  "requestId": "req_011CbJs5DjD7VthTgPARviTj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01af837d-4408-4a63-b09e-3e65e2571dfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "sessionId": "faebf5a1-083e-4ce1-9cc8-886f18725684",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ja5WthETsg85s9NnXWh3N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 19340,
      "output_tokens": 84,
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
          "output_tokens": 84,
          "cache_read_input_tokens": 19340,
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

_source line 17 · 2026-05-23T04:24:26.661Z_

<details><summary>↩ Tool result · `toolu_01Ftk8o1FNo41Dih2EXVKY5k`</summary>

```text
Web search results for query: "site:openreview.net "How bad is training on synthetic data" Seddik"

Links: [{"title":"How Bad is Training on Synthetic Data? A Statistical ...","url":"https://openreview.net/pdf/4b55130ce33429ab600e5cde927dfe10a36328ba.pdf"},{"title":"Escaping Collapse: The Strength of Weak Data for Large Language Model Training∗","url":"https://openreview.net/pdf?id=xpY3C8HxNh"},{"title":"HOW TO PREVENT MODEL COLLAPSE IN SELF- ...","url":"https://openreview.net/pdf?id=WttfQGwpES"},{"title":"How bad is training on synthetic data? A statistical analysis of language model collapse | OpenReview","url":"https://openreview.net/forum?id=t3z6UlV09o"},{"title":"Maximizing the Potential of Synthetic Data: Insights from Random Matrix   Theory","url":"https://arxiv.org/pdf/2410.08942"},{"title":"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls","url":"https://arxiv.org/pdf/2510.01631"},{"title":"Does Training on Synthetic Data Make Models Less Robust?","url":"https://arxiv.org/pdf/2502.07164"}]

I found the paper you're looking for! The paper "How bad is training on synthetic data? A statistical analysis of language model collapse" by Mohamed El Amine Seddik and colleagues addresses model collapse, where training models on synthetic data generated from previously trained models leads to performance deterioration, as the recursive training loop makes the tails of the original distribution disappear.

The paper demonstrates that model collapse cannot be avoided when training solely on synthetic data, but when mixing both real and synthetic data, they provide an estimate of a maximal amount of synthetic data below which model collapse can eventually be avoided.

The paper is available on OpenReview at: https://openreview.net/forum?id=t3z6UlV09o


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01af837d-4408-4a63-b09e-3e65e2571dfd",
  "isSidechain": true,
  "promptId": "6d5a3b42-48f6-4d72-9d8d-293aeffbae34",
  "agentId": "a63c74b398248d91b",
  "type": "user",
  "uuid": "7593d27e-16f2-47b3-bd7d-b9e0e5663e69",
  "sourceToolAssistantUUID": "01af837d-4408-4a63-b09e-3e65e2571dfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "sessionId": "faebf5a1-083e-4ce1-9cc8-886f18725684",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-23T04:24:29.095Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019ya6H1mpfxDU22MSqeCZxJ`</summary>

```json
{
  "query": "openreview.net t3z6UlV09o venue ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7593d27e-16f2-47b3-bd7d-b9e0e5663e69",
  "isSidechain": true,
  "agentId": "a63c74b398248d91b",
  "requestId": "req_011CbJs5n9c5V3JWK22CqNKp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b87f29b-7191-4146-b64b-4673daa411ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "sessionId": "faebf5a1-083e-4ce1-9cc8-886f18725684",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ZgRF2bVcfNEinPhEeg6XZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 619,
      "cache_read_input_tokens": 20193,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 619,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
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

_source line 19 · 2026-05-23T04:24:29.627Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017w63VBT7s5CWrppjMi2yXw`</summary>

```json
{
  "query": "Seddik Chen Hayou Youssef Debbah \"How Bad is Training\" published conference proceedings 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b87f29b-7191-4146-b64b-4673daa411ef",
  "isSidechain": true,
  "agentId": "a63c74b398248d91b",
  "requestId": "req_011CbJs5n9c5V3JWK22CqNKp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "719be55a-a9ce-42bf-9cbd-69ac5ee4e363",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "sessionId": "faebf5a1-083e-4ce1-9cc8-886f18725684",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ZgRF2bVcfNEinPhEeg6XZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 619,
      "cache_read_input_tokens": 20193,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 619
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 20193,
          "cache_creation_input_tokens": 619,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 619,
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

_source line 20 · 2026-05-23T04:24:33.815Z_

<details><summary>↩ Tool result · `toolu_019ya6H1mpfxDU22MSqeCZxJ`</summary>

```text
Web search results for query: "openreview.net t3z6UlV09o venue ICML 2024"

Links: [{"title":"ICML 2024 Conference | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2024%2FConference"},{"title":"ICML 2024 Workshop | OpenReview","url":"https://openreview.net/group?id=ICML.cc/2024/Workshop"},{"title":"ICML 2024 Workshop MI | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2024%2FWorkshop%2FMI"},{"title":"ICML 2024 | OpenReview","url":"https://openreview.net/group?id=ICML.cc/2024"},{"title":"ICML 2024 Workshop ICL | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2024%2FWorkshop%2FICL"},{"title":"Venues | OpenReview","url":"https://openreview.net/venue?id=ICML.cc"},{"title":"ICML 2024 Call for Papers","url":"https://icml.cc/Conferences/2024/CallForPapers"},{"title":"ICML 2024 Conference Submissions | OpenReview","url":"https://openreview.net/submissions?page=15&venue=ICML.cc/2024/Conference"},{"title":"OpenReviewer: A Specialized Large Language Model for Generating Critical   Scientific Paper Reviews","url":"https://arxiv.org/pdf/2412.11948"}]

The search results show general information about ICML 2024 on OpenReview, but they don't contain specific information about the paper with the ID "t3z6UlV09o". The search results include links to ICML 2024 conference submissions and venues on OpenReview, but the particular paper ID you mentioned doesn't appear in these results.

To find the specific paper, you would likely need to:
1. Visit the OpenReview URL directly: `https://openreview.net/forum?id=t3z6UlV09o`
2. Or search on OpenReview's ICML 2024 Conference page at `https://openreview.net/group?id=ICML.cc/2024/Conference`

The search results confirm that papers can be submitted through OpenReview for ICML 2024, and ICML 2024 was held in Vienna, Austria, July 21st - 27th, but I wasn't able to retrieve details about that specific paper ID from the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b87f29b-7191-4146-b64b-4673daa411ef",
  "isSidechain": true,
  "promptId": "6d5a3b42-48f6-4d72-9d8d-293aeffbae34",
  "agentId": "a63c74b398248d91b",
  "type": "user",
  "uuid": "704d951b-88f2-48f8-936c-570011c09d3b",
  "sourceToolAssistantUUID": "2b87f29b-7191-4146-b64b-4673daa411ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "sessionId": "faebf5a1-083e-4ce1-9cc8-886f18725684",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-23T04:24:34.594Z_

<details><summary>↩ Tool result · `toolu_017w63VBT7s5CWrppjMi2yXw`</summary>

```text
Web search results for query: "Seddik Chen Hayou Youssef Debbah "How Bad is Training" published conference proceedings 2024"

Links: [{"title":"GitHub - computationelewetenschapsgroep/genai-telecom: Generative AI models in telecom","url":"https://github.com/computationelewetenschapsgroep/genai-telecom"},{"title":"[2404.05090] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/abs/2404.05090"},{"title":"COLM 2024: Accepted Papers","url":"https://colmweb.org/2024/AcceptedPapers.html"},{"title":"Soufiane Hayou","url":"https://www.soufianehayou.com/"},{"title":"AI Is Not Intelligence: Why Structure, Not Data, Governs Machine Reasononing — Biopharma Business Intelligence Unit (BBIU)","url":"https://www.biopharmabusinessintelligenceunit.com/arch-science/obyzembu2xdh78o9xg8wg0f8lmsqbx"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240405090E/abstract"},{"title":"Real vs Synthetic Data: Is Generative Content in Need of Human Touch - Khalifa University","url":"https://www.ku.ac.ae/real-vs-synthetic-data-is-generative-content-in-need-of-human-touch"},{"title":"How bad is training on synthetic data? A statistical analysis of language model collapse | OpenReview","url":"https://openreview.net/forum?id=t3z6UlV09o"}]

Based on the search results, here's what I found about this paper:

"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse" was published at COLM 2024 by Mohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, and Merouane Debbah.

The paper was presented at the Conference on Language Modeling 2024 (COLM 2024) at the University of Pennsylvania, held from October 7-9, 2024.

**Key Findings:**
The paper addresses the phenomenon of model collapse, which refers to the deterioration in performance that occurs when new models are trained on synthetic data generated from previously trained models, as this recursive training loop makes the tails of the original distribution disappear. 

The authors demonstrate that model collapse cannot be avoided when training solely on synthetic data, but when mixing both real and synthetic data, they provide an estimate of a maximal amount of synthetic data below which model collapse can eventually be avoided.

The paper was submitted to arXiv on April 7, 2024 (arXiv:2404.05090).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "719be55a-a9ce-42bf-9cbd-69ac5ee4e363",
  "isSidechain": true,
  "promptId": "6d5a3b42-48f6-4d72-9d8d-293aeffbae34",
  "agentId": "a63c74b398248d91b",
  "type": "user",
  "uuid": "17c3e4f0-064d-448b-8af7-c564875d3bb0",
  "sourceToolAssistantUUID": "719be55a-a9ce-42bf-9cbd-69ac5ee4e363",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "sessionId": "faebf5a1-083e-4ce1-9cc8-886f18725684",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-23T04:24:50.013Z_

The paper was published at COLM 2024. Here are the full details:

---

**Exact title:** How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse

**Authors:** Mohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, Merouane Debbah

**Venue:** COLM 2024 (Conference on Language Modeling), University of Pennsylvania, October 7--9, 2024

**arXiv ID:** 2404.05090

**BibTeX entry:**

```bibtex
@inproceedings{seddik2024how,
  title={How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse},
  author={Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},
  booktitle={First Conference on Language Modeling (COLM)},
  year={2024},
  url={https://openreview.net/forum?id=t3z6UlV09o}
}
```

**What the paper is about:**

The paper provides a statistical/theoretical analysis of model collapse -- the performance degradation that occurs when models are recursively trained on synthetic data generated by previous-generation models. Using a linear Softmax classifier for next-token prediction as an analytical framework, they characterize how the distribution of synthetic data shifts across generations. Their key findings:

1. Model collapse is **unavoidable** when training solely on synthetic data -- the tails of the original distribution vanish across generations.
2. When **mixing real and synthetic data**, there exists a maximal proportion of synthetic data below which model collapse can be avoided. They provide theoretical estimates for this threshold.

**Relevance to spectral collapse / model collapse in recursive LLM training:**

Highly relevant. This paper directly studies model collapse in the recursive training setting (train model G_n on data from model G_{n-1}), which is the same core phenomenon as "spectral collapse" framed from a spectral/eigenvalue perspective. Seddik et al. approach it from a statistical/distributional angle (distribution shift, tail disappearance), while spectral collapse work examines it through the lens of covariance eigenvalue structure. Both address the same underlying degeneracy in iteratively-trained generative models. The paper's theoretical result on the real/synthetic data mixing threshold is particularly relevant as a complementary analytical perspective.

Sources:
- [arXiv:2404.05090](https://arxiv.org/abs/2404.05090)
- [OpenReview page](https://openreview.net/forum?id=t3z6UlV09o)
- [Semantic Scholar](https://www.semanticscholar.org/paper/How-Bad-is-Training-on-Synthetic-Data-A-Statistical-Seddik-Chen/1f71820adfe5eaa344494b1158cbe46ca2d00fc3)
- [COLM 2024 Accepted Papers](https://colmweb.org/2024/AcceptedPapers.html)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17c3e4f0-064d-448b-8af7-c564875d3bb0",
  "isSidechain": true,
  "agentId": "a63c74b398248d91b",
  "requestId": "req_011CbJs6N72B4GBcduqzMtv1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9993dc38-ac7b-4566-9e0c-667d294d5a15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "sessionId": "faebf5a1-083e-4ce1-9cc8-886f18725684",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JyvQBYam3uX9ccsBjXNxN4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1603,
      "cache_read_input_tokens": 20812,
      "output_tokens": 758,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1603
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 758,
          "cache_read_input_tokens": 20812,
          "cache_creation_input_tokens": 1603,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1603,
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
