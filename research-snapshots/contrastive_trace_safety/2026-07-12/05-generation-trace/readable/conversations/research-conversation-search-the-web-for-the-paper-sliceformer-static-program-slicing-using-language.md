# Research conversation: Search the web for the paper "Sliceformer: Static Program Slicing Using Language Models With Dataflow-Aware Pretraining"

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a8ce9e4db0ebbe7fc.jsonl`
- **Structured JSON:** [`c60c6e05f933988ad1f5.json`](../../sessions/c6/c60c6e05f933988ad1f5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

17 recorded events

### User

_source line 1 · 2026-05-10T18:40:26.743Z_

Search the web for the paper "Sliceformer: Static Program Slicing Using Language Models With Dataflow-Aware Pretraining" (arXiv:2604.26961). I need to verify:
1. Does this paper actually exist?
2. Is it accepted at ACL 2026?
3. Does it validate data-flow knowledge transfer to neural models?
4. What are the key results (e.g., 22% ExactMatch gains)?

Use WebSearch and WebFetch to find this. Report exactly what you find.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a8ce9e4db0ebbe7fc",
  "type": "user",
  "uuid": "549ec35c-d757-4430-bb7f-ce4f2cfbcc71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:40:26.745Z_

```json
{
  "parentUuid": "549ec35c-d757-4430-bb7f-ce4f2cfbcc71",
  "isSidechain": true,
  "agentId": "a8ce9e4db0ebbe7fc",
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
      "TodoWrite",
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
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "70392fc2-5f7a-4925-b5b8-3909fa998a0d",
  "timestamp": "2026-05-10T18:40:26.745Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:40:29.081Z_



I'll search for this paper. Let me first load the WebSearch and WebFetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70392fc2-5f7a-4925-b5b8-3909fa998a0d",
  "isSidechain": true,
  "agentId": "a8ce9e4db0ebbe7fc",
  "requestId": "req_011CauNqr8j9Kg8PsPyRxAu5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0b62d85-0cf0-4a47-8466-116e720b3e81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017tnc68P8iPJ4XmtCwdqCHa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 670,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 670,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T18:40:29.253Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CM8d51kUXMjrknwwLpQx3w`</summary>

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
  "parentUuid": "c0b62d85-0cf0-4a47-8466-116e720b3e81",
  "isSidechain": true,
  "agentId": "a8ce9e4db0ebbe7fc",
  "requestId": "req_011CauNqr8j9Kg8PsPyRxAu5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff8df1c4-58b8-4d7d-86bf-04c39fd64a09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017tnc68P8iPJ4XmtCwdqCHa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 670,
      "cache_read_input_tokens": 8223,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 670
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 670,
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

_source line 5 · 2026-05-10T18:40:29.256Z_

<details><summary>↩ Tool result · `toolu_01CM8d51kUXMjrknwwLpQx3w`</summary>

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
  "parentUuid": "ff8df1c4-58b8-4d7d-86bf-04c39fd64a09",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a8ce9e4db0ebbe7fc",
  "type": "user",
  "uuid": "76881b63-ec28-4627-8ae1-7aa68fa5db23",
  "sourceToolAssistantUUID": "ff8df1c4-58b8-4d7d-86bf-04c39fd64a09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T18:40:31.795Z_



Now let me search for this paper using multiple queries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76881b63-ec28-4627-8ae1-7aa68fa5db23",
  "isSidechain": true,
  "agentId": "a8ce9e4db0ebbe7fc",
  "requestId": "req_011CauNr372zu6bvAbZmNW5v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "def97ac4-cb88-44b1-85a9-b316f02d1996",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RKmVZM8RZXsnjWpSqRq54A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T18:40:33.456Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cq7tq3exMt3MrcThuabaPo`</summary>

```json
{
  "query": "Sliceformer Static Program Slicing Language Models Dataflow-Aware Pretraining arXiv 2604.26961"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "def97ac4-cb88-44b1-85a9-b316f02d1996",
  "isSidechain": true,
  "agentId": "a8ce9e4db0ebbe7fc",
  "requestId": "req_011CauNr372zu6bvAbZmNW5v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "914271cc-71ff-4bdf-a4ea-86a0c7f146cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RKmVZM8RZXsnjWpSqRq54A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-10T18:40:33.637Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011nUJa2ZBYcfWZYo36uu947`</summary>

```json
{
  "query": "\"Sliceformer\" program slicing neural models ACL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "914271cc-71ff-4bdf-a4ea-86a0c7f146cf",
  "isSidechain": true,
  "agentId": "a8ce9e4db0ebbe7fc",
  "requestId": "req_011CauNr372zu6bvAbZmNW5v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d7fbacd-241e-44ca-9c2d-8989a2726596",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RKmVZM8RZXsnjWpSqRq54A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8893,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1910
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 146,
          "cache_read_input_tokens": 8893,
          "cache_creation_input_tokens": 1910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1910,
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

_source line 9 · 2026-05-10T18:40:39.058Z_

<details><summary>↩ Tool result · `toolu_011nUJa2ZBYcfWZYo36uu947`</summary>

```text
Web search results for query: ""Sliceformer" program slicing neural models ACL 2026"

Links: [{"title":"[2604.26961] Static Program Slicing Using Language Models With Dataflow-Aware Pretraining and Constrained Decoding","url":"https://arxiv.org/abs/2604.26961"},{"title":"Static Program Slicing Using Language Models With Dataflow-Aware Pretraining and Constrained Decoding","url":"https://arxiv.org/html/2604.26961"},{"title":"Workshops - ACL 2026","url":"https://2026.aclweb.org/program/workshops/"},{"title":"Machine Learning | ACL Member Portal","url":"https://www.aclweb.org/portal/category/topics/machine-learning"},{"title":"SLICET5: Static Program Slicing using Language Models with","url":"https://arxiv.org/pdf/2509.17338"},{"title":"AAAI-26 New Faculty Highlights Program - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/new-faculty-highlights-program/"},{"title":"ACL 2026 on X: \"🏆 ACL Best Paper Awards: - Mission: Impossible Language Models by Kallini et al. - Semisupervised Neural Proto-Language Reconstruction by Lu et al. - Why are Sensitive Functions Hard for Transformers? By Hahn et al. #NLProc #ACL2024NLP\" / X","url":"https://x.com/aclmeeting/status/1823664612581273959"},{"title":"Slice-based Learning: A Programming Model for Residual Learning in Critical Data Slices - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC6927210/"},{"title":"Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning | Proceedings of the ACM on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3643739"},{"title":"EMNLP 2025 The 2025 Conference on Empirical Methods in Natural","url":"https://aclanthology.org/2025.emnlp-tutorials.pdf"}]

Based on the web search results, here's what I found about Sliceformer:

Sliceformer is a novel approach that reformulates static program slicing as a sequence-to-sequence task using small language models such as CodeT5+.

**Key Innovations:**

To improve dependency modeling, Sliceformer design dataflow-aware pretraining objectives that leverage data flow graphs (DFG) to teach models data dependencies through dataflow-preserving statement permutation and dataflow-aware span corruption. Second, to eliminate hallucination, it develops a constrained decoding mechanism that enforces both lexical and syntactic constraints.

**Performance:**

Sliceformer was evaluated on Java and Python program slicing benchmarks, demonstrating consistent improvements over state-of-the-art baselines with up to 22% gain in ExactMatch.

The research was posted to arXiv on April 9, 2026, indicating this is a recent work in the program slicing and neural models field. However, I did not find specific information about an ACL 2026 publication acceptance for this work in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d7fbacd-241e-44ca-9c2d-8989a2726596",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a8ce9e4db0ebbe7fc",
  "type": "user",
  "uuid": "65e3590b-e584-43e5-81a1-5db927cde027",
  "sourceToolAssistantUUID": "0d7fbacd-241e-44ca-9c2d-8989a2726596",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T18:40:41.273Z_

<details><summary>↩ Tool result · `toolu_01Cq7tq3exMt3MrcThuabaPo`</summary>

```text
Web search results for query: "Sliceformer Static Program Slicing Language Models Dataflow-Aware Pretraining arXiv 2604.26961"

Links: [{"title":"Static Program Slicing Using Language Models With Dataflow-Aware Pretraining and Constrained Decoding","url":"https://arxiv.org/html/2604.26961"},{"title":"[2604.26961] Static Program Slicing Using Language Models With Dataflow-Aware Pretraining and Constrained Decoding","url":"https://arxiv.org/abs/2604.26961"},{"title":"Programming Languages","url":"https://arxiv.org/list/cs.PL/new"},{"title":"SliceT5: Static Program Slicing using Language Models with Copy Mechanism and Constrained Decoding","url":"https://arxiv.org/html/2509.17338v1"},{"title":"SLICET5: Static Program Slicing using Language Models with","url":"https://arxiv.org/pdf/2509.17338"},{"title":"SliceMate: Accurate and Scalable Static Program Slicing via LLM-Powered Agents","url":"https://arxiv.org/html/2507.18957v1"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"[2509.17338] SLICET5: Static Program Slicing using Language Models with Copy Mechanism and Constrained Decoding","url":"https://arxiv.org/abs/2509.17338"},{"title":"Program Slicing in the Era of Large Language Models","url":"https://arxiv.org/html/2409.12369v1"},{"title":"Predictive Program Slicing via Execution Knowledge-Guided","url":"https://aashishyadavally.github.io/assets/pdf/pub-fse2024.pdf"}]

I found the arXiv paper you're looking for. Here's the information about Sliceformer:

## Paper Overview

Sliceformer presents "Static Program Slicing Using Language Models With Dataflow-Aware Pretraining and Constrained Decoding", with arXiv ID 2604.26961.

## Key Innovation

Sliceformer reformulates static program slicing as a sequence-to-sequence task using small language models such as CodeT5+.

## Two Main Contributions

Sliceformer enhances standard supervised fine-tuning (SFT) with dataflow-aware pretraining and constrained decoding, where the former equips the model with dataflow semantic understanding before SFT, while the latter operates at inference time to prevent hallucinated tokens and invalid statement generation.

More specifically, it designs dataflow-aware pretraining objectives that leverage data flow graphs (DFG) to teach models data dependencies through dataflow-preserving statement permutation and dataflow-aware span corruption, and develops a constrained decoding mechanism that enforces both lexical and syntactic constraints.

## Performance Results

On Java programs, Sliceformer attains an ExactMatch score of 92.20%, significantly outperforming the strongest baseline NS-slicer (GraphBERT) at 85.77%. On Python programs, Sliceformer reaches 83.15% in ExactMatch compared to only 61.25% for NS-slicer, surpassing the best-performing baseline by 6.4% and 21.9% in ExactMatch on Java and Python, respectively.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "914271cc-71ff-4bdf-a4ea-86a0c7f146cf",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a8ce9e4db0ebbe7fc",
  "type": "user",
  "uuid": "401fa720-ba35-40ca-826d-3efd6b873e44",
  "sourceToolAssistantUUID": "914271cc-71ff-4bdf-a4ea-86a0c7f146cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-10T18:40:45.266Z_

Let me fetch the arXiv abstract page directly to get more details, including venue and author information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "401fa720-ba35-40ca-826d-3efd6b873e44",
  "isSidechain": true,
  "agentId": "a8ce9e4db0ebbe7fc",
  "requestId": "req_011CauNrvLWnw73fYwkizgN9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0badc1be-c8bc-41ad-8144-5b1cadf85a5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HFiswgnTE87BPum5K7PRE7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 855,
      "cache_creation_input_tokens": 1065,
      "cache_read_input_tokens": 10803,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1065,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-10T18:40:47.949Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012MhiCkWRNC9FjQKLGig2Hw`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.26961",
  "prompt": "Extract: 1) The full title, 2) All authors, 3) The abstract, 4) Any mention of conference venue (ACL 2026 or otherwise), 5) Submission/publication dates, 6) Any key numerical results mentioned (ExactMatch scores, percentage gains), 7) Whether it mentions \"Sliceformer\" as the system name."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0badc1be-c8bc-41ad-8144-5b1cadf85a5d",
  "isSidechain": true,
  "agentId": "a8ce9e4db0ebbe7fc",
  "requestId": "req_011CauNrvLWnw73fYwkizgN9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ac470ae-8f37-4588-bd21-198022e3a0f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HFiswgnTE87BPum5K7PRE7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 855,
      "cache_creation_input_tokens": 1065,
      "cache_read_input_tokens": 10803,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1065
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 855,
          "output_tokens": 186,
          "cache_read_input_tokens": 10803,
          "cache_creation_input_tokens": 1065,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1065,
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

_source line 13 · 2026-05-10T18:40:51.793Z_

<details><summary>↩ Tool result · `toolu_012MhiCkWRNC9FjQKLGig2Hw`</summary>

```text
# Paper Extraction Summary

**1) Full Title:**
"Static Program Slicing Using Language Models With Dataflow-Aware Pretraining and Constrained Decoding"

**2) All Authors:**
- Pengfei He
- Shaowei Wang
- Tse-Hsun (Peter) Chen
- Muhammad Asaduzzaman

**3) Abstract:**
The work addresses limitations in learning-based program slicing by proposing an approach that reformulates the task using sequence-to-sequence models. It incorporates dataflow-aware pretraining objectives leveraging data flow graphs and implements constrained decoding to prevent hallucinated outputs. The method was evaluated on both Java and Python benchmarks.

**4) Conference Venue:**
"Accepted at ACL 2026"

**5) Submission/Publication Dates:**
Submitted April 9, 2026 (version 1)

**6) Key Numerical Results:**
The paper reports "up to 22% gain in ExactMatch" compared to state-of-the-art baselines.

**7) System Name:**
Yes, the approach is called "Sliceformer" and uses CodeT5+ as the underlying language model.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ac470ae-8f37-4588-bd21-198022e3a0f2",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a8ce9e4db0ebbe7fc",
  "type": "user",
  "uuid": "3bb1cac1-9f4f-4042-89ad-3a49083191fd",
  "sourceToolAssistantUUID": "8ac470ae-8f37-4588-bd21-198022e3a0f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-10T18:40:54.180Z_

Now let me fetch the full HTML version to get more detailed results and confirm all the specifics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3bb1cac1-9f4f-4042-89ad-3a49083191fd",
  "isSidechain": true,
  "agentId": "a8ce9e4db0ebbe7fc",
  "requestId": "req_011CauNshGjMgsY1v7jjWGp9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97277871-937d-475d-8823-1f925612e876",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vr2unFY3Jtbm8rotKF2sEB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1326,
      "cache_read_input_tokens": 11868,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1326,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-10T18:40:58.272Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011k16XPf4ix8E9C4BtUMEzm`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.26961",
  "prompt": "Extract the following details: 1) Exact ExactMatch scores for Java and Python (e.g., 92.20% for Java, 83.15% for Python), 2) Baseline comparison numbers (e.g., NS-slicer/GraphBERT scores), 3) The exact percentage gains reported (6.4% Java, 21.9% Python, or 22%), 4) Whether dataflow knowledge transfer to neural models is validated, 5) The two pretraining objectives (dataflow-preserving statement permutation and dataflow-aware span corruption), 6) Any mention of ACL 2026 acceptance, 7) The conclusion or key takeaway about data-flow knowledge transfer."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97277871-937d-475d-8823-1f925612e876",
  "isSidechain": true,
  "agentId": "a8ce9e4db0ebbe7fc",
  "requestId": "req_011CauNshGjMgsY1v7jjWGp9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75238eea-d9f6-4032-be37-b8189d22b296",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vr2unFY3Jtbm8rotKF2sEB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1326,
      "cache_read_input_tokens": 11868,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1326
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 261,
          "cache_read_input_tokens": 11868,
          "cache_creation_input_tokens": 1326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1326,
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

_source line 16 · 2026-05-10T18:41:03.418Z_

<details><summary>↩ Tool result · `toolu_011k16XPf4ix8E9C4BtUMEzm`</summary>

```text
# Sliceformer: Static Program Slicing Analysis

## Key Performance Metrics

**ExactMatch Scores:**
- Java: 92.20%
- Python: 83.15%

**Baseline Comparison (NS-slicer/GraphBERT):**
- Java: 85.77%
- Python: 61.25%

**Reported Improvements:**
The paper states gains of "6.4% and 21.9%, respectively" on Java and Python compared to the strongest baseline.

## Core Technical Contributions

**Two Pretraining Objectives:**
1. Dataflow-preserving statement permutation - trains models to identify statement dependencies by generating valid code reorderings that maintain dataflow constraints
2. Dataflow-aware span corruption - applies dataflow-guided masking to force reconstruction based on dependency relationships

## Validation of Dataflow Knowledge Transfer

Yes, the approach validates dataflow knowledge transfer to neural models through:
- Extensive ablation analysis (Figure 4) showing each component's contribution
- Span corruption identified as "most impactful" for learning data dependencies
- Comparative results demonstrating superiority over models lacking dataflow pretraining

## Publication Status

The paper is archived on arXiv (2604.26961v1, dated April 9, 2026). There is **no mention of ACL 2026 acceptance** in the provided content.

## Key Takeaway

The research demonstrates that "dataflow-aware pre-training objectives and constrained decoding" are essential for enabling language models to accurately capture data dependencies necessary for precise program slicing, enabling models to generate fully correct code extractions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75238eea-d9f6-4032-be37-b8189d22b296",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a8ce9e4db0ebbe7fc",
  "type": "user",
  "uuid": "94659d8a-347a-4953-a3e3-1f7cc5990d9d",
  "sourceToolAssistantUUID": "75238eea-d9f6-4032-be37-b8189d22b296",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-10T18:41:18.715Z_

Here are my findings on each of your questions:

**1. Does this paper actually exist?**

Yes. The paper is real and available on arXiv at ID **2604.26961**, submitted April 9, 2026. The full title is "Static Program Slicing Using Language Models With Dataflow-Aware Pretraining and Constrained Decoding." The authors are Pengfei He, Shaowei Wang, Tse-Hsun (Peter) Chen, and Muhammad Asaduzzaman. The system is indeed called "Sliceformer" and uses CodeT5+ as its backbone.

**2. Is it accepted at ACL 2026?**

The arXiv abstract page metadata indicates "Accepted at ACL 2026." However, the full HTML body of the paper itself does not explicitly repeat this claim in the text. The acceptance note appears on the abstract/metadata page, which is a standard place for authors to note venue acceptance on arXiv. So the evidence points to **yes, it is marked as accepted at ACL 2026** on arXiv.

**3. Does it validate data-flow knowledge transfer to neural models?**

Yes. The paper's central thesis is that dataflow-aware pretraining can transfer data-flow knowledge into neural sequence-to-sequence models. It validates this through:
- Two novel pretraining objectives that leverage Data Flow Graphs (DFGs): (a) **dataflow-preserving statement permutation** and (b) **dataflow-aware span corruption**.
- Ablation studies showing each component's contribution, with span corruption identified as the most impactful for learning data dependencies.
- Comparative results demonstrating clear superiority over models that lack dataflow pretraining.

**4. What are the key results?**

- **Java ExactMatch**: 92.20% (Sliceformer) vs. 85.77% (NS-slicer/GraphBERT baseline) -- a **6.4% gain**.
- **Python ExactMatch**: 83.15% (Sliceformer) vs. 61.25% (NS-slicer baseline) -- a **21.9% gain**.
- The "up to 22% ExactMatch gains" claim in the abstract rounds the 21.9% Python improvement. This is accurate.

In summary: the paper exists, it is marked as accepted at ACL 2026 on its arXiv page, it does validate data-flow knowledge transfer to neural models via novel pretraining objectives, and the headline result of ~22% ExactMatch gain (specifically 21.9% on Python) is substantiated by the reported numbers.

Sources:
- [arXiv Abstract: 2604.26961](https://arxiv.org/abs/2604.26961)
- [arXiv HTML: Full Paper](https://arxiv.org/html/2604.26961)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94659d8a-347a-4953-a3e3-1f7cc5990d9d",
  "isSidechain": true,
  "agentId": "a8ce9e4db0ebbe7fc",
  "requestId": "req_011CauNtYxhAfdkD77Ggyocv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7aa23bab-ff47-4bdd-8c07-b9ac12017beb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WRRYWCYBEhS5ZTZyrLgyVu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 641,
      "cache_read_input_tokens": 13194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 641,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---
