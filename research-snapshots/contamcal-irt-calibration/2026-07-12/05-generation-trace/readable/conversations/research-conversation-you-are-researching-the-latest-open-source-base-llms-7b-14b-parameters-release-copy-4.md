# Research conversation: You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Ru

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 1
- **Tool calls:** 24
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a72b4b1ce170203bc.jsonl`
- **Structured JSON:** [`0aa42b6b0e1a3e9da31e.json`](../../sessions/0a/0aa42b6b0e1a3e9da31e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

59 recorded events

### User

_source line 1 · 2026-05-18T07:07:46.106Z_

You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.

Search 1: "DeepSeek V3 base model"
Search 2: "Phi-4 base model"
Search 3: "DeepSeek R2 base model 2025 2026"

Return ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range. Also note if any of these models use MoE architecture (mixture of experts) and what the active parameter count is.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "dad4b010-2d99-4082-90f0-908dca468ef1",
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

_source line 2 · 2026-05-18T07:07:46.110Z_

```json
{
  "parentUuid": "dad4b010-2d99-4082-90f0-908dca468ef1",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
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
  "uuid": "c33eb44d-c736-42a0-bec2-c09bde57bcac",
  "timestamp": "2026-05-18T07:07:46.110Z",
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

_source line 3 · 2026-05-18T07:07:48.771Z_



I'll run all three web searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c33eb44d-c736-42a0-bec2-c09bde57bcac",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9cVZUzF8p37NTc8r7A2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5629da82-405c-4693-9b52-e03258cf9d19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FcYy1HWgNmMvQ1LPTKgYXT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7283,
      "cache_read_input_tokens": 8253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7283,
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

_source line 4 · 2026-05-18T07:07:49.132Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PmuWZTvFJWW2UJr1SeeRDN`</summary>

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
  "parentUuid": "5629da82-405c-4693-9b52-e03258cf9d19",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9cVZUzF8p37NTc8r7A2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4493316f-cfaa-4c9b-b1e2-4b09804d7a9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FcYy1HWgNmMvQ1LPTKgYXT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7283,
      "cache_read_input_tokens": 8253,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7283
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 87,
          "cache_read_input_tokens": 8253,
          "cache_creation_input_tokens": 7283,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7283,
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

_source line 5 · 2026-05-18T07:07:49.136Z_

<details><summary>↩ Tool result · `toolu_01PmuWZTvFJWW2UJr1SeeRDN`</summary>

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
  "parentUuid": "4493316f-cfaa-4c9b-b1e2-4b09804d7a9a",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "dd5729e2-89ca-4227-b3fd-a7491aaeaa94",
  "sourceToolAssistantUUID": "4493316f-cfaa-4c9b-b1e2-4b09804d7a9a",
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

_source line 6 · 2026-05-18T07:07:51.662Z_



Now I'll run all three searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd5729e2-89ca-4227-b3fd-a7491aaeaa94",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9cVnezzZwZ83YH4BCzj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76598b5d-b795-40b0-b22d-f86d2406c9a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4JzKiokS3km9MvED4LQgS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 15536,
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

_source line 7 · 2026-05-18T07:07:52.133Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013dnFFByY7aXsWdv3Taau1a`</summary>

```json
{
  "query": "DeepSeek V3 base model HuggingFace 7B 14B parameters 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76598b5d-b795-40b0-b22d-f86d2406c9a5",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9cVnezzZwZ83YH4BCzj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c03ea3ca-6c63-4285-bf03-9e8a8a1b708b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4JzKiokS3km9MvED4LQgS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 15536,
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

_source line 8 · 2026-05-18T07:07:52.605Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017VuJHp2EPxoQ9KhWYediGC`</summary>

```json
{
  "query": "Phi-4 base model HuggingFace parameters 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c03ea3ca-6c63-4285-bf03-9e8a8a1b708b",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9cVnezzZwZ83YH4BCzj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f51088c2-2dc6-42e3-be4b-48051e69e3ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4JzKiokS3km9MvED4LQgS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 15536,
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

_source line 9 · 2026-05-18T07:07:52.818Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015Cy6U2vyj3X8SnswnMQkLB`</summary>

```json
{
  "query": "DeepSeek R2 base model 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f51088c2-2dc6-42e3-be4b-48051e69e3ed",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9cVnezzZwZ83YH4BCzj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36036e67-a04c-4316-aa1f-03a04018b50d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4JzKiokS3km9MvED4LQgS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 15536,
      "output_tokens": 194,
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
          "output_tokens": 194,
          "cache_read_input_tokens": 15536,
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

_source line 10 · 2026-05-18T07:07:59.263Z_

<details><summary>↩ Tool result · `toolu_013dnFFByY7aXsWdv3Taau1a`</summary>

```text
Web search results for query: "DeepSeek V3 base model HuggingFace 7B 14B parameters 2025 2026"

Links: [{"title":"deepseek-ai/DeepSeek-V3 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V3"},{"title":"DeepSeek-V3 · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/deepseek_v3"},{"title":"deepseek-ai/DeepSeek-V3-Base · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V3-Base"},{"title":"DeepSeek-V3","url":"https://huggingface.co/docs/transformers/main/en/model_doc/deepseek_v3"},{"title":"deepseek-ai/DeepSeek-V3.1-Base · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V3.1-Base"},{"title":"anchovy/DeepSeek-V3-Base · Hugging Face","url":"https://huggingface.co/anchovy/DeepSeek-V3-Base"},{"title":"README_WEIGHTS.md · deepseek-ai/DeepSeek-V3 at main","url":"https://huggingface.co/deepseek-ai/DeepSeek-V3/blob/main/README_WEIGHTS.md"},{"title":"deepseek-ai/DeepSeek-V3.2 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V3.2"},{"title":"unsloth/DeepSeek-V3 · Hugging Face","url":"https://huggingface.co/unsloth/DeepSeek-V3"},{"title":"deepseek-ai/DeepSeek-V3 - Demo - DeepInfra","url":"https://deepinfra.com/deepseek-ai/DeepSeek-V3"}]

Based on the search results, I found information about DeepSeek V3. However, I should clarify that the specific 7B and 14B parameter versions you mentioned in your query don't appear to exist for DeepSeek V3.

## DeepSeek V3 Model Specifications

DeepSeek-V3 is a strong Mixture-of-Experts (MoE) language model with 671B total parameters with 37B activated for each token. The total size of DeepSeek-V3 models on HuggingFace is 685B, which includes 671B of the Main Model weights and 14B of the Multi-Token Prediction (MTP) Module weights.

The DeepSeek V3 base model is available on HuggingFace under the repository `deepseek-ai/DeepSeek-V3-Base`. This is the primary base model available, and it does not come in 7B or 14B variants - it is a 671B parameter model.

There are newer versions like DeepSeek-V3.1, which is a hybrid model that supports both thinking mode and non-thinking mode.

If you're looking for smaller parameter models from DeepSeek, you may want to explore other versions like DeepSeek-V2 or other model families, as the V3 series appears to be focused on the large 671B parameter model architecture.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c03ea3ca-6c63-4285-bf03-9e8a8a1b708b",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "be1f8a30-9c69-4e51-b9d0-88458d78fea3",
  "sourceToolAssistantUUID": "c03ea3ca-6c63-4285-bf03-9e8a8a1b708b",
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

_source line 11 · 2026-05-18T07:08:01.119Z_

<details><summary>↩ Tool result · `toolu_017VuJHp2EPxoQ9KhWYediGC`</summary>

```text
Web search results for query: "Phi-4 base model HuggingFace parameters 2025 2026"

Links: [{"title":"microsoft/Phi-4-mini-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-instruct"},{"title":"microsoft/Phi-4-reasoning-vision-15B · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B"},{"title":"microsoft/phi-4 · Hugging Face","url":"https://huggingface.co/microsoft/phi-4"},{"title":"nvidia/Phi-4-multimodal-instruct-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Phi-4-multimodal-instruct-NVFP4"},{"title":"microsoft/Phi-4-mini-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-reasoning"},{"title":"microsoft/Phi-4-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning"},{"title":"microsoft/Phi-4-reasoning-plus · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-plus"},{"title":"nvidia/Phi-4-reasoning-plus-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Phi-4-reasoning-plus-NVFP4"},{"title":"microsoft/Phi-4-mini-flash-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-flash-reasoning"},{"title":"microsoft/Phi-4-multimodal-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-multimodal-instruct"}]

Based on the web search results, here's information about Phi-4 base model parameters available on HuggingFace:

## Phi-4 Model Variants and Parameters

The Phi-4 family includes several models with different parameter sizes:

1. **Phi-4-mini models**: The model with only 3.8B-param achieves a similar level of multilingual language understanding and reasoning ability as much larger models. This includes variants like Phi-4-mini-instruct and Phi-4-mini-reasoning.

2. **Phi-4 Base Model**: While the search results don't explicitly state the base model's parameter count, they reference a standard Phi-4 model.

3. **Phi-4-Reasoning**: Phi-4-reasoning, with only 14B parameters, performs well across a wide range of reasoning tasks

4. **Phi-4-Reasoning-Vision-15B**: Released March 4, 2026 with 15B parameters and 16,384 tokens context length

5. **Phi-4-multimodal-instruct**: Number of model parameters 5.6×10^9 (5.6B parameters)

6. **Phi-4-mini-flash-reasoning**: Featuring 3.8 billion parameters and a 200K vocabulary

## Additional Technical Details

- Phi-4-mini-instruct supports a vocabulary size of up to 200064 tokens
- The model supports 128K token context length

These models are available on HuggingFace under the Microsoft organization and were released/updated between 2025 and early 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f51088c2-2dc6-42e3-be4b-48051e69e3ed",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "e41c0323-e56c-480f-bf40-e98999c6ec25",
  "sourceToolAssistantUUID": "f51088c2-2dc6-42e3-be4b-48051e69e3ed",
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

_source line 12 · 2026-05-18T07:08:01.825Z_

<details><summary>↩ Tool result · `toolu_015Cy6U2vyj3X8SnswnMQkLB`</summary>

```text
Web search results for query: "DeepSeek R2 base model 2025 2026"

Links: [{"title":"The Ultimate DeepSeek Guide 2026 | Master AI with DeepSeek-V3.2 & R2","url":"https://deepseek.ai/blog/deepseek-guide-2026"},{"title":"Will DeepSeek’s new model spark another global AI shake-up in 2026?","url":"https://restofworld.org/2025/deepseek-china-r2-ai-model-us-rivalry/"},{"title":"DeepSeek V4 and R2 Deep Dive | Meta Intelligence","url":"https://www.meta-intelligence.tech/en/insight-deepseek-v4-r2"},{"title":"DeepSeek's Next Move: What V4 Will Look Like","url":"https://recodechinaai.substack.com/p/deepseeks-next-move-what-v4-will"},{"title":"What is DeepSeek R2: The Best Upcoming AI Model In 2025? | AI Hub","url":"https://overchat.ai/ai-hub/what-is-deepseek-r2"},{"title":"Deepseek R2 Release Timeline & Updates 2025","url":"https://www.byteplus.com/en/topic/384181"},{"title":"DeepSeek - Wikipedia","url":"https://en.wikipedia.org/wiki/DeepSeek"},{"title":"DeepSeek Plans AI Agent Rollout in Late 2025 - Techstrong.ai","url":"https://techstrong.ai/features/deepseek-plans-ai-agent-rollout-in-late-2025/"},{"title":"DeepSeek Roadmap, Rumors & Confirmed Releases: What Is Official and What Is Not - Chat-Deep.ai","url":"https://chat-deep.ai/guide/deepseek-roadmap-rumors/"},{"title":"Ultimate Guide - The Best DeepSeek-AI Models in 2026","url":"https://www.siliconflow.com/articles/en/the-best-deepseek-ai-models-in-2025"}]

Based on the search results, here's what I found regarding DeepSeek R2 base model in 2025-2026:

## DeepSeek R2 Status

In late February 2026, multiple sources confirmed that DeepSeek was preparing to release two new models: DeepSeek V4 (the fourth generation of its general-purpose foundation model) and DeepSeek R2 (the second generation of its reasoning model).

However, as of May 7, 2026, R2 is not listed among the current model IDs in the official DeepSeek API model list, and no official R2 release was found in the checked DeepSeek model list or release pages.

## Development Timeline and Delays

The widely anticipated DeepSeek-V4 and DeepSeek-R2, which were reportedly slated for release in the first half of 2025, were delayed. DeepSeek initially attempted to train R2 using Huawei's Ascend AI chips rather than Western silicon like Nvidia's GPUs, partly due to pressure from the Chinese government to reduce reliance on U.S.-made hardware. The training runs encountered repeated failures and performance issues stemming from stability problems, slow chip-to-chip interconnect speeds, and immature software tooling.

## What Is Currently Available

Instead of R2, on April 24, 2026, DeepSeek released a preview of its V4 series, including the 1.6-trillion parameter DeepSeek-V4-Pro and the 284-billion parameter DeepSeek-V4-Flash, both featuring a 1-million token context window.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36036e67-a04c-4316-aa1f-03a04018b50d",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "b71eefce-fc6d-41e8-b6bc-3ba293ae96a7",
  "sourceToolAssistantUUID": "36036e67-a04c-4316-aa1f-03a04018b50d",
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

_source line 13 · 2026-05-18T07:08:04.802Z_

Let me run additional searches to get more specific details on the models in the 7B-14B range.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b71eefce-fc6d-41e8-b6bc-3ba293ae96a7",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9cWiiPqfhGMCJf9xEJp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ea77c9a-9d32-46bd-9b9d-c12f42f3f5c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsLNqEhKFpFMvSMZNE6cvF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2940,
      "cache_read_input_tokens": 16987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2940,
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

_source line 14 · 2026-05-18T07:08:05.737Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QNSqgeU7eL4UnNrVUnF346`</summary>

```json
{
  "query": "microsoft phi-4 14B base model HuggingFace parameters release date gated"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ea77c9a-9d32-46bd-9b9d-c12f42f3f5c9",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9cWiiPqfhGMCJf9xEJp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c379a0ea-de86-4ada-ab00-3edc215eca0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsLNqEhKFpFMvSMZNE6cvF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2940,
      "cache_read_input_tokens": 16987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2940,
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

_source line 15 · 2026-05-18T07:08:06.681Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JKRViMRvEi7fp8YmNYvPE4`</summary>

```json
{
  "query": "DeepSeek V3 V2 small model 7B 14B 16B lite base 2025 2026 HuggingFace"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c379a0ea-de86-4ada-ab00-3edc215eca0c",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9cWiiPqfhGMCJf9xEJp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b4d74b2-d7a0-44d7-af93-0ca48ff0395f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsLNqEhKFpFMvSMZNE6cvF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2940,
      "cache_read_input_tokens": 16987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2940,
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

_source line 16 · 2026-05-18T07:08:07.321Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CkKiWfnh2V3QRabazuRRMP`</summary>

```json
{
  "query": "Phi-4 base pretrained model not instruct HuggingFace microsoft 14B"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b4d74b2-d7a0-44d7-af93-0ca48ff0395f",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9cWiiPqfhGMCJf9xEJp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70587238-2616-4115-896a-1ad5dc09d8c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsLNqEhKFpFMvSMZNE6cvF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2940,
      "cache_read_input_tokens": 16987,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2940
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 221,
          "cache_read_input_tokens": 16987,
          "cache_creation_input_tokens": 2940,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2940,
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

_source line 17 · 2026-05-18T07:08:11.880Z_

<details><summary>↩ Tool result · `toolu_01QNSqgeU7eL4UnNrVUnF346`</summary>

```text
Web search results for query: "microsoft phi-4 14B base model HuggingFace parameters release date gated"

Links: [{"title":"microsoft/phi-4 · Hugging Face","url":"https://huggingface.co/microsoft/phi-4"},{"title":"microsoft/Phi-4-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning"},{"title":"Phi-4 Local Setup: Microsoft's 14B Reasoning on 12GB GPUs | Local AI Master","url":"https://localaimaster.com/blog/phi-4-local-setup"},{"title":"Introducing Phi-4: Microsoft’s Newest Small Language Model Specializing in Complex Reasoning | Microsoft Community Hub","url":"https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-phi-4-microsoft%E2%80%99s-newest-small-language-model-specializing-in-comple/4357090"},{"title":"Microsoft Launches Two Powerful Phi-4 Reasoning Models","url":"https://www.analyticsvidhya.com/blog/2025/05/phi-4-reasoning-models/"},{"title":"microsoft/Phi-4-reasoning-vision-15B · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B"},{"title":"NyxKrage/Microsoft_Phi-4 · Hugging Face","url":"https://huggingface.co/NyxKrage/Microsoft_Phi-4"},{"title":"microsoft/phi-4 · Base model","url":"https://huggingface.co/microsoft/phi-4/discussions/4"},{"title":"microsoft/Phi-4-reasoning-plus · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-plus"},{"title":"microsoft/Phi-4-multimodal-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-multimodal-instruct"}]

Based on the web search results, here's what I found about Microsoft Phi-4 14B base model on HuggingFace:

## Key Information

**Parameters:** Phi-4 has 14.7B parameters

**Release Date:** Phi-4 is the December 2024 release of Microsoft's Phi family

**Model Status:** Phi-4 is available on Azure AI Foundry and on Hugging Face

**Architecture:** It's a standard decoder-only transformer with 16K context and ChatML chat template

**License:** The license is MIT — most permissive of recent major releases

Regarding the "gated" status of the base model, the search results show that base model release becomes difficult because of safety guidelines, which suggests there may be some considerations around the base model availability, though the results don't explicitly confirm whether the model card itself is gated or if it's freely available with standard MIT licensing.

The model is designed to excel at complex reasoning tasks, particularly in mathematics and coding, despite its relatively small size compared to larger language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c379a0ea-de86-4ada-ab00-3edc215eca0c",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "6378e633-e0ce-46d7-98f4-3485e0deb956",
  "sourceToolAssistantUUID": "c379a0ea-de86-4ada-ab00-3edc215eca0c",
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

_source line 18 · 2026-05-18T07:08:15.407Z_

<details><summary>↩ Tool result · `toolu_01CkKiWfnh2V3QRabazuRRMP`</summary>

```text
Web search results for query: "Phi-4 base pretrained model not instruct HuggingFace microsoft 14B"

Links: [{"title":"microsoft/Phi-4-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning"},{"title":"microsoft/phi-4 · Hugging Face","url":"https://huggingface.co/microsoft/phi-4"},{"title":"Introducing Phi-4: Microsoft’s Newest Small Language Model Specializing in Complex Reasoning | Microsoft Community Hub","url":"https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-phi-4-microsoft%E2%80%99s-newest-small-language-model-specializing-in-comple/4357090"},{"title":"microsoft/Phi-4-reasoning-plus · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-plus"},{"title":"Phi-4 Local Setup: Microsoft's 14B Reasoning on 12GB GPUs | Local AI Master","url":"https://localaimaster.com/blog/phi-4-local-setup"},{"title":"Welcome to the new Phi-4 models - Microsoft Phi-4-mini & Phi-4-multimodal","url":"https://techcommunity.microsoft.com/blog/educatordeveloperblog/welcome-to-the-new-phi-4-models---microsoft-phi-4-mini--phi-4-multimodal/4386037"},{"title":"NyxKrage/Microsoft_Phi-4 · Hugging Face","url":"https://huggingface.co/NyxKrage/Microsoft_Phi-4"},{"title":"microsoft/Phi-4-mini-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-instruct"},{"title":"Phi-4 - a microsoft Collection","url":"https://huggingface.co/collections/microsoft/phi-4-677e9380e514feb5577a40e4"},{"title":"Microsoft makes powerful Phi-4 model fully open-source on Hugging Face | VentureBeat","url":"https://venturebeat.com/ai/microsoft-makes-powerful-phi-4-model-fully-open-source-on-hugging-face"}]

Based on the search results, here's what I found about the Phi-4 base pretrained model:

## Phi-4 Base Model Overview

Phi-4 is a 14B parameters, dense decoder-only transformer model. Phi-4 is available on Azure AI Foundry and on Hugging Face.

### Model Details

The training data is an extension of the data used for Phi-3 and includes a wide variety of sources from: Publicly available documents filtered rigorously for quality, selected high-quality educational data, and code. Newly created synthetic, "textbook-like" data for the purpose of teaching math, coding, common sense reasoning, general knowledge of the world (science, daily activities, theory of mind, etc.). Acquired academic books and Q&A datasets.

### Architecture & Context

The architecture consists of a standard decoder-only transformer with 14.7B parameters and 16K context, using ChatML chat template.

### Licensing

Phi-4 comes with a permissive MIT License, allowing it to be used for commercial applications.

### Key Capabilities

The models improve significantly from Phi-4, despite the post-training being focused on reasoning. The base model is designed for high-quality reasoning and complex problem-solving tasks.

You can find the official microsoft/phi-4 repository on HuggingFace for direct access to the base pretrained model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70587238-2616-4115-896a-1ad5dc09d8c9",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "26f13acf-1b76-4cac-9d5c-2b622f7d2ea1",
  "sourceToolAssistantUUID": "70587238-2616-4115-896a-1ad5dc09d8c9",
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

_source line 19 · 2026-05-18T07:08:16.189Z_

<details><summary>↩ Tool result · `toolu_01JKRViMRvEi7fp8YmNYvPE4`</summary>

```text
Web search results for query: "DeepSeek V3 V2 small model 7B 14B 16B lite base 2025 2026 HuggingFace"

Links: [{"title":"DeepSeek Official Models List 2026 (V4, Flash, Pro) | DeepSeek V4 Network","url":"https://deepseekv4.network/models"},{"title":"DeepSeek Models Guide: R1, V3, and Coder | InsiderLLM","url":"https://insiderllm.com/guides/deepseek-models-guide/"},{"title":"The Complete Guide to DeepSeek Models: V3, R1, V4 and Beyond","url":"https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond"},{"title":"GitHub - deepseek-ai/DeepSeek-V3 · GitHub","url":"https://github.com/deepseek-ai/deepseek-v3"},{"title":"GitHub - deepseek-ai/DeepSeek-Coder-V2: DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-Coder-V2"},{"title":"Ultimate Guide - The Best DeepSeek-AI Models in 2026","url":"https://www.siliconflow.com/articles/en/the-best-deepseek-ai-models-in-2025"},{"title":"DeepSeek-V3.2 Release | DeepSeek API Docs","url":"https://api-docs.deepseek.com/news/news251201"},{"title":"DeepSeek Models: V3.2, R1, Distills, and Production Caveats","url":"https://fireworks.ai/blog/deepseek-models"},{"title":"GitHub - deepseek-ai/DeepSeek-R1 · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-R1"},{"title":"DeepSeek - Wikipedia","url":"https://en.wikipedia.org/wiki/DeepSeek"}]

Based on the search results, here's a comprehensive overview of DeepSeek models including the versions and sizes you asked about:

## DeepSeek Model Family Overview

### V1 Series
V1 has a dense stack of 7B and 67B models with 4K context and ~2T tokens.

### V2 Series
V2 uses MoE architecture with 236B total parameters, ~21B active, 128K context, ~8T tokens. V2-Lite trims to ~16B total and ~2.4B active for smaller clusters.

### V3 Series
V3 MoE has 671B total parameters, ~37B active, 256 experts, ~14T tokens. In March 2025, DeepSeek released DeepSeek-V3-0324, which uses the same base model as DeepSeek-V3 but with improved post-training pipeline drawing lessons from the RL technique in DeepSeek-R1, allowing better reasoning performance, coding skills and tool-use capabilities.

### Small Models and Lite Versions
Lite and 16B MoE models are available for constrained deployments. DeepSeek-Coder-V2 comes in 16B and 236B parameter sizes based on the DeepSeekMoE framework, with activated parameters of 2.4B and 21B respectively.

### R1 Distilled Models
DeepSeek open-sourced distilled 1.5B, 7B, 8B, 14B, 32B, and 70B checkpoints based on Qwen2.5 and Llama3 series.

### V4 Series (2026)
In April 2026, DeepSeek released a preview of its V4 series, including the 1.6-trillion parameter DeepSeek-V4-Pro and the 284-billion parameter DeepSeek-V4-Flash, both featuring a 1-million token context window.

All these models are available on HuggingFace for community use and deployment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b4d74b2-d7a0-44d7-af93-0ca48ff0395f",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "f02ce24f-9a6c-409b-8564-e3b717b208cd",
  "sourceToolAssistantUUID": "3b4d74b2-d7a0-44d7-af93-0ca48ff0395f",
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

_source line 20 · 2026-05-18T07:08:19.482Z_

Let me get more details on specific models, especially around gating, training data, benchmarks, and the DeepSeek smaller models.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f02ce24f-9a6c-409b-8564-e3b717b208cd",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9cXnMhTqvJ2aNDuAZY2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b528503a-3d8c-4d6e-ad59-a3e24fd940df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NB9dg2TFQahhP1NChMjrUD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 935,
      "cache_creation_input_tokens": 2182,
      "cache_read_input_tokens": 19927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2182,
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

_source line 21 · 2026-05-18T07:08:20.494Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HwhzW91FS2ggAX9YTzTGaZ`</summary>

```json
{
  "query": "microsoft/phi-4 HuggingFace benchmark MMLU training data size tokens gated access"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b528503a-3d8c-4d6e-ad59-a3e24fd940df",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9cXnMhTqvJ2aNDuAZY2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c27f27ef-bc25-4787-84a7-c7dc491441ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NB9dg2TFQahhP1NChMjrUD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 935,
      "cache_creation_input_tokens": 2182,
      "cache_read_input_tokens": 19927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2182,
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

_source line 22 · 2026-05-18T07:08:21.651Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WBntCuDtM4WNQSMmgyTAwg`</summary>

```json
{
  "query": "DeepSeek-R1-Distill-Qwen-14B DeepSeek-R1-Distill-Qwen-7B HuggingFace base model benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c27f27ef-bc25-4787-84a7-c7dc491441ad",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9cXnMhTqvJ2aNDuAZY2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b992dd7-5e04-4f6b-8ac3-fda146cb9f6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NB9dg2TFQahhP1NChMjrUD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 935,
      "cache_creation_input_tokens": 2182,
      "cache_read_input_tokens": 19927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2182,
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

_source line 23 · 2026-05-18T07:08:21.941Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014PsKTJdbUUVH9PhiPuTAHN`</summary>

```json
{
  "query": "DeepSeek-Coder-V2-Lite-Base 16B HuggingFace parameters MoE active benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b992dd7-5e04-4f6b-8ac3-fda146cb9f6d",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9cXnMhTqvJ2aNDuAZY2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb003938-011a-421c-abf0-851090ce9499",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NB9dg2TFQahhP1NChMjrUD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 935,
      "cache_creation_input_tokens": 2182,
      "cache_read_input_tokens": 19927,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2182
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 935,
          "output_tokens": 248,
          "cache_read_input_tokens": 19927,
          "cache_creation_input_tokens": 2182,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2182,
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

_source line 24 · 2026-05-18T07:08:28.219Z_

<details><summary>↩ Tool result · `toolu_01HwhzW91FS2ggAX9YTzTGaZ`</summary>

```text
Web search results for query: "microsoft/phi-4 HuggingFace benchmark MMLU training data size tokens gated access"

Links: [{"title":"microsoft/phi-4 · Hugging Face","url":"https://huggingface.co/microsoft/phi-4"},{"title":"microsoft/Phi-4-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning"},{"title":"microsoft/Phi-4-reasoning-plus · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-plus"},{"title":"microsoft/Phi-4-mini-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-instruct"},{"title":"phi-4 | AI Model Details","url":"https://www.aimodels.fyi/models/huggingFace/phi-4-microsoft"},{"title":"GitHub - microsoft/MMLU-CF: A Contamination-free Multi-task Language Understanding Benchmark [Official, ACL 2025] · GitHub","url":"https://github.com/microsoft/MMLU-CF"},{"title":"microsoft/Phi-4-multimodal-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-multimodal-instruct"},{"title":"Microsoft AI Just Released Phi-4: A Small Language Model Available on Hugging Face Under the MIT License - MarkTechPost","url":"https://www.marktechpost.com/2025/01/08/microsoft-ai-just-fully-open-sourced-phi-4-a-small-language-model-available-on-hugging-face-under-the-mit-license/"},{"title":"Phi-4: Small Language Models That Pack a Punch | Microsoft Community Hub","url":"https://techcommunity.microsoft.com/blog/educatordeveloperblog/phi-4-small-language-models-that-pack-a-punch/4464167"},{"title":"microsoft/phi-4-gguf · Hugging Face","url":"https://huggingface.co/microsoft/phi-4-gguf"}]

Based on the search results, here's what I found about microsoft/phi-4 on HuggingFace:

## MMLU Benchmark Performance
Phi-4 scores 84.8% on MMLU (a broad test of knowledge across 57 subjects), and achieved 84.8% on MMLU, 80.4% on MATH, and 82.6% on HumanEval.

## Training Data Size
Microsoft trained it on 9.8 trillion tokens over three weeks, using a mix of synthetic data (generated by larger models like GPT-4o) and high-quality web content.

## Model Architecture
Phi-4 represents Microsoft's latest advancement in language modeling, featuring 14B parameters and a 16K token context length.

## Training Sources
The training data is an extension of the data used for Phi-3 and includes publicly available documents filtered rigorously for quality, selected high-quality educational data and code, newly created synthetic "textbook-like" data for teaching math, coding, common sense reasoning and general knowledge, acquired academic books and Q&A datasets, and high quality chat format supervised data covering various topics.

## Gated Access
The model is available on HuggingFace under the MIT license with open access - Phi-4 is hosted on Hugging Face under the MIT license, so it does not appear to have gated access restrictions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c27f27ef-bc25-4787-84a7-c7dc491441ad",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "145a069e-4112-44f9-b04c-1b8572aedc78",
  "sourceToolAssistantUUID": "c27f27ef-bc25-4787-84a7-c7dc491441ad",
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

_source line 25 · 2026-05-18T07:08:28.230Z_

<details><summary>↩ Tool result · `toolu_01WBntCuDtM4WNQSMmgyTAwg`</summary>

```text
Web search results for query: "DeepSeek-R1-Distill-Qwen-14B DeepSeek-R1-Distill-Qwen-7B HuggingFace base model benchmark"

Links: [{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-14B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-7B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-32B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B"},{"title":"litert-community/DeepSeek-R1-Distill-Qwen-1.5B · Hugging Face","url":"https://huggingface.co/litert-community/DeepSeek-R1-Distill-Qwen-1.5B"},{"title":"unsloth/DeepSeek-R1-Distill-Qwen-14B · Hugging Face","url":"https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-14B"},{"title":"Mungert/DeepSeek-R1-Distill-Qwen-14B-GGUF · Hugging Face","url":"https://huggingface.co/Mungert/DeepSeek-R1-Distill-Qwen-14B-GGUF"},{"title":"stelterlab/DeepSeek-R1-Distill-Qwen-14B-AWQ · Hugging Face","url":"https://huggingface.co/stelterlab/DeepSeek-R1-Distill-Qwen-14B-AWQ"},{"title":"deepseek-ai/DeepSeek-R1 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1"},{"title":"unsloth/DeepSeek-R1-Distill-Qwen-32B · Hugging Face","url":"https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-32B"}]

Based on the search results, here's what I found about the DeepSeek-R1-Distill-Qwen models on HuggingFace:

## Model Overview

DeepSeek has open-sourced distilled 1.5B, 7B, 8B, 14B, 32B, and 70B checkpoints based on Qwen2.5 and Llama3 series.

## Benchmark Performance

The evaluation results demonstrate that the distilled smaller dense models perform exceptionally well on benchmarks. DeepSeek-R1-Distill-Qwen-32B outperforms OpenAI-o1-mini across various benchmarks, achieving new state-of-the-art results for dense models.

## Model Development

DeepSeek-R1-Distill models are fine-tuned based on open-source models, using samples generated by DeepSeek-R1. Specifically, DeepSeek-R1-Distill-Qwen-1.5B, DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Qwen-14B and DeepSeek-R1-Distill-Qwen-32B are derived from Qwen-2.5 series, which are originally licensed under Apache 2.0 License, and now finetuned with 800k samples curated with DeepSeek-R1.

## Evaluation Settings

For benchmarks requiring sampling, they use a temperature of 0.6, a top-p value of 0.95, and generate 64 responses per query to estimate pass@1.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b992dd7-5e04-4f6b-8ac3-fda146cb9f6d",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "3b2fc2a8-b4a1-44e9-89e3-43274734a892",
  "sourceToolAssistantUUID": "8b992dd7-5e04-4f6b-8ac3-fda146cb9f6d",
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

_source line 26 · 2026-05-18T07:08:29.516Z_

<details><summary>↩ Tool result · `toolu_014PsKTJdbUUVH9PhiPuTAHN`</summary>

```text
Web search results for query: "DeepSeek-Coder-V2-Lite-Base 16B HuggingFace parameters MoE active benchmark"

Links: [{"title":"deepseek-ai/DeepSeek-Coder-V2-Lite-Base · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Base"},{"title":"deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct"},{"title":"DeepSeek-Coder V2 Lite Instruct","url":"https://www.emergentmind.com/topics/deepseek-coder-v2-lite-instruct"},{"title":"GitHub - deepseek-ai/DeepSeek-Coder-V2: DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-Coder-V2"},{"title":"deepseek-ai/DeepSeek-V2-Lite · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V2-Lite"},{"title":"deepseek-ai/deepseek-coder-v2-lite-instruct | Run with an API on Replicate","url":"https://replicate.com/deepseek-ai/deepseek-coder-v2-lite-instruct"},{"title":"deepseek-coder-v2:16b-lite-instruct-fp16","url":"https://ollama.com/library/deepseek-coder-v2:16b-lite-instruct-fp16"},{"title":"DeepSeek-Coder-V2: An Open-Source Marvel in Code Intelligence | by givkashi | Medium","url":"https://medium.com/@givkashi/deepseek-coder-v2-an-open-source-marvel-in-code-intelligence-e8572f7741e0"},{"title":"Model Variants | deepseek-ai/DeepSeek-Coder-V2 | DeepWiki","url":"https://deepwiki.com/deepseek-ai/DeepSeek-Coder-V2/2.1-model-variants"},{"title":"deepseek-coder-v2:16b","url":"https://ollama.com/library/deepseek-coder-v2:16b"}]

Based on the search results, here's the information about DeepSeek-Coder-V2-Lite-Base 16B parameters and MoE active parameters:

## Parameters and MoE Configuration

DeepSeek-Coder-V2-Lite-Base has 16B parameters based on the DeepSeekMoE framework, with only 2.4B active parameters. 

This means that for any given input, the model routes the computation through only about 15% of its total parameters (for Lite variants).

## Model Architecture Details

For the Lite variant specifically, each MoE layer consists of 2 shared experts and 64 routed experts, where 6 experts will be activated for each token, resulting in 15.7B total parameters with 2.4B activated for each token.

## Benchmark Performance

In standard benchmark evaluations, DeepSeek-Coder-V2 achieves superior performance compared to closed-source models such as GPT4-Turbo, Claude 3 Opus, and Gemini. Additionally, the full-sized models consistently outperform the Lite variants across all benchmarks, with the full DeepSeek-Coder-V2-Instruct model competing with or exceeding the performance of GPT-4-Turbo on many code and mathematical reasoning tasks.

The model is available on HuggingFace at the official DeepSeek-AI repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb003938-011a-421c-abf0-851090ce9499",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "50852bda-fa70-41cc-a113-f384e34cf2c2",
  "sourceToolAssistantUUID": "fb003938-011a-421c-abf0-851090ce9499",
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

_source line 27 · 2026-05-18T07:08:34.215Z_

Let me get more specific benchmark numbers and check on a few more models.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50852bda-fa70-41cc-a113-f384e34cf2c2",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9cYmFzvwrxkKGX1jWNm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9911c3c-d76c-4ba7-8cea-ef2b1fdb7aac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MaZ6XxEVW2ZS7NBuyWRTsg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4289,
      "cache_read_input_tokens": 22109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4289,
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

_source line 28 · 2026-05-18T07:08:34.739Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Tr51pgpA5SvebdBXNEf7em`</summary>

```json
{
  "query": "DeepSeek-R1-Distill-Qwen-14B benchmark MMLU MATH AIME pass@1 scores"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9911c3c-d76c-4ba7-8cea-ef2b1fdb7aac",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9cYmFzvwrxkKGX1jWNm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "681bef2b-98a5-4a13-88b0-55a2c9a643f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MaZ6XxEVW2ZS7NBuyWRTsg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4289,
      "cache_read_input_tokens": 22109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4289,
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

_source line 29 · 2026-05-18T07:08:35.703Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RkknRkQyGS8BttodDkMAzn`</summary>

```json
{
  "query": "Phi-4 mini 3.8B base pretrained model HuggingFace release date benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "681bef2b-98a5-4a13-88b0-55a2c9a643f8",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9cYmFzvwrxkKGX1jWNm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5241baa7-6448-4c25-9e3b-d98fca2b0052",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MaZ6XxEVW2ZS7NBuyWRTsg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4289,
      "cache_read_input_tokens": 22109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4289,
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

_source line 30 · 2026-05-18T07:08:36.245Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017ySAP5VC24qGWY2CAMipjh`</summary>

```json
{
  "query": "open source base LLM 7B 8B 14B released 2025 2026 Qwen Llama Gemma Mistral"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5241baa7-6448-4c25-9e3b-d98fca2b0052",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9cYmFzvwrxkKGX1jWNm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8fe4e97-a93d-4874-b9de-00ac934c20c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MaZ6XxEVW2ZS7NBuyWRTsg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4289,
      "cache_read_input_tokens": 22109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4289,
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

_source line 31 · 2026-05-18T07:08:40.398Z_

<details><summary>↩ Tool result · `toolu_01Tr51pgpA5SvebdBXNEf7em`</summary>

```text
Web search results for query: "DeepSeek-R1-Distill-Qwen-14B benchmark MMLU MATH AIME pass@1 scores"

Links: [{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2501.12948v1"},{"title":"GitHub - deepseek-ai/DeepSeek-R1 · GitHub","url":"https://github.com/deepseek-ai/deepseek-r1"},{"title":"deepseek-ai/DeepSeek-R1 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1"},{"title":"DeepSeek-R1-Distill-Qwen-14B - Model Info, Parameters, Benchmarks - SiliconFlow\"","url":"https://www.siliconflow.com/models/deepseek-r1-distill-qwen-14b"},{"title":"DeepSeek R1 Distill Qwen 14B: Pricing, Benchmarks & Performance","url":"https://llm-stats.com/models/deepseek-r1-distill-qwen-14b"},{"title":"DeepSeek-R1: Features, o1 Comparison, Distilled Models & More | DataCamp","url":"https://www.datacamp.com/blog/deepseek-r1"},{"title":"Deployment-ready reasoning with quantized DeepSeek-R1 models | Red Hat Developer","url":"https://developers.redhat.com/articles/2025/03/03/deployment-ready-reasoning-quantized-deepseek-r1-models"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-7B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"},{"title":"How to Benchmark DeepSeek-R1 Distilled Models on GPQA Using Ollama and OpenAI’s simple-evals | Towards Data Science","url":"https://towardsdatascience.com/how-to-benchmark-deepseek-r1-distilled-models-on-gpqa-using-ollama-and-openais-simple-evals/"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-14B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B"}]

Based on the search results, I found benchmark scores for DeepSeek-R1-Distill-Qwen-14B:

## Benchmark Scores for DeepSeek-R1-Distill-Qwen-14B (Pass@1)

**AIME 2024:** 69.7% pass rate

**MATH-500:** 93.9% accuracy

**MMLU:** The search results do not contain specific MMLU pass@1 scores for the 14B distilled model specifically. However, DeepSeek-R1 (the full model) achieves 90.8% on MMLU.

The search results indicate that for benchmarks requiring sampling, a temperature of 0.6, a top-p value of 0.95, and 64 responses per query are generated to estimate pass@1.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "681bef2b-98a5-4a13-88b0-55a2c9a643f8",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "d258e898-92cf-47af-8bc2-67ed7a1b3c59",
  "sourceToolAssistantUUID": "681bef2b-98a5-4a13-88b0-55a2c9a643f8",
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

_source line 32 · 2026-05-18T07:08:43.680Z_

<details><summary>↩ Tool result · `toolu_01RkknRkQyGS8BttodDkMAzn`</summary>

```text
Web search results for query: "Phi-4 mini 3.8B base pretrained model HuggingFace release date benchmark"

Links: [{"title":"microsoft/Phi-4-mini-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-instruct"},{"title":"Phi-4 Local Setup: Microsoft's 14B Reasoning on 12GB GPUs | Local AI Master","url":"https://localaimaster.com/blog/phi-4-local-setup"},{"title":"microsoft/Phi-4-mini-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-reasoning"},{"title":"unsloth/Phi-4-mini-reasoning-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Phi-4-mini-reasoning-GGUF"},{"title":"Phi-4 Mini: Microsoft's Best Small Model (3.8B) — Guide & Benchmarks | Local AI Master","url":"https://localaimaster.com/models/phi-4-mini"},{"title":"microsoft/Phi-3-mini-4k-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-3-mini-4k-instruct"},{"title":"microsoft/Phi-4-mini-flash-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-flash-reasoning"},{"title":"unsloth/Phi-4-mini-instruct-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Phi-4-mini-instruct-GGUF"},{"title":"microsoft/Phi-3.5-mini-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-3.5-mini-instruct"},{"title":"Mungert/Phi-4-mini-reasoning-GGUF · Hugging Face","url":"https://huggingface.co/Mungert/Phi-4-mini-reasoning-GGUF"}]

Based on the search results, here's the information about Phi-4 mini 3.8B:

## Release Information

Phi-4 (microsoft/phi-4 on HuggingFace) is the December 2024 release of Microsoft's Phi family. More specifically, Phi-4 Mini was published on March 19, 2026, representing a later update to the Phi-4 family.

## Base Model Availability

The search results primarily show instruct and reasoning variants of Phi-4-mini rather than explicit base pretrained models. However, the 3.8B parameters Phi-4-mini-instruct model was compared with a set of models over a variety of benchmarks using an internal benchmark platform.

## Benchmark Performance

The model with only 3.8B-param achieves a similar level of multilingual language understanding and reasoning ability as much larger models. More specifically, Phi-4 Mini matches Llama 3.1 8B on MMLU (73%) while using half the memory and running 2x faster.

For reasoning-focused variants, the 3.8B parameters Phi-4-mini-reasoning model was compared with a set of models over a variety of reasoning benchmarks, evaluating with Math-500, AIME 2024, and GPQA Diamond benchmarks.

## Technical Details

Phi-4-mini-instruct has 3.8B parameters and is a dense decoder-only Transformer model. Phi-4-mini's training data includes a wide variety of sources, totaling 5 trillion tokens.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5241baa7-6448-4c25-9e3b-d98fca2b0052",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "4b336932-fbe6-4a43-bb44-55395ddf86f5",
  "sourceToolAssistantUUID": "5241baa7-6448-4c25-9e3b-d98fca2b0052",
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

_source line 33 · 2026-05-18T07:08:47.993Z_

<details><summary>↩ Tool result · `toolu_017ySAP5VC24qGWY2CAMipjh`</summary>

```text
Web search results for query: "open source base LLM 7B 8B 14B released 2025 2026 Qwen Llama Gemma Mistral"

Links: [{"title":"Best Open-Source LLM Models in 2026: Coding, Local, Agentic AI, Benchmarks, and License","url":"https://huggingface.co/blog/daya-shankar/open-source-llms"},{"title":"Open-Source LLMs Compared 2026 – 25+ Models… – Till Freitag","url":"https://till-freitag.com/en/blog/open-source-llm-comparison"},{"title":"Best Open-Source LLMs in 2026 - Featherless","url":"https://featherless.ai/blog/best-open-source-llms-2026"},{"title":"Best Open Source LLMs in 2026: DeepSeek, Llama & More","url":"https://www.miniloop.ai/blog/best-open-source-llms-2026"},{"title":"Open-Source LLM Landscape 2026, 15+ Model Families Mapped | Presenc AI","url":"https://presenc.ai/research/open-source-llm-landscape-2026"},{"title":"Open-Source LLM Landscape 2026: DeepSeek V4 vs Llama 4 vs Qwen 3.5 vs Gemma 4","url":"https://codersera.com/blog/open-source-llms-landscape-2026/"},{"title":"Top 7 open source LLMs for 2026","url":"https://www.instaclustr.com/education/open-source-ai/top-7-open-source-llms-for-2026/"},{"title":"Best Open-Source LLM 2026: 8 Tested, 3 Beat GPT-4 | TECHSY","url":"https://techsy.io/en/blog/best-open-source-llms-2026"},{"title":"library","url":"https://ollama.com/library"},{"title":"Open Source LLM Comparison Table (2026) | ComputingForGeeks","url":"https://computingforgeeks.com/open-source-llm-comparison/"}]

Based on the search results, here's a comprehensive overview of open source base LLMs in the 7B-14B range released in 2025-2026 from the major providers you mentioned:

## Qwen
Qwen 3.5 (released February 2026) is a native vision-language model with 397B total parameters (17B active per pass), supporting 201 languages and offering a 1M token context window. The Qwen 3 family also includes smaller variants (32B, 14B, 8B, 4B) that run on consumer hardware. Qwen3 is a strong fit when you need multilingual support, commercial flexibility, and a broad ecosystem of fine-tunes, quantizations, and deployment examples.

## Llama
Meta's Llama family remains the most influential open-source LLM series, and the latest generation, Llama 4, released in April 2025, is Meta's first natively multimodal model family and its first to use a mixture-of-experts (MoE) architecture. Llama 4 Scout fits on a single NVIDIA H100 GPU and offers an industry-leading 10M token context window, outperforming previous-generation models like Gemma 3 and Mistral 3.1 across a broad range of benchmarks.

## Gemma
Google's open model family ranges from 1B to 27B – optimized for on-device use. Gemma 4 26B A4B is the most practical local model recommendation for many developers, with Apache 2.0 licensing, 25.2B total parameters, 3.8B active parameters, text and image support, and a 256K token context window.

## Mistral
The 7B model released by Mistral AI, updated to version 0.3. Mistral's flagship features 123B parameters, 128k context, 80+ languages. Both Mistral Large 3 and Mistral Small 4 now ship under Apache 2.0, a significant shift from Mistral's earlier restrictive licensing.

## Key Licensing Notes
LLaMA uses the Meta Community License, Mistral uses Apache 2.0, Qwen uses Apache 2.0, and DeepSeek uses MIT. Apache 2.0 has won the license war for permissive labs, with Gemma 4, Qwen 3.5, Mistral Large 3, and Yi all shipping under Apache 2.0; DeepSeek V4 ships MIT; and Llama 4 keeps the Meta custom license with the 700M MAU clause.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8fe4e97-a93d-4874-b9de-00ac934c20c9",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "28ce173e-2080-43ba-8162-352e2a1923f2",
  "sourceToolAssistantUUID": "c8fe4e97-a93d-4874-b9de-00ac934c20c9",
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

_source line 34 · 2026-05-18T07:08:50.395Z_

Let me get more details on the specific models in the 7B-14B range.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28ce173e-2080-43ba-8162-352e2a1923f2",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9ca82gdjARmwEBSBbwH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6720a4b7-5b87-4eb4-9a27-6e0f74219f1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015f4Aixw9EZrsqfourjXbjK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3267,
      "cache_read_input_tokens": 26398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3267,
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

_source line 35 · 2026-05-18T07:08:51.585Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013HYTL2dHVWtVEVhtKkDC36`</summary>

```json
{
  "query": "Qwen3 7B 8B 14B base model HuggingFace release date benchmark MMLU parameters 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6720a4b7-5b87-4eb4-9a27-6e0f74219f1b",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9ca82gdjARmwEBSBbwH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "26e629f3-c4bd-4369-8362-7da1772d558a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015f4Aixw9EZrsqfourjXbjK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3267,
      "cache_read_input_tokens": 26398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3267,
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

_source line 36 · 2026-05-18T07:08:52.316Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PtZj1rmNwwwPryZKyp3r3x`</summary>

```json
{
  "query": "Gemma 3 7B 12B base model HuggingFace release date 2025 benchmark parameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26e629f3-c4bd-4369-8362-7da1772d558a",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9ca82gdjARmwEBSBbwH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "baa8a974-1363-4d5a-bbe5-ef6f475b25e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015f4Aixw9EZrsqfourjXbjK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3267,
      "cache_read_input_tokens": 26398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3267,
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

_source line 37 · 2026-05-18T07:08:52.668Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E4hPcgTXBxwZ8ctz3NfZHi`</summary>

```json
{
  "query": "Llama 4 Scout Maverick 7B 8B parameters MoE active base model HuggingFace 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "baa8a974-1363-4d5a-bbe5-ef6f475b25e9",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9ca82gdjARmwEBSBbwH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4561fe72-56de-452a-b74a-dc35bc60d16f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015f4Aixw9EZrsqfourjXbjK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3267,
      "cache_read_input_tokens": 26398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3267,
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

_source line 38 · 2026-05-18T07:08:58.935Z_

<details><summary>↩ Tool result · `toolu_01PtZj1rmNwwwPryZKyp3r3x`</summary>

```text
Web search results for query: "Gemma 3 7B 12B base model HuggingFace release date 2025 benchmark parameters"

Links: [{"title":"Gemma 3 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/gemma3"},{"title":"Gemma 3 Release - a google Collection","url":"https://huggingface.co/collections/google/gemma-3-release"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"google/gemma-3-12b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-it"},{"title":"Google's Gemma 3: Features, Benchmarks, Performance and Implementation","url":"https://www.analyticsvidhya.com/blog/2025/03/gemma-3/"},{"title":"google/gemma-3-27b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-27b-it"},{"title":"Gemma 3 12B Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/gemma-3-12b-it"},{"title":"google/gemma-7b · Hugging Face","url":"https://huggingface.co/google/gemma-7b"},{"title":"Gemma releases | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/releases"},{"title":"Gemma 3: Google’s new open model based on Gemini 2.0","url":"https://blog.google/technology/developers/gemma-3/"}]

Based on the search results, here's the information about Gemma 3:

## Model Sizes and Parameters

Gemma 3 is a multimodal model with pretrained and instruction-tuned variants, available in 1B, 13B, and 27B parameters. However, other sources indicate it comes in four distinct sizes – 1B, 4B, 12B, and 27B parameters with both base (pre-trained) and instruction-tuned variants. Note that there is no 7B variant in Gemma 3; the search results mention a 4B and 12B model instead.

## Release Date

Gemma 3 12B was released on March 12, 2025 by Google.

## Training Data

The 27B model was trained with 14 trillion tokens, the 12B model was trained with 12 trillion tokens, 4B model was trained with 4 trillion tokens and 1B with 2 trillion tokens.

## Key Features and Benchmarks

Gemma 3 has a large, 128K context window, multilingual support in over 140 languages, and is available in more sizes than previous versions. 

Regarding performance, Gemma 3 delivers state-of-the-art performance for its size, outperforming Llama3-405B, DeepSeek-V3 and o3-mini in preliminary human preference evaluations on LMArena's leaderboard.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "baa8a974-1363-4d5a-bbe5-ef6f475b25e9",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "9fb907b4-5ef6-485b-8a96-417e4ee85b12",
  "sourceToolAssistantUUID": "baa8a974-1363-4d5a-bbe5-ef6f475b25e9",
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

_source line 39 · 2026-05-18T07:08:59.722Z_

<details><summary>↩ Tool result · `toolu_013HYTL2dHVWtVEVhtKkDC36`</summary>

```text
Web search results for query: "Qwen3 7B 8B 14B base model HuggingFace release date benchmark MMLU parameters 2025"

Links: [{"title":"Qwen/Qwen3.6-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-27B"},{"title":"Qwen/Qwen3.5-9B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-9B"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series developed by Qwen team, Alibaba Group. · GitHub","url":"https://github.com/QwenLM/Qwen3.6"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Qwen/Qwen3.5-0.8B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-0.8B"},{"title":"Qwen/Qwen3-14B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B-Base"},{"title":"Qwen/Qwen3.5-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-27B"},{"title":"Qwen/Qwen3-8B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B-Base"},{"title":"GitHub - QwenLM/Qwen: The official repo of Qwen (通义千问) chat & pretrained large language model proposed by Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen"}]

Based on the search results, here's the information about Qwen3 models:

## Release Date and Model Sizes

Qwen3 was announced as the latest addition to the Qwen family of large language models, with the release occurring in 2025. Six dense models were open-weighted, including Qwen3-32B, Qwen3-14B, Qwen3-8B, Qwen3-4B, Qwen3-1.7B, and Qwen3-0.6B, under Apache 2.0 license.

## Model Parameters and Performance

The overall performance of Qwen3 dense base models matches that of Qwen2.5 base models with more parameters. For instance, Qwen3-1.7B/4B/8B/14B/32B-Base performs as well as Qwen2.5-3B/7B/14B/32B/72B-Base, respectively.

## MMLU Benchmark

The search results reference MMLU benchmark testing. For MMLU-ProX, they report the averaged accuracy on 29 languages. However, the specific MMLU scores are mentioned as being available in detailed evaluation results but are not provided in the excerpts returned.

## HuggingFace Availability

The post-trained models and their pre-trained counterparts are now available on platforms like Hugging Face, ModelScope, and Kaggle. You can access the base models directly on HuggingFace's model hub with model IDs like `Qwen/Qwen3-8B-Base`, `Qwen/Qwen3-14B-Base`, etc.

For detailed benchmark results including specific MMLU scores, you may want to refer to the official Qwen blog post or the technical report mentioned in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26e629f3-c4bd-4369-8362-7da1772d558a",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "72109dc4-e0ef-4f78-b8f2-b7f3df63e2d3",
  "sourceToolAssistantUUID": "26e629f3-c4bd-4369-8362-7da1772d558a",
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

_source line 40 · 2026-05-18T07:09:01.040Z_

<details><summary>↩ Tool result · `toolu_01E4hPcgTXBxwZ8ctz3NfZHi`</summary>

```text
Web search results for query: "Llama 4 Scout Maverick 7B 8B parameters MoE active base model HuggingFace 2025"

Links: [{"title":"Welcome Llama 4 Maverick & Scout on Hugging Face","url":"https://huggingface.co/blog/llama4-release"},{"title":"The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation","url":"https://ai.meta.com/blog/llama-4-multimodal-intelligence/"},{"title":"Evolution of Meta’s LLaMA Models and Parameter-Efficient Fine-Tuning of Large Language Models: A Survey","url":"https://arxiv.org/html/2510.12178v1"},{"title":"meta-llama/Llama-4-Scout-17B-16E · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E"},{"title":"Llama4 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/llama4"},{"title":"meta-llama (Meta Llama)","url":"https://huggingface.co/meta-llama"},{"title":"Llama 4 (Scout/Maverick) - D-Central","url":"https://d-central.tech/ai/model/llama-4/"},{"title":"Welcome Llama 4 Maverick & Scout on Hugging Face","url":"https://github.com/huggingface/blog/blob/main/llama4-release.md"},{"title":"meta-llama/Llama-4-Maverick-17B-128E-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct"},{"title":"meta-llama/Llama-4-Scout-17B-16E-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct"}]

Based on the search results, here's detailed information about Llama 4 Scout and Maverick:

## Model Parameters and Architecture

Llama 4 Maverick (~400B) and Llama 4 Scout (~109B) were released by Meta in 2025. Both models feature Mixture of Experts (MoE) architecture:

- Both are Mixture of Experts (MoE) models with 17B active parameters
- Llama 4 Maverick with 17B active parameters out of ~400B total, with 128 experts
- Llama 4 Scout also has 17B active parameters out of ~109B total, using just 16 experts

## MoE Architecture Details

The two models differ in their expert implementation:

- Llama Scout is a full MoE consisting of 16 experts
- Llama Maverick uses 128 experts, but MoE and dense layers alternate. Therefore, experts are applied in half of the layers

## Availability on HuggingFace

Both Llama 4 Maverick and Llama 4 Scout model weights are available directly on the Hugging Face Hub under the meta-llama organization. This includes both base and instruction tuned variants.

## Context Length and Training Data

The Llama 4 models were pre-trained with a context length of 256K. The Instruct models were fine-tuned to support much larger context lengths: 1M in the large 128 experts version (Maverick), and 10M (!) for the 16 experts version (Scout).

Llama 4 Scout was pretrained on ~40 trillion tokens and Llama 4 Maverick was pretrained on ~22 trillion tokens of multimodal data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4561fe72-56de-452a-b74a-dc35bc60d16f",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "c965c21f-1f88-449f-9a5d-d53e690d1b07",
  "sourceToolAssistantUUID": "4561fe72-56de-452a-b74a-dc35bc60d16f",
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

_source line 41 · 2026-05-18T07:09:03.594Z_

Let me get additional details on a few more specific items.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c965c21f-1f88-449f-9a5d-d53e690d1b07",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9cb5rk7ReZQVr7muU5X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5fa123d-9668-4f2e-8a94-6bcd4ef03b3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RD522mNXRwZzytfigMGV1X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3169,
      "cache_read_input_tokens": 29665,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3169,
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

_source line 42 · 2026-05-18T07:09:04.533Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WNo2ZGCJjkoS9Y9idP5kdi`</summary>

```json
{
  "query": "Qwen3 14B base training tokens data size MMLU benchmark score release date April 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5fa123d-9668-4f2e-8a94-6bcd4ef03b3a",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9cb5rk7ReZQVr7muU5X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b3ba1ba-9ae4-4880-a79a-efa6c3a1bb14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RD522mNXRwZzytfigMGV1X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3169,
      "cache_read_input_tokens": 29665,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3169,
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

_source line 43 · 2026-05-18T07:09:05.534Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GvgZjFUCLx83GyN8QLCnbk`</summary>

```json
{
  "query": "Gemma 3 12B base pretrained \"gemma-3-12b-pt\" HuggingFace gated benchmark MMLU"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b3ba1ba-9ae4-4880-a79a-efa6c3a1bb14",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9cb5rk7ReZQVr7muU5X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9fd5f462-fc5e-4da4-8dda-47fa28035bf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RD522mNXRwZzytfigMGV1X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3169,
      "cache_read_input_tokens": 29665,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3169,
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

_source line 44 · 2026-05-18T07:09:05.936Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012zdEe8pjsiA4f1fqpZ6dCA`</summary>

```json
{
  "query": "Mistral Small 3 7B 8B base model 2025 HuggingFace parameters benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fd5f462-fc5e-4da4-8dda-47fa28035bf1",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9cb5rk7ReZQVr7muU5X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "163020bb-0d72-491c-a57f-562c5eeeaf72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RD522mNXRwZzytfigMGV1X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3169,
      "cache_read_input_tokens": 29665,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3169
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 215,
          "cache_read_input_tokens": 29665,
          "cache_creation_input_tokens": 3169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3169,
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

_source line 45 · 2026-05-18T07:09:10.583Z_

<details><summary>↩ Tool result · `toolu_01WNo2ZGCJjkoS9Y9idP5kdi`</summary>

```text
Web search results for query: "Qwen3 14B base training tokens data size MMLU benchmark score release date April 2025"

Links: [{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Qwen3 14B | Open Laboratory","url":"https://openlaboratory.com/models/qwen3-14b/"},{"title":"An Empirical Study of Qwen3 Quantization","url":"https://arxiv.org/html/2505.02214v1"},{"title":"2025-05-13 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://cdn.jsdelivr.net/gh/yanfeng98/paper-is-all-you-need/papers/00069-Qwen3_Technical_Report.pdf"},{"title":"Qwen3 Technical Report","url":"https://arxiv.org/html/2505.09388v1"},{"title":"An empirical study of Qwen3 quantization | Visual Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44267-026-00114-4"},{"title":"Qwen3 4B | Open Laboratory","url":"https://openlaboratory.ai/models/qwen3-4b"},{"title":"Qwen3 14B - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/qwen3-14b-instruct"},{"title":"Qwen3 0.6B | Open Laboratory","url":"https://openlaboratory.com/models/qwen3-0_6b/"},{"title":"Home GPU LLM Leaderboard: Best Open Source Models by VRAM Tier with Token/s Benchmarks | Awesome Agents","url":"https://awesomeagents.ai/leaderboards/home-gpu-llm-leaderboard/"}]

Based on the search results, here's the information about Qwen3 14B:

## Key Information:

**Release Date:** Qwen3-14B was officially released on April 29, 2025.

**MMLU Benchmark Score:** Qwen3-14B-Base attains scores of 81.05 on MMLU.

**Training Data:** While the search results don't provide the exact training token count specifically for Qwen3-14B, they indicate that the Qwen3 series was developed by Alibaba Cloud's Qwen team and represents a significant advancement in their model lineup.

**Model Size:** Qwen3-14B is a dense model with 14 billion total parameters.

The model demonstrates strong performance across multiple benchmarks and includes hybrid "thinking" and "non-thinking" modes for flexible reasoning capabilities. The model and its weights are made publicly available under the Apache 2.0 license.

Note: The search results did not contain specific information about the exact data size (in terms of training tokens) for Qwen3-14B's pretraining, though this data may be available in the full technical report.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b3ba1ba-9ae4-4880-a79a-efa6c3a1bb14",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "babca3c5-0e2f-4d6d-80ae-e06d7df4a548",
  "sourceToolAssistantUUID": "2b3ba1ba-9ae4-4880-a79a-efa6c3a1bb14",
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

_source line 46 · 2026-05-18T07:09:11.500Z_

<details><summary>↩ Tool result · `toolu_01GvgZjFUCLx83GyN8QLCnbk`</summary>

```text
Web search results for query: "Gemma 3 12B base pretrained "gemma-3-12b-pt" HuggingFace gated benchmark MMLU"

Links: [{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"google/gemma-3-12b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-it"},{"title":"google/gemma-3-12b-pt · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-pt"},{"title":"cjvt/GaMS3-12B-Instruct · Hugging Face","url":"https://huggingface.co/cjvt/GaMS3-12B-Instruct"},{"title":"gemma3:12b","url":"https://ollama.com/library/gemma3:12b"},{"title":"Gemma 3 — Google DeepMind","url":"https://deepmind.google/models/gemma/gemma-3/"},{"title":"litert-community/Gemma3-12B-IT · Hugging Face","url":"https://huggingface.co/litert-community/Gemma3-12B-IT"},{"title":"google/gemma-3-12b-pt at main","url":"https://huggingface.co/google/gemma-3-12b-pt/tree/main"},{"title":"Gemma 3 12B Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/gemma-3-12b-it"},{"title":"INSAIT-Institute/MamayLM-Gemma-3-12B-IT-v1.0 · Hugging Face","url":"https://huggingface.co/INSAIT-Institute/MamayLM-Gemma-3-12B-IT-v1.0"}]

Based on the search results, here's what I found regarding Gemma 3 12B base pretrained model:

## Model Access
To access Gemma on Hugging Face, you're required to review and agree to Google's usage license, and you need to be logged in to Hugging Face. The model is indeed gated on HuggingFace.

## Model Specifications
Gemma 3 models are multimodal, handling text and image input and generating text output, with open weights for both pre-trained variants and instruction-tuned variants. Gemma 3 has a large, 128K context window, multilingual support in over 140 languages, and is available in more sizes than previous versions.

## MMLU Benchmark
Regarding MMLU benchmarks, the search results indicate that Gemma 3 has been evaluated across benchmarks like MMLU-Pro (27B: 67.5), LiveCodeBench (27B: 29.7), and Bird-SQL (27B: 54.4). However, the specific MMLU benchmark scores for the 12B base pretrained variant ("gemma-3-12b-pt") were not included in the search results. The available benchmark data focuses on the 27B model size.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9fd5f462-fc5e-4da4-8dda-47fa28035bf1",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "fb9a4b45-9344-4b85-a28c-0ba2c83402b9",
  "sourceToolAssistantUUID": "9fd5f462-fc5e-4da4-8dda-47fa28035bf1",
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

_source line 47 · 2026-05-18T07:09:17.492Z_

<details><summary>↩ Tool result · `toolu_012zdEe8pjsiA4f1fqpZ6dCA`</summary>

```text
Web search results for query: "Mistral Small 3 7B 8B base model 2025 HuggingFace parameters benchmark"

Links: [{"title":"unsloth/Mistral-Small-24B-Base-2501-bnb-4bit · Hugging Face","url":"https://huggingface.co/unsloth/Mistral-Small-24B-Base-2501-bnb-4bit"},{"title":"Mistral 7B","url":"https://mistral.ai/news/announcing-mistral-7b"},{"title":"unsloth/Mistral-Small-24B-Base-2501 · Hugging Face","url":"https://huggingface.co/unsloth/Mistral-Small-24B-Base-2501"},{"title":"NVIDIA-Accelerated Mistral 3 Open Models Deliver Efficiency, Accuracy at Any Scale | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/nvidia-accelerated-mistral-3-open-models-deliver-efficiency-accuracy-at-any-scale/"},{"title":"Mistral Docs","url":"https://docs.mistral.ai/models/overview"},{"title":"Introducing Mistral 3 | Mistral AI","url":"https://mistral.ai/news/mistral-3"},{"title":"mistralai/Mistral-7B-Instruct-v0.3 · Hugging Face","url":"https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3"},{"title":"mistralai/Mistral-7B-v0.1 · Hugging Face","url":"https://huggingface.co/mistralai/Mistral-7B-v0.1"},{"title":"Mistral · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/mistral"},{"title":"Ministral 3 Abstract","url":"https://arxiv.org/pdf/2601.08584"}]

Based on the search results, here's what I found about Mistral models in 2025:

## Mistral Small 3 (2501)

Mistral Small 3 (2501) sets a new benchmark in the "small" Large Language Models category below 70B, boasting 24B parameters and achieving state-of-the-art capabilities comparable to larger models.

## Ministral 3 Series

For smaller models, Mistral released the Ministral 3 family, which includes multiple parameter sizes:

A suite of small, dense high-performance models (called Ministral 3) of sizes 3B, 8B, and 14B, each with Base, Instruct, and Reasoning variants (nine models total) All the models were trained on NVIDIA Hopper GPUs and are now available through Mistral AI on Hugging Face.

## Performance Benchmarks

The Ministral instruct models match or exceed the performance of comparable models while often producing an order of magnitude fewer tokens. Additionally, Ministral 3 8B outperforms the larger Gemma 12B in most of the evaluations (except TriviaQA), highlighting the strong parameter efficiency of Ministral 3 models.

The Ministral reasoning variants can think longer to produce state-of-the-art accuracy amongst their weight class - for instance 85% on AIME '25 with our 14B variant.

All these models are available on HuggingFace under the Apache 2.0 license.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "163020bb-0d72-491c-a57f-562c5eeeaf72",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "4de84d8a-dcaf-4a48-82d5-25870d65900f",
  "sourceToolAssistantUUID": "163020bb-0d72-491c-a57f-562c5eeeaf72",
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

_source line 48 · 2026-05-18T07:09:26.268Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G98CMuXEmGPRyFJiBk4Doz`</summary>

```json
{
  "query": "Ministral 3 8B 14B base model HuggingFace repo ID release date 2025 2026 training data benchmark MMLU"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4de84d8a-dcaf-4a48-82d5-25870d65900f",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9ccJNbDCDz6CeaMJ424",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4e6eeaf-d987-4f15-a8d2-6fed4345d7a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DximVYVGSmQw7hRTjn1vV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2759,
      "cache_read_input_tokens": 32834,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2759,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 51,
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

_source line 49 · 2026-05-18T07:09:26.432Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YVHFp9Vm2wqTh7xANos3ce`</summary>

```json
{
  "query": "Qwen3 8B 14B base training data tokens pretraining technical report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4e6eeaf-d987-4f15-a8d2-6fed4345d7a3",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9ccJNbDCDz6CeaMJ424",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f747e1a4-3685-4979-9f43-800f9f285772",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DximVYVGSmQw7hRTjn1vV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2759,
      "cache_read_input_tokens": 32834,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2759,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 51,
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

_source line 50 · 2026-05-18T07:09:26.516Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019e5HAbuVBBLensc33Hy7Yk`</summary>

```json
{
  "query": "DeepSeek V2 Lite base 15.7B HuggingFace release date gated benchmark MMLU training tokens"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f747e1a4-3685-4979-9f43-800f9f285772",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9ccJNbDCDz6CeaMJ424",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "acef8e8d-221f-4bac-8ab2-1d1c4e85fa97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DximVYVGSmQw7hRTjn1vV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2759,
      "cache_read_input_tokens": 32834,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2759,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 51,
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

_source line 51 · 2026-05-18T07:09:33.457Z_

<details><summary>↩ Tool result · `toolu_019e5HAbuVBBLensc33Hy7Yk`</summary>

```text
Web search results for query: "DeepSeek V2 Lite base 15.7B HuggingFace release date gated benchmark MMLU training tokens"

Links: [{"title":"deepseek-ai/DeepSeek-V2-Lite · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V2-Lite"},{"title":"deepseek-ai/DeepSeek-V4-Pro · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"},{"title":"deepseek-ai/DeepSeek-Coder-V2-Lite-Base · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Base"},{"title":"deepseek-ai/DeepSeek-V2-Lite-Chat · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V2-Lite-Chat"},{"title":"lmstudio-community/DeepSeek-Coder-V2-Lite-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/lmstudio-community/DeepSeek-Coder-V2-Lite-Instruct-GGUF"},{"title":"GitHub - deepseek-ai/DeepSeek-Coder-V2: DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-Coder-V2"},{"title":"deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct"},{"title":"deepseek-ai/DeepSeek-V2 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V2"},{"title":"deepseek-ai/DeepSeek-Coder-V2-Base · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Base"},{"title":"GitHub - deepseek-ai/DeepSeek-LLM: DeepSeek LLM: Let there be answers · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-LLM"}]

Based on the search results, here's what I found about DeepSeek V2 Lite base 15.7B:

**Model Architecture & Parameters:**
DeepSeek-V2-Lite comprises 15.7B total parameters, of which 2.4B are activated for each token.

**Training Details:**
During pre-training, the maximum sequence length was set to 4K, and DeepSeek-V2-Lite was trained on 5.7T tokens. DeepSeek-V2-Lite was trained from scratch on the same pre-training corpus of DeepSeek-V2, which is not polluted by any SFT data.

**Release Date:**
DeepSeek-V2-Lite comes out with 16B total params, 2.4B active params, scratch training with 5.7T tokens. According to the metadata, this was released on May 7, 2024.

**Performance:**
DeepSeek-V2-Lite outperforms 7B dense and 16B MoE on many English & Chinese benchmarks.

However, I didn't find specific information in the search results about MMLU benchmark scores or whether the model is gated on HuggingFace. You may need to check the HuggingFace model card directly for those specific details.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acef8e8d-221f-4bac-8ab2-1d1c4e85fa97",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "4e0de0ee-4fe4-435c-8475-0ea5b5efd45f",
  "sourceToolAssistantUUID": "acef8e8d-221f-4bac-8ab2-1d1c4e85fa97",
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

_source line 52 · 2026-05-18T07:09:33.511Z_

<details><summary>↩ Tool result · `toolu_01YVHFp9Vm2wqTh7xANos3ce`</summary>

```text
Web search results for query: "Qwen3 8B 14B base training data tokens pretraining technical report"

Links: [{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Qwen3-8B-Base: Open 8B LLM Overview","url":"https://www.emergentmind.com/topics/qwen3-8b-base"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"Qwen/Qwen3-14B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B-Base"},{"title":"[Literature Review] Qwen3 Technical Report","url":"https://www.themoonlight.io/en/review/qwen3-technical-report"},{"title":"Qwen3 Technical Report","url":"https://arxiv.org/html/2505.09388v1"},{"title":"2025-05-13 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://cdn.jsdelivr.net/gh/yanfeng98/paper-is-all-you-need/papers/00069-Qwen3_Technical_Report.pdf"},{"title":"(PDF) QWEN TECHNICAL REPORT","url":"https://www.researchgate.net/publication/377112868_QWEN_TECHNICAL_REPORT"},{"title":"Qwen3 Technical Report: Reasoning in Pre-Training and Post-Training","url":"https://thesalt.substack.com/p/qwen3-technical-report-reasoning"},{"title":"Qwen/Qwen3-8B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B-Base"}]

Based on the search results, here's the information about Qwen3 8B and 14B base models' pretraining details from the technical report:

## Pretraining Data and Tokens

Qwen3 uses approximately 36 trillion tokens covering 119 languages and dialects, which is a significant expansion compared to its predecessor.

### Three-Stage Pretraining Process

In the first stage (S1), the model was pretrained on over 30 trillion tokens with a context length of 4K tokens, which provided the model with basic language skills and general knowledge. In the second stage (S2), the dataset was improved by increasing the proportion of knowledge-intensive data such as STEM, coding, and reasoning tasks, and the model was pretrained on an additional 5 trillion tokens. In the final stage, high-quality long-context data was used to extend the context length to 32K tokens.

### Data Sources

Pretraining spans 36 trillion tokens covering 119 languages and dialects, sourced from web crawls, OCR-extracted PDFs, Wikipedia, code repositories, and synthetic STEM/coding datasets.

### Model Performance

Qwen3-1.7B/4B/8B/14B/32B-Base performs as well as Qwen2.5-3B/7B/14B/32B/72B-Base, respectively.

The official Qwen3 Technical Report is available on arXiv (2505.09388) for more detailed information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f747e1a4-3685-4979-9f43-800f9f285772",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "62ba2887-7441-4831-91e4-7eee0892538a",
  "sourceToolAssistantUUID": "f747e1a4-3685-4979-9f43-800f9f285772",
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

_source line 53 · 2026-05-18T07:09:42.139Z_

<details><summary>↩ Tool result · `toolu_01G98CMuXEmGPRyFJiBk4Doz`</summary>

```text
Web search results for query: "Ministral 3 8B 14B base model HuggingFace repo ID release date 2025 2026 training data benchmark MMLU"

Links: [{"title":"mistralai/Ministral-3-3B-Instruct-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512"},{"title":"mistralai/Ministral-3-14B-Instruct-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512"},{"title":"mistralai/Ministral-3-8B-Base-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-8B-Base-2512"},{"title":"Ministral3","url":"https://huggingface.co/docs/transformers/main/en/model_doc/ministral3"},{"title":"mistralai/Ministral-3-14B-Reasoning-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-14B-Reasoning-2512"},{"title":"mistralai/Ministral-3-3B-Base-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-3B-Base-2512"},{"title":"Ministral 3 - a mistralai Collection","url":"https://huggingface.co/collections/mistralai/ministral-3"},{"title":"mistralai/Ministral-3-14B-Base-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-14B-Base-2512"},{"title":"mistralai/Ministral-3-14B-Instruct-2512-BF16 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512-BF16"},{"title":"mistralai/Ministral-3-8B-Reasoning-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-8B-Reasoning-2512"}]

Now let me search for more specific information about training data and benchmark performance including MMLU scores:

Links: [{"title":"Ministral 3 Abstract","url":"https://arxiv.org/pdf/2601.08584"},{"title":"Multilingual MMLU Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/multilingual-mmlu"},{"title":"Mistral: Ministral 3B Free Chat Online - Skywork ai","url":"https://skywork.ai/blog/models/mistral-ministral-3b-free-chat-online/"},{"title":"Mistral 3: Model Family, Architecture, Benchmarks & More - CometAPI - All AI Models in One API","url":"https://www.cometapi.com/mistral-3-model-family-architecture-benchmarks-more/"},{"title":"MMLU - Wikipedia","url":"https://en.wikipedia.org/wiki/MMLU"},{"title":"Min istral 3 (3B Reasoning 2512): Pricing, Benchmarks & Performance","url":"https://llm-stats.com/models/ministral-3b-latest"},{"title":"MMLU | DeepEval by Confident AI - The LLM Evaluation Framework","url":"https://deepeval.com/docs/benchmarks-mmlu"},{"title":"Ministral 3","url":"https://arxiv.org/html/2601.08584v1"},{"title":"What is MMLU? LLM Benchmark Explained and Why It Matters | DataCamp","url":"https://www.datacamp.com/blog/what-is-mmlu"},{"title":"MMLU Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/mmlu"}]

Now let me search for more specific information about the training data composition:

Links: [{"title":"Ministral 3","url":"https://arxiv.org/html/2601.08584v1"},{"title":"Ministral 3 Abstract","url":"https://arxiv.org/pdf/2601.08584"},{"title":"Introducing Mistral 3 | Mistral AI","url":"https://mistral.ai/news/mistral-3"},{"title":"Ministral 3 3B - Mistral AI | Mistral Docs","url":"https://docs.mistral.ai/models/ministral-3-3b-25-12"},{"title":"Fine-Tuning Ministral 3: A Step-by-Step Guide to Training a Vision-Language Model for X-Ray Classification | DataCamp","url":"https://www.datacamp.com/tutorial/fine-tuning-ministral-3"},{"title":"Mistral 3 Models on DigitalOcean | DigitalOcean","url":"https://www.digitalocean.com/community/tutorials/mistral-3-models"},{"title":"Mistral Large 3: An Open-Source MoE LLM Explained | IntuitionLabs","url":"https://intuitionlabs.ai/articles/mistral-large-3-moe-llm-explained"},{"title":"mistralai/Ministral-3-3B-Instruct-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512"},{"title":"mistralai/Ministral-3-3B-Base-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-3B-Base-2512"},{"title":"Mistral 3 : Best Open-sourced model is here !! | by Mehul Gupta | Data Science in Your Pocket | Medium","url":"https://medium.com/data-science-in-your-pocket/mistral-3-best-open-sourced-model-is-here-3b93a6b2b2e8"}]

Based on my web search results, here's a comprehensive summary of the Ministral 3 models:

## Release Information

The Ministral 3 models were released on December 1, 2025, and added to Hugging Face Transformers on the same date. The models were updated on December 2, 2025.

## Model Sizes and HuggingFace Repository IDs

The Ministral 3 family consists of edge models with Base, Instruct, and Reasoning variants in three different sizes: 3B, 8B, and 14B. The HuggingFace repository IDs follow the pattern:
- `mistralai/Ministral-3-3B-Base-2512`, `mistralai/Ministral-3-3B-Instruct-2512`, `mistralai/Ministral-3-3B-Reasoning-2512`
- `mistralai/Ministral-3-8B-Base-2512`, `mistralai/Ministral-3-8B-Instruct-2512`, `mistralai/Ministral-3-8B-Reasoning-2512`
- `mistralai/Ministral-3-14B-Base-2512`, `mistralai/Ministral-3-14B-Instruct-2512`, `mistralai/Ministral-3-14B-Reasoning-2512`

## Training Methodology

A key component of Ministral 3 is the Cascade Distillation training strategy, an iterative pruning and distillation method which progressively transfers pretrained knowledge from a large parent model down to a family of compact children models. Pretraining starts from pruning the parent model, Mistral Small 3.1, into the largest child model (14B), which continues pretraining with logit distillation from the parent model as the teacher to obtain the short context child model, followed by another round of distillation with a longer context window to obtain the final Ministral 3 14B Base model.

## Training Data

Mistral does not publicly disclose its dataset composition, which is common practice. However, given the model's strong multilingual performance, it likely included diverse sources (Web text, books, code, etc. in many languages) in training.

## MMLU Benchmark Performance

On Multilingual MMLU, Ministral 3 14B Base 2512 achieved 74.2% and Ministral 3 8B Base 2512 achieved 70.6%. For external benchmarks, Ministral 3 was evaluated on MMLU, MMLU-Redux, ARC-Challenge, RACE High, TriviaQA, NaturalQS, and AGIEval.

## Additional Features

All models have vision capabilities. All models use a vocabulary size of 131K tokens. All models are released under the Apache 2.0 license.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4e6eeaf-d987-4f15-a8d2-6fed4345d7a3",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "433ca3d6-6f1c-4449-9159-8cf2b156952a",
  "sourceToolAssistantUUID": "f4e6eeaf-d987-4f15-a8d2-6fed4345d7a3",
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

_source line 54 · 2026-05-18T07:09:44.744Z_

Now let me get a few final details to complete the picture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "433ca3d6-6f1c-4449-9159-8cf2b156952a",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9ce7cF8zi9Hgy5GoDKN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06f77729-d708-4f0e-9499-1e223dcecd88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDvLGxMTiu64i81AFWsSpo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1902,
      "cache_creation_input_tokens": 2469,
      "cache_read_input_tokens": 35593,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2469,
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

_source line 55 · 2026-05-18T07:09:45.926Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HhNCBBiqo47LzXPRX9cdr4`</summary>

```json
{
  "query": "Gemma 4 base model HuggingFace 2026 parameters 12B release date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06f77729-d708-4f0e-9499-1e223dcecd88",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9ce7cF8zi9Hgy5GoDKN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52f08d55-8531-4bdc-8434-36b387941ab5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDvLGxMTiu64i81AFWsSpo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1902,
      "cache_creation_input_tokens": 2469,
      "cache_read_input_tokens": 35593,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2469,
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

_source line 56 · 2026-05-18T07:09:46.593Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B6jYQCh3LrWW2wng68aAbb`</summary>

```json
{
  "query": "Phi-4 reasoning 14B HuggingFace release date gated benchmark AIME MATH training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52f08d55-8531-4bdc-8434-36b387941ab5",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9ce7cF8zi9Hgy5GoDKN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f96a87d-653d-4621-be3f-10cfd4b8a5f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDvLGxMTiu64i81AFWsSpo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1902,
      "cache_creation_input_tokens": 2469,
      "cache_read_input_tokens": 35593,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2469
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1902,
          "output_tokens": 149,
          "cache_read_input_tokens": 35593,
          "cache_creation_input_tokens": 2469,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2469,
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

_source line 57 · 2026-05-18T07:09:53.054Z_

<details><summary>↩ Tool result · `toolu_01HhNCBBiqo47LzXPRX9cdr4`</summary>

```text
Web search results for query: "Gemma 4 base model HuggingFace 2026 parameters 12B release date"

Links: [{"title":"Gemma4 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/gemma4"},{"title":"google/gemma-4-31B · Hugging Face","url":"https://huggingface.co/google/gemma-4-31B"},{"title":"nvidia/Gemma-4-26B-A4B-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Gemma-4-26B-A4B-NVFP4"},{"title":"Gemma 4 model overview | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core"},{"title":"google/gemma-4-26B-A4B-it · Hugging Face","url":"https://huggingface.co/google/gemma-4-26B-A4B-it"},{"title":"google/gemma-4-31B-it · Hugging Face","url":"https://huggingface.co/google/gemma-4-31B-it"},{"title":"Welcome Gemma 4: Frontier multimodal intelligence on device","url":"https://huggingface.co/blog/gemma4"},{"title":"nvidia/Gemma-4-31B-IT-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Gemma-4-31B-IT-NVFP4"},{"title":"google/gemma-4-E4B · Hugging Face","url":"https://huggingface.co/google/gemma-4-E4B"},{"title":"Gemma 4: Our most capable open models to date","url":"https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/"}]

Based on the search results, here's what I found regarding Gemma 4:

## Gemma 4 Model Overview

Gemma 4 is a multimodal model with pretrained and instruction-tuned variants, available in E2B, E4B, 31B and 26B-A4B (MoE) parameter sizes. 

**Important Note:** The search results do not show a 12B base model variant. The available sizes are E2B, E4B, 26B A4B, and 31B.

## Release Date

The model was added to Hugging Face Transformers on 2026-04-01.

## Model Characteristics

Gemma 4 models are multimodal, handling text and image input (with audio supported on small models) and generating text output. Gemma 4 features a context window of up to 256K tokens and maintains multilingual support in over 140 languages.

If you were specifically looking for information about a 12B parameter model, it doesn't appear to be part of the Gemma 4 family based on the available documentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52f08d55-8531-4bdc-8434-36b387941ab5",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "c149174f-7c35-4964-9236-c1b5a6566968",
  "sourceToolAssistantUUID": "52f08d55-8531-4bdc-8434-36b387941ab5",
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

_source line 58 · 2026-05-18T07:09:55.734Z_

<details><summary>↩ Tool result · `toolu_01B6jYQCh3LrWW2wng68aAbb`</summary>

```text
Web search results for query: "Phi-4 reasoning 14B HuggingFace release date gated benchmark AIME MATH training"

Links: [{"title":"microsoft/Phi-4-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning"},{"title":"Phi-4 Local Setup: Microsoft's 14B Reasoning on 12GB GPUs | Local AI Master","url":"https://localaimaster.com/blog/phi-4-local-setup"},{"title":"microsoft/Phi-4-mini-flash-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-flash-reasoning"},{"title":"Microsoft Phi-4 Reasoning: Small Model, Big Math | Awesome Agents","url":"https://awesomeagents.ai/reviews/review-phi-4-reasoning/"},{"title":"microsoft/Phi-4-reasoning-plus · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-plus"},{"title":"Phi 4 Reasoning Benchmarks, Model Specs, and Comparisons - DEV Community","url":"https://dev.to/best_codes/phi-4-reasoning-benchmarks-model-specs-and-comparisons-4hk"},{"title":"unsloth/Phi-4-reasoning-plus · Hugging Face","url":"https://huggingface.co/unsloth/Phi-4-reasoning-plus"},{"title":"unsloth/Phi-4-reasoning-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Phi-4-reasoning-GGUF"},{"title":"microsoft/Phi-4-mini-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-reasoning"},{"title":"Microsoft Launches Two Powerful Phi-4 Reasoning Models","url":"https://www.analyticsvidhya.com/blog/2025/05/phi-4-reasoning-models/"}]

Based on the search results, here's comprehensive information about Phi-4 reasoning models:

## Release Timeline

The original Phi-4 (14B) was released in December 2024 under MIT license. Phi-4-reasoning and Phi-4-reasoning-plus were released simultaneously on April 30, 2025. Phi-4-mini-flash-reasoning was released on July 9, 2025.

## Model Specifications

The core text models are Phi-4-reasoning and Phi-4-reasoning-plus, both 14B parameters with a 32K token context window. Both ship under MIT license, run locally via Ollama on a consumer GPU, and cost nothing to download.

## Benchmark Performance

When Phi-4-reasoning was released in April 2025, it scored 75.3% on AIME 2024, beating DeepSeek-R1-Distill-70B (69.3%). The stronger sibling, Phi-4-reasoning-plus, pushed that number to 81.3%.

The models were evaluated on AIME 2025, 2024, 2023, and 2022 (math olympiad questions), GPQA-Diamond (complex, graduate-level science questions), and OmniMath (collection of over 4000 olympiad-level math problems with human annotation).

## Training Data

The training data is a mixture of Q&A, chat format data in math, science, and coding, with chat prompts sourced from filtered high-quality web data and optionally rewritten through a synthetic data generation pipeline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f96a87d-653d-4621-be3f-10cfd4b8a5f5",
  "isSidechain": true,
  "promptId": "04205c35-fa25-4f0b-9c44-5def633915cd",
  "agentId": "a72b4b1ce170203bc",
  "type": "user",
  "uuid": "92b127b7-2538-43d9-9c74-4e4f3887c91e",
  "sourceToolAssistantUUID": "0f96a87d-653d-4621-be3f-10cfd4b8a5f5",
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

_source line 59 · 2026-05-18T07:11:04.320Z_

Here is the compiled structured report of all findings.

---

## Search 1: DeepSeek V3 Base Model

DeepSeek-V3 is **not** in the 7B-14B range. It is a large MoE model. However, the DeepSeek ecosystem includes several models that do fall in the target range.

### DeepSeek-V3 (for reference, out of range)
- **Full name:** DeepSeek-V3
- **HuggingFace repo:** `deepseek-ai/DeepSeek-V3-Base`
- **Total parameters:** 671B (+14B MTP module = 685B total weights)
- **Active parameters:** 37B per token
- **Architecture:** MoE (256 experts)
- **Release date:** December 2024 (V3-0324 update March 2025; V3.1 and V3.2 followed)
- **Gated:** No (MIT license)
- **Base version exists:** Yes (`deepseek-ai/DeepSeek-V3-Base`)
- **Training data:** ~14.8T tokens
- **NOT in 7B-14B range**

### DeepSeek-V2-Lite (in range)
- **Full name:** DeepSeek-V2-Lite
- **HuggingFace repo:** `deepseek-ai/DeepSeek-V2-Lite`
- **Total parameters:** 15.7B
- **Active parameters:** 2.4B per token
- **Architecture:** MoE (2 shared experts + 64 routed experts, 6 activated per token)
- **Release date:** May 7, 2024
- **Gated:** No (MIT license)
- **Base version exists:** Yes (this IS the base version; chat version at `deepseek-ai/DeepSeek-V2-Lite-Chat`)
- **Training data:** 5.7T tokens (same pre-training corpus as DeepSeek-V2)
- **Benchmarks:** Outperforms 7B dense and 16B MoE models on many English/Chinese benchmarks (specific MMLU not retrieved)

### DeepSeek-Coder-V2-Lite-Base (in range)
- **Full name:** DeepSeek-Coder-V2-Lite-Base
- **HuggingFace repo:** `deepseek-ai/DeepSeek-Coder-V2-Lite-Base`
- **Total parameters:** 15.7B (sometimes cited as 16B)
- **Active parameters:** 2.4B per token
- **Architecture:** MoE (2 shared experts + 64 routed experts, 6 activated per token)
- **Release date:** June 2024
- **Gated:** No
- **Base version exists:** Yes (this IS the base; instruct variant at `deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct`)
- **Training data:** Not separately disclosed; code-focused extension of V2 data
- **Benchmarks:** Strong on code intelligence tasks; competes with closed-source models on coding benchmarks

### DeepSeek-R1-Distill-Qwen-14B (in range)
- **Full name:** DeepSeek-R1-Distill-Qwen-14B
- **HuggingFace repo:** `deepseek-ai/DeepSeek-R1-Distill-Qwen-14B`
- **Parameters:** 14B (dense)
- **Architecture:** Dense transformer (based on Qwen2.5-14B)
- **Release date:** January 20, 2025
- **Gated:** No (MIT license for DeepSeek distillation; underlying Qwen2.5 is Apache 2.0)
- **Base version exists:** No -- this is a distilled/fine-tuned model (SFT on 800K reasoning samples from DeepSeek-R1), not a base pretrained model
- **Training data:** Fine-tuned with 800K samples curated from DeepSeek-R1 outputs
- **Benchmarks:** AIME 2024: 69.7%, MATH-500: 93.9% (pass@1 with temperature=0.6, top-p=0.95, 64 samples)

### DeepSeek-R1-Distill-Qwen-7B (in range)
- **Full name:** DeepSeek-R1-Distill-Qwen-7B
- **HuggingFace repo:** `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B`
- **Parameters:** 7B (dense)
- **Architecture:** Dense transformer (based on Qwen2.5-7B)
- **Release date:** January 20, 2025
- **Gated:** No
- **Base version exists:** No -- distilled model, not base pretrained
- **Training data:** Fine-tuned with 800K samples from DeepSeek-R1

---

## Search 2: Phi-4 Base Model

### Phi-4 (14B base)
- **Full name:** Phi-4
- **HuggingFace repo:** `microsoft/phi-4`
- **Parameters:** 14.7B (dense)
- **Architecture:** Dense decoder-only transformer
- **Release date:** December 2024 (initially on Azure; open-sourced on HuggingFace January 2025)
- **Gated:** No (MIT license, fully open access)
- **Base version exists:** Yes -- `microsoft/phi-4` IS the base pretrained model
- **Training data:** 9.8T tokens; mix of synthetic data (generated by GPT-4o), high-quality web content, educational data, code, academic books, Q&A datasets
- **Context length:** 16K tokens
- **Benchmarks:** MMLU: 84.8%, MATH: 80.4%, HumanEval: 82.6%

### Phi-4-reasoning (14B, fine-tuned)
- **Full name:** Phi-4-reasoning
- **HuggingFace repo:** `microsoft/Phi-4-reasoning`
- **Parameters:** 14B (dense)
- **Release date:** April 30, 2025
- **Gated:** No (MIT license)
- **Base version exists:** Not a base model; fine-tuned from Phi-4 for reasoning
- **Benchmarks:** AIME 2024: 75.3%

### Phi-4-reasoning-plus (14B, fine-tuned)
- **Full name:** Phi-4-reasoning-plus
- **HuggingFace repo:** `microsoft/Phi-4-reasoning-plus`
- **Parameters:** 14B (dense)
- **Release date:** April 30, 2025
- **Gated:** No (MIT license)
- **Base version exists:** Not a base model
- **Benchmarks:** AIME 2024: 81.3%

### Phi-4-mini-instruct (3.8B, NOT in 7B-14B range)
- **Full name:** Phi-4-mini-instruct
- **HuggingFace repo:** `microsoft/Phi-4-mini-instruct`
- **Parameters:** 3.8B (dense)
- **Release date:** March 19, 2026
- **Training data:** 5T tokens
- **Context length:** 128K tokens
- **Benchmarks:** MMLU: ~73% (matches Llama 3.1 8B)
- **NOT in 7B-14B range**

---

## Search 3: DeepSeek R2

**DeepSeek R2 has NOT been released as of May 2026.** Key findings:

- DeepSeek R2 was widely anticipated as the second-generation reasoning model.
- It was reportedly slated for release in H1 2025 but was delayed.
- The delay was caused by failed training runs on Huawei Ascend AI chips (stability problems, slow interconnect, immature software tooling).
- As of April 2026, DeepSeek instead released DeepSeek-V4-Pro (1.6T parameters) and DeepSeek-V4-Flash (284B parameters) with 1M token context windows.
- R2 is NOT listed in the official DeepSeek API model list as of May 2026.
- No HuggingFace repository exists for DeepSeek R2.

---

## Additional Models Found in the 7B-14B Range (2025-2026)

### Qwen3-14B-Base
- **HuggingFace repo:** `Qwen/Qwen3-14B-Base`
- **Parameters:** 14B (dense)
- **Architecture:** Dense transformer
- **Release date:** April 29, 2025
- **Gated:** No (Apache 2.0)
- **Base version exists:** Yes (this IS the base)
- **Training data:** ~36T tokens covering 119 languages (3-stage pretraining: S1 >30T tokens at 4K context, S2 +5T tokens STEM-heavy, S3 long-context extension to 32K)
- **Benchmarks:** MMLU: 81.05 (base model). Performance matches Qwen2.5-32B-Base.

### Qwen3-8B-Base
- **HuggingFace repo:** `Qwen/Qwen3-8B-Base`
- **Parameters:** 8B (dense)
- **Architecture:** Dense transformer
- **Release date:** April 29, 2025
- **Gated:** No (Apache 2.0)
- **Base version exists:** Yes
- **Training data:** ~36T tokens (same corpus as all Qwen3 models)
- **Benchmarks:** Performance matches Qwen2.5-14B-Base

### Gemma 3 12B (pretrained base)
- **Full name:** Gemma 3 12B PT
- **HuggingFace repo:** `google/gemma-3-12b-pt`
- **Parameters:** 12B (dense)
- **Architecture:** Dense transformer, multimodal (text+image input, text output)
- **Release date:** March 12, 2025
- **Gated:** Yes (requires agreeing to Google's usage license on HuggingFace)
- **Base version exists:** Yes (`google/gemma-3-12b-pt` is the pretrained base)
- **Training data:** 12T tokens
- **Context length:** 128K tokens
- **Benchmarks:** Specific MMLU for 12B not retrieved; 27B version: MMLU-Pro 67.5

### Ministral-3-14B-Base-2512
- **Full name:** Ministral 3 14B Base
- **HuggingFace repo:** `mistralai/Ministral-3-14B-Base-2512`
- **Parameters:** 14B (dense)
- **Architecture:** Dense transformer with vision capabilities
- **Release date:** December 1, 2025
- **Gated:** No (Apache 2.0)
- **Base version exists:** Yes (this IS the base)
- **Training data:** Not publicly disclosed. Trained via cascade distillation from Mistral Small 3.1 (24B parent)
- **Vocab size:** 131K tokens
- **Benchmarks:** Multilingual MMLU: 74.2%. Reasoning variant achieves 85% on AIME 2025.

### Ministral-3-8B-Base-2512
- **Full name:** Ministral 3 8B Base
- **HuggingFace repo:** `mistralai/Ministral-3-8B-Base-2512`
- **Parameters:** 8B (dense)
- **Architecture:** Dense transformer with vision capabilities
- **Release date:** December 1, 2025
- **Gated:** No (Apache 2.0)
- **Base version exists:** Yes
- **Training data:** Not disclosed. Cascade distillation from Ministral 3 14B.
- **Benchmarks:** Multilingual MMLU: 70.6%. Outperforms Gemma 3 12B on most evaluations except TriviaQA.

### Llama 4 Scout (out of strict 7B-14B range but noteworthy for active params)
- **Full name:** Llama 4 Scout 17B-16E
- **HuggingFace repo:** `meta-llama/Llama-4-Scout-17B-16E`
- **Total parameters:** ~109B
- **Active parameters:** 17B per token
- **Architecture:** MoE (16 experts)
- **Release date:** April 2025
- **Gated:** Yes (Meta Community License, 700M MAU clause)
- **Base version exists:** Yes (base and instruct variants both available)
- **Training data:** ~40T tokens (multimodal)
- **Context length:** 256K (pretrained), 10M (instruct)
- **Note:** While total params are 109B, active params (17B) are close to the 14B range. This is an MoE model.

---

## Summary Table: Models with Base Versions in the 7B-14B Dense Parameter Range

| Model | HF Repo ID | Params | Architecture | Release | License | Gated | Training Data | Base Exists | MMLU |
|---|---|---|---|---|---|---|---|---|---|
| **Phi-4** | `microsoft/phi-4` | 14.7B dense | Dense | Dec 2024 / Jan 2025 | MIT | No | 9.8T tokens | Yes | 84.8% |
| **Qwen3-14B** | `Qwen/Qwen3-14B-Base` | 14B dense | Dense | Apr 29, 2025 | Apache 2.0 | No | ~36T tokens | Yes | 81.05% |
| **Qwen3-8B** | `Qwen/Qwen3-8B-Base` | 8B dense | Dense | Apr 29, 2025 | Apache 2.0 | No | ~36T tokens | Yes | -- |
| **Gemma 3 12B** | `google/gemma-3-12b-pt` | 12B dense | Dense | Mar 12, 2025 | Gemma license | Yes | 12T tokens | Yes | -- |
| **Ministral 3 14B** | `mistralai/Ministral-3-14B-Base-2512` | 14B dense | Dense | Dec 1, 2025 | Apache 2.0 | No | Undisclosed | Yes | 74.2% (multilingual) |
| **Ministral 3 8B** | `mistralai/Ministral-3-8B-Base-2512` | 8B dense | Dense | Dec 1, 2025 | Apache 2.0 | No | Undisclosed | Yes | 70.6% (multilingual) |
| **DeepSeek-V2-Lite** | `deepseek-ai/DeepSeek-V2-Lite` | 15.7B total / **2.4B active** | **MoE** | May 7, 2024 | MIT | No | 5.7T tokens | Yes | -- |
| **DeepSeek-Coder-V2-Lite** | `deepseek-ai/DeepSeek-Coder-V2-Lite-Base` | 15.7B total / **2.4B active** | **MoE** | Jun 2024 | MIT | No | Undisclosed | Yes | -- |

## MoE Models Near the Range (for reference)

| Model | Total Params | Active Params | Experts | Notes |
|---|---|---|---|---|
| DeepSeek-V2-Lite | 15.7B | 2.4B | 64 routed + 2 shared, 6 active | Smallest DeepSeek MoE |
| DeepSeek-Coder-V2-Lite | 15.7B | 2.4B | Same as above | Code-focused variant |
| Llama 4 Scout | ~109B | 17B | 16 experts | Active params close to range |
| Gemma 4 26B-A4B | 25.2B | 3.8B | MoE | Out of range but notable |
| DeepSeek-V3 | 671B | 37B | 256 experts | Far out of range |

## Key Takeaway for Your Paper

For an academic paper needing open-source base (non-instruct) LLMs in the 7B-14B dense parameter range released in 2025-2026, the strongest candidates are:

1. **Phi-4** (`microsoft/phi-4`) -- 14.7B, MIT, not gated, highest MMLU at 84.8%
2. **Qwen3-14B-Base** (`Qwen/Qwen3-14B-Base`) -- 14B, Apache 2.0, not gated, MMLU 81.05%, largest training corpus (36T tokens)
3. **Qwen3-8B-Base** (`Qwen/Qwen3-8B-Base`) -- 8B, Apache 2.0, not gated
4. **Gemma 3 12B PT** (`google/gemma-3-12b-pt`) -- 12B, gated (license agreement required)
5. **Ministral 3 14B Base** (`mistralai/Ministral-3-14B-Base-2512`) -- 14B, Apache 2.0, Dec 2025
6. **Ministral 3 8B Base** (`mistralai/Ministral-3-8B-Base-2512`) -- 8B, Apache 2.0, Dec 2025

DeepSeek R2 does not exist yet. DeepSeek V3 is far too large (671B). The DeepSeek-R1-Distill models (7B/14B) exist but are fine-tuned reasoning models, not base pretrained models.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92b127b7-2538-43d9-9c74-4e4f3887c91e",
  "isSidechain": true,
  "agentId": "a72b4b1ce170203bc",
  "requestId": "req_011Cb9cf7nSZAbg6aPNtSMvW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c7bda20-8223-4485-9f96-15af8e2fcc0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016cjYAzfvPVftZYiKW4HiTR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3858,
      "cache_read_input_tokens": 38062,
      "output_tokens": 4492,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3858
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4492,
          "cache_read_input_tokens": 38062,
          "cache_creation_input_tokens": 3858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3858,
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
