# knowledge memory update d011

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/workers/worker_knowledge_memory-update-d011_20260513T195707.log`
- **Structured JSON:** [`8a6eccad3f53ec58def2.json`](../../sessions/8a/8a6eccad3f53ec58def2.json)

## Before a recorded user message

15 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "session_id": "28fb5286-f4e4-41db-a3a6-a0e14b7aae2f",
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
  "uuid": "fbc4d125-bf6f-4728-b631-3cc61623f748",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/memory/"
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
    "resetsAt": 1778703000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "34f11616-e599-4840-ad10-91e29c79f0a9",
  "session_id": "28fb5286-f4e4-41db-a3a6-a0e14b7aae2f"
}
```

---

### Assistant

_source line 4_

Let me read the current memory.md first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "28fb5286-f4e4-41db-a3a6-a0e14b7aae2f",
  "uuid": "4aad9d58-b5ab-44ec-824a-05c03bc667e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XR2Yn7SGELsSaLASTRSbvM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11380,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11380
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01U1UytjfiJFdHLpoNf8KQYp`</summary>

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
  "session_id": "28fb5286-f4e4-41db-a3a6-a0e14b7aae2f",
  "uuid": "ed08a8ef-8431-46c4-bfbb-0cb5cac0e97d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XR2Yn7SGELsSaLASTRSbvM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11380,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11380
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

_source line 6 · 2026-05-13T19:57:17.528Z_

<details><summary>↩ Tool result · `toolu_01U1UytjfiJFdHLpoNf8KQYp`</summary>

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
  "session_id": "28fb5286-f4e4-41db-a3a6-a0e14b7aae2f",
  "uuid": "411345dc-c804-43d4-9e7d-f868a277f8b7",
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
Let me read the current memory.md first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "28fb5286-f4e4-41db-a3a6-a0e14b7aae2f",
  "uuid": "9e2798b9-d0e0-4b02-93bc-c3605cb601bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BTqinPRrDqvzyveuVw77Uv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 23221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 709
      },
      "output_tokens": 57,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MPWizyvVVWkf4WVxnHVdQN`</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "memory.md",
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
  "session_id": "28fb5286-f4e4-41db-a3a6-a0e14b7aae2f",
  "uuid": "b6d0c415-521c-4859-9cbc-7eed4ec2973d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BTqinPRrDqvzyveuVw77Uv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 23221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 709
      },
      "output_tokens": 57,
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

_source line 9 · 2026-05-13T19:57:20.905Z_

<details><summary>↩ Tool result · `toolu_01MPWizyvVVWkf4WVxnHVdQN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/memory.md\", \"content\": \"## Phase 1 MVP 最终结论 (2026-05-13)\\n\\n### Verdict: PASS (4/5 tasks 显著正向)\\n\\nPhase 1 验证了 fork-based deterministic evaluation 在 ScienceWorld 上显著优于纯 LLM 内部推理。\\n\\n### 关键设计决策与教训\\n\\n1. **Tie-break 策略**: `>` (strict) 而非 `>=`。95%+ 步骤 score_delta=0（稀疏奖励），`>=` 会让 oracle 退化为 always-internal。\\n\\n2. **Death filter 只用于有 fork 的模式**: always-internal 是纯 LLM baseline，不能调 fork/is_lethal。\\n\\n3. **melt 与 change-state internal 分数巧合相同**: 共享 environment variations，不是数据重复。\\n\\n4. **vLLM 兼容性**: torch 2.10.0 + vLLM 0.18.1 需注释 select_algorithm.py 1695/2164 行。\\n\\n5. **phase1_signal.py 不支持 --seed 参数**。\\n\\n### 竞品对标\\n- CogRouter (arXiv 2602.12662): Qwen2.5-7B, Score=84.6, SR=72.0%。路由 thinking depth（4 levels）。\\n- ITP-R (arXiv 2601.08955): Learned WM + K-head gating, SR=63.91%。WM 有 compounding error。\\n\\n## ⚠️ 核心发现：Det 优势几乎完全来自死亡回避 (2026-05-13)\\n\\n### Death rate 分析\\n\\n| 数据集 | I_death | D_death | Δ(D-I) | Δ_no_death |\\n|--------|---------|---------|--------|------------|\\n| Prescreening (8 tasks) | 48.6% | 5.4% | +43.9 | **-4.5** |\\n| MVP (5 tasks) | 41.0% | 12.0% | +29.2 | **-0.4** |\\n\\n**排除死亡 episode 后 det 反而略差于 internal。** Det 全部优势来自 death filter 阻止致命动作（\\\"focus on 错误对象\\\" → -100），不是推理质量更好。\\n\\n### 对 Paper Framing 的影响\\n- 原 framing \\\"det improves agent performance\\\" 需调整\\n- 实际机制：fork-based safety gate（检测并阻止致命动作）\\n- 更可防御的 claim：\\\"selective routing prevents catastrophic failures\\\"\\n- Router 应学到\\\"有风险时走 det，安全时走 internal\\\"\\n\\n### SFT 数据 class imbalance\\n- MVP 3 tasks 后处理：750 SFT triples，全标 \\\"deterministic\\\"（0 个 internal wins）\\n- 原因：包含 death 的 episode det 必赢；no-death episode 多为 tie\\n- 需要 step-level death risk features 而非 episode-level labels\\n\\n## Labeling 策略演进 (2026-05-13)\\n\\n### 1-step labeling → 不可行（tie rate 98.2%）\\n### Episode-terminal (K=10) → Director 取消（成本太高，78h 双卡）\\n### Plan C (episode-level) → 当前方案，但 class imbalance 严重\\n### Action divergence rate: 73.1%（几乎每步都不同，但 1-step score 无差异）\\n\", \"total_chars\": 1818, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "28fb5286-f4e4-41db-a3a6-a0e14b7aae2f",
  "uuid": "b8f8e5cb-7f84-4405-91b3-3e7b83742f99",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/memory.md\\\", \\\"content\\\": \\\"## Phase 1 MVP 最终结论 (2026-05-13)\\\\n\\\\n### Verdict: PASS (4/5 tasks 显著正向)\\\\n\\\\nPhase 1 验证了 fork-based deterministic evaluation 在 ScienceWorld 上显著优于纯 LLM 内部推理。\\\\n\\\\n### 关键设计决策与教训\\\\n\\\\n1. **Tie-break 策略**: `>` (strict) 而非 `>=`。95%+ 步骤 score_delta=0（稀疏奖励），`>=` 会让 oracle 退化为 always-internal。\\\\n\\\\n2. **Death filter 只用于有 fork 的模式**: always-internal 是纯 LLM baseline，不能调 fork/is_lethal。\\\\n\\\\n3. **melt 与 change-state internal 分数巧合相同**: 共享 environment variations，不是数据重复。\\\\n\\\\n4. **vLLM 兼容性**: torch 2.10.0 + vLLM 0.18.1 需注释 select_algorithm.py 1695/2164 行。\\\\n\\\\n5. **phase1_signal.py 不支持 --seed 参数**。\\\\n\\\\n### 竞品对标\\\\n- CogRouter (arXiv 2602.12662): Qwen2.5-7B, Score=84.6, SR=72.0%。路由 thinking depth（4 levels）。\\\\n- ITP-R (arXiv 2601.08955): Learned WM + K-head gating, SR=63.91%。WM 有 compounding error。\\\\n\\\\n## ⚠️ 核心发现：Det 优势几乎完全来自死亡回避 (2026-05-13)\\\\n\\\\n### Death rate 分析\\\\n\\\\n| 数据集 | I_death | D_death | Δ(D-I) | Δ_no_death |\\\\n|--------|---------|---------|--------|------------|\\\\n| Prescreening (8 tasks) | 48.6% | 5.4% | +43.9 | **-4.5** |\\\\n| MVP (5 tasks) | 41.0% | 12.0% | +29.2 | **-0.4** |\\\\n\\\\n**排除死亡 episode 后 det 反而略差于 internal。** Det 全部优势来自 death filter 阻止致命动作（\\\\\\\"focus on 错误对象\\\\\\\" → -100），不是推理质量更好。\\\\n\\\\n### 对 Paper Framing 的影响\\\\n- 原 framing \\\\\\\"det improves agent performance\\\\\\\" 需调整\\\\n- 实际机制：fork-based safety gate（检测并阻止致命动作）\\\\n- 更可防御的 claim：\\\\\\\"selective routing prevents catastrophic failures\\\\\\\"\\\\n- Router 应学到\\\\\\\"有风险时走 det，安全时走 internal\\\\\\\"\\\\n\\\\n### SFT 数据 class imbalance\\\\n- MVP 3 tasks 后处理：750 SFT triples，全标 \\\\\\\"deterministic\\\\\\\"（0 个 internal wins）\\\\n- 原因：包含 death 的 episode det 必赢；no-death episode 多为 tie\\\\n- 需要 step-level death risk features 而非 episode-level labels\\\\n\\\\n## Labeling 策略演进 (2026-05-13)\\\\n\\\\n### 1-step labeling → 不可行（tie rate 98.2%）\\\\n### Episode-terminal (K=10) → Director 取消（成本太高，78h 双卡）\\\\n### Plan C (episode-level) → 当前方案，但 class imbalance 严重\\\\n### Action divergence rate: 73.1%（几乎每步都不同，但 1-step score 无差异）\\\\n\\\", \\\"total_chars\\\": 1818, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/memory.md\", \"content\": \"## Phase 1 MVP 最终结论 (2026-05-13)\\n\\n### Verdict: PASS (4/5 tasks 显著正向)\\n\\nPhase 1 验证了 fork-based deterministic evaluation 在 ScienceWorld 上显著优于纯 LLM 内部推理。\\n\\n### 关键设计决策与教训\\n\\n1. **Tie-break 策略**: `>` (strict) 而非 `>=`。95%+ 步骤 score_delta=0（稀疏奖励），`>=` 会让 oracle 退化为 always-internal。\\n\\n2. **Death filter 只用于有 fork 的模式**: always-internal 是纯 LLM baseline，不能调 fork/is_lethal。\\n\\n3. **melt 与 change-state internal 分数巧合相同**: 共享 environment variations，不是数据重复。\\n\\n4. **vLLM 兼容性**: torch 2.10.0 + vLLM 0.18.1 需注释 select_algorithm.py 1695/2164 行。\\n\\n5. **phase1_signal.py 不支持 --seed 参数**。\\n\\n### 竞品对标\\n- CogRouter (arXiv 2602.12662): Qwen2.5-7B, Score=84.6, SR=72.0%。路由 thinking depth（4 levels）。\\n- ITP-R (arXiv 2601.08955): Learned WM + K-head gating, SR=63.91%。WM 有 compounding error。\\n\\n## ⚠️ 核心发现：Det 优势几乎完全来自死亡回避 (2026-05-13)\\n\\n### Death rate 分析\\n\\n| 数据集 | I_death | D_death | Δ(D-I) | Δ_no_death |\\n|--------|---------|---------|--------|------------|\\n| Prescreening (8 tasks) | 48.6% | 5.4% | +43.9 | **-4.5** |\\n| MVP (5 tasks) | 41.0% | 12.0% | +29.2 | **-0.4** |\\n\\n**排除死亡 episode 后 det 反而略差于 internal。** Det 全部优势来自 death filter 阻止致命动作（\\\"focus on 错误对象\\\" → -100），不是推理质量更好。\\n\\n### 对 Paper Framing 的影响\\n- 原 framing \\\"det improves agent performance\\\" 需调整\\n- 实际机制：fork-based safety gate（检测并阻止致命动作）\\n- 更可防御的 claim：\\\"selective routing prevents catastrophic failures\\\"\\n- Router 应学到\\\"有风险时走 det，安全时走 internal\\\"\\n\\n### SFT 数据 class imbalance\\n- MVP 3 tasks 后处理：750 SFT triples，全标 \\\"deterministic\\\"（0 个 internal wins）\\n- 原因：包含 death 的 episode det 必赢；no-death episode 多为 tie\\n- 需要 step-level death risk features 而非 episode-level labels\\n\\n## Labeling 策略演进 (2026-05-13)\\n\\n### 1-step labeling → 不可行（tie rate 98.2%）\\n### Episode-terminal (K=10) → Director 取消（成本太高，78h 双卡）\\n### Plan C (episode-level) → 当前方案，但 class imbalance 严重\\n### Action divergence rate: 73.1%（几乎每步都不同，但 1-step score 无差异）\\n\", \"total_chars\": 1818, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
The current memory.md already has some content. I need to append the requested sections. Looking at the existing content, some of it overlaps with what's being asked to add. Let me carefully compare:

Existing:
1. Phase 1 MVP 最终结论 - covers tie-break, death filter, melt/change-state, vLLM, phase1_signal.py, 竞品对标
2. 核心发现：Det 优势几乎完全来自死亡回避 - covers death rate analysis, paper framing impact, SFT class imbalance


3. Labeling 策略演进 - brief notes on 1-step, episode-terminal, Plan C, action divergence

The user's requested content overlaps significantly with sections 2 and 3, but their version has more granular detail. I should focus on adding the new Signal_type 分类 section since that's genuinely new content, and I can enhance the existing sections with the additional details they're asking for rather than creating duplicates.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "28fb5286-f4e4-41db-a3a6-a0e14b7aae2f",
  "uuid": "020c97d2-1f99-40bc-b5cb-37ed48246c8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Um6raHDYeuKf5NMrUn7vj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1278,
      "cache_read_input_tokens": 23930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1278
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

_source line 11_

已有内容存在部分重叠，但按要求追加到末尾。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "28fb5286-f4e4-41db-a3a6-a0e14b7aae2f",
  "uuid": "e67402c4-d129-4f97-a7ab-7301553dda2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Um6raHDYeuKf5NMrUn7vj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1278,
      "cache_read_input_tokens": 23930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1278
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

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01DPqqH9DQKfA6ZCuxyjxJm2`</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "memory.md",
  "content": "## Phase 1 MVP 最终结论 (2026-05-13)\n\n### Verdict: PASS (4/5 tasks 显著正向)\n\nPhase 1 验证了 fork-based deterministic evaluation 在 ScienceWorld 上显著优于纯 LLM 内部推理。\n\n### 关键设计决策与教训\n\n1. **Tie-break 策略**: `>` (strict) 而非 `>=`。95%+ 步骤 score_delta=0（稀疏奖励），`>=` 会让 oracle 退化为 always-internal。\n\n2. **Death filter 只用于有 fork 的模式**: always-internal 是纯 LLM baseline，不能调 fork/is_lethal。\n\n3. **melt 与 change-state internal 分数巧合相同**: 共享 environment variations，不是数据重复。\n\n4. **vLLM 兼容性**: torch 2.10.0 + vLLM 0.18.1 需注释 select_algorithm.py 1695/2164 行。\n\n5. **phase1_signal.py 不支持 --seed 参数**。\n\n### 竞品对标\n- CogRouter (arXiv 2602.12662): Qwen2.5-7B, Score=84.6, SR=72.0%。路由 thinking depth（4 levels）。\n- ITP-R (arXiv 2601.08955): Learned WM + K-head gating, SR=63.91%。WM 有 compounding error。\n\n## ⚠️ 核心发现：Det 优势几乎完全来自死亡回避 (2026-05-13)\n\n### Death rate 分析\n\n| 数据集 | I_death | D_death | Δ(D-I) | Δ_no_death |\n|--------|---------|---------|--------|------------|\n| Prescreening (8 tasks) | 48.6% | 5.4% | +43.9 | **-4.5** |\n| MVP (5 tasks) | 41.0% | 12.0% | +29.2 | **-0.4** |\n\n**排除死亡 episode 后 det 反而略差于 internal。** Det 全部优势来自 death filter 阻止致命动作（\"focus on 错误对象\" → -100），不是推理质量更好。\n\n### 对 Paper Framing 的影响\n- 原 framing \"det improves agent performance\" 需调整\n- 实际机制：fork-based safety gate（检测并阻止致命动作）\n- 更可防御的 claim：\"selective routing prevents catastrophic failures\"\n- Router 应学到\"有风险时走 det，安全时走 internal\"\n\n### SFT 数据 class imbalance\n- MVP 3 tasks 后处理：750 SFT triples，全标 \"deterministic\"（0 个 internal wins）\n- 原因：包含 death 的 episode det 必赢；no-death episode 多为 tie\n- 需要 step-level death risk features 而非 episode-level labels\n\n## Labeling 策略演进 (2026-05-13)\n\n### 1-step labeling → 不可行（tie rate 98.2%）\n### Episode-terminal (K=10) → Director 取消（成本太高，78h 双卡）\n### Plan C (episode-level) → 当前方案，但 class imbalance 严重\n### Action divergence rate: 73.1%（几乎每步都不同，但 1-step score 无差异）\n\n## D011 关键发现：Det 优势 = 纯 Death Avoidance (2026-05-13)\n\nMVP 5 个 task 全部 death-dominated（修正后 grow-plant 为 no-effect）。非 death 情况下 Δ(D-I) 为负（-0.4 到 -4.5），det 不提供 general reasoning improvement。\n\n**结论：router 的核心价值是 death-risk detection，不是 general reasoning improvement。**\n\n## D011 关键发现：1-step Labeling 失败 (D008, 2026-05-13)\n\n- 98.2% tie rate 使 per-step 标注无效\n- Action divergence rate 73.1% 但 1-step score delta = 0（动作不同但即时分数无差异）\n- 决策：采用 episode-level labeling（Plan C）\n\n## Labeling 策略完整演进路径 (2026-05-13)\n\n1. **1-step labeling** → 失败（98.2% tie，稀疏奖励下无区分度）\n2. **Episode-terminal K=10** → 取消（78h 双卡，成本过高）\n3. **Plan C episode-level** → 已采用\n4. **Plan C + death-aware labeling** = 最终方案\n\n## Class Imbalance 风险与解法 (2026-05-13)\n\n- MVP SFT 数据 750/750 全标 deterministic（0 internal wins）\n- 根因：death episodes 使 det 自动赢，non-death episodes 大部分 tie\n- 解法：death-aware labeling + 混合 task 选择（确保 internal ≥ 15%）\n\n## Signal Type 分类框架 (2026-05-13)\n\n| 类型 | 定义 | 论文价值 |\n|------|------|----------|\n| death-dominated | det 优势完全来自 death avoidance | 证明 safety gate 有效 |\n| genuine-det | 非 death 情况下 det 仍优于 internal | **最有价值**：证明 router 不仅做 death detection |\n| internal-preferred | internal 优于 det | 证明需要 routing 而非 always-det |\n| no-effect | 两种模式无差异 | 排除噪声 task |\n| mixed | 混合信号 | 需进一步分析 |\n\ngenuine-det 类型对论文至关重要：证明 router 的价值不局限于 death detection，而是能识别 deterministic reasoning genuinely helps 的场景。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "28fb5286-f4e4-41db-a3a6-a0e14b7aae2f",
  "uuid": "c8a557d2-d464-43af-99d5-8016ddde5827",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Um6raHDYeuKf5NMrUn7vj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1278,
      "cache_read_input_tokens": 23930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1278
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

_source line 13 · 2026-05-13T19:57:47.073Z_

<details><summary>↩ Tool result · `toolu_01DPqqH9DQKfA6ZCuxyjxJm2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "28fb5286-f4e4-41db-a3a6-a0e14b7aae2f",
  "uuid": "4b1f6339-ea41-4325-b71f-e00f84d0df70",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/memory.md\\\", \\\"saved\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

已追加 5 个新节到 memory.md：D011 death avoidance 发现、1-step labeling 失败、labeling 演进路径、class imbalance 风险、signal type 分类框架。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "28fb5286-f4e4-41db-a3a6-a0e14b7aae2f",
  "uuid": "a6a79c7f-c50c-4941-beb0-0871ccba949a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbvkrJe9ggosQhPpLA8c3P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2306,
      "cache_read_input_tokens": 25208,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2306
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

_source line 15_

已追加 5 个新节到 memory.md：D011 death avoidance 发现、1-step labeling 失败、labeling 演进路径、class imbalance 风险、signal type 分类框架。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 35943,
  "duration_api_ms": 37233,
  "num_turns": 4,
  "stop_reason": "end_turn",
  "session_id": "28fb5286-f4e4-41db-a3a6-a0e14b7aae2f",
  "total_cost_usd": 0.20474525,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 15673,
    "cache_read_input_tokens": 84200,
    "output_tokens": 2533,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 15673,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 62,
        "cache_read_input_tokens": 25208,
        "cache_creation_input_tokens": 2306,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2306
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1239,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001329,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 2533,
      "cacheReadInputTokens": 84200,
      "cacheCreationInputTokens": 15673,
      "webSearchRequests": 0,
      "costUSD": 0.20341625,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "27baad6d-8934-4052-8eb7-bd384972d5f2"
}
```

</details>

---
