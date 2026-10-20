# Research conversation: You are researching the paper "Robust Reasoning Benchmark" by Golikov et al. (arXiv 2026), available at https://arxiv.or

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a56d5b8ff9d0d9bc6.jsonl`
- **Structured JSON:** [`65b78e6e880f2f10c419.json`](../../sessions/65/65b78e6e880f2f10c419.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

36 recorded events

### User

_source line 1 · 2026-05-29T07:27:53.290Z_

You are researching the paper "Robust Reasoning Benchmark" by Golikov et al. (arXiv 2026), available at https://arxiv.org/abs/2604.08571.

Your task:
1. Use WebFetch to read the paper's abstract and introduction from the arxiv page.
2. Search for any additional information, blog posts, or discussions about this paper.
3. Try to find details about the 13 deterministic perturbation types they apply to AIME problems.

For your final response, provide a detailed summary covering:
- What gap/problem did they identify and HOW?
- What was the key insight others missed?
- How did they formulate the problem differently from GSM-Symbolic and GSM-Plus?
- What are the 13 perturbation types (or as many as you can find)?
- What failure modes did they identify (cognitive thrashing, tokenization breakdown)?
- What existing technique did they adapt/combine/simplify?
- What are the main limitations?
- Key quantitative results (up to 54% accuracy drops, which models are resilient vs vulnerable)
- How do they differentiate between frontier models and open-weights models?

Be thorough and specific — include numbers, method details, and concrete findings. This is a very recent 2026 paper so search carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e2027b0c-9c37-4d02-abda-83dbebeded5e",
  "agentId": "a56d5b8ff9d0d9bc6",
  "type": "user",
  "uuid": "a01ce3aa-8220-4ff0-9c30-8529bb3f05e6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-29T07:27:53.293Z_

```json
{
  "parentUuid": "a01ce3aa-8220-4ff0-9c30-8529bb3f05e6",
  "isSidechain": true,
  "agentId": "a56d5b8ff9d0d9bc6",
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
  "uuid": "ed9e2f49-e77e-45c1-b1a0-95733f0444f4",
  "timestamp": "2026-05-29T07:27:53.293Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-29T07:27:53.294Z_

```json
{
  "parentUuid": "ed9e2f49-e77e-45c1-b1a0-95733f0444f4",
  "isSidechain": true,
  "agentId": "a56d5b8ff9d0d9bc6",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "70b83182-3df4-4860-ae6c-dbaa62b8ac1f",
  "timestamp": "2026-05-29T07:27:53.294Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-29T07:27:56.373Z_



I'll research this paper thoroughly. Let me start by fetching the arxiv page and searching for additional information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70b83182-3df4-4860-ae6c-dbaa62b8ac1f",
  "isSidechain": true,
  "agentId": "a56d5b8ff9d0d9bc6",
  "requestId": "req_011CbWTvcwarC4Sa2H1WWLf7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c566344-cd89-4681-ae64-71e2e10c3036",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HzekYEktPrg4b1wqMgmmBG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1635,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1635,
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

_source line 5 · 2026-05-29T07:27:57.019Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RvA2RMUoqPK4BUw87FAgKr`</summary>

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
  "parentUuid": "8c566344-cd89-4681-ae64-71e2e10c3036",
  "isSidechain": true,
  "agentId": "a56d5b8ff9d0d9bc6",
  "requestId": "req_011CbWTvcwarC4Sa2H1WWLf7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1200b539-2138-423a-9cdb-3a09016628d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HzekYEktPrg4b1wqMgmmBG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1635,
      "cache_read_input_tokens": 7413,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1635
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 104,
          "cache_read_input_tokens": 7413,
          "cache_creation_input_tokens": 1635,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1635,
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

_source line 6 · 2026-05-29T07:27:57.023Z_

<details><summary>↩ Tool result · `toolu_01RvA2RMUoqPK4BUw87FAgKr`</summary>

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
  "parentUuid": "1200b539-2138-423a-9cdb-3a09016628d6",
  "isSidechain": true,
  "promptId": "e2027b0c-9c37-4d02-abda-83dbebeded5e",
  "agentId": "a56d5b8ff9d0d9bc6",
  "type": "user",
  "uuid": "f2283896-0dc2-4195-8497-cb88f510e48c",
  "sourceToolAssistantUUID": "1200b539-2138-423a-9cdb-3a09016628d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-29T07:27:59.709Z_



Now let me fetch the arxiv page and search for discussions about this paper in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2283896-0dc2-4195-8497-cb88f510e48c",
  "isSidechain": true,
  "agentId": "a56d5b8ff9d0d9bc6",
  "requestId": "req_011CbWTvu9u5h8ZyaPkvUAea",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be15f283-4062-482d-9987-e721991586b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWVyFynt9MP3BAapEGXJ3X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9048,
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

_source line 8 · 2026-05-29T07:28:01.588Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HMdBoRG6TZt2t8m5axxxKF`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.08571",
  "prompt": "Extract the full abstract, all author names, the title, and any other metadata from this arxiv paper page. Include every detail available on the abstract page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be15f283-4062-482d-9987-e721991586b3",
  "isSidechain": true,
  "agentId": "a56d5b8ff9d0d9bc6",
  "requestId": "req_011CbWTvu9u5h8ZyaPkvUAea",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16113cc9-6f51-4456-9286-1edc31b80393",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWVyFynt9MP3BAapEGXJ3X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9048,
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

_source line 9 · 2026-05-29T07:28:02.586Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01119XpmCKYoXF8hsFwLieH9`</summary>

```json
{
  "query": "Robust Reasoning Benchmark Golikov arXiv 2604.08571 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16113cc9-6f51-4456-9286-1edc31b80393",
  "isSidechain": true,
  "agentId": "a56d5b8ff9d0d9bc6",
  "requestId": "req_011CbWTvu9u5h8ZyaPkvUAea",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1370a0c-18bb-4035-b1a5-2dbbffcecb2e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWVyFynt9MP3BAapEGXJ3X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9048,
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

_source line 10 · 2026-05-29T07:28:03.140Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017bqrYkPESyQuXbj8TZTUji`</summary>

```json
{
  "query": "\"Robust Reasoning Benchmark\" AIME perturbation types 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1370a0c-18bb-4035-b1a5-2dbbffcecb2e",
  "isSidechain": true,
  "agentId": "a56d5b8ff9d0d9bc6",
  "requestId": "req_011CbWTvu9u5h8ZyaPkvUAea",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e36069a9-d8b1-4de0-8727-3ee452b2245b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWVyFynt9MP3BAapEGXJ3X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9048,
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

### Tool result

_source line 11 · 2026-05-29T07:28:07.230Z_

<details><summary>↩ Tool result · `toolu_01HMdBoRG6TZt2t8m5axxxKF`</summary>

```text
# Robust Reasoning Benchmark - Paper Metadata

**Title:** Robust Reasoning Benchmark

**Authors:**
- Pavel Golikov
- Evgenii Opryshko
- Gennady Pekhimenko
- Mark C. Jeffrey

**arXiv Identifier:** 2604.08571

**Submission History:**
- Initial submission: March 26, 2026
- Latest revision (v2): May 20, 2026

**Subject Classification:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)

**DOI:** https://doi.org/10.48550/arXiv.2604.08571

**Abstract Summary:**

The paper introduces a benchmark pipeline applying "13 deterministic textual perturbations applied to AIME 2024 and AIME 2025" to evaluate eight LLM models. Key findings include frontier models showing resilience except Claude, which "categorically refuses many transformed prompts," while open-weights reasoning models experience accuracy drops up to 54%. The authors identify "Intra-Query Attention Dilution," where solving sequential math problems in a single context causes performance decay on subsequent problems across models from 7B to 120B parameters, suggesting intermediate reasoning pollutes attention mechanisms.

**Available Formats:** PDF, HTML (experimental), TeX Source
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16113cc9-6f51-4456-9286-1edc31b80393",
  "isSidechain": true,
  "promptId": "e2027b0c-9c37-4d02-abda-83dbebeded5e",
  "agentId": "a56d5b8ff9d0d9bc6",
  "type": "user",
  "uuid": "f3f72622-716e-4985-9766-7d879caf3145",
  "sourceToolAssistantUUID": "16113cc9-6f51-4456-9286-1edc31b80393",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-29T07:28:09.680Z_

<details><summary>↩ Tool result · `toolu_017bqrYkPESyQuXbj8TZTUji`</summary>

```text
Web search results for query: ""Robust Reasoning Benchmark" AIME perturbation types 2026"

Links: [{"title":"Robust Reasoning Benchmark","url":"https://arxiv.org/html/2604.08571v2"},{"title":"[2604.08571] Robust Reasoning Benchmark","url":"https://arxiv.org/abs/2604.08571"},{"title":"AIME 2025 Benchmark: An Analysis of AI Math Reasoning | IntuitionLabs","url":"https://intuitionlabs.ai/articles/aime-2025-ai-benchmark-explained"},{"title":"AIME 2026 Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/aime-2026"},{"title":"Towards Robust Mathematical Reasoning","url":"https://arxiv.org/html/2511.01846v1"},{"title":"AIME Benchmarks: Math & AI Evaluation","url":"https://www.emergentmind.com/topics/aime-benchmarks"},{"title":"Fragile Thoughts: How Large Language Models Handle Chain-of-Thought Perturbations","url":"https://arxiv.org/pdf/2603.03332"},{"title":"Benchmarking Reasoning Robustness in Large Language Models","url":"https://arxiv.org/pdf/2503.04550"}]

Based on the search results, here's what I found about the Robust Reasoning Benchmark and its AIME perturbation types:

The Robust Reasoning Benchmark (RRB) is a pipeline of 13 deterministic textual perturbations applied to AIME 2024 and AIME 2025.

The RRB augments AIME with 13 deterministic textual transformations that perturb structure without altering meaning or difficulty.

However, the search results do not provide a detailed breakdown of what these 13 specific perturbation types are. The papers mention that the benchmark evaluates models on these structural perturbations, but the specific names and descriptions of each perturbation type are not included in the available excerpts.

The research does identify some related failure modes that models experience under these perturbations, such as "cognitive thrashing, tokenization breakdown, and reasoning collapse" in open-weights models, as well as "attention dilution caused by the model's own chain-of-thought" and "Intra-Query Attention Dilution."

To get the complete list of the 13 specific perturbation types, you would need to access the full paper on arXiv (arxiv.org/abs/2604.08571).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e36069a9-d8b1-4de0-8727-3ee452b2245b",
  "isSidechain": true,
  "promptId": "e2027b0c-9c37-4d02-abda-83dbebeded5e",
  "agentId": "a56d5b8ff9d0d9bc6",
  "type": "user",
  "uuid": "0996b55b-8e81-4921-9372-20bb28326dc8",
  "sourceToolAssistantUUID": "e36069a9-d8b1-4de0-8727-3ee452b2245b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-29T07:28:12.197Z_

<details><summary>↩ Tool result · `toolu_01119XpmCKYoXF8hsFwLieH9`</summary>

```text
Web search results for query: "Robust Reasoning Benchmark Golikov arXiv 2604.08571 2026"

Links: [{"title":"[2604.08571] Robust Reasoning Benchmark","url":"https://arxiv.org/abs/2604.08571"},{"title":"Robust Reasoning Benchmark","url":"https://arxiv.org/html/2604.08571"},{"title":"Robust Reasoning Benchmark – Paper Detail · SwiftScholar - Review with AI","url":"https://www.swiftscholar.net/paper/69dd894984947a5132b62b34"},{"title":"Benchmarking Reasoning Robustness in Large Language Models","url":"https://arxiv.org/pdf/2503.04550"},{"title":"Functional Benchmarks for Robust Evaluation of Reasoning Performance,   and the Reasoning Gap","url":"https://arxiv.org/pdf/2402.19450"},{"title":"[2402.19450] Functional Benchmarks for Robust Evaluation of Reasoning Performance, and the Reasoning Gap","url":"https://arxiv.org/abs/2402.19450"},{"title":"[2503.04550] Benchmarking Reasoning Robustness in Large Language Models","url":"https://arxiv.org/abs/2503.04550"}]

Based on the search results, here's information about the paper:

## Robust Reasoning Benchmark (arXiv:2604.08571)

The paper was authored by Pavel Golikov, Evgenii Opryshko, Gennady Pekhimenko, and Mark C. Jeffrey, and they are affiliated with the University of Toronto and the Vector Institute.

**Overview:**
The paper introduces the Robust Reasoning Benchmark (RRB), a pipeline of 13 deterministic textual perturbations applied to AIME 2024 and AIME 2025.

**Key Findings:**
Evaluating 8 state-of-the-art models, the researchers found that frontier models are largely resilient, with the notable exception of Claude, which categorically refuses many transformed prompts. Additionally, open-weights reasoning models exhibit a range of failure modes under structural noise (cognitive thrashing, tokenization breakdown, and reasoning collapse), with up to 54% average accuracy drops across perturbations and up to 100% on some.

The paper further studies one failure mode in isolation: attention dilution caused by the model's own chain-of-thought, by tasking models with solving multiple independent mathematical problems sequentially within a single context window.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1370a0c-18bb-4035-b1a5-2dbbffcecb2e",
  "isSidechain": true,
  "promptId": "e2027b0c-9c37-4d02-abda-83dbebeded5e",
  "agentId": "a56d5b8ff9d0d9bc6",
  "type": "user",
  "uuid": "163a24fe-163d-48ac-a1aa-e87987a18adb",
  "sourceToolAssistantUUID": "b1370a0c-18bb-4035-b1a5-2dbbffcecb2e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-29T07:28:16.580Z_

Good, I have the basic overview. Now let me fetch the full HTML version of the paper to get the detailed content, including the 13 perturbation types, methodology, and results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "163a24fe-163d-48ac-a1aa-e87987a18adb",
  "isSidechain": true,
  "agentId": "a56d5b8ff9d0d9bc6",
  "requestId": "req_011CbWTx1nYBXCeuEUEP6xde",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6928c695-1986-4a58-8b8a-d5f07c9ed807",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hq7GMPhJMhvJ7Byhdd4u98",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 660,
      "cache_creation_input_tokens": 1219,
      "cache_read_input_tokens": 10174,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1219,
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

_source line 15 · 2026-05-29T07:28:19.992Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TC2t14o5zxvwfR79Xc48Z9`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.08571v2",
  "prompt": "Extract ALL details about the 13 deterministic perturbation types applied to AIME problems. List each perturbation type by name and description. Also extract details about the methodology, how the benchmark differs from GSM-Symbolic and GSM-Plus, the failure modes (cognitive thrashing, tokenization breakdown, reasoning collapse), the Intra-Query Attention Dilution finding, quantitative results including accuracy drops for specific models, and any limitations discussed. Be as comprehensive as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6928c695-1986-4a58-8b8a-d5f07c9ed807",
  "isSidechain": true,
  "agentId": "a56d5b8ff9d0d9bc6",
  "requestId": "req_011CbWTx1nYBXCeuEUEP6xde",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a4268a5-9b60-4dfd-b503-4267def3258d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hq7GMPhJMhvJ7Byhdd4u98",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 660,
      "cache_creation_input_tokens": 1219,
      "cache_read_input_tokens": 10174,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1219,
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

_source line 16 · 2026-05-29T07:28:21.934Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01W8CjgJYJLMp616k7dKUWT2`</summary>

```json
{
  "url": "https://www.swiftscholar.net/paper/69dd894984947a5132b62b34",
  "prompt": "Extract all details about the Robust Reasoning Benchmark paper, including methodology, perturbation types, results, and any discussion or commentary about the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a4268a5-9b60-4dfd-b503-4267def3258d",
  "isSidechain": true,
  "agentId": "a56d5b8ff9d0d9bc6",
  "requestId": "req_011CbWTx1nYBXCeuEUEP6xde",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bacd7884-551e-496e-8047-7c6dbd897c10",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hq7GMPhJMhvJ7Byhdd4u98",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 660,
      "cache_creation_input_tokens": 1219,
      "cache_read_input_tokens": 10174,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1219,
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

_source line 17 · 2026-05-29T07:28:22.538Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KsHra5TEt134BrS4DbU2uG`</summary>

```json
{
  "query": "Robust Reasoning Benchmark \"cognitive thrashing\" \"tokenization breakdown\" perturbation AIME LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bacd7884-551e-496e-8047-7c6dbd897c10",
  "isSidechain": true,
  "agentId": "a56d5b8ff9d0d9bc6",
  "requestId": "req_011CbWTx1nYBXCeuEUEP6xde",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "040d048b-f83b-43e6-a16e-cf2a5acacc03",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hq7GMPhJMhvJ7Byhdd4u98",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 660,
      "cache_creation_input_tokens": 1219,
      "cache_read_input_tokens": 10174,
      "output_tokens": 394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1219
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 660,
          "output_tokens": 394,
          "cache_read_input_tokens": 10174,
          "cache_creation_input_tokens": 1219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1219,
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

_source line 18 · 2026-05-29T07:28:29.821Z_

<details><summary>↩ Tool result · `toolu_01KsHra5TEt134BrS4DbU2uG`</summary>

```text
Web search results for query: "Robust Reasoning Benchmark "cognitive thrashing" "tokenization breakdown" perturbation AIME LLM"

Links: [{"title":"[2604.08571] Robust Reasoning Benchmark","url":"https://arxiv.org/abs/2604.08571"},{"title":"Robust Reasoning Benchmark","url":"https://arxiv.org/html/2604.08571v2"},{"title":"Eliciting Reasoning in Language Models with Cognitive Tools Brown Ebouky","url":"https://arxiv.org/pdf/2506.12115"},{"title":"CodeCrash: Exposing LLM Fragility to Misleading Natural Language in Code Reasoning","url":"https://arxiv.org/pdf/2504.14119"},{"title":"Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens","url":"https://arxiv.org/pdf/2602.13517"},{"title":"ReasonBENCH: Benchmarking the (In)Stability of LLM Reasoning","url":"https://arxiv.org/html/2512.07795v1"},{"title":"Benchmarking Reasoning Robustness in Large Language Models","url":"https://arxiv.org/pdf/2503.04550"}]

Based on the search results, I found comprehensive information about the Robust Reasoning Benchmark:

## Overview

The Robust Reasoning Benchmark (RRB) is a pipeline of 13 deterministic textual perturbations applied to AIME 2024 and AIME 2025.

## Key Findings

Frontier models are largely resilient, with the notable exception of Claude, which categorically refuses many transformed prompts. However, open-weights reasoning models exhibit a range of failure modes under structural noise (cognitive thrashing, tokenization breakdown, and reasoning collapse), with up to 54% average accuracy drops across perturbations and up to 100% on some.

## Methodology

The researchers do not alter the mathematical values, the logic, or the final answer, but instead apply reversible algorithmic perturbations such as syntactic string reversals, visual 2D grid encodings (e.g., Rail Fence, Horizontal Snake), and semantic wrappers. The transformations are trivial for humans to decode but structurally hostile to LLM tokenization and attention.

## Additional Investigation

The researchers further study one of these failure modes in isolation: attention dilution caused by the model's own chain-of-thought.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "040d048b-f83b-43e6-a16e-cf2a5acacc03",
  "isSidechain": true,
  "promptId": "e2027b0c-9c37-4d02-abda-83dbebeded5e",
  "agentId": "a56d5b8ff9d0d9bc6",
  "type": "user",
  "uuid": "8bab05a2-3960-4379-b6f8-c31a3f7c603a",
  "sourceToolAssistantUUID": "040d048b-f83b-43e6-a16e-cf2a5acacc03",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-29T07:28:32.662Z_

<details><summary>↩ Tool result · `toolu_01W8CjgJYJLMp616k7dKUWT2`</summary>

```text
# Robust Reasoning Benchmark Paper Summary

## Paper Identification
- **Title:** Robust Reasoning Benchmark (RRB)
- **Authors:** Pavel Golikov, Evgenii Opryshko, Gennady Pekhimenko, Mark C. Jeffrey
- **Affiliation:** University of Toronto and Vector Institute
- **Status:** Preprint (arXiv:2604.08571)
- **Published:** March 26, 2026

## Core Research Question
The paper investigates whether large language models genuinely perform mathematical reasoning or merely execute surface-level pattern matching. It tests robustness through structural perturbations that preserve mathematical meaning while altering text presentation.

## Methodology Overview

### The 14 Perturbation Techniques
The authors developed a taxonomy across four categories:

**Semantic/Lexical:** "Not not" insertions, antonym substitution, arbitrary wrappers around values

**Contextual Overload:** Interleaved dual problems (line/word/symbol level), synthetic problem saturation filling 75% of context

**Syntactic Distortion:** Sentence reversal, word reversal, character reversal within words

**Visual/Spatial Encoding:** Rail Fence Cipher, rectangle perimeter mapping, vertical snake, horizontal snake patterns

### Dataset and Models
- **Dataset:** AIME 2024 mathematics problems
- **Proprietary Models:** GPT-5.4, Gemini 3.1 Pro, Claude Opus 4.6
- **Open-Weight Models:** Qwen3-30B, Nemotron-7B/32B, DeepSeek-R1-Distill-70B, gpt-oss-120b

## Key Findings

### The Robustness Gap
"Frontier" models demonstrated resilience with accuracy drops of 7-10%, while open-weight models suffered catastrophic failures reaching 55% average accuracy loss. This disparity suggests different architectural approaches to abstraction.

### Intra-Query Attention Dilution
A novel phenomenon where solving multiple problems sequentially within one context degrades performance on subsequent problems. The authors argue that intermediate reasoning steps create "pollution" in standard dense attention mechanisms, lacking working memory isolation.

### Failure Pattern Analysis
Open-weight models exhibited universal failure on character-level and spatial reasoning tasks (0% accuracy on some perturbations), suggesting overfit to standard tokenization patterns rather than abstract reasoning capability.

### Cognitive Thrashing
Models like Nemotron-7B generated 27,000 tokens at 0% accuracy on certain tasks, indicating broken confidence mechanisms that perpetuate unproductive processing loops rather than recognizing confusion.

## Architectural Implications

The authors conclude that future models require "explicit contextual resets" between reasoning steps. Standard transformer attention proves insufficient for maintaining logical coherence across extended reasoning chains without prior steps degrading subsequent performance.

## Critical Assessment

The paper provides compelling evidence that claimed "reasoning" capabilities often mask tokenization dependency. The finding that frontier APIs outperform open models suggests proprietary architectural advantages remain undisclosed, while the Claude refusal issue illustrates safety-capability tradeoffs in alignment procedures.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bacd7884-551e-496e-8047-7c6dbd897c10",
  "isSidechain": true,
  "promptId": "e2027b0c-9c37-4d02-abda-83dbebeded5e",
  "agentId": "a56d5b8ff9d0d9bc6",
  "type": "user",
  "uuid": "5c32b11c-dff3-4896-8a8e-9a4b5adca942",
  "sourceToolAssistantUUID": "bacd7884-551e-496e-8047-7c6dbd897c10",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-29T07:28:47.988Z_

<details><summary>↩ Tool result · `toolu_01TC2t14o5zxvwfR79Xc48Z9`</summary>

```text
# Robust Reasoning Benchmark: Comprehensive Extraction

## The 13 Deterministic Perturbation Types

### Category 1: Semantic and Lexical Substitutions

**Not Not**: Double negations inserted before numerical values and adjectives (e.g., "not not least"). Since double negation logically equals the original term, robust reasoning should discard these additions without altering mathematical logic.

**Opposites**: Semantic terms remapped to antonyms within queries (e.g., "short" means "long"). Specific substitutions are defined inside the prompt, requiring simple key-value lookup for decoding.

**Wrappers**: Terms encapsulated in arbitrary syntactic wrappers serving as identity functions (e.g., "3(p)" replaces "p"). Mappings are explicitly provided within the query.

### Category 2: Contextual Overload (Interleaved Contexts)

**Line-level Interleaving**: Two distinct math problems split into 60-character segments, alternated with problem tags, forcing models to extract only the designated problem.

**Word-level Interleaving**: Words from two problems strictly alternated one-by-one, with shorter problems repeated to match length.

**Symbol-level Interleaving**: Individual characters from two problems alternately interwoven, maintaining strict character-by-character alternation.

### Category 3: Syntactic Distortions

**Sentence Reversal**: Order of sentences (symbol sequences separated by periods) reversed in the entire query.

**Word Reversal**: Order of words (sequences separated by spaces) reversed throughout the input.

**Symbol Reversal**: Each word's characters reversed individually while maintaining word positions.

### Category 4: Visual and Spatial Encoding

**Rail Fence Cipher**: Symbols placed in zigzag patterns across multiple rows with dots filling gaps, requiring diagonal reading to reconstruct original text.

**Rectangle Perimeter**: Query mapped onto a rectangle's perimeter, flowing clockwise from top-left, with dots filling the center.

**Snake Vertical**: Text written into grids using vertical zigzag patterns—down the first column, up the second, down the third, continuing this alternation.

**Snake Horizontal**: Horizontal boustrophedon pattern—right across row one, left across row two, right across row three, alternating directions.

---

## Methodology Details

### Dataset and Preprocessing

The benchmark applies transformations to AIME 2024 and AIME 2025 problems. Critical preprocessing steps include:

- **LaTeX Comment Removal**: Eliminates inline comments that could create artifacts
- **Newline Flattening**: Replaces newlines with semicolons and spaces to prevent spatial layout anomalies
- **Escape Sequence Neutralization**: Inserts spaces between backslashes and specific characters (n, t, b, r, a, f) to prevent accidental control character formation during reversals

### Design Principles

Transformations adhere to strict guidelines:

1. **Information-Theoretic Invariance**: Cannot add mathematical constraints, remove premises, or introduce ambiguities changing difficulty
2. **Algorithmic Reversibility**: Must be deterministic and programmatically invertible (verified via Python scripts)
3. **Cognitive Tractability**: Simple enough for humans with pen and paper to decode
4. **Explicit Decoding Protocol**: Exact transformation rules provided in plain English; models execute two-stage trajectories: first decode, then solve
5. **Grid Preservation**: Character spacing strictly maintained using dots or perfect padding

---

## Key Differentiators from Prior Work

The Robust Reasoning Benchmark distinguishes itself from **GSM-Symbolic** and **GSM-Plus** through several innovations:

**Unlike GSM-Symbolic** (which alters numeric values): RRB preserves exact mathematical values and difficulty. The research notes that "we do not alter the mathematical values, the logic, or the final answer," isolating pure structural fragility without confounding reasoning failures with arithmetic failures.

**Unlike GSM-Plus** (which adds irrelevant context): RRB applies reversible transformations that remain mathematically and logically equivalent. Rather than introducing new complexity, these transformations challenge tokenization and attention mechanisms while maintaining problem integrity.

**Unique aspects**: The benchmark uses deterministic, domain-agnostic algorithmic transformations rather than LLM-generated perturbations, eliminating non-deterministic noise and validity errors.

---

## Identified Failure Modes

### 1. Cognitive Thrashing

Modern open-weights reasoning models (Qwen3, Nemotron) enter unproductive loops rather than failing cleanly when encountering unrecognizable structural patterns. For example, Nemotron-7B generates approximately 27,000 tokens on Rectangle Perimeter tasks while achieving 0% accuracy. The paper observes that "the stopping criteria and logical progression heuristics are highly brittle."

### 2. Tokenization Breakdown

Transformations breaking words into isolated characters—such as Symbol Reversal and Rail Fence Cipher—severely disrupt Byte-Pair Encoding (BPE) boundaries. Models cannot map isolated character tokens back into coherent internal causal graphs, resulting in near-zero accuracy on these tasks.

### 3. Reasoning Collapse

Complete accuracy degradation on specific transformation types. Qwen3 drops from strong baseline performance to approximately 1% on Snake (Vertical) tasks, suggesting that "left-to-right, 1D pre-training biases" fundamentally constrain spatial reasoning capabilities.

---

## Intra-Query Attention Dilution: Core Finding

### Definition and Protocol

When models solve multiple independent mathematical problems sequentially within a single context window, accuracy on subsequent problems degrades. The sequential cognitive overload protocol presents 2-4 completely unrelated AIME problems in one prompt, measuring accuracy only on the final problem.

### Mechanistic Evidence

Attention analysis (Equations 1-2 in the paper) partitions token sequences into three regions: Instruction/Sink (system prompt), Distractor (irrelevant prior problems), and Target (final problem). The research finds that "middle and late layers consistently allocate 10% to 16.5% of attention probability mass to irrelevant distractor regions." Additionally, approximately 32.9% of attention in deeper layers attaches to initial system prompts, demonstrating classic "attention sink" behavior.

### Scale Invariance

The degradation affects "open-weights models ranging from 7B to 120B parameters," suggesting this represents a fundamental architectural limitation rather than a scale-dependent phenomenon.

---

## Quantitative Results

### Model Performance Comparison

**Frontier Models (Closed-Source)**:
- GPT-5.4: 3% average accuracy drop across perturbations
- Gemini 3.1 Pro: 8% average accuracy drop
- Claude 4.6 Opus: 52% average accuracy drop (primarily due to refusals, not reasoning failures)

**Open-Weights Models**:
- Nemotron-7B: 53% average accuracy drop
- Qwen3-30B-A3B-Thinking: 47% average accuracy drop
- DeepSeek-R1-Distill-70B: Substantial degradation (specific percentages not provided)
- Up to 100% accuracy drops on individual transformation types (e.g., symbol-level interleaving)

### Transformation-Specific Performance

On Snake (Horizontal): Gemini scores 99% while Qwen3 achieves 16%. On Snake (Vertical): Gemini drops to 65%, and Qwen3 to approximately 1%, demonstrating that spatial orientation severely impacts performance despite identical underlying text.

### Sequential Cognitive Overload Results

As context windows accumulate multiple problems, accuracy on final problems consistently declines across all open-weights models tested, with the exact degradation rate varying by model architecture and parameter count.

---

## Noted Limitations

The research acknowledges several constraints:

1. **Domain Specificity**: "Our evaluation primarily focuses on the domain of competitive mathematics. The extent to which these findings generalize to other high-stakes reasoning tasks (e.g., legal, medical, coding) remains to be explored in future work."

2. **Optimal Task Granularity**: An unresolved question remains regarding the ideal decomposition size for sub-tasks. The paper discusses a theoretical "atomic unit" of reasoning—"the maximum amount of computation a model can perform in a single context state before structural noise substantially degrades its algorithmic logic."

3. **Generalization Unknown**: Whether findings extend to non-numeric reasoning tasks and how maximum safe "cognitive load" scales with parameter count remain open questions.

4. **Proprietary Model Testing**: Due to computational costs, proprietary models were evaluated on baseline and only 4 sequential problems, less comprehensively than open-weights variants.

---

## Supporting Evidence and Implications

The paper strengthens its findings by noting that proprietary agentic frameworks (including Google's AntiGravity) appear to already implement explicit contextual resets and task boundary tools—suggesting industry awareness of these phenomena. The authors argue that future architectures require "explicit contextual resets within the model's own Chain-of-Thought" to achieve reliable reasoning, whether through native implementations or sub-agent delegation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a4268a5-9b60-4dfd-b503-4267def3258d",
  "isSidechain": true,
  "promptId": "e2027b0c-9c37-4d02-abda-83dbebeded5e",
  "agentId": "a56d5b8ff9d0d9bc6",
  "type": "user",
  "uuid": "7bb418ae-7687-4d0f-a366-df9d15aedc58",
  "sourceToolAssistantUUID": "8a4268a5-9b60-4dfd-b503-4267def3258d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-29T07:28:50.938Z_

Let me search for more details about how they differentiate between frontier and open-weights models, and any additional discussions or blog posts about this paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bb418ae-7687-4d0f-a366-df9d15aedc58",
  "isSidechain": true,
  "agentId": "a56d5b8ff9d0d9bc6",
  "requestId": "req_011CbWTzeoozffx7ttYNW48s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b3d3375-d4f7-4eb5-bf69-d0f9e35a2f75",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5FnUDvnTTv4E1iAEQ89cP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1366,
      "cache_creation_input_tokens": 3192,
      "cache_read_input_tokens": 11393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3192,
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

_source line 22 · 2026-05-29T07:28:51.424Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VEYhNuEBnTviLgiA67suRv`</summary>

```json
{
  "query": "Robust Reasoning Benchmark \"Intra-Query Attention Dilution\" open-weights frontier models Claude refusal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b3d3375-d4f7-4eb5-bf69-d0f9e35a2f75",
  "isSidechain": true,
  "agentId": "a56d5b8ff9d0d9bc6",
  "requestId": "req_011CbWTzeoozffx7ttYNW48s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9faa9504-9a8e-40a4-bf25-60bbefef7c96",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5FnUDvnTTv4E1iAEQ89cP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1366,
      "cache_creation_input_tokens": 3192,
      "cache_read_input_tokens": 11393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3192,
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

_source line 23 · 2026-05-29T07:28:52.000Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SRX9fvh6SRjAwei2NN3HGK`</summary>

```json
{
  "query": "arxiv 2604.08571 \"Robust Reasoning Benchmark\" blog discussion review commentary 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9faa9504-9a8e-40a4-bf25-60bbefef7c96",
  "isSidechain": true,
  "agentId": "a56d5b8ff9d0d9bc6",
  "requestId": "req_011CbWTzeoozffx7ttYNW48s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a5e9c22-782d-4f31-89ac-ee47ab09a542",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5FnUDvnTTv4E1iAEQ89cP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1366,
      "cache_creation_input_tokens": 3192,
      "cache_read_input_tokens": 11393,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3192
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1366,
          "output_tokens": 166,
          "cache_read_input_tokens": 11393,
          "cache_creation_input_tokens": 3192,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3192,
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

_source line 24 · 2026-05-29T07:28:59.074Z_

<details><summary>↩ Tool result · `toolu_01VEYhNuEBnTviLgiA67suRv`</summary>

```text
Web search results for query: "Robust Reasoning Benchmark "Intra-Query Attention Dilution" open-weights frontier models Claude refusal"

Links: [{"title":"Robust Reasoning Benchmark","url":"https://arxiv.org/html/2604.08571v2"},{"title":"[2604.08571] Robust Reasoning Benchmark","url":"https://arxiv.org/abs/2604.08571"},{"title":"Robust Reasoning Benchmark – Paper Detail · SwiftScholar - Review with AI","url":"https://www.swiftscholar.net/paper/69dd894984947a5132b62b34"},{"title":"The illusion of reasoning: step-level evaluation reveals decorative chain-of-thought in frontier language models","url":"https://arxiv.org/pdf/2603.22816"},{"title":"Claude Opus 4.7 vs Qwen 3.6: Closed Frontier Meets Open-Weight Reasoning","url":"https://www.getmaxim.ai/articles/claude-opus-4-7-vs-qwen-3-6-closed-frontier-meets-open-weight-reasoning/"},{"title":"Functional Benchmarks for Robust Evaluation of Reasoning Performance,   and the Reasoning Gap","url":"https://arxiv.org/pdf/2402.19450"},{"title":"Benchmarking Reasoning Robustness in Large Language Models","url":"https://arxiv.org/pdf/2503.04550"},{"title":"Responsible Agentic Reasoning and AI Agents: A Critical Survey","url":"https://www.techrxiv.org/users/574774/articles/1329333/master/file/data/Responsible_reasoning_survey%20(5)/Responsible_reasoning_survey%20(5).pdf"}]

Based on the search results, I found relevant information about the Robust Reasoning Benchmark and the topics you queried:

## Robust Reasoning Benchmark Overview

The Robust Reasoning Benchmark (RRB) is a pipeline of 13 deterministic textual perturbations applied to AIME 2024 and AIME 2025.

## Key Findings

**Frontier Models vs. Open-Weights:**
Frontier models are largely resilient, with the notable exception of Claude, which categorically refuses many transformed prompts. Open-weights reasoning models exhibit a range of failure modes under structural noise (cognitive thrashing, tokenization breakdown, and reasoning collapse), with up to 54% average accuracy drops across perturbations and up to 100% on some.

**Intra-Query Attention Dilution:**
One of the failure modes studied in isolation is attention dilution caused by the model's own chain-of-thought. The paper introduces a test for Intra-Query Attention Dilution by forcing models to solve multiple unperturbed problems sequentially in a single context window. Results indicate that open-weight models (7B to 120B parameters) and Claude Opus 4.6 suffer accuracy decay on subsequent problems.

**Mechanism:**
Intermediate reasoning steps pollute standard dense attention mechanisms and future architectures need explicit contextual resets within the Chain-of-Thought to ensure reliable reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9faa9504-9a8e-40a4-bf25-60bbefef7c96",
  "isSidechain": true,
  "promptId": "e2027b0c-9c37-4d02-abda-83dbebeded5e",
  "agentId": "a56d5b8ff9d0d9bc6",
  "type": "user",
  "uuid": "5d004c39-5dfb-4762-af9d-e5b10bff12e9",
  "sourceToolAssistantUUID": "9faa9504-9a8e-40a4-bf25-60bbefef7c96",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-29T07:29:01.913Z_

<details><summary>↩ Tool result · `toolu_01SRX9fvh6SRjAwei2NN3HGK`</summary>

```text
Web search results for query: "arxiv 2604.08571 "Robust Reasoning Benchmark" blog discussion review commentary 2026"

Links: [{"title":"Robust Reasoning Benchmark","url":"https://arxiv.org/html/2604.08571"},{"title":"Robust Reasoning Benchmark – Paper Detail · SwiftScholar - Review with AI","url":"https://www.swiftscholar.net/paper/69dd894984947a5132b62b34"},{"title":"[2604.08571] Robust Reasoning Benchmark","url":"https://arxiv.org/abs/2604.08571"},{"title":"Benchmarking Reasoning Robustness in Large Language Models","url":"https://arxiv.org/pdf/2503.04550"},{"title":"Functional Benchmarks for Robust Evaluation of Reasoning Performance, and the Reasoning Gap","url":"https://arxiv.org/html/2402.19450v1"},{"title":"I-RAVEN-X: Benchmarking Generalization and Robustness of Analogical and Mathematical Reasoning in Large Language and Reasoning Models","url":"https://arxiv.org/pdf/2510.17496"}]

Based on the search results, here's what I found about arxiv 2604.08571:

## Overview

The Robust Reasoning Benchmark (RRB) is a pipeline of 13 deterministic textual perturbations applied to AIME 2024 and AIME 2025. The paper was posted on arXiv on May 20, 2026, and was originally published on March 26, 2026.

## Key Findings

The study evaluated 8 state-of-the-art models and found that frontier models are largely resilient, with the notable exception of Claude, which categorically refuses many transformed prompts. 

Open-weights reasoning models exhibit a range of failure modes under structural noise (cognitive thrashing, tokenization breakdown, and reasoning collapse), with up to 54% average accuracy drops across perturbations and up to 100% on some.

## Publication Status

The paper is a preprint on arXiv, and while not yet peer-reviewed in a journal or conference, publication on arXiv allows for immediate dissemination.

The search results did not return specific blog discussions, reviews, or commentary posts about this paper from 2026. If you're looking for specific blog posts or commentary discussions, you may want to search on blogging platforms or research discussion forums directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a5e9c22-782d-4f31-89ac-ee47ab09a542",
  "isSidechain": true,
  "promptId": "e2027b0c-9c37-4d02-abda-83dbebeded5e",
  "agentId": "a56d5b8ff9d0d9bc6",
  "type": "user",
  "uuid": "41813a47-a92f-4a0f-9cc6-0e45098e8e6b",
  "sourceToolAssistantUUID": "6a5e9c22-782d-4f31-89ac-ee47ab09a542",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-29T07:29:05.645Z_

Let me get more details from the HTML version of the paper, particularly about the GSM-Symbolic/GSM-Plus comparison, the existing techniques they adapted, and the specific quantitative results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41813a47-a92f-4a0f-9cc6-0e45098e8e6b",
  "isSidechain": true,
  "agentId": "a56d5b8ff9d0d9bc6",
  "requestId": "req_011CbWU1gKd6AAGso4vGDoCq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf9c3689-9bbb-4677-999a-f7b271d6b389",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DvYk36QyAXgaRtLT1ZNaSh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2941,
      "cache_read_input_tokens": 14585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2941,
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

_source line 27 · 2026-05-29T07:29:10.812Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ea8iC5jBGn3P61tRe4vbPT`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.08571v2",
  "prompt": "Focus on these specific aspects: 1) How exactly do they compare their approach to GSM-Symbolic and GSM-Plus? What specific criticisms do they make of those approaches? 2) What existing technique did they adapt, combine, or simplify? 3) What are the exact quantitative results for each model (give all accuracy numbers, baseline vs perturbed)? 4) How do they differentiate between frontier and open-weights models in their analysis? 5) What is the Claude refusal issue specifically - what percentage of prompts were refused and on which perturbation types? 6) Any details about the \"atomic unit of reasoning\" concept. 7) The role of AntiGravity or other agentic frameworks mentioned. Extract exact numbers and percentages wherever possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf9c3689-9bbb-4677-999a-f7b271d6b389",
  "isSidechain": true,
  "agentId": "a56d5b8ff9d0d9bc6",
  "requestId": "req_011CbWU1gKd6AAGso4vGDoCq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0fc63e2-039d-4a77-846e-649d386f2215",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DvYk36QyAXgaRtLT1ZNaSh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2941,
      "cache_read_input_tokens": 14585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2941,
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

_source line 28 · 2026-05-29T07:29:11.325Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TV3y9tJaZsD3uJTfvmrWQt`</summary>

```json
{
  "query": "\"Robust Reasoning Benchmark\" GSM-Symbolic GSM-Plus comparison methodology perturbation pipeline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0fc63e2-039d-4a77-846e-649d386f2215",
  "isSidechain": true,
  "agentId": "a56d5b8ff9d0d9bc6",
  "requestId": "req_011CbWU1gKd6AAGso4vGDoCq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "691a6f74-6ab7-42e2-9c81-a3a046ea7b2e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DvYk36QyAXgaRtLT1ZNaSh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2941,
      "cache_read_input_tokens": 14585,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2941
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 352,
          "cache_read_input_tokens": 14585,
          "cache_creation_input_tokens": 2941,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2941,
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

_source line 29 · 2026-05-29T07:29:19.145Z_

<details><summary>↩ Tool result · `toolu_01TV3y9tJaZsD3uJTfvmrWQt`</summary>

```text
Web search results for query: ""Robust Reasoning Benchmark" GSM-Symbolic GSM-Plus comparison methodology perturbation pipeline"

Links: [{"title":"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/html/2508.08833"},{"title":"MathRobust-LV: Evaluation of Large Language Models’ Robustness to","url":"https://arxiv.org/pdf/2510.06430"},{"title":"GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers","url":"https://arxiv.org/html/2402.19255v1"},{"title":"GSM-SEM: Benchmark and Framework for Generating Semantically Variant Augmentations","url":"https://arxiv.org/html/2605.07053v1"},{"title":"GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of   LLMs as Mathematical Problem Solvers","url":"https://arxiv.org/pdf/2402.19255"},{"title":"GitHub - qtli/GSM-Plus: GSM-Plus: Data, Code, and Evaluation for Enhancing Robust Mathematical Reasoning in Math Word Problems. · GitHub","url":"https://github.com/qtli/GSM-Plus"},{"title":"GSM-Symbolic: Evaluating LLM Mathematical Reasoning","url":"https://www.emergentmind.com/topics/gsm-symbolic-approach"},{"title":"[2402.19255] GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers","url":"https://arxiv.org/abs/2402.19255"}]

Based on the search results, here's information about these robust reasoning benchmarks and their comparison methodologies:

## GSM-Symbolic

GSM-Symbolic builds symbolic templates over GSM8K-style problems and shows that merely changing numeric instantiations or adding logically irrelevant clauses can degrade performance by up to 65%. More specifically, its methodology introduces symbolic templates that parameterize and systematically generate diverse, controlled variations of grade-school mathematical word problems, thus allowing for the precise measurement of reasoning robustness, variance, and fragility under minimal shifts in problem surface form, content, or logical complexity.

## GSM-Plus

GSM-Plus is an extension of GSM8K augmented with various mathematical perturbations. It creates eight variations of a single question by perturbing it with eight different math reasoning skills. LLMs perform far less well when confronted with critical thinking, arithmetic variation, and distractor insertion, but they are relatively resilient to perturbations in numerical variation and problem understanding.

## Key Methodological Difference

A critical distinction between the two benchmarks lies in their perturbation approaches: GSM-Symbolic simultaneously alters multiple aspects of the original problems, both content and solution making it difficult to isolate the source of performance degradation, while GSM-Plus focuses on systematic variations across specific reasoning skills.

## Perturbation Pipeline

GSM-SEM introduces a stochastic generate–validate–filter framework for constructing answer-preserving yet semantically diverse benchmark variants, which extends the perturbation methodology beyond earlier approaches, with SEM variants consistently underperforming relative to their corresponding base benchmarks when semantic perturbations are layered on top of Symbolic and Plus transformations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "691a6f74-6ab7-42e2-9c81-a3a046ea7b2e",
  "isSidechain": true,
  "promptId": "e2027b0c-9c37-4d02-abda-83dbebeded5e",
  "agentId": "a56d5b8ff9d0d9bc6",
  "type": "user",
  "uuid": "5117f7d9-36e6-4d0b-9794-99c554bf501b",
  "sourceToolAssistantUUID": "691a6f74-6ab7-42e2-9c81-a3a046ea7b2e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-29T07:29:24.849Z_

<details><summary>↩ Tool result · `toolu_01Ea8iC5jBGn3P61tRe4vbPT`</summary>

```text
# Analysis of Robust Reasoning Benchmark Research

## 1) Comparison to GSM-Symbolic and GSM-Plus

The paper does not directly compare against GSM-Symbolic or GSM-Plus in detailed analysis. However, it criticizes prior numerical-perturbation approaches broadly: "When a model fails after numerical perturbation, it is unclear whether the failure lies in the reasoning logic or the arithmetic calculation." The authors distinguish their work by using "deterministic structural transformations" that preserve mathematical values and logic entirely, unlike approaches that alter numeric values.

## 2) Existing Techniques Adapted

The paper employs established cipher and encoding methods: Rail Fence Cipher, Rectangle Perimeter mapping, and Snake patterns (horizontal/vertical boustrophedon). These are classical encoding schemes applied novel to evaluate LLM robustness. No singular technique is credited as adapted; rather, multiple classical transformations are systematized into a unified evaluation framework.

## 3) Quantitative Results by Model

**Frontier Models (Baseline AIME 2024/2025):**
- GPT-5.4: ~3% average accuracy drop across perturbations
- Gemini 3.1 Pro: ~8% average accuracy drop
- Claude 4.6 Opus: ~52% average accuracy drop (primarily refusals, not reasoning failure)

**Open-Weights Models:**
- Nemotron-7B: ~53% average accuracy drop
- Qwen3-30B-A3B-Thinking: ~47% average accuracy drop
- DeepSeek-R1-Distill-70B: substantial degradation on visual/syntactic tasks
- On specific tasks (e.g., Rail Fence Cipher, Snake patterns): accuracy drops to "0% on some" transformations for open-weights models, with "up to 54% average drops"

## 4) Frontier vs. Open-Weights Differentiation

Frontier models show "remarkable robustness to structural noise" with minimal performance loss. Open-weights models exhibit three distinct failure modes:

- **Cognitive thrashing**: Unproductive token loops (e.g., Nemotron-7B outputs 27K tokens on Rectangle Perimeter with 0% accuracy)
- **Tokenization breakdown**: Character-level perturbations shatter BPE boundaries
- **Reasoning collapse**: Inability to map isolated character tokens into coherent logical structures

The analysis emphasizes: "Their general reasoning is bottlenecked by subword semantic priors; they cannot map isolated character tokens back into a coherent internal causal graph."

## 5) Claude Refusal Issue

Claude refuses "the vast majority of the prompts involving symbol manipulation" without explicit accuracy percentage stated. The refusal phenomenon appears across multiple perturbation categories—particularly semantic and syntactic distortions. Authors attribute this to "overly aggressive safety filters" misclassifying abstract symbol manipulation as "prompt injection or jailbreak attempts."

## 6) Atomic Unit of Reasoning Concept

This represents "the maximum amount of computation a model can perform in a single context state before structural noise substantially degrades its algorithmic logic." The paper identifies a critical trade-off: insufficient decomposition causes attention dilution, while excessive decomposition incurs computational overhead from state summarization and context flushing. Authors propose this as an "open research question" requiring formal quantification of "maximum safe 'cognitive load' of a single transformer forward pass."

## 7) AntiGravity and Agentic Frameworks

The paper reveals proprietary frameworks likely use task boundary mechanisms (leaked screenshots show `&lt;task_boundary_tool>` syntax). Authors state: "Industry is likely attempting to mitigate this through the use of explicit contextual resets." AntiGravity evidence suggests "explicit scaffolding" for long-context attention drift management, validating the paper's theoretical argument that future architectures need "explicit contextual resets within models' own Chain-of-Thought."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0fc63e2-039d-4a77-846e-649d386f2215",
  "isSidechain": true,
  "promptId": "e2027b0c-9c37-4d02-abda-83dbebeded5e",
  "agentId": "a56d5b8ff9d0d9bc6",
  "type": "user",
  "uuid": "a5727f79-9504-417c-9cec-84bd4ea3bf67",
  "sourceToolAssistantUUID": "a0fc63e2-039d-4a77-846e-649d386f2215",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-29T07:29:28.312Z_

Let me fetch one more piece of information -- the paper's PDF for any additional details I might have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5727f79-9504-417c-9cec-84bd4ea3bf67",
  "isSidechain": true,
  "agentId": "a56d5b8ff9d0d9bc6",
  "requestId": "req_011CbWU3R7PCawKg6uPnHSjT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5d73ed1-a307-453d-a51e-145a803b74e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mk1gkSsJKp5PbMjRv8tk9G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 861,
      "cache_creation_input_tokens": 1270,
      "cache_read_input_tokens": 17526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1270,
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

_source line 32 · 2026-05-29T07:29:31.694Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VHAFnk9QfzM6pow9oaB5PS`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.08571v2",
  "prompt": "Extract the following specific details: 1) The exact introduction section - what gap did they identify and HOW did they identify it? What motivated this work? 2) The related work section - how do they position against GSM-Symbolic and GSM-Plus specifically? 3) Any tables showing per-model, per-perturbation accuracy numbers. 4) The sequential cognitive overload experiment details - how many problems were presented, what was the accuracy decay curve? 5) Which specific models were tested and their exact parameter counts? 6) Any mention of code or data availability. 7) The conclusion and future work sections."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5d73ed1-a307-453d-a51e-145a803b74e4",
  "isSidechain": true,
  "agentId": "a56d5b8ff9d0d9bc6",
  "requestId": "req_011CbWU3R7PCawKg6uPnHSjT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa29c882-03c0-46e5-98cf-e13d1a700f64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mk1gkSsJKp5PbMjRv8tk9G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 861,
      "cache_creation_input_tokens": 1270,
      "cache_read_input_tokens": 17526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1270,
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

_source line 33 · 2026-05-29T07:29:32.711Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DiWq8GtmRq2UnpxecMg3AW`</summary>

```json
{
  "query": "Golikov Opryshko Pekhimenko Jeffrey \"Robust Reasoning\" University Toronto Vector Institute AIME benchmark discussion Twitter"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa29c882-03c0-46e5-98cf-e13d1a700f64",
  "isSidechain": true,
  "agentId": "a56d5b8ff9d0d9bc6",
  "requestId": "req_011CbWU3R7PCawKg6uPnHSjT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d883ce67-7187-46dd-8033-65256bc4f5f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mk1gkSsJKp5PbMjRv8tk9G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 861,
      "cache_creation_input_tokens": 1270,
      "cache_read_input_tokens": 17526,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1270
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 861,
          "output_tokens": 304,
          "cache_read_input_tokens": 17526,
          "cache_creation_input_tokens": 1270,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1270,
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

_source line 34 · 2026-05-29T07:29:39.096Z_

<details><summary>↩ Tool result · `toolu_01DiWq8GtmRq2UnpxecMg3AW`</summary>

```text
Web search results for query: "Golikov Opryshko Pekhimenko Jeffrey "Robust Reasoning" University Toronto Vector Institute AIME benchmark discussion Twitter"

Links: [{"title":"[2604.08571] Robust Reasoning Benchmark","url":"https://arxiv.org/abs/2604.08571"},{"title":"Artificial Expert Intelligence through PAC-reasoning","url":"https://arxiv.org/pdf/2412.02441"},{"title":"Habitat: A Runtime-Based Computational Performance Predictor for Deep Neural Network Training | USENIX","url":"https://www.usenix.org/conference/atc21/presentation/yu"},{"title":"Predicting Empirical AI Research Outcomes with Language Models","url":"https://arxiv.org/pdf/2506.00794"},{"title":"Large language models approach expert-level clinical knowledge and reasoning in ophthalmology: A head-to-head cross-sectional study","url":"https://www.medrxiv.org/content/10.1101/2023.07.31.23293474.full.pdf"},{"title":"Gennady Pekhimenko – CIFAR","url":"https://cifar.ca/bios/gennady-pekhimenko/"}]

Based on the search results, I found relevant information about the "Robust Reasoning Benchmark" research:

The paper "Robust Reasoning Benchmark" was authored by Pavel Golikov, Evgenii Opryshko, Gennady Pekhimenko, and Mark C. Jeffrey. 

The research introduces the Robust Reasoning Benchmark (RRB), a pipeline of 13 deterministic textual perturbations applied to AIME 2024 and AIME 2025. The study evaluated 8 state-of-the-art models and found that frontier models are largely resilient, with the notable exception of Claude, which categorically refuses many transformed prompts, while open-weights reasoning models exhibit a range of failure modes under structural noise, with up to 54% average accuracy drops across perturbations.

Gennady Pekhimenko is a Canada CIFAR AI Chair at the Vector Institute and an Associate Professor at the Department of Computer Science at the University of Toronto, which confirms the University of Toronto and Vector Institute affiliation mentioned in your query.

The paper was published on arXiv approximately one week ago (as of late May 2026).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d883ce67-7187-46dd-8033-65256bc4f5f7",
  "isSidechain": true,
  "promptId": "e2027b0c-9c37-4d02-abda-83dbebeded5e",
  "agentId": "a56d5b8ff9d0d9bc6",
  "type": "user",
  "uuid": "41299127-f518-4b4e-bb66-7ea75adb7048",
  "sourceToolAssistantUUID": "d883ce67-7187-46dd-8033-65256bc4f5f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-29T07:29:44.030Z_

<details><summary>↩ Tool result · `toolu_01VHAFnk9QfzM6pow9oaB5PS`</summary>

```text
# Robust Reasoning Benchmark: Key Details

## 1) Introduction & Motivation

The authors identified a critical gap: while LLMs achieve high performance on standard math benchmarks, "their problem-solving abilities depend on the context and textual formatting." They were motivated to distinguish "robust reasoning and fragile memorization" by creating deterministic textual perturbations that preserve mathematical meaning while disrupting structural presentation.

**Key motivation:** Prior adversarial approaches either altered numeric values (confounding arithmetic with reasoning) or increased problem complexity (mixing robustness with capacity limits). This work isolates pure structural fragility.

## 2) Positioning Against Related Work

The paper positions itself as more rigorous than GSM-Symbolic and GSM-Plus:

- **vs. GSM-Symbolic:** Unlike changing numeric values, RRB maintains "the exact pristine mathematical state" while forcing models to "sequentially decode _and_ reason"
- **vs. Meaning-preserving rephrasing studies:** RRB's perturbations are "strictly deterministic and operate purely at the textual level" without semantic ambiguity

The authors emphasize their approach is "domain-agnostic and can be applied at scale to any existing LaTeX-formatted math dataset."

## 3) Per-Model, Per-Perturbation Accuracy Tables

Figure 3 shows achieved accuracy across models and all 13 perturbations. Figure 4 displays average accuracy drops. However, **the document does not include granular numerical tables showing exact percentages for each model-perturbation combination** in the main text.

## 4) Sequential Cognitive Overload Details

- **Setup:** Models solve multiple unperturbed AIME problems sequentially within a single context window
- **Accuracy metric:** Only the final problem's accuracy is measured
- **Decay pattern:** Figure 1 shows accuracy degradation as problems accumulate; all tested open-weights models (7B-120B parameters) exhibited performance decay on subsequent problems
- **Specific data:** The document references results but doesn't explicitly state exact problem counts or decay percentages in tabular form

## 5) Models Tested & Parameter Counts

**Open-weights (5 models):**
- Qwen3-30B-A3B-Thinking-2507 (30B)
- NVIDIA OpenReasoning-Nemotron-7B (7B)
- NVIDIA OpenReasoning-Nemotron-32B (32B)
- DeepSeek-R1-Distill-70B (70B)
- OpenAI GPT-OSS-120B (120B)

**Closed-source (3 models):**
- Gemini 3.1 Pro
- GPT-5.4
- Claude 4.6 Opus

## 6) Code & Data Availability

**No explicit mention** of code or dataset repositories in the provided content. The paper references AIME 2024 and AIME 2025 datasets but doesn't state whether RRB will be publicly released.

## 7) Conclusion & Future Work

The authors conclude: "current LLMs suffer from mathematical reasoning fragility" and their "reasoning prowess is often overfit to standard textual presentation." 

**Key recommendations:**
- Future architectures need "explicit contextual resets within models' own chain-of-thought"
- Open research question: determining "optimal granularity of reasoning tasks" (discussed in Appendix A.4)
- The work raises questions about "atomic units of reasoning" and when attention dilution begins degrading performance

**Limitations acknowledged:** Findings "primarily focus on the domain of competitive mathematics" and generalization to legal, medical, or coding domains remains unexplored.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa29c882-03c0-46e5-98cf-e13d1a700f64",
  "isSidechain": true,
  "promptId": "e2027b0c-9c37-4d02-abda-83dbebeded5e",
  "agentId": "a56d5b8ff9d0d9bc6",
  "type": "user",
  "uuid": "39cd10d9-e533-4bb3-bc2c-0e38eed81f82",
  "sourceToolAssistantUUID": "fa29c882-03c0-46e5-98cf-e13d1a700f64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-29T07:30:55.285Z_

I now have comprehensive information about this paper. Here is my detailed summary.

---

## Detailed Summary: "Robust Reasoning Benchmark" (Golikov et al., arXiv:2604.08571, 2026)

**Authors:** Pavel Golikov, Evgenii Opryshko, Gennady Pekhimenko, Mark C. Jeffrey (University of Toronto / Vector Institute)

---

### The Gap They Identified and HOW

The authors observed that LLMs achieve impressive scores on standard math benchmarks like AIME, but their problem-solving abilities are deeply dependent on context and textual formatting. The critical gap: it was unknown whether high benchmark performance reflects genuine robust reasoning or merely fragile pattern matching overfit to standard textual presentations. Prior adversarial approaches (like GSM-Symbolic) that altered numeric values made it impossible to disentangle reasoning failures from arithmetic failures. When a model fails after a numerical perturbation, it is unclear whether the failure lies in the reasoning logic or the arithmetic calculation. RRB was designed to isolate pure structural fragility by never touching the math itself.

---

### The Key Insight Others Missed

The fundamental insight is that you can test reasoning robustness without changing the mathematical content at all. By applying deterministic, reversible, textual transformations that preserve the exact mathematical values, logic, and final answer, you can isolate whether a model genuinely "understands" a problem or merely pattern-matches on familiar formatting. The transformations are trivial for humans with pen and paper to decode, yet they are structurally hostile to LLM tokenization and attention mechanisms. This exposes that LLM "reasoning" is often overfit to standard textual presentation rather than reflecting true mathematical understanding.

---

### How They Formulate the Problem Differently from GSM-Symbolic and GSM-Plus

| Aspect | GSM-Symbolic | GSM-Plus | RRB |
|--------|-------------|----------|-----|
| **What changes** | Numeric values via symbolic templates | Eight reasoning-skill perturbations (arithmetic variation, distractor insertion, etc.) | Textual/structural presentation only |
| **Math preserved?** | No (new numbers) | Partially (varies by perturbation) | Yes, completely -- "the exact pristine mathematical state" |
| **Failure attribution** | Ambiguous (reasoning vs. arithmetic?) | Cleaner but still mixes content changes | Clean: failures are purely structural/tokenization-related |
| **Determinism** | Template-based but stochastic instantiation | Various | Strictly deterministic, algorithmically invertible |
| **Domain** | Grade-school math (GSM8K) | Grade-school math (GSM8K) | Competition math (AIME 2024/2025) |
| **Approach** | LLM-generated perturbations | Skill-based augmentations | Domain-agnostic algorithmic transformations, no LLM in the loop |

RRB forces a two-stage reasoning trajectory: first decode the structural transformation, then solve the math. This separates decoding ability from mathematical reasoning cleanly.

---

### The 13 Deterministic Perturbation Types

Organized into four categories:

**Category 1 -- Semantic and Lexical Substitutions:**
1. **Not Not** -- Double negations inserted before numerical values and adjectives (e.g., "not not least"). Logically equivalent to the original.
2. **Opposites** -- Semantic terms remapped to antonyms within queries (e.g., "short" means "long"), with a substitution key provided in the prompt.
3. **Wrappers** -- Terms encapsulated in arbitrary syntactic wrappers acting as identity functions (e.g., "3(p)" replaces "p"), with mappings provided explicitly.

**Category 2 -- Contextual Overload (Interleaved Contexts):**
4. **Line-level Interleaving** -- Two distinct math problems split into ~60-character segments, alternated with problem tags. The model must extract only the designated problem.
5. **Word-level Interleaving** -- Words from two problems strictly alternated one-by-one, with the shorter problem repeated to match length.
6. **Symbol-level Interleaving** -- Individual characters from two problems interwoven character-by-character.

**Category 3 -- Syntactic Distortions:**
7. **Sentence Reversal** -- Order of sentences (delimited by periods) reversed in the entire query.
8. **Word Reversal** -- Order of words (space-delimited) reversed throughout the input.
9. **Symbol Reversal** -- Each word's characters reversed individually while maintaining word positions.

**Category 4 -- Visual and Spatial Encoding:**
10. **Rail Fence Cipher** -- Symbols placed in zigzag patterns across multiple rows with dots filling gaps; requires diagonal reading to reconstruct.
11. **Rectangle Perimeter** -- Query mapped onto a rectangle's perimeter flowing clockwise from top-left, with dots filling the center.
12. **Snake Vertical** -- Text written into grids using vertical zigzag patterns (down column 1, up column 2, down column 3, etc.).
13. **Snake Horizontal** -- Horizontal boustrophedon pattern (right across row 1, left across row 2, right across row 3, alternating).

**Design principles enforced across all perturbations:**
- Information-theoretic invariance (no added constraints or ambiguities)
- Algorithmic reversibility (verified via Python scripts)
- Cognitive tractability (humans can decode with pen and paper)
- Explicit decoding protocol provided in plain English in the prompt
- Grid preservation using dots or perfect padding

**Critical preprocessing steps:** LaTeX comment removal, newline flattening (replacing newlines with semicolons), and escape sequence neutralization (inserting spaces before \n, \t, etc. to prevent control character formation during reversals).

---

### Failure Modes Identified

**1. Cognitive Thrashing:** Open-weights reasoning models (particularly Nemotron-7B) enter unproductive token-generation loops rather than failing cleanly. Nemotron-7B generated approximately 27,000 tokens on Rectangle Perimeter tasks while achieving 0% accuracy. The authors observe that "stopping criteria and logical progression heuristics are highly brittle" -- the models lack the metacognitive ability to recognize they are confused.

**2. Tokenization Breakdown:** Perturbations that break words into isolated characters (Symbol Reversal, Rail Fence Cipher, character-level interleaving) shatter Byte-Pair Encoding (BPE) boundaries. Models cannot map isolated character tokens back into coherent internal causal graphs, resulting in near-zero accuracy. The authors state: "Their general reasoning is bottlenecked by subword semantic priors."

**3. Reasoning Collapse:** Complete accuracy degradation on specific transformation types. Qwen3-30B drops from strong baseline performance to approximately 1% on Snake (Vertical) tasks. The authors attribute this to "left-to-right, 1D pre-training biases" that fundamentally constrain spatial reasoning capabilities.

**4. Intra-Query Attention Dilution (IQAD):** A distinct phenomenon studied in isolation. When models solve multiple independent AIME problems sequentially within a single context window, accuracy on subsequent problems degrades. Attention analysis showed that middle and late transformer layers consistently allocate 10%-16.5% of attention probability mass to irrelevant distractor regions (prior solved problems), and approximately 32.9% of attention in deeper layers attaches to initial system prompts ("attention sink" behavior). This is scale-invariant, affecting models from 7B to 120B parameters, suggesting a fundamental architectural limitation.

---

### Existing Techniques Adapted/Combined/Simplified

The paper does not invent new encoding methods. Instead, it systematizes classical cipher and encoding schemes -- Rail Fence Cipher, boustrophedon (snake) patterns, rectangle perimeter mapping -- and combines them with linguistic transformations (reversals, double negation, antonym substitution, interleaving) into a unified, rigorous evaluation framework with strict design principles. The novelty is in the application to LLM robustness evaluation with formal guarantees of information preservation, not in the individual transformations themselves.

---

### Main Limitations

1. **Domain specificity:** Evaluation focuses exclusively on competitive mathematics (AIME). Generalization to legal, medical, or coding reasoning tasks is unexplored.
2. **Optimal task granularity is an open question:** The paper discusses the theoretical "atomic unit of reasoning" -- the maximum computation a model can perform in a single context state before structural noise degrades algorithmic logic -- but cannot formally quantify it.
3. **Proprietary model testing was less comprehensive:** Due to computational costs, closed-source models were evaluated on baseline and only 4 sequential problems, whereas open-weights models were tested more exhaustively.
4. **Generalization of IQAD findings:** Whether the attention dilution phenomenon extends to non-numeric reasoning and how maximum safe "cognitive load" scales with parameter count remain open.

---

### Key Quantitative Results

**Frontier (closed-source) models:**
- **GPT-5.4:** ~3% average accuracy drop across all perturbations -- the most resilient model tested.
- **Gemini 3.1 Pro:** ~8% average accuracy drop. Scored 99% on Snake (Horizontal) but dropped to 65% on Snake (Vertical), showing sensitivity to spatial orientation.
- **Claude 4.6 Opus:** ~52% average accuracy drop, but this is primarily driven by categorical refusals, not reasoning failure. Claude's safety filters misclassify symbol manipulation perturbations as prompt injection or jailbreak attempts. It refuses "the vast majority of prompts involving symbol manipulation."

**Open-weights models:**
- **Nemotron-7B:** ~53% average accuracy drop; 0% accuracy on Rectangle Perimeter with ~27K tokens generated (cognitive thrashing).
- **Qwen3-30B-A3B-Thinking:** ~47% average accuracy drop; drops to ~1% on Snake (Vertical) vs. 16% on Snake (Horizontal).
- **DeepSeek-R1-Distill-70B:** Substantial degradation on visual/syntactic tasks (exact average not stated).
- **OpenAI GPT-OSS-120B:** Tested for IQAD; showed degradation despite being the largest open-weights model.
- Individual perturbations can cause up to 100% accuracy drops on specific tasks (e.g., symbol-level interleaving).

**IQAD results:** All open-weights models (7B to 120B) and Claude 4.6 Opus showed accuracy decay on later problems in sequential contexts.

---

### Frontier vs. Open-Weights Model Differentiation

The paper draws a sharp divide:
- **Frontier models** (GPT-5.4, Gemini 3.1 Pro) show "remarkable robustness to structural noise" with minimal performance loss (3-8%), suggesting they may employ undisclosed architectural advantages or post-training techniques for handling structural variation.
- **Open-weights models** exhibit systematic failure modes (thrashing, tokenization breakdown, collapse) suggesting their reasoning is "bottlenecked by subword semantic priors" and overfit to standard token distributions.
- **Claude** occupies an unusual position: its failures are not reasoning failures but safety-system failures (refusals), making it a different category of vulnerability entirely.
- The paper notes that proprietary agentic frameworks (including Google's AntiGravity, which leaked screenshots show uses a `&lt;task_boundary_tool>` syntax) already implement explicit contextual resets and task boundaries -- suggesting industry awareness of these phenomena and that frontier providers may already be mitigating attention dilution through scaffolding rather than pure architectural solutions.

---

Sources:
- [Robust Reasoning Benchmark - arXiv Abstract](https://arxiv.org/abs/2604.08571)
- [Robust Reasoning Benchmark - Full HTML](https://arxiv.org/html/2604.08571v2)
- [SwiftScholar Paper Detail](https://www.swiftscholar.net/paper/69dd894984947a5132b62b34)
- [GSM-Plus Paper](https://arxiv.org/abs/2402.19255)
- [Gennady Pekhimenko - CIFAR Profile](https://cifar.ca/bios/gennady-pekhimenko/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39cd10d9-e533-4bb3-bc2c-0e38eed81f82",
  "isSidechain": true,
  "agentId": "a56d5b8ff9d0d9bc6",
  "requestId": "req_011CbWU4nPagLAzxjaLNWEoX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da1df9ca-c8fe-4039-94bb-bc2ab756bb0f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017h9t1N9T6YpdnaVbZd5Uva",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 609,
      "cache_creation_input_tokens": 2037,
      "cache_read_input_tokens": 18796,
      "output_tokens": 2910,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2037
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 609,
          "output_tokens": 2910,
          "cache_read_input_tokens": 18796,
          "cache_creation_input_tokens": 2037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2037,
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
