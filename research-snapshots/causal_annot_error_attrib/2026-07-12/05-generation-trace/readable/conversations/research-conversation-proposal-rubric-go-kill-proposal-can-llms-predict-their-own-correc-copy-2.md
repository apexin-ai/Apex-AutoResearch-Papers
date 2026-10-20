# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Can LLMs Predict Their Own Correc

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-1/d00bcc48-da96-4dd3-97ae-3a28bcad8e94.jsonl`
- **Structured JSON:** [`19c1b03f21a1fd695a7e.json`](../../sessions/19/19c1b03f21a1fd695a7e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:22:04.291Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:22:04.291Z",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction\n\n## Description\nWe investigate whether LLMs' internal representations can predict which of their errors are self-correctable, and whether this prediction enables selective correction that outperforms both ungated correction, the trivial 'Wait' baseline, and confidence-based routing. Prior work shows a faint correctability signal at the post-answer newline token (PANL) achieving only 0.614 AUROC with a single-layer linear probe — insufficient for reliable gating. We develop Enhanced Correctability Probes (ECP) that combine multi-layer ensemble stacking, multi-token features (PANL + last-answer-token + reasoning tokens), attention-entropy features, pre-Wait hidden-state features (informed by crosscoder analysis of Wait-token mechanisms, arXiv:2510.04128), and SAE-guided feature selection targeting the confounded feature intersection that bridges uncertainty and correctness (motivated by the functional dissociation finding of arXiv:2604.19974, where 68% of pure incorrectness features are causally inert). We begin with a Phase 0 pilot that directly tests whether multi-layer ensembling — which improved deception detection AUROC by up to 78% (arXiv:2604.13386, specifically on Harm-Pressure Knowledge in Llama-70B) — transfers to the fundamentally different task of correctability prediction. These probes gate a three-way decision: retain the original answer (likely correct), attempt correction including probe-selective Wait insertion (error detected, high correctability), or abstain (error detected, low correctability). This framework is distinguished from CoRefine's (arXiv:2602.08948) three-way routing — which uses output-level confidence, lacks genuine abstention, and is not correctability-aware — by using hidden-state probes, providing a genuine abstention option for unfixable errors, and explicitly predicting error fixability rather than confidence. Critically, we provide the first evaluation of the 'Wait' baseline on correct answers, measuring its previously-unknown overcorrection cost. We also conduct the first representational geometry and SAE feature decomposition analysis of correctability vs. correctness, testing whether correctability — a second-order property that depends not just on whether the model is wrong but on whether correction mechanisms can reach the right answer — shares the low-dimensional, linearly-separable structure that correctness exhibits (arXiv:2602.08159), requires higher dimensionality or non-linear boundaries, or depends disproportionately on the narrow confounded feature population identified by arXiv:2604.19974. This analysis, combined with error depth characterization (arXiv:2601.00828) and threshold analysis mapping probe quality to gating utility, ensures publishable contributions even if probe AUROC plateaus at marginal levels. We evaluate across Gemma-3-27B, Qwen-2.5-7B-Instruct, and Mistral-Small-3.2-24B on TriviaQA, MMLU, and GSM8K, comparing against eight baselines including ungated correction, Wait (universal and probe-selective), confidence-based routing (CoRefine-style and Reflective Confidence-style), PAG, and oracle gating. Our contributions are: (1) operationalizing correctability as a prediction target distinct from correctness, (2) the first pilot testing whether multi-layer ensembling transfers from deception to correctability, (3) the first hidden-state probe-based gating with genuine abstention for correctability-aware self-correction — distinguished from CoRefine's confidence-based routing by signal source, abstention capability, and correctability specificity, (4) the first representational geometry and SAE feature decomposition comparison of correctability vs. correctness, testing whether second-order properties have a different confounded-feature signature than first-order properties, and (5) establishing the conditions — including minimum probe quality thresholds — under which probe-gated correction outperforms simpler alternatives including confidence-based controllers.\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T03:22:04.294Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:22:04.294Z",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94"
}
```

---

## Round 1

56 recorded events

### User

_source line 3 · 2026-05-20T03:22:04.309Z_

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
  "promptId": "42ed86f0-30d1-4a3d-bc0e-e280317c2813",
  "type": "user",
  "uuid": "547591e4-4839-4e24-831e-f3047772cbcd",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:22:04.308Z_

```json
{
  "parentUuid": "547591e4-4839-4e24-831e-f3047772cbcd",
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
  "uuid": "f876c69f-46da-4d0f-86ba-a1508829cd9d",
  "timestamp": "2026-05-20T03:22:04.308Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:22:04.308Z_

```json
{
  "parentUuid": "f876c69f-46da-4d0f-86ba-a1508829cd9d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a62b6e21-89e0-4bd2-bbb8-c5faf1c084fb",
  "timestamp": "2026-05-20T03:22:04.308Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
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
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94"
}
```

---

### Assistant

_source line 7 · 2026-05-20T03:22:19.145Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for CoRL 2026. Let me first carefully read the proposal, then conduct web searches to understand the current state of the field before making my assessment.

Wait - CoRL is Conference on Robot Learning. But this proposal is about LLM self-correction, probing internal representations, etc. This seems more like an NLP/ML paper than a robotics paper. Let me re-read the user's instructions... they say "CoRL 2026 主会" but the proposal is clearly about LLM internal representations and self-correction. This is a mismatch - CoRL focuses on robot learning, not LLM probing. 

I should focus on evaluating the idea quality itself rather than getting caught up on the venue question. The proposal might be intended for a different conference, or there could be a connection to robotics I'm missing, but either way I can assess the research merit and provide useful feedback on the core ideas.

Now I need to do some background research to properly evaluate this work. I'll search for recent developments in LLM self-correction, probing techniques for internal representations, and the specific papers they're building on to understand where this fits in the current landscape.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a62b6e21-89e0-4bd2-bbb8-c5faf1c084fb",
  "isSidechain": false,
  "requestId": "req_011CbD6uAuNvQYpAqTrKrUHb",
  "type": "assistant",
  "uuid": "631ef6b8-57fa-4782-a666-ba44e78b88b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014WoFGK586WiaLYQ6AzcBYn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 2346,
      "cache_read_input_tokens": 13985,
      "output_tokens": 625,
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
          "output_tokens": 625,
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

_source line 8 · 2026-05-20T03:22:19.631Z_

我需要先对这个 proposal 所涉及的领域进行详细调研，然后再进行评估。让我先加载 WebSearch 工具，然后进行多轮搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "631ef6b8-57fa-4782-a666-ba44e78b88b6",
  "isSidechain": false,
  "requestId": "req_011CbD6uAuNvQYpAqTrKrUHb",
  "type": "assistant",
  "uuid": "9b150d09-a3a0-4de9-9188-34fd502503be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014WoFGK586WiaLYQ6AzcBYn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 2346,
      "cache_read_input_tokens": 13985,
      "output_tokens": 625,
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
          "output_tokens": 625,
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

_source line 9 · 2026-05-20T03:22:20.126Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GPyijR2LumrRaXRjK5zjGQ`</summary>

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
  "parentUuid": "9b150d09-a3a0-4de9-9188-34fd502503be",
  "isSidechain": false,
  "requestId": "req_011CbD6uAuNvQYpAqTrKrUHb",
  "type": "assistant",
  "uuid": "2809cee6-102c-4784-a31e-551f8131e417",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014WoFGK586WiaLYQ6AzcBYn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 2346,
      "cache_read_input_tokens": 13985,
      "output_tokens": 625,
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
          "output_tokens": 625,
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

_source line 10 · 2026-05-20T03:22:20.133Z_

<details><summary>↩ Tool result · `toolu_01GPyijR2LumrRaXRjK5zjGQ`</summary>

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
  "parentUuid": "2809cee6-102c-4784-a31e-551f8131e417",
  "isSidechain": false,
  "promptId": "42ed86f0-30d1-4a3d-bc0e-e280317c2813",
  "type": "user",
  "uuid": "7bb68f59-1100-407c-a257-09ab7494a16c",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "2809cee6-102c-4784-a31e-551f8131e417",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-20T03:22:40.138Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct multiple searches to understand the field. I'll search for:
1. LLM self-correction recent work, selective self-correction
2. Probing LLM internal representations for correctness/uncertainty
3. The specific papers cited (CoRefine, Wait token, etc.)
4. Multi-layer probing for deception detection
5. SAE features for correctness/uncertainty in LLMs

Let me start with parallel searches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bb68f59-1100-407c-a257-09ab7494a16c",
  "isSidechain": false,
  "requestId": "req_011CbD6vLXbcFVxDskbd2tVG",
  "type": "assistant",
  "uuid": "27ecd5ab-3813-4f1e-aaea-c72d6cf5ef9f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HNGpT1S7iQRfcUwnEsRKB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 16331,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1151,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 429,
          "cache_read_input_tokens": 16331,
          "cache_creation_input_tokens": 1151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1151
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

_source line 12 · 2026-05-20T03:22:41.118Z_

现在让我进行系统性的领域调研。我会并行发起多个搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27ecd5ab-3813-4f1e-aaea-c72d6cf5ef9f",
  "isSidechain": false,
  "requestId": "req_011CbD6vLXbcFVxDskbd2tVG",
  "type": "assistant",
  "uuid": "8863d2ec-3407-4444-81cb-ae1cdcf47aa9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HNGpT1S7iQRfcUwnEsRKB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 16331,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1151,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 429,
          "cache_read_input_tokens": 16331,
          "cache_creation_input_tokens": 1151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1151
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

_source line 13 · 2026-05-20T03:22:41.609Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017i768BBJCwF92TmvjEQApW`</summary>

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
  "parentUuid": "8863d2ec-3407-4444-81cb-ae1cdcf47aa9",
  "isSidechain": false,
  "requestId": "req_011CbD6vLXbcFVxDskbd2tVG",
  "type": "assistant",
  "uuid": "2e4ebe64-73c6-4f28-87f3-3bcbeeb452e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HNGpT1S7iQRfcUwnEsRKB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 16331,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1151,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 429,
          "cache_read_input_tokens": 16331,
          "cache_creation_input_tokens": 1151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1151
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

_source line 14 · 2026-05-20T03:22:42.609Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018YLwxUzwFs1CHRGdmVkZPM`</summary>

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
  "parentUuid": "2e4ebe64-73c6-4f28-87f3-3bcbeeb452e5",
  "isSidechain": false,
  "requestId": "req_011CbD6vLXbcFVxDskbd2tVG",
  "type": "assistant",
  "uuid": "35fe69f0-2409-4361-a2f1-26ee2d84b610",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HNGpT1S7iQRfcUwnEsRKB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 16331,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1151,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 429,
          "cache_read_input_tokens": 16331,
          "cache_creation_input_tokens": 1151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1151
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

_source line 15 · 2026-05-20T03:22:43.081Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011DetJ96eApvvS4uRrmvYzC`</summary>

```json
{
  "query": "probing LLM correctness uncertainty internal representations linear probe AUROC 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35fe69f0-2409-4361-a2f1-26ee2d84b610",
  "isSidechain": false,
  "requestId": "req_011CbD6vLXbcFVxDskbd2tVG",
  "type": "assistant",
  "uuid": "b3167eb5-83b7-407f-a0da-9c3fe1b3f1f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HNGpT1S7iQRfcUwnEsRKB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 16331,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1151,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 429,
          "cache_read_input_tokens": 16331,
          "cache_creation_input_tokens": 1151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1151
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

_source line 16 · 2026-05-20T03:22:43.579Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PVW3AjWtw7kBVHvCkig3Tz`</summary>

```json
{
  "query": "multi-layer ensemble probing deception detection LLM arXiv 2604.13386"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3167eb5-83b7-407f-a0da-9c3fe1b3f1f7",
  "isSidechain": false,
  "requestId": "req_011CbD6vLXbcFVxDskbd2tVG",
  "type": "assistant",
  "uuid": "b86f3003-cc8c-4ed5-ad58-ff174d07a831",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HNGpT1S7iQRfcUwnEsRKB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 16331,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1151,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 429,
          "cache_read_input_tokens": 16331,
          "cache_creation_input_tokens": 1151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1151
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

_source line 17 · 2026-05-20T03:22:44.082Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018VnPduGoTu85zhkeARMtUi`</summary>

```json
{
  "query": "\"Wait\" token baseline LLM reasoning self-correction budget forcing 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b86f3003-cc8c-4ed5-ad58-ff174d07a831",
  "isSidechain": false,
  "requestId": "req_011CbD6vLXbcFVxDskbd2tVG",
  "type": "assistant",
  "uuid": "0cb644fa-3d92-4d17-82f4-dea9cd96eafd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HNGpT1S7iQRfcUwnEsRKB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 16331,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1151,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 429,
          "cache_read_input_tokens": 16331,
          "cache_creation_input_tokens": 1151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1151
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

_source line 18 · 2026-05-20T03:22:48.977Z_

<details><summary>↩ Tool result · `toolu_017i768BBJCwF92TmvjEQApW`</summary>

```text
Web search results for query: "LLM self-correction selective gating probe internal representations 2025 2026"

Links: [{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"},{"title":"Superscopes: Amplifying Internal Feature Representations for Language   Model Interpretation","url":"https://arxiv.org/pdf/2503.02078"},{"title":"Probing for Arithmetic Errors in Language Models","url":"https://arxiv.org/pdf/2507.12379"},{"title":"Internalized Self-Correction for Large Language Models","url":"https://arxiv.org/pdf/2412.16653"},{"title":"From Emergence to Control: Probing and Modulating Self-Reflection in Language Models","url":"https://arxiv.org/pdf/2506.12217"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/pdf/2512.20578"},{"title":"LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations","url":"https://arxiv.org/pdf/2602.09924"}]

I've performed the web search for your query. Here are the relevant findings:

## Key Research Areas Found:

**LLM Self-Correction and Internal Representations:**

Research indicates that approaches leveraging internal model representations often outperform logit-based methods, with methods like INTRA exploiting interactions between internal representations to achieve state-of-the-art self-correction performance.

**Probing Internal Mechanisms:**

Patchscopes introduced a method for probing internal activations by patching them into new prompts, while Superscopes systematically amplifies superposed features in MLP outputs and hidden states before patching them into new contexts.

**Selective Gating and Error Detection:**

Research demonstrates that probes can guide selective re-prompting of erroneous reasoning steps to improve task accuracy, with findings suggesting that arithmetic errors can be anticipated from internal activations alone, offering a viable path toward lightweight model self-correction.

**Self-Reflection Mechanisms:**

Recent work on probing and modulating self-reflection in LLMs shows that self-reflection correlates with improved reasoning accuracy, though its origin and mechanisms remain poorly understood, and self-reflection emerges in pretrained models albeit rarely.

**Failure Prediction from Internal Representations:**

A fundamental open question is whether LLMs can anticipate their own failures by examining the internal dynamics that govern their generation process.

The search results show active research in 2025-2026 on probing internal representations for self-correction, selective routing based on internal signals, and understanding the mechanisms underlying LLM self-awareness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e4ebe64-73c6-4f28-87f3-3bcbeeb452e5",
  "isSidechain": false,
  "promptId": "42ed86f0-30d1-4a3d-bc0e-e280317c2813",
  "type": "user",
  "uuid": "cb8395e8-925d-4750-86fc-c1260c68b89b",
  "toolUseResult": {
    "query": "LLM self-correction selective gating probe internal representations 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LC9VExQSo5SqXXWEtj8JZu",
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
      "I've performed the web search for your query. Here are the relevant findings:\n\n## Key Research Areas Found:\n\n**LLM Self-Correction and Internal Representations:**\n\nResearch indicates that approaches leveraging internal model representations often outperform logit-based methods, with methods like INTRA exploiting interactions between internal representations to achieve state-of-the-art self-correction performance.\n\n**Probing Internal Mechanisms:**\n\nPatchscopes introduced a method for probing internal activations by patching them into new prompts, while Superscopes systematically amplifies superposed features in MLP outputs and hidden states before patching them into new contexts.\n\n**Selective Gating and Error Detection:**\n\nResearch demonstrates that probes can guide selective re-prompting of erroneous reasoning steps to improve task accuracy, with findings suggesting that arithmetic errors can be anticipated from internal activations alone, offering a viable path toward lightweight model self-correction.\n\n**Self-Reflection Mechanisms:**\n\nRecent work on probing and modulating self-reflection in LLMs shows that self-reflection correlates with improved reasoning accuracy, though its origin and mechanisms remain poorly understood, and self-reflection emerges in pretrained models albeit rarely.\n\n**Failure Prediction from Internal Representations:**\n\nA fundamental open question is whether LLMs can anticipate their own failures by examining the internal dynamics that govern their generation process.\n\nThe search results show active research in 2025-2026 on probing internal representations for self-correction, selective routing based on internal signals, and understanding the mechanisms underlying LLM self-awareness."
    ],
    "durationSeconds": 7.361499541000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2e4ebe64-73c6-4f28-87f3-3bcbeeb452e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T03:22:49.020Z_

<details><summary>↩ Tool result · `toolu_018YLwxUzwFs1CHRGdmVkZPM`</summary>

```text
Web search results for query: "CoRefine arXiv 2602.08948 LLM self-correction routing confidence"

Links: [{"title":"[2602.08948] CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute","url":"https://arxiv.org/abs/2602.08948"},{"title":"CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute","url":"https://arxiv.org/pdf/2602.08948"},{"title":"Learning to Route LLMs with Confidence Tokens","url":"https://arxiv.org/html/2410.13284v3"},{"title":"Learning to Route LLMs with Confidence Tokens","url":"https://arxiv.org/pdf/2410.13284"},{"title":"Confidence v.s. Critique: A Decomposition of Self-Correction Capability   for LLMs","url":"https://arxiv.org/pdf/2412.19513"}]

Based on the search results, here's what I found about CoRefine (arXiv 2602.08948):

CoRefine is a confidence-guided self-refinement method that achieves competitive accuracy using a fraction of the tokens via a lightweight 211k-parameter Conv1D controller atop a frozen LLM.

**Key Features:**

The controller consumes full-trace confidence to decide whether to halt, re-examine, or try a different approach, enabling targeted self-correction with an average of 2.7 refinement steps per problem and roughly 190-fold token reduction relative to 512-sample baselines.

**Routing Mechanism:**

The controller consumes full-trace confidence features of the LLM decoded reasoning chain and decides: HALT (accept current answer), RETHINK (verify reasoning), or ALTERNATIVE (explore new approach).

**Performance:**

The controller achieves 92.6 percent precision when it confidently halts, indicating that confidence dynamics reliably signal when to stop refinement. Additionally, CoRefine saves up to 63% over parallel baselines in terms of latency.

The paper was submitted on February 9, 2026, and addresses the problem of test-time scaling in large language models by using confidence signals to guide adaptive self-correction rather than relying on expensive parallel decoding approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35fe69f0-2409-4361-a2f1-26ee2d84b610",
  "isSidechain": false,
  "promptId": "42ed86f0-30d1-4a3d-bc0e-e280317c2813",
  "type": "user",
  "uuid": "364277b4-3811-4f92-85c7-faef59241418",
  "toolUseResult": {
    "query": "CoRefine arXiv 2602.08948 LLM self-correction routing confidence",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LJx4odw8NC5RaNZRz1JbEE",
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
      "Based on the search results, here's what I found about CoRefine (arXiv 2602.08948):\n\nCoRefine is a confidence-guided self-refinement method that achieves competitive accuracy using a fraction of the tokens via a lightweight 211k-parameter Conv1D controller atop a frozen LLM.\n\n**Key Features:**\n\nThe controller consumes full-trace confidence to decide whether to halt, re-examine, or try a different approach, enabling targeted self-correction with an average of 2.7 refinement steps per problem and roughly 190-fold token reduction relative to 512-sample baselines.\n\n**Routing Mechanism:**\n\nThe controller consumes full-trace confidence features of the LLM decoded reasoning chain and decides: HALT (accept current answer), RETHINK (verify reasoning), or ALTERNATIVE (explore new approach).\n\n**Performance:**\n\nThe controller achieves 92.6 percent precision when it confidently halts, indicating that confidence dynamics reliably signal when to stop refinement. Additionally, CoRefine saves up to 63% over parallel baselines in terms of latency.\n\nThe paper was submitted on February 9, 2026, and addresses the problem of test-time scaling in large language models by using confidence signals to guide adaptive self-correction rather than relying on expensive parallel decoding approaches."
    ],
    "durationSeconds": 6.408715194999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "35fe69f0-2409-4361-a2f1-26ee2d84b610",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "364277b4-3811-4f92-85c7-faef59241418",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM correctability prediction proposal",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94"
}
```

---

### Tool result

_source line 22 · 2026-05-20T03:22:50.526Z_

<details><summary>↩ Tool result · `toolu_01PVW3AjWtw7kBVHvCkig3Tz`</summary>

```text
Web search results for query: "multi-layer ensemble probing deception detection LLM arXiv 2604.13386"

Links: [{"title":"[2604.13386] Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling","url":"https://arxiv.org/abs/2604.13386"},{"title":"Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling","url":"https://arxiv.org/html/2604.13386v1"},{"title":"Caught in the Act: a mechanistic approach to detecting deception","url":"https://arxiv.org/pdf/2508.19505"},{"title":"DeceptGuard :A Constitutional Oversight Framework For Detecting Deception in LLM Agents","url":"https://arxiv.org/pdf/2603.13791"},{"title":"Detecting Multi-Agent Collusion Through Multi-Agent Interpretability","url":"https://arxiv.org/pdf/2604.01151"},{"title":"Hidden in Plain Sight: Evaluation of the Deception Detection Capabilities of LLMs in Multimodal Settings","url":"https://arxiv.org/pdf/2506.09424"}]

I found the paper! Here are the search results for arXiv paper 2604.13386:

**Title:** Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling

**Key Findings:**

Linear probes can detect when language models produce outputs they "know" are wrong, a capability relevant to both deception and reward hacking. However, single-layer probes are fragile: the best layer varies across models and tasks, and probes fail entirely on some deception types.

**Main Contribution:**

Combining probes from multiple layers into an ensemble recovers strong performance even where single-layer probes fail, improving AUROC by +29% on Insider Trading and +78% on Harm-Pressure Knowledge.

**Scaling Results:**

Across 12 models (0.5B--176B parameters), probe accuracy improves with scale: ~5% AUROC per 10x parameters (R=0.81).

**Geometric Insight:**

Deception directions rotate gradually across layers rather than appearing at one location, explaining both why single-layer probes are brittle and why multi-layer ensembles succeed.

The paper was published on April 15, 2026, by Erik Nordby, Tasha Pais, and Aviel Parrack.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b86f3003-cc8c-4ed5-ad58-ff174d07a831",
  "isSidechain": false,
  "promptId": "42ed86f0-30d1-4a3d-bc0e-e280317c2813",
  "type": "user",
  "uuid": "cdb0969f-88e1-4569-adc9-1fb243945ca8",
  "toolUseResult": {
    "query": "multi-layer ensemble probing deception detection LLM arXiv 2604.13386",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ndu4WwKzqk3CRzuvfwkPnz",
        "content": [
          {
            "title": "[2604.13386] Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling",
            "url": "https://arxiv.org/abs/2604.13386"
          },
          {
            "title": "Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling",
            "url": "https://arxiv.org/html/2604.13386v1"
          },
          {
            "title": "Caught in the Act: a mechanistic approach to detecting deception",
            "url": "https://arxiv.org/pdf/2508.19505"
          },
          {
            "title": "DeceptGuard :A Constitutional Oversight Framework For Detecting Deception in LLM Agents",
            "url": "https://arxiv.org/pdf/2603.13791"
          },
          {
            "title": "Detecting Multi-Agent Collusion Through Multi-Agent Interpretability",
            "url": "https://arxiv.org/pdf/2604.01151"
          },
          {
            "title": "Hidden in Plain Sight: Evaluation of the Deception Detection Capabilities of LLMs in Multimodal Settings",
            "url": "https://arxiv.org/pdf/2506.09424"
          }
        ]
      },
      "I found the paper! Here are the search results for arXiv paper 2604.13386:\n\n**Title:** Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling\n\n**Key Findings:**\n\nLinear probes can detect when language models produce outputs they \"know\" are wrong, a capability relevant to both deception and reward hacking. However, single-layer probes are fragile: the best layer varies across models and tasks, and probes fail entirely on some deception types.\n\n**Main Contribution:**\n\nCombining probes from multiple layers into an ensemble recovers strong performance even where single-layer probes fail, improving AUROC by +29% on Insider Trading and +78% on Harm-Pressure Knowledge.\n\n**Scaling Results:**\n\nAcross 12 models (0.5B--176B parameters), probe accuracy improves with scale: ~5% AUROC per 10x parameters (R=0.81).\n\n**Geometric Insight:**\n\nDeception directions rotate gradually across layers rather than appearing at one location, explaining both why single-layer probes are brittle and why multi-layer ensembles succeed.\n\nThe paper was published on April 15, 2026, by Erik Nordby, Tasha Pais, and Aviel Parrack."
    ],
    "durationSeconds": 6.9396650609999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b86f3003-cc8c-4ed5-ad58-ff174d07a831",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T03:22:50.957Z_

<details><summary>↩ Tool result · `toolu_018VnPduGoTu85zhkeARMtUi`</summary>

```text
Web search results for query: ""Wait" token baseline LLM reasoning self-correction budget forcing 2025 2026"

Links: [{"title":"arXiv:2412.18547v5 [cs.CL] 2 Jun 2025 Token-Budget-Aware LLM Reasoning","url":"https://arxiv.org/pdf/2412.18547"},{"title":"Wait, We Don't Need to “Wait”! Removing Thinking Tokens ...","url":"https://aclanthology.org/2025.findings-emnlp.394.pdf"},{"title":"Boosting Accuracy and Efficiency of Budget Forcing in ...","url":"https://fse.studenttheses.ub.rug.nl/36698/1/bAI2025TarunokusumoRA.pdf"},{"title":"Token-Budget-Aware LLM Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1274/"},{"title":"Token-Budget-Aware LLM Reasoning","url":"https://aclanthology.org/2025.findings-acl.1274.pdf"},{"title":"Steering LLM Thinking with Budget Guidance","url":"https://arxiv.org/html/2506.13752v1"},{"title":"BudgetThinker: Empowering Budget-aware LLM Reasoning with Control Tokens","url":"https://arxiv.org/pdf/2508.17196"},{"title":"Understanding Reasoning in LLMs through Strategic Information Allocation under Uncertainty","url":"https://arxiv.org/pdf/2603.15500"}]

Based on the search results, here's what I found about these topics:

## Token-Budget-Aware LLM Reasoning

A token-budget-aware LLM reasoning framework dynamically adjusts the number of reasoning tokens based on the reasoning complexity of each problem. This method effectively reduces token costs in CoT reasoning with only a slight performance reduction, offering a practical solution to balance efficiency and accuracy in LLM reasoning.

## Budget Forcing

Budget forcing enforces a hard token limit by appending an end-of-thinking delimiter (and optionally "Final Answer:") to trigger early exit and force the model to proceed.

## "Wait" Tokens

The "Wait" token is related to thinking tokens, with research revealing an information peak phenomenon in which effective reasoning shows a peak of information in a small number of critical steps.

## Recent Research (2025-2026)

Several recent papers address LLM reasoning efficiency:

- Test-time scaling is a paradigm where models are prompted to "think longer" by generating extended Chain-of-Thought reasoning before delivering a final answer. While this approach has unlocked state-of-the-art performance in complex domains like advanced mathematics and coding, it comes at the significant cost of increased latency and computational overhead.

- Research demonstrated that SFT+RL models performed better on the GSM8K dataset with varying compute budgets, showing an overall higher accuracy while significantly reducing token usage by over 40% compared to the SFT model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0cb644fa-3d92-4d17-82f4-dea9cd96eafd",
  "isSidechain": false,
  "promptId": "42ed86f0-30d1-4a3d-bc0e-e280317c2813",
  "type": "user",
  "uuid": "8cd40319-4dd7-47c4-9fc2-e64ff354b4cf",
  "toolUseResult": {
    "query": "\"Wait\" token baseline LLM reasoning self-correction budget forcing 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Q7bXYhJ6Pnst5GsXxVVrVt",
        "content": [
          {
            "title": "arXiv:2412.18547v5 [cs.CL] 2 Jun 2025 Token-Budget-Aware LLM Reasoning",
            "url": "https://arxiv.org/pdf/2412.18547"
          },
          {
            "title": "Wait, We Don't Need to “Wait”! Removing Thinking Tokens ...",
            "url": "https://aclanthology.org/2025.findings-emnlp.394.pdf"
          },
          {
            "title": "Boosting Accuracy and Efficiency of Budget Forcing in ...",
            "url": "https://fse.studenttheses.ub.rug.nl/36698/1/bAI2025TarunokusumoRA.pdf"
          },
          {
            "title": "Token-Budget-Aware LLM Reasoning - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-acl.1274/"
          },
          {
            "title": "Token-Budget-Aware LLM Reasoning",
            "url": "https://aclanthology.org/2025.findings-acl.1274.pdf"
          },
          {
            "title": "Steering LLM Thinking with Budget Guidance",
            "url": "https://arxiv.org/html/2506.13752v1"
          },
          {
            "title": "BudgetThinker: Empowering Budget-aware LLM Reasoning with Control Tokens",
            "url": "https://arxiv.org/pdf/2508.17196"
          },
          {
            "title": "Understanding Reasoning in LLMs through Strategic Information Allocation under Uncertainty",
            "url": "https://arxiv.org/pdf/2603.15500"
          }
        ]
      },
      "Based on the search results, here's what I found about these topics:\n\n## Token-Budget-Aware LLM Reasoning\n\nA token-budget-aware LLM reasoning framework dynamically adjusts the number of reasoning tokens based on the reasoning complexity of each problem. This method effectively reduces token costs in CoT reasoning with only a slight performance reduction, offering a practical solution to balance efficiency and accuracy in LLM reasoning.\n\n## Budget Forcing\n\nBudget forcing enforces a hard token limit by appending an end-of-thinking delimiter (and optionally \"Final Answer:\") to trigger early exit and force the model to proceed.\n\n## \"Wait\" Tokens\n\nThe \"Wait\" token is related to thinking tokens, with research revealing an information peak phenomenon in which effective reasoning shows a peak of information in a small number of critical steps.\n\n## Recent Research (2025-2026)\n\nSeveral recent papers address LLM reasoning efficiency:\n\n- Test-time scaling is a paradigm where models are prompted to \"think longer\" by generating extended Chain-of-Thought reasoning before delivering a final answer. While this approach has unlocked state-of-the-art performance in complex domains like advanced mathematics and coding, it comes at the significant cost of increased latency and computational overhead.\n\n- Research demonstrated that SFT+RL models performed better on the GSM8K dataset with varying compute budgets, showing an overall higher accuracy while significantly reducing token usage by over 40% compared to the SFT model."
    ],
    "durationSeconds": 6.872555210000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0cb644fa-3d92-4d17-82f4-dea9cd96eafd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T03:22:52.107Z_

<details><summary>↩ Tool result · `toolu_011DetJ96eApvvS4uRrmvYzC`</summary>

```text
Web search results for query: "probing LLM correctness uncertainty internal representations linear probe AUROC 2025"

Links: [{"title":"Published as a conference paper at ICLR 2025 DO LLMS ESTIMATE UNCERTAINTY WELL","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/ef472869c217bf693f2d9bbde66a6b07-Paper-Conference.pdf"},{"title":"Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation","url":"https://arxiv.org/html/2512.22245"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/html/2505.21772v1"},{"title":"Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty","url":"https://arxiv.org/pdf/2512.22245"},{"title":"Confidence Before Answering: A Paradigm Shift for Efficient LLM Uncertainty Estimation","url":"https://arxiv.org/html/2603.05881v1"},{"title":"Can Linear Probes Measure LLM Uncertainty ?","url":"https://arxiv.org/html/2510.04108"},{"title":"Can Linear Probes Measure LLM Uncertainty ? Ramzi Dakhmouche ∗","url":"https://arxiv.org/pdf/2510.04108"},{"title":"Between the Layers Lies the Truth: Uncertainty Estimation in LLMs Using Intra-Layer Local Information Scores","url":"https://arxiv.org/html/2603.22299"},{"title":"Response Uncertainty and Probe Modeling: Two Sides of the Same Coin in LLM Interpretability?","url":"https://arxiv.org/html/2505.18575v1"}]

Based on the web search results, here are the key findings related to probing LLM correctness, uncertainty estimation, internal representations, and linear probe AUROC from 2025 research:

## LLM Uncertainty Estimation Challenges

LLMs struggle to estimate uncertainty in instruction-following, with average AUROC values across models and uncertainty estimation methods hovering around chance levels (between 0.43 and 0.53). Probe AUROC scores drop below 0.60 across all models when task complexity increases, revealing that even internal representations struggle to estimate uncertainty accurately.

## Linear Probes for Uncertainty Estimation

AUROC is the most widely used metric for selective classification, quantifying the likelihood that a correct prediction will have a lower uncertainty score than an incorrect one, where an AUROC of 0.5 indicates no discriminative ability and values approaching 1.0 reflect strong discriminative performance.

Recent approaches have shown promise: Linear probes achieve superior AUROC performance compared to baseline methods, and sparse linear regression approaches consistently achieve state-of-the-art performance, surpassing existing methods, with findings highlighting that effective uncertainty quantification in LLMs does not necessarily require complex architectures.

## Internal Representation Probing

A number of studies investigate whether a model is able to answer a question by probing its internal representations, with some employing probes to predict confidence for a given question. LLM internals encode signals correlated with correctness; however, these probes often rely on high-dimensional hidden vectors, tend to be task-specific, and can be difficult to interpret or generalize.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3167eb5-83b7-407f-a0da-9c3fe1b3f1f7",
  "isSidechain": false,
  "promptId": "42ed86f0-30d1-4a3d-bc0e-e280317c2813",
  "type": "user",
  "uuid": "f6f3f16b-31f1-417b-9f0b-14e1c947766c",
  "toolUseResult": {
    "query": "probing LLM correctness uncertainty internal representations linear probe AUROC 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01X5DmcptR5Wm7MDqQF3H2dm",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2025 DO LLMS ESTIMATE UNCERTAINTY WELL",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/ef472869c217bf693f2d9bbde66a6b07-Paper-Conference.pdf"
          },
          {
            "title": "Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation",
            "url": "https://arxiv.org/html/2512.22245"
          },
          {
            "title": "Calibrating LLM Confidence by Probing Perturbed Representation Stability",
            "url": "https://arxiv.org/html/2505.21772v1"
          },
          {
            "title": "Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty",
            "url": "https://arxiv.org/pdf/2512.22245"
          },
          {
            "title": "Confidence Before Answering: A Paradigm Shift for Efficient LLM Uncertainty Estimation",
            "url": "https://arxiv.org/html/2603.05881v1"
          },
          {
            "title": "Can Linear Probes Measure LLM Uncertainty ?",
            "url": "https://arxiv.org/html/2510.04108"
          },
          {
            "title": "Can Linear Probes Measure LLM Uncertainty ? Ramzi Dakhmouche ∗",
            "url": "https://arxiv.org/pdf/2510.04108"
          },
          {
            "title": "Between the Layers Lies the Truth: Uncertainty Estimation in LLMs Using Intra-Layer Local Information Scores",
            "url": "https://arxiv.org/html/2603.22299"
          },
          {
            "title": "Response Uncertainty and Probe Modeling: Two Sides of the Same Coin in LLM Interpretability?",
            "url": "https://arxiv.org/html/2505.18575v1"
          }
        ]
      },
      "Based on the web search results, here are the key findings related to probing LLM correctness, uncertainty estimation, internal representations, and linear probe AUROC from 2025 research:\n\n## LLM Uncertainty Estimation Challenges\n\nLLMs struggle to estimate uncertainty in instruction-following, with average AUROC values across models and uncertainty estimation methods hovering around chance levels (between 0.43 and 0.53). Probe AUROC scores drop below 0.60 across all models when task complexity increases, revealing that even internal representations struggle to estimate uncertainty accurately.\n\n## Linear Probes for Uncertainty Estimation\n\nAUROC is the most widely used metric for selective classification, quantifying the likelihood that a correct prediction will have a lower uncertainty score than an incorrect one, where an AUROC of 0.5 indicates no discriminative ability and values approaching 1.0 reflect strong discriminative performance.\n\nRecent approaches have shown promise: Linear probes achieve superior AUROC performance compared to baseline methods, and sparse linear regression approaches consistently achieve state-of-the-art performance, surpassing existing methods, with findings highlighting that effective uncertainty quantification in LLMs does not necessarily require complex architectures.\n\n## Internal Representation Probing\n\nA number of studies investigate whether a model is able to answer a question by probing its internal representations, with some employing probes to predict confidence for a given question. LLM internals encode signals correlated with correctness; however, these probes often rely on high-dimensional hidden vectors, tend to be task-specific, and can be difficult to interpret or generalize."
    ],
    "durationSeconds": 9.023025003999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b3167eb5-83b7-407f-a0da-9c3fe1b3f1f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-20T03:22:55.421Z_

<details><summary>Logged reasoning block</summary>

```text
Let me do more targeted searches for the other cited papers and for the specific concept of "correctability" as a prediction target.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6f3f16b-31f1-417b-9f0b-14e1c947766c",
  "isSidechain": false,
  "requestId": "req_011CbD6xh3Bdz3f2EdM9575m",
  "type": "assistant",
  "uuid": "a00b660b-f496-4fac-a854-8a192ecc6bdf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHbLE2pUzYK76XKuJaGk8M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1391,
      "cache_creation_input_tokens": 2601,
      "cache_read_input_tokens": 17482,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2601,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1391,
          "output_tokens": 298,
          "cache_read_input_tokens": 17482,
          "cache_creation_input_tokens": 2601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2601
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

_source line 26 · 2026-05-20T03:22:56.378Z_

让我继续搜索更多关键引用和领域近况。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a00b660b-f496-4fac-a854-8a192ecc6bdf",
  "isSidechain": false,
  "requestId": "req_011CbD6xh3Bdz3f2EdM9575m",
  "type": "assistant",
  "uuid": "90b827c5-d0b5-4fce-9052-1ec2b086f8bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHbLE2pUzYK76XKuJaGk8M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1391,
      "cache_creation_input_tokens": 2601,
      "cache_read_input_tokens": 17482,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2601,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1391,
          "output_tokens": 298,
          "cache_read_input_tokens": 17482,
          "cache_creation_input_tokens": 2601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2601
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

_source line 27 · 2026-05-20T03:22:57.324Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KZo83YBVSnA8sU9GWQKVNz`</summary>

```json
{
  "query": "arXiv 2604.19974 SAE features correctness uncertainty LLM confounded features"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90b827c5-d0b5-4fce-9052-1ec2b086f8bf",
  "isSidechain": false,
  "requestId": "req_011CbD6xh3Bdz3f2EdM9575m",
  "type": "assistant",
  "uuid": "23e5e017-f402-4233-9401-ed979d027f61",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHbLE2pUzYK76XKuJaGk8M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1391,
      "cache_creation_input_tokens": 2601,
      "cache_read_input_tokens": 17482,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2601,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1391,
          "output_tokens": 298,
          "cache_read_input_tokens": 17482,
          "cache_creation_input_tokens": 2601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2601
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

_source line 28 · 2026-05-20T03:22:58.301Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TtfLLEn6jRVVLReXVC9S2S`</summary>

```json
{
  "query": "arXiv 2602.08159 representational geometry correctness LLM linear separability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23e5e017-f402-4233-9401-ed979d027f61",
  "isSidechain": false,
  "requestId": "req_011CbD6xh3Bdz3f2EdM9575m",
  "type": "assistant",
  "uuid": "bc03c28d-3e0c-49d0-9b0f-1807c303fa9a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHbLE2pUzYK76XKuJaGk8M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1391,
      "cache_creation_input_tokens": 2601,
      "cache_read_input_tokens": 17482,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2601,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1391,
          "output_tokens": 298,
          "cache_read_input_tokens": 17482,
          "cache_creation_input_tokens": 2601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2601
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

_source line 29 · 2026-05-20T03:22:58.754Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XKX1uQfYQ6Gd8qDugopyM6`</summary>

```json
{
  "query": "arXiv 2601.00828 error depth characterization LLM self-correction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc03c28d-3e0c-49d0-9b0f-1807c303fa9a",
  "isSidechain": false,
  "requestId": "req_011CbD6xh3Bdz3f2EdM9575m",
  "type": "assistant",
  "uuid": "91c1db14-c44d-45da-8df2-376b2931590c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHbLE2pUzYK76XKuJaGk8M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1391,
      "cache_creation_input_tokens": 2601,
      "cache_read_input_tokens": 17482,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2601,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1391,
          "output_tokens": 298,
          "cache_read_input_tokens": 17482,
          "cache_creation_input_tokens": 2601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2601
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

_source line 30 · 2026-05-20T03:22:59.442Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xrhs4YuqCqvwSwHnQaTi4V`</summary>

```json
{
  "query": "LLM correctability prediction self-correction when to correct probe gating 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91c1db14-c44d-45da-8df2-376b2931590c",
  "isSidechain": false,
  "requestId": "req_011CbD6xh3Bdz3f2EdM9575m",
  "type": "assistant",
  "uuid": "49ecfc7c-750c-49f4-af16-9a9bb3bc19d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHbLE2pUzYK76XKuJaGk8M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1391,
      "cache_creation_input_tokens": 2601,
      "cache_read_input_tokens": 17482,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2601,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1391,
          "output_tokens": 298,
          "cache_read_input_tokens": 17482,
          "cache_creation_input_tokens": 2601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2601
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

_source line 31 · 2026-05-20T03:23:04.409Z_

<details><summary>↩ Tool result · `toolu_01KZo83YBVSnA8sU9GWQKVNz`</summary>

```text
Web search results for query: "arXiv 2604.19974 SAE features correctness uncertainty LLM confounded features"

Links: [{"title":"[2604.19974] Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders","url":"https://arxiv.org/abs/2604.19974"},{"title":"Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders","url":"https://arxiv.org/html/2604.19974"},{"title":"Sparse but Wrong: Incorrect L0 Leads to Incorrect Features in Sparse Autoencoders","url":"https://arxiv.org/pdf/2508.16560"},{"title":"Falsifying Sparse Autoencoder Reasoning Features in Language Models","url":"https://arxiv.org/pdf/2601.05679"},{"title":"Can LLMs Detect Their Confabulations? Estimating Reliability in Uncertainty-Aware Language Models","url":"https://arxiv.org/pdf/2508.08139"},{"title":"Interpreting and Mitigating Unwanted Uncertainty in LLMs","url":"https://arxiv.org/pdf/2510.22866"}]

I found the paper! Here are the key details about arXiv 2604.19974:

**Title:** "Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders"

**Main Research Question:** The paper investigates whether output-level uncertainty and actual correctness in large language models are driven by the same internal mechanisms or by distinct feature populations.

**Methodology:** The researchers introduce a 2x2 framework that partitions model predictions along correctness and confidence axes, and uses sparse autoencoders to identify features associated with each dimension independently.

**Key Findings:** The study identifies three distinct feature populations—pure uncertainty features, pure incorrectness features, and confounded features—with each category playing a fundamentally different role in the model's computation.

**Feature Categories:**
- Pure uncertainty features are functionally essential: suppressing them severely degrades accuracy.
- Pure incorrectness features are functionally inert: despite showing statistically significant activation differences between correct and incorrect predictions, the majority produce near-zero change in accuracy when suppressed.
- Confounded features that encode both signals are detrimental to output quality, and targeted suppression of them yields a 1.1% accuracy improvement and a 75% entropy reduction, with effects transferring across the ARC-Challenge and RACE benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23e5e017-f402-4233-9401-ed979d027f61",
  "isSidechain": false,
  "promptId": "42ed86f0-30d1-4a3d-bc0e-e280317c2813",
  "type": "user",
  "uuid": "f6ac2263-209f-4a52-b368-92b571ed3763",
  "toolUseResult": {
    "query": "arXiv 2604.19974 SAE features correctness uncertainty LLM confounded features",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KCES6xmgGGUw3F3Z67xZJN",
        "content": [
          {
            "title": "[2604.19974] Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders",
            "url": "https://arxiv.org/abs/2604.19974"
          },
          {
            "title": "Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders",
            "url": "https://arxiv.org/html/2604.19974"
          },
          {
            "title": "Sparse but Wrong: Incorrect L0 Leads to Incorrect Features in Sparse Autoencoders",
            "url": "https://arxiv.org/pdf/2508.16560"
          },
          {
            "title": "Falsifying Sparse Autoencoder Reasoning Features in Language Models",
            "url": "https://arxiv.org/pdf/2601.05679"
          },
          {
            "title": "Can LLMs Detect Their Confabulations? Estimating Reliability in Uncertainty-Aware Language Models",
            "url": "https://arxiv.org/pdf/2508.08139"
          },
          {
            "title": "Interpreting and Mitigating Unwanted Uncertainty in LLMs",
            "url": "https://arxiv.org/pdf/2510.22866"
          }
        ]
      },
      "I found the paper! Here are the key details about arXiv 2604.19974:\n\n**Title:** \"Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders\"\n\n**Main Research Question:** The paper investigates whether output-level uncertainty and actual correctness in large language models are driven by the same internal mechanisms or by distinct feature populations.\n\n**Methodology:** The researchers introduce a 2x2 framework that partitions model predictions along correctness and confidence axes, and uses sparse autoencoders to identify features associated with each dimension independently.\n\n**Key Findings:** The study identifies three distinct feature populations—pure uncertainty features, pure incorrectness features, and confounded features—with each category playing a fundamentally different role in the model's computation.\n\n**Feature Categories:**\n- Pure uncertainty features are functionally essential: suppressing them severely degrades accuracy.\n- Pure incorrectness features are functionally inert: despite showing statistically significant activation differences between correct and incorrect predictions, the majority produce near-zero change in accuracy when suppressed.\n- Confounded features that encode both signals are detrimental to output quality, and targeted suppression of them yields a 1.1% accuracy improvement and a 75% entropy reduction, with effects transferring across the ARC-Challenge and RACE benchmarks."
    ],
    "durationSeconds": 7.042975127999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "23e5e017-f402-4233-9401-ed979d027f61",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T03:23:04.665Z_

<details><summary>↩ Tool result · `toolu_01XKX1uQfYQ6Gd8qDugopyM6`</summary>

```text
Web search results for query: "arXiv 2601.00828 error depth characterization LLM self-correction"

Links: [{"title":"[2601.00828] Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis","url":"https://arxiv.org/abs/2601.00828"},{"title":"Decomposing LLM Self-Correction:","url":"https://arxiv.org/pdf/2601.00828"},{"title":"Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis","url":"https://arxiv.org/html/2601.00828"},{"title":"Self-Correction Makes LLMs Better Parsers","url":"https://arxiv.org/html/2504.14165v1"},{"title":"Self-Correction Bench: Revealing and Addressing the Self-Correction Blind Spot in LLMs","url":"https://arxiv.org/html/2507.02778v1"},{"title":"Self-Correction Makes LLMs Better Parsers","url":"https://arxiv.org/pdf/2504.14165"},{"title":"Self-Correction Bench: Uncovering and Addressing the Self-Correction Blind Spot in Large Language Models","url":"https://arxiv.org/pdf/2507.02778"}]

Based on the search results, here's what I found about arXiv paper 2601.00828:

## Paper Overview

The paper is titled "Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis" and was submitted on December 24, 2025.

## Key Findings

The paper systematically decomposes self-correction into three distinct sub-capabilities: error detection, error localization, and error correction.

The research uncovers a striking paradox: weaker models (GPT-3.5, 66% accuracy) achieve 1.6x higher intrinsic correction rates than stronger models (DeepSeek, 94% accuracy)--26.8% vs 16.7%.

## The Error Depth Hypothesis

The paper proposes the Error Depth Hypothesis: stronger models make fewer but deeper errors that resist self-correction.

## Additional Insights

Claude detects 10% but corrects 29%; GPT-3.5 detects 82% but corrects 27%, demonstrating that error detection capability does not necessarily predict correction success.

You can access the full paper at https://arxiv.org/abs/2601.00828.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91c1db14-c44d-45da-8df2-376b2931590c",
  "isSidechain": false,
  "promptId": "42ed86f0-30d1-4a3d-bc0e-e280317c2813",
  "type": "user",
  "uuid": "93f1fe44-df1d-4c3d-a6b7-0a8751e21984",
  "toolUseResult": {
    "query": "arXiv 2601.00828 error depth characterization LLM self-correction",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SYSLLYzENQf8dhTqrTX1sj",
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
      "Based on the search results, here's what I found about arXiv paper 2601.00828:\n\n## Paper Overview\n\nThe paper is titled \"Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis\" and was submitted on December 24, 2025.\n\n## Key Findings\n\nThe paper systematically decomposes self-correction into three distinct sub-capabilities: error detection, error localization, and error correction.\n\nThe research uncovers a striking paradox: weaker models (GPT-3.5, 66% accuracy) achieve 1.6x higher intrinsic correction rates than stronger models (DeepSeek, 94% accuracy)--26.8% vs 16.7%.\n\n## The Error Depth Hypothesis\n\nThe paper proposes the Error Depth Hypothesis: stronger models make fewer but deeper errors that resist self-correction.\n\n## Additional Insights\n\nClaude detects 10% but corrects 29%; GPT-3.5 detects 82% but corrects 27%, demonstrating that error detection capability does not necessarily predict correction success.\n\nYou can access the full paper at https://arxiv.org/abs/2601.00828."
    ],
    "durationSeconds": 5.904823996000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "91c1db14-c44d-45da-8df2-376b2931590c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "93f1fe44-df1d-4c3d-a6b7-0a8751e21984",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM correctability prediction proposal",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94"
}
```

---

### Tool result

_source line 35 · 2026-05-20T03:23:05.129Z_

<details><summary>↩ Tool result · `toolu_01TtfLLEn6jRVVLReXVC9S2S`</summary>

```text
Web search results for query: "arXiv 2602.08159 representational geometry correctness LLM linear separability"

Links: [{"title":"Large Language Models Encode Semantics and Alignment in Linearly Separable Representations","url":"https://arxiv.org/pdf/2507.09709"},{"title":"Mechanistic Interpretability of Cognitive Complexity in LLMs via Linear Probing using Bloom’s Taxonomy","url":"https://arxiv.org/html/2602.17229"},{"title":"LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals","url":"https://arxiv.org/pdf/2604.05655"},{"title":"Predicting LLM Answer Accuracy from Question-Only ...","url":"https://arxiv.org/pdf/2509.10625"},{"title":"Evaluating Embedding Generalization: How LLMs, LoRA, and SLERP Shape Representational Geometry","url":"https://arxiv.org/html/2511.21703v1"},{"title":"On Representational Dissociation of Language and Arithmetic in Large   Language Models","url":"https://arxiv.org/pdf/2502.11932"}]

Based on the search results, I found several relevant papers on representational geometry, linear separability, and correctness in LLMs, though the specific arXiv ID 2602.08159 didn't appear directly in the results. However, the search returned highly related work:

The most relevant result is a paper on "LLM Reasoning as Trajectories" that characterizes chain-of-thought generation as structured trajectories through representation space, showing that mathematical reasoning traverses step-specific subspaces that become increasingly separable with layer depth. 

Additionally, the work shows that correct and incorrect solutions diverge systematically at late stages, enabling mid-reasoning prediction of final-answer correctness with ROC-AUC up to 0.87.

Another related study examined the Linear Representation Hypothesis for correctness, finding a "correctness direction" that is linearly separable in the residual stream and generalizes across diverse factual tasks.

The search results also include work on how arithmetic equations and general language input are encoded in completely separated regions in LLMs' internal representation space across all layers, as demonstrated through linear classifiers and cluster separability tests.

These papers collectively explore how correctness and semantic properties are encoded as linearly separable features in LLM representations, which aligns with your query topic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc03c28d-3e0c-49d0-9b0f-1807c303fa9a",
  "isSidechain": false,
  "promptId": "42ed86f0-30d1-4a3d-bc0e-e280317c2813",
  "type": "user",
  "uuid": "6da0f06c-4b05-4ce2-aab4-07711add0069",
  "toolUseResult": {
    "query": "arXiv 2602.08159 representational geometry correctness LLM linear separability",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Xhkeo8SPVWvVA76A6uk1MR",
        "content": [
          {
            "title": "Large Language Models Encode Semantics and Alignment in Linearly Separable Representations",
            "url": "https://arxiv.org/pdf/2507.09709"
          },
          {
            "title": "Mechanistic Interpretability of Cognitive Complexity in LLMs via Linear Probing using Bloom’s Taxonomy",
            "url": "https://arxiv.org/html/2602.17229"
          },
          {
            "title": "LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals",
            "url": "https://arxiv.org/pdf/2604.05655"
          },
          {
            "title": "Predicting LLM Answer Accuracy from Question-Only ...",
            "url": "https://arxiv.org/pdf/2509.10625"
          },
          {
            "title": "Evaluating Embedding Generalization: How LLMs, LoRA, and SLERP Shape Representational Geometry",
            "url": "https://arxiv.org/html/2511.21703v1"
          },
          {
            "title": "On Representational Dissociation of Language and Arithmetic in Large   Language Models",
            "url": "https://arxiv.org/pdf/2502.11932"
          }
        ]
      },
      "Based on the search results, I found several relevant papers on representational geometry, linear separability, and correctness in LLMs, though the specific arXiv ID 2602.08159 didn't appear directly in the results. However, the search returned highly related work:\n\nThe most relevant result is a paper on \"LLM Reasoning as Trajectories\" that characterizes chain-of-thought generation as structured trajectories through representation space, showing that mathematical reasoning traverses step-specific subspaces that become increasingly separable with layer depth. \n\nAdditionally, the work shows that correct and incorrect solutions diverge systematically at late stages, enabling mid-reasoning prediction of final-answer correctness with ROC-AUC up to 0.87.\n\nAnother related study examined the Linear Representation Hypothesis for correctness, finding a \"correctness direction\" that is linearly separable in the residual stream and generalizes across diverse factual tasks.\n\nThe search results also include work on how arithmetic equations and general language input are encoded in completely separated regions in LLMs' internal representation space across all layers, as demonstrated through linear classifiers and cluster separability tests.\n\nThese papers collectively explore how correctness and semantic properties are encoded as linearly separable features in LLM representations, which aligns with your query topic."
    ],
    "durationSeconds": 6.809021678999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bc03c28d-3e0c-49d0-9b0f-1807c303fa9a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T03:23:07.114Z_

<details><summary>↩ Tool result · `toolu_01Xrhs4YuqCqvwSwHnQaTi4V`</summary>

```text
Web search results for query: "LLM correctability prediction self-correction when to correct probe gating 2025 2026"

Links: [{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"},{"title":"How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals","url":"https://arxiv.org/html/2604.22271v1"},{"title":"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs | OpenReview","url":"https://openreview.net/forum?id=956KYtqwcU"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/pdf/2512.20578"},{"title":"Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis","url":"https://arxiv.org/pdf/2601.00828"},{"title":"Confidence v.s. Critique: A Decomposition of Self-Correction Capability   for LLMs","url":"https://arxiv.org/pdf/2412.19513"}]

I found several relevant research papers on LLM self-correction and correctability prediction from 2025-2026. Here are the key findings:

## Recent Research on LLM Self-Correction (2025-2026)

**Confidence Signals and Error Detection:**
Research addresses whether a model's own confidence predicts whether it will identify an error and whether a correction attempt will succeed, examining this both behaviorally through verbal confidence and representationally through internal activations. Recent work showed that LLMs cache an evaluative representation that drives verbal confidence and dissociates from log-probabilities, with this signal extending to error detection and self-correction—predicting which errors the model can correct.

**Comprehensive Benchmarking:**
CorrectBench was introduced as the first comprehensive benchmark for systematically evaluating self-correction mechanisms in LLMs, evaluating the effectiveness of intrinsic, external, and fine-tuned approaches across commonsense reasoning, mathematical reasoning, and code generation.

**The Accuracy-Correction Paradox:**
Research uncovered a striking paradox where weaker models achieve higher intrinsic correction rates than stronger models, with the Error Depth Hypothesis proposing that stronger models make "deeper" errors that resist self-correction, while weaker models make "shallower" errors that are easily fixable.

**Fundamental Limitations:**
LLMs cannot correct their own reasoning without external feedback, and no prior work shows successful intrinsic self-correction using only the model's own feedback. Self-correction sometimes flips correct answers to incorrect ones through prompt bias and cognitive-like biases in the correction process.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49ecfc7c-750c-49f4-af16-9a9bb3bc19d0",
  "isSidechain": false,
  "promptId": "42ed86f0-30d1-4a3d-bc0e-e280317c2813",
  "type": "user",
  "uuid": "8eb7fe69-a480-4e63-9cdb-151840ca5d90",
  "toolUseResult": {
    "query": "LLM correctability prediction self-correction when to correct probe gating 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Wbu3yDbU6tfA8kK5UYi6Qz",
        "content": [
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs",
            "url": "https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"
          },
          {
            "title": "How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals",
            "url": "https://arxiv.org/html/2604.22271v1"
          },
          {
            "title": "Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs | OpenReview",
            "url": "https://openreview.net/forum?id=956KYtqwcU"
          },
          {
            "title": "Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/pdf/2512.20578"
          },
          {
            "title": "Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis",
            "url": "https://arxiv.org/pdf/2601.00828"
          },
          {
            "title": "Confidence v.s. Critique: A Decomposition of Self-Correction Capability   for LLMs",
            "url": "https://arxiv.org/pdf/2412.19513"
          }
        ]
      },
      "I found several relevant research papers on LLM self-correction and correctability prediction from 2025-2026. Here are the key findings:\n\n## Recent Research on LLM Self-Correction (2025-2026)\n\n**Confidence Signals and Error Detection:**\nResearch addresses whether a model's own confidence predicts whether it will identify an error and whether a correction attempt will succeed, examining this both behaviorally through verbal confidence and representationally through internal activations. Recent work showed that LLMs cache an evaluative representation that drives verbal confidence and dissociates from log-probabilities, with this signal extending to error detection and self-correction—predicting which errors the model can correct.\n\n**Comprehensive Benchmarking:**\nCorrectBench was introduced as the first comprehensive benchmark for systematically evaluating self-correction mechanisms in LLMs, evaluating the effectiveness of intrinsic, external, and fine-tuned approaches across commonsense reasoning, mathematical reasoning, and code generation.\n\n**The Accuracy-Correction Paradox:**\nResearch uncovered a striking paradox where weaker models achieve higher intrinsic correction rates than stronger models, with the Error Depth Hypothesis proposing that stronger models make \"deeper\" errors that resist self-correction, while weaker models make \"shallower\" errors that are easily fixable.\n\n**Fundamental Limitations:**\nLLMs cannot correct their own reasoning without external feedback, and no prior work shows successful intrinsic self-correction using only the model's own feedback. Self-correction sometimes flips correct answers to incorrect ones through prompt bias and cognitive-like biases in the correction process."
    ],
    "durationSeconds": 7.65435755,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "49ecfc7c-750c-49f4-af16-9a9bb3bc19d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37 · 2026-05-20T03:23:07.119Z_

```json
{
  "parentUuid": "8eb7fe69-a480-4e63-9cdb-151840ca5d90",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "0279a6ef-d6dc-420f-818c-c57171164386",
  "timestamp": "2026-05-20T03:23:07.119Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 38 · 2026-05-20T03:23:11.879Z_

<details><summary>Logged reasoning block</summary>

```text
Let me search for a few more things:
1. The specific paper about "Wait" token in LLM reasoning (this seems related to budget forcing / thinking tokens)
2. The paper arXiv:2510.04128 about crosscoder analysis of Wait-token mechanisms
3. More about "correctability" as a distinct concept from "correctness" in recent literature
4. The specific paper arXiv:2604.22271 that just appeared about internal confidence signals for self-correction
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0279a6ef-d6dc-420f-818c-c57171164386",
  "isSidechain": false,
  "requestId": "req_011CbD6yoH1eJf2UDS7UyG4H",
  "type": "assistant",
  "uuid": "d2cc0015-b2b3-4c54-9702-c14ed56d6bc5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ACWvnL1hJ9DH3ezeBpWM1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4489,
      "cache_read_input_tokens": 20083,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4489,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 326,
          "cache_read_input_tokens": 20083,
          "cache_creation_input_tokens": 4489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4489
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

_source line 39 · 2026-05-20T03:23:12.875Z_

让我继续搜索更多关键引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2cc0015-b2b3-4c54-9702-c14ed56d6bc5",
  "isSidechain": false,
  "requestId": "req_011CbD6yoH1eJf2UDS7UyG4H",
  "type": "assistant",
  "uuid": "7a0135eb-4029-49e8-809f-1177f0fd731a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ACWvnL1hJ9DH3ezeBpWM1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4489,
      "cache_read_input_tokens": 20083,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4489,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 326,
          "cache_read_input_tokens": 20083,
          "cache_creation_input_tokens": 4489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4489
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

_source line 40 · 2026-05-20T03:23:13.377Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F3pVbRdmzR6WGrT4y1To6A`</summary>

```json
{
  "query": "arXiv 2510.04128 crosscoder Wait token mechanisms LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a0135eb-4029-49e8-809f-1177f0fd731a",
  "isSidechain": false,
  "requestId": "req_011CbD6yoH1eJf2UDS7UyG4H",
  "type": "assistant",
  "uuid": "938e9bfb-9265-401f-bfc8-5727f17d25cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ACWvnL1hJ9DH3ezeBpWM1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4489,
      "cache_read_input_tokens": 20083,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4489,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 326,
          "cache_read_input_tokens": 20083,
          "cache_creation_input_tokens": 4489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4489
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

_source line 41 · 2026-05-20T03:23:13.863Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011W4jRzPr28D2SSedaSBtsN`</summary>

```json
{
  "query": "arXiv 2604.22271 LLMs detect correct errors internal confidence signals 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "938e9bfb-9265-401f-bfc8-5727f17d25cf",
  "isSidechain": false,
  "requestId": "req_011CbD6yoH1eJf2UDS7UyG4H",
  "type": "assistant",
  "uuid": "fc7f1079-f097-44db-8c8c-fe17d4546f76",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ACWvnL1hJ9DH3ezeBpWM1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4489,
      "cache_read_input_tokens": 20083,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4489,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 326,
          "cache_read_input_tokens": 20083,
          "cache_creation_input_tokens": 4489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4489
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

_source line 42 · 2026-05-20T03:23:15.043Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JyCzp2AyQAHTfaYMR6JoqB`</summary>

```json
{
  "query": "\"LLMs Encode Their Failures\" arXiv 2602.09924 pre-generation activations predict success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc7f1079-f097-44db-8c8c-fe17d4546f76",
  "isSidechain": false,
  "requestId": "req_011CbD6yoH1eJf2UDS7UyG4H",
  "type": "assistant",
  "uuid": "d6d5015f-b64c-40c6-b5e7-fb3129f9c143",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ACWvnL1hJ9DH3ezeBpWM1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4489,
      "cache_read_input_tokens": 20083,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4489,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 326,
          "cache_read_input_tokens": 20083,
          "cache_creation_input_tokens": 4489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4489
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

_source line 43 · 2026-05-20T03:23:18.303Z_

<details><summary>↩ Tool result · `toolu_011W4jRzPr28D2SSedaSBtsN`</summary>

```text
Web search results for query: "arXiv 2604.22271 LLMs detect correct errors internal confidence signals 2026"

Links: [{"title":"How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals","url":"https://arxiv.org/html/2604.22271v1"},{"title":"On LLMs' Internal Representation of Code Correctness","url":"https://arxiv.org/pdf/2512.07404"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/pdf/2512.20578"},{"title":"InternalInspector $I^2$: Robust Confidence Estimation in LLMs through   Internal States","url":"https://arxiv.org/pdf/2406.12053"},{"title":"Know When You're Wrong: Aligning Confidence with Correctness for LLM Error Detection","url":"https://arxiv.org/pdf/2603.06604"},{"title":"Can LLMs Detect Their Confabulations? Estimating Reliability in Uncertainty-Aware Language Models","url":"https://arxiv.org/pdf/2508.08139"},{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/pdf/2602.08159"}]

I found the paper you're looking for! Here's what I found:

The paper arXiv:2604.22271 addresses how large language models can detect their own errors and sometimes correct them without external feedback, investigating the underlying mechanisms.

The researchers investigate this through the lens of second-order models of confidence from decision neuroscience, where second-order models posit a partially independent evaluative signal that can disagree with the committed response, providing the basis for error detection.

The paper is titled "How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals" and was published on April 24, 2026. You can access the full paper at: https://arxiv.org/html/2604.22271v1


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc7f1079-f097-44db-8c8c-fe17d4546f76",
  "isSidechain": false,
  "promptId": "42ed86f0-30d1-4a3d-bc0e-e280317c2813",
  "type": "user",
  "uuid": "85b6b6a5-5d07-47ac-925b-6894913a897f",
  "toolUseResult": {
    "query": "arXiv 2604.22271 LLMs detect correct errors internal confidence signals 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EptuwjMrNN7mpPYuDfonRA",
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
            "title": "Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/pdf/2512.20578"
          },
          {
            "title": "InternalInspector $I^2$: Robust Confidence Estimation in LLMs through   Internal States",
            "url": "https://arxiv.org/pdf/2406.12053"
          },
          {
            "title": "Know When You're Wrong: Aligning Confidence with Correctness for LLM Error Detection",
            "url": "https://arxiv.org/pdf/2603.06604"
          },
          {
            "title": "Can LLMs Detect Their Confabulations? Estimating Reliability in Uncertainty-Aware Language Models",
            "url": "https://arxiv.org/pdf/2508.08139"
          },
          {
            "title": "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models",
            "url": "https://arxiv.org/pdf/2602.08159"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I found:\n\nThe paper arXiv:2604.22271 addresses how large language models can detect their own errors and sometimes correct them without external feedback, investigating the underlying mechanisms.\n\nThe researchers investigate this through the lens of second-order models of confidence from decision neuroscience, where second-order models posit a partially independent evaluative signal that can disagree with the committed response, providing the basis for error detection.\n\nThe paper is titled \"How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals\" and was published on April 24, 2026. You can access the full paper at: https://arxiv.org/html/2604.22271v1"
    ],
    "durationSeconds": 4.436209758999991,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fc7f1079-f097-44db-8c8c-fe17d4546f76",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T03:23:20.848Z_

<details><summary>↩ Tool result · `toolu_01F3pVbRdmzR6WGrT4y1To6A`</summary>

```text
Web search results for query: "arXiv 2510.04128 crosscoder Wait token mechanisms LLM"

Links: [{"title":"[2510.04128] Internal states before wait modulate reasoning patterns","url":"https://arxiv.org/abs/2510.04128"},{"title":"Oops, Wait: Token-Level Signals as a Lens into LLM Reasoning","url":"https://arxiv.org/pdf/2601.17421"},{"title":"Internal states before wait modulate reasoning patterns","url":"https://arxiv.org/pdf/2510.04128"},{"title":"Crosscoding Through Time: Tracking Emergence & Consolidation Of Linguistic Representations Throughout LLM Pretraining","url":"https://arxiv.org/html/2509.05291"},{"title":"Internal states before wait modulate reasoning patterns","url":"https://arxiv.org/html/2510.04128"},{"title":"CrossLMM: Decoupling Long Video Sequences from LMMs via Dual Cross-Attention Mechanisms","url":"https://arxiv.org/pdf/2505.17020"}]

Based on the search results, here's what I found about arXiv paper 2510.04128:

**Title:** Internal states before wait modulate reasoning patterns

**Overview:**
The token "wait" often signals reasoning behavior such as backtracking in language models. The paper investigates whether the model's internal states before generating wait tokens contain relevant information for the subsequent reasoning process.

**Methodology:**
The researchers train crosscoders at multiple layers of DeepSeek-R1-Distill-Llama-8B and its base version, and introduce a latent attribution technique in the crosscoder setting.

**Key Findings:**
They locate a small set of features relevant for promoting/suppressing wait tokens' probabilities. Through experiments analyzing max-activating examples and causal interventions, they show that many of their identified features are relevant for the reasoning process and give rise to different types of reasoning patterns such as restarting from the beginning, recalling prior knowledge, expressing uncertainty, and double-checking.

The paper was published on October 5, 2025, and uses crosscoders, a mechanistic interpretability technique, to understand how reasoning models decide when to pause and reason (via wait tokens) during problem-solving.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "938e9bfb-9265-401f-bfc8-5727f17d25cf",
  "isSidechain": false,
  "promptId": "42ed86f0-30d1-4a3d-bc0e-e280317c2813",
  "type": "user",
  "uuid": "0d7bc4cc-5734-4600-8848-0f7fed799835",
  "toolUseResult": {
    "query": "arXiv 2510.04128 crosscoder Wait token mechanisms LLM",
    "results": [
      {
        "tool_use_id": "srvtoolu_011YQHz2ayZp78VARnrGZmxZ",
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
            "url": "https://arxiv.org/pdf/2510.04128"
          },
          {
            "title": "Crosscoding Through Time: Tracking Emergence & Consolidation Of Linguistic Representations Throughout LLM Pretraining",
            "url": "https://arxiv.org/html/2509.05291"
          },
          {
            "title": "Internal states before wait modulate reasoning patterns",
            "url": "https://arxiv.org/html/2510.04128"
          },
          {
            "title": "CrossLMM: Decoupling Long Video Sequences from LMMs via Dual Cross-Attention Mechanisms",
            "url": "https://arxiv.org/pdf/2505.17020"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2510.04128:\n\n**Title:** Internal states before wait modulate reasoning patterns\n\n**Overview:**\nThe token \"wait\" often signals reasoning behavior such as backtracking in language models. The paper investigates whether the model's internal states before generating wait tokens contain relevant information for the subsequent reasoning process.\n\n**Methodology:**\nThe researchers train crosscoders at multiple layers of DeepSeek-R1-Distill-Llama-8B and its base version, and introduce a latent attribution technique in the crosscoder setting.\n\n**Key Findings:**\nThey locate a small set of features relevant for promoting/suppressing wait tokens' probabilities. Through experiments analyzing max-activating examples and causal interventions, they show that many of their identified features are relevant for the reasoning process and give rise to different types of reasoning patterns such as restarting from the beginning, recalling prior knowledge, expressing uncertainty, and double-checking.\n\nThe paper was published on October 5, 2025, and uses crosscoders, a mechanistic interpretability technique, to understand how reasoning models decide when to pause and reason (via wait tokens) during problem-solving."
    ],
    "durationSeconds": 7.463562523,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "938e9bfb-9265-401f-bfc8-5727f17d25cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-20T03:23:22.539Z_

<details><summary>↩ Tool result · `toolu_01JyCzp2AyQAHTfaYMR6JoqB`</summary>

```text
Web search results for query: ""LLMs Encode Their Failures" arXiv 2602.09924 pre-generation activations predict success"

Links: [{"title":"[2602.09924] LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations","url":"https://arxiv.org/abs/2602.09924"},{"title":"LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations","url":"https://arxiv.org/html/2602.09924"},{"title":"llms encode their failures: predicting suc","url":"https://arxiv.org/pdf/2602.09924"},{"title":"Understanding LLM Failures: A Multi-Tape Turing Machine Analysis of Systematic Errors in Language Model Reasoning","url":"https://arxiv.org/pdf/2602.15868"},{"title":"Uncovering Systematic Failures of LLMs in Verifying Code Against Natural Language Specifications","url":"https://arxiv.org/pdf/2508.12358"},{"title":"Understanding LLM Failures: A Multi-Tape Turing Machine Analysis of Systematic Errors in Language Model Reasoning","url":"https://arxiv.org/html/2602.15868v2"}]

I found the paper! Here's what I found about "LLMs Encode Their Failures":

## Paper Overview

The paper, submitted on February 10, 2026 with the most recent version on April 6, 2026, investigates whether LLMs' likelihood of success is recoverable from internal representations before generation and whether this signal can guide more efficient inference.

## Key Methodology

The researchers train linear probes on pre-generation activations to predict policy-specific success on math and coding tasks, substantially outperforming surface features such as question length and TF-IDF.

## Main Findings

Using E2H-AMC, which provides both human and model performance on identical problems, they show that models encode a model-specific notion of difficulty that is distinct from human difficulty, and that this distinction increases with extended reasoning.

The researchers demonstrate that probe-guided routing can match high-compute accuracy at 40% cost reduction, while identifying critical failure modes where probe reliability becomes the bottleneck.

## Authors

The paper is authored by William Lugoloobi, Thomas Foster, William Bankes, and Chris Russell from Oxford Internet Institute, FLAIR at University of Oxford, and the Department of Computer Science at University College London.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6d5015f-b64c-40c6-b5e7-fb3129f9c143",
  "isSidechain": false,
  "promptId": "42ed86f0-30d1-4a3d-bc0e-e280317c2813",
  "type": "user",
  "uuid": "4d7c8dae-b5bb-4cb6-9281-39e0ce6c221b",
  "toolUseResult": {
    "query": "\"LLMs Encode Their Failures\" arXiv 2602.09924 pre-generation activations predict success",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CG3AXeXUZyK5bdvgZDLPgW",
        "content": [
          {
            "title": "[2602.09924] LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations",
            "url": "https://arxiv.org/abs/2602.09924"
          },
          {
            "title": "LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations",
            "url": "https://arxiv.org/html/2602.09924"
          },
          {
            "title": "llms encode their failures: predicting suc",
            "url": "https://arxiv.org/pdf/2602.09924"
          },
          {
            "title": "Understanding LLM Failures: A Multi-Tape Turing Machine Analysis of Systematic Errors in Language Model Reasoning",
            "url": "https://arxiv.org/pdf/2602.15868"
          },
          {
            "title": "Uncovering Systematic Failures of LLMs in Verifying Code Against Natural Language Specifications",
            "url": "https://arxiv.org/pdf/2508.12358"
          },
          {
            "title": "Understanding LLM Failures: A Multi-Tape Turing Machine Analysis of Systematic Errors in Language Model Reasoning",
            "url": "https://arxiv.org/html/2602.15868v2"
          }
        ]
      },
      "I found the paper! Here's what I found about \"LLMs Encode Their Failures\":\n\n## Paper Overview\n\nThe paper, submitted on February 10, 2026 with the most recent version on April 6, 2026, investigates whether LLMs' likelihood of success is recoverable from internal representations before generation and whether this signal can guide more efficient inference.\n\n## Key Methodology\n\nThe researchers train linear probes on pre-generation activations to predict policy-specific success on math and coding tasks, substantially outperforming surface features such as question length and TF-IDF.\n\n## Main Findings\n\nUsing E2H-AMC, which provides both human and model performance on identical problems, they show that models encode a model-specific notion of difficulty that is distinct from human difficulty, and that this distinction increases with extended reasoning.\n\nThe researchers demonstrate that probe-guided routing can match high-compute accuracy at 40% cost reduction, while identifying critical failure modes where probe reliability becomes the bottleneck.\n\n## Authors\n\nThe paper is authored by William Lugoloobi, Thomas Foster, William Bankes, and Chris Russell from Oxford Internet Institute, FLAIR at University of Oxford, and the Department of Computer Science at University College London."
    ],
    "durationSeconds": 7.485674482000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d6d5015f-b64c-40c6-b5e7-fb3129f9c143",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "4d7c8dae-b5bb-4cb6-9281-39e0ce6c221b",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM correctability prediction proposal",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94"
}
```

---

### Assistant

_source line 48 · 2026-05-20T03:23:45.467Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a very comprehensive picture of the field. Let me also search for "The Confidence Manifold" paper (arXiv:2602.08159) which appeared in the last search results, and look for any work specifically on "correctability" as a distinct property from "correctness".
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d7c8dae-b5bb-4cb6-9281-39e0ce6c221b",
  "isSidechain": false,
  "requestId": "req_011CbD6zwW9EHTcPFxHtkp4m",
  "type": "assistant",
  "uuid": "90c80116-04b6-4615-96eb-5ac48bcf5c8f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bjh9vnyXmLhxvVtmW16SYD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2071,
      "cache_read_input_tokens": 24572,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 24572,
          "cache_creation_input_tokens": 2071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2071
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

_source line 49 · 2026-05-20T03:23:46.409Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01633NGUbuQLgNuGjTxVnu9W`</summary>

```json
{
  "query": "\"Confidence Manifold\" arXiv 2602.08159 geometric structure correctness representations language models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90c80116-04b6-4615-96eb-5ac48bcf5c8f",
  "isSidechain": false,
  "requestId": "req_011CbD6zwW9EHTcPFxHtkp4m",
  "type": "assistant",
  "uuid": "56afe9bf-8cd3-4bdf-b3fb-1c3e03e3ad7e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bjh9vnyXmLhxvVtmW16SYD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2071,
      "cache_read_input_tokens": 24572,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 24572,
          "cache_creation_input_tokens": 2071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2071
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

_source line 50 · 2026-05-20T03:23:47.139Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0166ABS8ggEEB7yRj6DCkcpS`</summary>

```json
{
  "query": "LLM self-correction overcorrection cost correct answers flipping 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56afe9bf-8cd3-4bdf-b3fb-1c3e03e3ad7e",
  "isSidechain": false,
  "requestId": "req_011CbD6zwW9EHTcPFxHtkp4m",
  "type": "assistant",
  "uuid": "00e32521-cdd0-484e-8494-db6c91f80816",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bjh9vnyXmLhxvVtmW16SYD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2071,
      "cache_read_input_tokens": 24572,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 24572,
          "cache_creation_input_tokens": 2071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2071
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

_source line 51 · 2026-05-20T03:23:52.095Z_

<details><summary>↩ Tool result · `toolu_01633NGUbuQLgNuGjTxVnu9W`</summary>

```text
Web search results for query: ""Confidence Manifold" arXiv 2602.08159 geometric structure correctness representations language models"

Links: [{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/html/2602.08159v1"},{"title":"The Confidence Manifold:","url":"https://www.arxiv.org/pdf/2602.08159"},{"title":"The Confidence Manifold - Seongland","url":"https://seongland.com/article/confidence-manifold/"},{"title":"(PDF) The Confidence Manifold: Geometric Structure of ...","url":"https://www.researchgate.net/publication/400604407_The_Confidence_Manifold_Geometric_Structure_of_Correctness_Representations_in_Language_Models"},{"title":"What Topological and Geometric Structure Do Biological Foundation Models Learn? Evidence from 141 Hypotheses","url":"https://arxiv.org/html/2602.22289v1"},{"title":"Geometric Manifold Rectification for Imbalanced Learning","url":"https://arxiv.org/html/2602.13045"},{"title":"Representational geometry explains puzzling error distributions in behavioral tasks","url":"https://www.biorxiv.org/content/10.1101/2023.01.03.522667.full.pdf"},{"title":"Variational Geometric Information Bottleneck: Learning the Shape of Understanding","url":"https://arxiv.org/pdf/2511.02496"}]

I found the paper you're looking for! Here's what the search revealed:

## The Confidence Manifold (arXiv 2602.08159)

The research characterizes the geometry of correctness representations across 9 models from 5 architecture families, finding that the discriminative signal occupies 3–8 dimensions, performance degrades with additional dimensions, and no nonlinear classifier improves over linear separation.

### Key Findings:

The analysis reveals three key findings: (1) intrinsic dimension follows a compression pattern with initial expansion in early layers (peaking around 10–20% depth) before decreasing through middle and late layers, (2) probe weight similarity exhibits block-diagonal structure indicating distinct processing phases, and (3) dimension alone explains only 18% of classification variance with the orientation of the low-dimensional subspace mattering more than its dimensionality.

The research was published on February 8, 2026, and explores how language models represent correctness through geometric structures in their internal representations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56afe9bf-8cd3-4bdf-b3fb-1c3e03e3ad7e",
  "isSidechain": false,
  "promptId": "42ed86f0-30d1-4a3d-bc0e-e280317c2813",
  "type": "user",
  "uuid": "1a3c1b9c-f5e1-4ead-a493-d4ff0e83831e",
  "toolUseResult": {
    "query": "\"Confidence Manifold\" arXiv 2602.08159 geometric structure correctness representations language models",
    "results": [
      {
        "tool_use_id": "srvtoolu_01J98aND1dJWuAe5Xu5ufdDg",
        "content": [
          {
            "title": "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models",
            "url": "https://arxiv.org/html/2602.08159v1"
          },
          {
            "title": "The Confidence Manifold:",
            "url": "https://www.arxiv.org/pdf/2602.08159"
          },
          {
            "title": "The Confidence Manifold - Seongland",
            "url": "https://seongland.com/article/confidence-manifold/"
          },
          {
            "title": "(PDF) The Confidence Manifold: Geometric Structure of ...",
            "url": "https://www.researchgate.net/publication/400604407_The_Confidence_Manifold_Geometric_Structure_of_Correctness_Representations_in_Language_Models"
          },
          {
            "title": "What Topological and Geometric Structure Do Biological Foundation Models Learn? Evidence from 141 Hypotheses",
            "url": "https://arxiv.org/html/2602.22289v1"
          },
          {
            "title": "Geometric Manifold Rectification for Imbalanced Learning",
            "url": "https://arxiv.org/html/2602.13045"
          },
          {
            "title": "Representational geometry explains puzzling error distributions in behavioral tasks",
            "url": "https://www.biorxiv.org/content/10.1101/2023.01.03.522667.full.pdf"
          },
          {
            "title": "Variational Geometric Information Bottleneck: Learning the Shape of Understanding",
            "url": "https://arxiv.org/pdf/2511.02496"
          }
        ]
      },
      "I found the paper you're looking for! Here's what the search revealed:\n\n## The Confidence Manifold (arXiv 2602.08159)\n\nThe research characterizes the geometry of correctness representations across 9 models from 5 architecture families, finding that the discriminative signal occupies 3–8 dimensions, performance degrades with additional dimensions, and no nonlinear classifier improves over linear separation.\n\n### Key Findings:\n\nThe analysis reveals three key findings: (1) intrinsic dimension follows a compression pattern with initial expansion in early layers (peaking around 10–20% depth) before decreasing through middle and late layers, (2) probe weight similarity exhibits block-diagonal structure indicating distinct processing phases, and (3) dimension alone explains only 18% of classification variance with the orientation of the low-dimensional subspace mattering more than its dimensionality.\n\nThe research was published on February 8, 2026, and explores how language models represent correctness through geometric structures in their internal representations."
    ],
    "durationSeconds": 5.678328987,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "56afe9bf-8cd3-4bdf-b3fb-1c3e03e3ad7e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T03:23:54.302Z_

<details><summary>↩ Tool result · `toolu_0166ABS8ggEEB7yRj6DCkcpS`</summary>

```text
Web search results for query: "LLM self-correction overcorrection cost correct answers flipping 2025 2026"

Links: [{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"},{"title":"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs | OpenReview","url":"https://openreview.net/forum?id=956KYtqwcU"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://arxiv.org/html/2406.01297v1"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/When-Can-LLMs-Actually-Correct-Their-Own-Mistakes"},{"title":"Confidence v.s. Critique: A Decomposition of Self-Correction Capability   for LLMs","url":"https://arxiv.org/pdf/2412.19513"},{"title":"Large Language Models Cannot Self-Correct Reasoning Yet | OpenReview","url":"https://openreview.net/forum?id=IkmD3fKBPQ"},{"title":"LLMs cannot find reasoning errors, but can correct them given the error   location","url":"https://arxiv.org/pdf/2311.08516"}]

Based on the search results, here's what recent research has found about LLM self-correction and the problem of overcorrection:

## Key Findings on Self-Correction Overcorrection

Research from 2025 found that self-correction sometimes flips correct answers to incorrect ones through prompt bias and cognitive-like biases in the correction process. This is a critical issue that undermines the effectiveness of self-correction approaches.

## The Cost-Benefit Problem

Self-correction can lead to better responses at the cost of increased inference time. However, this benefit comes with a significant downside: LLMs can turn correct answers to incorrect ones or fail to correct erroneous answers.

## Overall State of LLM Self-Correction

Research shows that no prior work demonstrates successful self-correction with feedback from prompted LLMs in general tasks, self-correction works well in tasks that can use reliable external feedback, and large-scale fine-tuning enables self-correction. 

Research indicates that LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction.

The research landscape indicates that while self-correction is theoretically appealing, the practical reality—particularly the problem of flipping correct answers to incorrect ones—remains a significant challenge in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00e32521-cdd0-484e-8494-db6c91f80816",
  "isSidechain": false,
  "promptId": "42ed86f0-30d1-4a3d-bc0e-e280317c2813",
  "type": "user",
  "uuid": "805e4294-c075-4547-9689-0d3dcae00421",
  "toolUseResult": {
    "query": "LLM self-correction overcorrection cost correct answers flipping 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01C4RtvRbMcjYsy8JmEaJe9B",
        "content": [
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs",
            "url": "https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"
          },
          {
            "title": "Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs | OpenReview",
            "url": "https://openreview.net/forum?id=956KYtqwcU"
          },
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs",
            "url": "https://arxiv.org/html/2406.01297v1"
          },
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs | Transactions of the Association for Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/When-Can-LLMs-Actually-Correct-Their-Own-Mistakes"
          },
          {
            "title": "Confidence v.s. Critique: A Decomposition of Self-Correction Capability   for LLMs",
            "url": "https://arxiv.org/pdf/2412.19513"
          },
          {
            "title": "Large Language Models Cannot Self-Correct Reasoning Yet | OpenReview",
            "url": "https://openreview.net/forum?id=IkmD3fKBPQ"
          },
          {
            "title": "LLMs cannot find reasoning errors, but can correct them given the error   location",
            "url": "https://arxiv.org/pdf/2311.08516"
          }
        ]
      },
      "Based on the search results, here's what recent research has found about LLM self-correction and the problem of overcorrection:\n\n## Key Findings on Self-Correction Overcorrection\n\nResearch from 2025 found that self-correction sometimes flips correct answers to incorrect ones through prompt bias and cognitive-like biases in the correction process. This is a critical issue that undermines the effectiveness of self-correction approaches.\n\n## The Cost-Benefit Problem\n\nSelf-correction can lead to better responses at the cost of increased inference time. However, this benefit comes with a significant downside: LLMs can turn correct answers to incorrect ones or fail to correct erroneous answers.\n\n## Overall State of LLM Self-Correction\n\nResearch shows that no prior work demonstrates successful self-correction with feedback from prompted LLMs in general tasks, self-correction works well in tasks that can use reliable external feedback, and large-scale fine-tuning enables self-correction. \n\nResearch indicates that LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction.\n\nThe research landscape indicates that while self-correction is theoretically appealing, the practical reality—particularly the problem of flipping correct answers to incorrect ones—remains a significant challenge in 2025-2026."
    ],
    "durationSeconds": 7.158986347000012,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "00e32521-cdd0-484e-8494-db6c91f80816",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-20T03:25:18.873Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture of the field. Let me synthesize my findings and produce the evaluation.

Let me think through this proposal carefully:

## Understanding the Proposal

The core idea is:
1. LLMs have internal representations that can predict whether their errors are "self-correctable" (as opposed to just predicting whether they're correct/incorrect)
2. Build "Enhanced Correctability Probes" (ECP) using multi-layer ensembles, multi-token features, attention-entropy, SAE-guided features
3. Use these probes to gate a three-way decision: keep answer / attempt correction / abstain


4. Compare against baselines including ungated correction, "Wait" baseline, confidence-based routing

## Key Claims to Evaluate

The main novelty hinges on whether "correctability" is genuinely distinct from "correctness" as a prediction target, whether the multi-layer ensemble approach transfers meaningfully from deception detection, and whether hidden-state probes with abstention capability outperform simpler confidence-based routing like CoRefine uses.

## Trivial Alternative Check

The obvious concern is that confidence-based routing might already capture most of the value. But there's a deeper question: even if I can detect that an answer is wrong, can I tell whether it's fixable or fundamentally broken? Some errors might be shallow and correctable while others are rooted in deep misunderstandings. The real test is whether the model's hidden representations can actually distinguish between these two cases, and whether that distinction translates to better routing decisions than just using confidence scores alone.

## Novelty Assessment

Looking at what's actually new here versus what's just combining existing pieces: the "correctability" framing as an explicit prediction target has some precedent—papers on error detection and error depth already touch on this conceptually. Building probes specifically for it might add incremental novelty, but it's not groundbreaking. The multi-layer ensemble probing is directly borrowed from existing work, and the three-way gating with abstention is a minor extension of routing schemes that already exist. The representational geometry angle is interesting, but confidence manifold papers have already explored how correctness structures itself in representation space.

## Significance Assessment

The overcorrection problem is real and worth solving, but the field is saturated with recent work on this exact issue. What matters is whether correctability probes actually outperform simpler baselines—that's where the practical contribution lives. The proposal essentially stacks together existing techniques: multi-layer ensembles, SAE feature decomposition, and crosscoder analysis. It's solid engineering but not a conceptual breakthrough.

## Concerns

The proposal reads like a greatest hits compilation of recent techniques rather than a unified insight.

Correctability isn't cleanly separable from existing work—error depth papers and internal confidence studies already cover much of this ground, which weakens the novelty claim. The "publishable even if negative" framing also feels like hedging rather than confidence in the core idea.

The proposal stacks so many techniques together that it's hard to isolate what actually matters—if results are positive, which component drove it? If negative, what's the takeaway? And there's a fundamental venue mismatch here since this is an NLP interpretability paper being submitted to a robotics conference, though I should focus on evaluating the idea itself as requested. There's definitely a venue mismatch here—CoRL is the Conference on Robot Learning, but this proposal is entirely about LLM self-correction, which has nothing to do with robotics. That said, the evaluation rubric explicitly mentions "NLP/CL 领域," so I should assess this as an NLP paper and flag the venue concern separately. Now I'm working through the actual idea quality, starting with whether there are simpler alternatives to what they're proposing.

The confidence-based routing approach is the obvious baseline, and while they acknowledge it, their claim that hidden-state probes are superior is purely empirical and unproven. There's also a more fundamental issue: if you can already detect when a model is wrong, you essentially know when to attempt correction—so the added value of predicting "correctability" specifically versus just "correctness" lacks theoretical grounding and hinges entirely on whether the model can internally distinguish between fixable and unfixable errors.

The deeper problem is that their core premise—that correctability is a linearly separable property in the model's hidden states, distinct from correctness—is completely unvalidated. There's no theoretical justification for why this should be true, and recent work suggests that even correctness features themselves are largely functionally inert in these models.

The novelty is modest since each component draws from existing work, and while the combination is new, it's not particularly surprising. The concept of correctability as distinct from correctness has some novelty but sits close to related ideas like error depth and internal confidence signals. The significance is medium—self-correction is important, but this approach is engineering-focused with limited scientific insight. The related work section shows good awareness of the field, though that also reveals how saturated this research area has become. I'd put the acceptance probability around 15-25%—it's a reasonable incremental extension but lacks a compelling novel core.

Looking more carefully at what a reviewer would actually say: the problem is well-motivated and the related work coverage is solid, but correctability feels too similar to existing concepts, the method just combines borrowed techniques without theoretical grounding for why correctability should even be detectable, and the approach seems over-engineered with too many techniques layered together. If results are positive, it's unclear which component drove it; if negative, there's little to learn. The dual-outcome framing itself signals weak confidence in the core hypothesis. I think 18-22% is probably the right central estimate for idea quality alone, though the venue mismatch with CoRL is another separate concern.

Now considering the actual evaluation context: for NLP venues like ACL or EMNLP this lands in the 15-25% range, but for CoRL it would be essentially zero since it's completely off-topic. For NeurIPS or ICML it might edge slightly higher if the interpretability angle is executed well. Since the rubric focuses on NLP, I should evaluate against those standards.

The real question is whether correctability as a distinct prediction target is actually novel. There's already work directly examining what internal signals drive error detection and correction, and other papers decomposing the accuracy-correction paradox—both of which cover very similar ground.

I'm also seeing that probe-guided routing approaches have already demonstrated matching high-compute accuracy at significant cost reduction, which is quite close to the gating mechanism being proposed here.

The novelty is actually quite constrained. While the error depth paper identifies that stronger models make fewer but deeper errors, it doesn't build probes to predict which specific errors fall into each category. Similarly, the internal confidence work shows that confidence predicts correction success, but doesn't frame this as a separate prediction target. So there might be a small gap to fill, but it's narrow.

The real question is whether explicitly building probes to predict "can the model fix this error?" constitutes enough of a contribution for a top venue. This feels borderline—some reviewers would appreciate the systematic approach, while others might view it as combining existing ideas without substantial novelty. I'm settling on a weak-to-medium novelty score since the conceptual contribution is incremental despite having some merit.

For significance, the work addresses an important problem but probably won't shift how we think about error correction. The related work section is thorough and clearly positions this against CoRefine and other baselines. My overall probability estimate is around 20%, though I should flag that if this is genuinely being submitted to CoRL 2026, the venue mismatch makes it essentially non-viable since there's no robotics component. But evaluating it as an NLP submission, the main risks are that the core concept overlaps too closely with existing work on error depth and internal confidence signals, and the approach amounts to engineering a combination of borrowed techniques without a clear scientific insight.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "805e4294-c075-4547-9689-0d3dcae00421",
  "isSidechain": false,
  "requestId": "req_011CbD73Gyy4J2pHDcTbd4hP",
  "type": "assistant",
  "uuid": "1212eca0-fb43-4632-aa72-138bd36d285c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RUcmNQPinSTt24NtVu6R31",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1638,
      "cache_read_input_tokens": 26643,
      "output_tokens": 7458,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1638,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7458,
          "cache_read_input_tokens": 26643,
          "cache_creation_input_tokens": 1638,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1638
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

_source line 54 · 2026-05-20T03:26:44.654Z_

现在我已经完成了充分的领域调研，可以进行系统评估了。

---

```
【阶段】: Triage

【领域调研】:

1. [arXiv:2604.22271] "How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals" (2026.04):
   — 直接竞争者。该论文从决策神经科学的"二阶模型"出发，研究 LLM 内部的评价性信号如何驱动错误检测与自我修正，发现 LLM 缓存了一个独立于 log-prob 的评价性表征，能预测哪些错误模型可以修正。这与本 proposal 的核心 claim（用内部表征预测 correctability）高度重叠。

2. [arXiv:2601.00828] "Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis" (2025.12):
   — 直接前驱。该论文将 self-correction 分解为 error detection / localization / correction 三个子能力，提出 Error Depth Hypothesis：强模型犯的错误更"深"、更抗修正。这在概念层面与 "correctability" 作为预测目标高度一致——"浅错误=可修正，深错误=不可修正"。

3. [arXiv:2602.09924] "LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations" (2026.02):
   — 密切相关。该论文训练 linear probe on pre-generation activations 预测模型是否会答对，并展示 probe-guided routing 可在减少 40% 计算成本的同时匹配高计算精度。方法论上（probe → gating）与本 proposal 的框架非常接近，区别仅在目标（correctness vs. correctability）。

4. [arXiv:2604.13386] "Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling" (2026.04):
   — 本 proposal 直接引用的方法来源。该论文证明多层 ensemble probe 在 deception detection 上大幅优于单层 probe（+78% AUROC on Harm-Pressure Knowledge）。本 proposal 的"Phase 0 pilot"本质是测试此技术是否 transfer 到 correctability 任务。

5. [arXiv:2604.19974] "Are LLM Uncertainty and Correctness Encoded by the Same Features?" (2026.04):
   — 本 proposal 引用的 SAE 分析基础。该论文区分了 pure uncertainty / pure incorrectness / confounded features 三类特征，发现 68% 的 pure incorrectness features 在因果干预下是 inert 的。本 proposal 拟将此分析框架延伸到 correctability。

6. [arXiv:2602.08159] "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models" (2026.02):
   — 本 proposal 引用的几何分析基础。该论文在 9 个模型上发现 correctness 信号占据 3-8 维、线性可分、非线性分类器无额外提升。本 proposal 拟测试 correctability（二阶属性）是否也具有类似结构。

7. [arXiv:2510.04128] "Internal states before wait modulate reasoning patterns" (2025.10):
   — 本 proposal 引用的 Wait-token 机制分析。使用 crosscoder 定位影响 wait token 概率的特征集。

8. [arXiv:2602.08948] "CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute" (2026.02):
   — 本 proposal 的主要对比系统。CoRefine 使用 output-level confidence 做三路路由（HALT/RETHINK/ALTERNATIVE），211K 参数 Conv1D controller，精度 92.6%。

- 调研总结: 2025-2026 年间，LLM 自我修正的 probe-based gating、内部表征对 correctness/uncertainty 的编码、以及 self-correction 的分解分析已成为非常拥挤的研究方向。本 proposal 的每一个技术组件（multi-layer ensemble probe、SAE feature decomposition、representational geometry analysis、probe-gated routing）均已在近期独立论文中被提出和验证。Proposal 的差异化定位在于将预测目标从 "correctness" 切换为 "correctability"，但这一概念与 Error Depth Hypothesis 和内部 confidence 信号的工作存在显著重叠。


【Trivial Alternative 检验】:
存在多个成本更低的 trivial alternatives：

(1) **直接用 correctness probe 做代理**：既然已经有成熟的 correctness linear probe（AUROC ~0.87，见 LLM Reasoning as Trajectories），可以简单地"检测错误 → 一律尝试修正"，省去 correctability 预测这一步。Proposal 的增量价值取决于"可修正"vs."不可修正"的区分能否提供超过 correctness probe 的显著收益——但这本身是一个 empirical claim，且 Error Depth Hypothesis 已经暗示更强的模型犯的错更少但更难修正，意味着 correctability prediction 可能本身就很难（大多数错误要么都可修正，要么都不可修正）。

(2) **CoRefine 的 confidence-based routing**：CoRefine 使用 output-level confidence 做 routing，精度达 92.6%，且只需 211K 参数。本 proposal 使用 hidden-state probe 做 routing 的增量收益需要超过这个强 baseline，但 hidden-state probe 的额外复杂度（multi-layer extraction, SAE feature selection）是否值得，是一个未回答的问题。

(3) **简单的 logit entropy / verbalized confidence**：多篇论文已表明 logit-based uncertainty 和 verbalized confidence 在某些场景下已经是有效的 proxy。

增量价值在于：如果 correctability 确实是一个与 correctness 不同的、可预测的内部属性，且其预测能带来超越 confidence-based routing 的 gating 收益。但这是一个层层叠加的条件假设，每层都有 fail 的风险。


【前提假设检验】:
核心 claim 的逻辑链存在多个未验证的前提假设：

(1) **"Correctability 是模型内部表征中一个可检测的、与 correctness 不同的独立属性"** —— 这是最关键的假设，完全没有理论或实证支撑。已有证据反而不利：arXiv:2604.19974 发现 68% 的 pure incorrectness features 是 causally inert 的。如果 correctness 的一阶属性都在内部表征中缺乏 causal footprint，一个依赖于 correctness 的二阶属性（correctability = "wrong AND fixable"）为什么会有更强的可检测信号？没有理论解释。

(2) **"Multi-layer ensemble 从 deception detection transfer 到 correctability"** —— Deception 是一个有意的、二元的行为（模型"知道"正确答案但选择输出错误答案），内部表征的几何结构可能与 correctability（模型不知道正确答案但可能通过 reasoning 找到）完全不同。Transfer 假设缺乏理论支撑。

(3) **"三路 gating 优于二路 gating"** —— 添加 abstain 选项的前提是 correctability probe 能可靠区分"可修正"和"不可修正"的错误。如果 probe 精度不够，三路 gating 反而可能比二路更差（多了一个错误分类的维度）。

(4) **Prior work 的 0.614 AUROC 意味着 "insufficient but improvable"** —— 这假设了信号存在但 extraction 方法不够好。但另一种解释是：信号本身就很弱（correctability 可能不是一个被模型内部清晰编码的属性），再好的 probe 也不会提升太多。


【3 维度打分】:

1. **Novelty: 弱** — 
   核心概念 "correctability as a prediction target" 与 Error Depth Hypothesis (arXiv:2601.00828) 在概念上高度重叠（浅错误=可修正，深错误=不可修正）；arXiv:2604.22271 已经从内部 confidence 信号角度研究了 LLM 的错误检测和修正预测；arXiv:2602.09924 已经展示了 probe-guided routing 框架。本 proposal 的方法论组件——multi-layer ensemble probe、SAE feature decomposition、representational geometry analysis——全部来自 2025-2026 年的独立论文（分别是 arXiv:2604.13386、arXiv:2604.19974、arXiv:2602.08159），组合应用到一个新目标上。这更接近于"工程集成"而非"科学发现"。剔除 surface differences 后，novelty delta 有限：将预测目标从 correctness 切换为 correctability，但 correctability 这个概念本身已被相关工作以不同名称（error depth, correction success prediction）实质性地探索。

2. **Significance: 中** — 
   研究问题本身重要：LLM self-correction 的 overcorrection 问题是真实的 pain point（多篇 survey 和 benchmark 论文确认），selective correction 有实际应用价值。但本 proposal 的预期影响受限于：(a) 如果 correctability 不可靠预测（前提假设未验证），贡献退化为一个"negative result + representational geometry analysis"，这虽然 publishable 但影响有限；(b) 即使 positive，主要是一个工程改进（从 confidence-based routing 到 probe-based routing 的 incremental gain），不太可能改变领域的研究范式。如果核心实验结果 positive，审稿人的反应更可能是 "reasonable extension, I would have guessed this could work" 而非 "surprising"。

3. **Related Work: 强** — 
   Proposal 对近期相关工作的覆盖非常全面：明确引用了 Error Depth Hypothesis (arXiv:2601.00828)、multi-layer ensemble probing (arXiv:2604.13386)、SAE feature dissociation (arXiv:2604.19974)、Confidence Manifold (arXiv:2602.08159)、Wait-token mechanisms (arXiv:2510.04128)、CoRefine (arXiv:2602.08948)。与 CoRefine 的差异化定位清晰（signal source, abstention capability, correctability specificity）。唯一的遗漏是 arXiv:2604.22271（2026.04），这篇直接研究 internal confidence signals 对 error detection and correction 的预测作用，是最直接的竞争者，proposal 未引用。此外 arXiv:2602.09924 也未被引用但在方法论上高度相关。


【概率估计】: [12% - 22%] 中位 17%

【估计理由】: 
Novelty 维度是主要瓶颈。核心贡献——correctability 作为独立预测目标——在概念上已被 Error Depth Hypothesis 和 internal confidence signals 工作实质性地触及；方法论上是对 5-6 篇近期论文技术组件的组合应用，缺乏独立的方法论创新。Significance 受限于"条件性贡献"结构：只有当多个未验证的前提假设同时成立时才能产生有意义的 positive result。Related Work 的良好覆盖提供了一定的下限保护，但不足以弥补 novelty 的不足。

此外需要严重注意：**本 proposal 投稿 CoRL（Conference on Robot Learning）存在根本性的 venue mismatch——proposal 内容完全是 NLP interpretability / self-correction，不包含任何 robotics 相关内容**。如果确实投 CoRL，中稿概率接近 0%。上述 12-22% 的估计是假设投稿到 ACL/EMNLP/NeurIPS 等适配 venue 的情况。

【主要风险】:
1. **核心 novelty 不足**: "Correctability as a prediction target" 与 Error Depth Hypothesis (arXiv:2601.00828) 和 Internal Confidence Signals (arXiv:2604.22271) 在概念上重叠过多，审稿人可能认为这只是已有工作的 rebranding + 工程组合，而非独立的科学贡献。

2. **核心前提假设脆弱**: Correctability 作为模型内部表征中一个可检测的独立属性，这一假设缺乏理论支撑，且已有证据（68% pure incorrectness features 是 causally inert）暗示二阶属性的信号可能更弱。如果 probe AUROC 无法显著超过 0.614 baseline，proposal 的退路（representational geometry analysis）虽然 publishable，但价值和 novelty 都很有限。
```

---

Sources:
- [How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals](https://arxiv.org/html/2604.22271v1)
- [Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis](https://arxiv.org/abs/2601.00828)
- [LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations](https://arxiv.org/abs/2602.09924)
- [Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling](https://arxiv.org/abs/2604.13386)
- [Are LLM Uncertainty and Correctness Encoded by the Same Features?](https://arxiv.org/abs/2604.19974)
- [The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models](https://arxiv.org/html/2602.08159v1)
- [Internal states before wait modulate reasoning patterns](https://arxiv.org/abs/2510.04128)
- [CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute](https://arxiv.org/abs/2602.08948)
- [When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/)
- [Can Linear Probes Measure LLM Uncertainty?](https://arxiv.org/html/2510.04108)
- [Confidence Before Answering: A Paradigm Shift for Efficient LLM Uncertainty Estimation](https://arxiv.org/html/2603.05881v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1212eca0-fb43-4632-aa72-138bd36d285c",
  "isSidechain": false,
  "requestId": "req_011CbD73Gyy4J2pHDcTbd4hP",
  "type": "assistant",
  "uuid": "33f4b9c3-a763-4bf9-a3b2-22b4e3793744",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RUcmNQPinSTt24NtVu6R31",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1638,
      "cache_read_input_tokens": 26643,
      "output_tokens": 7458,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1638,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7458,
          "cache_read_input_tokens": 26643,
          "cache_creation_input_tokens": 1638,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1638
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

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "33f4b9c3-a763-4bf9-a3b2-22b4e3793744",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM correctability prediction proposal",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "33f4b9c3-a763-4bf9-a3b2-22b4e3793744",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94"
}
```

---

### Runtime record

_source line 58_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM correctability prediction proposal",
  "sessionId": "d00bcc48-da96-4dd3-97ae-3a28bcad8e94"
}
```

---
