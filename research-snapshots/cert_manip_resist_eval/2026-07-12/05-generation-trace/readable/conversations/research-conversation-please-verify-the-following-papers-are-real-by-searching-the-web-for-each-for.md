# Research conversation: Please verify the following papers are real by searching the web for each. For each paper, confirm the title, venue, yea

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ab6365162daadbc82.jsonl`
- **Structured JSON:** [`8b00a9a7c4724889733d.json`](../../sessions/8b/8b00a9a7c4724889733d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

50 recorded events

### User

_source line 1 · 2026-05-19T19:09:09.270Z_

Please verify the following papers are real by searching the web for each. For each paper, confirm the title, venue, year, and key findings. Also find specific baseline numbers I should know about.

Papers to verify:
1. "The Token Tax" - arXiv:2509.05486 - AfricaNLP 2026 - claims fertility explains 20-50% of variance
2. "Why Do Multilingual Reasoning Gaps Emerge" - arXiv:2510.27269 - Selective Translation method
3. "Causal Estimation of Tokenisation Bias" - arXiv:2506.03149 - regression discontinuity, 17x probability effect
4. "The Script Tax" - arXiv:2602.11174 - 3.4x fertility, 16.5x inference slowdown
5. "Language-reasoning disentanglement" - arXiv:2505.15257 - removing language-specific components
6. "Reducing Tokenization Premiums" - arXiv:2601.13328 - post-hoc vocabulary additions, LLaMA 3.2

For each: search "[paper title] arxiv" and confirm it exists. Report which ones are verified and which are NOT found.

Also search for:
- AfriMMLU benchmark: what are the current best scores? What languages does it cover?
- MGSM (Multilingual Grade School Math) benchmark: current SOTA scores
- What are the best open-source multilingual models as of May 2026? Search "best open source multilingual LLM 2026" and "top multilingual language models 2026"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ab6365162daadbc82",
  "type": "user",
  "uuid": "261c305a-d820-4692-bccc-f97280c3e0f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T19:09:09.272Z_

```json
{
  "parentUuid": "261c305a-d820-4692-bccc-f97280c3e0f7",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
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
  "uuid": "684128e9-0095-4b27-a855-c82ce7a064ec",
  "timestamp": "2026-05-19T19:09:09.272Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T19:09:09.272Z_

```json
{
  "parentUuid": "684128e9-0095-4b27-a855-c82ce7a064ec",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0ad518bf-9589-4685-b0a5-1cac99ff2cb7",
  "timestamp": "2026-05-19T19:09:09.272Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T19:09:12.192Z_



I'll search for each paper and the benchmarks. Let me start by loading the WebSearch tool, then run all searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ad518bf-9589-4685-b0a5-1cac99ff2cb7",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTK4io7GpeQE28s2Jrb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "446d6de6-a8c8-44c0-9473-6ae04b3649ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MGy5ZGo8SK6mjRDSu5nVa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1720,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1720,
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

_source line 5 · 2026-05-19T19:09:12.607Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013aBGH62eW6mG4U4iUn2qCD`</summary>

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
  "parentUuid": "446d6de6-a8c8-44c0-9473-6ae04b3649ab",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTK4io7GpeQE28s2Jrb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54d05742-0748-49c0-ac22-c45c0001cd5a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MGy5ZGo8SK6mjRDSu5nVa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1720,
      "cache_read_input_tokens": 7773,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1720
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 109,
          "cache_read_input_tokens": 7773,
          "cache_creation_input_tokens": 1720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1720,
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

_source line 6 · 2026-05-19T19:09:12.614Z_

<details><summary>↩ Tool result · `toolu_013aBGH62eW6mG4U4iUn2qCD`</summary>

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
  "parentUuid": "54d05742-0748-49c0-ac22-c45c0001cd5a",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ab6365162daadbc82",
  "type": "user",
  "uuid": "572af8d7-ce9b-4f0a-b435-2a98b414aaa8",
  "sourceToolAssistantUUID": "54d05742-0748-49c0-ac22-c45c0001cd5a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T19:09:15.409Z_



Now let me search for all papers and benchmarks in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "572af8d7-ce9b-4f0a-b435-2a98b414aaa8",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTKKERqXVcckgaWwDLB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d61b87a-a490-4a5a-8f80-74f44453fca2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5wKFRNBnybzUVyGNoubxe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1131,
      "cache_read_input_tokens": 9493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1131,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
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

### Tool call

_source line 8 · 2026-05-19T19:09:15.813Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NPnrwRZFJN1wMiPX7pXNp9`</summary>

```json
{
  "query": "\"The Token Tax\" arXiv 2509.05486 AfricaNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d61b87a-a490-4a5a-8f80-74f44453fca2",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTKKERqXVcckgaWwDLB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc12c4e1-8ef2-4204-a0e5-323428d95e34",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5wKFRNBnybzUVyGNoubxe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1131,
      "cache_read_input_tokens": 9493,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1131
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 85,
          "cache_read_input_tokens": 9493,
          "cache_creation_input_tokens": 1131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1131,
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

### Tool result

_source line 9 · 2026-05-19T19:09:22.967Z_

<details><summary>↩ Tool result · `toolu_01NPnrwRZFJN1wMiPX7pXNp9`</summary>

```text
Web search results for query: ""The Token Tax" arXiv 2509.05486 AfricaNLP"

Links: [{"title":"[2509.05486] The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://arxiv.org/abs/2509.05486"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization - ACL Anthology","url":"https://aclanthology.org/2026.africanlp-main.10/"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://arxiv.org/html/2509.05486v1"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://aclanthology.org/2026.africanlp-main.10.pdf"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization Jessica M. Lundin","url":"https://arxiv.org/pdf/2509.05486"},{"title":"(PDF) The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://www.researchgate.net/publication/395355055_The_Token_Tax_Systematic_Bias_in_Multilingual_Tokenization"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/token-tax-systematic-bias-multilingual-tokenization"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://chatpaper.com/ja/chatpaper/paper/186756"}]

I found the paper for you! Here are the key details:

**"The Token Tax: Systematic Bias in Multilingual Tokenization"** (arXiv 2509.05486)

Tokenization inefficiency imposes structural disadvantages on morphologically complex, low-resource languages, inflating compute resources and depressing accuracy. 

The paper evaluates 10 large language models (LLMs) on AfriMMLU (9,000 MCQA items; 5 subjects; 16 African languages) and shows that fertility (tokens/word) reliably predicts accuracy. Higher fertility consistently predicts lower accuracy across all models and subjects.

Reasoning models (DeepSeek, o1) consistently outperform non-reasoning peers across high and low resource languages in the AfriMMLU dataset, narrowing accuracy gaps observed in prior generations.

The economic implications are significant: A doubling in tokens results in quadrupled training cost and time, underscoring the token tax faced by many languages.

The paper was published in the Proceedings of the 7th Workshop on African Natural Language Processing (AfricaNLP 2026) in Rabat, Morocco.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc12c4e1-8ef2-4204-a0e5-323428d95e34",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ab6365162daadbc82",
  "type": "user",
  "uuid": "c9ddfde6-26ce-4fd1-b145-2148eea9ee47",
  "sourceToolAssistantUUID": "bc12c4e1-8ef2-4204-a0e5-323428d95e34",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T19:09:25.898Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012R38B4Xpe8MN9U5pHP8Ujs`</summary>

```json
{
  "query": "\"Why Do Multilingual Reasoning Gaps Emerge\" arXiv 2510.27269 Selective Translation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9ddfde6-26ce-4fd1-b145-2148eea9ee47",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTL5KndXwRcYrnLveUt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ffe548b-80c3-4f44-8e7f-04ae164cddac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFFhaqBGbFEUEz8X565dyZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9493,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1915
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 9493,
          "cache_creation_input_tokens": 1915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1915,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T19:09:31.970Z_

<details><summary>↩ Tool result · `toolu_012R38B4Xpe8MN9U5pHP8Ujs`</summary>

```text
Web search results for query: ""Why Do Multilingual Reasoning Gaps Emerge" arXiv 2510.27269 Selective Translation"

Links: [{"title":"[2510.27269] Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models?","url":"https://arxiv.org/abs/2510.27269"},{"title":"Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models?","url":"https://arxiv.org/pdf/2510.27269"},{"title":"Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251027269K/abstract"},{"title":"Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models?","url":"https://arxiv.org/html/2510.27269v1"},{"title":"Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models?","url":"https://www.arxiv.org/pdf/2510.27269"},{"title":"Paper page - Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models?","url":"https://huggingface.co/papers/2510.27269"},{"title":"Large Reasoning Models Are (Not Yet) Multilingual Latent Reasoners","url":"https://arxiv.org/html/2601.02996v1"},{"title":"Self-Improving Multilingual Long Reasoning via Translation-Reasoning Integrated Training","url":"https://arxiv.org/html/2602.05940v1"}]

Based on the search results, here's what I found about this research paper:

## Overview

Reasoning language models (RLMs) achieve strong performance on complex reasoning tasks, yet they still exhibit a multilingual reasoning gap, performing better in high-resource languages than in low-resource ones.

## Root Cause

The multilingual reasoning gap primarily stems from failures in language understanding—specifically, the model's inability to translate multilingual inputs into the language dominating its reasoning traces (typically English).

## Key Findings

Understanding failures are detectable to a meaningful extent, with supervised approaches performing best.

## Proposed Solution: Selective Translation

Selective Translation is a strategy that incorporates an English translation into the initial reasoning trace only when an understanding failure is detected. 

Selective Translation bridges the multilingual reasoning gap, achieving near full-translation performance while using translation for only about 20% of inputs.

The paper by Kang et al. provides a systematic analysis showing that understanding failures are the dominant source of the multilingual reasoning gap in reasoning language models, and demonstrates that targeted intervention through Selective Translation can effectively address this issue with minimal computational overhead.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ffe548b-80c3-4f44-8e7f-04ae164cddac",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ab6365162daadbc82",
  "type": "user",
  "uuid": "8b8cb705-24cf-42c1-bb7f-22338397885c",
  "sourceToolAssistantUUID": "6ffe548b-80c3-4f44-8e7f-04ae164cddac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T19:09:34.221Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FZJvhKzKBkhMaH2Ejeu5yL`</summary>

```json
{
  "query": "\"Causal Estimation of Tokenisation Bias\" arXiv 2506.03149 regression discontinuity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b8cb705-24cf-42c1-bb7f-22338397885c",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTLjo577CdacucJ72wo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80542137-08ad-43dd-86ef-0e3aff33573d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JiuW3ZHqqg41djs37e3wX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 731,
      "cache_read_input_tokens": 11408,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 731
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 11408,
          "cache_creation_input_tokens": 731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 731,
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

_source line 13 · 2026-05-19T19:09:43.191Z_

<details><summary>↩ Tool result · `toolu_01FZJvhKzKBkhMaH2Ejeu5yL`</summary>

```text
Web search results for query: ""Causal Estimation of Tokenisation Bias" arXiv 2506.03149 regression discontinuity"

Links: [{"title":"[2506.03149v1] Causal Estimation of Tokenisation Bias","url":"http://arxiv.org/abs/2506.03149v1"},{"title":"[2506.03149] Causal Estimation of Tokenisation Bias","url":"https://arxiv.org/abs/2506.03149"},{"title":"Causal Estimation of Tokenisation Bias","url":"https://arxiv.org/html/2506.03149v1"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=7650&show=50"},{"title":"Computation and Language Jun 2025","url":"https://www.arxiv.org/list/cs.CL/2025-06?skip=325&show=25"},{"title":"Machine Learning Jun 2025","url":"https://www.arxiv.org/list/cs.LG/2025-06?skip=2600&show=50"},{"title":"Exploiting Vocabulary Frequency Imbalance in Language Model Pre-training","url":"https://arxiv.org/html/2508.15390v2"},{"title":"Computer Science Jun 2025","url":"https://www.arxiv.org/list/cs/2025-06?skip=1775&show=50"},{"title":"Token Distillation: Attention-Aware Input Embeddings for New Tokens","url":"https://arxiv.org/html/2505.20133v2"}]

Based on the search results, I found the paper you're looking for. Here's what I found:

**Paper Title:** "Causal Estimation of Tokenisation Bias"
**arXiv ID:** 2506.03149
**Authors:** Pietro Lesci, Clara Meister, Thomas Hofmann, Andreas Vlachos, and Tiago Pimentel
**Status:** Published as a conference paper at ACL 2025

**Overview:**

The tokeniser choice should ideally not affect the probability assigned to the underlying character-string, but in practice it does. This mismatch is defined as tokenisation bias.

**Main Research Question:**

The paper quantifies one particular type of tokenisation bias: the effect of including or not a subword in a tokeniser's vocabulary on the probability a trained model assigns to the corresponding characters.

**Methodological Approach:**

The researchers frame tokenisation bias as a causal effect and estimate it using the regression discontinuity design. They exploit the fact that tokenisation algorithms rank subwords and add the first K to a tokeniser's vocabulary, where K is an arbitrary cutoff point, allowing them to estimate a causal effect by comparing similar subwords around this cutoff.

**Key Findings:**

The researchers find that tokenisation consistently affects models' outputs across scales, vocabularies, and tokenisers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80542137-08ad-43dd-86ef-0e3aff33573d",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ab6365162daadbc82",
  "type": "user",
  "uuid": "7cf3706b-1a50-484e-8959-8d31d9a56a24",
  "sourceToolAssistantUUID": "80542137-08ad-43dd-86ef-0e3aff33573d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T19:09:45.601Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EpX5NLR7wV9iuFhaSutPSJ`</summary>

```json
{
  "query": "\"The Script Tax\" arXiv 2602.11174 fertility inference slowdown"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cf3706b-1a50-484e-8959-8d31d9a56a24",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTMZj7ZPAhyHDo5jchT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0338eb16-e1b8-40b6-8d60-b879c57606ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017cM2PrEVabYUbNkT47xzNN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 12139,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 809
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 12139,
          "cache_creation_input_tokens": 809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 809,
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

### Tool result

_source line 15 · 2026-05-19T19:09:53.424Z_

<details><summary>↩ Tool result · `toolu_01EpX5NLR7wV9iuFhaSutPSJ`</summary>

```text
Web search results for query: ""The Script Tax" arXiv 2602.11174 fertility inference slowdown"

Links: [{"title":"[2602.11174] The Script Tax: Measuring Tokenization-Driven Efficiency and Latency Disparities in Multilingual Language Models","url":"https://arxiv.org/abs/2602.11174"},{"title":"The Script Tax: Measuring Tokenization-Driven Efficiency and Latency Disparities in Multilingual Language Models","url":"https://arxiv.org/html/2602.11174"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization Jessica M. Lundin","url":"https://arxiv.org/pdf/2509.05486"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://arxiv.org/html/2509.05486v1"},{"title":"TaxBreak: Unmasking the Hidden Costs of LLM Inference Through Overhead Decomposition","url":"https://arxiv.org/pdf/2603.12465"},{"title":"Kinship governs fertility with pre-and post-zygotic mechanisms mediated by match of methylation patterns","url":"https://www.biorxiv.org/content/10.1101/135327.full.pdf"}]

Based on the search results, I found the paper you're looking for:

"The Script Tax: Measuring Tokenization-Driven Efficiency and Latency Disparities in Multilingual Language Models" (arXiv:2602.11174) was submitted on January 19, 2026.

The paper's key findings regarding the relationship between fertility and inference slowdown are:

Across mBERT and XLM-R, the higher-fragmentation orthography shows a ~3.4x increase in fertility (6.73-6.85 vs. 2.10-2.35 tokens/word), leading to a 16.5x inference slowdown (0.23 vs. 3.8 sentences/second) on identical hardware.

The core mechanism is tokenization fragmentation, which is quantified with fertility (tokens per word). Higher fertility inflates the effective sequence length, which can induce disproportionate slowdowns in Transformer inference due to attention costs that scale superlinearly with sequence length.

The research demonstrates that tokenization differences between writing systems can impose significant computational costs on multilingual language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0338eb16-e1b8-40b6-8d60-b879c57606ea",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ab6365162daadbc82",
  "type": "user",
  "uuid": "fab466c3-9687-4da0-a823-f8dbeff92dcd",
  "sourceToolAssistantUUID": "0338eb16-e1b8-40b6-8d60-b879c57606ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T19:09:56.030Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015T2kjSQr3gAuPo3drRPHGY`</summary>

```json
{
  "query": "\"Language-reasoning disentanglement\" arXiv 2505.15257 removing language-specific components"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fab466c3-9687-4da0-a823-f8dbeff92dcd",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTNKTQGuBrLmbABNrAg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c327be0-d6d6-4966-8716-fed6a419eabe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MhWakRZc8LGJfr4Toryja7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1477,
      "cache_read_input_tokens": 12139,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1477
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 12139,
          "cache_creation_input_tokens": 1477,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1477,
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

### Tool result

_source line 17 · 2026-05-19T19:10:02.382Z_

<details><summary>↩ Tool result · `toolu_015T2kjSQr3gAuPo3drRPHGY`</summary>

```text
Web search results for query: ""Language-reasoning disentanglement" arXiv 2505.15257 removing language-specific components"

Links: [{"title":"[2505.15257] When Less Language is More: Language-Reasoning Disentanglement Makes LLMs Better Multilingual Reasoners","url":"https://arxiv.org/abs/2505.15257"},{"title":"Language-Reasoning Disentanglement","url":"https://www.emergentmind.com/topics/language-reasoning-disentanglement"},{"title":"When Less Language is More: Language-Reasoning Disentanglement Makes LLMs Better Multilingual Reasoners","url":"https://arxiv.org/html/2505.15257"},{"title":"When Less Language is More: Language-Reasoning Disentanglement Makes LLMs","url":"https://arxiv.org/pdf/2505.15257"},{"title":"Far from the Shallow: Brain-Predictive Reasoning Embedding through Residual Disentanglement","url":"https://arxiv.org/html/2510.22860v1"},{"title":"Computation and Language","url":"https://www.arxiv.org/list/cs.CL/pastweek?skip=255&show=25"},{"title":"Computation and Language May 2025","url":"https://arxiv.org/list/cs.CL/2025-05?skip=900&show=250"}]

Based on the search results, here's what I found about arXiv paper 2505.15257 on language-reasoning disentanglement:

## Overview

The paper is titled "When Less Language is More: Language-Reasoning Disentanglement Makes LLMs Better Multilingual Reasoners" and addresses the challenge that multilingual reasoning in large language models shows performance disproportionately favoring high-resource languages.

## Core Hypothesis and Methodology

The research is inspired by cognitive neuroscience, hypothesizing that LLMs similarly encode reasoning and language as separable components that can be disentangled to enhance multilingual reasoning. To validate this hypothesis, the researchers perform a causal intervention by removing language-specific components from hidden representations.

## Key Findings

The causal intervention involves ablating language-specific representations at inference time, and experiments on 10 open-weight LLMs spanning 11 typologically diverse languages show that this language-specific ablation consistently boosts multilingual reasoning performance.

Layer-wise analyses confirm that language and reasoning representations can be effectively disentangled throughout the model, yielding improved multilingual reasoning capabilities, while preserving top-layer language features remains essential for multilingual reasoning.

The paper was submitted on May 21, 2025, with a revised version on December 11, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c327be0-d6d6-4966-8716-fed6a419eabe",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ab6365162daadbc82",
  "type": "user",
  "uuid": "42adb922-4ae5-431e-b434-be0361dde2ad",
  "sourceToolAssistantUUID": "3c327be0-d6d6-4966-8716-fed6a419eabe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T19:10:05.031Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Tt8N97EnZ71PmsZwPwhkSU`</summary>

```json
{
  "query": "\"Reducing Tokenization Premiums\" arXiv 2601.13328 vocabulary additions LLaMA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42adb922-4ae5-431e-b434-be0361dde2ad",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTNymkdFc51AZZejaVj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95dbb421-45a5-4c0a-92c7-0f9c91069b93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013riE3RGVFYujZwhrPaHXRo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 12948,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1410
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 12948,
          "cache_creation_input_tokens": 1410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1410,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T19:10:10.873Z_

<details><summary>↩ Tool result · `toolu_01Tt8N97EnZ71PmsZwPwhkSU`</summary>

```text
Web search results for query: ""Reducing Tokenization Premiums" arXiv 2601.13328 vocabulary additions LLaMA"

Links: [{"title":"[2601.13328] Reducing Tokenization Premiums for Low-Resource Languages","url":"https://arxiv.org/abs/2601.13328"},{"title":"Reducing Tokenization Premiums for Low-Resource Languages","url":"https://arxiv.org/html/2601.13328"},{"title":"Reducing Tokenization Premiums for Low-Resource Languages","url":"https://arxiv.org/pdf/2601.13328"},{"title":"Explaining and Mitigating Crosslingual Tokenizer Inequities","url":"https://arxiv.org/pdf/2510.21909"},{"title":"Vocabulary Customization for Efficient Domain-Specific LLM Deployment","url":"https://arxiv.org/pdf/2509.26124"}]

Based on the search results, here's what I found about arXiv paper 2601.13328:

The paper addresses how low-resource languages suffer from substantial tokenization premiums in modern language models, meaning that it generally requires several times as many tokens to encode a sentence in a low-resource language than to encode the analogous sentence in English. This tokenization premium results in increased API and energy costs and reduced effective context windows for these languages.

The authors propose a mechanism to reduce tokenization premiums in pre-trained models, by post-hoc additions to the token vocabulary that coalesce multi-token characters into single tokens. They apply this methodology to 12 low-resource languages, demonstrating that the original and compressed inputs often have similar last hidden states when run through the Llama 3.2 1B model.

The paper was authored by Geoffrey Churchill and Steven Skiena from Stony Brook University and was published on January 19, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95dbb421-45a5-4c0a-92c7-0f9c91069b93",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ab6365162daadbc82",
  "type": "user",
  "uuid": "a98063c3-52ac-4ab1-85c5-e53819eb7d2e",
  "sourceToolAssistantUUID": "95dbb421-45a5-4c0a-92c7-0f9c91069b93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-19T19:10:13.918Z_

Good, all six papers are found. Now let me search for the benchmarks and models.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a98063c3-52ac-4ab1-85c5-e53819eb7d2e",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTPc73e1e26Wmjt8omR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7775ba91-8e6d-4f23-9de1-80ba6f10a3b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0111bubPZsxUHsTL7Hx2EDZg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 542,
      "cache_read_input_tokens": 14358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 542,
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

_source line 21 · 2026-05-19T19:10:14.132Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XiVuurEQ8mTHnnEgnwLmTA`</summary>

```json
{
  "query": "AfriMMLU benchmark best scores languages 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7775ba91-8e6d-4f23-9de1-80ba6f10a3b7",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTPc73e1e26Wmjt8omR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97652998-a78e-44e5-a315-96a8cb36ef91",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0111bubPZsxUHsTL7Hx2EDZg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 542,
      "cache_read_input_tokens": 14358,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 542
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 86,
          "cache_read_input_tokens": 14358,
          "cache_creation_input_tokens": 542,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 542,
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

_source line 22 · 2026-05-19T19:10:21.803Z_

<details><summary>↩ Tool result · `toolu_01XiVuurEQ8mTHnnEgnwLmTA`</summary>

```text
Web search results for query: "AfriMMLU benchmark best scores languages 2025 2026"

Links: [{"title":"IrokoBench: A New Benchmark for African Languages in the Age of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.139/"},{"title":"AfriqueLLM: Open LLMs for African Languages","url":"https://www.emergentmind.com/topics/afriquellm"},{"title":"The AI Language Proficiency Monitor – Tracking the Progress of LLMs on Multilingual Benchmarks","url":"https://arxiv.org/html/2507.08538v1"},{"title":"[2504.06536] Lugha-Llama: Adapting Large Language Models for African Languages","url":"https://arxiv.org/abs/2504.06536"},{"title":"IrokoBench: A New Benchmark for African Languages in the Age of Large","url":"https://arxiv.org/pdf/2406.03368"},{"title":"[2406.03368] IrokoBench: A New Benchmark for African Languages in the Age of Large Language Models","url":"https://arxiv.org/abs/2406.03368"},{"title":"IrokoBench: A New Benchmark for African Languages in the Age of Large Language Models","url":"https://arxiv.org/html/2406.03368v1"},{"title":"Lugha-Llama: Adapting Large Language Models for African Languages","url":"https://arxiv.org/pdf/2504.06536"}]

Based on the search results, here's what I found about the AfriMMLU benchmark and best scores:

## Overview of AfriMMLU

AfriMMLU is a multi-choice knowledge-based QA task that is part of the IrokoBench benchmark dataset for 17 typologically-diverse low-resource African languages. The AfriMMLU component covers 64 languages with 5-shot multiple-choice knowledge QA evaluation.

## Best Performing Models

Closed models Claude OPUS, GPT-4-Turbo, and GPT-4o consistently outperform open models on the IrokoBench benchmarks. Specifically for AfriMMLU, GPT-4o outperforms LLaMa 3 70B by approximately 21.1 points.

The highest performing open model, Gemma 2 27B, only achieves 63% of the best-performing proprietary model GPT-4o's performance.

For African-language-specific adaptations, Lugha-Llama's overall performance on IrokoBench is the best of any current open-weight model.

## Performance Insights

Evaluation reveals a significant performance gap between high-resource languages (such as English and French) and low-resource African languages. Additionally, machine translating the test set to English before evaluation helped close the gap for larger models that are English-centric, like Gemma 2 27B and LLaMa 3.1 70B.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97652998-a78e-44e5-a315-96a8cb36ef91",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ab6365162daadbc82",
  "type": "user",
  "uuid": "9226bb94-d228-43e2-9beb-cd7b81a91915",
  "sourceToolAssistantUUID": "97652998-a78e-44e5-a315-96a8cb36ef91",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T19:10:24.750Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EyvBBG4HDYdELpLvFT7f75`</summary>

```json
{
  "query": "MGSM multilingual grade school math benchmark SOTA scores 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9226bb94-d228-43e2-9beb-cd7b81a91915",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTQQrA1h3Esgzc2g3VP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f75078a-5e1d-4d12-83d2-1648e82a0ebb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Y8sDPsw5ro1naJypPRYZA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 924,
      "cache_read_input_tokens": 14900,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 924
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 14900,
          "cache_creation_input_tokens": 924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 924,
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

_source line 24 · 2026-05-19T19:10:31.445Z_

<details><summary>↩ Tool result · `toolu_01EyvBBG4HDYdELpLvFT7f75`</summary>

```text
Web search results for query: "MGSM multilingual grade school math benchmark SOTA scores 2025 2026"

Links: [{"title":"MGSM (Multilingual Grade School Math) | AI Wiki","url":"https://aiwiki.ai/wiki/mgsm"},{"title":"MGSM Benchmark: Multilingual Grade School Math","url":"https://www.emergentmind.com/topics/multilingual-grade-school-math-mgsm-benchmark"},{"title":"MGSM: Multilingual Grade School Math","url":"https://ukgovernmentbeis.github.io/inspect_evals/evals/mathematics/mgsm/"},{"title":"MGSM: Multilingual Grade School Math Benchmark","url":"https://www.kaggle.com/datasets/open-benchmarks/mgsm-multilingual-grade-school-math-benchmark/data"},{"title":"LLM Benchmarks in 2024: Overview, Limits and Model Comparison","url":"https://www.vellum.ai/blog/llm-benchmarks-overview-limits-and-model-comparison"},{"title":"MGSM Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/mgsm"},{"title":"Language Models are Multilingual Chain-of-Thought Reasoners","url":"https://arxiv.org/pdf/2210.03057"},{"title":"juletxara/mgsm · Datasets at Hugging Face","url":"https://huggingface.co/datasets/juletxara/mgsm"}]

Based on the search results, here's what I found about MGSM benchmark SOTA scores for 2025-2026:

## Latest SOTA Scores (2025-2026)

Llama 4 Maverick from Meta currently leads the MGSM leaderboard with a score of 92.3%, followed by o3-mini at 92.0% and Claude 3.5 Sonnet at 91.6%.

For earlier frontier models, Claude Opus 4.5 (Thinking) has reached 95.2% on MGSM, and GPT-5.3 Codex has been reported at 96% as of early 2025.

## About the Benchmark

MGSM (Multilingual Grade School Math) is a benchmark dataset that evaluates the mathematical reasoning capabilities of large language models across multiple languages, released in October 2022 by Google Research and published at ICLR 2023, extending the popular GSM8K benchmark by manually translating 250 grade-school math problems into 10 typologically diverse languages.

## Recent Updates

In 2026, researchers introduced MGSM-Pro, which applies the GSM-Symbolic approach of varying surface-level details while preserving mathematical structure, addressing concerns about potential model memorization of the original 250 problems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f75078a-5e1d-4d12-83d2-1648e82a0ebb",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ab6365162daadbc82",
  "type": "user",
  "uuid": "465ef74a-104a-4834-82f5-0adef839cb0b",
  "sourceToolAssistantUUID": "0f75078a-5e1d-4d12-83d2-1648e82a0ebb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T19:10:33.934Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014hbLHZi7W1RViecJsrJL7h`</summary>

```json
{
  "query": "best open source multilingual LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "465ef74a-104a-4834-82f5-0adef839cb0b",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTR858Sfm1cPnxpTske",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6169daa8-c188-4d3d-94f8-ef164d76f538",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hd7UdvfeAG8JEqNLBRXUPZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 778,
      "cache_read_input_tokens": 15824,
      "output_tokens": 62,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 778
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 62,
          "cache_read_input_tokens": 15824,
          "cache_creation_input_tokens": 778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 778,
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

_source line 26 · 2026-05-19T19:10:40.451Z_

<details><summary>↩ Tool result · `toolu_014hbLHZi7W1RViecJsrJL7h`</summary>

```text
Web search results for query: "best open source multilingual LLM 2026"

Links: [{"title":"Top Open-Source LLMs 2026: The Best Models & Comparison","url":"https://kairntech.com/blog/articles/top-open-source-llm-models-in-2026/"},{"title":"Best Open Source LLMs in 2026: DeepSeek, Llama & More","url":"https://www.miniloop.ai/blog/best-open-source-llms-2026"},{"title":"Ultimate Guide - The Best Open Source LLM For Spanish In 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-llm-for-spanish"},{"title":"Best Open-Source LLM 2026: 8 Tested, 3 Beat GPT-4 | TECHSY","url":"https://techsy.io/en/blog/best-open-source-llms-2026"},{"title":"The Best Open Source and Open-Weight LLM Models to Run Locally in 2026","url":"https://huggingface.co/blog/daya-shankar/open-source-llm-models-to-run-locally"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"Best Open Source LLMs: Complete 2026 Guide | Contabo Blog","url":"https://contabo.com/blog/open-source-llms/"},{"title":"The Best Open Source LLMs and Their Uses in 2026 | igmGuru","url":"https://www.igmguru.com/blog/top-open-source-llms"}]

Based on the search results, here are the best open source multilingual LLMs in 2026:

## Top Multilingual Models

Qwen 2.5 is highlighted for multilingual tasks, and more specifically, Qwen 3 235B-A22B currently leads on the broadest range of benchmarks, combining top-tier reasoning, coding, and multilingual capabilities under an Apache 2.0 license.

Qwen 3 is identified as the best multilingual option, and supports 29+ languages with native fluency. Additionally, Qwen3 has strong multilingual support across 100+ languages and dialects.

For most users, Qwen3 is the best overall local LLM family because it balances quality, model sizes, multilingual support, tooling, and Apache 2.0 licensing.

## Other Strong Contenders

Llama 4 Scout is noted as the best for long context, and DeepSeek-V3.2 is the overall best model. Qwen 3 is particularly strong for multilingual workloads with 256K context and support for 100+ languages.

For Spanish specifically, top recommendations for 2026 include Qwen3-235B-A22B, Meta-Llama-3.1-8B-Instruct, and Qwen3-14B.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6169daa8-c188-4d3d-94f8-ef164d76f538",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ab6365162daadbc82",
  "type": "user",
  "uuid": "6fe3250e-9858-4447-b1e5-15a774c0a0c6",
  "sourceToolAssistantUUID": "6169daa8-c188-4d3d-94f8-ef164d76f538",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T19:10:44.116Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QSU1W5k6hkzJTc152BRxBJ`</summary>

```json
{
  "query": "top multilingual language models 2026 African low-resource languages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fe3250e-9858-4447-b1e5-15a774c0a0c6",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTRnYepNbJipDoYr2TN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d8d6a0f-375b-4a02-9ddd-fb9bfa55ae00",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5u7thUgB8sUYg77L6XUFv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 834,
      "cache_read_input_tokens": 16602,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 834,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
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

_source line 28 · 2026-05-19T19:10:50.669Z_

<details><summary>↩ Tool result · `toolu_01QSU1W5k6hkzJTc152BRxBJ`</summary>

```text
Web search results for query: "top multilingual language models 2026 African low-resource languages"

Links: [{"title":"[2605.18239] Multilingual jailbreaking of LLMs using low-resource languages","url":"https://arxiv.org/abs/2605.18239"},{"title":"AfriqueLLM: Open LLMs for African Languages","url":"https://www.emergentmind.com/topics/afriquellm"},{"title":"Training Language Models (LLMs) for Low-Resource African Languages | by Equalyz_AI | Medium","url":"https://medium.com/@equalyz_ai/training-language-models-llms-for-low-resource-african-languages-7c3b9b26955c"},{"title":"UCT researchers develop AI model for 11 South African languages | UCT News","url":"https://www.news.uct.ac.za/article/-2026-05-04-uct-researchers-develop-ai-model-for-11-south-african-languages"},{"title":"The State of Large Language Models for African Languages: Progress and Challenges","url":"https://arxiv.org/html/2506.02280v3"},{"title":"AfroBench: How Good are Large Language Models on African Languages?","url":"https://arxiv.org/html/2311.07978v4"},{"title":"Cross-lingual transfer of multilingual models on low resource African   Languages","url":"https://arxiv.org/pdf/2409.10965"},{"title":"Cheetah: Natural Language Generation for 517 African Languages","url":"https://arxiv.org/pdf/2401.01053"}]

Based on the search results, here are the top multilingual language models for African low-resource languages in 2026:

## Specialized African Language Models

**AfriqueLLM** is a suite of open LLMs specifically adapted for African languages via continued pre-training on curated, task-diverse data mixtures, focusing on 20–24 African and African-relevant high-resource languages.

**MzansiLM** is an AI language model developed by UCT researchers covering 11 of South Africa's official languages, addressing a critical gap in AI tools for low-resource languages.

**Cheetah** is a language model specifically designed to support 517 African languages and language varieties.

## Established Multilingual Models

Pre-trained multilingual models like mT5, mBART, and XLM-R have demonstrated remarkable capabilities in processing African languages, even with limited exposure during pre-training.

**AfriBERT** achieved the highest cross-lingual accuracy of 88.3% after fine-tuning in studies on Bantu languages.

## Key Challenge

Among 42 supported African languages, only four languages (Amharic, Swahili, Afrikaans, and Malagasy) are consistently treated while there is over 98% of unsupported African languages, highlighting the significant gap in coverage for African language models in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d8d6a0f-375b-4a02-9ddd-fb9bfa55ae00",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ab6365162daadbc82",
  "type": "user",
  "uuid": "3b87e281-0bdf-4827-9914-4c0dabbf0117",
  "sourceToolAssistantUUID": "0d8d6a0f-375b-4a02-9ddd-fb9bfa55ae00",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-19T19:10:54.045Z_

Now let me get more specific details on a few items - the Token Tax paper's specific claim about variance, and the Causal Estimation paper's 17x probability claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b87e281-0bdf-4827-9914-4c0dabbf0117",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTSYFhh452JnZ76wL6H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4559b697-c8e5-4db9-9a02-63a24d35879c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJF3EcXSAehbR7mYssYUdT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 796,
      "cache_read_input_tokens": 17436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 796,
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

_source line 30 · 2026-05-19T19:10:55.646Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UUWhnJFTu2yxTbrXg6RvcW`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.05486",
  "prompt": "What specific claims does this paper make about fertility explaining variance? Does it claim fertility explains 20-50% of variance? What are the key quantitative findings and baseline numbers?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4559b697-c8e5-4db9-9a02-63a24d35879c",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTSYFhh452JnZ76wL6H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4bf31dfa-3b8f-4fc3-a235-9f6886838b2f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJF3EcXSAehbR7mYssYUdT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 796,
      "cache_read_input_tokens": 17436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 796,
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

_source line 31 · 2026-05-19T19:10:59.416Z_

<details><summary>↩ Tool result · `toolu_01UUWhnJFTu2yxTbrXg6RvcW`</summary>

```text
# Summary of Fertility Findings

Based on the provided abstract, the paper makes a clear claim about fertility's predictive power:

**Key Claim:**
The authors state that "fertility (tokens/word) reliably predicts accuracy" and that "Higher fertility consistently predicts lower accuracy across all models and subjects."

**Specificity Limitation:**
The abstract does not provide specific quantitative figures regarding variance explained (such as 20-50% claims). It only establishes that fertility shows a **reliable, consistent inverse relationship** with accuracy across the evaluated 10 LLMs on the AfriMMLU benchmark (9,000 multiple-choice items across 16 African languages).

**Economic Quantification:**
The only concrete numerical claim is economic rather than statistical: "a doubling in tokens results in quadrupled training cost and time."

The full paper (accessible via PDF) would contain detailed statistical analyses, but those specific variance percentages are not disclosed in this abstract summary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bf31dfa-3b8f-4fc3-a235-9f6886838b2f",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ab6365162daadbc82",
  "type": "user",
  "uuid": "9aed6444-a0aa-4495-bb59-f59461c22bc1",
  "sourceToolAssistantUUID": "4bf31dfa-3b8f-4fc3-a235-9f6886838b2f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-19T19:11:03.312Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GQ3xUD3WrTwMgqy8RkRtqP`</summary>

```json
{
  "url": "https://arxiv.org/html/2509.05486v1",
  "prompt": "What specific claims does this paper make about fertility explaining variance in accuracy? Does it say fertility explains 20-50% of variance? What are the specific R-squared values or regression results? What are the key quantitative baseline numbers for different languages and models?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9aed6444-a0aa-4495-bb59-f59461c22bc1",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTTBhidgQkdYyGiqeNm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb8571ed-61a7-40f3-8014-7ff1434f8129",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Liizkin6TM1yEYgW97oP1j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 378,
      "cache_read_input_tokens": 18232,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 378
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 18232,
          "cache_creation_input_tokens": 378,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 378,
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

_source line 33 · 2026-05-19T19:11:08.164Z_

<details><summary>↩ Tool result · `toolu_01GQ3xUD3WrTwMgqy8RkRtqP`</summary>

```text
# Key Claims About Fertility and Variance in Accuracy

## Main Variance Claims

The paper states that "Fertility explains 20-50% of variance in accuracy across these regressions, underscoring its importance as a predictor."

More specifically, the regression slopes range substantially: each additional token per word reduces accuracy by **8-18 percentage points** depending on subject and model.

## Specific R² Values

Table 1 provides detailed statistics. Notable examples include:

- **Llama 3.1 405B on Microeconomics**: slope = -0.185 (p = 0.002), R² = 0.476
- **Qwen 2.5 32B on Geography**: slope = -0.155 (p = 0.006), R² = 0.404
- **Aya23 35B on Elementary Math**: slope = -0.079 (p = 0.001), R² = 0.523

The paper notes that "several effects are large and statistically significant" across the 10 models and 5 subjects tested.

## Language Performance Baseline

On average, African languages trail English by **25 accuracy points** across MMLU. However, reasoning models (DeepSeek, o1) narrow this gap substantially—reducing it to 12-14 points on the most challenging subject (Global Facts), representing an **8-12 point improvement** for African language performance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb8571ed-61a7-40f3-8014-7ff1434f8129",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ab6365162daadbc82",
  "type": "user",
  "uuid": "4f6ade38-96a7-4740-ac11-681a42f1995b",
  "sourceToolAssistantUUID": "fb8571ed-61a7-40f3-8014-7ff1434f8129",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-19T19:11:11.599Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JuCQWmMrzjTEMVNWh5WuTn`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.03149",
  "prompt": "What are the specific quantitative findings? Does it mention a 17x probability effect? What are the key numbers about tokenisation bias?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f6ade38-96a7-4740-ac11-681a42f1995b",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTTq32frUXuPJeZPfmC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f99854f-88c7-47a9-a066-3fe28137e788",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013LK2D92sJEtiVjRgw38QKS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 471,
      "cache_read_input_tokens": 18610,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 471
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 110,
          "cache_read_input_tokens": 18610,
          "cache_creation_input_tokens": 471,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 471,
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

_source line 35 · 2026-05-19T19:11:14.471Z_

<details><summary>↩ Tool result · `toolu_01JuCQWmMrzjTEMVNWh5WuTn`</summary>

```text
# Key Quantitative Findings on Tokenisation Bias

The paper identifies one major quantitative result: **a subword's presence in a small model's vocabulary may increase its characters' probability by up to 17 times.**

The abstract states: "a subword's presence in a small model's vocabulary may increase its characters' probability by up to 17 times, highlighting tokenisation as a key design choice in language modelling."

Beyond this specific finding, the research confirms that "tokenisation consistently affects models' outputs across scales, vocabularies, and tokenisers," but the document does not provide additional numerical metrics for the broader effect. The 17x multiplier represents the most concrete quantitative measure of tokenisation bias mentioned in the abstract.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f99854f-88c7-47a9-a066-3fe28137e788",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ab6365162daadbc82",
  "type": "user",
  "uuid": "49958147-7ef9-49f4-87ca-65d4953d19a2",
  "sourceToolAssistantUUID": "4f99854f-88c7-47a9-a066-3fe28137e788",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-19T19:11:18.210Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019Fu4dRMaBJKRkUStUkXTZG`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.27269",
  "prompt": "What are the specific quantitative findings? What are the key baseline numbers for the Selective Translation method? What benchmarks were used and what were the scores? What models were evaluated?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49958147-7ef9-49f4-87ca-65d4953d19a2",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTUHz1nfF82dfjskMSm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7e12a8a-b5d3-4acf-bd7a-17948037f793",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MoUcADmJhDrEC2NQrKKKF3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 278,
      "cache_read_input_tokens": 19081,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 278
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 19081,
          "cache_creation_input_tokens": 278,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 278,
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

_source line 37 · 2026-05-19T19:11:22.846Z_

<details><summary>↩ Tool result · `toolu_019Fu4dRMaBJKRkUStUkXTZG`</summary>

```text
# Quantitative Findings from the arXiv Paper

Based on the provided webpage content, specific quantitative benchmarks and detailed baseline numbers are **not included** in this abstract. The page only offers high-level results.

## Available Information:

**Key Finding:** The paper reports that "Selective Translation substantially bridges the multilingual reasoning gap, achieving near full-translation performance while translating only about 20% of inputs."

**Model Tested:** The experiments utilized "Qwen3-4B" for evaluation.

**Detection Performance:** The abstract notes that "understanding failures are detectable to a meaningful extent, with supervised approaches performing best," but exact detection accuracy percentages are not provided in this excerpt.

## Missing Details:

The webpage does not contain:
- Specific benchmark names or datasets used
- Exact performance scores (accuracy percentages, F1 scores, etc.)
- Comparative baseline metrics
- Language-specific performance breakdowns
- Complete evaluation results

For detailed quantitative findings, you would need to access the full PDF or HTML version of the paper available through the provided links.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7e12a8a-b5d3-4acf-bd7a-17948037f793",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ab6365162daadbc82",
  "type": "user",
  "uuid": "b2ea161a-a311-4d52-ab74-29946f7e18ee",
  "sourceToolAssistantUUID": "c7e12a8a-b5d3-4acf-bd7a-17948037f793",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-19T19:11:26.456Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FJ8FwvYNByXQEAZq1LhSUb`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.27269v1",
  "prompt": "What are the specific quantitative findings? What benchmarks were used (e.g., MGSM)? What were the specific accuracy numbers for Selective Translation vs baselines? What models were evaluated? What languages were tested?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2ea161a-a311-4d52-ab74-29946f7e18ee",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTUuqHboQKeCSCaP8Q3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62af361e-86a4-43d9-b974-19866f748786",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016C7U12qZSSNPcttbUEhT6A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 364,
      "cache_read_input_tokens": 19359,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 364
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 19359,
          "cache_creation_input_tokens": 364,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 364,
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

### Tool result

_source line 39 · 2026-05-19T19:11:31.667Z_

<details><summary>↩ Tool result · `toolu_01FJ8FwvYNByXQEAZq1LhSUb`</summary>

```text
# Key Quantitative Findings

## Models Evaluated
The research examined five reasoning language models: "Qwen3-1.7B, 8B, 4B, 14B" and gpt-oss-20b, which were selected for their public availability and state-of-the-art reasoning capabilities.

## Languages Tested
The study covered ten typologically diverse languages: English, German, Spanish, Arabic, Japanese, Korean, Thai, Bengali, Swahili, and Telugu—spanning high-resource, mid-resource, and low-resource categories.

## Benchmarks
Two primary multilingual reasoning benchmarks were used:
- **Polymath**: Mathematical reasoning across difficulty levels (Low, Medium, High)
- **MMLU-ProX-Lite**: STEM-related reasoning tasks

Additional calibration data came from the MGSM dataset.

## Key Accuracy Results

**Polymath-Low (Qwen3-4B):**
- Base performance: 81.1% average
- With Understanding Intervention: 91.9%
- Selective Translation: 88.0%
- Full Translation: 89.4%

**MMLU-ProX-Lite (Qwen3-4B):**
- Base: 72.7% average
- Selective Translation: 74.3%
- Full Translation: 76.5%

## Critical Finding
"Understanding intervention significantly improves performance, especially in low-resource languages such as Swahili (29.3→88.0)" on Polymath-Low, demonstrating that input comprehension failures dominate the multilingual reasoning gap.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62af361e-86a4-43d9-b974-19866f748786",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ab6365162daadbc82",
  "type": "user",
  "uuid": "f76b20f5-fd05-425a-a2bf-e57322ce96b9",
  "sourceToolAssistantUUID": "62af361e-86a4-43d9-b974-19866f748786",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-19T19:11:34.404Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UBkQv2LLi1fdME7wAcavvn`</summary>

```json
{
  "query": "AfriMMLU benchmark languages covered list scores GPT-4o Claude"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f76b20f5-fd05-425a-a2bf-e57322ce96b9",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTVZXw8NhGnsTWeoriF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c240d39-4f39-4b0a-bc63-815106e8a5b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012k589ZQNh3vHjgFrMmp2cy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 875,
      "cache_read_input_tokens": 19359,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 875
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 19359,
          "cache_creation_input_tokens": 875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 875,
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

### Tool result

_source line 41 · 2026-05-19T19:11:41.735Z_

<details><summary>↩ Tool result · `toolu_01UBkQv2LLi1fdME7wAcavvn`</summary>

```text
Web search results for query: "AfriMMLU benchmark languages covered list scores GPT-4o Claude"

Links: [{"title":"ChatGPT-4o vs Claude 4: Comprehensive Report and Comparison","url":"https://www.datastudios.org/post/chatgpt-4o-vs-claude-4-comprehensive-report-and-comparison"},{"title":"IrokoBench: A New Benchmark for African Languages in the Age of Large   Language Models","url":"https://arxiv.org/pdf/2406.03368"},{"title":"Large Language Models for Accessible Reporting of Bioinformatics Analyses in Interdisciplinary Contexts","url":"https://www.biorxiv.org/content/10.1101/2025.11.09.687479.full.pdf"},{"title":"Top LLM Benchmarks Explained: MMLU, HellaSwag, BBH, and Beyond - Confident AI","url":"https://www.confident-ai.com/blog/llm-benchmarks-mmlu-hellaswag-and-beyond"},{"title":"Probing the Surgical Competence of LLMs: A global health study leveraging AfriMedQA benchmarks","url":"https://www.medrxiv.org/content/10.1101/2025.10.05.25337350.full.pdf"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"Benchmarking large language models for cell-free RNA diagnostic biomarker discovery","url":"https://www.biorxiv.org/content/10.1101/2025.08.20.671358.full.pdf"}]

Based on the search results, I found relevant information about the AfriMMLU benchmark. AfriMMLU is a multi-choice knowledge-based question answering benchmark dataset covering 17 typologically-diverse low-resource African languages, and is part of the IrokoBench suite that includes three tasks: natural language inference (AfriXNLI), mathematical reasoning (AfriMGSM), and multi-choice knowledge-based question answering (AfriMMLU).

The benchmark was used to evaluate zero-shot, few-shot, and translate-test settings across 10 open and six proprietary LLMs. However, the search results don't provide the specific list of the 17 African languages covered or detailed scores for GPT-4o and Claude models specifically on the AfriMMLU benchmark.

For more detailed information about the specific languages included and the comparative scores of GPT-4o and Claude on AfriMMLU, you may want to consult the full IrokoBench paper directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c240d39-4f39-4b0a-bc63-815106e8a5b6",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ab6365162daadbc82",
  "type": "user",
  "uuid": "20f6e6fb-0024-4cdc-9134-a8bc9bec6208",
  "sourceToolAssistantUUID": "7c240d39-4f39-4b0a-bc63-815106e8a5b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-19T19:11:45.031Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DqmmdH3zjEYAG7QWrzy4Lt`</summary>

```json
{
  "url": "https://arxiv.org/abs/2406.03368",
  "prompt": "What are the specific languages covered in AfriMMLU/IrokoBench? What are the best scores for each model? What are the GPT-4o, Claude, and top open model scores?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20f6e6fb-0024-4cdc-9134-a8bc9bec6208",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTWJbHePos4CbL8TNUu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6fb26f8b-a95b-45e6-9272-2f417ab720eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THvoeHV3uLyLH6GNm1btPy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1716,
      "cache_read_input_tokens": 19359,
      "output_tokens": 126,
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
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 19359,
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

### Tool result

_source line 43 · 2026-05-19T19:11:48.459Z_

<details><summary>↩ Tool result · `toolu_01DqmmdH3zjEYAG7QWrzy4Lt`</summary>

```text
# IrokoBench Language Coverage and Model Performance

Based on the provided content, I cannot provide the specific information you requested. While the abstract mentions that IrokoBench covers "17 typologically-diverse low-resource African languages," the document does not list which specific languages are included.

Similarly, the page does not contain detailed performance scores for individual models. The abstract only notes that:

- "Gemma 2 27B only at 63% of the best-performing proprietary model GPT-4o performance"

No specific numerical scores are provided for GPT-4o, Claude, or other models in the available text. To obtain the detailed breakdowns you're seeking—including the complete language list and comprehensive performance metrics—you would need to access the full paper itself through the PDF or HTML versions linked on this arXiv page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fb26f8b-a95b-45e6-9272-2f417ab720eb",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ab6365162daadbc82",
  "type": "user",
  "uuid": "3a962a61-776e-4b65-8fdf-b6acc685349f",
  "sourceToolAssistantUUID": "6fb26f8b-a95b-45e6-9272-2f417ab720eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-19T19:11:51.888Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M18caougeF5BcRRmnG26uC`</summary>

```json
{
  "url": "https://arxiv.org/html/2406.03368v1",
  "prompt": "What are the 17 specific African languages covered in AfriMMLU/IrokoBench? What are the best scores for GPT-4o and other top models on AfriMMLU? List the specific accuracy numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a962a61-776e-4b65-8fdf-b6acc685349f",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTWoMfNCE4Jo4fbafxY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d361125-d83b-4bcf-9899-ed2ee1db1800",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UV1mNzzC1bAT3Xp5Nm4ZKq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2031,
      "cache_read_input_tokens": 19359,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2031
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 133,
          "cache_read_input_tokens": 19359,
          "cache_creation_input_tokens": 2031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2031,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-19T19:11:56.705Z_

<details><summary>↩ Tool result · `toolu_01M18caougeF5BcRRmnG26uC`</summary>

```text
# AfriMMLU Languages and GPT-4o Performance

## Languages Covered

AfriMMLU includes **17 languages total**: English, French, and 15 African languages. The African languages are:

1. Amharic (amh)
2. Ewe (ewe)
3. Hausa (hau)
4. Igbo (ibo)
5. Kinyarwanda (kin)
6. Lingala (lin)
7. Luganda (lug)
8. Oromo (orm)
9. Sesotho (sot)
10. Swahili (swa)
11. Twi (twi)
12. Wolof (wol)
13. isiXhosa (xho)
14. isiZulu (zul)
15. Yoruba (yor)

Note: The paper states "17 (incl. French)" for AfriMMLU in Table 1, indicating French was included alongside English and the 15 African languages.

## Top Model Performance on AfriMMLU

**GPT-4o results** (in-language evaluation):
- **Average accuracy across African languages: 52.3%**
- English: 78.6%
- French: 71.4%

**Other top performers** (in-language):
- GPT-4-Turbo: 50.9% (African languages average)
- Claude OPUS: 43.0% (African languages average)

The document notes that "in-language prompting to be better on 10 out of the 16 African languages" evaluated for this task.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d361125-d83b-4bcf-9899-ed2ee1db1800",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ab6365162daadbc82",
  "type": "user",
  "uuid": "9880d8d0-e22a-4f32-83c6-3f86152fd6d1",
  "sourceToolAssistantUUID": "9d361125-d83b-4bcf-9899-ed2ee1db1800",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-19T19:11:59.377Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HFgT1i26iUa565izoyfv2y`</summary>

```json
{
  "query": "MGSM leaderboard 2026 scores multilingual math reasoning models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9880d8d0-e22a-4f32-83c6-3f86152fd6d1",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTXQaiuryuqcWoarJ7B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98486b8d-0834-4255-9c1f-73c7ef8bb793",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NdWz7KGaiWYmKCHUZ6fSJv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 527,
      "cache_read_input_tokens": 21390,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 527
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 21390,
          "cache_creation_input_tokens": 527,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 527,
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

### Tool result

_source line 47 · 2026-05-19T19:12:06.220Z_

<details><summary>↩ Tool result · `toolu_01HFgT1i26iUa565izoyfv2y`</summary>

```text
Web search results for query: "MGSM leaderboard 2026 scores multilingual math reasoning models"

Links: [{"title":"Multilingual Benchmarks 2026: MGSM, MMLU-ProX LLM Scores | BenchLM.ai","url":"https://benchlm.ai/multilingual"},{"title":"MGSM Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/mgsm"},{"title":"MGSM: Multilingual Grade School Math Benchmark Leaderboard | Kaggle","url":"https://www.kaggle.com/benchmarks/open-benchmarks/mgsm"},{"title":"MGSM, methodology, history, and how to verify a published score · Benchlist","url":"https://getbenchlist.com/articles/mgsm"},{"title":"MGSM (Multilingual Grade School Math) | AI Wiki","url":"https://aiwiki.ai/wiki/mgsm"},{"title":"MGSM Benchmark: Multilingual Grade School Math","url":"https://www.emergentmind.com/topics/multilingual-grade-school-math-mgsm-benchmark"},{"title":"MGSM-Pro: A Simple Strategy for Robust Multilingual Mathematical Reasoning Evaluation","url":"https://arxiv.org/html/2601.21225v2"}]

Based on the web search results, here are the latest MGSM leaderboard scores for multilingual math reasoning models in 2026:

## Current Top Performers

**On the LLM-Stats MGSM leaderboard:**
Llama 4 Maverick by Meta leads with a score of 0.923, followed by o3-mini at 92.0% and Claude 3.5 Sonnet at 91.6%. The average score across all models is 0.779.

**On the BenchLM multilingual leaderboard (May 2026):**
Claude Mythos Preview leads the provisional multilingual leaderboard with a weighted score of 100.0%, followed by Gemini 3.1 Pro (100.0%) and Grok 4.1 (100.0%). Claude Mythos Preview leads multilingual with the most consistent cross-language scores. GPT-5.4 is close second, strong on MMLU-ProX across all tested languages. Claude Opus 4.6 holds #3, with particularly strong MGSM performance.

## About MGSM

MGSM (Multilingual Grade School Math) is a benchmark of grade-school math problems containing 250 grade-school math problems manually translated from the GSM8K dataset into ten typologically diverse languages: Spanish, French, German, Russian, Chinese, Japanese, Thai, Swahili, Bengali, and Telugu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98486b8d-0834-4255-9c1f-73c7ef8bb793",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ab6365162daadbc82",
  "type": "user",
  "uuid": "d008de2c-392d-4ed0-af4c-e2ea09259116",
  "sourceToolAssistantUUID": "98486b8d-0834-4255-9c1f-73c7ef8bb793",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-19T19:12:09.109Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Pf95jqL2EFhwrGsYeFpbDR`</summary>

```json
{
  "url": "https://llm-stats.com/benchmarks/mgsm",
  "prompt": "What are the top 10 model scores on the MGSM leaderboard? List model names and their exact scores."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d008de2c-392d-4ed0-af4c-e2ea09259116",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTY7Exwod5vsNefXcU3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebb31a02-be7f-44aa-9413-6dd911a4a9b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VzpgboFDghLUvALwFFpV6F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1285,
      "cache_read_input_tokens": 21390,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1285
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 109,
          "cache_read_input_tokens": 21390,
          "cache_creation_input_tokens": 1285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1285,
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

### Tool result

_source line 49 · 2026-05-19T19:12:14.365Z_

<details><summary>↩ Tool result · `toolu_01Pf95jqL2EFhwrGsYeFpbDR`</summary>

```text
# Top 10 MGSM Leaderboard Scores

Based on the leaderboard data provided:

1. **Llama 4 Maverick** (Meta) — 0.923
2. **o3-mini** (OpenAI) — 0.920
3. **Claude 3.5 Sonnet** (Anthropic, Oct 2024) — 0.916
4. **Claude 3.5 Sonnet** (Anthropic, June 2024) — 0.916
5. **Llama 3.3 70B Instruct** (Meta) — 0.911
6. **o1-preview** (OpenAI) — 0.908
7. **Claude 3 Opus** (Anthropic) — 0.907
8. **Llama 4 Scout** (Meta) — 0.906
9. **GPT-4o** (OpenAI) — 0.905
10. **o1** (OpenAI) — 0.893

The benchmark evaluates "multilingual mathematical reasoning capabilities" across ten languages including Spanish, French, German, Russian, Chinese, Japanese, Thai, Swahili, Bengali, and Telugu.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebb31a02-be7f-44aa-9413-6dd911a4a9b1",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ab6365162daadbc82",
  "type": "user",
  "uuid": "e6f5bfcb-02da-471e-8e78-13964f894479",
  "sourceToolAssistantUUID": "ebb31a02-be7f-44aa-9413-6dd911a4a9b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-19T19:13:04.102Z_

Now I have all the information needed. Here is my comprehensive report:

---

## Paper Verification Results

### All 6 papers are VERIFIED as real. Here are the details:

---

### 1. "The Token Tax" -- arXiv:2509.05486 -- VERIFIED

- **Full title:** "The Token Tax: Systematic Bias in Multilingual Tokenization"
- **Venue:** AfricaNLP 2026 (7th Workshop on African Natural Language Processing), Rabat, Morocco. Also listed in [ACL Anthology](https://aclanthology.org/2026.africanlp-main.10/).
- **Author:** Jessica M. Lundin
- **Claim check:** The claim that "fertility explains 20-50% of variance" is **confirmed**. The paper states: "Fertility explains 20-50% of variance in accuracy across these regressions."
- **Key baseline numbers:**
  - R-squared values range from ~0.40 to ~0.52 (e.g., Llama 3.1 405B on Microeconomics: R^2=0.476; Aya23 35B on Elementary Math: R^2=0.523)
  - Each additional token per word reduces accuracy by 8-18 percentage points
  - African languages trail English by ~25 accuracy points on average across MMLU
  - Reasoning models (DeepSeek, o1) narrow the gap to 12-14 points
  - Evaluated 10 LLMs on AfriMMLU (9,000 MCQA items, 5 subjects, 16 African languages)

---

### 2. "Why Do Multilingual Reasoning Gaps Emerge" -- arXiv:2510.27269 -- VERIFIED

- **Full title:** "Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models?"
- **Venue:** arXiv preprint (cited by subsequent works at ACL-adjacent venues)
- **Authors:** Kang et al.
- **Claim check:** Selective Translation method is **confirmed**.
- **Key baseline numbers:**
  - Polymath-Low (Qwen3-4B): Base=81.1%, With Understanding Intervention=91.9%, Selective Translation=88.0%, Full Translation=89.4%
  - MMLU-ProX-Lite (Qwen3-4B): Base=72.7%, Selective Translation=74.3%, Full Translation=76.5%
  - Swahili on Polymath-Low improved from 29.3% to 88.0% with understanding intervention
  - Selective Translation translates only ~20% of inputs while achieving near full-translation performance
  - Models tested: Qwen3-1.7B, 4B, 8B, 14B and gpt-oss-20b
  - Languages: 10 typologically diverse (English, German, Spanish, Arabic, Japanese, Korean, Thai, Bengali, Swahili, Telugu)

---

### 3. "Causal Estimation of Tokenisation Bias" -- arXiv:2506.03149 -- VERIFIED

- **Full title:** "Causal Estimation of Tokenisation Bias"
- **Venue:** ACL 2025 (published as a conference paper)
- **Authors:** Pietro Lesci, Clara Meister, Thomas Hofmann, Andreas Vlachos, Tiago Pimentel
- **Claim check:** The 17x probability effect is **confirmed**. The paper states: "a subword's presence in a small model's vocabulary may increase its characters' probability by up to 17 times."
- **Method:** Regression discontinuity design exploiting the arbitrary cutoff K in BPE vocabulary construction
- **Key finding:** Tokenisation consistently affects model outputs across scales, vocabularies, and tokenisers

---

### 4. "The Script Tax" -- arXiv:2602.11174 -- VERIFIED

- **Full title:** "The Script Tax: Measuring Tokenization-Driven Efficiency and Latency Disparities in Multilingual Language Models"
- **Venue:** arXiv preprint, submitted January 19, 2026
- **Claim check:** Both 3.4x fertility and 16.5x inference slowdown are **confirmed**.
- **Key baseline numbers:**
  - Higher-fragmentation orthography: fertility of 6.73-6.85 tokens/word vs. 2.10-2.35 for lower-fragmentation (ratio ~3.4x)
  - Inference speed: 0.23 vs. 3.8 sentences/second on identical hardware (ratio ~16.5x slowdown)
  - Tested on mBERT and XLM-R
  - Mechanism: attention costs scale superlinearly with sequence length

---

### 5. "Language-reasoning disentanglement" -- arXiv:2505.15257 -- VERIFIED

- **Full title:** "When Less Language is More: Language-Reasoning Disentanglement Makes LLMs Better Multilingual Reasoners"
- **Venue:** arXiv preprint, submitted May 21, 2025, revised December 11, 2025
- **Claim check:** Removing language-specific components is **confirmed**. The paper performs causal intervention by ablating language-specific representations at inference time.
- **Key findings:**
  - Tested on 10 open-weight LLMs across 11 typologically diverse languages
  - Language-specific ablation consistently boosts multilingual reasoning performance
  - Preserving top-layer language features remains essential for multilingual reasoning
  - Inspired by cognitive neuroscience hypothesis that reasoning and language are separable

---

### 6. "Reducing Tokenization Premiums" -- arXiv:2601.13328 -- VERIFIED

- **Full title:** "Reducing Tokenization Premiums for Low-Resource Languages"
- **Venue:** arXiv preprint, published January 19, 2026
- **Authors:** Geoffrey Churchill, Steven Skiena (Stony Brook University)
- **Claim check:** Post-hoc vocabulary additions applied to LLaMA 3.2 is **confirmed**.
- **Key findings:**
  - Proposes post-hoc additions to the token vocabulary that coalesce multi-token characters into single tokens
  - Applied to 12 low-resource languages
  - Demonstrates original and compressed inputs often have similar last hidden states when run through Llama 3.2 1B

---

## Benchmark Information

### AfriMMLU

- **Languages covered (17 total):** English, French, and 15 African languages: Amharic, Ewe, Hausa, Igbo, Kinyarwanda, Lingala, Luganda, Oromo, Sesotho, Swahili, Twi, Wolof, isiXhosa, isiZulu, Yoruba
- **Best scores (in-language evaluation from IrokoBench paper):**
  - GPT-4o: 52.3% avg on African languages (78.6% English, 71.4% French)
  - GPT-4-Turbo: 50.9% avg on African languages
  - Claude Opus: 43.0% avg on African languages
  - Top open model Gemma 2 27B achieves only 63% of GPT-4o's performance

### MGSM (Multilingual Grade School Math)

- **Languages:** 250 problems translated into 10 languages: Spanish, French, German, Russian, Chinese, Japanese, Thai, Swahili, Bengali, Telugu
- **Top scores on the leaderboard:**
  1. Llama 4 Maverick (Meta): 92.3%
  2. o3-mini (OpenAI): 92.0%
  3. Claude 3.5 Sonnet (Anthropic): 91.6%
  4. Llama 3.3 70B Instruct (Meta): 91.1%
  5. o1-preview (OpenAI): 90.8%
  6. Claude 3 Opus (Anthropic): 90.7%
  7. Llama 4 Scout (Meta): 90.6%
  8. GPT-4o (OpenAI): 90.5%

### Best Open-Source Multilingual Models (May 2026)

- **Qwen 3 235B-A22B:** Currently the top general-purpose open multilingual model; supports 100+ languages/dialects, Apache 2.0 license
- **Llama 4 Maverick/Scout:** Strong on MGSM; Scout noted for long context (256K+)
- **DeepSeek-V3.2:** Strong overall
- **For African languages specifically:**
  - Lugha-Llama: Best open-weight model on IrokoBench for African languages
  - AfriqueLLM: Suite adapted for 20-24 African languages
  - MzansiLM: Covers 11 South African languages (UCT, 2026)
  - Cheetah: Supports 517 African languages

---

Sources:
- [The Token Tax - arXiv](https://arxiv.org/abs/2509.05486)
- [The Token Tax - ACL Anthology](https://aclanthology.org/2026.africanlp-main.10/)
- [Why Do Multilingual Reasoning Gaps Emerge - arXiv](https://arxiv.org/abs/2510.27269)
- [Causal Estimation of Tokenisation Bias - arXiv](https://arxiv.org/abs/2506.03149)
- [The Script Tax - arXiv](https://arxiv.org/abs/2602.11174)
- [Language-Reasoning Disentanglement - arXiv](https://arxiv.org/abs/2505.15257)
- [Reducing Tokenization Premiums - arXiv](https://arxiv.org/abs/2601.13328)
- [IrokoBench / AfriMMLU - arXiv](https://arxiv.org/abs/2406.03368)
- [MGSM Leaderboard](https://llm-stats.com/benchmarks/mgsm)
- [Lugha-Llama - arXiv](https://arxiv.org/abs/2504.06536)
- [BenchLM Multilingual Benchmarks 2026](https://benchlm.ai/multilingual)
- [Top Open-Source LLMs 2026](https://kairntech.com/blog/articles/top-open-source-llm-models-in-2026/)
- [Best Open Source LLMs 2026](https://www.miniloop.ai/blog/best-open-source-llms-2026)
- [UCT MzansiLM](https://www.news.uct.ac.za/article/-2026-05-04-uct-researchers-develop-ai-model-for-11-south-african-languages)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6f5bfcb-02da-471e-8e78-13964f894479",
  "isSidechain": true,
  "agentId": "ab6365162daadbc82",
  "requestId": "req_011CbCTYiQomYaeUvo7UJSU5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74e9be28-c2a9-47c8-947a-979a13dd60b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YF4YmDuMG65xUe6jpcrWhU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1691,
      "cache_read_input_tokens": 21390,
      "output_tokens": 2654,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1691
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2654,
          "cache_read_input_tokens": 21390,
          "cache_creation_input_tokens": 1691,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1691,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---
