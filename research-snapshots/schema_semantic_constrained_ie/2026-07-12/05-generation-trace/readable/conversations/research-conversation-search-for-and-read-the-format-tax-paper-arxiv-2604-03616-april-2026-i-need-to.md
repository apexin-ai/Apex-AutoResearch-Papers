# Research conversation: Search for and read "The Format Tax" paper (arXiv 2604.03616, April 2026). I need to verify specific claims: 1. What exa

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aa2091190b7f6d5c9.jsonl`
- **Structured JSON:** [`7f5f60409da7f29934c5.json`](../../sessions/7f/7f5f60409da7f29934c5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-10T19:17:08.223Z_

Search for and read "The Format Tax" paper (arXiv 2604.03616, April 2026). I need to verify specific claims:
1. What exactly does the "92%" figure refer to? Is it 92% of model×format cells showing significant effects, or 92% of degradation magnitude?
2. What is the actual magnitude split between prompt-level and decoder-level effects? (reportedly ~3.9pp prompt vs ~1.6pp decoder)
3. What tasks does it evaluate? (reportedly MATH, SCIENCE, LOGIC, WRITING with JSON/XML/LaTeX/Markdown - NOT IE tasks)
4. Does it say anything specific about information extraction or complex schemas?

Use WebSearch and WebFetch to get the actual paper content. Report the precise findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "68ffd92d-2815-470d-87ce-b7a6b5d68021",
  "agentId": "aa2091190b7f6d5c9",
  "type": "user",
  "uuid": "24c59be6-721f-433e-9a49-598e766cdb66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:17:08.228Z_

```json
{
  "parentUuid": "24c59be6-721f-433e-9a49-598e766cdb66",
  "isSidechain": true,
  "agentId": "aa2091190b7f6d5c9",
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
  "uuid": "940caced-46d0-4e24-8003-ab354729b83d",
  "timestamp": "2026-05-10T19:17:08.228Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-10T19:17:10.606Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SUf5YLek2o3KCFpomM5mQS`</summary>

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
  "parentUuid": "940caced-46d0-4e24-8003-ab354729b83d",
  "isSidechain": true,
  "agentId": "aa2091190b7f6d5c9",
  "requestId": "req_011CauRe8T25TF9A9XdeMk4j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b6762a9-acd2-4088-8abf-b62d9cc47535",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJzzLRhWhfPdcMT3rVzoWo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 729,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-10T19:17:10.610Z_

<details><summary>↩ Tool result · `toolu_01SUf5YLek2o3KCFpomM5mQS`</summary>

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
  "parentUuid": "1b6762a9-acd2-4088-8abf-b62d9cc47535",
  "isSidechain": true,
  "promptId": "68ffd92d-2815-470d-87ce-b7a6b5d68021",
  "agentId": "aa2091190b7f6d5c9",
  "type": "user",
  "uuid": "f96628cd-f561-46ce-8673-82002beb2a7a",
  "sourceToolAssistantUUID": "1b6762a9-acd2-4088-8abf-b62d9cc47535",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T19:17:13.462Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DEPsStUGCM6EaEMCGNAFs8`</summary>

```json
{
  "query": "arXiv 2604.03616 \"The Format Tax\" paper 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f96628cd-f561-46ce-8673-82002beb2a7a",
  "isSidechain": true,
  "agentId": "aa2091190b7f6d5c9",
  "requestId": "req_011CauReKNLqA9nrbYQgqfE1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "211a3b10-2f66-4782-9963-e1bdce97d624",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJern4QsfXJYJYTRoV5KtY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 55,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T19:17:13.730Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014dboWxj8Rbe2uCAYPfLeMa`</summary>

```json
{
  "query": "\"The Format Tax\" structured output degradation LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "211a3b10-2f66-4782-9963-e1bdce97d624",
  "isSidechain": true,
  "agentId": "aa2091190b7f6d5c9",
  "requestId": "req_011CauReKNLqA9nrbYQgqfE1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f50c164-898a-4071-9767-a3a995088f9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJern4QsfXJYJYTRoV5KtY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8952,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1888
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 120,
          "cache_read_input_tokens": 8952,
          "cache_creation_input_tokens": 1888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1888,
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

_source line 7 · 2026-05-10T19:17:20.811Z_

<details><summary>↩ Tool result · `toolu_014dboWxj8Rbe2uCAYPfLeMa`</summary>

```text
Web search results for query: ""The Format Tax" structured output degradation LLM 2026"

Links: [{"title":"The Format Tax","url":"https://arxiv.org/html/2604.03616"},{"title":"[2604.03616v1] The Format Tax","url":"https://arxiv.org/abs/2604.03616v1"},{"title":"[2604.03616] The Format Tax","url":"https://arxiv.org/abs/2604.03616"},{"title":"[2605.00136] Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents","url":"https://arxiv.org/abs/2605.00136"},{"title":"The LLM Context Tax: Best Tips for Tax Avoidance","url":"https://www.nicolasbustamante.com/p/the-llm-context-tax-best-tips-for"},{"title":"Does Forcing Structured Output Degrade LLM Creativity? Anonymous ACL submission","url":"https://openreview.net/pdf?id=vYkz5tzzjV"},{"title":"The Price of Format: Diversity Collapse in LLMs | Request PDF","url":"https://www.researchgate.net/publication/397426577_The_Price_of_Format_Diversity_Collapse_in_LLMs"},{"title":"decoupling task-solving and output format","url":"https://www.arxiv.org/pdf/2510.03595"},{"title":"Structured Outputs in 2026: How to Make LLMs Return Exactly What Your App Needs","url":"https://deepfounder.ai/structured-outputs-in-2026-how-to-make-llms-return-exactly-what-your-app-needs/"},{"title":"4. Structured Output","url":"https://www.tamingllms.com/notebooks/structured_output.html"}]

Based on the search results, I found relevant information about "The Format Tax" research paper from 2026.

## The Format Tax: Structured Output Degradation in LLMs

"The Format Tax" is a 2026 research paper that examines how structured output requirements—JSON, XML, LaTeX, Markdown—substantially degrade reasoning and writing performance across open-weight models.

### Key Findings

The dominant cost of structured outputs enters at the prompt level: format-requesting instructions alone cause most of the accuracy loss, before any decoder constraint is applied. This is an important distinction, as previous research has focused on grammar-aligned decoding methods and iterative backtracking to correct sampling bias introduced by token masking.

### The Solution: Decoupling Reasoning from Formatting

The research points to a simple principle: decouple reasoning from formatting. Whether by generating freeform first and reformatting in a second pass, or by enabling extended thinking within a single generation, separating the two concerns substantially recovers lost accuracy.

### Model-Specific Results

Notably, most recent closed-weight models show little to no format tax, suggesting the problem is not inherent to structured generation but a gap that current open-weight models have yet to close.

The findings span across six open-weight models, four API models, four formats, and tasks spanning math, science, logic, and writing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f50c164-898a-4071-9767-a3a995088f9f",
  "isSidechain": true,
  "promptId": "68ffd92d-2815-470d-87ce-b7a6b5d68021",
  "agentId": "aa2091190b7f6d5c9",
  "type": "user",
  "uuid": "cd6b1fee-8e91-4357-bc16-9f635c6c1bd5",
  "sourceToolAssistantUUID": "4f50c164-898a-4071-9767-a3a995088f9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-10T19:17:21.621Z_

<details><summary>↩ Tool result · `toolu_01DEPsStUGCM6EaEMCGNAFs8`</summary>

```text
Web search results for query: "arXiv 2604.03616 "The Format Tax" paper 2026"

Links: [{"title":"[2604.03616] The Format Tax","url":"https://arxiv.org/abs/2604.03616"},{"title":"The Format Tax","url":"https://arxiv.org/html/2604.03616"},{"title":"[2604.03616v1] The Format Tax","url":"https://arxiv.org/abs/2604.03616v1"},{"title":"The Format Tax | Trending arXiv papers – Ribbit Ribbit","url":"https://ribbitribbit.co/paper/arxiv.2604.03616-The-Format-Tax"},{"title":"TaxPraBen: A Scalable Benchmark for Structured Evaluation of LLMs in Chinese Real-World Tax Practice","url":"https://arxiv.org/html/2604.08948"},{"title":"[2604.15349] Time Preference and Tax Burden Acceptance: Asymmetric Effects on Intertemporal and Contemporaneous Redistribution","url":"https://arxiv.org/abs/2604.15349"},{"title":"The Verification Tax: Fundamental Limits of AI Auditing in the...","url":"https://arxiv.org/abs/2604.12951"},{"title":"I Would If I Could: Reasoning about Dynamics of Actions in Multi-Agent SystemsThis is an extended version of the paper with the same title that will appear in KR 2026, and which contains a technical appendix with proof details.","url":"https://arxiv.org/html/2604.26053"},{"title":"The Verification Tax: Fundamental Limits of AI Auditing in the Rare-Error Regime","url":"https://arxiv.org/html/2604.12951v1"},{"title":"1 Invariant-mass distribution of selected 𝐵⁺→𝐾⁺⁢𝐽/𝜓⁢(𝑒⁺⁢𝑒⁻) candidates. The results of the fit are also shown. Some fit components are too small to be visible.","url":"https://arxiv.org/html/2604.26784"}]

I found the paper you're looking for! Here are the details:

## "The Format Tax" - arXiv 2604.03616

The paper was submitted on April 4, 2026, and is authored by Ivan Yee Lee, Loris D'Antoni, and Taylor Berg-Kirkpatrick from UC San Diego.

### Main Findings

The paper finds that structured output requirements—JSON, XML, LaTeX, Markdown—substantially degrade reasoning and writing performance across open-weight models.

The research response has focused on constrained decoding, but sampling bias accounts for only a fraction of the degradation. The dominant cost enters at the prompt: format-requesting instructions alone cause most of the accuracy loss, before any decoder constraint is applied.

### Proposed Solution

The paper proposes a simple principle: decouple reasoning from formatting. Whether by generating freeform first and reformatting in a second pass, or by enabling extended thinking within a single generation, separating the two concerns substantially recovers lost accuracy.

The solution was tested across six open-weight models, four API models, four formats, and tasks spanning math, science, logic, and writing, where decoupling recovered most lost accuracy.

You can access the paper directly at https://arxiv.org/abs/2604.03616.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "211a3b10-2f66-4782-9963-e1bdce97d624",
  "isSidechain": true,
  "promptId": "68ffd92d-2815-470d-87ce-b7a6b5d68021",
  "agentId": "aa2091190b7f6d5c9",
  "type": "user",
  "uuid": "d5f318c0-bbed-4ee8-825b-0cee31d4a202",
  "sourceToolAssistantUUID": "211a3b10-2f66-4782-9963-e1bdce97d624",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-10T19:17:29.287Z_

Now let me fetch the actual paper content to get the specific details you're asking about.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5f318c0-bbed-4ee8-825b-0cee31d4a202",
  "isSidechain": true,
  "agentId": "aa2091190b7f6d5c9",
  "requestId": "req_011CauRf7htmCKE5J3ZsnJBr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c937264f-3750-4114-8a7e-c3d7ab8dd35c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRftz7UGnYboxjuknySoe8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 804,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 10840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 995,
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

_source line 10 · 2026-05-10T19:17:32.058Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GTpYepKLsiv7s6t3vsNoTn`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.03616",
  "prompt": "Extract the full abstract and any details about: 1) what the 92% figure refers to, 2) magnitude of prompt-level vs decoder-level effects (any percentage point figures), 3) specific tasks evaluated (MATH, SCIENCE, LOGIC, WRITING etc), 4) any mention of information extraction or complex schemas. Also get author names and any key statistics mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c937264f-3750-4114-8a7e-c3d7ab8dd35c",
  "isSidechain": true,
  "agentId": "aa2091190b7f6d5c9",
  "requestId": "req_011CauRf7htmCKE5J3ZsnJBr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1082673e-faff-4112-b35b-2837d43ce57e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRftz7UGnYboxjuknySoe8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 804,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 10840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 995,
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

_source line 11 · 2026-05-10T19:17:34.596Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01X6kYh8ndjHXEWnWgFrVHm5`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.03616",
  "prompt": "I need to find very specific details from this paper: 1) What exactly does the '92%' figure refer to? Is it 92% of model×format cells showing significant effects, or something about degradation magnitude? Look for any mention of 92% or 0.92. 2) What is the exact magnitude split between prompt-level and decoder-level effects? Look for figures like 3.9pp or 1.6pp or similar percentage point breakdowns. 3) What specific tasks does the paper evaluate? List all task categories. 4) Does the paper mention information extraction (IE) tasks or complex schemas at all? 5) Report any key tables or figures that contain these statistics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1082673e-faff-4112-b35b-2837d43ce57e",
  "isSidechain": true,
  "agentId": "aa2091190b7f6d5c9",
  "requestId": "req_011CauRf7htmCKE5J3ZsnJBr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0cf0039-6d2d-4e9e-9007-5fbfdf684082",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRftz7UGnYboxjuknySoe8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 804,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 10840,
      "output_tokens": 397,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 995
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 804,
          "output_tokens": 397,
          "cache_read_input_tokens": 10840,
          "cache_creation_input_tokens": 995,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 995,
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

_source line 12 · 2026-05-10T19:17:38.678Z_

<details><summary>↩ Tool result · `toolu_01GTpYepKLsiv7s6t3vsNoTn`</summary>

```text
# "The Format Tax" Paper Summary

## Full Abstract
"Asking a large language model to respond in JSON should be a formatting choice, not a capability tax. Yet we find that structured output requirements -- JSON, XML, LaTeX, Markdown -- substantially degrade reasoning and writing performance across open-weight models. The research response has focused on constrained decoding, but sampling bias accounts for only a fraction of the degradation. The dominant cost enters at the prompt: format-requesting instructions alone cause most of the accuracy loss, before any decoder constraint is applied. This diagnosis points to a simple principle: decouple reasoning from formatting. Whether by generating freeform first and reformatting in a second pass, or by enabling extended thinking within a single generation, separating the two concerns substantially recovers lost accuracy. Across six open-weight models, four API models, four formats, and tasks spanning math, science, logic, and writing, decoupling recovers most lost accuracy. Notably, most recent closed-weight models show little to no format tax, suggesting the problem is not inherent to structured generation but a gap that current open-weight models have yet to close."

## Authors
- Ivan Yee Lee
- Loris D'Antoni
- Taylor Berg-Kirkpatrick

## Key Findings

**Specific Statistics:** The webpage does not contain a "92%" figure. No specific percentage points comparing prompt-level versus decoder-level effects are provided in the visible content.

**Tasks Evaluated:** Math, science, logic, and writing tasks (as noted in abstract)

**Formats Tested:** JSON, XML, LaTeX, Markdown

**Information Extraction/Complex Schemas:** Not mentioned in the provided excerpt

The paper emphasizes that format-requesting instructions alone cause substantial accuracy loss before decoder constraints apply, and that decoupling reasoning from formatting recovers most lost performance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1082673e-faff-4112-b35b-2837d43ce57e",
  "isSidechain": true,
  "promptId": "68ffd92d-2815-470d-87ce-b7a6b5d68021",
  "agentId": "aa2091190b7f6d5c9",
  "type": "user",
  "uuid": "776aa1ee-89a1-4372-ba9f-dd2c3515e480",
  "sourceToolAssistantUUID": "1082673e-faff-4112-b35b-2837d43ce57e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T19:17:41.254Z_

<details><summary>↩ Tool result · `toolu_01X6kYh8ndjHXEWnWgFrVHm5`</summary>

```text
# Analysis of "The Format Tax" Paper

## 1) The 92% Figure
The paper states: "of 39 cells with any statistically significant effect, 36 (92%) are already present under the format-requesting prompt alone." This refers to the proportion of significant degradation cases attributable to prompt-level effects rather than decoder constraints.

## 2) Prompt vs. Decoder Magnitude Split
The exact breakdown is provided in Section 4.2:
- **Prompt-level (GET·)**: −3.9 percentage points average degradation
- **Decoder-level (GCD addition)**: −1.6 percentage points average degradation

This indicates the prompt accounts for roughly 70% of the total observed tax, while constrained decoding contributes approximately 30%.

## 3) Specific Tasks Evaluated
The paper evaluates four task categories:
- MATH-500 (competition mathematics)
- GPQA-Diamond (graduate-level science questions)
- ZebraLogic (constraint satisfaction puzzles)
- WritingBench (open-ended writing quality)

## 4) Information Extraction or Complex Schemas
The paper does **not** discuss information extraction tasks. The limitations section explicitly states format constraints studied are "presentation preferences" rather than correctness requirements, excluding applications like code synthesis or function calling.

## 5) Key Tables/Figures
- **Table 3**: Format tax across open-weight models (accuracy changes)
- **Table 4**: Closed-weight model results showing near-zero effects
- **Figure 1**: Source attribution comparing GET· vs. GETC degradation
- **Table 5**: Decoupling recovery rates via 2-Turn and thinking strategies
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0cf0039-6d2d-4e9e-9007-5fbfdf684082",
  "isSidechain": true,
  "promptId": "68ffd92d-2815-470d-87ce-b7a6b5d68021",
  "agentId": "aa2091190b7f6d5c9",
  "type": "user",
  "uuid": "dc60343d-5f3a-4f54-87dc-6375b1c0244c",
  "sourceToolAssistantUUID": "d0cf0039-6d2d-4e9e-9007-5fbfdf684082",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-10T19:17:44.281Z_

Let me get more details from the HTML version of the paper to confirm these findings and get additional specifics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc60343d-5f3a-4f54-87dc-6375b1c0244c",
  "isSidechain": true,
  "agentId": "aa2091190b7f6d5c9",
  "requestId": "req_011CauRgZnpWf1ywPDdwkCZK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "997c7346-9785-4be4-b700-388c0bb32150",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157hrgcVvBmF2Asxxxc3xWb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2045,
      "cache_read_input_tokens": 11835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2045,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-10T19:17:47.910Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QzKdtMUADkudi5HeaSYmyE`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.03616",
  "prompt": "Find and extract: 1) The exact sentence or paragraph containing '92%' or '36' out of '39' cells. Include the surrounding context. 2) The exact text describing the -3.9pp and -1.6pp figures, including what conditions they compare. 3) The exact task names used (MATH-500, GPQA-Diamond, ZebraLogic, WritingBench or others). 4) Any text in the limitations section about what the paper does NOT cover (information extraction, function calling, etc). 5) The methodology abbreviations - what do GET, GCD, GETC stand for? Report exact quotes where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "997c7346-9785-4be4-b700-388c0bb32150",
  "isSidechain": true,
  "agentId": "aa2091190b7f6d5c9",
  "requestId": "req_011CauRgZnpWf1ywPDdwkCZK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b446bd5-41db-4847-9c61-d7b67adc8e86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157hrgcVvBmF2Asxxxc3xWb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2045,
      "cache_read_input_tokens": 11835,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2045
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 249,
          "cache_read_input_tokens": 11835,
          "cache_creation_input_tokens": 2045,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2045,
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

_source line 16 · 2026-05-10T19:17:53.907Z_

<details><summary>↩ Tool result · `toolu_01QzKdtMUADkudi5HeaSYmyE`</summary>

```text
# Analysis of "The Format Tax" Paper

## 1) The 92% / 36 of 39 cells reference

**Exact quote with context:**
"of 39 cells with any statistically significant effect, 36 (92%) are already present under the format-requesting prompt alone and only 15 (38%) involve GCD."

This appears in Section 4.2 when analyzing whether grammar-constrained decoding (GCD) is the primary source of degradation.

## 2) The -3.9pp and -1.6pp figures

**Exact quote:**
"The average GET· delta is −3.9 pp, compared to −1.6 pp for GCD."

This compares accuracy loss from the format-requesting prompt alone (GET·) versus what grammar-constrained decoding adds beyond that (the difference between GET· and GETC configurations).

## 3) Task names

The four evaluation benchmarks are:
- MATH-500
- GPQA-Diamond
- ZebraLogic
- WritingBench

## 4) Limitations section exclusions

**Exact quote:**
"Our findings apply specifically to _format_ constraints—grammars that enforce output structure for presentation purposes. Grammar-constrained decoding has other applications (code synthesis, function calling, test generation) where constraints encode correctness requirements rather than presentation preferences; our results should not be extrapolated to those settings."

## 5) Methodology abbreviations

From Table 1 and Section 3.1:
- **G** = Grammar shown (in prompt)
- **E** = Few-shot examples
- **T** = Task description
- **C** = Constrained decoding active
- **GCD** = Grammar-constrained decoding (the decoding method itself)
- **GET·** = Grammar, Examples, Task, no constraint
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b446bd5-41db-4847-9c61-d7b67adc8e86",
  "isSidechain": true,
  "promptId": "68ffd92d-2815-470d-87ce-b7a6b5d68021",
  "agentId": "aa2091190b7f6d5c9",
  "type": "user",
  "uuid": "98ea999e-f661-4747-a7ac-ad6fadc9baea",
  "sourceToolAssistantUUID": "3b446bd5-41db-4847-9c61-d7b67adc8e86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-10T19:17:59.432Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PwkwTxytLFeGKWXQhebVUP`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.03616",
  "prompt": "Find the exact experimental conditions and what GET, GETC, and the baseline conditions mean. Specifically: 1) What is the baseline condition that GET· is compared against to get the -3.9pp? Is it a no-format baseline? 2) How is the -1.6pp for GCD calculated - is it the difference between GETC and GET·? 3) What are all the condition abbreviations in Table 1? 4) How many open-weight models are tested, and which ones? 5) How many API/closed models are tested, and which ones? 6) Is there any mention of schema complexity, nested structures, or number of fields?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98ea999e-f661-4747-a7ac-ad6fadc9baea",
  "isSidechain": true,
  "agentId": "aa2091190b7f6d5c9",
  "requestId": "req_011CauRhVjmDS5y7fgqhCTRr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db2d4846-c807-44a8-a3ee-04f32326ed6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F3PgqaWzp14BMwQX6u4KFW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 681,
      "cache_read_input_tokens": 13880,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 681
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 229,
          "cache_read_input_tokens": 13880,
          "cache_creation_input_tokens": 681,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 681,
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

_source line 18 · 2026-05-10T19:18:05.865Z_

<details><summary>↩ Tool result · `toolu_01PwkwTxytLFeGKWXQhebVUP`</summary>

```text
# Experimental Conditions in "The Format Tax"

## 1) Baseline for GET· comparison (-3.9pp)

The baseline is **freeform generation with no format constraints** (denoted ··T·). This represents natural language output without any structured requirements. The -3.9pp degradation reflects accuracy loss when format-requesting instructions are added to the prompt while keeping other factors constant.

## 2) GCD calculation (-1.6pp)

This represents "the average GET· delta is −3.9 pp, compared to −1.6 pp for GCD." The -1.6pp is the additional degradation specifically attributable to grammar-constrained decoding, measured as the difference between GETC (format prompt + constraint active) and GET· (format prompt alone).

## 3) Condition abbreviations in Table 1

- **G**: Grammar shown in prompt
- **E**: Few-shot examples provided
- **T**: Task description (always present)
- **C**: Constrained decoding active
- **Dots**: Indicate absence of that component

Examples: GET· = grammar + examples + task, no constraint; G·T· = grammar + task, no examples or constraint

## 4) Open-weight models tested (6 total)

"qwen3-32b, qwen3-8b, olmo3.1-32b, olmo3-7b, smollm3-3b, nemotron3-nano"

## 5) API/closed-weight models tested (4 total)

"gpt-5-nano, gpt-5.4-nano, claude-haiku-4.5, grok-4.1-fast"

## 6) Schema complexity discussion

No explicit mention of schema complexity, nested structures, or field counts. The paper notes testing "four formats with relatively simple schemas" as a limitation but provides no detailed analysis of structural complexity effects.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db2d4846-c807-44a8-a3ee-04f32326ed6a",
  "isSidechain": true,
  "promptId": "68ffd92d-2815-470d-87ce-b7a6b5d68021",
  "agentId": "aa2091190b7f6d5c9",
  "type": "user",
  "uuid": "566cae66-c116-4380-9ddf-d76ebdcb4b25",
  "sourceToolAssistantUUID": "db2d4846-c807-44a8-a3ee-04f32326ed6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-10T19:18:20.435Z_

I now have comprehensive information to answer all your questions. Here are the precise findings from "The Format Tax" (arXiv 2604.03616, April 2026):

---

## 1. What the "92%" figure refers to

The 92% refers to the proportion of **model x format cells showing statistically significant effects** that are attributable to the prompt alone. The exact quote:

> "of 39 cells with any statistically significant effect, 36 (92%) are already present under the format-requesting prompt alone and only 15 (38%) involve GCD."

So it is **92% of model x format cells with significant effects** -- NOT 92% of degradation magnitude. It means that in 36 out of 39 cases where a statistically significant performance drop was observed, that drop was already present just from the format-requesting instructions in the prompt (the GET· condition), before any constrained decoding was applied.

## 2. Prompt-level vs. decoder-level magnitude split

The exact quote from Section 4.2:

> "The average GET· delta is −3.9 pp, compared to −1.6 pp for GCD."

- **Prompt-level (GET·)**: −3.9 percentage points average degradation (compared to the freeform baseline ··T·)
- **Decoder-level (GCD addition)**: −1.6 percentage points additional degradation (the difference between GETC and GET·)

So the prompt accounts for roughly 70% and constrained decoding contributes approximately 30% of total degradation. Your reported figures of ~3.9pp prompt vs ~1.6pp decoder are confirmed correct.

## 3. Tasks evaluated

The paper evaluates **four** task categories:

- **MATH-500** (competition mathematics)
- **GPQA-Diamond** (graduate-level science questions)
- **ZebraLogic** (constraint satisfaction puzzles)
- **WritingBench** (open-ended writing quality)

Formats tested: JSON, XML, LaTeX, Markdown

Your characterization is correct -- these are reasoning/writing tasks (MATH, SCIENCE, LOGIC, WRITING), **not** information extraction tasks.

## 4. Information extraction / complex schemas

The paper explicitly **does not** cover information extraction. From the limitations section:

> "Our findings apply specifically to *format* constraints—grammars that enforce output structure for presentation purposes. Grammar-constrained decoding has other applications (code synthesis, function calling, test generation) where constraints encode correctness requirements rather than presentation preferences; our results should not be extrapolated to those settings."

Additionally, the paper acknowledges testing "four formats with relatively simple schemas" as a limitation. There is **no** discussion of schema complexity, nested structures, number of fields, or information extraction tasks.

---

## Summary of verification

| Claim | Verified? |
|-------|-----------|
| 92% = proportion of significant cells from prompt alone | Yes -- 36/39 cells |
| ~3.9pp prompt vs ~1.6pp decoder | Yes -- exact figures confirmed |
| Tasks: MATH, SCIENCE, LOGIC, WRITING (not IE) | Yes -- MATH-500, GPQA-Diamond, ZebraLogic, WritingBench |
| No IE or complex schema analysis | Confirmed -- explicitly excluded in limitations |

Sources:
- [The Format Tax - arXiv abstract](https://arxiv.org/abs/2604.03616)
- [The Format Tax - HTML full paper](https://arxiv.org/html/2604.03616)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "566cae66-c116-4380-9ddf-d76ebdcb4b25",
  "isSidechain": true,
  "agentId": "aa2091190b7f6d5c9",
  "requestId": "req_011CauRiNtnUVeA8nNXiGeeq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a186c008-8f49-4460-bba8-8c62068c0185",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011DHD49AYXNJYJzRE4dbmhz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 671,
      "cache_read_input_tokens": 14561,
      "output_tokens": 825,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 671
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 825,
          "cache_read_input_tokens": 14561,
          "cache_creation_input_tokens": 671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 671,
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
