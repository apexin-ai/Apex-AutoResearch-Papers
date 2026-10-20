# Research conversation: Search for and read the paper "Training AI Co-Scientists" (arXiv:2512.23707, Dec 2025) which does rubric RL for scientif

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aba5f8b5a313742c2.jsonl`
- **Structured JSON:** [`8e1d97300d020a46f7fe.json`](../../sessions/8e/8e1d97300d020a46f7fe.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-28T03:25:11.429Z_

Search for and read the paper "Training AI Co-Scientists" (arXiv:2512.23707, Dec 2025) which does rubric RL for scientific research plan generation.

I need to understand:
1. What scientific reasoning tasks does it address?
2. How does it use rubrics for RL training?
3. Is it multimodal or text-only?
4. What are its key contributions and results?
5. How does it relate to non-verifiable scientific reasoning with rubric-based rewards?

Use WebSearch and WebFetch to find and read this paper. Search for "Training AI Co-Scientists arXiv 2512.23707 rubric reinforcement learning scientific" and related queries. Report your findings in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "agentId": "aba5f8b5a313742c2",
  "type": "user",
  "uuid": "e7f811ff-1c59-4e19-8be0-69031f0649a7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-28T03:25:11.431Z_

```json
{
  "parentUuid": "e7f811ff-1c59-4e19-8be0-69031f0649a7",
  "isSidechain": true,
  "agentId": "aba5f8b5a313742c2",
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
  "uuid": "1e172313-703a-4aa2-bdb2-b9b5ddf2216f",
  "timestamp": "2026-05-28T03:25:11.431Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-28T03:25:11.432Z_

```json
{
  "parentUuid": "1e172313-703a-4aa2-bdb2-b9b5ddf2216f",
  "isSidechain": true,
  "agentId": "aba5f8b5a313742c2",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c0e6c6cc-0f13-4e6b-9c7b-fa6405c4974f",
  "timestamp": "2026-05-28T03:25:11.432Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-28T03:25:14.361Z_



I'll search for this paper using WebSearch and WebFetch. Let me first load those tool schemas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0e6c6cc-0f13-4e6b-9c7b-fa6405c4974f",
  "isSidechain": true,
  "agentId": "aba5f8b5a313742c2",
  "requestId": "req_011CbUFcHd5GfKF7ANG2dxCt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99b80334-2537-4580-8071-31c19b96eda2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UiK2MoHdzuGvdPCicjYSNC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1474,
      "cache_read_input_tokens": 7411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1474,
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

_source line 5 · 2026-05-28T03:25:14.490Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EMfwBQfhsoTdcrQqi7NmJH`</summary>

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
  "parentUuid": "99b80334-2537-4580-8071-31c19b96eda2",
  "isSidechain": true,
  "agentId": "aba5f8b5a313742c2",
  "requestId": "req_011CbUFcHd5GfKF7ANG2dxCt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a56f71a-ef7f-417c-84ae-3006dea94369",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UiK2MoHdzuGvdPCicjYSNC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1474,
      "cache_read_input_tokens": 7411,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1474
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 103,
          "cache_read_input_tokens": 7411,
          "cache_creation_input_tokens": 1474,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1474,
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

_source line 6 · 2026-05-28T03:25:14.494Z_

<details><summary>↩ Tool result · `toolu_01EMfwBQfhsoTdcrQqi7NmJH`</summary>

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
  "parentUuid": "6a56f71a-ef7f-417c-84ae-3006dea94369",
  "isSidechain": true,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "agentId": "aba5f8b5a313742c2",
  "type": "user",
  "uuid": "de977d6e-a659-48dc-93db-73952414fcf8",
  "sourceToolAssistantUUID": "6a56f71a-ef7f-417c-84ae-3006dea94369",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T03:25:17.064Z_



Now let me search for this paper using multiple queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de977d6e-a659-48dc-93db-73952414fcf8",
  "isSidechain": true,
  "agentId": "aba5f8b5a313742c2",
  "requestId": "req_011CbUFcWv2nHhzNtSiuqKLr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cba749ad-6c52-43a0-ab72-4b1fd2d9d9d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0121GQpRQHtj5ACBKUGGpkwC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 8885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
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

_source line 8 · 2026-05-28T03:25:17.650Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KDnKTjW9XG1PN9udhY7ywJ`</summary>

```json
{
  "query": "Training AI Co-Scientists arXiv 2512.23707 rubric reinforcement learning scientific"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cba749ad-6c52-43a0-ab72-4b1fd2d9d9d9",
  "isSidechain": true,
  "agentId": "aba5f8b5a313742c2",
  "requestId": "req_011CbUFcWv2nHhzNtSiuqKLr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6373993-2be0-402b-9cec-a1fe022dc34c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0121GQpRQHtj5ACBKUGGpkwC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 8885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
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

_source line 9 · 2026-05-28T03:25:18.458Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mc3HXA3BYgJjxfvKxFmVig`</summary>

```json
{
  "query": "\"AI Co-Scientists\" rubric RL scientific research plan generation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6373993-2be0-402b-9cec-a1fe022dc34c",
  "isSidechain": true,
  "agentId": "aba5f8b5a313742c2",
  "requestId": "req_011CbUFcWv2nHhzNtSiuqKLr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7dc9a109-6186-432f-a24b-20bf2148bc7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0121GQpRQHtj5ACBKUGGpkwC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 8885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
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

_source line 10 · 2026-05-28T03:25:18.548Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vfh8KSxhYXkvkxXRfLfBtt`</summary>

```json
{
  "query": "arXiv 2512.23707 rubric reward model scientific reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7dc9a109-6186-432f-a24b-20bf2148bc7d",
  "isSidechain": true,
  "agentId": "aba5f8b5a313742c2",
  "requestId": "req_011CbUFcWv2nHhzNtSiuqKLr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7b966b4-9b29-4c21-9dd2-b86bd5256b98",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0121GQpRQHtj5ACBKUGGpkwC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 8885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
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

_source line 11 · 2026-05-28T03:25:25.020Z_

<details><summary>↩ Tool result · `toolu_01KDnKTjW9XG1PN9udhY7ywJ`</summary>

```text
Web search results for query: "Training AI Co-Scientists arXiv 2512.23707 rubric reinforcement learning scientific"

Links: [{"title":"[2512.23707] Training AI Co-Scientists Using Rubric Rewards","url":"https://arxiv.org/abs/2512.23707"},{"title":"Training AI Co-Scientists with Rubric Rewards","url":"https://www.emergentmind.com/papers/2512.23707"},{"title":"Training AI Co-Scientists Using Rubric Rewards - ArXivIQ","url":"https://arxiviq.substack.com/p/training-ai-co-scientists-using-rubric"},{"title":"Training AI Co-Scientists Using Rubric Rewards","url":"https://arxiv.org/pdf/2512.23707"},{"title":"Training AI Co-Scientists Using Rubric Rewards | alphaXiv","url":"https://www.alphaxiv.org/resources/2512.23707v1"},{"title":"Training AI Co-Scientists Using Rubric Rewards | Papers | HyperAI","url":"https://hyper.ai/en/papers/2512.23707"},{"title":"[Paper Note] Training AI Co-Scientists Using Rubric Rewards, Shashwat Goel+, arXiv'25, 2025.12 · Issue #4101 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/4101"},{"title":"Training AI Co-Scientists Using Rubric Rewards","url":"https://www.researchgate.net/publication/399175480_Training_AI_Co-Scientists_Using_Rubric_Rewards"},{"title":"Training AI Co-Scientists Using Rubric Rewards","url":"https://arxiv.org/html/2512.23707"},{"title":"Training AI Co-Scientists Using Rubric Rewards - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251223707G/abstract"}]

I found the paper! Here's what the search results show about arXiv 2512.23707:

**Title:** Training AI Co-Scientists Using Rubric Rewards

**Main Contribution:** The work studies how to leverage the vast corpus of existing research papers to train language models that generate better research plans. The authors build a scalable, diverse training corpus by automatically extracting research goals and goal-specific grading rubrics from papers across several domains.

**Methodology:** Models are trained for research plan generation via reinforcement learning with self-grading, where a frozen copy of the initial policy acts as the grader during training, with the rubrics creating a generator-verifier gap that enables improvements without external human supervision.

**Validation and Results:** The authors conducted a study with human experts for machine learning research goals spanning 225 hours, where experts preferred plans generated by their finetuned Qwen3-30B-A3B model over the initial model for 70% of research goals, and approved 84% of the automatically extracted goal-specific grading rubrics. Their finetuning yielded 12-22% relative improvements and significant cross-domain generalization, proving effective even in problem settings like medical research where execution feedback is infeasible.

**Authors:** The paper was published on December 29, 2025, by Shashwat Goel, Rishi Hazra, Dulhan Jayalath, and others from Meta Superintelligence Labs and other institutions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6373993-2be0-402b-9cec-a1fe022dc34c",
  "isSidechain": true,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "agentId": "aba5f8b5a313742c2",
  "type": "user",
  "uuid": "010ccdc8-bc23-4f73-aca8-82bf8956d46f",
  "sourceToolAssistantUUID": "b6373993-2be0-402b-9cec-a1fe022dc34c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T03:25:25.100Z_

<details><summary>↩ Tool result · `toolu_01Mc3HXA3BYgJjxfvKxFmVig`</summary>

```text
Web search results for query: ""AI Co-Scientists" rubric RL scientific research plan generation 2025"

Links: [{"title":"[Quick Review] Training AI Co-Scientists Using Rubric Rewards","url":"https://liner.com/review/training-ai-coscientists-using-rubric-rewards"},{"title":"Training AI Co-Scientists Using Rubric Rewards","url":"https://arxiv.org/html/2512.23707"},{"title":"[Paper Note] Training AI Co-Scientists Using Rubric Rewards, Shashwat Goel+, arXiv'25, 2025.12 · Issue #4101 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/4101"},{"title":"Training AI Co-Scientists Using Rubric Rewards | Papers | HyperAI","url":"https://hyper.ai/en/papers/2512.23707"},{"title":"Training AI Co-Scientists with Rubric Rewards","url":"https://www.emergentmind.com/papers/2512.23707"},{"title":"Training AI Co-Scientists Using Rubric Rewards","url":"https://arxiv.org/pdf/2512.23707"},{"title":"Paper page - Training AI Co-Scientists Using Rubric Rewards","url":"https://huggingface.co/papers/2512.23707"}]

Based on the search results, I found comprehensive information about this research:

## Overview

This arXiv 2025 paper presents a method for training AI co-scientists to generate research plans using rubric rewards. The research comes from Meta Superintelligence Labs, ELLIS Institute Tübingen, Max Planck Institute for Intelligent Systems, University of Oxford, and University of Cambridge.

## Core Methodology

To scalably train models to generate better research plans, the approach uses language models to extract training data from scientific papers, including an open-ended research goal and goal-specific rubrics that consist of the essential requirements a valid plan must satisfy.

The plan generator is optimized via Reinforcement Learning with self-grading, where a copy of the initial model acts as the grader and grades the generated plans using the extracted rubrics as privileged information.

## Key Innovation

A frozen copy of the initial policy acts as the grader, accessing the rubrics as privileged information to evaluate plans generated by the training policy, creating a generator-verifier gap that enables improvements without external human supervision.

## Results

Human experts preferred plans from their finetuned Qwen3-30B-A3B model over the initial model for 70% of machine learning research goals, with strong performance gains across medical and arXiv domains, demonstrating significant cross-domain generalization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7dc9a109-6186-432f-a24b-20bf2148bc7d",
  "isSidechain": true,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "agentId": "aba5f8b5a313742c2",
  "type": "user",
  "uuid": "71239f6c-f90c-41f4-90ef-aba3fc76dc0f",
  "sourceToolAssistantUUID": "7dc9a109-6186-432f-a24b-20bf2148bc7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-28T03:25:26.540Z_

<details><summary>↩ Tool result · `toolu_01Vfh8KSxhYXkvkxXRfLfBtt`</summary>

```text
Web search results for query: "arXiv 2512.23707 rubric reward model scientific reasoning"

Links: [{"title":"Training AI Co-Scientists Using Rubric Rewards","url":"https://www.researchgate.net/publication/399175480_Training_AI_Co-Scientists_Using_Rubric_Rewards"},{"title":"Training AI Co-Scientists with Rubric Rewards","url":"https://www.emergentmind.com/papers/2512.23707"},{"title":"Paper page - Training AI Co-Scientists Using Rubric Rewards","url":"https://huggingface.co/papers/2512.23707"},{"title":"[2512.23707] Training AI Co-Scientists Using Rubric Rewards","url":"https://arxiv.org/abs/2512.23707"},{"title":"Training AI Co-Scientists Using Rubric Rewards | alphaXiv","url":"https://www.alphaxiv.org/resources/2512.23707v1"},{"title":"Improving Data and Reward Design for Scientific Reasoning in Large Language Models","url":"https://arxiv.org/pdf/2602.08321"},{"title":"Improving Data and Reward Design for Scientific Reasoning in Large Language Models","url":"https://arxiv.org/html/2602.08321"},{"title":"Reward and Guidance through Rubrics: Promoting Exploration to Improve Multi-Domain Reasoning","url":"https://arxiv.org/pdf/2511.12344"},{"title":"Generating Data-Driven Reasoning Rubrics for Domain-Adaptive Reward Modeling","url":"https://arxiv.org/pdf/2602.06795"}]

Based on the search results, here's what I found about arXiv paper 2512.23707:

## Paper Overview

The paper "Training AI Co-Scientists Using Rubric Rewards" was submitted on December 29, 2025, and is authored by Shashwat Goel, Rishi Hazra, Dulhan Jayalath, Timon Willi, and collaborators.

## Main Focus

The paper focuses on AI co-scientists as tools to assist human researchers in achieving their research goals, with a crucial feature being the ability to generate research plans given a set of aims and constraints. However, language models currently struggle to generate research plans that follow all constraints and implicit requirements, so the work studies how to leverage the vast corpus of existing research papers to train language models that generate better research plans.

## Key Innovation: Rubric Reward Model

The paper introduces the Rubric Reward Model (RRM), a process-oriented reward function that evaluates the entire reasoning trajectory against problem-specific rubrics. The researchers build a scalable, diverse training corpus by automatically extracting research goals and goal-specific grading rubrics from papers across several domains, and then train models for research plan generation via reinforcement learning with self-grading.

## Research Contribution

The instance-specific rubric mechanism provides a robust framework for aligning LLMs with nuanced, domain-appropriate desiderata that cannot be distilled from fixed-format, synthetic data or passive imitation learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7b966b4-9b29-4c21-9dd2-b86bd5256b98",
  "isSidechain": true,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "agentId": "aba5f8b5a313742c2",
  "type": "user",
  "uuid": "12b47f52-9678-4a94-92f1-f305b4870ada",
  "sourceToolAssistantUUID": "c7b966b4-9b29-4c21-9dd2-b86bd5256b98",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-28T03:25:29.386Z_

I found the paper. Now let me fetch the full paper content from the arXiv HTML version and the abstract page to get comprehensive details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12b47f52-9678-4a94-92f1-f305b4870ada",
  "isSidechain": true,
  "agentId": "aba5f8b5a313742c2",
  "requestId": "req_011CbUFdQAFeB1XkzuxxqCBv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ce91bd8-b937-4925-bfb2-448272c4f857",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TPi1ZZ2n4RLFy3khQLg5f1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2510,
      "cache_read_input_tokens": 10010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2510,
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

_source line 15 · 2026-05-28T03:25:30.128Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NR2nQtabYwZJ9zAi3cQViZ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.23707",
  "prompt": "Extract the full abstract, list of authors, their affiliations, and any summary information about this paper. Include all details about the methodology, contributions, and results mentioned on this page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ce91bd8-b937-4925-bfb2-448272c4f857",
  "isSidechain": true,
  "agentId": "aba5f8b5a313742c2",
  "requestId": "req_011CbUFdQAFeB1XkzuxxqCBv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f71cd9de-3c9e-4333-ac38-565e6e5d9620",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TPi1ZZ2n4RLFy3khQLg5f1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2510,
      "cache_read_input_tokens": 10010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2510,
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

_source line 16 · 2026-05-28T03:25:33.933Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VfAhSQ7fbHytraJCFBbrwu`</summary>

```json
{
  "url": "https://arxiv.org/html/2512.23707",
  "prompt": "Extract ALL details from this paper including: 1) The full abstract, 2) Introduction and motivation, 3) The complete methodology - how rubrics are extracted from papers, how RL training works with self-grading, the generator-verifier gap concept, 4) What scientific domains are covered, 5) Whether this is multimodal or text-only, 6) All experimental results including the human study details, automatic evaluation metrics, cross-domain generalization results, 7) Key contributions listed by the authors, 8) How this relates to non-verifiable reasoning tasks, 9) The training pipeline details, 10) Any limitations discussed. Be as comprehensive as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f71cd9de-3c9e-4333-ac38-565e6e5d9620",
  "isSidechain": true,
  "agentId": "aba5f8b5a313742c2",
  "requestId": "req_011CbUFdQAFeB1XkzuxxqCBv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38aa1435-9317-4b17-8e46-b56910ca1c40",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TPi1ZZ2n4RLFy3khQLg5f1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2510,
      "cache_read_input_tokens": 10010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2510,
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

### Tool result

_source line 17 · 2026-05-28T03:25:36.737Z_

<details><summary>↩ Tool result · `toolu_01NR2nQtabYwZJ9zAi3cQViZ`</summary>

```text
# Paper Summary: Training AI Co-Scientists Using Rubric Rewards

## Full Abstract
The paper addresses how to train language models to generate better research plans. Researchers built a scalable training corpus by extracting research goals and grading rubrics from papers across multiple domains. They employed reinforcement learning with self-grading, where a frozen initial policy model acts as evaluator during training. The rubrics create a gap between generator and verifier, enabling improvements without external human supervision.

## Authors
Shashwat Goel, Rishi Hazra, Dulhan Jayalath, Timon Willi, Parag Jain, William F. Shen, Ilias Leontiadis, Francesco Barbieri, Yoram Bachrach, Jonas Geiping, and Chenxi Whitehouse

*Note: Author affiliations are not listed on this arXiv abstract page.*

## Key Contributions & Results

**Validation Study:** Human expert evaluation spanning 225 hours for machine learning research showed the finetuned Qwen3-30B-A3B model was preferred "70% of the time" and "84% of automatically extracted goal-specific grading rubrics" received expert approval.

**Generalization:** The approach demonstrates "12-22% relative improvements" and cross-domain effectiveness, extending successfully to medical research goals and new arXiv preprints evaluated by frontier model panels.

## Paper Details
- **Submission Date:** December 29, 2025
- **Length:** 11 pages main text, 119 pages including appendices
- **Classifications:** Machine Learning (cs.LG), Computation and Language (cs.CL), Human-Computer Interaction (cs.HC)
- **License:** CC BY 4.0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f71cd9de-3c9e-4333-ac38-565e6e5d9620",
  "isSidechain": true,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "agentId": "aba5f8b5a313742c2",
  "type": "user",
  "uuid": "c8c34d8a-55ea-4a62-82ce-1b2a5434ca6b",
  "sourceToolAssistantUUID": "f71cd9de-3c9e-4333-ac38-565e6e5d9620",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-28T03:26:05.545Z_

<details><summary>↩ Tool result · `toolu_01VfAhSQ7fbHytraJCFBbrwu`</summary>

```text
# Comprehensive Summary: Training AI Co-Scientists Using Rubric Rewards

## 1. Abstract
The paper proposes a scalable approach to train language models that generate research plans for open-ended scientific goals. Rather than requiring execution feedback (which is infeasible for most science), the method extracts training data from existing papers and uses "self-grading with goal-specific rubrics as privileged information" to create a generator-verifier gap. A frozen copy of the initial model grades plans using rubrics accessible only to the grader. Human evaluation shows experts prefer the finetuned 30B model's plans in 70% of cases.

## 2. Introduction and Motivation
The authors argue that unlike well-defined tasks (math, coding) where "rapid feedback for training" is available, scientific research planning is open-ended. Rather than building specialized execution environments for each domain, they propose training "co-scientists" that help researchers by generating sound plans before implementation. This mirrors scientific apprenticeships where advisors critique plans before experiments begin, avoiding "wasting significant resources" or raising ethical concerns with flawed early-stage plans.

## 3. Complete Methodology

### 3.1 Rubric Extraction Pipeline
The system extracts training samples from papers through four steps:

**Extract Insights**: A sample creator model identifies up to three novel "insights" or reasoning approaches in papers.

**Generate Goals and Rubrics**: For each insight, the system creates:
- A research goal: "self-contained description, including constraints and key uncertainties"
- 15 preliminary rubric items, filtered to 10 final items testing "must-have features" of valid plans

**Generate Reference Solutions**: Using paper context and rubrics as privileged information, the creator model summarizes how the paper solved the problem.

**Filter for Quality**: A selector model independently scores each component. The sample with highest average score becomes the training sample. Filtering improves composite scores from 0.84 to 0.89 across domains.

### 3.2 Rubric Grading System
The grader uses two key resources:

**Goal-Specific Rubrics**: Extracted from papers, these provide instance-specific evaluation criteria.

**Seven General Guidelines**:
- Handles all criteria
- Detailed, specific solution
- No overlooked flaws
- Well-justified rationale
- Cost and effort efficient
- No ethical issues
- Consistent with overall plan

The grader checks which guidelines are violated for each rubric item. An item is satisfied only if zero violations are found. Final score = (satisfied items / total items).

### 3.3 RL Training with Self-Rewards
- Uses Group Relative Policy Optimization (GRPO) with group size 8
- Frozen copy of initial Qwen-3-30B acts as reward model
- No KL penalty (exploration encouraged)
- Length constraint: final plan limited to 750 words (unlimited thinking tokens permitted)
- Reward formula: (# satisfied rubric items / # rubric items) - format penalty indicator

## 4. Scientific Domains Covered

**ResearchPlanGen-ML**: 6,872 training samples from NeurIPS 2023-2024, ICLR 2025; 685 test samples from top ~2% papers

**ResearchPlanGen-ArXiv**: 6,573 training samples from 2024; 1,496 test samples from August-September 2025 across 8 subjects (Physics, Math, Statistics, CS, Economics, EESS, Quantitative Finance, Quantitative Biology)

**ResearchPlanGen-Medical**: Papers from PMC/OpenAccess dataset (post-March 2023)

## 5. Modality
Text-only. The paper does not incorporate images, tables, or other modalities in the generation or evaluation process.

## 6. Experimental Results

### 6.1 Human Study (ML Domain Only)
- 25 expert annotators (graduate students to senior practitioners)
- 100 test samples, each reviewed by 3 topic experts
- 45 minutes per annotation

**Key Findings**:
- Finetuned model preferred in 70.0% ± 5.3% of annotations (p<0.0001)
- Initial model: 7.3/10 average score; Finetuned: 7.89/10
- Finetuned model stronger on: addressing requirements, soundness, predicted outcomes
- Finetuned model weaker on: clarity and feasibility (likely due to weaker grading on cost-efficiency)
- 84% of automatically extracted rubric items rated necessary (≥4/5)

**Criteria-wise Breakdown**:
- Addresses Requirements: 77% win rate
- Soundness: 75% win rate
- Predicted Outcomes: 82% win rate
- Clear Execution: 49% win rate
- Feasibility: 45% win rate

### 6.2 Automated Evaluation (Jury of Three Frontier Models)
Using GPT-5-Thinking, Claude-4-Sonnet, Gemini-2.5-Pro consensus:

**Within-Domain Improvements**:
- ML: 10-15% relative improvement
- ArXiv: 12-22% relative improvement
- Medical: Significant improvements without real execution feedback

**Performance Comparison**:
- Our Qwen-3-30B finetuned: ~36% rubric satisfaction (ML), competitive with Grok-4-Thinking
- GPT-5-Thinking: Substantially better (~49%)
- Gap remains to frontier models despite improvements

**Jury Alignment**:
- Cohen's κ = 0.297 with human consensus (significantly above chance, p<0.01)
- GPT-5-Thinking individual agreement: 75.3% with humans (κ=0.441)
- Gemini-2.5-Pro: 73.9% (κ=0.269)
- Claude-4-Sonnet: 50.0% (κ=0.076)

### 6.3 Cross-Domain Generalization
The medical-finetuned model achieves:
- 15% relative improvement on ML tasks
- 17.5% on ArXiv tasks
- Sometimes outperforms domain-specific finetuning, suggesting "general research plan principles"

### 6.4 Other Model Architectures
Tested generalization across:
- Gemma-3-4B: 12.0-16.7% improvements
- Llama-3.1-8B: 4.9-18.5% improvements
- Qwen-3-4B instruct vs. thinking: similar performance (thinking 2x compute cost)

## 7. Key Contributions (Author-Stated)

1. "Scalable recipe to extract research goals, and rubrics to grade research plans proposed for each goal, from scientific papers" with public ResearchPlanGen dataset release

2. "Human study with ML experts demonstrates that training via rubric-guided self-grading significantly improves the quality of generated research plans, without requiring the construction of specialized execution environments"

3. "Cross-domain generalization, providing evidence for the viability of training generalist AI Co-scientists"

## 8. Relation to Non-Verifiable Reasoning Tasks

The work directly addresses the non-verifiable reasoning problem. Unlike code or math problems with executable feedback, "verification of research plans by executing experiments is slow and expensive to obtain." The paper shows that self-grading with rubrics creates a "generator-verifier gap" that enables training without external supervision. However, this relies on the initial model's grading being directionally correct—an assumption validated only post-hoc through human study and stronger model jury evaluation.

## 9. Training Pipeline Details

**Data Collection**:
- Paper filtering: documents >15,000 words excluded
- 1-3 candidate samples per paper → 1 selected sample per paper

**RL Training**:
- Learning rate: 1×10⁻⁶
- Batch size: 64
- Temperature: 0.7
- Hardware: Qwen-3-30B trained on 2 A100 80GB nodes
- Max output tokens: 2048 (actor), 8192 (judge)

**Stopping Criteria**:
- Checkpoint selection based on validation performance with Claude-4-Sonnet
- ML Finetune: 100 steps; Medical: 140 steps
- Selection driven by held-out stronger grader to detect overoptimization

**Reference Solutions as Privileged Information**:
- Provided to grader (reward model) to strengthen evaluation signal
- Not provided to plan generator (policy)

## 10. Limitations Acknowledged

- "Instead of implementing each proposed research plan and observing the outcomes, we use human expert preferences for evaluation"—this is "a useful proxy" but not ground truth

- "Only for one domain (machine learning), and only after developing our final model" could human evaluation be afforded

- Finetuned plans become "more complicated after training" due to "Qwen-3-30B-MoE being poor at grading itself on cost and effort efficiency"

- "Self-grading is important as stronger graders are unavailable at the frontier"—reliance on weaker models for training creates divergence risk

- "At the sample level, the task of comparing research plans can be quite subjective"—though aggregate statistics provide significant evidence

## Additional Notable Details

**Reward Model Overoptimization**: Figure 4 shows plans self-grade as improving indefinitely, but Claude-4-Sonnet grading diverges after ~step 120, demonstrating reward hacking despite rubric-based training.

**SFT Failure**: Supervised fine-tuning on reference solutions worsens performance (24.1% → 3.4% satisfaction), confirming RL's superiority for long-form outputs.

**Validation Protocol**: The approach uses "privileged information" (rubrics, reference solutions) available to grader but not generator, creating intentional asymmetry to enable training signals.

**Structured Grading Output**: Grader explicitly lists which guidelines are violated—enabling interpretable error analysis and ablations along seven distinct dimensions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38aa1435-9317-4b17-8e46-b56910ca1c40",
  "isSidechain": true,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "agentId": "aba5f8b5a313742c2",
  "type": "user",
  "uuid": "4011469a-fa12-46c7-82f6-f37c27c0a537",
  "sourceToolAssistantUUID": "38aa1435-9317-4b17-8e46-b56910ca1c40",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-28T03:26:08.349Z_

Excellent -- I got very comprehensive details. Let me also fetch the EmergentMind summary to get any additional details and cross-reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4011469a-fa12-46c7-82f6-f37c27c0a537",
  "isSidechain": true,
  "agentId": "aba5f8b5a313742c2",
  "requestId": "req_011CbUFgGwWPLhpvpzZJTfa6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9adb968a-9648-44a1-a63c-cafcff4859e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Trt9FCqCBbruoSQajE6SG6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3173,
      "cache_read_input_tokens": 12520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3173,
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

_source line 20 · 2026-05-28T03:26:10.033Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ghoi14NibGeJDXxKkip3mb`</summary>

```json
{
  "url": "https://www.emergentmind.com/papers/2512.23707",
  "prompt": "Extract any additional details about the paper's methodology, results, or contributions that supplement what we already know. Focus on: the exact rubric extraction pipeline, RL training details, how the generator-verifier gap works, cross-domain results, and any discussion of the relationship to non-verifiable reasoning tasks."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9adb968a-9648-44a1-a63c-cafcff4859e9",
  "isSidechain": true,
  "agentId": "aba5f8b5a313742c2",
  "requestId": "req_011CbUFgGwWPLhpvpzZJTfa6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf4a147d-0252-46b7-aa1a-ab4522913340",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Trt9FCqCBbruoSQajE6SG6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3173,
      "cache_read_input_tokens": 12520,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3173
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 12520,
          "cache_creation_input_tokens": 3173,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3173,
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

_source line 21 · 2026-05-28T03:26:19.158Z_

<details><summary>↩ Tool result · `toolu_01Ghoi14NibGeJDXxKkip3mb`</summary>

```text
# Supplementary Details on Paper Methodology and Results

## Rubric Extraction Pipeline

The automated extraction process involves two LLM stages. First, one model generates multiple candidate goal-rubric-solution triplets from scientific papers. A second LLM then "filters and assesses for quality" by selecting the best candidates. The rubrics codify "must-have requirements for a valid plan" and are goal-specific, extracted directly from paper content alongside research aims and constraints.

## RL Training Mechanism

Training uses Group Relative Policy Optimization (GRPO) where "a frozen copy of the initial policy acts as the grader during training." This frozen model accesses "privileged information" in the form of goal-specific rubrics, creating what researchers call the "generator-verifier gap." The grader scores plans by evaluating compliance against both instance-specific rubrics and "seven general guidelines" covering clarity, justification, cost-efficiency, and ethics. The study disabled "KL divergence penalty" during training, an unusual finding suggesting "plans benefit from less-constrained exploration."

## Generator-Verifier Gap Mechanism

The gap functions as an asymmetry: the verifier (frozen grader) knows the rubric checklist; the generator (training model) does not. This design avoids "noisy scalar feedback" by providing "fine-grained" rubric-based rewards. Researchers note this setup enables "improvements without external human supervision."

## Cross-Domain Results

Models finetuned on one domain showed "notable cross-domain improvements." Notably, "medical-domain finetunes substantially improved performance on ML and ArXiv goals, exceeding ArXiv-specific finetuning" in transfer evaluations. Overall improvements ranged "12–22% relative" across domains.

## Non-Verifiable Reasoning Context

The work explicitly addresses settings "where execution feedback is infeasible," particularly medicine. The approach circumvents "the impracticality of trial-and-error RL" by substituting rubric satisfaction for end-to-end experimental validation, positioning it as a scalable method for high-expertise, slow-feedback domains.

Human evaluation (225 expert hours in ML) yielded 70% preference rates for finetuned outputs and 84% approval of automatically extracted rubric items.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf4a147d-0252-46b7-aa1a-ab4522913340",
  "isSidechain": true,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "agentId": "aba5f8b5a313742c2",
  "type": "user",
  "uuid": "ad8e5322-b716-4f20-a9f2-981eb9a61d1c",
  "sourceToolAssistantUUID": "bf4a147d-0252-46b7-aa1a-ab4522913340",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-28T03:27:01.516Z_

I now have a thorough understanding of this paper. Here is my detailed report.

---

## "Training AI Co-Scientists Using Rubric Rewards" (arXiv:2512.23707, Dec 2025)

**Authors:** Shashwat Goel, Rishi Hazra, Dulhan Jayalath, Timon Willi, Parag Jain, William F. Shen, Ilias Leontiadis, Francesco Barbieri, Yoram Bachrach, Jonas Geiping, and Chenxi Whitehouse

**Affiliations:** Meta Superintelligence Labs, ELLIS Institute Tubingen, Max Planck Institute for Intelligent Systems, University of Oxford, University of Cambridge

**Paper length:** 11 pages main text, 119 pages including appendices

---

### 1. Scientific Reasoning Tasks Addressed

The paper addresses **research plan generation** -- given an open-ended scientific research goal (with aims and constraints), the model must produce a detailed, sound research plan. This is fundamentally different from math/code tasks because there is no executable verifier. The paper covers three scientific domains:

- **ResearchPlanGen-ML:** 6,872 training samples from NeurIPS 2023-2024 and ICLR 2025; 685 test samples from top ~2% papers
- **ResearchPlanGen-ArXiv:** 6,573 training samples from 2024 across 8 subjects (Physics, Math, Statistics, CS, Economics, EESS, Quantitative Finance, Quantitative Biology); 1,496 test samples from Aug-Sep 2025
- **ResearchPlanGen-Medical:** Papers from PMC/OpenAccess dataset (post-March 2023)

The core task is: given a research goal description, generate a plan that satisfies all implicit and explicit requirements, constraints, and domain conventions -- without access to the actual paper's solution.

---

### 2. How Rubrics Are Used for RL Training

This is the paper's central contribution. The pipeline has four stages:

**Stage 1 -- Extract Insights:** A "sample creator" LLM identifies up to 3 novel insights or reasoning approaches from each paper.

**Stage 2 -- Generate Goals and Rubrics:** For each insight, the system creates:
- A self-contained research goal description (including constraints and key uncertainties)
- 15 preliminary rubric items, filtered down to 10 final items that test "must-have features" of a valid plan

**Stage 3 -- Generate Reference Solutions:** Using the paper content and rubrics as privileged information, the creator model summarizes how the paper solved the problem.

**Stage 4 -- Quality Filtering:** A separate selector model scores each component independently. The best sample per paper is selected. This filtering improves composite scores from 0.84 to 0.89.

**RL Training with Self-Grading:**
- Uses **Group Relative Policy Optimization (GRPO)** with group size 8
- A **frozen copy of the initial Qwen-3-30B model** serves as the reward model/grader
- The grader receives **privileged information** (the rubrics + reference solutions) that the generator policy does NOT see -- this creates an intentional asymmetry called the **"generator-verifier gap"**
- The grader evaluates each plan against both the 10 goal-specific rubric items AND 7 general guidelines (handles all criteria, detailed/specific solution, no overlooked flaws, well-justified rationale, cost/effort efficient, no ethical issues, internally consistent)
- A rubric item is satisfied only if zero guideline violations are found
- **Reward = (# satisfied rubric items / total rubric items) - format penalty**
- No KL divergence penalty is used (an unusual design choice; the authors find less-constrained exploration benefits plan quality)
- Final plans are limited to 750 words, though unlimited thinking tokens are permitted
- Training: LR 1e-6, batch size 64, temperature 0.7, trained on 2x A100 80GB nodes
- Checkpoint selection uses a held-out stronger grader (Claude-4-Sonnet) to detect reward model overoptimization

**Key insight:** The rubrics enable a *process-oriented, instance-specific* reward signal. Rather than a single scalar "good/bad" score, the grader provides fine-grained feedback along multiple domain-specific dimensions. The frozen grader knows what a good plan should contain (via rubrics), while the generator must figure this out from the goal alone.

---

### 3. Multimodal or Text-Only?

**Text-only.** The paper does not incorporate images, tables, figures, or any other modalities in either the generation or evaluation pipeline. Inputs are textual research goals, and outputs are textual research plans.

---

### 4. Key Contributions and Results

**Stated contributions:**
1. A **scalable recipe** to extract research goals and goal-specific grading rubrics from scientific papers, with public release of the ResearchPlanGen dataset
2. A **human study with ML experts** (225 hours, 25 expert annotators, 100 test samples) demonstrating that rubric-guided self-grading significantly improves plan quality without specialized execution environments
3. Evidence of **cross-domain generalization**, supporting the viability of training generalist AI co-scientists

**Key results:**

| Metric | Value |
|--------|-------|
| Human preference for finetuned vs. base model | 70.0% +/- 5.3% (p < 0.0001) |
| Average human score (base vs. finetuned) | 7.3/10 vs. 7.89/10 |
| Rubric items rated necessary by experts | 84% |
| Relative improvement (ML domain) | 10-15% |
| Relative improvement (ArXiv domain) | 12-22% |
| Cross-domain transfer (medical -> ML) | 15% relative improvement |
| Cross-domain transfer (medical -> ArXiv) | 17.5% relative improvement |

**Criteria-wise human preference (finetuned win rate):**
- Addresses Requirements: 77%
- Soundness: 75%
- Predicted Outcomes: 82%
- Clear Execution: 49% (weaker)
- Feasibility: 45% (weaker -- plans become more complex)

**Other notable findings:**
- Supervised fine-tuning (SFT) on reference solutions actually **worsens** performance (24.1% -> 3.4% rubric satisfaction), confirming RL's superiority for this long-form generation task
- The medical-finetuned model sometimes **outperforms domain-specific finetuning** when transferred, suggesting the model learns "general research planning principles"
- The approach generalizes across model architectures: Gemma-3-4B (12-17% improvement), Llama-3.1-8B (5-18.5% improvement)
- Reward model overoptimization is observed: self-graded scores improve indefinitely, but Claude-4-Sonnet grading diverges after ~step 120, demonstrating reward hacking even with rubric-based rewards

---

### 5. Relationship to Non-Verifiable Scientific Reasoning with Rubric-Based Rewards

This paper directly and explicitly addresses the **non-verifiable reasoning** problem. The core motivation is stated upfront: unlike math (checkable proofs) or code (executable tests), scientific research plans cannot be verified through execution -- "verification of research plans by executing experiments is slow and expensive to obtain." In medical research, execution feedback is often entirely infeasible due to ethical constraints, cost, and timelines.

The paper's solution is to **replace execution-based verification with rubric-based self-grading.** The key elements that make this work for non-verifiable domains:

1. **Rubrics as surrogate verifiers:** Goal-specific rubrics extracted from papers serve as a proxy for ground-truth execution outcomes. They encode domain-specific "must-have" requirements without needing to actually run experiments.

2. **Privileged information asymmetry:** The grader sees rubrics and reference solutions; the generator sees only the goal. This creates a training signal even when the generator cannot self-verify.

3. **Self-grading eliminates external supervision:** No human-in-the-loop or stronger external model is needed during training. The frozen base model, augmented with rubrics, provides sufficient signal.

4. **Scalability across domains:** The same pipeline works for ML, physics, math, economics, medicine, etc., because rubrics are automatically extracted from any paper corpus.

5. **Limitations acknowledged:** The approach depends on the initial model being a directionally correct grader when given rubrics (validated post-hoc). Reward model overoptimization remains a challenge. The paper notes that "at the sample level, the task of comparing research plans can be quite subjective."

This positions the paper as a foundational method for applying RL to **open-ended, non-verifiable reasoning tasks** where traditional reward signals (correctness, execution success) are unavailable. The rubric mechanism transforms an unverifiable generation problem into a (partially) verifiable checklist-grading problem.

---

Sources:
- [arXiv Abstract: Training AI Co-Scientists Using Rubric Rewards](https://arxiv.org/abs/2512.23707)
- [arXiv HTML Full Paper](https://arxiv.org/html/2512.23707)
- [EmergentMind Summary](https://www.emergentmind.com/papers/2512.23707)
- [HuggingFace Paper Page](https://huggingface.co/papers/2512.23707)
- [ArXivIQ Substack Discussion](https://arxiviq.substack.com/p/training-ai-co-scientists-using-rubric)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad8e5322-b716-4f20-a9f2-981eb9a61d1c",
  "isSidechain": true,
  "agentId": "aba5f8b5a313742c2",
  "requestId": "req_011CbUFhHBBMu54d9wgi4aeF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df2ede42-2bd7-4975-af12-d8f1c0874aeb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0181HdZYiTL6Y4DzykUZezwA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 696,
      "cache_read_input_tokens": 15693,
      "output_tokens": 2316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 696
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2316,
          "cache_read_input_tokens": 15693,
          "cache_creation_input_tokens": 696,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 696,
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
