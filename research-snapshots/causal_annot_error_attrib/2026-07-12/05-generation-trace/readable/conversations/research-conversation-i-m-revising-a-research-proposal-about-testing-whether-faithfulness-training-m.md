# Research conversation: I'm revising a research proposal about testing whether faithfulness training methods survive adversarial pressure. A rev

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a7ed4918e81d4960b.jsonl`
- **Structured JSON:** [`af286bbbf91e51e52eb2.json`](../../sessions/af/af286bbbf91e51e52eb2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

51 recorded events

### User

_source line 1 · 2026-05-19T09:11:48.930Z_

I'm revising a research proposal about testing whether faithfulness training methods survive adversarial pressure. A reviewer flagged several missing papers. Please research each one:

1. **REMUL "Balancing Faithfulness and Performance" (arXiv:2602.16154, Feb 2026)** — a 4th faithfulness training method. Search for it and read it via WebFetch on https://arxiv.org/abs/2602.16154. I need: what method does REMUL use? How does it differ from FRIT (causal interventions + DPO), CST (counterfactual simulation + RL), and FaithRL (step-level process rewards)? What models/benchmarks did they test on?

2. **"Mechanistic Evidence for Faithfulness Decay" (arXiv:2602.11201, Feb 2026)** — mentions a "reasoning horizon" phenomenon. Search and read via WebFetch on https://arxiv.org/abs/2602.11201. What is the "reasoning horizon" phenomenon? How is it relevant to faithfulness decay under adversarial pressure?

3. **"Reasoning Theater" (arXiv:2603.05488, March 2026)** — evidence of performative CoT from activation probing. Search and read via WebFetch on https://arxiv.org/abs/2603.05488. What did they find about performative vs genuine reasoning in CoT?

For each paper, extract: title, authors, key method, main findings, and how it relates to testing faithfulness training under adversarial pressure. Report in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8029e2e4-25c6-47cb-9539-6d3b0938c122",
  "agentId": "a7ed4918e81d4960b",
  "type": "user",
  "uuid": "18329763-024a-4059-aeb5-f487cafe6fa7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T09:11:48.937Z_

```json
{
  "parentUuid": "18329763-024a-4059-aeb5-f487cafe6fa7",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
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
  "uuid": "f078e1ac-1b9f-4d06-8140-6123ceb574de",
  "timestamp": "2026-05-19T09:11:48.937Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T09:11:48.940Z_

```json
{
  "parentUuid": "f078e1ac-1b9f-4d06-8140-6123ceb574de",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "20f8013f-67f6-4e74-a351-6d4fd0faddac",
  "timestamp": "2026-05-19T09:11:48.940Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T09:11:51.944Z_



I'll fetch all three papers simultaneously to gather the information you need.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20f8013f-67f6-4e74-a351-6d4fd0faddac",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfm7wtKmi9vUdjU1ERP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "608e589d-dff3-41e5-b445-981e942e0df0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmXQAC6qsTFayUmuRbNea3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1678,
      "cache_read_input_tokens": 7409,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1678
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 7409,
          "cache_creation_input_tokens": 1678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1678,
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

### Tool call

_source line 5 · 2026-05-19T09:11:51.951Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0157UrSRut5UZ9B2Afy81KVA`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "608e589d-dff3-41e5-b445-981e942e0df0",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfm7wtKmi9vUdjU1ERP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f714d80-e25a-4ab0-9c74-6d9d1de50bb8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmXQAC6qsTFayUmuRbNea3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1678,
      "cache_read_input_tokens": 7409,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1678
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 7409,
          "cache_creation_input_tokens": 1678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1678,
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

_source line 6 · 2026-05-19T09:11:51.954Z_

<details><summary>↩ Tool result · `toolu_0157UrSRut5UZ9B2Afy81KVA`</summary>

````text
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
  "parentUuid": "1f714d80-e25a-4ab0-9c74-6d9d1de50bb8",
  "isSidechain": true,
  "promptId": "8029e2e4-25c6-47cb-9539-6d3b0938c122",
  "agentId": "a7ed4918e81d4960b",
  "type": "user",
  "uuid": "366ea3c8-7ddf-4b2d-9d73-158d18f7a1b6",
  "sourceToolAssistantUUID": "1f714d80-e25a-4ab0-9c74-6d9d1de50bb8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T09:11:55.370Z_



Now let me fetch all three papers simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "366ea3c8-7ddf-4b2d-9d73-158d18f7a1b6",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfmMPmjLkd5HpfzhbmV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe882f62-0f31-46c5-b97d-46f616c7d0f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QfH9cHMAzdQ153JnZbZGTt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 9087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 614,
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

_source line 8 · 2026-05-19T09:11:57.837Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KczLkjVMa9g5hKyKDkCDki`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.16154",
  "prompt": "Extract ALL available information about this paper. I need: 1) Full title, 2) All authors, 3) The complete abstract, 4) What method REMUL uses for faithfulness training, 5) How it differs from other methods like causal interventions + DPO, counterfactual simulation + RL, and step-level process rewards, 6) What models and benchmarks they tested on, 7) Key findings and results. Be as detailed and thorough as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe882f62-0f31-46c5-b97d-46f616c7d0f9",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfmMPmjLkd5HpfzhbmV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3045cb35-f795-47a6-8e0c-2a100cd0218c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QfH9cHMAzdQ153JnZbZGTt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 9087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 614,
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

_source line 9 · 2026-05-19T09:11:59.238Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LSMSvQNmvCSFDcAVbGDcSN`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.11201",
  "prompt": "Extract ALL available information about this paper. I need: 1) Full title, 2) All authors, 3) The complete abstract, 4) What the \"reasoning horizon\" phenomenon is, 5) What mechanistic evidence they found for faithfulness decay, 6) How this relates to adversarial pressure on reasoning models, 7) Key findings and experimental results. Be as detailed and thorough as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3045cb35-f795-47a6-8e0c-2a100cd0218c",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfmMPmjLkd5HpfzhbmV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e606f9bb-49ee-4acd-b933-1df334d35fc4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QfH9cHMAzdQ153JnZbZGTt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 9087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 614,
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

_source line 10 · 2026-05-19T09:12:01.157Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013eswrjGKSQ8UW1jMe6PkZD`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.05488",
  "prompt": "Extract ALL available information about this paper. I need: 1) Full title, 2) All authors, 3) The complete abstract, 4) What they found about \"performative\" vs \"genuine\" reasoning in chain-of-thought, 5) What activation probing methods they used, 6) Evidence of \"reasoning theater\" - models producing CoT that looks like reasoning but isn't faithfully representing internal computation, 7) Key findings and experimental results. Be as detailed and thorough as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e606f9bb-49ee-4acd-b933-1df334d35fc4",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfmMPmjLkd5HpfzhbmV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aec62b20-5836-4006-857f-a64b18c63478",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QfH9cHMAzdQ153JnZbZGTt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 9087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 614,
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

_source line 11 · 2026-05-19T09:12:05.503Z_

<details><summary>↩ Tool result · `toolu_01KczLkjVMa9g5hKyKDkCDki`</summary>

```text
# Paper Analysis: REMUL

## 1) Full Title
"Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"

## 2) All Authors
Nithin Sivakumaran, Shoubin Yu, Hyunji Lee, Yue Zhang, Ali Payani, Mohit Bansal, and Elias Stengel-Eskin

## 3) Complete Abstract
The paper addresses a core challenge in chain-of-thought reasoning: explanations from large language models often fail to accurately represent the model's actual computational process. The authors note that "Chain-of-thought (CoT) reasoning sometimes fails to faithfully reflect the true computation of a large language model (LLM)." Additionally, pursuing faithfulness typically comes at the cost of task accuracy. Their work proposes a solution designed to improve both dimensions simultaneously.

## 4) REMUL's Faithfulness Training Method
REMUL employs a multi-party reinforcement learning framework based on a core hypothesis: "reasoning traces which other parties can follow will be more faithful." The mechanism operates as follows:

- A speaker model generates reasoning traces
- These traces are truncated and passed to listener models who continue them toward answers
- Speakers receive rewards for producing reasoning that listeners can comprehend and execute
- Additional regularization through masked supervised finetuning counters the faithfulness-performance tradeoff

## 5) Differentiation from Other Approaches
The document does not provide explicit comparisons with causal interventions + DPO, counterfactual simulation + RL, or step-level process rewards. Direct information about how REMUL differs from these alternative methods is unavailable in the provided content.

## 6) Models and Benchmarks Tested
**Benchmarks evaluated:**
- BIG-Bench Extra Hard
- MuSR
- ZebraLogicBench
- FOLIO

The specific models used are not detailed in this abstract page.

## 7) Key Findings
The research demonstrates that REMUL "consistently and substantially improves three measures of faithfulness -- hint attribution, early answering area over the curve (AOC), and mistake injection AOC -- while also improving accuracy." Additional analysis reveals improvements are robust across training domains, translate to legibility gains, and correlate with shorter, more direct reasoning chains.

**Access:** Code available at the provided GitHub repository.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3045cb35-f795-47a6-8e0c-2a100cd0218c",
  "isSidechain": true,
  "promptId": "8029e2e4-25c6-47cb-9539-6d3b0938c122",
  "agentId": "a7ed4918e81d4960b",
  "type": "user",
  "uuid": "baee7f0a-a9db-4a31-a5ec-754039113efd",
  "sourceToolAssistantUUID": "3045cb35-f795-47a6-8e0c-2a100cd0218c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T09:12:05.614Z_

<details><summary>↩ Tool result · `toolu_01LSMSvQNmvCSFDcAVbGDcSN`</summary>

```text
# Paper Analysis: Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning

## 1) Full Title
"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning"

## 2) All Authors
- Donald Ye
- Max Loffgren
- Om Kotadia
- Linus Wong

## 3) Complete Abstract
The researchers investigate whether chain-of-thought (CoT) explanations genuinely reflect model decision-making or serve as post-hoc justifications. They introduce a metric called Normalized Logit Difference Decay (NLDD) that measures faithfulness by corrupting individual reasoning steps and observing confidence drops in model answers. Testing across three model families on syntactic, logical, and arithmetic tasks reveals a consistent threshold called Reasoning Horizon (k*) at 70-85% of chain length. Beyond this point, "reasoning tokens have little or negative effect on the final answer." They observe that models can generate correct internal representations while completely failing tasks, indicating that accuracy metrics alone don't demonstrate genuine reasoning processes.

## 4) Reasoning Horizon Phenomenon
The Reasoning Horizon (k*) represents a critical discovery: a consistent point at 70-85% through the chain where reasoning tokens cease having meaningful positive impact on model outputs. Beyond this threshold, additional reasoning steps demonstrate minimal or counterproductive effects.

## 5) Mechanistic Evidence for Faithfulness Decay
The paper employs the NLDD metric through a corruption approach: individual reasoning steps are deliberately altered, and resulting confidence degradation is measured. This standardized approach enables cross-model architectural comparisons and reveals that "accuracy alone does not reveal whether a model actually reasons through its chain."

## 6) Relation to Adversarial Pressure
The document doesn't explicitly discuss adversarial pressure on reasoning models.

## 7) Key Findings
- Consistent Reasoning Horizon threshold across tested models
- Disconnect between task completion and actual reasoning processes
- Models encode correct representations despite task failures
- NLDD provides quantifiable faithfulness measurement capability
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e606f9bb-49ee-4acd-b933-1df334d35fc4",
  "isSidechain": true,
  "promptId": "8029e2e4-25c6-47cb-9539-6d3b0938c122",
  "agentId": "a7ed4918e81d4960b",
  "type": "user",
  "uuid": "a9a46fb2-282d-49c7-b4c4-2ac9b8c97bfc",
  "sourceToolAssistantUUID": "e606f9bb-49ee-4acd-b933-1df334d35fc4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T09:12:08.340Z_

<details><summary>↩ Tool result · `toolu_013eswrjGKSQ8UW1jMe6PkZD`</summary>

```text
# Paper Analysis: "Reasoning Theater"

## 1) Full Title
"Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"

## 2) All Authors
Siddharth Boppana, Annabel Ma, Max Loeffler, Raphael Sarfati, Eric Bigelow, Atticus Geiger, Owen Lewis, Jack Merullo

## 3) Complete Abstract
The researchers document evidence that reasoning models exhibit performative chain-of-thought behavior. They note: "a model becomes strongly confident in its final answer, but continues generating tokens without revealing its internal belief." Their comparative analysis examines activation probing, early forced answering, and CoT monitoring across DeepSeek-R1 (671B) and GPT-OSS (120B).

## 4) Performative vs. Genuine Reasoning
**Performative reasoning (theater):** Models decode final answers from activations much earlier than monitors detect certainty, particularly on easy recall-based MMLU questions.

**Genuine reasoning:** Contrasts appear in difficult multihop GPQA-Diamond questions where authentic reasoning patterns emerge.

Critically, "inflection points (e.g., backtracking, 'aha' moments) occur almost exclusively in responses where probes show large belief shifts, suggesting these behaviors track genuine uncertainty rather than learned 'reasoning theater.'"

## 5) Activation Probing Methods
The study employs three complementary techniques:
- Activation probing (decoding beliefs from internal activations)
- Early forced answering (prematurely requesting final answers)
- CoT monitoring (tracking when models express confidence)

## 6) "Reasoning Theater" Evidence
The core finding demonstrates a temporal disconnect: internal model certainty arrives substantially before explicit verbal acknowledgment. Models essentially "perform" extended reasoning after deciding internally.

## 7) Key Findings & Results
- Probe-guided early exit reduces tokens by up to 80% on MMLU and 30% on GPQA-Diamond while maintaining accuracy
- Task difficulty significantly modulates these patterns
- Activation probing functions as an "efficient tool for detecting performative reasoning and enabling adaptive computation"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aec62b20-5836-4006-857f-a64b18c63478",
  "isSidechain": true,
  "promptId": "8029e2e4-25c6-47cb-9539-6d3b0938c122",
  "agentId": "a7ed4918e81d4960b",
  "type": "user",
  "uuid": "58a0f4e1-4c3b-4f5b-b22f-1985736bc7af",
  "sourceToolAssistantUUID": "aec62b20-5836-4006-857f-a64b18c63478",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-19T09:12:12.219Z_

Let me now fetch the full HTML pages for each paper to try to get additional details on models tested, methods comparisons, and relevance to adversarial faithfulness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58a0f4e1-4c3b-4f5b-b22f-1985736bc7af",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfnYqP4TMkdeAg9E7K4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "269af3b6-75a9-4f3f-9810-0a7296fefbf1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8RzjxPTu9FmNjqgLTTMg3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2100,
      "cache_read_input_tokens": 9701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2100,
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

_source line 15 · 2026-05-19T09:12:15.570Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018kRaKoxjtomjGGDsLBw6h5`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.16154",
  "prompt": "Look for any additional details beyond the abstract: 1) What specific LLM models did they use as speaker and listener? (e.g., Llama, Qwen, GPT, etc.) 2) Any mention of how REMUL compares to DPO-based faithfulness methods, counterfactual simulation, or process reward models? 3) What is the \"masked supervised finetuning\" regularization? 4) What are the specific faithfulness metrics (hint attribution, early answering AOC, mistake injection AOC) and how much did they improve? 5) Any GitHub repo link? Extract every detail you can find on the page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "269af3b6-75a9-4f3f-9810-0a7296fefbf1",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfnYqP4TMkdeAg9E7K4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46618107-4a1b-45f8-90a6-e06af7b3be6c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8RzjxPTu9FmNjqgLTTMg3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2100,
      "cache_read_input_tokens": 9701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2100,
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

_source line 16 · 2026-05-19T09:12:18.868Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TXRD1CFH1aZsH3k9rbST8j`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.11201",
  "prompt": "Look for any additional details: 1) What three model families did they test? 2) What specific tasks (syntactic, logical, arithmetic) did they use? 3) How exactly does the NLDD metric work - what does \"corrupting reasoning steps\" mean mechanistically? 4) What does it mean that \"models encode correct representations despite task failures\"? 5) Any discussion of how this relates to adversarial attacks on reasoning, or how adversarial pressure might exploit the reasoning horizon? 6) Any quantitative results about the 70-85% threshold? Extract every detail available on the page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46618107-4a1b-45f8-90a6-e06af7b3be6c",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfnYqP4TMkdeAg9E7K4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8baef235-f6da-41ad-8d15-053b6f9f5723",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8RzjxPTu9FmNjqgLTTMg3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2100,
      "cache_read_input_tokens": 9701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2100,
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

_source line 17 · 2026-05-19T09:12:20.419Z_

<details><summary>↩ Tool result · `toolu_018kRaKoxjtomjGGDsLBw6h5`</summary>

```text
# Analysis of REMUL Paper Details

Based on the provided arXiv page, here's what I found:

## Available Information

**GitHub Repository:**
The page confirms code availability: "Code: this https URL" with a link to `https://github.com/nsivaku/remul`

**Faithfulness Metrics:**
The abstract mentions three specific measures: "hint attribution, early answering area over the curve (AOC), and mistake injection AOC" — however, the exact improvement percentages are not provided on this landing page.

**Evaluation Benchmarks:**
Testing occurred on "multiple reasoning benchmarks (BIG-Bench Extra Hard, MuSR, ZebraLogicBench, and FOLIO)"

## Information NOT Found on This Page

Unfortunately, the arXiv abstract page doesn't contain:
- Specific LLM model names (speaker/listener architectures)
- Comparisons to DPO-based methods, counterfactual simulation, or process reward models
- Technical details about "masked supervised finetuning" regularization
- Numerical improvement values for the three faithfulness metrics

**To obtain these details**, you would need to access the full PDF or HTML versions available through the provided links (`/pdf/2602.16154` or the HTML experimental version), as abstract pages typically omit granular technical specifications and experimental results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46618107-4a1b-45f8-90a6-e06af7b3be6c",
  "isSidechain": true,
  "promptId": "8029e2e4-25c6-47cb-9539-6d3b0938c122",
  "agentId": "a7ed4918e81d4960b",
  "type": "user",
  "uuid": "bf847cb5-25f7-4b5f-8bf8-036765d315cd",
  "sourceToolAssistantUUID": "46618107-4a1b-45f8-90a6-e06af7b3be6c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T09:12:21.661Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018fbAXwPe16Noxyav6Tq5Pr`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.05488",
  "prompt": "Look for any additional details: 1) What specific models were tested beyond DeepSeek-R1 and GPT-OSS? 2) What is MMLU and GPQA-Diamond specifically? 3) How does the 80% token reduction on MMLU work - what is probe-guided early exit? 4) What are the \"inflection points\" like backtracking and \"aha moments\"? 5) How does this relate to faithfulness of chain-of-thought reasoning? 6) Any discussion of adversarial implications - could adversarial pressure make performative reasoning worse? 7) Any quantitative metrics on the temporal gap between internal certainty and verbal expression? Extract every detail available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf847cb5-25f7-4b5f-8bf8-036765d315cd",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfnYqP4TMkdeAg9E7K4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b688e73-3776-4d40-a4f8-d504f45068a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8RzjxPTu9FmNjqgLTTMg3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2100,
      "cache_read_input_tokens": 9701,
      "output_tokens": 677,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2100
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 677,
          "cache_read_input_tokens": 9701,
          "cache_creation_input_tokens": 2100,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2100,
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

_source line 19 · 2026-05-19T09:12:24.068Z_

<details><summary>↩ Tool result · `toolu_01TXRD1CFH1aZsH3k9rbST8j`</summary>

```text
# Analysis of arXiv Paper 2602.11201

Based on the available page content, here's what can be extracted:

## Questions 1-2: Model Families and Tasks
The page does **not specify** which three model families were tested, nor does it detail the specific syntactic, logical, or arithmetic tasks used. The abstract only states they tested "three model families across syntactic, logical, and arithmetic tasks" without naming them.

## Question 3: NLDD Mechanism
The metric works by: "corrupt[ing] individual reasoning steps from the explanation and measur[ing] how much the model's confidence in its answer drops, to determine if a step is truly important."

The page doesn't provide mechanistic details about what "corrupting" entails (e.g., ablation, masking, noise injection).

## Question 4: Correct Representations Despite Failures
The finding states: "models can encode correct internal representations while completely failing the task." The page offers no elaboration on this phenomenon's interpretation.

## Question 5: Adversarial Attacks Discussion
**Not addressed** on this page. No mention of adversarial pressure or exploitation of the reasoning horizon.

## Question 6: Quantitative Results
The threshold is identified as a "Reasoning Horizon (k*) at 70--85% of chain length, beyond which reasoning tokens have little or negative effect on the final answer."

**Note:** Full details would require accessing the PDF or HTML versions linked on the page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8baef235-f6da-41ad-8d15-053b6f9f5723",
  "isSidechain": true,
  "promptId": "8029e2e4-25c6-47cb-9539-6d3b0938c122",
  "agentId": "a7ed4918e81d4960b",
  "type": "user",
  "uuid": "db630653-bc0f-4490-bf98-9dd37931ff1e",
  "sourceToolAssistantUUID": "8baef235-f6da-41ad-8d15-053b6f9f5723",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T09:12:26.782Z_

<details><summary>↩ Tool result · `toolu_018fbAXwPe16Noxyav6Tq5Pr`</summary>

```text
# Analysis of "Reasoning Theater" Paper

Based on the arXiv abstract provided, here's what can be extracted:

## Models Tested
The abstract specifies only **two large models**: DeepSeek-R1 671B and GPT-OSS 120B. No additional models are mentioned in the available content.

## Benchmark Datasets
- **MMLU**: Characterized as "easy recall-based" questions
- **GPQA-Diamond**: Described as testing "genuine reasoning in difficult multihop" scenarios

## Probe-Guided Early Exit Mechanism
The abstract indicates this technique achieves token reduction "up to 80% on MMLU and 30% on GPQA-Diamond with similar accuracy," but specific implementation details aren't provided in this excerpt.

## Inflection Points
The paper identifies behavioral markers including "backtracking, 'aha' moments," occurring "almost exclusively in responses where probes show large belief shifts."

## Chain-of-Thought Faithfulness
The core finding suggests a **gap between internal certainty and verbal expression**: "a model becomes strongly confident in its final answer, but continues generating tokens without revealing its internal belief."

## Limitations of Available Content
The abstract does not address:
- Adversarial robustness implications
- Specific quantitative temporal measurements between activation certainty and token generation
- Detailed methodology explanations

The paper's title—**"Reasoning Theater"**—itself suggests skepticism about whether extended reasoning outputs reflect genuine deliberation versus performative behavior.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b688e73-3776-4d40-a4f8-d504f45068a9",
  "isSidechain": true,
  "promptId": "8029e2e4-25c6-47cb-9539-6d3b0938c122",
  "agentId": "a7ed4918e81d4960b",
  "type": "user",
  "uuid": "073de186-71ed-48e8-b867-d49e7d7ffeaa",
  "sourceToolAssistantUUID": "5b688e73-3776-4d40-a4f8-d504f45068a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-19T09:12:29.348Z_

Now let me try to get more details by fetching the full HTML versions of these papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "073de186-71ed-48e8-b867-d49e7d7ffeaa",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfouhHBGtNLP15QGwAf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "539bba78-47e4-42e4-86c5-72420f4d5e31",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTU8L2GyztL93AZgr4QTop",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1729,
      "cache_read_input_tokens": 11801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1729,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T09:12:32.169Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YQon4VUAcKBFGWw3wk49Nj`</summary>

```json
{
  "url": "https://html.arxiv.org/abs/2602.16154",
  "prompt": "Extract all technical details about the REMUL method: 1) What specific LLM models were used as speaker and listener? 2) How does the multi-listener reinforcement learning work step by step? 3) What is the masked supervised finetuning component? 4) How does REMUL compare to baselines or prior faithfulness methods? 5) What are the quantitative results - improvement numbers on faithfulness metrics and accuracy? 6) Any ablation studies? Give me as much detail as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "539bba78-47e4-42e4-86c5-72420f4d5e31",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfouhHBGtNLP15QGwAf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9010b9f4-5c7d-4567-ab00-243d64e5036e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTU8L2GyztL93AZgr4QTop",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1729,
      "cache_read_input_tokens": 11801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1729,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T09:12:32.395Z_

<details><summary>↩ Tool result · reported error · `toolu_01YQon4VUAcKBFGWw3wk49Nj`</summary>

```text
ECONNREFUSED
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9010b9f4-5c7d-4567-ab00-243d64e5036e",
  "isSidechain": true,
  "promptId": "8029e2e4-25c6-47cb-9539-6d3b0938c122",
  "agentId": "a7ed4918e81d4960b",
  "type": "user",
  "uuid": "80acf56e-6eea-4cc9-95a3-c0e76aa38546",
  "toolUseResult": "Error: ECONNREFUSED",
  "sourceToolAssistantUUID": "9010b9f4-5c7d-4567-ab00-243d64e5036e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T09:12:34.532Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CQZMdJxS6UdeEMtAw4cPFC`</summary>

```json
{
  "url": "https://html.arxiv.org/abs/2602.11201",
  "prompt": "Extract all technical details: 1) What three model families were tested? 2) How exactly does the NLDD (Normalized Logit Difference Decay) metric work step by step? 3) What does corrupting reasoning steps involve? 4) What specific tasks were used? 5) Quantitative results about the reasoning horizon at 70-85%. 6) What does it mean that models encode correct representations while failing tasks? 7) Any implications for adversarial robustness or faithfulness under pressure? Give me maximum detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80acf56e-6eea-4cc9-95a3-c0e76aa38546",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfouhHBGtNLP15QGwAf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5016728-99d9-43e4-8643-e676ed94e224",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTU8L2GyztL93AZgr4QTop",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1729,
      "cache_read_input_tokens": 11801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1729,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T09:12:34.538Z_

<details><summary>↩ Tool result · reported error · `toolu_01CQZMdJxS6UdeEMtAw4cPFC`</summary>

```text
Was there a typo in the url or port?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5016728-99d9-43e4-8643-e676ed94e224",
  "isSidechain": true,
  "promptId": "8029e2e4-25c6-47cb-9539-6d3b0938c122",
  "agentId": "a7ed4918e81d4960b",
  "type": "user",
  "uuid": "0238f799-1b98-4757-930a-73e87f5fc28b",
  "toolUseResult": "Error: Was there a typo in the url or port?",
  "sourceToolAssistantUUID": "c5016728-99d9-43e4-8643-e676ed94e224",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T09:12:36.427Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SYs8qpiHCpeNqHuLfhqJwQ`</summary>

```json
{
  "url": "https://html.arxiv.org/abs/2603.05488",
  "prompt": "Extract all technical details: 1) How does activation probing work in this paper? 2) What is the exact methodology for detecting performative vs genuine reasoning? 3) What are the quantitative findings about token reduction? 4) How do inflection points (backtracking, aha moments) correlate with probe belief shifts? 5) What are the implications for CoT faithfulness? 6) Any discussion of adversarial scenarios or how these findings relate to faithfulness training? Give me maximum detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0238f799-1b98-4757-930a-73e87f5fc28b",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfouhHBGtNLP15QGwAf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72c31080-dbed-4788-be1a-63c8808c883b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTU8L2GyztL93AZgr4QTop",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1729,
      "cache_read_input_tokens": 11801,
      "output_tokens": 573,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1729
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 573,
          "cache_read_input_tokens": 11801,
          "cache_creation_input_tokens": 1729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1729,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T09:12:36.436Z_

<details><summary>↩ Tool result · reported error · `toolu_01SYs8qpiHCpeNqHuLfhqJwQ`</summary>

```text
ECONNREFUSED
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72c31080-dbed-4788-be1a-63c8808c883b",
  "isSidechain": true,
  "promptId": "8029e2e4-25c6-47cb-9539-6d3b0938c122",
  "agentId": "a7ed4918e81d4960b",
  "type": "user",
  "uuid": "ab9cb6c0-ba19-4aa6-b09d-f69ffa085378",
  "toolUseResult": "Error: ECONNREFUSED",
  "sourceToolAssistantUUID": "72c31080-dbed-4788-be1a-63c8808c883b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-19T09:12:39.865Z_

The HTML versions aren't accessible. Let me try the PDF endpoints and also the Hugging Face paper pages, which sometimes have more details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab9cb6c0-ba19-4aa6-b09d-f69ffa085378",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfpd7AVsJRPBm3qbWde",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "547c0969-0ef5-46ce-b769-20b0bd67f356",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pv4Qv1aSwy7n3v5JUtA8rQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2411,
      "cache_read_input_tokens": 11801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2411,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T09:12:40.754Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WsipDpz1NE32BCo2LPsyNa`</summary>

```json
{
  "url": "https://huggingface.co/papers/2602.16154",
  "prompt": "Extract all available details about the REMUL paper \"Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution\": models used, method details, quantitative results, comparisons to baselines. Be as thorough as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "547c0969-0ef5-46ce-b769-20b0bd67f356",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfpd7AVsJRPBm3qbWde",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea4e4374-3465-48c7-a9c9-d6fbb5856ec9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pv4Qv1aSwy7n3v5JUtA8rQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2411,
      "cache_read_input_tokens": 11801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2411,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T09:12:41.480Z_

<details><summary>↩ Tool result · `toolu_01WsipDpz1NE32BCo2LPsyNa`</summary>

```text
&lt;persisted-output>
Output too large (91.7KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-gen-pipeline/d3232602-cd70-49bb-a57b-21b3ab7347ad/tool-results/toolu_01WsipDpz1NE32BCo2LPsyNa.txt

Preview (first 2KB):
Title: Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution

URL Source: https://arxiv.org/html/2602.16154

Markdown Content:
Shoubin Yu Hyunji Lee Yue Zhang Ali Payani Mohit Bansal Elias Stengel-Eskin

###### Abstract

Chain-of-thought (CoT) reasoning sometimes fails to faithfully reflect the true computation of a large language model (LLM), hampering its utility in explaining how LLMs arrive at their answers. Moreover, optimizing for faithfulness and interpretability in reasoning often degrades task performance. To address this tradeoff and improve CoT faithfulness, we propose Reasoning Execution by Multiple Listeners (REMuL), a multi-party reinforcement learning approach. REMuL builds on the hypothesis that reasoning traces which other parties can follow will be more faithful. A speaker model generates a reasoning trace, which is truncated and passed to a pool of listener models who “execute” the trace, continuing the trace to an answer. Speakers are rewarded for producing reasoning that is clear to listeners, with additional correctness regularization via masked supervised finetuning to counter the tradeoff between faithfulness and performance. On multiple reasoning benchmarks (BIG-Bench Extra Hard, MuSR, ZebraLogicBench, and FOLIO), REMuL consistently and substantially improves three measures of faithfulness – hint attribution, early answering area over the curve (AOC), and mistake injection AOC – while also improving accuracy. Our analysis finds that these gains are robust across training domains, translate to legibility gains, and are associated with shorter and more direct CoTs.1 1 1 Code: [https://github.com/nsivaku/remul](https://github.com/nsivaku/remul)

Machine Learning, ICML

![Image 1: Refer to caption](https://arxiv.org/html/2602.16154v1/x1.png)

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea4e4374-3465-48c7-a9c9-d6fbb5856ec9",
  "isSidechain": true,
  "promptId": "8029e2e4-25c6-47cb-9539-6d3b0938c122",
  "agentId": "a7ed4918e81d4960b",
  "type": "user",
  "uuid": "2c46e913-8a41-4845-ba09-c0c474c7408c",
  "sourceToolAssistantUUID": "ea4e4374-3465-48c7-a9c9-d6fbb5856ec9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T09:12:42.221Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Yc1YnLX84sxFMNzNY1prxw`</summary>

```json
{
  "url": "https://huggingface.co/papers/2602.11201",
  "prompt": "Extract all available details about \"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning\": model families tested, NLDD metric details, reasoning horizon quantitative results, implications. Be as thorough as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c46e913-8a41-4845-ba09-c0c474c7408c",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfpd7AVsJRPBm3qbWde",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "358d9255-1434-4dcc-8281-0cc9c5fedbf6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pv4Qv1aSwy7n3v5JUtA8rQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2411,
      "cache_read_input_tokens": 11801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2411,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T09:12:42.398Z_

<details><summary>↩ Tool result · `toolu_01Yc1YnLX84sxFMNzNY1prxw`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "358d9255-1434-4dcc-8281-0cc9c5fedbf6",
  "isSidechain": true,
  "promptId": "8029e2e4-25c6-47cb-9539-6d3b0938c122",
  "agentId": "a7ed4918e81d4960b",
  "type": "user",
  "uuid": "a6ec03bc-003a-4974-b8b8-548b90eeff07",
  "sourceToolAssistantUUID": "358d9255-1434-4dcc-8281-0cc9c5fedbf6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T09:12:43.131Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0117AjQicFafhxyJJ96WZwub`</summary>

```json
{
  "url": "https://huggingface.co/papers/2603.05488",
  "prompt": "Extract all available details about \"Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought\": activation probing methodology, models tested, quantitative results, performative vs genuine reasoning findings. Be as thorough as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6ec03bc-003a-4974-b8b8-548b90eeff07",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfpd7AVsJRPBm3qbWde",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71777a6e-97ff-4c24-b7f4-453701946a28",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pv4Qv1aSwy7n3v5JUtA8rQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2411,
      "cache_read_input_tokens": 11801,
      "output_tokens": 403,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2411
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 403,
          "cache_read_input_tokens": 11801,
          "cache_creation_input_tokens": 2411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2411,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T09:12:43.615Z_

<details><summary>↩ Tool result · `toolu_0117AjQicFafhxyJJ96WZwub`</summary>

```text
&lt;persisted-output>
Output too large (96.3KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-gen-pipeline/d3232602-cd70-49bb-a57b-21b3ab7347ad/tool-results/toolu_0117AjQicFafhxyJJ96WZwub.txt

Preview (first 2KB):
Title: Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought

URL Source: https://arxiv.org/html/2603.05488

Published Time: Fri, 13 Mar 2026 00:32:53 GMT

Markdown Content:
Annabel Ma Max Loeffler Raphael Sarfati Eric Bigelow Atticus Geiger Owen Lewis Jack Merullo

###### Abstract

We provide evidence of performative chain-of-thought (CoT) in reasoning models, where a model becomes strongly confident in its final answer, but continues generating tokens without revealing its internal belief. Our analysis compares activation probing, early forced answering, and a CoT monitor across two large models (DeepSeek-R1 671B & GPT-OSS 120B) and find task difficulty-specific differences: The model’s final answer is decodable from activations far earlier in CoT than a monitor is able to say, especially for easy recall-based MMLU questions. We contrast this with genuine reasoning in difficult multihop GPQA-Diamond questions. Despite this, inflection points (e.g., backtracking, ‘aha’ moments) occur almost exclusively in responses where probes show large belief shifts, suggesting these behaviors track genuine uncertainty rather than learned “reasoning theater.” Finally, probe-guided early exit reduces tokens by up to 80% on MMLU and 30% on GPQA-Diamond with similar accuracy, positioning attention probing as an efficient tool for detecting performative reasoning and enabling adaptive computation.1 1 1 Codebase: [github.com/AskSid/disentangling-computation-from-cot](https://github.com/AskSid/disentangling-computation-from-cot)2 2 2 Visualization of our data: [reasoning-theater.streamlit.app](https://reasoning-theater.streamlit.app/)

Machine Learning, ICML

## 1 Introduction

![Image 1: Refer to caption](https://arxiv.org/html/2603.05488v3/x1.png)

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71777a6e-97ff-4c24-b7f4-453701946a28",
  "isSidechain": true,
  "promptId": "8029e2e4-25c6-47cb-9539-6d3b0938c122",
  "agentId": "a7ed4918e81d4960b",
  "type": "user",
  "uuid": "a3c31541-d35d-40f5-893b-b2a496d4c977",
  "sourceToolAssistantUUID": "71777a6e-97ff-4c24-b7f4-453701946a28",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-19T09:12:47.944Z_

I got the full paper content for papers 1 and 3. Let me read the saved outputs for more detail, and try another approach for paper 2.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3c31541-d35d-40f5-893b-b2a496d4c977",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfq9eSjUv8cwgwKkNWY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5ba039e-9b3a-4d92-a4df-c0c5007fb465",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5AscghX2VQrCt8AYFNvGc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1704,
      "cache_read_input_tokens": 14212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1704,
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

_source line 36 · 2026-05-19T09:12:48.881Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VphPb5yQchL2SMH6nx6Uzq`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-gen-pipeline/d3232602-cd70-49bb-a57b-21b3ab7347ad/tool-results/toolu_01WsipDpz1NE32BCo2LPsyNa.txt",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5ba039e-9b3a-4d92-a4df-c0c5007fb465",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfq9eSjUv8cwgwKkNWY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc6a88e1-52c8-461b-a3bf-63d4ac5d54e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5AscghX2VQrCt8AYFNvGc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1704,
      "cache_read_input_tokens": 14212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1704,
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

_source line 37 · 2026-05-19T09:12:49.167Z_

<details><summary>↩ Tool result · reported error · `toolu_01VphPb5yQchL2SMH6nx6Uzq`</summary>

```text
File content (27359 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc6a88e1-52c8-461b-a3bf-63d4ac5d54e3",
  "isSidechain": true,
  "promptId": "8029e2e4-25c6-47cb-9539-6d3b0938c122",
  "agentId": "a7ed4918e81d4960b",
  "type": "user",
  "uuid": "69c41b87-5d9e-4f68-a154-63d36952d5a7",
  "toolUseResult": "Error: File content (27359 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "bc6a88e1-52c8-461b-a3bf-63d4ac5d54e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-19T09:12:49.881Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YDCeefpHvC1GN88X8ZzVK5`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-gen-pipeline/d3232602-cd70-49bb-a57b-21b3ab7347ad/tool-results/toolu_0117AjQicFafhxyJJ96WZwub.txt",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69c41b87-5d9e-4f68-a154-63d36952d5a7",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfq9eSjUv8cwgwKkNWY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3610fb9-96ba-46f4-b4a1-976a6de53578",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5AscghX2VQrCt8AYFNvGc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1704,
      "cache_read_input_tokens": 14212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1704,
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

_source line 39 · 2026-05-19T09:12:50.275Z_

<details><summary>↩ Tool result · `toolu_01YDCeefpHvC1GN88X8ZzVK5`</summary>

```text
1	Title: Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought
2	
3	URL Source: https://arxiv.org/html/2603.05488
4	
5	Published Time: Fri, 13 Mar 2026 00:32:53 GMT
6	
7	Markdown Content:
8	Annabel Ma Max Loeffler Raphael Sarfati Eric Bigelow Atticus Geiger Owen Lewis Jack Merullo
9	
10	###### Abstract
11	
12	We provide evidence of performative chain-of-thought (CoT) in reasoning models, where a model becomes strongly confident in its final answer, but continues generating tokens without revealing its internal belief. Our analysis compares activation probing, early forced answering, and a CoT monitor across two large models (DeepSeek-R1 671B & GPT-OSS 120B) and find task difficulty-specific differences: The model’s final answer is decodable from activations far earlier in CoT than a monitor is able to say, especially for easy recall-based MMLU questions. We contrast this with genuine reasoning in difficult multihop GPQA-Diamond questions. Despite this, inflection points (e.g., backtracking, ‘aha’ moments) occur almost exclusively in responses where probes show large belief shifts, suggesting these behaviors track genuine uncertainty rather than learned “reasoning theater.” Finally, probe-guided early exit reduces tokens by up to 80% on MMLU and 30% on GPQA-Diamond with similar accuracy, positioning attention probing as an efficient tool for detecting performative reasoning and enabling adaptive computation.1 1 1 Codebase: [github.com/AskSid/disentangling-computation-from-cot](https://github.com/AskSid/disentangling-computation-from-cot)2 2 2 Visualization of our data: [reasoning-theater.streamlit.app](https://reasoning-theater.streamlit.app/)
13	
14	Machine Learning, ICML
15	
16	## 1 Introduction
17	
18	![Image 1: Refer to caption](https://arxiv.org/html/2603.05488v3/x1.png)
19	
20	Figure 1: Early decoding helps us identify performative reasoning, when an LLM knows what it will answer. We study whether a reasoning LLM’s final answer can be decoded given a prefix of its chain of thought up to an intermediate token x x. We use this to identify _performative reasoning_, where a model internally knows its final answer early on but still generates text as if it does not. (1) Attention Probes: We train attention probes on varying-length activations of text to predict the model’s final answer. At test-time, we use activations up to x x to study when the model internalizes its final answer. (2) Forced Answering: At token x x, we inject a forced answering prompt to obtain its final answer prediction at that point in reasoning. (3) Chain-of-thought Monitor: We provide the chain of thought up to x x to another LLM, which determines whether the reasoning chain contains a potential final answer.
21	
22	Chain-of-thought (CoT) has emerged as a powerful method to improve Large Language Model (LLM) performance by leveraging step-by-step computation, particularly on math and science tasks that require complex reasoning(Reynolds and McDonell, [2021](https://arxiv.org/html/2603.05488#bib.bib5 "Prompt programming for large language models: beyond the few-shot paradigm"); Wei et al., [2022](https://arxiv.org/html/2603.05488#bib.bib6 "Chain-of-thought prompting elicits reasoning in large language models")). Notably, _reasoning_ LLMs trained using reinforcement learning (RL) have demonstrated impressive gains, accounting for many of the latest breakthroughs in capabilities(DeepSeek-AI, [2025](https://arxiv.org/html/2603.05488#bib.bib7 "DeepSeek-r1: incentivizing reasoning capability in llms via reinforcement learning"); OpenAI, [2024](https://arxiv.org/html/2603.05488#bib.bib8 "Learning to reason with llms")). On one hand, long CoTs, which emerge from RL training, appear to provide a promising opportunity for safety and interpretability: if we can watch the model think, we should be able to find evidence of malicious intentions or flawed logic and respond accordingly(Korbak et al., [2025](https://arxiv.org/html/2603.05488#bib.bib9 "Chain of thought monitorability: a new and fragile opportunity for ai safety")). On the other hand, recent research has shown that CoT traces are not necessarily faithful to the internal reasoning processes employed by the model(Turpin et al., [2023](https://arxiv.org/html/2603.05488#bib.bib10 "Language models don’t always say what they think: unfaithful explanations in chain-of-thought prompting"); Lanham et al., [2023](https://arxiv.org/html/2603.05488#bib.bib11 "Measuring faithfulness in chain-of-thought reasoning"); Arcuschin et al., [2025](https://arxiv.org/html/2603.05488#bib.bib12 "Chain-of-thought reasoning in the wild is not always faithful"); Chen et al., [2025](https://arxiv.org/html/2603.05488#bib.bib35 "Reasoning models don’t always say what they think")), undermining the reliability of these explanations for safety applications. In this work, we study unfaithfulness through the lens of _performative_ chain-of-thought(Palod et al., [2025](https://arxiv.org/html/2603.05488#bib.bib33 "Performative thinking? the brittle correlation between cot length and problem complexity")), which is a mismatch between external and internal deliberation: the model continues to generate tokens that read as step-by-step reasoning without disclosing its internally committed confidence.
23	
24	Our results show that models are at times strongly confident in their final answer immediately into reasoning, and this belief can be probed from the activations of the model far before any confidence is verbalized in CoT. We describe this as performative reasoning, as it is unfaithful to the model’s confident underlying belief. The full story is complicated, however. Harder tasks that require test-time compute exhibit genuine reasoning, for which this mismatch is not present. We also find that inflection points like backtracking, sudden realizations (‘aha’ moments), and reconsiderations appear almost exclusively in questions that also contain large shifts in internal confidence within CoT reasoning, signifying faithful expressions of internal uncertainty resolution. Our probes are able to distinguish both of these phenomena from performative CoT; this degree of calibration has the added benefit of giving us an early exit signal that generalizes to a task the probes weren’t trained on (§[7](https://arxiv.org/html/2603.05488#S7 "7 Attention Probes for Early Exit ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought")).
25	
26	We argue CoT monitors are at best cooperative listeners, but reasoning models are not cooperative speakers(Grice, [1975](https://arxiv.org/html/2603.05488#bib.bib37 "Logic and conversation")), and many failures in CoT faithfulness can be explained by this framing. Thus, we suggest caution in assuming the settings CoT monitors are effective, and propose an activation monitoring strategy that helps cover the failure cases we describe. We make the following contributions:
27	
28	1.   1.
29	We propose activation attention probes as an effective way to decode concepts from long-form chain-of-thought reasoning. We train these probes to predict the model’s final answer and evaluate them throughout generation to track how the model’s belief state evolves over time (§[4](https://arxiv.org/html/2603.05488#S4 "4 Attention Probe Results ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought")).
30	
31	2.   2.
32	Evidence for difficulty-dependent performative reasoning. We find a difficulty-dependent split, extending prior work (Palod et al., [2025](https://arxiv.org/html/2603.05488#bib.bib33 "Performative thinking? the brittle correlation between cot length and problem complexity")). On MMLU-Redux, CoTs are often performative: answer information is available well before a CoT monitor indicates a conclusion, as opposed to on GPQA-Diamond, which exhibits more genuine reasoning. As model size increases, a similar trend arises: smaller, less capable models require more test-time compute to reach a final answer (§[5](https://arxiv.org/html/2603.05488#S5 "5 Easier Tasks Exhibit More Performative Reasoning ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought")).
33	
34	3.   3.
35	Inflection points correspond with internal uncertainty at the question level. We find that not all extended reasoning is performative: inflection points corresponding to backtracking or ‘aha’ moments are consistent indicators of genuine belief updates. Responses that have consistent high internal confidence contain fewer inflections, but we find inconsistent results on whether inflections directly coincide with belief updates within a trace (§[6](https://arxiv.org/html/2603.05488#S6 "6 Inflection Points Suggest Faithful Reasoning ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought")).
36	
37	4.   4.
38	Practical token savings via calibrated early exit. We demonstrate that our attention probes trained on reasoning prefixes are well-calibrated, enabling confidence-based early exit that substantially reduces generation without sacrificing accuracy. Early exit saves 80% and 30% of generated tokens on MMLU-Redux and GPQA-Diamond, respectively, with comparable performance (§[7](https://arxiv.org/html/2603.05488#S7 "7 Attention Probes for Early Exit ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought")).
39	
40	## 2 Related Work
41	
42	Faithfulness in language model chain-of-thought explanations. A growing body of work has investigated the faithfulness of chain-of-thought, showing that models can omit the true causes of their decisions. Models can produce plausible but unfaithful rationales, both under explicit interventions and natural settings(Turpin et al., [2023](https://arxiv.org/html/2603.05488#bib.bib10 "Language models don’t always say what they think: unfaithful explanations in chain-of-thought prompting"); Lanham et al., [2023](https://arxiv.org/html/2603.05488#bib.bib11 "Measuring faithfulness in chain-of-thought reasoning"); Arcuschin et al., [2025](https://arxiv.org/html/2603.05488#bib.bib12 "Chain-of-thought reasoning in the wild is not always faithful"); Agarwal et al., [2024](https://arxiv.org/html/2603.05488#bib.bib45 "Faithfulness vs. plausibility: on the (un) reliability of explanations from large language models")). This has direct implications for safety proposals that rely on monitoring CoT, which has been framed as a promising but fragile opportunity for detecting misalignment(Korbak et al., [2025](https://arxiv.org/html/2603.05488#bib.bib9 "Chain of thought monitorability: a new and fragile opportunity for ai safety")). Subsequent work has stress-tested CoT monitoring and identified settings where solely relying on textual reasoning fails to reveal critical internal information(Arnav et al., [2025](https://arxiv.org/html/2603.05488#bib.bib18 "CoT red-handed: stress testing chain-of-thought monitoring"); Baker et al., [2025](https://arxiv.org/html/2603.05488#bib.bib20 "Monitoring reasoning models for misbehavior and the risks of promoting obfuscation"); Wang et al., [2025](https://arxiv.org/html/2603.05488#bib.bib26 "Is it thinking or cheating? detecting implicit reward hacking by measuring reasoning effort"); Emmons et al., [2025](https://arxiv.org/html/2603.05488#bib.bib27 "When chain of thought is necessary, language models struggle to evade monitors")), identified brittle correlation between CoT length and problem difficulty(Palod et al., [2025](https://arxiv.org/html/2603.05488#bib.bib33 "Performative thinking? the brittle correlation between cot length and problem complexity")), as well as explored whether misaligned or high-risk behavior can be predicted before a model finishes reasoning(Chan et al., [2025](https://arxiv.org/html/2603.05488#bib.bib21 "Can we predict alignment before models finish thinking? towards monitoring misaligned reasoning models")). Other work has shown that monitoring may be well-suited for faithfulness(Kadavath et al., [2022](https://arxiv.org/html/2603.05488#bib.bib42 "Language models (mostly) know what they know"); Mayne et al., [2026](https://arxiv.org/html/2603.05488#bib.bib44 "A positive case for faithfulness: llm self-explanations help predict model behavior")), finding that explanations have predictive power.
43	
44	Although unfaithful CoT is well-documented, predicting how and when it will be unfaithful continues to be difficult. Traditional interpretability tools are ill-equipped to interpret information flow along the sequence dimension, focusing instead on single token activations or layer-wise signals which scale poorly to very long contexts(Wang et al., [2022](https://arxiv.org/html/2603.05488#bib.bib14 "Interpretability in the wild: a circuit for indirect object identification in GPT-2 small"); Dunefsky et al., [2024](https://arxiv.org/html/2603.05488#bib.bib13 "Transcoders find interpretable LLM feature circuits"); Ameisen et al., [2025](https://arxiv.org/html/2603.05488#bib.bib25 "Circuit tracing: revealing computational graphs in language models")). Black-box approaches study longer responses directly via the output text, such as through CoT monitors(Emmons et al., [2025](https://arxiv.org/html/2603.05488#bib.bib27 "When chain of thought is necessary, language models struggle to evade monitors"); Arnav et al., [2025](https://arxiv.org/html/2603.05488#bib.bib18 "CoT red-handed: stress testing chain-of-thought monitoring")) or resampling(Bigelow et al., [2025](https://arxiv.org/html/2603.05488#bib.bib3 "Forking paths in neural text generation"); Bogdan et al., [2025](https://arxiv.org/html/2603.05488#bib.bib19 "Thought anchors: which LLM reasoning steps matter?"); Macar et al., [2025](https://arxiv.org/html/2603.05488#bib.bib31 "Thought branches: interpreting llm reasoning requires resampling")). While resampling can be an effective causal analysis tool, thorough analysis of even simple behaviors can be cost-prohibitive, especially for models in the hundreds of billions of parameters, or with very long CoTs, like those studied here.
45	
46	Activation Probing. Activation probing is a practical way to extract latent information from a model’s internals by training lightweight linear classifiers on residual stream activations(Alain and Bengio, [2016](https://arxiv.org/html/2603.05488#bib.bib32 "Understanding intermediate layers using linear classifier probes"); Belinkov, [2022](https://arxiv.org/html/2603.05488#bib.bib38 "Probing classifiers: promises, shortcomings, and advances")). Recent work uses probes for safety applications(McKenzie et al., [2025](https://arxiv.org/html/2603.05488#bib.bib2 "Detecting high-stakes interactions with activation probes")), predicting reasoning model correctness and self-verification(Zhang et al., [2025](https://arxiv.org/html/2603.05488#bib.bib16 "Reasoning models know when they’re right: probing hidden states for self-verification")), and analyzing hidden uncertainty and branching dynamics during generation(Zur et al., [2025](https://arxiv.org/html/2603.05488#bib.bib15 "Are language models aware of the road not taken? token-level uncertainty and hidden state dynamics"); Ahdritz et al., [2024](https://arxiv.org/html/2603.05488#bib.bib43 "Distinguishing the knowable from the unknowable with language models")). Prior work has examined when sparse or structured probes meaningfully improve interpretability and monitoring(Kantamneni et al., [2025](https://arxiv.org/html/2603.05488#bib.bib1 "Are sparse autoencoders useful? A case study in sparse probing")). Our use of attention pooling probes, which uses attention to pool a set of activations together, builds on this literature by tracking answer information over the course of a reasoning trace and evaluating probe calibration for early exit.
47	
48	Reasoning Model Interpretability. Recent work in reasoning model interpretability has sought to understand the internal mechanisms underlying chain-of-thought computation. Sentence-level analysis has identified which reasoning steps are causally important for final answers(Bogdan et al., [2025](https://arxiv.org/html/2603.05488#bib.bib19 "Thought anchors: which LLM reasoning steps matter?")), while comparative studies have evaluated differences between base and reasoning models, suggesting that reasoning models repurpose pre-trained knowledge(Venhoff et al., [2025a](https://arxiv.org/html/2603.05488#bib.bib23 "Base models know how to reason, thinking models learn when")). Our work complements these approaches by examining information flow at the token level throughout generation, tracking when answer representations emerge relative to their expression in the reasoning trace.
49	
50	Cooperative Communication Grice ([1975](https://arxiv.org/html/2603.05488#bib.bib37 "Logic and conversation")) propose maxims of communication that effective and pragmatic communicators abide by. It is interesting to consider CoT monitoring from this perspective. Prior work models informative interactions between speakers and listeners under rational speech acts (RSA) (Frank and Goodman, [2012](https://arxiv.org/html/2603.05488#bib.bib46 "Predicting pragmatic reasoning in language games"); Goodman and Stuhlmüller, [2013](https://arxiv.org/html/2603.05488#bib.bib47 "Knowledge and implicature: modeling language understanding as social cognition")) and connects this to linguistic pragmatics (Goodman and Frank, [2016](https://arxiv.org/html/2603.05488#bib.bib48 "Pragmatic language interpretation as probabilistic inference"); Levinson, [1983](https://arxiv.org/html/2603.05488#bib.bib49 "Pragmatics")). Currently, reasoning models are perhaps only indirectly optimized for effective/pragmatic communication (if at all), and it may be productive to understand monitoring shortcomings from this perspective, as well as a way to improve monitorability. We touch on these principles here, but future work may develop this framing further.
51	
52	![Image 2: Refer to caption](https://arxiv.org/html/2603.05488v3/x2.png)
53	
54	![Image 3: Refer to caption](https://arxiv.org/html/2603.05488v3/x3.png)
55	
56	Figure 2: Accuracy of three early decoding methods by position of DeepSeek-R1 and GPT-OSS on MMLU-Redux and GPQA-Diamond.MMLU (left): For both models, probing and forced answering predict the models’ predictions with much higher accuracy earlier than CoT Monitoring. The CoT monitor’s accuracy rapidly gains relative to the other two methods, indicating performative CoT that did not lead to the model’s internal accuracy improving. GPQA-D (right): All three methods begin with similar accuracy around chance performance, and generally increase at similar rates, indicating closer tracking between internal beliefs and CoT. This is genuine, as the CoT generated corresponds to gains in performance seen in probes and forced answering.
57	
58	## 3 Methods
59	
60	We use three methods to determine when models know their final answer during a reasoning trace, each with different levels of privileged information from generation: probes trained on layer activations, forced answer prompting, and a CoT monitor. Each method predicts the model’s final answer from some prefix of reasoning, making it possible to track when answer information can be decoded exclusively from linear directions in activation space, a few extra forward passes, or the response text itself. A high level overview of the three methods is shown in Figure [1](https://arxiv.org/html/2603.05488#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought").
61	
62	### 3.1 Models & Datasets
63	
64	We focus our CoT analysis primarily on DeepSeek-R1-0528 671B(DeepSeek-AI, [2025](https://arxiv.org/html/2603.05488#bib.bib7 "DeepSeek-r1: incentivizing reasoning capability in llms via reinforcement learning")) and GPT-OSS 120B(Agarwal et al., [2025](https://arxiv.org/html/2603.05488#bib.bib28 "Gpt-oss-120b & gpt-oss-20b model card")), two open-weight reasoning models with frontier performance on verifiable domains such as math and science. We additionally include analysis on the set of distilled DeepSeek-R1 Qwen2.5 models (1.5B, 7B, 14B, 32B) to study the effect of model size and capability on performative reasoning.
65	
66	We evaluate these reasoning models on MMLU-Redux 2.0(Gema et al., [2025](https://arxiv.org/html/2603.05488#bib.bib17 "Are we done with MMLU?")) and GPQA-Diamond(Rein et al., [2023](https://arxiv.org/html/2603.05488#bib.bib22 "GPQA: a graduate-level google-proof q&a benchmark")), two popular benchmarks requiring both domain-specific knowledge and step-by-step reasoning skills. MMLU-Redux-2.0 is composed of 5700 questions across 57 domains, which we filter down to 5280 questions using provided error annotations. GPQA-Diamond is a harder subset of the GPQA dataset, containing 198 questions requiring graduate-level expertise in biology, chemistry, and physics. These benchmarks are both in multiple-choice format with four options (A-D), allowing us train probes with a classification objective across answer choices rather than decoding the exact semantic answer.
67	
68	We collect model responses on both datasets using the same inference settings reported by the original authors, and include these details in Appendix[A.1](https://arxiv.org/html/2603.05488#A1.SS1 "A.1 Model Inference Details ‣ Appendix A Inference and Prompting Details ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). When doing analysis at the step level, the reasoning portion of the response (between the <&lt;think>> and <&lt;/think>> tags) is split into paragraphs using the ‘\n\n’ delimiter. To train probes, we collected activations from every layer at every token of the responses.
69	
70	### 3.2 Attention Probes
71	
72	Let ℳ\mathcal{M} be a transformer language model with L L layers processing an input sequence 𝐱=(x 1,…,x T)\mathbf{x}=(x_{1},\ldots,x_{T}). We denote the hidden state at layer ℓ∈{1,…,L}\ell\in\{1,\ldots,L\} and token position t∈{1,…,T}t\in\{1,\ldots,T\} as 𝐡 t(ℓ)∈ℝ d\mathbf{h}_{t}^{(\ell)}\in\mathbb{R}^{d}, where d d is the model’s hidden dimension.
73	
74	Given a reasoning trace prefix generated by ℳ\mathcal{M}, let 𝐇(ℓ)=(𝐡 1(ℓ),…,𝐡 T(ℓ))\mathbf{H}^{(\ell)}=(\mathbf{h}_{1}^{(\ell)},\ldots,\mathbf{h}_{T}^{(\ell)}) denote the sequence of hidden states at layer ℓ\ell for the first T T response tokens. An attention probe f θ:ℝ d×T→ℝ C f_{\theta}:\mathbb{R}^{d\times T}\rightarrow\mathbb{R}^{C} performs multi-way classification over C C answer choices via attention-weighted pooling of the model’s hidden states:
75	
76	𝐳=𝐖 v​𝐇(ℓ)⋅softmax​(𝐖 q​𝐇(ℓ))\mathbf{z}=\mathbf{W}_{v}\mathbf{H}^{(\ell)}\cdot\text{softmax}(\mathbf{W}_{q}\mathbf{H}^{(\ell)})(1)
77	
78	where 𝐖 q∈ℝ 1×d\mathbf{W}_{q}\in\mathbb{R}^{1\times d} computes attention weights and 𝐖 v∈ℝ C×d\mathbf{W}_{v}\in\mathbb{R}^{C\times d} projects to answer logits(Kantamneni et al., [2025](https://arxiv.org/html/2603.05488#bib.bib1 "Are sparse autoencoders useful? A case study in sparse probing")). The probe is trained on a fixed layer ℓ\ell using cross-entropy loss across all token positions in each reasoning trace.
79	
80	During training, we sample random prefixes of the full sequence to encourage the probe to decode the final answer independent of sequence length. At inference time, we evaluate the probe at every prefix position, yielding a probability distribution over answer choices that evolves throughout generation. For each model, we train one probe per layer; results are reported using the best-performing layer across all sequence positions (all layers reported in Appendix [E](https://arxiv.org/html/2603.05488#A5 "Appendix E Probe Accuracy Heatmaps ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought")).
81	
82	### 3.3 Forced Answering
83	
84	Forced answer prompting (i.e., early answering) is a method that has been used for validating whether models rely on their chain-of-thought reasoning(Lanham et al., [2023](https://arxiv.org/html/2603.05488#bib.bib11 "Measuring faithfulness in chain-of-thought reasoning"); Wang et al., [2026](https://arxiv.org/html/2603.05488#bib.bib41 "Is it thinking or cheating? detecting implicit reward hacking by measuring reasoning effort")). Given a reasoning trace, we truncate at some intermediate step and prompt the same model to provide its final answer choice (A-D), bypassing the remaining steps. We gather predictions by taking the logits for the four classes and computing the softmax over them to obtain a probability distribution. The model’s forced answer has access to all layers’ activations from previous text, and can aggregate information to make its final prediction as there are a few forward passes before the final answer is generated. We include our forced answering prompt in Appendix[A.2](https://arxiv.org/html/2603.05488#A1.SS2 "A.2 Forced Answer Prompt ‣ Appendix A Inference and Prompting Details ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought").
85	
86	### 3.4 Chain of Thought Monitoring
87	
88	A CoT monitor is a LLM for evaluating another model’s response, often used in safety settings to detect misaligned behavior(Korbak et al., [2025](https://arxiv.org/html/2603.05488#bib.bib9 "Chain of thought monitorability: a new and fragile opportunity for ai safety")). We use a CoT monitor for two distinct purposes:
89	
90	##### Predicting the final answer:
91	
92	Given a question, our CoT monitor is prompted to predict whether the reasoning model has committed to a final answer from a prefix of reasoning steps. The monitor either predicts one of the four choices, or outputs ‘N/A’ if the partial CoT is not sufficient to predict the final answer. Allowing the monitor to defer to ‘N/A’ de-incentivizes it from computing the answer based on its own knowledge.
93	
94	##### Identifying inflection points:
95	
96	We additionally (separately) prompt the CoT monitor to identify key inflection steps in responses, looking for three types: backtracking, realizations, and reconsiderations, and record the steps at which they occur.
97	
98	We use Gemini-2.5-Flash as our CoT monitor(Comanici et al., [2025](https://arxiv.org/html/2603.05488#bib.bib29 "Gemini 2.5: pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities")) and provide both prompts in Appendix[A.3](https://arxiv.org/html/2603.05488#A1.SS3 "A.3 Chain-of-Thought Monitor Details ‣ Appendix A Inference and Prompting Details ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought").
99	
100	### 3.5 Performativity
101	
102	We define _performativity_ as the gap in accuracy between the CoT monitor and the probe or forced answer methods. If the probe (resp. forced answer) is correct and has near certainty at an earlier point in the sequence, then the reasoning steps following this point are performative, since the model’s confidence in an answer is not verbalized.
103	
104	## 4 Attention Probe Results
105	
106	We train attention probes per layer of both DeepSeek-R1 and GPT-OSS, along with the DeepSeek-R1 Qwen distilled models on MMLU questions, and evaluate on a held-out set of MMLU (N=528) and GPQA-D (N=157). We experiment with both direct transfer and fine-tuning on a set of 20 questions, and find negligible improvement for fine-tuning in terms of overall probe accuracy.
107	
108	Traditional linear probes fail at this task, performing near chance across layers and positions (Appendix[C](https://arxiv.org/html/2603.05488#A3 "Appendix C Attention Probe vs. Baselines ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought")). A single token’s activation is unlikely to consistently encode the final answer across arbitrary positions in a long reasoning trace, as the belief state updates dynamically at specific tokens. On the other hand, attention probes pool across the sequence dimension, allowing relevant token representations to be weighted higher, and succeed where linear probes do not. We find a distinct relation between layer and final answer prediction accuracy: the second half of layers in DeepSeek-R1 and the last three quarters of GPT-OSS layers can decode the final answer (Appendix[E](https://arxiv.org/html/2603.05488#A5 "Appendix E Probe Accuracy Heatmaps ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought")).
109	
110	## 5 Easier Tasks Exhibit More Performative Reasoning
111	
112	Probes and forced answering provide us with final answer predictions based on the model’s internals, while also providing a level of confidence in their predictions. A CoT monitor measures whether the model has indicated a final answer in its CoT up to a certain step. Comparing these two types of methods allows us to study performative CoT in two ways. If probes and forced answering are much more accurate than the monitor at a specific timestep, the model has not revealed its current belief. Informally, we define performativity as this gap. We find that harder tasks exhibit genuine reasoning, where the CoT is necessary and probe confidence and CoT monitor accuracy increase together. Meanwhile easier tasks are much more performative, where a spike in probe or forced answer confidence early in the CoT precedes the monitor reaching its predictions.
113	
114	### 5.1 Dataset Dependent Trends
115	
116	Table 1: Comparison of the amount of information gained per step for the CoT Monitor vs. the Probe/Forced Answer. A large difference indicates that the LLM does not produce its answer based on the addition of information from the CoT while small differences indicate more genuine reasoning. This is measured as the change in slope of the average probe (or forced answer) accuracy minus CoT accuracy shown in Fig. [2](https://arxiv.org/html/2603.05488#S2.F2 "Figure 2 ‣ 2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"): |Δ​Probe−Δ​Monitor||\Delta\text{Probe}-\Delta\text{Monitor}|
117	
118	Figure[2](https://arxiv.org/html/2603.05488#S2.F2 "Figure 2 ‣ 2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought") shows the relative accuracies of our three early decoding methods across both DeepSeek-R1 and GPT-OSS, and MMLU and GPQA-D. We collect predictions by step between the <&lt;think>> and <&lt;/think>> tokens in a response.
119	
120	We find that much of the initial reasoning done in chain-of-thought is performative across both models, with both probes and forced answering showing high accuracy from the beginning of reasoning, while the CoT monitor cannot identify the indicated answer until later. This gap is significantly larger for MMLU than GPQA-D, likely because MMLU questions mainly require recall rather than multi-hop reasoning. For GPQA-D, accuracy for all three methods increases gradually over the reasoning trace, with probes and forced answering still ahead but starting much lower. This shows the necessity of CoT for answering harder questions, in which the rate of information gain per reasoning step is reflected by the probe and CoT monitor, while easier questions exhibit much more performative reasoning.
121	
122	##### Performativity Rate
123	
124	To quantify how much each reasoning step increases probe or forced answer accuracy relative to the CoT monitor, we compute the difference in slopes between the two types of methods at each 5% timestep bin, averaged over questions and bins. We apply a quadratic fit before computing slopes to smooth over response-count variance, which is particularly pronounced for GPT-OSS due to having fewer reasoning steps overall.
125	
126	Table[1](https://arxiv.org/html/2603.05488#S5.T1 "Table 1 ‣ 5.1 Dataset Dependent Trends ‣ 5 Easier Tasks Exhibit More Performative Reasoning ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought") shows average performativity rate across models and datasets. Under this measurement, both the probe and forced answer show that MMLU is much more performative than GPQA-D: in R1, MMLU has a performativity measure of 0.417, whereas GPQA-D is 0.012. A rate near 0 means added tokens roughly translate to similar increases in both probe and monitor accuracy, indicating genuine reasoning. This trend holds for both models and for forced answering, confirming that MMLU performance does not improve with more tokens relative to the monitor, while GPQA-D shows matched incremental gains. Together, the initial difference in final answer decoding accuracy along with the difference in accuracy slope over sequence length between probes/forced answering and the CoT monitor shows a clear trend of performative CoT for MMLU: models know their final answer early, and do not benefit from additional CoT compared to a monitor.
127	
128	### 5.2 Model Size Dependent Trends
129	
130	If harder tasks lead to more faithful CoT, are smaller models more faithful than large models on equivalent datasets? We conduct the same analysis on the DeepSeek-R1 model family, comparing our three early decoding methods on each distilled model’s MMLU responses. We exclude GPQA-D from this analysis as the task is too difficult for smaller models, causing answer choice collapse that confounds early decoding.
131	
132	![Image 4: Refer to caption](https://arxiv.org/html/2603.05488v3/x4.png)
133	
134	Figure 3: Probe accuracy across DeepSeek-R1 model sizes on MMLU-Redux. Larger models achieve higher probe accuracy earlier in reasoning, likely reflecting greater in-weights knowledge. The 671B probe reaches high accuracy quickly and plateaus, the distilled models (7B–32B) remain flat before rising late in the sequence, and the 1.5B probe starts near chance and sharply increases only in the second half of reasoning.
135	
136	Figure [3](https://arxiv.org/html/2603.05488#S5.F3 "Figure 3 ‣ 5.2 Model Size Dependent Trends ‣ 5 Easier Tasks Exhibit More Performative Reasoning ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought") shows probe accuracy over reasoning for each distill along with the original R1 model used earlier. We find that in MMLU responses the final answer can be decoded with greater accuracy at the beginning of reasoning as model size increases. All models converge towards perfect accuracy during reasoning, with the 1.5B model’s best probe reaching it at a slower rate in the first half of reasoning. Surprisingly, performance for the 7B, 14B, and 32B model’s best probes are largely similar, suggesting comparable ability to decode the final answer information in this model size regime.
137	
138	![Image 5: Refer to caption](https://arxiv.org/html/2603.05488v3/x5.png)
139	
140	Figure 4: Probe performance vs. other methods by model size. When comparing probes to forced answering, we see that the gap between them rises during reasoning for distilled models due to probe performance increasing while forced answering performance stays the same. In contrast, the gap between probes and the CoT monitor decreases over reasoning. We find that smaller models are less performative as the task is more difficult, requiring genuine reasoning.
141	
142	Comparing to forced answering and CoT monitoring (Figure [4](https://arxiv.org/html/2603.05488#S5.F4 "Figure 4 ‣ 5.2 Model Size Dependent Trends ‣ 5 Easier Tasks Exhibit More Performative Reasoning ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought")), forced answering accuracy improves relative to probe accuracy as model size increases, potentially due to the off-policy nature of the prompting scheme. All model sizes are able to eventually decode the final answer towards the end of the reasoning trace. Smaller models show a smaller probe-to-monitor gap, particularly in the first half of reasoning, suggesting they generate more faithful CoT relative to their internal beliefs due to a weaker prior on answer choices. However, we note that the 671B DeepSeek-R1’s probe performance gap with the CoT monitor rapidly drops relative to smaller models, implying that the CoT “catches up” to internal beliefs faster over reasoning. Model size seems to be correlated with performative reasoning, with smaller models needing to employ more test-time compute to solve the same problem. We include comparisons of the three decoding methods’ accuracy per distilled model separately in Appendix[F](https://arxiv.org/html/2603.05488#A6 "Appendix F Probe vs. Forced Answering vs. CoT Monitor for Distilled R1 Models ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought").
143	
144	## 6 Inflection Points Suggest Faithful Reasoning
145	
146	We have shown evidence for performative CoT in the sense that models do not convey that they are highly confident. Here, we investigate the extent to which individual steps betray this. We look at inflection points in reasoning like backtracking (DeepSeek-AI, [2025](https://arxiv.org/html/2603.05488#bib.bib7 "DeepSeek-r1: incentivizing reasoning capability in llms via reinforcement learning"); Ward et al., [2025](https://arxiv.org/html/2603.05488#bib.bib39 "Reasoning-finetuning repurposes latent representations in base models"); Venhoff et al., [2025b](https://arxiv.org/html/2603.05488#bib.bib40 "Understanding reasoning in thinking language models via steering vectors")) or ‘Aha’ realizations as points of interest. If the model produces these even when it is highly confident internally, these would be highly unfaithful. We have the same CoT monitor label each reasoning step as one of: backtracking, realizations (‘aha’s), reconsiderations, or not an inflection (see §[3.4](https://arxiv.org/html/2603.05488#S3.SS4 "3.4 Chain of Thought Monitoring ‣ 3 Methods ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought")) and analyze their occurrences compared to probe confidences.
147	
148	Table 2: Inflection points by probe confidence level for DeepSeek-R1 on MMLU (probe layer 60). Highly confident CoTs produce dramatically fewer inflection points per step, suggesting that when they do show up, they are genuine.
149	
150	### 6.1 Inflection Points Occur in Less Confident Responses
151	
152	##### Setup
153	
154	First, we label reasoning steps across traces as High Confidence if the probe begins the reasoning trace at 90% or above confidence in its final answer, and never falls below that threshold throughout the CoT. This criterion basically selects for the most performative CoTs. For this experiment, we look at R1’s MMLU traces, which are the most performative, and find 215/522 are High Confidence.
155	
156	##### Results
157	
158	Table[2](https://arxiv.org/html/2603.05488#S6.T2 "Table 2 ‣ 6 Inflection Points Suggest Faithful Reasoning ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought") shows the distribution of inflections across confidence levels, controlled for the number of steps in a response. We find inflections appear twice as often when the model is not internally confident, indicating that when inflections appear, they are genuine. Reconsiderations occur significantly more often than realizations and backtracks, making up 1.4% of all high confidence response steps and 3.2% of all other response steps. This suggests that inflections are not performative, as they occur more in less confident responses, and indicates that they faithfully reflect internal computation resolving or increasing uncertainty.
159	
160	![Image 6: Refer to caption](https://arxiv.org/html/2603.05488v3/x6.png)
161	
162	Figure 5: Rate of inflection points occurring within windows beginning with probe shifts and windows containing no probe shifts. We observe that reconsideration points occur twice as often for 20% confidence shifts of the highest probability answer choice for MMLU with a window size of 10 steps ahead, but find no other significant trend for other answer types or for any inflections in GPQA-D.
163	
164	### 6.2 Inflection Points do not Reliably Occur with Shifts in Confidence
165	
166	##### Setup
167	
168	Having shown that inflection points occur in less confident responses, we study whether there is a simple local relationship between probe jumps and inflection points, e.g., a belief shift always preceding a CoT within some window. We measure temporal co-occurrence by asking two questions: given an inflection, does a probe shift occur within the next n steps more often than in windows without inflections? And conversely, given a probe shift, does an inflection follow within n steps more often than in windows without probe shifts? A probe shift is defined as a 20% change in the highest probability answer between two consecutive steps, and the window size is defined as 10 steps.
169	
170	##### Results
171	
172	Across models and datasets, we obtain mixed results, indicating no simple pattern of causality. For DeepSeek-R1 on MMLU, reconsideration inflections occur twice as often after probe shifts than in windows without probe shifts, suggesting that verbalized reconsiderations tend to follow internal belief updates. However, this relationship does not hold for GPQA-D, and the reverse direction (inflection →\rightarrow probe shift) shows little to no difference for either dataset. For GPT-OSS, the pattern reverses: inflections appear to precede probe shifts on both MMLU and GPQA-D, suggesting that for this model, verbalization may drive rather than follow internal updates. The trend also flips for GPQA-D on MMLU, where inflections occur less often after probe shifts than after non-probe-shift windows. Varying the window size and confidence threshold changes these trends substantially (Appendix[I](https://arxiv.org/html/2603.05488#A9 "Appendix I Additional Inflection Analysis ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought")), suggesting the results are sensitive to these choices. We conclude that the relationship between verbalized inflections and internal confidence shifts is not consistently captured by local windowed co-occurrence. The timing of internal belief updates relative to their verbalization appears to vary across individual responses, datasets, and models. We suggest that further work and deeper analysis is needed to connect changes in internal belief states to verbalized inflection points.
173	
174	![Image 7: Refer to caption](https://arxiv.org/html/2603.05488v3/x7.png)
175	
176	(a)Example of performative reasoning. The model is internally very confident about its final answer from the first step of reasoning, yet states that it needs to “recall the term”.
177	
178	![Image 8: Refer to caption](https://arxiv.org/html/2603.05488v3/x8.png)
179	
180	(b)Example of genuine reasoning. The model’s internal belief shifts locally within the response around the same time it has a realization about Python syntax. This correspondance between CoT and probe confidence indicates genuine reasoning.
181	
182	Figure 6: Comparison of performative vs. genuine reasoning in DeepSeek-R1 MMLU responses.
183	
184	### 6.3 Case Study Examples
185	
186	To study how probe confidence, chain-of-thought, and specific inflection points co-occur, we include two examples from DeepSeek-R1 responses in Figures [6(a)](https://arxiv.org/html/2603.05488#S6.F6.sf1 "Figure 6(a) ‣ Figure 6 ‣ Results ‣ 6.2 Inflection Points do not Reliably Occur with Shifts in Confidence ‣ 6 Inflection Points Suggest Faithful Reasoning ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought") and [6(b)](https://arxiv.org/html/2603.05488#S6.F6.sf2 "Figure 6(b) ‣ Figure 6 ‣ Results ‣ 6.2 Inflection Points do not Reliably Occur with Shifts in Confidence ‣ 6 Inflection Points Suggest Faithful Reasoning ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). We show probe confidence at the step-level over the course of reasoning and highlight key steps as well as inflections identified by the CoT monitor. Probe, forced answering, and CoT monitor predictions for each response (for both DeepSeek-R1 and GPT-OSS on our MMLU test set and GPQA-D) along with identified inflections can be found at [reasoning-theater.streamlit.app](http://reasoning-theater.streamlit.app/).
187	
188	##### Performative CoT in MMLU:
189	
190	In Figure[6(a)](https://arxiv.org/html/2603.05488#S6.F6.sf1 "Figure 6(a) ‣ Figure 6 ‣ Results ‣ 6.2 Inflection Points do not Reliably Occur with Shifts in Confidence ‣ 6 Inflection Points Suggest Faithful Reasoning ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"), we study a question that mainly requires recall about a history term. The trained attention probe is highly confident in answer choice B from the beginning of reasoning (directly after the prompt finishes) with over 90% confidence. Despite this, it states it needs to ‘recall’ the term. During the CoT, the model reasons three separate times explicitly over each of the four options, with no change in internal confidence. This is likely performative reasoning, as the model knows its final answer with high confidence yet continues to generate CoT as if it is solving the question.
191	
192	##### Genuine CoT in MMLU:
193	
194	In Figure[6(b)](https://arxiv.org/html/2603.05488#S6.F6.sf2 "Figure 6(b) ‣ Figure 6 ‣ Results ‣ 6.2 Inflection Points do not Reliably Occur with Shifts in Confidence ‣ 6 Inflection Points Suggest Faithful Reasoning ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"), we study a question about Python syntax. The trained attention probe is more confident in answer choice B at the beginning of reasoning, following Python 2 syntax. This increases significantly to 90% confidence after reasoning about each choice. However, at step 38 the model focuses on Python 3, and observes the difference between versions for tuples. This leads to a correction, both in CoT and probe predictions. The CoT here matches probe confidence more closely, and changes in beliefs are reflected.
195	
196	## 7 Attention Probes for Early Exit
197	
198	![Image 9: Refer to caption](https://arxiv.org/html/2603.05488v3/x9.png)
199	
200	Figure 7: Calibration curves for the most accurate attention probes for DeepSeek-R1 on MMLU and GPQA-Diamond. Both probes are well-calibrated, closely tracking perfect calibration.
201	
202	Our experiments provide evidence that models reach a final answer well before they are done verbalizing chain of thought. In this section, we evaluate how well we can use features from internal activations to accurately and precisely signal early exit across tasks. While this is infeasible with resampling at test time, we can use our probes to cheaply signal that the model has finished thinking, and then predict the final answer choice.
203	
204	![Image 10: Refer to caption](https://arxiv.org/html/2603.05488v3/x10.png)
205	
206	Figure 8: Early Exit Accuracy & Tokens Saved for DeepSeek-R1 on MMLU & GPQA. We use binned confidence thresholds to decide when to early exit. The resulting accuracy is calculated using the probe’s prediction as well as the percent of tokens saved, if exiting at the first point where the probe reaches the confidence threshold.
207	
208	First, we show our probe are highly calibrated (Figure[7](https://arxiv.org/html/2603.05488#S7.F7 "Figure 7 ‣ 7 Attention Probes for Early Exit ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought")), with confidence closely tracking forced answer accuracy, and transfers as well to GPQA. This well-calibrated behavior makes the probe suitable for confidence-based early exit decisions, letting us use set some threshold at which an LLM can adaptively exit its reasoning trace.
209	
210	Figure[8](https://arxiv.org/html/2603.05488#S7.F8 "Figure 8 ‣ 7 Attention Probes for Early Exit ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought") demonstrates the practical application of using attention probes for early exit on MMLU. We plot probe accuracy at predicting the correct answer (rather than the model’s final answer) and where in the chain of thought the exit occurs at different confidence thresholds for the highest probability answer choice. Early exiting at 95% confidence retains 97% of original performance on MMLU while saving 68% of the tokens used. Meanwhile, exiting at 80% confidence for GPQA also retains 97% of performance while saving 50% of tokens. This method does not require a chain of thought monitor to find the model’s answer so far in the response, as we directly use the attention probe’s prediction. We find that the same trends hold for GPT-OSS, and include those results in Appendix[H](https://arxiv.org/html/2603.05488#A8 "Appendix H GPT-OSS Calibration for Early Exit ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought").
211	
212	## 8 Discussion
213	
214	##### Performative CoT
215	
216	Our results demonstrate a divergence between internal processes of a language model and its the expressed chain-of-thought. On MMLU, answer information becomes decodable from later-layer activations well before the model’s text reveals a commitment, and forced answering can often recover the final choice from early prefixes. This pattern is consistent with a conclusion being reached early, after which additional chain-of-thought tokens are generated without materially contributing to the decision. In contrast, on GPQA-D, both probes and forced answers improve more gradually over the trace and the CoT monitor’s ability to infer the final choice rises in tandem, indicating that intermediate textual computation is more aligned with the emergence of internal answer information. Taken together, these findings support a view in which “performative” CoT is not a uniform property of reasoning LLMs, but rather an interaction between the model and the relative difficulty of the task. On the other hand, we show that commonly studied reasoning steps like backtracking or sudden realizations typically (but not universally) reflect genuine updates to internal belief about the outcome.
217	
218	These differences have practical implications for monitoring and for how we should interpret chain-of-thought as evidence. If a model can internally encode its final answer well before it is reflected in the reasoning trace, then the trace may be an unreliable substrate for detecting early commitments, measuring uncertainty, or auditing why a decision was made. In such settings, a monitor that only reads the emitted text may lag behind or misrepresent the model’s internal state. This is further complicated by the difficulty in finding where inflection points occur relative to internal belief updates (§[6.2](https://arxiv.org/html/2603.05488#S6.SS2 "6.2 Inflection Points do not Reliably Occur with Shifts in Confidence ‣ 6 Inflection Points Suggest Faithful Reasoning ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought")). Conversely, in tasks where answer information truly emerges through incremental computation, the emitted reasoning can be more informative and may better track the model’s evolving beliefs.
219	
220	##### Tokens Savings through Early Exit
221	
222	A second implication is that internal signals can be leveraged for adaptive computation. The calibration results indicate that, at least on MMLU-Redux, attention probe confidence can be informative enough to drive early exit with minimal loss in accuracy, yielding large token savings. This is especially relevant for reasoning models that are incentivized to produce long traces even when unnecessary. From an efficiency perspective, this suggests a simple deployment strategy: learn a cheap predictor over existing activations and stop generation once confidence is high.
223	
224	##### Cooperative Communication and Monitoring
225	
226	The cases in which we find faithful or unfaithful (performative) reasoning are not random, and we propose viewing this from the lenses of cooperative communication (Grice, [1975](https://arxiv.org/html/2603.05488#bib.bib37 "Logic and conversation")) and reasoning models’ training objective: Standard reasoning models are optimized for outcome reward 3 3 3 We don’t want to oversimplify reasoning model training. DeepSeek-AI ([2025](https://arxiv.org/html/2603.05488#bib.bib7 "DeepSeek-r1: incentivizing reasoning capability in llms via reinforcement learning")) train R1 with a sophisticated compound reward, for example, and their communicative “intent” is at most instrumental towards this goal. Gricean cooperation is incidental: Relation (relevance) and Quality (supported evidence) are typically aligned with reward, while Quantity (verbosity) and Manner (obscurity) are not. This explains why traces are usually on-topic and not blatantly false, yet can be excessively long and fail to surface early internal commitment, which is precisely the failure mode that breaks CoT monitors as pragmatic listeners.
227	
228	This framing is useful to describe phenomena from prior work: 1) RL first increasing faithfulness without fully saturating (Chen et al., [2025](https://arxiv.org/html/2603.05488#bib.bib35 "Reasoning models don’t always say what they think")) and 2) propensity (or lack thereof) to verbalize hints in easy tasks (Chua and Evans, [2025](https://arxiv.org/html/2603.05488#bib.bib36 "Are deepseek r1 and other reasoning models more faithful?")), but offers less explanation for unfaithfulness described as post-hoc rationalization (Turpin et al., [2023](https://arxiv.org/html/2603.05488#bib.bib10 "Language models don’t always say what they think: unfaithful explanations in chain-of-thought prompting")). This suggests faithfulness is multifaceted and requires further study. Nevertheless, our probing strategy provides an effective way to both access information that isn’t easily attained through monitoring, and provides a method for early exiting reasoning traces to improve efficiency.
229	
230	## 9 Conclusion
231	
232	Frameworks and methods for investigating chain-of-thought are required to understand and control reasoning models. Towards this goal, we (1) compare black-box LM monitors and white-box attention probes abilities to predict a model’s eventual answer, (2) identify performative reasoning, where LMs continue producing tokens without disclosing their strong confidence in an answer decoded by probing, and (3) use attention probes for calibrated early exits to save tokens. We hope these contributions help build towards safer and more interpretable reasoning models.
233	
234	## Acknowledgements
235	
236	AM and SB began the project through the Supervised Program for Alignment Research (SPAR), mentored by JM and OL. We thank the SPAR team for their support. We would like to thank Yik Siu Chan, Usha Bhalla, Ren Makino, and Michael Byun for their helpful discussions.
237	
238	## References
239	
240	*   C. Agarwal, S. H. Tanneru, and H. Lakkaraju (2024)Faithfulness vs. plausibility: on the (un) reliability of explanations from large language models. arXiv preprint arXiv:2402.04614. Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p1.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
241	*   S. Agarwal, L. Ahmad, J. Ai, S. Altman, A. Applebaum, E. Arbus, R. K. Arora, Y. Bai, B. Baker, H. Bao, et al. (2025)Gpt-oss-120b & gpt-oss-20b model card. arXiv preprint arXiv:2508.10925. Cited by: [§A.1](https://arxiv.org/html/2603.05488#A1.SS1.p1.1 "A.1 Model Inference Details ‣ Appendix A Inference and Prompting Details ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"), [§3.1](https://arxiv.org/html/2603.05488#S3.SS1.p1.1 "3.1 Models & Datasets ‣ 3 Methods ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
242	*   G. Ahdritz, T. Qin, N. Vyas, B. Barak, and B. L. Edelman (2024)Distinguishing the knowable from the unknowable with language models. In Proceedings of the 41st International Conference on Machine Learning, R. Salakhutdinov, Z. Kolter, K. Heller, A. Weller, N. Oliver, J. Scarlett, and F. Berkenkamp (Eds.), Proceedings of Machine Learning Research, Vol. 235,  pp.503–549. External Links: [Link](https://proceedings.mlr.press/v235/ahdritz24a.html)Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p3.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
243	*   G. Alain and Y. Bengio (2016)Understanding intermediate layers using linear classifier probes. arXiv preprint arXiv:1610.01644. Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p3.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
244	*   E. Ameisen, J. Lindsey, A. Pearce, W. Gurnee, N. L. Turner, B. Chen, C. Citro, D. Abrahams, S. Carter, B. Hosmer, J. Marcus, M. Sklar, A. Templeton, T. Bricken, C. McDougall, H. Cunningham, T. Henighan, A. Jermyn, A. Jones, A. Persic, Z. Qi, T. Ben Thompson, S. Zimmerman, K. Rivoire, T. Conerly, C. Olah, and J. Batson (2025)Circuit tracing: revealing computational graphs in language models. Transformer Circuits Thread. External Links: [Link](https://transformer-circuits.pub/2025/attribution-graphs/methods.html)Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p2.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
245	*   I. Arcuschin, J. Janiak, R. Krzyzanowski, S. Rajamanoharan, N. Nanda, and A. Conmy (2025)Chain-of-thought reasoning in the wild is not always faithful. In ICLR 2025 Workshop on Reasoning and Planning for LLMs, External Links: [Link](https://openreview.net/forum?id=L8094Whth0), 2503.08679 Cited by: [§1](https://arxiv.org/html/2603.05488#S1.p1.1 "1 Introduction ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"), [§2](https://arxiv.org/html/2603.05488#S2.p1.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
246	*   B. Arnav, P. Bernabeu-Perez, N. Helm-Burger, T. Kostolansky, H. Whittingham, and M. Phuong (2025)CoT red-handed: stress testing chain-of-thought monitoring. In NeurIPS 2025, Note: Poster External Links: [Link](https://openreview.net/forum?id=oHB4Ee77uG), 2505.23575 Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p1.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"), [§2](https://arxiv.org/html/2603.05488#S2.p2.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
247	*   B. Baker, J. Huizinga, L. Gao, Z. Dou, M. Y. Guan, A. Madry, W. Zaremba, J. Pachocki, and D. Farhi (2025)Monitoring reasoning models for misbehavior and the risks of promoting obfuscation. Note: OpenAI technical report; OpenAI-hosted PDF available at https://cdn.openai.com/pdf/34f2ada6-870f-4c26-9790-fd8def56387f/CoT_Monitoring.pdf External Links: 2503.11926, [Document](https://dx.doi.org/10.48550/arXiv.2503.11926), [Link](https://arxiv.org/abs/2503.11926)Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p1.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
248	*   Y. Belinkov (2022)Probing classifiers: promises, shortcomings, and advances. Computational Linguistics 48 (1),  pp.207–219. Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p3.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
249	*   E. J. Bigelow, A. Holtzman, H. Tanaka, and T. Ullman (2025)Forking paths in neural text generation. In International Conference on Learning Representations (ICLR), External Links: [Link](https://openreview.net/forum?id=8RCmNLeeXx), 2412.07961 Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p2.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
250	*   P. C. Bogdan, U. Macar, N. Nanda, and A. Conmy (2025)Thought anchors: which LLM reasoning steps matter?. External Links: 2506.19143, [Document](https://dx.doi.org/10.48550/arXiv.2506.19143), [Link](https://arxiv.org/abs/2506.19143)Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p2.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"), [§2](https://arxiv.org/html/2603.05488#S2.p4.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
251	*   Y. S. Chan, Z. Yong, and S. H. Bach (2025)Can we predict alignment before models finish thinking? towards monitoring misaligned reasoning models. External Links: 2507.12428, [Document](https://dx.doi.org/10.48550/arXiv.2507.12428), [Link](https://arxiv.org/abs/2507.12428)Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p1.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
252	*   Y. Chen, J. Benton, A. Radhakrishnan, J. Uesato, C. Denison, J. Schulman, A. Somani, P. Hase, M. Wagner, F. Roger, V. Mikulik, S. R. Bowman, J. Leike, J. Kaplan, and E. Perez (2025)Reasoning models don’t always say what they think. External Links: 2505.05410, [Link](https://arxiv.org/abs/2505.05410)Cited by: [§1](https://arxiv.org/html/2603.05488#S1.p1.1 "1 Introduction ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"), [§8](https://arxiv.org/html/2603.05488#S8.SS0.SSS0.Px3.p2.1 "Cooperative Communication and Monitoring ‣ 8 Discussion ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
253	*   J. Chua and O. Evans (2025)Are deepseek r1 and other reasoning models more faithful?. External Links: 2501.08156, [Link](https://arxiv.org/abs/2501.08156)Cited by: [§8](https://arxiv.org/html/2603.05488#S8.SS0.SSS0.Px3.p2.1 "Cooperative Communication and Monitoring ‣ 8 Discussion ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
254	*   G. Comanici, E. Bieber, M. Schaekermann, I. Pasupat, N. Sachdeva, I. Dhillon, M. Blistein, O. Ram, D. Zhang, E. Rosen, et al. (2025)Gemini 2.5: pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities. arXiv preprint arXiv:2507.06261. Cited by: [§3.4](https://arxiv.org/html/2603.05488#S3.SS4.SSS0.Px2.p2.1 "Identifying inflection points: ‣ 3.4 Chain of Thought Monitoring ‣ 3 Methods ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
255	*   DeepSeek-AI (2025)DeepSeek-r1: incentivizing reasoning capability in llms via reinforcement learning. External Links: 2501.12948, [Link](https://arxiv.org/abs/2501.12948)Cited by: [§A.1](https://arxiv.org/html/2603.05488#A1.SS1.p1.1 "A.1 Model Inference Details ‣ Appendix A Inference and Prompting Details ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"), [§1](https://arxiv.org/html/2603.05488#S1.p1.1 "1 Introduction ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"), [§3.1](https://arxiv.org/html/2603.05488#S3.SS1.p1.1 "3.1 Models & Datasets ‣ 3 Methods ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"), [§6](https://arxiv.org/html/2603.05488#S6.p1.1 "6 Inflection Points Suggest Faithful Reasoning ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"), [footnote 3](https://arxiv.org/html/2603.05488#footnote3 "In Cooperative Communication and Monitoring ‣ 8 Discussion ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
256	*   J. Dunefsky, P. Chlenski, and N. Nanda (2024)Transcoders find interpretable LLM feature circuits. In Advances in Neural Information Processing Systems, Vol. 37. External Links: 2406.11944, [Link](https://arxiv.org/abs/2406.11944)Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p2.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
257	*   S. Emmons, E. Jenner, D. K. Elson, R. A. Saurous, S. Rajamanoharan, H. Chen, I. Shafkat, and R. Shah (2025)When chain of thought is necessary, language models struggle to evade monitors. arXiv preprint arXiv:2507.05246. Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p1.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"), [§2](https://arxiv.org/html/2603.05488#S2.p2.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
258	*   M. C. Frank and N. D. Goodman (2012)Predicting pragmatic reasoning in language games. Science 336 (6084),  pp.998–998. Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p5.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
259	*   A. P. Gema, J. O. J. Leang, G. Hong, A. Devoto, A. C. M. Mancino, R. Saxena, X. He, Y. Zhao, X. Du, M. R. Ghasemi Madani, C. Barale, R. McHardy, J. Harris, J. Kaddour, E. Van Krieken, and P. Minervini (2025)Are we done with MMLU?. In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), Albuquerque, New Mexico,  pp.5069–5096. External Links: [Document](https://dx.doi.org/10.18653/v1/2025.naacl-long.262), [Link](https://aclanthology.org/2025.naacl-long.262/)Cited by: [§3.1](https://arxiv.org/html/2603.05488#S3.SS1.p2.1 "3.1 Models & Datasets ‣ 3 Methods ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
260	*   N. D. Goodman and M. C. Frank (2016)Pragmatic language interpretation as probabilistic inference. Trends in cognitive sciences 20 (11),  pp.818–829. Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p5.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
261	*   N. D. Goodman and A. Stuhlmüller (2013)Knowledge and implicature: modeling language understanding as social cognition. Topics in cognitive science 5 (1),  pp.173–184. Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p5.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
262	*   H. P. Grice (1975)Logic and conversation. In Speech acts,  pp.41–58. Cited by: [§1](https://arxiv.org/html/2603.05488#S1.p3.1 "1 Introduction ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"), [§2](https://arxiv.org/html/2603.05488#S2.p5.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"), [§8](https://arxiv.org/html/2603.05488#S8.SS0.SSS0.Px3.p1.1 "Cooperative Communication and Monitoring ‣ 8 Discussion ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
263	*   S. Kadavath, T. Conerly, A. Askell, T. Henighan, D. Drain, E. Perez, N. Schiefer, Z. Hatfield-Dodds, N. DasSarma, E. Tran-Johnson, S. Johnston, S. El-Showk, A. Jones, N. Elhage, T. Hume, A. Chen, Y. Bai, S. Bowman, S. Fort, D. Ganguli, D. Hernandez, J. Jacobson, J. Kernion, S. Kravec, L. Lovitt, K. Ndousse, C. Olsson, S. Ringer, D. Amodei, T. Brown, J. Clark, N. Joseph, B. Mann, S. McCandlish, C. Olah, and J. Kaplan (2022)Language models (mostly) know what they know. External Links: 2207.05221, [Link](https://arxiv.org/abs/2207.05221)Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p1.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
264	*   S. Kantamneni, J. Engels, S. Rajamanoharan, M. Tegmark, and N. Nanda (2025)Are sparse autoencoders useful? A case study in sparse probing. In Proceedings of the 42nd International Conference on Machine Learning, Proceedings of Machine Learning Research, Vol. 267,  pp.29018–29049. External Links: [Link](https://proceedings.mlr.press/v267/kantamneni25a.html), 2502.16681 Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p3.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"), [§3.2](https://arxiv.org/html/2603.05488#S3.SS2.p2.9 "3.2 Attention Probes ‣ 3 Methods ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
265	*   T. Korbak, M. Balesni, E. Barnes, Y. Bengio, et al. (2025)Chain of thought monitorability: a new and fragile opportunity for ai safety. External Links: 2507.11473, [Link](https://arxiv.org/abs/2507.11473)Cited by: [§1](https://arxiv.org/html/2603.05488#S1.p1.1 "1 Introduction ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"), [§2](https://arxiv.org/html/2603.05488#S2.p1.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"), [§3.4](https://arxiv.org/html/2603.05488#S3.SS4.p1.1 "3.4 Chain of Thought Monitoring ‣ 3 Methods ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
266	*   T. Lanham, A. Chen, A. Radhakrishnan, B. Steiner, et al. (2023)Measuring faithfulness in chain-of-thought reasoning. External Links: 2307.13702, [Link](https://arxiv.org/abs/2307.13702)Cited by: [§1](https://arxiv.org/html/2603.05488#S1.p1.1 "1 Introduction ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"), [§2](https://arxiv.org/html/2603.05488#S2.p1.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"), [§3.3](https://arxiv.org/html/2603.05488#S3.SS3.p1.1 "3.3 Forced Answering ‣ 3 Methods ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
267	*   S. C. Levinson (1983)Pragmatics. Cambridge university press. Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p5.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
268	*   U. Macar, P. C. Bogdan, S. Rajamanoharan, and N. Nanda (2025)Thought branches: interpreting llm reasoning requires resampling. arXiv preprint arXiv:2510.27484. Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p2.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
269	*   H. Mayne, J. S. Kang, D. Gould, K. Ramchandran, A. Mahdi, and N. Y. Siegel (2026)A positive case for faithfulness: llm self-explanations help predict model behavior. External Links: 2602.02639, [Link](https://arxiv.org/abs/2602.02639)Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p1.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
270	*   A. McKenzie, U. Pawar, P. Blandfort, W. Bankes, D. Krueger, E. S. Lubana, and D. Krasheninnikov (2025)Detecting high-stakes interactions with activation probes. External Links: 2506.10805, [Link](https://arxiv.org/abs/2506.10805)Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p3.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
271	*   OpenAI (2024)Learning to reason with llms. External Links: [Link](https://openai.com/index/learning-to-reason-with-llms/)Cited by: [§1](https://arxiv.org/html/2603.05488#S1.p1.1 "1 Introduction ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
272	*   V. Palod, K. Valmeekam, K. Stechly, and S. Kambhampati (2025)Performative thinking? the brittle correlation between cot length and problem complexity. In NeurIPS 2025 Workshop on Efficient Reasoning, Cited by: [item 2](https://arxiv.org/html/2603.05488#S1.I1.i2.p1.1 "In 1 Introduction ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"), [§1](https://arxiv.org/html/2603.05488#S1.p1.1 "1 Introduction ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"), [§2](https://arxiv.org/html/2603.05488#S2.p1.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
273	*   D. Rein, B. L. Hou, A. C. Stickland, J. Petty, R. Y. Pang, J. Dirani, J. Michael, and S. R. Bowman (2023)GPQA: a graduate-level google-proof q&a benchmark. External Links: 2311.12022, [Document](https://dx.doi.org/10.48550/arXiv.2311.12022), [Link](https://arxiv.org/abs/2311.12022)Cited by: [§3.1](https://arxiv.org/html/2603.05488#S3.SS1.p2.1 "3.1 Models & Datasets ‣ 3 Methods ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
274	*   L. Reynolds and K. McDonell (2021)Prompt programming for large language models: beyond the few-shot paradigm. In Extended Abstracts of the 2021 CHI Conference on Human Factors in Computing Systems, External Links: [Document](https://dx.doi.org/10.1145/3411763.3451760), 2102.07350, [Link](https://arxiv.org/abs/2102.07350)Cited by: [§1](https://arxiv.org/html/2603.05488#S1.p1.1 "1 Introduction ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
275	*   M. Turpin, J. Michael, E. Perez, and S. R. Bowman (2023)Language models don’t always say what they think: unfaithful explanations in chain-of-thought prompting. In Advances in Neural Information Processing Systems, Vol. 36. External Links: [Link](https://arxiv.org/abs/2305.04388), 2305.04388 Cited by: [§1](https://arxiv.org/html/2603.05488#S1.p1.1 "1 Introduction ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"), [§2](https://arxiv.org/html/2603.05488#S2.p1.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"), [§8](https://arxiv.org/html/2603.05488#S8.SS0.SSS0.Px3.p2.1 "Cooperative Communication and Monitoring ‣ 8 Discussion ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
276	*   C. Venhoff, I. Arcuschin, P. Torr, A. Conmy, and N. Nanda (2025a)Base models know how to reason, thinking models learn when. External Links: 2510.07364, [Document](https://dx.doi.org/10.48550/arXiv.2510.07364), [Link](https://arxiv.org/abs/2510.07364)Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p4.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
277	*   C. Venhoff, I. Arcuschin, P. Torr, A. Conmy, and N. Nanda (2025b)Understanding reasoning in thinking language models via steering vectors. arXiv preprint arXiv:2506.18167. Cited by: [§6](https://arxiv.org/html/2603.05488#S6.p1.1 "6 Inflection Points Suggest Faithful Reasoning ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
278	*   K. Wang, A. Variengien, A. Conmy, B. Shlegeris, and J. Steinhardt (2022)Interpretability in the wild: a circuit for indirect object identification in GPT-2 small. External Links: 2211.00593, [Link](https://arxiv.org/abs/2211.00593)Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p2.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
279	*   X. Wang, N. Joshi, B. Plank, R. Angell, and H. He (2025)Is it thinking or cheating? detecting implicit reward hacking by measuring reasoning effort. arXiv preprint arXiv:2510.01367. Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p1.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
280	*   X. Wang, N. Joshi, B. Plank, R. Angell, and H. He (2026)Is it thinking or cheating? detecting implicit reward hacking by measuring reasoning effort. External Links: 2510.01367, [Link](https://arxiv.org/abs/2510.01367)Cited by: [§3.3](https://arxiv.org/html/2603.05488#S3.SS3.p1.1 "3.3 Forced Answering ‣ 3 Methods ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
281	*   J. Ward, C. Lin, C. Venhoff, and N. Nanda (2025)Reasoning-finetuning repurposes latent representations in base models. arXiv preprint arXiv:2507.12638. Cited by: [§6](https://arxiv.org/html/2603.05488#S6.p1.1 "6 Inflection Points Suggest Faithful Reasoning ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
282	*   J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. Chi, Q. Le, and D. Zhou (2022)Chain-of-thought prompting elicits reasoning in large language models. In Advances in Neural Information Processing Systems, Vol. 35. External Links: 2201.11903, [Link](https://arxiv.org/abs/2201.11903)Cited by: [§1](https://arxiv.org/html/2603.05488#S1.p1.1 "1 Introduction ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
283	*   A. Zhang, Y. Chen, J. Pan, C. Zhao, A. Panda, J. Li, and H. He (2025)Reasoning models know when they’re right: probing hidden states for self-verification. External Links: 2504.05419, [Document](https://dx.doi.org/10.48550/arXiv.2504.05419), [Link](https://arxiv.org/abs/2504.05419)Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p3.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
284	*   A. Zur, A. Geiger, E. S. Lubana, and E. Bigelow (2025)Are language models aware of the road not taken? token-level uncertainty and hidden state dynamics. External Links: 2511.04527, [Document](https://dx.doi.org/10.48550/arXiv.2511.04527), [Link](https://arxiv.org/abs/2511.04527)Cited by: [§2](https://arxiv.org/html/2603.05488#S2.p3.1 "2 Related Work ‣ Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"). 
285	
286	## Appendix A Inference and Prompting Details
287	
288	### A.1 Model Inference Details
289	
290	We collect model responses on both MMLU-Redux 2.0 and GPQA-Diamond using the same inference settings reported by the original authors(DeepSeek-AI, [2025](https://arxiv.org/html/2603.05488#bib.bib7 "DeepSeek-r1: incentivizing reasoning capability in llms via reinforcement learning"); Agarwal et al., [2025](https://arxiv.org/html/2603.05488#bib.bib28 "Gpt-oss-120b & gpt-oss-20b model card")).
291	
292	For DeepSeek-R1 671B, we run inference through the OpenRouter API using model deepseek-r1-0528 using the SiliconFlow provider. For both datasets, we use a temperature of 0.6, a top_p of 0.95, and a max_tokens of 30,000. The prompt used is as follows:
293	
294	System prompt:
295	
296	The assistant is DeepSeek-R1,created by DeepSeek.
297	
298	User message:
299	
300	##Question:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3610fb9-96ba-46f4-b4a1-976a6de53578",
  "isSidechain": true,
  "promptId": "8029e2e4-25c6-47cb-9539-6d3b0938c122",
  "agentId": "a7ed4918e81d4960b",
  "type": "user",
  "uuid": "880302ec-054b-439b-a954-ab9fc18deab3",
  "sourceToolAssistantUUID": "d3610fb9-96ba-46f4-b4a1-976a6de53578",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-19T09:12:52.292Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01R22f7tHBqW58H8LF4G2Pkd`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.11201",
  "prompt": "Extract ALL technical details from this paper about mechanistic evidence for faithfulness decay. I need: 1) The three model families tested, 2) Exact NLDD metric definition and how corruption works, 3) The reasoning horizon phenomenon with quantitative details, 4) What tasks were used, 5) What \"encoding correct representations while failing\" means, 6) All quantitative results, 7) Implications for faithfulness and adversarial robustness. Be maximally detailed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "880302ec-054b-439b-a954-ab9fc18deab3",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfq9eSjUv8cwgwKkNWY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87d60fe5-d883-4b07-aecd-653f08a1e2f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5AscghX2VQrCt8AYFNvGc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1704,
      "cache_read_input_tokens": 14212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1704,
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

_source line 41 · 2026-05-19T09:13:19.495Z_

<details><summary>↩ Tool result · `toolu_01R22f7tHBqW58H8LF4G2Pkd`</summary>

````text
# Technical Details: Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning

## 1. Three Model Families Tested

The research evaluated three instruction-tuned decoder-only transformers:

- **DeepSeek-Coder-6.7B-Instruct**: Optimized for source code generation, testing whether specialization in rigid logical structures enhances reasoning faithfulness
- **Llama-3.1-8B-Instruct**: General-purpose baseline representing standard dense transformer architectures
- **Gemma-2-9B-Instruct**: Uses logit soft-capping to compress output distributions, validating metric generalization across architectural variance

## 2. NLDD Metric Definition and Corruption Mechanism

**Metric Formula:**
The NLDD (Normalized Logit Difference Decay) quantifies proportional confidence loss when reasoning steps are corrupted:

```
NLDD = (LD_clean - LD_corrupt) / |LD_clean| × 100
```

**Global Calibration Constant:**
```
S = (1/M) Σ σ(z_m)
```
where σ computes standard deviation across vocabulary logits on clean traces, enabling cross-architecture comparison.

**Logit Difference (LD):**
```
LD = [max_y∈Y_correct ℓ(y) - max_y'∉Y_correct ℓ(y')] / S
```

**Corruption Process:**
- Researchers corrupt individual reasoning steps at specific positions
- Task-specific corruption strategies: depth errors (Dyck-nn), entity substitutions (PrOntoQA), arithmetic errors (GSM8K)
- All subsequent steps are truncated
- Counterfactuals filtered for coherence: token count delta ≤2 and perplexity ratio ≤1.5-3.5
- Samples with |LD_clean| <10⁻⁶ excluded to prevent noise amplification

**Interpretation:**
- Positive NLDD: causal reliance on reasoning
- Near-zero NLDD: weak coupling between reasoning and prediction
- Negative NLDD: confidence paradoxically increases when reasoning corrupted (anti-faithful regime)

## 3. Reasoning Horizon (k*) Phenomenon

**Definition:**
The reasoning horizon represents the chain position with maximum mean NLDD, excluding the premise:

```
k* = argmax_k>1 NLDD̄(k)
```

**Quantitative Findings:**

| Task | Steps | Llama k* | DeepSeek k* | Gemma k* | Relative Position |
|------|-------|----------|-------------|----------|-------------------|
| GSM8K | 8 | 6 | 5 | 6 | ~85% through chain |
| Dyck-nn | 12 | 11 | 11 | 9 | ~80% through chain |
| PrOntoQA | 16 | 16 | 16 | 11 | 70-100% through chain |

**Key Pattern:** The horizon concentrates causal influence in early-to-middle reasoning, with later portions contributing diminishing or negative returns regardless of absolute chain length. Beyond k*, NLDD drops sharply while geometric properties remain stable, suggesting reasoning affects surface behavior without altering underlying computational trajectories.

## 4. Tasks and Evaluation Design

Three benchmarks spanning increasing semantic ambiguity:

**Dyck-nn** (Syntactic State Tracking)
- 100 samples per model
- Classification task requiring bracket-matching logic
- Probe target: stack depth at each step (0-10)

**PrOntoQA** (Logical Inference)
- 100 samples per model
- Multi-hop logical entailment
- Probe target: final truth value throughout reasoning (True/False)

**GSM8K** (Multi-step Arithmetic)
- 100 samples per model
- Math word problems requiring sequential calculation
- Probe target: arithmetic operation type (addition/subtraction/multiplication)

**Dataset Construction:**
- Clean CoT traces paired with counterfactual variants
- Filtering: only samples with correct final answers included
- Disjoint subsets for evaluation and diagnostic probing prevent representational leakage

## 5. "Encoding Correct Representations While Failing" (The Mapping Gap)

The researchers identified a critical dissociation between internal representation and external performance:

**Gemma's Dyck-nn Performance:**
- Linear probes achieved 82.0% accuracy recovering stack-depth information from hidden states
- Model achieved only 0.0% accuracy on the actual task
- Interpretation: task-relevant structure encoded internally but not utilized in final decoding

**Representational Similarity Analysis (RSA) Dynamics:**
- Dyck-nn maintained moderate representational stability (RSA=0.422)
- PrOntoQA showed low stability (RSA=0.254) despite 99.0% accuracy
- High representational fidelity does not ensure causal utilization

**Trajectory Alignment Score (TAS) Variance:**
- Llama exhibited systematic geometric convergence with steady TAS decay across tasks
- Gemma and DeepSeek showed marginal TAS variance between first and last steps
- Gemma's trajectory rigidity aligns with anti-faithfulness where generated reasoning lacks computational effect

This demonstrates that models can maintain geometrically consistent internal states encoding correct task logic while completely failing task execution or ignoring the reasoning chain for prediction.

## 6. Quantitative Results Summary

**Table 1: Accuracy and NLDD by Model and Task**

| Model | Task | Accuracy (%) | NLDD (%) |
|-------|------|--------------|----------|
| Llama-3.1-8B | Dyck-nn | 64.4 | 3.0 |
| | PrOntoQA | 100.0 | 20.6 |
| | GSM8K | 100.0 | 96.7 |
| DeepSeek-6.7B | Dyck-nn | 47.2 | 9.5 |
| | PrOntoQA | 100.0 | 84.3 |
| | GSM8K | 100.0 | 96.1 |
| Gemma-2-9B | Dyck-nn | 0.0 | 12.5 |
| | PrOntoQA | 99.0 | **-52.5** |
| | GSM8K | 100.0 | 61.5 |

**Behavioral Regimes:**
- **Faithful Regime**: Llama and DeepSeek exhibit high positive NLDD, indicating causal grounding in reasoning
- **Anti-Faithful Regime**: Gemma achieves 99% PrOntoQA accuracy with negative NLDD (-52.5%), revealing complete causal disconnection from CoT despite correct answers

**Representational Metrics (Extended Results in Table 6):**

| Model | Task | RSA | Probe Accuracy |
|-------|------|-----|----------------|
| DeepSeek | Dyck-nn | 0.481 | 81.1% |
| | PrOntoQA | 0.176 | 91.7% |
| | GSM8K | 0.560 | 81.8% |
| Llama | Dyck-nn | 0.436 | 74.9% |
| | PrOntoQA | 0.228 | 91.8% |
| | GSM8K | 0.548 | 71.2% |
| Gemma | Dyck-nn | 0.422 | 82.0% |
| | PrOntoQA | 0.254 | 91.7% |
| | GSM8K | 0.568 | 74.2% |

**NLDD Confidence Intervals (95% BCa Bootstrap, B=10,000):**
- DeepSeek PrOntoQA: [82.00, 85.73]
- Llama PrOntoQA: [18.46, 23.05]
- Gemma PrOntoQA: [-57.98, -46.54] (significantly negative)

## 7. Implications for Faithfulness and Adversarial Robustness

**Faithfulness Implications:**

1. **Accuracy Masks Causal Disconnection**: The research demonstrates that "near-perfect task performance can coexist with lack of functional dependence on CoT," as shown by Gemma's 99% accuracy despite -52.5% NLDD on PrOntoQA.

2. **Two Failure Modes Revealed**: NLDD distinguishes between task failure (low accuracy) and causal disconnection (low NLDD), enabling targeted model improvement. Models can fail because they cannot perform the task or because their reasoning doesn't causally influence outputs.

3. **Reasoning as Post-Hoc Rationalization**: Models exhibit "Clever Hans" behavior where "the probability of the correct token increases when the reasoning chain is corrupted," suggesting generated explanations serve as plausible rationalizations rather than causal drivers of decision-making.

**Adversarial Robustness Implications:**

1. **Vulnerability Beyond Horizon**: Beyond k* (70-85% chain length), additional reasoning tokens contribute "negligible or negative causal influence," suggesting that extended CoT may introduce adversarial surfaces without strengthening actual reasoning.

2. **Anti-Faithful Models Paradoxically Harmed by Extended Reasoning**: In Gemma's PrOntoQA, NLDD deteriorates from -22.9 to -120.2 beyond k*, indicating "extended reasoning interferes with pre-computed answers," making models more vulnerable to reasoning-based adversarial attacks.

3. **Representational Stability Decoupled from Robustness**: RSA remains stable beyond k* (p>0.05) despite causal collapse, demonstrating that "models maintain geometric consistency without utilizing those representations," creating vulnerability: internal states appear robust while output causal dependence deteriorates.

4. **Practical Pruning Strategy**: The consistent k* positioning (70-85% chain length) across tasks enables empirically-justified chain truncation without accuracy loss, reducing attack surface from extraneous reasoning steps that don't causally contribute to predictions.

5. **Architecture-Dependent Vulnerability**: Different models exhibit divergent faithfulness regimes on identical tasks, suggesting that adversarial robustness strategies must be architecture-specific rather than task-specific, as some models rely on reasoning while others circumvent it entirely.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87d60fe5-d883-4b07-aecd-653f08a1e2f0",
  "isSidechain": true,
  "promptId": "8029e2e4-25c6-47cb-9539-6d3b0938c122",
  "agentId": "a7ed4918e81d4960b",
  "type": "user",
  "uuid": "60e571b3-b2ea-426d-b619-2112b301bb32",
  "sourceToolAssistantUUID": "87d60fe5-d883-4b07-aecd-653f08a1e2f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-19T09:13:26.992Z_

Excellent -- I got comprehensive data for papers 2 and 3. Now let me read the rest of the REMUL paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60e571b3-b2ea-426d-b619-2112b301bb32",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfso6GAv9z5C3vwsspH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75417aa2-a01c-4715-a807-7d02d1e543fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESe6Yfu88AxYYdDtW8Wc9w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27113,
      "cache_read_input_tokens": 15916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27113,
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

_source line 43 · 2026-05-19T09:13:30.372Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UWcChe6qMZPtPqeiFr7tsw`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-gen-pipeline/d3232602-cd70-49bb-a57b-21b3ab7347ad/tool-results/toolu_01WsipDpz1NE32BCo2LPsyNa.txt",
  "limit": 500,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75417aa2-a01c-4715-a807-7d02d1e543fc",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfso6GAv9z5C3vwsspH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "145b7067-6d24-44d4-b2b3-b5d9ee8318e6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESe6Yfu88AxYYdDtW8Wc9w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27113,
      "cache_read_input_tokens": 15916,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 27113
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 191,
          "cache_read_input_tokens": 15916,
          "cache_creation_input_tokens": 27113,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 27113,
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

_source line 44 · 2026-05-19T09:13:30.647Z_

<details><summary>↩ Tool result · reported error · `toolu_01UWcChe6qMZPtPqeiFr7tsw`</summary>

```text
File content (29169 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "145b7067-6d24-44d4-b2b3-b5d9ee8318e6",
  "isSidechain": true,
  "promptId": "8029e2e4-25c6-47cb-9539-6d3b0938c122",
  "agentId": "a7ed4918e81d4960b",
  "type": "user",
  "uuid": "3f0aa370-bbd0-494a-a08d-73175d3c7ba4",
  "toolUseResult": "Error: File content (29169 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "145b7067-6d24-44d4-b2b3-b5d9ee8318e6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T09:13:34.041Z_

<details open><summary>🔧 Tool call — Read · `toolu_015HB3kcqn3kQx2Tfaxa6qqq`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-gen-pipeline/d3232602-cd70-49bb-a57b-21b3ab7347ad/tool-results/toolu_01WsipDpz1NE32BCo2LPsyNa.txt",
  "limit": 400,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f0aa370-bbd0-494a-a08d-73175d3c7ba4",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBftckC45ea5W5yT8rib",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "788f8fcd-45ff-43f8-aac5-016cc7925324",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017kW69TPy8XiopfUDgXWu1G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 252,
      "cache_read_input_tokens": 43029,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 252
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 43029,
          "cache_creation_input_tokens": 252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 252,
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

_source line 46 · 2026-05-19T09:13:34.316Z_

<details><summary>↩ Tool result · reported error · `toolu_015HB3kcqn3kQx2Tfaxa6qqq`</summary>

```text
File content (29169 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "788f8fcd-45ff-43f8-aac5-016cc7925324",
  "isSidechain": true,
  "promptId": "8029e2e4-25c6-47cb-9539-6d3b0938c122",
  "agentId": "a7ed4918e81d4960b",
  "type": "user",
  "uuid": "8c9014d6-9185-49fb-9293-0421915f4c15",
  "toolUseResult": "Error: File content (29169 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "788f8fcd-45ff-43f8-aac5-016cc7925324",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-19T09:13:37.757Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ELoSd4YfuuPWqyaMV7VTj4`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-gen-pipeline/d3232602-cd70-49bb-a57b-21b3ab7347ad/tool-results/toolu_01WsipDpz1NE32BCo2LPsyNa.txt",
  "limit": 200,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c9014d6-9185-49fb-9293-0421915f4c15",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfttTkUzWedKGwcTh6o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0267a10f-9c10-4e66-a97d-93e09c4e5833",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S5MMJhXHWuupnk6HEWW9Vo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 222,
      "cache_read_input_tokens": 43281,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 222
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 43281,
          "cache_creation_input_tokens": 222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 222,
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

_source line 48 · 2026-05-19T09:13:38.283Z_

<details><summary>↩ Tool result · `toolu_01ELoSd4YfuuPWqyaMV7VTj4`</summary>

```text
0	Title: Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution
1	
2	URL Source: https://arxiv.org/html/2602.16154
3	
4	Markdown Content:
5	Shoubin Yu Hyunji Lee Yue Zhang Ali Payani Mohit Bansal Elias Stengel-Eskin
6	
7	###### Abstract
8	
9	Chain-of-thought (CoT) reasoning sometimes fails to faithfully reflect the true computation of a large language model (LLM), hampering its utility in explaining how LLMs arrive at their answers. Moreover, optimizing for faithfulness and interpretability in reasoning often degrades task performance. To address this tradeoff and improve CoT faithfulness, we propose Reasoning Execution by Multiple Listeners (REMuL), a multi-party reinforcement learning approach. REMuL builds on the hypothesis that reasoning traces which other parties can follow will be more faithful. A speaker model generates a reasoning trace, which is truncated and passed to a pool of listener models who “execute” the trace, continuing the trace to an answer. Speakers are rewarded for producing reasoning that is clear to listeners, with additional correctness regularization via masked supervised finetuning to counter the tradeoff between faithfulness and performance. On multiple reasoning benchmarks (BIG-Bench Extra Hard, MuSR, ZebraLogicBench, and FOLIO), REMuL consistently and substantially improves three measures of faithfulness – hint attribution, early answering area over the curve (AOC), and mistake injection AOC – while also improving accuracy. Our analysis finds that these gains are robust across training domains, translate to legibility gains, and are associated with shorter and more direct CoTs.1 1 1 Code: [https://github.com/nsivaku/remul](https://github.com/nsivaku/remul)
10	
11	Machine Learning, ICML
12	
13	![Image 1: Refer to caption](https://arxiv.org/html/2602.16154v1/x1.png)
14	
15	Figure 1:  Existing reasoning models are prone to producing reasoning that is unfaithful and hard to follow. Thus, when given a reasoning chain prefix (blue) from a base speaker model (A), listener models are often unable to reproduce the speaker’s final decision, i.e., their soft execution suffix (white) diverges. REMuL rewards speakers for inducing consistent reasoning in the listener pool. With REMuL, the speaker’s reasoning is more faithful and easier for the listeners to follow consistently, with all listeners reaching the same conclusion as the speaker. Note that reasoning here is elided, and the shown prefix and truncated suffix are not by necessity the same length. 
16	
17	1 Introduction
18	--------------
19	
20	While current reasoning large language models (LLMs) produce chain-of-thought (CoT) outputs that ostensibly reflect their reasoning, it remains unclear to what extent these outputs faithfully represent the model’s true computational process (Lanham et al., [2023](https://arxiv.org/html/2602.16154v1#bib.bib5 "Measuring faithfulness in chain-of-thought reasoning"); Barez et al., [2025](https://arxiv.org/html/2602.16154v1#bib.bib47 "Chain-of-thought is not explainability"); Chen et al., [2025](https://arxiv.org/html/2602.16154v1#bib.bib4 "Reasoning models don’t always say what they think")). This gap limits the reliability of LLMs and makes verifying their answers challenging, especially in domains (e.g., medicine, law, scientific research) where users require not just an answer but a faithful explanation of how that answer was reached (Sitaraman, [2025](https://arxiv.org/html/2602.16154v1#bib.bib7 "AI-driven healthcare systems enhanced by advanced data analytics and mobile computing"); Mashraqi and Allehyani, [2022](https://arxiv.org/html/2602.16154v1#bib.bib8 "Current trends on the application of artificial intelligence in medical sciences"); Rajpurkar et al., [2022](https://arxiv.org/html/2602.16154v1#bib.bib9 "AI in health and medicine"); Resnik and Hosseini, [2025](https://arxiv.org/html/2602.16154v1#bib.bib10 "The ethics of using artificial intelligence in scientific research: new guidance needed for a new tool"); Schwarcz et al., [2025](https://arxiv.org/html/2602.16154v1#bib.bib11 "Ai-powered lawyering: ai reasoning models, retrieval augmented generation, and the future of legal practice")). Moreover, a line of prior work points to a tension between task performance and reasoning faithfulness, with improvements to accuracy often coming at a cost to reasoning faithfulness or interpretability (Arrieta et al., [2020](https://arxiv.org/html/2602.16154v1#bib.bib1 "Explainable artificial intelligence (xai): concepts, taxonomies, opportunities and challenges toward responsible ai"); Kenny and Shah, [2024](https://arxiv.org/html/2602.16154v1#bib.bib2 "Regulation of language models with interpretability will likely result in a performance trade-off"); McMillan et al., [2025](https://arxiv.org/html/2602.16154v1#bib.bib3 "Towards transparent reasoning: what drives faithfulness in large language models?")).
21	
22	In the context of LLM reasoning, the risk of unfaithful reasoning is compounded by reinforcement learning (RL)-based approaches, which typically reward the accuracy of the final answer but not the faithfulness of the model’s reasoning (Lambert et al., [2024](https://arxiv.org/html/2602.16154v1#bib.bib28 "Tulu 3: pushing frontiers in open language model post-training")). Indeed, past work has found that outcome-only RL can lead to unfaithful or uninterpretable outputs (Guo et al., [2025](https://arxiv.org/html/2602.16154v1#bib.bib6 "Deepseek-r1: incentivizing reasoning capability in llms via reinforcement learning"); Kirchner et al., [2024](https://arxiv.org/html/2602.16154v1#bib.bib21 "Prover-verifier games improve legibility of llm outputs"); Jose, [2025](https://arxiv.org/html/2602.16154v1#bib.bib22 "Reasoning models sometimes output illegible chains of thought")). Unlike correctness, which can be objectively defined, we argue that faithfulness is a multi-party property: given a speaker and a listener, a faithful explanation is one which enables the listener model to come to the same conclusion as the speaker, without access to the speaker’s answer. For example, in [Figure 1](https://arxiv.org/html/2602.16154v1#S0.F1 "In Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution")(A), we see that when we truncate a reasoning chain from a speaker model to exclude its final few steps and its answer, listener models use the same reasoning prefix to come to different conclusions, indicating that the speaker’s reasoning prefix does not necessarily clearly lead to their final answer. We frame this as a question of _reasoning executability_: a reasoning chain is faithful if it can be executed by a similarly capable listener to recover the same conclusion, without access to the speaker’s answer; execution here refers to a “soft execution”, where a prefix of the speaker’s reasoning chain is provided to the listener, who follows it to its conclusion. Using this framing, we propose R easoning E xecution by Mu ltiple L isteners (REMuL), which trains models for both faithfulness and correctness simultaneously.
23	
24	Concretely, we train a speaker policy using Group Relative Policy Optimization (GRPO) (Guo et al., [2025](https://arxiv.org/html/2602.16154v1#bib.bib6 "Deepseek-r1: incentivizing reasoning capability in llms via reinforcement learning")) where the speaker generates a reasoning trace, which we then truncate to produce a prefix. This is illustrated in [Figure 1](https://arxiv.org/html/2602.16154v1#S0.F1 "In Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), where the speaker CoT is cut into two portions, prefix and suffix. The prefix is then passed to multiple independent listener models, while the truncated suffix is not shown. Each listener begins execution from the prefix and produces its own answer. As shown in [Figure 2](https://arxiv.org/html/2602.16154v1#S2.F2 "In 2.2 Cross-model Soft Reasoning Execution ‣ 2 Method ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution") (top), the speaker is rewarded when the listener agents converge to the same answer, with higher rewards for stronger consensus. Note that this process does not necessarily require the listener models to converge to a correct answer, but only to match the speaker’s answer. Indeed, we find that simultaneously aiming to reward for consistent listener reasoning execution and answer correctness often results in degraded performance for both metrics. Specifically, consistent with prior work (Arrieta et al., [2020](https://arxiv.org/html/2602.16154v1#bib.bib1 "Explainable artificial intelligence (xai): concepts, taxonomies, opportunities and challenges toward responsible ai"); Kenny and Shah, [2024](https://arxiv.org/html/2602.16154v1#bib.bib2 "Regulation of language models with interpretability will likely result in a performance trade-off"); McMillan et al., [2025](https://arxiv.org/html/2602.16154v1#bib.bib3 "Towards transparent reasoning: what drives faithfulness in large language models?")), we find that increasing faithfulness alone comes at a cost to correctness. To offset this, we incorporate correctness training into REMuL. Finding that jointly rewarding correctness and faithfulness via GRPO tends to lead to competing rewards and suboptimal performance, we introduce a mixed method which optimizes for faithfulness via RL and optimizes for correctness using supervised finetuning (SFT) with a LoRA (Hu et al., [2021](https://arxiv.org/html/2602.16154v1#bib.bib46 "LoRA: low-rank adaptation of large language models")) adapter, shown in [Figure 2](https://arxiv.org/html/2602.16154v1#S2.F2 "In 2.2 Cross-model Soft Reasoning Execution ‣ 2 Method ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution") (bottom).
25	
26	After training on data from BIG-Bench Hard (BBH; Suzgun et al., [2023](https://arxiv.org/html/2602.16154v1#bib.bib25 "Challenging big-bench tasks and whether chain-of-thought can solve them")), we evaluate REMuL on challenging reasoning problems from BIG-Bench Extra Hard (Kazemi et al., [2025](https://arxiv.org/html/2602.16154v1#bib.bib12 "Big-bench extra hard")), logic puzzles from ZebraLogicBench (Lin et al., [2025](https://arxiv.org/html/2602.16154v1#bib.bib13 "ZebraLogic: on the scaling limits of llms for logical reasoning")), multi-step logical deduction puzzles from MuSR (Sprague et al., [2024](https://arxiv.org/html/2602.16154v1#bib.bib14 "MuSR: testing the limits of chain-of-thought with multistep soft reasoning")), and first-order logic questions from FOLIO (Han et al., [2024](https://arxiv.org/html/2602.16154v1#bib.bib15 "Folio: natural language reasoning with first-order logic")). We measure faithfulness using intervention-based area over the curve (AOC) metrics (Lanham et al., [2023](https://arxiv.org/html/2602.16154v1#bib.bib5 "Measuring faithfulness in chain-of-thought reasoning")) as well as hint usage (Chen et al., [2025](https://arxiv.org/html/2602.16154v1#bib.bib4 "Reasoning models don’t always say what they think")), which tests whether model outputs faithfully verbalize changes in answers due to user-provided hints. Here, we find that our method improves hint attribution by up to 3.1% on Qwen3 and 2.7% on Phi4, while also boosting accuracy by up to 2.1% and 3.2%, respectively. We additionally observe gains of up to 4.6 AOC points for early answering from truncated CoT (a faithfulness measure introduced by Lanham et al. ([2023](https://arxiv.org/html/2602.16154v1#bib.bib5 "Measuring faithfulness in chain-of-thought reasoning"))).
27	
28	In our analysis, we explore REMuL’s impact on several dimensions of model behavior and justify key design choices. First, we find that our method improves legibility(Emmons et al., [2025](https://arxiv.org/html/2602.16154v1#bib.bib16 "A pragmatic way to measure chain-of-thought monitorability")) in model outputs, meaning that the produced reasoning chains are rated more clear and readable. We also perform an ablation study on our speaker-listener setup to demonstrate the importance of having multiple diverse listeners during training. Without either, we see diminished gains in both accuracy and faithfulness measures. We also observe a conflict in correctness and faithfulness reward signals when jointly optimized under a single reward, explaining the tradeoff observed under joint optimization and further motivating our multi-loss approach, which optimizes for correctness and faithfulness via distinct mechanisms. Finally, we study the impact of using in-domain data and find that while it does provide substantial boosts in accuracy, it does not necessarily result in gains to faithfulness. Our key contributions are summarized as follows:
29	
30	*   •We propose REMuL, a novel multi-party RL framework that trains models to produce faithful reasoning by rewarding speaker models for generating reasoning that is consistently executable by a diverse group of listener models, while simultaneously regularizing for correctness. 
31	*   •We show consistent gains on different faithfulness measures – hint attribution, AOC for early answering after CoT truncation, and AOC for mistake injection – while maintaining or improving task accuracy on multiple challenging reasoning benchmarks. 
32	*   •Our analysis indicates that REMuL’s gains translate to legibility, and we show that REMuL’s improved performance correlates with more concise and linear reasoning. 
33	
34	2 Method
35	--------
36	
37	### 2.1 Problem Setup
38	
39	Given an input prompt x x, a speaker model S S generates an explicit reasoning trace t t and a final answer a a, yielding an output y y. Our goal is to train S S to produce more faithful reasoning. More specifically, the produced trace t t should better reflect the process required to reach the answer a a. We formalize this computation via the notion of soft executability by a listener model L L.
40	
41	### 2.2 Cross-model Soft Reasoning Execution
42	
43	More formally, let t=⟨t 1,t 2,…,t n⟩t=\langle t_{1},t_{2},\ldots,t_{n}\rangle be a reasoning chain with n n steps, leading to answer a a. We define a soft execution of t t as M​(x,t 1,m)=a′M(x,t_{1,m})=a^{\prime}, where M M is a model, x x is an input prompt, t 1,m t_{1,m}, m≤n m\leq n is a partial reasoning chain, and a′a^{\prime} is the listener model response.2 2 2 We refer to this execution as “soft” to distinguish it from programmatic execution, e.g., Lyu et al. ([2023](https://arxiv.org/html/2602.16154v1#bib.bib30 "Faithful chain-of-thought reasoning")). Note that in this formulation, M M completes the remaining reasoning steps to reach a potentially different answer a′a^{\prime}. We define our faithfulness reward as 𝕀​[L​(x,t 1,m)=S​(x,t)]\mathbb{I}[L(x,t_{1,m})=S(x,t)] (or, equivalently, 𝕀[a′=a\mathbb{I}[a^{\prime}=a]) i.e. the degree to which a listener model L L reaches the same answer as the original speaker reasoning model S S. This process is illustrated in [Figure 1](https://arxiv.org/html/2602.16154v1#S0.F1 "In Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), where the speaker model’s partial chain is passed to multiple listeners.
44	
45	![Image 2: Refer to caption](https://arxiv.org/html/2602.16154v1/x2.png)
46	
47	Figure 2: REMuL consists of two components: (Top) A speaker-listener reasoning execution reward, where listeners execute reasoning prefixes from a speaker, who is rewarded for listener consensus. The speaker’s final answer is only used for reward computation and not seen by the listeners. (Bottom) A masked supervised finetuning step to maintain correctness via a LoRA adapter, with loss computed only on answer tokens.
48	
49	As illustrated in [Figure 2](https://arxiv.org/html/2602.16154v1#S2.F2 "In 2.2 Cross-model Soft Reasoning Execution ‣ 2 Method ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution") (top), REMuL uses cross-model execution as a training signal. We generate an initial response to input x x using S S and generate reasoning trace t t and final answer a a. We then truncate t t to 25%, 50%, and 75% of its length (split on newlines) to get T′={t 1,t 2,t 3}T^{\prime}=\{t_{1},t_{2},t_{3}\}. Then, given a set of listener models ℳ\mathcal{M}, for each listener model L i∈ℳ L_{i}\in\mathcal{M}, we obtain a finished reasoning trace starting from t j∈T′t_{j}\in T^{\prime} and final listener answer of a j i a_{j}^{i}. We compute a matching reward across the pool by the formula:
50	
51	r m​a​t​c​h=∑L i∈ℳ∑t j∈T′𝕀​[a j i=a]r_{match}=\sum_{L_{i}\in\mathcal{M}}\sum_{t_{j}\in T^{\prime}}\mathbb{I}\!\left[a_{j}^{i}=a\right](1)
52	
53	Based on this continued generation process, we reward the speaker policy using r m​a​t​c​h r_{match}. The main assumption is that if the speaker policy’s reasoning is logically sound, listener models should be more likely to converge to the same answer when continuing from the trace. Note that when training with r m​a​t​c​h r_{match} we use full-rank updates.
54	
55	### 2.3 Incorporating Correctness
56	
57	Due to observed accuracy tradeoffs (see [Section 3.4](https://arxiv.org/html/2602.16154v1#S3.SS4.SSS0.Px1 "Faithfulness improves with multi-party training, but naive optimization reduces correctness. ‣ 3.4 Main Results ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution")) when optimizing only for faithfulness, we test a variety of methods to improve correctness results during training.
58	
59	#### Balanced Rewards.
60	
61	We train S S with a reward that combines matching under cross-model execution and correctness term based on ground truth label g g. Under the balanced reward, the full reward function is as follows:
62	
63	r b​a​l​(x,y)=r m​a​t​c​h+λ​𝕀​[a=g],r_{bal}(x,y)=r_{match}+\lambda\,\mathbb{I}[a=g],(2)
64	
65	where λ\lambda is defined as the number of the listener models (i.e., |ℳ|\;|\mathcal{M}|). This balanced reward is then used when doing GRPO on our training data.
66	
67	#### Correctness Supervised Finetuning.
68	
69	We explore a supervised finetuning (SFT) strategy to mitigate accuracy drops while optimizing for faithfulness. In this approach, as illustrated in [Figure 2](https://arxiv.org/html/2602.16154v1#S2.F2 "In 2.2 Cross-model Soft Reasoning Execution ‣ 2 Method ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution") (bottom), we add a standard SFT loss to supervise only the final answer tokens while masking the reasoning trace, similar to Fang et al. ([2025](https://arxiv.org/html/2602.16154v1#bib.bib37 "Thinkless: llm learns when to think")). This isolates the correctness signal to the answer channel and avoids directly altering the reasoning trace. In other words, our loss is given by:
70	
71	ℒ ans​(θ)=−∑i∈𝒜 log⁡p θ​(y i∣x,y&lt;i),\mathcal{L}_{\text{ans}}(\theta)\;=\;-\sum_{i\in\mathcal{A}}\log p_{\theta}\!\left(y_{i}\mid x,y_{&lt;i}\right),(3)
72	
73	where 𝒜\mathcal{A} indexes the token positions corresponding to the final answer and token positions belonging to t t receive zero loss. Intuitively, this preserves the reasoning behaviors learned during faithfulness training (since we do not explicitly force a particular chain-of-thought), while still correcting the final decision boundary.
74	
75	### 2.4 Training Procedure
76	
77	We first optimize the original speaker model S S using Group Relative Policy Optimization (GRPO) (Guo et al., [2025](https://arxiv.org/html/2602.16154v1#bib.bib6 "Deepseek-r1: incentivizing reasoning capability in llms via reinforcement learning")). For each prompt x x, we sample a group of G G outputs {y i}i=1 G\{y_{i}\}_{i=1}^{G} from S S; then, for each y i y_{i} we apply truncation, pass the truncated traces through the population of listeners ℳ\mathcal{M}, and compute the reward r m​a​t​c​h r_{match}. When using a balanced reward that accounts for correctness, we instead use r b​a​l r_{bal}, an augmented version of r m​a​t​c​h r_{match} defined in [Equation 2](https://arxiv.org/html/2602.16154v1#S2.E2 "In Balanced Rewards. ‣ 2.3 Incorporating Correctness ‣ 2 Method ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). This reward is used to calculate relative advantages and increase the likelihood of higher-advantage outputs, iteratively teaching the speaker policy S S to output more executable and faithful traces.
78	
79	Separately, we finetune LoRA parameters using the masked correctness loss on top of the faithfulness-trained speaker checkpoint. We then merge the resulting trained LoRA adapter back into the original speaker checkpoint. Empirically, we find that this approach is especially effective for recovering accuracy while maintaining the behaviors induced by our multi-party training. Note that at test-time, only a single model (the speaker) is required, making the requirement for multiple models a fixed, training-time cost.
80	
81	3 Experiments and Results
82	-------------------------
83	
84	### 3.1 Experimental Setup
85	
86	#### Training data.
87	
88	We train on a subset of Big-Bench Hard (BBH) consisting of five tasks chosen because they reliably benefit from chain-of-thought (CoT) reasoning (Suzgun et al., [2023](https://arxiv.org/html/2602.16154v1#bib.bib25 "Challenging big-bench tasks and whether chain-of-thought can solve them")): (1) _Logical deduction – 5 objects_, (2) _Navigate_, (3) _Temporal_, (4) _Sports understanding_, and (5) _Shuffled objects_. We train Qwen3-14B (Yang et al., [2025](https://arxiv.org/html/2602.16154v1#bib.bib39 "Qwen3 technical report")) and Phi4 (Abdin et al., [2025](https://arxiv.org/html/2602.16154v1#bib.bib41 "Phi-4-reasoning technical report")) with thinking enabled for 3 epochs on this subset of 1250 QA pairs.
89	
90	#### Evaluation datasets.
91	
92	We evaluate on four multi-step reasoning benchmarks: Big-Bench Extra Hard (BBEH; Kazemi et al., [2025](https://arxiv.org/html/2602.16154v1#bib.bib12 "Big-bench extra hard")), ZebraLogicBench (ZLB; Lin et al., [2025](https://arxiv.org/html/2602.16154v1#bib.bib13 "ZebraLogic: on the scaling limits of llms for logical reasoning")), FOLIO (Han et al., [2024](https://arxiv.org/html/2602.16154v1#bib.bib15 "Folio: natural language reasoning with first-order logic")), and MuSR (Sprague et al., [2024](https://arxiv.org/html/2602.16154v1#bib.bib14 "MuSR: testing the limits of chain-of-thought with multistep soft reasoning")). For BBEH, we filter the benchmark to include only multiple-choice questions to match the training data and other evaluation setups, yielding 120 questions. For MuSR, we evaluate on the 250 question murder mysteries split of the dataset. For ZLB and FOLIO, we use the full multiple-choice splits with 3,259 and 202 question respectively. All four benchmarks require multi-step inference to reach the final answer and are designed to test models’ reasoning capabilities.
93	
94	#### Implementation details.
95	
96	Our training procedure follows the multi-party GRPO scheme described in Section[2](https://arxiv.org/html/2602.16154v1#S2 "2 Method ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), where listener models provide a matching-based learning signal via cross-model execution. To construct truncated reasoning traces, we split the model’s reasoning (contained between the &lt;think> tag) by newline characters and take the first p p% of lines as the truncated reasoning trace t j t_{j}. Listener models ℳ\mathcal{M} are prompted to continue from this truncated reasoning and produce a final answer, which we use to compute matching rewards. The listener models we use are Ministral-3-14B-Reasoning (Liu et al., [2026](https://arxiv.org/html/2602.16154v1#bib.bib42 "Ministral 3")), Phi-4-reasoning-plus 14B (Abdin et al., [2025](https://arxiv.org/html/2602.16154v1#bib.bib41 "Phi-4-reasoning technical report")), and Qwen3-14B (Yang et al., [2025](https://arxiv.org/html/2602.16154v1#bib.bib39 "Qwen3 technical report")). Across all methods, we keep prompts and answer formatting consistent within each dataset and evaluate each model under the same truncation and answer parsing rules. Details about individual model configurations are provided in [Appendix A](https://arxiv.org/html/2602.16154v1#A1.SS0.SSS0.Px1 "Model Details. ‣ Appendix A REMuL Details ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). Prompts are given in [Appendix C](https://arxiv.org/html/2602.16154v1#A3 "Appendix C Prompts ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution").
97	
98	### 3.2 Metrics
99	
100	We report end-task performance in terms of accuracy, as well as the following faithfulness metrics:
101	
102	Hint Usage. We measure faithfulness using the hint-injection protocol from Chen et al. ([2025](https://arxiv.org/html/2602.16154v1#bib.bib4 "Reasoning models don’t always say what they think")). For each example, we evaluate the model on the original prompt and a modified prompt containing an explicit hint. We use the sycophantic hint outlined in Chen et al. ([2025](https://arxiv.org/html/2602.16154v1#bib.bib4 "Reasoning models don’t always say what they think")) (e.g., _“Hint: I think the answer is Option A: True. What do you think?”_). If the model’s final answer changes between the two prompts, we check whether the model attributes the change to the hint in its explanation (rather than presenting the new answer as independently derived). The intuition is that if a model changed its answer from its original response without referencing the hint, then it is not faithfully expressing its decision making process, which depends on the hint. Inherently, this metric can only consider examples where the model changed its answer. We report hint usage as the percentage of changed-answer cases where the model explicitly cites the hint as the reason for the change. We detect hint usage by checking for a set of tokens listed in [Appendix A](https://arxiv.org/html/2602.16154v1#A1.SS0.SSS0.Px4 "Detection of hints. ‣ Appendix A REMuL Details ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution").
103	
104	Table 1: Accuracy and hint usage across different reasoning benchmarks. REMuL consistently improves hint usage over the correctness baseline while maintaining or improving accuracy, demonstrating an effective balance between task performance and faithful reasoning. We bold and italicize the first and second-best results, respectively. Hint Optimized (grayed) is excluded from ranking as it is directly optimized for the hint usage test metric. 
105	
106	#### AOC Metrics.
107	
108	Here, we use the early answering and adding mistakes area-over-the-curve (AOC) metrics from Lanham et al. ([2023](https://arxiv.org/html/2602.16154v1#bib.bib5 "Measuring faithfulness in chain-of-thought reasoning")). This metric truncates CoT reasoning at various split-points. For the “Truncated CoT Answering” setting, we force the model to answer at each point, measuring the accuracy. The higher the AOC is, the more of the reasoning chain is required to correctly answer, i.e., an AOC of 1 indicates that the model cannot answer correctly until the full reasoning is achieved. On the other hand, a lower AOC indicates that most of the reasoning is post-hoc rationalization, and that the answer is already inevitable early on in the reasoning chain. For the “Adding Mistakes” setting, we corrupt the reasoning chain by inserting errors at each split-point and allow the model to continue generating from the corrupted point onward. A higher AOC indicates that the model’s final answer is more sensitive to mistakes in its reasoning, suggesting it is faithfully conditioning on its chain of thought. Conversely, a lower AOC suggests the model arrives at the correct answer despite the introduced errors, indicating that the reasoning is not being faithfully followed. In our experiments, we measure accuracy at evenly spaced 20% increments along the original reasoning chain.
109	
110	### 3.3 Baselines
111	
112	We compare our trained models to the following baselines:
113	
114	*   •Original: the model before training. 
115	*   •Faithfulness Only: the model trained with only a matching reward using GRPO. 
116	*   •Correctness Only: the model trained with only a correctness reward, using GRPO. 
117	*   •Hint optimization: here, we directly optimize for hint usage via GRPO, i.e., directly optimize for the test metric; therefore, we treat this as a ceiling for hint usage. 
118	*   •MAT-Steer: introduced by Nguyen et al. ([2025](https://arxiv.org/html/2602.16154v1#bib.bib26 "Multi-attribute steering of language models via targeted intervention")), a steering approach that enables steering for multiple, potentially conflicting objectives. We produce steering vectors for correctness and faithfulness by collecting positive and negative samples in BIG-Bench Hard for these traits (i.e., final answers for correctness and presence of hints for prompts including hints) and apply MAT-Steer to layer 16 for both Qwen3 and Phi4, following Nguyen et al. ([2025](https://arxiv.org/html/2602.16154v1#bib.bib26 "Multi-attribute steering of language models via targeted intervention")). This represents a strong training-free baseline. 
119	
120	### 3.4 Main Results
121	
122	#### Faithfulness improves with multi-party training, but naive optimization reduces correctness.
123	
124	[Table 1](https://arxiv.org/html/2602.16154v1#S3.T1 "In 3.2 Metrics ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution") shows accuracy and hint usage across the four reasoning tasks. Optimizing for faithfulness alone (via speaker-listener RL) consistently leads to the highest hint usage, with a 4.1% and 3.7% average increase compared to the base model for Qwen3 and Phi4, respectively. The improvement is also most pronounced on benchmarks where baseline hint attribution is lower, suggesting that our training particularly helps when models have more room to grow. However, these improvements come at a cost to performance, with an average decrease in accuracy of 3.2% in Qwen3 and 2.2% in Phi4. Correctness-only training shows the opposite trend, with improvements of 2.9% in accuracy but a decrease of 1.8% in faithfulness. REMuL strikes a balance between these extremes, obtaining a 2.5% faithfulness gain while also maintaining accuracy, with 1.8% gains over the base model for Qwen3, and achieving similar faithfulness gains of 2.5% alongside a 1.5% accuracy improvement for Phi4.
125	
126	Table 2: Qwen3-14B AOC metrics for measuring faithfulness using truncated CoT and after adding mistakes to the CoT, following Lanham et al. ([2023](https://arxiv.org/html/2602.16154v1#bib.bib5 "Measuring faithfulness in chain-of-thought reasoning")). 
127	
128	Examining AOC metrics in [Table 2](https://arxiv.org/html/2602.16154v1#S3.T2 "In Faithfulness improves with multi-party training, but naive optimization reduces correctness. ‣ 3.4 Main Results ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), we see similar trends, with faithfulness-only training on Qwen3 improving AOC of Truncated CoT Answering by an average of 0.054 points across four datasets. Correctness-only results in the worst AOC in half the cases, whereas REMuL again balances faithfulness and correctness, improving by 0.033 points on average over the baseline.
129	
130	The Adding Mistake AOC shows similar trends. Faithfulness-only training again achieves the highest AOC across all four benchmarks, while correctness-only training and hint optimization yield the lowest scores, suggesting these models are more likely to ignore errors in their reasoning. REMuL obtains the second-best Adding Mistake AOC on all four datasets, improving over the base model by an average of 0.030 points, further supporting the finding that multi-party training produces reasoning that the model relies on.
131	
132	#### Steering improves faithfulness but falls short of training.
133	
134	In [Table 1](https://arxiv.org/html/2602.16154v1#S3.T1 "In 3.2 Metrics ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), we see that the steering baseline, MAT-Steer, consistently improves faithfulness, with 1.3% average gain. However, this falls short of the training-based approach in REMuL, which boosts faithfulness by 2.5%. Similarly, in [Table 2](https://arxiv.org/html/2602.16154v1#S3.T2 "In Faithfulness improves with multi-party training, but naive optimization reduces correctness. ‣ 3.4 Main Results ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), MAT-Steer offers strong improvements in Truncated CoT Answering on some datasets but not others, with substantial boosts on BBEH and FOLIO but marginal gains on ZebraLogicBench and MuSR. However, this pattern does not hold for Adding Mistake AOC, where MAT-Steer’s improvements over the base model are less pronounced, falling behind both faithfulness-only training and REMuL.
135	
136	#### Hint-only training increases hint usage but does not reliably improve other metrics.
137	
138	When optimizing for hint usage directly, we see a major increase in hint usage, as one might expect. However, this seems to be a local improvement without transferable improvements on other metrics: [Table 2](https://arxiv.org/html/2602.16154v1#S3.T2 "In Faithfulness improves with multi-party training, but naive optimization reduces correctness. ‣ 3.4 Main Results ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution") indicates that AOC with Truncated CoT Answering decreases when models are optimized for hint usage, with the hint usage-optimized model obtaining the worst AOC for half the datasets. This holds true for the AOC with Adding Mistake, where hint-optimized models obtain the lowest scores on all benchmarks.
139	
140	In contrast, faithfulness-only training and REMuL’s improvements to hint usage in [Table 1](https://arxiv.org/html/2602.16154v1#S3.T1 "In 3.2 Metrics ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution") transfer to [Table 2](https://arxiv.org/html/2602.16154v1#S3.T2 "In Faithfulness improves with multi-party training, but naive optimization reduces correctness. ‣ 3.4 Main Results ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), suggesting that multi-party listener training may do more to address unfaithfulness at its core, whereas optimizing for hint usage merely addresses one symptom. Similarly, [Table 1](https://arxiv.org/html/2602.16154v1#S3.T1 "In 3.2 Metrics ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution") shows that hint usage optimization hurts accuracy, with a 4.5% drop.
141	
142	4 Discussion and Analysis
143	-------------------------
144	
145	#### REMuL generalizes to legibility.
146	
147	Faithfulness and legibility – how easy a chain-of-thought is to read and understand – are highly related. In our evaluations, faithfulness metrics like hint usage and AOC measure to what degree a model makes use of its reasoning (i.e., to what degree the computation given is necessary and sufficient to reach the output), whereas legibility asks how comprehensible it is. Thus, it stands to reason that the improvements we see in faithfulness in [Table 1](https://arxiv.org/html/2602.16154v1#S3.T1 "In 3.2 Metrics ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution") and [Table 2](https://arxiv.org/html/2602.16154v1#S3.T2 "In Faithfulness improves with multi-party training, but naive optimization reduces correctness. ‣ 3.4 Main Results ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution") should also translate to better legibility.
148	
149	To measure this, we follow the legibility measurement method introduced by Emmons et al. ([2025](https://arxiv.org/html/2602.16154v1#bib.bib16 "A pragmatic way to measure chain-of-thought monitorability")). This process involves passing a model output to an autorater model and asking it to rate on a scale of 0 to 4 based on a set of scoring criteria. We perform all our measurements of legibility using GPT-OSS 20B (OpenAI, [2025](https://arxiv.org/html/2602.16154v1#bib.bib40 "GPT-OSS-120b and GPT-OSS-20b model card")) as our autorater model and evaluate on BBEH, ZLB, MuSR, and FOLIO. We use the prompt from Emmons et al. ([2025](https://arxiv.org/html/2602.16154v1#bib.bib16 "A pragmatic way to measure chain-of-thought monitorability")).
150	
151	As shown in [Table 3](https://arxiv.org/html/2602.16154v1#S4.T3 "In REMuL generalizes to legibility. ‣ 4 Discussion and Analysis ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), faithfulness-oriented training tends to make reasoning easier to follow. The faithfulness-only baseline achieves the highest legibility scores, improving by an average of 1.5 points over the base model. REMuL maintains high legibility with a comparable average score of 94.1, whereas correctness-only training produces the least legible traces, dropping 2.1 points below the baseline. The faithfulness improvements therefore lead to generated chains that are judged as clearer and more readable.
152	
153	Table 3: Legibility scores obtained following Emmons et al. ([2025](https://arxiv.org/html/2602.16154v1#bib.bib16 "A pragmatic way to measure chain-of-thought monitorability")), from a Qwen3-14B speaker. The best and second-best scores are in bold and italics, respectively.
154	
155	#### Ablations: multi-listener diverse models are required.
156	
157	To understand the design choices made in REMuL, we conduct two ablations investigating the necessity of our heterogeneous, multi-party setup. First, we test a single model type configuration where, instead of using diverse listener architectures, we use three instances of the speaker model with increased temperature. This tests the necessity of using multiple model types, rather than just the same speaker model. Second, we evaluate a single listener variant where the speaker trains against a randomly sampled model from the pool rather than aggregating consensus from three distinct listeners. This captures the benefit of multiple listeners, as opposed to a cheaper one-listener variant.
158	
159	[Table 4](https://arxiv.org/html/2602.16154v1#S4.T4 "In Ablations: multi-listener diverse models are required. ‣ 4 Discussion and Analysis ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution") shows that both of these changes hurt overall performance. While using a single model type does not damage the accuracy much, it does substantially reduce the faithfulness gains. Using a single listener instance, on the other hand, eliminates the gains for both accuracy and hint usage. Taken together, these ablations underscore the importance of multi-listener consensus with different model types.
160	
161	Table 4: Ablation study on listener model configurations (Qwen3). The best and second-best scores are in bold and italics, respectively.
162	
163	#### Faithfulness and correctness reward signals conflict.
164	
165	In [Table 1](https://arxiv.org/html/2602.16154v1#S3.T1 "In 3.2 Metrics ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), we see that rewarding correctness and faithfulness equally via RL leads to suboptimal performance, often with drops in performance for both accuracy and hint usage as compared to an untrained base model. Here, we explore this further by plotting the rewards over time for the correctness and faithfulness when trained together, as opposed to when trained separately. In [Figure 3](https://arxiv.org/html/2602.16154v1#S4.F3 "In REMuL leads to more concise and linear reasoning chains. ‣ 4 Discussion and Analysis ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), while we see that, individually, we can optimize models to improve both rewards, when these rewards are combined, they fail to increase at the same rate. Specifically, while the faithfulness component of the combined reward does increase (albeit at a more modest rate compared to the faithfulness-only reward), the correctness component of the combined reward stagnates. In other words, adding these rewards together seems to cancel them out, leading to little learning taking place.
166	
167	#### REMuL leads to more concise and linear reasoning chains.
168	
169	Qualitatively, we find that, whereas the base model’s reasoning chains are often quite long and convoluted, REMuL’s reasoning is often more concise and easier to follow. Here, we quantify this intuition in terms of reasoning length and number of backtracking steps.
170	
171	We measure length in terms of tokens in the reasoning chain (computed with a Qwen3 tokenizer). From [Table 5](https://arxiv.org/html/2602.16154v1#S4.T5 "In REMuL leads to more concise and linear reasoning chains. ‣ 4 Discussion and Analysis ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), we see that REMuL generally produces somewhat shorter reasoning traces for both the speaker and listener models compared to the base model. Specifically, for a Qwen3 speaker model, we see an average decrease of 4.88% in tokens on BBEH, ZLB, and FOLIO (with a modest increase in tokens by 2.61% for the MuSR dataset). Notably, these shorter chains from the speaker also result in shorter listener chains: for the set of listener models, REMuL produces 8.05% fewer tokens on average than the base model.
172	
173	Zooming in on this change in tokens, we also examine whether the resulting chains are more linear. Here, we measure the frequency of “backtracking” statements in the reasoning chain, e.g., _“Wait”_, _“Hold on…”_, etc., which typically result in a model reversing or abandoning its current line of thinking to pursue a different thought. While some degree of backtracking can be beneficial, excessive backtracking makes a reasoning chain hard to follow and may indicate unfaithfulness, with the model exploring paths that do not contribute to the final answer. We estimate backtracking by finding the average frequency of certain tokens (the full list of tokens is provided in [Appendix A](https://arxiv.org/html/2602.16154v1#A1.SS0.SSS0.Px3 "Detection of backtracking. ‣ Appendix A REMuL Details ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution")) that commonly indicate the emergence of this behavior. As seen in [Table 6](https://arxiv.org/html/2602.16154v1#S4.T6 "In REMuL leads to more concise and linear reasoning chains. ‣ 4 Discussion and Analysis ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), REMuL consistently reduces backtracking across all four benchmarks compared to the base model, with the largest reductions observed on BBEH and ZLB with 0.63 and 0.61 fewer backtracking statements, respectively. This suggests that training with REMuL encourages the speaker model to produce reasoning chains that more linearly leads to a final conclusion.
174	
175	![Image 3: Refer to caption](https://arxiv.org/html/2602.16154v1/x3.png)
176	
177	Figure 3:  Qwen3-14B reward curves during training for a model trained with a balanced, joint reward (Faithfulness + Correctness) as compared to each feature trained separately. 
178	
179	Table 5: Percent change in tokens after training with REMuL. For the Speaker models, the token count is the full generation length. For the Listener models, the token count is the generation length after a 50% truncated prefix CoT is passed in from the speaker (i.e., only counting the newly generated tokens).
180	
181	Table 6: Average frequency of backtracking terms in speaker CoTs.
182	
183	#### Training REMuL with in-domain data improves accuracy but does not necessarily improve faithfulness.
184	
185	The models in [Table 1](https://arxiv.org/html/2602.16154v1#S3.T1 "In 3.2 Metrics ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution") are trained on data sourced from BigBenchHard (BBH), making problems from other datasets out-of-domain. Nevertheless, REMuL is able to obtain generalizable improvements to faithfulness. Here, we examine to what extent domain matters for these faithfulness improvements, i.e., asking whether training on in-domain data would provide an even greater increase to faithfulness. For this experiment, we compare a model trained with REMuL on BBH samples to one trained on FOLIO samples (the only other dataset we evaluate on that has a training split). FOLIO’s training split contains 1000 samples compared to our subset of BBH with 1250 examples. We evaluate these trained models on FOLIO’s test set, as before. If faithfulness is learned as a generalizable skill, the domain of the training data should have a smaller impact.
186	
187	As shown in [Table 7](https://arxiv.org/html/2602.16154v1#S4.T7 "In Training REMuL with in-domain data improves accuracy but does not necessarily improve faithfulness. ‣ 4 Discussion and Analysis ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), training REMuL results in substantial improvements in task accuracy on FOLIO, improving by 5.7% compared to our original accuracy with REMuL. However, this gain in correctness with FOLIO training data does not translate into an improvement in the faithfulness metrics (Hint Usage and AOC for Truncated CoT). In fact, although AOC still improves by 0.008 points, implying slight faithfulness gains, hint attribution decreases even below the baseline by 1.7%. In contrast, REMuL trained on our multi-task subset of BBH has weaker accuracy, but the faithfulness measures increase. These findings motivate the need to use diverse training data in order to improve overall reasoning robustness rather than task accuracy alone.
188	
189	Table 7: Performance on FOLIO across Accuracy (Acc), hint attribution (Hint), and area over curve (AOC) for CoT Truncation answering for Qwen3-14b, REMuL using our default training data, and REMuL finetuned on the FOLIO training split. The best and second-best scores in bold and italics, respectively.
190	
191	5 Related Work
192	--------------
193	
194	#### Faithful Reasoning.
195	
196	A growing body of work has examined the faithfulness of chain-of-thought reasoning in LLMs, including work analyzing and measuring the degree to which LLMs generate reasoning that is a true representation of the computational process underlying an answer (Turpin et al., [2023](https://arxiv.org/html/2602.16154v1#bib.bib32 "Language models don’t always say what they think: unfaithful explanations in chain-of-thought prompting"); Lanham et al., [2023](https://arxiv.org/html/2602.16154v1#bib.bib5 "Measuring faithfulness in chain-of-thought reasoning"); Chen et al., [2025](https://arxiv.org/html/2602.16154v1#bib.bib4 "Reasoning models don’t always say what they think")). We make use of many of these metrics in our work. Related to executability, several approaches have sought to improve faithfulness by making reasoning chains executable via external systems (e.g., Python scripts), which we call hard execution(Chen et al., [2023](https://arxiv.org/html/2602.16154v1#bib.bib29 "Program of thoughts prompting: disentangling computation from reasoning for numerical reasoning tasks"); Lyu et al., [2023](https://arxiv.org/html/2602.16154v1#bib.bib30 "Faithful chain-of-thought reasoning")). While this ensures faithfulness, it can limit the model’s flexibility. In contrast, other works follow a notion of soft execution, where reasoning is completed by other language models rather than deterministic interpreters, broadening the scope of potential reasoning paths. Creswell and Shanahan ([2022](https://arxiv.org/html/2602.16154v1#bib.bib31 "Faithful reasoning using large language models")) explore the soft execution paradigm by separating selection of contextual information for question-answering from the actual LLM reasoning execution, leading to more humanly interpretable outputs. Wan et al. ([2025a](https://arxiv.org/html/2602.16154v1#bib.bib45 "GenerationPrograms: fine-grained attribution with executable programs")) also performs something between soft and hard execution, combining generation actions (select, paraphrase, fuse) that are executed by an LLM into a Python-style program for summarization and long-form QA. Similar programmatic approaches have been used in multimodal tasks (Surís et al., [2023](https://arxiv.org/html/2602.16154v1#bib.bib54 "Vipergpt: visual inference via python execution for reasoning"); Gupta and Kembhavi, [2023](https://arxiv.org/html/2602.16154v1#bib.bib55 "Visual programming: compositional visual reasoning without training")).
197	
198	A related line of work focuses on legibility (whether model outputs are clear and easily understood) and introduces methods to improve it (Kirchner et al., [2024](https://arxiv.org/html/2602.16154v1#bib.bib21 "Prover-verifier games improve legibility of llm outputs"); Korbak et al., [2022](https://arxiv.org/html/2602.16154v1#bib.bib33 "On reinforcement learning and distribution matching for fine-tuning language models with no catastrophic forgetting"); Emmons et al., [2025](https://arxiv.org/html/2602.16154v1#bib.bib16 "A pragmatic way to measure chain-of-thought monitorability")). We connect legibility and faithfulness, proposing a solution that offers improvements to both.
199	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0267a10f-9c10-4e66-a97d-93e09c4e5833",
  "isSidechain": true,
  "promptId": "8029e2e4-25c6-47cb-9539-6d3b0938c122",
  "agentId": "a7ed4918e81d4960b",
  "type": "user",
  "uuid": "f50f230f-85a0-42e7-82a7-aff3d2933619",
  "sourceToolAssistantUUID": "0267a10f-9c10-4e66-a97d-93e09c4e5833",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-19T09:13:45.395Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B4DZ3c1V6SzLBKgNPnSzTw`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-gen-pipeline/d3232602-cd70-49bb-a57b-21b3ab7347ad/tool-results/toolu_01WsipDpz1NE32BCo2LPsyNa.txt",
  "limit": 100,
  "offset": 199
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f50f230f-85a0-42e7-82a7-aff3d2933619",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfuBPERxWBXEtjzjVKs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "340229cd-adc3-4b04-9581-c240bd90557f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4QFpgiyJ3yZAtNpWGxWdb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14421,
      "cache_read_input_tokens": 43503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14421,
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

_source line 50 · 2026-05-19T09:13:45.659Z_

<details><summary>↩ Tool result · `toolu_01B4DZ3c1V6SzLBKgNPnSzTw`</summary>

```text
199	A related line of work focuses on legibility (whether model outputs are clear and easily understood) and introduces methods to improve it (Kirchner et al., [2024](https://arxiv.org/html/2602.16154v1#bib.bib21 "Prover-verifier games improve legibility of llm outputs"); Korbak et al., [2022](https://arxiv.org/html/2602.16154v1#bib.bib33 "On reinforcement learning and distribution matching for fine-tuning language models with no catastrophic forgetting"); Emmons et al., [2025](https://arxiv.org/html/2602.16154v1#bib.bib16 "A pragmatic way to measure chain-of-thought monitorability")). We connect legibility and faithfulness, proposing a solution that offers improvements to both.
200	
201	#### Multi-Model Training.
202	
203	Our approach builds on emerging work that uses multi-agent signals to train and improve LLMs. LACIE (Stengel-Eskin et al., [2024b](https://arxiv.org/html/2602.16154v1#bib.bib43 "LACIE: listener-aware finetuning for calibration in large language models")) introduces a speaker-listener finetuning method for verbalized confidence calibration, where a speaker model generates responses and a listener model judges whether to accept or reject them based on perceived confidence. A similar approach is applied by Stengel-Eskin et al. ([2025](https://arxiv.org/html/2602.16154v1#bib.bib38 "Teaching models to balance resisting and accepting persuasion")) for teaching models to accept or reject persuasion as appropriate. West et al. ([2025](https://arxiv.org/html/2602.16154v1#bib.bib34 "Tandem training for language models")) propose a reinforcement learning algorithm in which tokens are sampled intermittently from a weak frozen model to ensure that the output of the strong model remains intelligible to weaker collaborators. Wang et al. ([2024](https://arxiv.org/html/2602.16154v1#bib.bib44 "SOTOPIA-π: interactive learning of socially intelligent language agents")) improves the social intelligence of a small model by using expert model ratings for self-reinforcement learning. Other collaborative training approaches include Berant et al. ([2025](https://arxiv.org/html/2602.16154v1#bib.bib35 "Learning steerable clarification policies with collaborative self-play")) who use interactions between user and assistant models to adapt to varying cost constraints, and Eisenstein et al. ([2025](https://arxiv.org/html/2602.16154v1#bib.bib36 "Don’t lie to your friends: learning what you know from collaborative self-play")) who use group-level rewards in multi-agent interactions to train models for tool-use and calibration. Recent work has also explored joint optimization via multi-agent reinforcement learning. For instance, Wan et al. ([2025b](https://arxiv.org/html/2602.16154v1#bib.bib57 "ReMA: learning to meta-think for llms with multi-agent reinforcement learning")) and Park et al. ([2025](https://arxiv.org/html/2602.16154v1#bib.bib58 "MAPoRL: multi-agent post-co-training for collaborative large language models with reinforcement learning")) utilize RL to train models for collaborative reasoning and meta-thinking. Yuan et al. ([2025](https://arxiv.org/html/2602.16154v1#bib.bib59 "Marshal: incentivizing multi-agent reasoning via self-play with strategic llms")) uses “self-play” among LLMs to improve performance in strategic games. In contrast to these works, REMuL focuses on faithfulness, has speakers exchange truncated reasoning prefixes rather than complete messages, and incorporates correctness signals as a separate training procedure.
204	
205	6 Conclusion
206	------------
207	
208	We proposed REMuL, a multi-party training framework to improve faithfulness in reasoning models. By incentivizing the speaker model to produce reasoning traces that listener models can effectively execute across multiple truncation points, we encourage the policy model to generate responses that are executable by listener models using soft execution, i.e., completing a reasoning prefix. A key finding of our work is the importance of decoupling the training strategies for faithfulness and accuracy, allowing us to improve faithfulness without incurring the typical loss in accuracy that comes with such improvements. REMuL shows consistent gains on different faithfulness measures – hint attribution and AOC for early answering after CoT truncation – while maintaining or improving task accuracy across multiple challenging reasoning benchmarks. Our analysis indicates that REMuL’s gains translate to legibility, and we show that REMuL’s improved performance correlates with more concise and linear reasoning. Taken together, our results across multiple benchmarks demonstrate that it is possible to train models that are both more transparent about their computational process and accurate on downstream tasks.
209	
210	Impact Statement
211	----------------
212	
213	Faithful reasoning is a critical component to monitorability, verifiability and trust. By improving faithfulness in models, we are taking a step towards improving these qualities and making models more reliable. Beyond this, there are no particular societal consequences that apply to our work aside from those that apply to LLMs more generally.
214	
215	Acknowledgments
216	---------------
217	
218	This work was supported by NSF-CAREER Award 1846185, DARPA ECOLE Program No. HR00112390060, NSF AI Engage Institute DRL-2112635, National Institutes of Health (NIH) under other transactions 1OT2OD038045-01, and Cisco Faculty Award. The views and conclusions contained in this document are those of the authors and should not be interpreted as representing official policies, either expressed or implied, of the NIH or other sponsors.
219	
220	References
221	----------
222	
223	*   M. Abdin, S. Agarwal, A. Awadallah, V. Balachandran, H. Behl, L. Chen, G. de Rosa, S. Gunasekar, M. Javaheripi, N. Joshi, et al. (2025)Phi-4-reasoning technical report. arXiv preprint arXiv:2504.21318. Cited by: [§3.1](https://arxiv.org/html/2602.16154v1#S3.SS1.SSS0.Px1.p1.1 "Training data. ‣ 3.1 Experimental Setup ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [§3.1](https://arxiv.org/html/2602.16154v1#S3.SS1.SSS0.Px3.p1.3 "Implementation details. ‣ 3.1 Experimental Setup ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
224	*   A. B. Arrieta, N. Díaz-Rodríguez, J. Del Ser, A. Bennetot, S. Tabik, A. Barbado, S. García, S. Gil-López, D. Molina, R. Benjamins, et al. (2020)Explainable artificial intelligence (xai): concepts, taxonomies, opportunities and challenges toward responsible ai. Information fusion 58,  pp.82–115. Cited by: [§1](https://arxiv.org/html/2602.16154v1#S1.p1.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [§1](https://arxiv.org/html/2602.16154v1#S1.p3.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
225	*   F. Barez, T. Wu, I. Arcuschin, M. Lan, V. Wang, N. Siegel, N. Collignon, C. Neo, I. Lee, A. Paren, et al. (2025)Chain-of-thought is not explainability. Preprint, alphaXiv,  pp.v1. Cited by: [§1](https://arxiv.org/html/2602.16154v1#S1.p1.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
226	*   J. Berant, M. Chen, A. Fisch, R. Aghajani, F. Huot, M. Lapata, and J. Eisenstein (2025)Learning steerable clarification policies with collaborative self-play. arXiv preprint arXiv:2512.04068. Cited by: [§5](https://arxiv.org/html/2602.16154v1#S5.SS0.SSS0.Px2.p1.1 "Multi-Model Training. ‣ 5 Related Work ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
227	*   W. Chen, X. Ma, X. Wang, and W. W. Cohen (2023)Program of thoughts prompting: disentangling computation from reasoning for numerical reasoning tasks. Transactions on Machine Learning Research. Cited by: [§5](https://arxiv.org/html/2602.16154v1#S5.SS0.SSS0.Px1.p1.1 "Faithful Reasoning. ‣ 5 Related Work ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
228	*   Y. Chen, J. Benton, A. Radhakrishnan, J. Uesato, C. Denison, J. Schulman, A. Somani, P. Hase, M. Wagner, F. Roger, et al. (2025)Reasoning models don’t always say what they think. arXiv preprint arXiv:2505.05410. Cited by: [§1](https://arxiv.org/html/2602.16154v1#S1.p1.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [§1](https://arxiv.org/html/2602.16154v1#S1.p4.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [§3.2](https://arxiv.org/html/2602.16154v1#S3.SS2.p2.1 "3.2 Metrics ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [§5](https://arxiv.org/html/2602.16154v1#S5.SS0.SSS0.Px1.p1.1 "Faithful Reasoning. ‣ 5 Related Work ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
229	*   D. Choi, J. Lee, J. Tack, W. Song, S. Dingliwal, S. M. Jayanthi, B. Ganesh, J. Shin, A. Galstyan, and S. B. Bodapati (2025)Think clearly: improving reasoning via redundant token pruning. In ES-FoMo III: 3rd Workshop on Efficient Systems for Foundation Models, Cited by: [Appendix A](https://arxiv.org/html/2602.16154v1#A1.SS0.SSS0.Px3.p1.1 "Detection of backtracking. ‣ Appendix A REMuL Details ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
230	*   A. Creswell and M. Shanahan (2022)Faithful reasoning using large language models. arXiv preprint arXiv:2208.14271. Cited by: [§5](https://arxiv.org/html/2602.16154v1#S5.SS0.SSS0.Px1.p1.1 "Faithful Reasoning. ‣ 5 Related Work ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
231	*   J. Eisenstein, R. Aghajani, A. Fisch, D. Dua, F. Huot, M. Lapata, V. Zayats, and J. Berant (2025)Don’t lie to your friends: learning what you know from collaborative self-play. arXiv preprint arXiv:2503.14481. Cited by: [§5](https://arxiv.org/html/2602.16154v1#S5.SS0.SSS0.Px2.p1.1 "Multi-Model Training. ‣ 5 Related Work ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
232	*   S. Emmons, R. S. Zimmermann, D. K. Elson, and R. Shah (2025)A pragmatic way to measure chain-of-thought monitorability. arXiv preprint arXiv:2510.23966. Cited by: [§1](https://arxiv.org/html/2602.16154v1#S1.p5.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [§4](https://arxiv.org/html/2602.16154v1#S4.SS0.SSS0.Px1.p2.1 "REMuL generalizes to legibility. ‣ 4 Discussion and Analysis ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [Table 3](https://arxiv.org/html/2602.16154v1#S4.T3 "In REMuL generalizes to legibility. ‣ 4 Discussion and Analysis ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [Table 3](https://arxiv.org/html/2602.16154v1#S4.T3.5.2 "In REMuL generalizes to legibility. ‣ 4 Discussion and Analysis ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [§5](https://arxiv.org/html/2602.16154v1#S5.SS0.SSS0.Px1.p2.1 "Faithful Reasoning. ‣ 5 Related Work ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
233	*   G. Fang, X. Ma, and X. Wang (2025)Thinkless: llm learns when to think. arXiv preprint arXiv:2505.13379. Cited by: [§2.3](https://arxiv.org/html/2602.16154v1#S2.SS3.SSS0.Px2.p1.3 "Correctness Supervised Finetuning. ‣ 2.3 Incorporating Correctness ‣ 2 Method ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
234	*   A. Fanous, J. Goldberg, A. Agarwal, J. Lin, A. Zhou, S. Xu, V. Bikia, R. Daneshjou, and S. Koyejo (2025)Syceval: evaluating llm sycophancy. In Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society, Vol. 8,  pp.893–900. Cited by: [Appendix B](https://arxiv.org/html/2602.16154v1#A2.SS0.SSS0.Px5.p1.1 "Sycophancy. ‣ Appendix B Additional Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
235	*   J. Geng, F. Cai, Y. Wang, H. Koeppl, P. Nakov, and I. Gurevych (2024)A survey of confidence estimation and calibration in large language models. In Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), K. Duh, H. Gomez, and S. Bethard (Eds.), Mexico City, Mexico,  pp.6577–6595. External Links: [Link](https://aclanthology.org/2024.naacl-long.366/), [Document](https://dx.doi.org/10.18653/v1/2024.naacl-long.366)Cited by: [Appendix B](https://arxiv.org/html/2602.16154v1#A2.SS0.SSS0.Px3.p1.1 "Calibration. ‣ Appendix B Additional Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
236	*   C. Guo, G. Pleiss, Y. Sun, and K. Q. Weinberger (2017)On calibration of modern neural networks. In International conference on machine learning,  pp.1321–1330. Cited by: [Appendix B](https://arxiv.org/html/2602.16154v1#A2.SS0.SSS0.Px3.p1.1 "Calibration. ‣ Appendix B Additional Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
237	*   D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, S. Ma, P. Wang, X. Bi, et al. (2025)Deepseek-r1: incentivizing reasoning capability in llms via reinforcement learning. arXiv preprint arXiv:2501.12948. Cited by: [§1](https://arxiv.org/html/2602.16154v1#S1.p2.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [§1](https://arxiv.org/html/2602.16154v1#S1.p3.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [§2.4](https://arxiv.org/html/2602.16154v1#S2.SS4.p1.11 "2.4 Training Procedure ‣ 2 Method ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
238	*   T. Gupta and A. Kembhavi (2023)Visual programming: compositional visual reasoning without training. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition,  pp.14953–14962. Cited by: [§5](https://arxiv.org/html/2602.16154v1#S5.SS0.SSS0.Px1.p1.1 "Faithful Reasoning. ‣ 5 Related Work ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
239	*   S. Han, H. Schoelkopf, Y. Zhao, Z. Qi, M. Riddell, W. Zhou, J. Coady, D. Peng, Y. Qiao, L. Benson, et al. (2024)Folio: natural language reasoning with first-order logic. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing,  pp.22017–22031. Cited by: [§1](https://arxiv.org/html/2602.16154v1#S1.p4.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [§3.1](https://arxiv.org/html/2602.16154v1#S3.SS1.SSS0.Px2.p1.1 "Evaluation datasets. ‣ 3.1 Experimental Setup ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
240	*   D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, D. Song, and J. Steinhardt (2021)Measuring mathematical problem solving with the math dataset. In Thirty-fifth Conference on Neural Information Processing Systems, Cited by: [Appendix B](https://arxiv.org/html/2602.16154v1#A2.SS0.SSS0.Px5.p1.1 "Sycophancy. ‣ Appendix B Additional Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
241	*   E. J. Hu, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, W. Chen, et al. (2021)LoRA: low-rank adaptation of large language models. In International Conference on Learning Representations, Cited by: [§1](https://arxiv.org/html/2602.16154v1#S1.p3.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
242	*   A. Jose (2025)Reasoning models sometimes output illegible chains of thought. In The Thirty-ninth Annual Conference on Neural Information Processing Systems, External Links: [Link](https://openreview.net/forum?id=w1TjXJk846)Cited by: [§1](https://arxiv.org/html/2602.16154v1#S1.p2.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
243	*   S. Kadavath, T. Conerly, A. Askell, T. Henighan, D. Drain, E. Perez, N. Schiefer, Z. Hatfield-Dodds, N. DasSarma, E. Tran-Johnson, et al. (2022)Language models (mostly) know what they know. arXiv preprint arXiv:2207.05221. Cited by: [Appendix B](https://arxiv.org/html/2602.16154v1#A2.SS0.SSS0.Px4.p1.1 "Solvability estimation. ‣ Appendix B Additional Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
244	*   M. Kazemi, B. Fatemi, H. Bansal, J. Palowitch, C. Anastasiou, S. V. Mehta, L. K. Jain, V. Aglietti, D. Jindal, Y. P. Chen, et al. (2025)Big-bench extra hard. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),  pp.26473–26501. Cited by: [§1](https://arxiv.org/html/2602.16154v1#S1.p4.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [§3.1](https://arxiv.org/html/2602.16154v1#S3.SS1.SSS0.Px2.p1.1 "Evaluation datasets. ‣ 3.1 Experimental Setup ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
245	*   E. M. Kenny and J. A. Shah (2024)Regulation of language models with interpretability will likely result in a performance trade-off. arXiv preprint arXiv:2412.12169. Cited by: [§1](https://arxiv.org/html/2602.16154v1#S1.p1.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [§1](https://arxiv.org/html/2602.16154v1#S1.p3.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
246	*   J. H. Kirchner, Y. Chen, H. Edwards, J. Leike, N. McAleese, and Y. Burda (2024)Prover-verifier games improve legibility of llm outputs. arXiv preprint arXiv:2407.13692. Cited by: [§1](https://arxiv.org/html/2602.16154v1#S1.p2.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [§5](https://arxiv.org/html/2602.16154v1#S5.SS0.SSS0.Px1.p2.1 "Faithful Reasoning. ‣ 5 Related Work ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
247	*   T. Korbak, H. Elsahar, G. Kruszewski, and M. Dymetmant (2022)On reinforcement learning and distribution matching for fine-tuning language models with no catastrophic forgetting. In Proceedings of the 36th International Conference on Neural Information Processing Systems,  pp.16203–16220. Cited by: [§5](https://arxiv.org/html/2602.16154v1#S5.SS0.SSS0.Px1.p2.1 "Faithful Reasoning. ‣ 5 Related Work ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
248	*   W. Kwon, Z. Li, S. Zhuang, Y. Sheng, L. Zheng, C. H. Yu, J. E. Gonzalez, H. Zhang, and I. Stoica (2023)Efficient memory management for large language model serving with pagedattention. In Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles, Cited by: [Appendix A](https://arxiv.org/html/2602.16154v1#A1.SS0.SSS0.Px2.p1.1 "Training details. ‣ Appendix A REMuL Details ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
249	*   N. Lambert, J. Morrison, V. Pyatkin, S. Huang, H. Ivison, F. Brahman, L. J. V. Miranda, A. Liu, N. Dziri, S. Lyu, et al. (2024)Tulu 3: pushing frontiers in open language model post-training. arXiv preprint arXiv:2411.15124. Cited by: [§1](https://arxiv.org/html/2602.16154v1#S1.p2.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
250	*   T. Lanham, A. Chen, A. Radhakrishnan, B. Steiner, C. Denison, D. Hernandez, D. Li, E. Durmus, E. Hubinger, J. Kernion, et al. (2023)Measuring faithfulness in chain-of-thought reasoning. arXiv preprint arXiv:2307.13702. Cited by: [§1](https://arxiv.org/html/2602.16154v1#S1.p1.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [§1](https://arxiv.org/html/2602.16154v1#S1.p4.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [§3.2](https://arxiv.org/html/2602.16154v1#S3.SS2.SSS0.Px1.p1.1 "AOC Metrics. ‣ 3.2 Metrics ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [Table 2](https://arxiv.org/html/2602.16154v1#S3.T2 "In Faithfulness improves with multi-party training, but naive optimization reduces correctness. ‣ 3.4 Main Results ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [Table 2](https://arxiv.org/html/2602.16154v1#S3.T2.3.2 "In Faithfulness improves with multi-party training, but naive optimization reduces correctness. ‣ 3.4 Main Results ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [§5](https://arxiv.org/html/2602.16154v1#S5.SS0.SSS0.Px1.p1.1 "Faithful Reasoning. ‣ 5 Related Work ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
251	*   B. Y. Lin, R. Le Bras, K. Richardson, A. Sabharwal, R. Poovendran, P. Clark, and Y. Choi (2025)ZebraLogic: on the scaling limits of llms for logical reasoning. In Forty-second International Conference on Machine Learning, Cited by: [§1](https://arxiv.org/html/2602.16154v1#S1.p4.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [§3.1](https://arxiv.org/html/2602.16154v1#S3.SS1.SSS0.Px2.p1.1 "Evaluation datasets. ‣ 3.1 Experimental Setup ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
252	*   A. H. Liu, K. Khandelwal, S. Subramanian, V. Jouault, A. Rastogi, A. Sadé, A. Jeffares, A. Jiang, A. Cahill, A. Gavaudan, et al. (2026)Ministral 3. arXiv preprint arXiv:2601.08584. Cited by: [§3.1](https://arxiv.org/html/2602.16154v1#S3.SS1.SSS0.Px3.p1.3 "Implementation details. ‣ 3.1 Experimental Setup ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
253	*   I. Loshchilov and F. Hutter (2017)Decoupled weight decay regularization. In International Conference on Learning Representations, Cited by: [Appendix A](https://arxiv.org/html/2602.16154v1#A1.SS0.SSS0.Px2.p1.1 "Training details. ‣ Appendix A REMuL Details ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
254	*   Q. Lyu, S. Havaldar, A. Stein, L. Zhang, D. Rao, E. Wong, M. Apidianaki, and C. Callison-Burch (2023)Faithful chain-of-thought reasoning. In Proceedings of the 13th International Joint Conference on Natural Language Processing and the 3rd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (Volume 1: Long Papers),  pp.305–329. Cited by: [§5](https://arxiv.org/html/2602.16154v1#S5.SS0.SSS0.Px1.p1.1 "Faithful Reasoning. ‣ 5 Related Work ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [footnote 2](https://arxiv.org/html/2602.16154v1#footnote2 "In 2.2 Cross-model Soft Reasoning Execution ‣ 2 Method ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
255	*   S. Mangrulkar, S. Gugger, L. Debut, Y. Belkada, S. Paul, B. Bossan, and M. Tietz (2022)PEFT: state-of-the-art parameter-efficient fine-tuning methods. Note: [https://github.com/huggingface/peft](https://github.com/huggingface/peft)Cited by: [Appendix A](https://arxiv.org/html/2602.16154v1#A1.SS0.SSS0.Px2.p1.1 "Training details. ‣ Appendix A REMuL Details ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
256	*   A. M. Mashraqi and B. Allehyani (2022)Current trends on the application of artificial intelligence in medical sciences. Bioinformation 18 (11),  pp.1050. Cited by: [§1](https://arxiv.org/html/2602.16154v1#S1.p1.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
257	*   T. McMillan, G. Dominici, M. Gjoreski, and M. Langheinrich (2025)Towards transparent reasoning: what drives faithfulness in large language models?. In NeurIPS 2025 Workshop on Evaluating the Evolving LLM Lifecycle: Benchmarks, Emergent Abilities, and Scaling, Cited by: [§1](https://arxiv.org/html/2602.16154v1#S1.p1.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [§1](https://arxiv.org/html/2602.16154v1#S1.p3.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
258	*   D. Nguyen, A. Prasad, E. Stengel-Eskin, and M. Bansal (2025)Multi-attribute steering of language models via targeted intervention. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), W. Che, J. Nabende, E. Shutova, and M. T. Pilehvar (Eds.), Vienna, Austria,  pp.20619–20634. External Links: [Link](https://aclanthology.org/2025.acl-long.1007/), [Document](https://dx.doi.org/10.18653/v1/2025.acl-long.1007), ISBN 979-8-89176-251-0 Cited by: [5th item](https://arxiv.org/html/2602.16154v1#S3.I1.i5.p1.1 "In 3.3 Baselines ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
259	*   OpenAI (2025)GPT-OSS-120b and GPT-OSS-20b model card. External Links: 2508.10925, [Link](https://arxiv.org/abs/2508.10925)Cited by: [§4](https://arxiv.org/html/2602.16154v1#S4.SS0.SSS0.Px1.p2.1 "REMuL generalizes to legibility. ‣ 4 Discussion and Analysis ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
260	*   M. Pakdaman Naeini, G. Cooper, and M. Hauskrecht (2015)Obtaining well calibrated probabilities using bayesian binning. Proceedings of the AAAI Conference on Artificial Intelligence 29 (1). External Links: [Link](https://ojs.aaai.org/index.php/AAAI/article/view/9602), [Document](https://dx.doi.org/10.1609/aaai.v29i1.9602)Cited by: [Appendix B](https://arxiv.org/html/2602.16154v1#A2.SS0.SSS0.Px3.p1.1 "Calibration. ‣ Appendix B Additional Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
261	*   C. Park, S. Han, X. Guo, A. E. Ozdaglar, K. Zhang, and J. Kim (2025)MAPoRL: multi-agent post-co-training for collaborative large language models with reinforcement learning. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), W. Che, J. Nabende, E. Shutova, and M. T. Pilehvar (Eds.), Vienna, Austria,  pp.30215–30248. External Links: [Link](https://aclanthology.org/2025.acl-long.1459/), [Document](https://dx.doi.org/10.18653/v1/2025.acl-long.1459), ISBN 979-8-89176-251-0 Cited by: [§5](https://arxiv.org/html/2602.16154v1#S5.SS0.SSS0.Px2.p1.1 "Multi-Model Training. ‣ 5 Related Work ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
262	*   P. Rajpurkar, E. Chen, O. Banerjee, and E. J. Topol (2022)AI in health and medicine. Nature medicine 28 (1),  pp.31–38. Cited by: [§1](https://arxiv.org/html/2602.16154v1#S1.p1.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
263	*   D. B. Resnik and M. Hosseini (2025)The ethics of using artificial intelligence in scientific research: new guidance needed for a new tool. AI and Ethics 5 (2),  pp.1499–1521. Cited by: [§1](https://arxiv.org/html/2602.16154v1#S1.p1.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
264	*   D. Schwarcz, S. Manning, P. Barry, D. R. Cleveland, J. Prescott, and B. Rich (2025)Ai-powered lawyering: ai reasoning models, retrieval augmented generation, and the future of legal practice. Journal of Law and Empirical Analysis. Cited by: [§1](https://arxiv.org/html/2602.16154v1#S1.p1.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
265	*   G. Sheng, C. Zhang, Z. Ye, X. Wu, W. Zhang, R. Zhang, Y. Peng, H. Lin, and C. Wu (2024)HybridFlow: a flexible and efficient rlhf framework. arXiv preprint arXiv: 2409.19256. Cited by: [Appendix A](https://arxiv.org/html/2602.16154v1#A1.SS0.SSS0.Px2.p1.1 "Training details. ‣ Appendix A REMuL Details ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
266	*   S. R. Sitaraman (2025)AI-driven healthcare systems enhanced by advanced data analytics and mobile computing. International Journal of Information Technology and Computer Engineering. Cited by: [§1](https://arxiv.org/html/2602.16154v1#S1.p1.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
267	*   Z. R. Sprague, X. Ye, K. Bostrom, S. Chaudhuri, and G. Durrett (2024)MuSR: testing the limits of chain-of-thought with multistep soft reasoning. In The Twelfth International Conference on Learning Representations, Cited by: [§1](https://arxiv.org/html/2602.16154v1#S1.p4.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [§3.1](https://arxiv.org/html/2602.16154v1#S3.SS1.SSS0.Px2.p1.1 "Evaluation datasets. ‣ 3.1 Experimental Setup ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
268	*   E. Stengel-Eskin, P. Hase, and M. Bansal (2024a)LACIE: listener-aware finetuning for calibration in large language models. Advances in Neural Information Processing Systems 37,  pp.43080–43106. Cited by: [Appendix B](https://arxiv.org/html/2602.16154v1#A2.SS0.SSS0.Px3.p1.1 "Calibration. ‣ Appendix B Additional Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
269	*   E. Stengel-Eskin, P. Hase, and M. Bansal (2024b)LACIE: listener-aware finetuning for calibration in large language models. Advances in Neural Information Processing Systems 37,  pp.43080–43106. Cited by: [§5](https://arxiv.org/html/2602.16154v1#S5.SS0.SSS0.Px2.p1.1 "Multi-Model Training. ‣ 5 Related Work ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
270	*   E. Stengel-Eskin, P. Hase, and M. Bansal (2025)Teaching models to balance resisting and accepting persuasion. In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers),  pp.8108–8122. Cited by: [§5](https://arxiv.org/html/2602.16154v1#S5.SS0.SSS0.Px2.p1.1 "Multi-Model Training. ‣ 5 Related Work ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
271	*   D. Surís, S. Menon, and C. Vondrick (2023)Vipergpt: visual inference via python execution for reasoning. In Proceedings of the IEEE/CVF international conference on computer vision,  pp.11888–11898. Cited by: [§5](https://arxiv.org/html/2602.16154v1#S5.SS0.SSS0.Px1.p1.1 "Faithful Reasoning. ‣ 5 Related Work ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
272	*   M. Suzgun, N. Scales, N. Schärli, S. Gehrmann, Y. Tay, H. W. Chung, A. Chowdhery, Q. Le, E. Chi, D. Zhou, et al. (2023)Challenging big-bench tasks and whether chain-of-thought can solve them. In Findings of the Association for Computational Linguistics: ACL 2023,  pp.13003–13051. Cited by: [§1](https://arxiv.org/html/2602.16154v1#S1.p4.1 "1 Introduction ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [§3.1](https://arxiv.org/html/2602.16154v1#S3.SS1.SSS0.Px1.p1.1 "Training data. ‣ 3.1 Experimental Setup ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
273	*   M. Turpin, J. Michael, E. Perez, and S. R. Bowman (2023)Language models don’t always say what they think: unfaithful explanations in chain-of-thought prompting. In Proceedings of the 37th International Conference on Neural Information Processing Systems,  pp.74952–74965. Cited by: [§5](https://arxiv.org/html/2602.16154v1#S5.SS0.SSS0.Px1.p1.1 "Faithful Reasoning. ‣ 5 Related Work ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
274	*   D. Wan, E. Hirsch, E. Stengel-Eskin, I. Dagan, and M. Bansal (2025a)GenerationPrograms: fine-grained attribution with executable programs. arXiv preprint arXiv:2506.14580. Cited by: [§5](https://arxiv.org/html/2602.16154v1#S5.SS0.SSS0.Px1.p1.1 "Faithful Reasoning. ‣ 5 Related Work ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
275	*   Z. Wan, L. Yunxiang, X. Wen, Y. Song, H. Wang, L. Yang, M. Schmidt, J. Wang, W. Zhang, S. Hu, et al. (2025b)ReMA: learning to meta-think for llms with multi-agent reinforcement learning. In The Thirty-ninth Annual Conference on Neural Information Processing Systems, Cited by: [§5](https://arxiv.org/html/2602.16154v1#S5.SS0.SSS0.Px2.p1.1 "Multi-Model Training. ‣ 5 Related Work ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
276	*   R. Wang, H. Yu, W. Zhang, Z. Qi, M. Sap, Y. Bisk, G. Neubig, and H. Zhu (2024)SOTOPIA-π\pi: interactive learning of socially intelligent language agents. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),  pp.12912–12940. Cited by: [§5](https://arxiv.org/html/2602.16154v1#S5.SS0.SSS0.Px2.p1.1 "Multi-Model Training. ‣ 5 Related Work ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
277	*   R. West, A. Anderson, E. Kamar, and E. Horvitz (2025)Tandem training for language models. arXiv preprint arXiv:2510.13551. Cited by: [§5](https://arxiv.org/html/2602.16154v1#S5.SS0.SSS0.Px2.p1.1 "Multi-Model Training. ‣ 5 Related Work ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
278	*   H. Xiao, V. Patil, H. Lee, E. Stengel-Eskin, and M. Bansal (2025)Generalized correctness models: learning calibrated and model-agnostic correctness predictors from historical patterns. arXiv preprint arXiv:2509.24988. Cited by: [Appendix B](https://arxiv.org/html/2602.16154v1#A2.SS0.SSS0.Px4.p1.1 "Solvability estimation. ‣ Appendix B Additional Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
279	*   A. Yang, A. Li, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Gao, C. Huang, C. Lv, et al. (2025)Qwen3 technical report. arXiv preprint arXiv:2505.09388. Cited by: [§3.1](https://arxiv.org/html/2602.16154v1#S3.SS1.SSS0.Px1.p1.1 "Training data. ‣ 3.1 Experimental Setup ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"), [§3.1](https://arxiv.org/html/2602.16154v1#S3.SS1.SSS0.Px3.p1.3 "Implementation details. ‣ 3.1 Experimental Setup ‣ 3 Experiments and Results ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
280	*   H. Yuan, Z. Xu, Z. Tan, X. Yi, M. Guang, K. Long, H. Hui, B. Li, X. Chen, B. Zhao, et al. (2025)Marshal: incentivizing multi-agent reasoning via self-play with strategic llms. arXiv preprint arXiv:2510.15414. Cited by: [§5](https://arxiv.org/html/2602.16154v1#S5.SS0.SSS0.Px2.p1.1 "Multi-Model Training. ‣ 5 Related Work ‣ Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"). 
281	
282	Appendix A REMuL Details
283	------------------------
284	
285	#### Model Details.
286	
287	We experiment with Qwen3-14b (Apache-2.0 license), Phi-4-reasoning-plus (Apache-2.0 license), and Ministral 3 14B Reasoning (Apache-2.0 license). All models are given the same repetition penalty of 1.1 along with Top-p sampling parameter of 0.9. For the speaker models Qwen3-14b and Phi-4-reasoning-plus, we use a temperature of 0.7. For the listener models Qwen3-14b, Phi-4-reasoning-plus, and Ministral 3 14B Reasoning, we use temperatures of 1.1, 0.9, and 0.9 respectively. All other generation parameters are taken from the default HuggingFace generation configuration.
288	
289	#### Training details.
290	
291	We finetune our speaker models using the VERL library (Sheng et al., [2024](https://arxiv.org/html/2602.16154v1#bib.bib48 "HybridFlow: a flexible and efficient rlhf framework")) to configure GRPO and perform rollouts using vLLM (Kwon et al., [2023](https://arxiv.org/html/2602.16154v1#bib.bib49 "Efficient memory management for large language model serving with pagedattention")). We use learning rate of 1e-6 and train batch size of 64. For regularization, we use an entropy coefficient of 0.001 and a KL loss coefficient of 0.001 with low-variance KL loss. We generate 5 rollouts per prompt during training and train for 3 epochs. We use tensor parallelism with parallel size of 4 with GPU memory utilization set to 0.8. We additionally perform SFT using PEFT (Mangrulkar et al., [2022](https://arxiv.org/html/2602.16154v1#bib.bib50 "PEFT: state-of-the-art parameter-efficient fine-tuning methods")) with LoRA rank of 32, scaling factor of 128, and dropout of 0.05. We use learning rate of 1e-5 and train for 5 epochs with the AdamW optimizer (Loshchilov and Hutter, [2017](https://arxiv.org/html/2602.16154v1#bib.bib51 "Decoupled weight decay regularization")). All experiments are performed with a mix of A6000s, A100s, and H100s.
292	
293	#### Detection of backtracking.
294	
295	We take a subset of the tokens/phrases listed in Choi et al. ([2025](https://arxiv.org/html/2602.16154v1#bib.bib56 "Think clearly: improving reasoning via redundant token pruning")) as markers of reasoning segments that we use to flag backtracking in reasoning. The list of tokens is as follows: “Wait”, “Alternatively”, “Another angle”, “Another approach”, “But wait”, “Hold on”, “Hmm”, “Maybe”, “Let me double-check.”
296	
297	#### Detection of hints.
298	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "340229cd-adc3-4b04-9581-c240bd90557f",
  "isSidechain": true,
  "promptId": "8029e2e4-25c6-47cb-9539-6d3b0938c122",
  "agentId": "a7ed4918e81d4960b",
  "type": "user",
  "uuid": "b4a48cf5-0e65-40f7-9198-57026f263273",
  "sourceToolAssistantUUID": "340229cd-adc3-4b04-9581-c240bd90557f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-19T09:15:24.835Z_

I now have comprehensive information on all three papers. Here is the detailed report.

---

## Paper 1: REMUL -- "Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution"

**arXiv:** 2602.16154 (Feb 2026)
**Authors:** Nithin Sivakumaran, Shoubin Yu, Hyunji Lee, Yue Zhang, Ali Payani, Mohit Bansal, Elias Stengel-Eskin
**Venue:** ICML
**Code:** https://github.com/nsivaku/remul

### Method

REMUL (Reasoning Execution by Multiple Listeners) is a multi-party reinforcement learning framework. The core hypothesis is that *reasoning traces which other parties can follow will be more faithful*. The method works as follows:

1. A **speaker model** generates a reasoning trace, which is truncated at 25%, 50%, and 75% of its length.
2. These truncated prefixes are passed to a **pool of diverse listener models** (Ministral-3-14B-Reasoning, Phi-4-reasoning-plus 14B, and Qwen3-14B), who "soft execute" the trace by continuing it to an answer.
3. The speaker receives a **matching reward** based on how many listeners converge to the same answer as the speaker. This is optimized via Group Relative Policy Optimization (GRPO).
4. To counter the faithfulness-performance tradeoff, REMUL uses a **decoupled training strategy**: faithfulness is optimized via RL, while correctness is maintained via **masked supervised finetuning** (SFT with a LoRA adapter), where loss is computed only on final answer tokens, leaving the reasoning trace unaltered.

The key insight is that jointly optimizing correctness and faithfulness rewards via a single RL objective causes the rewards to conflict and cancel out. Decoupling them into separate training mechanisms resolves this.

### Models and Benchmarks

- **Speaker models trained:** Qwen3-14B and Phi4 (with thinking enabled)
- **Training data:** Subset of BIG-Bench Hard (5 tasks, 1250 QA pairs)
- **Evaluation benchmarks:** BIG-Bench Extra Hard (BBEH), MuSR (murder mysteries), ZebraLogicBench, FOLIO
- **Faithfulness metrics:** Hint attribution (from Chen et al. 2025), early answering AOC, mistake injection AOC (from Lanham et al. 2023)

### Key Results

- Hint attribution improved by up to **3.1% on Qwen3** and **2.7% on Phi4**, while accuracy improved by up to **2.1% and 3.2%** respectively.
- AOC for truncated CoT answering improved by an average of **0.033 points** over baseline.
- AOC for adding mistakes improved by an average of **0.030 points**.
- Faithfulness-only training achieved best faithfulness but lost ~3% accuracy; REMUL balanced both.
- Ablations showed that both **multiple listeners** and **diverse model types** are essential -- single-listener or same-model-type variants degraded performance.
- REMUL also improved **legibility** (rated by GPT-OSS-20B) and produced **shorter, more linear reasoning chains** with less backtracking.

### How REMUL Differs from FRIT, CST, and FaithRL

- **FRIT** (causal interventions + DPO) uses causal tracing to identify which reasoning steps causally influence the answer, then trains with DPO to prefer faithful traces. REMUL instead uses a *social/communicative* signal -- can other models follow the reasoning?
- **CST** (counterfactual simulation + RL) generates counterfactual reasoning traces to train models to distinguish faithful from unfaithful reasoning. REMUL uses *real execution by diverse listeners* rather than counterfactual generation.
- **FaithRL** (step-level process rewards) assigns process-level rewards to individual reasoning steps. REMUL rewards the *entire trace holistically* based on listener consensus, and uses a multi-party setup rather than a single reward model.
- REMUL's distinctive feature is the **multi-listener soft execution paradigm** -- faithfulness is defined as a multi-party property (can others follow your reasoning?) rather than a causal or process-level property. It also uniquely **decouples faithfulness and correctness training** into separate mechanisms.

### Relevance to Adversarial Faithfulness

REMUL is directly relevant as a 4th faithfulness training method to be tested under adversarial pressure. Key questions for your proposal: Does the "social" faithfulness signal (listener executability) produce more robust faithfulness than causal/process-level methods? Does the diversity of listener models provide adversarial robustness, or do adversarial attacks that fool one architecture also fool others? REMUL's finding that faithfulness and correctness rewards conflict is important -- adversarial pressure might exploit exactly this tension.

---

## Paper 2: "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning"

**arXiv:** 2602.11201 (Feb 2026)
**Authors:** Donald Ye, Max Loffgren, Om Kotadia, Linus Wong

### The "Reasoning Horizon" Phenomenon

The **reasoning horizon (k\*)** is a critical threshold at **70-85% of the chain length**, beyond which reasoning tokens have little or *negative* effect on the final answer. This was measured using a novel metric called **Normalized Logit Difference Decay (NLDD)**:

```
NLDD = (LD_clean - LD_corrupt) / |LD_clean| x 100
```

The metric works by **corrupting individual reasoning steps** (task-specific: depth errors for Dyck-nn, entity substitutions for PrOntoQA, arithmetic errors for GSM8K), truncating all subsequent steps, and measuring how much the model's confidence in its answer drops. A global calibration constant normalizes across architectures.

Interpretation:
- **Positive NLDD**: The reasoning step causally contributes to the answer (faithful).
- **Near-zero NLDD**: The step has no causal effect (post-hoc rationalization).
- **Negative NLDD**: Corrupting the step *increases* confidence (anti-faithful regime).

### Three Model Families Tested

1. **DeepSeek-Coder-6.7B-Instruct** -- optimized for code, testing whether rigid logical specialization enhances faithfulness
2. **Llama-3.1-8B-Instruct** -- general-purpose baseline
3. **Gemma-2-9B-Instruct** -- uses logit soft-capping, validating metric generalization

### Tasks
- **Dyck-nn** (syntactic bracket matching, 100 samples)
- **PrOntoQA** (multi-hop logical inference, 100 samples)
- **GSM8K** (multi-step arithmetic, 100 samples)

### Quantitative Results

| Model | Task | Accuracy | NLDD |
|-------|------|----------|------|
| Llama-3.1-8B | GSM8K | 100% | 96.7% |
| Llama-3.1-8B | PrOntoQA | 100% | 20.6% |
| DeepSeek-6.7B | PrOntoQA | 100% | 84.3% |
| Gemma-2-9B | PrOntoQA | 99% | **-52.5%** |
| Gemma-2-9B | Dyck-nn | 0% | 12.5% |

The most striking finding: **Gemma achieves 99% accuracy on PrOntoQA with an NLDD of -52.5%**, meaning its reasoning is *anti-faithful* -- corrupting the reasoning chain *increases* confidence. The model produces correct answers while completely ignoring its own CoT.

### The "Mapping Gap"

Models can **encode correct internal representations while completely failing the task**. Gemma's linear probes achieved 82% accuracy recovering stack-depth information from hidden states on Dyck-nn, but the model achieved 0% on the actual task. This demonstrates that task-relevant structure is encoded internally but not used for prediction.

### Relevance to Adversarial Faithfulness

This paper is highly relevant to your proposal in several ways:

1. **The reasoning horizon defines a vulnerability window**: Beyond k* (70-85%), additional tokens contribute "negligible or negative causal influence," creating attack surface without strengthening reasoning. Adversarial attacks could target this post-horizon region.
2. **Anti-faithful models are paradoxically harmed by extended reasoning**: In Gemma's PrOntoQA case, NLDD deteriorated from -22.9 to -120.2 beyond k*, meaning extended reasoning *interferes* with pre-computed answers.
3. **Accuracy alone masks causal disconnection**: A model can score 99% while having completely unfaithful reasoning, meaning adversarial pressure tests must go beyond accuracy metrics.
4. **Architecture-dependent vulnerability**: Different models show divergent faithfulness regimes on identical tasks, suggesting adversarial robustness strategies must be architecture-specific.
5. **NLDD provides a quantitative tool** for measuring whether faithfulness training actually produces causal dependence on reasoning, rather than just "looking faithful."

---

## Paper 3: "Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought"

**arXiv:** 2603.05488 (March 2026)
**Authors:** Siddharth Boppana, Annabel Ma, Max Loeffler, Raphael Sarfati, Eric Bigelow, Atticus Geiger, Owen Lewis, Jack Merullo
**Venue:** ICML
**Code:** github.com/AskSid/disentangling-computation-from-cot
**Visualization:** reasoning-theater.streamlit.app

### What They Found About Performative vs. Genuine Reasoning

The paper introduces the concept of **"performative reasoning"** -- when a model becomes internally confident in its final answer early in generation but continues producing tokens as if it is still reasoning. They use three complementary methods:

1. **Attention probes**: Lightweight classifiers trained on residual stream activations (using attention-weighted pooling across sequence positions) to predict the model's final answer from prefixes of varying length. Traditional linear probes fail because a single token's activation doesn't consistently encode the answer; attention probes succeed by pooling across the sequence.
2. **Forced answering**: Truncating the reasoning trace at intermediate points and prompting the model to give its final answer.
3. **CoT monitoring**: Using Gemini-2.5-Flash to evaluate whether the reasoning text contains an indicated answer.

### Models and Datasets

- **Primary models:** DeepSeek-R1-0528 (671B) and GPT-OSS (120B)
- **Additional models:** DeepSeek-R1 Qwen2.5 distills (1.5B, 7B, 14B, 32B) for model-size analysis
- **Datasets:** MMLU-Redux 2.0 (5280 questions, recall-based) and GPQA-Diamond (198 questions, graduate-level multihop reasoning)

### Key Findings

**Difficulty-dependent performativity:**
- On **MMLU** (easier, recall-based): Probes and forced answering predict the final answer with high accuracy from very early in the reasoning trace, while the CoT monitor cannot identify the answer until much later. The performativity rate for DeepSeek-R1 on MMLU was **0.417**, meaning a large gap between internal certainty and verbalized certainty.
- On **GPQA-Diamond** (harder, multihop): All three methods improve gradually together, with performativity rate of only **0.012** -- indicating genuine reasoning where CoT actually contributes to the answer.

**Inflection points track genuine reasoning:**
- Backtracking, "aha moments," and reconsiderations appear **twice as often** in responses where the probe shows the model is *not* internally confident (high confidence responses: 215/522 traces).
- This suggests inflection points are genuine markers of internal uncertainty, not performative behavior. However, the temporal relationship between inflection points and probe confidence shifts is inconsistent across models and datasets.

**Model size effects:**
- Larger models are more performative on MMLU: the 671B model's probe reaches high accuracy immediately, while smaller distilled models (1.5B-32B) require more reasoning steps to reach the answer.
- Smaller models exhibit more faithful CoT because the task is genuinely harder for them.

**Practical early exit results:**
- Probe-guided early exit at 95% confidence retains **97% accuracy on MMLU while saving 68% of tokens**.
- At 80% confidence on GPQA-Diamond, saves **50% of tokens** while retaining 97% performance.

**Gricean communication framing:**
The authors argue that reasoning models are "not cooperative speakers" in the Gricean sense. They satisfy Relation (relevance) and Quality (supported evidence) because these align with RL rewards, but violate Quantity (are excessively verbose) and Manner (don't surface early commitments). This explains why CoT monitors fail as "pragmatic listeners."

### Relevance to Adversarial Faithfulness

1. **Performative CoT is a fundamental challenge**: If models already know their answer but generate reasoning as "theater," then adversarial pressure on the reasoning trace may not actually change the model's answer -- or conversely, the model may produce *different* theater under adversarial pressure without changing its actual computation.
2. **Activation probing as an adversarial evaluation tool**: The probing methodology could be used to test whether faithfulness training methods actually change *internal* beliefs or just change the *surface CoT*. If a "faithful" model still shows large performativity gaps under probing, the training hasn't worked at the mechanistic level.
3. **Task difficulty modulates vulnerability**: Faithfulness training might only be needed (and only work) for harder tasks where genuine reasoning occurs. For easy tasks, the model will be performative regardless.
4. **The Gricean framing connects to REMUL**: REMUL's multi-listener approach essentially tries to make models more "cooperative speakers" -- the Reasoning Theater paper provides theoretical grounding for why this approach is needed and what obstacles it faces.
5. **Early exit as a safety tool**: If an adversary tries to smuggle unfaithful reasoning into later parts of the CoT (past the point where the model is already confident), probe-guided monitoring could detect this.

---

## Summary: How These Three Papers Fit Together for Your Proposal

These papers form a complementary picture relevant to testing faithfulness training under adversarial pressure:

- **REMUL** (Paper 1) provides a 4th faithfulness training method with a fundamentally different approach (social/communicative signal) compared to FRIT (causal), CST (counterfactual), and FaithRL (process rewards). It should be included as a condition in your experimental design.

- **Mechanistic Evidence for Faithfulness Decay** (Paper 2) provides the *mechanistic basis* for why faithfulness might fail under adversarial pressure: the reasoning horizon phenomenon shows that models already have a built-in "faithfulness decay" pattern where late reasoning steps are causally disconnected. Adversarial attacks could exploit this. The NLDD metric also provides a quantitative tool for measuring whether faithfulness training produces genuine causal dependence.

- **Reasoning Theater** (Paper 3) provides *empirical evidence* that models already engage in performative reasoning, and that the degree of performativity depends on task difficulty and model size. This constrains your experimental design: adversarial tests should include both easy tasks (where performativity is high and faithfulness training may have limited effect) and hard tasks (where genuine reasoning occurs and faithfulness training can actually bite).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4a48cf5-0e65-40f7-9198-57026f263273",
  "isSidechain": true,
  "agentId": "a7ed4918e81d4960b",
  "requestId": "req_011CbBfuiw3Pyehg9Sd3ctSH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2803dbf3-660d-4dca-b663-120ede499072",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "d3232602-cd70-49bb-a57b-21b3ab7347ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Puhi2FJuzgHtgpBoZh6RxL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14122,
      "cache_read_input_tokens": 57924,
      "output_tokens": 3814,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14122
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3814,
          "cache_read_input_tokens": 57924,
          "cache_creation_input_tokens": 14122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14122,
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
