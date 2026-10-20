# Research conversation: 任务：plan_004 Step 2 — GSM8K Semi-Synthetic Injection（复制 plan_011 方法） **P0 紧急。** 在 GSM8K response matrix 上验证 DIF 方法论有效性。 #

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/c9888f1d-7b39-4f56-88ab-428b671b99c5.jsonl`
- **Structured JSON:** [`3949948a6232c2572046.json`](../../sessions/39/3949948a6232c2572046.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T00:52:06.407Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T00:52:06.407Z",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "content": "## 任务：plan_004 Step 2 — GSM8K Semi-Synthetic Injection（复制 plan_011 方法）\n\n**P0 紧急。** 在 GSM8K response matrix 上验证 DIF 方法论有效性。\n\n### 背景\n\nStep 1 已完成：GSM8K temporal DIF 确认存在（standard 18.9% C, external 47.4% C）。现在需要验证 DIF 能在 GSM8K 上检测已知注入的差异性污染。\n\n### 参考代码\n\n- plan_011 semi-synthetic: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/` 下的脚本\n- plan_004 Step 1 脚本: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_step1_gsm8k_temporal_dif.py`（已有数据加载和 MH-DIF 函数）\n\n### 数据\n\n- GSM8K responses: `artifacts/metabench_data/benchmark-data/gsm8k.csv`\n- Model metadata: `artifacts/model_metadata.csv`\n- External benchmark data: `artifacts/metabench_data/benchmark-data/` 下的 ARC, HellaSwag, TruthfulQA, Winogrande\n- Step 1 已有的 temporal cohort 划分和 external matching variable\n\n### 实验设计\n\n1. **Cohort**: temporal, ref=2023 (N=1017), foc=2024 (N=804)\n2. **Injection**: 随机选 20% GSM8K items (≈264 items) 作为 contaminated\n3. **Injection probabilities**: p ∈ {0.0, 0.3, 0.5, 0.7, 1.0}\n4. **Seeds**: 5 per p-level\n5. **Injection mechanism**: 对 focal group 中 ability-overlapping models，以概率 p 将 incorrect→correct 翻转\n6. **Matching variants**:\n   - `standard`: GSM8K purified total score（会被 contamination 污染）\n   - `external`: 其他 4 benchmarks 平均分（不受 GSM8K 注入影响）\n7. **Focal injection subset**: 选 focal (2024) 中与 ref (2023) 有 ability overlap 的模型\n\n### 评估指标\n\n- TPR: contaminated items 被标记 ETS C 的比例\n- FPR: clean items 被标记 ETS C 的比例\n- ΔTPR = TPR(p=x) - TPR(p=0)\n- Fisher exact test: contaminated vs clean 的 C-rate 差异\n\n### 关键对比\n\n与 MMLU plan_011 的结果对比：\n\n| Metric | MMLU plan_011 | GSM8K (target) |\n|--------|---------------|----------------|\n| Baseline FPR (external) | 0.314 | ? |\n| ΔTPR at p=0.5 | +0.508 | ? |\n| ΔTPR at p=1.0 | +0.674 | ? |\n\n### 技术注意\n\n- GSM8K 只有 1,319 items，20% = ~264 contaminated items。Power 可能比 MMLU 低\n- External matching 要求模型同时有其他 benchmark 分数 → 取交集\n- 注意 inf delta 处理（classify as extreme DIF, not A）\n- Standard matching 预期 FPR 膨胀（matching variable 包含 injected items），external 应该稳定\n\n### 输出\n\n1. `artifacts/plan_004/plan_004_step2_gsm8k_semi_synthetic.py` — 脚本\n2. `artifacts/plan_004/gsm8k_dose_response.csv` — p × matching_type × seed 结果\n3. `artifacts/plan_004/gsm8k_dose_response_summary.csv` — 按 p × matching_type 汇总\n4. `artifacts/plan_004/plan_004_step2_report.md` — 报告\n\n用 `register_artifact` 注册所有产出。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T00:52:06.411Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T00:52:06.411Z",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5"
}
```

---

## Round 1

46 recorded events

### User

_source line 3 · 2026-05-21T00:52:06.448Z_

## 任务：plan_004 Step 2 — GSM8K Semi-Synthetic Injection（复制 plan_011 方法）

**P0 紧急。** 在 GSM8K response matrix 上验证 DIF 方法论有效性。

### 背景

Step 1 已完成：GSM8K temporal DIF 确认存在（standard 18.9% C, external 47.4% C）。现在需要验证 DIF 能在 GSM8K 上检测已知注入的差异性污染。

### 参考代码

- plan_011 semi-synthetic: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/` 下的脚本
- plan_004 Step 1 脚本: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_step1_gsm8k_temporal_dif.py`（已有数据加载和 MH-DIF 函数）

### 数据

- GSM8K responses: `artifacts/metabench_data/benchmark-data/gsm8k.csv`
- Model metadata: `artifacts/model_metadata.csv`
- External benchmark data: `artifacts/metabench_data/benchmark-data/` 下的 ARC, HellaSwag, TruthfulQA, Winogrande
- Step 1 已有的 temporal cohort 划分和 external matching variable

### 实验设计

1. **Cohort**: temporal, ref=2023 (N=1017), foc=2024 (N=804)
2. **Injection**: 随机选 20% GSM8K items (≈264 items) 作为 contaminated
3. **Injection probabilities**: p ∈ {0.0, 0.3, 0.5, 0.7, 1.0}
4. **Seeds**: 5 per p-level
5. **Injection mechanism**: 对 focal group 中 ability-overlapping models，以概率 p 将 incorrect→correct 翻转
6. **Matching variants**:
   - `standard`: GSM8K purified total score（会被 contamination 污染）
   - `external`: 其他 4 benchmarks 平均分（不受 GSM8K 注入影响）
7. **Focal injection subset**: 选 focal (2024) 中与 ref (2023) 有 ability overlap 的模型

### 评估指标

- TPR: contaminated items 被标记 ETS C 的比例
- FPR: clean items 被标记 ETS C 的比例
- ΔTPR = TPR(p=x) - TPR(p=0)
- Fisher exact test: contaminated vs clean 的 C-rate 差异

### 关键对比

与 MMLU plan_011 的结果对比：

| Metric | MMLU plan_011 | GSM8K (target) |
|--------|---------------|----------------|
| Baseline FPR (external) | 0.314 | ? |
| ΔTPR at p=0.5 | +0.508 | ? |
| ΔTPR at p=1.0 | +0.674 | ? |

### 技术注意

- GSM8K 只有 1,319 items，20% = ~264 contaminated items。Power 可能比 MMLU 低
- External matching 要求模型同时有其他 benchmark 分数 → 取交集
- 注意 inf delta 处理（classify as extreme DIF, not A）
- Standard matching 预期 FPR 膨胀（matching variable 包含 injected items），external 应该稳定

### 输出

1. `artifacts/plan_004/plan_004_step2_gsm8k_semi_synthetic.py` — 脚本
2. `artifacts/plan_004/gsm8k_dose_response.csv` — p × matching_type × seed 结果
3. `artifacts/plan_004/gsm8k_dose_response_summary.csv` — 按 p × matching_type 汇总
4. `artifacts/plan_004/plan_004_step2_report.md` — 报告

用 `register_artifact` 注册所有产出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "b681718f-ed7e-4c71-ace8-cbf70777063c",
  "type": "user",
  "uuid": "44628cf3-229d-4cd4-94de-071d62f9f54c",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T00:52:06.447Z_

```json
{
  "parentUuid": "44628cf3-229d-4cd4-94de-071d62f9f54c",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__update_registry"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "e110c11d-01b1-4c77-8d52-f1c5579b793a",
  "timestamp": "2026-05-21T00:52:06.447Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T00:52:06.447Z_

```json
{
  "parentUuid": "e110c11d-01b1-4c77-8d52-f1c5579b793a",
  "isSidechain": false,
  "attachment": {
    "type": "mcp_instructions_delta",
    "addedNames": [
      "agent-ml-research"
    ],
    "addedBlocks": [
      "## agent-ml-research\nML research experiment management tools"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "45aae80a-cb98-48ba-b514-eef087ca9d0d",
  "timestamp": "2026-05-21T00:52:06.447Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-21T00:52:06.447Z_

```json
{
  "parentUuid": "45aae80a-cb98-48ba-b514-eef087ca9d0d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8c5fa502-6aa9-4d90-93f5-92f152e254f8",
  "timestamp": "2026-05-21T00:52:06.447Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "GSM8K semi-synthetic DIF injection validation",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5"
}
```

---

### Assistant

_source line 8 · 2026-05-21T00:52:09.461Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by understanding the task and reading the reference files to build the semi-synthetic injection script for GSM8K.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c5fa502-6aa9-4d90-93f5-92f152e254f8",
  "isSidechain": false,
  "requestId": "req_011CbEoGpBxsgBFfVdcCZCx9",
  "type": "assistant",
  "uuid": "c057e740-2852-4d7e-98bf-ffab09befcc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01861sM9KDgMz2taRiacvfsY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11778,
      "cache_read_input_tokens": 11841,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11778,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 310,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11778
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

_source line 9 · 2026-05-21T00:52:09.982Z_

Reading reference code and data to understand the existing implementation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c057e740-2852-4d7e-98bf-ffab09befcc5",
  "isSidechain": false,
  "requestId": "req_011CbEoGpBxsgBFfVdcCZCx9",
  "type": "assistant",
  "uuid": "f6f813db-96d7-4c68-a720-9c83d4a0d7b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01861sM9KDgMz2taRiacvfsY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11778,
      "cache_read_input_tokens": 11841,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11778,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 310,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11778
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

_source line 10 · 2026-05-21T00:52:13.173Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01NjHmZxLDByjBvDgWnPML5t`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Explore plan_011 semi-synthetic code",
  "prompt": "Find and read the semi-synthetic injection scripts in /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/. I need to understand:\n1. The full injection mechanism (how contaminated items are selected, how ability-overlapping models are identified, how incorrect→correct flipping works)\n2. The MH-DIF implementation\n3. The dose-response evaluation (TPR, FPR, Fisher exact test)\n4. The matching variable computation (standard vs external)\n5. How results are summarized\n\nRead ALL python files in that directory thoroughly. Return the complete code of the main semi-synthetic script."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6f813db-96d7-4c68-a720-9c83d4a0d7b1",
  "isSidechain": false,
  "requestId": "req_011CbEoGpBxsgBFfVdcCZCx9",
  "type": "assistant",
  "uuid": "9485294a-9b09-4562-8e23-ca034e4631de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01861sM9KDgMz2taRiacvfsY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11778,
      "cache_read_input_tokens": 11841,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11778,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 310,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11778
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

_source line 11 · 2026-05-21T00:53:37.027Z_

<details><summary>↩ Tool result · `toolu_01NjHmZxLDByjBvDgWnPML5t`</summary>

````text
Perfect! I have the complete semi-synthetic injection script. Let me now provide you with a comprehensive analysis of the code:

## Complete Analysis of plan_011_analysis.py

### 1. **Full Injection Mechanism** (Lines 307-330)

The injection process works as follows:

- **Contaminated item selection**: For each seed, `N_CONTAMINATED=100` items are randomly selected from the `N_BASELINE=500` baseline items using `np.random.choice()` without replacement (line 311).
- **Ability-overlapping model identification**: The script identifies focal models that fall within the ability (or temporal) overlap range:
  - For ability cohort: models in Q4-5 (highest accuracy) whose accuracy falls within [min(Q1-2 accuracy), min(Q4-5 accuracy)] (lines 237-242)
  - This ensures contamination is injected into models with similar base abilities as reference models, creating a "differential" contamination scenario
- **Incorrect→Correct flipping** (lines 318-324):
  - For each contaminated item and each focal model to inject into
  - Only flip if current response is 0 (incorrect), with probability `p` (the injection strength)
  - Only incorrect responses can be flipped to correct (never the reverse)
  - Count total flips via `n_flipped`

### 2. **MH-DIF Implementation** (Lines 46-167)

The `mh_dif_subset()` function implements Mantel-Haenszel DIF testing with three matching variable modes:

**Stratification priority**:
1. **External**: Pre-computed ability scores from full 12,508-item matrix (lines 71-73)
2. **Anchor**: Sum of known-clean items only (lines 74-80)
3. **Standard**: Total score minus current item (lines 81-83) - purified approach

**Core MH computation** (lines 101-149):
- Stratifies both reference and focal groups into `n_strata=5` bins based on matching variable (lines 85-93)
- For each stratum k, computes 2×2 contingency table (A, B, C, D) for item j (lines 109-115)
- Accumulates Mantel-Haenszel statistics across strata:
  - R and S: numerator/denominator of alpha (lines 121-124)
  - Variance components for SE calculation (lines 126-134)
- Calculates MH alpha (odds ratio) and delta (log-odds effect size) (lines 145-148)
- Computes chi-square statistic with continuity correction (line 151)

**ETS classification** (lines 156-162):
- Class A: |delta| < 1.0 (negligible)
- Class C: |delta| >= 1.5 AND p-value < 0.05 (significant DIF)
- Class B: everything else (moderate)

### 3. **Dose-Response Evaluation** (Lines 345-370)

For each injection run, the script computes:

**TPR (True Positive Rate)**:
- Number of contaminated items flagged as class C (DIF detected)
- Divided by N_CONTAMINATED (100)
- Formula: `tpr = (contaminated items flagged as C) / 100`

**FPR (False Positive Rate)**:
- Number of clean items flagged as class C
- Divided by N_CLEAN (400)
- Formula: `fpr = (clean items flagged as C) / 400`

**Fisher Exact Test** (lines 356-358):
- Builds contingency table:
  ```
  [[n_c_contam, N_CONTAMINATED - n_c_contam],
   [n_c_clean, (N_BASELINE - N_CONTAMINATED) - n_c_clean]]
  ```
- Tests association between DIF detection (C-class) and contamination status
- Reports OR (odds ratio) and p-value

### 4. **Matching Variable Computation** (Lines 59-83)

**Standard** (purified):
```python
tot_ref = X_ref.sum(axis=1)  # total across all 500 items
tot_foc = X_foc.sum(axis=1)
# For item j: score = total - response[j]
s_ref = tot_ref - X_ref[:, j]
```

**Anchor**:
```python
anchor_cols = clean_local_idx  # the 400 known-clean items
tot_ref = X_ref[:, anchor_cols].sum(axis=1)
tot_foc = X_foc[:, anchor_cols].sum(axis=1)
# score = total of clean items only (never adjusted per-item)
```

**External**:
```python
# Pre-computed from full 12,508-item matrix
ext_ref = full_totals[ref_idx]  # shape: (N_ref,)
ext_foc = full_totals[foc_idx]  # shape: (N_foc,)
# score = pre-injection full-matrix total (immune to any injection)
```

### 5. **Results Summarization** (Lines 400-416)

**Injection results** (one row per condition):
- Groupby: (p, cohort_type, mh_variant)
- Saved to `injection_results.csv` with:
  - Raw counts and rates (TPR, FPR, Fisher stats)
  - Density metrics (orig_density, new_density, n_responses_flipped)

**Dose-response summary** (lines 401-408):
- Aggregated across 5 seeds
- Computed mean/std for TPR and FPR
- Median Fisher p-value (more robust to outliers than mean)

**Per-item results** (lines 372-383):
- Only for anchor variant (to keep CSV manageable)
- Saved to `per_item_results.csv` with:
  - Individual item delta_mh, p_value, ets_class
  - Whether item was in contamination set

---

## Complete Main Script Code

Here is the full, uninterrupted code of the main semi-synthetic analysis script:

```python
#!/usr/bin/env python3
"""
plan_011_analysis.py — Semi-Synthetic DIF Validation

Injects known differential contamination into real MMLU response data and tests
whether MH-DIF can detect it. Validates the DIF methodology used in plan_001.

Three MH variants:
  (1) standard  — total score on 500 items minus current (same as plan_001)
  (2) anchor    — total score on 400 known-clean items only
  (3) external  — total score on full 12508-item original matrix (best matching)

Inputs:
  response_matrix.npz, response_matrix_index.npz, model_metadata.csv,
  item_metadata.csv, mmlu_li2024_proxy_labels.csv,
  plan_001/dif_results_ability.csv

Outputs (all in plan_011/):
  injection_results.csv, dose_response_summary.csv, per_item_results.csv,
  plan_011_report.md
"""

import numpy as np
import pandas as pd
from scipy.sparse import load_npz
from scipy.stats import chi2 as chi2_dist, fisher_exact
from pathlib import Path
import time
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)

BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
OUT = BASE / "plan_011"
OUT.mkdir(exist_ok=True)

INJECTION_PS = [0.0, 0.3, 0.5, 0.7, 1.0]
N_SEEDS = 5
N_BASELINE = 500
N_CONTAMINATED = 100


# ════════════════════════════════════════════════════════════════════════════
#  MH-DIF CORE
# ════════════════════════════════════════════════════════════════════════════
def mh_dif_subset(X_ref, X_foc, n_strata=5, anchor_cols=None,
                  external_scores_ref=None, external_scores_foc=None):
    """
    Purified MH-DIF for all columns.

    Stratification source (in priority order):
      1. external_scores_ref/foc — precomputed ability scores (e.g. full-matrix total)
      2. anchor_cols — total score from specified columns only
      3. None — standard purified (all cols minus current)
    """
    J = X_ref.shape[1]
    use_external = external_scores_ref is not None

    if not use_external:
        if anchor_cols is not None:
            tot_ref = X_ref[:, anchor_cols].sum(axis=1).astype(np.float64)
            tot_foc = X_foc[:, anchor_cols].sum(axis=1).astype(np.float64)
            anchor_set = set(anchor_cols.tolist()) if hasattr(anchor_cols, 'tolist') else set(anchor_cols)
        else:
            tot_ref = X_ref.sum(axis=1).astype(np.float64)
            tot_foc = X_foc.sum(axis=1).astype(np.float64)
            anchor_set = None

    rows = []
    for j in range(J):
        if use_external:
            s_ref = external_scores_ref
            s_foc = external_scores_foc
        elif anchor_set is not None:
            if j in anchor_set:
                s_ref = tot_ref - X_ref[:, j].astype(np.float64)
                s_foc = tot_foc - X_foc[:, j].astype(np.float64)
            else:
                s_ref = tot_ref
                s_foc = tot_foc
        else:
            s_ref = tot_ref - X_ref[:, j].astype(np.float64)
            s_foc = tot_foc - X_foc[:, j].astype(np.float64)

        s_all = np.concatenate([s_ref, s_foc])
        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
        if len(edges) < 2:
            rows.append(_nan_row(j))
            continue
        n_bins = len(edges) - 1

        k_ref = np.digitize(s_ref, edges[1:-1])
        k_foc = np.digitize(s_foc, edges[1:-1])

        R = S = 0.0
        sum_diff = 0.0
        sum_var = 0.0
        pr = ps_qr = qs = 0.0
        n_ok = 0

        for k in range(n_bins):
            mr = (k_ref == k)
            mf = (k_foc == k)
            n1 = int(mr.sum())
            n0 = int(mf.sum())
            if n1 == 0 or n0 == 0:
                continue

            A = float(X_ref[mr, j].sum())
            B = float(n1 - A)
            C = float(X_foc[mf, j].sum())
            D = float(n0 - C)
            Nk = float(n1 + n0)
            m1 = A + C
            m0 = B + D

            if m1 == 0 or m0 == 0 or Nk <= 1:
                continue
            n_ok += 1

            Rk = A * D / Nk
            Sk = B * C / Nk
            R += Rk
            S += Sk

            EA = n1 * m1 / Nk
            sum_diff += A - EA
            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))

            Pk = (A + D) / Nk
            Qk = (B + C) / Nk
            pr += Pk * Rk
            ps_qr += Pk * Sk + Qk * Rk
            qs += Qk * Sk

        if n_ok == 0 or (R == 0 and S == 0):
            rows.append(_nan_row(j))
            continue

        if S == 0:
            alpha, delta, se = np.inf, -np.inf, np.nan
        elif R == 0:
            alpha, delta, se = 0.0, np.inf, np.nan
        else:
            alpha = R / S
            delta = -2.35 * np.log(alpha)
            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)
            se = 2.35 * np.sqrt(v) if v > 0 else np.nan

        if sum_var > 0:
            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var
            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)
        else:
            chi2_stat = pval = np.nan

        ad = abs(delta) if np.isfinite(delta) else np.inf
        if ad < 1.0:
            ets = "A"
        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:
            ets = "C"
        else:
            ets = "B"

        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,
                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets))

    return pd.DataFrame(rows)


def _nan_row(j):
    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,
                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class="A")


# ════════════════════════════════════════════════════════════════════════════
#  DATA LOADING
# ════════════════════════════════════════════════════════════════════════════
print("=== Loading data ===")
mat = load_npz(BASE / "response_matrix.npz")
idx = np.load(BASE / "response_matrix_index.npz", allow_pickle=True)
MODEL_NAMES = idx["model_names"]
ITEM_IDS = idx["item_ids"]
ITEM2COL = {iid: i for i, iid in enumerate(ITEM_IDS)}

model_meta = pd.read_csv(BASE / "model_metadata.csv")
li_labels = pd.read_csv(BASE / "mmlu_li2024_proxy_labels.csv")
ability_dif = pd.read_csv(BASE / "plan_001" / "dif_results_ability.csv")

NAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}
N_MODELS, J_FULL = mat.shape
print(f"  Matrix: {N_MODELS} × {J_FULL}")

# Precompute full-matrix total scores (for external matching)
print("  Computing full-matrix total scores...")
full_totals = np.asarray(mat.sum(axis=1)).ravel().astype(np.float64)  # (5227,)
print(f"  Full total scores: mean={full_totals.mean():.1f}, "
      f"range=[{full_totals.min():.0f}, {full_totals.max():.0f}]")


# ════════════════════════════════════════════════════════════════════════════
#  STEP 1: SELECT BASELINE ITEMS
# ════════════════════════════════════════════════════════════════════════════
print("\n=== Step 1: Selecting baseline items ===")
merged = ability_dif.merge(li_labels[["item_id", "contamination_type"]], on="item_id", how="inner")
baseline_pool = merged[(merged["contamination_type"] == "clean") & (merged["ets_class"] == "A")]
print(f"  Baseline pool (clean + ETS A in ability DIF): {len(baseline_pool)}")

baseline_items = baseline_pool.sample(N_BASELINE, random_state=42)
baseline_item_ids = baseline_items["item_id"].values
baseline_col_indices = np.array([ITEM2COL[iid] for iid in baseline_item_ids])
print(f"  Selected {N_BASELINE} baseline items")


# ════════════════════════════════════════════════════════════════════════════
#  STEP 2: DEFINE COHORTS
# ════════════════════════════════════════════════════════════════════════════
print("\n=== Step 2: Defining cohorts ===")


def get_row_indices(col, values):
    names = model_meta.loc[model_meta[col].isin(values), "model_name"]
    return np.array([NAME2ROW[n] for n in names if n in NAME2ROW])


cohort_defs = {}

# (a) Ability cohort
ref_ability_idx = get_row_indices("cohort_accuracy_quintile", [1, 2])
foc_ability_idx = get_row_indices("cohort_accuracy_quintile", [4, 5])

ref_acc = model_meta.loc[model_meta["cohort_accuracy_quintile"].isin([1, 2]), "accuracy"]
foc_acc = model_meta.loc[model_meta["cohort_accuracy_quintile"].isin([4, 5]), "accuracy"]
ab_overlap_min = max(ref_acc.min(), foc_acc.min())
ab_overlap_max = min(ref_acc.max(), foc_acc.max())

if ab_overlap_min <= ab_overlap_max:
    foc_ab_inject_mask = (
        model_meta["cohort_accuracy_quintile"].isin([4, 5]) &
        (model_meta["accuracy"] >= ab_overlap_min) &
        (model_meta["accuracy"] <= ab_overlap_max)
    )
    foc_ab_inject_idx = np.array([NAME2ROW[n] for n in model_meta.loc[foc_ab_inject_mask, "model_name"] if n in NAME2ROW])
else:
    foc_ab_inject_idx = foc_ability_idx

print(f"  Ability: ref={len(ref_ability_idx)} (Q1-2), foc={len(foc_ability_idx)} (Q4-5)")
print(f"    Accuracy overlap: [{ab_overlap_min:.4f}, {ab_overlap_max:.4f}]"
      f" → {'EMPTY, injecting all focal' if ab_overlap_min > ab_overlap_max else f'{len(foc_ab_inject_idx)} focal models'}")

cohort_defs["ability"] = dict(
    ref_idx=ref_ability_idx, foc_idx=foc_ability_idx,
    foc_inject_idx=foc_ab_inject_idx
)

# (b) Temporal cohort
ref_temporal_idx = get_row_indices("cohort_temporal", ["2023"])
foc_temporal_idx = get_row_indices("cohort_temporal", ["2024"])

ref_t_acc = model_meta.loc[model_meta["cohort_temporal"] == "2023", "accuracy"]
foc_t_acc = model_meta.loc[model_meta["cohort_temporal"] == "2024", "accuracy"]
t_overlap_min = max(ref_t_acc.min(), foc_t_acc.min())
t_overlap_max = min(ref_t_acc.max(), foc_t_acc.max())

foc_t_inject_mask = (
    (model_meta["cohort_temporal"] == "2024") &
    (model_meta["accuracy"] >= t_overlap_min) &
    (model_meta["accuracy"] <= t_overlap_max)
)
foc_t_inject_idx = np.array([NAME2ROW[n] for n in model_meta.loc[foc_t_inject_mask, "model_name"] if n in NAME2ROW])

print(f"  Temporal: ref={len(ref_temporal_idx)} (2023), foc={len(foc_temporal_idx)} (2024)")
print(f"    Accuracy overlap: [{t_overlap_min:.4f}, {t_overlap_max:.4f}]"
      f" → {len(foc_t_inject_idx)} focal models for injection")

cohort_defs["temporal"] = dict(
    ref_idx=ref_temporal_idx, foc_idx=foc_temporal_idx,
    foc_inject_idx=foc_t_inject_idx
)


# ════════════════════════════════════════════════════════════════════════════
#  STEP 3-4: INJECTION + MH-DIF
# ════════════════════════════════════════════════════════════════════════════
print("\n=== Step 3-4: Injection + MH-DIF ===")

X_base = mat[:, baseline_col_indices].toarray().astype(np.int8)
print(f"  Baseline submatrix: {X_base.shape}, density: {X_base.mean():.4f}")

injection_rows = []
per_item_rows = []

MH_VARIANTS = ["standard", "anchor", "external"]

total_runs = len(INJECTION_PS) * N_SEEDS * len(cohort_defs) * len(MH_VARIANTS)
run_count = 0
t_start = time.time()

for cohort_name, cdef in cohort_defs.items():
    ref_idx = cdef["ref_idx"]
    foc_idx = cdef["foc_idx"]
    foc_inject_idx = cdef["foc_inject_idx"]

    # External scores for this cohort (from full original matrix)
    ext_ref = full_totals[ref_idx]
    ext_foc = full_totals[foc_idx]

    for p in INJECTION_PS:
        for seed in range(1, N_SEEDS + 1):
            rng = np.random.RandomState(seed)

            contam_local_idx = rng.choice(N_BASELINE, N_CONTAMINATED, replace=False)
            contam_set = set(contam_local_idx.tolist())
            clean_local_idx = np.array([i for i in range(N_BASELINE) if i not in contam_set])

            X_inj = X_base.copy()
            n_flipped = 0

            if p > 0:
                for local_j in contam_local_idx:
                    for model_row in foc_inject_idx:
                        if X_inj[model_row, local_j] == 0:
                            if rng.random() < p:
                                X_inj[model_row, local_j] = 1
                                n_flipped += 1

            orig_density = X_base[np.ix_(foc_inject_idx, contam_local_idx)].mean()
            new_density = X_inj[np.ix_(foc_inject_idx, contam_local_idx)].mean()

            X_ref = X_inj[ref_idx]
            X_foc = X_inj[foc_idx]

            for variant in MH_VARIANTS:
                run_count += 1

                if variant == "anchor":
                    dif_results = mh_dif_subset(X_ref, X_foc, n_strata=5,
                                                anchor_cols=clean_local_idx)
                elif variant == "external":
                    dif_results = mh_dif_subset(X_ref, X_foc, n_strata=5,
                                                external_scores_ref=ext_ref,
                                                external_scores_foc=ext_foc)
                else:
                    dif_results = mh_dif_subset(X_ref, X_foc, n_strata=5)

                contam_mask = dif_results["col_idx"].isin(contam_set)
                clean_mask = ~contam_mask

                contam_results = dif_results[contam_mask]
                clean_results = dif_results[clean_mask]

                n_c_contam = (contam_results["ets_class"] == "C").sum()
                n_c_clean = (clean_results["ets_class"] == "C").sum()
                tpr = n_c_contam / N_CONTAMINATED
                fpr = n_c_clean / (N_BASELINE - N_CONTAMINATED)

                table = [[n_c_contam, N_CONTAMINATED - n_c_contam],
                         [n_c_clean, (N_BASELINE - N_CONTAMINATED) - n_c_clean]]
                fisher_or, fisher_p = fisher_exact(table)

                injection_rows.append(dict(
                    p=p, seed=seed, cohort_type=cohort_name,
                    mh_variant=variant,
                    n_baseline=N_BASELINE, n_contaminated=N_CONTAMINATED,
                    n_clean=N_BASELINE - N_CONTAMINATED,
                    n_foc_inject=len(foc_inject_idx),
                    tpr=tpr, fpr=fpr,
                    fisher_or=fisher_or, fisher_p=fisher_p,
                    n_responses_flipped=n_flipped,
                    orig_density=orig_density, new_density=new_density,
                ))

                # Per-item results only for anchor variant (keeps CSV manageable)
                if variant == "anchor":
                    for _, row in dif_results.iterrows():
                        local_j = int(row["col_idx"])
                        per_item_rows.append(dict(
                            item_id=baseline_item_ids[local_j],
                            p=p, seed=seed, cohort_type=cohort_name,
                            mh_variant=variant,
                            delta_mh=row["delta_mh"], p_value=row["p_value"],
                            ets_class=row["ets_class"],
                            is_injected=local_j in contam_set,
                        ))

                elapsed = time.time() - t_start
                if variant == "external" or (variant == "standard" and p in [0.0, 1.0]):
                    print(f"  [{run_count}/{total_runs}] {cohort_name} {variant:8s} p={p} seed={seed}: "
                          f"TPR={tpr:.3f} FPR={fpr:.3f} flipped={n_flipped} "
                          f"({elapsed:.0f}s)")


# ════════════════════════════════════════════════════════════════════════════
#  STEP 5-6: AGGREGATE & SAVE
# ════════════════════════════════════════════════════════════════════════════
print("\n=== Step 5: Aggregating results ===")

inj_df = pd.DataFrame(injection_rows)
per_item_df = pd.DataFrame(per_item_rows)

summary_rows = []
for (p_val, cohort, variant), grp in inj_df.groupby(["p", "cohort_type", "mh_variant"]):
    summary_rows.append(dict(
        p=p_val, cohort_type=cohort, mh_variant=variant,
        tpr_mean=grp["tpr"].mean(), tpr_std=grp["tpr"].std(),
        fpr_mean=grp["fpr"].mean(), fpr_std=grp["fpr"].std(),
        fisher_or_mean=grp["fisher_or"].mean(),
        fisher_p_median=grp["fisher_p"].median(),
    ))
summary_df = pd.DataFrame(summary_rows)

inj_df.to_csv(OUT / "injection_results.csv", index=False)
summary_df.to_csv(OUT / "dose_response_summary.csv", index=False)
per_item_df.to_csv(OUT / "per_item_results.csv", index=False)
print(f"  Saved injection_results.csv ({len(inj_df)} rows)")
print(f"  Saved dose_response_summary.csv ({len(summary_df)} rows)")
print(f"  Saved per_item_results.csv ({len(per_item_df)} rows)")


# ════════════════════════════════════════════════════════════════════════════
#  REPORT
# ════════════════════════════════════════════════════════════════════════════
print("\n=== Generating report ===")

L = []
def w(s=""):
    L.append(s)

w("# Plan 011: Semi-Synthetic DIF Validation")
w()
w("## 1. Objective")
w()
w("Inject known **differential** contamination into real MMLU response data and test")
w("whether MH-DIF can detect it. This validates whether plan_001/001b's failure to find")
w("enrichment was due to Li et al. labels being non-differential (global contamination)")
w("rather than a fundamental limitation of MH-DIF.")
w()

w("## 2. Setup")
w()
w(f"- **Baseline items**: {N_BASELINE} (clean in Li et al. + ETS A in plan_001 ability DIF)")
w(f"- **Contaminated per run**: {N_CONTAMINATED} of {N_BASELINE}")
w(f"- **Injection probabilities**: {INJECTION_PS}")
w(f"- **Seeds per p**: {N_SEEDS}")
w()
w("### Cohort definitions")
w()
for cn, cd in cohort_defs.items():
    w(f"- **{cn}**: ref N={len(cd['ref_idx'])}, foc N={len(cd['foc_idx'])}, "
      f"foc inject N={len(cd['foc_inject_idx'])}")
w()

if ab_overlap_min > ab_overlap_max:
    w("> **Note**: Ability quintiles (Q1-2 vs Q4-5) have no accuracy overlap by construction "
      f"(ref max={ref_acc.max():.4f}, foc min={foc_acc.min():.4f}). "
      "All focal models used for injection. MH stratification handles ability matching.")
    w()

w("### MH variants")
w()
w("| Variant | Matching variable | Rationale |")
w("|---------|-------------------|-----------|")
w("| standard | sum of 500 items − current | Same as plan_001; susceptible to matching variable contamination when 20% items injected |")
w("| anchor | sum of 400 known-clean items | Eliminates matching variable contamination; assumes oracle knowledge of clean items |")
w("| external | sum of all 12,508 items (original, pre-injection) | Best matching precision; immune to injection; requires external ability estimate |")
w()

w("## 3. Results by MH Variant")
w()
for variant in MH_VARIANTS:
    w(f"### {variant.capitalize()} MH")
    w()
    w("| Cohort | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |")
    w("|--------|---|----------------|----------------|------|-----------|----------|")
    sub = summary_df[summary_df["mh_variant"] == variant]
    for _, r in sub.sort_values(["cohort_type", "p"]).iterrows():
        # ΔTPR = TPR - baseline TPR at p=0
        base_tpr = sub[(sub["cohort_type"] == r.cohort_type) & (sub["p"] == 0.0)]["tpr_mean"].values
        d_tpr = r.tpr_mean - base_tpr[0] if len(base_tpr) > 0 else 0
        w(f"| {r.cohort_type} | {r.p} | {r.tpr_mean:.3f}±{r.tpr_std:.3f} | "
          f"{r.fpr_mean:.3f}±{r.fpr_std:.3f} | {d_tpr:+.3f} | "
          f"{r.fisher_or_mean:.2f} | {r.fisher_p_median:.4f} |")
    w()

w("## 4. Key Comparison: Baseline FPR by Variant")
w()
w("| Cohort | standard | anchor | external |")
w("|--------|----------|--------|----------|")
for cohort in ["ability", "temporal"]:
    vals = []
    for variant in MH_VARIANTS:
        r = summary_df[(summary_df["p"] == 0.0) & (summary_df["cohort_type"] == cohort) &
                       (summary_df["mh_variant"] == variant)]
        vals.append(f"{r.iloc[0]['fpr_mean']:.3f}" if len(r) > 0 else "—")
    w(f"| {cohort} | {vals[0]} | {vals[1]} | {vals[2]} |")
w()
w("If external FPR ≪ standard FPR, the high baseline rate is from matching precision,")
w("not inherent DIF in the selected items.")
w()

w("## 5. Sanity Checks")
w()
w("### Density change (focal × contaminated items)")
w()
w("| Cohort | p | Orig density | Post density | Responses flipped |")
w("|--------|---|--------------|--------------|-------------------|")
for (p_val, cohort), grp in inj_df[inj_df["mh_variant"] == "standard"].groupby(["p", "cohort_type"]):
    if p_val == 0:
        continue
    w(f"| {cohort} | {p_val} | {grp['orig_density'].mean():.4f} | "
      f"{grp['new_density'].mean():.4f} | {grp['n_responses_flipped'].mean():.0f} |")
w()

w("## 6. Verdict")
w()

for variant in MH_VARIANTS:
    w(f"### {variant.capitalize()} MH")
    w()
    sub = summary_df[summary_df["mh_variant"] == variant]

    for cohort in ["ability", "temporal"]:
        c_sub = sub[sub["cohort_type"] == cohort]
        p0 = c_sub[c_sub["p"] == 0.0]
        p1 = c_sub[c_sub["p"] == 1.0]
        if len(p1) == 0 or len(p0) == 0:
            continue

        fpr0 = p0.iloc[0]["fpr_mean"]
        tpr0 = p0.iloc[0]["tpr_mean"]
        tpr1 = p1.iloc[0]["tpr_mean"]
        fpr1 = p1.iloc[0]["fpr_mean"]
        d_tpr = tpr1 - tpr0

        w(f"**{cohort}**: baseline TPR={tpr0:.3f}/FPR={fpr0:.3f}, "
          f"p=1.0 TPR={tpr1:.3f}/FPR={fpr1:.3f}, ΔTPR={d_tpr:+.3f}")

        if d_tpr > 0.3 and tpr1 > 0.5:
            w(f"→ **SUCCESS**: injection raises TPR by {d_tpr:.3f} with clear dose-response")
        elif d_tpr > 0.1:
            w(f"→ **PARTIAL**: detectable signal (ΔTPR={d_tpr:.3f}) but modest")
        else:
            w(f"→ **FAIL**: ΔTPR={d_tpr:.3f} too small to indicate detection")
        w()

w("## 7. Overall Interpretation")
w()
w("### Does MH-DIF detect differential contamination?")
w()

# Compute key numbers for conclusion
ext_t = summary_df[(summary_df["mh_variant"] == "external") & (summary_df["cohort_type"] == "temporal")]
ext_a = summary_df[(summary_df["mh_variant"] == "external") & (summary_df["cohort_type"] == "ability")]

if len(ext_t) > 0:
    ext_t_p0 = ext_t[ext_t["p"] == 0.0]["tpr_mean"].values[0]
    ext_t_p1 = ext_t[ext_t["p"] == 1.0]["tpr_mean"].values[0]
    ext_t_fpr0 = ext_t[ext_t["p"] == 0.0]["fpr_mean"].values[0]
    ext_t_fpr1 = ext_t[ext_t["p"] == 1.0]["fpr_mean"].values[0]
    w(f"- **Temporal + external matching**: TPR rises {ext_t_p0:.3f} → {ext_t_p1:.3f} "
      f"(ΔTPR=+{ext_t_p1-ext_t_p0:.3f}), FPR {ext_t_fpr0:.3f} → {ext_t_fpr1:.3f}")

if len(ext_a) > 0:
    ext_a_p0 = ext_a[ext_a["p"] == 0.0]["tpr_mean"].values[0]
    ext_a_p1 = ext_a[ext_a["p"] == 1.0]["tpr_mean"].values[0]
    ext_a_fpr0 = ext_a[ext_a["p"] == 0.0]["fpr_mean"].values[0]
    ext_a_fpr1 = ext_a[ext_a["p"] == 1.0]["fpr_mean"].values[0]
    w(f"- **Ability + external matching**: TPR rises {ext_a_p0:.3f} → {ext_a_p1:.3f} "
      f"(ΔTPR=+{ext_a_p1-ext_a_p0:.3f}), FPR {ext_a_fpr0:.3f} → {ext_a_fpr1:.3f}")

w()
w("### Implications for plan_001")
w()
w("If semi-synthetic injection is detectable → plan_001's failure to find enrichment")
w("against Li et al. labels is because Li et al. contamination is **non-differential**")
w("(Common Crawl data available to all models), not because MH-DIF is fundamentally limited.")
w()
w("### Matching variable contamination")
w()
w("When 20% of items are injected, standard MH's matching variable (total score) is")
w("corrupted by injected items, inflating FPR. This is a known limitation when DIF items")
w("constitute a large fraction of the test. In practice, iterative purification (exclude")
w("suspected DIF items from matching) or external ability estimates mitigate this.")
w()

(OUT / "plan_011_report.md").write_text("\n".join(L) + "\n")
print("  Report written.")

# Console summary
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
for variant in MH_VARIANTS:
    print(f"\n--- {variant} MH ---")
    sub = summary_df[summary_df["mh_variant"] == variant]
    for _, r in sub.sort_values(["cohort_type", "p"]).iterrows():
        print(f"  {r.cohort_type:8s} p={r.p}: TPR={r.tpr_mean:.3f}±{r.tpr_std:.3f}  "
              f"FPR={r.fpr_mean:.3f}±{r.fpr_std:.3f}")

total_elapsed = time.time() - t_start
print(f"\nTotal time: {total_elapsed:.0f}s")
print(f"All outputs saved to {OUT}")
```

---

## Key Insights

1. **Contaminated Item Selection**: Randomly samples 100 items per run (seeded), ensuring stochastic replication.

2. **Ability-Overlapping Models**: Uses accuracy ranges to find models in the focal cohort that fall within the reference accuracy range. This ensures that injected contamination affects ability-matched focal models only.

3. **Flipping Mechanism**: Only flips incorrect responses (0 → 1) with probability p per focal model per item. Never flips correct responses back to incorrect.

4. **Three-Variant MH Approach**:
   - **Standard**: Most realistic but vulnerable to matching variable contamination
   - **Anchor**: Oracle-clean validation (20% of items not contaminated)
   - **External**: Immune to all injection effects, measures best-case DIF detection

5. **Dose-Response Design**: By varying p ∈ [0.0, 0.3, 0.5, 0.7, 1.0], the script validates whether MH-DIF shows monotonic increase in TPR with injection strength.

6. **Fisher Exact Test**: Validates that the association between DIF detection (class C) and contamination status is significant, accounting for small-cell counts.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "9485294a-9b09-4562-8e23-ca034e4631de",
  "isSidechain": false,
  "promptId": "b681718f-ed7e-4c71-ace8-cbf70777063c",
  "type": "user",
  "uuid": "06eaa02c-05b3-4983-87ec-c727c9fcf3ea",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Find and read the semi-synthetic injection scripts in /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/. I need to understand:\n1. The full injection mechanism (how contaminated items are selected, how ability-overlapping models are identified, how incorrect→correct flipping works)\n2. The MH-DIF implementation\n3. The dose-response evaluation (TPR, FPR, Fisher exact test)\n4. The matching variable computation (standard vs external)\n5. How results are summarized\n\nRead ALL python files in that directory thoroughly. Return the complete code of the main semi-synthetic script.",
    "agentId": "af14da85843b71e93",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I have the complete semi-synthetic injection script. Let me now provide you with a comprehensive analysis of the code:\n\n## Complete Analysis of plan_011_analysis.py\n\n### 1. **Full Injection Mechanism** (Lines 307-330)\n\nThe injection process works as follows:\n\n- **Contaminated item selection**: For each seed, `N_CONTAMINATED=100` items are randomly selected from the `N_BASELINE=500` baseline items using `np.random.choice()` without replacement (line 311).\n- **Ability-overlapping model identification**: The script identifies focal models that fall within the ability (or temporal) overlap range:\n  - For ability cohort: models in Q4-5 (highest accuracy) whose accuracy falls within [min(Q1-2 accuracy), min(Q4-5 accuracy)] (lines 237-242)\n  - This ensures contamination is injected into models with similar base abilities as reference models, creating a \"differential\" contamination scenario\n- **Incorrect→Correct flipping** (lines 318-324):\n  - For each contaminated item and each focal model to inject into\n  - Only flip if current response is 0 (incorrect), with probability `p` (the injection strength)\n  - Only incorrect responses can be flipped to correct (never the reverse)\n  - Count total flips via `n_flipped`\n\n### 2. **MH-DIF Implementation** (Lines 46-167)\n\nThe `mh_dif_subset()` function implements Mantel-Haenszel DIF testing with three matching variable modes:\n\n**Stratification priority**:\n1. **External**: Pre-computed ability scores from full 12,508-item matrix (lines 71-73)\n2. **Anchor**: Sum of known-clean items only (lines 74-80)\n3. **Standard**: Total score minus current item (lines 81-83) - purified approach\n\n**Core MH computation** (lines 101-149):\n- Stratifies both reference and focal groups into `n_strata=5` bins based on matching variable (lines 85-93)\n- For each stratum k, computes 2×2 contingency table (A, B, C, D) for item j (lines 109-115)\n- Accumulates Mantel-Haenszel statistics across strata:\n  - R and S: numerator/denominator of alpha (lines 121-124)\n  - Variance components for SE calculation (lines 126-134)\n- Calculates MH alpha (odds ratio) and delta (log-odds effect size) (lines 145-148)\n- Computes chi-square statistic with continuity correction (line 151)\n\n**ETS classification** (lines 156-162):\n- Class A: |delta| < 1.0 (negligible)\n- Class C: |delta| >= 1.5 AND p-value < 0.05 (significant DIF)\n- Class B: everything else (moderate)\n\n### 3. **Dose-Response Evaluation** (Lines 345-370)\n\nFor each injection run, the script computes:\n\n**TPR (True Positive Rate)**:\n- Number of contaminated items flagged as class C (DIF detected)\n- Divided by N_CONTAMINATED (100)\n- Formula: `tpr = (contaminated items flagged as C) / 100`\n\n**FPR (False Positive Rate)**:\n- Number of clean items flagged as class C\n- Divided by N_CLEAN (400)\n- Formula: `fpr = (clean items flagged as C) / 400`\n\n**Fisher Exact Test** (lines 356-358):\n- Builds contingency table:\n  ```\n  [[n_c_contam, N_CONTAMINATED - n_c_contam],\n   [n_c_clean, (N_BASELINE - N_CONTAMINATED) - n_c_clean]]\n  ```\n- Tests association between DIF detection (C-class) and contamination status\n- Reports OR (odds ratio) and p-value\n\n### 4. **Matching Variable Computation** (Lines 59-83)\n\n**Standard** (purified):\n```python\ntot_ref = X_ref.sum(axis=1)  # total across all 500 items\ntot_foc = X_foc.sum(axis=1)\n# For item j: score = total - response[j]\ns_ref = tot_ref - X_ref[:, j]\n```\n\n**Anchor**:\n```python\nanchor_cols = clean_local_idx  # the 400 known-clean items\ntot_ref = X_ref[:, anchor_cols].sum(axis=1)\ntot_foc = X_foc[:, anchor_cols].sum(axis=1)\n# score = total of clean items only (never adjusted per-item)\n```\n\n**External**:\n```python\n# Pre-computed from full 12,508-item matrix\next_ref = full_totals[ref_idx]  # shape: (N_ref,)\next_foc = full_totals[foc_idx]  # shape: (N_foc,)\n# score = pre-injection full-matrix total (immune to any injection)\n```\n\n### 5. **Results Summarization** (Lines 400-416)\n\n**Injection results** (one row per condition):\n- Groupby: (p, cohort_type, mh_variant)\n- Saved to `injection_results.csv` with:\n  - Raw counts and rates (TPR, FPR, Fisher stats)\n  - Density metrics (orig_density, new_density, n_responses_flipped)\n\n**Dose-response summary** (lines 401-408):\n- Aggregated across 5 seeds\n- Computed mean/std for TPR and FPR\n- Median Fisher p-value (more robust to outliers than mean)\n\n**Per-item results** (lines 372-383):\n- Only for anchor variant (to keep CSV manageable)\n- Saved to `per_item_results.csv` with:\n  - Individual item delta_mh, p_value, ets_class\n  - Whether item was in contamination set\n\n---\n\n## Complete Main Script Code\n\nHere is the full, uninterrupted code of the main semi-synthetic analysis script:\n\n```python\n#!/usr/bin/env python3\n\"\"\"\nplan_011_analysis.py — Semi-Synthetic DIF Validation\n\nInjects known differential contamination into real MMLU response data and tests\nwhether MH-DIF can detect it. Validates the DIF methodology used in plan_001.\n\nThree MH variants:\n  (1) standard  — total score on 500 items minus current (same as plan_001)\n  (2) anchor    — total score on 400 known-clean items only\n  (3) external  — total score on full 12508-item original matrix (best matching)\n\nInputs:\n  response_matrix.npz, response_matrix_index.npz, model_metadata.csv,\n  item_metadata.csv, mmlu_li2024_proxy_labels.csv,\n  plan_001/dif_results_ability.csv\n\nOutputs (all in plan_011/):\n  injection_results.csv, dose_response_summary.csv, per_item_results.csv,\n  plan_011_report.md\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.sparse import load_npz\nfrom scipy.stats import chi2 as chi2_dist, fisher_exact\nfrom pathlib import Path\nimport time\nimport warnings\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\")\nOUT = BASE / \"plan_011\"\nOUT.mkdir(exist_ok=True)\n\nINJECTION_PS = [0.0, 0.3, 0.5, 0.7, 1.0]\nN_SEEDS = 5\nN_BASELINE = 500\nN_CONTAMINATED = 100\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MH-DIF CORE\n# ════════════════════════════════════════════════════════════════════════════\ndef mh_dif_subset(X_ref, X_foc, n_strata=5, anchor_cols=None,\n                  external_scores_ref=None, external_scores_foc=None):\n    \"\"\"\n    Purified MH-DIF for all columns.\n\n    Stratification source (in priority order):\n      1. external_scores_ref/foc — precomputed ability scores (e.g. full-matrix total)\n      2. anchor_cols — total score from specified columns only\n      3. None — standard purified (all cols minus current)\n    \"\"\"\n    J = X_ref.shape[1]\n    use_external = external_scores_ref is not None\n\n    if not use_external:\n        if anchor_cols is not None:\n            tot_ref = X_ref[:, anchor_cols].sum(axis=1).astype(np.float64)\n            tot_foc = X_foc[:, anchor_cols].sum(axis=1).astype(np.float64)\n            anchor_set = set(anchor_cols.tolist()) if hasattr(anchor_cols, 'tolist') else set(anchor_cols)\n        else:\n            tot_ref = X_ref.sum(axis=1).astype(np.float64)\n            tot_foc = X_foc.sum(axis=1).astype(np.float64)\n            anchor_set = None\n\n    rows = []\n    for j in range(J):\n        if use_external:\n            s_ref = external_scores_ref\n            s_foc = external_scores_foc\n        elif anchor_set is not None:\n            if j in anchor_set:\n                s_ref = tot_ref - X_ref[:, j].astype(np.float64)\n                s_foc = tot_foc - X_foc[:, j].astype(np.float64)\n            else:\n                s_ref = tot_ref\n                s_foc = tot_foc\n        else:\n            s_ref = tot_ref - X_ref[:, j].astype(np.float64)\n            s_foc = tot_foc - X_foc[:, j].astype(np.float64)\n\n        s_all = np.concatenate([s_ref, s_foc])\n        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n        if len(edges) < 2:\n            rows.append(_nan_row(j))\n            continue\n        n_bins = len(edges) - 1\n\n        k_ref = np.digitize(s_ref, edges[1:-1])\n        k_foc = np.digitize(s_foc, edges[1:-1])\n\n        R = S = 0.0\n        sum_diff = 0.0\n        sum_var = 0.0\n        pr = ps_qr = qs = 0.0\n        n_ok = 0\n\n        for k in range(n_bins):\n            mr = (k_ref == k)\n            mf = (k_foc == k)\n            n1 = int(mr.sum())\n            n0 = int(mf.sum())\n            if n1 == 0 or n0 == 0:\n                continue\n\n            A = float(X_ref[mr, j].sum())\n            B = float(n1 - A)\n            C = float(X_foc[mf, j].sum())\n            D = float(n0 - C)\n            Nk = float(n1 + n0)\n            m1 = A + C\n            m0 = B + D\n\n            if m1 == 0 or m0 == 0 or Nk <= 1:\n                continue\n            n_ok += 1\n\n            Rk = A * D / Nk\n            Sk = B * C / Nk\n            R += Rk\n            S += Sk\n\n            EA = n1 * m1 / Nk\n            sum_diff += A - EA\n            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n            Pk = (A + D) / Nk\n            Qk = (B + C) / Nk\n            pr += Pk * Rk\n            ps_qr += Pk * Sk + Qk * Rk\n            qs += Qk * Sk\n\n        if n_ok == 0 or (R == 0 and S == 0):\n            rows.append(_nan_row(j))\n            continue\n\n        if S == 0:\n            alpha, delta, se = np.inf, -np.inf, np.nan\n        elif R == 0:\n            alpha, delta, se = 0.0, np.inf, np.nan\n        else:\n            alpha = R / S\n            delta = -2.35 * np.log(alpha)\n            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)\n            se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n        if sum_var > 0:\n            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n        else:\n            chi2_stat = pval = np.nan\n\n        ad = abs(delta) if np.isfinite(delta) else np.inf\n        if ad < 1.0:\n            ets = \"A\"\n        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n            ets = \"C\"\n        else:\n            ets = \"B\"\n\n        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,\n                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets))\n\n    return pd.DataFrame(rows)\n\n\ndef _nan_row(j):\n    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,\n                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class=\"A\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  DATA LOADING\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"=== Loading data ===\")\nmat = load_npz(BASE / \"response_matrix.npz\")\nidx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\nMODEL_NAMES = idx[\"model_names\"]\nITEM_IDS = idx[\"item_ids\"]\nITEM2COL = {iid: i for i, iid in enumerate(ITEM_IDS)}\n\nmodel_meta = pd.read_csv(BASE / \"model_metadata.csv\")\nli_labels = pd.read_csv(BASE / \"mmlu_li2024_proxy_labels.csv\")\nability_dif = pd.read_csv(BASE / \"plan_001\" / \"dif_results_ability.csv\")\n\nNAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}\nN_MODELS, J_FULL = mat.shape\nprint(f\"  Matrix: {N_MODELS} × {J_FULL}\")\n\n# Precompute full-matrix total scores (for external matching)\nprint(\"  Computing full-matrix total scores...\")\nfull_totals = np.asarray(mat.sum(axis=1)).ravel().astype(np.float64)  # (5227,)\nprint(f\"  Full total scores: mean={full_totals.mean():.1f}, \"\n      f\"range=[{full_totals.min():.0f}, {full_totals.max():.0f}]\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 1: SELECT BASELINE ITEMS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 1: Selecting baseline items ===\")\nmerged = ability_dif.merge(li_labels[[\"item_id\", \"contamination_type\"]], on=\"item_id\", how=\"inner\")\nbaseline_pool = merged[(merged[\"contamination_type\"] == \"clean\") & (merged[\"ets_class\"] == \"A\")]\nprint(f\"  Baseline pool (clean + ETS A in ability DIF): {len(baseline_pool)}\")\n\nbaseline_items = baseline_pool.sample(N_BASELINE, random_state=42)\nbaseline_item_ids = baseline_items[\"item_id\"].values\nbaseline_col_indices = np.array([ITEM2COL[iid] for iid in baseline_item_ids])\nprint(f\"  Selected {N_BASELINE} baseline items\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 2: DEFINE COHORTS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 2: Defining cohorts ===\")\n\n\ndef get_row_indices(col, values):\n    names = model_meta.loc[model_meta[col].isin(values), \"model_name\"]\n    return np.array([NAME2ROW[n] for n in names if n in NAME2ROW])\n\n\ncohort_defs = {}\n\n# (a) Ability cohort\nref_ability_idx = get_row_indices(\"cohort_accuracy_quintile\", [1, 2])\nfoc_ability_idx = get_row_indices(\"cohort_accuracy_quintile\", [4, 5])\n\nref_acc = model_meta.loc[model_meta[\"cohort_accuracy_quintile\"].isin([1, 2]), \"accuracy\"]\nfoc_acc = model_meta.loc[model_meta[\"cohort_accuracy_quintile\"].isin([4, 5]), \"accuracy\"]\nab_overlap_min = max(ref_acc.min(), foc_acc.min())\nab_overlap_max = min(ref_acc.max(), foc_acc.max())\n\nif ab_overlap_min <= ab_overlap_max:\n    foc_ab_inject_mask = (\n        model_meta[\"cohort_accuracy_quintile\"].isin([4, 5]) &\n        (model_meta[\"accuracy\"] >= ab_overlap_min) &\n        (model_meta[\"accuracy\"] <= ab_overlap_max)\n    )\n    foc_ab_inject_idx = np.array([NAME2ROW[n] for n in model_meta.loc[foc_ab_inject_mask, \"model_name\"] if n in NAME2ROW])\nelse:\n    foc_ab_inject_idx = foc_ability_idx\n\nprint(f\"  Ability: ref={len(ref_ability_idx)} (Q1-2), foc={len(foc_ability_idx)} (Q4-5)\")\nprint(f\"    Accuracy overlap: [{ab_overlap_min:.4f}, {ab_overlap_max:.4f}]\"\n      f\" → {'EMPTY, injecting all focal' if ab_overlap_min > ab_overlap_max else f'{len(foc_ab_inject_idx)} focal models'}\")\n\ncohort_defs[\"ability\"] = dict(\n    ref_idx=ref_ability_idx, foc_idx=foc_ability_idx,\n    foc_inject_idx=foc_ab_inject_idx\n)\n\n# (b) Temporal cohort\nref_temporal_idx = get_row_indices(\"cohort_temporal\", [\"2023\"])\nfoc_temporal_idx = get_row_indices(\"cohort_temporal\", [\"2024\"])\n\nref_t_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"accuracy\"]\nfoc_t_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2024\", \"accuracy\"]\nt_overlap_min = max(ref_t_acc.min(), foc_t_acc.min())\nt_overlap_max = min(ref_t_acc.max(), foc_t_acc.max())\n\nfoc_t_inject_mask = (\n    (model_meta[\"cohort_temporal\"] == \"2024\") &\n    (model_meta[\"accuracy\"] >= t_overlap_min) &\n    (model_meta[\"accuracy\"] <= t_overlap_max)\n)\nfoc_t_inject_idx = np.array([NAME2ROW[n] for n in model_meta.loc[foc_t_inject_mask, \"model_name\"] if n in NAME2ROW])\n\nprint(f\"  Temporal: ref={len(ref_temporal_idx)} (2023), foc={len(foc_temporal_idx)} (2024)\")\nprint(f\"    Accuracy overlap: [{t_overlap_min:.4f}, {t_overlap_max:.4f}]\"\n      f\" → {len(foc_t_inject_idx)} focal models for injection\")\n\ncohort_defs[\"temporal\"] = dict(\n    ref_idx=ref_temporal_idx, foc_idx=foc_temporal_idx,\n    foc_inject_idx=foc_t_inject_idx\n)\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 3-4: INJECTION + MH-DIF\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 3-4: Injection + MH-DIF ===\")\n\nX_base = mat[:, baseline_col_indices].toarray().astype(np.int8)\nprint(f\"  Baseline submatrix: {X_base.shape}, density: {X_base.mean():.4f}\")\n\ninjection_rows = []\nper_item_rows = []\n\nMH_VARIANTS = [\"standard\", \"anchor\", \"external\"]\n\ntotal_runs = len(INJECTION_PS) * N_SEEDS * len(cohort_defs) * len(MH_VARIANTS)\nrun_count = 0\nt_start = time.time()\n\nfor cohort_name, cdef in cohort_defs.items():\n    ref_idx = cdef[\"ref_idx\"]\n    foc_idx = cdef[\"foc_idx\"]\n    foc_inject_idx = cdef[\"foc_inject_idx\"]\n\n    # External scores for this cohort (from full original matrix)\n    ext_ref = full_totals[ref_idx]\n    ext_foc = full_totals[foc_idx]\n\n    for p in INJECTION_PS:\n        for seed in range(1, N_SEEDS + 1):\n            rng = np.random.RandomState(seed)\n\n            contam_local_idx = rng.choice(N_BASELINE, N_CONTAMINATED, replace=False)\n            contam_set = set(contam_local_idx.tolist())\n            clean_local_idx = np.array([i for i in range(N_BASELINE) if i not in contam_set])\n\n            X_inj = X_base.copy()\n            n_flipped = 0\n\n            if p > 0:\n                for local_j in contam_local_idx:\n                    for model_row in foc_inject_idx:\n                        if X_inj[model_row, local_j] == 0:\n                            if rng.random() < p:\n                                X_inj[model_row, local_j] = 1\n                                n_flipped += 1\n\n            orig_density = X_base[np.ix_(foc_inject_idx, contam_local_idx)].mean()\n            new_density = X_inj[np.ix_(foc_inject_idx, contam_local_idx)].mean()\n\n            X_ref = X_inj[ref_idx]\n            X_foc = X_inj[foc_idx]\n\n            for variant in MH_VARIANTS:\n                run_count += 1\n\n                if variant == \"anchor\":\n                    dif_results = mh_dif_subset(X_ref, X_foc, n_strata=5,\n                                                anchor_cols=clean_local_idx)\n                elif variant == \"external\":\n                    dif_results = mh_dif_subset(X_ref, X_foc, n_strata=5,\n                                                external_scores_ref=ext_ref,\n                                                external_scores_foc=ext_foc)\n                else:\n                    dif_results = mh_dif_subset(X_ref, X_foc, n_strata=5)\n\n                contam_mask = dif_results[\"col_idx\"].isin(contam_set)\n                clean_mask = ~contam_mask\n\n                contam_results = dif_results[contam_mask]\n                clean_results = dif_results[clean_mask]\n\n                n_c_contam = (contam_results[\"ets_class\"] == \"C\").sum()\n                n_c_clean = (clean_results[\"ets_class\"] == \"C\").sum()\n                tpr = n_c_contam / N_CONTAMINATED\n                fpr = n_c_clean / (N_BASELINE - N_CONTAMINATED)\n\n                table = [[n_c_contam, N_CONTAMINATED - n_c_contam],\n                         [n_c_clean, (N_BASELINE - N_CONTAMINATED) - n_c_clean]]\n                fisher_or, fisher_p = fisher_exact(table)\n\n                injection_rows.append(dict(\n                    p=p, seed=seed, cohort_type=cohort_name,\n                    mh_variant=variant,\n                    n_baseline=N_BASELINE, n_contaminated=N_CONTAMINATED,\n                    n_clean=N_BASELINE - N_CONTAMINATED,\n                    n_foc_inject=len(foc_inject_idx),\n                    tpr=tpr, fpr=fpr,\n                    fisher_or=fisher_or, fisher_p=fisher_p,\n                    n_responses_flipped=n_flipped,\n                    orig_density=orig_density, new_density=new_density,\n                ))\n\n                # Per-item results only for anchor variant (keeps CSV manageable)\n                if variant == \"anchor\":\n                    for _, row in dif_results.iterrows():\n                        local_j = int(row[\"col_idx\"])\n                        per_item_rows.append(dict(\n                            item_id=baseline_item_ids[local_j],\n                            p=p, seed=seed, cohort_type=cohort_name,\n                            mh_variant=variant,\n                            delta_mh=row[\"delta_mh\"], p_value=row[\"p_value\"],\n                            ets_class=row[\"ets_class\"],\n                            is_injected=local_j in contam_set,\n                        ))\n\n                elapsed = time.time() - t_start\n                if variant == \"external\" or (variant == \"standard\" and p in [0.0, 1.0]):\n                    print(f\"  [{run_count}/{total_runs}] {cohort_name} {variant:8s} p={p} seed={seed}: \"\n                          f\"TPR={tpr:.3f} FPR={fpr:.3f} flipped={n_flipped} \"\n                          f\"({elapsed:.0f}s)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 5-6: AGGREGATE & SAVE\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 5: Aggregating results ===\")\n\ninj_df = pd.DataFrame(injection_rows)\nper_item_df = pd.DataFrame(per_item_rows)\n\nsummary_rows = []\nfor (p_val, cohort, variant), grp in inj_df.groupby([\"p\", \"cohort_type\", \"mh_variant\"]):\n    summary_rows.append(dict(\n        p=p_val, cohort_type=cohort, mh_variant=variant,\n        tpr_mean=grp[\"tpr\"].mean(), tpr_std=grp[\"tpr\"].std(),\n        fpr_mean=grp[\"fpr\"].mean(), fpr_std=grp[\"fpr\"].std(),\n        fisher_or_mean=grp[\"fisher_or\"].mean(),\n        fisher_p_median=grp[\"fisher_p\"].median(),\n    ))\nsummary_df = pd.DataFrame(summary_rows)\n\ninj_df.to_csv(OUT / \"injection_results.csv\", index=False)\nsummary_df.to_csv(OUT / \"dose_response_summary.csv\", index=False)\nper_item_df.to_csv(OUT / \"per_item_results.csv\", index=False)\nprint(f\"  Saved injection_results.csv ({len(inj_df)} rows)\")\nprint(f\"  Saved dose_response_summary.csv ({len(summary_df)} rows)\")\nprint(f\"  Saved per_item_results.csv ({len(per_item_df)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  REPORT\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Generating report ===\")\n\nL = []\ndef w(s=\"\"):\n    L.append(s)\n\nw(\"# Plan 011: Semi-Synthetic DIF Validation\")\nw()\nw(\"## 1. Objective\")\nw()\nw(\"Inject known **differential** contamination into real MMLU response data and test\")\nw(\"whether MH-DIF can detect it. This validates whether plan_001/001b's failure to find\")\nw(\"enrichment was due to Li et al. labels being non-differential (global contamination)\")\nw(\"rather than a fundamental limitation of MH-DIF.\")\nw()\n\nw(\"## 2. Setup\")\nw()\nw(f\"- **Baseline items**: {N_BASELINE} (clean in Li et al. + ETS A in plan_001 ability DIF)\")\nw(f\"- **Contaminated per run**: {N_CONTAMINATED} of {N_BASELINE}\")\nw(f\"- **Injection probabilities**: {INJECTION_PS}\")\nw(f\"- **Seeds per p**: {N_SEEDS}\")\nw()\nw(\"### Cohort definitions\")\nw()\nfor cn, cd in cohort_defs.items():\n    w(f\"- **{cn}**: ref N={len(cd['ref_idx'])}, foc N={len(cd['foc_idx'])}, \"\n      f\"foc inject N={len(cd['foc_inject_idx'])}\")\nw()\n\nif ab_overlap_min > ab_overlap_max:\n    w(\"> **Note**: Ability quintiles (Q1-2 vs Q4-5) have no accuracy overlap by construction \"\n      f\"(ref max={ref_acc.max():.4f}, foc min={foc_acc.min():.4f}). \"\n      \"All focal models used for injection. MH stratification handles ability matching.\")\n    w()\n\nw(\"### MH variants\")\nw()\nw(\"| Variant | Matching variable | Rationale |\")\nw(\"|---------|-------------------|-----------|\")\nw(\"| standard | sum of 500 items − current | Same as plan_001; susceptible to matching variable contamination when 20% items injected |\")\nw(\"| anchor | sum of 400 known-clean items | Eliminates matching variable contamination; assumes oracle knowledge of clean items |\")\nw(\"| external | sum of all 12,508 items (original, pre-injection) | Best matching precision; immune to injection; requires external ability estimate |\")\nw()\n\nw(\"## 3. Results by MH Variant\")\nw()\nfor variant in MH_VARIANTS:\n    w(f\"### {variant.capitalize()} MH\")\n    w()\n    w(\"| Cohort | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |\")\n    w(\"|--------|---|----------------|----------------|------|-----------|----------|\")\n    sub = summary_df[summary_df[\"mh_variant\"] == variant]\n    for _, r in sub.sort_values([\"cohort_type\", \"p\"]).iterrows():\n        # ΔTPR = TPR - baseline TPR at p=0\n        base_tpr = sub[(sub[\"cohort_type\"] == r.cohort_type) & (sub[\"p\"] == 0.0)][\"tpr_mean\"].values\n        d_tpr = r.tpr_mean - base_tpr[0] if len(base_tpr) > 0 else 0\n        w(f\"| {r.cohort_type} | {r.p} | {r.tpr_mean:.3f}±{r.tpr_std:.3f} | \"\n          f\"{r.fpr_mean:.3f}±{r.fpr_std:.3f} | {d_tpr:+.3f} | \"\n          f\"{r.fisher_or_mean:.2f} | {r.fisher_p_median:.4f} |\")\n    w()\n\nw(\"## 4. Key Comparison: Baseline FPR by Variant\")\nw()\nw(\"| Cohort | standard | anchor | external |\")\nw(\"|--------|----------|--------|----------|\")\nfor cohort in [\"ability\", \"temporal\"]:\n    vals = []\n    for variant in MH_VARIANTS:\n        r = summary_df[(summary_df[\"p\"] == 0.0) & (summary_df[\"cohort_type\"] == cohort) &\n                       (summary_df[\"mh_variant\"] == variant)]\n        vals.append(f\"{r.iloc[0]['fpr_mean']:.3f}\" if len(r) > 0 else \"—\")\n    w(f\"| {cohort} | {vals[0]} | {vals[1]} | {vals[2]} |\")\nw()\nw(\"If external FPR ≪ standard FPR, the high baseline rate is from matching precision,\")\nw(\"not inherent DIF in the selected items.\")\nw()\n\nw(\"## 5. Sanity Checks\")\nw()\nw(\"### Density change (focal × contaminated items)\")\nw()\nw(\"| Cohort | p | Orig density | Post density | Responses flipped |\")\nw(\"|--------|---|--------------|--------------|-------------------|\")\nfor (p_val, cohort), grp in inj_df[inj_df[\"mh_variant\"] == \"standard\"].groupby([\"p\", \"cohort_type\"]):\n    if p_val == 0:\n        continue\n    w(f\"| {cohort} | {p_val} | {grp['orig_density'].mean():.4f} | \"\n      f\"{grp['new_density'].mean():.4f} | {grp['n_responses_flipped'].mean():.0f} |\")\nw()\n\nw(\"## 6. Verdict\")\nw()\n\nfor variant in MH_VARIANTS:\n    w(f\"### {variant.capitalize()} MH\")\n    w()\n    sub = summary_df[summary_df[\"mh_variant\"] == variant]\n\n    for cohort in [\"ability\", \"temporal\"]:\n        c_sub = sub[sub[\"cohort_type\"] == cohort]\n        p0 = c_sub[c_sub[\"p\"] == 0.0]\n        p1 = c_sub[c_sub[\"p\"] == 1.0]\n        if len(p1) == 0 or len(p0) == 0:\n            continue\n\n        fpr0 = p0.iloc[0][\"fpr_mean\"]\n        tpr0 = p0.iloc[0][\"tpr_mean\"]\n        tpr1 = p1.iloc[0][\"tpr_mean\"]\n        fpr1 = p1.iloc[0][\"fpr_mean\"]\n        d_tpr = tpr1 - tpr0\n\n        w(f\"**{cohort}**: baseline TPR={tpr0:.3f}/FPR={fpr0:.3f}, \"\n          f\"p=1.0 TPR={tpr1:.3f}/FPR={fpr1:.3f}, ΔTPR={d_tpr:+.3f}\")\n\n        if d_tpr > 0.3 and tpr1 > 0.5:\n            w(f\"→ **SUCCESS**: injection raises TPR by {d_tpr:.3f} with clear dose-response\")\n        elif d_tpr > 0.1:\n            w(f\"→ **PARTIAL**: detectable signal (ΔTPR={d_tpr:.3f}) but modest\")\n        else:\n            w(f\"→ **FAIL**: ΔTPR={d_tpr:.3f} too small to indicate detection\")\n        w()\n\nw(\"## 7. Overall Interpretation\")\nw()\nw(\"### Does MH-DIF detect differential contamination?\")\nw()\n\n# Compute key numbers for conclusion\next_t = summary_df[(summary_df[\"mh_variant\"] == \"external\") & (summary_df[\"cohort_type\"] == \"temporal\")]\next_a = summary_df[(summary_df[\"mh_variant\"] == \"external\") & (summary_df[\"cohort_type\"] == \"ability\")]\n\nif len(ext_t) > 0:\n    ext_t_p0 = ext_t[ext_t[\"p\"] == 0.0][\"tpr_mean\"].values[0]\n    ext_t_p1 = ext_t[ext_t[\"p\"] == 1.0][\"tpr_mean\"].values[0]\n    ext_t_fpr0 = ext_t[ext_t[\"p\"] == 0.0][\"fpr_mean\"].values[0]\n    ext_t_fpr1 = ext_t[ext_t[\"p\"] == 1.0][\"fpr_mean\"].values[0]\n    w(f\"- **Temporal + external matching**: TPR rises {ext_t_p0:.3f} → {ext_t_p1:.3f} \"\n      f\"(ΔTPR=+{ext_t_p1-ext_t_p0:.3f}), FPR {ext_t_fpr0:.3f} → {ext_t_fpr1:.3f}\")\n\nif len(ext_a) > 0:\n    ext_a_p0 = ext_a[ext_a[\"p\"] == 0.0][\"tpr_mean\"].values[0]\n    ext_a_p1 = ext_a[ext_a[\"p\"] == 1.0][\"tpr_mean\"].values[0]\n    ext_a_fpr0 = ext_a[ext_a[\"p\"] == 0.0][\"fpr_mean\"].values[0]\n    ext_a_fpr1 = ext_a[ext_a[\"p\"] == 1.0][\"fpr_mean\"].values[0]\n    w(f\"- **Ability + external matching**: TPR rises {ext_a_p0:.3f} → {ext_a_p1:.3f} \"\n      f\"(ΔTPR=+{ext_a_p1-ext_a_p0:.3f}), FPR {ext_a_fpr0:.3f} → {ext_a_fpr1:.3f}\")\n\nw()\nw(\"### Implications for plan_001\")\nw()\nw(\"If semi-synthetic injection is detectable → plan_001's failure to find enrichment\")\nw(\"against Li et al. labels is because Li et al. contamination is **non-differential**\")\nw(\"(Common Crawl data available to all models), not because MH-DIF is fundamentally limited.\")\nw()\nw(\"### Matching variable contamination\")\nw()\nw(\"When 20% of items are injected, standard MH's matching variable (total score) is\")\nw(\"corrupted by injected items, inflating FPR. This is a known limitation when DIF items\")\nw(\"constitute a large fraction of the test. In practice, iterative purification (exclude\")\nw(\"suspected DIF items from matching) or external ability estimates mitigate this.\")\nw()\n\n(OUT / \"plan_011_report.md\").write_text(\"\\n\".join(L) + \"\\n\")\nprint(\"  Report written.\")\n\n# Console summary\nprint(\"\\n\" + \"=\" * 60)\nprint(\"SUMMARY\")\nprint(\"=\" * 60)\nfor variant in MH_VARIANTS:\n    print(f\"\\n--- {variant} MH ---\")\n    sub = summary_df[summary_df[\"mh_variant\"] == variant]\n    for _, r in sub.sort_values([\"cohort_type\", \"p\"]).iterrows():\n        print(f\"  {r.cohort_type:8s} p={r.p}: TPR={r.tpr_mean:.3f}±{r.tpr_std:.3f}  \"\n              f\"FPR={r.fpr_mean:.3f}±{r.fpr_std:.3f}\")\n\ntotal_elapsed = time.time() - t_start\nprint(f\"\\nTotal time: {total_elapsed:.0f}s\")\nprint(f\"All outputs saved to {OUT}\")\n```\n\n---\n\n## Key Insights\n\n1. **Contaminated Item Selection**: Randomly samples 100 items per run (seeded), ensuring stochastic replication.\n\n2. **Ability-Overlapping Models**: Uses accuracy ranges to find models in the focal cohort that fall within the reference accuracy range. This ensures that injected contamination affects ability-matched focal models only.\n\n3. **Flipping Mechanism**: Only flips incorrect responses (0 → 1) with probability p per focal model per item. Never flips correct responses back to incorrect.\n\n4. **Three-Variant MH Approach**:\n   - **Standard**: Most realistic but vulnerable to matching variable contamination\n   - **Anchor**: Oracle-clean validation (20% of items not contaminated)\n   - **External**: Immune to all injection effects, measures best-case DIF detection\n\n5. **Dose-Response Design**: By varying p ∈ [0.0, 0.3, 0.5, 0.7, 1.0], the script validates whether MH-DIF shows monotonic increase in TPR with injection strength.\n\n6. **Fisher Exact Test**: Validates that the association between DIF detection (class C) and contamination status is significant, accounting for small-cell counts."
      }
    ],
    "totalDurationMs": 83847,
    "totalTokens": 41623,
    "totalToolUseCount": 3,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 10278,
      "cache_read_input_tokens": 20701,
      "output_tokens": 10639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10278
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 10639,
          "cache_read_input_tokens": 20701,
          "cache_creation_input_tokens": 10278,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10278,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 0,
      "bashCount": 2,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "9485294a-9b09-4562-8e23-ca034e4631de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## 任务：plan_004 Step 2 — GSM8K Semi-Synthetic Injection（复制 plan_011 方法）  **P0 紧急。** 在 GSM8K response matrix 上验证 DIF 方法论有效性。  ### 背景  Step 1 已完成：GSM8K temporal DIF 确认存在（standard 18.9% C, external 47.4%…",
  "leafUuid": "06eaa02c-05b3-4983-87ec-c727c9fcf3ea",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "GSM8K semi-synthetic DIF injection validation",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5"
}
```

---

### Tool call

_source line 14 · 2026-05-21T00:53:41.646Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RM6vJey45YjsqeSLSjVtoj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_step1_gsm8k_temporal_dif.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06eaa02c-05b3-4983-87ec-c727c9fcf3ea",
  "isSidechain": false,
  "requestId": "req_011CbEoPVPZgXw85aW8W3eZ3",
  "type": "assistant",
  "uuid": "e8936ae6-1273-4cf4-a75b-8ee59b0128f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018BU1Pz79kw3wqYWfixW69x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10958,
      "cache_read_input_tokens": 23619,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10958,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 109,
          "cache_read_input_tokens": 23619,
          "cache_creation_input_tokens": 10958,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10958
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

_source line 15 · 2026-05-21T00:53:41.659Z_

<details><summary>↩ Tool result · `toolu_01RM6vJey45YjsqeSLSjVtoj`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_004_step1 — GSM8K Temporal MH-DIF Analysis
4	
5	Replicates plan_001 methodology on GSM8K data from METABENCH.
6	Two matching strategies:
7	  - standard: purified GSM8K total score
8	  - external: total scores from ARC + HellaSwag + TruthfulQA + Winogrande
9	
10	Inputs:
11	  metabench_data/benchmark-data/gsm8k.csv  — (source, item, correct) long format
12	  model_metadata.csv                        — cohort_temporal, etc.
13	  metabench_data/benchmark-data/{arc,hellaswag,truthfulqa,winogrande}.csv
14	
15	Outputs (in plan_004/):
16	  gsm8k_dif_results.csv, gsm8k_ets_summary.csv, plan_004_step1_report.md
17	"""
18	
19	import numpy as np
20	import pandas as pd
21	from scipy.stats import chi2 as chi2_dist
22	from pathlib import Path
23	import time
24	import warnings
25	import csv
26	
27	warnings.filterwarnings("ignore", category=RuntimeWarning)
28	
29	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
30	BENCH_DIR = BASE / "metabench_data" / "benchmark-data"
31	OUT = BASE / "plan_004"
32	OUT.mkdir(exist_ok=True)
33	
34	
35	# ════════════════════════════════════════════════════════════════════════════
36	#  DATA LOADING
37	# ════════════════════════════════════════════════════════════════════════════
38	print("=== Loading GSM8K data ===")
39	t0_load = time.time()
40	gsm = pd.read_csv(BENCH_DIR / "gsm8k.csv")
41	print(f"  Raw rows: {len(gsm):,}")
42	
43	gsm["correct"] = gsm["correct"].map({"True": 1, "False": 0, True: 1, False: 0}).astype(np.int8)
44	gsm_pivot = gsm.pivot(index="source", columns="item", values="correct")
45	gsm_pivot = gsm_pivot.fillna(0).astype(np.int8)
46	
47	MODEL_NAMES = np.array(gsm_pivot.index.tolist())
48	ITEM_IDS = np.array(gsm_pivot.columns.tolist())
49	X = gsm_pivot.values  # (N_models, J)
50	N_MODELS, J = X.shape
51	print(f"  Response matrix: {N_MODELS} models × {J} items")
52	del gsm, gsm_pivot
53	
54	NAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}
55	
56	# Load model metadata
57	model_meta = pd.read_csv(BASE / "model_metadata.csv")
58	print(f"  Model metadata: {len(model_meta)} models")
59	print(f"  Cohort distribution: {model_meta.cohort_temporal.value_counts().to_dict()}")
60	
61	# Intersection: GSM8K models ∩ metadata models
62	meta_names = set(model_meta["model_name"])
63	gsm_names = set(MODEL_NAMES)
64	common_names = meta_names & gsm_names
65	print(f"  GSM8K ∩ metadata: {len(common_names)} models")
66	
67	elapsed_load = time.time() - t0_load
68	print(f"  Load time: {elapsed_load:.1f}s")
69	
70	
71	# ════════════════════════════════════════════════════════════════════════════
72	#  EXTERNAL MATCHING SCORES
73	# ════════════════════════════════════════════════════════════════════════════
74	def compute_benchmark_scores(filepath, benchmark_name):
75	    """Compute per-model total scores from a benchmark CSV (chunked for large files)."""
76	    print(f"  Loading {benchmark_name}...")
77	    t0 = time.time()
78	    scores = {}
79	    counts = {}
80	    chunk_size = 500_000
81	    for chunk in pd.read_csv(filepath, chunksize=chunk_size):
82	        chunk["correct"] = chunk["correct"].map({"True": 1, "False": 0, True: 1, False: 0})
83	        grouped = chunk.groupby("source")["correct"].agg(["sum", "count"])
84	        for model, row in grouped.iterrows():
85	            if model in scores:
86	                scores[model] += row["sum"]
87	                counts[model] += row["count"]
88	            else:
89	                scores[model] = row["sum"]
90	                counts[model] = row["count"]
91	    # Normalize: proportion correct
92	    result = {m: scores[m] / counts[m] for m in scores if counts[m] > 0}
93	    print(f"    {benchmark_name}: {len(result)} models, {time.time()-t0:.1f}s")
94	    return result
95	
96	
97	print("\n=== Computing external matching scores ===")
98	ext_benchmarks = ["arc", "hellaswag", "truthfulqa", "winogrande"]
99	ext_scores_raw = {}
100	for bm in ext_benchmarks:
101	    ext_scores_raw[bm] = compute_benchmark_scores(BENCH_DIR / f"{bm}.csv", bm)
102	
103	# Combine: for each model, average across available benchmarks
104	# Only include models that appear in GSM8K AND have at least 2 external benchmarks
105	ext_combined = {}
106	for model in MODEL_NAMES:
107	    bm_scores = []
108	    for bm in ext_benchmarks:
109	        if model in ext_scores_raw[bm]:
110	            bm_scores.append(ext_scores_raw[bm][model])
111	    if len(bm_scores) >= 2:
112	        ext_combined[model] = np.mean(bm_scores)
113	
114	print(f"  Models with external scores (≥2 benchmarks): {len(ext_combined)}")
115	del ext_scores_raw
116	
117	
118	# ════════════════════════════════════════════════════════════════════════════
119	#  COHORT CONSTRUCTION
120	# ════════════════════════════════════════════════════════════════════════════
121	print("\n=== Cohort construction ===")
122	
123	
124	def rows_for(col, values):
125	    names = model_meta.loc[model_meta[col].isin(values), "model_name"]
126	    return np.array([NAME2ROW[n] for n in names if n in NAME2ROW])
127	
128	
129	ref_idx = rows_for("cohort_temporal", ["2023"])
130	foc_idx = rows_for("cohort_temporal", ["2024"])
131	print(f"  Temporal cohort: ref=2023 (N={len(ref_idx)}), foc=2024 (N={len(foc_idx)})")
132	
133	# For external matching, further restrict to models with external scores
134	ref_names_ext = [MODEL_NAMES[i] for i in ref_idx if MODEL_NAMES[i] in ext_combined]
135	foc_names_ext = [MODEL_NAMES[i] for i in foc_idx if MODEL_NAMES[i] in ext_combined]
136	ref_idx_ext = np.array([NAME2ROW[n] for n in ref_names_ext])
137	foc_idx_ext = np.array([NAME2ROW[n] for n in foc_names_ext])
138	print(f"  External cohort: ref=2023 (N={len(ref_idx_ext)}), foc=2024 (N={len(foc_idx_ext)})")
139	
140	
141	# ════════════════════════════════════════════════════════════════════════════
142	#  MH-DIF CORE
143	# ════════════════════════════════════════════════════════════════════════════
144	def _nan_row(j):
145	    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,
146	                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class="A")
147	
148	
149	def mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None, external_scores_foc=None):
150	    """
151	    Purified Mantel-Haenszel DIF.
152	
153	    If external_scores_{ref,foc} are provided, use them as the matching
154	    variable instead of purified total scores.
155	    """
156	    _Nr, Jc = X_ref.shape
157	    use_external = external_scores_ref is not None
158	
159	    if not use_external:
160	        tot_ref = X_ref.sum(axis=1).astype(np.float64)
161	        tot_foc = X_foc.sum(axis=1).astype(np.float64)
162	    else:
163	        ext_ref = external_scores_ref.astype(np.float64)
164	        ext_foc = external_scores_foc.astype(np.float64)
165	
166	    cols = np.arange(Jc)
167	    rows = []
168	    t0 = time.time()
169	
170	    for pos, j in enumerate(cols):
171	        if pos % 200 == 0 and pos > 0:
172	            print(f"    {pos}/{len(cols)}  ({time.time()-t0:.0f}s)")
173	
174	        if use_external:
175	            s_ref = ext_ref
176	            s_foc = ext_foc
177	        else:
178	            # Purified: exclude item j
179	            s_ref = tot_ref - X_ref[:, j].astype(np.float64)
180	            s_foc = tot_foc - X_foc[:, j].astype(np.float64)
181	
182	        s_all = np.concatenate([s_ref, s_foc])
183	        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
184	        if len(edges) < 2:
185	            rows.append(_nan_row(j))
186	            continue
187	        n_bins = len(edges) - 1
188	
189	        k_ref = np.digitize(s_ref, edges[1:-1])
190	        k_foc = np.digitize(s_foc, edges[1:-1])
191	
192	        R = S = 0.0
193	        sum_diff = 0.0
194	        sum_var = 0.0
195	        pr = ps_qr = qs = 0.0
196	        n_ok = 0
197	
198	        for k in range(n_bins):
199	            mr = (k_ref == k)
200	            mf = (k_foc == k)
201	            n1 = int(mr.sum())
202	            n0 = int(mf.sum())
203	            if n1 == 0 or n0 == 0:
204	                continue
205	
206	            A = float(X_ref[mr, j].sum())
207	            B = float(n1 - A)
208	            C = float(X_foc[mf, j].sum())
209	            D = float(n0 - C)
210	            Nk = float(n1 + n0)
211	            m1 = A + C
212	            m0 = B + D
213	
214	            if m1 == 0 or m0 == 0 or Nk <= 1:
215	                continue
216	            n_ok += 1
217	
218	            Rk = A * D / Nk
219	            Sk = B * C / Nk
220	            R += Rk
221	            S += Sk
222	
223	            EA = n1 * m1 / Nk
224	            sum_diff += A - EA
225	            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))
226	
227	            Pk = (A + D) / Nk
228	            Qk = (B + C) / Nk
229	            pr += Pk * Rk
230	            ps_qr += Pk * Sk + Qk * Rk
231	            qs += Qk * Sk
232	
233	        if n_ok == 0 or (R == 0 and S == 0):
234	            rows.append(_nan_row(j))
235	            continue
236	
237	        # MH odds ratio — handle inf properly
238	        if S == 0:
239	            alpha, delta, se = np.inf, -np.inf, np.nan
240	        elif R == 0:
241	            alpha, delta, se = 0.0, np.inf, np.nan
242	        else:
243	            alpha = R / S
244	            delta = -2.35 * np.log(alpha)
245	            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)
246	            se = 2.35 * np.sqrt(v) if v > 0 else np.nan
247	
248	        # MH chi2 with continuity correction
249	        if sum_var > 0:
250	            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var
251	            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)
252	        else:
253	            chi2_stat = pval = np.nan
254	
255	        # ETS classification — inf delta → extreme DIF (C if significant)
256	        ad = abs(delta) if np.isfinite(delta) else 999.0
257	        if ad < 1.0:
258	            ets = "A"
259	        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:
260	            ets = "C"
261	        else:
262	            ets = "B"
263	
264	        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,
265	                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets))
266	
267	    elapsed = time.time() - t0
268	    print(f"    done — {len(cols)} items in {elapsed:.1f}s")
269	    return pd.DataFrame(rows)
270	
271	
272	# ════════════════════════════════════════════════════════════════════════════
273	#  MAIN ANALYSIS
274	# ════════════════════════════════════════════════════════════════════════════
275	def main():
276	    results_parts = []
277	
278	    # ── Standard MH-DIF (purified GSM8K total score) ──────────────────────
279	    print("\n=== Standard MH-DIF (purified GSM8K total, 5 strata) ===")
280	    print(f"  ref=2023 (N={len(ref_idx)}), foc=2024 (N={len(foc_idx)})")
281	
282	    dif_std = mh_dif(X[ref_idx], X[foc_idx], n_strata=5)
283	    dif_std["item_id"] = [ITEM_IDS[i] for i in dif_std["col_idx"]]
284	    dif_std["matching_type"] = "standard"
285	    print(f"  ETS: {dif_std.ets_class.value_counts().to_dict()}")
286	
287	    delta_finite = dif_std.loc[np.isfinite(dif_std.delta_mh), "delta_mh"]
288	    print(f"  Δ_MH stats: mean={delta_finite.mean():.3f}, median={delta_finite.median():.3f}, "
289	          f"std={delta_finite.std():.3f}, range=[{delta_finite.min():.3f}, {delta_finite.max():.3f}]")
290	    results_parts.append(dif_std)
291	
292	    # ── External MH-DIF (other benchmarks total score) ────────────────────
293	    print("\n=== External MH-DIF (ARC+HellaSwag+TruthfulQA+Winogrande, 5 strata) ===")
294	    print(f"  ref=2023 (N={len(ref_idx_ext)}), foc=2024 (N={len(foc_idx_ext)})")
295	
296	    ext_ref_scores = np.array([ext_combined[MODEL_NAMES[i]] for i in ref_idx_ext])
297	    ext_foc_scores = np.array([ext_combined[MODEL_NAMES[i]] for i in foc_idx_ext])
298	
299	    dif_ext = mh_dif(X[ref_idx_ext], X[foc_idx_ext], n_strata=5,
300	                     external_scores_ref=ext_ref_scores,
301	                     external_scores_foc=ext_foc_scores)
302	    dif_ext["item_id"] = [ITEM_IDS[i] for i in dif_ext["col_idx"]]
303	    dif_ext["matching_type"] = "external"
304	    print(f"  ETS: {dif_ext.ets_class.value_counts().to_dict()}")
305	
306	    delta_finite_ext = dif_ext.loc[np.isfinite(dif_ext.delta_mh), "delta_mh"]
307	    print(f"  Δ_MH stats: mean={delta_finite_ext.mean():.3f}, median={delta_finite_ext.median():.3f}, "
308	          f"std={delta_finite_ext.std():.3f}, range=[{delta_finite_ext.min():.3f}, {delta_finite_ext.max():.3f}]")
309	    results_parts.append(dif_ext)
310	
311	    # ── Sanity check: random split ────────────────────────────────────────
312	    print("\n=== Sanity check: random half-split of 2023 cohort ===")
313	    rng = np.random.RandomState(42)
314	    perm = rng.permutation(len(ref_idx))
315	    half = len(perm) // 2
316	    san_ref = ref_idx[perm[:half]]
317	    san_foc = ref_idx[perm[half:]]
318	    print(f"  Split: {len(san_ref)} vs {len(san_foc)}")
319	    dif_san = mh_dif(X[san_ref], X[san_foc], n_strata=5)
320	    vc_san = dif_san["ets_class"].value_counts()
321	    n_c_san = vc_san.get("C", 0)
322	    pct_c_san = n_c_san / len(dif_san) * 100
323	    print(f"  ETS C: {n_c_san}/{len(dif_san)} = {pct_c_san:.2f}% (expect <5%)")
324	
325	    # ── Agreement between standard and external ───────────────────────────
326	    print("\n=== Agreement: standard vs external ===")
327	    merged = dif_std[["item_id", "ets_class", "delta_mh"]].merge(
328	        dif_ext[["item_id", "ets_class", "delta_mh"]],
329	        on="item_id", suffixes=("_std", "_ext"))
330	
331	    both_c = ((merged.ets_class_std == "C") & (merged.ets_class_ext == "C")).sum()
332	    std_only_c = ((merged.ets_class_std == "C") & (merged.ets_class_ext != "C")).sum()
333	    ext_only_c = ((merged.ets_class_std != "C") & (merged.ets_class_ext == "C")).sum()
334	    neither_c = ((merged.ets_class_std != "C") & (merged.ets_class_ext != "C")).sum()
335	    print(f"  both_C={both_c}, std_only_C={std_only_c}, ext_only_C={ext_only_c}, neither={neither_c}")
336	
337	    # Correlation of delta_mh between standard and external
338	    finite_mask = np.isfinite(merged.delta_mh_std) & np.isfinite(merged.delta_mh_ext)
339	    if finite_mask.sum() > 10:
340	        from scipy.stats import spearmanr, pearsonr
341	        rho_s, p_s = spearmanr(merged.loc[finite_mask, "delta_mh_std"],
342	                                merged.loc[finite_mask, "delta_mh_ext"])
343	        r_p, p_p = pearsonr(merged.loc[finite_mask, "delta_mh_std"],
344	                            merged.loc[finite_mask, "delta_mh_ext"])
345	        print(f"  Δ_MH correlation: Spearman ρ={rho_s:.3f} (p={p_s:.2e}), Pearson r={r_p:.3f} (p={p_p:.2e})")
346	
347	    # ── Save results ──────────────────────────────────────────────────────
348	    print("\n=== Saving outputs ===")
349	
350	    # Combined DIF results
351	    all_results = pd.concat(results_parts, ignore_index=True)
352	    out_cols = ["item_id", "matching_type", "alpha_mh", "delta_mh", "se",
353	                "chi2", "p_value", "ets_class"]
354	    all_results[out_cols].to_csv(OUT / "gsm8k_dif_results.csv", index=False)
355	
356	    # ETS summary
357	    summary_rows = []
358	    for mt in ["standard", "external"]:
359	        sub = all_results[all_results.matching_type == mt]
360	        vc = sub.ets_class.value_counts()
361	        n = len(sub)
362	        d_fin = sub.loc[np.isfinite(sub.delta_mh), "delta_mh"]
363	        summary_rows.append(dict(
364	            matching_type=mt,
365	            n_ref=len(ref_idx) if mt == "standard" else len(ref_idx_ext),
366	            n_foc=len(foc_idx) if mt == "standard" else len(foc_idx_ext),
367	            n_items=n,
368	            n_ets_a=vc.get("A", 0), n_ets_b=vc.get("B", 0), n_ets_c=vc.get("C", 0),
369	            pct_a=vc.get("A", 0) / n * 100,
370	            pct_b=vc.get("B", 0) / n * 100,
371	            pct_c=vc.get("C", 0) / n * 100,
372	            delta_mean=d_fin.mean(), delta_median=d_fin.median(),
373	            delta_std=d_fin.std(), delta_min=d_fin.min(), delta_max=d_fin.max(),
374	        ))
375	    summary_rows.append(dict(
376	        matching_type="sanity_random",
377	        n_ref=len(san_ref), n_foc=len(san_foc),
378	        n_items=len(dif_san),
379	        n_ets_a=vc_san.get("A", 0), n_ets_b=vc_san.get("B", 0), n_ets_c=vc_san.get("C", 0),
380	        pct_a=vc_san.get("A", 0) / len(dif_san) * 100,
381	        pct_b=vc_san.get("B", 0) / len(dif_san) * 100,
382	        pct_c=pct_c_san,
383	        delta_mean=np.nan, delta_median=np.nan,
384	        delta_std=np.nan, delta_min=np.nan, delta_max=np.nan,
385	    ))
386	    summary_df = pd.DataFrame(summary_rows)
387	    summary_df.to_csv(OUT / "gsm8k_ets_summary.csv", index=False)
388	
389	    # ── Generate report ───────────────────────────────────────────────────
390	    L = []
391	    def w(s=""):
392	        L.append(s)
393	
394	    w("# Plan 004 Step 1: GSM8K Temporal MH-DIF Analysis")
395	    w()
396	    w("## 1. Data & Setup")
397	    w()
398	    w(f"- **Benchmark**: GSM8K (grade-school math, single domain)")
399	    w(f"- **Response matrix**: {N_MODELS} models × {J} items")
400	    w(f"- **GSM8K ∩ metadata**: {len(common_names)} models")
401	    w(f"- **Temporal cohort (standard)**: ref=2023 (N={len(ref_idx)}), foc=2024 (N={len(foc_idx)})")
402	    w(f"- **Temporal cohort (external)**: ref=2023 (N={len(ref_idx_ext)}), foc=2024 (N={len(foc_idx_ext)})")
403	    w(f"- **External matching**: average proportion correct across ARC, HellaSwag, TruthfulQA, Winogrande")
404	    w(f"- **Models with external scores**: {len(ext_combined)} (require ≥2 benchmarks)")
405	    w()
406	
407	    w("## 2. ETS Classification")
408	    w()
409	    w("| Matching | N_ref | N_foc | Items | A | B | C | %A | %B | %C |")
410	    w("|----------|-------|-------|-------|---|---|---|-----|-----|-----|")
411	    for _, r in summary_df.iterrows():
412	        w(f"| {r.matching_type} | {r.n_ref} | {r.n_foc} | {r.n_items} | "
413	          f"{r.n_ets_a} | {r.n_ets_b} | {r.n_ets_c} | "
414	          f"{r.pct_a:.1f}% | {r.pct_b:.1f}% | {r.pct_c:.1f}% |")
415	    w()
416	
417	    w("## 3. Δ_MH Distribution (finite values)")
418	    w()
419	    w("| Matching | Mean | Median | Std | Min | Max |")
420	    w("|----------|------|--------|-----|-----|-----|")
421	    for _, r in summary_df[summary_df.matching_type != "sanity_random"].iterrows():
422	        w(f"| {r.matching_type} | {r.delta_mean:.3f} | {r.delta_median:.3f} | "
423	          f"{r.delta_std:.3f} | {r.delta_min:.3f} | {r.delta_max:.3f} |")
424	    w()
425	
426	    # Inf delta items
427	    n_inf_std = (~np.isfinite(dif_std.delta_mh)).sum()
428	    n_inf_ext = (~np.isfinite(dif_ext.delta_mh)).sum()
429	    w(f"- Non-finite Δ_MH: standard={n_inf_std}, external={n_inf_ext}")
430	    w()
431	
432	    w("## 4. Standard vs External Agreement")
433	    w()
434	    w(f"- Both C: {both_c}")
435	    w(f"- Standard-only C: {std_only_c}")
436	    w(f"- External-only C: {ext_only_c}")
437	    w(f"- Neither C: {neither_c}")
438	    if finite_mask.sum() > 10:
439	        w(f"- Δ_MH Spearman ρ = {rho_s:.3f} (p = {p_s:.2e})")
440	        w(f"- Δ_MH Pearson r = {r_p:.3f} (p = {p_p:.2e})")
441	    w()
442	
443	    w("## 5. Sanity Check")
444	    w()
445	    w(f"Random half-split of 2023 cohort: **{pct_c_san:.2f}% C** (expect < 5%)")
446	    w()
447	
448	    w("## 6. Comparison with MMLU (plan_001)")
449	    w()
450	    w("| | MMLU (plan_001) | GSM8K (this) |")
451	    w("|--|----------------|--------------|")
452	    w(f"| Items | 12,508 | {J} |")
453	    w(f"| Models (temporal) | 1,080 vs 807 | {len(ref_idx)} vs {len(foc_idx)} |")
454	    w(f"| Standard %C | (see plan_001_report) | {summary_df.loc[summary_df.matching_type=='standard','pct_c'].iloc[0]:.1f}% |")
455	    w(f"| Sanity %C | (see plan_001_report) | {pct_c_san:.1f}% |")
456	    w()
457	
458	    # Top DIF items
459	    w("## 7. Top 20 DIF Items (standard matching, by |Δ_MH|)")
460	    w()
461	    dif_std_sorted = dif_std.loc[np.isfinite(dif_std.delta_mh)].copy()
462	    dif_std_sorted["abs_delta"] = dif_std_sorted.delta_mh.abs()
463	    top20 = dif_std_sorted.nlargest(20, "abs_delta")
464	    w("| Item | Δ_MH | SE | p-value | ETS |")
465	    w("|------|------|----|---------|-----|")
466	    for _, r in top20.iterrows():
467	        p_str = f"{r.p_value:.2e}" if not np.isnan(r.p_value) else "NaN"
468	        w(f"| {r.item_id} | {r.delta_mh:+.3f} | {r.se:.3f} | {p_str} | {r.ets_class} |")
469	    w()
470	
471	    # Direction analysis
472	    w("## 8. DIF Direction Analysis")
473	    w()
474	    n_pos = (dif_std_sorted.delta_mh > 0).sum()
475	    n_neg = (dif_std_sorted.delta_mh < 0).sum()
476	    n_zero = (dif_std_sorted.delta_mh == 0).sum()
477	    w(f"- Positive Δ (favoring 2024): {n_pos} items ({n_pos/len(dif_std_sorted)*100:.1f}%)")
478	    w(f"- Negative Δ (favoring 2023): {n_neg} items ({n_neg/len(dif_std_sorted)*100:.1f}%)")
479	    w(f"- Zero Δ: {n_zero} items")
480	    w()
481	
482	    c_items = dif_std[dif_std.ets_class == "C"]
483	    if len(c_items) > 0:
484	        c_pos = (c_items.delta_mh > 0).sum()
485	        c_neg = (c_items.delta_mh < 0).sum()
486	        w(f"Among ETS-C items: {c_pos} favor 2024, {c_neg} favor 2023")
487	    w()
488	
489	    report_text = "\n".join(L) + "\n"
490	    (OUT / "plan_004_step1_report.md").write_text(report_text)
491	
492	    print("\n" + "=" * 60)
493	    print("SUMMARY")
494	    print("=" * 60)
495	    for _, r in summary_df.iterrows():
496	        print(f"  {r.matching_type}: A={r.n_ets_a}, B={r.n_ets_b}, C={r.n_ets_c} ({r.pct_c:.1f}%)")
497	    print(f"  Sanity random: {pct_c_san:.2f}% C")
498	    print(f"\nAll outputs saved to {OUT}")
499	
500	
501	if __name__ == "__main__":
502	    main()
503	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8936ae6-1273-4cf4-a75b-8ee59b0128f9",
  "isSidechain": false,
  "promptId": "b681718f-ed7e-4c71-ace8-cbf70777063c",
  "type": "user",
  "uuid": "abe9bc77-63b5-4dd8-a3df-770b075f6d82",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_step1_gsm8k_temporal_dif.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nplan_004_step1 — GSM8K Temporal MH-DIF Analysis\n\nReplicates plan_001 methodology on GSM8K data from METABENCH.\nTwo matching strategies:\n  - standard: purified GSM8K total score\n  - external: total scores from ARC + HellaSwag + TruthfulQA + Winogrande\n\nInputs:\n  metabench_data/benchmark-data/gsm8k.csv  — (source, item, correct) long format\n  model_metadata.csv                        — cohort_temporal, etc.\n  metabench_data/benchmark-data/{arc,hellaswag,truthfulqa,winogrande}.csv\n\nOutputs (in plan_004/):\n  gsm8k_dif_results.csv, gsm8k_ets_summary.csv, plan_004_step1_report.md\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.stats import chi2 as chi2_dist\nfrom pathlib import Path\nimport time\nimport warnings\nimport csv\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\")\nBENCH_DIR = BASE / \"metabench_data\" / \"benchmark-data\"\nOUT = BASE / \"plan_004\"\nOUT.mkdir(exist_ok=True)\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  DATA LOADING\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"=== Loading GSM8K data ===\")\nt0_load = time.time()\ngsm = pd.read_csv(BENCH_DIR / \"gsm8k.csv\")\nprint(f\"  Raw rows: {len(gsm):,}\")\n\ngsm[\"correct\"] = gsm[\"correct\"].map({\"True\": 1, \"False\": 0, True: 1, False: 0}).astype(np.int8)\ngsm_pivot = gsm.pivot(index=\"source\", columns=\"item\", values=\"correct\")\ngsm_pivot = gsm_pivot.fillna(0).astype(np.int8)\n\nMODEL_NAMES = np.array(gsm_pivot.index.tolist())\nITEM_IDS = np.array(gsm_pivot.columns.tolist())\nX = gsm_pivot.values  # (N_models, J)\nN_MODELS, J = X.shape\nprint(f\"  Response matrix: {N_MODELS} models × {J} items\")\ndel gsm, gsm_pivot\n\nNAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}\n\n# Load model metadata\nmodel_meta = pd.read_csv(BASE / \"model_metadata.csv\")\nprint(f\"  Model metadata: {len(model_meta)} models\")\nprint(f\"  Cohort distribution: {model_meta.cohort_temporal.value_counts().to_dict()}\")\n\n# Intersection: GSM8K models ∩ metadata models\nmeta_names = set(model_meta[\"model_name\"])\ngsm_names = set(MODEL_NAMES)\ncommon_names = meta_names & gsm_names\nprint(f\"  GSM8K ∩ metadata: {len(common_names)} models\")\n\nelapsed_load = time.time() - t0_load\nprint(f\"  Load time: {elapsed_load:.1f}s\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  EXTERNAL MATCHING SCORES\n# ════════════════════════════════════════════════════════════════════════════\ndef compute_benchmark_scores(filepath, benchmark_name):\n    \"\"\"Compute per-model total scores from a benchmark CSV (chunked for large files).\"\"\"\n    print(f\"  Loading {benchmark_name}...\")\n    t0 = time.time()\n    scores = {}\n    counts = {}\n    chunk_size = 500_000\n    for chunk in pd.read_csv(filepath, chunksize=chunk_size):\n        chunk[\"correct\"] = chunk[\"correct\"].map({\"True\": 1, \"False\": 0, True: 1, False: 0})\n        grouped = chunk.groupby(\"source\")[\"correct\"].agg([\"sum\", \"count\"])\n        for model, row in grouped.iterrows():\n            if model in scores:\n                scores[model] += row[\"sum\"]\n                counts[model] += row[\"count\"]\n            else:\n                scores[model] = row[\"sum\"]\n                counts[model] = row[\"count\"]\n    # Normalize: proportion correct\n    result = {m: scores[m] / counts[m] for m in scores if counts[m] > 0}\n    print(f\"    {benchmark_name}: {len(result)} models, {time.time()-t0:.1f}s\")\n    return result\n\n\nprint(\"\\n=== Computing external matching scores ===\")\next_benchmarks = [\"arc\", \"hellaswag\", \"truthfulqa\", \"winogrande\"]\next_scores_raw = {}\nfor bm in ext_benchmarks:\n    ext_scores_raw[bm] = compute_benchmark_scores(BENCH_DIR / f\"{bm}.csv\", bm)\n\n# Combine: for each model, average across available benchmarks\n# Only include models that appear in GSM8K AND have at least 2 external benchmarks\next_combined = {}\nfor model in MODEL_NAMES:\n    bm_scores = []\n    for bm in ext_benchmarks:\n        if model in ext_scores_raw[bm]:\n            bm_scores.append(ext_scores_raw[bm][model])\n    if len(bm_scores) >= 2:\n        ext_combined[model] = np.mean(bm_scores)\n\nprint(f\"  Models with external scores (≥2 benchmarks): {len(ext_combined)}\")\ndel ext_scores_raw\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  COHORT CONSTRUCTION\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Cohort construction ===\")\n\n\ndef rows_for(col, values):\n    names = model_meta.loc[model_meta[col].isin(values), \"model_name\"]\n    return np.array([NAME2ROW[n] for n in names if n in NAME2ROW])\n\n\nref_idx = rows_for(\"cohort_temporal\", [\"2023\"])\nfoc_idx = rows_for(\"cohort_temporal\", [\"2024\"])\nprint(f\"  Temporal cohort: ref=2023 (N={len(ref_idx)}), foc=2024 (N={len(foc_idx)})\")\n\n# For external matching, further restrict to models with external scores\nref_names_ext = [MODEL_NAMES[i] for i in ref_idx if MODEL_NAMES[i] in ext_combined]\nfoc_names_ext = [MODEL_NAMES[i] for i in foc_idx if MODEL_NAMES[i] in ext_combined]\nref_idx_ext = np.array([NAME2ROW[n] for n in ref_names_ext])\nfoc_idx_ext = np.array([NAME2ROW[n] for n in foc_names_ext])\nprint(f\"  External cohort: ref=2023 (N={len(ref_idx_ext)}), foc=2024 (N={len(foc_idx_ext)})\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MH-DIF CORE\n# ════════════════════════════════════════════════════════════════════════════\ndef _nan_row(j):\n    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,\n                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class=\"A\")\n\n\ndef mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None, external_scores_foc=None):\n    \"\"\"\n    Purified Mantel-Haenszel DIF.\n\n    If external_scores_{ref,foc} are provided, use them as the matching\n    variable instead of purified total scores.\n    \"\"\"\n    _Nr, Jc = X_ref.shape\n    use_external = external_scores_ref is not None\n\n    if not use_external:\n        tot_ref = X_ref.sum(axis=1).astype(np.float64)\n        tot_foc = X_foc.sum(axis=1).astype(np.float64)\n    else:\n        ext_ref = external_scores_ref.astype(np.float64)\n        ext_foc = external_scores_foc.astype(np.float64)\n\n    cols = np.arange(Jc)\n    rows = []\n    t0 = time.time()\n\n    for pos, j in enumerate(cols):\n        if pos % 200 == 0 and pos > 0:\n            print(f\"    {pos}/{len(cols)}  ({time.time()-t0:.0f}s)\")\n\n        if use_external:\n            s_ref = ext_ref\n            s_foc = ext_foc\n        else:\n            # Purified: exclude item j\n            s_ref = tot_ref - X_ref[:, j].astype(np.float64)\n            s_foc = tot_foc - X_foc[:, j].astype(np.float64)\n\n        s_all = np.concatenate([s_ref, s_foc])\n        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n        if len(edges) < 2:\n            rows.append(_nan_row(j))\n            continue\n        n_bins = len(edges) - 1\n\n        k_ref = np.digitize(s_ref, edges[1:-1])\n        k_foc = np.digitize(s_foc, edges[1:-1])\n\n        R = S = 0.0\n        sum_diff = 0.0\n        sum_var = 0.0\n        pr = ps_qr = qs = 0.0\n        n_ok = 0\n\n        for k in range(n_bins):\n            mr = (k_ref == k)\n            mf = (k_foc == k)\n            n1 = int(mr.sum())\n            n0 = int(mf.sum())\n            if n1 == 0 or n0 == 0:\n                continue\n\n            A = float(X_ref[mr, j].sum())\n            B = float(n1 - A)\n            C = float(X_foc[mf, j].sum())\n            D = float(n0 - C)\n            Nk = float(n1 + n0)\n            m1 = A + C\n            m0 = B + D\n\n            if m1 == 0 or m0 == 0 or Nk <= 1:\n                continue\n            n_ok += 1\n\n            Rk = A * D / Nk\n            Sk = B * C / Nk\n            R += Rk\n            S += Sk\n\n            EA = n1 * m1 / Nk\n            sum_diff += A - EA\n            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n            Pk = (A + D) / Nk\n            Qk = (B + C) / Nk\n            pr += Pk * Rk\n            ps_qr += Pk * Sk + Qk * Rk\n            qs += Qk * Sk\n\n        if n_ok == 0 or (R == 0 and S == 0):\n            rows.append(_nan_row(j))\n            continue\n\n        # MH odds ratio — handle inf properly\n        if S == 0:\n            alpha, delta, se = np.inf, -np.inf, np.nan\n        elif R == 0:\n            alpha, delta, se = 0.0, np.inf, np.nan\n        else:\n            alpha = R / S\n            delta = -2.35 * np.log(alpha)\n            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)\n            se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n        # MH chi2 with continuity correction\n        if sum_var > 0:\n            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n        else:\n            chi2_stat = pval = np.nan\n\n        # ETS classification — inf delta → extreme DIF (C if significant)\n        ad = abs(delta) if np.isfinite(delta) else 999.0\n        if ad < 1.0:\n            ets = \"A\"\n        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n            ets = \"C\"\n        else:\n            ets = \"B\"\n\n        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,\n                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets))\n\n    elapsed = time.time() - t0\n    print(f\"    done — {len(cols)} items in {elapsed:.1f}s\")\n    return pd.DataFrame(rows)\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MAIN ANALYSIS\n# ════════════════════════════════════════════════════════════════════════════\ndef main():\n    results_parts = []\n\n    # ── Standard MH-DIF (purified GSM8K total score) ──────────────────────\n    print(\"\\n=== Standard MH-DIF (purified GSM8K total, 5 strata) ===\")\n    print(f\"  ref=2023 (N={len(ref_idx)}), foc=2024 (N={len(foc_idx)})\")\n\n    dif_std = mh_dif(X[ref_idx], X[foc_idx], n_strata=5)\n    dif_std[\"item_id\"] = [ITEM_IDS[i] for i in dif_std[\"col_idx\"]]\n    dif_std[\"matching_type\"] = \"standard\"\n    print(f\"  ETS: {dif_std.ets_class.value_counts().to_dict()}\")\n\n    delta_finite = dif_std.loc[np.isfinite(dif_std.delta_mh), \"delta_mh\"]\n    print(f\"  Δ_MH stats: mean={delta_finite.mean():.3f}, median={delta_finite.median():.3f}, \"\n          f\"std={delta_finite.std():.3f}, range=[{delta_finite.min():.3f}, {delta_finite.max():.3f}]\")\n    results_parts.append(dif_std)\n\n    # ── External MH-DIF (other benchmarks total score) ────────────────────\n    print(\"\\n=== External MH-DIF (ARC+HellaSwag+TruthfulQA+Winogrande, 5 strata) ===\")\n    print(f\"  ref=2023 (N={len(ref_idx_ext)}), foc=2024 (N={len(foc_idx_ext)})\")\n\n    ext_ref_scores = np.array([ext_combined[MODEL_NAMES[i]] for i in ref_idx_ext])\n    ext_foc_scores = np.array([ext_combined[MODEL_NAMES[i]] for i in foc_idx_ext])\n\n    dif_ext = mh_dif(X[ref_idx_ext], X[foc_idx_ext], n_strata=5,\n                     external_scores_ref=ext_ref_scores,\n                     external_scores_foc=ext_foc_scores)\n    dif_ext[\"item_id\"] = [ITEM_IDS[i] for i in dif_ext[\"col_idx\"]]\n    dif_ext[\"matching_type\"] = \"external\"\n    print(f\"  ETS: {dif_ext.ets_class.value_counts().to_dict()}\")\n\n    delta_finite_ext = dif_ext.loc[np.isfinite(dif_ext.delta_mh), \"delta_mh\"]\n    print(f\"  Δ_MH stats: mean={delta_finite_ext.mean():.3f}, median={delta_finite_ext.median():.3f}, \"\n          f\"std={delta_finite_ext.std():.3f}, range=[{delta_finite_ext.min():.3f}, {delta_finite_ext.max():.3f}]\")\n    results_parts.append(dif_ext)\n\n    # ── Sanity check: random split ────────────────────────────────────────\n    print(\"\\n=== Sanity check: random half-split of 2023 cohort ===\")\n    rng = np.random.RandomState(42)\n    perm = rng.permutation(len(ref_idx))\n    half = len(perm) // 2\n    san_ref = ref_idx[perm[:half]]\n    san_foc = ref_idx[perm[half:]]\n    print(f\"  Split: {len(san_ref)} vs {len(san_foc)}\")\n    dif_san = mh_dif(X[san_ref], X[san_foc], n_strata=5)\n    vc_san = dif_san[\"ets_class\"].value_counts()\n    n_c_san = vc_san.get(\"C\", 0)\n    pct_c_san = n_c_san / len(dif_san) * 100\n    print(f\"  ETS C: {n_c_san}/{len(dif_san)} = {pct_c_san:.2f}% (expect <5%)\")\n\n    # ── Agreement between standard and external ───────────────────────────\n    print(\"\\n=== Agreement: standard vs external ===\")\n    merged = dif_std[[\"item_id\", \"ets_class\", \"delta_mh\"]].merge(\n        dif_ext[[\"item_id\", \"ets_class\", \"delta_mh\"]],\n        on=\"item_id\", suffixes=(\"_std\", \"_ext\"))\n\n    both_c = ((merged.ets_class_std == \"C\") & (merged.ets_class_ext == \"C\")).sum()\n    std_only_c = ((merged.ets_class_std == \"C\") & (merged.ets_class_ext != \"C\")).sum()\n    ext_only_c = ((merged.ets_class_std != \"C\") & (merged.ets_class_ext == \"C\")).sum()\n    neither_c = ((merged.ets_class_std != \"C\") & (merged.ets_class_ext != \"C\")).sum()\n    print(f\"  both_C={both_c}, std_only_C={std_only_c}, ext_only_C={ext_only_c}, neither={neither_c}\")\n\n    # Correlation of delta_mh between standard and external\n    finite_mask = np.isfinite(merged.delta_mh_std) & np.isfinite(merged.delta_mh_ext)\n    if finite_mask.sum() > 10:\n        from scipy.stats import spearmanr, pearsonr\n        rho_s, p_s = spearmanr(merged.loc[finite_mask, \"delta_mh_std\"],\n                                merged.loc[finite_mask, \"delta_mh_ext\"])\n        r_p, p_p = pearsonr(merged.loc[finite_mask, \"delta_mh_std\"],\n                            merged.loc[finite_mask, \"delta_mh_ext\"])\n        print(f\"  Δ_MH correlation: Spearman ρ={rho_s:.3f} (p={p_s:.2e}), Pearson r={r_p:.3f} (p={p_p:.2e})\")\n\n    # ── Save results ──────────────────────────────────────────────────────\n    print(\"\\n=== Saving outputs ===\")\n\n    # Combined DIF results\n    all_results = pd.concat(results_parts, ignore_index=True)\n    out_cols = [\"item_id\", \"matching_type\", \"alpha_mh\", \"delta_mh\", \"se\",\n                \"chi2\", \"p_value\", \"ets_class\"]\n    all_results[out_cols].to_csv(OUT / \"gsm8k_dif_results.csv\", index=False)\n\n    # ETS summary\n    summary_rows = []\n    for mt in [\"standard\", \"external\"]:\n        sub = all_results[all_results.matching_type == mt]\n        vc = sub.ets_class.value_counts()\n        n = len(sub)\n        d_fin = sub.loc[np.isfinite(sub.delta_mh), \"delta_mh\"]\n        summary_rows.append(dict(\n            matching_type=mt,\n            n_ref=len(ref_idx) if mt == \"standard\" else len(ref_idx_ext),\n            n_foc=len(foc_idx) if mt == \"standard\" else len(foc_idx_ext),\n            n_items=n,\n            n_ets_a=vc.get(\"A\", 0), n_ets_b=vc.get(\"B\", 0), n_ets_c=vc.get(\"C\", 0),\n            pct_a=vc.get(\"A\", 0) / n * 100,\n            pct_b=vc.get(\"B\", 0) / n * 100,\n            pct_c=vc.get(\"C\", 0) / n * 100,\n            delta_mean=d_fin.mean(), delta_median=d_fin.median(),\n            delta_std=d_fin.std(), delta_min=d_fin.min(), delta_max=d_fin.max(),\n        ))\n    summary_rows.append(dict(\n        matching_type=\"sanity_random\",\n        n_ref=len(san_ref), n_foc=len(san_foc),\n        n_items=len(dif_san),\n        n_ets_a=vc_san.get(\"A\", 0), n_ets_b=vc_san.get(\"B\", 0), n_ets_c=vc_san.get(\"C\", 0),\n        pct_a=vc_san.get(\"A\", 0) / len(dif_san) * 100,\n        pct_b=vc_san.get(\"B\", 0) / len(dif_san) * 100,\n        pct_c=pct_c_san,\n        delta_mean=np.nan, delta_median=np.nan,\n        delta_std=np.nan, delta_min=np.nan, delta_max=np.nan,\n    ))\n    summary_df = pd.DataFrame(summary_rows)\n    summary_df.to_csv(OUT / \"gsm8k_ets_summary.csv\", index=False)\n\n    # ── Generate report ───────────────────────────────────────────────────\n    L = []\n    def w(s=\"\"):\n        L.append(s)\n\n    w(\"# Plan 004 Step 1: GSM8K Temporal MH-DIF Analysis\")\n    w()\n    w(\"## 1. Data & Setup\")\n    w()\n    w(f\"- **Benchmark**: GSM8K (grade-school math, single domain)\")\n    w(f\"- **Response matrix**: {N_MODELS} models × {J} items\")\n    w(f\"- **GSM8K ∩ metadata**: {len(common_names)} models\")\n    w(f\"- **Temporal cohort (standard)**: ref=2023 (N={len(ref_idx)}), foc=2024 (N={len(foc_idx)})\")\n    w(f\"- **Temporal cohort (external)**: ref=2023 (N={len(ref_idx_ext)}), foc=2024 (N={len(foc_idx_ext)})\")\n    w(f\"- **External matching**: average proportion correct across ARC, HellaSwag, TruthfulQA, Winogrande\")\n    w(f\"- **Models with external scores**: {len(ext_combined)} (require ≥2 benchmarks)\")\n    w()\n\n    w(\"## 2. ETS Classification\")\n    w()\n    w(\"| Matching | N_ref | N_foc | Items | A | B | C | %A | %B | %C |\")\n    w(\"|----------|-------|-------|-------|---|---|---|-----|-----|-----|\")\n    for _, r in summary_df.iterrows():\n        w(f\"| {r.matching_type} | {r.n_ref} | {r.n_foc} | {r.n_items} | \"\n          f\"{r.n_ets_a} | {r.n_ets_b} | {r.n_ets_c} | \"\n          f\"{r.pct_a:.1f}% | {r.pct_b:.1f}% | {r.pct_c:.1f}% |\")\n    w()\n\n    w(\"## 3. Δ_MH Distribution (finite values)\")\n    w()\n    w(\"| Matching | Mean | Median | Std | Min | Max |\")\n    w(\"|----------|------|--------|-----|-----|-----|\")\n    for _, r in summary_df[summary_df.matching_type != \"sanity_random\"].iterrows():\n        w(f\"| {r.matching_type} | {r.delta_mean:.3f} | {r.delta_median:.3f} | \"\n          f\"{r.delta_std:.3f} | {r.delta_min:.3f} | {r.delta_max:.3f} |\")\n    w()\n\n    # Inf delta items\n    n_inf_std = (~np.isfinite(dif_std.delta_mh)).sum()\n    n_inf_ext = (~np.isfinite(dif_ext.delta_mh)).sum()\n    w(f\"- Non-finite Δ_MH: standard={n_inf_std}, external={n_inf_ext}\")\n    w()\n\n    w(\"## 4. Standard vs External Agreement\")\n    w()\n    w(f\"- Both C: {both_c}\")\n    w(f\"- Standard-only C: {std_only_c}\")\n    w(f\"- External-only C: {ext_only_c}\")\n    w(f\"- Neither C: {neither_c}\")\n    if finite_mask.sum() > 10:\n        w(f\"- Δ_MH Spearman ρ = {rho_s:.3f} (p = {p_s:.2e})\")\n        w(f\"- Δ_MH Pearson r = {r_p:.3f} (p = {p_p:.2e})\")\n    w()\n\n    w(\"## 5. Sanity Check\")\n    w()\n    w(f\"Random half-split of 2023 cohort: **{pct_c_san:.2f}% C** (expect < 5%)\")\n    w()\n\n    w(\"## 6. Comparison with MMLU (plan_001)\")\n    w()\n    w(\"| | MMLU (plan_001) | GSM8K (this) |\")\n    w(\"|--|----------------|--------------|\")\n    w(f\"| Items | 12,508 | {J} |\")\n    w(f\"| Models (temporal) | 1,080 vs 807 | {len(ref_idx)} vs {len(foc_idx)} |\")\n    w(f\"| Standard %C | (see plan_001_report) | {summary_df.loc[summary_df.matching_type=='standard','pct_c'].iloc[0]:.1f}% |\")\n    w(f\"| Sanity %C | (see plan_001_report) | {pct_c_san:.1f}% |\")\n    w()\n\n    # Top DIF items\n    w(\"## 7. Top 20 DIF Items (standard matching, by |Δ_MH|)\")\n    w()\n    dif_std_sorted = dif_std.loc[np.isfinite(dif_std.delta_mh)].copy()\n    dif_std_sorted[\"abs_delta\"] = dif_std_sorted.delta_mh.abs()\n    top20 = dif_std_sorted.nlargest(20, \"abs_delta\")\n    w(\"| Item | Δ_MH | SE | p-value | ETS |\")\n    w(\"|------|------|----|---------|-----|\")\n    for _, r in top20.iterrows():\n        p_str = f\"{r.p_value:.2e}\" if not np.isnan(r.p_value) else \"NaN\"\n        w(f\"| {r.item_id} | {r.delta_mh:+.3f} | {r.se:.3f} | {p_str} | {r.ets_class} |\")\n    w()\n\n    # Direction analysis\n    w(\"## 8. DIF Direction Analysis\")\n    w()\n    n_pos = (dif_std_sorted.delta_mh > 0).sum()\n    n_neg = (dif_std_sorted.delta_mh < 0).sum()\n    n_zero = (dif_std_sorted.delta_mh == 0).sum()\n    w(f\"- Positive Δ (favoring 2024): {n_pos} items ({n_pos/len(dif_std_sorted)*100:.1f}%)\")\n    w(f\"- Negative Δ (favoring 2023): {n_neg} items ({n_neg/len(dif_std_sorted)*100:.1f}%)\")\n    w(f\"- Zero Δ: {n_zero} items\")\n    w()\n\n    c_items = dif_std[dif_std.ets_class == \"C\"]\n    if len(c_items) > 0:\n        c_pos = (c_items.delta_mh > 0).sum()\n        c_neg = (c_items.delta_mh < 0).sum()\n        w(f\"Among ETS-C items: {c_pos} favor 2024, {c_neg} favor 2023\")\n    w()\n\n    report_text = \"\\n\".join(L) + \"\\n\"\n    (OUT / \"plan_004_step1_report.md\").write_text(report_text)\n\n    print(\"\\n\" + \"=\" * 60)\n    print(\"SUMMARY\")\n    print(\"=\" * 60)\n    for _, r in summary_df.iterrows():\n        print(f\"  {r.matching_type}: A={r.n_ets_a}, B={r.n_ets_b}, C={r.n_ets_c} ({r.pct_c:.1f}%)\")\n    print(f\"  Sanity random: {pct_c_san:.2f}% C\")\n    print(f\"\\nAll outputs saved to {OUT}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 503,
      "startLine": 1,
      "totalLines": 503
    }
  },
  "sourceToolAssistantUUID": "e8936ae6-1273-4cf4-a75b-8ee59b0128f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
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
  "lastPrompt": "## 任务：plan_004 Step 2 — GSM8K Semi-Synthetic Injection（复制 plan_011 方法）  **P0 紧急。** 在 GSM8K response matrix 上验证 DIF 方法论有效性。  ### 背景  Step 1 已完成：GSM8K temporal DIF 确认存在（standard 18.9% C, external 47.4%…",
  "leafUuid": "abe9bc77-63b5-4dd8-a3df-770b075f6d82",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "GSM8K semi-synthetic DIF injection validation",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5"
}
```

---

### Assistant

_source line 18 · 2026-05-21T00:54:02.282Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of both:
1. The plan_011 semi-synthetic injection methodology (MMLU-based)
2. The plan_004 step 1 code (GSM8K temporal DIF)

I need to create a GSM8K semi-synthetic injection script that:
- Uses the GSM8K response matrix from metabench CSV (not sparse npz)
- Uses temporal cohorts (ref=2023, foc=2024)
- Selects 20% of GSM8K items (~264) as contaminated


- Injects at multiple contamination levels with multiple seeds, computing detection metrics like TPR, FPR, and Fisher exact test
- Outputs dose-response and summary CSVs with a final report

The main adaptation from plan_011 is switching to CSV-based data loading aligned with step 1, using only temporal cohorts without ability stratification, and limiting matching variants to standard and external approaches.

For matching, I'm using GSM8K's purified total score as the standard variant and averaging the other four benchmarks (ARC, HellaSwag, TruthfulQA, Winogrande) as the external variant—this gives me two clean comparison points since the external benchmarks won't be affected by the GSM8K injection.

Now I'm ready to write the script: I'll load the GSM8K and external benchmark data, set up the temporal cohort with reference models from 2023 and focal models from 2024, select models with overlapping ability ranges for injection, and randomly choose 20% of items to contaminate.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abe9bc77-63b5-4dd8-a3df-770b075f6d82",
  "isSidechain": false,
  "requestId": "req_011CbEoPqCvhZTxqJRd4Skbf",
  "type": "assistant",
  "uuid": "34f6ca27-47df-49f0-99ab-eae98c6f2234",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XhGdo1sHnNoGAxxxqqQsFB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9239,
      "cache_read_input_tokens": 34577,
      "output_tokens": 900,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9239,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 900,
          "cache_read_input_tokens": 34577,
          "cache_creation_input_tokens": 9239,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9239
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

_source line 19 · 2026-05-21T00:54:02.293Z_

Now I have the complete reference code. Let me write the GSM8K semi-synthetic injection script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34f6ca27-47df-49f0-99ab-eae98c6f2234",
  "isSidechain": false,
  "requestId": "req_011CbEoPqCvhZTxqJRd4Skbf",
  "type": "assistant",
  "uuid": "f1a97133-6a7a-4938-b89d-9797de2af7a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XhGdo1sHnNoGAxxxqqQsFB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9239,
      "cache_read_input_tokens": 34577,
      "output_tokens": 900,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9239,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 900,
          "cache_read_input_tokens": 34577,
          "cache_creation_input_tokens": 9239,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9239
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

_source line 20 · 2026-05-21T00:54:04.292Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0135joWTxqoN7coMmJLw8k7k`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/",
  "description": "List existing plan_004 artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1a97133-6a7a-4938-b89d-9797de2af7a6",
  "isSidechain": false,
  "requestId": "req_011CbEoPqCvhZTxqJRd4Skbf",
  "type": "assistant",
  "uuid": "7ebc83f7-e0eb-44be-9875-b290f7606c40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XhGdo1sHnNoGAxxxqqQsFB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9239,
      "cache_read_input_tokens": 34577,
      "output_tokens": 900,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9239,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 900,
          "cache_read_input_tokens": 34577,
          "cache_creation_input_tokens": 9239,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9239
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

_source line 21 · 2026-05-21T00:54:04.380Z_

<details><summary>↩ Tool result · `toolu_0135joWTxqoN7coMmJLw8k7k`</summary>

```text
gsm8k_dif_results.csv
gsm8k_ets_summary.csv
plan_004_step1_gsm8k_temporal_dif.py
plan_004_step1_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ebc83f7-e0eb-44be-9875-b290f7606c40",
  "isSidechain": false,
  "promptId": "b681718f-ed7e-4c71-ace8-cbf70777063c",
  "type": "user",
  "uuid": "7f2f18c4-501c-45f3-901b-b36bbb2ccdb0",
  "toolUseResult": {
    "stdout": "gsm8k_dif_results.csv\ngsm8k_ets_summary.csv\nplan_004_step1_gsm8k_temporal_dif.py\nplan_004_step1_report.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7ebc83f7-e0eb-44be-9875-b290f7606c40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T00:55:54.808Z_

<details open><summary>🔧 Tool call — Write · `toolu_01SZgt1Wxfy9pjT8nfQp6pqq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_step2_gsm8k_semi_synthetic.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nplan_004_step2 — GSM8K Semi-Synthetic DIF Injection\n\nReplicates plan_011 methodology on GSM8K: inject known differential contamination\ninto real response data and test whether MH-DIF detects it.\n\nTwo matching variants:\n  - standard: purified GSM8K total score (contaminated by injection)\n  - external: average proportion correct on ARC+HellaSwag+TruthfulQA+Winogrande\n\nCohort: temporal, ref=2023, foc=2024\nInjection: 20% of GSM8K items, p ∈ {0.0, 0.3, 0.5, 0.7, 1.0}, 5 seeds\n\nInputs:\n  metabench_data/benchmark-data/gsm8k.csv\n  model_metadata.csv\n  metabench_data/benchmark-data/{arc,hellaswag,truthfulqa,winogrande}.csv\n\nOutputs (in plan_004/):\n  gsm8k_dose_response.csv, gsm8k_dose_response_summary.csv,\n  plan_004_step2_report.md\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.stats import chi2 as chi2_dist, fisher_exact\nfrom pathlib import Path\nimport time\nimport warnings\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\")\nBENCH_DIR = BASE / \"metabench_data\" / \"benchmark-data\"\nOUT = BASE / \"plan_004\"\nOUT.mkdir(exist_ok=True)\n\nINJECTION_PS = [0.0, 0.3, 0.5, 0.7, 1.0]\nN_SEEDS = 5\nCONTAM_FRAC = 0.20\n\nMH_VARIANTS = [\"standard\", \"external\"]\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MH-DIF CORE\n# ════════════════════════════════════════════════════════════════════════════\ndef _nan_row(j):\n    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,\n                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class=\"A\")\n\n\ndef mh_dif(X_ref, X_foc, n_strata=5,\n           external_scores_ref=None, external_scores_foc=None):\n    \"\"\"Purified Mantel-Haenszel DIF for all columns.\"\"\"\n    J = X_ref.shape[1]\n    use_external = external_scores_ref is not None\n\n    if not use_external:\n        tot_ref = X_ref.sum(axis=1).astype(np.float64)\n        tot_foc = X_foc.sum(axis=1).astype(np.float64)\n\n    rows = []\n    for j in range(J):\n        if use_external:\n            s_ref = external_scores_ref.astype(np.float64)\n            s_foc = external_scores_foc.astype(np.float64)\n        else:\n            s_ref = tot_ref - X_ref[:, j].astype(np.float64)\n            s_foc = tot_foc - X_foc[:, j].astype(np.float64)\n\n        s_all = np.concatenate([s_ref, s_foc])\n        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n        if len(edges) < 2:\n            rows.append(_nan_row(j))\n            continue\n        n_bins = len(edges) - 1\n\n        k_ref = np.digitize(s_ref, edges[1:-1])\n        k_foc = np.digitize(s_foc, edges[1:-1])\n\n        R = S = 0.0\n        sum_diff = 0.0\n        sum_var = 0.0\n        pr = ps_qr = qs = 0.0\n        n_ok = 0\n\n        for k in range(n_bins):\n            mr = (k_ref == k)\n            mf = (k_foc == k)\n            n1 = int(mr.sum())\n            n0 = int(mf.sum())\n            if n1 == 0 or n0 == 0:\n                continue\n\n            A = float(X_ref[mr, j].sum())\n            B = float(n1 - A)\n            C = float(X_foc[mf, j].sum())\n            D = float(n0 - C)\n            Nk = float(n1 + n0)\n            m1 = A + C\n            m0 = B + D\n\n            if m1 == 0 or m0 == 0 or Nk <= 1:\n                continue\n            n_ok += 1\n\n            Rk = A * D / Nk\n            Sk = B * C / Nk\n            R += Rk\n            S += Sk\n\n            EA = n1 * m1 / Nk\n            sum_diff += A - EA\n            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n            Pk = (A + D) / Nk\n            Qk = (B + C) / Nk\n            pr += Pk * Rk\n            ps_qr += Pk * Sk + Qk * Rk\n            qs += Qk * Sk\n\n        if n_ok == 0 or (R == 0 and S == 0):\n            rows.append(_nan_row(j))\n            continue\n\n        if S == 0:\n            alpha, delta, se = np.inf, -np.inf, np.nan\n        elif R == 0:\n            alpha, delta, se = 0.0, np.inf, np.nan\n        else:\n            alpha = R / S\n            delta = -2.35 * np.log(alpha)\n            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)\n            se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n        if sum_var > 0:\n            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n        else:\n            chi2_stat = pval = np.nan\n\n        ad = abs(delta) if np.isfinite(delta) else 999.0\n        if ad < 1.0:\n            ets = \"A\"\n        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n            ets = \"C\"\n        else:\n            ets = \"B\"\n\n        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,\n                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets))\n\n    return pd.DataFrame(rows)\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  DATA LOADING\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"=== Loading GSM8K data ===\")\nt0 = time.time()\ngsm = pd.read_csv(BENCH_DIR / \"gsm8k.csv\")\ngsm[\"correct\"] = gsm[\"correct\"].map({\"True\": 1, \"False\": 0, True: 1, False: 0}).astype(np.int8)\ngsm_pivot = gsm.pivot(index=\"source\", columns=\"item\", values=\"correct\")\ngsm_pivot = gsm_pivot.fillna(0).astype(np.int8)\n\nMODEL_NAMES = np.array(gsm_pivot.index.tolist())\nITEM_IDS = np.array(gsm_pivot.columns.tolist())\nX_full = gsm_pivot.values\nN_MODELS, J_TOTAL = X_full.shape\nprint(f\"  Response matrix: {N_MODELS} × {J_TOTAL}\")\ndel gsm, gsm_pivot\n\nNAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}\nN_CONTAMINATED = int(round(J_TOTAL * CONTAM_FRAC))\nN_CLEAN = J_TOTAL - N_CONTAMINATED\nprint(f\"  Contaminated items: {N_CONTAMINATED} ({CONTAM_FRAC*100:.0f}%), clean: {N_CLEAN}\")\n\n# Model metadata\nmodel_meta = pd.read_csv(BASE / \"model_metadata.csv\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  EXTERNAL MATCHING SCORES\n# ════════════════════════════════════════════════════════════════════════════\ndef compute_benchmark_scores(filepath, benchmark_name):\n    \"\"\"Compute per-model proportion correct from a benchmark CSV.\"\"\"\n    print(f\"  Loading {benchmark_name}...\")\n    t0b = time.time()\n    scores = {}\n    counts = {}\n    for chunk in pd.read_csv(filepath, chunksize=500_000):\n        chunk[\"correct\"] = chunk[\"correct\"].map({\"True\": 1, \"False\": 0, True: 1, False: 0})\n        grouped = chunk.groupby(\"source\")[\"correct\"].agg([\"sum\", \"count\"])\n        for model, row in grouped.iterrows():\n            if model in scores:\n                scores[model] += row[\"sum\"]\n                counts[model] += row[\"count\"]\n            else:\n                scores[model] = row[\"sum\"]\n                counts[model] = row[\"count\"]\n    result = {m: scores[m] / counts[m] for m in scores if counts[m] > 0}\n    print(f\"    {benchmark_name}: {len(result)} models, {time.time()-t0b:.1f}s\")\n    return result\n\n\nprint(\"\\n=== Computing external matching scores ===\")\next_benchmarks = [\"arc\", \"hellaswag\", \"truthfulqa\", \"winogrande\"]\next_scores_raw = {}\nfor bm in ext_benchmarks:\n    ext_scores_raw[bm] = compute_benchmark_scores(BENCH_DIR / f\"{bm}.csv\", bm)\n\next_combined = {}\nfor model in MODEL_NAMES:\n    bm_scores = [ext_scores_raw[bm][model] for bm in ext_benchmarks if model in ext_scores_raw[bm]]\n    if len(bm_scores) >= 2:\n        ext_combined[model] = np.mean(bm_scores)\nprint(f\"  Models with external scores (≥2 benchmarks): {len(ext_combined)}\")\ndel ext_scores_raw\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  COHORT CONSTRUCTION\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Cohort construction ===\")\n\n\ndef rows_for(col, values):\n    names = model_meta.loc[model_meta[col].isin(values), \"model_name\"]\n    return np.array([NAME2ROW[n] for n in names if n in NAME2ROW])\n\n\nref_idx = rows_for(\"cohort_temporal\", [\"2023\"])\nfoc_idx = rows_for(\"cohort_temporal\", [\"2024\"])\nprint(f\"  Temporal: ref=2023 (N={len(ref_idx)}), foc=2024 (N={len(foc_idx)})\")\n\n# External subset: models with external scores\nref_names_ext = [MODEL_NAMES[i] for i in ref_idx if MODEL_NAMES[i] in ext_combined]\nfoc_names_ext = [MODEL_NAMES[i] for i in foc_idx if MODEL_NAMES[i] in ext_combined]\nref_idx_ext = np.array([NAME2ROW[n] for n in ref_names_ext])\nfoc_idx_ext = np.array([NAME2ROW[n] for n in foc_names_ext])\nprint(f\"  External subset: ref (N={len(ref_idx_ext)}), foc (N={len(foc_idx_ext)})\")\n\n# Focal injection subset: models with accuracy overlap with ref\ngsm8k_acc = X_full.mean(axis=1)\nref_acc = gsm8k_acc[ref_idx]\nfoc_acc = gsm8k_acc[foc_idx]\noverlap_min = max(ref_acc.min(), foc_acc.min())\noverlap_max = min(ref_acc.max(), foc_acc.max())\n\nif overlap_min <= overlap_max:\n    foc_inject_mask = np.array([(gsm8k_acc[i] >= overlap_min) and (gsm8k_acc[i] <= overlap_max)\n                                 for i in foc_idx])\n    foc_inject_idx = foc_idx[foc_inject_mask]\nelse:\n    foc_inject_idx = foc_idx.copy()\n\n# Same for external subset\nif overlap_min <= overlap_max:\n    foc_inject_ext_mask = np.array([(gsm8k_acc[i] >= overlap_min) and (gsm8k_acc[i] <= overlap_max)\n                                     for i in foc_idx_ext])\n    foc_inject_idx_ext = foc_idx_ext[foc_inject_ext_mask]\nelse:\n    foc_inject_idx_ext = foc_idx_ext.copy()\n\nprint(f\"  Accuracy overlap: [{overlap_min:.4f}, {overlap_max:.4f}]\")\nprint(f\"  Focal inject (standard): {len(foc_inject_idx)} models\")\nprint(f\"  Focal inject (external): {len(foc_inject_idx_ext)} models\")\n\n# Precompute external scores arrays\next_ref_scores = np.array([ext_combined[MODEL_NAMES[i]] for i in ref_idx_ext])\next_foc_scores = np.array([ext_combined[MODEL_NAMES[i]] for i in foc_idx_ext])\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  INJECTION + MH-DIF\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Injection + MH-DIF ===\")\n\ntotal_runs = len(INJECTION_PS) * N_SEEDS * len(MH_VARIANTS)\nrun_count = 0\nt_start = time.time()\n\ninjection_rows = []\n\nfor p in INJECTION_PS:\n    for seed in range(1, N_SEEDS + 1):\n        rng = np.random.RandomState(seed)\n\n        contam_local_idx = rng.choice(J_TOTAL, N_CONTAMINATED, replace=False)\n        contam_set = set(contam_local_idx.tolist())\n        clean_local_idx = np.array([i for i in range(J_TOTAL) if i not in contam_set])\n\n        X_inj = X_full.copy()\n        n_flipped = 0\n\n        if p > 0:\n            for local_j in contam_local_idx:\n                for model_row in foc_inject_idx:\n                    if X_inj[model_row, local_j] == 0:\n                        if rng.random() < p:\n                            X_inj[model_row, local_j] = 1\n                            n_flipped += 1\n\n        orig_density = X_full[np.ix_(foc_inject_idx, contam_local_idx)].mean()\n        new_density = X_inj[np.ix_(foc_inject_idx, contam_local_idx)].mean()\n\n        for variant in MH_VARIANTS:\n            run_count += 1\n\n            if variant == \"standard\":\n                X_ref_v = X_inj[ref_idx]\n                X_foc_v = X_inj[foc_idx]\n                dif_results = mh_dif(X_ref_v, X_foc_v, n_strata=5)\n            else:\n                X_ref_v = X_inj[ref_idx_ext]\n                X_foc_v = X_inj[foc_idx_ext]\n                dif_results = mh_dif(X_ref_v, X_foc_v, n_strata=5,\n                                     external_scores_ref=ext_ref_scores,\n                                     external_scores_foc=ext_foc_scores)\n\n            contam_mask = dif_results[\"col_idx\"].isin(contam_set)\n            contam_results = dif_results[contam_mask]\n            clean_results = dif_results[~contam_mask]\n\n            n_c_contam = (contam_results[\"ets_class\"] == \"C\").sum()\n            n_c_clean = (clean_results[\"ets_class\"] == \"C\").sum()\n            tpr = n_c_contam / N_CONTAMINATED\n            fpr = n_c_clean / N_CLEAN\n\n            table = [[n_c_contam, N_CONTAMINATED - n_c_contam],\n                     [n_c_clean, N_CLEAN - n_c_clean]]\n            fisher_or, fisher_p = fisher_exact(table)\n\n            injection_rows.append(dict(\n                p=p, seed=seed, matching_type=variant,\n                n_items=J_TOTAL, n_contaminated=N_CONTAMINATED, n_clean=N_CLEAN,\n                n_ref=len(ref_idx) if variant == \"standard\" else len(ref_idx_ext),\n                n_foc=len(foc_idx) if variant == \"standard\" else len(foc_idx_ext),\n                n_foc_inject=len(foc_inject_idx) if variant == \"standard\" else len(foc_inject_idx_ext),\n                tpr=tpr, fpr=fpr,\n                n_c_contam=n_c_contam, n_c_clean=n_c_clean,\n                fisher_or=fisher_or, fisher_p=fisher_p,\n                n_responses_flipped=n_flipped,\n                orig_density=orig_density, new_density=new_density,\n            ))\n\n            elapsed = time.time() - t_start\n            print(f\"  [{run_count}/{total_runs}] {variant:8s} p={p} seed={seed}: \"\n                  f\"TPR={tpr:.3f} FPR={fpr:.3f} flipped={n_flipped} ({elapsed:.0f}s)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  AGGREGATE & SAVE\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Aggregating results ===\")\n\ninj_df = pd.DataFrame(injection_rows)\ninj_df.to_csv(OUT / \"gsm8k_dose_response.csv\", index=False)\nprint(f\"  Saved gsm8k_dose_response.csv ({len(inj_df)} rows)\")\n\nsummary_rows = []\nfor (p_val, variant), grp in inj_df.groupby([\"p\", \"matching_type\"]):\n    base_grp = inj_df[(inj_df[\"p\"] == 0.0) & (inj_df[\"matching_type\"] == variant)]\n    base_tpr = base_grp[\"tpr\"].mean()\n    summary_rows.append(dict(\n        p=p_val, matching_type=variant,\n        tpr_mean=grp[\"tpr\"].mean(), tpr_std=grp[\"tpr\"].std(),\n        fpr_mean=grp[\"fpr\"].mean(), fpr_std=grp[\"fpr\"].std(),\n        delta_tpr=grp[\"tpr\"].mean() - base_tpr,\n        fisher_or_mean=grp[\"fisher_or\"].mean(),\n        fisher_p_median=grp[\"fisher_p\"].median(),\n        n_flipped_mean=grp[\"n_responses_flipped\"].mean(),\n    ))\nsummary_df = pd.DataFrame(summary_rows)\nsummary_df.to_csv(OUT / \"gsm8k_dose_response_summary.csv\", index=False)\nprint(f\"  Saved gsm8k_dose_response_summary.csv ({len(summary_df)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  REPORT\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Generating report ===\")\n\nL = []\ndef w(s=\"\"):\n    L.append(s)\n\nw(\"# Plan 004 Step 2: GSM8K Semi-Synthetic DIF Injection\")\nw()\nw(\"## 1. Objective\")\nw()\nw(\"Inject known differential contamination into GSM8K response data and test whether\")\nw(\"MH-DIF detects it. Validates that the DIF methodology works on GSM8K (single-domain,\")\nw(\"math benchmark) and enables comparison with MMLU results from plan_011.\")\nw()\n\nw(\"## 2. Setup\")\nw()\nw(f\"- **Benchmark**: GSM8K ({J_TOTAL} items)\")\nw(f\"- **Contaminated items**: {N_CONTAMINATED} ({CONTAM_FRAC*100:.0f}% of {J_TOTAL})\")\nw(f\"- **Injection probabilities**: {INJECTION_PS}\")\nw(f\"- **Seeds per p-level**: {N_SEEDS}\")\nw(f\"- **Cohort**: temporal, ref=2023 (N={len(ref_idx)}), foc=2024 (N={len(foc_idx)})\")\nw(f\"- **External cohort**: ref (N={len(ref_idx_ext)}), foc (N={len(foc_idx_ext)})\")\nw(f\"- **Focal inject (standard)**: {len(foc_inject_idx)} models in accuracy overlap [{overlap_min:.4f}, {overlap_max:.4f}]\")\nw(f\"- **Focal inject (external)**: {len(foc_inject_idx_ext)} models\")\nw()\n\nw(\"### Matching variants\")\nw()\nw(\"| Variant | Matching variable | Properties |\")\nw(\"|---------|-------------------|------------|\")\nw(\"| standard | purified GSM8K total score | Contaminated by injection (20% items affected) |\")\nw(\"| external | avg proportion correct on ARC+HellaSwag+TruthfulQA+Winogrande | Immune to GSM8K injection |\")\nw()\n\nw(\"## 3. Dose-Response Results\")\nw()\nfor variant in MH_VARIANTS:\n    w(f\"### {variant.capitalize()} matching\")\n    w()\n    w(\"| p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |\")\n    w(\"|---|----------------|----------------|------|-----------|----------|\")\n    sub = summary_df[summary_df[\"matching_type\"] == variant].sort_values(\"p\")\n    for _, r in sub.iterrows():\n        w(f\"| {r.p} | {r.tpr_mean:.3f}±{r.tpr_std:.3f} | \"\n          f\"{r.fpr_mean:.3f}±{r.fpr_std:.3f} | {r.delta_tpr:+.3f} | \"\n          f\"{r.fisher_or_mean:.2f} | {r.fisher_p_median:.4f} |\")\n    w()\n\nw(\"## 4. Comparison with MMLU (plan_011)\")\nw()\nw(\"| Metric | MMLU plan_011 (external) | GSM8K (external) |\")\nw(\"|--------|--------------------------|------------------|\")\n\next_sub = summary_df[summary_df[\"matching_type\"] == \"external\"]\next_p0 = ext_sub[ext_sub[\"p\"] == 0.0]\next_p05 = ext_sub[ext_sub[\"p\"] == 0.5]\next_p1 = ext_sub[ext_sub[\"p\"] == 1.0]\n\nmmlu_baseline_fpr = 0.314\nmmlu_dtpr_05 = 0.508\nmmlu_dtpr_10 = 0.674\n\ngsm_fpr0 = ext_p0.iloc[0][\"fpr_mean\"] if len(ext_p0) > 0 else np.nan\ngsm_dtpr05 = ext_p05.iloc[0][\"delta_tpr\"] if len(ext_p05) > 0 else np.nan\ngsm_dtpr10 = ext_p1.iloc[0][\"delta_tpr\"] if len(ext_p1) > 0 else np.nan\n\nw(f\"| Baseline FPR (p=0) | {mmlu_baseline_fpr:.3f} | {gsm_fpr0:.3f} |\")\nw(f\"| ΔTPR at p=0.5 | +{mmlu_dtpr_05:.3f} | {gsm_dtpr05:+.3f} |\")\nw(f\"| ΔTPR at p=1.0 | +{mmlu_dtpr_10:.3f} | {gsm_dtpr10:+.3f} |\")\nw(f\"| Items | 500 (subset) | {J_TOTAL} (all) |\")\nw(f\"| Contaminated | 100 (20%) | {N_CONTAMINATED} (~20%) |\")\nw()\n\nw(\"## 5. Standard vs External Matching\")\nw()\nw(\"| p | Standard TPR | External TPR | Standard FPR | External FPR |\")\nw(\"|---|-------------|-------------|-------------|-------------|\")\nfor p_val in INJECTION_PS:\n    std_r = summary_df[(summary_df[\"p\"] == p_val) & (summary_df[\"matching_type\"] == \"standard\")]\n    ext_r = summary_df[(summary_df[\"p\"] == p_val) & (summary_df[\"matching_type\"] == \"external\")]\n    if len(std_r) > 0 and len(ext_r) > 0:\n        w(f\"| {p_val} | {std_r.iloc[0].tpr_mean:.3f} | {ext_r.iloc[0].tpr_mean:.3f} | \"\n          f\"{std_r.iloc[0].fpr_mean:.3f} | {ext_r.iloc[0].fpr_mean:.3f} |\")\nw()\n\nw(\"## 6. Density Changes\")\nw()\nw(\"| p | Orig density | Post density | Responses flipped |\")\nw(\"|---|-------------|-------------|-------------------|\")\nfor p_val in INJECTION_PS:\n    if p_val == 0:\n        continue\n    sub = inj_df[(inj_df[\"p\"] == p_val) & (inj_df[\"matching_type\"] == \"standard\")]\n    if len(sub) > 0:\n        w(f\"| {p_val} | {sub.orig_density.mean():.4f} | {sub.new_density.mean():.4f} | \"\n          f\"{sub.n_responses_flipped.mean():.0f} |\")\nw()\n\nw(\"## 7. Verdict\")\nw()\n\nfor variant in MH_VARIANTS:\n    sub = summary_df[summary_df[\"matching_type\"] == variant]\n    p0 = sub[sub[\"p\"] == 0.0]\n    p1 = sub[sub[\"p\"] == 1.0]\n    if len(p0) == 0 or len(p1) == 0:\n        continue\n    tpr0 = p0.iloc[0][\"tpr_mean\"]\n    fpr0 = p0.iloc[0][\"fpr_mean\"]\n    tpr1 = p1.iloc[0][\"tpr_mean\"]\n    fpr1 = p1.iloc[0][\"fpr_mean\"]\n    d_tpr = tpr1 - tpr0\n\n    w(f\"### {variant.capitalize()} matching\")\n    w()\n    w(f\"- Baseline (p=0): TPR={tpr0:.3f}, FPR={fpr0:.3f}\")\n    w(f\"- Full injection (p=1): TPR={tpr1:.3f}, FPR={fpr1:.3f}\")\n    w(f\"- ΔTPR = {d_tpr:+.3f}\")\n    w()\n\n    if d_tpr > 0.3 and tpr1 > 0.5:\n        w(f\"**SUCCESS**: injection raises TPR by {d_tpr:.3f} with clear dose-response.\")\n    elif d_tpr > 0.1:\n        w(f\"**PARTIAL**: detectable signal (ΔTPR={d_tpr:.3f}) but modest.\")\n    else:\n        w(f\"**FAIL**: ΔTPR={d_tpr:.3f} too small to indicate reliable detection.\")\n    w()\n\nw(\"## 8. Implications\")\nw()\nw(\"### Cross-benchmark generalization\")\nw()\nw(\"If GSM8K semi-synthetic results are comparable to MMLU plan_011, this confirms\")\nw(\"MH-DIF methodology generalizes beyond MMLU to single-domain math benchmarks.\")\nw()\nw(\"### Matching variable contamination\")\nw()\nw(\"Standard matching uses GSM8K total score, which is corrupted when 20% of items\")\nw(\"are injected. This should inflate FPR compared to external matching.\")\nw(\"External matching (other benchmarks) is immune to GSM8K injection and should\")\nw(\"provide cleaner separation between contaminated and clean items.\")\nw()\n\nreport_text = \"\\n\".join(L) + \"\\n\"\n(OUT / \"plan_004_step2_report.md\").write_text(report_text)\nprint(\"  Report written.\")\n\n# Console summary\nprint(\"\\n\" + \"=\" * 60)\nprint(\"SUMMARY\")\nprint(\"=\" * 60)\nfor variant in MH_VARIANTS:\n    print(f\"\\n--- {variant} matching ---\")\n    sub = summary_df[summary_df[\"matching_type\"] == variant].sort_values(\"p\")\n    for _, r in sub.iterrows():\n        print(f\"  p={r.p}: TPR={r.tpr_mean:.3f}±{r.tpr_std:.3f}  \"\n              f\"FPR={r.fpr_mean:.3f}±{r.fpr_std:.3f}  ΔTPR={r.delta_tpr:+.3f}\")\n\ntotal_elapsed = time.time() - t_start\nprint(f\"\\nTotal time: {total_elapsed:.0f}s\")\nprint(f\"All outputs saved to {OUT}\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f2f18c4-501c-45f3-901b-b36bbb2ccdb0",
  "isSidechain": false,
  "requestId": "req_011CbEoRWLvAe5PRo7xH5mDK",
  "type": "assistant",
  "uuid": "10bb8829-7d0d-4a1f-923a-356d808d20f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PnuhdWGkXocKPRqdwQZpDx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 964,
      "cache_read_input_tokens": 43816,
      "output_tokens": 8089,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 964,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8089,
          "cache_read_input_tokens": 43816,
          "cache_creation_input_tokens": 964,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 964
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

_source line 23 · 2026-05-21T00:55:54.837Z_

<details><summary>↩ Tool result · `toolu_01SZgt1Wxfy9pjT8nfQp6pqq`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_step2_gsm8k_semi_synthetic.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10bb8829-7d0d-4a1f-923a-356d808d20f9",
  "isSidechain": false,
  "promptId": "b681718f-ed7e-4c71-ace8-cbf70777063c",
  "type": "user",
  "uuid": "3de792de-59b2-48fa-b870-d55b70c5a9ea",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_step2_gsm8k_semi_synthetic.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nplan_004_step2 — GSM8K Semi-Synthetic DIF Injection\n\nReplicates plan_011 methodology on GSM8K: inject known differential contamination\ninto real response data and test whether MH-DIF detects it.\n\nTwo matching variants:\n  - standard: purified GSM8K total score (contaminated by injection)\n  - external: average proportion correct on ARC+HellaSwag+TruthfulQA+Winogrande\n\nCohort: temporal, ref=2023, foc=2024\nInjection: 20% of GSM8K items, p ∈ {0.0, 0.3, 0.5, 0.7, 1.0}, 5 seeds\n\nInputs:\n  metabench_data/benchmark-data/gsm8k.csv\n  model_metadata.csv\n  metabench_data/benchmark-data/{arc,hellaswag,truthfulqa,winogrande}.csv\n\nOutputs (in plan_004/):\n  gsm8k_dose_response.csv, gsm8k_dose_response_summary.csv,\n  plan_004_step2_report.md\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.stats import chi2 as chi2_dist, fisher_exact\nfrom pathlib import Path\nimport time\nimport warnings\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\")\nBENCH_DIR = BASE / \"metabench_data\" / \"benchmark-data\"\nOUT = BASE / \"plan_004\"\nOUT.mkdir(exist_ok=True)\n\nINJECTION_PS = [0.0, 0.3, 0.5, 0.7, 1.0]\nN_SEEDS = 5\nCONTAM_FRAC = 0.20\n\nMH_VARIANTS = [\"standard\", \"external\"]\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MH-DIF CORE\n# ════════════════════════════════════════════════════════════════════════════\ndef _nan_row(j):\n    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,\n                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class=\"A\")\n\n\ndef mh_dif(X_ref, X_foc, n_strata=5,\n           external_scores_ref=None, external_scores_foc=None):\n    \"\"\"Purified Mantel-Haenszel DIF for all columns.\"\"\"\n    J = X_ref.shape[1]\n    use_external = external_scores_ref is not None\n\n    if not use_external:\n        tot_ref = X_ref.sum(axis=1).astype(np.float64)\n        tot_foc = X_foc.sum(axis=1).astype(np.float64)\n\n    rows = []\n    for j in range(J):\n        if use_external:\n            s_ref = external_scores_ref.astype(np.float64)\n            s_foc = external_scores_foc.astype(np.float64)\n        else:\n            s_ref = tot_ref - X_ref[:, j].astype(np.float64)\n            s_foc = tot_foc - X_foc[:, j].astype(np.float64)\n\n        s_all = np.concatenate([s_ref, s_foc])\n        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n        if len(edges) < 2:\n            rows.append(_nan_row(j))\n            continue\n        n_bins = len(edges) - 1\n\n        k_ref = np.digitize(s_ref, edges[1:-1])\n        k_foc = np.digitize(s_foc, edges[1:-1])\n\n        R = S = 0.0\n        sum_diff = 0.0\n        sum_var = 0.0\n        pr = ps_qr = qs = 0.0\n        n_ok = 0\n\n        for k in range(n_bins):\n            mr = (k_ref == k)\n            mf = (k_foc == k)\n            n1 = int(mr.sum())\n            n0 = int(mf.sum())\n            if n1 == 0 or n0 == 0:\n                continue\n\n            A = float(X_ref[mr, j].sum())\n            B = float(n1 - A)\n            C = float(X_foc[mf, j].sum())\n            D = float(n0 - C)\n            Nk = float(n1 + n0)\n            m1 = A + C\n            m0 = B + D\n\n            if m1 == 0 or m0 == 0 or Nk <= 1:\n                continue\n            n_ok += 1\n\n            Rk = A * D / Nk\n            Sk = B * C / Nk\n            R += Rk\n            S += Sk\n\n            EA = n1 * m1 / Nk\n            sum_diff += A - EA\n            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n            Pk = (A + D) / Nk\n            Qk = (B + C) / Nk\n            pr += Pk * Rk\n            ps_qr += Pk * Sk + Qk * Rk\n            qs += Qk * Sk\n\n        if n_ok == 0 or (R == 0 and S == 0):\n            rows.append(_nan_row(j))\n            continue\n\n        if S == 0:\n            alpha, delta, se = np.inf, -np.inf, np.nan\n        elif R == 0:\n            alpha, delta, se = 0.0, np.inf, np.nan\n        else:\n            alpha = R / S\n            delta = -2.35 * np.log(alpha)\n            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)\n            se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n        if sum_var > 0:\n            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n        else:\n            chi2_stat = pval = np.nan\n\n        ad = abs(delta) if np.isfinite(delta) else 999.0\n        if ad < 1.0:\n            ets = \"A\"\n        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n            ets = \"C\"\n        else:\n            ets = \"B\"\n\n        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,\n                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets))\n\n    return pd.DataFrame(rows)\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  DATA LOADING\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"=== Loading GSM8K data ===\")\nt0 = time.time()\ngsm = pd.read_csv(BENCH_DIR / \"gsm8k.csv\")\ngsm[\"correct\"] = gsm[\"correct\"].map({\"True\": 1, \"False\": 0, True: 1, False: 0}).astype(np.int8)\ngsm_pivot = gsm.pivot(index=\"source\", columns=\"item\", values=\"correct\")\ngsm_pivot = gsm_pivot.fillna(0).astype(np.int8)\n\nMODEL_NAMES = np.array(gsm_pivot.index.tolist())\nITEM_IDS = np.array(gsm_pivot.columns.tolist())\nX_full = gsm_pivot.values\nN_MODELS, J_TOTAL = X_full.shape\nprint(f\"  Response matrix: {N_MODELS} × {J_TOTAL}\")\ndel gsm, gsm_pivot\n\nNAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}\nN_CONTAMINATED = int(round(J_TOTAL * CONTAM_FRAC))\nN_CLEAN = J_TOTAL - N_CONTAMINATED\nprint(f\"  Contaminated items: {N_CONTAMINATED} ({CONTAM_FRAC*100:.0f}%), clean: {N_CLEAN}\")\n\n# Model metadata\nmodel_meta = pd.read_csv(BASE / \"model_metadata.csv\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  EXTERNAL MATCHING SCORES\n# ════════════════════════════════════════════════════════════════════════════\ndef compute_benchmark_scores(filepath, benchmark_name):\n    \"\"\"Compute per-model proportion correct from a benchmark CSV.\"\"\"\n    print(f\"  Loading {benchmark_name}...\")\n    t0b = time.time()\n    scores = {}\n    counts = {}\n    for chunk in pd.read_csv(filepath, chunksize=500_000):\n        chunk[\"correct\"] = chunk[\"correct\"].map({\"True\": 1, \"False\": 0, True: 1, False: 0})\n        grouped = chunk.groupby(\"source\")[\"correct\"].agg([\"sum\", \"count\"])\n        for model, row in grouped.iterrows():\n            if model in scores:\n                scores[model] += row[\"sum\"]\n                counts[model] += row[\"count\"]\n            else:\n                scores[model] = row[\"sum\"]\n                counts[model] = row[\"count\"]\n    result = {m: scores[m] / counts[m] for m in scores if counts[m] > 0}\n    print(f\"    {benchmark_name}: {len(result)} models, {time.time()-t0b:.1f}s\")\n    return result\n\n\nprint(\"\\n=== Computing external matching scores ===\")\next_benchmarks = [\"arc\", \"hellaswag\", \"truthfulqa\", \"winogrande\"]\next_scores_raw = {}\nfor bm in ext_benchmarks:\n    ext_scores_raw[bm] = compute_benchmark_scores(BENCH_DIR / f\"{bm}.csv\", bm)\n\next_combined = {}\nfor model in MODEL_NAMES:\n    bm_scores = [ext_scores_raw[bm][model] for bm in ext_benchmarks if model in ext_scores_raw[bm]]\n    if len(bm_scores) >= 2:\n        ext_combined[model] = np.mean(bm_scores)\nprint(f\"  Models with external scores (≥2 benchmarks): {len(ext_combined)}\")\ndel ext_scores_raw\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  COHORT CONSTRUCTION\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Cohort construction ===\")\n\n\ndef rows_for(col, values):\n    names = model_meta.loc[model_meta[col].isin(values), \"model_name\"]\n    return np.array([NAME2ROW[n] for n in names if n in NAME2ROW])\n\n\nref_idx = rows_for(\"cohort_temporal\", [\"2023\"])\nfoc_idx = rows_for(\"cohort_temporal\", [\"2024\"])\nprint(f\"  Temporal: ref=2023 (N={len(ref_idx)}), foc=2024 (N={len(foc_idx)})\")\n\n# External subset: models with external scores\nref_names_ext = [MODEL_NAMES[i] for i in ref_idx if MODEL_NAMES[i] in ext_combined]\nfoc_names_ext = [MODEL_NAMES[i] for i in foc_idx if MODEL_NAMES[i] in ext_combined]\nref_idx_ext = np.array([NAME2ROW[n] for n in ref_names_ext])\nfoc_idx_ext = np.array([NAME2ROW[n] for n in foc_names_ext])\nprint(f\"  External subset: ref (N={len(ref_idx_ext)}), foc (N={len(foc_idx_ext)})\")\n\n# Focal injection subset: models with accuracy overlap with ref\ngsm8k_acc = X_full.mean(axis=1)\nref_acc = gsm8k_acc[ref_idx]\nfoc_acc = gsm8k_acc[foc_idx]\noverlap_min = max(ref_acc.min(), foc_acc.min())\noverlap_max = min(ref_acc.max(), foc_acc.max())\n\nif overlap_min <= overlap_max:\n    foc_inject_mask = np.array([(gsm8k_acc[i] >= overlap_min) and (gsm8k_acc[i] <= overlap_max)\n                                 for i in foc_idx])\n    foc_inject_idx = foc_idx[foc_inject_mask]\nelse:\n    foc_inject_idx = foc_idx.copy()\n\n# Same for external subset\nif overlap_min <= overlap_max:\n    foc_inject_ext_mask = np.array([(gsm8k_acc[i] >= overlap_min) and (gsm8k_acc[i] <= overlap_max)\n                                     for i in foc_idx_ext])\n    foc_inject_idx_ext = foc_idx_ext[foc_inject_ext_mask]\nelse:\n    foc_inject_idx_ext = foc_idx_ext.copy()\n\nprint(f\"  Accuracy overlap: [{overlap_min:.4f}, {overlap_max:.4f}]\")\nprint(f\"  Focal inject (standard): {len(foc_inject_idx)} models\")\nprint(f\"  Focal inject (external): {len(foc_inject_idx_ext)} models\")\n\n# Precompute external scores arrays\next_ref_scores = np.array([ext_combined[MODEL_NAMES[i]] for i in ref_idx_ext])\next_foc_scores = np.array([ext_combined[MODEL_NAMES[i]] for i in foc_idx_ext])\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  INJECTION + MH-DIF\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Injection + MH-DIF ===\")\n\ntotal_runs = len(INJECTION_PS) * N_SEEDS * len(MH_VARIANTS)\nrun_count = 0\nt_start = time.time()\n\ninjection_rows = []\n\nfor p in INJECTION_PS:\n    for seed in range(1, N_SEEDS + 1):\n        rng = np.random.RandomState(seed)\n\n        contam_local_idx = rng.choice(J_TOTAL, N_CONTAMINATED, replace=False)\n        contam_set = set(contam_local_idx.tolist())\n        clean_local_idx = np.array([i for i in range(J_TOTAL) if i not in contam_set])\n\n        X_inj = X_full.copy()\n        n_flipped = 0\n\n        if p > 0:\n            for local_j in contam_local_idx:\n                for model_row in foc_inject_idx:\n                    if X_inj[model_row, local_j] == 0:\n                        if rng.random() < p:\n                            X_inj[model_row, local_j] = 1\n                            n_flipped += 1\n\n        orig_density = X_full[np.ix_(foc_inject_idx, contam_local_idx)].mean()\n        new_density = X_inj[np.ix_(foc_inject_idx, contam_local_idx)].mean()\n\n        for variant in MH_VARIANTS:\n            run_count += 1\n\n            if variant == \"standard\":\n                X_ref_v = X_inj[ref_idx]\n                X_foc_v = X_inj[foc_idx]\n                dif_results = mh_dif(X_ref_v, X_foc_v, n_strata=5)\n            else:\n                X_ref_v = X_inj[ref_idx_ext]\n                X_foc_v = X_inj[foc_idx_ext]\n                dif_results = mh_dif(X_ref_v, X_foc_v, n_strata=5,\n                                     external_scores_ref=ext_ref_scores,\n                                     external_scores_foc=ext_foc_scores)\n\n            contam_mask = dif_results[\"col_idx\"].isin(contam_set)\n            contam_results = dif_results[contam_mask]\n            clean_results = dif_results[~contam_mask]\n\n            n_c_contam = (contam_results[\"ets_class\"] == \"C\").sum()\n            n_c_clean = (clean_results[\"ets_class\"] == \"C\").sum()\n            tpr = n_c_contam / N_CONTAMINATED\n            fpr = n_c_clean / N_CLEAN\n\n            table = [[n_c_contam, N_CONTAMINATED - n_c_contam],\n                     [n_c_clean, N_CLEAN - n_c_clean]]\n            fisher_or, fisher_p = fisher_exact(table)\n\n            injection_rows.append(dict(\n                p=p, seed=seed, matching_type=variant,\n                n_items=J_TOTAL, n_contaminated=N_CONTAMINATED, n_clean=N_CLEAN,\n                n_ref=len(ref_idx) if variant == \"standard\" else len(ref_idx_ext),\n                n_foc=len(foc_idx) if variant == \"standard\" else len(foc_idx_ext),\n                n_foc_inject=len(foc_inject_idx) if variant == \"standard\" else len(foc_inject_idx_ext),\n                tpr=tpr, fpr=fpr,\n                n_c_contam=n_c_contam, n_c_clean=n_c_clean,\n                fisher_or=fisher_or, fisher_p=fisher_p,\n                n_responses_flipped=n_flipped,\n                orig_density=orig_density, new_density=new_density,\n            ))\n\n            elapsed = time.time() - t_start\n            print(f\"  [{run_count}/{total_runs}] {variant:8s} p={p} seed={seed}: \"\n                  f\"TPR={tpr:.3f} FPR={fpr:.3f} flipped={n_flipped} ({elapsed:.0f}s)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  AGGREGATE & SAVE\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Aggregating results ===\")\n\ninj_df = pd.DataFrame(injection_rows)\ninj_df.to_csv(OUT / \"gsm8k_dose_response.csv\", index=False)\nprint(f\"  Saved gsm8k_dose_response.csv ({len(inj_df)} rows)\")\n\nsummary_rows = []\nfor (p_val, variant), grp in inj_df.groupby([\"p\", \"matching_type\"]):\n    base_grp = inj_df[(inj_df[\"p\"] == 0.0) & (inj_df[\"matching_type\"] == variant)]\n    base_tpr = base_grp[\"tpr\"].mean()\n    summary_rows.append(dict(\n        p=p_val, matching_type=variant,\n        tpr_mean=grp[\"tpr\"].mean(), tpr_std=grp[\"tpr\"].std(),\n        fpr_mean=grp[\"fpr\"].mean(), fpr_std=grp[\"fpr\"].std(),\n        delta_tpr=grp[\"tpr\"].mean() - base_tpr,\n        fisher_or_mean=grp[\"fisher_or\"].mean(),\n        fisher_p_median=grp[\"fisher_p\"].median(),\n        n_flipped_mean=grp[\"n_responses_flipped\"].mean(),\n    ))\nsummary_df = pd.DataFrame(summary_rows)\nsummary_df.to_csv(OUT / \"gsm8k_dose_response_summary.csv\", index=False)\nprint(f\"  Saved gsm8k_dose_response_summary.csv ({len(summary_df)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  REPORT\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Generating report ===\")\n\nL = []\ndef w(s=\"\"):\n    L.append(s)\n\nw(\"# Plan 004 Step 2: GSM8K Semi-Synthetic DIF Injection\")\nw()\nw(\"## 1. Objective\")\nw()\nw(\"Inject known differential contamination into GSM8K response data and test whether\")\nw(\"MH-DIF detects it. Validates that the DIF methodology works on GSM8K (single-domain,\")\nw(\"math benchmark) and enables comparison with MMLU results from plan_011.\")\nw()\n\nw(\"## 2. Setup\")\nw()\nw(f\"- **Benchmark**: GSM8K ({J_TOTAL} items)\")\nw(f\"- **Contaminated items**: {N_CONTAMINATED} ({CONTAM_FRAC*100:.0f}% of {J_TOTAL})\")\nw(f\"- **Injection probabilities**: {INJECTION_PS}\")\nw(f\"- **Seeds per p-level**: {N_SEEDS}\")\nw(f\"- **Cohort**: temporal, ref=2023 (N={len(ref_idx)}), foc=2024 (N={len(foc_idx)})\")\nw(f\"- **External cohort**: ref (N={len(ref_idx_ext)}), foc (N={len(foc_idx_ext)})\")\nw(f\"- **Focal inject (standard)**: {len(foc_inject_idx)} models in accuracy overlap [{overlap_min:.4f}, {overlap_max:.4f}]\")\nw(f\"- **Focal inject (external)**: {len(foc_inject_idx_ext)} models\")\nw()\n\nw(\"### Matching variants\")\nw()\nw(\"| Variant | Matching variable | Properties |\")\nw(\"|---------|-------------------|------------|\")\nw(\"| standard | purified GSM8K total score | Contaminated by injection (20% items affected) |\")\nw(\"| external | avg proportion correct on ARC+HellaSwag+TruthfulQA+Winogrande | Immune to GSM8K injection |\")\nw()\n\nw(\"## 3. Dose-Response Results\")\nw()\nfor variant in MH_VARIANTS:\n    w(f\"### {variant.capitalize()} matching\")\n    w()\n    w(\"| p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |\")\n    w(\"|---|----------------|----------------|------|-----------|----------|\")\n    sub = summary_df[summary_df[\"matching_type\"] == variant].sort_values(\"p\")\n    for _, r in sub.iterrows():\n        w(f\"| {r.p} | {r.tpr_mean:.3f}±{r.tpr_std:.3f} | \"\n          f\"{r.fpr_mean:.3f}±{r.fpr_std:.3f} | {r.delta_tpr:+.3f} | \"\n          f\"{r.fisher_or_mean:.2f} | {r.fisher_p_median:.4f} |\")\n    w()\n\nw(\"## 4. Comparison with MMLU (plan_011)\")\nw()\nw(\"| Metric | MMLU plan_011 (external) | GSM8K (external) |\")\nw(\"|--------|--------------------------|------------------|\")\n\next_sub = summary_df[summary_df[\"matching_type\"] == \"external\"]\next_p0 = ext_sub[ext_sub[\"p\"] == 0.0]\next_p05 = ext_sub[ext_sub[\"p\"] == 0.5]\next_p1 = ext_sub[ext_sub[\"p\"] == 1.0]\n\nmmlu_baseline_fpr = 0.314\nmmlu_dtpr_05 = 0.508\nmmlu_dtpr_10 = 0.674\n\ngsm_fpr0 = ext_p0.iloc[0][\"fpr_mean\"] if len(ext_p0) > 0 else np.nan\ngsm_dtpr05 = ext_p05.iloc[0][\"delta_tpr\"] if len(ext_p05) > 0 else np.nan\ngsm_dtpr10 = ext_p1.iloc[0][\"delta_tpr\"] if len(ext_p1) > 0 else np.nan\n\nw(f\"| Baseline FPR (p=0) | {mmlu_baseline_fpr:.3f} | {gsm_fpr0:.3f} |\")\nw(f\"| ΔTPR at p=0.5 | +{mmlu_dtpr_05:.3f} | {gsm_dtpr05:+.3f} |\")\nw(f\"| ΔTPR at p=1.0 | +{mmlu_dtpr_10:.3f} | {gsm_dtpr10:+.3f} |\")\nw(f\"| Items | 500 (subset) | {J_TOTAL} (all) |\")\nw(f\"| Contaminated | 100 (20%) | {N_CONTAMINATED} (~20%) |\")\nw()\n\nw(\"## 5. Standard vs External Matching\")\nw()\nw(\"| p | Standard TPR | External TPR | Standard FPR | External FPR |\")\nw(\"|---|-------------|-------------|-------------|-------------|\")\nfor p_val in INJECTION_PS:\n    std_r = summary_df[(summary_df[\"p\"] == p_val) & (summary_df[\"matching_type\"] == \"standard\")]\n    ext_r = summary_df[(summary_df[\"p\"] == p_val) & (summary_df[\"matching_type\"] == \"external\")]\n    if len(std_r) > 0 and len(ext_r) > 0:\n        w(f\"| {p_val} | {std_r.iloc[0].tpr_mean:.3f} | {ext_r.iloc[0].tpr_mean:.3f} | \"\n          f\"{std_r.iloc[0].fpr_mean:.3f} | {ext_r.iloc[0].fpr_mean:.3f} |\")\nw()\n\nw(\"## 6. Density Changes\")\nw()\nw(\"| p | Orig density | Post density | Responses flipped |\")\nw(\"|---|-------------|-------------|-------------------|\")\nfor p_val in INJECTION_PS:\n    if p_val == 0:\n        continue\n    sub = inj_df[(inj_df[\"p\"] == p_val) & (inj_df[\"matching_type\"] == \"standard\")]\n    if len(sub) > 0:\n        w(f\"| {p_val} | {sub.orig_density.mean():.4f} | {sub.new_density.mean():.4f} | \"\n          f\"{sub.n_responses_flipped.mean():.0f} |\")\nw()\n\nw(\"## 7. Verdict\")\nw()\n\nfor variant in MH_VARIANTS:\n    sub = summary_df[summary_df[\"matching_type\"] == variant]\n    p0 = sub[sub[\"p\"] == 0.0]\n    p1 = sub[sub[\"p\"] == 1.0]\n    if len(p0) == 0 or len(p1) == 0:\n        continue\n    tpr0 = p0.iloc[0][\"tpr_mean\"]\n    fpr0 = p0.iloc[0][\"fpr_mean\"]\n    tpr1 = p1.iloc[0][\"tpr_mean\"]\n    fpr1 = p1.iloc[0][\"fpr_mean\"]\n    d_tpr = tpr1 - tpr0\n\n    w(f\"### {variant.capitalize()} matching\")\n    w()\n    w(f\"- Baseline (p=0): TPR={tpr0:.3f}, FPR={fpr0:.3f}\")\n    w(f\"- Full injection (p=1): TPR={tpr1:.3f}, FPR={fpr1:.3f}\")\n    w(f\"- ΔTPR = {d_tpr:+.3f}\")\n    w()\n\n    if d_tpr > 0.3 and tpr1 > 0.5:\n        w(f\"**SUCCESS**: injection raises TPR by {d_tpr:.3f} with clear dose-response.\")\n    elif d_tpr > 0.1:\n        w(f\"**PARTIAL**: detectable signal (ΔTPR={d_tpr:.3f}) but modest.\")\n    else:\n        w(f\"**FAIL**: ΔTPR={d_tpr:.3f} too small to indicate reliable detection.\")\n    w()\n\nw(\"## 8. Implications\")\nw()\nw(\"### Cross-benchmark generalization\")\nw()\nw(\"If GSM8K semi-synthetic results are comparable to MMLU plan_011, this confirms\")\nw(\"MH-DIF methodology generalizes beyond MMLU to single-domain math benchmarks.\")\nw()\nw(\"### Matching variable contamination\")\nw()\nw(\"Standard matching uses GSM8K total score, which is corrupted when 20% of items\")\nw(\"are injected. This should inflate FPR compared to external matching.\")\nw(\"External matching (other benchmarks) is immune to GSM8K injection and should\")\nw(\"provide cleaner separation between contaminated and clean items.\")\nw()\n\nreport_text = \"\\n\".join(L) + \"\\n\"\n(OUT / \"plan_004_step2_report.md\").write_text(report_text)\nprint(\"  Report written.\")\n\n# Console summary\nprint(\"\\n\" + \"=\" * 60)\nprint(\"SUMMARY\")\nprint(\"=\" * 60)\nfor variant in MH_VARIANTS:\n    print(f\"\\n--- {variant} matching ---\")\n    sub = summary_df[summary_df[\"matching_type\"] == variant].sort_values(\"p\")\n    for _, r in sub.iterrows():\n        print(f\"  p={r.p}: TPR={r.tpr_mean:.3f}±{r.tpr_std:.3f}  \"\n              f\"FPR={r.fpr_mean:.3f}±{r.fpr_std:.3f}  ΔTPR={r.delta_tpr:+.3f}\")\n\ntotal_elapsed = time.time() - t_start\nprint(f\"\\nTotal time: {total_elapsed:.0f}s\")\nprint(f\"All outputs saved to {OUT}\")\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "10bb8829-7d0d-4a1f-923a-356d808d20f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## 任务：plan_004 Step 2 — GSM8K Semi-Synthetic Injection（复制 plan_011 方法）  **P0 紧急。** 在 GSM8K response matrix 上验证 DIF 方法论有效性。  ### 背景  Step 1 已完成：GSM8K temporal DIF 确认存在（standard 18.9% C, external 47.4%…",
  "leafUuid": "3de792de-59b2-48fa-b870-d55b70c5a9ea",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "GSM8K semi-synthetic DIF injection validation",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5"
}
```

---

### Assistant

_source line 26 · 2026-05-21T00:55:57.379Z_

Running the script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3de792de-59b2-48fa-b870-d55b70c5a9ea",
  "isSidechain": false,
  "requestId": "req_011CbEoZecDuE4nk4k9qZS5R",
  "type": "assistant",
  "uuid": "acddffd8-516d-4a0c-a87e-b02659358b54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkbiFmzbyuKg2Y5cLVkxnH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8162,
      "cache_read_input_tokens": 44780,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8162,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 44780,
          "cache_creation_input_tokens": 8162,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8162
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

_source line 27 · 2026-05-21T00:55:58.539Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01T7Vqs4hFFCKPeyVmEvARw4`</summary>

```json
{
  "command": "python artifacts/plan_004/plan_004_step2_gsm8k_semi_synthetic.py 2>&1",
  "description": "Run GSM8K semi-synthetic injection script",
  "timeout": 600000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acddffd8-516d-4a0c-a87e-b02659358b54",
  "isSidechain": false,
  "requestId": "req_011CbEoZecDuE4nk4k9qZS5R",
  "type": "assistant",
  "uuid": "e7a9e003-ddf2-45a0-89f1-59e2a6904c7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkbiFmzbyuKg2Y5cLVkxnH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8162,
      "cache_read_input_tokens": 44780,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8162,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 44780,
          "cache_creation_input_tokens": 8162,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8162
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

_source line 28 · 2026-05-21T00:55:58.598Z_

<details><summary>↩ Tool result · reported error · `toolu_01T7Vqs4hFFCKPeyVmEvARw4`</summary>

```text
Exit code 127
/bin/bash: line 1: python: command not found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7a9e003-ddf2-45a0-89f1-59e2a6904c7f",
  "isSidechain": false,
  "promptId": "b681718f-ed7e-4c71-ace8-cbf70777063c",
  "type": "user",
  "uuid": "cdf8d309-9bb6-4d3b-820c-68dffd9dbad4",
  "toolUseResult": "Error: Exit code 127\n/bin/bash: line 1: python: command not found",
  "sourceToolAssistantUUID": "e7a9e003-ddf2-45a0-89f1-59e2a6904c7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T00:56:01.858Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Q71AuX9d9YRsGtuWFpbogu`</summary>

```json
{
  "command": "which python3 && python3 artifacts/plan_004/plan_004_step2_gsm8k_semi_synthetic.py 2>&1",
  "description": "Run GSM8K semi-synthetic injection script with python3",
  "timeout": 600000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdf8d309-9bb6-4d3b-820c-68dffd9dbad4",
  "isSidechain": false,
  "requestId": "req_011CbEoZvesmGkqoU97pBRMV",
  "type": "assistant",
  "uuid": "3f5e7e10-ba4c-436a-9f7e-b4cc2a8474cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JdW4KeVHBriSn5d7SYiapn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 167,
      "cache_read_input_tokens": 52942,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 167,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 52942,
          "cache_creation_input_tokens": 167,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 167
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

_source line 30 · 2026-05-21T00:57:40.856Z_

<details><summary>↩ Tool result · `toolu_01Q71AuX9d9YRsGtuWFpbogu`</summary>

```text
/usr/bin/python3
=== Loading GSM8K data ===
  Response matrix: 6702 × 1319
  Contaminated items: 264 (20%), clean: 1055

=== Computing external matching scores ===
  Loading arc...
    arc: 5227 models, 4.3s
  Loading hellaswag...
    hellaswag: 5227 models, 34.3s
  Loading truthfulqa...
    truthfulqa: 5228 models, 2.7s
  Loading winogrande...
    winogrande: 6558 models, 4.8s
  Models with external scores (≥2 benchmarks): 5057

=== Cohort construction ===
  Temporal: ref=2023 (N=1017), foc=2024 (N=804)
  External subset: ref (N=1017), foc (N=804)
  Accuracy overlap: [0.0000, 0.7589]
  Focal inject (standard): 779 models
  Focal inject (external): 779 models

=== Injection + MH-DIF ===
  [1/50] standard p=0.0 seed=1: TPR=0.227 FPR=0.179 flipped=0 (1s)
  [2/50] external p=0.0 seed=1: TPR=0.470 FPR=0.475 flipped=0 (2s)
  [3/50] standard p=0.0 seed=2: TPR=0.155 FPR=0.197 flipped=0 (2s)
  [4/50] external p=0.0 seed=2: TPR=0.492 FPR=0.469 flipped=0 (3s)
  [5/50] standard p=0.0 seed=3: TPR=0.163 FPR=0.195 flipped=0 (4s)
  [6/50] external p=0.0 seed=3: TPR=0.455 FPR=0.479 flipped=0 (5s)
  [7/50] standard p=0.0 seed=4: TPR=0.220 FPR=0.181 flipped=0 (5s)
  [8/50] external p=0.0 seed=4: TPR=0.527 FPR=0.461 flipped=0 (6s)
  [9/50] standard p=0.0 seed=5: TPR=0.144 FPR=0.200 flipped=0 (7s)
  [10/50] external p=0.0 seed=5: TPR=0.473 FPR=0.474 flipped=0 (8s)
  [11/50] standard p=0.3 seed=1: TPR=0.739 FPR=0.262 flipped=37260 (9s)
  [12/50] external p=0.3 seed=1: TPR=0.951 FPR=0.475 flipped=37260 (9s)
  [13/50] standard p=0.3 seed=2: TPR=0.750 FPR=0.264 flipped=36402 (10s)
  [14/50] external p=0.3 seed=2: TPR=0.973 FPR=0.469 flipped=36402 (11s)
  [15/50] standard p=0.3 seed=3: TPR=0.750 FPR=0.259 flipped=35947 (12s)
  [16/50] external p=0.3 seed=3: TPR=0.981 FPR=0.479 flipped=35947 (13s)
  [17/50] standard p=0.3 seed=4: TPR=0.754 FPR=0.250 flipped=36437 (14s)
  [18/50] external p=0.3 seed=4: TPR=0.958 FPR=0.461 flipped=36437 (15s)
  [19/50] standard p=0.3 seed=5: TPR=0.712 FPR=0.247 flipped=35130 (16s)
  [20/50] external p=0.3 seed=5: TPR=0.985 FPR=0.474 flipped=35130 (17s)
  [21/50] standard p=0.5 seed=1: TPR=0.928 FPR=0.369 flipped=62216 (17s)
  [22/50] external p=0.5 seed=1: TPR=0.996 FPR=0.475 flipped=62216 (18s)
  [23/50] standard p=0.5 seed=2: TPR=0.932 FPR=0.367 flipped=60419 (19s)
  [24/50] external p=0.5 seed=2: TPR=1.000 FPR=0.469 flipped=60419 (20s)
  [25/50] standard p=0.5 seed=3: TPR=0.932 FPR=0.370 flipped=59974 (21s)
  [26/50] external p=0.5 seed=3: TPR=0.996 FPR=0.479 flipped=59974 (22s)
  [27/50] standard p=0.5 seed=4: TPR=0.924 FPR=0.366 flipped=60673 (22s)
  [28/50] external p=0.5 seed=4: TPR=0.996 FPR=0.461 flipped=60673 (23s)
  [29/50] standard p=0.5 seed=5: TPR=0.939 FPR=0.365 flipped=58945 (24s)
  [30/50] external p=0.5 seed=5: TPR=1.000 FPR=0.474 flipped=58945 (25s)
  [31/50] standard p=0.7 seed=1: TPR=1.000 FPR=0.492 flipped=86992 (26s)
  [32/50] external p=0.7 seed=1: TPR=1.000 FPR=0.475 flipped=86992 (27s)
  [33/50] standard p=0.7 seed=2: TPR=1.000 FPR=0.474 flipped=84565 (27s)
  [34/50] external p=0.7 seed=2: TPR=1.000 FPR=0.469 flipped=84565 (28s)
  [35/50] standard p=0.7 seed=3: TPR=1.000 FPR=0.478 flipped=83801 (29s)
  [36/50] external p=0.7 seed=3: TPR=1.000 FPR=0.479 flipped=83801 (30s)
  [37/50] standard p=0.7 seed=4: TPR=1.000 FPR=0.467 flipped=84819 (31s)
  [38/50] external p=0.7 seed=4: TPR=1.000 FPR=0.461 flipped=84819 (32s)
  [39/50] standard p=0.7 seed=5: TPR=1.000 FPR=0.469 flipped=82445 (33s)
  [40/50] external p=0.7 seed=5: TPR=1.000 FPR=0.474 flipped=82445 (33s)
  [41/50] standard p=1.0 seed=1: TPR=1.000 FPR=0.665 flipped=124221 (34s)
  [42/50] external p=1.0 seed=1: TPR=1.000 FPR=0.475 flipped=124221 (35s)
  [43/50] standard p=1.0 seed=2: TPR=1.000 FPR=0.640 flipped=121047 (36s)
  [44/50] external p=1.0 seed=2: TPR=1.000 FPR=0.469 flipped=121047 (37s)
  [45/50] standard p=1.0 seed=3: TPR=1.000 FPR=0.640 flipped=119972 (38s)
  [46/50] external p=1.0 seed=3: TPR=1.000 FPR=0.479 flipped=119972 (38s)
  [47/50] standard p=1.0 seed=4: TPR=1.000 FPR=0.648 flipped=121223 (39s)
  [48/50] external p=1.0 seed=4: TPR=1.000 FPR=0.461 flipped=121223 (40s)
  [49/50] standard p=1.0 seed=5: TPR=1.000 FPR=0.633 flipped=118180 (41s)
  [50/50] external p=1.0 seed=5: TPR=1.000 FPR=0.474 flipped=118180 (42s)

=== Aggregating results ===
  Saved gsm8k_dose_response.csv (50 rows)
  Saved gsm8k_dose_response_summary.csv (10 rows)

=== Generating report ===
  Report written.

============================================================
SUMMARY
============================================================

--- standard matching ---
  p=0.0: TPR=0.182±0.039  FPR=0.191±0.010  ΔTPR=+0.000
  p=0.3: TPR=0.741±0.017  FPR=0.256±0.007  ΔTPR=+0.559
  p=0.5: TPR=0.931±0.006  FPR=0.367±0.002  ΔTPR=+0.749
  p=0.7: TPR=1.000±0.000  FPR=0.476±0.010  ΔTPR=+0.818
  p=1.0: TPR=1.000±0.000  FPR=0.645±0.012  ΔTPR=+0.818

--- external matching ---
  p=0.0: TPR=0.483±0.028  FPR=0.471±0.007  ΔTPR=+0.000
  p=0.3: TPR=0.970±0.015  FPR=0.471±0.007  ΔTPR=+0.486
  p=0.5: TPR=0.998±0.002  FPR=0.471±0.007  ΔTPR=+0.514
  p=0.7: TPR=1.000±0.000  FPR=0.471±0.007  ΔTPR=+0.517
  p=1.0: TPR=1.000±0.000  FPR=0.471±0.007  ΔTPR=+0.517

Total time: 42s
All outputs saved to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f5e7e10-ba4c-436a-9f7e-b4cc2a8474cb",
  "isSidechain": false,
  "promptId": "b681718f-ed7e-4c71-ace8-cbf70777063c",
  "type": "user",
  "uuid": "ecf54534-1cd2-4373-b583-a2158b152abf",
  "toolUseResult": {
    "stdout": "/usr/bin/python3\n=== Loading GSM8K data ===\n  Response matrix: 6702 × 1319\n  Contaminated items: 264 (20%), clean: 1055\n\n=== Computing external matching scores ===\n  Loading arc...\n    arc: 5227 models, 4.3s\n  Loading hellaswag...\n    hellaswag: 5227 models, 34.3s\n  Loading truthfulqa...\n    truthfulqa: 5228 models, 2.7s\n  Loading winogrande...\n    winogrande: 6558 models, 4.8s\n  Models with external scores (≥2 benchmarks): 5057\n\n=== Cohort construction ===\n  Temporal: ref=2023 (N=1017), foc=2024 (N=804)\n  External subset: ref (N=1017), foc (N=804)\n  Accuracy overlap: [0.0000, 0.7589]\n  Focal inject (standard): 779 models\n  Focal inject (external): 779 models\n\n=== Injection + MH-DIF ===\n  [1/50] standard p=0.0 seed=1: TPR=0.227 FPR=0.179 flipped=0 (1s)\n  [2/50] external p=0.0 seed=1: TPR=0.470 FPR=0.475 flipped=0 (2s)\n  [3/50] standard p=0.0 seed=2: TPR=0.155 FPR=0.197 flipped=0 (2s)\n  [4/50] external p=0.0 seed=2: TPR=0.492 FPR=0.469 flipped=0 (3s)\n  [5/50] standard p=0.0 seed=3: TPR=0.163 FPR=0.195 flipped=0 (4s)\n  [6/50] external p=0.0 seed=3: TPR=0.455 FPR=0.479 flipped=0 (5s)\n  [7/50] standard p=0.0 seed=4: TPR=0.220 FPR=0.181 flipped=0 (5s)\n  [8/50] external p=0.0 seed=4: TPR=0.527 FPR=0.461 flipped=0 (6s)\n  [9/50] standard p=0.0 seed=5: TPR=0.144 FPR=0.200 flipped=0 (7s)\n  [10/50] external p=0.0 seed=5: TPR=0.473 FPR=0.474 flipped=0 (8s)\n  [11/50] standard p=0.3 seed=1: TPR=0.739 FPR=0.262 flipped=37260 (9s)\n  [12/50] external p=0.3 seed=1: TPR=0.951 FPR=0.475 flipped=37260 (9s)\n  [13/50] standard p=0.3 seed=2: TPR=0.750 FPR=0.264 flipped=36402 (10s)\n  [14/50] external p=0.3 seed=2: TPR=0.973 FPR=0.469 flipped=36402 (11s)\n  [15/50] standard p=0.3 seed=3: TPR=0.750 FPR=0.259 flipped=35947 (12s)\n  [16/50] external p=0.3 seed=3: TPR=0.981 FPR=0.479 flipped=35947 (13s)\n  [17/50] standard p=0.3 seed=4: TPR=0.754 FPR=0.250 flipped=36437 (14s)\n  [18/50] external p=0.3 seed=4: TPR=0.958 FPR=0.461 flipped=36437 (15s)\n  [19/50] standard p=0.3 seed=5: TPR=0.712 FPR=0.247 flipped=35130 (16s)\n  [20/50] external p=0.3 seed=5: TPR=0.985 FPR=0.474 flipped=35130 (17s)\n  [21/50] standard p=0.5 seed=1: TPR=0.928 FPR=0.369 flipped=62216 (17s)\n  [22/50] external p=0.5 seed=1: TPR=0.996 FPR=0.475 flipped=62216 (18s)\n  [23/50] standard p=0.5 seed=2: TPR=0.932 FPR=0.367 flipped=60419 (19s)\n  [24/50] external p=0.5 seed=2: TPR=1.000 FPR=0.469 flipped=60419 (20s)\n  [25/50] standard p=0.5 seed=3: TPR=0.932 FPR=0.370 flipped=59974 (21s)\n  [26/50] external p=0.5 seed=3: TPR=0.996 FPR=0.479 flipped=59974 (22s)\n  [27/50] standard p=0.5 seed=4: TPR=0.924 FPR=0.366 flipped=60673 (22s)\n  [28/50] external p=0.5 seed=4: TPR=0.996 FPR=0.461 flipped=60673 (23s)\n  [29/50] standard p=0.5 seed=5: TPR=0.939 FPR=0.365 flipped=58945 (24s)\n  [30/50] external p=0.5 seed=5: TPR=1.000 FPR=0.474 flipped=58945 (25s)\n  [31/50] standard p=0.7 seed=1: TPR=1.000 FPR=0.492 flipped=86992 (26s)\n  [32/50] external p=0.7 seed=1: TPR=1.000 FPR=0.475 flipped=86992 (27s)\n  [33/50] standard p=0.7 seed=2: TPR=1.000 FPR=0.474 flipped=84565 (27s)\n  [34/50] external p=0.7 seed=2: TPR=1.000 FPR=0.469 flipped=84565 (28s)\n  [35/50] standard p=0.7 seed=3: TPR=1.000 FPR=0.478 flipped=83801 (29s)\n  [36/50] external p=0.7 seed=3: TPR=1.000 FPR=0.479 flipped=83801 (30s)\n  [37/50] standard p=0.7 seed=4: TPR=1.000 FPR=0.467 flipped=84819 (31s)\n  [38/50] external p=0.7 seed=4: TPR=1.000 FPR=0.461 flipped=84819 (32s)\n  [39/50] standard p=0.7 seed=5: TPR=1.000 FPR=0.469 flipped=82445 (33s)\n  [40/50] external p=0.7 seed=5: TPR=1.000 FPR=0.474 flipped=82445 (33s)\n  [41/50] standard p=1.0 seed=1: TPR=1.000 FPR=0.665 flipped=124221 (34s)\n  [42/50] external p=1.0 seed=1: TPR=1.000 FPR=0.475 flipped=124221 (35s)\n  [43/50] standard p=1.0 seed=2: TPR=1.000 FPR=0.640 flipped=121047 (36s)\n  [44/50] external p=1.0 seed=2: TPR=1.000 FPR=0.469 flipped=121047 (37s)\n  [45/50] standard p=1.0 seed=3: TPR=1.000 FPR=0.640 flipped=119972 (38s)\n  [46/50] external p=1.0 seed=3: TPR=1.000 FPR=0.479 flipped=119972 (38s)\n  [47/50] standard p=1.0 seed=4: TPR=1.000 FPR=0.648 flipped=121223 (39s)\n  [48/50] external p=1.0 seed=4: TPR=1.000 FPR=0.461 flipped=121223 (40s)\n  [49/50] standard p=1.0 seed=5: TPR=1.000 FPR=0.633 flipped=118180 (41s)\n  [50/50] external p=1.0 seed=5: TPR=1.000 FPR=0.474 flipped=118180 (42s)\n\n=== Aggregating results ===\n  Saved gsm8k_dose_response.csv (50 rows)\n  Saved gsm8k_dose_response_summary.csv (10 rows)\n\n=== Generating report ===\n  Report written.\n\n============================================================\nSUMMARY\n============================================================\n\n--- standard matching ---\n  p=0.0: TPR=0.182±0.039  FPR=0.191±0.010  ΔTPR=+0.000\n  p=0.3: TPR=0.741±0.017  FPR=0.256±0.007  ΔTPR=+0.559\n  p=0.5: TPR=0.931±0.006  FPR=0.367±0.002  ΔTPR=+0.749\n  p=0.7: TPR=1.000±0.000  FPR=0.476±0.010  ΔTPR=+0.818\n  p=1.0: TPR=1.000±0.000  FPR=0.645±0.012  ΔTPR=+0.818\n\n--- external matching ---\n  p=0.0: TPR=0.483±0.028  FPR=0.471±0.007  ΔTPR=+0.000\n  p=0.3: TPR=0.970±0.015  FPR=0.471±0.007  ΔTPR=+0.486\n  p=0.5: TPR=0.998±0.002  FPR=0.471±0.007  ΔTPR=+0.514\n  p=0.7: TPR=1.000±0.000  FPR=0.471±0.007  ΔTPR=+0.517\n  p=1.0: TPR=1.000±0.000  FPR=0.471±0.007  ΔTPR=+0.517\n\nTotal time: 42s\nAll outputs saved to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3f5e7e10-ba4c-436a-9f7e-b4cc2a8474cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-21T00:58:01.883Z_

<details><summary>Logged reasoning block</summary>

```text
The results are very interesting. Let me analyze them:

**Standard matching:**
- Baseline FPR: 0.191 (much lower than external's 0.471)
- ΔTPR at p=0.5: +0.749 (higher than MMLU's +0.508!)
- ΔTPR at p=1.0: +0.818
- But FPR inflates badly at high p: 0.645 at p=1.0

**External matching:**


- Baseline FPR: 0.471 (extremely high compared to MMLU's 0.314)
- ΔTPR at p=0.5: +0.514 (similar to MMLU's +0.508)
- ΔTPR at p=1.0: +0.517
- FPR remains constant at 0.471 since external scores aren't affected by confidence thresholds
- TPR saturates quickly at p=0.3-0.5, hitting 1.0 early

The external false positive rate is strikingly high at 47.1%, likely because GSM8K operates as a single-domain benchmark, making it much noisier than MMLU's multi-domain structure.

MH-DIF successfully detects the injected contamination on GSM8K through strong dose-response with standard matching and near-perfect sensitivity with external matching even at low p-levels. However, the external approach suffers from a severe baseline FPR of 47.1%—almost half of clean items get flagged as contaminated—which aligns with the 47.4% contamination rate found in the initial analysis. This high false positive rate reflects genuine temporal differential item functioning already present in GSM8K itself, making external matching problematic for this particular benchmark.

Standard matching proves more practical despite its own limitations: it maintains a lower baseline FPR of 19.1% and shows stronger dose-response effects, though the FPR does increase at higher p-levels due to contamination in the matching variable itself. Now I'll save these results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecf54534-1cd2-4373-b583-a2158b152abf",
  "isSidechain": false,
  "requestId": "req_011CbEohTsY4tyJW9gZ2o28u",
  "type": "assistant",
  "uuid": "2a32e2a1-ff49-490c-ab87-d9554f5b47ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VE2otz8hQNUuR4XM8JftHk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3096,
      "cache_read_input_tokens": 53109,
      "output_tokens": 724,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3096,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 724,
          "cache_read_input_tokens": 53109,
          "cache_creation_input_tokens": 3096,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3096
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

_source line 32 · 2026-05-21T00:58:01.885Z_

Script completed successfully in 42s. Now registering artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a32e2a1-ff49-490c-ab87-d9554f5b47ef",
  "isSidechain": false,
  "requestId": "req_011CbEohTsY4tyJW9gZ2o28u",
  "type": "assistant",
  "uuid": "2e342e11-196a-4503-8ade-19241a2aa65b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VE2otz8hQNUuR4XM8JftHk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3096,
      "cache_read_input_tokens": 53109,
      "output_tokens": 724,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3096,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 724,
          "cache_read_input_tokens": 53109,
          "cache_creation_input_tokens": 3096,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3096
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

_source line 33 · 2026-05-21T00:58:02.105Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019bwuEcUBB3ywzVinjWBc6W`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e342e11-196a-4503-8ade-19241a2aa65b",
  "isSidechain": false,
  "requestId": "req_011CbEohTsY4tyJW9gZ2o28u",
  "type": "assistant",
  "uuid": "e6901e0f-9ca5-45d7-8bcc-94d6d88318dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VE2otz8hQNUuR4XM8JftHk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3096,
      "cache_read_input_tokens": 53109,
      "output_tokens": 724,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3096,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 724,
          "cache_read_input_tokens": 53109,
          "cache_creation_input_tokens": 3096,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3096
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

_source line 34 · 2026-05-21T00:58:02.110Z_

<details><summary>↩ Tool result · `toolu_019bwuEcUBB3ywzVinjWBc6W`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6901e0f-9ca5-45d7-8bcc-94d6d88318dd",
  "isSidechain": false,
  "promptId": "b681718f-ed7e-4c71-ace8-cbf70777063c",
  "type": "user",
  "uuid": "23e9e21e-7cbc-43bc-b70b-3d399601b0a5",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  },
  "sourceToolAssistantUUID": "e6901e0f-9ca5-45d7-8bcc-94d6d88318dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35 · 2026-05-21T00:58:02.249Z_

```json
{
  "parentUuid": "23e9e21e-7cbc-43bc-b70b-3d399601b0a5",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6be3e57e-0a68-454a-9f4a-3603320be35b",
  "timestamp": "2026-05-21T00:58:02.249Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 36 · 2026-05-21T00:58:09.027Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01YSs4oPa8bQnd6TQh3fq1gz`</summary>

```json
{
  "name": "plan_004_step2_gsm8k_semi_synthetic",
  "type": "intermediate",
  "description": "GSM8K semi-synthetic DIF injection script — injects known differential contamination and tests MH-DIF detection with standard/external matching",
  "project": "irt_equated_bench_regen",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_step2_gsm8k_semi_synthetic.py",
  "tags": [
    "plan_004",
    "gsm8k",
    "semi-synthetic",
    "dif",
    "injection"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6be3e57e-0a68-454a-9f4a-3603320be35b",
  "isSidechain": false,
  "requestId": "req_011CbEoj3JyGzMYy19Bau6N4",
  "type": "assistant",
  "uuid": "9cd9b36e-5968-4f0a-9ce5-016369adf32d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ho23VwPk2NNf2TiLD3EUTf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 56205,
      "output_tokens": 1014,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1448,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1014,
          "cache_read_input_tokens": 56205,
          "cache_creation_input_tokens": 1448,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1448
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

_source line 37 · 2026-05-21T00:58:09.261Z_

<details><summary>↩ Tool result · `toolu_01YSs4oPa8bQnd6TQh3fq1gz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_3f68a2\", \"name\": \"plan_004_step2_gsm8k_semi_synthetic\", \"type\": \"intermediate\", \"description\": \"GSM8K semi-synthetic DIF injection script — injects known differential contamination and tests MH-DIF detection with standard/external matching\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_004_step2_gsm8k_semi_synthetic.py\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T00:58:09.035640+00:00\", \"tags\": [\"plan_004\", \"gsm8k\", \"semi-synthetic\", \"dif\", \"injection\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9cd9b36e-5968-4f0a-9ce5-016369adf32d",
  "isSidechain": false,
  "promptId": "b681718f-ed7e-4c71-ace8-cbf70777063c",
  "type": "user",
  "uuid": "03554c6f-98fc-4bdd-9db3-b99e97d420d1",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260521_3f68a2\\\", \\\"name\\\": \\\"plan_004_step2_gsm8k_semi_synthetic\\\", \\\"type\\\": \\\"intermediate\\\", \\\"description\\\": \\\"GSM8K semi-synthetic DIF injection script — injects known differential contamination and tests MH-DIF detection with standard/external matching\\\", \\\"path\\\": \\\"projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_004_step2_gsm8k_semi_synthetic.py\\\", \\\"url\\\": null, \\\"project\\\": \\\"irt_equated_bench_regen\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-21T00:58:09.035640+00:00\\\", \\\"tags\\\": [\\\"plan_004\\\", \\\"gsm8k\\\", \\\"semi-synthetic\\\", \\\"dif\\\", \\\"injection\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_3f68a2\", \"name\": \"plan_004_step2_gsm8k_semi_synthetic\", \"type\": \"intermediate\", \"description\": \"GSM8K semi-synthetic DIF injection script — injects known differential contamination and tests MH-DIF detection with standard/external matching\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_004_step2_gsm8k_semi_synthetic.py\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T00:58:09.035640+00:00\", \"tags\": [\"plan_004\", \"gsm8k\", \"semi-synthetic\", \"dif\", \"injection\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "9cd9b36e-5968-4f0a-9ce5-016369adf32d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T00:58:11.900Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01VQ3abAggfLcecvRY4egK5d`</summary>

```json
{
  "name": "gsm8k_dose_response",
  "type": "data",
  "description": "GSM8K dose-response raw results: TPR/FPR/Fisher for each p × matching_type × seed (50 rows)",
  "project": "irt_equated_bench_regen",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/gsm8k_dose_response.csv",
  "tags": [
    "plan_004",
    "gsm8k",
    "dose-response"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03554c6f-98fc-4bdd-9db3-b99e97d420d1",
  "isSidechain": false,
  "requestId": "req_011CbEoj3JyGzMYy19Bau6N4",
  "type": "assistant",
  "uuid": "d2f701de-079f-4393-9225-27a4e8f87007",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ho23VwPk2NNf2TiLD3EUTf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 56205,
      "output_tokens": 1014,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1448,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1014,
          "cache_read_input_tokens": 56205,
          "cache_creation_input_tokens": 1448,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1448
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

_source line 39 · 2026-05-21T00:58:12.072Z_

<details><summary>↩ Tool result · `toolu_01VQ3abAggfLcecvRY4egK5d`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_36bb27\", \"name\": \"gsm8k_dose_response\", \"type\": \"data\", \"description\": \"GSM8K dose-response raw results: TPR/FPR/Fisher for each p × matching_type × seed (50 rows)\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/data/gsm8k_dose_response.csv\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T00:58:11.905186+00:00\", \"tags\": [\"plan_004\", \"gsm8k\", \"dose-response\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2f701de-079f-4393-9225-27a4e8f87007",
  "isSidechain": false,
  "promptId": "b681718f-ed7e-4c71-ace8-cbf70777063c",
  "type": "user",
  "uuid": "21739fae-d14e-4068-9be2-be718ec5e9f8",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260521_36bb27\\\", \\\"name\\\": \\\"gsm8k_dose_response\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"GSM8K dose-response raw results: TPR/FPR/Fisher for each p × matching_type × seed (50 rows)\\\", \\\"path\\\": \\\"projects/irt_equated_bench_regen/artifacts/_project/data/gsm8k_dose_response.csv\\\", \\\"url\\\": null, \\\"project\\\": \\\"irt_equated_bench_regen\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-21T00:58:11.905186+00:00\\\", \\\"tags\\\": [\\\"plan_004\\\", \\\"gsm8k\\\", \\\"dose-response\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_36bb27\", \"name\": \"gsm8k_dose_response\", \"type\": \"data\", \"description\": \"GSM8K dose-response raw results: TPR/FPR/Fisher for each p × matching_type × seed (50 rows)\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/data/gsm8k_dose_response.csv\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T00:58:11.905186+00:00\", \"tags\": [\"plan_004\", \"gsm8k\", \"dose-response\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "d2f701de-079f-4393-9225-27a4e8f87007",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-21T00:58:14.376Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_011nYSeU3gQjnmDx8s2uTq1W`</summary>

```json
{
  "name": "gsm8k_dose_response_summary",
  "type": "data",
  "description": "GSM8K dose-response summary: mean TPR/FPR/ΔTPR aggregated across 5 seeds per p × matching_type (10 rows)",
  "project": "irt_equated_bench_regen",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/gsm8k_dose_response_summary.csv",
  "tags": [
    "plan_004",
    "gsm8k",
    "dose-response",
    "summary"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21739fae-d14e-4068-9be2-be718ec5e9f8",
  "isSidechain": false,
  "requestId": "req_011CbEoj3JyGzMYy19Bau6N4",
  "type": "assistant",
  "uuid": "f961f356-179c-4ca8-b703-8dd2e8089bbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ho23VwPk2NNf2TiLD3EUTf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 56205,
      "output_tokens": 1014,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1448,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1014,
          "cache_read_input_tokens": 56205,
          "cache_creation_input_tokens": 1448,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1448
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

_source line 41 · 2026-05-21T00:58:14.554Z_

<details><summary>↩ Tool result · `toolu_011nYSeU3gQjnmDx8s2uTq1W`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_ab8247\", \"name\": \"gsm8k_dose_response_summary\", \"type\": \"data\", \"description\": \"GSM8K dose-response summary: mean TPR/FPR/ΔTPR aggregated across 5 seeds per p × matching_type (10 rows)\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/data/gsm8k_dose_response_summary.csv\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T00:58:14.383381+00:00\", \"tags\": [\"plan_004\", \"gsm8k\", \"dose-response\", \"summary\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f961f356-179c-4ca8-b703-8dd2e8089bbd",
  "isSidechain": false,
  "promptId": "b681718f-ed7e-4c71-ace8-cbf70777063c",
  "type": "user",
  "uuid": "378c1c1d-9822-47cf-85b6-e9ac35cb5c8c",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260521_ab8247\\\", \\\"name\\\": \\\"gsm8k_dose_response_summary\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"GSM8K dose-response summary: mean TPR/FPR/ΔTPR aggregated across 5 seeds per p × matching_type (10 rows)\\\", \\\"path\\\": \\\"projects/irt_equated_bench_regen/artifacts/_project/data/gsm8k_dose_response_summary.csv\\\", \\\"url\\\": null, \\\"project\\\": \\\"irt_equated_bench_regen\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-21T00:58:14.383381+00:00\\\", \\\"tags\\\": [\\\"plan_004\\\", \\\"gsm8k\\\", \\\"dose-response\\\", \\\"summary\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_ab8247\", \"name\": \"gsm8k_dose_response_summary\", \"type\": \"data\", \"description\": \"GSM8K dose-response summary: mean TPR/FPR/ΔTPR aggregated across 5 seeds per p × matching_type (10 rows)\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/data/gsm8k_dose_response_summary.csv\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T00:58:14.383381+00:00\", \"tags\": [\"plan_004\", \"gsm8k\", \"dose-response\", \"summary\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "f961f356-179c-4ca8-b703-8dd2e8089bbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-21T00:58:16.447Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01LpSrgrNtMujuWTxxfZAmGV`</summary>

```json
{
  "name": "plan_004_step2_report",
  "type": "report",
  "description": "Plan 004 Step 2 report: GSM8K semi-synthetic DIF injection results, comparison with MMLU plan_011",
  "project": "irt_equated_bench_regen",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_step2_report.md",
  "tags": [
    "plan_004",
    "gsm8k",
    "report"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "378c1c1d-9822-47cf-85b6-e9ac35cb5c8c",
  "isSidechain": false,
  "requestId": "req_011CbEoj3JyGzMYy19Bau6N4",
  "type": "assistant",
  "uuid": "990c3632-b009-4ef2-bce1-fb7023af182a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ho23VwPk2NNf2TiLD3EUTf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 56205,
      "output_tokens": 1014,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1448,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1014,
          "cache_read_input_tokens": 56205,
          "cache_creation_input_tokens": 1448,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1448
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

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## 任务：plan_004 Step 2 — GSM8K Semi-Synthetic Injection（复制 plan_011 方法）  **P0 紧急。** 在 GSM8K response matrix 上验证 DIF 方法论有效性。  ### 背景  Step 1 已完成：GSM8K temporal DIF 确认存在（standard 18.9% C, external 47.4%…",
  "leafUuid": "990c3632-b009-4ef2-bce1-fb7023af182a",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "GSM8K semi-synthetic DIF injection validation",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5"
}
```

---

### Tool result

_source line 45 · 2026-05-21T00:58:16.619Z_

<details><summary>↩ Tool result · `toolu_01LpSrgrNtMujuWTxxfZAmGV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_42613e\", \"name\": \"plan_004_step2_report\", \"type\": \"report\", \"description\": \"Plan 004 Step 2 report: GSM8K semi-synthetic DIF injection results, comparison with MMLU plan_011\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/report/plan_004_step2_report.md\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T00:58:16.451993+00:00\", \"tags\": [\"plan_004\", \"gsm8k\", \"report\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "990c3632-b009-4ef2-bce1-fb7023af182a",
  "isSidechain": false,
  "promptId": "b681718f-ed7e-4c71-ace8-cbf70777063c",
  "type": "user",
  "uuid": "c5094949-d1fd-4ff2-8049-7c266f377965",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260521_42613e\\\", \\\"name\\\": \\\"plan_004_step2_report\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Plan 004 Step 2 report: GSM8K semi-synthetic DIF injection results, comparison with MMLU plan_011\\\", \\\"path\\\": \\\"projects/irt_equated_bench_regen/artifacts/_project/report/plan_004_step2_report.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"irt_equated_bench_regen\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-21T00:58:16.451993+00:00\\\", \\\"tags\\\": [\\\"plan_004\\\", \\\"gsm8k\\\", \\\"report\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_42613e\", \"name\": \"plan_004_step2_report\", \"type\": \"report\", \"description\": \"Plan 004 Step 2 report: GSM8K semi-synthetic DIF injection results, comparison with MMLU plan_011\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/report/plan_004_step2_report.md\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T00:58:16.451993+00:00\", \"tags\": [\"plan_004\", \"gsm8k\", \"report\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "990c3632-b009-4ef2-bce1-fb7023af182a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-21T00:58:29.124Z_

全部完成。核心结果：

### GSM8K vs MMLU 对比

| 指标 | MMLU plan_011 (external) | GSM8K (external) | GSM8K (standard) |
|------|--------------------------|------------------|-------------------|
| Baseline FPR | 0.314 | **0.471** | 0.191 |
| ΔTPR p=0.5 | +0.508 | **+0.514** | **+0.749** |
| ΔTPR p=1.0 | +0.674 | +0.517 | **+0.818** |

### 关键发现

1. **Standard matching 表现优于预期**：baseline FPR 仅 19.1%，ΔTPR 在 p=0.5 就达到 +0.749，p=0.7 时 TPR 已饱和至 1.000。比 MMLU 的 external matching 更强。

2. **External matching 灵敏度极高但 FPR 太高**：p=0.3 时 TPR 已达 0.970，但 baseline FPR 高达 47.1%（与 Step 1 的 47.4% C-rate 一致）。FPR 不随 p 变化（预期行为——外部分数不受 GSM8K 注入影响），但这意味着 external matching 在 GSM8K 上无法区分真实 temporal DIF 和注入污染。

3. **Standard matching 的 FPR 膨胀**：从 p=0 的 0.191 升至 p=1.0 的 0.645，符合预期——20% items 被注入时 matching variable 被污染。

4. **方法论在 GSM8K 上验证成功**：standard matching 展现清晰的 dose-response，ΔTPR 单调递增，Fisher exact test 显著。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5094949-d1fd-4ff2-8049-7c266f377965",
  "isSidechain": false,
  "requestId": "req_011CbEok6k7wojPTjBhHT2bf",
  "type": "assistant",
  "uuid": "30414ce3-f2ea-4bb0-a063-8229d18d5b79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011va6foQhdRTvmzkNPNBeUh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2326,
      "cache_read_input_tokens": 57653,
      "output_tokens": 517,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2326,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 517,
          "cache_read_input_tokens": 57653,
          "cache_creation_input_tokens": 2326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2326
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

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## 任务：plan_004 Step 2 — GSM8K Semi-Synthetic Injection（复制 plan_011 方法）  **P0 紧急。** 在 GSM8K response matrix 上验证 DIF 方法论有效性。  ### 背景  Step 1 已完成：GSM8K temporal DIF 确认存在（standard 18.9% C, external 47.4%…",
  "leafUuid": "30414ce3-f2ea-4bb0-a063-8229d18d5b79",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "GSM8K semi-synthetic DIF injection validation",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5"
}
```

---
