# Research conversation: I need to deeply research GSPO (Group Sequence Policy Optimization), arXiv:2507.18071, July 2025. This was developed by 

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-acd6bd3eff75572c3.jsonl`
- **Structured JSON:** [`a171a67c060d4b93806f.json`](../../sessions/a1/a171a67c060d4b93806f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

49 recorded events

### User

_source line 1 · 2026-05-27T23:04:44.234Z_

I need to deeply research GSPO (Group Sequence Policy Optimization), arXiv:2507.18071, July 2025. This was developed by the Qwen team specifically because GRPO fails on MoE (Mixture-of-Experts) models like Qwen3-30B-A3B.

Please:
1. Search the web for "GSPO Group Sequence Policy Optimization arXiv 2507.18071" and related queries
2. Fetch the arXiv abstract page at https://arxiv.org/abs/2507.18071
3. Search for "GSPO MoE GRPO Qwen sequence-level importance ratio"
4. Search for any blog posts or discussions about GSPO vs GRPO for MoE models
5. Try to fetch the paper PDF or HTML version to get more details about the algorithm

Key questions I need answered:
- What exactly is GSPO's mechanism? (sequence-level vs token-level importance ratios)
- Why does it solve the MoE routing instability problem?
- How does it interact with multi-objective/multi-component rewards?
- Does GSPO use sequence-level clipping? If so, can per-component reward signals still be extracted?
- What were the specific experimental results showing GSPO > GRPO on MoE?
- Is there any discussion of GSPO with composite/multi-objective rewards?

Please be thorough - read actual paper content, not just abstracts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "acd6bd3eff75572c3",
  "type": "user",
  "uuid": "cca102fe-b607-44cd-be53-27aa00d38621",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-27T23:04:44.237Z_

```json
{
  "parentUuid": "cca102fe-b607-44cd-be53-27aa00d38621",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
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
  "uuid": "b77dc85b-919a-4594-8318-8731f655adc9",
  "timestamp": "2026-05-27T23:04:44.237Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-27T23:04:44.238Z_

```json
{
  "parentUuid": "b77dc85b-919a-4594-8318-8731f655adc9",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f484d9df-7a9b-40a7-8004-a1198bb540a1",
  "timestamp": "2026-05-27T23:04:44.238Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-27T23:04:46.898Z_



I'll conduct a thorough research on GSPO. Let me start by searching the web and fetching the arXiv page in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f484d9df-7a9b-40a7-8004-a1198bb540a1",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTukLengur9r9aYfsrnS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f9bd121-15a9-415a-a99d-774a9561dce9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PbMUxSmwpNxE8zKT9yuqU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9080,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9080,
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

_source line 5 · 2026-05-27T23:04:47.131Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TYrYXCs9hPTGkXLUfEjXV1`</summary>

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
  "parentUuid": "5f9bd121-15a9-415a-a99d-774a9561dce9",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTukLengur9r9aYfsrnS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f15049af-02c1-4c8e-a911-8791b2f78d8f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PbMUxSmwpNxE8zKT9yuqU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9080,
      "cache_read_input_tokens": 0,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9080
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 111,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9080,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9080,
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

_source line 6 · 2026-05-27T23:04:47.135Z_

<details><summary>↩ Tool result · `toolu_01TYrYXCs9hPTGkXLUfEjXV1`</summary>

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
  "parentUuid": "f15049af-02c1-4c8e-a911-8791b2f78d8f",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "acd6bd3eff75572c3",
  "type": "user",
  "uuid": "e8ead5e6-9a7c-4dfb-82a8-e7b54a96369b",
  "sourceToolAssistantUUID": "f15049af-02c1-4c8e-a911-8791b2f78d8f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-27T23:04:50.003Z_



Now let me run all the initial searches and fetches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8ead5e6-9a7c-4dfb-82a8-e7b54a96369b",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTukZM2CPxFSEDzz4cr8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d800ca09-b98a-4a36-b180-9fc08b67d590",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzDXEQCwVpSNzWX31HwEam",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 9080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1133,
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

_source line 8 · 2026-05-27T23:04:50.004Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SFrhhVTbLyc9Gj3mKJyu7p`</summary>

```json
{
  "query": "GSPO Group Sequence Policy Optimization arXiv 2507.18071"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d800ca09-b98a-4a36-b180-9fc08b67d590",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTukZM2CPxFSEDzz4cr8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b43bddb-020a-42a3-91c3-23689360f41b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzDXEQCwVpSNzWX31HwEam",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 9080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1133,
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

_source line 9 · 2026-05-27T23:04:50.479Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BC8jgJFtHizVCgUcsu8tLm`</summary>

```json
{
  "query": "GSPO MoE GRPO Qwen sequence-level importance ratio"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b43bddb-020a-42a3-91c3-23689360f41b",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTukZM2CPxFSEDzz4cr8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c5337ad-1751-4315-bf6c-5196405d8aa0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzDXEQCwVpSNzWX31HwEam",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 9080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1133,
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

_source line 10 · 2026-05-27T23:04:51.006Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RSjRkqUb6YD62a48b6qoff`</summary>

```json
{
  "query": "GSPO vs GRPO MoE models blog discussion 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c5337ad-1751-4315-bf6c-5196405d8aa0",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTukZM2CPxFSEDzz4cr8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58156139-d919-4a30-951e-cbf7cbf71aad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzDXEQCwVpSNzWX31HwEam",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 9080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1133,
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

_source line 11 · 2026-05-27T23:04:52.012Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0153cMCjMx2AqFFmuDj4iByF`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.18071",
  "prompt": "Extract the full abstract, title, authors, and all details about the GSPO paper. Include the complete abstract text, submission date, and any other metadata visible on the page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58156139-d919-4a30-951e-cbf7cbf71aad",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTukZM2CPxFSEDzz4cr8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01dd8ba1-0a05-4f6e-9586-dd3261210b44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzDXEQCwVpSNzWX31HwEam",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 9080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1133,
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

_source line 12 · 2026-05-27T23:04:54.592Z_

<details><summary>↩ Tool result · `toolu_01SFrhhVTbLyc9Gj3mKJyu7p`</summary>

```text
Web search results for query: "GSPO Group Sequence Policy Optimization arXiv 2507.18071"

Links: [{"title":"[2507.18071] Group Sequence Policy Optimization","url":"https://arxiv.org/abs/2507.18071"},{"title":"[2507.18071v2] Group Sequence Policy Optimization","url":"https://arxiv.org/abs/2507.18071v2"},{"title":"Paper page - Group Sequence Policy Optimization","url":"https://huggingface.co/papers/2507.18071"},{"title":"Group Sequence Policy Optimization","url":"https://arxiv.org/html/2507.18071v2"},{"title":"Group Sequence Policy Optimization (arXiv:2507.18071v2) - ScienceStack","url":"https://www.sciencestack.ai/paper/2507.18071v2"},{"title":"Group Sequence Policy Optimization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/group-sequence-policy-optimization"},{"title":"2025-07-29 Group Sequence Policy Optimization Chujie Zheng∗ Shixuan Liu","url":"https://arxiv.org/pdf/2507.18071"},{"title":"Group Sequence Policy Optimization for Stable RL","url":"https://www.emergentmind.com/papers/2507.18071"},{"title":"Group Sequence Policy Optimization - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250718071Z/abstract"},{"title":"GSPO: Towards Scalable Reinforcement Learning for Language Models | Qwen","url":"https://qwenlm.github.io/blog/gspo/"}]

I found comprehensive information about the paper. Here's what the search revealed:

## Overview

Group Sequence Policy Optimization (GSPO) is a stable, efficient, and performant reinforcement learning algorithm for training large language models.

## Key Innovation

Unlike previous algorithms that adopt token-level importance ratios, GSPO defines the importance ratio based on sequence likelihood and performs sequence-level clipping, rewarding, and optimization.

## Performance and Applications

GSPO achieves superior training efficiency and performance compared to the GRPO algorithm, notably stabilizes Mixture-of-Experts (MoE) RL training, and has the potential for simplifying the design of RL infrastructure. These merits of GSPO have contributed to the remarkable improvements in the latest Qwen3 models.

## Publication Details

The paper was submitted on July 24, 2025 and last revised on July 28, 2025, with authors from the Qwen Team at Alibaba Inc, led by Chujie Zheng.

The paper is available at: https://arxiv.org/abs/2507.18071


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b43bddb-020a-42a3-91c3-23689360f41b",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "acd6bd3eff75572c3",
  "type": "user",
  "uuid": "dccb3632-54cf-41c0-84f1-6afacd211191",
  "sourceToolAssistantUUID": "6b43bddb-020a-42a3-91c3-23689360f41b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-27T23:04:57.019Z_

<details><summary>↩ Tool result · `toolu_0153cMCjMx2AqFFmuDj4iByF`</summary>

```text
# Group Sequence Policy Optimization (GSPO) - Paper Details

**Title:** Group Sequence Policy Optimization

**arXiv Identifier:** 2507.18071 (cs.LG)

**Submission Dates:**
- Version 1: July 24, 2025
- Version 2 (current): July 28, 2025

**Authors:** Chujie Zheng, Shixuan Liu, Mingze Li, Xiong-Hui Chen, Bowen Yu, Chang Gao, Kai Dang, Yuqiong Liu, Rui Men, An Yang, Jingren Zhou, and Junyang Lin

**Abstract Summary:**
The paper presents GSPO, a reinforcement learning algorithm designed for training large language models. Rather than utilizing token-level importance ratios as prior approaches do, this method "defines the importance ratio based on sequence likelihood and performs sequence-level clipping, rewarding, and optimization." The authors report achieving improved training efficiency and performance relative to GRPO, enhanced stability in Mixture-of-Experts training, and potential infrastructure simplification benefits. These advancements contributed to improvements in Qwen3 models.

**Subject Categories:** Machine Learning (cs.LG), Artificial Intelligence (cs.AI), Computation and Language (cs.CL)

**DOI:** https://doi.org/10.48550/arXiv.2507.18071
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01dd8ba1-0a05-4f6e-9586-dd3261210b44",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "acd6bd3eff75572c3",
  "type": "user",
  "uuid": "a1effab6-05d9-4c96-a450-269acd8b60aa",
  "sourceToolAssistantUUID": "01dd8ba1-0a05-4f6e-9586-dd3261210b44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-27T23:04:58.692Z_

<details><summary>↩ Tool result · `toolu_01BC8jgJFtHizVCgUcsu8tLm`</summary>

```text
Web search results for query: "GSPO MoE GRPO Qwen sequence-level importance ratio"

Links: [{"title":"GRPO++: Tricks for Making RL Actually Work","url":"https://cameronrwolfe.substack.com/p/grpo-tricks"},{"title":"GSPO: Towards Scalable Reinforcement Learning for Language Models | Qwen","url":"https://qwenlm.github.io/blog/gspo/"},{"title":"[2507.18071] Group Sequence Policy Optimization","url":"https://arxiv.org/abs/2507.18071"},{"title":"2025-07-29 Group Sequence Policy Optimization Chujie Zheng∗ Shixuan Liu","url":"https://arxiv.org/pdf/2507.18071"},{"title":"Paper Review: Group Sequence Policy Optimization – Andrey Lukyanenko","url":"https://andlukyane.com/blog/paper-review-gspo"},{"title":"Paper Review: Group Sequence Policy Optimization | by Andrew Lukyanenko | Medium","url":"https://artgor.medium.com/paper-review-group-sequence-policy-optimization-543c3526c240"},{"title":"Towards Stable and Effective Reinforcement Learning for Mixture-of-Experts","url":"https://www.arxiv.org/pdf/2510.23027"},{"title":"What is GSPO ? The RL algorithm used to train Qwen3 | by Mehul Gupta | Data Science in Your Pocket | Medium","url":"https://medium.com/data-science-in-your-pocket/what-is-gspo-the-rl-algorithm-used-to-train-qwen3-506d56ff49e6"},{"title":"Orchestrating Tokens and Sequences: Dynamic Hybrid Policy Optimization for RLVR","url":"https://arxiv.org/pdf/2601.05607"}]

Based on the search results, here's information about GSPO, MoE, GRPO, Qwen, and sequence-level importance ratio:

## Overview

Group Sequence Policy Optimization (GSPO) is a stable, efficient, and performant reinforcement learning algorithm for training large language models. These merits of GSPO have contributed to the remarkable improvements in the latest Qwen3 models.

## Sequence-Level Importance Ratio

The key distinction of GSPO is how it handles importance ratios. Unlike previous algorithms that adopt token-level importance ratios, GSPO defines the importance ratio based on sequence likelihood and performs sequence-level clipping, rewarding, and optimization. The importance ratio in GSPO is defined based on sequence likelihood, where length normalization is performed to reduce variance and unify the numerical range.

## Advantages for MoE Models

The stability of GSPO is found to be especially useful when training large MoE models, such as Qwen3-235B-A22B. With the 48-layer Qwen3-30B-A3B-Base model, after each RL gradient update and for the same rollout sample, there are roughly 10% of the experts activated under the new policy that are different from those under the old policy. GSPO avoids training instability by relying on sequence-level likelihood, which is stable and unaffected by expert routing changes at the token level, making GSPO inherently robust to expert-activation volatility and removing the need for Routing Replay.

## Performance and Efficiency

GSPO demonstrates significantly higher training efficiency than GRPO, achieving better performance under the same training cost.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c5337ad-1751-4315-bf6c-5196405d8aa0",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "acd6bd3eff75572c3",
  "type": "user",
  "uuid": "69b87773-6799-444e-bb36-76509e0305c8",
  "sourceToolAssistantUUID": "2c5337ad-1751-4315-bf6c-5196405d8aa0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-27T23:04:59.329Z_

<details><summary>↩ Tool result · `toolu_01RSjRkqUb6YD62a48b6qoff`</summary>

```text
Web search results for query: "GSPO vs GRPO MoE models blog discussion 2025"

Links: [{"title":"GSPO: Towards Scalable Reinforcement Learning for Language Models | Qwen","url":"https://qwenlm.github.io/blog/gspo/"},{"title":"Group Sequence Policy Optimization (GSPO); A Smarter Approach to RL for LLMs and MoE Models | Tolgahan Cakaloglu","url":"https://tolga-han.com/blog/2025/group-sequence-policy-optimization-gspo.md/"},{"title":"GSPO vs GRPO: Reinforcement Learning for MoE Models","url":"https://kaitchup.substack.com/p/gspo-vs-grpo-reinforcement-learning"},{"title":"Alibaba Introduces Group Sequence Policy Optimization (GSPO): An Efficient Reinforcement Learning Algorithm that Powers the Qwen3 Models - MarkTechPost","url":"https://www.marktechpost.com/2025/08/07/alibaba-introduces-group-sequence-policy-optimization-gspo-an-efficient-reinforcement-learning-algorithm-that-powers-the-qwen3-models/"},{"title":"What is GSPO ? The RL algorithm used to train Qwen3 | by Mehul Gupta | Data Science in Your Pocket | Medium","url":"https://medium.com/data-science-in-your-pocket/what-is-gspo-the-rl-algorithm-used-to-train-qwen3-506d56ff49e6"},{"title":"RLHF Algorithms: PPO, GRPO, GSPO — Differences, Trade-offs, and Use Cases | by Hongjian | Medium","url":"https://medium.com/@hongjianzou/rlhf-algorithms-ppo-grpo-gspo-differences-trade-offs-and-use-cases-241d003d806d"},{"title":"From GRPO to DAPO and GSPO: What, Why and How [En/中] - 张逸骅的博客 | Yihua's Blog","url":"https://normaluhr.github.io/2025/08/08/GRPO_DAPO_GSPO/"},{"title":"Paper Review: Group Sequence Policy Optimization – Andrey Lukyanenko","url":"https://andlukyane.com/blog/paper-review-gspo"},{"title":"From GRPO to DAPO and GSPO: What, Why, and How","url":"https://huggingface.co/blog/NormalUhr/grpo-to-dapo-and-gspo"},{"title":"Group Sequence Policy Optimization","url":"https://arxiv.org/pdf/2507.18071"}]

I found several excellent blog discussions and resources comparing GSPO and GRPO MoE models from 2025. Here's a summary of the key findings:

## Overview

The Qwen team unveiled a new reinforcement learning method called Group Sequence Policy Optimization (GSPO) that demonstrates notably superior training stability, efficiency, and performance, especially for MoE models compared to GRPO, the RL techniques popularized by the DeepSeek Models.

## Key Differences

**Optimization Approach:**
GSPO aligns the objective with how rewards are provided in RLHF by moving from token-level to sequence-level optimization. Instead of focusing on individual tokens, it evaluates and rewards the entire generated sequence, shifting from "is this a good next word?" to "is this a good overall response?"

**MoE Training Advantages:**
GSPO offers significant advantages for MoE training by stabilizing the process through consistent expert activations across gradient updates, unlike GRPO, which struggles with expert-activation volatility. GRPO necessitates the Routing Replay training strategy for the normal convergence of MoE RL, while GSPO has obviated the need for this strategy.

## Performance Results

GSPO demonstrates significantly higher training efficiency than GRPO, achieving better performance under the same training cost. GSPO showed stable training, consistent performance gains with more compute and longer generations, and better efficiency than GRPO under the same conditions.

Several blogs from July-August 2025 covered this comparison, including discussions on Qwen's official blog, Medium articles, and dedicated blog posts examining the technical details and practical implications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58156139-d919-4a30-951e-cbf7cbf71aad",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "acd6bd3eff75572c3",
  "type": "user",
  "uuid": "c187036a-d3ad-4122-af76-94226c0482a9",
  "sourceToolAssistantUUID": "58156139-d919-4a30-951e-cbf7cbf71aad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-27T23:05:03.282Z_

Good, I have a solid overview. Now let me fetch the detailed content from the paper HTML version and the Qwen blog post, plus some of the review articles.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c187036a-d3ad-4122-af76-94226c0482a9",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTumTxbsbVwLpycjh5zf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c681136b-2f29-40e8-af3c-3b276ac83869",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kq7jisbgSBN52r8uu7AGVb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 354,
      "cache_creation_input_tokens": 2975,
      "cache_read_input_tokens": 10213,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2975,
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

_source line 17 · 2026-05-27T23:05:07.763Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01F6uUJsVoaM8XBYaFewm6s3`</summary>

```json
{
  "url": "https://arxiv.org/html/2507.18071v2",
  "prompt": "Extract the COMPLETE technical details of the GSPO algorithm. I need:\n1. The exact mathematical formulation of GSPO - all equations, especially the sequence-level importance ratio formula, the clipping mechanism, and the loss function\n2. The detailed explanation of WHY token-level importance ratios cause problems for MoE models (expert routing instability)\n3. The specific experimental results comparing GSPO vs GRPO, including benchmark numbers\n4. Any discussion of multi-objective or multi-component rewards\n5. Details about length normalization\n6. The relationship between sequence-level clipping and reward signals\n7. Any discussion about how GSPO handles different reward types or composite rewards\n8. The specific findings about Qwen3-30B-A3B routing instability statistics\nPlease be as detailed and complete as possible, including all mathematical notation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c681136b-2f29-40e8-af3c-3b276ac83869",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTumTxbsbVwLpycjh5zf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88c7cae0-1339-4586-b7b3-736c9fa80984",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kq7jisbgSBN52r8uu7AGVb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 354,
      "cache_creation_input_tokens": 2975,
      "cache_read_input_tokens": 10213,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2975,
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

_source line 18 · 2026-05-27T23:05:09.975Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012qia7JkgTKdQSdTKxH2p5o`</summary>

```json
{
  "url": "https://qwenlm.github.io/blog/gspo/",
  "prompt": "Extract ALL technical details from this blog post about GSPO. I need:\n1. The complete mathematical formulation and equations\n2. Explanation of sequence-level vs token-level importance ratios\n3. Why GSPO helps with MoE training stability\n4. Experimental results and benchmarks\n5. Any discussion of multi-objective rewards or composite reward signals\n6. Details about the clipping mechanism\n7. Training infrastructure simplifications\n8. Comparison with GRPO\nPlease be extremely thorough and include all equations and technical details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88c7cae0-1339-4586-b7b3-736c9fa80984",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTumTxbsbVwLpycjh5zf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49e5674c-f586-438f-bf95-d356a2985f3d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kq7jisbgSBN52r8uu7AGVb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 354,
      "cache_creation_input_tokens": 2975,
      "cache_read_input_tokens": 10213,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2975,
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

_source line 19 · 2026-05-27T23:05:11.773Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VP7L5cr6i6VfkhNJupnu3K`</summary>

```json
{
  "url": "https://andlukyane.com/blog/paper-review-gspo",
  "prompt": "Extract all technical details from this paper review about GSPO. Include the mathematical formulations, key insights about sequence-level vs token-level optimization, MoE stability findings, experimental results, and any analysis or commentary about the algorithm's strengths and limitations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49e5674c-f586-438f-bf95-d356a2985f3d",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTumTxbsbVwLpycjh5zf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75905f95-245b-4675-8b74-23fad3747cd8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kq7jisbgSBN52r8uu7AGVb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 354,
      "cache_creation_input_tokens": 2975,
      "cache_read_input_tokens": 10213,
      "output_tokens": 611,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2975
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 354,
          "output_tokens": 611,
          "cache_read_input_tokens": 10213,
          "cache_creation_input_tokens": 2975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2975,
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

_source line 20 · 2026-05-27T23:05:17.485Z_

<details><summary>↩ Tool result · `toolu_012qia7JkgTKdQSdTKxH2p5o`</summary>

```text
# GSPO Technical Details Summary

## 1. Mathematical Formulation

The core optimization objective is:

$$\mathcal{J}_\text{GSPO}(\theta) = \mathbb{E}_{x \sim \mathcal{D}, \{y_i\}_{i=1}^G} \left[\frac{1}{G} \sum_{i=1}^{G} \min(s_i(\theta)\widehat{A}_i, \text{clip}(s_i(\theta), 1-\varepsilon, 1+\varepsilon)\widehat{A}_i)\right]$$

The sequence-level importance ratio uses length normalization:

$$s_i(\theta) = \left(\frac{\pi_\theta(y_i|x)}{\pi_{\theta_\text{old}}(y_i|x)}\right)^{1/|y_i|} = \exp\left(\frac{1}{|y_i|}\sum_{t=1}^{|y_i|}\log\frac{\pi_\theta(y_{i,t}|x,y_{i,<t})}{\pi_{\theta_\text{old}}(y_{i,t}|x,y_{i,<t})}\right)$$

## 2. Sequence vs. Token-Level Ratios

GSPO operates on "sequence likelihood" rather than individual token probabilities. This distinction proves critical: the algorithm "only focuses on sequence-level likelihood" and demonstrates reduced "sensitivity to individual token likelihood." This makes the approach "much more tolerant of precision discrepancies."

## 3. MoE Training Stability

GRPO requires the Routing Replay strategy—caching and replaying expert routing patterns—to prevent convergence failures caused by "expert activation volatility." GSPO "completely eliminates the dependency on Routing Replay" since it ignores token-level variations, removing "infrastructure-heavy workarounds" while allowing models to maximize capacity.

## 4. Experimental Results

Testing on a Qwen3-30B model measured performance via AIME'24, LiveCodeBench, and CodeForces benchmarks. Results show GSPO achieves "significantly higher training efficiency" than GRPO with "better performance under the same training cost" and demonstrates "continuous performance improvement through increasing training compute."

## 5. Clipping Mechanism

The algorithm employs sequence-level clipping with ratio $s_i(\theta)$ constrained to $[1-\varepsilon, 1+\varepsilon]$. Notably, "the fraction of tokens clipped in GSPO is two orders of magnitude higher than that in GRPO," yet efficiency remains superior, suggesting "GRPO's token-level optimization objective is noisy and inefficient."

## 6. Infrastructure Benefits

GSPO enables "directly use likelihoods returned by inference engines for optimization, eliminating the need for recomputation with training engines," benefiting partial rollout and disaggregated frameworks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49e5674c-f586-438f-bf95-d356a2985f3d",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "acd6bd3eff75572c3",
  "type": "user",
  "uuid": "6d7598b0-07e8-4c45-9060-d7f71aacee13",
  "sourceToolAssistantUUID": "49e5674c-f586-438f-bf95-d356a2985f3d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-27T23:05:19.078Z_

<details><summary>↩ Tool result · `toolu_01VP7L5cr6i6VfkhNJupnu3K`</summary>

```text
# Technical Summary: Group Sequence Policy Optimization (GSPO)

## Core Innovation
GSPO shifts from token-level to sequence-level importance weighting in RL training for LLMs. Rather than computing importance ratios at individual tokens, the method "optimizes a clipped objective over groups of sequences, using normalized sequence-level advantage and importance ratios."

## Key Technical Differences from GRPO

**Token-Level Issues in GRPO:**
The fundamental problem is "a mismatch between the unit of reward (sequence-level) and the unit of optimization (token-level)." GRPO applies importance sampling at the token level using only single samples, causing high variance in gradients and potential model collapse.

**GSPO's Sequence-Level Approach:**
- Computes importance ratios using full sequence likelihood ratios, normalized by length to reduce variance
- Clips entire sequences rather than individual tokens
- Prevents unstable gradients from overly off-policy samples while maintaining consistency between reward and optimization units

## MoE Stability Breakthrough

A critical finding addresses Mixture-of-Experts training instability. In tested models, "the set of experts activated for the same input can change significantly after each gradient update (about 10% difference in a 48-layer Qwen3-30B-A3B-Base model)."

GSPO's sequence-level approach eliminates the need for Routing Replay strategies because "sequence-level likelihood is stable and unaffected by expert routing changes at the token level."

## Experimental Evidence

**Performance:** GSPO outperforms GRPO on coding benchmarks (AIME'24, LiveCodeBench, CodeForces) despite clipping significantly more tokens, suggesting "token-level gradients in GRPO are noisier and less effective."

**Efficiency:** Demonstrates consistent gains with increased compute and longer generations compared to GRPO under identical conditions, with successful deployment in Qwen3 model training.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75905f95-245b-4675-8b74-23fad3747cd8",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "acd6bd3eff75572c3",
  "type": "user",
  "uuid": "3a60f607-f281-4bff-bdc1-6dbc554133a9",
  "sourceToolAssistantUUID": "75905f95-245b-4675-8b74-23fad3747cd8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-27T23:05:26.125Z_

<details><summary>↩ Tool result · `toolu_01F6uUJsVoaM8XBYaFewm6s3`</summary>

```text
# Complete Technical Details of GSPO Algorithm

## 1. Mathematical Formulation

### Core Loss Function
The GSPO objective is:

$$\mathcal{J}_{\text{GSPO}}(\theta) = \mathbb{E}_{x \sim \mathcal{D}, \{y_i\}_{i=1}^G \sim \pi_{\theta_{\text{old}}}(\cdot|x)} \left[\frac{1}{G}\sum_{i=1}^G \min(s_i(\theta)\hat{A}_i, \text{clip}(s_i(\theta), 1-\varepsilon, 1+\varepsilon)\hat{A}_i)\right]$$

### Sequence-Level Importance Ratio
The critical innovation is the length-normalized importance ratio:

$$s_i(\theta) = \left(\frac{\pi_\theta(y_i|x)}{\pi_{\theta_{\text{old}}}(y_i|x)}\right)^{1/|y_i|} = \exp\left(\frac{1}{|y_i|}\sum_{t=1}^{|y_i|}\log\frac{\pi_\theta(y_{i,t}|x,y_{i,<t})}{\pi_{\theta_{\text{old}}}(y_{i,t}|x,y_{i,<t})}\right)$$

The length normalization prevents "dramatic fluctuations" when likelihood changes occur across responses of varying lengths.

### Advantage Estimation
Group-relative normalization applies:

$$\hat{A}_i = \frac{r(x,y_i) - \text{mean}(\{r(x,y_i)\}_{i=1}^G)}{\text{std}(\{r(x,y_i)\}_{i=1}^G)}$$

### Gradient Formulation
The derived gradient (omitting clipping) is:

$$\nabla_\theta\mathcal{J}_{\text{GSPO}}(\theta) = \mathbb{E}_{x \sim \mathcal{D}, \{y_i\}_{i=1}^G \sim \pi_{\theta_{\text{old}}}(\cdot|x)} \left[\frac{1}{G}\sum_{i=1}^G\left(\frac{\pi_\theta(y_i|x)}{\pi_{\theta_{\text{old}}}(y_i|x)}\right)^{1/|y_i|}\hat{A}_i \cdot \frac{1}{|y_i|}\sum_{t=1}^{|y_i|}\nabla_\theta\log\pi_\theta(y_{i,t}|x,y_{i,<t})\right]$$

## 2. Why Token-Level Ratios Fail for MoE Models

The paper identifies fundamental issues:

**Expert Routing Volatility:** In the 48-layer Qwen3-30B-A3B-Base model, "after each RL gradient update and for the same rollout sample, there are roughly 10% of the experts activated under the new policy that are different from those under the old policy."

**Causation Mechanism:** Token-level importance weights $w_{i,t}(\theta) = \frac{\pi_\theta(y_{i,t}|x,y_{i,<t})}{\pi_{\theta_{\text{old}}}(y_{i,t}|x,y_{i,<t})}$ depend directly on per-token routing decisions. When MoE experts change between $\pi_{\theta_{\text{old}}}$ and $\pi_\theta$, these ratios "fluctuate drastically and further invalidates them."

**Why GSPO Avoids This:** The sequence-level importance ratio $s_i(\theta)$ depends only on aggregate sequence likelihood. Since "the MoE model always maintains its language modeling capability, the sequence likelihood will not fluctuate drastically" despite expert routing changes.

## 3. Experimental Results

### Training Performance
Using cold-start fine-tuning from Qwen3-30B-A3B-Base:

**AIME'24:** GSPO demonstrates "remarkably higher training efficiency than GRPO" with better Pass@1 scores under equivalent training compute.

**LiveCodeBench (202410-202502):** Continuous improvement shown across datasets with extended generation lengths.

**CodeForces Elo Rating:** Superior progression compared to baseline.

### Clipping Fraction Observation
A "counter-intuitive finding" emerged: GSPO clips "a much larger fraction of tokens" (two orders of magnitude difference) yet achieves superior efficiency. This suggests "GRPO's token-level gradient estimates are inherently noisy and inefficient for sample exploitation."

### Hyperparameter Settings
- GSPO clipping ranges: left=3e-4, right=4e-4
- GRPO clipping ranges (tuned): left=0.2, right=0.27
- The magnitude difference reflects distinct importance ratio definitions

## 4. Routing Replay Strategy (Previous Approach)

To stabilize GRPO on MoE models, "we cache the activated experts in $\pi_{\theta_{\text{old}}}$ and 'replay' these routing modes in $\pi_\theta$ when computing the importance ratios." This ensured both probabilities used "the same activated network" for consistent token-level ratios.

**Result:** "Routing Replay serves as an essential technique in the normal convergence of the GRPO training of MoE models," but incurred "additional memory and communication overhead and can also limit the actual capacity of the MoE model."

**GSPO Benefit:** Eliminates this dependency entirely, allowing models to "leverage its full capacity without artificial constraints."

## 5. GSPO-token Variant

For finer-grained control, a token-level variant exists:

$$\mathcal{J}_{\text{GSPO-token}}(\theta) = \mathbb{E}\left[\frac{1}{G}\sum_{i=1}^G\frac{1}{|y_i|}\sum_{t=1}^{|y_i|}\min(s_{i,t}(\theta)\hat{A}_{i,t}, \text{clip}(s_{i,t}(\theta), 1-\varepsilon, 1+\varepsilon)\hat{A}_{i,t})\right]$$

Where:
$$s_{i,t}(\theta) = \text{sg}[s_i(\theta)] \cdot \frac{\pi_\theta(y_{i,t}|x,y_{i,<t})}{\text{sg}[\pi_\theta(y_{i,t}|x,y_{i,<t})]}$$

The "sg" denotes gradient stopping (detach). The gradient simplifies to the GSPO form when all token advantages equal sequence advantage.

## 6. Infrastructure Implications

GSPO "makes it possible to directly use the likelihoods returned by the inference engine for optimization, thereby avoiding the need for recomputation with the training engine," since sequence-level likelihoods demonstrate greater tolerance for precision discrepancies between training and inference engines.

## 7. Key Distinction from GRPO

The gradient comparison reveals the fundamental difference. GRPO applies:

$$\nabla_\theta\mathcal{J}_{\text{GRPO}} = \mathbb{E}\left[\frac{1}{G}\sum_{i=1}^G\hat{A}_i \cdot \frac{1}{|y_i|}\sum_{t=1}^{|y_i|}\frac{\pi_\theta(y_{i,t}|x,y_{i,<t})}{\pi_{\theta_{\text{old}}}(y_{i,t}|x,y_{i,<t})}\nabla_\theta\log\pi_\theta(y_{i,t}|x,y_{i,<t})\right]$$

GSPO weights all tokens equally, "eliminating this instability factor of GRPO."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88c7cae0-1339-4586-b7b3-736c9fa80984",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "acd6bd3eff75572c3",
  "type": "user",
  "uuid": "32d5b919-0ac1-4fa9-9636-8e783b75ac01",
  "sourceToolAssistantUUID": "88c7cae0-1339-4586-b7b3-736c9fa80984",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-27T23:05:29.675Z_

Excellent. I have strong technical details now. Let me fetch more content to answer the remaining questions, especially about multi-objective rewards, composite rewards, and the GSPO-token variant.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32d5b919-0ac1-4fa9-9636-8e783b75ac01",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTuoRixocvDYjwKwGsKD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f984fa87-f66e-45e9-b18f-4500749599b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PcQs7riC18paZju4dH6Hum",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1191,
      "cache_creation_input_tokens": 2946,
      "cache_read_input_tokens": 13188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2946,
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

_source line 24 · 2026-05-27T23:05:33.967Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01U21ZbXZneGbKTNpjewQemi`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2507.18071",
  "prompt": "Extract ALL content about:\n1. Multi-objective rewards, multi-component rewards, or composite rewards in GSPO\n2. The GSPO-token variant - full mathematical details and when to use it vs standard GSPO\n3. How GSPO handles per-token advantage vs per-sequence advantage\n4. Token-level advantage assignment - can different tokens get different advantages?\n5. Any discussion of reward decomposition or multiple reward signals\n6. The exact clipping epsilon values used and how they differ from GRPO\n7. Section on related work discussing other sequence-level approaches\n8. Any limitations discussed\n9. The exact benchmark numbers (tables) comparing GSPO vs GRPO\n10. Discussion of KL divergence or entropy bonuses\n11. Any mention of how to combine GSPO with reward models that give different scores for different aspects"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f984fa87-f66e-45e9-b18f-4500749599b9",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTuoRixocvDYjwKwGsKD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08cd9ce9-4a3f-4418-80b7-c2499c1b2e97",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PcQs7riC18paZju4dH6Hum",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1191,
      "cache_creation_input_tokens": 2946,
      "cache_read_input_tokens": 13188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2946,
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

_source line 25 · 2026-05-27T23:05:35.386Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VuKnwzgedqF77YNWXiXEbq`</summary>

```json
{
  "url": "https://huggingface.co/papers/2507.18071",
  "prompt": "Extract all comments, discussions, and community reactions about the GSPO paper. Include any technical discussions about limitations, multi-objective rewards, practical implementation details, or comparisons with other methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08cd9ce9-4a3f-4418-80b7-c2499c1b2e97",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTuoRixocvDYjwKwGsKD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9a90d0d-1848-4a42-b426-9ba542fc0440",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PcQs7riC18paZju4dH6Hum",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1191,
      "cache_creation_input_tokens": 2946,
      "cache_read_input_tokens": 13188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2946,
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

_source line 26 · 2026-05-27T23:05:35.930Z_

<details><summary>↩ Tool result · `toolu_01VuKnwzgedqF77YNWXiXEbq`</summary>

```text
Title: Group Sequence Policy Optimization

URL Source: https://arxiv.org/html/2507.18071

Markdown Content:
Chujie Zheng Shixuan Liu Mingze Li Xiong-Hui Chen Bowen Yu††footnotemark: 

Chang Gao Kai Dang Yuqiong Liu Rui Men An Yang Jingren Zhou Junyang Lin 

 Qwen Team, Alibaba Inc

###### Abstract

This paper introduces Group Sequence Policy Optimization (GSPO), our stable, efficient, and performant reinforcement learning algorithm for training large language models. Unlike previous algorithms that adopt token-level importance ratios, GSPO defines the importance ratio based on sequence likelihood and performs sequence-level clipping, rewarding, and optimization. We demonstrate that GSPO achieves superior training efficiency and performance compared to the GRPO algorithm, notably stabilizes Mixture-of-Experts (MoE) RL training, and has the potential for simplifying the design of RL infrastructure. These merits of GSPO have contributed to the remarkable improvements in the latest Qwen3 models.

1 Introduction
--------------

Reinforcement learning (RL) has emerged as a pivotal paradigm for scaling language models (OpenAI, [2024](https://arxiv.org/html/2507.18071#bib.bib3); DeepSeek-AI, [2025](https://arxiv.org/html/2507.18071#bib.bib1); Qwen, [2025b](https://arxiv.org/html/2507.18071#bib.bib5); [a](https://arxiv.org/html/2507.18071#bib.bib4)). Through large-scale RL, language models develop the capability to tackle sophisticated problems, such as competition-level mathematics and programming, by undertaking deeper and longer reasoning processes.

To successfully scale RL with greater computational investment, the foremost prerequisite is maintaining stable and robust training dynamics. However, current state-of-the-art RL algorithms, exemplified by GRPO (Shao et al., [2024](https://arxiv.org/html/2507.18071#bib.bib7)), exhibit severe stability issues when training gigantic language models, often resulting in catastrophic and irreversible model collapse (Qwen, [2025a](https://arxiv.org/html/2507.18071#bib.bib4); MiniMax, [2025](https://arxiv.org/html/2507.18071#bib.bib2)). This instability hinders efforts to push the capability boundaries of language models through continued RL training.

In this paper, we identify that the instability of GRPO stems from the fundamental misapplication and invalidation of importance sampling weights in its algorithmic design. This introduces high-variance training noise that progressively accumulates with increased response length and is further amplified by the clipping mechanism, ultimately precipitating model collapse.

To address these core limitations, we propose Group Sequence Policy Optimization (GSPO), a new RL algorithm for training large language models. The key innovation of GSPO lies in its theoretically grounded definition of importance ratio based on sequence likelihood (Zheng et al., [2023](https://arxiv.org/html/2507.18071#bib.bib8)), aligning with the basic principle of importance sampling. Additionally, GSPO computes the normalized rewards as the advantages of multiple responses to a query, ensuring the alignment between sequence-level rewarding and optimization.

Our empirical evaluation demonstrates the significant superiority of GSPO over GRPO in training stability, efficiency, and performance. Critically, GSPO has inherently resolved the stability challenges in the RL training of large Mixture-of-Experts (MoE) models, eliminating the need for complex stabilization strategies, and shows the potential for simplifying RL infrastructure. These merits of GSPO ultimately contributed to the exceptional performance improvements in the latest Qwen3 models. We envision GSPO as a robust and scalable algorithmic foundation that will enable the continued advancement of large-scale RL training with language models.

2 Preliminaries
---------------

#### Notation

In this paper, an autoregressive language model parameterized by θ\theta is defined as a policy π θ\pi_{\theta}. We use x x to denote a query and 𝒟\mathcal{D} as the query set. Given a response y y to a query x x, its likelihood under the policy π θ\pi_{\theta} is denoted as π θ​(y|x)=∏t=1|y|π θ​(y t|x,y&lt;t)\pi_{\theta}(y|x)=\prod_{t=1}^{|y|}\pi_{\theta}(y_{t}|x,y_{&lt;t}) where |y||y| denotes the number of tokens in y y. A query-response pair (x,y)(x,y) can be scored by a verifier r r, resulting in a reward r​(x,y)∈[0,1]r(x,y)\in[0,1].

#### Proximal Policy Optimization (PPO)

Using samples generated from the old policy π θ old\pi_{\theta_{\text{old}}}, PPO (Schulman et al., [2017](https://arxiv.org/html/2507.18071#bib.bib6)) constrains the policy update within a proximal region of the old policy through the clipping mechanism. Specifically, PPO employs the following objective for policy optimization (we omit the KL regularization term hereinafter for brevity, as it is not the focus of this paper):

𝒥 PPO​(θ)=𝔼 x∼𝒟,y∼π θ old(⋅|x)​[1|y|​∑t=1|y|min⁡(w t​(θ)​A^t,clip​(w t​(θ),1−ε,1+ε)​A^t)],\displaystyle\mathcal{J}_{\text{PPO}}(\theta)=\mathbb{E}_{x\sim\mathcal{D},\,y\sim\pi_{\theta_{\text{old}}}(\cdot|x)}\left[\frac{1}{|y|}\sum_{t=1}^{|y|}\min\left(w_{t}(\theta)\widehat{A}_{t},\,\mathrm{clip}\left(w_{t}(\theta),1-{\varepsilon},1+{\varepsilon}\right)\widehat{A}_{t}\right)\right],(1)

where the importance ratio of the token y t y_{t} is defined as w t​(θ)=π θ​(y t|x,y&lt;t)π θ old​(y t|x,y&lt;t)w_{t}(\theta)=\frac{\pi_{\theta}(y_{t}|x,y_{&lt;t})}{\pi_{\theta_{\text{old}}}(y_{t}|x,y_{&lt;t})}, the advantage A^t\widehat{A}_{t} of y t y_{t} is estimated by another value model, and ε\varepsilon is the clipping range of importance ratios.

The core challenge of PPO in practice lies in its heavy reliance on the value model. Specifically, the value model usually has a similar size to the policy model, introducing a considerable memory and computational burden. Furthermore, the algorithmic effectiveness hinges on the reliability of its value estimate. While acquiring a reliable value model is inherently challenging, ensuring its scalability to longer responses and more complex tasks presents an even greater challenge.

#### Group Relative Policy Optimization (GRPO)

GRPO (Shao et al., [2024](https://arxiv.org/html/2507.18071#bib.bib7)) bypasses the need for the value model by computing the relative advantage of each response within a group of responses to the same query. Specifically, GRPO optimizes the following objective:

𝒥 GRPO​(θ)=𝔼 x∼𝒟,{y i}i=1 G∼π θ old(⋅|x)​[1 G​∑i=1 G 1|y i|​∑t=1|y i|min⁡(w i,t​(θ)​A^i,t,clip​(w i,t​(θ),1−ε,1+ε)​A^i,t)],\displaystyle\mathcal{J}_{\text{GRPO}}(\theta)=\mathbb{E}_{x\sim\mathcal{D},\,\{y_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\text{old}}}(\cdot|x)}\left[\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|y_{i}|}\sum_{t=1}^{|y_{i}|}\min\left(w_{i,t}(\theta)\widehat{A}_{i,t},\,\mathrm{clip}\left(w_{i,t}(\theta),1-{\varepsilon},1+{\varepsilon}\right)\widehat{A}_{i,t}\right)\right],(2)

where G G is the number of generated responses to each query x x (i.e., the group size), and the importance ratio w i,t​(θ)w_{i,t}(\theta) and advantage A^i,t\widehat{A}_{i,t} of token y i,t y_{i,t} are:

w i,t​(θ)=π θ​(y i,t|x,y i,&lt;t)π θ old​(y i,t|x,y i,&lt;t),A^i,t=A^i=r​(x,y i)−mean​({r​(x,y i)}i=1 G)std​({r​(x,y i)}i=1 G),\displaystyle w_{i,t}(\theta)=\frac{\pi_{\theta}(y_{i,t}|x,y_{i,&lt;t})}{\pi_{\theta_{\text{old}}}(y_{i,t}|x,y_{i,&lt;t})},\quad\ \widehat{A}_{i,t}=\widehat{A}_{i}=\frac{r(x,y_{i})-\mathrm{mean}\left(\{r(x,y_{i})\}_{i=1}^{G}\right)}{\mathrm{std}\left(\{r(x,y_{i})\}_{i=1}^{G}\right)},(3)

respectively, where all the tokens in y i y_{i} share the same advantage as A^i\widehat{A}_{i}.

3 Motivation
------------

The growth in model size, sparsity (e.g., in Mixture-of-Experts models), and response length necessitates a large rollout batch size to maximize hardware utilization during RL. To improve sample efficiency, it is standard practice to partition a large batch of rollout data into multiple mini-batches for gradient updates. This procedure inevitably introduces an off-policy learning setting, where responses y y are sampled from an old policy π θ old\pi_{\theta_{\text{old}}} rather than the current policy π θ\pi_{\theta} being optimized. This also explains the necessity of the clipping mechanism in PPO and GRPO, which prevents overly “off-policy” samples from being involved in gradient estimation.

While mechanisms like clipping aim to manage this off-policy discrepancy, we identify a more fundamental issue in GRPO: its objective is ill-posed. This problem becomes particularly acute when training large models on long-response tasks, leading to catastrophic model collapse. The ill-posed nature of the GRPO objective stems from a misapplication of importance sampling weights. The principle of importance sampling is to estimate the expectation of a function f f under a target distribution π tar\pi_{\text{tar}} by re-weighting samples drawn from a behavior distribution π beh\pi_{\text{beh}}:

𝔼 z∼π tar​[f​(z)]=𝔼 z∼π beh​[π tar​(z)π beh​(z)​f​(z)].\displaystyle\mathbb{E}_{z\sim\pi_{\text{tar}}}\left[f(z)\right]=\mathbb{E}_{z\sim\pi_{\text{beh}}}\left[\frac{\pi_{\text{tar}}(z)}{\pi_{\text{beh}}(z)}\,f(z)\right].(4)

Crucially, this relies on averaging over multiple samples (N≫1 N\gg 1) from the behavior distribution π beh\pi_{\text{beh}} for the importance weight π tar​(z)π beh​(z)\frac{\pi_{\text{tar}}(z)}{\pi_{\text{beh}}(z)} to effectively correct for the distributional mismatch.

In contrast, GRPO applies the importance weight π θ​(y i,t|x,y i,&lt;t)π θ old​(y i,t|x,y i,&lt;t)\frac{\pi_{\theta}(y_{i,t}|x,y_{i,&lt;t})}{\pi_{\theta_{\text{old}}}(y_{i,t}|x,y_{i,&lt;t})} at each token position t t. Since this weight is based on a single sample y i,t y_{i,t} from each next-token distribution π θ old(⋅|x,y i,&lt;t)\pi_{\theta_{\text{old}}}(\cdot|x,y_{i,&lt;t}), it fails to perform the intended distribution-correction role. Instead, it introduces high-variance noise into the training gradients, which accumulates over long sequences and is exacerbated by the clipping mechanism. We have empirically observed that this can lead to model collapse that is often irreversible. Once the collapse occurs, resuming training is unavailing, even when reverting to a previous checkpoint and meticulously tuning hyperparameters (e.g., the clipping ranges), extending generation length, or switching the RL queries.

The above observation suggests a fundamental issue in GRPO’s design. The failure of the token-level importance weight points to a core principle: the unit of optimization objective should match the unit of reward. Since the reward is granted to the entire sequence, applying off-policy correction at the token level appears problematic. This motivates us to forego the token-level objective and explore utilizing importance weights and performing optimization directly at the sequence level.

4 Algorithm
-----------

### 4.1 GSPO: Group Sequence Policy Optimization

While the token-level importance weight π θ​(y i,t|x,y i,&lt;t)π θ old​(y i,t|x,y i,&lt;t)\frac{\pi_{\theta}(y_{i,t}|x,y_{i,&lt;t})}{\pi_{\theta_{\text{old}}}(y_{i,t}|x,y_{i,&lt;t})} is problematic in GRPO, we observe that in the context of language generation, the sequence-level importance weight π θ​(y|x)π θ old​(y|x)\frac{\pi_{\theta}(y|x)}{\pi_{\theta_{\text{old}}}(y|x)} has a clear theoretical meaning: it reflects how far the response y y sampled from π θ old(⋅|x)\pi_{\theta_{\text{old}}}(\cdot|x) deviates from π θ(⋅|x)\pi_{\theta}(\cdot|x), which naturally aligns with the sequence-level reward and can also serve as a meaningful indicator of the clipping mechanism.

Based on this straightforward observation, we propose the Group Sequence Policy Optimization (GSPO) algorithm. GSPO employs the following sequence-level optimization objective:

𝒥 GSPO​(θ)=𝔼 x∼𝒟,{y i}i=1 G∼π θ old(⋅|x)​[1 G​∑i=1 G min⁡(s i​(θ)​A^i,clip​(s i​(θ),1−ε,1+ε)​A^i)],\displaystyle\mathcal{J}_{\text{GSPO}}(\theta)=\mathbb{E}_{x\sim\mathcal{D},\,\{y_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\text{old}}}(\cdot|x)}\left[\frac{1}{G}\sum_{i=1}^{G}\min\left(s_{i}(\theta)\widehat{A}_{i},\,\mathrm{clip}\left(s_{i}(\theta),1-{\varepsilon},1+{\varepsilon}\right)\widehat{A}_{i}\right)\right],(5)

where we adopt the group-based advantage estimation:

A^i=r​(x,y i)−mean​({r​(x,y i)}i=1 G)std​({r​(x,y i)}i=1 G),\displaystyle\widehat{A}_{i}=\frac{r(x,y_{i})-\mathrm{mean}\left(\{r(x,y_{i})\}_{i=1}^{G}\right)}{\mathrm{std}\left(\{r(x,y_{i})\}_{i=1}^{G}\right)},(6)

and define the importance ratio s i​(θ)s_{i}(\theta) based on sequence likelihood (Zheng et al., [2023](https://arxiv.org/html/2507.18071#bib.bib8)):

s i​(θ)=(π θ​(y i|x)π θ old​(y i|x))1|y i|=exp⁡(1|y i|​∑t=1|y i|log⁡π θ​(y i,t|x,y i,&lt;t)π θ old​(y i,t|x,y i,&lt;t)).\displaystyle s_{i}(\theta)=\left(\frac{\pi_{\theta}(y_{i}|x)}{\pi_{\theta_{\text{old}}}(y_{i}|x)}\right)^{\frac{1}{|y_{i}|}}=\exp\left(\frac{1}{|y_{i}|}\sum_{t=1}^{|y_{i}|}\log\frac{\pi_{\theta}(y_{i,t}|x,y_{i,&lt;t})}{\pi_{\theta_{\text{old}}}(y_{i,t}|x,y_{i,&lt;t})}\right).(7)

Therefore, GSPO applies clipping to entire responses instead of individual tokens to exclude the overly “off-policy” samples from gradient estimation, which matches both the sequence-level rewarding and optimization. Note that we adopt length normalization in s i​(θ)s_{i}(\theta) to reduce the variance and to control s i​(θ)s_{i}(\theta) within a unified numerical range. Otherwise, the likelihood changes of a few tokens can result in dramatic fluctuations of the sequence-level importance ratio, and the importance ratios of responses with different lengths will require varying clipping ranges. We also note that the clipping ranges in GSPO and in previous algorithms (e.g., GRPO) typically differ in order of magnitude due to the distinct definitions of importance ratios.

### 4.2 Gradient Analysis

We can derive the gradient of the GSPO objective as follows (clipping is omitted for brevity):

∇θ 𝒥 GSPO​(θ)=\displaystyle\nabla_{\theta}\mathcal{J}_{\text{GSPO}}(\theta)=∇θ 𝔼 x∼𝒟,{y i}i=1 G∼π θ old(⋅|x)​[1 G​∑i=1 G s i​(θ)​A^i]\displaystyle\ \nabla_{\theta}\mathbb{E}_{x\sim\mathcal{D},\,\{y_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\text{old}}}(\cdot|x)}\left[\frac{1}{G}\sum_{i=1}^{G}s_{i}(\theta)\widehat{A}_{i}\right](8)
=\displaystyle=𝔼 x∼𝒟,{y i}i=1 G∼π θ old(⋅|x)​[1 G​∑i=1 G s i​(θ)​A^i⋅∇θ log⁡s i​(θ)]\displaystyle\ \mathbb{E}_{x\sim\mathcal{D},\,\{y_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\text{old}}}(\cdot|x)}\left[\frac{1}{G}\sum_{i=1}^{G}s_{i}(\theta)\widehat{A}_{i}\cdot\nabla_{\theta}\log s_{i}(\theta)\right](9)
=\displaystyle=𝔼 x∼𝒟,{y i}i=1 G∼π θ old(⋅|x)​[1 G​∑i=1 G(π θ​(y i|x)π θ old​(y i|x))1|y i|​A^i⋅1|y i|​∑t=1|y i|∇θ log⁡π θ​(y i,t|x,y i,&lt;t)].\displaystyle\ \mathbb{E}_{x\sim\mathcal{D},\,\{y_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\text{old}}}(\cdot|x)}\left[\frac{1}{G}\sum_{i=1}^{G}\left(\frac{\pi_{\theta}(y_{i}|x)}{\pi_{\theta_{\text{old}}}(y_{i}|x)}\right)^{\frac{1}{|y_{i}|}}\widehat{A}_{i}\cdot\frac{1}{|y_{i}|}\sum_{t=1}^{|y_{i}|}\nabla_{\theta}\log\pi_{\theta}(y_{i,t}|x,y_{i,&lt;t})\right].(10)

For comparison, the gradient of the GRPO objective is as follows (note that A^i,t=A^i\widehat{A}_{i,t}=\widehat{A}_{i}):

∇θ 𝒥 GRPO​(θ)=\displaystyle\nabla_{\theta}\mathcal{J}_{\text{GRPO}}(\theta)=∇θ 𝔼 x∼𝒟,{y i}i=1 G∼π θ old(⋅|x)​[1 G​∑i=1 G 1|y i|​∑t=1|y i|w i,t​(θ)​A^i,t]\displaystyle\ \nabla_{\theta}\mathbb{E}_{x\sim\mathcal{D},\,\{y_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\text{old}}}(\cdot|x)}\left[\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|y_{i}|}\sum_{t=1}^{|y_{i}|}w_{i,t}(\theta)\widehat{A}_{i,t}\right](11)
=\displaystyle=𝔼 x∼𝒟,{y i}i=1 G∼π θ old(⋅|x)​[1 G​∑i=1 G A^i⋅1|y i|​∑t=1|y i|π θ​(y i,t|x,y i,&lt;t)π θ old​(y i,t|x,y i,&lt;t)​∇θ log⁡π θ​(y i,t|x,y i,&lt;t)].\displaystyle\ \mathbb{E}_{x\sim\mathcal{D},\,\{y_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\text{old}}}(\cdot|x)}\left[\frac{1}{G}\sum_{i=1}^{G}\widehat{A}_{i}\cdot\frac{1}{|y_{i}|}\sum_{t=1}^{|y_{i}|}\frac{\pi_{\theta}(y_{i,t}|x,y_{i,&lt;t})}{\pi_{\theta_{\text{old}}}(y_{i,t}|x,y_{i,&lt;t})}\nabla_{\theta}\log\pi_{\theta}(y_{i,t}|x,y_{i,&lt;t})\right].(12)

Therefore, the fundamental distinction between GSPO and GRPO lies in how they weight the gradients of the log likelihoods of tokens. In GRPO, the tokens are weighted according to their respective “importance weight” π θ​(y i,t|x,y i,&lt;t)π θ old​(y i,t|x,y i,&lt;t)\frac{\pi_{\theta}(y_{i,t}|x,y_{i,&lt;t})}{\pi_{\theta_{\text{old}}}(y_{i,t}|x,y_{i,&lt;t})}. However, these unequal weights, which can vary among (0,1+ε](0,1+\varepsilon] (for A^i>0\widehat{A}_{i}>0) or [1−ε,+∞)[1-\varepsilon,+\infty) (for A^i<0\widehat{A}_{i}<0), are not negligible, and their impact can accumulate and lead to unpredictable consequences as training progresses. In contrast, GSPO weights all the tokens in a response equally, eliminating this instability factor of GRPO.

### 4.3 GSPO-token: A Token-level Objective Variant

In scenarios like multi-turn RL, we may desire a finer-grained advantage adjustment than the sequence level. To this end, we introduce a token-level objective variant of GSPO, namely GSPO-token, to allow token-wise advantage customization:

𝒥 GSPO-token​(θ)=𝔼 x∼𝒟,{y i}i=1 G∼π θ old(⋅|x)​[1 G​∑i=1 G 1|y i|​∑t=1|y i|min⁡(s i,t​(θ)​A^i,t,clip​(s i,t​(θ),1−ε,1+ε)​A^i,t)],\displaystyle\mathcal{J}_{\text{GSPO-token}}(\theta)=\mathbb{E}_{x\sim\mathcal{D},\,\{y_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\text{old}}}(\cdot|x)}\left[\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|y_{i}|}\sum_{t=1}^{|y_{i}|}\min\left(s_{i,t}(\theta)\widehat{A}_{i,t},\,\mathrm{clip}\left(s_{i,t}(\theta),1-{\varepsilon},1+{\varepsilon}\right)\widehat{A}_{i,t}\right)\right],(13)

where

s i,t​(θ)=sg​[s i​(θ)]⋅π θ​(y i,t|x,y i,<t)sg​[π θ​(y i,t|x,y i,<t)],\displaystyle s_{i,t}(\theta)=\mathrm{sg}\left[s_{i}(\theta)\right]\cdot\frac{\pi_{\theta}(y_{i,t}|x,y_{i,<t})}{\mathrm{sg}\left[\pi_{\theta}(y_{i,t}|x,y_{i,<t})\right]},(14)

and sg​[⋅]\mathrm{sg}[\cdot] denotes only taking the numerical value but stopping the gradient, corresponding to the detach operation in PyTorch. The gradient of GSPO-token can be derived as:

∇θ 𝒥 GSPO-token​(θ)=\displaystyle\nabla_{\theta}\mathcal{J}_{\text{GSPO-token}}(\theta)=∇θ 𝔼 x∼𝒟,{y i}i=1 G∼π θ old(⋅|x)​[1 G​∑i=1 G 1|y i|​∑t=1|y i|s i,t​(θ)​A^i,t]\displaystyle\ \nabla_{\theta}\mathbb{E}_{x\sim\mathcal{D},\,\{y_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\text{old}}}(\cdot|x)}\left[\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|y_{i}|}\sum_{t=1}^{|y_{i}|}s_{i,t}(\theta)\widehat{A}_{i,t}\right](15)
=\displaystyle=𝔼 x∼𝒟,{y i}i=1 G∼π θ old(⋅|x)​[1 G​∑i=1 G s i​(θ)⋅1|y i|​∑t=1|y i|A^i,t​∇θ π θ​(y i,t|x,y i,<t)π θ​(y i,t|x,y i,<t)]\displaystyle\ \mathbb{E}_{x\sim\mathcal{D},\,\{y_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\text{old}}}(\cdot|x)}\left[\frac{1}{G}\sum_{i=1}^{G}s_{i}(\theta)\cdot\frac{1}{|y_{i}|}\sum_{t=1}^{|y_{i}|}\widehat{A}_{i,t}\frac{\nabla_{\theta}\pi_{\theta}(y_{i,t}|x,y_{i,<t})}{\pi_{\theta}(y_{i,t}|x,y_{i,<t})}\right](16)
=\displaystyle=𝔼 x∼𝒟,{y i}i=1 G∼π θ old(⋅|x)​[1 G​∑i=1 G(π θ​(y i|x)π θ old​(y i|x))1|y i|⋅1|y i|​∑t=1|y i|A^i,t​∇θ log⁡π θ​(y i,t|x,y i,<t)].\displaystyle\ \mathbb{E}_{x\sim\mathcal{D},\,\{y_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\text{old}}}(\cdot|x)}\left[\frac{1}{G}\sum_{i=1}^{G}\left(\frac{\pi_{\theta}(y_{i}|x)}{\pi_{\theta_{\text{old}}}(y_{i}|x)}\right)^{\frac{1}{|y_{i}|}}\cdot\frac{1}{|y_{i}|}\sum_{t=1}^{|y_{i}|}\widehat{A}_{i,t}\nabla_{\theta}\log\pi_{\theta}(y_{i,t}|x,y_{i,<t})\right].(17)

Note that the term π θ​(y i,t|x,y i,<t)sg​[π θ​(y i,t|x,y i,<t)]\frac{\pi_{\theta}(y_{i,t}|x,y_{i,<t})}{\mathrm{sg}\left[\pi_{\theta}(y_{i,t}|x,y_{i,<t})\right]} has a numerical value of 1, so s i,t​(θ)s_{i,t}(\theta) is numerically equal to s i​(θ)s_{i}(\theta). Comparing Equation([5](https://arxiv.org/html/2507.18071#S4.E5 "In 4.1 GSPO: Group Sequence Policy Optimization ‣ 4 Algorithm ‣ Group Sequence Policy Optimization")) and([13](https://arxiv.org/html/2507.18071#S4.E13 "In 4.3 GSPO-token: A Token-level Objective Variant ‣ 4 Algorithm ‣ Group Sequence Policy Optimization")), and Equation([10](https://arxiv.org/html/2507.18071#S4.E10 "In 4.2 Gradient Analysis ‣ 4 Algorithm ‣ Group Sequence Policy Optimization")) and([17](https://arxiv.org/html/2507.18071#S4.E17 "In 4.3 GSPO-token: A Token-level Objective Variant ‣ 4 Algorithm ‣ Group Sequence Policy Optimization")), GSPO-token and GSPO are numerically identical in the optimization objective, clipping condition, and theoretical gradient when we set the advantages of all the tokens in the response y i y_{i} to the same value (i.e., A^i,t=A^i\widehat{A}_{i,t}=\widehat{A}_{i}), while GSPO-token enjoys the higher flexibility of adjusting the advantages per token.

5 Experiments and Discussion
----------------------------

### 5.1 Empirical Results

We experiment with a cold-start model fine-tuned from Qwen3-30B-A3B-Base, and report the training reward curves as well as the model performance curves on the AIME’24 (average Pass@1 over 32 samplings), LiveCodeBench (202410-202502, average Pass@1 over 8 samplings), and CodeForces (Elo Rating) benchmarks. During the RL training, each batch of rollout data is partitioned into four mini-batches for gradient updates. In GSPO, we set the left and right clipping ranges in Equation([5](https://arxiv.org/html/2507.18071#S4.E5 "In 4.1 GSPO: Group Sequence Policy Optimization ‣ 4 Algorithm ‣ Group Sequence Policy Optimization")) to 3e-4 and 4e-4, respectively. We compare against GRPO as the baseline and set the left and right clipping ranges in Equation([2](https://arxiv.org/html/2507.18071#S2.E2 "In Group Relative Policy Optimization (GRPO) ‣ 2 Preliminaries ‣ Group Sequence Policy Optimization")) to 0.2 and 0.27, respectively, which we have carefully tuned to ensure a fair comparison. Note that GRPO necessitates the Routing Replay training strategy for the normal convergence of MoE RL, which we will additionally discuss in §[5.3](https://arxiv.org/html/2507.18071#S5.SS3 "5.3 Benefit of GSPO for MoE Training ‣ 5 Experiments and Discussion ‣ Group Sequence Policy Optimization"), while GSPO has obviated the need for this strategy.

Figure[1](https://arxiv.org/html/2507.18071#S5.F1 "Figure 1 ‣ 5.1 Empirical Results ‣ 5 Experiments and Discussion ‣ Group Sequence Policy Optimization") shows that the training with GSPO proceeds stably throughout. We observe that GSPO can deliver continuous performance improvement through increasing the training compute, regularly updating the query set, and extending the generation length. Moreover, GSPO also demonstrates superior training efficiency over GRPO, achieving better training accuracy and benchmark performance under the same training compute and consumed queries. Finally, we have successfully applied GSPO to the RL training of the latest Qwen3 models, strongly proving the efficacy of GSPO in unleashing the power of RL scaling for large language models.

![Image 1: Refer to caption](https://arxiv.org/html/2507.18071v2/x1.png)

Figure 1:  Training curves of a cold-start model fine-tuned from Qwen3-30B-A3B-Base. GSPO possesses remarkably higher training efficiency than GRPO. 

### 5.2 Curious Observation on Clipping Fractions

A key distinction of GSPO compared to GRPO is its practice of clipping entire responses rather than individual tokens. Particularly, as shown in Figure[2](https://arxiv.org/html/2507.18071#S5.F2 "Figure 2 ‣ 5.2 Curious Observation on Clipping Fractions ‣ 5 Experiments and Discussion ‣ Group Sequence Policy Optimization"), we observe a difference of two orders of magnitude in the fractions of clipped tokens between GSPO and GRPO (while adjusting the clipping ranges does not alter the disparity in magnitude). However, despite clipping significantly more tokens and consequently using fewer for training (or gradient estimation), GSPO still achieves higher training efficiency than GRPO. This counter-intuitive finding — that clipping a much larger fraction of tokens leads to superior training efficiency — further indicates that GRPO’s token-level gradient estimates are inherently noisy and inefficient for sample exploitation. In contrast, GSPO’s sequence-level approach provides a more reliable and effective learning signal.

![Image 2: Refer to caption](https://arxiv.org/html/2507.18071v2/x2.png)

Figure 2:  Average fractions of clipped tokens over the RL training of GSPO and GRPO. 

### 5.3 Benefit of GSPO for MoE Training

#### Background

Compared to the RL training of dense models, the sparse activation nature of MoE models introduces unique stability challenges. In particular, we found that when adopting the GRPO algorithm, the expert-activation volatility of MoE models can prevent RL training from converging properly. To be specific, after one or more gradient updates, the experts activated for the same response can change significantly. For example, with the 48-layer Qwen3-30B-A3B-Base model, after each RL gradient update and for the same rollout sample, there are roughly 10% of the experts activated under the new policy π θ\pi_{\theta} that are different from those under the old policy π θ old\pi_{\theta_{\text{old}}}. This phenomenon, which becomes more prominent in deeper MoE models, makes the token-level importance ratios w i,t​(θ)=π θ​(y i,t|x,y i,<t)π θ old​(y i,t|x,y i,<t)w_{i,t}(\theta)=\frac{\pi_{\theta}(y_{i,t}|x,y_{i,<t})}{\pi_{\theta_{\text{old}}}(y_{i,t}|x,y_{i,<t})} fluctuate drastically and further invalidates them, as discussed in §[3](https://arxiv.org/html/2507.18071#S3 "3 Motivation ‣ Group Sequence Policy Optimization") and[4.2](https://arxiv.org/html/2507.18071#S4.SS2 "4.2 Gradient Analysis ‣ 4 Algorithm ‣ Group Sequence Policy Optimization"), consequently hindering the normal convergence of RL training.

#### Our Previous Approach

To tackle this challenge, we previously employed the Routing Replay training strategy. Specifically, we cache the activated experts in π θ old\pi_{\theta_{\text{old}}} and “replay” these routing modes in π θ\pi_{\theta} when computing the importance ratios w i,t​(θ)=π θ​(y i,t|x,y i,<t)π θ old​(y i,t|x,y i,<t)w_{i,t}(\theta)=\frac{\pi_{\theta}(y_{i,t}|x,y_{i,<t})}{\pi_{\theta_{\text{old}}}(y_{i,t}|x,y_{i,<t})}. In this way, for each token y i,t y_{i,t}, π θ​(y i,t|x,y i,<t)\pi_{\theta}(y_{i,t}|x,y_{i,<t}) and π θ old​(y i,t|x,y i,<t)\pi_{\theta_{\text{old}}}(y_{i,t}|x,y_{i,<t}) share the same activated network, so that we can restore the stability of the token-level importance ratios and ensure optimization of the consistent activated network across gradient updates. Figure[3](https://arxiv.org/html/2507.18071#S5.F3 "Figure 3 ‣ Our Previous Approach ‣ 5.3 Benefit of GSPO for MoE Training ‣ 5 Experiments and Discussion ‣ Group Sequence Policy Optimization") demonstrates that Routing Replay serves as an essential technique in the normal convergence of the GRPO training of MoE models.

![Image 3: Refer to caption](https://arxiv.org/html/2507.18071v2/x3.png)

Figure 3:  The Routing Replay strategy plays a critical role in the normal convergence of the GRPO training of MoE models. 

#### Benefit of GSPO

Although Routing Replay enables the GRPO training of MoE models to converge properly, its practice of reusing routing modes incurs additional memory and communication overhead and can also limit the actual capacity of the MoE model. In contrast, as shown in Figure[1](https://arxiv.org/html/2507.18071#S5.F1 "Figure 1 ‣ 5.1 Empirical Results ‣ 5 Experiments and Discussion ‣ Group Sequence Policy Optimization"), GSPO eliminates the dependency on Routing Replay and is fully capable of computing the importance ratios s i​(θ)s_{i}(\theta) conventionally, converging normally, and optimizing stably. The key insight is that GSPO focuses only on the sequence likelihood (i.e., π θ​(y i|x)\pi_{\theta}(y_{i}|x)) and is not sensitive to the individual token likelihood (i.e., π θ​(y i,t|x,y i,<t)\pi_{\theta}(y_{i,t}|x,y_{i,<t})). Since the MoE model always maintains its language modeling capability, the sequence likelihood will not fluctuate drastically. In summary, GSPO fundamentally resolves the expert-activation volatility issue in MoE models, obviating the need for complex workarounds like Routing Replay. This not only simplifies and stabilizes the training process but also allows the model to leverage its full capacity without artificial constraints.

### 5.4 Benefit of GSPO for RL Infrastructure

Given the precision discrepancies between training engines (e.g., Megatron) and inference engines (e.g., SGLang and vLLM), in practice, we typically use the training engine to recompute the likelihoods of sampled responses under the old policy π θ old\pi_{\theta_{\text{old}}}. However, GSPO uses only sequence-level, rather than token-level, likelihoods for optimization, and intuitively, the former is much more tolerant of precision discrepancies. Hence, GSPO makes it possible to directly use the likelihoods returned by the inference engine for optimization, thereby avoiding the need for recomputation with the training engine. This can be especially beneficial in scenarios like partial rollout and multi-turn RL and in the training-inference disaggregated frameworks.

6 Conclusion
------------

We propose Group Sequence Policy Optimization (GSPO), a new reinforcement learning algorithm for training large language models. Following the basic principle of importance sampling, GSPO defines importance ratios based on sequence likelihood and performs sequence-level clipping, rewarding, and optimization. GSPO demonstrates notably superior training stability, efficiency, and performance compared to GRPO and exhibits particular efficacy for the large-scale RL training of MoE models, laying the foundation for the exceptional improvements in the latest Qwen3 models. With GSPO as a scalable algorithmic cornerstone, we will continue to scale RL and look forward to the resulting fundamental advances in intelligence.

References
----------

*   DeepSeek-AI [2025] DeepSeek-AI. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. _arXiv preprint arXiv:2501.12948_, 2025. 
*   MiniMax [2025] MiniMax. Minimax-m1: Scaling test-time compute efficiently with lightning attention. _arXiv preprint arXiv:2506.13585_, 2025. 
*   OpenAI [2024] OpenAI. Learning to reason with LLMs, 2024. URL [https://openai.com/index/learning-to-reason-with-llms/](https://openai.com/index/learning-to-reason-with-llms/). 
*   Qwen [2025a] Team Qwen. Qwen3 technical report. _arXiv preprint arXiv:2505.09388_, 2025a. 
*   Qwen [2025b] Team Qwen. Qwq-32b: Embracing the power of reinforcement learning, March 2025b. URL [https://qwenlm.github.io/blog/qwq-32b/](https://qwenlm.github.io/blog/qwq-32b/). 
*   Schulman et al. [2017] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. _arXiv preprint arXiv:1707.06347_, 2017. 
*   Shao et al. [2024] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y.K. Li, Y.Wu, and Daya Guo. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. _arXiv preprint arXiv:2402.03300_, 2024. 
*   Zheng et al. [2023] Chujie Zheng, Pei Ke, Zheng Zhang, and Minlie Huang. Click: Controllable text generation with sequence likelihood contrastive learning. In _Findings of the Association for Computational Linguistics: ACL 2023_, 2023. URL [https://aclanthology.org/2023.findings-acl.65/](https://aclanthology.org/2023.findings-acl.65/).

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9a90d0d-1848-4a42-b426-9ba542fc0440",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "acd6bd3eff75572c3",
  "type": "user",
  "uuid": "ce76ada0-93a1-49c5-97e7-dd5e1e8490e0",
  "sourceToolAssistantUUID": "b9a90d0d-1848-4a42-b426-9ba542fc0440",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-27T23:05:37.262Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015oqoHgLaY6sctzisG44svN`</summary>

```json
{
  "url": "https://normaluhr.github.io/2025/08/08/GRPO_DAPO_GSPO/",
  "prompt": "Extract all technical details about GSPO from this blog post. Focus on: mathematical formulations, comparison with GRPO and DAPO, any discussion of multi-objective rewards, limitations of sequence-level clipping, and practical implementation insights."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce76ada0-93a1-49c5-97e7-dd5e1e8490e0",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTuoRixocvDYjwKwGsKD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "873eae2e-6142-4330-89ff-0523abd948b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PcQs7riC18paZju4dH6Hum",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1191,
      "cache_creation_input_tokens": 2946,
      "cache_read_input_tokens": 13188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2946,
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

_source line 28 · 2026-05-27T23:05:40.548Z_

<details><summary>↩ Tool result · `toolu_01U21ZbXZneGbKTNpjewQemi`</summary>

```text
# GSPO Technical Details Extraction

## 1. Multi-objective/Composite Rewards
The document does not contain detailed discussion of multi-objective reward structures in GSPO. The focus remains on single reward signals applied at the sequence level.

## 2. GSPO-Token Variant
The PDF appears to be primarily a title page and metadata. The actual technical content describing token-level variants is not accessible in the provided excerpt.

## 3. Per-Token vs Per-Sequence Advantage
Specific mathematical details comparing token-level and sequence-level advantage assignment are not visible in the available content sections.

## 4. Token-Level Advantage Assignment
The document does not provide explicit details on whether different tokens receive differentiated advantages within sequences.

## 5. Reward Decomposition
No substantive discussion of reward decomposition or multiple reward signal integration appears in the accessible portions.

## 6. Clipping Epsilon Values
"This is pdfTeX, Version 3.141592653-2.6-1.40.25" - the actual hyperparameter values are not shown in available sections.

## 7. Related Work Section
References appear in the metadata (citations to O1, DPSK-R1, QWQ-32B, GRPO, QWEN3, MiniMax-M1, CLICK, PPO) but the actual comparative discussion text is not accessible.

## 8. Limitations Discussion
No limitations section appears in the provided PDF excerpt.

## 9. Benchmark Comparisons
Specific numerical benchmark tables comparing GSPO versus GRPO are not visible in the available content.

## 10. KL Divergence/Entropy Bonuses
These technical details are not present in the accessible document sections.

## 11. Combining GSPO with Multi-aspect Reward Models
No guidance on integrating multi-aspect reward structures appears in available content.

**Note:** The provided PDF appears truncated, containing primarily structural metadata rather than the full paper body where these technical details would reside.

[Binary content (application/pdf, 448KB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/6a7b539d-3001-4492-a786-49601df55b48/tool-results/webfetch-1779923133986-hk7p0d.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08cd9ce9-4a3f-4418-80b7-c2499c1b2e97",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "acd6bd3eff75572c3",
  "type": "user",
  "uuid": "88c9ea06-9e2b-4d61-ae0b-2b38e1928750",
  "sourceToolAssistantUUID": "08cd9ce9-4a3f-4418-80b7-c2499c1b2e97",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-27T23:05:45.701Z_

<details><summary>↩ Tool result · `toolu_015oqoHgLaY6sctzisG44svN`</summary>

```text
# Technical Details on GSPO from Blog Post

## Mathematical Formulation

GSPO's loss function replaces token-level importance ratios with sequence-level ones:

$$\mathcal{J}_{\text{GSPO}}(\theta) = \mathbb{E}_{q,\{o_i\}}\left[\frac{1}{G}\sum_{i=1}^G \frac{1}{|o_i|}\sum_{t=1}^{|o_i|} \min(s_i(\theta)A_i, \text{clip}(s_i(\theta), 1-\varepsilon, 1+\varepsilon)A_i)\right]$$

The sequence-level ratio uses length normalization and exponentiation:

$$s_i(\theta) = \exp\left(\frac{1}{|o_i|}\sum_{t=1}^{|o_i|}\log\frac{\pi_\theta(o_{i,t}|q,o_{i,<t})}{\pi_{\theta_{\text{old}}}(o_{i,t}|q,o_{i,<t})}\right)$$

## Key Architectural Differences

**GSPO vs. GRPO Gradient Behavior:**

- GSPO applies identical weighting across all tokens within a response: "all tokens in a response share the same weight $s_i(\theta)A_i/|o_i|$"
- GRPO varies weights per token position via $r_{i,t}(\theta)$, introducing higher variance in long sequences

**Design Rationale for Exponentiation:**

The post clarifies that "the weight must be a probability ratio ($\geq 0$), not a log-probability difference." Direct log-likelihood differences would violate importance sampling theory, requiring the exponential transformation to maintain unbiased gradient estimation.

## MoE-Specific Advantages

The core motivation addresses "expert activation volatility" where new and old policies activate different expert modules, creating structural noise. GSPO avoids "Routing Replay" infrastructure costs by optimizing entire sequences rather than tokens, naturally circumventing routing path inconsistencies.

## Sequence-Level Clipping Implications

When clipping triggers on $s_i(\theta)$, the entire sequence is clipped rather than individual tokens. The length normalization factor prevents "a few volatile tokens in a long sequence from causing the ratio to explode," maintaining numerical stability across variable-length outputs.

## Practical Training Insights

Despite using fewer effective tokens due to aggressive clipping, "GSPO achieved higher training efficiency" empirically, suggesting that sequence-level optimization provides better convergence properties even with reduced gradient-contributing samples.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "873eae2e-6142-4330-89ff-0523abd948b6",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "acd6bd3eff75572c3",
  "type": "user",
  "uuid": "5b80ba3e-357f-4408-9e79-26f426d80e80",
  "sourceToolAssistantUUID": "873eae2e-6142-4330-89ff-0523abd948b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-27T23:05:49.102Z_

I now have the complete paper content. Let me fetch a couple more resources to check for any discussion of multi-objective rewards and composite reward signals specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b80ba3e-357f-4408-9e79-26f426d80e80",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTupsR5EBbaLqcRNMqsT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b778297-0f50-4071-b5cf-9c3840162c69",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eq2e5xkYajAHsHgQJiMNdR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14946,
      "cache_read_input_tokens": 16134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14946,
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

_source line 31 · 2026-05-27T23:05:50.049Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HPEWieMfT8iWWUWjNG9vYY`</summary>

```json
{
  "query": "GSPO \"multi-objective\" OR \"composite reward\" OR \"reward decomposition\" OR \"multi-component\" reinforcement learning LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b778297-0f50-4071-b5cf-9c3840162c69",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTupsR5EBbaLqcRNMqsT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "367b7128-69d1-40ef-83e3-7f9fc700b68f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eq2e5xkYajAHsHgQJiMNdR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14946,
      "cache_read_input_tokens": 16134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14946,
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

_source line 32 · 2026-05-27T23:05:52.929Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Nr5jQV5jgLt5rBLrECUSRo`</summary>

```json
{
  "url": "https://medium.com/@hongjianzou/rlhf-algorithms-ppo-grpo-gspo-differences-trade-offs-and-use-cases-241d003d806d",
  "prompt": "Extract all technical details about GSPO, especially any discussion of:\n1. Multi-objective or multi-component rewards\n2. How GSPO handles different reward types\n3. Limitations of sequence-level clipping for fine-grained reward signals\n4. Any practical guidance on combining GSPO with composite rewards\n5. Trade-offs discussed"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "367b7128-69d1-40ef-83e3-7f9fc700b68f",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTupsR5EBbaLqcRNMqsT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d9cdb95-54e3-41ae-9c26-132362a8abba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eq2e5xkYajAHsHgQJiMNdR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14946,
      "cache_read_input_tokens": 16134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14946,
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

_source line 33 · 2026-05-27T23:05:54.699Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YSrUbFtmFFtNkLzshEDEhe`</summary>

```json
{
  "url": "https://kaitchup.substack.com/p/gspo-vs-grpo-reinforcement-learning",
  "prompt": "Extract all technical details comparing GSPO and GRPO, especially:\n1. Any discussion of multi-objective or composite rewards\n2. Practical implementation differences\n3. Performance benchmarks\n4. Limitations of either approach\n5. Any discussion of when GRPO might be preferred over GSPO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d9cdb95-54e3-41ae-9c26-132362a8abba",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTupsR5EBbaLqcRNMqsT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1404d059-5b60-472b-acca-644cbbcfd6cb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eq2e5xkYajAHsHgQJiMNdR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14946,
      "cache_read_input_tokens": 16134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14946,
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

_source line 34 · 2026-05-27T23:05:58.675Z_

<details><summary>↩ Tool result · `toolu_01HPEWieMfT8iWWUWjNG9vYY`</summary>

```text
Web search results for query: "GSPO "multi-objective" OR "composite reward" OR "reward decomposition" OR "multi-component" reinforcement learning LLM"

Links: [{"title":"Group Sequence Policy Optimization (GSPO)","url":"https://www.emergentmind.com/topics/group-sequence-policy-optimization-gspo"},{"title":"Composite Reward Models","url":"https://www.emergentmind.com/topics/composite-reward-models"},{"title":"Large Language Model Guided Incentive Aware Reward Design for Cooperative Multi-Agent Reinforcement Learning","url":"https://arxiv.org/pdf/2603.24324"},{"title":"Multi-Reward Reinforcement Learning","url":"https://www.emergentmind.com/topics/multi-reward-reinforcement-learning"},{"title":"Agent-GSPO: Communication-Efficient Multi-Agent Systems via Group Sequence Policy Optimization","url":"https://arxiv.org/html/2510.22477"},{"title":"Large Language Models as Efficient Reward Function Searchers for Custom-Environment Multi-Objective Reinforcement Learning","url":"https://arxiv.org/html/2409.02428v1"}]

I found relevant results for your search query. Here's a summary of the key findings:

## GSPO and Multi-Objective/Composite Reward RL with LLMs

**GSPO Overview:**
Group Sequence Policy Optimization (GSPO) is a reinforcement learning algorithm developed to address stability, efficiency, and scalability in policy optimization—particularly in LLM training. GSPO departs from conventional token-level importance weighting by introducing a sequence-level objective, with the aim of aligning optimization units with the granularity at which rewards are assigned.

**Composite Reward Models:**
A composite reward model is a reward function constructed by combining multiple component terms, each capturing a distinct facet of performance or behavioral preference in reinforcement learning (RL) and related settings. Composite reward models have become central to contemporary RL for complex decision-making tasks—such as aligning LLMs with human preferences, adaptive control, risk-constrained optimization, and more—because single-objective reward proxies rarely capture all relevant desiderata and are especially prone to overoptimization pathologies.

**Multi-Reward RL Frameworks:**
Multi-reward reinforcement learning (MRRL) encompasses frameworks where an agent's performance is evaluated or optimized using multiple reward signals—either simultaneously or as a latent structure embedded in the environment. This paradigm subsumes classic multi-objective RL, reward decomposition, joint optimization of stochastic and non-linear reward functionals, episodic or task-specific reward variation, and learning from human or bandit feedback that encodes composite preferences.

**LLM Applications:**
Research utilizes task decomposition and white-box search, employing LLMs as effective searchers to fully leverage its semantic understanding capabilities. Unlike previous work on LLM-aided reward function design, some approaches separate the process of reward code design and weight assignment into two stages, while dividing the multi-objective RL task into multiple explicit numerical goals.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "367b7128-69d1-40ef-83e3-7f9fc700b68f",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "acd6bd3eff75572c3",
  "type": "user",
  "uuid": "e72e1a9a-94d0-4750-966e-a55fc554f5af",
  "sourceToolAssistantUUID": "367b7128-69d1-40ef-83e3-7f9fc700b68f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-27T23:05:58.985Z_

<details><summary>↩ Tool result · `toolu_01YSrUbFtmFFtNkLzshEDEhe`</summary>

```text
# GSPO vs GRPO: Technical Comparison

Based on the provided content, here's what can be extracted about these reinforcement learning methods:

## Available Information

The article introduces **Group Sequence Policy Optimization (GSPO)** as Qwen's new RL technique for training mixture-of-experts (MoE) models. The author claims it shows "superior training stability, efficiency, and performance" compared to GRPO, particularly for MoE architectures.

## Key Claims

- GSPO has been integrated into Hugging Face TRL
- Implementation requires only minimal modifications to existing GRPO scripts
- The method was developed during updates to Qwen3-235B models

## Significant Limitation

**The article does not contain the detailed technical comparison you requested.** The substantive section titled "GSPO Explained" is behind a paywall for paid subscribers only. Therefore, I cannot provide specific information about:

- Multi-objective or composite reward mechanisms
- Concrete implementation differences
- Performance benchmarks or metrics
- Technical limitations of either approach
- Scenarios favoring GRPO over GSPO

## Recommendation

To access the technical details you're seeking, you would need to review the full paid article or locate the original Qwen research publication on this topic.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1404d059-5b60-472b-acca-644cbbcfd6cb",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "acd6bd3eff75572c3",
  "type": "user",
  "uuid": "a7a493e7-75eb-4c33-8344-dc82b401c7ff",
  "sourceToolAssistantUUID": "1404d059-5b60-472b-acca-644cbbcfd6cb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-27T23:06:01.139Z_

<details><summary>↩ Tool result · `toolu_01Nr5jQV5jgLt5rBLrECUSRo`</summary>

```text
# GSPO Technical Details: Multi-Reward and Composite Reward Analysis

Based on the provided article, here's what's discussed regarding GSPO and reward handling:

## What the Article Covers

**Core GSPO Mechanism:**
The article explains that GSPO moves from "token-level to sequence-level optimization" with "sequence-level clipping, rewarding, and optimization." The sequence-level importance ratio is defined as how much the updated policy diverges from the old policy for generating a complete response.

**Single Reward Model Focus:**
The article discusses GSPO primarily in the context of standard RLHF with one reward signal per sequence. It notes that rewards in RLHF are "usually at the sequence level," suggesting a single composite evaluation rather than multi-component rewards.

## Notable Gaps

The article does **not address**:
1. Multi-objective or multi-component reward architectures
2. How GSPO would handle multiple distinct reward signals simultaneously
3. Limitations when applying sequence-level clipping to fine-grained or granular reward signals
4. Practical strategies for combining GSPO with composite reward structures
5. Trade-offs between sequence-level and more granular reward approaches

## Summary

This article treats rewards as monolithic sequence-level signals. For guidance on GSPO with complex, multi-component rewards, you would need to consult the original GSPO research papers or implementations beyond this introductory comparison.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d9cdb95-54e3-41ae-9c26-132362a8abba",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "acd6bd3eff75572c3",
  "type": "user",
  "uuid": "5e78dce0-f0d1-4aa3-a68d-aa2af7798922",
  "sourceToolAssistantUUID": "1d9cdb95-54e3-41ae-9c26-132362a8abba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-27T23:06:04.787Z_

Let me search for the Agent-GSPO paper and any more discussion about GSPO with multi-turn/multi-objective setups, plus check for the GSPO-token variant's applicability to multi-component rewards.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e78dce0-f0d1-4aa3-a68d-aa2af7798922",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTur1RJwbBhTvLyLhJ7K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "484f6227-a92f-4678-8f12-fb86f4704f9b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0161E9hYi9M6Ny7f2bjQqbct",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 314,
      "cache_creation_input_tokens": 1537,
      "cache_read_input_tokens": 31080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1537,
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

_source line 38 · 2026-05-27T23:06:05.264Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01682n49Zz31Kf9kRuAGLEeo`</summary>

```json
{
  "query": "GSPO-token variant multi-turn RL per-token advantage different reward signals"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "484f6227-a92f-4678-8f12-fb86f4704f9b",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTur1RJwbBhTvLyLhJ7K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b954b10b-6777-4d1b-9103-118f3f91b2ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0161E9hYi9M6Ny7f2bjQqbct",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 314,
      "cache_creation_input_tokens": 1537,
      "cache_read_input_tokens": 31080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1537,
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

_source line 39 · 2026-05-27T23:06:05.736Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MnQUY695ruHPCdGqzEou3J`</summary>

```json
{
  "query": "\"GSPO\" sequence-level clipping limitation per-component reward granular feedback"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b954b10b-6777-4d1b-9103-118f3f91b2ee",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTur1RJwbBhTvLyLhJ7K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0341f0fe-c7b4-40f2-bacf-59549e76977e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0161E9hYi9M6Ny7f2bjQqbct",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 314,
      "cache_creation_input_tokens": 1537,
      "cache_read_input_tokens": 31080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1537,
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

_source line 40 · 2026-05-27T23:06:07.196Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MjSY12YEDFariSUwdSLPb5`</summary>

```json
{
  "url": "https://www.emergentmind.com/papers/2507.18071",
  "prompt": "Extract all technical details, community discussion, analysis, and any mention of limitations, multi-objective rewards, composite rewards, or practical implementation concerns about GSPO."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0341f0fe-c7b4-40f2-bacf-59549e76977e",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTur1RJwbBhTvLyLhJ7K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37b0435d-9b75-4aac-8e9a-bd986ad47f2a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0161E9hYi9M6Ny7f2bjQqbct",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 314,
      "cache_creation_input_tokens": 1537,
      "cache_read_input_tokens": 31080,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1537
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 314,
          "output_tokens": 272,
          "cache_read_input_tokens": 31080,
          "cache_creation_input_tokens": 1537,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1537,
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

_source line 41 · 2026-05-27T23:06:12.824Z_

<details><summary>↩ Tool result · `toolu_01MnQUY695ruHPCdGqzEou3J`</summary>

```text
Web search results for query: ""GSPO" sequence-level clipping limitation per-component reward granular feedback"

Links: [{"title":"Group Sequence Policy Optimization (GSPO)","url":"https://www.emergentmind.com/topics/group-sequence-policy-optimization-gspo"},{"title":"Beyond PPO - The New Wave of Policy Optimization Techniques for LLM Post-Training | yadnyesh's blog","url":"https://ydnyshhh.github.io/posts/policy_optimization/"},{"title":"What is GSPO ? The RL algorithm used to train Qwen3 | by Mehul Gupta | Data Science in Your Pocket | Medium","url":"https://medium.com/data-science-in-your-pocket/what-is-gspo-the-rl-algorithm-used-to-train-qwen3-506d56ff49e6"},{"title":"Reinforcement Learning | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/06-policy-gradients"},{"title":"From GRPO to DAPO and GSPO: What, Why, and How","url":"https://huggingface.co/blog/NormalUhr/grpo-to-dapo-and-gspo"},{"title":"2025-07-29 Group Sequence Policy Optimization Chujie Zheng∗ Shixuan Liu","url":"https://arxiv.org/pdf/2507.18071"},{"title":"Paper Review: Group Sequence Policy Optimization | by Andrew Lukyanenko | Medium","url":"https://artgor.medium.com/paper-review-group-sequence-policy-optimization-543c3526c240"},{"title":"Paper Review: Group Sequence Policy Optimization – Andrey Lukyanenko","url":"https://andlukyane.com/blog/paper-review-gspo"},{"title":"Orchestrating Tokens and Sequences: Dynamic Hybrid Policy Optimization for RLVR","url":"https://arxiv.org/pdf/2601.05607"}]

Based on the search results, here's what I found about GSPO's sequence-level clipping limitation and per-component reward granular feedback:

## Sequence-Level Clipping in GSPO

Rather than applying the PPO clipping at each token, all importance sampling and clipping is sequence-level in GSPO. GSPO applies clipping to entire responses instead of individual tokens to exclude the overly "off-policy" samples from gradient estimation, which matches both the sequence-level rewarding and optimization.

## Key Limitation and Solution

The core limitation GSPO addresses is granularity misalignment: A big chunk of the mess comes from how current methods try to squeeze a reward, which is usually given for the whole output, into a token-by-token update process, asking the model to learn at a level of granularity that the reward doesn't actually care about.

GSPO can be summarized as "GRPO with sequence-level importance ratios"—the IS correction granularity is matched to the reward granularity.

## Length Normalization for Stability

To handle the challenge of variable-length sequences, GSPO adopts length normalization in the importance ratio to reduce the variance and to control it within a unified numerical range, since the likelihood changes of a few tokens can result in dramatic fluctuations of the sequence-level importance ratio.

## Performance Results

Despite the broader clipping approach, although GSPO clips far more tokens by applying sequence-level clipping, it still outperforms GRPO, indicating that token-level gradients in GRPO are noisier and less effective.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0341f0fe-c7b4-40f2-bacf-59549e76977e",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "acd6bd3eff75572c3",
  "type": "user",
  "uuid": "fa575f92-b65a-459f-9c84-a82ae97e6a54",
  "sourceToolAssistantUUID": "0341f0fe-c7b4-40f2-bacf-59549e76977e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-27T23:06:13.630Z_

<details><summary>↩ Tool result · `toolu_01MjSY12YEDFariSUwdSLPb5`</summary>

```text
# GSPO Technical Analysis & Community Discussion

## Core Technical Details

**Sequence-Level Importance Ratio:**
The method replaces token-level weighting with: "s_i(θ) = (π_θ(y_i|x) / π_θ_old(y_i|x))^(1/|y_i|)" normalizing by sequence length to control variance across varying response lengths.

**Algorithmic Objective:**
GSPO employs "min(s_i(θ)Â_i, clip(s_i(θ), 1-ε, 1+ε)Â_i)" at the sequence level rather than token granularity, aligning off-policy correction with reward assignment units.

## Key Problem Identification

The paper identifies that GRPO's "token-level importance ratio introduces high-variance noise" particularly in extended sequences, causing "catastrophic and often irreversible model collapse" during large-scale LLM training.

## MoE Training Innovation

GSPO "eliminates the need for Routing Replay" by leveraging sequence-level likelihoods robust to expert-activation changes, removing additional memory overhead required in GRPO's MoE implementation.

## Empirical Findings

Counterintuitively, GSPO "clips a much larger fraction of tokens than GRPO—by two orders of magnitude—yet still achieves better training efficiency," suggesting superior gradient signal reliability.

## Notable Limitations & Gaps

The document contains **no explicit discussion** of:
- Multi-objective or composite reward handling
- Failure cases or boundary conditions
- Computational overhead comparisons
- Generalization beyond code-based benchmarks (AIME, LiveCodeBench, CodeForces)

## Community Reception

Social engagement shows "2,766 likes across 65 tweets," with modest Reddit discussion (80 points) and HackerNews traction (2 points).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37b0435d-9b75-4aac-8e9a-bd986ad47f2a",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "acd6bd3eff75572c3",
  "type": "user",
  "uuid": "db94d971-0020-4939-8804-a6ad815311cc",
  "sourceToolAssistantUUID": "37b0435d-9b75-4aac-8e9a-bd986ad47f2a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-27T23:06:14.345Z_

<details><summary>↩ Tool result · `toolu_01682n49Zz31Kf9kRuAGLEeo`</summary>

```text
Web search results for query: "GSPO-token variant multi-turn RL per-token advantage different reward signals"

Links: [{"title":"2025-07-29 Group Sequence Policy Optimization Chujie Zheng∗ Shixuan Liu","url":"https://arxiv.org/pdf/2507.18071"},{"title":"Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs","url":"https://arxiv.org/html/2512.17008"},{"title":"GTPO: Fine-Grained Policy Optimization","url":"https://www.emergentmind.com/topics/gtpo"},{"title":"Multi-Turn Reinforcement Learning for Tool-Calling Agents with Iterative Reward Calibration","url":"https://arxiv.org/pdf/2604.02869"},{"title":"Turn-Level Advantage Estimation with PPO for Improved ...","url":"https://aclanthology.org/2026.findings-eacl.328.pdf"},{"title":"GRPO++: Tricks for Making RL Actually Work","url":"https://cameronrwolfe.substack.com/p/grpo-tricks"},{"title":"Empowering Multi-Turn Tool-Integrated Reasoning with Group Turn Policy Optimization","url":"https://arxiv.org/pdf/2511.14846"},{"title":"RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents","url":"https://arxiv.org/pdf/2602.03025"}]

Based on the search results, here's what I found about GSPO-token and related approaches:

## GSPO-token Overview

In scenarios like multi-turn RL, a finer-grained advantage adjustment than the sequence level is desired, which is addressed by introducing a token-level objective variant of GSPO, namely GSPO-token. 

GSPO-token is identical in the optimization objective, clipping condition, and theoretical gradient when advantages of all tokens in a response are set to the same value, while GSPO-token enjoys higher flexibility of adjusting the advantages per token.

## Context: Multi-Turn RL with Different Reward Signals

The broader context shows that for multi-turn tasks, variants like GTPO assign rewards and advantages per turn rather than per sequence. Recent work has proposed per-turn reward signals to improve credit assignment, with MT-GRPO normalizing rewards within rollout groups at each turn position, while GTPO applies discounted returns.

Unlike standard GRPO, which propagates the same scalar reward to all tokens or turns in a response, fine-grained variants allocate rewards or advantage signals at the token, turn, or trajectory level, often using additional shaping or normalization.

The GSPO-token variant specifically enables more granular control over advantage estimation in multi-turn reinforcement learning scenarios compared to the sequence-level approach.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b954b10b-6777-4d1b-9103-118f3f91b2ee",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "acd6bd3eff75572c3",
  "type": "user",
  "uuid": "059bbcd6-4439-4ce5-87e4-02a6608355bb",
  "sourceToolAssistantUUID": "b954b10b-6777-4d1b-9103-118f3f91b2ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-27T23:06:17.860Z_

Let me get one more important source -- the "Orchestrating Tokens and Sequences" paper that seems to discuss hybrid approaches, and the HuggingFace blog that compares GRPO, DAPO, and GSPO in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "059bbcd6-4439-4ce5-87e4-02a6608355bb",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTuryxnNVmihavyDBc52",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33fe0232-d6cb-434c-b1d2-59ad637def40",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B7wF6byRRt8HzMHETCsxrX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1359,
      "cache_creation_input_tokens": 1318,
      "cache_read_input_tokens": 32617,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1318,
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

_source line 45 · 2026-05-27T23:06:20.157Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EMoHpkwegVbAXNaddK73GW`</summary>

```json
{
  "url": "https://huggingface.co/blog/NormalUhr/grpo-to-dapo-and-gspo",
  "prompt": "Extract all technical details about GSPO from this blog post, including:\n1. Mathematical formulations and comparisons with GRPO/DAPO\n2. Any discussion of limitations of sequence-level approach\n3. Any mention of multi-objective rewards or composite reward signals\n4. Any analysis of when sequence-level clipping loses information compared to token-level\n5. Implementation details\n6. The GSPO-token variant discussion\nPlease be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33fe0232-d6cb-434c-b1d2-59ad637def40",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTuryxnNVmihavyDBc52",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e4d85fa-e590-46ae-b590-9e0a0773c573",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B7wF6byRRt8HzMHETCsxrX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1359,
      "cache_creation_input_tokens": 1318,
      "cache_read_input_tokens": 32617,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1318,
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

_source line 46 · 2026-05-27T23:06:21.816Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LzdSWwpMEedHZ9iHHisGVQ`</summary>

```json
{
  "url": "https://tolga-han.com/blog/2025/group-sequence-policy-optimization-gspo.md/",
  "prompt": "Extract all technical analysis and commentary about GSPO, especially any discussion of limitations, multi-objective rewards, composite rewards, practical considerations, and comparisons with other methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e4d85fa-e590-46ae-b590-9e0a0773c573",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTuryxnNVmihavyDBc52",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1dd77bb1-fe31-4003-9a5f-90b41fc63b27",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B7wF6byRRt8HzMHETCsxrX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1359,
      "cache_creation_input_tokens": 1318,
      "cache_read_input_tokens": 32617,
      "output_tokens": 361,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1318
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1359,
          "output_tokens": 361,
          "cache_read_input_tokens": 32617,
          "cache_creation_input_tokens": 1318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1318,
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

_source line 47 · 2026-05-27T23:06:22.143Z_

<details><summary>↩ Tool result · `toolu_01LzdSWwpMEedHZ9iHHisGVQ`</summary>

```text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1dd77bb1-fe31-4003-9a5f-90b41fc63b27",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "acd6bd3eff75572c3",
  "type": "user",
  "uuid": "3427c21a-404a-4d7a-b092-7b8004befbd9",
  "sourceToolAssistantUUID": "1dd77bb1-fe31-4003-9a5f-90b41fc63b27",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-27T23:06:37.392Z_

<details><summary>↩ Tool result · `toolu_01EMoHpkwegVbAXNaddK73GW`</summary>

````text
# Technical Details about GSPO from the Blog Post

## 1. Mathematical Formulations

### GSPO Loss Function
```
J_GSPO(θ) = E_{q∼P(Q), {o_i}_{i=1}^G ∼ π_{θ_old}(O|q)} 
[1/G ∑_{i=1}^G 1/|o_i| ∑_{t=1}^{|o_i|} 
(min(s_i(θ)A_i, clip(s_i(θ), 1-ε, 1+ε)A_i)]
```

### Sequence-Level Importance Ratio (Key Innovation)
```
s_i(θ) = (π_θ(o_i|q) / π_{θ_old}(o_i|q))^{1/|o_i|}
       = exp(1/|o_i| ∑_{t=1}^{|o_i|} log π_θ(o_{i,t}|q,o_{i,<t}) / π_{θ_old}(o_{i,t}|q,o_{i,<t}))
```

**Key Difference from GRPO:** Replaces per-token ratio `r_{i,t}(θ)` with sequence-level ratio `s_i(θ)` that is **length-normalized** and **identical for all tokens in a sequence**.

### Comparison with GRPO
GRPO uses per-token importance ratios:
```
r_{i,t}(θ) = π_θ(o_{i,t}|q,o_{i,<t}) / π_{θ_old}(o_{i,t}|q,o_{i,<t})
```

## 2. Gradient Analysis: GSPO vs GRPO

### GSPO Gradient
```
∇_θ J_GSPO(θ) = E[1/G ∑_{i=1}^G s_i(θ) A_i · 1/|o_i| ∑_{t=1}^{|o_i|} ∇_θ log π_θ(o_{i,t}|q,o_{i,<t})]
```
All tokens in a response share the same weight: `s_i(θ)A_i/|o_i|`

### GRPO Gradient
```
∇_θ J_GRPO(θ) = E[1/G ∑_{i=1}^G Â_i/|o_i| ∑_{t=1}^{|o_i|} r_{i,t}(θ) ∇_θ log π_θ(o_{i,t}|q,o_{i,<t})]
```
Weights vary by token position: `r_{i,t}(θ)A_i/|o_i|`

**Critical Finding:** GSPO achieves "consistent intra-sequence gradient weights, reduces variance between tokens" compared to GRPO's token-level variance.

## 3. Limitations of Sequence-Level Approach

The blog post acknowledges one significant limitation through implicit analysis:

### Information Loss from Clipping
- **GRPO:** Can clip individual problematic tokens, preserving other tokens' gradients
- **GSPO:** "If triggered, will clip the **entire sequence**, not just certain tokens"
- **Trade-off:** GSPO "trains with fewer effective tokens (due to more aggressive clipping) yet achieves higher training efficiency"

### Implicit Limitations Mentioned
1. **Long sequence variability:** A few volatile tokens in long sequences can affect the normalized ratio less than in token-level schemes
2. **Token-level signal nuance:** Individual tokens with extremely good/bad logits lose independent weighting

## 4. Multi-Objective Rewards or Composite Signals

**Not discussed in this blog post.** The article assumes single scalar rewards per sequence. The reward shaping discussion focuses on:
- **Overlong Reward Shaping (DAPO feature):** Soft penalties for exceeding length thresholds, not multi-objective optimization
- No mention of Pareto-style or composite reward signals

## 5. Implementation Details

### Length Normalization Mechanism
```
1/|o_i| factor applied in log-space before exponentiation to:
- Prevent extreme values from few token probability shifts
- Keep ratios on consistent scale across variable-length sequences
- Avoid length-sensitive extreme values
```

### Why Exponentiate Instead of Using Log-Differences Directly?

The blog explains this is **essential for mathematical correctness**:

```
WRONG (would break importance sampling):
E[Δ log p · A]  ← This is NOT an unbiased importance sampling correction

CORRECT:
E[exp(Δ log p) · A]  ← This maintains proper probability ratio weighting
```

The importance sampling formula fundamentally requires a **probability ratio** (≥0), not log-probability differences.

### Clipping Asymmetry in GRPO vs GSPO
- **GRPO:** For positive advantages, ratio range ≈ [0, 1.x]; for negative, [0.x, ∞) → highly asymmetric
- **GSPO:** Applies symmetric clipping to entire sequence, reducing noise accumulation in long sequences

## 6. GSPO-Token Variant Discussion

**Not discussed in this blog post.** The article does not mention a hybrid GSPO-token approach. Focus remains entirely on pure sequence-level GSPO optimization.

---

## Additional Critical Insights

### Why GSPO Solves MoE Training Instability
1. **Expert Activation Volatility Problem:** New/old policies may activate different experts, causing large probability fluctuations unrelated to optimization
2. **GSPO Solution:** By operating at sequence level, avoids reliance on per-token routing consistency and eliminates need for **Routing Replay** (recording expert activations during sampling)
3. **Practical Benefit:** Reduces engineering cost while improving stability in MoE architectures

### Variance Reduction Mechanism
The blog notes that GSPO reduces:
- **Structural bias:** Different expert activation patterns between policies
- **Token-level noise:** Accumulation of per-token ratio variance over long sequences
- **Clipping asymmetry noise:** More predictable behavior than GRPO's asymmetric [0.x, ∞) range

### Performance Trade-off
- **Fewer effective tokens** processed during training (due to more aggressive sequence-level clipping)
- **Higher training efficiency** despite fewer tokens (better signal-to-noise ratio)
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e4d85fa-e590-46ae-b590-9e0a0773c573",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "acd6bd3eff75572c3",
  "type": "user",
  "uuid": "6f3382b8-07a3-4f96-adce-e398fb4b8904",
  "sourceToolAssistantUUID": "0e4d85fa-e590-46ae-b590-9e0a0773c573",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-27T23:08:12.696Z_

I now have comprehensive information. Let me compile the complete research findings.

---

# GSPO (Group Sequence Policy Optimization) -- Deep Research Report

**Paper:** "Group Sequence Policy Optimization," arXiv:2507.18071 (v1: July 24, 2025; v2: July 28, 2025)
**Authors:** Chujie Zheng, Shixuan Liu, Mingze Li, Xiong-Hui Chen, Bowen Yu, Chang Gao, Kai Dang, Yuqiong Liu, Rui Men, An Yang, Jingren Zhou, Junyang Lin (Qwen Team, Alibaba Inc.)

---

## 1. GSPO's Core Mechanism: Sequence-Level vs Token-Level Importance Ratios

### The Problem with GRPO's Token-Level Ratios

GRPO uses per-token importance ratios:

```
w_{i,t}(theta) = pi_theta(y_{i,t} | x, y_{i,&lt;t}) / pi_theta_old(y_{i,t} | x, y_{i,&lt;t})
```

The paper identifies this as a **fundamental misapplication of importance sampling**. The key argument: importance sampling requires averaging over *multiple samples* from the behavior distribution to correct for distributional mismatch. But at each token position `t`, there is only a *single sample* `y_{i,t}` from each next-token distribution. This means the token-level importance weight "fails to perform the intended distribution-correction role" and instead introduces high-variance noise that:
- Accumulates over long sequences
- Is exacerbated by the clipping mechanism
- Can lead to irreversible model collapse

The paper states a core principle: **"the unit of optimization objective should match the unit of reward."** Since rewards are granted to entire sequences, token-level off-policy correction is misaligned.

### GSPO's Sequence-Level Solution

GSPO defines the importance ratio at the sequence level with length normalization:

```
s_i(theta) = (pi_theta(y_i|x) / pi_theta_old(y_i|x))^{1/|y_i|}
           = exp( (1/|y_i|) * sum_{t=1}^{|y_i|} log[pi_theta(y_{i,t}|x,y_{i,&lt;t}) / pi_theta_old(y_{i,t}|x,y_{i,&lt;t})] )
```

The full GSPO objective:

```
J_GSPO(theta) = E[ (1/G) * sum_{i=1}^{G} min(s_i(theta) * A_hat_i, clip(s_i(theta), 1-eps, 1+eps) * A_hat_i) ]
```

With group-relative advantage estimation:

```
A_hat_i = (r(x, y_i) - mean({r(x, y_j)})) / std({r(x, y_j)})
```

**Length normalization** is critical: without it, likelihood changes of a few tokens cause dramatic fluctuations in the sequence-level ratio, and responses of different lengths would require different clipping ranges.

### Gradient-Level Difference

The key distinction at the gradient level:

- **GRPO gradient**: Each token's gradient `nabla log pi(y_{i,t})` is weighted by its *own individual* importance ratio `w_{i,t}(theta)`. These unequal weights range in `(0, 1+eps]` for positive advantages or `[1-eps, infinity)` for negative advantages -- highly asymmetric and noisy.

- **GSPO gradient**: ALL tokens in a response share the *same* weight `s_i(theta)`. The gradient is:
  ```
  (pi_theta(y_i|x) / pi_theta_old(y_i|x))^{1/|y_i|} * A_hat_i * (1/|y_i|) * sum_t nabla log pi_theta(y_{i,t})
  ```
  This eliminates token-level weighting variance entirely.

---

## 2. Why GSPO Solves MoE Routing Instability

### The MoE Problem

In MoE models like Qwen3-30B-A3B (48 layers), the paper reports that **after each RL gradient update, roughly 10% of the experts activated under the new policy are different from those under the old policy** for the same rollout sample. This "expert-activation volatility" means:

- The token-level probabilities `pi_theta(y_{i,t}|...)` and `pi_theta_old(y_{i,t}|...)` are computed by **different sub-networks** (different expert combinations)
- The ratios `w_{i,t}` therefore "fluctuate drastically" -- not because the model changed its beliefs, but because it is routing through entirely different experts
- This noise is structural, not informational, and it compounds across tokens in long sequences

### The Previous Workaround: Routing Replay

Before GSPO, the Qwen team used "Routing Replay": caching which experts were activated under `pi_theta_old` and forcing `pi_theta` to use the same expert routing when computing importance ratios. This ensured both probabilities used the same activated network, restoring ratio stability. However, Routing Replay:
- Incurred additional memory and communication overhead
- Limited the actual capacity of the MoE model (prevented it from using its natural routing)
- Was shown to be **essential** for GRPO convergence on MoE (without it, GRPO fails to converge)

### GSPO's Natural Solution

GSPO resolves this **without any workaround** because:
- The sequence-level likelihood `pi_theta(y_i|x)` is an aggregate quantity
- While individual token probabilities fluctuate due to expert routing changes, the overall sequence likelihood remains stable because "the MoE model always maintains its language modeling capability"
- GSPO is "not sensitive to the individual token likelihood" -- it only uses the aggregate
- This allows the model to "leverage its full capacity without artificial constraints" on routing

---

## 3. Interaction with Multi-Objective / Multi-Component Rewards

### What the Paper Says

The paper does **not** directly discuss multi-objective or multi-component rewards. The reward `r(x, y_i)` throughout the paper is treated as a single scalar in `[0,1]`. The advantage estimation is a single group-normalized value per sequence.

### The GSPO-token Variant: The Pathway to Per-Component Signals

The paper introduces **GSPO-token** (Section 4.3) specifically for scenarios requiring "finer-grained advantage adjustment than the sequence level," with multi-turn RL cited as the motivating example:

```
J_GSPO-token(theta) = E[ (1/G) sum_i (1/|y_i|) sum_t min(s_{i,t}(theta) * A_hat_{i,t}, clip(s_{i,t}(theta), 1-eps, 1+eps) * A_hat_{i,t}) ]
```

Where the token-level ratio is defined using a stop-gradient trick:

```
s_{i,t}(theta) = sg[s_i(theta)] * pi_theta(y_{i,t}|...) / sg[pi_theta(y_{i,t}|...)]
```

Key properties:
- `s_{i,t}(theta)` is **numerically equal** to `s_i(theta)` (since the token ratio term has value 1)
- The **clipping condition** is identical to standard GSPO (based on `s_i(theta)`)
- But the **gradient** allows per-token advantage differentiation: different `A_hat_{i,t}` values for different tokens
- When all token advantages are set equal (`A_hat_{i,t} = A_hat_i`), GSPO-token reduces exactly to standard GSPO

**This is directly relevant to multi-component rewards**: you could assign different advantage values to different tokens (or turns) based on different reward components, while still benefiting from GSPO's sequence-level importance ratio for stability. However, the paper does not explicitly discuss this application.

### Implications for Composite Rewards

Based on the algorithm design, here is the analysis:

1. **Standard GSPO with composite rewards as a single scalar**: If you combine multiple reward components into a single `r(x, y_i)` (e.g., weighted sum of correctness, format, safety), GSPO works identically -- the advantage is computed from this composite scalar. The sequence-level clipping means you cannot separately control the policy gradient for each reward component, since the entire sequence is either clipped or not based on the aggregate importance ratio.

2. **GSPO-token for per-component credit assignment**: If different tokens or turns correspond to different reward aspects (e.g., reasoning quality for thinking tokens, format compliance for output tokens), GSPO-token allows assigning different `A_hat_{i,t}` values to different tokens while retaining the sequence-level importance ratio and clipping. This preserves MoE stability while enabling finer-grained reward attribution.

3. **What you cannot do with standard GSPO**: Extract per-component gradients with independent clipping per component. The clipping is always at the sequence level based on overall policy divergence, not per-component divergence.

---

## 4. Sequence-Level Clipping Details

### Clipping Mechanism

The clipping operates on `s_i(theta)`, constraining it to `[1-eps, 1+eps]`. When the importance ratio for a sequence falls outside this range, the **entire sequence** is excluded from gradient estimation. This is fundamentally different from GRPO where individual tokens can be clipped independently.

### Clipping Hyperparameters

The clipping ranges differ by orders of magnitude from GRPO due to the distinct definitions:
- **GSPO**: left clipping = 3e-4, right clipping = 4e-4
- **GRPO**: left clipping = 0.2, right clipping = 0.27

This makes sense because `s_i(theta)` is a length-normalized geometric mean of token ratios, so it stays very close to 1.

### The "Curious Observation"

GSPO clips **two orders of magnitude more tokens** than GRPO (measured by fraction of clipped tokens), yet achieves superior training efficiency. The paper interprets this as evidence that "GRPO's token-level gradient estimates are inherently noisy and inefficient for sample exploitation." In other words, GRPO's un-clipped tokens carry so much noise that GSPO's cleaner (but fewer) gradient signals are more useful.

---

## 5. Experimental Results: GSPO > GRPO on MoE

### Setup
- Model: Cold-start fine-tuned from Qwen3-30B-A3B-Base (MoE model)
- Each batch of rollout data partitioned into 4 mini-batches for gradient updates
- GRPO required Routing Replay for convergence; GSPO did not

### Benchmarks
- **AIME'24**: Average Pass@1 over 32 samplings
- **LiveCodeBench** (202410-202502): Average Pass@1 over 8 samplings
- **CodeForces**: Elo Rating

### Key Findings (from training curves, Figure 1 in the paper)
1. GSPO training proceeds **stably throughout** -- no collapse episodes
2. GSPO delivers **continuous performance improvement** through increasing training compute, regularly updating query sets, and extending generation length
3. GSPO demonstrates **"remarkably higher training efficiency"** than GRPO: better training accuracy and benchmark performance under the same training compute and consumed queries
4. GRPO **without Routing Replay fails to converge** on MoE models (Figure 3)
5. GRPO **with Routing Replay** converges but is less efficient than GSPO

The paper does not provide exact numerical benchmark scores in tables -- results are shown as training curves. The main claim is about relative efficiency and stability rather than specific point estimates.

### Production Validation
GSPO was successfully applied to the RL training of the latest Qwen3 models (including Qwen3-235B-A22B), demonstrating its scalability to production-scale training.

---

## 6. Discussion of GSPO with Composite/Multi-Objective Rewards

### What Exists in the Literature

The paper itself does **not** discuss composite or multi-objective rewards. Across all the blog posts, reviews, and discussions I found, **none** address this topic specifically for GSPO. The entire treatment assumes a single scalar reward per sequence.

### What Can Be Inferred from the Algorithm

**For standard GSPO:**
- You can feed in any scalar reward, including one that is a weighted sum of multiple components
- The clipping is purely based on policy divergence (the importance ratio), not on reward magnitude, so using a composite reward does not change the clipping behavior
- You **lose the ability** to independently control how much each reward component drives the gradient, since there is a single advantage `A_hat_i` per sequence and a single clipping decision per sequence

**For GSPO-token:**
- This variant was explicitly designed for multi-turn RL where different parts of a sequence merit different advantages
- You could assign per-token advantages derived from different reward components
- The clipping is still sequence-level (based on `s_i(theta)`), so you cannot independently clip based on individual reward component divergence
- But you **can** decompose the reward signal into per-token advantages while retaining the stability benefits

**A potential approach for multi-component rewards with GSPO:**
1. Compute a composite reward: `r(x, y_i) = w1*r1(x,y_i) + w2*r2(x,y_i) + ...`
2. Use standard GSPO with this composite scalar
3. Or, if different tokens/turns correspond to different reward aspects, use GSPO-token with per-token advantages derived from the relevant reward component

---

## 7. Infrastructure Benefits

GSPO also simplifies RL training infrastructure:
- Since GSPO uses only sequence-level likelihoods (not per-token), it is **more tolerant of precision discrepancies** between training engines (Megatron) and inference engines (SGLang, vLLM)
- This makes it possible to **directly use likelihoods from inference engines** without recomputation by the training engine
- This is especially beneficial for partial rollout, multi-turn RL, and disaggregated training-inference frameworks
- GSPO has been integrated into HuggingFace TRL

---

## Summary of Answers to Your Questions

| Question | Answer |
|----------|--------|
| GSPO's mechanism | Sequence-level importance ratio (length-normalized geometric mean of token ratios), sequence-level clipping, sequence-level advantage. All tokens in a response share the same gradient weight. |
| Why it solves MoE routing instability | Token-level ratios depend on which experts are activated; with ~10% expert changes per gradient step in MoE, token ratios become noisy. Sequence-level likelihood is stable because overall language modeling capability is preserved despite routing changes. Eliminates need for Routing Replay. |
| Interaction with multi-component rewards | Not directly addressed in the paper. Standard GSPO uses a single scalar reward per sequence. GSPO-token variant allows per-token advantage differentiation, which could be used for multi-component credit assignment, but this application is not explicitly discussed. |
| Sequence-level clipping and per-component signals | Standard GSPO clips entire sequences, so per-component reward signals cannot be independently clipped. GSPO-token preserves per-token advantage differences but still uses sequence-level clipping. You can still feed composite rewards into the advantage computation. |
| Experimental results GSPO > GRPO on MoE | GSPO shows remarkably higher training efficiency on Qwen3-30B-A3B-Base across AIME'24, LiveCodeBench, and CodeForces. GRPO requires Routing Replay to even converge on MoE; GSPO does not. GSPO clips 100x more tokens yet still outperforms GRPO. |
| GSPO with composite/multi-objective rewards | No direct discussion exists anywhere in the paper or community. It is an open area. GSPO-token is the natural extension point for this use case. |

Sources:
- [GSPO Paper (arXiv)](https://arxiv.org/abs/2507.18071)
- [GSPO Paper HTML Version](https://arxiv.org/html/2507.18071v2)
- [Qwen Team Official Blog Post on GSPO](https://qwenlm.github.io/blog/gspo/)
- [HuggingFace Paper Page](https://huggingface.co/papers/2507.18071)
- [From GRPO to DAPO and GSPO (HuggingFace Blog)](https://huggingface.co/blog/NormalUhr/grpo-to-dapo-and-gspo)
- [Paper Review by Andrey Lukyanenko](https://andlukyane.com/blog/paper-review-gspo)
- [GSPO vs GRPO: RL for MoE Models (Kaitchup)](https://kaitchup.substack.com/p/gspo-vs-grpo-reinforcement-learning)
- [RLHF Algorithms: PPO, GRPO, GSPO (Medium)](https://medium.com/@hongjianzou/rlhf-algorithms-ppo-grpo-gspo-differences-trade-offs-and-use-cases-241d003d806d)
- [Emergent Mind GSPO Topic Page](https://www.emergentmind.com/papers/2507.18071)
- [MarkTechPost Coverage](https://www.marktechpost.com/2025/08/07/alibaba-introduces-group-sequence-policy-optimization-gspo-an-efficient-reinforcement-learning-algorithm-that-powers-the-qwen3-models/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f3382b8-07a3-4f96-adce-e398fb4b8904",
  "isSidechain": true,
  "agentId": "acd6bd3eff75572c3",
  "requestId": "req_011CbTutgSPPigQDFZNfGf24",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b6f26f2-7795-449b-9d00-4b60daaf90f1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018uh6wF4pYPXKR95Et42icx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 3349,
      "cache_read_input_tokens": 33935,
      "output_tokens": 4360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3349
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 4360,
          "cache_read_input_tokens": 33935,
          "cache_creation_input_tokens": 3349,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3349,
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
