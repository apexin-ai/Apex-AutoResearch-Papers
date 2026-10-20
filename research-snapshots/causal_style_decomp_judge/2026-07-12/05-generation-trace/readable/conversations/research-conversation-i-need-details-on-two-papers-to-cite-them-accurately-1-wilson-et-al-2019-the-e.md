# Research conversation: I need details on two papers to cite them accurately: 1. **Wilson et al. (2019), "The Eighty Five Percent Rule for Optim

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aedc97a984ac18058.jsonl`
- **Structured JSON:** [`496c082c2d6a89396a3b.json`](../../sessions/49/496c082c2d6a89396a3b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

23 recorded events

### User

_source line 1 · 2026-05-28T16:33:28.907Z_

I need details on two papers to cite them accurately:

1. **Wilson et al. (2019), "The Eighty Five Percent Rule for Optimal Learning"** — published in Nature Communications. What exactly does it prove? The claim is that gradient-based learners in binary classification tasks learn fastest at ~15.87% error rate (not 50%). What's the precise result and how does it relate to p=0.5 symmetry?

2. **Rollout Pass-Rate Control (arXiv:2605.05112)** — What exactly does this paper contribute? I've heard it formalizes 4 independent criteria all showing p=0.5 maximizes GRPO learning signal: reward entropy, group-filtering survival, RLOO advantage energy, and contrastive pair count k(N-k). Get the exact title, authors, and key results.

Search for these papers, read their abstracts, and report:
- Full title and authors
- Key results relevant to my use case
- Any caveats or limitations

Report in under 300 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3fdf0914-321d-49ba-a4b5-3866e437b394",
  "agentId": "aedc97a984ac18058",
  "type": "user",
  "uuid": "ec1ce000-33e0-4877-b110-6ec6b7193273",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e2a6ee4-c608-4da9-8a29-ea30b57d8b30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-28T16:33:28.912Z_

```json
{
  "parentUuid": "ec1ce000-33e0-4877-b110-6ec6b7193273",
  "isSidechain": true,
  "agentId": "aedc97a984ac18058",
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
  "uuid": "e3945b6f-4b83-42fe-9fe5-2c397aa4a3e2",
  "timestamp": "2026-05-28T16:33:28.912Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e2a6ee4-c608-4da9-8a29-ea30b57d8b30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-28T16:33:28.913Z_

```json
{
  "parentUuid": "e3945b6f-4b83-42fe-9fe5-2c397aa4a3e2",
  "isSidechain": true,
  "agentId": "aedc97a984ac18058",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "aac1baa5-58e0-4b44-a4ec-ad999b9dc970",
  "timestamp": "2026-05-28T16:33:28.913Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e2a6ee4-c608-4da9-8a29-ea30b57d8b30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-28T16:33:32.529Z_



I'll search for both papers online.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aac1baa5-58e0-4b44-a4ec-ad999b9dc970",
  "isSidechain": true,
  "agentId": "aedc97a984ac18058",
  "requestId": "req_011CbVHinfyAaMWgMbzRgk52",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48408960-fc76-4c29-b983-e9d6912f61a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e2a6ee4-c608-4da9-8a29-ea30b57d8b30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FN8XUaEizY9rcngUKWb9Y9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1582,
      "cache_read_input_tokens": 7407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1582,
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

_source line 5 · 2026-05-28T16:33:32.831Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VFzcqzoFhr379p7FiU4Dqr`</summary>

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
  "parentUuid": "48408960-fc76-4c29-b983-e9d6912f61a9",
  "isSidechain": true,
  "agentId": "aedc97a984ac18058",
  "requestId": "req_011CbVHinfyAaMWgMbzRgk52",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a02de81d-7528-4340-955a-10cdbb42633a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e2a6ee4-c608-4da9-8a29-ea30b57d8b30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FN8XUaEizY9rcngUKWb9Y9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1582,
      "cache_read_input_tokens": 7407,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1582
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 89,
          "cache_read_input_tokens": 7407,
          "cache_creation_input_tokens": 1582,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1582,
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

_source line 6 · 2026-05-28T16:33:32.836Z_

<details><summary>↩ Tool result · `toolu_01VFzcqzoFhr379p7FiU4Dqr`</summary>

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
  "parentUuid": "a02de81d-7528-4340-955a-10cdbb42633a",
  "isSidechain": true,
  "promptId": "3fdf0914-321d-49ba-a4b5-3866e437b394",
  "agentId": "aedc97a984ac18058",
  "type": "user",
  "uuid": "a5dd65f1-ff0d-4862-b889-bb2d299f68b7",
  "sourceToolAssistantUUID": "a02de81d-7528-4340-955a-10cdbb42633a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e2a6ee4-c608-4da9-8a29-ea30b57d8b30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T16:33:35.334Z_



Now let me search for both papers simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5dd65f1-ff0d-4862-b889-bb2d299f68b7",
  "isSidechain": true,
  "agentId": "aedc97a984ac18058",
  "requestId": "req_011CbVHj5huFYTRaEMkuCrSH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5822c21-768e-4d9e-8d56-af791056ceaa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e2a6ee4-c608-4da9-8a29-ea30b57d8b30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R92W53Y8CrgFp9TECC1WxR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1111,
      "cache_read_input_tokens": 8989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1111,
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

_source line 8 · 2026-05-28T16:33:36.816Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019YZVxN3PcSuDwzKfhnwxR9`</summary>

```json
{
  "query": "Wilson et al 2019 \"The Eighty Five Percent Rule for Optimal Learning\" Nature Communications"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5822c21-768e-4d9e-8d56-af791056ceaa",
  "isSidechain": true,
  "agentId": "aedc97a984ac18058",
  "requestId": "req_011CbVHj5huFYTRaEMkuCrSH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5eb169cf-6cbb-47f6-aedb-acca8b1243da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e2a6ee4-c608-4da9-8a29-ea30b57d8b30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R92W53Y8CrgFp9TECC1WxR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1111,
      "cache_read_input_tokens": 8989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1111,
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

_source line 9 · 2026-05-28T16:33:37.424Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KNpypZvHG7DjUrGKApRwZJ`</summary>

```json
{
  "query": "arXiv 2605.05112 \"Rollout Pass-Rate Control\" GRPO learning signal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5eb169cf-6cbb-47f6-aedb-acca8b1243da",
  "isSidechain": true,
  "agentId": "aedc97a984ac18058",
  "requestId": "req_011CbVHj5huFYTRaEMkuCrSH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a784516e-fe88-433a-be65-429b5715dc2b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e2a6ee4-c608-4da9-8a29-ea30b57d8b30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R92W53Y8CrgFp9TECC1WxR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1111,
      "cache_read_input_tokens": 8989,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1111
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 143,
          "cache_read_input_tokens": 8989,
          "cache_creation_input_tokens": 1111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1111,
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

_source line 10 · 2026-05-28T16:33:42.771Z_

<details><summary>↩ Tool result · `toolu_019YZVxN3PcSuDwzKfhnwxR9`</summary>

```text
Web search results for query: "Wilson et al 2019 "The Eighty Five Percent Rule for Optimal Learning" Nature Communications"

Links: [{"title":"The Eighty Five Percent Rule for optimal learning | Nature Communications","url":"https://www.nature.com/articles/s41467-019-12552-4"},{"title":"The Eighty Five Percent Rule for optimal learning - Princeton University","url":"https://collaborate.princeton.edu/en/publications/the-eighty-five-percent-rule-for-optimal-learning/"},{"title":"The Eighty Five Percent Rule for optimal learning - University of Arizona","url":"https://experts.arizona.edu/en/publications/the-eighty-five-percent-rule-for-optimal-learning"},{"title":"The Eighty Five Percent Rule for optimal learning","url":"https://repository.arizona.edu/handle/10150/636293"},{"title":"85% Rule of Optimal Learning. Science has discovered the sweet spot… | by Drenizë Rama | Medium","url":"https://medium.com/@drenizerama/85-rule-of-optimal-learning-15581eca9842"},{"title":"(PDF) The Eighty Five Percent Rule for optimal learning","url":"https://www.researchgate.net/publication/337036886_The_Eighty_Five_Percent_Rule_for_optimal_learning"},{"title":"Learning is optimized when we fail 15% of the time | ScienceDaily","url":"https://www.sciencedaily.com/releases/2019/11/191105113457.htm"},{"title":"The Eighty Five Percent Rule for optimal learning","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6831579/"}]

I found the paper you're looking for! Here are the search results:

The article "The Eighty Five Percent Rule for optimal learning" was published by Wilson, R.C., Shenhav, A., Straccia, M. et al. in Nature Communications, volume 10, article 4646 (2019).

The paper is available through multiple sources:
- **Official Nature Communications article**: https://www.nature.com/articles/s41467-019-12552-4
- **PubMed Central**: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6831579/
- **DOI**: 10.1038/s41467-019-12552-4

**Key findings**: The study found that for stochastic gradient-descent based learning algorithms, the optimal error rate for training is around 15.87%, or conversely, that optimal training accuracy is about 85%, and demonstrated this "Eighty Five Percent Rule" for both artificial neural networks used in AI and biologically plausible neural networks thought to describe animal learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5eb169cf-6cbb-47f6-aedb-acca8b1243da",
  "isSidechain": true,
  "promptId": "3fdf0914-321d-49ba-a4b5-3866e437b394",
  "agentId": "aedc97a984ac18058",
  "type": "user",
  "uuid": "0b2704cd-94bb-4ea4-81e8-c5a274e306c8",
  "sourceToolAssistantUUID": "5eb169cf-6cbb-47f6-aedb-acca8b1243da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e2a6ee4-c608-4da9-8a29-ea30b57d8b30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-28T16:33:45.708Z_

<details><summary>↩ Tool result · `toolu_01KNpypZvHG7DjUrGKApRwZJ`</summary>

```text
Web search results for query: "arXiv 2605.05112 "Rollout Pass-Rate Control" GRPO learning signal"

Links: [{"title":"[2605.05112] Rollout Pass-Rate Control: Steering Binary-Reward RL Toward Its Most Informative Regime","url":"https://arxiv.org/abs/2605.05112"},{"title":"Rollout Pass-Rate Control: Steering Binary-Reward RL Toward Its Most Informative Regime","url":"https://arxiv.org/html/2605.05112v1"},{"title":"Prompt replay: speeding up grpo with on-policy reuse of high-signal prompts","url":"https://arxiv.org/pdf/2603.21177"},{"title":"Exploring Pass-Rate Reward in Reinforcement Learning for Code Generation","url":"https://arxiv.org/html/2605.02944"},{"title":"Train Less, Learn More: Adaptive Efficient Rollout Optimization for Group-Based Reinforcement Learning","url":"https://arxiv.org/pdf/2602.14338"},{"title":"Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/pdf/2601.22478"}]

I found the paper! Here are the key details:

arXiv paper 2605.05112, titled "Rollout Pass-Rate Control: Steering Binary-Reward RL Toward Its Most Informative Regime," was authored by Tianshu Zhu and colleagues from Baidu.

**Main Contribution:**

The paper shows that the binary reward-side signal is strongest near a 50% rollout pass rate under four criteria: reward entropy, group-filtering survival, leave-one-out (RLOO) advantage energy under Group Relative Policy Optimization (GRPO), and success-failure pair count.

**Problem & Solution:**

The paper addresses the inefficiency in agentic reinforcement learning for software engineering, where much compute is spent on stateful trajectories with highly skewed and weakly contrastive grouped binary rewards. The authors propose Prefix Sampling (PS), which replays self-generated trajectory prefixes to steer skewed groups toward the 50% pass-rate regime: successful prefixes give mostly failing groups a head start, while failing prefixes handicap mostly passing groups.

The paper demonstrates that optimizing for a 50% pass rate creates the strongest learning signal for GRPO and other binary-reward RL algorithms in code generation and software engineering tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a784516e-fe88-433a-be65-429b5715dc2b",
  "isSidechain": true,
  "promptId": "3fdf0914-321d-49ba-a4b5-3866e437b394",
  "agentId": "aedc97a984ac18058",
  "type": "user",
  "uuid": "9082f4de-7487-47fe-85b3-b907b5921dfa",
  "sourceToolAssistantUUID": "a784516e-fe88-433a-be65-429b5715dc2b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e2a6ee4-c608-4da9-8a29-ea30b57d8b30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-28T16:33:48.868Z_

Now let me fetch the actual paper pages for more precise details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9082f4de-7487-47fe-85b3-b907b5921dfa",
  "isSidechain": true,
  "agentId": "aedc97a984ac18058",
  "requestId": "req_011CbVHk2REcSYTbXZotWbS8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c270d8a-cb87-4232-bc0d-2d70c693805d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e2a6ee4-c608-4da9-8a29-ea30b57d8b30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F4MepRkp9NTtmWwUk4eJ4c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1494,
      "cache_read_input_tokens": 10100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1494,
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

_source line 13 · 2026-05-28T16:33:51.041Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FBWM5vVMBmAqZeQ8pvjbKF`</summary>

```json
{
  "url": "https://www.nature.com/articles/s41467-019-12552-4",
  "prompt": "Extract: full list of authors, the precise mathematical result (what is the optimal error rate and how is it derived — specifically its relationship to 1/e and p=0.5), and any stated limitations or caveats."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c270d8a-cb87-4232-bc0d-2d70c693805d",
  "isSidechain": true,
  "agentId": "aedc97a984ac18058",
  "requestId": "req_011CbVHk2REcSYTbXZotWbS8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be60a019-9648-48bd-a4c2-2088be3afdb5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e2a6ee4-c608-4da9-8a29-ea30b57d8b30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F4MepRkp9NTtmWwUk4eJ4c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1494,
      "cache_read_input_tokens": 10100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1494,
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

_source line 14 · 2026-05-28T16:33:51.586Z_

<details><summary>↩ Tool result · `toolu_01FBWM5vVMBmAqZeQ8pvjbKF`</summary>

```text
REDIRECT DETECTED: The URL redirects to a different host.

Original URL: https://www.nature.com/articles/s41467-019-12552-4
Redirect URL: https://idp.nature.com/authorize?response_type=cookie&client_id=grover&redirect_uri=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41467-019-12552-4
Status: 303 See Other

To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
- url: "https://idp.nature.com/authorize?response_type=cookie&client_id=grover&redirect_uri=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41467-019-12552-4"
- prompt: "Extract: full list of authors, the precise mathematical result (what is the optimal error rate and how is it derived — specifically its relationship to 1/e and p=0.5), and any stated limitations or caveats."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be60a019-9648-48bd-a4c2-2088be3afdb5",
  "isSidechain": true,
  "promptId": "3fdf0914-321d-49ba-a4b5-3866e437b394",
  "agentId": "aedc97a984ac18058",
  "type": "user",
  "uuid": "7b997f8c-c3b9-4e46-b185-89688ac8b5c0",
  "sourceToolAssistantUUID": "be60a019-9648-48bd-a4c2-2088be3afdb5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e2a6ee4-c608-4da9-8a29-ea30b57d8b30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-28T16:33:53.196Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0144uNHoz7sRdtRyZyf3bVCq`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.05112",
  "prompt": "Extract: full title, complete author list, and the four criteria that all peak at p=0.5. Also extract any caveats or limitations mentioned. Report the exact mathematical expressions if available (e.g. k(N-k) for contrastive pairs)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b997f8c-c3b9-4e46-b185-89688ac8b5c0",
  "isSidechain": true,
  "agentId": "aedc97a984ac18058",
  "requestId": "req_011CbVHk2REcSYTbXZotWbS8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0aa4bee2-45f6-4a76-93cd-25d88c58e96c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e2a6ee4-c608-4da9-8a29-ea30b57d8b30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F4MepRkp9NTtmWwUk4eJ4c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1494,
      "cache_read_input_tokens": 10100,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1494
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 271,
          "cache_read_input_tokens": 10100,
          "cache_creation_input_tokens": 1494,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1494,
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

_source line 16 · 2026-05-28T16:33:58.338Z_

<details><summary>↩ Tool result · `toolu_0144uNHoz7sRdtRyZyf3bVCq`</summary>

```text
# Paper Extraction Summary

**Full Title:** "Rollout Pass-Rate Control: Steering Binary-Reward RL Toward Its Most Informative Regime"

**Complete Author List:** Tianshu Zhu, Wenyu Zhang, Xiaoying Zuo, Lun Tian, Haotian Zhao, Yucheng Zeng, Jingnan Gu, Daxiang Dong, Jianmin Wu, Dawei Yin, Dou Shen

**Four Criteria Peaking at 50% Pass Rate:**
1. Reward entropy
2. Group-filtering survival
3. Leave-one-out (RLOO) advantage energy under Group Relative Policy Optimization (GRPO)
4. Success-failure pair count

**Mathematical Expressions:** The abstract does not provide explicit mathematical formulas for these criteria. The document mentions "success-failure pair count" but does not express it as k(N-k) or similar notation.

**Caveats/Limitations Mentioned:**
- The method is evaluated specifically on software engineering tasks (SWE-bench Verified and AIME 2025)
- Results show "evaluation variability" considerations
- The approach requires "reconstructed" states through existing rollout paths
- Gains are attributed to specific components in ablations: "replay, bidirectional coverage, and adaptive control"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0aa4bee2-45f6-4a76-93cd-25d88c58e96c",
  "isSidechain": true,
  "promptId": "3fdf0914-321d-49ba-a4b5-3866e437b394",
  "agentId": "aedc97a984ac18058",
  "type": "user",
  "uuid": "f4330596-0259-46a3-b743-ed31c07f19d1",
  "sourceToolAssistantUUID": "0aa4bee2-45f6-4a76-93cd-25d88c58e96c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e2a6ee4-c608-4da9-8a29-ea30b57d8b30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-28T16:34:02.753Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013X3ieANi3Zdo5j26txv91w`</summary>

```json
{
  "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6831579/",
  "prompt": "Extract: full list of authors, the precise mathematical result for the optimal error rate (how 15.87% is derived, its relationship to 1/e), and any stated limitations or caveats. Also clarify: does the result apply only to binary classification with gradient descent? What is the connection to p=0.5?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4330596-0259-46a3-b743-ed31c07f19d1",
  "isSidechain": true,
  "agentId": "aedc97a984ac18058",
  "requestId": "req_011CbVHkxRAD1ZtNCYk18ydE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7290b9a4-c236-4ebd-bde2-3e7652a8d164",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e2a6ee4-c608-4da9-8a29-ea30b57d8b30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018kpPNjqp7BHrQQGwWeQq39",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 917,
      "cache_read_input_tokens": 11594,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 917,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
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

_source line 18 · 2026-05-28T16:34:03.468Z_

<details><summary>↩ Tool result · `toolu_013X3ieANi3Zdo5j26txv91w`</summary>

```text
REDIRECT DETECTED: The URL redirects to a different host.

Original URL: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6831579/
Redirect URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC6831579/
Status: 301 Moved Permanently

To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
- url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC6831579/"
- prompt: "Extract: full list of authors, the precise mathematical result for the optimal error rate (how 15.87% is derived, its relationship to 1/e), and any stated limitations or caveats. Also clarify: does the result apply only to binary classification with gradient descent? What is the connection to p=0.5?"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7290b9a4-c236-4ebd-bde2-3e7652a8d164",
  "isSidechain": true,
  "promptId": "3fdf0914-321d-49ba-a4b5-3866e437b394",
  "agentId": "aedc97a984ac18058",
  "type": "user",
  "uuid": "ca423fea-1bfd-437f-a598-5fc406b83a7b",
  "sourceToolAssistantUUID": "7290b9a4-c236-4ebd-bde2-3e7652a8d164",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e2a6ee4-c608-4da9-8a29-ea30b57d8b30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-28T16:34:04.067Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VzT9FzFqGsukXWFvWD2V3v`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.05112v1",
  "prompt": "Extract the precise mathematical expressions for the four criteria that peak at p=0.5: reward entropy, group-filtering survival, RLOO advantage energy, and contrastive pair count k(N-k). Report exact formulas. Also report any caveats or limitations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca423fea-1bfd-437f-a598-5fc406b83a7b",
  "isSidechain": true,
  "agentId": "aedc97a984ac18058",
  "requestId": "req_011CbVHkxRAD1ZtNCYk18ydE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a3c9f10-c832-4c06-8689-49f50f49137d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e2a6ee4-c608-4da9-8a29-ea30b57d8b30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018kpPNjqp7BHrQQGwWeQq39",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 917,
      "cache_read_input_tokens": 11594,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 917
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 11594,
          "cache_creation_input_tokens": 917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 917,
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

_source line 20 · 2026-05-28T16:34:09.636Z_

<details><summary>↩ Tool result · `toolu_01VzT9FzFqGsukXWFvWD2V3v`</summary>

````text
# Mathematical Expressions for p=0.5 Optimality

## Four Peak Criteria

**1. Reward Entropy**
```
H(p) = -p log₂(p) - (1-p) log₂(1-p)
Maximized at: p = 0.5
```

**2. Group-Filtering Survival Probability**
```
S_N(p) = Pr(0 < K < N) = 1 - p^N - (1-p)^N
Maximized at: p = 0.5
```

**3. RLOO Advantage Energy**
```
E_RLOO(k) = k(N-k)/(N-1)²
Maximized at: k = N/2
```

**4. Contrastive Pair Count**
```
C(k) = k(N-k)
Maximized at: k = N/2
```

## Key Caveats

The paper explicitly states these measures identify "the binary reward-side signal available to a grouped policy-gradient update" and do not claim that "every global curriculum, every rollout count N, or every controller hyperparameter schedule is globally optimal."

Additional limitations noted:
- Claims are scoped to binary-reward RLVR with grouped rollouts using N=8 configurations
- The 50% target applies during training, not necessarily as a final model success rate
- Results depend on implementation-specific framework details for stateful agents
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a3c9f10-c832-4c06-8689-49f50f49137d",
  "isSidechain": true,
  "promptId": "3fdf0914-321d-49ba-a4b5-3866e437b394",
  "agentId": "aedc97a984ac18058",
  "type": "user",
  "uuid": "c4a8323f-a037-44df-a1fc-089573f973ea",
  "sourceToolAssistantUUID": "2a3c9f10-c832-4c06-8689-49f50f49137d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e2a6ee4-c608-4da9-8a29-ea30b57d8b30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-28T16:34:12.741Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HsSzYCehCTr26LJhWyuXXU`</summary>

```json
{
  "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6831579/",
  "prompt": "Extract: full list of authors, the precise mathematical result for the optimal error rate (how 15.87% is derived, its relationship to 1/e), and any stated limitations or caveats. Does the result apply only to binary classification with gradient descent? What is the connection to p=0.5?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4a8323f-a037-44df-a1fc-089573f973ea",
  "isSidechain": true,
  "agentId": "aedc97a984ac18058",
  "requestId": "req_011CbVHmnn185NzbjzGgkqCU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55a17763-a28b-4536-8a17-1c66ab218284",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e2a6ee4-c608-4da9-8a29-ea30b57d8b30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9MkHbFpWNSwGY6DM4w1xi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1006,
      "cache_read_input_tokens": 12511,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1006
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 158,
          "cache_read_input_tokens": 12511,
          "cache_creation_input_tokens": 1006,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1006,
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

_source line 22 · 2026-05-28T16:34:19.591Z_

<details><summary>↩ Tool result · `toolu_01HsSzYCehCTr26LJhWyuXXU`</summary>

```text
# The Eighty Five Percent Rule: Key Details

## Authors
Robert C Wilson, Amitai Shenhav, Mark Straccia, and Jonathan D Cohen

## Mathematical Derivation of 15.87%

The optimal error rate emerges from maximizing the learning gradient ∂ER/∂β. For Gaussian noise, the paper derives:

**ER* = ½(1 − erf(1/√2)) ≈ 0.1587**

This connects to 1/e through the standard normal distribution. The constant arises because the optimal difficulty occurs where βΔ* = 1, making the cumulative distribution function F(−1) yield approximately 15.87%.

## Scope and Limitations

**Applies specifically to:**
- "Binary classification tasks" with "stochastic gradient-descent based learning algorithms"
- The analysis assumes Gaussian noise in the decision variable representation

**Important caveats stated:**
- Different noise distributions yield different optima (82% for Laplacian noise, 75% for Cauchy)
- "Batch-based training changes the optimal accuracy"
- Extensions to "multi-category" tasks would be more complex
- Assumes noise affects only the scale factor β, not the noise form itself

The authors note that "Bayesian learners with perfect memory" show no optimal difficulty, demonstrating the result is specific to gradient-based approaches.

## No Connection to p=0.5

The document contains no discussion of p=0.5 or probability relationships beyond error rate thresholds.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55a17763-a28b-4536-8a17-1c66ab218284",
  "isSidechain": true,
  "promptId": "3fdf0914-321d-49ba-a4b5-3866e437b394",
  "agentId": "aedc97a984ac18058",
  "type": "user",
  "uuid": "1a46cc12-5b1a-465a-bd10-cd7b48286860",
  "sourceToolAssistantUUID": "55a17763-a28b-4536-8a17-1c66ab218284",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e2a6ee4-c608-4da9-8a29-ea30b57d8b30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-28T16:34:39.027Z_

I now have all the details needed. Here is the report.

---

**Paper 1: The Eighty Five Percent Rule for Optimal Learning**

- **Authors:** Robert C. Wilson, Amitai Shenhav, Mark Straccia, Jonathan D. Cohen
- **Published:** Nature Communications 10, 4646 (2019)

**Key result:** For binary classification with stochastic gradient descent under Gaussian noise, the learning rate (gradient magnitude dER/d-beta) is maximized when difficulty is tuned so the error rate equals ER* = 1/2(1 - erf(1/sqrt(2))) = ~15.87%. This is not 50% -- it arises because the steepest point of the Gaussian CDF is at one standard deviation, not at the midpoint of [0,1]. The 85% accuracy figure is specific to Gaussian noise; Laplacian noise gives ~82%, Cauchy ~75%. The result does not apply to Bayesian learners with perfect memory, batch training changes the optimum, and multi-class extensions are unaddressed. There is no direct connection to p=0.5 symmetry in this paper.

**Paper 2: Rollout Pass-Rate Control: Steering Binary-Reward RL Toward Its Most Informative Regime**

- **Authors:** Tianshu Zhu, Wenyu Zhang, Xiaoying Zuo, Lun Tian, Haotian Zhao, Yucheng Zeng, Jingnan Gu, Daxiang Dong, Jianmin Wu, Dawei Yin, Dou Shen
- **Published:** arXiv:2605.05112

**Key result:** Four independent measures of binary-reward learning signal under grouped rollouts all peak at pass-rate p=0.5:
1. **Reward entropy:** H(p) = -p log p - (1-p) log(1-p), maximized at p=0.5
2. **Group-filtering survival:** S_N(p) = 1 - p^N - (1-p)^N, maximized at p=0.5
3. **RLOO advantage energy:** k(N-k)/(N-1)^2, maximized at k=N/2
4. **Contrastive pair count:** k(N-k), maximized at k=N/2

They propose Prefix Sampling (PS) to steer skewed groups toward p=0.5. **Caveats:** scoped to binary-reward RLVR with grouped rollouts (N=8); does not claim global optimality across all curricula or hyperparameter schedules; evaluated on SWE-bench Verified and AIME 2025 only.

**Important distinction:** Wilson's 85% rule and this paper's 50% rule are not contradictory -- they optimize different quantities (single-example gradient magnitude vs. group-level reward contrast in GRPO).

Sources:
- [The Eighty Five Percent Rule - Nature Communications](https://www.nature.com/articles/s41467-019-12552-4)
- [The Eighty Five Percent Rule - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6831579/)
- [Rollout Pass-Rate Control - arXiv](https://arxiv.org/abs/2605.05112)
- [Rollout Pass-Rate Control - HTML](https://arxiv.org/html/2605.05112v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a46cc12-5b1a-465a-bd10-cd7b48286860",
  "isSidechain": true,
  "agentId": "aedc97a984ac18058",
  "requestId": "req_011CbVHnXLbVxLjQfMAS64kb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b7aaf9b-e03d-4d7b-8324-3c8ef22b97f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e2a6ee4-c608-4da9-8a29-ea30b57d8b30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018mwSD3YBpqQtWHQVDNSUSW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 522,
      "cache_read_input_tokens": 13517,
      "output_tokens": 835,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 522
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 835,
          "cache_read_input_tokens": 13517,
          "cache_creation_input_tokens": 522,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 522,
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
