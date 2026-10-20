# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Can LLMs Predict Their Own Correc

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/d69ae16d-908d-4923-816c-a366b56904be.jsonl`
- **Structured JSON:** [`12d1ccb65f94c64f3a00.json`](../../sessions/12/12d1ccb65f94c64f3a00.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:25:53.953Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:25:53.953Z",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction\n\n## Description\nWe investigate whether LLMs' internal representations can predict which of their errors are self-correctable, and whether this prediction enables selective correction that outperforms both ungated correction, the trivial 'Wait' baseline, and confidence-based routing. Prior work shows a faint correctability signal at the post-answer newline token (PANL) achieving only 0.614 AUROC with a single-layer linear probe — insufficient for reliable gating. We develop Enhanced Correctability Probes (ECP) that combine multi-layer ensemble stacking, multi-token features (PANL + last-answer-token + reasoning tokens), attention-entropy features, pre-Wait hidden-state features (informed by crosscoder analysis of Wait-token mechanisms, arXiv:2510.04128), and SAE-guided feature selection targeting the confounded feature intersection that bridges uncertainty and correctness (motivated by the functional dissociation finding of arXiv:2604.19974, where 68% of pure incorrectness features are causally inert). We begin with a Phase 0 pilot that directly tests whether multi-layer ensembling — which improved deception detection AUROC by up to 78% (arXiv:2604.13386, specifically on Harm-Pressure Knowledge in Llama-70B) — transfers to the fundamentally different task of correctability prediction. These probes gate a three-way decision: retain the original answer (likely correct), attempt correction including probe-selective Wait insertion (error detected, high correctability), or abstain (error detected, low correctability). This framework is distinguished from CoRefine's (arXiv:2602.08948) three-way routing — which uses output-level confidence, lacks genuine abstention, and is not correctability-aware — by using hidden-state probes, providing a genuine abstention option for unfixable errors, and explicitly predicting error fixability rather than confidence. Critically, we provide the first evaluation of the 'Wait' baseline on correct answers, measuring its previously-unknown overcorrection cost. We also conduct the first representational geometry and SAE feature decomposition analysis of correctability vs. correctness, testing whether correctability — a second-order property that depends not just on whether the model is wrong but on whether correction mechanisms can reach the right answer — shares the low-dimensional, linearly-separable structure that correctness exhibits (arXiv:2602.08159), requires higher dimensionality or non-linear boundaries, or depends disproportionately on the narrow confounded feature population identified by arXiv:2604.19974. This analysis, combined with error depth characterization (arXiv:2601.00828) and threshold analysis mapping probe quality to gating utility, ensures publishable contributions even if probe AUROC plateaus at marginal levels. We evaluate across Gemma-3-27B, Qwen-2.5-7B-Instruct, and Mistral-Small-3.2-24B on TriviaQA, MMLU, and GSM8K, comparing against eight baselines including ungated correction, Wait (universal and probe-selective), confidence-based routing (CoRefine-style and Reflective Confidence-style), PAG, and oracle gating. Our contributions are: (1) operationalizing correctability as a prediction target distinct from correctness, (2) the first pilot testing whether multi-layer ensembling transfers from deception to correctability, (3) the first hidden-state probe-based gating with genuine abstention for correctability-aware self-correction — distinguished from CoRefine's confidence-based routing by signal source, abstention capability, and correctability specificity, (4) the first representational geometry and SAE feature decomposition comparison of correctability vs. correctness, testing whether second-order properties have a different confounded-feature signature than first-order properties, and (5) establishing the conditions — including minimum probe quality thresholds — under which probe-gated correction outperforms simpler alternatives including confidence-based controllers.\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T03:25:53.957Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:25:53.957Z",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be"
}
```

---

## Round 1

46 recorded events

### User

_source line 3 · 2026-05-20T03:25:53.976Z_

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
  "promptId": "cfd26950-1158-49a2-b94b-ad272b2bb26f",
  "type": "user",
  "uuid": "8e916360-4462-4615-a978-7f711712258d",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:25:53.975Z_

```json
{
  "parentUuid": "8e916360-4462-4615-a978-7f711712258d",
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
  "uuid": "4a39b90b-e9f2-48af-a038-fd9fc03ca163",
  "timestamp": "2026-05-20T03:25:53.975Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:25:53.975Z_

```json
{
  "parentUuid": "4a39b90b-e9f2-48af-a038-fd9fc03ca163",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b17f48d0-083a-417c-b4d1-1917f15bb2ef",
  "timestamp": "2026-05-20T03:25:53.975Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
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
  "aiTitle": "Evaluate LLM correctability prediction proposal",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be"
}
```

---

### Assistant

_source line 7 · 2026-05-20T03:26:07.420Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for CoRL 2026. Let me first carefully read the proposal, then conduct web searches to understand the field, and finally provide my assessment.

Wait - CoRL is Conference on Robot Learning. But this proposal is about LLMs, self-correction, probing internal representations... This doesn't seem like a CoRL paper at all. Let me re-read the instructions.

Actually, the user said "CoRL 2026 主会" but the proposal is about LLM self-correction probing. This seems more like an NLP/ML venue (ACL, NeurIPS, ICML, ICLR). 

I'll set aside the venue mismatch and focus on evaluating the proposal quality itself. The rubric mentions "NLP/CL 领域" so I'll treat this as an NLP/ML evaluation. Let me search for the related work to understand the landscape better—specifically looking into LLM self-correction mechanisms, correctability probing techniques, the papers cited, and how thinking tokens factor into this research direction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b17f48d0-083a-417c-b4d1-1917f15bb2ef",
  "isSidechain": false,
  "requestId": "req_011CbD7C71h6uHv3yTzHNWHg",
  "type": "assistant",
  "uuid": "af664e53-54cb-43ce-8268-74636b717f2f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RAaeQMT3z9a2CtXtwUKNLT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 16331,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 429,
          "cache_read_input_tokens": 16331,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
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

### Assistant

_source line 8 · 2026-05-20T03:26:07.429Z_

I need to conduct thorough field research before evaluating this proposal. Let me search for the key related works and the current state of the field.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af664e53-54cb-43ce-8268-74636b717f2f",
  "isSidechain": false,
  "requestId": "req_011CbD7C71h6uHv3yTzHNWHg",
  "type": "assistant",
  "uuid": "5c658f1e-8540-45c3-b6e8-f552ddc1c7cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RAaeQMT3z9a2CtXtwUKNLT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 16331,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 429,
          "cache_read_input_tokens": 16331,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
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

_source line 9 · 2026-05-20T03:26:07.434Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DRB6dUAhw8rJh7cRWTfFyf`</summary>

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
  "parentUuid": "5c658f1e-8540-45c3-b6e8-f552ddc1c7cd",
  "isSidechain": false,
  "requestId": "req_011CbD7C71h6uHv3yTzHNWHg",
  "type": "assistant",
  "uuid": "3ab8e7d8-4d10-499b-8ae2-1cceb209f3dc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RAaeQMT3z9a2CtXtwUKNLT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 16331,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 429,
          "cache_read_input_tokens": 16331,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
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

_source line 10 · 2026-05-20T03:26:07.443Z_

<details><summary>↩ Tool result · `toolu_01DRB6dUAhw8rJh7cRWTfFyf`</summary>

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
  "parentUuid": "3ab8e7d8-4d10-499b-8ae2-1cceb209f3dc",
  "isSidechain": false,
  "promptId": "cfd26950-1158-49a2-b94b-ad272b2bb26f",
  "type": "user",
  "uuid": "f1da9521-b045-434f-bae5-cae6388929e0",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "3ab8e7d8-4d10-499b-8ae2-1cceb209f3dc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-20T03:26:10.951Z_

Now let me conduct multiple searches in parallel to understand the field.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1da9521-b045-434f-bae5-cae6388929e0",
  "isSidechain": false,
  "requestId": "req_011CbD7D6fPdGMeSVJsUYV52",
  "type": "assistant",
  "uuid": "95c9293e-6238-44ec-b1e6-74bff20e1b9d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RF7yPz9y97YsbJ6Xu8kgYD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 16331,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 955,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 84,
          "cache_read_input_tokens": 16331,
          "cache_creation_input_tokens": 955,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 955
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

_source line 12 · 2026-05-20T03:26:11.207Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0154yme3wanFM5wExU1T38md`</summary>

```json
{
  "query": "LLM self-correction selective gating probe internal representations 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95c9293e-6238-44ec-b1e6-74bff20e1b9d",
  "isSidechain": false,
  "requestId": "req_011CbD7D6fPdGMeSVJsUYV52",
  "type": "assistant",
  "uuid": "94d81195-08a7-4404-a633-4bf054477b40",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RF7yPz9y97YsbJ6Xu8kgYD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 16331,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 955,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 84,
          "cache_read_input_tokens": 16331,
          "cache_creation_input_tokens": 955,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 955
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

_source line 13 · 2026-05-20T03:26:18.488Z_

<details><summary>↩ Tool result · `toolu_0154yme3wanFM5wExU1T38md`</summary>

```text
Web search results for query: "LLM self-correction selective gating probe internal representations 2024 2025"

Links: [{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"},{"title":"LARGE LANGUAGE MODELS HAVE INTRINSIC SELF- ...","url":"https://openreview.net/pdf?id=pTyEnkuSQ0"},{"title":"Superscopes: Amplifying Internal Feature Representations for Language   Model Interpretation","url":"https://arxiv.org/pdf/2503.02078"},{"title":"Probing for Arithmetic Errors in Language Models","url":"https://arxiv.org/pdf/2507.12379"},{"title":"Published as a conference paper at ICLR 2025","url":"https://belinkov.com/assets/pdf/iclr2025-know.pdf"},{"title":"Internalized Self-Correction for Large Language Models","url":"https://arxiv.org/pdf/2412.16653"},{"title":"LLM Representations Encode Information About Chain-of- ...","url":"https://aclanthology.org/2025.findings-acl.662.pdf"},{"title":"LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations","url":"https://arxiv.org/pdf/2602.09924"}]

Based on the search results, here are the key findings related to LLM self-correction and probing internal representations from 2024-2025:

## Self-Correction and Internal Representations

Logit-based approaches often underperform compared to those that leverage internal model representations, with methods that exploit interactions between internal representations achieving state-of-the-art performance with strong generalization.

## Probing Internal Activations

Recent work has focused on understanding how models encode information internally. Patchscopes introduced a method for probing internal activations by patching them into new prompts, with Superscopes systematically amplifying superposed features in MLP outputs and hidden states before patching them into new contexts.

## Error Detection and Selective Correction

Probes can guide selective re-prompting of erroneous reasoning steps, improving task accuracy with minimal disruption to correct outputs, with findings suggesting that arithmetic errors can be anticipated from internal activations alone.

## Truthfulness Signals

Internal representations of LLMs encode much more information about truthfulness than previously recognized, with classifiers trained on these internal representations able to predict various features related to the truthfulness of generated outputs and reveal the patterns and types of information encoded in model representations.

## Chain-of-Thought Prediction

LLMs generate intermediate reasoning steps in Chain-of-Thought sequences, with internal representations used to predict whether the CoT process will succeed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94d81195-08a7-4404-a633-4bf054477b40",
  "isSidechain": false,
  "promptId": "cfd26950-1158-49a2-b94b-ad272b2bb26f",
  "type": "user",
  "uuid": "5bbd06f5-dc6e-44fa-804d-b096829b9290",
  "toolUseResult": {
    "query": "LLM self-correction selective gating probe internal representations 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_011W8G7h1HhZBTGUMmEdDbjV",
        "content": [
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs",
            "url": "https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"
          },
          {
            "title": "LARGE LANGUAGE MODELS HAVE INTRINSIC SELF- ...",
            "url": "https://openreview.net/pdf?id=pTyEnkuSQ0"
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
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://belinkov.com/assets/pdf/iclr2025-know.pdf"
          },
          {
            "title": "Internalized Self-Correction for Large Language Models",
            "url": "https://arxiv.org/pdf/2412.16653"
          },
          {
            "title": "LLM Representations Encode Information About Chain-of- ...",
            "url": "https://aclanthology.org/2025.findings-acl.662.pdf"
          },
          {
            "title": "LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations",
            "url": "https://arxiv.org/pdf/2602.09924"
          }
        ]
      },
      "Based on the search results, here are the key findings related to LLM self-correction and probing internal representations from 2024-2025:\n\n## Self-Correction and Internal Representations\n\nLogit-based approaches often underperform compared to those that leverage internal model representations, with methods that exploit interactions between internal representations achieving state-of-the-art performance with strong generalization.\n\n## Probing Internal Activations\n\nRecent work has focused on understanding how models encode information internally. Patchscopes introduced a method for probing internal activations by patching them into new prompts, with Superscopes systematically amplifying superposed features in MLP outputs and hidden states before patching them into new contexts.\n\n## Error Detection and Selective Correction\n\nProbes can guide selective re-prompting of erroneous reasoning steps, improving task accuracy with minimal disruption to correct outputs, with findings suggesting that arithmetic errors can be anticipated from internal activations alone.\n\n## Truthfulness Signals\n\nInternal representations of LLMs encode much more information about truthfulness than previously recognized, with classifiers trained on these internal representations able to predict various features related to the truthfulness of generated outputs and reveal the patterns and types of information encoded in model representations.\n\n## Chain-of-Thought Prediction\n\nLLMs generate intermediate reasoning steps in Chain-of-Thought sequences, with internal representations used to predict whether the CoT process will succeed."
    ],
    "durationSeconds": 7.272010172999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "94d81195-08a7-4404-a633-4bf054477b40",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T03:26:20.982Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BxoLNJcwvV8AXcn9Kq9uTh`</summary>

```json
{
  "query": "CoRefine arXiv 2602.08948 LLM self-correction routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bbd06f5-dc6e-44fa-804d-b096829b9290",
  "isSidechain": false,
  "requestId": "req_011CbD7DuVD2cD4RBki6J5Sw",
  "type": "assistant",
  "uuid": "f4d2673d-74e8-4467-84c5-e59e90b3fb3e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018yTv5vnDksQD2jRD6jkGBr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 815,
      "cache_read_input_tokens": 17286,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 815,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 17286,
          "cache_creation_input_tokens": 815,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 815
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

_source line 15 · 2026-05-20T03:26:28.476Z_

<details><summary>↩ Tool result · `toolu_01BxoLNJcwvV8AXcn9Kq9uTh`</summary>

```text
Web search results for query: "CoRefine arXiv 2602.08948 LLM self-correction routing"

Links: [{"title":"[2602.08948] CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute","url":"https://arxiv.org/abs/2602.08948"},{"title":"CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute","url":"https://arxiv.org/pdf/2602.08948"},{"title":"Unleashing the True Potential of LLMs: A Feedback-Triggered Self-Correction with Long-Term Multipath Decoding","url":"https://arxiv.org/pdf/2509.07676"},{"title":"Learning to Route LLMs with Confidence Tokens","url":"https://arxiv.org/pdf/2410.13284"},{"title":"Self-Correction Bench: Revealing and Addressing the Self-Correction Blind Spot in LLMs","url":"https://arxiv.org/html/2507.02778v1"},{"title":"Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis","url":"https://arxiv.org/pdf/2601.00828"},{"title":"Self-Correction Makes LLMs Better Parsers","url":"https://arxiv.org/pdf/2504.14165"}]

Based on the search results, here's what I found about CoRefine (arXiv 2602.08948):

## CoRefine: Confidence-Guided Self-Refinement

CoRefine is a confidence-guided self-refinement method that achieves competitive accuracy using a fraction of the tokens via a lightweight 211k-parameter Conv1D controller atop a frozen LLM.

**Purpose and Motivation:**
Large Language Models (LLMs) often rely on test-time scaling via parallel decoding (for example, 512 samples) to boost reasoning accuracy, but this incurs substantial compute.

**How It Works:**
The controller consumes full-trace confidence features of the LLM decoded reasoning chain and decides: HALT (accept current answer), RETHINK (verify reasoning), or ALTERNATIVE (explore new approach).

**Performance:**
The controller enables targeted self-correction with an average of 2.7 refinement steps per problem and roughly 190-fold token reduction relative to 512-sample baselines. The controller achieves 92.6 percent precision when it confidently halts, indicating that confidence dynamics reliably signal answer correctness.

**Efficiency Gains:**
Token savings translate to actual latency reduction, with CoRefine saving up to 63% over parallel baselines.

The paper was submitted on February 9, 2026, and authored by Chen Jin, Ryutaro Tanno, Tom Diethe, and Philip Teare.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4d2673d-74e8-4467-84c5-e59e90b3fb3e",
  "isSidechain": false,
  "promptId": "cfd26950-1158-49a2-b94b-ad272b2bb26f",
  "type": "user",
  "uuid": "0865b6fb-b590-49a5-8eae-ffa248226fcc",
  "toolUseResult": {
    "query": "CoRefine arXiv 2602.08948 LLM self-correction routing",
    "results": [
      {
        "tool_use_id": "srvtoolu_015qUQ2deWAPcyiFNj34qgYG",
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
            "title": "Unleashing the True Potential of LLMs: A Feedback-Triggered Self-Correction with Long-Term Multipath Decoding",
            "url": "https://arxiv.org/pdf/2509.07676"
          },
          {
            "title": "Learning to Route LLMs with Confidence Tokens",
            "url": "https://arxiv.org/pdf/2410.13284"
          },
          {
            "title": "Self-Correction Bench: Revealing and Addressing the Self-Correction Blind Spot in LLMs",
            "url": "https://arxiv.org/html/2507.02778v1"
          },
          {
            "title": "Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis",
            "url": "https://arxiv.org/pdf/2601.00828"
          },
          {
            "title": "Self-Correction Makes LLMs Better Parsers",
            "url": "https://arxiv.org/pdf/2504.14165"
          }
        ]
      },
      "Based on the search results, here's what I found about CoRefine (arXiv 2602.08948):\n\n## CoRefine: Confidence-Guided Self-Refinement\n\nCoRefine is a confidence-guided self-refinement method that achieves competitive accuracy using a fraction of the tokens via a lightweight 211k-parameter Conv1D controller atop a frozen LLM.\n\n**Purpose and Motivation:**\nLarge Language Models (LLMs) often rely on test-time scaling via parallel decoding (for example, 512 samples) to boost reasoning accuracy, but this incurs substantial compute.\n\n**How It Works:**\nThe controller consumes full-trace confidence features of the LLM decoded reasoning chain and decides: HALT (accept current answer), RETHINK (verify reasoning), or ALTERNATIVE (explore new approach).\n\n**Performance:**\nThe controller enables targeted self-correction with an average of 2.7 refinement steps per problem and roughly 190-fold token reduction relative to 512-sample baselines. The controller achieves 92.6 percent precision when it confidently halts, indicating that confidence dynamics reliably signal answer correctness.\n\n**Efficiency Gains:**\nToken savings translate to actual latency reduction, with CoRefine saving up to 63% over parallel baselines.\n\nThe paper was submitted on February 9, 2026, and authored by Chen Jin, Ryutaro Tanno, Tom Diethe, and Philip Teare."
    ],
    "durationSeconds": 7.488518487000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f4d2673d-74e8-4467-84c5-e59e90b3fb3e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "0865b6fb-b590-49a5-8eae-ffa248226fcc",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM correctability prediction proposal",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be"
}
```

---

### Tool call

_source line 18 · 2026-05-20T03:26:31.029Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018Ga6fCxDEK9uhjhBgTut9w`</summary>

```json
{
  "query": "arXiv 2604.19974 LLM correctness features SAE sparse autoencoder dissociation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0865b6fb-b590-49a5-8eae-ffa248226fcc",
  "isSidechain": false,
  "requestId": "req_011CbD7EeA13K8GMrLRzvWLp",
  "type": "assistant",
  "uuid": "74e606ee-2664-405e-8bbe-e22cb2d32694",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012BTAhwRVZMaTj3j8ASe1Vw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 773,
      "cache_read_input_tokens": 18101,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 773,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 18101,
          "cache_creation_input_tokens": 773,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 773
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

_source line 19 · 2026-05-20T03:26:38.547Z_

<details><summary>↩ Tool result · `toolu_018Ga6fCxDEK9uhjhBgTut9w`</summary>

```text
Web search results for query: "arXiv 2604.19974 LLM correctness features SAE sparse autoencoder dissociation 2026"

Links: [{"title":"Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders","url":"https://arxiv.org/html/2604.19974"},{"title":"[2604.19974] Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders","url":"https://arxiv.org/abs/2604.19974"},{"title":"Sparse but Wrong: Incorrect L0 Leads to Incorrect Features in Sparse Autoencoders","url":"https://arxiv.org/pdf/2508.16560"},{"title":"Mechanistic Interpretability of Code Correctness in LLMs via Sparse Autoencoders","url":"https://arxiv.org/html/2510.02917v1"},{"title":"Sparse Autoencoder Features for Classifications and Transferability","url":"https://arxiv.org/pdf/2502.11367"},{"title":"Taming Polysemanticity in LLMs: Provable Feature Recovery via Sparse Autoencoders","url":"https://arxiv.org/pdf/2506.14002"},{"title":"CorrSteer: Generation-Time LLM Steering via Correlated Sparse Autoencoder Features","url":"https://arxiv.org/pdf/2508.12535"},{"title":"Sparse Autoencoder Features for Classifications and Transferability","url":"https://arxiv.org/html/2502.11367v1"}]

I found the paper! Here are the key details about arXiv 2604.19974:

## Paper Summary

The paper titled "Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders" was submitted on April 21, 2026, by Het Patel, Tiejin Chen, Hua Wei, Evangelos E. Papalexakis, and Jia Chen.

### Key Research Question

The paper addresses whether large language models' output-level uncertainty and their actual correctness are driven by the same internal mechanisms or by distinct feature populations.

### Methodology

The researchers introduce a 2x2 framework that partitions model predictions along correctness and confidence axes, and uses sparse autoencoders to identify features associated with each dimension independently. They apply this to Llama-3.1-8B and Gemma-2-9B models.

### Key Findings

The analysis yields three distinct feature populations: pure uncertainty features, pure incorrectness features, and confounded features associated with both signals. Through targeted suppression experiments, the researchers reveal a three-way dissociation in which each category plays a fundamentally different role in the model's computation.

Pure uncertainty features are functionally essential—suppressing them severely degrades accuracy—while pure incorrectness features are functionally inert, as the majority produce near-zero change in accuracy when suppressed despite showing statistically significant activation differences.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74e606ee-2664-405e-8bbe-e22cb2d32694",
  "isSidechain": false,
  "promptId": "cfd26950-1158-49a2-b94b-ad272b2bb26f",
  "type": "user",
  "uuid": "cf39beaf-5e69-41d1-afcb-4330e7498626",
  "toolUseResult": {
    "query": "arXiv 2604.19974 LLM correctness features SAE sparse autoencoder dissociation 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QgMDw4yN1SSjmMpEM4BB2Z",
        "content": [
          {
            "title": "Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders",
            "url": "https://arxiv.org/html/2604.19974"
          },
          {
            "title": "[2604.19974] Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders",
            "url": "https://arxiv.org/abs/2604.19974"
          },
          {
            "title": "Sparse but Wrong: Incorrect L0 Leads to Incorrect Features in Sparse Autoencoders",
            "url": "https://arxiv.org/pdf/2508.16560"
          },
          {
            "title": "Mechanistic Interpretability of Code Correctness in LLMs via Sparse Autoencoders",
            "url": "https://arxiv.org/html/2510.02917v1"
          },
          {
            "title": "Sparse Autoencoder Features for Classifications and Transferability",
            "url": "https://arxiv.org/pdf/2502.11367"
          },
          {
            "title": "Taming Polysemanticity in LLMs: Provable Feature Recovery via Sparse Autoencoders",
            "url": "https://arxiv.org/pdf/2506.14002"
          },
          {
            "title": "CorrSteer: Generation-Time LLM Steering via Correlated Sparse Autoencoder Features",
            "url": "https://arxiv.org/pdf/2508.12535"
          },
          {
            "title": "Sparse Autoencoder Features for Classifications and Transferability",
            "url": "https://arxiv.org/html/2502.11367v1"
          }
        ]
      },
      "I found the paper! Here are the key details about arXiv 2604.19974:\n\n## Paper Summary\n\nThe paper titled \"Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders\" was submitted on April 21, 2026, by Het Patel, Tiejin Chen, Hua Wei, Evangelos E. Papalexakis, and Jia Chen.\n\n### Key Research Question\n\nThe paper addresses whether large language models' output-level uncertainty and their actual correctness are driven by the same internal mechanisms or by distinct feature populations.\n\n### Methodology\n\nThe researchers introduce a 2x2 framework that partitions model predictions along correctness and confidence axes, and uses sparse autoencoders to identify features associated with each dimension independently. They apply this to Llama-3.1-8B and Gemma-2-9B models.\n\n### Key Findings\n\nThe analysis yields three distinct feature populations: pure uncertainty features, pure incorrectness features, and confounded features associated with both signals. Through targeted suppression experiments, the researchers reveal a three-way dissociation in which each category plays a fundamentally different role in the model's computation.\n\nPure uncertainty features are functionally essential—suppressing them severely degrades accuracy—while pure incorrectness features are functionally inert, as the majority produce near-zero change in accuracy when suppressed despite showing statistically significant activation differences."
    ],
    "durationSeconds": 7.513807080999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "74e606ee-2664-405e-8bbe-e22cb2d32694",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T03:26:41.108Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UHpZ6UkTEtXxsfTwgzt7UG`</summary>

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
  "parentUuid": "cf39beaf-5e69-41d1-afcb-4330e7498626",
  "isSidechain": false,
  "requestId": "req_011CbD7FPDMbM3oeZfsQEcX4",
  "type": "assistant",
  "uuid": "5499e99f-2a3d-425b-a3fd-8e0886e5d88d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRyeQYtwy17gEA8W2DH7uJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 849,
      "cache_read_input_tokens": 18874,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 849,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 18874,
          "cache_creation_input_tokens": 849,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 849
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

_source line 21 · 2026-05-20T03:26:47.626Z_

<details><summary>↩ Tool result · `toolu_01UHpZ6UkTEtXxsfTwgzt7UG`</summary>

```text
Web search results for query: "arXiv 2604.13386 multi-layer ensemble probing deception detection LLM 2026"

Links: [{"title":"Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling","url":"https://arxiv.org/html/2604.13386v1"},{"title":"[2604.13386] Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling","url":"https://arxiv.org/abs/2604.13386"},{"title":"Caught in the Act: a mechanistic approach to detecting deception","url":"https://arxiv.org/pdf/2508.19505"},{"title":"Caught in the Act: a mechanistic approach to detecting deception","url":"https://arxiv.org/html/2508.19505v2"},{"title":"Probing the Limits of the Lie Detector Approach to LLM Deception","url":"https://arxiv.org/html/2603.10003"},{"title":"DeceptGuard :A Constitutional Oversight Framework For Detecting Deception in LLM Agents","url":"https://arxiv.org/pdf/2603.13791"},{"title":"Detecting Multi-Agent Collusion Through Multi-Agent Interpretability","url":"https://arxiv.org/html/2604.01151v1"}]

I found the paper you're looking for! Here are the key findings:

The paper (arXiv:2604.13386) demonstrates that linear probes can detect when language models produce outputs they "know" are wrong, a capability relevant to both deception and reward hacking.

**Key Results:**

While single-layer probes are fragile with the best layer varying across models and tasks, combining probes from multiple layers into an ensemble recovers strong performance even where single-layer probes fail, improving AUROC by +29% on Insider Trading and +78% on Harm-Pressure Knowledge.

Across 12 models ranging from 0.5B to 176B parameters, probe accuracy improves with scale: approximately 5% AUROC per 10x parameters (R=0.81).

**Technical Insight:**

Geometrically, deception directions rotate gradually across layers rather than appearing at one location, explaining both why single-layer probes are brittle and why multi-layer ensembles succeed.

The paper was published on April 15, 2026, and is authored by Erik Nordby, Tasha Pais, and Aviel Parrack.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5499e99f-2a3d-425b-a3fd-8e0886e5d88d",
  "isSidechain": false,
  "promptId": "cfd26950-1158-49a2-b94b-ad272b2bb26f",
  "type": "user",
  "uuid": "6cee8b78-c448-4bdc-902a-eae2e2f5d6b5",
  "toolUseResult": {
    "query": "arXiv 2604.13386 multi-layer ensemble probing deception detection LLM 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01E72sYKLPHqKPGVeGbgv194",
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
      "I found the paper you're looking for! Here are the key findings:\n\nThe paper (arXiv:2604.13386) demonstrates that linear probes can detect when language models produce outputs they \"know\" are wrong, a capability relevant to both deception and reward hacking.\n\n**Key Results:**\n\nWhile single-layer probes are fragile with the best layer varying across models and tasks, combining probes from multiple layers into an ensemble recovers strong performance even where single-layer probes fail, improving AUROC by +29% on Insider Trading and +78% on Harm-Pressure Knowledge.\n\nAcross 12 models ranging from 0.5B to 176B parameters, probe accuracy improves with scale: approximately 5% AUROC per 10x parameters (R=0.81).\n\n**Technical Insight:**\n\nGeometrically, deception directions rotate gradually across layers rather than appearing at one location, explaining both why single-layer probes are brittle and why multi-layer ensembles succeed.\n\nThe paper was published on April 15, 2026, and is authored by Erik Nordby, Tasha Pais, and Aviel Parrack."
    ],
    "durationSeconds": 6.513072492999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5499e99f-2a3d-425b-a3fd-8e0886e5d88d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T03:26:50.071Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TUZpRhM6c761iXD7oJxGEj`</summary>

```json
{
  "query": "arXiv 2602.08159 LLM correctness linear probe representational geometry 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cee8b78-c448-4bdc-902a-eae2e2f5d6b5",
  "isSidechain": false,
  "requestId": "req_011CbD7G4BeCZi5rarxjQTMa",
  "type": "assistant",
  "uuid": "91b66ffe-86b9-4a35-9752-209e1567ec16",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lj5fcZny75yMBczDMqCzuC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 19723,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 697,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 19723,
          "cache_creation_input_tokens": 697,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 697
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

_source line 23 · 2026-05-20T03:27:08.394Z_

<details><summary>↩ Tool result · `toolu_01TUZpRhM6c761iXD7oJxGEj`</summary>

```text
Web search results for query: "arXiv 2602.08159 LLM correctness linear probe representational geometry 2026"

Links: [{"title":"Predicting LLM Answer Accuracy from Question-Only ...","url":"https://arxiv.org/pdf/2509.10625"},{"title":"Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation","url":"https://arxiv.org/html/2512.22245"},{"title":"Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation","url":"https://arxiv.org/pdf/2512.22245"},{"title":"No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes | OpenReview","url":"https://openreview.net/forum?id=OhN25uxVab"},{"title":"Can Linear Probes Measure LLM Uncertainty ?","url":"https://arxiv.org/html/2510.04108"}]

I didn't find the specific arXiv paper 2602.08159 in those results. Let me search more directly for that paper ID.

Links: [{"title":"Detection of patient metadata in published articles for genomic epidemiology using machine learning and large language models","url":"https://www.medrxiv.org/content/10.1101/2025.04.25.25326298.full.pdf"},{"title":"Association between TM6SF2 rs58542926 T/C gene polymorphism and significant liver fibrosis: A meta-analysis","url":"https://www.medrxiv.org/content/10.1101/2020.10.11.20210690.full.pdf"},{"title":"Unsupervised cross-domain data augmentation for long-document based prediction and explanation","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12321841"},{"title":"Dual-Model LLM Ensemble via Web Chat Interfaces Reaches Near-Perfect Sensitivity for Systematic-Review Screening: A Multi-Domain Validation with Equivalence to API Access","url":"https://www.medrxiv.org/content/10.1101/2025.11.03.25339455.full.pdf"},{"title":"LeafyResNet: Fusarium Wilt Detection in Lettuce Using UAV RGB Imaging and Advanced Deep Learning Model","url":"https://www.biorxiv.org/content/10.1101/2025.05.21.655416.full.pdf"}]

The results don't appear to contain the specific arXiv paper 2602.08159. Let me try a more targeted search for this paper.

Links: [{"title":"When do measured representational distances reflect the neural representational geometry?","url":"https://www.biorxiv.org/content/10.1101/2024.12.30.630743.full.pdf"},{"title":"The Representational Geometry of Number","url":"https://arxiv.org/html/2602.06843"},{"title":"Symmetry in language statistics shapes the geometry of model representations","url":"https://arxiv.org/html/2602.15029v1"},{"title":"Change-resistance distinguishes the representational geometries of human spatial memory and mouse CA1 in deformed environments","url":"https://www.biorxiv.org/content/10.1101/2025.07.09.663962.full.pdf"},{"title":"Representational geometry explains puzzling error distributions in behavioral tasks","url":"https://www.biorxiv.org/content/10.1101/2023.01.03.522667.full.pdf"},{"title":"Representational geometry: integrating cognition, computation, and the brain","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3730178/"},{"title":"The representational geometry for naturalistic textures in macaque V1 and V2","url":"https://www.biorxiv.org/content/10.1101/2024.10.18.619102.full.pdf"}]

I found a paper with ID 2602.06843, but not 2602.08159. Let me search specifically for the paper using a different approach.

Links: [{"title":"[2604.08159] Face-D(^2)CL: Multi-Domain Synergistic Representation with Dual Continual Learning for Facial DeepFake Detection","url":"https://arxiv.org/abs/2604.08159"},{"title":"Fine-tuned large language models enhance influenza forecasting","url":"https://www.medrxiv.org/content/10.1101/2025.03.27.25324747.full.pdf"},{"title":"LeafyResNet: Fusarium Wilt Detection in Lettuce Using UAV RGB Imaging and Advanced Deep Learning Model","url":"https://www.biorxiv.org/content/10.1101/2025.05.21.655416.full.pdf"},{"title":"Detection of patient metadata in published articles for genomic epidemiology using machine learning and large language models","url":"https://www.medrxiv.org/content/10.1101/2025.04.25.25326298.full.pdf"},{"title":"Privacy-Enhancing Sequential Learning under Heterogeneous Selection Bias in Multi-Site EHR Data","url":"https://www.medrxiv.org/content/10.1101/2025.09.26.25336642.full.pdf"},{"title":"Unsupervised cross-domain data augmentation for long-document based prediction and explanation","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12321841"}]

I found a paper with ID 2604.08159, but not 2602.08159. Let me try one more specific search to find this exact paper.

Links: [{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/pdf/2602.08159"},{"title":"The Geometry of Forgetting: Temporal Knowledge Drift as an Independent Axis in LLM Representations","url":"https://arxiv.org/html/2605.09195"},{"title":"Concept Probing and Representation Analysis","url":"https://apxml.com/courses/llm-alignment-safety/chapter-6-interpretability-monitoring-safety/concept-probing-representation-analysis"},{"title":"The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets | OpenReview","url":"https://openreview.net/forum?id=CeJEfNKstt"},{"title":"Predicting LLM Answer Accuracy from Question-Only ...","url":"https://arxiv.org/pdf/2509.10625"},{"title":"The Geometry of Truth: Emergent Linear Structure in Large Language Model   Representations of True/False Datasets","url":"https://arxiv.org/pdf/2310.06824"},{"title":"Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling","url":"https://arxiv.org/html/2604.13386v1"},{"title":"Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation","url":"https://arxiv.org/html/2512.22245v1"}]

Perfect! I found the paper. Here's what I found about arXiv paper 2602.08159:

## Paper Summary

The paper characterizes the geometry of correctness representations in transformer activations. The paper is titled "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models."

### Key Findings

Analyzing 9 models from 5 architecture families, the paper finds the discriminative signal is simple: it occupies 3–8 dimensions, performance decreases with additional dimensions, and no nonlinear classifier improves over linear probes. The optimal decision boundary is a hyperplane; complex boundaries model structure that does not exist.

### Validation and Performance

The authors validate causally through activation steering: the learned direction produces 10.9 percentage point changes in error rates while random directions show no effect. Internal probes achieve 0.80-0.97 AUC; output-based methods (P(True), semantic entropy) achieve only 0.44–0.64 AUC. The correctness signal exists internally but is not expressed in outputs.

### Geometric Structure

Centroid distance matches probe performance indicates class separation is a mean shift, making detection geometric rather than learned.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91b66ffe-86b9-4a35-9752-209e1567ec16",
  "isSidechain": false,
  "promptId": "cfd26950-1158-49a2-b94b-ad272b2bb26f",
  "type": "user",
  "uuid": "2497da07-175e-4331-90e9-59f4d5fdb5a1",
  "toolUseResult": {
    "query": "arXiv 2602.08159 LLM correctness linear probe representational geometry 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0173bFdabYEbMguk4nvT797z",
        "content": [
          {
            "title": "Predicting LLM Answer Accuracy from Question-Only ...",
            "url": "https://arxiv.org/pdf/2509.10625"
          },
          {
            "title": "Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation",
            "url": "https://arxiv.org/html/2512.22245"
          },
          {
            "title": "Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation",
            "url": "https://arxiv.org/pdf/2512.22245"
          },
          {
            "title": "No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes | OpenReview",
            "url": "https://openreview.net/forum?id=OhN25uxVab"
          },
          {
            "title": "Can Linear Probes Measure LLM Uncertainty ?",
            "url": "https://arxiv.org/html/2510.04108"
          }
        ]
      },
      "I didn't find the specific arXiv paper 2602.08159 in those results. Let me search more directly for that paper ID.",
      {
        "tool_use_id": "srvtoolu_01WNJCd7FKg9ZmYoYsyvzrcr",
        "content": [
          {
            "title": "Detection of patient metadata in published articles for genomic epidemiology using machine learning and large language models",
            "url": "https://www.medrxiv.org/content/10.1101/2025.04.25.25326298.full.pdf"
          },
          {
            "title": "Association between TM6SF2 rs58542926 T/C gene polymorphism and significant liver fibrosis: A meta-analysis",
            "url": "https://www.medrxiv.org/content/10.1101/2020.10.11.20210690.full.pdf"
          },
          {
            "title": "Unsupervised cross-domain data augmentation for long-document based prediction and explanation",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12321841"
          },
          {
            "title": "Dual-Model LLM Ensemble via Web Chat Interfaces Reaches Near-Perfect Sensitivity for Systematic-Review Screening: A Multi-Domain Validation with Equivalence to API Access",
            "url": "https://www.medrxiv.org/content/10.1101/2025.11.03.25339455.full.pdf"
          },
          {
            "title": "LeafyResNet: Fusarium Wilt Detection in Lettuce Using UAV RGB Imaging and Advanced Deep Learning Model",
            "url": "https://www.biorxiv.org/content/10.1101/2025.05.21.655416.full.pdf"
          }
        ]
      },
      "The results don't appear to contain the specific arXiv paper 2602.08159. Let me try a more targeted search for this paper.",
      {
        "tool_use_id": "srvtoolu_01JovrFerEySUSQvs2RZiqY8",
        "content": [
          {
            "title": "When do measured representational distances reflect the neural representational geometry?",
            "url": "https://www.biorxiv.org/content/10.1101/2024.12.30.630743.full.pdf"
          },
          {
            "title": "The Representational Geometry of Number",
            "url": "https://arxiv.org/html/2602.06843"
          },
          {
            "title": "Symmetry in language statistics shapes the geometry of model representations",
            "url": "https://arxiv.org/html/2602.15029v1"
          },
          {
            "title": "Change-resistance distinguishes the representational geometries of human spatial memory and mouse CA1 in deformed environments",
            "url": "https://www.biorxiv.org/content/10.1101/2025.07.09.663962.full.pdf"
          },
          {
            "title": "Representational geometry explains puzzling error distributions in behavioral tasks",
            "url": "https://www.biorxiv.org/content/10.1101/2023.01.03.522667.full.pdf"
          },
          {
            "title": "Representational geometry: integrating cognition, computation, and the brain",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3730178/"
          },
          {
            "title": "The representational geometry for naturalistic textures in macaque V1 and V2",
            "url": "https://www.biorxiv.org/content/10.1101/2024.10.18.619102.full.pdf"
          }
        ]
      },
      "I found a paper with ID 2602.06843, but not 2602.08159. Let me search specifically for the paper using a different approach.",
      {
        "tool_use_id": "srvtoolu_01TTw2qS7wvEJVWaLw1PFzxi",
        "content": [
          {
            "title": "[2604.08159] Face-D(^2)CL: Multi-Domain Synergistic Representation with Dual Continual Learning for Facial DeepFake Detection",
            "url": "https://arxiv.org/abs/2604.08159"
          },
          {
            "title": "Fine-tuned large language models enhance influenza forecasting",
            "url": "https://www.medrxiv.org/content/10.1101/2025.03.27.25324747.full.pdf"
          },
          {
            "title": "LeafyResNet: Fusarium Wilt Detection in Lettuce Using UAV RGB Imaging and Advanced Deep Learning Model",
            "url": "https://www.biorxiv.org/content/10.1101/2025.05.21.655416.full.pdf"
          },
          {
            "title": "Detection of patient metadata in published articles for genomic epidemiology using machine learning and large language models",
            "url": "https://www.medrxiv.org/content/10.1101/2025.04.25.25326298.full.pdf"
          },
          {
            "title": "Privacy-Enhancing Sequential Learning under Heterogeneous Selection Bias in Multi-Site EHR Data",
            "url": "https://www.medrxiv.org/content/10.1101/2025.09.26.25336642.full.pdf"
          },
          {
            "title": "Unsupervised cross-domain data augmentation for long-document based prediction and explanation",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12321841"
          }
        ]
      },
      "I found a paper with ID 2604.08159, but not 2602.08159. Let me try one more specific search to find this exact paper.",
      {
        "tool_use_id": "srvtoolu_01Akq213SyjVv2cdkpNyiiBC",
        "content": [
          {
            "title": "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models",
            "url": "https://arxiv.org/pdf/2602.08159"
          },
          {
            "title": "The Geometry of Forgetting: Temporal Knowledge Drift as an Independent Axis in LLM Representations",
            "url": "https://arxiv.org/html/2605.09195"
          },
          {
            "title": "Concept Probing and Representation Analysis",
            "url": "https://apxml.com/courses/llm-alignment-safety/chapter-6-interpretability-monitoring-safety/concept-probing-representation-analysis"
          },
          {
            "title": "The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets | OpenReview",
            "url": "https://openreview.net/forum?id=CeJEfNKstt"
          },
          {
            "title": "Predicting LLM Answer Accuracy from Question-Only ...",
            "url": "https://arxiv.org/pdf/2509.10625"
          },
          {
            "title": "The Geometry of Truth: Emergent Linear Structure in Large Language Model   Representations of True/False Datasets",
            "url": "https://arxiv.org/pdf/2310.06824"
          },
          {
            "title": "Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling",
            "url": "https://arxiv.org/html/2604.13386v1"
          },
          {
            "title": "Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation",
            "url": "https://arxiv.org/html/2512.22245v1"
          }
        ]
      },
      "Perfect! I found the paper. Here's what I found about arXiv paper 2602.08159:\n\n## Paper Summary\n\nThe paper characterizes the geometry of correctness representations in transformer activations. The paper is titled \"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models.\"\n\n### Key Findings\n\nAnalyzing 9 models from 5 architecture families, the paper finds the discriminative signal is simple: it occupies 3–8 dimensions, performance decreases with additional dimensions, and no nonlinear classifier improves over linear probes. The optimal decision boundary is a hyperplane; complex boundaries model structure that does not exist.\n\n### Validation and Performance\n\nThe authors validate causally through activation steering: the learned direction produces 10.9 percentage point changes in error rates while random directions show no effect. Internal probes achieve 0.80-0.97 AUC; output-based methods (P(True), semantic entropy) achieve only 0.44–0.64 AUC. The correctness signal exists internally but is not expressed in outputs.\n\n### Geometric Structure\n\nCentroid distance matches probe performance indicates class separation is a mean shift, making detection geometric rather than learned."
    ],
    "durationSeconds": 18.31808888999999,
    "searchCount": 5
  },
  "sourceToolAssistantUUID": "91b66ffe-86b9-4a35-9752-209e1567ec16",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T03:27:11.207Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Jx6VwEyUwHYF1U7h11vEBK`</summary>

```json
{
  "query": "arXiv 2601.00828 error depth hypothesis LLM self-correction decomposing 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2497da07-175e-4331-90e9-59f4d5fdb5a1",
  "isSidechain": false,
  "requestId": "req_011CbD7HarQ8JPTaTWbDhJq5",
  "type": "assistant",
  "uuid": "6fb6c62c-1680-41f3-a33f-feb6286e6f95",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GnLY4Q8T9CX9r2w9gCSUvg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2145,
      "cache_read_input_tokens": 20420,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2145,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 20420,
          "cache_creation_input_tokens": 2145,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2145
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

_source line 25 · 2026-05-20T03:27:20.747Z_

<details><summary>↩ Tool result · `toolu_01Jx6VwEyUwHYF1U7h11vEBK`</summary>

```text
Web search results for query: "arXiv 2601.00828 error depth hypothesis LLM self-correction decomposing 2026"

Links: [{"title":"[2601.00828] Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis","url":"https://arxiv.org/abs/2601.00828"},{"title":"Decomposing LLM Self-Correction:","url":"https://arxiv.org/pdf/2601.00828"},{"title":"Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis","url":"https://arxiv.org/html/2601.00828"},{"title":"Confidence v.s. Critique: A Decomposition of Self-Correction Capability   for LLMs","url":"https://arxiv.org/pdf/2412.19513"},{"title":"Structure Enables Effective Self-Localization of Errors in LLMs","url":"https://arxiv.org/pdf/2602.02416"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://arxiv.org/html/2406.01297v3"},{"title":"Unleashing the True Potential of LLMs: A Feedback-Triggered Self-Correction with Long-Term Multipath Decoding","url":"https://arxiv.org/html/2509.07676"},{"title":"A Probabilistic Inference Scaling Theory for LLM Self-Correction","url":"https://arxiv.org/pdf/2508.16456"},{"title":"Self-Correction Makes LLMs Better Parsers","url":"https://arxiv.org/pdf/2504.14165"}]

Based on the search results, here's what I found about arXiv paper 2601.00828:

## Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis

Large Language Models (LLMs) are widely believed to possess self-correction capabilities, yet recent studies suggest that intrinsic self-correction--where models correct their own outputs without external feedback--remains largely ineffective.

**Key Contributions:**

The work systematically decomposes self-correction into three distinct sub-capabilities: error detection, error localization, and error correction.

**Main Findings:**

Through cross-model experiments on GSM8K-Complex (n=500 per model, 346 total errors) with three major LLMs, the research uncovers a striking Accuracy-Correction Paradox: weaker models (GPT-3.5, 66% accuracy) achieve 1.6x higher intrinsic correction rates than stronger models (DeepSeek, 94% accuracy)--26.8% vs 16.7%.

**The Error Depth Hypothesis:**

The researchers propose the Error Depth Hypothesis: stronger models make fewer but deeper errors that resist self-correction.

The paper was submitted to arXiv on December 24, 2025, and provides a novel framework for understanding the limitations of LLMs in correcting their own errors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fb6c62c-1680-41f3-a33f-feb6286e6f95",
  "isSidechain": false,
  "promptId": "cfd26950-1158-49a2-b94b-ad272b2bb26f",
  "type": "user",
  "uuid": "9a0aae61-5e29-4e91-8476-4e96d8cdb19f",
  "toolUseResult": {
    "query": "arXiv 2601.00828 error depth hypothesis LLM self-correction decomposing 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PjLE85gfvztT21P1NmSNG9",
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
            "title": "Confidence v.s. Critique: A Decomposition of Self-Correction Capability   for LLMs",
            "url": "https://arxiv.org/pdf/2412.19513"
          },
          {
            "title": "Structure Enables Effective Self-Localization of Errors in LLMs",
            "url": "https://arxiv.org/pdf/2602.02416"
          },
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs",
            "url": "https://arxiv.org/html/2406.01297v3"
          },
          {
            "title": "Unleashing the True Potential of LLMs: A Feedback-Triggered Self-Correction with Long-Term Multipath Decoding",
            "url": "https://arxiv.org/html/2509.07676"
          },
          {
            "title": "A Probabilistic Inference Scaling Theory for LLM Self-Correction",
            "url": "https://arxiv.org/pdf/2508.16456"
          },
          {
            "title": "Self-Correction Makes LLMs Better Parsers",
            "url": "https://arxiv.org/pdf/2504.14165"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2601.00828:\n\n## Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis\n\nLarge Language Models (LLMs) are widely believed to possess self-correction capabilities, yet recent studies suggest that intrinsic self-correction--where models correct their own outputs without external feedback--remains largely ineffective.\n\n**Key Contributions:**\n\nThe work systematically decomposes self-correction into three distinct sub-capabilities: error detection, error localization, and error correction.\n\n**Main Findings:**\n\nThrough cross-model experiments on GSM8K-Complex (n=500 per model, 346 total errors) with three major LLMs, the research uncovers a striking Accuracy-Correction Paradox: weaker models (GPT-3.5, 66% accuracy) achieve 1.6x higher intrinsic correction rates than stronger models (DeepSeek, 94% accuracy)--26.8% vs 16.7%.\n\n**The Error Depth Hypothesis:**\n\nThe researchers propose the Error Depth Hypothesis: stronger models make fewer but deeper errors that resist self-correction.\n\nThe paper was submitted to arXiv on December 24, 2025, and provides a novel framework for understanding the limitations of LLMs in correcting their own errors."
    ],
    "durationSeconds": 9.534315786999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6fb6c62c-1680-41f3-a33f-feb6286e6f95",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "9a0aae61-5e29-4e91-8476-4e96d8cdb19f",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM correctability prediction proposal",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be"
}
```

---

### Tool call

_source line 28 · 2026-05-20T03:27:24.217Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JH84vYHyT2rwNvdPy5e1pi`</summary>

```json
{
  "query": "arXiv 2510.04128 Wait token mechanism crosscoder LLM hidden state 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a0aae61-5e29-4e91-8476-4e96d8cdb19f",
  "isSidechain": false,
  "requestId": "req_011CbD7JVePZWKvwHWbuR1A1",
  "type": "assistant",
  "uuid": "050ca074-013b-4333-a675-288d65463305",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017WeaUYCCGbHmc3gqLzruFf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 22565,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 853,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 22565,
          "cache_creation_input_tokens": 853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 853
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

_source line 29 · 2026-05-20T03:27:31.383Z_

<details><summary>↩ Tool result · `toolu_01JH84vYHyT2rwNvdPy5e1pi`</summary>

```text
Web search results for query: "arXiv 2510.04128 Wait token mechanism crosscoder LLM hidden state 2025"

Links: [{"title":"[2510.04128] Internal states before wait modulate reasoning patterns","url":"https://arxiv.org/abs/2510.04128"},{"title":"Oops, Wait: Token-Level Signals as a Lens into LLM Reasoning","url":"https://arxiv.org/pdf/2601.17421"},{"title":"Internal states before wait modulate reasoning patterns","url":"https://arxiv.org/html/2510.04128"},{"title":"Internal states before wait modulate reasoning patterns","url":"https://arxiv.org/pdf/2510.04128"},{"title":"CrossLMM: Decoupling Long Video Sequences from LMMs via Dual Cross-Attention Mechanisms","url":"https://arxiv.org/pdf/2505.17020"},{"title":"Behavior-Equivalent Token: Single-Token Replacement for Long Prompts in LLMs","url":"https://arxiv.org/pdf/2511.23271"}]

Based on the search results, here's what I found about arXiv paper 2510.04128:

The paper is titled "Internal states before wait modulate reasoning patterns", published on October 5, 2025.

**Research Focus:**

The work addresses whether model latents preceding wait tokens contain relevant information for modulating the subsequent reasoning process. The token "wait" often signals reasoning behavior such as backtracking.

**Methodology:**

The researchers train crosscoders at multiple layers of DeepSeek-R1-Distill-Llama-8B and its base version, and introduce a latent attribution technique in the crosscoder setting. Their crosscoder latent attribution method efficiently scores 32,768 features regarding their contribution to the logits of wait tokens.

**Key Findings:**

They locate a small set of features relevant for promoting/suppressing wait tokens' probabilities, and through experiments analyzing max-activating examples and causal interventions, show that many identified features are relevant for the reasoning process and give rise to different types of reasoning patterns such as restarting from the beginning, recalling prior knowledge, expressing uncertainty, and double-checking.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "050ca074-013b-4333-a675-288d65463305",
  "isSidechain": false,
  "promptId": "cfd26950-1158-49a2-b94b-ad272b2bb26f",
  "type": "user",
  "uuid": "34b5a6ae-1f90-41fb-aa37-55090f151d68",
  "toolUseResult": {
    "query": "arXiv 2510.04128 Wait token mechanism crosscoder LLM hidden state 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_0142fKsN9CduxXYHbDubiemz",
        "content": [
          {
            "title": "[2510.04128] Internal states before wait modulate reasoning patterns",
            "url": "https://arxiv.org/abs/2510.04128"
          },
          {
            "title": "Oops, Wait: Token-Level Signals as a Lens into LLM Reasoning",
            "url": "https://arxiv.org/pdf/2601.17421"
          },
          {
            "title": "Internal states before wait modulate reasoning patterns",
            "url": "https://arxiv.org/html/2510.04128"
          },
          {
            "title": "Internal states before wait modulate reasoning patterns",
            "url": "https://arxiv.org/pdf/2510.04128"
          },
          {
            "title": "CrossLMM: Decoupling Long Video Sequences from LMMs via Dual Cross-Attention Mechanisms",
            "url": "https://arxiv.org/pdf/2505.17020"
          },
          {
            "title": "Behavior-Equivalent Token: Single-Token Replacement for Long Prompts in LLMs",
            "url": "https://arxiv.org/pdf/2511.23271"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2510.04128:\n\nThe paper is titled \"Internal states before wait modulate reasoning patterns\", published on October 5, 2025.\n\n**Research Focus:**\n\nThe work addresses whether model latents preceding wait tokens contain relevant information for modulating the subsequent reasoning process. The token \"wait\" often signals reasoning behavior such as backtracking.\n\n**Methodology:**\n\nThe researchers train crosscoders at multiple layers of DeepSeek-R1-Distill-Llama-8B and its base version, and introduce a latent attribution technique in the crosscoder setting. Their crosscoder latent attribution method efficiently scores 32,768 features regarding their contribution to the logits of wait tokens.\n\n**Key Findings:**\n\nThey locate a small set of features relevant for promoting/suppressing wait tokens' probabilities, and through experiments analyzing max-activating examples and causal interventions, show that many identified features are relevant for the reasoning process and give rise to different types of reasoning patterns such as restarting from the beginning, recalling prior knowledge, expressing uncertainty, and double-checking."
    ],
    "durationSeconds": 7.162020854000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "050ca074-013b-4333-a675-288d65463305",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-20T03:27:31.391Z_

```json
{
  "parentUuid": "34b5a6ae-1f90-41fb-aa37-55090f151d68",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "aabfaa98-9065-4285-990c-b09ce740aad5",
  "timestamp": "2026-05-20T03:27:31.391Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-20T03:27:34.980Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012q8f1bwJqJeTLJJ76Vappu`</summary>

```json
{
  "query": "\"LLMs encode their failures\" predicting success pre-generation activations correctability probing 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aabfaa98-9065-4285-990c-b09ce740aad5",
  "isSidechain": false,
  "requestId": "req_011CbD7KH9qHs24eY33L7LTV",
  "type": "assistant",
  "uuid": "dbfddffc-1d01-46a5-8e93-ccd867c1bec8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J9HAiG8X9bk4XHiH96Jd18",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 23418,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 23418,
          "cache_creation_input_tokens": 723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 723
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

_source line 32 · 2026-05-20T03:27:41.561Z_

<details><summary>↩ Tool result · `toolu_012q8f1bwJqJeTLJJ76Vappu`</summary>

```text
Web search results for query: ""LLMs encode their failures" predicting success pre-generation activations correctability probing 2026"

Links: [{"title":"LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations","url":"https://arxiv.org/html/2602.09924"},{"title":"[2602.09924] LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations","url":"https://arxiv.org/abs/2602.09924"},{"title":"llms encode their failures: predicting suc","url":"https://arxiv.org/pdf/2602.09924"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/pdf/2512.20578"},{"title":"No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes","url":"https://arxiv.org/pdf/2509.10625"},{"title":"[2512.20578] Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/abs/2512.20578"},{"title":"Why LLMs Fail: A Failure Analysis and Partial Success Measurement for Automated Security Patch Generation","url":"https://arxiv.org/html/2603.10072v1"}]

I found the research paper matching your query! Here are the key findings:

## LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations

LLMs internally encode estimates of their own success in pre-generation activations, and these estimates can be efficiently extracted using linear probes.

**Key Research Results:**

- Linear probes trained on pre-generation activations predict policy-specific success on math and coding tasks, substantially outperforming surface features such as question length and TF-IDF.

- Models encode a model-specific notion of difficulty that is distinct from human difficulty, and this distinction increases with extended reasoning.

- Routing queries across a pool of models can exceed the performance of the best-performing model whilst reducing inference cost by up to 70% on MATH.

**Study Details:**

The empirical study spans mathematics (MATH, GSM8K, AIME, E2H-AMC) and coding (LiveCodeBench) domains, training linear probes on pre-generation activations to predict success under various decoding policies. The paper was accepted at the ICLR 2026 LIT Workshop.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbfddffc-1d01-46a5-8e93-ccd867c1bec8",
  "isSidechain": false,
  "promptId": "cfd26950-1158-49a2-b94b-ad272b2bb26f",
  "type": "user",
  "uuid": "532064b0-25ba-469d-a0e4-eb97b8437705",
  "toolUseResult": {
    "query": "\"LLMs encode their failures\" predicting success pre-generation activations correctability probing 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VBUJPCM8VsGNV8rK8kxW6V",
        "content": [
          {
            "title": "LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations",
            "url": "https://arxiv.org/html/2602.09924"
          },
          {
            "title": "[2602.09924] LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations",
            "url": "https://arxiv.org/abs/2602.09924"
          },
          {
            "title": "llms encode their failures: predicting suc",
            "url": "https://arxiv.org/pdf/2602.09924"
          },
          {
            "title": "Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/pdf/2512.20578"
          },
          {
            "title": "No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes",
            "url": "https://arxiv.org/pdf/2509.10625"
          },
          {
            "title": "[2512.20578] Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/abs/2512.20578"
          },
          {
            "title": "Why LLMs Fail: A Failure Analysis and Partial Success Measurement for Automated Security Patch Generation",
            "url": "https://arxiv.org/html/2603.10072v1"
          }
        ]
      },
      "I found the research paper matching your query! Here are the key findings:\n\n## LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations\n\nLLMs internally encode estimates of their own success in pre-generation activations, and these estimates can be efficiently extracted using linear probes.\n\n**Key Research Results:**\n\n- Linear probes trained on pre-generation activations predict policy-specific success on math and coding tasks, substantially outperforming surface features such as question length and TF-IDF.\n\n- Models encode a model-specific notion of difficulty that is distinct from human difficulty, and this distinction increases with extended reasoning.\n\n- Routing queries across a pool of models can exceed the performance of the best-performing model whilst reducing inference cost by up to 70% on MATH.\n\n**Study Details:**\n\nThe empirical study spans mathematics (MATH, GSM8K, AIME, E2H-AMC) and coding (LiveCodeBench) domains, training linear probes on pre-generation activations to predict success under various decoding policies. The paper was accepted at the ICLR 2026 LIT Workshop."
    ],
    "durationSeconds": 6.573224119000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "dbfddffc-1d01-46a5-8e93-ccd867c1bec8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T03:27:44.233Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013D8FFt7sjaqKhRDfam6v3z`</summary>

```json
{
  "query": "LLM self-correction Wait baseline overcorrection cost probe-gated correction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "532064b0-25ba-469d-a0e4-eb97b8437705",
  "isSidechain": false,
  "requestId": "req_011CbD7L2eEkFxfYpXWTS4sC",
  "type": "assistant",
  "uuid": "408d590a-ee2d-488c-a1ef-320f88333c6d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9yu7YsrHZfxGH6YVhUiHB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 24141,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 693,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 24141,
          "cache_creation_input_tokens": 693,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 693
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

_source line 34 · 2026-05-20T03:27:55.800Z_

<details><summary>↩ Tool result · `toolu_013D8FFt7sjaqKhRDfam6v3z`</summary>

```text
Web search results for query: "LLM self-correction Wait baseline overcorrection cost probe-gated correction 2025 2026"

Links: [{"title":"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs | OpenReview","url":"https://openreview.net/forum?id=956KYtqwcU"},{"title":"Self-Correction Bench for LLMs","url":"https://www.emergentmind.com/topics/self-correction-bench"},{"title":"[2510.16062] Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs","url":"https://arxiv.org/abs/2510.16062"},{"title":"Self-Correction Bench: Revealing and Addressing the Self-Correction Blind Spot in LLMs","url":"https://arxiv.org/html/2507.02778v1"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/When-Can-LLMs-Actually-Correct-Their-Own-Mistakes"},{"title":"Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis","url":"https://arxiv.org/pdf/2601.00828"},{"title":"CorrectBench: A Benchmark of Self-Correction in LLMs","url":"https://correctbench.github.io/"},{"title":"Self-Correction Makes LLMs Better Parsers","url":"https://arxiv.org/pdf/2504.14165"}]

Based on the web search results, I found several relevant papers and research on LLM self-correction from 2025-2026. Here are the key findings:

## Key Research on LLM Self-Correction

**CorrectBench Benchmark (2025)**
CorrectBench is the first comprehensive benchmark for evaluating self-correction mechanisms in LLMs, assessing effectiveness across commonsense reasoning, mathematical reasoning, and code generation tasks. While self-correction strategies achieve 5.2% accuracy gains on complex mathematical reasoning (MATH dataset), hybrid approaches incur significant efficiency costs (≈40% slower than baseline).

**The "Wait" Marker Intervention**
A critical intervention discovered is the use of correction "markers"—single tokens or phrases appended after an incorrect answer (e.g., "Wait"), which dramatically increases self-correction probability: appending "Wait" after incorrect output reduces average blind spot by 89.3% and increases accuracy by +156.0% across models and datasets.

**Self-Correction Blind Spot**
The "self-correction blind spot" is a phenomenon where a model fails to rectify errors present in its own output, despite being able to address numerically identical errors if supplied as user input.

**Accuracy-Correction Paradox (January 2026)**
Recent research uncovered an "Accuracy-Correction Paradox": weaker models (GPT-3.5, 66% accuracy) achieve 1.6× higher intrinsic correction rates than stronger models (DeepSeek, 94% accuracy)—26.8% vs 16.7%.

The research from 2025-2026 suggests that while self-correction holds promise for improving LLM performance, efficiency costs and inherent limitations in error detection remain significant challenges.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "408d590a-ee2d-488c-a1ef-320f88333c6d",
  "isSidechain": false,
  "promptId": "cfd26950-1158-49a2-b94b-ad272b2bb26f",
  "type": "user",
  "uuid": "8596900c-7e04-4360-ae8c-fe3ef5b4bb25",
  "toolUseResult": {
    "query": "LLM self-correction Wait baseline overcorrection cost probe-gated correction 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0154uArxDu4xccCrCz6RMhWT",
        "content": [
          {
            "title": "Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs | OpenReview",
            "url": "https://openreview.net/forum?id=956KYtqwcU"
          },
          {
            "title": "Self-Correction Bench for LLMs",
            "url": "https://www.emergentmind.com/topics/self-correction-bench"
          },
          {
            "title": "[2510.16062] Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs",
            "url": "https://arxiv.org/abs/2510.16062"
          },
          {
            "title": "Self-Correction Bench: Revealing and Addressing the Self-Correction Blind Spot in LLMs",
            "url": "https://arxiv.org/html/2507.02778v1"
          },
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs | Transactions of the Association for Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/When-Can-LLMs-Actually-Correct-Their-Own-Mistakes"
          },
          {
            "title": "Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis",
            "url": "https://arxiv.org/pdf/2601.00828"
          },
          {
            "title": "CorrectBench: A Benchmark of Self-Correction in LLMs",
            "url": "https://correctbench.github.io/"
          },
          {
            "title": "Self-Correction Makes LLMs Better Parsers",
            "url": "https://arxiv.org/pdf/2504.14165"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers and research on LLM self-correction from 2025-2026. Here are the key findings:\n\n## Key Research on LLM Self-Correction\n\n**CorrectBench Benchmark (2025)**\nCorrectBench is the first comprehensive benchmark for evaluating self-correction mechanisms in LLMs, assessing effectiveness across commonsense reasoning, mathematical reasoning, and code generation tasks. While self-correction strategies achieve 5.2% accuracy gains on complex mathematical reasoning (MATH dataset), hybrid approaches incur significant efficiency costs (≈40% slower than baseline).\n\n**The \"Wait\" Marker Intervention**\nA critical intervention discovered is the use of correction \"markers\"—single tokens or phrases appended after an incorrect answer (e.g., \"Wait\"), which dramatically increases self-correction probability: appending \"Wait\" after incorrect output reduces average blind spot by 89.3% and increases accuracy by +156.0% across models and datasets.\n\n**Self-Correction Blind Spot**\nThe \"self-correction blind spot\" is a phenomenon where a model fails to rectify errors present in its own output, despite being able to address numerically identical errors if supplied as user input.\n\n**Accuracy-Correction Paradox (January 2026)**\nRecent research uncovered an \"Accuracy-Correction Paradox\": weaker models (GPT-3.5, 66% accuracy) achieve 1.6× higher intrinsic correction rates than stronger models (DeepSeek, 94% accuracy)—26.8% vs 16.7%.\n\nThe research from 2025-2026 suggests that while self-correction holds promise for improving LLM performance, efficiency costs and inherent limitations in error detection remain significant challenges."
    ],
    "durationSeconds": 11.562717378,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "408d590a-ee2d-488c-a1ef-320f88333c6d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T03:27:58.382Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015C3V4Jc97am2oXteaeJ492`</summary>

```json
{
  "query": "Reflective Confidence LLM self-correction PAG probe-guided abstain gating hidden state 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8596900c-7e04-4360-ae8c-fe3ef5b4bb25",
  "isSidechain": false,
  "requestId": "req_011CbD7M5Uv9rY6VrnRAKn9Z",
  "type": "assistant",
  "uuid": "fab09950-6b78-4a99-9be9-54ed516f2816",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TndFvAo1AYJE3tJW8drUwx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 937,
      "cache_read_input_tokens": 24834,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 937,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 24834,
          "cache_creation_input_tokens": 937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 937
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

_source line 36 · 2026-05-20T03:28:06.981Z_

<details><summary>↩ Tool result · `toolu_015C3V4Jc97am2oXteaeJ492`</summary>

```text
Web search results for query: "Reflective Confidence LLM self-correction PAG probe-guided abstain gating hidden state 2025 2026"

Links: [{"title":"PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier","url":"https://jackory.github.io/pag/"},{"title":"PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier","url":"https://arxiv.org/pdf/2506.10406"},{"title":"Confidence-Based Response Abstinence: Improving LLM Trustworthiness via Activation-Based Uncertainty Estimation","url":"https://arxiv.org/pdf/2510.13750"},{"title":"Confidence v.s. Critique: A Decomposition of Self-Correction Capability   for LLMs","url":"https://arxiv.org/pdf/2412.19513"},{"title":"REFLECTIVE CONFIDENCE: CORRECTING REASONING FLAWS VIA ONLINE SELF-CORRECTION","url":"https://arxiv.org/pdf/2512.18605"}]

Based on the search results, I found relevant information about these topics:

## PAG: Multi-Turn Reinforced LLM Self-Correction

Policy as Generative Verifier (PAG) is a framework that empowers LLMs to self-correct where a single model alternates between policy and generative verifier roles. PAG introduces a selective revision mechanism where the model revises its answer only when its own generative verification step detects an error. The paper was published on September 2, 2025.

## Reflective Confidence

ReflectiveConf is a proposed method that triggers a reflect-and-correct procedure and surpasses Self-Consistency in accuracy and efficiency. The approach utilizes the model's internal confidence signals to evaluate the quality of reasoning paths in real-time, enabling more efficient inference.

## Related Research on Confidence and Self-Correction

Recent research decomposes self-correction capability into confidence and critique capacities, with metrics to measure both.

The search results show active research in 2025-2026 on using confidence mechanisms and internal model states (hidden states) to guide self-correction in LLMs, with approaches like PAG and ReflectiveConf representing the current frontier in this area.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fab09950-6b78-4a99-9be9-54ed516f2816",
  "isSidechain": false,
  "promptId": "cfd26950-1158-49a2-b94b-ad272b2bb26f",
  "type": "user",
  "uuid": "70039b1f-8499-419d-989b-168fa864f3aa",
  "toolUseResult": {
    "query": "Reflective Confidence LLM self-correction PAG probe-guided abstain gating hidden state 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_015apqdL1g6c6L4KXr5WAHDc",
        "content": [
          {
            "title": "PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier",
            "url": "https://jackory.github.io/pag/"
          },
          {
            "title": "PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier",
            "url": "https://arxiv.org/pdf/2506.10406"
          },
          {
            "title": "Confidence-Based Response Abstinence: Improving LLM Trustworthiness via Activation-Based Uncertainty Estimation",
            "url": "https://arxiv.org/pdf/2510.13750"
          },
          {
            "title": "Confidence v.s. Critique: A Decomposition of Self-Correction Capability   for LLMs",
            "url": "https://arxiv.org/pdf/2412.19513"
          },
          {
            "title": "REFLECTIVE CONFIDENCE: CORRECTING REASONING FLAWS VIA ONLINE SELF-CORRECTION",
            "url": "https://arxiv.org/pdf/2512.18605"
          }
        ]
      },
      "Based on the search results, I found relevant information about these topics:\n\n## PAG: Multi-Turn Reinforced LLM Self-Correction\n\nPolicy as Generative Verifier (PAG) is a framework that empowers LLMs to self-correct where a single model alternates between policy and generative verifier roles. PAG introduces a selective revision mechanism where the model revises its answer only when its own generative verification step detects an error. The paper was published on September 2, 2025.\n\n## Reflective Confidence\n\nReflectiveConf is a proposed method that triggers a reflect-and-correct procedure and surpasses Self-Consistency in accuracy and efficiency. The approach utilizes the model's internal confidence signals to evaluate the quality of reasoning paths in real-time, enabling more efficient inference.\n\n## Related Research on Confidence and Self-Correction\n\nRecent research decomposes self-correction capability into confidence and critique capacities, with metrics to measure both.\n\nThe search results show active research in 2025-2026 on using confidence mechanisms and internal model states (hidden states) to guide self-correction in LLMs, with approaches like PAG and ReflectiveConf representing the current frontier in this area."
    ],
    "durationSeconds": 8.594623504000017,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fab09950-6b78-4a99-9be9-54ed516f2816",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T03:28:09.558Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0192X2pHpoNPA2RhQncYss6V`</summary>

```json
{
  "query": "correctability prediction LLM which errors are fixable self-correctable internal probe 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70039b1f-8499-419d-989b-168fa864f3aa",
  "isSidechain": false,
  "requestId": "req_011CbD7MuPUaXJRwtBVqPMsE",
  "type": "assistant",
  "uuid": "97bd659e-8f4d-4e72-a394-1573792a9105",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQqwGJ4Lp4YhR3y6KmvsmL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 656,
      "cache_read_input_tokens": 25771,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 25771,
          "cache_creation_input_tokens": 656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 656
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

_source line 38 · 2026-05-20T03:28:18.723Z_

<details><summary>↩ Tool result · `toolu_0192X2pHpoNPA2RhQncYss6V`</summary>

```text
Web search results for query: "correctability prediction LLM which errors are fixable self-correctable internal probe 2025 2026"

Links: [{"title":"How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals","url":"https://arxiv.org/html/2604.22271v1"},{"title":"[2512.20578] Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/abs/2512.20578"},{"title":"Know When You’re Wrong: Aligning Confidence with Correctness for LLM Error Detection","url":"https://arxiv.org/html/2603.06604"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"},{"title":"[2601.00828] Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis","url":"https://arxiv.org/abs/2601.00828"},{"title":"Probing for Arithmetic Errors in Language Models","url":"https://arxiv.org/pdf/2507.12379"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/pdf/2512.20578"},{"title":"No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes","url":"https://arxiv.org/pdf/2509.10625"}]

Based on the search results, here's what recent research has found about correctability prediction in LLMs:

## Internal Probes and Error Detection

LLMs cache evaluative representations that drive verbal confidence and dissociate from log-probabilities, and this signal extends to error detection and self-correction—critically predicting which errors the model can correct.

Arithmetic errors can be anticipated from internal activations alone, and simple probes offer a viable path toward lightweight model self-correction.

## Predicting Failure and Correctness

Gnosis consistently outperforms strong internal baselines and large external judges in both accuracy and calibration across math reasoning, open-domain question answering, and academic knowledge benchmarks. This approach learns to compress hidden states and attention maps from a frozen LLM into descriptors and predicts correctness scores with only ~5 million extra parameters and essentially zero added inference cost.

## The Error Depth Hypothesis

The Error Depth Hypothesis proposes that stronger models make fewer but deeper errors that resist self-correction, suggesting that not all errors are equally correctable.

## Limitations of Self-Correction

Research demonstrates that LLMs cannot correct their own reasoning without external feedback, and no prior work shows successful intrinsic self-correction using only the model's own feedback.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97bd659e-8f4d-4e72-a394-1573792a9105",
  "isSidechain": false,
  "promptId": "cfd26950-1158-49a2-b94b-ad272b2bb26f",
  "type": "user",
  "uuid": "5cc44e4f-4de6-4ea4-a731-e94da8b1b59c",
  "toolUseResult": {
    "query": "correctability prediction LLM which errors are fixable self-correctable internal probe 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XKrwnUanDUHTbxpMyVH1WM",
        "content": [
          {
            "title": "How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals",
            "url": "https://arxiv.org/html/2604.22271v1"
          },
          {
            "title": "[2512.20578] Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/abs/2512.20578"
          },
          {
            "title": "Know When You’re Wrong: Aligning Confidence with Correctness for LLM Error Detection",
            "url": "https://arxiv.org/html/2603.06604"
          },
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs",
            "url": "https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"
          },
          {
            "title": "[2601.00828] Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis",
            "url": "https://arxiv.org/abs/2601.00828"
          },
          {
            "title": "Probing for Arithmetic Errors in Language Models",
            "url": "https://arxiv.org/pdf/2507.12379"
          },
          {
            "title": "Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/pdf/2512.20578"
          },
          {
            "title": "No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes",
            "url": "https://arxiv.org/pdf/2509.10625"
          }
        ]
      },
      "Based on the search results, here's what recent research has found about correctability prediction in LLMs:\n\n## Internal Probes and Error Detection\n\nLLMs cache evaluative representations that drive verbal confidence and dissociate from log-probabilities, and this signal extends to error detection and self-correction—critically predicting which errors the model can correct.\n\nArithmetic errors can be anticipated from internal activations alone, and simple probes offer a viable path toward lightweight model self-correction.\n\n## Predicting Failure and Correctness\n\nGnosis consistently outperforms strong internal baselines and large external judges in both accuracy and calibration across math reasoning, open-domain question answering, and academic knowledge benchmarks. This approach learns to compress hidden states and attention maps from a frozen LLM into descriptors and predicts correctness scores with only ~5 million extra parameters and essentially zero added inference cost.\n\n## The Error Depth Hypothesis\n\nThe Error Depth Hypothesis proposes that stronger models make fewer but deeper errors that resist self-correction, suggesting that not all errors are equally correctable.\n\n## Limitations of Self-Correction\n\nResearch demonstrates that LLMs cannot correct their own reasoning without external feedback, and no prior work shows successful intrinsic self-correction using only the model's own feedback."
    ],
    "durationSeconds": 9.159721636000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "97bd659e-8f4d-4e72-a394-1573792a9105",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "5cc44e4f-4de6-4ea4-a731-e94da8b1b59c",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM correctability prediction proposal",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be"
}
```

---

### Tool call

_source line 41 · 2026-05-20T03:28:21.820Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S9XysRLQMRxkiEVvjajSQx`</summary>

```json
{
  "query": "\"post-answer newline\" PANL token probe correctability AUROC 0.614 LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cc44e4f-4de6-4ea4-a731-e94da8b1b59c",
  "isSidechain": false,
  "requestId": "req_011CbD7NmWjobkC2r2PMsPKE",
  "type": "assistant",
  "uuid": "10bcdfec-1a56-41ff-b5bf-ce64755ec7ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MY1rSJDd6QqCZJvGLzWMfk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 813,
      "cache_read_input_tokens": 26427,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 813,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 26427,
          "cache_creation_input_tokens": 813,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 813
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

_source line 42 · 2026-05-20T03:28:36.072Z_

<details><summary>↩ Tool result · `toolu_01S9XysRLQMRxkiEVvjajSQx`</summary>

```text
Web search results for query: ""post-answer newline" PANL token probe correctability AUROC 0.614 LLM 2025 2026"

Links: [{"title":"Token Probabilities to Mitigate Large Language Models Overconfidence in Answering Medical Questions: Quantitative Study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12396779/"},{"title":"Updated: November 6, 2025 Measures of Predictive Accuracy","url":"https://www.casact.org/sites/default/files/2026-01/MAS-II_Measures_of_Predictive_Accuracy_Study_Note-1.pdf"},{"title":"A Closer Look at AUROC and AUPRC under Class Imbalance","url":"https://arxiv.org/html/2401.06091v1"},{"title":"A Closer Look at AUROC and AUPRC under Class Imbalance Matthew B. McDermott","url":"https://openreview.net/pdf?id=S3HvA808gk"},{"title":"Model-Agnostic Correctness Assessment for LLM-Generated Code via Dynamic Internal Representation Selection","url":"https://arxiv.org/pdf/2510.02934"}]

The search didn't return results for "post-answer newline" (PANL) token probe. Let me try a more specific search:

Links: [{"title":"How do LLMs Compute Verbal Confidence?","url":"https://arxiv.org/html/2603.17839v1"},{"title":"ProbeLLM: Automating Principled Diagnosis of LLM Failures","url":"https://arxiv.org/pdf/2602.12966"},{"title":"Predicting LLM Answer Accuracy from Question-Only ...","url":"https://arxiv.org/pdf/2509.10625"},{"title":"Solving Markdown Newline Issues in LLM Stream Responses | Yingjie's Blog","url":"https://yingjiezhao.com/en/articles/Solving-Markdown-Newline-Issues-in-LLM-Stream-Responses/"},{"title":"No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2509.10625"},{"title":"No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes | alphaXiv","url":"https://www.alphaxiv.org/abs/2509.10625v1"},{"title":"No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes | OpenReview","url":"https://openreview.net/forum?id=OhN25uxVab"}]

Great! I found relevant information. Let me search for more specific details about the AUROC 0.614 metric mentioned in your query:

Links: [{"title":"No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes","url":"https://arxiv.org/pdf/2509.10625"},{"title":"Reasoning Models Know When They're Right: Probing Hidden States for   Self-Verification","url":"https://arxiv.org/pdf/2504.05419"},{"title":"Probing for Arithmetic Errors in Language Models","url":"https://arxiv.org/pdf/2507.12379"},{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/pdf/2602.08159"},{"title":"Grade 6, Probe 1 Answer Key 1 0 2 ...","url":"https://www.wssd.k12.pa.us/Downloads/Grade%206%20M-Comp%20Answer%20Key.pdf"}]

Based on my web search results, I found highly relevant information about the post-answer newline (PANL) token probe research:

PANL stands for the post-answer-newline token position in LLM prompts, which is used in confidence probing experiments. Mean ablation of representations of PANL token at a single layer causes disruption of verbal confidence reporting as measured by decrease in logit difference and change in first token outputted by model.

Confidence information is gathered at the post-answer-newline token via attention to answer tokens, particularly the last answer token, at earlier layers (21–25), and this information is routed to the confidence-colon token—either directly or through intermediate tokens.

Regarding the broader context of LLM correctability probing, research tests the Linear Representation Hypothesis for correctness by checking if the residual stream activation contains a direction that linearly separates questions the model will answer correctly from those it will not. Recent work has shown that internal probes achieve 0.80-0.97 AUC while output-based methods achieve only 0.44–0.64 AUC, demonstrating that correctness signals are encoded in model internals.

However, I wasn't able to find a specific source for the exact AUROC value of 0.614 you mentioned in your search query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10bcdfec-1a56-41ff-b5bf-ce64755ec7ba",
  "isSidechain": false,
  "promptId": "cfd26950-1158-49a2-b94b-ad272b2bb26f",
  "type": "user",
  "uuid": "855b0ab4-487a-4f44-87cb-3eda582b4bac",
  "toolUseResult": {
    "query": "\"post-answer newline\" PANL token probe correctability AUROC 0.614 LLM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QRLDb1ZsbJTPUS8Mr8UtES",
        "content": [
          {
            "title": "Token Probabilities to Mitigate Large Language Models Overconfidence in Answering Medical Questions: Quantitative Study",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12396779/"
          },
          {
            "title": "Updated: November 6, 2025 Measures of Predictive Accuracy",
            "url": "https://www.casact.org/sites/default/files/2026-01/MAS-II_Measures_of_Predictive_Accuracy_Study_Note-1.pdf"
          },
          {
            "title": "A Closer Look at AUROC and AUPRC under Class Imbalance",
            "url": "https://arxiv.org/html/2401.06091v1"
          },
          {
            "title": "A Closer Look at AUROC and AUPRC under Class Imbalance Matthew B. McDermott",
            "url": "https://openreview.net/pdf?id=S3HvA808gk"
          },
          {
            "title": "Model-Agnostic Correctness Assessment for LLM-Generated Code via Dynamic Internal Representation Selection",
            "url": "https://arxiv.org/pdf/2510.02934"
          }
        ]
      },
      "The search didn't return results for \"post-answer newline\" (PANL) token probe. Let me try a more specific search:",
      {
        "tool_use_id": "srvtoolu_01LyFzD63yqLgheRzWYD8cco",
        "content": [
          {
            "title": "How do LLMs Compute Verbal Confidence?",
            "url": "https://arxiv.org/html/2603.17839v1"
          },
          {
            "title": "ProbeLLM: Automating Principled Diagnosis of LLM Failures",
            "url": "https://arxiv.org/pdf/2602.12966"
          },
          {
            "title": "Predicting LLM Answer Accuracy from Question-Only ...",
            "url": "https://arxiv.org/pdf/2509.10625"
          },
          {
            "title": "Solving Markdown Newline Issues in LLM Stream Responses | Yingjie's Blog",
            "url": "https://yingjiezhao.com/en/articles/Solving-Markdown-Newline-Issues-in-LLM-Stream-Responses/"
          },
          {
            "title": "No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/arXiv:2509.10625"
          },
          {
            "title": "No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes | alphaXiv",
            "url": "https://www.alphaxiv.org/abs/2509.10625v1"
          },
          {
            "title": "No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes | OpenReview",
            "url": "https://openreview.net/forum?id=OhN25uxVab"
          }
        ]
      },
      "Great! I found relevant information. Let me search for more specific details about the AUROC 0.614 metric mentioned in your query:",
      {
        "tool_use_id": "srvtoolu_013deYZVHspAxarwkdfbewB6",
        "content": [
          {
            "title": "No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes",
            "url": "https://arxiv.org/pdf/2509.10625"
          },
          {
            "title": "Reasoning Models Know When They're Right: Probing Hidden States for   Self-Verification",
            "url": "https://arxiv.org/pdf/2504.05419"
          },
          {
            "title": "Probing for Arithmetic Errors in Language Models",
            "url": "https://arxiv.org/pdf/2507.12379"
          },
          {
            "title": "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models",
            "url": "https://arxiv.org/pdf/2602.08159"
          },
          {
            "title": "Grade 6, Probe 1 Answer Key 1 0 2 ...",
            "url": "https://www.wssd.k12.pa.us/Downloads/Grade%206%20M-Comp%20Answer%20Key.pdf"
          }
        ]
      },
      "Based on my web search results, I found highly relevant information about the post-answer newline (PANL) token probe research:\n\nPANL stands for the post-answer-newline token position in LLM prompts, which is used in confidence probing experiments. Mean ablation of representations of PANL token at a single layer causes disruption of verbal confidence reporting as measured by decrease in logit difference and change in first token outputted by model.\n\nConfidence information is gathered at the post-answer-newline token via attention to answer tokens, particularly the last answer token, at earlier layers (21–25), and this information is routed to the confidence-colon token—either directly or through intermediate tokens.\n\nRegarding the broader context of LLM correctability probing, research tests the Linear Representation Hypothesis for correctness by checking if the residual stream activation contains a direction that linearly separates questions the model will answer correctly from those it will not. Recent work has shown that internal probes achieve 0.80-0.97 AUC while output-based methods achieve only 0.44–0.64 AUC, demonstrating that correctness signals are encoded in model internals.\n\nHowever, I wasn't able to find a specific source for the exact AUROC value of 0.614 you mentioned in your search query."
    ],
    "durationSeconds": 14.245498124000004,
    "searchCount": 3
  },
  "sourceToolAssistantUUID": "10bcdfec-1a56-41ff-b5bf-ce64755ec7ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-20T03:29:41.386Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough research to make an informed assessment. Let me synthesize what I've found:

## Summary of the proposal

The proposal investigates whether LLMs' internal representations can predict which errors are self-correctable (as opposed to just predicting correctness). It proposes:
1. Enhanced Correctability Probes (ECP) using multi-layer ensemble stacking, multi-token features, attention-entropy, etc.
2. Three-way gating: retain, correct (with selective Wait), or abstain
3. Representational geometry analysis of correctability vs. correctness
4. Comparison against 8 baselines


5. Several closely related works already exist in this space: correctness probing is well-established with strong linear separability results, multi-layer ensembling for probes has shown promise for deception detection, confidence-based routing systems like CoRefine already implement gating mechanisms, and research on error depth suggests deeper errors are harder to self-correct.

6. There's also work on SAE dissociation showing uncertainty and correctness use different feature spaces, wait token mechanisms that have been analyzed through crosscoder approaches, and pre-generation failure prediction methods.

7. Self-correction approaches like PAG and ReflectiveConf already use confidence-based mechanisms for selective revision.

The core novelty here is framing **correctability as a distinct prediction target** — not just predicting whether the model is wrong, but whether it can actually fix that specific error. This is genuinely a second-order property that hasn't been the primary focus before. But I should push back on this: could you achieve similar results by just looking at whether errors are correctable through simpler heuristics?

For instance, if you combine a correctness probe with error depth characterization, you'd essentially get a correctability estimate without needing a separate probe. The error depth work already suggests this decomposition. Or you could rely on existing confidence-based routing like CoRefine's three-way system, which already achieves 92.6% precision. Even majority voting or best-of-N sampling would be simpler alternatives that don't require probes at all.

The real question is whether correctability represents a genuinely distinct internal signal, or if it's just a function of being wrong plus having sufficient uncertainty or feature space to enable self-correction.

The novelty here is thin—the core idea of predicting correctability is interesting but incremental, and the technical components are largely borrowed from recent work on deception detection, uncertainty dissociation, and representational geometry. The combination is legitimate but doesn't feel sufficiently novel. On significance, while identifying self-correctable errors would be practically useful, the whole premise depends on whether this is even a well-defined problem.

The related work section misses some directly competing papers on error detection and self-correction. More fundamentally, the core assumption that correctability is encoded as a deterministic property in the model's hidden state is questionable—self-correction success likely depends more on the specific correction prompt, temperature, and stochastic factors than on any fixed internal representation. And there's a simpler threat: a basic correctness probe already achieves strong performance, so combining it with straightforward heuristics might work just as well without the elaborate machinery.

The proposal feels engineering-heavy, layering on multiple techniques like multi-layer ensembles, attention entropy, and SAE features without a clear conceptual advance—it reads like a kitchen-sink approach. The "dual-outcome" safety net is concerning too, suggesting the authors are hedging their bets in case the core probe result doesn't pan out. Finally, submitting to CoRL is a venue mismatch since this is purely about LLM probing and has nothing to do with robotics; it belongs at ACL, EMNLP, NeurIPS, or ICLR instead.

Setting aside venue concerns and focusing on the core idea quality: the concept of "correctability as a distinct prediction target" is a genuine contribution, but most technical components are borrowed from recent work, making the combination feel incremental rather than surprising. The practical relevance is there, but the impact hinges on whether correctability actually emerges as a distinct internal signal—and the dual-outcome framing suggests the authors aren't fully confident in that outcome. I'd rate novelty and significance both as medium, with related work coverage being solid though missing some recent papers. My assessment lands around 20-30% acceptance probability, with a median of about 25%.

Actually, reconsidering more carefully: the core question—whether we can predict which errors are self-correctable using internal probes—is genuinely novel and no one has directly tackled this before. The distinction between correctness and correctability as first-order versus second-order properties is conceptually interesting. However, the proposal feels over-engineered, like someone threw every available technique at the problem, which often signals weak confidence in the underlying idea. The most compelling contribution would be if representational geometry analysis reveals that correctability has a fundamentally different structure than correctness, but the proposal doesn't make a convincing case for why we should expect this difference. I think 25-35% is the right range—the idea has real substance but isn't particularly surprising.

The "kitchen sink" approach muddies what the actual contribution is. I should also note this is supposedly for CoRL 2026, yet it's pure NLP/interpretability work with zero robotics content—that's a significant venue mismatch, though I'll evaluate it as an NLP paper per the rubric. Looking at what's genuinely novel here: correctability as a prediction target is new, three-way gating with abstention is somewhat new, representational geometry analysis of correctability is new, and there's a wait baseline. These are real contributions, but the proposal obscures them under layers of unnecessary complexity.

The core techniques are all borrowed from existing work—multi-layer ensembling from deception detection, SAE feature analysis from uncertainty research, representational geometry from the Confidence Manifold paper, and error depth from self-correction decomposition. So the novelty lives in the research question, not the methodology. That's defensible, but it means everything hinges on whether the empirical findings are actually surprising. The real problem is the trivial alternative: you could just combine an existing correctness probe (already achieving 0.80-0.97 AUC) with an uncertainty probe, then route based on whether the model is wrong and uncertain versus wrong and confident. That's straightforwardly derivable from prior work and undermines the contribution.

The proposal needs to demonstrate that correctability captures information beyond what correctness and uncertainty already provide. If it does, the elaborate probe construction is justified. If not, the whole thing collapses. Given this tension, I'm settling on medium novelty—the question is fresh but the techniques are borrowed and there's a credible trivial alternative threat. Significance is also medium because the impact depends entirely on whether correctability is genuinely distinct from correctness plus uncertainty. The related work coverage is solid but could dig deeper into recent papers. I'm estimating 22-32% probability, median around 25%. The core risk is that correctability might just be a repackaging of existing signals rather than a new insight. Also, the proposal is extremely long and detailed, which is itself a warning sign.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "855b0ab4-487a-4f44-87cb-3eda582b4bac",
  "isSidechain": false,
  "requestId": "req_011CbD7Q3ooKxWshaf8PJP8m",
  "type": "assistant",
  "uuid": "1f5c2804-7bca-4b82-96bc-2ae6807ed270",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0192hBd3aeNg6hS4rN85bFwP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1347,
      "cache_read_input_tokens": 27240,
      "output_tokens": 6575,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1347,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6575,
          "cache_read_input_tokens": 27240,
          "cache_creation_input_tokens": 1347,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1347
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

_source line 44 · 2026-05-20T03:31:06.468Z_

Now I have sufficient research to make an informed assessment. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models" (arXiv:2602.08159, 2026):
   最直接的竞争性工作。已证明 correctness 在 transformer hidden states 中是低维(3-8维)、线性可分的，linear probes 达到 0.80-0.97 AUC，远超 output-based 方法(0.44-0.64 AUC)。这意味着 correctness probing 已经是一个成熟的技术——本 proposal 的 correctability probing 需要证明自己在 correctness probing 之上有增量价值。

2. "Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders" (arXiv:2604.19974, 2026):
   本 proposal 直接依赖的基础工作。已发现 uncertainty 和 correctness 由不同 feature populations 编码（pure uncertainty features, pure incorrectness features, confounded features），且 68% 的 pure incorrectness features 是 causally inert。本 proposal 拟将此框架扩展到 correctability，但这个扩展的增量价值需要论证。

3. "Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling" (arXiv:2604.13386, 2026):
   本 proposal 拟迁移的技术来源。已证明 multi-layer ensemble 在 deception detection 上相比 single-layer 可提升 AUROC 达 78%。本 proposal 的核心技术贡献之一（multi-layer ensembling for correctability）本质上是该技术的直接应用。

4. "CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute" (arXiv:2602.08948, 2026):
   最直接的系统级竞争者。已实现三路路由(HALT/RETHINK/ALTERNATIVE)，用 211K 参数 Conv1D controller 在 confidence features 上做决策，halting precision 达 92.6%。本 proposal 需要证明 hidden-state probe 比 output-level confidence 更优。

5. "Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis" (arXiv:2601.00828, 2025):
   提出 Error Depth Hypothesis——更强的模型犯更少但更深的错误，深错误抗拒自我修正。这为 correctability 的异质性提供了经验证据，但也暗示了一个 trivial baseline：correctability ≈ f(error depth)，而 error depth 可能通过 correctness probe confidence 近似估计。

6. "Internal states before wait modulate reasoning patterns" (arXiv:2510.04128, 2025):
   分析了 Wait token 前的 hidden states 如何影响后续推理模式。本 proposal 拟利用这些 pre-Wait features，但该论文已做了大量 crosscoder 分析，留给 proposal 的新贡献空间有限。

7. "LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations" (arXiv:2602.09924, 2026, ICLR 2026 LIT Workshop):
   用 pre-generation activations 上的 linear probes 预测 task success。证明了 LLM 内部编码了 model-specific 的难度信号。但该工作预测的是"是否会答对"（correctness），而非"答错了能否修正"（correctability），这是本 proposal 声称的关键区分。

8. "How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals" (arXiv:2604.22271, 2026):
   直接相关但 proposal 未引用。研究 LLM 内部 confidence signals 在 error detection 和 self-correction 中的角色，声称 confidence signals 可以 predict which errors the model can correct。这与本 proposal 的核心 claim 高度重叠。

- 调研总结: LLM 内部表征对 correctness 的编码已被充分研究(linear probes 达 0.80-0.97 AUC)，uncertainty 与 correctness 的 feature dissociation 已被 SAE 分析揭示，confidence-based routing 已有成熟方案(CoRefine)。本 proposal 处于这些工作的交叉地带，试图将 probing 目标从 correctness 推进到 correctability，但这个概念距离上的推进在技术上是否对应一个genuinely distinct internal signal 尚不清楚。同时，arXiv:2604.22271 已在非常接近的方向上开展工作，对 novelty 构成实质威胁。


【Trivial Alternative 检验】:

**存在明确的 trivial alternative 威胁。** 

最直接的替代方案：将已有的 correctness probe (0.80-0.97 AUC, arXiv:2602.08159) 与 uncertainty probe 简单组合——如果模型 (1) 被探测为"大概率错误"且 (2) 具有高 uncertainty，则尝试修正；如果 (1) 大概率错误但 (2) 低 uncertainty（即"自信地犯错"），则 abstain。这种组合不需要引入"correctability"作为独立的预测目标，只需要现成的 correctness + uncertainty probes 的逻辑运算。

第二个替代方案：CoRefine 的 confidence-based controller 已经在 output-level features 上实现了三路路由且 halting precision 达 92.6%。本 proposal 需要证明 hidden-state probes 提供的增量超过 output-level confidence features，而 arXiv:2602.08159 虽然显示 internal probes > output-based methods 在 correctness detection 上，但这不等同于在 routing/gating 任务上也成立。

**增量价值的关键条件**：本 proposal 的增量价值完全取决于一个未经验证的假设——"correctability 是一个在模型内部有独立表征的信号，不可还原为 correctness + uncertainty 的组合"。如果这个假设不成立，整个 elaborate probe 构建就是过度工程化。


【前提假设检验】:

核心 claim 的逻辑链条中有以下未经验证的关键假设：

1. **"Correctability 是一个内部编码的独立属性"假设**（最关键）：
   一个错误是否可自修正，可能并非模型在生成错误答案时已经"知道"的信息，而是取决于修正过程中的 stochastic factors（采样温度、prompt 形式、解码策略等）。如果 correctability 不是模型 hidden state 中的确定性属性，而是修正过程的涌现结果，那么从 pre-correction hidden state 去预测它在原理上就存在 ceiling。Error Depth Hypothesis (arXiv:2601.00828) 暗示 correctability 与 error depth 相关，但 error depth 本身可能不完全由 hidden state 编码。

2. **"Multi-layer ensembling 从 deception 迁移到 correctability"假设**：
   Deception detection 的信号结构（deception direction 跨层缓慢旋转）可能与 correctability 的信号结构有本质不同。Deception 涉及模型"知道真答案但选择说谎"，信号清晰；correctability 涉及"模型不确定是否能找到正确答案"，信号可能更模糊、更分散。直接迁移的合理性需要论证。

3. **"PANL + last-answer-token + reasoning tokens 的 multi-token 组合能提升 probe 性能"假设**：
   arXiv:2602.08159 已证明 correctness signal 只需 3-8 维就能捕获，暗示信号结构简单。添加更多 token positions 和 feature types 可能导致过拟合而非性能提升。proposal 缺少对这一 over-parameterization 风险的讨论。


【3 维度打分】:

1. **Novelty: 弱-中** — 
   "Correctability 作为独立预测目标"这一概念确实新颖，但增量有限。技术层面几乎全部借用自近期工作：multi-layer ensembling 直接来自 arXiv:2604.13386，SAE feature decomposition 框架来自 arXiv:2604.19974，representational geometry 分析来自 arXiv:2602.08159。更关键的是，arXiv:2604.22271 已经在研究 "internal confidence signals predict which errors the model can correct"——与本 proposal 的核心 claim 高度重叠。剥离 surface differences 后，本 proposal 的核心新增量是 (a) 将 correctability 形式化为独立预测目标，(b) 与 correctness 做 representational geometry 对比。(a) 是一个好的 framing 但不是 deep insight；(b) 是一个有意思的实验但结论可能是 "correctability 的表征结构与 correctness 类似"——这在审稿人看来属于 "I would have guessed this"。

2. **Significance: 中** — 
   "哪些错误值得修正、哪些应该 abstain"在实际部署中确实重要。如果 probe-gated correction 能可靠工作，对 test-time compute allocation 有实际价值。但问题的重要性被两个因素削弱：(a) CoRefine 等 output-level 方案已经在实用层面解决了类似问题（92.6% halting precision），hidden-state probe 的增量收益可能不足以 justify 额外的复杂性；(b) 随着 reasoning models 和 extended thinking 的快速发展，self-correction 本身的范式可能正在被超越——模型可能会通过更好的 initial reasoning 而非 post-hoc correction 来提升准确率。

3. **Related Work: 中** — 
   对 CoRefine、Error Depth Hypothesis、SAE dissociation、Wait token 机制等的引用是准确和相关的。但缺失了一些直接竞争的工作：arXiv:2604.22271 ("How LLMs Detect and Correct Their Own Errors") 研究的方向与本 proposal 高度重叠但未被引用；arXiv:2512.20578 ("Can LLMs Predict Their Own Failures?") 和 arXiv:2510.16062 (CorrectBench) 也是应该讨论的工作。与 CoRefine 的差异化定位虽然有尝试（hidden-state vs. output-level, genuine abstention），但论证深度不足——proposal 未能解释为什么 hidden-state probe 在 gating 任务上比 output-level confidence 更优的理论原因。


【概率估计】: [18% - 28%] 中位 22%

【估计理由】: 
Novelty 是主要限制维度。核心概念（correctability as distinct target）有新颖性但增量有限——剥离借用的技术后，真正新的 insight 薄弱，且 arXiv:2604.22271 已在高度重叠的方向上工作。Significance 受限于 CoRefine 等 output-level 方案已提供了实用的替代方案。最关键的风险是 Trivial Alternative 威胁：correctness probe + uncertainty probe 的简单组合可能达到接近的 gating 效果，使得 correctability 作为独立信号的 value proposition 不成立。proposal 的"kitchen-sink"风格（堆叠多层 ensemble、multi-token features、attention entropy、SAE features、crosscoder analysis 等）反映了对核心 idea 深度的不自信，审稿人可能会批评 contribution 不够 focused。dual-outcome 保底策略（"even if probe AUROC plateaus"）虽然务实，但从 idea 评估角度看是一个负面信号——proposal 自身暗示了核心 result 可能为 negative。

【主要风险】: 
1. **Correctability 不是独立信号风险**：如果 correctability ≈ correctness + uncertainty 的组合，核心 contribution 瓦解，trivial baseline (correctness probe + uncertainty threshold) 即可 replicate 主要效果
2. **与 arXiv:2604.22271 的重叠风险**：该工作已研究 internal confidence signals 如何 predict which errors the model can correct，如果在 submission 前该工作被进一步发展或被顶会接收，本 proposal 的 novelty claim 将受到严重质疑
```

Sources:
- [The Confidence Manifold (arXiv:2602.08159)](https://arxiv.org/pdf/2602.08159)
- [SAE Functional Dissociation (arXiv:2604.19974)](https://arxiv.org/abs/2604.19974)
- [Multi-Layer Ensemble Probing (arXiv:2604.13386)](https://arxiv.org/abs/2604.13386)
- [CoRefine (arXiv:2602.08948)](https://arxiv.org/abs/2602.08948)
- [Error Depth Hypothesis (arXiv:2601.00828)](https://arxiv.org/abs/2601.00828)
- [Wait Token Mechanisms (arXiv:2510.04128)](https://arxiv.org/abs/2510.04128)
- [LLMs Encode Their Failures (arXiv:2602.09924)](https://arxiv.org/abs/2602.09924)
- [How LLMs Detect and Correct Their Own Errors (arXiv:2604.22271)](https://arxiv.org/html/2604.22271v1)
- [Can LLMs Predict Their Own Failures? (arXiv:2512.20578)](https://arxiv.org/abs/2512.20578)
- [Self-Correction Bench (arXiv:2507.02778)](https://arxiv.org/html/2507.02778v1)
- [CorrectBench (arXiv:2510.16062)](https://arxiv.org/abs/2510.16062)
- [Reflective Confidence (arXiv:2512.18605)](https://arxiv.org/pdf/2512.18605)
- [PAG (arXiv:2506.10406)](https://arxiv.org/pdf/2506.10406)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f5c2804-7bca-4b82-96bc-2ae6807ed270",
  "isSidechain": false,
  "requestId": "req_011CbD7Q3ooKxWshaf8PJP8m",
  "type": "assistant",
  "uuid": "892d3aa8-4082-4a6a-a86c-643305f7a107",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0192hBd3aeNg6hS4rN85bFwP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1347,
      "cache_read_input_tokens": 27240,
      "output_tokens": 6575,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1347,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6575,
          "cache_read_input_tokens": 27240,
          "cache_creation_input_tokens": 1347,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1347
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

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "892d3aa8-4082-4a6a-a86c-643305f7a107",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM correctability prediction proposal",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "892d3aa8-4082-4a6a-a86c-643305f7a107",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM correctability prediction proposal",
  "sessionId": "d69ae16d-908d-4923-816c-a366b56904be"
}
```

---
