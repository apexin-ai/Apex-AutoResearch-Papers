# Research conversation: I need to deeply research the paper PROF (arXiv 2509.03403, September 2025) which uses PRM+ORM for data curation in iter

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a4fe046b7e78cd743.jsonl`
- **Structured JSON:** [`a82b461b38ee78ca1015.json`](../../sessions/a8/a82b461b38ee78ca1015.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

37 recorded events

### User

_source line 1 · 2026-05-19T09:22:55.502Z_

I need to deeply research the paper PROF (arXiv 2509.03403, September 2025) which uses PRM+ORM for data curation in iterative RL training. This is a critical missing competitor for a research proposal about using multi-verifier disagreement for synthetic data curation.

Please:
1. Search for "PROF PRM ORM iterative RL training arXiv 2509.03403" and related queries
2. Fetch and read the actual paper from arxiv.org (try https://arxiv.org/abs/2509.03403 and the PDF)
3. Extract:
   - The exact method: how does PROF use PRM and ORM together?
   - Does it use agreement/consistency to FILTER data (as claimed by the reviewer)?
   - How does it handle the interplay between different verifier types?
   - What benchmarks and baselines does it use?
   - What are its key results and limitations?
   - How does it relate to using disagreement (the INVERSE of what PROF does) as a signal?

Report your findings in detail. This is crucial for positioning our work against PROF.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ae35a659-7407-4079-9c58-2bf4f6ffeb73",
  "agentId": "a4fe046b7e78cd743",
  "type": "user",
  "uuid": "f974e2de-4267-4b30-9e0b-fb222808dd41",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T09:22:55.506Z_

```json
{
  "parentUuid": "f974e2de-4267-4b30-9e0b-fb222808dd41",
  "isSidechain": true,
  "agentId": "a4fe046b7e78cd743",
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
  "uuid": "797e77de-2e2d-465b-a5f0-4d66b6566411",
  "timestamp": "2026-05-19T09:22:55.506Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T09:22:55.506Z_

```json
{
  "parentUuid": "797e77de-2e2d-465b-a5f0-4d66b6566411",
  "isSidechain": true,
  "agentId": "a4fe046b7e78cd743",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f7d3917c-6956-4188-8cda-d19ddb7e1f43",
  "timestamp": "2026-05-19T09:22:55.506Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T09:22:58.097Z_



I'll research the PROF paper thoroughly. Let me start by searching for it and fetching the actual paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7d3917c-6956-4188-8cda-d19ddb7e1f43",
  "isSidechain": true,
  "agentId": "a4fe046b7e78cd743",
  "requestId": "req_011CbBgcFk4iK4AoQe2E3iPk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5f6d393-ac67-4191-a36c-aed3c4029c51",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LqcXccczzFxiaCNWcEFFzV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9379,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9379,
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

_source line 5 · 2026-05-19T09:22:58.661Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LabHAeV4kSXREMwRniRu3D`</summary>

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
  "parentUuid": "b5f6d393-ac67-4191-a36c-aed3c4029c51",
  "isSidechain": true,
  "agentId": "a4fe046b7e78cd743",
  "requestId": "req_011CbBgcFk4iK4AoQe2E3iPk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3f10d60-98f8-4c62-a2bb-d22cb427c0be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LqcXccczzFxiaCNWcEFFzV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9379,
      "cache_read_input_tokens": 0,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9379
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 104,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9379,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9379,
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

_source line 6 · 2026-05-19T09:22:58.664Z_

<details><summary>↩ Tool result · `toolu_01LabHAeV4kSXREMwRniRu3D`</summary>

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
  "parentUuid": "d3f10d60-98f8-4c62-a2bb-d22cb427c0be",
  "isSidechain": true,
  "promptId": "ae35a659-7407-4079-9c58-2bf4f6ffeb73",
  "agentId": "a4fe046b7e78cd743",
  "type": "user",
  "uuid": "da7ed290-932e-4c01-8c4d-3d4f7582d4e1",
  "sourceToolAssistantUUID": "d3f10d60-98f8-4c62-a2bb-d22cb427c0be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T09:23:01.121Z_



Now let me search for the paper and fetch it simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da7ed290-932e-4c01-8c4d-3d4f7582d4e1",
  "isSidechain": true,
  "agentId": "a4fe046b7e78cd743",
  "requestId": "req_011CbBgcVUoukBWzJDF7nMSk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69b97d91-3ed6-49df-a9dc-b562bbcea200",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M1CxCwBBexsr9FzynUguxg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 8 · 2026-05-19T09:23:01.596Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MK3Log9WFZakVJq9UzyvKB`</summary>

```json
{
  "query": "PROF PRM ORM iterative RL training arXiv 2509.03403"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69b97d91-3ed6-49df-a9dc-b562bbcea200",
  "isSidechain": true,
  "agentId": "a4fe046b7e78cd743",
  "requestId": "req_011CbBgcVUoukBWzJDF7nMSk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "903421d1-8b5f-45dd-9125-adae0e06005c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M1CxCwBBexsr9FzynUguxg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 9 · 2026-05-19T09:23:02.550Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X9WQcnuYBwcpaVeEV5LQBM`</summary>

```json
{
  "query": "PROF paper \"process reward model\" \"outcome reward model\" data curation reinforcement learning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "903421d1-8b5f-45dd-9125-adae0e06005c",
  "isSidechain": true,
  "agentId": "a4fe046b7e78cd743",
  "requestId": "req_011CbBgcVUoukBWzJDF7nMSk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9497c5b-129b-4b60-9510-5e13b30212a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M1CxCwBBexsr9FzynUguxg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 10 · 2026-05-19T09:23:03.103Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TnzcAocxNoLn5VavmKdR2g`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.03403",
  "prompt": "Extract the full title, authors, abstract, and any other details visible on this arxiv page. What is this paper about? What method does it propose?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9497c5b-129b-4b60-9510-5e13b30212a4",
  "isSidechain": true,
  "agentId": "a4fe046b7e78cd743",
  "requestId": "req_011CbBgcVUoukBWzJDF7nMSk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3574002b-9557-45c6-a653-9de655c31a2e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M1CxCwBBexsr9FzynUguxg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9379,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1126
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 238,
          "cache_read_input_tokens": 9379,
          "cache_creation_input_tokens": 1126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1126,
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

_source line 11 · 2026-05-19T09:23:07.879Z_

<details><summary>↩ Tool result · `toolu_01MK3Log9WFZakVJq9UzyvKB`</summary>

```text
Web search results for query: "PROF PRM ORM iterative RL training arXiv 2509.03403"

Links: [{"title":"[2509.03403] Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training","url":"https://arxiv.org/abs/2509.03403"},{"title":"[2509.03403v1] Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training","url":"https://arxiv.org/abs/2509.03403v1"},{"title":"Paper page - Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training","url":"https://huggingface.co/papers/2509.03403"},{"title":"PROF: Process Consistency Filter BEYOND CORRECTNESS: HARMONIZING PROCESS AND","url":"https://arxiv.org/pdf/2509.03403"},{"title":"Adversarial reinforcement learning for procedural content generation and improved generalization","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11883746"},{"title":"Adversarial reinforcement learning for procedural content generation and improved generalization","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12157063"}]

Based on the search results, here's what I found about arXiv paper 2509.03403:

**Title:** Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training

**Key Contribution:** The paper introduces PRocess cOnsistency Filter (PROF), an effective data process curation method that harmonizes noisy, fine-grained process rewards with accurate, coarse-grained outcome rewards.

**Problem Addressed:** Outcome Reward Models (ORMs) are too coarse-grained to distinguish flawed reasoning within correct answers or valid reasoning within incorrect answers, while Process Reward Models (PRMs) offer fine-grained guidance for intermediate steps but frequently suffer from inaccuracies and are susceptible to reward hacking.

**Approach:** Rather than naively blending PRM and ORM in the objective function, PROF leverages their complementary strengths through consistency-driven sample selection.

**Results:** Experiments demonstrate that the method consistently improves final accuracy over 4% compared to blending approaches, while also strengthening the quality of intermediate reasoning steps.

The paper was submitted on September 3, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "903421d1-8b5f-45dd-9125-adae0e06005c",
  "isSidechain": true,
  "promptId": "ae35a659-7407-4079-9c58-2bf4f6ffeb73",
  "agentId": "a4fe046b7e78cd743",
  "type": "user",
  "uuid": "f8d1cf62-cb5d-4236-b7ff-98a4695b8ed5",
  "sourceToolAssistantUUID": "903421d1-8b5f-45dd-9125-adae0e06005c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T09:23:08.953Z_

<details><summary>↩ Tool result · `toolu_01TnzcAocxNoLn5VavmKdR2g`</summary>

```text
# Paper Summary

## Title
"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"

## Authors
Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, and Anurag Beniwal

## Core Focus
This research addresses a fundamental limitation in reinforcement learning systems trained on reasoning tasks. While outcome-based rewards improve final answer accuracy, they fail to ensure high-quality reasoning because "flawed reasoning can still receive maximal reward when it accidentally reaches the correct outcome."

## Proposed Method
The authors introduce PROF (PRocess cOnsistency Filter), a data curation approach that combines two types of feedback:

- **Process Reward Models (PRMs)**: Provide step-by-step supervision
- **Outcome Reward Models (ORMs)**: Assess final answers

Rather than directly optimizing either reward type, PROF uses their consistency to select training samples. The method retains correct responses with strong reasoning support while filtering weak reasoning, even when answers are correct.

## Key Results
According to the abstract, PROF "consistently improves both final-answer accuracy and intermediate reasoning quality over strong baselines, with less dependence on strong PRMs."

The work addresses the critical gap between achieving correct outputs and developing genuinely faithful reasoning processes in AI systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3574002b-9557-45c6-a653-9de655c31a2e",
  "isSidechain": true,
  "promptId": "ae35a659-7407-4079-9c58-2bf4f6ffeb73",
  "agentId": "a4fe046b7e78cd743",
  "type": "user",
  "uuid": "93050d01-c2b1-4b2a-8bfc-1616b4ebd463",
  "sourceToolAssistantUUID": "3574002b-9557-45c6-a653-9de655c31a2e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T09:23:09.508Z_

<details><summary>↩ Tool result · `toolu_01X9WQcnuYBwcpaVeEV5LQBM`</summary>

```text
Web search results for query: "PROF paper "process reward model" "outcome reward model" data curation reinforcement learning 2025"

Links: [{"title":"Paper page - Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training","url":"https://huggingface.co/papers/2509.03403"},{"title":"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training","url":"https://arxiv.org/html/2509.03403v1"},{"title":"[2509.03403] Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training","url":"https://arxiv.org/abs/2509.03403"},{"title":"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training | OpenReview","url":"https://openreview.net/forum?id=JKr77ZmZcM"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=process+reward"},{"title":"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training","url":"https://arxiv.org/pdf/2509.03403"},{"title":"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training - Paper Detail","url":"https://deeplearn.org/arxiv/634130/beyond-correctness:-harmonizing-process-and-outcome-rewards-through-rl-training"},{"title":"Process-supervised Reward Models (PRMs)","url":"https://www.emergentmind.com/topics/process-supervised-reward-models-prm"},{"title":"GitHub - bobxwu/learning-from-rewards-llm-papers: A comrephensive collection of learning from rewards in the post-training and test-time scaling of LLMs, with a focus on both reward models and learning strategies across training, inference, and post-inference stages. · GitHub","url":"https://github.com/bobxwu/learning-from-rewards-llm-papers"}]

Based on the search results, here's what I found about the PROF paper:

## PROF: Process Consistency Filter

PROF (PRocess cOnsistency Filter) is a data process curation method that harmonizes noisy, fine-grained process rewards with accurate, coarse-grained outcome rewards.

### The Problem It Addresses

Outcome Reward Models (ORMs) are too coarse-grained to distinguish flawed reasoning within correct answers or valid reasoning within incorrect answers, introducing noisy and misleading gradients that hinder progress in reasoning process quality. Meanwhile, Process Reward Models (PRMs) offer fine-grained guidance for intermediate steps but frequently suffer from inaccuracies and are susceptible to reward hacking.

### The Approach

Rather than naively blending PRM and ORM in the objective function, PROF leverages their complementary strengths through consistency-driven sample selection, retaining correct responses with higher averaged process values and incorrect responses with lower averaged process values, while maintaining positive/negative training sample balance.

### Results

The method consistently improves final accuracy over 4% compared to blending approaches, while also strengthening the quality of intermediate reasoning steps.

The paper was released in September 2025 (arXiv ID: 2509.03403), and the code and training recipes are available on GitHub at https://github.com/Chenluye99/PROF.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9497c5b-129b-4b60-9510-5e13b30212a4",
  "isSidechain": true,
  "promptId": "ae35a659-7407-4079-9c58-2bf4f6ffeb73",
  "agentId": "a4fe046b7e78cd743",
  "type": "user",
  "uuid": "a34514f6-1ed9-4644-bcb1-6f9f20d12926",
  "sourceToolAssistantUUID": "f9497c5b-129b-4b60-9510-5e13b30212a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-19T09:23:12.132Z_

Good, I've confirmed the paper exists and have the basics. Now let me fetch the full paper content from the HTML version and the PDF for maximum detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a34514f6-1ed9-4644-bcb1-6f9f20d12926",
  "isSidechain": true,
  "agentId": "a4fe046b7e78cd743",
  "requestId": "req_011CbBgdHbTxpMA8FLuqKjX3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "475aeb4b-4ed3-45bb-8e6f-b43fcc2ce0be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018EejxZNdcunjgGC668a6hz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 342,
      "cache_creation_input_tokens": 1702,
      "cache_read_input_tokens": 10505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1702,
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

_source line 15 · 2026-05-19T09:23:16.326Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Q6pr1qPwSXYjrvVSioP3P1`</summary>

```json
{
  "url": "https://arxiv.org/html/2509.03403v1",
  "prompt": "Extract the COMPLETE content of this paper in detail. I need:\n1. The full method section - exactly how PROF works step by step, including the consistency filter mechanism\n2. How PRM and ORM are used together - what is the filtering/selection criterion?\n3. What does \"consistency-driven sample selection\" mean concretely? What samples are kept vs discarded?\n4. The algorithm or pseudocode if available\n5. All experimental details: benchmarks, baselines, models used\n6. Key results tables and numbers\n7. Ablation studies\n8. Limitations discussed\n9. Any discussion of agreement vs disagreement between verifiers\nPlease be as detailed and complete as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "475aeb4b-4ed3-45bb-8e6f-b43fcc2ce0be",
  "isSidechain": true,
  "agentId": "a4fe046b7e78cd743",
  "requestId": "req_011CbBgdHbTxpMA8FLuqKjX3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "79a065d6-e9bd-4037-8dd0-bdee603bb073",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018EejxZNdcunjgGC668a6hz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 342,
      "cache_creation_input_tokens": 1702,
      "cache_read_input_tokens": 10505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1702,
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

_source line 16 · 2026-05-19T09:23:17.603Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UdVwyzEz7qPZWjAbDRhXtA`</summary>

```json
{
  "url": "https://openreview.net/forum?id=JKr77ZmZcM",
  "prompt": "Extract all reviews, scores, and discussion about this paper. What did reviewers say about strengths, weaknesses, and limitations? What scores did it receive?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79a065d6-e9bd-4037-8dd0-bdee603bb073",
  "isSidechain": true,
  "agentId": "a4fe046b7e78cd743",
  "requestId": "req_011CbBgdHbTxpMA8FLuqKjX3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49847756-e9bb-4fa5-a8c3-fb60aed061bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018EejxZNdcunjgGC668a6hz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 342,
      "cache_creation_input_tokens": 1702,
      "cache_read_input_tokens": 10505,
      "output_tokens": 373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1702
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 342,
          "output_tokens": 373,
          "cache_read_input_tokens": 10505,
          "cache_creation_input_tokens": 1702,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1702,
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

_source line 17 · 2026-05-19T09:23:20.938Z_

<details><summary>↩ Tool result · `toolu_01UdVwyzEz7qPZWjAbDRhXtA`</summary>

```text
# Paper Review Summary: Not Available

Based on the provided web page content, I cannot extract reviews, scores, or discussion feedback about this paper. 

The page shows only the paper's metadata, including:
- Title and author information
- Submission status: "Withdrawn Submission"
- Abstract describing the research
- Keywords and primary area
- Links to supplementary materials

**What's missing:** The actual peer review section, reviewer comments, scores, and any discussion threads that would typically appear on an OpenReview page are not included in the content provided. To access this information, you would need to visit the full OpenReview page directly, as the page structure appears to indicate that "Revisions" and review content exist but weren't captured in the excerpt shared.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49847756-e9bb-4fa5-a8c3-fb60aed061bf",
  "isSidechain": true,
  "promptId": "ae35a659-7407-4079-9c58-2bf4f6ffeb73",
  "agentId": "a4fe046b7e78cd743",
  "type": "user",
  "uuid": "3845d173-a79e-4423-8077-8fcb7f4e044d",
  "sourceToolAssistantUUID": "49847756-e9bb-4fa5-a8c3-fb60aed061bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T09:23:45.974Z_

<details><summary>↩ Tool result · `toolu_01Q6pr1qPwSXYjrvVSioP3P1`</summary>

```text
# Complete Summary of PROF Paper

## 1. THE CORE METHOD: PROF (Process Consistency Filter)

### Core Problem
The paper addresses a fundamental issue: Outcome Reward Models (ORMs) only verify final answers, missing flawed reasoning that happens to reach correct answers. Process Reward Models (PRMs) provide step-level feedback but suffer from noise and reward hacking when naively blended into training.

### PROF Solution Architecture
Instead of directly blending PRM and ORM signals, PROF uses a **data curation strategy** that filters samples based on consistency between the two reward signals.

### Algorithm 1: Step-by-Step Process

**Input:** n rollouts per prompt, outcome rewards, process rewards from PRM

**Step 1 - Consistency Scoring:**
"Compute the trajectory-wise consistency score r^pro = [1/H_i ∑(r_i^h) - λI(...)]·r_o,i" where the consistency combines:
- Average of step-wise PRM rewards across trajectory
- Step length regularization (penalizing single-step or extremely long responses)
- Multiplication by outcome reward (±1)

**Step 2 - Group Separation:**
- Divide into correct group 𝒢+ (outcome reward = +1)
- Divide into incorrect group 𝒢- (outcome reward = -1)

**Step 3 - Balanced Filtering:**
Calculate removal counts to maintain balanced correct/incorrect ratio:
- k+ = min(n-m, ⌈(Δ+n-m)/2⌉)
- k- = n-m-k+

**Step 4 - Selective Ranking:**
- Rank correct group by consistency → **keep highest consistency scores**
- Rank incorrect group by consistency → **keep lowest consistency scores**
- This retains correct answers with sound reasoning AND incorrect answers with flawed steps

**Step 5 - Output:** m filtered trajectories for policy update

## 2. PRM-ORM INTEGRATION MECHANISM

### Filtering Criterion (Consistency Definition)
The consistency score fundamentally measures agreement between process and outcome signals:

**For correct responses:** Keep those where PRM gives high step-wise rewards (reasoning quality matches outcome correctness)

**For incorrect responses:** Keep those where PRM gives low step-wise rewards (flawed reasoning matches outcome incorrectness)

**Samples filtered out:**
- Correct answers with low average PRM scores (lucky guesses with flawed logic)
- Incorrect answers with high average PRM scores (sound reasoning interrupted by error)

### Why This Avoids Reward Hacking
Unlike direct PRM-ORM weighting (β=0.8 in Blend baseline), PROF:
- Uses PRM only for ranking/selection, not gradient computation
- Doesn't feed noisy PRM values into loss function
- Maintains outcome-based advantage calculations in GRPO
- Prevents models from gaming PRM by generating verbose, repetitive steps

## 3. CONCRETE SAMPLE SELECTION LOGIC

**Example from Table 1 (counterintuitive coin weighing problem):**
- Final answer: Correct (2 weighings)
- Reasoning: Fundamentally invalid (unbalanced scale comparison)
- Standard ORM: Would train on this
- PROF detection: Averages low PRM scores across steps → filters out

**Figure 1 right panel finding:** "30.1% responses among filtered-out correct responses are judged to possess flawed reasoning" (verified by Claude-3-Sonnet)

### Step Length Regularization
"λ = 10 and H_λ = 30" penalizes responses with:
- Single step (no reasoning shown)
- Extreme length (>30 steps, indicates gaming through verbosity)

## 4. EXPERIMENTAL SETUP

### Datasets & Models
- **Training prompts:** Numina-Math (860k problems)
- **Base models:** Qwen2.5-Math-1.5B and 7B-base
- **PRM:** Qwen2.5-Math-PRM-7B (Zhang et al. 2025)
- **Evaluation benchmarks:** Math500, Minerva Math, Olympiad Bench, AMC2023, AIME2024

### Training Configuration
- 1024 prompts per iteration
- n=4 rollouts (GRPO) vs n=8 (PROF-GRPO)
- m=4 policy update samples
- Learning rate: 1×10^-6 AdamW
- Temperature: 1.0 for generation, top-p=1.0
- 4096 token generation limit

### Evaluation Metric
Average@16: accuracy averaged over 16 sampled responses per prompt

## 5. KEY RESULTS

### Main Performance (Table 2)

**Qwen2.5-Math-1.5B-base:**
| Algorithm | Math500 | Minerva | Olympiad | AIME24 | AMC23 | Average |
|-----------|---------|---------|----------|--------|-------|---------|
| GRPO | 70.3 | 29.1 | 33.0 | 9.0 | 44.5 | 37.2 |
| Blend-PRM | 67.6 | 27.8 | 31.1 | 7.7 | 42.5 | 35.3 |
| **PROF-GRPO** | **73.2** | **30.0** | **36.1** | **9.6** | **49.1** | **39.6** |

**Qwen2.5-Math-7B-base:**
| Algorithm | Math500 | Minerva | Olympiad | AIME24 | AMC23 | Average |
|-----------|---------|---------|----------|--------|-------|---------|
| GRPO | 81.6 | 37.2 | 45.5 | 20.6 | 64.4 | 49.9 |
| Blend-PRM | 81.7 | 36.7 | 45.0 | 15.2 | 58.0 | 47.3 |
| **PROF-GRPO** | **83.1** | **39.0** | **47.8** | **17.5** | **70.9** | **51.7** |

**Summary:** PROF-GRPO achieves +2.4% (1.5B) and +1.8% (7B) improvement over GRPO, and ~4% improvement over Blend baseline.

### Robustness Analysis (Figure 3)

**Entropy collapse:** Blend-PRM exhibits rapid entropy loss collapse toward zero, indicating reward hacking. PROF maintains gradual, controlled entropy decrease.

**Response length control:** Blend-PRM shows uncontrolled length growth (model gaming verbosity). PROF maintains reasonable length growth trajectory.

**Convergence:** PROF achieves faster convergence and higher final accuracy than GRPO throughout training.

## 6. PROCESS QUALITY IMPROVEMENTS

### Monte Carlo Value Estimation (Figure 4 leftmost)
Measuring intermediate step quality by generating 8 continuations from each step:

| Benchmark | GRPO | PROF-GRPO | Improvement |
|-----------|------|-----------|-------------|
| Math500 | - | - | +9.2% |
| Minerva Math | - | - | +37.4% |
| Olympiad Bench | - | - | +15.9% |
| AMC2023 | - | - | +9.2% |
| AIME2024 | - | - | +11.1% |

**Finding:** "Much larger than the outcome accuracy gap," showing PROF significantly improves reasoning trajectory quality.

### Step-Level Metrics on Math500
- **Step count:** PROF produces more steps
- **PRM scores:** Higher averaged process rewards for PROF
- **LLM preference:** Claude-3-Sonnet strongly prefers PROF's "more complete and detailed steps"

## 7. ABLATION STUDIES

### 5.1: Importance of Group Separation
**Variants tested:**
- PROF w/o Separation: Both groups ranked together → 2%+ reward gap drift, performance loss
- Filter-Correct: PRM filter only correct group → competitive with PROF-Both
- Filter-Incorrect: PRM filter only incorrect → worse performance
- Filter-Random: No PRM filtering → minimal improvement

**Conclusion:** Separating groups is critical. Filtering correct samples via PRM consistency is most important.

### 5.2: Rollout Count (n=4,8,12,16 with m=4)
- Optimal at n=8
- Beyond n=12: performance degrades (trade-off between quality and reward hacking risk)
- Filter-Correct more robust at higher n values

### 5.3: Consistency Computation Methods (Table 3)
| Method | Average Accuracy |
|--------|------------------|
| **Mean** (proposed) | **51.7%** |
| Minimum | 50.9% |
| Sum | 50.6% |
| Ratio (no balancing) | 50.6% |

**Rationale:** Mean avoids single-step bias (minimum) and length bias (sum), provides stable consistency estimate.

### 5.4: Cross-Model Generalization (LLaMA-3.2-3B)
**With distribution shift (Qwen PRM on LLaMA base):**
- Filter-Correct: 25.4% (best)
- PROF-Both: 23.9% (marginal improvement)
- Blend-PRM: 15.7% (severe degradation)

**Finding:** Filter-Correct safer when PRM reliability questionable; PROF-Both preferred when PRM reliable.

## 8. LIMITATIONS DISCUSSED

1. **PRM dependency:** Method tied to pre-trained PRM quality. Not developing improved PRM but rather better integration strategy.

2. **Domain restriction:** Focuses on mathematical reasoning; extension to coding and web navigation marked as future work.

3. **Statistical significance:** AIME24 results cautioned due to small dataset (30 samples).

4. **Cross-model distribution shift:** Demonstrated with LLaMA experiment where PRM trained on Qwen distribution shows degradation.

## 9. VERIFIER AGREEMENT ANALYSIS

The paper validates PROF's filtering via human/LLM agreement:

**Consistency with LLM judgment:** Claude-3-Sonnet reviewed filtered-out correct responses. Result: "30.1% responses...judged to possess flawed reasoning," confirming PROF successfully identifies inconsistencies that pure outcome-based methods miss.

**Two types of agreement validated:**
1. Agreement between PRM and outcome (samples retained)
2. Agreement between PROF filtering and human reasoning assessment

No explicit discussion of disagreement rates, but the 30.1% "flawed reasoning" detection rate suggests PROF catches false positives that naive outcome filtering would preserve.

---

**Code availability:** "https://github.com/Chenluye99/PROF"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79a065d6-e9bd-4037-8dd0-bdee603bb073",
  "isSidechain": true,
  "promptId": "ae35a659-7407-4079-9c58-2bf4f6ffeb73",
  "agentId": "a4fe046b7e78cd743",
  "type": "user",
  "uuid": "a69972cf-bbf8-4a6d-93d6-c4c54c5868ed",
  "sourceToolAssistantUUID": "79a065d6-e9bd-4037-8dd0-bdee603bb073",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-19T09:23:49.740Z_

Excellent, I have very detailed information. Let me now get additional details - the OpenReview page shows it was "Withdrawn Submission" which is important. Let me also check the GitHub repo and get more context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a69972cf-bbf8-4a6d-93d6-c4c54c5868ed",
  "isSidechain": true,
  "agentId": "a4fe046b7e78cd743",
  "requestId": "req_011CbBgfyXrPgumA3KWX2dng",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70236b85-bc3c-42c0-ab03-fbeb71cbe9f6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StCtv6VFhS6e6KLKrQd5Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 193,
      "cache_creation_input_tokens": 3375,
      "cache_read_input_tokens": 12207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3375,
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

_source line 20 · 2026-05-19T09:23:50.809Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015TrTWNyTHgfJoQjooUSg8a`</summary>

```json
{
  "url": "https://github.com/Chenluye99/PROF",
  "prompt": "Extract all information about this repository: README contents, method description, code structure, any details about the implementation. What does the code show about how PROF works?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70236b85-bc3c-42c0-ab03-fbeb71cbe9f6",
  "isSidechain": true,
  "agentId": "a4fe046b7e78cd743",
  "requestId": "req_011CbBgfyXrPgumA3KWX2dng",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a46cb51-47e5-458b-b852-4bf621713895",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StCtv6VFhS6e6KLKrQd5Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 193,
      "cache_creation_input_tokens": 3375,
      "cache_read_input_tokens": 12207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3375,
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

_source line 21 · 2026-05-19T09:23:51.762Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012bJoRbn7jWoEj5RfB6ZXSA`</summary>

```json
{
  "query": "PROF \"process consistency filter\" \"beyond correctness\" limitations disagreement verifier 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a46cb51-47e5-458b-b852-4bf621713895",
  "isSidechain": true,
  "agentId": "a4fe046b7e78cd743",
  "requestId": "req_011CbBgfyXrPgumA3KWX2dng",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "657f7688-9e59-4703-87f5-4e2439d27279",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StCtv6VFhS6e6KLKrQd5Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 193,
      "cache_creation_input_tokens": 3375,
      "cache_read_input_tokens": 12207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3375,
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

_source line 22 · 2026-05-19T09:23:52.331Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ExYQWQ1hs5zgHSw1A9JPVd`</summary>

```json
{
  "url": "https://huggingface.co/papers/2509.03403",
  "prompt": "Extract all comments, discussions, and community feedback about this paper. Are there any critiques or analyses of the PROF method?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "657f7688-9e59-4703-87f5-4e2439d27279",
  "isSidechain": true,
  "agentId": "a4fe046b7e78cd743",
  "requestId": "req_011CbBgfyXrPgumA3KWX2dng",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ea0e0c9-92e0-460a-9a4c-fa2ef71d4da4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StCtv6VFhS6e6KLKrQd5Gc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 193,
      "cache_creation_input_tokens": 3375,
      "cache_read_input_tokens": 12207,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3375
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 193,
          "output_tokens": 309,
          "cache_read_input_tokens": 12207,
          "cache_creation_input_tokens": 3375,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3375,
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

_source line 23 · 2026-05-19T09:23:53.106Z_

<details><summary>↩ Tool result · `toolu_01ExYQWQ1hs5zgHSw1A9JPVd`</summary>

```text
&lt;persisted-output>
Output too large (62.9KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-gen-pipeline/593b0787-5a72-44d5-85e8-706f2a81fa97/tool-results/toolu_01ExYQWQ1hs5zgHSw1A9JPVd.txt

Preview (first 2KB):
Title: Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training

URL Source: https://arxiv.org/html/2509.03403

Published Time: Thu, 04 Sep 2025 00:49:10 GMT

Markdown Content:
Chenlu Ye 1,2 Zhou Yu 1 Ziji Zhang 1 Hao Chen 1 Narayanan Sadagopan 1\AND Jing Huang 1 Tong Zhang 2 Anurag Beniwal 1

1 Amazon 2 University of Illinois Urbana-Champaign

###### Abstract

Reinforcement learning with verifiable rewards (RLVR) has emerged to be a predominant paradigm for mathematical reasoning tasks, offering stable improvements in reasoning ability. However, Outcome Reward Models (ORMs) in RLVR are too coarse-grained to distinguish flawed reasoning within correct answers or valid reasoning within incorrect answers. This lack of granularity introduces noisy and misleading gradients significantly and hinders further progress in reasoning process quality. While Process Reward Models (PRMs) offer fine-grained guidance for intermediate steps, they frequently suffer from inaccuracies and are susceptible to reward hacking.

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ea0e0c9-92e0-460a-9a4c-fa2ef71d4da4",
  "isSidechain": true,
  "promptId": "ae35a659-7407-4079-9c58-2bf4f6ffeb73",
  "agentId": "a4fe046b7e78cd743",
  "type": "user",
  "uuid": "48a91a97-ac87-426a-8c5a-67394db96af8",
  "sourceToolAssistantUUID": "8ea0e0c9-92e0-460a-9a4c-fa2ef71d4da4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T09:23:57.018Z_

<details><summary>↩ Tool result · `toolu_015TrTWNyTHgfJoQjooUSg8a`</summary>

```text
# PROF Repository Analysis

## Overview
The PROF (PRocess cOnsistency Filter) repository presents a method for improving reasoning quality in large language model reinforcement learning by harmonizing process and outcome rewards.

## Core Problem
The repository addresses a fundamental tension in RL training:
- **Outcome Reward Models (ORMs)**: Only evaluate final correctness, missing flawed reasoning that happens to reach correct answers
- **Process Reward Models (PRMs)**: Evaluate intermediate steps but suffer from inaccuracy and reward hacking when directly integrated

Simply combining them creates unstable training signals.

## PROF Method Description
Rather than using PRM scores directly in training objectives, PROF functions as a "consistency filter" for data curation:

**For correct responses**: Remove those with lowest average PRM values across steps
**For incorrect responses**: Remove those with highest average PRM values across steps

The filtering maintains a balanced correct-to-incorrect ratio in training data.

## Key Results
Across multiple math benchmarks (Math500, Minerva Math, Olympiad Bench, AIME24, AMC23):
- PROF-GRPO achieves ~2% improvement over vanilla GRPO
- Outperforms naive PRM-ORM blending by ~4%
- Identifies and removes flawed reasoning with correct final answers
- Improves intermediate step quality and verification simplicity

## Implementation Notes
- Code and scripts were noted as "coming soon" at publication
- Tested on Qwen2.5-Math models (1.5B and 7B) and LLaMA-3.2-3B-instruct
- Includes ablation studies showing separate filtering of correct/incorrect samples outperforms joint filtering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a46cb51-47e5-458b-b852-4bf621713895",
  "isSidechain": true,
  "promptId": "ae35a659-7407-4079-9c58-2bf4f6ffeb73",
  "agentId": "a4fe046b7e78cd743",
  "type": "user",
  "uuid": "7c5f3c66-150e-4d8c-b083-ef0562c58cd6",
  "sourceToolAssistantUUID": "2a46cb51-47e5-458b-b852-4bf621713895",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T09:23:57.916Z_

<details><summary>↩ Tool result · `toolu_012bJoRbn7jWoEj5RfB6ZXSA`</summary>

```text
Web search results for query: "PROF "process consistency filter" "beyond correctness" limitations disagreement verifier 2025"

Links: [{"title":"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training","url":"https://arxiv.org/html/2509.03403"},{"title":"PROF: Process Consistency Filter BEYOND CORRECTNESS: HARMONIZING PROCESS AND","url":"https://arxiv.org/pdf/2509.03403"},{"title":"[2509.03403] Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training","url":"https://arxiv.org/abs/2509.03403"},{"title":"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training | OpenReview","url":"https://openreview.net/forum?id=JKr77ZmZcM"},{"title":"[2509.03403v1] Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training","url":"https://arxiv.org/abs/2509.03403v1"},{"title":"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training","url":"https://openreview.net/pdf?id=i6lySxAqe4"},{"title":"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training – Own Your AI","url":"https://www.ownyourai.com/beyond-correctness-harmonizing-process-and-outcome-rewards-through-rl-training/"},{"title":"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training - Paper Detail","url":"https://deeplearn.org/arxiv/634130/beyond-correctness:-harmonizing-process-and-outcome-rewards-through-rl-training"},{"title":"Paper page - Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training","url":"https://huggingface.co/papers/2509.03403"}]

Based on the search results, here's what I found about PROF (Process Consistency Filter):

## Overview

PROF (PRocess cOnsistency Filter) is an effective data process curation method that harmonizes noisy, fine-grained process rewards with accurate, coarse-grained outcome rewards.

## Problem It Addresses

Outcome Reward Models (ORMs) in reinforcement learning for verifiable rewards are too coarse-grained to distinguish flawed reasoning within correct answers or valid reasoning within incorrect answers, introducing noisy and misleading gradients that hinder progress in reasoning process quality. Additionally, Process Reward Models (PRMs) frequently suffer from inaccuracies and are susceptible to reward hacking.

## Key Limitations and Disagreement Issues

Process Reward Models often suffer from misspecification and distribution shift due to the limitation of offline training data, and in boundary cases where the policy encounters difficult problems and produces rarely seen responses, PRMs often fail to judge them correctly. The model can develop shortcuts that RL algorithms exploit due to inherent human disagreement and finite training data.

## How PROF Works

Rather than naively blending PRM and ORM in the objective function, PROF leverages their complementary strengths through consistency-driven sample selection, retaining correct responses with higher averaged process values and incorrect responses with lower averaged process values, while maintaining positive/negative training sample balance.

## Results

The method improves final accuracy by over 4% compared to blending approaches, and strengthens the quality of intermediate reasoning steps.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "657f7688-9e59-4703-87f5-4e2439d27279",
  "isSidechain": true,
  "promptId": "ae35a659-7407-4079-9c58-2bf4f6ffeb73",
  "agentId": "a4fe046b7e78cd743",
  "type": "user",
  "uuid": "72870885-940d-4a2c-b3e0-afbed7851642",
  "sourceToolAssistantUUID": "657f7688-9e59-4703-87f5-4e2439d27279",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-19T09:24:00.763Z_

Let me read the full paper content that was saved, and also look for more details on the mathematical formulation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72870885-940d-4a2c-b3e0-afbed7851642",
  "isSidechain": true,
  "agentId": "a4fe046b7e78cd743",
  "requestId": "req_011CbBggrbApQu5z6vhJXXwY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f06966e-39bb-42c9-92d2-2874eb5d200f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nvjzmm9haCCyZmTQQpDTB3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 439,
      "cache_creation_input_tokens": 1872,
      "cache_read_input_tokens": 15582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1872,
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

_source line 27 · 2026-05-19T09:24:01.406Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NCLXgBjf2k83MbjoqcwrZt`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-gen-pipeline/593b0787-5a72-44d5-85e8-706f2a81fa97/tool-results/toolu_01ExYQWQ1hs5zgHSw1A9JPVd.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f06966e-39bb-42c9-92d2-2874eb5d200f",
  "isSidechain": true,
  "agentId": "a4fe046b7e78cd743",
  "requestId": "req_011CbBggrbApQu5z6vhJXXwY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b51c24b-bbcd-44b9-a016-93a001bb67ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nvjzmm9haCCyZmTQQpDTB3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 439,
      "cache_creation_input_tokens": 1872,
      "cache_read_input_tokens": 15582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1872,
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

_source line 28 · 2026-05-19T09:24:01.930Z_

<details><summary>↩ Tool result · `toolu_01NCLXgBjf2k83MbjoqcwrZt`</summary>

```text
1	Title: Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training
2	
3	URL Source: https://arxiv.org/html/2509.03403
4	
5	Published Time: Thu, 04 Sep 2025 00:49:10 GMT
6	
7	Markdown Content:
8	Chenlu Ye 1,2 Zhou Yu 1 Ziji Zhang 1 Hao Chen 1 Narayanan Sadagopan 1\AND Jing Huang 1 Tong Zhang 2 Anurag Beniwal 1
9	
10	1 Amazon 2 University of Illinois Urbana-Champaign
11	
12	###### Abstract
13	
14	Reinforcement learning with verifiable rewards (RLVR) has emerged to be a predominant paradigm for mathematical reasoning tasks, offering stable improvements in reasoning ability. However, Outcome Reward Models (ORMs) in RLVR are too coarse-grained to distinguish flawed reasoning within correct answers or valid reasoning within incorrect answers. This lack of granularity introduces noisy and misleading gradients significantly and hinders further progress in reasoning process quality. While Process Reward Models (PRMs) offer fine-grained guidance for intermediate steps, they frequently suffer from inaccuracies and are susceptible to reward hacking.
15	
16	To resolve this dilemma, we introduce PRocess cOnsistency Filter (PROF), an effective data process curation method that harmonizes noisy, fine-grained process rewards with accurate, coarse-grained outcome rewards. Rather than naively blending PRM and ORM in the objective function (Zou et al., [2025](https://arxiv.org/html/2509.03403v1#bib.bib45)), PROF leverages their complementary strengths through consistency-driven sample selection. Our approach retains correct responses with higher averaged process values and incorrect responses with lower averaged process values, while maintaining positive/negative training sample balance. Extensive experiments demonstrate that our method not only consistently improves the final accuracy over 4%4\% compared to the blending approaches, but also strengthens the quality of intermediate reasoning steps. Codes and training recipes are available at [https://github.com/Chenluye99/PROF](https://github.com/Chenluye99/PROF).
17	
18	1 Introduction
19	--------------
20	
21	Verifiable rewards have spurred the widest attention recently because they can reliably improve the performance on reasoning tasks with easily verifiable outcomes, such as mathematical and coding problems (Cobbe et al., [2021](https://arxiv.org/html/2509.03403v1#bib.bib4); Jaech et al., [2024](https://arxiv.org/html/2509.03403v1#bib.bib12); Shao et al., [2024](https://arxiv.org/html/2509.03403v1#bib.bib23); Xiong et al., [2025b](https://arxiv.org/html/2509.03403v1#bib.bib30)). However, since the verifiers can only verify the outcome results, the rewards are too sparse and coarse to measure and supervise the reasoning quality in intermediate steps. For instance, if a correct answer contains flawed logic, Outcome Reward Models (ORMs) cannot distinguish it from a completely correct response. We present a classic example from the training data in Table [1](https://arxiv.org/html/2509.03403v1#S1.T1 "Table 1 ‣ 1 Introduction ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"), which has fundamentally invalid reasoning but happens to obtain the correct answer. Incorporating such flawed examples into the training process introduces unreliable gradients, leading to significant instability and misguided learning. Moreover, the quality and interpretability of the Chain of Thought (CoT) are crucial for a model’s practical reasoning ability, not just the accuracy of the final answer (Zhu et al., [2025](https://arxiv.org/html/2509.03403v1#bib.bib44); Lyu et al., [2023](https://arxiv.org/html/2509.03403v1#bib.bib20); Yeo et al., [2024](https://arxiv.org/html/2509.03403v1#bib.bib34)).
22	
23	This limitation of ORMs can be addressed by using LLM-as-a-judge or Monte-Carlo (MC) estimation to provide step-wise judgments or values (Wang et al., [2023](https://arxiv.org/html/2509.03403v1#bib.bib26); Zheng et al., [2024](https://arxiv.org/html/2509.03403v1#bib.bib42)). However, the cost of inferring LLM step-wise judgments or MC estimation at each iteration during online training is so high. Hence, it is inefficient and expensive to infer the step-wise scores or values for online training. Alternatively, an efficient solution is to use the pre-trained Process Reward Models (PRMs) (Lightman et al., [2023](https://arxiv.org/html/2509.03403v1#bib.bib17); Zhang et al., [2025](https://arxiv.org/html/2509.03403v1#bib.bib40)), but these models often suffer from misspecification and distribution shift due to the limitation of offline training data. Especially in boundary cases where the policy encounters difficult problems and produces rarely seen responses, PRMs often fail to judge them correctly, thus leading to severe reward hacking (Michaud et al., [2020](https://arxiv.org/html/2509.03403v1#bib.bib21); Tien et al., [2022](https://arxiv.org/html/2509.03403v1#bib.bib25)). Even if some works (Zha et al., [2025](https://arxiv.org/html/2509.03403v1#bib.bib38); Cui et al., [2025](https://arxiv.org/html/2509.03403v1#bib.bib5)) attempt to co-train the policy and PRMs online, they can only train in implicit ways such as using implicit generative reward or aligning process rewards with outcomes.
24	
25	Table 1: An Example of Reaching a Correct Result Through Flawed Reasoning
26	
27	Although numerous works have made enormous efforts to train PRMs offline or online, the problem of effectively coordinating PRMs with outcome-verifiable rewards remains largely underexplored. Existing approaches typically combine process and outcome rewards in a simple weighted manner (Zha et al., [2025](https://arxiv.org/html/2509.03403v1#bib.bib38); Cui et al., [2025](https://arxiv.org/html/2509.03403v1#bib.bib5); Zou et al., [2025](https://arxiv.org/html/2509.03403v1#bib.bib45)), which is vulnerable for reward hacking due to the noises and misspecification in PRMs. Therefore, in this paper, instead of developing another PRM, we focus on how to robustly integrate a pre-trained PRM into the online training process, i.e.,
28	
29	H ow to harmonize the accurate but coarse-grained ORMs with fine-grained but noisy Process Reward Models (PRMs) in Reinforcement Learning (RL)?
30	
31	In this work, instead of fine-tuning another PRM, we answer this question with a PRocess cOnsistency Filtering (PROF) framework, a data curation strategy based on process-outcome consistency. PROF oversamples more responses at training time, and then, ranks and filters the responses by the consistency between their PRMs and ORMs. Specifically, it removes samples where the process and outcome signals conflict—such as correct responses derived from flawed reasoning, or incorrect responses that contain sound reasoning steps. By filtering out these inconsistent samples, PROF eliminates conflicting and noisy gradients. Furthermore, observing that correct and incorrect responses have different consistency distributions, we rank each group separately to maintain a balanced training ratio. PROF is a modular framework that can be combined with RL algorithms like Group Relative Policy Optimization (GRPO) for online training.
32	
33	![Image 1: Refer to caption](https://arxiv.org/html/2509.03403v1/fig/PROF_alg.jpeg)
34	
35	![Image 2: Refer to caption](https://arxiv.org/html/2509.03403v1/fig/filtered_out_correct_response_pie.png)
36	
37	Figure 1: Left: Visualization of PROF Algorithm [1](https://arxiv.org/html/2509.03403v1#alg1 "Algorithm 1 ‣ 3.1 Preliminaries ‣ 3 Method ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"), where the length of each rectangle represents values of process rewards averaged over steps for each rollout. After generating n n rollouts and process rewards, PROF ranks the correct and incorrect group separately according to PRM-ORM consistency, so for the correct group, the longer items are kept; for the incorrect group, the shorter items are kept. The number to remove is to balance correct and incorrect ratio. Right: Fraction of flawed-reasoning responses judged by LLM among the filtered-out correct responses.
38	
39	We conduct extensive experiments to validate the improvement of PROF-GRPO on both outcome accuracy and process reasoning quality at diverse math reasoning benchmarks using both Qwen (Yang et al., [2024](https://arxiv.org/html/2509.03403v1#bib.bib33)) and LLaMA (Dubey et al., [2024](https://arxiv.org/html/2509.03403v1#bib.bib8)) models. To summarize, we highlight our key contributions as follows:
40	
41	*   •We propose PRocess cOnsistency Filtering (PROF) to robustly integrate noisy Process Reward Models (PRMs) with Outcome Reward Models (ORMs). Compared to the GRPO-type algorithms that only leveraged outcome rewards, our implementation PROF-GRPO can effectively distinguish the inconsistent trajectories, such as correct answers with flawed reasoning steps or incorrect answers with mostly valid steps. Moreover, unlike prior approaches that simply blend PRMs and PRMs, our method only rely on PRMs to rank and filter rather than directly involving them into gradients. This separation essentially avoids reward hacking and entropy collapse, thus achieving stable performance gains throughout training. 
42	*   •We conduct extensive studies to demonstrate that PROF-GRPO not only increases the final outcome accuracy but also shapes the intermediate reasoning steps and improves the process reasoning quality. Various metrics such as Monte-Carlo estimation, LLM-as-a judge are used to validate that our method enable models to segment reasoning trajectories into detailed and easy-to-verify steps. 
43	*   •We conduct a series of ablation studies to illustrate the importance of separating the correct and incorrect responses during the filtration. Meanwhile, we investigate various ways of calculating the consistency and filtering, and ablate on LLaMA base models for generalization. 
44	
45	2 Related Work
46	--------------
47	
48	#### Sample Filtering in Reinforcement Learning for LLM.
49	
50	A key challenge in applying reinforcement learning to LLM applications is the imperfection of reward signals. These signals often stem from a learned reward model, such as Reinforcement Learning from Human Feedback (RLHF), or are sparse, delivered only at the end of a trajectory (e.g. RLVR). In Reinforcement Learning from Human Feedback (RLHF), the reward model is trained on human-annotated pairwise comparisons, typically using a Bradley-Terry model (Bradley & Terry, [1952](https://arxiv.org/html/2509.03403v1#bib.bib2)). Due to inherent human disagreement and finite training data, the model develops shortcuts that RL algorithms can exploit (Lin et al., [2023](https://arxiv.org/html/2509.03403v1#bib.bib18); Eisenstein et al., [2023](https://arxiv.org/html/2509.03403v1#bib.bib9)) to chase for a fake high reward. Consequently, these rewards may not fully align with the underlying intended goals, leading to reward hacking.
51	
52	Data filtering, a data curation technique, has proven effective in mitigating this issue across various LLM applications with RL. A prominent line of work proposes filtering training pairs based on the reward gap, i.e., the difference in predicted rewards for the chosen and rejected responses (Yuan et al., [2024](https://arxiv.org/html/2509.03403v1#bib.bib37); Dong et al., [2024](https://arxiv.org/html/2509.03403v1#bib.bib7); Xiong et al., [2024a](https://arxiv.org/html/2509.03403v1#bib.bib27); Zhang et al., [2024](https://arxiv.org/html/2509.03403v1#bib.bib39)). The high-level intuition is that a larger reward gap indicates higher model confidence, making these pairs less noisy and more reliable for training when the reward model is well-calibrated. Moreover, Kim et al. ([2024](https://arxiv.org/html/2509.03403v1#bib.bib15)); Yu et al. ([2025a](https://arxiv.org/html/2509.03403v1#bib.bib35)) further rank and filter the samples by combining their rewards and responses length during the preference learning process.
53	
54	Similarly, in reasoning tasks employing RL with verifier feedback (RLVR), where rewards are sparse and only provided for the final outcome, filtering is also proven to be helpful. For instance, the simple rejection sampling fine-tuning (Dong et al., [2023](https://arxiv.org/html/2509.03403v1#bib.bib6); Chen et al., [2025](https://arxiv.org/html/2509.03403v1#bib.bib3)) which discards all incorrect trajectories, serves as a powerful baseline, often approaching the performance of more complex algorithms like GRPO (Dong et al., [2023](https://arxiv.org/html/2509.03403v1#bib.bib6); Chen et al., [2025](https://arxiv.org/html/2509.03403v1#bib.bib3); Xiong et al., [2025a](https://arxiv.org/html/2509.03403v1#bib.bib29)). Other methods like (Yang et al., [2024](https://arxiv.org/html/2509.03403v1#bib.bib33)) filters the prompts by difficulty using metrics like pass@k prior to the RL training. Yu et al. ([2025b](https://arxiv.org/html/2509.03403v1#bib.bib36)) removes prompts that yield zero gradients during training and dynamically re-generates samples. This technique is known as dynamic sampling and has been rather widely accepted. Xiong et al. ([2025a](https://arxiv.org/html/2509.03403v1#bib.bib29)) demonstrates that prompts where all generated responses are incorrect can significantly hurt the performance of the vanilla Reinforce algorithm. They propose an online data filtering strategy based on the correctness reward, showing that a modified Reinforce with filtering (Reinforce-rej) can match or exceed GRPO’s performance. Their results suggest that the advantage of GRPO compared to Reinforce is likely due to the implicit data filtering mechanism from the reward shaping. Finally, Xu et al. ([2025](https://arxiv.org/html/2509.03403v1#bib.bib32)) proposes to over-sample and keep a subset such that the variance of the rewards in the subset is maximized, which implies that they try to balance the ratio of correct and incorrect responses for reasoning tasks.
55	
56	In contrast to these methods, which primarily rely on coarse, outcome-based metrics (e.g., final answer correctness, trajectory-level rewards), our approach introduces a more fine-grained filtering mechanism. We leverage process-supervised reward models (PRMs) (Lightman et al., [2023](https://arxiv.org/html/2509.03403v1#bib.bib17)) to evaluate and filter based on the quality of intermediate reasoning steps, and their consistency with ORMs.
57	
58	#### Process-Supervised Reward Models for Fine-Grained Feedback.
59	
60	The RLHF focuses on the trajectory-level comparison under the Bradley-Terry model. For reasoning-related task, Yang et al. ([2024](https://arxiv.org/html/2509.03403v1#bib.bib33)) uses the correctness of the final answer to construct the preference pairs and trains Bradley-Terry reward models for mathematical reasoning. A more widely used approach, termed Outcome Reward Models (ORMs) trains a classifier to predict whether the final answer is correct or not based on the reasoning history. However, Lightman et al. ([2023](https://arxiv.org/html/2509.03403v1#bib.bib17)) have shown that Process-Supervised Reward Models (PRMs), which evaluate each intermediate step of a reasoning chain, significantly outperform ORMs, especially for data selection tasks like best-of-n sampling (Lightman et al., [2023](https://arxiv.org/html/2509.03403v1#bib.bib17)). But their approach requires human annotators to label each intermediate steps of the reasoning. Wang et al. ([2023](https://arxiv.org/html/2509.03403v1#bib.bib26)) proposes to use Monte-Carlo estimation of the Q value to automatically decide the label. After this, a long line of works proposes to improve the PRMs by generative reward modeling, advanced training technique like RL, and refined engineering practices (Xiong et al., [2024b](https://arxiv.org/html/2509.03403v1#bib.bib28); Zhang et al., [2025](https://arxiv.org/html/2509.03403v1#bib.bib40); Khalifa et al., [2025](https://arxiv.org/html/2509.03403v1#bib.bib14); Zhao et al., [2025](https://arxiv.org/html/2509.03403v1#bib.bib41); Xiong et al., [2025c](https://arxiv.org/html/2509.03403v1#bib.bib31)). Our work does not focus on improving PRMs but uses the PRMs to supervise the intermediate steps of CoT trajectories for data filtering. We mainly use the Qwen2.5-Math-PRM-7B from Zhang et al. ([2025](https://arxiv.org/html/2509.03403v1#bib.bib40)) as it is trained on the distribution of Qwen model and achieves superior performance on ProcessBench (Zheng et al., [2024](https://arxiv.org/html/2509.03403v1#bib.bib42)).
61	
62	3 Method
63	--------
64	
65	### 3.1 Preliminaries
66	
67	An LLM is a policy distribution such that given a prompt x x, it provides the density π​(a|x)\pi(a|x) of generating each response a a. For mathematical reasoning tasks with a binary verifiable reward, there exists a verifier mapping prompt-response pairs (x,a)(x,a) to a scalar reward r o​(x,a)∈{−1,1}r_{o}(x,a)\in\{-1,1\}. For each prompt, we can generate a group of responses and their corresponding responses with the verifier {(a i,r o,i)}i=1 G\{(a_{i},r_{o,i})\}_{i=1}^{G}.
68	
69	Algorithm 1 Process Consistency Filter (PROF)
70	
71	1:Input: Number of rollouts
72	
73	n n
74	, policy update size
75	
76	m m
77	, rollout
78	
79	{a 1,…,a n}\{a_{1},\ldots,a_{n}\}
80	, outcome rewards
81	
82	{r o,1,…,r o,n}\{r_{o,1},\ldots,r_{o,n}\}
83	, step number regularization parameter
84	
85	λ,H λ>0\lambda,H_{\lambda}>0
86	.
87	
88	2: Obtain process rewards for each rollout
89	
90	a i a_{i}
91	with
92	
93	H i H_{i}
94	steps:
95	
96	(r i 1,…,r i H i)(r^{1}_{i},\ldots,r^{H_{i}}_{i})
97	and compute the trajectory-wise consistency score
98	
99	r i pro=[1 H i​∑h=1 H i r i h−λ​I​(H i=1​or​H i≥H λ)]⋅r o,i.r^{\mathrm{pro}}_{i}=\Big{[}\frac{1}{H_{i}}\sum_{h=1}^{H_{i}}r^{h}_{i}-\lambda I(H_{i}=1\text{~or~}H_{i}\geq H_{\lambda})\Big{]}\cdot r_{o,i}.(1)
100	
101	3: Divide rollouts into correct group
102	
103	𝒢+={a 1+,…,a n++}\mathcal{G}_{+}=\{a^{+}_{1},\ldots,a^{+}_{n_{+}}\}
104	with
105	
106	r o,i=1 r_{o,i}=1
107	and incorrect group
108	
109	𝒢−={a 1−,…,a n−−}\mathcal{G}_{-}=\{a^{-}_{1},\ldots,a^{-}_{n_{-}}\}
110	with
111	
112	r o,i=−1 r_{o,i}=-1
113	, where
114	
115	n++n−=n n_{+}+n_{-}=n
116	.
117	
118	4: Compute the number to remove
119	
120	k+∈[n+],k−∈[n−]k_{+}\in[n_{+}],k_{-}\in[n_{-}]
121	in each group:
122	
123	k+=min⁡(n−m,⌈(Δ+n−m)/2⌉),k−=n−m−k+,k_{+}=\min(n-m,\lceil(\Delta+n-m)/2\rceil),~k_{-}=n-m-k_{+},(2)
124	
125	where
126	
127	Δ=n+−n−\Delta=n_{+}-n_{-}
128	.
129	
130	5: Rank
131	
132	𝒢+\mathcal{G}_{+}
133	and
134	
135	𝒢−\mathcal{G}_{-}
136	by
137	
138	r pro r^{\mathrm{pro}}
139	separately, and keep the samples
140	
141	𝒦+={a i+|rank​(a i+)≥n+−k+},𝒦−={a i−|rank​(a i−)≥n−−k−}.\mathcal{K}^{+}=\{a^{+}_{i}|\mathrm{rank}(a^{+}_{i})\geq n_{+}-k_{+}\},~\mathcal{K}^{-}=\{a^{-}_{i}|\mathrm{rank}(a^{-}_{i})\geq n_{-}-k_{-}\}.
142	
143	6:Output: The kept trajectories
144	
145	𝒦+∪𝒦−\mathcal{K}^{+}\cup\mathcal{K}^{-}
146	with final kept size
147	
148	m m
149	.
150	
151	#### GRPO.
152	
153	Group Relative Policy Optimization (GRPO) (Shao et al., [2024](https://arxiv.org/html/2509.03403v1#bib.bib23)) is a policy gradient algorithm that simplifies the Proximal Policy Optimization (PPO) (Schulman et al., [2017](https://arxiv.org/html/2509.03403v1#bib.bib22)) by only computing the advantage based on the outcome rewards in a group. Instead of maintaining and updating another value network, GRPO computes the advantage by standardizing the outcome rewards within a group:
154	
155	A i=r​(x,a i)−mean​({r​(x,a j)}j=1 n)std​({r​(x,a j)}j=1 n)+δ,i=1,…,n,A_{i}=\frac{r(x,a_{i})-\text{mean}\left(\{r(x,a_{j})\}_{j=1}^{n}\right)}{\text{std}\left(\{r(x,a_{j})\}_{j=1}^{n}\right)+\delta},\quad i=1,\ldots,n,
156	
157	where r​(x,a i)r(x,a_{i}) is the reward for a given response and δ>0\delta>0 is a small constant for numerical stability. This advantage is then incorporated into a clipped surrogate objective function, which is optimized to update the policy from π θ old\pi_{\theta_{\text{old}}} to π θ\pi_{\theta}:
158	
159	𝒥 GRPO​(θ)=𝔼 x∼𝒟​[1 n​∑i=1 n 1|a i|​∑t=1|a i|min⁡(π θ​(a i,<t|x)π θ old​(a i,<t|x)​A i,clip​(π θ​(a i,<t|x)π θ old​(a i,<t|x),1−ϵ,1+ϵ)​A i)],\displaystyle\mathcal{J}_{\text{GRPO}}(\theta)=\mathbb{E}_{x\sim\mathcal{D}}\left[\frac{1}{n}\sum_{i=1}^{n}\frac{1}{|a_{i}|}\sum_{t=1}^{|a_{i}|}\min\left(\frac{\pi_{\theta}(a_{i,<t}|x)}{\pi_{\theta_{\text{old}}}(a_{i,<t}|x)}A_{i},\text{clip}\left(\frac{\pi_{\theta}(a_{i,<t}|x)}{\pi_{\theta_{\text{old}}}(a_{i,<t}|x)},1-\epsilon,1+\epsilon\right)A_{i}\right)\right],
160	
161	where a t a_{t} denotes the t t-th token of response a a and a<t a_{<t} denotes (a 1,…,a t−1)(a_{1},\ldots,a_{t-1}).
162	
163	Although this approach stabilizes the online policy optimization and is efficient, the sparse reward signal limits further improvement on the intermediate reasoning steps.
164	
165	#### Process Reward Model (PRM).
166	
167	For a response a a containing CoT reasoning, it can be decomposed into multiple reasoning steps a=(a 1,…,a H)a=(a^{1},\ldots,a^{H}). We follow previous works (Zheng et al., [2024](https://arxiv.org/html/2509.03403v1#bib.bib42); Zhang et al., [2025](https://arxiv.org/html/2509.03403v1#bib.bib40); Zou et al., [2025](https://arxiv.org/html/2509.03403v1#bib.bib45)) to use a newline as a sign for a new step. For each step a h a^{h}, the PRM r h r^{h} maps it, the previous steps and the prompt (x,a≤h)(x,a^{\leq h}) to a scalar r h​(x,a≤h)r^{h}(x,a^{\leq h}), where we use the short-hand notation a≤h=(a 1,…,a h)a^{\leq h}=(a^{1},\ldots,a^{h}).
168	
169	### 3.2 PROF: Process Consistency Filter Framework
170	
171	#### Algorithm.
172	
173	We propose our Process Consistency Filter (PROF) in Algorithm [1](https://arxiv.org/html/2509.03403v1#alg1 "Algorithm 1 ‣ 3.1 Preliminaries ‣ 3 Method ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training") to incorporate the consistency of PRMs and ORMs robustly after the rollout phase, and also present a visualization in Figure [1](https://arxiv.org/html/2509.03403v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"). First, we generate G G samples and access the outcome reward. Then, we call the PRM to generate step-wise rewards for each rollout and compute the trajectory-wise consistency score r pro r^{\mathrm{pro}} by taking the mean over the step-wise rewards and adding a step length regularization in equation[1](https://arxiv.org/html/2509.03403v1#S3.E1 "In 2 ‣ Algorithm 1 ‣ 3.1 Preliminaries ‣ 3 Method ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"), where λ\lambda is the regularization parameter and H λ H_{\lambda} is the threshold for the penalized step number. This regularization is to ensure that samples with no step segments or over-long steps are discarded in the correct group. The samples are divided into two subgroups: 𝒢+\mathcal{G}_{+} contains the correct samples with r o=1 r_{o}=1, and 𝒢−\mathcal{G}_{-} contains the incorrect samples with r o=−1 r_{o}=-1. Inspired by (Xu et al., [2025](https://arxiv.org/html/2509.03403v1#bib.bib32)), The numbers to discard in each subgroup k+,k−k_{+},k_{-} are calculated as equation[2](https://arxiv.org/html/2509.03403v1#S3.E2 "In 4 ‣ Algorithm 1 ‣ 3.1 Preliminaries ‣ 3 Method ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training") such that the outcome-reward variance of the final kept samples is maximized, which implies that the ratio of correct and incorrect responses should be balanced. After that, we use r pro r^{\mathrm{pro}} to rank and filter the correct group and randomly filter the incorrect group. Finally, we collect the kept m m trajectories and use them for policy update.
174	
175	#### Intuition of Consistency Filtration.
176	
177	To demonstrate that our algorithm can effectively differentiate the inconsistent trajectories, especially those correct answers with flawed reasoning steps, we conduct some understanding experiments. We prompt Qwen2.5-Math-7B-base (Yang et al., [2024](https://arxiv.org/html/2509.03403v1#bib.bib33)) to generate rollouts for 500 500 problems randomly selected from the training set (introduced in next section) and implement the filtration exactly as Algorithm [1](https://arxiv.org/html/2509.03403v1#alg1 "Algorithm 1 ‣ 3.1 Preliminaries ‣ 3 Method ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"). Then, the filtered-out correct responses are judged by Claude-3-7-sonnet from Anthropic to verify whether they contain flawed steps. We use the prompt in Zhang et al. ([2025](https://arxiv.org/html/2509.03403v1#bib.bib40)) and provide the details in Appendix [A](https://arxiv.org/html/2509.03403v1#A1 "Appendix A Additional Experimental Details and Results ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"). As shown in the right plot of Figure [1](https://arxiv.org/html/2509.03403v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"), 30.1%30.1\% responses among the filtered-out correct responses are judged to possess flawed reasoning. This indicates that our methods can efficiently distinguish a number of flawed responses and reach consensus with LLM. Furthermore, with human checking those filtered-out correct responses, there are many responses with invalid or even completely wrong reasoning steps but luckily reaching the correct answer. A typical example is presented in Table [1](https://arxiv.org/html/2509.03403v1#S1.T1 "Table 1 ‣ 1 Introduction ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"). However, flawed reasoning processes would be entirely missed by a standard ORM.
178	
179	4 Experiments
180	-------------
181	
182	### 4.1 Setup
183	
184	#### Dataset and Models.
185	
186	We focus on mathematical reasoning tasks in this work. For online training, we use the prompt set Numina-Math (Beeching et al., [2024](https://arxiv.org/html/2509.03403v1#bib.bib1)) containing nearly 860k math problems with ground-truth answers ranging from Chinese high school math exercises to US and international mathematics Olympiad competition problems. We choose Qwen2.5-Math-1.5B-base, Qwen2.5-Math-7B-base (Yang et al., [2024](https://arxiv.org/html/2509.03403v1#bib.bib33)) as the training base models. For the PRM, we use Qwen2.5-Math-PRM-7B (Zhang et al., [2025](https://arxiv.org/html/2509.03403v1#bib.bib40)) to generate process rewards.
187	
188	#### Implementation Details.
189	
190	The implementations are based on the verl framework (Sheng et al., [2025](https://arxiv.org/html/2509.03403v1#bib.bib24)), and we follow most of the parameter settings in verl. Detailedly, we apply the AdamW optimizer with learning rate 1×10−6 1\times 10^{-6}. We adopt the clip higher trick (Yu et al., [2025b](https://arxiv.org/html/2509.03403v1#bib.bib36)) that clips the sampling ratio π θ/π old\pi_{\theta}/\pi_{\text{old}} to an asymmetric range (1−ϵ low,1+ϵ high)(1-\epsilon_{\text{low}},1+\epsilon_{\text{high}}). Specifically, we set ϵ low=0.2,ϵ high=0.28\epsilon_{\text{low}}=0.2,\epsilon_{\text{high}}=0.28 for models started from Qwen2.5-Math-1.5B-base and maintain ϵ high=ϵ low=0.2\epsilon_{\text{high}}=\epsilon_{\text{low}}=0.2 for other cases. In each iteration, we sample 1024 1024 prompts, rollout n=4 n=4 responses per prompt for GRPO and n=8 n=8 responses for PROF-GRPO. Note that the policy update number for all algorithms is m=4 m=4. For the regularization of step numbers in Algorithm [1](https://arxiv.org/html/2509.03403v1#alg1 "Algorithm 1 ‣ 3.1 Preliminaries ‣ 3 Method ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"), we take λ=10\lambda=10 and H λ=30 H_{\lambda}=30. More details are provided in Appendix [A](https://arxiv.org/html/2509.03403v1#A1 "Appendix A Additional Experimental Details and Results ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training") and scripts are available in the GitHub repository.
191	
192	#### Evaluation.
193	
194	The models’ performance is evaluated on 5 benchmarks: Math500 (Hendrycks et al., [2021](https://arxiv.org/html/2509.03403v1#bib.bib11)), Minerva Math (Lewkowycz et al., [2022](https://arxiv.org/html/2509.03403v1#bib.bib16)), Olympiad Bench (He et al., [2024](https://arxiv.org/html/2509.03403v1#bib.bib10)), AMC2023 1 1 1 https://huggingface.co/datasets/math-ai/amc23 and AIME2024 2 2 2 https://huggingface.co/datasets/math-ai/aime24. We mainly use average@16 16 for evaluation, i.e., the accuracy is averaged over 16 16 responses per prompt under temperature 1.0 1.0. The models are allowed to generate 4096 4096 tokens.
195	
196	### 4.2 Main Results
197	
198	Model Algorithm Math500 Minerva Math Olympiad Bench AIME24 AMC23 Average
199	Qwen2.5-Math- 1.5B-base Base 39.9 11.4 19.1 3.5 23.6 19.5
200	GRPO 70.3 29.1 33.0 9.0 44.5 37.2
201	Blend 67.6 27.8 31.1 7.7 42.5 35.3
202	PROF-GRPO 73.2 30.0 36.1 9.6 49.1 39.6
203	Qwen2.5-Math- 7B-base Base 42.0 12.8 19.2 12.9 30.0 23.4
204	GRPO 81.6 37.2 45.5 20.6 64.4 49.9
205	Blend 81.7 36.7 45.0 15.2 58.0 47.3
206	PROF-GRPO 83.1 39.0 47.8 17.5 70.9 51.7
207	
208	Table 2: Performance of different algorithms across five benchmarks including Math500 (Hendrycks et al., [2021](https://arxiv.org/html/2509.03403v1#bib.bib11)), Minerva Math (Lewkowycz et al., [2022](https://arxiv.org/html/2509.03403v1#bib.bib16)), Olympiad Bench (He et al., [2024](https://arxiv.org/html/2509.03403v1#bib.bib10)), AMC2023 and AIME2024. We denote Blend-PRM-GRPO by Blend for short. We tune all the algorithms to their best performance and refer the readers to Appendix for the detailed parameter setup. The reported accuracy is average@16 under temperature 1.0 1.0.
209	
210	We summarize our main results in Table [2](https://arxiv.org/html/2509.03403v1#S4.T2 "Table 2 ‣ 4.2 Main Results ‣ 4 Experiments ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"), where Blend denotes a commonly used way that mixes the PRM with outcome rewards (Zha et al., [2025](https://arxiv.org/html/2509.03403v1#bib.bib38); Cui et al., [2025](https://arxiv.org/html/2509.03403v1#bib.bib5); Zou et al., [2025](https://arxiv.org/html/2509.03403v1#bib.bib45)). Following (Zou et al., [2025](https://arxiv.org/html/2509.03403v1#bib.bib45)), the PRMs are averaged over steps for each response, weighted by a parameter β\beta, and added to the outcome rewards. We use the parameter β=0.8\beta=0.8 according to Table 5 of (Zou et al., [2025](https://arxiv.org/html/2509.03403v1#bib.bib45)). Our main findings are as follows.
211	
212	#### PROF-GRPO Outperforms the Baselines.
213	
214	As shown in Table [2](https://arxiv.org/html/2509.03403v1#S4.T2 "Table 2 ‣ 4.2 Main Results ‣ 4 Experiments ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"), our proposed method, PROF-GRPO, consistently outperforms GRPO and Blend-PRM-GRPO over various benchmarks. Specifically, for models starting from Qwen2.5-Math-1.5B-base, PROF-GRPO achieves an average accuracy of 39.6%39.6\%, surpassing the standard GRPO baseline (37.2%37.2\%) and the Blend-PRM-GRPO method (35.3%35.3\%). A similar trend is observed with the Qwen2.5-Math-7B-base model, where PROF-GRPO achieves a 51.7%51.7\% average accuracy, a significant improvement over GRPO’s 49.9%49.9\% and Blend-PRM-GRPO’s 47.3%47.3\%. 3 3 3 Although PROF-GRPO underperformed relative to GRPO on AIME24 for Qwen2.5-Math-7B-base, this result should be interpreted with caution. Given the dataset’s small size of only 30 samples, the performance difference may not be statistically significant.
215	
216	The learning dynamics in Figure[2](https://arxiv.org/html/2509.03403v1#S4.F2 "Figure 2 ‣ PROF-GRPO Outperforms the Baselines. ‣ 4.2 Main Results ‣ 4 Experiments ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training") corroborate these findings, illustrating that PROF-GRPO steadily maintains a consistent performance advantage over both GRPO and Blend-PRM-GRPO throughout the training process. Notably, PROF-GRPO achieves faster convergence rate and higher final accuracy than GRPO.
217	
218	![Image 3: Refer to caption](https://arxiv.org/html/2509.03403v1/fig/Qwen2.5-Math-1.5B_data_temp1.0_comparison_main.png)
219	
220	![Image 4: Refer to caption](https://arxiv.org/html/2509.03403v1/fig/7B_model_comparison_temp1.0_main.png)
221	
222	Figure 2: The learning dynamics of PROF-GRPO initialized from Qwen2.5-Math-1.5B-base (left) and Qwen2.5-Math-7B-base (right). The y-axis is the average@16 16 accuracy and is further averaged on Math500, Minerva Math and Olympiad Bench. For comparison, we also plot the baseline GRPO and directly blending PRM with outcome rewards, denoted as Blend-PRM-GRPO.
223	
224	#### Filtration Method is Much More Robust than Blending.
225	
226	![Image 5: Refer to caption](https://arxiv.org/html/2509.03403v1/fig/actor_entropy_loss.png)
227	
228	![Image 6: Refer to caption](https://arxiv.org/html/2509.03403v1/fig/response_length_mean.png)
229	
230	Figure 3: Left: the entropy loss curves of GRPO, Blend-PRM-GRPO and PROF-GRPO; Right: the response length curves of GRPO, Blend-PRM-GRPO and PROF-GRPO, all of which are initialized from Qwen2.5-Math-7B-base.
231	
232	We plot the entropy loss and response length curves of GRPO, Blend-PRM-GRPO and PROF-GRPO in Figure [3](https://arxiv.org/html/2509.03403v1#S4.F3 "Figure 3 ‣ Filtration Method is Much More Robust than Blending. ‣ 4.2 Main Results ‣ 4 Experiments ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"). Combining it and Figure [2](https://arxiv.org/html/2509.03403v1#S4.F2 "Figure 2 ‣ PROF-GRPO Outperforms the Baselines. ‣ 4.2 Main Results ‣ 4 Experiments ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"), we observe that Blending-PRM-GRPO suffers from severe rewarding hacking. Figure [3](https://arxiv.org/html/2509.03403v1#S4.F3 "Figure 3 ‣ Filtration Method is Much More Robust than Blending. ‣ 4.2 Main Results ‣ 4 Experiments ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training") shows that its entropy collapse quickly towards zero. Simultaneously, its response length in the right figure uncontrollably increases, indicating that the model has learned to game the PRM by over-generating verbose responses and more repetitive steps to get a higher averaged process reward. Therefore, Blend-PRM-GRPO’s testing accuracy even falls below GRPO. In contrast, PROF-GRPO maintains gradual and slightly faster decrease in entropy loss and controllable response length growth. This illustrates that our filtration method effectively leverages the PRM signal while stay robust to reward hacking. We will carefully analyze and compare the quality of intermediate reasoning steps of our method and baselines.
233	
234	### 4.3 How PROF shapes Intermediate Reasoning Steps
235	
236	![Image 7: Refer to caption](https://arxiv.org/html/2509.03403v1/fig/mc_prm_bar.png)
237	
238	![Image 8: Refer to caption](https://arxiv.org/html/2509.03403v1/fig/step_number_bar.png)
239	
240	![Image 9: Refer to caption](https://arxiv.org/html/2509.03403v1/fig/prm_bar.png)
241	
242	![Image 10: Refer to caption](https://arxiv.org/html/2509.03403v1/fig/claude_pref_bar.png)
243	
244	Figure 4: Reasoning intermediate-steps performance of PROF-GRPO in comparison with GRPO. The most left plot is the Monte Carlo (MC) estimation scores across five benchmarks. The other three are on Math500 under metrics of number of steps (2nd left), the averaged process rewards generated by Qwen2.5-Math-PRM-7B (3rd left), and LLM’s preference between two modes’ responses (most right).
245	
246	#### Improved Step-wise Value.
247	
248	To evaluate the quality of intermediate steps, we adopt Monte Carlo (MC) estimation, a commonly used way to estimate the probability of getting to the correct final answer and estimate process values (Wang et al., [2023](https://arxiv.org/html/2509.03403v1#bib.bib26); Xiong et al., [2024a](https://arxiv.org/html/2509.03403v1#bib.bib27); Luo et al., [2024](https://arxiv.org/html/2509.03403v1#bib.bib19)). For this analysis, we select problem-response pairs from the test prompts where our method (PROF-GRPO) and GRPO both produced the correct final answer. Both models were initialized from Qwen2.5-Math-7B-base. To estimate the value of each reasoning step, we generate eight independent completions from that point using a temperature of 1.0, and the resulting empirical success rate serves as the MC value.
249	
250	Our primary finding is that PROF-GRPO achieves a significant improvement in step-wise values compared to GRPO. As shown in the leftmost plot of Figure [4](https://arxiv.org/html/2509.03403v1#S4.F4 "Figure 4 ‣ 4.3 How PROF shapes Intermediate Reasoning Steps ‣ 4 Experiments ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"), the average MC estimations across all five benchmarks are consistently higher for our model. The specific improvement gaps are 9.2%9.2\% on Math500, 37.4%37.4\% on Minerval Math, 15.9%15.9\% on Olympiad Bench, 9.2%9.2\% on AMC2023, and 11.1%11.1\% on AIME2024, which are much larger than the outcome accuracy gap in Table [2](https://arxiv.org/html/2509.03403v1#S4.T2 "Table 2 ‣ 4.2 Main Results ‣ 4 Experiments ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"). This finding validates that in addition to improve the outcome accuracy, more importantly, our PROF method substantially improves the quality and consistency of intermediate steps.
251	
252	#### Deeper Analysis on Math500.
253	
254	We conducted further comparisons on the Math500 benchmark using responses where both models were correct in figure [4](https://arxiv.org/html/2509.03403v1#S4.F4 "Figure 4 ‣ 4.3 How PROF shapes Intermediate Reasoning Steps ‣ 4 Experiments ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"). In the second left figure, PROF-GRPO’s responses have more reasoning steps. In the third left figure, the PRM used for training assigns higher rewards for PROF-GRPO’s responses. In the most right figure, we use Claude-3-7-sonnet from Anthropic to judge which one’s reasoning process has more complete and detailed steps, and PROF-GRPO’s responses are significantly preferred. The prompt for LLM-as-a-judge is presented in Table [A.2](https://arxiv.org/html/2509.03403v1#A1.SS2 "A.2 Prompt Template ‣ Appendix A Additional Experimental Details and Results ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"). Overall, the key takeaway is that our PROF method reshapes the model’s CoT process from complicated and skipping reasoning into detailed and easy-to-verify steps. This can be further validated by two examples in Figure [5](https://arxiv.org/html/2509.03403v1#S4.F5 "Figure 5 ‣ Deeper Analysis on Math500. ‣ 4.3 How PROF shapes Intermediate Reasoning Steps ‣ 4 Experiments ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training") and [8](https://arxiv.org/html/2509.03403v1#A3.F8 "Figure 8 ‣ Appendix C Additional Examples ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training").
255	
256	![Image 11: Refer to caption](https://arxiv.org/html/2509.03403v1/fig/PRM_example_minerval.jpeg)
257	
258	Figure 5: A Minerval-Math example to compare distinct intermediate reasoning patterns of PROF-GRPO, vanilla GRPO and Blend-PRM-GRPO. PROF-GRPO presents concrete and correct deduction steps. GRPO’s solution skips detailed deduction steps and there are flaws in the calculation precision and the final rounding. Blend-PRM-GRPO has long-winded steps and makes a big mistake in calculating the power.
259	
260	5 Ablations
261	-----------
262	
263	To understand the superior performance of PROF-GRPO, we conduct a series of ablation studies.
264	
265	### 5.1 Separation of Correct and Incorrect Group
266	
267	![Image 12: Refer to caption](https://arxiv.org/html/2509.03403v1/fig/Qwen2.5-Math-1.5B_data_temp1.0_comparison_+-.png)
268	
269	![Image 13: Refer to caption](https://arxiv.org/html/2509.03403v1/fig/7B_model_comparison_temp1.0_+-.png)
270	
271	![Image 14: Refer to caption](https://arxiv.org/html/2509.03403v1/fig/gap_after_before_filtering.png)
272	
273	![Image 15: Refer to caption](https://arxiv.org/html/2509.03403v1/fig/nroll_plot.png)
274	
275	Figure 6: First row: the averaged accuracy over three benchmarks Math500, Minerva Math and Olympiad Bench for PROF-GRPO (Filter both correct and incorrect with PRM consistency) and its variants initialized from wen2.5-Math-1.5B-base (left) and Qwen2.5-Math-7B-base (right). Lower left: the gap between the training rewards after and before the filtering for PROF-GRPO in comparison with not separating correct and incorrect groups (w/o separation). Lower right: the averaged accuracy across all five benchmarks over rollout sizes n=4,8,12,16 n=4,8,12,16 for filtering both correct and incorrect groups with PRM consistency (Both) and only the correct group with PRM consistency (Correct).
276	
277	To justify the necessity of handling correct and incorrect samples separately, we conduct an ablation experiment PROF-GRPO w/o separation, where the n n rollouts are ranked and filtered without separating correct and incorrect responses. To mitigate bias in PRM, each step’s PRM is subtracted by the averaged PRM of the batch. Even after centering, the lower left plot in Figure [6](https://arxiv.org/html/2509.03403v1#S5.F6 "Figure 6 ‣ 5.1 Separation of Correct and Incorrect Group ‣ 5 Ablations ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training") shows that PROF-GRPO w/o Separation has over 2%2\% gap between the training reward after and before the filtration. This indicates that a disproportionate number of negative samples are removed, thereby distorting the ratio of correct to incorrect samples. One explanation is that incorrect responses often contain several correct intermediate steps, thus increasing the averaged PRM over steps and leading to lower consistency. Consequently, incorrect responses exhibit lower consistency than correct ones, especially as the policy model improves over training. In contrast, PROF-GRPO successfully balances the bias by separating the correct and incorrect groups and maintains nearly the same reward before and after filtering.
278	
279	To further disentangle the contributions of filtering correct versus incorrect samples, we design the following variants of PROF:
280	
281	1.   (1)Filter-Correct: use PRM consistency to filter the correct group and randomly filter the incorrect group; 
282	2.   (2)Filter-Incorrect: use PRM consistency to filter the incorrect group and randomly filter the correct group; 
283	3.   (3)Filter-Random: only maximize the outcome reward variance and randomly filter both correct and incorrect samples, following Xu et al. ([2025](https://arxiv.org/html/2509.03403v1#bib.bib32)). 
284	
285	As shown in the first row of Figure [6](https://arxiv.org/html/2509.03403v1#S5.F6 "Figure 6 ‣ 5.1 Separation of Correct and Incorrect Group ‣ 5 Ablations ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"), Filter-Correct and PROF-GRPO (Filter-both) achieve comparably best performances among the variants across the 1.5B and 7B models. While Filter-both converges more efficiently because it leverages the consistency filtration for both correct and incorrect groups. Filter-incorrect is less efficient and has slightly poorer performance. In contrast, Filter-Random only performs slightly better than GRPO, and w/o Separation performs the worst.
286	
287	These findings lead to a clear conclusion: separating the correct and incorrect groups is essential to prevent the over-removal of valuable incorrect samples during training. While both Filter-both and Filter-Correct are top-performing strategies, with the former being more efficient, the trade-offs between them will be discussed in the following section. Furthermore, the comparable performance of Filter-both and Filter-Correct indicates that the process quality for correct samples is more crucial than the consistency for incorrect samples during the training process.
288	
289	### 5.2 Effect of Rollout Numbers
290	
291	We study the scale of rollout numbers n n with fixed policy-update number m=4 m=4 by varying n=4,8,12,16 n=4,8,12,16. The lower-right plot in Figure[6](https://arxiv.org/html/2509.03403v1#S5.F6 "Figure 6 ‣ 5.1 Separation of Correct and Incorrect Group ‣ 5 Ablations ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training") presents the test accuracy averaged over all five benchmarks for PROF-GRPO (Both) and Filter-Correct (Correct) started from Qwen2.5-Math-7B-base. We observe the performance first increases then decreases as n n increases, revealing a trade-off between enhancing process reasoning quality and avoiding reward hacking. Notably, Filter-Correct decreases later (after n=12 n=12) because it only leverages the influence of PRM only in the correct group, indicating that Filter-Correct is more robust when the PRM’s influence is higher, like when increasing the scale of ranking and filtering.
292	
293	### 5.3 Variants of Filtration Methods
294	
295	Algorithm Math500 Minerva Math Olympiad Bench AIME24 AMC23 Average
296	Mean 83.1 39.0 47.8 17.5 70.9 51.7
297	Minimum 82.9 38.3 46.7 20.8 65.9 50.9
298	Sum 82.4 38.1 47.4 17.7 67.5 50.6
299	Ratio 81.4 36.6 45.0 24.8 65.2 50.6
300	
301	Table 3: Performance of different filtration ways in PROF starting from Qwen2.5-Math-7B-base.
302	
303	In this subsection, we investigate the influence of different computation methods of consistency score r pro r^{\mathrm{pro}} in addition to the mean of PRMs over steps, where Mean denotes averaging over steps in Algorithm [1](https://arxiv.org/html/2509.03403v1#alg1 "Algorithm 1 ‣ 3.1 Preliminaries ‣ 3 Method ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"), Minimum and Sum denotes taking the minimum and sum summation over steps, Ratio denotes filtering while preserving the original positive–negative sample distribution, instead of balancing. As shown in Table [3](https://arxiv.org/html/2509.03403v1#S5.T3 "Table 3 ‣ 5.3 Variants of Filtration Methods ‣ 5 Ablations ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"), the performances of Minimum (50.9%50.9\%), Sum (50.6%50.6\%), and Ratio (50.6%50.6\%) are inferior to the mean. This suggests that the mean provides a more stable estimate of reasoning consistency: unlike the minimum, it is less sensitive to a single poorly scored step, and unlike the summation, it avoids bias towards longer trajectories. Additionally, balancing the correct-incorrect ratio can use data consistency to select the group with more sufficient samples without breaking their balance.
304	
305	### 5.4 Ablation Study on Base Model
306	
307	Algorithm Math500 Minerva Math Olympiad Bench AIME24 AMC23 Average
308	Base 30.0 8.8 6.1 2.3 10.6 11.6
309	GRPO 50.5 18.8 17.9 5.0 25.6 23.6
310	PROF-GRPO (Both)50.4 19.1 18.7 3.5 27.8 23.9
311	PROF-GRPO (Correct)52.4 19.5 19.8 6.7 28.6 25.4
312	PROF-GRPO (Incorrect)49.0 18.0 17.3 5.4 23.9 22.7
313	Blend-PRM-GRPO 37.2 13.1 9.9 1.0 17.2 15.7
314	
315	Table 4: The test accuracy of different methods initialized from LLaMA-3.2-3B-instruct that is average@16 under temperature 1.0 1.0 and further averaged across all the five benchmarks.
316	
317	To showcase the generalization of our algorithm, we conduct experiments on LLaMA-3.2-3B-instruct (Dubey et al., [2024](https://arxiv.org/html/2509.03403v1#bib.bib8)) that has weaker math-reasoning abilities and more distribution shift since Qwen2.5-Math-PRM-7B is trained on the distribution of Qwen’s family. As provided in Table [4](https://arxiv.org/html/2509.03403v1#S5.T4 "Table 4 ‣ 5.4 Ablation Study on Base Model ‣ 5 Ablations ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"), PROF-GRPO with PRM consistency filtering both correct and incorrect groups (Both) achieves 23.9%23.9\%, marginally outperforming the GRPO baseline (23.6%23.6\%), while only applying PRM consistency to filter the correct group (Correct) exhibits the strongest (25.4%25.4\%) performance. Conversely, applying the filter solely to the incorrect group (PROF-GRPO (Incorrect)) is counterproductive, causing accuracy to drop to 22.7%22.7\%. Blend-PRM-GRPO still scores the worst (15.7%15.7\%) among all the methods. These results suggest that our PROF methods can consistently outperform baselines across various base models.
318	
319	For the trade-off between the Both and Correct, we conclude that when the PRM is less reliable or prone to reward hacking (as in this cross-model scenario), the “Correct” method offers more robust improvements by safely constraining the PRM’s influence. However, when the PRM is highly reliable and training efficiency is a priority, the “Both” method is recommended.
320	
321	6 Conclusion and Future Work
322	----------------------------
323	
324	In this work, we introduce the Process Consistency Filter (PROF), a novel data curation technique that filters generated responses by the data PRM-ORM consistency, and maintains the balance of correct and incorrect ratios. We demonstrate its effectiveness and robustness in not only consistently improving the accuracy of obtaining correct final answers, but also shaping the policy model to generate more detailed and fine-grained segmented intermediate reasoning steps. Particularly, PROF is a general subsampling and filtration framework without reliance on specific PRMs or the RL algorithms. Thus, the use of Qwen2.5-Math-PRM-7B as the PRM in our experiments is not a limitation. Exploring the integration of PROF with more accurate or diverse PRMs remains an interesting direction for future work. Additionally, how to extend our method to other reasoning tasks, such as coding (Jimenez et al., [2023](https://arxiv.org/html/2509.03403v1#bib.bib13)) and web navigation (Zhou et al., [2023](https://arxiv.org/html/2509.03403v1#bib.bib43)) also deserves to be explored.
325	
326	Acknowledgment
327	--------------
328	
329	This work is partially supported by NSF grant No. 2416897 and ONR grant No. N000142512318.
330	
331	References
332	----------
333	
334	*   Beeching et al. (2024) Edward Beeching, Shengyi Costa Huang, Albert Jiang, Jia Li, Benjamin Lipkin, Zihan Qina, Kashif Rasul, Ziju Shen, Roman Soletskyi, and Lewis Tunstall. Numinamath 7b cot. [https://huggingface.co/AI-MO/NuminaMath-7B-CoT](https://huggingface.co/AI-MO/NuminaMath-7B-CoT), 2024. 
335	*   Bradley & Terry (1952) Ralph Allan Bradley and Milton E Terry. Rank analysis of incomplete block designs: I. the method of paired comparisons. _Biometrika_, 39(3/4):324–345, 1952. 
336	*   Chen et al. (2025) Huayu Chen, Kaiwen Zheng, Qinsheng Zhang, Ganqu Cui, Yin Cui, Haotian Ye, Tsung-Yi Lin, Ming-Yu Liu, Jun Zhu, and Haoxiang Wang. Bridging supervised learning and reinforcement learning in math reasoning. _arXiv preprint arXiv:2505.18116_, 2025. 
337	*   Cobbe et al. (2021) Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. Training verifiers to solve math word problems. _arXiv preprint arXiv:2110.14168_, 2021. 
338	*   Cui et al. (2025) Ganqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Wendi Li, Bingxiang He, Yuchen Fan, Tianyu Yu, Qixin Xu, Weize Chen, et al. Process reinforcement through implicit rewards. _arXiv preprint arXiv:2502.01456_, 2025. 
339	*   Dong et al. (2023) Hanze Dong, Wei Xiong, Deepanshu Goyal, Yihan Zhang, Winnie Chow, Rui Pan, Shizhe Diao, Jipeng Zhang, Kashun Shum, and Tong Zhang. Raft: Reward ranked finetuning for generative foundation model alignment. _arXiv preprint arXiv:2304.06767_, 2023. 
340	*   Dong et al. (2024) Hanze Dong, Wei Xiong, Bo Pang, Haoxiang Wang, Han Zhao, Yingbo Zhou, Nan Jiang, Doyen Sahoo, Caiming Xiong, and Tong Zhang. Rlhf workflow: From reward modeling to online rlhf. _arXiv preprint arXiv:2405.07863_, 2024. 
341	*   Dubey et al. (2024) Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al. The llama 3 herd of models. _arXiv e-prints_, pp. arXiv–2407, 2024. 
342	*   Eisenstein et al. (2023) Jacob Eisenstein, Chirag Nagpal, Alekh Agarwal, Ahmad Beirami, Alex D’Amour, DJ Dvijotham, Adam Fisch, Katherine Heller, Stephen Pfohl, Deepak Ramachandran, et al. Helping or herding? reward model ensembles mitigate but do not eliminate reward hacking. _arXiv preprint arXiv:2312.09244_, 2023. 
343	*   He et al. (2024) Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, et al. Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems. _arXiv preprint arXiv:2402.14008_, 2024. 
344	*   Hendrycks et al. (2021) Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. _arXiv preprint arXiv:2103.03874_, 2021. 
345	*   Jaech et al. (2024) Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, Aiden Low, Alec Helyar, Aleksander Madry, Alex Beutel, Alex Carney, et al. Openai o1 system card. _arXiv preprint arXiv:2412.16720_, 2024. 
346	*   Jimenez et al. (2023) Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan. Swe-bench: Can language models resolve real-world github issues? _arXiv preprint arXiv:2310.06770_, 2023. 
347	*   Khalifa et al. (2025) Muhammad Khalifa, Rishabh Agarwal, Lajanugen Logeswaran, Jaekyeom Kim, Hao Peng, Moontae Lee, Honglak Lee, and Lu Wang. Process reward models that think. _arXiv preprint arXiv:2504.16828_, 2025. 
348	*   Kim et al. (2024) Sunnie SY Kim, Q Vera Liao, Mihaela Vorvoreanu, Stephanie Ballard, and Jennifer Wortman Vaughan. " i’m not sure, but…": Examining the impact of large language models’ uncertainty expression on user reliance and trust. In _Proceedings of the 2024 ACM conference on fairness, accountability, and transparency_, pp. 822–835, 2024. 
349	*   Lewkowycz et al. (2022) Aitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay Ramasesh, Ambrose Slone, Cem Anil, Imanol Schlag, Theo Gutman-Solo, et al. Solving quantitative reasoning problems with language models. _Advances in neural information processing systems_, 35:3843–3857, 2022. 
350	*   Lightman et al. (2023) Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. In _The Twelfth International Conference on Learning Representations_, 2023. 
351	*   Lin et al. (2023) Yong Lin, Hangyu Lin, Wei Xiong, Shizhe Diao, Jianmeng Liu, Jipeng Zhang, Rui Pan, Haoxiang Wang, Wenbin Hu, Hanning Zhang, et al. Mitigating the alignment tax of rlhf. _arXiv preprint arXiv:2309.06256_, 2023. 
352	*   Luo et al. (2024) Liangchen Luo, Yinxiao Liu, Rosanne Liu, Samrat Phatale, Meiqi Guo, Harsh Lara, Yunxuan Li, Lei Shu, Yun Zhu, Lei Meng, Jiao Sun, and Abhinav Rastogi. Improve mathematical reasoning in language models by automated process supervision, 2024. URL [https://arxiv.org/abs/2406.06592](https://arxiv.org/abs/2406.06592). 
353	*   Lyu et al. (2023) Qing Lyu, Shreya Havaldar, Adam Stein, Li Zhang, Delip Rao, Eric Wong, Marianna Apidianaki, and Chris Callison-Burch. Faithful chain-of-thought reasoning. In _The 13th International Joint Conference on Natural Language Processing and the 3rd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (IJCNLP-AACL 2023)_, 2023. 
354	*   Michaud et al. (2020) Eric J Michaud, Adam Gleave, and Stuart Russell. Understanding learned reward functions. _arXiv preprint arXiv:2012.05862_, 2020. 
355	*   Schulman et al. (2017) John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. _arXiv preprint arXiv:1707.06347_, 2017. 
356	*   Shao et al. (2024) Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Yang Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. _arXiv preprint arXiv:2402.03300_, 2024. 
357	*   Sheng et al. (2025) Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng, Haibin Lin, and Chuan Wu. Hybridflow: A flexible and efficient rlhf framework. In _Proceedings of the Twentieth European Conference on Computer Systems_, pp. 1279–1297, 2025. 
358	*   Tien et al. (2022) Jeremy Tien, Jerry Zhi-Yang He, Zackory Erickson, Anca D Dragan, and Daniel S Brown. Causal confusion and reward misidentification in preference-based reward learning. _arXiv preprint arXiv:2204.06601_, 2022. 
359	*   Wang et al. (2023) Peiyi Wang, Lei Li, Zhihong Shao, RX Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang Sui. Math-shepherd: Verify and reinforce llms step-by-step without human annotations. _arXiv preprint arXiv:2312.08935_, 2023. 
360	*   Xiong et al. (2024a) Wei Xiong, Chengshuai Shi, Jiaming Shen, Aviv Rosenberg, Zhen Qin, Daniele Calandriello, Misha Khalman, Rishabh Joshi, Bilal Piot, Mohammad Saleh, et al. Building math agents with multi-turn iterative preference learning. _arXiv preprint arXiv:2409.02392_, 2024a. 
361	*   Xiong et al. (2024b) Wei Xiong, Hanning Zhang, Nan Jiang, and Tong Zhang. An implementation of generative prm, 2024b. 
362	*   Xiong et al. (2025a) Wei Xiong, Jiarui Yao, Yuhui Xu, Bo Pang, Lei Wang, Doyen Sahoo, Junnan Li, Nan Jiang, Tong Zhang, Caiming Xiong, et al. A minimalist approach to llm reasoning: from rejection sampling to reinforce. _arXiv preprint arXiv:2504.11343_, 2025a. 
363	*   Xiong et al. (2025b) Wei Xiong, Hanning Zhang, Chenlu Ye, Lichang Chen, Nan Jiang, and Tong Zhang. Self-rewarding correction for mathematical reasoning. _arXiv preprint arXiv:2502.19613_, 2025b. 
364	*   Xiong et al. (2025c) Wei Xiong, Wenting Zhao, Weizhe Yuan, Olga Golovneva, Tong Zhang, Jason Weston, and Sainbayar Sukhbaatar. Stepwiser: Stepwise generative judges for wiser reasoning, 2025c. URL [https://arxiv.org/abs/2508.19229](https://arxiv.org/abs/2508.19229). 
365	*   Xu et al. (2025) Yixuan Even Xu, Yash Savani, Fei Fang, and Zico Kolter. Not all rollouts are useful: Down-sampling rollouts in llm reinforcement learning. _arXiv preprint arXiv:2504.13818_, 2025. 
366	*   Yang et al. (2024) An Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, et al. Qwen2. 5-math technical report: Toward mathematical expert model via self-improvement. _arXiv preprint arXiv:2409.12122_, 2024. 
367	*   Yeo et al. (2024) Wei Jie Yeo, Ranjan Satapathy, Rick Siow Mong Goh, and Erik Cambria. How interpretable are reasoning explanations from prompting large language models? _arXiv preprint arXiv:2402.11863_, 2024. 
368	*   Yu et al. (2025a) Ping Yu, Weizhe Yuan, Olga Golovneva, Tianhao Wu, Sainbayar Sukhbaatar, Jason Weston, and Jing Xu. Rip: Better models by survival of the fittest prompts. _arXiv preprint arXiv:2501.18578_, 2025a. 
369	*   Yu et al. (2025b) Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Weinan Dai, Tiantian Fan, Gaohong Liu, Lingjun Liu, et al. Dapo: An open-source llm reinforcement learning system at scale. _arXiv preprint arXiv:2503.14476_, 2025b. 
370	*   Yuan et al. (2024) Weizhe Yuan, Richard Yuanzhe Pang, Kyunghyun Cho, Sainbayar Sukhbaatar, Jing Xu, and Jason Weston. Self-rewarding language models. _arXiv preprint arXiv:2401.10020_, 3, 2024. 
371	*   Zha et al. (2025) Kaiwen Zha, Zhengqi Gao, Maohao Shen, Zhang-Wei Hong, Duane S Boning, and Dina Katabi. Rl tango: Reinforcing generator and verifier together for language reasoning. _arXiv preprint arXiv:2505.15034_, 2025. 
372	*   Zhang et al. (2024) Chuheng Zhang, Wei Shen, Li Zhao, Xuyun Zhang, Lianyong Qi, Wanchun Dou, and Jiang Bian. Policy filtration in rlhf to fine-tune llm for code generation. 2024. 
373	*   Zhang et al. (2025) Zhenru Zhang, Chujie Zheng, Yangzhen Wu, Beichen Zhang, Runji Lin, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin. The lessons of developing process reward models in mathematical reasoning. _arXiv preprint arXiv:2501.07301_, 2025. 
374	*   Zhao et al. (2025) Jian Zhao, Runze Liu, Kaiyan Zhang, Zhimu Zhou, Junqi Gao, Dong Li, Jiafei Lyu, Zhouyi Qian, Biqing Qi, Xiu Li, and Bowen Zhou. Genprm: Scaling test-time compute of process reward models via generative reasoning, 2025. URL [https://arxiv.org/abs/2504.00891](https://arxiv.org/abs/2504.00891). 
375	*   Zheng et al. (2024) Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin. Processbench: Identifying process errors in mathematical reasoning. _arXiv preprint arXiv:2412.06559_, 2024. 
376	*   Zhou et al. (2023) Shuyan Zhou, Frank F Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, et al. Webarena: A realistic web environment for building autonomous agents. _arXiv preprint arXiv:2307.13854_, 2023. 
377	*   Zhu et al. (2025) Dawei Zhu, Xiyu Wei, Guangxiang Zhao, Wenhao Wu, Haosheng Zou, Junfeng Ran, Xun Wang, Lin Sun, Xiangzheng Zhang, and Sujian Li. Chain-of-thought matters: improving long-context language models with reasoning path supervision. _arXiv preprint arXiv:2502.20790_, 2025. 
378	*   Zou et al. (2025) Jiaru Zou, Ling Yang, Jingwen Gu, Jiahao Qiu, Ke Shen, Jingrui He, and Mengdi Wang. Reasonflux-prm: Trajectory-aware prms for long chain-of-thought reasoning in llms. _arXiv preprint arXiv:2506.18896_, 2025. 
379	
380	Appendix A Additional Experimental Details and Results
381	------------------------------------------------------
382	
383	### A.1 Main Experiments
384	
385	For the rollout stage, we use a temperature of 1.0 1.0 and a top-p value of 1.0 1.0. We set the KL loss coefficient to 0.001 0.001 and entropy loss coefficient to 0.001 0.001. All the models are trained with 8 8 H100 GPUs. We set the training mini-batch size as 256 256 and allow the models to generate 4096 4096 tokens per prompt.
386	
387	### A.2 Prompt Template
388	
389	We present the template used for LLM to compare step-level reasoning.
390	
391	Appendix B Addtional Experimental Results
392	-----------------------------------------
393	
394	In this section, we include additional ablation studies and evaluation results for a more comprehensive understanding of the PROF-GRPO framework. We conduct the following variants of PROF framework:
395	
396	1.   1.Ratio: remove correct and incorrect responses according to the original correct–incorrect ratio rather than enforcing a balanced ratio in PROF. 
397	2.   2.Filter-Nstep: Ranking and filtering out the samples with smaller number of steps instead of lower PRM-ORM consistency. 
398	
399	From Table [5](https://arxiv.org/html/2509.03403v1#A2.T5 "Table 5 ‣ Appendix B Addtional Experimental Results ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"), we find that Ratio scores 51.7%51.7\% on average and cannot compete with balancing the proportion (PROF-GRPO), which also corroborates the conclusion that maintaining a balanced correct-incorrect proportion is essential. Additionally, since we observe that PROF boosts the number of intermediate reasoning steps, to verify that PROF does not simply increase the step length, but more importantly, enhances the quality of reasoning steps, we simply use the step length as the filtering criterion for comparison. As shown in Figure [7](https://arxiv.org/html/2509.03403v1#A2.F7 "Figure 7 ‣ Appendix B Addtional Experimental Results ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training") and Table [5](https://arxiv.org/html/2509.03403v1#A2.T5 "Table 5 ‣ Appendix B Addtional Experimental Results ‣ Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"), Filter-Nstep manipulates the step length, which exhibits an unreasonable increase followed by a sudden drop, and its average accuracy is inferior.
400	
401	Algorithm Math500 Minerva Math Olympiad Bench AIME24 AMC23 Average
402	PROF-GRPO 83.1 39.0 47.8 17.5 70.9 51.7
403	Filter-Nstep 81.5 35.5 45.9 16.3 58.6 47.6
404	
405	Table 5: Performance of variants of filtering methods besides PROF-GRPO starting from Qwen2.5-Math-7B-base averaged on all five benchmarks, where Ratio denotes filtering while preserving the original correct/incorrect proportion, Filter-Nstep denotes ranking and filtering based on the number of step segments.
406	
407	![Image 16: Refer to caption](https://arxiv.org/html/2509.03403v1/fig/train_len_segs_mean.png)
408	
409	Figure 7: The number of reasoning steps during training time for PROF-GRPO and Filter-Nstep initialized from Qwen2.5-Math-7B-base.
410	
411	Appendix C Additional Examples
412	------------------------------
413	
414	![Image 17: Refer to caption](https://arxiv.org/html/2509.03403v1/fig/PRM_example_math500.jpeg)
415	
416	Figure 8: A Math500 example to compare distinct intermediate reasoning patterns of PROF-GRPO, vanilla GRPO and Blend-PRM-GRPO. PROF-GRPO presents concrete and correct deduction steps. PROF-GRPO’s solution shows how to find the divisors and summation in detail, and is easy to follow. GRPO skips all core reasoning. Blend-PRM-GRPO has inefficient and excessively tedious steps.
417	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b51c24b-bbcd-44b9-a016-93a001bb67ae",
  "isSidechain": true,
  "promptId": "ae35a659-7407-4079-9c58-2bf4f6ffeb73",
  "agentId": "a4fe046b7e78cd743",
  "type": "user",
  "uuid": "1d28ed4c-950c-4dce-9cd1-a441db3816f0",
  "sourceToolAssistantUUID": "7b51c24b-bbcd-44b9-a016-93a001bb67ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-19T09:24:06.476Z_

I now have the complete paper. Let me also check whether there are any related papers about disagreement-based data curation to help with the positioning analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d28ed4c-950c-4dce-9cd1-a441db3816f0",
  "isSidechain": true,
  "agentId": "a4fe046b7e78cd743",
  "requestId": "req_011CbBgh9qkT4QRTmgXPeqVy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f15e38d7-2f15-40d1-aacc-8bdc30195111",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCceHoLFPrdS9JDbkssxM1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23184,
      "cache_read_input_tokens": 17454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23184,
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

_source line 30 · 2026-05-19T09:24:07.982Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rzy2r5EiT7WNY47jYuNT5q`</summary>

```json
{
  "query": "multi-verifier disagreement synthetic data curation reasoning LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f15e38d7-2f15-40d1-aacc-8bdc30195111",
  "isSidechain": true,
  "agentId": "a4fe046b7e78cd743",
  "requestId": "req_011CbBgh9qkT4QRTmgXPeqVy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53020257-0a86-41a0-8afc-8da40da506fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCceHoLFPrdS9JDbkssxM1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23184,
      "cache_read_input_tokens": 17454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23184,
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

_source line 31 · 2026-05-19T09:24:08.256Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VXnF1hXrdzsDCsBxR19Vvs`</summary>

```json
{
  "query": "\"reward model ensemble\" disagreement signal data selection reinforcement learning LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53020257-0a86-41a0-8afc-8da40da506fb",
  "isSidechain": true,
  "agentId": "a4fe046b7e78cd743",
  "requestId": "req_011CbBgh9qkT4QRTmgXPeqVy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1780b9d5-f74a-4461-a907-cd88e62b4944",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCceHoLFPrdS9JDbkssxM1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23184,
      "cache_read_input_tokens": 17454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23184,
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

_source line 32 · 2026-05-19T09:24:14.963Z_

<details><summary>↩ Tool result · `toolu_01Rzy2r5EiT7WNY47jYuNT5q`</summary>

```text
Web search results for query: "multi-verifier disagreement synthetic data curation reasoning LLM 2025"

Links: [{"title":"Learning from Synthetic Data Improves Multi-hop Reasoning","url":"https://arxiv.org/pdf/2603.02091"},{"title":"ORCHESTRATING SYNTHETIC DATA WITH REASONING","url":"https://openreview.net/pdf?id=VOoeogZbMb"},{"title":"A Survey on Efficient Large Language Model Training","url":"https://aclanthology.org/2025.acl-long.1493.pdf"},{"title":"Rethinking Data Quality for LLM Reasoning","url":"https://aclanthology.org/2025.findings-emnlp.616.pdf"},{"title":"GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub","url":"https://github.com/pengr/LLM-Synthetic-Data"},{"title":"Source2Synth: Synthetic Data Generation and Curation Grounded in Real Data Sources","url":"https://arxiv.org/pdf/2409.08239"},{"title":"Verifying the Verifiers: Unveiling Pitfalls and Potentials in Fact Verifiers","url":"https://arxiv.org/pdf/2506.13342"}]

Based on the search results, here are the key findings related to your query about multi-verifier disagreement, synthetic data curation, and reasoning in LLMs from 2025:

## Synthetic Data for LLM Reasoning

Recent work investigates RL fine-tuning on rule-generated synthetic data for multi-hop reasoning tasks, finding that LLMs fine-tuned on synthetic data perform significantly better on real-world question-answering benchmarks despite the synthetic data containing only fictional knowledge. Synthetic data teaches LLMs to compose knowledge—a fundamental and generalizable reasoning skill.

## Data Curation Challenges

A fundamental challenge is that high-quality training data with verifiable answers is scarce and expensive to curate, and LLM verifiers are slow and inaccurate.

## Model Disagreement and Data Quality

One framework for assessing data quality for LLM reasoning uses model disagreement to assess data quality via "Distortion", indicating that verifier disagreement is being studied as a metric for evaluating synthetic data quality.

## Recent Approaches (2025)

Recent work on Source2Synth addresses synthetic data generation and curation grounded in real data sources, demonstrating improvements of 25.51% for tabular question answering on WikiSQL and 22.57% for multi-hop question answering on HotpotQA.

The research landscape in 2025 shows growing attention to synthetic data quality assessment using multiple verification signals, particularly for complex reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53020257-0a86-41a0-8afc-8da40da506fb",
  "isSidechain": true,
  "promptId": "ae35a659-7407-4079-9c58-2bf4f6ffeb73",
  "agentId": "a4fe046b7e78cd743",
  "type": "user",
  "uuid": "2d8e8f2c-1879-4748-be19-5d893e1289b2",
  "sourceToolAssistantUUID": "53020257-0a86-41a0-8afc-8da40da506fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T09:24:15.208Z_

<details><summary>↩ Tool result · `toolu_01VXnF1hXrdzsDCsBxR19Vvs`</summary>

```text
Web search results for query: ""reward model ensemble" disagreement signal data selection reinforcement learning LLM"

Links: [{"title":"Reward Model Ensembles","url":"https://www.emergentmind.com/topics/reward-model-ensembles"},{"title":"Reward Modelling in Modern AI","url":"https://www.emergentmind.com/topics/reward-modelling"},{"title":"Enhancing Large Language Model Reasoning with Reward Models: An Analytical Survey","url":"https://arxiv.org/pdf/2510.01925"},{"title":"Reward-Robust RLHF in LLMs","url":"https://arxiv.org/html/2409.15360v3"},{"title":"MiniRec: Data-Efficient Reinforcement Learning for LLM-based Recommendation","url":"https://arxiv.org/pdf/2602.04278"},{"title":"Reward Models - by Cameron R. Wolfe, Ph.D.","url":"https://cameronrwolfe.substack.com/p/reward-models"},{"title":"LLM-Based Reward Models","url":"https://www.emergentmind.com/topics/llm-based-reward-models"}]

I found relevant search results on reward model ensembles, disagreement signals, and data selection in reinforcement learning for LLMs. Here are the key findings:

## Reward Model Ensembles Overview

Reward model ensembles are techniques that aggregate multiple reward models to robustly generate reward signals, with ensembles capturing epistemic uncertainty based on disagreement in outputs, allowing for filtering and robustness.

## Disagreement Signals for Data Selection

Higher reward gap signals lower reliability, enabling filtering of unreliable or out-of-distribution evaluations. Probabilistic value heads output uncertainty estimates, and ensembles (URME) capture epistemic uncertainty based on disagreement in the outputs.

## Applications in LLM Alignment

Conservative ensemble objectives eliminate or drastically reduce overoptimization in both best-of-n sampling and PPO settings, with up to 70% performance improvement over single model optimization reported under label noise.

## Data Quality and Label Noise

Real-world preference datasets contain substantial label noise—20%–40% disagreements or flips—leading to reward misgeneralization, overfitting, or spurious correlations that degrade downstream policy quality.

## RL-Driven Data Selection

MiniRec evaluates sample learnability using key RL signals—rewards—pruning samples that are too easy or too difficult, and assesses representativeness by aligning sample gradients with the approximated ideal global RL optimization trajectory.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1780b9d5-f74a-4461-a907-cd88e62b4944",
  "isSidechain": true,
  "promptId": "ae35a659-7407-4079-9c58-2bf4f6ffeb73",
  "agentId": "a4fe046b7e78cd743",
  "type": "user",
  "uuid": "777b90bf-2708-4ad4-a207-0ccd896b9f57",
  "sourceToolAssistantUUID": "1780b9d5-f74a-4461-a907-cd88e62b4944",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-19T09:24:19.187Z_

Now let me also check the Eisenstein et al. 2023 paper that PROF cites, which is specifically about reward model ensembles and disagreement.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "777b90bf-2708-4ad4-a207-0ccd896b9f57",
  "isSidechain": true,
  "agentId": "a4fe046b7e78cd743",
  "requestId": "req_011CbBgi8WerEQqewYq7k9cB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0065df2e-4b82-4e91-bf73-58e8640a0c99",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVrAzNCn5aP1e4jSjiYFk4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1516,
      "cache_read_input_tokens": 40638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1516,
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

_source line 35 · 2026-05-19T09:24:19.771Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GLTQ3p73KZA1qNk28mLHTh`</summary>

```json
{
  "query": "Eisenstein 2023 \"helping or herding\" reward model ensembles mitigate reward hacking disagreement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0065df2e-4b82-4e91-bf73-58e8640a0c99",
  "isSidechain": true,
  "agentId": "a4fe046b7e78cd743",
  "requestId": "req_011CbBgi8WerEQqewYq7k9cB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "600373e9-eaab-494d-8984-327953632c2b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVrAzNCn5aP1e4jSjiYFk4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1516,
      "cache_read_input_tokens": 40638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1516,
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

_source line 36 · 2026-05-19T09:24:26.645Z_

<details><summary>↩ Tool result · `toolu_01GLTQ3p73KZA1qNk28mLHTh`</summary>

```text
Web search results for query: "Eisenstein 2023 "helping or herding" reward model ensembles mitigate reward hacking disagreement"

Links: [{"title":"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking - Consensus","url":"https://consensus.app/papers/details/f74cb495d447504eaf62a11e74dfa5f5/"},{"title":"[2312.09244] Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking","url":"https://arxiv.org/abs/2312.09244"},{"title":"[PDF] Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking | Semantic Scholar","url":"https://www.semanticscholar.org/paper/b4afc7b4a6836054c1b4568ce9d49993afbb0461"},{"title":"[2312.09244] Helping or Herding? \\scalerel*\\vstretch1.25X Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking","url":"https://ar5iv.labs.arxiv.org/html/2312.09244"},{"title":"Adversarial Training of Reward Models","url":"https://arxiv.org/html/2504.06141v2"},{"title":"GitHub - google-deepmind/reward-ensembles","url":"https://github.com/google-deepmind/reward-ensembles"},{"title":"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking","url":"https://arxiv.org/html/2312.09244v3"},{"title":"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate   Reward Hacking","url":"https://arxiv.org/pdf/2312.09244"}]

I found the paper you were looking for! Here are the key details:

**Title:** "Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking"

**Authors:** Jacob Eisenstein, Chirag Nagpal, Alekh Agarwal, Ahmad Beirami, Alex D'Amour, DJ Dvijotham, Adam Fisch, Katherine Heller, Stephen Pfohl, Deepak Ramachandran, Peter Shaw, and Jonathan Berant

**Publication Date:** Published Dec 14, 2023

**Main Findings:**

The paper addresses reward hacking in language model alignment. Language models have an incentive to exploit errors in the reward model to achieve high estimated reward, a phenomenon often termed reward hacking. A natural mitigation is to train an ensemble of reward models, aggregating over model outputs to obtain a more robust reward estimate.

However, the research reveals important limitations: Reward models are underspecified - reward models that perform similarly in-distribution can yield very different rewards when used in alignment, due to distribution shift. This underspecification results in overoptimization, where alignment to one reward model does not improve reward as measured by another reward model trained on the same data.

The paper explores the application of reward ensembles to alignment at both training time (through reinforcement learning) and inference time (through reranking).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "600373e9-eaab-494d-8984-327953632c2b",
  "isSidechain": true,
  "promptId": "ae35a659-7407-4079-9c58-2bf4f6ffeb73",
  "agentId": "a4fe046b7e78cd743",
  "type": "user",
  "uuid": "6137a2fb-002d-4d8e-8c15-3f9f2b771e8b",
  "sourceToolAssistantUUID": "600373e9-eaab-494d-8984-327953632c2b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-19T09:25:36.559Z_

I now have comprehensive information to provide a thorough analysis. Here is the complete research report:

---

## PROF: Deep Research Report

### Paper Identity

**Title:** "Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"
**arXiv ID:** 2509.03403 (submitted September 4, 2025)
**Authors:** Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal (Amazon / UIUC)
**Code:** https://github.com/Chenluye99/PROF
**OpenReview status:** The submission to OpenReview (ID: JKr77ZmZcM) shows status **"Withdrawn Submission"**, which is a potentially useful detail for positioning.

---

### 1. The Exact Method: How PROF Uses PRM and ORM Together

PROF (PRocess cOnsistency Filter) is a **data curation / sample filtering** method inserted between the rollout phase and the policy update phase of GRPO training. It does NOT blend PRM and ORM scores into the reward function. Instead:

**Step-by-step algorithm:**

1. **Oversample:** Generate n=8 rollouts per prompt (vs. n=4 for vanilla GRPO), keeping only m=4 for the policy update.

2. **Compute consistency score** for each trajectory i:
   ```
   r_i^pro = [ (1/H_i) * sum(r_i^h for h=1..H_i) - lambda * I(H_i=1 or H_i >= H_lambda) ] * r_o,i
   ```
   Where:
   - `r_i^h` = PRM score for step h
   - `H_i` = number of steps in the trajectory
   - `r_o,i` = outcome reward (+1 or -1)
   - `lambda=10, H_lambda=30` = step-length regularization parameters
   - The multiplication by `r_o,i` is critical: for correct responses (r_o=+1), high avg PRM means high consistency; for incorrect responses (r_o=-1), the sign flips so low avg PRM means high consistency.

3. **Separate into groups:** G+ (correct, r_o=+1) and G- (incorrect, r_o=-1).

4. **Compute balanced removal counts** k+, k- to maintain a balanced correct/incorrect ratio (maximizing outcome reward variance).

5. **Rank and filter:**
   - In the correct group G+: **keep the top-ranked** by consistency (highest avg PRM scores) -> removes correct answers with poor reasoning.
   - In the incorrect group G-: **keep the top-ranked** by consistency (which, due to the sign flip from r_o=-1, means lowest avg PRM scores) -> removes incorrect answers with deceptively good-looking reasoning.

6. **Output:** m=4 filtered trajectories used for standard GRPO policy update with outcome-based advantages only. PRM values are NEVER fed into the gradient computation.

---

### 2. Does PROF Use Agreement/Consistency to FILTER Data?

**Yes, this is precisely what it does.** PROF is fundamentally an **agreement-based filter**. It retains samples where PRM and ORM **agree**:

- **Kept:** Correct answer + high PRM scores (agreement: good process, good outcome)
- **Kept:** Incorrect answer + low PRM scores (agreement: bad process, bad outcome)

It **discards** samples where PRM and ORM **disagree**:

- **Discarded:** Correct answer + low PRM scores (disagreement: bad process, lucky outcome -- "false positive")
- **Discarded:** Incorrect answer + high PRM scores (disagreement: good process, unlucky outcome -- "false negative")

The paper explicitly validates this with Claude-3-7-Sonnet: among filtered-out correct responses, **30.1% were confirmed to contain flawed reasoning**, showing the filter successfully catches false positives from ORM.

---

### 3. How PROF Handles the Interplay Between Different Verifier Types

PROF's key design insight is that PRM and ORM have **complementary failure modes**:

| Verifier | Strength | Weakness |
|----------|----------|----------|
| ORM | Accurate (verifiable ground truth) | Coarse-grained, cannot see reasoning quality |
| PRM | Fine-grained, step-level signal | Noisy, suffers from distribution shift, reward hacking |

PROF addresses this by:
- **Using ORM as the authority on correctness** (binary, reliable).
- **Using PRM only as a ranking signal within ORM-defined groups** (never in the loss function).
- This separation is critical: the "Blend" baseline that linearly combines PRM into the reward (r = r_o + beta * avg_PRM, with beta=0.8) suffers severe **entropy collapse** and **response length explosion** (reward hacking), performing WORSE than vanilla GRPO.
- PROF avoids reward hacking because PRM scores never enter the gradient computation; they only determine which samples are selected.

---

### 4. Benchmarks and Baselines

**Training data:** Numina-Math (~860k math problems)

**Base models:** Qwen2.5-Math-1.5B-base, Qwen2.5-Math-7B-base, LLaMA-3.2-3B-instruct (ablation)

**PRM:** Qwen2.5-Math-PRM-7B

**Evaluation benchmarks (Average@16):**
- Math500
- Minerva Math
- Olympiad Bench
- AMC2023
- AIME2024

**Baselines:**
- Base model (no RL)
- Vanilla GRPO (n=4 rollouts, outcome reward only)
- Blend-PRM-GRPO (linearly blends averaged PRM into outcome reward with beta=0.8)

---

### 5. Key Results

**Main performance (7B model):**
| Method | Average Accuracy |
|--------|-----------------|
| Base | 23.4% |
| GRPO | 49.9% |
| Blend-PRM-GRPO | 47.3% (WORSE than GRPO) |
| **PROF-GRPO** | **51.7%** (+1.8% over GRPO, +4.4% over Blend) |

**Main performance (1.5B model):**
| Method | Average Accuracy |
|--------|-----------------|
| GRPO | 37.2% |
| Blend-PRM-GRPO | 35.3% |
| **PROF-GRPO** | **39.6%** (+2.4% over GRPO) |

**Process quality improvement (Monte Carlo value estimation, 7B):**
- Improvements of 9.2% to 37.4% on intermediate step quality across benchmarks -- much larger than outcome accuracy gains.

**Ablation findings:**
- Separating groups is essential; without it, incorrect samples get disproportionately removed.
- Filter-Correct alone is nearly as good as filtering both groups.
- Optimal rollout count is n=8 (with m=4); performance degrades beyond n=12.
- Mean aggregation of PRM scores outperforms minimum, sum, or ratio-based methods.
- Cross-model (LLaMA with Qwen PRM): Filter-Correct is safer when PRM is less reliable.

---

### 6. Limitations

1. **PRM dependency:** Quality is tied to the pre-trained PRM. The authors do not develop improved PRMs.
2. **Domain restriction:** Only tested on mathematical reasoning. Extension to coding/web navigation is future work.
3. **Single PRM architecture:** Only uses Qwen2.5-Math-PRM-7B. No experiments with diverse or ensemble PRMs.
4. **Small test sets:** AIME2024 has only 30 samples; statistical significance is questionable.
5. **Withdrawn from peer review:** The paper was withdrawn from its OpenReview submission (venue unknown), which may indicate issues identified during review.
6. **Modest absolute gains:** The improvement over vanilla GRPO is ~2% in outcome accuracy. The larger story is process quality improvement.

---

### 7. Critical Analysis: PROF vs. Disagreement-Based Curation

This is the most important section for positioning your work. PROF and a disagreement-based approach represent **two sides of the same coin**:

**PROF uses AGREEMENT as a signal to KEEP data:**
- Agreement between PRM and ORM -> "clean" training signal -> keep for RL training.
- The goal: remove noisy gradients from inconsistent samples.

**Your proposed approach uses DISAGREEMENT as a signal (the inverse):**
- Disagreement between multiple verifiers -> identifies "interesting" or "hard" or "uncertain" samples.
- The key question is: what do you DO with the disagreement signal?

**Key differentiators for your positioning:**

1. **PROF uses exactly TWO verifiers (one PRM, one ORM) in a fixed hierarchy.** The ORM is treated as ground truth (it IS ground truth for math). PROF cannot work in domains without verifiable outcomes. A multi-verifier disagreement approach could work with arbitrary combinations of verifiers without requiring one to be a ground-truth oracle.

2. **PROF discards disagreement cases entirely.** It throws away the most "interesting" samples -- the ones where process and outcome conflict. Your work could argue that these disagreement cases contain the richest learning signal (e.g., for curriculum design, targeted improvement, or uncertainty-aware training).

3. **PROF is limited to the binary agree/disagree between process and outcome.** A multi-verifier framework could capture richer disagreement patterns across many verifiers (e.g., 3+ reward models, LLM-as-judge, formal verifiers, unit tests), enabling more nuanced data curation.

4. **PROF addresses reward hacking by excluding PRM from gradients.** A disagreement approach could use disagreement to detect and characterize reward hacking more directly (samples where one verifier is "fooled" but others are not).

5. **PROF's 30.1% flawed-reasoning detection rate** means it catches less than a third of the problematic samples among filtered correct responses. This leaves room for improvement that a multi-verifier disagreement approach might capture.

6. **PROF was withdrawn from peer review**, suggesting potential issues with the approach that reviewers identified.

**Positioning language suggestion:**
PROF demonstrates that PRM-ORM consistency is a useful signal for data curation in RL training. However, PROF treats PRM-ORM disagreement purely as noise to be discarded. Your work takes the complementary view: multi-verifier disagreement is an **informative signal** that identifies samples at the decision boundary where targeted training is most valuable. While PROF uses a fixed two-verifier hierarchy (PRM subordinate to ground-truth ORM), your approach generalizes to arbitrary verifier ensembles without requiring ground-truth outcomes, making it applicable beyond math to domains like code generation, open-ended reasoning, and scientific discovery.

Sources:
- [PROF Paper (arXiv)](https://arxiv.org/abs/2509.03403)
- [PROF Paper HTML](https://arxiv.org/html/2509.03403v1)
- [PROF on HuggingFace Papers](https://huggingface.co/papers/2509.03403)
- [PROF OpenReview (Withdrawn)](https://openreview.net/forum?id=JKr77ZmZcM)
- [PROF GitHub Repository](https://github.com/Chenluye99/PROF)
- [Eisenstein et al. 2023 - Reward Model Ensembles](https://arxiv.org/abs/2312.09244)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6137a2fb-002d-4d8e-8c15-3f9f2b771e8b",
  "isSidechain": true,
  "agentId": "a4fe046b7e78cd743",
  "requestId": "req_011CbBgiyRjkHUgwipAFLQPC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fee625cb-8685-4433-98bf-676adb89674e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TtmvzhJAhtxzEd59joLArP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 42154,
      "output_tokens": 2861,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 951
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2861,
          "cache_read_input_tokens": 42154,
          "cache_creation_input_tokens": 951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 951,
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
