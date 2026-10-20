# Research conversation: You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Ru

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 72
- **Recorded user turns:** 1
- **Tool calls:** 33
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a07b72467ddf2db7b.jsonl`
- **Structured JSON:** [`67d422b626b7611bc63e.json`](../../sessions/67/67d422b626b7611bc63e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

72 recorded events

### User

_source line 1 · 2026-05-18T07:07:38.449Z_

You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.

Search 1: "best open source LLM 2025 2026 base model"
Search 2: "latest base models huggingface 2025"
Search 3: "new open source LLM families 2025 2026"

Return ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "f05d6f35-cf46-42fd-9ae7-58743bd9d106",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T07:07:38.454Z_

```json
{
  "parentUuid": "f05d6f35-cf46-42fd-9ae7-58743bd9d106",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
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
      "TodoWrite",
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
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "0a9ee59a-d6d0-4024-b644-2d58aa5dc208",
  "timestamp": "2026-05-18T07:07:38.454Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T07:07:41.581Z_



I'll run all three web searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a9ee59a-d6d0-4024-b644-2d58aa5dc208",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cUzmjVip15wkmKTy9Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "038f8d2d-70fd-4a49-8445-8164142d4b00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tg18Hh2mtyrCZHumEmUv1D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15518,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15518,
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

_source line 4 · 2026-05-18T07:07:41.938Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018ELxibVVD5ckC6fCZpvEp1`</summary>

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
  "parentUuid": "038f8d2d-70fd-4a49-8445-8164142d4b00",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cUzmjVip15wkmKTy9Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "406ece16-a79f-47a2-ab48-4d6e7117c7ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tg18Hh2mtyrCZHumEmUv1D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15518,
      "cache_read_input_tokens": 0,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15518
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 87,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15518,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15518,
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

_source line 5 · 2026-05-18T07:07:41.941Z_

<details><summary>↩ Tool result · `toolu_018ELxibVVD5ckC6fCZpvEp1`</summary>

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
  "parentUuid": "406ece16-a79f-47a2-ab48-4d6e7117c7ba",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "499db8e1-e6b1-4929-8fb9-95c3ac52a50d",
  "sourceToolAssistantUUID": "406ece16-a79f-47a2-ab48-4d6e7117c7ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-18T07:07:44.610Z_



Now I'll run all three searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "499db8e1-e6b1-4929-8fb9-95c3ac52a50d",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cVFupNKdVW94jok9ht",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa118901-11ec-461f-87f3-8b9788bbc6e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8bbgSSwYxysuP3tZgow4o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 15518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
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

_source line 7 · 2026-05-18T07:07:45.112Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RKx8Sb6C1xa3wMXpnYfWmJ`</summary>

```json
{
  "query": "best open source LLM 2025 2026 base model 7B 14B parameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa118901-11ec-461f-87f3-8b9788bbc6e7",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cVFupNKdVW94jok9ht",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8d7199f-46cf-4a72-9a85-5e03daabc728",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8bbgSSwYxysuP3tZgow4o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 15518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
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

_source line 8 · 2026-05-18T07:07:45.612Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xf1AdMfWajmi3d4RXg9YLA`</summary>

```json
{
  "query": "latest base models huggingface 2025 2026 open source LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8d7199f-46cf-4a72-9a85-5e03daabc728",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cVFupNKdVW94jok9ht",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b882b5a-c0c6-491b-9978-2c3ca06f2daf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8bbgSSwYxysuP3tZgow4o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 15518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
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

_source line 9 · 2026-05-18T07:07:45.665Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PuNz9DDDjEg8pJUQbgBHs2`</summary>

```json
{
  "query": "new open source LLM families 2025 2026 base model release"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b882b5a-c0c6-491b-9978-2c3ca06f2daf",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cVFupNKdVW94jok9ht",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0fc92ea-e644-40f9-81d4-4637ea81a036",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8bbgSSwYxysuP3tZgow4o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 15518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
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

### Tool result

_source line 10 · 2026-05-18T07:07:55.425Z_

<details><summary>↩ Tool result · `toolu_01Xf1AdMfWajmi3d4RXg9YLA`</summary>

```text
Web search results for query: "latest base models huggingface 2025 2026 open source LLM"

Links: [{"title":"Best Open-Source LLM Models in 2026: Coding, Local, Agentic AI, Benchmarks, and License","url":"https://huggingface.co/blog/daya-shankar/open-source-llms"},{"title":"State of Open Source on Hugging Face: Spring 2026","url":"https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026"},{"title":"Open LLM Leaderboard best models ❤️‍🔥 - a open-llm-leaderboard Collection","url":"https://huggingface.co/collections/open-llm-leaderboard/open-llm-leaderboard-best-models"},{"title":"The Best Open Source and Open-Weight LLM Models to Run Locally in 2026","url":"https://huggingface.co/blog/daya-shankar/open-source-llm-models-to-run-locally"},{"title":"Best Open Source LLMs: Complete 2026 Guide | Contabo Blog","url":"https://contabo.com/blog/open-source-llms/"},{"title":"Top 10 Downloaded Open-Source Models on HuggingFace","url":"https://www.analyticsvidhya.com/blog/2025/11/top-open-source-models-on-huggingface/"},{"title":"Top 10 LLM Models on Hugging Face | Cloudsmith","url":"https://cloudsmith.com/blog/top-10-most-popular-llm-models-on-hugging-face"},{"title":"Top 7 Platforms to Fine-Tune Open Source LLMs in 2026 | Second Talent","url":"https://www.secondtalent.com/resources/top-platforms-to-fine-tune-open-source-llms/"},{"title":"Models – Hugging Face","url":"https://huggingface.co/models"},{"title":"The Best Open-Source Small Language Models (SLMs) in 2026","url":"https://www.bentoml.com/blog/the-best-open-source-small-language-models"}]

Based on the search results, here's a comprehensive overview of the latest base models on Hugging Face for 2025-2026 open source LLMs:

## Key Latest Models (2025-2026)

### Flagship Models

Kimi K2.6 is one of the strongest open-weight models for developers in 2026. The Hugging Face model card lists it under a Modified MIT license and shows a model size of about 1.1T parameters.

Qwen3 is the model family that quietly became the answer to "what should I run locally?" for most developers. Sizes range from 1.7B to 235B, with an Apache 2.0 license with no user cap, no commercial restrictions, no legal headaches.

Meta dropped Llama 4 in April 2025, and it's a different beast from what came before. Llama 4 won gold medals in IMO 2025 and IOI 2025, solving competitive programming and math olympiads with an open-weights model.

### Small Language Models (SLMs)

SmolLM3-3B is a fully open instruct and reasoning model from Hugging Face, outperforming Llama-3.2-3B and Qwen2.5-3B while staying competitive with many 4B-class alternatives across 12 popular LLM benchmarks.

### For Local Deployment

Microsoft built Phi-4-mini-instruct, one of the most quietly impressive models of 2026, and the point is that it runs on the machine you already have.

## Ecosystem Growth

In 2025, Hugging Face grew to 13 million users, more than 2 million public models, and over 500,000 public datasets. China surpassed the U.S. in monthly downloads and overall downloads, with Chinese models quickly accounting for the plurality or 41% of downloads.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b882b5a-c0c6-491b-9978-2c3ca06f2daf",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "4b2532cf-91a8-4a5d-990c-97a3142e6640",
  "sourceToolAssistantUUID": "5b882b5a-c0c6-491b-9978-2c3ca06f2daf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-18T07:07:56.121Z_

<details><summary>↩ Tool result · `toolu_01RKx8Sb6C1xa3wMXpnYfWmJ`</summary>

```text
Web search results for query: "best open source LLM 2025 2026 base model 7B 14B parameters"

Links: [{"title":"Best Open-Source LLM Models in 2026: Coding, Local, Agentic AI, Benchmarks, and License","url":"https://huggingface.co/blog/daya-shankar/open-source-llms"},{"title":"Open-Source LLMs Compared 2026 – 25+ Models… – Till Freitag","url":"https://till-freitag.com/en/blog/open-source-llm-comparison"},{"title":"Best Open-Source LLM 2026: 8 Tested, 3 Beat GPT-4 | TECHSY","url":"https://techsy.io/en/blog/best-open-source-llms-2026"},{"title":"Best Open-Source LLMs in 2026 - Featherless","url":"https://featherless.ai/blog/best-open-source-llms-2026"},{"title":"Open LLM Leaderboard best models ❤️‍🔥 - a open-llm-leaderboard Collection","url":"https://huggingface.co/collections/open-llm-leaderboard/open-llm-leaderboard-best-models"},{"title":"The Best Open Source and Open-Weight LLM Models to Run Locally in 2026","url":"https://huggingface.co/blog/daya-shankar/open-source-llm-models-to-run-locally"},{"title":"Best Open Source LLMs: Complete 2026 Guide | Contabo Blog","url":"https://contabo.com/blog/open-source-llms/"},{"title":"Best Open-Source LLMs in 2026: A Practical Guide by Use Case - ML Journey","url":"https://mljourney.com/best-open-source-llms-in-2026-a-practical-guide-by-use-case/"},{"title":"Best Local LLM Models 2026 | Developer Comparison","url":"https://www.sitepoint.com/best-local-llm-models-2026/"},{"title":"Best Open Source LLMs in 2026: DeepSeek, Llama & More","url":"https://www.miniloop.ai/blog/best-open-source-llms-2026"}]

Based on the search results, here's a comprehensive overview of the best open-source LLM base models in the 7B-14B parameter range for 2025-2026:

## Top Base Models in 7B-14B Range

### 7B Models

**Qwen2.5-Coder 7B** - Fits on 8GB VRAM and outperforms general-purpose models twice its size on code generation, debugging, and refactoring.

**Qwen 3 7B** - Posts the highest HumanEval score (76.0) of any model under 8B parameters in this comparison, a 3.4-point margin over Llama 3.3's 72.6. Its multilingual support is the strongest across all four families, with particular strength in CJK languages alongside robust English performance.

**Mistral Small 3 7B** - Achieves approximately 50 tokens per second on mid-range 16GB hardware at Q4_K_M, the fastest in this comparison. It scores 8.0 on MT-Bench, the instruction-following benchmark, producing well-structured outputs with minimal prompt engineering.

### 14B Models

**DeepSeek-R1 14B** - DeepSeek also released distilled variants at 1.5B, 7B, 14B, 32B, and 70B parameters.

**Phi-4 14B** - Phi-4 14B is recommended for those who want to run something on a single GPU. The Phi-4 14B variant at Q5_K_M scales up to 76.2 MMLU, competitive with much larger models.

**Qwen2.5-Coder 14B** - The 14B variant is the sweet spot for 16GB VRAM setups — noticeably better at multi-file reasoning and complex algorithm implementation.

## Key Recommendations

For general use: For most developers, Llama 3.3 8B is the best overall starting point. Mistral Small 3 7B wins when throughput matters most, Phi-4-mini (3.8B) is the only real option on low-resource hardware, and Qwen 3 7B leads for code generation and multilingual work.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8d7199f-46cf-4a72-9a85-5e03daabc728",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "a503b54e-6289-4a49-98b4-6c73c1f7253f",
  "sourceToolAssistantUUID": "e8d7199f-46cf-4a72-9a85-5e03daabc728",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T07:07:58.470Z_

<details><summary>↩ Tool result · `toolu_01PuNz9DDDjEg8pJUQbgBHs2`</summary>

```text
Web search results for query: "new open source LLM families 2025 2026 base model release"

Links: [{"title":"Open-Source LLM Landscape 2026, 15+ Model Families Mapped | Presenc AI","url":"https://presenc.ai/research/open-source-llm-landscape-2026"},{"title":"Best Open-Source LLMs in 2026 - Featherless","url":"https://featherless.ai/blog/best-open-source-llms-2026"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"Best Open Source Self-Hosted LLMs for Coding in 2026 - Pinggy","url":"https://pinggy.io/blog/best_open_source_self_hosted_llms_for_coding/"},{"title":"Open-Source LLMs Compared 2026 – 25+ Models… – Till Freitag","url":"https://till-freitag.com/en/blog/open-source-llm-comparison"},{"title":"AI Updates Today (May 2026) – Latest AI Model Releases","url":"https://llm-stats.com/llm-updates"},{"title":"Top 7 open source LLMs for 2026","url":"https://www.instaclustr.com/education/open-source-ai/top-7-open-source-llms-for-2026/"},{"title":"Open-Source LLMs 2026: Llama 4, Mistral, Qwen, Falcon & More | AI Moments","url":"https://www.singularitymoments.com/open-source-llms-2026/"},{"title":"Open Source LLM Releases 2026: Every Major Model So Far - Fazm Blog","url":"https://fazm.ai/blog/open-source-llm-releases-2026"},{"title":"Best Open Source LLMs: Complete 2026 Guide | Contabo Blog","url":"https://contabo.com/blog/open-source-llms/"}]

Based on the search results, here's a comprehensive overview of new open-source LLM families released in 2025-2026:

## Major Model Families Released

### Meta Llama 4 (April 2025)
Llama 4 includes Scout (109B total, 17B active, 10M context window), Maverick (400B total, 17B active, 1M context), and the announced but unreleased Behemoth (~2T total, 288B active). Llama 4 is the most widely deployed open source model family, with over 650 million total downloads and roughly 9% of enterprise production workloads running on Llama variants.

### DeepSeek Models (2024-2025)
DeepSeek has released open-weight models including DeepSeek V2, V3, and the reasoning-focused R1 (2024-2025). The latest release DeepSeek-V4 is designed for long-context reasoning, coding, and agentic workflows, with two large MoE models: DeepSeek-V4-Pro (1.6T total, 49B active) and DeepSeek-V4-Flash (284B total, 13B active).

### Alibaba Qwen Models (2025-2026)
Qwen 3.5 (released February 2026) is a native vision-language model with 397B total parameters (17B active per pass), supporting 201 languages and offering a 1M token context window.

### Moonshot Kimi K2 Line (2025)
Moonshot released the open-weight Kimi K2 line during 2025. Kimi K2.5 has 1 trillion parameters with MoE (32B active), 384 experts, and a unique Agent Swarm architecture.

### Google Gemma 3 (January 2026)
Google released Gemma 3 in January 2026 with four sizes: 1B, 4B, 12B, and 27B parameters. Key improvements include native vision support, a 128K context window across all sizes, and a new sliding-window attention mechanism that reduces memory usage.

### Mistral Family (2025-2026)
Mistral is a European frontier AI company with models including Mistral 7B, Mixtral 8x7B/8x22B (mixture-of-experts), Mistral Large (2024), and later iterations, offering both fully open-weight models under Apache 2.0 and commercial tier models.

### Other Notable Releases
Cohere released Command A in March 2026, using a 111B parameter MoE architecture with 23B active parameters and supporting a 256K context window, optimized for retrieval-augmented generation (RAG) workflows.

2025 was the year open-source LLMs closed the gap with proprietary models, and in 2026, they're on par in many areas – or better.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0fc92ea-e644-40f9-81d4-4637ea81a036",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "086fa922-3f8e-4d73-b003-d965dc937345",
  "sourceToolAssistantUUID": "f0fc92ea-e644-40f9-81d4-4637ea81a036",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-18T07:08:01.317Z_

Let me get more specific details on models in the 7B-14B range with HuggingFace repo IDs and benchmark numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "086fa922-3f8e-4d73-b003-d965dc937345",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cWUNCLQf5rfETXF7zu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2533cfe8-f214-4af0-8b65-df637ed2671e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013SKekHLGuou85HY3kMEt9Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3640,
      "cache_read_input_tokens": 16969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3640,
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

_source line 14 · 2026-05-18T07:08:02.395Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016j9mQYndRRdA9Q6Sth2QCj`</summary>

```json
{
  "query": "Qwen3 7B 8B base model huggingface repo release date benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2533cfe8-f214-4af0-8b65-df637ed2671e",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cWUNCLQf5rfETXF7zu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b63afec5-bbdb-4cd1-bc37-0b7fc9024c05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013SKekHLGuou85HY3kMEt9Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3640,
      "cache_read_input_tokens": 16969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3640,
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

_source line 15 · 2026-05-18T07:08:02.733Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V4ACkuaeDNffwnUYvBQW5x`</summary>

```json
{
  "query": "Gemma 3 12B base model huggingface repo benchmark 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b63afec5-bbdb-4cd1-bc37-0b7fc9024c05",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cWUNCLQf5rfETXF7zu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d3848b1-fad8-49bd-818e-fc25f79c8127",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013SKekHLGuou85HY3kMEt9Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3640,
      "cache_read_input_tokens": 16969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3640,
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

_source line 16 · 2026-05-18T07:08:03.263Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017sHpfYuQ6DKc2TMyiLhEQb`</summary>

```json
{
  "query": "Llama 4 8B base model huggingface 2025 release"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d3848b1-fad8-49bd-818e-fc25f79c8127",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cWUNCLQf5rfETXF7zu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36b8db71-02e4-42b3-8481-a0b2fd9c4b7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013SKekHLGuou85HY3kMEt9Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3640,
      "cache_read_input_tokens": 16969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3640,
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

_source line 17 · 2026-05-18T07:08:03.650Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AkbAta3waqKdU5g4qkRVcX`</summary>

```json
{
  "query": "Phi-4 14B base model huggingface repo release date training data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36b8db71-02e4-42b3-8481-a0b2fd9c4b7a",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cWUNCLQf5rfETXF7zu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a45af7d-d527-4219-b217-8168086e030b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013SKekHLGuou85HY3kMEt9Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3640,
      "cache_read_input_tokens": 16969,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3640
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 261,
          "cache_read_input_tokens": 16969,
          "cache_creation_input_tokens": 3640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3640,
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

_source line 18 · 2026-05-18T07:08:09.944Z_

<details><summary>↩ Tool result · `toolu_016j9mQYndRRdA9Q6Sth2QCj`</summary>

```text
Web search results for query: "Qwen3 7B 8B base model huggingface repo release date benchmark"

Links: [{"title":"Qwen/Qwen3-8B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B-Base"},{"title":"GitHub - QwenLM/Qwen: The official repo of Qwen (通义千问) chat & pretrained large language model proposed by Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen"},{"title":"GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series developed by Qwen team, Alibaba Group. · GitHub","url":"https://github.com/QwenLM/Qwen3.6"},{"title":"Qwen/Qwen3.6-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-27B"},{"title":"Qwen/Qwen3-8B-FP8 · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B-FP8"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"Qwen3.6-27B: 27B Model Beats 397B on Coding (2026)","url":"https://www.buildfastwithai.com/blogs/qwen3-6-27b-review-2026"},{"title":"Qwen3 - a Qwen Collection","url":"https://huggingface.co/collections/Qwen/qwen3"},{"title":"Qwen/Qwen3-Embedding-8B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Embedding-8B"},{"title":"Qwen (Qwen)","url":"https://huggingface.co/Qwen"}]

Based on the search results, here's what I found about Qwen3 7B/8B base models:

## Release Date

Qwen3 was released in 2025, with the technical report available on arXiv (2505.09388). More specifically, Qwen3 was announced as the latest addition to the Qwen family of large language models.

## Hugging Face Repository

Six dense models are open-weighted, including Qwen3-32B, Qwen3-14B, Qwen3-8B, Qwen3-4B, Qwen3-1.7B, and Qwen3-0.6B, with pre-trained counterparts available on Hugging Face, ModelScope, and Kaggle.

## Base Model Performance Benchmarks

The overall performance of Qwen3 dense base models matches that of Qwen2.5 base models with more parameters. For instance, Qwen3-8B-Base performs as well as Qwen2.5-14B-Base. Additionally, in areas like STEM, coding, and reasoning, Qwen3 dense base models even outperform larger Qwen2.5 models.

## Key Features

Qwen3 is pre-trained on 36 trillion tokens across 119 languages — tripling the language coverage of Qwen2.5 — with a much richer mix of high-quality data, including coding, STEM, reasoning, book, multilingual, and synthetic data.

For more detailed benchmark evaluations, the blog, GitHub, and documentation contain detailed information including benchmark evaluation, hardware requirements, and inference performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b63afec5-bbdb-4cd1-bc37-0b7fc9024c05",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "3dd936d3-ccc3-4451-8e91-394b2fc5f927",
  "sourceToolAssistantUUID": "b63afec5-bbdb-4cd1-bc37-0b7fc9024c05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T07:08:10.217Z_

<details><summary>↩ Tool result · `toolu_017sHpfYuQ6DKc2TMyiLhEQb`</summary>

```text
Web search results for query: "Llama 4 8B base model huggingface 2025 release"

Links: [{"title":"meta-llama (Meta Llama)","url":"https://huggingface.co/meta-llama"},{"title":"nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 · Hugging Face","url":"https://huggingface.co/nvidia/Llama-4-Scout-17B-16E-Instruct-FP8"},{"title":"aviol/Meta-Llama-4-8B · Hugging Face","url":"https://huggingface.co/aviol/Meta-Llama-4-8B"},{"title":"nvidia/Llama-3.1-8B-Instruct-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Llama-3.1-8B-Instruct-NVFP4"},{"title":"Llama4 · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/llama4"},{"title":"Welcome Llama 4 Maverick & Scout on Hugging Face","url":"https://huggingface.co/blog/llama4-release"},{"title":"Meta Llama 4 explained: Everything you need to know","url":"https://www.techtarget.com/whatis/feature/Meta-Llama-4-explained-Everything-you-need-to-know"},{"title":"LLaMA 4 Explained - Everything You Need to Know","url":"https://www.labellerr.com/blog/llama-4/"},{"title":"Llama (language model) - Wikipedia","url":"https://en.wikipedia.org/wiki/Llama_(language_model)"},{"title":"meta-llama/Llama-4-Scout-17B-16E-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct"}]

Based on the search results, here's what I found about Llama 4 and the 8B base model:

## Llama 4 Release Information

Llama 4 was released on April 5, 2025. However, it's important to note that the Llama 4 family of models comes in two flavors: 109B and 402B parameters, along with smaller efficient models.

## Llama 4 Model Sizes

Rather than an 8B base model, Meta is launching two efficient models in the Llama 4 series: Llama 4 Scout, a 17 billion parameter model with 16 experts, and Llama 4 Maverick, a 17 billion parameter model with 128 experts.

The Llama 4 collection of models are natively multimodal AI models that enable text and multimodal experiences, leveraging a mixture-of-experts architecture to offer industry-leading performance in text and image understanding.

## Availability on Hugging Face

Llama 4 is available at https://huggingface.co/meta-llama. The models can be accessed and used through the Hugging Face platform with the appropriate licenses and authentication.

If you were specifically looking for an 8B Llama model, Meta's previous generation Llama 3 came in 8B and 70B sizes, but Llama 4 focuses on larger, more efficient models using mixture-of-experts architecture.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36b8db71-02e4-42b3-8481-a0b2fd9c4b7a",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "b7eb9741-0a6c-40fa-af89-98a2e98eb596",
  "sourceToolAssistantUUID": "36b8db71-02e4-42b3-8481-a0b2fd9c4b7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T07:08:11.384Z_

<details><summary>↩ Tool result · `toolu_01AkbAta3waqKdU5g4qkRVcX`</summary>

```text
Web search results for query: "Phi-4 14B base model huggingface repo release date training data"

Links: [{"title":"microsoft/Phi-4-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning"},{"title":"microsoft/phi-4 · Hugging Face","url":"https://huggingface.co/microsoft/phi-4"},{"title":"microsoft/Phi-4-multimodal-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-multimodal-instruct"},{"title":"microsoft/Phi-4-mini-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-reasoning"},{"title":"OpenMeditron/Meditron3-Phi4-14B · Hugging Face","url":"https://huggingface.co/OpenMeditron/Meditron3-Phi4-14B"},{"title":"Phi-4 Local Setup: Microsoft's 14B Reasoning on 12GB GPUs | Local AI Master","url":"https://localaimaster.com/blog/phi-4-local-setup"},{"title":"microsoft/Phi-4-reasoning-plus · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-plus"},{"title":"Phi · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/phi"},{"title":"NyxKrage/Microsoft_Phi-4 · Hugging Face","url":"https://huggingface.co/NyxKrage/Microsoft_Phi-4"},{"title":"microsoft/Phi-4-mini-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-instruct"}]

Based on the web search results, here's the information about Phi-4 14B base model:

## Release Date

Phi-4 is Microsoft's December 2024 release of their efficient-LLM family — a 14.7B-parameter model.

## Training Data

The training data is an extension of the data used for Phi-3 and includes a wide variety of sources from: Publicly available documents filtered rigorously for quality, selected high-quality educational data, and code. Newly created synthetic, "textbook-like" data for the purpose of teaching math, coding, common sense reasoning, general knowledge of the world. Acquired academic books and Q&A datasets. High quality chat format supervised data covering various topics to reflect human preferences on different aspects such as instruct-following, truthfulness, honesty and helpfulness. Additionally, multilingual data constitutes about 8% of the overall data.

## HuggingFace Repository

The base model can be found at the official HuggingFace repository: `microsoft/phi-4`


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a45af7d-d527-4219-b217-8168086e030b",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "2fb2e494-fa2d-4817-889a-97679a0e5e85",
  "sourceToolAssistantUUID": "9a45af7d-d527-4219-b217-8168086e030b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T07:08:13.634Z_

<details><summary>↩ Tool result · `toolu_01V4ACkuaeDNffwnUYvBQW5x`</summary>

```text
Web search results for query: "Gemma 3 12B base model huggingface repo benchmark 2026"

Links: [{"title":"google/gemma-3-12b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-it"},{"title":"tensorblock/gemma-3-12b-it-GGUF · Hugging Face","url":"https://huggingface.co/tensorblock/gemma-3-12b-it-GGUF"},{"title":"google/gemma-3-12b-it-qat-q4_0-gguf · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-gguf"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"google/gemma-3-12b-pt · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-pt"},{"title":"RedHatAI/gemma-3-12b-it-quantized.w8a8 · Hugging Face","url":"https://huggingface.co/RedHatAI/gemma-3-12b-it-quantized.w8a8"},{"title":"Gemma 4 model overview | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core"},{"title":"nocturne23/gemma-3-12b-it-Q4_K_M-GGUF · Hugging Face","url":"https://huggingface.co/nocturne23/gemma-3-12b-it-Q4_K_M-GGUF"},{"title":"lmstudio-community/gemma-3-12b-it-GGUF · Hugging Face","url":"https://huggingface.co/lmstudio-community/gemma-3-12b-it-GGUF"},{"title":"Quantized Models for google/gemma-3-12b-it – Hugging Face","url":"https://huggingface.co/models?other=base_model%3Aquantized%3Agoogle%2Fgemma-3-12b-it"}]

Based on the web search results, I found information about the Gemma 3 12B model on Hugging Face. Here's what I found:

## Gemma 3 12B Base Model Overview

Gemma 3 is a family of lightweight, state-of-the-art open models from Google, and Gemma 3 models are multimodal, handling text and image input and generating text output, with open weights for both pre-trained variants and instruction-tuned variants.

Gemma 3 has a large, 128K context window, multilingual support in over 140 languages, and is available in more sizes than previous versions.

## Benchmark Performance

Using the benchmark evaluation metrics described in this document, these models have shown to provide superior performance to other, comparably-sized open model alternatives. However, the specific benchmark metrics and numerical results are not detailed in the search results.

The 12B model was trained with 12 trillion tokens.

## Repository Access

The Gemma 3 12B model repositories on Hugging Face include:
- **Instruction-tuned version**: google/gemma-3-12b-it
- **Pre-trained version**: google/gemma-3-12b-pt

To access Gemma on Hugging Face, you're required to review and agree to Google's usage license.

If you're looking for specific benchmark scores or detailed performance metrics for the base model, you may need to check the official Gemma 3 report or the model documentation directly on the Hugging Face repository pages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d3848b1-fad8-49bd-818e-fc25f79c8127",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "66dc5a2b-ad99-481b-9a86-9912e48c1235",
  "sourceToolAssistantUUID": "1d3848b1-fad8-49bd-818e-fc25f79c8127",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-18T07:08:16.697Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YUVVB71nKv5cP15eC66Yy9`</summary>

```json
{
  "query": "Mistral Small 3 7B base model huggingface release date 2025 benchmark MMLU"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66dc5a2b-ad99-481b-9a86-9912e48c1235",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cXbBF8YzvnQRDFHzkb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4ee4359-30d5-4e24-bde6-599dc46f678a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNPJ5LscWEEDyyDb2jdW9m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1646,
      "cache_creation_input_tokens": 2297,
      "cache_read_input_tokens": 20609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2297,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 23 · 2026-05-18T07:08:17.769Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C7Fe9WLPEiE62JR9v3UxUK`</summary>

```json
{
  "query": "DeepSeek V2 V3 7B 14B base model huggingface distilled 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4ee4359-30d5-4e24-bde6-599dc46f678a",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cXbBF8YzvnQRDFHzkb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a8a1211-f929-4a36-bcda-ed7161cdbf75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNPJ5LscWEEDyyDb2jdW9m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1646,
      "cache_creation_input_tokens": 2297,
      "cache_read_input_tokens": 20609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2297,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 24 · 2026-05-18T07:08:18.105Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BEXBM5kKmHtDWYvbzuaCNo`</summary>

```json
{
  "query": "Qwen2.5 7B 14B base model huggingface benchmark training tokens 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a8a1211-f929-4a36-bcda-ed7161cdbf75",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cXbBF8YzvnQRDFHzkb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd530fe0-1303-4c5a-b4cc-868e6733658c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNPJ5LscWEEDyyDb2jdW9m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1646,
      "cache_creation_input_tokens": 2297,
      "cache_read_input_tokens": 20609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2297,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 25 · 2026-05-18T07:08:18.620Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018hzzuzEY7t4QqDTYYBH7z2`</summary>

```json
{
  "query": "OLMo 2 7B 13B base model huggingface 2025 release Allen AI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd530fe0-1303-4c5a-b4cc-868e6733658c",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cXbBF8YzvnQRDFHzkb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24f8f430-5ced-484e-80b5-98c60e9f2a2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNPJ5LscWEEDyyDb2jdW9m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1646,
      "cache_creation_input_tokens": 2297,
      "cache_read_input_tokens": 20609,
      "output_tokens": 256,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2297
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1646,
          "output_tokens": 256,
          "cache_read_input_tokens": 20609,
          "cache_creation_input_tokens": 2297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2297,
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

_source line 26 · 2026-05-18T07:08:23.158Z_

<details><summary>↩ Tool result · `toolu_01YUVVB71nKv5cP15eC66Yy9`</summary>

```text
Web search results for query: "Mistral Small 3 7B base model huggingface release date 2025 benchmark MMLU"

Links: [{"title":"Mistral 7B","url":"https://mistral.ai/news/announcing-mistral-7b"},{"title":"Mistral Small 3 | Mistral AI","url":"https://mistral.ai/news/mistral-small-3"},{"title":"unsloth/Mistral-Small-24B-Base-2501-bnb-4bit · Hugging Face","url":"https://huggingface.co/unsloth/Mistral-Small-24B-Base-2501-bnb-4bit"},{"title":"mistralai/Mistral-7B-v0.1 · Hugging Face","url":"https://huggingface.co/mistralai/Mistral-7B-v0.1"},{"title":"Mistral Small 3.1 | Mistral AI","url":"https://mistral.ai/news/mistral-small-3-1"},{"title":"unsloth/Mistral-Small-24B-Base-2501 · Hugging Face","url":"https://huggingface.co/unsloth/Mistral-Small-24B-Base-2501"},{"title":"Introducing Mistral 3 | Mistral AI","url":"https://mistral.ai/news/mistral-3"},{"title":"mistralai/Mistral-Small-24B-Instruct-2501 · Hugging Face","url":"https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501"},{"title":"mistralai/Mistral-Small-3.1-24B-Instruct-2503 · Hugging Face","url":"https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503"},{"title":"Mistral Docs","url":"https://docs.mistral.ai/getting-started/models/benchmark/"}]

Based on the search results, here's what I found about Mistral Small 3:

**Model Details:**
Mistral Small 3 boasts 24B parameters and achieves state-of-the-art capabilities comparable to larger models. Note that the search results do not show a 7B version of Mistral Small 3 - the model has 24 billion parameters, not 7 billion.

**Release Date:**
The model was released in January 2025. The version labeled "2501" (indicating January 2025) is referenced in the HuggingFace documentation.

**MMLU Benchmark:**
Mistral Small 3 achieves over 81% accuracy on MMLU and 150 tokens/s latency, making it currently the most efficient model of its category.

**HuggingFace Availability:**
Mistral Small 3.1 is available to download on the HuggingFace website in both Base and Instruct versions.

It's worth noting that there's also a newer version - Mistral Small 3.1 (2503) builds upon Mistral Small 3 (2501) and adds state-of-the-art vision understanding and enhances long context capabilities up to 128k tokens.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4ee4359-30d5-4e24-bde6-599dc46f678a",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "38b9b3a1-1103-43b6-8f54-ed0b3a5d0e9f",
  "sourceToolAssistantUUID": "a4ee4359-30d5-4e24-bde6-599dc46f678a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-18T07:08:26.022Z_

<details><summary>↩ Tool result · `toolu_01BEXBM5kKmHtDWYvbzuaCNo`</summary>

```text
Web search results for query: "Qwen2.5 7B 14B base model huggingface benchmark training tokens 2024 2025"

Links: [{"title":"2025-01-06 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2412.15115"},{"title":"Qwen/Qwen2.5-7B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-7B-Instruct"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Qwen/Qwen2.5-7B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-7B"},{"title":"Qwen/Qwen2.5-Coder-14B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-Coder-14B"},{"title":"Qwen/Qwen2.5-14B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-14B"},{"title":"Qwen/Qwen2.5-Coder-14B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct"},{"title":"Qwen/Qwen2.5-14B-Instruct-1M · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-14B-Instruct-1M"},{"title":"Qwen/Qwen2.5-7B-Instruct-1M · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-1M"},{"title":"Qwen/Qwen2.5-14B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-14B-Instruct"}]

Based on the search results, here's information about Qwen2.5 7B and 14B base models:

## Model Overview

Qwen2.5 includes pre-trained and instruction-tuned models of 7 sizes, including 0.5B, 1.5B, 3B, 7B, 14B, 32B, and 72B.

## Training Tokens

The pre-training data increased from 7 trillion tokens to 18 trillion tokens, with focus on knowledge, coding, and mathematics. For the Qwen2.5-Coder variant, the training tokens were scaled up into 5.5 trillion including source code, text-code grounding, Synthetic data, etc.

## Benchmark Performance

For the 7B model, Qwen2.5-7B demonstrates significant improvements achieving 74.2 on MMLU, 49.8 on MATH, and 57.9 on coding tasks like HumanEval.

The Qwen2.5-7B model surpasses its predecessors and counterparts in numerous benchmarks, despite having fewer non-embedding parameters.

## Capabilities

Qwen2.5 exhibits competitive performance in instruction following, multilingual knowledge, and mathematical reasoning, aligning well with models of comparable size.

The models are available on Hugging Face for both base and instruction-tuned variants, with long-context support up to 128K tokens and ability to generate up to 8K tokens.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd530fe0-1303-4c5a-b4cc-868e6733658c",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "345b54ef-b5d2-451b-ac21-6d010923bb36",
  "sourceToolAssistantUUID": "cd530fe0-1303-4c5a-b4cc-868e6733658c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T07:08:26.333Z_

<details><summary>↩ Tool result · `toolu_01C7Fe9WLPEiE62JR9v3UxUK`</summary>

```text
Web search results for query: "DeepSeek V2 V3 7B 14B base model huggingface distilled 2025"

Links: [{"title":"deepseek-ai/DeepSeek-V3 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V3"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-7B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"},{"title":"deepseek-ai/DeepSeek-V4-Pro · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-32B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B"},{"title":"The Complete Guide to DeepSeek Models: V3, R1, V4 and Beyond","url":"https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond"},{"title":"DeepSeek-V2 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/deepseek_v2"},{"title":"DeepSeek-V3 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/deepseek_v3"},{"title":"DeepSeek-V3.2 Release | DeepSeek API Docs","url":"https://api-docs.deepseek.com/news/news251201"},{"title":"deepseek-ai/DeepSeek-R1 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1"},{"title":"deepseek-ai/DeepSeek-V3-Base · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V3-Base"}]

Based on the search results, here's what I found about DeepSeek models and their distilled variants on Hugging Face:

## DeepSeek-V3 Base Model

DeepSeek-V3 is a strong Mixture-of-Experts (MoE) language model with 671B total parameters with 37B activated for each token. To achieve efficient inference and cost-effective training, DeepSeek-V3 adopts Multi-head Latent Attention (MLA) and DeepSeekMoE architectures, which were thoroughly validated in DeepSeek-V2.

## Distilled Models (2025)

DeepSeek has open-sourced distilled 1.5B, 7B, 8B, 14B, 32B, and 70B checkpoints based on Qwen2.5 and Llama3 series to the community. 

Specifically, DeepSeek-R1-Distill-Qwen-1.5B, DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Qwen-14B and DeepSeek-R1-Distill-Qwen-32B are derived from Qwen-2.5 series, which are originally licensed under Apache 2.0 License, and now finetuned with 800k samples curated with DeepSeek-R1. DeepSeek-R1-Distill-Llama-8B is derived from Llama3.1-8B-Base and is originally licensed under llama3.1 license.

DeepSeek-R1-Zero & DeepSeek-R1 are trained based on DeepSeek-V3-Base.

All of these models are available on Hugging Face in the deepseek-ai organization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a8a1211-f929-4a36-bcda-ed7161cdbf75",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "b1c49772-7f7b-4ffd-ae57-0e888e098e81",
  "sourceToolAssistantUUID": "6a8a1211-f929-4a36-bcda-ed7161cdbf75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-18T07:08:26.428Z_

<details><summary>↩ Tool result · `toolu_018hzzuzEY7t4QqDTYYBH7z2`</summary>

```text
Web search results for query: "OLMo 2 7B 13B base model huggingface 2025 release Allen AI"

Links: [{"title":"OLMo 2 - a allenai Collection","url":"https://huggingface.co/collections/allenai/olmo-2"},{"title":"allenai/OLMo-2-1124-13B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B"},{"title":"allenai/OLMo-2-1124-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B"},{"title":"allenai/OLMo-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-7B"},{"title":"OLMo 2: The best fully open language model to date | Ai2","url":"https://allenai.org/blog/olmo2"},{"title":"allenai/OLMo-2-1124-13B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B-Instruct-GGUF"},{"title":"OLMo release notes | Ai2","url":"https://allenai.org/olmo/release-notes"},{"title":"allenai/OLMo-2-1124-7B-RM · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B-RM"},{"title":"allenai/OLMo-2-0325-32B-SFT · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0325-32B-SFT"},{"title":"allenai/Olmo-3-1025-7B · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-1025-7B"}]

Based on the search results, here's what I found about OLMo 2:

## OLMo 2 Release Overview

OLMo 2 is a new family of 7B and 13B models trained on up to 5T tokens. These models are on par with or better than equivalently-sized fully-open models, and competitive with open-weight models from Meta and Mistral on English academic benchmarks.

## Base Models on Hugging Face

The base models are available on Hugging Face:
- OLMo 2 7B base version is available for use as foundation for post-training.
- OLMo 2 13B base version is available for use as foundation for post-training.

## Training Details

OLMo 2 features a 9-point increase in MMLU compared to the original OLMo 7B model, with these gains coming from training on OLMo-mix-1124 and Dolmino-mix-1124 datasets and staged training approach.

## Performance

OLMo 2 7B outperforms LLama-3.1 8B and OLMo 2 13B outperforms Qwen 2.5 7B despite its lower total training FLOPs.

The models were released in late 2024 and are available on the Allen AI Hugging Face collection with various variants including instruct, quantized, and reward model versions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24f8f430-5ced-484e-80b5-98c60e9f2a2e",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "16168af6-e7d6-49ba-a82d-8940b5d1e15b",
  "sourceToolAssistantUUID": "24f8f430-5ced-484e-80b5-98c60e9f2a2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-18T07:08:29.546Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MpHfia2WRFeUQy4wHja4aT`</summary>

```json
{
  "query": "Qwen3 8B base benchmark MMLU ARC HellaSwag scores 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16168af6-e7d6-49ba-a82d-8940b5d1e15b",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cYXt5rjq2NNqdA4M2t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7700b55f-8397-4e8d-8425-866a5d9edfd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114AWbUGQKLmWDBLHRjt7Kt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5698,
      "cache_read_input_tokens": 22906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5698,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 31 · 2026-05-18T07:08:30.478Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WXvDfUz4XiJ4CMQJ8m4QtY`</summary>

```json
{
  "query": "Gemma 3 12B base pretrained benchmark scores MMLU 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7700b55f-8397-4e8d-8425-866a5d9edfd1",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cYXt5rjq2NNqdA4M2t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f626d3ed-da2c-4b1e-9172-6e4c55fb9d4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114AWbUGQKLmWDBLHRjt7Kt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5698,
      "cache_read_input_tokens": 22906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5698,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 32 · 2026-05-18T07:08:30.953Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xa8pxNSg9F2NoK2gFojeKR`</summary>

```json
{
  "query": "Llama 3.3 8B base model huggingface release 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f626d3ed-da2c-4b1e-9172-6e4c55fb9d4c",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cYXt5rjq2NNqdA4M2t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ecf0f50f-a483-4f40-9258-e92aadbd5ce1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114AWbUGQKLmWDBLHRjt7Kt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5698,
      "cache_read_input_tokens": 22906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5698,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 33 · 2026-05-18T07:08:31.890Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011MS5A9Ji6Wabu5HpP6mQPR`</summary>

```json
{
  "query": "Falcon 3 7B 10B base model huggingface 2024 2025 TII"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecf0f50f-a483-4f40-9258-e92aadbd5ce1",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cYXt5rjq2NNqdA4M2t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92b8a650-062c-480c-be76-e2af2288f7b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114AWbUGQKLmWDBLHRjt7Kt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5698,
      "cache_read_input_tokens": 22906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5698,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 34 · 2026-05-18T07:08:32.165Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K1z6xz2rXfA93LvH4PakR9`</summary>

```json
{
  "query": "InternLM3 8B base model huggingface 2025 Shanghai AI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92b8a650-062c-480c-be76-e2af2288f7b5",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cYXt5rjq2NNqdA4M2t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d37c9dc-a375-46ef-8184-b72f25a697ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114AWbUGQKLmWDBLHRjt7Kt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5698,
      "cache_read_input_tokens": 22906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5698,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 35 · 2026-05-18T07:08:36.138Z_

<details><summary>↩ Tool result · `toolu_01MpHfia2WRFeUQy4wHja4aT`</summary>

```text
Web search results for query: "Qwen3 8B base benchmark MMLU ARC HellaSwag scores 2025"

Links: [{"title":"An Empirical Study of Qwen3 Quantization","url":"https://arxiv.org/html/2505.02214v1"},{"title":"An empirical study of Qwen3 quantization | Visual Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44267-026-00114-4"},{"title":"eaddario/Qwen3-8B-GGUF · Hugging Face","url":"https://huggingface.co/eaddario/Qwen3-8B-GGUF"},{"title":"Swallow LLM Leaderboard","url":"https://swallow-llm.github.io/leaderboard/about.en.html"},{"title":"Top LLM Benchmarks Explained: MMLU, HellaSwag, BBH, and Beyond - Confident AI","url":"https://www.confident-ai.com/blog/llm-benchmarks-mmlu-hellaswag-and-beyond"},{"title":"LLM Benchmarks Compared: MMLU, HumanEval, GSM8K and More (2026)","url":"https://www.lxt.ai/blog/llm-benchmarks/"},{"title":"We Benchmarked 12 Small Language Models Across 8 Tasks to Find the Best Base Model for Fine-Tuning — distil labs","url":"https://www.distillabs.ai/blog/we-benchmarked-12-small-language-models-across-8-tasks-to-find-the-best-base-model-for-fine-tuning/"},{"title":"LLM Benchmarks 2026 - Compare AI Benchmarks and Tests","url":"https://llm-stats.com/benchmarks"},{"title":"Qwen3 8B - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/qwen3-8b-instruct"},{"title":"LLM Benchmark Wars 2025–2026: Performance, Cost, Speed, and Value | RankSaga","url":"https://ranksaga.com/blog/llm-benchmark-wars-2025-2026/"}]

Based on the search results, I found relevant benchmark information about Qwen3-8B-Base. Here's what I found:

Qwen-8B's MMLU score is 74.7 in its full precision form, though this appears to be from a quantization study focused on performance degradation at lower bit widths.

The search results include detailed benchmark data from an empirical study of Qwen3 quantization published in early 2025. Zero-shot accuracy is evaluated across reasoning benchmarks including ARC-Easy, ARC-Challenge, and HellaSwag, with 5-shot MMLU also examined. However, the specific individual scores for MMLU, ARC, and HellaSwag for the Qwen3-8B-Base model are referenced in tables within the research paper but not fully extracted in the search results provided.

For more complete and specific benchmark scores for Qwen3-8B-Base across MMLU, ARC, and HellaSwag, you would want to access the full research paper directly at the ArXiv link (https://arxiv.org/html/2505.02214v1), where Table 2 and related tables contain the detailed per-benchmark scores.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7700b55f-8397-4e8d-8425-866a5d9edfd1",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "84ab487b-308b-45c9-a029-4283625fb83f",
  "sourceToolAssistantUUID": "7700b55f-8397-4e8d-8425-866a5d9edfd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-18T07:08:36.863Z_

<details><summary>↩ Tool result · `toolu_01WXvDfUz4XiJ4CMQJ8m4QtY`</summary>

```text
Web search results for query: "Gemma 3 12B base pretrained benchmark scores MMLU 2025"

Links: [{"title":"Gemma 3 Technical Report","url":"https://arxiv.org/html/2503.19786v1"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"Gemma 3 12B Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/gemma-3-12b-it"},{"title":"(PDF) Gemma 3 Technical Report","url":"https://www.researchgate.net/publication/390175982_Gemma_3_Technical_Report"},{"title":"Google: Gemma 3 12B Review | Pricing, Benchmarks & Capabilities (2026) | Design for Online","url":"https://designforonline.com/ai-models/google-gemma-3-12b/"},{"title":"Gemma 3 model card | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core/model_card_3"},{"title":"Gemma 3 — Google DeepMind","url":"https://deepmind.google/models/gemma/gemma-3/"},{"title":"Gemma 3 12B - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/gemma-3-12b"},{"title":"Google's Gemma 3: Features, Benchmarks, Performance and Implementation","url":"https://www.analyticsvidhya.com/blog/2025/03/gemma-3/"},{"title":"LLM Benchmarks March 2025","url":"https://www.timetoact-group.at/en/insights/llm-benchmarks/llm-benchmarks-march-2025"}]

Based on the search results, I found benchmark information for Gemma 3 12B, though the specific MMLU score for the base pretrained model wasn't directly listed in these results. Here's what I found:

**Gemma 3 12B Benchmark Performance:**

For the Gemma 3 12B model, MMLU-Pro shows a score of 59.5%. This is from the instruction-tuned (IT) variant.

The search results primarily focus on the instruction-tuned (IT) versions of Gemma 3 rather than the base pretrained models. Gemma 3 has been evaluated across benchmarks like MMLU-Pro (27B: 67.5), but specific base model MMLU scores for the 12B variant were not included in the available search results.

For context on the multilingual performance of the base models, the Gemma 3 12B base model showed a Global-MMLU-Lite (GMMLU) score of 69.4, which is a multilingual variant of MMLU.

If you need the specific MMLU score for the Gemma 3 12B base pretrained model, you may want to consult the full Gemma 3 Technical Report directly, as the search results focused more on the instruction-tuned variants and other benchmark types.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f626d3ed-da2c-4b1e-9172-6e4c55fb9d4c",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "3c172a62-41a5-43de-ac71-3a2f5c40b0a8",
  "sourceToolAssistantUUID": "f626d3ed-da2c-4b1e-9172-6e4c55fb9d4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-18T07:08:37.869Z_

<details><summary>↩ Tool result · `toolu_01Xa8pxNSg9F2NoK2gFojeKR`</summary>

```text
Web search results for query: "Llama 3.3 8B base model huggingface release 2024 2025"

Links: [{"title":"meta-llama/Llama-3.1-8B · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-3.1-8B"},{"title":"meta-llama (Meta Llama)","url":"https://huggingface.co/meta-llama"},{"title":"meta-llama/Meta-Llama-3-8B · Hugging Face","url":"https://huggingface.co/meta-llama/Meta-Llama-3-8B"},{"title":"meta-llama/Llama-3.2-3B · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-3.2-3B"},{"title":"NousResearch/Meta-Llama-3-8B · Hugging Face","url":"https://huggingface.co/NousResearch/Meta-Llama-3-8B"},{"title":"meta-llama/Llama-3.2-3B-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct"},{"title":"meta-llama/Llama-3.3-70B-Instruct · Release of an 8B model?","url":"https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/discussions/11"},{"title":"nvidia/Llama-3.1-8B-Instruct-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Llama-3.1-8B-Instruct-NVFP4"},{"title":"meta-llama/Llama-Guard-3-8B · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-Guard-3-8B"},{"title":"QuantFactory/Meta-Llama-3-8B-GGUF · Hugging Face","url":"https://huggingface.co/QuantFactory/Meta-Llama-3-8B-GGUF"}]

Based on the search results, here's what I found regarding Llama 3.3 8B base model on Hugging Face:

Llama 3.3 is mentioned in Meta's Hugging Face collection, with the 71B model being updated on December 21, 2024. However, the search results indicate that as of late 2024, users were waiting for an 8B model release.

The Llama 3.3 8B Instruct model became available through third-party APIs (like OpenRouter) in mid-2025, but based on the search results provided, there is no direct mention of an official Llama 3.3 8B base model being released on Hugging Face's main meta-llama repository during 2024-2025.

The search results primarily show information about:
- Llama 3.1 8B released July 23, 2024
- Llama 3 8B released April 18, 2024
- Llama 3.2 released September 25, 2024

If you're looking for the Llama 3.3 8B base model specifically, you may need to check if it's available through alternative sources or wait for an official release on the main Hugging Face repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecf0f50f-a483-4f40-9258-e92aadbd5ce1",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "035d2258-e952-42fc-9d20-4be4f083287b",
  "sourceToolAssistantUUID": "ecf0f50f-a483-4f40-9258-e92aadbd5ce1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-18T07:08:39.096Z_

<details><summary>↩ Tool result · `toolu_01K1z6xz2rXfA93LvH4PakR9`</summary>

```text
Web search results for query: "InternLM3 8B base model huggingface 2025 Shanghai AI"

Links: [{"title":"GitHub - InternLM/InternLM: Official release of InternLM series (InternLM, InternLM2, InternLM2.5, InternLM3). · GitHub","url":"https://github.com/InternLM/InternLM"},{"title":"internlm/internlm3-8b-instruct · Hugging Face","url":"https://huggingface.co/internlm/internlm3-8b-instruct"},{"title":"InternLM3 Open Source: Achieving High-Performance Models with 4T Data | by OpenMMLab | Medium","url":"https://openmmlab.medium.com/internlm3-open-source-achieving-high-performance-models-with-4t-data-c18e94bd5c6a"},{"title":"internlm/internlm3-8b-instruct-gguf · Hugging Face","url":"https://huggingface.co/internlm/internlm3-8b-instruct-gguf"},{"title":"internlm (Intern Large Models)","url":"https://huggingface.co/internlm"},{"title":"InternLM3 - a internlm Collection","url":"https://huggingface.co/collections/internlm/internlm3"},{"title":"Internlm3 8b Instruct - a Hugging Face Space by internlm","url":"https://huggingface.co/spaces/internlm/internlm3-8b-instruct"},{"title":"HuggingFace Transformers 😊 — InternLM","url":"https://internlm.readthedocs.io/en/latest/inference/huggingface_transformers.html"},{"title":"internlm3-8b-instruct | AI Model Details","url":"https://www.aimodels.fyi/models/huggingFace/internlm3-8b-instruct-internlm"},{"title":"Intern-ai","url":"https://internlm.intern-ai.org.cn/"}]

Based on the search results, here's what I found about InternLM3 8B:

## Overview

InternLM3 has open-sourced an 8-billion parameter instruction model, InternLM3-8B-Instruct, designed for general-purpose usage and advanced reasoning. InternLM is a conversational language model that is developed by Shanghai AI Laboratory.

## Release Date

On January 15, Shanghai AI Lab announced a major upgrade to the InternLM model with the release of InternLM3.

## Key Features

InternLM3 offers state-of-the-art performance on reasoning and knowledge-intensive tasks surpassing models like Llama3.1-8B and Qwen2.5-7B. InternLM3 is trained on only 4 trillion high-quality tokens, saving more than 75% of the training cost compared to other LLMs of similar scale.

InternLM3 supports both the deep thinking mode for solving complicated reasoning tasks via the long chain-of-thought and the normal response mode for fluent user interactions.

## HuggingFace Availability

The model is available on HuggingFace at `internlm/internlm3-8b-instruct`, where you can find documentation for loading and using the model with various frameworks like transformers, vLLM, and Ollama.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d37c9dc-a375-46ef-8184-b72f25a697ff",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "2d91b21f-c1b7-4fda-bdc2-032567dd2f1a",
  "sourceToolAssistantUUID": "5d37c9dc-a375-46ef-8184-b72f25a697ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-18T07:08:40.310Z_

<details><summary>↩ Tool result · `toolu_011MS5A9Ji6Wabu5HpP6mQPR`</summary>

```text
Web search results for query: "Falcon 3 7B 10B base model huggingface 2024 2025 TII"

Links: [{"title":"tiiuae/Falcon3-7B-Base · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-7B-Base"},{"title":"Welcome to the Falcon 3 Family of Open Models!","url":"https://huggingface.co/blog/falcon3"},{"title":"tiiuae/Falcon3-10B-Base · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-10B-Base"},{"title":"TII launches world’s most powerful SLMs under 13B parameters","url":"https://www.middleeastainews.com/p/tii-launches-most-powerful-slm"},{"title":"Falcon 3: UAE’s Technology Innovation Institute Launches World’s most Powerful Small AI Models that can also be run on Light Infrastructures, including Laptops | Technology Innovation Institute","url":"https://www.tii.ae/news/falcon-3-uaes-technology-innovation-institute-launches-worlds-most-powerful-small-ai-models"},{"title":"tiiuae/Falcon3-7B-Instruct · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-7B-Instruct"},{"title":"tiiuae/Falcon3-10B-Instruct · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-10B-Instruct"},{"title":"Technology Innovation Institute TII-UAE Just Released Falcon 3: A Family of Open-Source AI Models with 30 New Model Checkpoints from 1B to 10B - MarkTechPost","url":"https://www.marktechpost.com/2024/12/17/technology-innovation-institute-tii-uae-just-released-falcon-3-a-family-of-open-source-ai-models-with-30-new-model-checkpoints-from-1b-to-10b/"},{"title":"tiiuae/Falcon3-3B-Base · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-3B-Base"},{"title":"tiiuae/Falcon3-Mamba-7B-Instruct · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-Mamba-7B-Instruct"}]

Based on the search results, here's what I found about Falcon 3 models:

## Overview

Falcon3 is a family of decoder-only large language models under 10 billion parameters, developed by Technology Innovation Institute (TII) in Abu Dhabi. The Falcon 3 family of Open Foundation Models was released in December 2024 and includes four AI model sizes: Falcon3-1B, -3B, -7B and -10B, which are all available as open-source code via the Hugging Face community website.

## Base Models: 7B and 10B

**Falcon3-7B-Base:**
- Supports 4 languages (English, French, Spanish, Portuguese) and a context length up to 32K
- Pretrained on 14 Teratokens of datasets comprising web, code, STEM, high quality and multilingual data using 1024 H100 GPU chips

**Falcon3-10B-Base:**
- Depth up-scaled from Falcon3-7B-Base with continual pretraining on 2 Teratokens of datasets comprising web, code, STEM, high quality and multilingual data using 1024 H100 GPU chips
- Achieves state-of-the-art zero-shot and few-shot performance for models under 13B parameters

## Performance and Features

Falcon3-7B achieves competitive scores on reasoning and math, while Falcon3-10B demonstrates further improvements. All transformer-based Falcon3 models are compatible with Llama architecture allowing better integration in the AI ecosystem.

## Future Developments

In January 2025, enhanced models featuring multimodal capabilities including image, video, and audio support will be released, along with a full technical report.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92b8a650-062c-480c-be76-e2af2288f7b5",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "d6b6dc85-ed2a-4c5d-9bd1-6ece0ec17c4f",
  "sourceToolAssistantUUID": "92b8a650-062c-480c-be76-e2af2288f7b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-18T07:08:43.496Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RktS9DiqVzLTK4YEBv2EeG`</summary>

```json
{
  "query": "MAP-Neo 7B base model huggingface 2025 fully open source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6b6dc85-ed2a-4c5d-9bd1-6ece0ec17c4f",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cZZFTvznFabu2MzaDc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d04739c-0864-4a1a-8154-acd7c9e3b45e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015eA9GFtGku2xt3U61mvLh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 907,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 28604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3979,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 41 · 2026-05-18T07:08:43.955Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ACyQrSBPWCD2N3Mre5XZSf`</summary>

```json
{
  "query": "SmolLM2 7B base model huggingface 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d04739c-0864-4a1a-8154-acd7c9e3b45e",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cZZFTvznFabu2MzaDc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73bb96b7-cc9e-426d-a080-d58810397a0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015eA9GFtGku2xt3U61mvLh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 907,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 28604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3979,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 42 · 2026-05-18T07:08:44.426Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GtWvkHwkNKo59yLKkcpKxt`</summary>

```json
{
  "query": "Phi-4 14B MMLU benchmark score base model december 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73bb96b7-cc9e-426d-a080-d58810397a0b",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cZZFTvznFabu2MzaDc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e11d45ad-45f2-46e1-9006-abab827e4d7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015eA9GFtGku2xt3U61mvLh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 907,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 28604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3979,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 43 · 2026-05-18T07:08:45.418Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014WyPuvfMMbBafWjPzucQQQ`</summary>

```json
{
  "query": "Yi-1.5 9B base model huggingface 01.AI 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e11d45ad-45f2-46e1-9006-abab827e4d7f",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cZZFTvznFabu2MzaDc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9c30d4d-df3c-4636-83ab-ee3f50ae8a7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015eA9GFtGku2xt3U61mvLh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 907,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 28604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3979,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 44 · 2026-05-18T07:08:45.666Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013VUt3RhDzXqDuaJT3s8rFu`</summary>

```json
{
  "query": "Mistral Nemo 12B base model huggingface 2024 benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9c30d4d-df3c-4636-83ab-ee3f50ae8a7c",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cZZFTvznFabu2MzaDc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96e8385f-2ceb-4e4a-99ec-035f22b2c1e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015eA9GFtGku2xt3U61mvLh8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 907,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 28604,
      "output_tokens": 285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3979
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 907,
          "output_tokens": 285,
          "cache_read_input_tokens": 28604,
          "cache_creation_input_tokens": 3979,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3979,
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

_source line 45 · 2026-05-18T07:08:49.140Z_

<details><summary>↩ Tool result · `toolu_01GtWvkHwkNKo59yLKkcpKxt`</summary>

```text
Web search results for query: "Phi-4 14B MMLU benchmark score base model december 2024"

Links: [{"title":"Qwen3.5-27B vs Phi-4: When Twice the Parameters Is Not Twice as Obvious | Awesome Agents","url":"https://awesomeagents.ai/tools/qwen-3-5-27b-vs-phi-4/"},{"title":"Microsoft PHI-4: A 14B Parameter Model That Rivals Models 5x Its Size - Developers Digest","url":"https://www.developersdigest.tech/blog/microsoft-phi-4-guide"},{"title":"Phi-4: Small Language Models That Pack a Punch | Microsoft Community Hub","url":"https://techcommunity.microsoft.com/blog/educatordeveloperblog/phi-4-small-language-models-that-pack-a-punch/4464167"},{"title":"Microsoft releases full Phi-4 model with weights under MIT license","url":"https://the-decoder.com/microsoft-releases-full-phi-4-model-with-weights-under-mit-license/"},{"title":"Phi-4 Local Setup: Microsoft's 14B Reasoning on 12GB GPUs | Local AI Master","url":"https://localaimaster.com/blog/phi-4-local-setup"},{"title":"Phi-4 Technical Report","url":"https://arxiv.org/html/2412.08905v1"},{"title":"Phi-4 - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/phi-4"},{"title":"Phi 4 by Microsoft: Complete Performance Review & Benchmarks (2025)","url":"https://airank.dev/models/phi-4"},{"title":"microsoft/phi-4 · Hugging Face","url":"https://huggingface.co/microsoft/phi-4"},{"title":"Phi-4","url":"https://ai.azure.com/catalog/models/Phi-4"}]

Based on the search results, here is the MMLU benchmark score for Phi-4 14B base model from December 2024:

On MMLU (a broad test of knowledge across 57 subjects), Phi-4 scores 84.8%. Microsoft released Phi-4 in December 2024, and this MMLU score of 84.8 puts Phi-4 ahead of Llama-3.3-70B on the same evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e11d45ad-45f2-46e1-9006-abab827e4d7f",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "13b43e15-0fbb-4622-be4f-6ee14fa600f3",
  "sourceToolAssistantUUID": "e11d45ad-45f2-46e1-9006-abab827e4d7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-18T07:08:50.910Z_

<details><summary>↩ Tool result · `toolu_01ACyQrSBPWCD2N3Mre5XZSf`</summary>

```text
Web search results for query: "SmolLM2 7B base model huggingface 2025"

Links: [{"title":"HuggingFaceTB/SmolLM2-1.7B · Hugging Face","url":"https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B"},{"title":"HuggingFaceTB/SmolLM2-1.7B-Instruct · Hugging Face","url":"https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct"},{"title":"HuggingFaceTB/SmolLM2-1.7B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct-GGUF"},{"title":"SmolLM2 - a HuggingFaceTB Collection","url":"https://huggingface.co/collections/HuggingFaceTB/smollm2"},{"title":"tensorblock/SmolLM2-1.7B-GGUF · Hugging Face","url":"https://huggingface.co/tensorblock/SmolLM2-1.7B-GGUF"},{"title":"HuggingFaceTB/SmolLM2-1.7B-Instruct-16k · Hugging Face","url":"https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct-16k"},{"title":"HuggingFaceTB/SmolLM2-135M · Hugging Face","url":"https://huggingface.co/HuggingFaceTB/SmolLM2-135M"},{"title":"bartowski/SmolLM2-1.7B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/bartowski/SmolLM2-1.7B-Instruct-GGUF"},{"title":"GitHub - huggingface/smollm: Everything about the SmolLM and SmolVLM family of models · GitHub","url":"https://github.com/huggingface/smollm"},{"title":"HuggingFaceTB/SmolVLM-Instruct · Hugging Face","url":"https://huggingface.co/HuggingFaceTB/SmolVLM-Instruct"}]

Based on the search results, here's what I found about SmolLM2 models:

## Overview

SmolLM2 is a family of compact language models available in three sizes: 135M, 360M, and 1.7B parameters. Note that there isn't a 7B variant in the SmolLM2 family—the largest model is 1.7B.

## Base Model Details

These models are capable of solving a wide range of tasks while being lightweight enough to run on-device. The 1.7B variant demonstrates significant advances over its predecessor SmolLM1-1.7B, particularly in instruction following, knowledge, reasoning, and mathematics. It was trained on 11 trillion tokens using a diverse dataset combination: FineWeb-Edu, DCLM, The Stack, along with new mathematics and coding datasets.

## Hugging Face Availability

The base model is available on Hugging Face as **HuggingFaceTB/SmolLM2-1.7B**. The research was published in 2025 with the paper titled "SmolLM2: When Smol Goes Big -- Data-Centric Training of a Small Language Model" (arXiv:2502.02737).

There are also instruct versions and other variants available on Hugging Face Hub, such as the SmolLM2-1.7B-Instruct model with extended context support.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73bb96b7-cc9e-426d-a080-d58810397a0b",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "a987eb7f-52b8-472b-9569-056aa9531102",
  "sourceToolAssistantUUID": "73bb96b7-cc9e-426d-a080-d58810397a0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-18T07:08:51.197Z_

<details><summary>↩ Tool result · `toolu_01RktS9DiqVzLTK4YEBv2EeG`</summary>

```text
Web search results for query: "MAP-Neo 7B base model huggingface 2025 fully open source"

Links: [{"title":"m-a-p/neo_7b · Hugging Face","url":"https://huggingface.co/m-a-p/neo_7b"},{"title":"Paper page - MAP-Neo: Highly Capable and Transparent Bilingual Large \nLanguage Model Series","url":"https://huggingface.co/papers/2405.19327"},{"title":"GitHub - multimodal-art-projection/MAP-NEO · GitHub","url":"https://github.com/multimodal-art-projection/MAP-NEO"},{"title":"m-a-p/neo_7b_instruct_v0.1 · Hugging Face","url":"https://huggingface.co/m-a-p/neo_7b_instruct_v0.1"},{"title":"m-a-p/neo_7b_sft_v0.1 · Hugging Face","url":"https://huggingface.co/m-a-p/neo_7b_sft_v0.1"},{"title":"MAP-NEO/README.md at main · multimodal-art-projection/MAP-NEO","url":"https://github.com/multimodal-art-projection/MAP-NEO/blob/main/README.md"},{"title":"GitHub - huggingface/open-r1: Fully open reproduction of DeepSeek-R1 · GitHub","url":"https://github.com/huggingface/open-r1"},{"title":"nvidia/OpenMath-Nemotron-7B · Hugging Face","url":"https://huggingface.co/nvidia/OpenMath-Nemotron-7B"},{"title":"neulab/Pangea-7B · Hugging Face","url":"https://huggingface.co/neulab/Pangea-7B"},{"title":"m-a-p/YuE-s1-7B-anneal-en-cot · Hugging Face","url":"https://huggingface.co/m-a-p/YuE-s1-7B-anneal-en-cot"}]

Based on the search results, here's what I found about MAP-Neo 7B:

## MAP-Neo 7B Overview

MAP-Neo is a fully open-sourced bilingual LLM with 7B parameters that achieves performance comparable to existing state-of-the-art LLMs.

## Key Characteristics

MAP-NEO is a fully open-sourced Large Language Model that includes the pretraining data, a data processing pipeline (Matrix), pretraining scripts, and alignment code, and is trained from scratch on 4.5T English and Chinese tokens, exhibiting performance comparable to LLaMA2 7B.

## Complete Transparency

All details to reproduce MAP-Neo are open-sourced, including the cleaned pre-training corpus, data cleaning pipeline, checkpoints, and well-optimized training/evaluation framework. The comprehensive release includes the final and intermediate checkpoints, a self-trained tokenizer, the pre-training corpus, and an efficient, stable optimized pre-training codebase.

## Performance

The MAP-Neo model delivers proprietary-model-like performance in challenging tasks such as reasoning, mathematics, and coding, outperforming its peers of similar size.

## Availability

The model is available on Hugging Face under the m-a-p organization, with both base and fine-tuned variants available. Commercial usage is permitted under the model's terms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d04739c-0864-4a1a-8154-acd7c9e3b45e",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "d19f1b94-6fa1-4439-b673-c107ad586eb8",
  "sourceToolAssistantUUID": "0d04739c-0864-4a1a-8154-acd7c9e3b45e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-18T07:08:52.575Z_

<details><summary>↩ Tool result · `toolu_013VUt3RhDzXqDuaJT3s8rFu`</summary>

```text
Web search results for query: "Mistral Nemo 12B base model huggingface 2024 benchmark"

Links: [{"title":"nvidia/Mistral-NeMo-12B-Base · Hugging Face","url":"https://huggingface.co/nvidia/Mistral-NeMo-12B-Base"},{"title":"nvidia/Mistral-NeMo-12B-Instruct · Hugging Face","url":"https://huggingface.co/nvidia/Mistral-NeMo-12B-Instruct"},{"title":"Mistral NeMo | Mistral AI","url":"https://mistral.ai/news/mistral-nemo"},{"title":"Mistral NeMo 12B | Open Laboratory","url":"https://openlaboratory.com/models/mistral-nemo-12b/"},{"title":"Mistral NeMo 12B — A comprehensive look at the next-generation enterprise AI model | UnfoldAI","url":"https://unfoldai.com/mistral-nemo-12b-review/"},{"title":"mistralai/Mistral-Nemo-Base-2407 · Hugging Face","url":"https://huggingface.co/mistralai/Mistral-Nemo-Base-2407"},{"title":"mistralai/Mistral-Nemo-Instruct-2407 · Hugging Face","url":"https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407"},{"title":"starble-dev/Mistral-Nemo-12B-Instruct-2407-GGUF · Hugging Face","url":"https://huggingface.co/starble-dev/Mistral-Nemo-12B-Instruct-2407-GGUF"},{"title":"EasierAI/Mistral-NeMo-12B · Hugging Face","url":"https://huggingface.co/EasierAI/Mistral-NeMo-12B"},{"title":"README.md · nvidia/Mistral-NeMo-12B-Base at main","url":"https://huggingface.co/nvidia/Mistral-NeMo-12B-Base/blob/main/README.md"}]

Based on the search results, here's comprehensive information about the Mistral Nemo 12B base model and its 2024 benchmarks:

## Model Overview

Mistral-NeMo-12B-Base is a Large Language Model (LLM) composed of 12B parameters, trained jointly by NVIDIA and Mistral AI. The model was trained between May 2024 and June 2024.

## Key Capabilities

Mistral-NeMo-12B-Base is a completion model intended for use in over 80+ programming languages and designed for global, multilingual applications. It is fast, trained on function-calling, has a large context window, and is particularly strong in English, French, German, Spanish, Italian, Portuguese, Chinese, Japanese, Korean, Arabic, and Hindi.

## Benchmark Performance

The model shows strong performance across major evaluation benchmarks:

Zero-shot performance on HellaSwag reaches 83.5%, and the model delivers 76.8% accuracy on Winogrande. On comprehension tasks, it scores 73.8% on TriviaQA (five-shot) and 68.0% on MMLU (five-shot).

Mistral NeMo 12B exhibits competitive results on established language model evaluation benchmarks, frequently surpassing other models in its parameter range such as Gemma 2 9B and Llama 3 8B.

## Availability

Weights are hosted on HuggingFace both for the base and for the instruct models. The base model is available at the official Mistral AI repository on Hugging Face.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96e8385f-2ceb-4e4a-99ec-035f22b2c1e6",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "b7fce39d-6c0b-44a0-a69e-dad583b12659",
  "sourceToolAssistantUUID": "96e8385f-2ceb-4e4a-99ec-035f22b2c1e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-18T07:08:52.700Z_

<details><summary>↩ Tool result · `toolu_014WyPuvfMMbBafWjPzucQQQ`</summary>

```text
Web search results for query: "Yi-1.5 9B base model huggingface 01.AI 2024 2025"

Links: [{"title":"01-ai (01-ai)","url":"https://huggingface.co/01-ai"},{"title":"GitHub - 01-ai/Yi-1.5: Yi-1.5 is an upgraded version of Yi, delivering stronger performance in coding, math, reasoning, and instruction-following capability. · GitHub","url":"https://github.com/01-ai/Yi-1.5"},{"title":"01-ai/Yi-1.5-9B · Hugging Face","url":"https://huggingface.co/01-ai/Yi-1.5-9B"},{"title":"Paper page - Yi: Open Foundation Models by 01.AI","url":"https://huggingface.co/papers/2403.04652"},{"title":"01-ai/Yi-1.5-9B-Chat-16K · Hugging Face","url":"https://huggingface.co/01-ai/Yi-1.5-9B-Chat-16K"},{"title":"Yi 1.5 34B | Open Laboratory","url":"https://openlaboratory.ai/models/yi-1_5-34b"},{"title":"01-ai/Yi-Coder-1.5B-Chat · Hugging Face","url":"https://huggingface.co/01-ai/Yi-Coder-1.5B-Chat"},{"title":"Models – Hugging Face","url":"https://huggingface.co/models"},{"title":"01-ai/Yi-1.5-9B · extended context","url":"https://huggingface.co/01-ai/Yi-1.5-9B/discussions/1"},{"title":"01-ai/Yi-1.5-9B-32K · Hugging Face","url":"https://huggingface.co/01-ai/Yi-1.5-9B-32K"}]

Based on the search results, here's what I found about the Yi-1.5 9B base model from 01.AI on Hugging Face:

## Overview
Yi-1.5 is an upgraded version of Yi, delivering stronger performance in coding, math, reasoning, and instruction-following capability. The Yi-1.5 series models were open-sourced on 2024-05-13, further improving coding, math, reasoning, and instruction-following abilities.

## Model Availability
The Yi 1.5 family includes multiple parameter scales and configurations, such as 6B, 9B, and 34B models, in both base and chat forms, and offers long-context and multimodal versions. The Yi-1.5-9B base model is available on Hugging Face at the official 01-ai organization.

## Performance
Yi-1.5-9B is the top performer among similarly sized open-source models. The base model achieves reported scores of 76.3 on MMLU, 54.3 on BBH, and 81.4 on C-Eval.

## Architecture
Yi 1.5 34B is a 34.4 billion parameter decoder-only Transformer language model featuring Grouped-Query Attention and SwiGLU activations, trained on 3.1 trillion bilingual tokens.

The model also has extended context variants available, including the Yi-1.5-9B-32K version that supports longer input sequences.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9c30d4d-df3c-4636-83ab-ee3f50ae8a7c",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "fdeb63c5-cc8f-4859-b4c6-2c3a0637b563",
  "sourceToolAssistantUUID": "f9c30d4d-df3c-4636-83ab-ee3f50ae8a7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-18T07:08:55.658Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0115L1pj43aEA4fKbYJrBRAJ`</summary>

```json
{
  "query": "Qwen3 14B base model huggingface benchmark 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdeb63c5-cc8f-4859-b4c6-2c3a0637b563",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9caUBtaS6BoxsE5Hhbf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0fcf659c-decf-426d-970b-1acf08805792",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TTynS6ZSPsB6GQxX3BZuu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 974,
      "cache_creation_input_tokens": 4681,
      "cache_read_input_tokens": 32583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4681,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 51 · 2026-05-18T07:08:59.422Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014pNScz91HxxLov4auhkB2G`</summary>

```json
{
  "query": "OLMo 2 7B 13B benchmark MMLU scores training tokens 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fcf659c-decf-426d-970b-1acf08805792",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9caUBtaS6BoxsE5Hhbf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b2448c2-9b31-427b-8d2d-6daf361e0ed9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TTynS6ZSPsB6GQxX3BZuu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 974,
      "cache_creation_input_tokens": 4681,
      "cache_read_input_tokens": 32583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4681,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 52 · 2026-05-18T07:08:59.506Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WgBEHpo4QiDgevicEsueoh`</summary>

```json
{
  "query": "Gemma 2 9B base model huggingface benchmark 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b2448c2-9b31-427b-8d2d-6daf361e0ed9",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9caUBtaS6BoxsE5Hhbf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "432ab22e-7e66-4ad1-808d-57d03c4ee5a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TTynS6ZSPsB6GQxX3BZuu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 974,
      "cache_creation_input_tokens": 4681,
      "cache_read_input_tokens": 32583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4681,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 53 · 2026-05-18T07:08:59.606Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LJZdd6cx826GbwmJ13aSYQ`</summary>

```json
{
  "query": "StarCoder2 7B 15B base model huggingface 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "432ab22e-7e66-4ad1-808d-57d03c4ee5a6",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9caUBtaS6BoxsE5Hhbf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70a5f23f-dabc-4ad9-acb8-50c87a274f5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TTynS6ZSPsB6GQxX3BZuu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 974,
      "cache_creation_input_tokens": 4681,
      "cache_read_input_tokens": 32583,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4681
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 974,
          "output_tokens": 232,
          "cache_read_input_tokens": 32583,
          "cache_creation_input_tokens": 4681,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4681,
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

_source line 54 · 2026-05-18T07:09:02.681Z_

<details><summary>↩ Tool result · `toolu_0115L1pj43aEA4fKbYJrBRAJ`</summary>

```text
Web search results for query: "Qwen3 14B base model huggingface benchmark 2025"

Links: [{"title":"Qwen/Qwen3-14B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B"},{"title":"Qwen/Qwen3-14B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B-Base"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"nvidia/Qwen3-14B-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Qwen3-14B-NVFP4"},{"title":"unsloth/Qwen3-14B-Base · Hugging Face","url":"https://huggingface.co/unsloth/Qwen3-14B-Base"},{"title":"Qwen/Qwen3-8B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B-Base"},{"title":"nvidia/Qwen3-14B-FP8 · Hugging Face","url":"https://huggingface.co/nvidia/Qwen3-14B-FP8"},{"title":"Quantized Models for Qwen/Qwen3-14B – Hugging Face","url":"https://huggingface.co/models?other=base_model%3Aquantized%3AQwen%2FQwen3-14B"},{"title":"GitHub - QwenLM/Qwen3: Qwen3 is the large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/qwen3"}]

Based on the search results, here's what I found about the Qwen3 14B base model and its 2025 benchmarks:

## Model Specifications

Qwen3-14B-Base has 14.8B parameters (13.2B non-embedding parameters), 40 layers, 40 attention heads (Q) and 8 for KV with Group Query Attention (GQA), and a context length of 32,768 tokens.

## Benchmark Performance

Qwen3-14B-Base performs as well as Qwen2.5-32B-Base, and notably outperforms larger Qwen2.5 models in areas like STEM, coding, and reasoning.

More specifically, Qwen3-14B-Base achieves very competitive results compared to Qwen2.5-32B-Base, demonstrating significant efficiency gains.

## Training and Performance

Qwen3 is pre-trained on 36 trillion tokens across 119 languages, tripling the language coverage of Qwen2.5, with a rich mix of high-quality data including coding, STEM, reasoning, book, multilingual, and synthetic data.

## Documentation Reference

Detailed evaluation results are reported in a blog post, and transformers version 4.51.0 or higher is required to use the model. The official technical report was published in May 2025 (arXiv:2505.09388).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fcf659c-decf-426d-970b-1acf08805792",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "6bd2b8c4-1bdd-42ad-bda2-07259b3a46e6",
  "sourceToolAssistantUUID": "0fcf659c-decf-426d-970b-1acf08805792",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-18T07:09:06.243Z_

<details><summary>↩ Tool result · `toolu_014pNScz91HxxLov4auhkB2G`</summary>

```text
Web search results for query: "OLMo 2 7B 13B benchmark MMLU scores training tokens 2024"

Links: [{"title":"OLMo 1.7–7B: A 24 point improvement on MMLU | Ai2","url":"https://allenai.org/blog/olmo-1-7-7b-a-24-point-improvement-on-mmlu-92b43f7d269d"},{"title":"OLMo 2: The best fully open language model to date | Ai2","url":"https://allenai.org/blog/olmo2"},{"title":"OLMo release notes | Ai2","url":"https://allenai.org/olmo/release-notes"},{"title":"2 OLMo 2 Furious OLMo Team Pete Walsh 1 Luca Soldaini 1 Dirk Groeneveld 1","url":"https://arxiv.org/pdf/2501.00656"},{"title":"allenai/OLMo-2-1124-7B-Instruct Free Chat Online - skywork.ai - Skywork ai","url":"https://skywork.ai/blog/models/allenai-olmo-2-1124-7b-instruct-free-chat-online-skywork-ai/"},{"title":"OLMo 2 7B vs 13B: Research Performance and Resource Analysis | Markaicode","url":"https://markaicode.com/vs/olmo-2-7b-vs-13b/"},{"title":"OLMo 1.7–7B: A 24 point improvement on MMLU | by Ai2 | Ai2 Blog | Medium","url":"https://medium.com/ai2-blog/olmo-1-7-7b-a-24-point-improvement-on-mmlu-92b43f7d269d"},{"title":"allenai/OLMo-2-1124-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B"},{"title":"(PDF) 2 OLMo 2 Furious","url":"https://www.researchgate.net/publication/387671074_2_OLMo_2_Furious"},{"title":"allenai/OLMo-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-7B"}]

Based on the search results, here's the key information about OLMo 2 7B and 13B models:

## Training Tokens

OLMo 2 is a family of 7B and 13B models trained on up to 5T tokens. More specifically, OLMo 2 7B is trained for approximately one epoch on the first-stage dataset, while OLMo 2 13B is trained for 1.2 epochs up to 5T tokens.

## MMLU Benchmark Scores

OLMo 2 achieved MMLU scores of 63.7 for the 7B model and 67.5 for the 13B model. This represents a 9-point increase in MMLU compared to the original OLMo 7B model.

## Training Approach

OLMo 2 is pretrained in two stages using a curriculum approach. In the first stage, which covers over 90% of the total pretraining budget, the models use OLMo-Mix-1124, a collection of approximately 3.9 trillion tokens sourced from DCLM, Dolma, Starcoder, and Proof Pile II. The second stage curates a mixture of high-quality web data and domain-specific content, consisting of 843 billion tokens total, sampled to create mixes of 50 billion, 100 billion, and 300 billion tokens.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b2448c2-9b31-427b-8d2d-6daf361e0ed9",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "1f1ca039-5b2f-4854-9ac5-e1595d6ac861",
  "sourceToolAssistantUUID": "0b2448c2-9b31-427b-8d2d-6daf361e0ed9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-18T07:09:07.013Z_

<details><summary>↩ Tool result · `toolu_01WgBEHpo4QiDgevicEsueoh`</summary>

```text
Web search results for query: "Gemma 2 9B base model huggingface benchmark 2024"

Links: [{"title":"google/gemma-2-9b · Hugging Face","url":"https://huggingface.co/google/gemma-2-9b"},{"title":"RedHatAI/gemma-2-9b-it-FP8 · Hugging Face","url":"https://huggingface.co/RedHatAI/gemma-2-9b-it-FP8"},{"title":"google/gemma-2-2b · Hugging Face","url":"https://huggingface.co/google/gemma-2-2b"},{"title":"bartowski/gemma-2-9b-it-GGUF · Hugging Face","url":"https://huggingface.co/bartowski/gemma-2-9b-it-GGUF"},{"title":"neuralmagic/gemma-2-9b-it-FP8 · Hugging Face","url":"https://huggingface.co/neuralmagic/gemma-2-9b-it-FP8"},{"title":"Gemma 2: Improving Open Language Models at a Practical Size","url":"https://arxiv.org/html/2408.00118v2"},{"title":"google/gemma-2-2b-it · Hugging Face","url":"https://huggingface.co/google/gemma-2-2b-it"},{"title":"Gemma2 · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/gemma2"},{"title":"google/gemma-2-27b · Hugging Face","url":"https://huggingface.co/google/gemma-2-27b"},{"title":"google/recurrentgemma-9b · Hugging Face","url":"https://huggingface.co/google/recurrentgemma-9b"}]

Based on the search results, here's information about the Gemma 2 9B base model and its benchmark performance:

## Model Overview

Gemma 2 is a family of language models with pretrained and instruction-tuned variants, available in 2B, 9B, 27B parameters. The 9B model was trained with 8 trillion tokens, and the 2B and 9B models are trained with knowledge distillation.

## Architecture

The architecture features interleaved local attention (4096 tokens) and global attention (8192 tokens) and grouped-query attention (GQA) to increase inference performance.

## Benchmark Performance

The search results include benchmark information for the Gemma 2 9B instruction-tuned variant. The unquantized gemma-2-9b-it model achieves an average score of 73.23 on the OpenLLM benchmark (version 1).

Additionally, there was a massive improvement in the models compared to previous versions, by up to 10% in some benchmarks for the 9B model. Gemma 2 significantly advances state-of-the-art performance relative to comparable-scale open models and are even competitive with some models more than twice their size.

The Gemma 2 9B model was released in July 2024 and is available on Hugging Face for download and use.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "432ab22e-7e66-4ad1-808d-57d03c4ee5a6",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "64e2c99d-153c-4ca4-a63a-ddab7fddc48d",
  "sourceToolAssistantUUID": "432ab22e-7e66-4ad1-808d-57d03c4ee5a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-18T07:09:07.107Z_

<details><summary>↩ Tool result · `toolu_01LJZdd6cx826GbwmJ13aSYQ`</summary>

```text
Web search results for query: "StarCoder2 7B 15B base model huggingface 2024 2025"

Links: [{"title":"Starcoder2 · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/starcoder2"},{"title":"bigcode/starcoder2-15b · Hugging Face","url":"https://huggingface.co/bigcode/starcoder2-15b"},{"title":"GitHub - bigcode-project/starcoder2: Home of StarCoder2! · GitHub","url":"https://github.com/bigcode-project/starcoder2"},{"title":"bigcode/starcoder2-7b · Hugging Face","url":"https://huggingface.co/bigcode/starcoder2-7b"},{"title":"Starcoder2","url":"https://huggingface.co/docs/transformers/v4.46.0/model_doc/starcoder2"},{"title":"StarCoder2: AI-Powered Code Generation by ServiceNow, Hugging Face and NVIDIA | by My Social | 𝐀𝐈 𝐦𝐨𝐧𝐤𝐬.𝐢𝐨 | Medium","url":"https://medium.com/aimonks/starcoder2-ai-powered-code-generation-by-servicenow-hugging-face-and-nvidia-7f51763af0e6"},{"title":"blog/starcoder2.md at main · huggingface/blog","url":"https://github.com/huggingface/blog/blob/main/starcoder2.md"},{"title":"bigcode (BigCode)","url":"https://huggingface.co/bigcode"},{"title":"FineTuning StarCoder2 on Google Colab T4 GPU","url":"https://medium.com/codex/finetuning-starcoder2-on-google-colab-t4-gpu-a7a416efde4e"},{"title":"StarCoder 2 is a code-generating AI that runs on most GPUs | TechCrunch","url":"https://techcrunch.com/2024/02/28/starcoder-2-is-a-code-generating-ai-that-runs-on-most-gpus/"}]

Based on the search results, here's what I found about StarCoder2 7B and 15B base models on Hugging Face:

## Release Information

StarCoder2 was released on February 29, 2024 and added to Hugging Face Transformers on February 28, 2024.

## Model Overview

StarCoder2 is a family of open LLMs for code and comes in 3 different sizes with 3B, 7B and 15B parameters.

## StarCoder2-7B Details

StarCoder2-7B is a 7B parameter model trained on 17 programming languages from The Stack v2, with opt-out requests excluded. The model uses Grouped Query Attention, a context window of 16,384 tokens with a sliding window attention of 4,096 tokens, and was trained using the Fill-in-the-Middle objective on 3.5+ trillion tokens.

## StarCoder2-15B Details

StarCoder2-15B is a 15B parameter model trained on 600+ programming languages from The Stack v2, with opt-out requests excluded. The model uses Grouped Query Attention, a context window of 16,384 tokens with a sliding window attention of 4,096 tokens, and was trained using the Fill-in-the-Middle objective on 4+ trillion tokens.

## Licensing

The models are licensed under the BigCode OpenRAIL-M v1 license agreement.

Both models are available on Hugging Face Hub under the `bigcode` organization and can be accessed via the model IDs `bigcode/starcoder2-7b` and `bigcode/starcoder2-15b`.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70a5f23f-dabc-4ad9-acb8-50c87a274f5c",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "aefd724c-ba73-4983-8a17-41b126011cde",
  "sourceToolAssistantUUID": "70a5f23f-dabc-4ad9-acb8-50c87a274f5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-18T07:09:09.855Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FhcwKwrrSymitQTfCHJokP`</summary>

```json
{
  "query": "Falcon3 7B 10B MMLU benchmark scores training data 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aefd724c-ba73-4983-8a17-41b126011cde",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cbXoTRALYVth35kGfz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a86e11a-43ac-4ab3-8e06-edfe3149383b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZH1gmWYngF8M89n3ztzXs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4942,
      "cache_read_input_tokens": 37264,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4942,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 59 · 2026-05-18T07:09:10.780Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NFkezhfys1NQ7yj79NC3ii`</summary>

```json
{
  "query": "Gemma 3 release date January March 2025 google 4B 12B"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a86e11a-43ac-4ab3-8e06-edfe3149383b",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cbXoTRALYVth35kGfz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1fe5c4c2-385c-4806-84b9-3c21fba2f167",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZH1gmWYngF8M89n3ztzXs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4942,
      "cache_read_input_tokens": 37264,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4942,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 60 · 2026-05-18T07:09:11.313Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PaC8nq3HA8YvDRJXxDUTaM`</summary>

```json
{
  "query": "OLMo 3 7B base model allenai huggingface 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1fe5c4c2-385c-4806-84b9-3c21fba2f167",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cbXoTRALYVth35kGfz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05d50d94-2c16-49b8-b4e9-cb16d282f365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZH1gmWYngF8M89n3ztzXs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4942,
      "cache_read_input_tokens": 37264,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4942,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 61 · 2026-05-18T07:09:11.694Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RP9eAduRdF9AwM9oR6ovxG`</summary>

```json
{
  "query": "Llama 3.1 8B base MMLU benchmark training tokens 15T 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05d50d94-2c16-49b8-b4e9-cb16d282f365",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cbXoTRALYVth35kGfz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3684f2f-cb36-4c44-8de9-677abd897496",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZH1gmWYngF8M89n3ztzXs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4942,
      "cache_read_input_tokens": 37264,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4942
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 237,
          "cache_read_input_tokens": 37264,
          "cache_creation_input_tokens": 4942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4942,
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

_source line 62 · 2026-05-18T07:09:16.812Z_

<details><summary>↩ Tool result · `toolu_01NFkezhfys1NQ7yj79NC3ii`</summary>

```text
Web search results for query: "Gemma 3 release date January March 2025 google 4B 12B"

Links: [{"title":"Gemma releases | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/releases"},{"title":"Gemma 3 - D-Central","url":"https://d-central.tech/ai/model/gemma-3/"},{"title":"Gemma (language model) - Wikipedia","url":"https://en.wikipedia.org/wiki/Gemma_(language_model)"},{"title":"Gemma 3 4B Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/gemma-3-4b-it"},{"title":"Gemma 3 4B – Try & Compare | Roboflow Playground","url":"https://playground.roboflow.com/models/google/gemma-3-4b"},{"title":"Gemma 3 12B Model Specs, Costs & Benchmarks (April 2026) | Galaxy.ai","url":"https://blog.galaxy.ai/model/gemma-3-12b-it"},{"title":"Introducing Gemma 3: The Developer Guide - Google Developers Blog","url":"https://developers.googleblog.com/en/introducing-gemma3/"},{"title":"Gemma 3 12B - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/gemma-3-12b"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"Notes on Google’s Gemma 3","url":"https://simonwillison.net/2025/Mar/12/gemma-3/"}]

Based on the search results, here's what I found about Gemma 3's release:

Gemma 3 was released on March 12, 2025. This was not in January, but rather in March 2025 as part of your search query timeframe.

Google DeepMind's March 2025 Gemma family includes vision-capable models (4B+) with 128K context and official quantization-aware 4-bit variants.

**Available Model Sizes:**
Gemma 3 was offered in 1, 4, 12, and 27 billion parameter sizes with support for over 140 languages. So the 4B and 12B models you mentioned in your query were indeed released as part of the Gemma 3 family.

**Key Features:**
As multimodal models, they support both text and image input. Additionally, Gemma 3 handles context windows up to 128k tokens, understands over 140 languages, and offers improved math, reasoning, and chat capabilities, including structured outputs and function calling.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1fe5c4c2-385c-4806-84b9-3c21fba2f167",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "f8d23114-f9b9-4ec6-8e40-1a7bc5c1650b",
  "sourceToolAssistantUUID": "1fe5c4c2-385c-4806-84b9-3c21fba2f167",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-18T07:09:18.134Z_

<details><summary>↩ Tool result · `toolu_01PaC8nq3HA8YvDRJXxDUTaM`</summary>

```text
Web search results for query: "OLMo 3 7B base model allenai huggingface 2025"

Links: [{"title":"allenai/Olmo-3-1025-7B · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-1025-7B"},{"title":"allenai/Olmo-3-1125-32B · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-1125-32B"},{"title":"Olmo 3 - a allenai Collection","url":"https://huggingface.co/collections/allenai/olmo-3"},{"title":"allenai/Olmo-3-7B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-Instruct"},{"title":"allenai/Olmo-3-7B-Think · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-Think"},{"title":"allenai/Olmo-3.1-32B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3.1-32B-Instruct"},{"title":"allenai/Olmo-3.1-32B-Think · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3.1-32B-Think"},{"title":"allenai/Olmo-3-7B-RL-Zero-Math · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Math"},{"title":"Mungert/Olmo-3-1025-7B-GGUF · Hugging Face","url":"https://huggingface.co/Mungert/Olmo-3-1025-7B-GGUF"},{"title":"allenai/Olmo-3-7B-Think-DPO · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-Think-DPO"}]

Based on the web search results, here's what I found about the OLMo 3 7B base model from Allen AI on Hugging Face:

## Overview

OLMo 3 is a new family of 7B and 32B models, with a suite that includes Base, Instruct, and Think variants. The Base models were trained using a staged training approach.

## Training Details

The main dataset used is dolma3_6T-mix-1025, consisting of 5.93T tokens with coverage of 97.53%+ of total pretraining budget. The training mix composition includes 20% code, 28% web pages, 19% math, 14% QA, 8% thinking, 6% instruction, and 5% PDFs.

## Model Availability

The base model is available on Hugging Face at `allenai/Olmo-3-1025-7B`. The research paper and details are available at https://allenai.org/papers/olmo3.

## Licensing and Usage

This model is licensed under Apache 2.0 and is intended for research and educational use in accordance with AI2's Responsible Use Guidelines.

The search results show this is a relatively recent release, with information from January 2026 regarding the October 2025 model version.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05d50d94-2c16-49b8-b4e9-cb16d282f365",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "4627875b-9362-4861-a566-bcc0a864a120",
  "sourceToolAssistantUUID": "05d50d94-2c16-49b8-b4e9-cb16d282f365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-18T07:09:19.207Z_

<details><summary>↩ Tool result · `toolu_01FhcwKwrrSymitQTfCHJokP`</summary>

```text
Web search results for query: "Falcon3 7B 10B MMLU benchmark scores training data 2024"

Links: [{"title":"Welcome to the Falcon 3 Family of Open Models! | Falcon","url":"https://falcon-lm.github.io/blog/falcon-3/"},{"title":"Welcome to the Falcon 3 Family of Open Models!","url":"https://huggingface.co/blog/falcon3"},{"title":"🐺🐦‍⬛ LLM Comparison/Test: DeepSeek-V3, QVQ-72B-Preview, Falcon3 10B, Llama 3.3 70B, Nemotron 70B in my updated MMLU-Pro CS benchmark","url":"https://huggingface.co/blog/wolfram/llm-comparison-test-2025-01-02"},{"title":"tiiuae/Falcon3-7B-Base · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-7B-Base"},{"title":"tiiuae/Falcon3-1B-Base · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-1B-Base"},{"title":"Falcon LLM Architecture: Deep Dive into its Design and Performance | SaM Solutions","url":"https://sam-solutions.com/blog/falcon-llm-architecture/"},{"title":"Experience Advanced AI Anywhere with Falcon 3's Lightweight Design","url":"https://www.analyticsvidhya.com/blog/2024/12/falcon-3/"},{"title":"TII launches world’s most powerful SLMs under 13B parameters","url":"https://www.middleeastainews.com/p/tii-launches-most-powerful-slm"},{"title":"Falcon 3 series sets new benchmarks for open-source LLMs on a single GPU","url":"https://the-decoder.com/abu-dhabis-tii-releases-falcon-3-setting-new-benchmarks-for-efficient-open-source-ai-models/"},{"title":"Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance | Falcon","url":"https://falcon-lm.github.io/blog/falcon-h1/"}]

Based on the search results, here's the information about Falcon3 7B and 10B MMLU benchmark scores and training data:

## MMLU Benchmark Scores

Falcon3-7B-Base achieved scores of 67.4 on MMLU and 39.2 on MMLU-PRO, while Falcon3-10B-Base achieved 73.1 on MMLU and 42.5 on MMLU-PRO respectively.

## Training Data

The 7B model was trained on 14 trillion tokens using 1024 H100 GPU chips, leveraging web, code, STEM, and curated high-quality multilingual data. The 10B model was created by upscaling the 7B model with continued pre-training using 2 trillion tokens of high-quality data.

Falcon 3 was trained in four major languages: English, Spanish, Portuguese, and French.

## Performance Context

Falcon3-10B-Base achieves state-of-the-art zero-shot and few-shot performance for models under 13B parameters. Falcon3-7B-Base demonstrates top performance, on par with Qwen2.5-7B, among models under the 9B scale.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a86e11a-43ac-4ab3-8e06-edfe3149383b",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "2accc153-854e-41c8-9449-5e2d5e25d2a5",
  "sourceToolAssistantUUID": "5a86e11a-43ac-4ab3-8e06-edfe3149383b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-18T07:09:20.089Z_

<details><summary>↩ Tool result · `toolu_01RP9eAduRdF9AwM9oR6ovxG`</summary>

```text
Web search results for query: "Llama 3.1 8B base MMLU benchmark training tokens 15T 2024"

Links: [{"title":"Llama 3.1 8B Instruct - NGC Catalog - NVIDIA","url":"https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/llama-3_1-8b-instruct-nemo"},{"title":"MLPerf Training Adds Llama 3.1 8B Benchmark - MLCommons","url":"https://mlcommons.org/2025/10/training-llama-3-1-8b/"},{"title":"Llama 3.1 8B - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/llama-3-1-instruct-8b"},{"title":"Introducing Meta Llama 3: The most capable openly available LLM to date","url":"https://ai.meta.com/blog/meta-llama-3/"},{"title":"Llama 3.1","url":"https://www.llama.com/llama3_1/"},{"title":"Llama 3's Performance Benchmark Values Explained | by Ingrid Stevens | Medium","url":"https://medium.com/@ingridwickstevens/more-llm-acronyms-an-explainer-on-llama-3s-performance-benchmark-values-36722c6dcabb"},{"title":"Llama 3.2: Revolutionizing edge AI and vision with open, customizable models","url":"https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/"},{"title":"llama-models/models/llama3_1/eval_details.md at main · meta-llama/llama-models","url":"https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/eval_details.md"},{"title":"Meta's New Llama 3.1 AI Model: Use Cases & Benchmark","url":"https://research.aimultiple.com/meta-llama/"},{"title":"Llama 3.1 Guide: What to know about Meta's new 405B model and its data","url":"https://kili-technology.com/large-language-models-llms/llama-3-1-guide-what-to-know-about-meta-s-new-405b-model-and-its-data"}]

Based on the search results, I found relevant information about Llama 3.1 8B's training and MMLU benchmark performance:

## Training Tokens

Llama 3.1 used about 15T multilingual tokens, compared to 1.8T tokens for Llama 2. This confirms the 15T token training mentioned in your query.

## MMLU Benchmark Performance

For the Llama 3.1 8B base model specifically:

- For the pre-trained 8B model, the micro average MMLU score is 65.6 for the 5-shot config

The search results also show that Llama 3.1 scores 89 on the MMLU Chat (0-shot) benchmark, though this appears to be referring to the instruction-tuned version rather than the base model.

The official Meta evaluation details indicate that different evaluation configurations produce different scores, with the base pre-trained 8B model achieving 65.6 micro average on MMLU using a 5-shot configuration.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3684f2f-cb36-4c44-8de9-677abd897496",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "99957111-683b-4f5a-9112-203578f7e63a",
  "sourceToolAssistantUUID": "f3684f2f-cb36-4c44-8de9-677abd897496",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-18T07:09:23.218Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P5bNa3iv6SNa5xQKDh7j6P`</summary>

```json
{
  "query": "Qwen2.5 14B MMLU benchmark base model training tokens"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99957111-683b-4f5a-9112-203578f7e63a",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9ccVJAopQPFjyCQ1ieZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ba850e7-2e1f-4ac2-bb22-91c600edd9b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Tv4BNUpe83tjC98U8uGKF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3658,
      "cache_read_input_tokens": 42206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3658,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 67 · 2026-05-18T07:09:23.702Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FHqgLBPxKo5AdbHgYqnHfu`</summary>

```json
{
  "query": "Gemma 4 base model release 2026 huggingface google"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ba850e7-2e1f-4ac2-bb22-91c600edd9b0",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9ccVJAopQPFjyCQ1ieZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca2a55d1-56fd-4a00-a028-6886208d7935",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Tv4BNUpe83tjC98U8uGKF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3658,
      "cache_read_input_tokens": 42206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3658,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 68 · 2026-05-18T07:09:24.207Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CAcCQMJzPrL5gxnKWUDARF`</summary>

```json
{
  "query": "Falcon H1 7B 14B hybrid model huggingface 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca2a55d1-56fd-4a00-a028-6886208d7935",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9ccVJAopQPFjyCQ1ieZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f17553e-61aa-440d-975f-31c86133a7ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Tv4BNUpe83tjC98U8uGKF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3658,
      "cache_read_input_tokens": 42206,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3658
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 42206,
          "cache_creation_input_tokens": 3658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3658,
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

_source line 69 · 2026-05-18T07:09:28.942Z_

<details><summary>↩ Tool result · `toolu_01P5bNa3iv6SNa5xQKDh7j6P`</summary>

```text
Web search results for query: "Qwen2.5 14B MMLU benchmark base model training tokens"

Links: [{"title":"Qwen2.5-LLM: Extending the boundary of LLMs | Qwen","url":"https://qwenlm.github.io/blog/qwen2.5-llm/"},{"title":"2025-01-06 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2412.15115"},{"title":"Qwen2.5 14B Instruct Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/qwen-2.5-14b-instruct"},{"title":"2025-01-26 Qwen2.5-1M Technical Report","url":"https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-1M/Qwen2_5_1M_Technical_Report.pdf"},{"title":"Qwen 2.5 14B | Open Laboratory","url":"https://openlaboratory.ai/models/qwen-2_5-14b"},{"title":"Technical Report Qwen2.5-Coder Technical Report Binyuan Hui* Jian Yang*","url":"https://arxiv.org/pdf/2409.12186"},{"title":"Qwen2.5-Coder Technical Report","url":"https://arxiv.org/html/2409.12186v3"},{"title":"Qwen 2.5","url":"https://qwen2.org/qwen2-5/"},{"title":"Qwen2.5-LLM: Extending the Boundary of LLMs - Alibaba Cloud Community","url":"https://www.alibabacloud.com/blog/601786"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"}]

Based on the search results, here's what I found about Qwen2.5-14B:

## MMLU Benchmark Performance

The Qwen2.5-14B model achieves a score of 79.7 on MMLU, demonstrating strong performance on this general language understanding benchmark.

## Training Tokens

The pre-training dataset was expanded from 7 trillion tokens to a maximum of 18 trillion tokens. This represents the training data size used for the Qwen2.5 series models, including the 14B variant.

## Additional Context

Qwen2.5 models, including the 14B variant, are pretrained on a large-scale corpus comprising up to 18 trillion tokens, with the pretraining data covering diverse domains and curated for high data quality.

The Qwen2.5-14B base model demonstrates competitive performance, particularly excelling in general language understanding tasks as evidenced by its MMLU score.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ba850e7-2e1f-4ac2-bb22-91c600edd9b0",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "fda321d4-5bb5-4482-9a02-70db3508cb14",
  "sourceToolAssistantUUID": "2ba850e7-2e1f-4ac2-bb22-91c600edd9b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-18T07:09:29.885Z_

<details><summary>↩ Tool result · `toolu_01FHqgLBPxKo5AdbHgYqnHfu`</summary>

```text
Web search results for query: "Gemma 4 base model release 2026 huggingface google"

Links: [{"title":"google/gemma-4-26B-A4B · Hugging Face","url":"https://huggingface.co/google/gemma-4-26B-A4B"},{"title":"Gemma 4 model overview | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core"},{"title":"Gemma 4 — Google DeepMind","url":"https://deepmind.google/models/gemma/gemma-4/"},{"title":"google/gemma-4-E4B-it · Hugging Face","url":"https://huggingface.co/google/gemma-4-E4B-it"},{"title":"google/gemma-4-26B-A4B-it · Hugging Face","url":"https://huggingface.co/google/gemma-4-26B-A4B-it"},{"title":"What Is Google Gemma 4? Architecture, Benchmarks, and Why It Matters | WaveSpeed Blog","url":"https://wavespeed.ai/blog/posts/what-is-google-gemma-4/"},{"title":"google/gemma-4-31B · Hugging Face","url":"https://huggingface.co/google/gemma-4-31B"},{"title":"google/gemma-4-E4B · Hugging Face","url":"https://huggingface.co/google/gemma-4-E4B"},{"title":"Gemma4 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/gemma4"},{"title":"Gemma 4: Byte for byte, the most capable open models","url":"https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/"}]

I've found comprehensive information about the Gemma 4 base model release. Here's what I found:

## Gemma 4 Release

On April 2, 2026, Google DeepMind released Gemma 4 — four open-weight models built from the same research lineage as Gemini 3, now shipped under the Apache 2.0 license.

## Model Variants

The models are available in four distinct sizes: E2B, E4B, 26B A4B, and 31B. This release includes open-weights models in both pre-trained and instruction-tuned variants.

## Key Capabilities

Gemma 4 models are multimodal, handling text and image input (with audio supported on small models) and generating text output. Gemma 4 features a context window of up to 256K tokens and maintains multilingual support in over 140 languages.

## Availability

You can download Gemma 4 models from Kaggle and Hugging Face. The models are available on Hugging Face under Google's official collection, with both base and instruction-tuned variants for each size.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca2a55d1-56fd-4a00-a028-6886208d7935",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "0cc50757-b08c-4b73-8a7b-d5b9bcaf46dc",
  "sourceToolAssistantUUID": "ca2a55d1-56fd-4a00-a028-6886208d7935",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-18T07:09:33.222Z_

<details><summary>↩ Tool result · `toolu_01CAcCQMJzPrL5gxnKWUDARF`</summary>

```text
Web search results for query: "Falcon H1 7B 14B hybrid model huggingface 2025"

Links: [{"title":"tiiuae/Falcon-H1R-7B · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon-H1R-7B"},{"title":"Introducing Falcon H1R 7B","url":"https://huggingface.co/blog/tiiuae/falcon-h1r-7b"},{"title":"tiiuae/Falcon-H1R-7B-GGUF · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon-H1R-7B-GGUF"},{"title":"Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance | Falcon","url":"https://falcon-lm.github.io/blog/falcon-h1/"},{"title":"Falcon-H1R: Pushing the Reasoning Frontiers with a Hybrid Model for Efficient Test-Time Scaling | Falcon","url":"https://falcon-lm.github.io/blog/falcon-h1r-7b/"},{"title":"FalconH1","url":"https://huggingface.co/docs/transformers/en/model_doc/falcon_h1"},{"title":"tiiuae/Falcon-H1-7B-Instruct · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon-H1-7B-Instruct"},{"title":"[2507.22448] Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance","url":"https://arxiv.org/abs/2507.22448"},{"title":"Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance","url":"https://huggingface.co/blog/tiiuae/falcon-h1"},{"title":"tiiuae/Falcon-H1-7B-Base · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon-H1-7B-Base"}]

Based on the search results, here's information about the Falcon H1 hybrid models:

## Falcon-H1 Hybrid Model Family

Falcon-H1 is a series of large language models featuring hybrid architecture designs that combines Transformer-based attention with State Space Models (SSMs), known for superior long-context memory and computational efficiency.

### Model Sizes and Availability

Falcon-H1 is released in multiple configurations, including base and instruction-tuned variants at 0.5B, 1.5B, 1.5B-deep, 3B, 7B, and 34B parameters.

### Key Features

- The amount of attention and mamba heads can be adjusted independently, allowing for an optimal attention/SSM ratio, which enables faster inference, lower memory usage, and strong generalization across tasks.

- Falcon-H1 models support up to 256K context length, enabling applications in long-document processing, multi-turn dialogue, and long-range reasoning.

- The models support 18 languages natively, including Arabic, Czech, German, English, Spanish, French, Hindi, Italian, Japanese, Korean, Dutch, Polish, Portuguese, Romanian, Russian, Swedish, Urdu, and Chinese.

### Performance

The flagship Falcon-H1-34B matches or outperforms models up to 70B scale, while using fewer parameters and less data. Smaller models show similar trends: the Falcon-H1-1.5B-Deep rivals current leading 7B-10B models, and Falcon-H1-0.5B performs comparably to typical 7B models from 2024.

### Falcon-H1R Reasoning Variant

Falcon-H1R-7B is a reasoning-specialized model that was trained via cold-start supervised fine-tuning with long reasoning traces and further enhanced by scaling RL with GRPO.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f17553e-61aa-440d-975f-31c86133a7ae",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a07b72467ddf2db7b",
  "type": "user",
  "uuid": "f82af57f-e711-4be3-a599-837f9f2ab522",
  "sourceToolAssistantUUID": "9f17553e-61aa-440d-975f-31c86133a7ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 72 · 2026-05-18T07:11:31.910Z_

Now I have comprehensive data. Here is the structured compilation of all findings.

---

## Open-Source Base LLMs (7B-14B Parameters) Released 2024-2026

### 1. Qwen3-8B-Base (Alibaba)

| Field | Detail |
|---|---|
| **Full Name** | Qwen3-8B-Base |
| **HuggingFace Repo** | `Qwen/Qwen3-8B-Base` |
| **Parameters** | 8B (7.6B non-embedding) |
| **Release Date** | May 2025 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | 36T tokens, 119 languages |
| **Benchmarks** | MMLU ~74.7; performs on par with Qwen2.5-14B-Base. Top HumanEval (76.0) under 8B. Strong CJK multilingual. |

### 2. Qwen3-14B-Base (Alibaba)

| Field | Detail |
|---|---|
| **Full Name** | Qwen3-14B-Base |
| **HuggingFace Repo** | `Qwen/Qwen3-14B-Base` |
| **Parameters** | 14.8B (13.2B non-embedding), 40 layers, GQA (40 Q heads / 8 KV heads) |
| **Release Date** | May 2025 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | 36T tokens, 119 languages |
| **Benchmarks** | Performs on par with Qwen2.5-32B-Base; outperforms larger Qwen2.5 in STEM, coding, reasoning. Context 32K. |

### 3. Qwen2.5-7B (Alibaba)

| Field | Detail |
|---|---|
| **Full Name** | Qwen2.5-7B |
| **HuggingFace Repo** | `Qwen/Qwen2.5-7B` |
| **Parameters** | 7B |
| **Release Date** | September 2024 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | 18T tokens |
| **Benchmarks** | MMLU 74.2, MATH 49.8, HumanEval 57.9. Context 128K, generates up to 8K tokens. |

### 4. Qwen2.5-14B (Alibaba)

| Field | Detail |
|---|---|
| **Full Name** | Qwen2.5-14B |
| **HuggingFace Repo** | `Qwen/Qwen2.5-14B` |
| **Parameters** | 14B |
| **Release Date** | September 2024 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | Up to 18T tokens |
| **Benchmarks** | MMLU 79.7. Context 128K. |

### 5. Qwen2.5-Coder-7B (Alibaba)

| Field | Detail |
|---|---|
| **Full Name** | Qwen2.5-Coder-7B |
| **HuggingFace Repo** | `Qwen/Qwen2.5-Coder-7B` |
| **Parameters** | 7B |
| **Release Date** | Late 2024 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | 5.5T tokens (source code, text-code grounding, synthetic data) |
| **Benchmarks** | Outperforms general-purpose models 2x its size on code generation. Fits 8GB VRAM. |

### 6. Qwen2.5-Coder-14B (Alibaba)

| Field | Detail |
|---|---|
| **Full Name** | Qwen2.5-Coder-14B |
| **HuggingFace Repo** | `Qwen/Qwen2.5-Coder-14B` |
| **Parameters** | 14B |
| **Release Date** | Late 2024 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | 5.5T tokens |
| **Benchmarks** | Sweet spot for 16GB VRAM; stronger multi-file reasoning and algorithm implementation vs 7B. |

### 7. Gemma 3 12B (Google)

| Field | Detail |
|---|---|
| **Full Name** | Gemma 3 12B |
| **HuggingFace Repo** | `google/gemma-3-12b-pt` (pretrained) / `google/gemma-3-12b-it` (instruct) |
| **Parameters** | 12B |
| **Release Date** | March 12, 2025 |
| **Gated** | Yes (requires Google usage license agreement) |
| **Base Version Exists** | Yes (`gemma-3-12b-pt`) |
| **Training Data** | 12T tokens |
| **Benchmarks** | Global-MMLU-Lite 69.4 (base); MMLU-Pro 59.5 (IT). Native vision support, 128K context, 140+ languages. |

### 8. Gemma 2 9B (Google)

| Field | Detail |
|---|---|
| **Full Name** | Gemma 2 9B |
| **HuggingFace Repo** | `google/gemma-2-9b` |
| **Parameters** | 9B |
| **Release Date** | July 2024 |
| **Gated** | Yes (Google usage license) |
| **Base Version Exists** | Yes |
| **Training Data** | 8T tokens; trained with knowledge distillation |
| **Benchmarks** | OpenLLM v1 average 73.23 (IT). Interleaved local/global attention, GQA. Competitive with 2x-size models. |

### 9. Phi-4 14B (Microsoft)

| Field | Detail |
|---|---|
| **Full Name** | Phi-4 |
| **HuggingFace Repo** | `microsoft/phi-4` |
| **Parameters** | 14.7B |
| **Release Date** | December 2024 |
| **Gated** | No (MIT license) |
| **Base Version Exists** | Yes (the `microsoft/phi-4` model is the base) |
| **Training Data** | Extension of Phi-3 data: filtered web docs, educational data, synthetic "textbook-like" data for math/coding/reasoning, academic books, Q&A datasets. ~8% multilingual. |
| **Benchmarks** | MMLU 84.8 (surpasses Llama-3.3-70B). Q5_K_M variant reaches 76.2 MMLU. Strong in reasoning and math. |

### 10. Llama 3.1 8B (Meta)

| Field | Detail |
|---|---|
| **Full Name** | Llama 3.1 8B |
| **HuggingFace Repo** | `meta-llama/Llama-3.1-8B` |
| **Parameters** | 8B |
| **Release Date** | July 23, 2024 |
| **Gated** | Yes (Llama 3.1 Community License) |
| **Base Version Exists** | Yes |
| **Training Data** | ~15T multilingual tokens |
| **Benchmarks** | MMLU 65.6 (5-shot, base). 128K context window. |

### 11. Llama 3 8B (Meta)

| Field | Detail |
|---|---|
| **Full Name** | Meta-Llama-3-8B |
| **HuggingFace Repo** | `meta-llama/Meta-Llama-3-8B` |
| **Parameters** | 8B |
| **Release Date** | April 18, 2024 |
| **Gated** | Yes (Llama 3 Community License) |
| **Base Version Exists** | Yes |
| **Training Data** | ~15T tokens |
| **Benchmarks** | Predecessor to 3.1; widely used baseline. |

### 12. DeepSeek-R1-Distill-Qwen-7B (DeepSeek)

| Field | Detail |
|---|---|
| **Full Name** | DeepSeek-R1-Distill-Qwen-7B |
| **HuggingFace Repo** | `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B` |
| **Parameters** | 7B |
| **Release Date** | January 2025 |
| **Gated** | No (Apache 2.0, inherited from Qwen2.5) |
| **Base Version Exists** | This is a distilled/fine-tuned model (from Qwen2.5 base), not a pretrained-from-scratch base |
| **Training Data** | Distilled from DeepSeek-R1 with 800K curated reasoning samples |
| **Benchmarks** | Strong chain-of-thought reasoning; inherits R1's reasoning capabilities at 7B scale. |

### 13. DeepSeek-R1-Distill-Qwen-14B (DeepSeek)

| Field | Detail |
|---|---|
| **Full Name** | DeepSeek-R1-Distill-Qwen-14B |
| **HuggingFace Repo** | `deepseek-ai/DeepSeek-R1-Distill-Qwen-14B` |
| **Parameters** | 14B |
| **Release Date** | January 2025 |
| **Gated** | No (Apache 2.0, inherited from Qwen2.5) |
| **Base Version Exists** | Distilled model, not pretrained base |
| **Training Data** | 800K curated samples from DeepSeek-R1 |
| **Benchmarks** | Strongest distilled reasoning model at 14B scale. |

### 14. DeepSeek-R1-Distill-Llama-8B (DeepSeek)

| Field | Detail |
|---|---|
| **Full Name** | DeepSeek-R1-Distill-Llama-8B |
| **HuggingFace Repo** | `deepseek-ai/DeepSeek-R1-Distill-Llama-8B` |
| **Parameters** | 8B |
| **Release Date** | January 2025 |
| **Gated** | Llama 3.1 license (inherited from Llama3.1-8B-Base) |
| **Base Version Exists** | Distilled model built on Llama 3.1 8B base |
| **Training Data** | 800K curated samples from DeepSeek-R1 |
| **Benchmarks** | Reasoning-enhanced Llama variant. |

### 15. Falcon 3 7B (TII)

| Field | Detail |
|---|---|
| **Full Name** | Falcon3-7B-Base |
| **HuggingFace Repo** | `tiiuae/Falcon3-7B-Base` |
| **Parameters** | 7B |
| **Release Date** | December 2024 |
| **Gated** | No (TII Falcon License 2.0; compatible with Llama architecture) |
| **Base Version Exists** | Yes |
| **Training Data** | 14T tokens (web, code, STEM, multilingual: EN/FR/ES/PT) |
| **Benchmarks** | MMLU 67.4, MMLU-PRO 39.2. On par with Qwen2.5-7B among sub-9B models. |

### 16. Falcon 3 10B (TII)

| Field | Detail |
|---|---|
| **Full Name** | Falcon3-10B-Base |
| **HuggingFace Repo** | `tiiuae/Falcon3-10B-Base` |
| **Parameters** | 10B |
| **Release Date** | December 2024 |
| **Gated** | No |
| **Base Version Exists** | Yes |
| **Training Data** | Upscaled from 7B + 2T additional tokens (web, code, STEM) |
| **Benchmarks** | MMLU 73.1, MMLU-PRO 42.5. SOTA zero-shot and few-shot for sub-13B models. |

### 17. Falcon-H1-7B (TII)

| Field | Detail |
|---|---|
| **Full Name** | Falcon-H1-7B-Base |
| **HuggingFace Repo** | `tiiuae/Falcon-H1-7B-Base` |
| **Parameters** | 7B |
| **Release Date** | 2025 |
| **Gated** | No |
| **Base Version Exists** | Yes |
| **Training Data** | Not specified in search results |
| **Benchmarks** | Hybrid Transformer + SSM (Mamba) architecture. 256K context. 18 native languages. Adjustable attention/SSM ratio for efficiency. |

### 18. OLMo 2 7B (Allen AI)

| Field | Detail |
|---|---|
| **Full Name** | OLMo-2-1124-7B |
| **HuggingFace Repo** | `allenai/OLMo-2-1124-7B` |
| **Parameters** | 7B |
| **Release Date** | November 2024 |
| **Gated** | No (fully open: data, code, weights, training logs) |
| **Base Version Exists** | Yes |
| **Training Data** | ~5T tokens (OLMo-Mix-1124: DCLM, Dolma, Starcoder, Proof Pile II) |
| **Benchmarks** | MMLU 63.7. Outperforms Llama-3.1-8B. Staged training approach. |

### 19. OLMo 2 13B (Allen AI)

| Field | Detail |
|---|---|
| **Full Name** | OLMo-2-1124-13B |
| **HuggingFace Repo** | `allenai/OLMo-2-1124-13B` |
| **Parameters** | 13B |
| **Release Date** | November 2024 |
| **Gated** | No (fully open) |
| **Base Version Exists** | Yes |
| **Training Data** | ~5T tokens (1.2 epochs) |
| **Benchmarks** | MMLU 67.5. Outperforms Qwen2.5-7B despite lower training FLOPs. |

### 20. OLMo 3 7B (Allen AI)

| Field | Detail |
|---|---|
| **Full Name** | Olmo-3-1025-7B |
| **HuggingFace Repo** | `allenai/Olmo-3-1025-7B` |
| **Parameters** | 7B |
| **Release Date** | October 2025 |
| **Gated** | No (Apache 2.0; fully open) |
| **Base Version Exists** | Yes |
| **Training Data** | ~5.93T tokens (dolma3_6T-mix-1025). Mix: 20% code, 28% web, 19% math, 14% QA, 8% thinking, 6% instruction, 5% PDFs. |
| **Benchmarks** | Successor to OLMo 2; details in paper at allenai.org/papers/olmo3. |

### 21. Mistral Nemo 12B (Mistral AI / NVIDIA)

| Field | Detail |
|---|---|
| **Full Name** | Mistral-NeMo-12B-Base |
| **HuggingFace Repo** | `mistralai/Mistral-Nemo-Base-2407` (also `nvidia/Mistral-NeMo-12B-Base`) |
| **Parameters** | 12B |
| **Release Date** | July 2024 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | Trained May-June 2024; 80+ programming languages, multilingual (EN/FR/DE/ES/IT/PT/ZH/JA/KO/AR/HI) |
| **Benchmarks** | MMLU 68.0 (5-shot), HellaSwag 83.5, Winogrande 76.8, TriviaQA 73.8. Outperforms Gemma 2 9B and Llama 3 8B. |

### 22. InternLM3 8B (Shanghai AI Lab)

| Field | Detail |
|---|---|
| **Full Name** | InternLM3-8B |
| **HuggingFace Repo** | `internlm/internlm3-8b-instruct` (instruct version released; base checkpoint may be in the `internlm` collection) |
| **Parameters** | 8B |
| **Release Date** | January 15, 2025 |
| **Gated** | No |
| **Base Version Exists** | Instruct version publicly available; base checkpoint availability unclear from search results |
| **Training Data** | 4T tokens (claimed 75% training cost savings vs comparable models) |
| **Benchmarks** | Surpasses Llama3.1-8B and Qwen2.5-7B on reasoning/knowledge tasks. Supports deep thinking (long CoT) mode. |

### 23. Yi-1.5-9B (01.AI)

| Field | Detail |
|---|---|
| **Full Name** | Yi-1.5-9B |
| **HuggingFace Repo** | `01-ai/Yi-1.5-9B` |
| **Parameters** | 9B |
| **Release Date** | May 13, 2024 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | Bilingual (EN/ZH); 34B variant trained on 3.1T tokens (9B likely similar or subset) |
| **Benchmarks** | MMLU 76.3, BBH 54.3, C-Eval 81.4. Top performer among similarly sized open-source models. GQA + SwiGLU architecture. |

### 24. MAP-Neo 7B (MAP)

| Field | Detail |
|---|---|
| **Full Name** | MAP-Neo 7B |
| **HuggingFace Repo** | `m-a-p/neo_7b` |
| **Parameters** | 7B |
| **Release Date** | Mid 2024 |
| **Gated** | No (commercial use permitted) |
| **Base Version Exists** | Yes |
| **Training Data** | 4.5T tokens (English + Chinese). Fully open: data pipeline, cleaning code, all checkpoints, tokenizer. |
| **Benchmarks** | Comparable to LLaMA 2 7B. Strong in reasoning, math, coding. Fully reproducible (all artifacts released). |

### 25. StarCoder2-7B (BigCode)

| Field | Detail |
|---|---|
| **Full Name** | StarCoder2-7B |
| **HuggingFace Repo** | `bigcode/starcoder2-7b` |
| **Parameters** | 7B |
| **Release Date** | February 28, 2024 |
| **Gated** | No (BigCode OpenRAIL-M v1) |
| **Base Version Exists** | Yes (code-only base model) |
| **Training Data** | 3.5T+ tokens, 17 programming languages (The Stack v2) |
| **Benchmarks** | Code generation specialist. GQA, 16K context, sliding window attention 4K. Fill-in-the-Middle objective. |

### 26. StarCoder2-15B (BigCode)

| Field | Detail |
|---|---|
| **Full Name** | StarCoder2-15B |
| **HuggingFace Repo** | `bigcode/starcoder2-15b` |
| **Parameters** | 15B (slightly above 14B range, included for completeness) |
| **Release Date** | February 28, 2024 |
| **Gated** | No (BigCode OpenRAIL-M v1) |
| **Base Version Exists** | Yes (code-only base model) |
| **Training Data** | 4T+ tokens, 600+ programming languages (The Stack v2) |
| **Benchmarks** | Strongest code model in its size class at release. 16K context. |

### 27. Mistral Small 3 24B (Mistral AI) [NOTE: Not 7B]

| Field | Detail |
|---|---|
| **Full Name** | Mistral-Small-24B-Base-2501 |
| **HuggingFace Repo** | `mistralai/Mistral-Small-24B-Base-2501` (also Instruct: `mistralai/Mistral-Small-3.1-24B-Instruct-2503`) |
| **Parameters** | 24B (outside 7B-14B range) |
| **Release Date** | January 2025 |
| **Gated** | No |
| **Base Version Exists** | Yes |
| **Note** | Included because some sources incorrectly describe it as "7B." Actual parameter count is 24B. MMLU >81%, ~150 tokens/s, MT-Bench 8.0. |

---

## Summary: Models Strictly in 7B-14B Range with Base Versions Available

| Model | Params | Release | License | Training Data | MMLU (base) | HF Repo |
|---|---|---|---|---|---|---|
| Qwen3-8B-Base | 8B | May 2025 | Apache 2.0 | 36T tokens | ~74.7 | `Qwen/Qwen3-8B-Base` |
| Qwen3-14B-Base | 14.8B | May 2025 | Apache 2.0 | 36T tokens | ~Qwen2.5-32B level | `Qwen/Qwen3-14B-Base` |
| Qwen2.5-7B | 7B | Sep 2024 | Apache 2.0 | 18T tokens | 74.2 | `Qwen/Qwen2.5-7B` |
| Qwen2.5-14B | 14B | Sep 2024 | Apache 2.0 | 18T tokens | 79.7 | `Qwen/Qwen2.5-14B` |
| Qwen2.5-Coder-7B | 7B | Late 2024 | Apache 2.0 | 5.5T tokens | Code specialist | `Qwen/Qwen2.5-Coder-7B` |
| Qwen2.5-Coder-14B | 14B | Late 2024 | Apache 2.0 | 5.5T tokens | Code specialist | `Qwen/Qwen2.5-Coder-14B` |
| Phi-4 | 14.7B | Dec 2024 | MIT | Synthetic+web+academic | 84.8 | `microsoft/phi-4` |
| Gemma 3 12B | 12B | Mar 2025 | Google license (gated) | 12T tokens | GMMLU 69.4 | `google/gemma-3-12b-pt` |
| Gemma 2 9B | 9B | Jul 2024 | Google license (gated) | 8T tokens | ~68-70 est. | `google/gemma-2-9b` |
| Llama 3.1 8B | 8B | Jul 2024 | Llama license (gated) | 15T tokens | 65.6 | `meta-llama/Llama-3.1-8B` |
| Mistral Nemo 12B | 12B | Jul 2024 | Apache 2.0 | Multilingual | 68.0 | `mistralai/Mistral-Nemo-Base-2407` |
| Falcon3-7B | 7B | Dec 2024 | Falcon License 2.0 | 14T tokens | 67.4 | `tiiuae/Falcon3-7B-Base` |
| Falcon3-10B | 10B | Dec 2024 | Falcon License 2.0 | 7B+2T upscale | 73.1 | `tiiuae/Falcon3-10B-Base` |
| Falcon-H1-7B | 7B | 2025 | Open | Not specified | Hybrid SSM+Attn | `tiiuae/Falcon-H1-7B-Base` |
| OLMo 2 7B | 7B | Nov 2024 | Apache 2.0 (fully open) | 5T tokens | 63.7 | `allenai/OLMo-2-1124-7B` |
| OLMo 2 13B | 13B | Nov 2024 | Apache 2.0 (fully open) | 5T tokens | 67.5 | `allenai/OLMo-2-1124-13B` |
| OLMo 3 7B | 7B | Oct 2025 | Apache 2.0 (fully open) | 5.93T tokens | Improved over OLMo 2 | `allenai/Olmo-3-1025-7B` |
| InternLM3 8B | 8B | Jan 2025 | Open | 4T tokens | Beats Llama3.1-8B | `internlm/internlm3-8b-instruct` |
| Yi-1.5-9B | 9B | May 2024 | Apache 2.0 | ~3T tokens | 76.3 | `01-ai/Yi-1.5-9B` |
| MAP-Neo 7B | 7B | Mid 2024 | Open (commercial OK) | 4.5T tokens | ~LLaMA2-7B level | `m-a-p/neo_7b` |
| StarCoder2-7B | 7B | Feb 2024 | OpenRAIL-M | 3.5T tokens | Code specialist | `bigcode/starcoder2-7b` |
| DeepSeek-R1-Distill-Qwen-7B | 7B | Jan 2025 | Apache 2.0 | 800K reasoning samples | Reasoning specialist | `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B` |
| DeepSeek-R1-Distill-Qwen-14B | 14B | Jan 2025 | Apache 2.0 | 800K reasoning samples | Reasoning specialist | `deepseek-ai/DeepSeek-R1-Distill-Qwen-14B` |
| DeepSeek-R1-Distill-Llama-8B | 8B | Jan 2025 | Llama 3.1 license | 800K reasoning samples | Reasoning specialist | `deepseek-ai/DeepSeek-R1-Distill-Llama-8B` |

---

## Key Observations for Academic Paper Use

1. **Strongest base models by MMLU in range**: Phi-4 (84.8) > Qwen2.5-14B (79.7) > Yi-1.5-9B (76.3) > Qwen3-8B (~74.7) > Qwen2.5-7B (74.2) > Falcon3-10B (73.1)

2. **Fully open models** (data + code + weights): OLMo 2/3 (Allen AI) and MAP-Neo are the only models with complete reproducibility artifacts (training data, pipeline code, all checkpoints).

3. **2025-2026 releases**: Qwen3-8B-Base, Qwen3-14B-Base, Gemma 3 12B, InternLM3-8B, OLMo 3 7B, Falcon-H1-7B, DeepSeek-R1 distilled variants.

4. **Llama 4 does NOT have a dense 7B-14B base model**. Llama 4 uses MoE: Scout (109B total, 17B active) and Maverick (400B total, 17B active). The last dense Llama base in this range is Llama 3.1 8B.

5. **Gated models** requiring license agreement: All Gemma models (Google), all Llama models (Meta). Non-gated: Qwen, Phi-4, Falcon, OLMo, Mistral Nemo, Yi, MAP-Neo, StarCoder2.

6. **Gemma 4** was released April 2, 2026 but its sizes are E2B, E4B, 26B-A4B, and 31B (none in the 7B-14B dense range).

Sources:
- [Qwen3-8B-Base on HuggingFace](https://huggingface.co/Qwen/Qwen3-8B-Base)
- [Qwen3 Blog Post](https://qwenlm.github.io/blog/qwen3/)
- [Qwen3-14B-Base on HuggingFace](https://huggingface.co/Qwen/Qwen3-14B-Base)
- [Qwen2.5-7B on HuggingFace](https://huggingface.co/Qwen/Qwen2.5-7B)
- [Qwen2.5-14B on HuggingFace](https://huggingface.co/Qwen/Qwen2.5-14B)
- [Qwen2.5 Technical Report](https://arxiv.org/pdf/2412.15115)
- [Phi-4 on HuggingFace](https://huggingface.co/microsoft/phi-4)
- [Phi-4 Technical Report](https://arxiv.org/html/2412.08905v1)
- [Gemma 3 12B Pretrained](https://huggingface.co/google/gemma-3-12b-pt)
- [Gemma 3 Blog](https://huggingface.co/blog/gemma3)
- [Gemma 2 9B](https://huggingface.co/google/gemma-2-9b)
- [Llama 3.1 8B](https://huggingface.co/meta-llama/Llama-3.1-8B)
- [Mistral Nemo Base](https://huggingface.co/mistralai/Mistral-Nemo-Base-2407)
- [Falcon3-7B-Base](https://huggingface.co/tiiuae/Falcon3-7B-Base)
- [Falcon3-10B-Base](https://huggingface.co/tiiuae/Falcon3-10B-Base)
- [Falcon3 Blog](https://huggingface.co/blog/falcon3)
- [Falcon-H1 Blog](https://falcon-lm.github.io/blog/falcon-h1/)
- [OLMo 2 Collection](https://huggingface.co/collections/allenai/olmo-2)
- [OLMo 2 Blog](https://allenai.org/blog/olmo2)
- [OLMo 3 7B](https://huggingface.co/allenai/Olmo-3-1025-7B)
- [InternLM3-8B](https://huggingface.co/internlm/internlm3-8b-instruct)
- [Yi-1.5-9B](https://huggingface.co/01-ai/Yi-1.5-9B)
- [MAP-Neo 7B](https://huggingface.co/m-a-p/neo_7b)
- [StarCoder2-7B](https://huggingface.co/bigcode/starcoder2-7b)
- [DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B)
- [DeepSeek-R1-Distill-Qwen-14B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B)
- [Open-Source LLM Landscape 2026](https://presenc.ai/research/open-source-llm-landscape-2026)
- [Featherless Best Open-Source LLMs 2026](https://featherless.ai/blog/best-open-source-llms-2026)
- [HuggingFace State of Open Source Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)
- [Gemma 4 Overview](https://ai.google.dev/gemma/docs/core)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f82af57f-e711-4be3-a599-837f9f2ab522",
  "isSidechain": true,
  "agentId": "a07b72467ddf2db7b",
  "requestId": "req_011Cb9cdTSaZEPQnZZroMdcr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dee5900e-e391-4b5e-ba8c-82db755b3447",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xsz79PhbGvhKPxwDVZVqQq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2827,
      "cache_read_input_tokens": 45864,
      "output_tokens": 8646,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2827
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8646,
          "cache_read_input_tokens": 45864,
          "cache_creation_input_tokens": 2827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2827,
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
