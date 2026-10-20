# Research conversation: Search for and verify the paper "Data Selection via Optimal Control for Language Models" (arXiv:2410.07064). It's claime

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ab14a02b19efc99e2.jsonl`
- **Structured JSON:** [`0d62baf699c96fadf788.json`](../../sessions/0d/0d62baf699c96fadf788.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

21 recorded events

### User

_source line 1 · 2026-05-10T21:05:56.293Z_

Search for and verify the paper "Data Selection via Optimal Control for Language Models" (arXiv:2410.07064). It's claimed to be an ICLR 2025 Oral.

1. Search for "Data Selection via Optimal Control ICLR 2025" and "arxiv 2410.07064"
2. If you find the paper, use WebFetch to read the abstract from https://arxiv.org/abs/2410.07064
3. Determine: Does this paper use Pontryagin's Maximum Principle for data selection? Is it offline or online? Does it target collapse prevention specifically? Does it use spectral indicators?

This matters because a proposal about "PI control for adaptive synthetic-to-real data mixing" should probably cite this paper if it uses control theory for data selection. I need to know if the overlap is fundamental or superficial.

Report: the paper's exact method, whether it's online/offline, what signals it uses, and whether it's ICLR 2025 accepted.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4dda2a4b-380c-4285-b547-9faea07a14da",
  "agentId": "ab14a02b19efc99e2",
  "type": "user",
  "uuid": "fe24a34c-543e-403b-9702-f4fed720de8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "afb7a545-a0ba-4e71-a393-62297003c9c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T21:05:56.298Z_

```json
{
  "parentUuid": "fe24a34c-543e-403b-9702-f4fed720de8d",
  "isSidechain": true,
  "agentId": "ab14a02b19efc99e2",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "68cd518d-1190-49b6-ba0c-0e24bd1b873c",
  "timestamp": "2026-05-10T21:05:56.298Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "afb7a545-a0ba-4e71-a393-62297003c9c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-10T21:06:02.935Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GnBkKgZUpx3D4mdoRhFdEV`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68cd518d-1190-49b6-ba0c-0e24bd1b873c",
  "isSidechain": true,
  "agentId": "ab14a02b19efc99e2",
  "requestId": "req_011CauZwLp4cd2zq2fmioKPT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1361afc-fb03-48e3-badf-2ba36eac31a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "afb7a545-a0ba-4e71-a393-62297003c9c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G6f8NixJcGi5Qv19i3A2Pd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 776,
      "cache_read_input_tokens": 8223,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 776
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 80,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 776,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-10T21:06:02.941Z_

<details><summary>↩ Tool result · `toolu_01GnBkKgZUpx3D4mdoRhFdEV`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

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
  "parentUuid": "d1361afc-fb03-48e3-badf-2ba36eac31a2",
  "isSidechain": true,
  "promptId": "4dda2a4b-380c-4285-b547-9faea07a14da",
  "agentId": "ab14a02b19efc99e2",
  "type": "user",
  "uuid": "fb3a1342-243d-413a-a875-523cc29d8083",
  "sourceToolAssistantUUID": "d1361afc-fb03-48e3-badf-2ba36eac31a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "afb7a545-a0ba-4e71-a393-62297003c9c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T21:06:06.869Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MzUPLZB7wKeYzFUGt5KsQo`</summary>

```json
{
  "query": "Data Selection via Optimal Control ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb3a1342-243d-413a-a875-523cc29d8083",
  "isSidechain": true,
  "agentId": "ab14a02b19efc99e2",
  "requestId": "req_011CauZwqQXLaBKs8r3efuXP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "690afb9c-b0d0-4c27-82db-de2a908bd95c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "afb7a545-a0ba-4e71-a393-62297003c9c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DT5ENnQLgeHyYSafzFj4NX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T21:06:06.944Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TXAJeLAcGn4GM54XTywww6`</summary>

```json
{
  "query": "arxiv 2410.07064 Data Selection Optimal Control Language Models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "690afb9c-b0d0-4c27-82db-de2a908bd95c",
  "isSidechain": true,
  "agentId": "ab14a02b19efc99e2",
  "requestId": "req_011CauZwqQXLaBKs8r3efuXP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e782b219-0ea6-4942-8d83-7990773712cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "afb7a545-a0ba-4e71-a393-62297003c9c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DT5ENnQLgeHyYSafzFj4NX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-10T21:06:12.476Z_

<details><summary>↩ Tool result · `toolu_01TXAJeLAcGn4GM54XTywww6`</summary>

```text
Web search results for query: "arxiv 2410.07064 Data Selection Optimal Control Language Models"

Links: [{"title":"[2410.07064] Data Selection via Optimal Control for Language Models","url":"https://arxiv.org/abs/2410.07064"},{"title":"data selection via optimal control for language models","url":"https://arxiv.org/pdf/2410.07064"},{"title":"Paper page - Data Selection via Optimal Control for Language Models","url":"https://huggingface.co/papers/2410.07064"},{"title":"Data Selection via Optimal Control for Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/data-selection-via-optimal-control-language-models"},{"title":"[Literature Review] Data Selection via Optimal Control for Language Models","url":"https://www.themoonlight.io/en/review/data-selection-via-optimal-control-for-language-models"},{"title":"(PDF) Data Selection via Optimal Control for Language Models","url":"https://www.researchgate.net/publication/384770316_Data_Selection_via_Optimal_Control_for_Language_Models"},{"title":"Data-Selection/PDS-1.7B · Hugging Face","url":"https://huggingface.co/Data-Selection/PDS-1.7B"},{"title":"Data Selection via Optimal Control for Language Models | OpenReview","url":"https://openreview.net/forum?id=dhAL5fy8wS"},{"title":"Data Efficacy for Language Model Training","url":"https://arxiv.org/html/2506.21545v1"},{"title":"ICLR 2025 Data Selection via Optimal Control for Language Models Oral","url":"https://iclr.cc/virtual/2025/oral/31812"}]

I found the paper arxiv 2410.07064 on data selection for language models. Here are the key details:

**Title:** Data Selection via Optimal Control for Language Models

**Authors:** Yuxian Gu, Li Dong, Hongning Wang, Yaru Hao, Qingxiu Dong, Furu Wei, Minlie Huang

**Main Contribution:** This work investigates the selection of high-quality pre-training data from massive corpora to enhance LMs' capabilities for downstream usage.

**Methodology:** The authors formulate data selection as a generalized Optimal Control problem, which can be solved theoretically by Pontryagin's Maximum Principle (PMP), yielding a set of necessary conditions that characterize the relationship between optimal data selection and LM training dynamics.

**Framework:** Based on these theoretical results, they introduce PMP-based Data Selection (PDS), a framework that approximates optimal data selection by solving the PMP conditions.

**Results:** In their experiments, they adopt PDS to select data from CommonCrawl and show that the PDS-selected corpus accelerates the learning of LMs and constantly boosts their performance on a wide range of downstream tasks across various model sizes. The benefits of PDS extend to ~400B models trained on ~10T tokens, as evidenced by the extrapolation of the test loss curves according to the Scaling Laws.

**Publication:** The paper was published as a conference paper at ICLR 2025


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e782b219-0ea6-4942-8d83-7990773712cc",
  "isSidechain": true,
  "promptId": "4dda2a4b-380c-4285-b547-9faea07a14da",
  "agentId": "ab14a02b19efc99e2",
  "type": "user",
  "uuid": "49b19b52-48f4-45c8-9561-48bb8cef73e7",
  "sourceToolAssistantUUID": "e782b219-0ea6-4942-8d83-7990773712cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "afb7a545-a0ba-4e71-a393-62297003c9c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-10T21:06:16.165Z_

<details><summary>↩ Tool result · `toolu_01MzUPLZB7wKeYzFUGt5KsQo`</summary>

```text
Web search results for query: "Data Selection via Optimal Control ICLR 2025"

Links: [{"title":"DATA SELECTION VIA OPTIMAL CONTROL FOR ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/9ad4891facabf17aa11580686bacfe4e-Paper-Conference.pdf"},{"title":"ICLR 2025 Data Selection via Optimal Control for Language Models Oral","url":"https://iclr.cc/virtual/2025/oral/31812"},{"title":"Data Selection via Optimal Control for Language Models | OpenReview","url":"https://openreview.net/forum?id=dhAL5fy8wS"},{"title":"data selection via optimal control for language models","url":"https://arxiv.org/pdf/2410.07064"},{"title":"ICLR Poster Data Selection via Optimal Control for Language Models","url":"https://iclr.cc/virtual/2025/poster/28972"},{"title":"About me - Yuxian Gu","url":"https://t1101675.github.io/"},{"title":"[2410.07064] Data Selection via Optimal Control for Language Models","url":"https://arxiv.org/abs/2410.07064"},{"title":"ICLR 2025 Oral Papers - Yan Lin's Blog","url":"https://blog.yanlincs.com/conf-paper/iclr-2025-oral"},{"title":"ICLR 2025 oral notes","url":"https://liu-qilong.github.io/note/iclr-2025-oral-notes"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"}]

Based on the search results, here's information about "Data Selection via Optimal Control for Language Models" at ICLR 2025:

## Paper Overview

This paper was published as a conference paper at ICLR 2025 by Yuxian Gu, Li Dong, Hongning Wang, Yaru Hao, Qingxiu Dong, Furu Wei, and Minlie Huang from Tsinghua University, Microsoft Research, and Peking University.

## Main Contribution

The paper formulates data selection as a generalized Optimal Control problem, which can be solved theoretically by Pontryagin's Maximum Principle (PMP), yielding a set of necessary conditions that characterize the relationship between optimal data selection and LM training dynamics.

## Proposed Framework

Based on these theoretical results, the authors introduce PMP-based Data Selection (PDS), a framework that approximates optimal data selection by solving the PMP conditions.

## Key Advantages

Unlike previous pre-training data selection methods based on deduplication, pattern matching, or single checkpoint performance that are agnostic to the pre-training process of LMs, PDS exploits the highly dynamic nature of LM pre-training through the theoretical optimal control perspective, and it operates offline, before training begins, which avoids additional training-time computation overhead.

## Experimental Results

In experiments, PDS selected data from CommonCrawl and showed that the PDS-selected corpus accelerates the learning of LMs and constantly boosts their performance on a wide range of downstream tasks across various model sizes.

The paper was selected as an ICLR 2025 Oral presentation (top 1.8%).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "690afb9c-b0d0-4c27-82db-de2a908bd95c",
  "isSidechain": true,
  "promptId": "4dda2a4b-380c-4285-b547-9faea07a14da",
  "agentId": "ab14a02b19efc99e2",
  "type": "user",
  "uuid": "3095adee-74d4-412d-b500-61a648de24c0",
  "sourceToolAssistantUUID": "690afb9c-b0d0-4c27-82db-de2a908bd95c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "afb7a545-a0ba-4e71-a393-62297003c9c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-10T21:06:21.409Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01U7u3uWczSG3WuSmJ24Taz2`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.07064",
  "prompt": "Extract the full abstract of this paper. Also note: does it mention Pontryagin's Maximum Principle? Is the method offline or online? Does it mention collapse prevention? Does it use spectral indicators or eigenvalue-based signals? What specific signals/objectives does it optimize for?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3095adee-74d4-412d-b500-61a648de24c0",
  "isSidechain": true,
  "agentId": "ab14a02b19efc99e2",
  "requestId": "req_011CauZxojqZ8w4oSh1q75D5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6981f33d-ce0e-4a3a-96c5-a7cf61688639",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "afb7a545-a0ba-4e71-a393-62297003c9c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N7kdpPz9GcrrYqDdvC4iZg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 821,
      "cache_creation_input_tokens": 967,
      "cache_read_input_tokens": 10887,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 967
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 821,
          "output_tokens": 142,
          "cache_read_input_tokens": 10887,
          "cache_creation_input_tokens": 967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 967,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T21:06:28.339Z_

<details><summary>↩ Tool result · `toolu_01U7u3uWczSG3WuSmJ24Taz2`</summary>

```text
# Paper Analysis: Data Selection via Optimal Control for Language Models

## Full Abstract
"This work investigates the selection of high-quality pre-training data from massive corpora to enhance LMs' capabilities for downstream usage. We formulate data selection as a generalized Optimal Control problem, which can be solved theoretically by Pontryagin's Maximum Principle (PMP), yielding a set of necessary conditions that characterize the relationship between optimal data selection and LM training dynamics. Based on these theoretical results, we introduce PMP-based Data Selection (PDS), a framework that approximates optimal data selection by solving the PMP conditions. In our experiments, we adopt PDS to select data from CommmonCrawl and show that the PDS-selected corpus accelerates the learning of LMs and constantly boosts their performance on a wide range of downstream tasks across various model sizes. Moreover, the benefits of PDS extend to ~400B models trained on ~10T tokens, as evidenced by the extrapolation of the test loss curves according to the Scaling Laws. PDS also improves data utilization when the pre-training data is limited, by reducing the data demand by 1.8 times, which helps mitigate the quick exhaustion of available web-crawled corpora."

## Key Questions Answered

**Pontryagin's Maximum Principle?** Yes, explicitly mentioned as the theoretical foundation for solving the optimal control formulation.

**Offline or Online?** The content indicates an **offline approach**—data is selected from CommonCrawl before training.

**Collapse Prevention?** Not mentioned in the abstract or visible page content.

**Spectral Indicators/Eigenvalue Signals?** Not mentioned in the provided content.

**Specific Signals/Objectives:** The method optimizes for downstream task performance and accelerated learning, with improvement measured through test loss curves aligned with scaling laws.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6981f33d-ce0e-4a3a-96c5-a7cf61688639",
  "isSidechain": true,
  "promptId": "4dda2a4b-380c-4285-b547-9faea07a14da",
  "agentId": "ab14a02b19efc99e2",
  "type": "user",
  "uuid": "1cad3d2a-6712-4ef0-890b-4214f424e482",
  "sourceToolAssistantUUID": "6981f33d-ce0e-4a3a-96c5-a7cf61688639",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "afb7a545-a0ba-4e71-a393-62297003c9c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-10T21:06:33.987Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XUhaSxUB56ZSwhGZqQADBn`</summary>

```json
{
  "url": "https://openreview.net/forum?id=dhAL5fy8wS",
  "prompt": "What is the acceptance status of this paper? Is it an oral? What are the key technical details of the method - specifically: what is the costate/adjoint variable, how does it solve the PMP conditions in practice, is it online or offline, what proxy signals does it use to score data? Does it mention spectral methods, eigenvalues, or collapse prevention?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cad3d2a-6712-4ef0-890b-4214f424e482",
  "isSidechain": true,
  "agentId": "ab14a02b19efc99e2",
  "requestId": "req_011CauZyhjTrwPifa9pD7gca",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a63524f-fef9-41bc-9af3-89381c58bdbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "afb7a545-a0ba-4e71-a393-62297003c9c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fh6oDPbqA2qTr3ZzAoBLdX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1384,
      "cache_read_input_tokens": 11854,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1384
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 11854,
          "cache_creation_input_tokens": 1384,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1384,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T21:06:38.609Z_

<details><summary>↩ Tool result · `toolu_01XUhaSxUB56ZSwhGZqQADBn`</summary>

```text
# Analysis of Paper Acceptance and Technical Details

## Acceptance Status
Yes, this paper was accepted as an **oral presentation** at ICLR 2025, as indicated by the "ICLR 2025 Oral" designation on the webpage.

## Technical Details
Based on the provided content, the webpage offers **limited technical specifics**. Here's what is available:

**Method Overview:**
The paper formulates data selection as an "Optimal Control problem, which can be solved theoretically by Pontryagin's Maximum Principle (PMP)." The framework (PDS) aims to approximate optimal data selection by solving the PMP conditions.

**What the Webpage Does NOT Contain:**
The abstract and metadata provided do not detail:
- Specific costate or adjoint variable formulations
- Practical implementation procedures for solving PMP conditions
- Whether the approach is online or offline
- Specific proxy signals or scoring mechanisms
- Any discussion of spectral methods, eigenvalues, or collapse prevention

## Key Results
The paper demonstrates that "PDS-selected corpus accelerates the learning of LMs" across various model sizes, and benefits extend to models with ~400B parameters trained on ~10T tokens. Additionally, it "reduces the data demand by 1.8 times."

**For complete technical details**, you would need to access the full PDF available through the OpenReview link.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a63524f-fef9-41bc-9af3-89381c58bdbd",
  "isSidechain": true,
  "promptId": "4dda2a4b-380c-4285-b547-9faea07a14da",
  "agentId": "ab14a02b19efc99e2",
  "type": "user",
  "uuid": "fb4b6cfd-bfcc-47aa-bb82-53034b8596d7",
  "sourceToolAssistantUUID": "2a63524f-fef9-41bc-9af3-89381c58bdbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "afb7a545-a0ba-4e71-a393-62297003c9c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-10T21:06:44.740Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LNf8GJoK8qQPcBaDmX5Lwb`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2410.07064",
  "prompt": "I need the technical details of how PDS works in practice. Specifically: 1) What is the costate/adjoint variable and how is it computed? 2) Is data selection done offline (before training) or online (during training)? 3) What signal does PDS use to score/select data - is it based on loss, gradients, or something else? 4) Does the paper mention spectral indicators, eigenvalues, or Hessian-based signals? 5) Does the paper address collapse prevention or training instability? 6) What is the practical algorithm - how does it approximate PMP? Please extract the key method section details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb4b6cfd-bfcc-47aa-bb82-53034b8596d7",
  "isSidechain": true,
  "agentId": "ab14a02b19efc99e2",
  "requestId": "req_011CauZzTfADJTNGztkcKVXv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2c8fee5-964c-4b71-9668-5697d2620442",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "afb7a545-a0ba-4e71-a393-62297003c9c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GebVk8aPm362WtENrZebCc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 483,
      "cache_read_input_tokens": 13238,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 483
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 224,
          "cache_read_input_tokens": 13238,
          "cache_creation_input_tokens": 483,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 483,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T21:06:50.120Z_

<details><summary>↩ Tool result · `toolu_01LNf8GJoK8qQPcBaDmX5Lwb`</summary>

```text
# Technical Details of PDS (Pontryagin Data Selection)

I've reviewed the PDF content provided, which appears to be a research document with figures and mathematical notation. However, the document is heavily compressed in PDF format, making it difficult to extract precise technical details about the PDS methodology.

Based on what can be discerned from the structure, here's what I can identify:

## Observable from Document Structure:

**1) Costate/Adjoint Variables:**
The document contains mathematical formulations typical of optimal control theory, suggesting adjoint-based computation, though specific algorithmic details are obscured by the PDF compression.

**2) Data Selection Timing:**
References to scaling and harness figures suggest analysis of training dynamics, indicating this likely addresses **online selection during training** rather than offline preprocessing.

**3) Selection Signal:**
The presence of "theory.pdf" as a figure element suggests theoretical foundations, possibly involving gradient or loss-based scoring mechanisms common in curriculum learning approaches.

**4) Spectral Indicators:**
While the document structure includes mathematical content that could involve Hessian analysis, I cannot extract explicit mention of eigenvalues or spectral methods from the compressed content.

**5) Collapse Prevention:**
The document appears to address training stability through structured data selection, though explicit collapse-prevention mechanisms aren't clearly legible.

**6) PMP Approximation Algorithm:**
The core algorithm description is inaccessible due to PDF compression limitations.

**Recommendation:** Please provide the source paper in text or HTML format for precise extraction of the method section details you're requesting.

[Binary content (application/pdf, 1.1MB) also saved to /home/ubuntu/.claude-account-1/projects/-/afb7a545-a0ba-4e71-a393-62297003c9c7/tool-results/webfetch-1778447204758-lkz0n3.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2c8fee5-964c-4b71-9668-5697d2620442",
  "isSidechain": true,
  "promptId": "4dda2a4b-380c-4285-b547-9faea07a14da",
  "agentId": "ab14a02b19efc99e2",
  "type": "user",
  "uuid": "fa845237-81f6-4da6-88f6-af5fa30a12e2",
  "sourceToolAssistantUUID": "e2c8fee5-964c-4b71-9668-5697d2620442",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "afb7a545-a0ba-4e71-a393-62297003c9c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-10T21:06:55.034Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FhvM2vx1XYBRotHxPgjzz7`</summary>

```json
{
  "query": "\"PMP-based Data Selection\" PDS method costate adjoint offline \"Pontryagin\" language model training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa845237-81f6-4da6-88f6-af5fa30a12e2",
  "isSidechain": true,
  "agentId": "ab14a02b19efc99e2",
  "requestId": "req_011Caua1JuaiKMiq2ydAVkv5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8257b730-de56-4b46-81ec-9253c5af101b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "afb7a545-a0ba-4e71-a393-62297003c9c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPzYuD8xXkEg8qHhkbxdNF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 659,
      "cache_read_input_tokens": 13721,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 659,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-10T21:06:55.258Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q6b9vovhnUvLMFu6Eefazh`</summary>

```json
{
  "query": "arxiv 2410.07064 PDS algorithm offline data selection proxy model scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8257b730-de56-4b46-81ec-9253c5af101b",
  "isSidechain": true,
  "agentId": "ab14a02b19efc99e2",
  "requestId": "req_011Caua1JuaiKMiq2ydAVkv5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f40b7bcb-98e5-47d0-b23d-e37177aa003a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "afb7a545-a0ba-4e71-a393-62297003c9c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPzYuD8xXkEg8qHhkbxdNF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 659,
      "cache_read_input_tokens": 13721,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 659
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 129,
          "cache_read_input_tokens": 13721,
          "cache_creation_input_tokens": 659,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 659,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T21:07:02.568Z_

<details><summary>↩ Tool result · `toolu_01Q6b9vovhnUvLMFu6Eefazh`</summary>

```text
Web search results for query: "arxiv 2410.07064 PDS algorithm offline data selection proxy model scoring"

Links: [{"title":"data selection via optimal control for language models","url":"https://arxiv.org/pdf/2410.07064"},{"title":"[2410.07064] Data Selection via Optimal Control for Language Models","url":"https://arxiv.org/abs/2410.07064"},{"title":"Paper page - Data Selection via Optimal Control for Language Models","url":"https://huggingface.co/papers/2410.07064"},{"title":"[1906.11829v2] Selection via Proxy: Efficient Data Selection for Deep Learning","url":"https://arxiv.org/abs/1906.11829v2"},{"title":"[2004.00827] Approximate Selection with Guarantees using Proxies","url":"https://arxiv.org/abs/2004.00827"},{"title":"BLISS: A Lightweight Bilevel Influence Scoring Method for Data Selection in Language Model Pretraining","url":"https://arxiv.org/html/2510.06048"},{"title":"[2410.11820] Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws","url":"https://arxiv.org/abs/2410.11820"},{"title":"[1906.11829] Selection via Proxy: Efficient Data Selection for Deep Learning","url":"https://ar5iv.labs.arxiv.org/html/1906.11829"},{"title":"Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws","url":"https://arxiv.org/html/2410.11820"},{"title":"[2511.21056] A Unified Understanding of Offline Data Selection and Online Self-refining Generation for Post-training LLMs","url":"https://arxiv.org/abs/2511.21056"}]

Based on the search results, I found information about arxiv paper 2410.07064 on data selection for language models. Here's what the paper describes:

## PDS (PMP-based Data Selection) Algorithm

The paper formulates data selection as a generalized Optimal Control problem, which can be solved theoretically by Pontryagin's Maximum Principle (PMP), yielding a set of necessary conditions that characterize the relationship between optimal data selection and LM training dynamics. Based on these theoretical results, PDS introduces a framework that approximates optimal data selection by solving the PMP conditions.

## Framework Components

To balance effectiveness and efficiency, PDS first uniformly samples a proxy dataset from the pre-training corpus. Algorithm 1, derived from the PMP conditions, is then applied to the proxy dataset to compute data quality scores for each instance.

A data scorer, typically a small LM, is fine-tuned to predict the quality scores based on the instances in the proxy dataset. The learnt data scorer is subsequently applied to infer quality scores on the entire pre-training corpus.

Finally, the instances with large scores are selected to form a high-quality corpus, which is used to pre-train LMs with any size.

## Key Advantages

Unlike recent online data selection approaches, PDS selects the pre-training corpus offline. This allows PDS to be run only once and used for pre-training multiple LMs of any sizes, without incurring additional computational overhead.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f40b7bcb-98e5-47d0-b23d-e37177aa003a",
  "isSidechain": true,
  "promptId": "4dda2a4b-380c-4285-b547-9faea07a14da",
  "agentId": "ab14a02b19efc99e2",
  "type": "user",
  "uuid": "4f905229-3375-4153-9ac5-3225c7797dd0",
  "sourceToolAssistantUUID": "f40b7bcb-98e5-47d0-b23d-e37177aa003a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "afb7a545-a0ba-4e71-a393-62297003c9c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T21:07:04.315Z_

<details><summary>↩ Tool result · `toolu_01FhvM2vx1XYBRotHxPgjzz7`</summary>

```text
Web search results for query: ""PMP-based Data Selection" PDS method costate adjoint offline "Pontryagin" language model training"

Links: [{"title":"Data Selection via Optimal Control for Language Models | OpenReview","url":"https://openreview.net/forum?id=dhAL5fy8wS"},{"title":"Data Selection via Optimal Control for Language Models","url":"https://arxiv.org/html/2410.07064v1"},{"title":"[2410.07064] Data Selection via Optimal Control for Language Models","url":"https://arxiv.org/abs/2410.07064"},{"title":"Paper page - Data Selection via Optimal Control for Language Models","url":"https://huggingface.co/papers/2410.07064"},{"title":"DATA SELECTION VIA OPTIMAL CONTROL FOR ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/9ad4891facabf17aa11580686bacfe4e-Paper-Conference.pdf"},{"title":"Data Selection via Optimal Control for Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/data-selection-via-optimal-control-language-models"},{"title":"ICLR 2025 Data Selection via Optimal Control for Language Models Oral","url":"https://iclr.cc/virtual/2025/oral/31812"},{"title":"(PDF) Data Selection via Optimal Control for Language Models","url":"https://www.researchgate.net/publication/384770316_Data_Selection_via_Optimal_Control_for_Language_Models"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=data+selection"},{"title":"Pontryagin Maximum Principle (PMP)","url":"https://www.emergentmind.com/topics/pontryagin-maximum-principle-pmp"}]

Based on the search results, here's information about the PMP-based Data Selection (PDS) method:

## Overview

PDS investigates the selection of high-quality pre-training data from massive corpora to enhance language models' capabilities for downstream usage.

## Theoretical Foundation

The method formulates data selection as a generalized Optimal Control problem, which can be solved theoretically by Pontryagin's Maximum Principle (PMP), yielding a set of necessary conditions that characterize the relationship between optimal data selection and LM training dynamics.

## Framework

PMP-based Data Selection (PDS) is a framework that approximates optimal data selection by solving the PMP conditions. The approach connects data selection with classical Optimal Control theory, where control variables in a dynamic system are optimized to achieve desired objectives. By treating data selection as the control variables (whether a data point is included in pre-training), the LM pre-training process as the dynamic system, and the LM's downstream performance as the objective, the framework leverages Pontryagin's Maximum Principle to derive the necessary conditions for optimal data selection in theory.

## Offline Nature and Practical Implementation

The control variables are constrained to be time-invariant due to the offline nature of data selection in this setting. To balance effectiveness and efficiency, PDS first uniformly samples a proxy dataset from the pre-training corpus. Algorithm 1, derived from the PMP conditions, is then applied to compute data quality scores for each instance. A data scorer, typically a small LM, is fine-tuned to predict the quality scores based on the instances. The learnt data scorer is subsequently applied to infer quality scores on the entire pre-training corpus, and finally, the instances with large scores are selected to form a high-quality corpus.

## Experimental Results

In experiments, PDS is adopted to select data from CommmonCrawl and shows that the PDS-selected corpus accelerates the learning of LMs and constantly boosts their performance on a wide range of downstream tasks across various model sizes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8257b730-de56-4b46-81ec-9253c5af101b",
  "isSidechain": true,
  "promptId": "4dda2a4b-380c-4285-b547-9faea07a14da",
  "agentId": "ab14a02b19efc99e2",
  "type": "user",
  "uuid": "c04562c9-ee91-4cab-b2b3-b880608015b2",
  "sourceToolAssistantUUID": "8257b730-de56-4b46-81ec-9253c5af101b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "afb7a545-a0ba-4e71-a393-62297003c9c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-10T21:07:10.816Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Xm5ZerAvw8n2zRKXHfZSPE`</summary>

```json
{
  "url": "https://arxiv.org/html/2410.07064v1",
  "prompt": "I need the technical details of the PDS method. Specifically: 1) What is the costate/adjoint variable in their formulation? How is it computed? 2) How are data quality scores computed from the PMP conditions (Algorithm 1)? What signal is used - loss reduction, gradient alignment, something else? 3) Does the paper mention spectral indicators, eigenvalues, Hessian, or any stability-related signals? 4) Does the paper discuss collapse prevention, training instability, or mode collapse? 5) Is this purely offline (select data before training starts) or does it adapt during training? 6) What is the objective function being optimized - downstream task loss, perplexity, or something else?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c04562c9-ee91-4cab-b2b3-b880608015b2",
  "isSidechain": true,
  "agentId": "ab14a02b19efc99e2",
  "requestId": "req_011Caua2MaM4sMsZDSyGMa8K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0723e1ea-03e7-4b26-a91d-5f57b9a32d2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "afb7a545-a0ba-4e71-a393-62297003c9c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L7vEj3A5VHHg7PmiysEP1f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 805,
      "cache_creation_input_tokens": 1085,
      "cache_read_input_tokens": 14380,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1085
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 805,
          "output_tokens": 245,
          "cache_read_input_tokens": 14380,
          "cache_creation_input_tokens": 1085,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1085,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T21:07:18.538Z_

<details><summary>↩ Tool result · `toolu_01Xm5ZerAvw8n2zRKXHfZSPE`</summary>

```text
# Technical Details of the PDS Method

## 1) Costate/Adjoint Variable Computation

The costate variable is **λ_t*** (called the "target vector"). It's computed via backward recursion:

"λ_t* = λ_{t+1}* + ∇J(θ_t*) − η∇²L(θ_t*, γ*)λ_{t+1}*" with boundary condition "λ_T* = ∇J(θ_T*)".

This aggregates downstream loss gradients and Hessian information backward through training steps.

## 2) Data Quality Score Computation

Quality scores come from alignment between instance gradients and the costate:

"γ_n ← γ_n + α∑_{t=0}^{T-1} λ_{t+1}^T ∇l(x_n, θ_t)"

The signal is **gradient alignment**: instances whose gradients align with the optimal "target direction" (λ_t*) receive higher scores. No spectral indicators or eigenvalues mentioned.

## 3) Stability-Related Signals

**No mention of spectral properties, eigenvalues, Hessian eigenvalues, or stability indicators.** The Hessian appears only in the adjoint equation (Eq. 5) for computing dynamics, not for stability assessment.

## 4) Collapse Prevention

**No discussion of collapse prevention, training instability, or mode collapse.** The paper focuses on data quality without addressing training stability concerns.

## 5) Offline vs. Adaptive

**Purely offline.** "PDS operates offline, before the training begins, which avoids additional training-time computation overhead." Data is selected once from a proxy corpus and reused for any LM size.

## 6) Objective Function

**Area Under the Curve (AUC) of downstream loss over time:**

"min_γ ∑_{t=1}^T J(θ_t)" where J(θ) is downstream task loss (computed on LIMA training split).

This captures cumulative convergence speed rather than final performance alone.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0723e1ea-03e7-4b26-a91d-5f57b9a32d2b",
  "isSidechain": true,
  "promptId": "4dda2a4b-380c-4285-b547-9faea07a14da",
  "agentId": "ab14a02b19efc99e2",
  "type": "user",
  "uuid": "76967ab6-3e47-42b4-80c2-868f897feb22",
  "sourceToolAssistantUUID": "0723e1ea-03e7-4b26-a91d-5f57b9a32d2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "afb7a545-a0ba-4e71-a393-62297003c9c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-10T21:07:49.853Z_

Now I have comprehensive technical details about the paper. Here is my report:

---

## Report: "Data Selection via Optimal Control for Language Models" (arXiv:2410.07064)

### Confirmation of Status

The paper is **confirmed as an ICLR 2025 Oral** (top ~1.8% of submissions). It appears on the official ICLR proceedings and OpenReview with oral designation.

### Authors
Yuxian Gu, Li Dong, Hongning Wang, Yaru Hao, Qingxiu Dong, Furu Wei, Minlie Huang (Tsinghua, Microsoft Research, Peking University)

### Exact Method

The paper introduces **PDS (PMP-based Data Selection)**:

1. **Formulation**: Data selection is cast as an optimal control problem where the control variable is gamma_n (binary inclusion of each data point), the dynamic system is LM pre-training (SGD updates), and the objective is minimizing cumulative downstream loss over training (area under the curve of J(theta_t)).

2. **Pontryagin's Maximum Principle**: They apply PMP to derive necessary optimality conditions. The key object is the **costate/adjoint variable** lambda_t*, computed via backward recursion:
   - lambda_t* = lambda_{t+1}* + nabla J(theta_t*) - eta * nabla^2 L(theta_t*, gamma*) * lambda_{t+1}*
   - Boundary condition: lambda_T* = nabla J(theta_T*)

3. **Data scoring signal**: **Gradient alignment** -- each instance is scored by how well its per-step gradient aligns with the costate (target direction): gamma_n += alpha * sum_t lambda_{t+1}^T nabla l(x_n, theta_t). Instances whose gradients point in the direction that reduces downstream loss fastest get the highest scores.

4. **Practical pipeline**: (a) Sample a proxy dataset from the corpus, (b) run Algorithm 1 on a small proxy model to compute quality scores, (c) train a small scorer LM to predict these scores, (d) apply the scorer to the full corpus, (e) select top-scoring data, (f) train any size LM on the selected data.

### Online vs. Offline

**Purely offline.** Data is selected before training begins. The method is run once on a proxy model and the resulting corpus is reused for training models of any size. It explicitly contrasts itself with online data selection methods, noting the advantage of no additional training-time computation.

### Signals Used

- **Gradient alignment with costate** (the costate aggregates downstream loss gradients backward through time)
- The Hessian appears in the adjoint equation but only for computing dynamics, **not** as a stability signal
- **No spectral indicators, eigenvalues, or Hessian-eigenvalue-based signals**
- **No collapse prevention or training instability discussion**

### What It Does NOT Do

- Does **not** address collapse prevention or training instability
- Does **not** use spectral/eigenvalue-based monitoring
- Does **not** adapt the data mixture during training (purely offline)
- Does **not** deal with synthetic-vs-real data mixing
- Does **not** use PI/PID control or any feedback control during training

### Relevance to a "PI Control for Adaptive Synthetic-to-Real Data Mixing" Proposal

The overlap is **conceptually significant but methodologically superficial**:

| Dimension | PDS (this paper) | PI control proposal |
|-----------|------------------|---------------------|
| Control theory? | Yes (Pontryagin/optimal control) | Yes (PI feedback control) |
| Online/offline? | Offline | Online (adaptive during training) |
| What's controlled? | Static data subset selection | Dynamic mixing ratio |
| Signal used? | Gradient alignment with adjoint | Spectral indicators (collapse) |
| Goal? | Maximize downstream performance | Prevent collapse/instability |
| Data type? | Filter from web crawl | Mix synthetic vs. real |

**You should cite this paper.** The connection is at the level of "using control theory for data selection in LM training" -- the same problem family. However, the methods are fundamentally different: PDS is offline optimal control (open-loop), while PI control for mixing is online feedback control (closed-loop). A proper framing would be: "Gu et al. (2025) showed that optimal control theory can improve data selection for LM pre-training via offline PMP-based scoring; we address the complementary online problem of adaptively adjusting the synthetic-to-real ratio during training using closed-loop PI control with spectral stability signals."

The overlap is real enough to warrant citation (same intellectual lineage of control theory applied to data selection) but different enough that the contributions are clearly distinct (offline/open-loop vs. online/closed-loop; performance optimization vs. collapse prevention; gradient alignment vs. spectral indicators).

Sources:
- [arXiv:2410.07064](https://arxiv.org/abs/2410.07064)
- [ICLR 2025 Oral page](https://iclr.cc/virtual/2025/oral/31812)
- [OpenReview](https://openreview.net/forum?id=dhAL5fy8wS)
- [HTML version with full method details](https://arxiv.org/html/2410.07064v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76967ab6-3e47-42b4-80c2-868f897feb22",
  "isSidechain": true,
  "agentId": "ab14a02b19efc99e2",
  "requestId": "req_011Caua3QhPdjP3bG5qmuyKp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9066cda-0bbb-4e45-a24d-2641940af08c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "afb7a545-a0ba-4e71-a393-62297003c9c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JnZmZgA2XftS4hNkCQD4bz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1556,
      "cache_read_input_tokens": 15465,
      "output_tokens": 1279,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1556
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1279,
          "cache_read_input_tokens": 15465,
          "cache_creation_input_tokens": 1556,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1556,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---
