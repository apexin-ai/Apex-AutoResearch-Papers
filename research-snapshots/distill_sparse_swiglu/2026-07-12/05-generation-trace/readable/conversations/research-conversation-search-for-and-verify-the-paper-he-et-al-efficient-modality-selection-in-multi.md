# Research conversation: Search for and verify the paper "He et al., Efficient Modality Selection in Multimodal Learning, JMLR 2024". I need to k

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a2a37f3b8ac03d6e4.jsonl`
- **Structured JSON:** [`67efd93da1e7f1d54346.json`](../../sessions/67/67efd93da1e7f1d54346.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-13T17:23:44.330Z_

Search for and verify the paper "He et al., Efficient Modality Selection in Multimodal Learning, JMLR 2024". I need to know:
1. Does this paper actually exist? What is its exact title, authors, and venue?
2. What is its theoretical framework — does it use mutual information, submodularity?
3. Does it address ranking objectives or only prediction (classification/regression)?
4. How would it relate to a paper proposing information-theoretic bounds for ranking error in demonstration curation for robot learning?

Use WebSearch to find this paper, then use WebFetch to read its abstract and key sections if possible. Report your findings in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "a2a37f3b8ac03d6e4",
  "type": "user",
  "uuid": "42aebf39-0017-4fd8-88d7-fa7bfb1e436d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T17:23:44.335Z_

```json
{
  "parentUuid": "42aebf39-0017-4fd8-88d7-fa7bfb1e436d",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
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
  "uuid": "59fcb832-ecf7-4995-8abb-eda740f293e7",
  "timestamp": "2026-05-13T17:23:44.335Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T17:23:46.681Z_



I'll search for this paper using WebSearch. Let me first load the necessary tool schemas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59fcb832-ecf7-4995-8abb-eda740f293e7",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxRLFSgSowJjeo52fEi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a10be0da-7e0d-4f8a-ae3d-04f0a368ab1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Ua9DPy9RnVvzQDBRKarPC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8916,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8916,
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

_source line 4 · 2026-05-13T17:23:47.111Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JaV2471Pguh9zRoevraHSM`</summary>

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
  "parentUuid": "a10be0da-7e0d-4f8a-ae3d-04f0a368ab1f",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxRLFSgSowJjeo52fEi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc6e27ae-f63c-416f-ac99-2e6a721b16da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Ua9DPy9RnVvzQDBRKarPC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8916,
      "cache_read_input_tokens": 0,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8916
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 100,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8916,
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

_source line 5 · 2026-05-13T17:23:47.115Z_

<details><summary>↩ Tool result · `toolu_01JaV2471Pguh9zRoevraHSM`</summary>

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
  "parentUuid": "dc6e27ae-f63c-416f-ac99-2e6a721b16da",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "a2a37f3b8ac03d6e4",
  "type": "user",
  "uuid": "899dc8a7-65fd-453b-b7d2-5dc1342f9ba7",
  "sourceToolAssistantUUID": "dc6e27ae-f63c-416f-ac99-2e6a721b16da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T17:23:50.318Z_



Now let me search for this paper using multiple queries to be thorough.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "899dc8a7-65fd-453b-b7d2-5dc1342f9ba7",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxRYU9mketZCgJYQSAw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b000343c-01d9-4e2d-8df5-19b66cf585f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7TtZumgcQtwVqvdkSb6E3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 8916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 7 · 2026-05-13T17:23:51.313Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ToubM4HvQWQQfa3TQ5B3RL`</summary>

```json
{
  "query": "He et al. \"Efficient Modality Selection in Multimodal Learning\" JMLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b000343c-01d9-4e2d-8df5-19b66cf585f8",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxRYU9mketZCgJYQSAw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "838500d1-25bf-42c3-aea0-2db3256ce159",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7TtZumgcQtwVqvdkSb6E3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 8916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 8 · 2026-05-13T17:23:51.743Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rd7RQZr2H5hVnzMBKuBS7f`</summary>

```json
{
  "query": "\"Efficient Modality Selection\" multimodal learning JMLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "838500d1-25bf-42c3-aea0-2db3256ce159",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxRYU9mketZCgJYQSAw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6ddb552-a777-418f-b7c5-ffeb60710877",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7TtZumgcQtwVqvdkSb6E3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 8916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 9 · 2026-05-13T17:23:52.292Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J1fyyJfwXbNHyWZPfJ8vJx`</summary>

```json
{
  "query": "modality selection multimodal learning submodularity mutual information JMLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6ddb552-a777-418f-b7c5-ffeb60710877",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxRYU9mketZCgJYQSAw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebd03d58-3151-4022-9060-142d5ae54914",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7TtZumgcQtwVqvdkSb6E3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 8916,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1909
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 197,
          "cache_read_input_tokens": 8916,
          "cache_creation_input_tokens": 1909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1909,
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

_source line 10 · 2026-05-13T17:23:58.923Z_

<details><summary>↩ Tool result · `toolu_01J1fyyJfwXbNHyWZPfJ8vJx`</summary>

```text
Web search results for query: "modality selection multimodal learning submodularity mutual information JMLR"

Links: [{"title":"Efficient Modality Selection in Multimodal Learning","url":"https://www.jmlr.org/papers/volume25/23-0439/23-0439.pdf"},{"title":"Efficient Modality Selection in Multimodal Learning","url":"https://jmlr.org/papers/v25/23-0439.html"},{"title":"Greedy Modality Selection via Approximate Submodular Maximization","url":"https://proceedings.mlr.press/v180/cheng22a/cheng22a.pdf"},{"title":"Efficient modality selection in multimodal learning | The Journal of Machine Learning Research","url":"https://dl.acm.org/doi/10.5555/3722577.3722624"},{"title":"DeepSuM: Deep Sufficient Modality Learning Framework","url":"https://arxiv.org/html/2503.01728"},{"title":"Balanced Multimodal Learning via Mutual Information","url":"https://arxiv.org/html/2511.00987"},{"title":"Toward Structural Multimodal Representations: Specialization, Selection, and Sparsification via Mixture-of-Experts","url":"https://arxiv.org/html/2605.03348"},{"title":"Deep Multimodal Learning with Missing Modality: A Survey","url":"https://arxiv.org/html/2409.07825v3"},{"title":"Mutual Information Analysis in Multimodal Learning Systems","url":"https://arxiv.org/html/2405.12456v1"},{"title":"Multimodal learning - Wikipedia","url":"https://en.wikipedia.org/wiki/Multimodal_learning"}]

Based on the search results, I found highly relevant research on modality selection in multimodal learning that combines submodularity and mutual information:

## Key Research Finding

The primary source is "Efficient Modality Selection in Multimodal Learning," which provides the first unified theoretical framework based on submodularity for tackling the modality selection problem in both classification and regression settings.

## Theoretical Framework

The paper proposes a unified theoretical framework to quantify the learning utility of modalities and identifies dependence assumptions to flexibly model the heterogeneous nature of multimodal data, which also allows efficient algorithm design, deriving a greedy modality selection algorithm via submodular maximization.

## Connection Between Mutual Information and Submodularity

The framework connects to Shannon mutual information (I(S; Y)) between the output Y and multimodal input S, showing that I(S; Y) is monotonically non-decreasing on the set of input modalities. Additionally, the research addresses the case of approximate submodularity of mutual information for multimodal learning.

## Publication Venue

This work was published in the Journal of Machine Learning Research (JMLR), Volume 25, with the paper accessible through both the JMLR website and academic databases.

The research effectively bridges theoretical information-theoretic concepts (mutual information) with practical optimization techniques (submodular maximization) to efficiently select the most informative subset of modalities for multimodal learning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebd03d58-3151-4022-9060-142d5ae54914",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "a2a37f3b8ac03d6e4",
  "type": "user",
  "uuid": "b584a37a-7b2e-4c61-97d4-76261f132c04",
  "sourceToolAssistantUUID": "ebd03d58-3151-4022-9060-142d5ae54914",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-13T17:24:00.818Z_

<details><summary>↩ Tool result · `toolu_01Rd7RQZr2H5hVnzMBKuBS7f`</summary>

```text
Web search results for query: ""Efficient Modality Selection" multimodal learning JMLR 2024"

Links: [{"title":"Efficient Modality Selection in Multimodal Learning","url":"https://jmlr.org/papers/v25/23-0439.html"},{"title":"Efficient Modality Selection in Multimodal Learning","url":"https://www.jmlr.org/papers/volume25/23-0439/23-0439.pdf"},{"title":"Efficient modality selection in multimodal learning | The Journal of Machine Learning Research","url":"https://dl.acm.org/doi/10.5555/3722577.3722624"},{"title":"Journal of Machine Learning Research on X: \"'Efficient Modality Selection in Multimodal Learning', by Yifei He, Runxiang Cheng, Gargi Balasubramaniam, Yao-Hung Hubert Tsai, Han Zhao. https://t.co/K7o2CBIlit #multimodal #modality #modalities\" / X","url":"https://x.com/JmlrOrg/status/1767657167190933840"},{"title":"Efficient modality selection in multimodal learning","url":"https://dl.acm.org/doi/pdf/10.5555/3722577.3722624"},{"title":"Journal of Machine Learning Research 24 (2023) 1-7","url":"https://www.jmlr.org/papers/volume24/22-1021/22-1021.pdf"},{"title":"Robust Multimodal Learning with Missing Modalities via Parameter-Efficient Adaptation | OpenReview","url":"https://openreview.net/forum?id=XTwwtlEfTF"},{"title":"Robust Multimodal Learning with Missing Modalities via Parameter-Efficient Adaptation","url":"https://arxiv.org/html/2310.03986v3"},{"title":"Deep Multimodal Learning with Missing Modality: A Survey","url":"https://arxiv.org/html/2409.07825v3"},{"title":"Robust Multimodal Learning With Missing Modalities via ...","url":"https://www.computer.org/csdl/journal/tp/2025/02/10713849/20VwC7hALjq"}]

I found the paper you're looking for! Here are the key details:

## "Efficient Modality Selection in Multimodal Learning"

The paper was authored by Yifei He, Runxiang Cheng, Gargi Balasubramaniam, Yao-Hung Hubert Tsai, and Han Zhao, and it was published in the Journal of Machine Learning Research Volume 25, Issue 1 in January 2024.

### Main Contributions:

The paper addresses multimodal learning, which aims to learn from data of different modalities by fusing information from heterogeneous sources, but notes that it is often infeasible to use all available modalities under limited computational resources.

The authors derive a greedy modality selection algorithm via submodular maximization, which selects the most useful modalities with an optimality guarantee on learning performance. They also connect marginal-contribution-based feature importance scores, such as Shapley value, from the feature selection domain to the context of modality selection, to efficiently compute the importance of individual modality.

### Evaluation:

The efficacy of their theoretical results and modality selection algorithms was demonstrated on 2 synthetic and 4 real-world data sets on a diverse range of multimodal data.

The paper is available at: https://jmlr.org/papers/v25/23-0439.html


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6ddb552-a777-418f-b7c5-ffeb60710877",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "a2a37f3b8ac03d6e4",
  "type": "user",
  "uuid": "6cc425b4-164a-4a90-9aa9-0b0b0defc178",
  "sourceToolAssistantUUID": "c6ddb552-a777-418f-b7c5-ffeb60710877",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T17:24:01.574Z_

<details><summary>↩ Tool result · `toolu_01ToubM4HvQWQQfa3TQ5B3RL`</summary>

```text
Web search results for query: "He et al. "Efficient Modality Selection in Multimodal Learning" JMLR 2024"

Links: [{"title":"Efficient Modality Selection in Multimodal Learning","url":"https://jmlr.org/papers/v25/23-0439.html"},{"title":"Efficient Modality Selection in Multimodal Learning","url":"https://sampalomad.github.io/paper/he2024efficient.pdf"},{"title":"Efficient Modality Selection in Multimodal Learning","url":"https://www.jmlr.org/papers/volume25/23-0439/23-0439.pdf"},{"title":"Efficient modality selection in multimodal learning | The Journal of Machine Learning Research","url":"https://dl.acm.org/doi/10.5555/3722577.3722624"},{"title":"Journal of Machine Learning Research on X: \"'Efficient Modality Selection in Multimodal Learning', by Yifei He, Runxiang Cheng, Gargi Balasubramaniam, Yao-Hung Hubert Tsai, Han Zhao. https://t.co/K7o2CBIlit #multimodal #modality #modalities\" / X","url":"https://x.com/JmlrOrg/status/1767657167190933840"},{"title":"Efficient modality selection in multimodal learning","url":"https://dl.acm.org/doi/pdf/10.5555/3722577.3722624"},{"title":"dblp: Journal of Machine Learning Research, Volume 25","url":"https://dblp.org/db/journals/jmlr/jmlr25.html"},{"title":"A survey on knowledge-enhanced multimodal learning | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-024-10825-z"},{"title":"Robust Multimodal Learning With Missing Modalities via ...","url":"https://www.computer.org/csdl/journal/tp/2025/02/10713849/20VwC7hALjq"},{"title":"Journal of Machine Learning Research","url":"https://twitter.com/JmlrOrg/status/1767657167190933840"}]

I found the paper! Here's what I discovered:

"Efficient Modality Selection in Multimodal Learning" is authored by Yifei He, Runxiang Cheng, Gargi Balasubramaniam, Yao-Hung Hubert Tsai, and Han Zhao, and it was published in JMLR 2024.

**Paper Overview:**

Multimodal learning aims to learn from data of different modalities by fusing information from heterogeneous sources, though it is often infeasible to use all available modalities under limited computational resources.

**Main Contributions:**

The authors derive a greedy modality selection algorithm via submodular maximization, which selects the most useful modalities with an optimality guarantee on learning performance. They also connect marginal-contribution-based feature importance scores, such as Shapley value, from the feature selection domain to the context of modality selection, to efficiently compute the importance of individual modality.

**Technical Framework:**

In classification with cross-entropy loss, a modality's utility is quantified as the Shannon mutual information between the modality and the target; in regression with quadratic loss, the utility is quantified as the variance of the conditional expectation of the target given the modality.

**Evaluation:**

The authors demonstrate the efficacy of their theoretical results and modality selection algorithms on 2 synthetic and 4 real-world data sets on a diverse range of multimodal data.

The paper is accessible at https://jmlr.org/papers/v25/23-0439.html


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "838500d1-25bf-42c3-aea0-2db3256ce159",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "a2a37f3b8ac03d6e4",
  "type": "user",
  "uuid": "3b6db1a5-e5b7-45f4-96a0-937005be951d",
  "sourceToolAssistantUUID": "838500d1-25bf-42c3-aea0-2db3256ce159",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-13T17:24:04.779Z_

The paper is confirmed to exist. Now let me fetch the actual paper to get more details on the theoretical framework, especially regarding whether it addresses ranking objectives.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b6db1a5-e5b7-45f4-96a0-937005be951d",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxSbwnZtCcLyd69cTnB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32093401-0999-4085-9be0-08a7a77f30ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136dEeVHZz7QyWKYeBs741P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1711,
      "cache_creation_input_tokens": 1154,
      "cache_read_input_tokens": 10825,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1154,
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

_source line 14 · 2026-05-13T17:24:07.171Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FGK1TcDvkhe9TPCwZeohbn`</summary>

```json
{
  "url": "https://jmlr.org/papers/v25/23-0439.html",
  "prompt": "Extract the full abstract, list of authors, publication details, and any information about what types of tasks/objectives the paper addresses (classification, regression, ranking, etc.). Also extract information about the theoretical framework: mutual information, submodularity, Shapley values, and any bounds they prove."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32093401-0999-4085-9be0-08a7a77f30ce",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxSbwnZtCcLyd69cTnB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3fbb8f1c-a227-4fcb-a510-b1d9bb9832ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136dEeVHZz7QyWKYeBs741P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1711,
      "cache_creation_input_tokens": 1154,
      "cache_read_input_tokens": 10825,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1154,
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

_source line 15 · 2026-05-13T17:24:10.388Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016APdVUWjYTLXq46cj87EUi`</summary>

```json
{
  "url": "https://www.jmlr.org/papers/volume25/23-0439/23-0439.pdf",
  "prompt": "Extract the following from this paper: 1) The full abstract. 2) The theoretical framework - what mathematical tools are used (mutual information, submodularity, Shapley values, information-theoretic bounds). 3) What types of learning tasks are addressed - specifically does the paper cover ranking objectives, or only classification and regression? 4) Any discussion of demonstration selection, imitation learning, or robot learning. 5) The key theorems and their statements. 6) The section headings and structure of the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fbb8f1c-a227-4fcb-a510-b1d9bb9832ca",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxSbwnZtCcLyd69cTnB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b50c6f6-9702-46dd-be25-c8b32d5c5e5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136dEeVHZz7QyWKYeBs741P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1711,
      "cache_creation_input_tokens": 1154,
      "cache_read_input_tokens": 10825,
      "output_tokens": 367,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1154
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1711,
          "output_tokens": 367,
          "cache_read_input_tokens": 10825,
          "cache_creation_input_tokens": 1154,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1154,
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

_source line 16 · 2026-05-13T17:24:10.975Z_

<details><summary>↩ Tool result · `toolu_01FGK1TcDvkhe9TPCwZeohbn`</summary>

```text
# Paper Extraction: Efficient Modality Selection in Multimodal Learning

## Authors
Yifei He, Runxiang Cheng, Gargi Balasubramaniam, Yao-Hung Hubert Tsai, Han Zhao

## Publication Details
- Journal: JMLR (Journal of Machine Learning Research)
- Volume: 25, Issue: 47
- Pages: 1–39
- Year: 2024

## Abstract
The researchers address "the modality selection problem, which aims to select the most useful subset of modalities for learning under a cardinality constraint." Their work focuses on scenarios where computational resources limit the ability to use all available modalities, and where information overlap across modalities exists.

## Theoretical Framework Components
The paper develops:
- A unified theoretical framework to measure learning utility across modalities
- **Submodular maximization approach**: A greedy algorithm for modality selection with "an optimality guarantee on learning performance"
- **Shapley values**: They "connect marginal-contribution-based feature importance scores, such as Shapley value, from the feature selection domain to the context of modality selection"
- Dependence assumptions for modeling heterogeneous multimodal data

## Task/Objective Type
The paper addresses general **multimodal fusion and learning** rather than specific supervised tasks like classification or regression. It focuses on optimizing *which modalities to use* rather than how to solve downstream tasks.

## Evaluation
Testing conducted on 2 synthetic and 4 real-world multimodal datasets.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fbb8f1c-a227-4fcb-a510-b1d9bb9832ca",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "a2a37f3b8ac03d6e4",
  "type": "user",
  "uuid": "1c57d6c5-67cb-4d79-af3c-91723553246b",
  "sourceToolAssistantUUID": "3fbb8f1c-a227-4fcb-a510-b1d9bb9832ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-13T17:24:15.745Z_

<details><summary>↩ Tool result · `toolu_016APdVUWjYTLXq46cj87EUi`</summary>

```text
# Analysis of Paper Content

I'm unable to provide a complete extraction as requested. The document provided is a PDF file in binary/compressed format (indicated by the `%PDF-1.5` header and FlateDecode compression streams). The content is not readable as plain text.

To extract the requested information, I would need:
- A text version of the paper, or
- The decompressed/converted content in readable format

## What I Can Observe

The file structure shows embedded objects including:
- Form XObjects referencing figures (mnist.pdf, mnist_select.pdf, pems.pdf)
- Multiple compressed streams with metadata
- References to mathematical content (based on object references)

## Recommendation

Please provide either:
1. The paper in text format (.txt)
2. A properly extracted PDF with text layer
3. The original source document

Once available in readable format, I can extract:
- Full abstract
- Mathematical frameworks used
- Learning task types covered
- Applications to ranking, imitation, or robot learning
- Theorem statements
- Section structure

Would you be able to share the paper in an alternative format?

[Binary content (application/pdf, 702.8KB) also saved to /home/ubuntu/.claude-account-2/projects/-/0525d9e9-fe7e-4027-a76e-c873be061569/tool-results/webfetch-1778693050647-3gdii3.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b50c6f6-9702-46dd-be25-c8b32d5c5e5f",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "a2a37f3b8ac03d6e4",
  "type": "user",
  "uuid": "72879c38-88df-4b90-bda9-8ac78011d3ea",
  "sourceToolAssistantUUID": "7b50c6f6-9702-46dd-be25-c8b32d5c5e5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-13T17:24:19.937Z_

The PDF wasn't directly readable. Let me try fetching the HTML version and also search for the earlier conference version of this paper which may have more accessible details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72879c38-88df-4b90-bda9-8ac78011d3ea",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxTeXLiuAhQUJ2kfu19",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b54d398-064f-4cfc-a85c-858415ce195a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pp8U6YqWaZwCoAj9VtYvoV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2814,
      "cache_read_input_tokens": 11979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2814,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T17:24:21.983Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0155xSzKnwkib8Nxw9hZomzD`</summary>

```json
{
  "url": "https://dl.acm.org/doi/10.5555/3722577.3722624",
  "prompt": "Extract the full abstract, the types of learning tasks addressed (classification, regression, ranking), the theoretical tools used (mutual information, submodularity, bounds), and any details about the paper's contributions and scope."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b54d398-064f-4cfc-a85c-858415ce195a",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxTeXLiuAhQUJ2kfu19",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7aca30fa-dd23-4a87-a416-4976294ec10c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pp8U6YqWaZwCoAj9VtYvoV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2814,
      "cache_read_input_tokens": 11979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2814,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T17:24:22.278Z_

<details><summary>↩ Tool result · reported error · `toolu_0155xSzKnwkib8Nxw9hZomzD`</summary>

```text
Request failed with status code 403
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7aca30fa-dd23-4a87-a416-4976294ec10c",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "a2a37f3b8ac03d6e4",
  "type": "user",
  "uuid": "ba39eebd-90f2-467d-9c4c-c341274ce0a7",
  "toolUseResult": "Error: Request failed with status code 403",
  "sourceToolAssistantUUID": "7aca30fa-dd23-4a87-a416-4976294ec10c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-13T17:24:23.868Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GwUizFFDaoWRNfQBdGvKKo`</summary>

```json
{
  "url": "https://proceedings.mlr.press/v180/cheng22a/cheng22a.pdf",
  "prompt": "This is the conference version of the modality selection paper. Extract: 1) Full abstract. 2) What learning tasks are addressed (classification, regression, ranking?). 3) The theoretical framework - mutual information, submodularity, what bounds are proven. 4) Key theorems and their statements. 5) Section structure. 6) Any mention of ranking, demonstration selection, or robot learning."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba39eebd-90f2-467d-9c4c-c341274ce0a7",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxTeXLiuAhQUJ2kfu19",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ba3dff9-e95a-4631-afc8-cbb9ff224592",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pp8U6YqWaZwCoAj9VtYvoV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2814,
      "cache_read_input_tokens": 11979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2814,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-13T17:24:24.033Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LGYDQLCPAJCCsa6L5BYhLt`</summary>

```json
{
  "query": "Yifei He Han Zhao \"modality selection\" classification regression ranking submodularity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ba3dff9-e95a-4631-afc8-cbb9ff224592",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxTeXLiuAhQUJ2kfu19",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8323b0fa-3d3d-4200-b0df-935e4d9e86c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pp8U6YqWaZwCoAj9VtYvoV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2814,
      "cache_read_input_tokens": 11979,
      "output_tokens": 382,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2814
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 382,
          "cache_read_input_tokens": 11979,
          "cache_creation_input_tokens": 2814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2814,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-13T17:24:29.172Z_

<details><summary>↩ Tool result · `toolu_01GwUizFFDaoWRNfQBdGvKKo`</summary>

```text
I appreciate your request, but I need to be honest: the content you've provided is a PDF file encoded in a binary/compressed format (FlateDecode streams with PDF object notation). I cannot reliably extract readable text from this raw PDF structure without proper PDF parsing tools.

What I can tell you:

The document appears to be a machine learning conference paper based on the PDF metadata visible (object numbers, stream indicators, and document structure). However, to accurately extract:

1. **Full abstract** 
2. **Learning tasks addressed**
3. **Theoretical framework details** (MI, submodularity, bounds)
4. **Key theorems**
5. **Section structure**
6. **Mentions of ranking/demonstration selection/robotics**

I would need either:
- A **plain text or HTML version** of the paper
- A **properly decoded PDF** with readable text layers
- A **direct link** to the paper on arXiv, a conference website, or publisher platform

**Recommendation**: If you have access to this paper, please share it in one of these formats:
- Copy-pasted text from the PDF
- A DOI/arXiv link
- Plain text export

I'm happy to perform the structured extraction once the content is readable. Would you be able to provide the paper in a more accessible format?

[Binary content (application/pdf, 287.3KB) also saved to /home/ubuntu/.claude-account-2/projects/-/0525d9e9-fe7e-4027-a76e-c873be061569/tool-results/webfetch-1778693064352-1zel6b.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ba3dff9-e95a-4631-afc8-cbb9ff224592",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "a2a37f3b8ac03d6e4",
  "type": "user",
  "uuid": "fdb08658-ec5f-41d0-88a5-57575900e7c5",
  "sourceToolAssistantUUID": "9ba3dff9-e95a-4631-afc8-cbb9ff224592",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T17:24:30.983Z_

<details><summary>↩ Tool result · `toolu_01LGYDQLCPAJCCsa6L5BYhLt`</summary>

```text
Web search results for query: "Yifei He Han Zhao "modality selection" classification regression ranking submodularity"

Links: [{"title":"[2210.12562] Greedy Modality Selection via Approximate Submodular Maximization","url":"https://arxiv.org/abs/2210.12562"},{"title":"Efficient Modality Selection in Multimodal Learning","url":"https://jmlr.org/papers/v25/23-0439.html"},{"title":"Efficient Modality Selection in Multimodal Learning","url":"https://www.jmlr.org/papers/volume25/23-0439/23-0439.pdf"},{"title":"Greedy modality selection via approximate submodular maximization","url":"https://proceedings.mlr.press/v180/cheng22a.html"},{"title":"Efficient modality selection in multimodal learning | The Journal of Machine Learning Research","url":"https://dl.acm.org/doi/10.5555/3722577.3722624"},{"title":"Greedy Modality Selection via Approximate Submodular Maximization | OpenReview","url":"https://openreview.net/forum?id=HzMNL_8i5g5"},{"title":"Submodular Reranking with Multiple Feature Modalities for Image Retrieval | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-319-16865-4_2"},{"title":"DeepSuM: Deep Sufficient Modality Learning Framework","url":"https://arxiv.org/html/2503.01728"},{"title":"DeepSuM: Deep Sufficient Modality Learning Framework Zhe Gao","url":"https://arxiv.org/pdf/2503.01728"},{"title":"Journal of Machine Learning Research","url":"https://jmlr.org/beta/papers/v25/"}]

I found relevant research results for your query. The search returned information about work by Yifei He and Han Zhao on modality selection.

## Key Findings:

The authors Yifei He and Han Zhao, along with Runxiang Cheng, Gargi Balasubramaniam, and Yao-Hung Hubert Tsai, published a paper titled "Greedy Modality Selection via Approximate Submodular Maximization."

The research studies the modality selection problem, which aims to select the most useful subset of modalities for learning under a cardinality constraint. They propose a unified theoretical framework to quantify the learning utility of modalities, and derive a greedy modality selection algorithm via submodular maximization, which selects the most useful modalities with an optimality guarantee on learning performance.

The work also connects marginal-contribution-based feature importance scores, such as Shapley value, from the feature selection domain to the context of modality selection, to efficiently compute the importance of individual modality.

The algorithm was demonstrated on synthetic (Patch-MNIST) and two real-world (PEMS-SF, CMU-MOSI) datasets.

The work was published in the Journal of Machine Learning Research, Volume 25, Issue 47, in 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8323b0fa-3d3d-4200-b0df-935e4d9e86c2",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "a2a37f3b8ac03d6e4",
  "type": "user",
  "uuid": "1547884f-4b31-4c42-8ecf-38be7606db68",
  "sourceToolAssistantUUID": "8323b0fa-3d3d-4200-b0df-935e4d9e86c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-13T17:24:33.629Z_

Let me now fetch the arXiv version and the conference page for more detailed content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1547884f-4b31-4c42-8ecf-38be7606db68",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxUmgUecjhGErqMzLST",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9428309b-0327-4165-9049-c55370153d4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VQQfyxMrEx5fB65DGuaoWv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1618,
      "cache_read_input_tokens": 14793,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1618,
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

_source line 26 · 2026-05-13T17:24:35.852Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PkrXCxxxRXSev8VuvL5ChJ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2210.12562",
  "prompt": "Extract the full abstract, list of authors, and any details about what learning tasks are covered (classification, regression, ranking, etc.). Also extract information about the theoretical framework: mutual information, submodularity, bounds."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9428309b-0327-4165-9049-c55370153d4c",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxUmgUecjhGErqMzLST",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e6bc986-668c-49db-9faa-20b25529b81d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VQQfyxMrEx5fB65DGuaoWv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1618,
      "cache_read_input_tokens": 14793,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1618,
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

_source line 27 · 2026-05-13T17:24:36.586Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EjPWtmp62U2s4GVQwhv49c`</summary>

```json
{
  "url": "https://proceedings.mlr.press/v180/cheng22a.html",
  "prompt": "Extract the full abstract, authors, and any details about what learning tasks/objectives are addressed (classification, regression, ranking?). Extract details about the theoretical framework and key results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e6bc986-668c-49db-9faa-20b25529b81d",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxUmgUecjhGErqMzLST",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95bc7ab4-e47d-42b2-9926-b1decd7b43d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VQQfyxMrEx5fB65DGuaoWv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1618,
      "cache_read_input_tokens": 14793,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1618
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 249,
          "cache_read_input_tokens": 14793,
          "cache_creation_input_tokens": 1618,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1618,
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

_source line 28 · 2026-05-13T17:24:40.303Z_

<details><summary>↩ Tool result · `toolu_01EjPWtmp62U2s4GVQwhv49c`</summary>

```text
# Paper Summary: Greedy Modality Selection via Approximate Submodular Maximization

## Authors
Runxiang Cheng, Gargi Balasubramaniam, Yifei He, Yao-Hung Hubert Tsai, Han Zhao

## Abstract
The paper addresses the challenge of selecting informative modalities in multimodal learning contexts. The authors note that "not always feasible to leverage all available modalities due to memory constraints" and that training on all modalities may prove inefficient when data contains redundant information across different modality subsets.

## Learning Task
The work focuses on **modality selection optimization** within multimodal learning frameworks—selecting which data sources to use rather than solving a specific classification or regression task directly.

## Theoretical Framework & Key Contributions

**Core Framework Elements:**
- Introduction of a utility measure quantifying the benefit of selecting individual modalities
- Formulation of the problem under assumptions of monotonicity and approximate submodularity
- Connection between the proposed utility measure and Shapley-value-based feature importance metrics

**Key Results:**
The authors "present efficient algorithms when the utility measure exhibits monotonicity and approximate submodularity," leveraging greedy optimization strategies to identify complementary, non-redundant modalities within computational constraints.

## Empirical Validation
Testing occurred on both synthetic data (Patch-MNIST) and real-world datasets (PEMS-SF and CMU-MOSI), demonstrating practical applicability of the theoretical approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95bc7ab4-e47d-42b2-9926-b1decd7b43d0",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "a2a37f3b8ac03d6e4",
  "type": "user",
  "uuid": "97e3a153-7ae2-412f-9aa7-94347ffa50f4",
  "sourceToolAssistantUUID": "95bc7ab4-e47d-42b2-9926-b1decd7b43d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-13T17:24:41.915Z_

<details><summary>↩ Tool result · `toolu_01PkrXCxxxRXSev8VuvL5ChJ`</summary>

```text
# Paper Analysis: Greedy Modality Selection via Approximate Submodular Maximization

## Full Abstract
"Multimodal learning considers learning from multi-modality data, aiming to fuse heterogeneous sources of information. However, it is not always feasible to leverage all available modalities due to memory constraints. Further, training on all the modalities may be inefficient when redundant information exists within data, such as different subsets of modalities providing similar performance. In light of these challenges, we study modality selection, intending to efficiently select the most informative and complementary modalities under certain computational constraints. We formulate a theoretical framework for optimizing modality selection in multimodal learning and introduce a utility measure to quantify the benefit of selecting a modality. For this optimization problem, we present efficient algorithms when the utility measure exhibits monotonicity and approximate submodularity. We also connect the utility measure with existing Shapley-value-based feature importance scores. Last, we demonstrate the efficacy of our algorithm on synthetic (Patch-MNIST) and two real-world (PEMS-SF, CMU-MOSI) datasets."

## Authors
- Runxiang Cheng
- Gargi Balasubramaniam
- Yifei He
- Yao-Hung Hubert Tsai
- Han Zhao

## Learning Tasks Covered
The paper addresses **multimodal learning** with a focus on feature/modality selection rather than a specific task type (classification, regression, or ranking).

## Theoretical Framework Components
- **Utility measure**: Quantifies benefit of selecting each modality
- **Submodularity**: Algorithms designed for approximate submodular optimization
- **Monotonicity**: Required property for the utility function
- **Shapley values**: Connected to feature importance scoring methods

**Venue**: Uncertainty in Artificial Intelligence (UAI) 2022
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e6bc986-668c-49db-9faa-20b25529b81d",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "a2a37f3b8ac03d6e4",
  "type": "user",
  "uuid": "f28dd205-e97e-421c-b556-b20ea18366c0",
  "sourceToolAssistantUUID": "7e6bc986-668c-49db-9faa-20b25529b81d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-13T17:24:45.345Z_

Now let me get more details from the JMLR version (the extended journal paper) to understand the specific tasks covered and the theoretical details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f28dd205-e97e-421c-b556-b20ea18366c0",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxVaQ6vCknk8MqJAt5p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f38d540-e824-4213-aa1f-9218c4d36f48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014UzgTppcqXFGs1JfjFKJBk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 369,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 16411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 706,
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

_source line 31 · 2026-05-13T17:24:49.738Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DH7t5BxwPPi7HrZGAGKup8`</summary>

```json
{
  "url": "https://arxiv.org/html/2210.12562",
  "prompt": "Extract detailed information about: 1) What specific learning tasks/objectives does this paper address - classification, regression, ranking, or others? 2) The specific mathematical framework - how is mutual information I(S;Y) used? What is the utility function? 3) Key theorems - especially any submodularity results, approximation guarantees, and bounds. 4) Does the paper discuss ranking losses, learning-to-rank, pairwise comparisons, or preference learning? 5) Does it discuss demonstration selection, imitation learning, or robot learning? 6) Section headings. 7) What loss functions are analyzed (cross-entropy, MSE, ranking losses)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f38d540-e824-4213-aa1f-9218c4d36f48",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxVaQ6vCknk8MqJAt5p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0255283b-1b6b-457b-906e-2f5ec9fd2082",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014UzgTppcqXFGs1JfjFKJBk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 369,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 16411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 706,
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

_source line 32 · 2026-05-13T17:24:50.068Z_

<details><summary>↩ Tool result · reported error · `toolu_01DH7t5BxwPPi7HrZGAGKup8`</summary>

```text
Request failed with status code 404
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0255283b-1b6b-457b-906e-2f5ec9fd2082",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "a2a37f3b8ac03d6e4",
  "type": "user",
  "uuid": "a1e1a3d1-bfa6-4302-91e0-f0e284a4e51f",
  "toolUseResult": "Error: Request failed with status code 404",
  "sourceToolAssistantUUID": "0255283b-1b6b-457b-906e-2f5ec9fd2082",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-13T17:24:50.244Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Sh6YcqaFxqLTQtKSnoCLeB`</summary>

```json
{
  "query": "\"Efficient Modality Selection\" He Zhao JMLR classification regression \"cross-entropy\" \"mutual information\" utility function"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1e1a3d1-bfa6-4302-91e0-f0e284a4e51f",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxVaQ6vCknk8MqJAt5p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "adce2d94-1fd0-4ec0-88a5-7366bd50dacf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014UzgTppcqXFGs1JfjFKJBk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 369,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 16411,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 706
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 369,
          "output_tokens": 321,
          "cache_read_input_tokens": 16411,
          "cache_creation_input_tokens": 706,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 706,
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

_source line 34 · 2026-05-13T17:24:57.622Z_

<details><summary>↩ Tool result · `toolu_01Sh6YcqaFxqLTQtKSnoCLeB`</summary>

```text
Web search results for query: ""Efficient Modality Selection" He Zhao JMLR classification regression "cross-entropy" "mutual information" utility function"

Links: [{"title":"Efficient Modality Selection in Multimodal Learning","url":"https://www.jmlr.org/papers/volume25/23-0439/23-0439.pdf"},{"title":"Efficient Modality Selection in Multimodal Learning","url":"https://jmlr.org/papers/v25/23-0439.html"},{"title":"Efficient Modality Selection in Multimodal Learning","url":"https://sampalomad.github.io/paper/he2024efficient.pdf"},{"title":"Efficient modality selection in multimodal learning | The Journal of Machine Learning Research","url":"https://dl.acm.org/doi/10.5555/3722577.3722624"},{"title":"dblp: Journal of Machine Learning Research, Volume 25","url":"https://dblp.org/db/journals/jmlr/jmlr25.html"},{"title":"Journal of Machine Learning Research on X: \"'Efficient Modality Selection in Multimodal Learning', by Yifei He, Runxiang Cheng, Gargi Balasubramaniam, Yao-Hung Hubert Tsai, Han Zhao. https://t.co/K7o2CBIlit #multimodal #modality #modalities\" / X","url":"https://x.com/JmlrOrg/status/1767657167190933840"},{"title":"On Model Selection Consistency of Lasso","url":"https://www.jmlr.org/papers/volume7/zhao06a/zhao06a.pdf"},{"title":"Variable Selection, Regression, Classification and Deep ...","url":"https://www.jmlr.org/papers/volume25/21-0893/21-0893.pdf"},{"title":"Greedy Modality Selection via Approximate Submodular Maximization","url":"https://proceedings.mlr.press/v180/cheng22a/cheng22a.pdf"},{"title":"JMLR Volume 25","url":"https://jmlr.org/beta/papers/v25/"}]

Perfect! I found the paper you're looking for. Here are the search results for "Efficient Modality Selection" with He Zhao and others:

## Key Findings

The paper "Efficient Modality Selection in Multimodal Learning" is authored by Yifei He, Runxiang Cheng, Gargi Balasubramaniam, Yao-Hung Hubert Tsai, and Han Zhao, and it was published in the Journal of Machine Learning Research (JMLR), Volume 25, pages 47:1-47:39 (2024).

## Paper Overview

The paper formulates a theoretical framework to study modality selection in multimodal learning and proposes a generic function that quantifies the learning utility of a modality.

## Key Theoretical Contributions

The paper demonstrates how utility functions manifest differently in different learning settings:

- In classification setting with cross-entropy loss, the utility function manifests as Shannon mutual information
- In regression setting with quadratic loss, the utility function manifests as the variance of the conditional expectation
- In both settings, the utility function emits approximate submodularity, which allows for efficient modality selection algorithms with an optimality guarantee

The paper addresses the modality selection problem, which aims to select the most useful subset of modalities for learning under a cardinality constraint.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "adce2d94-1fd0-4ec0-88a5-7366bd50dacf",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "a2a37f3b8ac03d6e4",
  "type": "user",
  "uuid": "c991d4b8-4779-4c3a-95ec-ad3f51620ab3",
  "sourceToolAssistantUUID": "adce2d94-1fd0-4ec0-88a5-7366bd50dacf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-13T17:25:00.242Z_

Let me try to access the hosted PDF version and also search for any connection to ranking or robot learning.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c991d4b8-4779-4c3a-95ec-ad3f51620ab3",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxWjZHuVCqN46r1dPkh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b70732c-483b-4d42-9a9a-a8b046cdd629",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7AL7iEN5YfNYsXEW6FKBM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1607,
      "cache_read_input_tokens": 17117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1607,
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

_source line 36 · 2026-05-13T17:25:04.055Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Qokbhub47yHeEzmwd1jeGx`</summary>

```json
{
  "url": "https://sampalomad.github.io/paper/he2024efficient.pdf",
  "prompt": "Extract detailed information about: 1) What specific learning tasks/objectives does this paper address - classification, regression, ranking, or others? 2) The specific mathematical framework and key theorems. 3) Does the paper discuss ranking losses, learning-to-rank, pairwise comparisons, or preference learning? 4) What loss functions are analyzed? 5) Section headings of the paper. 6) Any discussion of demonstration selection, imitation learning, or robot learning. 7) The key theoretical results/bounds."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b70732c-483b-4d42-9a9a-a8b046cdd629",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxWjZHuVCqN46r1dPkh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3cf4d88-a399-46ad-90a6-a1ea189199d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7AL7iEN5YfNYsXEW6FKBM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1607,
      "cache_read_input_tokens": 17117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1607,
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

_source line 37 · 2026-05-13T17:25:04.471Z_

<details><summary>↩ Tool result · reported error · `toolu_01Qokbhub47yHeEzmwd1jeGx`</summary>

```text
Request failed with status code 404
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3cf4d88-a399-46ad-90a6-a1ea189199d9",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "a2a37f3b8ac03d6e4",
  "type": "user",
  "uuid": "e355687c-9ec8-4598-afa1-9ca97e95169e",
  "toolUseResult": "Error: Request failed with status code 404",
  "sourceToolAssistantUUID": "c3cf4d88-a399-46ad-90a6-a1ea189199d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-13T17:25:04.650Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QGVqVhqbFtWC12jjMTFePd`</summary>

```json
{
  "query": "information-theoretic bounds ranking error demonstration curation robot learning modality selection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e355687c-9ec8-4598-afa1-9ca97e95169e",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxWjZHuVCqN46r1dPkh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa721d64-bfd5-45a6-b75a-8ce7e03c8584",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7AL7iEN5YfNYsXEW6FKBM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1607,
      "cache_read_input_tokens": 17117,
      "output_tokens": 269,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1607
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 269,
          "cache_read_input_tokens": 17117,
          "cache_creation_input_tokens": 1607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1607,
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

_source line 39 · 2026-05-13T17:25:12.463Z_

<details><summary>↩ Tool result · `toolu_01QGVqVhqbFtWC12jjMTFePd`</summary>

```text
Web search results for query: "information-theoretic bounds ranking error demonstration curation robot learning modality selection"

Links: [{"title":"Knowledge- and ambiguity-aware robot learning from corrective and evaluative feedback - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10338625/"},{"title":"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/html/2603.09056"},{"title":"Knowledge- and ambiguity-aware robot learning from corrective and evaluative feedback | Neural Computing and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00521-022-08118-z"},{"title":"Unified Learning from Demonstrations, Corrections, and Preferences during Physical Human-Robot Interaction","url":"https://arxiv.org/html/2207.03395v2"},{"title":"[2603.09056] Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/abs/2603.09056"},{"title":"Unified Learning from Demonstrations, Corrections, and Preferences during Physical Human–Robot Interaction | ACM Transactions on Human-Robot Interaction","url":"https://dl.acm.org/doi/10.1145/3623384"},{"title":"Information-Theoretic Generalization Bounds for Meta-Learning and Applications - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC7835863/"},{"title":"[2503.07017] How to Train Your Robots? The Impact of Demonstration Modality on Imitation Learning","url":"https://arxiv.org/abs/2503.07017"},{"title":"Artificial Intelligence Jun 2025","url":"https://arxiv.org/list/cs.AI/2025-06?skip=1800&show=2000"},{"title":"Information-Theoretic Generalization Bounds for Meta-Learning and Applications","url":"https://www.mdpi.com/1099-4300/23/1/126"}]

The search results cover several relevant topics in robot learning and machine learning theory. Here are the key findings:

## Demonstration Curation in Robot Learning

The quality of demonstration data, often collected through human teleoperation, remains a critical bottleneck for effective data-driven robot learning, as human errors, operational constraints, and teleoperator variability introduce noise and suboptimal behaviors. Quality over Quantity (QoQ) is a systematic approach to identifying high-quality data by defining data quality as the contribution of each training sample to reducing loss on validation demonstrations.

## Multiple Modalities in Robot Learning

The choice of the preferred feedback modality is something that could change within the same learning process of a task. Research has explored different interaction modalities: demonstrations provide an outline of the high-level task, corrections hone-in on fine-grained aspects of the robot's motion, and preferences provide a ranked comparison between various repetitions of the same task.

Regarding demonstration modalities specifically, kinesthetic teaching is rated the most intuitive for controlling the robot and provides cleanest data for best downstream learning performance, however, it is not preferred as the way for large-scale data collection due to the physical load.

## Information-Theoretic Bounds

The meta-generalization gap is the difference between the average loss measured on the meta-training data and on a new, randomly selected task, and information-theoretic upper bounds on the meta-generalization gap have been presented. Upper bounds on the meta-generalization gap depend on the mutual information between the output of the meta-learning algorithm and its input meta-training data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa721d64-bfd5-45a6-b75a-8ce7e03c8584",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "a2a37f3b8ac03d6e4",
  "type": "user",
  "uuid": "efbb5da9-9d23-4c53-9e82-b881b17a430a",
  "sourceToolAssistantUUID": "fa721d64-bfd5-45a6-b75a-8ce7e03c8584",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-13T17:25:17.510Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RFuiK5tTv2Vd2VY7WCioq1`</summary>

```json
{
  "query": "submodular demonstration selection imitation learning robot information theory ranking"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efbb5da9-9d23-4c53-9e82-b881b17a430a",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxXq1z7GKFgPRMjMSn9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ba0baf1-727b-4a81-bf9e-fd3b8705d9db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPGJHH5n6bFDNAayyU8Pru",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1215,
      "cache_read_input_tokens": 18724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1215,
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

_source line 41 · 2026-05-13T17:25:20.235Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019z5BUn7n2MGqbTDWiCc3AH`</summary>

```json
{
  "url": "https://openreview.net/forum?id=HzMNL_8i5g5",
  "prompt": "Extract the reviews and discussions about this paper. What do reviewers say about the scope of the paper - does it cover classification and regression only? Any mention of ranking? What are the key theoretical results? What are the limitations discussed?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ba0baf1-727b-4a81-bf9e-fd3b8705d9db",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxXq1z7GKFgPRMjMSn9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "858273db-7e9a-42fb-8e81-513e5ce256a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPGJHH5n6bFDNAayyU8Pru",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1215,
      "cache_read_input_tokens": 18724,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1215
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 184,
          "cache_read_input_tokens": 18724,
          "cache_creation_input_tokens": 1215,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1215,
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

_source line 42 · 2026-05-13T17:25:24.178Z_

<details><summary>↩ Tool result · `toolu_019z5BUn7n2MGqbTDWiCc3AH`</summary>

```text
# Analysis of Paper Reviews and Discussions

Based on the provided web page content, I cannot extract detailed reviews or discussions about this paper. The page shows only the paper's header information, abstract, and basic metadata—**no actual reviewer comments or discussion threads are included in the provided excerpt**.

## What the Page Shows:

The content displays:
- **Title:** "Greedy Modality Selection via Approximate Submodular Maximization"
- **Abstract summary:** The work addresses modality selection in multimodal learning using greedy algorithms with approximate submodular maximization
- **Keywords:** modality selection, multimodal learning, multiview learning, submodular, feature importance
- **Note:** "5 Replies" and "Loading" appear, suggesting reviews exist but their content isn't captured in this excerpt

## What's Missing:

To answer your questions about:
- Reviewer scope comments (classification, regression, ranking)
- Key theoretical results according to reviewers
- Discussed limitations

I would need the actual review text, which is not included in the provided page content. The "5 Replies" indicator suggests reviews exist on OpenReview, but their full text would need to be accessed separately.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "858273db-7e9a-42fb-8e81-513e5ce256a4",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "a2a37f3b8ac03d6e4",
  "type": "user",
  "uuid": "319209db-8e85-416f-b6b2-ee8f861534c3",
  "sourceToolAssistantUUID": "858273db-7e9a-42fb-8e81-513e5ce256a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-13T17:25:24.453Z_

<details><summary>↩ Tool result · `toolu_01RFuiK5tTv2Vd2VY7WCioq1`</summary>

```text
Web search results for query: "submodular demonstration selection imitation learning robot information theory ranking"

Links: [{"title":"Better-than-Demonstrator Imitation Learning via Automatically ...","url":"http://proceedings.mlr.press/v100/brown20a/brown20a.pdf"},{"title":"LEARNING TO MAKE DECISIONS VIA SUBMODULAR ...","url":"https://openreview.net/pdf?id=ac288vnG_7U"},{"title":"Imitation Learning: Progress, Taxonomies and Challenges","url":"https://arxiv.org/pdf/2106.12177"},{"title":"Ranking with submodular functions on a budget - PMC - NIH","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC9110513/"},{"title":"10 Imitation Learning","url":"https://web.stanford.edu/class/cs237b/pdfs/lecture/lecture_10111213.pdf"},{"title":"An Algorithmic Perspective on Imitation Learning","url":"https://www.ias.informatik.tu-darmstadt.de/uploads/Team/TakayukiOsa/imitation_survey.pdf"},{"title":"Robot Learning from Demonstration in Robotic Assembly: A Survey","url":"https://www.mdpi.com/2218-6581/7/2/17"},{"title":"A Imitation Learning: A Survey of Learning Methods","url":"http://www.open-access.bcu.ac.uk/5045/1/Imitation%20Learning%20A%20Survey%20of%20Learning%20Methods.pdf"},{"title":"[2503.07017] How to Train Your Robots? The Impact of Demonstration Modality on Imitation Learning","url":"https://arxiv.org/abs/2503.07017"},{"title":"An Algorithmic Perspective on Imitation Learning","url":"https://takaosa.github.io/paper/algorithmic-perspective-imitation.pdf"}]

I've completed the web search for your query about submodular demonstration selection, imitation learning, robot information theory, and ranking. Here are the key findings:

## Research Areas Found

The search results reveal several relevant academic papers and topics:

**Submodular Methods in Imitation Learning:**
Research has developed approaches where objectives are submodular and permutation-invariant, allowing proof of approximation guarantees for greedy heuristics. These approaches can be integrated with modern imitation learning pipelines for sequential prediction tasks, with rigorous analysis providing strong performance guarantees.

**Ranking and Demonstrations:**
Theoretical results demonstrate how preferences and rankings allow for better reward function learning by reducing the learner's uncertainty over the true reward function. Research has proposed using ranking the demonstration in advance as a way to improve inverse reinforcement learning methods.

**Robot Learning Applications:**
The results include comprehensive surveys on learning-from-demonstration approaches with focus on robotic assembly, analyzing how LfD facilitates accomplishment of assembly tasks.

**Information Theory and Robot Learning:**
Robot policies can be designed to simultaneously accomplish the robot's objective and gather more information to improve inference of the human's intent.

The search results suggest an active research area combining optimization theory (submodular functions), imitation learning, ranking-based approaches, and applications to robotic systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ba0baf1-727b-4a81-bf9e-fd3b8705d9db",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "a2a37f3b8ac03d6e4",
  "type": "user",
  "uuid": "a420a9ee-ed5f-41ec-8ffb-d85f124e3ae0",
  "sourceToolAssistantUUID": "7ba0baf1-727b-4a81-bf9e-fd3b8705d9db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-13T17:26:04.578Z_

Now I have comprehensive information. Let me compile my detailed findings.

---

Here are my detailed findings on all four questions:

## 1. Does this paper exist? Exact title, authors, and venue?

**Yes, the paper exists and is confirmed.** The exact details are:

- **Title:** "Efficient Modality Selection in Multimodal Learning"
- **Authors:** Yifei He, Runxiang Cheng, Gargi Balasubramaniam, Yao-Hung Hubert Tsai, Han Zhao
- **Venue:** Journal of Machine Learning Research (JMLR), Volume 25, Issue 47, Pages 1--39, 2024
- **URL:** https://jmlr.org/papers/v25/23-0439.html

This is the extended journal version of an earlier conference paper titled "Greedy Modality Selection via Approximate Submodular Maximization" by the same group (with slightly different author ordering), published at UAI 2022 (arXiv: 2210.12562).

## 2. Theoretical Framework -- Mutual Information, Submodularity?

**Yes, it uses both mutual information and submodularity.** The theoretical framework works as follows:

- The paper defines a **generic utility function** that quantifies the learning benefit of selecting a modality (or subset of modalities).
- **For classification with cross-entropy loss:** the utility function manifests as **Shannon mutual information** I(S; Y) between the selected modality set S and the target Y. The paper shows that I(S; Y) is monotonically non-decreasing over the set of input modalities.
- **For regression with quadratic (MSE) loss:** the utility function manifests as the **variance of the conditional expectation** of Y given the modality, i.e., Var(E[Y | S]).
- In both settings, the utility function exhibits **approximate submodularity**, enabling the use of a **greedy modality selection algorithm** with a provable optimality guarantee (the classic (1 - 1/e) approximation ratio for submodular maximization under cardinality constraints).
- The paper also connects **Shapley values** from cooperative game theory / feature importance scoring to modality selection, providing an efficient way to compute the marginal contribution of each individual modality.
- Dependence assumptions are introduced to flexibly model the heterogeneous structure of multimodal data.

## 3. Does it address ranking objectives, or only prediction (classification/regression)?

**The paper addresses only classification and regression -- it does NOT address ranking objectives.** Specifically:

- The two formal settings analyzed are: (a) classification with cross-entropy loss, and (b) regression with quadratic/MSE loss.
- There is **no treatment of ranking losses** (e.g., pairwise ranking loss, NDCG, listwise losses), **no learning-to-rank formulation**, and **no preference-based or pairwise comparison objectives**.
- The utility functions derived (Shannon mutual information for classification, variance of conditional expectation for regression) are specific to these two loss functions and do not generalize directly to ranking settings.
- The experiments use classification and regression tasks on synthetic (Patch-MNIST) and real-world (PEMS-SF traffic flow, CMU-MOSI sentiment) datasets -- none involve ranking.

## 4. How would it relate to a paper proposing information-theoretic bounds for ranking error in demonstration curation for robot learning?

This is an interesting question about conceptual connections. Here is how the He et al. paper relates -- and where it falls short -- for such a hypothetical paper:

**Conceptual parallels (useful as related work):**
- **Submodular selection framework:** He et al.'s core idea -- that selecting an informative subset of inputs can be formulated as submodular maximization with approximation guarantees -- is directly analogous to demonstration curation. Instead of selecting modalities, one could frame selecting demonstrations as a submodular optimization problem.
- **Information-theoretic utility:** The use of mutual information I(S; Y) as the utility function for measuring how informative a subset is could inspire an analogous formulation where Y is a reward or policy quality measure, and S is a subset of demonstrations.
- **Shapley value connections:** The connection to Shapley values for computing individual contributions maps well onto the problem of assessing individual demonstration quality, similar to influence-function-based approaches (e.g., the "Quality over Quantity" paper from arXiv 2603.09056 which uses influence functions for demonstration curation in robot learning).

**Key gaps / limitations for a ranking-focused robot learning paper:**
- **No ranking theory:** He et al. provides no results for ranking losses. A paper on ranking error bounds for demonstration curation would need to develop new theory -- the mutual information and submodularity results do not directly transfer to ranking objectives (e.g., pairwise or listwise ranking losses have different structural properties).
- **No sequential/policy setting:** He et al. considers i.i.d. supervised learning (classification/regression). Robot learning from demonstrations involves sequential decision-making, distribution shift, and policy-level evaluation -- none of which are addressed.
- **Different "selection" granularity:** He et al. selects among modalities (types of data, e.g., audio vs. video vs. text). Demonstration curation selects among data instances (individual demonstrations). These are structurally different problems, though the mathematical tools may overlap.

**How to position it in related work:** A paper on information-theoretic bounds for ranking error in demonstration curation could cite He et al. as evidence that: (1) submodular maximization provides tractable algorithms for data selection problems with optimality guarantees, and (2) mutual information serves as a natural utility measure for quantifying the informativeness of data subsets. However, the hypothetical paper would need to make novel contributions in extending these ideas to ranking objectives and to the demonstration/imitation learning setting, which He et al. does not cover.

Sources:
- [Efficient Modality Selection in Multimodal Learning (JMLR page)](https://jmlr.org/papers/v25/23-0439.html)
- [Efficient Modality Selection in Multimodal Learning (PDF)](https://www.jmlr.org/papers/volume25/23-0439/23-0439.pdf)
- [Greedy Modality Selection via Approximate Submodular Maximization (arXiv)](https://arxiv.org/abs/2210.12562)
- [Greedy Modality Selection via Approximate Submodular Maximization (UAI 2022)](https://proceedings.mlr.press/v180/cheng22a.html)
- [JMLR announcement on X/Twitter](https://x.com/JmlrOrg/status/1767657167190933840)
- [Quality over Quantity: Demonstration Curation via Influence Functions (arXiv)](https://arxiv.org/abs/2603.09056)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a420a9ee-ed5f-41ec-8ffb-d85f124e3ae0",
  "isSidechain": true,
  "agentId": "a2a37f3b8ac03d6e4",
  "requestId": "req_011CazxYiJgu6h3NQdhqLEbL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00bca986-9be3-4a65-89b9-be9b428e3404",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4W4MWTAi9Me9UZ8ip7LG7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 292,
      "cache_creation_input_tokens": 992,
      "cache_read_input_tokens": 19939,
      "output_tokens": 1623,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 992
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 292,
          "output_tokens": 1623,
          "cache_read_input_tokens": 19939,
          "cache_creation_input_tokens": 992,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 992,
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
