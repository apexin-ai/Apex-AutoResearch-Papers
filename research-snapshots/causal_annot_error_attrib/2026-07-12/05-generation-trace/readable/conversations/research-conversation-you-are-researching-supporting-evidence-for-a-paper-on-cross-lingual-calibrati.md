# Research conversation: You are researching supporting evidence for a paper on cross-lingual calibration transfer in LLMs. A reviewer suggested 

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ae15bcf2ece33be45.jsonl`
- **Structured JSON:** [`7f93e5142ebdf93c8fd4.json`](../../sessions/7f/7f93e5142ebdf93c8fd4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-19T09:13:55.854Z_

You are researching supporting evidence for a paper on cross-lingual calibration transfer in LLMs.

A reviewer suggested we cite arXiv 2505.17306 "Refusal Direction is Universal Across Safety-Aligned Languages" as supporting evidence that some representation directions transfer cross-lingually.

Your tasks:
1. Use WebFetch to read https://arxiv.org/abs/2505.17306 — extract: key findings, how many languages tested, which models, how they identified the refusal direction, how well it transferred across languages, any limitations on cross-family transfer, and the exact mechanism of direction extraction.
2. Use WebSearch for "universal direction representation space cross-lingual LLM 2025 2026" to find other papers showing universal/shared directions across languages.
3. Use WebSearch for "linear direction representation engineering cross-lingual transfer 2025 2026" to find additional supporting or contradicting evidence.

Report in detail (400+ words): What does this paper show? How strong is the evidence for universal directions? What are the key caveats? How does this relate to calibration (as opposed to refusal)?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "ae15bcf2ece33be45",
  "type": "user",
  "uuid": "879eab09-2cca-4bb7-8309-2f545d4b2b74",
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

_source line 2 · 2026-05-19T09:13:55.856Z_

```json
{
  "parentUuid": "879eab09-2cca-4bb7-8309-2f545d4b2b74",
  "isSidechain": true,
  "agentId": "ae15bcf2ece33be45",
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
  "uuid": "a713053d-facd-453e-b8e8-399f22581a6f",
  "timestamp": "2026-05-19T09:13:55.856Z",
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

_source line 3 · 2026-05-19T09:13:55.857Z_

```json
{
  "parentUuid": "a713053d-facd-453e-b8e8-399f22581a6f",
  "isSidechain": true,
  "agentId": "ae15bcf2ece33be45",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f0d3ecc6-cb21-4f7a-8062-8649adc0d4a3",
  "timestamp": "2026-05-19T09:13:55.857Z",
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

_source line 4 · 2026-05-19T09:13:59.640Z_



I'll start by fetching the paper and running both web searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0d3ecc6-cb21-4f7a-8062-8649adc0d4a3",
  "isSidechain": true,
  "agentId": "ae15bcf2ece33be45",
  "requestId": "req_011CbBfvUasAbF9y1QUd8Ef7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a6880f4-f2ec-4a4e-9d8f-a5791984abad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Awm2fGq5A25TmyCcWZB8bK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1589,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1589,
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

_source line 5 · 2026-05-19T09:13:59.772Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01ETzvsjgFiRDcW41fGQqnvE`</summary>

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
  "parentUuid": "4a6880f4-f2ec-4a4e-9d8f-a5791984abad",
  "isSidechain": true,
  "agentId": "ae15bcf2ece33be45",
  "requestId": "req_011CbBfvUasAbF9y1QUd8Ef7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ca76287-43cc-4c85-9ecc-2ec935048073",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Awm2fGq5A25TmyCcWZB8bK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1589,
      "cache_read_input_tokens": 7773,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1589
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 97,
          "cache_read_input_tokens": 7773,
          "cache_creation_input_tokens": 1589,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1589,
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

_source line 6 · 2026-05-19T09:13:59.775Z_

<details><summary>↩ Tool result · `toolu_01ETzvsjgFiRDcW41fGQqnvE`</summary>

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
  "parentUuid": "7ca76287-43cc-4c85-9ecc-2ec935048073",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "ae15bcf2ece33be45",
  "type": "user",
  "uuid": "66ea7f03-9104-4e93-8e91-ae371d5d87c5",
  "sourceToolAssistantUUID": "7ca76287-43cc-4c85-9ecc-2ec935048073",
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

_source line 7 · 2026-05-19T09:14:02.507Z_



Now I'll fetch the paper and run both searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66ea7f03-9104-4e93-8e91-ae371d5d87c5",
  "isSidechain": true,
  "agentId": "ae15bcf2ece33be45",
  "requestId": "req_011CbBfvmbonQoaAf766sNHh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ccd8770-9aea-440e-88ef-5889b0857162",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsBJYtXtqsFCn7MTgpLnaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 9362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1119,
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

_source line 8 · 2026-05-19T09:14:05.789Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GBV9KH2wFjCbyiTDvvi79q`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.17306",
  "prompt": "Extract ALL of the following details from this paper abstract and page:\n\n1. Full title and authors\n2. Key findings / main claims\n3. How many languages were tested and which ones\n4. Which LLM models were used\n5. How they identified/extracted the refusal direction (exact mechanism)\n6. How well the refusal direction transferred across languages (quantitative results if available)\n7. Any limitations mentioned, especially regarding cross-family language transfer\n8. The methodology in detail - how directions were computed, what layers, what data was used\n9. Any discussion of universality of the direction across languages\n10. Date of publication"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ccd8770-9aea-440e-88ef-5889b0857162",
  "isSidechain": true,
  "agentId": "ae15bcf2ece33be45",
  "requestId": "req_011CbBfvmbonQoaAf766sNHh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a45702bc-09df-469e-8c3e-291cb7b25324",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsBJYtXtqsFCn7MTgpLnaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 9362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1119,
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

_source line 9 · 2026-05-19T09:14:06.263Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RRNZDuL1r9mTpPvPGArMiV`</summary>

```json
{
  "query": "universal direction representation space cross-lingual LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a45702bc-09df-469e-8c3e-291cb7b25324",
  "isSidechain": true,
  "agentId": "ae15bcf2ece33be45",
  "requestId": "req_011CbBfvmbonQoaAf766sNHh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eab4fabe-c540-4c59-860b-4aaae0087e82",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsBJYtXtqsFCn7MTgpLnaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 9362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1119,
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

_source line 10 · 2026-05-19T09:14:06.461Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TeP2KW1XczJrnidpsHn5GL`</summary>

```json
{
  "query": "linear direction representation engineering cross-lingual transfer 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eab4fabe-c540-4c59-860b-4aaae0087e82",
  "isSidechain": true,
  "agentId": "ae15bcf2ece33be45",
  "requestId": "req_011CbBfvmbonQoaAf766sNHh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7e21f04-656e-40a4-a408-d6a0564205ca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsBJYtXtqsFCn7MTgpLnaW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 9362,
      "output_tokens": 334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1119
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 334,
          "cache_read_input_tokens": 9362,
          "cache_creation_input_tokens": 1119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1119,
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

_source line 11 · 2026-05-19T09:14:11.351Z_

<details><summary>↩ Tool result · `toolu_01GBV9KH2wFjCbyiTDvvi79q`</summary>

```text
# Research Paper Summary: Refusal Direction Universality Across Languages

## 1. Title and Authors
**Title:** "Refusal Direction is Universal Across Safety-Aligned Languages"

**Authors:** Xinpeng Wang, Mingyang Wang, Yihong Liu, Hinrich Schütze, Barbara Plank

## 2. Key Findings
The research demonstrates that "a vector extracted from English can bypass refusals in other languages with near-perfect effectiveness, without any additional fine-tuning." Additionally, refusal directions derived from any safety-aligned language transfer seamlessly to others.

## 3. Languages Tested
The study examined **14 languages** through PolyRefuse, a multilingual safety dataset created by translating English prompts. However, the specific languages are not enumerated in the provided abstract.

## 4. LLM Models Used
The abstract does not specify which particular language models were tested in this research.

## 5. Refusal Direction Extraction Mechanism
The abstract does not detail the exact technical mechanism for identifying or extracting refusal directions from activation space.

## 6. Transfer Effectiveness Results
The study reports "near-perfect effectiveness" for cross-lingual transfer, but specific quantitative metrics are not provided in the abstract.

## 7. Limitations
No limitations regarding cross-family language transfer are mentioned in the provided content.

## 8. Detailed Methodology
The abstract lacks specific details about layer selection, computation methods, or data specifications.

## 9. Universality Discussion
The findings reveal "surprising cross-lingual universality" and attribute this to "parallelism of refusal vectors across languages in the embedding space."

## 10. Publication Date
**Submitted:** May 22, 2025; **Last Revised:** February 25, 2026 (v2)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a45702bc-09df-469e-8c3e-291cb7b25324",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "ae15bcf2ece33be45",
  "type": "user",
  "uuid": "879bf77a-fdd5-462e-a52f-1a104faf46f6",
  "sourceToolAssistantUUID": "a45702bc-09df-469e-8c3e-291cb7b25324",
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

_source line 12 · 2026-05-19T09:14:13.099Z_

<details><summary>↩ Tool result · `toolu_01RRNZDuL1r9mTpPvPGArMiV`</summary>

```text
Web search results for query: "universal direction representation space cross-lingual LLM 2025 2026"

Links: [{"title":"Refusal Direction is Universal Across Safety-Aligned Languages | OpenReview","url":"https://openreview.net/forum?id=eWxKpdAdXH"},{"title":"LUSIFER: Language Universal Space Integration for Enhanced Multilingual Embeddings with Large Language Models","url":"https://arxiv.org/html/2501.00874"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/pdf/2502.15639"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/pdf/2602.02326"},{"title":"Benchmarking Concept-Spilling Across Languages in LLMs Ilia Badanin EPFL","url":"https://arxiv.org/pdf/2601.12549"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/pdf/2502.14830"},{"title":"High-Dimensional Interlingual Representations of Large Language Models","url":"https://arxiv.org/pdf/2503.11280"}]

Based on the search results, here's what I found regarding universal direction representation space and cross-lingual LLMs in 2025-2026:

## Key Research Areas

**Universal Representation Spaces in Multilingual LLMs:**

Recent work like LUSIFER creates a language-agnostic universal space through multilingual encoder integration, serving as a bridge between different languages and enabling the target language model to process semantic information independently of the input language.

**Interlingual Representations:**

Interlingua, a universal language-neutral representation, is pivotal for cross-lingual generalization and aims to treat languages equitably and capture universal semantic structures independent of any specific language. However, evidence remains mixed on whether LLMs converge all language-specific representations into a unified single interlingual representation space, raising questions about whether LLMs develop a universal interlingua representation or present a partially aligned construct toward certain languages.

**Language Steering Through Representation Directions:**

If LLMs operate in a universal semantic space, then transferring knowledge across languages should not require retraining or additional data, but simply a way to redirect the model's internal representations toward the target language. Mean activation differences between contrastive inputs have been shown to encode interpretable directions in representation space, and such directions have been applied to address language confusion in multilingual models.

**Safety and Jailbreaks Across Languages:**

Research published at NeurIPS 2025 found that refusal directions in LLMs work across languages, revealing shared jailbreak mechanisms and raising the need for stronger multilingual safety.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eab4fabe-c540-4c59-860b-4aaae0087e82",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "ae15bcf2ece33be45",
  "type": "user",
  "uuid": "5af8fec0-73b2-441a-9da9-5515bd1a543a",
  "sourceToolAssistantUUID": "eab4fabe-c540-4c59-860b-4aaae0087e82",
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

_source line 13 · 2026-05-19T09:14:14.021Z_

<details><summary>↩ Tool result · `toolu_01TeP2KW1XczJrnidpsHn5GL`</summary>

```text
Web search results for query: "linear direction representation engineering cross-lingual transfer 2025 2026"

Links: [{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs | Request PDF","url":"https://www.researchgate.net/publication/394303200_Middle-Layer_Representation_Alignment_for_Cross-Lingual_Transfer_in_Fine-Tuned_LLMs"},{"title":"Rethinking Alignment in Cross-Lingual Knowledge Transfer | OpenReview","url":"https://openreview.net/forum?id=nId47dxIr2"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/pdf/2502.14830"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.778/"},{"title":"Semantic Aware Linear Transfer by Recycling Pre-trained Language Models for Cross-lingual Transfer","url":"https://arxiv.org/pdf/2505.10945"},{"title":"Cross-Lingual Representation Alignment Through ...","url":"https://aclanthology.org/2025.acl-short.95.pdf"}]

I found several relevant research papers on cross-lingual transfer and representation alignment from 2025-2026:

## Key Recent Research

Research analyzing LLM internal representations from over 1,000+ language pairs discovered that middle layers exhibit the strongest potential for cross-lingual alignment. Liu and Niehues published "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs" at ACL 2025.

Recent work formulates the cross-lingual transfer problem into a gradient alignment problem and then connects it to the representation alignment problem. This research was submitted to ICLR 2026 and addresses the performance gap between dominant languages like English and non-dominant languages like Turkish.

## Applications and Approaches

Experiments on slot filling, machine translation, and structured text generation show consistent improvements in cross-lingual transfer, especially to lower-resource languages. Cross-lingual word embeddings exhibit isometric relationships, where the geometric structure of semantically equivalent items is preserved across languages, a property proven crucial for transferring learned models across languages.

Cross-lingual transfer approaches include manipulating the vocabulary or initializing embeddings for new target vocabulary.

These recent papers highlight the focus on understanding and improving how neural models align representations across languages for better transfer learning performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7e21f04-656e-40a4-a408-d6a0564205ca",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "ae15bcf2ece33be45",
  "type": "user",
  "uuid": "0d612ab7-8710-491b-975f-fed07486d8a7",
  "sourceToolAssistantUUID": "c7e21f04-656e-40a4-a408-d6a0564205ca",
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

_source line 14 · 2026-05-19T09:14:18.094Z_

The abstract was sparse on details. Let me fetch the full paper content from the OpenReview page (which likely has the full PDF or more detail) and also the HTML version on arXiv for more technical depth.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d612ab7-8710-491b-975f-fed07486d8a7",
  "isSidechain": true,
  "agentId": "ae15bcf2ece33be45",
  "requestId": "req_011CbBfwpCMfR84GicUYpLGj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d13e3e9-89b4-4c81-a221-d7218cee57ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gi8NumaJk95ab7taGeC8jm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2153,
      "cache_read_input_tokens": 10481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2153,
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

_source line 15 · 2026-05-19T09:14:20.980Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QDVwGr8xu5MbcwJWFGEiWA`</summary>

```json
{
  "url": "https://openreview.net/forum?id=eWxKpdAdXH",
  "prompt": "Extract all technical details from this paper page:\n1. Which specific LLM models were tested?\n2. Which 14 languages were tested?\n3. The exact mechanism for extracting the refusal direction - how was it computed? Which layers? What contrastive data was used?\n4. Quantitative results: success rates for cross-lingual transfer of refusal direction\n5. Any limitations on cross-language-family transfer\n6. Any discussion of why the direction is universal\n7. Conference venue and reviews\n8. Any details about the PolyRefuse dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d13e3e9-89b4-4c81-a221-d7218cee57ee",
  "isSidechain": true,
  "agentId": "ae15bcf2ece33be45",
  "requestId": "req_011CbBfwpCMfR84GicUYpLGj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "774d60e8-111e-4741-b45a-eecd17fa85f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gi8NumaJk95ab7taGeC8jm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2153,
      "cache_read_input_tokens": 10481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2153,
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

_source line 16 · 2026-05-19T09:14:24.731Z_

<details><summary>↩ Tool result · `toolu_01QDVwGr8xu5MbcwJWFGEiWA`</summary>

```text
# Technical Details from Paper Page

Based on the provided OpenReview page content, here's what can be extracted:

## Available Information

**Dataset & Languages:**
The paper created "PolyRefuse, a multilingual safety dataset created by translating malicious and benign English prompts" across 14 languages, though the specific languages aren't listed on this page.

**Key Finding:**
"A vector extracted from English can bypass refusals in other languages with near-perfect effectiveness, without any additional fine-tuning."

**Mechanism Insight:**
The authors attribute findings "to the parallelism of refusal vectors across languages in the embedding space" and claim to "identify the underlying mechanism behind cross-lingual jailbreaks."

## Information NOT Available on This Page

Unfortunately, this OpenReview abstract page does not contain:
- Specific LLM models tested
- The 14 specific languages
- Technical details on refusal direction extraction (layers, computation methods, contrastive data)
- Quantitative success rates
- Cross-language-family limitations
- Detailed mechanistic explanations
- Peer review comments
- Comprehensive PolyRefuse dataset specifications

**Note:** This appears to be an abstract/landing page. The full paper (available via PDF download link) would contain these technical details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "774d60e8-111e-4741-b45a-eecd17fa85f3",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "ae15bcf2ece33be45",
  "type": "user",
  "uuid": "0ec51e44-1c34-4dd2-b00a-ee1f97160ac6",
  "sourceToolAssistantUUID": "774d60e8-111e-4741-b45a-eecd17fa85f3",
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

_source line 17 · 2026-05-19T09:14:24.807Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Pd3rXpchsi8R46sNTMyogD`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.17306",
  "prompt": "Extract ALL technical details from this paper:\n1. Which specific LLM models were tested?\n2. Which 14 languages were tested? List them all.\n3. The EXACT mechanism for extracting the refusal direction - how was it computed? Which layers? What contrastive data pairs were used? Was it PCA, mean difference, or something else?\n4. Quantitative results: success rates, attack success rates for cross-lingual transfer\n5. Any limitations on cross-language-family transfer (e.g., did some language families transfer worse?)\n6. Any discussion of why the direction is universal - what causes this parallelism?\n7. Details about the PolyRefuse dataset - how many prompts, how translated\n8. Any comparison to other methods like abliteration\n9. What layers were most effective?\n10. Any caveats or failure modes mentioned"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ec51e44-1c34-4dd2-b00a-ee1f97160ac6",
  "isSidechain": true,
  "agentId": "ae15bcf2ece33be45",
  "requestId": "req_011CbBfwpCMfR84GicUYpLGj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "672a2c50-31a8-4a6a-8c67-8ce6f193d06c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gi8NumaJk95ab7taGeC8jm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2153,
      "cache_read_input_tokens": 10481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2153,
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

_source line 18 · 2026-05-19T09:14:26.104Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ju27ckJrfRFcjb3rLzSgmm`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2502.15639",
  "prompt": "Extract key findings from this paper about cross-lingual alignment induced by model interventions in multilingual language models. What do they find about representation directions transferring across languages? What models and languages were tested? What interventions were studied?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "672a2c50-31a8-4a6a-8c67-8ce6f193d06c",
  "isSidechain": true,
  "agentId": "ae15bcf2ece33be45",
  "requestId": "req_011CbBfwpCMfR84GicUYpLGj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a6e9df8-533b-47dd-bccb-fd6ea658fd5d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gi8NumaJk95ab7taGeC8jm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2153,
      "cache_read_input_tokens": 10481,
      "output_tokens": 631,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2153
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 631,
          "cache_read_input_tokens": 10481,
          "cache_creation_input_tokens": 2153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2153,
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

_source line 19 · 2026-05-19T09:14:29.109Z_

<details><summary>↩ Tool result · reported error · `toolu_01Ju27ckJrfRFcjb3rLzSgmm`</summary>

```text
maxContentLength size of 10485760 exceeded
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a6e9df8-533b-47dd-bccb-fd6ea658fd5d",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "ae15bcf2ece33be45",
  "type": "user",
  "uuid": "f4a28a8e-ca16-4fb1-a122-490d43e4745f",
  "toolUseResult": "Error: maxContentLength size of 10485760 exceeded",
  "sourceToolAssistantUUID": "6a6e9df8-533b-47dd-bccb-fd6ea658fd5d",
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

_source line 20 · 2026-05-19T09:14:39.344Z_

<details><summary>↩ Tool result · `toolu_01Pd3rXpchsi8R46sNTMyogD`</summary>

```text
# Technical Details from "Refusal Direction is Universal Across Safety-Aligned Languages"

## 1. LLM Models Tested
- Llama3.1-8B-Instruct
- Llama-3 (various sizes)
- Qwen2.5-7B-Instruct
- Qwen2.5-14B-Instruct
- Gemma-2-9B-Instruct
- Yi (multiple sizes)

## 2. The 14 Languages
German (de), Spanish (es), French (fr), Italian (it), Dutch (nl), Japanese (ja), Polish (pl), Russian (ru), Chinese (zh), Korean (ko), Arabic (ar), Thai (th), Yoruba (yo), and English (en).

## 3. Refusal Direction Extraction Mechanism
The authors employed "difference-in-means" methodology. Specifically: "the extraction method computes mean activation differences between harmful prompt contexts 𝒟harmful and benign prompt contexts 𝒟harmless at specific layer ll and token position ii." The formula is:

**𝐫i,l = 𝐯i,lharmful − 𝐯i,lharmless**

They computed this across all Transformer layers at final instruction token positions (e.g., "[/INST]" for Llama2). The most effective vector was selected by measuring "reduction in refusal behavior after ablating each candidate" using a refusal score based on token probabilities.

## 4. Quantitative Results: Cross-Lingual Transfer Success
- English refusal vectors achieved "substantial increase in harmful compliance across all evaluated models and safety-aligned languages"
- Ablating non-English derived vectors resulted in "near-complete collapse of refusal behavior across all other safety-aligned languages, with compliance rates consistently approaching or exceeding 90%"
- Vector addition decreased compliance across languages, with "most languages achieving 0% compliance" in most cases
- Yoruba showed significantly higher baseline compliance (56.6%-82.9%) before interventions

## 5. Language Family Transfer Patterns
The paper demonstrates transfer worked across "language and script boundaries" without family-specific degradation. However, Yoruba (Niger-Congo family) exhibited substantially different behavior—classified as "safety-misaligned"—showing the universality applies only to "safety-aligned languages."

## 6. Mechanism for Universality
The authors identified parallel geometric structure: "refusal vectors are approximately parallel across languages" in the embedding space. Visualizations showed "consistently high cross-lingual similarity" in refusal direction heatmaps. However, they noted critical vulnerability: "harmful and harmless samples form clearly separated clusters in English, [but] the separation is substantially less distinct in non-English languages."

Quantitatively, Silhouette Scores showed English consistently higher (0.3063-0.4960) versus other languages (0.1958-0.3165).

## 7. PolyRefuse Dataset Details
- **Size**: 128 harmful + 128 harmless samples per language for training; 32 for validation; 572 for testing
- **Translation method**: Google Translate
- **Source data**: Harmful prompts from "Advbench, MaliciousInstruct, and TDC2023"; harmless from "Alpaca"
- **Quality control**: Samples with negative refusal scores removed; translation quality validated through back-translation

## 8. Comparison to Other Methods
The paper does not compare to "abliteration" or other competing approaches. The authors acknowledge they "do not evaluate concrete defense strategies," though they suggest "methods that enhance separation of harmful and harmless content" as future work.

## 9. Most Effective Layers
Layer 12 showed "consistent peak" similarity in Llama3.1-8B-Instruct heatmaps. However, the paper states ablation requires "across all layers" while addition works at "only a single layer."

## 10. Caveats and Failure Modes
- Analysis limited to 14 languages; findings "may not extend to languages with extremely limited data"
- Refusal transferability applies only to "safety-aligned languages"; misaligned languages like Yoruba showed persistent high compliance
- "Identical refusal directions across languages alone are not sufficient for ensuring robust multilingual refusal"
- Jailbroken samples "lie in the intermediate region between harmful and harmless clusters, indicating... the model struggles to decisively classify them"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "672a2c50-31a8-4a6a-8c67-8ce6f193d06c",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "ae15bcf2ece33be45",
  "type": "user",
  "uuid": "6ecb5742-f87a-41b9-b9cb-f7e6213b0fed",
  "sourceToolAssistantUUID": "672a2c50-31a8-4a6a-8c67-8ce6f193d06c",
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

_source line 21 · 2026-05-19T09:14:42.926Z_

Excellent, that gave rich detail. Let me now fetch the steering paper abstract and one more related paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ecb5742-f87a-41b9-b9cb-f7e6213b0fed",
  "isSidechain": true,
  "agentId": "ae15bcf2ece33be45",
  "requestId": "req_011CbBfygTaNYLKVHfUfkYkS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1350fa1e-6a38-4652-8537-0f269f0ba667",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AFKHt95tKhULPUaUS55n9Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 43,
      "cache_creation_input_tokens": 2000,
      "cache_read_input_tokens": 12634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2000,
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

_source line 22 · 2026-05-19T09:14:44.335Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YWb8S5HVuj7DPPtMyHmP1n`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.15639",
  "prompt": "Extract key findings: What do they find about cross-lingual alignment from model interventions? Do representation directions transfer across languages? What models and languages tested? What interventions were studied? Any findings about universal directions in multilingual LLMs?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1350fa1e-6a38-4652-8537-0f269f0ba667",
  "isSidechain": true,
  "agentId": "ae15bcf2ece33be45",
  "requestId": "req_011CbBfygTaNYLKVHfUfkYkS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc939eff-083f-4c2b-9797-b7240febc448",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AFKHt95tKhULPUaUS55n9Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 43,
      "cache_creation_input_tokens": 2000,
      "cache_read_input_tokens": 12634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2000,
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

_source line 23 · 2026-05-19T09:14:45.225Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ac8qyxc8kiT28xSGcSbBcs`</summary>

```json
{
  "url": "https://arxiv.org/abs/2503.11280",
  "prompt": "Extract key findings about high-dimensional interlingual representations in LLMs. Do they find universal representations across languages? What is their evidence? How does this relate to shared directions in representation space?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc939eff-083f-4c2b-9797-b7240febc448",
  "isSidechain": true,
  "agentId": "ae15bcf2ece33be45",
  "requestId": "req_011CbBfygTaNYLKVHfUfkYkS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8d3000b-6fab-4366-ae5c-9d8838e1e852",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AFKHt95tKhULPUaUS55n9Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 43,
      "cache_creation_input_tokens": 2000,
      "cache_read_input_tokens": 12634,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2000
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 43,
          "output_tokens": 260,
          "cache_read_input_tokens": 12634,
          "cache_creation_input_tokens": 2000,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2000,
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

_source line 24 · 2026-05-19T09:14:48.970Z_

<details><summary>↩ Tool result · `toolu_01YWb8S5HVuj7DPPtMyHmP1n`</summary>

```text
# Key Findings from arXiv:2502.15639

## Cross-Lingual Alignment from Model Interventions

The research demonstrates that model interventions can enhance cross-lingual alignment without costly fine-tuning. The abstract states: "modifying the mLLM's activations changes its embedding space such that cross-lingual alignment is enhanced."

## Performance Improvements

The intervention approach achieved substantial gains on retrieval tasks, with "up to 2x improvements in top-1 accuracy on cross-lingual retrieval," showing that embedding space modifications translate to practical performance benefits.

## Methodology

The study focuses on the "finding experts" intervention technique, which identifies and manipulates specific neurons for targeted languages. Researchers conducted introspection of embedding spaces before and after manipulation.

## Data Efficiency

A key advantage highlighted is the data-efficient nature of this approach: "A data-efficient alternative to fine-tuning is model interventions -- a method for manipulating model activations to steer generation into the desired direction."

## Limitations of Available Content

The webpage excerpt does not provide details about:
- Specific models tested (multilingual LLMs mentioned but not named)
- Languages included in experiments
- Whether representation directions transfer across languages
- Evidence regarding universal directional patterns in multilingual systems

These details would require accessing the full PDF paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc939eff-083f-4c2b-9797-b7240febc448",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "ae15bcf2ece33be45",
  "type": "user",
  "uuid": "d59f1d5f-5b73-49c0-93b2-d2ed20c11ea2",
  "sourceToolAssistantUUID": "cc939eff-083f-4c2b-9797-b7240febc448",
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

_source line 25 · 2026-05-19T09:14:50.233Z_

<details><summary>↩ Tool result · `toolu_01Ac8qyxc8kiT28xSGcSbBcs`</summary>

```text
# Key Findings on Interlingual Representations in LLMs

## Universal Representations: Mixed Evidence

The research finds that multilingual LLMs do **not** develop truly universal representations. The authors state: "multilingual LLMs exhibit inconsistent cross-lingual alignments" and that models present "partially aligned constructs" rather than unified representations.

## Evidence of Fragmentation

The study examined 31 languages across varying resource levels, typologies, and regions. Their key insight reveals that while some shared semantic subspace exists, representational limitations create fragmented components. As they note, interlingual alignment involves "shared interlingual semantic subspace and fragmented components, existed due to representational limitations."

## Measuring Alignment Through Local Structure

Rather than assuming universal directions exist, the researchers introduced the **Interlingual Local Overlap (ILO) score**—a metric quantifying alignment by "comparing the local neighborhood structures of high-dimensional representations." This neighborhood-based approach suggests alignment exists at a local rather than global level.

## Practical Implications

Their findings show that "training exclusively on a single language disrupts the alignment in early layers," while preserving early layers maintains cross-lingual generalization. This indicates interlingual alignment operates as a layer-specific property rather than a universal directional phenomenon throughout the network.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8d3000b-6fab-4366-ae5c-9d8838e1e852",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "ae15bcf2ece33be45",
  "type": "user",
  "uuid": "82c3e227-32a7-4717-98ab-e81161238f59",
  "sourceToolAssistantUUID": "e8d3000b-6fab-4366-ae5c-9d8838e1e852",
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

_source line 26 · 2026-05-19T09:15:32.558Z_

Now I have comprehensive information. Here is the detailed report:

---

## Detailed Report: Cross-Lingual Universality of Representation Directions in LLMs

### What arXiv 2505.17306 Shows

Wang et al. (2025, revised Feb 2026; published at NeurIPS 2025) demonstrate that the **refusal direction** -- the linear direction in activation space that distinguishes refusal from compliance behavior -- is approximately parallel across all safety-aligned languages in a model's representation space. The core claim is striking: a single refusal vector extracted from English activations alone can bypass safety refusals in 13 other languages with near-perfect effectiveness, requiring zero additional fine-tuning.

**Languages tested (14):** English, German, Spanish, French, Italian, Dutch, Japanese, Polish, Russian, Chinese, Korean, Arabic, Thai, and Yoruba -- spanning Indo-European, Japonic, Sino-Tibetan, Koreanic, Afro-Asiatic, Tai-Kadai, and Niger-Congo families.

**Models tested:** Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct, Qwen2.5-14B-Instruct, Gemma-2-9B-Instruct, and Yi models of multiple sizes.

**Direction extraction mechanism:** They use a **difference-in-means** approach. Given contrastive datasets of harmful prompts (from AdvBench, MaliciousInstruct, TDC2023) and harmless prompts (from Alpaca), they compute at each Transformer layer *l* and the final instruction token position *i*: **r_{i,l} = mean(v_{harmful}) - mean(v_{harmless})**. They compute this across all layers, then select the most effective vector by measuring which candidate produces the largest reduction in refusal behavior when ablated. The PolyRefuse dataset provided 128 harmful + 128 harmless samples per language (translated via Google Translate, quality-validated through back-translation). Layer 12 in Llama-3.1-8B showed peak cross-lingual similarity.

**Transfer effectiveness:** Ablating (removing) a refusal vector derived from any single safety-aligned language caused near-complete collapse of refusal across all other safety-aligned languages, with compliance rates consistently approaching or exceeding 90%. Adding the refusal direction suppressed harmful compliance, with most languages reaching 0% compliance. Cross-lingual cosine similarity heatmaps showed consistently high parallelism across language pairs.

### Key Caveats and Limitations

1. **Safety-aligned languages only.** The universality holds only for languages the model was safety-trained on. Yoruba, which was safety-misaligned in most tested models, showed dramatically different behavior (56-83% baseline compliance even before intervention). This is critical: the shared direction is an artifact of shared safety training, not an inherent property of multilingual representations.

2. **Weaker separation in non-English languages.** While refusal directions are parallel, the *separability* of harmful vs. harmless clusters is substantially weaker in non-English languages (Silhouette Scores: English 0.31-0.50 vs. non-English 0.20-0.32). Jailbroken samples land in an intermediate zone where the model cannot decisively classify them.

3. **Limited language coverage.** Only 14 languages were tested. The authors explicitly caution that findings "may not extend to languages with extremely limited data."

4. **No defense evaluation.** The paper does not evaluate concrete defense strategies against cross-lingual direction transfer.

5. **Translation-based dataset.** PolyRefuse uses Google Translate, which may not capture culturally specific harmful content or natural phrasing in all languages.

### Broader Evidence: Is This Universal?

The evidence is **convergent but incomplete**:

- **Supporting:** The Steering into New Embedding Spaces paper (arXiv 2502.15639, Pham et al.) shows that model interventions -- manipulating activations along specific directions -- enhance cross-lingual alignment with up to 2x improvement on retrieval tasks, confirming that directional manipulations in activation space have cross-lingual effects.

- **Supporting:** Middle-Layer Representation Alignment work (Liu & Niehues, ACL 2025) finds that middle layers exhibit the strongest potential for cross-lingual alignment, and cross-lingual word embeddings exhibit isometric relationships where geometric structure is preserved across languages.

- **Complicating:** The High-Dimensional Interlingual Representations study (arXiv 2503.11280) examining 31 languages finds that multilingual LLMs exhibit **inconsistent** cross-lingual alignments -- presenting "partially aligned constructs" rather than a unified universal space. Alignment is local and layer-specific, not globally uniform. Training on a single language disrupts alignment in early layers.

- **Complicating:** The ICLR 2026 submission "Rethinking Alignment in Cross-Lingual Knowledge Transfer" highlights persistent performance gaps between dominant languages (English) and non-dominant languages (e.g., Turkish), suggesting the "universality" is asymmetric and English-centric.

### Relevance to Calibration Transfer (vs. Refusal)

This is the most important caveat for your paper. The Wang et al. result concerns **refusal** -- a binary safety behavior that is explicitly trained into models via RLHF/DPO across languages simultaneously. Calibration (the alignment between predicted confidence and actual accuracy) is a more nuanced, continuous property that is not explicitly trained. The analogy is suggestive but not direct:

- **For your argument:** If safety-alignment training produces parallel linear directions across languages, it is plausible that other trained behaviors (including the implicit calibration patterns learned during instruction tuning) also develop shared directional structure. The difference-in-means methodology is the same one used in representation engineering for concepts like truthfulness and confidence.

- **Against over-claiming:** Refusal is a deliberately trained, high-salience behavior with explicit multilingual training signal. Calibration is emergent and much less likely to have been uniformly optimized across languages. The finding that non-English languages already have weaker cluster separation for refusal suggests calibration directions may be even more fragile cross-lingually. Furthermore, the interlingual representation work shows alignment is partial and layer-specific, not globally universal.

**Recommendation for citation:** Cite Wang et al. as evidence that *some* behaviorally meaningful linear directions transfer cross-lingually, supporting the plausibility of calibration direction transfer, but note the key disanalogy: refusal is explicitly trained while calibration is emergent, and even for refusal, non-English separation is weaker.

---

### Sources

- [Refusal Direction is Universal Across Safety-Aligned Languages (arXiv 2505.17306)](https://arxiv.org/abs/2505.17306)
- [Refusal Direction -- OpenReview / NeurIPS 2025](https://openreview.net/forum?id=eWxKpdAdXH)
- [Steering into New Embedding Spaces: Cross-Lingual Alignment from Model Interventions (arXiv 2502.15639)](https://arxiv.org/abs/2502.15639)
- [High-Dimensional Interlingual Representations of LLMs (arXiv 2503.11280)](https://arxiv.org/abs/2503.11280)
- [Middle-Layer Representation Alignment for Cross-Lingual Transfer (ACL 2025)](https://aclanthology.org/2025.acl-long.778/)
- [LUSIFER: Language Universal Space Integration (arXiv 2501.00874)](https://arxiv.org/html/2501.00874)
- [Rethinking Alignment in Cross-Lingual Knowledge Transfer (ICLR 2026 submission)](https://openreview.net/forum?id=nId47dxIr2)
- [Language Steering for Multilingual In-Context Learning (arXiv 2602.02326)](https://arxiv.org/pdf/2602.02326)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82c3e227-32a7-4717-98ab-e81161238f59",
  "isSidechain": true,
  "agentId": "ae15bcf2ece33be45",
  "requestId": "req_011CbBfzVGQVXescL9eXGkkz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4728c597-ce1d-4cc2-a10d-be6888133908",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015LZ62uqMWX49gQqxZ2XNdH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 943,
      "cache_read_input_tokens": 14634,
      "output_tokens": 1906,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 943
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1906,
          "cache_read_input_tokens": 14634,
          "cache_creation_input_tokens": 943,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 943,
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
