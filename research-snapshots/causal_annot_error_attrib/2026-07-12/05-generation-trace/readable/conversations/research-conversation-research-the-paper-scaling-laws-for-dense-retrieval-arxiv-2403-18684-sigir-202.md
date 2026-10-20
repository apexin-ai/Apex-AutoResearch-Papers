# Research conversation: Research the paper "Scaling Laws for Dense Retrieval" (arXiv 2403.18684, SIGIR 2024 Best Paper). 1. Use WebFetch to read

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a68e4306d3984469c.jsonl`
- **Structured JSON:** [`4da11e33a97ba84cac33.json`](../../sessions/4d/4da11e33a97ba84cac33.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

33 recorded events

### User

_source line 1 · 2026-05-30T06:20:54.900Z_

Research the paper "Scaling Laws for Dense Retrieval" (arXiv 2403.18684, SIGIR 2024 Best Paper). 

1. Use WebFetch to read the arxiv abstract page: https://arxiv.org/abs/2403.18684
2. Use WebFetch to read the HTML version for method details: https://arxiv.org/html/2403.18684
3. Search for any reviews or discussions about this paper being SIGIR 2024 Best Paper.

Extract:
- The exact gap/problem they identified
- Their key contributions: what scaling laws they discovered, the functional form (power-law relationships)
- Method details: how they derived scaling laws, what models/data they used, experimental setup
- How model size and training data quantity affect dense retrieval performance
- Practical implications for compute budget allocation
- Any specific numbers: scaling exponents, model sizes tested, datasets used

Be thorough with technical details about the scaling law formulation and how it can guide resource allocation decisions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "agentId": "a68e4306d3984469c",
  "type": "user",
  "uuid": "954d1f40-dc84-464a-8476-b0ab9235b61c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-30T06:20:54.903Z_

```json
{
  "parentUuid": "954d1f40-dc84-464a-8476-b0ab9235b61c",
  "isSidechain": true,
  "agentId": "a68e4306d3984469c",
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
  "uuid": "465a45ec-4c84-4093-a23a-63b0d157503e",
  "timestamp": "2026-05-30T06:20:54.903Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-30T06:20:54.904Z_

```json
{
  "parentUuid": "465a45ec-4c84-4093-a23a-63b0d157503e",
  "isSidechain": true,
  "agentId": "a68e4306d3984469c",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b254b292-fdca-4035-9ecc-ce39c5f4c70d",
  "timestamp": "2026-05-30T06:20:54.904Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-30T06:20:57.213Z_



I'll research this paper thoroughly. Let me start by fetching the necessary tools and then the paper content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b254b292-fdca-4035-9ecc-ce39c5f4c70d",
  "isSidechain": true,
  "agentId": "a68e4306d3984469c",
  "requestId": "req_011CbYGdKkj4TFZtqVNeNJYh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2112e291-7c75-43d4-9bad-c5ede1cb0650",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtKNSiMw6FH3SHmsbXTD4j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1564,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1564,
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

_source line 5 · 2026-05-30T06:20:57.870Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Eo4EN7tkwTzqpgCj8STkk9`</summary>

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
  "parentUuid": "2112e291-7c75-43d4-9bad-c5ede1cb0650",
  "isSidechain": true,
  "agentId": "a68e4306d3984469c",
  "requestId": "req_011CbYGdKkj4TFZtqVNeNJYh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c7c4741-01b3-47f8-908c-8a053023601e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtKNSiMw6FH3SHmsbXTD4j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1564,
      "cache_read_input_tokens": 7413,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1564
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 103,
          "cache_read_input_tokens": 7413,
          "cache_creation_input_tokens": 1564,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1564,
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

_source line 6 · 2026-05-30T06:20:57.878Z_

<details><summary>↩ Tool result · `toolu_01Eo4EN7tkwTzqpgCj8STkk9`</summary>

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
  "parentUuid": "7c7c4741-01b3-47f8-908c-8a053023601e",
  "isSidechain": true,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "agentId": "a68e4306d3984469c",
  "type": "user",
  "uuid": "d9ddca66-b785-4fe8-a7db-4b79d5210f38",
  "sourceToolAssistantUUID": "7c7c4741-01b3-47f8-908c-8a053023601e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-30T06:21:00.457Z_



Now let me fetch the paper content from multiple sources in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9ddca66-b785-4fe8-a7db-4b79d5210f38",
  "isSidechain": true,
  "agentId": "a68e4306d3984469c",
  "requestId": "req_011CbYGdYn4MpT6yHg714vgf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37aa5724-5dbb-4b22-8213-6070d03eb455",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155nkdUiqaE2z7PfeFJPyeT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 8977,
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

_source line 8 · 2026-05-30T06:21:03.552Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013qovKJTAZVZaakxLdUch2U`</summary>

```json
{
  "url": "https://arxiv.org/abs/2403.18684",
  "prompt": "Extract ALL details from this paper's abstract page: the full title, all authors, the complete abstract text, any metadata about publication venue (SIGIR 2024), submission dates, and any other information available on the page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37aa5724-5dbb-4b22-8213-6070d03eb455",
  "isSidechain": true,
  "agentId": "a68e4306d3984469c",
  "requestId": "req_011CbYGdYn4MpT6yHg714vgf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3815e71-4aaa-4e4b-b108-cf9daf2fe0c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155nkdUiqaE2z7PfeFJPyeT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 8977,
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

_source line 9 · 2026-05-30T06:21:09.171Z_

<details><summary>↩ Tool result · `toolu_013qovKJTAZVZaakxLdUch2U`</summary>

```text
# Paper Details: Scaling Laws For Dense Retrieval

**Full Title:** "Scaling Laws For Dense Retrieval"

**Authors:** Yan Fang, Jingtao Zhan, Qingyao Ai, Jiaxin Mao, Weihang Su, Jia Chen, Yiqun Liu

**arXiv Identifier:** 2403.18684

**Subject Categories:** Information Retrieval (cs.IR); Computation and Language (cs.CL)

**Submission History:**
- Version 1 submitted: March 27, 2024
- Version 2 (current): July 15, 2024

**Publication Venue:** Accepted at SIGIR 2024

**Abstract Summary:**
The research explores whether dense retrieval models follow predictable scaling laws like other neural models. The team proposes contrastive log-likelihood as an evaluation metric and conducts experiments varying model parameters and training data quantities. Their findings indicate that performance follows "a precise power-law scaling related to the model size and the number of annotations." The study also examines data augmentation effects on annotation quality and applies scaling insights to optimize resource allocation under budget constraints.

**DOI:** https://doi.org/10.48550/arXiv.2403.18684

**Available Formats:** PDF, HTML (experimental), TeX Source

**Note:** Version 2 corrected an experimental bug from the initial submission.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3815e71-4aaa-4e4b-b108-cf9daf2fe0c3",
  "isSidechain": true,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "agentId": "a68e4306d3984469c",
  "type": "user",
  "uuid": "814a0517-ad2e-4c4c-a2f4-d2ef1da6a226",
  "sourceToolAssistantUUID": "a3815e71-4aaa-4e4b-b108-cf9daf2fe0c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-30T06:21:09.576Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018ycRZziV7eTbaFEZoCV7r2`</summary>

```json
{
  "url": "https://arxiv.org/html/2403.18684",
  "prompt": "Extract ALL technical details from this paper. I need:\n1. The exact problem/gap they identified in dense retrieval scaling\n2. The functional form of their scaling laws - exact mathematical formulas, power-law relationships, exponents\n3. Method details: how they derived the scaling laws, what methodology they used\n4. All model sizes tested (parameter counts), all datasets used, training data quantities\n5. Experimental setup: training details, evaluation metrics, hardware\n6. Key results: specific scaling exponents/coefficients, how model size vs data quantity affect performance\n7. Practical implications: compute budget allocation recommendations, resource allocation guidance\n8. The concept of \"contrastive entropy\" or any custom metrics they defined\n9. Any tables or figures with specific numerical results\n10. Their conclusions about optimal scaling strategies\nBe extremely thorough and include all numbers, formulas, and technical specifics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "814a0517-ad2e-4c4c-a2f4-d2ef1da6a226",
  "isSidechain": true,
  "agentId": "a68e4306d3984469c",
  "requestId": "req_011CbYGdYn4MpT6yHg714vgf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc59d6d9-a804-4d7b-90d1-db1f97cdbb8b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155nkdUiqaE2z7PfeFJPyeT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 8977,
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

_source line 11 · 2026-05-30T06:21:09.811Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HJHkQqu8XLQw1JFt8eBbiN`</summary>

```json
{
  "query": "SIGIR 2024 Best Paper \"Scaling Laws for Dense Retrieval\" arXiv 2403.18684"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc59d6d9-a804-4d7b-90d1-db1f97cdbb8b",
  "isSidechain": true,
  "agentId": "a68e4306d3984469c",
  "requestId": "req_011CbYGdYn4MpT6yHg714vgf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4b8461c-b793-476a-b05d-551ff4e40217",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155nkdUiqaE2z7PfeFJPyeT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 8977,
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

_source line 12 · 2026-05-30T06:21:15.012Z_

<details><summary>↩ Tool result · `toolu_01HJHkQqu8XLQw1JFt8eBbiN`</summary>

```text
Web search results for query: "SIGIR 2024 Best Paper "Scaling Laws for Dense Retrieval" arXiv 2403.18684"

Links: [{"title":"[2403.18684] Scaling Laws For Dense Retrieval","url":"https://arxiv.org/abs/2403.18684"},{"title":"Scaling Laws For Dense Retrieval Yan Fang∗ Jingtao Zhan∗","url":"https://arxiv.org/pdf/2403.18684v1"},{"title":"Scaling Laws For Dense Retrieval Yan Fang∗ fangy21@mails.tsinghua.edu.cn","url":"https://arxiv.org/pdf/2403.18684"},{"title":"Scaling Laws for Dense Retrieval","url":"https://www.emergentmind.com/papers/2403.18684"},{"title":"Scaling Laws For Dense Retrieval","url":"https://arxiv.org/html/2403.18684"},{"title":"On the Scaling of Robustness and Effectiveness in Dense Retrieval","url":"https://arxiv.org/pdf/2505.24279"},{"title":"Scaling Laws For Dense Retrieval | Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/abs/10.1145/3626772.3657743"}]

Based on the search results, I found information about this paper. The paper "Scaling Laws For Dense Retrieval" (arXiv 2403.18684) was presented at SIGIR '24, July 14–18, 2024, in Washington, DC.

The paper investigates whether dense retrieval model performance follows scaling laws like other neural models, proposing to use contrastive log-likelihood as an evaluation metric and conducting extensive experiments with models of different sizes trained on different amounts of data.

The paper demonstrates power-law scaling in dense retrieval by examining model size, data volume, and annotation quality to optimize semantic search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4b8461c-b793-476a-b05d-551ff4e40217",
  "isSidechain": true,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "agentId": "a68e4306d3984469c",
  "type": "user",
  "uuid": "951a40f7-d514-4ea1-9b3a-a49c0fe83019",
  "sourceToolAssistantUUID": "b4b8461c-b793-476a-b05d-551ff4e40217",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-30T06:21:25.542Z_

<details><summary>↩ Tool result · `toolu_018ycRZziV7eTbaFEZoCV7r2`</summary>

````text
# Technical Details from "Scaling Laws For Dense Retrieval"

## 1. Problem/Gap Identified

The researchers identified that while scaling laws have been extensively studied in language generation, they remain unexplored in dense retrieval. They noted two specific challenges: (1) traditional ranking metrics like NDCG are discrete, limiting their ability to smoothly reflect performance changes, and (2) multiple interrelated factors (model size, annotation size, annotation quality) make it difficult to isolate individual effects.

## 2. Scaling Law Formulas

**Model Size Scaling:**
```
L(N) = (A/N)^α + δ_N
```
Where N = non-embedding parameters, L(N) = contrastive entropy

**Data Size Scaling:**
```
L(D) = (B/D)^β + δ_D
```
Where D = annotated query-passage pairs

**Joint Model-Data Scaling:**
```
L(N,D) = [(A/N)^(α/β) + B/D]^β + δ
```

## 3. Derivation Methodology

The authors: (1) implemented dense retrieval models varying in parameter count from 0.5M to 82M parameters; (2) trained on different data volumes; (3) measured performance using contrastive entropy (a continuous metric); (4) fitted power-law curves using least squares regression; (5) validated across multiple datasets and annotation methods.

## 4. Model Sizes and Datasets

**Models tested:** BERT-Tiny (0.5M) through BERT-Base (82M non-embedding parameters); ERNIE variants for Chinese

**Datasets:** 
- MS MARCO Passage Ranking: 0.5M training queries, 8.8M passages
- T2Ranking (Chinese): 300k+ queries, 2M+ unique passages

## 5. Experimental Setup

**Training:** 10,000 fixed steps, batch size 256, random negative sampling with 256 negatives per step, contrastive ranking loss optimization

**Evaluation:** Contrastive entropy metric defined as:
```
-log(exp(s(q_i, p_i^+; θ)) / (exp(s(q_i, p_i^+; θ)) + Σ_j exp(s(q_i, p_j^-; θ))))
```

**Validation:** Strong positive correlation demonstrated between contrastive entropy and ranking metrics (NDCG@10, MAP@10, Recall@1000)

## 6. Key Results with Coefficients

**MSMARCO Fitting Parameters:**
- Model scaling: A = 3.22×10⁴, α = 0.53, δ_N = 0.04, R² = 0.991
- Data scaling: B = 3.49×10³, β = 1.05, δ_D = 0.05, R² = 0.954

**T2Ranking Fitting Parameters:**
- Model scaling: A = 9.89×10⁶, α = 0.53, δ_N = 0.14, R² = 0.999
- Data scaling: B = 6.04×10⁴, β = 0.50, δ_D = 0.15, R² = 0.991

**Joint scaling (MSMARCO):** A ≈ 3.6×10⁴, B ≈ 7.1×10³, α ≈ 0.56, β ≈ 1.31, δ ≈ 0.03

## 7. Budget Allocation Recommendations

The authors calculated total lifecycle costs as:
```
Z(N,D) = Z_data·D + Z_train·N + Z_infer·N
```

**Cost estimates:** $0.6 per annotation; Z_train ≈ 3.22×10⁻⁸; Z_infer ≈ 0.43

**Key finding:** Excluding inference, optimal allocation favors larger models (13B parameters on $20k budget). Including inference costs, optimal models shrink to million-scale parameters due to inference dominance (Z_infer >> Z_train).

## 8. Contrastive Entropy Metric

This novel continuous metric measures "the likelihood of retrieving a relevant document from a randomly sampled candidate set." It mirrors the training loss structure and provides smoother performance gradients than discrete ranking metrics, enabling precise scaling law fitting. An emergent ability threshold appears around 0.25 contrastive entropy where ranking performance substantially improves.

## 9. Annotation Quality Results

Three data generation methods tested on MSMARCO:
- **Inverse Cloze Task (ICT):** Lowest quality, smallest slope
- **docT5query:** Medium quality, trained on human annotations
- **ChatGLM3:** Zero-shot generation, surpasses human annotations at 500k pairs despite lower per-sample quality

All methods demonstrated power-law scaling despite quality differences.

## 10. Optimal Scaling Strategy Conclusions

Dense retrieval performance follows precise power laws across model size, data size, and annotation methods. Larger models are more data-efficient. The irreducible loss term (δ) acknowledges incomplete annotations and subjective relevance. Practitioners can: (1) train smaller models and extrapolate performance via scaling laws rather than training large models directly; (2) estimate required annotation amounts for target performance; (3) optimize budget allocation accounting for data, training, and inference costs; (4) expect consistent scaling regardless of annotation method (though human annotations remain superior).
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc59d6d9-a804-4d7b-90d1-db1f97cdbb8b",
  "isSidechain": true,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "agentId": "a68e4306d3984469c",
  "type": "user",
  "uuid": "2c3f6043-05c5-4bfa-b077-3bb1f68146c9",
  "sourceToolAssistantUUID": "bc59d6d9-a804-4d7b-90d1-db1f97cdbb8b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-30T06:21:27.938Z_

Now let me search for more details about the SIGIR 2024 Best Paper award and any reviews/discussions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c3f6043-05c5-4bfa-b077-3bb1f68146c9",
  "isSidechain": true,
  "agentId": "a68e4306d3984469c",
  "requestId": "req_011CbYGfaeyaFarjj5nJhzhm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e157a4d-cfba-45d8-af01-07df2e016628",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtYHw54joZ1aPPCCz76cnF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 530,
      "cache_creation_input_tokens": 2149,
      "cache_read_input_tokens": 10102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2149,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 15 · 2026-05-30T06:21:28.433Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X2KjY1ppt6fWTNXGxfF6bK`</summary>

```json
{
  "query": "SIGIR 2024 Best Paper Award winner list Washington DC"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e157a4d-cfba-45d8-af01-07df2e016628",
  "isSidechain": true,
  "agentId": "a68e4306d3984469c",
  "requestId": "req_011CbYGfaeyaFarjj5nJhzhm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ee86dfa-0dcf-487d-9b5a-23b05d7043cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtYHw54joZ1aPPCCz76cnF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 530,
      "cache_creation_input_tokens": 2149,
      "cache_read_input_tokens": 10102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2149,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 16 · 2026-05-30T06:21:29.950Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01L4tH9VhSGKML1BqaTRf7LE`</summary>

```json
{
  "url": "https://dl.acm.org/doi/abs/10.1145/3626772.3657743",
  "prompt": "Extract all information about this paper from the ACM Digital Library page: publication details, awards mentioned, citation count, any supplementary information, conference details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ee86dfa-0dcf-487d-9b5a-23b05d7043cf",
  "isSidechain": true,
  "agentId": "a68e4306d3984469c",
  "requestId": "req_011CbYGfaeyaFarjj5nJhzhm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c4a43c2-3f2d-4592-8eb5-634d9dbdf786",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtYHw54joZ1aPPCCz76cnF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 530,
      "cache_creation_input_tokens": 2149,
      "cache_read_input_tokens": 10102,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2149
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 530,
          "output_tokens": 197,
          "cache_read_input_tokens": 10102,
          "cache_creation_input_tokens": 2149,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2149,
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

_source line 17 · 2026-05-30T06:21:30.182Z_

<details><summary>↩ Tool result · `toolu_01L4tH9VhSGKML1BqaTRf7LE`</summary>

```text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c4a43c2-3f2d-4592-8eb5-634d9dbdf786",
  "isSidechain": true,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "agentId": "a68e4306d3984469c",
  "type": "user",
  "uuid": "75b0f729-612d-4486-b859-9a028b6cc494",
  "sourceToolAssistantUUID": "3c4a43c2-3f2d-4592-8eb5-634d9dbdf786",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-30T06:21:34.532Z_

<details><summary>↩ Tool result · `toolu_01X2KjY1ppt6fWTNXGxfF6bK`</summary>

```text
Web search results for query: "SIGIR 2024 Best Paper Award winner list Washington DC"

Links: [{"title":"SIGIR 2024","url":"https://sigir-2024.github.io/keynotes.html"},{"title":"NExT Researchers Receive SIGIR Best Paper Honorable Mentions 2024","url":"https://www.nextcenter.org/post/next-researchers-receive-sigir-best-paper-honorable-mentions-2024"},{"title":"CIIR researchers receive ACM SIGIR 2024 Awards | Center for Intelligent Information Retrieval","url":"https://ciir.cs.umass.edu/node/757"},{"title":"CNR Wins the Best Paper Runner-Up Award at ACM SIGIR 2024 - EFRA Project","url":"https://efraproject.eu/cnr-wins-the-best-paper-runner-up-award-at-acm-sigir-2024/"},{"title":"Best Paper Awards | SIGIR","url":"https://sigir.org/awards/best-paper-awards/"},{"title":"Best Paper Awards","url":"https://sigir-2024.github.io/best_papers.html"},{"title":"ISTI-CNR - Best Paper Runner Up at SIGIR 2024","url":"https://www.isti.cnr.it/en/announcements/achievements/2508-best-paper-runner-up-at-sigir-2024"},{"title":"Best Paper Award Honorable Mention at SIGIR 2024 – IRLab","url":"https://irlab.science.uva.nl/2024/07/18/best-paper-award-honorable-mention-at-sigir-2024/"},{"title":"Executive Functioning in TBI From Rehabilitation to Social Reintegration: COMPASS","url":"https://clinicaltrials.gov/study/NCT01816061"},{"title":"SIGIR-AP 2024","url":"https://www.sigir-ap.org/sigir-ap-2024/bestpapers/"}]

Based on the search results, here's information about the SIGIR 2024 Best Paper Awards:

## Best Paper Award Winners

The 2024 SIGIR Best Paper Award was shared by Qingyao Ai and co-authors for "Scaling Laws for Dense Retrieval," and Laura Dietz for her paper, "A Workbench for Autograding Retrieve/Generate Systems."

## Best Paper Runner-Up Award

The Best Paper Runner-up award was won by CNR-ISTI for the paper "Efficient Inverted Indexes for Approximate Retrieval over Learned Sparse Representations" by Sebastian Bruch, Franco Maria Nardini, Cosimo Rulli, and Rossano Venturini.

## Best Paper Honorable Mentions

Researchers including Xu Chen, Wang Wenjie, Pang Liang, and Chua Tat-Seng received a Best Paper Honorable Mention for their paper titled "A Taxation Perspective for Fair Re-ranking."

The conference was held in Washington D.C., from 14 to 18 July 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ee86dfa-0dcf-487d-9b5a-23b05d7043cf",
  "isSidechain": true,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "agentId": "a68e4306d3984469c",
  "type": "user",
  "uuid": "5672c22e-dc1f-4d0c-b4f7-426d132cb76f",
  "sourceToolAssistantUUID": "2ee86dfa-0dcf-487d-9b5a-23b05d7043cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-30T06:21:38.450Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RWiZnsR5fkgwc9d2aRj8JB`</summary>

```json
{
  "url": "https://sigir-2024.github.io/best_papers.html",
  "prompt": "List all best paper awards given at SIGIR 2024. Include the full paper titles, authors, and award categories (Best Paper, Runner-Up, Honorable Mention, etc.)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5672c22e-dc1f-4d0c-b4f7-426d132cb76f",
  "isSidechain": true,
  "agentId": "a68e4306d3984469c",
  "requestId": "req_011CbYGgF7FogPvo4hKZJtrG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3235dcd0-e7cd-443d-ac37-3e6e3f0acfbb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CGzHSdaFGXfvi9qqks6uXr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 1531,
      "cache_read_input_tokens": 12251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1531,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 20 · 2026-05-30T06:21:38.954Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LKc5tFQLxyHTiAjBufZM94`</summary>

```json
{
  "query": "\"Scaling Laws for Dense Retrieval\" review discussion analysis contrastive entropy power law"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3235dcd0-e7cd-443d-ac37-3e6e3f0acfbb",
  "isSidechain": true,
  "agentId": "a68e4306d3984469c",
  "requestId": "req_011CbYGgF7FogPvo4hKZJtrG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb71b79d-0468-459e-aa81-223c04d0200c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CGzHSdaFGXfvi9qqks6uXr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 1531,
      "cache_read_input_tokens": 12251,
      "output_tokens": 179,
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
          "input_tokens": 85,
          "output_tokens": 179,
          "cache_read_input_tokens": 12251,
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

_source line 21 · 2026-05-30T06:21:43.583Z_

<details><summary>↩ Tool result · `toolu_01RWiZnsR5fkgwc9d2aRj8JB`</summary>

```text
# SIGIR 2024 Best Paper Awards

## Best Long Papers

**Best Papers:**
1. "Scaling Laws For Dense Retrieval" – Yan Fang, Jingtao Zhan, Qingyao Ai, Jiaxin Mao, Weihang Su, Jia Chen, Yiqun Liu

2. "A Workbench for Autograding Retrieve/Generate Systems" – Laura Dietz

**Runner-ups:**
1. "Efficient Inverted Indexes for Approximate Retrieval over Learned Sparse Representations" – Sebastian Bruch, Franco Maria Nardini, Cosimo Rulli, Rossano Venturini

2. "A Reproducibility Study of PLAID" – Sean MacAvaney, Nicola Tonellotto

**Honorable Mentions:**
1. "Generative Retrieval as Multi-Vector Dense Retrieval" – Shiguang Wu, Wenda Wei, Mengqi Zhang, Zhumin Chen, Jun Ma, Zhaochun Ren, Maarten de Rijke, Pengjie Ren

2. "Leveraging LLMs for Unsupervised Dense Retriever Ranking" – Ekaterina Khramtsova, Shengyao Zhuang, Mahsa Baktashmotlagh, Guido Zuccon

3. "LDRE: LLM-based Divergent Reasoning and Ensemble for Zero-Shot Composed Image Retrieval" – Zhenyu Yang, Dizhan Xue, Shengsheng Qian, Weiming Dong, Changsheng Xu

4. "Pacer and Runner: Cooperative Learning Framework between Single- and Cross-Domain Sequential Recommendation" – Chung Park, Taesan Kim, Hyungjun Yoon, Junui Hong, Yelim Yu, Mincheol Cho, Minsung Choi, Jaegul Choo

5. "A Taxation Perspective for Fair Re-ranking" – Chen Xu, Xiaopeng Ye, Wang Wenjie, Liang Pang, Jun Xu, Tat-Seng Chua

## Best Short Papers

**Best Paper:**
"Evaluating Retrieval Quality in Retrieval-Augmented Generation" – Alireza Salemi, Hamed Zamani

**Honorable Mentions:**
1. "Towards Robust QA Evaluation via Open LLMs" – Ehsan Kamalloo, Shivani Upadhyay, Jimmy Lin

2. "MeMemo: On-device Retrieval Augmentation for Private and Personalized Text Generation" – Zijie J. Wang, Duen Horng Chau
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3235dcd0-e7cd-443d-ac37-3e6e3f0acfbb",
  "isSidechain": true,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "agentId": "a68e4306d3984469c",
  "type": "user",
  "uuid": "18c07c62-75d6-492b-aee8-80848102188b",
  "sourceToolAssistantUUID": "3235dcd0-e7cd-443d-ac37-3e6e3f0acfbb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-30T06:21:51.997Z_

<details><summary>↩ Tool result · `toolu_01LKc5tFQLxyHTiAjBufZM94`</summary>

```text
Web search results for query: ""Scaling Laws for Dense Retrieval" review discussion analysis contrastive entropy power law"

Links: [{"title":"[Literature Review] Scaling Laws For Dense Retrieval","url":"https://www.themoonlight.io/en/review/scaling-laws-for-dense-retrieval"},{"title":"Scaling Laws for Dense Retrieval","url":"https://www.emergentmind.com/papers/2403.18684"},{"title":"Scaling Laws For Dense Retrieval","url":"https://arxiv.org/html/2403.18684v1"},{"title":"Scaling Laws For Dense Retrieval Yan Fang∗ Jingtao Zhan∗","url":"https://openreview.net/pdf?id=zWOlnUzEjK"},{"title":"Scaling Laws For Dense Retrieval | OpenReview","url":"https://openreview.net/forum?id=pC695J6QQd"},{"title":"Scaling Laws For Dense Retrieval | Request PDF","url":"https://www.researchgate.net/publication/382186952_Scaling_Laws_For_Dense_Retrieval"},{"title":"On the Scaling of Robustness and Effectiveness in Dense Retrieval","url":"https://arxiv.org/html/2505.24279"},{"title":"Scaling Laws For Dense Retrieval | Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/10.1145/3626772.3657743"},{"title":"[2403.18684] Scaling Laws For Dense Retrieval","url":"https://arxiv.org/abs/2403.18684"}]

Based on the web search results, I can provide you with a comprehensive overview of the "Scaling Laws for Dense Retrieval" paper:

## Overview

The paper delves into the scaling laws for dense retrieval models, examining how performance scales with model size, training data size, and annotation quality. The research is motivated by the observation that while scaling laws have been extensively studied in language modeling, their application to dense retrieval remains largely unexplored, with the paper aiming to fill this gap by conducting a systematic investigation of these scaling effects.

## Key Findings

### Power-Law Scaling
The paper finds that the performance of dense retrieval models follows a power-law scaling relationship with both model size and the amount of training data, meaning that increasing either model size or data size leads to predictable improvements in performance.

### Contrastive Entropy as Evaluation Metric
The researchers propose to use the contrastive entropy as the evaluation metric, which is continuous compared with discrete ranking metrics and thus can accurately reflect model performance.

## Experimental Approach

To disentangle the effects of model size and data size in dense retrieval, the researchers conducted experiments with models implemented with different pre-trained language models with non-embedding parameter sizes ranging from 0.5 to 87 million, on two of the largest web search datasets, i.e., MSMARCO and T2Ranking.

## Practical Applications

The scaling laws help optimize the training process, such as resolving the resource allocation problem under a budget constraint.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb71b79d-0468-459e-aa81-223c04d0200c",
  "isSidechain": true,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "agentId": "a68e4306d3984469c",
  "type": "user",
  "uuid": "701f1e67-064c-44d0-9633-bfc5bf285068",
  "sourceToolAssistantUUID": "eb71b79d-0468-459e-aa81-223c04d0200c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-30T06:21:54.413Z_

Let me get the review discussions and additional technical details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "701f1e67-064c-44d0-9633-bfc5bf285068",
  "isSidechain": true,
  "agentId": "a68e4306d3984469c",
  "requestId": "req_011CbYGhXo8iPJAFowTcUADi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97f8ec84-7a20-438d-961d-db948644a4da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015TTLFu85QxtXzuwbnfnf3o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1752,
      "cache_read_input_tokens": 13782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1752,
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

_source line 24 · 2026-05-30T06:21:56.258Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WGJZoZubNhTe1bXYbkgrPz`</summary>

```json
{
  "url": "https://openreview.net/forum?id=pC695J6QQd",
  "prompt": "Extract all reviewer comments, scores, and discussions about the paper \"Scaling Laws for Dense Retrieval\". Include reviewer ratings, strengths and weaknesses identified, key criticisms, and author responses if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97f8ec84-7a20-438d-961d-db948644a4da",
  "isSidechain": true,
  "agentId": "a68e4306d3984469c",
  "requestId": "req_011CbYGhXo8iPJAFowTcUADi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e70d979d-7d33-4bcc-860a-caf190e56b0d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015TTLFu85QxtXzuwbnfnf3o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1752,
      "cache_read_input_tokens": 13782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1752,
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

_source line 25 · 2026-05-30T06:21:57.190Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NP938np1WBdG3k3xcqXGed`</summary>

```json
{
  "url": "https://www.emergentmind.com/papers/2403.18684",
  "prompt": "Extract all analysis, discussion, and commentary about the paper \"Scaling Laws for Dense Retrieval\". Include any community reactions, key takeaways highlighted, and technical analysis provided."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e70d979d-7d33-4bcc-860a-caf190e56b0d",
  "isSidechain": true,
  "agentId": "a68e4306d3984469c",
  "requestId": "req_011CbYGhXo8iPJAFowTcUADi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71f31393-02a5-42ad-b8ad-d0a6a64c457d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015TTLFu85QxtXzuwbnfnf3o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1752,
      "cache_read_input_tokens": 13782,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1752
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 13782,
          "cache_creation_input_tokens": 1752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1752,
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

_source line 26 · 2026-05-30T06:21:59.125Z_

<details><summary>↩ Tool result · `toolu_01WGJZoZubNhTe1bXYbkgrPz`</summary>

```text
# Reviewer Comments and Discussion Analysis

Based on the provided web page content, **no reviewer comments, scores, discussions, strengths, weaknesses, or author responses are available**. 

The page displays only:
- Paper title and metadata
- Author list
- Publication venue (SIGIR 2024)
- Abstract summarizing the research on scaling laws in dense retrieval models
- Navigation and footer elements

To access detailed peer review information, you would need to navigate to the full review section of the OpenReview page, which is not included in the content provided. The page indicates there is a "[Revisions](/revisions?id=pC695J6QQd)" link that might contain additional discussion materials, but that content was not extracted here.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e70d979d-7d33-4bcc-860a-caf190e56b0d",
  "isSidechain": true,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "agentId": "a68e4306d3984469c",
  "type": "user",
  "uuid": "905a817c-13da-4550-be0a-dd7006b4e5b3",
  "sourceToolAssistantUUID": "e70d979d-7d33-4bcc-860a-caf190e56b0d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-30T06:22:02.664Z_

<details><summary>↩ Tool result · `toolu_01NP938np1WBdG3k3xcqXGed`</summary>

```text
# Analysis of "Scaling Laws for Dense Retrieval"

## Key Technical Contributions

The paper introduces **contrastive log-likelihood as an evaluation metric**, bridging the gap between continuous scaling laws and discrete retrieval metrics. This methodological innovation allows researchers to apply scaling law frameworks traditionally used in language models to dense retrieval systems.

## Primary Findings

The research demonstrates that dense retrieval performance follows **"a precise power-law scaling related to the model size and the number of annotations."** This discovery parallels scaling behavior observed in other neural architectures, establishing predictable performance relationships.

## Scaling Dimensions Analyzed

**Model Size Effects:** Larger models show improved retrieval capabilities with diminishing returns, revealing clear scaling patterns in performance gains.

**Training Data Volume:** Additional annotated data consistently enhances performance, though improvements plateau progressively—a critical insight for resource planning.

**Annotation Quality:** The study reveals that **"higher-quality annotations yielding steeper improvements in model performance"** suggests prioritizing data quality over quantity in annotation strategies.

## Practical Implications

The findings enable **"optimal resource allocation under budget constraints,"** allowing organizations to make informed decisions about computational investment and annotation strategies in dense retrieval systems.

## Community Engagement

The paper generated modest discussion, with 7 Reddit mentions and 124 social media engagements, indicating specialized audience interest rather than mainstream adoption of these findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71f31393-02a5-42ad-b8ad-d0a6a64c457d",
  "isSidechain": true,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "agentId": "a68e4306d3984469c",
  "type": "user",
  "uuid": "350c76db-b53c-4716-bd92-4f1a6226eb14",
  "sourceToolAssistantUUID": "71f31393-02a5-42ad-b8ad-d0a6a64c457d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-30T06:22:05.882Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01426wLw7Lz6rRr53WpJvLvy`</summary>

```json
{
  "url": "https://www.themoonlight.io/en/review/scaling-laws-for-dense-retrieval",
  "prompt": "Extract the full literature review and analysis of the paper \"Scaling Laws for Dense Retrieval\". Include all technical details discussed, any critiques, and the reviewer's assessment of strengths and weaknesses."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "350c76db-b53c-4716-bd92-4f1a6226eb14",
  "isSidechain": true,
  "agentId": "a68e4306d3984469c",
  "requestId": "req_011CbYGiKUFRg65ZpydxtvPq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35ca0bbf-990c-463b-b06a-623f8f44f110",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q2yiUpaMTkwCViKKtK5MyL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 772,
      "cache_read_input_tokens": 15534,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 772
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 133,
          "cache_read_input_tokens": 15534,
          "cache_creation_input_tokens": 772,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 772,
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

_source line 29 · 2026-05-30T06:22:11.420Z_

<details><summary>↩ Tool result · `toolu_01426wLw7Lz6rRr53WpJvLvy`</summary>

```text
# Analysis of "Scaling Laws for Dense Retrieval"

## Overview
This research investigates how dense retrieval model performance scales with model size, training data volume, and annotation quality—an area previously underexplored compared to language modeling scaling studies.

## Methodology Summary

**Model Architecture:**
The study employs Transformer-based models (BERT, ERNIE) with added projection layers mapping embeddings to 768 dimensions. Relevance scoring uses inner products: "s(q, p) = ⟨f(q; θ), f(p; θ)⟩" between query and passage encoders.

**Training Approach:**
Models undergo fine-tuning using contrastive ranking loss with random and in-batch negative sampling across two datasets (MSMARCO Passage Ranking and T2Ranking).

**Evaluation Innovation:**
Rather than traditional ranking metrics, the authors propose "contrastive entropy as the primary evaluation metric" to enable precise scaling observations.

## Key Findings

- **Power-Law Relationships:** Performance follows predictable scaling curves with both model and data size, expressed as L(N) = (A/N)^α + δ(N) for model scaling
- **Annotation Quality Effects:** Higher-quality annotations produce improved performance with varying scaling slopes
- **Practical Application:** Scaling laws enable budget-constrained resource allocation optimization

## Assessment

**Strengths:** Systematic investigation of previously unexplored scaling dynamics; introduces continuous metrics enabling precise measurement

**Limitations:** The content provided lacks explicit discussion of weaknesses, alternative approaches, or comparative analyses against baseline methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35ca0bbf-990c-463b-b06a-623f8f44f110",
  "isSidechain": true,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "agentId": "a68e4306d3984469c",
  "type": "user",
  "uuid": "4b754d62-64ef-4b2d-9710-77d872c97bf1",
  "sourceToolAssistantUUID": "35ca0bbf-990c-463b-b06a-623f8f44f110",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-30T06:22:22.213Z_

Now let me get more details about the specific model architectures and the data augmentation analysis from the HTML version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b754d62-64ef-4b2d-9710-77d872c97bf1",
  "isSidechain": true,
  "agentId": "a68e4306d3984469c",
  "requestId": "req_011CbYGixqJU2DY5X3aGQEeB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "969bea2d-2f7b-4298-9e12-4c97b361e530",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012LbrvixW8NLbcEpUwcHYS8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 499,
      "cache_read_input_tokens": 16306,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 499,
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

_source line 31 · 2026-05-30T06:22:28.444Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014XYU7XpsgYNfaJ8nb3iQ9e`</summary>

```json
{
  "url": "https://arxiv.org/html/2403.18684",
  "prompt": "Focus specifically on these sections and extract ALL numerical details:\n1. Section on data augmentation / annotation quality: What three methods did they test? What were the exact scaling coefficients for each method? How did ChatGLM3-generated data compare to human annotations?\n2. The budget allocation / resource allocation section: What is the exact cost model formula? What were the specific cost parameters they used? What were the optimal model sizes at different budgets?\n3. The emergent ability threshold: At what contrastive entropy value does performance sharply improve? What is the relationship between contrastive entropy and NDCG/MAP?\n4. Any discussion of limitations or the irreducible loss term delta\n5. The exact BERT model variants used and their parameter counts\n6. Any validation results: R-squared values for the power law fits, prediction accuracy when extrapolating from small to large models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "969bea2d-2f7b-4298-9e12-4c97b361e530",
  "isSidechain": true,
  "agentId": "a68e4306d3984469c",
  "requestId": "req_011CbYGixqJU2DY5X3aGQEeB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92be89c5-4a60-43cd-84b8-f7c38bd9266d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012LbrvixW8NLbcEpUwcHYS8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 499,
      "cache_read_input_tokens": 16306,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 499,
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

_source line 32 · 2026-05-30T06:22:38.544Z_

<details><summary>↩ Tool result · `toolu_014XYU7XpsgYNfaJ8nb3iQ9e`</summary>

```text
# Scaling Laws for Dense Retrieval: Key Numerical Details

## Annotation Quality Methods & Results

Three annotation approaches were tested:
- **Inverse Cloze Task (ICT)**: Low-quality, sentence-based pseudo-queries
- **DocT5query**: Medium-quality, supervised generation model
- **ChatGLM3**: Higher-quality LLM-based generation

The paper states ChatGLM3 annotations "surpass human annotations at 500k" data points, though human-annotated data consistently outperformed all synthetic methods across smaller datasets. No specific scaling coefficients were provided per method; instead, Figure 5 demonstrated "power-law scaling across different annotation methods."

## Budget Allocation Cost Model

Formula: Z(N,D) = Z_data·D + Z_train·N + Z_infer·N

Specific parameters used:
- **Z_data**: $0.6 per query-passage pair
- **Z_train**: 3.22×10⁻⁸ (computational cost)
- **Z_infer**: 0.43 (computational cost)

Optimal model sizes varied dramatically:
- **Excluding inference costs** ($20,000 budget): 13 billion parameters optimal
- **Including inference costs** ($20,000 budget): "million-scale parameters" optimal due to "prohibitively high" inference expenses

## Emergent Ability Threshold

Performance exhibits "emergent ranking ability" at approximately **0.25 contrastive entropy**, where "ranking metrics substantially improve." Strong positive linear correlation exists between contrastive entropy and traditional metrics (MAP@10, NDCG@10, Recall@1000).

## Irreducible Loss Term (δ)

The model incorporates an irreducible loss because "some relevant passages may not be annotated" and "relevance may be subjective to different annotators," preventing perfect agreement with human judgments.

## BERT Model Variants

Models ranged from **0.5 million** (BERT-Tiny) to **82 million non-embedding parameters** (BERT-Base). The study used "24 BERT checkpoints from the original Google release" with varying architectures.

## Validation Results

**R² values for power law fits:**
- MSMARCO model size scaling: **0.991**
- T2Ranking model size scaling: **0.999**
- MSMARCO data size scaling: **0.954**
- T2Ranking data size scaling: **0.991**

The paper demonstrated prediction accuracy through Figure 6, where "predictions relatively are close to the real values" when extrapolating combined model-data effects.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92be89c5-4a60-43cd-84b8-f7c38bd9266d",
  "isSidechain": true,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "agentId": "a68e4306d3984469c",
  "type": "user",
  "uuid": "d6137209-e9a8-4953-99fc-58f7916a744a",
  "sourceToolAssistantUUID": "92be89c5-4a60-43cd-84b8-f7c38bd9266d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-30T06:23:38.743Z_

I now have comprehensive information. Here is the thorough research summary:

---

## "Scaling Laws for Dense Retrieval" -- Full Technical Summary

**Paper:** arXiv 2403.18684 (v2, July 15, 2024)
**Authors:** Yan Fang, Jingtao Zhan, Qingyao Ai, Jiaxin Mao, Weihang Su, Jia Chen, Yiqun Liu (Tsinghua University / Renmin University of China)
**Venue:** SIGIR 2024 (47th International ACM SIGIR Conference, Washington DC, July 14-18, 2024) -- **Best Long Paper Award** (co-winner with "A Workbench for Autograding Retrieve/Generate Systems" by Laura Dietz)

---

### 1. Problem / Gap Identified

While scaling laws have been extensively studied for language modeling (e.g., Kaplan et al., Chinchilla), they remained **entirely unexplored for dense retrieval**. Two specific challenges blocked progress:

- **Discrete metrics problem:** Traditional ranking metrics like NDCG and MAP are discrete and cannot smoothly reflect fine-grained performance changes, making it impossible to fit continuous power-law curves.
- **Entangled factors:** Dense retrieval performance depends on multiple interrelated factors -- model size, annotation quantity, and annotation quality -- making it difficult to isolate individual effects and derive clean scaling relationships.

---

### 2. Key Methodological Innovation: Contrastive Entropy

The authors introduced **contrastive entropy** (equivalently, contrastive log-likelihood) as a continuous evaluation metric for dense retrieval:

```
CE = -log( exp(s(q_i, p_i^+; theta)) / (exp(s(q_i, p_i^+; theta)) + sum_j exp(s(q_i, p_j^-; theta))) )
```

where `s(q, p) = &lt;f(q; theta), f(p; theta)>` is the inner product between query and passage embeddings. This metric mirrors the contrastive training loss and measures the likelihood of retrieving a relevant document from a randomly sampled candidate set.

**Crucially**, the authors demonstrated a strong positive linear correlation between contrastive entropy and traditional ranking metrics (NDCG@10, MAP@10, Recall@1000), validating it as a faithful proxy. They also observed an **emergent ability threshold** around contrastive entropy of approximately **0.25**, below which ranking performance sharply improves -- analogous to emergent abilities in large language models.

---

### 3. Scaling Law Formulations

The authors derived three power-law relationships:

**Model size scaling (fixed data):**
```
L(N) = (A / N)^alpha + delta_N
```

**Data size scaling (fixed model):**
```
L(D) = (B / D)^beta + delta_D
```

**Joint model-data scaling:**
```
L(N, D) = [(A / N)^(alpha/beta) + B / D]^beta + delta
```

Where:
- `N` = number of non-embedding model parameters
- `D` = number of annotated query-passage training pairs
- `L` = contrastive entropy (lower is better)
- `A, B` = scaling coefficients
- `alpha, beta` = scaling exponents
- `delta` = irreducible loss term (accounts for incomplete annotations and subjective relevance)

---

### 4. Fitted Coefficients and R-squared Values

**MS MARCO Passage Ranking:**
| Scaling | A | alpha | delta | R-squared |
|---------|---|-------|-------|-----------|
| Model size | 3.22 x 10^4 | 0.53 | 0.04 | 0.991 |
| Data size | 3.49 x 10^3 | 1.05 | 0.05 | 0.954 |

**T2Ranking (Chinese):**
| Scaling | A | alpha | delta | R-squared |
|---------|---|-------|-------|-----------|
| Model size | 9.89 x 10^6 | 0.53 | 0.14 | 0.999 |
| Data size | 6.04 x 10^4 | 0.50 | 0.15 | 0.991 |

**Joint scaling (MS MARCO):** A ~ 3.6 x 10^4, B ~ 7.1 x 10^3, alpha ~ 0.56, beta ~ 1.31, delta ~ 0.03

Notable: The model size exponent alpha = 0.53 is **consistent across both datasets** (MS MARCO and T2Ranking), suggesting a universal scaling relationship for model size in dense retrieval. The data exponents differ more (1.05 vs 0.50), reflecting dataset-specific annotation characteristics.

---

### 5. Experimental Setup

**Models:** 24 BERT checkpoints from Google's original release, ranging from BERT-Tiny (0.5M non-embedding parameters) to BERT-Base (82M non-embedding parameters). For Chinese experiments, ERNIE model variants were used.

**Architecture:** Transformer-based dual encoders with a projection layer mapping to 768-dimensional embeddings. Relevance scored via inner product between query and passage embeddings.

**Datasets:**
- **MS MARCO Passage Ranking:** ~0.5M training queries, 8.8M passages (English web search)
- **T2Ranking:** 300k+ queries, 2M+ unique passages (Chinese web search)

**Training protocol:** Fixed at 10,000 steps, batch size 256, random negative sampling with 256 negatives per step, contrastive ranking loss.

---

### 6. Data Augmentation / Annotation Quality Analysis

Three synthetic annotation methods were tested alongside human annotations:

1. **Inverse Cloze Task (ICT):** Lowest quality -- uses random sentences from passages as pseudo-queries
2. **DocT5query:** Medium quality -- a supervised T5 model trained on human annotations to generate queries
3. **ChatGLM3:** Zero-shot LLM-based generation -- higher per-sample diversity

**Key finding:** All methods followed power-law scaling, but with different slopes (higher quality = steeper improvement curve). ChatGLM3-generated annotations **surpassed human annotations when scaled to 500k+ pairs**, despite lower per-sample quality. This suggests that for large-scale annotation, LLM-generated data can be more cost-effective than human labeling, leveraging the power of scaling.

---

### 7. Budget Allocation and Practical Implications

The authors formulated a total lifecycle cost model:

```
Z(N, D) = Z_data * D + Z_train * N + Z_infer * N
```

With cost parameters:
- **Z_data** = $0.60 per annotated query-passage pair
- **Z_train** = 3.22 x 10^-8 (training compute cost per parameter)
- **Z_infer** = 0.43 (inference compute cost per parameter)

**Critical insight -- inference cost dominance:** The ratio Z_infer / Z_train is enormous (~10^7), meaning inference costs dwarf training costs for dense retrieval (unlike language modeling where training dominates).

**Optimal allocation results for a $20,000 budget:**
- **Excluding inference costs:** Optimal model size is ~13 billion parameters, with budget favoring larger models and less data annotation
- **Including inference costs:** Optimal model shrinks dramatically to **million-scale parameters** because inference cost is proportional to model size and dominates the budget

This leads to a fundamentally different recommendation than LLM scaling: **for dense retrieval, practitioners should favor smaller, more efficient models** because retrieval requires encoding the entire corpus at inference time, making per-parameter inference cost the binding constraint.

---

### 8. The Irreducible Loss Term (delta)

The delta term captures a performance floor that cannot be overcome regardless of model or data scaling. It exists because:
- Some relevant passages are never annotated in the training data
- Relevance judgments are inherently subjective across annotators
- No finite model can achieve perfect retrieval from incomplete labels

Delta values were consistently small but non-zero: 0.03-0.05 for MS MARCO, 0.14-0.15 for T2Ranking (reflecting T2Ranking's noisier annotation process).

---

### 9. Predictive Power and Practical Use

The scaling laws enable:
1. **Performance extrapolation:** Train small models cheaply and predict large-model performance without actually training them
2. **Annotation budgeting:** Estimate how many annotations are needed to reach a target performance level
3. **Compute-optimal allocation:** Given a fixed budget, determine the best split between model size, training data, and inference resources
4. **Method comparison:** Different annotation strategies can be compared by their scaling coefficients rather than single-point evaluations

The joint scaling law predictions were validated against real experiments, with predictions "relatively close to real values" when extrapolating from smaller configurations.

---

### 10. SIGIR 2024 Best Paper Recognition

The paper was one of **two co-winners of the SIGIR 2024 Best Long Paper Award**. The other best paper awards at SIGIR 2024 included:
- **Runner-ups:** "Efficient Inverted Indexes for Approximate Retrieval over Learned Sparse Representations" (Bruch et al.) and "A Reproducibility Study of PLAID" (MacAvaney & Tonellotto)
- **Honorable mentions** included five additional papers on topics ranging from generative retrieval to fair re-ranking

---

### Summary of the Paper's Core Contribution

This paper establishes that dense retrieval follows precise, predictable power-law scaling with respect to both model size and training data quantity -- a finding that parallels the famous neural scaling laws for language models but reveals a critical difference: because dense retrieval requires encoding entire corpora at inference time, the inference cost (not training cost) becomes the dominant budget constraint. This inverts the conventional "bigger is better" wisdom from language modeling and suggests that for practical dense retrieval, compute budgets should favor smaller models with more training data, with the exact optimal tradeoff calculable from the discovered scaling laws.

---

Sources:
- [arXiv Abstract Page](https://arxiv.org/abs/2403.18684)
- [arXiv HTML Full Paper](https://arxiv.org/html/2403.18684)
- [SIGIR 2024 Best Papers Page](https://sigir-2024.github.io/best_papers.html)
- [ACM Digital Library Entry](https://dl.acm.org/doi/abs/10.1145/3626772.3657743)
- [EmergentMind Analysis](https://www.emergentmind.com/papers/2403.18684)
- [Moonlight Literature Review](https://www.themoonlight.io/en/review/scaling-laws-for-dense-retrieval)
- [OpenReview Page](https://openreview.net/forum?id=pC695J6QQd)
- [SIGIR Best Paper Awards History](https://sigir.org/awards/best-paper-awards/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6137209-e9a8-4953-99fc-58f7916a744a",
  "isSidechain": true,
  "agentId": "a68e4306d3984469c",
  "requestId": "req_011CbYGky5jdxhFeEmQMwzxM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebf1cf94-ec68-4fc2-97a4-b57bf8994fd3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KKqAyZrpe3eBQFZUWSsFnz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 913,
      "cache_read_input_tokens": 16805,
      "output_tokens": 2686,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 913
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2686,
          "cache_read_input_tokens": 16805,
          "cache_creation_input_tokens": 913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 913,
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
