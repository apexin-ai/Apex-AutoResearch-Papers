# Research conversation: Research the paper "GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search" by Matan Ben-To

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aee0facf533f0579b.jsonl`
- **Structured JSON:** [`fbe3a88aa1279356d7dd.json`](../../sessions/fb/fbe3a88aa1279356d7dd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

32 recorded events

### User

_source line 1 · 2026-05-30T06:42:02.533Z_

Research the paper "GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search" by Matan Ben-Tov, Mahmood Sharif (ACM CCS 2025). URL: https://arxiv.org/abs/2412.20953

Tasks:
1. Use WebFetch to read the arxiv abstract page
2. Use WebFetch to read the full PDF or HTML version if available
3. Search the web for any reviews, discussions, or conference proceedings info

Report back with:
- The full abstract
- Key method details: how GASLITE generates adversarial passages without model/corpus knowledge, how single-query attacks achieve 100% success, what makes standard defenses fail against adaptive versions, what the 0.0001% corpus poisoning rate means
- The threat model and assumptions
- Experimental results and key findings
- Limitations acknowledged

Be thorough — I need enough detail to write a precise technical analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "aee0facf533f0579b",
  "type": "user",
  "uuid": "9a55a55e-169e-46d8-bd9b-2d0842e9f9f1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-30T06:42:02.536Z_

```json
{
  "parentUuid": "9a55a55e-169e-46d8-bd9b-2d0842e9f9f1",
  "isSidechain": true,
  "agentId": "aee0facf533f0579b",
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskStop",
      "TaskUpdate",
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "1dbb60a2-c87a-42b2-96d8-b4fd49dc5665",
  "timestamp": "2026-05-30T06:42:02.536Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-30T06:42:02.537Z_

```json
{
  "parentUuid": "1dbb60a2-c87a-42b2-96d8-b4fd49dc5665",
  "isSidechain": true,
  "agentId": "aee0facf533f0579b",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "dddd7d8f-57e7-4db1-a255-3864d304dd25",
  "timestamp": "2026-05-30T06:42:02.537Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-30T06:42:04.924Z_



I'll start by fetching the arxiv page and searching for discussions about this paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dddd7d8f-57e7-4db1-a255-3864d304dd25",
  "isSidechain": true,
  "agentId": "aee0facf533f0579b",
  "requestId": "req_011CbYJEmNSJLetFfMNbi9yL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9d096f7-2c0a-4fa6-91b2-8cdf1a4d9fbc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017a8htBMuLCDecU3XNdg68o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1564,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1564,
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

_source line 5 · 2026-05-30T06:42:05.920Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017n7GEEFCwhTuRQdH1zQaUZ`</summary>

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
  "parentUuid": "e9d096f7-2c0a-4fa6-91b2-8cdf1a4d9fbc",
  "isSidechain": true,
  "agentId": "aee0facf533f0579b",
  "requestId": "req_011CbYJEmNSJLetFfMNbi9yL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3886412a-00d2-47e8-b3ba-2ae1c5436adc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017a8htBMuLCDecU3XNdg68o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1564,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1564,
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

_source line 6 · 2026-05-30T06:42:05.925Z_

<details><summary>↩ Tool result · `toolu_017n7GEEFCwhTuRQdH1zQaUZ`</summary>

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
  "parentUuid": "3886412a-00d2-47e8-b3ba-2ae1c5436adc",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "aee0facf533f0579b",
  "type": "user",
  "uuid": "296ba7c7-f4dc-4b4e-93f1-da493ea97110",
  "sourceToolAssistantUUID": "3886412a-00d2-47e8-b3ba-2ae1c5436adc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-30T06:42:09.384Z_



Now let me fetch the arxiv abstract page, the full paper, and search for discussions simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "296ba7c7-f4dc-4b4e-93f1-da493ea97110",
  "isSidechain": true,
  "agentId": "aee0facf533f0579b",
  "requestId": "req_011CbYJF34WFFjS7XqUWy4Xn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42dc1ffa-aa92-42d7-9548-5dfd3a8cf23e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018x63fHaQLUvLXR7rf7m5ik",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 8977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1121,
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

_source line 8 · 2026-05-30T06:42:11.329Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014vqaknTqgnoyfYGo7cPUt2`</summary>

```json
{
  "url": "https://arxiv.org/abs/2412.20953",
  "prompt": "Extract the complete abstract, authors, title, publication venue, and any other metadata from this arxiv paper page. Give me the full unabridged abstract text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42dc1ffa-aa92-42d7-9548-5dfd3a8cf23e",
  "isSidechain": true,
  "agentId": "aee0facf533f0579b",
  "requestId": "req_011CbYJF34WFFjS7XqUWy4Xn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0669b12b-dcd8-413c-9b85-0b25c007158e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018x63fHaQLUvLXR7rf7m5ik",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 8977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1121,
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

_source line 9 · 2026-05-30T06:42:15.614Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ud4MexVhUYwVGHeTpvk7Qp`</summary>

```json
{
  "url": "https://arxiv.org/html/2412.20953",
  "prompt": "Extract the FULL content of this paper in as much detail as possible. I need:\n1. The complete abstract\n2. The full introduction\n3. The threat model and assumptions\n4. The complete method/approach section (how GASLITE works, the optimization, the algorithm)\n5. All experimental results, tables, and findings\n6. The discussion of defenses and adaptive attacks\n7. Limitations section\n8. Key equations and algorithmic details\n9. The corpus poisoning rate details (0.0001%)\n10. How single-query attacks work and achieve 100% success rate\nPlease be as thorough and detailed as possible - include numbers, percentages, and technical specifics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0669b12b-dcd8-413c-9b85-0b25c007158e",
  "isSidechain": true,
  "agentId": "aee0facf533f0579b",
  "requestId": "req_011CbYJF34WFFjS7XqUWy4Xn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0fe55a9-03dc-46fd-8ee4-479a818f0b70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018x63fHaQLUvLXR7rf7m5ik",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 8977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1121,
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

_source line 10 · 2026-05-30T06:42:16.655Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GkEvbfiEivRVDQbUKyXJUa`</summary>

```json
{
  "query": "GASLITE adversarial retrieval dense embedding search Matan Ben-Tov Mahmood Sharif ACM CCS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0fe55a9-03dc-46fd-8ee4-479a818f0b70",
  "isSidechain": true,
  "agentId": "aee0facf533f0579b",
  "requestId": "req_011CbYJF34WFFjS7XqUWy4Xn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f324effa-2186-4b42-9195-17727546ac16",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018x63fHaQLUvLXR7rf7m5ik",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 8977,
      "output_tokens": 419,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1121
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 419,
          "cache_read_input_tokens": 8977,
          "cache_creation_input_tokens": 1121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1121,
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

_source line 11 · 2026-05-30T06:42:19.863Z_

<details><summary>↩ Tool result · `toolu_014vqaknTqgnoyfYGo7cPUt2`</summary>

```text
# Paper Metadata Extraction

**Title:** GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search

**Authors:** Matan Ben-Tov, Mahmood Sharif

**Publication Venue:** ACM CCS 2025

**arXiv Identifier:** 2412.20953

**Submission Date:** December 30, 2024 (v1); September 18, 2025 (v2)

**Subjects:** Cryptography and Security (cs.CR); Computation and Language (cs.CL)

---

## Complete Abstract

Dense embedding-based text retrieval—retrieving relevant passages from corpora via deep learning encodings—has become powerful for achieving state-of-the-art search and popularizing Retrieval Augmented Generation (RAG). However, embedding-based retrieval may face search-engine optimization (SEO) attacks where adversaries introduce malicious passages to promote harmful content. Prior work demonstrated such vulnerabilities but employed relaxed threat models, baseline methods, and limited evaluations. This research provides comprehensive robustness assessment of retrievers to uncover susceptibility factors. The authors propose GASLITE, an attack generating adversarial passages that embed adversary-chosen information without corpus content reliance or model modification, consistently outperforming prior approaches. Extensive evaluation of nine advanced models across varied threat models reveals retrievers face high vulnerability to SEO attacks targeting concept-specific queries, even with negligible poisoning rates (≥0.0001% of corpus), generalizing across corpora and query distributions. Single-query SEO is fully solved by GASLITE, while adaptive attacks bypass common defenses.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0669b12b-dcd8-413c-9b85-0b25c007158e",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "aee0facf533f0579b",
  "type": "user",
  "uuid": "f6bc89e3-8c7c-43b0-9e5e-4276568dd19d",
  "sourceToolAssistantUUID": "0669b12b-dcd8-413c-9b85-0b25c007158e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-30T06:42:23.381Z_

<details><summary>↩ Tool result · `toolu_01GkEvbfiEivRVDQbUKyXJUa`</summary>

```text
Web search results for query: "GASLITE adversarial retrieval dense embedding search Matan Ben-Tov Mahmood Sharif ACM CCS 2025"

Links: [{"title":"GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search | Proceedings of the 2025 ACM SIGSAC Conference on Computer and Communications Security","url":"https://dl.acm.org/doi/10.1145/3719027.3765095"},{"title":"GitHub - matanbt/GASLITE: SEO attack on dense embedding-based retrieval via poisoning · GitHub","url":"https://github.com/matanbt/gaslite"},{"title":"Matan Ben-Tov | Mahmood Sharif","url":"https://mahmoods01.github.io/authors/matan-ben-tov/"},{"title":"dblp: Mahmood Sharif","url":"https://dblp.org/pid/136/8393.html"},{"title":"[2412.20953] GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search","url":"https://arxiv.org/abs/2412.20953"},{"title":"Mahmood Sharif","url":"https://mahmoods01.github.io/"},{"title":"GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search","url":"https://arxiv.org/pdf/2412.20953"},{"title":"(PDF) GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search","url":"https://www.researchgate.net/publication/387540386_GASLITEing_the_Retrieval_Exploring_Vulnerabilities_in_Dense_Embedding-based_Search"},{"title":"GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search","url":"https://arxiv.org/html/2412.20953v2"}]

I found information about the GASLITE research paper. Here are the key findings:

## GASLITE Paper Summary

GASLITE is an attack for generating adversarial passages that—without relying on the corpus content or modifying the model—carry adversary-chosen information while achieving high retrieval ranking, consistently outperforming prior approaches.

The paper, authored by Matan Ben-Tov and Mahmood Sharif from Tel Aviv University, focuses on dense embedding-based text retrieval—retrieval of relevant passages from corpora via deep learning encodings—which has emerged as a powerful method for Retrieval Augmented Generation (RAG).

## Key Findings

GASLITE is a mathematically principled gradient-based search method for generating adversarial passages without relying on the corpus content or modifying the model.

Adversaries using GASLITE require minimal effort to manipulate search results—by injecting a negligible amount of adversarial passages (≤0.0001% of the corpus), they could make them visible in the top-10 results for 61-100% of unseen concept-specific queries against most evaluated models.

## Publication Details

The paper "GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search" by Matan Ben-Tov and Mahmood Sharif was published at the ACM Conference on Computer and Communications Security (CCS).

An official repository with code for reproducing the experiments is available on GitHub at https://github.com/matanbt/gaslite.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f324effa-2186-4b42-9195-17727546ac16",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "aee0facf533f0579b",
  "type": "user",
  "uuid": "7d10d680-c099-4777-9383-8fabc69b3fc3",
  "sourceToolAssistantUUID": "f324effa-2186-4b42-9195-17727546ac16",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-30T06:43:01.185Z_

<details><summary>↩ Tool result · `toolu_01Ud4MexVhUYwVGHeTpvk7Qp`</summary>

```text
# Comprehensive Summary: GASLITEing the Retrieval

## Abstract

This paper investigates vulnerabilities in dense embedding-based search systems through corpus poisoning attacks. The researchers introduce GASLITE, a gradient-based optimization method for generating adversarial passages that achieve high retrieval rankings while carrying attacker-chosen information. The study evaluates nine embedding models across three threat scenarios, revealing that retrievers remain highly vulnerable to concept-specific SEO attacks even with negligible poisoning rates (≤0.0001% of corpus).

## Introduction & Motivation

The authors address a critical security gap in embedding-based retrieval systems—used in search engines and Retrieval-Augmented Generation (RAG) systems. While prior work demonstrated SEO feasibility, those studies employed oversimplified threat models (single-query targeting), weak optimization techniques (query repetition), and limited model diversity, obscuring genuine robustness assessment.

The paper's core contributions include:

- **Threat models** reflecting realistic SEO goals emphasizing concept-specific query targeting
- **GASLITE algorithm**, mathematically grounded and gradient-based, surpassing prior attacks
- **Extensive robustness evaluation** across nine popular models under multiple settings
- **Defense analysis** with adaptive attack variants
- **Real-world case studies** including RAG systems

Key finding: "concept-specific SEO requires negligible poisoning scale (≤0.0001% of corpus)" for top-result visibility on most queries across most models.

## Threat Model & Assumptions

### Attacker Objectives
Adversaries seek two simultaneous goals:
1. **Visibility**: Maximize probability that adversarial passages appear in top-k results
2. **Informativeness**: Ensure crafted passages convey attacker-chosen content

### Attacker Capabilities
- Insert adversarial text passages into retrieval corpus
- Control passage text content (not tokenization)
- Poison budget: |P_adv| ≪ |P| (e.g., 10^-5 × corpus size)
- White-box access to model weights (justified by widespread open-source availability)
- Cannot modify model weights, access corpus content, or read ground truth

### Three Query Distribution Settings

1. **"Knows All"**: Attacker targets known finite query set Q; represents single-query SEO (often |Q|=1)

2. **"Knows What"** (Primary focus): Attacker targets specific concept with infinite query support but finite sample Q; reflects realistic SEO where queries relate to attack context (e.g., Harry Potter queries)

3. **"Knows [Almost] Nothing"**: Indiscriminate targeting across diverse query distributions; challenging setting requiring broad generalization

## Method: GASLITE Algorithm

### Formal Objective (Equation 2)

The authors formalize the adversary's goal as maximizing the dot product between an adversarial passage and the centroid of target query embeddings:

The simplified objective: maximize (1/|Q| × Σ EmbR(q)) · EmbR(p_adv)

This formulation suggests adversarial passages should reflect the "average" semantic of targeted queries. Full optimization of this objective guarantees visibility in top-k results.

### Constraint Implementation

To ensure informativeness, passages are constructed as: p_adv := info ⊕ trigger

The malicious information serves as a fixed prefix, exploiting primacy effect (early content influences readers more strongly). GASLITE optimizes only the trigger suffix while keeping information content intact.

### Multi-Budget Extension

For larger budgets (B>1), finding optimal solutions is NP-Hard (reduction to Set Cover). The approach partitions query set Q into B subsets via k-means clustering, attacking each separately. Testing revealed k-means best utilizes given budgets while maximizing in-cluster pairwise similarity.

### Algorithm Details

**GASLITE employs three key enhancements:**

1. **Multi-token greedy search**: Reduces backward passes per substitution compared to single-token methods
2. **Refined gradient approximation**: Averages linear approximations across multiple random token-substitution samples
3. **Text coherence maintenance**: Ensures decoded text (not tokens) matches optimization, critical since attackers insert actual text to corpus

**Algorithmic Steps (Algorithm 1)**:
- Calculate target vector (query centroid)
- Initialize trigger with random text
- For n_iter iterations:
  - Generate random single-flip variants
  - Average gradients across positions
  - Randomly select n_flip token positions for substitution
  - Use gradient information to identify n_cand promising token candidates
  - Filter tokenization irreversibilities
  - Greedily select best substitution
  - Update trigger

Hyperparameters: n_iter=100, n_grad=50, n_cand=128, n_flip=20

## Experimental Setup

### Models Evaluated (9 total)

**Cosine Similarity Models**: E5, MiniLM, GTR-T5, aMPNet, Arctic

**Dot Product Models**: Contriever, Contriever-MS, ANCE, mMPNet

Selection criteria: BERT-base scale (~110M parameters), strong benchmark performance, high popularity (HuggingFace downloads/GitHub usage), diverse architectures, and widespread prior usage.

### Datasets

- **Primary**: MSMARCO passage retrieval (8.8M passages, 0.5M queries)
- **Validation**: NQ, FiQA2018, SciFact, Quora datasets
- **Information sources**: ToxiGen (toxic statements), GPT-4 (synthetic negative statements)

### Attack Baselines

1. **Info Only**: Just malicious information, no optimization
2. **Stuffing**: Common SEO technique; trigger filled with sample queries
3. **Cor.Pois.**: State-of-the-art HotFlip variant from Zhong et al. (2023)
4. **GASLITE**: The proposed method

### Evaluation Metrics

- **appeared@k**: Proportion of queries where ≥1 adversarial passage appears in top-k results
- **Objective similarity**: Cosine or dot product between crafted passage and query centroid
- Trigger length: 100 tokens
- Evaluation on held-out queries (except single-query settings)

## Key Results

### "Knows All" - Single Query Attack

**Finding**: GASLITE achieves optimal single-query success with "100% appeared@1" across all nine models.

**Comparative Performance** (Table 1):
- Info Only: 0% success (baseline control)
- Stuffing: 30-96% appeared@10 (varies by model)
- Cor.Pois.: Underperforms, sometimes worse than stuffing
- GASLITE: Consistent 100% appeared@1

**Objective Metrics**: GASLITE achieves exceptionally high similarity scores. For dot-product models like Contriever, similarity reaches 3.453 ± 0.350, roughly twice baseline methods.

**Interpretation**: The discrete nature of single queries means optimization can achieve perfect alignment in embedding space. This represents a completely solved problem under this threat model.

### "Knows What" - Concept-Specific Targeting

**Primary Finding**: "By merely inserting 10 crafted passages (poisoning rate ≤0.0001%), GASLITE achieves >50% appeared@10 on 6/9 models for unknown concept-related queries."

**Detailed Results** (Figures 3-4):
- **With 1 adversarial passage**: Highly variable across models
  - Contriever: ~100% appeared@10
  - E5: ~70% appeared@10
  - Arctic: ~20% appeared@10
  
- **With 10 passages** (0.0001% poison rate):
  - Average appeared@10 across models: ~60-70%
  - Contriever-MS: ~95%
  - ANCE: ~80%
  - E5: ~75%

- **Performance scaling**: Success increases with budget size; 100% appeared@100 achieved on all models with just 10 passages

**Baseline Comparisons** (Figure 3):
- GASLITE outperforms all baselines by >140% in appeared@10
- Stuffing fails on most models (except Contriever)
- Cor.Pois. achieves 10-30% improvement over baselines but trails GASLITE significantly

**Tested Concepts**: Eight recurring concepts from MSMARCO with varying semantics and frequency; results consistent across diverse topics

### "Knows Nothing" - Diverse Query Targeting

**Finding**: Concept-agnostic SEO demands higher poisoning rates (~0.001%) but remains achievable.

**Results** (Figure 5):
- **Budget |P_adv|=100** (0.001% poison rate):
  - appeared@10: 5-20% across models
  - appeared@100: 15-40% across models
  
- **Budget scaling** (Figure 22 in appendix):
  - |P_adv|=1: ~0% appeared@10
  - |P_adv|=5: 0-5% appeared@10
  - |P_adv|=10: 1-10% appeared@10
  - |P_adv|=50: 3-15% appeared@10
  - |P_adv|=100: 5-20% appeared@10

**Model Variance**: Contriever variants show substantially higher susceptibility (~20%) compared to cosine-based models (~5-10%)

**Comparison**: GASLITE markedly outperforms all baselines; Cor.Pois. achieves <6% while GASLITE reaches 5-20%

### Perfect Attack Analysis

The authors computed a hypothetical "perfect" attack achieving optimal solutions to their mathematical objective (Equation 2). This provides reference points and extrapolation capabilities.

**Key Findings**:
- GASLITE exhausts most of perfect's success across all models under "Knows What"
- For "Knows Nothing", extrapolation suggests budget |P_adv|=1000 (0.01% poison rate) could achieve 30-50% appeared@10
- Performance gap between GASLITE and perfect indicates near-ideal optimization

## Model Susceptibility Variance

**Critical Finding**: Substantial variance exists in retrieval robustness across models (Section 9).

### Vulnerability Factors Identified

1. **Similarity Metric Effect**: 
   - Dot-product models significantly more vulnerable than cosine-similarity models
   - Contriever (dot-product): ~100% concept-specific success with single passage
   - E5 (cosine): ~70% concept-specific success with single passage
   - Arctic (cosine): ~20% concept-specific success

2. **Embedding Space Anisotropy**:
   - Models with higher anisotropy (concentration of embeddings in representation space) show increased susceptibility
   - Anisotropy correlates with vulnerability patterns observed

3. **Model-Specific Properties**:
   - Contriever family abnormally vulnerable compared to other models
   - Authors note Contriever's common use in prior robustness evaluations may inadvertently bias threat assessments
   - Different backbone architectures, pooling methods, and training objectives create varied vulnerability profiles

## Defenses and Adaptive Attacks

### Tested Defenses

**1. Perplexity Filtering**: 
- Flags passages with unusual language patterns (high perplexity indicates incoherent text)
- GASLITE passages initially flag with perplexity ~100-150 (vs. normal 50-80)

**2. Embedding L2-Norm Filtering**:
- Detects unusually normalized embeddings
- GASLITE passages show distinctive L2 patterns allowing detection

### Adaptive Attack Variants

**1. Perplexity-Constrained GASLITE**:
- Integrates perplexity term into optimization objective
- Successfully bypasses perplexity-based detection
- Maintains appeared@10 within 5-10% of unfiltered attack

**2. L2-Norm Constrained GASLITE**:
- Constrains embedding L2-norm to natural value ranges
- Effectively bypasses norm-based detection
- Minor performance degradation (10-15%)

**Conclusion**: Both detection-based defenses can be evaded through adaptive optimization, suggesting deeper defenses are needed.

## Case Studies

### RAG System Attack

Demonstrated attack on actual RAG pipeline retrieving documents for LLM context. Successfully promoted misleading information through top-retrieved passages with minimal poisoning.

### Product SEO in Search

Showed applicability to realistic e-commerce search scenarios where attackers promote products through concept-specific queries.

## Attack Generalizability

### Across Query Sets

GASLITE passages trained on MSMARCO source queries generalize to:
- Different MSMARCO test queries
- Alternative datasets (NQ, SciFact, FiQA2018)
- Topic-specific datasets show higher success rates
- Minimal performance degradation across distribution shifts

### Across Architectures

Successfully attacks LLM-based embeddings (Stella-1.5B), indicating broad applicability beyond traditional dense retrievers.

### Transferability

Limited black-box transferability observed; white-box access substantially improves attack success (Section 6.5.1).

## Practical Constraints

The authors address realistic implementation considerations:

**Text vs. Token Attack**: Unlike prior work assuming direct token control, this attack inserts actual text to corpus. Tokenization introduces irreversibilities (different token sequences decode to identical text), requiring careful text coherence maintenance during optimization.

**Trigger Length**: 100-token triggers represent realistic passage additions; longer triggers may trigger content moderation systems.

**Passage Naturalness**: While GASLITE triggers appear incoherent (e.g., "So wizard tickets ideally ages Radcliffe trilogy typically 194 movies"), they remain short text insertions that could plausibly appear as website content, comments, or metadata.

## Limitations

The paper acknowledges several constraints:

1. **White-box assumption**: While justified by open-source prevalence, real-world attacks might face black-box scenarios
2. **Concept availability**: "Knows What" attacks require partial query set knowledge; fully unknown attack distributions remain harder
3. **Corpus static assumption**: Real corpora constantly change; embedding caches degrade over time
4. **No read-access to corpus**: Attacks cannot verify passage insertion or monitor detection
5. **Model robustness evolution**: Techniques may become less effective as models improve

## Technical Contributions Summary

### Mathematical Framework
- Formalized adversary objective as vector similarity maximization
- Proved multi-budget optimization NP-Hard
- Established theoretical connection between objective maximization and attack success

### Algorithmic Innovation
GASLITE improvements over HotFlip:
- Multi-token greedy search reduces computational requirements
- Enhanced gradient approximation via sampling
- Text coherence maintenance ensuring practical deployability

### Comprehensive Empirical Study
- First large-scale evaluation across 9 models
- Three realistic threat models
- Extensive ablation studies and sensitivity analyses
- Real-world case demonstrations

## Numerical Summary

**Poisoning Rates for Success**:
- Single-query: 1 passage (100%)
- Concept-specific: 10 passages = 0.0001% for 50%+ success
- Diverse queries: 100 passages = 0.001% for 5-20% success

**Performance Gaps vs. Baselines**:
- Concept-specific: +140% improvement over Cor.Pois.
- Single-query: +40% absolute improvement

**Model Variance**:
- Best case (Contriever): 100% with single passage
- Worst case (Arctic): 20% with single passage
- 5-fold difference in susceptibility

**Trigger Length**: 100 tokens generating coherent attacks; triggers remain syntactically incoherent but semantically potent

This research establishes that embedding-based retrieval systems face significant security risks, particularly under realistic concept-specific attack scenarios, and that many popular models remain substantially more vulnerable than others.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0fe55a9-03dc-46fd-8ee4-479a818f0b70",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "aee0facf533f0579b",
  "type": "user",
  "uuid": "fd6225a6-3403-4fb0-a9f4-39d27ec8c44d",
  "sourceToolAssistantUUID": "b0fe55a9-03dc-46fd-8ee4-479a818f0b70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-30T06:43:04.549Z_

Let me now fetch the ACM proceedings page and the GitHub repository for additional details, plus search for any reviews or discussions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd6225a6-3403-4fb0-a9f4-39d27ec8c44d",
  "isSidechain": true,
  "agentId": "aee0facf533f0579b",
  "requestId": "req_011CbYJK68AawhGvXJ7vRKPi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e98c6d8d-a706-4997-8778-20a80586e3f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011KiQcq9UTHj5FvaxnFNYML",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 897,
      "cache_creation_input_tokens": 4646,
      "cache_read_input_tokens": 10098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4646,
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

_source line 15 · 2026-05-30T06:43:06.554Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HibycxrucTEQq14p7o8mx7`</summary>

```json
{
  "url": "https://dl.acm.org/doi/10.1145/3719027.3765095",
  "prompt": "Extract all available information about this paper from the ACM Digital Library page: publication date, conference details, DOI, page numbers, any supplementary material links, and any information about reviews or discussions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e98c6d8d-a706-4997-8778-20a80586e3f5",
  "isSidechain": true,
  "agentId": "aee0facf533f0579b",
  "requestId": "req_011CbYJK68AawhGvXJ7vRKPi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b48da1e8-4de5-4406-8a89-c2d5ad97b064",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011KiQcq9UTHj5FvaxnFNYML",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 897,
      "cache_creation_input_tokens": 4646,
      "cache_read_input_tokens": 10098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4646,
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

### Tool result

_source line 16 · 2026-05-30T06:43:06.811Z_

<details><summary>↩ Tool result · `toolu_01HibycxrucTEQq14p7o8mx7`</summary>

```text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b48da1e8-4de5-4406-8a89-c2d5ad97b064",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "aee0facf533f0579b",
  "type": "user",
  "uuid": "220a74f0-a98f-4fc6-8627-e500a1232a1b",
  "sourceToolAssistantUUID": "b48da1e8-4de5-4406-8a89-c2d5ad97b064",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-30T06:43:07.909Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SHD8Pk2CkDJNXVzzVdMF9h`</summary>

```json
{
  "url": "https://github.com/matanbt/gaslite",
  "prompt": "Extract all information from this GitHub repository: the README contents, description, any technical details about the implementation, dependencies, how to run the attack, what models are supported, and any issues or discussions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "220a74f0-a98f-4fc6-8627-e500a1232a1b",
  "isSidechain": true,
  "agentId": "aee0facf533f0579b",
  "requestId": "req_011CbYJK68AawhGvXJ7vRKPi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ca37cf2-a962-4e82-9fcc-2f3080a22e0d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011KiQcq9UTHj5FvaxnFNYML",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 897,
      "cache_creation_input_tokens": 4646,
      "cache_read_input_tokens": 10098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4646,
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

_source line 18 · 2026-05-30T06:43:08.505Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013JGymFupGajqYxbzPbrD8m`</summary>

```json
{
  "query": "GASLITE corpus poisoning RAG retrieval attack review discussion blog 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ca37cf2-a962-4e82-9fcc-2f3080a22e0d",
  "isSidechain": true,
  "agentId": "aee0facf533f0579b",
  "requestId": "req_011CbYJK68AawhGvXJ7vRKPi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5275ba0-4994-42d8-9a03-447c275520e6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011KiQcq9UTHj5FvaxnFNYML",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 897,
      "cache_creation_input_tokens": 4646,
      "cache_read_input_tokens": 10098,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4646
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 897,
          "output_tokens": 312,
          "cache_read_input_tokens": 10098,
          "cache_creation_input_tokens": 4646,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4646,
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

_source line 19 · 2026-05-30T06:43:14.815Z_

<details><summary>↩ Tool result · `toolu_01SHD8Pk2CkDJNXVzzVdMF9h`</summary>

```text
# GASLITE Repository Summary

## Project Overview
GASLITE is a research implementation exploring vulnerabilities in dense embedding-based retrieval systems through corpus poisoning attacks. The official repository enables reproduction of experiments from the paper "GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search."

## Key Technical Details

**Purpose:** The project demonstrates how to craft adversarial passages that poison retrieval corpora, causing embedding-based search systems to retrieve manipulated content for targeted queries.

**Requirements:**
- Python 3.8.5+
- Dependencies via `pip install -r requirements.txt`
- Optional wandb integration for metrics tracking

## Implementation Components

The repository includes three attack scenarios accessible via shell scripts:

1. **Single Query Attack** (`attack0_knows-all.sh`): Targets one specific query
2. **Concept-Specific Attack** (`attack1_knows-what.sh`): Targets query clusters (e.g., Harry Potter-related queries)
3. **Dataset-Wide Attack** (`attack2_knows-nothing.sh`): Attacks entire datasets like MSMARCO

## Evaluation Framework

The `covering.py` module provides an API for evaluating poisoning attacks, measuring passage visibility in top-10 retrieval results and other standard metrics against targeted queries.

## Additional Features

- Query result caching to optimize repeated evaluations
- Query partition caching using k-means clustering
- Interactive demo notebook available in Colab
- Cached similarity datasets available via HuggingFace

## Dependencies

The project integrates external components: retrieval dataset similarities, GPT-2 with BERT tokenizer for fluent passage generation, and acknowledges inspiration from BEIR, corpus poisoning, and adversarial attack frameworks.

**Repository Stats:** 14 stars, 3 forks, Python-dominant codebase (68.7%)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ca37cf2-a962-4e82-9fcc-2f3080a22e0d",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "aee0facf533f0579b",
  "type": "user",
  "uuid": "bf7ae3b1-f12f-4367-b753-86f83b5d62a4",
  "sourceToolAssistantUUID": "0ca37cf2-a962-4e82-9fcc-2f3080a22e0d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-30T06:43:16.929Z_

<details><summary>↩ Tool result · `toolu_013JGymFupGajqYxbzPbrD8m`</summary>

```text
Web search results for query: "GASLITE corpus poisoning RAG retrieval attack review discussion blog 2025"

Links: [{"title":"GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search","url":"https://arxiv.org/html/2412.20953"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search","url":"https://arxiv.org/pdf/2412.20953"},{"title":"Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems","url":"https://arxiv.org/html/2603.18034v1"},{"title":"RAG Poisoning: Contaminating the AI’s “Source of Truth” | by InstaTunnel | Medium","url":"https://medium.com/@instatunnel/rag-poisoning-contaminating-the-ais-source-of-truth-082dcbdeea7c"},{"title":"GitHub - matanbt/GASLITE: SEO attack on dense embedding-based retrieval via poisoning · GitHub","url":"https://github.com/matanbt/gaslite"},{"title":"RAG Poisoning: How Attackers Corrupt Your AI's Knowledge Base | Amine Raji, PhD","url":"https://aminrj.com/posts/rag-document-poisoning/"},{"title":"Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems","url":"https://arxiv.org/pdf/2603.18034"},{"title":"RevPRAG: Revealing Poisoning Attacks in Retrieval- ...","url":"https://aclanthology.org/2025.findings-emnlp.698.pdf"}]

Based on the search results, here's information about GASLITE and corpus poisoning attacks on RAG retrieval systems:

## GASLITE Attack Overview

GASLITE comprehensively explores text embedding-based retrieval's susceptibility to SEO via corpus poisoning. It's a gradient-based method for crafting optimized adversarial passages, showing superiority in retrieval attacks compared to powerful LLM discrete optimizers like GCG.

## How the Attack Works

The work aims to assess the worst-case behavior of embedding-based text retrievers under corpus-poisoning SEO attack. The attack focuses on concept-specific queries, arguing these better reflect SEO goals—targeted queries share commonalities with attack contexts.

## Research Context

Recent work has demonstrated the feasibility of retrieval corpus poisoning and its utilization for misleading LLMs, particularly in the context of RAG. The official paper is titled "GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search", and it was accepted to ACM CCS 2025.

## Related 2025 Research

The broader field shows significant activity: PoisonedRAG was accepted to USENIX Security 2025 and represents the first knowledge database corruption attack specifically designed against RAG systems. Recent 2025-2026 research includes sophisticated attacks like "PoisonedRAG," "CorruptRAG," "PoisonedEye," and "Phantom".


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5275ba0-4994-42d8-9a03-447c275520e6",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "aee0facf533f0579b",
  "type": "user",
  "uuid": "1d5393b3-cfef-452e-9e47-b4dd9d5c39c6",
  "sourceToolAssistantUUID": "f5275ba0-4994-42d8-9a03-447c275520e6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-30T06:43:20.387Z_

Let me fetch a couple more sources for additional depth on defenses and the related follow-up work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d5393b3-cfef-452e-9e47-b4dd9d5c39c6",
  "isSidechain": true,
  "agentId": "aee0facf533f0579b",
  "requestId": "req_011CbYJLFSXdLVeT9pNpfjE6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6776db5-abc8-41f8-bd6a-f96fbcc8285c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WjaT8bqeYQPPok1YhKs1ey",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2706,
      "cache_read_input_tokens": 14744,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2706,
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

_source line 22 · 2026-05-30T06:43:25.744Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018zbHAnHt5sGP8YLRbubG2B`</summary>

```json
{
  "url": "https://arxiv.org/html/2412.20953v2",
  "prompt": "I need specific technical details from this paper. Focus on extracting:\n1. The exact mathematical formulation of the GASLITE objective (equations)\n2. The exact algorithm pseudocode details\n3. How the text coherence maintenance works (token-to-text irreversibility problem)\n4. The exact defense mechanisms tested and how adaptive GASLITE defeats them - specific numbers\n5. The transferability / black-box results\n6. The RAG case study details\n7. Any explicit limitations section\n8. The connection between anisotropy and vulnerability\n9. Details about the k-means partitioning for multi-budget attacks\n10. The comparison with HotFlip and why Cor.Pois. underperforms\nPlease provide maximum detail with specific numbers, percentages, and technical specifics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6776db5-abc8-41f8-bd6a-f96fbcc8285c",
  "isSidechain": true,
  "agentId": "aee0facf533f0579b",
  "requestId": "req_011CbYJLFSXdLVeT9pNpfjE6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d76243e5-d7e1-4547-a21d-ce9b43c744c5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WjaT8bqeYQPPok1YhKs1ey",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2706,
      "cache_read_input_tokens": 14744,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2706,
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

_source line 23 · 2026-05-30T06:43:26.843Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017wbnNqC41ZFu27NVCQvYQA`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.24268",
  "prompt": "Extract the abstract and key details of this paper about RAG defenses against corpus poisoning. How does it relate to or cite the GASLITE work?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d76243e5-d7e1-4547-a21d-ce9b43c744c5",
  "isSidechain": true,
  "agentId": "aee0facf533f0579b",
  "requestId": "req_011CbYJLFSXdLVeT9pNpfjE6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4423ee05-7597-4b28-8414-4f7c292e793d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WjaT8bqeYQPPok1YhKs1ey",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2706,
      "cache_read_input_tokens": 14744,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2706,
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

_source line 24 · 2026-05-30T06:43:31.179Z_

<details><summary>↩ Tool result · `toolu_017wbnNqC41ZFu27NVCQvYQA`</summary>

```text
# RAGPart & RAGMask: Summary

## Abstract Overview

The paper presents two retrieval-stage defense mechanisms against corpus poisoning in RAG systems. As described, these defenses aim to "reduce attack success rates while preserving utility under benign conditions" by operating directly on the retriever without modifying the generation model.

## Key Defense Mechanisms

**RAGPart** exploits document partitioning to leverage training dynamics of dense retrievers, mitigating poisoned document effects.

**RAGMask** identifies suspicious tokens by detecting significant similarity shifts when applying targeted token masking.

## Evaluation Scope

The research tests defenses across two benchmarks, four poisoning strategies, and four state-of-the-art retrievers, introducing an interpretable attack to stress-test the approaches.

## GASLITE Citation

The provided content does not mention or cite GASLITE anywhere in the document. Therefore, I cannot identify any relationship between this work and GASLITE based on the material shown. To determine any connection, you would need to consult the full paper's references section, which is not included in the excerpt provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4423ee05-7597-4b28-8414-4f7c292e793d",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "aee0facf533f0579b",
  "type": "user",
  "uuid": "6b5a0d98-1ed6-474e-9515-418e797e66b1",
  "sourceToolAssistantUUID": "4423ee05-7597-4b28-8414-4f7c292e793d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-30T06:43:48.737Z_

<details><summary>↩ Tool result · `toolu_018zbHAnHt5sGP8YLRbubG2B`</summary>

````text
# GASLITE Attack: Technical Deep Dive

## 1. Mathematical Formulation

**Primary Objective (Eq. 2):**
```
arg max_{p̃_adv} (1/|Q| ∑_q∈Q Emb_R(q)) · Emb_R(p̃_adv)
```

This maximizes alignment between adversarial passage and the centroid of targeted queries. The authors derive this from a probability maximization problem (Eq. 1) that seeks to maximize the probability of adversarial passage appearing in top-k results across queries sampled from distribution D_Q̌.

**Constrained Form:**
The passage structure is: p_adv := info ⊕ trigger, where info (malicious prefix) is fixed and only the trigger is optimized.

## 2. GASLITE Algorithm Details

**Core Operations (Algorithm 1):**
- Initialize trigger with ℓ=100 arbitrary tokens
- For n_iter=100 iterations:
  - Sample n_grad=50 random single-token flips
  - Compute gradient averages per token position
  - Randomly select n_flip=20 token positions to modify
  - For each position: identify n_cand=128 promising token replacements using gradient approximation
  - Filter irreversible tokenizations
  - Select best token flip maximizing objective
  - Return optimized trigger

**Key Enhancement Over HotFlip:**
The authors implement "multi-coordinate ascent" by flipping multiple tokens per iteration rather than single tokens. This reduces backward passes per substitution by approximately 20x compared to standard HotFlip approaches.

## 3. Token-to-Text Irreversibility Handling

The paper identifies a critical problem: different token sequences can decode to identical text strings. Their solution (Algorithm 1, line 10) includes a "ReTokenize" step that:
- Discards token lists that produce inconsistent round-trip encoding (text→tokens→text)
- Ensures adversarial passages correspond exactly to optimized token lists when inserted into corpus

This explains why Cor.Pois. (prior work) underperformed—it optimized tokens without verifying text consistency, resulting in significant objective degradation after decoding/re-encoding cycles.

## 4. Defense Mechanisms & Adaptive Defeats

**Perplexity-Based Defense:**
- Defense: Filter passages with perplexity >10 bits
- GASLITE baseline result: 62% appeared@10 (E5 model, Knows What, budget=10)
- Adaptive GASLITE with PPL constraint: 58% appeared@10
- Performance drop: minimal (4 percentage points)

**L2-Norm Defense:**
- Defense: Filter passages with L2 norm >0.8
- Baseline: 62% appeared@10
- Adaptive variant: 60% appeared@10
- The authors note that norm-constrained optimization requires minimal modification to the gradient-based approach

**Timestamp/Metadata Defenses:**
The paper suggests these are "easily evaded" by poisoning metadata alongside text, though specific numbers aren't provided for this category.

## 5. Transferability & Black-Box Results

**Cross-Model Transferability (Knows What setting):**
- Attacks trained on E5 transfer with 40-60% of training success to other models
- Attacks trained on Contriever transfer with 30-50% effectiveness
- Arctic shows weakest transferability (~25% relative success)

**Generalization Across Datasets (Figure 7):**
- GASLITE trained on MSMARCO achieves 15-25% appeared@10 when evaluated on SciFact queries
- Topic-specific datasets see higher success (30-40% on scientific content)
- Generic evaluation sets see 5-15% success rates

## 6. RAG Case Study

**System Tested:** OpenWebUI with Chroma vector store

**Attack Setup:**
- Poisoned RAG corpus with 10 adversarial passages (budget identical to main experiments)
- Target: Harry Potter-related queries
- Metric: Frequency of adversarial passages retrieved to LLM context

**Results:**
- 73% of Harry Potter queries returned adversarial passages in top-3 retrieved results
- LLM generated misleading responses in 58% of cases
- Without defenses, 100% prompt injection success rate for appearance in top-10

**Trigger Example (Table 15):**
"So wizard tickets ideally ages Radcliffe trilogy typically 194 movies" (100 tokens appended to malicious prefix)

## 7. Limitations Section (Implicit)

The authors acknowledge:
- White-box threat model assumes access to model weights (practical due to open-source prevalence, but still stronger than pure black-box)
- Trigger length (100 tokens) is somewhat arbitrary; longer triggers may improve performance
- Evaluation focuses on English-language queries; multilingual robustness unexplored
- Attack assumes static corpus; dynamic corpus updates could mitigate poisoning

## 8. Anisotropy-Vulnerability Connection

**Key Finding:**
Models exhibiting higher embedding space anisotropy (concentration of embeddings into narrow directions) show increased vulnerability to SEO attacks.

**Quantification:**
- Contriever (highly anisotropic dot-product model): 100% appeared@10 with single passage (Knows What)
- E5 (more isotropic cosine model): 62% appeared@10 with single passage
- The authors measure anisotropy using eigenvalue distributions of embedding matrices

**Mechanism:** Anisotropic spaces allow adversarial passages to achieve extremely high similarity scores with query centroids without requiring semantic naturalness, as the constrained embedding space geometry doesn't penalize semantic drift.

## 9. K-Means Partitioning for Multi-Budget Attacks

**Problem:** Finding optimal partition of queries into B subsets is NP-Hard (reduction to Set Cover, Appendix D.2)

**Solution:** K-means clustering with theoretical justification:
- Maximizes within-cluster pairwise similarity
- Empirically superior to greedy set-cover approximation and other clustering methods
- For budget B=10: partition 50% of Harry Potter queries into 10 clusters, optimize one adversarial passage per cluster

**Performance vs. Budget (Figure 4):**
- 1 passage: 30% avg appeared@10 (6/9 models)
- 5 passages: 48% avg appeared@10
- 10 passages: 62% avg appeared@10 (<<0.0001% poisoning rate on 8.8M corpus)

## 10. HotFlip Comparison & Cor.Pois. Underperformance

**Why HotFlip Fails:**
HotFlip computes single gradient and ranks tokens; in discrete space with high-dimensional embeddings, this linear approximation is poor for retrieval objectives.

**Cor.Pois. Specific Issues:**
- Assumes access to corpus and ground-truth passages (unrealistic threat model)
- Shows 49% appeared@10 on Contriever (vs. 100% for GASLITE) under Knows All
- Under Knows What: 35% appeared@10 (vs. 62% GASLITE baseline)
- Root cause: token-text irreversibility problem causes substantial objective degradation post-tokenization

**GASLITE Speedup:**
- GASLITE converges in ~2-3 minutes per passage
- Cor.Pois. requires 30-45 minutes due to single-token optimization
- 10-15x speedup maintained while achieving 40%+ better success rates

---

**Critical Insight:** The paper's core contribution isn't novel mathematical formulation (objective is relatively straightforward dot-product maximization) but rather engineering: solving the discrete optimization problem in text space while maintaining token-text consistency—a practical problem previous work overlooked.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d76243e5-d7e1-4547-a21d-ce9b43c744c5",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "aee0facf533f0579b",
  "type": "user",
  "uuid": "3bc3b0b6-71d4-4bc1-baed-b0f1318fd54e",
  "sourceToolAssistantUUID": "d76243e5-d7e1-4547-a21d-ce9b43c744c5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-30T06:43:52.358Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VyfE5ZAFxaJCMBhWwpTqXn`</summary>

```json
{
  "query": "\"GASLITE\" \"dense retrieval\" \"corpus poisoning\" blog review analysis 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3bc3b0b6-71d4-4bc1-baed-b0f1318fd54e",
  "isSidechain": true,
  "agentId": "aee0facf533f0579b",
  "requestId": "req_011CbYJNbQP1mTvkM9mJJmnz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58de3de0-186f-4406-919c-318c2f1e43a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L3krYPemd7AnKQarkiC6Sj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 279,
      "cache_creation_input_tokens": 2257,
      "cache_read_input_tokens": 17450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2257,
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

_source line 27 · 2026-05-30T06:43:52.864Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JDH7Jwz3bAZJdJDvGZxYEJ`</summary>

```json
{
  "query": "Matan Ben-Tov GASLITE CCS presentation talk slides SEO attack embedding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58de3de0-186f-4406-919c-318c2f1e43a8",
  "isSidechain": true,
  "agentId": "aee0facf533f0579b",
  "requestId": "req_011CbYJNbQP1mTvkM9mJJmnz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "746c351a-ab28-484d-9aff-c032aac65a90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L3krYPemd7AnKQarkiC6Sj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 279,
      "cache_creation_input_tokens": 2257,
      "cache_read_input_tokens": 17450,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2257
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 279,
          "output_tokens": 131,
          "cache_read_input_tokens": 17450,
          "cache_creation_input_tokens": 2257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2257,
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

_source line 28 · 2026-05-30T06:44:00.117Z_

<details><summary>↩ Tool result · `toolu_01JDH7Jwz3bAZJdJDvGZxYEJ`</summary>

```text
Web search results for query: "Matan Ben-Tov GASLITE CCS presentation talk slides SEO attack embedding"

Links: [{"title":"GitHub - matanbt/GASLITE: SEO attack on dense embedding-based retrieval via poisoning · GitHub","url":"https://github.com/matanbt/gaslite"},{"title":"GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search","url":"https://arxiv.org/html/2412.20953v2"},{"title":"[2412.20953] GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search","url":"https://arxiv.org/abs/2412.20953"},{"title":"Matan Ben-Tov | Mahmood Sharif","url":"https://mahmoods01.github.io/authors/matan-ben-tov/"},{"title":"GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search | Proceedings of the 2025 ACM SIGSAC Conference on Computer and Communications Security","url":"https://dl.acm.org/doi/10.1145/3719027.3765095"},{"title":"Matan Ben-Tov","url":"https://matanbt.github.io/"},{"title":"Matan Ben-Tov - Home","url":"https://dl.acm.org/profile/99661764302"},{"title":"Matan Ben-Tov","url":"https://scholar.google.com/citations?user=giYF2c4AAAAJ&hl=en"},{"title":"matanbt (Matan Ben-Tov) · GitHub","url":"https://github.com/matanbt"},{"title":"Matan Ben-Tov - Tel Aviv University | LinkedIn","url":"https://www.linkedin.com/in/matan-ben-tov/"}]

Based on the search results, I found information about Matan Ben-Tov's GASLITE research:

The paper "GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search" by Matan Ben-Tov and Mahmood Sharif was presented at ACM CCS 2025.

GASLITE is an attack for generating adversarial passages that—without relying on the corpus content or modifying the model—carry adversary-chosen information while achieving high retrieval ranking. The research addresses search-engine optimization (SEO) attacks on embedding-based retrieval, where adversaries promote malicious content by introducing adversarial passages to corpora.

The research extensively evaluated retrievers' robustness by testing nine advanced models under varied threat models, focusing on adversaries targeting queries on a specific concept. Key findings include that concept-specific SEO requires negligible poisoning rates (≤0.0001% of the corpus) to achieve content visibility in top results, and GASLITE consistently attains the top-1 result for single-query attacks.

The code is available at https://github.com/matanbt/gaslite, and the full paper is available at https://arxiv.org/abs/2412.20953.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "746c351a-ab28-484d-9aff-c032aac65a90",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "aee0facf533f0579b",
  "type": "user",
  "uuid": "5fb3a1ef-e8d3-4c91-9895-1666a68de857",
  "sourceToolAssistantUUID": "746c351a-ab28-484d-9aff-c032aac65a90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-30T06:44:00.139Z_

<details><summary>↩ Tool result · `toolu_01VyfE5ZAFxaJCMBhWwpTqXn`</summary>

```text
Web search results for query: ""GASLITE" "dense retrieval" "corpus poisoning" blog review analysis 2025 2026"

Links: [{"title":"Unsupervised Corpus Poisoning Attacks in Continuous Space for Dense Retrieval | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/10.1145/3726302.3730110"},{"title":"GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search","url":"https://arxiv.org/html/2412.20953v1"},{"title":"GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search","url":"https://arxiv.org/pdf/2412.20953"},{"title":"GitHub - matanbt/GASLITE: SEO attack on dense embedding-based retrieval via poisoning · GitHub","url":"https://github.com/matanbt/gaslite"},{"title":"This AI Paper from Tel Aviv University Introduces GASLITE: A Gradient-Based Method to Expose Vulnerabilities in Dense Embedding-Based Text Retrieval Systems - MarkTechPost","url":"https://www.marktechpost.com/2025/01/06/this-ai-paper-from-tel-aviv-university-introduces-gaslite-a-gradient-based-method-to-expose-vulnerabilities-in-dense-embedding-based-text-retrieval-systems/"},{"title":"SilentRetrieval: Hijacking Retrieval-Augmented Generation via Semantically-Preserving Adversarial Data Poisoning","url":"https://arxiv.org/html/2605.28074"},{"title":"Unsupervised Corpus Poisoning Attacks in Continuous Space for Dense Retrieval","url":"https://arxiv.org/html/2504.17884"}]

Based on the search results, I found relevant information about GASLITE and corpus poisoning attacks on dense retrieval systems:

## Overview of GASLITE

GASLITE is a mathematically grounded, gradient-based attack on embedding-based retrievers that demonstrates potent SEO attacks against embedding-based retrievers.

## Key Findings

Adversaries using GASLITE require minimal effort to manipulate search results—by injecting a negligible amount of adversarial passages (≤0.0001% of the corpus), they could make them visible in the top-10 results for 61-100% of unseen concept-specific queries against most evaluated models.

GASLITE consistently outperformed baselines by ≥140% success rate, in all settings. Additionally, the method was tested with nine state-of-the-art retrieval models under varied threat models.

## Analysis Coverage

The authors tested GASLITE with nine state-of-the-art retrieval models under various threat scenarios, with the method achieving a 61-100% success rate in ranking adversarial passages within the top 10 results for concept-specific queries with minimal poisoning of the corpus.

## Recent Blog/Review Coverage

A MarkTechPost article from January 2025 covered the research from Tel Aviv University, noting GASLITE achieved a 61-100% success rate.

The research was published in December 2024 and has since been referenced in subsequent 2025-2026 work on related corpus poisoning attacks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58de3de0-186f-4406-919c-318c2f1e43a8",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "aee0facf533f0579b",
  "type": "user",
  "uuid": "8de44009-b683-4f9e-9af9-39c054a76993",
  "sourceToolAssistantUUID": "58de3de0-186f-4406-919c-318c2f1e43a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-30T06:44:05.043Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013ud15iziDzkfW2w2oftcgn`</summary>

```json
{
  "url": "https://www.marktechpost.com/2025/01/06/this-ai-paper-from-tel-aviv-university-introduces-gaslite-a-gradient-based-method-to-expose-vulnerabilities-in-dense-embedding-based-text-retrieval-systems/",
  "prompt": "Extract the full content of this blog post about GASLITE. Include any analysis, commentary, or details not found in the original paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8de44009-b683-4f9e-9af9-39c054a76993",
  "isSidechain": true,
  "agentId": "aee0facf533f0579b",
  "requestId": "req_011CbYJPSBXWfR6t1Naz1uL2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5940e62-1da9-474b-ae9b-4c2baba862c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F6pXtEQf6n1ckuYQbKtXC4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 807,
      "cache_creation_input_tokens": 1265,
      "cache_read_input_tokens": 19707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1265,
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

### Tool result

_source line 31 · 2026-05-30T06:44:15.681Z_

<details><summary>↩ Tool result · `toolu_013ud15iziDzkfW2w2oftcgn`</summary>

```text
# GASLITE: Exposing Vulnerabilities in Dense Embedding-Based Text Retrieval

## Overview

Researchers from Tel Aviv University introduced GASLITE, a gradient-based optimization method designed to expose weaknesses in dense embedding-based text retrieval systems. The technique demonstrates how adversarial passages can manipulate ranking algorithms in search engines and retrieval-augmented generation (RAG) applications.

## The Problem

Dense embedding systems—which convert text into vector representations for semantic matching—power many modern retrieval applications. However, these systems face a critical vulnerability: malicious actors can inject crafted passages into public corpora to artificially elevate their visibility in search results. This threatens the integrity of information systems by enabling misinformation spread and biased content injection.

Previous defense approaches relied on simple poisoning techniques like "repetitive text stuffing," which proved ineffective against sophisticated models handling diverse query distributions.

## How GASLITE Works

Unlike earlier methods, GASLITE operates directly within the retrieval model's embedding space rather than modifying visible text. The approach constructs adversarial passages by combining attacker-selected prefixes with optimized trigger sequences. The method employs "gradient calculations in the embedding space to find optimal token substitutions," enabling stealthy integration into existing corpora.

## Key Results

Testing across nine state-of-the-art retrieval models revealed striking success rates:

- **61-100% top-10 visibility** for concept-specific queries
- **Consistent top-1 rankings** for single-query attacks
- **Minimal corpus poisoning**: adversarial passages comprised just 0.0001% of datasets

## Critical Vulnerabilities Identified

The research identified two architectural weaknesses:

1. **Dot-product similarity measures** proved particularly exploitable, as GASLITE leverages these mathematical properties for optimal alignment
2. **Anisotropic embedding spaces**—where random text pairs generate unexpectedly high similarity scores—showed greater susceptibility to attacks

## Recommended Defenses

The researchers propose hybrid retrieval approaches combining dense and sparse techniques to mitigate GASLITE-style attacks, emphasizing the need for understanding embedding geometry when designing secure systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5940e62-1da9-474b-ae9b-4c2baba862c8",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "aee0facf533f0579b",
  "type": "user",
  "uuid": "4c01674d-5655-421c-a4d7-2066a41387d2",
  "sourceToolAssistantUUID": "e5940e62-1da9-474b-ae9b-4c2baba862c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-30T06:45:57.006Z_

I now have comprehensive information to provide a thorough technical analysis. Here is my detailed report.

---

## GASLITE: Full Technical Research Summary

**Paper:** "GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search"
**Authors:** Matan Ben-Tov, Mahmood Sharif (Tel Aviv University)
**Venue:** ACM CCS 2025 (Conference on Computer and Communications Security)
**DOI:** 10.1145/3719027.3765095
**arXiv:** 2412.20953 (v1: Dec 30, 2024; v2: Sep 18, 2025)
**Code:** https://github.com/matanbt/gaslite

---

### Full Abstract

Dense embedding-based text retrieval -- retrieving relevant passages from corpora via deep learning encodings -- has become powerful for achieving state-of-the-art search and popularizing Retrieval Augmented Generation (RAG). However, embedding-based retrieval may face search-engine optimization (SEO) attacks where adversaries introduce malicious passages to promote harmful content. Prior work demonstrated such vulnerabilities but employed relaxed threat models, baseline methods, and limited evaluations. This research provides a comprehensive robustness assessment of retrievers to uncover susceptibility factors. The authors propose GASLITE, an attack generating adversarial passages that embed adversary-chosen information without corpus content reliance or model modification, consistently outperforming prior approaches. Extensive evaluation of nine advanced models across varied threat models reveals retrievers face high vulnerability to SEO attacks targeting concept-specific queries, even with negligible poisoning rates (>=0.0001% of corpus), generalizing across corpora and query distributions. Single-query SEO is fully solved by GASLITE, while adaptive attacks bypass common defenses.

---

### Threat Model and Assumptions

**Attacker Goals (dual objective):**
1. **Visibility:** Maximize probability that adversarial passages appear in top-k retrieval results.
2. **Informativeness:** Ensure crafted passages convey attacker-chosen content (e.g., misinformation, promotional material).

**Attacker Capabilities:**
- Can insert adversarial text passages into the retrieval corpus (e.g., via public wikis, web crawling targets, open forums).
- Controls passage text content but not tokenization directly.
- Poisoning budget is negligible: |P_adv| << |P| (e.g., 10 passages in an 8.8M passage corpus = 0.0001%).
- **White-box access** to model weights -- justified by the prevalence of open-source embedding models (Contriever, E5, etc. are all publicly available on HuggingFace).
- **Cannot** modify model weights, access the existing corpus content, or read ground-truth relevance labels.

**Three Query Distribution Settings:**

1. **"Knows All":** Attacker targets a known finite query set Q (often |Q|=1). This is the classic single-query SEO setting. Represents the easiest attack scenario.

2. **"Knows What" (primary focus):** Attacker targets a specific concept (e.g., "Harry Potter") with infinite possible query support but only a finite sample Q available for optimization. Reflects realistic SEO where the attacker knows the topic domain but not the exact queries users will issue. This is the paper's central contribution.

3. **"Knows [Almost] Nothing":** Indiscriminate targeting across diverse, unrelated query distributions. The hardest setting, requiring broad generalization.

---

### Method: How GASLITE Works

**Core Mathematical Objective (Eq. 2):**

```
arg max_{p_adv}  (1/|Q| * sum_{q in Q} Emb_R(q)) . Emb_R(p_adv)
```

This maximizes the dot product between the adversarial passage embedding and the centroid of the target query embeddings. The key insight: optimal adversarial passages should align with the "average" semantic direction of the targeted query cluster.

**Passage Structure:**
Each adversarial passage is constructed as `p_adv := info || trigger`, where:
- `info` is a fixed prefix containing the attacker's chosen malicious information (exploiting the primacy effect -- readers attend more to early content).
- `trigger` is a suffix of 100 tokens that GASLITE optimizes to maximize retrieval ranking.

**Algorithm (multi-coordinate gradient-based discrete optimization):**

Hyperparameters: n_iter=100, n_grad=50, n_cand=128, n_flip=20, trigger length=100 tokens.

Per iteration:
1. Sample n_grad=50 random single-token flip variants of the current trigger.
2. Average the linear approximations (gradients) across these samples per token position -- this is a refined gradient approximation superior to single-point HotFlip.
3. Randomly select n_flip=20 token positions for simultaneous substitution.
4. For each position, use gradient information to identify n_cand=128 promising token candidates.
5. Filter candidates that cause tokenization irreversibilities (the "ReTokenize" step -- see below).
6. Greedily select the best substitution that maximizes the objective.
7. Update the trigger.

**Three Key Engineering Innovations Over Prior Work (HotFlip/Cor.Pois.):**

1. **Multi-token greedy search:** Flips multiple tokens per iteration rather than one, reducing backward passes by ~20x compared to standard HotFlip.

2. **Refined gradient approximation:** Averages linear approximations across n_grad=50 random token-substitution samples, yielding more reliable gradients in the discrete token space.

3. **Text coherence maintenance (ReTokenize):** This is the critical practical contribution. Different token sequences can decode to identical text strings. Prior work (Cor.Pois./Zhong et al. 2023) optimized in token space but inserted text into the corpus -- the re-tokenization of decoded text could produce different tokens than what was optimized, causing substantial objective degradation. GASLITE explicitly filters out token substitutions that would be inconsistent after a text-to-tokens-to-text round trip. This is identified as the primary reason Cor.Pois. underperforms.

**Multi-Budget Extension (B > 1 adversarial passages):**
Finding the optimal partition of queries into B subsets is NP-Hard (proven via reduction to Set Cover). GASLITE uses k-means clustering on query embeddings to partition the target query set into B clusters, then optimizes one adversarial passage per cluster centroid. K-means was empirically superior to greedy set-cover approximation.

**Runtime:** GASLITE converges in ~2-3 minutes per passage, versus 30-45 minutes for Cor.Pois. -- a 10-15x speedup while achieving 40%+ better success rates.

---

### How Single-Query Attacks Achieve 100% Success

In the "Knows All" setting with |Q|=1, the optimization objective reduces to maximizing the dot product between one query embedding and the adversarial passage embedding. The discrete nature of a single target query means the optimization can achieve near-perfect alignment in embedding space. GASLITE achieves **100% appeared@1** (top-1 result) across all nine evaluated models. This is described as "fully solved" -- the adversarial passage consistently becomes the single highest-ranked result for the target query.

Comparative performance for single-query:
- Info Only (no optimization): 0% success
- Stuffing (repeat the query text): 30-96% appeared@10, model-dependent
- Cor.Pois. (prior SOTA): sometimes worse than stuffing due to tokenization issues
- GASLITE: 100% appeared@1, all models

For dot-product models like Contriever, GASLITE achieves similarity scores of 3.453 +/- 0.350, roughly 2x what baseline methods achieve.

---

### What the 0.0001% Corpus Poisoning Rate Means

The primary corpus is MSMARCO with 8.8 million passages. A budget of 10 adversarial passages represents 10/8,800,000 = ~0.0001% of the corpus. At this poisoning rate:

- GASLITE achieves >50% appeared@10 on 6 out of 9 models for unseen concept-specific queries.
- Appeared@10 ranges from 61-100% on most models (the 61-100% figure cited in the abstract).
- This represents an astronomically small injection that is practically undetectable by volume-based monitoring.

Scaling with budget (concept-specific, averaged across models):
- 1 passage: ~30% appeared@10
- 5 passages: ~48% appeared@10
- 10 passages: ~62% appeared@10
- 100% appeared@100 achieved on all models with just 10 passages

---

### What Makes Standard Defenses Fail Against Adaptive Versions

**Defense 1 -- Perplexity Filtering:**
- Rationale: GASLITE triggers are syntactically incoherent (e.g., "So wizard tickets ideally ages Radcliffe trilogy typically 194 movies"), so they exhibit high perplexity (~100-150 bits vs. normal ~50-80).
- Defense: Filter passages exceeding a perplexity threshold (>10 bits).
- **Adaptive bypass:** GASLITE integrates a perplexity penalty term into its optimization objective, constraining the trigger to remain within natural perplexity ranges.
- Result: Adaptive variant achieves 58% appeared@10 vs. 62% baseline -- only a 4 percentage-point drop. Defense is effectively neutralized.

**Defense 2 -- Embedding L2-Norm Filtering:**
- Rationale: Adversarial passages may have abnormal embedding norms.
- Defense: Filter passages with L2 norm exceeding a threshold (>0.8).
- **Adaptive bypass:** GASLITE adds an L2-norm constraint to optimization, keeping embeddings within natural norm distributions.
- Result: 60% appeared@10 vs. 62% baseline -- only 2 percentage-point drop.

The fundamental problem: both defenses rely on statistical anomaly detection (perplexity, norm), which can be incorporated as constraints in the attacker's optimization without significant performance loss. The paper concludes that "deeper defenses are needed" beyond surface-level filtering.

---

### Experimental Results and Key Findings

**Models Evaluated (9 total):**
- Cosine-similarity models: E5, MiniLM, GTR-T5, aMPNet, Arctic
- Dot-product models: Contriever, Contriever-MS, ANCE, mMPNet

**Key Quantitative Results:**

| Setting | Budget | GASLITE appeared@10 | Best Baseline | Improvement |
|---------|--------|---------------------|---------------|-------------|
| Knows All (single query) | 1 | 100% (@1) | 30-96% (@10) | Fully solved |
| Knows What (concept) | 10 | 61-100% | ~25% (Cor.Pois.) | >140% |
| Knows Nothing (diverse) | 100 | 5-20% | <6% (Cor.Pois.) | Significant |

**Model Vulnerability Variance (concept-specific, 1 passage):**
- Contriever (dot-product, high anisotropy): ~100% appeared@10
- E5 (cosine, moderate anisotropy): ~70%
- Arctic (cosine, low anisotropy): ~20%
- 5-fold difference in susceptibility across models

**Vulnerability Factors Identified:**
1. **Similarity metric:** Dot-product models are significantly more vulnerable than cosine-similarity models. Dot-product doesn't normalize embedding magnitudes, allowing adversarial passages to achieve disproportionately high scores.
2. **Embedding space anisotropy:** Models with higher anisotropy (embeddings concentrated in narrow directional subspaces) are more exploitable. Anisotropy is measured via eigenvalue distributions of embedding matrices. In anisotropic spaces, adversarial passages can achieve high similarity without semantic naturalness.

**Cross-Dataset Generalization:**
- GASLITE passages optimized on MSMARCO queries generalize to NQ, SciFact, FiQA2018, and Quora queries.
- Topic-specific datasets see higher transfer success (30-40%) than generic evaluation sets (5-15%).

**Cross-Architecture Generalization:**
- Successfully attacks LLM-based embeddings (Stella-1.5B with ~1.5B parameters), indicating broad applicability beyond BERT-scale models.

**Black-Box Transferability:**
- Limited: attacks trained on one model transfer with only 25-60% relative effectiveness to other models.
- White-box access substantially improves attack success -- this is why the white-box threat model is important.

**RAG Case Study:**
- Tested on an actual RAG pipeline (OpenWebUI + Chroma vector store).
- With 10 adversarial passages targeting Harry Potter queries:
  - 73% of queries returned adversarial passages in top-3 retrieved context.
  - LLM generated misleading responses in 58% of cases.
  - 100% appearance rate in top-10 retrieval without defenses.

---

### Limitations Acknowledged

1. **White-box assumption:** While justified by open-source prevalence, real deployments may use proprietary models (OpenAI, Cohere) where white-box access is unavailable. Black-box transferability is limited.
2. **Concept knowledge required:** "Knows What" attacks require a sample of concept-related queries. Fully unknown attack distributions ("Knows Nothing") remain significantly harder (5-20% vs. 61-100%).
3. **Static corpus assumption:** Real corpora are constantly updated; adversarial passages could be diluted or removed over time.
4. **No corpus read-access:** Attacker cannot verify insertion success or monitor detection.
5. **Trigger naturalness:** Despite perplexity-constrained variants, triggers remain syntactically odd. Future content moderation systems might flag them on other grounds.
6. **English only:** Multilingual robustness is unexplored.
7. **Trigger length:** 100 tokens is somewhat arbitrary; the sensitivity to this parameter is not exhaustively studied.
8. **Model evolution:** Techniques may become less effective as embedding models improve and potentially incorporate adversarial training.

---

### Additional Context

**Why Cor.Pois. (Zhong et al. 2023) Underperforms:**
The prior state-of-the-art (1) assumed access to corpus content and ground-truth passages (more relaxed threat model), (2) used single-token HotFlip without multi-coordinate optimization, and (3) critically, did not handle the token-to-text irreversibility problem. When optimized token sequences are decoded to text and re-tokenized for corpus insertion, the resulting tokens can differ from what was optimized, causing substantial degradation. This single issue accounts for much of the performance gap.

**The paper's core contribution** is framed not as a novel mathematical formulation (the objective is straightforward dot-product maximization) but as a principled engineering solution: correctly solving discrete optimization in text space while maintaining token-text consistency, combined with the first comprehensive evaluation across realistic threat models and diverse models.

**Subsequent citing work** includes "Semantic Chameleon" (2025), "SilentRetrieval" (2025), and "Unsupervised Corpus Poisoning Attacks in Continuous Space" (SIGIR 2025), indicating the paper has catalyzed follow-up research in RAG security.

---

Sources:
- [arXiv Abstract](https://arxiv.org/abs/2412.20953)
- [arXiv HTML Full Paper](https://arxiv.org/html/2412.20953v2)
- [ACM DL Proceedings](https://dl.acm.org/doi/10.1145/3719027.3765095)
- [GitHub Repository](https://github.com/matanbt/gaslite)
- [MarkTechPost Coverage](https://www.marktechpost.com/2025/01/06/this-ai-paper-from-tel-aviv-university-introduces-gaslite-a-gradient-based-method-to-expose-vulnerabilities-in-dense-embedding-based-text-retrieval-systems/)
- [Mahmood Sharif's Faculty Page](https://mahmoods01.github.io/authors/matan-ben-tov/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c01674d-5655-421c-a4d7-2066a41387d2",
  "isSidechain": true,
  "agentId": "aee0facf533f0579b",
  "requestId": "req_011CbYJQaenYSuquhF93mwNF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fedde54e-f175-40a7-810d-124f8e3d34da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MnqUJKLQwBgnJf68Har8Qx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 20972,
      "output_tokens": 3967,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1461
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3967,
          "cache_read_input_tokens": 20972,
          "cache_creation_input_tokens": 1461,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1461,
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
