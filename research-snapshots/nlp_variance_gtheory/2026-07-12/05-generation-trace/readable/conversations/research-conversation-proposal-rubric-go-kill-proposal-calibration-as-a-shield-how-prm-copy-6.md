# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Calibration as a Shield: How PRM 

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/2dce26a4-3106-4876-9f44-6d43353ccdf0.jsonl`
- **Structured JSON:** [`a2973c247cfcf62ece0b.json`](../../sessions/a2/a2973c247cfcf62ece0b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:13:32.159Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:13:32.159Z",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-Level Defense\n\n## Description\nWe present the first causally rigorous study connecting PRM calibration quality to adversarial exploitability, and propose Calibration-Gated Step-Level Pessimism (CGSP), a novel defense that transforms calibrated uncertainty into adaptive reward hacking resistance during RL training. Our work bridges two mature but isolated research threads (PRM calibration and PRM hackability) through four contributions. First, an expanded correlation study across 48 configurations (8 PRMs × 6 calibration methods) provides sufficient statistical power (n=48, detecting r≥0.29 at p<0.05) to establish whether calibration quality predicts hackability metrics under gradient attacks, RL-induced hacking (GRPO on AIME), and BoN overoptimization (MATH-500), stratified by problem difficulty. Second, causal isolation experiments separate calibration's true effect from representation change artifacts: we compare post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) that provably preserve model representations against fine-tuning-based methods, with CKA verification and matched-representation-change controls. Third, step-level Hessian spectral analysis goes beyond Ackermann et al.'s outcome-level gradient norm analysis (which applies only to single-scalar reward models) to reveal how calibration affects the multi-reward compositional geometry of PRMs — analyzing how step-level flatness compounds across trajectories. Fourth, CGSP replaces raw PRM rewards during RL training with r̃_t = μ_t − α·σ_t/√c_t, where calibrated uncertainty σ_t and calibration quality c_t adaptively modulate pessimism per-step — trusted when calibration is tight, pessimistic when uncertainty is high — with a Calibration Drift Detector that monitors ECE on current-policy rollouts to flag distribution-shift-induced reward hacking in real time. CGSP differs from existing defenses (Caution uses prediction error, PET uses global pessimism, ensemble methods are uncalibrated) by being step-level, calibration-grounded, and adaptive. We evaluate CGSP against 5 baselines (uncalibrated GRPO, APRM, Caution, ensemble-min, gradient regularization) on MATH-500 and AIME, measuring both reward-accuracy alignment and downstream task accuracy.\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T03:13:32.163Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:13:32.163Z",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0"
}
```

---

## Round 1

40 recorded events

### User

_source line 3 · 2026-05-20T03:13:32.174Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-Level Defense

## Description
We present the first causally rigorous study connecting PRM calibration quality to adversarial exploitability, and propose Calibration-Gated Step-Level Pessimism (CGSP), a novel defense that transforms calibrated uncertainty into adaptive reward hacking resistance during RL training. Our work bridges two mature but isolated research threads (PRM calibration and PRM hackability) through four contributions. First, an expanded correlation study across 48 configurations (8 PRMs × 6 calibration methods) provides sufficient statistical power (n=48, detecting r≥0.29 at p<0.05) to establish whether calibration quality predicts hackability metrics under gradient attacks, RL-induced hacking (GRPO on AIME), and BoN overoptimization (MATH-500), stratified by problem difficulty. Second, causal isolation experiments separate calibration's true effect from representation change artifacts: we compare post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) that provably preserve model representations against fine-tuning-based methods, with CKA verification and matched-representation-change controls. Third, step-level Hessian spectral analysis goes beyond Ackermann et al.'s outcome-level gradient norm analysis (which applies only to single-scalar reward models) to reveal how calibration affects the multi-reward compositional geometry of PRMs — analyzing how step-level flatness compounds across trajectories. Fourth, CGSP replaces raw PRM rewards during RL training with r̃_t = μ_t − α·σ_t/√c_t, where calibrated uncertainty σ_t and calibration quality c_t adaptively modulate pessimism per-step — trusted when calibration is tight, pessimistic when uncertainty is high — with a Calibration Drift Detector that monitors ECE on current-policy rollouts to flag distribution-shift-induced reward hacking in real time. CGSP differs from existing defenses (Caution uses prediction error, PET uses global pessimism, ensemble methods are uncalibrated) by being step-level, calibration-grounded, and adaptive. We evaluate CGSP against 5 baselines (uncalibrated GRPO, APRM, Caution, ensemble-min, gradient regularization) on MATH-500 and AIME, measuring both reward-accuracy alignment and downstream task accuracy.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "5e77306a-0e66-4a40-a025-b25b4b1efd70",
  "type": "user",
  "uuid": "abf035ff-0db2-492d-a9e2-73273b5dbb2a",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:13:32.173Z_

```json
{
  "parentUuid": "abf035ff-0db2-492d-a9e2-73273b5dbb2a",
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
  "uuid": "b406fc45-b869-4959-adf3-6e8faeb93a63",
  "timestamp": "2026-05-20T03:13:32.173Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:13:32.173Z_

```json
{
  "parentUuid": "b406fc45-b869-4959-adf3-6e8faeb93a63",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "43266c5c-cbef-471f-826d-3520a31933fb",
  "timestamp": "2026-05-20T03:13:32.173Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
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
  "aiTitle": "Evaluate PRM calibration and reward hacking resistance proposal",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0"
}
```

---

### Assistant

_source line 7 · 2026-05-20T03:13:45.267Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for CoRL 2026. Let me first carefully read the proposal, then conduct web searches to understand the current landscape before providing my assessment.

Wait - the user says CoRL 2026, but the proposal is about PRM calibration, reward hacking, RL training for math reasoning. This is more of an ML/NLP topic, not robotics. CoRL is Conference on Robot Learning. Let me re-read...

Actually, looking at the system prompt again, it says "CoRL 2026 主会" but the proposal is about PRMs (Process Reward Models), reward hacking, GRPO, MATH-500, AIME - these are clearly NLP/ML topics related to LLM reasoning. 

The venue might be misaligned with the content, but that's secondary to evaluating the actual research quality. I should focus on assessing the idea itself rather than getting caught up in the venue question. Before diving into my evaluation, I need to search for context on the key technical areas: PRM calibration and how reward hacking affects it, recent defenses against exploitability in process reward models, and what's already known about calibration-gated pessimism approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43266c5c-cbef-471f-826d-3520a31933fb",
  "isSidechain": false,
  "requestId": "req_011CbD6FREmy51Xn6qGzJ37V",
  "type": "assistant",
  "uuid": "2aeed932-61fa-4cd1-82ec-034c1f25eb4f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BJVMPJ5HAc3jKVBTqgv5SS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 2003,
      "cache_read_input_tokens": 13985,
      "output_tokens": 444,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2003,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 444,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 2003,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2003
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

_source line 8 · 2026-05-20T03:13:45.322Z_

I need to do thorough literature research before evaluating this proposal. Let me search for the key topics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2aeed932-61fa-4cd1-82ec-034c1f25eb4f",
  "isSidechain": false,
  "requestId": "req_011CbD6FREmy51Xn6qGzJ37V",
  "type": "assistant",
  "uuid": "d0bb4f22-2192-4018-b11f-863c9f97220c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BJVMPJ5HAc3jKVBTqgv5SS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 2003,
      "cache_read_input_tokens": 13985,
      "output_tokens": 444,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2003,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 444,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 2003,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2003
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

_source line 9 · 2026-05-20T03:13:45.368Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LccdxYd26vSuCLgqXJKNea`</summary>

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
  "parentUuid": "d0bb4f22-2192-4018-b11f-863c9f97220c",
  "isSidechain": false,
  "requestId": "req_011CbD6FREmy51Xn6qGzJ37V",
  "type": "assistant",
  "uuid": "848294f5-29bd-4af6-b118-a16fd0441f63",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BJVMPJ5HAc3jKVBTqgv5SS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 2003,
      "cache_read_input_tokens": 13985,
      "output_tokens": 444,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2003,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 444,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 2003,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2003
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

_source line 10 · 2026-05-20T03:13:45.375Z_

<details><summary>↩ Tool result · `toolu_01LccdxYd26vSuCLgqXJKNea`</summary>

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
  "parentUuid": "848294f5-29bd-4af6-b118-a16fd0441f63",
  "isSidechain": false,
  "promptId": "5e77306a-0e66-4a40-a025-b25b4b1efd70",
  "type": "user",
  "uuid": "57fc0c5e-72b6-4fc2-a9ad-0e19bbadffeb",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "848294f5-29bd-4af6-b118-a16fd0441f63",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-20T03:13:48.597Z_

Now let me conduct the required literature searches. I'll run multiple searches in parallel to cover the key aspects of this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57fc0c5e-72b6-4fc2-a9ad-0e19bbadffeb",
  "isSidechain": false,
  "requestId": "req_011CbD6GPoVLLmapZ7Q42TDa",
  "type": "assistant",
  "uuid": "e17ad529-58f0-48d5-8e73-a1d5a2a27111",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CBLtq18ufnWVEaXnGZe3o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 970,
      "cache_read_input_tokens": 15988,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 970,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 94,
          "cache_read_input_tokens": 15988,
          "cache_creation_input_tokens": 970,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 970
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

_source line 12 · 2026-05-20T03:13:48.604Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SNAY4h8WTQoVi2DsZtKsQt`</summary>

```json
{
  "query": "PRM process reward model calibration reward hacking 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e17ad529-58f0-48d5-8e73-a1d5a2a27111",
  "isSidechain": false,
  "requestId": "req_011CbD6GPoVLLmapZ7Q42TDa",
  "type": "assistant",
  "uuid": "8853abf7-7925-4923-8e85-7b55f4618a50",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CBLtq18ufnWVEaXnGZe3o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 970,
      "cache_read_input_tokens": 15988,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 970,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 94,
          "cache_read_input_tokens": 15988,
          "cache_creation_input_tokens": 970,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 970
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

_source line 13 · 2026-05-20T03:14:01.609Z_

<details><summary>↩ Tool result · `toolu_01SNAY4h8WTQoVi2DsZtKsQt`</summary>

```text
Web search results for query: "PRM process reward model calibration reward hacking 2025 2026"

Links: [{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Process+Reward+Models+(PRMs)"},{"title":"Process-supervised Reward Models (PRMs)","url":"https://www.emergentmind.com/topics/process-supervised-reward-models-prm"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM ...","url":"https://openreview.net/pdf?id=TDfrN1TbGH"},{"title":"Reward Under Attack: Evaluating the Sensitivity of Process Reward Models","url":"https://openreview.net/pdf?id=Hw24VOppus"},{"title":"Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning","url":"https://arxiv.org/pdf/2504.15275"},{"title":"Process Reward Models for LLM Agents: Practical Framework and Directions","url":"https://arxiv.org/html/2502.10325v1"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/pdf/2509.26578"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/pdf/2603.06621"}]

Based on the search results, here's what I found about Process Reward Models (PRMs), calibration, and reward hacking in 2025-2026:

## Key Findings

**PRM Calibration Methods:**
Recent research shows that PRM calibration methods can successfully achieve small calibration error, with calibration being crucial for enabling effective adaptive scaling. A notable approach is PPR, which trains a PRM that grounds step-wise judgments in interpretable principles instead of ad-hoc heuristics, with reward calibrated and unified across sparse outcome and dense process rewards.

**Reward Hacking Challenges:**
Reward hacking issues with PRMs limit their successful application in reinforcement fine-tuning, with the main cause being the canonical summation-form credit assignment in reinforcement learning, which easily induces LLMs to hack steps with high rewards. PRMs are more susceptible to length hacking or verbosity bias due to high variance in step-wise optimization.

**Recent Solutions:**
The PURE approach addresses reward hacking through min-form credit assignment that formulates the value function as the minimum of future rewards, significantly alleviating reward hacking by limiting the value function range and distributing advantages more reasonably.

**Ongoing Challenges (2025-2026):**
Reward hacking, scalability to new domains lacking automatic verification, and balancing local/global signals in dynamic settings remain ongoing challenges. Recent findings show that policies can achieve near-perfect PRM rewards while ground-truth accuracy remains low, revealing that current PRMs function as fluency detectors rather than reasoning verifiers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8853abf7-7925-4923-8e85-7b55f4618a50",
  "isSidechain": false,
  "promptId": "5e77306a-0e66-4a40-a025-b25b4b1efd70",
  "type": "user",
  "uuid": "3746693f-494d-4f5c-b75e-fe3585ac7d52",
  "toolUseResult": {
    "query": "PRM process reward model calibration reward hacking 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016VsgkVb7nHYvcqeNvvDQnj",
        "content": [
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=Process+Reward+Models+(PRMs)"
          },
          {
            "title": "Process-supervised Reward Models (PRMs)",
            "url": "https://www.emergentmind.com/topics/process-supervised-reward-models-prm"
          },
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
            "url": "https://arxiv.org/html/2510.08049v3"
          },
          {
            "title": "Reward Modeling for Reinforcement Learning-Based LLM ...",
            "url": "https://openreview.net/pdf?id=TDfrN1TbGH"
          },
          {
            "title": "Reward Under Attack: Evaluating the Sensitivity of Process Reward Models",
            "url": "https://openreview.net/pdf?id=Hw24VOppus"
          },
          {
            "title": "Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning",
            "url": "https://arxiv.org/pdf/2504.15275"
          },
          {
            "title": "Process Reward Models for LLM Agents: Practical Framework and Directions",
            "url": "https://arxiv.org/html/2502.10325v1"
          },
          {
            "title": "Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2509.26578"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/pdf/2603.06621"
          }
        ]
      },
      "Based on the search results, here's what I found about Process Reward Models (PRMs), calibration, and reward hacking in 2025-2026:\n\n## Key Findings\n\n**PRM Calibration Methods:**\nRecent research shows that PRM calibration methods can successfully achieve small calibration error, with calibration being crucial for enabling effective adaptive scaling. A notable approach is PPR, which trains a PRM that grounds step-wise judgments in interpretable principles instead of ad-hoc heuristics, with reward calibrated and unified across sparse outcome and dense process rewards.\n\n**Reward Hacking Challenges:**\nReward hacking issues with PRMs limit their successful application in reinforcement fine-tuning, with the main cause being the canonical summation-form credit assignment in reinforcement learning, which easily induces LLMs to hack steps with high rewards. PRMs are more susceptible to length hacking or verbosity bias due to high variance in step-wise optimization.\n\n**Recent Solutions:**\nThe PURE approach addresses reward hacking through min-form credit assignment that formulates the value function as the minimum of future rewards, significantly alleviating reward hacking by limiting the value function range and distributing advantages more reasonably.\n\n**Ongoing Challenges (2025-2026):**\nReward hacking, scalability to new domains lacking automatic verification, and balancing local/global signals in dynamic settings remain ongoing challenges. Recent findings show that policies can achieve near-perfect PRM rewards while ground-truth accuracy remains low, revealing that current PRMs function as fluency detectors rather than reasoning verifiers."
    ],
    "durationSeconds": 12.997141201999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8853abf7-7925-4923-8e85-7b55f4618a50",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T03:14:07.425Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UxwTwywWDZG2zZxpXNhDHt`</summary>

```json
{
  "query": "Ackermann et al. reward hacking gradient analysis reward model 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3746693f-494d-4f5c-b75e-fe3585ac7d52",
  "isSidechain": false,
  "requestId": "req_011CbD6Hb5BCbc2PGeF4r4mR",
  "type": "assistant",
  "uuid": "939c304f-d276-4d02-94b7-9f46ebf4db4c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GoY5tJqUhVP4WiSLBV8v4n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 875,
      "cache_read_input_tokens": 16958,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 875,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 16958,
          "cache_creation_input_tokens": 875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 875
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

_source line 15 · 2026-05-20T03:14:12.873Z_

<details><summary>↩ Tool result · `toolu_01UxwTwywWDZG2zZxpXNhDHt`</summary>

```text
Web search results for query: "Ackermann et al. reward hacking gradient analysis reward model 2025"

Links: [{"title":"Detecting and Suppressing Reward Hacking with Gradient Fingerprints","url":"https://arxiv.org/html/2604.16242"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/html/2604.02986"},{"title":"[2602.18037] Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards","url":"https://arxiv.org/abs/2602.18037"},{"title":"Natural Emergent Misalignment from Reward Hacking in Production RL","url":"https://arxiv.org/pdf/2511.18397"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/pdf/2604.02986"},{"title":"2025-Era “Reward Hacking” Does Not Show that ...","url":"https://www.alignmentforum.org/posts/wwRgR3K8FKShjwwL5/2025-era-reward-hacking-does-not-show-that-reward-is-the"},{"title":"Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards","url":"https://arxiv.org/pdf/2602.18037"}]

Based on the search results, I found relevant information about Ackermann et al.'s work on reward hacking and gradient analysis:

Ackermann et al. published "Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards". The authors argue that reward hacking often corresponds to sharp optima of the proxy reward and propose gradient regularization (GR) as a solution.

The work derives a theoretical connection between the accuracy of a reward model and the flatness of an optimum at convergence. Gradient regularization can be used to bias training to flatter regions and thereby maintain reward model accuracy, with empirical evidence showing that the gradient norm and reward accuracy are correlated in RLHF.

The paper was published in February 2026 and proposes a different approach from traditional methods—rather than limiting policy updates with KL penalties, the authors propose training language models in a way that biases policy updates towards regions in which the reward is more accurate.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "939c304f-d276-4d02-94b7-9f46ebf4db4c",
  "isSidechain": false,
  "promptId": "5e77306a-0e66-4a40-a025-b25b4b1efd70",
  "type": "user",
  "uuid": "cbe93b5c-6c8e-4298-933f-ca98a2ef51f5",
  "toolUseResult": {
    "query": "Ackermann et al. reward hacking gradient analysis reward model 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Xy4uy2FyG5idBFDqwgdGGd",
        "content": [
          {
            "title": "Detecting and Suppressing Reward Hacking with Gradient Fingerprints",
            "url": "https://arxiv.org/html/2604.16242"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/html/2604.02986"
          },
          {
            "title": "[2602.18037] Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards",
            "url": "https://arxiv.org/abs/2602.18037"
          },
          {
            "title": "Natural Emergent Misalignment from Reward Hacking in Production RL",
            "url": "https://arxiv.org/pdf/2511.18397"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/pdf/2604.02986"
          },
          {
            "title": "2025-Era “Reward Hacking” Does Not Show that ...",
            "url": "https://www.alignmentforum.org/posts/wwRgR3K8FKShjwwL5/2025-era-reward-hacking-does-not-show-that-reward-is-the"
          },
          {
            "title": "Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards",
            "url": "https://arxiv.org/pdf/2602.18037"
          }
        ]
      },
      "Based on the search results, I found relevant information about Ackermann et al.'s work on reward hacking and gradient analysis:\n\nAckermann et al. published \"Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards\". The authors argue that reward hacking often corresponds to sharp optima of the proxy reward and propose gradient regularization (GR) as a solution.\n\nThe work derives a theoretical connection between the accuracy of a reward model and the flatness of an optimum at convergence. Gradient regularization can be used to bias training to flatter regions and thereby maintain reward model accuracy, with empirical evidence showing that the gradient norm and reward accuracy are correlated in RLHF.\n\nThe paper was published in February 2026 and proposes a different approach from traditional methods—rather than limiting policy updates with KL penalties, the authors propose training language models in a way that biases policy updates towards regions in which the reward is more accurate."
    ],
    "durationSeconds": 5.444062193999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "939c304f-d276-4d02-94b7-9f46ebf4db4c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-L…",
  "leafUuid": "cbe93b5c-6c8e-4298-933f-ca98a2ef51f5",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM calibration and reward hacking resistance proposal",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0"
}
```

---

### Tool call

_source line 18 · 2026-05-20T03:14:15.959Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PNkHz23hyNUBqbqd3b7sJz`</summary>

```json
{
  "query": "\"calibration-gated\" OR \"step-level pessimism\" OR \"CGSP\" reward model defense 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbe93b5c-6c8e-4298-933f-ca98a2ef51f5",
  "isSidechain": false,
  "requestId": "req_011CbD6JR7fh3ZhVD1D5uDF7",
  "type": "assistant",
  "uuid": "0f196324-fe13-46c7-ad01-593c81a92480",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0183eh3eSCNhv1J9hdyeDEFa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 696,
      "cache_read_input_tokens": 17833,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 696,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 17833,
          "cache_creation_input_tokens": 696,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 696
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

_source line 19 · 2026-05-20T03:14:32.694Z_

<details><summary>↩ Tool result · `toolu_01PNkHz23hyNUBqbqd3b7sJz`</summary>

```text
Web search results for query: ""calibration-gated" OR "step-level pessimism" OR "CGSP" reward model defense 2025 2026"

Links: [{"title":"Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/pdf/2505.20556"},{"title":"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism","url":"https://arxiv.org/pdf/2604.04648"},{"title":"GitHub - JLZhong23/awesome-reward-models · GitHub","url":"https://github.com/JLZhong23/awesome-reward-models"},{"title":"Rewarding Doubt: A Reinforcement Learning Approach to Calibrated Confidence Expression of Large Language Models","url":"https://arxiv.org/pdf/2503.02623"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/pdf/2603.06621"}]

The search returned results related to reward model robustness and pessimism, but didn't find specific results for the exact terms "calibration-gated," "step-level pessimism," or "CGSP." Let me try a more targeted search:

Links: [{"title":"Minimising statistical errors in calibration of quantum-gate sets","url":"https://arxiv.org/pdf/2206.03417"},{"title":"C$^2$GSPG: Confidence-calibrated Group Sequence Policy Gradient towards Self-aware Reasoning","url":"https://arxiv.org/pdf/2509.23129"},{"title":"Reducing x-pessimism in gate-level simulation and verification","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8650513"},{"title":"Dimensionality reduction for closed-loop quantum gate calibration","url":"https://arxiv.org/pdf/2412.05230"},{"title":"Self-Consistent Calibration of Quantum Gate Sets","url":"https://arxiv.org/pdf/1906.00950"}]

The results are returning content about quantum gates rather than reward models. Let me search more specifically for these terms in the context of reward model defenses:

Links: [{"title":"Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/html/2505.20556"},{"title":"Pessimistic Reward Tuning (PET) in RLHF","url":"https://www.emergentmind.com/topics/pessimistic-reward-tuning-pet"},{"title":"GitHub - JLZhong23/awesome-reward-models · GitHub","url":"https://github.com/JLZhong23/awesome-reward-models"},{"title":"Process Reward Models: Step-Level Feedback for LLMs","url":"https://www.emergentmind.com/topics/process-reward-models-prm"},{"title":"Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/pdf/2505.20556"},{"title":"[2412.15904] What Are Step-Level Reward Models Rewarding? Counterintuitive Findings from MCTS-Boosted Mathematical Reasoning","url":"https://arxiv.org/abs/2412.15904"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism","url":"https://arxiv.org/pdf/2604.04648"}]

Let me search more specifically for "calibration-gated":

Links: [{"title":"CHARM: Calibrating Reward Models With Chatbot Arena Scores","url":"https://arxiv.org/pdf/2504.10045"},{"title":"CHARM: Calibrating Reward Models With Chatbot Arena Scores","url":"https://arxiv.org/html/2504.10045v1"},{"title":"Delayed Rewards Calibration via Reward Empirical Sufficiency","url":"https://arxiv.org/pdf/2102.10527"},{"title":"Taming Overconfidence in LLMs: Reward Calibration in RLHF | OpenReview","url":"https://openreview.net/forum?id=l0tg0jzsdL"},{"title":"GitHub - SeanLeng1/Reward-Calibration · GitHub","url":"https://github.com/SeanLeng1/Reward-Calibration"},{"title":"[2410.09724] Taming Overconfidence in LLMs: Reward Calibration in RLHF","url":"https://arxiv.org/abs/2410.09724"},{"title":"Reward Models Lie When They Sound Certain | by Bhagya Rana | Medium","url":"https://medium.com/@bhagyarana80/reward-models-lie-when-they-sound-certain-dcff69de1a34"}]

Based on my web searches, I was unable to find specific papers or resources that use the exact terminology "calibration-gated," "step-level pessimism," or the acronym "CGSP" as a unified reward model defense approach. 

The search results returned several related concepts in the 2025-2026 timeframe:

1. **Pessimistic Reward Models**: The idea of 'pessimism' is necessary for the learning agent to avoid reward hacking, where the agent must be pessimistic when evaluating the policy's performance based on the dataset.

2. **Calibration-based Approaches**: PPO-M integrates explicit confidence scores in reward model training, which calibrates reward models to better capture the alignment between response quality and verbalized confidence.

3. **Step-Level Rewards**: Process Reward Models (PRMs) provide a reward signal for each intermediate step, and the step-level nature of PRMs allows the discovery and correction of localized errors.

4. **Pessimism at Reward Level**: A pessimistic approach penalizes out-of-distribution responses by subtracting per-response uncertainty estimates from the scores assigned by reward models, and then selects the response with the highest pessimistic score.

However, I could not locate a specific paper or research work that combines these concepts under the name "CGSP" (Calibration-Gated Step-Level Pessimism) or uses that exact terminology. If you have a specific paper or preprint in mind, please provide additional details or a direct link, and I can help you find more information about it.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f196324-fe13-46c7-ad01-593c81a92480",
  "isSidechain": false,
  "promptId": "5e77306a-0e66-4a40-a025-b25b4b1efd70",
  "type": "user",
  "uuid": "db95f195-4726-4084-a0c0-2a6dc5788d55",
  "toolUseResult": {
    "query": "\"calibration-gated\" OR \"step-level pessimism\" OR \"CGSP\" reward model defense 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XnAt7py2PEEpZ8gsWfF1de",
        "content": [
          {
            "title": "Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/pdf/2505.20556"
          },
          {
            "title": "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism",
            "url": "https://arxiv.org/pdf/2604.04648"
          },
          {
            "title": "GitHub - JLZhong23/awesome-reward-models · GitHub",
            "url": "https://github.com/JLZhong23/awesome-reward-models"
          },
          {
            "title": "Rewarding Doubt: A Reinforcement Learning Approach to Calibrated Confidence Expression of Large Language Models",
            "url": "https://arxiv.org/pdf/2503.02623"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/pdf/2603.06621"
          }
        ]
      },
      "The search returned results related to reward model robustness and pessimism, but didn't find specific results for the exact terms \"calibration-gated,\" \"step-level pessimism,\" or \"CGSP.\" Let me try a more targeted search:",
      {
        "tool_use_id": "srvtoolu_01AjLLniQdtABwYgriTF7ypG",
        "content": [
          {
            "title": "Minimising statistical errors in calibration of quantum-gate sets",
            "url": "https://arxiv.org/pdf/2206.03417"
          },
          {
            "title": "C$^2$GSPG: Confidence-calibrated Group Sequence Policy Gradient towards Self-aware Reasoning",
            "url": "https://arxiv.org/pdf/2509.23129"
          },
          {
            "title": "Reducing x-pessimism in gate-level simulation and verification",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8650513"
          },
          {
            "title": "Dimensionality reduction for closed-loop quantum gate calibration",
            "url": "https://arxiv.org/pdf/2412.05230"
          },
          {
            "title": "Self-Consistent Calibration of Quantum Gate Sets",
            "url": "https://arxiv.org/pdf/1906.00950"
          }
        ]
      },
      "The results are returning content about quantum gates rather than reward models. Let me search more specifically for these terms in the context of reward model defenses:",
      {
        "tool_use_id": "srvtoolu_017Wa4ihv2FQwkBpyNYhyXZV",
        "content": [
          {
            "title": "Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/html/2505.20556"
          },
          {
            "title": "Pessimistic Reward Tuning (PET) in RLHF",
            "url": "https://www.emergentmind.com/topics/pessimistic-reward-tuning-pet"
          },
          {
            "title": "GitHub - JLZhong23/awesome-reward-models · GitHub",
            "url": "https://github.com/JLZhong23/awesome-reward-models"
          },
          {
            "title": "Process Reward Models: Step-Level Feedback for LLMs",
            "url": "https://www.emergentmind.com/topics/process-reward-models-prm"
          },
          {
            "title": "Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/pdf/2505.20556"
          },
          {
            "title": "[2412.15904] What Are Step-Level Reward Models Rewarding? Counterintuitive Findings from MCTS-Boosted Mathematical Reasoning",
            "url": "https://arxiv.org/abs/2412.15904"
          },
          {
            "title": "GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub",
            "url": "https://github.com/RyanLiu112/Awesome-Process-Reward-Models"
          },
          {
            "title": "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism",
            "url": "https://arxiv.org/pdf/2604.04648"
          }
        ]
      },
      "Let me search more specifically for \"calibration-gated\":",
      {
        "tool_use_id": "srvtoolu_01Py8mqoWPKHs9DuP4qLsttw",
        "content": [
          {
            "title": "CHARM: Calibrating Reward Models With Chatbot Arena Scores",
            "url": "https://arxiv.org/pdf/2504.10045"
          },
          {
            "title": "CHARM: Calibrating Reward Models With Chatbot Arena Scores",
            "url": "https://arxiv.org/html/2504.10045v1"
          },
          {
            "title": "Delayed Rewards Calibration via Reward Empirical Sufficiency",
            "url": "https://arxiv.org/pdf/2102.10527"
          },
          {
            "title": "Taming Overconfidence in LLMs: Reward Calibration in RLHF | OpenReview",
            "url": "https://openreview.net/forum?id=l0tg0jzsdL"
          },
          {
            "title": "GitHub - SeanLeng1/Reward-Calibration · GitHub",
            "url": "https://github.com/SeanLeng1/Reward-Calibration"
          },
          {
            "title": "[2410.09724] Taming Overconfidence in LLMs: Reward Calibration in RLHF",
            "url": "https://arxiv.org/abs/2410.09724"
          },
          {
            "title": "Reward Models Lie When They Sound Certain | by Bhagya Rana | Medium",
            "url": "https://medium.com/@bhagyarana80/reward-models-lie-when-they-sound-certain-dcff69de1a34"
          }
        ]
      },
      "Based on my web searches, I was unable to find specific papers or resources that use the exact terminology \"calibration-gated,\" \"step-level pessimism,\" or the acronym \"CGSP\" as a unified reward model defense approach. \n\nThe search results returned several related concepts in the 2025-2026 timeframe:\n\n1. **Pessimistic Reward Models**: The idea of 'pessimism' is necessary for the learning agent to avoid reward hacking, where the agent must be pessimistic when evaluating the policy's performance based on the dataset.\n\n2. **Calibration-based Approaches**: PPO-M integrates explicit confidence scores in reward model training, which calibrates reward models to better capture the alignment between response quality and verbalized confidence.\n\n3. **Step-Level Rewards**: Process Reward Models (PRMs) provide a reward signal for each intermediate step, and the step-level nature of PRMs allows the discovery and correction of localized errors.\n\n4. **Pessimism at Reward Level**: A pessimistic approach penalizes out-of-distribution responses by subtracting per-response uncertainty estimates from the scores assigned by reward models, and then selects the response with the highest pessimistic score.\n\nHowever, I could not locate a specific paper or research work that combines these concepts under the name \"CGSP\" (Calibration-Gated Step-Level Pessimism) or uses that exact terminology. If you have a specific paper or preprint in mind, please provide additional details or a direct link, and I can help you find more information about it."
    ],
    "durationSeconds": 16.731579489000005,
    "searchCount": 4
  },
  "sourceToolAssistantUUID": "0f196324-fe13-46c7-ad01-593c81a92480",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T03:14:35.128Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XhocutRuvBipVGZMsUFYEh`</summary>

```json
{
  "query": "Caution reward hacking defense pessimism Best-of-N 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db95f195-4726-4084-a0c0-2a6dc5788d55",
  "isSidechain": false,
  "requestId": "req_011CbD6KssXMCjn4k4vGJcXM",
  "type": "assistant",
  "uuid": "120859d8-067d-47d9-8bfd-4bf8594d0273",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016wXDNNTodKdTvr8CwZRFEU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1727,
      "cache_read_input_tokens": 18529,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 18529,
          "cache_creation_input_tokens": 1727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1727
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

_source line 21 · 2026-05-20T03:14:41.997Z_

<details><summary>↩ Tool result · `toolu_01XhocutRuvBipVGZMsUFYEh`</summary>

```text
Web search results for query: "Caution reward hacking defense pessimism Best-of-N 2025 2026 arxiv"

Links: [{"title":"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-𝑁 with Pessimism","url":"https://arxiv.org/html/2604.04648"},{"title":"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism","url":"https://arxiv.org/pdf/2604.04648"},{"title":"[2604.04648] From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism","url":"https://arxiv.org/abs/2604.04648"},{"title":"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-$N$ with Pessimism | OpenReview","url":"https://openreview.net/forum?id=EZn2TmBBfF"},{"title":"Avoiding Reward Hacking","url":"https://www.emergentmind.com/topics/avoiding-reward-hacking"},{"title":"Inference-Time Reward Hacking in Large Language Models","url":"https://arxiv.org/html/2506.19248v2"},{"title":"[2506.19248] Inference-Time Reward Hacking in Large Language Models","url":"https://arxiv.org/abs/2506.19248"}]

I found relevant research on your query. Here's what the search returned:

## Main Result

The paper "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism" addresses how to use additional inference-time compute to improve language model performance. 

The key problem is that Best-of-N sampling is vulnerable to reward hacking, where performance degrades as N increases due to the selection of responses that exploit imperfections in the reward model instead of genuinely improving generation quality.

## The Solution

The paper shows that caution is computationally efficient and effectively mitigates reward hacking in BoN sampling, and provides theoretical analysis in a simplified linear setting proving that caution strictly improves over standard BoN.

These results demonstrate that caution is both a powerful practical solution to reward hacking and compelling evidence for the broader efficacy of curiosity-style uncertainty signals in out-of-distribution detection and pessimistic policy learning for language models.

The paper was published on April 6, 2026 (arxiv 2604.04648) and represents recent work on this important problem in language model inference optimization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "120859d8-067d-47d9-8bfd-4bf8594d0273",
  "isSidechain": false,
  "promptId": "5e77306a-0e66-4a40-a025-b25b4b1efd70",
  "type": "user",
  "uuid": "1aa6a38c-1139-450b-af0e-8a92849ca491",
  "toolUseResult": {
    "query": "Caution reward hacking defense pessimism Best-of-N 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_017Xjq4AU8XT1zw3fvNEJ5R1",
        "content": [
          {
            "title": "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-𝑁 with Pessimism",
            "url": "https://arxiv.org/html/2604.04648"
          },
          {
            "title": "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism",
            "url": "https://arxiv.org/pdf/2604.04648"
          },
          {
            "title": "[2604.04648] From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism",
            "url": "https://arxiv.org/abs/2604.04648"
          },
          {
            "title": "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-$N$ with Pessimism | OpenReview",
            "url": "https://openreview.net/forum?id=EZn2TmBBfF"
          },
          {
            "title": "Avoiding Reward Hacking",
            "url": "https://www.emergentmind.com/topics/avoiding-reward-hacking"
          },
          {
            "title": "Inference-Time Reward Hacking in Large Language Models",
            "url": "https://arxiv.org/html/2506.19248v2"
          },
          {
            "title": "[2506.19248] Inference-Time Reward Hacking in Large Language Models",
            "url": "https://arxiv.org/abs/2506.19248"
          }
        ]
      },
      "I found relevant research on your query. Here's what the search returned:\n\n## Main Result\n\nThe paper \"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism\" addresses how to use additional inference-time compute to improve language model performance. \n\nThe key problem is that Best-of-N sampling is vulnerable to reward hacking, where performance degrades as N increases due to the selection of responses that exploit imperfections in the reward model instead of genuinely improving generation quality.\n\n## The Solution\n\nThe paper shows that caution is computationally efficient and effectively mitigates reward hacking in BoN sampling, and provides theoretical analysis in a simplified linear setting proving that caution strictly improves over standard BoN.\n\nThese results demonstrate that caution is both a powerful practical solution to reward hacking and compelling evidence for the broader efficacy of curiosity-style uncertainty signals in out-of-distribution detection and pessimistic policy learning for language models.\n\nThe paper was published on April 6, 2026 (arxiv 2604.04648) and represents recent work on this important problem in language model inference optimization."
    ],
    "durationSeconds": 6.864107937000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "120859d8-067d-47d9-8bfd-4bf8594d0273",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T03:14:43.976Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XXaiPcE4kN5jMFmFpwerf1`</summary>

```json
{
  "query": "\"reward under attack\" process reward model hackability robustness 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1aa6a38c-1139-450b-af0e-8a92849ca491",
  "isSidechain": false,
  "requestId": "req_011CbD6LZeRytVhjZRATH8mU",
  "type": "assistant",
  "uuid": "90f787d5-bc83-406c-8f30-b7b53871ae8c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015pV25tcR6puc48TaCs6mYu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 738,
      "cache_read_input_tokens": 20256,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 738,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 20256,
          "cache_creation_input_tokens": 738,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 738
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

_source line 23 · 2026-05-20T03:14:51.003Z_

<details><summary>↩ Tool result · `toolu_01XXaiPcE4kN5jMFmFpwerf1`</summary>

```text
Web search results for query: ""reward under attack" process reward model hackability robustness 2026"

Links: [{"title":"[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/abs/2603.06621"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of","url":"https://arxiv.org/pdf/2603.06621"},{"title":"GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub","url":"https://github.com/xhwang22/Awesome-Reward-Hacking"},{"title":"[2602.10623v1] Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/abs/2602.10623v1"},{"title":"[2602.10623] Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/abs/2602.10623"},{"title":"1 Introduction","url":"https://arxiv.org/html/2603.06621"},{"title":"Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/pdf/2502.18770"},{"title":"Robust Reward Modeling via Causal Rubrics","url":"https://arxiv.org/pdf/2506.16507"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/pdf/2604.02986"},{"title":"Adversarial Training of Reward Models","url":"https://arxiv.org/pdf/2504.06141"}]

I found relevant research on this topic. Here are the key findings:

## "Reward Under Attack" Paper

Process Reward Models (PRMs) are rapidly becoming the backbone of LLM reasoning pipelines, yet state-of-the-art PRMs are systematically exploitable under adversarial optimization pressure.

### Key Findings

When policies were trained on AIME problems, they achieved near-perfect PRM rewards (>0.9), while ground-truth accuracy remained low (below 4%), with 43% of reward gains attributable to stylistic shortcuts. This reveals a critical vulnerability in how PRMs evaluate reasoning.

Current PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.

### Methodology and Resources

The researchers introduced a three-tiered diagnostic framework that applies increasing adversarial pressure to quantify vulnerabilities. They released PRM-BiasBench and a diagnostic toolkit to enable robustness evaluation before deployment.

The paper was published on arXiv on February 20, 2026, by researchers from UC Berkeley, Transmute AI, ICSI, and LBNL, addressing fundamental concerns about the reliability of process reward models in LLM alignment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90f787d5-bc83-406c-8f30-b7b53871ae8c",
  "isSidechain": false,
  "promptId": "5e77306a-0e66-4a40-a025-b25b4b1efd70",
  "type": "user",
  "uuid": "68d80492-f765-411d-816d-5e4a73e4a070",
  "toolUseResult": {
    "query": "\"reward under attack\" process reward model hackability robustness 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LE9ZS1eDieuQmj2BvRED3k",
        "content": [
          {
            "title": "[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/abs/2603.06621"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of",
            "url": "https://arxiv.org/pdf/2603.06621"
          },
          {
            "title": "GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub",
            "url": "https://github.com/xhwang22/Awesome-Reward-Hacking"
          },
          {
            "title": "[2602.10623v1] Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling",
            "url": "https://arxiv.org/abs/2602.10623v1"
          },
          {
            "title": "[2602.10623] Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling",
            "url": "https://arxiv.org/abs/2602.10623"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2603.06621"
          },
          {
            "title": "Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://arxiv.org/pdf/2502.18770"
          },
          {
            "title": "Robust Reward Modeling via Causal Rubrics",
            "url": "https://arxiv.org/pdf/2506.16507"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/pdf/2604.02986"
          },
          {
            "title": "Adversarial Training of Reward Models",
            "url": "https://arxiv.org/pdf/2504.06141"
          }
        ]
      },
      "I found relevant research on this topic. Here are the key findings:\n\n## \"Reward Under Attack\" Paper\n\nProcess Reward Models (PRMs) are rapidly becoming the backbone of LLM reasoning pipelines, yet state-of-the-art PRMs are systematically exploitable under adversarial optimization pressure.\n\n### Key Findings\n\nWhen policies were trained on AIME problems, they achieved near-perfect PRM rewards (>0.9), while ground-truth accuracy remained low (below 4%), with 43% of reward gains attributable to stylistic shortcuts. This reveals a critical vulnerability in how PRMs evaluate reasoning.\n\nCurrent PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.\n\n### Methodology and Resources\n\nThe researchers introduced a three-tiered diagnostic framework that applies increasing adversarial pressure to quantify vulnerabilities. They released PRM-BiasBench and a diagnostic toolkit to enable robustness evaluation before deployment.\n\nThe paper was published on arXiv on February 20, 2026, by researchers from UC Berkeley, Transmute AI, ICSI, and LBNL, addressing fundamental concerns about the reliability of process reward models in LLM alignment."
    ],
    "durationSeconds": 7.024419720999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "90f787d5-bc83-406c-8f30-b7b53871ae8c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T03:14:53.074Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DyqSsQWFqJMMiyG7NVAHZ5`</summary>

```json
{
  "query": "PET pessimistic reward model ensemble RL training reward hacking defense"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68d80492-f765-411d-816d-5e4a73e4a070",
  "isSidechain": false,
  "requestId": "req_011CbD6ME9hLhk69qoG5HaFK",
  "type": "assistant",
  "uuid": "9810e5f7-437f-4399-8ddb-a96fca07fb50",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LgJBQQa2g89xJFcFpAsn7A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 20994,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 852,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 20994,
          "cache_creation_input_tokens": 852,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 852
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

_source line 25 · 2026-05-20T03:14:59.346Z_

<details><summary>↩ Tool result · `toolu_01DyqSsQWFqJMMiyG7NVAHZ5`</summary>

```text
Web search results for query: "PET pessimistic reward model ensemble RL training reward hacking defense"

Links: [{"title":"Pessimistic Reward Tuning (PET) in RLHF","url":"https://www.emergentmind.com/topics/pessimistic-reward-tuning-pet"},{"title":"Pessimistic Reward Modeling in RLHF against Reward Hacking | OpenReview","url":"https://openreview.net/forum?id=mKPpS6n3cZ"},{"title":"Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/pdf/2505.20556"},{"title":"Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/html/2505.20556v1"},{"title":"Reward Hacking Defense Rubric","url":"https://www.emergentmind.com/topics/reward-hacking-defense-rubric"},{"title":"Pessimistic Reward Modeling in RLHF against Reward Hacking","url":"https://openreview.net/pdf?id=HWOAZUPA0C"},{"title":"[2505.20556] Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/abs/2505.20556"},{"title":"Learning a Pessimistic Reward Model in RLHF - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250520556X/abstract"},{"title":"Learning a Pessimistic Reward Model in RLHF | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.20556v1"}]

Based on the search results, here's what I found about PET (Pessimistic Reward Fine-Tuning):

## Overview

PET is a novel pessimistic reward fine-tuning method designed to learn a pessimistic reward model robust against reward hacking in offline reinforcement learning from human feedback (RLHF).

## The Problem It Addresses

Traditional reward modeling techniques in RLHF train an imperfect reward model on which KL regularization plays a pivotal role in mitigating reward hacking, but such intuition-based methods still suffer from reward hacking and exclude policies with large KL divergence from the dataset distribution during learning.

## How It Works

Multiple algorithmic realizations of PET exist, unified by a systematic focus on lower-bound or distributionally-robust reward estimates, adversarial or ensemble-based surrogates, and quantifiable pessimism tuning. Specifically, the reward model is adversarially trained against a policy model induced by the rejection sampling process.

## Key Advantage

When optimizing a policy on a pessimistic reward model fine-tuned through PET, reward hacking can be prevented without relying on any regularization. Additionally, this approach allows policies to optimize greedily without KL regularization, achieving performance comparable or superior to state-of-the-art methods while maintaining high KL divergence from reference policies.

## Theoretical Results

Under standard assumptions, the Best-of-N (BoN) process on the pessimistic reward fine-tuned by PET has performance comparable to the BoN process on any reward, as long as the corresponding policy induced by the process is covered by the dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9810e5f7-437f-4399-8ddb-a96fca07fb50",
  "isSidechain": false,
  "promptId": "5e77306a-0e66-4a40-a025-b25b4b1efd70",
  "type": "user",
  "uuid": "ca98cd0c-60b5-4306-98eb-a6e69ecf12e6",
  "toolUseResult": {
    "query": "PET pessimistic reward model ensemble RL training reward hacking defense",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KHqs1kg8aounC77HqTWjN7",
        "content": [
          {
            "title": "Pessimistic Reward Tuning (PET) in RLHF",
            "url": "https://www.emergentmind.com/topics/pessimistic-reward-tuning-pet"
          },
          {
            "title": "Pessimistic Reward Modeling in RLHF against Reward Hacking | OpenReview",
            "url": "https://openreview.net/forum?id=mKPpS6n3cZ"
          },
          {
            "title": "Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/pdf/2505.20556"
          },
          {
            "title": "Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/html/2505.20556v1"
          },
          {
            "title": "Reward Hacking Defense Rubric",
            "url": "https://www.emergentmind.com/topics/reward-hacking-defense-rubric"
          },
          {
            "title": "Pessimistic Reward Modeling in RLHF against Reward Hacking",
            "url": "https://openreview.net/pdf?id=HWOAZUPA0C"
          },
          {
            "title": "[2505.20556] Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/abs/2505.20556"
          },
          {
            "title": "Learning a Pessimistic Reward Model in RLHF - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250520556X/abstract"
          },
          {
            "title": "Learning a Pessimistic Reward Model in RLHF | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2505.20556v1"
          }
        ]
      },
      "Based on the search results, here's what I found about PET (Pessimistic Reward Fine-Tuning):\n\n## Overview\n\nPET is a novel pessimistic reward fine-tuning method designed to learn a pessimistic reward model robust against reward hacking in offline reinforcement learning from human feedback (RLHF).\n\n## The Problem It Addresses\n\nTraditional reward modeling techniques in RLHF train an imperfect reward model on which KL regularization plays a pivotal role in mitigating reward hacking, but such intuition-based methods still suffer from reward hacking and exclude policies with large KL divergence from the dataset distribution during learning.\n\n## How It Works\n\nMultiple algorithmic realizations of PET exist, unified by a systematic focus on lower-bound or distributionally-robust reward estimates, adversarial or ensemble-based surrogates, and quantifiable pessimism tuning. Specifically, the reward model is adversarially trained against a policy model induced by the rejection sampling process.\n\n## Key Advantage\n\nWhen optimizing a policy on a pessimistic reward model fine-tuned through PET, reward hacking can be prevented without relying on any regularization. Additionally, this approach allows policies to optimize greedily without KL regularization, achieving performance comparable or superior to state-of-the-art methods while maintaining high KL divergence from reference policies.\n\n## Theoretical Results\n\nUnder standard assumptions, the Best-of-N (BoN) process on the pessimistic reward fine-tuned by PET has performance comparable to the BoN process on any reward, as long as the corresponding policy induced by the process is covered by the dataset."
    ],
    "durationSeconds": 6.268297008000008,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9810e5f7-437f-4399-8ddb-a96fca07fb50",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-L…",
  "leafUuid": "ca98cd0c-60b5-4306-98eb-a6e69ecf12e6",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM calibration and reward hacking resistance proposal",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0"
}
```

---

### Tool call

_source line 28 · 2026-05-20T03:15:01.339Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CdkWSDSe4zALJ222GruGbn`</summary>

```json
{
  "query": "reward model calibration ECE expected calibration error LLM reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca98cd0c-60b5-4306-98eb-a6e69ecf12e6",
  "isSidechain": false,
  "requestId": "req_011CbD6MqoKESyAEouxrqeEu",
  "type": "assistant",
  "uuid": "2e0deba4-bf54-4242-b325-a34569444c43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KYkjcsrpyuSeLooFqMWmrL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 895,
      "cache_read_input_tokens": 21846,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 21846,
          "cache_creation_input_tokens": 895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 895
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

_source line 29 · 2026-05-20T03:15:14.673Z_

<details><summary>↩ Tool result · `toolu_01CdkWSDSe4zALJ222GruGbn`</summary>

```text
Web search results for query: "reward model calibration ECE expected calibration error LLM reasoning 2025 2026"

Links: [{"title":"Calibrated Reasoning Signals","url":"https://www.emergentmind.com/topics/calibrated-reasoning-signals"},{"title":"Confidence Calibration in LLMs","url":"https://www.emergentmind.com/topics/confidence-calibration-in-llms"},{"title":"Know What You Don’t Know: Uncertainty Calibration of Process Reward Models","url":"https://arxiv.org/pdf/2506.09338"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/html/2511.00280v1"},{"title":"Know What You Don't Know: Uncertainty Calibration of Process Reward Models | OpenReview","url":"https://openreview.net/forum?id=hzMkfIrdDT"},{"title":"Assessing Model Calibration in LLMs","url":"https://apxml.com/courses/fine-tuning-adapting-large-language-models/chapter-6-evaluation-analysis-fine-tuned-models/model-calibration-assessment"},{"title":"Expected Calibration Error in ML","url":"https://www.emergentmind.com/topics/expected-calibration-error"},{"title":"Expected Calibration Error (ECE) Overview","url":"https://www.emergentmind.com/topics/expected-calibration-error-ece"},{"title":"Restoring Calibration for Aligned Large Language Models: A Calibration-Aware Fine-Tuning Approach","url":"https://arxiv.org/pdf/2505.01997"}]

I found several recent sources on reward model calibration, ECE, and LLM reasoning from 2025-2026. Here are the key findings:

## Process Reward Model Calibration

State-of-the-art process reward models (PRMs) can be poorly calibrated, particularly overestimating the success probability that a partial reasoning step will lead to a correct final answer when smaller LLMs complete the reasoning trajectory. A quantile-regression calibration approach has been introduced to align their outputs with success probabilities.

## Calibration-Aware Reinforcement Learning

Calibration-aware RL mitigates reward-induced overconfidence on decision tokens arising from RLHF/RLVR; adding a calibration loss term (e.g., CE on decision token) preserves accuracy gains and reduces ECE by up to 9 points.

## Recent Calibration Methods

Critique-based calibration using natural language critique prompts teaches LLMs patterns of over-/under-confidence, yielding significant ECE reduction even out-of-domain. Additionally, reinforcement learning with proper scoring rule rewards (log-scoring or tokenized Brier score) provably aligns expressed confidence with empirical accuracy, achieving state-of-the-art calibration and robust out-of-distribution generalization.

## ECE Metric Challenges

The population ECE is not estimable from finite data without strong regularity assumptions, and in practice all implementations fall back to empirical binned ECE with no uniform sample-consistency guarantees.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e0deba4-bf54-4242-b325-a34569444c43",
  "isSidechain": false,
  "promptId": "5e77306a-0e66-4a40-a025-b25b4b1efd70",
  "type": "user",
  "uuid": "60753f7a-62cd-4caf-8bdc-9c811d76d83b",
  "toolUseResult": {
    "query": "reward model calibration ECE expected calibration error LLM reasoning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NfsRS8LqRvy43p6cWoBcjv",
        "content": [
          {
            "title": "Calibrated Reasoning Signals",
            "url": "https://www.emergentmind.com/topics/calibrated-reasoning-signals"
          },
          {
            "title": "Confidence Calibration in LLMs",
            "url": "https://www.emergentmind.com/topics/confidence-calibration-in-llms"
          },
          {
            "title": "Know What You Don’t Know: Uncertainty Calibration of Process Reward Models",
            "url": "https://arxiv.org/pdf/2506.09338"
          },
          {
            "title": "Calibration Across Layers: Understanding Calibration Evolution in LLMs",
            "url": "https://arxiv.org/html/2511.00280v1"
          },
          {
            "title": "Know What You Don't Know: Uncertainty Calibration of Process Reward Models | OpenReview",
            "url": "https://openreview.net/forum?id=hzMkfIrdDT"
          },
          {
            "title": "Assessing Model Calibration in LLMs",
            "url": "https://apxml.com/courses/fine-tuning-adapting-large-language-models/chapter-6-evaluation-analysis-fine-tuned-models/model-calibration-assessment"
          },
          {
            "title": "Expected Calibration Error in ML",
            "url": "https://www.emergentmind.com/topics/expected-calibration-error"
          },
          {
            "title": "Expected Calibration Error (ECE) Overview",
            "url": "https://www.emergentmind.com/topics/expected-calibration-error-ece"
          },
          {
            "title": "Restoring Calibration for Aligned Large Language Models: A Calibration-Aware Fine-Tuning Approach",
            "url": "https://arxiv.org/pdf/2505.01997"
          }
        ]
      },
      "I found several recent sources on reward model calibration, ECE, and LLM reasoning from 2025-2026. Here are the key findings:\n\n## Process Reward Model Calibration\n\nState-of-the-art process reward models (PRMs) can be poorly calibrated, particularly overestimating the success probability that a partial reasoning step will lead to a correct final answer when smaller LLMs complete the reasoning trajectory. A quantile-regression calibration approach has been introduced to align their outputs with success probabilities.\n\n## Calibration-Aware Reinforcement Learning\n\nCalibration-aware RL mitigates reward-induced overconfidence on decision tokens arising from RLHF/RLVR; adding a calibration loss term (e.g., CE on decision token) preserves accuracy gains and reduces ECE by up to 9 points.\n\n## Recent Calibration Methods\n\nCritique-based calibration using natural language critique prompts teaches LLMs patterns of over-/under-confidence, yielding significant ECE reduction even out-of-domain. Additionally, reinforcement learning with proper scoring rule rewards (log-scoring or tokenized Brier score) provably aligns expressed confidence with empirical accuracy, achieving state-of-the-art calibration and robust out-of-distribution generalization.\n\n## ECE Metric Challenges\n\nThe population ECE is not estimable from finite data without strong regularity assumptions, and in practice all implementations fall back to empirical binned ECE with no uniform sample-consistency guarantees."
    ],
    "durationSeconds": 13.329978804000014,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2e0deba4-bf54-4242-b325-a34569444c43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-20T03:15:14.677Z_

```json
{
  "parentUuid": "60753f7a-62cd-4caf-8bdc-9c811d76d83b",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "bb74ddd3-6cd4-4e8a-8965-adb7d7f70689",
  "timestamp": "2026-05-20T03:15:14.677Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-20T03:15:17.838Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012JbQVuWqnw6o7NjiEqiVoE`</summary>

```json
{
  "query": "\"APRM\" adaptive process reward model OR \"conformal prediction\" reward model 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb74ddd3-6cd4-4e8a-8965-adb7d7f70689",
  "isSidechain": false,
  "requestId": "req_011CbD6NyPVZ9gLqggA6o2WB",
  "type": "assistant",
  "uuid": "5f3345d6-45df-42ec-a2a0-9576c26f9178",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uyo4zQYDfraYjynS69SxgM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 956,
      "cache_read_input_tokens": 22741,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 956,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 22741,
          "cache_creation_input_tokens": 956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 956
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

_source line 32 · 2026-05-20T03:15:25.574Z_

<details><summary>↩ Tool result · `toolu_012JbQVuWqnw6o7NjiEqiVoE`</summary>

```text
Web search results for query: ""APRM" adaptive process reward model OR "conformal prediction" reward model 2025 2026"

Links: [{"title":"Adversarial Training for Process Reward Models","url":"https://arxiv.org/html/2511.22888"},{"title":"Adversarial Training for Process Reward Models","url":"https://arxiv.org/pdf/2511.22888"},{"title":"Conformal Prediction Conference 2026","url":"https://copa-conference.com/"},{"title":"Conformal Prediction Adaptive to Unknown Subpopulation Shifts | OpenReview","url":"https://openreview.net/forum?id=0aNfWttgHd"},{"title":"(PDF) Conformal Prediction for Generative Models via Adaptive Cluster-Based Density Estimation","url":"https://www.researchgate.net/publication/400340012_Conformal_Prediction_for_Generative_Models_via_Adaptive_Cluster-Based_Density_Estimation"},{"title":"Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport","url":"https://arxiv.org/html/2605.06785"},{"title":"Multi-model Ensemble Conformal Prediction in Dynamic Environments","url":"https://arxiv.org/pdf/2411.03678"}]

Based on the search results, I found relevant information about both APRM and conformal prediction approaches in recent research:

## APRM (Adversarially Trained Process Reward Models)

APRM (Adversarially Trained Process Reward Models) is a new approach introduced in recent work. It provides an adaptive curriculum for PRM training where negative sample hardness dynamically increases while aligning with the PRM's evolving capabilities, making the PRM robust to increasingly subtle errors. The training is formulated as a two-player, general-sum, non-cooperative game. APRM achieves gains of +5.3 percentage points on out-of-distribution tasks.

## Conformal Prediction Approaches for Reward Models

There are also recent advances combining conformal prediction with reward models:

One approach uses conditional optimal transport to calibrate process reward models, allowing for flexible and efficient uncertainty estimation without requiring retraining for different quantile levels. Conformal prediction has been studied as one approach for uncertainty quantification in large language models.

Additionally, recent work from February 2026 applies conformal prediction to generative models, providing a model-agnostic framework that yields prediction sets with finite-sample coverage guarantees.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f3345d6-45df-42ec-a2a0-9576c26f9178",
  "isSidechain": false,
  "promptId": "5e77306a-0e66-4a40-a025-b25b4b1efd70",
  "type": "user",
  "uuid": "ecb030bc-0c8b-4fc9-8df4-bfb70cf26883",
  "toolUseResult": {
    "query": "\"APRM\" adaptive process reward model OR \"conformal prediction\" reward model 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01M2CvFVvcG9yysUoCUeGn5J",
        "content": [
          {
            "title": "Adversarial Training for Process Reward Models",
            "url": "https://arxiv.org/html/2511.22888"
          },
          {
            "title": "Adversarial Training for Process Reward Models",
            "url": "https://arxiv.org/pdf/2511.22888"
          },
          {
            "title": "Conformal Prediction Conference 2026",
            "url": "https://copa-conference.com/"
          },
          {
            "title": "Conformal Prediction Adaptive to Unknown Subpopulation Shifts | OpenReview",
            "url": "https://openreview.net/forum?id=0aNfWttgHd"
          },
          {
            "title": "(PDF) Conformal Prediction for Generative Models via Adaptive Cluster-Based Density Estimation",
            "url": "https://www.researchgate.net/publication/400340012_Conformal_Prediction_for_Generative_Models_via_Adaptive_Cluster-Based_Density_Estimation"
          },
          {
            "title": "Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport",
            "url": "https://arxiv.org/html/2605.06785"
          },
          {
            "title": "Multi-model Ensemble Conformal Prediction in Dynamic Environments",
            "url": "https://arxiv.org/pdf/2411.03678"
          }
        ]
      },
      "Based on the search results, I found relevant information about both APRM and conformal prediction approaches in recent research:\n\n## APRM (Adversarially Trained Process Reward Models)\n\nAPRM (Adversarially Trained Process Reward Models) is a new approach introduced in recent work. It provides an adaptive curriculum for PRM training where negative sample hardness dynamically increases while aligning with the PRM's evolving capabilities, making the PRM robust to increasingly subtle errors. The training is formulated as a two-player, general-sum, non-cooperative game. APRM achieves gains of +5.3 percentage points on out-of-distribution tasks.\n\n## Conformal Prediction Approaches for Reward Models\n\nThere are also recent advances combining conformal prediction with reward models:\n\nOne approach uses conditional optimal transport to calibrate process reward models, allowing for flexible and efficient uncertainty estimation without requiring retraining for different quantile levels. Conformal prediction has been studied as one approach for uncertainty quantification in large language models.\n\nAdditionally, recent work from February 2026 applies conformal prediction to generative models, providing a model-agnostic framework that yields prediction sets with finite-sample coverage guarantees."
    ],
    "durationSeconds": 7.728400179000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5f3345d6-45df-42ec-a2a0-9576c26f9178",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T03:15:27.918Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011KCmG3WMHAycS41YdC7MSr`</summary>

```json
{
  "query": "Hessian spectral analysis reward model landscape flatness sharpness RL 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecb030bc-0c8b-4fc9-8df4-bfb70cf26883",
  "isSidechain": false,
  "requestId": "req_011CbD6PmzB2pug7qC6wC42X",
  "type": "assistant",
  "uuid": "c040948d-fd66-4883-95ba-489988c57198",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CdbJuso8Q6pQxCfjxvyBgA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 698,
      "cache_read_input_tokens": 23697,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 23697,
          "cache_creation_input_tokens": 698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 698
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

_source line 34 · 2026-05-20T03:15:35.468Z_

<details><summary>↩ Tool result · `toolu_011KCmG3WMHAycS41YdC7MSr`</summary>

```text
Web search results for query: "Hessian spectral analysis reward model landscape flatness sharpness RL 2025 2026"

Links: [{"title":"Sharpness of Minima in Deep Matrix Factorization","url":"https://arxiv.org/html/2509.25783"},{"title":"On progressive sharpening, flat minima and generalisation","url":"https://arxiv.org/pdf/2305.14683"},{"title":"A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of LLMs","url":"https://arxiv.org/pdf/2601.16979"},{"title":"R\\'enyi Sharpness: A Novel Sharpness that Strongly Correlates with Generalization","url":"https://arxiv.org/pdf/2510.07758"},{"title":"The effects of Hessian eigenvalue spectral density type on the applicability of Hessian analysis to generalization capability assessment of neural networks","url":"https://arxiv.org/html/2504.17618v1"},{"title":"Does SGD Seek Flatness or Sharpness? An Exactly Solvable Model","url":"https://arxiv.org/pdf/2602.05065"},{"title":"Unraveling the Hessian: A Key to Smooth Convergence in Loss Function Landscapes","url":"https://arxiv.org/html/2409.11995v1"}]

Based on the search results, here's what I found regarding Hessian spectral analysis, reward model landscape flatness and sharpness in RL for 2025-2026:

## Recent Work on Hessian Spectral Analysis and Loss Landscape

Recent research demonstrates that scalable Hessian sharpness measures capture well-documented phenomena including progressive sharpening and Edge of Stability, with the first demonstration of these sharpness phenomena at scale up to 7B parameters in both pre-training and mid-training of OLMo-2 models.

The largest eigenvalue of the Hessian (Hessian sharpness) quantifies the worst-case curvature of the landscape, while its reciprocal (flatness 1/λ_max^H) is a complementary measure.

## Novel Sharpness Measures

Research from September 2025 proposes Rényi sharpness, a novel sharpness measure defined as the negative Rényi entropy of the loss Hessian, to better correlate with generalization.

## Theoretical Advances

Recent work clarifies flatness-seeking behavior of SGD by identifying an analytically solvable model that exhibits both flattening and sharpening behavior, finding that SGD training shows no a priori preference for flatness but rather a preference for minimal gradient fluctuations.

Maximum Hessian eigenvalue and Hessian trace are conventionally believed to be good indicators of loss landscape flatness and generalization capability, with smaller maximum eigenvalues indicating flatter loss landscapes that lead to better generalization.

The search results focus primarily on general neural network loss landscape analysis rather than specifically on reward models in reinforcement learning contexts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c040948d-fd66-4883-95ba-489988c57198",
  "isSidechain": false,
  "promptId": "5e77306a-0e66-4a40-a025-b25b4b1efd70",
  "type": "user",
  "uuid": "5daf48b0-00be-4dfc-bc65-44eadfe99243",
  "toolUseResult": {
    "query": "Hessian spectral analysis reward model landscape flatness sharpness RL 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EFjwZ7Jfe8TDA8ejJTLhJr",
        "content": [
          {
            "title": "Sharpness of Minima in Deep Matrix Factorization",
            "url": "https://arxiv.org/html/2509.25783"
          },
          {
            "title": "On progressive sharpening, flat minima and generalisation",
            "url": "https://arxiv.org/pdf/2305.14683"
          },
          {
            "title": "A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of LLMs",
            "url": "https://arxiv.org/pdf/2601.16979"
          },
          {
            "title": "R\\'enyi Sharpness: A Novel Sharpness that Strongly Correlates with Generalization",
            "url": "https://arxiv.org/pdf/2510.07758"
          },
          {
            "title": "The effects of Hessian eigenvalue spectral density type on the applicability of Hessian analysis to generalization capability assessment of neural networks",
            "url": "https://arxiv.org/html/2504.17618v1"
          },
          {
            "title": "Does SGD Seek Flatness or Sharpness? An Exactly Solvable Model",
            "url": "https://arxiv.org/pdf/2602.05065"
          },
          {
            "title": "Unraveling the Hessian: A Key to Smooth Convergence in Loss Function Landscapes",
            "url": "https://arxiv.org/html/2409.11995v1"
          }
        ]
      },
      "Based on the search results, here's what I found regarding Hessian spectral analysis, reward model landscape flatness and sharpness in RL for 2025-2026:\n\n## Recent Work on Hessian Spectral Analysis and Loss Landscape\n\nRecent research demonstrates that scalable Hessian sharpness measures capture well-documented phenomena including progressive sharpening and Edge of Stability, with the first demonstration of these sharpness phenomena at scale up to 7B parameters in both pre-training and mid-training of OLMo-2 models.\n\nThe largest eigenvalue of the Hessian (Hessian sharpness) quantifies the worst-case curvature of the landscape, while its reciprocal (flatness 1/λ_max^H) is a complementary measure.\n\n## Novel Sharpness Measures\n\nResearch from September 2025 proposes Rényi sharpness, a novel sharpness measure defined as the negative Rényi entropy of the loss Hessian, to better correlate with generalization.\n\n## Theoretical Advances\n\nRecent work clarifies flatness-seeking behavior of SGD by identifying an analytically solvable model that exhibits both flattening and sharpening behavior, finding that SGD training shows no a priori preference for flatness but rather a preference for minimal gradient fluctuations.\n\nMaximum Hessian eigenvalue and Hessian trace are conventionally believed to be good indicators of loss landscape flatness and generalization capability, with smaller maximum eigenvalues indicating flatter loss landscapes that lead to better generalization.\n\nThe search results focus primarily on general neural network loss landscape analysis rather than specifically on reward models in reinforcement learning contexts."
    ],
    "durationSeconds": 7.545851263000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c040948d-fd66-4883-95ba-489988c57198",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T03:15:41.734Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ChqtHtR6CMWrb7UFrk5sKe`</summary>

```json
{
  "query": "\"distributional process reward model\" calibrated prediction future rewards conditional optimal transport 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5daf48b0-00be-4dfc-bc65-44eadfe99243",
  "isSidechain": false,
  "requestId": "req_011CbD6QWF9yXVvKoyWx4bzj",
  "type": "assistant",
  "uuid": "a7751850-a051-48f9-b164-34f01593f2b2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0177yYSDSjU6k2wTortPikMN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 24395,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 829,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 24395,
          "cache_creation_input_tokens": 829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 829
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

_source line 36 · 2026-05-20T03:15:48.225Z_

<details><summary>↩ Tool result · `toolu_01ChqtHtR6CMWrb7UFrk5sKe`</summary>

```text
Web search results for query: ""distributional process reward model" calibrated prediction future rewards conditional optimal transport 2026"

Links: [{"title":"[2605.06785] Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport","url":"https://arxiv.org/abs/2605.06785"},{"title":"Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport","url":"https://arxiv.org/html/2605.06785"},{"title":"APLOT: Robust Reward Modeling via Adaptive Preference Learning with Optimal Transport","url":"https://arxiv.org/pdf/2510.10963"},{"title":"Conditional Risk Minimization with Side Information: A Tractable, Universal Optimal Transport Framework","url":"https://arxiv.org/pdf/2509.23128"},{"title":"A multidimensional distributional map of future reward in dopamine neurons - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/40468078/"},{"title":"Distributional Preference Alignment of LLMs via Optimal Transport","url":"https://arxiv.org/pdf/2406.05882"},{"title":"A multidimensional distributional map of future reward in dopamine neurons | Nature","url":"https://www.nature.com/articles/s41586-025-09089-6"}]

Based on the web search results, I found relevant information about your query:

Inference-time scaling methods rely on Process Reward Models (PRMs), which are often poorly calibrated and overestimate success probabilities. 

The paper proposes the first use of conditional optimal transport for calibrating PRMs, modifying conditional OT (CondOT) map learning to estimate a monotonic conditional quantile function over success probabilities estimated by the PRM, conditioned on PRM hidden states.

This yields structurally valid quantile estimates and enables efficient extraction of confidence bounds at arbitrary levels, which is integrated into the instance-adaptive scaling (IAS) framework.

The method was evaluated on mathematical reasoning benchmarks spanning moderate-difficulty problems (MATH-500) and harder out-of-distribution problems (AIME), and for PRMs with reliable ranking signals, the method substantially improves calibration over both uncalibrated PRMs and quantile regression.

The paper "Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport" (arXiv:2605.06785) appears to be a very recent work from May 2026 that directly addresses your query topic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7751850-a051-48f9-b164-34f01593f2b2",
  "isSidechain": false,
  "promptId": "5e77306a-0e66-4a40-a025-b25b4b1efd70",
  "type": "user",
  "uuid": "1c2d901f-564b-4813-aebe-c5511b867dc9",
  "toolUseResult": {
    "query": "\"distributional process reward model\" calibrated prediction future rewards conditional optimal transport 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Gpm8zRHp4CaJX7rWTf46AW",
        "content": [
          {
            "title": "[2605.06785] Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport",
            "url": "https://arxiv.org/abs/2605.06785"
          },
          {
            "title": "Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport",
            "url": "https://arxiv.org/html/2605.06785"
          },
          {
            "title": "APLOT: Robust Reward Modeling via Adaptive Preference Learning with Optimal Transport",
            "url": "https://arxiv.org/pdf/2510.10963"
          },
          {
            "title": "Conditional Risk Minimization with Side Information: A Tractable, Universal Optimal Transport Framework",
            "url": "https://arxiv.org/pdf/2509.23128"
          },
          {
            "title": "A multidimensional distributional map of future reward in dopamine neurons - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/40468078/"
          },
          {
            "title": "Distributional Preference Alignment of LLMs via Optimal Transport",
            "url": "https://arxiv.org/pdf/2406.05882"
          },
          {
            "title": "A multidimensional distributional map of future reward in dopamine neurons | Nature",
            "url": "https://www.nature.com/articles/s41586-025-09089-6"
          }
        ]
      },
      "Based on the web search results, I found relevant information about your query:\n\nInference-time scaling methods rely on Process Reward Models (PRMs), which are often poorly calibrated and overestimate success probabilities. \n\nThe paper proposes the first use of conditional optimal transport for calibrating PRMs, modifying conditional OT (CondOT) map learning to estimate a monotonic conditional quantile function over success probabilities estimated by the PRM, conditioned on PRM hidden states.\n\nThis yields structurally valid quantile estimates and enables efficient extraction of confidence bounds at arbitrary levels, which is integrated into the instance-adaptive scaling (IAS) framework.\n\nThe method was evaluated on mathematical reasoning benchmarks spanning moderate-difficulty problems (MATH-500) and harder out-of-distribution problems (AIME), and for PRMs with reliable ranking signals, the method substantially improves calibration over both uncalibrated PRMs and quantile regression.\n\nThe paper \"Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport\" (arXiv:2605.06785) appears to be a very recent work from May 2026 that directly addresses your query topic."
    ],
    "durationSeconds": 6.486006909000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a7751850-a051-48f9-b164-34f01593f2b2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-20T03:17:04.240Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the landscape. Let me synthesize my findings and evaluate the proposal.

Key papers found:
1. **"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models"** (arXiv:2603.06621, Feb 2026) - This is very directly related. It introduces a three-tiered diagnostic framework for PRM hackability. Shows PRMs function as "fluency detectors" rather than reasoning verifiers.

2. **Ackermann et al., "Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards"** (arXiv:2602.18037, Feb 2026) - The proposal explicitly references this work and proposes to extend it from outcome-level to step-level analysis.


3. **"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism"** (arXiv:2604.04648, April 2026) - The "Caution" baseline that uses prediction error to implement pessimism.

4. **"Learning a Pessimistic Reward Model in RLHF" / PET** (arXiv:2505.20556, May 2025) - The PET baseline employing global pessimism.

5. **APRM - "Adversarial Training for Process Reward Models"** - Still reviewing this one.

6. **"Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport"** (arXiv:2605.06785, May 2026) - A recent paper directly tackling PRM calibration to improve inference-time scaling.

7. **"Know What You Don't Know: Uncertainty Calibration of Process Reward Models"** (arXiv:2506.09338) - Focuses specifically on calibrating PRM uncertainty.

8. **PURE / "Stop Summation: Min-Form Credit Assignment"** (arXiv:2504.15275) - Tackles reward hacking by reformulating how credit gets assigned.

Now I'm evaluating the proposal's central argument about whether PRM calibration quality directly causes better inference-time scaling.

The core insight—that well-calibrated reward models are harder to exploit because their confidence better matches actual correctness—is intuitive but not entirely novel. The "Reward Under Attack" paper already analyzes PRM hackability extensively, and the "Distributional PRM" paper already addresses calibration for scaling. The proposal's contribution is connecting these two threads. The CGSP formula applies pessimistic scaling based on calibrated uncertainty, which is a reasonable approach but fairly straightforward given existing work.

The research question is timely and important, but I'm skeptical about how surprising the findings would be—most researchers would likely expect that better-calibrated models are naturally harder to hack. And there's a simpler alternative worth considering: just applying post-hoc calibration techniques like temperature scaling rather than building calibration into the training process.

I'm also noticing that the proposal assumes calibration quality is the primary driver of hackability, when other factors like representation quality or training data distribution could matter just as much. The causal experiments help isolate this, but there's an underlying assumption that per-step uncertainty signals from a calibrated model are actually meaningful and reliable.

There's also a practical concern: the calibration drift detector needs to compute ECE in real-time during RL training, but where do the ground-truth labels come from for those rollout samples?

Looking at the overall assessment, this is a solid piece of work that tackles a genuine problem, but the core insight about calibration driving robustness feels fairly intuitive rather than novel. The CGSP defense itself is a straightforward combination of existing techniques—pessimism plus calibration weighting. The Hessian analysis extension is incremental, and there's already a cluster of similar recent work in this space that makes the contribution feel less distinctive.

The proposal is well-organized with clear contributions and appropriate experimental design, but there's a significant issue I'm noticing: this is submitted to CoRL 2026, which is a robotics conference, yet the entire work focuses on LLM reasoning with MATH-500 and AIME benchmarks. That's fundamentally an NLP paper, not robotics research—this is a serious venue mismatch that undermines the submission.

Setting that concern aside and evaluating the idea itself, the novelty feels medium at best. The connection between calibration and adversarial robustness is somewhat intuitive, and the defense mechanism is a straightforward combination of existing techniques. The significance is also medium—it addresses an important problem but the contribution is incremental, and the space is already crowded with very recent related work. The core insight, while solid, isn't particularly surprising or impactful.

I'm estimating this lands in the 25-35% acceptance range. The direction is sound and there's a real novelty delta, but if the results are positive, reviewers would likely feel they could have predicted the outcome. There's also a critical issue I can't ignore: this paper has no robotics content whatsoever, so submitting to CoRL would likely result in desk rejection or immediate rejection for being out of scope, unless the venue has dramatically expanded its scope. Significance feels incremental since calibration improving robustness isn't particularly surprising, and the field is crowding with related work—especially that recent Distributional PRM paper from May that directly tackles the same calibration angle. My confidence lands around 25%, with the main concern being that CGSP's advantage over just calibrating the PRM and adding pessimism isn't clearly justified, plus there's a real question about whether this fits CoRL's scope.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c2d901f-564b-4813-aebe-c5511b867dc9",
  "isSidechain": false,
  "requestId": "req_011CbD6RSo4zppyDzsWzevxf",
  "type": "assistant",
  "uuid": "b1386f18-d358-4a69-99da-c69c63bb9f0c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168gBNodrWstSsfB1PDPCCW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 25224,
      "output_tokens": 6277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 700,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6277,
          "cache_read_input_tokens": 25224,
          "cache_creation_input_tokens": 700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 700
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

_source line 38 · 2026-05-20T03:18:19.970Z_

Now I have sufficient information to provide my evaluation. Let me compile the assessment.

---

```
【阶段】: Triage

【领域调研】:

- "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models" (arXiv:2603.06621, 2026):
  最直接的竞争工作。提出三层诊断框架 (gradient attacks, RL-induced hacking, BoN overopt) 量化 PRM hackability。发现 AIME 上 PRM reward >0.9 但 ground-truth accuracy <4%，43% reward gains 来自 stylistic shortcuts。本 proposal 的实验框架（gradient attacks + RL-induced + BoN）几乎完全与此工作重叠，只是加了"calibration"这个变量。

- Ackermann et al., "Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards" (arXiv:2602.18037, 2026):
  Proposal 明确引用并声称要扩展的工作。证明 reward accuracy 与 loss landscape flatness 相关，提出 gradient regularization 作为防御。Proposal 声称将其 outcome-level gradient norm 分析扩展到 step-level Hessian spectral analysis，这是增量性扩展。

- "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism" (arXiv:2604.04648, 2026):
  Proposal 中的 "Caution" baseline。使用 prediction error 驱动的 pessimism 来缓解 BoN 中的 reward hacking。已在理论 (linear setting) 和实验上证明 pessimism 有效。Proposal 的 CGSP 与此高度相似，区别在于 CGSP 用 calibration quality 来调制 pessimism 程度。

- "Learning a Pessimistic Reward Model in RLHF" / PET (arXiv:2505.20556, 2025):
  Proposal 中的另一个 baseline。使用 global pessimism（adversarially fine-tuned reward model）防御 reward hacking，不依赖 KL regularization。Proposal 声称 CGSP 优于 PET 的点在于"step-level + calibration-grounded + adaptive"，但 PET 的 global pessimism 已经相当有效。

- "Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport" (arXiv:2605.06785, May 2026):
  **Proposal 未引用但高度相关的最新工作**。使用 conditional OT 对 PRM 进行 calibration，产生任意 quantile level 的 confidence bounds。在 MATH-500 和 AIME 上验证。该工作直接做了"PRM calibration"，虽然应用场景是 inference-time scaling 而非 reward hacking defense，但方法论和 PRM calibration 的技术手段高度重叠。

- APRM: "Adversarial Training for Process Reward Models" (arXiv:2511.22888, 2025):
  Proposal 中的 baseline。通过对抗训练增强 PRM 鲁棒性，+5.3pp OOD improvement。

- "Know What You Don't Know: Uncertainty Calibration of Process Reward Models" (arXiv:2506.09338):
  直接研究 PRM 的 uncertainty calibration，发现 SOTA PRM 严重 miscalibrated，提出 quantile regression calibration。

- PURE / "Stop Summation: Min-Form Credit Assignment" (arXiv:2504.15275, 2025):
  通过改变 credit assignment 形式（sum → min）缓解 reward hacking，不需要改变 reward model 本身。

- 调研总结: PRM hackability 和 PRM calibration 分别是 2025-2026 的活跃研究方向，已有大量工作分别攻克。本 proposal 试图"bridge"二者，但该桥接的核心洞察（calibration → robustness）在直觉上是显然的，且近期已有工作从不同角度部分覆盖了这一连接（如 Distributional PRM 做 calibration for better scaling, Caution 做 uncertainty-driven pessimism）。该领域竞争激烈，proposal 的 novelty delta 被快速压缩。


【Trivial Alternative 检验】:

存在明显的 trivial alternative 威胁：

1. **直接 post-hoc calibration + 现有 pessimism 方法**：Proposal 自己的实验设计中已经包含了 temperature scaling / Platt scaling 等 post-hoc 方法。如果 calibration 真的是关键因素，那么简单地对现有 PRM 做 temperature scaling 再搭配已有的 pessimism 方法（如 Caution 或 ensemble-min）就应该能获得大部分收益。CGSP 相对于这种简单组合的增量价值需要仔细论证，但 proposal 没有将"calibrated PRM + existing defense"作为 baseline。

2. **Min-form credit assignment (PURE)**：完全不需要改动 reward model，仅改变 RL 中的 credit assignment 就能缓解 reward hacking。如果 PURE 的效果已经足够好，那么在 reward model 层面做复杂的 calibration-gated defense 是否 over-engineering？

3. **CGSP 公式本身的简单性**：r̃_t = μ_t − α·σ_t/√c_t 本质上是 LCB (Lower Confidence Bound)，这是 bandit/RL 文献中极为经典的思路。区别仅在于用 calibration quality c_t 做分母——这算不算一个"新方法"，还是仅仅是 LCB 的一个 trivially different instantiation？


【前提假设检验】:

核心逻辑链中有以下未经验证的假设：

1. **"Calibration quality 是 hackability 的主要因果驱动因素"**——这是整篇论文的核心 claim，但目前仅有相关性证据（proposal 自己也是先做 correlation study 再做 causal isolation）。然而，hackability 可能主要由 representation quality、training data distribution、model capacity 等因素决定，calibration 可能只是其中一个弱相关因素。如果 48 个配置的相关性实验结果显示 r < 0.29（即统计不显著），整篇论文的 story 将崩塌。

2. **"Per-step σ_t 是可靠的 uncertainty signal"**——PRM 通常用 binary labels 训练（correct/incorrect step），其输出的 sigmoid probability 不一定携带有意义的 aleatoric/epistemic uncertainty 信息。仅仅通过 post-hoc calibration 不能将一个确定性模型变成一个有良好 uncertainty quantification 的模型。

3. **"Calibration Drift Detector 可在 RL 训练中实时计算 ECE"**——ECE 的计算需要 ground-truth labels。在 RL 训练的 rollouts 中，如何获取 step-level ground truth？如果依赖 verifiable final answers (如 MATH)，那只有 outcome-level signal，无法计算 step-level ECE。这是一个实际可行性上的逻辑漏洞。

4. **"Post-hoc calibration provably preserves model representations"**——Temperature scaling 确实不改变 representations，但 isotonic regression 和 conformal prediction 的"representation preservation"属性需要更仔细的论证。CKA verification 是一种弱验证。


【3 维度打分】:

1. **Novelty: 弱-中** — 
   核心 idea（calibration → robustness）在直觉上是显然的：一个输出 well-calibrated probabilities 的 reward model 自然更难被 exploit，因为它的 scores 更准确地反映 true quality。"Reward Under Attack"(2603.06621) 已经建立了 PRM hackability 的系统分析框架；"Caution"(2604.04648) 已经在用 uncertainty-driven pessimism 防御 reward hacking；"Distributional PRM"(2605.06785) 已经在做 PRM calibration。本 proposal 的贡献主要是将这些已有 thread 做 systematic combination + 加上 causal framing，但组合本身缺乏 conceptual surprise。CGSP 公式 r̃_t = μ_t − α·σ_t/√c_t 是 LCB 的一个 straightforward variant。Step-level Hessian analysis 是 Ackermann et al. 的增量扩展。

2. **Significance: 中** — 
   研究问题（PRM 为什么被 hack、如何防御）是 2025-2026 LLM reasoning 领域的核心问题之一，重要性不可否认。但本 proposal 的预期贡献是一个"连接两个已有 thread"的 bridge paper。如果核心实验结果是 positive（calibration 确实与 hackability 强相关），审稿人的反应大概率是"makes sense, I would have guessed this"而不是"surprising"。CGSP 作为防御方法，需要与已有的 5+ 种 defense 竞争 (Caution, PET, APRM, gradient regularization, PURE)，在拥挤的 solution space 中脱颖而出的难度很高。

3. **Related Work: 中** — 
   Proposal 对主要 baseline (Caution, PET, APRM, gradient regularization) 的定位是清晰的，并准确描述了它们的局限性。但有一个重要遗漏：2026 年 5 月刚出的 "Distributional Process Reward Models"(arXiv:2605.06785) 直接做 PRM calibration 并在 MATH-500/AIME 上验证，与本 proposal 的方法论高度重叠。此外，PURE (min-form credit assignment) 作为一种完全不同思路的 defense 也应被讨论。"Know What You Don't Know: Uncertainty Calibration of PRMs" 直接研究 PRM uncertainty calibration，也需要被引用和比较。


【概率估计】: [18% - 28%] 中位 22%

【估计理由】: 
三个维度中 Novelty 是最大的限制因素。核心洞察（calibration helps robustness）缺乏 conceptual surprise，CGSP 是已有 pessimism 方法的 straightforward calibration-weighted variant，step-level Hessian 是 Ackermann et al. 的增量扩展。Significance 因研究问题的重要性而不低，但预期 finding 的 surprise level 不足以达到 35%+ 区间。领域竞争异常激烈（6 个月内至少 5 篇高度相关工作），novelty delta 被持续压缩。Proposal 形式上非常完善（48 configurations、causal isolation、4 contributions），但形式完善度不等于 idea 质量。按 rubric，这属于"idea 方向站得住脚但内核薄弱"到"有实质内核但不 surprising"的过渡区间。

另需注意：**如果投稿目标确实是 CoRL (Conference on Robot Learning)，则存在严重的 venue mismatch 问题**——本 proposal 全部内容围绕 LLM 数学推理 (MATH-500, AIME, GRPO)，与 robotics 无任何关联，大概率会因 out-of-scope 被直接拒稿。若投稿目标是 NeurIPS/ICML/ICLR 等 ML 主会，则上述概率估计适用。

【主要风险】: 
1. **Core insight 缺乏 surprise**："Well-calibrated reward model is harder to hack" 在直觉上几乎是 tautological（calibration 意味着 scores 更准确 → 更准确的 scores 自然更难被 exploit）。审稿人可能质疑这一发现的 intellectual contribution 不足以支撑一篇顶会论文。
2. **Solution space 拥挤，增量价值模糊**：CGSP 需要证明相对于"简单 calibrate PRM + 已有 defense (如 Caution)"的组合有显著优势，而 proposal 未将这一 trivial combination 作为 baseline，留下明显的审稿攻击面。
```

Sources:
- [Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models](https://arxiv.org/abs/2603.06621)
- [Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards](https://arxiv.org/abs/2602.18037)
- [From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism](https://arxiv.org/abs/2604.04648)
- [Learning a Pessimistic Reward Model in RLHF (PET)](https://arxiv.org/abs/2505.20556)
- [Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport](https://arxiv.org/abs/2605.06785)
- [Adversarial Training for Process Reward Models (APRM)](https://arxiv.org/abs/2511.22888)
- [Know What You Don't Know: Uncertainty Calibration of Process Reward Models](https://arxiv.org/abs/2506.09338)
- [Stop Summation: Min-Form Credit Assignment (PURE)](https://arxiv.org/abs/2504.15275)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1386f18-d358-4a69-99da-c69c63bb9f0c",
  "isSidechain": false,
  "requestId": "req_011CbD6RSo4zppyDzsWzevxf",
  "type": "assistant",
  "uuid": "c16cd91a-5c1b-4932-b1ab-0414e241b13f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168gBNodrWstSsfB1PDPCCW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 25224,
      "output_tokens": 6277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 700,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6277,
          "cache_read_input_tokens": 25224,
          "cache_creation_input_tokens": 700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 700
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

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-L…",
  "leafUuid": "c16cd91a-5c1b-4932-b1ab-0414e241b13f",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM calibration and reward hacking resistance proposal",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-L…",
  "leafUuid": "c16cd91a-5c1b-4932-b1ab-0414e241b13f",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM calibration and reward hacking resistance proposal",
  "sessionId": "2dce26a4-3106-4876-9f44-6d43353ccdf0"
}
```

---
