# Research conversation: Research the paper "Towards Poisoning Robustness Certification for Natural Language Generation" by Mihnea Ghitu, Matthew

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a8858d54dfffc89c6.jsonl`
- **Structured JSON:** [`3dedac400fe33369f2ad.json`](../../sessions/3d/3dedac400fe33369f2ad.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

33 recorded events

### User

_source line 1 · 2026-05-30T06:33:49.544Z_

Research the paper "Towards Poisoning Robustness Certification for Natural Language Generation" by Mihnea Ghitu, Matthew Wicker (arXiv 2026). URL: https://arxiv.org/abs/2602.09757

Tasks:
1. Use WebFetch to read the arxiv abstract page
2. Use WebFetch to read the full PDF or HTML version if available
3. Search the web for any discussions or reviews of this paper

Report back with:
- The full abstract
- Key method details: what is Targeted Partition Aggregation (TPA), how they certify NLG validity against poisoning, how they compute minimum poisoning budgets, what validity functions they use
- The theoretical guarantees
- How it relates to RobustRAG
- Limitations acknowledged

Be thorough — I need enough detail to write a precise technical analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "a8858d54dfffc89c6",
  "type": "user",
  "uuid": "ee4c1469-1dce-4fd4-b7d5-516f7f801020",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-30T06:33:49.547Z_

```json
{
  "parentUuid": "ee4c1469-1dce-4fd4-b7d5-516f7f801020",
  "isSidechain": true,
  "agentId": "a8858d54dfffc89c6",
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
  "uuid": "73ede1f1-8552-49b2-b192-6465a08ba03a",
  "timestamp": "2026-05-30T06:33:49.547Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-30T06:33:49.548Z_

```json
{
  "parentUuid": "73ede1f1-8552-49b2-b192-6465a08ba03a",
  "isSidechain": true,
  "agentId": "a8858d54dfffc89c6",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "335b6939-4af9-4ba1-85d5-e9b4758c2150",
  "timestamp": "2026-05-30T06:33:49.548Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-30T06:33:52.791Z_



I'll start by fetching the tools I need, then gather information about this paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "335b6939-4af9-4ba1-85d5-e9b4758c2150",
  "isSidechain": true,
  "agentId": "a8858d54dfffc89c6",
  "requestId": "req_011CbYHcRfGXk4YC6A7Uc3M5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b9131f1-2436-405a-a7f1-d5d402f67b5e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LqCdJD96WiX7asgXniQLJV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1540,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1540,
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

_source line 5 · 2026-05-30T06:33:53.418Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HREDXj5wn7mw4G83xtN5Yz`</summary>

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
  "parentUuid": "4b9131f1-2436-405a-a7f1-d5d402f67b5e",
  "isSidechain": true,
  "agentId": "a8858d54dfffc89c6",
  "requestId": "req_011CbYHcRfGXk4YC6A7Uc3M5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "713319b5-1da7-43aa-a6c7-66e6ee14152d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LqCdJD96WiX7asgXniQLJV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1540,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1540,
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

_source line 6 · 2026-05-30T06:33:53.422Z_

<details><summary>↩ Tool result · `toolu_01HREDXj5wn7mw4G83xtN5Yz`</summary>

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
  "parentUuid": "713319b5-1da7-43aa-a6c7-66e6ee14152d",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "a8858d54dfffc89c6",
  "type": "user",
  "uuid": "2a9d4795-97c6-4391-9517-81988eed6140",
  "sourceToolAssistantUUID": "713319b5-1da7-43aa-a6c7-66e6ee14152d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-30T06:33:56.653Z_



Now let me fetch the arxiv abstract page, the full paper, and search for discussions in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a9d4795-97c6-4391-9517-81988eed6140",
  "isSidechain": true,
  "agentId": "a8858d54dfffc89c6",
  "requestId": "req_011CbYHcjqewL3x4JghGsZ2x",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5e9075c-7eed-43fe-ba74-98f27e0b33ed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Muo3VwcPdviaTF2H5nFT31",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 8953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1121,
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

_source line 8 · 2026-05-30T06:33:58.012Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M6zsGG3pvgSPqEx7GzY8M1`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.09757",
  "prompt": "Extract the complete abstract, all author names and affiliations, the full title, and any other metadata (submission date, categories, etc.) from this arxiv paper page. Provide everything verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5e9075c-7eed-43fe-ba74-98f27e0b33ed",
  "isSidechain": true,
  "agentId": "a8858d54dfffc89c6",
  "requestId": "req_011CbYHcjqewL3x4JghGsZ2x",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00237650-9408-414c-b1a4-d27ec1618d44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Muo3VwcPdviaTF2H5nFT31",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 8953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1121,
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

_source line 9 · 2026-05-30T06:34:04.182Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KuNv4bwS3RDSJhvqxdwRca`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.09757v1",
  "prompt": "Extract ALL technical details from this paper. I need:\n1. The full abstract\n2. Complete description of Targeted Partition Aggregation (TPA) - how it works, the algorithm, all steps\n3. How they certify NLG validity against poisoning attacks - the certification procedure\n4. How they compute minimum poisoning budgets\n5. What validity functions they use (exact definitions)\n6. All theoretical guarantees, theorems, propositions, and proofs (at least theorem statements)\n7. How this work relates to RobustRAG and other prior work\n8. Limitations acknowledged by the authors\n9. Experimental setup and results\n10. Any definitions of key terms like \"validity\", \"poisoning budget\", etc.\nBe as thorough and detailed as possible - extract equations, algorithm pseudocode, theorem statements verbatim if possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00237650-9408-414c-b1a4-d27ec1618d44",
  "isSidechain": true,
  "agentId": "a8858d54dfffc89c6",
  "requestId": "req_011CbYHcjqewL3x4JghGsZ2x",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54fdaa22-5b63-4aea-9cbf-ba36a5ec98ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Muo3VwcPdviaTF2H5nFT31",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 8953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1121,
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

_source line 10 · 2026-05-30T06:34:04.972Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VXrJLu6RHh1ZGsg1nvRU4S`</summary>

```json
{
  "query": "\"Towards Poisoning Robustness Certification for Natural Language Generation\" Ghitu Wicker 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54fdaa22-5b63-4aea-9cbf-ba36a5ec98ee",
  "isSidechain": true,
  "agentId": "a8858d54dfffc89c6",
  "requestId": "req_011CbYHcjqewL3x4JghGsZ2x",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aed88526-350b-4f82-96ac-992f49a367ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Muo3VwcPdviaTF2H5nFT31",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 8953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1121,
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

_source line 11 · 2026-05-30T06:34:05.301Z_

<details><summary>↩ Tool result · `toolu_01M6zsGG3pvgSPqEx7GzY8M1`</summary>

```text
# Paper Metadata Extraction

**Title:** "Towards Poisoning Robustness Certification for Natural Language Generation"

**Authors:** Mihnea Ghitu, Matthew Wicker

**Affiliations:** Not provided on this page

**Submission Date:** February 10, 2026

**arXiv Identifier:** 2602.09757

**Category:** Computer Science - Machine Learning (cs.LG)

**Abstract:** The paper addresses reliability of language generation systems by formalizing two security properties: stability and validity. It introduces Targeted Partition Aggregation (TPA), described as "the first algorithm to certify validity/targeted attacks by computing the minimum poisoning budget needed to induce a specific harmful class, token, or phrase." The authors extend TPA using mixed integer linear programming for multi-turn generations and demonstrate effectiveness in certifying agent tool-calling robustness and preference-based alignment.

**License:** Creative Commons Attribution 4.0 (CC BY 4.0)

**Available Formats:** PDF, HTML (experimental), TeX Source

**Note:** Author affiliations are not displayed on this arxiv abstract page, though email contact information is available through a contact option.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00237650-9408-414c-b1a4-d27ec1618d44",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "a8858d54dfffc89c6",
  "type": "user",
  "uuid": "4a16951a-b2c4-44e7-8c13-2f024644d7f5",
  "sourceToolAssistantUUID": "00237650-9408-414c-b1a4-d27ec1618d44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-30T06:34:10.908Z_

<details><summary>↩ Tool result · `toolu_01VXrJLu6RHh1ZGsg1nvRU4S`</summary>

```text
Web search results for query: ""Towards Poisoning Robustness Certification for Natural Language Generation" Ghitu Wicker 2026"

Links: [{"title":"Towards Poisoning Robustness Certification for Natural Language Generation","url":"https://arxiv.org/pdf/2602.09757"},{"title":"[2602.09757] Towards Poisoning Robustness Certification for Natural Language Generation","url":"https://arxiv.org/abs/2602.09757"},{"title":"Towards Poisoning Robustness Certification for Natural Language Generation","url":"https://arxiv.org/html/2602.09757"},{"title":"Certifying Language Model Robustness with Fuzzed Randomized Smoothing:   An Efficient Defense Against Backdoor Attacks","url":"https://arxiv.org/pdf/2502.06892"},{"title":"Certified Robustness to Data Poisoning in Gradient-Based Training","url":"https://arxiv.org/pdf/2406.05670"}]

I found the paper! Here are the details about "Towards Poisoning Robustness Certification for Natural Language Generation":

**Paper Details:**
- Authors: Mihnea Ghitu and Matthew Wicker
- Published: February 11, 2026
- Available at: https://arxiv.org/abs/2602.09757

**Overview:**
The paper addresses how certified poisoning defenses are ill-equipped for autoregressive generation since they cannot handle sequential predictions or the exponentially large output space of language models.

**Key Contributions:**
- The authors formalize two security properties: stability (robustness to any change in generation) and validity (robustness to targeted, harmful changes in generation).
- They introduce Targeted Partition Aggregation (TPA), the first algorithm to certify validity/targeted attacks by computing the minimum poisoning budget needed to induce a specific harmful class, token, or phrase.
- They extend TPA to provide tighter guarantees for multi-turn generations using mixed integer linear programming (MILP).

**Empirical Results:**
They demonstrate TPA's effectiveness across diverse settings including certifying validity of agent tool-calling when adversaries modify up to 0.5% of the dataset and certifying 8-token stability horizons in preference-based alignment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aed88526-350b-4f82-96ac-992f49a367ac",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "a8858d54dfffc89c6",
  "type": "user",
  "uuid": "84f62911-92d7-45f3-a1e9-6243154af76d",
  "sourceToolAssistantUUID": "aed88526-350b-4f82-96ac-992f49a367ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-30T06:34:33.423Z_

<details><summary>↩ Tool result · `toolu_01KuNv4bwS3RDSJhvqxdwRca`</summary>

````text
# Technical Details from "Towards Poisoning Robustness Certification for Natural Language Generation"

## 1. Abstract

The paper introduces a framework for certified natural language generation against training-time data poisoning. It distinguishes between **stability** (robustness to any output change) and **validity** (robustness to specific harmful outputs). The authors present Targeted Partition Aggregation (TPA), the first algorithm certifying validity by computing minimum poisoning budgets needed to induce harmful generations. They extend this to phrase-level and multi-turn settings using mixed integer linear programming, demonstrating effectiveness on agent tool-calling, preference alignment, and achieving >90% validity certification at k=9 poisoning budget with 20+ token horizons.

## 2. Targeted Partition Aggregation (TPA) Algorithm

**Algorithm 1: Core TPA Procedure**

```
Input: Token index i, vote counts V, target token t, v_t ← votes of token t
Let j ∈ {0,...,|V|-2} and s ∈ {1,...,|V|-1}
Δ[j] ← (V[j] - V[j+1])
Φ[s] ← v_t + Σ(ℓ=0 to s-1) Δ[ℓ]
s* ← min{s | Φ[s] > V[s] or s = |V|-1}
return r_i^t = Φ[s*-1] + ⌊((V_s* - Φ[s*-1] + 1) · s*) / (s*+1)⌋
```

**Core Concept**: TPA iteratively reallocates votes from top-ranked classes to a target harmful token *t* until achieving plurality. The algorithm tracks a cascading reduction where, at phase *s*, the top *s* classes are equalized and jointly reduced to the next vote level, with removed votes reassigned to *t*.

## 3. Validity and Stability Definitions

**Definition 4.1 (i-th token stability):**
For prompt *x*, the i-th token generation is *k*-stable if:
```
max_{D̃ ∈ B_k(D)} 𝕀(f(x)[i] ≠ f̃(x)[i]) = 0
```

The stability radius is the minimum *r* where there exists a poisoned dataset causing token change.

**Definition 4.2 (i-th token validity):**
Given harmful sentence s_h = {t_1,...,t_T}, generation is valid at *x* if:
```
max_{D̃ ∈ B_k(D)} 𝕀(f̃(x+{t_1,...,t_{i-1}})[0] = t_i) = 0
```

The validity radius is the minimum poisoning budget needed to make target token *t_i* the next generated token.

**Definition 4.4 (Finite-horizon validity & stability):**
```
r_{1:L}^⊛(x) = min_{i∈[L]} {r_i^⊛(x)}
```

where ⊛ = * for stability, ⊛ = t for validity.

## 4. Theoretical Guarantees

**Theorem 4.3** (Token-Level Validity Certificate):
The value r_i^t computed by Algorithm 1 is a sound lower bound on the i-th token validity radius. For poisoning budget k ≤ r_i^t, the adversary cannot make target token *t* the plurality prediction.

**Proof sketch**: The optimal attack strategy iteratively reallocates votes from top-ranked classes to *t* until achieving plurality. The algorithm tracks this cascading reduction, making it a tight lower bound under the worst-case assumption that adversaries can arbitrarily change any shard's output with a single data point modification.

**Proposition 4.5** (Sequential stability/validity certificate):
```
r_min(x;1:L) = min_{i∈{1,...,L}} r_i^⊛(x) ≤ r_{1:L}^⊛(x)
```

Any attack on the prefix requires at least r_min samples.

**Proposition 4.6** (Phrase-level certificate):
Phrase-level voting over m-token sequences maintains soundness. The algorithm remains valid when applied to the transformed problem space 𝒱^m.

## 5. Multi-Turn Collective Certification (MILP Formulation)

**Definition 4.7** (Collective TPA Certificate):

For *N* test prompts, global budget *K*, shards {𝒫_j} with base models f_j:

```
max_a (1/N)Σ(i=1 to N) 𝕀[τ_i ≤ Σ(j=1 to M) ψ_j^(i)]

subject to:
ψ_j^(i) = 𝕀{a_j ≥ R_j(x^(i))} · (1 + 𝕀{f_j(x^(i)) ∈ C_{s*}^(i)})
τ_i = (μ - v_t^(i)) + Σ(b=1 to s*)(v_b - μ)
μ = Φ[s*-1] + ((V_c[s*] - Φ[s*-1] + 1) · s*)/(s*+1)
R_j(x^(i)) = {K+1 if f_j(x^(i)) ≠ t^(i); 1 otherwise}
Σ(j=1 to M) a_j = K
```

**Theorem 4.8**: The solution 𝒜(K) guarantees at least ⌊N·𝒜(K)⌋ prompts maintain original predictions under budget *K*.

## 6. Threat Model

- **Adversary capabilities**: Unbounded, general poisoning of features, labels, or both
- **Perturbation constraint**: |D △ D̃| ≤ r (symmetric difference bounded)
- **Adversary knowledge**: White-box with access to architecture, dataset, training order, hyperparameters
- **Adversary goals**: 
  - Untargeted: maximize ℙ_x[f(x) ≠ f̃(x)]
  - Targeted: maximize ℙ_x[f̃(x) = y*]

## 7. Shard-and-Aggregate Framework

Training proceeds by:
1. Partitioning dataset D into S disjoint shards {D_s}
2. Training independent base models {f_s}
3. At test time, ensemble generates using majority voting

**Ensemble prediction**: F(x) = argmax_{y∈𝒴} V[y] where V[t] = count of votes for token t

**Robustness condition**: If V_1 - V_2 ≥ 2k + 1, prediction is certified robust to k dataset changes.

## 8. Evaluation Metrics

**First-Token Stability (FTS@k)**: Fraction of test prompts where first token remains unchanged under k-poisoning.

**First-Token Validity (FTV@k)**: Fraction where first token cannot be changed to target harmful token t_1.

**Stability Horizon (SH@k)**: Average length of longest certified stable prefix.

**Validity Horizon (VH@k)**: Average length before harmful sequence s_h can be induced.

**Certified Response Radius**: Number of dataset changes a response is certified against, regardless of length.

## 9. Experimental Results Summary

**Agent Tool-Calling (MCP)**:
- 500 shards on 50K Toucan dataset examples
- Full LoRA: median robustness r=249 (0.5% poisoning resistance)
- Accuracy: 67% (Full LoRA) vs 40% (zero-shot baseline)
- Latency: 150s (Full LoRA), reduced to 25s via Last-3 LoRA

**Preference Alignment (HH-RLHF)**:
- 20 shards across OLMo-1B, Gemma2-2B, Qwen1.5-4B
- DPA+ROE achieves 42%-54% FTS@k=9
- TPA+MSC maintains >90% FTV@k=9 with 21+ token horizons
- Stability Horizon varies 0.25-8.31 tokens depending on model and method

**Empirical Attack Robustness**:
- Ensemble defense reduces attack success from 40-48% to <6% against practical backdoor attacks
- Stealth scores remain >95% across configurations

## 10. Limitations Acknowledged

The authors explicitly note:
- Inference-time latency remains "an open challenge"
- "Certification framework addresses a specific threat model: training-time poisoning under worst-case assumptions"
- "Other important threat modes—such as test-time evasion, prompt-based attacks, and triggered backdoors—remain critical open challenges"
- Bounds are "inherently conservative" compared to empirical robustness
- Methods do not eliminate vulnerabilities from alternative attack surfaces

## 11. Key Distinctions from Prior Work

**vs. Deep Partition Aggregation (DPA)**: DPA cannot soundly handle autoregressive dependencies where changing token i affects distribution of subsequent tokens j>i.

**vs. RobustRAG**: This work addresses post-training data poisoning, while RobustRAG addresses inference-time retrieval corruption.

**vs. TextGuard & FCert**: Limited prior work directly certifies robustness in NLG; existing methods primarily address text classification or few-shot learning.

The core innovation is formalizing **validity as distinct from stability** for generation tasks and providing the first algorithms certifying resistance to targeted harmful outputs at scale.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54fdaa22-5b63-4aea-9cbf-ba36a5ec98ee",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "a8858d54dfffc89c6",
  "type": "user",
  "uuid": "79c551e5-c41f-42cd-81f2-342c66128c88",
  "sourceToolAssistantUUID": "54fdaa22-5b63-4aea-9cbf-ba36a5ec98ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-30T06:34:35.903Z_

Now let me search for any discussions, reviews, or follow-up work about this paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79c551e5-c41f-42cd-81f2-342c66128c88",
  "isSidechain": true,
  "agentId": "a8858d54dfffc89c6",
  "requestId": "req_011CbYHffHPvKQBCnZnTefZt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1cde33cc-3ae9-4ddb-85d6-b07cb151d6d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QNKYsYax99dNaXQ9kp6Y9S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 585,
      "cache_creation_input_tokens": 3202,
      "cache_read_input_tokens": 10074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3202,
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

_source line 15 · 2026-05-30T06:34:36.347Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UYRnkULv2YPpRwKnLsv5pM`</summary>

```json
{
  "query": "Targeted Partition Aggregation TPA poisoning certification NLG Ghitu Wicker discussion review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cde33cc-3ae9-4ddb-85d6-b07cb151d6d2",
  "isSidechain": true,
  "agentId": "a8858d54dfffc89c6",
  "requestId": "req_011CbYHffHPvKQBCnZnTefZt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc53896e-64b5-4e2d-aad1-231bb0095ea8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QNKYsYax99dNaXQ9kp6Y9S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 585,
      "cache_creation_input_tokens": 3202,
      "cache_read_input_tokens": 10074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3202,
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

_source line 16 · 2026-05-30T06:34:36.876Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013rNivXt3ZiYUBS55Uerg9D`</summary>

```json
{
  "query": "\"Targeted Partition Aggregation\" poisoning robustness natural language generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc53896e-64b5-4e2d-aad1-231bb0095ea8",
  "isSidechain": true,
  "agentId": "a8858d54dfffc89c6",
  "requestId": "req_011CbYHffHPvKQBCnZnTefZt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ad2d0a1-c0d9-4278-8ae7-e5944cb16244",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QNKYsYax99dNaXQ9kp6Y9S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 585,
      "cache_creation_input_tokens": 3202,
      "cache_read_input_tokens": 10074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3202,
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

_source line 17 · 2026-05-30T06:34:41.744Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Bn2gbtYZVyHTB7sdotSQtR`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2602.09757",
  "prompt": "Extract ALL additional details not covered in the HTML version, focusing on:\n1. The exact relationship to RobustRAG - what do the authors say about it specifically?\n2. Any additional theorems, lemmas, or proofs in the appendix\n3. The exact validity functions used - how they define them precisely\n4. The phrase-level certification details\n5. Any ablation studies or additional experiments\n6. The exact experimental configurations (number of shards, models, datasets)\n7. Any details about the MILP formulation for collective certification\n8. The connection to Deep Partition Aggregation (DPA)\n9. Specific numbers from results tables\n10. Any discussion of computational costs or scalability\nBe extremely thorough - I need every technical detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ad2d0a1-c0d9-4278-8ae7-e5944cb16244",
  "isSidechain": true,
  "agentId": "a8858d54dfffc89c6",
  "requestId": "req_011CbYHffHPvKQBCnZnTefZt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3e7ad96-49ba-43f2-a164-ca09cb02bdc7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QNKYsYax99dNaXQ9kp6Y9S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 585,
      "cache_creation_input_tokens": 3202,
      "cache_read_input_tokens": 10074,
      "output_tokens": 376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3202
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 585,
          "output_tokens": 376,
          "cache_read_input_tokens": 10074,
          "cache_creation_input_tokens": 3202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3202,
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

_source line 18 · 2026-05-30T06:34:42.995Z_

<details><summary>↩ Tool result · `toolu_01UYRnkULv2YPpRwKnLsv5pM`</summary>

```text
Web search results for query: "Targeted Partition Aggregation TPA poisoning certification NLG Ghitu Wicker discussion review"

Links: [{"title":"[2602.09757] Towards Poisoning Robustness Certification for Natural Language Generation","url":"https://arxiv.org/abs/2602.09757"},{"title":"Towards Poisoning Robustness Certification for Natural Language Generation","url":"https://arxiv.org/html/2602.09757"},{"title":"Towards Poisoning Robustness Certification for Natural Language Generation","url":"https://arxiv.org/pdf/2602.09757"},{"title":"Deep Partition Aggregation: Provable Defense against General Poisoning Attacks | Request PDF","url":"https://www.researchgate.net/publication/342520348_Deep_Partition_Aggregation_Provable_Defense_against_General_Poisoning_Attacks"},{"title":"Deep Partition Aggregation: Provable Defense against General Poisoning   Attacks","url":"https://arxiv.org/pdf/2006.14768"},{"title":"Improved Certified Defenses against Data Poisoning with (Deterministic)   Finite Aggregation","url":"https://arxiv.org/pdf/2202.02628"},{"title":"[Quick Review] Deep Partition Aggregation: Provable Defense against General Poisoning Attacks","url":"https://liner.com/review/deep-partition-aggregation-provable-defense-against-general-poisoning-attacks"},{"title":"Deep Partition Aggregation: Provable Defenses against General Poisoning Attacks | OpenReview","url":"https://openreview.net/forum?id=YUGG2tFuPM"}]

Based on the web search results, I found relevant information about the paper you're asking about:

The paper "Towards Poisoning Robustness Certification for Natural Language Generation" is authored by Mihnea Ghitu and Matthew Wicker. 

Targeted Partition Aggregation (TPA) is the first algorithm to certify validity/targeted attacks by computing the minimum poisoning budget needed to induce a specific harmful class, token, or phrase. 

The paper addresses the fact that while certified poisoning defenses provide provable robustness bounds for classification tasks, they are fundamentally ill-equipped for autoregressive generation. The work formalizes two security properties: stability (robustness to any change in generation) and validity (robustness to targeted, harmful changes in generation).

TPA is extended to provide tighter guarantees for multi-turn generations using mixed integer linear programming (MILP). The paper was recently published on February 10, 2026 on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc53896e-64b5-4e2d-aad1-231bb0095ea8",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "a8858d54dfffc89c6",
  "type": "user",
  "uuid": "9ddc46d1-cea9-41b6-9d3b-e314b706279d",
  "sourceToolAssistantUUID": "dc53896e-64b5-4e2d-aad1-231bb0095ea8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-30T06:34:43.087Z_

<details><summary>↩ Tool result · `toolu_013rNivXt3ZiYUBS55Uerg9D`</summary>

```text
Web search results for query: ""Targeted Partition Aggregation" poisoning robustness natural language generation"

Links: [{"title":"[2602.09757] Towards Poisoning Robustness Certification for Natural Language Generation","url":"https://arxiv.org/abs/2602.09757"},{"title":"Towards Poisoning Robustness Certification for Natural Language Generation","url":"https://arxiv.org/pdf/2602.09757"},{"title":"Towards Poisoning Robustness Certification for Natural Language Generation","url":"https://arxiv.org/html/2602.09757"},{"title":"Practical Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/html/2504.03957"},{"title":"Exact Certification of Neural Networks and Partition Aggregation Ensembles Against Label Poisoning","url":"https://arxiv.org/html/2604.11416"},{"title":"Deep Partition Aggregation: Provable Defense against General Poisoning Attacks | Request PDF","url":"https://www.researchgate.net/publication/342520348_Deep_Partition_Aggregation_Provable_Defense_against_General_Poisoning_Attacks"}]

Based on the search results, I found detailed information about Targeted Partition Aggregation:

## Overview

Targeted Partition Aggregation (TPA) is the first algorithm to certify validity/targeted attacks by computing the minimum poisoning budget needed to induce a specific harmful class, token, or phrase.

## Context and Problem

Understanding the reliability of natural language generation is critical for deploying foundation models in security-sensitive domains. While certified poisoning defenses provide provable robustness bounds for classification tasks, they are fundamentally ill-equipped for autoregressive generation: they cannot handle sequential predictions or the exponentially large output space of language models.

## Security Framework

The framework formalizes two security properties: stability (robustness to any change in generation) and validity (robustness to targeted, harmful changes in generation).

## Technical Extensions

The TPA algorithm is further extended to provide tighter guarantees for multi-turn generations using mixed integer linear programming (MILP).

This research addresses an important gap in certified robustness for natural language generation systems, particularly in protecting against poisoning attacks that could compromise model behavior during training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ad2d0a1-c0d9-4278-8ae7-e5944cb16244",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "a8858d54dfffc89c6",
  "type": "user",
  "uuid": "110f835f-d10d-401e-b241-5971359f8ac9",
  "sourceToolAssistantUUID": "1ad2d0a1-c0d9-4278-8ae7-e5944cb16244",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-30T06:34:47.373Z_

<details><summary>↩ Tool result · `toolu_01Bn2gbtYZVyHTB7sdotSQtR`</summary>

```text
I appreciate the request, but I need to be transparent about a limitation: the provided content is a PDF file encoded in raw PDF format, which makes it extremely difficult to extract accurate textual information. The document appears to be corrupted or improperly rendered in the text provided, showing primarily binary/compressed data rather than readable content.

From the limited metadata I can access:
- **Title**: "Towards Poisoning Robustness Certification for Natural Language Generation"
- **Authors**: Mihnea Ghitu and Matthew Wicker
- **ArXiv ID**: 2602.09757v1
- **License**: CC-BY 4.0

However, I cannot reliably extract the specific technical details you've requested (exact theorems, experimental configurations, validity functions, MILP formulations, computational costs, etc.) from the corrupted PDF data provided.

**Recommendation**: To get the comprehensive technical details you need, I suggest:
1. Accessing the paper directly from arXiv.org (https://arxiv.org/abs/2602.09757)
2. Downloading the PDF directly and converting it to text format using a proper PDF parser
3. Providing the text content directly rather than raw PDF binary data

I want to ensure accuracy rather than speculate about technical details I cannot verify from the source material.

[Binary content (application/pdf, 3.1MB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/8ee4913b-30ba-4fac-800b-6164c595a9ea/tool-results/webfetch-1780122882234-353qge.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3e7ad96-49ba-43f2-a164-ca09cb02bdc7",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "a8858d54dfffc89c6",
  "type": "user",
  "uuid": "8ddd099c-9057-4a33-b0d0-cda197290c0d",
  "sourceToolAssistantUUID": "e3e7ad96-49ba-43f2-a164-ca09cb02bdc7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-30T06:34:50.922Z_

Let me search for more discussions and also try to get additional details from the HTML version about the RobustRAG relationship.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ddd099c-9057-4a33-b0d0-cda197290c0d",
  "isSidechain": true,
  "agentId": "a8858d54dfffc89c6",
  "requestId": "req_011CbYHgh27474hPTmoMTQfW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb3493ff-131f-4abd-ae74-adc9bd1b493c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HLQ5nwo9dXNXWzU4A9YG8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2731,
      "cache_read_input_tokens": 13276,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2731,
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

_source line 22 · 2026-05-30T06:34:51.436Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XoF5sE7BumAkUrYLPkNPsQ`</summary>

```json
{
  "query": "RobustRAG poisoning certification partition aggregation language generation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb3493ff-131f-4abd-ae74-adc9bd1b493c",
  "isSidechain": true,
  "agentId": "a8858d54dfffc89c6",
  "requestId": "req_011CbYHgh27474hPTmoMTQfW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "859bd85c-b0ad-4c98-8232-d51cd4b0506b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HLQ5nwo9dXNXWzU4A9YG8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2731,
      "cache_read_input_tokens": 13276,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2731,
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

_source line 23 · 2026-05-30T06:34:56.802Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MJw34Jysoiu6dSk7TXwKTC`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.09757v1",
  "prompt": "Focus specifically on:\n1. Every mention of RobustRAG - how is it related, how does this paper differ from it, what specific comparisons are made?\n2. The Related Work section - what papers are discussed and how does this work position itself?\n3. The exact definition of validity functions - what are they, how are they formalized?\n4. The phrase-level certification: how do they extend from token-level to phrase-level?\n5. Appendix content: any additional theorems, proofs, or experimental details\n6. The MILP formulation details for collective/multi-turn certification\n7. Specific experimental numbers from tables and figures\n8. Any discussion of the gap between certified and empirical robustness\nExtract everything verbatim where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "859bd85c-b0ad-4c98-8232-d51cd4b0506b",
  "isSidechain": true,
  "agentId": "a8858d54dfffc89c6",
  "requestId": "req_011CbYHgh27474hPTmoMTQfW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "848720f0-d310-4c95-b853-8365ffb8a6d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HLQ5nwo9dXNXWzU4A9YG8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2731,
      "cache_read_input_tokens": 13276,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2731,
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

_source line 24 · 2026-05-30T06:34:57.374Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TbRW1V7Yu4azK2pGfMQg1R`</summary>

```json
{
  "query": "arXiv 2602.09757 poisoning robustness NLG blog review discussion twitter"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "848720f0-d310-4c95-b853-8365ffb8a6d9",
  "isSidechain": true,
  "agentId": "a8858d54dfffc89c6",
  "requestId": "req_011CbYHgh27474hPTmoMTQfW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d6d1045-ef51-4737-a0d5-79b4c04c4971",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HLQ5nwo9dXNXWzU4A9YG8h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2731,
      "cache_read_input_tokens": 13276,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2731
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 386,
          "cache_read_input_tokens": 13276,
          "cache_creation_input_tokens": 2731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2731,
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

_source line 25 · 2026-05-30T06:34:58.440Z_

<details><summary>↩ Tool result · `toolu_01XoF5sE7BumAkUrYLPkNPsQ`</summary>

```text
Web search results for query: "RobustRAG poisoning certification partition aggregation language generation 2026"

Links: [{"title":"Advances LLM Security, RAGPart And RAGMask Mitigates Corpus Poisoning In Generation Pipelines","url":"https://quantumzeitgeist.com/security-advances-llm-ragpart-ragmask-mitigates/"},{"title":"Towards Poisoning Robustness Certification for Natural Language Generation","url":"https://arxiv.org/pdf/2602.09757"},{"title":"Certifiably Robust RAG against Retrieval Corruption | Request PDF","url":"https://www.researchgate.net/publication/380895542_Certifiably_Robust_RAG_against_Retrieval_Corruption"},{"title":"Towards Poisoning Robustness Certification for Natural Language Generation","url":"https://arxiv.org/html/2602.09757"},{"title":"[2602.09757] Towards Poisoning Robustness Certification for Natural Language Generation","url":"https://arxiv.org/abs/2602.09757"}]

Based on the search results, here's what I found related to your query:

The search revealed several relevant research papers and frameworks from 2026:

**RobustRAG:** RobustRAG is proposed as the first defense framework against retrieval corruption attacks, using an isolate-then-aggregate strategy where LLM responses are obtained from each passage in isolation and then securely aggregated.

**Poisoning Robustness Certification for Natural Language Generation:** A recent paper titled "Towards Poisoning Robustness Certification for Natural Language Generation" addresses the critical need to understand the reliability of natural language generation for deploying foundation models in security-sensitive domains.

**Targeted Partition Aggregation (TPA):** TPA is introduced as the first algorithm to certify validity/targeted attacks by computing the minimum poisoning budget needed to induce a specific harmful class, token, or phrase. The framework extends TPA to provide tighter guarantees for multi-turn generations using mixed integer linear programming (MILP).

**RAGPart and RAGMask:** These are promising defenses against retrieval poisoning in RAG systems that can significantly improve robustness. Research confirms that majority voting is the most effective aggregation method, providing a good balance between utility and defense.

These frameworks represent recent advances in securing language generation systems against poisoning attacks through certified robustness approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "859bd85c-b0ad-4c98-8232-d51cd4b0506b",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "a8858d54dfffc89c6",
  "type": "user",
  "uuid": "88e6b36e-fac0-4680-9b7c-29d9a0622915",
  "sourceToolAssistantUUID": "859bd85c-b0ad-4c98-8232-d51cd4b0506b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-30T06:35:04.431Z_

<details><summary>↩ Tool result · `toolu_01TbRW1V7Yu4azK2pGfMQg1R`</summary>

```text
Web search results for query: "arXiv 2602.09757 poisoning robustness NLG blog review discussion twitter"

Links: [{"title":"[2602.09757] Towards Poisoning Robustness Certification for Natural Language Generation","url":"https://arxiv.org/abs/2602.09757"},{"title":"Towards Poisoning Robustness Certification for Natural Language Generation","url":"https://arxiv.org/html/2602.09757"},{"title":"Towards Poisoning Robustness Certification for Natural Language Generation","url":"https://arxiv.org/pdf/2602.09757"},{"title":"Like Oil and Water: Group Robustness Methods and Poisoning Defenses May Be at Odds","url":"https://arxiv.org/html/2504.02142"},{"title":"Towards Building a Robust Toxicity Predictor","url":"https://arxiv.org/pdf/2404.08690"},{"title":"Are LLM-Enhanced Graph Neural Networks Robust against Poisoning Attacks?","url":"https://arxiv.org/pdf/2603.26105"}]

Based on the search results, I found the arXiv paper 2602.09757. Here's what I found:

The paper "Towards Poisoning Robustness Certification for Natural Language Generation" addresses understanding the reliability of natural language generation for deploying foundation models in security-sensitive domains.

The paper introduces Targeted Partition Aggregation (TPA), the first algorithm to certify validity/targeted attacks by computing the minimum poisoning budget needed to induce a specific harmful class, token, or phrase. The work addresses a gap where certified poisoning defenses for classification tasks cannot handle sequential predictions or the exponentially large output space of language models.

The authors formalize two security properties: stability (robustness to any change in generation) and validity (robustness to targeted, harmful changes in generation). The paper also extends TPA to provide tighter guarantees for multi-turn generations using mixed integer linear programming (MILP).

The paper was submitted to arXiv on February 10, 2026, by authors Mihnea Ghitu and Matthew Wicker.

However, I should note that my search focused on the paper itself from arXiv. The search did not return results about blog reviews, discussions, or Twitter commentary about this paper. If you're looking for those specific types of secondary discussions or commentary, you may want to search for those separately on platforms like Twitter, blogs, or ML discussion forums.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d6d1045-ef51-4737-a0d5-79b4c04c4971",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "a8858d54dfffc89c6",
  "type": "user",
  "uuid": "9736b0fb-9b15-4ac1-b843-19b4f6fd3b0f",
  "sourceToolAssistantUUID": "1d6d1045-ef51-4737-a0d5-79b4c04c4971",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-30T06:35:13.605Z_

<details><summary>↩ Tool result · `toolu_01MJw34Jysoiu6dSk7TXwKTC`</summary>

```text
# Analysis of "Towards Poisoning Robustness Certification for Natural Language Generation"

## RobustRAG and Related Work

**RobustRAG is not mentioned in this paper.** The Related Work section (§2) discusses inference-time formal generation guarantees but focuses on different threat models. The paper cites Xiang et al. (2024) on "Certifiably robust RAG against retrieval corruption," which addresses retrieval corruption rather than training-time data poisoning: "Unlike our focus on post-training poisoning, this research addresses retrieval corruption in Retrieval-Augmented Generation (RAG)."

The authors position their work as addressing a critical gap: "to the best of our knowledge, limited work has directly addressed certified poisoning defenses of natural language generation."

## Validity Function Definitions

**Definition 4.2 (i-th token validity)** formalizes validity as:

"the generation is i-th token valid at x if max_{𝒟̃∈ℬ_k(𝒟)} 𝕀(f̃(x+{t₁,...,t_{i-1}})[0]=t_i)=0"

This means an adversary cannot make target token t_i appear at position 0 after prepending the previous i-1 tokens of a harmful sentence, given budget k.

The validity radius r_i^t is the minimum poisoning budget needed to induce target token t at position i.

## Phrase-Level Certification

**Proposition 4.6** extends token-level to phrase-level by treating length-m sequences as atomic units. Each shard generates m tokens autoregressively: f_s(x)[1:m]∈𝒱^m, then majority voting occurs over this expanded space.

The trade-off is explicitly stated: "In the case of m=1, phrase-level certification reduces to token-level certification, thus the certificate is tight but comes with the aforementioned latency issues. Where m∈[5,20]: certifies moderate-length phrases directly (tighter than sequential min_i) while remaining tractable."

For m=L (full sequence), latency minimizes but "votes diffuse over the |𝒱|^L classes, where each model voting for slightly different variations yield potentially weak margins and thus loose guarantees."

## MILP Formulation for Collective Certification

**Definition 4.7** presents the collective TPA certificate as a mixed-integer linear program maximizing:

"1/N ∑_{i=1}^N 𝕀[τ_i ≤ ∑_{j=1}^M ψ_j^(i)]"

Where τ_i is the aggregation margin to flip ensemble prediction and ψ_j^(i) represents poisonable votes from shard j for prompt i. The constraint ∑_{j=1}^M a_j=K distributes global budget K across M shards.

**Theorem 4.8** guarantees: "at least ⌊N·𝒜(K)⌋ prompts maintain their original (safe) predictions" under attack budget K.

## Experimental Results Summary

**Table 1 (Stability):** DPA+ROE achieves 42%-54% First Token Stability at k=9 across three models. Stability Horizon exceeds 3 tokens until k>5.

**Table 2 (Validity):** TPA+MSC maintains >90% First Token Validity at k=9 with 21+ token validity horizons, substantially outperforming standalone TPA.

**Table 3 (Empirical Attack Robustness):** Ensemble defenses reduce attack success rates from 40-48% (single model) to below 6% against backdoor attacks.

**Figure 2 (MCP Tool-Calling):** Full LoRA achieves median certified radius r=249 (0.5% poisoning resistance) but requires ~150s latency per query; Last-3 LoRA trades robustness (r=163) for 5.9× speedup.

## Certified vs. Empirical Gap

The authors acknowledge conservative certification: "Although our certificates provide rigorous lower bounds, they are inherently conservative. We posit that partition-based defenses perform significantly better against practical adversaries than the theoretical worst-case suggests."

Empirical results substantially exceed certified guarantees—for instance, Table 3 shows near-zero attack success rates where certified bounds would be looser.

## Impact Statement

The conclusion acknowledges scope limitations: "our certification framework addresses a specific threat model: training-time poisoning under worst-case assumptions. Other important threat modes—such as test-time evasion, prompt-based attacks, and triggered backdoors—remain critical open challenges."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "848720f0-d310-4c95-b853-8365ffb8a6d9",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "a8858d54dfffc89c6",
  "type": "user",
  "uuid": "d82a2947-9b3f-4c7e-8ffe-72579c2ca189",
  "sourceToolAssistantUUID": "848720f0-d310-4c95-b853-8365ffb8a6d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-30T06:35:16.501Z_

Let me get one more round of detail on the specific relationship to RobustRAG and the exact theorems.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d82a2947-9b3f-4c7e-8ffe-72579c2ca189",
  "isSidechain": true,
  "agentId": "a8858d54dfffc89c6",
  "requestId": "req_011CbYHid5XTJ2gySGgX9Bd2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b107b68-15a2-42d5-8ee9-022f75e89cb8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013FE9GAQG2JxViEyTfZbPBB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 625,
      "cache_creation_input_tokens": 2137,
      "cache_read_input_tokens": 16007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2137,
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

_source line 29 · 2026-05-30T06:35:23.261Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018WbYkxpjdSGKZNgegHi7Zi`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.09757v1",
  "prompt": "Extract the following specific details:\n1. The EXACT text of Theorem 4.3 (the token-level validity certificate) - verbatim\n2. The EXACT text of Theorem 4.8 (collective TPA certificate) - verbatim\n3. The EXACT text of Propositions 4.5 and 4.6 - verbatim\n4. What specifically do they say about Xiang et al. 2024 (the RobustRAG / certifiably robust RAG paper)? Quote the relevant passage.\n5. What do they say about Deep Partition Aggregation (DPA) by Levine & Feizi? How does TPA extend or differ from DPA?\n6. The ROE (Randomized Ordering Ensemble) and MSC (Most Specific Class) methods - what are these?\n7. Any mention of specific models used (Qwen, OLMo, Gemma, etc.) and their sizes\n8. The Toucan dataset - what is it and how is it used?\n9. Any details about how they handle the autoregressive dependency problem\n10. What is the \"shard-and-aggregate\" framework exactly?\nProvide as much verbatim text as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b107b68-15a2-42d5-8ee9-022f75e89cb8",
  "isSidechain": true,
  "agentId": "a8858d54dfffc89c6",
  "requestId": "req_011CbYHid5XTJ2gySGgX9Bd2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5cb1d86-9b91-477c-9761-7c73f51ca665",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013FE9GAQG2JxViEyTfZbPBB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 625,
      "cache_creation_input_tokens": 2137,
      "cache_read_input_tokens": 16007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2137,
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

_source line 30 · 2026-05-30T06:35:23.884Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QCyqwXNi2MH8PPWWGppF9c`</summary>

```json
{
  "query": "Matthew Wicker certified robustness poisoning NLG paper 2026 ICML NeurIPS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5cb1d86-9b91-477c-9761-7c73f51ca665",
  "isSidechain": true,
  "agentId": "a8858d54dfffc89c6",
  "requestId": "req_011CbYHid5XTJ2gySGgX9Bd2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03c814c1-6966-4700-918c-11cb8c19aaf1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013FE9GAQG2JxViEyTfZbPBB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 625,
      "cache_creation_input_tokens": 2137,
      "cache_read_input_tokens": 16007,
      "output_tokens": 450,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2137
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 625,
          "output_tokens": 450,
          "cache_read_input_tokens": 16007,
          "cache_creation_input_tokens": 2137,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2137,
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

_source line 31 · 2026-05-30T06:35:30.164Z_

<details><summary>↩ Tool result · `toolu_01QCyqwXNi2MH8PPWWGppF9c`</summary>

```text
Web search results for query: "Matthew Wicker certified robustness poisoning NLG paper 2026 ICML NeurIPS"

Links: [{"title":"Towards Poisoning Robustness Certification for Natural Language Generation","url":"https://arxiv.org/html/2602.09757"},{"title":"Certified Robustness to Data Poisoning in Gradient-Based Training","url":"https://arxiv.org/html/2406.05670v1"},{"title":"Towards Poisoning Robustness Certification for Natural Language Generation","url":"https://arxiv.org/pdf/2602.09757"},{"title":"Provable Robustness of (Graph) Neural Networks Against ...","url":"https://openreview.net/pdf?id=jIAPLDdGVx"},{"title":"Certified Robustness to Data Poisoning in Gradient-Based Training","url":"https://arxiv.org/pdf/2406.05670"},{"title":"[2406.05670] Certified Robustness to Data Poisoning in Gradient-Based Training","url":"https://arxiv.org/abs/2406.05670"},{"title":"Matthew WICKER | DPhil (PhD) Student | Bachelor of Science | University of Oxford, Oxford | OX | Department of Computer Science | Research profile","url":"https://www.researchgate.net/profile/Matthew-Wicker"},{"title":"Keeping up with dynamic attackers: Certifying robustness to adaptive   online data poisoning","url":"https://arxiv.org/pdf/2502.16737"}]

Based on the search results, I found relevant information about Matthew Wicker's work on poisoning robustness for natural language generation:

The paper is titled "Towards Poisoning Robustness Certification for Natural Language Generation" by Mihnea Ghitu and Matthew Wicker. While certified poisoning defenses provide provable robustness bounds for classification tasks, they are fundamentally ill-equipped for autoregressive generation as they cannot handle sequential predictions or the exponentially large output space of language models. The authors formalize two security properties: stability (robustness to any change in generation) and validity (robustness to targeted, harmful changes in generation), and introduce Targeted Partition Aggregation (TPA), the first algorithm to certify validity/targeted attacks by computing the minimum poisoning budget needed to induce a specific harmful class, token, or phrase.

This paper appears to be from February 10, 2026 according to the metadata, and is available on arXiv (preprint arXiv:2602.09757). However, the search results do not specifically indicate whether this paper was submitted to or accepted at ICML or NeurIPS.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03c814c1-6966-4700-918c-11cb8c19aaf1",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "a8858d54dfffc89c6",
  "type": "user",
  "uuid": "4d66553c-eaaf-4561-8bfd-2f9bd7c22ccb",
  "sourceToolAssistantUUID": "03c814c1-6966-4700-918c-11cb8c19aaf1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-30T06:35:34.739Z_

<details><summary>↩ Tool result · `toolu_018WbYkxpjdSGKZNgegHi7Zi`</summary>

```text
# Extraction from "Towards Poisoning Robustness Certification for Natural Language Generation"

## 1. Theorem 4.3 (Token-Level Validity Certificate)

"The value r_i^t computed by Algorithm 1 is a sound lower bound on the i^th-token validity radius (Definition 4.2). For any poisoning budget k ≤ r_i^t, the adversary cannot make target token t the plurality prediction."

## 2. Theorem 4.8 (Collective TPA Certificate)

"Let 𝒜(K) denote the solution to the MILP in Definition 4.7. For any attack within budget K, at least ⌊N·𝒜(K)⌋ prompts maintain their original (safe) predictions."

## 3. Propositions 4.5 and 4.6

**Proposition 4.5**: "Define r_min(x;1:L):=min_{i∈{1,…,L}}r^⊛_i(x). Then r_min(x;1:L)≤r_{1:L}^⊛(x)."

**Proposition 4.6**: "∀φ∈𝒱^m let V[φ] denote votes received by phrase φ. Our prior certification algorithms remain sound for the transformed problem."

## 4. Xiang et al. 2024 (RobustRAG)

"Unlike our focus on post-training poisoning, this research addresses retrieval corruption in Retrieval-Augmented Generation (RAG), where attackers corrupt retrieved documents rather than the model's (post-)training data."

## 5. Deep Partition Aggregation (DPA) vs. TPA

DPA "provide[s] strong guarantees for classification. However, autoregressive language generation introduces a fundamental challenge: changing token i intervenes on the distribution of all subsequent tokens j>i." TPA extends DPA by introducing **Targeted Partition Aggregation** specifically for **validity** (targeted harmful outputs) rather than just stability.

## 6. ROE and MSC Methods

The paper references "DPA+ROE" which "incorporates run-off elections" (Rezaei et al., 2023). However, **MSC is not defined as separate methodology**—"DPA+MSC" refers to their proposed multi-turn/multi-sample collective certification technique.

## 7. Models Used

- **OLMo-1B** and **OLMo-2-1B-Instruct** (Groeneveld et al., 2024)
- **Gemma2-2B** (Team et al., 2024)
- **Qwen1.5-4B** (Yang et al., 2024)

## 8. Toucan Dataset

"Toucan dataset (Xu et al., 2025)…a dataset with 50,000 training instances" filtered to "top 150 tools" from "tool-agentic data from real-world MCP environments."

## 9. Autoregressive Dependency Problem

Two soundness concerns: "(i) the i^th-token certificate assumes the prefix f(x)[1:i−1] are fixed, but if an adversary changes any token j<i, this assumption is violated; (ii) details likely comprise multiple tokens rather than one."

## 10. Shard-and-Aggregate Framework

"Partition the provided training dataset 𝒟 into S disjoint shards…train independent base models…At test time, generate using majority vote of the ensemble."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5cb1d86-9b91-477c-9761-7c73f51ca665",
  "isSidechain": true,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "agentId": "a8858d54dfffc89c6",
  "type": "user",
  "uuid": "18de535b-daf3-46b5-8ffc-66517eabaf3e",
  "sourceToolAssistantUUID": "c5cb1d86-9b91-477c-9761-7c73f51ca665",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-30T06:36:49.423Z_

Here is a thorough technical summary of the paper.

---

## "Towards Poisoning Robustness Certification for Natural Language Generation"
**Authors:** Mihnea Ghitu, Matthew Wicker
**arXiv:** 2602.09757, submitted February 10, 2026
**Category:** cs.LG

---

### Full Abstract

The paper addresses the reliability of language generation systems deployed in security-sensitive domains. While certified poisoning defenses provide provable robustness bounds for classification tasks, they are fundamentally ill-equipped for autoregressive generation because they cannot handle sequential predictions or the exponentially large output space of language models. The authors formalize two security properties -- **stability** (robustness to any change in generation) and **validity** (robustness to targeted, harmful changes in generation) -- and introduce **Targeted Partition Aggregation (TPA)**, described as "the first algorithm to certify validity/targeted attacks by computing the minimum poisoning budget needed to induce a specific harmful class, token, or phrase." They extend TPA using mixed integer linear programming (MILP) for multi-turn generations and demonstrate effectiveness in certifying agent tool-calling robustness and preference-based alignment, achieving >90% validity certification at k=9 poisoning budget with 20+ token horizons.

---

### Key Method Details

#### 1. Targeted Partition Aggregation (TPA)

TPA builds on the **shard-and-aggregate** framework:
1. Partition training dataset D into S disjoint shards {D_s}
2. Train independent base models {f_s} on each shard
3. At test time, ensemble generates via majority voting: F(x) = argmax_{y in V} V[y], where V[t] counts votes for token t

**Algorithm 1 (Core TPA):** Given token index i, vote counts V (sorted descending), and target token t with v_t votes:
- For each phase s, compute Delta[j] = V[j] - V[j+1] (gap between consecutive vote counts)
- Compute Phi[s] = v_t + sum of first s gaps (cumulative votes reassigned to t)
- Find s* = min{s | Phi[s] > V[s] or s = |V|-1}
- Return r_i^t = Phi[s*-1] + floor(((V_{s*} - Phi[s*-1] + 1) * s*) / (s*+1))

The intuition: TPA iteratively reallocates votes from top-ranked classes to the target harmful token t until achieving plurality. At each phase s, the top s classes are equalized and jointly reduced to the next vote level, with removed votes reassigned to t. This computes the **minimum number of shard poisonings** needed to make t win the vote.

#### 2. Stability vs. Validity Definitions

**Definition 4.1 (i-th token stability):** For prompt x, the i-th token generation is k-stable if:
max_{D_tilde in B_k(D)} I(f(x)[i] != f_tilde(x)[i]) = 0

The stability radius is the minimum r where a poisoned dataset can cause any token change.

**Definition 4.2 (i-th token validity):** Given harmful sentence s_h = {t_1,...,t_T}, generation is i-th token valid at x if:
max_{D_tilde in B_k(D)} I(f_tilde(x + {t_1,...,t_{i-1}})[0] = t_i) = 0

The validity radius r_i^t is the minimum poisoning budget needed to make target token t_i the next generated token. This is the key conceptual innovation: validity asks whether a **specific harmful output** can be induced, rather than whether **any** change occurs.

**Definition 4.4 (Finite-horizon stability/validity):**
r_{1:L}(x) = min_{i in [L]} {r_i(x)}

#### 3. Handling the Autoregressive Dependency Problem

Two soundness concerns arise: (i) the i-th token certificate assumes the prefix f(x)[1:i-1] is fixed, but if an adversary changes token j&lt;i, this assumption is violated; (ii) harmful phrases comprise multiple tokens. Solutions:

**Proposition 4.5 (Sequential certificate):** r_min(x; 1:L) = min_{i in {1,...,L}} r_i(x) <= r_{1:L}(x). Any attack on the full prefix requires at least r_min poisoned samples. This is a sound lower bound because changing any prefix token requires at least as many poisoned points as the weakest position.

**Proposition 4.6 (Phrase-level certificate):** Treat length-m token sequences as atomic units. Each shard generates m tokens autoregressively, then majority voting occurs over the expanded space V^m. For m=1, this reduces to token-level certification (tight but high latency). For moderate m in [5,20], it certifies moderate-length phrases directly with tighter bounds than sequential min. For m=L (full sequence), latency minimizes but "votes diffuse over the |V|^L classes" making margins weak.

#### 4. Multi-Turn Collective Certification (MILP)

**Definition 4.7 (Collective TPA Certificate):** For N test prompts with global budget K and M shards, the MILP maximizes:
(1/N) sum_{i=1}^N I[tau_i <= sum_{j=1}^M psi_j^(i)]

Subject to:
- psi_j^(i) encodes poisonable votes from shard j for prompt i
- tau_i is the aggregation margin to flip the ensemble prediction
- sum_{j=1}^M a_j = K (global budget constraint distributes K across M shards)

**Theorem 4.8:** The solution A(K) guarantees at least floor(N * A(K)) prompts maintain their original (safe) predictions under any attack within budget K.

#### 5. Validity Functions

Validity is defined relative to a specific harmful target. The paper does not propose separate "validity functions" as modular components; rather, validity is formalized directly in Definition 4.2 as the impossibility of inducing a specific target token/phrase given a poisoning budget. The key distinction is that stability measures robustness to **any** output change (untargeted), while validity measures robustness to a **specific harmful** output change (targeted).

---

### Theoretical Guarantees

1. **Theorem 4.3 (Token-Level Validity Certificate):** "The value r_i^t computed by Algorithm 1 is a sound lower bound on the i-th token validity radius. For any poisoning budget k <= r_i^t, the adversary cannot make target token t the plurality prediction."

2. **Proposition 4.5 (Sequential certificate):** The minimum per-position radius is a sound lower bound on the full-sequence radius.

3. **Proposition 4.6 (Phrase-level certificate):** Certification algorithms remain sound when applied to phrase-level (m-token) voting over the transformed space V^m.

4. **Theorem 4.8 (Collective certificate):** For any attack within global budget K, at least floor(N * A(K)) prompts maintain safe predictions.

The threat model assumes an **unbounded, white-box adversary** with access to architecture, dataset, training order, and hyperparameters, who can perform general poisoning of features, labels, or both, constrained only by |D symmetric_difference D_tilde| <= r.

---

### Relationship to RobustRAG

The paper explicitly distinguishes itself from RobustRAG (Xiang et al., 2024, "Certifiably robust RAG against retrieval corruption"). The authors state: **"Unlike our focus on post-training poisoning, this research addresses retrieval corruption in Retrieval-Augmented Generation (RAG), where attackers corrupt retrieved documents rather than the model's (post-)training data."**

Key differences:
- **Threat model:** RobustRAG addresses **inference-time retrieval corruption** (adversary corrupts retrieved documents at test time). This paper addresses **training-time data poisoning** (adversary corrupts the training data before/during fine-tuning).
- **Defense mechanism:** Both use isolate-then-aggregate strategies, but RobustRAG isolates retrieved passages and aggregates LLM responses, while this paper partitions training data into shards, trains independent models, and aggregates via majority voting.
- **Certification target:** RobustRAG certifies that retrieval corruption cannot change outputs. This paper certifies that training data poisoning cannot induce specific harmful outputs (validity) or any output change (stability).

---

### Experimental Results

**Models used:** OLMo-1B, OLMo-2-1B-Instruct, Gemma2-2B, Qwen1.5-4B

**Datasets and settings:**

1. **Agent Tool-Calling (MCP):** Toucan dataset (50K training instances, top 150 tools from real-world MCP environments), 500 shards.
   - Full LoRA: median certified robustness r=249 (resists 0.5% dataset poisoning), accuracy 67% vs 40% zero-shot baseline, latency ~150s
   - Last-3 LoRA: r=163, 5.9x speedup (latency ~25s)

2. **Preference Alignment (HH-RLHF):** 20 shards across three models.
   - DPA+ROE (stability): 42-54% First Token Stability at k=9
   - TPA+MSC (validity): >90% First Token Validity at k=9, validity horizons of 21+ tokens
   - Stability Horizon: 0.25-8.31 tokens depending on model and method

3. **Empirical Attack Robustness:** Ensemble defense reduces backdoor attack success from 40-48% (single model) to <6%, with stealth scores >95%

**Evaluation Metrics:**
- First-Token Stability (FTS@k): fraction of prompts with unchanged first token under k-poisoning
- First-Token Validity (FTV@k): fraction where first token cannot be changed to target harmful token
- Stability Horizon (SH@k): average length of longest certified stable prefix
- Validity Horizon (VH@k): average length before harmful sequence can be induced

---

### Limitations Acknowledged

1. **Inference-time latency** remains "an open challenge" -- running hundreds of shard models is expensive (150s for Full LoRA with 500 shards).
2. **Conservative bounds:** "Although our certificates provide rigorous lower bounds, they are inherently conservative. We posit that partition-based defenses perform significantly better against practical adversaries than the theoretical worst-case suggests." The empirical results substantially exceed certified guarantees.
3. **Narrow threat model:** "Our certification framework addresses a specific threat model: training-time poisoning under worst-case assumptions. Other important threat modes -- such as test-time evasion, prompt-based attacks, and triggered backdoors -- remain critical open challenges."
4. **Bounds do not eliminate vulnerabilities** from alternative attack surfaces.
5. The stability-validity trade-off and the phrase-length trade-off (tight bounds vs. computational cost) are inherent tensions in the framework.

---

### Discussion/Reviews

No external reviews, blog posts, or social media discussions of this paper were found. The paper appears to be a recent preprint (February 2026) without yet appearing at a major venue. It is positioned in the lineage of Deep Partition Aggregation (DPA) by Levine & Feizi and Finite Aggregation by Rezaei et al., extending these classification-oriented certified defenses to the autoregressive NLG setting for the first time.

Sources:
- [arXiv Abstract Page](https://arxiv.org/abs/2602.09757)
- [arXiv HTML Version](https://arxiv.org/html/2602.09757)
- [arXiv PDF](https://arxiv.org/pdf/2602.09757)
- [Deep Partition Aggregation (Levine & Feizi)](https://arxiv.org/pdf/2006.14768)
- [RobustRAG (Xiang et al.)](https://www.researchgate.net/publication/380895542_Certifiably_Robust_RAG_against_Retrieval_Corruption)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18de535b-daf3-46b5-8ffc-66517eabaf3e",
  "isSidechain": true,
  "agentId": "a8858d54dfffc89c6",
  "requestId": "req_011CbYHkBTUCW8LHjJykYAwX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33f89169-392f-42f9-8f67-e290a4a6775e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YJgcxVpKYLEkBm27MbXJ1Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 682,
      "cache_creation_input_tokens": 1946,
      "cache_read_input_tokens": 18144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1946,
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
