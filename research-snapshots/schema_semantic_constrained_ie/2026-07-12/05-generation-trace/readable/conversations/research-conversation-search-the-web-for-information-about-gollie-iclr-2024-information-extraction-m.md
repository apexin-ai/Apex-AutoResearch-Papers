# Research conversation: Search the web for information about GoLLIE (ICLR 2024) information extraction model. I need: 1. Model architecture - wh

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a72094e6b0cb3482f.jsonl`
- **Structured JSON:** [`9d41a2169fb244801be8.json`](../../sessions/9d/9d41a2169fb244801be8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

35 recorded events

### User

_source line 1 · 2026-05-15T14:08:03.710Z_

Search the web for information about GoLLIE (ICLR 2024) information extraction model. I need:

1. Model architecture - what base model is it built on? (Code-Llama?)
2. Output format - does it output JSON? What structure?
3. SciERC performance - what F1 scores does it achieve on relation extraction?
4. GitHub repo URL and model weights availability (HuggingFace?)
5. How does it handle entity types and relation types - does it use Python class definitions?
6. Model sizes available

Search queries to try:
- "GoLLIE ICLR 2024 information extraction"
- "GoLLIE github code llama structured extraction"
- "GoLLIE SciERC relation extraction results"

Report all findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0b1e6eb4-459b-4f0f-bf9c-f0f393f18537",
  "agentId": "a72094e6b0cb3482f",
  "type": "user",
  "uuid": "18e6e0be-c2aa-4b2e-b563-a5c268492343",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T14:08:03.714Z_

```json
{
  "parentUuid": "18e6e0be-c2aa-4b2e-b563-a5c268492343",
  "isSidechain": true,
  "agentId": "a72094e6b0cb3482f",
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
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "3ed7b810-6a47-4aa3-8fb3-869da5982ef6",
  "timestamp": "2026-05-15T14:08:03.714Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T14:08:06.332Z_



I'll search the web for GoLLIE information using multiple queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ed7b810-6a47-4aa3-8fb3-869da5982ef6",
  "isSidechain": true,
  "agentId": "a72094e6b0cb3482f",
  "requestId": "req_011Cb4V7iGsvYA1iqx33gj99",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb4a662a-b664-4858-b029-25d6a991deec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KeizvVinyyCCd2CkpH6DwS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13300,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13300,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 4 · 2026-05-15T14:08:06.682Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01ExBbN9ReqGZhGy3tC7zCUx`</summary>

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
  "parentUuid": "cb4a662a-b664-4858-b029-25d6a991deec",
  "isSidechain": true,
  "agentId": "a72094e6b0cb3482f",
  "requestId": "req_011Cb4V7iGsvYA1iqx33gj99",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38451f51-1e18-4fc5-93b8-a83e0751112c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KeizvVinyyCCd2CkpH6DwS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13300,
      "cache_read_input_tokens": 0,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13300
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 95,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 13300,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13300,
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

_source line 5 · 2026-05-15T14:08:06.686Z_

<details><summary>↩ Tool result · `toolu_01ExBbN9ReqGZhGy3tC7zCUx`</summary>

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
  "parentUuid": "38451f51-1e18-4fc5-93b8-a83e0751112c",
  "isSidechain": true,
  "promptId": "0b1e6eb4-459b-4f0f-bf9c-f0f393f18537",
  "agentId": "a72094e6b0cb3482f",
  "type": "user",
  "uuid": "54b0c428-07f1-43aa-8947-bf08e3d46f4d",
  "sourceToolAssistantUUID": "38451f51-1e18-4fc5-93b8-a83e0751112c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T14:08:11.002Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QB3Pm8HcknVQedjn5E1ujK`</summary>

```json
{
  "query": "GoLLIE ICLR 2024 information extraction Code-Llama architecture"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54b0c428-07f1-43aa-8947-bf08e3d46f4d",
  "isSidechain": true,
  "agentId": "a72094e6b0cb3482f",
  "requestId": "req_011Cb4V7wFjXCNwzWeJRBusQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd07a28a-e289-4242-b3d7-3d0c7810f623",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhjMg4YNGanwRjahn2MviT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1459,
      "cache_read_input_tokens": 13300,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1459,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 7 · 2026-05-15T14:08:11.448Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LHBDSCkSy8CJqzJv9Ghkj7`</summary>

```json
{
  "query": "GoLLIE github repo HuggingFace model weights"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd07a28a-e289-4242-b3d7-3d0c7810f623",
  "isSidechain": true,
  "agentId": "a72094e6b0cb3482f",
  "requestId": "req_011Cb4V7wFjXCNwzWeJRBusQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c336925-1f9a-4964-9620-62615740038b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhjMg4YNGanwRjahn2MviT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1459,
      "cache_read_input_tokens": 13300,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1459
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 171,
          "cache_read_input_tokens": 13300,
          "cache_creation_input_tokens": 1459,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1459,
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

### Tool call

_source line 8 · 2026-05-15T14:08:11.456Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015c926WeaaVtxaEQuD7sMzc`</summary>

```json
{
  "query": "GoLLIE SciERC relation extraction F1 results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c336925-1f9a-4964-9620-62615740038b",
  "isSidechain": true,
  "agentId": "a72094e6b0cb3482f",
  "requestId": "req_011Cb4V7wFjXCNwzWeJRBusQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "768150bc-ff56-4844-a928-4a2a147e0de5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhjMg4YNGanwRjahn2MviT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1459,
      "cache_read_input_tokens": 13300,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1459
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 171,
          "cache_read_input_tokens": 13300,
          "cache_creation_input_tokens": 1459,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1459,
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

_source line 9 · 2026-05-15T14:08:16.670Z_

<details><summary>↩ Tool result · `toolu_015c926WeaaVtxaEQuD7sMzc`</summary>

```text
Web search results for query: "GoLLIE SciERC relation extraction F1 results"

Links: [{"title":"GoLLIE/notebooks/Relation Extraction.ipynb at main · hitz-zentroa/GoLLIE","url":"https://github.com/hitz-zentroa/GoLLIE/blob/main/notebooks/Relation%20Extraction.ipynb"},{"title":"GitHub - TigranGalstyan/SciERC: A fork of https://bitbucket.org/luanyi/scierc/src","url":"https://github.com/TigranGalstyan/SciERC"},{"title":"SciERC/README.md at master · YerevaNN/SciERC","url":"https://github.com/YerevaNN/SciERC/blob/master/README.md"},{"title":"A Few-Shot Approach for Relation Extraction Domain Adaptation using Large Language Models","url":"https://arxiv.org/html/2408.02377v1"},{"title":"Full article: An entity and relation extraction model based on context query and axial attention towards patent texts","url":"https://www.tandfonline.com/doi/full/10.1080/09540091.2024.2426816"},{"title":"Performance on SciERC dataset. (The highest F1 is shown in bold.) | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Performance-on-SciERC-dataset-The-highest-F1-is-shown-in-bold_tbl2_361413093"},{"title":"A Scientific Information Extraction Dataset for Nature ...","url":"https://aclanthology.org/2020.lrec-1.255.pdf"},{"title":"GitHub - YerevaNN/SciERC: A fork of https://bitbucket.org/luanyi/scierc/src","url":"https://github.com/YerevaNN/SciERC"},{"title":"SciREX: A Challenge Dataset for Document-Level ...","url":"https://aclanthology.org/2020.acl-main.670.pdf"},{"title":"GoLLIE : Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/html/2310.03668v5"}]

Based on the web search results, I found information about GoLLIE (Guideline-following Large Language Model for Information Extraction) and its performance on information extraction tasks. However, the specific F1 results for GoLLIE on SciERC relation extraction are not directly detailed in these search results.

What I can tell you from the search results is:

GoLLIE's results on supervised datasets show that comparing GoLLIE with the baseline, they both obtain very similar results, with an absolute difference of 0.3 F1 points on average. Additionally, compared to the baseline, the results are improved significantly when using guidelines on almost every dataset in zero-shot settings, with an absolute difference of 13 F1 points on average.

For context on SciERC relation extraction performance more generally, SpERT significantly outperforms other joint entity/relation extraction models on SciERC dataset, reaching up to 50.84% micro-average F1 on relation extraction.

For more specific GoLLIE results on SciERC relation extraction, you may want to check the GoLLIE paper directly or the model's official repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "768150bc-ff56-4844-a928-4a2a147e0de5",
  "isSidechain": true,
  "promptId": "0b1e6eb4-459b-4f0f-bf9c-f0f393f18537",
  "agentId": "a72094e6b0cb3482f",
  "type": "user",
  "uuid": "9be1ae9d-48ea-493a-8c04-c3c5d926dc26",
  "sourceToolAssistantUUID": "768150bc-ff56-4844-a928-4a2a147e0de5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T14:08:17.160Z_

<details><summary>↩ Tool result · `toolu_01LHBDSCkSy8CJqzJv9Ghkj7`</summary>

```text
Web search results for query: "GoLLIE github repo HuggingFace model weights"

Links: [{"title":"GitHub - hitz-zentroa/GoLLIE: Guideline following Large Language Model for Information Extraction · GitHub","url":"https://github.com/hitz-zentroa/GoLLIE"},{"title":"HiTZ/GoLLIE-13B · Hugging Face","url":"https://huggingface.co/HiTZ/GoLLIE-13B"},{"title":"HiTZ/GoLLIE-7B · Hugging Face","url":"https://huggingface.co/HiTZ/GoLLIE-7B"},{"title":"GitHub - bodaay/HuggingFaceModelDownloader: Simple go utility to download HuggingFace Models and Datasets · GitHub","url":"https://github.com/bodaay/HuggingFaceModelDownloader"},{"title":"GoLLIE - a HiTZ Collection","url":"https://huggingface.co/collections/HiTZ/gollie-651bf19ee315e8a224aacc4f"},{"title":"Update README.md · HiTZ/GoLLIE-34B at cb31bf3","url":"https://huggingface.co/HiTZ/GoLLIE-34B/commit/cb31bf3786f023a130cbf9179d1ea362ee72656b"},{"title":"Commits · HiTZ/GoLLIE-7B","url":"https://huggingface.co/HiTZ/GoLLIE-7B/commits/6a52e87565fd759ec2ddf14ed67593de0f57b5c6"},{"title":"GGUF · Hugging Face","url":"https://huggingface.co/docs/hub/gguf"},{"title":"GIT · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/git"},{"title":"Getting Started with Repositories · Hugging Face","url":"https://huggingface.co/docs/hub/en/repositories-getting-started"}]

Based on the search results, here's what I found about GoLLIE:

## GitHub Repository
GoLLIE is a guideline-following Large Language Model for Information Extraction with three models based on CODE-LLaMA (7B, 13B, and 34B) that are available on the HuggingFace Hub. The main GitHub repository is located at: **https://github.com/hitz-zentroa/GoLLIE**

## HuggingFace Model Weights
The GoLLIE models are available on HuggingFace under the HiTZ organization:

1. **HiTZ/GoLLIE-7B** - https://huggingface.co/HiTZ/GoLLIE-7B
2. **HiTZ/GoLLIE-13B** - https://huggingface.co/HiTZ/GoLLIE-13B
3. **HiTZ/GoLLIE-34B** - (34B variant)

There's also a HuggingFace collection at: https://huggingface.co/collections/HiTZ/gollie-651bf19ee315e8a224aacc4f

## Important Usage Notes
The models use flash attention and require the flag `trust_remote_code=True` to load properly, flash attention requires an available CUDA GPU, and running GoLLIE pre-trained models on a CPU is not supported.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c336925-1f9a-4964-9620-62615740038b",
  "isSidechain": true,
  "promptId": "0b1e6eb4-459b-4f0f-bf9c-f0f393f18537",
  "agentId": "a72094e6b0cb3482f",
  "type": "user",
  "uuid": "cc72931e-c2f8-46ab-9a4d-27c00b2fbed7",
  "sourceToolAssistantUUID": "9c336925-1f9a-4964-9620-62615740038b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T14:08:18.699Z_

<details><summary>↩ Tool result · `toolu_01QB3Pm8HcknVQedjn5E1ujK`</summary>

```text
Web search results for query: "GoLLIE ICLR 2024 information extraction Code-Llama architecture"

Links: [{"title":"ICLR Poster GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://iclr.cc/virtual/2024/poster/18435"},{"title":"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction | OpenReview","url":"https://openreview.net/forum?id=Y3wpuxd7u9"},{"title":"GitHub - hitz-zentroa/GoLLIE: Guideline following Large Language Model for Information Extraction · GitHub","url":"https://github.com/hitz-zentroa/GoLLIE"},{"title":"GitHub - azminewasi/Awesome-LLMs-ICLR-24: It is a comprehensive resource hub compiling all LLM papers accepted at the International Conference on Learning Representations (ICLR) in 2024. · GitHub","url":"https://github.com/azminewasi/Awesome-LLMs-ICLR-24"},{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf"},{"title":"GoLLIE | Guideline following Large Language Model for Information Extraction","url":"https://hitz-zentroa.github.io/GoLLIE/"},{"title":"[2310.03668] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/abs/2310.03668"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"Downloads 2024","url":"https://iclr.cc/Downloads/2024"},{"title":"gollie : annotation guidelines improve zero-shot ...","url":"https://arxiv.org/pdf/2310.03668"}]

Based on the search results, here's comprehensive information about GoLLIE from ICLR 2024:

## Overview

GoLLIE (Guideline-following Large Language Model for IE) is a model able to improve zero-shot results on unseen IE tasks by virtue of being fine-tuned to comply with annotation guidelines.

## Key Problem Addressed

While Large Language Models (LLMs) combined with instruction tuning have made significant progress when generalizing to unseen tasks, they have been less successful in Information Extraction (IE), lagging behind task-specific models. Typically, IE tasks are characterized by complex annotation guidelines which describe the task and give examples to humans. Previous attempts to leverage such information have failed, even with the largest models, as they are not able to follow the guidelines out-of-the-box.

## Architecture and Models

Three GoLLIE models based on CODE-LLama (7B, 13B, and 34B) were released. This builds upon the Code-Llama architecture to create a specialized model for information extraction tasks.

## Performance and Capabilities

GoLLIE is able to generalize to and follow unseen guidelines, outperforming previous attempts at zero-shot information extraction. Additionally, GoLLIE outperforms previous approaches on zero-shot Information Extraction and allows the user to perform inferences with annotation schemas defined on the fly.

## Key Insight

Detailed guidelines are key for good results. The model leverages annotation guidelines as a primary mechanism for improving information extraction performance.

The paper was presented at ICLR 2024 by researchers from HiTZ Basque Center for Language Technology and is publicly available with code and models released on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd07a28a-e289-4242-b3d7-3d0c7810f623",
  "isSidechain": true,
  "promptId": "0b1e6eb4-459b-4f0f-bf9c-f0f393f18537",
  "agentId": "a72094e6b0cb3482f",
  "type": "user",
  "uuid": "a9d154f0-1bfa-48b9-99e1-4e74db6fbfb2",
  "sourceToolAssistantUUID": "fd07a28a-e289-4242-b3d7-3d0c7810f623",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-15T14:08:21.588Z_

Let me get more specific details on the output format and SciERC numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9d154f0-1bfa-48b9-99e1-4e74db6fbfb2",
  "isSidechain": true,
  "agentId": "a72094e6b0cb3482f",
  "requestId": "req_011Cb4V8pLHT3wrLaYeF5RBe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "869fed3e-5bde-46b9-a56e-fb6bc94dcbb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GjUU3NkaeaTYrwSxhh1Rn4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1796,
      "cache_creation_input_tokens": 1153,
      "cache_read_input_tokens": 14759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1153,
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

_source line 13 · 2026-05-15T14:08:22.070Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017EdQsPvw7fhCyarebSpxKr`</summary>

```json
{
  "query": "GoLLIE output format Python class definitions annotation guidelines schema"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "869fed3e-5bde-46b9-a56e-fb6bc94dcbb9",
  "isSidechain": true,
  "agentId": "a72094e6b0cb3482f",
  "requestId": "req_011Cb4V8pLHT3wrLaYeF5RBe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "603c01c3-864a-4f0b-b154-654059fba6cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GjUU3NkaeaTYrwSxhh1Rn4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1796,
      "cache_creation_input_tokens": 1153,
      "cache_read_input_tokens": 14759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1153,
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

_source line 14 · 2026-05-15T14:08:22.648Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0156uHDFrUEWKgt3NBT5YVtb`</summary>

```json
{
  "query": "GoLLIE paper results table zero-shot SciERC CrossNER ACE performance F1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "603c01c3-864a-4f0b-b154-654059fba6cf",
  "isSidechain": true,
  "agentId": "a72094e6b0cb3482f",
  "requestId": "req_011Cb4V8pLHT3wrLaYeF5RBe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0f437e9-a3a1-45c6-b1c1-d5d1106ce903",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GjUU3NkaeaTYrwSxhh1Rn4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1796,
      "cache_creation_input_tokens": 1153,
      "cache_read_input_tokens": 14759,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1153
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1796,
          "output_tokens": 139,
          "cache_read_input_tokens": 14759,
          "cache_creation_input_tokens": 1153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1153,
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

_source line 15 · 2026-05-15T14:08:28.120Z_

<details><summary>↩ Tool result · `toolu_0156uHDFrUEWKgt3NBT5YVtb`</summary>

```text
Web search results for query: "GoLLIE paper results table zero-shot SciERC CrossNER ACE performance F1"

Links: [{"title":"Integrated Recall and Retrieval Augmentation","url":"https://aclanthology.org/2025.naacl-long.540.pdf"},{"title":"GoLLIE : Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/html/2310.03668v5"},{"title":"Show Less, Instruct More: Enriching Prompts with Definitions and Guidelines for Zero-Shot NER","url":"https://arxiv.org/html/2407.01272v3"},{"title":"gollie : annotation guidelines improve zero-shot ...","url":"https://arxiv.org/pdf/2310.03668"},{"title":"[2310.03668] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/abs/2310.03668"},{"title":"GOLLIE : ANNOTATION GUIDELINES IMPROVE ZERO- ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf"},{"title":"KnowCoder","url":"https://ict-goknow.github.io/knowcoder/"},{"title":"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction | OpenReview","url":"https://openreview.net/forum?id=Y3wpuxd7u9"},{"title":"[PDF] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/3f40edfcafc018b2cb54612a9aaa9d6b43a11a26"},{"title":"DiZiNER: Disagreement-guided Instruction Refinement via Pilot Annotation Simulation for Zero-shot Named Entity Recognition","url":"https://arxiv.org/html/2604.15866"}]

Based on the search results, I found information about the GoLLIE paper. The search results reference the GoLLIE paper and mention it includes results on zero-shot information extraction tasks including CrossNER and other datasets. However, the specific results table with exact F1 scores for SciERC, CrossNER, and ACE is not fully displayed in these search results.

GoLLIE (Guideline-following Large Language Model for IE) is an LLM fine-tuned to learn how to attend to the guidelines on a small set of well known IE tasks. Comprehensive zero-shot evaluation empirically demonstrates that GoLLIE outperforms the state-of-the-art in zero-shot information extraction.

The search results mention that the original GoLLIE paper (arXiv:2310.03668) contains results tables, but the specific numerical F1 scores from the results table for SciERC, CrossNER, and ACE are not visible in the search excerpts. To access the actual results table with the specific F1 performance metrics you're looking for, you would need to view the full PDF of the paper directly from the arxiv or proceedings links in the search results (such as https://arxiv.org/html/2310.03668v5 or the ICLR proceedings version).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0f437e9-a3a1-45c6-b1c1-d5d1106ce903",
  "isSidechain": true,
  "promptId": "0b1e6eb4-459b-4f0f-bf9c-f0f393f18537",
  "agentId": "a72094e6b0cb3482f",
  "type": "user",
  "uuid": "702b0be8-413b-49d9-a6b9-b799af8ca7bc",
  "sourceToolAssistantUUID": "a0f437e9-a3a1-45c6-b1c1-d5d1106ce903",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T14:08:30.690Z_

<details><summary>↩ Tool result · `toolu_017EdQsPvw7fhCyarebSpxKr`</summary>

```text
Web search results for query: "GoLLIE output format Python class definitions annotation guidelines schema"

Links: [{"title":"GoLLIE | Guideline following Large Language Model for Information Extraction","url":"https://hitz-zentroa.github.io/GoLLIE/"},{"title":"GoLLIE : Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/html/2310.03668v3"},{"title":"HiTZ/GoLLIE-13B · Hugging Face","url":"https://huggingface.co/HiTZ/GoLLIE-13B"},{"title":"GOLLIE : ANNOTATION GUIDELINES IMPROVE ZERO- ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf"},{"title":"GitHub - hitz-zentroa/GoLLIE: Guideline following Large Language Model for Information Extraction · GitHub","url":"https://github.com/hitz-zentroa/GoLLIE"},{"title":"HiTZ/GoLLIE-7B · Hugging Face","url":"https://huggingface.co/HiTZ/GoLLIE-7B"},{"title":"GoLLIE 7B · Models · Dataloop","url":"https://dataloop.ai/library/model/hitz_gollie-7b/"},{"title":"Glossary — Python 3.14.5 documentation","url":"https://docs.python.org/3/glossary.html"},{"title":"Type annotations — typing documentation","url":"https://typing.python.org/en/latest/spec/annotations.html"},{"title":"Google Python Style Guide","url":"https://google.github.io/styleguide/pyguide.html"}]

Based on the search results, here's comprehensive information about GoLLIE's output format, Python class definitions, annotation guidelines, and schema:

## Output Format

GoLLIE's format has three main parts: schema definition, input text and output annotations. The annotations are represented as a list of instances of the classes defined on the schema definition part, and parsing the output is straightforward; executing the generated code in Python yields a list containing the result.

## Python Class Definitions

The labels are represented as Python classes, and the guidelines or instructions are introduced as docstrings. Classes are flexible and vary for each task. For example, classes for a NER dataset merely require an attribute to specify the text span that correspond to the class. On the other side, more complex tasks such as Event Argument Extraction (EAE) or Slot Filling (SF) demand more class attributes to categorize the task, such as a list of participants in an event.

## Annotation Guidelines Schema

Schema definition forms the initial segment of the input. This section contains the information about the labels which are represented as Python classes; guidelines, articulated as docstrings; and representative annotation candidates presented in the form of code comments. The model's output satisfies the type constraints defined in the guidelines, for instance, attributes can be defined as strings, except for certain fields which are lists. Other constraints can also be applied, such as Optional attributes or more detailed types like Name, Value or String types.

## Code Generation and Execution

The generated output can be directly evaluated as it is Python working code. This allows the user to directly parse and interpret the output. The inputs can be automatically standardized using Python code formatters such as Black.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "603c01c3-864a-4f0b-b154-654059fba6cf",
  "isSidechain": true,
  "promptId": "0b1e6eb4-459b-4f0f-bf9c-f0f393f18537",
  "agentId": "a72094e6b0cb3482f",
  "type": "user",
  "uuid": "9b998013-3919-4dd5-97d2-140a8767401b",
  "sourceToolAssistantUUID": "603c01c3-864a-4f0b-b154-654059fba6cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T14:08:33.439Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Npz5adEzNcdsQE7JxMFyw3`</summary>

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
  "parentUuid": "9b998013-3919-4dd5-97d2-140a8767401b",
  "isSidechain": true,
  "agentId": "a72094e6b0cb3482f",
  "requestId": "req_011Cb4V9hczYxjusdfFbnVoS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c1e493cc-2434-4311-8ef7-6ca5ee4c4075",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012j8tBZXtekWWAhzCvsv3kA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 854,
      "cache_creation_input_tokens": 2805,
      "cache_read_input_tokens": 15912,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2805
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 854,
          "output_tokens": 76,
          "cache_read_input_tokens": 15912,
          "cache_creation_input_tokens": 2805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2805,
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

_source line 18 · 2026-05-15T14:08:33.442Z_

<details><summary>↩ Tool result · `toolu_01Npz5adEzNcdsQE7JxMFyw3`</summary>

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
  "parentUuid": "c1e493cc-2434-4311-8ef7-6ca5ee4c4075",
  "isSidechain": true,
  "promptId": "0b1e6eb4-459b-4f0f-bf9c-f0f393f18537",
  "agentId": "a72094e6b0cb3482f",
  "type": "user",
  "uuid": "1524f050-7b23-456a-9f1b-48dc373b508b",
  "sourceToolAssistantUUID": "c1e493cc-2434-4311-8ef7-6ca5ee4c4075",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T14:08:39.405Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012Mtx1sgXJ4bDFqw6sLqFi7`</summary>

```json
{
  "url": "https://arxiv.org/html/2310.03668v5",
  "prompt": "Extract the following specific information from the GoLLIE paper:\n1. Exact F1 scores on SciERC dataset (especially relation extraction)\n2. All results tables with numerical F1 scores for zero-shot and supervised settings\n3. The exact output format - does it output JSON or Python code? Show examples if available.\n4. How entity types and relation types are defined - Python class definitions with docstrings?\n5. What datasets were used for training vs zero-shot evaluation?\n6. Model sizes (7B, 13B, 34B) and their comparative performance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1524f050-7b23-456a-9f1b-48dc373b508b",
  "isSidechain": true,
  "agentId": "a72094e6b0cb3482f",
  "requestId": "req_011Cb4V9vHkGH7zr93XwHDUD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "acecb279-db77-4dd6-baac-35f9409ad0cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01584RYj6syjU32HG974jpXD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 18717,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 20 · 2026-05-15T14:08:41.377Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CTBvY49FPjvhZge33394NA`</summary>

```json
{
  "url": "https://github.com/hitz-zentroa/GoLLIE",
  "prompt": "Extract the following from the GoLLIE GitHub README:\n1. Model architecture details - base model (Code-Llama?)\n2. Available model sizes and HuggingFace links\n3. Output format examples - JSON or Python code?\n4. How schemas are defined (Python classes?)\n5. Example of how entity types and relation types are specified\n6. Installation and usage instructions\n7. Any mention of SciERC or relation extraction support"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acecb279-db77-4dd6-baac-35f9409ad0cb",
  "isSidechain": true,
  "agentId": "a72094e6b0cb3482f",
  "requestId": "req_011Cb4V9vHkGH7zr93XwHDUD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a3aa3ec-909a-4855-b388-4b19ea842543",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01584RYj6syjU32HG974jpXD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 18717,
      "output_tokens": 384,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1448
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 384,
          "cache_read_input_tokens": 18717,
          "cache_creation_input_tokens": 1448,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1448,
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

_source line 21 · 2026-05-15T14:08:46.541Z_

<details><summary>↩ Tool result · `toolu_012Mtx1sgXJ4bDFqw6sLqFi7`</summary>

```text
# GoLLIE Paper: Key Information Extract

## 1. SciERC Dataset Results
The provided content does **not include SciERC results**. The paper evaluates on different datasets (ACE05, CoNLL03, CrossNER domains, etc.) but SciERC is not mentioned.

## 2. Results Tables Summary

**Zero-Shot Evaluation (Table 3 - Selected):**
- MultiNERD: 76.0 F1 (7B model)
- Movie: 63.0 F1
- Restaurants: 43.4 F1
- Average across all datasets: 55.3 F1

**Supervised Evaluation (Table 2 - Selected):**
- CoNLL 2003: 92.8 F1
- ACE05 NER: 88.1 F1
- Average: 73.0 F1

## 3. Output Format
The system outputs **Python code**, not JSON. The model generates executable Python with "result =" followed by class instantiations that can be parsed directly by executing the code.

## 4. Entity/Relation Type Definition
Entity types are defined as "Python classes" with docstrings containing guidelines and comments with representative candidates. For complex tasks like Event Argument Extraction, classes include multiple attributes beyond just text spans.

## 5. Training vs. Evaluation Datasets

**Training:** Primarily News and Biomedical domains (ACE05, CoNLL03, BC5CDR, RAMS, etc.)

**Zero-Shot Evaluation:** Diverse domains—CrossNER (AI, Literature, Music, Politics, Science), Movie, Restaurants, MultiNERD, WikiEvents, CASIE

## 6. Model Scaling Results
- **7B:** 55.3 F1 (zero-shot average)
- **13B:** 56.0 F1
- **34B:** 57.2 F1

Larger models show consistent improvements, though some datasets don't benefit substantially.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acecb279-db77-4dd6-baac-35f9409ad0cb",
  "isSidechain": true,
  "promptId": "0b1e6eb4-459b-4f0f-bf9c-f0f393f18537",
  "agentId": "a72094e6b0cb3482f",
  "type": "user",
  "uuid": "c8d27873-d04d-440d-9417-d31cd6783dc9",
  "sourceToolAssistantUUID": "acecb279-db77-4dd6-baac-35f9409ad0cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T14:08:47.756Z_

<details><summary>↩ Tool result · `toolu_01CTBvY49FPjvhZge33394NA`</summary>

```text
# GoLLIE GitHub Repository Extract

## 1. Base Model Architecture
GoLLIE is built on **CODE-LLaMA**, as indicated in the model configuration files and documentation.

## 2. Available Model Sizes & HuggingFace Links

| Model | Supervised F1 | Zero-shot F1 | Link |
|-------|---------------|--------------|------|
| GoLLIE-7B | 73.0 | 55.3 | HiTZ/GoLLIE-7B |
| GoLLIE-13B | 73.9 | 56.0 | HiTZ/GoLLIE-13B |
| GoLLIE-34B | 75.0 | 57.2 | HiTZ/GoLLIE-34B |

## 3. Output Format
"The labels are represented as Python classes, and the guidelines or instructions are introduced as docstrings. The model start generating after the `result = [` line." This indicates structured Python code generation rather than JSON.

## 4. Schema Definition
Schemas are defined as Python classes with docstrings containing annotation guidelines.

## 5. Entity/Relation Type Specification
The repository demonstrates specification through class-based definitions, though specific examples of entity and relation type syntax are not detailed in the provided excerpt.

## 6. Installation Requirements
Dependencies include: PyTorch ≥2.0.0, transformers ≥4.33.1, PEFT ≥0.4.0, bitsandbytes ≥0.40.0, and Flash Attention 2.0, plus utilities like numpy, Jinja2, and datasets.

## 7. SciERC/Relation Extraction
No specific mention of SciERC support appears in the provided content, though the supported tasks section references relation extraction generally.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a3aa3ec-909a-4855-b388-4b19ea842543",
  "isSidechain": true,
  "promptId": "0b1e6eb4-459b-4f0f-bf9c-f0f393f18537",
  "agentId": "a72094e6b0cb3482f",
  "type": "user",
  "uuid": "0dbdb74e-4c0a-4a60-9e4c-68d97ac18ed9",
  "sourceToolAssistantUUID": "4a3aa3ec-909a-4855-b388-4b19ea842543",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T14:08:52.594Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01L89m6xJxEoeMi7YSYVkQXH`</summary>

```json
{
  "url": "https://github.com/hitz-zentroa/GoLLIE/blob/main/notebooks/Relation%20Extraction.ipynb",
  "prompt": "Extract: 1. How are relation types defined in GoLLIE? Show the Python class definitions for relations. 2. What is the exact output format for relation extraction? 3. Is SciERC mentioned? 4. Show examples of entity and relation class definitions with docstrings. 5. How does the model output look - show the result format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dbdb74e-4c0a-4a60-9e4c-68d97ac18ed9",
  "isSidechain": true,
  "agentId": "a72094e6b0cb3482f",
  "requestId": "req_011Cb4VAxXxVQyPYraomxrcp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "762d5f19-6c69-4103-9747-7afb864bd368",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019riQvSSVZeLxXKEEzUTz54",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1346,
      "cache_read_input_tokens": 20165,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1346,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 57,
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

_source line 24 · 2026-05-15T14:08:53.036Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F3a9j5Bwd7FKNFx9K6p69J`</summary>

```json
{
  "query": "GoLLIE relation extraction Python class example \"result =\" entity relation schema definition code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "762d5f19-6c69-4103-9747-7afb864bd368",
  "isSidechain": true,
  "agentId": "a72094e6b0cb3482f",
  "requestId": "req_011Cb4VAxXxVQyPYraomxrcp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "321c72c8-13a9-4628-a841-dd196776db4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019riQvSSVZeLxXKEEzUTz54",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1346,
      "cache_read_input_tokens": 20165,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1346
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 20165,
          "cache_creation_input_tokens": 1346,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1346,
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

_source line 25 · 2026-05-15T14:08:56.569Z_

<details><summary>↩ Tool result · `toolu_01L89m6xJxEoeMi7YSYVkQXH`</summary>

```text
I appreciate your detailed questions about the GoLLIE relation extraction notebook. However, I cannot provide the specific information you're requesting because the webpage content provided only shows the GitHub interface navigation and metadata for the file — it doesn't include the actual notebook content itself.

To answer your questions about:
1. How relation types are defined as Python classes
2. Output format specifications
3. SciERC dataset mentions
4. Entity and relation class definitions with docstrings
5. Model result formats

I would need access to the actual notebook content, which isn't included in what was provided. The page shows only the file structure, header navigation, and repository metadata.

**To find this information, you could:**
- View the raw notebook file directly at the GitHub repository
- Clone the GoLLIE repository and open the notebook locally
- Check the project's documentation or README files
- Review any associated research papers or documentation linked in the repository

If you can share the actual notebook content, I'd be happy to extract the specific technical details you're seeking.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "762d5f19-6c69-4103-9747-7afb864bd368",
  "isSidechain": true,
  "promptId": "0b1e6eb4-459b-4f0f-bf9c-f0f393f18537",
  "agentId": "a72094e6b0cb3482f",
  "type": "user",
  "uuid": "81b5cbd5-9616-4505-91fa-5df3d2d3386b",
  "sourceToolAssistantUUID": "762d5f19-6c69-4103-9747-7afb864bd368",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T14:09:00.029Z_

<details><summary>↩ Tool result · `toolu_01F3a9j5Bwd7FKNFx9K6p69J`</summary>

````text
Web search results for query: "GoLLIE relation extraction Python class example "result =" entity relation schema definition code"

Links: [{"title":"GoLLIE/notebooks/Relation Extraction.ipynb at main · hitz-zentroa/GoLLIE","url":"https://github.com/hitz-zentroa/GoLLIE/blob/main/notebooks/Relation%20Extraction.ipynb"},{"title":"GoLLIE | Guideline following Large Language Model for Information Extraction","url":"https://hitz-zentroa.github.io/GoLLIE/"},{"title":"HiTZ/GoLLIE-13B · Hugging Face","url":"https://huggingface.co/HiTZ/GoLLIE-13B"},{"title":"GitHub - hitz-zentroa/GoLLIE: Guideline following Large Language Model for Information Extraction · GitHub","url":"https://github.com/hitz-zentroa/GoLLIE"},{"title":"HiTZ/GoLLIE-34B · Hugging Face","url":"https://huggingface.co/HiTZ/GoLLIE-34B"},{"title":"HiTZ/GoLLIE-7B · Hugging Face","url":"https://huggingface.co/HiTZ/GoLLIE-7B"},{"title":"GoLLIE : Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/html/2310.03668v3"},{"title":"Relationship Extraction in NLP - GeeksforGeeks","url":"https://www.geeksforgeeks.org/nlp/relationship-extraction-in-nlp/"},{"title":"Relation Extraction","url":"https://paperswithcode.com/task/relation-extraction"},{"title":"glirel · PyPI","url":"https://pypi.org/project/glirel/"}]

Based on the search results, I found relevant information about GoLLIE relation extraction with Python class examples:

## GoLLIE Relation Extraction with Python Classes

The labels are represented as Python classes, and the guidelines or instructions are introduced as docstrings. The model start generating after the result = [ line.

GoLLIE can perform basic relation extraction with two string arguments per Relation class, and can handle more complex relations with multiple arguments.

### Schema Definition Example

GoLLIE adopts a Python code-based representation for both the input and output of the model, which offers a clear and human-readable structure and enables the representation of any information extraction task under a unified format.

An example entity definition uses the `@dataclass` decorator with a `Template` base class:

```python
@dataclass
class Launcher(Template):
    """Refers to a vehicle designed primarily to transport payloads from the Earth's surface to space."""
```

The model's output (everything after result = [) satisfies the type constraints defined in the guidelines, with attributes defined as strings filled with strings and arguments defined as lists filled with lists.

For more detailed examples and to get started with GoLLIE, you can refer to example Jupyter Notebooks, particularly the Relation Extraction notebook available in the official GoLLIE GitHub repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "321c72c8-13a9-4628-a841-dd196776db4c",
  "isSidechain": true,
  "promptId": "0b1e6eb4-459b-4f0f-bf9c-f0f393f18537",
  "agentId": "a72094e6b0cb3482f",
  "type": "user",
  "uuid": "55fc1716-5b4e-4645-a290-fcfc4861ff93",
  "sourceToolAssistantUUID": "321c72c8-13a9-4628-a841-dd196776db4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T14:09:04.174Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Q81ygbcUeBygs6YSX1fm5E`</summary>

```json
{
  "url": "https://hitz-zentroa.github.io/GoLLIE/",
  "prompt": "Extract all details about: 1. Python class definitions for entities and relations - show full code examples 2. The exact output format (result = [...]) 3. How guidelines/docstrings are used 4. Any relation extraction examples 5. Training datasets list 6. Zero-shot evaluation datasets and F1 scores"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55fc1716-5b4e-4645-a290-fcfc4861ff93",
  "isSidechain": true,
  "agentId": "a72094e6b0cb3482f",
  "requestId": "req_011Cb4VBs1MPk6dTUa56Z24n",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87c6b5b3-7f9f-4427-b246-5a7f2d742548",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CDUiLxaTae7JXCdKmCwh37",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1310,
      "cache_read_input_tokens": 21511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1310,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 28 · 2026-05-15T14:09:04.600Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R7WEzcsffdp73aEwrvTbxm`</summary>

```json
{
  "query": "GoLLIE dataclass Template relation extraction \"@dataclass\" \"class\" docstring example input output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87c6b5b3-7f9f-4427-b246-5a7f2d742548",
  "isSidechain": true,
  "agentId": "a72094e6b0cb3482f",
  "requestId": "req_011Cb4VBs1MPk6dTUa56Z24n",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cdfe1345-0378-4e8a-9ec1-b5c83b66a9f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CDUiLxaTae7JXCdKmCwh37",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1310,
      "cache_read_input_tokens": 21511,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1310
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 212,
          "cache_read_input_tokens": 21511,
          "cache_creation_input_tokens": 1310,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1310,
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

_source line 29 · 2026-05-15T14:09:10.062Z_

<details><summary>↩ Tool result · `toolu_01Q81ygbcUeBygs6YSX1fm5E`</summary>

````text
# GoLLIE Information Extraction Overview

## 1. Python Class Definitions for Entities

The page provides a space missions example showing the approach:

**Entity Definition Pattern:**
```python
class Launcher:
    """Guidelines as docstring"""
    space_company: str  # attribute with guideline as comment
    crew: list  # typed attributes

class Mission:
    """Mission entity guidelines"""
```

The full code snippets are referenced as images rather than provided as text in this document.

## 2. Output Format

Results are generated as "Python working code" that can be directly evaluated. The example shows: `result = [extracted_entities]` format. As stated, the "generated output can be directly evaluated as it is Python working code."

## 3. Guidelines/Docstrings Usage

Guidelines are embedded as Python docstrings in class definitions. The model learns to follow "annotation guidelines" encoded this way. For attributes, guidelines appear as inline comments.

## 4. Relation Extraction Examples

The page focuses on entity extraction. While "Event Argument Extraction (EAE)" is mentioned, no specific relation extraction examples or code are provided in the content.

## 5. Training Datasets List

This information is not explicitly listed. The page references evaluation on existing datasets but doesn't detail training data.

## 6. Zero-Shot Evaluation Results

**Datasets mentioned:**
- MIT Movie
- MIT Restaurant  
- CrossNER

The page states GoLLIE "outperforms previous approaches on almost all the datasets" but specific F1 scores are not provided—readers are directed to the paper for detailed metrics.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87c6b5b3-7f9f-4427-b246-5a7f2d742548",
  "isSidechain": true,
  "promptId": "0b1e6eb4-459b-4f0f-bf9c-f0f393f18537",
  "agentId": "a72094e6b0cb3482f",
  "type": "user",
  "uuid": "f97e8141-737e-4070-ada0-53ed7584c524",
  "sourceToolAssistantUUID": "87c6b5b3-7f9f-4427-b246-5a7f2d742548",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T14:09:11.414Z_

<details><summary>↩ Tool result · `toolu_01R7WEzcsffdp73aEwrvTbxm`</summary>

```text
Web search results for query: "GoLLIE dataclass Template relation extraction "@dataclass" "class" docstring example input output"

Links: [{"title":"GoLLIE/notebooks/Relation Extraction.ipynb at main · hitz-zentroa/GoLLIE","url":"https://github.com/hitz-zentroa/GoLLIE/blob/main/notebooks/Relation%20Extraction.ipynb"},{"title":"GoLLIE | Guideline following Large Language Model for Information Extraction","url":"https://hitz-zentroa.github.io/GoLLIE/"},{"title":"HiTZ/GoLLIE-13B · Hugging Face","url":"https://huggingface.co/HiTZ/GoLLIE-13B"},{"title":"GoLLIE/notebooks/Create Custom Task.ipynb at main · hitz-zentroa/GoLLIE","url":"https://github.com/hitz-zentroa/GoLLIE/blob/main/notebooks/Create%20Custom%20Task.ipynb"},{"title":"GitHub - hitz-zentroa/GoLLIE: Guideline following Large Language Model for Information Extraction · GitHub","url":"https://github.com/hitz-zentroa/GoLLIE"},{"title":"HiTZ/GoLLIE-7B · Discussions","url":"https://huggingface.co/HiTZ/GoLLIE-7B/discussions"},{"title":"HiTZ/GoLLIE-7B · Hugging Face","url":"https://huggingface.co/HiTZ/GoLLIE-7B"},{"title":"GLiREL - Generalist Model for Zero-Shot Relation Extraction","url":"https://arxiv.org/html/2501.03172v1"},{"title":"GoLLIE 34B · Models · Dataloop","url":"https://dataloop.ai/library/model/hitz_gollie-34b/"},{"title":"GoLLIE : Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/html/2310.03668v3"}]

Based on the search results, I've found information about GoLLIE and how it uses dataclass templates with docstrings for relation extraction. Here's what I found:

## GoLLIE Dataclass Template for Relation Extraction

GoLLIE uses `@dataclass` decorated classes to define relations, with docstrings that describe the relation and attributes that define the arguments.

### Example Structure

The labels are represented as Python classes, and the guidelines or instructions are introduced as docstrings. Here's an example from the documentation:

A `PhysicalRelation` class is defined with `@dataclass` decorator, including a docstring that explains "The Physical Relation captures the physical location relation of entities" and has an `arg1: str` attribute.

### Input/Output Format

GoLLIE uses a Python code-based representation for both the input and output of the model, which offers a clear and human-readable structure and enables the representation of any information extraction task under a unified format, with inputs automatically standardized using Python code formatters.

The model starts generating after the `result = [` line.

### Key Features

GoLLIE is a Large Language Model trained to follow annotation guidelines and outperforms previous approaches on zero-shot Information Extraction while allowing users to perform inferences with annotation schemas defined on the fly.

For more detailed examples, you can refer to the official GoLLIE notebooks on GitHub, particularly the "Relation Extraction.ipynb" notebook which contains complete working examples.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cdfe1345-0378-4e8a-9ec1-b5c83b66a9f1",
  "isSidechain": true,
  "promptId": "0b1e6eb4-459b-4f0f-bf9c-f0f393f18537",
  "agentId": "a72094e6b0cb3482f",
  "type": "user",
  "uuid": "5493c86d-19a1-4def-8839-13a1058dde6d",
  "sourceToolAssistantUUID": "cdfe1345-0378-4e8a-9ec1-b5c83b66a9f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T14:09:15.696Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Cpszue1mTaY8Xn5KGi59SU`</summary>

```json
{
  "url": "https://huggingface.co/HiTZ/GoLLIE-7B",
  "prompt": "Extract: 1. Full model card details - base model, architecture 2. Any code examples showing input/output format 3. Training details 4. Supported tasks 5. Any performance benchmarks or F1 scores listed"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5493c86d-19a1-4def-8839-13a1058dde6d",
  "isSidechain": true,
  "agentId": "a72094e6b0cb3482f",
  "requestId": "req_011Cb4VChiHjKdScbUsSA4NP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19ccece7-e78a-4a8d-bce6-4a9001527b18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01776DieTBYPFgjkxbtdL6YA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1526,
      "cache_read_input_tokens": 22821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1526,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 32 · 2026-05-15T14:09:18.614Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0153Wd9KdMj2qjUZeA9qajmE`</summary>

```json
{
  "url": "https://arxiv.org/html/2310.03668v3",
  "prompt": "I need the EXACT numerical F1 scores from ALL results tables in this paper. Specifically:\n1. Table 2 (supervised results) - all datasets and F1 scores\n2. Table 3 (zero-shot results) - all datasets and F1 scores  \n3. Any results on relation extraction specifically\n4. Does the paper evaluate on SciERC at all?\n5. What IE tasks does it cover? (NER, RE, EE, EAE, Slot Filling?)\n6. The exact Python class definition format with a complete code example from the paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19ccece7-e78a-4a8d-bce6-4a9001527b18",
  "isSidechain": true,
  "agentId": "a72094e6b0cb3482f",
  "requestId": "req_011Cb4VChiHjKdScbUsSA4NP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a670bca3-e9c7-4b3f-aa5b-258b41e70ce0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01776DieTBYPFgjkxbtdL6YA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1526,
      "cache_read_input_tokens": 22821,
      "output_tokens": 337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1526
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 337,
          "cache_read_input_tokens": 22821,
          "cache_creation_input_tokens": 1526,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1526,
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

_source line 33 · 2026-05-15T14:09:25.650Z_

<details><summary>↩ Tool result · `toolu_01Cpszue1mTaY8Xn5KGi59SU`</summary>

````text
# HiTZ/GoLLIE-7B Model Card Summary

## 1. Full Model Details

**Base Model:** CODE-LLaMA2 (7B parameters)

**Architecture:** Text Generation / Causal Language Model

**Developers:** Oscar Sainz, Iker García-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, and Eneko Agirre

**Institution:** HiTZ Basque Center for Language Technology, University of the Basque Country UPV/EHU

**License:** LLaMA2 License (base and merged model); Apache 2.0 (pre-trained LoRA Adapters)

**Language:** English

---

## 2. Code Examples

### Loading the Model

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("HiTZ/GoLLIE-7B", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("HiTZ/GoLLIE-7B", trust_remote_code=True, torch_dtype=torch.bfloat16)
model.to("cuda")
```

### Input/Output Format Example

```python
from dataclasses import dataclass
from typing import List

@dataclass
class Launcher(Template):
    """Refers to a vehicle designed primarily to transport payloads from the Earth's 
    surface to space..."""
    mention: str  
    space_company: str
    crew: List[str]

@dataclass
class Mission(Template):
    """Any planned or accomplished journey beyond Earth's atmosphere..."""
    mention: str
    date: str
    departure: str
    destination: str

# Input text
text = (
    "The Ares 3 mission to Mars is scheduled for 2032. The Starship rocket build by SpaceX will take off from Boca Chica,"
    "carrying the astronauts Max Rutherford, Elena Soto, and Jake Martinez."
)

# Expected output
result = [
    Mission(mention='Ares 3', date='2032', departure='Boca Chica', destination='Mars'),
    Launcher(mention='Starship', space_company='SpaceX', crew=['Max Rutherford', 'Elena Soto', 'Jake Martinez'])
]
```

---

## 3. Training Details

**Datasets Used (8 total):**
- CoNLL2003 (Named Entity Recognition)
- WNUT 17
- NCBI Disease
- Additional unlisted datasets

**Hardware:** 1x A100 GPU

**Training Time:** 44.5 hours

**FLOPs:** 11.9e18

**CO2 Emissions:** 1.57 kg CO2eq

---

## 4. Supported Tasks

- **Named Entity Recognition (NER)**
- **Event Extraction**
- **Relation Extraction**
- **Information Extraction (IE)** - primary task
- **Zero-shot Information Extraction**
- Custom tasks defined on-the-fly via annotation guidelines

---

## 5. Performance Benchmarks

| Metric | Score |
|--------|-------|
| **Supervised Average F1** | 73.0 |
| **Zero-shot Average F1** | 55.3 |

**Note:** GoLLIE-34B achieves higher performance (75.0 supervised F1, 57.2 zero-shot F1)

---

## Key Features

✅ **Guideline-following:** Trained to follow detailed annotation guidelines in docstrings  
✅ **Zero-shot capable:** Outperforms previous approaches on zero-shot IE tasks  
✅ **Custom schemas:** Supports dynamically defined schemas at inference time  
✅ **Flash Attention 2:** Requires CUDA GPU and `trust_remote_code=True` flag

---

## Resources

- 📖 [Paper](https://arxiv.org/abs/2310.03668)
- 💻 [GitHub Repository](https://github.com/hitz-zentroa/GoLLIE)
- 🚀 [Jupyter Notebooks](https://github.com/hitz-zentroa/GoLLIE/tree/main/notebooks)
- 📚 [Blog Post](https://hitz-zentroa.github.io/GoLLIE/)
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19ccece7-e78a-4a8d-bce6-4a9001527b18",
  "isSidechain": true,
  "promptId": "0b1e6eb4-459b-4f0f-bf9c-f0f393f18537",
  "agentId": "a72094e6b0cb3482f",
  "type": "user",
  "uuid": "b6a7e275-a894-4e08-b345-a31564d84f07",
  "sourceToolAssistantUUID": "19ccece7-e78a-4a8d-bce6-4a9001527b18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T14:09:26.086Z_

<details><summary>↩ Tool result · `toolu_0153Wd9KdMj2qjUZeA9qajmE`</summary>

```text
# GoLLIE Paper Results Summary

## Tasks Covered
The paper evaluates on **five IE tasks**: Named Entity Recognition (NER), Relation Extraction (RE), Event Extraction (EE), Event Argument Extraction (EAE), and Slot Filling (SF). However, evaluation focuses on three main tasks: NER, EE, and EAE.

## SciERC Evaluation
**No, SciERC is not evaluated in this paper.** The evaluation datasets are listed in Table 1 and do not include SciERC.

## Table 2: Supervised Results (Selected F1 Scores)

| Dataset | SoTA | Baseline | GoLLIE 7B | GoLLIE 13B | GoLLIE 34B |
|---------|------|----------|-----------|-----------|-----------|
| ACE05 NER | 86.6 | 89.1 | 88.1 | 89.4 | 89.6 |
| CoNLL 2003 | 93.0 | 92.9 | 92.8 | 93.0 | 93.1 |
| BC5CDR | 91.9 | 87.5 | 87.5 | 87.9 | 88.4 |

## Table 3: Zero-Shot Results (Selected F1 Scores)

| Dataset | SoTA | Baseline | GoLLIE 7B | GoLLIE 13B | GoLLIE 34B |
|---------|------|----------|-----------|-----------|-----------|
| MultiNERD | — | 55.0 | 76.0 | 77.5 | 77.2 |
| Music | 53.2 | 56.2 | 67.8 | 65.5 | 68.4 |
| Movie | 63.0 | 43.4 | 63.0 | 62.5 | 62.4 |
| **Average** | **42.6** | **45.4** | **58.4** | **58.3** | **60.0** |

## Relation Extraction Results
RE results appear in supervised settings (Table 2): ACE05 RE shows Baseline 63.8, GoLLIE 7B 63.6, GoLLIE 13B 67.5, GoLLIE 34B 70.1.

## Python Class Definition Format

The paper uses "Python code-based representation" structured with three components. Classes are defined with docstrings containing guidelines and comments for candidates. For example, entities have attributes specified as class variables, with documentation describing what should be extracted and representative examples as code comments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a670bca3-e9c7-4b3f-aa5b-258b41e70ce0",
  "isSidechain": true,
  "promptId": "0b1e6eb4-459b-4f0f-bf9c-f0f393f18537",
  "agentId": "a72094e6b0cb3482f",
  "type": "user",
  "uuid": "bdb6ea63-f07c-4fd0-84b9-e1020ed7afdd",
  "sourceToolAssistantUUID": "a670bca3-e9c7-4b3f-aa5b-258b41e70ce0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-15T14:09:55.120Z_

Now I have comprehensive information. Here is the consolidated report:

---

## GoLLIE (ICLR 2024) -- Research Findings

### 1. Model Architecture

- **Base model: CODE-LLaMA 2** (not plain LLaMA)
- Causal language model fine-tuned with **LoRA adapters** for information extraction
- Requires Flash Attention 2, CUDA GPU, and `trust_remote_code=True`
- License: LLaMA2 License (merged model), Apache 2.0 (LoRA adapters)

### 2. Output Format -- Python Code, NOT JSON

GoLLIE uses a **Python code-based representation** for both input and output. The output is executable Python code, not JSON. The model generates text after a `result = [` prompt, producing dataclass instantiations:

```python
result = [
    Mission(mention='Ares 3', date='2032', departure='Boca Chica', destination='Mars'),
    Launcher(mention='Starship', space_company='SpaceX', crew=['Max Rutherford', 'Elena Soto', 'Jake Martinez'])
]
```

Parsing is done by directly executing the generated Python code, which yields a list of typed objects.

### 3. SciERC Performance

**GoLLIE does NOT evaluate on SciERC.** The paper does not include SciERC in its benchmark suite. However, it does evaluate **relation extraction on ACE05 RE** in supervised settings:

| Model | ACE05 RE F1 |
|-------|------------|
| Baseline (Code-LLaMA) | 63.8 |
| GoLLIE-7B | 63.6 |
| GoLLIE-13B | 67.5 |
| GoLLIE-34B | 70.1 |

Zero-shot evaluation covers NER, EE, and EAE tasks on CrossNER, MultiNERD, Movie, Restaurants, WikiEvents, and CASIE -- but **no zero-shot relation extraction evaluation** is reported.

### 4. GitHub Repo & Model Weights

- **GitHub**: https://github.com/hitz-zentroa/GoLLIE
- **HuggingFace models**:
  - `HiTZ/GoLLIE-7B` -- https://huggingface.co/HiTZ/GoLLIE-7B
  - `HiTZ/GoLLIE-13B` -- https://huggingface.co/HiTZ/GoLLIE-13B
  - `HiTZ/GoLLIE-34B` -- https://huggingface.co/HiTZ/GoLLIE-34B
- **Collection**: https://huggingface.co/collections/HiTZ/gollie-651bf19ee315e8a224aacc4f

### 5. Schema Definition -- Python @dataclass with Docstrings

Entity types and relation types are defined as **Python `@dataclass` classes** inheriting from a `Template` base class. Annotation guidelines are encoded as **docstrings**, and representative annotation candidates appear as **code comments**:

```python
@dataclass
class Launcher(Template):
    """Refers to a vehicle designed primarily to transport payloads from the Earth's 
    surface to space..."""
    mention: str
    space_company: str
    crew: List[str]
```

For relations, the same pattern applies -- e.g., a `PhysicalRelation` class with `arg1: str`, `arg2: str` attributes and a docstring describing the relation semantics. The type constraints in the class definitions (str, List[str], Optional[str]) are enforced in the output. Inputs are standardized using the **Black** Python code formatter.

### 6. Model Sizes & Performance

| Model | Params | Supervised F1 (avg) | Zero-shot F1 (avg) |
|-------|--------|---------------------|---------------------|
| GoLLIE-7B | 7B | 73.0 | 55.3 |
| GoLLIE-13B | 13B | 73.9 | 56.0 |
| GoLLIE-34B | 34B | 75.0 | 57.2 |

Training: 1x A100 GPU, ~44.5 hours for the 7B model. Training datasets include CoNLL2003, ACE05, BC5CDR, WNUT17, NCBI Disease, RAMS, and others (8 total, covering News and Biomedical domains). The five IE tasks covered are NER, RE, EE, EAE, and Slot Filling.

### Key Takeaway for Your Project

GoLLIE's Python-class-as-schema approach is directly relevant to schema-semantic-constrained IE. However, note that (a) it has **no SciERC evaluation**, (b) zero-shot RE is not benchmarked, and (c) relation extraction results are only reported on ACE05 in supervised settings (best: 70.1 F1 with 34B). If you need SciERC RE baselines, you would need to run GoLLIE yourself with custom SciERC schema definitions, or look at other baselines.

Sources:
- [GoLLIE Paper (arXiv)](https://arxiv.org/abs/2310.03668)
- [GoLLIE Paper HTML](https://arxiv.org/html/2310.03668v5)
- [ICLR 2024 Proceedings PDF](https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf)
- [GoLLIE GitHub Repository](https://github.com/hitz-zentroa/GoLLIE)
- [GoLLIE Project Page](https://hitz-zentroa.github.io/GoLLIE/)
- [HiTZ/GoLLIE-7B on HuggingFace](https://huggingface.co/HiTZ/GoLLIE-7B)
- [HiTZ/GoLLIE-13B on HuggingFace](https://huggingface.co/HiTZ/GoLLIE-13B)
- [GoLLIE Relation Extraction Notebook](https://github.com/hitz-zentroa/GoLLIE/blob/main/notebooks/Relation%20Extraction.ipynb)
- [OpenReview Page](https://openreview.net/forum?id=Y3wpuxd7u9)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdb6ea63-f07c-4fd0-84b9-e1020ed7afdd",
  "isSidechain": true,
  "agentId": "a72094e6b0cb3482f",
  "requestId": "req_011Cb4VDnSKmzjjYjGu1X1gH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2483f50c-543f-4d65-ab93-7fb8a1cb5bd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59f61c90-1518-4eee-b679-19b7e383a0b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CWXfF3qd22YG59Bu98om7L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2124,
      "cache_read_input_tokens": 24347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2124,
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
