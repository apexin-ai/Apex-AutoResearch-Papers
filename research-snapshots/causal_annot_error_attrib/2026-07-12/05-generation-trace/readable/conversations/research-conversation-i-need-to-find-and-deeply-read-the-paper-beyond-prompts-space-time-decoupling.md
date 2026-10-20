# Research conversation: I need to find and deeply read the paper "Beyond Prompts: Space-Time Decoupling Control-Plane Jailbreaks in LLM Structur

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aba53dbf8214eeda6.jsonl`
- **Structured JSON:** [`e6f157b76941a99d82f0.json`](../../sessions/e6/e6f157b76941a99d82f0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-19T09:26:52.191Z_

I need to find and deeply read the paper "Beyond Prompts: Space-Time Decoupling Control-Plane Jailbreaks in LLM Structured Output" (arXiv 2503.24191, Mar 2025, revised Jan 2026). 

Please:
1. Search for this paper using multiple queries: the title, the arXiv ID, "structured output jailbreak constrained decoding"
2. Fetch the arXiv abstract page (https://arxiv.org/abs/2503.24191) to get the full abstract and details
3. If possible, fetch the HTML version (https://arxiv.org/html/2503.24191) to read methodology details

I need to understand:
- What exactly is "Space-Time Decoupling"? What are "Control-Plane Jailbreaks"?
- How do they achieve 94.3-99.5% ASR? What models were tested?
- What specific evidence do they provide that constrained decoding/structured output suppresses refusal?
- How does this relate to tool-call generation specifically?

Report detailed findings - this paper is supposedly the strongest empirical motivation for a mechanistic study of why refusal fails during structured/tool-call output.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a8927760-54f5-4249-ad03-f69ac6716d84",
  "agentId": "aba53dbf8214eeda6",
  "type": "user",
  "uuid": "245b2186-a364-4b4d-aeb1-863ca53fa748",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T09:26:52.194Z_

```json
{
  "parentUuid": "245b2186-a364-4b4d-aeb1-863ca53fa748",
  "isSidechain": true,
  "agentId": "aba53dbf8214eeda6",
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
  "uuid": "ae830862-c278-4da8-af97-6b775512a79f",
  "timestamp": "2026-05-19T09:26:52.194Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T09:26:52.195Z_

```json
{
  "parentUuid": "ae830862-c278-4da8-af97-6b775512a79f",
  "isSidechain": true,
  "agentId": "aba53dbf8214eeda6",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "311c7ea6-da55-4c92-a0b6-ff4bb885bfc2",
  "timestamp": "2026-05-19T09:26:52.195Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T09:26:55.496Z_



I'll search for this paper using multiple approaches and fetch the actual arXiv pages. Let me start with all the searches and fetches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "311c7ea6-da55-4c92-a0b6-ff4bb885bfc2",
  "isSidechain": true,
  "agentId": "aba53dbf8214eeda6",
  "requestId": "req_011CbBguhijGcdd6G9imqmWx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "890f6363-05f9-4510-a16e-f2ea71e90c7f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VXN6MeYJfNhFtm7zNZZC7u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1629,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1629,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 5 · 2026-05-19T09:26:55.765Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WuKbgrt28jevbHwLKeWXFV`</summary>

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
  "parentUuid": "890f6363-05f9-4510-a16e-f2ea71e90c7f",
  "isSidechain": true,
  "agentId": "aba53dbf8214eeda6",
  "requestId": "req_011CbBguhijGcdd6G9imqmWx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "652cecca-9858-4108-b89d-3cfce287b28e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VXN6MeYJfNhFtm7zNZZC7u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1629,
      "cache_read_input_tokens": 7773,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1629
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 112,
          "cache_read_input_tokens": 7773,
          "cache_creation_input_tokens": 1629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1629,
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

_source line 6 · 2026-05-19T09:26:55.773Z_

<details><summary>↩ Tool result · `toolu_01WuKbgrt28jevbHwLKeWXFV`</summary>

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
  "parentUuid": "652cecca-9858-4108-b89d-3cfce287b28e",
  "isSidechain": true,
  "promptId": "a8927760-54f5-4249-ad03-f69ac6716d84",
  "agentId": "aba53dbf8214eeda6",
  "type": "user",
  "uuid": "fdb0fedf-149c-4152-a55c-92b4de105bcd",
  "sourceToolAssistantUUID": "652cecca-9858-4108-b89d-3cfce287b28e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T09:26:59.121Z_



Now let me run all the searches and fetches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdb0fedf-149c-4152-a55c-92b4de105bcd",
  "isSidechain": true,
  "agentId": "aba53dbf8214eeda6",
  "requestId": "req_011CbBguyD9G3p5cPfbqfrsn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea44f031-dfa5-4282-bb1b-21cd7e59af27",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NmueVKzkuarfHgcnTpf4xx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 9402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1134,
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

_source line 8 · 2026-05-19T09:26:59.326Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017A5hhpVe5qknMgywtcTefa`</summary>

```json
{
  "query": "Beyond Prompts Space-Time Decoupling Control-Plane Jailbreaks LLM Structured Output arXiv 2503.24191"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea44f031-dfa5-4282-bb1b-21cd7e59af27",
  "isSidechain": true,
  "agentId": "aba53dbf8214eeda6",
  "requestId": "req_011CbBguyD9G3p5cPfbqfrsn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6caee1e3-de9e-43c8-bc04-565f4216caf0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NmueVKzkuarfHgcnTpf4xx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 9402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1134,
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

_source line 9 · 2026-05-19T09:27:05.694Z_

<details><summary>↩ Tool result · `toolu_017A5hhpVe5qknMgywtcTefa`</summary>

```text
Web search results for query: "Beyond Prompts Space-Time Decoupling Control-Plane Jailbreaks LLM Structured Output arXiv 2503.24191"

Links: [{"title":"[2503.24191] Beyond Prompts: Space-Time Decoupling Control-Plane Jailbreaks in LLM Structured Output","url":"https://arxiv.org/abs/2503.24191"},{"title":"Beyond Prompts: Space–Time Decoupling Control-Plane Jailbreaks in LLM Structured Output","url":"https://arxiv.org/html/2503.24191"},{"title":"Space-Time Decoupling Control-Plane Jailbreaks in LLM ...","url":"https://arxiv.org/pdf/2503.24191"},{"title":"Do Internal Layers of LLMs Reveal Patterns for Jailbreak Detection?","url":"https://arxiv.org/pdf/2510.06594"},{"title":"Output Constraints as Attack Surface: Exploiting Structured Generation to Bypass LLM Safety Mechanisms","url":"https://arxiv.org/html/2503.24191v1"},{"title":"Anyone Can Jailbreak: Prompt-Based Attacks on LLMs and T2Is","url":"https://arxiv.org/pdf/2507.21820"}]

I found the paper! Here's what the search revealed:

The paper focuses on how LLMs are used through structured output APIs to ensure syntax compliance, but this feature presents significant security vulnerabilities.

The research introduces Constrained Decoding Attack (CDA), a novel jailbreak class that weaponizes structured output constraints to bypass both external auditing and internal safety alignment, operating by embedding malicious intent in schema-level grammar rules (control-plane) while maintaining benign surface prompts (data-plane).

The paper instantiates this with two proof-of-concept attacks: EnumAttack, which embeds malicious content in enum fields; and DictAttack, which decouples the malicious payload across a benign prompt and a dictionary-based grammar.

The vulnerability is particularly relevant as LLMs are increasingly integrated into complex agent frameworks and enterprise automation pipelines where they function as core reasoning engines.

The paper was published on arXiv on January 5, 2026 (version 2) and appears to be addressing a previously overlooked attack surface in LLM safety mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6caee1e3-de9e-43c8-bc04-565f4216caf0",
  "isSidechain": true,
  "promptId": "a8927760-54f5-4249-ad03-f69ac6716d84",
  "agentId": "aba53dbf8214eeda6",
  "type": "user",
  "uuid": "1db2e18c-5969-4e20-be57-988494092704",
  "sourceToolAssistantUUID": "6caee1e3-de9e-43c8-bc04-565f4216caf0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T09:27:08.291Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016CXNxAorvwoFojHJCeibg2`</summary>

```json
{
  "query": "structured output jailbreak constrained decoding attack safety bypass 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1db2e18c-5969-4e20-be57-988494092704",
  "isSidechain": true,
  "agentId": "aba53dbf8214eeda6",
  "requestId": "req_011CbBgvhNgDGQcyX5BZrKei",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8178f7b3-9e24-4998-9906-130b2ba37834",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ysNcsbbEm9rjgaC5ZH1CV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 10536,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 697
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 10536,
          "cache_creation_input_tokens": 697,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 697,
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

_source line 11 · 2026-05-19T09:27:15.378Z_

<details><summary>↩ Tool result · `toolu_016CXNxAorvwoFojHJCeibg2`</summary>

```text
Web search results for query: "structured output jailbreak constrained decoding attack safety bypass 2025"

Links: [{"title":"Output Constraints as Attack Surface: Exploiting Structured Generation to Bypass LLM Safety Mechanisms - Advanced AI News","url":"https://advancedainews.com/output-constraints-as-attack-surface-exploiting-structured-generation-to-bypass-llm-safety-mechanisms/"},{"title":"Output Constraints as Attack Surface: Exploiting Structured Generation to Bypass LLM Safety Mechanisms","url":"https://arxiv.org/html/2503.24191v1"},{"title":"Exploiting Prefix-Tree in Structured Output Interfaces for Enhancing Jailbreak Attacking","url":"https://arxiv.org/html/2502.13527"},{"title":"Awesome-LM-SSP/collection/paper/safety/jailbreak.md at main · CryptoAILab/Awesome-LM-SSP","url":"https://github.com/CryptoAILab/Awesome-LM-SSP/blob/main/collection/paper/safety/jailbreak.md"},{"title":"Output Constraints as Attack Surface: Exploiting Structured ...","url":"https://arxiv.org/abs/2503.24191"},{"title":"(PDF) Output Constraints as Attack Surface: Exploiting Structured Generation to Bypass LLM Safety Mechanisms","url":"https://www.researchgate.net/publication/390404554_Output_Constraints_as_Attack_Surface_Exploiting_Structured_Generation_to_Bypass_LLM_Safety_Mechanisms"},{"title":"Output Constraints as Attack Surface: Exploiting Structured Generation to Bypass LLM Safety Mechanisms - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250324191Z/abstract"},{"title":"[Literature Review] Output Constraints as Attack Surface: Exploiting Structured Generation to Bypass LLM Safety Mechanisms","url":"https://www.themoonlight.io/en/review/output-constraints-as-attack-surface-exploiting-structured-generation-to-bypass-llm-safety-mechanisms"}]

Based on the search results, here's what I found about structured output jailbreak and constrained decoding attacks:

## Key Findings

Constrained Decoding Attack (CDA) is a novel jailbreak class that weaponizes structured output constraints to bypass safety mechanisms. This represents a significant recent development in LLM security research from 2025.

### How It Works

CDA exploits the output constraints enforced by structured output APIs, effectively bypassing the LLM's safety mechanisms, differing from traditional attacks that focus on input prompts. Constrained Decoding Attacks represent a significant shift in the jailbreaking paradigm by targeting the decoding process rather than relying on prompt engineering.

### The Underlying Vulnerability

LLMs are extensively used as tooling platforms through structured output APIs to ensure syntax compliance for robust integration with existing software, but the feature enabling grammar-guided structured output presents significant security vulnerabilities. Constrained decoding combines grammar-level rules with LLM decoding process to ensure grammar-compatible output, enabling structured output features like regular expressions, JSON schema or arbitrary EBNF grammars.

### Threat Assessment

Chain Enum Attack bypasses most existing prompt-based external safeguards, including industrially deployed defenses from OpenAI and Gemini. To counter structured output-based jailbreak attacks, service vendors could implement real-time constrained decoding monitors to detect adversarial pattern manipulation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8178f7b3-9e24-4998-9906-130b2ba37834",
  "isSidechain": true,
  "promptId": "a8927760-54f5-4249-ad03-f69ac6716d84",
  "agentId": "aba53dbf8214eeda6",
  "type": "user",
  "uuid": "c81cc46a-148a-4a23-a84a-e36a734fe77c",
  "sourceToolAssistantUUID": "8178f7b3-9e24-4998-9906-130b2ba37834",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T09:27:17.941Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SZXjvTr6VSsDyB1ssGjWfG`</summary>

```json
{
  "query": "\"constrained decoding attack\" \"EnumAttack\" \"DictAttack\" jailbreak LLM safety alignment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c81cc46a-148a-4a23-a84a-e36a734fe77c",
  "isSidechain": true,
  "agentId": "aba53dbf8214eeda6",
  "requestId": "req_011CbBgwQp3ouKDsLCe8PwcL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3df9fcf3-38a8-4c49-b923-d8d79ae9cff1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Azb1By59QtTdhsAE4ZBMdV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 932,
      "cache_read_input_tokens": 11233,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 932
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 11233,
          "cache_creation_input_tokens": 932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 932,
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

_source line 13 · 2026-05-19T09:27:26.107Z_

<details><summary>↩ Tool result · `toolu_01SZXjvTr6VSsDyB1ssGjWfG`</summary>

```text
Web search results for query: ""constrained decoding attack" "EnumAttack" "DictAttack" jailbreak LLM safety alignment"

Links: [{"title":"Beyond Prompts: Space–Time Decoupling Control-Plane Jailbreaks in LLM Structured Output","url":"https://arxiv.org/html/2503.24191"},{"title":"Output Constraints as Attack Surface: Exploiting Structured Generation to Bypass LLM Safety Mechanisms","url":"https://arxiv.org/html/2503.24191v1"},{"title":"[2503.24191] Beyond Prompts: Space-Time Decoupling Control-Plane Jailbreaks in LLM Structured Output","url":"https://arxiv.org/abs/2503.24191"},{"title":"[Literature Review] Output Constraints as Attack Surface: Exploiting Structured Generation to Bypass LLM Safety Mechanisms","url":"https://www.themoonlight.io/en/review/output-constraints-as-attack-surface-exploiting-structured-generation-to-bypass-llm-safety-mechanisms"},{"title":"Space-Time Decoupling Control-Plane Jailbreaks in LLM ...","url":"https://arxiv.org/pdf/2503.24191"},{"title":"BreakFun: Jailbreaking LLMs via Schema Exploitation","url":"https://arxiv.org/html/2510.17904v2"},{"title":"Exploiting Prefix-Tree in Structured Output Interfaces for Enhancing Jailbreak Attacking","url":"https://arxiv.org/html/2502.13527"}]

Based on the search results, here's what I found about constrained decoding attacks, EnumAttack, and DictAttack:

## Overview

Constrained Decoding Attack (CDA) is a novel class of jailbreaks that targets the LLM control plane—the grammar that dictates the output structure. Unlike conventional jailbreak attacks on the data plane, hiding unsafe instructions inside otherwise benign prompts, CDA embeds malicious intent directly into the grammar itself.

## EnumAttack and DictAttack

EnumAttack embeds malicious content in enum fields; and the more evasive DictAttack decouples the malicious payload across a benign prompt and a dictionary-based grammar. 

Enum Attack leverages JSON Schema's enum feature to exploit structured output constraints in modern LLM APIs, allowing attackers to bypass safety mechanisms and generate harmful outputs.

## Attack Effectiveness and Defense Challenges

The attacks show significant success rates: DictAttack achieves 94.3--99.5% ASR across five benchmarks on gpt-5, gemini-2.5-pro, deepseek-r1, and gpt-oss-120b.

While basic grammar auditing mitigates EnumAttack, the more sophisticated DictAttack maintains a 75.8% ASR even against multiple state-of-the-art jailbreak guardrails. This exposes a critical "semantic gap" in current safety architectures and underscores the urgent need for cross-plane defenses that can bridge the data and control planes to secure the LLM generation pipeline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3df9fcf3-38a8-4c49-b923-d8d79ae9cff1",
  "isSidechain": true,
  "promptId": "a8927760-54f5-4249-ad03-f69ac6716d84",
  "agentId": "aba53dbf8214eeda6",
  "type": "user",
  "uuid": "abb7c18b-5e1c-45ba-9468-45c8ec010aa7",
  "sourceToolAssistantUUID": "3df9fcf3-38a8-4c49-b923-d8d79ae9cff1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-19T09:27:28.871Z_

Now let me fetch the actual arXiv pages for detailed content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abb7c18b-5e1c-45ba-9468-45c8ec010aa7",
  "isSidechain": true,
  "agentId": "aba53dbf8214eeda6",
  "requestId": "req_011CbBgxCf5ZJjk34XGvqoxg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb4256f0-d5df-4205-932e-46d78a7d635b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WCMhxNd22WZiJHQ6ain1Kz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 858,
      "cache_read_input_tokens": 12165,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 858,
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

_source line 15 · 2026-05-19T09:27:30.536Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016J4XMG5gUWRUMoj6iV27zy`</summary>

```json
{
  "url": "https://arxiv.org/abs/2503.24191",
  "prompt": "Extract ALL information from this arXiv abstract page: full title, all authors, full abstract text, submission dates, revision history, all categories, and any other metadata. Be complete - capture every detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb4256f0-d5df-4205-932e-46d78a7d635b",
  "isSidechain": true,
  "agentId": "aba53dbf8214eeda6",
  "requestId": "req_011CbBgxCf5ZJjk34XGvqoxg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5db11813-ecdb-4586-b256-e9040d628dde",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WCMhxNd22WZiJHQ6ain1Kz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 858,
      "cache_read_input_tokens": 12165,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 858
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 12165,
          "cache_creation_input_tokens": 858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 858,
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

_source line 16 · 2026-05-19T09:27:36.485Z_

<details><summary>↩ Tool result · `toolu_016J4XMG5gUWRUMoj6iV27zy`</summary>

```text
# arXiv Paper Extraction: 2503.24191

## Title
"Beyond Prompts: Space-Time Decoupling Control-Plane Jailbreaks in LLM Structured Output"

## Authors
Shuoming Zhang, Jiacheng Zhao, Hanyuan Dong, Ruiyuan Xu, Zhicheng Li, Yangyu Zhang, Shuaijiang Li, Yuan Wen, Chunwei Xia, Zheng Wang, Xiaobing Feng, Huimin Cui

## Abstract Summary
The paper introduces Constrained Decoding Attack (CDA), a novel jailbreak technique targeting structured output APIs in large language models. Unlike conventional prompt-based attacks, CDA embeds harmful content within schema-level grammar rules while keeping surface prompts benign. Two proof-of-concept attacks are presented: EnumAttack (embedding malicious content in enumeration fields) and DictAttack (distributing payloads across prompts and dictionary-based grammars). Testing across 13 models showed DictAttack achieving "94.3--99.5% ASR across five benchmarks" on certain GPT and other models, with 75.8% effectiveness even against guardrails.

## Submission Information
- **Original submission:** March 31, 2025
- **Latest revision:** January 5, 2026 (version 2)
- **arXiv identifier:** 2503.24191

## Categories
- Cryptography and Security (cs.CR)
- Artificial Intelligence (cs.AI)

## Additional Metadata
- **Paper length:** 15 pages, 9 figures, 8 tables
- **License:** CC BY 4.0
- **DOI:** https://doi.org/10.48550/arXiv.2503.24191
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5db11813-ecdb-4586-b256-e9040d628dde",
  "isSidechain": true,
  "promptId": "a8927760-54f5-4249-ad03-f69ac6716d84",
  "agentId": "aba53dbf8214eeda6",
  "type": "user",
  "uuid": "b52c6ead-64be-45dc-a69d-003a6508a12f",
  "sourceToolAssistantUUID": "5db11813-ecdb-4586-b256-e9040d628dde",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T09:27:45.218Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NEfAPtNzwaHpXf5ELTCxWr`</summary>

```json
{
  "url": "https://arxiv.org/html/2503.24191",
  "prompt": "Extract the FULL content of this paper in maximum detail. I need:\n\n1. The complete abstract verbatim\n2. The full Introduction section - what problem they identify, what is the \"control plane\" vs \"data plane\" distinction\n3. The full methodology: How exactly do EnumAttack and DictAttack work? What is \"Space-Time Decoupling\"? What does \"control plane jailbreak\" mean precisely?\n4. All experimental results: Which 13 models were tested? What were the exact ASR numbers for each model? What benchmarks were used?\n5. The specific evidence/analysis of WHY constrained decoding suppresses refusal - any mechanistic explanation they provide\n6. Discussion of how this relates to tool-call generation and agent frameworks\n7. Defense analysis - what defenses were tested and how effective were they?\n8. All figures and tables descriptions\n\nBe as thorough and detailed as possible. Extract actual numbers, actual model names, actual methodology details. Do not summarize - give me the full details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b52c6ead-64be-45dc-a69d-003a6508a12f",
  "isSidechain": true,
  "agentId": "aba53dbf8214eeda6",
  "requestId": "req_011CbBgxy4JE5bUg3sJGxwu7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "352b6dcd-3a03-4424-a31d-1b797d915429",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAPdQJDh1YUri9yXQ3RNoe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 569,
      "cache_read_input_tokens": 13023,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 569
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 308,
          "cache_read_input_tokens": 13023,
          "cache_creation_input_tokens": 569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 569,
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

_source line 18 · 2026-05-19T09:29:07.939Z_

<details><summary>↩ Tool result · `toolu_01NEfAPtNzwaHpXf5ELTCxWr`</summary>

````text
# Comprehensive Extraction: "Beyond Prompts: Space–Time Decoupling Control-Plane Jailbreaks in LLM Structured Output"

## 1. COMPLETE ABSTRACT

"Large Language Models (LLMs) are extensively used as tooling platforms through structured output APIs to ensure syntax compliance so that robust integration with existing software, like agent systems, can be achieved. However, the feature enabling the functionality of grammar-guided structured output presents significant security vulnerabilities. In this work, we reveal a critical control-plane attack surface orthogonal to traditional data-plane vulnerabilities. We introduce Constrained Decoding Attack (CDA), a novel jailbreak class that weaponizes structured output constraints to bypass both external auditing and internal safety alignment. Unlike prior attacks focused on input prompt designs, CDA operates by embedding malicious intent in schema-level grammar rules (control-plane) while maintaining benign surface prompts (data-plane). We instantiate this with two proof-of-concept attacks: EnumAttack, which embeds malicious content in enum fields; and the more evasive DictAttack, which decouples the malicious payload across a benign prompt and a dictionary-based grammar. Our evaluation spans a broad spectrum of 13 proprietary/open-weight models. In particular, DictAttack achieves 94.3–99.5% ASR across five benchmarks on gpt-5, gemini-2.5-pro, deepseek-r1, and gpt-oss-120b. Furthermore, we demonstrate the significant challenge in defending against these threats: while basic grammar auditing mitigates EnumAttack, the more sophisticated DictAttack maintains a 75.8% ASR even against multiple state-of-the-art jailbreak guardrails. This exposes a critical "semantic gap" in current safety architectures and underscores the urgent need for cross-plane defenses that can bridge the data and control planes to secure the LLM generation pipeline."

---

## 2. INTRODUCTION: PROBLEM IDENTIFICATION & CONCEPTUAL FRAMEWORK

### Core Problem Identified

The paper reveals that modern LLM deployments rely heavily on **structured output** mechanisms to generate formatted, syntactically-compliant outputs. These mechanisms use **constrained decoding**—grammar-guided generation that masks invalid tokens during inference. While this ensures reliable tool integration and function calling, it introduces a novel attack vector previously unexamined in jailbreak literature.

### Data Plane vs. Control Plane Distinction

The authors formalize two orthogonal dimensions of LLM generation:

**Data Plane**: "The standard LLM query–response process. Specifically, a prompt is passed to the LLM, which then generates a text response." This includes both the model's internal safety alignment and external guardrails (classifiers, content filters) that operate on prompts/outputs.

**Control Plane**: "The formatting constraints, or grammars, that guide structured outputs. These constraints are enforced after generation through the model's logit processor, meaning the LLM itself is unaware of them. The control plane supervises generation with user-defined hard rules, such as requiring outputs to match a JSON schema."

### The Conceptual Insight

Traditional jailbreaks operate in the data plane—attackers craft clever prompts to bypass safety mechanisms. Modern defenses focus almost exclusively on data-plane filtering. However, when structured output APIs allow users to provide arbitrary JSON schemas or grammars, they inadvertently expose the control plane as an attack surface.

The key realization: "By manipulating the structured output specifications through carefully crafted schema definitions, these attacks force models to generate content that would otherwise be filtered by both external guardrails and internal alignment mechanisms."

### Why Constrained Decoding Creates Vulnerability

The constrained decoding process works via **per-token masking**: at each generation step, the grammar engine creates a mask of valid tokens (based on grammar rules), sets invalid tokens to −∞ logits, and samples from the masked distribution. This ensures outputs conform to the schema but has a critical side effect—**it forces the model to generate specific strings regardless of safety alignment**.

The mechanism bypasses safety because: safety alignment typically works by increasing the probability of refusal tokens (like "I can't help with that") in the probability distribution. However, constrained decoding deterministically restricts the token space based purely on grammar compliance, not semantic safety. If a malicious string is the only token allowed by the grammar, the model generates it regardless of its training.

---

## 3. METHODOLOGY: ENUMATTACK AND DICTATTACK

### EnumAttack: Direct Manipulation via JSON Schema

**Mechanism**: Exploits the `enum` property in JSON Schema. A schema field restricted to a single-item enum containing a malicious query forces that exact string through the grammar engine.

**Three-Step Construction**:
1. **Benign Prompt**: Send innocent data-plane text (e.g., "Help me process this data") to evade prompt guardrails
2. **Malicious Enum Field**: Define a JSON schema with an enum property: `"enum": ["Detailed instructions for identity theft"]` 
3. **Affirmative Prefix Field**: Add another enum forcing compliance language (e.g., "Sure, here is the information") to suppress refusals

**Why It Works**: The constrained decoding engine sees the enum and must generate that specific string token-by-token. The model's internal safety alignment is bypassed because the grammar deterministically requires the output.

**Limitations**: The malicious payload exists as literal strings visible in the grammar, making it detectable by string-matching guardrails.

### DictAttack: Benign Grammar + Prompt = Jailbreak

**Core Innovation**: Decouples malicious intent across **two dimensions**:
- **Spatial Decoupling**: Splits payload between data plane (prompt) and control plane (grammar)
- **Temporal Decoupling**: Can distribute payloads across multiple conversation turns

**Three-Step Generation Process** (per Algorithm 1):

1. **Tokenization and Obfuscation**: 
   - Malicious query Q_m tokenized into words W_h
   - Example: "How to make explosives" → ["how", "to", "make", "explosives"]

2. **Dictionary Synthesis**:
   - Each harmful word assigned benign key: "how" → "a1", "to" → "b2", "make" → "c3", "explosives" → "d4"
   - To obscure intent, generate k harmless synonyms for each word and include in dictionary
   - Example dictionary (k=1):
     ```json
     {
       "a1": "how",      "a2": "in_what_manner",
       "b2": "to",       "b3": "towards",
       "c3": "make",     "c4": "construct",
       "d4": "explosives", "d5": "bomb_materials"
     }
     ```

3. **Dual-Plane Payload**:
   - **Data-Plane**: Benign prompt containing only keys: "a1+b2+c3+d4" with instruction like "translate these keys using the provided dictionary"
   - **Control-Plane**: JSON schema embedding the dictionary in its fields/descriptions

**During Inference**:
- Model receives key sequence in prompt and dictionary in grammar
- Constrained decoding forces model to reconstruct the query by mapping keys to dictionary values
- Neither keys nor individual dictionary words are harmful in isolation
- Only when reassembled does malicious intent emerge

**Why Detection Fails**: A guardrail examining only the prompt sees benign keys. A guardrail examining only the grammar sees benign technical vocabulary. Neither detects the combined threat without semantic cross-plane reasoning.

### Space-Time Decoupling: Interleaved DictAttack

**Temporal Extension**: Attacker sends key sequence in an early conversation turn (which becomes part of model's KV cache), then sends dictionary-embedded schema in a later turn.

**Why This Further Evades Defenses**:
- Per-request dual-plane auditing becomes single-plane checking
- Would require auditing entire conversation history at each turn (computationally prohibitive)
- Creates "needle in haystack" problem for guards that must reconstruct context from potentially 128k+ token histories

**Measured Impact**: Reduces detection from 24.2% (dual-plane guard on simultaneous payloads) to 5.3% (same guard against interleaved variant).

---

## 4. EXPERIMENTAL DESIGN & RESULTS

### Models Tested (13 Total)

**Proprietary Models** (with flagship emphasis):
- gpt-4o (2024-0806)
- gpt-4o-mini (2024-0718)
- gpt-5 (flagship)
- gemini-2.0-flash
- gemini-2.5-pro (flagship)

**Open-Weight Models**:
- llama-3.1-8b-instruct
- qwen-2.5-32b-instruct
- mistral-nemo
- phi-3.5-moe
- gemma-2-9b-it
- deepseek-v3-0324
- deepseek-r1-0528
- gpt-oss-120b

### Benchmarks (6 datasets)

| Dataset | Size | Categories | Special Properties |
|---------|------|-----------|-------------------|
| AdvBench | 520 | General | — |
| StrongREJECT | 311 | 6 categories | — |
| JailbreakBench | 100 | 10 categories | — |
| HarmBench | 100 | 3 categories | — |
| SorryBench | 440 | 44 categories | 21 attack variants |
| JBShield | 850 | — | 9 attack variants |

### Exact ASR Results

#### EnumAttack Results (Table 2)

On AdvBench with JBShield prompt guard:
- phi-3.5-moe: 99.2%
- mistral-nemo: 100.0%
- qwen-2.5-32b: 99.0%
- llama-3.1-8b: 99.2%
- gemma-2-9b: 98.6%
- deepseek-v3: 98.7%
- gpt-4o: 100.0%
- gpt-4o-mini: 99.0%
- gemini-2.0-flash: 95.8%

**Key Finding**: ASR identical with/without prompt guard (showing complete bypass of data-plane defenses).

#### DictAttack Results on Mainstream Models (Table 4)

**gpt-4o**:
- AdvBench: 98.1% (with guard) / 99.8% (without)
- HarmBench: 98.3% / 100.0%
- JailbreakBench: 98.3% / 100.0%
- SorryBench: 96.9% / 98.6%
- StrongREJECT: 96.7% / 98.4%

**gpt-4o-mini**:
- AdvBench: 95.5% / 97.1%
- HarmBench: 83.6% / 85.0%
- JailbreakBench: 92.4% / 94.0%
- SorryBench: 83.8% / 85.2%
- StrongREJECT: 69.4% / 70.6%

**gemini-2.0-flash**:
- AdvBench: 96.8% / 98.5%
- HarmBench: 97.3% / 99.0%
- JailbreakBench: 89.5% / 91.0%
- SorryBench: 93.9% / 95.5%
- StrongREJECT: 91.4% / 93.0%

#### DictAttack on Flagship/High-Capability Models (Table 5)

**gpt-5**:
- AdvBench: 94.4% (with guard) / 96.0%
- HarmBench: 90.4% / 92.0%
- JailbreakBench: 93.4% / 95.0%
- SorryBench: 91.6% / 93.2%
- StrongREJECT: 93.9% / 95.5%

**gemini-2.5-pro**:
- AdvBench: 97.5% / 99.2%
- HarmBench: 98.3% / 100.0%
- JailbreakBench: 98.3% / 100.0%
- SorryBench: 97.6% / 99.3%
- StrongREJECT: 97.3% / 99.0%

**deepseek-r1**:
- AdvBench: 97.2% / 98.9%
- HarmBench: 93.4% / 95.0%
- JailbreakBench: 95.4% / 97.0%
- SorryBench: 96.9% / 98.6%
- StrongREJECT: 96.4% / 98.1%

**gpt-oss-120b**:
- AdvBench: 96.6% / 98.3%
- HarmBench: 90.4% / 92.0%
- JailbreakBench: 89.4% / 91.0%
- SorryBench: 94.8% / 96.4%
- StrongREJECT: 94.2% / 95.8%

**Summary**: Average DictAttack ASR across flagship models is 94.3-99.5% (near-perfect success).

#### Comparison to SOTA Data-Plane Attacks (Table 6)

Against gpt-4o on AdvBench:
- PAIR: 11.5% ASR undefended, 1.6% with guard
- TAP: 24.4% undefended, 0.4% with guard
- AutoDAN-Turbo: 96.0% undefended, 26.0% with guard
- **DictAttack: 99.8% undefended, 75.8% with dual-plane guard**

### Defense Evaluation Results

#### Table 3: EnumAttack vs. JBShield on llama-3.1-8b

Baseline attacks (data-plane, AdvBench):
- IJP: 0.85% ASR with JBShield (48.9% without)
- DrAttack: 0% with JBShield (65.9% without)
- Puzzler: 0% with JBShield (100% without)
- Zulu: 0% with JBShield (2.7% without)
- Base64: 0.82% with JBShield (8.4% without)

**EnumAttack**: 
- ASR identical with/without JBShield (completely bypasses it)

#### Table 7: Detection Rates Under Different Guards (AdvBench)

**Defense 1 (Grammar-Only)**:
- EnumAttack detection: 97.7% (llamaguard), 90.2% (Moderation), 100.0% (gpt-4o)
- DictAttack (k=0): 6.5%, 0.0%, 17.7%
- DictAttack (k=1): 1.7%, 0.0%, 8.1%
- DictAttack (k=10): 1.5%, 0.0%, 5.3%

**Defense 2 (Dual-Plane Guard, SelfDefend-based)**:
- DictAttack (simultaneous payloads): 28.6% (llamaguard), 0.2% (Moderation), 24.2% (gpt-4o)
- **Interleaved DictAttack**: 1.5% (llamaguard), 0.0% (Moderation), 5.3% (gpt-4o)

**Key Finding**: Grammar-only guard achieves 97.7% detection of EnumAttack but only 1.7% of DictAttack. Dual-plane guard improves detection to 24.2% but Interleaved variant reduces to 5.3%.

### Infrastructure Sensitivity (Figure 5)

Tested combinations:
- Grammar backends: xgrammar, outlines
- Serving frameworks: vLLM 0.10.1, SGLang 0.4.10

**Result**: EnumAttack achieves ~99-100% ASR across all four combinations, demonstrating vulnerability is backend-agnostic.

### Baseline Results (Undefended Models)

- AdvBench: 1.2% ASR on gpt-4o (showing strong baseline safety)
- Average across benchmarks: 6.7-38.7% ASR

---

## 5. MECHANISTIC ANALYSIS: WHY CONSTRAINED DECODING SUPPRESSES REFUSAL

### Token Distribution Analysis (Figures 7-8)

The authors conducted case study using **phi-3.5-moe**, examining token probability distributions across seven progressive attack stages:

1. **Direct Prompt**: Refusal tokens achieve ~100% probability
   - Model strongly refuses harmful request

2. **Yes-Prefix**: Minimal impact
   - Refusal tokens remain ~90% probable
   - Safety alignment strongly suppresses jailbreak tokens

3. **JSON Format**: Refusal probability drops ~50%
   - Structured output constraint begins affecting alignment

4. **EnumAttack**: Refusal tokens disappear
   - Safe tokens remain highly probable (~70%)
   - Jailbreak tokens possible but not dominant

5. **System Prompt Injection**: Refusal/safe tokens suppressed
   - Jailbreak tokens become most likely

6. **Chain EnumAttack**: Complete alignment breakdown
   - Top-5 generation beams are all jailbreak tokens
   - Model fully compromised

7. **Chained Steps**: Permanent alignment collapse
   - Continued degradation through multi-turn attacks

### Quantitative Shift (Figure 8)

Token proportion evolution:
- **Normal state**: 90% refusal tokens, 8% safe, 2% jailbreak
- **After EnumAttack**: Refusal tokens eliminated
- **Final state**: Balanced distribution with jailbreak tokens dominant (no token type dominating)

### Mechanistic Explanation Provided

The authors argue: "While pre-trained LLMs naturally exhibit a diverse and open-ended token distribution, safety alignment artificially distorts this space by forcing refusal tokens to dominate when harmful intents are detected. By imposing structured constraints that fall outside the model's safety-aligned training distribution, CDAs allow the generation process to 'escape' these artificial refusal peaks. Consequently, the distribution reverts from a safety-aligned state (dominated by refusal tokens, ¿90%) to a balanced, context-sensitive state, restoring the model's original open-ended generation capacity."

They further note alignment is "only a few tokens deep" (consistent with deepalignment research). By using grammar to force specific initial tokens (affirmative prefixes, malicious queries), CDAs "bypass this shallow layer of internal resistance."

**Critical Insight**: Safety alignment primarily works by steering token selection at the response's start. Once constrained decoding forces specific initial tokens (via enum fields or dictionary reconstruction), the model's subsequent generation behaves as if no alignment exists—the safety mechanism has been circumvented through forced initial context rather than through genuine model reasoning.

---

## 6. RELATIONSHIP TO TOOL-CALL GENERATION & AGENT FRAMEWORKS

### Context for Structured Output Deployment

The paper emphasizes that structured output has become essential for agent frameworks:

"Beyond standalone chatbots, LLMs are increasingly integrated into complex agent frameworks (langchain; langgraph) and enterprise automation pipelines (mcp2025website; cursor_ide) where they function as core reasoning engines. In these agentic workflows (e.g., Cursor, LangChain, and Model Context Protocol), a service component or an agent backend often supplies a grammar—typically a JSON schema—to a hosted LLM to ensure structured and reliable outputs."

### Specific Use Cases at Risk

1. **Function Calling**: Agents provide JSON schemas defining available functions with parameters. DictAttack could force malicious function calls.

2. **Code Generation**: Grammar constraints ensure syntactic validity. Attackers could hide code injection in schema-level structures.

3. **API Integration**: Structured outputs enable reliable tool interaction. A compromised schema could force unintended API invocations.

### Why Tool-Calling Amplifies Risk

Traditional jailbreaks produce harmful text—the user can ignore it. But structured output jailbreaks force specific API calls, function parameters, or tool invocations that execute automatically in agent pipelines. This transforms jailbreaks from information leaks into **actionable exploits** that directly manipulate external systems.

---

## 7. DEFENSE ANALYSIS & EFFECTIVENESS EVALUATION

### Tested Defense Mechanisms

#### Industrial Guardrails
- **llama-guard-3-8b**: String-based filtering on prompts and outputs
- **OpenAI Moderation API**: Content classification system

#### SOTA Academic Defenses
- **JBShield**: Lightweight defense using static attack profiles
- **SelfDefend**: LLM-based auditing system examining responses for jailbreak indicators

#### Dual-Plane Guard
- Adapted SelfDefend to jointly audit prompt and grammar simultaneously
- Uses gpt-4o as auditing LLM

### Effectiveness Against EnumAttack

**Grammar-Only Guard (llama-guard-3-8b)**:
- Detection rate: 97.7%
- ASR reduction: 100% → 3.4% (near-complete mitigation)

**Simple string matching suffices** because enum fields contain literal malicious strings.

### Effectiveness Against DictAttack

**Grammar-Only Guard**:
- Detection rate: 1.7% (k=1) to 6.5% (k=0)
- ASR reduction: 99.8% → 98.1% (minimal impact)
- **Reason**: Dictionary contains only benign words; no suspicious strings to detect

**Dual-Plane Guard (simultaneous payloads)**:
- Detection rate: 24.2% (gpt-4o), 28.6% (llamaguard)
- ASR reduction: 99.8% → 75.8% (35% reduction)
- **Limitation**: LLM auditor struggles to semantically reconstruct query from distributed components; complex JSON schemas defeat reasoning

**Dual-Plane Guard (interleaved payloads)**:
- Detection rate: 5.3% (gpt-4o)
- ASR reduction: 99.8% → 75.8% (identical to simultaneous due to full conversation auditing failure)
- **Critical Problem**: Would require auditing entire 128k-token history at each turn; computationally prohibitive

### Why Defenses Fail

1. **Single-Plane Myopia**: Prompt guardrails see benign keys; grammar guardrails see benign dictionary
2. **Semantic Complexity**: Complex JSON schemas exceed reasoning capability of lightweight guard models
3. **Temporal Coupling**: Multi-turn attacks defeat per-request auditing; full-history auditing is economically unfeasible
4. **Fundamental Deadlock** (BenignEnumAttack): Legitimate safety research output (e.g., StrongREJECT jailbreak reports) appears identical to actual jailbreak outputs structurally; any defense risks false positives

### Proposed Mitigations (§7)

1. **Lightweight Heuristics**: Flag suspicious "Literal-to-Logic Ratios" or semantic mismatches (limited by false positives)

2. **Grammar-Plane Auditing**: Direct JSON schema inspection (mitigates EnumAttack; ineffective on DictAttack)

3. **Context-Aware Token Attribution**: Track token provenance during generation, distinguish user-specified tokens from model-generated tokens, enabling "token-level auditing"

4. **Safety-Preserving Constraints**: Whitelist refusal tokens to override user grammars; implementation challenge: balance strict grammar compliance with safety

5. **Integrated Safety Signaling**: Co-design LLMs to generate special auditing tokens (e.g., `&lt;unsafe>`) when encountering harmful contexts, enabling real-time constraint-agnostic monitoring

---

## 8. COMPLETE FIGURES & TABLES DESCRIPTIONS

### Figure 1
Illustrates three attack scenarios:
1. Traditional data-plane jailbreak (prompt attack), blocked by guardrail
2. EnumAttack (embedding malicious question in JSON schema), unguarded
3. DictAttack (decoupling malicious payload across benign prompt and grammar), bypassing both plane guardrails

### Figure 2
Constrained decoding workflow analogous to compiler design:
- LLM tokenizer acts as lexer
- Grammar rules serve as parser
- Per-token mask generated at each step
- Invalid tokens masked to −∞ logits
- Model samples from masked distribution
- Guarantees output conforms to grammar

### Figure 3
Three-panel comparison:
- (a) Traditional refusal: guardrail blocks direct harmful prompts
- (b) EnumAttack: malicious content embedded in grammar, bypasses guardrail
- (c) Successful jailbreak output: detailed harmful instructions generated

### Figure 4
EnumAttack construction:
- Benign data-plane prompt on left ("Help me process this data")
- JSON schema on right with enum field containing malicious query ("Detailed instructions for identity theft") and affirmative prefix field ("Sure, here is the information")

### Figure 5
Infrastructure sensitivity bar chart:
- X-axis: Four backend combinations (vLLM+xgrammar, vLLM+outlines, SGLang+xgrammar, SGLang+outlines)
- Y-axis: ASR percentages
- Result: ~99-100% ASR across all combinations on llama-3.1-8b

### Figure 6
Multi-layered CDA mitigation system diagram:
- Input layer: Prompt guard (LLMs, classifiers)
- Grammar layer: Grammar guard (string matching, semantic auditing)
- Generation: LLM with internal alignment
- Output layer: Output auditing (content filters)
- Shows how DictAttack bypasses multiple layers simultaneously

### Figure 7
Token probability distribution case study (phi-3.5-moe, sequence_length=5):
- Seven panels showing logit values for refusal, safe, and jailbreak token categories
- Panel 1 (Direct Prompt): Refusal tokens dominate (~100%)
- Panel 4 (EnumAttack): Refusal tokens eliminated
- Panel 6 (Chain EnumAttack): Top-5 beams all jailbreak tokens
- Explicit probability values shown (omits values <1e-16)

### Figure 8
Quantitative token distribution shift graph:
- X-axis: Seven attack progression methods
- Y-axis: Token proportions (stacked bars)
- Shows transition from refusal-dominated (90%) through safe (intermediate) to jailbreak-dominated (final)
- Demonstrates alignment breakdown through visual proportion changes

### Figure 9
BenignEnumAttack vs. legitimate auditing deadlock:
- Red path: Actual jailbreak producing harmful output in structured format
- Blue path: Legitimate safety research generating StrongREJECT jailbreak report
- Both produce identical structural outputs
- Illustrates fundamental detection ambiguity: auditor must either false-positive (reject safety research) or false-negative (leak jailbreak)

### Table 1
Datasets summary:
- 6 benchmarks with sizes 100-850
- Categories range from general (AdvBench) to 44-category (SorryBench)
- Special properties include extra attacks and variants

### Table 2
EnumAttack ASR on AdvBench (520 prompts):
- Nine models tested
- ASRs range 95.8-100%
- Identical results with/without prompt guard (showing complete bypass)

### Table 3
Comparison on llama-3.1-8b with JBShield:
- Five baseline attacks: all reduced to 0-0.85% ASR with guard
- EnumAttack: identical ASR with/without guard (~47-74% depending on dataset)
- Shows baseline attacks are well-defended; EnumAttack evades completely

### Table 4
DictAttack on mainstream models (gpt-4o, gpt-4o-mini, gemini-2.0-flash):
- Five benchmarks tested
- Values shown as "with guard (without guard)"
- gpt-4o: 96.7-99.8% ASR range
- gpt-4o-mini: Lower performance (~69-97%)
- gemini-2.0-flash: 89.5-99.0% range
- Grammar guard has minimal impact (1-3% reduction)

### Table 5
DictAttack on flagship models (gpt-5, gemini-2.5-pro, deepseek-r1, gpt-oss-120b):
- Five benchmarks: Adv, Harm, JB, Sorry, SR
- Column values: "with guard/without guard"
- All models: 90.4-99.2% ASR range
- Demonstrates vulnerability persists in latest, most-aligned models

### Table 6
SOTA comparison on gpt-4o AdvBench:
- PAIR: 11.5% → 1.6% (effective defense)
- TAP: 24.4% → 0.4% (effective defense)
- AutoDAN-Turbo: 96.0% → 26.0% (significant reduction)
- DictAttack: 99.8% → 75.8% (minimal reduction, marked with asterisk)
- Asterisk note: DictAttack uses dual-plane guard; others use best data-plane guard
- Demonstrates fundamental gap between traditional and control-plane defenses

### Table 7
Detection rates on AdvBench under two defense policies:
- Defense 1 (Grammar-only): EnumAttack 97.7-100%, DictAttack 1.5-6.5%
- Defense 2 (Dual-plane): DictAttack 24.2%, Interleaved DictAttack 5.3%
- Three guard types tested: llamaguard, Moderation API, gpt-4o
- Shows synthesis ratio k increases → detection decreases
- Interleaved variant drastically reduces detectability

### Table 8
Extended jailbreak taxonomy table:
- Categorizes 18+ attack methods across 6 categories
- New category added: "Output-based" (CDAs)
- Distinguishes white-box (∘) vs. black-box (∙) attacks
- Notes target LLM query counts and whether attacks target input or output
- EnumAttack and DictAttack positioned in output-based category with ~1 query requirement

---

## CRITICAL QUANTITATIVE SUMMARY

**Attack Effectiveness**:
- EnumAttack: 95.8-100% ASR across all 13 models
- DictAttack: 90.4-99.8% ASR, with 94.3-99.5% average on flagship models

**Defense Bypass Rates**:
- EnumAttack vs. grammar guard: 97.7% detection (mostly mitigated)
- DictAttack vs. grammar-only guard: 1.7% detection (nearly complete bypass)
- DictAttack vs. dual-plane guard: 24.2% detection (still majority bypass)
- Interleaved DictAttack vs. dual-plane guard: 5.3% detection (defeats practical defenses)

**Benchmark Coverage**: 2,421 total test cases across six standard jailbreak benchmarks

**Models at Risk**: All 13 tested models remain vulnerable; no model showed strong resistance to DictAttack
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "352b6dcd-3a03-4424-a31d-1b797d915429",
  "isSidechain": true,
  "promptId": "a8927760-54f5-4249-ad03-f69ac6716d84",
  "agentId": "aba53dbf8214eeda6",
  "type": "user",
  "uuid": "04134b23-8405-496f-a0b0-8105382e228d",
  "sourceToolAssistantUUID": "352b6dcd-3a03-4424-a31d-1b797d915429",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-19T09:29:10.903Z_

Now let me search for additional context on the mechanistic explanation and the relationship to tool-call generation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04134b23-8405-496f-a0b0-8105382e228d",
  "isSidechain": true,
  "agentId": "aba53dbf8214eeda6",
  "requestId": "req_011CbBh5i7KibHTUWzPj9Kqd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a69307ec-e7b8-426e-85db-4e79ccca7628",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQs1s5sLFAcrQPVkajm26u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7976,
      "cache_read_input_tokens": 13592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7976,
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

_source line 20 · 2026-05-19T09:29:14.203Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012LShuzLcpFgETkBLkx8d44`</summary>

```json
{
  "url": "https://www.themoonlight.io/en/review/output-constraints-as-attack-surface-exploiting-structured-generation-to-bypass-llm-safety-mechanisms",
  "prompt": "Extract the full literature review content. I need any additional analysis about: 1) the mechanistic explanation for why constrained decoding suppresses safety alignment, 2) how this relates to tool-call/function-call generation, 3) any critique or limitations noted, 4) comparison with other structured output attack papers like the prefix-tree paper (2502.13527). Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a69307ec-e7b8-426e-85db-4e79ccca7628",
  "isSidechain": true,
  "agentId": "aba53dbf8214eeda6",
  "requestId": "req_011CbBh5i7KibHTUWzPj9Kqd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48938110-5b24-4f93-b9b4-078d85132ff1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQs1s5sLFAcrQPVkajm26u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7976,
      "cache_read_input_tokens": 13592,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7976
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 13592,
          "cache_creation_input_tokens": 7976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7976,
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

_source line 21 · 2026-05-19T09:29:26.598Z_

<details><summary>↩ Tool result · `toolu_012LShuzLcpFgETkBLkx8d44`</summary>

```text
# Analysis of "Output Constraints as Attack Surface"

## 1) Mechanistic Explanation for Safety Suppression

The paper explains that constrained decoding bypasses safety mechanisms through several pathways:

**Token Distribution Compromise:** The masking process forces the model to generate from a restricted token set. When harmful enum values are embedded in JSON schemas, the model's logits are modified via the equation: `z'[i] = z[i] if valid; -∞ otherwise`. This mathematically eliminates safe token alternatives.

**Shallow Alignment Exploitation:** The document notes that "current LLM safety mechanisms predominantly protect only the first few tokens of generation." Chain Enum Attack weaponizes this by using a weakly-aligned model to generate harmful prefixes, then forcing a strongly-aligned model to continue those prefixes via grammar constraints. The result is a "cascading failure pattern where subsequent tokens increasingly favor harmful content completion."

**Prompt vs. Grammar Separation:** The key insight is the split between benign input prompts (data plane) and malicious grammar rules (control plane). Since safety auditing focuses on prompts, the attack "bypasses prompt-based guardrails because the attack body is concealed within structured output."

## 2) Relationship to Tool-Call/Function-Call Generation

The paper does **not explicitly discuss** tool-call or function-call APIs. However, the mechanism is directly applicable: any structured output API that constrains generation through grammar—including function signatures and their parameters—would be vulnerable to similar attacks. The paper's JSON schema exploitation suggests that function-call systems using similar constrained decoding would face equivalent risks.

## 3) Critique and Limitations Noted

**Limitations acknowledged:**

- The paper addresses "false positives" and "false negatives" in output auditing through BenignEnumAttack, noting that auditing "is not a silver bullet"
- Output auditing faces practical constraints: "latency, computational cost, and false positives"
- The threat model assumes "API access and grammar-level control"—this may not apply universally

**Proposed mitigations offered:**
- Token whitelisting to prevent user-controlled grammar constraints
- Context-aware token attribution to track provenance
- Integrated safety signaling tokens

The paper does not substantially critique its own methodology or discuss failure cases.

## 4) Comparison with Other Structured Output Attack Papers

**The document does not reference or compare** this work with arxiv:2502.13527 (the prefix-tree paper you mention) or other structured output attack literature beyond briefly categorizing existing jailbreak types. The review provides no comparative analysis with contemporaneous work in this emerging attack surface area.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48938110-5b24-4f93-b9b4-078d85132ff1",
  "isSidechain": true,
  "promptId": "a8927760-54f5-4249-ad03-f69ac6716d84",
  "agentId": "aba53dbf8214eeda6",
  "type": "user",
  "uuid": "2c30754e-7e66-49e3-af20-34dbe876bfc4",
  "sourceToolAssistantUUID": "48938110-5b24-4f93-b9b4-078d85132ff1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T09:29:29.376Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KSCmsz4ZbfneLw173hgxqT`</summary>

```json
{
  "query": "arXiv 2502.13527 prefix-tree structured output jailbreak constrained decoding comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c30754e-7e66-49e3-af20-34dbe876bfc4",
  "isSidechain": true,
  "agentId": "aba53dbf8214eeda6",
  "requestId": "req_011CbBh75wmGzwER3GmTZi4Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c873a6af-0c40-45a0-8802-2190fc6e440e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RYy22hAZiYMAQvJwizrScB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 916,
      "cache_read_input_tokens": 21568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 916,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 23 · 2026-05-19T09:29:36.320Z_

<details><summary>↩ Tool result · `toolu_01KSCmsz4ZbfneLw173hgxqT`</summary>

```text
Web search results for query: "arXiv 2502.13527 prefix-tree structured output jailbreak constrained decoding comparison"

Links: [{"title":"[2502.13527] Exploiting Prefix-Tree in Structured Output Interfaces for Enhancing Jailbreak Attacking","url":"https://arxiv.org/abs/2502.13527"},{"title":"Exploiting Prefix-Tree in Structured Output Interfaces for Enhancing Jailbreak Attacking","url":"https://powerdrill.ai/discover/summary-exploiting-prefix-tree-in-structured-output-cm7dttucq6o1907pgyfwxx86y"},{"title":"Exploiting Prefix-Tree in Structured Output Interfaces for Enhancing","url":"https://arxiv.org/pdf/2502.13527"},{"title":"Exploiting Prefix-Tree in Structured Output Interfaces for Enhancing Jailbreak Attacking","url":"https://arxiv.org/html/2502.13527"},{"title":"Exploiting Prefix-Tree in Structured Output Interfaces for Enhancing Jailbreak Attacking | Read Paper on Bytez","url":"https://bytez.com/docs/arxiv/2502.13527/paper"},{"title":"Sockpuppetting: Jailbreaking LLMs Without Optimization Through Output Prefix Injection","url":"https://arxiv.org/pdf/2601.13359"},{"title":"Output Constraints as Attack Surface: Exploiting Structured Generation to Bypass LLM Safety Mechanisms","url":"https://arxiv.org/html/2503.24191v1"},{"title":"Prefix Guidance: A Steering Wheel for Large Language Models to Defend   Against Jailbreak Attacks","url":"https://arxiv.org/pdf/2408.08924"}]

Based on the search results, I found the paper you're looking for:

## Paper Summary

arXiv paper 2502.13527 is titled "Exploiting Prefix-Tree in Structured Output Interfaces for Enhancing Jailbreak Attacking", submitted on February 19, 2025.

**Main Contribution:**
The paper reveals a new threat model targeting structured output interfaces that enable attackers to manipulate the inner logit during LLM generation with only API access permissions. The authors introduce a black-box attack framework called AttackPrefixTree (APT) that exploits structured output interfaces to dynamically construct attack patterns.

**Key Findings:**
By leveraging prefixes of models' safety refusal responses and latent harmful outputs, APT effectively bypasses safety measures. The paper also evaluates the attack on reasoning models and shows results on benchmarks like JailbreakBench and HarmBench.

The research highlights a critical vulnerability in structured output interfaces—a security mechanism designed to constrain model outputs—which can paradoxically be exploited to enhance jailbreak attacks by manipulating the underlying token probabilities during generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c873a6af-0c40-45a0-8802-2190fc6e440e",
  "isSidechain": true,
  "promptId": "a8927760-54f5-4249-ad03-f69ac6716d84",
  "agentId": "aba53dbf8214eeda6",
  "type": "user",
  "uuid": "89d23c79-7f6d-4c2b-bed5-07a67cf630b1",
  "sourceToolAssistantUUID": "c873a6af-0c40-45a0-8802-2190fc6e440e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T09:29:39.325Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TGvYVh7Ug8vBYZsRwpeEAC`</summary>

```json
{
  "query": "\"constrained decoding\" \"safety alignment\" mechanistic explanation refusal suppression token probability structured output 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89d23c79-7f6d-4c2b-bed5-07a67cf630b1",
  "isSidechain": true,
  "agentId": "aba53dbf8214eeda6",
  "requestId": "req_011CbBh7oNPZ7sTcb2Ltt3kS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77673d9f-3bf9-440e-8178-2578a00e65a5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XhvVWLUNfEFdqSUGPSs9MM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 789,
      "cache_read_input_tokens": 22484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 789,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
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

_source line 25 · 2026-05-19T09:29:51.118Z_

<details><summary>↩ Tool result · `toolu_01TGvYVh7Ug8vBYZsRwpeEAC`</summary>

```text
Web search results for query: ""constrained decoding" "safety alignment" mechanistic explanation refusal suppression token probability structured output 2025 2026"

Links: [{"title":"Output Constraints as Attack Surface: Exploiting Structured Generation to Bypass LLM Safety Mechanisms","url":"https://arxiv.org/html/2503.24191v1"},{"title":"Constrained Decoding Mechanism","url":"https://www.emergentmind.com/topics/constrained-decoding-mechanism"},{"title":"Correctness-Guaranteed Code Generation via Constrained Decoding","url":"https://arxiv.org/html/2508.15866v1"},{"title":"A Guide to Structured Outputs Using Constrained Decoding","url":"https://www.aidancooper.co.uk/constrained-decoding/"},{"title":"Vulnerability Constrained Decoding","url":"https://www.catalyzex.com/s/Vulnerability%20Constrained%20Decoding"},{"title":"Refusal Falls off a Cliff: How Safety Alignment Fails in Reasoning?","url":"https://arxiv.org/pdf/2510.06036"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"Alignment-Enhanced Decoding: Defending via Token-Level Adaptive Refining of Probability Distributions WARNING: This paper contains harmful content that can be offensive.","url":"https://arxiv.org/html/2408.07663"}]

I've found several highly relevant research papers and resources on constrained decoding and its relationship to safety alignment. Here are the key findings:

## Constrained Decoding Mechanism

Constrained decoding is a class of post-hoc generation algorithms for sequence models that explicitly restricts the output space at each decoding step so that only sequences satisfying user-specified hard or soft constraints can ever be generated. At each decoding step, tokens that violate the constraint have their probability set to 0 in the next-token probability vector output by the LM, and the masked-out probability vector is then renormalized before sampling the next token.

## Safety Alignment and Token Probabilities

Techniques that modify output distribution through constrained decoding demonstrate different behavior patterns, with four distinct token types identified: refusal tokens, safe tokens, weak jailbreak tokens and strong jailbreak tokens, in ascending threat level to conduct jailbreak behaviors.

Recent mechanistic research on refusal has revealed interesting dynamics: Safety-aligned LLMs often undergo shallow safety alignment, where the first few tokens largely determine whether the response will be harmful, with safety-aligned LLMs generating highly similar initial tokens in their refusal responses, which are defined as safety trigger tokens.

Researchers observe a recurrent pattern called the Refusal Cliff, where intermediate reasoning steps yield refusal scores comparable to strongly aligned models but scores drop sharply in final steps, reflecting suppression of refusal behavior even where refusal would be the alignment-consistent choice.

## Potential Vulnerabilities

Direct prompt attacks are mostly ineffective for safety aligned models, but techniques that modify output distribution through constrained decoding demonstrate different behavior patterns.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77673d9f-3bf9-440e-8178-2578a00e65a5",
  "isSidechain": true,
  "promptId": "a8927760-54f5-4249-ad03-f69ac6716d84",
  "agentId": "aba53dbf8214eeda6",
  "type": "user",
  "uuid": "2affb660-b0e8-4f59-b04a-e895fe742a70",
  "sourceToolAssistantUUID": "77673d9f-3bf9-440e-8178-2578a00e65a5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-19T09:31:25.778Z_

Now I have comprehensive information. Let me compile the detailed findings.

---

## Detailed Findings: "Beyond Prompts: Space-Time Decoupling Control-Plane Jailbreaks in LLM Structured Output"

**arXiv ID:** 2503.24191  
**Authors:** Shuoming Zhang, Jiacheng Zhao, Hanyuan Dong, Ruiyuan Xu, Zhicheng Li, Yangyu Zhang, Shuaijiang Li, Yuan Wen, Chunwei Xia, Zheng Wang, Xiaobing Feng, Huimin Cui  
**Original submission:** March 31, 2025 | **Revised:** January 5, 2026 (v2)  
**Categories:** cs.CR (Cryptography and Security), cs.AI  
**Note on title:** The v1 title was "Output Constraints as Attack Surface: Exploiting Structured Generation to Bypass LLM Safety Mechanisms"; v2 adopted the current title.

---

### 1. What Exactly Is "Space-Time Decoupling"? What Are "Control-Plane Jailbreaks"?

**Control-Plane vs. Data-Plane:**

The paper formalizes LLM generation as operating on two orthogonal planes, borrowing networking terminology:

- **Data Plane**: The standard query-response process. The prompt goes in, the model generates text. Both the model's internal safety alignment and external guardrails (classifiers, content filters) operate here. All prior jailbreak research targets this plane.

- **Control Plane**: The formatting constraints/grammars that guide structured output. These constraints are enforced *after* generation through the model's logit processor -- the LLM itself is not aware of them. The control plane supervises generation with user-defined hard rules (e.g., requiring outputs to match a JSON schema). Crucially, when structured output APIs allow users to provide arbitrary JSON schemas or grammars, they expose the control plane as an attack surface.

A **Control-Plane Jailbreak** embeds malicious intent not in the prompt (data plane) but in the schema-level grammar rules (control plane), while keeping the surface prompt completely benign. Because safety auditing focuses overwhelmingly on prompts and outputs, the attack body hidden in the grammar is invisible to standard defenses.

**Space-Time Decoupling** refers to the two axes along which DictAttack distributes its malicious payload:

- **Spatial Decoupling**: The payload is split between the data plane (prompt contains only benign lookup keys like "a1+b2+c3") and the control plane (grammar contains a benign-looking dictionary mapping keys to words). Neither plane contains recognizably harmful content alone.

- **Temporal Decoupling**: The key sequence can be sent in an early conversation turn (becoming part of the KV cache), and the dictionary-embedded schema sent in a later turn. This defeats per-request auditing because no single request contains both halves of the payload.

---

### 2. How Do They Achieve 94.3-99.5% ASR? What Models Were Tested?

**Two Attack Instantiations:**

**EnumAttack** (simpler, detectable): Exploits JSON Schema's `enum` property. A field restricted to a single-item enum containing a malicious query (e.g., `"enum": ["Detailed instructions for identity theft"]`) forces the constrained decoding engine to emit that exact string token-by-token. An additional enum field forces an affirmative prefix (e.g., "Sure, here is the information") to suppress any residual refusal tendency. The data-plane prompt remains innocent. This achieves 95.8-100% ASR across all 13 models but is detectable by grammar-level string matching (97.7% detection rate).

**DictAttack** (sophisticated, evasive): The malicious query is tokenized into words, each assigned a benign key. Harmless synonyms are generated for each word (controlled by parameter k) and included as noise. The dictionary is embedded in the JSON schema. The prompt contains only the key sequence plus an instruction like "translate these keys using the provided dictionary." During inference, constrained decoding forces the model to reconstruct the harmful query by mapping keys to dictionary values. Neither the keys nor individual dictionary words are harmful in isolation.

**13 Models Tested:**

Proprietary: gpt-4o, gpt-4o-mini, gpt-5, gemini-2.0-flash, gemini-2.5-pro  
Open-weight: llama-3.1-8b-instruct, qwen-2.5-32b-instruct, mistral-nemo, phi-3.5-moe, gemma-2-9b-it, deepseek-v3-0324, deepseek-r1-0528, gpt-oss-120b

**DictAttack ASR on Flagship Models (the 94.3-99.5% headline):**

| Model | AdvBench | HarmBench | JailbreakBench | SorryBench | StrongREJECT |
|-------|----------|-----------|----------------|------------|---------------|
| gpt-5 | 94.4% | 90.4% | 93.4% | 91.6% | 93.9% |
| gemini-2.5-pro | 97.5% | 98.3% | 98.3% | 97.6% | 97.3% |
| deepseek-r1 | 97.2% | 93.4% | 95.4% | 96.9% | 96.4% |
| gpt-oss-120b | 96.6% | 90.4% | 89.4% | 94.8% | 94.2% |

(Values shown are with grammar guard; without guard, add ~1.5-2%.)

For comparison, traditional SOTA data-plane attacks on gpt-4o: PAIR achieves 11.5% ASR, TAP 24.4%, AutoDAN-Turbo 96.0% but drops to 26.0% with a guard. DictAttack: 99.8% undefended, 75.8% even against a dual-plane guard.

**6 Benchmarks used:** AdvBench (520), StrongREJECT (311), JailbreakBench (100), HarmBench (100), SorryBench (440), JBShield (850) -- totaling 2,421 test cases.

**Infrastructure-agnostic:** Tested across vLLM and SGLang serving frameworks with xgrammar and outlines grammar backends. ASR ~99-100% across all four combinations.

---

### 3. What Specific Evidence That Constrained Decoding Suppresses Refusal?

This is the mechanistically richest part of the paper. They provide a detailed token probability distribution analysis using phi-3.5-moe, tracking four token categories (refusal, safe, weak-jailbreak, strong-jailbreak) across seven progressive attack stages:

**The Token Distribution Shift (Figures 7-8):**

1. **Direct harmful prompt**: Refusal tokens dominate at ~90-100% probability. Model strongly refuses.
2. **Yes-prefix added**: Minimal impact. Refusal tokens remain ~90%. Safety alignment is robust against simple prefix injection.
3. **JSON format constraint imposed**: Refusal probability drops ~50%. This is the key transition -- merely requiring structured output begins degrading alignment.
4. **EnumAttack**: Refusal tokens *disappear entirely*. Safe tokens remain at ~70%. Jailbreak tokens become possible but not dominant.
5. **System prompt injection added**: Refusal and safe tokens suppressed. Jailbreak tokens become most likely.
6. **Chain EnumAttack**: Complete alignment breakdown. Top-5 generation beams are ALL jailbreak tokens.
7. **Chained multi-turn steps**: Permanent alignment collapse with continued degradation.

**Their Mechanistic Explanation:**

The authors argue that safety alignment "artificially distorts" the natural token distribution by forcing refusal tokens to dominate when harmful intent is detected. Constrained decoding imposes constraints that fall *outside the model's safety-aligned training distribution*, allowing the generation process to "escape" these artificial refusal peaks. The distribution reverts from a safety-aligned state (dominated by refusal tokens, >90%) to a "balanced, context-sensitive state, restoring the model's original open-ended generation capacity."

They further note that alignment is **"only a few tokens deep"** -- safety mechanisms primarily work by steering token selection at the response's start. Once constrained decoding forces specific initial tokens (via enum fields or dictionary reconstruction), subsequent generation behaves as if no alignment exists. The safety mechanism is circumvented through forced initial context rather than genuine model reasoning.

**The formal mechanism:** Constrained decoding applies per-token masking: `z'[i] = z[i] if valid; -inf otherwise`. When a malicious string is the only token sequence allowed by the grammar, the model generates it regardless of its safety training. Refusal tokens (like "I can't help with that") are literally impossible to produce when the grammar does not permit them.

---

### 4. How Does This Relate to Tool-Call Generation Specifically?

The paper explicitly motivates its work in the context of agent frameworks and tool-calling:

> "Beyond standalone chatbots, LLMs are increasingly integrated into complex agent frameworks (LangChain, LangGraph) and enterprise automation pipelines (MCP, Cursor IDE) where they function as core reasoning engines. In these agentic workflows, a service component or agent backend often supplies a grammar -- typically a JSON schema -- to a hosted LLM to ensure structured and reliable outputs."

**Specific tool-call implications identified:**

1. **Function calling**: Agents provide JSON schemas defining available functions with parameters. DictAttack could force malicious function calls by embedding the attack in the schema that constrains the function-call output.

2. **Escalation from text to action**: Traditional jailbreaks produce harmful text that a user can ignore. Structured output jailbreaks force specific API calls, function parameters, or tool invocations that *execute automatically* in agent pipelines. This transforms jailbreaks from information leaks into **actionable exploits** that directly manipulate external systems.

3. **The supply-chain threat**: In agent architectures, the grammar/schema is often supplied by a service component or plugin, not the end user. A compromised or malicious plugin providing schemas could use CDA to hijack the LLM's tool-call generation without the user or the main agent framework being aware.

**Critical gap the paper identifies but does not fully explore:** The paper does not conduct experiments specifically on tool-call/function-call APIs (e.g., OpenAI's function calling, Anthropic's tool use). It demonstrates the vulnerability on generic structured output (JSON schema constrained decoding) and argues the mechanism transfers. This is a significant open question for follow-up work -- whether the specific constrained decoding implementations used in tool-call generation exhibit the same vulnerability, and whether tool-call-specific defenses (like tool approval workflows) provide any additional protection.

---

### 5. Defense Landscape and the "Semantic Gap"

**What defenses were tested and how they fared:**

| Defense | vs. EnumAttack | vs. DictAttack | vs. Interleaved DictAttack |
|---------|---------------|----------------|---------------------------|
| Grammar-only (string matching) | 97.7% detection | 1.7% detection | N/A |
| Dual-plane guard (gpt-4o auditor) | N/A | 24.2% detection | 5.3% detection |
| JBShield (industrial) | 0% impact (complete bypass) | N/A | N/A |
| OpenAI Moderation API | 90.2% on grammar | 0.0% on grammar | 0.0% |

The fundamental problem they identify is the **"semantic gap"**: current safety architectures operate on either the data plane or control plane independently but cannot reason about the *combined* semantics across both planes. DictAttack exploits this by ensuring each plane individually appears benign.

**Proposed but unvalidated mitigations**: (1) Grammar-plane auditing for literal payloads, (2) Context-aware token attribution tracking provenance, (3) Safety-preserving constraints that whitelist refusal tokens, (4) Integrated safety signaling where models emit special `&lt;unsafe>` tokens.

---

### 6. Why This Paper Is the Strongest Empirical Motivation for Studying Refusal During Structured/Tool-Call Output

The paper provides:

1. **Quantitative proof** that constrained decoding eliminates refusal: the token distribution analysis showing refusal probability going from >90% to 0% when grammar constraints are applied.

2. **Scale of evidence**: 13 models, 6 benchmarks, 2,421 test cases, including the latest flagship models (gpt-5, gemini-2.5-pro, deepseek-r1).

3. **Defense futility**: Even the best dual-plane defense only detects 24.2% of attacks, and temporal decoupling reduces that to 5.3%.

4. **The mechanism is fundamental, not model-specific**: The vulnerability stems from how constrained decoding works (per-token masking at the logit level), not from any particular model's alignment weakness. Every model that uses grammar-guided generation is affected.

5. **Direct agent-framework relevance**: The paper explicitly connects to LangChain, MCP, Cursor, and tool-calling workflows where structured output is mandatory.

**What the paper does NOT provide** (and where a mechanistic follow-up study would add value): The paper observes that refusal tokens are eliminated but does not explain *why* at the representation level. They note alignment is "shallow" but do not probe internal model representations (attention patterns, residual stream directions, refusal features) to explain the mechanism. A mechanistic interpretability study could investigate: Do refusal-direction features still activate during constrained decoding but get overridden at the logit level? Or does the constraint itself propagate backward through the model's computation, suppressing refusal features at earlier layers? This is the gap between the empirical observation (this paper) and mechanistic understanding.

---

### Related Work

A companion paper worth noting: [arXiv 2502.13527](https://arxiv.org/abs/2502.13527) "Exploiting Prefix-Tree in Structured Output Interfaces for Enhancing Jailbreak Attacking" (Feb 2025) introduces AttackPrefixTree (APT), a black-box framework that exploits structured output interfaces by leveraging prefixes of safety refusal responses and latent harmful outputs to dynamically construct attack patterns. This approaches the same vulnerability from a different angle (prefix-tree manipulation vs. grammar/schema embedding).

Sources:
- [arXiv Abstract: 2503.24191](https://arxiv.org/abs/2503.24191)
- [arXiv HTML: 2503.24191](https://arxiv.org/html/2503.24191)
- [Literature Review on Moonlight](https://www.themoonlight.io/en/review/output-constraints-as-attack-surface-exploiting-structured-generation-to-bypass-llm-safety-mechanisms)
- [Advanced AI News Coverage](https://advancedainews.com/output-constraints-as-attack-surface-exploiting-structured-generation-to-bypass-llm-safety-mechanisms/)
- [Prefix-Tree Paper: 2502.13527](https://arxiv.org/abs/2502.13527)
- [Emergent Mind: Constrained Decoding Mechanism](https://www.emergentmind.com/topics/constrained-decoding-mechanism)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2affb660-b0e8-4f59-b04a-e895fe742a70",
  "isSidechain": true,
  "agentId": "aba53dbf8214eeda6",
  "requestId": "req_011CbBh8theJuwvkrijRiEEn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d00e4cf-bb5b-489b-810f-297c8c44d5df",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "06627d67-0d68-4ced-a8db-17daf79b8a83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KRYMKMiin2CkJ4ZpePFWBC",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 846,
      "cache_read_input_tokens": 23273,
      "output_tokens": 3729,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 846
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3729,
          "cache_read_input_tokens": 23273,
          "cache_creation_input_tokens": 846,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 846,
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
