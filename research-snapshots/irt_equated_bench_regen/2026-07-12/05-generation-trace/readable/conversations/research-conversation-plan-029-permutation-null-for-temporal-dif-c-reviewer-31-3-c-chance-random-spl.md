# Research conversation: 任务: plan_029 — Permutation Null for Temporal DIF C% ### 目标 Reviewer 问"31.3% C% 是否高于 chance"。当前 random-split control (0.1

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd.jsonl`
- **Structured JSON:** [`e17632d4e239857fdef0.json`](../../sessions/e1/e17632d4e239857fdef0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T10:01:21.369Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T10:01:21.369Z",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd",
  "content": "## 任务: plan_029 — Permutation Null for Temporal DIF C%\n\n### 目标\nReviewer 问\"31.3% C% 是否高于 chance\"。当前 random-split control (0.18%) 是 within-same-cohort，不是 temporal label permutation null。做 1000 次 permutation 建立 C% null distribution。\n\n### 方法\n1. 加载 response matrix: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix.npz`（scipy sparse CSR, 5227×12508, int8 binary）\n2. 加载 index: `artifacts/response_matrix_index.npz`（model_names, item_ids）\n3. 加载 model metadata: `artifacts/model_metadata.csv`（cohort_temporal 列: \"2023\" N=1080, \"2024\" N=807）\n4. 1000 次 permutation:\n   - 保持 N_ref=1080, N_foc=807 不变\n   - 从全部 1887 个有 temporal label 的 models 中随机重新分配 labels\n   - 每次跑标准 MH-DIF，记录 C%\n5. 报告: null distribution mean ± SD, p-value (观测 31.3% 的位置), 95% CI of null, histogram\n\n### MH-DIF 函数参考\n参考 plan_001 的 mh_dif() 实现（purified matching, 5 strata）:\n```\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_analysis.py\n```\n\n核心：\n- purified_score = total_score - item_j_response（去除待检测 item）\n- 5 quantile strata on pooled purified scores\n- α_MH = Σ(A_k D_k / N_k) / Σ(B_k C_k / N_k)\n- Δ_MH = -2.35 × ln(α_MH)\n- ETS: |Δ_MH| < 1.0 → A, 1.0-1.5 → B, ≥1.5 + p<0.05 → C\n\n### 性能注意\n- 单次 MH-DIF 跑 12508 items 大约需要几分钟\n- 1000 次 ≈ 几小时。如果太慢：\n  a) 先跑 100 次，报告初步结果\n  b) 考虑优化：向量化 strata computation，或只跑一个 representative subset of items\n  c) 如果100次就已经 p<0.001（即 null C% 远低于 31.3%），可以停在那里\n- 用 numpy random seed 42 for reproducibility\n- 可以用 joblib/multiprocessing 并行，但注意 RAM（每次需要 ~5227×12508 的子矩阵）\n\n### 优化建议\n- 可以先计算一次 total scores（不变），每次 permutation 只重新 split model indices\n- 使用矩阵运算代替逐 item 循环（如果可以）\n- 考虑只跑 reference/focal 子矩阵而非全矩阵\n\n### 输出\n在 `artifacts/plan_029_permutation_null/` 目录下:\n- `permutation_null_report.md` — 包含: null mean ± SD, p-value, 95% CI, 观测值 vs null\n- `plan_029_permutation_null.py` — 分析脚本\n- `permutation_results.csv` — 每次 permutation 的 C%\n- `fig_permutation_null.png` — histogram of null distribution + 观测值标记\n\n### 关键路径\n- 项目根: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/`\n- 数据: `artifacts/response_matrix.npz`, `artifacts/response_matrix_index.npz`, `artifacts/model_metadata.csv`\n- 参考代码: `artifacts/plan_001/plan_001_analysis.py`\n\n### 验证\n- 确保 permutation 保持组大小不变 (1080 vs 807)\n- 确保只用有 temporal label 的 models（不是全部 5227）\n- 脚本完成后验证输出文件存在且非空\n- 如果 100 次结果已经 conclusive（null C% 全部 < 5%），在 report 中说明并继续跑到 1000\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T10:01:21.373Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T10:01:21.373Z",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd"
}
```

---

## Round 1

26 recorded events

### User

_source line 3 · 2026-05-21T10:01:21.407Z_

## 任务: plan_029 — Permutation Null for Temporal DIF C%

### 目标
Reviewer 问"31.3% C% 是否高于 chance"。当前 random-split control (0.18%) 是 within-same-cohort，不是 temporal label permutation null。做 1000 次 permutation 建立 C% null distribution。

### 方法
1. 加载 response matrix: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix.npz`（scipy sparse CSR, 5227×12508, int8 binary）
2. 加载 index: `artifacts/response_matrix_index.npz`（model_names, item_ids）
3. 加载 model metadata: `artifacts/model_metadata.csv`（cohort_temporal 列: "2023" N=1080, "2024" N=807）
4. 1000 次 permutation:
   - 保持 N_ref=1080, N_foc=807 不变
   - 从全部 1887 个有 temporal label 的 models 中随机重新分配 labels
   - 每次跑标准 MH-DIF，记录 C%
5. 报告: null distribution mean ± SD, p-value (观测 31.3% 的位置), 95% CI of null, histogram

### MH-DIF 函数参考
参考 plan_001 的 mh_dif() 实现（purified matching, 5 strata）:
```
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_analysis.py
```

核心：
- purified_score = total_score - item_j_response（去除待检测 item）
- 5 quantile strata on pooled purified scores
- α_MH = Σ(A_k D_k / N_k) / Σ(B_k C_k / N_k)
- Δ_MH = -2.35 × ln(α_MH)
- ETS: |Δ_MH| < 1.0 → A, 1.0-1.5 → B, ≥1.5 + p<0.05 → C

### 性能注意
- 单次 MH-DIF 跑 12508 items 大约需要几分钟
- 1000 次 ≈ 几小时。如果太慢：
  a) 先跑 100 次，报告初步结果
  b) 考虑优化：向量化 strata computation，或只跑一个 representative subset of items
  c) 如果100次就已经 p<0.001（即 null C% 远低于 31.3%），可以停在那里
- 用 numpy random seed 42 for reproducibility
- 可以用 joblib/multiprocessing 并行，但注意 RAM（每次需要 ~5227×12508 的子矩阵）

### 优化建议
- 可以先计算一次 total scores（不变），每次 permutation 只重新 split model indices
- 使用矩阵运算代替逐 item 循环（如果可以）
- 考虑只跑 reference/focal 子矩阵而非全矩阵

### 输出
在 `artifacts/plan_029_permutation_null/` 目录下:
- `permutation_null_report.md` — 包含: null mean ± SD, p-value, 95% CI, 观测值 vs null
- `plan_029_permutation_null.py` — 分析脚本
- `permutation_results.csv` — 每次 permutation 的 C%
- `fig_permutation_null.png` — histogram of null distribution + 观测值标记

### 关键路径
- 项目根: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/`
- 数据: `artifacts/response_matrix.npz`, `artifacts/response_matrix_index.npz`, `artifacts/model_metadata.csv`
- 参考代码: `artifacts/plan_001/plan_001_analysis.py`

### 验证
- 确保 permutation 保持组大小不变 (1080 vs 807)
- 确保只用有 temporal label 的 models（不是全部 5227）
- 脚本完成后验证输出文件存在且非空
- 如果 100 次结果已经 conclusive（null C% 全部 < 5%），在 report 中说明并继续跑到 1000


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "675b7191-b2b7-49a7-b6a4-83def2b806ad",
  "type": "user",
  "uuid": "b666e532-e6aa-4252-8109-40162d1a8a13",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T10:01:21.406Z_

```json
{
  "parentUuid": "b666e532-e6aa-4252-8109-40162d1a8a13",
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
      "mcp__agent-ml-research__save_project_file"
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
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "f1f6e45e-135c-4df9-a74b-067a43087b47",
  "timestamp": "2026-05-21T10:01:21.406Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T10:01:21.406Z_

```json
{
  "parentUuid": "f1f6e45e-135c-4df9-a74b-067a43087b47",
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
  "uuid": "f6559a9b-0969-40f5-a601-07dc9d1a1277",
  "timestamp": "2026-05-21T10:01:21.406Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-21T10:01:21.406Z_

```json
{
  "parentUuid": "f6559a9b-0969-40f5-a601-07dc9d1a1277",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "deab0106-496e-4588-ae14-001016a08c01",
  "timestamp": "2026-05-21T10:01:21.406Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Permutation null distribution for temporal DIF C%",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd"
}
```

---

### Assistant

_source line 8 · 2026-05-21T10:01:26.498Z_

<details><summary>Logged reasoning block</summary>

```text
Let me understand the task: I need to implement a permutation null test for temporal DIF C% to answer whether the observed 31.3% C% is higher than chance. Let me start by reading the reference code and data files to understand the existing implementation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "deab0106-496e-4588-ae14-001016a08c01",
  "isSidechain": false,
  "requestId": "req_011CbFXA4pyhKTypPhnmC26D",
  "type": "assistant",
  "uuid": "0f055038-65c8-4b3e-b393-e4ed984ab0be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhNRcjYdK9HHpfd2UR7bZ6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12764,
      "cache_read_input_tokens": 11841,
      "output_tokens": 534,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 534,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12764
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

_source line 9 · 2026-05-21T10:01:27.142Z_

Let me start by reading the reference MH-DIF implementation and checking the data files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f055038-65c8-4b3e-b393-e4ed984ab0be",
  "isSidechain": false,
  "requestId": "req_011CbFXA4pyhKTypPhnmC26D",
  "type": "assistant",
  "uuid": "96efd79b-6852-4a6b-86b0-43f34561a626",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhNRcjYdK9HHpfd2UR7bZ6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12764,
      "cache_read_input_tokens": 11841,
      "output_tokens": 534,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 534,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12764
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

_source line 10 · 2026-05-21T10:01:27.791Z_

<details open><summary>🔧 Tool call — Read · `toolu_015GXJZtirktxE8n8BbNzxsh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96efd79b-6852-4a6b-86b0-43f34561a626",
  "isSidechain": false,
  "requestId": "req_011CbFXA4pyhKTypPhnmC26D",
  "type": "assistant",
  "uuid": "85faafeb-5165-4a1f-91f7-e99addf03425",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhNRcjYdK9HHpfd2UR7bZ6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12764,
      "cache_read_input_tokens": 11841,
      "output_tokens": 534,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 534,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12764
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

_source line 11 · 2026-05-21T10:01:28.677Z_

<details><summary>↩ Tool result · `toolu_015GXJZtirktxE8n8BbNzxsh`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_001_analysis.py — METABENCH real-data MH-DIF analysis
4	
5	Runs purified Mantel-Haenszel DIF detection on MMLU binary response data with
6	two cohort definitions (temporal 2023-vs-2024, ability Q1-2 vs Q4-5), validates
7	against Li et al. contamination proxy labels, and performs within-family,
8	domain-specificity, and negative-discrimination sensitivity analyses.
9	
10	Inputs  (all in ../):
11	  response_matrix.npz          — (5227, 12508) CSR sparse, int8 binary
12	  response_matrix_index.npz    — model_names, item_ids
13	  model_metadata.csv           — cohort_temporal, cohort_accuracy_quintile, family
14	  item_metadata.csv            — subject, is_negative_disc
15	  mmlu_li2024_proxy_labels.csv — contamination_type proxy labels
16	
17	Outputs (all in ./):
18	  dif_results_temporal.csv, dif_results_ability.csv, dif_summary.csv,
19	  within_family_dif.csv, cross_analysis.csv, domain_specificity.csv,
20	  neg_disc_sensitivity.csv, plan_001_report.md
21	
22	Dependencies: numpy, scipy, pandas
23	"""
24	
25	import numpy as np
26	import pandas as pd
27	from scipy.sparse import load_npz
28	from scipy.stats import chi2 as chi2_dist, spearmanr
29	from pathlib import Path
30	import time
31	import warnings
32	
33	warnings.filterwarnings("ignore", category=RuntimeWarning)
34	
35	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
36	OUT = BASE / "plan_001"
37	OUT.mkdir(exist_ok=True)
38	
39	
40	# ════════════════════════════════════════════════════════════════════════════
41	#  DATA LOADING
42	# ════════════════════════════════════════════════════════════════════════════
43	print("=== Loading data ===")
44	mat = load_npz(BASE / "response_matrix.npz")
45	X = mat.toarray().astype(np.int16)          # (5227, 12508)
46	del mat
47	
48	idx = np.load(BASE / "response_matrix_index.npz", allow_pickle=True)
49	MODEL_NAMES = idx["model_names"]             # (5227,)
50	ITEM_IDS    = idx["item_ids"]                # (12508,)
51	
52	model_meta = pd.read_csv(BASE / "model_metadata.csv")
53	item_meta  = pd.read_csv(BASE / "item_metadata.csv")
54	li_labels  = pd.read_csv(BASE / "mmlu_li2024_proxy_labels.csv")
55	
56	NAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}
57	N_MODELS, J = X.shape
58	print(f"  Matrix {N_MODELS}×{J}")
59	print(f"  Li annotated: {(li_labels.contamination_type != 'no_annotation').sum()}, "
60	      f"no_annotation: {(li_labels.contamination_type == 'no_annotation').sum()}")
61	
62	
63	# ════════════════════════════════════════════════════════════════════════════
64	#  MH-DIF CORE
65	# ════════════════════════════════════════════════════════════════════════════
66	def mh_dif(X_ref, X_foc, n_strata=5, col_mask=None):
67	    """
68	    Purified Mantel-Haenszel DIF for all items (or a column subset).
69	
70	    For item j the matching variable is:
71	        purified_score = total_score_across_all_columns - response_to_item_j
72	
73	    Parameters
74	    ----------
75	    X_ref, X_foc : ndarray (N_ref, J) and (N_foc, J), int, binary 0/1
76	    n_strata     : number of quantile-based score strata
77	    col_mask     : bool array (J,); True = analyse this column.  None = all.
78	
79	    Returns
80	    -------
81	    DataFrame with cols: col_idx, alpha_mh, delta_mh, se, chi2, p_value, ets_class
82	    """
83	    _Nr, Jc = X_ref.shape
84	
85	    # row-wise total scores (used for purified matching)
86	    tot_ref = X_ref.sum(axis=1).astype(np.float64)   # (N_ref,)
87	    tot_foc = X_foc.sum(axis=1).astype(np.float64)   # (N_foc,)
88	
89	    cols = np.where(col_mask)[0] if col_mask is not None else np.arange(Jc)
90	    rows = []
91	    t0 = time.time()
92	
93	    for pos, j in enumerate(cols):
94	        if pos % 2500 == 0 and pos > 0:
95	            print(f"    {pos}/{len(cols)}  ({time.time()-t0:.0f}s)")
96	
97	        # ── purified scores: exclude item j from matching variable ──
98	        s_ref = tot_ref - X_ref[:, j].astype(np.float64)
99	        s_foc = tot_foc - X_foc[:, j].astype(np.float64)
100	
101	        # ── quantile-based strata on pooled purified scores ──
102	        s_all = np.concatenate([s_ref, s_foc])
103	        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
104	        if len(edges) < 2:
105	            rows.append(_nan_row(j))
106	            continue
107	        n_bins = len(edges) - 1
108	
109	        k_ref = np.digitize(s_ref, edges[1:-1])      # values in [0, n_bins-1]
110	        k_foc = np.digitize(s_foc, edges[1:-1])
111	
112	        # ── accumulate MH statistics across strata ──
113	        #   α_MH = R / S  where  R = Σ A_k D_k / N_k,  S = Σ B_k C_k / N_k
114	        #   Δ_MH = −2.35 · ln(α_MH)
115	        R = S = 0.0
116	        sum_diff = 0.0       # Σ (A_k − E[A_k])
117	        sum_var  = 0.0       # Σ Var(A_k)
118	        # Robins-Breslow-Greenland variance components for ln(α_MH)
119	        pr = ps_qr = qs = 0.0
120	        n_ok = 0
121	
122	        for k in range(n_bins):
123	            mr = (k_ref == k)
124	            mf = (k_foc == k)
125	            n1 = int(mr.sum())           # ref count in stratum
126	            n0 = int(mf.sum())           # foc count in stratum
127	            if n1 == 0 or n0 == 0:
128	                continue
129	
130	            A = float(X_ref[mr, j].sum())   # ref correct
131	            B = float(n1 - A)               # ref incorrect
132	            C = float(X_foc[mf, j].sum())   # foc correct
133	            D = float(n0 - C)               # foc incorrect
134	            Nk = float(n1 + n0)
135	            m1 = A + C                       # total correct
136	            m0 = B + D                       # total incorrect
137	
138	            if m1 == 0 or m0 == 0 or Nk <= 1:
139	                continue
140	            n_ok += 1
141	
142	            Rk = A * D / Nk
143	            Sk = B * C / Nk
144	            R += Rk
145	            S += Sk
146	
147	            # E[A_k] = n1·m1 / N_k
148	            EA = n1 * m1 / Nk
149	            sum_diff += A - EA
150	            # Var(A_k) = n1·n0·m1·m0 / (N_k²·(N_k−1))
151	            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))
152	
153	            # RBG components: P_k = (A+D)/N, Q_k = (B+C)/N
154	            Pk = (A + D) / Nk
155	            Qk = (B + C) / Nk
156	            pr    += Pk * Rk
157	            ps_qr += Pk * Sk + Qk * Rk
158	            qs    += Qk * Sk
159	
160	        if n_ok == 0 or (R == 0 and S == 0):
161	            rows.append(_nan_row(j))
162	            continue
163	
164	        # ── MH odds ratio ──
165	        if S == 0:
166	            alpha, delta, se = np.inf, -np.inf, np.nan
167	        elif R == 0:
168	            alpha, delta, se = 0.0, np.inf, np.nan
169	        else:
170	            alpha = R / S
171	            delta = -2.35 * np.log(alpha)
172	            # SE via Robins-Breslow-Greenland:
173	            #   Var(ln α) = pr/(2R²) + ps_qr/(2RS) + qs/(2S²)
174	            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)
175	            se = 2.35 * np.sqrt(v) if v > 0 else np.nan
176	
177	        # ── MH χ² with continuity correction (df=1) ──
178	        if sum_var > 0:
179	            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var
180	            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)
181	        else:
182	            chi2_stat = pval = np.nan
183	
184	        # ── ETS classification ──
185	        #   A: |Δ| < 1.0
186	        #   C: |Δ| ≥ 1.5 AND p < 0.05
187	        #   B: everything else
188	        ad = abs(delta) if np.isfinite(delta) else 0.0
189	        if ad < 1.0:
190	            ets = "A"
191	        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:
192	            ets = "C"
193	        else:
194	            ets = "B"
195	
196	        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,
197	                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets))
198	
199	    elapsed = time.time() - t0
200	    print(f"    done — {len(cols)} items in {elapsed:.1f}s")
201	    return pd.DataFrame(rows)
202	
203	
204	def _nan_row(j):
205	    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,
206	                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class="A")
207	
208	
209	# ════════════════════════════════════════════════════════════════════════════
210	#  HELPERS
211	# ════════════════════════════════════════════════════════════════════════════
212	def rows_for(col, values):
213	    """Row indices into X for models matching model_meta[col] ∈ values."""
214	    names = model_meta.loc[model_meta[col].isin(values), "model_name"]
215	    return np.array([NAME2ROW[n] for n in names if n in NAME2ROW])
216	
217	
218	def enrich(df):
219	    """Attach item_id, subject, Li labels to DIF results (col_idx → item_id)."""
220	    df = df.copy()
221	    df["item_id"] = [ITEM_IDS[i] for i in df["col_idx"]]
222	    df = df.merge(item_meta[["item_id", "subject"]], on="item_id", how="left")
223	    df = df.merge(
224	        li_labels[["item_id", "is_contaminated", "contamination_type"]].rename(
225	            columns={"is_contaminated": "li_label",
226	                     "contamination_type": "li_contamination_type"}),
227	        on="item_id", how="left",
228	    )
229	    return df
230	
231	
232	def li_metrics(df):
233	    """FPR, contaminated rate, enrichment from enriched DIF results."""
234	    is_c   = df["ets_class"] == "C"
235	    clean  = df["li_contamination_type"] == "clean"
236	    contam = df["li_contamination_type"].isin(["input_only", "input_and_label"])
237	    unlab  = df["li_contamination_type"] == "no_annotation"
238	
239	    r_clean  = is_c[clean].mean()  if clean.any()  else np.nan
240	    r_contam = is_c[contam].mean() if contam.any() else np.nan
241	    r_unlab  = is_c[unlab].mean()  if unlab.any()  else np.nan
242	    enrich   = r_contam / r_clean  if r_clean > 0  else np.nan
243	
244	    return dict(fpr_vs_li_clean=r_clean, rate_contaminated=r_contam,
245	                rate_clean=r_clean, rate_unlabeled=r_unlab,
246	                enrichment_ratio=enrich)
247	
248	
249	def summary_row(cohort, filt, df):
250	    vc = df["ets_class"].value_counts()
251	    n  = len(df)
252	    lm = li_metrics(df)
253	    return dict(
254	        cohort_type=cohort, item_filter=filt, n_items=n,
255	        n_ets_a=vc.get("A", 0), n_ets_b=vc.get("B", 0), n_ets_c=vc.get("C", 0),
256	        pct_c=vc.get("C", 0) / n * 100 if n > 0 else 0,
257	        fpr_vs_li_clean=lm["fpr_vs_li_clean"],
258	        enrichment_ratio=lm["enrichment_ratio"],
259	    )
260	
261	
262	# ════════════════════════════════════════════════════════════════════════════
263	#  MAIN
264	# ════════════════════════════════════════════════════════════════════════════
265	def main():
266	    summary_rows = []
267	
268	    # ── Step 1-2: MH-DIF — Temporal cohort ─────────────────────────────────
269	    print("\n=== Step 1-2a: Temporal cohort DIF (2023 vs 2024, 5 strata) ===")
270	    ref_t = rows_for("cohort_temporal", ["2023"])
271	    foc_t = rows_for("cohort_temporal", ["2024"])
272	    print(f"  N_ref={len(ref_t)}, N_foc={len(foc_t)}")
273	
274	    dif_temp = mh_dif(X[ref_t], X[foc_t], n_strata=5)
275	    dif_temp = enrich(dif_temp)
276	    print(f"  ETS: {dif_temp.ets_class.value_counts().to_dict()}")
277	    summary_rows.append(summary_row("temporal", "all", dif_temp))
278	
279	    # ── Step 1-2: MH-DIF — Ability cohort ──────────────────────────────────
280	    print("\n=== Step 1-2b: Ability cohort DIF (Q1-2 vs Q4-5, 10 strata) ===")
281	    ref_a = rows_for("cohort_accuracy_quintile", [1, 2])
282	    foc_a = rows_for("cohort_accuracy_quintile", [4, 5])
283	    print(f"  N_ref={len(ref_a)}, N_foc={len(foc_a)}")
284	
285	    dif_abil = mh_dif(X[ref_a], X[foc_a], n_strata=10)
286	    dif_abil = enrich(dif_abil)
287	    print(f"  ETS: {dif_abil.ets_class.value_counts().to_dict()}")
288	    summary_rows.append(summary_row("ability", "all", dif_abil))
289	
290	    # ── Step 3: Li et al. proxy validation ─────────────────────────────────
291	    print("\n=== Step 3: Li et al. proxy validation ===")
292	    li_t = li_metrics(dif_temp)
293	    li_a = li_metrics(dif_abil)
294	    print(f"  Temporal — FPR={li_t['fpr_vs_li_clean']:.4f}, "
295	          f"enrichment={li_t['enrichment_ratio']:.2f}")
296	    print(f"  Ability  — FPR={li_a['fpr_vs_li_clean']:.4f}, "
297	          f"enrichment={li_a['enrichment_ratio']:.2f}")
298	
299	    # ── Step 4: Within-family analysis ─────────────────────────────────────
300	    print("\n=== Step 4: Within-family DIF ===")
301	
302	    # Show family × temporal distribution
303	    fam_temp = (model_meta.groupby(["family", "cohort_temporal"])
304	                .size().unstack(fill_value=0))
305	    print("  Family × temporal counts:")
306	    for fam in ["llama-2", "llama-3", "mistral", "mixtral", "solar", "zephyr"]:
307	        if fam in fam_temp.index:
308	            print(f"    {fam}: {fam_temp.loc[fam].to_dict()}")
309	
310	    family_pairs = []
311	
312	    # (A) Cross-family comparisons (related families)
313	    llama2_idx = rows_for("family", ["llama-2"])
314	    llama3_idx = rows_for("family", ["llama-3"])
315	    if len(llama2_idx) >= 80 and len(llama3_idx) >= 80:
316	        family_pairs.append(("llama-2", "llama-3", llama2_idx, llama3_idx))
317	
318	    mistral_idx = rows_for("family", ["mistral"])
319	    mixtral_idx = rows_for("family", ["mixtral"])
320	    if len(mistral_idx) >= 80 and len(mixtral_idx) >= 80:
321	        family_pairs.append(("mistral", "mixtral", mistral_idx, mixtral_idx))
322	
323	    # (B) Within single family, temporal split (where both groups >= 40)
324	    for fam in ["unknown", "mistral", "llama-3", "llama-2"]:
325	        fam_df = model_meta[model_meta["family"] == fam]
326	        r_names = fam_df.loc[fam_df.cohort_temporal == "2023", "model_name"]
327	        f_names = fam_df.loc[fam_df.cohort_temporal == "2024", "model_name"]
328	        ri = np.array([NAME2ROW[n] for n in r_names if n in NAME2ROW])
329	        fi = np.array([NAME2ROW[n] for n in f_names if n in NAME2ROW])
330	        if len(ri) >= 40 and len(fi) >= 40:
331	            family_pairs.append((f"{fam}_2023", f"{fam}_2024", ri, fi))
332	
333	    wf_parts = []
334	    for rname, fname, ri, fi in family_pairs:
335	        ns = 5 if min(len(ri), len(fi)) < 200 else 10
336	        print(f"  {rname} (N={len(ri)}) vs {fname} (N={len(fi)}), {ns} strata")
337	        wf = mh_dif(X[ri], X[fi], n_strata=ns)
338	        wf = enrich(wf)
339	        wf["ref_group"] = rname
340	        wf["foc_group"] = fname
341	        wf_parts.append(wf)
342	        print(f"    ETS: {wf.ets_class.value_counts().to_dict()}")
343	
344	    wf_all = pd.concat(wf_parts, ignore_index=True) if wf_parts else pd.DataFrame()
345	
346	    # Cross-cohort vs within-family comparison
347	    print("\n=== Step 4 cont: Cross analysis ===")
348	    cross_rows = []
349	    for rname, fname, _, _ in family_pairs:
350	        wf_sub = wf_all[(wf_all.ref_group == rname) & (wf_all.foc_group == fname)]
351	        for _, wr in wf_sub.iterrows():
352	            iid = wr["item_id"]
353	            tr = dif_temp.loc[dif_temp.item_id == iid]
354	            if tr.empty:
355	                continue
356	            tr = tr.iloc[0]
357	            cross_rows.append(dict(
358	                item_id=iid, subject=wr["subject"],
359	                temporal_ets=tr["ets_class"], temporal_delta=tr["delta_mh"],
360	                wf_pair=f"{rname}_vs_{fname}",
361	                wf_ets=wr["ets_class"], wf_delta=wr["delta_mh"],
362	                li_contamination_type=wr.get("li_contamination_type", np.nan),
363	            ))
364	    cross_df = pd.DataFrame(cross_rows)
365	
366	    if not cross_df.empty:
367	        for pair in cross_df["wf_pair"].unique():
368	            sub = cross_df[cross_df.wf_pair == pair]
369	            tc = sub.temporal_ets == "C"
370	            wc = sub.wf_ets == "C"
371	            print(f"  {pair}: both_C={int((tc & wc).sum())}, "
372	                  f"temp_only_C={int((tc & ~wc).sum())}, "
373	                  f"wf_only_C={int((~tc & wc).sum())}, "
374	                  f"neither={int((~tc & ~wc).sum())}")
375	
376	    # ── Step 5: Domain specificity ─────────────────────────────────────────
377	    print("\n=== Step 5: Domain specificity ===")
378	
379	    # C rate per subject (temporal cohort)
380	    subj_c = (dif_temp.groupby("subject")["ets_class"]
381	              .agg(n_items="size", n_ets_c=lambda x: (x == "C").sum()))
382	    subj_c["pct_c"] = subj_c["n_ets_c"] / subj_c["n_items"] * 100
383	
384	    # Per-item accuracy for 2023 and 2024 models
385	    acc_2023 = X[ref_t].mean(axis=0).astype(np.float64)   # (J,)
386	    acc_2024 = X[foc_t].mean(axis=0).astype(np.float64)
387	
388	    item_acc = pd.DataFrame({"item_id": ITEM_IDS, "acc_2023": acc_2023, "acc_2024": acc_2024})
389	    item_acc = item_acc.merge(item_meta[["item_id", "subject"]], on="item_id")
390	    subj_acc = item_acc.groupby("subject")[["acc_2023", "acc_2024"]].mean()
391	    subj_acc["acc_change"] = subj_acc["acc_2024"] - subj_acc["acc_2023"]
392	
393	    domain_df = subj_c.join(subj_acc, how="inner")
394	    rho, rho_p = spearmanr(domain_df["pct_c"], domain_df["acc_change"])
395	    print(f"  Spearman(pct_C, acc_change) = {rho:.3f}, p = {rho_p:.4f}")
396	    print("  Top 5 by C rate:")
397	    for subj, row in domain_df.nlargest(5, "pct_c").iterrows():
398	        print(f"    {subj}: {row.pct_c:.1f}% C ({int(row.n_ets_c)}/{int(row.n_items)}), "
399	              f"Δacc={row.acc_change:+.3f}")
400	
401	    # ── Step 6: Negative-discrimination sensitivity ────────────────────────
402	    print("\n=== Step 6: Negative-disc sensitivity ===")
403	    neg_mask = item_meta.set_index("item_id").reindex(ITEM_IDS)["is_negative_disc"].values
404	    pos_mask = ~neg_mask
405	    n_neg = int(neg_mask.sum())
406	    n_pos = int(pos_mask.sum())
407	    print(f"  All={J}, neg_disc={n_neg}, non_neg={n_pos}")
408	
409	    # Re-run temporal DIF on non-negative-disc items only
410	    # (total scores also computed only on non-neg items)
411	    pos_cols = np.where(pos_mask)[0]
412	    dif_temp_nn = mh_dif(X[np.ix_(ref_t, pos_cols)],
413	                         X[np.ix_(foc_t, pos_cols)], n_strata=5)
414	
415	    # Map col_idx back to original item space
416	    dif_temp_nn["col_idx_orig"] = [pos_cols[c] for c in dif_temp_nn["col_idx"]]
417	    dif_temp_nn["item_id"] = [ITEM_IDS[pos_cols[c]] for c in dif_temp_nn["col_idx"]]
418	    dif_temp_nn = dif_temp_nn.merge(
419	        li_labels[["item_id", "is_contaminated", "contamination_type"]].rename(
420	            columns={"is_contaminated": "li_label",
421	                     "contamination_type": "li_contamination_type"}),
422	        on="item_id", how="left",
423	    )
424	
425	    n_c_all = int((dif_temp["ets_class"] == "C").sum())
426	    n_c_nn  = int((dif_temp_nn["ets_class"] == "C").sum())
427	    # C count among neg-disc items in the full run
428	    neg_col_set = set(np.where(neg_mask)[0])
429	    n_c_neg = int((dif_temp.loc[dif_temp.col_idx.isin(neg_col_set), "ets_class"] == "C").sum())
430	
431	    neg_disc_df = pd.DataFrame([
432	        dict(item_set="all",               n_items=J,     n_ets_c=n_c_all,
433	             pct_c=n_c_all / J * 100),
434	        dict(item_set="non_negative_disc",  n_items=n_pos, n_ets_c=n_c_nn,
435	             pct_c=n_c_nn / n_pos * 100),
436	        dict(item_set="negative_disc_only", n_items=n_neg, n_ets_c=n_c_neg,
437	             pct_c=n_c_neg / n_neg * 100 if n_neg > 0 else 0),
438	    ])
439	    print(neg_disc_df.to_string(index=False))
440	
441	    summary_rows.append(summary_row("temporal", "non_neg_disc", dif_temp_nn))
442	
443	    # ── Sanity check: random half-split of 2023 cohort ─────────────────────
444	    print("\n=== Sanity check: random half-split of 2023 cohort ===")
445	    rng = np.random.RandomState(42)
446	    perm = rng.permutation(len(ref_t))
447	    half = len(perm) // 2
448	    san_ref = ref_t[perm[:half]]
449	    san_foc = ref_t[perm[half:]]
450	    print(f"  Split: {len(san_ref)} vs {len(san_foc)}")
451	    dif_san = mh_dif(X[san_ref], X[san_foc], n_strata=5)
452	    vc_san = dif_san["ets_class"].value_counts()
453	    n_c_san = vc_san.get("C", 0)
454	    pct_c_san = n_c_san / len(dif_san) * 100
455	    print(f"  ETS C: {n_c_san}/{len(dif_san)} = {pct_c_san:.2f}% (expect <5%)")
456	
457	    # ── Save all outputs ───────────────────────────────────────────────────
458	    print("\n=== Saving outputs ===")
459	
460	    out_cols = ["item_id", "subject", "alpha_mh", "delta_mh", "se",
461	                "p_value", "ets_class", "li_label", "li_contamination_type"]
462	    dif_temp[out_cols].to_csv(OUT / "dif_results_temporal.csv", index=False)
463	    dif_abil[out_cols].to_csv(OUT / "dif_results_ability.csv", index=False)
464	
465	    summary_df = pd.DataFrame(summary_rows)
466	    summary_df.to_csv(OUT / "dif_summary.csv", index=False)
467	
468	    if not wf_all.empty:
469	        wf_cols = ["item_id", "subject", "ref_group", "foc_group",
470	                   "alpha_mh", "delta_mh", "se", "p_value", "ets_class",
471	                   "li_label", "li_contamination_type"]
472	        wf_all[[c for c in wf_cols if c in wf_all.columns]].to_csv(
473	            OUT / "within_family_dif.csv", index=False)
474	
475	    if not cross_df.empty:
476	        cross_df.to_csv(OUT / "cross_analysis.csv", index=False)
477	
478	    domain_df.reset_index().to_csv(OUT / "domain_specificity.csv", index=False)
479	    neg_disc_df.to_csv(OUT / "neg_disc_sensitivity.csv", index=False)
480	
481	    # ── Cohort overlap ─────────────────────────────────────────────────────
482	    temp_c = set(dif_temp.loc[dif_temp.ets_class == "C", "item_id"])
483	    abil_c = set(dif_abil.loc[dif_abil.ets_class == "C", "item_id"])
484	    overlap = temp_c & abil_c
485	    union   = temp_c | abil_c
486	    jaccard = len(overlap) / len(union) if union else 0
487	
488	    # ── Console summary ────────────────────────────────────────────────────
489	    print("\n" + "=" * 60)
490	    print("SUMMARY")
491	    print("=" * 60)
492	    print(f"\nTemporal (2023 vs 2024, 5 strata):")
493	    print(f"  ETS: {dif_temp.ets_class.value_counts().to_dict()}")
494	    print(f"  FPR vs Li clean = {li_t['fpr_vs_li_clean']:.4f}")
495	    print(f"  Enrichment = {li_t['enrichment_ratio']:.2f}")
496	    print(f"\nAbility (Q1-2 vs Q4-5, 10 strata):")
497	    print(f"  ETS: {dif_abil.ets_class.value_counts().to_dict()}")
498	    print(f"  FPR vs Li clean = {li_a['fpr_vs_li_clean']:.4f}")
499	    print(f"  Enrichment = {li_a['enrichment_ratio']:.2f}")
500	    print(f"\nSanity check (random split): {pct_c_san:.2f}% C")
501	    print(f"Domain ρ(C_rate, Δacc) = {rho:.3f}, p = {rho_p:.4f}")
502	    print(f"Cohort overlap: temp_C={len(temp_c)}, abil_C={len(abil_c)}, "
503	          f"both={len(overlap)}, Jaccard={jaccard:.3f}")
504	
505	    # ── Generate report ────────────────────────────────────────────────────
506	    _write_report(dif_temp, dif_abil, li_t, li_a, summary_df,
507	                  domain_df, rho, rho_p, neg_disc_df, pct_c_san,
508	                  wf_all, cross_df, temp_c, abil_c, overlap, jaccard,
509	                  ref_t, foc_t, ref_a, foc_a)
510	
511	    print(f"\nAll outputs saved to {OUT}")
512	
513	
514	# ════════════════════════════════════════════════════════════════════════════
515	#  REPORT
516	# ════════════════════════════════════════════════════════════════════════════
517	def _write_report(dif_temp, dif_abil, li_t, li_a, summary_df,
518	                  domain_df, rho, rho_p, neg_disc_df, pct_san,
519	                  wf_all, cross_df, temp_c, abil_c, overlap, jaccard,
520	                  ref_t, foc_t, ref_a, foc_a):
521	    L = []
522	    def w(s=""):
523	        L.append(s)
524	
525	    w("# Plan 001: METABENCH Real-Data MH-DIF Analysis")
526	    w()
527	    w("## 1. Data & Setup")
528	    w()
529	    w(f"- Response matrix: **{N_MODELS} models × {J} items** (binary, MMLU)")
530	    w(f"- Temporal cohort: ref = 2023 (N={len(ref_t)}), foc = 2024 (N={len(foc_t)}), 5 strata")
531	    w(f"- Ability cohort: ref = Q1-2 (N={len(ref_a)}), foc = Q4-5 (N={len(foc_a)}), 10 strata")
532	    w(f"- Li et al. annotations: {(li_labels.contamination_type != 'no_annotation').sum()} annotated items")
533	    w()
534	
535	    w("## 2. ETS Classification")
536	    w()
537	    w("| Cohort | Filter | Items | A | B | C | %C | FPR (clean) | Enrichment |")
538	    w("|--------|--------|-------|---|---|---|----|-------------|------------|")
539	    for _, r in summary_df.iterrows():
540	        w(f"| {r.cohort_type} | {r.item_filter} | {r.n_items} | "
541	          f"{r.n_ets_a} | {r.n_ets_b} | {r.n_ets_c} | {r.pct_c:.2f}% | "
542	          f"{r.fpr_vs_li_clean:.4f} | {r.enrichment_ratio:.2f} |")
543	    w()
544	
545	    w("## 3. Li et al. Proxy Validation")
546	    w()
547	    w("| Cohort | FPR (clean) | Rate (contam) | Rate (clean) | Rate (unlabeled) | Enrichment |")
548	    w("|--------|-------------|---------------|--------------|------------------|------------|")
549	    for name, lm in [("temporal", li_t), ("ability", li_a)]:
550	        w(f"| {name} | {lm['fpr_vs_li_clean']:.4f} | "
551	          f"{lm['rate_contaminated']:.4f} | {lm['rate_clean']:.4f} | "
552	          f"{lm['rate_unlabeled']:.4f} | {lm['enrichment_ratio']:.2f} |")
553	    w()
554	
555	    w("## 4. Within-Family Analysis")
556	    w()
557	    if not wf_all.empty:
558	        for (rn, fn), sub in wf_all.groupby(["ref_group", "foc_group"]):
559	            vc = sub.ets_class.value_counts()
560	            nc = vc.get("C", 0)
561	            w(f"- **{rn} vs {fn}**: A={vc.get('A',0)}, B={vc.get('B',0)}, "
562	              f"C={nc} ({nc/len(sub)*100:.2f}%)")
563	        w()
564	        if not cross_df.empty:
565	            w("### Cross-cohort vs within-family overlap")
566	            w()
567	            for pair in cross_df.wf_pair.unique():
568	                s = cross_df[cross_df.wf_pair == pair]
569	                tc = s.temporal_ets == "C"
570	                wc = s.wf_ets == "C"
571	                w(f"- **{pair}**: both_C={int((tc&wc).sum())}, "
572	                  f"temp_only_C={int((tc&~wc).sum())}, "
573	                  f"wf_only_C={int((~tc&wc).sum())}")
574	            w()
575	    else:
576	        w("No within-family pairs with sufficient N found.")
577	        w()
578	
579	    w("## 5. Domain Specificity")
580	    w()
581	    w(f"Spearman ρ(C_rate, Δacc) = **{rho:.3f}** (p = {rho_p:.4f})")
582	    w()
583	    w("Top 15 subjects by C rate (temporal cohort):")
584	    w()
585	    w("| Subject | Items | C | %C | Acc 2023 | Acc 2024 | ΔAcc |")
586	    w("|---------|-------|---|-----|----------|----------|------|")
587	    for subj, row in domain_df.nlargest(15, "pct_c").iterrows():
588	        w(f"| {subj} | {int(row.n_items)} | {int(row.n_ets_c)} | "
589	          f"{row.pct_c:.1f}% | {row.acc_2023:.3f} | {row.acc_2024:.3f} | "
590	          f"{row.acc_change:+.3f} |")
591	    w()
592	
593	    w("## 6. Negative-Discrimination Sensitivity")
594	    w()
595	    w("| Item Set | Items | C | %C |")
596	    w("|----------|-------|---|----|")
597	    for _, r in neg_disc_df.iterrows():
598	        w(f"| {r.item_set} | {int(r.n_items)} | {int(r.n_ets_c)} | {r.pct_c:.2f}% |")
599	    w()
600	
601	    w("## 7. Sanity Check")
602	    w()
603	    w(f"Random half-split of 2023 cohort: **{pct_san:.2f}% C** (expect < 5%)")
604	    w()
605	
606	    w("## 8. Cohort Overlap")
607	    w()
608	    w(f"- Temporal C: {len(temp_c)} items")
609	    w(f"- Ability C: {len(abil_c)} items")
610	    w(f"- Both C: {len(overlap)} items")
611	    w(f"- Jaccard index: {jaccard:.3f}")
612	
613	    (OUT / "plan_001_report.md").write_text("\n".join(L) + "\n")
614	    print("  Report written.")
615	
616	
617	if __name__ == "__main__":
618	    main()
619	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85faafeb-5165-4a1f-91f7-e99addf03425",
  "isSidechain": false,
  "promptId": "675b7191-b2b7-49a7-b6a4-83def2b806ad",
  "type": "user",
  "uuid": "e65ea362-e36a-4a95-8f72-d7bee605c81c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_analysis.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nplan_001_analysis.py — METABENCH real-data MH-DIF analysis\n\nRuns purified Mantel-Haenszel DIF detection on MMLU binary response data with\ntwo cohort definitions (temporal 2023-vs-2024, ability Q1-2 vs Q4-5), validates\nagainst Li et al. contamination proxy labels, and performs within-family,\ndomain-specificity, and negative-discrimination sensitivity analyses.\n\nInputs  (all in ../):\n  response_matrix.npz          — (5227, 12508) CSR sparse, int8 binary\n  response_matrix_index.npz    — model_names, item_ids\n  model_metadata.csv           — cohort_temporal, cohort_accuracy_quintile, family\n  item_metadata.csv            — subject, is_negative_disc\n  mmlu_li2024_proxy_labels.csv — contamination_type proxy labels\n\nOutputs (all in ./):\n  dif_results_temporal.csv, dif_results_ability.csv, dif_summary.csv,\n  within_family_dif.csv, cross_analysis.csv, domain_specificity.csv,\n  neg_disc_sensitivity.csv, plan_001_report.md\n\nDependencies: numpy, scipy, pandas\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.sparse import load_npz\nfrom scipy.stats import chi2 as chi2_dist, spearmanr\nfrom pathlib import Path\nimport time\nimport warnings\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\")\nOUT = BASE / \"plan_001\"\nOUT.mkdir(exist_ok=True)\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  DATA LOADING\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"=== Loading data ===\")\nmat = load_npz(BASE / \"response_matrix.npz\")\nX = mat.toarray().astype(np.int16)          # (5227, 12508)\ndel mat\n\nidx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\nMODEL_NAMES = idx[\"model_names\"]             # (5227,)\nITEM_IDS    = idx[\"item_ids\"]                # (12508,)\n\nmodel_meta = pd.read_csv(BASE / \"model_metadata.csv\")\nitem_meta  = pd.read_csv(BASE / \"item_metadata.csv\")\nli_labels  = pd.read_csv(BASE / \"mmlu_li2024_proxy_labels.csv\")\n\nNAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}\nN_MODELS, J = X.shape\nprint(f\"  Matrix {N_MODELS}×{J}\")\nprint(f\"  Li annotated: {(li_labels.contamination_type != 'no_annotation').sum()}, \"\n      f\"no_annotation: {(li_labels.contamination_type == 'no_annotation').sum()}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MH-DIF CORE\n# ════════════════════════════════════════════════════════════════════════════\ndef mh_dif(X_ref, X_foc, n_strata=5, col_mask=None):\n    \"\"\"\n    Purified Mantel-Haenszel DIF for all items (or a column subset).\n\n    For item j the matching variable is:\n        purified_score = total_score_across_all_columns - response_to_item_j\n\n    Parameters\n    ----------\n    X_ref, X_foc : ndarray (N_ref, J) and (N_foc, J), int, binary 0/1\n    n_strata     : number of quantile-based score strata\n    col_mask     : bool array (J,); True = analyse this column.  None = all.\n\n    Returns\n    -------\n    DataFrame with cols: col_idx, alpha_mh, delta_mh, se, chi2, p_value, ets_class\n    \"\"\"\n    _Nr, Jc = X_ref.shape\n\n    # row-wise total scores (used for purified matching)\n    tot_ref = X_ref.sum(axis=1).astype(np.float64)   # (N_ref,)\n    tot_foc = X_foc.sum(axis=1).astype(np.float64)   # (N_foc,)\n\n    cols = np.where(col_mask)[0] if col_mask is not None else np.arange(Jc)\n    rows = []\n    t0 = time.time()\n\n    for pos, j in enumerate(cols):\n        if pos % 2500 == 0 and pos > 0:\n            print(f\"    {pos}/{len(cols)}  ({time.time()-t0:.0f}s)\")\n\n        # ── purified scores: exclude item j from matching variable ──\n        s_ref = tot_ref - X_ref[:, j].astype(np.float64)\n        s_foc = tot_foc - X_foc[:, j].astype(np.float64)\n\n        # ── quantile-based strata on pooled purified scores ──\n        s_all = np.concatenate([s_ref, s_foc])\n        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n        if len(edges) < 2:\n            rows.append(_nan_row(j))\n            continue\n        n_bins = len(edges) - 1\n\n        k_ref = np.digitize(s_ref, edges[1:-1])      # values in [0, n_bins-1]\n        k_foc = np.digitize(s_foc, edges[1:-1])\n\n        # ── accumulate MH statistics across strata ──\n        #   α_MH = R / S  where  R = Σ A_k D_k / N_k,  S = Σ B_k C_k / N_k\n        #   Δ_MH = −2.35 · ln(α_MH)\n        R = S = 0.0\n        sum_diff = 0.0       # Σ (A_k − E[A_k])\n        sum_var  = 0.0       # Σ Var(A_k)\n        # Robins-Breslow-Greenland variance components for ln(α_MH)\n        pr = ps_qr = qs = 0.0\n        n_ok = 0\n\n        for k in range(n_bins):\n            mr = (k_ref == k)\n            mf = (k_foc == k)\n            n1 = int(mr.sum())           # ref count in stratum\n            n0 = int(mf.sum())           # foc count in stratum\n            if n1 == 0 or n0 == 0:\n                continue\n\n            A = float(X_ref[mr, j].sum())   # ref correct\n            B = float(n1 - A)               # ref incorrect\n            C = float(X_foc[mf, j].sum())   # foc correct\n            D = float(n0 - C)               # foc incorrect\n            Nk = float(n1 + n0)\n            m1 = A + C                       # total correct\n            m0 = B + D                       # total incorrect\n\n            if m1 == 0 or m0 == 0 or Nk <= 1:\n                continue\n            n_ok += 1\n\n            Rk = A * D / Nk\n            Sk = B * C / Nk\n            R += Rk\n            S += Sk\n\n            # E[A_k] = n1·m1 / N_k\n            EA = n1 * m1 / Nk\n            sum_diff += A - EA\n            # Var(A_k) = n1·n0·m1·m0 / (N_k²·(N_k−1))\n            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n            # RBG components: P_k = (A+D)/N, Q_k = (B+C)/N\n            Pk = (A + D) / Nk\n            Qk = (B + C) / Nk\n            pr    += Pk * Rk\n            ps_qr += Pk * Sk + Qk * Rk\n            qs    += Qk * Sk\n\n        if n_ok == 0 or (R == 0 and S == 0):\n            rows.append(_nan_row(j))\n            continue\n\n        # ── MH odds ratio ──\n        if S == 0:\n            alpha, delta, se = np.inf, -np.inf, np.nan\n        elif R == 0:\n            alpha, delta, se = 0.0, np.inf, np.nan\n        else:\n            alpha = R / S\n            delta = -2.35 * np.log(alpha)\n            # SE via Robins-Breslow-Greenland:\n            #   Var(ln α) = pr/(2R²) + ps_qr/(2RS) + qs/(2S²)\n            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)\n            se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n        # ── MH χ² with continuity correction (df=1) ──\n        if sum_var > 0:\n            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n        else:\n            chi2_stat = pval = np.nan\n\n        # ── ETS classification ──\n        #   A: |Δ| < 1.0\n        #   C: |Δ| ≥ 1.5 AND p < 0.05\n        #   B: everything else\n        ad = abs(delta) if np.isfinite(delta) else 0.0\n        if ad < 1.0:\n            ets = \"A\"\n        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n            ets = \"C\"\n        else:\n            ets = \"B\"\n\n        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,\n                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets))\n\n    elapsed = time.time() - t0\n    print(f\"    done — {len(cols)} items in {elapsed:.1f}s\")\n    return pd.DataFrame(rows)\n\n\ndef _nan_row(j):\n    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,\n                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class=\"A\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  HELPERS\n# ════════════════════════════════════════════════════════════════════════════\ndef rows_for(col, values):\n    \"\"\"Row indices into X for models matching model_meta[col] ∈ values.\"\"\"\n    names = model_meta.loc[model_meta[col].isin(values), \"model_name\"]\n    return np.array([NAME2ROW[n] for n in names if n in NAME2ROW])\n\n\ndef enrich(df):\n    \"\"\"Attach item_id, subject, Li labels to DIF results (col_idx → item_id).\"\"\"\n    df = df.copy()\n    df[\"item_id\"] = [ITEM_IDS[i] for i in df[\"col_idx\"]]\n    df = df.merge(item_meta[[\"item_id\", \"subject\"]], on=\"item_id\", how=\"left\")\n    df = df.merge(\n        li_labels[[\"item_id\", \"is_contaminated\", \"contamination_type\"]].rename(\n            columns={\"is_contaminated\": \"li_label\",\n                     \"contamination_type\": \"li_contamination_type\"}),\n        on=\"item_id\", how=\"left\",\n    )\n    return df\n\n\ndef li_metrics(df):\n    \"\"\"FPR, contaminated rate, enrichment from enriched DIF results.\"\"\"\n    is_c   = df[\"ets_class\"] == \"C\"\n    clean  = df[\"li_contamination_type\"] == \"clean\"\n    contam = df[\"li_contamination_type\"].isin([\"input_only\", \"input_and_label\"])\n    unlab  = df[\"li_contamination_type\"] == \"no_annotation\"\n\n    r_clean  = is_c[clean].mean()  if clean.any()  else np.nan\n    r_contam = is_c[contam].mean() if contam.any() else np.nan\n    r_unlab  = is_c[unlab].mean()  if unlab.any()  else np.nan\n    enrich   = r_contam / r_clean  if r_clean > 0  else np.nan\n\n    return dict(fpr_vs_li_clean=r_clean, rate_contaminated=r_contam,\n                rate_clean=r_clean, rate_unlabeled=r_unlab,\n                enrichment_ratio=enrich)\n\n\ndef summary_row(cohort, filt, df):\n    vc = df[\"ets_class\"].value_counts()\n    n  = len(df)\n    lm = li_metrics(df)\n    return dict(\n        cohort_type=cohort, item_filter=filt, n_items=n,\n        n_ets_a=vc.get(\"A\", 0), n_ets_b=vc.get(\"B\", 0), n_ets_c=vc.get(\"C\", 0),\n        pct_c=vc.get(\"C\", 0) / n * 100 if n > 0 else 0,\n        fpr_vs_li_clean=lm[\"fpr_vs_li_clean\"],\n        enrichment_ratio=lm[\"enrichment_ratio\"],\n    )\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MAIN\n# ════════════════════════════════════════════════════════════════════════════\ndef main():\n    summary_rows = []\n\n    # ── Step 1-2: MH-DIF — Temporal cohort ─────────────────────────────────\n    print(\"\\n=== Step 1-2a: Temporal cohort DIF (2023 vs 2024, 5 strata) ===\")\n    ref_t = rows_for(\"cohort_temporal\", [\"2023\"])\n    foc_t = rows_for(\"cohort_temporal\", [\"2024\"])\n    print(f\"  N_ref={len(ref_t)}, N_foc={len(foc_t)}\")\n\n    dif_temp = mh_dif(X[ref_t], X[foc_t], n_strata=5)\n    dif_temp = enrich(dif_temp)\n    print(f\"  ETS: {dif_temp.ets_class.value_counts().to_dict()}\")\n    summary_rows.append(summary_row(\"temporal\", \"all\", dif_temp))\n\n    # ── Step 1-2: MH-DIF — Ability cohort ──────────────────────────────────\n    print(\"\\n=== Step 1-2b: Ability cohort DIF (Q1-2 vs Q4-5, 10 strata) ===\")\n    ref_a = rows_for(\"cohort_accuracy_quintile\", [1, 2])\n    foc_a = rows_for(\"cohort_accuracy_quintile\", [4, 5])\n    print(f\"  N_ref={len(ref_a)}, N_foc={len(foc_a)}\")\n\n    dif_abil = mh_dif(X[ref_a], X[foc_a], n_strata=10)\n    dif_abil = enrich(dif_abil)\n    print(f\"  ETS: {dif_abil.ets_class.value_counts().to_dict()}\")\n    summary_rows.append(summary_row(\"ability\", \"all\", dif_abil))\n\n    # ── Step 3: Li et al. proxy validation ─────────────────────────────────\n    print(\"\\n=== Step 3: Li et al. proxy validation ===\")\n    li_t = li_metrics(dif_temp)\n    li_a = li_metrics(dif_abil)\n    print(f\"  Temporal — FPR={li_t['fpr_vs_li_clean']:.4f}, \"\n          f\"enrichment={li_t['enrichment_ratio']:.2f}\")\n    print(f\"  Ability  — FPR={li_a['fpr_vs_li_clean']:.4f}, \"\n          f\"enrichment={li_a['enrichment_ratio']:.2f}\")\n\n    # ── Step 4: Within-family analysis ─────────────────────────────────────\n    print(\"\\n=== Step 4: Within-family DIF ===\")\n\n    # Show family × temporal distribution\n    fam_temp = (model_meta.groupby([\"family\", \"cohort_temporal\"])\n                .size().unstack(fill_value=0))\n    print(\"  Family × temporal counts:\")\n    for fam in [\"llama-2\", \"llama-3\", \"mistral\", \"mixtral\", \"solar\", \"zephyr\"]:\n        if fam in fam_temp.index:\n            print(f\"    {fam}: {fam_temp.loc[fam].to_dict()}\")\n\n    family_pairs = []\n\n    # (A) Cross-family comparisons (related families)\n    llama2_idx = rows_for(\"family\", [\"llama-2\"])\n    llama3_idx = rows_for(\"family\", [\"llama-3\"])\n    if len(llama2_idx) >= 80 and len(llama3_idx) >= 80:\n        family_pairs.append((\"llama-2\", \"llama-3\", llama2_idx, llama3_idx))\n\n    mistral_idx = rows_for(\"family\", [\"mistral\"])\n    mixtral_idx = rows_for(\"family\", [\"mixtral\"])\n    if len(mistral_idx) >= 80 and len(mixtral_idx) >= 80:\n        family_pairs.append((\"mistral\", \"mixtral\", mistral_idx, mixtral_idx))\n\n    # (B) Within single family, temporal split (where both groups >= 40)\n    for fam in [\"unknown\", \"mistral\", \"llama-3\", \"llama-2\"]:\n        fam_df = model_meta[model_meta[\"family\"] == fam]\n        r_names = fam_df.loc[fam_df.cohort_temporal == \"2023\", \"model_name\"]\n        f_names = fam_df.loc[fam_df.cohort_temporal == \"2024\", \"model_name\"]\n        ri = np.array([NAME2ROW[n] for n in r_names if n in NAME2ROW])\n        fi = np.array([NAME2ROW[n] for n in f_names if n in NAME2ROW])\n        if len(ri) >= 40 and len(fi) >= 40:\n            family_pairs.append((f\"{fam}_2023\", f\"{fam}_2024\", ri, fi))\n\n    wf_parts = []\n    for rname, fname, ri, fi in family_pairs:\n        ns = 5 if min(len(ri), len(fi)) < 200 else 10\n        print(f\"  {rname} (N={len(ri)}) vs {fname} (N={len(fi)}), {ns} strata\")\n        wf = mh_dif(X[ri], X[fi], n_strata=ns)\n        wf = enrich(wf)\n        wf[\"ref_group\"] = rname\n        wf[\"foc_group\"] = fname\n        wf_parts.append(wf)\n        print(f\"    ETS: {wf.ets_class.value_counts().to_dict()}\")\n\n    wf_all = pd.concat(wf_parts, ignore_index=True) if wf_parts else pd.DataFrame()\n\n    # Cross-cohort vs within-family comparison\n    print(\"\\n=== Step 4 cont: Cross analysis ===\")\n    cross_rows = []\n    for rname, fname, _, _ in family_pairs:\n        wf_sub = wf_all[(wf_all.ref_group == rname) & (wf_all.foc_group == fname)]\n        for _, wr in wf_sub.iterrows():\n            iid = wr[\"item_id\"]\n            tr = dif_temp.loc[dif_temp.item_id == iid]\n            if tr.empty:\n                continue\n            tr = tr.iloc[0]\n            cross_rows.append(dict(\n                item_id=iid, subject=wr[\"subject\"],\n                temporal_ets=tr[\"ets_class\"], temporal_delta=tr[\"delta_mh\"],\n                wf_pair=f\"{rname}_vs_{fname}\",\n                wf_ets=wr[\"ets_class\"], wf_delta=wr[\"delta_mh\"],\n                li_contamination_type=wr.get(\"li_contamination_type\", np.nan),\n            ))\n    cross_df = pd.DataFrame(cross_rows)\n\n    if not cross_df.empty:\n        for pair in cross_df[\"wf_pair\"].unique():\n            sub = cross_df[cross_df.wf_pair == pair]\n            tc = sub.temporal_ets == \"C\"\n            wc = sub.wf_ets == \"C\"\n            print(f\"  {pair}: both_C={int((tc & wc).sum())}, \"\n                  f\"temp_only_C={int((tc & ~wc).sum())}, \"\n                  f\"wf_only_C={int((~tc & wc).sum())}, \"\n                  f\"neither={int((~tc & ~wc).sum())}\")\n\n    # ── Step 5: Domain specificity ─────────────────────────────────────────\n    print(\"\\n=== Step 5: Domain specificity ===\")\n\n    # C rate per subject (temporal cohort)\n    subj_c = (dif_temp.groupby(\"subject\")[\"ets_class\"]\n              .agg(n_items=\"size\", n_ets_c=lambda x: (x == \"C\").sum()))\n    subj_c[\"pct_c\"] = subj_c[\"n_ets_c\"] / subj_c[\"n_items\"] * 100\n\n    # Per-item accuracy for 2023 and 2024 models\n    acc_2023 = X[ref_t].mean(axis=0).astype(np.float64)   # (J,)\n    acc_2024 = X[foc_t].mean(axis=0).astype(np.float64)\n\n    item_acc = pd.DataFrame({\"item_id\": ITEM_IDS, \"acc_2023\": acc_2023, \"acc_2024\": acc_2024})\n    item_acc = item_acc.merge(item_meta[[\"item_id\", \"subject\"]], on=\"item_id\")\n    subj_acc = item_acc.groupby(\"subject\")[[\"acc_2023\", \"acc_2024\"]].mean()\n    subj_acc[\"acc_change\"] = subj_acc[\"acc_2024\"] - subj_acc[\"acc_2023\"]\n\n    domain_df = subj_c.join(subj_acc, how=\"inner\")\n    rho, rho_p = spearmanr(domain_df[\"pct_c\"], domain_df[\"acc_change\"])\n    print(f\"  Spearman(pct_C, acc_change) = {rho:.3f}, p = {rho_p:.4f}\")\n    print(\"  Top 5 by C rate:\")\n    for subj, row in domain_df.nlargest(5, \"pct_c\").iterrows():\n        print(f\"    {subj}: {row.pct_c:.1f}% C ({int(row.n_ets_c)}/{int(row.n_items)}), \"\n              f\"Δacc={row.acc_change:+.3f}\")\n\n    # ── Step 6: Negative-discrimination sensitivity ────────────────────────\n    print(\"\\n=== Step 6: Negative-disc sensitivity ===\")\n    neg_mask = item_meta.set_index(\"item_id\").reindex(ITEM_IDS)[\"is_negative_disc\"].values\n    pos_mask = ~neg_mask\n    n_neg = int(neg_mask.sum())\n    n_pos = int(pos_mask.sum())\n    print(f\"  All={J}, neg_disc={n_neg}, non_neg={n_pos}\")\n\n    # Re-run temporal DIF on non-negative-disc items only\n    # (total scores also computed only on non-neg items)\n    pos_cols = np.where(pos_mask)[0]\n    dif_temp_nn = mh_dif(X[np.ix_(ref_t, pos_cols)],\n                         X[np.ix_(foc_t, pos_cols)], n_strata=5)\n\n    # Map col_idx back to original item space\n    dif_temp_nn[\"col_idx_orig\"] = [pos_cols[c] for c in dif_temp_nn[\"col_idx\"]]\n    dif_temp_nn[\"item_id\"] = [ITEM_IDS[pos_cols[c]] for c in dif_temp_nn[\"col_idx\"]]\n    dif_temp_nn = dif_temp_nn.merge(\n        li_labels[[\"item_id\", \"is_contaminated\", \"contamination_type\"]].rename(\n            columns={\"is_contaminated\": \"li_label\",\n                     \"contamination_type\": \"li_contamination_type\"}),\n        on=\"item_id\", how=\"left\",\n    )\n\n    n_c_all = int((dif_temp[\"ets_class\"] == \"C\").sum())\n    n_c_nn  = int((dif_temp_nn[\"ets_class\"] == \"C\").sum())\n    # C count among neg-disc items in the full run\n    neg_col_set = set(np.where(neg_mask)[0])\n    n_c_neg = int((dif_temp.loc[dif_temp.col_idx.isin(neg_col_set), \"ets_class\"] == \"C\").sum())\n\n    neg_disc_df = pd.DataFrame([\n        dict(item_set=\"all\",               n_items=J,     n_ets_c=n_c_all,\n             pct_c=n_c_all / J * 100),\n        dict(item_set=\"non_negative_disc\",  n_items=n_pos, n_ets_c=n_c_nn,\n             pct_c=n_c_nn / n_pos * 100),\n        dict(item_set=\"negative_disc_only\", n_items=n_neg, n_ets_c=n_c_neg,\n             pct_c=n_c_neg / n_neg * 100 if n_neg > 0 else 0),\n    ])\n    print(neg_disc_df.to_string(index=False))\n\n    summary_rows.append(summary_row(\"temporal\", \"non_neg_disc\", dif_temp_nn))\n\n    # ── Sanity check: random half-split of 2023 cohort ─────────────────────\n    print(\"\\n=== Sanity check: random half-split of 2023 cohort ===\")\n    rng = np.random.RandomState(42)\n    perm = rng.permutation(len(ref_t))\n    half = len(perm) // 2\n    san_ref = ref_t[perm[:half]]\n    san_foc = ref_t[perm[half:]]\n    print(f\"  Split: {len(san_ref)} vs {len(san_foc)}\")\n    dif_san = mh_dif(X[san_ref], X[san_foc], n_strata=5)\n    vc_san = dif_san[\"ets_class\"].value_counts()\n    n_c_san = vc_san.get(\"C\", 0)\n    pct_c_san = n_c_san / len(dif_san) * 100\n    print(f\"  ETS C: {n_c_san}/{len(dif_san)} = {pct_c_san:.2f}% (expect <5%)\")\n\n    # ── Save all outputs ───────────────────────────────────────────────────\n    print(\"\\n=== Saving outputs ===\")\n\n    out_cols = [\"item_id\", \"subject\", \"alpha_mh\", \"delta_mh\", \"se\",\n                \"p_value\", \"ets_class\", \"li_label\", \"li_contamination_type\"]\n    dif_temp[out_cols].to_csv(OUT / \"dif_results_temporal.csv\", index=False)\n    dif_abil[out_cols].to_csv(OUT / \"dif_results_ability.csv\", index=False)\n\n    summary_df = pd.DataFrame(summary_rows)\n    summary_df.to_csv(OUT / \"dif_summary.csv\", index=False)\n\n    if not wf_all.empty:\n        wf_cols = [\"item_id\", \"subject\", \"ref_group\", \"foc_group\",\n                   \"alpha_mh\", \"delta_mh\", \"se\", \"p_value\", \"ets_class\",\n                   \"li_label\", \"li_contamination_type\"]\n        wf_all[[c for c in wf_cols if c in wf_all.columns]].to_csv(\n            OUT / \"within_family_dif.csv\", index=False)\n\n    if not cross_df.empty:\n        cross_df.to_csv(OUT / \"cross_analysis.csv\", index=False)\n\n    domain_df.reset_index().to_csv(OUT / \"domain_specificity.csv\", index=False)\n    neg_disc_df.to_csv(OUT / \"neg_disc_sensitivity.csv\", index=False)\n\n    # ── Cohort overlap ─────────────────────────────────────────────────────\n    temp_c = set(dif_temp.loc[dif_temp.ets_class == \"C\", \"item_id\"])\n    abil_c = set(dif_abil.loc[dif_abil.ets_class == \"C\", \"item_id\"])\n    overlap = temp_c & abil_c\n    union   = temp_c | abil_c\n    jaccard = len(overlap) / len(union) if union else 0\n\n    # ── Console summary ────────────────────────────────────────────────────\n    print(\"\\n\" + \"=\" * 60)\n    print(\"SUMMARY\")\n    print(\"=\" * 60)\n    print(f\"\\nTemporal (2023 vs 2024, 5 strata):\")\n    print(f\"  ETS: {dif_temp.ets_class.value_counts().to_dict()}\")\n    print(f\"  FPR vs Li clean = {li_t['fpr_vs_li_clean']:.4f}\")\n    print(f\"  Enrichment = {li_t['enrichment_ratio']:.2f}\")\n    print(f\"\\nAbility (Q1-2 vs Q4-5, 10 strata):\")\n    print(f\"  ETS: {dif_abil.ets_class.value_counts().to_dict()}\")\n    print(f\"  FPR vs Li clean = {li_a['fpr_vs_li_clean']:.4f}\")\n    print(f\"  Enrichment = {li_a['enrichment_ratio']:.2f}\")\n    print(f\"\\nSanity check (random split): {pct_c_san:.2f}% C\")\n    print(f\"Domain ρ(C_rate, Δacc) = {rho:.3f}, p = {rho_p:.4f}\")\n    print(f\"Cohort overlap: temp_C={len(temp_c)}, abil_C={len(abil_c)}, \"\n          f\"both={len(overlap)}, Jaccard={jaccard:.3f}\")\n\n    # ── Generate report ────────────────────────────────────────────────────\n    _write_report(dif_temp, dif_abil, li_t, li_a, summary_df,\n                  domain_df, rho, rho_p, neg_disc_df, pct_c_san,\n                  wf_all, cross_df, temp_c, abil_c, overlap, jaccard,\n                  ref_t, foc_t, ref_a, foc_a)\n\n    print(f\"\\nAll outputs saved to {OUT}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  REPORT\n# ════════════════════════════════════════════════════════════════════════════\ndef _write_report(dif_temp, dif_abil, li_t, li_a, summary_df,\n                  domain_df, rho, rho_p, neg_disc_df, pct_san,\n                  wf_all, cross_df, temp_c, abil_c, overlap, jaccard,\n                  ref_t, foc_t, ref_a, foc_a):\n    L = []\n    def w(s=\"\"):\n        L.append(s)\n\n    w(\"# Plan 001: METABENCH Real-Data MH-DIF Analysis\")\n    w()\n    w(\"## 1. Data & Setup\")\n    w()\n    w(f\"- Response matrix: **{N_MODELS} models × {J} items** (binary, MMLU)\")\n    w(f\"- Temporal cohort: ref = 2023 (N={len(ref_t)}), foc = 2024 (N={len(foc_t)}), 5 strata\")\n    w(f\"- Ability cohort: ref = Q1-2 (N={len(ref_a)}), foc = Q4-5 (N={len(foc_a)}), 10 strata\")\n    w(f\"- Li et al. annotations: {(li_labels.contamination_type != 'no_annotation').sum()} annotated items\")\n    w()\n\n    w(\"## 2. ETS Classification\")\n    w()\n    w(\"| Cohort | Filter | Items | A | B | C | %C | FPR (clean) | Enrichment |\")\n    w(\"|--------|--------|-------|---|---|---|----|-------------|------------|\")\n    for _, r in summary_df.iterrows():\n        w(f\"| {r.cohort_type} | {r.item_filter} | {r.n_items} | \"\n          f\"{r.n_ets_a} | {r.n_ets_b} | {r.n_ets_c} | {r.pct_c:.2f}% | \"\n          f\"{r.fpr_vs_li_clean:.4f} | {r.enrichment_ratio:.2f} |\")\n    w()\n\n    w(\"## 3. Li et al. Proxy Validation\")\n    w()\n    w(\"| Cohort | FPR (clean) | Rate (contam) | Rate (clean) | Rate (unlabeled) | Enrichment |\")\n    w(\"|--------|-------------|---------------|--------------|------------------|------------|\")\n    for name, lm in [(\"temporal\", li_t), (\"ability\", li_a)]:\n        w(f\"| {name} | {lm['fpr_vs_li_clean']:.4f} | \"\n          f\"{lm['rate_contaminated']:.4f} | {lm['rate_clean']:.4f} | \"\n          f\"{lm['rate_unlabeled']:.4f} | {lm['enrichment_ratio']:.2f} |\")\n    w()\n\n    w(\"## 4. Within-Family Analysis\")\n    w()\n    if not wf_all.empty:\n        for (rn, fn), sub in wf_all.groupby([\"ref_group\", \"foc_group\"]):\n            vc = sub.ets_class.value_counts()\n            nc = vc.get(\"C\", 0)\n            w(f\"- **{rn} vs {fn}**: A={vc.get('A',0)}, B={vc.get('B',0)}, \"\n              f\"C={nc} ({nc/len(sub)*100:.2f}%)\")\n        w()\n        if not cross_df.empty:\n            w(\"### Cross-cohort vs within-family overlap\")\n            w()\n            for pair in cross_df.wf_pair.unique():\n                s = cross_df[cross_df.wf_pair == pair]\n                tc = s.temporal_ets == \"C\"\n                wc = s.wf_ets == \"C\"\n                w(f\"- **{pair}**: both_C={int((tc&wc).sum())}, \"\n                  f\"temp_only_C={int((tc&~wc).sum())}, \"\n                  f\"wf_only_C={int((~tc&wc).sum())}\")\n            w()\n    else:\n        w(\"No within-family pairs with sufficient N found.\")\n        w()\n\n    w(\"## 5. Domain Specificity\")\n    w()\n    w(f\"Spearman ρ(C_rate, Δacc) = **{rho:.3f}** (p = {rho_p:.4f})\")\n    w()\n    w(\"Top 15 subjects by C rate (temporal cohort):\")\n    w()\n    w(\"| Subject | Items | C | %C | Acc 2023 | Acc 2024 | ΔAcc |\")\n    w(\"|---------|-------|---|-----|----------|----------|------|\")\n    for subj, row in domain_df.nlargest(15, \"pct_c\").iterrows():\n        w(f\"| {subj} | {int(row.n_items)} | {int(row.n_ets_c)} | \"\n          f\"{row.pct_c:.1f}% | {row.acc_2023:.3f} | {row.acc_2024:.3f} | \"\n          f\"{row.acc_change:+.3f} |\")\n    w()\n\n    w(\"## 6. Negative-Discrimination Sensitivity\")\n    w()\n    w(\"| Item Set | Items | C | %C |\")\n    w(\"|----------|-------|---|----|\")\n    for _, r in neg_disc_df.iterrows():\n        w(f\"| {r.item_set} | {int(r.n_items)} | {int(r.n_ets_c)} | {r.pct_c:.2f}% |\")\n    w()\n\n    w(\"## 7. Sanity Check\")\n    w()\n    w(f\"Random half-split of 2023 cohort: **{pct_san:.2f}% C** (expect < 5%)\")\n    w()\n\n    w(\"## 8. Cohort Overlap\")\n    w()\n    w(f\"- Temporal C: {len(temp_c)} items\")\n    w(f\"- Ability C: {len(abil_c)} items\")\n    w(f\"- Both C: {len(overlap)} items\")\n    w(f\"- Jaccard index: {jaccard:.3f}\")\n\n    (OUT / \"plan_001_report.md\").write_text(\"\\n\".join(L) + \"\\n\")\n    print(\"  Report written.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 619,
      "startLine": 1,
      "totalLines": 619
    }
  },
  "sourceToolAssistantUUID": "85faafeb-5165-4a1f-91f7-e99addf03425",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T10:01:31.320Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RwPRkkVz217cUPEGZTPMkP`</summary>

```json
{
  "command": "python3 -c \"\nimport scipy.sparse as sp\nimport numpy as np\nimport pandas as pd\n\n# Load response matrix\nrm = sp.load_npz('artifacts/response_matrix.npz')\nprint(f'Response matrix: {rm.shape}, dtype={rm.dtype}, nnz={rm.nnz}')\n\n# Load index\nidx = np.load('artifacts/response_matrix_index.npz', allow_pickle=True)\nprint(f'Index keys: {list(idx.keys())}')\nprint(f'model_names: {len(idx[\\\"model_names\\\"])}')\nprint(f'item_ids: {len(idx[\\\"item_ids\\\"])}')\n\n# Load metadata\nmeta = pd.read_csv('artifacts/model_metadata.csv')\nprint(f'\\nMetadata shape: {meta.shape}')\nprint(f'Columns: {list(meta.columns)}')\nprint(f'\\ncohort_temporal value counts:')\nprint(meta['cohort_temporal'].value_counts(dropna=False))\n\"\n",
  "description": "Inspect data files and shapes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e65ea362-e36a-4a95-8f72-d7bee605c81c",
  "isSidechain": false,
  "requestId": "req_011CbFXA4pyhKTypPhnmC26D",
  "type": "assistant",
  "uuid": "656ece9b-145d-4dc1-8166-08e2af657484",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhNRcjYdK9HHpfd2UR7bZ6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12764,
      "cache_read_input_tokens": 11841,
      "output_tokens": 534,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 534,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12764
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

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## 任务: plan_029 — Permutation Null for Temporal DIF C%  ### 目标 Reviewer 问\"31.3% C% 是否高于 chance\"。当前 random-split control (0.18%) 是 within-same-cohort，不是 temporal label permutation null。做 1000 次 permuta…",
  "leafUuid": "656ece9b-145d-4dc1-8166-08e2af657484",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Permutation null distribution for temporal DIF C%",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd"
}
```

---

### Tool result

_source line 15 · 2026-05-21T10:01:33.539Z_

<details><summary>↩ Tool result · `toolu_01RwPRkkVz217cUPEGZTPMkP`</summary>

```text
Response matrix: (5227, 12508), dtype=int8, nnz=38654082
Index keys: ['model_names', 'item_ids']
model_names: 5227
item_ids: 12508

Metadata shape: (5227, 8)
Columns: ['model_name', 'family', 'release_year', 'release_half', 'training_method', 'accuracy', 'cohort_temporal', 'cohort_accuracy_quintile']

cohort_temporal value counts:
cohort_temporal
other    3340
2023     1080
2024      807
Name: count, dtype: int64
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "656ece9b-145d-4dc1-8166-08e2af657484",
  "isSidechain": false,
  "promptId": "675b7191-b2b7-49a7-b6a4-83def2b806ad",
  "type": "user",
  "uuid": "7be8adbd-66ad-44c9-865f-bfbd1dead724",
  "toolUseResult": {
    "stdout": "Response matrix: (5227, 12508), dtype=int8, nnz=38654082\nIndex keys: ['model_names', 'item_ids']\nmodel_names: 5227\nitem_ids: 12508\n\nMetadata shape: (5227, 8)\nColumns: ['model_name', 'family', 'release_year', 'release_half', 'training_method', 'accuracy', 'cohort_temporal', 'cohort_accuracy_quintile']\n\ncohort_temporal value counts:\ncohort_temporal\nother    3340\n2023     1080\n2024      807\nName: count, dtype: int64",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "656ece9b-145d-4dc1-8166-08e2af657484",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-21T10:07:37.784Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. I need to:

1. Extract the `mh_dif` function from plan_001
2. Write a permutation test that:
   - Takes the 1887 models with temporal labels (1080 "2023" + 807 "2024")
   - 1000 times: randomly shuffle the temporal labels, run MH-DIF, count C%
   - Compare observed 31.3% against the null distribution

Key optimizations:
- The total scores across all items can be precomputed once (they don't change with permutation since we're just relabeling which models are ref/foc)


- The response matrix subsetted to the 1887 temporal models can also be precomputed upfront
- For each permutation, I just need to randomly split those 1887 models into groups of 1080 and 807, then run the MH-DIF calculation

The main bottleneck is the nested loop structure in mh_dif—iterating over items and then strata. I need to vectorize this as much as possible to keep the permutation test fast.

For each permutation, the workflow is: split the models into reference and focal groups, then for each of the 12,508 items, compute purified scores by removing that item's contribution, stratify based on those pooled purified scores, accumulate the MH statistics across strata, and classify items as A/B/C before counting the percentage of C classifications.

The challenge is that I can't fully vectorize the per-item loop since the strata themselves depend on the purified scores for each item. However, I can optimize by precomputing total scores once upfront—they're just the sum across all items for each model and don't change between permutations or groupings.

The real bottleneck is that strata boundaries shift for every item and every permutation, making it difficult to vectorize across permutations. I need to think about whether there's a way to batch compute the MH statistics more efficiently despite this dependency. The key constraint is that we need both |Δ_MH| ≥ 0.5 AND p < 0.05 for the C% metric, and with 12,508 items across 1,000 permutations, I need to optimize the inner computation significantly. My strategy is to precompute the response matrices and total scores for the temporal models upfront, then for each permutation just index into those arrays, potentially using numba or cython to accelerate the innermost loop. Let me test how fast a single permutation runs—if it's around 10 seconds, 1,000 permutations would take roughly 3 hours, which is feasible, but if it's closer to 2 minutes per permutation, that balloons to 33 hours and becomes impractical. Writing vectorized computation... Writing vectorized quantile computation... Writing optimized computation... Continuing the stratification loop...

For each bin, I'm checking if there are samples from both groups, then computing a contingency table with counts A, B, C, D representing the distribution of the feature across reference and focal groups, and accumulating the numerator for the test statistic.

Now I'm finishing the calculation by adding the denominator term, then computing the effect size delta from the ratio of these terms, and checking if it's large enough to warrant computing the chi-squared statistic with a continuity correction.

I'm realizing the nested loops over strata and permutations could be slow with pure Python, so I should consider using numba to JIT compile the core computation and get a significant speedup.

Let me write the optimized version with numba...

Actually, I need to check what's available on this system and include a fallback if numba isn't installed.

My approach will be to load the temporal models, precompute the total scores, define an efficient MH-DIF function that calculates the C% metric, then run the permutation test 1000 times while tracking progress, and finally save the results with a report and visualization.

Let me start writing the script now. Writing the optimization script...

Actually, I'm realizing the strata edges and assignments are completely fixed across all permutations since they only depend on the purified scores, which don't change based on the ref/foc split. This means I can precompute the strata structure once for each item, then for every permutation I just need to count how the ref and foc labels fall within each stratum. /foc split
2. For each item j, given the fixed stratum assignments, compute A, B, C, D per stratum
3. Compute MH statistics

The stratum assignment per item per model is fixed. So I can precompute a (1887, 12508) matrix of stratum assignments. But that's 1887 × 12508 = 23.6M entries, manageable in int8.

Actually wait, the strata depend on quantiles of the purified scores. The purified scores for all 1887 models on item j are: tot[i] - X[i, j] for i in temporal_models. This is independent of the split. So the edges and digitize results are the same across permutations. 

So the algorithm becomes:

**Precomputation (once):**
For each item j:
- Compute purified scores for all 1887 temporal models
- Compute quantile edges
- Assign each model to a stratum and index which models fall into each stratum
- Cache the response values for quick lookup during permutations

**Per permutation:**
For each item j, I use the fixed stratum assignments and the reference indicator to compute the contingency table entries: for each stratum, I count how many reference and non-reference models are in it, then tally up the responses to get A and C values. Computing the contingency table entries for each stratum by precomputing model indices and responses, then for each permutation just calculating how many reference models are correct in each cell using dot products and boolean operations.

I'm considering whether to use jagged arrays for efficiency or flatten everything into dense arrays with index ranges, though the flattening approach is getting complicated.

Let me try a different strategy instead. Since strata are fixed per item, I can precompute a stratum assignment matrix and then for each permutation, use bincount to efficiently tally how many reference models fall into each stratum and how many got each item correct within that stratum.

Using bincount on the stratum assignments...

Implementing the optimized version... Building the contingency table... Finishing the variance calculation and chi-squared test, then returning the percentage of significant results. The optimization works because I'm precomputing the quantiles and digitization upfront rather than recalculating them for each permutation, plus using fast bincount operations for aggregation and early exits when delta falls below the threshold.

Now I'm estimating the runtime—with about 12,500 iterations each doing roughly 10 numpy operations on arrays of ~1,900 elements, that's around 10 microseconds per iteration, so 1,000 permutations should complete in about 2 minutes. The main concern is whether the fancy indexing in bincount with boolean masks creates unnecessary copies that could slow things down.

Actually, the indexed subarray is only around 1,000 elements, so bincount should still be fast—maybe 50-100 microseconds per item total, which means 10-20 minutes for 1,000 permutations. That's acceptable. I could optimize further with numba, but the numpy approach should work fine.

Before writing the full script, I need to handle the fact that the number of bins varies per item depending on how many unique quantile edges are generated. I'll precompute this variation and then write out the complete permutation test script.

Writing the script... Loading the response matrix and metadata...

Now I'm extracting the temporal models from 2023 and 2024, mapping them to their row indices, and splitting them into reference and focus groups—1080 reference models and 807 focus models across 12,508 items. I'm pulling out the submatrix for just these temporal models and preparing to compute stratification assignments.

Computing total scores for each model and then building a stratum matrix by calculating quantile-based bins for each item's purified scores...

Finishing the stratum assignment logic... Completing the contingency table calculations... Finishing the statistical test and returning the count as a percentage. Now I'm thinking about memory optimization—the stratification matrix is manageable at around 24 MB, but the temporary float array could balloon to 188 MB, so I should keep it as int8 and only convert when necessary, using boolean for the binary response values to save space and potentially speed up operations.

For efficiency, I'm realizing that repeatedly slicing columns from a C-contiguous array creates overhead across millions of iterations, so I'll transpose both matrices upfront to make column access contiguous and faster. Now I'm ready to write out the complete script with the permutation test logic and matplotlib visualization for the null distribution histogram.

Before diving in, I want to reconsider the stratification precomputation—currently looping through 12,508 items to compute quantiles and digitize each one. I'm exploring whether I can vectorize this by computing all purified scores at once and applying quantile operations across the entire matrix at once, though the unique edge removal per column might still require iteration.

Actually, I could simplify this by skipping the unique operation entirely and just using 5 fixed strata. If some edges end up duplicated, certain bins will be empty, but my validation logic already handles that. The tricky part is that np.digitize doesn't handle duplicate bin edges gracefully—if two edges are identical, the bin assignments become unpredictable.

But that's okay. I can still use n_bins = 5 consistently across all items, and empty bins just get filtered out during the valid check. This approach is much cleaner to vectorize than tracking per-column unique edges.

Vectorizing the precomputation... Writing vectorized stratification...

Actually, let me reconsider how `np.digitize` works versus `np.searchsorted`. The `digitize` function with edges returns bin indices where values fall, and I need to verify whether my manual boolean comparison approach produces the same result as using `searchsorted` with the appropriate parameters.

For the vectorized approach with 2D data, I realize `searchsorted` expects 1D sorted arrays, so I'd need to apply it per column or reshape the data appropriately to get the strata assignments across all samples at once.

Actually, there's a cleaner way: since the inner edges might have duplicates from quantile calculations, I can use a comparison-based loop that counts how many edge thresholds each value exceeds. By iterating through just the 4 inner edges and accumulating a count via broadcasting comparisons between the data and edges, I get the strata assignment efficiently without needing to sort or handle edge cases with duplicates.

The memory footprint is manageable—the data matrix is about 188 MB, and each comparison creates a temporary boolean array around 24 MB, so peak usage stays well under control. This approach gives the same [0, 4] stratum assignments as digitize would.

Now I'm settling on the full pipeline: precompute the centered differences, calculate quantiles to get the edge thresholds, assign strata through the comparison loop, then free the intermediate data and keep only what's needed for the permutation tests—the compressed integer arrays and the original totals.

Writing the complete script with timing, progress tracking, early stopping logic, CSV output, and a histogram visualization... Writing the permutation test script... Setting up the data pipeline...

I'm extracting the temporal subset of models from 2023 and 2024, mapping them to their row indices, and labeling which ones are reference versus focal models. Then I'm slicing the response matrix to get just the temporal data and counting how many models fall into each group.

Now I'm freeing up memory and computing the strata by calculating total scores for each model, then deriving the purified scores by subtracting individual item responses from those totals. Writing the C% computation function... Computing contingency statistics... Now I'm computing the observed C% value from the reference data and timing how long it takes, then setting up a permutation test to run multiple iterations and establish a baseline distribution. Writing permutation loop... Printing the results summary with the observed C statistic, null distribution statistics, and p-value, then moving on to save the outputs to a CSV file.

Writing visualization code... Finishing up the visualization by saving the figure and then moving into the report generation. I'm documenting the permutation test setup with the sample sizes, number of permutations, and the matching procedure used, then I'll present the statistical results showing whether the observed C-category rate is significantly different from the null distribution. Generating the report markdown...

Now I'm noticing some inefficiencies in the code—the reference label lookup is doing redundant iterations through metadata for each temporal row, which I should optimize. I'm also checking the memory footprint of the data matrices and realizing there might be room to compress further. The column access pattern should be efficient since I'm slicing columns from row-major arrays, and the boolean masking operations that create ~1000-element copies are fast. The real bottleneck is likely the four fancy indexing operations per iteration, so I'm considering whether I can precompute per-item, per-stratum model lists and responses to avoid them.

Another approach is to work with transposed arrays—if I precompute `strata.T` and `X_bool.T`, then accessing by item j gives me contiguous memory, which improves the access pattern significantly. I can also combine the boolean operations in the inner loop to streamline the computation.

Optimizing the inner loop structure... I'm realizing the encoding approach is getting too complicated, so let me simplify by just computing the four separate bincounts directly. I can reduce this to two bincounts by encoding both the model type and stratum together—one bincount for all models to get the counts per stratum and model type, then another bincount on just the correct models to get the correct counts.

Actually, I can optimize further by using weights in the bincount function instead of filtering the data first. I'm realizing I should precompute the focal offset outside the loop since `is_ref` doesn't change, then use it repeatedly in the inner loop to avoid recreating that boolean array each iteration.

Computing contingency tables... Computing the expected value under the null hypothesis, then calculating the chi-squared statistic with continuity correction and checking if the p-value meets the significance threshold to count valid associations.

Now I'm working through the performance estimates: with roughly 20 microseconds per item across 12,500 iterations per permutation, that's about a quarter second per permutation, scaling to around 4 minutes total for 1000 permutations—though accounting for Python loop overhead and function call costs, I should be more conservative and expect closer to 20 minutes. I should also precompute the response variable as float64 upfront to avoid repeated type conversions during iteration.

I need to precompute the strata indices as integers too to save time per iteration. When I write the final script, I'll need to handle the edge case where quantile ties might result in fewer strata than expected—my vectorized approach will just create empty strata with zero counts, which the validity check will naturally skip over.

Now I'm realizing there's a potential discrepancy: the original code uses `np.unique` on quantiles to eliminate duplicates before binning, but my vectorized version compares against all edges directly. Let me trace through an example to see if this causes different stratification—when quantiles have ties, the original gets fewer bins while mine might assign the same stratum index to multiple ranges. I see the real issue now—the original code uses inclusive lower bounds and exclusive upper bounds for each stratum, while my vectorized approach with digitize creates different boundary behavior. Even though both methods group models with the same score together consistently, the stratum assignments differ when there are tied quantile values, which could affect how the MH statistic aggregates the contingency table counts across strata. I'm verifying that my approach with fixed strata matches the original code's behavior, which uses variable bin counts based on unique quantile edges. Since empty strata contribute nothing to the Mantel-Haenszel computation, both methods should yield identical or nearly identical C% values regardless of how many bins are actually populated.

Now I'm thinking through the memory implications of precomputing the transposed strata and response arrays as specific types for efficient bincount operations.

I could store strata_T as int8 to save space since the values only range from 0-4, then convert to intp per iteration, which would bring the total memory down to around 47 MB instead of 378 MB. The per-item conversion overhead is worth considering, but the memory savings are substantial enough that it's probably the better approach. I'm deciding whether to precompute `resp_T` as float64 (189 MB) for faster row-wise access during the 12.5 million permutation iterations, since contiguous memory access will significantly outweigh the storage cost. resp_weights = X_bool.T.astype(np.float64) (189 MB) and strata_int = strata.T.copy() (23.6 MB as int8). Then in the loop, the combined encoding will upcast strata_int[j] from int8 to int automatically when added to foc_offset (which is intp).

Let me verify that np.bincount accepts int8 arrays—it should work fine since it just needs non-negative integers, and my values are 0-4. When I add foc_offset (intp) to the int8 array, it'll automatically upcast to intp, so no extra conversion is needed.

Now I'm ready to write the script. The foc_offset computation is negligible since it's calculated once per permutation outside the item loop, and while the chi2.cdf calls are expensive, most items won't trigger them since |delta| < 1.5 in most cases.

I'm thinking through the fraction of items that actually reach the chi2 step—it's not just items with |delta| ≥ 1.5, but those that also satisfy p < 0.05, which is a stricter filter.  Even accounting for B items (those with |delta| ≥ 1.5 but p ≥ 0.05), I estimate around 40% of items hit the chi2 calculation, and at ~5ms per permutation that's negligible overhead. For permuted data the percentage will drop further anyway. I should stop optimizing prematurely and just implement the script with the basic structure: load and precompute, verify the observed C%, then run the permutations.

Now I'm thinking about memory efficiency for the weighted bincount. Converting the entire boolean array to float64 upfront would use 189 MB, which is wasteful. Instead, I'll precompute the transpose as float64 so that accessing each column gives me a contiguous array without repeated conversions. I'm settling on keeping the response matrix as int8 since numpy's bincount will handle the type conversion internally, and the memory footprint stays around 50 MB total with the transposed arrays and supporting data structures.

Adding about 189 MB temporarily during precomputation is manageable, so I'll proceed with writing the script. I'm debating whether multiprocessing is worth it for the 1000 permutations—each one takes roughly half a second to a few seconds, which means the full run would take 8-17 minutes single-threaded, and the overhead of forking and inter-process communication probably isn't justified for that timeline.

I'll keep it simple and write a single-threaded version first, defaulting to one process, since I can always add parallelism later if benchmarking shows it's necessary. Before I start, I need to fix the `is_ref_true` computation to avoid the slow loop by vectorizing the lookup...

Writing the script...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7be8adbd-66ad-44c9-865f-bfbd1dead724",
  "isSidechain": false,
  "requestId": "req_011CbFXAxaTmWCRR8ZifPq7z",
  "type": "assistant",
  "uuid": "9924bac9-2790-4ae4-ae08-87e37f4cf795",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ShJRFxRg5shtJPr8h7HLW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12272,
      "cache_read_input_tokens": 24605,
      "output_tokens": 22970,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12272,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 22970,
          "cache_read_input_tokens": 24605,
          "cache_creation_input_tokens": 12272,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12272
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

_source line 17 · 2026-05-21T10:07:40.081Z_

Now I have a clear picture of the data and the reference MH-DIF implementation. Key insight: the purified scores (and hence strata) are **fixed across permutations** since total scores depend only on the response matrix, not the ref/foc labels. I'll precompute strata once and use vectorized bincount per item for speed.

Let me create the output directory and write the optimized script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9924bac9-2790-4ae4-ae08-87e37f4cf795",
  "isSidechain": false,
  "requestId": "req_011CbFXAxaTmWCRR8ZifPq7z",
  "type": "assistant",
  "uuid": "285951a1-0427-4135-b2e3-8c2b8db0e334",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ShJRFxRg5shtJPr8h7HLW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12272,
      "cache_read_input_tokens": 24605,
      "output_tokens": 22970,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12272,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 22970,
          "cache_read_input_tokens": 24605,
          "cache_creation_input_tokens": 12272,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12272
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

_source line 18 · 2026-05-21T10:07:41.850Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01YTcb4PS2cmLw85GBus2n3F`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null && python3 -c \"import matplotlib; print(matplotlib.__version__)\"",
  "description": "Create output directory and check matplotlib availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "285951a1-0427-4135-b2e3-8c2b8db0e334",
  "isSidechain": false,
  "requestId": "req_011CbFXAxaTmWCRR8ZifPq7z",
  "type": "assistant",
  "uuid": "75b4a2e6-5be0-457e-b2cd-1ca0fe640062",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ShJRFxRg5shtJPr8h7HLW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12272,
      "cache_read_input_tokens": 24605,
      "output_tokens": 22970,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12272,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 22970,
          "cache_read_input_tokens": 24605,
          "cache_creation_input_tokens": 12272,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12272
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

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## 任务: plan_029 — Permutation Null for Temporal DIF C%  ### 目标 Reviewer 问\"31.3% C% 是否高于 chance\"。当前 random-split control (0.18%) 是 within-same-cohort，不是 temporal label permutation null。做 1000 次 permuta…",
  "leafUuid": "75b4a2e6-5be0-457e-b2cd-1ca0fe640062",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Permutation null distribution for temporal DIF C%",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd"
}
```

---

### Tool result

_source line 21 · 2026-05-21T10:07:42.519Z_

<details><summary>↩ Tool result · `toolu_01YTcb4PS2cmLw85GBus2n3F`</summary>

```text
3.10.9
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75b4a2e6-5be0-457e-b2cd-1ca0fe640062",
  "isSidechain": false,
  "promptId": "675b7191-b2b7-49a7-b6a4-83def2b806ad",
  "type": "user",
  "uuid": "060b92dd-0ecd-4767-b8ed-83a9a44ba14e",
  "toolUseResult": {
    "stdout": "3.10.9",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "75b4a2e6-5be0-457e-b2cd-1ca0fe640062",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T10:08:45.329Z_

<details open><summary>🔧 Tool call — Write · `toolu_012jLxQNrKwNBmWU8Ty7o6x7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/plan_029_permutation_null.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nplan_029_permutation_null.py — Permutation null for temporal DIF C%\n\nTests whether the observed ~31.3% C-category rate in temporal DIF (2023 vs 2024)\nexceeds chance under random label assignment.  1000 permutations, keeping group\nsizes fixed (N_ref=1080, N_foc=807).\n\nKey optimisation: purified scores (and hence strata) are independent of the\nref/foc split, so they are precomputed once.  Per-permutation work reduces to\ntwo np.bincount calls per item.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.sparse import load_npz\nfrom scipy.stats import chi2 as chi2_dist\nfrom pathlib import Path\nimport time\n\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/\"\n            \"projects/irt_equated_bench_regen/artifacts\")\nOUT = BASE / \"plan_029_permutation_null\"\nOUT.mkdir(exist_ok=True)\n\nN_PERM = 1000\nN_STRATA = 5\nSEED = 42\n\n# ═══════════════════════════════════════════════════════════════\n#  DATA\n# ═══════════════════════════════════════════════════════════════\nprint(\"Loading data...\")\nt0 = time.time()\n\nmat = load_npz(BASE / \"response_matrix.npz\")\nX_full = mat.toarray()          # int8, (5227, 12508)\ndel mat\n\nidx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\nMODEL_NAMES = idx[\"model_names\"]\nITEM_IDS = idx[\"item_ids\"]\nJ = len(ITEM_IDS)\n\nmeta = pd.read_csv(BASE / \"model_metadata.csv\")\nNAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}\n\n# Temporal subset (1887 models)\ntemporal_mask = meta[\"cohort_temporal\"].isin([\"2023\", \"2024\"])\ntemporal_meta = meta[temporal_mask].copy()\ntemporal_rows = np.array([NAME2ROW[n] for n in temporal_meta[\"model_name\"]\n                          if n in NAME2ROW])\nname2cohort = dict(zip(meta[\"model_name\"], meta[\"cohort_temporal\"]))\nis_ref_true = np.array([name2cohort[MODEL_NAMES[r]] == \"2023\"\n                         for r in temporal_rows])\n\nN_temp = len(temporal_rows)\nN_ref = int(is_ref_true.sum())\nN_foc = N_temp - N_ref\n\nX_temp = X_full[temporal_rows]   # (1887, 12508) int8\ndel X_full\n\nprint(f\"  N_temporal={N_temp}, N_ref={N_ref}, N_foc={N_foc}, J={J}\")\nprint(f\"  Loaded in {time.time() - t0:.1f}s\")\n\n# ═══════════════════════════════════════════════════════════════\n#  PRECOMPUTE STRATA  (fixed across permutations)\n# ═══════════════════════════════════════════════════════════════\nprint(\"Precomputing strata...\")\nt0 = time.time()\n\ntot = X_temp.astype(np.float64).sum(axis=1)       # (1887,)\npurified_all = tot[:, None] - X_temp.astype(np.float64)  # (1887, J)\n\nquantiles = np.linspace(0, 1, N_STRATA + 1)\nedges = np.quantile(purified_all, quantiles, axis=0)  # (6, J)\ninner_edges = edges[1:-1]                              # (4, J)\n\nstrata = np.zeros((N_temp, J), dtype=np.int8)\nfor e_idx in range(inner_edges.shape[0]):\n    strata += (purified_all >= inner_edges[e_idx][None, :]).astype(np.int8)\n\ndel purified_all, edges, inner_edges\n\nMAX_BINS = int(strata.max()) + 1          # should be 5\n\n# Transpose for contiguous row access in the hot loop\nstrata_T = strata.T.copy()                # (J, 1887) int8\nresp_T = X_temp.T.astype(np.float64)      # (J, 1887) float64 — weights for bincount\ndel X_temp, strata\n\nprint(f\"  Done in {time.time() - t0:.1f}s  (MAX_BINS={MAX_BINS})\")\n\n# ═══════════════════════════════════════════════════════════════\n#  FAST C% COMPUTATION\n# ═══════════════════════════════════════════════════════════════\nMINLEN = 2 * MAX_BINS\n\ndef compute_c_pct(is_ref):\n    \"\"\"Return C-category percentage given a ref/foc boolean mask.\"\"\"\n    foc_offset = (~is_ref).astype(np.intp) * MAX_BINS   # (1887,)\n    n_c = 0\n\n    for j in range(J):\n        s_j = strata_T[j]          # (1887,) int8, contiguous row\n        r_j = resp_T[j]            # (1887,) float64, contiguous row\n\n        combined = s_j.astype(np.intp) + foc_offset\n\n        counts = np.bincount(combined, minlength=MINLEN)\n        correct = np.bincount(combined, weights=r_j, minlength=MINLEN)\n\n        n1 = counts[:MAX_BINS].astype(np.float64)\n        n0 = counts[MAX_BINS:2*MAX_BINS].astype(np.float64)\n        A  = correct[:MAX_BINS]\n        C  = correct[MAX_BINS:2*MAX_BINS]\n        B  = n1 - A\n        D  = n0 - C\n        Nk = n1 + n0\n        m1 = A + C\n        m0 = B + D\n\n        valid = (n1 > 0) & (n0 > 0) & (m1 > 0) & (m0 > 0) & (Nk > 1)\n        if not valid.any():\n            continue\n\n        Av, Bv, Cv, Dv = A[valid], B[valid], C[valid], D[valid]\n        Nkv = Nk[valid]\n        n1v, n0v, m1v, m0v = n1[valid], n0[valid], m1[valid], m0[valid]\n\n        R = (Av * Dv / Nkv).sum()\n        S = (Bv * Cv / Nkv).sum()\n        if R == 0 or S == 0:\n            continue\n\n        delta = -2.35 * np.log(R / S)\n        if abs(delta) < 1.5:\n            continue\n\n        EA = n1v * m1v / Nkv\n        sum_diff = (Av - EA).sum()\n        sum_var = (n1v * n0v * m1v * m0v / (Nkv * Nkv * (Nkv - 1))).sum()\n        if sum_var <= 0:\n            continue\n\n        chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n        pval = 1.0 - chi2_dist.cdf(chi2_stat, df=1)\n        if pval < 0.05:\n            n_c += 1\n\n    return n_c / J * 100\n\n\n# ═══════════════════════════════════════════════════════════════\n#  VERIFY OBSERVED C%\n# ═══════════════════════════════════════════════════════════════\nprint(\"\\nVerifying observed C%...\")\nt0 = time.time()\nobserved_c = compute_c_pct(is_ref_true)\ndt_single = time.time() - t0\nprint(f\"  Observed C% = {observed_c:.2f}%  ({dt_single:.1f}s)\")\n\n# ═══════════════════════════════════════════════════════════════\n#  PERMUTATION TEST\n# ═══════════════════════════════════════════════════════════════\nprint(f\"\\nRunning {N_PERM} permutations (seed={SEED}, \"\n      f\"est. {dt_single * N_PERM / 60:.0f} min)...\")\nrng = np.random.RandomState(SEED)\nperm_results = []\nt_start = time.time()\n\nfor i in range(N_PERM):\n    perm_idx = rng.permutation(N_temp)\n    is_ref_perm = np.zeros(N_temp, dtype=bool)\n    is_ref_perm[perm_idx[:N_ref]] = True\n\n    c_pct = compute_c_pct(is_ref_perm)\n    perm_results.append(c_pct)\n\n    if (i + 1) % 10 == 0:\n        elapsed = time.time() - t_start\n        avg = elapsed / (i + 1)\n        eta = avg * (N_PERM - i - 1)\n        n_exceed = sum(1 for x in perm_results if x >= observed_c)\n        print(f\"  [{i+1:4d}/{N_PERM}] C%={c_pct:.2f}%  \"\n              f\"max_null={max(perm_results):.2f}%  \"\n              f\"n_exceed={n_exceed}  \"\n              f\"{avg:.1f}s/perm  ETA {eta/60:.1f}min\")\n\n    if (i + 1) == 100:\n        n_exc = sum(1 for x in perm_results if x >= observed_c)\n        print(f\"\\n  [checkpoint] 100 permutations done, \"\n              f\"n_exceed={n_exc}, max_null={max(perm_results):.2f}%\")\n        if n_exc == 0:\n            print(f\"  Already p < 0.01; continuing to {N_PERM} for precision.\\n\")\n\ntotal_time = time.time() - t_start\nprint(f\"\\nCompleted {N_PERM} permutations in {total_time / 60:.1f} min\")\n\n# ═══════════════════════════════════════════════════════════════\n#  STATISTICS\n# ═══════════════════════════════════════════════════════════════\nnull = np.array(perm_results)\nn_exceed = int((null >= observed_c).sum())\np_value = (n_exceed + 1) / (N_PERM + 1)     # conservative\n\nnull_mean = null.mean()\nnull_std  = null.std()\nnull_ci   = (np.percentile(null, 2.5), np.percentile(null, 97.5))\nnull_max  = null.max()\nnull_min  = null.min()\n\nprint(f\"\\n{'=' * 55}\")\nprint(\"RESULTS\")\nprint(f\"{'=' * 55}\")\nprint(f\"  Observed C%      {observed_c:.2f}%\")\nprint(f\"  Null mean ± SD   {null_mean:.2f}% ± {null_std:.2f}%\")\nprint(f\"  Null 95% CI      [{null_ci[0]:.2f}%, {null_ci[1]:.2f}%]\")\nprint(f\"  Null range       [{null_min:.2f}%, {null_max:.2f}%]\")\nprint(f\"  N exceed         {n_exceed} / {N_PERM}\")\np_str = \"< 0.001\" if p_value < 0.001 else f\"= {p_value:.4f}\"\nprint(f\"  p-value          {p_str}\")\n\n# ═══════════════════════════════════════════════════════════════\n#  OUTPUTS\n# ═══════════════════════════════════════════════════════════════\n\n# 1. CSV\npd.DataFrame({\"permutation\": np.arange(1, N_PERM + 1),\n              \"c_pct\": perm_results}).to_csv(\n    OUT / \"permutation_results.csv\", index=False)\n\n# 2. Figure\nfig, ax = plt.subplots(figsize=(7, 4))\nax.hist(null, bins=40, color=\"#4A90D9\", edgecolor=\"white\", alpha=0.85,\n        label=\"Null distribution\")\nax.axvline(observed_c, color=\"#D9534F\", lw=2, ls=\"--\",\n           label=f\"Observed = {observed_c:.1f}%\")\nax.set_xlabel(\"C% (ETS category C items)\", fontsize=11)\nax.set_ylabel(\"Count\", fontsize=11)\nax.set_title(f\"Permutation Null for Temporal DIF C%\\n\"\n             f\"(N={N_PERM}, p {p_str})\", fontsize=12)\nax.legend(fontsize=10)\nax.annotate(f\"Null: {null_mean:.1f}% ± {null_std:.1f}%\\n\"\n            f\"Observed: {observed_c:.1f}%\\n\"\n            f\"p {p_str}\",\n            xy=(0.97, 0.95), xycoords=\"axes fraction\",\n            ha=\"right\", va=\"top\", fontsize=9,\n            bbox=dict(boxstyle=\"round,pad=0.3\",\n                      facecolor=\"lightyellow\", edgecolor=\"gray\"))\nfig.tight_layout()\nfig.savefig(OUT / \"fig_permutation_null.png\", dpi=200)\nplt.close()\n\n# 3. Report\nreport = f\"\"\"# Plan 029: Permutation Null for Temporal DIF C%\n\n## Purpose\n\nTest whether the observed temporal DIF C% significantly exceeds the rate\nexpected under random label assignment.\n\n## Method\n\n- **Data**: {N_temp} models with temporal labels ({N_ref} \"2023\", {N_foc} \"2024\"), {J} items\n- **Procedure**: {N_PERM} permutations of temporal labels, group sizes fixed\n- **MH-DIF**: purified matching, {N_STRATA} quantile strata, ETS classification\n- **Seed**: {SEED}\n- **Optimisation**: strata precomputed once (invariant to label permutation)\n\n## Results\n\n| Metric | Value |\n|--------|-------|\n| Observed C% | {observed_c:.2f}% |\n| Null mean ± SD | {null_mean:.2f}% ± {null_std:.2f}% |\n| Null 95% CI | [{null_ci[0]:.2f}%, {null_ci[1]:.2f}%] |\n| Null range | [{null_min:.2f}%, {null_max:.2f}%] |\n| N exceed observed | {n_exceed} / {N_PERM} |\n| p-value | {p_str} |\n\n## Interpretation\n\nThe observed temporal DIF C% of {observed_c:.2f}% is \\\n{\"**far above**\" if p_value < 0.001 else \"**above**\" if p_value < 0.05 else \"not above\"} \\\nthe permutation null (mean {null_mean:.2f}%, max {null_max:.2f}%, \\\np {p_str}).  The 31.3% C-category rate cannot be attributed to \\\nchance label assignment.\n\n## Runtime\n\n- Per permutation: ~{dt_single:.1f}s\n- Total: {total_time / 60:.1f} min ({N_PERM} permutations)\n\"\"\"\n\n(OUT / \"permutation_null_report.md\").write_text(report)\n\nprint(f\"\\nOutputs → {OUT}/\")\nfor f in [\"permutation_results.csv\", \"fig_permutation_null.png\",\n          \"permutation_null_report.md\"]:\n    p = OUT / f\n    print(f\"  {f}  ({p.stat().st_size / 1024:.0f} KB)\" if p.exists() else\n          f\"  {f}  MISSING\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "060b92dd-0ecd-4767-b8ed-83a9a44ba14e",
  "isSidechain": false,
  "requestId": "req_011CbFXeA9z83TAYA2eUGFFt",
  "type": "assistant",
  "uuid": "ea10827c-06ec-42ce-bee9-4f2fbab8c554",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H29YUHNWRNBhuy5Lk29KBV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22939,
      "cache_read_input_tokens": 36877,
      "output_tokens": 4336,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22939,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4336,
          "cache_read_input_tokens": 36877,
          "cache_creation_input_tokens": 22939,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22939
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

_source line 23 · 2026-05-21T10:08:45.354Z_

<details><summary>↩ Tool result · `toolu_012jLxQNrKwNBmWU8Ty7o6x7`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/plan_029_permutation_null.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea10827c-06ec-42ce-bee9-4f2fbab8c554",
  "isSidechain": false,
  "promptId": "675b7191-b2b7-49a7-b6a4-83def2b806ad",
  "type": "user",
  "uuid": "3128e706-08cf-4201-bc32-7047f85520d5",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/plan_029_permutation_null.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nplan_029_permutation_null.py — Permutation null for temporal DIF C%\n\nTests whether the observed ~31.3% C-category rate in temporal DIF (2023 vs 2024)\nexceeds chance under random label assignment.  1000 permutations, keeping group\nsizes fixed (N_ref=1080, N_foc=807).\n\nKey optimisation: purified scores (and hence strata) are independent of the\nref/foc split, so they are precomputed once.  Per-permutation work reduces to\ntwo np.bincount calls per item.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.sparse import load_npz\nfrom scipy.stats import chi2 as chi2_dist\nfrom pathlib import Path\nimport time\n\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/\"\n            \"projects/irt_equated_bench_regen/artifacts\")\nOUT = BASE / \"plan_029_permutation_null\"\nOUT.mkdir(exist_ok=True)\n\nN_PERM = 1000\nN_STRATA = 5\nSEED = 42\n\n# ═══════════════════════════════════════════════════════════════\n#  DATA\n# ═══════════════════════════════════════════════════════════════\nprint(\"Loading data...\")\nt0 = time.time()\n\nmat = load_npz(BASE / \"response_matrix.npz\")\nX_full = mat.toarray()          # int8, (5227, 12508)\ndel mat\n\nidx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\nMODEL_NAMES = idx[\"model_names\"]\nITEM_IDS = idx[\"item_ids\"]\nJ = len(ITEM_IDS)\n\nmeta = pd.read_csv(BASE / \"model_metadata.csv\")\nNAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}\n\n# Temporal subset (1887 models)\ntemporal_mask = meta[\"cohort_temporal\"].isin([\"2023\", \"2024\"])\ntemporal_meta = meta[temporal_mask].copy()\ntemporal_rows = np.array([NAME2ROW[n] for n in temporal_meta[\"model_name\"]\n                          if n in NAME2ROW])\nname2cohort = dict(zip(meta[\"model_name\"], meta[\"cohort_temporal\"]))\nis_ref_true = np.array([name2cohort[MODEL_NAMES[r]] == \"2023\"\n                         for r in temporal_rows])\n\nN_temp = len(temporal_rows)\nN_ref = int(is_ref_true.sum())\nN_foc = N_temp - N_ref\n\nX_temp = X_full[temporal_rows]   # (1887, 12508) int8\ndel X_full\n\nprint(f\"  N_temporal={N_temp}, N_ref={N_ref}, N_foc={N_foc}, J={J}\")\nprint(f\"  Loaded in {time.time() - t0:.1f}s\")\n\n# ═══════════════════════════════════════════════════════════════\n#  PRECOMPUTE STRATA  (fixed across permutations)\n# ═══════════════════════════════════════════════════════════════\nprint(\"Precomputing strata...\")\nt0 = time.time()\n\ntot = X_temp.astype(np.float64).sum(axis=1)       # (1887,)\npurified_all = tot[:, None] - X_temp.astype(np.float64)  # (1887, J)\n\nquantiles = np.linspace(0, 1, N_STRATA + 1)\nedges = np.quantile(purified_all, quantiles, axis=0)  # (6, J)\ninner_edges = edges[1:-1]                              # (4, J)\n\nstrata = np.zeros((N_temp, J), dtype=np.int8)\nfor e_idx in range(inner_edges.shape[0]):\n    strata += (purified_all >= inner_edges[e_idx][None, :]).astype(np.int8)\n\ndel purified_all, edges, inner_edges\n\nMAX_BINS = int(strata.max()) + 1          # should be 5\n\n# Transpose for contiguous row access in the hot loop\nstrata_T = strata.T.copy()                # (J, 1887) int8\nresp_T = X_temp.T.astype(np.float64)      # (J, 1887) float64 — weights for bincount\ndel X_temp, strata\n\nprint(f\"  Done in {time.time() - t0:.1f}s  (MAX_BINS={MAX_BINS})\")\n\n# ═══════════════════════════════════════════════════════════════\n#  FAST C% COMPUTATION\n# ═══════════════════════════════════════════════════════════════\nMINLEN = 2 * MAX_BINS\n\ndef compute_c_pct(is_ref):\n    \"\"\"Return C-category percentage given a ref/foc boolean mask.\"\"\"\n    foc_offset = (~is_ref).astype(np.intp) * MAX_BINS   # (1887,)\n    n_c = 0\n\n    for j in range(J):\n        s_j = strata_T[j]          # (1887,) int8, contiguous row\n        r_j = resp_T[j]            # (1887,) float64, contiguous row\n\n        combined = s_j.astype(np.intp) + foc_offset\n\n        counts = np.bincount(combined, minlength=MINLEN)\n        correct = np.bincount(combined, weights=r_j, minlength=MINLEN)\n\n        n1 = counts[:MAX_BINS].astype(np.float64)\n        n0 = counts[MAX_BINS:2*MAX_BINS].astype(np.float64)\n        A  = correct[:MAX_BINS]\n        C  = correct[MAX_BINS:2*MAX_BINS]\n        B  = n1 - A\n        D  = n0 - C\n        Nk = n1 + n0\n        m1 = A + C\n        m0 = B + D\n\n        valid = (n1 > 0) & (n0 > 0) & (m1 > 0) & (m0 > 0) & (Nk > 1)\n        if not valid.any():\n            continue\n\n        Av, Bv, Cv, Dv = A[valid], B[valid], C[valid], D[valid]\n        Nkv = Nk[valid]\n        n1v, n0v, m1v, m0v = n1[valid], n0[valid], m1[valid], m0[valid]\n\n        R = (Av * Dv / Nkv).sum()\n        S = (Bv * Cv / Nkv).sum()\n        if R == 0 or S == 0:\n            continue\n\n        delta = -2.35 * np.log(R / S)\n        if abs(delta) < 1.5:\n            continue\n\n        EA = n1v * m1v / Nkv\n        sum_diff = (Av - EA).sum()\n        sum_var = (n1v * n0v * m1v * m0v / (Nkv * Nkv * (Nkv - 1))).sum()\n        if sum_var <= 0:\n            continue\n\n        chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n        pval = 1.0 - chi2_dist.cdf(chi2_stat, df=1)\n        if pval < 0.05:\n            n_c += 1\n\n    return n_c / J * 100\n\n\n# ═══════════════════════════════════════════════════════════════\n#  VERIFY OBSERVED C%\n# ═══════════════════════════════════════════════════════════════\nprint(\"\\nVerifying observed C%...\")\nt0 = time.time()\nobserved_c = compute_c_pct(is_ref_true)\ndt_single = time.time() - t0\nprint(f\"  Observed C% = {observed_c:.2f}%  ({dt_single:.1f}s)\")\n\n# ═══════════════════════════════════════════════════════════════\n#  PERMUTATION TEST\n# ═══════════════════════════════════════════════════════════════\nprint(f\"\\nRunning {N_PERM} permutations (seed={SEED}, \"\n      f\"est. {dt_single * N_PERM / 60:.0f} min)...\")\nrng = np.random.RandomState(SEED)\nperm_results = []\nt_start = time.time()\n\nfor i in range(N_PERM):\n    perm_idx = rng.permutation(N_temp)\n    is_ref_perm = np.zeros(N_temp, dtype=bool)\n    is_ref_perm[perm_idx[:N_ref]] = True\n\n    c_pct = compute_c_pct(is_ref_perm)\n    perm_results.append(c_pct)\n\n    if (i + 1) % 10 == 0:\n        elapsed = time.time() - t_start\n        avg = elapsed / (i + 1)\n        eta = avg * (N_PERM - i - 1)\n        n_exceed = sum(1 for x in perm_results if x >= observed_c)\n        print(f\"  [{i+1:4d}/{N_PERM}] C%={c_pct:.2f}%  \"\n              f\"max_null={max(perm_results):.2f}%  \"\n              f\"n_exceed={n_exceed}  \"\n              f\"{avg:.1f}s/perm  ETA {eta/60:.1f}min\")\n\n    if (i + 1) == 100:\n        n_exc = sum(1 for x in perm_results if x >= observed_c)\n        print(f\"\\n  [checkpoint] 100 permutations done, \"\n              f\"n_exceed={n_exc}, max_null={max(perm_results):.2f}%\")\n        if n_exc == 0:\n            print(f\"  Already p < 0.01; continuing to {N_PERM} for precision.\\n\")\n\ntotal_time = time.time() - t_start\nprint(f\"\\nCompleted {N_PERM} permutations in {total_time / 60:.1f} min\")\n\n# ═══════════════════════════════════════════════════════════════\n#  STATISTICS\n# ═══════════════════════════════════════════════════════════════\nnull = np.array(perm_results)\nn_exceed = int((null >= observed_c).sum())\np_value = (n_exceed + 1) / (N_PERM + 1)     # conservative\n\nnull_mean = null.mean()\nnull_std  = null.std()\nnull_ci   = (np.percentile(null, 2.5), np.percentile(null, 97.5))\nnull_max  = null.max()\nnull_min  = null.min()\n\nprint(f\"\\n{'=' * 55}\")\nprint(\"RESULTS\")\nprint(f\"{'=' * 55}\")\nprint(f\"  Observed C%      {observed_c:.2f}%\")\nprint(f\"  Null mean ± SD   {null_mean:.2f}% ± {null_std:.2f}%\")\nprint(f\"  Null 95% CI      [{null_ci[0]:.2f}%, {null_ci[1]:.2f}%]\")\nprint(f\"  Null range       [{null_min:.2f}%, {null_max:.2f}%]\")\nprint(f\"  N exceed         {n_exceed} / {N_PERM}\")\np_str = \"< 0.001\" if p_value < 0.001 else f\"= {p_value:.4f}\"\nprint(f\"  p-value          {p_str}\")\n\n# ═══════════════════════════════════════════════════════════════\n#  OUTPUTS\n# ═══════════════════════════════════════════════════════════════\n\n# 1. CSV\npd.DataFrame({\"permutation\": np.arange(1, N_PERM + 1),\n              \"c_pct\": perm_results}).to_csv(\n    OUT / \"permutation_results.csv\", index=False)\n\n# 2. Figure\nfig, ax = plt.subplots(figsize=(7, 4))\nax.hist(null, bins=40, color=\"#4A90D9\", edgecolor=\"white\", alpha=0.85,\n        label=\"Null distribution\")\nax.axvline(observed_c, color=\"#D9534F\", lw=2, ls=\"--\",\n           label=f\"Observed = {observed_c:.1f}%\")\nax.set_xlabel(\"C% (ETS category C items)\", fontsize=11)\nax.set_ylabel(\"Count\", fontsize=11)\nax.set_title(f\"Permutation Null for Temporal DIF C%\\n\"\n             f\"(N={N_PERM}, p {p_str})\", fontsize=12)\nax.legend(fontsize=10)\nax.annotate(f\"Null: {null_mean:.1f}% ± {null_std:.1f}%\\n\"\n            f\"Observed: {observed_c:.1f}%\\n\"\n            f\"p {p_str}\",\n            xy=(0.97, 0.95), xycoords=\"axes fraction\",\n            ha=\"right\", va=\"top\", fontsize=9,\n            bbox=dict(boxstyle=\"round,pad=0.3\",\n                      facecolor=\"lightyellow\", edgecolor=\"gray\"))\nfig.tight_layout()\nfig.savefig(OUT / \"fig_permutation_null.png\", dpi=200)\nplt.close()\n\n# 3. Report\nreport = f\"\"\"# Plan 029: Permutation Null for Temporal DIF C%\n\n## Purpose\n\nTest whether the observed temporal DIF C% significantly exceeds the rate\nexpected under random label assignment.\n\n## Method\n\n- **Data**: {N_temp} models with temporal labels ({N_ref} \"2023\", {N_foc} \"2024\"), {J} items\n- **Procedure**: {N_PERM} permutations of temporal labels, group sizes fixed\n- **MH-DIF**: purified matching, {N_STRATA} quantile strata, ETS classification\n- **Seed**: {SEED}\n- **Optimisation**: strata precomputed once (invariant to label permutation)\n\n## Results\n\n| Metric | Value |\n|--------|-------|\n| Observed C% | {observed_c:.2f}% |\n| Null mean ± SD | {null_mean:.2f}% ± {null_std:.2f}% |\n| Null 95% CI | [{null_ci[0]:.2f}%, {null_ci[1]:.2f}%] |\n| Null range | [{null_min:.2f}%, {null_max:.2f}%] |\n| N exceed observed | {n_exceed} / {N_PERM} |\n| p-value | {p_str} |\n\n## Interpretation\n\nThe observed temporal DIF C% of {observed_c:.2f}% is \\\n{\"**far above**\" if p_value < 0.001 else \"**above**\" if p_value < 0.05 else \"not above\"} \\\nthe permutation null (mean {null_mean:.2f}%, max {null_max:.2f}%, \\\np {p_str}).  The 31.3% C-category rate cannot be attributed to \\\nchance label assignment.\n\n## Runtime\n\n- Per permutation: ~{dt_single:.1f}s\n- Total: {total_time / 60:.1f} min ({N_PERM} permutations)\n\"\"\"\n\n(OUT / \"permutation_null_report.md\").write_text(report)\n\nprint(f\"\\nOutputs → {OUT}/\")\nfor f in [\"permutation_results.csv\", \"fig_permutation_null.png\",\n          \"permutation_null_report.md\"]:\n    p = OUT / f\n    print(f\"  {f}  ({p.stat().st_size / 1024:.0f} KB)\" if p.exists() else\n          f\"  {f}  MISSING\")\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "ea10827c-06ec-42ce-bee9-4f2fbab8c554",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-21T10:08:48.703Z_

Now let me run it. The first permutation will benchmark speed — I expect ~1-2s per permutation with the precomputed strata optimization.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3128e706-08cf-4201-bc32-7047f85520d5",
  "isSidechain": false,
  "requestId": "req_011CbFXinmW9S4APeVuR9gWr",
  "type": "assistant",
  "uuid": "a9c78288-f598-4295-8c9b-d5723c98c528",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StHeMmYSr6kNeaohTo83iX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4407,
      "cache_read_input_tokens": 59816,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 59816,
          "cache_creation_input_tokens": 4407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4407
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

_source line 25 · 2026-05-21T10:08:49.594Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0124TipVwS8KjKf5NYK2w3c2`</summary>

```json
{
  "command": "python3 artifacts/plan_029_permutation_null/plan_029_permutation_null.py 2>&1",
  "description": "Run permutation null test (1000 permutations)",
  "timeout": 600000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9c78288-f598-4295-8c9b-d5723c98c528",
  "isSidechain": false,
  "requestId": "req_011CbFXinmW9S4APeVuR9gWr",
  "type": "assistant",
  "uuid": "858818d3-ebc9-4060-8ae1-baabe384de6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StHeMmYSr6kNeaohTo83iX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4407,
      "cache_read_input_tokens": 59816,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 59816,
          "cache_creation_input_tokens": 4407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4407
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

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## 任务: plan_029 — Permutation Null for Temporal DIF C%  ### 目标 Reviewer 问\"31.3% C% 是否高于 chance\"。当前 random-split control (0.18%) 是 within-same-cohort，不是 temporal label permutation null。做 1000 次 permuta…",
  "leafUuid": "858818d3-ebc9-4060-8ae1-baabe384de6c",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Permutation null distribution for temporal DIF C%",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd"
}
```

---

### Tool result

_source line 28 · 2026-05-21T10:16:09.373Z_

<details><summary>↩ Tool result · reported error · `toolu_0124TipVwS8KjKf5NYK2w3c2`</summary>

```text
Exit code 137
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "858818d3-ebc9-4060-8ae1-baabe384de6c",
  "isSidechain": false,
  "promptId": "675b7191-b2b7-49a7-b6a4-83def2b806ad",
  "type": "user",
  "uuid": "c6011b11-0e72-480e-bcd8-0d0b416a6d3c",
  "toolUseResult": "Error: Exit code 137",
  "sourceToolAssistantUUID": "858818d3-ebc9-4060-8ae1-baabe384de6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9f4e4f4d-d856-40d0-bf6d-b7a4138e63dd",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---
