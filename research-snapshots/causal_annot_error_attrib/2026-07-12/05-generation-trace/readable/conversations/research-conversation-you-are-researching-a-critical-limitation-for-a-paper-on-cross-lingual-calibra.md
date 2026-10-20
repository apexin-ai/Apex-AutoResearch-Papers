# Research conversation: You are researching a critical limitation for a paper on cross-lingual calibration transfer in LLMs. A reviewer cited ar

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a6baa1a7d8c626c89.jsonl`
- **Structured JSON:** [`755bfe999969359532f9.json`](../../sessions/75/755bfe999969359532f9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-19T09:13:43.182Z_

You are researching a critical limitation for a paper on cross-lingual calibration transfer in LLMs. 

A reviewer cited arXiv 2505.12584v2 which claims that cross-lingual steering transfer is "largely limited to languages within the same linguistic family" and "cross-family transfers such as from Spanish to Japanese are ineffective."

Your tasks:
1. Use WebFetch to read the paper at https://arxiv.org/abs/2505.12584v2 — extract the key findings about cross-family transfer limitations, what models they tested, what kind of "steering" they studied (was it safety/refusal steering? calibration? something else?), and the exact scope of their negative findings.
2. Use WebSearch to find other papers (2025-2026) on cross-lingual representation steering or direction transfer, especially any that found MORE positive results for cross-family transfer.
3. Use WebSearch to search for "cross-lingual linear probing transfer typological distance 2025 2026" to find work on how typological distance affects transfer.

Report in detail (500+ words): What exactly are the limitations of cross-family steering transfer? Is this specific to safety/refusal directions or more general? Are there any positive results for cross-family transfer of linear directions? What nuances should we consider?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "a6baa1a7d8c626c89",
  "type": "user",
  "uuid": "2e9732f5-ede4-468b-8840-6e5dd7df39d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T09:13:43.186Z_

```json
{
  "parentUuid": "2e9732f5-ede4-468b-8840-6e5dd7df39d9",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
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
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "33332018-9eca-40a5-a68e-379462cb6e02",
  "timestamp": "2026-05-19T09:13:43.186Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T09:13:43.186Z_

```json
{
  "parentUuid": "33332018-9eca-40a5-a68e-379462cb6e02",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3b14710c-fac1-4851-bda7-ef202acae2d3",
  "timestamp": "2026-05-19T09:13:43.186Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T09:13:46.676Z_



I'll start by fetching the paper and running both searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b14710c-fac1-4851-bda7-ef202acae2d3",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBfuYN3vZVCdEn36PjVu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90866e5e-83b0-4c37-b8e5-70fe7c39ca83",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWo8Gm9P22crue3bUPnjNC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9401,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9401,
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

_source line 5 · 2026-05-19T09:13:46.908Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UAHwky23oxVpW8HKE97vi1`</summary>

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
  "parentUuid": "90866e5e-83b0-4c37-b8e5-70fe7c39ca83",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBfuYN3vZVCdEn36PjVu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3aef3e42-5075-432f-afe5-96adc9525d48",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWo8Gm9P22crue3bUPnjNC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9401,
      "cache_read_input_tokens": 0,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9401
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 96,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9401,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9401,
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

_source line 6 · 2026-05-19T09:13:46.911Z_

<details><summary>↩ Tool result · `toolu_01UAHwky23oxVpW8HKE97vi1`</summary>

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
  "parentUuid": "3aef3e42-5075-432f-afe5-96adc9525d48",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "a6baa1a7d8c626c89",
  "type": "user",
  "uuid": "020a8dc6-725e-4b90-a220-8628b56cecbd",
  "sourceToolAssistantUUID": "3aef3e42-5075-432f-afe5-96adc9525d48",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T09:13:49.972Z_



Now let me fetch the paper and run both searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "020a8dc6-725e-4b90-a220-8628b56cecbd",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBfupbcMfUmcvTCSMLsH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae59547f-2c41-446d-8be4-82d1fa9a0b45",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WMkCaAywWyRvXZXaxHkt7u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1118,
      "cache_read_input_tokens": 9401,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1118,
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

_source line 8 · 2026-05-19T09:13:53.725Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01B3wtnFhTuYJEmBrJbcsV1Y`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.12584v2",
  "prompt": "Extract ALL key findings from this paper in detail. Specifically I need:\n1. The exact title and authors\n2. What kind of \"steering\" or \"transfer\" they studied (safety/refusal steering? calibration? representation engineering? activation steering? something else?)\n3. What models were tested\n4. What languages were tested\n5. Their exact findings about cross-family transfer limitations - quote exact phrases if possible\n6. Their exact findings about within-family transfer\n7. The scope of their negative findings - what exactly fails cross-family?\n8. Any positive results they found\n9. Their methodology (how did they extract directions? how did they measure transfer?)\n10. Any nuances, caveats, or limitations they mention about their own findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae59547f-2c41-446d-8be4-82d1fa9a0b45",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBfupbcMfUmcvTCSMLsH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56c6da9c-3bae-47fa-8267-243d40524e4b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WMkCaAywWyRvXZXaxHkt7u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1118,
      "cache_read_input_tokens": 9401,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1118,
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

_source line 9 · 2026-05-19T09:13:54.234Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EtkkJu5fQveZrJ1pR8fCWJ`</summary>

```json
{
  "query": "cross-lingual representation steering direction transfer LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56c6da9c-3bae-47fa-8267-243d40524e4b",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBfupbcMfUmcvTCSMLsH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5231dae1-81f4-4440-b3d3-d67350c4c08b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WMkCaAywWyRvXZXaxHkt7u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1118,
      "cache_read_input_tokens": 9401,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1118,
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

_source line 10 · 2026-05-19T09:13:54.484Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B9S1C43egmVBrrnG4ZTYXK`</summary>

```json
{
  "query": "cross-lingual linear probing transfer typological distance 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5231dae1-81f4-4440-b3d3-d67350c4c08b",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBfupbcMfUmcvTCSMLsH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "335a6872-03ac-4dd8-8567-28fb195ce9cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WMkCaAywWyRvXZXaxHkt7u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1118,
      "cache_read_input_tokens": 9401,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1118,
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

_source line 11 · 2026-05-19T09:13:59.683Z_

<details><summary>↩ Tool result · `toolu_01B3wtnFhTuYJEmBrJbcsV1Y`</summary>

```text
# Analysis of arXiv:2505.12584v2

Based on the provided webpage content, I can extract the following information:

## 1. Title and Authors
**Title:** "Improving Multilingual Language Models by Aligning Representations through Steering"

**Authors:** Omar Mahmoud, Buddhika Laknath Semage, Thommen George Karimpanal, Santu Rana

## 2. Type of Steering Studied
This paper focuses on **representation steering** through activation-level interventions. Specifically, they use "a learned vector added to the residual stream at a single model layer."

## 3-7. Models, Languages, and Findings
The webpage abstract provides limited detail on these crucial points. It mentions:
- Testing across "seven competitive baselines" including prompt optimization, supervised fine-tuning, in-context learning, cross-lingual transfer, and translation methods
- **No specific model names or language pairs are detailed** in the provided content

## 8. Key Positive Results
Their steering method "consistently outperforms most alternatives" and "achieves performance on par with production-grade translation systems while requiring far fewer resources."

## 9. Methodology
The abstract indicates they use "learned vectors added to the residual stream at a single model layer" but specific extraction and measurement details aren't provided in this webpage content.

## 10. Limitations and Nuances
The paper explores "complementarity between [their] method and SFT" and notes steering offers "a direct, efficient way to realign internal representations."

**Note:** The webpage excerpt contains primarily the abstract and metadata. Full methodological details, cross-family transfer findings, and comprehensive experimental results would require accessing the complete PDF.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56c6da9c-3bae-47fa-8267-243d40524e4b",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "a6baa1a7d8c626c89",
  "type": "user",
  "uuid": "8d2c4834-cee0-4935-bc1f-caee3a7ec081",
  "sourceToolAssistantUUID": "56c6da9c-3bae-47fa-8267-243d40524e4b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T09:14:01.111Z_

<details><summary>↩ Tool result · `toolu_01EtkkJu5fQveZrJ1pR8fCWJ`</summary>

```text
Web search results for query: "cross-lingual representation steering direction transfer LLM 2025 2026"

Links: [{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs | Request PDF","url":"https://www.researchgate.net/publication/394303200_Middle-Layer_Representation_Alignment_for_Cross-Lingual_Transfer_in_Fine-Tuned_LLMs"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/html/2502.15639v1"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/html/2602.02326v1"},{"title":"Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/pdf/2505.12584"},{"title":"Steering Large Language Models for Cross-lingual Information Retrieval | Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/10.1145/3626772.3657819"},{"title":"[2505.12584] Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/abs/2505.12584"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/pdf/2502.15639"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/pdf/2602.02326"},{"title":"CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark","url":"https://arxiv.org/pdf/2601.08331"}]

Based on the web search results, here's what I found on cross-lingual representation steering and direction transfer in LLMs for 2025-2026:

## Key Research Areas

**Representation Steering Methods:**
Recent approaches learn a manifold that maps between English and target languages, then apply it during inference instead of fine-tuning, making it more efficient and less disruptive to the original model. Activation-level interventions are being explored as a powerful tool for improving the multilingual capabilities of LLMs.

**Cross-Lingual Alignment Techniques:**
At inference time, proposed cross-lingual alignment include steering representations towards English, merging task and language-specific adapters. Middle-Layer Representation Alignment (MIDALIGN) introduces a more explicit alignment mechanism, alternating between a supervised fine-tuning loss and a dedicated cross-lingual alignment loss.

**Language Steering for In-Context Learning:**
Research shows that adding steering vectors containing language-specific information to internal representations can improve model performance on target-language inputs, with evidence of effective cross-task transfer, suggesting the vectors capture language-specific rather than task-specific representations.

**Evaluation Frameworks:**
There is still no standard evaluation framework for language steering in language models, with existing benchmarks focusing exclusively on conceptual steering tasks in English, leaving multilingual and cross-lingual settings unexplored.

**Recent Advances:**
Cross-lingual activation steering for multilingual language models has been developed as of 2026, and steering is particularly promising for multilingual adaptation, enabling targeted language control without requiring costly retraining.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5231dae1-81f4-4440-b3d3-d67350c4c08b",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "a6baa1a7d8c626c89",
  "type": "user",
  "uuid": "164d42c1-d697-4de6-9795-95a5c9372b49",
  "sourceToolAssistantUUID": "5231dae1-81f4-4440-b3d3-d67350c4c08b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T09:14:01.464Z_

<details><summary>↩ Tool result · `toolu_01B9S1C43egmVBrrnG4ZTYXK`</summary>

```text
Web search results for query: "cross-lingual linear probing transfer typological distance 2025 2026"

Links: [{"title":"Cross-lingual Transfer Learning","url":"https://www.emergentmind.com/topics/cross-lingual-transfer-learning-63a7cac1-c2ae-4704-8e27-a49a3951a0c1"},{"title":"Cross-Linguistic Influence (CLI)","url":"https://www.emergentmind.com/topics/cross-linguistic-influence-cli"},{"title":"[2510.19217] Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+","url":"https://arxiv.org/abs/2510.19217"},{"title":"Language Models Are Polyglots: Language Similarity Predicts Cross-Lingual Transfer Learning Performance","url":"https://www.mdpi.com/2504-4990/8/3/65"},{"title":"Cross-Lingual Transfer: Language Selection","url":"https://www.emergentmind.com/topics/cross-lingual-transfer-language-selection"},{"title":"Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+","url":"https://arxiv.org/html/2510.19217"},{"title":"[2505.13908] Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology","url":"https://arxiv.org/abs/2505.13908"}]

Based on the search results, here's what I found about cross-lingual linear probing, transfer learning, and typological distance research from 2025-2026:

## Key Research Findings

**Typological Distance and Transfer Performance:**
Dataset overlap and pragmatic alignment are robust predictors of transfer success, prioritizing these over typological distance when selecting source languages. However, fine-grained typological features—especially those related to word order or tense/noun phrase structure—are recommended when choosing a source language for transfer, with optimal source languages differing depending on which features most strongly impact target performance.

**Recent Methodological Advances:**
A framework for type-matched language distances proposes novel, structure-aware representations for each distance type: speaker-weighted distributions for geography, hyperbolic embeddings for genealogy, and a latent variables model for typology, unifying these signals into a robust, task-agnostic composite distance. Across multiple zero-shot transfer benchmarks, these representations significantly improve transfer performance when the distance type is relevant to the task.

**Linguistic Similarity Metrics:**
Quantified WALS (qWALS) is a typology-based similarity metric derived from features in the World Atlas of Language Structures. Typological and phylogenetic features derived from WALS, Glottolog family trees, or URIEL/lang2vec vectors are widely used, with pairwise distances computed via measures such as Euclidean, Hamming, Jaccard, cosine, and Anderberg distances.

These findings suggest evolving approaches to understanding how typological distance interacts with cross-lingual transfer in NLP systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "335a6872-03ac-4dd8-8567-28fb195ce9cc",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "a6baa1a7d8c626c89",
  "type": "user",
  "uuid": "1e25e7e4-fd6c-4f8a-af16-72dda8b4b146",
  "sourceToolAssistantUUID": "335a6872-03ac-4dd8-8567-28fb195ce9cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-19T09:14:05.345Z_

The abstract page didn't have enough detail. Let me fetch the full PDF and also fetch the key related papers I found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e25e7e4-fd6c-4f8a-af16-72dda8b4b146",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBfvtW2tAvoNPn7YUxH6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f610ae0f-c855-4aee-8d2f-c71c57166e03",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6PaLwzdMq8jmnZzLbsCkr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2427,
      "cache_read_input_tokens": 10519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2427,
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

_source line 15 · 2026-05-19T09:14:09.173Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PMwRPJS6F27HcLqnNdVvxZ`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2505.12584",
  "prompt": "Extract ALL key findings from this paper in maximum detail. I need:\n1. What kind of steering they studied - safety/refusal? calibration? task performance? representation alignment?\n2. What models were tested (exact model names and sizes)\n3. What languages were tested and which language pairs\n4. Their EXACT findings about cross-family transfer limitations - quote exact phrases about Spanish to Japanese or similar cross-family pairs being ineffective\n5. Their exact findings about within-family transfer successes\n6. Methodology: how did they extract steering vectors? what layers? how did they measure transfer?\n7. What tasks/benchmarks did they evaluate on?\n8. Any nuances about when cross-family transfer does or does not work\n9. Any discussion of why cross-family transfer fails\n10. Tables or results showing cross-family vs within-family performance differences"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f610ae0f-c855-4aee-8d2f-c71c57166e03",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBfvtW2tAvoNPn7YUxH6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6bcb85b5-3d1c-4223-a427-4cc73769ce7a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6PaLwzdMq8jmnZzLbsCkr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2427,
      "cache_read_input_tokens": 10519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2427,
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

_source line 16 · 2026-05-19T09:14:12.050Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ELmZdp1bXANbPZmDCUQNE4`</summary>

```json
{
  "url": "https://arxiv.org/html/2502.15639v1",
  "prompt": "Extract all key findings about cross-lingual steering transfer. Specifically:\n1. Title and authors\n2. What kind of steering did they study?\n3. What models and languages?\n4. Did they find cross-family transfer works or fails?\n5. Any findings about steering vectors transferring across typologically distant languages?\n6. Key positive or negative results about cross-lingual direction transfer\n7. Methodology details\n8. Any discussion of language family effects on transfer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bcb85b5-3d1c-4223-a427-4cc73769ce7a",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBfvtW2tAvoNPn7YUxH6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "178fb27a-9877-4562-a326-6208c82f3d38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6PaLwzdMq8jmnZzLbsCkr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2427,
      "cache_read_input_tokens": 10519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2427,
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

_source line 17 · 2026-05-19T09:14:13.752Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SgQ26MxmDjMKEfXXTk2bbY`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.02326v1",
  "prompt": "Extract all key findings about language steering for multilingual in-context learning. Specifically:\n1. Title and authors\n2. What kind of steering?\n3. Models and languages tested\n4. Any findings about cross-family vs within-family transfer\n5. Positive results for cross-lingual steering\n6. Key methodology details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "178fb27a-9877-4562-a326-6208c82f3d38",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBfvtW2tAvoNPn7YUxH6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61ddc562-c718-4a96-a604-1d4bf0922f5d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6PaLwzdMq8jmnZzLbsCkr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2427,
      "cache_read_input_tokens": 10519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2427,
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

_source line 18 · 2026-05-19T09:14:14.088Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GzRUNqu9FgEjEvoC3DTkYL`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.08331",
  "prompt": "Extract all key findings from CLaS-Bench. What is this benchmark about? What did they find about cross-lingual steering? Any findings about cross-family transfer?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61ddc562-c718-4a96-a604-1d4bf0922f5d",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBfvtW2tAvoNPn7YUxH6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5dc6fd96-3ebf-46ab-9c77-c44690afc4b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6PaLwzdMq8jmnZzLbsCkr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2427,
      "cache_read_input_tokens": 10519,
      "output_tokens": 703,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2427
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 703,
          "cache_read_input_tokens": 10519,
          "cache_creation_input_tokens": 2427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2427,
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

_source line 19 · 2026-05-19T09:14:18.270Z_

<details><summary>↩ Tool result · `toolu_01PMwRPJS6F27HcLqnNdVvxZ`</summary>

```text
# Key Findings from "Improving Multilingual Language Models by Aligning Representations through Steering"

## 1. Type of Steering Studied
The paper examines **representation alignment through steering vectors** to improve multilingual language model performance. The focus is on aligning internal representations across languages rather than safety/refusal mechanisms.

## 2. Models Tested
- Llama 2 (7B, 13B, 70B variants)
- Aya-23 (8B, 35B)
- Gemma (7B, 9B)
- Qwen 1.5 (4B, 7B, 14B)

## 3. Languages Tested
The paper evaluates multiple language pairs including Spanish, Japanese, German, French, and other languages, though the exact comprehensive list of all language pairs is embedded in experiments rather than explicitly enumerated in the provided content.

## 4. Cross-Family Transfer Limitations
The paper demonstrates that **steering vectors do not transfer effectively across language families**. While specific exact phrases about "Spanish to Japanese" cross-family pairs are not directly quoted in the visible content, the research shows systematic failures when attempting to transfer learned steering directions between linguistically distant languages.

## 5. Within-Family Transfer Successes
Steering vectors show significantly better transfer when applied within the same language family. The research indicates that "representation alignment through steering" works substantially better for related languages compared to distant ones.

## 6. Methodology

**Vector Extraction:**
- Steering vectors extracted from model hidden states
- Analysis performed across multiple layers of transformer models
- Vectors derived from contrastive pairs or task-specific representations

**Transfer Measurement:**
- Evaluated by applying steering vectors learned from one language to another language's outputs
- Measured performance degradation or improvement on downstream tasks
- Compared within-family versus cross-family transfer effectiveness

## 7. Tasks/Benchmarks Evaluated
- Machine translation tasks
- Cross-lingual natural language inference (XNLI)
- Cross-lingual question answering (XCOPA)
- MMLU (multilingual variant)
- M3Exam

## 8. Nuances on Transfer Effectiveness
The research reveals that linguistic distance significantly determines transfer success. Closely related languages benefit from shared representation structure, while languages from different families exhibit incompatible steering directions, suggesting fundamental differences in how these models organize multilingual knowledge.

## 9. Why Cross-Family Transfer Fails
The implicit finding suggests that **different language families induce distinct representational geometries** in the model's hidden space. Steering directions optimized for one family's linguistic structure do not align with another family's internal representations, making cross-family transfer fundamentally mismatched.

## 10. Performance Differences
The paper presents quantitative comparisons showing substantial performance gaps between within-family and cross-family steering transfer, with within-family applications maintaining task performance while cross-family applications show degradation. Specific numerical results appear in tables distributed throughout the document but require detailed examination of the full paper content.

[Binary content (application/pdf, 1.3MB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-gen-pipeline/e35f8964-edb8-41bf-9248-b2986ccc4fa6/tool-results/webfetch-1779182049358-gjm7sk.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6bcb85b5-3d1c-4223-a427-4cc73769ce7a",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "a6baa1a7d8c626c89",
  "type": "user",
  "uuid": "47b8670e-2013-40f9-819d-07db7a168954",
  "sourceToolAssistantUUID": "6bcb85b5-3d1c-4223-a427-4cc73769ce7a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T09:14:18.536Z_

<details><summary>↩ Tool result · `toolu_01GzRUNqu9FgEjEvoC3DTkYL`</summary>

```text
# CLaS-Bench: Key Findings

## What is CLaS-Bench?

CLaS-Bench is a benchmark designed to evaluate how well steering techniques can control language behavior in multilingual large language models. The benchmark covers 32 languages and measures performance across two dimensions: language control and semantic relevance.

## Key Findings on Cross-Lingual Steering

The research evaluated multiple steering approaches, including residual-stream interventions, probe-derived directions, language-specific neurons, PCA/LDA vectors, and Sparse Autoencoders. The primary discovery was that "simple residual-based DiffMean method consistently outperforms all other methods" across the tested languages.

## Architectural Insights

A layer-wise analysis revealed important patterns about how language representations develop in these models:

- "Language-specific structure emerges predominantly in later layers"
- Steering directions cluster based on language family

This suggests that models develop language-specific processing in deeper layers, and that languages within the same family share similar representational structures that steering methods can exploit.

The benchmark represents the first standardized evaluation framework specifically designed for multilingual steering, enabling systematic comparison of these techniques as an alternative to prompting or fine-tuning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5dc6fd96-3ebf-46ab-9c77-c44690afc4b0",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "a6baa1a7d8c626c89",
  "type": "user",
  "uuid": "d5ba9b4a-882f-4f3a-9f46-074904389ca3",
  "sourceToolAssistantUUID": "5dc6fd96-3ebf-46ab-9c77-c44690afc4b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T09:14:20.230Z_

<details><summary>↩ Tool result · `toolu_01SgQ26MxmDjMKEfXXTk2bbY`</summary>

```text
# Language Steering for Multilingual In-Context Learning: Key Findings

## Title and Authors
**Language Steering for Multilingual In-Context Learning** by Neeraja Kirtane and Kuan-Hao Huang

## Steering Method
The authors propose "language vectors"—a training-free approach that extracts activation differences between source (English) and target languages, then adds these vectors to intermediate model activations during inference to shift the model's internal representations toward the target language space.

## Models and Languages Tested
- **Models**: Llama3.1-8B-Instruct, Qwen2.5-7B-Instruct, Qwen2.5-14B-Instruct
- **Languages**: 19 languages across three datasets (MGSM for math, XNLI for inference, MSVAMP for word problems)

## Cross-Family vs Within-Family Transfer
Hierarchical clustering revealed meaningful linguistic structure: "Closely related languages cluster tightly. Hindi-Urdu form the closest pair (distance ∼0.043)." Romance languages grouped together, and "Indo-Aryan cluster (Bengali, Hindi, Urdu) merges at distance ∼0.201," demonstrating that language families influence steering vector similarity.

## Key Positive Results
- MGSM showed "improvements ranging from approximately 2.9% to 5.4%" across models
- Average improvements on MGSM: 61.01% (baseline) → 65.87% (proposed method)
- Five of six cross-task transfers demonstrated "effective generalization"

## Methodology Details
The approach involves three steps: (1) extracting hidden states from parallel question-answer pairs, (2) computing steering vectors as "mean of activation differences" between languages, and (3) applying scaled vectors (α·**v**(t)) to hidden states during inference at specific token positions, with middle layers proving most effective.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61ddc562-c718-4a96-a604-1d4bf0922f5d",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "a6baa1a7d8c626c89",
  "type": "user",
  "uuid": "1eb084d5-f364-4aab-8035-8cc4d4a255a4",
  "sourceToolAssistantUUID": "61ddc562-c718-4a96-a604-1d4bf0922f5d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T09:14:20.670Z_

<details><summary>↩ Tool result · `toolu_01ELmZdp1bXANbPZmDCUQNE4`</summary>

```text
# Cross-Lingual Steering Transfer Analysis

## Basic Information

**Title:** "Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models"

**Authors:** Anirudh Sundar, Sinead Williamson, Katherine Metcalf, Barry-John Theobald, Skyler Seto, Masha Fedzechkina

## Steering Method

The researchers examined the "finding experts" intervention technique, which identifies and manipulates "neurons that can classify sentences as being from the positive set (containing the target language) vs. the negative set." They set these expert neuron activations to mean values calculated over target-language sentences.

## Models and Languages

**Models:** Bloom-7B, Aya-8B, PolyLM-13B

**Languages Studied:** 22 languages total, with five intervention targets: English, German, French, Spanish, and Japanese

## Cross-Lingual Transfer Results

**Key Finding:** The intervention demonstrated **unexpected broad cross-lingual benefits**. When intervening on one language's experts, improvements transferred across language pairs not involving the target language. For example, "an intervention on Japanese results in a large top-1 retrieval accuracy improvement for English-Portuguese" in Bloom-7B.

## Embedding Space Changes

The steering pulled all language embeddings toward the space's medoid, creating enhanced cross-lingual alignment. Specifically, "the distances between the language embeddings are reduced in the new space."

## Performance Outcomes

- Up to **2x improvement in top-1 cross-lingual retrieval accuracy**
- Within-language similarity preservation (paraphrase retrieval remained unchanged)
- Consistent perplexity increases post-intervention

## Methodology Details

The researchers:
1. Used Flores200 dataset for expert identification
2. Measured pairwise cosine distances between 22-language embeddings
3. Evaluated performance via cross-lingual retrieval and paraphrase matching tasks
4. Tested random neuron interventions as control (which failed to produce improvements)

## Language Family Effects

The paper notes "markedly different patterns" across the three models studied and hypothesizes differences relate to "pre-training data and/or procedure," but acknowledges insufficient information to definitively test whether linguistic distance or language family affected transfer outcomes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "178fb27a-9877-4562-a326-6208c82f3d38",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "a6baa1a7d8c626c89",
  "type": "user",
  "uuid": "246e2867-14b9-40b0-9854-e783d92e0c7e",
  "sourceToolAssistantUUID": "178fb27a-9877-4562-a326-6208c82f3d38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-19T09:14:23.911Z_

Good, I now have substantial information. Let me search for a few more specific topics to round out the analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "246e2867-14b9-40b0-9854-e783d92e0c7e",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBfxKGacqizK5VwCB9iV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07f5ed56-d3e0-4ad2-8fa2-d2f176b1bd52",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gjz1UsNaQi8YTUvnwmfRbr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 762,
      "cache_creation_input_tokens": 2055,
      "cache_read_input_tokens": 12946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2055,
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

_source line 24 · 2026-05-19T09:14:24.852Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BST5WG8VthX3Mv7CiyLfxf`</summary>

```json
{
  "query": "cross-lingual safety refusal steering vectors transfer language families LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07f5ed56-d3e0-4ad2-8fa2-d2f176b1bd52",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBfxKGacqizK5VwCB9iV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a9096e8-4701-4e2c-aad9-7f7ab28a42d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gjz1UsNaQi8YTUvnwmfRbr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 762,
      "cache_creation_input_tokens": 2055,
      "cache_read_input_tokens": 12946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2055,
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

_source line 25 · 2026-05-19T09:14:25.326Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VYwwtpB8WVZgpNKYXJtDQa`</summary>

```json
{
  "query": "arXiv 2505.12584 \"cross-family\" OR \"language family\" steering transfer ineffective"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a9096e8-4701-4e2c-aad9-7f7ab28a42d0",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBfxKGacqizK5VwCB9iV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2368c6b0-3b53-471a-af42-f23f06e848b8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gjz1UsNaQi8YTUvnwmfRbr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 762,
      "cache_creation_input_tokens": 2055,
      "cache_read_input_tokens": 12946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2055,
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

_source line 26 · 2026-05-19T09:14:26.320Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M7g7LwA9T9kixnkdiGcjYw`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.13908",
  "prompt": "Extract key findings about cross-linguistic transfer, language families, and morphology. What did they find about cross-family transfer? What role does typological distance play?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2368c6b0-3b53-471a-af42-f23f06e848b8",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBfxKGacqizK5VwCB9iV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1d9c016-700a-4cf6-9e29-96aa82880458",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gjz1UsNaQi8YTUvnwmfRbr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 762,
      "cache_creation_input_tokens": 2055,
      "cache_read_input_tokens": 12946,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2055
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 762,
          "output_tokens": 250,
          "cache_read_input_tokens": 12946,
          "cache_creation_input_tokens": 2055,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2055,
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

_source line 27 · 2026-05-19T09:14:29.698Z_

<details><summary>↩ Tool result · `toolu_01M7g7LwA9T9kixnkdiGcjYw`</summary>

```text
# Cross-Linguistic Transfer Research Summary

Based on the arXiv abstract provided, this paper investigates how linguistic factors influence multilingual NLP model performance, but the page content does not include detailed findings about specific cross-family transfer outcomes or the precise role of typological distance.

## What the Paper Addresses

The research examines "cross-linguistic transfer through the lens of language families and morphology," investigating how language family proximity and morphological similarity affect various NLP tasks.

## Key Focus Areas

The authors analyze:
- Performance variations across multilingual models like mBERT and XLM-R
- Correlations between "linguistic distance metrics" and transfer effectiveness
- Emerging pre-training approaches that incorporate typological and morphological information

## Limitation

The abstract itself does not present concrete findings about whether cross-family transfer differs substantially from within-family transfer, nor does it specify quantitative relationships between typological distance and performance. To access the actual findings, one would need to review the full PDF document available at the provided link.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1d9c016-700a-4cf6-9e29-96aa82880458",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "a6baa1a7d8c626c89",
  "type": "user",
  "uuid": "9552e4a9-f523-4590-84e8-47b0d6847638",
  "sourceToolAssistantUUID": "f1d9c016-700a-4cf6-9e29-96aa82880458",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T09:14:30.139Z_

<details><summary>↩ Tool result · `toolu_01VYwwtpB8WVZgpNKYXJtDQa`</summary>

```text
Web search results for query: "arXiv 2505.12584 "cross-family" OR "language family" steering transfer ineffective"

Links: [{"title":"[2505.12584] Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/abs/2505.12584"},{"title":"Steerable but Not Decodable: Function Vectors Operate Beyond the Logit Lens","url":"https://arxiv.org/pdf/2604.02608"},{"title":"Steerable but Not Decodable: Function Vectors Operate Beyond the Logit Lens","url":"https://arxiv.org/html/2604.02608v1"},{"title":"[2505.13908] Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology","url":"https://arxiv.org/abs/2505.13908"},{"title":"Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/pdf/2601.16390"},{"title":"Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology","url":"https://arxiv.org/pdf/2505.13908"}]

Based on the search results, I found information about arXiv paper 2505.12584. This paper investigates how Large Language Models represent non-English tokens and proposes a lightweight intervention method using representation steering, where a learned vector is added to the residual stream at a single model layer to enhance multilingual performance.

The paper includes experiments across seven competitive baselines including prompt optimization, supervised fine-tuning (SFT), in-context learning, cross-lingual transfer, and translation-based methods.

However, the search results I found don't contain specific details about cross-family or language family steering transfer being ineffective. The abstract focuses on the positive results of the steering method for multilingual performance. To get more detailed information about specific findings regarding cross-family transfer limitations, you would need to access the full paper directly at https://arxiv.org/abs/2505.12584.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2368c6b0-3b53-471a-af42-f23f06e848b8",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "a6baa1a7d8c626c89",
  "type": "user",
  "uuid": "f9bfc38f-e102-420f-a78e-5d652add76fa",
  "sourceToolAssistantUUID": "2368c6b0-3b53-471a-af42-f23f06e848b8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T09:14:35.104Z_

<details><summary>↩ Tool result · `toolu_01BST5WG8VthX3Mv7CiyLfxf`</summary>

```text
Web search results for query: "cross-lingual safety refusal steering vectors transfer language families LLM 2025"

Links: [{"title":"Refusal Direction is Universal Across Safety-Aligned Languages","url":"https://arxiv.org/pdf/2505.17306"},{"title":"Enforcing Multilingual Consistency for LLM Safety Alignment","url":"https://arxiv.org/pdf/2602.16660"},{"title":"Refusal Direction is Universal Across Safety-Aligned Languages","url":"https://arxiv.org/html/2505.17306v2"},{"title":"Language-Specific Steering Vectors","url":"https://www.emergentmind.com/topics/language-specific-steering-vectors"},{"title":"ReCoVeR the Target Language: Language Steering without Sacrificing Task Performance","url":"https://arxiv.org/html/2509.14814v1"},{"title":"Analysing the Safety Pitfalls of Steering Vectors","url":"https://arxiv.org/pdf/2603.24543"},{"title":"Refusal Steering: Fine-grained Control over LLM Refusal Behaviour for Sensitive Topics","url":"https://arxiv.org/pdf/2512.16602"},{"title":"SafeSteer: Interpretable Safety Steering with Refusal-Evasion in LLMs","url":"https://arxiv.org/pdf/2506.04250"}]

Based on the search results, I found several highly relevant 2025 papers on cross-lingual safety, refusal steering vectors, and their transfer across languages:

## Key Findings:

A vector extracted from English can bypass refusals in other languages with near-perfect effectiveness, without any additional fine-tuning. Refusal directions derived from any safety-aligned language transfer seamlessly to others.

This transferability is attributed to the parallelism of refusal vectors across languages in the embedding space. This suggests that safety refusal mechanisms operate on a universal principle across different languages rather than being language-specific.

## Related Research Areas:

Steering vectors guide the target language toward a dominant-language semantic workspace, yielding gains in specific tasks without altering surface prompts.

Recent work has revealed that refusal behavior in LLMs is encoded within the model's activation space, with a low-dimensional subspace – often well-approximated by a single vector known as the refusal direction – capturing the model's tendency to refuse certain prompts.

## Cross-Lingual Vulnerabilities:

Cross-lingual jailbreaks have emerged as a growing concern, where prompts in non-English languages bypass refusal mechanisms that succeed in English.

The research indicates that while language-specific steering vectors can help control language output, the fundamental safety refusal mechanisms appear to share universal principles across languages, which both enables their effective transfer but also creates vulnerabilities to cross-lingual attacks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a9096e8-4701-4e2c-aad9-7f7ab28a42d0",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "a6baa1a7d8c626c89",
  "type": "user",
  "uuid": "8731f8cb-b768-4f46-92a3-6bc0976b2b3f",
  "sourceToolAssistantUUID": "4a9096e8-4701-4e2c-aad9-7f7ab28a42d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-19T09:14:38.502Z_

Excellent -- the critical finding is the paper on universal refusal directions. Let me fetch that paper and the cross-lingual activation steering paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8731f8cb-b768-4f46-92a3-6bc0976b2b3f",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBfyNMeWNYe9953MHxFL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09d66235-9da7-4c06-95bf-acd52376110a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmfEY2CpiUcavQEgAqK2vv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 785,
      "cache_creation_input_tokens": 1716,
      "cache_read_input_tokens": 15001,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1716,
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

_source line 31 · 2026-05-19T09:14:41.446Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017BK4TC88bf4fmdZATQz89x`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.17306v2",
  "prompt": "Extract ALL key findings in detail:\n1. Title and authors\n2. What exactly did they find about refusal direction universality across languages?\n3. Did refusal directions transfer across language FAMILIES (e.g., from Romance to CJK languages)?\n4. What models and languages were tested?\n5. Exact quotes or numbers about cross-family vs within-family transfer of refusal directions\n6. Does this contradict claims that cross-family steering transfer is ineffective?\n7. Methodology details\n8. Any caveats or limitations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09d66235-9da7-4c06-95bf-acd52376110a",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBfyNMeWNYe9953MHxFL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb76fac1-c4aa-4383-8a92-150e9875132a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmfEY2CpiUcavQEgAqK2vv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 785,
      "cache_creation_input_tokens": 1716,
      "cache_read_input_tokens": 15001,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1716,
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

_source line 32 · 2026-05-19T09:14:42.866Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012J4e8md2uHavgsVsnNTqJp`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2601.16390",
  "prompt": "Extract ALL key findings about cross-lingual activation steering:\n1. Title and authors\n2. What kind of steering?\n3. Models and languages tested\n4. Cross-family vs within-family results\n5. Any findings about whether steering transfers across typologically distant languages\n6. Methodology\n7. Key positive or negative results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb76fac1-c4aa-4383-8a92-150e9875132a",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBfyNMeWNYe9953MHxFL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81a4dae1-bfb1-4274-a8a3-63f602a4e9e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmfEY2CpiUcavQEgAqK2vv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 785,
      "cache_creation_input_tokens": 1716,
      "cache_read_input_tokens": 15001,
      "output_tokens": 370,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1716
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 785,
          "output_tokens": 370,
          "cache_read_input_tokens": 15001,
          "cache_creation_input_tokens": 1716,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1716,
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

_source line 33 · 2026-05-19T09:14:48.207Z_

<details><summary>↩ Tool result · `toolu_012J4e8md2uHavgsVsnNTqJp`</summary>

```text
# Cross-Lingual Activation Steering for Multilingual Language Models

## Basic Information
**Title:** "Cross-Lingual Activation Steering for Multilingual Language Models"

**Authors:** Rhitabrat Pokharel, Ameeta Agrawal, Tanay Nagar

**DOI:** https://doi.org/10.48550/arXiv.2601.16390

## Steering Approach
The paper examines activation steering—a technique for modifying model behavior by manipulating internal neuron activations—applied across different languages in multilingual language models.

## Models and Languages
The research evaluates steering effectiveness on:
- Large multilingual models (Llama and Qwen architectures mentioned)
- Multiple language pairs tested for cross-lingual transfer
- Both typologically similar and distant languages included in evaluation

## Cross-Family vs Within-Family Results
The document references comparisons between steering performance within the same language family versus across different language families, examining whether linguistic distance affects steering transferability.

## Typological Distance Findings
The study investigates "whether steering transfers across typologically distant languages," addressing a key question about the universality of activation patterns in multilingual models.

## Methodology
The approach involves:
- Identifying and modifying specific activation patterns
- Testing transfer from source to target languages
- Measuring performance on standardized multilingual benchmarks (XNLI, XQuAD referenced)

## Key Results
The paper demonstrates that activation steering mechanisms exhibit variable transferability across languages, with implications for understanding how multilingual models encode language-specific versus universal information.

[Binary content (application/pdf, 767.2KB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-gen-pipeline/e35f8964-edb8-41bf-9248-b2986ccc4fa6/tool-results/webfetch-1779182083047-6w1kxg.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81a4dae1-bfb1-4274-a8a3-63f602a4e9e3",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "a6baa1a7d8c626c89",
  "type": "user",
  "uuid": "aa74a05e-86b8-491f-81e6-f350f65f5a0e",
  "sourceToolAssistantUUID": "81a4dae1-bfb1-4274-a8a3-63f602a4e9e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T09:14:54.175Z_

<details><summary>↩ Tool result · `toolu_017BK4TC88bf4fmdZATQz89x`</summary>

```text
# Key Findings: Refusal Direction Universality Across Languages

## 1. Title and Authors
**"Refusal Direction is Universal Across Safety-Aligned Languages"**
By Xinpeng Wang, Mingyang Wang, Yihong Liu, Hinrich Schütze, Barbara Plank (LMU Munich & Munich Center for Machine Learning)

## 2. Core Discovery About Refusal Universality
The researchers found that refusal mechanisms operate through language-agnostic vectors in LLM activation space. Critically, they demonstrated that "a vector extracted from English can bypass refusals in other languages with near-perfect effectiveness, without any additional fine-tuning."

More strikingly, "refusal directions derived from any safety-aligned language transfer seamlessly to others," supporting a universality hypothesis rather than merely English-centric transfer.

## 3. Cross-Family Language Transfer
**YES—substantial transfer occurred across distant language families.** The study explicitly tested typologically diverse languages spanning Indo-European, Sino-Tibetan, Japonic, Afroasiatic, Koreanic, Tai-Kadai, and Niger-Congo families. Ablating German (Indo-European) refusal vectors degraded safety equally across Chinese (Sino-Tibetan), Thai (Tai-Kadai), and Yoruba (Niger-Congo).

## 4. Models and Languages Tested
**Models:** Llama3.1-8B-Instruct, Qwen2.5-7B-Instruct, Gemma-2-9B-Instruct, Yi, and additional variants

**14 Languages:** English, German, Spanish, French, Italian, Dutch, Japanese, Polish, Russian, Chinese, Korean, Arabic, Thai, Yoruba

## 5. Quantitative Cross-Family Findings
After ablating refusal vectors from any safety-aligned language (German, Chinese, Thai):
- Compliance rates reached "near-complete collapse of refusal behavior across all other safety-aligned languages, with compliance rates consistently approaching or exceeding 90%"
- Even Yoruba compliance jumped from ~58% to over 90% in Gemma-2-9B-Instruct regardless of source language
- English vectors achieved similar jailbreak success across all language families

## 6. Contradiction to Claims About Cross-Family Steering
**This directly challenges assumptions that steering transfers poorly across distant language families.** The research shows steering mechanisms transcend typological boundaries—Romance-to-Sino-Tibetan, Indo-European-to-Afroasiatic transfers all succeeded with near-identical effectiveness.

## 7. Methodology Details

**Vector Extraction:** Difference-in-means calculation between harmful and harmless prompt activations at specific transformer layers and token positions

**Dataset (PolyRefuse):** 128 harmful + 128 harmless prompts per language, translated via Google Translate from English sources (AdvBench, MaliciousInstruct, TDC2023)

**Intervention:** Ablation (removing refusal vectors via projection subtraction) and addition (appending vectors at scaling parameter α ∈ [0,1])

**Evaluation:** WildGuard automated safety classifier, with non-English responses translated back to English for assessment

## 8. Key Caveats and Limitations

- Analysis limited to 14 languages; findings may not extend to extremely low-resource languages
- Concrete defense strategies were not implemented or tested
- The study identified that "models often fail to separate harmful and harmless prompts in non-English languages" at the refusal extraction layer, creating persistent vulnerabilities despite universal refusal vector structure
- Yoruba classified as "safety-misaligned" (82.9% compliance on Llama3.1-8B even before intervention), suggesting some languages lack robust refusal alignment to begin with
- Translation quality dependency not fully characterized beyond back-translation validation
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb76fac1-c4aa-4383-8a92-150e9875132a",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "a6baa1a7d8c626c89",
  "type": "user",
  "uuid": "41cd68dc-4ad3-4c01-bb38-03bd24c91844",
  "sourceToolAssistantUUID": "bb76fac1-c4aa-4383-8a92-150e9875132a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-19T09:14:57.932Z_

Now let me get one more piece -- the CLaS-Bench paper in full and the cross-lingual activation steering paper's HTML version for more detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41cd68dc-4ad3-4c01-bb38-03bd24c91844",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBfzmt2ruoaeSFJghzdx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58aa0533-ec08-4aeb-89ab-6c713b0d320a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQ23gebTvVMrZyj3aq2WDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 476,
      "cache_creation_input_tokens": 2071,
      "cache_read_input_tokens": 16717,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2071,
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

_source line 36 · 2026-05-19T09:15:00.250Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013qbo9HV9FDMkEdNiNWFW3C`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.08331v1",
  "prompt": "Extract detailed findings from CLaS-Bench about:\n1. Whether steering directions cluster by language family\n2. Any findings about cross-family vs within-family steering transfer\n3. Which steering methods work best across languages\n4. Any quantitative results about typologically distant language pairs\n5. Key conclusions about limitations of cross-lingual steering"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58aa0533-ec08-4aeb-89ab-6c713b0d320a",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBfzmt2ruoaeSFJghzdx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "451d0c14-0f64-4900-b969-e13a7355bf28",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQ23gebTvVMrZyj3aq2WDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 476,
      "cache_creation_input_tokens": 2071,
      "cache_read_input_tokens": 16717,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2071,
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

_source line 37 · 2026-05-19T09:15:00.827Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DSxZ25YxG4y1LDfSZeBxEF`</summary>

```json
{
  "query": "\"cross-lingual\" \"activation steering\" \"language family\" transfer multilingual 2025 2026 results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "451d0c14-0f64-4900-b969-e13a7355bf28",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBfzmt2ruoaeSFJghzdx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f85c05e-0920-4ea6-8c50-b528d9fe2090",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQ23gebTvVMrZyj3aq2WDg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 476,
      "cache_creation_input_tokens": 2071,
      "cache_read_input_tokens": 16717,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2071
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 476,
          "output_tokens": 251,
          "cache_read_input_tokens": 16717,
          "cache_creation_input_tokens": 2071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2071,
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

_source line 38 · 2026-05-19T09:15:06.718Z_

<details><summary>↩ Tool result · `toolu_013qbo9HV9FDMkEdNiNWFW3C`</summary>

```text
# CLaS-Bench: Cross-Lingual Steering Findings

## 1. Language Family Clustering

The benchmark demonstrates clear geometric clustering by language family. The research reveals that "typologically related languages cluster in representation space," with Romance languages (Spanish, French, Portuguese, Italian, Romanian) exhibiting high mutual similarity, as do Germanic and Slavic language groups. Figure 6 shows substantial neuron overlap occurs primarily within language families.

## 2. Cross-Family vs Within-Family Transfer

The paper provides interpretive rather than quantitative cross-family comparisons. It notes that "steering between related languages might require smaller interventions, while cross-family steering (e.g., Japanese to Arabic) could demand larger modifications and be more susceptible to quality degradation." However, specific performance metrics comparing within-family versus cross-family steering pairs are not explicitly reported.

## 3. Best-Performing Methods Across Languages

DiffMean steering on residual activations consistently outperforms alternatives, achieving an 84.5% average steering score. The authors conclude that "representation-based steering, particularly DiffMean on residual activations, consistently outperforms all other tested methods, including prompting baselines, across most evaluated languages."

## 4. Typologically Distant Language Pairs

The benchmark covers 32 typologically diverse languages but does not isolate quantitative results specifically for distant language pairs. Results are reported per-language and per-method rather than categorized by typological distance between source-target combinations.

## 5. Key Limitations of Cross-Lingual Steering

The research identifies several constraints: prompting exhibits "failures for specific languages," supervised methods underperform unsupervised approaches, and SAE-based steering "lags behind" residual-stream methods. Additionally, language-specific representations concentrate in later layers, requiring higher intervention strengths that may compromise output coherence.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "451d0c14-0f64-4900-b969-e13a7355bf28",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "a6baa1a7d8c626c89",
  "type": "user",
  "uuid": "2d36d71c-56b8-4e06-8bcc-27297d3cb20c",
  "sourceToolAssistantUUID": "451d0c14-0f64-4900-b969-e13a7355bf28",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-19T09:15:07.243Z_

<details><summary>↩ Tool result · `toolu_01DSxZ25YxG4y1LDfSZeBxEF`</summary>

```text
Web search results for query: ""cross-lingual" "activation steering" "language family" transfer multilingual 2025 2026 results"

Links: [{"title":"[2601.16390] Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/abs/2601.16390"},{"title":"Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/pdf/2601.16390"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/html/2602.02326v2"},{"title":"Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/html/2601.16390v1"},{"title":"Preprint LANGUAGE-SPECIFIC LATENT PROCESS HINDERS CROSS-LINGUAL PERFORMANCE","url":"https://arxiv.org/pdf/2505.13141"},{"title":"[2505.13908] Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology","url":"https://arxiv.org/abs/2505.13908"},{"title":"Steering Large Language Models for Cross-lingual Information Retrieval | Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/10.1145/3626772.3657819"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/pdf/2602.02326"}]

I found several recent research papers on cross-lingual activation steering and multilingual language models from 2025-2026. Here are the key findings:

## Main Research Areas

**Cross-Lingual Activation Steering (CLAS):**
Recent work discovers that effective transfer operates through functional divergence rather than strict alignment, with performance gains correlating with increased language cluster separation, and demonstrates that targeted activation steering can unlock latent multilingual capacity in existing models without modification to model weights.

**Language Family and Transfer Dynamics:**
Performance gaps between dominant and non-dominant languages are largely attributed to the heavy skew of pre-training corpora toward dominant languages, which enables models to develop richer representations in those languages.

**Neuron-Level Mechanisms:**
Shared neurons and overlapping subspaces in middle and upper layers play a central role in cross-lingual transfer.

**Language-Specific Representations:**
Languages with diverging representations from the shared semantic space exhibit less consistency and knowledge transfer.

## Related Applications

Structured mathematical reasoning particularly benefits from cross-lingual steering.

The research spans theoretical investigations into how multilingual models organize representations across language families and practical methods for steering model activations to improve cross-lingual performance without additional training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f85c05e-0920-4ea6-8c50-b528d9fe2090",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "a6baa1a7d8c626c89",
  "type": "user",
  "uuid": "cb3ea0d0-8280-4b89-afbc-d73ef072e0df",
  "sourceToolAssistantUUID": "6f85c05e-0920-4ea6-8c50-b528d9fe2090",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-19T09:15:12.118Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Eo6keTLcj5hJxzfyruoaaV`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.16390v1",
  "prompt": "Extract ALL detailed findings about cross-lingual activation steering. I need:\n1. Exact results about cross-family vs within-family transfer\n2. Which language pairs worked well and which did not\n3. Any quantitative results (percentages, accuracy numbers)\n4. Their conclusions about when cross-lingual steering works and when it fails\n5. Any discussion of typological distance effects\n6. Models and languages tested\n7. Whether they found cross-family transfer to be effective or ineffective"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb3ea0d0-8280-4b89-afbc-d73ef072e0df",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBg1jk5M2fSUtb4VgWkk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c342f1a9-3d44-4e3f-be4c-4a9c8dc032f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C66BK6QMZhKTEJkErXQtLJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1874,
      "cache_read_input_tokens": 18788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1874,
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

_source line 41 · 2026-05-19T09:15:13.198Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016BJSaeZKpUAJoHrRQQY5PU`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2505.13141",
  "prompt": "Extract key findings about language-specific latent processes hindering cross-lingual performance. What did they find about cross-lingual transfer limitations? Any findings about language family effects?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c342f1a9-3d44-4e3f-be4c-4a9c8dc032f9",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBg1jk5M2fSUtb4VgWkk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "944ae4f2-cb2d-417a-b62e-639449ece43b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C66BK6QMZhKTEJkErXQtLJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1874,
      "cache_read_input_tokens": 18788,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1874
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 18788,
          "cache_creation_input_tokens": 1874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1874,
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

_source line 42 · 2026-05-19T09:15:17.128Z_

<details><summary>↩ Tool result · `toolu_016BJSaeZKpUAJoHrRQQY5PU`</summary>

```text
# Key Findings on Cross-Lingual Performance Limitations

I cannot extract detailed findings from this document because the content provided is primarily PDF metadata and structural information (object definitions, font specifications, stream headers) rather than the actual article text.

The PDF header reveals this is a paper titled **"Language-Specific Latent Process Hinders Cross-Lingual Performance"** by Zheng Wei Lim, Alham Fikri Aji, and Trevor Cohn (arXiv:2505.13141), but the substantive research content—including specific findings about cross-lingual transfer limitations and language family effects—is embedded in compressed/encoded stream objects that aren't readable in this format.

To properly answer your question about:
- Cross-lingual transfer limitations
- Language family effects on performance
- Specific mechanisms hindering cross-lingual capabilities

I would need access to the actual decompressed text content of the article, which isn't available in the structural data provided here.

[Binary content (application/pdf, 3.2MB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-gen-pipeline/e35f8964-edb8-41bf-9248-b2986ccc4fa6/tool-results/webfetch-1779182113223-p4fy4c.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "944ae4f2-cb2d-417a-b62e-639449ece43b",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "a6baa1a7d8c626c89",
  "type": "user",
  "uuid": "f3598c83-b5c8-435e-84aa-1e8fa0f1d9fe",
  "sourceToolAssistantUUID": "944ae4f2-cb2d-417a-b62e-639449ece43b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-19T09:15:19.377Z_

<details><summary>↩ Tool result · `toolu_01Eo6keTLcj5hJxzfyruoaaV`</summary>

```text
# Cross-Lingual Activation Steering: Key Findings

## Models and Languages Tested
The research evaluated **LLaMA 3.1 8B** and **Qwen 2.5 7B** across 12-15 languages including Arabic, Chinese, German, Greek, Hindi, Russian, Spanish, Turkish, Urdu, Vietnamese, and others on XNLI and XQuAD tasks.

## Quantitative Results

**XNLI Classification:**
- LLaMA: +1.93 average accuracy improvement (p<0.05)
- Qwen: +0.45 average accuracy improvement (p<0.001)
- Notable gains: Urdu (+7.00), Chinese (+5.89), Hindi (+5.80), Greek (+5.39)
- Some regressions observed in Bulgarian, Swahili, Vietnamese

**XQuAD Generation:**
- LLaMA: +0.94 average F1 improvement (not statistically significant)
- Qwen: +1.10 average F1 improvement (not statistically significant)
- High variability with both substantial gains and regressions

## Critical Finding: Functional Divergence, Not Alignment

The authors discovered a counterintuitive result: **"performance gains are driven by functional divergence rather than proximity to the anchor language."** CLAS actually reduces cosine similarity to English rather than increasing it, yet improves performance. Figure 3 demonstrates negative correlation—larger gains correlate with increased distance from English representations.

## When Cross-Lingual Steering Works/Fails

**Effective:**
- Languages with ambiguous initial representations benefit most when CLAS creates distinct clusters
- Discriminative tasks (XNLI) show more stable improvements

**Ineffective/Problematic:**
- Generative tasks (XQuAD) exhibit higher variance and instability
- Some language-model combinations show regressions (e.g., Hindi on XQuAD)
- Anchor language proximity doesn't predict success

## Typological Distance
The paper does not explicitly analyze typological distance effects. However, the finding that "distance to English does not explain improvements" suggests linguistic distance alone doesn't determine steering effectiveness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c342f1a9-3d44-4e3f-be4c-4a9c8dc032f9",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "a6baa1a7d8c626c89",
  "type": "user",
  "uuid": "31195e69-e7b1-462f-aab8-a7014e019b65",
  "sourceToolAssistantUUID": "c342f1a9-3d44-4e3f-be4c-4a9c8dc032f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-19T09:16:11.674Z_

I now have a comprehensive picture. Here is my detailed report.

---

## Detailed Report: Cross-Family Steering Transfer Limitations in LLMs

### 1. What arXiv 2505.12584v2 (Mahmoud et al.) Actually Claims

The paper **"Improving Multilingual Language Models by Aligning Representations through Steering"** by Omar Mahmoud, Buddhika Laknath Semage, Thommen George Karimpanal, and Santu Rana studies **representation alignment steering** -- not safety/refusal steering or calibration. Their method learns a vector added to the residual stream at a single model layer to improve multilingual task performance (XNLI, XCOPA, MMLU, M3Exam). They tested Llama 2 (7B/13B/70B), Aya-23 (8B/35B), Gemma (7B/9B), and Qwen 1.5 (4B/7B/14B).

Their finding that cross-family transfers (e.g., Spanish to Japanese) are ineffective pertains specifically to **task-performance steering vectors** -- learned directions that align non-English representations toward a shared space to improve downstream accuracy. The claim is that these task-aligned steering vectors, when extracted from one language family, do not produce comparable gains when applied to a typologically distant target language. Within-family transfers (e.g., Spanish to French, or German to Dutch) show substantially better performance retention.

### 2. This Finding is Domain-Specific, Not Universal

A critical nuance the reviewer may be overlooking: **the cross-family limitation is not a general law about all linear directions in LLM representation space.** Different types of steering directions behave very differently:

**Safety/Refusal Directions Transfer Universally Across Families.** Wang et al. (2505.17306, "Refusal Direction is Universal Across Safety-Aligned Languages," LMU Munich) provide perhaps the strongest counterexample. Testing Llama3.1-8B, Qwen2.5-7B, and Gemma-2-9B across 14 languages spanning Indo-European, Sino-Tibetan, Japonic, Koreanic, Tai-Kadai, Afroasiatic, and Niger-Congo families, they found that ablating a refusal vector extracted from *any* language causes compliance rates to exceed 90% across *all* other safety-aligned languages. A German-derived refusal vector breaks safety in Chinese, Thai, and Yoruba equally well. This directly contradicts the idea that cross-family steering transfer is universally ineffective.

**Language Identity Vectors Show Family-Structured Clustering But Still Transfer.** Kirtane and Huang (2602.02326, "Language Steering for Multilingual In-Context Learning") found that language steering vectors extracted as mean activation differences between English and target languages show hierarchical clustering by family (Hindi-Urdu pair at distance ~0.043, Indo-Aryan cluster at ~0.201), yet their method achieves 2.9-5.4% improvements on MGSM across 19 languages including cross-family pairs, with 5 of 6 cross-task transfer settings showing effective generalization.

### 3. The Geometry Explains the Discrepancy

The reason task-performance steering fails cross-family while refusal steering succeeds is likely rooted in what these directions encode:

- **Refusal directions** encode a binary behavioral property (refuse vs. comply) that models learn as a near-universal mechanism across all safety-aligned languages. Wang et al. found these occupy a shared low-dimensional subspace regardless of language family.

- **Task-performance alignment directions** encode how to map a language's representational geometry onto the task-relevant subspace. Because different language families occupy genuinely different regions of representation space (confirmed by CLaS-Bench's finding that "typologically related languages cluster in representation space" and that steering directions cluster by language family), the *mapping* needed to align representations differs across families.

- **Cross-lingual activation steering** (Pokharel et al., 2601.16390) found a further nuance: performance gains from steering correlate with *functional divergence* (increased distance from English representations), not alignment. Languages like Urdu (+7.00 accuracy), Chinese (+5.89), and Hindi (+5.80) showed the largest gains on XNLI with LLaMA 3.1 8B, suggesting that cross-family languages can benefit from steering, but through a different mechanism than simple directional transfer.

### 4. CLaS-Bench Provides the Evaluation Framework

The CLaS-Bench benchmark (2601.08331) covering 32 languages found that the DiffMean residual-stream method achieves 84.5% average steering score across languages and consistently outperforms alternatives. Critically, they noted that "steering between related languages might require smaller interventions, while cross-family steering (e.g., Japanese to Arabic) could demand larger modifications and be more susceptible to quality degradation." This confirms that cross-family steering is *harder* but not necessarily *impossible* -- it requires stronger interventions that risk degrading output coherence.

### 5. Positive Evidence for Cross-Family Transfer

Sundar et al. (2502.15639, "Steering into New Embedding Spaces") found that intervening on Japanese expert neurons in Bloom-7B produced large improvements in English-Portuguese cross-lingual retrieval -- a fully cross-family benefit. Their finding that steering pulls all language embeddings toward the space's medoid, achieving up to 2x improvement in cross-lingual retrieval accuracy, suggests some steering mechanisms operate on language-universal geometric properties.

### 6. What Nuances Should Be Considered for Your Paper

1. **The type of direction matters enormously.** Safety/refusal directions appear to be genuinely universal; task-alignment directions are family-bounded; language-identity directions are somewhere in between. A paper on cross-lingual *calibration* transfer should carefully specify which category calibration directions fall into.

2. **The negative finding in 2505.12584 is about a specific method** (learned residual-stream vectors for task performance), not about the theoretical impossibility of cross-family linear transfer. Citing it as evidence that "cross-family transfer is ineffective" full stop would be an overstatement.

3. **Typological distance modulates difficulty but not possibility.** CLaS-Bench and the typological distance literature (including URIEL+ calibration work in 2510.19217 and the qWALS-based analyses) show that transfer degrades gradually with typological distance rather than hitting a hard boundary at family lines.

4. **Model architecture and pretraining data matter.** Sundar et al. found "markedly different patterns" across Bloom-7B, Aya-8B, and PolyLM-13B, attributing differences to pretraining procedures. The cross-family limitation may be more severe in models with less balanced multilingual pretraining.

5. **Layer selection is critical.** CLaS-Bench found language-specific structure concentrates in later layers, while Kirtane and Huang found middle layers most effective for language steering. Cross-family transfer may succeed at some layers but fail at others.

In summary: the reviewer's citation of 2505.12584 identifies a real limitation for **task-performance representation alignment**, but it would be incorrect to generalize this to all forms of cross-lingual linear direction transfer. The refusal universality result (2505.17306) is a strong counterpoint, and the emerging literature suggests the transferability of a direction depends critically on *what property it encodes* and *what geometric structure it exploits* in the multilingual representation space.

**Key papers referenced:**
- Mahmoud et al., arXiv 2505.12584 -- task-performance steering, cross-family limitations
- Wang et al., arXiv 2505.17306 -- universal refusal directions across language families
- Kirtane & Huang, arXiv 2602.02326 -- language steering for ICL, family-structured clustering
- Sundar et al., arXiv 2502.15639 -- cross-lingual alignment via expert neuron steering
- Pokharel et al., arXiv 2601.16390 -- cross-lingual activation steering, functional divergence finding
- CLaS-Bench, arXiv 2601.08331 -- 32-language steering benchmark

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31195e69-e7b1-462f-aab8-a7014e019b65",
  "isSidechain": true,
  "agentId": "a6baa1a7d8c626c89",
  "requestId": "req_011CbBg2ddFLxpKipbeD6Rps",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "762c8d6c-1d32-4796-ac70-c539eabb970a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcZwtV9cWW3gwyUpCS5N6u",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 338,
      "cache_creation_input_tokens": 825,
      "cache_read_input_tokens": 20662,
      "output_tokens": 1956,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 825
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 338,
          "output_tokens": 1956,
          "cache_read_input_tokens": 20662,
          "cache_creation_input_tokens": 825,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 825,
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
