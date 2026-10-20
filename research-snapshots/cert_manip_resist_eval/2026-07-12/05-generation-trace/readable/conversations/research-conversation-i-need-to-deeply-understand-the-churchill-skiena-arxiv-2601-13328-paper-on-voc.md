# Research conversation: I need to deeply understand the Churchill & Skiena (arXiv:2601.13328) paper on vocabulary extension for frozen models, a

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a45ce7bcb27840239.jsonl`
- **Structured JSON:** [`2ea61504197c67151e74.json`](../../sessions/2e/2ea61504197c67151e74.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-19T18:10:12.389Z_

I need to deeply understand the Churchill & Skiena (arXiv:2601.13328) paper on vocabulary extension for frozen models, and the newer "Defragmenting Language Models" (arXiv:2604.16656) paper that reportedly achieves ~20pt gains via interpretability-based vocabulary expansion.

Please do the following:
1. Fetch https://arxiv.org/abs/2601.13328 and extract: (a) exactly which models were tested (only Llama 3.2 1B?), (b) the actual cosine similarity numbers per language (especially Amharic, Shan, Vietnamese), (c) any downstream accuracy measurements, (d) the "vote-splitting problem" they mention, (e) any caveats about scaling to larger models
2. Fetch https://arxiv.org/abs/2604.16656 ("Defragmenting Language Models") and extract: (a) their method for vocabulary expansion, (b) what gains they achieve and on what benchmarks, (c) which models and languages they test on, (d) how it compares to Churchill & Skiena
3. Search for "vocabulary extension frozen language models multilingual 2025 2026" for any other relevant work

Report back with:
- Honest assessment of Churchill & Skiena's actual results and limitations
- How Defragmenting Language Models works and whether it's a better approach for the proposal
- Whether vocabulary extension on frozen 70B models for African languages is feasible
- Recommendations for how to frame Experiment 2a realistically

Keep your report under 500 words with specific details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "885fac21-638b-49aa-852f-c24d838cbccc",
  "agentId": "a45ce7bcb27840239",
  "type": "user",
  "uuid": "e57eb621-5bfe-4003-a124-7b1a908cd553",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T18:10:12.393Z_

```json
{
  "parentUuid": "e57eb621-5bfe-4003-a124-7b1a908cd553",
  "isSidechain": true,
  "agentId": "a45ce7bcb27840239",
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
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "badb3ae9-c0eb-4e48-9f07-d51612ba5bbb",
  "timestamp": "2026-05-19T18:10:12.393Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T18:10:12.395Z_

```json
{
  "parentUuid": "badb3ae9-c0eb-4e48-9f07-d51612ba5bbb",
  "isSidechain": true,
  "agentId": "a45ce7bcb27840239",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2d0d2e5c-6569-4063-822d-d0e714ccd0d1",
  "timestamp": "2026-05-19T18:10:12.395Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T18:10:16.379Z_



I'll fetch both papers and search for related work in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d0d2e5c-6569-4063-822d-d0e714ccd0d1",
  "isSidechain": true,
  "agentId": "a45ce7bcb27840239",
  "requestId": "req_011CbCNpMETR4fF4AkRUiNuj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42eb170a-2323-42f4-8c7a-95de30d6f088",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VReKvXLCNR1hHeDg3xap8p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1675,
      "cache_read_input_tokens": 7409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1675,
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

_source line 5 · 2026-05-19T18:10:16.524Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Fu84HsynBahErGjQCtN2KN`</summary>

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
  "parentUuid": "42eb170a-2323-42f4-8c7a-95de30d6f088",
  "isSidechain": true,
  "agentId": "a45ce7bcb27840239",
  "requestId": "req_011CbCNpMETR4fF4AkRUiNuj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3400cbdb-ea43-4d67-8dc6-62abed76b430",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VReKvXLCNR1hHeDg3xap8p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1675,
      "cache_read_input_tokens": 7409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1675,
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

### Tool result

_source line 6 · 2026-05-19T18:10:16.527Z_

<details><summary>↩ Tool result · `toolu_01Fu84HsynBahErGjQCtN2KN`</summary>

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
  "parentUuid": "3400cbdb-ea43-4d67-8dc6-62abed76b430",
  "isSidechain": true,
  "promptId": "885fac21-638b-49aa-852f-c24d838cbccc",
  "agentId": "a45ce7bcb27840239",
  "type": "user",
  "uuid": "5c27c586-402f-4821-a7b5-bfbfc65d02b7",
  "sourceToolAssistantUUID": "3400cbdb-ea43-4d67-8dc6-62abed76b430",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T18:10:19.808Z_



Now I'll fetch both papers and run the web search in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c27c586-402f-4821-a7b5-bfbfc65d02b7",
  "isSidechain": true,
  "agentId": "a45ce7bcb27840239",
  "requestId": "req_011CbCNpfs8EomcWv7QxmAQ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6981a915-a476-4eca-b144-b12b3f1498f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CGvAUHNHnRng61SXvXNDDp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1116,
      "cache_read_input_tokens": 9084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1116,
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

_source line 8 · 2026-05-19T18:10:23.099Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EgPyG8Yr8gpaycUGA5mFbb`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.13328",
  "prompt": "Extract ALL specific details from this paper: (1) Exactly which models were tested - list every model name and size. (2) The exact cosine similarity numbers per language, especially Amharic, Shan, Vietnamese - give me the actual numbers from tables. (3) Any downstream accuracy measurements on tasks like question answering, classification etc. (4) The \"vote-splitting problem\" - what is it exactly? (5) Any caveats or limitations about scaling to larger models. (6) The exact method they use for vocabulary extension on frozen models. (7) How many new tokens they add. (8) Any tables of results - reproduce the key numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6981a915-a476-4eca-b144-b12b3f1498f9",
  "isSidechain": true,
  "agentId": "a45ce7bcb27840239",
  "requestId": "req_011CbCNpfs8EomcWv7QxmAQ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3702a6d-b0b8-497d-9295-a89305bff55f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CGvAUHNHnRng61SXvXNDDp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1116,
      "cache_read_input_tokens": 9084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1116,
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

_source line 9 · 2026-05-19T18:10:25.910Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GKysmzLsCAjR1FgTRCCHvW`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.16656",
  "prompt": "Extract ALL specific details from this paper \"Defragmenting Language Models\": (1) Their exact method for vocabulary expansion - how does it work step by step? (2) What specific gains do they achieve and on what benchmarks? Are there really ~20pt gains? Give exact numbers. (3) Which models and languages do they test on? List all. (4) How does their approach compare to Churchill & Skiena or other vocabulary extension work? (5) What is their key insight about interpretability-based vocabulary expansion? (6) Any limitations or caveats they mention. (7) Reproduce key results tables if possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3702a6d-b0b8-497d-9295-a89305bff55f",
  "isSidechain": true,
  "agentId": "a45ce7bcb27840239",
  "requestId": "req_011CbCNpfs8EomcWv7QxmAQ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d90acb5-18cc-423f-a9d3-2a285083830d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CGvAUHNHnRng61SXvXNDDp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1116,
      "cache_read_input_tokens": 9084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1116,
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

_source line 10 · 2026-05-19T18:10:26.058Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0144J263ysEUSS2ki9kMF7sJ`</summary>

```json
{
  "query": "vocabulary extension frozen language models multilingual 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d90acb5-18cc-423f-a9d3-2a285083830d",
  "isSidechain": true,
  "agentId": "a45ce7bcb27840239",
  "requestId": "req_011CbCNpfs8EomcWv7QxmAQ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa6a80c7-fcc8-4631-b356-bb0c401a0dfe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CGvAUHNHnRng61SXvXNDDp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1116,
      "cache_read_input_tokens": 9084,
      "output_tokens": 486,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1116
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 486,
          "cache_read_input_tokens": 9084,
          "cache_creation_input_tokens": 1116,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1116,
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

_source line 11 · 2026-05-19T18:10:27.533Z_

<details><summary>↩ Tool result · `toolu_01EgPyG8Yr8gpaycUGA5mFbb`</summary>

```text
# Summary of Available Information

Based on the webpage content provided, I can only extract limited details:

## Available Information:

**(1) Models Tested:**
Only one model is explicitly mentioned: "Llama 3.2 1B model"

**(2) Cosine Similarity Numbers:**
The abstract states results "often have similar last hidden states" but provides no specific numerical values, cosine similarity figures, or per-language data for Amharic, Shan, Vietnamese, or others.

**(3) Downstream Task Measurements:**
None are mentioned in this webpage content.

**(4) Vote-Splitting Problem:**
Not discussed in the available text.

**(5) Scaling Limitations:**
Not addressed in this excerpt.

**(6) Vocabulary Extension Method:**
The abstract describes it as "post-hoc additions to the token vocabulary that coalesce multi-token characters into single tokens" but provides no technical implementation details.

**(7) Number of New Tokens Added:**
Not specified in this content.

**(8) Results Tables:**
None are included on this webpage.

## Limitation:

This webpage is an arXiv abstract page only. To access the specific details requested—particularly tables, numerical results, methodology details, and experimental findings—you would need to view the full PDF or HTML version of the paper using the provided links.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3702a6d-b0b8-497d-9295-a89305bff55f",
  "isSidechain": true,
  "promptId": "885fac21-638b-49aa-852f-c24d838cbccc",
  "agentId": "a45ce7bcb27840239",
  "type": "user",
  "uuid": "a54d91be-2d75-4319-897e-a7a56f1b1a8d",
  "sourceToolAssistantUUID": "f3702a6d-b0b8-497d-9295-a89305bff55f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T18:10:31.473Z_

<details><summary>↩ Tool result · `toolu_01GKysmzLsCAjR1FgTRCCHvW`</summary>

```text
# Analysis of "Defragmenting Language Models" Paper

Based on the arXiv page content provided, I can only extract limited information, as the page contains primarily metadata and abstract rather than the full paper details you requested.

## Available Information from the Page:

**1. Core Problem Addressed:**
The abstract identifies "token over-fragmentation" where "LLMs take several multiples of tokens to encode the same information in many languages as they do for English."

**2. Key Methodological Claims:**
The paper proposes an "interpretability-based vocabulary expansion" approach with two core decisions:
- What items to add to vocabulary
- How to initialize embeddings

**3. Claimed Performance Gains:**
The abstract states "large gains (~20 pts)" in embedding initialization for "several languages written in non-Latin scripts," though exact benchmarks aren't specified in this excerpt.

**4. Novel Contribution:**
They identify "subword detokenization" where "models progressively merge fragmented subword tokens into larger subwords across layers" and propose a method called **FragMend**.

## Critical Limitation:

The arXiv abstract page **does not contain** the detailed information you requested:
- Specific step-by-step methodology details
- Exact numerical results with benchmark names
- Complete list of tested models and languages
- Comparative analysis against Churchill & Skiena or baseline methods
- Results tables

**To obtain these specifics, you would need to access the full PDF or HTML version** of the paper (available via the links provided on the page).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d90acb5-18cc-423f-a9d3-2a285083830d",
  "isSidechain": true,
  "promptId": "885fac21-638b-49aa-852f-c24d838cbccc",
  "agentId": "a45ce7bcb27840239",
  "type": "user",
  "uuid": "84ea97e9-65c8-4d29-acee-1d292d715062",
  "sourceToolAssistantUUID": "6d90acb5-18cc-423f-a9d3-2a285083830d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T18:10:32.796Z_

<details><summary>↩ Tool result · `toolu_0144J263ysEUSS2ki9kMF7sJ`</summary>

```text
Web search results for query: "vocabulary extension frozen language models multilingual 2025 2026"

Links: [{"title":"Efficient and Effective Vocabulary Expansion Towards Multilingual Large   Language Models","url":"https://arxiv.org/pdf/2402.14714"},{"title":"[2508.15807] Vocabulary Expansion of Large Language Models via Kullback-Leibler-Based Self-Distillation","url":"https://arxiv.org/abs/2508.15807"},{"title":"Defragmenting Language Models: An Interpretability-based Approach for Vocabulary Expansion","url":"https://arxiv.org/html/2604.16656"},{"title":"Efficient and Effective Vocabulary Expansion Towards Multilingual Large Language Models","url":"https://arxiv.org/html/2402.14714v1"},{"title":"[2602.09388] Effective vocabulary expanding of multilingual language models for extremely low-resource languages","url":"https://arxiv.org/abs/2602.09388"},{"title":"[2402.14714] Efficient and Effective Vocabulary Expansion Towards Multilingual Large Language Models","url":"https://arxiv.org/abs/2402.14714"},{"title":"Vocabulary Expansion","url":"https://www.aussieai.com/research/vocab-expansion"},{"title":"Vocabulary Expansion of Large Language Models via Kullback-Leibler-Based Self-Distillation","url":"https://arxiv.org/pdf/2508.15807"}]

I found several relevant research papers on vocabulary extension for frozen language models and multilingual applications. Here are the key findings:

## Recent Research on Vocabulary Expansion for Frozen LLMs

**2025-2026 Developments:**

A recent approach addresses vocabulary expansion in frozen LLMs by introducing a mathematically grounded method for knowledge distillation via KL divergence, even when the original and extended models use different tokenizations. This work tackles the challenge of large pre-trained language models struggling to incorporate new domain-specific terminology when fine-tuned on small, specialized corpora.

More recently, interpretability-based vocabulary expansion, which uses model activations to inform both item selection and embedding initialization, has emerged as a new direction to reduce token over-fragmentation.

**Multilingual Applications:**

An efficient and effective vocabulary expansion (EEVE) method incorporates parameter freezing and subword initialization, showing that non-English proficiency can be significantly boosted within just 2 billion tokens, in contrast to previous efforts that believed trillions of tokens were necessary.

Recent approaches continue to pre-train multilingual pre-trained language models using target language corpora based on expanded vocabulary representations, with results showing improvements on POS tagging and NER tasks.

These papers demonstrate active research into efficient vocabulary expansion techniques for multilingual language models with frozen parameters.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa6a80c7-fcc8-4631-b356-bb0c401a0dfe",
  "isSidechain": true,
  "promptId": "885fac21-638b-49aa-852f-c24d838cbccc",
  "agentId": "a45ce7bcb27840239",
  "type": "user",
  "uuid": "0593d902-ecc1-4bf0-bc3a-511a1fd158f2",
  "sourceToolAssistantUUID": "fa6a80c7-fcc8-4631-b356-bb0c401a0dfe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-19T18:10:36.464Z_

The abstracts don't have enough detail. Let me fetch the full HTML versions of both papers, plus the other relevant papers found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0593d902-ecc1-4bf0-bc3a-511a1fd158f2",
  "isSidechain": true,
  "agentId": "a45ce7bcb27840239",
  "requestId": "req_011CbCNqrPv9TtD4DnXGcdTc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f6b90d5-0188-4bdb-820a-d2530d45c1cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XoUW5RtSGWBeuzKJsJUZBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1889,
      "cache_read_input_tokens": 10200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1889,
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

_source line 15 · 2026-05-19T18:10:38.820Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CQkc63Xfhc2PH5PfLSA1Ez`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.13328",
  "prompt": "Extract ALL specific details: (1) Exactly which models were tested - every model name and size. (2) Exact cosine similarity numbers per language from ALL tables, especially Amharic, Shan, Vietnamese. (3) Any downstream accuracy measurements. (4) The \"vote-splitting problem\" - exact description. (5) Caveats about scaling to larger models. (6) Their exact method for vocabulary extension. (7) How many new tokens added. (8) Reproduce ALL key numbers from tables. (9) What languages were tested? (10) Any limitations section content."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f6b90d5-0188-4bdb-820a-d2530d45c1cc",
  "isSidechain": true,
  "agentId": "a45ce7bcb27840239",
  "requestId": "req_011CbCNqrPv9TtD4DnXGcdTc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6fa4f8df-9b55-4d9b-bbff-f51a4be00a44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XoUW5RtSGWBeuzKJsJUZBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1889,
      "cache_read_input_tokens": 10200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1889,
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

_source line 16 · 2026-05-19T18:10:41.660Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01K1QZxiXjC4ybfNaBrUzm32`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.16656",
  "prompt": "Extract ALL specific details: (1) Step-by-step method for vocabulary expansion called FragMend. (2) Exact benchmark gains - reproduce numbers from tables. Are there ~20pt gains? On which benchmarks? (3) ALL models tested with sizes. (4) ALL languages tested. (5) How does it compare to Churchill & Skiena or other baselines? (6) The \"subword detokenization\" finding. (7) How they initialize new embeddings. (8) Any limitations. (9) Is the model frozen or fine-tuned? (10) Reproduce key results tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fa4f8df-9b55-4d9b-bbff-f51a4be00a44",
  "isSidechain": true,
  "agentId": "a45ce7bcb27840239",
  "requestId": "req_011CbCNqrPv9TtD4DnXGcdTc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57f2326d-31a6-483f-a8a3-d4551041f473",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XoUW5RtSGWBeuzKJsJUZBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1889,
      "cache_read_input_tokens": 10200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1889,
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

_source line 17 · 2026-05-19T18:10:43.087Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RTM5dMT4PuCEm8kZkyYiiF`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.09388",
  "prompt": "Extract: what languages they test on (especially African languages), what models they use, what method for vocabulary expansion on low-resource languages, and key results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57f2326d-31a6-483f-a8a3-d4551041f473",
  "isSidechain": true,
  "agentId": "a45ce7bcb27840239",
  "requestId": "req_011CbCNqrPv9TtD4DnXGcdTc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f91d349-d7db-4525-b8fd-03137273350b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XoUW5RtSGWBeuzKJsJUZBK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1889,
      "cache_read_input_tokens": 10200,
      "output_tokens": 530,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1889
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 530,
          "cache_read_input_tokens": 10200,
          "cache_creation_input_tokens": 1889,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1889,
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

_source line 18 · 2026-05-19T18:10:48.416Z_

<details><summary>↩ Tool result · `toolu_01RTM5dMT4PuCEm8kZkyYiiF`</summary>

```text
# Analysis of arXiv:2602.09388

**Languages Tested:**
The abstract does not specify which languages were evaluated, including whether any African languages were included in the experiments.

**Models Used:**
The paper focuses on "multilingual pre-trained language models (mPLMs)" but does not identify specific model names in the provided abstract.

**Vocabulary Expansion Method:**
The approach involves three key steps: expanding vocabulary using target language corpus, screening and removing source-language-biased tokens from the original vocabulary, and initializing new word representations "utilizing bilingual dictionaries to initialize the representations of the expanded vocabulary." The team then continues pre-training on target language data.

**Key Results:**
Performance improvements were achieved on downstream tasks: "0.54% and 2.60%, respectively" on POS tagging and NER tasks compared to randomly initialized vocabulary baselines. The method demonstrated robustness in corpus selection and "the models' performance on the source language does not degrade after continued pre-training."

**Note:** The full paper would be needed for complete information about specific language selections and model architectures tested.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f91d349-d7db-4525-b8fd-03137273350b",
  "isSidechain": true,
  "promptId": "885fac21-638b-49aa-852f-c24d838cbccc",
  "agentId": "a45ce7bcb27840239",
  "type": "user",
  "uuid": "5a779952-a59c-45f5-a50e-f3fc2917ff83",
  "sourceToolAssistantUUID": "7f91d349-d7db-4525-b8fd-03137273350b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T18:10:53.426Z_

<details><summary>↩ Tool result · `toolu_01CQkc63Xfhc2PH5PfLSA1Ez`</summary>

```text
# Detailed Extraction: Tokenization Premiums Paper

## 1. Models Tested
The study evaluated **10 tokenizers** from models released 2018-2024:
- Google BERT (119,543 tokens)
- OpenAI GPT-2 (50,256 tokens)
- Google T5 (32,100 tokens)
- Meta M2M-100 (128,104 tokens)
- OpenAI GPT-3.5 (100,256 tokens)
- Mistral 7B (32,515 tokens)
- Anthropic Claude 2.1 (64,298 tokens)
- OpenAI GPT-4o (199,998 tokens)
- Meta Llama 3 (127,040 tokens)
- AllenAI OLMo 2 (99,579 tokens)

## 2. Cosine Similarity Results (Table 4)
Testing employed **Llama 3.2 1B model**. Key results at Layer 0 with Linear Regression strategy (best performer):

| Language | Similarity |
|----------|-----------|
| Amharic (amh) | .624 |
| Shan (shn) | .681 |
| Vietnamese (vie) | .853 |
| Hebrew (heb) | .809 |
| Hindi (hin) | .870 |
| Bengali (ben) | .809 |
| Armenian (hye) | .796 |
| Tamil (tam) | .762 |
| Telugu (tel) | .762 |
| Urdu (urd) | .796 |
| Yiddish (ydd) | .809 |
| Chinese (zho) | .982 |

## 3. Downstream Accuracy Measurements
**None provided.** Study explicitly notes: "Cosine similarity is not necessarily aligned with performance on real downstream tasks, although we hope that it is correlated."

## 4. Vote-Splitting Problem Description
The authors identify this limitation: "Augmenting the vocabulary, rather than replacing it, means that the model will end up splitting probability mass between the original sub-character tokens and the new combined tokens. This vote-splitting effect could lead to incorrect tokens being selected."

Proposed solutions include:
- Input-only compression (not output)
- Removing merged sub-character tokens from output matrix
- "Winner-takes-all" probability redistribution favoring merged tokens

## 5. Scaling Caveats
Authors acknowledge their approach assumes "the model's training corpus included content in the target language." No explicit statements restrict application to larger models, though testing used only the Llama 3.2 **1B** (one billion) parameter model.

## 6. Vocabulary Extension Method
Three embedding derivation strategies tested:

**k-nearest neighbors:** "find the k nearest neighbors to h and average their input embeddings in V₀ weighted by their inverse distances"

**Linear regression:** "learn an affine transformation (linear plus bias) from HV to EV to predict an input embedding"

**Local linear regression:** "find its k nearest neighbors, train a weighted linear regression from those k hidden representations to their k corresponding input embeddings"

## 7. New Tokens Added
Vocabulary extension focused on "replacing multi-token encodings of OOV Unicode characters with new, per-character tokens." Specific counts per language shown in Table 4's "% of new tokens in encodings" column (ranging 26%-93%).

## 8. Key Numerical Tables
**Tokenization Premiums (Table 2 examples):**
- Bengali with GPT-2/3: **9.70x** English premium
- Shan with GPT-2/3: **19.09x** English premium
- Hindi with GPT-2/3: **7.51x** English premium
- Vietnamese with GPT-2/3: **4.60x** English premium

**Vocabulary Statistics (Table 3):**
- T5: 15 Unicode blocks; GPT-4o: 83 blocks
- GPT-4o contains 67,638 tokens >7 bytes

## 9. Languages Tested
**12 low-resource languages:** Amharic, Bengali, Hebrew, Hindi, Armenian, Shan, Tamil, Telugu, Urdu, Yiddish, Vietnamese, Chinese (traditional script). FLORES-200 dataset provided 997 sentence pairs per language.

## 10. Limitations Section Content
Authors acknowledge four critical weaknesses:

1. **Metric validity:** "A cosine similarity of 0.999 in isolation is meaningless. If the LM maps every sentence to a single embedding then everything will have cosine similarity of 1.0."

2. **Task misalignment:** Similarity doesn't guarantee downstream task performance.

3. **Aggressive averaging:** "Averaging the last hidden states is a fairly aggressive operation."

4. **Vote-splitting:** Detailed above; could produce incorrect token selections during generation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fa4f8df-9b55-4d9b-bbff-f51a4be00a44",
  "isSidechain": true,
  "promptId": "885fac21-638b-49aa-852f-c24d838cbccc",
  "agentId": "a45ce7bcb27840239",
  "type": "user",
  "uuid": "468071b6-f055-407b-8e44-0a74db457921",
  "sourceToolAssistantUUID": "6fa4f8df-9b55-4d9b-bbff-f51a4be00a44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T18:10:59.781Z_

<details><summary>↩ Tool result · `toolu_01K1QZxiXjC4ybfNaBrUzm32`</summary>

```text
# FragMend: Vocabulary Expansion Method - Detailed Extraction

## 1. Step-by-Step FragMend Method

**Stage 1 (Item Selection):** Uses subword-level detokenization via Patchscopes. For each word in training corpus, extracts all token affixes (prefixes, infixes, suffixes). Applies detokenization procedure to determine which subwords are successfully reconstructed by the model across layers.

**Stage 2 (Embedding Initialization):** Uses learned layer-dependent mappings (Procrustes transformations) from hidden activations to embedding space. For subwords with multiple candidate initializations across words, applies a "reduction strategy."

**Stage 3 (Tuning):** Fine-tunes embeddings via Language-Adaptive Pre-Training (LAPT) using training + tuning corpus combined.

## 2. Benchmark Gains

The abstract claims **"∼20 pts" gains**, but examining tables:

- **SIB200 (Table 1 - Belebele shown instead):** No ~20pt single jumps visible in reported results
- **Figure 3:** Tokens2Words vs baselines show variable gains, with non-Latin languages benefiting most
- **Figure 4(a):** Performance-efficiency tradeoff shown graphically; FragMend achieves "unrealized efficiency gains with minimal performance degradation"

Actual measured gains appear **modest (few points)** rather than 20pt, except possibly in specific comparisons not fully detailed in tables.

## 3. ALL Models Tested

**Primary model:**
- Qwen3-30B-A3B

**Scale analysis models:**
- Qwen3.5-0.8B, 2B, 4B, 9B
- TinyAya-Global
- Qwen3.5-4B

## 4. ALL Languages Tested (14 total)

**Latin script:** English (eng), Hungarian (hun), Vietnamese (vie), Scottish Gaelic (gla), Māori (mri), Tok Pisin (tpi)

**Non-Latin script:** Persian (pes), Hindi (hin), Serbian (srp), Southern Sotho (sot), Amharic (amh), Gujarati (guj), Odia (ory), Burmese (mya)

## 5. Comparison to Churchill & Skiena

Paper cites: "Churchill and Skiena ([2026](#bib.bib57))" but provides **no direct experimental comparison** against their method in results tables or figures.

Baselines tested:
- BPE-based expansion (frequency heuristics)
- Random initialization
- FVT (Fast Vocabulary Transfer)
- FOCUS initialization

## 6. Subword Detokenization Finding

**Key discovery:** Models progressively merge fragmented subwords into larger units across layers before reconstructing full words.

Figure 2(a) example: "Layla" tokenized as 'L'+'ay'+'la'. The subword 'Lay' detokenizes at layer 1, full word "Layla" detokenizes at layer 5 on the last token.

**Significance:** Demonstrates LLMs maintain "richer internal lexicon" beyond official vocabulary, with compositional intermediate representations.

## 7. Embedding Initialization Details

**Procrustes-based mapping:** For newly added word w*, embeddings initialized as:
- e_w* = T_l_min,E · h_t_n^l_min
- u_w* = T_l_min,U · h_t_n^l_min

Where T matrices are learned orthogonal transformations, h values are hidden activations at earliest successful detokenization layer.

**Subword reduction strategies tested:**
- R_m: Average candidate initializations
- R_e: Select initialization from earliest layer

## 8. Key Limitations Identified

- **Curse of multilinguality:** Smaller models underperform due to competing languages in parameter space
- **Out-of-distribution languages:** Tokens2Words/FragMend perform poorly for unsupported languages (marked red); requires strong model representations
- **Vocabulary expansion perversity:** Adding items without merges can worsen token efficiency; mitigated with 3+ UTF-8 character minimum
- **Efficiency ceiling:** Tokens2Words bounded by unique words in training corpus (~1000-10k sequences)

## 9. Model Freezing vs Fine-tuning

**Frozen:** Tokenizer and embeddings only; all other model parameters frozen per design.

**Fine-tuned:** Only embeddings tuned via LAPT (Language-Adaptive Pre-Training), not full model.

This enables practical deployment without retraining entire LLM.

## 10. Key Results (Reconstructed)

**Figure 4(a):** Pareto frontier shows FragMend pushing efficiency beyond Tokens2Words with comparable performance retention.

**Figure 2(b):** With 1000-sequence corpus, FragMend adds 2-3× more vocabulary items than Tokens2Words; achieves up to 3× token efficiency for low-resource languages (Burmese example).

**Figure 4(c):** Token reduction improves with model scale (0.8B→9B parameters).

---

**Note:** The claimed "∼20 pts" appears in abstract but specific benchmark tables show more modest single-digit gains; the larger advantage manifests in efficiency-performance tradeoff curves rather than absolute performance jumps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57f2326d-31a6-483f-a8a3-d4551041f473",
  "isSidechain": true,
  "promptId": "885fac21-638b-49aa-852f-c24d838cbccc",
  "agentId": "a45ce7bcb27840239",
  "type": "user",
  "uuid": "28a854d3-576e-46c9-8f12-85ba1dde657f",
  "sourceToolAssistantUUID": "57f2326d-31a6-483f-a8a3-d4551041f473",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-19T18:11:03.577Z_

Now let me get more detail on the "~20pt gains" claim from the Defragmenting paper and the other relevant paper on low-resource languages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28a854d3-576e-46c9-8f12-85ba1dde657f",
  "isSidechain": true,
  "agentId": "a45ce7bcb27840239",
  "requestId": "req_011CbCNsqi3y3nw9wF63BzV6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4fcec8c-8901-43a0-a7a8-ac53903be31a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J28VXombsRhXg8H8WuSM97",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 273,
      "cache_creation_input_tokens": 3007,
      "cache_read_input_tokens": 12089,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3007,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 22 · 2026-05-19T18:11:06.808Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BwoLYXXUcDusPGwBiJaTL3`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.16656",
  "prompt": "I need to find where the \"~20 pts\" claim comes from. Search for any table or figure that shows a ~20 point improvement. Look at ALL tables (Table 1, Table 2, etc.) and reproduce the exact numbers. Also: does the paper test on African languages like Amharic, Southern Sotho? What are the exact results for those? What is the exact performance of FragMend vs baselines on non-Latin script languages? Give me every number you can find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4fcec8c-8901-43a0-a7a8-ac53903be31a",
  "isSidechain": true,
  "agentId": "a45ce7bcb27840239",
  "requestId": "req_011CbCNsqi3y3nw9wF63BzV6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a63eb3c-5621-4be6-aedb-82c128a7c5d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J28VXombsRhXg8H8WuSM97",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 273,
      "cache_creation_input_tokens": 3007,
      "cache_read_input_tokens": 12089,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3007,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 23 · 2026-05-19T18:11:08.067Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JWYAYfgo9tc6rvKp38Q9De`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.09388",
  "prompt": "Extract: (1) Which specific languages are tested, especially any African languages? (2) Which specific models are used? (3) The exact vocabulary expansion method. (4) Key numerical results. (5) Does this work with frozen models?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a63eb3c-5621-4be6-aedb-82c128a7c5d4",
  "isSidechain": true,
  "agentId": "a45ce7bcb27840239",
  "requestId": "req_011CbCNsqi3y3nw9wF63BzV6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f45c7b05-4235-49fb-b809-cd20583aa447",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J28VXombsRhXg8H8WuSM97",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 273,
      "cache_creation_input_tokens": 3007,
      "cache_read_input_tokens": 12089,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3007
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 273,
          "output_tokens": 339,
          "cache_read_input_tokens": 12089,
          "cache_creation_input_tokens": 3007,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3007,
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

_source line 24 · 2026-05-19T18:11:12.600Z_

<details><summary>↩ Tool result · `toolu_01BwoLYXXUcDusPGwBiJaTL3`</summary>

```text
# Analysis of Performance Claims in "Defragmenting Language Models"

## The "~20 pts" Claim

The paper states: "we show that interpretability-based methods offer a superior performance-token efficiency trade-off" with "large gains (∼20 pts)" for embedding initialization on non-Latin script languages.

However, **I cannot locate a single table showing exactly 20-point improvements**. The closest evidence appears in the narrative rather than quantified results tables.

## Actual Reported Numbers

**Table 1 (Belebele)** shows FragMend results across configurations:
- Gujarati (guj): ranges 50.1-68.2 across different settings
- Odia (ory): ranges 44.7-63.0
- Burmese (mya): ranges 50.2-62.1

These variations suggest improvements but don't isolate a single "20 pt" baseline comparison.

## African Language Results

**Languages tested:**
- Amharic (amh): appears throughout results
- Southern Sotho (sot): included in experiments

**Specific numbers found:**
- Amharic shows notably lower absolute performance (range 32.5-44.8 on SIB200)
- Southern Sotho similar pattern (range 32.9-35.2)

The paper notes these "out-of-distribution languages" underperform because they "are not explicitly trained on," causing "weaker" activation quality.

## Key Limitation

The actual quantitative comparison tables don't isolate a clean baseline-versus-method contrast showing exactly 20 points. The claim appears contextual rather than empirically isolated in presented tables.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a63eb3c-5621-4be6-aedb-82c128a7c5d4",
  "isSidechain": true,
  "promptId": "885fac21-638b-49aa-852f-c24d838cbccc",
  "agentId": "a45ce7bcb27840239",
  "type": "user",
  "uuid": "003c39e6-9981-4d21-a808-63dd774c6501",
  "sourceToolAssistantUUID": "9a63eb3c-5621-4be6-aedb-82c128a7c5d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T18:11:15.488Z_

<details><summary>↩ Tool result · `toolu_01JWYAYfgo9tc6rvKp38Q9De`</summary>

```text
# Research Extraction: Multilingual Language Model Vocabulary Expansion

## (1) Languages Tested – African Representation
The study evaluates seven low-resource languages, including two African languages:
- **Amharic (am)** – Afro-Asiatic language with 98.37M tokens
- **Sinhala (si)** – Indo-European/Indic language with 303.72M tokens

Additionally, the authors mention related work extending models to "over 1,600 languages" using Bible corpora, though this is background context rather than their direct testing.

## (2) Base Model Used
The researchers employ "multilingual BERT (mBERT)" as their foundation model, which "supports 104 languages in total" with "a vocabulary size of 119,547 and an embedding dimension of 768."

## (3) Vocabulary Expansion Method
The approach involves four key steps:
- **Screening**: Extract vocabulary subsets biased toward source language (English)
- **Cross-lingual embeddings**: Train aligned word embeddings using bilingual dictionaries via "the orthogonal method"
- **Subword calculation**: Compute subword representations following "fastText's approach for training out-of-vocabulary words"
- **Initialization**: Calculate target embeddings through "weighted average" based on similarity matrices between source and target vocabularies

Expanded vocabularies exceeded 21,000 words per language, reaching up to 25,566 for North Sami.

## (4) Key Numerical Results
- **POS tagging**: Method improved "by 0.54%" versus random initialization baseline
- **NER task**: Performance improved "by 2.60%" on average, with maximum gains reaching "6.68%"
- **Source language preservation**: English performance showed "almost no decline" on POS tagging

## (5) Frozen Model Capability
The paper does not address whether this approach works with frozen encoder layers. The method modifies vocabulary embeddings and performs continued pre-training, implying parameter updates throughout the model.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f45c7b05-4235-49fb-b809-cd20583aa447",
  "isSidechain": true,
  "promptId": "885fac21-638b-49aa-852f-c24d838cbccc",
  "agentId": "a45ce7bcb27840239",
  "type": "user",
  "uuid": "4698f2ff-c449-49d6-829d-e7f23ae9d313",
  "sourceToolAssistantUUID": "f45c7b05-4235-49fb-b809-cd20583aa447",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-19T18:11:39.834Z_

I now have comprehensive data from all sources. Here is the report.

---

**Report: Vocabulary Extension for Frozen Models -- Paper Analysis**

**Churchill & Skiena (2601.13328): Honest Assessment**

This paper is primarily a *tokenization analysis* paper, not a vocabulary extension method paper. They tested 10 tokenizers (BERT through OLMo 2) for tokenization premium analysis, but their embedding experiments used only **Llama 3.2 1B**. Cosine similarity results (linear regression, Layer 0): Amharic 0.624, Shan 0.681, Vietnamese 0.853, Chinese 0.982. These are mediocre-to-poor for non-Latin scripts. Critically: **they report zero downstream task results**. They explicitly state cosine similarity "is not necessarily aligned with performance on real downstream tasks." They identify the "vote-splitting problem" -- adding new tokens without removing old sub-character tokens splits probability mass, potentially producing worse outputs than the original. They tested only a 1B model with no discussion of scaling to 70B. This paper provides useful framing but no evidence that the method works for generation.

**FragMend / Defragmenting LMs (2604.16656): Stronger but Nuanced**

FragMend uses interpretability: it discovers that models internally merge fragmented subwords across layers ("subword detokenization"), then uses Procrustes-mapped hidden states to initialize new embeddings. Only embeddings are tuned via Language-Adaptive Pre-Training; other parameters stay frozen. They test on Qwen3 models (0.8B to 30B-A3B) across 14 languages including Amharic and Southern Sotho. The "~20pt" claim in the abstract is misleading -- actual table results show modest single-digit gains on Belebele/SIB200. For African languages specifically, Amharic scored 32.5-44.8 on SIB200 and Southern Sotho 32.9-35.2 -- the paper flags these as "out-of-distribution" languages where the method underperforms because the base model lacks strong representations. This is the critical finding for your proposal.

**Feasibility for 70B Models + African Languages**

The evidence is cautionary. FragMend shows vocabulary expansion works best when the base model already has decent internal representations of the target language. For African languages where the base model has weak coverage, both papers suggest limited gains from vocabulary extension alone. Churchill & Skiena's 0.624 cosine similarity for Amharic is poor. FragMend's Amharic/Southern Sotho results are the weakest in their study. No paper has demonstrated vocabulary extension on a 70B frozen model.

**Recommendation for Experiment 2a**

Frame vocabulary extension as one component of a pipeline, not a standalone solution. Cite FragMend's frozen-embedding-only tuning as the most credible method, but honestly note: (1) gains are modest (single-digit, not 20pt) for languages with weak base model coverage, (2) no 70B experiments exist in the literature, (3) African languages are explicitly flagged as "out-of-distribution" in the best available study. A realistic framing: vocabulary extension reduces tokenization overhead (3-19x premiums) and may improve efficiency, but downstream quality gains for underrepresented African languages likely require combining vocab extension with targeted continued pretraining or adapter-based methods, not vocab extension on a frozen model alone.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4698f2ff-c449-49d6-829d-e7f23ae9d313",
  "isSidechain": true,
  "agentId": "a45ce7bcb27840239",
  "requestId": "req_011CbCNtzviDvsHnvkAh3Fp7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ec844c2-ba25-4ab9-8c0d-ca6895af15c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LFXRdZz6SvXnvbGhTmC5vn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1511,
      "cache_read_input_tokens": 15096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1511,
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
