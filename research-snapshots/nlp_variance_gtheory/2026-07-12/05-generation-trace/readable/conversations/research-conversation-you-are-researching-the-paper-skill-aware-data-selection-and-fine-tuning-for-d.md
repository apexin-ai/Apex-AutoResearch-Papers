# Research conversation: You are researching the paper "Skill-Aware Data Selection and Fine-Tuning for Data-Efficient Reasoning Distillation" by 

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a351cc21b62865b86.jsonl`
- **Structured JSON:** [`ac3e01e49b064d13a8ef.json`](../../sessions/ac/ac3e01e49b064d13a8ef.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-29T05:36:50.882Z_

You are researching the paper "Skill-Aware Data Selection and Fine-Tuning for Data-Efficient Reasoning Distillation" by Lechen Zhang et al., arXiv 2026, at https://arxiv.org/abs/2601.10109

Tasks:
1. Use WebFetch to read the arxiv abstract page for this paper.
2. Use WebFetch to read the full PDF content at https://arxiv.org/pdf/2601.10109
3. Use WebSearch for "Skill-Aware Data Selection Fine-Tuning Reasoning Distillation Lechen Zhang 2026" to find any additional info.

For each fetch, extract:
- Abstract and key claims
- Problem identification: what gap did they find?
- Key insight: how do they label skills? How do they prioritize weak skills?
- Technical method: how does skill decomposition work? What's the data selection strategy?
- Key results: the +1.6% improvement from 1K out of 100K examples
- How do they treat skills — flat labels vs dependency structure?
- Any limitations

Report all findings in detail. This is for a research analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f933bd5a-1f38-482e-9a55-8990f3e8a283",
  "agentId": "a351cc21b62865b86",
  "type": "user",
  "uuid": "229ee8d7-028a-4fa4-add2-273f466a2d95",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6388a8b4-70e1-462a-a675-27840ef57338",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-29T05:36:50.884Z_

```json
{
  "parentUuid": "229ee8d7-028a-4fa4-add2-273f466a2d95",
  "isSidechain": true,
  "agentId": "a351cc21b62865b86",
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
  "uuid": "e743b1cc-4e2f-4fce-8720-516accbad55c",
  "timestamp": "2026-05-29T05:36:50.884Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6388a8b4-70e1-462a-a675-27840ef57338",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-29T05:36:50.884Z_

```json
{
  "parentUuid": "e743b1cc-4e2f-4fce-8720-516accbad55c",
  "isSidechain": true,
  "agentId": "a351cc21b62865b86",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "affac254-6ddf-47d1-96c4-0d61bf32e9f3",
  "timestamp": "2026-05-29T05:36:50.884Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6388a8b4-70e1-462a-a675-27840ef57338",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-29T05:36:54.347Z_



I'll research this paper thoroughly. Let me start by fetching the arxiv page, the PDF, and running a web search in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "affac254-6ddf-47d1-96c4-0d61bf32e9f3",
  "isSidechain": true,
  "agentId": "a351cc21b62865b86",
  "requestId": "req_011CbWKTWEpTvRRTLHQuJsPb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07253312-6208-4051-a48b-02bc74e8ef83",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6388a8b4-70e1-462a-a675-27840ef57338",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GFWMM8hdew1PnRMc8LzuCG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1610,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1610,
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

_source line 5 · 2026-05-29T05:36:54.795Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HUddaAQFfvjwSGSMLtEfiu`</summary>

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
  "parentUuid": "07253312-6208-4051-a48b-02bc74e8ef83",
  "isSidechain": true,
  "agentId": "a351cc21b62865b86",
  "requestId": "req_011CbWKTWEpTvRRTLHQuJsPb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2970689-2221-4e0a-9efc-3b2b0634cce9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6388a8b4-70e1-462a-a675-27840ef57338",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GFWMM8hdew1PnRMc8LzuCG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1610,
      "cache_read_input_tokens": 7413,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1610
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 110,
          "cache_read_input_tokens": 7413,
          "cache_creation_input_tokens": 1610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1610,
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

_source line 6 · 2026-05-29T05:36:54.799Z_

<details><summary>↩ Tool result · `toolu_01HUddaAQFfvjwSGSMLtEfiu`</summary>

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
  "parentUuid": "e2970689-2221-4e0a-9efc-3b2b0634cce9",
  "isSidechain": true,
  "promptId": "f933bd5a-1f38-482e-9a55-8990f3e8a283",
  "agentId": "a351cc21b62865b86",
  "type": "user",
  "uuid": "86880197-993c-4a98-aa41-accb1dd513c4",
  "sourceToolAssistantUUID": "e2970689-2221-4e0a-9efc-3b2b0634cce9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6388a8b4-70e1-462a-a675-27840ef57338",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-29T05:36:57.623Z_



Now let me fetch the arxiv abstract page, the PDF, and run the web search all in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86880197-993c-4a98-aa41-accb1dd513c4",
  "isSidechain": true,
  "agentId": "a351cc21b62865b86",
  "requestId": "req_011CbWKToTuvP9eWEguZjpEC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8be52c5-b081-44ea-a5a3-08f1c32bd542",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6388a8b4-70e1-462a-a675-27840ef57338",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hn5j4EJfbiBxWGe8GKqvV4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 9023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1132,
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

_source line 8 · 2026-05-29T05:37:00.504Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Snnhjx15LvVmwAExTKYkqR`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.10109",
  "prompt": "Extract ALL information from this arxiv paper page. I need:\n1. Full title\n2. All authors\n3. Complete abstract text (every word)\n4. Submission date\n5. Any subject categories\n6. Any comments (e.g., number of pages, figures, tables)\nProvide everything verbatim, do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8be52c5-b081-44ea-a5a3-08f1c32bd542",
  "isSidechain": true,
  "agentId": "a351cc21b62865b86",
  "requestId": "req_011CbWKToTuvP9eWEguZjpEC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3fc87bcf-6593-4be6-a1d1-a656b71a7208",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6388a8b4-70e1-462a-a675-27840ef57338",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hn5j4EJfbiBxWGe8GKqvV4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 9023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1132,
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

_source line 9 · 2026-05-29T05:37:05.882Z_

<details><summary>↩ Tool result · `toolu_01Snnhjx15LvVmwAExTKYkqR`</summary>

```text
# Paper Information Extract

**1. Full Title:**
"Skill-Aware Data Selection and Fine-Tuning for Data-Efficient Reasoning Distillation"

**2. All Authors:**
- Lechen Zhang
- Yunxiang Zhang
- Wei Hu
- Lu Wang

**3. Complete Abstract:**
"Large reasoning models such as DeepSeek-R1 and their distilled variants achieve strong performance on complex reasoning tasks. Yet, distilling these models often demands large-scale data for supervised fine-tuning (SFT), motivating the pursuit of data-efficient training methods. To address this, we propose a skill-centric distillation framework that efficiently transfers reasoning ability to weaker models with two components: (1) Skill-based data selection, which prioritizes examples targeting the student model's weaker skills, and (2) Skill-aware fine-tuning, which encourages explicit skill decomposition during problem solving. With only 1,000 training examples selected from a 100K teacher-generated corpus, our method surpasses random SFT baselines by +1.6% on Qwen3-4B and +1.4% on Qwen3-8B across five mathematical reasoning benchmarks. Further analysis confirms that these gains concentrate on skills emphasized during training, highlighting the effectiveness of skill-centric training for efficient reasoning distillation."

**4. Submission Date:**
January 15, 2026

**5. Subject Categories:**
Computation and Language (cs.CL)

**6. Comments:**
No page count, figure count, or table information provided on the page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fc87bcf-6593-4be6-a1d1-a656b71a7208",
  "isSidechain": true,
  "promptId": "f933bd5a-1f38-482e-9a55-8990f3e8a283",
  "agentId": "a351cc21b62865b86",
  "type": "user",
  "uuid": "bd227c7c-aa78-4c06-b19a-9fde162bc8d9",
  "sourceToolAssistantUUID": "3fc87bcf-6593-4be6-a1d1-a656b71a7208",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6388a8b4-70e1-462a-a675-27840ef57338",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-29T05:37:06.422Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GnVa83DLtk21Wv6XzDNdeR`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2601.10109",
  "prompt": "Extract the COMPLETE content of this paper in full detail. I need:\n1. Full abstract\n2. Introduction - what is the problem? What gap did they find?\n3. Related work section\n4. Method section - FULL details on:\n   - How they decompose problems into skills\n   - How they label skills\n   - How they identify weak skills\n   - The data selection strategy\n   - Any skill dependency structure or hierarchy\n   - The fine-tuning procedure\n5. Experiments section - ALL results, especially:\n   - The +1.6% improvement from 1K out of 100K examples\n   - Baselines compared\n   - Datasets used\n   - Ablation studies\n6. Analysis and discussion\n7. Limitations section\n8. How they treat skills - flat labels vs dependency structure?\n9. Any figures or tables descriptions\n\nBe as detailed and thorough as possible. Extract every technical detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd227c7c-aa78-4c06-b19a-9fde162bc8d9",
  "isSidechain": true,
  "agentId": "a351cc21b62865b86",
  "requestId": "req_011CbWKToTuvP9eWEguZjpEC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3569d5cd-e560-42be-9815-c10fdc91062f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6388a8b4-70e1-462a-a675-27840ef57338",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hn5j4EJfbiBxWGe8GKqvV4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 9023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1132,
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

_source line 11 · 2026-05-29T05:37:07.216Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W6uXqSwznG3vVisSUvENwg`</summary>

```json
{
  "query": "Skill-Aware Data Selection Fine-Tuning Reasoning Distillation Lechen Zhang 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3569d5cd-e560-42be-9815-c10fdc91062f",
  "isSidechain": true,
  "agentId": "a351cc21b62865b86",
  "requestId": "req_011CbWKToTuvP9eWEguZjpEC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d63f16e7-ff26-478e-a8db-2bb3cd514dd1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6388a8b4-70e1-462a-a675-27840ef57338",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hn5j4EJfbiBxWGe8GKqvV4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 9023,
      "output_tokens": 508,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1132
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 508,
          "cache_read_input_tokens": 9023,
          "cache_creation_input_tokens": 1132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1132,
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

_source line 12 · 2026-05-29T05:37:13.880Z_

<details><summary>↩ Tool result · `toolu_01W6uXqSwznG3vVisSUvENwg`</summary>

```text
Web search results for query: "Skill-Aware Data Selection Fine-Tuning Reasoning Distillation Lechen Zhang 2026"

Links: [{"title":"[2601.10109] Skill-Aware Data Selection and Fine-Tuning for Data-Efficient Reasoning Distillation","url":"https://arxiv.org/abs/2601.10109"},{"title":"Skill-Aware Data Selection and Fine-Tuning for Data-Efficient Reasoning Distillation","url":"https://arxiv.org/html/2601.10109v1"},{"title":"Skill-Aware Data Selection and Fine-Tuning for Data-Efficient Reasoning Distillation","url":"https://arxiv.org/pdf/2601.10109"},{"title":"(PDF) Skill-Aware Data Selection and Fine-Tuning for Data-Efficient Reasoning Distillation","url":"https://www.researchgate.net/publication/399808695_Skill-Aware_Data_Selection_and_Fine-Tuning_for_Data-Efficient_Reasoning_Distillation"},{"title":"[Literature Review] Skill-Aware Data Selection and Fine-Tuning for Data-Efficient Reasoning Distillation","url":"https://www.themoonlight.io/en/review/skill-aware-data-selection-and-fine-tuning-for-data-efficient-reasoning-distillation"}]

I found the paper you're searching for! Here are the details:

**Title:** Skill-Aware Data Selection and Fine-Tuning for Data-Efficient Reasoning Distillation

**Authors:** Lechen Zhang, Yunxiang Zhang, Wei Hu, and Lu Wang from University of Michigan, Ann Arbor

**Publication Date:** January 15, 2026

**Overview:** The paper addresses the challenge that distilling large reasoning models often demands large-scale data for supervised fine-tuning, proposing a skill-centric distillation framework with two components: skill-based data selection (prioritizing examples targeting the student model's weaker skills) and skill-aware fine-tuning (encouraging explicit skill decomposition during problem solving).

**Key Results:** With only 1,000 training examples selected from a 100K teacher-generated corpus, the method surpasses random SFT baselines by +1.6% on Qwen3-4B and +1.4% on Qwen3-8B across five mathematical reasoning benchmarks.

The paper is available on arXiv at: https://arxiv.org/abs/2601.10109


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d63f16e7-ff26-478e-a8db-2bb3cd514dd1",
  "isSidechain": true,
  "promptId": "f933bd5a-1f38-482e-9a55-8990f3e8a283",
  "agentId": "a351cc21b62865b86",
  "type": "user",
  "uuid": "14ff6342-7b38-48b0-8043-bfc12bf4ff93",
  "sourceToolAssistantUUID": "d63f16e7-ff26-478e-a8db-2bb3cd514dd1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6388a8b4-70e1-462a-a675-27840ef57338",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-29T05:37:16.518Z_

<details><summary>↩ Tool result · `toolu_01GnVa83DLtk21Wv6XzDNdeR`</summary>

```text
# Summary of "Skill-Aware Data Selection and Fine-Tuning for Data-Efficient Reasoning Distillation"

## Abstract
The paper presents a method for efficient reasoning model distillation through skill-aware data selection. The approach achieves significant performance gains by selectively fine-tuning on a small subset of training data labeled by underlying reasoning skills rather than using full datasets.

## Problem & Gap
The research addresses inefficiency in distilling reasoning capabilities from large language models. The authors identify that not all training examples equally contribute to student model improvement, and training data contains diverse reasoning skills that could be leveraged strategically for more efficient distillation.

## Core Method Components

**Skill Decomposition & Labeling:**
The framework decomposes reasoning problems into constituent skills required for solving them. Skills are identified through systematic analysis of reasoning trajectories and intermediate steps needed to reach solutions.

**Skill Identification Strategy:**
The authors employ a multi-step process:
- Analyze reasoning traces from teacher models
- Extract distinct reasoning skills appearing across problems
- Assign skill labels to training examples based on which skills they require

**Weak Skill Detection:**
The approach identifies skills where student models show performance gaps relative to the teacher model, prioritizing data samples containing these skills.

**Data Selection Mechanism:**
Rather than random or full-data approaches, the method selects examples strategically:
- Identifies which skills the student model struggles with
- Prioritizes training examples requiring those weak skills
- Focuses computational resources on high-impact samples

**Fine-Tuning Procedure:**
The distillation process involves supervised fine-tuning using the selected skill-aware subset rather than exhaustive training data.

## Key Results
The paper demonstrates that training on just 1,000 carefully selected examples (1% of a 100,000-example dataset) achieves improvements of approximately 1.6 percentage points over baseline approaches. This represents substantial data efficiency gains in reasoning task distillation.

## Skill Treatment Structure
Skills are treated as discrete labels assigned to training examples rather than as a formal dependency hierarchy. However, the method recognizes relationships between skills through analysis of which skills appear together in reasoning processes.

## Experimental Setup
- **Datasets:** Mathematical reasoning and other complex reasoning benchmarks
- **Baselines:** Random sampling, full-data training, and other data selection methods
- **Ablations:** Tests validating the importance of skill identification and weak skill prioritization

## Analysis Findings
The approach demonstrates that selective data focusing on weak skills substantially outperforms random sampling. The research provides evidence that "skill-aware selection targets high-impact training examples more effectively than generic sampling strategies."

## Limitations & Considerations
The method's effectiveness depends on accurate skill identification and labeling quality. Performance gains are task-dependent and may vary based on skill granularity and dataset characteristics.

[Binary content (application/pdf, 460.5KB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/6388a8b4-70e1-462a-a675-27840ef57338/tool-results/webfetch-1780033026438-gdmtqw.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3569d5cd-e560-42be-9815-c10fdc91062f",
  "isSidechain": true,
  "promptId": "f933bd5a-1f38-482e-9a55-8990f3e8a283",
  "agentId": "a351cc21b62865b86",
  "type": "user",
  "uuid": "7e419e0d-237d-4614-b80a-7e30b393c906",
  "sourceToolAssistantUUID": "3569d5cd-e560-42be-9815-c10fdc91062f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6388a8b4-70e1-462a-a675-27840ef57338",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-29T05:37:20.910Z_

Good, I have the abstract and a summary from the PDF. The PDF extraction was somewhat summarized by the processing model, so let me fetch the HTML version for more detailed technical content, and also fetch the Moonlight review for additional insights.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e419e0d-237d-4614-b80a-7e30b393c906",
  "isSidechain": true,
  "agentId": "a351cc21b62865b86",
  "requestId": "req_011CbWKVQSdDpHvnviKCoEmb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5429f0a6-fce0-4cdf-be49-791712f0d1c5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6388a8b4-70e1-462a-a675-27840ef57338",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcRngZM7cwUWFkuZKi34CL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 652,
      "cache_creation_input_tokens": 1636,
      "cache_read_input_tokens": 10155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1636,
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

_source line 15 · 2026-05-29T05:37:30.327Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016fEPyptvUvR2zc8Qptw3KM`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.10109v1",
  "prompt": "Extract the COMPLETE technical details from this paper. I need EVERYTHING from:\n\n1. INTRODUCTION: What specific gap/problem motivates this work? What are the key observations?\n\n2. METHOD section - every detail:\n   - How exactly do they define \"skills\"? What taxonomy do they use?\n   - How do they label each training example with skills? Do they use an LLM to tag skills?\n   - How do they measure which skills are \"weak\" for the student model?\n   - The exact data selection algorithm/procedure\n   - How does skill-aware fine-tuning work? Do they modify the training objective?\n   - Do they add skill labels to the prompt or the response during fine-tuning?\n   - Is there any skill dependency structure or is it flat?\n\n3. EXPERIMENTS - every result number:\n   - Which 5 math reasoning benchmarks?\n   - Exact accuracy numbers for all methods\n   - What teacher model generates the data?\n   - Baseline methods compared\n   - Ablation study results\n\n4. ANALYSIS section:\n   - Per-skill breakdown of improvements\n   - Any analysis of skill coverage\n   - How gains concentrate on skills emphasized during training\n\n5. LIMITATIONS - explicit and implicit\n\n6. Any skill taxonomy or list of specific skills they identify\n\nExtract verbatim text where possible, especially for technical definitions and algorithm descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5429f0a6-fce0-4cdf-be49-791712f0d1c5",
  "isSidechain": true,
  "agentId": "a351cc21b62865b86",
  "requestId": "req_011CbWKVQSdDpHvnviKCoEmb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57758fdc-9f9a-43ff-b212-282009b967ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6388a8b4-70e1-462a-a675-27840ef57338",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcRngZM7cwUWFkuZKi34CL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 652,
      "cache_creation_input_tokens": 1636,
      "cache_read_input_tokens": 10155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1636,
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

_source line 16 · 2026-05-29T05:37:32.655Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01B48qXsqyLMyiPVCNRKMJXy`</summary>

```json
{
  "url": "https://www.themoonlight.io/en/review/skill-aware-data-selection-and-fine-tuning-for-data-efficient-reasoning-distillation",
  "prompt": "Extract ALL information from this review/analysis of the paper. I need:\n1. Any critique or analysis of the method\n2. Any identified strengths and weaknesses\n3. Any additional technical details about the method\n4. Any discussion of limitations\n5. How they characterize the skill treatment (flat vs hierarchical)\nProvide everything in full detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57758fdc-9f9a-43ff-b212-282009b967ab",
  "isSidechain": true,
  "agentId": "a351cc21b62865b86",
  "requestId": "req_011CbWKVQSdDpHvnviKCoEmb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18947784-516d-4d3f-8fda-df4ba5d0dca3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6388a8b4-70e1-462a-a675-27840ef57338",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcRngZM7cwUWFkuZKi34CL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 652,
      "cache_creation_input_tokens": 1636,
      "cache_read_input_tokens": 10155,
      "output_tokens": 603,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1636
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 652,
          "output_tokens": 603,
          "cache_read_input_tokens": 10155,
          "cache_creation_input_tokens": 1636,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1636,
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

_source line 17 · 2026-05-29T05:37:40.104Z_

<details><summary>↩ Tool result · `toolu_01B48qXsqyLMyiPVCNRKMJXy`</summary>

```text
# Analysis of "Skill-Aware Data Selection and Fine-Tuning for Data-Efficient Reasoning Distillation"

## Critiques and Analysis

The review identifies a fundamental problem with traditional approaches: "traditional supervised fine-tuning (SFT) often treats all training data uniformly, neglecting the underlying skill structures." The paper presents this as a critical oversight in existing reasoning distillation methods.

A striking empirical finding challenges conventional wisdom: "fine-tuning on the full 100K corpus consistently degrades performance" relative to baseline models, suggesting that data quantity without strategic selection can harm model performance.

## Identified Strengths

1. **Hierarchical Skill Structure**: The framework explicitly uses a "hierarchical skill tree to inform data selection and training," enabling targeted learning rather than uniform data treatment.

2. **Computational Efficiency**: The skill attribution process achieves O(log N) complexity, making it scalable across large skill taxonomies.

3. **Robust Empirical Results**: Demonstrates "+1.6% accuracy gain on Qwen3-4B and +1.4% on Qwen3-8B" using only 1,000 selected examples from 100K candidates.

4. **Balanced Skill Mastery**: "Skill-based oversampling leads to a more balanced mastery across skills, flattening the per-skill accuracy curve."

## Identified Weaknesses and Limitations

1. **Limited Scale**: Experiments conducted only on "Qwen3-4B and Qwen3-8B models" with modest accuracy improvements (1.4-1.6%).

2. **Upfront Computational Cost**: Skill labeling requires "approximately 200 GPU hours" as a one-time investment.

3. **Taxonomy Dependency**: Framework relies on pre-defined skill hierarchies; performance with custom or poorly-designed taxonomies remains unclear.

4. **Narrow Evaluation Domain**: Testing restricted to "five diverse mathematical reasoning benchmarks," limiting generalizability claims.

## Technical Details

**Data Selection Mechanism**: Sampling probability inversely proportional to per-skill accuracy: P(skill) = clip(acc⁻¹, 0, w_max) / Σ clip(acc'⁻¹, 0, w_max), where w_max prevents excessive weighting of extremely weak skills.

**Skill-Aware Augmentation**: Training examples prepended with "explicit, ordered sequence of required skills" (e.g., "Skills: [Mathematics → Probability → Bayes' theorem]") to encourage structured decomposition.

## Skill Treatment Characterization

The framework explicitly employs **hierarchical skill organization**, not flat structures. The approach "navigates the tree, identifying high-level skills first and then drilling down to leaf nodes." Ablation studies confirm that "providing the full hierarchical skill chain" significantly outperforms using only "root-level or leaf-level skills," demonstrating the critical importance of hierarchical relationships for effective learning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18947784-516d-4d3f-8fda-df4ba5d0dca3",
  "isSidechain": true,
  "promptId": "f933bd5a-1f38-482e-9a55-8990f3e8a283",
  "agentId": "a351cc21b62865b86",
  "type": "user",
  "uuid": "26ba7092-87f0-4fa6-99ca-ff4d0a4b92f1",
  "sourceToolAssistantUUID": "18947784-516d-4d3f-8fda-df4ba5d0dca3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6388a8b4-70e1-462a-a675-27840ef57338",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-29T05:38:01.671Z_

<details><summary>↩ Tool result · `toolu_016fEPyptvUvR2zc8Qptw3KM`</summary>

````text
# Comprehensive Technical Extraction: Skill-Aware Data Selection for Reasoning Distillation

## 1. MOTIVATION & KEY OBSERVATIONS

**Core Gap:** Current reasoning distillation treats all training examples equally, overlooking latent data structure and model's current knowledge state. The authors observe that "human learning is highly structured, with knowledge organized hierarchically."

**Key Insight:** Models should receive more training data on weaker skills while avoiding redundancy on mastered competencies. Prior work either ignores atomic skill structure within problems or fails to adapt to individual model strengths/weaknesses.

---

## 2. METHOD DETAILS

### 2.1 Skill Definition & Taxonomy
The paper uses a **pre-defined hierarchical skill tree** from Instruct-SkillMix (Kaur et al., 2025), organizing mathematical problems into multi-level skills. Skills are defined as "atomic competencies" (e.g., addition, multiplication, probability, Bayes' theorem).

The hierarchy is **not flat**—they employ a tree structure with root-to-leaf organization. They also test alternative taxonomies (EvalTree) in generalization experiments.

### 2.2 Skill Attribution (Step 1)

**Process:** Each training problem's reference solution is mapped to relevant skills via top-down LLM-based attribution.

**Implementation:** Using Qwen2.5-32B-Instruct, they prompt the model to:
- Start at the root node and decide which high-level skill applies
- Recursively drill down at each level until reaching leaf nodes
- Select multiple skills if needed

**Key Quote:** "This recursive process leverages the hierarchical structure (with O(log N) complexity) to avoid overwhelming the model with a flat multi-label decision."

**Validation:** Manual inspection of ~100 random QA pairs found no evidence of missing/mislabeled skills.

**Computational Cost:** ~200 GPU hours for 100K examples (inference-only, amortizable across multiple students).

### 2.3 Skill-Based Sampling (Step 2)

**Measurement of Weakness:** Evaluate the student model on the entire 100K corpus, compute accuracy per leaf skill node.

**Sampling Formula:**
```
P(skill) = clip(acc_skill^(-1), 0, w_max) / Σ_skill' clip(acc_skill'^(-1), 0, w_max)

where w_max = 10,000 (empirically set to prevent divide-by-zero)
```

**Effect:** Probabilities are inversely proportional to per-skill accuracy. Underrepresented/difficult skills are emphasized; well-mastered skills are undersampled.

**Training Set Construction:** Using this distribution, they construct 1,000-example subsets from the 100K pool.

### 2.4 Skill-Aware Fine-Tuning (Step 3)

**Data Augmentation Strategy:** Prepend the explicit skill chain to each training instance before the solution.

**Example Format:**
```
Skills: [Mathematics → Probability → Bayes' theorem]
[Original problem + solution]
```

**Mechanism:** This encourages models to "explicitly traverse the required skills before attempting the solution, enabling fine-grained diagnostics."

**No Custom Training Objective:** Standard supervised fine-tuning is applied; the modification is purely data augmentation (prepending skill chains to prompts/responses).

---

## 3. EXPERIMENTS

### 3.1 Setup
- **Base Models:** Qwen3-4B and Qwen3-8B
- **Teacher Data:** 100K clean QA pairs extracted from OpenMathReasoning (DeepSeek-R1 outputs)
- **Evaluation Benchmarks (5 total):**
  1. AMC23
  2. AIME2024
  3. AIME2025
  4. MATH L5 (Level 5)
  5. OlympiadBench

- **Metric:** Avg@8 accuracy (average over 8 independent samples per question)
- **Training Details:** 5 epochs, batch size 32, learning rate 1e-5, max sequence length 8192

### 3.2 Main Results (Table 1)

**Qwen3-4B (1K examples):**
| Method | AMC23 | AIME2024 | AIME2025 | MATH L5 | OlympiadBench | Average |
|--------|-------|----------|----------|---------|---------------|---------|
| Base | 90.1 | 61.1 | 50.7 | 84.3 | 49.1 | 67.1 |
| Random SFT | 89.5 | 60.1 | 50.3 | 85.3 | 49.0 | 66.8 |
| Random + Skill-aware SFT | 90.9 | 62.2 | 49.9 | 85.8 | 49.0 | 67.6 |
| Skill-based SFT | 89.1 | 62.5 | 50.0 | 85.5 | 49.5 | 67.3 |
| **Skill-based + Skill-aware** | **91.9** | **64.6** | **50.8** | **85.3** | **49.6** | **68.4** |

**Improvement:** +1.6% over random sampling

---

**Qwen3-8B (1K examples):**
| Method | AMC23 | AIME2024 | AIME2025 | MATH L5 | OlympiadBench | Average |
|--------|-------|----------|----------|---------|---------------|---------|
| Base | 88.2 | 61.1 | 50.2 | 84.7 | 49.1 | 66.7 |
| Random SFT | 90.2 | 62.6 | 50.8 | 86.0 | 50.7 | 68.1 |
| Random + Skill-aware SFT | 91.5 | 65.7 | 52.6 | 86.6 | 50.4 | 69.4 |
| Skill-based SFT | 93.4 | 62.1 | 51.3 | 86.2 | 49.7 | 68.5 |
| **Skill-based + Skill-aware** | **91.9** | **67.1** | **50.0** | **86.6** | **51.6** | **69.5** |

**Improvement:** +1.4% over random sampling

---

**Critical Finding:** Training on the full 100K corpus degrades performance relative to base models (Qwen3-4B: 58.1% avg vs. 67.1% base), emphasizing data quality over quantity.

### 3.3 Ablation Studies

**Effect of Sampling Aggressiveness (varying exponent T in acc^-T):**

| T Value | Avg Accuracy |
|---------|--------------|
| T=0.5 | 70.7% |
| T=0.75 | 71.3% |
| **T=1.0** | **71.9%** |
| T=2.0 | 72.0% |
| T=3.0 | 71.9% |

Performance rises quickly then saturates; T=1.0 provides optimal balance.

---

**Full Skill Chain Necessity:**

| Configuration | Avg Accuracy |
|---------------|--------------|
| Full skill chain | **72.9%** |
| Root skills only | 72.2% |
| Leaf skills only | 72.7% |

Full hierarchy outperforms single-layer variants, confirming that "training with the complete skill tree structure is beneficial."

### 3.4 Per-Skill Analysis (Figure 2 & MATH-500)

**Key Finding:** Skill-based sampling "improves weaker skills while preserving strong ones, flattening the accuracy curve toward balanced mastery."

- Weaker skills sampled more frequently show largest accuracy gains
- Stronger skills maintain high accuracy despite reduced sampling
- Skill-aware augmentation further flattens the curve

The paper quantifies this by examining 500 MATH problems across distinct skill categories, showing more balanced skill-level performance.

### 3.5 Generalization Studies (Appendix C)

**C.1 - Skill Tree Variants:** EvalTree taxonomy yields comparable/better results than Instruct-SkillMix:
- Qwen3-4B with EvalTree: 68.2% avg vs. 67.3% with Instruct-SkillMix
- Qwen3-8B with EvalTree: 68.8% avg vs. 68.5% with Instruct-SkillMix

**C.2 - Model Family Generalization:** DeepSeek-R1-Distill-Llama-8B:
- Skill-based + Skill-aware: 53.0% avg
- Random SFT: 52.0% avg
- Improvement: +1.0%

**C.3 - Comparison to Existing Methods (Table 4, Qwen3-4B):**

| Method | AMC23 | AIME2024 | AIME2025 | MATH L5 | Average |
|--------|-------|----------|----------|---------|---------|
| Base | 90.1 | 61.1 | 50.7 | 84.3 | 71.6 |
| Random | 89.5 | 60.1 | 50.3 | 85.3 | 71.3 |
| LIMO (offline) | 88.4 | 61.3 | 45.4 | 85.3 | 70.1 |
| S1 (offline) | 89.1 | 57.9 | 47.5 | 85.9 | 70.1 |
| S1 (online) | 89.1 | 60.7 | 50.2 | 84.9 | 71.2 |
| **This work** | **91.9** | **64.6** | **50.8** | **85.3** | **73.2** |

Their method consistently outperforms LIMO and S1 baselines across all benchmarks.

---

## 4. ANALYSIS & INSIGHTS

**Mechanism of Improvement:** The paper demonstrates gains concentrate on emphasized skills:
- Weak skills receive larger accuracy improvements when prioritized
- Strong skills maintain performance despite reduced data allocation
- This suggests "models waste training cost on areas where they already excel"

**Interpretability Benefit:** By embedding skill chains in training data, "models learn to both solve problems and internalize how different levels of skills are organized."

---

## 5. LIMITATIONS (Section 6)

1. **Skill Tree Dependency:** Method relies on existing taxonomies; alternative hierarchies may misalign with student model's decomposition
2. **Noisy Per-Skill Evaluation:** Accuracy estimates can be unstable with limited evaluation data per skill; uncertainty modeling could improve robustness
3. **Limited Scale:** Evaluation on only 4B and 8B models; larger model validation needed
4. **No Custom Loss:** Uses standard SFT without skill-specific weighting in the training objective

---

## 6. KEY IMPLEMENTATION DETAILS

| Aspect | Value |
|--------|-------|
| Student Models | Qwen3-4B, Qwen3-8B |
| Skill Labeling Model | Qwen2.5-32B-Instruct |
| Training Data | 100K OpenMathReasoning pairs |
| Selected Subset | 1,000 examples |
| Epochs | 5 |
| Batch Size | 32 (8 GPUs × 4 accumulation) |
| Learning Rate | 1e-5 |
| Optimizer | AdamW with cosine schedule |
| Warmup | 10% of steps |
| GPU Cost (Labeling) | ~200 hours (amortizable) |
| GPU Cost (SFT per run) | ~40 hours per model |
| Hardware | NVIDIA A40 (48GB) |

---

## 7. SPECIFIC SKILLS IDENTIFIED

The paper does not enumerate a complete skill taxonomy (it references existing taxonomies). Example skills mentioned:
- Basic arithmetic (addition, subtraction)
- Probability theory
- Bayes' theorem
- Geometry
- Mathematical reasoning at various hierarchical levels

The actual taxonomy is drawn from Instruct-SkillMix or EvalTree (external sources).

---

**Code & Data Availability:** https://github.com/orange0629/skill-data-selection
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57758fdc-9f9a-43ff-b212-282009b967ab",
  "isSidechain": true,
  "promptId": "f933bd5a-1f38-482e-9a55-8990f3e8a283",
  "agentId": "a351cc21b62865b86",
  "type": "user",
  "uuid": "b8d37261-e0a4-43c0-a1a1-89243897bf1e",
  "sourceToolAssistantUUID": "57758fdc-9f9a-43ff-b212-282009b967ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6388a8b4-70e1-462a-a675-27840ef57338",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-29T05:38:05.356Z_

Excellent. I now have comprehensive information. Let me fetch one more source to get any additional details about the specific skill taxonomies and the GitHub repository.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8d37261-e0a4-43c0-a1a1-89243897bf1e",
  "isSidechain": true,
  "agentId": "a351cc21b62865b86",
  "requestId": "req_011CbWKYiuiMyMqpxesLwqmr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb35dfa7-e67f-4b4f-9516-987ce1a639e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6388a8b4-70e1-462a-a675-27840ef57338",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCqdV29dE3mpMQvmmvWLeG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 701,
      "cache_creation_input_tokens": 4371,
      "cache_read_input_tokens": 11791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4371,
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

_source line 20 · 2026-05-29T05:38:07.521Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012J9SXKjV3Ec7TV77qvmJh9`</summary>

```json
{
  "url": "https://github.com/orange0629/skill-data-selection",
  "prompt": "Extract all information about this repository:\n1. README contents - any details about the method, code structure, how to run\n2. Any information about the skill taxonomy used\n3. Any example skill trees or skill lists\n4. Any additional implementation details not in the paper\n5. Data formats and examples"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb35dfa7-e67f-4b4f-9516-987ce1a639e5",
  "isSidechain": true,
  "agentId": "a351cc21b62865b86",
  "requestId": "req_011CbWKYiuiMyMqpxesLwqmr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd3fa12e-d404-445f-bae3-5937647adb7f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6388a8b4-70e1-462a-a675-27840ef57338",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCqdV29dE3mpMQvmmvWLeG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 701,
      "cache_creation_input_tokens": 4371,
      "cache_read_input_tokens": 11791,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4371
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 701,
          "output_tokens": 178,
          "cache_read_input_tokens": 11791,
          "cache_creation_input_tokens": 4371,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4371,
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

_source line 21 · 2026-05-29T05:38:11.605Z_

<details><summary>↩ Tool result · `toolu_012J9SXKjV3Ec7TV77qvmJh9`</summary>

```text
# Repository Analysis: skill-data-selection

Based on the provided web page content, I cannot extract the requested information because **the repository is empty**.

The GitHub page explicitly states: "This repository is empty."

## What's Available:
- Repository name: `skill-data-selection`
- Owner: `orange0629`
- Status: Public repository
- Current content: None (no README, code files, or documentation)

## What's Missing:
1. **README contents** - Not present
2. **Skill taxonomy information** - Not available
3. **Example skill trees/lists** - Not provided
4. **Implementation details** - Absent
5. **Data formats and examples** - No files to reference

## Recommendation:
To obtain the information you're seeking about methodology, code structure, skill taxonomies, and implementation details, you would need to either:
- Contact the repository owner directly
- Check if related documentation exists elsewhere
- Wait for content to be added to this repository
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd3fa12e-d404-445f-bae3-5937647adb7f",
  "isSidechain": true,
  "promptId": "f933bd5a-1f38-482e-9a55-8990f3e8a283",
  "agentId": "a351cc21b62865b86",
  "type": "user",
  "uuid": "1370d610-c6bd-4d8f-a9e3-768ffddc5f4a",
  "sourceToolAssistantUUID": "dd3fa12e-d404-445f-bae3-5937647adb7f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6388a8b4-70e1-462a-a675-27840ef57338",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-29T05:39:33.495Z_

The repository is empty (code not yet released). I now have all the information needed for a comprehensive report. Here is the full research analysis:

---

## Comprehensive Research Analysis: "Skill-Aware Data Selection and Fine-Tuning for Data-Efficient Reasoning Distillation"

**Authors:** Lechen Zhang, Yunxiang Zhang, Wei Hu, Lu Wang (University of Michigan, Ann Arbor)
**Published:** January 15, 2026, arXiv:2601.10109
**Category:** Computation and Language (cs.CL)
**Code:** https://github.com/orange0629/skill-data-selection (repository exists but is currently empty)

---

### Abstract and Key Claims

Large reasoning models such as DeepSeek-R1 and their distilled variants achieve strong performance on complex reasoning tasks, but distilling them often demands large-scale data for supervised fine-tuning (SFT). The authors propose a **skill-centric distillation framework** with two components:

1. **Skill-based data selection** -- prioritizes examples targeting the student model's weaker skills
2. **Skill-aware fine-tuning** -- encourages explicit skill decomposition during problem solving

With only **1,000 training examples selected from a 100K teacher-generated corpus**, their method surpasses random SFT baselines by **+1.6% on Qwen3-4B** and **+1.4% on Qwen3-8B** across five mathematical reasoning benchmarks. Gains concentrate on skills emphasized during training.

---

### Problem Identification: The Gap

The paper identifies several gaps:

1. **Uniform data treatment:** Traditional SFT treats all training examples equally, neglecting latent skill structure within problems. This ignores the fact that not all examples contribute equally to student improvement.

2. **Quantity over quality failure:** A critical empirical finding is that fine-tuning on the **full 100K corpus consistently degrades performance** relative to base models (Qwen3-4B drops from 67.1% to 58.1% average). This directly challenges the "more data is better" assumption.

3. **No adaptation to student state:** Prior work does not adapt data selection to the individual student model's strengths and weaknesses. The paper draws an analogy to human learning: "human learning is highly structured, with knowledge organized hierarchically" -- models should receive more training on weaker skills while avoiding redundancy on mastered competencies.

---

### Key Insight: How They Label Skills and Prioritize Weak Skills

**Skill labeling** uses a **pre-defined hierarchical skill tree** from Instruct-SkillMix (Kaur et al., 2025), which organizes mathematical problems into multi-level skills. Skills are defined as "atomic competencies" (e.g., addition, multiplication, probability, Bayes' theorem).

The labeling process is **LLM-based and top-down recursive:**
- They use **Qwen2.5-32B-Instruct** to attribute skills to each training example
- The model starts at the root node, decides which high-level skill applies, then recursively drills down to leaf nodes
- Multiple skills can be assigned per problem
- This recursive traversal has **O(log N) complexity**, avoiding overwhelming the model with a flat multi-label decision over all possible skills

**Validation:** Manual inspection of ~100 random QA pairs found no evidence of missing or mislabeled skills.

**Weak skill identification:** They evaluate the student model on the entire 100K corpus, then compute **per-skill accuracy at the leaf level**. Skills with lower accuracy are deemed "weak."

---

### Technical Method in Detail

#### Step 1: Skill Attribution
Each problem's reference solution is mapped to relevant skills via top-down LLM-based attribution using the hierarchical taxonomy. Cost: ~200 GPU hours for 100K examples (inference-only, amortizable across multiple students).

#### Step 2: Skill-Based Sampling (Data Selection)
The sampling probability is **inversely proportional to per-skill accuracy:**

```
P(skill) = clip(acc_skill^(-1), 0, w_max) / Sigma_skill' clip(acc_skill'^(-1), 0, w_max)
```

Where `w_max = 10,000` (empirically set to prevent extreme weighting from near-zero accuracy skills). This ensures underperforming/difficult skills are emphasized while well-mastered skills are undersampled. Using this distribution, they construct 1,000-example subsets from the 100K pool.

#### Step 3: Skill-Aware Fine-Tuning (Data Augmentation)
They **prepend the explicit skill chain** to each training instance before the solution:

```
Skills: [Mathematics -> Probability -> Bayes' theorem]
[Original problem + solution]
```

This is purely a **data augmentation** strategy -- no custom training objective or loss function is used. Standard SFT is applied. The skill chain encourages models to "explicitly traverse the required skills before attempting the solution, enabling fine-grained diagnostics."

**Training details:**
- 5 epochs, batch size 32 (8 GPUs x 4 accumulation steps)
- Learning rate: 1e-5, AdamW with cosine schedule, 10% warmup
- Max sequence length: 8192
- Hardware: NVIDIA A40 (48GB)
- SFT cost: ~40 GPU hours per model

---

### Skill Treatment: Hierarchical, Not Flat

This is a critical architectural choice. The paper explicitly uses a **tree-structured hierarchy**, not flat labels:

- Skills are organized in a root-to-leaf tree structure
- Attribution traverses the tree top-down
- The full skill chain (e.g., `Mathematics -> Probability -> Bayes' theorem`) is preserved

**Ablation confirming hierarchy matters:**

| Configuration | Avg Accuracy |
|---|---|
| Full skill chain | **72.9%** |
| Root skills only | 72.2% |
| Leaf skills only | 72.7% |

The full hierarchy outperforms single-layer variants. The paper states: "training with the complete skill tree structure is beneficial."

However, it is important to note that while the skill taxonomy is hierarchical, **there is no formal dependency graph between skills** (e.g., no explicit modeling of "skill A is a prerequisite for skill B"). The hierarchy is a classification taxonomy (is-a relationship), not a prerequisite/dependency structure. Skills are treated as multi-level categories for labeling and sampling purposes.

---

### Key Results

#### Main Results (1K examples from 100K, Avg@8 accuracy)

**Qwen3-4B:**

| Method | AMC23 | AIME2024 | AIME2025 | MATH L5 | OlympiadBench | Average |
|---|---|---|---|---|---|---|
| Base (no SFT) | 90.1 | 61.1 | 50.7 | 84.3 | 49.1 | 67.1 |
| Random SFT | 89.5 | 60.1 | 50.3 | 85.3 | 49.0 | 66.8 |
| Random + Skill-aware SFT | 90.9 | 62.2 | 49.9 | 85.8 | 49.0 | 67.6 |
| Skill-based selection only | 89.1 | 62.5 | 50.0 | 85.5 | 49.5 | 67.3 |
| **Skill-based + Skill-aware** | **91.9** | **64.6** | **50.8** | **85.3** | **49.6** | **68.4** |

Delta vs random SFT: **+1.6%**

**Qwen3-8B:**

| Method | AMC23 | AIME2024 | AIME2025 | MATH L5 | OlympiadBench | Average |
|---|---|---|---|---|---|---|
| Base | 88.2 | 61.1 | 50.2 | 84.7 | 49.1 | 66.7 |
| Random SFT | 90.2 | 62.6 | 50.8 | 86.0 | 50.7 | 68.1 |
| **Skill-based + Skill-aware** | **91.9** | **67.1** | **50.0** | **86.6** | **51.6** | **69.5** |

Delta vs random SFT: **+1.4%**

#### Critical Finding: Full Data Hurts
Training on the full 100K corpus **degrades** Qwen3-4B from 67.1% (base) to 58.1% average -- a massive 9% drop. This powerfully motivates careful data selection.

#### Comparison to Existing Methods (Qwen3-4B)

| Method | Average |
|---|---|
| LIMO (offline) | 70.1 |
| S1 (offline) | 70.1 |
| S1 (online) | 71.2 |
| **This work** | **73.2** |

Consistently outperforms LIMO and S1 baselines.

#### Ablation: Sampling Aggressiveness (exponent T in acc^-T)

| T | Avg |
|---|---|
| 0.5 | 70.7% |
| 0.75 | 71.3% |
| 1.0 | 71.9% |
| 2.0 | 72.0% |
| 3.0 | 71.9% |

Performance rises quickly then saturates; T=1.0 is optimal.

#### Generalization: Alternative Taxonomy (EvalTree)
EvalTree taxonomy yields comparable or slightly better results than Instruct-SkillMix (Qwen3-4B: 68.2% vs 67.3%), suggesting the method is not overly sensitive to the specific taxonomy used.

#### Generalization: Different Model Family
DeepSeek-R1-Distill-Llama-8B: +1.0% improvement (53.0% vs 52.0% random SFT).

---

### Per-Skill Analysis

The paper demonstrates that skill-based sampling "improves weaker skills while preserving strong ones, flattening the accuracy curve toward balanced mastery." Specifically:
- Weaker skills that are sampled more frequently show the **largest accuracy gains**
- Stronger skills **maintain high accuracy** despite reduced sampling allocation
- This suggests "models waste training cost on areas where they already excel"
- Skill-aware augmentation further flattens the per-skill accuracy curve

The per-skill analysis on MATH-500 across distinct skill categories confirms more balanced skill-level performance.

---

### Limitations

**Explicit (from Section 6):**
1. **Skill tree dependency:** The method relies on existing pre-defined taxonomies. Alternative or poorly-designed hierarchies may misalign with the student model's actual decomposition of skills.
2. **Noisy per-skill evaluation:** Per-skill accuracy estimates can be unstable when there are limited evaluation examples per skill. Uncertainty modeling could improve robustness.
3. **Limited model scale:** Evaluated only on 4B and 8B parameter models. Validation on larger models is needed.
4. **No custom loss:** Uses standard SFT without skill-specific weighting in the training objective -- a natural but unexplored extension.

**Implicit limitations I identify:**
5. **Domain specificity:** Only tested on mathematical reasoning. Whether the skill-based framework transfers to code, science, or general reasoning is unknown.
6. **Taxonomy availability:** The method assumes a suitable hierarchical skill taxonomy exists for the domain. Creating such taxonomies for new domains may be non-trivial.
7. **Modest absolute gains:** The +1.6% improvement, while statistically meaningful, is relatively small. The practical significance depends on the application.
8. **Evaluation metric sensitivity:** Using Avg@8 (averaging over 8 samples) could mask variance issues.
9. **No dependency modeling:** Skills are organized taxonomically but without prerequisite/dependency relationships. A student might benefit from learning foundational skills before advanced ones, but this ordering is not captured.
10. **Static skill assessment:** The student's weak skills are assessed once before selection. An iterative/curriculum-style approach that reassesses skills during training might yield further gains.

---

### Summary of Key Takeaways for Research Analysis

- The core contribution is framing distillation as a **skill-aware curriculum** problem rather than a uniform sampling problem
- The hierarchical skill tree is borrowed from existing work (Instruct-SkillMix), not a novel contribution in itself
- The inverse-accuracy sampling formula is simple but effective
- The skill-chain prepending is a lightweight augmentation that requires no architectural changes
- The finding that **100K full-data SFT hurts performance** is arguably the most striking result
- Skills are treated as a **taxonomic hierarchy** (classification tree), not as a **dependency graph** with prerequisite relationships
- The method is validated primarily on math and on relatively small models (4B, 8B)
- Code has not been released yet despite a GitHub repository being created

Sources:
- [arXiv Abstract](https://arxiv.org/abs/2601.10109)
- [arXiv HTML](https://arxiv.org/html/2601.10109v1)
- [arXiv PDF](https://arxiv.org/pdf/2601.10109)
- [Moonlight Review](https://www.themoonlight.io/en/review/skill-aware-data-selection-and-fine-tuning-for-data-efficient-reasoning-distillation)
- [ResearchGate](https://www.researchgate.net/publication/399808695_Skill-Aware_Data_Selection_and_Fine-Tuning_for_Data-Efficient_Reasoning_Distillation)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1370d610-c6bd-4d8f-a9e3-768ffddc5f4a",
  "isSidechain": true,
  "agentId": "a351cc21b62865b86",
  "requestId": "req_011CbWKZTPLcU1P1nxRfhbxd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c2b4723-3005-4bb4-9900-21f84021669f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6388a8b4-70e1-462a-a675-27840ef57338",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Tzw2TmZkS4i8uYiB9A6sp",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 16162,
      "output_tokens": 3343,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1204
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3343,
          "cache_read_input_tokens": 16162,
          "cache_creation_input_tokens": 1204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1204,
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
