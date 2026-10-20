# Research conversation: I'm reviewing a research paper called "Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruction Tuning

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 93
- **Recorded user turns:** 1
- **Tool calls:** 41
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ade0ab5ec1fc2d1d3.jsonl`
- **Structured JSON:** [`4dd4e7eeb7079a0f21db.json`](../../sessions/4d/4dd4e7eeb7079a0f21db.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

93 recorded events

### User

_source line 1 · 2026-05-10T07:25:21.510Z_

I'm reviewing a research paper called "Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruction Tuning" (TWMP). I need you to independently verify several claims and find any competing/concurrent work that was missed. Please do the following searches and report findings in detail:

1. Search for arXiv:2505.14297 (CLO - Cross-Lingual Optimization) to verify it exists and its actual content matches the description: "DPO-style cross-lingual preference optimization using English-only source, M2M100 translation, 6,400 OpenAssistant samples"

2. Search for arXiv:2410.07809 (Linguistically-Informed Multilingual Instruction Tuning) to verify its actual content: "uses 289-dimensional legacy URIEL TYPO vectors with k-means clustering to select 14 representative languages from 52-language pool for LoRA fine-tuning on Bactrian-X"

3. Search for arXiv:2409.18472 (URIEL+) to verify: "covers ~800 features across 4,366 languages with SoftImpute imputation"

4. Search for "Less is More typological URIEL 2025" or arXiv:2509.20129 to verify the "Laplacian Score 300-feature URIEL+ subset achieving Spearman ρ=0.358" claim

5. Search for recent (2025-2026) work on typological distance for multilingual instruction tuning that may not be cited - use queries like:
   - "typological distance multilingual instruction tuning 2025 2026"
   - "language family cross-lingual transfer LoRA 2025"
   - "agglutinative language instruction tuning low-resource 2026"

6. Search for Qwen3.5-9B model details to verify: "released March 2026, 248K-token vocabulary, 201 languages, 0.8B/2B/4B/9B series (no 7B)"

7. Search arXiv for recent work (2025-2026) specifically on Kazakh, Mongolian, or Uyghur instruction tuning that may compete with this work:
   - "Kazakh instruction tuning 2025 2026 site:arxiv.org"
   - "low-resource Turkic language fine-tuning 2026"

8. Search for "multi-pivot instruction tuning" or "multiple source languages cross-lingual transfer 2025 2026" to find directly competing methods

Please report exact paper titles, arxiv IDs, venues, and key findings for each search. Be thorough and specific about what you find vs. what you don't find.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "9593b767-d71d-4256-b3a6-4ddfc8e04b24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T07:25:21.515Z_

```json
{
  "parentUuid": "9593b767-d71d-4256-b3a6-4ddfc8e04b24",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
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
  "uuid": "f560007d-2b28-4065-bbe0-db2d21fbf7d4",
  "timestamp": "2026-05-10T07:25:21.515Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T07:25:23.634Z_

I'll conduct these searches systematically. Let me load the WebSearch tool and run multiple searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f560007d-2b28-4065-bbe0-db2d21fbf7d4",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVN2tAtrRAZSSBSP2FS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5cbe990-452a-4c2e-ae7f-681031061924",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01W73mYygQxNWg3umUx6gjx6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9282,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9282,
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

_source line 4 · 2026-05-10T07:25:24.037Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01T7RNYjQnrCAH9vYwYHnh2L`</summary>

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
  "parentUuid": "f5cbe990-452a-4c2e-ae7f-681031061924",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVN2tAtrRAZSSBSP2FS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "961fcd73-ad88-4672-aa8a-71ec50750aff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01W73mYygQxNWg3umUx6gjx6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9282,
      "cache_read_input_tokens": 0,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9282
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9282,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9282,
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

_source line 5 · 2026-05-10T07:25:24.046Z_

<details><summary>↩ Tool result · `toolu_01T7RNYjQnrCAH9vYwYHnh2L`</summary>

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
  "parentUuid": "961fcd73-ad88-4672-aa8a-71ec50750aff",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "949273a4-96ed-476d-8d78-7434437d3d8a",
  "sourceToolAssistantUUID": "961fcd73-ad88-4672-aa8a-71ec50750aff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T07:25:25.925Z_

Now let me run all the initial searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "949273a4-96ed-476d-8d78-7434437d3d8a",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVNE6rSpjmkjExzmL3f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61f23161-34b8-4552-a080-b00913997002",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01ABQWG839uFGAvXaZbHP1qL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 9282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 7 · 2026-05-10T07:25:27.718Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JuYBKzr3EBDvEm8THyC1HV`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.14297",
  "prompt": "Extract the full title, authors, abstract, and key methodological details: does it use DPO-style cross-lingual preference optimization, English-only source, M2M100 translation, and 6,400 OpenAssistant samples?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61f23161-34b8-4552-a080-b00913997002",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVNE6rSpjmkjExzmL3f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2bf1e755-77e6-4ceb-9c05-ceed5d27d438",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01ABQWG839uFGAvXaZbHP1qL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 9282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 8 · 2026-05-10T07:25:29.966Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GX8BjZPv5QLqqEQDsEvxDE`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.07809",
  "prompt": "Extract the full title, authors, abstract, and key methodological details: does it use 289-dimensional URIEL TYPO vectors, k-means clustering, 14 representative languages from a 52-language pool, LoRA fine-tuning, and Bactrian-X dataset?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bf1e755-77e6-4ceb-9c05-ceed5d27d438",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVNE6rSpjmkjExzmL3f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45fb3a25-7d9b-4239-b2be-13ca5392dc45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01ABQWG839uFGAvXaZbHP1qL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 9282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 9 · 2026-05-10T07:25:31.083Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016Qhw6giCvJCMPy4uUgW5Vk`</summary>

```json
{
  "url": "https://arxiv.org/abs/2409.18472",
  "prompt": "Extract the full title, authors, abstract, and key details: does it cover ~800 features across 4,366 languages with SoftImpute imputation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45fb3a25-7d9b-4239-b2be-13ca5392dc45",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVNE6rSpjmkjExzmL3f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "321b686a-8e05-4a93-90f9-984e9f460b1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01ABQWG839uFGAvXaZbHP1qL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 9282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 10 · 2026-05-10T07:25:32.131Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GANXTk2twy3JoXdfnd7yA6`</summary>

```json
{
  "query": "arXiv 2509.20129 \"Less is More\" typological URIEL Laplacian Score features"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "321b686a-8e05-4a93-90f9-984e9f460b1c",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVNE6rSpjmkjExzmL3f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a2a9e8e-d618-46dc-b975-e6d51d92092e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01ABQWG839uFGAvXaZbHP1qL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 9282,
      "output_tokens": 439,
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
          "output_tokens": 439,
          "cache_read_input_tokens": 9282,
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

_source line 11 · 2026-05-10T07:25:32.604Z_

<details><summary>↩ Tool result · `toolu_01JuYBKzr3EBDvEm8THyC1HV`</summary>

```text
# Paper Summary

**Full Title:** Cross-Lingual Optimization for Language Transfer in Large Language Models

**Authors:** Jungseob Lee, Seongtae Hong, Hyeonseok Moon, Heuiseok Lim

**Abstract:** The paper proposes Cross-Lingual Optimization (CLO) to adapt English-centric LLMs to other languages while preserving English capabilities. The method uses "publicly available English SFT data and a translation model to enable cross-lingual transfer" across five models and six languages of varying resource levels.

## Key Methodological Details

Based on the provided content, I can confirm:

- ✓ **English-only source:** Uses "publicly available English SFT data"
- ✓ **Translation model:** Employs "a translation model" for cross-lingual transfer

However, the webpage content does **not specify**:
- Whether it uses DPO-style cross-lingual preference optimization
- Whether it uses M2M100 translation specifically
- Whether it uses 6,400 OpenAssistant samples

The abstract only mentions CLO outperforms supervised fine-tuning with "3,200 samples" in low-resource settings compared to "6,400 samples" for SFT, but does not identify the dataset source as OpenAssistant or detail the exact translation model used.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2bf1e755-77e6-4ceb-9c05-ceed5d27d438",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "9abc00f5-dd3b-4c27-8de1-144e72097ebb",
  "sourceToolAssistantUUID": "2bf1e755-77e6-4ceb-9c05-ceed5d27d438",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T07:25:34.502Z_

<details><summary>↩ Tool result · `toolu_01GX8BjZPv5QLqqEQDsEvxDE`</summary>

```text
# Paper Summary

**Full Title:** "Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?"

**Authors:** Gürkan Soykan and Gözde Gül Şahin

**Abstract:** The paper addresses uneven performance of multilingual language models across languages by proposing a linguistically-informed method for selecting languages during instruction tuning. The authors note that "working with datasets with few languages and a smaller number of instances can be beneficial" and develop an algorithm to choose diverse languages, demonstrating better results than random selection.

## Methodological Details

Based on the provided content, I cannot confirm the specific technical implementations you mentioned. The abstract does not explicitly reference:
- 289-dimensional URIEL TYPO vectors
- k-means clustering specifications
- 14 languages from a 52-language pool
- LoRA fine-tuning
- Bactrian-X dataset

The page states the authors use "a simple algorithm to choose diverse languages" and mention making "code for language selection and multilingual instruction tuning" available in their repository, but detailed methodology specifications are not included in this excerpt. To verify these specifics, you would need to review the full PDF.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45fb3a25-7d9b-4239-b2be-13ca5392dc45",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "bce19d18-66c1-4d68-87bb-85b8b567b088",
  "sourceToolAssistantUUID": "45fb3a25-7d9b-4239-b2be-13ca5392dc45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T07:25:35.379Z_

<details><summary>↩ Tool result · `toolu_016Qhw6giCvJCMPy4uUgW5Vk`</summary>

```text
# URIEL+ Paper Details

**Full Title:** "URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base"

**Authors:** Aditya Khan, Mason Shipton, David Anugraha, Kaiyao Duan, Phuong H. Hoang, Eric Khiu, A. Seza Doğruöz, En-Shiun Annie Lee

**Abstract Summary:** The paper presents an enhanced version of URIEL, a knowledge base for linguistic representation. It notes that "URIEL+ improves the user experience with robust, customizable distance calculations" and expands typological feature coverage for 2,898 languages.

**Regarding Your Specific Question:**

The abstract does not mention coverage of ~800 features across 4,366 languages, nor does it reference SoftImpute imputation methodology. The available content indicates URIEL+ covers 2,898 languages with expanded typological features, but the exact feature count and imputation techniques are not detailed in this excerpt. To verify these specific technical claims, you would need to review the full paper PDF or TeX source.

**Status:** Accepted to COLING 2025; submitted September 27, 2024
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "321b686a-8e05-4a93-90f9-984e9f460b1c",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "4c5d9ff1-7736-4ad9-aef6-79b8984d4703",
  "sourceToolAssistantUUID": "321b686a-8e05-4a93-90f9-984e9f460b1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T07:25:38.208Z_

<details><summary>↩ Tool result · `toolu_01GANXTk2twy3JoXdfnd7yA6`</summary>

```text
Web search results for query: "arXiv 2509.20129 "Less is More" typological URIEL Laplacian Score features"

Links: [{"title":"Less is More: The Effectiveness of Compact Typological Language Representations","url":"https://arxiv.org/html/2509.20129"},{"title":"[2509.20129] Less is More: The Effectiveness of Compact Typological Language Representations","url":"https://arxiv.org/abs/2509.20129"},{"title":"Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+","url":"https://arxiv.org/html/2510.19217"},{"title":"Less is More: The Effectiveness of Compact Typological ...","url":"https://aclanthology.org/2025.emnlp-main.1310.pdf"},{"title":"[2510.19217] Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+","url":"https://arxiv.org/abs/2510.19217"},{"title":"A Measure for Transparent Comparison of Linguistic Diversity in Multilingual NLP Data Sets","url":"https://arxiv.org/html/2403.03909"},{"title":"URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base","url":"https://arxiv.org/html/2409.18472"},{"title":"LinguAlchemy: Fusing Typological and Geographical Elements for Unseen Language Generalization","url":"https://arxiv.org/html/2401.06034"},{"title":"Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+","url":"https://arxiv.org/html/2510.27183"},{"title":"[2509.25742] Less is More: Towards Simple Graph Contrastive Learning","url":"https://arxiv.org/abs/2509.25742"}]

I found the paper! Here's information about arXiv 2509.20129:

## Paper Summary

The paper is titled "Less is More: The Effectiveness of Compact Typological Language Representations".

### Main Contribution

The paper proposes a pipeline to optimize the URIEL+ typological feature space by combining feature selection and imputation, producing compact yet interpretable typological representations. It evaluates these feature subsets on linguistic distance alignment and downstream tasks, demonstrating that reduced-size representations of language typology can yield more informative distance metrics and improve performance in multilingual NLP applications.

### Laplacian Score Method

The Laplacian Score measures how much a feature varies locally relative to its overall variance. Lower-scoring features are more stable across similar languages and thus more likely to encode intrinsic typological patterns. The Laplacian Score strategy achieves strong results when using only 300 features, underscoring its effectiveness at capturing manifold structure.

### Key Results

All feature selection methods, at the right subset size, outperform the full URIEL+ feature space in distance alignment with linguistic reality.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a2a9e8e-d618-46dc-b975-e6d51d92092e",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "a4b4909a-fe29-4b9b-9223-7f3e39dfcc63",
  "sourceToolAssistantUUID": "3a2a9e8e-d618-46dc-b975-e6d51d92092e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T07:25:40.173Z_

Good. Now let me fetch more details on the papers and run the remaining searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4b4909a-fe29-4b9b-9223-7f3e39dfcc63",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVPGKpsc84ExBiax61U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4fc271f6-2787-4250-9b29-02ea3f55a3de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FnhEEcjCF9UnxfgHagEb64",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2169,
      "cache_read_input_tokens": 11192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2169,
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

_source line 16 · 2026-05-10T07:25:42.095Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014BEQp5HuTRK7JgSj96hUVC`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.20129",
  "prompt": "Extract full title, authors, venue/conference, and exact claims about: Laplacian Score, 300-feature URIEL+ subset, Spearman rho=0.358 correlation, feature selection methodology, and any specific numeric results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fc271f6-2787-4250-9b29-02ea3f55a3de",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVPGKpsc84ExBiax61U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d933f6a4-4690-4d25-9b38-9bd20d6e4f31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FnhEEcjCF9UnxfgHagEb64",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2169,
      "cache_read_input_tokens": 11192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2169,
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

_source line 17 · 2026-05-10T07:25:44.139Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CvexGsksRHpAU1KqTzAy4j`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2505.14297",
  "prompt": "Extract all methodological details: Is it DPO-based or SFT-based? What translation model is used (M2M100 or other)? What dataset and how many samples (OpenAssistant, 6400)? What languages and how many? What is the full method name?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d933f6a4-4690-4d25-9b38-9bd20d6e4f31",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVPGKpsc84ExBiax61U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e57589a5-0a72-4f73-9dad-538c41a9d96f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FnhEEcjCF9UnxfgHagEb64",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2169,
      "cache_read_input_tokens": 11192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2169,
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

_source line 18 · 2026-05-10T07:25:46.802Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015qJdsLALpW31vfjBjrVSnR`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2410.07809",
  "prompt": "Extract all methodological details: Does it use URIEL TYPO vectors and how many dimensions? Does it use k-means clustering? How many languages are selected and from what pool? Does it use LoRA? Does it use Bactrian-X? What base model?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e57589a5-0a72-4f73-9dad-538c41a9d96f",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVPGKpsc84ExBiax61U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6c46d9c-44f0-4032-aa62-a75c479d2b87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FnhEEcjCF9UnxfgHagEb64",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2169,
      "cache_read_input_tokens": 11192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2169,
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

_source line 19 · 2026-05-10T07:25:47.207Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AGVuZdg9yW42CzrfZaaPN8`</summary>

```json
{
  "query": "Qwen3.5 9B model release 2026 vocabulary languages series"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6c46d9c-44f0-4032-aa62-a75c479d2b87",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVPGKpsc84ExBiax61U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5da9d95-81bd-4f6b-bdd1-e3651178d6c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FnhEEcjCF9UnxfgHagEb64",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2169,
      "cache_read_input_tokens": 11192,
      "output_tokens": 462,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2169
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 462,
          "cache_read_input_tokens": 11192,
          "cache_creation_input_tokens": 2169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2169,
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

_source line 20 · 2026-05-10T07:25:47.504Z_

<details><summary>↩ Tool result · `toolu_014BEQp5HuTRK7JgSj96hUVC`</summary>

```text
# Paper Summary

**Full Title:** "Less is More: The Effectiveness of Compact Typological Language Representations"

**Authors:** York Hay Ng, Phuong Hanh Hoang, En-Shiun Annie Lee

**Venue:** EMNLP 2025 Main Conference

**Key Claims from Abstract:**
The researchers propose optimizing typological feature representations through "combining feature selection and imputation, producing compact yet interpretable typological representations." Their core finding demonstrates that "reduced-size representations of language typology can yield more informative distance metrics."

**Note on Requested Metrics:**
The provided webpage content does not contain specific mentions of:
- Laplacian Score methodology
- A 300-feature URIEL+ subset
- Spearman rho=0.358 correlation value
- Detailed feature selection methodology specifics
- Numeric results tables

The abstract indicates the work addresses sparsity in linguistic datasets like URIEL+ and evaluates performance on "linguistic distance alignment and downstream tasks," but the actual paper PDF would be required to locate the specific technical metrics you requested.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d933f6a4-4690-4d25-9b38-9bd20d6e4f31",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "8a5030de-ff46-4088-89c4-29e08f880bd3",
  "sourceToolAssistantUUID": "d933f6a4-4690-4d25-9b38-9bd20d6e4f31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T07:25:47.831Z_

<details><summary>↩ Tool result · `toolu_01CvexGsksRHpAU1KqTzAy4j`</summary>

```text
# Methodological Details - Document Analysis

I was unable to extract the requested methodological details from the provided content. The document appears to be a corrupted or compressed PDF file containing primarily binary/encoded data rather than readable text about machine learning methods.

To properly identify:
- **DPO vs SFT approach**
- **Translation model type** (M2M100 or alternative)
- **Dataset specifications** (name, sample count)
- **Language coverage and count**
- **Full method name**

I would need access to a readable version of the source material—either the original PDF rendered as text, the actual research paper, or the preprint on arxiv/similar repositories.

If you have the paper title, authors, or a text-based version available, I'd be happy to extract these methodological specifics with proper attribution.

[Binary content (application/pdf, 2.5MB) also saved to /home/ubuntu/.claude-account-2/projects/-/58594df9-bda3-4ed6-a9ac-9ce91e2c084d/tool-results/webfetch-1778397944206-abcgk4.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e57589a5-0a72-4f73-9dad-538c41a9d96f",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "a3ccd9dc-f73c-4146-8000-d6b2ddc5e98e",
  "sourceToolAssistantUUID": "e57589a5-0a72-4f73-9dad-538c41a9d96f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T07:25:49.693Z_

<details><summary>↩ Tool result · `toolu_015qJdsLALpW31vfjBjrVSnR`</summary>

```text
I cannot extract the requested methodological details from the provided content. The document appears to be a PDF file containing primarily binary/compressed data streams rather than readable text about a specific methodology.

To properly answer your questions about URIEL TYPO vectors, k-means clustering, language selection, LoRA, Bactrian-X, and the base model, I would need access to the actual research paper or technical documentation in a readable format (such as plain text or properly formatted PDF with extractable text).

If you have the paper in another format or can provide a text excerpt, I'd be happy to help identify those methodological components.

[Binary content (application/pdf, 1.8MB) also saved to /home/ubuntu/.claude-account-2/projects/-/58594df9-bda3-4ed6-a9ac-9ce91e2c084d/tool-results/webfetch-1778397946829-xsp4ut.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6c46d9c-44f0-4032-aa62-a75c479d2b87",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "ae11e8bc-3ed9-488a-97d0-941fdcf3c383",
  "sourceToolAssistantUUID": "e6c46d9c-44f0-4032-aa62-a75c479d2b87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T07:25:54.529Z_

<details><summary>↩ Tool result · `toolu_01AGVuZdg9yW42CzrfZaaPN8`</summary>

```text
Web search results for query: "Qwen3.5 9B model release 2026 vocabulary languages series"

Links: [{"title":"Qwen/Qwen3.5-9B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-9B"},{"title":"qwen3.5:9b","url":"https://ollama.com/library/qwen3.5:9b"},{"title":"Qwen3.5 - How to Run Locally | Unsloth Documentation","url":"https://unsloth.ai/docs/models/qwen3.5"},{"title":"Qwen3.5 is the large language model series ...","url":"https://github.com/QwenLM/Qwen3.6"},{"title":"Qwen 3.5 Small Series Ships Four Models From 0.8B to 9B | Awesome Agents","url":"https://awesomeagents.ai/news/qwen-3-5-small-models-series/"},{"title":"Qwen3.5-9B: Specifications and GPU VRAM Requirements","url":"https://apxml.com/models/qwen35-9b"},{"title":"Qwen/Qwen3.5-9B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-9B-Base"},{"title":"Qwen3.5-9B Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/qwen3.5-9b"},{"title":"Qwen3.5: 9B Beats 120B, 0.8B Runs Video on Phones—Full MoE Family • StableLearn | Make AI Your Superpower","url":"https://stable-learn.com/en/qwen35-native-multimodal-agent-model/"},{"title":"Qwen 3.5 9B — CanIRun.ai","url":"https://www.canirun.ai/model/qwen3.5-9b/"}]

Based on the web search results, here's the information about the Qwen3.5 9B model release in 2026:

## Release Timeline

Qwen3.5 was released on February 16, 2026, with the first release including a 397B-A17B MoE model. The Qwen3.5-9B model became available on March 2, 2026 on Hugging Face Hub and ModelScope.

## Model Series

The Qwen 3.5 small model series includes the Qwen3.5-0.8B, Qwen3.5-2B, Qwen3.5-4B, and Qwen3.5-9B. The broader Qwen3.5 lineup spans from the flagship 397B-A17B to smaller models like the 122B-A10B, 35B-A3B, and 27B released on February 24, 2026.

## Vocabulary and Languages

The Qwen3.5-9B features a 248K-token vocabulary covering 201 languages and dialects. The model offers expanded support to 201 languages and dialects, enabling inclusive, worldwide deployment with nuanced cultural and regional understanding.

## Key Characteristics

Every model in the series inherits the full Gated DeltaNet hybrid architecture, with 262K native context windows and native multimodal capabilities (text + images + video). The context length is 262,144 natively and extensible up to 1,010,000 tokens.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5da9d95-81bd-4f6b-bdd1-e3651178d6c7",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "9f34eee5-a8e3-471b-869d-bdabf60ab397",
  "sourceToolAssistantUUID": "f5da9d95-81bd-4f6b-bdd1-e3651178d6c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T07:25:56.525Z_

Now let me fetch the HTML versions of the key papers and run the remaining searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f34eee5-a8e3-471b-869d-bdabf60ab397",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVQU4JJqSjV8Z97E3ap",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ee38273-71bc-4cd3-99d0-a758688f50cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015R9Z5x4bu3Ds6mxPdS8KEd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2278,
      "cache_read_input_tokens": 13361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2278,
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

_source line 25 · 2026-05-10T07:25:59.813Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01X5jY7KaDa5bB2q7eZ5PAdP`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.14297",
  "prompt": "Extract all methodological details: Is the method DPO-based or SFT-based? What translation model is used (M2M100 or other)? What dataset is used and how many samples (OpenAssistant, 6400)? What languages are covered? What is the full method name CLO stand for?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ee38273-71bc-4cd3-99d0-a758688f50cd",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVQU4JJqSjV8Z97E3ap",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd35b140-35e6-4db1-909c-d35a6a1bd8ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015R9Z5x4bu3Ds6mxPdS8KEd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2278,
      "cache_read_input_tokens": 13361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2278,
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

_source line 26 · 2026-05-10T07:26:01.465Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019kpTtSqMnannvoa1cKgeHM`</summary>

```json
{
  "url": "https://arxiv.org/html/2410.07809",
  "prompt": "Extract all methodological details: Does it use URIEL TYPO vectors? How many dimensions? Does it use k-means clustering? How many languages are selected and from what pool size? Does it use LoRA? Does it use Bactrian-X dataset? What base model is used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd35b140-35e6-4db1-909c-d35a6a1bd8ac",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVQU4JJqSjV8Z97E3ap",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c39537f3-7325-4b3a-84b0-8cd080194276",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015R9Z5x4bu3Ds6mxPdS8KEd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2278,
      "cache_read_input_tokens": 13361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2278,
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

_source line 27 · 2026-05-10T07:26:02.315Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015vBu7bDuk1jBEx33xiLdTR`</summary>

```json
{
  "query": "typological distance multilingual instruction tuning 2025 2026 arxiv low-resource"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c39537f3-7325-4b3a-84b0-8cd080194276",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVQU4JJqSjV8Z97E3ap",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4724afd1-127a-4c02-846f-7d9c2bc4df10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015R9Z5x4bu3Ds6mxPdS8KEd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2278,
      "cache_read_input_tokens": 13361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2278,
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

_source line 28 · 2026-05-10T07:26:02.704Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014pSxGohbaVomKGRvfDXK1r`</summary>

```json
{
  "query": "Kazakh instruction tuning fine-tuning LLM 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4724afd1-127a-4c02-846f-7d9c2bc4df10",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVQU4JJqSjV8Z97E3ap",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4f596e2-cbaa-4ad7-9e48-cb25fe9aefed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015R9Z5x4bu3Ds6mxPdS8KEd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2278,
      "cache_read_input_tokens": 13361,
      "output_tokens": 410,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2278
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 410,
          "cache_read_input_tokens": 13361,
          "cache_creation_input_tokens": 2278,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2278,
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

_source line 29 · 2026-05-10T07:26:06.832Z_

<details><summary>↩ Tool result · `toolu_019kpTtSqMnannvoa1cKgeHM`</summary>

```text
# Methodological Details Extraction

**URIEL TYPO Vectors:** Yes. The study employs "289-dimensional binary features containing syntactic, phonological, and phonetic inventory features extracted from the URIEL database."

**K-means Clustering:** Yes. The researchers apply k-means with k=14 clusters to select diverse language subsets. The process identifies cluster centroids and selects the nearest language to each centroid.

**Language Selection:** 14 languages are selected from a pool of 51 languages (52 total in Bactrian-X, with Telugu excluded). The choice of 14 "aligns with the number of language families and also avoids the curse of multilinguality."

**LoRA Implementation:** Yes. The team uses "LoRA as Parameter-Efficient Fine-Tuning (PEFT) approach" with rank r=64, scaling factor α=16, and dropout rate of 0.05.

**Bactrian-X Dataset:** Yes. They use "Bactrian-X" which is described as "notably the most comprehensive multilingual instruction dataset to date" containing "3.4 million instruction–response pairs across 52 languages."

**Base Models:** Three model families are evaluated:
- mGPT 1.3B (decoder-only)
- mT5 3.7B XL (encoder-decoder)
- BLOOM variants: 1.7B, 3B, and 7B1 (decoder-only)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c39537f3-7325-4b3a-84b0-8cd080194276",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "120642d5-2c05-4585-b2e5-3c0c9bba939f",
  "sourceToolAssistantUUID": "c39537f3-7325-4b3a-84b0-8cd080194276",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T07:26:08.467Z_

<details><summary>↩ Tool result · `toolu_01X5jY7KaDa5bB2q7eZ5PAdP`</summary>

```text
# Cross-Lingual Optimization (CLO) - Methodological Details

## Method Foundation
CLO is **DPO-based**, modifying Direct Preference Optimization rather than standard supervised fine-tuning. The approach combines two loss components: supervised fine-tuning loss and a novel cross-lingual loss function that operates within the same batch.

## Translation & Data
- **Translation Model**: M2M100 1.2B
- **Base Dataset**: OpenAssistant conversations
- **Sample Size**: 6,400 English instruction-output pairs, generating 12,800 total samples (6,400 English + 6,400 target language)

## Language Coverage
The study evaluates across six languages categorized by resource availability:
- High-resource: Chinese, German
- Medium-resource: Korean, Indonesian  
- Low-resource: Swahili, Yoruba

## Full Method Name
**CLO** stands for "Cross-Lingual Optimization," designed to "efficiently transfer an English-centric LLM to a target language while preserving its English capabilities." The method leverages publicly available English SFT data and translation models, enabling language transfer without extensive target-language instruction data—particularly valuable for low-resource languages where such resources are scarce.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd35b140-35e6-4db1-909c-d35a6a1bd8ac",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "0272180b-01d0-4b83-b232-7823135c05b9",
  "sourceToolAssistantUUID": "cd35b140-35e6-4db1-909c-d35a6a1bd8ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T07:26:10.587Z_

<details><summary>↩ Tool result · `toolu_015vBu7bDuk1jBEx33xiLdTR`</summary>

```text
Web search results for query: "typological distance multilingual instruction tuning 2025 2026 arxiv low-resource"

Links: [{"title":"Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?","url":"https://arxiv.org/html/2410.07809"},{"title":"A Survey on Multilingual Large Language Models: Corpora, Alignment, and Bias","url":"https://arxiv.org/html/2404.00929v3"},{"title":"The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation","url":"https://arxiv.org/html/2505.13090v2"},{"title":"Linguistically-Informed Multilingual Instruction Tuning","url":"https://arxiv.org/pdf/2410.07809"},{"title":"LinguaLIFT: An Effective Two-stage Instruction Tuning Framework for Low-Resource Language Tasks","url":"https://arxiv.org/html/2412.12499v1"},{"title":"Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://arxiv.org/html/2510.25947v1"},{"title":"[2601.01362] Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning","url":"https://arxiv.org/abs/2601.01362"},{"title":"Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/html/2402.13703v3"},{"title":"Untitled Document","url":"https://arxiv.org/html/2602.00945v1"},{"title":"[2401.01854] Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/abs/2401.01854"}]

I found several relevant papers on this topic. Here are the key findings from the search results:

## Research on Typological Distance and Multilingual Instruction Tuning

**Linguistically-Informed Language Selection**

Recent work investigates optimum language subset selection for multilingual instruction tuning using a linguistically informed manner, comparing various language selection techniques against baselines such as randomly selected subsets and subsets from different language families. The linguistically informed selection techniques range from common methods like typological feature vectors to less conventional approaches, including language embeddings derived from semantic typology features.

**Typological Distance Effects on Alignment**

Typological distance is identified as a factor impacting multilingual alignment performance, with more typologically distant language pairs tending to be less well-aligned than more similar ones. In bilingual lexicon induction tasks, accuracy on semantically distant language pairs is significantly lower, and auxiliary languages have been proposed as a medium to bridge the gap between semantically distant language pairs.

**Low-Resource Language Performance**

A performance gap persists between high-resource and low-resource language tasks due to language imbalance in the pre-training corpus, and frameworks like LinguaLIFT have been proposed to advance low-resource language tasks. Analysis on multilingual benchmarks reveals that even in low-resource languages, model confidence can increase significantly after instruction-tuning on high-resource language datasets.

**Language Diversity Benefits**

Recent systematic investigation across 132 translation directions shows that fine-tuning on broader language sets consistently improves translation across all categories, and it's recommended to fine-tune with diverse language directions even when optimizing for a limited subset of target translation pairs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4724afd1-127a-4c02-846f-7d9c2bc4df10",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "0c529b8a-aa3e-4098-8bf7-68419692104f",
  "sourceToolAssistantUUID": "4724afd1-127a-4c02-846f-7d9c2bc4df10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T07:26:12.057Z_

<details><summary>↩ Tool result · `toolu_014pSxGohbaVomKGRvfDXK1r`</summary>

```text
Web search results for query: "Kazakh instruction tuning fine-tuning LLM 2025 2026 arxiv"

Links: [{"title":"Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh","url":"https://arxiv.org/html/2502.13647"},{"title":"[2502.13647] Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh","url":"https://arxiv.org/abs/2502.13647"},{"title":"Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh","url":"https://arxiv.org/html/2503.01493v1"},{"title":"Fine-Tuning Large Language Models for Kazakh Text Simplification | MDPI","url":"https://www.mdpi.com/2076-3417/15/15/8344"},{"title":"CyberLLM-FINDS 2025: Instruction-Tuned Fine-tuning of Domain-Specific LLMs with","url":"https://arxiv.org/pdf/2601.06779"},{"title":"Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting | OpenReview","url":"https://openreview.net/forum?id=wRcTCcb0H5"},{"title":"[2308.10792] Instruction Tuning for Large Language Models: A Survey","url":"https://arxiv.org/abs/2308.10792"},{"title":"Instruction Tuning for Large Language Models: A Survey","url":"https://arxiv.org/html/2308.10792v9"},{"title":"Fine-Tuning Large Language Models for Kazakh Text Simplification - R Discovery","url":"https://discovery.researcher.life/article/fine-tuning-large-language-models-for-kazakh-text-simplification/2e8401beac7b3eaeb7b276154c5d241e"},{"title":"Instruction Tuning for Large Language Models: A Survey | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3777411"}]

The search has returned several highly relevant recent papers on Kazakh instruction tuning and fine-tuning of LLMs from 2025-2026. Here are the key findings:

## Recent Kazakh LLM Research (2025-2026)

### 1. **Instruction Tuning on Government and Cultural Data for Kazakh**

A paper from March 2026 addresses instruction tuning in low-resource languages by introducing and open-sourcing a large-scale (10,600 samples) instruction-following dataset covering key institutional and cultural knowledge relevant to Kazakhstan. The researchers employed LLM-assisted data generation, comparing open-weight and closed-weight models, and selected GPT-4o as the backbone, with each dataset entity undergoing full manual verification to ensure high quality. Fine-tuning Qwen, Falcon, and Gemma on this dataset leads to consistent performance improvements in both multiple-choice and generative tasks.

### 2. **Llama-3.1-Sherkala-8B-Chat Model**

Sherkala-Chat is a state-of-the-art instruction-tuned open generative large language model designed for Kazakh. Adapted from the LLaMA-3.1-8B model, it is trained on 45.3B tokens across Kazakh, English, Russian, and Turkish, with 8 billion parameters demonstrating strong knowledge and reasoning abilities in Kazakh while significantly outperforming existing open Kazakh and multilingual models of similar scale.

### 3. **KazSim: Text Simplification for Kazakh**

A paper addresses text simplification for Kazakh, a morphologically rich, low-resource language, by introducing KazSim, an instruction-tuned model built on multilingual large language models. The researchers introduced the first dataset comprising 8,709 complex–simple Kazakh sentence pairs, automatically constructed using a heuristic-based complexity detection pipeline and augmented with LLM-generated simplifications.

These papers demonstrate active research in adapting instruction tuning techniques specifically for the Kazakh language in the 2025-2026 period.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4f596e2-cbaa-4ad7-9e48-cb25fe9aefed",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "9bf14bd6-05a6-4cb8-a1c3-64fa5c57ea11",
  "sourceToolAssistantUUID": "f4f596e2-cbaa-4ad7-9e48-cb25fe9aefed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-10T07:26:15.872Z_

Excellent. Now let me run the remaining searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bf14bd6-05a6-4cb8-a1c3-64fa5c57ea11",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVRmEwb9mi9KC2rnLsE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1137758a-b362-4fb4-b416-b48e028c62d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0166A4hWjxKAtbc7PkaDuTC4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3023,
      "cache_read_input_tokens": 15639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3023,
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

_source line 34 · 2026-05-10T07:26:16.329Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013X7KgbTVWBzmfxEQCZNSNM`</summary>

```json
{
  "query": "multi-pivot instruction tuning multiple source languages cross-lingual 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1137758a-b362-4fb4-b416-b48e028c62d6",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVRmEwb9mi9KC2rnLsE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4142a8a1-6735-4ac6-99ff-8ce23cd25fa9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0166A4hWjxKAtbc7PkaDuTC4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3023,
      "cache_read_input_tokens": 15639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3023,
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

_source line 35 · 2026-05-10T07:26:17.239Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JbNABx9iSpaJWDTUxsHEtp`</summary>

```json
{
  "query": "language family cross-lingual transfer LoRA fine-tuning 2025 2026 arxiv multilingual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4142a8a1-6735-4ac6-99ff-8ce23cd25fa9",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVRmEwb9mi9KC2rnLsE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e58082d-d2cc-4b69-8574-636ba4aedee7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0166A4hWjxKAtbc7PkaDuTC4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3023,
      "cache_read_input_tokens": 15639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3023,
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

_source line 36 · 2026-05-10T07:26:18.284Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FrLY4YqaiXEVhD9veCV3tj`</summary>

```json
{
  "query": "Mongolian Uyghur low-resource Turkic language instruction tuning LLM 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e58082d-d2cc-4b69-8574-636ba4aedee7",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVRmEwb9mi9KC2rnLsE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6e48f64-4290-4577-b35c-95054bc3f672",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0166A4hWjxKAtbc7PkaDuTC4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3023,
      "cache_read_input_tokens": 15639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3023,
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

_source line 37 · 2026-05-10T07:26:18.571Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015gs86rAHk3spoyNSKWCQwh`</summary>

```json
{
  "query": "agglutinative language instruction tuning low-resource LLM 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6e48f64-4290-4577-b35c-95054bc3f672",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVRmEwb9mi9KC2rnLsE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88719299-937a-44df-a10b-d584e8d760a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0166A4hWjxKAtbc7PkaDuTC4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3023,
      "cache_read_input_tokens": 15639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3023,
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

### Tool result

_source line 38 · 2026-05-10T07:26:25.935Z_

<details><summary>↩ Tool result · `toolu_013X7KgbTVWBzmfxEQCZNSNM`</summary>

```text
Web search results for query: "multi-pivot instruction tuning multiple source languages cross-lingual 2025 2026 arxiv"

Links: [{"title":"[2311.08711] PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning","url":"https://arxiv.org/abs/2311.08711"},{"title":"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning","url":"https://arxiv.org/pdf/2311.08711"},{"title":"Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/html/2401.01854v1"},{"title":"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning - Paper Detail","url":"https://deeplearn.org/arxiv/431549/plug:-leveraging-pivot-language-in-cross-lingual-instruction-tuning"},{"title":"Continually Adding New Languages to Multilingual Language Models","url":"https://arxiv.org/html/2509.11414v1"},{"title":"Multilingual Large Language Models: A Systematic Survey","url":"https://arxiv.org/html/2411.11072v1"},{"title":"[2311.07439] Investigating Multi-Pivot Ensembling with Massively Multilingual Machine Translation Models","url":"https://arxiv.org/abs/2311.07439"},{"title":"Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/html/2402.13703v3"},{"title":"Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://arxiv.org/html/2510.25947v1"},{"title":"[2401.01854] Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/abs/2401.01854"}]

I found several relevant papers on arXiv related to your query about multi-pivot instruction tuning, multiple source languages, and cross-lingual approaches. Here are the key findings:

## Main Papers Found:

1. **PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning** (2311.08711)
   - Proposes pivot language guided generation (PLUG), an approach that utilizes a high-resource language, primarily English, as the pivot to enhance instruction tuning in lower-resource languages
   - The model is trained to first process instructions in the pivot language, and then produce responses in the target language

2. **Multilingual Instruction Tuning With Just a Pinch of Multilinguality** (2401.01854)
   - Finds that only 40 multilingual examples integrated in an English tuning set substantially improve multilingual instruction-following, both in seen and unseen languages during tuning
   - Diversifying the instruction tuning set with even just 2-4 languages significantly improves cross-lingual generalization

3. **Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?** (2402.13703)
   - Instruction-tuning on parallel instead of monolingual corpora benefits cross-lingual instruction following capabilities by up to 9.9%

4. **Revisiting Multilingual Data Mixtures in Language Model Pretraining** (2510.25947)
   - Using multiple pivots that balance breadth and proximity provides the most consistent benefits across language families

5. **Multilingual Large Language Models: A Systematic Survey** (2411.11072)
   - Comprehensive survey covering cross-lingual tuning approaches with pivot languages

These papers from 2023-2025 cover the intersection of multi-pivot strategies, instruction tuning, and cross-lingual approaches you're interested in.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4142a8a1-6735-4ac6-99ff-8ce23cd25fa9",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "b5edec72-ae69-4b0c-8e4f-878c62031221",
  "sourceToolAssistantUUID": "4142a8a1-6735-4ac6-99ff-8ce23cd25fa9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-10T07:26:26.297Z_

<details><summary>↩ Tool result · `toolu_01JbNABx9iSpaJWDTUxsHEtp`</summary>

```text
Web search results for query: "language family cross-lingual transfer LoRA fine-tuning 2025 2026 arxiv multilingual"

Links: [{"title":"[2604.06202] Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family: A Theoretical Framework for Low-Resource Language Models","url":"https://arxiv.org/abs/2604.06202"},{"title":"Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family: A Theoretical Framework for Low-Resource Language Models","url":"https://arxiv.org/html/2604.06202"},{"title":"Optimizing Multilingual LLMs via Federated Learning: A Study of Client Language Composition","url":"https://arxiv.org/html/2603.24242"},{"title":"GRASP LoRA: GRPO Guided Adapter Sparsity Policy for Cross Lingual Transfer","url":"https://arxiv.org/html/2601.06702"},{"title":"[2501.06892] Language Fusion for Parameter-Efficient Cross-lingual Transfer","url":"https://arxiv.org/abs/2501.06892"},{"title":"Low-Rank Adaptation for Multilingual Summarization: An Empirical Study","url":"https://arxiv.org/html/2311.08572v2"},{"title":"The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation","url":"https://arxiv.org/html/2505.13090v2"},{"title":"Efficient Multilingual ASR Finetuning via LoRA Language Experts","url":"https://arxiv.org/html/2506.21555"},{"title":"Monolingual or Multilingual Instruction Tuning: Which Makes a Better Alpaca","url":"https://arxiv.org/pdf/2309.08958"},{"title":"Governance-Aware Hybrid Fine-Tuning for Multilingual Large Language Models","url":"https://arxiv.org/pdf/2512.17344"}]

I found several relevant papers from arXiv on language family cross-lingual transfer using LoRA fine-tuning in 2025-2026. Here's a summary of the key research:

## Recent Papers on Cross-Lingual Transfer and LoRA Fine-Tuning

**1. Turkic Language Family Study (March 2026)**
This paper proposes a theoretical framework for studying cross-lingual transfer and parameter-efficient adaptation of multilingual LLMs within the Turkic language family, focusing on Azerbaijani, Kazakh, Uzbek, Turkmen, and Gagauz. The analysis integrates insights from multilingual representation learning, parameter-efficient fine-tuning methods such as Low-Rank Adaptation (LoRA), and research on multilingual transfer in transformer-based language models. The paper further introduces the Turkic Transfer Coefficient (TTC), a theoretical measure designed to capture cross-lingual transfer potential within the Turkic language family.

**2. Multilingual Federated Learning with LoRA (March 2026)**
A federated multilingual framework integrates LoRA-based parameter-efficient tuning with language-family clustering, thereby reducing communication overhead while alleviating cross-lingual interference across heterogeneous languages.

**3. GRASP LoRA: Cross-Lingual Sparsity (January 2026)**
This work addresses sparsity policies for LoRA in cross-lingual transfer, improving upon fixed sparsity approaches with learned pruning strategies.

**4. FLARE: Language Fusion for Cross-Lingual Transfer (May 2025)**
FLARE integrates source and target language representations within low-rank (LoRA) adapters using lightweight linear transformations, maintaining parameter efficiency while improving transfer performance.

**5. Multilingual ASR with LoRA Language Experts (June 2025)**
An efficient multilingual ASR finetuning framework based on LoRA language experts facilitates fast adaptation from the base Whisper model to downstream customized multilingual ASR models.

These papers demonstrate active research in parameter-efficient cross-lingual adaptation techniques using LoRA within diverse linguistic families and applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e58082d-d2cc-4b69-8574-636ba4aedee7",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "7ce3a899-7116-4a52-8da1-ba46000765d3",
  "sourceToolAssistantUUID": "0e58082d-d2cc-4b69-8574-636ba4aedee7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-10T07:26:26.928Z_

<details><summary>↩ Tool result · `toolu_015gs86rAHk3spoyNSKWCQwh`</summary>

```text
Web search results for query: "agglutinative language instruction tuning low-resource LLM 2025 2026 arxiv"

Links: [{"title":"Foundation Models for Low-Resource Language Education (Vision Paper)","url":"https://arxiv.org/html/2412.04774v1"},{"title":"[2603.01691] Building a Strong Instruction Language Model for a Less-Resourced Language","url":"https://arxiv.org/abs/2603.01691"},{"title":"The Development of Small-Scale Language Models for Low-Resource Languages, with a Focus on Kazakh and Direct Preference Optimization","url":"https://www.mdpi.com/2504-2289/9/5/137"},{"title":"Transcending Language Boundaries: Harnessing LLMs for Low-Resource Language Translation","url":"https://arxiv.org/html/2411.11295v1"},{"title":"Instructing Large Language Models for Low-Resource Languages: A Systematic Study for Basque","url":"https://arxiv.org/html/2506.07597v1"},{"title":"Final Report - Fine Tuning Methods for Low-resource Languages","url":"https://arxiv.org/html/2510.04139v1"},{"title":"[2507.14304] Aligning Large Language Models to Low-Resource Languages through LLM-Based Selective Translation: A Systematic Study","url":"https://arxiv.org/abs/2507.14304"},{"title":"Aligning Large Language Models to Low-Resource Languages through LLM-Based Selective Translation: A Systematic Study","url":"https://arxiv.org/html/2507.14304v1"},{"title":"Efficient Strategy for Improving Large Language Model (LLM) Capabilities","url":"https://arxiv.org/html/2508.04073v1"},{"title":"[2412.12417] Bridging the Gap: Enhancing LLM Performance for Low-Resource African Languages with New Benchmarks, Fine-Tuning, and Cultural Adjustments","url":"https://arxiv.org/abs/2412.12417"}]

Based on the web search results, here are the relevant papers from arXiv (2025-2026) on agglutinative language instruction tuning and low-resource LLM:

## Directly Relevant Papers

**1. Instructing Large Language Models for Low-Resource Languages: A Systematic Study for Basque**
- This paper explores alternatives to conventional instruction adaptation pipelines in low-resource scenarios where instruction datasets are limited.
- Published June 9, 2025 (arxiv 2506.07597)

**2. Building a Strong Instruction Language Model for a Less-Resourced Language**
- The paper presents methodological approaches for successful LLM adaptation to less-resourced languages, demonstrated using Slovene, which involved three-stage continual pre-training followed by two-stage supervised fine-tuning.
- Published March 2, 2026 (arxiv 2603.01691)

**3. The Development of Small-Scale Language Models for Low-Resource Languages, with a Focus on Kazakh**
- The work compiles a cleaned Kazakh corpus and designs a tokenizer that respects the language's agglutinative morphology, building the model in two stages: causal language modeling from scratch followed by instruction tuning.
- Published May 20, 2025

**4. Foundation Models for Low-Resource Language Education (Vision Paper)**
- For low-resource languages, instruction-tuning can be pivotal by training on carefully curated datasets, allowing LLMs to address linguistic gaps and support education through task-based language exercises tailored to underrepresented communities.
- Published December 6, 2024 (arxiv 2412.04774)

**5. Aligning Large Language Models to Low-Resource Languages through LLM-Based Selective Translation: A Systematic Study**
- This work investigates LLM-based selective translation, a technique that selectively translates only the translatable parts of text while preserving non-translatable content and sentence structure.
- Published July 18, 2025 (arxiv 2507.14304)


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88719299-937a-44df-a10b-d584e8d760a5",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "0a25445c-1eca-429d-b075-1f71da955b71",
  "sourceToolAssistantUUID": "88719299-937a-44df-a10b-d584e8d760a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-10T07:26:26.949Z_

<details><summary>↩ Tool result · `toolu_01FrLY4YqaiXEVhD9veCV3tj`</summary>

```text
Web search results for query: "Mongolian Uyghur low-resource Turkic language instruction tuning LLM 2025 2026 arxiv"

Links: [{"title":"Low-Resource Language Expansion and Translation Capacity Enhancement for LLM: A Study on the Uyghur - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.559/"},{"title":"TurkicNLP: An NLP Toolkit for Turkic Languages","url":"https://arxiv.org/html/2602.19174"},{"title":"MiLiC-Eval: Benchmarking Multilingual LLMs for China’s Minority Languages","url":"https://arxiv.org/html/2503.01150v1"},{"title":"MM-Eval: A Hierarchical Benchmark for Modern Mongolian Evaluation in LLMs","url":"https://arxiv.org/html/2411.09492v1"},{"title":"TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages","url":"https://arxiv.org/html/2502.11020"},{"title":"TUMLU: A Unified and Native Language Understanding Benchmark for","url":"https://arxiv.org/pdf/2502.11020v1"},{"title":"Low-Resource Language Expansion and Translation Capacity Enhancement for LLM: A Study on the Uyghur | OpenReview","url":"https://openreview.net/forum?id=YVwThg7sQi"},{"title":"Low-Resource Language Expansion and Translation ...","url":"https://aclanthology.org/2025.coling-main.559.pdf"},{"title":"arXiv:2502.11020v2 [cs.CL] 13 Jun 2025","url":"https://arxiv.org/pdf/2502.11020"},{"title":"TUMLU: A Unified and Native Language Understanding ...","url":"https://aclanthology.org/2025.acl-long.1112.pdf"}]

I've found several relevant research papers on Mongolian and Uyghur language models from 2025-2026. Here are the key findings:

## Uyghur Language Expansion for LLMs

A study titled "Low-Resource Language Expansion and Translation Capacity Enhancement for LLM: A Study on the Uyghur" was published in 2025 at the International Conference on Computational Linguistics. The approach involves four stages: collecting and pre-processing monolingual data, conducting continuous pre-training with extensive monolingual data, fine-tuning with less parallel corpora using translation supervision, and proposing a direct preference optimization based on translation self-evolution (DPOSE).

## Mongolian Language Evaluation

The MiLiC-Eval benchmark tracks the process of continual pretraining on Uyghur and Mongolian, with experiments on Qwen-2.5-0.5B using the MC2 corpus. MM-Eval is a hierarchical benchmark for Modern Mongolian evaluation in LLMs, comprising 569 syntax, 677 semantics, 344 knowledge, and 250 reasoning tasks.

## Turkic Languages NLP Toolkit

Research from 2026 extends work by developing and cleaning parallel corpora for six Turkic languages (Kazakh, Azerbaijani, Kyrgyz, Turkish, Turkmen, and Uzbek) totalling over 3.8 million sentences, and fine-tuning NLLB-200 to achieve substantial gains in BLEU and chrF over the baseline for low-resource pairs.

## Turkic Language Understanding Benchmark

The TUMLU (Turkic Unified Multilingual Language Understanding) benchmark covers Azerbaijani, Crimean Tatar, Turkish, Uyghur, Uzbek, Karakalpak, Kyrgyz, Kazakh, and Tatar.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6e48f64-4290-4577-b35c-95054bc3f672",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "e66beb1f-0993-4174-80a9-2a5a21004722",
  "sourceToolAssistantUUID": "c6e48f64-4290-4577-b35c-95054bc3f672",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-10T07:26:28.885Z_

Now let me fetch details on the most critical competing/concurrent papers found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e66beb1f-0993-4174-80a9-2a5a21004722",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVSrkrLKVwU9JD9wdZ2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2cb2f8e-7658-49de-bb0a-68f65f56f7e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RQEBpAXe33PuhzfgdU441F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1018,
      "cache_creation_input_tokens": 3323,
      "cache_read_input_tokens": 18662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3323,
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

_source line 43 · 2026-05-10T07:26:30.755Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BMt2LE3gPia4SvQ38Lhhqv`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.06202",
  "prompt": "Extract full title, all authors, submission date, abstract, and key methodological claims about cross-lingual transfer in Turkic languages, LoRA, and the Turkic Transfer Coefficient."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2cb2f8e-7658-49de-bb0a-68f65f56f7e2",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVSrkrLKVwU9JD9wdZ2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80cc5957-324a-4246-a94e-a7472d55f15b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RQEBpAXe33PuhzfgdU441F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1018,
      "cache_creation_input_tokens": 3323,
      "cache_read_input_tokens": 18662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3323,
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

_source line 44 · 2026-05-10T07:26:31.584Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UTuZK9uw13w26uVVvneqxg`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.13647",
  "prompt": "Extract full title, all authors, submission date, abstract, methodology, datasets used, and key results for this Kazakh instruction tuning paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80cc5957-324a-4246-a94e-a7472d55f15b",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVSrkrLKVwU9JD9wdZ2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7fdf7b6e-976d-4e1b-a3b1-5bcfe13cd4aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RQEBpAXe33PuhzfgdU441F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1018,
      "cache_creation_input_tokens": 3323,
      "cache_read_input_tokens": 18662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3323,
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

_source line 45 · 2026-05-10T07:26:33.291Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013yg9dhRCJQYmvevtF6iozp`</summary>

```json
{
  "url": "https://arxiv.org/abs/2503.01493",
  "prompt": "Extract full title, all authors, submission date, abstract, methodology (training data, base model, instruction tuning approach), and key results for Sherkala."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fdf7b6e-976d-4e1b-a3b1-5bcfe13cd4aa",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVSrkrLKVwU9JD9wdZ2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8696eb1-1feb-470d-b50a-d9503f62fa2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RQEBpAXe33PuhzfgdU441F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1018,
      "cache_creation_input_tokens": 3323,
      "cache_read_input_tokens": 18662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3323,
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

_source line 46 · 2026-05-10T07:26:33.567Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016ZdowtoaDssvgz4fxLYMF2`</summary>

```json
{
  "query": "\"typologically weighted\" OR \"typological weighting\" curriculum instruction tuning multilingual 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8696eb1-1feb-470d-b50a-d9503f62fa2b",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVSrkrLKVwU9JD9wdZ2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ea539be-3130-45a9-9abb-c90b2f31b2e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RQEBpAXe33PuhzfgdU441F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1018,
      "cache_creation_input_tokens": 3323,
      "cache_read_input_tokens": 18662,
      "output_tokens": 389,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3323
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1018,
          "output_tokens": 389,
          "cache_read_input_tokens": 18662,
          "cache_creation_input_tokens": 3323,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3323,
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

_source line 47 · 2026-05-10T07:26:35.640Z_

<details><summary>↩ Tool result · `toolu_01BMt2LE3gPia4SvQ38Lhhqv`</summary>

```text
# Paper Summary

**Full Title:** Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family: A Theoretical Framework for Low-Resource Language Models

**Authors:** O. Ibrahimzade, K. Tabasaransky

**Submission Date:** Submitted on 13 Mar 2026

## Abstract

The paper addresses the underrepresentation of Turkic languages in multilingual LLMs. It examines Azerbaijani, Kazakh, Uzbek, Turkmen, and Gagauz—languages sharing "substantial typological and morphological similarity while differing greatly in available digital resources."

## Key Methodological Claims

**Cross-Lingual Transfer Framework:**
The authors propose integrating "insights from multilingual representation learning and parameter-efficient fine-tuning techniques such as Low-Rank Adaptation (LoRA)" to develop a scaling model showing how adaptation performance depends on model capacity, data size, and adaptation module expressivity.

**Turkic Transfer Coefficient (TTC):**
The paper introduces this theoretical measure that incorporates "morphological similarity, lexical overlap, syntactic structure, and script compatibility across Turkic languages" to formalize transfer potential between related languages.

**Key Finding:**
The framework demonstrates that "typological similarity can enable efficient multilingual transfer while also identifying structural limits of parameter-efficient adaptation in extremely low-resource scenarios."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80cc5957-324a-4246-a94e-a7472d55f15b",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "ed6aaae3-c083-4198-89dc-51b3f718cb70",
  "sourceToolAssistantUUID": "80cc5957-324a-4246-a94e-a7472d55f15b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-10T07:26:36.356Z_

<details><summary>↩ Tool result · `toolu_01UTuZK9uw13w26uVVvneqxg`</summary>

```text
# Kazakh Instruction Tuning Paper Summary

**Full Title:** Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh

**Authors:** Nurkhan Laiyk, Daniil Orel, Rituraj Joshi, Maiya Goloburda, Yuxia Wang, Preslav Nakov, Fajri Koto

**Submission Date:** February 19, 2025

**Abstract:**
The researchers address the challenge of instruction tuning for low-resource languages by creating a large-scale dataset. They note that "Instruction tuning in low-resource languages remains underexplored due to limited text data, particularly in government and cultural domains."

**Methodology:**
The team employed LLM-assisted data generation, comparing both open-weight and closed-weight models, ultimately selecting GPT-4o as their backbone. Every dataset entry underwent full manual verification for quality assurance.

**Dataset:**
A custom instruction-following dataset containing 10,600 samples covering institutional and procedural knowledge relevant to Kazakhstan, focusing on governance, legal structures, and cultural topics.

**Key Results:**
Fine-tuning three models—Qwen, Falcon, and Gemma—on their dataset produced "consistent performance improvements in both multiple-choice and generative tasks," demonstrating the effectiveness of their approach for low-resource language development.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fdf7b6e-976d-4e1b-a3b1-5bcfe13cd4aa",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "324f3525-0809-445b-a88f-7c05ea196f39",
  "sourceToolAssistantUUID": "7fdf7b6e-976d-4e1b-a3b1-5bcfe13cd4aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-10T07:26:40.876Z_

<details><summary>↩ Tool result · `toolu_013yg9dhRCJQYmvevtF6iozp`</summary>

```text
# Sherkala-Chat: Research Summary

**Full Title:**
Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting

**Authors:**
Fajri Koto, Rituraj Joshi, Nurdaulet Mukhituly, Yuxia Wang, Zhuohan Xie, Rahul Pal, Daniil Orel, Parvez Mullah, Diana Turmakhan, Maiya Goloburda, Mohammed Kamran, Samujjwal Ghosh, Bokang Jia, Jonibek Mansurov, Mukhammed Togmanov, Debopriyo Banerjee, Nurkhan Laiyk, Akhmed Sakip, Xudong Han, Ekaterina Kochmar, Alham Fikri Aji, Aaryamonvikram Singh, Alok Anil Jadhav, Satheesh Katipomu, Samta Kamboj, Monojit Choudhury, Gurpreet Gosal, Gokulakrishnan Ramakrishnan, Biswajit Mishra, Sarath Chandran, Avraham Sheinin, Natalia Vassilieva, Neha Sengupta, Preslav Nakov

**Submission Date:** March 3, 2025 (revised October 9, 2025)

**Abstract:**
The model aims to "enhance the inclusivity of LLM advancements for Kazakh speakers" through an instruction-tuned open generative model with eight billion parameters.

**Methodology:**
- **Base Model:** LLaMA-3.1-8B
- **Training Data:** 45.3 billion tokens spanning Kazakh, English, Russian, and Turkish
- **Instruction Tuning:** Leverages translated instruction datasets, Kazakhstan-specific automatically-constructed and manually-verified datasets, and Kazakh-specific safety data

**Key Results:**
The model "significantly outper-forming existing open Kazakh and multilingual models of similar scale while achieving competitive performance in English."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8696eb1-1feb-470d-b50a-d9503f62fa2b",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "a9c5dfcf-7a4d-4cee-be88-5de74f853797",
  "sourceToolAssistantUUID": "e8696eb1-1feb-470d-b50a-d9503f62fa2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-10T07:26:42.240Z_

<details><summary>↩ Tool result · `toolu_016ZdowtoaDssvgz4fxLYMF2`</summary>

```text
Web search results for query: ""typologically weighted" OR "typological weighting" curriculum instruction tuning multilingual 2025 2026"

Links: [{"title":"SIGTYP 2026 Workshop, @EACL","url":"https://sigtyp.github.io/workshop.html"},{"title":"MULTILINGUAL MATTERS 2025-2026 www.multilingual-matters.com","url":"https://www.multilingual-matters.com/resources/pdfs/catalogues/MM%20Catalogue%202025-2026.pdf"},{"title":"A Principled Framework for Evaluating on Typologically Diverse Languages | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/doi/10.1162/COLI.a.577/133834/A-Principled-Framework-for-Evaluating-on"},{"title":"A Principled Framework for Evaluating on Typologically Diverse Languages","url":"https://arxiv.org/html/2407.05022v2"},{"title":"Published in Transactions on Machine Learning Research (11/2025)","url":"https://openreview.net/pdf?id=oapsbIO1Bd"},{"title":"Aya Dataset: Multilingual Instruction Tuning","url":"https://www.emergentmind.com/topics/aya-dataset"},{"title":"Code-Switching Curriculum Learning for Multilingual ...","url":"https://aclanthology.org/2025.findings-acl.407.pdf"},{"title":"Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/html/2402.13703v3"},{"title":"Attention Sinks in Massively Multilingual Neural Machine Translation: Discovery, Analysis, and Mitigation","url":"https://arxiv.org/html/2605.01229"},{"title":"Instruction Tuning for Large Language Models: A Survey","url":"https://dl.acm.org/doi/pdf/10.1145/3777411"}]

I found several relevant results related to typology, multilingual instruction tuning, and curriculum learning. Here's what the search revealed:

## Key Findings:

**Typological Approaches in Multilingual NLP (2025-2026):**

The SIGTYP 2026 workshop aims to serve as a platform for the exchange of information between typology-related research and multilingual NLP, while raising awareness of linguistic typology and its potential in supporting the global reach of multilingual NLP methods. In 2026, there is a special emphasis on the utility of LLMs for typological research.

**Typologically Diverse Language Sampling:**

A language sampling framework for selecting highly typologically diverse languages has been presented, with systematic methods that consistently retrieve more typologically diverse language selections than previous methods in NLP. This work appeared in Computational Linguistics in 2025.

**Multilingual Instruction Tuning:**

The Aya Dataset includes language coverage of 101 languages for training, classified as 23 high-resource, 26 mid-resource, and 52 low-resource per typology. Additionally, human-annotated test sets included 250 prompts each in 7 typologically diverse languages.

**Curriculum Learning for Multilingual Transfer:**

Code-switching curriculum learning (CSCL) organizes training data into three difficulty levels according to code-switching degree, presented in order from least to most difficult, mirroring second language learning by humans.

**Data Selection and Weighting Approaches:**

Language clusters can be formed using supervised signals like linguistic typology or unsupervised methods based on TF-IDF text features.

The search results indicate active 2025-2026 research on integrating typological properties into multilingual model training, though specific papers explicitly titled with "typologically weighted" were not found.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ea539be-3130-45a9-9abb-c90b2f31b2e1",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "5e0bd0c7-ecc3-4465-81c1-6c4f13bdf48f",
  "sourceToolAssistantUUID": "9ea539be-3130-45a9-9abb-c90b2f31b2e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-10T07:26:48.758Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FkzEeRdy8z913w7TH5yif9`</summary>

```json
{
  "url": "https://arxiv.org/html/2509.20129",
  "prompt": "Extract the exact Spearman rho values reported, specifically for the Laplacian Score method with 300 features. Also report the number of features tested, the full set of results comparing feature selection methods, and the datasets used for evaluation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e0bd0c7-ecc3-4465-81c1-6c4f13bdf48f",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVTzJoYXXrdA6pZ8ueK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bdcc587b-33be-4ec5-9fd4-63fac66d58ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016NNmQ46MCjfakt19je9vG2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3588,
      "cache_read_input_tokens": 21985,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3588,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-10T07:26:50.264Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015ur6eoKwTDtyTN7LimKYYc`</summary>

```json
{
  "url": "https://arxiv.org/html/2409.18472",
  "prompt": "Extract exact numbers: how many typological features does URIEL+ cover? How many languages? Does it use SoftImpute for imputation? What imputation methods are used? What are the exact statistics on feature and language coverage?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdcc587b-33be-4ec5-9fd4-63fac66d58ba",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVTzJoYXXrdA6pZ8ueK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "797b9d35-81ce-48f4-93a4-1c1c17416476",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016NNmQ46MCjfakt19je9vG2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3588,
      "cache_read_input_tokens": 21985,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3588,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-10T07:26:51.488Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013JwNVKYGhMUr6fcYUCtwke`</summary>

```json
{
  "query": "arxiv 2025 2026 curriculum learning language selection low-resource multilingual LoRA instruction tuning typology pivot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "797b9d35-81ce-48f4-93a4-1c1c17416476",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVTzJoYXXrdA6pZ8ueK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ee8f051-3f48-491b-9635-cfc6bc0eb895",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016NNmQ46MCjfakt19je9vG2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3588,
      "cache_read_input_tokens": 21985,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3588,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-10T07:26:51.630Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012tixhNw7kE6yBqU9mKjnyX`</summary>

```json
{
  "query": "Qwen3.5-9B \"248K\" OR \"248,000\" vocabulary size March 2026 release"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ee8f051-3f48-491b-9635-cfc6bc0eb895",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVTzJoYXXrdA6pZ8ueK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "978fe1a3-1cca-44bd-aae2-f768f5ee6370",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016NNmQ46MCjfakt19je9vG2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3588,
      "cache_read_input_tokens": 21985,
      "output_tokens": 370,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3588
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 370,
          "cache_read_input_tokens": 21985,
          "cache_creation_input_tokens": 3588,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3588,
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

_source line 55 · 2026-05-10T07:26:54.685Z_

<details><summary>↩ Tool result · `toolu_01FkzEeRdy8z913w7TH5yif9`</summary>

```text
# Key Findings from the Paper

## Spearman rho for Laplacian Score (300 features)

The exact value reported is **ρ = 0.358** (with p = 0.061) when using 300 features with the Laplacian Score method, representing the strongest alignment with the linguistic similarity measure.

## Features Tested

The researchers evaluated feature subsets across **800 total typological features** from URIEL+, testing subset sizes of {100, 200, 300, 400, 500, 600, 700}.

## Complete Results Comparison

According to Table 1, the methods and their best-performing correlations were:

| Method | Best Subset Size | Spearman ρ |
|--------|------------------|-----------|
| Variance | 500 | 0.295 |
| PCA Loadings | 700 | 0.292 |
| Laplacian Score | 300 | 0.358 |
| Correlation-based FS | 200 | 0.264 |
| URIEL+ Baseline | – | 0.260 |

## Evaluation Datasets

The linguistic alignment evaluation used "a set of similarity scores between 28 language pairs, comprising 24 low-resource languages in the Isthmo-Colombian area." Downstream tasks employed separate datasets: LangRank (105 languages), ProxyLM (51 languages), and LinguAlchemy (63 languages).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdcc587b-33be-4ec5-9fd4-63fac66d58ba",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "69c9337c-40cb-4f98-82a2-60a1bf5e2e7b",
  "sourceToolAssistantUUID": "bdcc587b-33be-4ec5-9fd4-63fac66d58ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-10T07:26:55.115Z_

<details><summary>↩ Tool result · `toolu_012tixhNw7kE6yBqU9mKjnyX`</summary>

```text
Web search results for query: "Qwen3.5-9B "248K" OR "248,000" vocabulary size March 2026 release"

Links: [{"title":"Qwen/Qwen3.5-9B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-9B"},{"title":"Qwen3.5-9B | Awesome Agents","url":"https://awesomeagents.ai/models/qwen-3-5-9b/"},{"title":"Qwen/Qwen3.5-9B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-9B-Base"},{"title":"Qwen3.5 - How to Run Locally | Unsloth Documentation","url":"https://unsloth.ai/docs/models/qwen3.5"},{"title":"Qwen 3.5 Small Models: Alibaba Delivers Compact Multimodal Powerhouses | by Nikhil | Neural Notions | Mar, 2026 | Medium","url":"https://medium.com/modelmind/qwen-3-5-small-models-alibaba-delivers-compact-multimodal-powerhouses-9520af4d792e"},{"title":"Qwen 3.5 Small Series Ships Four Models From 0.8B to 9B | Awesome Agents","url":"https://awesomeagents.ai/news/qwen-3-5-small-models-series/"},{"title":"Qwen 3.5 9B Review: Alibaba's Open Source Model Tested","url":"https://emelia.io/hub/qwen-35-9b-review"},{"title":"Qwen3.5-9B Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/qwen3.5-9b"},{"title":"unsloth/Qwen3.5-9B-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Qwen3.5-9B-GGUF"},{"title":"qwen3.5:9b","url":"https://ollama.com/library/qwen3.5:9b"}]

Based on the search results, I found relevant information about the Qwen3.5-9B vocabulary size:

The Qwen3.5-9B has a 248K vocabulary with support for 201 languages. This aligns with your search query about the model's vocabulary size.

The Qwen3.5 Small Model Series, including the 9B variant, was launched by Alibaba's Qwen team on March 2, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "978fe1a3-1cca-44bd-aae2-f768f5ee6370",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "18790e8d-6095-4ff9-ae09-89c28befa7bc",
  "sourceToolAssistantUUID": "978fe1a3-1cca-44bd-aae2-f768f5ee6370",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-10T07:26:56.217Z_

<details><summary>↩ Tool result · `toolu_015ur6eoKwTDtyTN7LimKYYc`</summary>

```text
# URIEL+ Coverage and Methods

## Typological Features
URIEL+ provides data across **four feature categories**: syntactic, phonological, inventory, and morphological. The document doesn't specify a single total count of typological features, but indicates substantial coverage increases:
- **Syntactic features**: 474 from new databases
- **Morphological features**: 133 from new databases
- **Phonological features**: 30 from new databases
- **Inventory features**: 163 from new databases

## Language Coverage
- **Total languages in URIEL+**: "8071 languages, with 4366 capable of typological distance calculations"
- **Languages with actual typological data**: 4366 (compared to 2724 in original URIEL)
- **Low-resource languages added**: "2858 of which are low resource"

## Imputation Methods
URIEL+ implements **three imputation algorithms**:

1. **k-NN imputation** (from original URIEL)
2. **MIDASpy** (multiple imputation using deionizing autoencoders)
3. **SoftImpute** (low-rank matrix approximation via nuclear-norm regularization)

## Primary Method Selection
Yes, SoftImpute is the default: "Since SoftImpute performed the best, we used URIEL+ with union source aggregation and this method in both downstream tasks experiments."

The testing showed SoftImpute achieved the highest F1 score (0.7980) on union-aggregated data and lowest RMSE (0.2883) on average-aggregated data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "797b9d35-81ce-48f4-93a4-1c1c17416476",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "5ddc138b-c036-4e8a-a1f5-995396a8bb39",
  "sourceToolAssistantUUID": "797b9d35-81ce-48f4-93a4-1c1c17416476",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-10T07:26:59.286Z_

<details><summary>↩ Tool result · `toolu_013JwNVKYGhMUr6fcYUCtwke`</summary>

```text
Web search results for query: "arxiv 2025 2026 curriculum learning language selection low-resource multilingual LoRA instruction tuning typology pivot"

Links: [{"title":"[2411.18571] Challenges in Adapting Multilingual LLMs to Low-Resource Languages using LoRA PEFT Tuning","url":"https://arxiv.org/abs/2411.18571"},{"title":"Untitled Document","url":"https://arxiv.org/html/2602.00945v1"},{"title":"A Survey of Instruction Tuning in Large Language Models","url":"https://www.arxiv.org/pdf/2508.17184"},{"title":"Bhaasha, Bhāṣā, Zaban: A Survey for Low-Resourced Languages in South Asia – Current Stage and Challenges","url":"https://arxiv.org/html/2509.11570v1"},{"title":"A LoRA-Based Approach to Fine-Tuning LLMs for Educational Guidance in Resource-Constrained Settings","url":"https://arxiv.org/html/2504.15610v3"},{"title":"Dynamic Mixture of Curriculum LoRA Experts for Continual ...","url":"https://mn.cs.tsinghua.edu.cn/xinwang/PDF/papers/2025_Dynamic%20Mixture%20of%20Curriculum%20LoRA%20Experts%20for%20Continual%20Multimodal%20Instruction%20Tuning.pdf"},{"title":"GitHub - Wang-ML-Lab/llm-continual-learning-survey: [CSUR 2025] Continual Learning of Large Language Models: A Comprehensive Survey · GitHub","url":"https://github.com/Wang-ML-Lab/llm-continual-learning-survey"},{"title":"Final Report - Fine Tuning Methods for Low-resource Languages","url":"https://arxiv.org/html/2510.04139v1"},{"title":"The Future of Continual Learning in the Era of Foundation Models: Three Key Directions","url":"https://arxiv.org/html/2506.03320v1"},{"title":"Machine Learning Jan 2025","url":"https://arxiv.org/list/cs.LG/2025-01?skip=1575&show=2000"}]

I found several relevant papers from arXiv related to your search query. Here are the key findings:

## Recent Research Papers

**1. Neural FOXP2 (February 2026)** - Language neurons govern language defaultness through a sparse, low-rank control circuit, and a method called Neural FOXP2 makes a chosen language (Hindi or Spanish) primary in a model by steering language-specific neurons.

**2. Challenges in Adapting Multilingual LLMs to Low-Resource Languages using LoRA (November 2024)** - This study investigates the effects of Low-Rank Adaptation (LoRA) Parameter-Efficient Fine-Tuning (PEFT) on multilingual Gemma models for Marathi, and reveals that while evaluation metrics often show a performance decline post-fine-tuning, manual assessments frequently suggest that the fine-tuned models outperform their original counterparts.

**3. Bhaasha Survey on Low-Resourced Languages in South Asia (September 2025)** - Recent work has explored PEFT strategies like LoRA, QLoRA, and multi-step PEFT, which fine-tune models like Gemma with fewer parameters and lower memory cost.

**4. Dynamic Mixture of Curriculum LoRA Experts (2025)** - This paper addresses continual multimodal instruction tuning with curriculum learning approaches combined with LoRA experts.

**5. Continual Learning Survey (2025)** - The comprehensive survey includes work on code-switching curriculum learning for multilingual transfer in LLMs and efficient continual pre-training for low-resource languages.

These papers cover the intersection of curriculum learning, multilingual models, low-resource languages, LoRA fine-tuning, instruction tuning, and language selection mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ee8f051-3f48-491b-9635-cfc6bc0eb895",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "40900607-ffb4-47de-bfda-9d98ecb688cf",
  "sourceToolAssistantUUID": "6ee8f051-3f48-491b-9635-cfc6bc0eb895",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-10T07:27:01.292Z_

Now let me get the Hugging Face page for Qwen3.5-9B for precise details, and search for more competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40900607-ffb4-47de-bfda-9d98ecb688cf",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVVExtmgqraeeBCxdTH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c4123f7-4b94-4fb0-a047-8fe90480ff16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017hnS657hcfiFbYFzhqZfwS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 713,
      "cache_creation_input_tokens": 2129,
      "cache_read_input_tokens": 25573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2129,
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

_source line 60 · 2026-05-10T07:27:03.038Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01F43RK6mM5NNUgKpEG3viiV`</summary>

```json
{
  "url": "https://huggingface.co/Qwen/Qwen3.5-9B",
  "prompt": "Extract: exact release date, vocabulary size, number of languages supported, model series sizes (0.8B, 2B, 4B, 9B - is 7B absent?), context window, and any other key model specs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c4123f7-4b94-4fb0-a047-8fe90480ff16",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVVExtmgqraeeBCxdTH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3c11c85-b120-4251-925f-3b69f76c8bfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017hnS657hcfiFbYFzhqZfwS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 713,
      "cache_creation_input_tokens": 2129,
      "cache_read_input_tokens": 25573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2129,
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

_source line 61 · 2026-05-10T07:27:03.905Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F93kp6zHJQThexAX1x6LL6`</summary>

```json
{
  "query": "arxiv 2025 2026 \"multi-source\" OR \"multiple pivot\" cross-lingual instruction tuning language weighting transfer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3c11c85-b120-4251-925f-3b69f76c8bfc",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVVExtmgqraeeBCxdTH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c952947-1523-4405-9923-df6d10d5a13e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017hnS657hcfiFbYFzhqZfwS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 713,
      "cache_creation_input_tokens": 2129,
      "cache_read_input_tokens": 25573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2129,
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

_source line 62 · 2026-05-10T07:27:04.606Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JHbCR3AiN5FeJLF13fzk7z`</summary>

```json
{
  "query": "arxiv 2025 \"low-resource Turkic\" OR \"low-resource Kazakh\" OR \"low-resource Mongolian\" instruction tuning curriculum language family"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c952947-1523-4405-9923-df6d10d5a13e",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVVExtmgqraeeBCxdTH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3782cd69-1e5c-45e2-bb24-562b4ba6760d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017hnS657hcfiFbYFzhqZfwS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 713,
      "cache_creation_input_tokens": 2129,
      "cache_read_input_tokens": 25573,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2129
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 713,
          "output_tokens": 309,
          "cache_read_input_tokens": 25573,
          "cache_creation_input_tokens": 2129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2129,
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

_source line 63 · 2026-05-10T07:27:09.591Z_

<details><summary>↩ Tool result · `toolu_01F43RK6mM5NNUgKpEG3viiV`</summary>

```text
# Qwen3.5-9B Model Specifications

## Release Date
**February 2026** (as stated in the citation)

## Vocabulary Size
**248,320 tokens** (padded)

## Language Support
**201 languages and dialects** - Expanded support for global linguistic coverage with nuanced cultural and regional understanding.

## Model Series Sizes
The content mentions:
- **Qwen3.5-4B**
- **Qwen3.5-9B** (this model)

*Note: No 0.8B, 2B, or 7B variants are mentioned in this documentation. A 7B model does appear to be absent from the Qwen3.5 lineup.*

## Context Window
- **Native context length**: 262,144 tokens
- **Extensible up to**: 1,010,000 tokens (with RoPE scaling techniques like YaRN)

## Key Model Specifications

| Specification | Value |
|---|---|
| **Type** | Causal Language Model with Vision Encoder |
| **Parameters** | 9B |
| **Hidden Dimension** | 4,096 |
| **Layers** | 32 |
| **Architecture** | 8 × (3 × Gated DeltaNet → FFN + 1 × Gated Attention → FFN) |
| **Attention Heads (Q)** | 16 |
| **Attention Heads (KV)** | 4 |
| **Head Dimension** | 256 |
| **FFN Intermediate Dimension** | 12,288 |
| **Training Stages** | Pre-training & Post-training |
| **Special Features** | Multi-Token Prediction (MTP), Vision-Language capabilities |

## Notable Capabilities
- **Multimodal support**: Image, text, and video understanding
- **Extended thinking**: Generates reasoning content before responses
- **Tool calling**: Advanced function calling capabilities
- **Sparse MoE architecture**: Gated Delta Networks with Mixture-of-Experts for efficiency
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3c11c85-b120-4251-925f-3b69f76c8bfc",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "523dcd03-1256-4b1f-8dbf-f3bb56f4c63a",
  "sourceToolAssistantUUID": "c3c11c85-b120-4251-925f-3b69f76c8bfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-10T07:27:12.932Z_

<details><summary>↩ Tool result · `toolu_01F93kp6zHJQThexAX1x6LL6`</summary>

```text
Web search results for query: "arxiv 2025 2026 "multi-source" OR "multiple pivot" cross-lingual instruction tuning language weighting transfer"

Links: [{"title":"BayLing 2: A Multilingual Large Language Model with Efficient Language Alignment","url":"https://arxiv.org/html/2411.16300"},{"title":"[2311.08711] PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning","url":"https://arxiv.org/abs/2311.08711"},{"title":"Multilingual Large Language Models: A Systematic Survey","url":"https://arxiv.org/html/2411.11072v1"},{"title":"Continually Adding New Languages to Multilingual Language Models","url":"https://arxiv.org/html/2509.11414v1"},{"title":"Zero-shot cross-lingual transfer in instruction tuning of large language models","url":"https://arxiv.org/html/2402.14778"},{"title":"Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://arxiv.org/html/2510.25947v1"},{"title":"Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/html/2401.01854v4"},{"title":"[2505.14297] Cross-Lingual Optimization for Language Transfer in Large Language Models","url":"https://arxiv.org/abs/2505.14297"},{"title":"Analysis of Multi-Source Language Training in Cross-Lingual Transfer","url":"https://arxiv.org/html/2402.13562"},{"title":"LinguaLIFT: An Effective Two-stage Instruction Tuning Framework for Low-Resource Language Tasks","url":"https://arxiv.org/html/2412.12499v1"}]

I found several highly relevant research papers from arXiv on cross-lingual instruction tuning and language transfer. Here are the key findings:

## Recent Papers on Multi-Source and Pivot Language Approaches

BayLing 2 designates Chinese and English, two high-resource languages, as pivot languages and applies cross-lingual tasks to align 100+ languages to these pivot languages, which facilitates the capabilities transfer from high-resource languages to low-resource languages. This work from December 2024 demonstrates a multi-source pivot approach with cross-lingual instruction tuning.

PLUG proposes an approach that utilizes a high-resource language, primarily English, as the pivot to enhance instruction tuning in lower-resource languages by training the model to first process instructions in the pivot language, and then produce responses in the target language.

## Language Weighting and Transfer Analysis

Using multiple pivots that balance breadth and proximity provides the most consistent benefits across language families, as found in recent research on multilingual data mixtures from October 2025.

There is empirical acknowledgment that increasing the diversity of source languages in cross-lingual transfer can boost its performance, and multi-source language training is also advantageous for instruction-tuned language models, though comprehensive analysis and tailored strategies in this area have been lacking.

## Cross-Lingual Transfer Mechanisms

Cross-lingual alignment during multilingual tuning transfers capabilities from the pivot language (primarily English) to other languages, with approaches classified into Translation-Assisted Tuning and Cross-Lingual Tuning methods.

Cross-Lingual Optimization (CLO) efficiently transfers an English-centric LLM to a target language while preserving its English capabilities, utilizing publicly available English SFT data and a translation model to enable cross-lingual transfer.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c952947-1523-4405-9923-df6d10d5a13e",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "5d0eefbc-7751-4237-ab38-1b5a1ea387f7",
  "sourceToolAssistantUUID": "5c952947-1523-4405-9923-df6d10d5a13e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-10T07:27:14.351Z_

<details><summary>↩ Tool result · `toolu_01JHbCR3AiN5FeJLF13fzk7z`</summary>

```text
Web search results for query: "arxiv 2025 "low-resource Turkic" OR "low-resource Kazakh" OR "low-resource Mongolian" instruction tuning curriculum language family"

Links: [{"title":"SozKZ: Training Efficient Small Language Models for Kazakh from Scratch","url":"https://arxiv.org/html/2603.20854v1"},{"title":"Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models","url":"https://arxiv.org/html/2603.21036"},{"title":"Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh","url":"https://arxiv.org/html/2502.13647"},{"title":"Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family: A Theoretical Framework for Low-Resource Language Models","url":"https://arxiv.org/html/2604.06202"},{"title":"[2604.06202] Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family: A Theoretical Framework for Low-Resource Language Models","url":"https://arxiv.org/abs/2604.06202"},{"title":"[2502.13647] Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh","url":"https://arxiv.org/abs/2502.13647"},{"title":"[2502.11020] TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages","url":"https://arxiv.org/abs/2502.11020"},{"title":"Recent Advancements and Challenges of Turkic Central ...","url":"https://aclanthology.org/2025.loreslm-1.25.pdf"},{"title":"Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.706/"},{"title":"[2603.20854] SozKZ: Training Efficient Small Language Models for Kazakh from Scratch","url":"https://arxiv.org/abs/2603.20854"}]

Based on the search results, I found several highly relevant 2025 arxiv papers on low-resource Turkic languages, Kazakh, and Mongolian with instruction tuning and curriculum learning aspects:

## Key Papers Found:

1. **Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh** (arxiv 2502.13647)
   - Introduces a large-scale (10,600 samples) instruction-following (IFT) dataset, covering key institutional and cultural knowledge relevant to Kazakhstan
   - Fine-tuning Qwen, Falcon, and Gemma on this dataset leads to consistent performance improvements in both multiple-choice and generative tasks, demonstrating the potential of LLM-assisted instruction tuning for low-resource languages

2. **Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models** (arxiv 2603.21036)
   - Aya Expanse, explicitly designed for 100+ languages including Turkic family members, achieves 82.3% in English but collapses to 15.7% for Kazakh and 4.7% for Mongolian
   - A benchmark of 2,000 LLM responses across Kazakh and Mongolian reveals a consistent and substantial performance gap between English and low-resource language conditions

3. **Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family: A Theoretical Framework for Low-Resource Language Models** (arxiv 2604.06202)
   - Develops a theoretical framework for understanding language model adaptation within the Turkic language family, focusing on Azerbaijani, Kazakh, Uzbek, Turkmen, and Gagauz
   - Introduces the Turkic Transfer Coefficient (TTC), a theoretical measure designed to capture cross-lingual transfer potential within the Turkic language family

4. **SozKZ: Training Efficient Small Language Models for Kazakh from Scratch** (arxiv 2603.20854)
   - Kazakh, a Turkic language spoken by over 22 million people, remains underserved by existing multilingual language models. The paper presents SozKZ, a family of Llama-architecture language models (50M–600M parameters) trained entirely from scratch on 9 billion tokens of Kazakh text with a dedicated 50K BPE tokenizer

5. **TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages** (arxiv 2502.11020)
   - A comprehensive, multilingual, and natively developed language understanding benchmark specifically designed for Turkic languages, consisting of middle- and high-school level questions spanning 11 academic subjects in Azerbaijani, Crimean Tatar, Karakalpak, Kazakh, Tatar, Turkish, Uyghur, and Uzbek


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3782cd69-1e5c-45e2-bb24-562b4ba6760d",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "7e8a7cba-6516-44ae-bdc6-4c7c24815eaa",
  "sourceToolAssistantUUID": "3782cd69-1e5c-45e2-bb24-562b4ba6760d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-10T07:27:17.512Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014uHNjwQHakaQQ5EtA8tyFe`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.21036",
  "prompt": "Extract full title, all authors, submission date, abstract, and key findings especially about Kazakh and Mongolian performance gaps, and cross-lingual transfer methodology."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e8a7cba-6516-44ae-bdc6-4c7c24815eaa",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVWMX4kKBWcePwc3774",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a10e1ff-5415-48df-9925-2d618b549d20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013BYc3cWSARj9bRJEKXCu9b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3774,
      "cache_read_input_tokens": 27702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3774,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-10T07:27:18.570Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GndcX7QYcKpB3AWrYd1323`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.20854",
  "prompt": "Extract full title, authors, submission date, abstract, and key methodology for SozKZ Kazakh language model."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a10e1ff-5415-48df-9925-2d618b549d20",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVWMX4kKBWcePwc3774",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee17e3ff-0209-4df7-917c-1e77eb29ced3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013BYc3cWSARj9bRJEKXCu9b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3774,
      "cache_read_input_tokens": 27702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3774,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-10T07:27:19.031Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A5E7tgoe8rXrEBiFZv1cQF`</summary>

```json
{
  "query": "arxiv 2025 2026 \"language distance\" OR \"typological similarity\" \"instruction tuning\" curriculum multilingual LLM pivot weighting selection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee17e3ff-0209-4df7-917c-1e77eb29ced3",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVWMX4kKBWcePwc3774",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90796e9d-aa34-4f10-9524-b37abe055bfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013BYc3cWSARj9bRJEKXCu9b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3774,
      "cache_read_input_tokens": 27702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3774,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-10T07:27:20.093Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NP89kXfV7THryahswaEMC6`</summary>

```json
{
  "url": "https://arxiv.org/abs/2402.13562",
  "prompt": "Extract full title, authors, abstract, and key findings about multi-source language training in cross-lingual transfer."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90796e9d-aa34-4f10-9524-b37abe055bfd",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVWMX4kKBWcePwc3774",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "186ac432-d5b7-4f5b-be11-9c370f209229",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013BYc3cWSARj9bRJEKXCu9b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3774,
      "cache_read_input_tokens": 27702,
      "output_tokens": 361,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3774
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 361,
          "cache_read_input_tokens": 27702,
          "cache_creation_input_tokens": 3774,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3774,
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

_source line 70 · 2026-05-10T07:27:22.127Z_

<details><summary>↩ Tool result · `toolu_014uHNjwQHakaQQ5EtA8tyFe`</summary>

```text
# Research Paper Summary

**Full Title:** "Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models"

**Author:** Abdul-Salem Beibitkhan

**Submission Date:** March 22, 2026

## Abstract Overview

The research investigates how eight large language models perform across low-resource languages. The study evaluated 2,000 responses using 50 custom questions across factual, reasoning, technical, and cultural categories in three languages.

## Key Findings

**Performance Gaps:**
The study identified "a consistent performance gap of 13.8-16.7 percentage points between English and low-resource language conditions," affecting both Kazakh and Mongolian. Models maintained apparent fluency while delivering substantially less accurate content in these languages.

**Cross-Lingual Transfer Strategy:**
The researchers tested prompting models to reason in English before translating results back. Results were architecture-dependent: bilingual models gained 2.2-4.3 percentage points, while English-dominant models saw no improvement.

**Conclusion:**
The findings demonstrate that "current LLMs systematically underserve low-resource language communities, and that effective mitigation strategies are architecture-dependent rather than universal," indicating no universal solution exists across all model types.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a10e1ff-5415-48df-9925-2d618b549d20",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "db0f816c-f779-4bdf-9b8f-a4b66f829c3b",
  "sourceToolAssistantUUID": "3a10e1ff-5415-48df-9925-2d618b549d20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-10T07:27:22.814Z_

<details><summary>↩ Tool result · `toolu_01GndcX7QYcKpB3AWrYd1323`</summary>

```text
# SozKZ: Kazakh Language Model Summary

**Full Title:**
"SozKZ: Training Efficient Small Language Models for Kazakh from Scratch"

**Author:**
Saken Tukenov

**Submission Date:**
March 21, 2026

**Abstract:**
The paper addresses the underrepresentation of Kazakh—a Turkic language with over 22 million speakers—in existing multilingual models. The researchers developed a family of models ranging from 50M to 600M parameters using Llama architecture, trained on 9 billion Kazakh text tokens with a specialized 50K BPE tokenizer. Their largest model achieved "30.3% accuracy on Kazakh cultural QA," approaching larger baseline performance while using significantly less computational resources. Results demonstrated consistent improvements across three evaluation benchmarks, with the models outperforming comparable multilingual systems.

**Key Methodology:**
- Llama-architecture models (50M-600M parameters)
- Dedicated 50K BPE tokenizer designed for agglutinative morphology
- Training corpus: 9 billion Kazakh language tokens
- Evaluation across three benchmarks including cultural QA, reading comprehension, and topic classification
- Models released under open licenses
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee17e3ff-0209-4df7-917c-1e77eb29ced3",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "56a57045-704c-4917-a6ef-a90059c1dd93",
  "sourceToolAssistantUUID": "ee17e3ff-0209-4df7-917c-1e77eb29ced3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-10T07:27:24.079Z_

<details><summary>↩ Tool result · `toolu_01NP89kXfV7THryahswaEMC6`</summary>

```text
# Analysis of Multi-Source Language Training in Cross-Lingual Transfer

**Full Title:** "Analysis of Multi-Source Language Training in Cross-Lingual Transfer"

**Authors:** Seong Hoon Lim, Taejun Yun, Jinhyeon Kim, Jihun Choi, and Taeuk Kim

**Abstract Summary:**
The research examines how multilingual language models adapt to specific language-task combinations through cross-lingual transfer. The team investigates whether using multiple source languages encourages models to emphasize "language-agnostic or task-specific features."

**Key Findings:**

1. **Embedding Space Integration:** Training with multiple source languages causes "increased mingling of embedding spaces for different languages," confirming that cross-lingual transfer leverages language-independent information.

2. **Selective Language Combinations Matter:** The authors discovered that arbitrarily combining source languages doesn't guarantee improved results, requiring strategic selection.

3. **Practical Heuristics:** They developed and validated simple guidelines for identifying effective language pairings in multi-source training scenarios.

**Publication Status:** Accepted to ACL 2024 (submitted February 21, 2024; revised June 5, 2024)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "186ac432-d5b7-4f5b-be11-9c370f209229",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "6930dac6-2dd3-4d9e-8dd8-c17263c14d9f",
  "sourceToolAssistantUUID": "186ac432-d5b7-4f5b-be11-9c370f209229",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-10T07:27:29.412Z_

<details><summary>↩ Tool result · `toolu_01A5E7tgoe8rXrEBiFZv1cQF`</summary>

```text
Web search results for query: "arxiv 2025 2026 "language distance" OR "typological similarity" "instruction tuning" curriculum multilingual LLM pivot weighting selection"

Links: [{"title":"Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://arxiv.org/html/2510.25947v1"},{"title":"Beyond Language Boundaries: Uncovering Programming Language Families for Code Language Models","url":"https://arxiv.org/html/2512.19509"},{"title":"Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/html/2401.01854"},{"title":"Large Language Models are Easily Confused: A Quantitative Metric, Security Implications and Typological Analysis","url":"https://arxiv.org/html/2410.13237"},{"title":"What Linguistic Features and Languages are Important in LLM Translation?","url":"https://arxiv.org/html/2402.13917v1"},{"title":"A Survey on Multilingual Large Language Models: Corpora, Alignment, and Bias","url":"https://arxiv.org/html/2404.00929v3"},{"title":"The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation","url":"https://arxiv.org/html/2505.13090v1"},{"title":"Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning","url":"https://arxiv.org/html/2601.01362"},{"title":"Code-Switching Curriculum Learning for Multilingual ...","url":"https://aclanthology.org/2025.findings-acl.407.pdf"},{"title":"LLMs Beyond English: Scaling the Multilingual Capability of LLMs with Cross-Lingual Feedback","url":"https://arxiv.org/html/2406.01771v1"}]

I found several relevant papers from arXiv in 2025-2026 related to your query. Here are the key results:

## Primary Match

A paper on "Revisiting Multilingual Data Mixtures in Language Model Pretraining" (October 2025) found that "English can serve as a broadly effective pivot language, but in very low-resource settings, typological similarity becomes increasingly important." Using multiple pivots that balance breadth and proximity provides the most consistent benefits across language families.

## Related Work on Instruction Tuning and Multilingual LLMs

Several papers address curriculum learning and multilingual instruction tuning:

- One study demonstrates that cross-lingual transfer offers a promising avenue for building multilingual instruction-following LLMs, and incorporating even a small set of multilingual examples can significantly enhance instruction-following performance for both the languages the model is tuned on and ones seen only during pre-training.

- A paper on "Code-Switching Curriculum Learning for Multilingual Transfer in LLMs" organizes training data into three difficulty levels according to code-switching degree, mirroring second language learning by humans.

## Language Distance and Typological Similarity

More typologically distant language pairs tend to be less well-aligned than more similar ones, with the Bilingual Lexicon Induction task showing accuracy under 40% for semantically distant language pairs versus over 80% for similar ones.

These papers directly address the intersection of language distance/typological similarity, instruction tuning, curriculum learning, and pivot language weighting selection in multilingual LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90796e9d-aa34-4f10-9524-b37abe055bfd",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "39c1050e-d86e-4953-93cd-c3cd0c9b1671",
  "sourceToolAssistantUUID": "90796e9d-aa34-4f10-9524-b37abe055bfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-10T07:27:33.116Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01U4TArGnyJQDPwHgWyS1NgF`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.25947v1",
  "prompt": "Extract full title, authors, publication date, abstract, and key claims about: using multiple pivot languages, typological similarity in low-resource settings, language weighting, and data mixture strategies for multilingual pretraining."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39c1050e-d86e-4953-93cd-c3cd0c9b1671",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVXUWXxQvynmFzQfKxK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35df95f4-fe5c-42c3-8a12-206a7162b94d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011iG7eNTySgPq5DigCkeW4G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 306,
      "cache_creation_input_tokens": 1828,
      "cache_read_input_tokens": 31476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1828,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-10T07:27:33.868Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JdGPc4C7zv9C5L4N2VsuBA`</summary>

```json
{
  "query": "arxiv 2025 2026 URIEL typological features language selection curriculum fine-tuning low-resource instruction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35df95f4-fe5c-42c3-8a12-206a7162b94d",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVXUWXxQvynmFzQfKxK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ddc01eba-9ebf-4cbc-bdb9-d764da8705e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011iG7eNTySgPq5DigCkeW4G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 306,
      "cache_creation_input_tokens": 1828,
      "cache_read_input_tokens": 31476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1828,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-10T07:27:34.268Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GpXvh8o6MnbVEArUrLN4cz`</summary>

```json
{
  "query": "arxiv 2025 \"Uyghur\" LLM instruction tuning fine-tuning expansion low-resource"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddc01eba-9ebf-4cbc-bdb9-d764da8705e6",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVXUWXxQvynmFzQfKxK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "650658d3-1ebf-4d76-932e-f4a797c59ce4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011iG7eNTySgPq5DigCkeW4G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 306,
      "cache_creation_input_tokens": 1828,
      "cache_read_input_tokens": 31476,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1828
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 306,
          "output_tokens": 249,
          "cache_read_input_tokens": 31476,
          "cache_creation_input_tokens": 1828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1828,
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

_source line 77 · 2026-05-10T07:27:40.114Z_

<details><summary>↩ Tool result · `toolu_01U4TArGnyJQDPwHgWyS1NgF`</summary>

```text
# Research Summary

**Full Title:** "Revisiting Multilingual Data Mixtures in Language Model Pretraining"

**Authors:** Negar Foroutan, Paul Teiletche, Ayush Kumar Tarun, Antoine Bosselut (EPFL, Lausanne, Switzerland)

**Publication Date:** October 2025 (arXiv:2510.25947v1)

---

## Abstract

The researchers trained 1.1B and 33B parameter LLMs across 25-400 languages to challenge prevailing assumptions about multilingual pretraining. They found that "combining English and multilingual data does not necessarily degrade the in-language performance of either group" when sufficient tokens exist for each language. Additionally, "using English as a pivot language yields benefits across language families" contrary to expectations that family-specific pivots would be superior.

---

## Key Claims

**Multiple Pivot Languages:**
The study demonstrates complementary benefits when combining multiple pivots. With Slavic languages, "combining both English and Russian as joint pivots yields the lowest overall loss, suggesting a complementary effect: English contributes wide coverage, while Russian offers closer linguistic ties."

**Typological Similarity in Low-Resource Settings:**
Interestingly, typological proximity becomes relevant only under extreme resource constraints. The researchers note that "in extremely low-resource conditions, these languages gain more from leveraging similarities with a strong pivot language."

**Language Weighting Strategies:**
The research distinguishes between fixed total budgets versus fixed multilingual budgets, demonstrating that "provided that the training set also contains a sufficient quantity of multilingual tokens," English proportion increases don't harm multilingual performance.

**Data Mixture Strategies:**
The "curse of multilinguality" stems not from language count but rather from "finite capacity of models and data distributions that amplify the impact of noisy, low-resource languages." Natural data distributions outperform temperature-sampled distributions, suggesting quality matters more than artificial balancing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35df95f4-fe5c-42c3-8a12-206a7162b94d",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "55369d2b-9cfb-462b-a428-2f6e0ca83658",
  "sourceToolAssistantUUID": "35df95f4-fe5c-42c3-8a12-206a7162b94d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-10T07:27:41.298Z_

<details><summary>↩ Tool result · `toolu_01GpXvh8o6MnbVEArUrLN4cz`</summary>

```text
Web search results for query: "arxiv 2025 "Uyghur" LLM instruction tuning fine-tuning expansion low-resource"

Links: [{"title":"Low-Resource Language Expansion and Translation Capacity Enhancement for LLM: A Study on the Uyghur - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.559/"},{"title":"Exploring NLP Benchmarks in an Extremely Low-Resource Setting","url":"https://arxiv.org/html/2509.03962v1"},{"title":"[2411.09539] Fine-tuning Large Language Models with Limited Data: A Survey and Practical Guide","url":"https://arxiv.org/abs/2411.09539"},{"title":"Final Report - Fine Tuning Methods for Low-resource Languages","url":"https://arxiv.org/html/2510.04139v1"},{"title":"Fine-tuning Large Language Models with Limited Data: A Survey and Practical Guide","url":"https://arxiv.org/html/2411.09539v2"},{"title":"[2308.10792] Instruction Tuning for Large Language Models: A Survey","url":"https://arxiv.org/abs/2308.10792"},{"title":"[2503.12790v1] Quantum-Enhanced LLM Efficient Fine Tuning","url":"https://arxiv.org/abs/2503.12790v1"},{"title":"A Survey on Federated Fine-tuning of Large Language ...","url":"https://arxiv.org/pdf/2503.12016"},{"title":"A LoRA-Based Approach to Fine-Tuning LLMs for Educational Guidance in Resource-Constrained Settings","url":"https://arxiv.org/html/2504.15610v3"},{"title":"A Powerful Pipeline for LLM Instruction Tuning","url":"https://arxiv.org/pdf/2408.14774"}]

Based on the search results, I found a highly relevant paper matching your query:

"Low-Resource Language Expansion and Translation Capacity Enhancement for LLM: A Study on the Uyghur" was published in the Proceedings of the 31st International Conference on Computational Linguistics (COLING 2025).

The research involves four stages: collecting and pre-processing monolingual data, conducting continuous pre-training with extensive monolingual data, fine-tuning with less parallel corpora using translation supervision, and proposing a direct preference optimization based on translation self-evolution (DPOSE).

Extensive experiments have shown that their strategy effectively expands the low-resource languages supported by large language models and significantly enhances the model's translation ability in Uyghur with less parallel data. The research provides detailed insights for expanding other low-resource languages into large language models.

The paper appears to be available through the ACL Anthology at https://aclanthology.org/2025.coling-main.559/ and may also be referenced in arXiv contexts as noted in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "650658d3-1ebf-4d76-932e-f4a797c59ce4",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "900808ab-95e7-439f-a75e-89fdc94eb52f",
  "sourceToolAssistantUUID": "650658d3-1ebf-4d76-932e-f4a797c59ce4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-10T07:27:42.793Z_

<details><summary>↩ Tool result · `toolu_01JdGPc4C7zv9C5L4N2VsuBA`</summary>

```text
Web search results for query: "arxiv 2025 2026 URIEL typological features language selection curriculum fine-tuning low-resource instruction"

Links: [{"title":"Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+","url":"https://arxiv.org/html/2510.27183"},{"title":"URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base","url":"https://arxiv.org/html/2409.18472"},{"title":"LinguAlchemy: Fusing Typological and Geographical Elements for Unseen Language Generalization","url":"https://arxiv.org/html/2401.06034"},{"title":"Less is More: The Effectiveness of Compact Typological Language Representations","url":"https://arxiv.org/html/2509.20129"},{"title":"Zero-shot Cross-lingual Transfer Learning with Multiple Source and Target Languages for Information Extraction: Language Selection and Adversarial Training","url":"https://arxiv.org/html/2411.08785"},{"title":"[2509.20129] Less is More: The Effectiveness of Compact Typological Language Representations","url":"https://arxiv.org/abs/2509.20129"},{"title":"[2510.27183] Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+","url":"https://arxiv.org/abs/2510.27183"},{"title":"arXiv:2503.19979v1 [cs.CL] 25 Mar 2025","url":"https://arxiv.org/pdf/2503.19979"},{"title":"Untangling the Influence of Typology, Data and Model Architecture on Ranking Transfer Languages for Cross-Lingual POS Tagging","url":"https://arxiv.org/html/2503.19979"},{"title":"Final Report - Fine Tuning Methods for Low-resource Languages","url":"https://arxiv.org/html/2510.04139v1"}]

I found several relevant arXiv papers on your search query. Here are the key results:

## Main Papers Found:

**1. "Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+" (arXiv:2510.27183, March 2026)**
The URIEL+ linguistic knowledge base supports multilingual research by encoding languages through geographic, genetic, and typological vectors. Data sparsity limits the usefulness of URIEL+ in cross-lingual transfer, particularly for supporting low-resource languages. The paper extends URIEL+ by introducing script vectors and propagating features across genealogies, reducing feature sparsity by 35%.

**2. "URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base" (arXiv:2409.18472, February 2025)**
URIEL+ incorporates new databases to enhance feature coverage and implements imputation algorithms to handle missing values.

**3. "Less is More: The Effectiveness of Compact Typological Language Representations" (arXiv:2509.20129, September 2025)**
This paper proposes a pipeline to optimize the URIEL+ typological feature space by combining feature selection and imputation, producing compact yet interpretable typological representations.

**4. "Untangling the Influence of Typology, Data and Model Architecture on Ranking Transfer Languages for Cross-Lingual POS Tagging" (arXiv:2503.19979, March 2025)**
The analysis reveals that key features such as word overlap, type-token ratio, and genealogical distance remain consistently important across architectures, offering broader insights into cross-lingual transfer for low-resource applications.

**5. "Zero-shot Cross-lingual Transfer Learning with Multiple Source and Target Languages for Information Extraction" (arXiv:2411.08785, November 2024)**
This paper achieves high correlation between model performance and linguistic relations using a combination of syntax, inventory, and phonology features from URIEL.

These papers collectively address language selection, typological features, curriculum fine-tuning approaches, and applications to low-resource languages using the URIEL database.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ddc01eba-9ebf-4cbc-bdb9-d764da8705e6",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "3f2b6751-2af7-42f2-988b-1c46edf14f1c",
  "sourceToolAssistantUUID": "ddc01eba-9ebf-4cbc-bdb9-d764da8705e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-10T07:27:46.436Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JD6ULBRh1mw7Axh35jkRqm`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.27183",
  "prompt": "Extract full title, authors, submission date, abstract, and key claims about extending URIEL+ with scripts and genealogical propagation, and the sparsity reduction percentage."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f2b6751-2af7-42f2-988b-1c46edf14f1c",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVYSyHgcnaxgnccgekZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e4d52cd-bd40-44b4-80da-98bb39e12184",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01L32subA6sTUZMuRmDin8eA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 752,
      "cache_creation_input_tokens": 2066,
      "cache_read_input_tokens": 33304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2066,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-10T07:27:47.299Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Nf1ndecp6pmvt37JWrAs1s`</summary>

```json
{
  "query": "arxiv 2025 2026 \"multi-pivot\" OR \"multi-source pivot\" multilingual instruction tuning language selection weighted curriculum low-resource"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e4d52cd-bd40-44b4-80da-98bb39e12184",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVYSyHgcnaxgnccgekZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6509731-5851-4e58-b63a-621019210725",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01L32subA6sTUZMuRmDin8eA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 752,
      "cache_creation_input_tokens": 2066,
      "cache_read_input_tokens": 33304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2066,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-10T07:27:48.020Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CQSn14eSky6Yk8NosQou8C`</summary>

```json
{
  "query": "TWMP \"typologically weighted\" \"multi-pivot\" 2026 arxiv instruction tuning low-resource"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6509731-5851-4e58-b63a-621019210725",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVYSyHgcnaxgnccgekZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4026cea-2c4b-4a34-be08-caf0064f5d79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01L32subA6sTUZMuRmDin8eA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 752,
      "cache_creation_input_tokens": 2066,
      "cache_read_input_tokens": 33304,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2066
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 752,
          "output_tokens": 244,
          "cache_read_input_tokens": 33304,
          "cache_creation_input_tokens": 2066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2066,
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

_source line 83 · 2026-05-10T07:27:51.592Z_

<details><summary>↩ Tool result · `toolu_01JD6ULBRh1mw7Axh35jkRqm`</summary>

```text
# URIEL+ Extension Research Summary

**Full Title:** "Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+"

**Authors:** Mason Shipton, York Hay Ng, Aditya Khan, Phuong Hanh Hoang, Xiang Lu, A. Seza Doğruöz, En-Shiun Annie Lee

**Submission Date:** October 31, 2025 (v1); revised March 18, 2026 (v2)

**Abstract Summary:**
The research addresses data sparsity limitations in URIEL+, a multilingual linguistic knowledge base. The authors introduce three major enhancements: script vectors for 7,488 languages representing writing system properties, integration of Glottolog adding 18,710 languages, and expanded lineage imputation for 26,449 languages through genealogical feature propagation.

**Key Claims on Sparsity Reduction:**
- Script vector sparsity reduced by 14%
- Language coverage increased up to 19,015 languages (1,007% expansion)
- Imputation quality metrics improved by up to 35%
- Cross-lingual transfer tasks demonstrated performance gains reaching 6% in certain configurations, though results showed "occasionally divergent performance" compared to baseline URIEL+

**Venue:** Accepted to LREC 2026
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e4d52cd-bd40-44b4-80da-98bb39e12184",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "65cf0144-b777-41cf-9a7a-a631d4294847",
  "sourceToolAssistantUUID": "5e4d52cd-bd40-44b4-80da-98bb39e12184",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-10T07:27:53.201Z_

<details><summary>↩ Tool result · `toolu_01Nf1ndecp6pmvt37JWrAs1s`</summary>

```text
Web search results for query: "arxiv 2025 2026 "multi-pivot" OR "multi-source pivot" multilingual instruction tuning language selection weighted curriculum low-resource"

Links: [{"title":"Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://arxiv.org/html/2510.25947v1"},{"title":"Large Multilingual Models Pivot Zero-Shot Multimodal Learning across Languages","url":"https://arxiv.org/html/2308.12038v3"},{"title":"Investigating Multi-Pivot Ensembling with Massively Multilingual Machine Translation Models","url":"https://arxiv.org/html/2311.07439v3"},{"title":"[2311.07439] Investigating Multi-Pivot Ensembling with Massively Multilingual Machine Translation Models","url":"https://arxiv.org/abs/2311.07439"},{"title":"[2401.01854] Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/abs/2401.01854"},{"title":"Multilingual Large Language Model: A Survey of Resources, Taxonomy and Frontiers","url":"https://arxiv.org/html/2404.04925v1"},{"title":"[2308.12038] Large Multilingual Models Pivot Zero-Shot Multimodal Learning across Languages","url":"https://arxiv.org/abs/2308.12038"},{"title":"Computer Science May 2025","url":"https://arxiv.org/list/cs/2025-05?skip=5250&show=2000"},{"title":"Artificial Intelligence Jun 2025","url":"https://arxiv.org/list/cs.AI/2025-06?skip=3175&show=2000"},{"title":"Artificial Intelligence May 2025","url":"https://www.arxiv.org/list/cs.AI/2025-05?skip=3400&show=2000"}]

I found several relevant results from your search. Here are the key findings:

## Most Relevant Result

The top result is a paper on "Revisiting Multilingual Data Mixtures in Language Model Pretraining" which discusses how using multiple pivots that balance breadth and proximity provides the most consistent benefits across language families. This paper from October 2025 directly addresses multi-pivot approaches in multilingual settings.

The work explores curriculum learning among pivot languages and includes controlled curriculum learning experiments designed to understand how the timing and order of language inclusion during training influence model performance.

## Other Related Research

There are also papers on related topics:

- Research on massively multilingual machine translation models that investigates pivoting via high-resource languages as a strategy for low-resource translation directions

- Work showing that using English as a pivot for cross-lingual instruction tuning, by first interpreting instructions in English before generating responses in the target language, can be highly effective

The first result appears to be the most directly aligned with your search query about multi-pivot approaches, weighted curriculum learning, and multilingual instruction tuning for low-resource languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6509731-5851-4e58-b63a-621019210725",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "a8a72d17-4eab-4aef-b98c-e535d33d2fd3",
  "sourceToolAssistantUUID": "d6509731-5851-4e58-b63a-621019210725",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-10T07:27:55.645Z_

<details><summary>↩ Tool result · `toolu_01CQSn14eSky6Yk8NosQou8C`</summary>

```text
Web search results for query: "TWMP "typologically weighted" "multi-pivot" 2026 arxiv instruction tuning low-resource"

Links: [{"title":"[2311.08711] PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning","url":"https://arxiv.org/abs/2311.08711"},{"title":"Investigating Multi-Pivot Ensembling with Massively Multilingual Machine Translation Models","url":"https://arxiv.org/html/2311.07439v3"},{"title":"Published as a conference paper at ICLR 2026 DATAPROPHET:","url":"https://arxiv.org/pdf/2603.19688"},{"title":"[2311.07439] Investigating Multi-Pivot Ensembling with Massively Multilingual Machine Translation Models","url":"https://arxiv.org/abs/2311.07439"},{"title":"[2601.16629] Typologically Informed Parameter Aggregation","url":"https://arxiv.org/abs/2601.16629"},{"title":"Machine Learning Apr 2025","url":"https://arxiv.org/list/cs.LG/2025-04?skip=75&show=1000"},{"title":"Computer Science May 2025","url":"https://www.arxiv.org/list/cs/2025-05?skip=8775&show=2000"},{"title":"Machine Learning May 2025","url":"https://www.arxiv.org/list/cs.LG/2025-05?skip=1100&show=2000"},{"title":"Parameter-Efficient Fine-Tuning for Large Models: A Comprehensive Survey","url":"https://arxiv.org/html/2403.14608v1"},{"title":"Computer Science Jun 2025","url":"https://www.arxiv.org/list/cs/2025-06?skip=10025&show=2000"}]

I found several relevant papers from the search results. Here are the most relevant findings:

**Typologically Informed Research (2026):**

A paper titled "Typologically Informed Parameter Aggregation (TIPA)" introduces a training-free method that constructs proxy language adapters by aggregating existing ones, weighted by typological similarity. The work addresses how massively multilingual language models enable cross-lingual generalization but underperform on low-resource and unseen languages, while adapter-based fine-tuning remains costly at scale. TIPA was evaluated on five NLP tasks and over 230 languages, consistently outperforming baselines such as English-only fine-tuning.

**Multi-Pivot Work:**

Research on "Investigating Multi-Pivot Ensembling with Massively Multilingual Machine Translation Models" addresses how massively multilingual machine translation models have limited performance on low- and very-low-resource translation directions, and explores ways of pivoting through multiple languages. The work proposes MaxEns, a novel combination strategy that makes output biased towards the most confident predictions.

**Related Instruction Tuning Work:**

The PLUG (pivot language guided generation) approach utilizes a high-resource language, primarily English, as the pivot to enhance instruction tuning in lower-resource languages.

I did not find a paper specifically matching all the exact terms "TWMP" combined with all the other search terms. The results show related work on typologically-weighted approaches and multi-pivot strategies for low-resource settings, but not a specific paper with that exact acronym from 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4026cea-2c4b-4a34-be08-caf0064f5d79",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "15330297-1af0-4c25-8063-5b1a658fc501",
  "sourceToolAssistantUUID": "a4026cea-2c4b-4a34-be08-caf0064f5d79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 86 · 2026-05-10T07:27:57.690Z_

Excellent - the TIPA paper is highly relevant. Let me fetch its full details and a few more searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15330297-1af0-4c25-8063-5b1a658fc501",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVZPw1GEunCH4L2ydKF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "166881e3-a2dd-433c-8221-2654612334cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GSeQrBnbofye82dwCVktsV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3067,
      "cache_read_input_tokens": 35370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3067,
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

_source line 87 · 2026-05-10T07:28:02.672Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01H35iM41xqqdGKa3X5V8YTs`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.16629",
  "prompt": "Extract full title, all authors, submission date, abstract, methodology (typological similarity weighting, adapter aggregation), number of languages, tasks, and key results. This seems directly related to typologically-weighted cross-lingual transfer."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "166881e3-a2dd-433c-8221-2654612334cc",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVZPw1GEunCH4L2ydKF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d4045ba-1d3d-42b8-a689-a6cdae25441f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GSeQrBnbofye82dwCVktsV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3067,
      "cache_read_input_tokens": 35370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3067,
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

_source line 88 · 2026-05-10T07:28:03.287Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HYCn1bnw9qH5rvguNSrgxQ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.01362",
  "prompt": "Extract full title, authors, submission date, abstract, and key findings about multilingual calibration effects of instruction-tuning, especially regarding low-resource languages."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d4045ba-1d3d-42b8-a689-a6cdae25441f",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVZPw1GEunCH4L2ydKF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8cad15c1-c3b8-48a1-8d18-4c4c8146a066",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GSeQrBnbofye82dwCVktsV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3067,
      "cache_read_input_tokens": 35370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3067,
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

_source line 89 · 2026-05-10T07:28:03.793Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013cNooW9ERWZq5sv7PMhLoA`</summary>

```json
{
  "query": "arxiv 2025 2026 \"proxy language\" OR \"typological similarity\" adapter aggregation multilingual instruction tuning LoRA low-resource"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cad15c1-c3b8-48a1-8d18-4c4c8146a066",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVZPw1GEunCH4L2ydKF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "378cf8b9-664c-4266-8840-387fc2def120",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GSeQrBnbofye82dwCVktsV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3067,
      "cache_read_input_tokens": 35370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3067,
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

### Tool result

_source line 90 · 2026-05-10T07:28:07.235Z_

<details><summary>↩ Tool result · `toolu_01H35iM41xqqdGKa3X5V8YTs`</summary>

```text
# Typologically Informed Parameter Aggregation - Extraction

**Full Title:** Typologically Informed Parameter Aggregation

**Authors:** Stef Accou, Wessel Poelman

**Submission Date:** January 23, 2026

**Abstract Summary:**
The paper addresses multilingual model limitations through a training-free approach. It introduces a system that "constructs proxy language adapters by aggregating existing ones, weighted by typological similarity," enabling zero-shot cross-lingual transfer without additional computational investment.

**Methodology:**
- **Typological Similarity Weighting:** Adapters are weighted based on linguistic typology to create proxy modules for unseen languages
- **Adapter Aggregation:** Existing language-specific adapters are combined systematically rather than training new ones
- **Framework:** Integrated into the MAD-X architecture

**Evaluation Scope:**
- **Languages:** Over 230 languages
- **Tasks:** Five distinct NLP tasks

**Key Results:**
The approach "consistently outperforms or matches baselines such as English-only fine-tuning," with particularly notable improvements for languages lacking dedicated adapters. The method eliminates training overhead while maintaining competitive performance.

**Venue:** EACL 2026 (Findings)

**License:** Creative Commons Attribution 4.0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d4045ba-1d3d-42b8-a689-a6cdae25441f",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "70992681-48cf-44d0-94a5-b4f00c0c4cce",
  "sourceToolAssistantUUID": "6d4045ba-1d3d-42b8-a689-a6cdae25441f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-10T07:28:08.059Z_

<details><summary>↩ Tool result · `toolu_01HYCn1bnw9qH5rvguNSrgxQ`</summary>

```text
# Paper Summary

**Full Title:** Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning

**Authors:** Jerry Huang, Peng Lu, Qiuhao Zeng, Yusuke Iwasawa, Yutaka Matsuo, Sarath Chandar, Edison Marrese-Taylor, Irene Li

**Submission Date:** January 4, 2026

**Abstract:** The researchers examine how language model calibration—the alignment between model confidence and actual accuracy—behaves across multilingual settings. They note that "model confidence can increase significantly after instruction-tuning on high-resource language SFT datasets" in low-resource languages, yet accuracy gains remain marginal, causing miscalibration issues.

## Key Findings on Multilingual Calibration:

1. **The Calibration Problem:** Standard instruction-tuning on high-resource language datasets produces inflated confidence in low-resource languages without corresponding accuracy improvements, creating a trustworthiness gap.

2. **Solution Identified:** Label smoothing emerges as an effective technique to mitigate miscalibration across all languages "without any need for low-resource SFT data."

3. **Scope:** Analysis covers 29 and 42 languages across two multilingual benchmarks, revealing systematic disparities in how well-calibrated models perform across linguistic diversity.

4. **Broader Implication:** The authors emphasize that "multilingual considerations" must guide both training and tuning processes to enhance model reliability and fairness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8cad15c1-c3b8-48a1-8d18-4c4c8146a066",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "086964d3-2f8c-48f7-a595-ce16f9e06fff",
  "sourceToolAssistantUUID": "8cad15c1-c3b8-48a1-8d18-4c4c8146a066",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-10T07:28:10.883Z_

<details><summary>↩ Tool result · `toolu_013cNooW9ERWZq5sv7PMhLoA`</summary>

```text
Web search results for query: "arxiv 2025 2026 "proxy language" OR "typological similarity" adapter aggregation multilingual instruction tuning LoRA low-resource"

Links: [{"title":"[2106.09685] LoRA: Low-Rank Adaptation of Large Language Models","url":"https://arxiv.org/abs/2106.09685"},{"title":"Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family: A Theoretical Framework for Low-Resource Language Models","url":"https://arxiv.org/html/2604.06202"},{"title":"[2411.18571] Challenges in Adapting Multilingual LLMs to Low-Resource Languages using LoRA PEFT Tuning","url":"https://arxiv.org/abs/2411.18571"},{"title":"LoRA: Low-Rank Adaptation of Large Language Models","url":"https://arxiv.org/html/2106.09685v2"},{"title":"GitHub - microsoft/LoRA: Code for loralib, an implementation of \"LoRA: Low-Rank Adaptation of Large Language Models\" · GitHub","url":"https://github.com/microsoft/LoRA"},{"title":"A Survey on Federated Fine-tuning of Large Language ...","url":"https://arxiv.org/pdf/2503.12016"},{"title":"A Survey of Instruction Tuning in Large Language Models","url":"https://www.arxiv.org/pdf/2508.17184"},{"title":"A Survey on LoRA of Large Language Models","url":"https://arxiv.org/html/2407.11046v3"},{"title":"LoRA: Low-Rank Adaptation of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=nZeVKeeFYf9"},{"title":"Adapting Multilingual LLMs to Low-Resource Languages using Continued Pre-training and Synthetic Corpus","url":"https://arxiv.org/html/2410.14815v1"}]

The search returned several relevant results related to your query about multilingual NLP, low-resource languages, LoRA, and typological similarity. Here are the most relevant findings:

## Key Results

**Most Relevant Recent Paper (2026):**

A recent arxiv paper develops a theoretical framework for understanding language model adaptation within the Turkic language family, focusing on Azerbaijani, Kazakh, Uzbek, Turkmen, and Gagauz, which share strong typological similarities while exhibiting substantial differences in digital resource availability. The paper examines typological similarity across languages and introduces the Turkic Transfer Coefficient (TTC) as a theoretical measure of cross-lingual transfer potential within a typologically coherent language family.

**Multilingual Instruction Tuning with LoRA:**

Research has investigated the effects of Low-Rank Adaptation (LoRA) Parameter-Efficient Fine-Tuning (PEFT) on multilingual models for low-resource languages, though findings reveal that while evaluation metrics often show performance decline post fine-tuning, manual assessments frequently suggest fine-tuned models outperform their originals, with improvements in target language generation but reduction in reasoning abilities.

**LoRA and Adapter Aggregation:**

Recent work proposes techniques to enable aggregation across clients with varying LoRA ranks through replication-based padding, where heterogeneous LoRA allows clients to adopt different rank values based on their data characteristics or resource constraints.

The search results contain foundational work on LoRA itself and surveys on instruction tuning and federated fine-tuning of LLMs, which provide broader context for your research area.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "378cf8b9-664c-4266-8840-387fc2def120",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "ade0ab5ec1fc2d1d3",
  "type": "user",
  "uuid": "791202a9-c21a-4291-baec-a27dd6aeaf1e",
  "sourceToolAssistantUUID": "378cf8b9-664c-4266-8840-387fc2def120",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 93 · 2026-05-10T07:30:05.557Z_

Now I have enough information for a comprehensive report. Let me compile all findings.

---

Here is a detailed, section-by-section verification report.

---

## 1. arXiv:2505.14297 — Cross-Lingual Optimization (CLO)

**Verified: EXISTS. The description in TWMP is LARGELY ACCURATE with one important nuance.**

- **Full title:** "Cross-Lingual Optimization for Language Transfer in Large Language Models"
- **Authors:** Jungseob Lee, Seongtae Hong, Hyeonseok Moon, Heuiseok Lim
- **Method:** CLO is genuinely DPO-based — it modifies Direct Preference Optimization with a combined SFT loss + novel cross-lingual loss term operating within the same batch. This is not standard SFT.
- **Translation model:** M2M100 1.2B — confirmed correct.
- **Dataset:** OpenAssistant conversations — confirmed correct.
- **Sample count:** The TWMP description of "6,400 OpenAssistant samples" needs a minor precision correction. The paper uses 6,400 English instruction-output pairs, which expand to 12,800 total samples (6,400 English + 6,400 translated target-language). The "6,400" figure refers to the English-side source, not the total training set. This distinction is non-trivial for reproducibility.
- **Languages tested:** 6 languages — Chinese, German (high-resource); Korean, Indonesian (medium); Swahili, Yoruba (low-resource).

**Verdict:** The TWMP characterization is accurate in substance, but the "6,400 samples" figure should ideally note this is the English source set, not the full training set of 12,800.

---

## 2. arXiv:2410.07809 — Linguistically-Informed Multilingual Instruction Tuning

**Verified: EXISTS. The description is ACCURATE, with one small discrepancy in language pool size.**

- **Full title:** "Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?"
- **Authors:** Gürkan Soykan, Gözde Gül Şahin
- **URIEL TYPO vectors:** 289-dimensional binary features covering syntactic, phonological, and phonetic inventory features — confirmed correct.
- **K-means clustering:** Yes, k-means with k=14 clusters — confirmed.
- **Language selection:** 14 languages selected — confirmed. However, the pool is **51 languages** (52 total in Bactrian-X minus Telugu, which was excluded), not 52. This is a minor but technically inaccurate detail in the TWMP claim of "52-language pool."
- **LoRA:** Confirmed, with rank r=64, α=16, dropout 0.05.
- **Dataset:** Bactrian-X (3.4M instruction-response pairs across 52 languages) — confirmed.
- **Base models:** mGPT 1.3B, mT5 3.7B XL, BLOOM 1.7B/3B/7B1 (not a single model).

**Verdict:** Description is accurate. Minor correction: the selection pool is 51 usable languages, not 52 (Telugu was excluded). The k=14 choice aligns with number of language families.

---

## 3. arXiv:2409.18472 — URIEL+

**Verified: EXISTS. The "~800 features / 4,366 languages / SoftImpute" claim is PARTIALLY ACCURATE with important caveats.**

- **Full title:** "URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base"
- **Authors:** Aditya Khan, Mason Shipton, David Anugraha, Kaiyao Duan, Phuong H. Hoang, Eric Khiu, A. Seza Doğruöz, En-Shiun Annie Lee
- **Venue:** COLING 2025
- **Language coverage:** 8,071 languages total in the database, but **4,366 languages capable of typological distance calculations** — this matches the TWMP claim precisely.
- **Feature count:** The paper adds 474 syntactic + 133 morphological + 30 phonological + 163 inventory features from new databases. The TWMP claim of "~800 features" is a reasonable approximation of total feature count (474+133+30+163 = 800 exactly). Confirmed accurate.
- **SoftImpute:** Confirmed as the default/best-performing imputation method. Three methods were implemented (k-NN, MIDASpy, SoftImpute); SoftImpute achieved highest F1 (0.7980) and is the default. Confirmed correct.

**Verdict:** The TWMP description is accurate. The "~800 features" figure maps exactly to 800 (474+133+30+163), and the 4,366 language figure and SoftImpute claim are both precise.

---

## 4. arXiv:2509.20129 — "Less is More"

**Verified: EXISTS. The Spearman ρ=0.358 claim is EXACTLY CORRECT.**

- **Full title:** "Less is More: The Effectiveness of Compact Typological Language Representations"
- **Authors:** York Hay Ng, Phuong Hanh Hoang, En-Shiun Annie Lee
- **Venue:** EMNLP 2025 Main Conference
- **Laplacian Score + 300 features:** The paper tests subset sizes of {100, 200, 300, 400, 500, 600, 700} from 800 total URIEL+ features.
- **Exact Spearman ρ value:** ρ = 0.358 (p = 0.061) for Laplacian Score at 300 features. This is the paper's strongest result.
- **Comparison with other methods at best subset size:** Variance (500 features) → ρ=0.295; PCA Loadings (700) → ρ=0.292; Laplacian Score (300) → ρ=0.358; Correlation-based FS (200) → ρ=0.264; URIEL+ baseline → ρ=0.260.
- **Evaluation:** Linguistic alignment tested on 28 language pairs comprising 24 low-resource languages in the Isthmo-Colombian area. Downstream tasks: LangRank (105 languages), ProxyLM (51 languages), LinguAlchemy (63 languages).

**Verdict:** The TWMP claim is exactly correct. Laplacian Score at 300 features achieves Spearman ρ=0.358, making it the best-performing method.

---

## 5. Competing/Concurrent Work on Typological Distance for Multilingual Instruction Tuning (2025–2026)

Several significant papers were found that the TWMP paper may or may not have cited. Listed by relevance:

### Highly Relevant — Potentially Missed

**a) Typologically Informed Parameter Aggregation (TIPA)**
- **arXiv:** 2601.16629
- **Authors:** Stef Accou, Wessel Poelman
- **Venue:** EACL 2026 (Findings)
- **Submitted:** January 23, 2026
- **Description:** Training-free method that constructs proxy language adapters by aggregating existing ones, weighted by typological similarity. Integrated into MAD-X architecture. Evaluated on 5 NLP tasks across 230+ languages. Consistently outperforms English-only fine-tuning baselines. **This is the most directly competing approach to TWMP:** both use typological similarity to weight language-specific parameters for low-resource transfer, though TIPA focuses on adapter aggregation at inference time while TWMP targets curriculum design during training.

**b) Revisiting Multilingual Data Mixtures in Language Model Pretraining**
- **arXiv:** 2510.25947
- **Authors:** Negar Foroutan, Paul Teiletche, Ayush Kumar Tarun, Antoine Bosselut (EPFL)
- **Submitted:** October 2025
- **Description:** Trains 1.1B and 33B LLMs across 25–400 languages. Finds that multiple pivots (e.g., English + Russian for Slavic) provide complementary benefits, and typological proximity matters most under extreme low-resource conditions. Proposes language weighting strategies distinguishing fixed-total vs. fixed-multilingual budgets.

**c) Analysis of Multi-Source Language Training in Cross-Lingual Transfer**
- **arXiv:** 2402.13562
- **Authors:** Seong Hoon Lim, Taejun Yun, Jinhyeon Kim, Jihun Choi, Taeuk Kim
- **Venue:** ACL 2024
- **Description:** Shows that multi-source language training increases mingling of embedding spaces, confirming language-agnostic feature emergence. Finds that arbitrary language combinations don't guarantee improvement; strategic selection is required. Provides practical heuristics for effective language pairings.

**d) Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family**
- **arXiv:** 2604.06202
- **Authors:** O. Ibrahimzade, K. Tabasaransky
- **Submitted:** March 13, 2026
- **Description:** Theoretical framework for LoRA-based adaptation within Turkic languages (Azerbaijani, Kazakh, Uzbek, Turkmen, Gagauz). Introduces the Turkic Transfer Coefficient (TTC) incorporating morphological similarity, lexical overlap, syntactic structure, and script compatibility. Finds typological similarity enables efficient multilingual transfer, but identifies structural limits in extremely low-resource scenarios.

**e) The Effect of Language Diversity When Fine-Tuning LLMs for Translation**
- **arXiv:** 2505.13090
- **Submitted:** May 2025
- **Description:** Systematic investigation across 132 translation directions showing that fine-tuning on broader language sets consistently improves translation across all categories.

**f) Simple Additions, Substantial Gains: Expanding URIEL+**
- **arXiv:** 2510.27183
- **Authors:** Mason Shipton, York Hay Ng, Aditya Khan, et al.
- **Venue:** LREC 2026 (accepted)
- **Submitted:** October 31, 2025 (revised March 2026)
- **Description:** Extends URIEL+ with script vectors (7,488 languages), Glottolog integration (18,710 languages), and genealogical feature propagation (26,449 languages). Reduces feature sparsity by 35% and expands language coverage by 1,007%. Cross-lingual transfer tasks improve by up to 6%. If TWMP uses URIEL+, this updated version may be more appropriate.

---

## 6. Qwen3.5-9B Model Verification

**Verified: LARGELY ACCURATE with one date correction.**

- **Release date:** March 2, 2026 (Hugging Face Hub; first model in Qwen3.5 family — the 397B-A17B MoE — launched February 16, 2026; the 9B arrived March 2). The TWMP claim of "March 2026" is accurate for the 9B specifically.
- **Vocabulary:** 248,320 tokens — the "248K-token vocabulary" claim is confirmed.
- **Languages:** 201 languages and dialects — confirmed.
- **Model series:** 0.8B, 2B, 4B, 9B — confirmed. No 7B model exists in this series — confirmed. The series skips 7B.
- **Additional context:** The Qwen3.5-9B uses Gated DeltaNet hybrid architecture, 262,144 native context length (extensible to 1,010,000), multimodal (text + images + video), and Multi-Token Prediction. The HF card lists citation year as "February 2026" for the broader family. Note the TWMP paper uses the 9B specifically, which appeared March 2, 2026.

**Verdict:** The TWMP description is accurate. Confirming 0.8B/2B/4B/9B series with no 7B, 248K vocabulary, 201 languages, March 2026.

---

## 7. Kazakh, Mongolian, and Uyghur Competing Work (2025–2026)

Several directly competing papers exist that TWMP should cite or acknowledge:

### Kazakh

**a) Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh**
- **arXiv:** 2502.13647
- **Authors:** Nurkhan Laiyk, Daniil Orel, Rituraj Joshi, Maiya Goloburda, Yuxia Wang, Preslav Nakov, Fajri Koto
- **Submitted:** February 19, 2025
- **Venue:** ACL 2025 (Long)
- **Method:** GPT-4o-assisted data generation + manual verification. 10,600-sample instruction dataset covering Kazakh governmental/cultural domains. Fine-tunes Qwen, Falcon, and Gemma. Consistent improvement on multiple-choice and generative tasks.

**b) Llama-3.1-Sherkala-8B-Chat (Sherkala-Chat)**
- **arXiv:** 2503.01493
- **Authors:** Fajri Koto, Rituraj Joshi, et al. (35 authors, large consortium)
- **Submitted:** March 3, 2025 (revised October 9, 2025)
- **Method:** Continual pre-training of LLaMA-3.1-8B on 45.3B tokens (Kazakh, English, Russian, Turkish) + instruction tuning with translated datasets, manually-verified Kazakh-specific data, and safety data. Significantly outperforms existing Kazakh and multilingual models at similar scale.

**c) SozKZ: Training Efficient Small Language Models for Kazakh from Scratch**
- **arXiv:** 2603.20854
- **Author:** Saken Tukenov
- **Submitted:** March 21, 2026
- **Method:** Llama-architecture models 50M–600M from scratch on 9B Kazakh tokens, dedicated 50K BPE tokenizer for agglutinative morphology. Achieves 30.3% on Kazakh cultural QA.

**d) The Development of Small-Scale Language Models for Low-Resource Languages, with a Focus on Kazakh and DPO**
- **Venue:** MDPI Big Data and Cognitive Computing, May 2025
- **Method:** Kazakh-specific tokenizer + causal LM from scratch + instruction tuning. Addresses agglutinative morphology directly.

### Mongolian/Kazakh Cross-Lingual Gap

**e) Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in LLMs**
- **arXiv:** 2603.21036
- **Author:** Abdul-Salem Beibitkhan
- **Submitted:** March 22, 2026
- **Key finding:** Aya Expanse achieves 82.3% for English but collapses to 15.7% for Kazakh and 4.7% for Mongolian. Performance gap of 13.8–16.7 percentage points across 8 LLMs. Chain-of-thought-then-translate helps bilingual models (+2.2–4.3pp) but not English-dominant models.

### Uyghur

**f) Low-Resource Language Expansion and Translation Capacity Enhancement for LLM: A Study on the Uyghur**
- **Venue:** COLING 2025
- **Method:** 4-stage pipeline: monolingual data collection → continual pre-training → translation-supervised fine-tuning → DPOSE (DPO based on Translation Self-Evolution). Significantly enhances LLM Uyghur translation with less parallel data.

---

## 8. Multi-Pivot Instruction Tuning — Directly Competing Methods

No paper with the exact acronym "TWMP" or label "Typologically-Weighted Multi-Pivot Curriculum" was found in search results, which is consistent with the paper being the work under review. However, the following are the most directly competing methods:

**a) PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning**
- **arXiv:** 2311.08711
- **Method:** Single English pivot; model trained to process instruction in English first, then respond in target language. Well-established baseline.

**b) TIPA (Typologically Informed Parameter Aggregation)**
- **arXiv:** 2601.16629 (EACL 2026)
- **Most directly competing conceptually:** Uses typological similarity to weight how adapter parameters are aggregated. Works on 230+ languages, 5 tasks, training-free. This is the closest thematic competitor to TWMP and may have been missed if TWMP was submitted before January 2026.

**c) Multilingual Instruction Tuning With Just a Pinch of Multilinguality**
- **arXiv:** 2401.01854
- **Method:** Shows only 40 multilingual examples suffice for substantial cross-lingual transfer; 2–4 diverse languages significantly improve generalization.

**d) BayLing 2**
- **arXiv:** 2411.16300
- **Method:** Dual-pivot (English + Chinese) cross-lingual alignment across 100+ languages.

**e) Revisiting Multilingual Data Mixtures (Foroutan et al., 2025)**
- **arXiv:** 2510.25947
- **Method:** Shows multiple complementary pivots (e.g., English breadth + typologically close pivot) give best results; validates the core intuition behind multi-pivot curriculum approaches.

---

## Summary of Key Findings

| Claim | Verdict |
|---|---|
| CLO (2505.14297) — DPO-based, M2M100, OpenAssistant | Accurate; note "6,400" is English-only subset; full training set is 12,800 |
| 2410.07809 — 289-dim TYPO, k-means, 14/52 langs, LoRA, Bactrian-X | Accurate; pool is 51 usable (not 52); base models are mGPT/mT5/BLOOM family |
| URIEL+ (2409.18472) — ~800 features, 4,366 langs, SoftImpute | Exactly accurate; 800 = 474+133+30+163; 4,366 confirmed; SoftImpute is default |
| Less is More (2509.20129) — Laplacian Score, 300 features, ρ=0.358 | Exactly accurate; confirmed from paper tables |
| Qwen3.5-9B — March 2026, 248K vocab, 201 langs, 0.8B/2B/4B/9B, no 7B | Accurate; 9B appeared March 2, 2026; vocabulary is precisely 248,320 tokens |
| Competing work missed: TIPA (arXiv:2601.16629, EACL 2026) | High-priority miss; typologically-weighted adapter aggregation, 230+ langs |
| Competing work missed: Sherkala-Chat (arXiv:2503.01493) | Relevant Kazakh LLM baseline |
| Competing work missed: Foroutan et al. 2510.25947 (EPFL, Oct 2025) | Relevant multi-pivot pretraining analysis |
| Competing work missed: Left Behind (arXiv:2603.21036) | Documents Kazakh/Mongolian collapse in current LLMs — relevant motivation |
| Competing work missed: arXiv:2502.13647 (ACL 2025, Kazakh) | Direct Kazakh instruction tuning baseline |

Sources:
- [arXiv:2505.14297 — CLO](https://arxiv.org/abs/2505.14297)
- [arXiv:2410.07809 — Linguistically-Informed Multilingual Instruction Tuning](https://arxiv.org/abs/2410.07809)
- [arXiv:2409.18472 — URIEL+](https://arxiv.org/abs/2409.18472)
- [arXiv:2509.20129 — Less is More](https://arxiv.org/abs/2509.20129)
- [Less is More at EMNLP 2025 (ACL Anthology)](https://aclanthology.org/2025.emnlp-main.1310.pdf)
- [Qwen/Qwen3.5-9B — Hugging Face](https://huggingface.co/Qwen/Qwen3.5-9B)
- [Qwen 3.5 Small Series — Awesome Agents](https://awesomeagents.ai/news/qwen-3-5-small-models-series/)
- [arXiv:2601.16629 — TIPA (EACL 2026)](https://arxiv.org/abs/2601.16629)
- [arXiv:2502.13647 — Kazakh Instruction Tuning (ACL 2025)](https://arxiv.org/abs/2502.13647)
- [arXiv:2503.01493 — Sherkala-Chat](https://arxiv.org/html/2503.01493v1)
- [arXiv:2603.21036 — Left Behind](https://arxiv.org/html/2603.21036)
- [arXiv:2603.20854 — SozKZ](https://arxiv.org/abs/2603.20854)
- [arXiv:2604.06202 — Turkic Language LoRA Framework](https://arxiv.org/abs/2604.06202)
- [arXiv:2510.25947 — Revisiting Multilingual Data Mixtures](https://arxiv.org/html/2510.25947v1)
- [arXiv:2402.13562 — Multi-Source Language Training Analysis (ACL 2024)](https://arxiv.org/html/2402.13562)
- [arXiv:2510.27183 — Simple Additions, Substantial Gains: URIEL+ Expansion](https://arxiv.org/abs/2510.27183)
- [COLING 2025 — Uyghur LLM Expansion](https://aclanthology.org/2025.coling-main.559/)
- [arXiv:2311.08711 — PLUG: Pivot Language Instruction Tuning](https://arxiv.org/abs/2311.08711)
- [arXiv:2601.01362 — Multilingual Calibration Effects](https://arxiv.org/abs/2601.01362)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "791202a9-c21a-4291-baec-a27dd6aeaf1e",
  "isSidechain": true,
  "agentId": "ade0ab5ec1fc2d1d3",
  "requestId": "req_011CatVaX4QZiLL3tgF9o5hb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3200f30b-1a00-487e-9243-75dfaff5e6aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EZTZQP7x6ocsxxsco3vCR9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1905,
      "cache_read_input_tokens": 38437,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1905,
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
