# Research conversation: I need to research the paper "From Chains to DAGs" with arXiv ID 2601.17593 (January 2026). It reportedly probes DAG str

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a654e0ba71297ac88.jsonl`
- **Structured JSON:** [`ab478f9b7dd443917f53.json`](../../sessions/ab/ab478f9b7dd443917f53.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-19T09:57:05.741Z_

I need to research the paper "From Chains to DAGs" with arXiv ID 2601.17593 (January 2026). It reportedly probes DAG structure in LLM reasoning representations.

Please do the following:
1. Search for "From Chains to DAGs arXiv 2601.17593", "DAG structure LLM reasoning probing representations", "chain of thought DAG dependency structure probing 2026"
2. Fetch and read the paper from https://arxiv.org/abs/2601.17593
3. Extract:
   - Exact title, authors, venue
   - Core method: How does it probe/extract DAG structures from reasoning chains? What specific algorithm or approach?
   - What kind of DAGs does it find — what are nodes and edges?
   - How reliable is the DAG extraction? Any failure modes discussed?
   - Key results and evaluation
   - Could this method be used as a component in another system to convert reasoning chains to DAGs?

This is critical because a reviewer asked us to specify how we'd construct DAGs from reasoning chains, and this paper may provide the method.

Report all findings in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c803892c-5106-4584-8104-83ba36b7b3b2",
  "agentId": "a654e0ba71297ac88",
  "type": "user",
  "uuid": "849627f0-f4be-4d3c-9ec4-63053cd5f0f2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T09:57:05.745Z_

```json
{
  "parentUuid": "849627f0-f4be-4d3c-9ec4-63053cd5f0f2",
  "isSidechain": true,
  "agentId": "a654e0ba71297ac88",
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
  "uuid": "119df487-360b-4d67-82dc-db32b330bbbd",
  "timestamp": "2026-05-19T09:57:05.745Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T09:57:05.745Z_

```json
{
  "parentUuid": "119df487-360b-4d67-82dc-db32b330bbbd",
  "isSidechain": true,
  "agentId": "a654e0ba71297ac88",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "22012e51-8982-4ab1-b88f-5fcb7811df7f",
  "timestamp": "2026-05-19T09:57:05.745Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T09:57:08.468Z_



I'll research this paper thoroughly. Let me start by searching for it and fetching the arXiv page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22012e51-8982-4ab1-b88f-5fcb7811df7f",
  "isSidechain": true,
  "agentId": "a654e0ba71297ac88",
  "requestId": "req_011CbBjDPNesvUGT5YCNB2xe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b44c4200-fd83-4b36-a139-71d301688a61",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017V3ARqVfpASKoJEwdVvN1g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1596,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1596,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 5 · 2026-05-19T09:57:09.008Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HPrP4Y6fXnu8jTHLi2nx1W`</summary>

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
  "parentUuid": "b44c4200-fd83-4b36-a139-71d301688a61",
  "isSidechain": true,
  "agentId": "a654e0ba71297ac88",
  "requestId": "req_011CbBjDPNesvUGT5YCNB2xe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84e84a97-2e97-4937-b34e-47cbc806863d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017V3ARqVfpASKoJEwdVvN1g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1596,
      "cache_read_input_tokens": 7773,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1596
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 104,
          "cache_read_input_tokens": 7773,
          "cache_creation_input_tokens": 1596,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1596,
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

_source line 6 · 2026-05-19T09:57:09.011Z_

<details><summary>↩ Tool result · `toolu_01HPrP4Y6fXnu8jTHLi2nx1W`</summary>

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
  "parentUuid": "84e84a97-2e97-4937-b34e-47cbc806863d",
  "isSidechain": true,
  "promptId": "c803892c-5106-4584-8104-83ba36b7b3b2",
  "agentId": "a654e0ba71297ac88",
  "type": "user",
  "uuid": "a093e35c-fcef-45ad-810e-9587125e7cc2",
  "sourceToolAssistantUUID": "84e84a97-2e97-4937-b34e-47cbc806863d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T09:57:11.645Z_



Now let me run all the searches and fetch the paper in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a093e35c-fcef-45ad-810e-9587125e7cc2",
  "isSidechain": true,
  "agentId": "a654e0ba71297ac88",
  "requestId": "req_011CbBjDdZwCmYkfD1296hMc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07d97e26-237b-4138-9242-bb3fe956c88f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L1KNNqdr4Z9K2YywPYN9Rr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9369,
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

_source line 8 · 2026-05-19T09:57:11.791Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013fy99L6TvP9WyjnieT9Q7V`</summary>

```json
{
  "query": "From Chains to DAGs arXiv 2601.17593"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07d97e26-237b-4138-9242-bb3fe956c88f",
  "isSidechain": true,
  "agentId": "a654e0ba71297ac88",
  "requestId": "req_011CbBjDdZwCmYkfD1296hMc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6566f766-8525-4dfd-9830-774179deda71",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L1KNNqdr4Z9K2YywPYN9Rr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9369,
      "output_tokens": 82,
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
          "output_tokens": 82,
          "cache_read_input_tokens": 9369,
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

_source line 9 · 2026-05-19T09:57:17.073Z_

<details><summary>↩ Tool result · `toolu_013fy99L6TvP9WyjnieT9Q7V`</summary>

```text
Web search results for query: "From Chains to DAGs arXiv 2601.17593"

Links: [{"title":"[2601.17593] From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/abs/2601.17593"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/html/2601.17593"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260117593Z/abstract"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/pdf/2601.17593"},{"title":"DAGs: Chains, Forks, Association, and Inverted Forks. From top to... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/DAGs-Chains-Forks-Association-and-Inverted-Forks-From-top-to-bottom-the-following_fig1_328753326"}]

I found the paper! Here are the details:

**Title:** From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs

**Authors:** Tianjun Zhong, Linyang He, and Nima Mesgarani from Columbia University

**Main Contribution:** The paper introduces Reasoning DAG Probing, a framework for testing whether LLM hidden states linearly encode properties of an underlying reasoning DAG and where this structure emerges across layers. They train lightweight probes to predict node depth, pairwise distance, and adjacency from hidden states.

**Key Motivation:** While prior work often treats reasoning as a linear chain, many reasoning problems are more naturally modeled as directed acyclic graphs (DAGs), where intermediate conclusions branch, merge, and are reused. Whether such graph structure is reflected in model internals remains unclear.

**Key Findings:** The researchers found that DAG structure is meaningfully encoded in LLM representations, with recoverability peaking in intermediate layers, varying systematically by node depth, edge span, and model scale. These findings suggest that LLM reasoning is not purely sequential, but exhibits measurable internal graph structure.

The paper was submitted on January 24, 2026 and last revised on April 5, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6566f766-8525-4dfd-9830-774179deda71",
  "isSidechain": true,
  "promptId": "c803892c-5106-4584-8104-83ba36b7b3b2",
  "agentId": "a654e0ba71297ac88",
  "type": "user",
  "uuid": "3ea1cce1-4c6d-4ff3-ace6-cab7c760d0dc",
  "sourceToolAssistantUUID": "6566f766-8525-4dfd-9830-774179deda71",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T09:57:20.030Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K9X6q46chc3LH9LNynJF6F`</summary>

```json
{
  "query": "DAG structure LLM reasoning probing representations 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ea1cce1-4c6d-4ff3-ace6-cab7c760d0dc",
  "isSidechain": true,
  "agentId": "a654e0ba71297ac88",
  "requestId": "req_011CbBjEDpi64ZTg33dBnSU2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "064e7bfc-9655-467e-abf3-174693f38904",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JxF3jvzL1WHGXnMCkCUEvq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 704,
      "cache_read_input_tokens": 10495,
      "output_tokens": 64,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 704
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 64,
          "cache_read_input_tokens": 10495,
          "cache_creation_input_tokens": 704,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 704,
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

_source line 11 · 2026-05-19T09:57:28.734Z_

<details><summary>↩ Tool result · `toolu_01K9X6q46chc3LH9LNynJF6F`</summary>

```text
Web search results for query: "DAG structure LLM reasoning probing representations 2026"

Links: [{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/html/2601.17593"},{"title":"GRaM workshop at ICLR 2026 Tiny Paper Track HYPERBOLIC GEOMETRY OF REASONING:","url":"https://openreview.net/pdf/1798e4ecb1f83df49d622b20bb88ad79af3b29d9.pdf"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/pdf/2601.17593"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260117593Z/abstract"},{"title":"[2601.17593] From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/abs/2601.17593"},{"title":"DAG-Math: Graph-of-Thought Guided Mathematical Reasoning in LLMs | OpenReview","url":"https://openreview.net/forum?id=ylr6WArKQN"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=ylr6WArKQN"},{"title":"ThoughtProbe: Classifier-Guided LLM Thought Space Exploration via Probing Representations","url":"https://arxiv.org/pdf/2510.27355"}]

Based on the search results, here's what I found about DAG structure, LLM reasoning, and probing representations in 2026:

## Key Research: "From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs"

A framework called Reasoning DAG Probing was introduced to examine whether and where large language models encode graph-structured reasoning in their internal representations. The framework directly asks whether LLM hidden states encode the geometry of a reasoning DAG in a linearly accessible form, and uses lightweight probes to predict graph-theoretic properties like node depth and pairwise node distance from hidden states.

## Main Findings

Across reasoning benchmarks, DAG structure is meaningfully encoded in LLM representations, with recoverability peaking in intermediate layers, varying systematically by node depth, edge span, and model scale, and enabling nontrivial recovery of dependency graphs. These findings suggest that LLM reasoning is not purely sequential, but exhibits measurable internal graph structure.

## Related Work: DAG-Math

Additionally, another 2026 research direction proposes modeling Chain-of-Thought as a rule-based stochastic process over directed acyclic graphs (DAGs), where nodes represent intermediate derivation states and edges encode rule applications.

These 2026 developments represent a shift from viewing LLM reasoning as purely sequential chains to understanding its underlying graph-structured nature through internal representation analysis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "064e7bfc-9655-467e-abf3-174693f38904",
  "isSidechain": true,
  "promptId": "c803892c-5106-4584-8104-83ba36b7b3b2",
  "agentId": "a654e0ba71297ac88",
  "type": "user",
  "uuid": "b022e1ca-c055-4d0b-9d7c-9ed2747a34c3",
  "sourceToolAssistantUUID": "064e7bfc-9655-467e-abf3-174693f38904",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T09:57:31.041Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QkZ9YPPvorjbV1vTz7chr5`</summary>

```json
{
  "query": "chain of thought DAG dependency structure probing 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b022e1ca-c055-4d0b-9d7c-9ed2747a34c3",
  "isSidechain": true,
  "agentId": "a654e0ba71297ac88",
  "requestId": "req_011CbBjF5hai5ygmDJKTgbP1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8113a84-050a-461d-9d29-cbb6d8c36329",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VKDKZR1jhTqjsSPzYwwYUQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 11199,
      "output_tokens": 63,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 829
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 63,
          "cache_read_input_tokens": 11199,
          "cache_creation_input_tokens": 829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 829,
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

_source line 13 · 2026-05-19T09:57:38.043Z_

<details><summary>↩ Tool result · `toolu_01QkZ9YPPvorjbV1vTz7chr5`</summary>

```text
Web search results for query: "chain of thought DAG dependency structure probing 2026"

Links: [{"title":"GRaM workshop at ICLR 2026 Tiny Paper Track HYPERBOLIC GEOMETRY OF REASONING:","url":"https://openreview.net/pdf/1798e4ecb1f83df49d622b20bb88ad79af3b29d9.pdf"},{"title":"[2601.17593] From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/abs/2601.17593"},{"title":"PROBING AND STEERING CHAIN-OF-THOUGHT UN","url":"https://openreview.net/attachment?id=LocRunEIxK&name=pdf"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/pdf/2601.17593"},{"title":"DAG-Math: Graph-Guided Mathematical Reasoning in LLMs","url":"https://arxiv.org/html/2510.19842v1"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260117593Z/abstract"},{"title":"Task–Skill Dependency Graph Overview","url":"https://www.emergentmind.com/topics/task-skill-dependency-graph"}]

Based on the search results, here's what I found about chain of thought DAG dependency structure probing in 2026:

## Key Research: "From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs"

A framework called "Reasoning DAG Probing" tests whether LLM hidden states linearly encode properties of an underlying reasoning DAG and where this structure emerges across layers.

### Methodology

The research associates each reasoning node with a textual realization and trains lightweight probes to predict node depth, pairwise distance, and adjacency from hidden states, then analyzes the emergence of DAG structure across layers, reconstructs approximate reasoning graphs, and evaluates controls that disrupt reasoning-relevant structure while preserving surface text.

### Key Findings

Across reasoning benchmarks, DAG structure is meaningfully encoded in LLM representations, with recoverability peaking in intermediate layers, varying systematically by node depth, edge span, and model scale, and enabling nontrivial recovery of dependency graphs, suggesting that LLM reasoning is not purely sequential, but exhibits measurable internal graph structure.

### Context

While prior work often treats reasoning as a linear chain, many reasoning problems are more naturally modeled as directed acyclic graphs (DAGs), where intermediate conclusions branch, merge, and are reused.

This work by Zhong et al. (arXiv:2601.17593) represents a significant advancement in understanding how language models internally represent complex, non-linear reasoning processes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8113a84-050a-461d-9d29-cbb6d8c36329",
  "isSidechain": true,
  "promptId": "c803892c-5106-4584-8104-83ba36b7b3b2",
  "agentId": "a654e0ba71297ac88",
  "type": "user",
  "uuid": "3472da70-73f2-460f-8d07-0ee2c087fff4",
  "sourceToolAssistantUUID": "e8113a84-050a-461d-9d29-cbb6d8c36329",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-19T09:57:41.017Z_

Good, I have the overview. Now let me fetch the full paper content for detailed extraction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3472da70-73f2-460f-8d07-0ee2c087fff4",
  "isSidechain": true,
  "agentId": "a654e0ba71297ac88",
  "requestId": "req_011CbBjFmVjN8yup9K6YHdQ5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c4f72fa-9c65-4e2f-8b37-502e4ac2b4d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013x3A5MaQ5VkxCv3y73CpXM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 12028,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 786,
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

_source line 15 · 2026-05-19T09:57:42.296Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01G13xTuZebEk2tvL2Xt6KX8`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.17593",
  "prompt": "Extract ALL details from this paper page: exact title, all authors and affiliations, submission/revision dates, venue if mentioned, and the full abstract. Also extract any links to the full paper or HTML version."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c4f72fa-9c65-4e2f-8b37-502e4ac2b4d3",
  "isSidechain": true,
  "agentId": "a654e0ba71297ac88",
  "requestId": "req_011CbBjFmVjN8yup9K6YHdQ5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5963e386-2132-4bea-81e1-b5591dde0604",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013x3A5MaQ5VkxCv3y73CpXM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 12028,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 786,
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

_source line 16 · 2026-05-19T09:57:47.199Z_

<details><summary>↩ Tool result · `toolu_01G13xTuZebEk2tvL2Xt6KX8`</summary>

```text
# Paper Details

**Title:** "From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs"

**Authors:**
- Tianjun Zhong
- Linyang He
- Nima Mesgarani

*Note: No institutional affiliations are explicitly listed on this page.*

**Submission & Revision Dates:**
- Initial submission: January 24, 2026
- Latest revision (v2): April 5, 2026

**Venue:** Computer Science > Computation and Language (cs.CL)

**arXiv Identifier:** 2601.17593

**Abstract Summary:**
The paper introduces a framework called Reasoning DAG Probing to investigate whether large language models internally encode directed acyclic graph (DAG) structures during multi-step reasoning. Rather than treating reasoning as linear chains, the authors test if LLM hidden states reflect graph-like properties (node depth, pairwise distance, adjacency). Key findings indicate that "DAG structure is meaningfully encoded in LLM representations, with recoverability peaking in intermediate layers."

**Paper Access Links:**
- PDF: https://arxiv.org/pdf/2601.17593
- HTML (experimental): https://arxiv.org/html/2601.17593v2
- TeX Source: https://arxiv.org/src/2601.17593
- DOI: https://doi.org/10.48550/arXiv.2601.17593
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5963e386-2132-4bea-81e1-b5591dde0604",
  "isSidechain": true,
  "promptId": "c803892c-5106-4584-8104-83ba36b7b3b2",
  "agentId": "a654e0ba71297ac88",
  "type": "user",
  "uuid": "ed566b9d-08da-42c3-8892-e4c13056dce2",
  "sourceToolAssistantUUID": "5963e386-2132-4bea-81e1-b5591dde0604",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T09:57:54.828Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015h9pQCasm2TjSp5yQ1pnyL`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.17593v2",
  "prompt": "Extract the FULL content of this paper in detail. I need:\n\n1. EXACT full abstract text\n2. All section headings and their content\n3. The CORE METHOD in detail: How exactly does \"Reasoning DAG Probing\" work? What are the steps? What algorithm is used? How are DAGs constructed from reasoning chains? What are the probing classifiers/regressors?\n4. What are the NODES and EDGES in the DAGs? How are they defined?\n5. What datasets/benchmarks are used?\n6. What models are probed?\n7. KEY RESULTS: All numerical results, accuracy scores, metrics\n8. FAILURE MODES: Any limitations, failure cases, or reliability concerns discussed\n9. How is adjacency/edge prediction done? What is the graph reconstruction approach?\n10. Any discussion of using this as a component in other systems\n\nPlease be as detailed and exhaustive as possible. Include specific numbers, formulas, algorithm descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed566b9d-08da-42c3-8892-e4c13056dce2",
  "isSidechain": true,
  "agentId": "a654e0ba71297ac88",
  "requestId": "req_011CbBjGShAfKWJLMAiUvEcd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "246b634e-2c22-409b-99bc-be34e432a284",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AAbubtpRDmZ242UbCzmu4J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 492,
      "cache_read_input_tokens": 12814,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 492
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 298,
          "cache_read_input_tokens": 12814,
          "cache_creation_input_tokens": 492,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 492,
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

_source line 18 · 2026-05-19T09:58:43.515Z_

<details><summary>↩ Tool result · `toolu_015h9pQCasm2TjSp5yQ1pnyL`</summary>

```text
# Detailed Extraction: "From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs"

## 1. EXACT FULL ABSTRACT

"Recent progress in large language models has renewed interest in how multi-step reasoning is represented internally. While prior work often treats reasoning as a linear chain, many reasoning problems are more naturally modeled as directed acyclic graphs (DAGs), where intermediate conclusions branch, merge, and are reused. Whether such graph structure is reflected in model internals remains unclear.

We introduce *Reasoning DAG Probing*, a framework for testing whether LLM hidden states linearly encode properties of an underlying reasoning DAG and where this structure emerges across layers. We associate each reasoning node with a textual realization and train lightweight probes to predict node depth, pairwise distance, and adjacency from hidden states. Using these probes, we analyze the emergence of DAG structure across layers, reconstruct approximate reasoning graphs, and evaluate controls that disrupt reasoning-relevant structure while preserving surface text. Across reasoning benchmarks, we find that DAG structure is meaningfully encoded in LLM representations, with recoverability peaking in intermediate layers, varying systematically by node depth, edge span, and model scale, and enabling nontrivial recovery of dependency graphs. These findings suggest that LLM reasoning is not purely sequential, but exhibits measurable internal graph structure."

---

## 2. CORE METHOD: REASONING DAG PROBING

### 2.1 DAG Construction Pipeline

**Input**: Multi-step reasoning problem (theory, query, proof)

**Process**:
- Formalize proof as directed acyclic graph G=(V,E)
- Nodes (V): premises, intermediate conclusions, final answer
- Edges (E): directed edges from premise nodes to conclusion nodes
- Each node v associated with its statement text as textual realization

**Example (ProofWriter)**: Theory contains facts and rules; a query generates a proof DAG where edges represent rule applications linking premises to derived conclusions.

### 2.2 Three Core Probing Targets

#### A. NODE DEPTH

**Definition**: For node v in graph G with sink node s:

- Raw depth: d_raw(v,s) = longest directed path length from v to s
- Normalized depth: depth(v) = max_u∈V d_raw(u,s) - d_raw(v,s)
- Result: sink has maximal depth; premises are shallow

**Rationale**: Longest path captures maximum inference steps a node participates in; avoids collapsing multi-premise dependencies.

#### B. PAIRWISE DISTANCE

**Definition**: For nodes u, v:
dist(u,v) = dist(v,u) = max(d_raw(u,v), d_raw(v,u))

Where d_raw(u,v) is longest directed path from u to v; undefined if no path exists.

**Purpose**: Measures geometric separation between nodes in dependency structure.

#### C. PAIRWISE ADJACENCY

**Definition**: 
adj(u,v) = {1 if (u,v)∈E or (v,u)∈E; 0 otherwise}

**Purpose**: Indicates direct edge presence regardless of direction.

### 2.3 Representation Extraction

**Process**:
1. Concatenate full theory 𝒯 and node textual realization x_v
2. Tokenize with offset mappings to identify x_v token span
3. For layer ℓ, extract hidden states {h_t^(ℓ)} for all tokens in span(v)
4. Mean-pool across token span: **z**_v^(ℓ) = (1/|span(v)|) Σ h_t^(ℓ)
5. Result: single node representation vector in ℝ^d per layer

### 2.4 Probe Architectures

**All probes**: Low-rank linear maps (rank k=1) without bias, trained with AdamW on frozen representations.

**DEPTH PROBE**:
- Predicts scalar: depth^(v) = **w**^T **z**_v
- Training: Pairwise ranking loss for depth(u)=depth(v)+1 pairs
- Loss: ℒ_depth = softplus(-(depth^(u) - depth^(v)))
- Evaluation: Spearman correlation (Depth_Spearman)

**DISTANCE PROBE**:
- Input: Absolute difference |**z**_u - **z**_v|
- Predicts: Graph distance via linear map
- Loss: Mean-squared error against annotated distances
- Evaluation: Spearman correlation (Dist_Spearman)

**ADJACENCY PROBE**:
- Score: s_uv = **w**^T |**z**_u - **z**_v|
- Prediction: sigmoid(s_uv) → adj^(u,v) ∈ [0,1]
- Loss: Binary cross-entropy with positive-class weighting
- Evaluation: Average precision (Adj_AvgPrc)

### 2.5 Graph Reconstruction Algorithm

**Input**: Probe predictions for all nodes and pairs

**Step 1—Sink identification**:
ŝ = arg max_v∈V depth^(v)

**Step 2—Candidate edge generation**:
- Consider all node pairs {u,v}
- Orient edges based on predicted depth ordering (shallower→deeper)
- Associate each with predicted distance and adjacency scores

**Step 3—Edge addition (two-stage)**:

*Stage A*: For each non-sink node, add its best outgoing candidate edge (highest adjacency probability; distance as tiebreaker).

*Stage B*: Add remaining candidates satisfying both thresholds:
dist^(u,v) ≤ τ_dist AND adj^(u,v) ≥ τ_adj

**Result**: Acyclic graph by construction (edges ordered by depth).

**Threshold selection**: τ_dist and τ_adj chosen on dev set to maximize edge F1.

---

## 3. DATASETS & DAG SOURCES

### Primary: ProofWriter
- Rule-based natural language inference
- Contains: Theory (facts, rules), query, proof
- Proof formalized as explicit DAG
- Nodes: proof statements (premises, intermediates, final answer)
- Edges: premise→conclusion from rule applications

### Secondary: GSM8K
- Grade-school math word problems
- Problem: No explicit proof structure
- Solution: GPT-5 mini prompted to extract reasoning DAGs from worked answers
- Nodes: Necessary reasoning statements from question/answer
- Edges: Premise-to-conclusion dependencies
- Purpose: Out-of-domain generalization test

---

## 4. MODELS PROBED

**Primary**: Qwen3 family (Yang et al., 2025)
- 1B, 3B, 4B, 8B, 14B, 32B variants
- Decoder-only transformer models

**Additional models** (Appendix D):
- K2-Think (32B)
- Ministral-3-14B-Reasoning-2512
- DeepSeek-R1-Distill-Llama-8B
- Llama-3.2-3B

**Generation setup**:
- Prompt: Full theory + query with "&lt;answer> true/false &lt;/answer>" tag
- Generation: Up to 1024 tokens, stochastic decoding
- Answer extraction: First token after &lt;answer> tag

---

## 5. KEY RESULTS

### 5.1 Layerwise Emergence (Figure 2a)

**Qwen3-14B on ProofWriter**:

| Metric | Pattern |
|--------|---------|
| Depth_Spearman | Peaks ~0.75 in intermediate layers (8-18) |
| Dist_Spearman | Peaks ~0.65 in intermediate layers |
| Adj_AvgPrc | Peaks ~0.70 in intermediate layers |

**Pattern**: Early layers weak → rapid improvement → strong intermediate peak → mild decline in late layers.

### 5.2 Baseline Comparisons (Figure 2b)

Peak performance across all layers:

| Method | Depth_Spearman | Dist_Spearman | Adj_AvgPrc |
|--------|-----------------|---------------|-----------|
| Full method | ~0.75 | ~0.65 | ~0.70 |
| Node-only | ~0.35 | ~0.25 | ~0.40 |
| Bag-of-words | ~0.15 | ~0.10 | ~0.25 |
| Label-shuffled | ~0.05 | ~0.02 | ~0.05 |

**Interpretation**: Structure recovery depends on contextualized full-theory representations, not surface text.

### 5.3 DAG Reconstruction Performance (Figure 2c)

Edge-level F1 across thresholds:
- Optimal performance: τ_dist = moderate-to-large, τ_adj = moderate range
- Peak F1: ~0.55-0.60 (intermediate layers)
- Pattern: Broad high-performance region over threshold space

### 5.4 Depth-Dependent Recoverability (Figure 3a)

Mean absolute error grouped by node depth:

**Key finding**: Layer of minimal error shifts systematically with depth
- Shallow nodes (depth 0-1): Best recovered in early layers (0-5)
- Deep nodes (depth 4-5): Best recovered in late-intermediate layers (15-25)
- Pattern: Diagonal banding—deeper representations encoded later in network

### 5.5 Span-Dependent Adjacency (Figure 3b)

Average precision grouped by edge depth gap:

- Small gaps (depth gap 1): High performance from layer 10 onward
- Large gaps (depth gap 5): Saturate much later (layer 25+)
- Pattern: Diagonal transition—longer-range edges encoded progressively deeper

**Interpretation**: Long-range dependencies become recoverable only after later processing stages.

### 5.6 Scaling Behavior (Figure 4)

**Model size dependence**:
- 1B: Depth_Spearman ~0.60, Dist ~0.50, Adj ~0.62
- 14B: Depth_Spearman ~0.75, Dist ~0.65, Adj ~0.70
- 32B: Depth_Spearman ~0.77, Dist ~0.67, Adj ~0.72
- Trend: Consistent improvement, approaching saturation around 8B+

**Training recipe dependence** (fixed 4B scale):
- Base model: Baseline performance
- Instruction-tuned: +2-3% improvement
- Reasoning-optimized: +3-5% improvement
- Finding: Minor effect vs. scale; pretraining dominant factor

### 5.7 DAG Recoverability vs. Generation Correctness (Figure 5)

Distributions of probing metrics by generation outcome:

**Correct generations**:
- Mean Depth_Spearman: ~0.65
- Mean Dist_Spearman: ~0.55
- Mean Adj_AvgPrc: ~0.62

**Incorrect generations**:
- Mean Depth_Spearman: ~0.58
- Mean Dist_Spearman: ~0.48
- Mean Adj_AvgPrc: ~0.55

**Incomplete generations**:
- Substantially weaker across all metrics
- Substantial overlap with correct group

**Key finding**: Modest distributional differences; DAG recoverability neither sufficient nor guaranteed for correctness.

### 5.8 Cross-Model Consistency (Appendix D)

All tested model families exhibit:
- Intermediate-layer peak structure
- Progressive emergence pattern
- Qualitative consistency despite scale/recipe differences

---

## 6. FAILURE MODES & LIMITATIONS

### 6.1 Explicit Limitations (Appendix A)

**Dataset scope**: Framework requires explicit proof structure (limits applicability to structured reasoning tasks like ProofWriter; harder for open-ended reasoning).

**Annotation richness**: Current framework probes depth, distance, adjacency; richer annotations could extend to rule types, edge semantics, etc.

**Test-time applicability**: DAG structure not directly observable for arbitrary user queries; requires either:
- Structured prompting
- Auxiliary supervision
- Representation-level interventions

### 6.2 Reconstruction Gaps

**Edge precision-recall tradeoff**:
- Recall consistently > Precision (high coverage, lower selectivity)
- Many spurious edges predicted in later layers
- Only moderate F1 (~0.55-0.60 peak)

**Threshold sensitivity**:
- Reconstruction quality dependent on τ_dist and τ_adj selection
- Requires development set tuning

### 6.3 Generation Correctness Decoupling

"Correct generations tend to have slightly higher probe scores on average, but the separation is limited and varies by metric... DAG recoverability alone is not sufficient for correct generation."

**Implication**: Internal structure encoding ≠ output reliability; downstream decoding processes still critical.

### 6.4 Late-Layer Degradation

"In the final layers, performance mildly declines, possibly reflecting a shift toward objectives less aligned with reasoning structure, though this remains speculative."

**Mechanism unclear**: Late-layer decline suggests representational focus shifts away from DAG geometry toward other objectives (output generation, etc.).

### 6.5 Generalization Constraints

**GSM8K results** (Appendix K):
- Out-of-domain application requires GPT-5 mini to construct DAGs from worked solutions
- DAG construction itself is external inference step, not ground truth
- Qualitative trends similar to ProofWriter, but lower absolute magnitudes

---

## 7. TECHNICAL DETAILS

### 7.1 Probing Setup Summary

| Component | Specification |
|-----------|-----------------|
| Probe rank | k=1 (low-capacity) |
| Bias | None |
| Optimizer | AdamW |
| Frozen model | Yes (probes only) |
| Model selection | Dev loss, task-specific hyperparameters |
| Depth loss | Pairwise ranking (softplus) |
| Distance loss | MSE |
| Adjacency loss | BCE with positive weighting |

### 7.2 Representation Details

- Mean-pooling across token span (not CLS or first token)
- Full theory context always included
- Hidden state extraction: All 42+ layers per model
- Evaluation metrics: Spearman (ranked), Average Precision (binary)

### 7.3 Alternative Training Objectives (Appendix E)

**Regression**: Direct MSE on scalar depth values
- Result: Similar qualitative patterns to ranking
- Slightly weaker late-layer stability

**Classification**: 6-way classification (depths 0-5)
- Result: Underperforms ranking; discretization loses ordinal structure
- Weaker sink identification

**Conclusion**: Ranking objective most stable; continuous objectives superior to discrete.

---

## 8. DISCUSSION POINTS

### Reasoning as Progressive Graph Construction

"Results support a view in which reasoning involves the progressive formation of structured dependencies during computation, rather than being captured solely by a linear trace."

### Localization of Reasoning Computation

"Reasoning-relevant structure is not uniformly distributed across the network... The depth- and span-dependent shifts further suggest that deeper nodes and longer-range dependencies become recoverable later in the network, pointing to partial localization of reasoning computation."

### Relation to Chain-of-Thought

"A linear rationale can be viewed as a projection of an underlying dependency structure... This helps explain why faithful reasoning need not correspond to a unique textual explanation, and why generated rationales may vary without implying inconsistency."

### Model Design Implications

"Structured dependency information may provide a target for model design, training, and control. Architectures or objectives that preserve or expose internal graph structure could improve interpretability."

---

## 9. CASE STUDY: PROOFWRITER EXAMPLE

**Theory**: Facts about Dave, Erin, Fiona, Gary; rules like "If someone is green and red then they are nice."

**Query**: "Fiona is nice."

**Proof DAG nodes**:
- C0: "Fiona is cold" (premise)
- C1: "Fiona is green" (from rule: cold→green)
- C2: "Fiona is young" (from rule: green→young)
- C3: "Fiona is smart" (from rule: green∧young→smart)
- C4: "Fiona is red" (from rule: smart→red)
- C5: "Fiona is nice" (sink, from rule: green∧red→nice)

**Key observations**:
- Long-range edge: C1→C5 spans multiple inference steps
- Longest-path depth justification: C1 participates in extended chain despite direct support path
- Why distance thresholds needed: Valid edges span multiple depth gaps

---

## 10. QUANTITATIVE SUMMARY TABLE

| Aspect | Finding |
|--------|---------|
| Intermediate-layer peak | Consistent across all metrics, all models |
| Baseline robustness | Full method ~3-5× baselines |
| Scaling trend | Logarithmic; saturation ~8B |
| Training recipe effect | <5% improvement vs. base |
| Depth ordering accuracy | Spearman ~0.75 peak |
| Edge reconstruction F1 | ~0.55-0.60 peak |
| Correct-vs-incorrect separation | Overlapping distributions; modest effect |
| Cross-model consistency | Qualitative alignment across families |

---

## 11. COMPONENT USE IN DOWNSTREAM SYSTEMS

**Potential applications** (from discussion):
1. **Structured decoding**: Align generation with recovered DAGs
2. **Auxiliary supervision**: Use layer-wise probes to train better representations
3. **Interventions**: Selectively preserve/enhance reasoning layers
4. **Interpretability**: Localize reasoning computation for mechanistic analysis
5. **Prompt engineering**: Leverage internal structure knowledge for prompt design

**Current limitation**: Requires explicit DAG annotations at training/evaluation time.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "246b634e-2c22-409b-99bc-be34e432a284",
  "isSidechain": true,
  "promptId": "c803892c-5106-4584-8104-83ba36b7b3b2",
  "agentId": "a654e0ba71297ac88",
  "type": "user",
  "uuid": "ccd516cd-f68d-4ec5-9999-af445cd91d96",
  "sourceToolAssistantUUID": "246b634e-2c22-409b-99bc-be34e432a284",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-19T09:58:46.475Z_

This is extremely detailed. Let me also search for any additional context about the venue and whether there's a code repository.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccd516cd-f68d-4ec5-9999-af445cd91d96",
  "isSidechain": true,
  "agentId": "a654e0ba71297ac88",
  "requestId": "req_011CbBjLbSPDpyyp3kPAdHHR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b1514b2-cf98-4c69-8bae-b0ad2d6e8b92",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JvwbKNqu9553ApbbHKmX5j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4670,
      "cache_read_input_tokens": 13306,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4670,
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

_source line 20 · 2026-05-19T09:58:47.576Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FCHryTGkF2XYK5r3SW8TpF`</summary>

```json
{
  "query": "\"From Chains to DAGs\" Zhong He Mesgarani Columbia University venue ICLR ACL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b1514b2-cf98-4c69-8bae-b0ad2d6e8b92",
  "isSidechain": true,
  "agentId": "a654e0ba71297ac88",
  "requestId": "req_011CbBjLbSPDpyyp3kPAdHHR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7794b29-a09e-4efd-befb-84070bb9e3c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JvwbKNqu9553ApbbHKmX5j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4670,
      "cache_read_input_tokens": 13306,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4670
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 13306,
          "cache_creation_input_tokens": 4670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4670,
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

_source line 21 · 2026-05-19T09:58:54.307Z_

<details><summary>↩ Tool result · `toolu_01FCHryTGkF2XYK5r3SW8TpF`</summary>

```text
Web search results for query: ""From Chains to DAGs" Zhong He Mesgarani Columbia University venue ICLR ACL 2026"

Links: [{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260117593Z/abstract"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/pdf/2601.17593"},{"title":"[2601.17593] From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/abs/2601.17593"},{"title":"Using Minimum Path Cover to Boost Dynamic Programming on DAGs: Co-Linear   Chaining Extended","url":"https://arxiv.org/pdf/1705.08754"},{"title":"Fast and Practical DAG Decomposition with Reachability Applications","url":"https://arxiv.org/pdf/2212.03945"}]

Based on the search results, I found information about "From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs."

The paper is by Tianjun Zhong, Linyang He, and Nima Mesgarani from Columbia University. The work introduces "Reasoning DAG Probing," a framework for testing whether LLM hidden states linearly encode properties of an underlying reasoning DAG and where this structure emerges across layers.

The researchers find that DAG structure is meaningfully encoded in LLM representations, with recoverability peaking in intermediate layers, varying systematically by node depth, edge span, and model scale, and enabling nontrivial recovery of dependency graphs.

However, I was unable to find specific information about the venue (ICLR or ACL) or confirmation of a 2026 conference presentation in the search results. The paper appears to be a recent preprint (dated April 5, 2026 on arXiv), but the search results don't contain details about where it has been or will be presented.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7794b29-a09e-4efd-befb-84070bb9e3c8",
  "isSidechain": true,
  "promptId": "c803892c-5106-4584-8104-83ba36b7b3b2",
  "agentId": "a654e0ba71297ac88",
  "type": "user",
  "uuid": "f3087255-a1b6-43ab-b133-1209d3de9a49",
  "sourceToolAssistantUUID": "c7794b29-a09e-4efd-befb-84070bb9e3c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T09:58:58.047Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NyzJXV1PFoeNgQdJw3zptd`</summary>

```json
{
  "query": "\"From Chains to DAGs\" github code repository reasoning DAG probing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3087255-a1b6-43ab-b133-1209d3de9a49",
  "isSidechain": true,
  "agentId": "a654e0ba71297ac88",
  "requestId": "req_011CbBjMPZYCQAx1mmyr1rCp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12582ae4-4db9-4b78-8c24-5b657c1ca4b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011b8mgmKDce8GrxkU3JL1B8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 636,
      "cache_read_input_tokens": 17976,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 636
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 17976,
          "cache_creation_input_tokens": 636,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 636,
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

_source line 23 · 2026-05-19T09:59:05.827Z_

<details><summary>↩ Tool result · `toolu_01NyzJXV1PFoeNgQdJw3zptd`</summary>

```text
Web search results for query: ""From Chains to DAGs" github code repository reasoning DAG probing"

Links: [{"title":"[2601.17593] From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/abs/2601.17593"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/html/2601.17593"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260117593Z/abstract"},{"title":"DAG-Math: Graph-Guided Mathematical Reasoning in LLMs","url":"https://arxiv.org/html/2510.19842v1"},{"title":"From Commits to DAGs: How Git Uses a DAG to Track Your Code History - DEV Community","url":"https://dev.to/ganesh-kumar/from-commits-to-dags-how-git-uses-a-dag-to-track-your-code-history-1p1j"},{"title":"DAG-Math: Graph-Guided Mathematical Reasoning in LLMs Yuanhe Zhang*","url":"https://arxiv.org/pdf/2510.19842"},{"title":"dags · GitHub Topics · GitHub","url":"https://github.com/topics/dags"},{"title":"GitHub - john-bradshaw/synthesis-dags: Code for our paper \"Barking up the right tree: an approach to search over molecule synthesis DAGs\"","url":"https://github.com/john-bradshaw/synthesis-dags"},{"title":"GitHub - astronomer/ded-ultimate-guide-to-dags: Webinar repository for example DAGs for the Data Engineering Digest webinar: Apache Airflow®: The Ultimate Guide to DAG Writing","url":"https://github.com/astronomer/ded-ultimate-guide-to-dags"}]

Based on the search results, I found relevant information about the "From Chains to DAGs" paper. Here's what I discovered:

## From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs

The research introduces Reasoning DAG Probing, a framework for testing whether LLM hidden states linearly encode properties of an underlying reasoning DAG and where this structure emerges across layers.

### Key Contributions

While prior work often treats reasoning as a linear chain, many reasoning problems are more naturally modeled as directed acyclic graphs (DAGs), where intermediate conclusions branch, merge, and are reused.

The researchers associate each reasoning node with a textual realization and train lightweight probes to predict node depth, pairwise distance, and adjacency from hidden states. Using these probes, they analyze the emergence of DAG structure across layers, reconstruct approximate reasoning graphs, and evaluate controls that disrupt reasoning-relevant structure while preserving surface text.

### Research Methodology

The approach trains low-capacity probes on frozen hidden states to recover three graph-theoretic properties: (i) node depth, which captures each node's relative position in the reasoning hierarchy, (ii) pairwise node distance, which measures how far two intermediate states lie from each other in the dependency structure, and (iii) pairwise node adjacency, which indicates whether two nodes are directly connected by an edge in the reasoning graph.

The paper was published on arXiv in April 2026 (arXiv:2601.17593). However, the search results did not reveal a specific GitHub code repository URL for this project.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12582ae4-4db9-4b78-8c24-5b657c1ca4b9",
  "isSidechain": true,
  "promptId": "c803892c-5106-4584-8104-83ba36b7b3b2",
  "agentId": "a654e0ba71297ac88",
  "type": "user",
  "uuid": "a41b1a5e-215f-4273-a3f9-3eac56be2dce",
  "sourceToolAssistantUUID": "12582ae4-4db9-4b78-8c24-5b657c1ca4b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-19T10:00:00.605Z_

I now have comprehensive information. Here is my detailed report.

---

## Detailed Research Report: "From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs"

### Basic Metadata

- **Exact title**: "From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs"
- **Authors**: Tianjun Zhong, Linyang He, Nima Mesgarani (Columbia University)
- **arXiv ID**: 2601.17593
- **Dates**: Submitted January 24, 2026; revised April 5, 2026 (v2)
- **Venue**: Listed under cs.CL on arXiv. No confirmed conference venue found (appears to be a preprint as of this search; no ICLR/ACL acceptance was found).
- **Code repository**: None found publicly.

---

### Core Method: Reasoning DAG Probing

The framework has four main components:

**1. DAG Construction from Reasoning Problems**

The paper requires reasoning problems with *explicit proof structure*. For their primary dataset (ProofWriter), the proof is already formalized as a DAG. For GSM8K (math), they use GPT-5 mini to extract reasoning DAGs from worked solutions (an external, non-ground-truth step).

- **Nodes (V)**: Premises, intermediate conclusions, and the final answer. Each node is associated with a textual realization (the natural-language statement it represents).
- **Edges (E)**: Directed edges from premise nodes to conclusion nodes, representing rule applications or logical dependencies. Edges point from supporting facts toward derived conclusions.

Example: For ProofWriter, a theory with facts like "Fiona is cold" generates a DAG where nodes are intermediate conclusions like "Fiona is green" (derived via a rule cold->green), and edges connect each premise to its derived conclusion, culminating in the query answer as the sink node.

**2. Representation Extraction**

For each node v in a DAG:
1. Concatenate the full theory text T with the node's textual realization x_v
2. Tokenize with offset mappings to identify the x_v token span
3. For each layer l, extract hidden states for all tokens in span(v)
4. Mean-pool across the token span to get a single vector z_v^(l) in R^d

All model weights are frozen; only the lightweight probes are trained.

**3. Three Probing Targets**

All probes are low-rank linear maps (rank k=1, no bias), trained with AdamW:

- **Node Depth Probe**: Predicts a scalar depth = w^T z_v. Trained with a pairwise ranking loss (softplus). Depth is defined as the longest directed path from a node to the sink, normalized so the sink has maximal depth. Evaluated via Spearman correlation.

- **Pairwise Distance Probe**: Takes |z_u - z_v| as input, predicts graph distance via a linear map. Trained with MSE. Distance is defined as the longest directed path between two nodes (symmetrized). Evaluated via Spearman correlation.

- **Pairwise Adjacency Probe**: Score s_uv = w^T |z_u - z_v|, then sigmoid -> prediction in [0,1]. Trained with binary cross-entropy with positive-class weighting. Evaluated via average precision.

**4. Graph Reconstruction Algorithm**

This is the key part for your reviewer question -- how DAGs are reconstructed:

1. **Sink identification**: Pick the node with highest predicted depth.
2. **Candidate edge generation**: Consider all node pairs; orient edges from shallower to deeper (by predicted depth); associate each with predicted distance and adjacency scores.
3. **Edge addition (two-stage)**:
   - Stage A: For each non-sink node, add its single best outgoing candidate edge (highest adjacency probability, distance as tiebreaker).
   - Stage B: Add remaining candidates satisfying *both* thresholds: predicted distance <= tau_dist AND predicted adjacency >= tau_adj.
4. The result is acyclic by construction (edges only go from lower to higher predicted depth).
5. Thresholds tau_dist and tau_adj are tuned on a dev set to maximize edge F1.

---

### Key Results

| Metric | Peak Value (Qwen3-14B) | Layer Range |
|--------|------------------------|-------------|
| Depth Spearman | ~0.75 | Intermediate (layers 8-18) |
| Distance Spearman | ~0.65 | Intermediate |
| Adjacency Avg Precision | ~0.70 | Intermediate |
| Edge Reconstruction F1 | ~0.55-0.60 | Intermediate |

**Scaling**: Performance improves with model scale (1B -> 32B), with logarithmic gains saturating around 8B+. Training recipe (base vs. instruction-tuned vs. reasoning-optimized) has <5% effect compared to scale.

**Depth-dependent encoding**: Shallow nodes are best recovered in early layers; deep nodes in later layers. This creates a diagonal banding pattern -- the network progressively builds the DAG structure across its depth.

**Correctness correlation**: Correct generations have modestly higher probe scores than incorrect ones, but distributions overlap substantially. DAG recoverability is neither sufficient nor guaranteed for correct generation.

**Cross-model consistency**: All tested model families (Qwen3, DeepSeek-R1-Distill, Llama-3.2, K2-Think, Ministral) show the same qualitative patterns.

**Baselines**: The full method outperforms controls by 3-5x. Node-only (without full theory context), bag-of-words, and label-shuffled baselines all perform far worse, confirming the signal comes from contextualized representations, not surface text.

---

### Failure Modes and Limitations

1. **Moderate reconstruction F1 (~0.55-0.60)**: The DAG reconstruction is approximate, not exact. Recall consistently exceeds precision (many spurious edges).

2. **Requires explicit DAG annotations**: The framework needs ground-truth DAGs for training probes. ProofWriter provides these natively; for other domains like GSM8K, they had to use GPT-5 mini to generate DAGs, which introduces noise.

3. **Threshold sensitivity**: Reconstruction quality depends on tuning tau_dist and tau_adj on a development set.

4. **Late-layer degradation**: Performance mildly declines in final layers, possibly reflecting a shift toward generation-oriented objectives.

5. **Test-time applicability gap**: For arbitrary user queries without pre-existing DAG structure, the method requires either structured prompting, auxiliary supervision, or representation-level interventions.

6. **Limited annotation types**: Currently probes only depth, distance, and adjacency -- not edge semantics, rule types, or other richer structural properties.

---

### Could This Method Be Used as a Component to Convert Reasoning Chains to DAGs?

This is the critical question for your reviewer response. The answer is **partially yes, but with important caveats**:

**What it can do**:
- Given a model processing a reasoning problem, extract hidden-state representations for each reasoning step.
- Train probes to predict depth ordering, pairwise distances, and adjacency.
- Use the graph reconstruction algorithm (sink identification -> depth ordering -> two-stage edge addition) to produce an approximate DAG.
- The paper explicitly discusses potential downstream uses: structured decoding, auxiliary supervision, interventions, and interpretability.

**What it cannot do (without extension)**:
- It cannot work "out of the box" on arbitrary reasoning chains. It requires: (a) a way to segment reasoning chains into discrete nodes with textual realizations, and (b) ground-truth DAGs for training the probes (or transfer from a domain where ground-truth DAGs exist).
- The reconstructed DAGs have moderate fidelity (F1 ~0.55-0.60), so they would need to be treated as approximate dependency structures, not precise graphs.
- The method probes *internal* representations of a specific model -- it is not a text-level parser that extracts DAGs from chain-of-thought text. It requires access to model hidden states.

**For your reviewer response**, you could cite this paper to argue that:
1. There is evidence that LLMs internally represent reasoning as DAGs, not just chains.
2. A concrete algorithm exists (the two-stage reconstruction with depth-ordered edge addition) for recovering approximate DAGs from model internals.
3. The probing framework could be adapted as a component by training probes on a domain with known DAG structure, then applying them to extract DAGs from reasoning chains in your target domain.
4. However, you should acknowledge the moderate reconstruction fidelity and the requirement for probe training data.

You may also want to look at the related paper **DAG-Math** (arXiv 2510.19842, published at ICLR 2026) which takes a complementary approach: modeling chain-of-thought as a rule-based stochastic process over DAGs where nodes represent derivation states and edges encode rule applications. That paper works at the text level rather than the representation level and may be more directly applicable as a chain-to-DAG conversion method.

---

Sources:
- [From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs (arXiv abstract)](https://arxiv.org/abs/2601.17593)
- [From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs (HTML)](https://arxiv.org/html/2601.17593v2)
- [From Chains to DAGs on ADS](https://ui.adsabs.harvard.edu/abs/2026arXiv260117593Z/abstract)
- [DAG-Math: Graph-Guided Mathematical Reasoning in LLMs](https://arxiv.org/html/2510.19842v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a41b1a5e-215f-4273-a3f9-3eac56be2dce",
  "isSidechain": true,
  "agentId": "a654e0ba71297ac88",
  "requestId": "req_011CbBjNEqwmbwDsUu7XJy4W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb0f9cbd-ab76-459a-b916-5c01bc32b070",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FgfiZNxKeRKcBUmNGZME1x",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 936,
      "cache_read_input_tokens": 18612,
      "output_tokens": 2340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 936
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2340,
          "cache_read_input_tokens": 18612,
          "cache_creation_input_tokens": 936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 936,
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
