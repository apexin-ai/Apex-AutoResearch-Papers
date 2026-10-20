# research rewrite scan report

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_research_rewrite_scan_report_20260515T134249.log`
- **Structured JSON:** [`1cd31681ee2f1a897a10.json`](../../sessions/1c/1cd31681ee2f1a897a10.json)

## Before a recorded user message

28 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "7c401b54-efc1-4d5f-9577-8e51945afc3a",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778862000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "48570abb-3f1c-4f6b-84af-9ebf12008580",
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6"
}
```

---

### Assistant

_source line 4_

I'll start by reading the current scan_report.md and literature_map.yaml to understand the existing content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "ce3927cc-14ff-4cb6-bdb8-07a438faae34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NP2mYaXZdDadxkKUqTv5SP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11413,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11413
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018xrLkKbrZwBg5zxoj9fxgB`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "9b9f3b2e-94de-4311-b175-dece04d81fec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NP2mYaXZdDadxkKUqTv5SP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11413,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11413
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T13:43:00.147Z_

<details><summary>↩ Tool result · `toolu_018xrLkKbrZwBg5zxoj9fxgB`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "92871caf-f913-4b5d-854d-96d89e201ed1",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me read the current scan_report.md and literature_map.yaml to understand the existing content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "77534006-7fb3-443b-b862-e06d7c0f5a9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QnsKSTDjFQCCXUBtMuTgbA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 724,
      "cache_read_input_tokens": 23254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 724
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01EzzFoT7VBdRPpZoCuvW8Ao`</summary>

```json
{
  "project": "trace-verdict-study",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "0c0eafbb-9232-471e-999d-18c1a0269fd1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QnsKSTDjFQCCXUBtMuTgbA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 724,
      "cache_read_input_tokens": 23254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 724
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T13:43:03.374Z_

<details><summary>↩ Tool result · `toolu_01EzzFoT7VBdRPpZoCuvW8Ao`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| deepseek_exception_only_seed42 | Multi-model validation: exception_only on DeepSeek-Coder-6.7B-Instruct (plan_004). Tests if exception dominance (99.83% on Qwen) generalizes across models — the most valuable cross-model evidence. | — | — | — |\\n\\n## 待处理\\n- vota_seed42_v2（排队等待 GPU）\\n- vota_seed42（排队等待 GPU）\\n- no_trace_seed42_v2（排队等待 GPU）\\n- no_trace_seed42（排队等待 GPU）\\n- vota_seed456: Seed robustness: VOTA with seed=456 (plan_008). Verifies VOTA 99.2% accuracy is stable across random seeds.（准备中）\\n- deepseek_full_trace_seed42: Multi-model comparison: full-trace verdict prediction on DeepSeek-Coder-6.7B-Instruct (plan_004). Tests if full_trace also shows intermediate performance on DeepSeek-Coder.（准备中）\\n\\n## 近期结论\\n- **deepseek_no_trace_seed42** (success): Multi-model baseline: no-trace verdict prediction on DeepSeek-Coder-6.7B-Instruct (plan_004). Establishes DeepSeek baseline for comparison with VOTA and full_trace conditions.\\n- **deepseek_vota_seed42** (success): Multi-model validation: VOTA on DeepSeek-Coder-6.7B-Instruct (plan_004). Tests if VOTA's verdict accuracy advantage generalizes beyond Qwen2.5-Coder to DCSH's same base model.\\n  [deepseek_vota_seed42_analysis](/api/workspace-files/projects/trace-verdict-study/artifacts/deepseek_vota_seed42/report/analysis.md)\\n- **vota_seed123** (failed): Seed robustness: VOTA with seed=123 (plan_008). Verifies VOTA 99.2% accuracy is stable across random seeds.\\n\\n## 趋势\\n成功 13 / 负向 1 / 失败 2 / 共 19\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-11235: 无 GPU 信息\\n\\n## 告警\\n- no_trace_seed42_v3: 已被终止 — unknown\\n- vota_seed42_v3: 已被终止 — unknown\\n- full_trace_seed42: 已被终止 — unknown\\n- vota_exception_only_seed42: 训练失败 — unknown\\n- vota_seed123: 训练失败 — unknown\\n\", \"total_chars\": 1846, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "46585f53-ea16-4c00-a0de-79ac5abc89a5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/report.md\\\", \\\"content\\\": \\\"# Handover — 2026-05-15\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\\\n|--------|------|------|---------|-----|\\\\n| deepseek_exception_only_seed42 | Multi-model validation: exception_only on DeepSeek-Coder-6.7B-Instruct (plan_004). Tests if exception dominance (99.83% on Qwen) generalizes across models — the most valuable cross-model evidence. | — | — | — |\\\\n\\\\n## 待处理\\\\n- vota_seed42_v2（排队等待 GPU）\\\\n- vota_seed42（排队等待 GPU）\\\\n- no_trace_seed42_v2（排队等待 GPU）\\\\n- no_trace_seed42（排队等待 GPU）\\\\n- vota_seed456: Seed robustness: VOTA with seed=456 (plan_008). Verifies VOTA 99.2% accuracy is stable across random seeds.（准备中）\\\\n- deepseek_full_trace_seed42: Multi-model comparison: full-trace verdict prediction on DeepSeek-Coder-6.7B-Instruct (plan_004). Tests if full_trace also shows intermediate performance on DeepSeek-Coder.（准备中）\\\\n\\\\n## 近期结论\\\\n- **deepseek_no_trace_seed42** (success): Multi-model baseline: no-trace verdict prediction on DeepSeek-Coder-6.7B-Instruct (plan_004). Establishes DeepSeek baseline for comparison with VOTA and full_trace conditions.\\\\n- **deepseek_vota_seed42** (success): Multi-model validation: VOTA on DeepSeek-Coder-6.7B-Instruct (plan_004). Tests if VOTA's verdict accuracy advantage generalizes beyond Qwen2.5-Coder to DCSH's same base model.\\\\n  [deepseek_vota_seed42_analysis](/api/workspace-files/projects/trace-verdict-study/artifacts/deepseek_vota_seed42/report/analysis.md)\\\\n- **vota_seed123** (failed): Seed robustness: VOTA with seed=123 (plan_008). Verifies VOTA 99.2% accuracy is stable across random seeds.\\\\n\\\\n## 趋势\\\\n成功 13 / 负向 1 / 失败 2 / 共 19\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\nwestd-11235: 无 GPU 信息\\\\n\\\\n## 告警\\\\n- no_trace_seed42_v3: 已被终止 — unknown\\\\n- vota_seed42_v3: 已被终止 — unknown\\\\n- full_trace_seed42: 已被终止 — unknown\\\\n- vota_exception_only_seed42: 训练失败 — unknown\\\\n- vota_seed123: 训练失败 — unknown\\\\n\\\", \\\"total_chars\\\": 1846, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| deepseek_exception_only_seed42 | Multi-model validation: exception_only on DeepSeek-Coder-6.7B-Instruct (plan_004). Tests if exception dominance (99.83% on Qwen) generalizes across models — the most valuable cross-model evidence. | — | — | — |\\n\\n## 待处理\\n- vota_seed42_v2（排队等待 GPU）\\n- vota_seed42（排队等待 GPU）\\n- no_trace_seed42_v2（排队等待 GPU）\\n- no_trace_seed42（排队等待 GPU）\\n- vota_seed456: Seed robustness: VOTA with seed=456 (plan_008). Verifies VOTA 99.2% accuracy is stable across random seeds.（准备中）\\n- deepseek_full_trace_seed42: Multi-model comparison: full-trace verdict prediction on DeepSeek-Coder-6.7B-Instruct (plan_004). Tests if full_trace also shows intermediate performance on DeepSeek-Coder.（准备中）\\n\\n## 近期结论\\n- **deepseek_no_trace_seed42** (success): Multi-model baseline: no-trace verdict prediction on DeepSeek-Coder-6.7B-Instruct (plan_004). Establishes DeepSeek baseline for comparison with VOTA and full_trace conditions.\\n- **deepseek_vota_seed42** (success): Multi-model validation: VOTA on DeepSeek-Coder-6.7B-Instruct (plan_004). Tests if VOTA's verdict accuracy advantage generalizes beyond Qwen2.5-Coder to DCSH's same base model.\\n  [deepseek_vota_seed42_analysis](/api/workspace-files/projects/trace-verdict-study/artifacts/deepseek_vota_seed42/report/analysis.md)\\n- **vota_seed123** (failed): Seed robustness: VOTA with seed=123 (plan_008). Verifies VOTA 99.2% accuracy is stable across random seeds.\\n\\n## 趋势\\n成功 13 / 负向 1 / 失败 2 / 共 19\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-11235: 无 GPU 信息\\n\\n## 告警\\n- no_trace_seed42_v3: 已被终止 — unknown\\n- vota_seed42_v3: 已被终止 — unknown\\n- full_trace_seed42: 已被终止 — unknown\\n- vota_exception_only_seed42: 训练失败 — unknown\\n- vota_seed123: 训练失败 — unknown\\n\", \"total_chars\": 1846, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01EZwvbzWbKzwgPNQPovGZR7`</summary>

```json
{
  "project": "trace-verdict-study",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "72c5ab93-7a66-4806-a51c-b2ecf2e821f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QnsKSTDjFQCCXUBtMuTgbA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 724,
      "cache_read_input_tokens": 23254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 724
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T13:43:03.870Z_

<details><summary>↩ Tool result · `toolu_01EZwvbzWbKzwgPNQPovGZR7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/literature_map.yaml\", \"content\": \"categories:\\n  execution-trace-llm:\\n    description: \\\"Execution trace 辅助 LLM 代码理解/调试/推理\\\"\\n    papers:\\n      - title: \\\"NExT: Teaching Large Language Models to Reason about Code Execution\\\"\\n        authors: \\\"Ansong Ni, Miltiadis Allamanis, et al. (Google DeepMind)\\\"\\n        year: 2024\\n        venue: \\\"ICML 2024\\\"\\n        role: method-component\\n        key_finding: \\\"自训练在 execution trace 上做 CoT rationale，程序修复 fix rate 在 MBPP +26.1%、HumanEval +14.3%。模型可泛化到无 trace 的场景。\\\"\\n        metrics:\\n          mbpp_fix_rate_improvement: \\\"+26.1%\\\"\\n          humaneval_fix_rate_improvement: \\\"+14.3%\\\"\\n\\n      - title: \\\"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code LLMs\\\"\\n        authors: \\\"Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li\\\"\\n        year: 2025\\n        venue: \\\"Findings of EMNLP 2025\\\"\\n        role: direct-competitor\\n        key_finding: \\\"综合研究发现 execution trace 对 SFT 和 test-time scaling 的帮助有限，与先前工作结论相左。提出 trace adapter 做格式化。这是 VOTA 必须回应的关键负面结果——说明原始 trace 不够，需要针对性压缩/抽象。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Code Execution as Grounded Supervision for LLM Reasoning\\\"\\n        authors: \\\"Dongwon Jung, Wenxuan Zhou, Muhao Chen\\\"\\n        year: 2025\\n        venue: \\\"EMNLP 2025\\\"\\n        role: method-component\\n        key_finding: \\\"用 Python debugger (Snoop) 提取 step-by-step execution trace，转换为自然语言 CoT。训练后模型推理能力提升且生成更少 token（减少 overthinking），具备跨域迁移能力。\\\"\\n        metrics: {}\\n\\n      - title: \\\"What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces\\\"\\n        authors: \\\"Lorenzo Ferrando, Nicola Ferraro, et al.\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2503.05703\\\"\\n        role: method-component\\n        key_finding: \\\"对比 regular/compact/dynamic 三种 scratchpad 策略，compact（仅记录变化变量）略优于 regular（全部变量值）。CruxEval/MBPP ~80%。直接支持 plan_001：完整值信息冗余，精简不损失效果。\\\"\\n        metrics:\\n          cruxeval_accuracy: \\\"~80%\\\"\\n          mbpp_accuracy: \\\"~80%\\\"\\n\\n      - title: \\\"Demystifying Errors in LLM Reasoning Traces: An Empirical Study of Code Execution Simulation\\\"\\n        authors: \\\"arXiv 2512.00215\\\"\\n        year: 2025\\n        venue: \\\"arXiv\\\"\\n        role: evaluation\\n        key_finding: \\\"LLM 在循环中频繁遗漏/多算变量修改，函数返回值预测不准。说明 LLM 对具体值追踪能力弱于结构理解，为 plan_001 发现（值冗余）提供机制解释。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Reasoning Runtime Behavior of a Program with LLM: How Far Are We? (REval)\\\"\\n        authors: \\\"Junkai Chen et al.\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2403.16437\\\"\\n        role: evaluation\\n        key_finding: \\\"REval 框架评估 LLM 在 4 种 runtime behavior 预测任务上的表现：coverage prediction、program state prediction、execution path prediction、output prediction。平均 accuracy 仅 44.4%，IC score 10.3。揭示 LLM runtime reasoning 能力有限，支持 VOTA 的发现——需要抽象而非让 LLM 直接消化全量 trace。\\\"\\n        metrics:\\n          avg_accuracy: \\\"44.4%\\\"\\n          avg_ic_score: \\\"10.3\\\"\\n\\n      - title: \\\"CodeMind: Evaluating Large Language Models for Code Reasoning\\\"\\n        authors: \\\"Changshu Liu et al. (UIUC)\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2402.09664\\\"\\n        role: evaluation\\n        key_finding: \\\"评估 LLM 在 IER（执行推理）、SR（规格推理）、DSR（动态语义推理）三个维度的代码推理能力。性能随代码复杂度（控制流、非原始类型、API 调用）显著下降。支持 VOTA 的 trace abstraction 动机——复杂 trace 超出 LLM 推理能力。\\\"\\n        metrics: {}\\n\\n      - title: \\\"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\\\"\\n        authors: \\\"Ruiyang Xu et al. (HKUST)\\\"\\n        year: 2025\\n        venue: \\\"ACL 2025\\\"\\n        role: evaluation\\n        key_finding: \\\"将 CRUXEval 扩展到 19 种编程语言，19K 测试。仅在 Python 训练的模型在其他语言最高 34.4% Pass@1，揭示 cross-language generalization 的局限。对 VOTA 的 cross-model generalization 实验提供方法论参考。\\\"\\n        metrics:\\n          languages: 19\\n          cross_lang_max_pass1: \\\"34.4%\\\"\\n\\n  code-verdict:\\n    description: \\\"LLM 判断代码 pass/fail、正确性分类、mutation testing\\\"\\n    papers:\\n      - title: \\\"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\\\"\\n        authors: \\\"iSEngLab (Nanjing University)\\\"\\n        year: 2024\\n        venue: \\\"IEEE TSE 2024\\\"\\n        role: direct-competitor\\n        key_finding: \\\"BERT + LSTM + classifier 微调做 patch 正确性二分类。在 1183 个 Defects4J patches 上 accuracy 79.7%、recall 83.2%，优于 CACHE。与 VOTA 的 verdict 分类目标最接近。\\\"\\n        metrics:\\n          accuracy: \\\"79.7%\\\"\\n          recall: \\\"83.2%\\\"\\n          f1_improvement_from_finetuning: \\\"+10.22%\\\"\\n\\n      - title: \\\"LLM4PatchCorrect: Leveraging Large Language Model for Automatic Patch Correctness Assessment\\\"\\n        authors: \\\"Xin Zhou et al. (SMU)\\\"\\n        year: 2024\\n        venue: \\\"IEEE TSE 2024\\\"\\n        role: direct-competitor\\n        key_finding: \\\"用 Starcoder-7B 零样本评估 patch 正确性，输入包含 bug description、execution traces、failing test cases、test coverage。无需微调即达 84.4% accuracy。使用了 execution trace 作为输入信号，与 VOTA 输入空间有重叠，但方法（zero-shot prompting vs SFT）和任务（patch correctness vs test verdict）不同。\\\"\\n        metrics:\\n          accuracy: \\\"84.4%\\\"\\n          f1: \\\"86.5%\\\"\\n        novelty_threat: medium\\n\\n      - title: \\\"Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph for Automated Patch Correctness Assessment\\\"\\n        authors: \\\"arXiv 2505.02629\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2505.02629\\\"\\n        role: direct-competitor\\n        key_finding: \\\"提出 APSG（Attributed Patch Semantic Graph）+ Graph-LoRA，用图结构捕获 patch 语义的 data/control flow。在 patch correctness 上比 SOTA 提升 accuracy 3.1-7.5%、F1 3.0-7.1%。方法论（PEFT + 结构化代码表示做分类）与 VOTA 有相似之处，但 VOTA 用 trace signal 而非 graph。\\\"\\n        metrics:\\n          accuracy_improvement: \\\"+3.1-7.5%\\\"\\n          f1_improvement: \\\"+3.0-7.1%\\\"\\n        novelty_threat: medium\\n\\n      - title: \\\"Calibration and Correctness of Language Models for Code\\\"\\n        authors: \\\"Claudio Spiess, David Gros, et al.\\\"\\n        year: 2025\\n        venue: \\\"ICSE 2025\\\"\\n        role: evaluation\\n        key_finding: \\\"代码生成模型的置信度校准普遍较差。Platt scaling 可改善但需要先验正确性数据。对 VOTA 的启示：verdict 分类需关注校准，不只是准确率。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Mutation-Guided LLM-based Test Generation at Meta\\\"\\n        authors: \\\"Christopher Foster et al. (Meta)\\\"\\n        year: 2025\\n        venue: \\\"FSE 2025 (Industry)\\\"\\n        role: evaluation\\n        key_finding: \\\"LLM equivalence detector 判断 mutant 是否等价，加简单预处理后 precision 0.95、recall 0.96。大规模部署到 10K+ 类，工程师接受率 73%。展示了 LLM 做代码正确性判断的工业可行性。\\\"\\n        metrics:\\n          precision: \\\"0.95\\\"\\n          recall: \\\"0.96\\\"\\n          classes_evaluated: \\\"10795\\\"\\n          test_acceptance_rate: \\\"73%\\\"\\n\\n      - title: \\\"FuseFL: Demystifying Faulty Code with LLM via Step-by-Step Reasoning\\\"\\n        authors: \\\"Ratnadira Widyasari et al. (SMU)\\\"\\n        year: 2024\\n        venue: \\\"SANER 2024\\\"\\n        role: background\\n        key_finding: \\\"融合 SBFL 排名 + test execution outcomes（input、expected/actual output、errors）+ code description 做 fault localization。Top-1 localization 比 baseline 提升 32.3%，比 SBFL 提升 68.4%。test execution outcomes 作为输入信号与 VOTA 的 fault indicator signals 理念相关。\\\"\\n        metrics:\\n          top1_improvement_over_baseline: \\\"+32.3%\\\"\\n          top1_improvement_over_sbfl: \\\"+68.4%\\\"\\n\\n  trace-compression:\\n    description: \\\"Execution trace 的压缩、摘要、抽象方法\\\"\\n    papers:\\n      - title: \\\"Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning\\\"\\n        authors: \\\"Aashish Yadavally, Yi Li, Tien Nguyen\\\"\\n        year: 2024\\n        venue: \\\"FSE 2024\\\"\\n        role: method-component\\n        key_finding: \\\"ND-Slicer 用 execution-aware 预训练学习动态依赖，无需实际执行即可预测特定输入的程序切片。Python 上 exact-match 81.31%、ROUGE-LCS 0.954。与 VOTA 的 assertion-point snapshots 思路类似——都是从完整 trace 中提取关键信息。\\\"\\n        metrics:\\n          exact_match: \\\"81.31%\\\"\\n          rouge_lcs: \\\"0.954\\\"\\n          fault_localization_accuracy: \\\"63.88%\\\"\\n\\n      - title: \\\"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\\\"\\n        authors: \\\"Mirazul Haque, Petr Babkin, et al. (J.P. Morgan AI Research)\\\"\\n        year: 2025\\n        venue: \\\"KnowledgeNLP Workshop @ ACL 2025\\\"\\n        role: background\\n        key_finding: \\\"直接将 execution trace 加入 prompt 帮助有限，且随 trace 复杂度增加效果递减。LLM 优化的 prompt 格式比原始 trace 更一致地优于无 trace baseline。直接支持 VOTA 的核心假设：原始 trace 太冗长，需要专门的压缩/抽象。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Making LLMs Program Interpreters via Execution Trace Chain of Thought (ET-CoT)\\\"\\n        authors: \\\"ICML 2025 Workshop PRAL\\\"\\n        year: 2025\\n        venue: \\\"ICML 2025 Workshop\\\"\\n        role: method-component\\n        key_finding: \\\"开发 PyTracify 工具生成 sub-line 粒度的结构化 execution trace，SFT 后 Qwen2.5-7B 在 CRUXEval-O 达 70.0%、LiveCodeBench 达 88.3%，超过同规模 code-oriented 模型。其 trace 格式本身是一种 trace abstraction。\\\"\\n        metrics:\\n          cruxeval_o: \\\"70.0%\\\"\\n          livecodebench_execution: \\\"88.3%\\\"\\n\\n      - title: \\\"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\\\"\\n        authors: \\\"ICSE 2026 Research Track\\\"\\n        year: 2026\\n        venue: \\\"ICSE 2026\\\"\\n        role: background\\n        key_finding: \\\"在特定位置插入 diagnostic probes 而非全量 trace 记录，Pass@1 提升 34.43%。选择性 trace 采集优于全量，支持 VOTA 的行为模式抽象思路。\\\"\\n        metrics:\\n          pass_at_1_improvement: \\\"+34.43%\\\"\\n\\n      - title: \\\"Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate\\\"\\n        authors: \\\"Jiaqing Wu et al.\\\"\\n        year: 2026\\n        venue: \\\"arXiv 2604.02647\\\"\\n        role: background\\n        key_finding: \\\"Probe agent 选择性捕获 critical variables 的 execution snapshots 用于 multi-agent repair debate，修复 392 个缺陷。验证了选择性 trace 信息优于全量记录。\\\"\\n        metrics:\\n          defects_fixed: \\\"392\\\"\\n\\n      - title: \\\"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration\\\"\\n        authors: \\\"arXiv 2510.18327\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2510.18327\\\"\\n        role: background\\n        key_finding: \\\"首个让 LLM 主动控制 debugger 做动态分析的 agentic repair 系统。Program Inspector 做策略性 breakpoint 放置和 runtime state 检查，Patch Coder 合成修复。比最强 baseline 提升 5.10-60.37%。选择性 runtime 检查理念与 VOTA 的 fault indicator signal 提取一致。\\\"\\n        metrics:\\n          repair_accuracy_improvement: \\\"+5.10-60.37%\\\"\\n\\n      - title: \\\"MGDebugger: From Code to Correctness via Hierarchical Debugging\\\"\\n        authors: \\\"Yuling Shi et al.\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2410.01215\\\"\\n        role: background\\n        key_finding: \\\"层次化分解代码为子函数树，LLM 模拟执行追踪关键变量状态，bottom-up 定位修复。HumanEval accuracy 75.6%→94.5%。其 LLM-simulated executor 追踪变量状态的方式是一种隐式 trace abstraction。\\\"\\n        metrics:\\n          humaneval_accuracy: \\\"94.5%\\\"\\n          humaneval_fix_accuracy: \\\"97.6%\\\"\\n\\n  debugging-agents:\\n    description: \\\"LLM 多智能体调试框架\\\"\\n    papers:\\n      - title: \\\"UniDebugger: Hierarchical Multi-Agent Framework for Unified Software Debugging\\\"\\n        authors: \\\"Cheryl Lee, Chunqiu Steven Xia, et al. (Lingming Zhang group)\\\"\\n        year: 2025\\n        venue: \\\"EMNLP 2025\\\"\\n        role: background\\n        key_finding: \\\"三层认知架构模拟开发者调试过程，L1→L2→L3 逐层升级。在 Defects4J 上修复 1.25-2.56x bugs。不使用 execution trace 作为输入（纯静态分析），与 VOTA 方法正交。\\\"\\n        metrics:\\n          defects4j_improvement: \\\"1.25-2.56x\\\"\\n\\n      - title: \\\"Seeker: Enhancing Exception Handling in Code with LLM-based Multi-Agent Approach\\\"\\n        authors: \\\"Xuanming Zhang et al.\\\"\\n        year: 2025\\n        venue: \\\"ICLR 2025\\\"\\n        role: background\\n        key_finding: \\\"5-agent 框架做 exception handling 生成，构建 Common Exception Enumeration (CEE) 知识库。Exception handling precision 提升 37%。从 exception taxonomy 角度提供背景——exception 类型和处理策略的系统化，与 VOTA 的 exception event 信号提取视角互补。\\\"\\n        metrics:\\n          exception_handling_precision_improvement: \\\"+37%\\\"\\n\\n  sft-classification:\\n    description: \\\"用 SFT 做分类任务的方法论和 findings\\\"\\n    papers:\\n      - title: \\\"Fine-Tuning Causal LLMs for Text Classification: Embedding-Based vs. Instruction-Based Approaches\\\"\\n        authors: \\\"Amirhossein Yousefiramandi, Ciaran Cooney\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2512.12677\\\"\\n        role: method-component\\n        key_finding: \\\"对比 embedding-based（加分类头）vs instruction-based（prompt->response）两种 SFT 分类方式。Embedding-based + QLoRA 在 F1 上与 instruction-tuned 持平，但可训练参数少得多。对 VOTA 的 verdict 分类有直接参考价值——选哪种 SFT 格式。\\\"\\n        metrics: {}\\n\\n      - title: \\\"FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain\\\"\\n        authors: \\\"Rohan Deb, Kiran Koshy Thekumparampil, et al.\\\"\\n        year: 2025\\n        venue: \\\"ICML 2025\\\"\\n        role: background\\n        key_finding: \\\"用 Fisher 信息矩阵选择信息量最大的训练样本子集，通过 last-layer 线性化高效近似。在固定数据预算下提升 SFT 效果。对 VOTA 的数据选择策略有参考价值。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Fine-Tuned 'Small' LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification\\\"\\n        authors: \\\"Martin Juan Jose Bucher, Marco Martini\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2406.08660\\\"\\n        role: background\\n        key_finding: \\\"跨多种分类任务（情感、立场、情绪等），fine-tuned 小模型全面优于 GPT-4/Claude 的 zero-shot。验证了 VOTA 用 SFT 做 verdict 分类的基本假设——fine-tuning 在分类上优于 prompting。\\\"\\n        metrics: {}\\n\\nmeta:\\n  last_updated: \\\"2026-05-15\\\"\\n  total_papers: 26\\n  search_scope: \\\"2024-2026, top ML/NLP/SE venues\\\"\\n  scan_date: \\\"2026-05-15\\\"\\n  scan_queries: 16\\n  key_gaps:\\n    - \\\"缺少直接将 execution trace 用于 binary verdict (pass/fail) 的工作——VOTA 填补此空白\\\"\\n    - \\\"trace compression 文献多在 distributed systems 或 formal verification 领域，code-level trace 压缩给 LLM 用的工作极少\\\"\\n    - \\\"SFT for classification 研究多在 NLP 文本分类，code verdict 场景的 SFT 方法论研究接近空白\\\"\\n    - \\\"patch correctness prediction（LLM4PatchCorrect、APSG）是最近的竞争方向，但任务定义和输入信号与 VOTA 有本质区别\\\"\\n    - \\\"selective trace（InspectCoder、TraceCoder）趋势明显，但均用于 program repair 而非 verdict classification\\\"\\n\", \"total_chars\": 13257, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "6f7d1728-c4cc-4d25-b844-2d29ceddb3af",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/literature_map.yaml\\\", \\\"content\\\": \\\"categories:\\\\n  execution-trace-llm:\\\\n    description: \\\\\\\"Execution trace 辅助 LLM 代码理解/调试/推理\\\\\\\"\\\\n    papers:\\\\n      - title: \\\\\\\"NExT: Teaching Large Language Models to Reason about Code Execution\\\\\\\"\\\\n        authors: \\\\\\\"Ansong Ni, Miltiadis Allamanis, et al. (Google DeepMind)\\\\\\\"\\\\n        year: 2024\\\\n        venue: \\\\\\\"ICML 2024\\\\\\\"\\\\n        role: method-component\\\\n        key_finding: \\\\\\\"自训练在 execution trace 上做 CoT rationale，程序修复 fix rate 在 MBPP +26.1%、HumanEval +14.3%。模型可泛化到无 trace 的场景。\\\\\\\"\\\\n        metrics:\\\\n          mbpp_fix_rate_improvement: \\\\\\\"+26.1%\\\\\\\"\\\\n          humaneval_fix_rate_improvement: \\\\\\\"+14.3%\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code LLMs\\\\\\\"\\\\n        authors: \\\\\\\"Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"Findings of EMNLP 2025\\\\\\\"\\\\n        role: direct-competitor\\\\n        key_finding: \\\\\\\"综合研究发现 execution trace 对 SFT 和 test-time scaling 的帮助有限，与先前工作结论相左。提出 trace adapter 做格式化。这是 VOTA 必须回应的关键负面结果——说明原始 trace 不够，需要针对性压缩/抽象。\\\\\\\"\\\\n        metrics: {}\\\\n\\\\n      - title: \\\\\\\"Code Execution as Grounded Supervision for LLM Reasoning\\\\\\\"\\\\n        authors: \\\\\\\"Dongwon Jung, Wenxuan Zhou, Muhao Chen\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"EMNLP 2025\\\\\\\"\\\\n        role: method-component\\\\n        key_finding: \\\\\\\"用 Python debugger (Snoop) 提取 step-by-step execution trace，转换为自然语言 CoT。训练后模型推理能力提升且生成更少 token（减少 overthinking），具备跨域迁移能力。\\\\\\\"\\\\n        metrics: {}\\\\n\\\\n      - title: \\\\\\\"What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces\\\\\\\"\\\\n        authors: \\\\\\\"Lorenzo Ferrando, Nicola Ferraro, et al.\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"arXiv 2503.05703\\\\\\\"\\\\n        role: method-component\\\\n        key_finding: \\\\\\\"对比 regular/compact/dynamic 三种 scratchpad 策略，compact（仅记录变化变量）略优于 regular（全部变量值）。CruxEval/MBPP ~80%。直接支持 plan_001：完整值信息冗余，精简不损失效果。\\\\\\\"\\\\n        metrics:\\\\n          cruxeval_accuracy: \\\\\\\"~80%\\\\\\\"\\\\n          mbpp_accuracy: \\\\\\\"~80%\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Demystifying Errors in LLM Reasoning Traces: An Empirical Study of Code Execution Simulation\\\\\\\"\\\\n        authors: \\\\\\\"arXiv 2512.00215\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"arXiv\\\\\\\"\\\\n        role: evaluation\\\\n        key_finding: \\\\\\\"LLM 在循环中频繁遗漏/多算变量修改，函数返回值预测不准。说明 LLM 对具体值追踪能力弱于结构理解，为 plan_001 发现（值冗余）提供机制解释。\\\\\\\"\\\\n        metrics: {}\\\\n\\\\n      - title: \\\\\\\"Reasoning Runtime Behavior of a Program with LLM: How Far Are We? (REval)\\\\\\\"\\\\n        authors: \\\\\\\"Junkai Chen et al.\\\\\\\"\\\\n        year: 2024\\\\n        venue: \\\\\\\"arXiv 2403.16437\\\\\\\"\\\\n        role: evaluation\\\\n        key_finding: \\\\\\\"REval 框架评估 LLM 在 4 种 runtime behavior 预测任务上的表现：coverage prediction、program state prediction、execution path prediction、output prediction。平均 accuracy 仅 44.4%，IC score 10.3。揭示 LLM runtime reasoning 能力有限，支持 VOTA 的发现——需要抽象而非让 LLM 直接消化全量 trace。\\\\\\\"\\\\n        metrics:\\\\n          avg_accuracy: \\\\\\\"44.4%\\\\\\\"\\\\n          avg_ic_score: \\\\\\\"10.3\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"CodeMind: Evaluating Large Language Models for Code Reasoning\\\\\\\"\\\\n        authors: \\\\\\\"Changshu Liu et al. (UIUC)\\\\\\\"\\\\n        year: 2024\\\\n        venue: \\\\\\\"arXiv 2402.09664\\\\\\\"\\\\n        role: evaluation\\\\n        key_finding: \\\\\\\"评估 LLM 在 IER（执行推理）、SR（规格推理）、DSR（动态语义推理）三个维度的代码推理能力。性能随代码复杂度（控制流、非原始类型、API 调用）显著下降。支持 VOTA 的 trace abstraction 动机——复杂 trace 超出 LLM 推理能力。\\\\\\\"\\\\n        metrics: {}\\\\n\\\\n      - title: \\\\\\\"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\\\\\\\"\\\\n        authors: \\\\\\\"Ruiyang Xu et al. (HKUST)\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"ACL 2025\\\\\\\"\\\\n        role: evaluation\\\\n        key_finding: \\\\\\\"将 CRUXEval 扩展到 19 种编程语言，19K 测试。仅在 Python 训练的模型在其他语言最高 34.4% Pass@1，揭示 cross-language generalization 的局限。对 VOTA 的 cross-model generalization 实验提供方法论参考。\\\\\\\"\\\\n        metrics:\\\\n          languages: 19\\\\n          cross_lang_max_pass1: \\\\\\\"34.4%\\\\\\\"\\\\n\\\\n  code-verdict:\\\\n    description: \\\\\\\"LLM 判断代码 pass/fail、正确性分类、mutation testing\\\\\\\"\\\\n    papers:\\\\n      - title: \\\\\\\"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\\\\\\\"\\\\n        authors: \\\\\\\"iSEngLab (Nanjing University)\\\\\\\"\\\\n        year: 2024\\\\n        venue: \\\\\\\"IEEE TSE 2024\\\\\\\"\\\\n        role: direct-competitor\\\\n        key_finding: \\\\\\\"BERT + LSTM + classifier 微调做 patch 正确性二分类。在 1183 个 Defects4J patches 上 accuracy 79.7%、recall 83.2%，优于 CACHE。与 VOTA 的 verdict 分类目标最接近。\\\\\\\"\\\\n        metrics:\\\\n          accuracy: \\\\\\\"79.7%\\\\\\\"\\\\n          recall: \\\\\\\"83.2%\\\\\\\"\\\\n          f1_improvement_from_finetuning: \\\\\\\"+10.22%\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"LLM4PatchCorrect: Leveraging Large Language Model for Automatic Patch Correctness Assessment\\\\\\\"\\\\n        authors: \\\\\\\"Xin Zhou et al. (SMU)\\\\\\\"\\\\n        year: 2024\\\\n        venue: \\\\\\\"IEEE TSE 2024\\\\\\\"\\\\n        role: direct-competitor\\\\n        key_finding: \\\\\\\"用 Starcoder-7B 零样本评估 patch 正确性，输入包含 bug description、execution traces、failing test cases、test coverage。无需微调即达 84.4% accuracy。使用了 execution trace 作为输入信号，与 VOTA 输入空间有重叠，但方法（zero-shot prompting vs SFT）和任务（patch correctness vs test verdict）不同。\\\\\\\"\\\\n        metrics:\\\\n          accuracy: \\\\\\\"84.4%\\\\\\\"\\\\n          f1: \\\\\\\"86.5%\\\\\\\"\\\\n        novelty_threat: medium\\\\n\\\\n      - title: \\\\\\\"Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph for Automated Patch Correctness Assessment\\\\\\\"\\\\n        authors: \\\\\\\"arXiv 2505.02629\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"arXiv 2505.02629\\\\\\\"\\\\n        role: direct-competitor\\\\n        key_finding: \\\\\\\"提出 APSG（Attributed Patch Semantic Graph）+ Graph-LoRA，用图结构捕获 patch 语义的 data/control flow。在 patch correctness 上比 SOTA 提升 accuracy 3.1-7.5%、F1 3.0-7.1%。方法论（PEFT + 结构化代码表示做分类）与 VOTA 有相似之处，但 VOTA 用 trace signal 而非 graph。\\\\\\\"\\\\n        metrics:\\\\n          accuracy_improvement: \\\\\\\"+3.1-7.5%\\\\\\\"\\\\n          f1_improvement: \\\\\\\"+3.0-7.1%\\\\\\\"\\\\n        novelty_threat: medium\\\\n\\\\n      - title: \\\\\\\"Calibration and Correctness of Language Models for Code\\\\\\\"\\\\n        authors: \\\\\\\"Claudio Spiess, David Gros, et al.\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"ICSE 2025\\\\\\\"\\\\n        role: evaluation\\\\n        key_finding: \\\\\\\"代码生成模型的置信度校准普遍较差。Platt scaling 可改善但需要先验正确性数据。对 VOTA 的启示：verdict 分类需关注校准，不只是准确率。\\\\\\\"\\\\n        metrics: {}\\\\n\\\\n      - title: \\\\\\\"Mutation-Guided LLM-based Test Generation at Meta\\\\\\\"\\\\n        authors: \\\\\\\"Christopher Foster et al. (Meta)\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"FSE 2025 (Industry)\\\\\\\"\\\\n        role: evaluation\\\\n        key_finding: \\\\\\\"LLM equivalence detector 判断 mutant 是否等价，加简单预处理后 precision 0.95、recall 0.96。大规模部署到 10K+ 类，工程师接受率 73%。展示了 LLM 做代码正确性判断的工业可行性。\\\\\\\"\\\\n        metrics:\\\\n          precision: \\\\\\\"0.95\\\\\\\"\\\\n          recall: \\\\\\\"0.96\\\\\\\"\\\\n          classes_evaluated: \\\\\\\"10795\\\\\\\"\\\\n          test_acceptance_rate: \\\\\\\"73%\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"FuseFL: Demystifying Faulty Code with LLM via Step-by-Step Reasoning\\\\\\\"\\\\n        authors: \\\\\\\"Ratnadira Widyasari et al. (SMU)\\\\\\\"\\\\n        year: 2024\\\\n        venue: \\\\\\\"SANER 2024\\\\\\\"\\\\n        role: background\\\\n        key_finding: \\\\\\\"融合 SBFL 排名 + test execution outcomes（input、expected/actual output、errors）+ code description 做 fault localization。Top-1 localization 比 baseline 提升 32.3%，比 SBFL 提升 68.4%。test execution outcomes 作为输入信号与 VOTA 的 fault indicator signals 理念相关。\\\\\\\"\\\\n        metrics:\\\\n          top1_improvement_over_baseline: \\\\\\\"+32.3%\\\\\\\"\\\\n          top1_improvement_over_sbfl: \\\\\\\"+68.4%\\\\\\\"\\\\n\\\\n  trace-compression:\\\\n    description: \\\\\\\"Execution trace 的压缩、摘要、抽象方法\\\\\\\"\\\\n    papers:\\\\n      - title: \\\\\\\"Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning\\\\\\\"\\\\n        authors: \\\\\\\"Aashish Yadavally, Yi Li, Tien Nguyen\\\\\\\"\\\\n        year: 2024\\\\n        venue: \\\\\\\"FSE 2024\\\\\\\"\\\\n        role: method-component\\\\n        key_finding: \\\\\\\"ND-Slicer 用 execution-aware 预训练学习动态依赖，无需实际执行即可预测特定输入的程序切片。Python 上 exact-match 81.31%、ROUGE-LCS 0.954。与 VOTA 的 assertion-point snapshots 思路类似——都是从完整 trace 中提取关键信息。\\\\\\\"\\\\n        metrics:\\\\n          exact_match: \\\\\\\"81.31%\\\\\\\"\\\\n          rouge_lcs: \\\\\\\"0.954\\\\\\\"\\\\n          fault_localization_accuracy: \\\\\\\"63.88%\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\\\\\\\"\\\\n        authors: \\\\\\\"Mirazul Haque, Petr Babkin, et al. (J.P. Morgan AI Research)\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"KnowledgeNLP Workshop @ ACL 2025\\\\\\\"\\\\n        role: background\\\\n        key_finding: \\\\\\\"直接将 execution trace 加入 prompt 帮助有限，且随 trace 复杂度增加效果递减。LLM 优化的 prompt 格式比原始 trace 更一致地优于无 trace baseline。直接支持 VOTA 的核心假设：原始 trace 太冗长，需要专门的压缩/抽象。\\\\\\\"\\\\n        metrics: {}\\\\n\\\\n      - title: \\\\\\\"Making LLMs Program Interpreters via Execution Trace Chain of Thought (ET-CoT)\\\\\\\"\\\\n        authors: \\\\\\\"ICML 2025 Workshop PRAL\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"ICML 2025 Workshop\\\\\\\"\\\\n        role: method-component\\\\n        key_finding: \\\\\\\"开发 PyTracify 工具生成 sub-line 粒度的结构化 execution trace，SFT 后 Qwen2.5-7B 在 CRUXEval-O 达 70.0%、LiveCodeBench 达 88.3%，超过同规模 code-oriented 模型。其 trace 格式本身是一种 trace abstraction。\\\\\\\"\\\\n        metrics:\\\\n          cruxeval_o: \\\\\\\"70.0%\\\\\\\"\\\\n          livecodebench_execution: \\\\\\\"88.3%\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\\\\\\\"\\\\n        authors: \\\\\\\"ICSE 2026 Research Track\\\\\\\"\\\\n        year: 2026\\\\n        venue: \\\\\\\"ICSE 2026\\\\\\\"\\\\n        role: background\\\\n        key_finding: \\\\\\\"在特定位置插入 diagnostic probes 而非全量 trace 记录，Pass@1 提升 34.43%。选择性 trace 采集优于全量，支持 VOTA 的行为模式抽象思路。\\\\\\\"\\\\n        metrics:\\\\n          pass_at_1_improvement: \\\\\\\"+34.43%\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate\\\\\\\"\\\\n        authors: \\\\\\\"Jiaqing Wu et al.\\\\\\\"\\\\n        year: 2026\\\\n        venue: \\\\\\\"arXiv 2604.02647\\\\\\\"\\\\n        role: background\\\\n        key_finding: \\\\\\\"Probe agent 选择性捕获 critical variables 的 execution snapshots 用于 multi-agent repair debate，修复 392 个缺陷。验证了选择性 trace 信息优于全量记录。\\\\\\\"\\\\n        metrics:\\\\n          defects_fixed: \\\\\\\"392\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration\\\\\\\"\\\\n        authors: \\\\\\\"arXiv 2510.18327\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"arXiv 2510.18327\\\\\\\"\\\\n        role: background\\\\n        key_finding: \\\\\\\"首个让 LLM 主动控制 debugger 做动态分析的 agentic repair 系统。Program Inspector 做策略性 breakpoint 放置和 runtime state 检查，Patch Coder 合成修复。比最强 baseline 提升 5.10-60.37%。选择性 runtime 检查理念与 VOTA 的 fault indicator signal 提取一致。\\\\\\\"\\\\n        metrics:\\\\n          repair_accuracy_improvement: \\\\\\\"+5.10-60.37%\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"MGDebugger: From Code to Correctness via Hierarchical Debugging\\\\\\\"\\\\n        authors: \\\\\\\"Yuling Shi et al.\\\\\\\"\\\\n        year: 2024\\\\n        venue: \\\\\\\"arXiv 2410.01215\\\\\\\"\\\\n        role: background\\\\n        key_finding: \\\\\\\"层次化分解代码为子函数树，LLM 模拟执行追踪关键变量状态，bottom-up 定位修复。HumanEval accuracy 75.6%→94.5%。其 LLM-simulated executor 追踪变量状态的方式是一种隐式 trace abstraction。\\\\\\\"\\\\n        metrics:\\\\n          humaneval_accuracy: \\\\\\\"94.5%\\\\\\\"\\\\n          humaneval_fix_accuracy: \\\\\\\"97.6%\\\\\\\"\\\\n\\\\n  debugging-agents:\\\\n    description: \\\\\\\"LLM 多智能体调试框架\\\\\\\"\\\\n    papers:\\\\n      - title: \\\\\\\"UniDebugger: Hierarchical Multi-Agent Framework for Unified Software Debugging\\\\\\\"\\\\n        authors: \\\\\\\"Cheryl Lee, Chunqiu Steven Xia, et al. (Lingming Zhang group)\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"EMNLP 2025\\\\\\\"\\\\n        role: background\\\\n        key_finding: \\\\\\\"三层认知架构模拟开发者调试过程，L1→L2→L3 逐层升级。在 Defects4J 上修复 1.25-2.56x bugs。不使用 execution trace 作为输入（纯静态分析），与 VOTA 方法正交。\\\\\\\"\\\\n        metrics:\\\\n          defects4j_improvement: \\\\\\\"1.25-2.56x\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Seeker: Enhancing Exception Handling in Code with LLM-based Multi-Agent Approach\\\\\\\"\\\\n        authors: \\\\\\\"Xuanming Zhang et al.\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"ICLR 2025\\\\\\\"\\\\n        role: background\\\\n        key_finding: \\\\\\\"5-agent 框架做 exception handling 生成，构建 Common Exception Enumeration (CEE) 知识库。Exception handling precision 提升 37%。从 exception taxonomy 角度提供背景——exception 类型和处理策略的系统化，与 VOTA 的 exception event 信号提取视角互补。\\\\\\\"\\\\n        metrics:\\\\n          exception_handling_precision_improvement: \\\\\\\"+37%\\\\\\\"\\\\n\\\\n  sft-classification:\\\\n    description: \\\\\\\"用 SFT 做分类任务的方法论和 findings\\\\\\\"\\\\n    papers:\\\\n      - title: \\\\\\\"Fine-Tuning Causal LLMs for Text Classification: Embedding-Based vs. Instruction-Based Approaches\\\\\\\"\\\\n        authors: \\\\\\\"Amirhossein Yousefiramandi, Ciaran Cooney\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"arXiv 2512.12677\\\\\\\"\\\\n        role: method-component\\\\n        key_finding: \\\\\\\"对比 embedding-based（加分类头）vs instruction-based（prompt->response）两种 SFT 分类方式。Embedding-based + QLoRA 在 F1 上与 instruction-tuned 持平，但可训练参数少得多。对 VOTA 的 verdict 分类有直接参考价值——选哪种 SFT 格式。\\\\\\\"\\\\n        metrics: {}\\\\n\\\\n      - title: \\\\\\\"FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain\\\\\\\"\\\\n        authors: \\\\\\\"Rohan Deb, Kiran Koshy Thekumparampil, et al.\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"ICML 2025\\\\\\\"\\\\n        role: background\\\\n        key_finding: \\\\\\\"用 Fisher 信息矩阵选择信息量最大的训练样本子集，通过 last-layer 线性化高效近似。在固定数据预算下提升 SFT 效果。对 VOTA 的数据选择策略有参考价值。\\\\\\\"\\\\n        metrics: {}\\\\n\\\\n      - title: \\\\\\\"Fine-Tuned 'Small' LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification\\\\\\\"\\\\n        authors: \\\\\\\"Martin Juan Jose Bucher, Marco Martini\\\\\\\"\\\\n        year: 2024\\\\n        venue: \\\\\\\"arXiv 2406.08660\\\\\\\"\\\\n        role: background\\\\n        key_finding: \\\\\\\"跨多种分类任务（情感、立场、情绪等），fine-tuned 小模型全面优于 GPT-4/Claude 的 zero-shot。验证了 VOTA 用 SFT 做 verdict 分类的基本假设——fine-tuning 在分类上优于 prompting。\\\\\\\"\\\\n        metrics: {}\\\\n\\\\nmeta:\\\\n  last_updated: \\\\\\\"2026-05-15\\\\\\\"\\\\n  total_papers: 26\\\\n  search_scope: \\\\\\\"2024-2026, top ML/NLP/SE venues\\\\\\\"\\\\n  scan_date: \\\\\\\"2026-05-15\\\\\\\"\\\\n  scan_queries: 16\\\\n  key_gaps:\\\\n    - \\\\\\\"缺少直接将 execution trace 用于 binary verdict (pass/fail) 的工作——VOTA 填补此空白\\\\\\\"\\\\n    - \\\\\\\"trace compression 文献多在 distributed systems 或 formal verification 领域，code-level trace 压缩给 LLM 用的工作极少\\\\\\\"\\\\n    - \\\\\\\"SFT for classification 研究多在 NLP 文本分类，code verdict 场景的 SFT 方法论研究接近空白\\\\\\\"\\\\n    - \\\\\\\"patch correctness prediction（LLM4PatchCorrect、APSG）是最近的竞争方向，但任务定义和输入信号与 VOTA 有本质区别\\\\\\\"\\\\n    - \\\\\\\"selective trace（InspectCoder、TraceCoder）趋势明显，但均用于 program repair 而非 verdict classification\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 13257, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/literature_map.yaml\", \"content\": \"categories:\\n  execution-trace-llm:\\n    description: \\\"Execution trace 辅助 LLM 代码理解/调试/推理\\\"\\n    papers:\\n      - title: \\\"NExT: Teaching Large Language Models to Reason about Code Execution\\\"\\n        authors: \\\"Ansong Ni, Miltiadis Allamanis, et al. (Google DeepMind)\\\"\\n        year: 2024\\n        venue: \\\"ICML 2024\\\"\\n        role: method-component\\n        key_finding: \\\"自训练在 execution trace 上做 CoT rationale，程序修复 fix rate 在 MBPP +26.1%、HumanEval +14.3%。模型可泛化到无 trace 的场景。\\\"\\n        metrics:\\n          mbpp_fix_rate_improvement: \\\"+26.1%\\\"\\n          humaneval_fix_rate_improvement: \\\"+14.3%\\\"\\n\\n      - title: \\\"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code LLMs\\\"\\n        authors: \\\"Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li\\\"\\n        year: 2025\\n        venue: \\\"Findings of EMNLP 2025\\\"\\n        role: direct-competitor\\n        key_finding: \\\"综合研究发现 execution trace 对 SFT 和 test-time scaling 的帮助有限，与先前工作结论相左。提出 trace adapter 做格式化。这是 VOTA 必须回应的关键负面结果——说明原始 trace 不够，需要针对性压缩/抽象。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Code Execution as Grounded Supervision for LLM Reasoning\\\"\\n        authors: \\\"Dongwon Jung, Wenxuan Zhou, Muhao Chen\\\"\\n        year: 2025\\n        venue: \\\"EMNLP 2025\\\"\\n        role: method-component\\n        key_finding: \\\"用 Python debugger (Snoop) 提取 step-by-step execution trace，转换为自然语言 CoT。训练后模型推理能力提升且生成更少 token（减少 overthinking），具备跨域迁移能力。\\\"\\n        metrics: {}\\n\\n      - title: \\\"What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces\\\"\\n        authors: \\\"Lorenzo Ferrando, Nicola Ferraro, et al.\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2503.05703\\\"\\n        role: method-component\\n        key_finding: \\\"对比 regular/compact/dynamic 三种 scratchpad 策略，compact（仅记录变化变量）略优于 regular（全部变量值）。CruxEval/MBPP ~80%。直接支持 plan_001：完整值信息冗余，精简不损失效果。\\\"\\n        metrics:\\n          cruxeval_accuracy: \\\"~80%\\\"\\n          mbpp_accuracy: \\\"~80%\\\"\\n\\n      - title: \\\"Demystifying Errors in LLM Reasoning Traces: An Empirical Study of Code Execution Simulation\\\"\\n        authors: \\\"arXiv 2512.00215\\\"\\n        year: 2025\\n        venue: \\\"arXiv\\\"\\n        role: evaluation\\n        key_finding: \\\"LLM 在循环中频繁遗漏/多算变量修改，函数返回值预测不准。说明 LLM 对具体值追踪能力弱于结构理解，为 plan_001 发现（值冗余）提供机制解释。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Reasoning Runtime Behavior of a Program with LLM: How Far Are We? (REval)\\\"\\n        authors: \\\"Junkai Chen et al.\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2403.16437\\\"\\n        role: evaluation\\n        key_finding: \\\"REval 框架评估 LLM 在 4 种 runtime behavior 预测任务上的表现：coverage prediction、program state prediction、execution path prediction、output prediction。平均 accuracy 仅 44.4%，IC score 10.3。揭示 LLM runtime reasoning 能力有限，支持 VOTA 的发现——需要抽象而非让 LLM 直接消化全量 trace。\\\"\\n        metrics:\\n          avg_accuracy: \\\"44.4%\\\"\\n          avg_ic_score: \\\"10.3\\\"\\n\\n      - title: \\\"CodeMind: Evaluating Large Language Models for Code Reasoning\\\"\\n        authors: \\\"Changshu Liu et al. (UIUC)\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2402.09664\\\"\\n        role: evaluation\\n        key_finding: \\\"评估 LLM 在 IER（执行推理）、SR（规格推理）、DSR（动态语义推理）三个维度的代码推理能力。性能随代码复杂度（控制流、非原始类型、API 调用）显著下降。支持 VOTA 的 trace abstraction 动机——复杂 trace 超出 LLM 推理能力。\\\"\\n        metrics: {}\\n\\n      - title: \\\"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\\\"\\n        authors: \\\"Ruiyang Xu et al. (HKUST)\\\"\\n        year: 2025\\n        venue: \\\"ACL 2025\\\"\\n        role: evaluation\\n        key_finding: \\\"将 CRUXEval 扩展到 19 种编程语言，19K 测试。仅在 Python 训练的模型在其他语言最高 34.4% Pass@1，揭示 cross-language generalization 的局限。对 VOTA 的 cross-model generalization 实验提供方法论参考。\\\"\\n        metrics:\\n          languages: 19\\n          cross_lang_max_pass1: \\\"34.4%\\\"\\n\\n  code-verdict:\\n    description: \\\"LLM 判断代码 pass/fail、正确性分类、mutation testing\\\"\\n    papers:\\n      - title: \\\"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\\\"\\n        authors: \\\"iSEngLab (Nanjing University)\\\"\\n        year: 2024\\n        venue: \\\"IEEE TSE 2024\\\"\\n        role: direct-competitor\\n        key_finding: \\\"BERT + LSTM + classifier 微调做 patch 正确性二分类。在 1183 个 Defects4J patches 上 accuracy 79.7%、recall 83.2%，优于 CACHE。与 VOTA 的 verdict 分类目标最接近。\\\"\\n        metrics:\\n          accuracy: \\\"79.7%\\\"\\n          recall: \\\"83.2%\\\"\\n          f1_improvement_from_finetuning: \\\"+10.22%\\\"\\n\\n      - title: \\\"LLM4PatchCorrect: Leveraging Large Language Model for Automatic Patch Correctness Assessment\\\"\\n        authors: \\\"Xin Zhou et al. (SMU)\\\"\\n        year: 2024\\n        venue: \\\"IEEE TSE 2024\\\"\\n        role: direct-competitor\\n        key_finding: \\\"用 Starcoder-7B 零样本评估 patch 正确性，输入包含 bug description、execution traces、failing test cases、test coverage。无需微调即达 84.4% accuracy。使用了 execution trace 作为输入信号，与 VOTA 输入空间有重叠，但方法（zero-shot prompting vs SFT）和任务（patch correctness vs test verdict）不同。\\\"\\n        metrics:\\n          accuracy: \\\"84.4%\\\"\\n          f1: \\\"86.5%\\\"\\n        novelty_threat: medium\\n\\n      - title: \\\"Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph for Automated Patch Correctness Assessment\\\"\\n        authors: \\\"arXiv 2505.02629\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2505.02629\\\"\\n        role: direct-competitor\\n        key_finding: \\\"提出 APSG（Attributed Patch Semantic Graph）+ Graph-LoRA，用图结构捕获 patch 语义的 data/control flow。在 patch correctness 上比 SOTA 提升 accuracy 3.1-7.5%、F1 3.0-7.1%。方法论（PEFT + 结构化代码表示做分类）与 VOTA 有相似之处，但 VOTA 用 trace signal 而非 graph。\\\"\\n        metrics:\\n          accuracy_improvement: \\\"+3.1-7.5%\\\"\\n          f1_improvement: \\\"+3.0-7.1%\\\"\\n        novelty_threat: medium\\n\\n      - title: \\\"Calibration and Correctness of Language Models for Code\\\"\\n        authors: \\\"Claudio Spiess, David Gros, et al.\\\"\\n        year: 2025\\n        venue: \\\"ICSE 2025\\\"\\n        role: evaluation\\n        key_finding: \\\"代码生成模型的置信度校准普遍较差。Platt scaling 可改善但需要先验正确性数据。对 VOTA 的启示：verdict 分类需关注校准，不只是准确率。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Mutation-Guided LLM-based Test Generation at Meta\\\"\\n        authors: \\\"Christopher Foster et al. (Meta)\\\"\\n        year: 2025\\n        venue: \\\"FSE 2025 (Industry)\\\"\\n        role: evaluation\\n        key_finding: \\\"LLM equivalence detector 判断 mutant 是否等价，加简单预处理后 precision 0.95、recall 0.96。大规模部署到 10K+ 类，工程师接受率 73%。展示了 LLM 做代码正确性判断的工业可行性。\\\"\\n        metrics:\\n          precision: \\\"0.95\\\"\\n          recall: \\\"0.96\\\"\\n          classes_evaluated: \\\"10795\\\"\\n          test_acceptance_rate: \\\"73%\\\"\\n\\n      - title: \\\"FuseFL: Demystifying Faulty Code with LLM via Step-by-Step Reasoning\\\"\\n        authors: \\\"Ratnadira Widyasari et al. (SMU)\\\"\\n        year: 2024\\n        venue: \\\"SANER 2024\\\"\\n        role: background\\n        key_finding: \\\"融合 SBFL 排名 + test execution outcomes（input、expected/actual output、errors）+ code description 做 fault localization。Top-1 localization 比 baseline 提升 32.3%，比 SBFL 提升 68.4%。test execution outcomes 作为输入信号与 VOTA 的 fault indicator signals 理念相关。\\\"\\n        metrics:\\n          top1_improvement_over_baseline: \\\"+32.3%\\\"\\n          top1_improvement_over_sbfl: \\\"+68.4%\\\"\\n\\n  trace-compression:\\n    description: \\\"Execution trace 的压缩、摘要、抽象方法\\\"\\n    papers:\\n      - title: \\\"Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning\\\"\\n        authors: \\\"Aashish Yadavally, Yi Li, Tien Nguyen\\\"\\n        year: 2024\\n        venue: \\\"FSE 2024\\\"\\n        role: method-component\\n        key_finding: \\\"ND-Slicer 用 execution-aware 预训练学习动态依赖，无需实际执行即可预测特定输入的程序切片。Python 上 exact-match 81.31%、ROUGE-LCS 0.954。与 VOTA 的 assertion-point snapshots 思路类似——都是从完整 trace 中提取关键信息。\\\"\\n        metrics:\\n          exact_match: \\\"81.31%\\\"\\n          rouge_lcs: \\\"0.954\\\"\\n          fault_localization_accuracy: \\\"63.88%\\\"\\n\\n      - title: \\\"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\\\"\\n        authors: \\\"Mirazul Haque, Petr Babkin, et al. (J.P. Morgan AI Research)\\\"\\n        year: 2025\\n        venue: \\\"KnowledgeNLP Workshop @ ACL 2025\\\"\\n        role: background\\n        key_finding: \\\"直接将 execution trace 加入 prompt 帮助有限，且随 trace 复杂度增加效果递减。LLM 优化的 prompt 格式比原始 trace 更一致地优于无 trace baseline。直接支持 VOTA 的核心假设：原始 trace 太冗长，需要专门的压缩/抽象。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Making LLMs Program Interpreters via Execution Trace Chain of Thought (ET-CoT)\\\"\\n        authors: \\\"ICML 2025 Workshop PRAL\\\"\\n        year: 2025\\n        venue: \\\"ICML 2025 Workshop\\\"\\n        role: method-component\\n        key_finding: \\\"开发 PyTracify 工具生成 sub-line 粒度的结构化 execution trace，SFT 后 Qwen2.5-7B 在 CRUXEval-O 达 70.0%、LiveCodeBench 达 88.3%，超过同规模 code-oriented 模型。其 trace 格式本身是一种 trace abstraction。\\\"\\n        metrics:\\n          cruxeval_o: \\\"70.0%\\\"\\n          livecodebench_execution: \\\"88.3%\\\"\\n\\n      - title: \\\"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\\\"\\n        authors: \\\"ICSE 2026 Research Track\\\"\\n        year: 2026\\n        venue: \\\"ICSE 2026\\\"\\n        role: background\\n        key_finding: \\\"在特定位置插入 diagnostic probes 而非全量 trace 记录，Pass@1 提升 34.43%。选择性 trace 采集优于全量，支持 VOTA 的行为模式抽象思路。\\\"\\n        metrics:\\n          pass_at_1_improvement: \\\"+34.43%\\\"\\n\\n      - title: \\\"Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate\\\"\\n        authors: \\\"Jiaqing Wu et al.\\\"\\n        year: 2026\\n        venue: \\\"arXiv 2604.02647\\\"\\n        role: background\\n        key_finding: \\\"Probe agent 选择性捕获 critical variables 的 execution snapshots 用于 multi-agent repair debate，修复 392 个缺陷。验证了选择性 trace 信息优于全量记录。\\\"\\n        metrics:\\n          defects_fixed: \\\"392\\\"\\n\\n      - title: \\\"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration\\\"\\n        authors: \\\"arXiv 2510.18327\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2510.18327\\\"\\n        role: background\\n        key_finding: \\\"首个让 LLM 主动控制 debugger 做动态分析的 agentic repair 系统。Program Inspector 做策略性 breakpoint 放置和 runtime state 检查，Patch Coder 合成修复。比最强 baseline 提升 5.10-60.37%。选择性 runtime 检查理念与 VOTA 的 fault indicator signal 提取一致。\\\"\\n        metrics:\\n          repair_accuracy_improvement: \\\"+5.10-60.37%\\\"\\n\\n      - title: \\\"MGDebugger: From Code to Correctness via Hierarchical Debugging\\\"\\n        authors: \\\"Yuling Shi et al.\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2410.01215\\\"\\n        role: background\\n        key_finding: \\\"层次化分解代码为子函数树，LLM 模拟执行追踪关键变量状态，bottom-up 定位修复。HumanEval accuracy 75.6%→94.5%。其 LLM-simulated executor 追踪变量状态的方式是一种隐式 trace abstraction。\\\"\\n        metrics:\\n          humaneval_accuracy: \\\"94.5%\\\"\\n          humaneval_fix_accuracy: \\\"97.6%\\\"\\n\\n  debugging-agents:\\n    description: \\\"LLM 多智能体调试框架\\\"\\n    papers:\\n      - title: \\\"UniDebugger: Hierarchical Multi-Agent Framework for Unified Software Debugging\\\"\\n        authors: \\\"Cheryl Lee, Chunqiu Steven Xia, et al. (Lingming Zhang group)\\\"\\n        year: 2025\\n        venue: \\\"EMNLP 2025\\\"\\n        role: background\\n        key_finding: \\\"三层认知架构模拟开发者调试过程，L1→L2→L3 逐层升级。在 Defects4J 上修复 1.25-2.56x bugs。不使用 execution trace 作为输入（纯静态分析），与 VOTA 方法正交。\\\"\\n        metrics:\\n          defects4j_improvement: \\\"1.25-2.56x\\\"\\n\\n      - title: \\\"Seeker: Enhancing Exception Handling in Code with LLM-based Multi-Agent Approach\\\"\\n        authors: \\\"Xuanming Zhang et al.\\\"\\n        year: 2025\\n        venue: \\\"ICLR 2025\\\"\\n        role: background\\n        key_finding: \\\"5-agent 框架做 exception handling 生成，构建 Common Exception Enumeration (CEE) 知识库。Exception handling precision 提升 37%。从 exception taxonomy 角度提供背景——exception 类型和处理策略的系统化，与 VOTA 的 exception event 信号提取视角互补。\\\"\\n        metrics:\\n          exception_handling_precision_improvement: \\\"+37%\\\"\\n\\n  sft-classification:\\n    description: \\\"用 SFT 做分类任务的方法论和 findings\\\"\\n    papers:\\n      - title: \\\"Fine-Tuning Causal LLMs for Text Classification: Embedding-Based vs. Instruction-Based Approaches\\\"\\n        authors: \\\"Amirhossein Yousefiramandi, Ciaran Cooney\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2512.12677\\\"\\n        role: method-component\\n        key_finding: \\\"对比 embedding-based（加分类头）vs instruction-based（prompt->response）两种 SFT 分类方式。Embedding-based + QLoRA 在 F1 上与 instruction-tuned 持平，但可训练参数少得多。对 VOTA 的 verdict 分类有直接参考价值——选哪种 SFT 格式。\\\"\\n        metrics: {}\\n\\n      - title: \\\"FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain\\\"\\n        authors: \\\"Rohan Deb, Kiran Koshy Thekumparampil, et al.\\\"\\n        year: 2025\\n        venue: \\\"ICML 2025\\\"\\n        role: background\\n        key_finding: \\\"用 Fisher 信息矩阵选择信息量最大的训练样本子集，通过 last-layer 线性化高效近似。在固定数据预算下提升 SFT 效果。对 VOTA 的数据选择策略有参考价值。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Fine-Tuned 'Small' LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification\\\"\\n        authors: \\\"Martin Juan Jose Bucher, Marco Martini\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2406.08660\\\"\\n        role: background\\n        key_finding: \\\"跨多种分类任务（情感、立场、情绪等），fine-tuned 小模型全面优于 GPT-4/Claude 的 zero-shot。验证了 VOTA 用 SFT 做 verdict 分类的基本假设——fine-tuning 在分类上优于 prompting。\\\"\\n        metrics: {}\\n\\nmeta:\\n  last_updated: \\\"2026-05-15\\\"\\n  total_papers: 26\\n  search_scope: \\\"2024-2026, top ML/NLP/SE venues\\\"\\n  scan_date: \\\"2026-05-15\\\"\\n  scan_queries: 16\\n  key_gaps:\\n    - \\\"缺少直接将 execution trace 用于 binary verdict (pass/fail) 的工作——VOTA 填补此空白\\\"\\n    - \\\"trace compression 文献多在 distributed systems 或 formal verification 领域，code-level trace 压缩给 LLM 用的工作极少\\\"\\n    - \\\"SFT for classification 研究多在 NLP 文本分类，code verdict 场景的 SFT 方法论研究接近空白\\\"\\n    - \\\"patch correctness prediction（LLM4PatchCorrect、APSG）是最近的竞争方向，但任务定义和输入信号与 VOTA 有本质区别\\\"\\n    - \\\"selective trace（InspectCoder、TraceCoder）趋势明显，但均用于 program repair 而非 verdict classification\\\"\\n\", \"total_chars\": 13257, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Glob · `toolu_01PpikTyZCxYezJjZ9Kcf23e`</summary>

```json
{
  "pattern": "**/scan_report*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "79a95af2-31bf-473e-96ce-f447a6ada4b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QnsKSTDjFQCCXUBtMuTgbA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 724,
      "cache_read_input_tokens": 23254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 724
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T13:43:05.021Z_

<details><summary>↩ Tool result · `toolu_01PpikTyZCxYezJjZ9Kcf23e`</summary>

```text
artifacts/_project/report/scan_report.md
artifacts/literature_scan_20260515/scan_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "c930657c-df85-4e3d-8b30-038e0442ed27",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/report/scan_report.md",
      "artifacts/literature_scan_20260515/scan_report.md"
    ],
    "durationMs": 12,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Found scan_report.md in two locations. Let me read both to see which is the current version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "b8998ff6-595f-40cf-8674-f2c6b63ef314",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mg7ZcVSaRGfDj2vgHVhzmb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7724,
      "cache_read_input_tokens": 23978,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7724
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 15_

Found scan_report.md in two locations. Let me read both.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "e2b4fc21-4186-44a3-b2e4-887378cc9e3c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mg7ZcVSaRGfDj2vgHVhzmb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7724,
      "cache_read_input_tokens": 23978,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7724
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01Pu9rjr3zy1T2B5Rq3kQLfU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/report/scan_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "98b57185-c615-4e19-a58e-3f754c7844cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mg7ZcVSaRGfDj2vgHVhzmb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7724,
      "cache_read_input_tokens": 23978,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7724
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T13:43:11.195Z_

<details><summary>↩ Tool result · `toolu_01Pu9rjr3zy1T2B5Rq3kQLfU`</summary>

```text
1	# Literature Scan Report — VOTA (Verdict-Oriented Trace Abstraction)
2	
3	**Date**: 2026-05-15  
4	**Target**: EMNLP 2026 Main (ARR May 25 deadline)  
5	**Queries executed**: 16 search groups across arXiv, ACL Anthology, Semantic Scholar, IEEE Xplore  
6	
7	## Summary
8	
9	No **high-threat** direct competitor found. VOTA's core contribution — using fault indicator signals (exception events + assertion comparison points) from execution traces for binary verdict prediction via SFT — remains novel. The closest related works are in **patch correctness prediction**, which overlaps on input signals but differs fundamentally in task definition.
10	
11	---
12	
13	## New Papers Found (10 additions, 16→26 total)
14	
15	### MEDIUM Threat — Patch Correctness Prediction (Closest Competitors)
16	
17	| # | Paper | Venue | Threat | Relation to VOTA |
18	|---|-------|-------|--------|-----------------|
19	| 1 | **LLM4PatchCorrect** (Xin Zhou et al.) | TSE 2024 | **MEDIUM** | Uses execution traces + test cases as input for patch correctness assessment. Key difference: zero-shot prompting (no SFT), task is patch correctness (not test verdict), no trace compression. |
20	| 2 | **APSG + Graph-LoRA** (arXiv 2505.02629) | arXiv 2025 | **MEDIUM** | PEFT for patch correctness with graph-structured code representation. Key difference: uses static code graph (not runtime trace), no fault indicator signals. |
21	
22	**Differentiation from VOTA**:
23	- **Task**: Patch correctness (is this fix correct?) vs. VOTA's verdict prediction (does this test pass/fail?)
24	- **Input**: LLM4PatchCorrect uses raw traces + test info; VOTA uses decision-relevant compressed signals
25	- **Method**: LLM4PatchCorrect = zero-shot prompting; APSG = graph-LoRA; VOTA = SFT with trace abstraction
26	- **Core finding**: Neither identifies fault indicator signals as near-perfect discriminative features (99.83%)
27	
28	### LOW Threat — Supporting Evidence & Background
29	
30	| # | Paper | Venue | Category | Why Relevant |
31	|---|-------|-------|----------|-------------|
32	| 3 | **FuseFL** (Widyasari et al.) | SANER 2024 | code-verdict | Uses test execution outcomes (expected/actual output, errors) for fault localization. Validates that test outcome signals carry discriminative value — same intuition as VOTA, different task. |
33	| 4 | **REval** (Junkai Chen et al.) | arXiv 2403.16437 | evaluation | LLM runtime behavior prediction: avg accuracy 44.4%. Directly supports VOTA's argument that LLMs struggle with raw trace reasoning. |
34	| 5 | **CodeMind** (Changshu Liu et al.) | arXiv 2402.09664 | evaluation | Code reasoning drops with complexity (control flow, API calls). Supports trace abstraction motivation. |
35	| 6 | **CRUXEval-X** (Ruiyang Xu et al.) | ACL 2025 | evaluation | Multilingual CRUXEval (19 langs). Cross-language generalization reference for VOTA's cross-model experiments. |
36	| 7 | **InspectCoder** (arXiv 2510.18327) | arXiv 2025 | trace-compression | Strategic breakpoint placement + runtime state inspection for repair. Selective inspection philosophy aligns with VOTA's fault indicator extraction. |
37	| 8 | **MGDebugger** (Yuling Shi et al.) | arXiv 2410.01215 | trace-compression | Hierarchical debugging with LLM-simulated execution tracking key variables. Implicit trace abstraction. |
38	| 9 | **UniDebugger** (Cheryl Lee et al.) | EMNLP 2025 | debugging-agents | Multi-agent debugging without execution traces (static analysis). Orthogonal to VOTA. |
39	| 10 | **Seeker** (Xuanming Zhang et al.) | ICLR 2025 | debugging-agents | Exception handling with CEE knowledge base. Exception taxonomy provides complementary perspective to VOTA's exception event signals. |
40	
41	---
42	
43	## Threat Analysis
44	
45	### No HIGH Threat Competitors
46	
47	After 16 search queries, **no paper was found that**:
48	1. Uses execution trace fault indicator signals (exceptions + assertion comparisons) specifically for verdict prediction
49	2. Demonstrates that these signals alone achieve near-perfect accuracy
50	3. Proposes decision-relevant trace compression for binary classification via SFT
51	
52	### MEDIUM Threats — How to Differentiate
53	
54	**vs. LLM4PatchCorrect**: Cite as evidence that execution traces contain useful signals for code correctness tasks. Differentiate on: (a) VOTA identifies *which parts* of the trace matter (fault indicators), while LLM4PatchCorrect uses raw traces; (b) SFT vs. zero-shot; (c) different task granularity.
55	
56	**vs. APSG + Graph-LoRA**: Cite as concurrent work on PEFT for code correctness. Differentiate on: (a) runtime signal vs. static graph; (b) VOTA's discovery that 2 signal types suffice, vs. APSG's complex graph construction.
57	
58	### Emerging Trend: Selective Trace
59	
60	Multiple 2025-2026 papers (InspectCoder, TraceCoder, Runtime Traces + Multi-Agent Debate) converge on the same insight: **selective trace information > full trace**. VOTA should position itself within this trend while emphasizing its unique angle — the selection criterion is *decision-relevance for verdict prediction*, not general debugging utility.
61	
62	---
63	
64	## Recommended Citations to Add
65	
66	Papers that should be cited in the VOTA paper (if not already):
67	
68	1. **LLM4PatchCorrect** (TSE 2024) — closest work using execution traces for correctness assessment
69	2. **REval** (2024) — empirical evidence LLMs struggle with runtime reasoning (avg 44.4%)
70	3. **CodeMind** (2024) — code reasoning evaluation showing complexity-dependent degradation
71	4. **FuseFL** (SANER 2024) — validates test execution outcomes as discriminative signals
72	5. **CRUXEval-X** (ACL 2025) — cross-language generalization methodology reference
73	6. **InspectCoder** (2025) — selective runtime inspection trend
74	
75	---
76	
77	## Key Gaps Confirmed
78	
79	1. **No work directly applies execution trace to binary verdict (pass/fail) prediction** — VOTA fills this gap
80	2. **No work identifies fault indicator signals as near-perfect discriminative features** — VOTA's core empirical finding
81	3. **Decision-relevant trace compression for LLM classification is unexplored** — VOTA's methodological contribution
82	4. **Cross-model generalization of trace-based verdict prediction is unstudied** — VOTA addresses this
83	
84	---
85	
86	## Search Methodology
87	
88	16 query groups covering:
89	- "execution trace" + "fault detection" / "verdict prediction" / "test prediction"
90	- "trace compression" + "code understanding" / "debugging"
91	- "exception signal" + "fault localization"
92	- "VOTA" / "trace abstraction" / "verdict oriented"
93	- "CRUXEval" + "execution reasoning"
94	- "patch correctness prediction" / "automated patch assessment"
95	- "test outcome prediction" / "pass fail prediction"
96	- "selective trace" + "debugging" / "program repair"
97	- "code correctness prediction" / "classification"
98	- "error message" / "exception" + "program repair effectiveness"
99	- Cross-model generalization + code LLM fine-tuning
100	
101	Sources: arXiv, ACL Anthology, IEEE Xplore, Semantic Scholar, DBLP, Google Scholar
102	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "b5a29159-f20e-4a81-98d3-4ffccf799f41",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/report/scan_report.md",
      "content": "# Literature Scan Report — VOTA (Verdict-Oriented Trace Abstraction)\n\n**Date**: 2026-05-15  \n**Target**: EMNLP 2026 Main (ARR May 25 deadline)  \n**Queries executed**: 16 search groups across arXiv, ACL Anthology, Semantic Scholar, IEEE Xplore  \n\n## Summary\n\nNo **high-threat** direct competitor found. VOTA's core contribution — using fault indicator signals (exception events + assertion comparison points) from execution traces for binary verdict prediction via SFT — remains novel. The closest related works are in **patch correctness prediction**, which overlaps on input signals but differs fundamentally in task definition.\n\n---\n\n## New Papers Found (10 additions, 16→26 total)\n\n### MEDIUM Threat — Patch Correctness Prediction (Closest Competitors)\n\n| # | Paper | Venue | Threat | Relation to VOTA |\n|---|-------|-------|--------|-----------------|\n| 1 | **LLM4PatchCorrect** (Xin Zhou et al.) | TSE 2024 | **MEDIUM** | Uses execution traces + test cases as input for patch correctness assessment. Key difference: zero-shot prompting (no SFT), task is patch correctness (not test verdict), no trace compression. |\n| 2 | **APSG + Graph-LoRA** (arXiv 2505.02629) | arXiv 2025 | **MEDIUM** | PEFT for patch correctness with graph-structured code representation. Key difference: uses static code graph (not runtime trace), no fault indicator signals. |\n\n**Differentiation from VOTA**:\n- **Task**: Patch correctness (is this fix correct?) vs. VOTA's verdict prediction (does this test pass/fail?)\n- **Input**: LLM4PatchCorrect uses raw traces + test info; VOTA uses decision-relevant compressed signals\n- **Method**: LLM4PatchCorrect = zero-shot prompting; APSG = graph-LoRA; VOTA = SFT with trace abstraction\n- **Core finding**: Neither identifies fault indicator signals as near-perfect discriminative features (99.83%)\n\n### LOW Threat — Supporting Evidence & Background\n\n| # | Paper | Venue | Category | Why Relevant |\n|---|-------|-------|----------|-------------|\n| 3 | **FuseFL** (Widyasari et al.) | SANER 2024 | code-verdict | Uses test execution outcomes (expected/actual output, errors) for fault localization. Validates that test outcome signals carry discriminative value — same intuition as VOTA, different task. |\n| 4 | **REval** (Junkai Chen et al.) | arXiv 2403.16437 | evaluation | LLM runtime behavior prediction: avg accuracy 44.4%. Directly supports VOTA's argument that LLMs struggle with raw trace reasoning. |\n| 5 | **CodeMind** (Changshu Liu et al.) | arXiv 2402.09664 | evaluation | Code reasoning drops with complexity (control flow, API calls). Supports trace abstraction motivation. |\n| 6 | **CRUXEval-X** (Ruiyang Xu et al.) | ACL 2025 | evaluation | Multilingual CRUXEval (19 langs). Cross-language generalization reference for VOTA's cross-model experiments. |\n| 7 | **InspectCoder** (arXiv 2510.18327) | arXiv 2025 | trace-compression | Strategic breakpoint placement + runtime state inspection for repair. Selective inspection philosophy aligns with VOTA's fault indicator extraction. |\n| 8 | **MGDebugger** (Yuling Shi et al.) | arXiv 2410.01215 | trace-compression | Hierarchical debugging with LLM-simulated execution tracking key variables. Implicit trace abstraction. |\n| 9 | **UniDebugger** (Cheryl Lee et al.) | EMNLP 2025 | debugging-agents | Multi-agent debugging without execution traces (static analysis). Orthogonal to VOTA. |\n| 10 | **Seeker** (Xuanming Zhang et al.) | ICLR 2025 | debugging-agents | Exception handling with CEE knowledge base. Exception taxonomy provides complementary perspective to VOTA's exception event signals. |\n\n---\n\n## Threat Analysis\n\n### No HIGH Threat Competitors\n\nAfter 16 search queries, **no paper was found that**:\n1. Uses execution trace fault indicator signals (exceptions + assertion comparisons) specifically for verdict prediction\n2. Demonstrates that these signals alone achieve near-perfect accuracy\n3. Proposes decision-relevant trace compression for binary classification via SFT\n\n### MEDIUM Threats — How to Differentiate\n\n**vs. LLM4PatchCorrect**: Cite as evidence that execution traces contain useful signals for code correctness tasks. Differentiate on: (a) VOTA identifies *which parts* of the trace matter (fault indicators), while LLM4PatchCorrect uses raw traces; (b) SFT vs. zero-shot; (c) different task granularity.\n\n**vs. APSG + Graph-LoRA**: Cite as concurrent work on PEFT for code correctness. Differentiate on: (a) runtime signal vs. static graph; (b) VOTA's discovery that 2 signal types suffice, vs. APSG's complex graph construction.\n\n### Emerging Trend: Selective Trace\n\nMultiple 2025-2026 papers (InspectCoder, TraceCoder, Runtime Traces + Multi-Agent Debate) converge on the same insight: **selective trace information > full trace**. VOTA should position itself within this trend while emphasizing its unique angle — the selection criterion is *decision-relevance for verdict prediction*, not general debugging utility.\n\n---\n\n## Recommended Citations to Add\n\nPapers that should be cited in the VOTA paper (if not already):\n\n1. **LLM4PatchCorrect** (TSE 2024) — closest work using execution traces for correctness assessment\n2. **REval** (2024) — empirical evidence LLMs struggle with runtime reasoning (avg 44.4%)\n3. **CodeMind** (2024) — code reasoning evaluation showing complexity-dependent degradation\n4. **FuseFL** (SANER 2024) — validates test execution outcomes as discriminative signals\n5. **CRUXEval-X** (ACL 2025) — cross-language generalization methodology reference\n6. **InspectCoder** (2025) — selective runtime inspection trend\n\n---\n\n## Key Gaps Confirmed\n\n1. **No work directly applies execution trace to binary verdict (pass/fail) prediction** — VOTA fills this gap\n2. **No work identifies fault indicator signals as near-perfect discriminative features** — VOTA's core empirical finding\n3. **Decision-relevant trace compression for LLM classification is unexplored** — VOTA's methodological contribution\n4. **Cross-model generalization of trace-based verdict prediction is unstudied** — VOTA addresses this\n\n---\n\n## Search Methodology\n\n16 query groups covering:\n- \"execution trace\" + \"fault detection\" / \"verdict prediction\" / \"test prediction\"\n- \"trace compression\" + \"code understanding\" / \"debugging\"\n- \"exception signal\" + \"fault localization\"\n- \"VOTA\" / \"trace abstraction\" / \"verdict oriented\"\n- \"CRUXEval\" + \"execution reasoning\"\n- \"patch correctness prediction\" / \"automated patch assessment\"\n- \"test outcome prediction\" / \"pass fail prediction\"\n- \"selective trace\" + \"debugging\" / \"program repair\"\n- \"code correctness prediction\" / \"classification\"\n- \"error message\" / \"exception\" + \"program repair effectiveness\"\n- Cross-model generalization + code LLM fine-tuning\n\nSources: arXiv, ACL Anthology, IEEE Xplore, Semantic Scholar, DBLP, Google Scholar\n",
      "numLines": 102,
      "startLine": 1,
      "totalLines": 102
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_018EtZCqKsoVAYGXbot6fFVa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/literature_scan_20260515/scan_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "60f9e805-a280-4757-8a45-39f12a75adbe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mg7ZcVSaRGfDj2vgHVhzmb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7724,
      "cache_read_input_tokens": 23978,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7724
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T13:43:11.558Z_

<details><summary>↩ Tool result · `toolu_018EtZCqKsoVAYGXbot6fFVa`</summary>

```text
1	# Literature Scan Report — VOTA (Verdict-Oriented Trace Abstraction)
2	
3	**Date**: 2026-05-15  
4	**Target**: EMNLP 2026 Main (ARR May 25 deadline)  
5	**Queries executed**: 16 search groups across arXiv, ACL Anthology, Semantic Scholar, IEEE Xplore  
6	
7	## Summary
8	
9	No **high-threat** direct competitor found. VOTA's core contribution — using fault indicator signals (exception events + assertion comparison points) from execution traces for binary verdict prediction via SFT — remains novel. The closest related works are in **patch correctness prediction**, which overlaps on input signals but differs fundamentally in task definition.
10	
11	---
12	
13	## New Papers Found (10 additions, 16→26 total)
14	
15	### MEDIUM Threat — Patch Correctness Prediction (Closest Competitors)
16	
17	| # | Paper | Venue | Threat | Relation to VOTA |
18	|---|-------|-------|--------|-----------------|
19	| 1 | **LLM4PatchCorrect** (Xin Zhou et al.) | TSE 2024 | **MEDIUM** | Uses execution traces + test cases as input for patch correctness assessment. Key difference: zero-shot prompting (no SFT), task is patch correctness (not test verdict), no trace compression. |
20	| 2 | **APSG + Graph-LoRA** (arXiv 2505.02629) | arXiv 2025 | **MEDIUM** | PEFT for patch correctness with graph-structured code representation. Key difference: uses static code graph (not runtime trace), no fault indicator signals. |
21	
22	**Differentiation from VOTA**:
23	- **Task**: Patch correctness (is this fix correct?) vs. VOTA's verdict prediction (does this test pass/fail?)
24	- **Input**: LLM4PatchCorrect uses raw traces + test info; VOTA uses decision-relevant compressed signals
25	- **Method**: LLM4PatchCorrect = zero-shot prompting; APSG = graph-LoRA; VOTA = SFT with trace abstraction
26	- **Core finding**: Neither identifies fault indicator signals as near-perfect discriminative features (99.83%)
27	
28	### LOW Threat — Supporting Evidence & Background
29	
30	| # | Paper | Venue | Category | Why Relevant |
31	|---|-------|-------|----------|-------------|
32	| 3 | **FuseFL** (Widyasari et al.) | SANER 2024 | code-verdict | Uses test execution outcomes (expected/actual output, errors) for fault localization. Validates that test outcome signals carry discriminative value — same intuition as VOTA, different task. |
33	| 4 | **REval** (Junkai Chen et al.) | arXiv 2403.16437 | evaluation | LLM runtime behavior prediction: avg accuracy 44.4%. Directly supports VOTA's argument that LLMs struggle with raw trace reasoning. |
34	| 5 | **CodeMind** (Changshu Liu et al.) | arXiv 2402.09664 | evaluation | Code reasoning drops with complexity (control flow, API calls). Supports trace abstraction motivation. |
35	| 6 | **CRUXEval-X** (Ruiyang Xu et al.) | ACL 2025 | evaluation | Multilingual CRUXEval (19 langs). Cross-language generalization reference for VOTA's cross-model experiments. |
36	| 7 | **InspectCoder** (arXiv 2510.18327) | arXiv 2025 | trace-compression | Strategic breakpoint placement + runtime state inspection for repair. Selective inspection philosophy aligns with VOTA's fault indicator extraction. |
37	| 8 | **MGDebugger** (Yuling Shi et al.) | arXiv 2410.01215 | trace-compression | Hierarchical debugging with LLM-simulated execution tracking key variables. Implicit trace abstraction. |
38	| 9 | **UniDebugger** (Cheryl Lee et al.) | EMNLP 2025 | debugging-agents | Multi-agent debugging without execution traces (static analysis). Orthogonal to VOTA. |
39	| 10 | **Seeker** (Xuanming Zhang et al.) | ICLR 2025 | debugging-agents | Exception handling with CEE knowledge base. Exception taxonomy provides complementary perspective to VOTA's exception event signals. |
40	
41	---
42	
43	## Threat Analysis
44	
45	### No HIGH Threat Competitors
46	
47	After 16 search queries, **no paper was found that**:
48	1. Uses execution trace fault indicator signals (exceptions + assertion comparisons) specifically for verdict prediction
49	2. Demonstrates that these signals alone achieve near-perfect accuracy
50	3. Proposes decision-relevant trace compression for binary classification via SFT
51	
52	### MEDIUM Threats — How to Differentiate
53	
54	**vs. LLM4PatchCorrect**: Cite as evidence that execution traces contain useful signals for code correctness tasks. Differentiate on: (a) VOTA identifies *which parts* of the trace matter (fault indicators), while LLM4PatchCorrect uses raw traces; (b) SFT vs. zero-shot; (c) different task granularity.
55	
56	**vs. APSG + Graph-LoRA**: Cite as concurrent work on PEFT for code correctness. Differentiate on: (a) runtime signal vs. static graph; (b) VOTA's discovery that 2 signal types suffice, vs. APSG's complex graph construction.
57	
58	### Emerging Trend: Selective Trace
59	
60	Multiple 2025-2026 papers (InspectCoder, TraceCoder, Runtime Traces + Multi-Agent Debate) converge on the same insight: **selective trace information > full trace**. VOTA should position itself within this trend while emphasizing its unique angle — the selection criterion is *decision-relevance for verdict prediction*, not general debugging utility.
61	
62	---
63	
64	## Recommended Citations to Add
65	
66	Papers that should be cited in the VOTA paper (if not already):
67	
68	1. **LLM4PatchCorrect** (TSE 2024) — closest work using execution traces for correctness assessment
69	2. **REval** (2024) — empirical evidence LLMs struggle with runtime reasoning (avg 44.4%)
70	3. **CodeMind** (2024) — code reasoning evaluation showing complexity-dependent degradation
71	4. **FuseFL** (SANER 2024) — validates test execution outcomes as discriminative signals
72	5. **CRUXEval-X** (ACL 2025) — cross-language generalization methodology reference
73	6. **InspectCoder** (2025) — selective runtime inspection trend
74	
75	---
76	
77	## Key Gaps Confirmed
78	
79	1. **No work directly applies execution trace to binary verdict (pass/fail) prediction** — VOTA fills this gap
80	2. **No work identifies fault indicator signals as near-perfect discriminative features** — VOTA's core empirical finding
81	3. **Decision-relevant trace compression for LLM classification is unexplored** — VOTA's methodological contribution
82	4. **Cross-model generalization of trace-based verdict prediction is unstudied** — VOTA addresses this
83	
84	---
85	
86	## Search Methodology
87	
88	16 query groups covering:
89	- "execution trace" + "fault detection" / "verdict prediction" / "test prediction"
90	- "trace compression" + "code understanding" / "debugging"
91	- "exception signal" + "fault localization"
92	- "VOTA" / "trace abstraction" / "verdict oriented"
93	- "CRUXEval" + "execution reasoning"
94	- "patch correctness prediction" / "automated patch assessment"
95	- "test outcome prediction" / "pass fail prediction"
96	- "selective trace" + "debugging" / "program repair"
97	- "code correctness prediction" / "classification"
98	- "error message" / "exception" + "program repair effectiveness"
99	- Cross-model generalization + code LLM fine-tuning
100	
101	Sources: arXiv, ACL Anthology, IEEE Xplore, Semantic Scholar, DBLP, Google Scholar
102	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "474a80cd-9a68-4196-b3fb-963e0a4b7962",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/literature_scan_20260515/scan_report.md",
      "content": "# Literature Scan Report — VOTA (Verdict-Oriented Trace Abstraction)\n\n**Date**: 2026-05-15  \n**Target**: EMNLP 2026 Main (ARR May 25 deadline)  \n**Queries executed**: 16 search groups across arXiv, ACL Anthology, Semantic Scholar, IEEE Xplore  \n\n## Summary\n\nNo **high-threat** direct competitor found. VOTA's core contribution — using fault indicator signals (exception events + assertion comparison points) from execution traces for binary verdict prediction via SFT — remains novel. The closest related works are in **patch correctness prediction**, which overlaps on input signals but differs fundamentally in task definition.\n\n---\n\n## New Papers Found (10 additions, 16→26 total)\n\n### MEDIUM Threat — Patch Correctness Prediction (Closest Competitors)\n\n| # | Paper | Venue | Threat | Relation to VOTA |\n|---|-------|-------|--------|-----------------|\n| 1 | **LLM4PatchCorrect** (Xin Zhou et al.) | TSE 2024 | **MEDIUM** | Uses execution traces + test cases as input for patch correctness assessment. Key difference: zero-shot prompting (no SFT), task is patch correctness (not test verdict), no trace compression. |\n| 2 | **APSG + Graph-LoRA** (arXiv 2505.02629) | arXiv 2025 | **MEDIUM** | PEFT for patch correctness with graph-structured code representation. Key difference: uses static code graph (not runtime trace), no fault indicator signals. |\n\n**Differentiation from VOTA**:\n- **Task**: Patch correctness (is this fix correct?) vs. VOTA's verdict prediction (does this test pass/fail?)\n- **Input**: LLM4PatchCorrect uses raw traces + test info; VOTA uses decision-relevant compressed signals\n- **Method**: LLM4PatchCorrect = zero-shot prompting; APSG = graph-LoRA; VOTA = SFT with trace abstraction\n- **Core finding**: Neither identifies fault indicator signals as near-perfect discriminative features (99.83%)\n\n### LOW Threat — Supporting Evidence & Background\n\n| # | Paper | Venue | Category | Why Relevant |\n|---|-------|-------|----------|-------------|\n| 3 | **FuseFL** (Widyasari et al.) | SANER 2024 | code-verdict | Uses test execution outcomes (expected/actual output, errors) for fault localization. Validates that test outcome signals carry discriminative value — same intuition as VOTA, different task. |\n| 4 | **REval** (Junkai Chen et al.) | arXiv 2403.16437 | evaluation | LLM runtime behavior prediction: avg accuracy 44.4%. Directly supports VOTA's argument that LLMs struggle with raw trace reasoning. |\n| 5 | **CodeMind** (Changshu Liu et al.) | arXiv 2402.09664 | evaluation | Code reasoning drops with complexity (control flow, API calls). Supports trace abstraction motivation. |\n| 6 | **CRUXEval-X** (Ruiyang Xu et al.) | ACL 2025 | evaluation | Multilingual CRUXEval (19 langs). Cross-language generalization reference for VOTA's cross-model experiments. |\n| 7 | **InspectCoder** (arXiv 2510.18327) | arXiv 2025 | trace-compression | Strategic breakpoint placement + runtime state inspection for repair. Selective inspection philosophy aligns with VOTA's fault indicator extraction. |\n| 8 | **MGDebugger** (Yuling Shi et al.) | arXiv 2410.01215 | trace-compression | Hierarchical debugging with LLM-simulated execution tracking key variables. Implicit trace abstraction. |\n| 9 | **UniDebugger** (Cheryl Lee et al.) | EMNLP 2025 | debugging-agents | Multi-agent debugging without execution traces (static analysis). Orthogonal to VOTA. |\n| 10 | **Seeker** (Xuanming Zhang et al.) | ICLR 2025 | debugging-agents | Exception handling with CEE knowledge base. Exception taxonomy provides complementary perspective to VOTA's exception event signals. |\n\n---\n\n## Threat Analysis\n\n### No HIGH Threat Competitors\n\nAfter 16 search queries, **no paper was found that**:\n1. Uses execution trace fault indicator signals (exceptions + assertion comparisons) specifically for verdict prediction\n2. Demonstrates that these signals alone achieve near-perfect accuracy\n3. Proposes decision-relevant trace compression for binary classification via SFT\n\n### MEDIUM Threats — How to Differentiate\n\n**vs. LLM4PatchCorrect**: Cite as evidence that execution traces contain useful signals for code correctness tasks. Differentiate on: (a) VOTA identifies *which parts* of the trace matter (fault indicators), while LLM4PatchCorrect uses raw traces; (b) SFT vs. zero-shot; (c) different task granularity.\n\n**vs. APSG + Graph-LoRA**: Cite as concurrent work on PEFT for code correctness. Differentiate on: (a) runtime signal vs. static graph; (b) VOTA's discovery that 2 signal types suffice, vs. APSG's complex graph construction.\n\n### Emerging Trend: Selective Trace\n\nMultiple 2025-2026 papers (InspectCoder, TraceCoder, Runtime Traces + Multi-Agent Debate) converge on the same insight: **selective trace information > full trace**. VOTA should position itself within this trend while emphasizing its unique angle — the selection criterion is *decision-relevance for verdict prediction*, not general debugging utility.\n\n---\n\n## Recommended Citations to Add\n\nPapers that should be cited in the VOTA paper (if not already):\n\n1. **LLM4PatchCorrect** (TSE 2024) — closest work using execution traces for correctness assessment\n2. **REval** (2024) — empirical evidence LLMs struggle with runtime reasoning (avg 44.4%)\n3. **CodeMind** (2024) — code reasoning evaluation showing complexity-dependent degradation\n4. **FuseFL** (SANER 2024) — validates test execution outcomes as discriminative signals\n5. **CRUXEval-X** (ACL 2025) — cross-language generalization methodology reference\n6. **InspectCoder** (2025) — selective runtime inspection trend\n\n---\n\n## Key Gaps Confirmed\n\n1. **No work directly applies execution trace to binary verdict (pass/fail) prediction** — VOTA fills this gap\n2. **No work identifies fault indicator signals as near-perfect discriminative features** — VOTA's core empirical finding\n3. **Decision-relevant trace compression for LLM classification is unexplored** — VOTA's methodological contribution\n4. **Cross-model generalization of trace-based verdict prediction is unstudied** — VOTA addresses this\n\n---\n\n## Search Methodology\n\n16 query groups covering:\n- \"execution trace\" + \"fault detection\" / \"verdict prediction\" / \"test prediction\"\n- \"trace compression\" + \"code understanding\" / \"debugging\"\n- \"exception signal\" + \"fault localization\"\n- \"VOTA\" / \"trace abstraction\" / \"verdict oriented\"\n- \"CRUXEval\" + \"execution reasoning\"\n- \"patch correctness prediction\" / \"automated patch assessment\"\n- \"test outcome prediction\" / \"pass fail prediction\"\n- \"selective trace\" + \"debugging\" / \"program repair\"\n- \"code correctness prediction\" / \"classification\"\n- \"error message\" / \"exception\" + \"program repair effectiveness\"\n- Cross-model generalization + code LLM fine-tuning\n\nSources: arXiv, ACL Anthology, IEEE Xplore, Semantic Scholar, DBLP, Google Scholar\n",
      "numLines": 102,
      "startLine": 1,
      "totalLines": 102
    }
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Both files are identical. Now I need to rewrite the scan_report.md with:

1. Wang et al. (EMNLP 2025 Findings) added as MEDIUM-HIGH threat
2. LLM4PatchCorrect elevated discussion
3. APSG+Graph-LoRA kept
4. All assertive language ("remains novel", "fills this gap") replaced with neutral phrasing

Let me write the updated version. The key changes:

**Summary**: Remove "remains novel", use neutral language
**New Papers Found**: Add Wang et al. as MEDIUM-HIGH threat, restructure the threat table


**Threat Analysis**: Add Wang et al. as the conceptual-level MEDIUM-HIGH threat, rewrite differentiation points, and remove all assertive language
**Key Gaps**: Rewrite without "fills this gap" etc.

Now I'm drafting the new version with these modifications throughout.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "075298cf-bd09-4d6a-a1b1-719c2473beef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1jg4UmeBUyJb9Ag8srVkb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4559,
      "cache_read_input_tokens": 31702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4559
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 21_

Both copies are identical. Now I'll rewrite the report with Wang et al. as MEDIUM-HIGH threat and neutral language throughout.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "dde5fbd9-63f0-4961-ab97-9e338e5b3795",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1jg4UmeBUyJb9Ag8srVkb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4559,
      "cache_read_input_tokens": 31702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4559
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Write · `toolu_01Pmt5KoinYDSYVCFZhKjezB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/report/scan_report.md",
  "content": "# Literature Scan Report — VOTA (Verdict-Oriented Trace Abstraction)\n\n**Date**: 2026-05-15  \n**Target**: EMNLP 2026 Main (ARR May 25 deadline)  \n**Queries executed**: 16 search groups across arXiv, ACL Anthology, Semantic Scholar, IEEE Xplore  \n\n## Summary\n\nNo direct competitor was found that combines execution trace compression with SFT for binary verdict prediction. However, Wang et al. (EMNLP 2025 Findings) present a significant conceptual challenge: their comprehensive study of 5 trace formats for SFT concludes that semantic information from execution traces has limited usefulness. VOTA's response hinges on the distinction between raw/formatted traces and decision-relevant compression targeting fault indicator signals. The closest methodological neighbors are in **patch correctness prediction**, which shares input signal space but differs in task definition and approach.\n\n---\n\n## New Papers Found (10 additions, 16→26 total)\n\n### MEDIUM-HIGH Threat — Trace SFT Effectiveness\n\n| # | Paper | Venue | Threat | Relation to VOTA |\n|---|-------|-------|--------|-----------------|\n| 1 | **Wang et al. \"Do Code Semantics Help?\"** (Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li) | Findings of EMNLP 2025 | **MEDIUM-HIGH** | Comprehensive study testing 5 trace formats (Scratchpad, NExT, SemCoder, CodeExecutor, Concise) for SFT on code generation/repair. Conclusion: \"semantic information has limited usefulness for SFT.\" Conceptually the strongest challenge to any trace-based SFT approach including VOTA. |\n\n**Why MEDIUM-HIGH, not HIGH**: Wang et al.'s study differs from VOTA on three axes:\n- **Task**: They evaluate code generation and repair; VOTA targets verdict prediction (binary classification), a fundamentally different downstream task where trace signals serve as discriminative features rather than generative context\n- **Trace content**: All 5 formats they test preserve execution flow information (variable states, step-by-step traces); none isolates fault indicator signals (exception events, assertion comparison outcomes) — the specific signals VOTA's ablation identifies as carrying nearly all discriminative power\n- **Compression strategy**: Their \"Concise\" format is a syntactic reduction of trace verbosity; VOTA's compression is semantic, retaining only decision-relevant signals for the verdict task\n\n**Implication for VOTA paper**: This paper must be cited and directly addressed. The argument is: \"raw trace ineffective for SFT ≠ compressed fault-indicator signals ineffective for SFT.\" VOTA's component ablation (exception_only achieving 99.83%) provides the empirical counterpoint — the value is not in trace format but in isolating the right signals for the right task.\n\n### MEDIUM Threat — Patch Correctness Prediction\n\n| # | Paper | Venue | Threat | Relation to VOTA |\n|---|-------|-------|--------|-----------------|\n| 2 | **LLM4PatchCorrect** (Xin Zhou et al.) | TSE 2024 | **MEDIUM** | Uses execution traces + test cases as input for patch correctness assessment. Key difference: zero-shot prompting (no SFT), task is patch correctness (not test verdict), no trace compression. |\n| 3 | **APSG + Graph-LoRA** (arXiv 2505.02629) | arXiv 2025 | **LOW-MEDIUM** | PEFT for patch correctness with graph-structured code representation. Key difference: uses static code graph (not runtime trace), no fault indicator signals. |\n\n**Differentiation from VOTA**:\n- **Task**: Patch correctness (is this fix correct?) vs. VOTA's verdict prediction (does this test pass/fail?)\n- **Input**: LLM4PatchCorrect uses raw traces + test info; VOTA uses decision-relevant compressed signals\n- **Method**: LLM4PatchCorrect = zero-shot prompting; APSG = graph-LoRA on static graphs; VOTA = SFT with trace abstraction\n- **Signal identification**: Neither work isolates fault indicator signals or measures their individual contribution\n\n### LOW Threat — Supporting Evidence & Background\n\n| # | Paper | Venue | Category | Why Relevant |\n|---|-------|-------|----------|-------------|\n| 4 | **FuseFL** (Widyasari et al.) | SANER 2024 | code-verdict | Uses test execution outcomes (expected/actual output, errors) for fault localization. Validates that test outcome signals carry discriminative value — same intuition as VOTA, different task. |\n| 5 | **REval** (Junkai Chen et al.) | arXiv 2403.16437 | evaluation | LLM runtime behavior prediction: avg accuracy 44.4%. Supports VOTA's argument that LLMs struggle with raw trace reasoning. |\n| 6 | **CodeMind** (Changshu Liu et al.) | arXiv 2402.09664 | evaluation | Code reasoning drops with complexity (control flow, API calls). Supports trace abstraction motivation. |\n| 7 | **CRUXEval-X** (Ruiyang Xu et al.) | ACL 2025 | evaluation | Multilingual CRUXEval (19 langs). Cross-language generalization reference for VOTA's cross-model experiments. |\n| 8 | **InspectCoder** (arXiv 2510.18327) | arXiv 2025 | trace-compression | Strategic breakpoint placement + runtime state inspection for repair. Selective inspection philosophy aligns with VOTA's fault indicator extraction. |\n| 9 | **MGDebugger** (Yuling Shi et al.) | arXiv 2410.01215 | trace-compression | Hierarchical debugging with LLM-simulated execution tracking key variables. Implicit trace abstraction. |\n| 10 | **UniDebugger** (Cheryl Lee et al.) | EMNLP 2025 | debugging-agents | Multi-agent debugging without execution traces (static analysis). Orthogonal to VOTA. |\n| 11 | **Seeker** (Xuanming Zhang et al.) | ICLR 2025 | debugging-agents | Exception handling with CEE knowledge base. Exception taxonomy provides complementary perspective to VOTA's exception event signals. |\n\n---\n\n## Threat Analysis\n\n### Conceptual Threat: Wang et al. (EMNLP 2025 Findings) — MEDIUM-HIGH\n\nThis is the most important paper for VOTA to address. Their finding that \"execution trace semantic information has limited usefulness for SFT\" could be read as undermining any trace-based SFT approach. VOTA's differentiation rests on three empirical arguments:\n\n1. **Task difference**: Wang et al. study code generation/repair (open-ended generative tasks); VOTA targets binary classification (verdict prediction). Trace signals that fail to improve generation may still serve as strong discriminative features for classification.\n2. **Signal granularity**: Wang et al.'s 5 trace formats all represent execution flow at varying verbosity levels. None isolates fault indicator signals (exception type/message, assertion expected-vs-actual). VOTA's ablation shows the exception signal alone drives 99.83% accuracy — this is a qualitatively different use of trace information.\n3. **Compression semantics**: Their \"Concise\" format reduces trace tokens but preserves the same information type. VOTA's compression is task-driven: it discards execution flow and retains only signals relevant to the pass/fail decision.\n\n**Risk**: A reviewer familiar with Wang et al. may question whether VOTA is \"yet another trace SFT paper.\" The response should preemptively frame VOTA as studying *which* trace signals matter for *which* tasks, not whether traces help generically.\n\n### Methodological Threats\n\n**vs. LLM4PatchCorrect (TSE 2024) — MEDIUM**: The closest work combining execution traces with correctness assessment. Differentiation: (a) VOTA identifies *which parts* of the trace matter (fault indicators), while LLM4PatchCorrect uses uncompressed traces; (b) SFT vs. zero-shot prompting; (c) verdict prediction vs. patch correctness. LLM4PatchCorrect should be cited as evidence that execution traces contain useful signals for correctness tasks, while noting the methodological gap VOTA addresses.\n\n**vs. APSG + Graph-LoRA (arXiv 2025) — LOW-MEDIUM**: Concurrent work on PEFT for code correctness. Differentiation: (a) runtime signals vs. static code graphs; (b) VOTA's finding that 2 signal types suffice, vs. APSG's complex graph construction. The approaches are largely complementary — APSG could potentially benefit from incorporating runtime signals.\n\n### Emerging Trend: Selective Trace\n\nMultiple 2025-2026 papers (InspectCoder, TraceCoder, Runtime Traces + Multi-Agent Debate) converge on the insight that **selective trace information outperforms full traces**. VOTA aligns with this trend; its distinguishing characteristic is that the selection criterion is *decision-relevance for verdict prediction* rather than general debugging utility.\n\n---\n\n## Recommended Citations to Add\n\n1. **Wang et al. \"Do Code Semantics Help?\"** (Findings of EMNLP 2025) — must-cite; primary conceptual challenge to address\n2. **LLM4PatchCorrect** (TSE 2024) — closest work using execution traces for correctness assessment\n3. **REval** (2024) — empirical evidence LLMs struggle with runtime reasoning (avg 44.4%)\n4. **CodeMind** (2024) — code reasoning evaluation showing complexity-dependent degradation\n5. **FuseFL** (SANER 2024) — validates test execution outcomes as discriminative signals\n6. **CRUXEval-X** (ACL 2025) — cross-language generalization methodology reference\n7. **InspectCoder** (2025) — selective runtime inspection trend\n\n---\n\n## Gap Assessment\n\nBased on the current scan, the following gaps appear to hold:\n\n1. **Binary verdict prediction from execution traces**: No identified work directly applies execution trace signals to pass/fail prediction via SFT. The closest (LLM4PatchCorrect) uses zero-shot prompting for a different task (patch correctness).\n2. **Fault indicator signal isolation**: No identified work measures the individual contribution of exception events or assertion comparison signals to classification accuracy. VOTA's ablation results (exception_only at 99.83%) appear to be a novel empirical finding in this space.\n3. **Decision-relevant trace compression for LLM classification**: Existing trace compression/selection work targets program repair or debugging, not binary classification. Whether VOTA's compression strategy generalizes beyond verdict prediction is an open question.\n4. **Cross-model generalization**: Trace-based verdict prediction across different base models (Qwen, DeepSeek) has not been studied elsewhere in the surveyed literature.\n\nThese assessments are based on the 26 papers currently in the literature map. A reviewer with deeper knowledge of the software testing or mutation testing literature may identify additional related work not covered here.\n\n---\n\n## Search Methodology\n\n16 query groups covering:\n- \"execution trace\" + \"fault detection\" / \"verdict prediction\" / \"test prediction\"\n- \"trace compression\" + \"code understanding\" / \"debugging\"\n- \"exception signal\" + \"fault localization\"\n- \"VOTA\" / \"trace abstraction\" / \"verdict oriented\"\n- \"CRUXEval\" + \"execution reasoning\"\n- \"patch correctness prediction\" / \"automated patch assessment\"\n- \"test outcome prediction\" / \"pass fail prediction\"\n- \"selective trace\" + \"debugging\" / \"program repair\"\n- \"code correctness prediction\" / \"classification\"\n- \"error message\" / \"exception\" + \"program repair effectiveness\"\n- Cross-model generalization + code LLM fine-tuning\n- \"code semantics\" + \"execution trace\" + \"SFT\" (added for Wang et al. coverage)\n\nSources: arXiv, ACL Anthology, IEEE Xplore, Semantic Scholar, DBLP, Google Scholar\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "1f33fa93-e106-4682-9268-7952306f8dcd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1jg4UmeBUyJb9Ag8srVkb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4559,
      "cache_read_input_tokens": 31702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4559
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T13:44:08.690Z_

<details><summary>↩ Tool result · `toolu_01Pmt5KoinYDSYVCFZhKjezB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/report/scan_report.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "8ec42665-68bb-4b8c-8725-51f07cce2e68",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/report/scan_report.md",
    "content": "# Literature Scan Report — VOTA (Verdict-Oriented Trace Abstraction)\n\n**Date**: 2026-05-15  \n**Target**: EMNLP 2026 Main (ARR May 25 deadline)  \n**Queries executed**: 16 search groups across arXiv, ACL Anthology, Semantic Scholar, IEEE Xplore  \n\n## Summary\n\nNo direct competitor was found that combines execution trace compression with SFT for binary verdict prediction. However, Wang et al. (EMNLP 2025 Findings) present a significant conceptual challenge: their comprehensive study of 5 trace formats for SFT concludes that semantic information from execution traces has limited usefulness. VOTA's response hinges on the distinction between raw/formatted traces and decision-relevant compression targeting fault indicator signals. The closest methodological neighbors are in **patch correctness prediction**, which shares input signal space but differs in task definition and approach.\n\n---\n\n## New Papers Found (10 additions, 16→26 total)\n\n### MEDIUM-HIGH Threat — Trace SFT Effectiveness\n\n| # | Paper | Venue | Threat | Relation to VOTA |\n|---|-------|-------|--------|-----------------|\n| 1 | **Wang et al. \"Do Code Semantics Help?\"** (Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li) | Findings of EMNLP 2025 | **MEDIUM-HIGH** | Comprehensive study testing 5 trace formats (Scratchpad, NExT, SemCoder, CodeExecutor, Concise) for SFT on code generation/repair. Conclusion: \"semantic information has limited usefulness for SFT.\" Conceptually the strongest challenge to any trace-based SFT approach including VOTA. |\n\n**Why MEDIUM-HIGH, not HIGH**: Wang et al.'s study differs from VOTA on three axes:\n- **Task**: They evaluate code generation and repair; VOTA targets verdict prediction (binary classification), a fundamentally different downstream task where trace signals serve as discriminative features rather than generative context\n- **Trace content**: All 5 formats they test preserve execution flow information (variable states, step-by-step traces); none isolates fault indicator signals (exception events, assertion comparison outcomes) — the specific signals VOTA's ablation identifies as carrying nearly all discriminative power\n- **Compression strategy**: Their \"Concise\" format is a syntactic reduction of trace verbosity; VOTA's compression is semantic, retaining only decision-relevant signals for the verdict task\n\n**Implication for VOTA paper**: This paper must be cited and directly addressed. The argument is: \"raw trace ineffective for SFT ≠ compressed fault-indicator signals ineffective for SFT.\" VOTA's component ablation (exception_only achieving 99.83%) provides the empirical counterpoint — the value is not in trace format but in isolating the right signals for the right task.\n\n### MEDIUM Threat — Patch Correctness Prediction\n\n| # | Paper | Venue | Threat | Relation to VOTA |\n|---|-------|-------|--------|-----------------|\n| 2 | **LLM4PatchCorrect** (Xin Zhou et al.) | TSE 2024 | **MEDIUM** | Uses execution traces + test cases as input for patch correctness assessment. Key difference: zero-shot prompting (no SFT), task is patch correctness (not test verdict), no trace compression. |\n| 3 | **APSG + Graph-LoRA** (arXiv 2505.02629) | arXiv 2025 | **LOW-MEDIUM** | PEFT for patch correctness with graph-structured code representation. Key difference: uses static code graph (not runtime trace), no fault indicator signals. |\n\n**Differentiation from VOTA**:\n- **Task**: Patch correctness (is this fix correct?) vs. VOTA's verdict prediction (does this test pass/fail?)\n- **Input**: LLM4PatchCorrect uses raw traces + test info; VOTA uses decision-relevant compressed signals\n- **Method**: LLM4PatchCorrect = zero-shot prompting; APSG = graph-LoRA on static graphs; VOTA = SFT with trace abstraction\n- **Signal identification**: Neither work isolates fault indicator signals or measures their individual contribution\n\n### LOW Threat — Supporting Evidence & Background\n\n| # | Paper | Venue | Category | Why Relevant |\n|---|-------|-------|----------|-------------|\n| 4 | **FuseFL** (Widyasari et al.) | SANER 2024 | code-verdict | Uses test execution outcomes (expected/actual output, errors) for fault localization. Validates that test outcome signals carry discriminative value — same intuition as VOTA, different task. |\n| 5 | **REval** (Junkai Chen et al.) | arXiv 2403.16437 | evaluation | LLM runtime behavior prediction: avg accuracy 44.4%. Supports VOTA's argument that LLMs struggle with raw trace reasoning. |\n| 6 | **CodeMind** (Changshu Liu et al.) | arXiv 2402.09664 | evaluation | Code reasoning drops with complexity (control flow, API calls). Supports trace abstraction motivation. |\n| 7 | **CRUXEval-X** (Ruiyang Xu et al.) | ACL 2025 | evaluation | Multilingual CRUXEval (19 langs). Cross-language generalization reference for VOTA's cross-model experiments. |\n| 8 | **InspectCoder** (arXiv 2510.18327) | arXiv 2025 | trace-compression | Strategic breakpoint placement + runtime state inspection for repair. Selective inspection philosophy aligns with VOTA's fault indicator extraction. |\n| 9 | **MGDebugger** (Yuling Shi et al.) | arXiv 2410.01215 | trace-compression | Hierarchical debugging with LLM-simulated execution tracking key variables. Implicit trace abstraction. |\n| 10 | **UniDebugger** (Cheryl Lee et al.) | EMNLP 2025 | debugging-agents | Multi-agent debugging without execution traces (static analysis). Orthogonal to VOTA. |\n| 11 | **Seeker** (Xuanming Zhang et al.) | ICLR 2025 | debugging-agents | Exception handling with CEE knowledge base. Exception taxonomy provides complementary perspective to VOTA's exception event signals. |\n\n---\n\n## Threat Analysis\n\n### Conceptual Threat: Wang et al. (EMNLP 2025 Findings) — MEDIUM-HIGH\n\nThis is the most important paper for VOTA to address. Their finding that \"execution trace semantic information has limited usefulness for SFT\" could be read as undermining any trace-based SFT approach. VOTA's differentiation rests on three empirical arguments:\n\n1. **Task difference**: Wang et al. study code generation/repair (open-ended generative tasks); VOTA targets binary classification (verdict prediction). Trace signals that fail to improve generation may still serve as strong discriminative features for classification.\n2. **Signal granularity**: Wang et al.'s 5 trace formats all represent execution flow at varying verbosity levels. None isolates fault indicator signals (exception type/message, assertion expected-vs-actual). VOTA's ablation shows the exception signal alone drives 99.83% accuracy — this is a qualitatively different use of trace information.\n3. **Compression semantics**: Their \"Concise\" format reduces trace tokens but preserves the same information type. VOTA's compression is task-driven: it discards execution flow and retains only signals relevant to the pass/fail decision.\n\n**Risk**: A reviewer familiar with Wang et al. may question whether VOTA is \"yet another trace SFT paper.\" The response should preemptively frame VOTA as studying *which* trace signals matter for *which* tasks, not whether traces help generically.\n\n### Methodological Threats\n\n**vs. LLM4PatchCorrect (TSE 2024) — MEDIUM**: The closest work combining execution traces with correctness assessment. Differentiation: (a) VOTA identifies *which parts* of the trace matter (fault indicators), while LLM4PatchCorrect uses uncompressed traces; (b) SFT vs. zero-shot prompting; (c) verdict prediction vs. patch correctness. LLM4PatchCorrect should be cited as evidence that execution traces contain useful signals for correctness tasks, while noting the methodological gap VOTA addresses.\n\n**vs. APSG + Graph-LoRA (arXiv 2025) — LOW-MEDIUM**: Concurrent work on PEFT for code correctness. Differentiation: (a) runtime signals vs. static code graphs; (b) VOTA's finding that 2 signal types suffice, vs. APSG's complex graph construction. The approaches are largely complementary — APSG could potentially benefit from incorporating runtime signals.\n\n### Emerging Trend: Selective Trace\n\nMultiple 2025-2026 papers (InspectCoder, TraceCoder, Runtime Traces + Multi-Agent Debate) converge on the insight that **selective trace information outperforms full traces**. VOTA aligns with this trend; its distinguishing characteristic is that the selection criterion is *decision-relevance for verdict prediction* rather than general debugging utility.\n\n---\n\n## Recommended Citations to Add\n\n1. **Wang et al. \"Do Code Semantics Help?\"** (Findings of EMNLP 2025) — must-cite; primary conceptual challenge to address\n2. **LLM4PatchCorrect** (TSE 2024) — closest work using execution traces for correctness assessment\n3. **REval** (2024) — empirical evidence LLMs struggle with runtime reasoning (avg 44.4%)\n4. **CodeMind** (2024) — code reasoning evaluation showing complexity-dependent degradation\n5. **FuseFL** (SANER 2024) — validates test execution outcomes as discriminative signals\n6. **CRUXEval-X** (ACL 2025) — cross-language generalization methodology reference\n7. **InspectCoder** (2025) — selective runtime inspection trend\n\n---\n\n## Gap Assessment\n\nBased on the current scan, the following gaps appear to hold:\n\n1. **Binary verdict prediction from execution traces**: No identified work directly applies execution trace signals to pass/fail prediction via SFT. The closest (LLM4PatchCorrect) uses zero-shot prompting for a different task (patch correctness).\n2. **Fault indicator signal isolation**: No identified work measures the individual contribution of exception events or assertion comparison signals to classification accuracy. VOTA's ablation results (exception_only at 99.83%) appear to be a novel empirical finding in this space.\n3. **Decision-relevant trace compression for LLM classification**: Existing trace compression/selection work targets program repair or debugging, not binary classification. Whether VOTA's compression strategy generalizes beyond verdict prediction is an open question.\n4. **Cross-model generalization**: Trace-based verdict prediction across different base models (Qwen, DeepSeek) has not been studied elsewhere in the surveyed literature.\n\nThese assessments are based on the 26 papers currently in the literature map. A reviewer with deeper knowledge of the software testing or mutation testing literature may identify additional related work not covered here.\n\n---\n\n## Search Methodology\n\n16 query groups covering:\n- \"execution trace\" + \"fault detection\" / \"verdict prediction\" / \"test prediction\"\n- \"trace compression\" + \"code understanding\" / \"debugging\"\n- \"exception signal\" + \"fault localization\"\n- \"VOTA\" / \"trace abstraction\" / \"verdict oriented\"\n- \"CRUXEval\" + \"execution reasoning\"\n- \"patch correctness prediction\" / \"automated patch assessment\"\n- \"test outcome prediction\" / \"pass fail prediction\"\n- \"selective trace\" + \"debugging\" / \"program repair\"\n- \"code correctness prediction\" / \"classification\"\n- \"error message\" / \"exception\" + \"program repair effectiveness\"\n- Cross-model generalization + code LLM fine-tuning\n- \"code semantics\" + \"execution trace\" + \"SFT\" (added for Wang et al. coverage)\n\nSources: arXiv, ACL Anthology, IEEE Xplore, Semantic Scholar, DBLP, Google Scholar\n",
    "structuredPatch": [
      {
        "oldStart": 6,
        "oldLines": 81,
        "newStart": 6,
        "newLines": 100,
        "lines": [
          " ",
          " ## Summary",
          " ",
          "-No **high-threat** direct competitor found. VOTA's core contribution — using fault indicator signals (exception events + assertion comparison points) from execution traces for binary verdict prediction via SFT — remains novel. The closest related works are in **patch correctness prediction**, which overlaps on input signals but differs fundamentally in task definition.",
          "+No direct competitor was found that combines execution trace compression with SFT for binary verdict prediction. However, Wang et al. (EMNLP 2025 Findings) present a significant conceptual challenge: their comprehensive study of 5 trace formats for SFT concludes that semantic information from execution traces has limited usefulness. VOTA's response hinges on the distinction between raw/formatted traces and decision-relevant compression targeting fault indicator signals. The closest methodological neighbors are in **patch correctness prediction**, which shares input signal space but differs in task definition and approach.",
          " ",
          " ---",
          " ",
          " ## New Papers Found (10 additions, 16→26 total)",
          " ",
          "-### MEDIUM Threat — Patch Correctness Prediction (Closest Competitors)",
          "+### MEDIUM-HIGH Threat — Trace SFT Effectiveness",
          " ",
          " | # | Paper | Venue | Threat | Relation to VOTA |",
          " |---|-------|-------|--------|-----------------|",
          "-| 1 | **LLM4PatchCorrect** (Xin Zhou et al.) | TSE 2024 | **MEDIUM** | Uses execution traces + test cases as input for patch correctness assessment. Key difference: zero-shot prompting (no SFT), task is patch correctness (not test verdict), no trace compression. |",
          "-| 2 | **APSG + Graph-LoRA** (arXiv 2505.02629) | arXiv 2025 | **MEDIUM** | PEFT for patch correctness with graph-structured code representation. Key difference: uses static code graph (not runtime trace), no fault indicator signals. |",
          "+| 1 | **Wang et al. \"Do Code Semantics Help?\"** (Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li) | Findings of EMNLP 2025 | **MEDIUM-HIGH** | Comprehensive study testing 5 trace formats (Scratchpad, NExT, SemCoder, CodeExecutor, Concise) for SFT on code generation/repair. Conclusion: \"semantic information has limited usefulness for SFT.\" Conceptually the strongest challenge to any trace-based SFT approach including VOTA. |",
          " ",
          "+**Why MEDIUM-HIGH, not HIGH**: Wang et al.'s study differs from VOTA on three axes:",
          "+- **Task**: They evaluate code generation and repair; VOTA targets verdict prediction (binary classification), a fundamentally different downstream task where trace signals serve as discriminative features rather than generative context",
          "+- **Trace content**: All 5 formats they test preserve execution flow information (variable states, step-by-step traces); none isolates fault indicator signals (exception events, assertion comparison outcomes) — the specific signals VOTA's ablation identifies as carrying nearly all discriminative power",
          "+- **Compression strategy**: Their \"Concise\" format is a syntactic reduction of trace verbosity; VOTA's compression is semantic, retaining only decision-relevant signals for the verdict task",
          "+",
          "+**Implication for VOTA paper**: This paper must be cited and directly addressed. The argument is: \"raw trace ineffective for SFT ≠ compressed fault-indicator signals ineffective for SFT.\" VOTA's component ablation (exception_only achieving 99.83%) provides the empirical counterpoint — the value is not in trace format but in isolating the right signals for the right task.",
          "+",
          "+### MEDIUM Threat — Patch Correctness Prediction",
          "+",
          "+| # | Paper | Venue | Threat | Relation to VOTA |",
          "+|---|-------|-------|--------|-----------------|",
          "+| 2 | **LLM4PatchCorrect** (Xin Zhou et al.) | TSE 2024 | **MEDIUM** | Uses execution traces + test cases as input for patch correctness assessment. Key difference: zero-shot prompting (no SFT), task is patch correctness (not test verdict), no trace compression. |",
          "+| 3 | **APSG + Graph-LoRA** (arXiv 2505.02629) | arXiv 2025 | **LOW-MEDIUM** | PEFT for patch correctness with graph-structured code representation. Key difference: uses static code graph (not runtime trace), no fault indicator signals. |",
          "+",
          " **Differentiation from VOTA**:",
          " - **Task**: Patch correctness (is this fix correct?) vs. VOTA's verdict prediction (does this test pass/fail?)",
          " - **Input**: LLM4PatchCorrect uses raw traces + test info; VOTA uses decision-relevant compressed signals",
          "-- **Method**: LLM4PatchCorrect = zero-shot prompting; APSG = graph-LoRA; VOTA = SFT with trace abstraction",
          "-- **Core finding**: Neither identifies fault indicator signals as near-perfect discriminative features (99.83%)",
          "+- **Method**: LLM4PatchCorrect = zero-shot prompting; APSG = graph-LoRA on static graphs; VOTA = SFT with trace abstraction",
          "+- **Signal identification**: Neither work isolates fault indicator signals or measures their individual contribution",
          " ",
          " ### LOW Threat — Supporting Evidence & Background",
          " ",
          " | # | Paper | Venue | Category | Why Relevant |",
          " |---|-------|-------|----------|-------------|",
          "-| 3 | **FuseFL** (Widyasari et al.) | SANER 2024 | code-verdict | Uses test execution outcomes (expected/actual output, errors) for fault localization. Validates that test outcome signals carry discriminative value — same intuition as VOTA, different task. |",
          "-| 4 | **REval** (Junkai Chen et al.) | arXiv 2403.16437 | evaluation | LLM runtime behavior prediction: avg accuracy 44.4%. Directly supports VOTA's argument that LLMs struggle with raw trace reasoning. |",
          "-| 5 | **CodeMind** (Changshu Liu et al.) | arXiv 2402.09664 | evaluation | Code reasoning drops with complexity (control flow, API calls). Supports trace abstraction motivation. |",
          "-| 6 | **CRUXEval-X** (Ruiyang Xu et al.) | ACL 2025 | evaluation | Multilingual CRUXEval (19 langs). Cross-language generalization reference for VOTA's cross-model experiments. |",
          "-| 7 | **InspectCoder** (arXiv 2510.18327) | arXiv 2025 | trace-compression | Strategic breakpoint placement + runtime state inspection for repair. Selective inspection philosophy aligns with VOTA's fault indicator extraction. |",
          "-| 8 | **MGDebugger** (Yuling Shi et al.) | arXiv 2410.01215 | trace-compression | Hierarchical debugging with LLM-simulated execution tracking key variables. Implicit trace abstraction. |",
          "-| 9 | **UniDebugger** (Cheryl Lee et al.) | EMNLP 2025 | debugging-agents | Multi-agent debugging without execution traces (static analysis). Orthogonal to VOTA. |",
          "-| 10 | **Seeker** (Xuanming Zhang et al.) | ICLR 2025 | debugging-agents | Exception handling with CEE knowledge base. Exception taxonomy provides complementary perspective to VOTA's exception event signals. |",
          "+| 4 | **FuseFL** (Widyasari et al.) | SANER 2024 | code-verdict | Uses test execution outcomes (expected/actual output, errors) for fault localization. Validates that test outcome signals carry discriminative value — same intuition as VOTA, different task. |",
          "+| 5 | **REval** (Junkai Chen et al.) | arXiv 2403.16437 | evaluation | LLM runtime behavior prediction: avg accuracy 44.4%. Supports VOTA's argument that LLMs struggle with raw trace reasoning. |",
          "+| 6 | **CodeMind** (Changshu Liu et al.) | arXiv 2402.09664 | evaluation | Code reasoning drops with complexity (control flow, API calls). Supports trace abstraction motivation. |",
          "+| 7 | **CRUXEval-X** (Ruiyang Xu et al.) | ACL 2025 | evaluation | Multilingual CRUXEval (19 langs). Cross-language generalization reference for VOTA's cross-model experiments. |",
          "+| 8 | **InspectCoder** (arXiv 2510.18327) | arXiv 2025 | trace-compression | Strategic breakpoint placement + runtime state inspection for repair. Selective inspection philosophy aligns with VOTA's fault indicator extraction. |",
          "+| 9 | **MGDebugger** (Yuling Shi et al.) | arXiv 2410.01215 | trace-compression | Hierarchical debugging with LLM-simulated execution tracking key variables. Implicit trace abstraction. |",
          "+| 10 | **UniDebugger** (Cheryl Lee et al.) | EMNLP 2025 | debugging-agents | Multi-agent debugging without execution traces (static analysis). Orthogonal to VOTA. |",
          "+| 11 | **Seeker** (Xuanming Zhang et al.) | ICLR 2025 | debugging-agents | Exception handling with CEE knowledge base. Exception taxonomy provides complementary perspective to VOTA's exception event signals. |",
          " ",
          " ---",
          " ",
          " ## Threat Analysis",
          " ",
          "-### No HIGH Threat Competitors",
          "+### Conceptual Threat: Wang et al. (EMNLP 2025 Findings) — MEDIUM-HIGH",
          " ",
          "-After 16 search queries, **no paper was found that**:",
          "-1. Uses execution trace fault indicator signals (exceptions + assertion comparisons) specifically for verdict prediction",
          "-2. Demonstrates that these signals alone achieve near-perfect accuracy",
          "-3. Proposes decision-relevant trace compression for binary classification via SFT",
          "+This is the most important paper for VOTA to address. Their finding that \"execution trace semantic information has limited usefulness for SFT\" could be read as undermining any trace-based SFT approach. VOTA's differentiation rests on three empirical arguments:",
          " ",
          "-### MEDIUM Threats — How to Differentiate",
          "+1. **Task difference**: Wang et al. study code generation/repair (open-ended generative tasks); VOTA targets binary classification (verdict prediction). Trace signals that fail to improve generation may still serve as strong discriminative features for classification.",
          "+2. **Signal granularity**: Wang et al.'s 5 trace formats all represent execution flow at varying verbosity levels. None isolates fault indicator signals (exception type/message, assertion expected-vs-actual). VOTA's ablation shows the exception signal alone drives 99.83% accuracy — this is a qualitatively different use of trace information.",
          "+3. **Compression semantics**: Their \"Concise\" format reduces trace tokens but preserves the same information type. VOTA's compression is task-driven: it discards execution flow and retains only signals relevant to the pass/fail decision.",
          " ",
          "-**vs. LLM4PatchCorrect**: Cite as evidence that execution traces contain useful signals for code correctness tasks. Differentiate on: (a) VOTA identifies *which parts* of the trace matter (fault indicators), while LLM4PatchCorrect uses raw traces; (b) SFT vs. zero-shot; (c) different task granularity.",
          "+**Risk**: A reviewer familiar with Wang et al. may question whether VOTA is \"yet another trace SFT paper.\" The response should preemptively frame VOTA as studying *which* trace signals matter for *which* tasks, not whether traces help generically.",
          " ",
          "-**vs. APSG + Graph-LoRA**: Cite as concurrent work on PEFT for code correctness. Differentiate on: (a) runtime signal vs. static graph; (b) VOTA's discovery that 2 signal types suffice, vs. APSG's complex graph construction.",
          "+### Methodological Threats",
          " ",
          "+**vs. LLM4PatchCorrect (TSE 2024) — MEDIUM**: The closest work combining execution traces with correctness assessment. Differentiation: (a) VOTA identifies *which parts* of the trace matter (fault indicators), while LLM4PatchCorrect uses uncompressed traces; (b) SFT vs. zero-shot prompting; (c) verdict prediction vs. patch correctness. LLM4PatchCorrect should be cited as evidence that execution traces contain useful signals for correctness tasks, while noting the methodological gap VOTA addresses.",
          "+",
          "+**vs. APSG + Graph-LoRA (arXiv 2025) — LOW-MEDIUM**: Concurrent work on PEFT for code correctness. Differentiation: (a) runtime signals vs. static code graphs; (b) VOTA's finding that 2 signal types suffice, vs. APSG's complex graph construction. The approaches are largely complementary — APSG could potentially benefit from incorporating runtime signals.",
          "+",
          " ### Emerging Trend: Selective Trace",
          " ",
          "-Multiple 2025-2026 papers (InspectCoder, TraceCoder, Runtime Traces + Multi-Agent Debate) converge on the same insight: **selective trace information > full trace**. VOTA should position itself within this trend while emphasizing its unique angle — the selection criterion is *decision-relevance for verdict prediction*, not general debugging utility.",
          "+Multiple 2025-2026 papers (InspectCoder, TraceCoder, Runtime Traces + Multi-Agent Debate) converge on the insight that **selective trace information outperforms full traces**. VOTA aligns with this trend; its distinguishing characteristic is that the selection criterion is *decision-relevance for verdict prediction* rather than general debugging utility.",
          " ",
          " ---",
          " ",
          " ## Recommended Citations to Add",
          " ",
          "-Papers that should be cited in the VOTA paper (if not already):",
          "+1. **Wang et al. \"Do Code Semantics Help?\"** (Findings of EMNLP 2025) — must-cite; primary conceptual challenge to address",
          "+2. **LLM4PatchCorrect** (TSE 2024) — closest work using execution traces for correctness assessment",
          "+3. **REval** (2024) — empirical evidence LLMs struggle with runtime reasoning (avg 44.4%)",
          "+4. **CodeMind** (2024) — code reasoning evaluation showing complexity-dependent degradation",
          "+5. **FuseFL** (SANER 2024) — validates test execution outcomes as discriminative signals",
          "+6. **CRUXEval-X** (ACL 2025) — cross-language generalization methodology reference",
          "+7. **InspectCoder** (2025) — selective runtime inspection trend",
          " ",
          "-1. **LLM4PatchCorrect** (TSE 2024) — closest work using execution traces for correctness assessment",
          "-2. **REval** (2024) — empirical evidence LLMs struggle with runtime reasoning (avg 44.4%)",
          "-3. **CodeMind** (2024) — code reasoning evaluation showing complexity-dependent degradation",
          "-4. **FuseFL** (SANER 2024) — validates test execution outcomes as discriminative signals",
          "-5. **CRUXEval-X** (ACL 2025) — cross-language generalization methodology reference",
          "-6. **InspectCoder** (2025) — selective runtime inspection trend",
          "-",
          " ---",
          " ",
          "-## Key Gaps Confirmed",
          "+## Gap Assessment",
          " ",
          "-1. **No work directly applies execution trace to binary verdict (pass/fail) prediction** — VOTA fills this gap",
          "-2. **No work identifies fault indicator signals as near-perfect discriminative features** — VOTA's core empirical finding",
          "-3. **Decision-relevant trace compression for LLM classification is unexplored** — VOTA's methodological contribution",
          "-4. **Cross-model generalization of trace-based verdict prediction is unstudied** — VOTA addresses this",
          "+Based on the current scan, the following gaps appear to hold:",
          " ",
          "+1. **Binary verdict prediction from execution traces**: No identified work directly applies execution trace signals to pass/fail prediction via SFT. The closest (LLM4PatchCorrect) uses zero-shot prompting for a different task (patch correctness).",
          "+2. **Fault indicator signal isolation**: No identified work measures the individual contribution of exception events or assertion comparison signals to classification accuracy. VOTA's ablation results (exception_only at 99.83%) appear to be a novel empirical finding in this space.",
          "+3. **Decision-relevant trace compression for LLM classification**: Existing trace compression/selection work targets program repair or debugging, not binary classification. Whether VOTA's compression strategy generalizes beyond verdict prediction is an open question.",
          "+4. **Cross-model generalization**: Trace-based verdict prediction across different base models (Qwen, DeepSeek) has not been studied elsewhere in the surveyed literature.",
          "+",
          "+These assessments are based on the 26 papers currently in the literature map. A reviewer with deeper knowledge of the software testing or mutation testing literature may identify additional related work not covered here.",
          "+",
          " ---",
          " ",
          " ## Search Methodology"
        ]
      },
      {
        "oldStart": 97,
        "oldLines": 5,
        "newStart": 116,
        "newLines": 6,
        "lines": [
          " - \"code correctness prediction\" / \"classification\"",
          " - \"error message\" / \"exception\" + \"program repair effectiveness\"",
          " - Cross-model generalization + code LLM fine-tuning",
          "+- \"code semantics\" + \"execution trace\" + \"SFT\" (added for Wang et al. coverage)",
          " ",
          " Sources: arXiv, ACL Anthology, IEEE Xplore, Semantic Scholar, DBLP, Google Scholar"
        ]
      }
    ],
    "originalFile": "# Literature Scan Report — VOTA (Verdict-Oriented Trace Abstraction)\n\n**Date**: 2026-05-15  \n**Target**: EMNLP 2026 Main (ARR May 25 deadline)  \n**Queries executed**: 16 search groups across arXiv, ACL Anthology, Semantic Scholar, IEEE Xplore  \n\n## Summary\n\nNo **high-threat** direct competitor found. VOTA's core contribution — using fault indicator signals (exception events + assertion comparison points) from execution traces for binary verdict prediction via SFT — remains novel. The closest related works are in **patch correctness prediction**, which overlaps on input signals but differs fundamentally in task definition.\n\n---\n\n## New Papers Found (10 additions, 16→26 total)\n\n### MEDIUM Threat — Patch Correctness Prediction (Closest Competitors)\n\n| # | Paper | Venue | Threat | Relation to VOTA |\n|---|-------|-------|--------|-----------------|\n| 1 | **LLM4PatchCorrect** (Xin Zhou et al.) | TSE 2024 | **MEDIUM** | Uses execution traces + test cases as input for patch correctness assessment. Key difference: zero-shot prompting (no SFT), task is patch correctness (not test verdict), no trace compression. |\n| 2 | **APSG + Graph-LoRA** (arXiv 2505.02629) | arXiv 2025 | **MEDIUM** | PEFT for patch correctness with graph-structured code representation. Key difference: uses static code graph (not runtime trace), no fault indicator signals. |\n\n**Differentiation from VOTA**:\n- **Task**: Patch correctness (is this fix correct?) vs. VOTA's verdict prediction (does this test pass/fail?)\n- **Input**: LLM4PatchCorrect uses raw traces + test info; VOTA uses decision-relevant compressed signals\n- **Method**: LLM4PatchCorrect = zero-shot prompting; APSG = graph-LoRA; VOTA = SFT with trace abstraction\n- **Core finding**: Neither identifies fault indicator signals as near-perfect discriminative features (99.83%)\n\n### LOW Threat — Supporting Evidence & Background\n\n| # | Paper | Venue | Category | Why Relevant |\n|---|-------|-------|----------|-------------|\n| 3 | **FuseFL** (Widyasari et al.) | SANER 2024 | code-verdict | Uses test execution outcomes (expected/actual output, errors) for fault localization. Validates that test outcome signals carry discriminative value — same intuition as VOTA, different task. |\n| 4 | **REval** (Junkai Chen et al.) | arXiv 2403.16437 | evaluation | LLM runtime behavior prediction: avg accuracy 44.4%. Directly supports VOTA's argument that LLMs struggle with raw trace reasoning. |\n| 5 | **CodeMind** (Changshu Liu et al.) | arXiv 2402.09664 | evaluation | Code reasoning drops with complexity (control flow, API calls). Supports trace abstraction motivation. |\n| 6 | **CRUXEval-X** (Ruiyang Xu et al.) | ACL 2025 | evaluation | Multilingual CRUXEval (19 langs). Cross-language generalization reference for VOTA's cross-model experiments. |\n| 7 | **InspectCoder** (arXiv 2510.18327) | arXiv 2025 | trace-compression | Strategic breakpoint placement + runtime state inspection for repair. Selective inspection philosophy aligns with VOTA's fault indicator extraction. |\n| 8 | **MGDebugger** (Yuling Shi et al.) | arXiv 2410.01215 | trace-compression | Hierarchical debugging with LLM-simulated execution tracking key variables. Implicit trace abstraction. |\n| 9 | **UniDebugger** (Cheryl Lee et al.) | EMNLP 2025 | debugging-agents | Multi-agent debugging without execution traces (static analysis). Orthogonal to VOTA. |\n| 10 | **Seeker** (Xuanming Zhang et al.) | ICLR 2025 | debugging-agents | Exception handling with CEE knowledge base. Exception taxonomy provides complementary perspective to VOTA's exception event signals. |\n\n---\n\n## Threat Analysis\n\n### No HIGH Threat Competitors\n\nAfter 16 search queries, **no paper was found that**:\n1. Uses execution trace fault indicator signals (exceptions + assertion comparisons) specifically for verdict prediction\n2. Demonstrates that these signals alone achieve near-perfect accuracy\n3. Proposes decision-relevant trace compression for binary classification via SFT\n\n### MEDIUM Threats — How to Differentiate\n\n**vs. LLM4PatchCorrect**: Cite as evidence that execution traces contain useful signals for code correctness tasks. Differentiate on: (a) VOTA identifies *which parts* of the trace matter (fault indicators), while LLM4PatchCorrect uses raw traces; (b) SFT vs. zero-shot; (c) different task granularity.\n\n**vs. APSG + Graph-LoRA**: Cite as concurrent work on PEFT for code correctness. Differentiate on: (a) runtime signal vs. static graph; (b) VOTA's discovery that 2 signal types suffice, vs. APSG's complex graph construction.\n\n### Emerging Trend: Selective Trace\n\nMultiple 2025-2026 papers (InspectCoder, TraceCoder, Runtime Traces + Multi-Agent Debate) converge on the same insight: **selective trace information > full trace**. VOTA should position itself within this trend while emphasizing its unique angle — the selection criterion is *decision-relevance for verdict prediction*, not general debugging utility.\n\n---\n\n## Recommended Citations to Add\n\nPapers that should be cited in the VOTA paper (if not already):\n\n1. **LLM4PatchCorrect** (TSE 2024) — closest work using execution traces for correctness assessment\n2. **REval** (2024) — empirical evidence LLMs struggle with runtime reasoning (avg 44.4%)\n3. **CodeMind** (2024) — code reasoning evaluation showing complexity-dependent degradation\n4. **FuseFL** (SANER 2024) — validates test execution outcomes as discriminative signals\n5. **CRUXEval-X** (ACL 2025) — cross-language generalization methodology reference\n6. **InspectCoder** (2025) — selective runtime inspection trend\n\n---\n\n## Key Gaps Confirmed\n\n1. **No work directly applies execution trace to binary verdict (pass/fail) prediction** — VOTA fills this gap\n2. **No work identifies fault indicator signals as near-perfect discriminative features** — VOTA's core empirical finding\n3. **Decision-relevant trace compression for LLM classification is unexplored** — VOTA's methodological contribution\n4. **Cross-model generalization of trace-based verdict prediction is unstudied** — VOTA addresses this\n\n---\n\n## Search Methodology\n\n16 query groups covering:\n- \"execution trace\" + \"fault detection\" / \"verdict prediction\" / \"test prediction\"\n- \"trace compression\" + \"code understanding\" / \"debugging\"\n- \"exception signal\" + \"fault localization\"\n- \"VOTA\" / \"trace abstraction\" / \"verdict oriented\"\n- \"CRUXEval\" + \"execution reasoning\"\n- \"patch correctness prediction\" / \"automated patch assessment\"\n- \"test outcome prediction\" / \"pass fail prediction\"\n- \"selective trace\" + \"debugging\" / \"program repair\"\n- \"code correctness prediction\" / \"classification\"\n- \"error message\" / \"exception\" + \"program repair effectiveness\"\n- Cross-model generalization + code LLM fine-tuning\n\nSources: arXiv, ACL Anthology, IEEE Xplore, Semantic Scholar, DBLP, Google Scholar\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 24_

Now update the second copy as well.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "aa619ce8-fd17-4fee-b652-3fbf431dc7c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KjheQDnpQuVRpdCS4uxw6t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3458,
      "cache_read_input_tokens": 36261,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3458
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Write · `toolu_012HReCgWWduPDaMBESaZJWD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/literature_scan_20260515/scan_report.md",
  "content": "# Literature Scan Report — VOTA (Verdict-Oriented Trace Abstraction)\n\n**Date**: 2026-05-15  \n**Target**: EMNLP 2026 Main (ARR May 25 deadline)  \n**Queries executed**: 16 search groups across arXiv, ACL Anthology, Semantic Scholar, IEEE Xplore  \n\n## Summary\n\nNo direct competitor was found that combines execution trace compression with SFT for binary verdict prediction. However, Wang et al. (EMNLP 2025 Findings) present a significant conceptual challenge: their comprehensive study of 5 trace formats for SFT concludes that semantic information from execution traces has limited usefulness. VOTA's response hinges on the distinction between raw/formatted traces and decision-relevant compression targeting fault indicator signals. The closest methodological neighbors are in **patch correctness prediction**, which shares input signal space but differs in task definition and approach.\n\n---\n\n## New Papers Found (10 additions, 16→26 total)\n\n### MEDIUM-HIGH Threat — Trace SFT Effectiveness\n\n| # | Paper | Venue | Threat | Relation to VOTA |\n|---|-------|-------|--------|-----------------|\n| 1 | **Wang et al. \"Do Code Semantics Help?\"** (Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li) | Findings of EMNLP 2025 | **MEDIUM-HIGH** | Comprehensive study testing 5 trace formats (Scratchpad, NExT, SemCoder, CodeExecutor, Concise) for SFT on code generation/repair. Conclusion: \"semantic information has limited usefulness for SFT.\" Conceptually the strongest challenge to any trace-based SFT approach including VOTA. |\n\n**Why MEDIUM-HIGH, not HIGH**: Wang et al.'s study differs from VOTA on three axes:\n- **Task**: They evaluate code generation and repair; VOTA targets verdict prediction (binary classification), a fundamentally different downstream task where trace signals serve as discriminative features rather than generative context\n- **Trace content**: All 5 formats they test preserve execution flow information (variable states, step-by-step traces); none isolates fault indicator signals (exception events, assertion comparison outcomes) — the specific signals VOTA's ablation identifies as carrying nearly all discriminative power\n- **Compression strategy**: Their \"Concise\" format is a syntactic reduction of trace verbosity; VOTA's compression is semantic, retaining only decision-relevant signals for the verdict task\n\n**Implication for VOTA paper**: This paper must be cited and directly addressed. The argument is: \"raw trace ineffective for SFT ≠ compressed fault-indicator signals ineffective for SFT.\" VOTA's component ablation (exception_only achieving 99.83%) provides the empirical counterpoint — the value is not in trace format but in isolating the right signals for the right task.\n\n### MEDIUM Threat — Patch Correctness Prediction\n\n| # | Paper | Venue | Threat | Relation to VOTA |\n|---|-------|-------|--------|-----------------|\n| 2 | **LLM4PatchCorrect** (Xin Zhou et al.) | TSE 2024 | **MEDIUM** | Uses execution traces + test cases as input for patch correctness assessment. Key difference: zero-shot prompting (no SFT), task is patch correctness (not test verdict), no trace compression. |\n| 3 | **APSG + Graph-LoRA** (arXiv 2505.02629) | arXiv 2025 | **LOW-MEDIUM** | PEFT for patch correctness with graph-structured code representation. Key difference: uses static code graph (not runtime trace), no fault indicator signals. |\n\n**Differentiation from VOTA**:\n- **Task**: Patch correctness (is this fix correct?) vs. VOTA's verdict prediction (does this test pass/fail?)\n- **Input**: LLM4PatchCorrect uses raw traces + test info; VOTA uses decision-relevant compressed signals\n- **Method**: LLM4PatchCorrect = zero-shot prompting; APSG = graph-LoRA on static graphs; VOTA = SFT with trace abstraction\n- **Signal identification**: Neither work isolates fault indicator signals or measures their individual contribution\n\n### LOW Threat — Supporting Evidence & Background\n\n| # | Paper | Venue | Category | Why Relevant |\n|---|-------|-------|----------|-------------|\n| 4 | **FuseFL** (Widyasari et al.) | SANER 2024 | code-verdict | Uses test execution outcomes (expected/actual output, errors) for fault localization. Validates that test outcome signals carry discriminative value — same intuition as VOTA, different task. |\n| 5 | **REval** (Junkai Chen et al.) | arXiv 2403.16437 | evaluation | LLM runtime behavior prediction: avg accuracy 44.4%. Supports VOTA's argument that LLMs struggle with raw trace reasoning. |\n| 6 | **CodeMind** (Changshu Liu et al.) | arXiv 2402.09664 | evaluation | Code reasoning drops with complexity (control flow, API calls). Supports trace abstraction motivation. |\n| 7 | **CRUXEval-X** (Ruiyang Xu et al.) | ACL 2025 | evaluation | Multilingual CRUXEval (19 langs). Cross-language generalization reference for VOTA's cross-model experiments. |\n| 8 | **InspectCoder** (arXiv 2510.18327) | arXiv 2025 | trace-compression | Strategic breakpoint placement + runtime state inspection for repair. Selective inspection philosophy aligns with VOTA's fault indicator extraction. |\n| 9 | **MGDebugger** (Yuling Shi et al.) | arXiv 2410.01215 | trace-compression | Hierarchical debugging with LLM-simulated execution tracking key variables. Implicit trace abstraction. |\n| 10 | **UniDebugger** (Cheryl Lee et al.) | EMNLP 2025 | debugging-agents | Multi-agent debugging without execution traces (static analysis). Orthogonal to VOTA. |\n| 11 | **Seeker** (Xuanming Zhang et al.) | ICLR 2025 | debugging-agents | Exception handling with CEE knowledge base. Exception taxonomy provides complementary perspective to VOTA's exception event signals. |\n\n---\n\n## Threat Analysis\n\n### Conceptual Threat: Wang et al. (EMNLP 2025 Findings) — MEDIUM-HIGH\n\nThis is the most important paper for VOTA to address. Their finding that \"execution trace semantic information has limited usefulness for SFT\" could be read as undermining any trace-based SFT approach. VOTA's differentiation rests on three empirical arguments:\n\n1. **Task difference**: Wang et al. study code generation/repair (open-ended generative tasks); VOTA targets binary classification (verdict prediction). Trace signals that fail to improve generation may still serve as strong discriminative features for classification.\n2. **Signal granularity**: Wang et al.'s 5 trace formats all represent execution flow at varying verbosity levels. None isolates fault indicator signals (exception type/message, assertion expected-vs-actual). VOTA's ablation shows the exception signal alone drives 99.83% accuracy — this is a qualitatively different use of trace information.\n3. **Compression semantics**: Their \"Concise\" format reduces trace tokens but preserves the same information type. VOTA's compression is task-driven: it discards execution flow and retains only signals relevant to the pass/fail decision.\n\n**Risk**: A reviewer familiar with Wang et al. may question whether VOTA is \"yet another trace SFT paper.\" The response should preemptively frame VOTA as studying *which* trace signals matter for *which* tasks, not whether traces help generically.\n\n### Methodological Threats\n\n**vs. LLM4PatchCorrect (TSE 2024) — MEDIUM**: The closest work combining execution traces with correctness assessment. Differentiation: (a) VOTA identifies *which parts* of the trace matter (fault indicators), while LLM4PatchCorrect uses uncompressed traces; (b) SFT vs. zero-shot prompting; (c) verdict prediction vs. patch correctness. LLM4PatchCorrect should be cited as evidence that execution traces contain useful signals for correctness tasks, while noting the methodological gap VOTA addresses.\n\n**vs. APSG + Graph-LoRA (arXiv 2025) — LOW-MEDIUM**: Concurrent work on PEFT for code correctness. Differentiation: (a) runtime signals vs. static code graphs; (b) VOTA's finding that 2 signal types suffice, vs. APSG's complex graph construction. The approaches are largely complementary — APSG could potentially benefit from incorporating runtime signals.\n\n### Emerging Trend: Selective Trace\n\nMultiple 2025-2026 papers (InspectCoder, TraceCoder, Runtime Traces + Multi-Agent Debate) converge on the insight that **selective trace information outperforms full traces**. VOTA aligns with this trend; its distinguishing characteristic is that the selection criterion is *decision-relevance for verdict prediction* rather than general debugging utility.\n\n---\n\n## Recommended Citations to Add\n\n1. **Wang et al. \"Do Code Semantics Help?\"** (Findings of EMNLP 2025) — must-cite; primary conceptual challenge to address\n2. **LLM4PatchCorrect** (TSE 2024) — closest work using execution traces for correctness assessment\n3. **REval** (2024) — empirical evidence LLMs struggle with runtime reasoning (avg 44.4%)\n4. **CodeMind** (2024) — code reasoning evaluation showing complexity-dependent degradation\n5. **FuseFL** (SANER 2024) — validates test execution outcomes as discriminative signals\n6. **CRUXEval-X** (ACL 2025) — cross-language generalization methodology reference\n7. **InspectCoder** (2025) — selective runtime inspection trend\n\n---\n\n## Gap Assessment\n\nBased on the current scan, the following gaps appear to hold:\n\n1. **Binary verdict prediction from execution traces**: No identified work directly applies execution trace signals to pass/fail prediction via SFT. The closest (LLM4PatchCorrect) uses zero-shot prompting for a different task (patch correctness).\n2. **Fault indicator signal isolation**: No identified work measures the individual contribution of exception events or assertion comparison signals to classification accuracy. VOTA's ablation results (exception_only at 99.83%) appear to be a novel empirical finding in this space.\n3. **Decision-relevant trace compression for LLM classification**: Existing trace compression/selection work targets program repair or debugging, not binary classification. Whether VOTA's compression strategy generalizes beyond verdict prediction is an open question.\n4. **Cross-model generalization**: Trace-based verdict prediction across different base models (Qwen, DeepSeek) has not been studied elsewhere in the surveyed literature.\n\nThese assessments are based on the 26 papers currently in the literature map. A reviewer with deeper knowledge of the software testing or mutation testing literature may identify additional related work not covered here.\n\n---\n\n## Search Methodology\n\n16 query groups covering:\n- \"execution trace\" + \"fault detection\" / \"verdict prediction\" / \"test prediction\"\n- \"trace compression\" + \"code understanding\" / \"debugging\"\n- \"exception signal\" + \"fault localization\"\n- \"VOTA\" / \"trace abstraction\" / \"verdict oriented\"\n- \"CRUXEval\" + \"execution reasoning\"\n- \"patch correctness prediction\" / \"automated patch assessment\"\n- \"test outcome prediction\" / \"pass fail prediction\"\n- \"selective trace\" + \"debugging\" / \"program repair\"\n- \"code correctness prediction\" / \"classification\"\n- \"error message\" / \"exception\" + \"program repair effectiveness\"\n- Cross-model generalization + code LLM fine-tuning\n- \"code semantics\" + \"execution trace\" + \"SFT\" (added for Wang et al. coverage)\n\nSources: arXiv, ACL Anthology, IEEE Xplore, Semantic Scholar, DBLP, Google Scholar\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "34e00ac3-778c-4722-80fc-d345889527c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KjheQDnpQuVRpdCS4uxw6t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3458,
      "cache_read_input_tokens": 36261,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3458
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T13:44:34.043Z_

<details><summary>↩ Tool result · `toolu_012HReCgWWduPDaMBESaZJWD`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/literature_scan_20260515/scan_report.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "810f6f0e-f171-4c52-aff4-aa43664d4b54",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/literature_scan_20260515/scan_report.md",
    "content": "# Literature Scan Report — VOTA (Verdict-Oriented Trace Abstraction)\n\n**Date**: 2026-05-15  \n**Target**: EMNLP 2026 Main (ARR May 25 deadline)  \n**Queries executed**: 16 search groups across arXiv, ACL Anthology, Semantic Scholar, IEEE Xplore  \n\n## Summary\n\nNo direct competitor was found that combines execution trace compression with SFT for binary verdict prediction. However, Wang et al. (EMNLP 2025 Findings) present a significant conceptual challenge: their comprehensive study of 5 trace formats for SFT concludes that semantic information from execution traces has limited usefulness. VOTA's response hinges on the distinction between raw/formatted traces and decision-relevant compression targeting fault indicator signals. The closest methodological neighbors are in **patch correctness prediction**, which shares input signal space but differs in task definition and approach.\n\n---\n\n## New Papers Found (10 additions, 16→26 total)\n\n### MEDIUM-HIGH Threat — Trace SFT Effectiveness\n\n| # | Paper | Venue | Threat | Relation to VOTA |\n|---|-------|-------|--------|-----------------|\n| 1 | **Wang et al. \"Do Code Semantics Help?\"** (Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li) | Findings of EMNLP 2025 | **MEDIUM-HIGH** | Comprehensive study testing 5 trace formats (Scratchpad, NExT, SemCoder, CodeExecutor, Concise) for SFT on code generation/repair. Conclusion: \"semantic information has limited usefulness for SFT.\" Conceptually the strongest challenge to any trace-based SFT approach including VOTA. |\n\n**Why MEDIUM-HIGH, not HIGH**: Wang et al.'s study differs from VOTA on three axes:\n- **Task**: They evaluate code generation and repair; VOTA targets verdict prediction (binary classification), a fundamentally different downstream task where trace signals serve as discriminative features rather than generative context\n- **Trace content**: All 5 formats they test preserve execution flow information (variable states, step-by-step traces); none isolates fault indicator signals (exception events, assertion comparison outcomes) — the specific signals VOTA's ablation identifies as carrying nearly all discriminative power\n- **Compression strategy**: Their \"Concise\" format is a syntactic reduction of trace verbosity; VOTA's compression is semantic, retaining only decision-relevant signals for the verdict task\n\n**Implication for VOTA paper**: This paper must be cited and directly addressed. The argument is: \"raw trace ineffective for SFT ≠ compressed fault-indicator signals ineffective for SFT.\" VOTA's component ablation (exception_only achieving 99.83%) provides the empirical counterpoint — the value is not in trace format but in isolating the right signals for the right task.\n\n### MEDIUM Threat — Patch Correctness Prediction\n\n| # | Paper | Venue | Threat | Relation to VOTA |\n|---|-------|-------|--------|-----------------|\n| 2 | **LLM4PatchCorrect** (Xin Zhou et al.) | TSE 2024 | **MEDIUM** | Uses execution traces + test cases as input for patch correctness assessment. Key difference: zero-shot prompting (no SFT), task is patch correctness (not test verdict), no trace compression. |\n| 3 | **APSG + Graph-LoRA** (arXiv 2505.02629) | arXiv 2025 | **LOW-MEDIUM** | PEFT for patch correctness with graph-structured code representation. Key difference: uses static code graph (not runtime trace), no fault indicator signals. |\n\n**Differentiation from VOTA**:\n- **Task**: Patch correctness (is this fix correct?) vs. VOTA's verdict prediction (does this test pass/fail?)\n- **Input**: LLM4PatchCorrect uses raw traces + test info; VOTA uses decision-relevant compressed signals\n- **Method**: LLM4PatchCorrect = zero-shot prompting; APSG = graph-LoRA on static graphs; VOTA = SFT with trace abstraction\n- **Signal identification**: Neither work isolates fault indicator signals or measures their individual contribution\n\n### LOW Threat — Supporting Evidence & Background\n\n| # | Paper | Venue | Category | Why Relevant |\n|---|-------|-------|----------|-------------|\n| 4 | **FuseFL** (Widyasari et al.) | SANER 2024 | code-verdict | Uses test execution outcomes (expected/actual output, errors) for fault localization. Validates that test outcome signals carry discriminative value — same intuition as VOTA, different task. |\n| 5 | **REval** (Junkai Chen et al.) | arXiv 2403.16437 | evaluation | LLM runtime behavior prediction: avg accuracy 44.4%. Supports VOTA's argument that LLMs struggle with raw trace reasoning. |\n| 6 | **CodeMind** (Changshu Liu et al.) | arXiv 2402.09664 | evaluation | Code reasoning drops with complexity (control flow, API calls). Supports trace abstraction motivation. |\n| 7 | **CRUXEval-X** (Ruiyang Xu et al.) | ACL 2025 | evaluation | Multilingual CRUXEval (19 langs). Cross-language generalization reference for VOTA's cross-model experiments. |\n| 8 | **InspectCoder** (arXiv 2510.18327) | arXiv 2025 | trace-compression | Strategic breakpoint placement + runtime state inspection for repair. Selective inspection philosophy aligns with VOTA's fault indicator extraction. |\n| 9 | **MGDebugger** (Yuling Shi et al.) | arXiv 2410.01215 | trace-compression | Hierarchical debugging with LLM-simulated execution tracking key variables. Implicit trace abstraction. |\n| 10 | **UniDebugger** (Cheryl Lee et al.) | EMNLP 2025 | debugging-agents | Multi-agent debugging without execution traces (static analysis). Orthogonal to VOTA. |\n| 11 | **Seeker** (Xuanming Zhang et al.) | ICLR 2025 | debugging-agents | Exception handling with CEE knowledge base. Exception taxonomy provides complementary perspective to VOTA's exception event signals. |\n\n---\n\n## Threat Analysis\n\n### Conceptual Threat: Wang et al. (EMNLP 2025 Findings) — MEDIUM-HIGH\n\nThis is the most important paper for VOTA to address. Their finding that \"execution trace semantic information has limited usefulness for SFT\" could be read as undermining any trace-based SFT approach. VOTA's differentiation rests on three empirical arguments:\n\n1. **Task difference**: Wang et al. study code generation/repair (open-ended generative tasks); VOTA targets binary classification (verdict prediction). Trace signals that fail to improve generation may still serve as strong discriminative features for classification.\n2. **Signal granularity**: Wang et al.'s 5 trace formats all represent execution flow at varying verbosity levels. None isolates fault indicator signals (exception type/message, assertion expected-vs-actual). VOTA's ablation shows the exception signal alone drives 99.83% accuracy — this is a qualitatively different use of trace information.\n3. **Compression semantics**: Their \"Concise\" format reduces trace tokens but preserves the same information type. VOTA's compression is task-driven: it discards execution flow and retains only signals relevant to the pass/fail decision.\n\n**Risk**: A reviewer familiar with Wang et al. may question whether VOTA is \"yet another trace SFT paper.\" The response should preemptively frame VOTA as studying *which* trace signals matter for *which* tasks, not whether traces help generically.\n\n### Methodological Threats\n\n**vs. LLM4PatchCorrect (TSE 2024) — MEDIUM**: The closest work combining execution traces with correctness assessment. Differentiation: (a) VOTA identifies *which parts* of the trace matter (fault indicators), while LLM4PatchCorrect uses uncompressed traces; (b) SFT vs. zero-shot prompting; (c) verdict prediction vs. patch correctness. LLM4PatchCorrect should be cited as evidence that execution traces contain useful signals for correctness tasks, while noting the methodological gap VOTA addresses.\n\n**vs. APSG + Graph-LoRA (arXiv 2025) — LOW-MEDIUM**: Concurrent work on PEFT for code correctness. Differentiation: (a) runtime signals vs. static code graphs; (b) VOTA's finding that 2 signal types suffice, vs. APSG's complex graph construction. The approaches are largely complementary — APSG could potentially benefit from incorporating runtime signals.\n\n### Emerging Trend: Selective Trace\n\nMultiple 2025-2026 papers (InspectCoder, TraceCoder, Runtime Traces + Multi-Agent Debate) converge on the insight that **selective trace information outperforms full traces**. VOTA aligns with this trend; its distinguishing characteristic is that the selection criterion is *decision-relevance for verdict prediction* rather than general debugging utility.\n\n---\n\n## Recommended Citations to Add\n\n1. **Wang et al. \"Do Code Semantics Help?\"** (Findings of EMNLP 2025) — must-cite; primary conceptual challenge to address\n2. **LLM4PatchCorrect** (TSE 2024) — closest work using execution traces for correctness assessment\n3. **REval** (2024) — empirical evidence LLMs struggle with runtime reasoning (avg 44.4%)\n4. **CodeMind** (2024) — code reasoning evaluation showing complexity-dependent degradation\n5. **FuseFL** (SANER 2024) — validates test execution outcomes as discriminative signals\n6. **CRUXEval-X** (ACL 2025) — cross-language generalization methodology reference\n7. **InspectCoder** (2025) — selective runtime inspection trend\n\n---\n\n## Gap Assessment\n\nBased on the current scan, the following gaps appear to hold:\n\n1. **Binary verdict prediction from execution traces**: No identified work directly applies execution trace signals to pass/fail prediction via SFT. The closest (LLM4PatchCorrect) uses zero-shot prompting for a different task (patch correctness).\n2. **Fault indicator signal isolation**: No identified work measures the individual contribution of exception events or assertion comparison signals to classification accuracy. VOTA's ablation results (exception_only at 99.83%) appear to be a novel empirical finding in this space.\n3. **Decision-relevant trace compression for LLM classification**: Existing trace compression/selection work targets program repair or debugging, not binary classification. Whether VOTA's compression strategy generalizes beyond verdict prediction is an open question.\n4. **Cross-model generalization**: Trace-based verdict prediction across different base models (Qwen, DeepSeek) has not been studied elsewhere in the surveyed literature.\n\nThese assessments are based on the 26 papers currently in the literature map. A reviewer with deeper knowledge of the software testing or mutation testing literature may identify additional related work not covered here.\n\n---\n\n## Search Methodology\n\n16 query groups covering:\n- \"execution trace\" + \"fault detection\" / \"verdict prediction\" / \"test prediction\"\n- \"trace compression\" + \"code understanding\" / \"debugging\"\n- \"exception signal\" + \"fault localization\"\n- \"VOTA\" / \"trace abstraction\" / \"verdict oriented\"\n- \"CRUXEval\" + \"execution reasoning\"\n- \"patch correctness prediction\" / \"automated patch assessment\"\n- \"test outcome prediction\" / \"pass fail prediction\"\n- \"selective trace\" + \"debugging\" / \"program repair\"\n- \"code correctness prediction\" / \"classification\"\n- \"error message\" / \"exception\" + \"program repair effectiveness\"\n- Cross-model generalization + code LLM fine-tuning\n- \"code semantics\" + \"execution trace\" + \"SFT\" (added for Wang et al. coverage)\n\nSources: arXiv, ACL Anthology, IEEE Xplore, Semantic Scholar, DBLP, Google Scholar\n",
    "structuredPatch": [
      {
        "oldStart": 6,
        "oldLines": 81,
        "newStart": 6,
        "newLines": 100,
        "lines": [
          " ",
          " ## Summary",
          " ",
          "-No **high-threat** direct competitor found. VOTA's core contribution — using fault indicator signals (exception events + assertion comparison points) from execution traces for binary verdict prediction via SFT — remains novel. The closest related works are in **patch correctness prediction**, which overlaps on input signals but differs fundamentally in task definition.",
          "+No direct competitor was found that combines execution trace compression with SFT for binary verdict prediction. However, Wang et al. (EMNLP 2025 Findings) present a significant conceptual challenge: their comprehensive study of 5 trace formats for SFT concludes that semantic information from execution traces has limited usefulness. VOTA's response hinges on the distinction between raw/formatted traces and decision-relevant compression targeting fault indicator signals. The closest methodological neighbors are in **patch correctness prediction**, which shares input signal space but differs in task definition and approach.",
          " ",
          " ---",
          " ",
          " ## New Papers Found (10 additions, 16→26 total)",
          " ",
          "-### MEDIUM Threat — Patch Correctness Prediction (Closest Competitors)",
          "+### MEDIUM-HIGH Threat — Trace SFT Effectiveness",
          " ",
          " | # | Paper | Venue | Threat | Relation to VOTA |",
          " |---|-------|-------|--------|-----------------|",
          "-| 1 | **LLM4PatchCorrect** (Xin Zhou et al.) | TSE 2024 | **MEDIUM** | Uses execution traces + test cases as input for patch correctness assessment. Key difference: zero-shot prompting (no SFT), task is patch correctness (not test verdict), no trace compression. |",
          "-| 2 | **APSG + Graph-LoRA** (arXiv 2505.02629) | arXiv 2025 | **MEDIUM** | PEFT for patch correctness with graph-structured code representation. Key difference: uses static code graph (not runtime trace), no fault indicator signals. |",
          "+| 1 | **Wang et al. \"Do Code Semantics Help?\"** (Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li) | Findings of EMNLP 2025 | **MEDIUM-HIGH** | Comprehensive study testing 5 trace formats (Scratchpad, NExT, SemCoder, CodeExecutor, Concise) for SFT on code generation/repair. Conclusion: \"semantic information has limited usefulness for SFT.\" Conceptually the strongest challenge to any trace-based SFT approach including VOTA. |",
          " ",
          "+**Why MEDIUM-HIGH, not HIGH**: Wang et al.'s study differs from VOTA on three axes:",
          "+- **Task**: They evaluate code generation and repair; VOTA targets verdict prediction (binary classification), a fundamentally different downstream task where trace signals serve as discriminative features rather than generative context",
          "+- **Trace content**: All 5 formats they test preserve execution flow information (variable states, step-by-step traces); none isolates fault indicator signals (exception events, assertion comparison outcomes) — the specific signals VOTA's ablation identifies as carrying nearly all discriminative power",
          "+- **Compression strategy**: Their \"Concise\" format is a syntactic reduction of trace verbosity; VOTA's compression is semantic, retaining only decision-relevant signals for the verdict task",
          "+",
          "+**Implication for VOTA paper**: This paper must be cited and directly addressed. The argument is: \"raw trace ineffective for SFT ≠ compressed fault-indicator signals ineffective for SFT.\" VOTA's component ablation (exception_only achieving 99.83%) provides the empirical counterpoint — the value is not in trace format but in isolating the right signals for the right task.",
          "+",
          "+### MEDIUM Threat — Patch Correctness Prediction",
          "+",
          "+| # | Paper | Venue | Threat | Relation to VOTA |",
          "+|---|-------|-------|--------|-----------------|",
          "+| 2 | **LLM4PatchCorrect** (Xin Zhou et al.) | TSE 2024 | **MEDIUM** | Uses execution traces + test cases as input for patch correctness assessment. Key difference: zero-shot prompting (no SFT), task is patch correctness (not test verdict), no trace compression. |",
          "+| 3 | **APSG + Graph-LoRA** (arXiv 2505.02629) | arXiv 2025 | **LOW-MEDIUM** | PEFT for patch correctness with graph-structured code representation. Key difference: uses static code graph (not runtime trace), no fault indicator signals. |",
          "+",
          " **Differentiation from VOTA**:",
          " - **Task**: Patch correctness (is this fix correct?) vs. VOTA's verdict prediction (does this test pass/fail?)",
          " - **Input**: LLM4PatchCorrect uses raw traces + test info; VOTA uses decision-relevant compressed signals",
          "-- **Method**: LLM4PatchCorrect = zero-shot prompting; APSG = graph-LoRA; VOTA = SFT with trace abstraction",
          "-- **Core finding**: Neither identifies fault indicator signals as near-perfect discriminative features (99.83%)",
          "+- **Method**: LLM4PatchCorrect = zero-shot prompting; APSG = graph-LoRA on static graphs; VOTA = SFT with trace abstraction",
          "+- **Signal identification**: Neither work isolates fault indicator signals or measures their individual contribution",
          " ",
          " ### LOW Threat — Supporting Evidence & Background",
          " ",
          " | # | Paper | Venue | Category | Why Relevant |",
          " |---|-------|-------|----------|-------------|",
          "-| 3 | **FuseFL** (Widyasari et al.) | SANER 2024 | code-verdict | Uses test execution outcomes (expected/actual output, errors) for fault localization. Validates that test outcome signals carry discriminative value — same intuition as VOTA, different task. |",
          "-| 4 | **REval** (Junkai Chen et al.) | arXiv 2403.16437 | evaluation | LLM runtime behavior prediction: avg accuracy 44.4%. Directly supports VOTA's argument that LLMs struggle with raw trace reasoning. |",
          "-| 5 | **CodeMind** (Changshu Liu et al.) | arXiv 2402.09664 | evaluation | Code reasoning drops with complexity (control flow, API calls). Supports trace abstraction motivation. |",
          "-| 6 | **CRUXEval-X** (Ruiyang Xu et al.) | ACL 2025 | evaluation | Multilingual CRUXEval (19 langs). Cross-language generalization reference for VOTA's cross-model experiments. |",
          "-| 7 | **InspectCoder** (arXiv 2510.18327) | arXiv 2025 | trace-compression | Strategic breakpoint placement + runtime state inspection for repair. Selective inspection philosophy aligns with VOTA's fault indicator extraction. |",
          "-| 8 | **MGDebugger** (Yuling Shi et al.) | arXiv 2410.01215 | trace-compression | Hierarchical debugging with LLM-simulated execution tracking key variables. Implicit trace abstraction. |",
          "-| 9 | **UniDebugger** (Cheryl Lee et al.) | EMNLP 2025 | debugging-agents | Multi-agent debugging without execution traces (static analysis). Orthogonal to VOTA. |",
          "-| 10 | **Seeker** (Xuanming Zhang et al.) | ICLR 2025 | debugging-agents | Exception handling with CEE knowledge base. Exception taxonomy provides complementary perspective to VOTA's exception event signals. |",
          "+| 4 | **FuseFL** (Widyasari et al.) | SANER 2024 | code-verdict | Uses test execution outcomes (expected/actual output, errors) for fault localization. Validates that test outcome signals carry discriminative value — same intuition as VOTA, different task. |",
          "+| 5 | **REval** (Junkai Chen et al.) | arXiv 2403.16437 | evaluation | LLM runtime behavior prediction: avg accuracy 44.4%. Supports VOTA's argument that LLMs struggle with raw trace reasoning. |",
          "+| 6 | **CodeMind** (Changshu Liu et al.) | arXiv 2402.09664 | evaluation | Code reasoning drops with complexity (control flow, API calls). Supports trace abstraction motivation. |",
          "+| 7 | **CRUXEval-X** (Ruiyang Xu et al.) | ACL 2025 | evaluation | Multilingual CRUXEval (19 langs). Cross-language generalization reference for VOTA's cross-model experiments. |",
          "+| 8 | **InspectCoder** (arXiv 2510.18327) | arXiv 2025 | trace-compression | Strategic breakpoint placement + runtime state inspection for repair. Selective inspection philosophy aligns with VOTA's fault indicator extraction. |",
          "+| 9 | **MGDebugger** (Yuling Shi et al.) | arXiv 2410.01215 | trace-compression | Hierarchical debugging with LLM-simulated execution tracking key variables. Implicit trace abstraction. |",
          "+| 10 | **UniDebugger** (Cheryl Lee et al.) | EMNLP 2025 | debugging-agents | Multi-agent debugging without execution traces (static analysis). Orthogonal to VOTA. |",
          "+| 11 | **Seeker** (Xuanming Zhang et al.) | ICLR 2025 | debugging-agents | Exception handling with CEE knowledge base. Exception taxonomy provides complementary perspective to VOTA's exception event signals. |",
          " ",
          " ---",
          " ",
          " ## Threat Analysis",
          " ",
          "-### No HIGH Threat Competitors",
          "+### Conceptual Threat: Wang et al. (EMNLP 2025 Findings) — MEDIUM-HIGH",
          " ",
          "-After 16 search queries, **no paper was found that**:",
          "-1. Uses execution trace fault indicator signals (exceptions + assertion comparisons) specifically for verdict prediction",
          "-2. Demonstrates that these signals alone achieve near-perfect accuracy",
          "-3. Proposes decision-relevant trace compression for binary classification via SFT",
          "+This is the most important paper for VOTA to address. Their finding that \"execution trace semantic information has limited usefulness for SFT\" could be read as undermining any trace-based SFT approach. VOTA's differentiation rests on three empirical arguments:",
          " ",
          "-### MEDIUM Threats — How to Differentiate",
          "+1. **Task difference**: Wang et al. study code generation/repair (open-ended generative tasks); VOTA targets binary classification (verdict prediction). Trace signals that fail to improve generation may still serve as strong discriminative features for classification.",
          "+2. **Signal granularity**: Wang et al.'s 5 trace formats all represent execution flow at varying verbosity levels. None isolates fault indicator signals (exception type/message, assertion expected-vs-actual). VOTA's ablation shows the exception signal alone drives 99.83% accuracy — this is a qualitatively different use of trace information.",
          "+3. **Compression semantics**: Their \"Concise\" format reduces trace tokens but preserves the same information type. VOTA's compression is task-driven: it discards execution flow and retains only signals relevant to the pass/fail decision.",
          " ",
          "-**vs. LLM4PatchCorrect**: Cite as evidence that execution traces contain useful signals for code correctness tasks. Differentiate on: (a) VOTA identifies *which parts* of the trace matter (fault indicators), while LLM4PatchCorrect uses raw traces; (b) SFT vs. zero-shot; (c) different task granularity.",
          "+**Risk**: A reviewer familiar with Wang et al. may question whether VOTA is \"yet another trace SFT paper.\" The response should preemptively frame VOTA as studying *which* trace signals matter for *which* tasks, not whether traces help generically.",
          " ",
          "-**vs. APSG + Graph-LoRA**: Cite as concurrent work on PEFT for code correctness. Differentiate on: (a) runtime signal vs. static graph; (b) VOTA's discovery that 2 signal types suffice, vs. APSG's complex graph construction.",
          "+### Methodological Threats",
          " ",
          "+**vs. LLM4PatchCorrect (TSE 2024) — MEDIUM**: The closest work combining execution traces with correctness assessment. Differentiation: (a) VOTA identifies *which parts* of the trace matter (fault indicators), while LLM4PatchCorrect uses uncompressed traces; (b) SFT vs. zero-shot prompting; (c) verdict prediction vs. patch correctness. LLM4PatchCorrect should be cited as evidence that execution traces contain useful signals for correctness tasks, while noting the methodological gap VOTA addresses.",
          "+",
          "+**vs. APSG + Graph-LoRA (arXiv 2025) — LOW-MEDIUM**: Concurrent work on PEFT for code correctness. Differentiation: (a) runtime signals vs. static code graphs; (b) VOTA's finding that 2 signal types suffice, vs. APSG's complex graph construction. The approaches are largely complementary — APSG could potentially benefit from incorporating runtime signals.",
          "+",
          " ### Emerging Trend: Selective Trace",
          " ",
          "-Multiple 2025-2026 papers (InspectCoder, TraceCoder, Runtime Traces + Multi-Agent Debate) converge on the same insight: **selective trace information > full trace**. VOTA should position itself within this trend while emphasizing its unique angle — the selection criterion is *decision-relevance for verdict prediction*, not general debugging utility.",
          "+Multiple 2025-2026 papers (InspectCoder, TraceCoder, Runtime Traces + Multi-Agent Debate) converge on the insight that **selective trace information outperforms full traces**. VOTA aligns with this trend; its distinguishing characteristic is that the selection criterion is *decision-relevance for verdict prediction* rather than general debugging utility.",
          " ",
          " ---",
          " ",
          " ## Recommended Citations to Add",
          " ",
          "-Papers that should be cited in the VOTA paper (if not already):",
          "+1. **Wang et al. \"Do Code Semantics Help?\"** (Findings of EMNLP 2025) — must-cite; primary conceptual challenge to address",
          "+2. **LLM4PatchCorrect** (TSE 2024) — closest work using execution traces for correctness assessment",
          "+3. **REval** (2024) — empirical evidence LLMs struggle with runtime reasoning (avg 44.4%)",
          "+4. **CodeMind** (2024) — code reasoning evaluation showing complexity-dependent degradation",
          "+5. **FuseFL** (SANER 2024) — validates test execution outcomes as discriminative signals",
          "+6. **CRUXEval-X** (ACL 2025) — cross-language generalization methodology reference",
          "+7. **InspectCoder** (2025) — selective runtime inspection trend",
          " ",
          "-1. **LLM4PatchCorrect** (TSE 2024) — closest work using execution traces for correctness assessment",
          "-2. **REval** (2024) — empirical evidence LLMs struggle with runtime reasoning (avg 44.4%)",
          "-3. **CodeMind** (2024) — code reasoning evaluation showing complexity-dependent degradation",
          "-4. **FuseFL** (SANER 2024) — validates test execution outcomes as discriminative signals",
          "-5. **CRUXEval-X** (ACL 2025) — cross-language generalization methodology reference",
          "-6. **InspectCoder** (2025) — selective runtime inspection trend",
          "-",
          " ---",
          " ",
          "-## Key Gaps Confirmed",
          "+## Gap Assessment",
          " ",
          "-1. **No work directly applies execution trace to binary verdict (pass/fail) prediction** — VOTA fills this gap",
          "-2. **No work identifies fault indicator signals as near-perfect discriminative features** — VOTA's core empirical finding",
          "-3. **Decision-relevant trace compression for LLM classification is unexplored** — VOTA's methodological contribution",
          "-4. **Cross-model generalization of trace-based verdict prediction is unstudied** — VOTA addresses this",
          "+Based on the current scan, the following gaps appear to hold:",
          " ",
          "+1. **Binary verdict prediction from execution traces**: No identified work directly applies execution trace signals to pass/fail prediction via SFT. The closest (LLM4PatchCorrect) uses zero-shot prompting for a different task (patch correctness).",
          "+2. **Fault indicator signal isolation**: No identified work measures the individual contribution of exception events or assertion comparison signals to classification accuracy. VOTA's ablation results (exception_only at 99.83%) appear to be a novel empirical finding in this space.",
          "+3. **Decision-relevant trace compression for LLM classification**: Existing trace compression/selection work targets program repair or debugging, not binary classification. Whether VOTA's compression strategy generalizes beyond verdict prediction is an open question.",
          "+4. **Cross-model generalization**: Trace-based verdict prediction across different base models (Qwen, DeepSeek) has not been studied elsewhere in the surveyed literature.",
          "+",
          "+These assessments are based on the 26 papers currently in the literature map. A reviewer with deeper knowledge of the software testing or mutation testing literature may identify additional related work not covered here.",
          "+",
          " ---",
          " ",
          " ## Search Methodology"
        ]
      },
      {
        "oldStart": 97,
        "oldLines": 5,
        "newStart": 116,
        "newLines": 6,
        "lines": [
          " - \"code correctness prediction\" / \"classification\"",
          " - \"error message\" / \"exception\" + \"program repair effectiveness\"",
          " - Cross-model generalization + code LLM fine-tuning",
          "+- \"code semantics\" + \"execution trace\" + \"SFT\" (added for Wang et al. coverage)",
          " ",
          " Sources: arXiv, ACL Anthology, IEEE Xplore, Semantic Scholar, DBLP, Google Scholar"
        ]
      }
    ],
    "originalFile": "# Literature Scan Report — VOTA (Verdict-Oriented Trace Abstraction)\n\n**Date**: 2026-05-15  \n**Target**: EMNLP 2026 Main (ARR May 25 deadline)  \n**Queries executed**: 16 search groups across arXiv, ACL Anthology, Semantic Scholar, IEEE Xplore  \n\n## Summary\n\nNo **high-threat** direct competitor found. VOTA's core contribution — using fault indicator signals (exception events + assertion comparison points) from execution traces for binary verdict prediction via SFT — remains novel. The closest related works are in **patch correctness prediction**, which overlaps on input signals but differs fundamentally in task definition.\n\n---\n\n## New Papers Found (10 additions, 16→26 total)\n\n### MEDIUM Threat — Patch Correctness Prediction (Closest Competitors)\n\n| # | Paper | Venue | Threat | Relation to VOTA |\n|---|-------|-------|--------|-----------------|\n| 1 | **LLM4PatchCorrect** (Xin Zhou et al.) | TSE 2024 | **MEDIUM** | Uses execution traces + test cases as input for patch correctness assessment. Key difference: zero-shot prompting (no SFT), task is patch correctness (not test verdict), no trace compression. |\n| 2 | **APSG + Graph-LoRA** (arXiv 2505.02629) | arXiv 2025 | **MEDIUM** | PEFT for patch correctness with graph-structured code representation. Key difference: uses static code graph (not runtime trace), no fault indicator signals. |\n\n**Differentiation from VOTA**:\n- **Task**: Patch correctness (is this fix correct?) vs. VOTA's verdict prediction (does this test pass/fail?)\n- **Input**: LLM4PatchCorrect uses raw traces + test info; VOTA uses decision-relevant compressed signals\n- **Method**: LLM4PatchCorrect = zero-shot prompting; APSG = graph-LoRA; VOTA = SFT with trace abstraction\n- **Core finding**: Neither identifies fault indicator signals as near-perfect discriminative features (99.83%)\n\n### LOW Threat — Supporting Evidence & Background\n\n| # | Paper | Venue | Category | Why Relevant |\n|---|-------|-------|----------|-------------|\n| 3 | **FuseFL** (Widyasari et al.) | SANER 2024 | code-verdict | Uses test execution outcomes (expected/actual output, errors) for fault localization. Validates that test outcome signals carry discriminative value — same intuition as VOTA, different task. |\n| 4 | **REval** (Junkai Chen et al.) | arXiv 2403.16437 | evaluation | LLM runtime behavior prediction: avg accuracy 44.4%. Directly supports VOTA's argument that LLMs struggle with raw trace reasoning. |\n| 5 | **CodeMind** (Changshu Liu et al.) | arXiv 2402.09664 | evaluation | Code reasoning drops with complexity (control flow, API calls). Supports trace abstraction motivation. |\n| 6 | **CRUXEval-X** (Ruiyang Xu et al.) | ACL 2025 | evaluation | Multilingual CRUXEval (19 langs). Cross-language generalization reference for VOTA's cross-model experiments. |\n| 7 | **InspectCoder** (arXiv 2510.18327) | arXiv 2025 | trace-compression | Strategic breakpoint placement + runtime state inspection for repair. Selective inspection philosophy aligns with VOTA's fault indicator extraction. |\n| 8 | **MGDebugger** (Yuling Shi et al.) | arXiv 2410.01215 | trace-compression | Hierarchical debugging with LLM-simulated execution tracking key variables. Implicit trace abstraction. |\n| 9 | **UniDebugger** (Cheryl Lee et al.) | EMNLP 2025 | debugging-agents | Multi-agent debugging without execution traces (static analysis). Orthogonal to VOTA. |\n| 10 | **Seeker** (Xuanming Zhang et al.) | ICLR 2025 | debugging-agents | Exception handling with CEE knowledge base. Exception taxonomy provides complementary perspective to VOTA's exception event signals. |\n\n---\n\n## Threat Analysis\n\n### No HIGH Threat Competitors\n\nAfter 16 search queries, **no paper was found that**:\n1. Uses execution trace fault indicator signals (exceptions + assertion comparisons) specifically for verdict prediction\n2. Demonstrates that these signals alone achieve near-perfect accuracy\n3. Proposes decision-relevant trace compression for binary classification via SFT\n\n### MEDIUM Threats — How to Differentiate\n\n**vs. LLM4PatchCorrect**: Cite as evidence that execution traces contain useful signals for code correctness tasks. Differentiate on: (a) VOTA identifies *which parts* of the trace matter (fault indicators), while LLM4PatchCorrect uses raw traces; (b) SFT vs. zero-shot; (c) different task granularity.\n\n**vs. APSG + Graph-LoRA**: Cite as concurrent work on PEFT for code correctness. Differentiate on: (a) runtime signal vs. static graph; (b) VOTA's discovery that 2 signal types suffice, vs. APSG's complex graph construction.\n\n### Emerging Trend: Selective Trace\n\nMultiple 2025-2026 papers (InspectCoder, TraceCoder, Runtime Traces + Multi-Agent Debate) converge on the same insight: **selective trace information > full trace**. VOTA should position itself within this trend while emphasizing its unique angle — the selection criterion is *decision-relevance for verdict prediction*, not general debugging utility.\n\n---\n\n## Recommended Citations to Add\n\nPapers that should be cited in the VOTA paper (if not already):\n\n1. **LLM4PatchCorrect** (TSE 2024) — closest work using execution traces for correctness assessment\n2. **REval** (2024) — empirical evidence LLMs struggle with runtime reasoning (avg 44.4%)\n3. **CodeMind** (2024) — code reasoning evaluation showing complexity-dependent degradation\n4. **FuseFL** (SANER 2024) — validates test execution outcomes as discriminative signals\n5. **CRUXEval-X** (ACL 2025) — cross-language generalization methodology reference\n6. **InspectCoder** (2025) — selective runtime inspection trend\n\n---\n\n## Key Gaps Confirmed\n\n1. **No work directly applies execution trace to binary verdict (pass/fail) prediction** — VOTA fills this gap\n2. **No work identifies fault indicator signals as near-perfect discriminative features** — VOTA's core empirical finding\n3. **Decision-relevant trace compression for LLM classification is unexplored** — VOTA's methodological contribution\n4. **Cross-model generalization of trace-based verdict prediction is unstudied** — VOTA addresses this\n\n---\n\n## Search Methodology\n\n16 query groups covering:\n- \"execution trace\" + \"fault detection\" / \"verdict prediction\" / \"test prediction\"\n- \"trace compression\" + \"code understanding\" / \"debugging\"\n- \"exception signal\" + \"fault localization\"\n- \"VOTA\" / \"trace abstraction\" / \"verdict oriented\"\n- \"CRUXEval\" + \"execution reasoning\"\n- \"patch correctness prediction\" / \"automated patch assessment\"\n- \"test outcome prediction\" / \"pass fail prediction\"\n- \"selective trace\" + \"debugging\" / \"program repair\"\n- \"code correctness prediction\" / \"classification\"\n- \"error message\" / \"exception\" + \"program repair effectiveness\"\n- Cross-model generalization + code LLM fine-tuning\n\nSources: arXiv, ACL Anthology, IEEE Xplore, Semantic Scholar, DBLP, Google Scholar\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 27_

两份 scan_report.md 已同步更新。主要变更：

1. **Wang et al. (EMNLP 2025 Findings) 作为 MEDIUM-HIGH threat 加入** — 独立小节详细分析三个差异轴（task/signal granularity/compression semantics），并给出 VOTA paper 的回应策略
2. **APSG 降级为 LOW-MEDIUM**（静态图，非 runtime trace）
3. **所有断言性措辞已替换**：
   - "remains novel" → 删除
   - "fills this gap" → "no identified work directly applies..."
   - "VOTA's core empirical finding" → "appear to be a novel empirical finding"
   - "Key Gaps Confirmed" → "Gap Assessment" + 加了 caveat 说明基于当前 26 篇文献的局限性
4. **Recommended Citations** 首位改为 Wang et al.（must-cite）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "uuid": "31924754-5d4b-43be-b625-20a6b18ebe0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kJGhKCvdFLe7R7hDcPRF5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3117,
      "cache_read_input_tokens": 39719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3117
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 28_

两份 scan_report.md 已同步更新。主要变更：

1. **Wang et al. (EMNLP 2025 Findings) 作为 MEDIUM-HIGH threat 加入** — 独立小节详细分析三个差异轴（task/signal granularity/compression semantics），并给出 VOTA paper 的回应策略
2. **APSG 降级为 LOW-MEDIUM**（静态图，非 runtime trace）
3. **所有断言性措辞已替换**：
   - "remains novel" → 删除
   - "fills this gap" → "no identified work directly applies..."
   - "VOTA's core empirical finding" → "appear to be a novel empirical finding"
   - "Key Gaps Confirmed" → "Gap Assessment" + 加了 caveat 说明基于当前 26 篇文献的局限性
4. **Recommended Citations** 首位改为 Wang et al.（must-cite）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 105038,
  "duration_api_ms": 106058,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "d2887f5f-9f05-4a7f-bd3d-6bb97265ace6",
  "total_cost_usd": 0.46048125000000006,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 30995,
    "cache_read_input_tokens": 166755,
    "output_tokens": 7278,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 30995,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 257,
        "cache_read_input_tokens": 39719,
        "cache_creation_input_tokens": 3117,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3117
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1290,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001385,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 7278,
      "cacheReadInputTokens": 166755,
      "cacheCreationInputTokens": 30995,
      "webSearchRequests": 0,
      "costUSD": 0.45909625,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "2b4533f6-0306-4ac4-a771-72e2fd6d987a"
}
```

</details>

---
