# Research conversation: Search for and verify the paper "The Format Tax" (arXiv 2604.03616, April 2026). The claim is that it shows 92% of forma

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a155484fa15f65f16.jsonl`
- **Structured JSON:** [`8d22264bd1375b32bccf.json`](../../sessions/8d/8d22264bd1375b32bccf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

14 recorded events

### User

_source line 1 · 2026-05-10T18:49:24.806Z_

Search for and verify the paper "The Format Tax" (arXiv 2604.03616, April 2026). The claim is that it shows 92% of format-induced accuracy degradation originates at the PROMPT LEVEL (from schema complexity in the prompt forcing the model to simultaneously reason about content and satisfy structural constraints), not from decoder-level grammar masking (which contributes only ~1.6 pp additional loss). 

Use WebSearch to find this paper and WebFetch to read its abstract and key findings. Report:
1. Does this paper exist?
2. Does it actually claim 92% prompt-level vs ~1.6pp decoder-level?
3. What tasks/benchmarks does it evaluate on?
4. Any caveats or limitations that would affect its applicability to information extraction?

Be concise in your report (under 300 words).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8ecf08e1-2116-4f25-b8d6-7ecf13c4de4d",
  "agentId": "a155484fa15f65f16",
  "type": "user",
  "uuid": "36431360-3f9a-413b-8a87-ece6ae0c1159",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:49:24.811Z_

```json
{
  "parentUuid": "36431360-3f9a-413b-8a87-ece6ae0c1159",
  "isSidechain": true,
  "agentId": "a155484fa15f65f16",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "e7d6799c-2abe-4365-a10d-ac3ab672b558",
  "timestamp": "2026-05-10T18:49:24.811Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:49:27.182Z_



I'll search for this paper. Let me first load the WebSearch and WebFetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7d6799c-2abe-4365-a10d-ac3ab672b558",
  "isSidechain": true,
  "agentId": "a155484fa15f65f16",
  "requestId": "req_011CauPXWcbAPhWdsrdENvmu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bcf98db6-1efb-4521-8511-205d773b943c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012bJ6apANVvRgSzQ44t2K41",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8017,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8017,
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

_source line 4 · 2026-05-10T18:49:27.349Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BFMcW542YTa6LJ38WWFCAe`</summary>

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
  "parentUuid": "bcf98db6-1efb-4521-8511-205d773b943c",
  "isSidechain": true,
  "agentId": "a155484fa15f65f16",
  "requestId": "req_011CauPXWcbAPhWdsrdENvmu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "535fc343-d8f0-427e-b5b8-5c2b717817a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012bJ6apANVvRgSzQ44t2K41",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8017,
      "cache_read_input_tokens": 0,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8017
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8017,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8017,
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

_source line 5 · 2026-05-10T18:49:27.353Z_

<details><summary>↩ Tool result · `toolu_01BFMcW542YTa6LJ38WWFCAe`</summary>

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
  "parentUuid": "535fc343-d8f0-427e-b5b8-5c2b717817a3",
  "isSidechain": true,
  "promptId": "8ecf08e1-2116-4f25-b8d6-7ecf13c4de4d",
  "agentId": "a155484fa15f65f16",
  "type": "user",
  "uuid": "5665a592-092f-4915-8f0c-c6ebbf2198d5",
  "sourceToolAssistantUUID": "535fc343-d8f0-427e-b5b8-5c2b717817a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T18:49:30.143Z_



Now let me search for the paper and fetch it from arXiv.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5665a592-092f-4915-8f0c-c6ebbf2198d5",
  "isSidechain": true,
  "agentId": "a155484fa15f65f16",
  "requestId": "req_011CauPXhuVZGfHBBJEuj9AU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6193afe-ec22-4065-a813-9144cbd0cee3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWuQQewf2Hnji1vduM6gt9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8017,
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

_source line 7 · 2026-05-10T18:49:31.061Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J5BmPNXywsTVDsNe2wNJhJ`</summary>

```json
{
  "query": "arXiv 2604.03616 \"The Format Tax\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6193afe-ec22-4065-a813-9144cbd0cee3",
  "isSidechain": true,
  "agentId": "a155484fa15f65f16",
  "requestId": "req_011CauPXhuVZGfHBBJEuj9AU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8cd01a56-b6fd-42d1-b791-167323adcbd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWuQQewf2Hnji1vduM6gt9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8017,
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

_source line 8 · 2026-05-10T18:49:33.221Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011wqeoov1fSxupwHDhLGbb3`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.03616",
  "prompt": "Extract the full abstract, author names, title, and any key findings or claims about prompt-level vs decoder-level accuracy degradation, percentages like 92% or 1.6pp, and what benchmarks/tasks were evaluated."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cd01a56-b6fd-42d1-b791-167323adcbd7",
  "isSidechain": true,
  "agentId": "a155484fa15f65f16",
  "requestId": "req_011CauPXhuVZGfHBBJEuj9AU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9aa04523-f425-4f4a-bfd9-5649e1499871",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWuQQewf2Hnji1vduM6gt9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8017,
      "output_tokens": 200,
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
          "output_tokens": 200,
          "cache_read_input_tokens": 8017,
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

_source line 9 · 2026-05-10T18:49:34.930Z_

<details><summary>↩ Tool result · `toolu_01J5BmPNXywsTVDsNe2wNJhJ`</summary>

```text
Web search results for query: "arXiv 2604.03616 "The Format Tax" 2026"

Links: [{"title":"[2604.03616] The Format Tax","url":"https://arxiv.org/abs/2604.03616"},{"title":"The Format Tax","url":"https://arxiv.org/html/2604.03616"},{"title":"[2604.03616v1] The Format Tax","url":"https://arxiv.org/abs/2604.03616v1"},{"title":"The Format Tax | Trending arXiv papers – Ribbit Ribbit","url":"https://ribbitribbit.co/paper/arxiv.2604.03616-The-Format-Tax"}]

I found the paper you're looking for. Here's what I found about arXiv paper 2604.03616:

**Title:** "The Format Tax"

**Authors:** Ivan Yee Lee, Loris D'Antoni, and Taylor Berg-Kirkpatrick from UC San Diego

**Submission Date:** April 4, 2026

**Main Findings:** 

The paper argues that asking a large language model to respond in JSON should be a formatting choice, not a capability tax, yet they find that structured output requirements like JSON, XML, LaTeX, and Markdown substantially degrade reasoning and writing performance across open-weight models.

The dominant cost enters at the prompt: format-requesting instructions alone cause most of the accuracy loss, before any decoder constraint is applied.

**Proposed Solution:** The paper suggests decoupling reasoning from formatting, either by generating freeform first and reformatting in a second pass, or by enabling extended thinking within a single generation, which substantially recovers lost accuracy.

The results are demonstrated across six open-weight models, four API models, four formats, and tasks spanning math, science, logic, and writing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8cd01a56-b6fd-42d1-b791-167323adcbd7",
  "isSidechain": true,
  "promptId": "8ecf08e1-2116-4f25-b8d6-7ecf13c4de4d",
  "agentId": "a155484fa15f65f16",
  "type": "user",
  "uuid": "65243b04-2c37-4df9-bfb9-809648686eb2",
  "sourceToolAssistantUUID": "8cd01a56-b6fd-42d1-b791-167323adcbd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T18:49:39.499Z_

<details><summary>↩ Tool result · `toolu_011wqeoov1fSxupwHDhLGbb3`</summary>

```text
# The Format Tax - Paper Summary

**Title:** The Format Tax

**Authors:** Ivan Yee Lee, Loris D'Antoni, Taylor Berg-Kirkpatrick

**Abstract:**
"Asking a large language model to respond in JSON should be a formatting choice, not a capability tax. Yet we find that structured output requirements -- JSON, XML, LaTeX, Markdown -- substantially degrade reasoning and writing performance across open-weight models."

The research identifies that format-requesting instructions in prompts cause the majority of accuracy loss before any decoder constraint applies. The authors propose decoupling reasoning from formatting through two-pass generation or extended thinking approaches.

**Key Findings:**

- **Prompt-level vs. decoder-level degradation:** Sampling bias accounts for only a fraction of performance decline; the dominant cost originates from format instructions in the prompt itself, before constrained decoding is applied.

- **Solution effectiveness:** Separating reasoning from formatting substantially recovers lost accuracy across evaluated models.

- **Model differences:** Most recent closed-weight models show minimal or no format tax, suggesting this is a capability gap in current open-weight models rather than an inherent limitation of structured generation.

**Evaluated Elements:** Six open-weight models, four API models, four formats (JSON, XML, LaTeX, Markdown), and tasks spanning mathematics, science, logic, and writing.

**Availability:** Code is available at the linked repository.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9aa04523-f425-4f4a-bfd9-5649e1499871",
  "isSidechain": true,
  "promptId": "8ecf08e1-2116-4f25-b8d6-7ecf13c4de4d",
  "agentId": "a155484fa15f65f16",
  "type": "user",
  "uuid": "977ee759-5114-49c4-9d25-c403a32b987e",
  "sourceToolAssistantUUID": "9aa04523-f425-4f4a-bfd9-5649e1499871",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-10T18:49:42.408Z_

The paper exists. Let me fetch more detail to verify the specific numerical claims (92%, 1.6pp).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "977ee759-5114-49c4-9d25-c403a32b987e",
  "isSidechain": true,
  "agentId": "a155484fa15f65f16",
  "requestId": "req_011CauPYbQ6sujxUpTCTVnpf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "368aa329-d42a-45bf-ae87-25f8b4be1281",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JrmNuyNMR8Zx3sXECnNRZF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1012,
      "cache_read_input_tokens": 9927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1012,
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

_source line 12 · 2026-05-10T18:49:44.443Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UKQjyZMuH8Rhe8dofmTQPu`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.03616",
  "prompt": "Find the specific numerical claims about what percentage of format-induced accuracy degradation originates at the prompt level vs the decoder level. Look for numbers like 92%, 1.6pp, or any decomposition of the accuracy loss between prompt-level and decoder-level sources. Also list all specific benchmarks and tasks evaluated. Also note any caveats or limitations mentioned, especially regarding information extraction tasks."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "368aa329-d42a-45bf-ae87-25f8b4be1281",
  "isSidechain": true,
  "agentId": "a155484fa15f65f16",
  "requestId": "req_011CauPYbQ6sujxUpTCTVnpf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ba6aa94-f8bd-4722-aaaa-79e9128ac8ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JrmNuyNMR8Zx3sXECnNRZF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1012,
      "cache_read_input_tokens": 9927,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1012
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 9927,
          "cache_creation_input_tokens": 1012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1012,
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

_source line 13 · 2026-05-10T18:49:50.766Z_

<details><summary>↩ Tool result · `toolu_01UKQjyZMuH8Rhe8dofmTQPu`</summary>

```text
# Format Tax: Prompt vs. Decoder Attribution

## Key Numerical Claims

**Prompt-level dominance:**
The research demonstrates that "of 39 cells with any statistically significant effect, 36 (92%) are already present under the format-requesting prompt alone and only 15 (38%) involve GCD." Additionally, the average accuracy loss from the format-requesting prompt alone (GET·) is −3.9 percentage points, compared to just −1.6 pp for grammar-constrained decoding.

**Flip rates reveal the source:**
"Per-question flip rates—the rate at which freeform-correct answers become incorrect under structured output—are 25.9% with GCD and 24.1% without," indicating the decoder constraint adds minimal degradation beyond the prompt effect.

## Benchmarks and Tasks Evaluated

- **MATH-500:** 500 competition math problems
- **GPQA-Diamond:** 198 graduate-level science questions
- **ZebraLogic:** 500 constraint satisfaction puzzles
- **WritingBench:** 500 open-ended writing tasks

Four output formats tested: JSON, XML, Markdown, and LaTeX

## Important Limitations

The authors note their "controlled setting likely underestimates the format tax in practice. Real deployments contend with schema errors, ambiguous specifications, and malformed examples." They also caution findings "apply specifically to format constraints" for presentation, not cases where grammars encode correctness requirements like code synthesis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ba6aa94-f8bd-4722-aaaa-79e9128ac8ca",
  "isSidechain": true,
  "promptId": "8ecf08e1-2116-4f25-b8d6-7ecf13c4de4d",
  "agentId": "a155484fa15f65f16",
  "type": "user",
  "uuid": "601733d9-140d-434a-950c-3efc13b997da",
  "sourceToolAssistantUUID": "1ba6aa94-f8bd-4722-aaaa-79e9128ac8ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-10T18:50:03.852Z_

Here is my report.

---

**1. Does the paper exist?**
Yes. "The Format Tax" (arXiv 2604.03616) by Ivan Yee Lee, Loris D'Antoni, and Taylor Berg-Kirkpatrick (UC San Diego), submitted April 4, 2026.

**2. Does it claim 92% prompt-level vs ~1.6pp decoder-level?**
Partially -- the numbers are real but the "92%" means something different than implied. The paper finds that of 39 model/format cells showing a statistically significant accuracy drop, 36 (92%) already appear under the format-requesting prompt alone, before any constrained decoding. The average prompt-level loss is -3.9 pp, while grammar-constrained decoding (GCD) adds only -1.6 pp on top. So "92%" refers to the fraction of *cells* showing a significant effect at the prompt level, not that 92% of the magnitude of degradation comes from the prompt. The directional claim is correct -- the prompt is the dominant source -- but citing "92%" as a magnitude share is a mischaracterization.

**3. Tasks/benchmarks evaluated:**
- MATH-500 (competition math)
- GPQA-Diamond (graduate-level science)
- ZebraLogic (constraint-satisfaction logic puzzles)
- WritingBench (open-ended writing)
- Four formats: JSON, XML, Markdown, LaTeX
- Six open-weight models + four API models

**4. Caveats for information extraction:**
Critical: the paper explicitly studies *presentation formatting* (asking a model to wrap its answer in JSON/XML), not cases where structured output encodes correctness requirements. Information extraction -- where the schema defines *what* to extract -- is a fundamentally different use case the authors themselves exclude. Additionally, the authors note their controlled setup likely *underestimates* real-world format tax (schema errors, ambiguous specs). Finally, most recent closed-weight API models showed minimal or no format tax, suggesting this is primarily an open-weight model issue.

Sources:
- [The Format Tax - arXiv abstract](https://arxiv.org/abs/2604.03616)
- [The Format Tax - full HTML](https://arxiv.org/html/2604.03616)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "601733d9-140d-434a-950c-3efc13b997da",
  "isSidechain": true,
  "agentId": "a155484fa15f65f16",
  "requestId": "req_011CauPZRb2Lav6YYR1gMgRP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e1a65fc4-9805-451b-9f9b-2771eba2c672",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUcShraoFaesxiytyszU6h",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 536,
      "cache_read_input_tokens": 10939,
      "output_tokens": 532,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 536
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 532,
          "cache_read_input_tokens": 10939,
          "cache_creation_input_tokens": 536,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 536,
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
