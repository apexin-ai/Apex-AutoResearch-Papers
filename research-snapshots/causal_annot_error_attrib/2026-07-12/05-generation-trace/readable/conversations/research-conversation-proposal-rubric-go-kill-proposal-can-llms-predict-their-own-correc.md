# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Can LLMs Predict Their Own Correc

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-1/d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3.jsonl`
- **Structured JSON:** [`1f8190556922bb6aac72.json`](../../sessions/1f/1f8190556922bb6aac72.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:22:04.038Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:22:04.038Z",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction\n\n## Description\nWe investigate whether LLMs' internal representations can predict which of their errors are self-correctable, and whether this prediction enables selective correction that outperforms both ungated correction, the trivial 'Wait' baseline, and confidence-based routing. Prior work shows a faint correctability signal at the post-answer newline token (PANL) achieving only 0.614 AUROC with a single-layer linear probe — insufficient for reliable gating. We develop Enhanced Correctability Probes (ECP) that combine multi-layer ensemble stacking, multi-token features (PANL + last-answer-token + reasoning tokens), attention-entropy features, pre-Wait hidden-state features (informed by crosscoder analysis of Wait-token mechanisms, arXiv:2510.04128), and SAE-guided feature selection targeting the confounded feature intersection that bridges uncertainty and correctness (motivated by the functional dissociation finding of arXiv:2604.19974, where 68% of pure incorrectness features are causally inert). We begin with a Phase 0 pilot that directly tests whether multi-layer ensembling — which improved deception detection AUROC by up to 78% (arXiv:2604.13386, specifically on Harm-Pressure Knowledge in Llama-70B) — transfers to the fundamentally different task of correctability prediction. These probes gate a three-way decision: retain the original answer (likely correct), attempt correction including probe-selective Wait insertion (error detected, high correctability), or abstain (error detected, low correctability). This framework is distinguished from CoRefine's (arXiv:2602.08948) three-way routing — which uses output-level confidence, lacks genuine abstention, and is not correctability-aware — by using hidden-state probes, providing a genuine abstention option for unfixable errors, and explicitly predicting error fixability rather than confidence. Critically, we provide the first evaluation of the 'Wait' baseline on correct answers, measuring its previously-unknown overcorrection cost. We also conduct the first representational geometry and SAE feature decomposition analysis of correctability vs. correctness, testing whether correctability — a second-order property that depends not just on whether the model is wrong but on whether correction mechanisms can reach the right answer — shares the low-dimensional, linearly-separable structure that correctness exhibits (arXiv:2602.08159), requires higher dimensionality or non-linear boundaries, or depends disproportionately on the narrow confounded feature population identified by arXiv:2604.19974. This analysis, combined with error depth characterization (arXiv:2601.00828) and threshold analysis mapping probe quality to gating utility, ensures publishable contributions even if probe AUROC plateaus at marginal levels. We evaluate across Gemma-3-27B, Qwen-2.5-7B-Instruct, and Mistral-Small-3.2-24B on TriviaQA, MMLU, and GSM8K, comparing against eight baselines including ungated correction, Wait (universal and probe-selective), confidence-based routing (CoRefine-style and Reflective Confidence-style), PAG, and oracle gating. Our contributions are: (1) operationalizing correctability as a prediction target distinct from correctness, (2) the first pilot testing whether multi-layer ensembling transfers from deception to correctability, (3) the first hidden-state probe-based gating with genuine abstention for correctability-aware self-correction — distinguished from CoRefine's confidence-based routing by signal source, abstention capability, and correctability specificity, (4) the first representational geometry and SAE feature decomposition comparison of correctability vs. correctness, testing whether second-order properties have a different confounded-feature signature than first-order properties, and (5) establishing the conditions — including minimum probe quality thresholds — under which probe-gated correction outperforms simpler alternatives including confidence-based controllers.\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T03:22:04.047Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:22:04.047Z",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3"
}
```

---

## Round 1

59 recorded events

### User

_source line 3 · 2026-05-20T03:22:04.073Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction

## Description
We investigate whether LLMs' internal representations can predict which of their errors are self-correctable, and whether this prediction enables selective correction that outperforms both ungated correction, the trivial 'Wait' baseline, and confidence-based routing. Prior work shows a faint correctability signal at the post-answer newline token (PANL) achieving only 0.614 AUROC with a single-layer linear probe — insufficient for reliable gating. We develop Enhanced Correctability Probes (ECP) that combine multi-layer ensemble stacking, multi-token features (PANL + last-answer-token + reasoning tokens), attention-entropy features, pre-Wait hidden-state features (informed by crosscoder analysis of Wait-token mechanisms, arXiv:2510.04128), and SAE-guided feature selection targeting the confounded feature intersection that bridges uncertainty and correctness (motivated by the functional dissociation finding of arXiv:2604.19974, where 68% of pure incorrectness features are causally inert). We begin with a Phase 0 pilot that directly tests whether multi-layer ensembling — which improved deception detection AUROC by up to 78% (arXiv:2604.13386, specifically on Harm-Pressure Knowledge in Llama-70B) — transfers to the fundamentally different task of correctability prediction. These probes gate a three-way decision: retain the original answer (likely correct), attempt correction including probe-selective Wait insertion (error detected, high correctability), or abstain (error detected, low correctability). This framework is distinguished from CoRefine's (arXiv:2602.08948) three-way routing — which uses output-level confidence, lacks genuine abstention, and is not correctability-aware — by using hidden-state probes, providing a genuine abstention option for unfixable errors, and explicitly predicting error fixability rather than confidence. Critically, we provide the first evaluation of the 'Wait' baseline on correct answers, measuring its previously-unknown overcorrection cost. We also conduct the first representational geometry and SAE feature decomposition analysis of correctability vs. correctness, testing whether correctability — a second-order property that depends not just on whether the model is wrong but on whether correction mechanisms can reach the right answer — shares the low-dimensional, linearly-separable structure that correctness exhibits (arXiv:2602.08159), requires higher dimensionality or non-linear boundaries, or depends disproportionately on the narrow confounded feature population identified by arXiv:2604.19974. This analysis, combined with error depth characterization (arXiv:2601.00828) and threshold analysis mapping probe quality to gating utility, ensures publishable contributions even if probe AUROC plateaus at marginal levels. We evaluate across Gemma-3-27B, Qwen-2.5-7B-Instruct, and Mistral-Small-3.2-24B on TriviaQA, MMLU, and GSM8K, comparing against eight baselines including ungated correction, Wait (universal and probe-selective), confidence-based routing (CoRefine-style and Reflective Confidence-style), PAG, and oracle gating. Our contributions are: (1) operationalizing correctability as a prediction target distinct from correctness, (2) the first pilot testing whether multi-layer ensembling transfers from deception to correctability, (3) the first hidden-state probe-based gating with genuine abstention for correctability-aware self-correction — distinguished from CoRefine's confidence-based routing by signal source, abstention capability, and correctability specificity, (4) the first representational geometry and SAE feature decomposition comparison of correctability vs. correctness, testing whether second-order properties have a different confounded-feature signature than first-order properties, and (5) establishing the conditions — including minimum probe quality thresholds — under which probe-gated correction outperforms simpler alternatives including confidence-based controllers.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f4225287-4bc9-436c-8172-482fb17da145",
  "type": "user",
  "uuid": "44b5fdc4-1049-407b-90b4-e9222e4d47f2",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:22:04.072Z_

```json
{
  "parentUuid": "44b5fdc4-1049-407b-90b4-e9222e4d47f2",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "b554daff-3d79-4a37-ba15-5fb59866936f",
  "timestamp": "2026-05-20T03:22:04.072Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:22:04.072Z_

```json
{
  "parentUuid": "b554daff-3d79-4a37-ba15-5fb59866936f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "af52c6f7-8017-43ad-bb92-6acb49292c5b",
  "timestamp": "2026-05-20T03:22:04.072Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate correctability prediction proposal AUROC",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3"
}
```

---

### Assistant

_source line 7 · 2026-05-20T03:22:16.667Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for CoRL 2026. Let me first carefully read the proposal, then conduct web searches to understand the field landscape before making my assessment.

Wait - the user says CoRL 2026, but this proposal is about LLMs, self-correction, probing internal representations... This is clearly an NLP/ML paper, not a robotics paper. CoRL is Conference on Robot Learning. Let me re-read the system prompt - it says "CoRL 2026 主会" but the rubric mentions "NLP/CL 领域". This seems like the system prompt is a generic template and the actual target venue might be different. 

There's a clear mismatch between the stated venue (robotics) and the actual proposal content (NLP), so I'll evaluate the idea on its merits as a top-tier ML/AI contribution and note this discrepancy. Let me start with the necessary web searches to get context on recent work in LLM self-correction and probing techniques.

I need to look up the specific papers mentioned, understand the landscape around selective self-correction and internal representation analysis, and get familiar with emerging techniques like sparse autoencoders for interpreting LLM behavior.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af52c6f7-8017-43ad-bb92-6acb49292c5b",
  "isSidechain": false,
  "requestId": "req_011CbD6u9w5voEGr5caJ7RgT",
  "type": "assistant",
  "uuid": "8742797d-0fbf-4b4e-b9d0-92f044ce5cab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhCky6UQHdr2DmbcTv7E3N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 2346,
      "cache_read_input_tokens": 13985,
      "output_tokens": 556,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2346,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 556,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 2346,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2346
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

### Assistant

_source line 8 · 2026-05-20T03:22:16.669Z_

I need to conduct thorough field research before evaluating this proposal. Let me first load the WebSearch tool, then run multiple targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8742797d-0fbf-4b4e-b9d0-92f044ce5cab",
  "isSidechain": false,
  "requestId": "req_011CbD6u9w5voEGr5caJ7RgT",
  "type": "assistant",
  "uuid": "c8b15a53-8c8d-4b82-b729-9081ae3330dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhCky6UQHdr2DmbcTv7E3N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 2346,
      "cache_read_input_tokens": 13985,
      "output_tokens": 556,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2346,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 556,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 2346,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2346
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

_source line 9 · 2026-05-20T03:22:16.748Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018yBCRbzmJky6dxxZtSXkAp`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8b15a53-8c8d-4b82-b729-9081ae3330dd",
  "isSidechain": false,
  "requestId": "req_011CbD6u9w5voEGr5caJ7RgT",
  "type": "assistant",
  "uuid": "e9144d68-1a6b-4915-b4f6-45660ac7c509",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhCky6UQHdr2DmbcTv7E3N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 2346,
      "cache_read_input_tokens": 13985,
      "output_tokens": 556,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2346,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 556,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 2346,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2346
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

_source line 10 · 2026-05-20T03:22:16.755Z_

<details><summary>↩ Tool result · `toolu_018yBCRbzmJky6dxxZtSXkAp`</summary>

````text
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
  "parentUuid": "e9144d68-1a6b-4915-b4f6-45660ac7c509",
  "isSidechain": false,
  "promptId": "f4225287-4bc9-436c-8172-482fb17da145",
  "type": "user",
  "uuid": "5499dabe-d254-41c2-b50a-f5a9fd43cba9",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "e9144d68-1a6b-4915-b4f6-45660ac7c509",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-20T03:22:19.607Z_

Now let me run multiple targeted searches in parallel to understand the field landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5499dabe-d254-41c2-b50a-f5a9fd43cba9",
  "isSidechain": false,
  "requestId": "req_011CbD6v5v2C1NrVFPFVzJVS",
  "type": "assistant",
  "uuid": "a1165eee-5de4-4516-a7de-030ef29fd76f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2aQtcMrcAoQiPjvHhrjbE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1083,
      "cache_read_input_tokens": 16331,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1083,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 312,
          "cache_read_input_tokens": 16331,
          "cache_creation_input_tokens": 1083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1083
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

_source line 12 · 2026-05-20T03:22:20.024Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GiBQHwH4nPRwu2kWsyrPb7`</summary>

```json
{
  "query": "LLM self-correction selective gating probe internal representations 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1165eee-5de4-4516-a7de-030ef29fd76f",
  "isSidechain": false,
  "requestId": "req_011CbD6v5v2C1NrVFPFVzJVS",
  "type": "assistant",
  "uuid": "eaa8caef-7c3c-421a-9397-90f508d1af44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2aQtcMrcAoQiPjvHhrjbE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1083,
      "cache_read_input_tokens": 16331,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1083,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 312,
          "cache_read_input_tokens": 16331,
          "cache_creation_input_tokens": 1083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1083
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

_source line 13 · 2026-05-20T03:22:21.115Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H7x2LrfoejCL7DdxjMaFgk`</summary>

```json
{
  "query": "CoRefine arXiv 2602.08948 LLM self-correction routing confidence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eaa8caef-7c3c-421a-9397-90f508d1af44",
  "isSidechain": false,
  "requestId": "req_011CbD6v5v2C1NrVFPFVzJVS",
  "type": "assistant",
  "uuid": "1c8acb65-3338-4d5f-a9fa-f0224e78da0f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2aQtcMrcAoQiPjvHhrjbE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1083,
      "cache_read_input_tokens": 16331,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1083,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 312,
          "cache_read_input_tokens": 16331,
          "cache_creation_input_tokens": 1083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1083
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

_source line 14 · 2026-05-20T03:22:21.485Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PxgW4xe6pTHsFfXtNm91La`</summary>

```json
{
  "query": "arXiv 2604.19974 SAE correctness features LLM sparse autoencoder 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c8acb65-3338-4d5f-a9fa-f0224e78da0f",
  "isSidechain": false,
  "requestId": "req_011CbD6v5v2C1NrVFPFVzJVS",
  "type": "assistant",
  "uuid": "b6cc89d1-bdee-4322-ac5c-7663f7158081",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2aQtcMrcAoQiPjvHhrjbE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1083,
      "cache_read_input_tokens": 16331,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1083,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 312,
          "cache_read_input_tokens": 16331,
          "cache_creation_input_tokens": 1083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1083
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

_source line 15 · 2026-05-20T03:22:22.427Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UetyGM1FEfDruEK1fx8wdW`</summary>

```json
{
  "query": "arXiv 2604.13386 multi-layer ensemble probing deception detection LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6cc89d1-bdee-4322-ac5c-7663f7158081",
  "isSidechain": false,
  "requestId": "req_011CbD6v5v2C1NrVFPFVzJVS",
  "type": "assistant",
  "uuid": "fceec196-3f56-4f1d-8bc0-4d14e3aca094",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2aQtcMrcAoQiPjvHhrjbE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1083,
      "cache_read_input_tokens": 16331,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1083,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 312,
          "cache_read_input_tokens": 16331,
          "cache_creation_input_tokens": 1083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1083
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

_source line 16 · 2026-05-20T03:22:22.558Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018PBmf47s3TwD5mj49duA9b`</summary>

```json
{
  "query": "LLM correctability prediction probing hidden states self-correction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fceec196-3f56-4f1d-8bc0-4d14e3aca094",
  "isSidechain": false,
  "requestId": "req_011CbD6v5v2C1NrVFPFVzJVS",
  "type": "assistant",
  "uuid": "29bfb76a-7b34-48a0-92eb-edbf300d1f19",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2aQtcMrcAoQiPjvHhrjbE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1083,
      "cache_read_input_tokens": 16331,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1083,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 312,
          "cache_read_input_tokens": 16331,
          "cache_creation_input_tokens": 1083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1083
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

_source line 17 · 2026-05-20T03:22:28.201Z_

<details><summary>↩ Tool result · `toolu_01GiBQHwH4nPRwu2kWsyrPb7`</summary>

```text
Web search results for query: "LLM self-correction selective gating probe internal representations 2025 2026"

Links: [{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"},{"title":"Superscopes: Amplifying Internal Feature Representations for Language   Model Interpretation","url":"https://arxiv.org/pdf/2503.02078"},{"title":"Probing for Arithmetic Errors in Language Models","url":"https://arxiv.org/pdf/2507.12379"},{"title":"Internalized Self-Correction for Large Language Models","url":"https://arxiv.org/pdf/2412.16653"},{"title":"From Emergence to Control: Probing and Modulating Self-Reflection in Language Models","url":"https://arxiv.org/pdf/2506.12217"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/pdf/2512.20578"},{"title":"LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations","url":"https://arxiv.org/pdf/2602.09924"}]

Based on the search results, here are relevant research findings on LLM self-correction, probing internal representations, and related mechanistic interpretability topics from 2025-2026:

## Self-Correction and Internal Representations

Recent experiments across multiple datasets and models indicate that logit-based approaches often underperform compared to those that leverage internal model representations, with methods like INTRA exploiting interactions between internal representations achieving state-of-the-art performance.

## Probing Internal Representations

Patchscopes introduced a method for probing internal activations by patching them into new prompts, and Superscopes builds on this by systematically amplifying superposed features in MLP outputs and hidden states before patching them into new contexts. This approach amplifies weak but meaningful features, enabling interpretation of internal representations without requiring additional training.

## Selective Gating and Error Detection

Research demonstrates that probes can guide selective re-prompting of erroneous reasoning steps, with findings suggesting that arithmetic errors can be anticipated from internal activations alone, offering a path toward lightweight model self-correction.

## Self-Reflection Mechanisms

Self-reflection—the ability of an LLM to revisit, evaluate, and revise its own reasoning—has emerged as a behavior enabled by reinforcement learning, though its origin and underlying mechanisms remain poorly understood, with evidence showing self-reflection already emerges in pretrained models.

These recent works demonstrate growing interest in understanding and leveraging internal model mechanisms for improved self-correction and failure prediction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eaa8caef-7c3c-421a-9397-90f508d1af44",
  "isSidechain": false,
  "promptId": "f4225287-4bc9-436c-8172-482fb17da145",
  "type": "user",
  "uuid": "f4ed556c-179b-45d0-8d72-94fbddc59a6d",
  "toolUseResult": {
    "query": "LLM self-correction selective gating probe internal representations 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GMhCpL7Ey13G8UkcB2vbBp",
        "content": [
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs",
            "url": "https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"
          },
          {
            "title": "Superscopes: Amplifying Internal Feature Representations for Language   Model Interpretation",
            "url": "https://arxiv.org/pdf/2503.02078"
          },
          {
            "title": "Probing for Arithmetic Errors in Language Models",
            "url": "https://arxiv.org/pdf/2507.12379"
          },
          {
            "title": "Internalized Self-Correction for Large Language Models",
            "url": "https://arxiv.org/pdf/2412.16653"
          },
          {
            "title": "From Emergence to Control: Probing and Modulating Self-Reflection in Language Models",
            "url": "https://arxiv.org/pdf/2506.12217"
          },
          {
            "title": "Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/pdf/2512.20578"
          },
          {
            "title": "LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations",
            "url": "https://arxiv.org/pdf/2602.09924"
          }
        ]
      },
      "Based on the search results, here are relevant research findings on LLM self-correction, probing internal representations, and related mechanistic interpretability topics from 2025-2026:\n\n## Self-Correction and Internal Representations\n\nRecent experiments across multiple datasets and models indicate that logit-based approaches often underperform compared to those that leverage internal model representations, with methods like INTRA exploiting interactions between internal representations achieving state-of-the-art performance.\n\n## Probing Internal Representations\n\nPatchscopes introduced a method for probing internal activations by patching them into new prompts, and Superscopes builds on this by systematically amplifying superposed features in MLP outputs and hidden states before patching them into new contexts. This approach amplifies weak but meaningful features, enabling interpretation of internal representations without requiring additional training.\n\n## Selective Gating and Error Detection\n\nResearch demonstrates that probes can guide selective re-prompting of erroneous reasoning steps, with findings suggesting that arithmetic errors can be anticipated from internal activations alone, offering a path toward lightweight model self-correction.\n\n## Self-Reflection Mechanisms\n\nSelf-reflection—the ability of an LLM to revisit, evaluate, and revise its own reasoning—has emerged as a behavior enabled by reinforcement learning, though its origin and underlying mechanisms remain poorly understood, with evidence showing self-reflection already emerges in pretrained models.\n\nThese recent works demonstrate growing interest in understanding and leveraging internal model mechanisms for improved self-correction and failure prediction."
    ],
    "durationSeconds": 8.164587983999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "eaa8caef-7c3c-421a-9397-90f508d1af44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "f4ed556c-179b-45d0-8d72-94fbddc59a6d",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate correctability prediction proposal AUROC",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3"
}
```

---

### Tool result

_source line 20 · 2026-05-20T03:22:28.774Z_

<details><summary>↩ Tool result · `toolu_01H7x2LrfoejCL7DdxjMaFgk`</summary>

```text
Web search results for query: "CoRefine arXiv 2602.08948 LLM self-correction routing confidence"

Links: [{"title":"[2602.08948] CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute","url":"https://arxiv.org/abs/2602.08948"},{"title":"CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute","url":"https://arxiv.org/pdf/2602.08948"},{"title":"Learning to Route LLMs with Confidence Tokens","url":"https://arxiv.org/html/2410.13284v3"},{"title":"Learning to Route LLMs with Confidence Tokens","url":"https://arxiv.org/pdf/2410.13284"},{"title":"Confidence v.s. Critique: A Decomposition of Self-Correction Capability   for LLMs","url":"https://arxiv.org/pdf/2412.19513"}]

Based on the search results, here's what I found about CoRefine (arXiv 2602.08948):

## CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute

CoRefine is a confidence-guided self-refinement method that achieves competitive accuracy using a fraction of the tokens via a lightweight 211k-parameter Conv1D controller atop a frozen LLM.

### How It Works

The controller consumes full-trace confidence to decide whether to halt, re-examine, or try a different approach, enabling targeted self-correction with an average of 2.7 refinement steps per problem and roughly 190-fold token reduction relative to 512-sample baselines.

More specifically, the controller consumes full-trace confidence features of the LLM decoded reasoning chain and decides: HALT (accept current answer), RETHINK (verify reasoning), or ALTERNATIVE (explore new approach).

### Performance

The controller achieves 92.6 percent precision when it confidently halts, indicating that confidence dynamics reliably signal correctness. Additionally, token savings translate to actual latency reduction, with CoRefine saving up to 63% over parallel baselines.

The paper was submitted to arXiv on February 9, 2026, by Chen Jin and three other authors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c8acb65-3338-4d5f-a9fa-f0224e78da0f",
  "isSidechain": false,
  "promptId": "f4225287-4bc9-436c-8172-482fb17da145",
  "type": "user",
  "uuid": "63aa5e6a-2c92-4422-87fe-6df07478fd74",
  "toolUseResult": {
    "query": "CoRefine arXiv 2602.08948 LLM self-correction routing confidence",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HP7QH3BH4bU3CZx6rK49An",
        "content": [
          {
            "title": "[2602.08948] CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute",
            "url": "https://arxiv.org/abs/2602.08948"
          },
          {
            "title": "CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute",
            "url": "https://arxiv.org/pdf/2602.08948"
          },
          {
            "title": "Learning to Route LLMs with Confidence Tokens",
            "url": "https://arxiv.org/html/2410.13284v3"
          },
          {
            "title": "Learning to Route LLMs with Confidence Tokens",
            "url": "https://arxiv.org/pdf/2410.13284"
          },
          {
            "title": "Confidence v.s. Critique: A Decomposition of Self-Correction Capability   for LLMs",
            "url": "https://arxiv.org/pdf/2412.19513"
          }
        ]
      },
      "Based on the search results, here's what I found about CoRefine (arXiv 2602.08948):\n\n## CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute\n\nCoRefine is a confidence-guided self-refinement method that achieves competitive accuracy using a fraction of the tokens via a lightweight 211k-parameter Conv1D controller atop a frozen LLM.\n\n### How It Works\n\nThe controller consumes full-trace confidence to decide whether to halt, re-examine, or try a different approach, enabling targeted self-correction with an average of 2.7 refinement steps per problem and roughly 190-fold token reduction relative to 512-sample baselines.\n\nMore specifically, the controller consumes full-trace confidence features of the LLM decoded reasoning chain and decides: HALT (accept current answer), RETHINK (verify reasoning), or ALTERNATIVE (explore new approach).\n\n### Performance\n\nThe controller achieves 92.6 percent precision when it confidently halts, indicating that confidence dynamics reliably signal correctness. Additionally, token savings translate to actual latency reduction, with CoRefine saving up to 63% over parallel baselines.\n\nThe paper was submitted to arXiv on February 9, 2026, by Chen Jin and three other authors."
    ],
    "durationSeconds": 7.655329653000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1c8acb65-3338-4d5f-a9fa-f0224e78da0f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T03:22:29.073Z_

<details><summary>↩ Tool result · `toolu_01PxgW4xe6pTHsFfXtNm91La`</summary>

```text
Web search results for query: "arXiv 2604.19974 SAE correctness features LLM sparse autoencoder 2026"

Links: [{"title":"[2604.19974] Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders","url":"https://arxiv.org/abs/2604.19974"},{"title":"Sparse but Wrong: Incorrect L0 Leads to Incorrect Features in Sparse Autoencoders","url":"https://arxiv.org/pdf/2508.16560"},{"title":"Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders","url":"https://arxiv.org/html/2604.19974"},{"title":"Mechanistic Interpretability of Code Correctness in LLMs via Sparse Autoencoders","url":"https://arxiv.org/pdf/2510.02917"},{"title":"Sparse Autoencoder Features for Classifications and Transferability","url":"https://arxiv.org/pdf/2502.11367"},{"title":"AdaptiveK Sparse Autoencoders: Dynamic Sparsity Allocation for Interpretable LLM Representations","url":"https://arxiv.org/pdf/2508.17320"}]

Based on the search results, here's what I found about arXiv paper 2604.19974:

**Title:** "Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders"

**Authors and Submission:** Het Patel, Tiejin Chen, Hua Wei, Evangelos E. Papalexakis, and Jia Chen (submitted on 21 Apr 2026)

**Research Question:** The paper investigates whether large language models' output-level uncertainty and actual correctness are driven by the same internal mechanisms or by distinct feature populations.

**Methodology:** The authors introduce a 2x2 framework that partitions model predictions along correctness and confidence axes, and uses sparse autoencoders to identify features associated with each dimension independently.

**Key Findings:** Applying this to Llama-3.1-8B and Gemma-2-9B, they identify three feature populations that play fundamentally different functional roles. Specifically, pure uncertainty features are functionally essential—suppressing them severely degrades accuracy, while pure incorrectness features are functionally inert—despite showing statistically significant activation differences between correct and incorrect predictions, the majority produce near-zero change in accuracy when suppressed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6cc89d1-bdee-4322-ac5c-7663f7158081",
  "isSidechain": false,
  "promptId": "f4225287-4bc9-436c-8172-482fb17da145",
  "type": "user",
  "uuid": "96f0479d-7ed6-474b-a512-bc4fad106f43",
  "toolUseResult": {
    "query": "arXiv 2604.19974 SAE correctness features LLM sparse autoencoder 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_019p6c87De6hWmLQ228xsyoB",
        "content": [
          {
            "title": "[2604.19974] Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders",
            "url": "https://arxiv.org/abs/2604.19974"
          },
          {
            "title": "Sparse but Wrong: Incorrect L0 Leads to Incorrect Features in Sparse Autoencoders",
            "url": "https://arxiv.org/pdf/2508.16560"
          },
          {
            "title": "Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders",
            "url": "https://arxiv.org/html/2604.19974"
          },
          {
            "title": "Mechanistic Interpretability of Code Correctness in LLMs via Sparse Autoencoders",
            "url": "https://arxiv.org/pdf/2510.02917"
          },
          {
            "title": "Sparse Autoencoder Features for Classifications and Transferability",
            "url": "https://arxiv.org/pdf/2502.11367"
          },
          {
            "title": "AdaptiveK Sparse Autoencoders: Dynamic Sparsity Allocation for Interpretable LLM Representations",
            "url": "https://arxiv.org/pdf/2508.17320"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2604.19974:\n\n**Title:** \"Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders\"\n\n**Authors and Submission:** Het Patel, Tiejin Chen, Hua Wei, Evangelos E. Papalexakis, and Jia Chen (submitted on 21 Apr 2026)\n\n**Research Question:** The paper investigates whether large language models' output-level uncertainty and actual correctness are driven by the same internal mechanisms or by distinct feature populations.\n\n**Methodology:** The authors introduce a 2x2 framework that partitions model predictions along correctness and confidence axes, and uses sparse autoencoders to identify features associated with each dimension independently.\n\n**Key Findings:** Applying this to Llama-3.1-8B and Gemma-2-9B, they identify three feature populations that play fundamentally different functional roles. Specifically, pure uncertainty features are functionally essential—suppressing them severely degrades accuracy, while pure incorrectness features are functionally inert—despite showing statistically significant activation differences between correct and incorrect predictions, the majority produce near-zero change in accuracy when suppressed."
    ],
    "durationSeconds": 7.582557274999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b6cc89d1-bdee-4322-ac5c-7663f7158081",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T03:22:30.607Z_

<details><summary>↩ Tool result · `toolu_01UetyGM1FEfDruEK1fx8wdW`</summary>

```text
Web search results for query: "arXiv 2604.13386 multi-layer ensemble probing deception detection LLM 2026"

Links: [{"title":"Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling","url":"https://arxiv.org/html/2604.13386v1"},{"title":"[2604.13386] Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling","url":"https://arxiv.org/abs/2604.13386"},{"title":"Caught in the Act: a mechanistic approach to detecting deception","url":"https://arxiv.org/pdf/2508.19505"},{"title":"Caught in the Act: a mechanistic approach to detecting deception","url":"https://arxiv.org/html/2508.19505v2"},{"title":"Probing the Limits of the Lie Detector Approach to LLM Deception","url":"https://arxiv.org/html/2603.10003"},{"title":"DeceptGuard :A Constitutional Oversight Framework For Detecting Deception in LLM Agents","url":"https://arxiv.org/pdf/2603.13791"},{"title":"Detecting Multi-Agent Collusion Through Multi-Agent Interpretability","url":"https://arxiv.org/html/2604.01151v1"}]

I found the paper you're looking for. Here are the key details:

**Paper:** Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling (arXiv:2604.13386)

**Main Findings:**

Linear probes can detect when language models produce outputs they "know" are wrong, a capability relevant to both deception and reward hacking. However, single-layer probes are fragile: the best layer varies across models and tasks, and probes fail entirely on some deception types.

The paper's key contribution is that combining probes from multiple layers into an ensemble recovers strong performance even where single-layer probes fail, improving AUROC by +29% on Insider Trading and +78% on Harm-Pressure Knowledge.

**Scaling Results:** Across 12 models (0.5B–176B parameters), probe accuracy improves with scale: ~5% AUROC per 10× parameters (R=0.81).

**Geometric Explanation:** Deception directions rotate gradually across layers rather than appearing at one location, explaining both why single-layer probes are brittle and why multi-layer ensembles succeed.

The paper was published on April 15, 2026, with authors Erik Nordby, Tasha Pais, and Aviel Parrack.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fceec196-3f56-4f1d-8bc0-4d14e3aca094",
  "isSidechain": false,
  "promptId": "f4225287-4bc9-436c-8172-482fb17da145",
  "type": "user",
  "uuid": "2d8192d9-082f-4fdf-8635-f812db288b4b",
  "toolUseResult": {
    "query": "arXiv 2604.13386 multi-layer ensemble probing deception detection LLM 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CaqQ7ZX1UjLstZWhoD2ccT",
        "content": [
          {
            "title": "Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling",
            "url": "https://arxiv.org/html/2604.13386v1"
          },
          {
            "title": "[2604.13386] Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling",
            "url": "https://arxiv.org/abs/2604.13386"
          },
          {
            "title": "Caught in the Act: a mechanistic approach to detecting deception",
            "url": "https://arxiv.org/pdf/2508.19505"
          },
          {
            "title": "Caught in the Act: a mechanistic approach to detecting deception",
            "url": "https://arxiv.org/html/2508.19505v2"
          },
          {
            "title": "Probing the Limits of the Lie Detector Approach to LLM Deception",
            "url": "https://arxiv.org/html/2603.10003"
          },
          {
            "title": "DeceptGuard :A Constitutional Oversight Framework For Detecting Deception in LLM Agents",
            "url": "https://arxiv.org/pdf/2603.13791"
          },
          {
            "title": "Detecting Multi-Agent Collusion Through Multi-Agent Interpretability",
            "url": "https://arxiv.org/html/2604.01151v1"
          }
        ]
      },
      "I found the paper you're looking for. Here are the key details:\n\n**Paper:** Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling (arXiv:2604.13386)\n\n**Main Findings:**\n\nLinear probes can detect when language models produce outputs they \"know\" are wrong, a capability relevant to both deception and reward hacking. However, single-layer probes are fragile: the best layer varies across models and tasks, and probes fail entirely on some deception types.\n\nThe paper's key contribution is that combining probes from multiple layers into an ensemble recovers strong performance even where single-layer probes fail, improving AUROC by +29% on Insider Trading and +78% on Harm-Pressure Knowledge.\n\n**Scaling Results:** Across 12 models (0.5B–176B parameters), probe accuracy improves with scale: ~5% AUROC per 10× parameters (R=0.81).\n\n**Geometric Explanation:** Deception directions rotate gradually across layers rather than appearing at one location, explaining both why single-layer probes are brittle and why multi-layer ensembles succeed.\n\nThe paper was published on April 15, 2026, with authors Erik Nordby, Tasha Pais, and Aviel Parrack."
    ],
    "durationSeconds": 8.177312254,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fceec196-3f56-4f1d-8bc0-4d14e3aca094",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T03:22:31.051Z_

<details><summary>↩ Tool result · `toolu_018PBmf47s3TwD5mj49duA9b`</summary>

```text
Web search results for query: "LLM correctability prediction probing hidden states self-correction 2025 2026"

Links: [{"title":"Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/html/2504.05419v1"},{"title":"[2512.20578] Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/abs/2512.20578"},{"title":"Latent Space Chain-of-Embedding Enables Output-free LLM Self-Evaluation","url":"https://arxiv.org/pdf/2410.13640"},{"title":"Predicting LLM Answer Accuracy from Question-Only ...","url":"https://arxiv.org/pdf/2509.10625"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018.full.pdf"},{"title":"Temporal Predictors of Outcome in Reasoning Language Models","url":"https://arxiv.org/pdf/2511.14773"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"},{"title":"Published as a conference paper at COLM 2025","url":"https://arxiv.org/pdf/2503.15299"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/pdf/2512.20578"}]

Based on the web search results, here's what I found on this research topic:

## Recent Research on LLM Correctability Prediction

There has been significant recent work on predicting LLM correctness by probing hidden states:

**Key Findings:**

An LLM's representation after processing a statement is highly predictive of the statement's correctness, and linear probes trained on these representations can classify correctness even without ground-truth labels.

Research has shown the ability to predict answer correctness directly from an LLM's hidden state while the chain-of-thought is being generated, using a fixed, auditable recipe. Notably, hidden states from very short prefixes already contain linearly decodable information about eventual correctness, reaching AUCs up to 0.8+ on MATH-like data.

**Recent 2025-2026 Developments:**

Gnosis is a lightweight self-awareness mechanism that enables frozen LLMs to perform intrinsic self-verification by decoding signals from hidden states and attention patterns. It learns to compress hidden states and attention maps from a frozen LLM into descriptors and predicts a scalar correctness score with only ~5 million extra parameters and essentially zero added inference cost.

Additionally, PING (Probing INternal states of Generative models) is a framework to leverage internal states for improved predictions directly at inference time, turning latent signals into calibrated, deployable predictions.

These approaches represent a shift toward more efficient, on-policy verification methods that leverage the model's internal representations for self-correction capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29bfb76a-7b34-48a0-92eb-edbf300d1f19",
  "isSidechain": false,
  "promptId": "f4225287-4bc9-436c-8172-482fb17da145",
  "type": "user",
  "uuid": "2db3ff04-df41-4a33-a670-bb193fd227a9",
  "toolUseResult": {
    "query": "LLM correctability prediction probing hidden states self-correction 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Vfm9PcQi1fePpA51tUf7P3",
        "content": [
          {
            "title": "Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification",
            "url": "https://arxiv.org/html/2504.05419v1"
          },
          {
            "title": "[2512.20578] Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/abs/2512.20578"
          },
          {
            "title": "Latent Space Chain-of-Embedding Enables Output-free LLM Self-Evaluation",
            "url": "https://arxiv.org/pdf/2410.13640"
          },
          {
            "title": "Predicting LLM Answer Accuracy from Question-Only ...",
            "url": "https://arxiv.org/pdf/2509.10625"
          },
          {
            "title": "Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs",
            "url": "https://www.medrxiv.org/content/10.1101/2025.09.17.25336018.full.pdf"
          },
          {
            "title": "Temporal Predictors of Outcome in Reasoning Language Models",
            "url": "https://arxiv.org/pdf/2511.14773"
          },
          {
            "title": "Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs",
            "url": "https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"
          },
          {
            "title": "Published as a conference paper at COLM 2025",
            "url": "https://arxiv.org/pdf/2503.15299"
          },
          {
            "title": "Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/pdf/2512.20578"
          }
        ]
      },
      "Based on the web search results, here's what I found on this research topic:\n\n## Recent Research on LLM Correctability Prediction\n\nThere has been significant recent work on predicting LLM correctness by probing hidden states:\n\n**Key Findings:**\n\nAn LLM's representation after processing a statement is highly predictive of the statement's correctness, and linear probes trained on these representations can classify correctness even without ground-truth labels.\n\nResearch has shown the ability to predict answer correctness directly from an LLM's hidden state while the chain-of-thought is being generated, using a fixed, auditable recipe. Notably, hidden states from very short prefixes already contain linearly decodable information about eventual correctness, reaching AUCs up to 0.8+ on MATH-like data.\n\n**Recent 2025-2026 Developments:**\n\nGnosis is a lightweight self-awareness mechanism that enables frozen LLMs to perform intrinsic self-verification by decoding signals from hidden states and attention patterns. It learns to compress hidden states and attention maps from a frozen LLM into descriptors and predicts a scalar correctness score with only ~5 million extra parameters and essentially zero added inference cost.\n\nAdditionally, PING (Probing INternal states of Generative models) is a framework to leverage internal states for improved predictions directly at inference time, turning latent signals into calibrated, deployable predictions.\n\nThese approaches represent a shift toward more efficient, on-policy verification methods that leverage the model's internal representations for self-correction capabilities."
    ],
    "durationSeconds": 8.486265554999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "29bfb76a-7b34-48a0-92eb-edbf300d1f19",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-20T03:22:34.566Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have initial results. Let me now search for more specific papers mentioned in the proposal and additional related work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2db3ff04-df41-4a33-a670-bb193fd227a9",
  "isSidechain": false,
  "requestId": "req_011CbD6w96Hg3pK4uxaLBj59",
  "type": "assistant",
  "uuid": "95f125f6-de02-4b17-9cd8-44012e25a866",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6QHvySLjdDuzoWQTvYRU6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3762,
      "cache_read_input_tokens": 17414,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3762,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 303,
          "cache_read_input_tokens": 17414,
          "cache_creation_input_tokens": 3762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3762
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

### Assistant

_source line 25 · 2026-05-20T03:22:34.982Z_

Let me do a few more targeted searches for the remaining cited papers and closely related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95f125f6-de02-4b17-9cd8-44012e25a866",
  "isSidechain": false,
  "requestId": "req_011CbD6w96Hg3pK4uxaLBj59",
  "type": "assistant",
  "uuid": "8b15fac6-ee78-4cb8-8e6d-5f3caa135e6a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6QHvySLjdDuzoWQTvYRU6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3762,
      "cache_read_input_tokens": 17414,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3762,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 303,
          "cache_read_input_tokens": 17414,
          "cache_creation_input_tokens": 3762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3762
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

_source line 26 · 2026-05-20T03:22:35.387Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PovUYVHumCBR2vZnU77YQE`</summary>

```json
{
  "query": "arXiv 2602.08159 correctness linear probes LLM representational geometry 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b15fac6-ee78-4cb8-8e6d-5f3caa135e6a",
  "isSidechain": false,
  "requestId": "req_011CbD6w96Hg3pK4uxaLBj59",
  "type": "assistant",
  "uuid": "03565e41-90cd-4115-81fd-0e31e816a2b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6QHvySLjdDuzoWQTvYRU6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3762,
      "cache_read_input_tokens": 17414,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3762,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 303,
          "cache_read_input_tokens": 17414,
          "cache_creation_input_tokens": 3762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3762
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

_source line 27 · 2026-05-20T03:22:36.463Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Tv2pWjW74FusWwqs1GdXF9`</summary>

```json
{
  "query": "arXiv 2510.04128 Wait token crosscoder mechanism LLM reasoning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03565e41-90cd-4115-81fd-0e31e816a2b3",
  "isSidechain": false,
  "requestId": "req_011CbD6w96Hg3pK4uxaLBj59",
  "type": "assistant",
  "uuid": "01ab105c-8699-463a-9d80-63ec818d12fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6QHvySLjdDuzoWQTvYRU6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3762,
      "cache_read_input_tokens": 17414,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3762,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 303,
          "cache_read_input_tokens": 17414,
          "cache_creation_input_tokens": 3762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3762
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

_source line 28 · 2026-05-20T03:22:37.348Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XqY1Yw4Wh84TppcWobXYPe`</summary>

```json
{
  "query": "\"Wait\" baseline LLM self-correction budget forcing test-time compute 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01ab105c-8699-463a-9d80-63ec818d12fd",
  "isSidechain": false,
  "requestId": "req_011CbD6w96Hg3pK4uxaLBj59",
  "type": "assistant",
  "uuid": "aba94c8e-f17a-4cf1-be12-b75031b84d2c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6QHvySLjdDuzoWQTvYRU6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3762,
      "cache_read_input_tokens": 17414,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3762,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 303,
          "cache_read_input_tokens": 17414,
          "cache_creation_input_tokens": 3762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3762
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

_source line 29 · 2026-05-20T03:22:37.797Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019RrftKiNck7wHKs87YmxBq`</summary>

```json
{
  "query": "arXiv 2601.00828 error depth characterization LLM self-correction 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aba94c8e-f17a-4cf1-be12-b75031b84d2c",
  "isSidechain": false,
  "requestId": "req_011CbD6w96Hg3pK4uxaLBj59",
  "type": "assistant",
  "uuid": "4ed8fe85-4895-433e-999a-744f2bf6c5ad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6QHvySLjdDuzoWQTvYRU6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3762,
      "cache_read_input_tokens": 17414,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3762,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 303,
          "cache_read_input_tokens": 17414,
          "cache_creation_input_tokens": 3762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3762
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

_source line 30 · 2026-05-20T03:22:42.517Z_

<details><summary>↩ Tool result · `toolu_01PovUYVHumCBR2vZnU77YQE`</summary>

```text
Web search results for query: "arXiv 2602.08159 correctness linear probes LLM representational geometry 2026"

Links: [{"title":"The Geometry of Truth: Emergent Linear Structure in Large Language Model   Representations of True/False Datasets","url":"https://arxiv.org/pdf/2310.06824"},{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/pdf/2602.08159"},{"title":"No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes","url":"https://arxiv.org/html/2509.10625.pdf"},{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/html/2602.08159v1"},{"title":"The Geometry of Truth: Emergent Linear Structure in LLM Representations of True/False Datasets","url":"https://arxiv.org/html/2310.06824v3"},{"title":"LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals","url":"https://arxiv.org/pdf/2604.05655"}]

Perfect! I found the paper you're looking for. Here's information about arXiv 2602.08159:

## "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models"

This paper characterizes the geometry of correctness representations in transformer activations across 9 models from 5 architecture families, finding that the discriminative signal occupies 3–8 dimensions, performance decreases with additional dimensions, and no nonlinear classifier improves over linear probes.

**Key Findings:**

1. **Linear Structure Dominance**: The optimal decision boundary is a hyperplane; complex boundaries model structure that does not exist.

2. **Internal vs Output Gap**: Internal probes achieve 0.80-0.97 AUC while output-based methods achieve only 0.44–0.64 AUC, indicating the correctness signal exists internally but is not expressed in outputs.

3. **Causal Validation**: The learned direction produces 10.9 percentage point changes in error rates through activation steering while random directions show no effect.

4. **Geometric Properties**: Centroid distance matches probe performance, indicating class separation is a mean shift, making detection geometric rather than learned.

The paper advances our understanding of how language models represent correctness internally by revealing the low-dimensional, linearly-separable structure of this phenomenon.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03565e41-90cd-4115-81fd-0e31e816a2b3",
  "isSidechain": false,
  "promptId": "f4225287-4bc9-436c-8172-482fb17da145",
  "type": "user",
  "uuid": "9ef5da2e-c5c0-4e33-8e98-253246addb13",
  "toolUseResult": {
    "query": "arXiv 2602.08159 correctness linear probes LLM representational geometry 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MYvLsqUWVCCLYVePAGEMeo",
        "content": [
          {
            "title": "The Geometry of Truth: Emergent Linear Structure in Large Language Model   Representations of True/False Datasets",
            "url": "https://arxiv.org/pdf/2310.06824"
          },
          {
            "title": "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models",
            "url": "https://arxiv.org/pdf/2602.08159"
          },
          {
            "title": "No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes",
            "url": "https://arxiv.org/html/2509.10625.pdf"
          },
          {
            "title": "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models",
            "url": "https://arxiv.org/html/2602.08159v1"
          },
          {
            "title": "The Geometry of Truth: Emergent Linear Structure in LLM Representations of True/False Datasets",
            "url": "https://arxiv.org/html/2310.06824v3"
          },
          {
            "title": "LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals",
            "url": "https://arxiv.org/pdf/2604.05655"
          }
        ]
      },
      "Perfect! I found the paper you're looking for. Here's information about arXiv 2602.08159:\n\n## \"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models\"\n\nThis paper characterizes the geometry of correctness representations in transformer activations across 9 models from 5 architecture families, finding that the discriminative signal occupies 3–8 dimensions, performance decreases with additional dimensions, and no nonlinear classifier improves over linear probes.\n\n**Key Findings:**\n\n1. **Linear Structure Dominance**: The optimal decision boundary is a hyperplane; complex boundaries model structure that does not exist.\n\n2. **Internal vs Output Gap**: Internal probes achieve 0.80-0.97 AUC while output-based methods achieve only 0.44–0.64 AUC, indicating the correctness signal exists internally but is not expressed in outputs.\n\n3. **Causal Validation**: The learned direction produces 10.9 percentage point changes in error rates through activation steering while random directions show no effect.\n\n4. **Geometric Properties**: Centroid distance matches probe performance, indicating class separation is a mean shift, making detection geometric rather than learned.\n\nThe paper advances our understanding of how language models represent correctness internally by revealing the low-dimensional, linearly-separable structure of this phenomenon."
    ],
    "durationSeconds": 7.124068085999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "03565e41-90cd-4115-81fd-0e31e816a2b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "9ef5da2e-c5c0-4e33-8e98-253246addb13",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate correctability prediction proposal AUROC",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3"
}
```

---

### Tool result

_source line 33 · 2026-05-20T03:22:43.451Z_

<details><summary>↩ Tool result · `toolu_01Tv2pWjW74FusWwqs1GdXF9`</summary>

```text
Web search results for query: "arXiv 2510.04128 Wait token crosscoder mechanism LLM reasoning 2025"

Links: [{"title":"[2510.04128] Internal states before wait modulate reasoning patterns","url":"https://arxiv.org/abs/2510.04128"},{"title":"Understanding Reasoning in LLMs through Strategic Information Allocation under Uncertainty","url":"https://arxiv.org/pdf/2603.15500"},{"title":"Internal states before wait modulate reasoning patterns","url":"https://arxiv.org/pdf/2510.04128"},{"title":"Internal states before wait modulate reasoning patterns","url":"https://arxiv.org/html/2510.04128"},{"title":"Extending Token Computation for LLM Reasoning","url":"https://arxiv.org/pdf/2403.14932"},{"title":"Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning","url":"https://arxiv.org/pdf/2506.02867"}]

Based on the search results, here's what I found about arXiv paper 2510.04128:

## Paper Overview

The paper is titled "Internal states before wait modulate reasoning patterns", published on October 5, 2025.

## Main Research Focus

The paper identifies the "wait" token as a distinctive marker in reasoning traces that often signals reasoning behavior such as backtracking. The research addresses whether model latents preceding wait tokens contain relevant information for modulating the subsequent reasoning process.

## Methodology

The researchers trained crosscoders at multiple layers of DeepSeek-R1-Distill-Llama-8B and its base version, and introduced a latent attribution technique in the crosscoder setting.

## Key Findings

The study located a small set of features relevant for promoting/suppressing wait tokens' probabilities, and through experiments analyzing max-activating examples and causal interventions, showed that many identified features are relevant for the reasoning process and give rise to different types of reasoning patterns such as restarting from the beginning, recalling prior knowledge, expressing uncertainty, and double-checking.

The paper contributes to understanding the internal mechanisms of reasoning models by analyzing what information in the model's hidden states influences whether the model chooses to use the "wait" token and subsequent reasoning behaviors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01ab105c-8699-463a-9d80-63ec818d12fd",
  "isSidechain": false,
  "promptId": "f4225287-4bc9-436c-8172-482fb17da145",
  "type": "user",
  "uuid": "30ab045e-cf5a-408f-82d9-3ec2bc46b639",
  "toolUseResult": {
    "query": "arXiv 2510.04128 Wait token crosscoder mechanism LLM reasoning 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TbCDE5VoAbp7uPWgRnHjXj",
        "content": [
          {
            "title": "[2510.04128] Internal states before wait modulate reasoning patterns",
            "url": "https://arxiv.org/abs/2510.04128"
          },
          {
            "title": "Understanding Reasoning in LLMs through Strategic Information Allocation under Uncertainty",
            "url": "https://arxiv.org/pdf/2603.15500"
          },
          {
            "title": "Internal states before wait modulate reasoning patterns",
            "url": "https://arxiv.org/pdf/2510.04128"
          },
          {
            "title": "Internal states before wait modulate reasoning patterns",
            "url": "https://arxiv.org/html/2510.04128"
          },
          {
            "title": "Extending Token Computation for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2403.14932"
          },
          {
            "title": "Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning",
            "url": "https://arxiv.org/pdf/2506.02867"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2510.04128:\n\n## Paper Overview\n\nThe paper is titled \"Internal states before wait modulate reasoning patterns\", published on October 5, 2025.\n\n## Main Research Focus\n\nThe paper identifies the \"wait\" token as a distinctive marker in reasoning traces that often signals reasoning behavior such as backtracking. The research addresses whether model latents preceding wait tokens contain relevant information for modulating the subsequent reasoning process.\n\n## Methodology\n\nThe researchers trained crosscoders at multiple layers of DeepSeek-R1-Distill-Llama-8B and its base version, and introduced a latent attribution technique in the crosscoder setting.\n\n## Key Findings\n\nThe study located a small set of features relevant for promoting/suppressing wait tokens' probabilities, and through experiments analyzing max-activating examples and causal interventions, showed that many identified features are relevant for the reasoning process and give rise to different types of reasoning patterns such as restarting from the beginning, recalling prior knowledge, expressing uncertainty, and double-checking.\n\nThe paper contributes to understanding the internal mechanisms of reasoning models by analyzing what information in the model's hidden states influences whether the model chooses to use the \"wait\" token and subsequent reasoning behaviors."
    ],
    "durationSeconds": 6.984144198000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "01ab105c-8699-463a-9d80-63ec818d12fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T03:22:43.610Z_

<details><summary>↩ Tool result · `toolu_01XqY1Yw4Wh84TppcWobXYPe`</summary>

```text
Web search results for query: ""Wait" baseline LLM self-correction budget forcing test-time compute 2025 2026"

Links: [{"title":"The State of LLM Reasoning Model Inference","url":"https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling"},{"title":"Boosting Accuracy and Efficiency of Budget Forcing in LLMs via Reinforcement Learning for Mathematical Reasoning","url":"https://arxiv.org/html/2510.21398v1"},{"title":"Test‑Time Self‑Training to Boost LLM Reasoning - Newline.co","url":"https://www.newline.co/@Dipen/testtime-selftraining-to-boost-llm-reasoning--09e52239"},{"title":"SETS: Leveraging Self-Verification and Self-Correction for Improved Test-Time Scaling","url":"https://arxiv.org/pdf/2501.19306"},{"title":"Boosting Accuracy and Efficiency of Budget Forcing in ...","url":"https://fse.studenttheses.ub.rug.nl/36698/1/bAI2025TarunokusumoRA.pdf"},{"title":"Boosting Accuracy and Efficiency of Budget Forcing in LLMs via Reinforcement Learning for Mathematical Reasoning","url":"https://arxiv.org/pdf/2510.21398"},{"title":"Spend Less, Reason Better: Budget-Aware Value Tree Search for LLM Agents","url":"https://arxiv.org/pdf/2603.12634"}]

Based on the search results, here's what I found about "Wait" tokens, baseline LLM self-correction, budget forcing, and test-time compute:

## Key Findings

**"Wait" Token Mechanism:**
Budget forcing compels additional reasoning steps by injecting a special token—often "Wait"—to allow the model to self-correct and self-verify its answers. The appended "Wait" token prompted the model to revise its reasoning and correct itself.

**Budget Forcing Overview:**
Budget forcing is a decoding intervention strategy which allocates extra compute budget for thinking and elicits the inherent self-correcting behavior of the model. Budget forcing explicitly controls the number of "thinking tokens" generated by the model during inference.

**Test-Time Compute Trends:**
The trend of adding reasoning capabilities whether via inference-time or train-time compute scaling is a major step forward for LLMs in 2025.

**Challenges with Budget Forcing:**
Budget forcing with SFT alone often performs suboptimally and even degrades accuracy compared to its base model for smaller LLMs, and increasing the token budget often causes models to "overthink", increasing computational overhead.

These findings come from recent 2025-2026 research on test-time scaling and reasoning enhancements for language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aba94c8e-f17a-4cf1-be12-b75031b84d2c",
  "isSidechain": false,
  "promptId": "f4225287-4bc9-436c-8172-482fb17da145",
  "type": "user",
  "uuid": "e304c80a-4678-43c5-a688-5755950408d9",
  "toolUseResult": {
    "query": "\"Wait\" baseline LLM self-correction budget forcing test-time compute 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AJZGmaVR1j2bo2SxkKvwSv",
        "content": [
          {
            "title": "The State of LLM Reasoning Model Inference",
            "url": "https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling"
          },
          {
            "title": "Boosting Accuracy and Efficiency of Budget Forcing in LLMs via Reinforcement Learning for Mathematical Reasoning",
            "url": "https://arxiv.org/html/2510.21398v1"
          },
          {
            "title": "Test‑Time Self‑Training to Boost LLM Reasoning - Newline.co",
            "url": "https://www.newline.co/@Dipen/testtime-selftraining-to-boost-llm-reasoning--09e52239"
          },
          {
            "title": "SETS: Leveraging Self-Verification and Self-Correction for Improved Test-Time Scaling",
            "url": "https://arxiv.org/pdf/2501.19306"
          },
          {
            "title": "Boosting Accuracy and Efficiency of Budget Forcing in ...",
            "url": "https://fse.studenttheses.ub.rug.nl/36698/1/bAI2025TarunokusumoRA.pdf"
          },
          {
            "title": "Boosting Accuracy and Efficiency of Budget Forcing in LLMs via Reinforcement Learning for Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2510.21398"
          },
          {
            "title": "Spend Less, Reason Better: Budget-Aware Value Tree Search for LLM Agents",
            "url": "https://arxiv.org/pdf/2603.12634"
          }
        ]
      },
      "Based on the search results, here's what I found about \"Wait\" tokens, baseline LLM self-correction, budget forcing, and test-time compute:\n\n## Key Findings\n\n**\"Wait\" Token Mechanism:**\nBudget forcing compels additional reasoning steps by injecting a special token—often \"Wait\"—to allow the model to self-correct and self-verify its answers. The appended \"Wait\" token prompted the model to revise its reasoning and correct itself.\n\n**Budget Forcing Overview:**\nBudget forcing is a decoding intervention strategy which allocates extra compute budget for thinking and elicits the inherent self-correcting behavior of the model. Budget forcing explicitly controls the number of \"thinking tokens\" generated by the model during inference.\n\n**Test-Time Compute Trends:**\nThe trend of adding reasoning capabilities whether via inference-time or train-time compute scaling is a major step forward for LLMs in 2025.\n\n**Challenges with Budget Forcing:**\nBudget forcing with SFT alone often performs suboptimally and even degrades accuracy compared to its base model for smaller LLMs, and increasing the token budget often causes models to \"overthink\", increasing computational overhead.\n\nThese findings come from recent 2025-2026 research on test-time scaling and reasoning enhancements for language models."
    ],
    "durationSeconds": 6.258528257999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "aba94c8e-f17a-4cf1-be12-b75031b84d2c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-20T03:22:44.757Z_

<details><summary>↩ Tool result · `toolu_019RrftKiNck7wHKs87YmxBq`</summary>

```text
Web search results for query: "arXiv 2601.00828 error depth characterization LLM self-correction 2026"

Links: [{"title":"[2601.00828] Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis","url":"https://arxiv.org/abs/2601.00828"},{"title":"Decomposing LLM Self-Correction:","url":"https://arxiv.org/pdf/2601.00828"},{"title":"Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis","url":"https://arxiv.org/html/2601.00828"},{"title":"Self-Correction Makes LLMs Better Parsers","url":"https://arxiv.org/html/2504.14165v1"},{"title":"Self-Correction Bench: Revealing and Addressing the Self-Correction Blind Spot in LLMs","url":"https://arxiv.org/html/2507.02778v1"},{"title":"Self-Correction Makes LLMs Better Parsers","url":"https://arxiv.org/pdf/2504.14165"},{"title":"Self-Correction Bench: Uncovering and Addressing the Self-Correction Blind Spot in Large Language Models","url":"https://arxiv.org/pdf/2507.02778"}]

I found the paper! Here's what the search results reveal about arXiv 2601.00828:

## Paper Overview

The paper is titled "Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis" and was submitted on December 24, 2025.

## Key Findings

The work systematically decomposes self-correction into three distinct sub-capabilities: error detection, error localization, and error correction.

Through cross-model experiments on GSM8K-Complex with three major LLMs, the authors uncover an Accuracy-Correction Paradox: weaker models (GPT-3.5, 66% accuracy) achieve 1.6x higher intrinsic correction rates than stronger models (DeepSeek, 94% accuracy)—26.8% vs 16.7%.

## The Error Depth Hypothesis

The paper proposes the Error Depth Hypothesis: stronger models make fewer but deeper errors that resist self-correction.

## Notable Observations

Claude detects 10% of errors but corrects 29%; GPT-3.5 detects 82% but corrects 27%, suggesting that error detection capability does not necessarily predict correction success.

The paper appears to be a significant contribution to understanding the limitations of LLM self-correction across models of varying capability levels.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ed8fe85-4895-433e-999a-744f2bf6c5ad",
  "isSidechain": false,
  "promptId": "f4225287-4bc9-436c-8172-482fb17da145",
  "type": "user",
  "uuid": "4bdb3fc5-8c34-4b19-9d0c-8152834bbc3b",
  "toolUseResult": {
    "query": "arXiv 2601.00828 error depth characterization LLM self-correction 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RwZyCezunEZtAstLuEDsXK",
        "content": [
          {
            "title": "[2601.00828] Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis",
            "url": "https://arxiv.org/abs/2601.00828"
          },
          {
            "title": "Decomposing LLM Self-Correction:",
            "url": "https://arxiv.org/pdf/2601.00828"
          },
          {
            "title": "Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis",
            "url": "https://arxiv.org/html/2601.00828"
          },
          {
            "title": "Self-Correction Makes LLMs Better Parsers",
            "url": "https://arxiv.org/html/2504.14165v1"
          },
          {
            "title": "Self-Correction Bench: Revealing and Addressing the Self-Correction Blind Spot in LLMs",
            "url": "https://arxiv.org/html/2507.02778v1"
          },
          {
            "title": "Self-Correction Makes LLMs Better Parsers",
            "url": "https://arxiv.org/pdf/2504.14165"
          },
          {
            "title": "Self-Correction Bench: Uncovering and Addressing the Self-Correction Blind Spot in Large Language Models",
            "url": "https://arxiv.org/pdf/2507.02778"
          }
        ]
      },
      "I found the paper! Here's what the search results reveal about arXiv 2601.00828:\n\n## Paper Overview\n\nThe paper is titled \"Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis\" and was submitted on December 24, 2025.\n\n## Key Findings\n\nThe work systematically decomposes self-correction into three distinct sub-capabilities: error detection, error localization, and error correction.\n\nThrough cross-model experiments on GSM8K-Complex with three major LLMs, the authors uncover an Accuracy-Correction Paradox: weaker models (GPT-3.5, 66% accuracy) achieve 1.6x higher intrinsic correction rates than stronger models (DeepSeek, 94% accuracy)—26.8% vs 16.7%.\n\n## The Error Depth Hypothesis\n\nThe paper proposes the Error Depth Hypothesis: stronger models make fewer but deeper errors that resist self-correction.\n\n## Notable Observations\n\nClaude detects 10% of errors but corrects 29%; GPT-3.5 detects 82% but corrects 27%, suggesting that error detection capability does not necessarily predict correction success.\n\nThe paper appears to be a significant contribution to understanding the limitations of LLM self-correction across models of varying capability levels."
    ],
    "durationSeconds": 6.957106631000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4ed8fe85-4895-433e-999a-744f2bf6c5ad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-20T03:22:44.762Z_

```json
{
  "parentUuid": "4bdb3fc5-8c34-4b19-9d0c-8152834bbc3b",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f19c38a4-ca07-44bb-bf75-3bd08d7ca3a1",
  "timestamp": "2026-05-20T03:22:44.762Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 37 · 2026-05-20T03:22:49.203Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent, I now have a good picture of the cited papers and the field. Let me do one more round of searches to look for the most directly competing work - specifically, anyone who has already tried to predict "correctability" (as opposed to just "correctness") from internal representations, and also for PAG and Reflective Confidence baselines mentioned in the proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f19c38a4-ca07-44bb-bf75-3bd08d7ca3a1",
  "isSidechain": false,
  "requestId": "req_011CbD6x9eofTJWv7x6bs8pN",
  "type": "assistant",
  "uuid": "165b6c98-7299-4902-aeac-3f7f650efce0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DKFNBzUCQV9f9xAXYQqZTE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3031,
      "cache_read_input_tokens": 21176,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 299,
          "cache_read_input_tokens": 21176,
          "cache_creation_input_tokens": 3031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3031
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

### Assistant

_source line 38 · 2026-05-20T03:22:49.695Z_

Let me do a couple more targeted searches to complete my understanding of the competitive landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "165b6c98-7299-4902-aeac-3f7f650efce0",
  "isSidechain": false,
  "requestId": "req_011CbD6x9eofTJWv7x6bs8pN",
  "type": "assistant",
  "uuid": "cf9f9b8f-aa59-4f1f-9e2a-0c6b9f4ce080",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DKFNBzUCQV9f9xAXYQqZTE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3031,
      "cache_read_input_tokens": 21176,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 299,
          "cache_read_input_tokens": 21176,
          "cache_creation_input_tokens": 3031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3031
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

_source line 39 · 2026-05-20T03:22:50.648Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DXAPFccLxVSjwKQ7dt3rqn`</summary>

```json
{
  "query": "probe-gated self-correction LLM hidden state routing abstention 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf9f9b8f-aa59-4f1f-9e2a-0c6b9f4ce080",
  "isSidechain": false,
  "requestId": "req_011CbD6x9eofTJWv7x6bs8pN",
  "type": "assistant",
  "uuid": "367e5f16-a936-4e3b-ae58-b27d1f0b0958",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DKFNBzUCQV9f9xAXYQqZTE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3031,
      "cache_read_input_tokens": 21176,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 299,
          "cache_read_input_tokens": 21176,
          "cache_creation_input_tokens": 3031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3031
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

_source line 40 · 2026-05-20T03:22:51.184Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M58j6diwVKA4e7WYVfr5oQ`</summary>

```json
{
  "query": "PAG probe-guided aggregation LLM reasoning self-correction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "367e5f16-a936-4e3b-ae58-b27d1f0b0958",
  "isSidechain": false,
  "requestId": "req_011CbD6x9eofTJWv7x6bs8pN",
  "type": "assistant",
  "uuid": "b97a3f58-791b-4dc1-bff4-dc84f45d8a8e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DKFNBzUCQV9f9xAXYQqZTE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3031,
      "cache_read_input_tokens": 21176,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 299,
          "cache_read_input_tokens": 21176,
          "cache_creation_input_tokens": 3031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3031
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

_source line 41 · 2026-05-20T03:22:51.857Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B6usQwfJvPyWnUR5ZgWWgp`</summary>

```json
{
  "query": "Gnosis LLM self-verification hidden states correctness probing 2025 arXiv 2512.20578"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b97a3f58-791b-4dc1-bff4-dc84f45d8a8e",
  "isSidechain": false,
  "requestId": "req_011CbD6x9eofTJWv7x6bs8pN",
  "type": "assistant",
  "uuid": "3f0235e7-b037-417a-a867-a035d9c9619c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DKFNBzUCQV9f9xAXYQqZTE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3031,
      "cache_read_input_tokens": 21176,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 299,
          "cache_read_input_tokens": 21176,
          "cache_creation_input_tokens": 3031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3031
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

_source line 42 · 2026-05-20T03:22:57.124Z_

<details><summary>↩ Tool result · `toolu_01DXAPFccLxVSjwKQ7dt3rqn`</summary>

```text
Web search results for query: "probe-gated self-correction LLM hidden state routing abstention 2025 2026"

Links: [{"title":"ReLope: KL-Regularized LoRA Probes for Multimodal LLM Routing","url":"https://arxiv.org/pdf/2603.24787"},{"title":"ReLope: KL-Regularized LoRA Probes for Multimodal LLM Routing","url":"https://arxiv.org/html/2603.24787"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018.full.pdf"},{"title":"Latent Space Chain-of-Embedding Enables Output-free LLM Self-Evaluation","url":"https://arxiv.org/pdf/2410.13640"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/pdf/2512.20578"}]

Based on the web search results, I found several relevant papers on related topics from 2025-2026, though the exact phrase "probe-gated self-correction" didn't appear in these results. Here's what I found:

## Recent Research on LLM Probes and Hidden States (2025-2026)

**ReLope: KL-Regularized LoRA Probes for Multimodal LLM Routing** (March 2026)
Probe routing, which predicts the correctness of a small model using its hidden states, provides an effective solution in text-only LLMs. The KL-Regularized LoRA Probe (ReLope) inserts a lightweight LoRA adapter and applies a KL regularizer to learn routing-aware representations.

**Gnosis: Self-Awareness via Internal Circuits** (December 2025)
Gnosis is a lightweight mechanism that enables frozen LLMs to predict the correctness of their own generations by decoding signals intrinsic to the inference process. Gnosis jointly models hidden-state evolution and attention-routing patterns through a compact, fixed-budget architecture.

**PING Framework** (September 2025)
PING is the first framework to leverage internal states for improved predictions directly at inference time, turning latent signals into calibrated, deployable predictions.

These papers explore how probes can extract correctness signals from hidden states for routing, self-correction, and abstention in LLMs, which aligns with the topics in your search query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "367e5f16-a936-4e3b-ae58-b27d1f0b0958",
  "isSidechain": false,
  "promptId": "f4225287-4bc9-436c-8172-482fb17da145",
  "type": "user",
  "uuid": "1f17a7e5-68bc-410b-9204-0f275c7a3c0a",
  "toolUseResult": {
    "query": "probe-gated self-correction LLM hidden state routing abstention 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DWboCRbgEp8jhw2UyBmD1G",
        "content": [
          {
            "title": "ReLope: KL-Regularized LoRA Probes for Multimodal LLM Routing",
            "url": "https://arxiv.org/pdf/2603.24787"
          },
          {
            "title": "ReLope: KL-Regularized LoRA Probes for Multimodal LLM Routing",
            "url": "https://arxiv.org/html/2603.24787"
          },
          {
            "title": "Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs",
            "url": "https://www.medrxiv.org/content/10.1101/2025.09.17.25336018.full.pdf"
          },
          {
            "title": "Latent Space Chain-of-Embedding Enables Output-free LLM Self-Evaluation",
            "url": "https://arxiv.org/pdf/2410.13640"
          },
          {
            "title": "Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs",
            "url": "https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"
          },
          {
            "title": "Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/pdf/2512.20578"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers on related topics from 2025-2026, though the exact phrase \"probe-gated self-correction\" didn't appear in these results. Here's what I found:\n\n## Recent Research on LLM Probes and Hidden States (2025-2026)\n\n**ReLope: KL-Regularized LoRA Probes for Multimodal LLM Routing** (March 2026)\nProbe routing, which predicts the correctness of a small model using its hidden states, provides an effective solution in text-only LLMs. The KL-Regularized LoRA Probe (ReLope) inserts a lightweight LoRA adapter and applies a KL regularizer to learn routing-aware representations.\n\n**Gnosis: Self-Awareness via Internal Circuits** (December 2025)\nGnosis is a lightweight mechanism that enables frozen LLMs to predict the correctness of their own generations by decoding signals intrinsic to the inference process. Gnosis jointly models hidden-state evolution and attention-routing patterns through a compact, fixed-budget architecture.\n\n**PING Framework** (September 2025)\nPING is the first framework to leverage internal states for improved predictions directly at inference time, turning latent signals into calibrated, deployable predictions.\n\nThese papers explore how probes can extract correctness signals from hidden states for routing, self-correction, and abstention in LLMs, which aligns with the topics in your search query."
    ],
    "durationSeconds": 6.463785453999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "367e5f16-a936-4e3b-ae58-b27d1f0b0958",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-20T03:22:58.372Z_

<details><summary>↩ Tool result · `toolu_01M58j6diwVKA4e7WYVfr5oQ`</summary>

```text
Web search results for query: "PAG probe-guided aggregation LLM reasoning self-correction 2025 2026"

Links: [{"title":"PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250610406J/abstract"},{"title":"[2506.10406] PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier","url":"https://arxiv.org/abs/2506.10406"},{"title":"PAG: Multi-Turn Reinforced LLM Self-Correction with ...","url":"https://openreview.net/pdf?id=uqMXNXSUzB"},{"title":"A Single Revision Step Improves Token-Efficient LLM Reasoning","url":"https://arxiv.org/pdf/2602.02828"},{"title":"PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier","url":"https://jackory.github.io/pag/"},{"title":"Multi-Turn Reinforced LLM Self-Correction with Policy as ...","url":"https://arxiv.org/pdf/2506.10406"},{"title":"[Literature Review] PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier","url":"https://www.themoonlight.io/en/review/pag-multi-turn-reinforced-llm-self-correction-with-policy-as-generative-verifier"},{"title":"(PDF) PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier","url":"https://www.researchgate.net/publication/392629943_PAG_Multi-Turn_Reinforced_LLM_Self-Correction_with_Policy_as_Generative_Verifier"},{"title":"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs","url":"https://arxiv.org/pdf/2510.16062"}]

Based on the search results, here's what I found about PAG and related LLM self-correction research:

## PAG: Policy as Generative Verifier

PAG is a framework that empowers LLMs to self-correct by alternating between policy and verifier roles within a unified multi-turn reinforcement learning paradigm.

### Key Innovation

Distinct from prior approaches that always generate a second attempt regardless of model confidence, PAG introduces a selective revision mechanism where the model revises its answer only when its own generative verification step detects an error, and this verify-then-revise workflow alleviates model collapse while enhancing both reasoning and verification abilities.

### Performance Results

Extensive experiments across diverse reasoning benchmarks highlight PAG's dual advancements: as a policy, it enhances direct generation and self-correction accuracy; as a verifier, its self-verification outperforms self-consistency. Additionally, PAG's generative verifier achieves self-verify Best-of-N selection that consistently outperforms traditional majority voting, demonstrating genuine verification ability rather than just aggregation heuristics.

### Training Architecture

A single LLM seamlessly alternates between policy and verifier roles, jointly improving both reasoning and verification capabilities in a unified approach that is more efficient than training separate models or components.

The paper was published in June 2025 and represents recent advances in LLM self-correction techniques for complex reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b97a3f58-791b-4dc1-bff4-dc84f45d8a8e",
  "isSidechain": false,
  "promptId": "f4225287-4bc9-436c-8172-482fb17da145",
  "type": "user",
  "uuid": "fb4b29fc-81bc-494d-a31d-a2e0b9fe1144",
  "toolUseResult": {
    "query": "PAG probe-guided aggregation LLM reasoning self-correction 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MWhWDYTiU9SUtYaoywtGxk",
        "content": [
          {
            "title": "PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250610406J/abstract"
          },
          {
            "title": "[2506.10406] PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier",
            "url": "https://arxiv.org/abs/2506.10406"
          },
          {
            "title": "PAG: Multi-Turn Reinforced LLM Self-Correction with ...",
            "url": "https://openreview.net/pdf?id=uqMXNXSUzB"
          },
          {
            "title": "A Single Revision Step Improves Token-Efficient LLM Reasoning",
            "url": "https://arxiv.org/pdf/2602.02828"
          },
          {
            "title": "PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier",
            "url": "https://jackory.github.io/pag/"
          },
          {
            "title": "Multi-Turn Reinforced LLM Self-Correction with Policy as ...",
            "url": "https://arxiv.org/pdf/2506.10406"
          },
          {
            "title": "[Literature Review] PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier",
            "url": "https://www.themoonlight.io/en/review/pag-multi-turn-reinforced-llm-self-correction-with-policy-as-generative-verifier"
          },
          {
            "title": "(PDF) PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier",
            "url": "https://www.researchgate.net/publication/392629943_PAG_Multi-Turn_Reinforced_LLM_Self-Correction_with_Policy_as_Generative_Verifier"
          },
          {
            "title": "Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs",
            "url": "https://arxiv.org/pdf/2510.16062"
          }
        ]
      },
      "Based on the search results, here's what I found about PAG and related LLM self-correction research:\n\n## PAG: Policy as Generative Verifier\n\nPAG is a framework that empowers LLMs to self-correct by alternating between policy and verifier roles within a unified multi-turn reinforcement learning paradigm.\n\n### Key Innovation\n\nDistinct from prior approaches that always generate a second attempt regardless of model confidence, PAG introduces a selective revision mechanism where the model revises its answer only when its own generative verification step detects an error, and this verify-then-revise workflow alleviates model collapse while enhancing both reasoning and verification abilities.\n\n### Performance Results\n\nExtensive experiments across diverse reasoning benchmarks highlight PAG's dual advancements: as a policy, it enhances direct generation and self-correction accuracy; as a verifier, its self-verification outperforms self-consistency. Additionally, PAG's generative verifier achieves self-verify Best-of-N selection that consistently outperforms traditional majority voting, demonstrating genuine verification ability rather than just aggregation heuristics.\n\n### Training Architecture\n\nA single LLM seamlessly alternates between policy and verifier roles, jointly improving both reasoning and verification capabilities in a unified approach that is more efficient than training separate models or components.\n\nThe paper was published in June 2025 and represents recent advances in LLM self-correction techniques for complex reasoning tasks."
    ],
    "durationSeconds": 7.171183141000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b97a3f58-791b-4dc1-bff4-dc84f45d8a8e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "fb4b29fc-81bc-494d-a31d-a2e0b9fe1144",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate correctability prediction proposal AUROC",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3"
}
```

---

### Tool result

_source line 46 · 2026-05-20T03:23:00.040Z_

<details><summary>↩ Tool result · `toolu_01B6usQwfJvPyWnUR5ZgWWgp`</summary>

```text
Web search results for query: "Gnosis LLM self-verification hidden states correctness probing 2025 arXiv 2512.20578"

Links: [{"title":"Paper page - Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://huggingface.co/papers/2512.20578"},{"title":"[2512.20578] Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/abs/2512.20578"},{"title":"Self-Awareness in LLMs: Gnosis Circuits","url":"https://www.emergentmind.com/papers/2512.20578"},{"title":"(PDF) Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://www.researchgate.net/publication/399026830_Can_LLMs_Predict_Their_Own_Failures_Self-Awareness_via_Internal_Circuits"},{"title":"Self-aware LLMs Advance AI Safety, Predicting Errors With ~5M Parameter Gnosis","url":"https://quantumzeitgeist.com/ai-self-aware-llms-advance-safety-predicting-errors-parameter/"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/html/2512.20578v1"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/pdf/2512.20578"}]

Based on the search results, here's information about the paper with arXiv ID 2512.20578:

## Paper Overview

The paper "Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits" was submitted on December 23, 2025, by Amirhosein Ghasemabadi and Di Niu.

## Gnosis Mechanism

Gnosis is a lightweight self-awareness mechanism that enables frozen LLMs to perform intrinsic self-verification by decoding signals from hidden states and attention patterns. Gnosis passively observes internal traces, compresses them into fixed-budget descriptors, and predicts correctness with negligible inference cost, adding only ~5M parameters and operating independently of sequence length.

## Key Features

Gnosis employs dual-stream introspection from hidden states and attention, jointly modeling hidden-state evolution and attention-routing patterns through a compact, fixed-budget architecture that operates independently of sequence length.

## Evaluation

The paper evaluates Gnosis on three domains: Math-Reasoning (AMC12, AIME, HMMT), Open-Domain QA (TriviaQA), and Academic Knowledge Reasoning (MMLU-Pro), with these benchmarks stressing multi-step reasoning, hallucination detection, and out-of-distribution generalization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f0235e7-b037-417a-a867-a035d9c9619c",
  "isSidechain": false,
  "promptId": "f4225287-4bc9-436c-8172-482fb17da145",
  "type": "user",
  "uuid": "ea27b21d-314b-4c54-ac69-74f290cc86da",
  "toolUseResult": {
    "query": "Gnosis LLM self-verification hidden states correctness probing 2025 arXiv 2512.20578",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XMaACZSj2JKhuE2tefjc1w",
        "content": [
          {
            "title": "Paper page - Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://huggingface.co/papers/2512.20578"
          },
          {
            "title": "[2512.20578] Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/abs/2512.20578"
          },
          {
            "title": "Self-Awareness in LLMs: Gnosis Circuits",
            "url": "https://www.emergentmind.com/papers/2512.20578"
          },
          {
            "title": "(PDF) Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://www.researchgate.net/publication/399026830_Can_LLMs_Predict_Their_Own_Failures_Self-Awareness_via_Internal_Circuits"
          },
          {
            "title": "Self-aware LLMs Advance AI Safety, Predicting Errors With ~5M Parameter Gnosis",
            "url": "https://quantumzeitgeist.com/ai-self-aware-llms-advance-safety-predicting-errors-parameter/"
          },
          {
            "title": "Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/html/2512.20578v1"
          },
          {
            "title": "Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/pdf/2512.20578"
          }
        ]
      },
      "Based on the search results, here's information about the paper with arXiv ID 2512.20578:\n\n## Paper Overview\n\nThe paper \"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits\" was submitted on December 23, 2025, by Amirhosein Ghasemabadi and Di Niu.\n\n## Gnosis Mechanism\n\nGnosis is a lightweight self-awareness mechanism that enables frozen LLMs to perform intrinsic self-verification by decoding signals from hidden states and attention patterns. Gnosis passively observes internal traces, compresses them into fixed-budget descriptors, and predicts correctness with negligible inference cost, adding only ~5M parameters and operating independently of sequence length.\n\n## Key Features\n\nGnosis employs dual-stream introspection from hidden states and attention, jointly modeling hidden-state evolution and attention-routing patterns through a compact, fixed-budget architecture that operates independently of sequence length.\n\n## Evaluation\n\nThe paper evaluates Gnosis on three domains: Math-Reasoning (AMC12, AIME, HMMT), Open-Domain QA (TriviaQA), and Academic Knowledge Reasoning (MMLU-Pro), with these benchmarks stressing multi-step reasoning, hallucination detection, and out-of-distribution generalization."
    ],
    "durationSeconds": 8.179667634999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3f0235e7-b037-417a-a867-a035d9c9619c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-20T03:23:03.652Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do one final search to see if anyone has specifically tried to predict "correctability" (whether an error is self-correctable) as distinct from "correctness" - this is the core claim of the proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea27b21d-314b-4c54-ac69-74f290cc86da",
  "isSidechain": false,
  "requestId": "req_011CbD6yH4pFcL39RA3ymKtn",
  "type": "assistant",
  "uuid": "d2e89858-bcfc-4907-a1d3-a022087ab5e8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GgxsVvH5gi9gQhPT3yuTHx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2638,
      "cache_read_input_tokens": 24207,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2638,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 215,
          "cache_read_input_tokens": 24207,
          "cache_creation_input_tokens": 2638,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2638
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

### Assistant

_source line 48 · 2026-05-20T03:23:04.573Z_

One final critical search — has anyone already framed "correctability" as a distinct prediction target?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2e89858-bcfc-4907-a1d3-a022087ab5e8",
  "isSidechain": false,
  "requestId": "req_011CbD6yH4pFcL39RA3ymKtn",
  "type": "assistant",
  "uuid": "ebf1684f-21e1-48c2-a74a-a49c6901226d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GgxsVvH5gi9gQhPT3yuTHx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2638,
      "cache_read_input_tokens": 24207,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2638,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 215,
          "cache_read_input_tokens": 24207,
          "cache_creation_input_tokens": 2638,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2638
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

_source line 49 · 2026-05-20T03:23:05.067Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F62QBPbGTZ1mejmk3hL4ZC`</summary>

```json
{
  "query": "\"correctability\" prediction LLM self-correction which errors fixable probing 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebf1684f-21e1-48c2-a74a-a49c6901226d",
  "isSidechain": false,
  "requestId": "req_011CbD6yH4pFcL39RA3ymKtn",
  "type": "assistant",
  "uuid": "aee73943-cdae-497d-a37a-ba4c51237c62",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GgxsVvH5gi9gQhPT3yuTHx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2638,
      "cache_read_input_tokens": 24207,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2638,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 215,
          "cache_read_input_tokens": 24207,
          "cache_creation_input_tokens": 2638,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2638
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

_source line 50 · 2026-05-20T03:23:05.620Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W7Q7pym8udCxVBkoEhe8qU`</summary>

```json
{
  "query": "predicting which LLM errors are self-correctable internal representations selective correction gating 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aee73943-cdae-497d-a37a-ba4c51237c62",
  "isSidechain": false,
  "requestId": "req_011CbD6yH4pFcL39RA3ymKtn",
  "type": "assistant",
  "uuid": "023436ca-ccc3-433a-b2cb-39e0167bce0f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GgxsVvH5gi9gQhPT3yuTHx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2638,
      "cache_read_input_tokens": 24207,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2638,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 215,
          "cache_read_input_tokens": 24207,
          "cache_creation_input_tokens": 2638,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2638
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

_source line 51 · 2026-05-20T03:23:11.626Z_

<details><summary>↩ Tool result · `toolu_01F62QBPbGTZ1mejmk3hL4ZC`</summary>

```text
Web search results for query: ""correctability" prediction LLM self-correction which errors fixable probing 2025 2026"

Links: [{"title":"How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals","url":"https://arxiv.org/html/2604.22271v1"},{"title":"Decomposing LLM Self-Correction:","url":"https://web3.arxiv.org/pdf/2601.00828"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"},{"title":"Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis","url":"https://arxiv.org/pdf/2601.00828"},{"title":"Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis","url":"https://arxiv.org/html/2601.00828"}]

Based on the web search results, here are key findings on correctability prediction in LLM self-correction:

## Correctability Prediction Through Internal Signals

Internal neural activations (PANL) can predict which errors a model can correct—where all behavioral signals fail. More specifically, LLMs naturally implement a second-order confidence architecture whose internal evaluative signal encodes not only whether an answer is likely wrong but whether the model has the knowledge to fix it.

## The Accuracy-Correction Paradox

Recent research reveals a counterintuitive finding: weaker models (GPT-3.5, 66% accuracy) achieve 1.6× higher intrinsic correction rates than stronger models (DeepSeek, 94% accuracy)—26.8% vs 16.7%.

## Error Depth Hypothesis

To explain this paradox, researchers propose that stronger models make fewer but "deeper" errors that resist self-correction, while weaker models make more but "shallower" errors (calculation) that are easily fixable upon re-examination.

## Detection vs. Correction Gap

Interestingly, error detection rates vary dramatically across architectures (10% to 82%), yet detection capability does not predict correction success—Claude detects only 10% of errors but corrects 29% intrinsically.

These findings from 2025-2026 demonstrate that determining error correctability requires probing internal model representations rather than relying on behavioral measures alone.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aee73943-cdae-497d-a37a-ba4c51237c62",
  "isSidechain": false,
  "promptId": "f4225287-4bc9-436c-8172-482fb17da145",
  "type": "user",
  "uuid": "acacbead-f3da-48af-9d2b-49546ba68f21",
  "toolUseResult": {
    "query": "\"correctability\" prediction LLM self-correction which errors fixable probing 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TJ9gRR4KGG4AXDkZH6ZgMZ",
        "content": [
          {
            "title": "How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals",
            "url": "https://arxiv.org/html/2604.22271v1"
          },
          {
            "title": "Decomposing LLM Self-Correction:",
            "url": "https://web3.arxiv.org/pdf/2601.00828"
          },
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs",
            "url": "https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"
          },
          {
            "title": "Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis",
            "url": "https://arxiv.org/pdf/2601.00828"
          },
          {
            "title": "Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis",
            "url": "https://arxiv.org/html/2601.00828"
          }
        ]
      },
      "Based on the web search results, here are key findings on correctability prediction in LLM self-correction:\n\n## Correctability Prediction Through Internal Signals\n\nInternal neural activations (PANL) can predict which errors a model can correct—where all behavioral signals fail. More specifically, LLMs naturally implement a second-order confidence architecture whose internal evaluative signal encodes not only whether an answer is likely wrong but whether the model has the knowledge to fix it.\n\n## The Accuracy-Correction Paradox\n\nRecent research reveals a counterintuitive finding: weaker models (GPT-3.5, 66% accuracy) achieve 1.6× higher intrinsic correction rates than stronger models (DeepSeek, 94% accuracy)—26.8% vs 16.7%.\n\n## Error Depth Hypothesis\n\nTo explain this paradox, researchers propose that stronger models make fewer but \"deeper\" errors that resist self-correction, while weaker models make more but \"shallower\" errors (calculation) that are easily fixable upon re-examination.\n\n## Detection vs. Correction Gap\n\nInterestingly, error detection rates vary dramatically across architectures (10% to 82%), yet detection capability does not predict correction success—Claude detects only 10% of errors but corrects 29% intrinsically.\n\nThese findings from 2025-2026 demonstrate that determining error correctability requires probing internal model representations rather than relying on behavioral measures alone."
    ],
    "durationSeconds": 6.546915518000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "aee73943-cdae-497d-a37a-ba4c51237c62",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T03:23:12.633Z_

<details><summary>↩ Tool result · `toolu_01W7Q7pym8udCxVBkoEhe8qU`</summary>

```text
Web search results for query: "predicting which LLM errors are self-correctable internal representations selective correction gating 2025 2026"

Links: [{"title":"How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals","url":"https://arxiv.org/html/2604.22271v1"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/pdf/2512.20578"},{"title":"[2512.20578] Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/abs/2512.20578"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"},{"title":"Self-Correction in Language Models","url":"https://www.emergentmind.com/topics/self-correction-in-language-models"},{"title":"Published as a conference paper at ICLR 2026 MECHANISTIC INTERPRETABILITY","url":"https://arxiv.org/pdf/2510.02917"}]

Based on the search results, I found several highly relevant papers on this topic:

## Key Research Findings

LLMs cache an evaluative representation that drives verbal confidence and predicts which errors the model can correct. This research addresses a fundamental question in LLM self-correction: whether the model's own confidence predicts whether it will identify an error and whether a correction attempt will succeed.

Large language models can detect their own errors and sometimes correct them without external feedback, investigated through the lens of second-order models of confidence from decision neuroscience. The key insight is that second-order models posit a partially independent evaluative signal that can disagree with the committed response, providing the basis for error detection.

## Recent 2025-2026 Work

Recent research has also explored predicting LLM failures through internal circuits. One approach taps hidden states and attention maps from a frozen LLM, compresses them into descriptors, and predicts correctness with negligible inference cost, adding only ~5M parameters.

Additionally, predictors can guide selective steering, intervening only when errors are anticipated to prevent corruption from constant steering, suggesting practical applications for selective correction based on error predictions.

These studies collectively show that internal representations within LLMs carry signals about error likelihood and self-correctability, enabling more targeted and efficient correction strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "023436ca-ccc3-433a-b2cb-39e0167bce0f",
  "isSidechain": false,
  "promptId": "f4225287-4bc9-436c-8172-482fb17da145",
  "type": "user",
  "uuid": "bc186af0-273c-467d-b845-6e4db69d5797",
  "toolUseResult": {
    "query": "predicting which LLM errors are self-correctable internal representations selective correction gating 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WS1JrCewZC53LSmCHgcNdr",
        "content": [
          {
            "title": "How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals",
            "url": "https://arxiv.org/html/2604.22271v1"
          },
          {
            "title": "Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/pdf/2512.20578"
          },
          {
            "title": "[2512.20578] Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/abs/2512.20578"
          },
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs",
            "url": "https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"
          },
          {
            "title": "Self-Correction in Language Models",
            "url": "https://www.emergentmind.com/topics/self-correction-in-language-models"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 MECHANISTIC INTERPRETABILITY",
            "url": "https://arxiv.org/pdf/2510.02917"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers on this topic:\n\n## Key Research Findings\n\nLLMs cache an evaluative representation that drives verbal confidence and predicts which errors the model can correct. This research addresses a fundamental question in LLM self-correction: whether the model's own confidence predicts whether it will identify an error and whether a correction attempt will succeed.\n\nLarge language models can detect their own errors and sometimes correct them without external feedback, investigated through the lens of second-order models of confidence from decision neuroscience. The key insight is that second-order models posit a partially independent evaluative signal that can disagree with the committed response, providing the basis for error detection.\n\n## Recent 2025-2026 Work\n\nRecent research has also explored predicting LLM failures through internal circuits. One approach taps hidden states and attention maps from a frozen LLM, compresses them into descriptors, and predicts correctness with negligible inference cost, adding only ~5M parameters.\n\nAdditionally, predictors can guide selective steering, intervening only when errors are anticipated to prevent corruption from constant steering, suggesting practical applications for selective correction based on error predictions.\n\nThese studies collectively show that internal representations within LLMs carry signals about error likelihood and self-correctability, enabling more targeted and efficient correction strategies."
    ],
    "durationSeconds": 7.005572918999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "023436ca-ccc3-433a-b2cb-39e0167bce0f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-20T03:23:15.628Z_

<details><summary>Logged reasoning block</summary>

```text
Let me also search for the paper arXiv:2604.22271 that keeps appearing in results - it seems directly relevant.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc186af0-273c-467d-b845-6e4db69d5797",
  "isSidechain": false,
  "requestId": "req_011CbD6zCp7LKYSvB8oZh6u6",
  "type": "assistant",
  "uuid": "bc158a0f-84b6-4752-8653-e070415c37d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Vv3cFsYXdcFa9q2Popka3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1553,
      "cache_read_input_tokens": 26845,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1553,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 128,
          "cache_read_input_tokens": 26845,
          "cache_creation_input_tokens": 1553,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1553
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

_source line 54 · 2026-05-20T03:23:15.962Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014cuRtcTSqRHyPLW3cTpA4q`</summary>

```json
{
  "query": "arXiv 2604.22271 \"How LLMs Detect and Correct Their Own Errors\" internal confidence signals PANL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc158a0f-84b6-4752-8653-e070415c37d0",
  "isSidechain": false,
  "requestId": "req_011CbD6zCp7LKYSvB8oZh6u6",
  "type": "assistant",
  "uuid": "e0ec181e-5530-41e4-8e65-d0ee843dc223",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Vv3cFsYXdcFa9q2Popka3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1553,
      "cache_read_input_tokens": 26845,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1553,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 128,
          "cache_read_input_tokens": 26845,
          "cache_creation_input_tokens": 1553,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1553
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

_source line 55 · 2026-05-20T03:23:22.513Z_

<details><summary>↩ Tool result · `toolu_014cuRtcTSqRHyPLW3cTpA4q`</summary>

```text
Web search results for query: "arXiv 2604.22271 "How LLMs Detect and Correct Their Own Errors" internal confidence signals PANL 2026"

Links: [{"title":"How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals","url":"https://arxiv.org/html/2604.22271v1"},{"title":"On LLMs' Internal Representation of Code Correctness","url":"https://arxiv.org/pdf/2512.07404"},{"title":"Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders","url":"https://arxiv.org/html/2604.19974"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/pdf/2512.20578"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/html/2512.20578"},{"title":"Can LLMs Detect Their Confabulations? Estimating Reliability in Uncertainty-Aware Language Models","url":"https://arxiv.org/pdf/2508.08139"},{"title":"Know When You're Wrong: Aligning Confidence with Correctness for LLM Error Detection","url":"https://arxiv.org/pdf/2603.06604"},{"title":"LLMs Know More Than They Show: On the Intrinsic Representation of LLM Hallucinations","url":"https://arxiv.org/pdf/2410.02707"}]

I found the paper! Here are the key details about arXiv:2604.22271:

## "How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals"

This paper by Dharshan Kumaran, Viorica Patraucean, Simon Osindero, Petar Veličković, and Nathaniel Daw from Google DeepMind (and Princeton University) was published on April 24, 2026, and investigates how large language models can detect their own errors and sometimes correct them without external feedback.

### Key Approach

The authors investigate this through the lens of second-order models of confidence from decision neuroscience. Second-order models posit a partially independent evaluative signal that can disagree with the committed response, providing the basis for error detection.

### Main Finding

The research shows that LLMs cache a confidence representation at a token immediately following the answer. This internal confidence signal mechanism is central to understanding how models can detect and potentially correct errors without relying on external feedback.

The paper addresses a significant gap in understanding the underlying mechanisms of LLM error detection and self-correction, using principles from neuroscience to explain how internal signals enable these capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0ec181e-5530-41e4-8e65-d0ee843dc223",
  "isSidechain": false,
  "promptId": "f4225287-4bc9-436c-8172-482fb17da145",
  "type": "user",
  "uuid": "cb752812-f800-47a4-b5d2-e82c6116e104",
  "toolUseResult": {
    "query": "arXiv 2604.22271 \"How LLMs Detect and Correct Their Own Errors\" internal confidence signals PANL 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016x9Lyo7gzoa1ZmQ4uQrDH9",
        "content": [
          {
            "title": "How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals",
            "url": "https://arxiv.org/html/2604.22271v1"
          },
          {
            "title": "On LLMs' Internal Representation of Code Correctness",
            "url": "https://arxiv.org/pdf/2512.07404"
          },
          {
            "title": "Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders",
            "url": "https://arxiv.org/html/2604.19974"
          },
          {
            "title": "Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/pdf/2512.20578"
          },
          {
            "title": "Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/html/2512.20578"
          },
          {
            "title": "Can LLMs Detect Their Confabulations? Estimating Reliability in Uncertainty-Aware Language Models",
            "url": "https://arxiv.org/pdf/2508.08139"
          },
          {
            "title": "Know When You're Wrong: Aligning Confidence with Correctness for LLM Error Detection",
            "url": "https://arxiv.org/pdf/2603.06604"
          },
          {
            "title": "LLMs Know More Than They Show: On the Intrinsic Representation of LLM Hallucinations",
            "url": "https://arxiv.org/pdf/2410.02707"
          }
        ]
      },
      "I found the paper! Here are the key details about arXiv:2604.22271:\n\n## \"How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals\"\n\nThis paper by Dharshan Kumaran, Viorica Patraucean, Simon Osindero, Petar Veličković, and Nathaniel Daw from Google DeepMind (and Princeton University) was published on April 24, 2026, and investigates how large language models can detect their own errors and sometimes correct them without external feedback.\n\n### Key Approach\n\nThe authors investigate this through the lens of second-order models of confidence from decision neuroscience. Second-order models posit a partially independent evaluative signal that can disagree with the committed response, providing the basis for error detection.\n\n### Main Finding\n\nThe research shows that LLMs cache a confidence representation at a token immediately following the answer. This internal confidence signal mechanism is central to understanding how models can detect and potentially correct errors without relying on external feedback.\n\nThe paper addresses a significant gap in understanding the underlying mechanisms of LLM error detection and self-correction, using principles from neuroscience to explain how internal signals enable these capabilities."
    ],
    "durationSeconds": 6.5432765739999885,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e0ec181e-5530-41e4-8e65-d0ee843dc223",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-20T03:24:40.560Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture of the field. Let me synthesize and evaluate this proposal.

## Key findings from my research:

### Most directly competing/overlapping work:

1. **arXiv:2604.22271 - "How LLMs Detect and Correct Their Own Errors"** (Google DeepMind, April 2026): This is EXTREMELY close to the proposal. It investigates internal confidence signals at the post-answer token (which the proposal calls PANL), finds that LLMs cache a confidence representation that predicts which errors are self-correctable. This paper seems to be the one that found the "0.614 AUROC" with single-layer linear probe that the proposal references. 

The proposal is explicitly building on this work, extending it further.

2. **arXiv:2512.20578 - Gnosis** (December 2025): A lightweight mechanism using hidden states and attention patterns to predict LLM correctness. Uses ~5M parameters, dual-stream approach. Very relevant - also probes hidden states for correctness prediction.

3. **arXiv:2602.08948 - CoRefine** (February 2026): Confidence-guided self-refinement with three-way routing (HALT/RETHINK/ALTERNATIVE). The proposal explicitly differentiates from this.

4. **arXiv:2602.08159 - The Confidence Manif

** (February 2026): Shows correctness representations are low-dimensional and linearly separable, which the proposal builds on.

5. **arXiv:2604.19974 - Functional Dissociation via SAEs** (April 2026): Demonstrates that uncertainty and correctness are encoded by different feature populations.

6. **arXiv:2604.13386 - Multi-layer ensemble probing** (April 2026): Multi-layer ensembling significantly improves probe AUROC, and this is the core technique the proposal uses.

7. **arXiv:2510.04128 - Wait token mechanisms** (October 2025): Crosscoder analysis of Wait tokens.

8. **arXiv:2601.00828 - Error Depth Hypothesis** (January 2026): Decomposes self-correction behavior to understand how errors propagate through model layers.

9. **arXiv:2506.10406 - PAG** (June 2025): Uses policy as a generative verifier for multi-turn self-correction, serving as one of the baselines.

Now I'm evaluating what the proposal actually does. The core idea is that LLM internal representations can distinguish not just whether they're wrong, but whether those errors are fixable through self-correction. They're building Enhanced Correctability Probes that improve on the baseline 0.614 AUROC by combining multi-layer ensembles, multi-token features, and attention entropy metrics. These probes would then gate a three-way decision between keeping the original response, attempting correction, or abstaining. They're also planning representational geometry analysis to compare how correctability and correctness are organized in the model's latent space.

The main concern is whether this is actually novel compared to existing work. Confidence-based routing already exists in CoRefine, and while the proposal claims to differentiate by using hidden-state probes instead of output-level confidence, the Confidence Manifold paper already demonstrated that internal probes achieve 0.80-0.97 AUC for correctness detection versus 0.44-0.64 for output-based methods. So using internal probes for correctness is well-established. The real question becomes whether "correctability" as a second-order property is meaningfully different from "correctness" when probing, or whether existing correctness probes like Gnosis could simply gate correction without needing this additional layer of analysis.

Looking at the core assumptions, the proposal hinges on "correctability" being a distinct representational target from "correctness"—that internal states encode not just "am I wrong?" but "can I fix this?"—but this remains untested. The error depth hypothesis cited as motivation is behavioral, not representational. There's also a leap in assuming multi-layer ensembling, which worked for deception detection, will transfer to correctability, even though these are fundamentally different tasks. The claim about SAE-guided feature selection improving correctability prediction also needs validation.

On novelty, framing correctability as a distinct prediction target has some merit and goes beyond prior work like 2604.22271, though the technical components—multi-layer ensembling, multi-token features, SAE features, attention entropy—are each borrowed from existing papers. The representational geometry comparison between correctability and correctness is genuinely interesting, and the three-way gating mechanism appears to be a novel contribution.

For significance, the core question about which errors are self-correctable matters for the field, but this is fundamentally an empirical probing study whose impact hinges on whether correctability probes substantially outperform existing correctness-based approaches for gating. The dual-outcome framing is pragmatic—positive results would validate the approach while negative results still contribute through the representational analysis—but doesn't strengthen the underlying idea. The proposal demonstrates strong engagement with related work and clearly differentiates itself from CoRefine.

Looking at the overall assessment, this feels like a well-executed but incremental effort that combines existing techniques—multi-layer ensembling, SAE features, Wait tokens, correctness probes—and redirects them toward correctability rather than correctness. The reframing is interesting, but it's unclear how much genuine novelty emerges beyond the existing correctness probing literature. The DeepMind paper from April 2026 already demonstrates that internal confidence signals predict which errors can be corrected, which substantially overlaps with this proposal's core claim. What concerns me most is that this reads as a systematic engineering effort to integrate established methods rather than a conceptual breakthrough, and the technique-heavy approach obscures any surprising insight.

For an appropriate NLP venue, I'd estimate this at around 20-30% acceptance probability—the work is competent and addresses an important question, but the incremental nature of both the core idea and the methodology limits its impact. The related work section is thorough and well-positioned, which is a strength, but that doesn't overcome the fundamental novelty gap. The technical novelty is limited since the core components—multi-layer ensembling, SAE features, and correctness probing—are all drawn from recent work, with the representational geometry analysis being the strongest original contribution. The significance hinges on whether correctability probes actually outperform what we'd expect from existing correctness probes, and if they underperform, the paper becomes primarily a negative result. The related work section demonstrates strong awareness of the latest developments and clearly positions this work relative to concurrent research.

Looking more carefully at the referenced paper, I see the proposal is explicitly attempting to improve upon prior work that achieved only 0.614 AUROC with a single-layer probe—so the novelty claim becomes clearer but also more constrained, since it's fundamentally an engineering effort to combine existing techniques rather than introducing conceptually new ideas. The probability of acceptance sits around 15-25%, with the main risks being that the core territory is already covered by concurrent work and the combination of techniques feels incremental rather than genuinely novel.

That said, I should acknowledge the proposal does have some legitimate contributions worth noting: it's the first to explicitly distinguish correctability from correctness as separate phenomena, the first to compare their representational geometry properties, and the first to measure the overcorrection cost of the Wait baseline on correct answers. Still, these feel like natural extensions of the prior work rather than fundamental breakthroughs, and venue fit also matters—this would be essentially unacceptable for CoRL given its robotics focus, though I'm evaluating it as NLP/AI work instead.

I'm inclined to bump up slightly from my initial assessment because the "correctability as a second-order property" framing is genuinely interesting, and the representational geometry comparison could surface surprising findings. The connection to confounded features from prior work is clever, and there's real practical value in probe-gated correction systems. I'll revise to 20-30% with a median around 22%.

But let me ground this in what actual reviewers would likely say. A probing expert would note the techniques are mostly combinations of existing methods with an interesting but incremental framing. A self-correction specialist would acknowledge the core question matters, but point out that prior work already showed internal signals predict correctability—the main contribution here is just improving probe quality through known techniques. A mechanistic interpretability reviewer might find the geometry analysis interesting but worry it won't yield surprising results if correctability is simply a rotated version of correctness in representation space.

Settling on 20% as my median feels right. Time to write this up.

Wait—I should flag that this proposal seems like a venue mismatch if we're talking about CoRL, which focuses on robot learning. This is clearly NLP/AI work about LLM self-correction. The rubric appears templated for NLP/CL though, so I'll evaluate the idea quality on its own merits while noting the venue concern.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb752812-f800-47a4-b5d2-e82c6116e104",
  "isSidechain": false,
  "requestId": "req_011CbD6zw75eYZq132P3r6EU",
  "type": "assistant",
  "uuid": "34cdef45-a00e-42af-9134-62d753296b06",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S1dc1YLYxzqkPY5Cnsf9WD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 826,
      "cache_read_input_tokens": 28398,
      "output_tokens": 7058,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 826,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7058,
          "cache_read_input_tokens": 28398,
          "cache_creation_input_tokens": 826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 826
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

### Assistant

_source line 57 · 2026-05-20T03:25:52.154Z_

Now I have a comprehensive picture of the field. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:

1. arXiv:2604.22271 — "How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals" (Google DeepMind, April 2026):
   **最直接的竞争工作。** 该论文已经证明 LLM 在 post-answer token 处缓存了一个内部 confidence representation，该信号不仅能检测错误，还能预测哪些错误可以被自我纠正。Proposal 中提到的 "0.614 AUROC at PANL with single-layer linear probe" 极可能来源于此。这意味着 proposal 的核心 claim——"内部表征可以预测 correctability"——已被 DeepMind 团队部分建立。

2. arXiv:2604.13386 — "Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling" (April 2026):
   Proposal 的核心技术手段（multi-layer ensemble stacking）直接来源于此。该论文在 deception detection 上展示了 multi-layer ensembling 将 AUROC 提升最高 78%。Proposal 明确标注要测试此技术是否迁移到 correctability——这是合理的，但属于"已知技术的新应用"而非方法创新。

3. arXiv:2604.19974 — "Are LLM Uncertainty and Correctness Encoded by the Same Features?" (April 2026):
   通过 SAE 发现 uncertainty 和 correctness 由不同 feature populations 编码。68% 的 pure incorrectness features 是因果惰性的。Proposal 利用这一发现做 SAE-guided feature selection，瞄准 confounded feature intersection。这是合理的技术利用，但 proposal 对其的使用仍是推测性的（"correctability 是否依赖于 confounded features"）。

4. arXiv:2602.08948 — CoRefine (February 2026):
   Confidence-guided self-refinement，使用 211k 参数的 Conv1D controller 实现三路决策（HALT/RETHINK/ALTERNATIVE）。Proposal 明确与之对比，声称区别在于：(a) 使用 hidden-state probes 而非 output-level confidence，(b) 真正的 abstention，(c) correctability-aware。这些区别是实质性的，但增量性质明显。

5. arXiv:2602.08159 — "The Confidence Manifold" (February 2026):
   已建立 correctness 在 transformer 表征中呈低维线性可分结构（3-8 维，AUC 0.80-0.97）。Proposal 要测试 correctability 是否也具有类似几何结构——这是对已有发现的自然延伸。

6. arXiv:2512.20578 — Gnosis (December 2025):
   轻量级 self-awareness mechanism，~5M 参数，双流（hidden states + attention patterns）预测 correctness。与 proposal 在技术路径上高度重叠（都是 probe hidden states to predict properties of model outputs）。

7. arXiv:2601.00828 — "Decomposing LLM Self-Correction: Error Depth Hypothesis" (January 2026):
   提出 stronger models make deeper errors that resist self-correction。为 proposal 的 correctability 概念提供了行为层面的动机。

8. arXiv:2506.10406 — PAG (June 2025):
   Policy as Generative Verifier，selective revision only when self-verification detects error。Proposal 将其作为 baseline 之一。

- **调研总结**: 这个领域在 2025-2026 年极其活跃。"correctness probing" 已经成熟（AUC 0.80-0.97），内部信号预测 error self-correctability 已被 DeepMind 团队初步建立（2604.22271），confidence-based routing 已有 CoRefine 等方案。Proposal 处于"已有发现的工程优化 + 概念细化"的位置——将多种已有技术组合以提升 correctability probe 质量，并将 correctability 形式化为独立于 correctness 的预测目标。

【Trivial Alternative 检验】:

**存在显著的 trivial alternative 威胁。** 

1. **Correctness probe + 简单阈值 gating**: 既然 correctness probes 已经能达到 0.80-0.97 AUC（The Confidence Manifold, 2602.08159），一个明显的 trivial baseline 是：用现成的 correctness probe 做 gating（"错了就尝试纠正，对了就保留"），而不需要专门预测"错误是否可纠正"。Proposal 的增量价值在于区分"可纠正的错误"和"不可纠正的错误"以避免无效的纠正尝试——但这个增量有多大取决于"不可纠正错误"在总错误中的占比以及无效纠正的实际损害。如果大多数错误要么容易纠正要么模型本来就不会尝试纠正，那 correctability-aware gating 的边际收益可能很小。

2. **CoRefine-style confidence routing**: CoRefine 用 output-level confidence 做三路 routing，已经达到 92.6% 的 halt precision。Proposal 声称用 hidden-state probes 更好，但需要证明这个"更好"是 substantial 而非 marginal。

增量价值的最终判断取决于实验结果——但从 idea 层面看，trivial alternative 是真实存在的威胁。

【前提假设检验】:

1. **核心假设："Correctability 是一个可在表征层面独立于 correctness 被探测到的属性"** — 这是整个 proposal 的立足点，但完全未经验证。Correctability 是 correctness 的"二阶属性"（不仅要错，还要错误可被修复），它可能不会在表征空间中以独立于 correctness 的方式编码。如果 correctability 的信号完全嵌套在 correctness 信号中（即只是 correctness probe 的低置信区域），那整个 correctability-specific probing 的努力就没有增量价值。

2. **迁移假设："multi-layer ensembling 从 deception detection 迁移到 correctability prediction"** — Deception 涉及模型"知道真相但说谎"的信号，这在层间有一致的方向性旋转（论文 2604.13386 的几何解释）。Correctability 的信号可能完全不同——它不是一个"方向"而是一个关于模型知识边界的属性。迁移性不能想当然。

3. **暗含假设："SAE confounded features 与 correctability 有特殊关联"** — 2604.19974 发现 confounded features（同时编码 uncertainty 和 correctness 的特征）与 pure features 有功能差异，但没有任何证据表明这些 confounded features 编码了 correctability 信息。这一步推理是 proposal 自己的推测。

【3 维度打分】:

1. **Novelty: 弱** — 
   - 核心 claim "内部表征可预测 correctability" 已被 arXiv:2604.22271 (DeepMind) 部分建立，该论文已展示 PANL 处的内部 confidence signal 能预测哪些错误可被纠正。Proposal 的增量是"提升 probe 质量"（0.614 → 更高），但方法全部来自已有技术的组合（multi-layer ensembling from 2604.13386 + SAE features from 2604.19974 + attention entropy + multi-token features）。
   - "Correctability 作为独立于 correctness 的预测目标"这一概念化有一定新意，但它是 correctness probing 领域的自然延伸，审稿人不太可能认为这是一个 surprising framing。
   - Representational geometry comparison（correctability vs correctness 的几何结构对比）是最新颖的分析角度，但它更像是 2602.08159 (Confidence Manifold) 的 follow-up analysis。
   - 综合来看，novelty 主要体现在"已有技术的新组合 + 已有分析框架的新应用目标"。

2. **Significance: 中** — 
   - "哪些错误可以被自我纠正"是一个有实际价值的问题，对 LLM deployment 有直接影响。
   - 但如果 core finding 是 positive（probes work well），审稿人可能会说 "I would have guessed this"——考虑到 correctness probes 已经 0.80-0.97 AUC，correctability 作为其 refinement 能被探测到并不令人意外。
   - 如果 core finding 是 negative（probes don't improve much），贡献主要是 negative result + representational analysis，影响力有限。
   - 三路 gating with abstention 有实用价值，但是 engineering contribution 而非 scientific insight。
   - Error Depth Hypothesis (2601.00828) 已经提供了为什么不同错误有不同 correctability 的行为层面解释——proposal 的贡献是将其推进到表征层面，这有价值但不是 paradigm-shifting。

3. **Related Work: 强** — 
   - 对领域内最新工作的覆盖非常全面，包括 2026 年 4 月的最新论文。
   - 与 CoRefine 的差异化定位是明确且实质的（signal source, abstention, correctability specificity）。
   - 正确引用了 multi-layer ensembling、SAE functional dissociation、Wait token mechanisms 等关键前期工作。
   - 唯一的遗漏可能是 Gnosis (arXiv:2512.20578)——一个同样用 hidden states + attention patterns 预测 correctness 的系统，与 proposal 的技术路径高度重叠，应被讨论。

【概率估计】: [15% - 25%] 中位 20%

【估计理由】: 
Novelty 是限制上界的主要因素。核心 claim 已被 2604.22271 部分覆盖，技术手段是已有方法的组合，concept framing 是自然延伸而非 surprising insight。Significance 中等——问题有价值但结果无论正负都难以达到"surprising"的门槛。Related Work 的强覆盖提供了一定的下限保障。综合来看，这是一篇方向正确、技术到位、但缺乏让审稿人写 "I didn't expect this" 的核心发现的 proposal——在顶会中属于 borderline reject 到 weak reject 区间。

【主要风险】: 
1. **Novelty 被 arXiv:2604.22271 实质性削弱**: DeepMind 的工作已经建立了"内部 confidence 信号预测 correctability"的基本结论。Proposal 的改进（更好的 probe）可能被审稿人视为 incremental engineering optimization 而非 new scientific insight。
2. **Trivial alternative 难以击败**: 如果简单的 correctness probe + threshold gating 已经能捕获大部分 correctability 信号（因为 correctability 可能高度相关于 low-confidence errors），那么整套 ECP 方案的增量收益可能不够显著以证明其复杂性。
```

Sources:
- [How LLMs Detect and Correct Their Own Errors (arXiv:2604.22271)](https://arxiv.org/html/2604.22271v1)
- [Linear Probe Accuracy Scales with Model Size (arXiv:2604.13386)](https://arxiv.org/abs/2604.13386)
- [Are LLM Uncertainty and Correctness Encoded by the Same Features? (arXiv:2604.19974)](https://arxiv.org/abs/2604.19974)
- [CoRefine: Confidence-Guided Self-Refinement (arXiv:2602.08948)](https://arxiv.org/abs/2602.08948)
- [The Confidence Manifold (arXiv:2602.08159)](https://arxiv.org/html/2602.08159v1)
- [Can LLMs Predict Their Own Failures? Gnosis (arXiv:2512.20578)](https://arxiv.org/abs/2512.20578)
- [Decomposing LLM Self-Correction: Error Depth Hypothesis (arXiv:2601.00828)](https://arxiv.org/abs/2601.00828)
- [Internal states before wait modulate reasoning patterns (arXiv:2510.04128)](https://arxiv.org/abs/2510.04128)
- [PAG: Multi-Turn Reinforced LLM Self-Correction (arXiv:2506.10406)](https://arxiv.org/abs/2506.10406)
- [LLM Reasoning as Trajectories (arXiv:2604.05655)](https://arxiv.org/pdf/2604.05655)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34cdef45-a00e-42af-9134-62d753296b06",
  "isSidechain": false,
  "requestId": "req_011CbD6zw75eYZq132P3r6EU",
  "type": "assistant",
  "uuid": "4111d0cc-8ad1-4514-a17d-973cf8cc9c37",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S1dc1YLYxzqkPY5Cnsf9WD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 826,
      "cache_read_input_tokens": 28398,
      "output_tokens": 7058,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 826,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7058,
          "cache_read_input_tokens": 28398,
          "cache_creation_input_tokens": 826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 826
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

### Runtime record

_source line 58_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "4111d0cc-8ad1-4514-a17d-973cf8cc9c37",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3"
}
```

---

### Runtime record

_source line 59_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate correctability prediction proposal AUROC",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3"
}
```

---

### Runtime record

_source line 60_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "4111d0cc-8ad1-4514-a17d-973cf8cc9c37",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3"
}
```

---

### Runtime record

_source line 61_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate correctability prediction proposal AUROC",
  "sessionId": "d7dfc27f-d9b3-48f3-8f30-1e65ac9f4bd3"
}
```

---
