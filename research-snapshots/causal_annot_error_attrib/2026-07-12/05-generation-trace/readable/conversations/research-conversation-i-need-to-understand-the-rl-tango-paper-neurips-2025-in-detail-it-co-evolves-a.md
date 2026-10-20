# Research conversation: I need to understand the RL Tango paper (NeurIPS 2025) in detail. It co-evolves a generator and generative verifier via 

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-af40b24dedf103df7.jsonl`
- **Structured JSON:** [`c5e80d720c9bb84f81bd.json`](../../sessions/c5/c5e80d720c9bb84f81bd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-28T01:52:32.858Z_

I need to understand the RL Tango paper (NeurIPS 2025) in detail. It co-evolves a generator and generative verifier via RL without process-level annotations, achieving 25.5% relative improvement.

Please search for and read this paper. I need to know:
1. Full title and authors
2. Exact method: how does it co-evolve generator and verifier?
3. What benchmarks and results? The 25.5% relative improvement - on what?
4. Does it use MC estimation at all? Does it need process-level labels?
5. How is it relevant to training process reward models?
6. What are its limitations?

Try searches like "RL Tango NeurIPS 2025 generator verifier co-evolution", "RL Tango reinforcement learning verifier", and fetch the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bf18714b-0e92-4a91-be0e-dc43bfe729a9",
  "agentId": "af40b24dedf103df7",
  "type": "user",
  "uuid": "9ca8810b-a837-4869-ab4e-503d40d26083",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-28T01:52:32.863Z_

```json
{
  "parentUuid": "9ca8810b-a837-4869-ab4e-503d40d26083",
  "isSidechain": true,
  "agentId": "af40b24dedf103df7",
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
  "uuid": "d0b8ce87-0683-4ea3-b9fe-5fdc49d6da81",
  "timestamp": "2026-05-28T01:52:32.863Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-28T01:52:32.864Z_

```json
{
  "parentUuid": "d0b8ce87-0683-4ea3-b9fe-5fdc49d6da81",
  "isSidechain": true,
  "agentId": "af40b24dedf103df7",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "932bfd3c-81f7-4253-b8fc-fb1b02818da2",
  "timestamp": "2026-05-28T01:52:32.864Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-28T01:52:35.842Z_



I'll search for the RL Tango paper online to get detailed information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "932bfd3c-81f7-4253-b8fc-fb1b02818da2",
  "isSidechain": true,
  "agentId": "af40b24dedf103df7",
  "requestId": "req_011CbU8YYLgFfBdSYE81wauQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0845d65-088c-4aba-aa57-1af720c2ac44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MvZcZJujst9UkjaxEF749V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1506,
      "cache_read_input_tokens": 7411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1506,
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

_source line 5 · 2026-05-28T01:52:36.197Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JpY5CsBcQWcfbrc75f2CMV`</summary>

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
  "parentUuid": "c0845d65-088c-4aba-aa57-1af720c2ac44",
  "isSidechain": true,
  "agentId": "af40b24dedf103df7",
  "requestId": "req_011CbU8YYLgFfBdSYE81wauQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "478b9b5f-916e-4a4e-a50c-c12144d56099",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MvZcZJujst9UkjaxEF749V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1506,
      "cache_read_input_tokens": 7411,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1506
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 98,
          "cache_read_input_tokens": 7411,
          "cache_creation_input_tokens": 1506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1506,
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

_source line 6 · 2026-05-28T01:52:36.200Z_

<details><summary>↩ Tool result · `toolu_01JpY5CsBcQWcfbrc75f2CMV`</summary>

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
  "parentUuid": "478b9b5f-916e-4a4e-a50c-c12144d56099",
  "isSidechain": true,
  "promptId": "bf18714b-0e92-4a91-be0e-dc43bfe729a9",
  "agentId": "af40b24dedf103df7",
  "type": "user",
  "uuid": "71c8f3c2-877a-41b9-93bb-d347b9a4e653",
  "sourceToolAssistantUUID": "478b9b5f-916e-4a4e-a50c-c12144d56099",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T01:52:38.744Z_



Now let me search for the RL Tango paper with multiple queries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71c8f3c2-877a-41b9-93bb-d347b9a4e653",
  "isSidechain": true,
  "agentId": "af40b24dedf103df7",
  "requestId": "req_011CbU8Ynnb7FuDrtQ4bf83k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8cdf2327-1d14-4f7b-8ed4-299fe6f336fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjahxiZTtMSZXVVAmQDKdz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1120,
      "cache_read_input_tokens": 8917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1120,
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

_source line 8 · 2026-05-28T01:52:39.751Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R13xAz3vPWAoJaYnecyc7k`</summary>

```json
{
  "query": "RL Tango NeurIPS 2025 generator verifier co-evolution reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cdf2327-1d14-4f7b-8ed4-299fe6f336fb",
  "isSidechain": true,
  "agentId": "af40b24dedf103df7",
  "requestId": "req_011CbU8Ynnb7FuDrtQ4bf83k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d21ac42f-b098-485b-b73e-45b24846da46",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjahxiZTtMSZXVVAmQDKdz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1120,
      "cache_read_input_tokens": 8917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1120,
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

_source line 9 · 2026-05-28T01:52:40.226Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YFP4erqnWtaCsDg4UGChGM`</summary>

```json
{
  "query": "\"RL Tango\" paper reinforcement learning generative verifier process reward model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d21ac42f-b098-485b-b73e-45b24846da46",
  "isSidechain": true,
  "agentId": "af40b24dedf103df7",
  "requestId": "req_011CbU8Ynnb7FuDrtQ4bf83k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a288789-fc7e-47e0-8eba-9414813f4a03",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjahxiZTtMSZXVVAmQDKdz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1120,
      "cache_read_input_tokens": 8917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1120,
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

_source line 10 · 2026-05-28T01:52:41.095Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016fxbeXcr8KEgK5QxQGWwS1`</summary>

```json
{
  "query": "RL Tango 25.5% relative improvement co-evolve generator verifier arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a288789-fc7e-47e0-8eba-9414813f4a03",
  "isSidechain": true,
  "agentId": "af40b24dedf103df7",
  "requestId": "req_011CbU8Ynnb7FuDrtQ4bf83k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a250d2a4-35c0-48a2-acb3-da68fbca7139",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjahxiZTtMSZXVVAmQDKdz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1120,
      "cache_read_input_tokens": 8917,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1120
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 198,
          "cache_read_input_tokens": 8917,
          "cache_creation_input_tokens": 1120,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1120,
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

_source line 11 · 2026-05-28T01:52:45.265Z_

<details><summary>↩ Tool result · `toolu_01YFP4erqnWtaCsDg4UGChGM`</summary>

```text
Web search results for query: ""RL Tango" paper reinforcement learning generative verifier process reward model"

Links: [{"title":"RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning","url":"https://arxiv.org/pdf/2505.15034"},{"title":"NeurIPS Poster RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning","url":"https://neurips.cc/virtual/2025/poster/118724"},{"title":"RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning","url":"https://openreview.net/pdf?id=JRkFZl0TJ2"},{"title":"RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250515034Z/abstract"},{"title":"RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning","url":"https://arxiv.org/html/2505.15034v2"},{"title":"RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.15034v2"},{"title":"[2505.15034] RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning","url":"https://arxiv.org/abs/2505.15034"},{"title":"RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning | OpenReview","url":"https://openreview.net/forum?id=JRkFZl0TJ2"},{"title":"Paper page - RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning","url":"https://huggingface.co/papers/2505.15034"}]

I found the RL Tango paper! Here's what the research is about:

## Overview

RL Tango is a reinforcement learning approach for enhancing the reasoning capabilities of large language models, where an LLM generator serves as a policy guided by a verifier (reward model).

## Key Innovation

A central innovation of TANGO is its generative, process-level LLM verifier, which is trained via RL and co-evolves with the generator. The verifier is trained solely based on outcome-level verification correctness rewards without requiring explicit process-level annotations.

## Problem It Addresses

Current RL post-training methods for LLMs typically use verifiers that are fixed or trained discriminatively via supervised finetuning, designs that are susceptible to reward hacking and generalize poorly beyond their training distributions.

## Framework

TANGO uses RL to concurrently train both an LLM generator and a verifier in an interleaved manner. The generative RL-trained verifier exhibits improved robustness and superior generalization compared to deterministic or SFT-trained verifiers, fostering effective mutual reinforcement with the generator.

## Results

Both components of TANGO achieve state-of-the-art results among 7B/8B-scale models: the generator attains best-in-class performance across five competition-level math benchmarks and four challenging out-of-domain reasoning tasks, while the verifier leads on the ProcessBench dataset.

The code is available at: https://github.com/kaiwenzha/rl-tango


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a288789-fc7e-47e0-8eba-9414813f4a03",
  "isSidechain": true,
  "promptId": "bf18714b-0e92-4a91-be0e-dc43bfe729a9",
  "agentId": "af40b24dedf103df7",
  "type": "user",
  "uuid": "c800678c-f3d4-40cb-868c-b70b16cc281d",
  "sourceToolAssistantUUID": "5a288789-fc7e-47e0-8eba-9414813f4a03",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T01:52:45.864Z_

<details><summary>↩ Tool result · `toolu_01R13xAz3vPWAoJaYnecyc7k`</summary>

```text
Web search results for query: "RL Tango NeurIPS 2025 generator verifier co-evolution reinforcement learning"

Links: [{"title":"RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning | OpenReview","url":"https://openreview.net/forum?id=JRkFZl0TJ2"},{"title":"NeurIPS Poster RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning","url":"https://neurips.cc/virtual/2025/poster/118724"},{"title":"[PDF] RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RL-Tango:-Reinforcing-Generator-and-Verifier-for-Zha-Gao/5becc8d0a5066c58d2785798519f2cddad7f4482"},{"title":"RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.15034v2"},{"title":"[Literature Review] RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning","url":"https://www.themoonlight.io/en/review/rl-tango-reinforcing-generator-and-verifier-together-for-language-reasoning"},{"title":"Paper page - RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning","url":"https://huggingface.co/papers/2505.15034"},{"title":"[2505.15034] RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning","url":"https://arxiv.org/abs/2505.15034"},{"title":"CoVerRL: Breaking the Consensus Trap in Label-Free Reasoning via Generator-Verifier Co-Evolution","url":"https://arxiv.org/pdf/2603.17775"}]

Based on the search results, here's what I found about RL Tango:

## RL Tango Overview

RL Tango is a novel co-evolutionary framework that uses RL to concurrently train an LLM generator and an LLM verifier in an interleaved manner for LLM reasoning. It was presented as a NeurIPS 2025 poster.

## Key Innovation: Generator-Verifier Co-Evolution

A central innovation of Tango is its generative, process-level LLM verifier, which is trained via RL and co-evolves with the generator. The verifier is trained solely based on outcome-level verification correctness rewards without requiring explicit process-level annotations.

## Motivation

Current RL post-training methods for LLMs typically use verifiers that are fixed or trained discriminatively via supervised fine-tuning, which are susceptible to reward hacking and generalize poorly beyond their training distributions.

## Results

The generative RL-trained verifier exhibits improved robustness and superior generalization compared to deterministic or SFT-trained verifiers, fostering effective mutual reinforcement with the generator. Both components achieve state-of-the-art results among 7B/8B-scale models across multiple benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d21ac42f-b098-485b-b73e-45b24846da46",
  "isSidechain": true,
  "promptId": "bf18714b-0e92-4a91-be0e-dc43bfe729a9",
  "agentId": "af40b24dedf103df7",
  "type": "user",
  "uuid": "531587c8-0164-4dfc-9963-d83436117c07",
  "sourceToolAssistantUUID": "d21ac42f-b098-485b-b73e-45b24846da46",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-28T01:52:47.258Z_

<details><summary>↩ Tool result · `toolu_016fxbeXcr8KEgK5QxQGWwS1`</summary>

```text
Web search results for query: "RL Tango 25.5% relative improvement co-evolve generator verifier arxiv"

Links: [{"title":"RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.15034v2"},{"title":"RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning","url":"https://openreview.net/pdf?id=JRkFZl0TJ2"},{"title":"RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning","url":"https://arxiv.org/html/2505.15034v2"},{"title":"[Quick Review] RL Tango: Reinforcing Generator and Verifier Together for Language\\n Reasoning","url":"https://liner.com/review/rl-tango-reinforcing-generator-and-verifier-together-for-language-reasoning"},{"title":"[2505.15034] RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning","url":"https://arxiv.org/abs/2505.15034"},{"title":"Paper page - RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning","url":"https://huggingface.co/papers/2505.15034"},{"title":"RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning","url":"https://www.researchgate.net/publication/391953673_RL_Tango_Reinforcing_Generator_and_Verifier_Together_for_Language_Reasoning"}]

Based on the search results, I found comprehensive information about RL Tango:

## RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning

TANGO introduces a framework that concurrently trains an LLM generator and a generative, process-level verifier using reinforcement learning.

**Key Results:**
Compared to vanilla RL methods trained only on outcome-level rewards, Tango achieves an average relative improvement of 25.5% on five competition-level math benchmarks and 7.3% on four challenging out-of-domain reasoning tasks, consistently across three RL algorithms.

**Core Innovation:**
A central innovation of Tango is its generative, process-level LLM verifier, which is trained via RL and co-evolves with the generator. Importantly, the verifier is trained solely based on outcome-level verification correctness rewards without requiring explicit process-level annotations.

**Performance:**
The generator attains best-in-class performance across five competition-level math benchmarks and four challenging out-of-domain reasoning tasks, while the verifier leads on the ProcessBench dataset.

The paper is available on arXiv as paper 2505.15034, with code available at GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a250d2a4-35c0-48a2-acb3-da68fbca7139",
  "isSidechain": true,
  "promptId": "bf18714b-0e92-4a91-be0e-dc43bfe729a9",
  "agentId": "af40b24dedf103df7",
  "type": "user",
  "uuid": "c5826543-5cb6-4745-9cf5-fce27f1c50cf",
  "sourceToolAssistantUUID": "a250d2a4-35c0-48a2-acb3-da68fbca7139",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-28T01:52:50.140Z_

Good, I have a solid overview. Now let me fetch the full paper for detailed information on the method, benchmarks, MC estimation, and limitations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5826543-5cb6-4745-9cf5-fce27f1c50cf",
  "isSidechain": true,
  "agentId": "af40b24dedf103df7",
  "requestId": "req_011CbU8ZbsHQXEdBxuxccczM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5dc157c-a0a1-4292-9ec0-777e17c87516",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwoUaVR8Dt7EcBMNukE9yC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2602,
      "cache_read_input_tokens": 10037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2602,
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

_source line 15 · 2026-05-28T01:52:51.540Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018w2vBk9pJtZvaTjuSfKvRy`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.15034",
  "prompt": "Extract the full title, all authors, and the complete abstract of this paper. Also extract any information about the method, benchmarks, and results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5dc157c-a0a1-4292-9ec0-777e17c87516",
  "isSidechain": true,
  "agentId": "af40b24dedf103df7",
  "requestId": "req_011CbU8ZbsHQXEdBxuxccczM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5fe1a60-c795-4ef3-9260-714f3fb74c62",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwoUaVR8Dt7EcBMNukE9yC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2602,
      "cache_read_input_tokens": 10037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2602,
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

_source line 16 · 2026-05-28T01:52:55.818Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019g8ny1fAYGvvPXVjgcTqoj`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.15034v2",
  "prompt": "Extract ALL detailed information about:\n1. The full method description - how does the co-evolution of generator and verifier work? What is the training loop? How does the verifier provide process-level rewards without process-level annotations?\n2. Does the paper use Monte Carlo (MC) estimation anywhere? \n3. How is the generative verifier trained? What rewards does it receive?\n4. What is the interleaved training procedure?\n5. All benchmark names and exact numerical results, especially the 25.5% relative improvement breakdown.\n6. All limitations mentioned in the paper.\n7. How is this relevant to process reward models (PRMs)?\n8. What RL algorithms are used (GRPO, etc.)?\n9. What base models are used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5fe1a60-c795-4ef3-9260-714f3fb74c62",
  "isSidechain": true,
  "agentId": "af40b24dedf103df7",
  "requestId": "req_011CbU8ZbsHQXEdBxuxccczM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebd786df-4612-4eb8-9bfe-8ba502e0b905",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwoUaVR8Dt7EcBMNukE9yC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2602,
      "cache_read_input_tokens": 10037,
      "output_tokens": 378,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2602
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 378,
          "cache_read_input_tokens": 10037,
          "cache_creation_input_tokens": 2602,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2602,
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

_source line 17 · 2026-05-28T01:52:57.120Z_

<details><summary>↩ Tool result · `toolu_018w2vBk9pJtZvaTjuSfKvRy`</summary>

```text
# RL Tango: Paper Summary

## Title
"RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning"

## Authors
Kaiwen Zha, Zhengqi Gao, Maohao Shen, Zhang-Wei Hong, Duane S. Boning, Dina Katabi

## Abstract
The paper proposes Tango, a framework using reinforcement learning to simultaneously train both an LLM generator and verifier in an interleaved manner. The key innovation is a "generative, process-level LLM verifier, which is trained via RL and co-evolves with the generator." Notably, the verifier learns from outcome-level rewards without needing process-level annotations. The authors claim this approach shows "improved robustness and superior generalization compared to deterministic or SFT-trained verifiers."

## Method
- Concurrent RL training of generator and verifier components
- Generative verifier trained through reinforcement learning
- Co-evolutionary approach enabling mutual reinforcement
- Uses outcome-level verification correctness rewards

## Benchmarks Tested
- Five competition-level math benchmarks
- Four challenging out-of-domain reasoning tasks
- ProcessBench dataset

## Key Results
Both components achieve state-of-the-art performance among 7B/8B-scale models. The framework shows "particularly substantial improvements on the most difficult mathematical reasoning problems." Code is available on GitHub.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5fe1a60-c795-4ef3-9260-714f3fb74c62",
  "isSidechain": true,
  "promptId": "bf18714b-0e92-4a91-be0e-dc43bfe729a9",
  "agentId": "af40b24dedf103df7",
  "type": "user",
  "uuid": "431e78da-0266-49d1-8777-40e326b28224",
  "sourceToolAssistantUUID": "a5fe1a60-c795-4ef3-9260-714f3fb74c62",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-28T01:53:14.303Z_

<details><summary>↩ Tool result · `toolu_019g8ny1fAYGvvPXVjgcTqoj`</summary>

```text
# RL Tango: Comprehensive Analysis

## 1. Full Method Description

**Co-evolution Framework:**
The method alternates training an LLM generator and verifier through interleaved RL. The generator produces multi-step solutions while the verifier outputs natural language feedback with step-level assessments and overall correctness judgments. This creates mutual reinforcement where improving one component strengthens the other.

**Training Loop:**
According to the paper, "Tango jointly trains an LLM generator and an LLM verifier via interleaved RL, creating a self-reinforcing loop where each agent iteratively strengthens the other." The system updates the generator for Ng steps, then the verifier for Nv steps (set to 3:1 ratio in experiments).

**Process-Level Rewards Without Annotations:**
The verifier learns through outcome-level correctness signals alone. Crucially, "the verifier is trained exclusively using outcome-level verification correctness rewards, without process-level annotations." Despite this, it progressively learns accurate step-level judgments through RL-based chain-of-thought refinement as the generator evolves.

## 2. Monte Carlo Estimation

The paper does not explicitly employ Monte Carlo estimation as a named technique. However, it uses sampling-based approaches: "the generator policy πg samples a group of M responses" for group-normalized reward calculations within the GRPO algorithm.

## 3. Generative Verifier Training

**Training Mechanism:**
The verifier receives outcome-level rewards based on judgment correctness:
- Correct judgment matching gold answer: +1
- Format compliance score (text-based feedback structure)
- Combined via: "rv,out(𝐨v) = rv,correct(𝐨v) + γ · rv,format(𝐨v)"

**Class Imbalance Handling:**
A critical innovation addresses early-training imbalance when most generator outputs are incorrect. The system applies "class-aware reweighting" with sample-specific scaling factors (s+ and s-) inversely proportional to correct/incorrect sample frequencies, preventing verifier collapse to trivial solutions.

## 4. Interleaved Training Procedure

The algorithm alternates phases:
- **Generator phase (3 steps):** Samples M responses per prompt, queries verifier for evaluations, computes separate outcome-level and step-level advantages, blends them with exponentially decaying weight α
- **Verifier phase (1 step):** Samples verifier responses, extracts final judgments, applies class-aware reweighting, updates via policy gradient

Key detail: "We apply an exponential decay schedule to α, which is essential to Tango's success. Early in training, step-level supervision has a stronger influence...gradually reduced to promote stable convergence."

## 5. Benchmark Results & 25.5% Improvement Breakdown

**Math Benchmarks (5 tasks):**
- MATH-500: 74.6% → 81.4% (GRPO with Tango)
- AIME 2024: 13.3% → 20.0%
- AIME 2025: 10.0% → 20.0% (100% relative gain)
- AMC 2023: 50.0% → 65.0%
- OlympiadBench: 36.9% → 43.9%
- **Average relative improvement: 24.6% (note: paper states 25.5% across multiple RL algorithms)**

**Out-of-Domain Tasks (4 benchmarks):**
- BoardgameQA, CRUXEval, StrategyQA, TableBench
- Average improvement: 6.1% relative gain

**State-of-the-art (7B/8B scale):**
- Math average: 49.5%
- Out-of-domain average: 62.8%

## 6. Limitations Mentioned

The paper does not explicitly dedicate a "Limitations" section. However, implied constraints include:

- Requires careful hyperparameter tuning (α decay schedule, class reweighting coefficients)
- Verifier initially weaker than generator (uses Qwen2.5-7B vs. Qwen2.5-Math-7B)
- Training efficiency gains diminish after 200 generator steps
- Method tested primarily on mathematical reasoning; generalization to other domains unclear
- Computational cost of interleaved training not thoroughly analyzed

## 7. Relevance to Process Reward Models (PRMs)

This work represents a paradigm shift in PRM design. Traditional PRMs are "discriminative, frozen, and deterministic," making them "brittle to distribution shifts and reward hacking." 

Tango's contribution: "ours is the first PRM trained using RL" and "produces stochastic, step-level rewards as textual judgments." The generative approach with sampling introduces stochasticity that "enhances robustness against reward hacking." Notably, the verifier achieves state-of-the-art on ProcessBench despite no step-level supervision.

## 8. RL Algorithms Used

**Primary algorithms tested:**
- **GRPO** (Group-normalized Policy Optimization) - default
- **RLOO** (Leave-One-Out reward averaging)
- **REINFORCE++** (batch-normalized rewards)

The paper demonstrates "Tango is compatible with other RL algorithms," with consistent 24-26% improvements across all three methods.

## 9. Base Models

**Generator:** Qwen2.5-Math-7B (strong mathematical reasoning)

**Verifier:** Qwen2.5-7B (larger context window for question + solution pairs)

**SFT Data:** 113K prompts from Eurus-2-SFT-Data with step-tagged responses

**RL Data:** 455K math question-answer pairs from Eurus-2-RL-Data

**Validation Models:** Also tested with Llama-3.1-8B-Instruct, demonstrating cross-architecture generalization
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebd786df-4612-4eb8-9bfe-8ba502e0b905",
  "isSidechain": true,
  "promptId": "bf18714b-0e92-4a91-be0e-dc43bfe729a9",
  "agentId": "af40b24dedf103df7",
  "type": "user",
  "uuid": "b3bc2396-a085-44d5-8b35-1694008bbea6",
  "sourceToolAssistantUUID": "ebd786df-4612-4eb8-9bfe-8ba502e0b905",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-28T01:53:18.072Z_

Excellent, I have very detailed information. Let me also fetch the review page to check for any additional limitations or criticisms, and the Moonlight review for any additional analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3bc2396-a085-44d5-8b35-1694008bbea6",
  "isSidechain": true,
  "agentId": "af40b24dedf103df7",
  "requestId": "req_011CbU8bbWGBUdGAnFWKnVtv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1eb1e770-e333-4c9e-9474-e797a1ec688a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176KLXMaqNVgFwRqsRtdzB9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2162,
      "cache_read_input_tokens": 12639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2162,
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

_source line 20 · 2026-05-28T01:53:20.913Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01S6k2wmuodMMCaSViiDCCtX`</summary>

```json
{
  "url": "https://www.themoonlight.io/en/review/rl-tango-reinforcing-generator-and-verifier-together-for-language-reasoning",
  "prompt": "Extract all information about limitations, weaknesses, criticisms, and any details about MC estimation or process reward model relevance. Also extract any additional method details not covered in the arxiv page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1eb1e770-e333-4c9e-9474-e797a1ec688a",
  "isSidechain": true,
  "agentId": "af40b24dedf103df7",
  "requestId": "req_011CbU8bbWGBUdGAnFWKnVtv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0aefbea-95ca-47d4-bfd8-f92abba1c433",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176KLXMaqNVgFwRqsRtdzB9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2162,
      "cache_read_input_tokens": 12639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2162,
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

_source line 21 · 2026-05-28T01:53:22.210Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FMZYDiyR1zLbjutdNChr4E`</summary>

```json
{
  "url": "https://openreview.net/forum?id=JRkFZl0TJ2",
  "prompt": "Extract all reviewer comments, criticisms, weaknesses, and limitations mentioned by reviewers. Also extract the paper's official scores/ratings if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0aefbea-95ca-47d4-bfd8-f92abba1c433",
  "isSidechain": true,
  "agentId": "af40b24dedf103df7",
  "requestId": "req_011CbU8bbWGBUdGAnFWKnVtv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0909af52-670b-4b43-b9c8-9ffd704fda5e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176KLXMaqNVgFwRqsRtdzB9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2162,
      "cache_read_input_tokens": 12639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2162,
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

_source line 22 · 2026-05-28T01:53:25.679Z_

<details><summary>↩ Tool result · `toolu_01FMZYDiyR1zLbjutdNChr4E`</summary>

```text
# RL Tango - Reviewer Comments and Ratings

Based on the provided webpage content, **no reviewer comments, criticisms, weaknesses, or official scores/ratings are available**. 

The page displays only the paper's abstract and metadata from OpenReview, including:
- Publication date (18 Sept 2025)
- Keywords and primary research area
- Author information
- A brief summary of the proposed Tango framework

To access reviewer feedback and ratings, you would need to visit the full OpenReview page for this submission (ID: 9763), which typically includes dedicated sections for official reviews once the peer review process is complete and results are published.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0909af52-670b-4b43-b9c8-9ffd704fda5e",
  "isSidechain": true,
  "promptId": "bf18714b-0e92-4a91-be0e-dc43bfe729a9",
  "agentId": "af40b24dedf103df7",
  "type": "user",
  "uuid": "23bf534e-b2e6-4b43-8892-024d03b5d7d4",
  "sourceToolAssistantUUID": "0909af52-670b-4b43-b9c8-9ffd704fda5e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-28T01:53:54.440Z_

<details><summary>↩ Tool result · `toolu_01S6k2wmuodMMCaSViiDCCtX`</summary>

```text
# TANGO Framework: Limitations, Weaknesses, and Method Details

## Limitations and Weaknesses

The webpage does not explicitly discuss limitations or weaknesses of the TANGO approach. However, one implicit challenge is identified:

**Class Imbalance Problem:** The content notes that "initially, most generator outputs are incorrect," creating a class imbalance issue. The framework addresses this through class-aware reweighting rather than acknowledging it as an unresolved limitation.

## MC Estimation and Process Reward Models

**No Monte Carlo Estimation Details:** The document does not discuss Monte Carlo estimation methods explicitly.

**Process Reward Model (PRM) Relevance:** TANGO is positioned as an alternative to existing PRM approaches. The text states comparisons show TANGO "substantially outperforms ORM- and PRM-based baselines like PRIME." The key differentiation is that TANGO's verifier is "RL-trained" rather than using "fixed, rule-based, or discriminative verifiers trained via supervised fine-tuning."

## Additional Method Details

1. **Verifier Training Signal:** The verifier is "trained solely on outcome-level verification correctness rewards, without requiring explicit process-level annotations"—a significant methodological distinction.

2. **Advantage Calculation:** Generator advantages blend outcome and step-level rewards using a weighted parameter α that is "annealed during training."

3. **Generative Feedback:** The verifier provides "natural language feedback, including step-level assessments and an overall correctness judgment," operating through sampling rather than deterministic prediction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0aefbea-95ca-47d4-bfd8-f92abba1c433",
  "isSidechain": true,
  "promptId": "bf18714b-0e92-4a91-be0e-dc43bfe729a9",
  "agentId": "af40b24dedf103df7",
  "type": "user",
  "uuid": "d8188f7f-df4f-4384-9fb3-6857b47be3fa",
  "sourceToolAssistantUUID": "b0aefbea-95ca-47d4-bfd8-f92abba1c433",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-28T01:54:50.162Z_

Now I have comprehensive information to provide a detailed analysis. Here is the full breakdown of the RL Tango paper:

---

## RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning

### 1. Full Title and Authors

**Title:** "RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning"

**Authors:** Kaiwen Zha, Zhengqi Gao, Maohao Shen, Zhang-Wei Hong, Duane S. Boning, Dina Katabi (MIT)

**Venue:** NeurIPS 2025 (Poster). ArXiv: 2505.15034. Code: https://github.com/kaiwenzha/rl-tango

---

### 2. Exact Method: How Generator and Verifier Co-Evolve

The core idea is **interleaved RL training** of two LLMs -- a generator and a generative verifier -- that mutually reinforce each other:

**Generator phase (N_g = 3 steps per round):**
- The generator (initialized from Qwen2.5-Math-7B) samples M responses per prompt.
- The co-evolving verifier evaluates each response, producing **natural language feedback** with step-level assessments and an overall correctness judgment.
- The generator's advantage function blends two signals:
  - **Outcome-level advantage** (from gold answer correctness, standard in GRPO/REINFORCE)
  - **Step-level advantage** (from the verifier's per-step judgments)
- These are blended via a weight alpha with an **exponential decay schedule**: early in training, the step-level signal from the verifier dominates (bootstrapping the generator); later, it is reduced to promote stable convergence and avoid over-reliance on a still-imperfect verifier.

**Verifier phase (N_v = 1 step per round):**
- The verifier (initialized from Qwen2.5-7B, a general-purpose model, not math-specialized) generates verification responses for the generator's current outputs.
- It is rewarded based on **outcome-level verification correctness only**: does its final judgment (correct/incorrect) match the gold label? The reward is r_v = r_correct + gamma * r_format.
- Crucially, **no process-level (step-level) annotations are ever provided to the verifier**. Despite this, the verifier progressively learns accurate step-level judgments through RL-based chain-of-thought refinement.

**Class-aware reweighting:** Early in training, most generator outputs are wrong, creating severe class imbalance. Tango applies class-aware reweighting with scaling factors inversely proportional to correct/incorrect sample frequencies to prevent the verifier from collapsing to trivially predicting "incorrect" for everything.

The alternating 3:1 ratio (generator:verifier steps) creates the "tango" -- a self-reinforcing loop where a better generator produces harder, more diverse solutions that challenge the verifier, and a better verifier provides more accurate step-level guidance that improves the generator.

---

### 3. Benchmarks and Results

**The 25.5% relative improvement** is averaged across **five competition-level math benchmarks**, consistently observed across three different RL algorithms (GRPO, RLOO, REINFORCE++):

| Benchmark | Vanilla GRPO | GRPO + Tango |
|-----------|-------------|--------------|
| MATH-500 | 74.6% | 81.4% |
| AIME 2024 | 13.3% | 20.0% |
| AIME 2025 | 10.0% | 20.0% |
| AMC 2023 | 50.0% | 65.0% |
| OlympiadBench | 36.9% | 43.9% |

**Out-of-domain reasoning tasks (4 benchmarks):** 7.3% average relative improvement on BoardgameQA, CRUXEval, StrategyQA, and TableBench.

**Verifier results:** State-of-the-art on ProcessBench (a benchmark for evaluating process-level verification) despite never being trained with process-level labels.

**Scale:** All results at 7B/8B parameter scale. The generator achieves best-in-class among comparable models. The method was also validated with Llama-3.1-8B-Instruct, demonstrating cross-architecture generalizability.

---

### 4. Monte Carlo Estimation and Process-Level Labels

**MC estimation:** The paper does **not** explicitly use Monte Carlo estimation as a named technique for estimating step-level rewards (unlike MC-based PRM approaches such as Math-Shepherd or PRIME). However, it does use sampling-based approaches inherent to GRPO -- the generator samples a group of M responses, and rewards are group-normalized. The verifier itself also uses **sampling** (stochastic generation) rather than deterministic scoring, which introduces beneficial stochasticity.

**Process-level labels:** The paper **does not require any process-level (step-level) annotations**. This is a central contribution. The verifier is trained purely on outcome-level correctness rewards (does the final judgment match the gold answer?). Despite this, it emergently learns to produce accurate step-level assessments through RL-driven chain-of-thought refinement. This is in contrast to traditional PRMs that require expensive human-annotated or MC-estimated step-level labels.

---

### 5. Relevance to Training Process Reward Models

This paper is **directly and highly relevant** to PRM research:

- **First RL-trained PRM:** The authors claim theirs is the first process reward model trained using RL (rather than SFT on human or MC-estimated labels).
- **Generative vs. discriminative:** Traditional PRMs are discriminative (predict a score per step) and deterministic. Tango's verifier is **generative** (produces natural language verification with reasoning) and **stochastic** (samples multiple verification responses). The stochasticity makes it inherently more robust to reward hacking.
- **No step-level annotations needed:** This eliminates the expensive data collection bottleneck of traditional PRMs (human annotation or MC rollout estimation).
- **Co-evolution prevents distribution shift:** Fixed/frozen PRMs suffer from distribution shift as the generator policy evolves during training. Co-evolving the verifier with the generator keeps the verifier calibrated to the current policy's output distribution.
- **Outperforms PRM baselines:** Tango substantially outperforms ORM- and PRM-based baselines like PRIME on the benchmarks tested.
- **State-of-the-art on ProcessBench:** Despite no step-level supervision, the verifier achieves leading results on a benchmark specifically designed to test process-level verification quality.

---

### 6. Limitations

The paper does not include an explicit "Limitations" section. The following limitations can be inferred:

1. **Hyperparameter sensitivity:** The method requires careful tuning of the alpha decay schedule, class reweighting coefficients (s+, s-), the generator-to-verifier step ratio (N_g:N_v), and the format reward weight gamma. The exponential decay of alpha is described as "essential to Tango's success."

2. **Compute cost:** Interleaved training of two LLMs is inherently more expensive than training one. The computational overhead of the co-training procedure is not thoroughly analyzed.

3. **Domain scope:** The method is evaluated primarily on mathematical reasoning. Generalization to other reasoning domains (coding, commonsense, scientific reasoning) beyond the four OOD benchmarks is not extensively explored.

4. **Verifier initialization gap:** The verifier uses a weaker base model (general Qwen2.5-7B) than the generator (math-specialized Qwen2.5-Math-7B), and is initially much weaker. The class imbalance handling and alpha decay schedule are engineering solutions to this cold-start problem.

5. **Diminishing returns:** Training efficiency gains reportedly diminish after approximately 200 generator steps.

6. **Scale:** Only validated at 7B/8B scale. Behavior at larger scales (70B+) is unknown.

7. **SFT warmup dependency:** Both generator and verifier require SFT warmup (on 113K prompts from Eurus-2-SFT-Data) before RL training begins, so the method is not purely RL.

---

Sources:
- [RL Tango on arXiv](https://arxiv.org/abs/2505.15034)
- [RL Tango HTML version](https://arxiv.org/html/2505.15034v2)
- [RL Tango on OpenReview (NeurIPS 2025)](https://openreview.net/forum?id=JRkFZl0TJ2)
- [NeurIPS 2025 Poster page](https://neurips.cc/virtual/2025/poster/118724)
- [RL Tango on Semantic Scholar](https://www.semanticscholar.org/paper/RL-Tango:-Reinforcing-Generator-and-Verifier-for-Zha-Gao/5becc8d0a5066c58d2785798519f2cddad7f4482)
- [RL Tango Literature Review (Moonlight)](https://www.themoonlight.io/en/review/rl-tango-reinforcing-generator-and-verifier-together-for-language-reasoning)
- [RL Tango on Hugging Face Papers](https://huggingface.co/papers/2505.15034)
- [RL Tango on alphaXiv](https://www.alphaxiv.org/overview/2505.15034v2)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8188f7f-df4f-4384-9fb3-6857b47be3fa",
  "isSidechain": true,
  "agentId": "af40b24dedf103df7",
  "requestId": "req_011CbU8eZ7Unkf2TohPsZTun",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d2b1cf0-c8b7-4736-93f9-435536d4e67b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y6t4BLQUdPh5k8fEBtGueN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 174,
      "cache_creation_input_tokens": 663,
      "cache_read_input_tokens": 14801,
      "output_tokens": 2330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 663
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 174,
          "output_tokens": 2330,
          "cache_read_input_tokens": 14801,
          "cache_creation_input_tokens": 663,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 663,
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
