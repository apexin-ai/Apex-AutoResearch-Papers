# Research conversation: I need to find and deeply read the paper "CCPS" (arXiv 2505.21772, EMNLP 2025) which achieves ~55% ECE reduction and 21%

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a877e5c2fa3ff03c8.jsonl`
- **Structured JSON:** [`23859d2ffe887330f88f.json`](../../sessions/23/23859d2ffe887330f88f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-19T14:59:49.905Z_

I need to find and deeply read the paper "CCPS" (arXiv 2505.21772, EMNLP 2025) which achieves ~55% ECE reduction and 21% Brier score improvement via perturbation-stability probing across 8B-32B models (Llama, Qwen, Mistral).

Use WebSearch to find this paper, then use WebFetch to read it from arxiv.org (try both the abstract page and the HTML version at https://arxiv.org/html/2505.21772v1 or similar).

I need to understand:
1. What does CCPS stand for?
2. What is the perturbation-stability probing methodology?
3. What specific models and benchmarks were evaluated?
4. What are the key quantitative results (ECE reduction, Brier score improvement)?
5. How does it compare to other calibration methods?
6. Is it training-free or does it require training?
7. What are its limitations?

This is for integrating into a research proposal about competing calibration biases. I need to position CCPS as a landscape reference and potential extended baseline.

Report detailed findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "a877e5c2fa3ff03c8",
  "type": "user",
  "uuid": "b09eb6df-99eb-49cc-a60e-d9901e6abeb1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T14:59:49.910Z_

```json
{
  "parentUuid": "b09eb6df-99eb-49cc-a60e-d9901e6abeb1",
  "isSidechain": true,
  "agentId": "a877e5c2fa3ff03c8",
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
  "uuid": "a7ec4955-e673-4fe3-95fe-268a75a4f9ae",
  "timestamp": "2026-05-19T14:59:49.910Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T14:59:49.911Z_

```json
{
  "parentUuid": "a7ec4955-e673-4fe3-95fe-268a75a4f9ae",
  "isSidechain": true,
  "agentId": "a877e5c2fa3ff03c8",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "282f9472-be1f-4c22-a141-6e646e538b52",
  "timestamp": "2026-05-19T14:59:49.911Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T14:59:53.715Z_



I'll search for this paper and fetch its details. Let me start by loading the necessary tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "282f9472-be1f-4c22-a141-6e646e538b52",
  "isSidechain": true,
  "agentId": "a877e5c2fa3ff03c8",
  "requestId": "req_011CbC8JM1qvMEmBpd1Cy9zt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e4b55f4-4912-4b8a-a0ca-a4718a566867",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AXMHfCk2vN2g1BZDS3jY9R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1582,
      "cache_read_input_tokens": 7409,
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

_source line 5 · 2026-05-19T14:59:54.362Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013RUoD2WMhdUFLzxM71eNAt`</summary>

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
  "parentUuid": "2e4b55f4-4912-4b8a-a0ca-a4718a566867",
  "isSidechain": true,
  "agentId": "a877e5c2fa3ff03c8",
  "requestId": "req_011CbC8JM1qvMEmBpd1Cy9zt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f2a7e82-c761-456f-9df4-9c5e02a6b283",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AXMHfCk2vN2g1BZDS3jY9R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1582,
      "cache_read_input_tokens": 7409,
      "output_tokens": 101,
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
          "output_tokens": 101,
          "cache_read_input_tokens": 7409,
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

_source line 6 · 2026-05-19T14:59:54.365Z_

<details><summary>↩ Tool result · `toolu_013RUoD2WMhdUFLzxM71eNAt`</summary>

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
  "parentUuid": "1f2a7e82-c761-456f-9df4-9c5e02a6b283",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "a877e5c2fa3ff03c8",
  "type": "user",
  "uuid": "b30bf069-0076-4025-bd2c-33d7d6cdfd0d",
  "sourceToolAssistantUUID": "1f2a7e82-c761-456f-9df4-9c5e02a6b283",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T14:59:56.983Z_



Now let me search for the paper and fetch it from multiple sources in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b30bf069-0076-4025-bd2c-33d7d6cdfd0d",
  "isSidechain": true,
  "agentId": "a877e5c2fa3ff03c8",
  "requestId": "req_011CbC8JgHxnrVsYSfYKLaCE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd8a4ce8-6b10-4f47-af3b-f02ab69b84e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DvkssNJ3kXhbbkS6nMULPj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 8991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1123,
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

_source line 8 · 2026-05-19T14:59:57.985Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BwwEg4WkJgbR6ib1NNtwzU`</summary>

```json
{
  "query": "CCPS arXiv 2505.21772 perturbation-stability probing calibration LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd8a4ce8-6b10-4f47-af3b-f02ab69b84e5",
  "isSidechain": true,
  "agentId": "a877e5c2fa3ff03c8",
  "requestId": "req_011CbC8JgHxnrVsYSfYKLaCE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "802419e1-2206-4e8d-802e-96d1a41e4c4a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DvkssNJ3kXhbbkS6nMULPj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 8991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1123,
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

_source line 9 · 2026-05-19T15:00:00.932Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015RECfyX7YoM3uxNUp4JWP6`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.21772",
  "prompt": "Extract ALL information from this paper page: full title, authors, abstract, what CCPS stands for, methodology, models evaluated, benchmarks, key results (ECE reduction, Brier score), comparison to other methods, whether it's training-free, and limitations. Give me every detail available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "802419e1-2206-4e8d-802e-96d1a41e4c4a",
  "isSidechain": true,
  "agentId": "a877e5c2fa3ff03c8",
  "requestId": "req_011CbC8JgHxnrVsYSfYKLaCE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41baacc2-47ed-429f-a2e5-22da0b013b04",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DvkssNJ3kXhbbkS6nMULPj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 8991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1123,
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

_source line 10 · 2026-05-19T15:00:03.346Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Gpkybtvmyiei6nCua6dsTo`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.21772v1",
  "prompt": "Extract the COMPLETE content of this paper. I need: 1) What CCPS stands for, 2) The full perturbation-stability probing methodology in detail, 3) All models and benchmarks evaluated, 4) All quantitative results (ECE reduction percentages, Brier score improvements, accuracy), 5) Comparison tables with other calibration methods, 6) Whether it requires training or is training-free, 7) Limitations section, 8) Key equations and algorithms. Provide as much detail as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41baacc2-47ed-429f-a2e5-22da0b013b04",
  "isSidechain": true,
  "agentId": "a877e5c2fa3ff03c8",
  "requestId": "req_011CbC8JgHxnrVsYSfYKLaCE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3290d06-80bd-49bf-bd6f-4697e7e70815",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DvkssNJ3kXhbbkS6nMULPj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 8991,
      "output_tokens": 405,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1123
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 405,
          "cache_read_input_tokens": 8991,
          "cache_creation_input_tokens": 1123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1123,
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

_source line 11 · 2026-05-19T15:00:04.225Z_

<details><summary>↩ Tool result · `toolu_01BwwEg4WkJgbR6ib1NNtwzU`</summary>

```text
Web search results for query: "CCPS arXiv 2505.21772 perturbation-stability probing calibration LLM"

Links: [{"title":"[2505.21772] Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/abs/2505.21772"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/pdf/2505.21772"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability | alphaXiv","url":"https://www.alphaxiv.org/abs/2505.21772"},{"title":"[Literature Review] Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://www.themoonlight.io/en/review/calibrating-llm-confidence-by-probing-perturbed-representation-stability"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/html/2505.21772v1"},{"title":"CCPS: Calibrating LLM Confidence via Perturbation Stability – EMNLP 2025 | Hacker News","url":"https://news.ycombinator.com/item?id=45055315"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250521772K/abstract"},{"title":"GitHub - Ledengary/CCPS: Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://github.com/ledengary/CCPS"},{"title":"(PDF) Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://www.researchgate.net/publication/392168633_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability | Request PDF","url":"https://www.researchgate.net/publication/397423860_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"}]

I found the paper! Here's the information about arXiv paper 2505.21772:

## CCPS: Calibrating LLM Confidence by Probing Perturbed Representation Stability

CCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability) is a novel method analyzing internal representational stability in LLMs.

### How It Works

CCPS applies targeted adversarial perturbations to final hidden states, extracts features reflecting the model's response to these perturbations, and uses a lightweight classifier to predict answer correctness. This model-agnostic probing offers an efficient confidence proxy without modifying the base LLM.

### Evaluation

CCPS was evaluated on LLMs from 8B to 32B parameters (covering Llama, Qwen, and Mistral architectures) using MMLU and MMLU-Pro benchmarks in both multiple-choice and open-ended formats.

### Performance

Across four LLMs and three MMLU variants, CCPS reduces Expected Calibration Error by approximately 55% and Brier score by 21%, while increasing accuracy by 5 percentage points, Area Under the Precision-Recall Curve by 4 percentage points, and Area Under the Receiver Operating Characteristic Curve by 6 percentage points, all relative to the strongest prior method.

The paper is available on arXiv, and there's also a GitHub repository with code and datasets for replication.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "802419e1-2206-4e8d-802e-96d1a41e4c4a",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "a877e5c2fa3ff03c8",
  "type": "user",
  "uuid": "bbf5e85a-4315-4216-9a4d-1d8535cdd53d",
  "sourceToolAssistantUUID": "802419e1-2206-4e8d-802e-96d1a41e4c4a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T15:00:06.833Z_

<details><summary>↩ Tool result · `toolu_015RECfyX7YoM3uxNUp4JWP6`</summary>

```text
# Paper Summary: Calibrating LLM Confidence by Probing Perturbed Representation Stability

**Full Title:** "Calibrating LLM Confidence by Probing Perturbed Representation Stability"

**Authors:** Reza Khanmohammadi, Erfan Miahi, Mehrsa Mardikoraem, Simerjot Kaur, Ivan Brugere, Charese H. Smiley, Kundan Thind, Mohammad M. Ghassemi

**Submission Date:** May 27, 2025 (revised September 18, 2025)

**arXiv ID:** 2505.21772

---

## What CCPS Stands For
**CCPS** = "Calibrating LLM Confidence by Probing Perturbed Representation Stability"

---

## Methodology
The approach works by applying "targeted adversarial perturbations to final hidden states, extracts features reflecting the model's response to these perturbations, and uses a lightweight classifier to predict answer correctness."

---

## Models Evaluated
- Parameter range: 8B to 32B
- Architectures: Llama, Qwen, and Mistral

---

## Benchmarks Used
- MMLU
- MMLU-Pro
- Both multiple-choice and open-ended formats

---

## Key Results
Compared to the strongest prior method across four LLMs and three MMLU variants:
- **Expected Calibration Error (ECE):** ~55% reduction
- **Brier Score:** 21% reduction
- **Accuracy:** 5 percentage point increase
- **AUPRC:** 4 percentage point increase
- **AUROC:** 6 percentage point increase

---

## Training-Free Status
Not explicitly stated in the available content.

---

## Limitations
Not detailed in the provided abstract or page content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41baacc2-47ed-429f-a2e5-22da0b013b04",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "a877e5c2fa3ff03c8",
  "type": "user",
  "uuid": "0f36b560-d704-489b-a844-a7f0ca5b5e61",
  "sourceToolAssistantUUID": "41baacc2-47ed-429f-a2e5-22da0b013b04",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T15:00:25.737Z_

<details><summary>↩ Tool result · `toolu_01Gpkybtvmyiei6nCua6dsTo`</summary>

```text
# CCPS: LLM Confidence Calibration via Perturbed Representation Stability

## 1. What CCPS Stands For

**CCPS** = "Calibrating LLM Confidence by Probing Perturbed Representation Stability"

## 2. Perturbation-Stability Probing Methodology

The method operates in three stages on frozen base LLMs:

### Stage 1: Adversarial Perturbation
For each token in an answer, the approach:
- Extracts the original final hidden state H₀⁽ⁱ⁾ that generated token tᵢ
- Computes the Jacobian vector J⁽ⁱ⁾ = ∇H₀(ℒ⁽ⁱ⁾), where ℒ⁽ⁱ⁾ is negative log-likelihood of the observed token
- Normalizes this to direction d⁽ⁱ⁾ = J⁽ⁱ⁾/||J⁽ⁱ⁾||₂
- Applies S=5 incremental perturbations: Hₛ⁽ⁱ⁾ = H₀⁽ⁱ⁾ + εₛ·d⁽ⁱ⁾, where εₛ ranges from 0 to ϵₘₐₓ=20.0

### Stage 2: Feature Extraction
Generates 75 features across four categories:

**Original State Features** (12): baseline probabilities, logits, entropy, margins, norms
**Overall Perturbation Features** (3): Jacobian norm, epsilon-to-flip (magnitude needed to change top token), Perturbation Energy Integral
**Perturbed State Features** (8): post-perturbation distributions, entropy, margins
**Comparison Features** (52): KL divergence, Jensen-Shannon divergence, cosine similarities, L2 distances between original and perturbed states

### Stage 3: Classification Architecture
- **Multiple-Choice**: Feature vector f⁽¹⁾ processed through MLP (EMC)
- **Open-Ended**: Sequence of feature vectors processed through CNN encoder with adaptive pooling (EOE)
- Both encoders pre-trained with max-margin contrastive loss
- Classification head outputs binary correctness prediction via softmax

## 3. Models and Benchmarks Evaluated

### Language Models (8B-32B parameters):
- Meta-Llama-3.1-8B-Instruct
- Qwen2.5-14B-Instruct
- Mistral-Small-24B-Instruct-2501
- Qwen2.5-32B-Instruct

### Datasets:
- **Training/Validation**: CT-CHOICE and CT-OE (aggregated from 16 public QA datasets)
- **Evaluation**: 
  - MMLU-CHOICE (57 tasks, 14,042 examples)
  - MMLU-OE (open-ended variant)
  - MMLU-PRO-CHOICE (14 tasks, 12,032 examples, more challenging)

## 4. Quantitative Results

### MMLU-CHOICE Performance (Table 1):
| Model | ECE (%) | Brier | ACC (%) | AUCPR (%) | AUROC (%) |
|-------|---------|-------|---------|-----------|-----------|
| **Llama-8B** | 6.5 | 17.1 | 73.4 | 84.1 | 77.1 |
| **Qwen-14B** | 6.3 | 13.1 | 80.2 | 92.1 | 81.6 |
| **Mistral-24B** | 5.8 | 11.5 | 83.0 | 93.1 | 83.3 |
| **Qwen-32B** | 6.3 | 10.8 | 84.1 | 94.1 | 82.8 |

### MMLU-PRO-CHOICE Performance:
- ECE: ~4.2-4.6% across all models (vs. LitCab 16.6-49.7%, CT 17.8-38.0%)
- AUROC: 67.9-77.8%

### MMLU-OE Performance:
- ECE: 6.7-8.7% 
- Competitive calibration advantage over baselines

### Aggregate Improvements vs. Best Baseline:
- **ECE reduction**: ~55% average (up to 88%)
- **Brier score**: 21% improvement (up to 45%)
- **Accuracy**: +5 percentage points average (up to +14 pp)
- **AUCPR**: +4 pp average (up to +13 pp)
- **AUROC**: +6 pp average (up to +17 pp)

## 5. Comparison with Other Calibration Methods

### Baselines Compared:
1. P(True) - Model self-evaluation of answer correctness
2. P(IK) - Model self-assessment of ability before answering
3. LTS (Logit Temperature Scaling) - Post-hoc temperature adjustment
4. IT (Instruction Tuning) - Fine-tuning on uncertainty
5. SAPLMA - Linear probe on hidden layers (variants: F, M, UM)
6. CT (Calibration-Tuning) - Fine-tuning with LoRA on self-eval
7. LitCab - Lightweight linear projection with contrastive loss

CCPS consistently outperformed all baselines, particularly excelling in simultaneous calibration (ECE) and discrimination (AUROC/AUCPR).

## 6. Training Requirements

**NOT training-free**, but lightweight:
- Requires 10,000 total training steps:
  - 5,000 steps: contrastive pre-training of encoder
  - 5,000 steps: classification head fine-tuning
- Only trains small MLPs/CNNs, not the base LLM
- Uses AdamW optimizer with learning rate 1×10⁻⁴, batch size 32, weight decay 0.1
- No fine-tuning of base LLM parameters (frozen throughout)

## 7. Limitations

The authors identify three main constraints:

1. **Computational cost of feature extraction**: Each token requires Jacobian computation plus S forward passes through LM head for perturbed logits; requires access to model internals

2. **Hyperparameter sensitivity**: Feature effectiveness depends on ϵₘₐₓ and S values; may require retuning for different models/tasks

3. **Dependence on representation quality**: Method assumes base LLM's hidden states systematically encode certainty information; effectiveness limited if they don't

## 8. Key Equations and Algorithms

### Loss Definition:
ℒ⁽ⁱ⁾ = −log P(tᵢ|H₀⁽ⁱ⁾)

### Jacobian & Direction:
J⁽ⁱ⁾ = ∇H₀⁽ⁱ⁾ ℒ⁽ⁱ⁾  
d⁽ⁱ⁾ = J⁽ⁱ⁾/||J⁽ⁱ⁾||₂

### Perturbation Trajectory:
Hₛ⁽ⁱ⁾ = H₀⁽ⁱ⁾ + εₛ·d⁽ⁱ⁾, where εₛ = s·(ϵₘₐₓ/S)

### Output:
Zₛ⁽ⁱ⁾ = LM_Head(Hₛ⁽ⁱ⁾)  
P(correct|A) = softmax(C(E(f⁽¹⁾)))  [for multiple-choice]  
P(correct|A) = softmax(C(E(f⁽¹⁾,...,f⁽ᴸ⁾)))  [for open-ended]

---

**Code & Data**: Available at https://github.com/ledengary/CCPS and https://huggingface.co/datasets/ledengary/CCPS
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3290d06-80bd-49bf-bd6f-4697e7e70815",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "a877e5c2fa3ff03c8",
  "type": "user",
  "uuid": "e46adf59-b547-433f-947f-659a25ceb610",
  "sourceToolAssistantUUID": "b3290d06-80bd-49bf-bd6f-4697e7e70815",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-19T15:00:29.778Z_

The HTML version provided rich detail. Let me also fetch the GitHub repo and the review/discussion page for any additional context on limitations and practical considerations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e46adf59-b547-433f-947f-659a25ceb610",
  "isSidechain": true,
  "agentId": "a877e5c2fa3ff03c8",
  "requestId": "req_011CbC8LzBnz7kZFS8AUXDBd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1b90d8f-593d-4a15-9eee-862794d2966c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WESZThDtVP6YzkTD6keCjR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3981,
      "cache_read_input_tokens": 10114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3981,
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

_source line 15 · 2026-05-19T15:00:31.718Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011y5DFTc5ARqS1S8LRoDNVA`</summary>

```json
{
  "url": "https://github.com/ledengary/CCPS",
  "prompt": "Extract the full README content, including: installation instructions, usage, what scripts are available, what models are supported, and any practical notes about running CCPS. Also look for any mention of computational requirements, GPU memory, or inference time."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1b90d8f-593d-4a15-9eee-862794d2966c",
  "isSidechain": true,
  "agentId": "a877e5c2fa3ff03c8",
  "requestId": "req_011CbC8LzBnz7kZFS8AUXDBd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4df2f1bb-b9e7-4061-b9c5-45301e7903ad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WESZThDtVP6YzkTD6keCjR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3981,
      "cache_read_input_tokens": 10114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3981,
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

_source line 16 · 2026-05-19T15:00:33.874Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017DnsmyBJUmURAgkjmHfB64`</summary>

```json
{
  "url": "https://www.themoonlight.io/en/review/calibrating-llm-confidence-by-probing-perturbed-representation-stability",
  "prompt": "Extract the complete review/analysis of this paper. I need: critiques, strengths, weaknesses, any additional insight about the methodology, and any comparisons to other methods not covered in the original paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4df2f1bb-b9e7-4061-b9c5-45301e7903ad",
  "isSidechain": true,
  "agentId": "a877e5c2fa3ff03c8",
  "requestId": "req_011CbC8LzBnz7kZFS8AUXDBd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf851bee-f6f3-48b4-be4a-fd24f59f575c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WESZThDtVP6YzkTD6keCjR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3981,
      "cache_read_input_tokens": 10114,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3981
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 287,
          "cache_read_input_tokens": 10114,
          "cache_creation_input_tokens": 3981,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3981,
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

_source line 17 · 2026-05-19T15:00:41.220Z_

<details><summary>↩ Tool result · `toolu_017DnsmyBJUmURAgkjmHfB64`</summary>

```text
# Analysis of "Calibrating LLM Confidence by Probing Perturbed Representation Stability"

## Strengths

**Novel Methodological Approach**
The paper introduces an innovative technique that "evaluates the stability of an LLM's internal representations under targeted adversarial perturbations." This model-agnostic approach operates on frozen models, avoiding computational overhead of fine-tuning.

**Comprehensive Feature Engineering**
The extraction of 75 features across multiple categories—original state, perturbation impact, perturbed states, and comparative metrics—provides rich signal for confidence prediction. This multi-dimensional characterization captures nuanced aspects of model behavior.

**Strong Empirical Performance**
Results demonstrate substantial improvements: "CCPS reduced Expected Calibration Error (ECE) by approximately 55% and Brier score by 21%" compared to existing methods. Performance gains across diverse LLMs and benchmarks suggest robust generalization.

**Parameter Efficiency**
The method achieves superior results with "significantly smaller" trainable components than competing approaches like LitCab, making deployment more practical.

## Weaknesses

**Computational Overhead**
The paper acknowledges that "limitations include the computational cost of feature extraction." Extracting 75 features per token through perturbation trajectories requires substantial computation, potentially limiting real-time applications.

**Model Internals Dependency**
The approach "relies on model internals," restricting applicability to proprietary models or systems where hidden state access isn't available—a significant constraint for broader adoption.

**Limited Baseline Comparisons**
While the paper compares against multiple baselines, no comparison is provided against emerging uncertainty quantification methods from the broader ML literature.

## Methodology Insights

The three-stage design is well-motivated: perturbation-based probing identifies fragile decision boundaries, feature extraction quantifies stability patterns, and neural classification leverages these signals. The use of Jacobian-guided perturbation directions ensures adversarial relevance rather than random noise.

## Missing Elements

The provided content lacks detailed ablation studies examining individual feature contributions, cross-domain generalization analysis, and runtime complexity benchmarks that would strengthen the evaluation narrative.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf851bee-f6f3-48b4-be4a-fd24f59f575c",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "a877e5c2fa3ff03c8",
  "type": "user",
  "uuid": "08ed13d1-1d8f-4ddd-ba3d-89761600e492",
  "sourceToolAssistantUUID": "cf851bee-f6f3-48b4-be4a-fd24f59f575c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T15:00:45.228Z_

<details><summary>↩ Tool result · `toolu_011y5DFTc5ARqS1S8LRoDNVA`</summary>

````text
# CCPS: LLM Confidence Calibration - Complete Overview

## Project Summary
CCPS is a method for estimating Large Language Model confidence by analyzing internal representation stability under adversarial perturbations. The repository provides implementation code for the paper at arXiv:2505.21772.

## Installation Requirements

**Python Version:** 3.12.9

**Basic Setup:**
```
git clone https://github.com/Ledengary/CCPS.git
cd CCPS
python -m venv ccps_env
source ccps_env/bin/activate
pip install -r requirements.txt
```

**Special Notes:** The developers recommend installing `vllm` and `unsloth` "from source for optimal performance and compatibility."

## Core Pipeline (5 Steps)

### Step 0: Answer Generation & Assessment
- `answer_with_vllm.py`: Generates LLM responses using vLLM library
- `answer_assessment.py`: Labels responses as correct/incorrect (substring matching for multiple-choice, GPT-4o-mini API for open-ended)

### Step 1: Hidden State Extraction
- `origpert_hidden_state_logit_extraction.py`: Extracts final hidden states, logits, Jacobian vectors, and perturbed states for each generated token
- Key parameters: `--pei_radius 20.0`, `--pei_steps 5`

### Step 2: Feature Calculation
- `origpert_feature_extraction.py`: Computes 75 features (D_f=75) from raw representations
- Key parameters: `--eps_search_low 0.01`, `--eps_search_high 20.0`

### Step 3: Contrastive Model Training
- MC format: `ccps_contrastive_train.py`
- OE format: `ccps_oe_contrastive_train.py`
- Creates discriminative embeddings via contrastive learning
- Typical hyperparameters: batch_size 32-64, lr 1e-4 to 1e-3, 5000 training steps

### Step 4: Classifier Training
- MC: `ccps_classifier_train.py`
- OE: `ccps_oe_classifier_train.py`
- Fine-tunes encoder and trains classification head jointly
- Default architecture includes dropout (0.05) and multiple hidden layers

### Step 5: Evaluation
- MC: `ccps_uncertainty.py`
- OE: `ccps_oe_uncertainty.py`
- Calculates metrics: ECE, Brier, ACC, AUCPR, AUROC

## Supported Models

The pipeline supports inference with:
- Meta-Llama-3.1-8B-Instruct
- Qwen2.5-14B-Instruct
- Mistral-Small-24B-Instruct-2501
- Qwen2.5-32B-Instruct

## Dataset Format

Training/validation datasets:
- CT-CHOICE (multiple-choice)
- CT-OE (open-ended)

Test datasets:
- MMLU-CHOICE
- MMLU-PRO-CHOICE
- MMLU-OE

All datasets hosted at huggingface.co/datasets/ledengary/CCPS

## Computational Considerations

**GPU Support:** Scripts accept `--gpu_ids` and `--visible_cudas` parameters for multi-GPU configuration. Example: `--tensor_parallel 2` for distributed inference across 2 GPUs, `--gpu_memory 0.9` for memory allocation.

**Memory Configuration:** The repository mentions GPU memory parameters but doesn't specify exact VRAM requirements per model size.

**Inference Speed:** Not detailed in documentation; processing involves feature extraction, model inference, and metric calculation steps.

## Key Technical Notes

- Uses bfloat16 dtype for efficiency
- Supports both supervised training and contrastive learning approaches
- Feature extraction happens offline (separate from classifier training)
- Configuration files (JSON) preserve hyperparameters for reproducibility
- All scripts use PyTorch with multi-worker data loading support

## Practical Workflow

Users should: (1) download datasets from HuggingFace, (2) run feature extraction on their base model, (3) train contrastive encoder, (4) train classifier head, (5) evaluate on test sets. Each step generates intermediate files (`.npz`, `.pkl`, `.pt`) consumed by subsequent steps.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4df2f1bb-b9e7-4061-b9c5-45301e7903ad",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "a877e5c2fa3ff03c8",
  "type": "user",
  "uuid": "60eb9624-ff94-4973-87e0-8f2fafe31fa2",
  "sourceToolAssistantUUID": "4df2f1bb-b9e7-4061-b9c5-45301e7903ad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-19T15:01:50.851Z_

I now have comprehensive information. Here is the detailed report.

---

## CCPS Paper: Detailed Findings

**Full title:** "Calibrating LLM Confidence by Probing Perturbed Representation Stability"
**arXiv:** 2505.21772 | **Venue:** EMNLP 2025
**Authors:** Reza Khanmohammadi, Erfan Miahi, Mehrsa Mardikoraem, Simerjot Kaur, Ivan Brugere, Charese H. Smiley, Kundan Thind, Mohammad M. Ghassemi
**Code:** https://github.com/Ledengary/CCPS | **Data:** https://huggingface.co/datasets/ledengary/CCPS

---

### 1. What CCPS stands for

**C**alibrating LLM **C**onfidence by **P**robing Perturbed Representation **S**tability. The acronym derives from the initials of the key conceptual words (Calibrating, Confidence, Probing, Stability).

---

### 2. Perturbation-Stability Probing Methodology

CCPS operates in three stages on **frozen** (unmodified) base LLMs:

**Stage 1 -- Adversarial Perturbation:**
For each token t_i in an answer, the method:
- Extracts the original final hidden state H_0^(i)
- Computes the Jacobian vector J^(i) = nabla_{H_0} L^(i), where L^(i) = -log P(t_i | H_0^(i)) (negative log-likelihood of the observed token)
- Normalizes to a direction: d^(i) = J^(i) / ||J^(i)||_2
- Applies S=5 incremental perturbations along this direction: H_s^(i) = H_0^(i) + epsilon_s * d^(i), where epsilon_s = s * (epsilon_max / S) and epsilon_max = 20.0

The key insight: the Jacobian direction is the steepest-ascent direction for the loss -- it pushes the hidden state in the direction most adversarial to the predicted token. Correct answers tend to be **stable** under these perturbations; incorrect answers tend to be **fragile**.

**Stage 2 -- Feature Extraction (75 features in 4 categories):**
- **Original State Features (12):** baseline probabilities, logits, entropy, margins, norms
- **Overall Perturbation Features (3):** Jacobian norm, epsilon-to-flip (magnitude needed to change top token), Perturbation Energy Integral
- **Perturbed State Features (8):** post-perturbation distributions, entropy, margins
- **Comparison Features (52):** KL divergence, Jensen-Shannon divergence, cosine similarities, L2 distances between original and perturbed states

**Stage 3 -- Classification:**
- **Multiple-Choice (EMC encoder):** Feature vector f^(1) processed through an MLP
- **Open-Ended (EOE encoder):** Sequence of feature vectors f^(1),...,f^(L) processed through a CNN encoder with adaptive pooling
- Both encoders are pre-trained with max-margin contrastive loss (5,000 steps), then a classification head is fine-tuned (5,000 steps)
- Output: P(correct | Answer) via softmax

---

### 3. Models and Benchmarks Evaluated

**Models (8B-32B):**
| Model | Size |
|---|---|
| Meta-Llama-3.1-8B-Instruct | 8B |
| Qwen2.5-14B-Instruct | 14B |
| Mistral-Small-24B-Instruct-2501 | 24B |
| Qwen2.5-32B-Instruct | 32B |

**Benchmarks:**
- **MMLU-CHOICE:** 57 tasks, 14,042 examples (multiple-choice)
- **MMLU-OE:** Open-ended variant of MMLU
- **MMLU-PRO-CHOICE:** 14 tasks, 12,032 examples (harder multiple-choice)

**Training data:** CT-CHOICE and CT-OE, aggregated from 16 public QA datasets.

---

### 4. Key Quantitative Results

**MMLU-CHOICE (representative results for CCPS):**

| Model | ECE (%) | Brier | ACC (%) | AUCPR (%) | AUROC (%) |
|---|---|---|---|---|---|
| Llama-8B | 6.5 | 17.1 | 73.4 | 84.1 | 77.1 |
| Qwen-14B | 6.3 | 13.1 | 80.2 | 92.1 | 81.6 |
| Mistral-24B | 5.8 | 11.5 | 83.0 | 93.1 | 83.3 |
| Qwen-32B | 6.3 | 10.8 | 84.1 | 94.1 | 82.8 |

**MMLU-PRO-CHOICE:** ECE of ~4.2-4.6% across all models (vs. LitCab 16.6-49.7%, CT 17.8-38.0%)

**Aggregate improvements vs. best prior baseline:**
- **ECE reduction:** ~55% average, up to **88%** in best case
- **Brier score improvement:** 21% average, up to **45%**
- **Accuracy:** +5 pp average, up to +14 pp
- **AUCPR:** +4 pp average, up to +13 pp
- **AUROC:** +6 pp average, up to +17 pp

---

### 5. Comparison to Other Calibration Methods

CCPS was compared against **7 baselines:**

| Method | Type | Key weakness vs. CCPS |
|---|---|---|
| P(True) | Verbalized self-evaluation | Poor calibration on hard tasks |
| P(IK) ("I Know") | Verbalized pre-assessment | Same |
| LTS (Logit Temperature Scaling) | Post-hoc logit adjustment | Calibration-only, no discrimination |
| IT (Instruction Tuning) | Fine-tuning with uncertainty | Requires LLM fine-tuning |
| SAPLMA (variants F, M, UM) | Linear probe on hidden layers | Weaker features (no perturbation signal) |
| CT (Calibration-Tuning) | LoRA fine-tuning for self-eval | Modifies the LLM; still worse calibration |
| LitCab | Lightweight linear projection + contrastive loss | Most competitive baseline; CCPS still dominates |

CCPS uniquely excels at **simultaneous** calibration (ECE) and discrimination (AUROC/AUCPR). Most prior methods trade off one for the other. The perturbation-stability features provide richer signal than raw hidden states (SAPLMA) or logit-level adjustments (LTS, LitCab).

---

### 6. Training Requirements

**Not training-free**, but **lightweight and LLM-frozen:**
- The base LLM is never fine-tuned -- parameters remain frozen throughout
- Only small auxiliary networks are trained:
  - 5,000 steps of contrastive pre-training (MLP or CNN encoder)
  - 5,000 steps of classification head fine-tuning
  - AdamW optimizer, lr=1e-4, batch size 32, weight decay 0.1, dropout 0.05
- The trainable component has "significantly smaller" parameter count than alternatives like LitCab
- Feature extraction is offline and can be precomputed
- The pipeline uses vLLM for inference and supports multi-GPU (tensor parallelism, bfloat16)

---

### 7. Limitations

The authors identify three main constraints:

1. **Computational cost of feature extraction:** Each token requires a Jacobian computation plus S=5 forward passes through the LM head for perturbed logits. This requires white-box access to model internals (hidden states and gradients), ruling out API-only models (GPT-4, Claude, etc.).

2. **Hyperparameter sensitivity:** Feature effectiveness depends on epsilon_max and S values, which may need retuning for different model families or task domains. The paper uses epsilon_max=20.0 and S=5 throughout, but generality is not guaranteed.

3. **Dependence on representation quality:** The method assumes that the base LLM's hidden states systematically encode certainty information. If the model's internal representations do not exhibit meaningful stability gradients (e.g., poorly trained or highly stochastic models), CCPS effectiveness would be limited.

**Additional practical limitations identified by reviewers:**
- No comparison against broader ML uncertainty quantification methods (e.g., conformal prediction, ensemble methods)
- No cross-domain generalization analysis (training and test are both MMLU-family)
- No runtime complexity benchmarks (wall-clock time per sample not reported)
- Restricted to open-weight models where hidden states are accessible

---

### 8. Positioning for Your Research Proposal

For a research proposal on **competing calibration biases**, CCPS offers several angles:

- **As a landscape reference:** CCPS represents the current SOTA for white-box LLM calibration at EMNLP 2025, setting the quantitative bar at ~55% ECE reduction. Any competing approach would need to benchmark against it.

- **As an extended baseline:** The GitHub repo and HuggingFace datasets are publicly available, making replication straightforward. The 5-step pipeline (answer generation -> hidden state extraction -> feature computation -> contrastive training -> classifier training) is modular.

- **Gap to exploit:** CCPS does not address *where* calibration biases come from or how they interact. It treats calibration as a classification problem (correct vs. incorrect) rather than analyzing the structure of miscalibration. A proposal on competing calibration biases could argue that CCPS's 75-feature representation captures symptoms of miscalibration but does not decompose the underlying bias mechanisms.

- **Another gap:** CCPS is evaluated only on MMLU-family benchmarks. Cross-domain generalization (reasoning, coding, long-form generation) is unexplored.

- **Complementarity:** CCPS's perturbation-stability features could potentially be decomposed to identify distinct calibration bias components, making it not just a baseline but a source of analytical signal for your bias framework.

Sources:
- [arXiv Abstract](https://arxiv.org/abs/2505.21772)
- [arXiv HTML Full Paper](https://arxiv.org/html/2505.21772v1)
- [GitHub Repository](https://github.com/Ledengary/CCPS)
- [Moonlight Literature Review](https://www.themoonlight.io/en/review/calibrating-llm-confidence-by-probing-perturbed-representation-stability)
- [alphaXiv Discussion](https://www.alphaxiv.org/abs/2505.21772)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60eb9624-ff94-4973-87e0-8f2fafe31fa2",
  "isSidechain": true,
  "agentId": "a877e5c2fa3ff03c8",
  "requestId": "req_011CbC8NRWaF8hUbDWQ3X7cP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33384a27-3c0c-4c87-952d-2a6642217eb2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ewtv1D9KmqBmK6LrfhjNgg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 513,
      "cache_creation_input_tokens": 1366,
      "cache_read_input_tokens": 14095,
      "output_tokens": 2730,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1366
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 513,
          "output_tokens": 2730,
          "cache_read_input_tokens": 14095,
          "cache_creation_input_tokens": 1366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1366,
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
