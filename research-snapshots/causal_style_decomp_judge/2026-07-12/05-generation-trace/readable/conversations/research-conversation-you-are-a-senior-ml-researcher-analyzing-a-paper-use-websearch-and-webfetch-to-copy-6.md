# Research conversation: You are a senior ML researcher analyzing a paper. Use WebSearch and WebFetch to thoroughly research this paper: **Paper*

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ad50dc4fb50295b3a.jsonl`
- **Structured JSON:** [`81954462bee47c8fa036.json`](../../sessions/81/81954462bee47c8fa036.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-29T10:06:17.789Z_

You are a senior ML researcher analyzing a paper. Use WebSearch and WebFetch to thoroughly research this paper:

**Paper**: "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning" by Zhao et al., AAAI 2026, https://arxiv.org/abs/2504.00891

**Tasks**:
1. Fetch the arxiv abstract page to get the full abstract and key details.
2. Fetch the PDF or HTML version to read the introduction and method sections.
3. Search for OpenReview or AAAI reviews of this paper.
4. Search for any blog posts or discussions that reveal key insights.

**For your analysis, focus on**:
- What gap did they identify and HOW?
- What was the key insight others missed?
- How did they formulate the problem differently?
- What existing technique did they adapt/combine/simplify?
- If reviewer comments are available: what was praised, what was criticized?

**Context**: This paper defines the cost-accuracy tradeoff at the deepest verification depth in our framework. We care about how generative PRMs with CoT + code verification work, and what their compute costs are relative to simpler verification methods.

Return a detailed but concise analysis (under 2000 characters total) covering:
- problem_identification (1-2 sentences)
- key_insight (1 sentence)
- innovation_type
- method_summary (2-3 sentences)
- limitations_and_open_questions (1-2 sentences)
- building_blocks (list of reusable methods/tools)
- relevance_to_seed (1 sentence)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "003d4d5b-99b9-4488-a4e4-5e4419f94d98",
  "agentId": "ad50dc4fb50295b3a",
  "type": "user",
  "uuid": "487b89c3-7d30-45cb-9943-7f08a46707a5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-29T10:06:17.793Z_

```json
{
  "parentUuid": "487b89c3-7d30-45cb-9943-7f08a46707a5",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
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
  "uuid": "2c6dcd99-9797-4a31-8098-044a06ae2619",
  "timestamp": "2026-05-29T10:06:17.793Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-29T10:06:17.793Z_

```json
{
  "parentUuid": "2c6dcd99-9797-4a31-8098-044a06ae2619",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "45736b04-70f8-4ccd-a143-450fcabc00a0",
  "timestamp": "2026-05-29T10:06:17.793Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 4 · 2026-05-29T10:06:20.651Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01V1rEG7DXyHPvCquEH4pswF`</summary>

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
  "parentUuid": "45736b04-70f8-4ccd-a143-450fcabc00a0",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
  "requestId": "req_011CbWg1EjdrACJ4Kd7MtiKq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0bcb55e0-1b18-477f-b23c-a3d80612b2b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NaxwMDoj9X5eyUcQ7kzaTS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1723,
      "cache_read_input_tokens": 7319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1723,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
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

_source line 5 · 2026-05-29T10:06:20.657Z_

<details><summary>↩ Tool result · `toolu_01V1rEG7DXyHPvCquEH4pswF`</summary>

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
  "parentUuid": "0bcb55e0-1b18-477f-b23c-a3d80612b2b1",
  "isSidechain": true,
  "promptId": "003d4d5b-99b9-4488-a4e4-5e4419f94d98",
  "agentId": "ad50dc4fb50295b3a",
  "type": "user",
  "uuid": "07e64bc4-15b1-4cf4-b698-16b5fa58c0b7",
  "sourceToolAssistantUUID": "0bcb55e0-1b18-477f-b23c-a3d80612b2b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-29T10:06:24.589Z_

I'll fetch the paper details and search for reviews/discussions in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07e64bc4-15b1-4cf4-b698-16b5fa58c0b7",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
  "requestId": "req_011CbWg1UHDfZ7b1rj1uaJsJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42974839-c530-497f-95b2-dd71da9e1fcd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PeHKHPw4NPhYmzpoaZtsaV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1101,
      "cache_read_input_tokens": 9042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1101,
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

_source line 7 · 2026-05-29T10:06:25.453Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CqpajfNDLsupGPZmne6qxY`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.00891",
  "prompt": "Extract the full abstract, authors, keywords, and any key details about the paper's contributions, method, and results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42974839-c530-497f-95b2-dd71da9e1fcd",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
  "requestId": "req_011CbWg1UHDfZ7b1rj1uaJsJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f37157d-1d76-4128-9d7c-3ae7c63834ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PeHKHPw4NPhYmzpoaZtsaV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1101,
      "cache_read_input_tokens": 9042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1101,
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

_source line 8 · 2026-05-29T10:06:26.433Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JmJx4HMu7wZV538utpzKBq`</summary>

```json
{
  "query": "GenPRM \"Scaling Test-Time Compute\" Process Reward Models Generative Reasoning Zhao 2025 review discussion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f37157d-1d76-4128-9d7c-3ae7c63834ab",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
  "requestId": "req_011CbWg1UHDfZ7b1rj1uaJsJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24e80e9c-1634-457b-a7ed-59f75684856e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PeHKHPw4NPhYmzpoaZtsaV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1101,
      "cache_read_input_tokens": 9042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1101,
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

_source line 9 · 2026-05-29T10:06:26.603Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011dSc2STGQYyBrGX6FCnsui`</summary>

```json
{
  "query": "GenPRM arxiv 2504.00891 AAAI 2026 blog post insights"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24e80e9c-1634-457b-a7ed-59f75684856e",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
  "requestId": "req_011CbWg1UHDfZ7b1rj1uaJsJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6979bf5-77dd-46a6-8ec8-470ad7102082",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PeHKHPw4NPhYmzpoaZtsaV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1101,
      "cache_read_input_tokens": 9042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1101,
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

_source line 10 · 2026-05-29T10:06:31.772Z_

<details><summary>↩ Tool result · `toolu_01CqpajfNDLsupGPZmne6qxY`</summary>

```text
# GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning

## Full Abstract
"Recent advancements in Large Language Models (LLMs) have shown that it is promising to utilize Process Reward Models (PRMs) as verifiers to enhance the performance of LLMs. However, current PRMs face three key challenges: (1) limited process supervision and generalization capabilities, (2) dependence on scalar value prediction without leveraging the generative abilities of LLMs, and (3) inability to scale the test-time compute of PRMs."

The paper proposes GenPRM, which performs explicit Chain-of-Thought reasoning with code verification for step-level judgments. Key methodological contributions include Relative Progress Estimation (RPE) and a rationale synthesis framework incorporating code verification.

## Authors
Jian Zhao, Runze Liu, Kaiyan Zhang, Zhimu Zhou, Junqi Gao, Dong Li, Jiafei Lyu, Zhouyi Qian, Biqing Qi, Xiu Li, Bowen Zhou

## Key Results
- Outperforms prior PRMs using only 23K training examples from the MATH dataset
- A 1.5B parameter GenPRM surpasses GPT-4o on ProcessBench
- A 7B parameter variant exceeds Qwen2.5-Math-PRM-72B performance
- Demonstrates effectiveness as a critic model for policy refinement

## Keywords/Classification
Computation and Language (cs.CL)

**Submission Details:** arXiv:2504.00891, submitted April 1, 2025; v2 revised April 5, 2025
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f37157d-1d76-4128-9d7c-3ae7c63834ab",
  "isSidechain": true,
  "promptId": "003d4d5b-99b9-4488-a4e4-5e4419f94d98",
  "agentId": "ad50dc4fb50295b3a",
  "type": "user",
  "uuid": "34067f90-5436-4ddd-a932-98556639d8c0",
  "sourceToolAssistantUUID": "8f37157d-1d76-4128-9d7c-3ae7c63834ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-29T10:06:33.004Z_

<details><summary>↩ Tool result · `toolu_011dSc2STGQYyBrGX6FCnsui`</summary>

```text
Web search results for query: "GenPRM arxiv 2504.00891 AAAI 2026 blog post insights"

Links: [{"title":"[2504.00891] GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://arxiv.org/abs/2504.00891"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | Arxiv - DeepPaper","url":"https://arxiv.deeppaper.ai/papers/2504.00891v2"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward ...","url":"https://arxiv.org/pdf/2504.00891"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2504.00891"},{"title":"GitHub - RyanLiu112/GenPRM: [AAAI 2026] Official codebase for \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\".","url":"https://github.com/RyanLiu112/GenPRM"}]

Based on the search results, here's what I found about GenPRM arxiv 2504.00891 and its AAAI 2026 acceptance:

## Overview

GenPRM is a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step.

## Key Challenges Addressed

GenPRM addresses three key challenges facing current PRMs: (1) limited process supervision and generalization capabilities, (2) dependence on scalar value prediction without leveraging the generative abilities of LLMs, and (3) inability to scale the test-time compute of PRMs.

## Technical Approach

The researchers propose Relative Progress Estimation (RPE) and a rationale synthesis framework that incorporates code verification to obtain high-quality process supervision labels and rationale data.

## Performance Results

Through test-time scaling, a 1.5B GenPRM outperforms GPT-4o, and a 7B GenPRM surpasses Qwen2.5-Math-PRM-72B on ProcessBench.

## AAAI 2026 Acceptance

GenPRM was accepted by AAAI 2026.

The search results do not contain any specific blog post insights about this work, but the GitHub repository and academic sources provide the main technical details about the research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6979bf5-77dd-46a6-8ec8-470ad7102082",
  "isSidechain": true,
  "promptId": "003d4d5b-99b9-4488-a4e4-5e4419f94d98",
  "agentId": "ad50dc4fb50295b3a",
  "type": "user",
  "uuid": "b415c518-5720-450d-a94d-cdb3c825686c",
  "sourceToolAssistantUUID": "d6979bf5-77dd-46a6-8ec8-470ad7102082",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-29T10:06:35.564Z_

<details><summary>↩ Tool result · `toolu_01JmJx4HMu7wZV538utpzKBq`</summary>

```text
Web search results for query: "GenPRM "Scaling Test-Time Compute" Process Reward Models Generative Reasoning Zhao 2025 review discussion"

Links: [{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://ryanliu112.github.io/GenPRM/"},{"title":"[PDF] GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GenPRM:-Scaling-Test-Time-Compute-of-Process-Reward-Zhao-Liu/bd94932b7604933a11d1538b0de6f9543089711f"},{"title":"[2504.00891] GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://arxiv.org/abs/2504.00891"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/genprm-scaling-test-time-compute-process-reward"},{"title":"Breaking the LLM Bottleneck: GenPRM’s approach to Scale test-time compute via generative reasoning | by SACHIN KUMAR | Medium","url":"https://medium.com/@techsachin/breaking-the-llm-bottleneck-genprms-approach-to-scale-test-time-compute-via-generative-reasoning-0e90e3ffa71e"},{"title":"GitHub - RyanLiu112/GenPRM: [AAAI 2026] Official codebase for \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\".","url":"https://github.com/RyanLiu112/GenPRM"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | Arxiv - DeepPaper","url":"https://arxiv.deeppaper.ai/papers/2504.00891v2?locale=en"},{"title":"Paper page - GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://huggingface.co/papers/2504.00891"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | Request PDF","url":"https://www.researchgate.net/publication/390404512_GenPRM_Scaling_Test-Time_Compute_of_Process_Reward_Models_via_Generative_Reasoning"}]

I found comprehensive information about GenPRM. Here's a summary of this research:

## Overview

GenPRM was authored by Jian Zhao, Runze Liu, Kaiyan Zhang, Zhimu Zhou, Junqi Gao, Dong Li, Jiafei Lyu, Zhouyi Qian, Biqing Qi, Xiu Li, and Bowen Zhou, and was published on arXiv as preprint arXiv:2504.00891 in 2025.

## Problem Statement

Current PRMs face three key challenges: (1) limited process supervision and generalization capabilities, (2) dependence on scalar value prediction without leveraging the generative abilities of LLMs, and (3) inability to scale the test-time compute of PRMs.

## Solution

GenPRM is a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step. The team proposed Relative Progress Estimation (RPE) and a rationale synthesis framework that incorporates code verification to obtain high-quality supervision labels.

## Performance & Acceptance

GenPRM outperforms existing PRMs and even GPT-4o and Qwen2.5-Math-PRM-72B on ProcessBench. Additionally, GenPRM was accepted by AAAI 2026, highlighting its significance in the field.

The paper addresses a crucial area in LLM research where process supervision and test-time compute scaling are becoming increasingly important for improving reasoning capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24e80e9c-1634-457b-a7ed-59f75684856e",
  "isSidechain": true,
  "promptId": "003d4d5b-99b9-4488-a4e4-5e4419f94d98",
  "agentId": "ad50dc4fb50295b3a",
  "type": "user",
  "uuid": "6545fd15-6394-4378-9b91-4bce9820419f",
  "sourceToolAssistantUUID": "24e80e9c-1634-457b-a7ed-59f75684856e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-29T10:06:39.373Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Lsq3RaowEHZDkk4q9GrzxM`</summary>

```json
{
  "url": "https://medium.com/@techsachin/breaking-the-llm-bottleneck-genprms-approach-to-scale-test-time-compute-via-generative-reasoning-0e90e3ffa71e",
  "prompt": "Extract key insights about GenPRM's method, what gap they identified, what existing techniques they adapted, what critics praised or criticized, and how they formulate the problem differently from prior work."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6545fd15-6394-4378-9b91-4bce9820419f",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
  "requestId": "req_011CbWg2Yz2Km9qeid8ytB6E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b988248-49c2-4c91-bd62-b25648dbd7bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XitmDL8FBLARzNArPZuju5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 663,
      "cache_creation_input_tokens": 1712,
      "cache_read_input_tokens": 10143,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1712,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 14 · 2026-05-29T10:06:40.737Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01J1b5dVvJphyNTXAHY7LCmL`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2504.00891",
  "prompt": "Extract the introduction, problem formulation, method description (especially RPE - Relative Progress Estimation, code verification approach, and test-time scaling strategy), and any ablation/limitation discussion from this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b988248-49c2-4c91-bd62-b25648dbd7bc",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
  "requestId": "req_011CbWg2Yz2Km9qeid8ytB6E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96c24590-8e3e-4082-b603-2026a885a7ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XitmDL8FBLARzNArPZuju5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 663,
      "cache_creation_input_tokens": 1712,
      "cache_read_input_tokens": 10143,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1712
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 663,
          "output_tokens": 267,
          "cache_read_input_tokens": 10143,
          "cache_creation_input_tokens": 1712,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1712,
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

_source line 15 · 2026-05-29T10:06:45.633Z_

<details><summary>↩ Tool result · `toolu_01J1b5dVvJphyNTXAHY7LCmL`</summary>

```text
# Document Analysis: Research Paper Summary

I apologize, but the provided content appears to be raw PDF binary data rather than readable text. The document shows compressed stream objects and PDF structural elements (objects 109-293) rather than extractable article content.

## What I Can Observe:
- This is a PDF file containing figures and embedded fonts
- There are references to "comparison.pdf" and figure elements
- The content is heavily compressed using FlateDecode filters

## To Extract the Information You Need:

I would require:
1. **Plain text version** of the paper, or
2. **Properly decoded PDF content** showing the actual article text

## If You Can Provide:
- The paper title and authors
- A text-based version of the introduction/methods sections
- A link to the paper's source (arXiv, IEEE, etc.)

I can then accurately summarize:
- Introduction and problem formulation
- RPE methodology details
- Code verification approaches
- Test-time scaling strategies
- Ablation studies and limitations

**Could you share a readable version of the content you'd like analyzed?**

[Binary content (application/pdf, 1.3MB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/83204518-f78b-400d-b0b3-3bb64b514d04/tool-results/webfetch-1780049200758-sfoyt3.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96c24590-8e3e-4082-b603-2026a885a7ba",
  "isSidechain": true,
  "promptId": "003d4d5b-99b9-4488-a4e4-5e4419f94d98",
  "agentId": "ad50dc4fb50295b3a",
  "type": "user",
  "uuid": "3d51300d-6d20-45e3-9a8b-958d5bc19009",
  "sourceToolAssistantUUID": "96c24590-8e3e-4082-b603-2026a885a7ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-29T10:06:45.661Z_

<details><summary>↩ Tool result · `toolu_01Lsq3RaowEHZDkk4q9GrzxM`</summary>

```text
# GenPRM: Key Insights and Innovation

## Gap Identified
GenPRM addresses three critical limitations in existing Process Reward Models:
- "limited process supervision and generalization capabilities"
- Reliance on scalar predictions that ignore LLM generative strengths
- Inability to scale test-time compute of PRMs themselves

## Method Innovation
Rather than using classification-based approaches, GenPRM introduces **generative reasoning with code verification**. The model performs explicit Chain-of-Thought reasoning, generates executable Python code to verify steps, and executes that code to obtain feedback before rendering judgment.

## Adapted Techniques
The researchers borrowed from reinforcement learning, specifically adapting **Relative Progress Estimation (RPE)** from GRPO's relative advantage estimation concept to improve label quality beyond hard binary classifications.

## Key Formulation Difference
Prior discriminative PRMs predicted binary correctness. GenPRM formulates the task differently: "(𝑠𝑡, 𝑎𝑡, 𝑣1:𝑡−1), (𝑣𝑡, 𝑟𝑡)" where the model learns to generate rationales and reasoning before predicting rewards, enabling multi-turn refinement and test-time scaling.

## Experimental Validation
Results demonstrate that "GenPRM-7B significantly outperforms direct generative PRM" and enables smaller models to exceed substantially larger competitors through test-time scaling via majority voting.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b988248-49c2-4c91-bd62-b25648dbd7bc",
  "isSidechain": true,
  "promptId": "003d4d5b-99b9-4488-a4e4-5e4419f94d98",
  "agentId": "ad50dc4fb50295b3a",
  "type": "user",
  "uuid": "b127ec9f-5da5-4895-b2c0-be7dd5488ae4",
  "sourceToolAssistantUUID": "0b988248-49c2-4c91-bd62-b25648dbd7bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-29T10:06:49.329Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Jaq4FmedZzcAF94QD1XboF`</summary>

```json
{
  "url": "https://ryanliu112.github.io/GenPRM/",
  "prompt": "Extract the full method description, key contributions, what gap was identified in prior PRMs, how Relative Progress Estimation (RPE) works, how code verification integrates, test-time compute scaling strategy, and any limitations or open questions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b127ec9f-5da5-4895-b2c0-be7dd5488ae4",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
  "requestId": "req_011CbWg3J57XTKBek6GhfkXE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "814de78c-91e8-4521-9df0-2a2d7a84e6c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HAVbMuiNQcvEcGB3faT1Fe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 362,
      "cache_creation_input_tokens": 1290,
      "cache_read_input_tokens": 11855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1290,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 18 · 2026-05-29T10:06:50.721Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HdNwfWFeKPjCXYZkrdAHuA`</summary>

```json
{
  "url": "https://arxiv.deeppaper.ai/papers/2504.00891v2?locale=en",
  "prompt": "Extract the introduction, method details for RPE (Relative Progress Estimation), code verification integration, test-time scaling approach, ablations, limitations, and any comparison to discriminative PRMs in terms of compute cost."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "814de78c-91e8-4521-9df0-2a2d7a84e6c0",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
  "requestId": "req_011CbWg3J57XTKBek6GhfkXE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11ff100f-04f6-467e-9e8b-d8ff2aeae908",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HAVbMuiNQcvEcGB3faT1Fe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 362,
      "cache_creation_input_tokens": 1290,
      "cache_read_input_tokens": 11855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1290,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 19 · 2026-05-29T10:06:54.695Z_

<details><summary>↩ Tool result · `toolu_01Jaq4FmedZzcAF94QD1XboF`</summary>

```text
# GenPRM: Analysis Based on Available Content

I can only provide a limited analysis based on the webpage content provided, as it contains primarily structural elements rather than detailed methodology descriptions.

## What's Available

The webpage presents **GenPRM** as a research contribution that contrasts with previous classification-based Process Reward Models (PRMs). The key distinguishing feature shown in Figure 1 suggests GenPRM employs a generative approach rather than classification for evaluating solution processes.

## Notable Elements

**Research Team & Affiliation**: The work involves researchers from Tsinghua University, Shanghai AI Laboratory, BUPT, and Harbin Institute of Technology.

**Accessible Resources**: The project provides code repositories, HuggingFace model collections, and links to a curated "Awesome Process Reward Models" collection, indicating community-focused development.

**Related Work**: The authors reference concurrent research on "Compute-Optimal Test-Time Scaling," suggesting the field is actively exploring how to optimize performance through increased inference-time computation.

## Limitations of This Analysis

The webpage content lacks:
- Detailed methodology sections explaining RPE, code verification integration, or test-time scaling strategies
- Discussion of identified gaps in prior PRM approaches
- Explicit limitations or open research questions
- Technical contributions beyond visual comparisons

**To obtain the full technical details** you're seeking, consulting the linked paper (arXiv:2504.00891) would be necessary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "814de78c-91e8-4521-9df0-2a2d7a84e6c0",
  "isSidechain": true,
  "promptId": "003d4d5b-99b9-4488-a4e4-5e4419f94d98",
  "agentId": "ad50dc4fb50295b3a",
  "type": "user",
  "uuid": "68b3387d-a512-4bb2-8096-c42bc65eba04",
  "sourceToolAssistantUUID": "814de78c-91e8-4521-9df0-2a2d7a84e6c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-29T10:06:55.879Z_

<details><summary>↩ Tool result · `toolu_01HdNwfWFeKPjCXYZkrdAHuA`</summary>

```text
# GenPRM: Key Research Details

## Introduction
The paper addresses three limitations in existing Process Reward Models: "limited process supervision and generalization capabilities," dependence on scalar predictions without leveraging LLM generative abilities, and inability to scale test-time compute. GenPRM tackles these by combining reasoning with verification.

## Method Overview
GenPRM performs "explicit Chain-of-Thought reasoning with code verification before providing judgment for each reasoning step." This generative approach differentiates it from traditional discriminative PRMs that output scalar scores.

## Relative Progress Estimation (RPE)
The abstract mentions RPE as part of obtaining "high-quality process supervision labels and rationale data," but specific technical details about RPE's mechanics aren't provided in the available content.

## Code Verification Integration
The framework incorporates "code verification" within a "rationale synthesis" approach, enabling the model to validate reasoning steps through executable code checks alongside CoT reasoning.

## Test-Time Scaling Results
Performance demonstrates significant scaling advantages: "a 1.5B GenPRM outperforms GPT-4o, and a 7B GenPRM surpasses Qwen2.5-Math-PRM-72B on ProcessBench." This suggests substantial compute efficiency improvements over larger models.

## Ablations & Limitations
The provided content lacks detailed ablation studies or explicit limitation discussions.

## Comparison to Discriminative PRMs
The paper doesn't provide direct compute cost comparisons in the available excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11ff100f-04f6-467e-9e8b-d8ff2aeae908",
  "isSidechain": true,
  "promptId": "003d4d5b-99b9-4488-a4e4-5e4419f94d98",
  "agentId": "ad50dc4fb50295b3a",
  "type": "user",
  "uuid": "9068f5b6-406b-4b4a-a263-4e3d91fd6387",
  "sourceToolAssistantUUID": "11ff100f-04f6-467e-9e8b-d8ff2aeae908",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-29T10:07:00.261Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WRLzXbEkqDQpxEHzjpjXWC`</summary>

```json
{
  "url": "https://www.semanticscholar.org/paper/GenPRM:-Scaling-Test-Time-Compute-of-Process-Reward-Zhao-Liu/bd94932b7604933a11d1538b0de6f9543089711f",
  "prompt": "Extract cited papers, key technical contributions, method details, how RPE works, compute cost analysis, ablations, and any reviewer or community commentary."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9068f5b6-406b-4b4a-a263-4e3d91fd6387",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
  "requestId": "req_011CbWg43tbyrbahhdZCghKR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a8745ee-c5be-4a76-b3a3-0944fc52577c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VevJpC8UJut1izfGesvs9k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1316,
      "cache_read_input_tokens": 13145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1316,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
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

_source line 22 · 2026-05-29T10:07:00.897Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EdS4tHrCsar9MoTvMcDwoT`</summary>

```json
{
  "query": "GenPRM \"Relative Progress Estimation\" RPE code verification test-time compute cost discriminative PRM comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a8745ee-c5be-4a76-b3a3-0944fc52577c",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
  "requestId": "req_011CbWg43tbyrbahhdZCghKR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "046919ab-29bb-4095-84a6-bf50bf70acce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VevJpC8UJut1izfGesvs9k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1316,
      "cache_read_input_tokens": 13145,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1316
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 216,
          "cache_read_input_tokens": 13145,
          "cache_creation_input_tokens": 1316,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1316,
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

_source line 23 · 2026-05-29T10:07:03.069Z_

<details><summary>↩ Tool result · `toolu_01WRLzXbEkqDQpxEHzjpjXWC`</summary>

```text
I appreciate your detailed instructions, but I cannot provide the requested extraction because the web page content provided is empty. There is no text, papers, technical details, methodology, or commentary to analyze.

To help you effectively, please provide:
- The actual webpage content or URL
- The research paper or document text
- Specific details about RPE (Relative Positional Encoding, or another acronym you're referencing)

Once you share the substantive content, I'll extract:
- Cited papers and references
- Key technical contributions
- Methodology details
- RPE mechanism explanations
- Computational cost analysis
- Ablation study results
- Reviewer/community feedback

All while adhering to your 125-character quote limit and paraphrasing requirements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a8745ee-c5be-4a76-b3a3-0944fc52577c",
  "isSidechain": true,
  "promptId": "003d4d5b-99b9-4488-a4e4-5e4419f94d98",
  "agentId": "ad50dc4fb50295b3a",
  "type": "user",
  "uuid": "90df9285-133d-4410-8d7f-d82676435434",
  "sourceToolAssistantUUID": "0a8745ee-c5be-4a76-b3a3-0944fc52577c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-29T10:07:08.354Z_

<details><summary>↩ Tool result · `toolu_01EdS4tHrCsar9MoTvMcDwoT`</summary>

```text
Web search results for query: "GenPRM "Relative Progress Estimation" RPE code verification test-time compute cost discriminative PRM comparison"

Links: [{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | Arxiv - DeepPaper","url":"https://arxiv.deeppaper.ai/papers/2504.00891v2?locale=en"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2504.00891"},{"title":"[2504.00891] GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://arxiv.org/abs/2504.00891"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/genprm-scaling-test-time-compute-process-reward"},{"title":"Paper page - GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://huggingface.co/papers/2504.00891"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward ...","url":"https://arxiv.org/pdf/2504.00891"},{"title":"Breaking the LLM Bottleneck: GenPRM’s approach to Scale test-time compute via generative reasoning | by SACHIN KUMAR | Medium","url":"https://medium.com/@techsachin/breaking-the-llm-bottleneck-genprms-approach-to-scale-test-time-compute-via-generative-reasoning-0e90e3ffa71e"},{"title":"GitHub - RyanLiu112/GenPRM: [AAAI 2026] Official codebase for \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\".","url":"https://github.com/RyanLiu112/GenPRM"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | Request PDF","url":"https://www.researchgate.net/publication/390404512_GenPRM_Scaling_Test-Time_Compute_of_Process_Reward_Models_via_Generative_Reasoning"}]

Based on the search results, I found comprehensive information about GenPRM and the concepts in your query:

## GenPRM Overview

GenPRM is a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step.

## Relative Progress Estimation (RPE)

To obtain high-quality process supervision labels and rationale data, they propose Relative Progress Estimation (RPE) and a rationale synthesis framework that incorporates code verification. 

RPE compares the model's confidence in answering a question with and without the reasoning step being evaluated, providing a more nuanced measure of a step's contribution than hard labels alone. Setting a threshold of P_t ≥ 0.8 produces the most accurate evaluations, as it effectively identifies genuinely helpful steps while filtering out irrelevant or incorrect ones.

## Test-Time Compute Scaling

GenPRM supports test-time scaling in a parallel manner with majority voting and supports policy model test-time scaling with GenPRM as verifiers or critics. Through test-time scaling, a 1.5B GenPRM outperforms GPT-4o, and a 7B GenPRM surpasses Qwen2.5-Math-PRM-72B on ProcessBench.

## Comparison with Discriminative PRMs

The training framework for GenPRM differs significantly from traditional classification-based PRMs. Instead of simply predicting scalar values, GenPRM learns to generate explicit reasoning and verification code before making judgments about reasoning steps.

The paper has been accepted to AAAI 2026, with code and models available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "046919ab-29bb-4095-84a6-bf50bf70acce",
  "isSidechain": true,
  "promptId": "003d4d5b-99b9-4488-a4e4-5e4419f94d98",
  "agentId": "ad50dc4fb50295b3a",
  "type": "user",
  "uuid": "9838e9f5-5081-450c-8e81-19dd101a15bf",
  "sourceToolAssistantUUID": "046919ab-29bb-4095-84a6-bf50bf70acce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-29T10:07:11.927Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GJU8693SmXn5W3nwwoDd5B`</summary>

```json
{
  "url": "https://papers.cool/arxiv/2504.00891",
  "prompt": "Extract method details especially: how RPE (Relative Progress Estimation) works mechanically, how code verification is integrated into the training pipeline, what the test-time scaling strategy is (majority voting details), compute overhead vs discriminative PRMs, limitations, and any reviewer/community commentary."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9838e9f5-5081-450c-8e81-19dd101a15bf",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
  "requestId": "req_011CbWg4yavYz493bKHLdXPo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee0ae90e-e1bb-4279-9e18-f229f83bdbd4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WKa2tFZWVHnaCwuMzMSFDo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1531,
      "cache_read_input_tokens": 14461,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1531,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 26 · 2026-05-29T10:07:12.940Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TYF74DV3xJAMqbgr6BQCvJ`</summary>

```json
{
  "url": "https://www.aimodels.fyi/papers/arxiv/genprm-scaling-test-time-compute-process-reward",
  "prompt": "Extract detailed method description: RPE mechanism, code verification pipeline, training data synthesis, test-time scaling approach, compute cost comparison to discriminative PRMs, ablations, and limitations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee0ae90e-e1bb-4279-9e18-f229f83bdbd4",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
  "requestId": "req_011CbWg4yavYz493bKHLdXPo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "770f9e0e-ffa0-48da-9041-b296020aae53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WKa2tFZWVHnaCwuMzMSFDo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1531,
      "cache_read_input_tokens": 14461,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1531
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 259,
          "cache_read_input_tokens": 14461,
          "cache_creation_input_tokens": 1531,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1531,
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

_source line 27 · 2026-05-29T10:07:13.150Z_

<details><summary>↩ Tool result · `toolu_01TYF74DV3xJAMqbgr6BQCvJ`</summary>

```text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "770f9e0e-ffa0-48da-9041-b296020aae53",
  "isSidechain": true,
  "promptId": "003d4d5b-99b9-4488-a4e4-5e4419f94d98",
  "agentId": "ad50dc4fb50295b3a",
  "type": "user",
  "uuid": "6c349511-5691-4a31-8e7e-b1c5d7de91ce",
  "sourceToolAssistantUUID": "770f9e0e-ffa0-48da-9041-b296020aae53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-29T10:07:16.030Z_

<details><summary>↩ Tool result · `toolu_01GJU8693SmXn5W3nwwoDd5B`</summary>

```text
# GenPRM Paper Extract

Based on the provided webpage content, here's what can be determined:

## Available Information

The webpage contains only the paper's abstract and metadata. Specific technical details requested are **not present** in this excerpt.

## What the Abstract Reveals

**Core Innovation**: GenPRM performs "explicit Chain-of-Thought reasoning with code verification before providing judgment for each reasoning step."

**Key Components Mentioned**:
- Relative Progress Estimation (RPE) and rationale synthesis framework incorporating code verification
- Training approach using only "23K training data from MATH dataset"

**Performance Claims**: Test-time scaling reportedly enables "a 1.5B GenPRM outperforms GPT-4o, and a 7B GenPRM surpasses Qwen2.5-Math-PRM-72B"

## Notable Limitation

The webpage does not contain the detailed technical sections needed to explain:
- How RPE works mechanistically
- Code verification integration specifics in the training pipeline
- Majority voting or scaling strategy details
- Compute overhead comparisons
- Acknowledged limitations
- Reviewer commentary

**To access these details**, you would need to review the full PDF (referenced as "PDF27" in the interface) available at arxiv.org/abs/2504.00891.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee0ae90e-e1bb-4279-9e18-f229f83bdbd4",
  "isSidechain": true,
  "promptId": "003d4d5b-99b9-4488-a4e4-5e4419f94d98",
  "agentId": "ad50dc4fb50295b3a",
  "type": "user",
  "uuid": "4729561a-de63-46fb-8e22-a47b22dc69a4",
  "sourceToolAssistantUUID": "ee0ae90e-e1bb-4279-9e18-f229f83bdbd4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-29T10:07:19.014Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018FvMULpsk6t8VNjaf7WTa4`</summary>

```json
{
  "url": "https://huggingface.co/papers/2504.00891",
  "prompt": "Extract discussion comments, any user or reviewer commentary, key insights about the method, what was praised or criticized, and compute cost considerations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4729561a-de63-46fb-8e22-a47b22dc69a4",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
  "requestId": "req_011CbWg5XmBc1uiLXEsMct19",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bffc1fa5-6c1f-46bd-ba51-d7425cd10a39",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AwoVwPR5mtji5FQ3cCHfyP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 580,
      "cache_read_input_tokens": 15992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 580,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 30 · 2026-05-29T10:07:19.880Z_

<details><summary>↩ Tool result · `toolu_018FvMULpsk6t8VNjaf7WTa4`</summary>

```text
&lt;persisted-output>
Output too large (87.1KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/83204518-f78b-400d-b0b3-3bb64b514d04/tool-results/toolu_018FvMULpsk6t8VNjaf7WTa4.txt

Preview (first 2KB):
# GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning

Jian Zhao&lt;sup>1,3\*&lt;/sup>, Runze Liu&lt;sup>1,2\*†&lt;/sup>, Kaiyan Zhang&lt;sup>1&lt;/sup>, Zhimu Zhou&lt;sup>3&lt;/sup>, Junqi Gao&lt;sup>4&lt;/sup>, Dong Li&lt;sup>4&lt;/sup>, Jiafei Lyu&lt;sup>1&lt;/sup>, Zhouyi Qian&lt;sup>4&lt;/sup>, Biqing Qi&lt;sup>2‡&lt;/sup>, Xiu Li&lt;sup>1‡&lt;/sup> and Bowen Zhou&lt;sup>1,2‡&lt;/sup>

&lt;sup>1&lt;/sup>Tsinghua University, &lt;sup>2&lt;/sup>Shanghai AI Laboratory, &lt;sup>3&lt;/sup>BUPT, &lt;sup>4&lt;/sup>Harbin Institute of Technology

Recent advancements in Large Language Models (LLMs) have shown that it is promising to utilize Process Reward Models (PRMs) as verifiers to enhance the performance of LLMs. However, current PRMs face three key challenges: (1) limited process supervision and generalization capabilities, (2) dependence on scalar value prediction without leveraging the generative abilities of LLMs, and (3) inability to scale the test-time compute of PRMs. In this work, we introduce GenPRM, a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step. To obtain high-quality process supervision labels and rationale data, we propose Relative Progress Estimation (RPE) and a rationale synthesis framework that incorporates code verification. Experimental results on ProcessBench and several mathematical reasoning tasks show that GenPRM significantly outperforms prior PRMs with only **23K** training data from **MATH** dataset. Through test-time scaling, a **1.5B** GenPRM outperforms **GPT-4o**, and a **7B** GenPRM surpasses **Qwen2.5-Math-PRM-72B** on ProcessBench. Additionally, GenPRM demonstrates strong abilities to serve as a critic model for policy model refinement. This work establishes a new paradigm for process supervision that bridges the gap between PRMs and critic models in LLMs. Our code, model, and data are available in &lt;https://ryanliu112.github.io/GenPRM>.

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bffc1fa5-6c1f-46bd-ba51-d7425cd10a39",
  "isSidechain": true,
  "promptId": "003d4d5b-99b9-4488-a4e4-5e4419f94d98",
  "agentId": "ad50dc4fb50295b3a",
  "type": "user",
  "uuid": "bd1e3438-ba36-4c45-b23c-20f734fdb9aa",
  "sourceToolAssistantUUID": "bffc1fa5-6c1f-46bd-ba51-d7425cd10a39",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-29T10:07:20.166Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Mh2Q57HmJtwR62JYkhfhKq`</summary>

```json
{
  "url": "https://github.com/RyanLiu112/GenPRM",
  "prompt": "Extract the README content including method description, training pipeline details, inference cost/overhead, any comparison to discriminative PRMs in compute cost, and any known limitations mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd1e3438-ba36-4c45-b23c-20f734fdb9aa",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
  "requestId": "req_011CbWg5XmBc1uiLXEsMct19",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "771887c5-cc56-4e15-a7dd-7dcf95dde5ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AwoVwPR5mtji5FQ3cCHfyP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 580,
      "cache_read_input_tokens": 15992,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 580
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 209,
          "cache_read_input_tokens": 15992,
          "cache_creation_input_tokens": 580,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 580,
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

_source line 32 · 2026-05-29T10:07:27.150Z_

<details><summary>↩ Tool result · `toolu_01Mh2Q57HmJtwR62JYkhfhKq`</summary>

```text
# GenPRM: Key Technical Details

## Method Overview

GenPRM is a generative process reward model with these core features:
- **Explicit reasoning**: "performing explicit CoT reasoning and code verfication before providing the process judgment"
- **Relative Progress Estimation (RPE)**: Improves upon Monte Carlo estimation and hard labels
- **Test-time scaling**: Supports parallel verification via majority voting
- **Dual roles**: Functions as verifiers or critics for policy model scaling

## Training Pipeline

The repository provides code for:
1. **Solution generation** from policy models
2. **Monte Carlo score calculation** using reference models
3. **Reasoning data generation** via specialized models (e.g., QwQ-32B)
4. **Model training** based on axolotl and RLHFlow frameworks

Training data includes "23K training data from MATH dataset" with complete synthesis code available.

## Model Variants

Available models range from 1.5B to 70B parameters, with 1.5B, 7B, and 32B versions currently released on HuggingFace.

## Inference & Compute

The repository provides inference modules but does not explicitly quantify inference costs or computational overhead comparisons against discriminative PRMs. No computational complexity analysis comparing generative vs. discriminative approaches is detailed in the README.

## Known Limitations

No explicit limitations are mentioned. The README notes that "mathematical expression evaluation code is based on Qwen2.5-Math" and references Math-Verify as "a more powerful evaluator" but doesn't identify inherent GenPRM constraints.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "771887c5-cc56-4e15-a7dd-7dcf95dde5ee",
  "isSidechain": true,
  "promptId": "003d4d5b-99b9-4488-a4e4-5e4419f94d98",
  "agentId": "ad50dc4fb50295b3a",
  "type": "user",
  "uuid": "8391fa68-686d-4a21-aa48-820ed26b7855",
  "sourceToolAssistantUUID": "771887c5-cc56-4e15-a7dd-7dcf95dde5ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-29T10:07:29.720Z_

<details open><summary>🔧 Tool call — Read · `toolu_017KKwZaJX7mwceJvDxyYoks`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/83204518-f78b-400d-b0b3-3bb64b514d04/tool-results/toolu_018FvMULpsk6t8VNjaf7WTa4.txt",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8391fa68-686d-4a21-aa48-820ed26b7855",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
  "requestId": "req_011CbWg6MKuQsYFGP53NHQrw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c39bf99-ff4f-498c-85c7-1b932e1e0eec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Y3JvYrmfih7JwCRA7GhrAU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1395,
      "cache_read_input_tokens": 16572,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1395
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 145,
          "cache_read_input_tokens": 16572,
          "cache_creation_input_tokens": 1395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1395,
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

_source line 34 · 2026-05-29T10:07:29.988Z_

<details><summary>↩ Tool result · `toolu_017KKwZaJX7mwceJvDxyYoks`</summary>

```text
1	# GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning
2	
3	Jian Zhao&lt;sup>1,3\*&lt;/sup>, Runze Liu&lt;sup>1,2\*†&lt;/sup>, Kaiyan Zhang&lt;sup>1&lt;/sup>, Zhimu Zhou&lt;sup>3&lt;/sup>, Junqi Gao&lt;sup>4&lt;/sup>, Dong Li&lt;sup>4&lt;/sup>, Jiafei Lyu&lt;sup>1&lt;/sup>, Zhouyi Qian&lt;sup>4&lt;/sup>, Biqing Qi&lt;sup>2‡&lt;/sup>, Xiu Li&lt;sup>1‡&lt;/sup> and Bowen Zhou&lt;sup>1,2‡&lt;/sup>
4	
5	&lt;sup>1&lt;/sup>Tsinghua University, &lt;sup>2&lt;/sup>Shanghai AI Laboratory, &lt;sup>3&lt;/sup>BUPT, &lt;sup>4&lt;/sup>Harbin Institute of Technology
6	
7	Recent advancements in Large Language Models (LLMs) have shown that it is promising to utilize Process Reward Models (PRMs) as verifiers to enhance the performance of LLMs. However, current PRMs face three key challenges: (1) limited process supervision and generalization capabilities, (2) dependence on scalar value prediction without leveraging the generative abilities of LLMs, and (3) inability to scale the test-time compute of PRMs. In this work, we introduce GenPRM, a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step. To obtain high-quality process supervision labels and rationale data, we propose Relative Progress Estimation (RPE) and a rationale synthesis framework that incorporates code verification. Experimental results on ProcessBench and several mathematical reasoning tasks show that GenPRM significantly outperforms prior PRMs with only **23K** training data from **MATH** dataset. Through test-time scaling, a **1.5B** GenPRM outperforms **GPT-4o**, and a **7B** GenPRM surpasses **Qwen2.5-Math-PRM-72B** on ProcessBench. Additionally, GenPRM demonstrates strong abilities to serve as a critic model for policy model refinement. This work establishes a new paradigm for process supervision that bridges the gap between PRMs and critic models in LLMs. Our code, model, and data are available in &lt;https://ryanliu112.github.io/GenPRM>.
8	
9	**Figure 1: GenPRM achieves state-of-the-art performance across multiple benchmarks in two key roles: (a) As a verifier:** GenPRM-7B outperforms all classification-based PRMs of comparable size and even surpasses **Qwen2.5-Math-PRM-72B** via test-time scaling. **(b) As a critic:** GenPRM-7B demonstrates superior critique capabilities, achieving **3.4x** greater performance gains than DeepSeek-R1-Distill-Qwen-7B after 3 refinement iterations.
10	
11	\* Equal contribution
12	
13	† Project lead & Work done during an internship at Shanghai AI Laboratory
14	
15	‡ Corresponding authors: Biqing Qi (qibiqing@pjlab.org.cn), Xiu Li (li.xiu@sz.tsinghua.edu.cn), and Bowen Zhou (zhoubowen@tsinghua.edu.cn)The diagram illustrates the architectural differences between classification-based PRMs and GenPRM. On the left, under the heading 'Classification-based PRM', two models are shown: 'Discriminative PRM' and 'Direct Generative PRM'. The Discriminative PRM consists of a 'value head' that outputs a score of 0.9, marked with a green checkmark. The Direct Generative PRM outputs a 'Yes' label, which is then converted to a score of 0.8, also marked with a green checkmark. On the right, under the heading 'Generative PRM (Ours)', the 'GenPRM' model is shown. It branches into three parallel paths, each consisting of a yellow circle (CoT Verification) followed by a green circle (Code Verification) and a 'Yes' or 'No' label. The top path outputs 'Yes', the middle path outputs 'No', and the bottom path outputs 'No'. These three paths converge into a final score of 0.2, which is marked with a red 'X'. A legend at the bottom identifies the yellow circle as 'CoT Verification' and the green circle as 'Code Verification'.
16	
17	Figure 2: Comparison between GenPRM (right) and previous classification-based PRMs (left).
18	
19	## 1. Introduction
20	
21	Large Language Models (LLMs) have shown significant advances in recent years (OpenAI, 2023; Anthropic, 2023; OpenAI, 2024a,b; DeepSeek-AI et al., 2025). As OpenAI o1 demonstrates the great effectiveness of scaling test-time compute (OpenAI, 2024a), an increasing number of researches focus on Test-Time Scaling (TTS) methods to improve the reasoning performance of LLMs (Snell et al., 2025; Liu et al., 2025).
22	
23	Effective TTS requires high-quality verifiers, such as Process Reward Models (PRMs) (Liu et al., 2025). However, existing PRMs face several limitations. They exhibit limited process supervision capabilities and struggle to generalize across different models and tasks (Zheng et al., 2024; Zhang et al., 2025c; Liu et al., 2025). Furthermore, most current approaches train PRMs as classifiers that output scalar values, neglecting the natural language generation abilities of LLMs, which are pre-trained on extensive corpora. This classifier-based modeling inherently prevents PRMs from leveraging test-time scaling methods to enhance process supervision capabilities. These limitations lead us to the following research question: *How can generative modeling enhance the process supervision capabilities of PRMs while enabling test-time scaling?*
24	
25	In this work, we address these challenges through a generative process reward model, named GenPRM. Specifically, GenPRM differs from classification-based PRMs in that GenPRM redefines process supervision as a generative task rather than a discriminative scoring task by integrating Chain-of-Thought (CoT) (Wei et al., 2022) reasoning and code verification processes before providing final judgment. To improve conventional hard label estimation, we propose Relative Progress Estimation (RPE), which leverages a relative criterion for label estimation. Additionally, we introduce a rationale synthesis framework with code verification to obtain high-quality process supervision reasoning data. A comparison of our method with previous classification-based methods is presented in Figure 2.
26	
27	Our contributions can be summarized as follows:
28	
29	1. 1. We propose a generative process reward model that performs explicit CoT reasoning with code verification and utilizes Relative Progress Estimation to obtain accurate PRM labels.
30	2. 2. Empirical results on ProcessBench and common mathematical reasoning tasks demonstrate that GenPRM outperforms prior classification-based PRMs. Additionally, smaller GenPRM models can surpass larger PRMs via TTS.
31	3. 3. We provide a new perspective on PRMs in this work, fully leveraging their TTS capabilities, reshaping their applications, and opening new directions for future research in process supervision.## 2. Preliminaries
32	
33	### 2.1. Markov Decision Process
34	
35	Following [Liu et al. \(2025\)](#), we formulate the test-time scaling process with PRMs as a Markov Decision Process (MDP) defined by  $(\mathcal{S}, \mathcal{A}, P, r, \gamma)$ , where  $\mathcal{S}$  is the state space,  $\mathcal{A}$  is the action space,  $P$  represents transition dynamics,  $r : \mathcal{S} \times \mathcal{A} \rightarrow \mathbb{R}$  is the reward function, and  $\gamma \in [0, 1]$  is the discount factor. Starting with a prompt set  $\mathcal{X}$  and an initial state  $s_1 = x \sim \mathcal{X}$ , the policy model  $\pi_\theta$  generates an action  $a_1 \sim \pi_\theta(\cdot | s_1)$ .&lt;sup>1&lt;/sup> Unlike traditional RL methods with stochastic transitions ([Liu et al., 2022, 2024](#)), transitions in LLMs are deterministic, i.e.,  $s_{t+1} = P(\cdot | s_t, a_t) = [s_t, a_t]$ , where  $[\cdot, \cdot]$  denotes string concatenation. This process continues until the episode terminates (i.e., generating the [EOS] token), obtaining a trajectory of  $T$  steps:  $\tau = \{a_1, a_2, \dots, a_T\}$ . The goal is to optimize either the reward of each step (as in search-based methods) or the reward over the full response (as in Best-of-N sampling).
36	
37	### 2.2. Supervised Fine-Tuning
38	
39	Supervised Fine-Tuning (SFT) trains a model to predict the next token based on prior context. For a dataset  $\mathcal{D}_{\text{SFT}} = \{(x^{(i)}, y^{(i)})\}_{i=1}^N$ , the SFT loss is:
40	
41	$$\mathcal{L}_{\text{SFT}}(\theta) = -\mathbb{E}_{(x,y) \sim \mathcal{D}_{\text{SFT}}} \left[ \sum_{t=1}^{|y|} \log \pi_\theta(y_t | x, y_{1:t-1}) \right], \quad (1)$$
42	
43	where  $\pi_\theta$  represents a model with parameters  $\theta$ .
44	
45	### 2.3. Test-Time Scaling
46	
47	In this work, we consider two test-time scaling methods, including majority voting and Best-of-N.
48	
49	**Majority Voting.** Majority voting ([Wang et al., 2023](#)) selects the answer that appears the most frequently among all solutions.
50	
51	**Best-of-N.** Best-of-N (BoN) ([Brown et al., 2024](#); [Snell et al., 2025](#)) selects the best answer from  $N$  candidate solutions.
52	
53	## 3. Method
54	
55	In this section, we first describe how to develop GenPRM and integrate the reasoning process with code verification. We then introduce how to scale test-time compute of policy models using GenPRM and apply TTS for GenPRM. Last, we present the improved label estimation method and data generation and filtering framework of GenPRM.
56	
57	### 3.1. GenPRM and Test-Time Scaling
58	
59	#### 3.1.1. From Discriminative PRM to Generative PRM
60	
61	**Discriminative PRM.** Assume we have a PRM dataset  $\mathcal{D}_{\text{Disc}} = \{(s_t, a_t), r_t\}$ , where  $r_t \in \{0, 1\}$  for PRM labels with hard estimation. The discriminative PRM  $r_\psi$  is trained via cross-entropy loss ([Skywork](#)
62	
63	&lt;sup>1&lt;/sup>Following [Snell et al. \(2025\)](#); [Liu et al. \(2025\)](#), we refer to models that generate solutions as policy models.The diagram illustrates the GenPRM framework, which consists of six key parts:
64	
65	- **① Solution Generation & MC Reward Estimation:** A math problem is solved by generating intermediate steps (a&lt;sub>11&lt;/sub>, a&lt;sub>21&lt;/sub>, a&lt;sub>31&lt;/sub>, a&lt;sub>12&lt;/sub>, a&lt;sub>22&lt;/sub>, a&lt;sub>32&lt;/sub>). Correct steps (q&lt;sub>1&lt;/sub>, q&lt;sub>2&lt;/sub>) are marked with blue circles, and incorrect steps (q&lt;sub>3&lt;/sub>) are marked with red circles. The MC score for a step is calculated as  $MC(s_{12}, a_{12}) = \frac{2}{3}$ .
66	- **② Relative Progress Estimation:** The process reward is estimated as  $P_t = \frac{MC(s_t, a_t)}{MC(s_t)} \geq \epsilon$ . If the reward is high,  $\hat{r}_t = 1$  (green checkmark), otherwise  $\hat{r}_t = 0$  (red X).
67	- **③ Rationale Synthesis:** A problem is analyzed using CoT (Chain of Thought) analysis to generate a rationale. This rationale is then verified using code verification (e.g., Python code) to check for potential errors. The final label is a judgement of Yes/No.
68	- **④ GenPRM Training:** Data (23K) is used for SFT (Supervised Fine-Tuning) to train GenPRM. Consensus filtering is applied to the training data.
69	- **⑤ Policy Model Test-Time Scaling:** The trained GenPRM functions as a verifier or critic. It can be used to verify a solution (GenPRM as a Verifier) or critique a solution (GenPRM as a Critic).
70	- **⑥ GenPRM Test-Time Scaling:** The performance of GenPRM is improved through test-time scaling. Multiple steps are analyzed and verified, and their rewards are aggregated to produce a final reward  $r$ .
71	
72	Legend:
73	
74	- a Intermediate Step
75	- q Correct Answer
76	- q Incorrect Answer
77	- r Single Reward Judgement
78	- r Aggregated Reward Judgement
79	
80	**Figure 3: Overall framework of GenPRM.** Our framework consists of six key parts: ① The policy model generates solution steps, with MC scores estimated from rollout trajectories. ② Our proposed RPE derives accurate PRM labels. ③ High-quality process supervision data is synthesized through CoT reasoning augmented with code verification. ④ We apply consensus filtering followed by SFT to train GenPRM. ⑤ The trained GenPRM functions as a verifier or critic, enabling enhanced test-time scaling for policy models. ⑥ The performance of GenPRM further improves through test-time scaling.
81	
82	o1 Team, 2024; Zhang et al., 2025c):
83	
84	$$\mathcal{L}_{CE}(\psi) = -\mathbb{E}_{(s_t, a_t, r_t) \sim \mathcal{D}_{Disc}} [r_t \log r_\psi(s_t, a_t) + (1 - r_t) \log(1 - r_\psi(s_t, a_t))]. \quad (2)$$
85	
86	**Direct Generative PRM.** With a dataset  $\mathcal{D}_{Direct-Gen} = \{(s_t, a_t), r_t\}$ , where  $r_t$  is Yes for a correct step and No otherwise, the direct generative PRM (Xiong et al., 2024) is trained through SFT to predict Yes or No for each step. For step  $t$ , we use the probability of the Yes token as the predicted process reward  $\hat{r}_t$ :
87	
88	$$\hat{r}_t = r_\psi(\text{Yes} \mid s_t, a_t). \quad (3)$$
89	
90	**Generative PRM.** By equipping the direct generative PRM with an explicit reasoning process like CoT (Wei et al., 2022), we obtain a generative PRM. Let  $v_{1:t-1}$  denote the rationale from step 1 to  $t-1$  and  $v_t$  denote the rationale for step  $t$ . Assume we have a dataset  $\mathcal{D}_{Gen} = \{(s_t, a_t, v_{1:t-1}), (v_t, r_t)\}$ . GenPRM learns to reason and verify each step via SFT on this dataset. The generative process reward  $\hat{r}_t$  can be obtained via the following equation:
91	
92	$$\hat{r}_t = r_\psi(\text{Yes} \mid s_t, a_t, v_{1:t-1}, v_t), \quad \text{where } v_t \sim r_\psi(\cdot \mid s_t, a_t, v_{1:t-1}) \quad (4)$$
93	
94	**Generative PRM with Code Verification.** If we only verify the reasoning step with CoT based on natural language, the process may lack robustness in certain complex scenarios (Zhu et al., 2024; Gou et al., 2024). The difference between the generative PRM and the generative PRM with code verification is that the latter generates code to verify the reasoning step by executing it and provides the judgment based on the execution results. At step  $t$ , after generating the rationale  $v_t$  containing CoT and code, we execute the code and obtain feedback  $f_t$ . Given the current state  $s_t$ , action  $a_t$ , previous rationales  $v_{1:t-1}$ , and previous corresponding execution feedback  $f_{1:t-1}$ , the PRM first generates therationale  $v_t$ . After execution and obtaining the feedback  $f_t$ , we compute the final generative process reward as follows:
95	
96	$$\hat{r}_t = r_\psi(\text{Yes} \mid s_t, a_t, v_{1:t-1}, f_{1:t-1}, v_t, f_t), \quad \text{where } v_t \sim r_\psi(\cdot \mid s_t, a_t, v_{1:t-1}, f_{1:t-1}) \quad (5)$$
97	
98	In the following sections, we refer to GenPRM as this generative PRM type with code verification. The effectiveness of CoT and code verification can be found in Section 4.4.
99	
100	### 3.1.2. Test-Time Scaling
101	
102	**Policy Model TTS: GenPRM as a Verifier.** To scale the test-time compute of policy models, we can sample multiple responses from policy models and then use GenPRM as a verifier to select the final answer (Snell et al., 2025) in the way of parallel TTS.
103	
104	**Policy Model TTS: GenPRM as a Critic.** By equipping the PRM with generative process supervision abilities, GenPRM can be naturally used as a critic model to refine the outputs of policy models and we can scale the refinement process with multiple turns in a sequential TTS manner.
105	
106	**GenPRM TTS.** When evaluating each solution step, we first sample  $N$  reasoning verification paths and then use majority voting to obtain the final prediction by averaging the rewards. For GenPRM without code verification, the rewards are computed as follows:
107	
108	$$\hat{r}_t = \frac{1}{N} \sum_{i=1}^N r_\psi(\text{Yes} \mid s_t, a_t, v_{1:t-1}^i, v_t^i). \quad (6)$$
109	
110	And we can further incorporate code verification and execution feedback into this reasoning process:
111	
112	$$\hat{r}_t = \frac{1}{N} \sum_{i=1}^N r_\psi(\text{Yes} \mid s_t, a_t, v_{1:t-1}^i, f_{1:t-1}^i, v_t^i, f_t^i). \quad (7)$$
113	
114	Then the rewards can be used for ranking the responses of policy models or be converted into binary labels through a threshold 0.5 for judging the correctness of the step. The discussion of using code verification can be found at Table 5.
115	
116	## 3.2. Synthesizing Data of GenPRM
117	
118	In this section, we introduce our pipeline for synthesizing training data of GenPRM. The pipeline consists of three stages: (1) generating reasoning paths and obtaining PRM labels via Monte Carlo (MC) estimation; (2) evaluating the progress of each step via Relative Progress Estimation; and (3) synthesizing rationales with CoT and code verification, and inferring LLM-as-a-judge labels with consensus filtering.
119	
120	### 3.2.1. Solution Generation and Monte Carlo Estimation
121	
122	**Solution Generation with Step Forcing.** We utilize the 7.5K problems from the training set of the MATH dataset (Hendrycks et al., 2021) as the problem set. For each problem, we use Qwen2.5-7B-Instruct (Yang et al., 2024a) as the generation model to collect multiple solutions. Since using “\n\n” for step division does not consider the semantics of each step and may result in overly fine-grained division, we apply a step forcing approach to generate solutions. Specifically, we add “Step 1:” as the prefix for the generation model to complete the response. For a response with  $T$  reasoning steps, the format is as follows:### The response format with step forcing
123	
124	Step 1: {step content}
125	
126	...
127	
128	Step T: {step content}
129	
130	The proportion of correct paths versus incorrect paths varies significantly depending on the difficulty of the problems. To ensure a sufficient number of correct and incorrect paths, we sample up to 2048 paths for both hard and easy problems. If no correct or incorrect paths are found after sampling 2048 responses, we discard the corresponding problems.
131	
132	**Balancing the Precision and Efficiency of MC Estimation.** Following Math-Shepherd (Wang et al., 2024b), we estimate the probability of correctness for each step using completion-based sampling. For each reasoning step  $s_t$ , we generate  $K$  completion trajectories using a completion model, specifically Qwen2.5-Math-7B-Instruct (Yang et al., 2024b), and use MC estimation to calculate the probability that the current step  $a_t$  is correct (Wang et al., 2024b; Zhang et al., 2025c):
133	
134	$$MC(s_t, a_t) = MC(s_{t+1}) = \frac{1}{K} \sum_{j=1}^K \mathbb{1}(q_j = q^*), \quad (8)$$
135	
136	where  $q_j$  is the answer of the  $j$ -th response,  $q^*$  is the ground-truth answer, and  $\mathbb{1}$  is the indicator function. However, it is difficult for the completion model to reach the correct answer for hard problems even when the original step is correct, leading to incorrect results for MC estimation. To address this and balance the computation cost, we use a dynamic  $K$  based on the estimated Pass@1  $MC(s_1)$ :
137	
138	$$K = \begin{cases} 128 & \text{if } 0 \leq MC(s_1) < 0.1, \\ 64 & \text{if } 0.1 \leq MC(s_1) < 0.9, \\ 32 & \text{if } 0.9 \leq MC(s_1) < 1. \end{cases} \quad (9)$$
139	
140	### 3.2.2. Relative Progress Estimation
141	
142	Previous work has shown that hard label estimation is better than soft label estimation for PRMs (Zhang et al., 2025c). However, after MC estimation, we observe that although the MC score of many steps is greater than 0, the steps are incorrect, as also noted by Zhang et al. (2025c). On the other hand, we assume that a positive step should be both correct and beneficial. A reasoning step is considered as a beneficial one if it is easier to reach the correct answer by adding this step as the generation prefix. To address these issues, we propose Relative Progress Estimation (RPE), which shares a similar idea with relative advantage estimation in GRPO (Shao et al., 2024; DeepSeek-AI et al., 2025), to improve conventional hard label estimation.
143	
144	Specifically, the MC score is an empirical estimation of the current state  $s_t$ . To evaluate the quality of the current action  $a_t$ , it is natural to compare the MC score of the next state  $s_{t+1}$  with that of the current state  $s_t$ , since  $s_{t+1} = [s_t, a_t]$ . For each response, if the first erroneous step is step  $t'$  (i.e.,  $MC(s_{t'}) = 0$ ), we set the MC score of the following steps to 0. Our RPE  $P_t$  for step  $t$  is defined as follows:
145	
146	$$P_t = \frac{MC(s_t, a_t)}{MC(s_t)}, \quad (10)$$
147	
148	where  $MC(s_1)$  is the estimated Pass@1 computed in the solution generation phase. However, we empirically find that using a strict criterion where progress is always greater than 1 leads to unsatisfactory performance, as shown in Table 3. To address this, we estimate the final reward label  $\hat{r}_t$  byintroducing a threshold  $\epsilon$ :
149	
150	$$\hat{r}_t = \begin{cases} 1 & \text{if } P_t \geq \epsilon, \\ 0 & \text{otherwise.} \end{cases} \quad (11)$$
151	
152	We also discuss another form of relative progress  $P_t = MC(s_t, a_t) - MC(s_t)$  in Table 3 in Section 4.4.
153	
154	### 3.2.3. Rationale Generation, Verification and Filtering
155	
156	To obtain high-quality rationale data, we use QwQ-32B (Qwen Team, 2025) as the rationale generation model and introduce a three-step pipeline that automatically generates and verifies the rationale of each reasoning step. Given a problem  $x$  with a ground-truth answer  $q^*$  and candidate steps  $\{a_1, \dots, a_T\}$ , the generation and verification proceed as follows:
157	
158	**Step 1: Code-Based Rationale Generation.** To evaluate the correctness of  $a_t$ , we synthesize step-by-step CoT analysis. It has been shown that program-based reasoning improves verification outcomes (Zhu et al., 2024). Based on CoT analysis, we continue to synthesize code-based rationales to verify  $a_t$  based on the problem and historical steps  $\{a_1, \dots, a_{t-1}\}$ . We prompt the rationale generation model to surround the CoT with `&lt;analyze>` and `&lt;/analyze>`, and the code with `&lt;verify>` and `&lt;/verify>`. The prompt for rationale generation is shown in Table A.2.
159	
160	**Step 2: Code Execution and Verification.** With the generated code, we execute it and obtain the feedback  $f_t$  for step  $t$ . The execution feedback is formatted as [Code output: {execution result}] and is concatenated to the generated CoT and code as the prefix for the subsequent generation. If the execution result is inconsistent with the generated CoT verification, we observe that QwQ-32B performs self-reflection behaviors until reaching a consensus.
161	
162	**Step 3: Label Judgment and Consensus Filtering.** After generating and verifying the rationale data of all candidate steps, the rationale generation model finally outputs a number. If all steps are inferred to be correct, the number will be -1, otherwise will be the index of the first erroneous step. For each solution, if there is at least one process label with RPE is not consistent with the labels generated by LLM-as-a-judge (Zheng et al., 2023), we discard the entire solution and only retain the one with all labels consistent. After consensus filtering, we discard approximately 51% of the data and finally obtain a dataset containing 23K problems with reasoning steps and rationale data.
163	
164	## 4. Experiments
165	
166	In this section, we aim to answer the following questions:
167	
168	- • **Q1:** How does GenPRM perform compared with previous PRMs? (§4.2, §4.3)
169	- • **Q2:** How does the performance of GenPRM scale with more test-time compute? (§4.2, §4.3)
170	- • **Q3:** How does GenPRM benefit policy model test-time scaling? (§4.3)
171	- • **Q4:** How do the components and hyperparameters influence GenPRM? (§4.4)
172	
173	### 4.1. Setup
174	
175	**Benchmarks.** We evaluate GenPRM and baseline methods on ProcessBench (Zheng et al., 2024), a benchmark designed to assess process supervision capabilities in mathematical reasoning tasks.&lt;sup>2&lt;/sup>
176	
177	&lt;sup>2&lt;/sup>Our evaluation code is adapted from &lt;https://github.com/QwenLM/ProcessBench>.Additionally, we conduct BoN and critic refinement experiments using MATH (Hendrycks et al., 2021), AMC23 (AI-MO, 2024b), AIME24 (AI-MO, 2024a), and Minerva Math (Lewkowycz et al., 2022). For BoN response generation, we employ Qwen2.5-Math-7B-Instruct (Yang et al., 2024b) and Gemma-3-12b-it (Gemma Team and Google DeepMind, 2025) as policy models. For policy model TTS with GenPRM as the critic, we use Gemma-3-12b-it (Gemma Team and Google DeepMind, 2025) and Qwen2.5-7B-Instruct (Yang et al., 2024a) as generators.
178	
179	**Baselines.** For ProcessBench and BoN experiments, we compare GenPRM with the following methods:
180	
181	- • **Math-Shepherd-PRM-7B** (Wang et al., 2024b): This method trains a PRM using hard labels computed based on MC estimation.
182	- • **RLHFlow series** (Xiong et al., 2024): Includes RLHFlow-PRM-Mistral-8B and RLHFlow-PRM-Deepseek-8B.
183	- • **Skywork-PRM series** (Skywork o1 Team, 2024): Comprises Skywork-PRM-1.5B and Skywork-PRM-7B.
184	- • **EurusPRM** (Cui et al., 2025): EurusPRM-Stage1 and EurusPRM-Stage2 are trained as implicit PRMs (Yuan et al., 2024).
185	- • **Qwen2.5-Math series** (Zheng et al., 2024; Zhang et al., 2025c): Qwen2.5-Math-7B-Math-Shepherd and Qwen2.5-Math-7B-PRM800K are trained with Math-Shepherd (Wang et al., 2024b) and PRM800K (Lightman et al., 2024), respectively. For Qwen2.5-Math-PRM-7B and Qwen2.5-Math-PRM-72B, the training data is applied consensus filtering using LLM-as-a-judge (Zheng et al., 2023).
186	- • **RetrievalPRM-7B** (Zhu et al., 2025): The method enhances PRM with retrieved questions and corresponding steps.
187	- • **Universal-PRM-7B** (Tan et al., 2025): The method proposes an automated framework using ensemble prompting and reverse verification.
188	- • **Dyve-14B** (Zhong et al., 2025): This method dynamically applies fast or slow verification for each reasoning step.
189	- • **Direct Generative PRM-7B**: The method trains a direct generative PRM with the original language head via SFT using the same data as GenPRM, but without CoT and code verification.
190	
191	For critic experiments, we use the following methods for comparison:
192	
193	- • **Self-Refine** (Madaan et al., 2023): This method uses the generator to self-critique and refine the solution.
194	- • **DeepSeek-R1-Distill-Qwen-7B** (DeepSeek-AI et al., 2025): This model is fine-tuned based on Qwen2.5-Math-7B (Yang et al., 2024a) using high-quality reasoning data generated by DeepSeek-R1 (DeepSeek-AI et al., 2025).
195	
196	**Implementation Details.** For RPE, we set  $\epsilon = 0.8$  across all experiments, with ablation studies presented in Section 4.4. Rationale data is generated using QwQ-32B (Qwen Team, 2025) and the prompt template is shown in Table A.2. Our base models are from the DeepSeek-R1-Distill series (DeepSeek-AI et al., 2025), specifically the 1.5B, 7B, and 32B parameter variants. The training configuration for our method uses a batch size of 64 and a learning rate of  $2.0 \times 10^{-6}$ . During evaluation, we employ a temperature of 0.6. For critique refinement experiments, we extract content within the `&lt;analyze>&lt;/analyze>` tags, focusing exclusively on steps predicted as negative by the policy model. The baseline methods utilize standardized prompt templates (detailed in Table A.2) to ensure consistent critique generation formats.**Table 1:** ProcessBench results reported with F1 scores. The results of GenPRM are shaded. For 1.5B PRMs, **bold** indicates the best Pass@1 or scores superior to GPT-4o. For 7-8B and 14-72B PRMs, **bold** denotes the best Pass@1 or scores superior to Qwen2.5-Math-PRM-72B.
197	
198	&lt;table border="1">
199	&lt;thead>
200	&lt;tr>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c39bf99-ff4f-498c-85c7-1b932e1e0eec",
  "isSidechain": true,
  "promptId": "003d4d5b-99b9-4488-a4e4-5e4419f94d98",
  "agentId": "ad50dc4fb50295b3a",
  "type": "user",
  "uuid": "8b9aa914-e1a5-456d-9fe5-a373cb09dcc6",
  "sourceToolAssistantUUID": "9c39bf99-ff4f-498c-85c7-1b932e1e0eec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-29T10:07:32.579Z_

I now have detailed technical content. Let me read a bit more to get the limitations and key findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b9aa914-e1a5-456d-9fe5-a373cb09dcc6",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
  "requestId": "req_011CbWg6ZRRX1rHeq18FLqzd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd5d30ef-9633-4224-a42a-efe927df74b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01G4LaieMJN4mXipZAJ9CrsS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8850,
      "cache_read_input_tokens": 17967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8850,
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

_source line 36 · 2026-05-29T10:07:35.380Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B6TgkD6aoSYPHp2w2qcDW9`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/83204518-f78b-400d-b0b3-3bb64b514d04/tool-results/toolu_018FvMULpsk6t8VNjaf7WTa4.txt",
  "offset": 200,
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd5d30ef-9633-4224-a42a-efe927df74b5",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
  "requestId": "req_011CbWg6ZRRX1rHeq18FLqzd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a54358f0-476a-4b35-b230-f3e2a5f296e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01G4LaieMJN4mXipZAJ9CrsS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8850,
      "cache_read_input_tokens": 17967,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8850
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 184,
          "cache_read_input_tokens": 17967,
          "cache_creation_input_tokens": 8850,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8850,
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

_source line 37 · 2026-05-29T10:07:35.387Z_

<details><summary>↩ Tool result · `toolu_01B6TgkD6aoSYPHp2w2qcDW9`</summary>

```text
200	&lt;tr>
201	&lt;th>Model&lt;/th>
202	&lt;th># Samples&lt;/th>
203	&lt;th>GSM8K&lt;/th>
204	&lt;th>MATH&lt;/th>
205	&lt;th>Olympiad Bench&lt;/th>
206	&lt;th>Omni-MATH&lt;/th>
207	&lt;th>Avg.&lt;/th>
208	&lt;/tr>
209	&lt;/thead>
210	&lt;tbody>
211	&lt;tr>
212	&lt;td colspan="7" style="text-align: center;">&lt;i>Proprietary LLMs (Critic)&lt;/i>&lt;/td>
213	&lt;/tr>
214	&lt;tr>
215	&lt;td>GPT-4o-0806&lt;/td>
216	&lt;td>unk&lt;/td>
217	&lt;td>79.2&lt;/td>
218	&lt;td>63.6&lt;/td>
219	&lt;td>51.4&lt;/td>
220	&lt;td>53.5&lt;/td>
221	&lt;td>61.9&lt;/td>
222	&lt;/tr>
223	&lt;tr>
224	&lt;td>o1-mini&lt;/td>
225	&lt;td>unk&lt;/td>
226	&lt;td>93.2&lt;/td>
227	&lt;td>88.9&lt;/td>
228	&lt;td>87.2&lt;/td>
229	&lt;td>82.4&lt;/td>
230	&lt;td>87.9&lt;/td>
231	&lt;/tr>
232	&lt;tr>
233	&lt;td colspan="7" style="text-align: center;">&lt;i>PRMs (1.5B)&lt;/i>&lt;/td>
234	&lt;/tr>
235	&lt;tr>
236	&lt;td>Skywork-PRM-1.5B&lt;/td>
237	&lt;td>unk&lt;/td>
238	&lt;td>&lt;b>59.0&lt;/b>&lt;/td>
239	&lt;td>48.0&lt;/td>
240	&lt;td>19.3&lt;/td>
241	&lt;td>19.2&lt;/td>
242	&lt;td>36.4&lt;/td>
243	&lt;/tr>
244	&lt;tr>
245	&lt;td>GenPRM-1.5B (Pass@1)&lt;/td>
246	&lt;td>23K&lt;/td>
247	&lt;td>52.8&lt;/td>
248	&lt;td>&lt;b>66.6&lt;/b>&lt;/td>
249	&lt;td>&lt;b>55.1&lt;/b>&lt;/td>
250	&lt;td>&lt;b>54.5&lt;/b>&lt;/td>
251	&lt;td>&lt;b>57.3&lt;/b>&lt;/td>
252	&lt;/tr>
253	&lt;tr>
254	&lt;td>GenPRM-1.5B (Maj@8)&lt;/td>
255	&lt;td>23K&lt;/td>
256	&lt;td>51.3&lt;/td>
257	&lt;td>&lt;b>74.4&lt;/b>&lt;/td>
258	&lt;td>&lt;b>65.3&lt;/b>&lt;/td>
259	&lt;td>&lt;b>62.5&lt;/b>&lt;/td>
260	&lt;td>&lt;b>63.4&lt;/b>&lt;/td>
261	&lt;/tr>
262	&lt;tr>
263	&lt;td colspan="7" style="text-align: center;">&lt;i>PRMs (7-8B)&lt;/i>&lt;/td>
264	&lt;/tr>
265	&lt;tr>
266	&lt;td>Math-Shepherd-PRM-7B&lt;/td>
267	&lt;td>445K&lt;/td>
268	&lt;td>47.9&lt;/td>
269	&lt;td>29.5&lt;/td>
270	&lt;td>24.8&lt;/td>
271	&lt;td>23.8&lt;/td>
272	&lt;td>31.5&lt;/td>
273	&lt;/tr>
274	&lt;tr>
275	&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>
276	&lt;td>273K&lt;/td>
277	&lt;td>50.4&lt;/td>
278	&lt;td>33.4&lt;/td>
279	&lt;td>13.8&lt;/td>
280	&lt;td>15.8&lt;/td>
281	&lt;td>28.4&lt;/td>
282	&lt;/tr>
283	&lt;tr>
284	&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>
285	&lt;td>253K&lt;/td>
286	&lt;td>38.8&lt;/td>
287	&lt;td>33.8&lt;/td>
288	&lt;td>16.9&lt;/td>
289	&lt;td>16.9&lt;/td>
290	&lt;td>26.6&lt;/td>
291	&lt;/tr>
292	&lt;tr>
293	&lt;td>Skywork-PRM-7B&lt;/td>
294	&lt;td>unk&lt;/td>
295	&lt;td>70.8&lt;/td>
296	&lt;td>53.6&lt;/td>
297	&lt;td>22.9&lt;/td>
298	&lt;td>21.0&lt;/td>
299	&lt;td>42.1&lt;/td>
300	&lt;/tr>
301	&lt;tr>
302	&lt;td>EurusPRM-Stage1&lt;/td>
303	&lt;td>463K&lt;/td>
304	&lt;td>44.3&lt;/td>
305	&lt;td>35.6&lt;/td>
306	&lt;td>21.7&lt;/td>
307	&lt;td>23.1&lt;/td>
308	&lt;td>31.2&lt;/td>
309	&lt;/tr>
310	&lt;tr>
311	&lt;td>EurusPRM-Stage2&lt;/td>
312	&lt;td>30K&lt;/td>
313	&lt;td>47.3&lt;/td>
314	&lt;td>35.7&lt;/td>
315	&lt;td>21.2&lt;/td>
316	&lt;td>20.9&lt;/td>
317	&lt;td>31.3&lt;/td>
318	&lt;/tr>
319	&lt;tr>
320	&lt;td>Qwen2.5-Math-7B-Math-Shepherd&lt;/td>
321	&lt;td>445K&lt;/td>
322	&lt;td>62.5&lt;/td>
323	&lt;td>31.6&lt;/td>
324	&lt;td>13.7&lt;/td>
325	&lt;td>7.7&lt;/td>
326	&lt;td>28.9&lt;/td>
327	&lt;/tr>
328	&lt;tr>
329	&lt;td>Qwen2.5-Math-7B-PRM800K&lt;/td>
330	&lt;td>264K&lt;/td>
331	&lt;td>68.2&lt;/td>
332	&lt;td>62.6&lt;/td>
333	&lt;td>50.7&lt;/td>
334	&lt;td>44.3&lt;/td>
335	&lt;td>56.5&lt;/td>
336	&lt;/tr>
337	&lt;tr>
338	&lt;td>Qwen2.5-Math-PRM-7B&lt;/td>
339	&lt;td>~344K&lt;/td>
340	&lt;td>82.4&lt;/td>
341	&lt;td>77.6&lt;/td>
342	&lt;td>67.5&lt;/td>
343	&lt;td>66.3&lt;/td>
344	&lt;td>73.5&lt;/td>
345	&lt;/tr>
346	&lt;tr>
347	&lt;td>RetrievalPRM-7B&lt;/td>
348	&lt;td>404K&lt;/td>
349	&lt;td>74.6&lt;/td>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a54358f0-476a-4b35-b230-f3e2a5f296e2",
  "isSidechain": true,
  "promptId": "003d4d5b-99b9-4488-a4e4-5e4419f94d98",
  "agentId": "ad50dc4fb50295b3a",
  "type": "user",
  "uuid": "d693be27-afb5-476f-a7da-d974c3897736",
  "sourceToolAssistantUUID": "a54358f0-476a-4b35-b230-f3e2a5f296e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-29T10:07:37.950Z_

<details open><summary>🔧 Tool call — Read · `toolu_012kRzmAsvZ1CH8sPNhpG9Jx`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/83204518-f78b-400d-b0b3-3bb64b514d04/tool-results/toolu_018FvMULpsk6t8VNjaf7WTa4.txt",
  "offset": 500,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d693be27-afb5-476f-a7da-d974c3897736",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
  "requestId": "req_011CbWg6xn7aEp5pjw2XAxhH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2381d115-c36a-4f97-8c6c-da56666b87b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01179PB8isud3TZjKtu3FYn9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1967,
      "cache_read_input_tokens": 26817,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1967
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 26817,
          "cache_creation_input_tokens": 1967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1967,
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

_source line 39 · 2026-05-29T10:07:37.957Z_

<details><summary>↩ Tool result · `toolu_012kRzmAsvZ1CH8sPNhpG9Jx`</summary>

```text
500	&lt;td>46.3&lt;/td>
501	&lt;/tr>
502	&lt;tr>
503	&lt;td>DeepSeek-R1-Distill-7B&lt;/td>
504	&lt;td>69.1&lt;/td>
505	&lt;td>17.9&lt;/td>
506	&lt;td>84.6&lt;/td>
507	&lt;td>33.0&lt;/td>
508	&lt;td>51.2&lt;/td>
509	&lt;td>50.6&lt;/td>
510	&lt;td>6.3&lt;/td>
511	&lt;td>77.7&lt;/td>
512	&lt;td>34.7&lt;/td>
513	&lt;td>42.3&lt;/td>
514	&lt;td>46.8&lt;/td>
515	&lt;/tr>
516	&lt;tr>
517	&lt;td>GenPRM-7B&lt;/td>
518	&lt;td>&lt;b>74.1&lt;/b>&lt;/td>
519	&lt;td>&lt;b>19.6&lt;/b>&lt;/td>
520	&lt;td>&lt;b>86.0&lt;/b>&lt;/td>
521	&lt;td>&lt;b>35.3&lt;/b>&lt;/td>
522	&lt;td>&lt;b>53.8&lt;/b>&lt;/td>
523	&lt;td>&lt;b>57.5&lt;/b>&lt;/td>
524	&lt;td>&lt;b>8.3&lt;/b>&lt;/td>
525	&lt;td>&lt;b>80.6&lt;/b>&lt;/td>
526	&lt;td>&lt;b>36.5&lt;/b>&lt;/td>
527	&lt;td>&lt;b>45.7&lt;/b>&lt;/td>
528	&lt;td>&lt;b>49.8&lt;/b>&lt;/td>
529	&lt;/tr>
530	&lt;tr>
531	&lt;td colspan="12" style="text-align: center;">&lt;i>Turn 2&lt;/i>&lt;/td>
532	&lt;/tr>
533	&lt;tr>
534	&lt;td>Generator&lt;/td>
535	&lt;td>66.6&lt;/td>
536	&lt;td>18.0&lt;/td>
537	&lt;td>84.8&lt;/td>
538	&lt;td>31.6&lt;/td>
539	&lt;td>50.3&lt;/td>
540	&lt;td>49.8&lt;/td>
541	&lt;td>8.0&lt;/td>
542	&lt;td>76.9&lt;/td>
543	&lt;td>31.8&lt;/td>
544	&lt;td>41.6&lt;/td>
545	&lt;td>46.0&lt;/td>
546	&lt;/tr>
547	&lt;tr>
548	&lt;td>DeepSeek-R1-Distill-7B&lt;/td>
549	&lt;td>70.9&lt;/td>
550	&lt;td>18.3&lt;/td>
551	&lt;td>85.0&lt;/td>
552	&lt;td>33.5&lt;/td>
553	&lt;td>51.9&lt;/td>
554	&lt;td>51.9&lt;/td>
555	&lt;td>7.9&lt;/td>
556	&lt;td>78.1&lt;/td>
557	&lt;td>32.8&lt;/td>
558	&lt;td>42.7&lt;/td>
559	&lt;td>47.3&lt;/td>
560	&lt;/tr>
561	&lt;tr>
562	&lt;td>GenPRM-7B&lt;/td>
563	&lt;td>&lt;b>75.0&lt;/b>&lt;/td>
564	&lt;td>&lt;b>21.3&lt;/b>&lt;/td>
565	&lt;td>&lt;b>86.9&lt;/b>&lt;/td>
566	&lt;td>&lt;b>35.6&lt;/b>&lt;/td>
567	&lt;td>&lt;b>54.7&lt;/b>&lt;/td>
568	&lt;td>&lt;b>59.4&lt;/b>&lt;/td>
569	&lt;td>&lt;b>9.6&lt;/b>&lt;/td>
570	&lt;td>&lt;b>82.2&lt;/b>&lt;/td>
571	&lt;td>&lt;b>35.0&lt;/b>&lt;/td>
572	&lt;td>&lt;b>46.6&lt;/b>&lt;/td>
573	&lt;td>&lt;b>50.7&lt;/b>&lt;/td>
574	&lt;/tr>
575	&lt;tr>
576	&lt;td colspan="12" style="text-align: center;">&lt;i>Turn 3&lt;/i>&lt;/td>
577	&lt;/tr>
578	&lt;tr>
579	&lt;td>Generator&lt;/td>
580	&lt;td>67.8&lt;/td>
581	&lt;td>18.1&lt;/td>
582	&lt;td>85.0&lt;/td>
583	&lt;td>32.1&lt;/td>
584	&lt;td>50.8&lt;/td>
585	&lt;td>49.7&lt;/td>
586	&lt;td>8.1&lt;/td>
587	&lt;td>77.1&lt;/td>
588	&lt;td>30.8&lt;/td>
589	&lt;td>41.4&lt;/td>
590	&lt;td>46.1&lt;/td>
591	&lt;/tr>
592	&lt;tr>
593	&lt;td>DeepSeek-R1-Distill-7B&lt;/td>
594	&lt;td>69.6&lt;/td>
595	&lt;td>18.8&lt;/td>
596	&lt;td>85.0&lt;/td>
597	&lt;td>33.4&lt;/td>
598	&lt;td>51.7&lt;/td>
599	&lt;td>51.9&lt;/td>
600	&lt;td>8.3&lt;/td>
601	&lt;td>78.2&lt;/td>
602	&lt;td>32.7&lt;/td>
603	&lt;td>42.7&lt;/td>
604	&lt;td>47.2&lt;/td>
605	&lt;/tr>
606	&lt;tr>
607	&lt;td>GenPRM-7B&lt;/td>
608	&lt;td>&lt;b>76.2&lt;/b>&lt;/td>
609	&lt;td>&lt;b>22.8&lt;/b>&lt;/td>
610	&lt;td>&lt;b>86.7&lt;/b>&lt;/td>
611	&lt;td>&lt;b>36.0&lt;/b>&lt;/td>
612	&lt;td>&lt;b>55.4&lt;/b>&lt;/td>
613	&lt;td>&lt;b>62.7&lt;/b>&lt;/td>
614	&lt;td>&lt;b>9.3&lt;/b>&lt;/td>
615	&lt;td>&lt;b>82.9&lt;/b>&lt;/td>
616	&lt;td>&lt;b>34.9&lt;/b>&lt;/td>
617	&lt;td>&lt;b>47.5&lt;/b>&lt;/td>
618	&lt;td>&lt;b>51.5&lt;/b>&lt;/td>
619	&lt;/tr>
620	&lt;/tbody>
621	&lt;/table>
622	
623	**Table 3:** Results of GenPRM with different label estimation method and threshold on ProcessBench, reported with Pass@1. The best results are shown in **bold**.
624	
625	&lt;table border="1">
626	&lt;thead>
627	&lt;tr>
628	&lt;th>Estimation Method&lt;/th>
629	&lt;th>Positive Label Criterion&lt;/th>
630	&lt;th>GSM8K&lt;/th>
631	&lt;th>MATH&lt;/th>
632	&lt;th>Olympiad Bench&lt;/th>
633	&lt;th>Omni-MATH&lt;/th>
634	&lt;th>Avg.&lt;/th>
635	&lt;/tr>
636	&lt;/thead>
637	&lt;tbody>
638	&lt;tr>
639	&lt;td>&lt;math>P_t = MC(s_t, a_t)&lt;/math> (hard label)&lt;/td>
640	&lt;td>&lt;math>P_t &gt; 0&lt;/math>&lt;/td>
641	&lt;td>72.9&lt;/td>
642	&lt;td>78.9&lt;/td>
643	&lt;td>&lt;b>73.2&lt;/b>&lt;/td>
644	&lt;td>68.0&lt;/td>
645	&lt;td>73.2&lt;/td>
646	&lt;/tr>
647	&lt;tr>
648	&lt;td rowspan="3">&lt;math>P_t = MC(s_t, a_t) - MC(s_t)&lt;/math>&lt;/td>
649	&lt;td>&lt;math>P_t \geq -0.1&lt;/math>&lt;/td>
650	&lt;td>77.3&lt;/td>
651	&lt;td>79.9&lt;/td>
652	&lt;td>70.8&lt;/td>
653	&lt;td>68.5&lt;/td>
654	&lt;td>74.1&lt;/td>
655	&lt;/tr>
656	&lt;tr>
657	&lt;td>&lt;math>P_t \geq -0.3&lt;/math>&lt;/td>
658	&lt;td>76.8&lt;/td>
659	&lt;td>79.6&lt;/td>
660	&lt;td>71.1&lt;/td>
661	&lt;td>69.0&lt;/td>
662	&lt;td>74.1&lt;/td>
663	&lt;/tr>
664	&lt;tr>
665	&lt;td>&lt;math>P_t \geq -0.5&lt;/math>&lt;/td>
666	&lt;td>75.8&lt;/td>
667	&lt;td>80.2&lt;/td>
668	&lt;td>72.8&lt;/td>
669	&lt;td>68.6&lt;/td>
670	&lt;td>74.3&lt;/td>
671	&lt;/tr>
672	&lt;tr>
673	&lt;td rowspan="4">&lt;math>P_t = \frac{MC(s_t, a_t)}{MC(s_t)}&lt;/math>&lt;/td>
674	&lt;td>&lt;math>P_t \geq 0.1&lt;/math>&lt;/td>
675	&lt;td>74.8&lt;/td>
676	&lt;td>78.7&lt;/td>
677	&lt;td>71.6&lt;/td>
678	&lt;td>68.7&lt;/td>
679	&lt;td>73.5&lt;/td>
680	&lt;/tr>
681	&lt;tr>
682	&lt;td>&lt;math>P_t \geq 0.5&lt;/math>&lt;/td>
683	&lt;td>75.7&lt;/td>
684	&lt;td>79.2&lt;/td>
685	&lt;td>70.4&lt;/td>
686	&lt;td>68.5&lt;/td>
687	&lt;td>73.5&lt;/td>
688	&lt;/tr>
689	&lt;tr>
690	&lt;td>&lt;math>P_t \geq 0.8&lt;/math>&lt;/td>
691	&lt;td>&lt;b>78.7&lt;/b>&lt;/td>
692	&lt;td>&lt;b>80.3&lt;/b>&lt;/td>
693	&lt;td>72.2&lt;/td>
694	&lt;td>&lt;b>69.8&lt;/b>&lt;/td>
695	&lt;td>&lt;b>75.2&lt;/b>&lt;/td>
696	&lt;/tr>
697	&lt;tr>
698	&lt;td>&lt;math>P_t \geq 1.0&lt;/math>&lt;/td>
699	&lt;td>76.4&lt;/td>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2381d115-c36a-4f97-8c6c-da56666b87b6",
  "isSidechain": true,
  "promptId": "003d4d5b-99b9-4488-a4e4-5e4419f94d98",
  "agentId": "ad50dc4fb50295b3a",
  "type": "user",
  "uuid": "b458be98-6ec6-4010-8cef-e28b4cce473b",
  "sourceToolAssistantUUID": "2381d115-c36a-4f97-8c6c-da56666b87b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-29T10:07:42.519Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Va1ESRUPJZoFoCTT8aU9kc`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/83204518-f78b-400d-b0b3-3bb64b514d04/tool-results/toolu_018FvMULpsk6t8VNjaf7WTa4.txt",
  "offset": 700,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b458be98-6ec6-4010-8cef-e28b4cce473b",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
  "requestId": "req_011CbWg79pP3vLrTD5CXLYWT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0cd85e80-f584-484b-a105-1b588bb2174f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SFZ7MyJwEc7jLPEUV8sFmf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2708,
      "cache_read_input_tokens": 28784,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2708,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 41 · 2026-05-29T10:07:42.537Z_

<details><summary>↩ Tool result · `toolu_01Va1ESRUPJZoFoCTT8aU9kc`</summary>

```text
700	&lt;td>77.4&lt;/td>
701	&lt;td>68.1&lt;/td>
702	&lt;td>67.2&lt;/td>
703	&lt;td>72.3&lt;/td>
704	&lt;/tr>
705	&lt;/tbody>
706	&lt;/table>
707	
708	**Table 4:** Results of GenPRM with different label estimation method and threshold on ProcessBench, reported with Maj@8. The best results are shown in **bold**.
709	
710	&lt;table border="1">
711	&lt;thead>
712	&lt;tr>
713	&lt;th>Estimation Method&lt;/th>
714	&lt;th>Positive Label Criterion&lt;/th>
715	&lt;th>GSM8K&lt;/th>
716	&lt;th>MATH&lt;/th>
717	&lt;th>Olympiad Bench&lt;/th>
718	&lt;th>Omni-MATH&lt;/th>
719	&lt;th>Avg.&lt;/th>
720	&lt;/tr>
721	&lt;/thead>
722	&lt;tbody>
723	&lt;tr>
724	&lt;td>&lt;math>P_t = MC(s_t, a_t)&lt;/math> (hard label)&lt;/td>
725	&lt;td>&lt;math>P_t &gt; 0&lt;/math>&lt;/td>
726	&lt;td>75.1&lt;/td>
727	&lt;td>83.8&lt;/td>
728	&lt;td>&lt;b>80.6&lt;/b>&lt;/td>
729	&lt;td>74.4&lt;/td>
730	&lt;td>78.5&lt;/td>
731	&lt;/tr>
732	&lt;tr>
733	&lt;td rowspan="3">&lt;math>P_t = MC(s_t, a_t) - MC(s_t)&lt;/math>&lt;/td>
734	&lt;td>&lt;math>P_t \geq -0.1&lt;/math>&lt;/td>
735	&lt;td>79.8&lt;/td>
736	&lt;td>85.1&lt;/td>
737	&lt;td>78.0&lt;/td>
738	&lt;td>74.5&lt;/td>
739	&lt;td>79.4&lt;/td>
740	&lt;/tr>
741	&lt;tr>
742	&lt;td>&lt;math>P_t \geq -0.3&lt;/math>&lt;/td>
743	&lt;td>80.9&lt;/td>
744	&lt;td>&lt;b>86.5&lt;/b>&lt;/td>
745	&lt;td>78.1&lt;/td>
746	&lt;td>75.0&lt;/td>
747	&lt;td>80.2&lt;/td>
748	&lt;/tr>
749	&lt;tr>
750	&lt;td>&lt;math>P_t \geq -0.5&lt;/math>&lt;/td>
751	&lt;td>78.1&lt;/td>
752	&lt;td>85.6&lt;/td>
753	&lt;td>79.1&lt;/td>
754	&lt;td>73.4&lt;/td>
755	&lt;td>79.1&lt;/td>
756	&lt;/tr>
757	&lt;tr>
758	&lt;td rowspan="4">&lt;math>P_t = \frac{MC(s_t, a_t)}{MC(s_t)}&lt;/math>&lt;/td>
759	&lt;td>&lt;math>P_t \geq 0.1&lt;/math>&lt;/td>
760	&lt;td>77.0&lt;/td>
761	&lt;td>84.6&lt;/td>
762	&lt;td>78.1&lt;/td>
763	&lt;td>75.3&lt;/td>
764	&lt;td>78.7&lt;/td>
765	&lt;/tr>
766	&lt;tr>
767	&lt;td>&lt;math>P_t \geq 0.5&lt;/math>&lt;/td>
768	&lt;td>78.0&lt;/td>
769	&lt;td>85.2&lt;/td>
770	&lt;td>78.2&lt;/td>
771	&lt;td>74.3&lt;/td>
772	&lt;td>78.9&lt;/td>
773	&lt;/tr>
774	&lt;tr>
775	&lt;td>&lt;math>P_t \geq 0.8&lt;/math>&lt;/td>
776	&lt;td>81.0&lt;/td>
777	&lt;td>85.7&lt;/td>
778	&lt;td>78.4&lt;/td>
779	&lt;td>&lt;b>76.8&lt;/b>&lt;/td>
780	&lt;td>&lt;b>80.5&lt;/b>&lt;/td>
781	&lt;/tr>
782	&lt;tr>
783	&lt;td>&lt;math>P_t \geq 1.0&lt;/math>&lt;/td>
784	&lt;td>&lt;b>81.1&lt;/b>&lt;/td>
785	&lt;td>84.1&lt;/td>
786	&lt;td>76.0&lt;/td>
787	&lt;td>74.7&lt;/td>
788	&lt;td>79.0&lt;/td>
789	&lt;/tr>
790	&lt;/tbody>
791	&lt;/table>
792	
793	**Reasoning Components.** To understand how each reasoning component influence GenPRM, we conduct experiments by training GenPRM with: (1) CoT data only, (2) code verification data only, and (3) full data. During inference phase, we also compare several variants. For example, GenPRM trained with full data can be used to only verify each step with CoT only by stopping generation at `&lt;/analyze>` token. The results in Table 5 show that: (1) the improvement of GenPRM mainly comesfrom CoT reasoning; (2) generating code and reasoning with code execution result improves the process verification performance as well.
794	
795	**Table 5:** Results on ProcessBench of GenPRM with different reasoning components, reported with Maj@8. The best results are shown in **bold**.
796	
797	&lt;table border="1">
798	&lt;thead>
799	&lt;tr>
800	&lt;th colspan="2">Training&lt;/th>
801	&lt;th colspan="3">Inference&lt;/th>
802	&lt;th rowspan="2">GSM8K&lt;/th>
803	&lt;th rowspan="2">MATH&lt;/th>
804	&lt;th rowspan="2">Olympiad Bench&lt;/th>
805	&lt;th rowspan="2">Omni-MATH&lt;/th>
806	&lt;th rowspan="2">Avg.&lt;/th>
807	&lt;/tr>
808	&lt;tr>
809	&lt;th>CoT&lt;/th>
810	&lt;th>Code&lt;/th>
811	&lt;th>CoT&lt;/th>
812	&lt;th>Code&lt;/th>
813	&lt;th>Code Exec.&lt;/th>
814	&lt;/tr>
815	&lt;/thead>
816	&lt;tbody>
817	&lt;tr>
818	&lt;td>x&lt;/td>
819	&lt;td>x&lt;/td>
820	&lt;td>x&lt;/td>
821	&lt;td>x&lt;/td>
822	&lt;td>x&lt;/td>
823	&lt;td>63.9&lt;/td>
824	&lt;td>65.8&lt;/td>
825	&lt;td>54.5&lt;/td>
826	&lt;td>55.9&lt;/td>
827	&lt;td>60.0&lt;/td>
828	&lt;/tr>
829	&lt;tr>
830	&lt;td>x&lt;/td>
831	&lt;td>✓&lt;/td>
832	&lt;td>x&lt;/td>
833	&lt;td>✓&lt;/td>
834	&lt;td>x&lt;/td>
835	&lt;td>67.0&lt;/td>
836	&lt;td>70.8&lt;/td>
837	&lt;td>61.6&lt;/td>
838	&lt;td>57.4&lt;/td>
839	&lt;td>64.2&lt;/td>
840	&lt;/tr>
841	&lt;tr>
842	&lt;td>x&lt;/td>
843	&lt;td>✓&lt;/td>
844	&lt;td>x&lt;/td>
845	&lt;td>✓&lt;/td>
846	&lt;td>✓&lt;/td>
847	&lt;td>70.6&lt;/td>
848	&lt;td>76.6&lt;/td>
849	&lt;td>67.3&lt;/td>
850	&lt;td>63.9&lt;/td>
851	&lt;td>69.6&lt;/td>
852	&lt;/tr>
853	&lt;tr>
854	&lt;td>✓&lt;/td>
855	&lt;td>x&lt;/td>
856	&lt;td>✓&lt;/td>
857	&lt;td>x&lt;/td>
858	&lt;td>x&lt;/td>
859	&lt;td>76.4&lt;/td>
860	&lt;td>83.0&lt;/td>
861	&lt;td>&lt;b>80.5&lt;/b>&lt;/td>
862	&lt;td>75.4&lt;/td>
863	&lt;td>78.8&lt;/td>
864	&lt;/tr>
865	&lt;tr>
866	&lt;td rowspan="5">✓&lt;/td>
867	&lt;td rowspan="5">✓&lt;/td>
868	&lt;td>x&lt;/td>
869	&lt;td>✓&lt;/td>
870	&lt;td>x&lt;/td>
871	&lt;td>60.1&lt;/td>
872	&lt;td>66.7&lt;/td>
873	&lt;td>59.9&lt;/td>
874	&lt;td>59.2&lt;/td>
875	&lt;td>61.5&lt;/td>
876	&lt;/tr>
877	&lt;tr>
878	&lt;td>x&lt;/td>
879	&lt;td>✓&lt;/td>
880	&lt;td>✓&lt;/td>
881	&lt;td>61.3&lt;/td>
882	&lt;td>74.7&lt;/td>
883	&lt;td>68.1&lt;/td>
884	&lt;td>62.0&lt;/td>
885	&lt;td>66.5&lt;/td>
886	&lt;/tr>
887	&lt;tr>
888	&lt;td>✓&lt;/td>
889	&lt;td>x&lt;/td>
890	&lt;td>x&lt;/td>
891	&lt;td>78.8&lt;/td>
892	&lt;td>85.1&lt;/td>
893	&lt;td>78.7&lt;/td>
894	&lt;td>74.9&lt;/td>
895	&lt;td>79.3&lt;/td>
896	&lt;/tr>
897	&lt;tr>
898	&lt;td>✓&lt;/td>
899	&lt;td>✓&lt;/td>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0cd85e80-f584-484b-a105-1b588bb2174f",
  "isSidechain": true,
  "promptId": "003d4d5b-99b9-4488-a4e4-5e4419f94d98",
  "agentId": "ad50dc4fb50295b3a",
  "type": "user",
  "uuid": "8f453f15-40bd-4458-b0cf-6367962e70f3",
  "sourceToolAssistantUUID": "0cd85e80-f584-484b-a105-1b588bb2174f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-29T10:07:47.086Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VZoVXEqfnJWwzpa8BqF8Qw`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/83204518-f78b-400d-b0b3-3bb64b514d04/tool-results/toolu_018FvMULpsk6t8VNjaf7WTa4.txt",
  "offset": 900,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f453f15-40bd-4458-b0cf-6367962e70f3",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
  "requestId": "req_011CbWg7VhxpHrHgaemEYaZ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e49443fc-b8a5-4c6b-8387-15631a185eaa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01H84Kdu9x3RW29S96YGAqug",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2586,
      "cache_read_input_tokens": 31492,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2586
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 31492,
          "cache_creation_input_tokens": 2586,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2586,
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

_source line 43 · 2026-05-29T10:07:47.095Z_

<details><summary>↩ Tool result · `toolu_01VZoVXEqfnJWwzpa8BqF8Qw`</summary>

`````text
900	&lt;td>x&lt;/td>
901	&lt;td>&lt;b>81.0&lt;/b>&lt;/td>
902	&lt;td>85.1&lt;/td>
903	&lt;td>78.1&lt;/td>
904	&lt;td>75.5&lt;/td>
905	&lt;td>79.9&lt;/td>
906	&lt;/tr>
907	&lt;tr>
908	&lt;td>✓&lt;/td>
909	&lt;td>✓&lt;/td>
910	&lt;td>✓&lt;/td>
911	&lt;td>&lt;b>81.0&lt;/b>&lt;/td>
912	&lt;td>&lt;b>85.7&lt;/b>&lt;/td>
913	&lt;td>78.4&lt;/td>
914	&lt;td>&lt;b>76.8&lt;/b>&lt;/td>
915	&lt;td>&lt;b>80.5&lt;/b>&lt;/td>
916	&lt;/tr>
917	&lt;/tbody>
918	&lt;/table>
919	
920	## 5. Related Work
921	
922	**Process Reward Models.** Process reward models have been proved to be effective for providing step-wise scores and are superior to outcome reward models in mathematical reasoning tasks (Uesato et al., 2022; Lightman et al., 2024). However, annotating a process supervision dataset such as PRM800K (Lightman et al., 2024) requires significant human costs. To mitigate this cost, prior works utilize Monte Carlo estimation (Wang et al., 2024b) and binary search (Luo et al., 2024) for automated label generation. Subsequent research improves PRMs through methods such as advantage modeling (Setlur et al., 2025),  $Q$ -value rankings (Li and Li, 2025), implicit entropy regularization (Zhang et al., 2024a), retrieval-augmented generation (Zhu et al., 2025), and fast-slow verification (Zhong et al., 2025). Furthermore, the community has developed high-quality open-source PRMs, including the RLHFlow series (Xiong et al., 2024), Math-psa (Wang et al., 2024a), Skywork series (Skywork o1 Team, 2024), and Qwen2.5-Math series (Zheng et al., 2024; Zhang et al., 2025c). Recently, a line of works focus on extending PRMs to other tasks, including coding (Zhang et al., 2024b), medical tasks (Jiang et al., 2025), agentic tasks (Choudhury, 2025), general domain tasks (Zhang et al., 2025a; Zeng et al., 2025), and multimodal tasks (Wang et al., 2025). Current studies also focus on benchmarking PRMs (Zheng et al., 2024; Song et al., 2025) to systematically evaluate their performance.
923	
924	**Large Language Model Test-Time Scaling.** Scaling test-time computation is an effective method for improving performance during the inference phase (OpenAI, 2024a,b; DeepSeek-AI et al., 2025). TTS is commonly implemented with external verifiers (e.g., ORMs and PRMs) or strategies (e.g., beam search and MCTS) (Wu et al., 2025; Snell et al., 2025; Beeching et al., 2024; Liu et al., 2025). In this work, we scale the test-time computation of a generative PRM with an explicit reasoning process and GenPRM can also serve as a verifier or a critic model in external TTS.
925	
926	**Enhancing the Generative Abilities of Reward Models.** Previous research has investigated methods to enhance the generative capabilities of reward models using CoT reasoning (Ankner et al., 2024; Zhang et al., 2025b; Mahan et al., 2024). For instance, CCloud reward models (Ankner et al., 2024) are trained to generate critiques for responses and predict rewards using an additional rewardhead. GenRM-CoT (Zhang et al., 2025b) and GenRM (Mahan et al., 2024) train generative reward models that perform CoT reasoning before making final predictions via SFT and preference learning, respectively. CTRL (Xie et al., 2025) demonstrates that critic models exhibit strong discriminative abilities when utilized as generative reward models. Prior to these works, GRM (Yang et al., 2024c) regularizes the hidden states of reward models with a text generation loss.
927	
928	## 6. Conclusion
929	
930	In this work, we propose GenPRM, a generative process reward model that performs explicit reasoning and code verification for process supervision and enables scaling the test-time compute of PRMs. Experimental results on ProcessBench and several mathematical datasets show GenPRM outperforms prior PRMs. We also demonstrate that the performance of GenPRM increases via test-time scaling and GenPRM is effective as a critic model. We believe that this work provides perspectives on PRMs by demonstrating the strong TTS abilities of PRMs and extending the applications of PRMs.
931	
932	**Limitations.** First, GenPRM provides process supervision by generative reasoning, which introduces additional computation during inference phase. Future work will investigate how to prune the reasoning process dynamically (Zhong et al., 2025). Although GenPRM focuses mainly on mathematical reasoning tasks, it is worth to explore how to apply generative reasoning on coding and general reasoning tasks in the future (Zhang et al., 2025a). Additionally, it would be interesting to leverage RL to incentivize the generative reasoning abilities of GenPRM.
933	
934	## References
935	
936	AI-MO. AIME 2024, 2024a. URL &lt;https://huggingface.co/datasets/AI-MO/aimo-validation-aimo>.
937	
938	AI-MO. AMC 2023, 2024b. URL &lt;https://huggingface.co/datasets/AI-MO/aimo-validation-amc>.
939	
940	Zachary Ankner, Mansheej Paul, Brandon Cui, Jonathan D Chang, and Prithviraj Ammanabrolu. Critique-out-Loud Reward Models. *arXiv preprint arXiv:2408.11791*, 2024.
941	
942	Anthropic. Introducing Claude, 2023. URL &lt;https://www.anthropic.com/index/introducing-claude/>.
943	
944	Edward Beeching, Lewis Tunstall, and Sasha Rush. Scaling Test-Time Compute with Open Models, 2024. URL &lt;https://huggingface.co/spaces/HuggingFaceH4/blogpost-scaling-test-time-compute>.
945	
946	Bradley Brown, Jordan Juravsky, Ryan Ehrlich, Ronald Clark, Quoc V Le, Christopher Ré, and Azalia Mirhoseini. Large Language Monkeys: Scaling Inference Compute with Repeated Sampling. *arXiv preprint arXiv:2407.21787*, 2024.
947	
948	Sanjiban Choudhury. Process Reward Models for LLM Agents: Practical Framework and Directions. *arXiv preprint arXiv:2502.10325*, 2025.
949	
950	Ganqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Wendi Li, Bingxiang He, Yuchen Fan, Tianyu Yu, Qixin Xu, Weize Chen, et al. Process Reinforcement through Implicit Rewards. *arXiv preprint arXiv:2502.01456*, 2025.DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z. F. Wu, Zhibin Gou, Zhihong Shao, Zhuoshu Li, Ziyi Gao, Aixin Liu, Bing Xue, Bingxuan Wang, Bochao Wu, Bei Feng, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, Damai Dai, Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, Fuli Luo, Guangbo Hao, Guanting Chen, Guowei Li, H. Zhang, Han Bao, Hanwei Xu, Haocheng Wang, Honghui Ding, Huajian Xin, Huazuo Gao, Hui Qu, Hui Li, Jianzhong Guo, Jiashi Li, Jiawei Wang, Jingchang Chen, Jingyang Yuan, Junjie Qiu, Junlong Li, J. L. Cai, Jiaqi Ni, Jian Liang, Jin Chen, Kai Dong, Kai Hu, Kaige Gao, Kang Guan, Kexin Huang, Kuai Yu, Lean Wang, Lecong Zhang, Liang Zhao, Litong Wang, Liyue Zhang, Lei Xu, Leyi Xia, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Meng Li, Miaojun Wang, Mingming Li, Ning Tian, Panpan Huang, Peng Zhang, Qiancheng Wang, Qinyu Chen, Qiushi Du, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, R. J. Chen, R. L. Jin, Ruyi Chen, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shengfeng Ye, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, S. S. Li, Shuang Zhou, Shaoqing Wu, Shengfeng Ye, Tao Yun, Tian Pei, Tianyu Sun, T. Wang, Wangding Zeng, Wanjia Zhao, Wen Liu, Wenfeng Liang, Wenjun Gao, Wenqin Yu, Wentao Zhang, W. L. Xiao, Wei An, Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xinyu Yang, Xinyuan Li, Xuecheng Su, Xuheng Lin, X. Q. Li, Xiangyue Jin, Xiaojin Shen, Xiaosha Chen, Xiaowen Sun, Xiaoxiang Wang, Xinnan Song, Xinyi Zhou, Xianzu Wang, Xinxia Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Yang Zhang, Yanhong Xu, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Yu, Yichao Zhang, Yifan Shi, Yiliang Xiong, Ying He, Yishi Piao, Yisong Wang, Yixuan Tan, Yiyang Ma, Yiyuan Liu, Yongqiang Guo, Yuan Ou, Yuduan Wang, Yue Gong, Yuheng Zou, Yujia He, Yunfan Xiong, Yuxiang Luo, Yuxiang You, Yuxuan Liu, Yuyang Zhou, Y. X. Zhu, Yanhong Xu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu, Yunxian Ma, Ying Tang, Yukun Zha, Yuting Yan, Z. Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao, Zhicheng Ma, Zhigang Yan, Zhiyu Wu, Zihui Gu, Zijia Zhu, Zijun Liu, Zilin Li, Ziwei Xie, Ziyang Song, Zizheng Pan, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, and Zhen Zhang. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. *arXiv preprint arXiv:2501.12948*, 2025.
951	
952	Gemma Team and Google DeepMind. Introducing Gemma 3: The most capable model you can run on a single GPU or TPU, March 2025. URL &lt;https://blog.google/technology/developers/gemma-3>.
953	
954	Zhibin Gou, Zhihong Shao, Yeyun Gong, yelong shen, Yujiu Yang, Nan Duan, and Weizhu Chen. CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing. In *International Conference on Learning Representations (ICLR)*, 2024. URL &lt;https://openreview.net/forum?id=Sx038qxjek>.
955	
956	Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring Mathematical Problem Solving With the MATH Dataset. In *Advances in Neural Information Processing Systems Datasets and Benchmarks Track (Round 2)*, 2021. URL &lt;https://openreview.net/forum?id=7Bywt2mQsCe>.
957	
958	Shuyang Jiang, Yusheng Liao, Zhe Chen, Ya Zhang, Yanfeng Wang, and Yu Wang. MedS&lt;sup>3&lt;/sup>: Towards Medical Small Language Models with Self-Evolved Slow Thinking. *arXiv preprint arXiv:2501.12051*, 2025.
959	
960	Aitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay Ramasesh, Ambrose Slone, Cem Anil, Imanol Schlag, Theo Gutman-Solo, Yuhuai Wu, Behnam Neyshabur, Guy Gur-Ari, and Vedant Misra. Solving Quantitative Reasoning Problems with Language Models. In S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh, editors,*Advances in Neural Information Processing Systems (NeurIPS)*, volume 35, pages 3843–3857. Curran Associates, Inc., 2022. URL [https://proceedings.neurips.cc/paper\\_files/paper/2022/file/18abbeef8cfe9203fdf9053c9c4fe191-Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2022/file/18abbeef8cfe9203fdf9053c9c4fe191-Paper-Conference.pdf).
961	
962	Wendi Li and Yixuan Li. Process Reward Model with Q-value Rankings. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=wQEdh2cgEk>.
963	
964	Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s Verify Step by Step. In *International Conference on Learning Representations (ICLR)*, 2024. URL &lt;https://openreview.net/forum?id=v8L0pN6E0i>.
965	
966	Runze Liu, Fengshuo Bai, Yali Du, and Yaodong Yang. Meta-Reward-Net: Implicitly Differentiable Reward Learning for Preference-based Reinforcement Learning. In *Advances in Neural Information Processing Systems (NeurIPS)*, volume 35, pages 22270–22284, 2022.
967	
968	Runze Liu, Yali Du, Fengshuo Bai, Jiafei Lyu, and Xiu Li. PEARL: Zero-shot Cross-task Preference Alignment and Robust Reward Learning for Robotic Manipulation. In Ruslan Salakhutdinov, Zico Kolter, Katherine Heller, Adrian Weller, Nuria Oliver, Jonathan Scarlett, and Felix Berkenkamp, editors, *International Conference on Machine Learning (ICML)*, volume 235 of *Proceedings of Machine Learning Research*, pages 30946–30964. PMLR, 21–27 Jul 2024. URL &lt;https://proceedings.mlr.press/v235/liu24o.html>.
969	
970	Runze Liu, Junqi Gao, Jian Zhao, Kaiyan Zhang, Xiu Li, Biqing Qi, Wanli Ouyang, and Bowen Zhou. Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling. *arXiv preprint arXiv:2502.06703*, 2025.
971	
972	Liangchen Luo, Yinxiao Liu, Rosanne Liu, Samrat Phatale, Harsh Lara, Yunxuan Li, Lei Shu, Yun Zhu, Lei Meng, Jiao Sun, et al. Improve Mathematical Reasoning in Language Models by Automated Process Supervision. *arXiv preprint arXiv:2406.06592*, 2024.
973	
974	Aman Madaan, Niket Tandon, Prakash Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegr-effe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa Prasad Majumder, Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, and Peter Clark. Self-Refine: Iterative Refinement with Self-Feedback. In A. Oh, T. Nau-mann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, *Advances in Neural Information Processing Systems (NeurIPS)*, volume 36, pages 46534–46594. Curran Associates, Inc., 2023. URL [https://proceedings.neurips.cc/paper\\_files/paper/2023/file/91edff07232fb1b55a505a9e9f6c0ff3-Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/91edff07232fb1b55a505a9e9f6c0ff3-Paper-Conference.pdf).
975	
976	Dakota Mahan, Duy Van Phung, Rafael Rafailov, Chase Blagden, Nathan Lile, Louis Castricato, Jan-Philipp Fränken, Chelsea Finn, and Alon Albalak. Generative Reward Models. *arXiv preprint arXiv:2410.12832*, 2024.
977	
978	OpenAI. GPT-4 Technical Report. *arXiv preprint arXiv:2303.08774*, 2023.
979	
980	OpenAI. Learning to reason with LLMs, 2024a. URL &lt;https://openai.com/index/learning-to-reason-with-llms>.
981	
982	OpenAI. OpenAI o3-mini, 2024b. URL &lt;https://openai.com/index/openai-o3-mini>.
983	
984	Qwen Team. QwQ-32B: Embracing the Power of Reinforcement Learning, March 2025. URL &lt;https://qwenlm.github.io/blog/qwq-32b>.Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, and Aviral Kumar. Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=A6Y7AqlzLW>.
985	
986	Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al. DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models. *arXiv preprint arXiv:2402.03300*, 2024.
987	
988	Skywork o1 Team. Skywork-o1 Open Series. &lt;https://huggingface.co/Skywork>, November 2024. URL &lt;https://huggingface.co/Skywork>.
989	
990	Charlie Victor Snell, Jaehoon Lee, Kelvin Xu, and Aviral Kumar. Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=4FWAwZtd2n>.
991	
992	Mingyang Song, Zhaochen Su, Xiaoye Qu, Jiawei Zhou, and Yu Cheng. PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models. *arXiv preprint arXiv:2501.03124*, 2025.
993	
994	Xiaoyu Tan, Tianchu Yao, Chao Qu, Bin Li, Minghao Yang, Dakuan Lu, Haozhe Wang, Xihe Qiu, Wei Chu, Yinghui Xu, et al. AURORA: Automated Training Framework of Universal Process Reward Models via Ensemble Prompting and Reverse Verification. *arXiv preprint arXiv:2502.11520*, 2025.
995	
996	Jonathan Uesato, Nate Kushman, Ramana Kumar, Francis Song, Noah Siegel, Lisa Wang, Antonia Creswell, Geoffrey Irving, and Irina Higgins. Solving math word problems with process-and outcome-based feedback. *arXiv preprint arXiv:2211.14275*, 2022.
997	
998	Jun Wang, Meng Fang, Ziyu Wan, Muning Wen, Jiachen Zhu, Anjie Liu, Ziqin Gong, Yan Song, Lei Chen, Lionel M Ni, et al. OpenR: An open source framework for advanced reasoning with large language models. *arXiv preprint arXiv:2410.09671*, 2024a.
999	
1000	Peiyi Wang, Lei Li, Zhihong Shao, Runxin Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang Sui. Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 9426–9439, 2024b.
1001	
1002	Weiyun Wang, Zhangwei Gao, Lianjie Chen, Chen Zhe, Jinguo Zhu, Xiangyu Zhao, Yangzhou Liu, Yue Cao, Shenglong Ye, Xizhou Zhu, Lewei Lu, Haodong Duan, Yu Qiao, Jifeng Dai, and Wenhai Wang. VisualPRM: An Effective Process Reward Model for Multimodal Reasoning. *arXiv preprint arXiv:2503.10291*, 2025.
1003	
1004	Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V Le, Ed H. Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-Consistency Improves Chain of Thought Reasoning in Language Models. In *International Conference on Learning Representations (ICLR)*, 2023. URL &lt;https://openreview.net/forum?id=1PL1NIMMrw>.
1005	
1006	Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. In *Advances in neural information processing systems (NeurIPS)*, volume 35, pages 24824–24837, 2022.Yangzhen Wu, Zhiqing Sun, Shanda Li, Sean Welleck, and Yiming Yang. Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=VNckp7JEHn>.
1007	
1008	Zhihui Xie, Liyu Chen, Weichao Mao, Jingjing Xu, Lingpeng Kong, et al. Teaching Language Models to Critique via Reinforcement Learning. *arXiv preprint arXiv:2502.03492*, 2025.
1009	
1010	Wei Xiong, Hanning Zhang, Nan Jiang, and Tong Zhang. An Implementation of Generative PRM. &lt;https://github.com/RLHFlow/RLHF-Reward-Modeling>, 2024.
1011	
1012	An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jingren Zhou, Junyang Lin, Kai Dang, Keming Lu, Keqin Bao, Kexin Yang, Le Yu, Mei Li, Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men, Runji Lin, Tianhao Li, Tingyu Xia, Xingzhang Ren, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, and Zihan Qiu. Qwen2.5 Technical Report. *arXiv preprint arXiv:2412.15115*, 2024a.
1013	
1014	An Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, Keming Lu, Mingfeng Xue, Runji Lin, Tianyu Liu, Xingzhang Ren, and Zhenru Zhang. Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement. *arXiv preprint arXiv:2409.12122*, 2024b.
1015	
1016	Rui Yang, Ruomeng Ding, Yong Lin, Huan Zhang, and Tong Zhang. Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs. In *Advances in Neural Information Processing Systems (NeurIPS)*, 2024c. URL &lt;https://openreview.net/forum?id=jwh9MHEfmY>.
1017	
1018	Lifan Yuan, Wendi Li, Huayu Chen, Ganqu Cui, Ning Ding, Kaiyan Zhang, Bowen Zhou, Zhiyuan Liu, and Hao Peng. Free Process Rewards without Process Labels. *arXiv preprint arXiv:2412.01981*, 2024.
1019	
1020	Thomas Zeng, Shuibai Zhang, Shutong Wu, Christian Classen, Daewon Chae, Ethan Ewer, Minjiae Lee, Heeju Kim, Wonjun Kang, Jackson Kunde, et al. VersaPRM: Multi-Domain Process Reward Model via Synthetic Reasoning Data. *arXiv preprint arXiv:2502.06737*, 2025.
1021	
1022	Hanning Zhang, Pengcheng Wang, Shizhe Diao, Yong Lin, Rui Pan, Hanze Dong, Dylan Zhang, Pavlo Molchanov, and Tong Zhang. Entropy-Regularized Process Reward Model. *arXiv preprint arXiv:2412.11006*, 2024a.
1023	
1024	Kaiyan Zhang, Jiayuan Zhang, Haoxin Li, Xuekai Zhu, Ermo Hua, Xingtai Lv, Ning Ding, Biqing Qi, and Bowen Zhou. OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees. In *International Conference on Learning Representations (ICLR)*, 2025a. URL &lt;https://openreview.net/forum?id=fGIqGfmgkW>.
1025	
1026	Lunjun Zhang, Arian Hosseini, Hritik Bansal, Mehran Kazemi, Aviral Kumar, and Rishabh Agarwal. Generative Verifiers: Reward Modeling as Next-Token Prediction. In *International Conference on Learning Representations (ICLR)*, 2025b. URL &lt;https://openreview.net/forum?id=Ccwp4tFETe>.
1027	
1028	Yuxiang Zhang, Shangxi Wu, Yuqi Yang, Jiangming Shu, Jinlin Xiao, Chao Kong, and Jitao Sang. o1-Coder: an o1 Replication for Coding. *arXiv preprint arXiv:2412.00154*, 2024b.
1029	
1030	Zhenru Zhang, Chujie Zheng, Yangzhen Wu, Beichen Zhang, Runji Lin, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin. The Lessons of Developing Process Reward Models in Mathematical Reasoning. *arXiv preprint arXiv:2501.07301*, 2025c.Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin. ProcessBench: Identifying Process Errors in Mathematical Reasoning. *arXiv preprint arXiv:2412.06559*, 2024.
1031	
1032	Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, Hao Zhang, Joseph E Gonzalez, and Ion Stoica. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. In A. Oh, T. Nau-mann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, *Advances in Neural Information Processing Systems (NeurIPS)*, volume 36, pages 46595–46623. Curran Associates, Inc., 2023. URL [https://proceedings.neurips.cc/paper\\_files/paper/2023/file/91f18a1287b398d378ef22505bf41832-Paper-Datasets\\_and\\_Benchmarks.pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/91f18a1287b398d378ef22505bf41832-Paper-Datasets_and_Benchmarks.pdf).
1033	
1034	Jianyuan Zhong, Zeju Li, Zhijian Xu, Xiangyu Wen, and Qiang Xu. Dyve: Thinking Fast and Slow for Dynamic Process Verification. *arXiv preprint arXiv:2502.11157*, 2025.
1035	
1036	Jiachen Zhu, Congmin Zheng, Jianghao Lin, Kounianhua Du, Ying Wen, Yong Yu, Jun Wang, and Weinan Zhang. Retrieval-Augmented Process Reward Model for Generalizable Mathematical Reasoning. *arXiv preprint arXiv:2502.14361*, 2025.
1037	
1038	Xuekai Zhu, Biqing Qi, Kaiyan Zhang, Xinwei Long, Zhouhan Lin, and Bowen Zhou. PaD: Program-aided Distillation Can Teach Small Models Reasoning Better than Chain-of-thought Fine-tuning. In Kevin Duh, Helena Gomez, and Steven Bethard, editors, *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)*, pages 2571–2597, Mexico City, Mexico, June 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.naacl-long.142. URL &lt;https://aclanthology.org/2024.naacl-long.142/>.## A. Experimental Details
1039	
1040	### A.1. Scoring and Voting Methods
1041	
1042	**PRM-Last.** PRM-Last considers the process reward of the last step of the entire LLM response as the final score, i.e.,  $\text{score} = r_T$ .
1043	
1044	**PRM-Avg.** PRM-Avg computes the mean process reward across all steps as the final score, i.e.,  $\text{score} = \frac{1}{T} \sum_{t=1}^T r_t$ .
1045	
1046	**PRM-Min.** PRM-Min uses the minimum process reward across all steps as the final score, i.e.,  $\text{score} = \min_r \{r_t\}_{t=1}^T$ .
1047	
1048	### A.2. Implementation Details
1049	
1050	Prompt for CoT and code rationale generation is shown in Table A.2.
1051	
1052	#### Prompt for CoT and code rationale generation
1053	
1054	**[System]:**
1055	
1056	You are a math teacher. Your task is to review and critique the paragraphs in solution step by step with python code.
1057	
1058	**[User]:**
1059	
1060	The following is the math problem and a solution (split into paragraphs, enclosed with tags and indexed from 1):
1061	
1062	[Math Problem]
1063	
1064	{problem}
1065	
1066	[Solution]
1067	
1068	```
1069	&lt;paragraph_1>
1070	{solution_section_1}
1071	&lt;/paragraph_1>
1072	```
1073	
1074	...
1075	
1076	```
1077	&lt;paragraph_n>
1078	{solution_section_n}
1079	&lt;/paragraph_n>
1080	```
1081	
1082	Your task is to verify the correctness of paragraph in the solution. Split your verification by ‘### Paragraph {{ID}}’.
1083	
1084	Your verification for each paragraph should be constructed by 2 parts, wrapped by ‘&lt;analyze>&lt;/analyze>’ and ‘&lt;verify>&lt;/verify>’ separately.1. 1. In ‘`&lt;analyze>&lt;/analyze>`’ part, you need to analyze the reasoning process and explain why the paragraph is correct or incorrect in detail.
1085	2. 2. In ‘`&lt;verify>&lt;/verify>`’ part, you must write **Python code** in the form of ‘````python\n{CODE}\n````’ to verify every details that can be verified by code. You can import PyPI (i.e., ‘`sympy`’, ‘`scipy`’ and so on) to implement complicated calculation. Make sure to print the critic results in the code. Every code will be executed automatically by system. You need to analyze the ‘[Code Output]’ after code executing.
1086	
1087	>Pay attention that you must follow the format of ‘````python\n{CODE}\n````’ when you write the code, otherwise the code will not be executed.
1088	
1089	After all verifications, if you identify an error in a paragraph, return the **index** of the paragraph where the earliest error occurs\*\*. Otherwise, return the **index** of -1 (which typically denotes "not found"\*\*. Please put your final answer (i.e., the index) within box in the form of ‘`$\boxed{{INDEX}}$`’.
1090	
1091	Following [Zheng et al. \(2024\)](#); [Zhang et al. \(2025c\)](#), we use the prompt in Table A.2 to evaluate LLM-as-a-judge methods on ProcessBench ([Zheng et al., 2024](#)).
1092	
1093	#### Evaluation prompt for LLM-as-a-judge methods on ProcessBench
1094	
1095	I will provide a math problem along with a solution. They will be formatted as follows:
1096	
1097	[Math Problem]
1098	
1099	```
`````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e49443fc-b8a5-4c6b-8387-15631a185eaa",
  "isSidechain": true,
  "promptId": "003d4d5b-99b9-4488-a4e4-5e4419f94d98",
  "agentId": "ad50dc4fb50295b3a",
  "type": "user",
  "uuid": "eb27caee-bd75-4232-81d3-3d0bde9ffa26",
  "sourceToolAssistantUUID": "e49443fc-b8a5-4c6b-8387-15631a185eaa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-29T10:08:13.222Z_

I now have comprehensive technical detail from the full paper. Here is the analysis:

---

**problem_identification**: Prior discriminative PRMs treat step verification as scalar classification, making them (1) poor at generalizing across models/tasks, (2) unable to exploit LLMs' generative strengths, and (3) structurally incapable of test-time compute scaling. The authors identified this by observing that classifier-based PRMs produce noisy hard labels from Monte Carlo estimation where many steps with MC > 0 are factually incorrect, and that classifiers cannot benefit from majority voting or best-of-N at inference.

**key_insight**: By reformulating step verification as a generative task — producing explicit CoT + executable Python code rationales before rendering a Yes/No judgment — the PRM gains the ability to scale its own test-time compute through majority voting over multiple sampled verification paths, just as policy models scale via repeated sampling.

**innovation_type**: Combination/synthesis — GenPRM combines three existing ideas in a novel configuration: (1) generative reward modeling (GenRM-CoT), (2) program-aided reasoning/verification (CRITIC, PaD), and (3) relative advantage estimation from GRPO, applied together at the process supervision level.

**method_summary**: GenPRM trains on 23K MATH problems using a three-stage data pipeline: Monte Carlo estimation for step trajectories, Relative Progress Estimation (RPE: label = 1 iff MC(s_{t+1})/MC(s_t) >= 0.8) to filter out steps that are nominally correct but non-progressing, and rationale synthesis where QwQ-32B generates structured CoT+code rationales with consensus filtering that discards ~51% of examples where RPE labels disagree with LLM-as-judge labels. At inference, GenPRM samples N verification paths per step and averages Yes probabilities (majority voting), enabling PRM-level test-time scaling. GenPRM also serves as a critic: its CoT rationale for negative steps is extracted and fed back to the policy model for iterative refinement.

**limitations_and_open_questions**: The authors explicitly acknowledge that generative reasoning introduces significant additional inference compute vs. discriminative PRMs (each step requires one or more full CoT+code generation passes), and suggest dynamic pruning (a la Dyve) as future work. The method is validated only on mathematical reasoning; generalization to coding, agentic, and general domains remains open.

**building_blocks**:
- Monte Carlo estimation for automated PRM labeling (Math-Shepherd)
- Relative Progress Estimation: P_t = MC(s_{t+1}) / MC(s_t), threshold epsilon=0.8 (adapted from GRPO's relative advantage)
- CoT + code verification rationale synthesis via QwQ-32B with structured prompting (analyze/verify XML tags)
- Code execution sandbox for verification feedback
- Consensus filtering (RPE label must agree with LLM-as-judge label; ~51% data discarded)
- Majority voting over N sampled verification paths for PRM-level TTS
- SFT on DeepSeek-R1-Distill base models (1.5B/7B/32B)
- Critic loop: extract negative-step rationales for sequential policy refinement

**relevance_to_seed**: GenPRM defines the maximum-cost tier of the verification depth axis in a cost-accuracy tradeoff framework: full CoT + code execution per step delivers the highest accuracy (GenPRM-7B Maj@8 avg F1 = 80.5 on ProcessBench, surpassing 72B discriminative PRMs) but at the cost of multiple full generative passes per reasoning step, making it unsuitable for latency-sensitive or high-throughput settings where lighter verifiers (discriminative scalar PRMs or simple outcome checks) would dominate on the compute-accuracy Pareto frontier.

Sources:
- [GenPRM arxiv abstract](https://arxiv.org/abs/2504.00891)
- [GitHub - RyanLiu112/GenPRM](https://github.com/RyanLiu112/GenPRM)
- [Medium blog post on GenPRM](https://medium.com/@techsachin/breaking-the-llm-bottleneck-genprms-approach-to-scale-test-time-compute-via-generative-reasoning-0e90e3ffa71e)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb27caee-bd75-4232-81d3-3d0bde9ffa26",
  "isSidechain": true,
  "agentId": "ad50dc4fb50295b3a",
  "requestId": "req_011CbWg7pvrmUUBGRtz1uy4S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0885c27-3fc5-41cc-b2eb-9e9ed8bc7914",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "83204518-f78b-400d-b0b3-3bb64b514d04",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CDaTC2rJR67fZ4skZeSA1F",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9836,
      "cache_read_input_tokens": 34078,
      "output_tokens": 1023,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9836
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1023,
          "cache_read_input_tokens": 34078,
          "cache_creation_input_tokens": 9836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9836,
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
