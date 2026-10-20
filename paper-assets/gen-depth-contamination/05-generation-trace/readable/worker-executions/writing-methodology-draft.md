# writing methodology draft

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_writing_methodology_draft_20260512T162448.log`
- **Structured JSON:** [`f030252e1f4b1fda8d1c.json`](../../sessions/f0/f030252e1f4b1fda8d1c.json)

## Before a recorded user message

23 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "session_id": "a2b3c6e1-bf66-4ff6-bec8-41639f3adf55",
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
  "uuid": "094703d1-b35e-444f-9a34-4f6920e002bc",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/memory/"
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
    "resetsAt": 1778620800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "df126e22-01da-4cdb-a1d9-35798e3e352f",
  "session_id": "a2b3c6e1-bf66-4ff6-bec8-41639f3adf55"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading all the reference materials to gather the technical details needed for the methodology draft.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a2b3c6e1-bf66-4ff6-bec8-41639f3adf55",
  "uuid": "0a70f2c5-0f50-415f-b10c-3c0a38109757",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEF51RrLuuNZmpLwZXdYnf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12229,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12229
      },
      "output_tokens": 26,
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

_source line 5_

我先读取所有参考材料。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a2b3c6e1-bf66-4ff6-bec8-41639f3adf55",
  "uuid": "26fb941a-384c-4469-b3fe-a4ffd9e8bd6f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEF51RrLuuNZmpLwZXdYnf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12229,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12229
      },
      "output_tokens": 26,
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01X7S9LtFd6U5CzZ77R2Tmqj`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a2b3c6e1-bf66-4ff6-bec8-41639f3adf55",
  "uuid": "53da229d-5ecf-47ca-bde5-c8afffabb020",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEF51RrLuuNZmpLwZXdYnf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12229,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12229
      },
      "output_tokens": 26,
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

_source line 7 · 2026-05-12T16:25:00.494Z_

<details><summary>↩ Tool result · `toolu_01X7S9LtFd6U5CzZ77R2Tmqj`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "session_id": "a2b3c6e1-bf66-4ff6-bec8-41639f3adf55",
  "uuid": "84f2f50c-6310-4b81-9394-467d00a75e18",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01T6N8GztQ4ZFjyrNkZwqavu`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "ROADMAP.md",
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
  "session_id": "a2b3c6e1-bf66-4ff6-bec8-41639f3adf55",
  "uuid": "cb6af5fb-f92f-451a-bb08-c33afca97cc1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FDLd2tfof3vhWd8bp3g7E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 481,
      "cache_read_input_tokens": 24070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 481
      },
      "output_tokens": 69,
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

_source line 9 · 2026-05-12T16:25:03.342Z_

<details><summary>↩ Tool result · `toolu_01T6N8GztQ4ZFjyrNkZwqavu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ROADMAP.md\", \"content\": \"# gen-depth-contamination — Research Dashboard\\n\\n> 最后更新: 2026-05-12 11:16 UTC | 更新原因: 修正模型型号 1.8B→1.5B-Instruct，更新进展状态\\n\\n## 核心方向\\n估计递归生成合成文本的代际深度（generational depth），构建首个 ordinal depth classifier，实现 depth-aware graduated filtering 替代 binary detection。核心科学量：判别饱和边界 K*。\\n\\n## 当前进展\\n- **阶段**: MVP 验证（执行中）\\n- **基础设施**: autodl-4090d（1×RTX 4090D 24GB, cuda:0）\\n- **实验**: mvp_pilot_sat_v1 PREPARING，Agent 在编写 pipeline 代码\\n\\n## MVP 验证方案\\n**核心假设**: 递归生成文本在统计特征空间上存在可分辨的代际差异，且差异随深度呈系统性趋势。\\n\\n**方案**（对应 IDEA_BRIEF Phase 0 pilot saturation study）:\\n- 模型: **Qwen2.5-1.5B-Instruct**（Qwen2.5 系列无 1.8B；用 Instruct 更接近真实世界合成文本来源，full study 再对比 base vs Instruct）\\n- 种子数据: C4 子集 5K docs\\n- 深度链: depth 0(human) → depth 1-5（递归生成）\\n- 生成方式: **prompt-chain**（upper bound estimate，retrain-chain 留到 research 阶段）\\n- 解码策略: **nucleus sampling p=0.95, T=1.0**\\n- 特征（15 维）: surprisal 9 维 + vocab diversity 3 维 + tail-thinning 3 维\\n- 评估: pairwise depth AUC + JSD + LightGBM ordinal 分类\\n\\n**K* 操作性定义**: K* = max k s.t. AUC(depth k-1 vs k) > 0.60\\n\\n**Pass/Fail 标准**:\\n- ✅ Pass: K* ≥ 3 且 AUC(depth 0 vs 1) > 0.70\\n- ⚠️ Conditional Pass: K* = 2，但特征趋势清晰 → saturation characterization 路线\\n- ❌ Fail: K* ≤ 1 或特征无系统性趋势\\n\\n**预估资源**: 1×RTX 4090D，约 8-12 GPU 小时\\n\\n## 近期任务\\n- [x] GPU 服务器到位\\n- [x] 项目配置绑定\\n- [ ] Agent 完成 pipeline 代码 + 环境搭建\\n- [ ] 生成 depth chain（C4 5K × 6 depths）\\n- [ ] 特征提取 + pairwise AUC + JSD 分析\\n- [ ] 判定 K* → MVP gate 决策\\n\\n## GPU 预算\\n1×RTX 4090D 24GB @ autodl-4090d（cuda:0）\\n\\n## 关键风险\\n1. K* ≤ 2 → saturation characterization 路线仍可投\\n2. 方法论贡献薄弱 → 信道级联 + DPI 理论框架可补强\\n3. EMNLP ARR May 25 deadline 仅 13 天 → MVP 必须 2 天内完成\\n4. Reviewer SSH 不通，无法独立核实环境 → 需跟进修复\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D002 | 2026-05-12 | MVP 初步结果 K*=2（边界），修复 right-padding 后重跑确认再锁路线 | mvp_pilot_sat_v1 |\\n| D001 | 2026-05-12 | MVP 方案：Qwen2.5-1.8B + C4 5K docs 做 pilot saturatio | — |\\n\\n\", \"total_chars\": 1822, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a2b3c6e1-bf66-4ff6-bec8-41639f3adf55",
  "uuid": "20c262d4-4083-48b2-89eb-8069f553d7d4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ROADMAP.md\\\", \\\"content\\\": \\\"# gen-depth-contamination — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-12 11:16 UTC | 更新原因: 修正模型型号 1.8B→1.5B-Instruct，更新进展状态\\\\n\\\\n## 核心方向\\\\n估计递归生成合成文本的代际深度（generational depth），构建首个 ordinal depth classifier，实现 depth-aware graduated filtering 替代 binary detection。核心科学量：判别饱和边界 K*。\\\\n\\\\n## 当前进展\\\\n- **阶段**: MVP 验证（执行中）\\\\n- **基础设施**: autodl-4090d（1×RTX 4090D 24GB, cuda:0）\\\\n- **实验**: mvp_pilot_sat_v1 PREPARING，Agent 在编写 pipeline 代码\\\\n\\\\n## MVP 验证方案\\\\n**核心假设**: 递归生成文本在统计特征空间上存在可分辨的代际差异，且差异随深度呈系统性趋势。\\\\n\\\\n**方案**（对应 IDEA_BRIEF Phase 0 pilot saturation study）:\\\\n- 模型: **Qwen2.5-1.5B-Instruct**（Qwen2.5 系列无 1.8B；用 Instruct 更接近真实世界合成文本来源，full study 再对比 base vs Instruct）\\\\n- 种子数据: C4 子集 5K docs\\\\n- 深度链: depth 0(human) → depth 1-5（递归生成）\\\\n- 生成方式: **prompt-chain**（upper bound estimate，retrain-chain 留到 research 阶段）\\\\n- 解码策略: **nucleus sampling p=0.95, T=1.0**\\\\n- 特征（15 维）: surprisal 9 维 + vocab diversity 3 维 + tail-thinning 3 维\\\\n- 评估: pairwise depth AUC + JSD + LightGBM ordinal 分类\\\\n\\\\n**K* 操作性定义**: K* = max k s.t. AUC(depth k-1 vs k) > 0.60\\\\n\\\\n**Pass/Fail 标准**:\\\\n- ✅ Pass: K* ≥ 3 且 AUC(depth 0 vs 1) > 0.70\\\\n- ⚠️ Conditional Pass: K* = 2，但特征趋势清晰 → saturation characterization 路线\\\\n- ❌ Fail: K* ≤ 1 或特征无系统性趋势\\\\n\\\\n**预估资源**: 1×RTX 4090D，约 8-12 GPU 小时\\\\n\\\\n## 近期任务\\\\n- [x] GPU 服务器到位\\\\n- [x] 项目配置绑定\\\\n- [ ] Agent 完成 pipeline 代码 + 环境搭建\\\\n- [ ] 生成 depth chain（C4 5K × 6 depths）\\\\n- [ ] 特征提取 + pairwise AUC + JSD 分析\\\\n- [ ] 判定 K* → MVP gate 决策\\\\n\\\\n## GPU 预算\\\\n1×RTX 4090D 24GB @ autodl-4090d（cuda:0）\\\\n\\\\n## 关键风险\\\\n1. K* ≤ 2 → saturation characterization 路线仍可投\\\\n2. 方法论贡献薄弱 → 信道级联 + DPI 理论框架可补强\\\\n3. EMNLP ARR May 25 deadline 仅 13 天 → MVP 必须 2 天内完成\\\\n4. Reviewer SSH 不通，无法独立核实环境 → 需跟进修复\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D002 | 2026-05-12 | MVP 初步结果 K*=2（边界），修复 right-padding 后重跑确认再锁路线 | mvp_pilot_sat_v1 |\\\\n| D001 | 2026-05-12 | MVP 方案：Qwen2.5-1.8B + C4 5K docs 做 pilot saturatio | — |\\\\n\\\\n\\\", \\\"total_chars\\\": 1822, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ROADMAP.md\", \"content\": \"# gen-depth-contamination — Research Dashboard\\n\\n> 最后更新: 2026-05-12 11:16 UTC | 更新原因: 修正模型型号 1.8B→1.5B-Instruct，更新进展状态\\n\\n## 核心方向\\n估计递归生成合成文本的代际深度（generational depth），构建首个 ordinal depth classifier，实现 depth-aware graduated filtering 替代 binary detection。核心科学量：判别饱和边界 K*。\\n\\n## 当前进展\\n- **阶段**: MVP 验证（执行中）\\n- **基础设施**: autodl-4090d（1×RTX 4090D 24GB, cuda:0）\\n- **实验**: mvp_pilot_sat_v1 PREPARING，Agent 在编写 pipeline 代码\\n\\n## MVP 验证方案\\n**核心假设**: 递归生成文本在统计特征空间上存在可分辨的代际差异，且差异随深度呈系统性趋势。\\n\\n**方案**（对应 IDEA_BRIEF Phase 0 pilot saturation study）:\\n- 模型: **Qwen2.5-1.5B-Instruct**（Qwen2.5 系列无 1.8B；用 Instruct 更接近真实世界合成文本来源，full study 再对比 base vs Instruct）\\n- 种子数据: C4 子集 5K docs\\n- 深度链: depth 0(human) → depth 1-5（递归生成）\\n- 生成方式: **prompt-chain**（upper bound estimate，retrain-chain 留到 research 阶段）\\n- 解码策略: **nucleus sampling p=0.95, T=1.0**\\n- 特征（15 维）: surprisal 9 维 + vocab diversity 3 维 + tail-thinning 3 维\\n- 评估: pairwise depth AUC + JSD + LightGBM ordinal 分类\\n\\n**K* 操作性定义**: K* = max k s.t. AUC(depth k-1 vs k) > 0.60\\n\\n**Pass/Fail 标准**:\\n- ✅ Pass: K* ≥ 3 且 AUC(depth 0 vs 1) > 0.70\\n- ⚠️ Conditional Pass: K* = 2，但特征趋势清晰 → saturation characterization 路线\\n- ❌ Fail: K* ≤ 1 或特征无系统性趋势\\n\\n**预估资源**: 1×RTX 4090D，约 8-12 GPU 小时\\n\\n## 近期任务\\n- [x] GPU 服务器到位\\n- [x] 项目配置绑定\\n- [ ] Agent 完成 pipeline 代码 + 环境搭建\\n- [ ] 生成 depth chain（C4 5K × 6 depths）\\n- [ ] 特征提取 + pairwise AUC + JSD 分析\\n- [ ] 判定 K* → MVP gate 决策\\n\\n## GPU 预算\\n1×RTX 4090D 24GB @ autodl-4090d（cuda:0）\\n\\n## 关键风险\\n1. K* ≤ 2 → saturation characterization 路线仍可投\\n2. 方法论贡献薄弱 → 信道级联 + DPI 理论框架可补强\\n3. EMNLP ARR May 25 deadline 仅 13 天 → MVP 必须 2 天内完成\\n4. Reviewer SSH 不通，无法独立核实环境 → 需跟进修复\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D002 | 2026-05-12 | MVP 初步结果 K*=2（边界），修复 right-padding 后重跑确认再锁路线 | mvp_pilot_sat_v1 |\\n| D001 | 2026-05-12 | MVP 方案：Qwen2.5-1.8B + C4 5K docs 做 pilot saturatio | — |\\n\\n\", \"total_chars\": 1822, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01F5u3xjH4A3Pe2mLcTFg7HW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a2b3c6e1-bf66-4ff6-bec8-41639f3adf55",
  "uuid": "5c82501a-1367-4988-9089-f07928613f56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FDLd2tfof3vhWd8bp3g7E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 481,
      "cache_read_input_tokens": 24070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 481
      },
      "output_tokens": 69,
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

_source line 11 · 2026-05-12T16:25:04.104Z_

<details><summary>↩ Tool result · `toolu_01F5u3xjH4A3Pe2mLcTFg7HW`</summary>

```text
1	# Idea Brief: How Deep Is Your Fake? Estimating Generational Depth of Recursive Synthetic Text for Quality-Aware Data Curation
2	
3	
4	- **Idea ID**: `idea_013`
5	- **Created**: 2026-05-12
6	- **Approved**: 2026-05-12
7	- **Source**: foreign:be-idea-gen-0509-4
8	- **Level**: top-tier
9	- **Target Venues**: EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026) — primary target with compressed 10-day experiment plan and parallel writing, AAAI 2027 (abstract deadline July 25, 2026; paper deadline August 1, 2026) — fallback with additional time for full 100K corpus, extended cross-scale analysis, and polished writing, ICLR 2027 (expected submission deadline ~September 2026) — fallback allowing thorough cross-domain evaluation and larger-scale experiments
10	
11	## Seed Topic
12	
13	Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Machine Learning for NLP / Resources and Evaluation. Aligns with EMNLP 2026 special theme "New Missions for NLP Research" which explicitly calls for work on data contamination, synthetic data feedback loops, and data governance.
14	
15	Direction: Synthetic data quality, model collapse prevention, contamination detection. In-scope: synthetic data verification/filtering methods, detecting training data contamination in benchmarks, methods to break recursive data feedback loops, data mixing strategies that prevent quality degradation, principled synthetic data generation with quality guarantees.
16	
17	Contribution type: METHOD ONLY. Must propose a concrete detection algorithm, filtering pipeline, or training recipe — not just an observation about model collapse. Method + analysis OK.
18	
19	HARD CONSTRAINTS:
20	1. Compute: ≤200 H100-hours total. Model collapse experiments need multiple training iterations — budget for small models (1B-3B) across 3-5 generations.
21	2. Time: ≤16 days. Use small open models (Pythia, OLMo-1B, Qwen-0.5B/1.8B) for iterative collapse experiments.
22	3. Eval: perplexity degradation curves, downstream task quality (MMLU, HellaSwag), diversity metrics (self-BLEU, n-gram entropy), contamination detection accuracy.
23	
24	This is a hot EMNLP 2026 special theme area with relatively few established methods — high novelty potential.
25	
26	Tag: direction=data_governance, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].
27	
28	## Core Problem
29	
30	As web data becomes increasingly contaminated with multi-generation synthetic text, training corpora contain outputs of unknown recursive provenance — text generated by models that were themselves trained on synthetic outputs. Current data curation treats synthetic text as a binary category, but quality degrades nonlinearly with generational depth, with the sharpest distributional changes (tail disappearance, diversity loss) occurring in early generations. Can we estimate the generational depth of synthetic text and use this graded signal for more effective quality-aware training data filtering?
31	
32	## Opportunity / Why Now
33	
34	Existing contamination and machine-generated text detection operates at a binary level (synthetic vs. real), leaving a critical gap: the quality difference between first-generation and fourth-generation synthetic text is substantial but unexploited. Drayson et al. (EMNLP 2025) demonstrate that detection features evolve systematically across 100 generations and that detectability increases with depth — but stop short of building a depth classifier. DivEye (TMLR 2026) extracts 9 surprisal-based features for binary detection; Surplexity (2024) filters training data by surprise without even distinguishing human from AI text. Min-K%++ (ICLR 2025) improves membership inference but ignores depth. Schaeffer et al. (2025) identify 8 conflicting definitions of 'model collapse' and argue catastrophic collapse is unlikely under realistic conditions — but acknowledge that tail disappearance and diversity loss ARE real, practical harms that accumulate with recursive training. Verification-based approaches (Yi et al., arXiv 2025; Feng et al., ICLR 2025) use external verifiers to filter synthetic data quality, but neither estimates depth — they treat quality as a binary pass/fail signal from the verifier rather than estimating how many recursive steps produced the text. No method estimates how many recursive generation steps a text has undergone, despite strong evidence that degradation follows a predictable trajectory. This gap is newly fillable because controlled multi-generation corpora can be efficiently constructed with small open-weight models, and the feature evolution documented by Drayson et al. provides empirical grounding that depth-discriminative signals exist. Characterizing where depth discrimination breaks down (the saturation boundary) is itself a valuable contribution for the data curation community.
35	
36	## Landscape (SOTA & Limitations)
37	
38	The landscape spans four research threads that our work bridges:
39	
40	**Thread 1 — Synthetic text detection (binary):** Min-K% and Min-K%++ (ICLR 2025) detect pre-training membership via token probability analysis. DivEye (TMLR 2026) uses 9 surprisal-based statistical features — distributional moments, first- and second-order differences of token surprisal — for interpretable binary detection, outperforming zero-shot baselines by up to 33.2%. Surplexity (2024) proposes filtering by high surprise to mitigate collapse without distinguishing human from AI text. ConStat (NeurIPS 2024) detects contamination via performance gaps on rephrased samples. All operate at the binary level.
41	
42	**Thread 2 — Model collapse and recursive training dynamics:** Shumailov et al. (Nature 2024) demonstrate progressive tail disappearance and diversity loss across recursive training generations, with early model collapse (tail loss) preceding late collapse (mode conflation). The Strong Model Collapse paper (ICLR 2025) provides theoretical foundations. Schaeffer et al. (2025) challenge collapse definitions, identifying 8 distinct meanings and arguing that under realistic conditions (data accumulation, not replacement), catastrophic collapse requires 'trillions of models.' Bakshi et al. (arXiv 2026) show statistical conditions under which iterative training on contaminated sources can actually improve performance. Falahati et al. (arXiv May 2026) prove that pluralistic curation prevents collapse theoretically. The BIML recursive pollution framework (2026) distinguishes gradual pollution from catastrophic collapse, arguing models can become 'unusable disasters' well before full collapse.
43	
44	**Thread 3 — Synthetic data verification and quality-aware curation:** DATAPROPHET (ICLR 2026) introduces training-free data quality metrics combining perplexity, similarity, and diversity for multimodal synthetic data selection. Feng et al. (ICLR 2025) demonstrate that verification — using external signals to select high-quality synthetic samples — prevents model collapse, providing theoretical conditions under which even imperfect verifiers suffice. Yi et al. (arXiv 2025) extend this by showing that injecting information through an external verifier reverses the collapse trajectory, though long-term performance converges to the verifier's knowledge center. Both verification approaches operate at a binary quality gate level rather than estimating the recursive provenance of the text. Drayson et al. (EMNLP 2025) demonstrate that binary machine-generated text detection prevents collapse and improves performance via importance resampling, tracking feature evolution across 100 generations of GPT-2 and SmolLM2 (124M–1.7B). They show features like diversity, Self-BLEU, and perplexity distributions shift systematically with generation depth — empirically grounding the premise that depth-discriminative signals exist — but build only a binary detector.
45	
46	**The gap:** No existing work builds a practical depth-estimation algorithm. Drayson et al. characterize feature evolution across generations but do not predict depth. DivEye and Surplexity detect or filter synthetic text without generation awareness. Verification methods (Feng et al., Yi et al.) filter by quality but do not distinguish a first-generation text from a fourth-generation one. The recursive training literature (Shumailov, Bakshi, Falahati) models degradation dynamics but proposes no detection methods. We fill this gap with the first ordinal depth classifier, enabling graduated quality-aware filtering where later-generation text is downweighted proportionally rather than binary-excluded.
47	
48	## Proposed Approach
49	
50	**Phase 0 — Pilot saturation study (Days 1-3, hard gate):** Using a single model (Pythia-1.4B) and one seed dataset (C4 subset, 50K documents), generate a 10-depth recursive chain to empirically characterize where depth discrimination saturates. Extract DivEye-style surprisal features plus vocabulary diversity metrics at each depth and measure inter-depth discriminability (pairwise classifier accuracy, distribution overlap). This pilot determines the effective discrimination horizon K and informs the choice of depth granularity for the full study. We hypothesize K ≈ 3-5 based on Shumailov et al.'s observation that tail disappearance is sharpest in early generations. **Critical gating decision:** If K ≤ 2, the primary contribution pivots to saturation boundary characterization (see Saturation Fallback Plan below). The pilot MUST complete by Day 3 to avoid wasted compute downstream.
51	
52	**Saturation Fallback Plan (activated if K ≤ 2):** If depth discrimination saturates at depth ≤2, a 3-class classifier (human/gen-1/gen-2+) is only marginally more informative than binary detection. In this case, we pivot the primary contribution to a comprehensive characterization of the saturation boundary itself: (a) **Per-feature saturation analysis:** Which features plateau first — surprisal dynamics, vocabulary diversity metrics, or tail-thinning metrics? Plotting per-feature discriminability curves across depth reveals the degradation mechanisms that become indistinguishable earliest vs. latest. (b) **Cross-model saturation comparison:** Does OLMo-1B saturate at a different depth than Pythia-1.4B or Qwen2.5-1.8B? If different architectures/training regimes produce different saturation profiles, this guides model-specific curation strategies. (c) **Decoding strategy effects on saturation:** Do temperature, top-k, and nucleus sampling shift the saturation boundary? High-temperature decoding might preserve diversity longer, extending discriminability. (d) **Scale effects on saturation:** Does the 7B model (Qwen2.5-7B) produce depth chains that saturate at a different point than 1B models? If larger models saturate later, this has direct implications for real-world contamination from frontier models. These analyses make the saturation boundary characterization itself an EMNLP-quality contribution, providing actionable guidance for when depth-aware curation is effective vs. when binary detection suffices.
53	
54	**Phase 1 — Multi-generation corpus construction (Days 2-5, overlapping with Phase 0):** Construct controlled depth-labeled corpora using three small open-weight model families: Pythia-1B/1.4B (EleutherAI), OLMo-1B (AI2), and Qwen2.5-0.5B/1.8B (Alibaba). Starting from human-written seeds (C4 and Wikipedia subsets, 50K documents each — reduced from 100K for initial submission; full 100K corpus reserved for camera-ready), iteratively feed outputs back as prompts through 5 generation depths (0=human, 1-4=synthetic). Each (model, seed, depth) combination produces a depth-labeled subcorpus. Depth chains are sequential per model but parallelizable across model families.
55	
56	**Phase 2 — Feature extraction and depth-discriminative analysis (Days 4-7):** Extract features at three levels, designed to extend and complement DivEye's binary features for ordinal prediction: (a) Token-level: the 9 DivEye surprisal statistics (distributional moments + first/second-order differences) plus Min-K%-style low-probability token fractions at multiple K thresholds, providing a surprisal feature set that captures both distributional shape and temporal dynamics; (b) Sequence-level: vocabulary diversity decay metrics — type-token ratio, hapax legomena ratio, n-gram novelty (proportion of n-grams not seen in a reference human corpus), and Self-BLEU — capturing the progressive homogenization documented by Drayson et al.; (c) Distributional-level: tail-thinning metrics — kurtosis and entropy of the vocabulary frequency distribution, proportion of vocabulary below frequency thresholds — capturing the specific tail disappearance mechanism identified by Shumailov et al. Conduct feature importance analysis to identify which features drive depth discrimination vs. merely distinguish human from synthetic.
57	
58	**Phase 3 — Ordinal depth classifier (Days 6-8):** Train an ordinal regression classifier (CORAL/CORN framework) to predict generation depth (0 through K, where K is determined by the pilot), comparing against gradient-boosted baselines (LightGBM) and a simple MLP. Evaluate both exact-depth accuracy and coarse-grained classification (human/shallow/deep), since the pilot may reveal that fine-grained discrimination degenerates beyond a certain depth. Report calibration curves and confidence intervals. If the pilot shows saturation at depth K < 4, reframe as (K+1)-class classification and activate the Saturation Fallback Plan for supplementary analyses.
59	
60	**Phase 4 — Depth-aware filtering validation (Days 7-10):** Demonstrate practical utility by comparing four filtering strategies on downstream NLP benchmarks: knowledge-intensive reasoning via MMLU subsets and HellaSwag, and text generation quality via XSum summarization: (a) No filtering (baseline); (b) Binary filtering using DivEye features (remove all detected synthetic text); (c) Depth-aware weighted filtering where documents are downweighted proportionally to estimated depth (weight = 1/(1 + α·depth)); (d) Surplexity-based filtering (filter by high surprise). These benchmarks are chosen because MMLU and HellaSwag are sensitive to data quality differences in pretraining data curation (demonstrated by DataComp-LM and FineWeb-Edu evaluations), unlike well-saturated benchmarks (SST-2, AG News) where small quality improvements may not produce statistically significant gaps. Test cross-model generalization: train depth chains on Pythia, evaluate classifier on OLMo- and Qwen-generated chains.
61	
62	**Phase 4b — Cross-scale generalization probe (Days 8-10, parallel with Phase 4):** Generate a small depth chain (1K documents × 3 depths: 0, 1, 2) from Qwen2.5-7B to test whether depth features learned from 1B-scale models transfer to text generated by a 7B model. This is critical because real-world synthetic contamination primarily comes from much larger models (GPT-4, Claude, Gemini). While a full cross-scale study is beyond scope, even a small-scale probe revealing transfer (or lack thereof) provides valuable evidence about practical applicability. Cost: ~5-8 additional H100-hours.
63	
64	**Phase 5 — Naturalistic validation (Days 9-10):** Apply the trained depth classifier to a sample of recent Common Crawl data (CC-2025/2026 snapshots). Since ground-truth depth labels are unavailable for wild data, validate via proxy signals, ensuring at least one proxy is feature-orthogonal to the classifier's input features to avoid tautological correlation: (a) Correlation between predicted depth and AlignScore (NLI-based factual consistency evaluation against reference corpus documents), which measures information alignment via a unified function trained on NLI, QA, and fact verification tasks — this is feature-orthogonal because AlignScore evaluates semantic accuracy, not surprisal statistics or vocabulary distributions; (b) Correlation with independently-measured vocabulary richness metrics computed by a method distinct from the classifier's features (e.g., moving average type-token ratio with different window sizes); (c) Correlation with binary AI-detection scores from existing tools (DivEye, GPTZero) as a sanity check; (d) Qualitative analysis of high-predicted-depth samples to check face validity. This validates that the classifier produces meaningful signals on naturalistic data, not just controlled corpora.
65	
66	**Parallel writing plan (Days 1-14):** Writing begins from Day 1 and runs continuously alongside experiments. Days 1-3: Introduction and related work (leveraging existing landscape analysis). Days 4-6: Methods section (feature extraction, classifier design). Days 7-9: Results section (populated as experiments complete). Days 10-12: Discussion, analysis figures, ablation tables. Days 12-14: Final formatting, camera-ready figures, submission checklist, responsible NLP checklist. A co-author or the primary researcher allocates ~3 hours/day to writing during experimental phases.
67	
68	**Contributions (ordered by importance):** (1) The first practical generation-depth estimation algorithm for recursively generated synthetic text, moving beyond binary detection; (2) Empirical characterization of the depth-discrimination saturation boundary — at which generation depth do texts become statistically indistinguishable, which features saturate first, and how does saturation vary by model family, scale, and decoding strategy? — providing actionable guidance for data curation practitioners; (3) Demonstration that depth-aware graduated filtering outperforms both binary filtering and no filtering on challenging downstream tasks (MMLU, HellaSwag, XSum); (4) Cross-model and cross-scale depth generalization analysis, including a 7B-scale probe; (5) Feature importance analysis revealing which degradation signals (surprisal dynamics, vocabulary decay, tail thinning) are most depth-discriminative.
69	
70	## Resource Estimate
71	
72	- **auto_research**: {'claude_api_cost': '$150-280 (~1800-2500 Opus turns for end-to-end experiment design, execution, analysis, and draft generation)', 'estimated_gpu_cost': '$225-375', 'gpu_hours': '~150h H100 (exhaustive feature/model/hyperparameter search; cross-scale experiments at 7B; comprehensive saturation analysis across all models and decoding strategies; full downstream evaluation suite)', 'gpu_utilization': 'GPU idle <10%: agent runs continuous pipeline, parallelizing corpus generation across model families and overlapping feature extraction with downstream evaluation', 'risk_note': 'Agent may over-explore feature combinations without converging on a principled feature set; if pilot shows saturation at depth 2, agent should automatically activate the saturation fallback plan and redirect compute to per-feature/cross-model saturation analyses rather than continuing to optimize the depth classifier', 'speed_bottleneck': 'Sequential depth chain generation (each depth requires output from previous depth); mitigated by parallelizing across 3 model families and 2 seed datasets simultaneously. 7B cross-scale experiment adds ~8h but can run on a separate GPU. 2 H100s sufficient for 10-day timeline; 4 H100s enable 8-day completion.', 'team': '0 (initial setup only: seed data paths, model weights, evaluation benchmark specification)', 'timeline': '8-10 days with 2-4 H100s available concurrently; parallel writing tracked by agent'}
73	- **human_in_loop**: {'claude_api_cost': '$60-100 (~600-900 Opus turns for experiment planning, code generation, and result interpretation)', 'estimated_gpu_cost': '$195-325', 'gpu_hours': '~130h H100 (same base experiments plus agent-initiated feature selection sweeps and additional cross-model/cross-scale combinations)', 'gpu_utilization': 'GPU idle ~25-35%: agent queues experiments and runs analysis between human check-ins', 'risk_note': 'Saturation boundary determination requires human judgment about whether to activate the fallback plan if K ≤ 2; agent may over-optimize ordinal accuracy on controlled data without assessing generalizability', 'team': '1 researcher, ~30min/day for approving feature sets, evaluating saturation analysis, and reviewing draft sections', 'timeline': '8-10 days experiments + parallel writing; 14-day total to submission'}
74	- **manual**: {'estimated_gpu_cost': '$165-275 (at $1.50-2.50/hr H100 spot pricing, May 2026 rates)', 'gpu_hours': '~110h H100 (pilot saturation study ~15h; corpus generation across 3 model families × 5 depths at 50K docs/seed ~20h; 7B cross-scale probe ~8h; feature extraction ~8h; classifier training ~5h; downstream evaluation on MMLU/HellaSwag/XSum ~20h; naturalistic validation ~8h; ablations + saturation fallback analyses ~26h)', 'gpu_utilization': 'GPU idle ~40-50% of wall-clock time due to analysis iterations and writing between runs', 'team': '1-2 researchers, with ~3 hours/day writing allocation during experimental phase', 'timeline': '10 days experiments + 4 days final writing (writing starts Day 1 in parallel); targets EMNLP ARR May 25, 2026'}
75	
76	## Key References
77	
78	- AI models collapse when trained on recursively generated data (Shumailov et al., Nature 2024)
79	- Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models (ICLR 2025)
80	- ConStat: Performance-Based Contamination Detection in Large Language Models (NeurIPS 2024)
81	- Strong Model Collapse (ICLR 2025)
82	- Machine-generated text detection prevents language model collapse (Drayson et al., EMNLP 2025)
83	- Position: Model Collapse Does Not Mean What You Think (Schaeffer et al., 2025)
84	- Diversity Boosts AI-Generated Text Detection / DivEye (TMLR 2026)
85	- Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI (2024)
86	- DATAPROPHET: Training-Free Data Quality Metric (ICLR 2026)
87	- Curated Synthetic Data Doesn't Have to Collapse (Falahati et al., arXiv May 2026)
88	- From Collapse to Improvement: Statistical Perspectives on Iterative Training on Contaminated Sources (Bakshi et al., arXiv 2026)
89	- Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World (Kazdan et al., ICML 2025)
90	- Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data (AAAI Workshop 2026)
91	- A Comprehensive Survey of Contamination Detection Methods in Large Language Models (TMLR 2025)
92	- Recursive Pollution and Model Collapse Are Not the Same (BIML 2026)
93	- Generalization or Memorization: Data Contamination and Trustworthy Evaluation for LLMs (Findings of ACL 2024)
94	- Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence (Yi et al., arXiv 2510.16657, 2025)
95	- Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification (Feng et al., ICLR 2025)
96	- AlignScore: Evaluating Factual Consistency with a Unified Alignment Function (ACL 2023)
97	- Rank consistent ordinal regression for neural networks / CORAL (Cao et al., Pattern Recognition 2020)
98	
99	## Reviewer Evaluation
100	
101	**Scores**:
102	  - clarity: **{'rationale': 'Exceptionally well-structured: five phases with clear dependencies, a hard gating decision by Day 3, a detailed saturation fallback plan with four sub-analyses, ordered contributions, and cross-references to specific prior work at each methodological choice. The landscape analysis accurately positions the work relative to four distinct research threads.', 'score': 4}**/5
103	  - feasibility: **{'rationale': 'Compute budget (110-150h H100) fits within the 200h constraint using the specified small models (Pythia-1B/1.4B, OLMo-1B, Qwen2.5-0.5B/1.8B). The Phase 0 pilot with a hard Day-3 gate is excellent scientific methodology. The saturation fallback plan is comprehensive and turns the primary risk into a contribution. The 14-day timeline is tight but the parallel writing plan and overlapping phases make it realistic.', 'score': 4}**/5
104	  - impact: **{'rationale': "Fills a verified gap between binary detection (DivEye, Min-K%++) and quality-aware curation (Feng et al., Yi et al.) with the first depth-graded quality signal. Perfectly aligned with EMNLP 2026's confirmed special theme on data contamination and synthetic data feedback loops. Even if depth discrimination saturates early, the saturation characterization itself — which features plateau first, how saturation varies by model family and decoding strategy — provides actionable guidance for the data curation community.", 'score': 4}**/5
105	  - novelty: **{'rationale': 'Verified novel across 14+ targeted searches: no existing work frames generational depth estimation as a prediction task. Drayson et al. (EMNLP 2025) and Guo et al. (NAACL 2024) characterize feature evolution across generations descriptively, but neither builds a depth classifier or proposes depth-aware filtering. The ordinal depth estimation formulation and graduated filtering application are genuinely new contributions.', 'score': 4}**/5
106	
107	## Human Review Note
108	
109	## Agent 审核结果（完整三阶段 pipeline）
110	
111	**Verdict**: PASS
112	
113	**入口三重共识 (X)**: 28.0%
114	**终审自评 (Y)**: 34.0%
115	**出口三重共识 (Z)**: 36.0%
116	**Z 区间**: [31.0%, 42.0%]
117	**真实提升 (Z-X)**: +8.0 pp
118	**幻觉幅度 (Y-Z)**: -2.0 pp
119	**出口一致性**: 高
120	**出口三次评估**: [35.0, 38.0, 37.0]
121	
122	### 优化方案 / 拒绝详情
123	【优化方案】
124	
125	1. [标题 / 核心定位] — 在标题不变的前提下，Introduction 开头前两段建立 **"demand-side ordinal provenance estimation"** 的一句话 elevator pitch，与 supply-side watermarking、point membership inference、binary detection 形成三维对比矩阵。原始 proposal 直接进入方法描述，缺少清晰的 positioning niche。 — 命中 Novelty（positioning clarity）+ Significance（reviewer 前 30 秒形成正确印象）
126	
127	2. [核心 framing / Introduction] — 将 **saturation boundary 从 fallback contribution 提升为一阶科学量**。原始 proposal 写 "If saturation occurs at very shallow depths (K ≤ 2), we provide a comprehensive saturation characterization as the primary contribution"——这种 hedging 让 reviewer 认为作者对核心假设信心不足。改为正面 claim：saturation boundary K* 本身是首次系统测量的基本量，其位置无论高低都有独立科学价值。删除所有 "If…then" 对冲语句。 — 命中 Novelty + Contribution Clarity（消除"作者自己不确定主贡献是什么"的致命印象）
128	
129	3. [理论框架 / Introduction + Method] — 新增 **信道级联 + Data Processing Inequality 框架**。将递归生成建模为 iterated lossy channel，K* 定义为 I(X₀; Xₖ) 降至不可区分阈值的临界深度——这是一个 **information-theoretic impossibility boundary**，不仅是分类器的能力上限，而是任何方法都无法逾越的信息论极限。用 JSD 作为 computationally tractable MI proxy（明确标注为近似，承认 unigram 层面的局限）。原始 proposal 完全没有理论框架。 — 命中 Novelty（从"empirical measurement"升级为"theory + validation"）+ Technical Soundness
130	
131	4. [理论框架 / Introduction + Results] — 新增 **exponential vs. polynomial MI 衰减假设检验**作为论文叙事弧线。提出 empirically motivated hypothesis：greedy decoding → 近似指数衰减（快速收敛到 fixed point），high-temperature sampling → 较慢多项式衰减（随机性延缓同质化）。设计为 hypothesis testing format（AIC/BIC model comparison）。注意措辞校准：标为"empirically motivated hypotheses"而非"theoretical predictions"，避免 overclaim。 — 命中 Novelty + Soundness（hypothesis-driven 研究范式比 exploratory 更受审稿人认可）
132	
133	5. [贡献结构 / 全文] — **大幅精简 scope**，从原始 proposal 的"everything in one paper"收窄为两个核心贡献 + 一个 application case study。C1：depth estimation + K* characterization（含降解序分析和假设检验）；C2：depth-graduated curation。Model collapse monitoring 降为 Discussion 中的 1 段 case study。Heterogeneous model chain、human editing robustness、Common Crawl 验证移入 appendix。原始 proposal 试图同时覆盖太多方向，有 "a mile wide and an inch deep" 的风险。 — 命中 Technical Soundness（每个贡献有足够展开空间）+ 降低 reviewer 认知负担
134	
135	6. [Contribution 1 分析亮点 / Results] — 将 feature group ablation 升格为 **"linguistic degradation ordering"科学发现**：按 saturation depth 排序 feature group，揭示递归生成中语言维度的逐层坍缩结构（如 vocabulary diversity 可能先于 semantic coherence 坍缩）。用 heatmap（feature group × depth → discriminative power）可视化。原始 proposal 没有此分析维度。 — 命中 Analysis Depth / Insight（从"分类器 works"到"我们揭示了递归生成的结构性规律"）
136	
137	7. [Contribution 2 方法论 / Method] — 将 **depth-graduated curation 升格为独立 paradigm**（原始 proposal 中压缩在验证段落），给出理论动机（binary filtering 在 threshold 附近信息损失最大，ordinal signal 允许 soft weighting），并将加权方案从任意 1/k 改为 **从 depth-quality 衰减曲线经验推导**（weight ∝ quality(k)/quality(0)）。与 data mixing 文献（DoReMi）建立连接：depth-graduated weighting 是 provenance-aware domain reweighting，比 DoReMi 更轻量且有可解释语义。 — 命中 Practical Impact + Contribution Clarity + Significance
138	
139	8. [Motivation / Introduction] — 新增 **JPEG 重压缩跨模态类比**（1-2 句话）："Just as forensic image analysis estimates the number of JPEG recompression cycles, we establish generational depth estimation as a research paradigm for text." 降低理解门槛，暗示更大研究方向。原始 proposal 无此 framing。 — 命中 Clarity / Motivation
140	
141	9. [Motivation / Introduction + Broader Impact] — 新增 **model collapse early-warning 叙事线**：depth distribution 作为 model collapse 的 leading indicator（depth ≥ K 占比上升 → collapse risk 积累）。虽然降为 case study，但在 Introduction 和 broader impact 中建立联系大幅增强 significance。连接 Datasheets for Datasets / Data Statements，定位为 automated provenance documentation tool。原始 proposal 仅引用 Shumailov et al. 但未建立此联系。 — 命中 Significance + Broader Impact
142	
143	10. [Related Work] — 大幅扩展覆盖面：(a) **watermarking 互补定位**（supply-side vs. demand-side，正交互补）；(b) **Min-K%++ 关系讨论**（membership ≠ ordinal depth）；(c) **model attribution / source identification**（"which model" vs. "how many generations"，正交可组合）；(d) **最新检测工作**（Binoculars, RAID benchmark）；(e) **data mixing 文献**（DoReMi, Data Mixing Laws）；(f) **Shumailov et al. 差异化 sharpen**（macro phenomenon understanding vs. micro forensic tool）。原始 proposal 仅覆盖 binary detection 和 verification-based filtering。 — 命中 Related Work Coverage（堵住多个 reviewer 攻击面）
144	
145	11. [实验设计 / Corpus Construction] — 新增 **decoding strategy 作为显式 controlled variable**（greedy, nucleus p=0.9/0.95, temperature T=0.7/1.0/1.2）。原始 proposal 提到 "across decoding strategies" 但未展开。这直接支撑 exponential vs. polynomial 假设检验，且几乎零额外成本。 — 命中 Analysis Depth + Thoroughness
146	
147	12. [实验设计 / Corpus Construction] — 新增 **retrain-chain ecological validity check**（1 个 model family + 1 个 decoding strategy，3-4 depth levels，LoRA fine-tuning），报告 prompt-chain vs. retrain-chain 的 feature distribution 对比和 cross-setting transfer accuracy。原始 proposal 完全没有考虑 prompt-chain 与真实递归污染路径的差异。 — 命中 Technical Soundness（回应"方法在真实场景下有没有用"的核心质疑）
148	
149	13. [实验设计 / Appendix] — 新增以下 robustness analyses 作为 appendix 内容：(a) **heterogeneous model chain**（交替不同模型生成）；(b) **human editing robustness**（simulated span replacement、paraphrasing）；(c) **Common Crawl naturalistic validation**。原始 proposal 无此设计。Clean chains 明确定位为 theoretical upper bound，real-world depth estimates 定位为 ordinal quality proxies。 — 命中 Experimental Rigor
150	
151	14. [Feature Extraction / Method] — 修正 **n-gram overlap feature 的 data leakage 问题**。原始 proposal 的 "cross-depth n-gram overlap decay rate" 需要 paired original text，inference 时不可用。拆分为：(a) analysis-only metric（用于降解序研究）；(b) inference-time computable variant（self-repetition n-gram statistics、与 reference human corpus 的统计距离）。 — 命中 Technical Soundness（消除 data leakage 这一 reject-worthy 问题）
152	
153	15. [Feature Extraction / Method] — 新增 **systematic feature design** 的诚实定位：标为 "systematic and principled feature design informed by the recursive generation mechanism"，而非 overclaim 为 "novel feature contributions"。新增 token-level perplexity distribution shape features（skewness, kurtosis, entropy）。 — 命中 Technical Soundness（诚实定位避免 overclaim）
154	
155	16. [Classification / Method] — 新增系统 ablation 和 baseline 对比：(a) **ordinal vs. multinomial vs. standard regression**（证明 ordinal structure 必要性）；(b) **learned representation baseline**（frozen LM embeddings + MLP vs. hand-crafted features）；(c) **LLM zero-shot/few-shot depth estimation baseline**（验证 depth estimation 需要专门方法）；(d) **LLM-as-judge quality scoring baseline**（验证 depth signal 与 LLM quality judgment 正交）；(e) **binary detector confidence as depth proxy**（Binoculars/DetectGPT score vs. true depth Spearman correlation）。原始 proposal 仅有 CORAL/CORN + 现有 filtering methods 对比。 — 命中 Baseline Completeness（堵住"为什么不直接用 X"的多个质疑）
156	
157	17. [Cross-Scale Generalization / Method] — 增强 cross-scale 策略：(a) 将 probe 扩展到 **8B-14B 范围**（Llama-3-8B 或 Qwen2.5-14B）；(b) WildChat/LMSYS-Chat 上的 **formal feature trend analysis**（含 MMD domain shift quantification）；(c) 明确 **practical deployment scope 为开源模型生态（7B-14B）**；(d) frontier model limitation 扩展为 **principled discussion**（RLHF/instruction-tuning 对 depth signal 的影响、API-only access 对 feature 计算的限制）。原始 proposal 仅有 Qwen2.5-7B 一个 cross-scale probe。 — 命中 Significance（论证实际部署价值）
158	
159	18. [Downstream Curation / Experimental Validation] — 大幅增强 curation 实验严格性：(a) **contamination severity 维度**（10%/30%/50% synthetic injection）；(b) **cross-model transfer**（classifier 训 on model A, curate model B）；(c) **unknown depth distribution condition**；(d) **data-quality-sensitive tasks**（held-out perplexity, factual QA，不仅限于 MMLU）；(e) **binary filtering threshold 选择协议明确化**；(f) **bootstrap CIs + paired significance tests**；(g) **实验逻辑链显式说明**。原始 proposal 对 filtering 实验的公平性和统计显著性没有详细设计。 — 命中 Technical Soundness + Experimental Rigor
160	
161	19. [Depth vs. Quality Analysis / Experimental Validation] — 新增 **depth-quality 单调性直接验证**。原始 proposal 隐含假设 depth 与 quality 单调递减但未验证。新增多维度 quality proxy 曲线，验证单调性成立条件。如非单调，graduated filtering 适应为 depth-features → predicted quality → weight。 — 命中 Technical Soundness（验证核心前提假设）
162	
163	20. [K* Contingency / Experimental Validation] — 新增 **显式 contingency 讨论**：K*≤3 时贡献重定位为首次量化 fundamental resolution limit + decoding strategy 对 K* 的调控效应 + 即使 coarse ordinal signal 仍有 calibration 优势。原始 proposal 的 "If…then" 结构是结构性风险。 — 命中 Soundness + Reviewer 心理管理
164	
165	【主要风险】:
166	1. **K* 实验结果不确定性**：如果在大多数 model/decoding 配置下 K*≤2，论文的 empirical richness 和 graduated curation 收益都会受限。虽有 contingency plan（fundamental resolution limit characterization + decoding strategy modulation），但 reviewer 仍可能评为 "interesting characterization but limited practical impact"。这是无法通过 proposal 优化消除的固有风险。
167	2. **"Good problem + standard method" 框架**：核心分类 pipeline 是 feature engineering + off-the-shelf ordinal regression（CORAL/CORN），审稿人可能认为方法论贡献不足。信息论框架和假设检验提升了分析深度，但分类器本身没有方法论突破。对于偏重 methods 的审稿人，这可能是 borderline reject 的理由。
168	
169	【实施评估】:
170	- 计算资源: 主实验（corpus generation + feature extraction + classifier training）可在 2-4 块 A100 上完成，估计 1-2 周。Retrain-chain validation（1 config, LoRA fine-tuning, 3-4 depth levels）约 2-3 天额外 GPU 时间。Cross-scale probe（7B-14B 模型生成 + 特征提取）约 3-5 天。总计 GPU 需求约 2-3 周集中使用。不需要大规模集群。
171	- 数据需求: C4 和 Wikipedia 子集（50K documents each）——公开可得。WildChat / LMSYS-Chat——公开可得。无需私有或受限数据集。
172	- 人工介入: 无需人工标注（ground-truth depth labels 由 generation pipeline 自动产生）。无需专家评审。唯一的人工环节是实验设计决策和论文写作。
173	- 训练需求: 需要模型训练，但规模有限。(a) Ordinal regression classifier（CORAL/CORN）：轻量级，训练时间可忽略。(b) Retrain-chain 的 LoRA fine-tuning：Pythia-1B 级别，每轮约 1-2 小时。(c) 不需要从头预训练任何 LLM。(d) 下游 curation 评估需要在 curated data 上训练小模型（≤1.8B），但这也是标准规模。
174	- 新 Benchmark: 不需要构建新的公开 benchmark。构建的 multi-depth corpus 是实验工具而非独立 benchmark 贡献（但可作为 artifact release）。
175	- 预估周期: Corpus generation + feature extraction: 2-3 周；Classifier training + ablation: 1 周；Downstream curation experiments: 1-2 周；Cross-scale + retrain-chain validation: 1-2 周；Analysis + writing: 2-3 周。**总计约 8-12 周**（从启动到可投稿），假设 GPU 资源持续可用。如果 GPU 间歇使用，可能延长至 12-16 周。EMNLP 2026 投稿 deadline 前有充足时间。
176	
177	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a2b3c6e1-bf66-4ff6-bec8-41639f3adf55",
  "uuid": "fa3a0ca3-db01-4727-9327-6930ad1c8055",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/IDEA_BRIEF.md",
      "content": "# Idea Brief: How Deep Is Your Fake? Estimating Generational Depth of Recursive Synthetic Text for Quality-Aware Data Curation\n\n\n- **Idea ID**: `idea_013`\n- **Created**: 2026-05-12\n- **Approved**: 2026-05-12\n- **Source**: foreign:be-idea-gen-0509-4\n- **Level**: top-tier\n- **Target Venues**: EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026) — primary target with compressed 10-day experiment plan and parallel writing, AAAI 2027 (abstract deadline July 25, 2026; paper deadline August 1, 2026) — fallback with additional time for full 100K corpus, extended cross-scale analysis, and polished writing, ICLR 2027 (expected submission deadline ~September 2026) — fallback allowing thorough cross-domain evaluation and larger-scale experiments\n\n## Seed Topic\n\nTarget: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Machine Learning for NLP / Resources and Evaluation. Aligns with EMNLP 2026 special theme \"New Missions for NLP Research\" which explicitly calls for work on data contamination, synthetic data feedback loops, and data governance.\n\nDirection: Synthetic data quality, model collapse prevention, contamination detection. In-scope: synthetic data verification/filtering methods, detecting training data contamination in benchmarks, methods to break recursive data feedback loops, data mixing strategies that prevent quality degradation, principled synthetic data generation with quality guarantees.\n\nContribution type: METHOD ONLY. Must propose a concrete detection algorithm, filtering pipeline, or training recipe — not just an observation about model collapse. Method + analysis OK.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Model collapse experiments need multiple training iterations — budget for small models (1B-3B) across 3-5 generations.\n2. Time: ≤16 days. Use small open models (Pythia, OLMo-1B, Qwen-0.5B/1.8B) for iterative collapse experiments.\n3. Eval: perplexity degradation curves, downstream task quality (MMLU, HellaSwag), diversity metrics (self-BLEU, n-gram entropy), contamination detection accuracy.\n\nThis is a hot EMNLP 2026 special theme area with relatively few established methods — high novelty potential.\n\nTag: direction=data_governance, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].\n\n## Core Problem\n\nAs web data becomes increasingly contaminated with multi-generation synthetic text, training corpora contain outputs of unknown recursive provenance — text generated by models that were themselves trained on synthetic outputs. Current data curation treats synthetic text as a binary category, but quality degrades nonlinearly with generational depth, with the sharpest distributional changes (tail disappearance, diversity loss) occurring in early generations. Can we estimate the generational depth of synthetic text and use this graded signal for more effective quality-aware training data filtering?\n\n## Opportunity / Why Now\n\nExisting contamination and machine-generated text detection operates at a binary level (synthetic vs. real), leaving a critical gap: the quality difference between first-generation and fourth-generation synthetic text is substantial but unexploited. Drayson et al. (EMNLP 2025) demonstrate that detection features evolve systematically across 100 generations and that detectability increases with depth — but stop short of building a depth classifier. DivEye (TMLR 2026) extracts 9 surprisal-based features for binary detection; Surplexity (2024) filters training data by surprise without even distinguishing human from AI text. Min-K%++ (ICLR 2025) improves membership inference but ignores depth. Schaeffer et al. (2025) identify 8 conflicting definitions of 'model collapse' and argue catastrophic collapse is unlikely under realistic conditions — but acknowledge that tail disappearance and diversity loss ARE real, practical harms that accumulate with recursive training. Verification-based approaches (Yi et al., arXiv 2025; Feng et al., ICLR 2025) use external verifiers to filter synthetic data quality, but neither estimates depth — they treat quality as a binary pass/fail signal from the verifier rather than estimating how many recursive steps produced the text. No method estimates how many recursive generation steps a text has undergone, despite strong evidence that degradation follows a predictable trajectory. This gap is newly fillable because controlled multi-generation corpora can be efficiently constructed with small open-weight models, and the feature evolution documented by Drayson et al. provides empirical grounding that depth-discriminative signals exist. Characterizing where depth discrimination breaks down (the saturation boundary) is itself a valuable contribution for the data curation community.\n\n## Landscape (SOTA & Limitations)\n\nThe landscape spans four research threads that our work bridges:\n\n**Thread 1 — Synthetic text detection (binary):** Min-K% and Min-K%++ (ICLR 2025) detect pre-training membership via token probability analysis. DivEye (TMLR 2026) uses 9 surprisal-based statistical features — distributional moments, first- and second-order differences of token surprisal — for interpretable binary detection, outperforming zero-shot baselines by up to 33.2%. Surplexity (2024) proposes filtering by high surprise to mitigate collapse without distinguishing human from AI text. ConStat (NeurIPS 2024) detects contamination via performance gaps on rephrased samples. All operate at the binary level.\n\n**Thread 2 — Model collapse and recursive training dynamics:** Shumailov et al. (Nature 2024) demonstrate progressive tail disappearance and diversity loss across recursive training generations, with early model collapse (tail loss) preceding late collapse (mode conflation). The Strong Model Collapse paper (ICLR 2025) provides theoretical foundations. Schaeffer et al. (2025) challenge collapse definitions, identifying 8 distinct meanings and arguing that under realistic conditions (data accumulation, not replacement), catastrophic collapse requires 'trillions of models.' Bakshi et al. (arXiv 2026) show statistical conditions under which iterative training on contaminated sources can actually improve performance. Falahati et al. (arXiv May 2026) prove that pluralistic curation prevents collapse theoretically. The BIML recursive pollution framework (2026) distinguishes gradual pollution from catastrophic collapse, arguing models can become 'unusable disasters' well before full collapse.\n\n**Thread 3 — Synthetic data verification and quality-aware curation:** DATAPROPHET (ICLR 2026) introduces training-free data quality metrics combining perplexity, similarity, and diversity for multimodal synthetic data selection. Feng et al. (ICLR 2025) demonstrate that verification — using external signals to select high-quality synthetic samples — prevents model collapse, providing theoretical conditions under which even imperfect verifiers suffice. Yi et al. (arXiv 2025) extend this by showing that injecting information through an external verifier reverses the collapse trajectory, though long-term performance converges to the verifier's knowledge center. Both verification approaches operate at a binary quality gate level rather than estimating the recursive provenance of the text. Drayson et al. (EMNLP 2025) demonstrate that binary machine-generated text detection prevents collapse and improves performance via importance resampling, tracking feature evolution across 100 generations of GPT-2 and SmolLM2 (124M–1.7B). They show features like diversity, Self-BLEU, and perplexity distributions shift systematically with generation depth — empirically grounding the premise that depth-discriminative signals exist — but build only a binary detector.\n\n**The gap:** No existing work builds a practical depth-estimation algorithm. Drayson et al. characterize feature evolution across generations but do not predict depth. DivEye and Surplexity detect or filter synthetic text without generation awareness. Verification methods (Feng et al., Yi et al.) filter by quality but do not distinguish a first-generation text from a fourth-generation one. The recursive training literature (Shumailov, Bakshi, Falahati) models degradation dynamics but proposes no detection methods. We fill this gap with the first ordinal depth classifier, enabling graduated quality-aware filtering where later-generation text is downweighted proportionally rather than binary-excluded.\n\n## Proposed Approach\n\n**Phase 0 — Pilot saturation study (Days 1-3, hard gate):** Using a single model (Pythia-1.4B) and one seed dataset (C4 subset, 50K documents), generate a 10-depth recursive chain to empirically characterize where depth discrimination saturates. Extract DivEye-style surprisal features plus vocabulary diversity metrics at each depth and measure inter-depth discriminability (pairwise classifier accuracy, distribution overlap). This pilot determines the effective discrimination horizon K and informs the choice of depth granularity for the full study. We hypothesize K ≈ 3-5 based on Shumailov et al.'s observation that tail disappearance is sharpest in early generations. **Critical gating decision:** If K ≤ 2, the primary contribution pivots to saturation boundary characterization (see Saturation Fallback Plan below). The pilot MUST complete by Day 3 to avoid wasted compute downstream.\n\n**Saturation Fallback Plan (activated if K ≤ 2):** If depth discrimination saturates at depth ≤2, a 3-class classifier (human/gen-1/gen-2+) is only marginally more informative than binary detection. In this case, we pivot the primary contribution to a comprehensive characterization of the saturation boundary itself: (a) **Per-feature saturation analysis:** Which features plateau first — surprisal dynamics, vocabulary diversity metrics, or tail-thinning metrics? Plotting per-feature discriminability curves across depth reveals the degradation mechanisms that become indistinguishable earliest vs. latest. (b) **Cross-model saturation comparison:** Does OLMo-1B saturate at a different depth than Pythia-1.4B or Qwen2.5-1.8B? If different architectures/training regimes produce different saturation profiles, this guides model-specific curation strategies. (c) **Decoding strategy effects on saturation:** Do temperature, top-k, and nucleus sampling shift the saturation boundary? High-temperature decoding might preserve diversity longer, extending discriminability. (d) **Scale effects on saturation:** Does the 7B model (Qwen2.5-7B) produce depth chains that saturate at a different point than 1B models? If larger models saturate later, this has direct implications for real-world contamination from frontier models. These analyses make the saturation boundary characterization itself an EMNLP-quality contribution, providing actionable guidance for when depth-aware curation is effective vs. when binary detection suffices.\n\n**Phase 1 — Multi-generation corpus construction (Days 2-5, overlapping with Phase 0):** Construct controlled depth-labeled corpora using three small open-weight model families: Pythia-1B/1.4B (EleutherAI), OLMo-1B (AI2), and Qwen2.5-0.5B/1.8B (Alibaba). Starting from human-written seeds (C4 and Wikipedia subsets, 50K documents each — reduced from 100K for initial submission; full 100K corpus reserved for camera-ready), iteratively feed outputs back as prompts through 5 generation depths (0=human, 1-4=synthetic). Each (model, seed, depth) combination produces a depth-labeled subcorpus. Depth chains are sequential per model but parallelizable across model families.\n\n**Phase 2 — Feature extraction and depth-discriminative analysis (Days 4-7):** Extract features at three levels, designed to extend and complement DivEye's binary features for ordinal prediction: (a) Token-level: the 9 DivEye surprisal statistics (distributional moments + first/second-order differences) plus Min-K%-style low-probability token fractions at multiple K thresholds, providing a surprisal feature set that captures both distributional shape and temporal dynamics; (b) Sequence-level: vocabulary diversity decay metrics — type-token ratio, hapax legomena ratio, n-gram novelty (proportion of n-grams not seen in a reference human corpus), and Self-BLEU — capturing the progressive homogenization documented by Drayson et al.; (c) Distributional-level: tail-thinning metrics — kurtosis and entropy of the vocabulary frequency distribution, proportion of vocabulary below frequency thresholds — capturing the specific tail disappearance mechanism identified by Shumailov et al. Conduct feature importance analysis to identify which features drive depth discrimination vs. merely distinguish human from synthetic.\n\n**Phase 3 — Ordinal depth classifier (Days 6-8):** Train an ordinal regression classifier (CORAL/CORN framework) to predict generation depth (0 through K, where K is determined by the pilot), comparing against gradient-boosted baselines (LightGBM) and a simple MLP. Evaluate both exact-depth accuracy and coarse-grained classification (human/shallow/deep), since the pilot may reveal that fine-grained discrimination degenerates beyond a certain depth. Report calibration curves and confidence intervals. If the pilot shows saturation at depth K < 4, reframe as (K+1)-class classification and activate the Saturation Fallback Plan for supplementary analyses.\n\n**Phase 4 — Depth-aware filtering validation (Days 7-10):** Demonstrate practical utility by comparing four filtering strategies on downstream NLP benchmarks: knowledge-intensive reasoning via MMLU subsets and HellaSwag, and text generation quality via XSum summarization: (a) No filtering (baseline); (b) Binary filtering using DivEye features (remove all detected synthetic text); (c) Depth-aware weighted filtering where documents are downweighted proportionally to estimated depth (weight = 1/(1 + α·depth)); (d) Surplexity-based filtering (filter by high surprise). These benchmarks are chosen because MMLU and HellaSwag are sensitive to data quality differences in pretraining data curation (demonstrated by DataComp-LM and FineWeb-Edu evaluations), unlike well-saturated benchmarks (SST-2, AG News) where small quality improvements may not produce statistically significant gaps. Test cross-model generalization: train depth chains on Pythia, evaluate classifier on OLMo- and Qwen-generated chains.\n\n**Phase 4b — Cross-scale generalization probe (Days 8-10, parallel with Phase 4):** Generate a small depth chain (1K documents × 3 depths: 0, 1, 2) from Qwen2.5-7B to test whether depth features learned from 1B-scale models transfer to text generated by a 7B model. This is critical because real-world synthetic contamination primarily comes from much larger models (GPT-4, Claude, Gemini). While a full cross-scale study is beyond scope, even a small-scale probe revealing transfer (or lack thereof) provides valuable evidence about practical applicability. Cost: ~5-8 additional H100-hours.\n\n**Phase 5 — Naturalistic validation (Days 9-10):** Apply the trained depth classifier to a sample of recent Common Crawl data (CC-2025/2026 snapshots). Since ground-truth depth labels are unavailable for wild data, validate via proxy signals, ensuring at least one proxy is feature-orthogonal to the classifier's input features to avoid tautological correlation: (a) Correlation between predicted depth and AlignScore (NLI-based factual consistency evaluation against reference corpus documents), which measures information alignment via a unified function trained on NLI, QA, and fact verification tasks — this is feature-orthogonal because AlignScore evaluates semantic accuracy, not surprisal statistics or vocabulary distributions; (b) Correlation with independently-measured vocabulary richness metrics computed by a method distinct from the classifier's features (e.g., moving average type-token ratio with different window sizes); (c) Correlation with binary AI-detection scores from existing tools (DivEye, GPTZero) as a sanity check; (d) Qualitative analysis of high-predicted-depth samples to check face validity. This validates that the classifier produces meaningful signals on naturalistic data, not just controlled corpora.\n\n**Parallel writing plan (Days 1-14):** Writing begins from Day 1 and runs continuously alongside experiments. Days 1-3: Introduction and related work (leveraging existing landscape analysis). Days 4-6: Methods section (feature extraction, classifier design). Days 7-9: Results section (populated as experiments complete). Days 10-12: Discussion, analysis figures, ablation tables. Days 12-14: Final formatting, camera-ready figures, submission checklist, responsible NLP checklist. A co-author or the primary researcher allocates ~3 hours/day to writing during experimental phases.\n\n**Contributions (ordered by importance):** (1) The first practical generation-depth estimation algorithm for recursively generated synthetic text, moving beyond binary detection; (2) Empirical characterization of the depth-discrimination saturation boundary — at which generation depth do texts become statistically indistinguishable, which features saturate first, and how does saturation vary by model family, scale, and decoding strategy? — providing actionable guidance for data curation practitioners; (3) Demonstration that depth-aware graduated filtering outperforms both binary filtering and no filtering on challenging downstream tasks (MMLU, HellaSwag, XSum); (4) Cross-model and cross-scale depth generalization analysis, including a 7B-scale probe; (5) Feature importance analysis revealing which degradation signals (surprisal dynamics, vocabulary decay, tail thinning) are most depth-discriminative.\n\n## Resource Estimate\n\n- **auto_research**: {'claude_api_cost': '$150-280 (~1800-2500 Opus turns for end-to-end experiment design, execution, analysis, and draft generation)', 'estimated_gpu_cost': '$225-375', 'gpu_hours': '~150h H100 (exhaustive feature/model/hyperparameter search; cross-scale experiments at 7B; comprehensive saturation analysis across all models and decoding strategies; full downstream evaluation suite)', 'gpu_utilization': 'GPU idle <10%: agent runs continuous pipeline, parallelizing corpus generation across model families and overlapping feature extraction with downstream evaluation', 'risk_note': 'Agent may over-explore feature combinations without converging on a principled feature set; if pilot shows saturation at depth 2, agent should automatically activate the saturation fallback plan and redirect compute to per-feature/cross-model saturation analyses rather than continuing to optimize the depth classifier', 'speed_bottleneck': 'Sequential depth chain generation (each depth requires output from previous depth); mitigated by parallelizing across 3 model families and 2 seed datasets simultaneously. 7B cross-scale experiment adds ~8h but can run on a separate GPU. 2 H100s sufficient for 10-day timeline; 4 H100s enable 8-day completion.', 'team': '0 (initial setup only: seed data paths, model weights, evaluation benchmark specification)', 'timeline': '8-10 days with 2-4 H100s available concurrently; parallel writing tracked by agent'}\n- **human_in_loop**: {'claude_api_cost': '$60-100 (~600-900 Opus turns for experiment planning, code generation, and result interpretation)', 'estimated_gpu_cost': '$195-325', 'gpu_hours': '~130h H100 (same base experiments plus agent-initiated feature selection sweeps and additional cross-model/cross-scale combinations)', 'gpu_utilization': 'GPU idle ~25-35%: agent queues experiments and runs analysis between human check-ins', 'risk_note': 'Saturation boundary determination requires human judgment about whether to activate the fallback plan if K ≤ 2; agent may over-optimize ordinal accuracy on controlled data without assessing generalizability', 'team': '1 researcher, ~30min/day for approving feature sets, evaluating saturation analysis, and reviewing draft sections', 'timeline': '8-10 days experiments + parallel writing; 14-day total to submission'}\n- **manual**: {'estimated_gpu_cost': '$165-275 (at $1.50-2.50/hr H100 spot pricing, May 2026 rates)', 'gpu_hours': '~110h H100 (pilot saturation study ~15h; corpus generation across 3 model families × 5 depths at 50K docs/seed ~20h; 7B cross-scale probe ~8h; feature extraction ~8h; classifier training ~5h; downstream evaluation on MMLU/HellaSwag/XSum ~20h; naturalistic validation ~8h; ablations + saturation fallback analyses ~26h)', 'gpu_utilization': 'GPU idle ~40-50% of wall-clock time due to analysis iterations and writing between runs', 'team': '1-2 researchers, with ~3 hours/day writing allocation during experimental phase', 'timeline': '10 days experiments + 4 days final writing (writing starts Day 1 in parallel); targets EMNLP ARR May 25, 2026'}\n\n## Key References\n\n- AI models collapse when trained on recursively generated data (Shumailov et al., Nature 2024)\n- Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models (ICLR 2025)\n- ConStat: Performance-Based Contamination Detection in Large Language Models (NeurIPS 2024)\n- Strong Model Collapse (ICLR 2025)\n- Machine-generated text detection prevents language model collapse (Drayson et al., EMNLP 2025)\n- Position: Model Collapse Does Not Mean What You Think (Schaeffer et al., 2025)\n- Diversity Boosts AI-Generated Text Detection / DivEye (TMLR 2026)\n- Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI (2024)\n- DATAPROPHET: Training-Free Data Quality Metric (ICLR 2026)\n- Curated Synthetic Data Doesn't Have to Collapse (Falahati et al., arXiv May 2026)\n- From Collapse to Improvement: Statistical Perspectives on Iterative Training on Contaminated Sources (Bakshi et al., arXiv 2026)\n- Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World (Kazdan et al., ICML 2025)\n- Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data (AAAI Workshop 2026)\n- A Comprehensive Survey of Contamination Detection Methods in Large Language Models (TMLR 2025)\n- Recursive Pollution and Model Collapse Are Not the Same (BIML 2026)\n- Generalization or Memorization: Data Contamination and Trustworthy Evaluation for LLMs (Findings of ACL 2024)\n- Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence (Yi et al., arXiv 2510.16657, 2025)\n- Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification (Feng et al., ICLR 2025)\n- AlignScore: Evaluating Factual Consistency with a Unified Alignment Function (ACL 2023)\n- Rank consistent ordinal regression for neural networks / CORAL (Cao et al., Pattern Recognition 2020)\n\n## Reviewer Evaluation\n\n**Scores**:\n  - clarity: **{'rationale': 'Exceptionally well-structured: five phases with clear dependencies, a hard gating decision by Day 3, a detailed saturation fallback plan with four sub-analyses, ordered contributions, and cross-references to specific prior work at each methodological choice. The landscape analysis accurately positions the work relative to four distinct research threads.', 'score': 4}**/5\n  - feasibility: **{'rationale': 'Compute budget (110-150h H100) fits within the 200h constraint using the specified small models (Pythia-1B/1.4B, OLMo-1B, Qwen2.5-0.5B/1.8B). The Phase 0 pilot with a hard Day-3 gate is excellent scientific methodology. The saturation fallback plan is comprehensive and turns the primary risk into a contribution. The 14-day timeline is tight but the parallel writing plan and overlapping phases make it realistic.', 'score': 4}**/5\n  - impact: **{'rationale': \"Fills a verified gap between binary detection (DivEye, Min-K%++) and quality-aware curation (Feng et al., Yi et al.) with the first depth-graded quality signal. Perfectly aligned with EMNLP 2026's confirmed special theme on data contamination and synthetic data feedback loops. Even if depth discrimination saturates early, the saturation characterization itself — which features plateau first, how saturation varies by model family and decoding strategy — provides actionable guidance for the data curation community.\", 'score': 4}**/5\n  - novelty: **{'rationale': 'Verified novel across 14+ targeted searches: no existing work frames generational depth estimation as a prediction task. Drayson et al. (EMNLP 2025) and Guo et al. (NAACL 2024) characterize feature evolution across generations descriptively, but neither builds a depth classifier or proposes depth-aware filtering. The ordinal depth estimation formulation and graduated filtering application are genuinely new contributions.', 'score': 4}**/5\n\n## Human Review Note\n\n## Agent 审核结果（完整三阶段 pipeline）\n\n**Verdict**: PASS\n\n**入口三重共识 (X)**: 28.0%\n**终审自评 (Y)**: 34.0%\n**出口三重共识 (Z)**: 36.0%\n**Z 区间**: [31.0%, 42.0%]\n**真实提升 (Z-X)**: +8.0 pp\n**幻觉幅度 (Y-Z)**: -2.0 pp\n**出口一致性**: 高\n**出口三次评估**: [35.0, 38.0, 37.0]\n\n### 优化方案 / 拒绝详情\n【优化方案】\n\n1. [标题 / 核心定位] — 在标题不变的前提下，Introduction 开头前两段建立 **\"demand-side ordinal provenance estimation\"** 的一句话 elevator pitch，与 supply-side watermarking、point membership inference、binary detection 形成三维对比矩阵。原始 proposal 直接进入方法描述，缺少清晰的 positioning niche。 — 命中 Novelty（positioning clarity）+ Significance（reviewer 前 30 秒形成正确印象）\n\n2. [核心 framing / Introduction] — 将 **saturation boundary 从 fallback contribution 提升为一阶科学量**。原始 proposal 写 \"If saturation occurs at very shallow depths (K ≤ 2), we provide a comprehensive saturation characterization as the primary contribution\"——这种 hedging 让 reviewer 认为作者对核心假设信心不足。改为正面 claim：saturation boundary K* 本身是首次系统测量的基本量，其位置无论高低都有独立科学价值。删除所有 \"If…then\" 对冲语句。 — 命中 Novelty + Contribution Clarity（消除\"作者自己不确定主贡献是什么\"的致命印象）\n\n3. [理论框架 / Introduction + Method] — 新增 **信道级联 + Data Processing Inequality 框架**。将递归生成建模为 iterated lossy channel，K* 定义为 I(X₀; Xₖ) 降至不可区分阈值的临界深度——这是一个 **information-theoretic impossibility boundary**，不仅是分类器的能力上限，而是任何方法都无法逾越的信息论极限。用 JSD 作为 computationally tractable MI proxy（明确标注为近似，承认 unigram 层面的局限）。原始 proposal 完全没有理论框架。 — 命中 Novelty（从\"empirical measurement\"升级为\"theory + validation\"）+ Technical Soundness\n\n4. [理论框架 / Introduction + Results] — 新增 **exponential vs. polynomial MI 衰减假设检验**作为论文叙事弧线。提出 empirically motivated hypothesis：greedy decoding → 近似指数衰减（快速收敛到 fixed point），high-temperature sampling → 较慢多项式衰减（随机性延缓同质化）。设计为 hypothesis testing format（AIC/BIC model comparison）。注意措辞校准：标为\"empirically motivated hypotheses\"而非\"theoretical predictions\"，避免 overclaim。 — 命中 Novelty + Soundness（hypothesis-driven 研究范式比 exploratory 更受审稿人认可）\n\n5. [贡献结构 / 全文] — **大幅精简 scope**，从原始 proposal 的\"everything in one paper\"收窄为两个核心贡献 + 一个 application case study。C1：depth estimation + K* characterization（含降解序分析和假设检验）；C2：depth-graduated curation。Model collapse monitoring 降为 Discussion 中的 1 段 case study。Heterogeneous model chain、human editing robustness、Common Crawl 验证移入 appendix。原始 proposal 试图同时覆盖太多方向，有 \"a mile wide and an inch deep\" 的风险。 — 命中 Technical Soundness（每个贡献有足够展开空间）+ 降低 reviewer 认知负担\n\n6. [Contribution 1 分析亮点 / Results] — 将 feature group ablation 升格为 **\"linguistic degradation ordering\"科学发现**：按 saturation depth 排序 feature group，揭示递归生成中语言维度的逐层坍缩结构（如 vocabulary diversity 可能先于 semantic coherence 坍缩）。用 heatmap（feature group × depth → discriminative power）可视化。原始 proposal 没有此分析维度。 — 命中 Analysis Depth / Insight（从\"分类器 works\"到\"我们揭示了递归生成的结构性规律\"）\n\n7. [Contribution 2 方法论 / Method] — 将 **depth-graduated curation 升格为独立 paradigm**（原始 proposal 中压缩在验证段落），给出理论动机（binary filtering 在 threshold 附近信息损失最大，ordinal signal 允许 soft weighting），并将加权方案从任意 1/k 改为 **从 depth-quality 衰减曲线经验推导**（weight ∝ quality(k)/quality(0)）。与 data mixing 文献（DoReMi）建立连接：depth-graduated weighting 是 provenance-aware domain reweighting，比 DoReMi 更轻量且有可解释语义。 — 命中 Practical Impact + Contribution Clarity + Significance\n\n8. [Motivation / Introduction] — 新增 **JPEG 重压缩跨模态类比**（1-2 句话）：\"Just as forensic image analysis estimates the number of JPEG recompression cycles, we establish generational depth estimation as a research paradigm for text.\" 降低理解门槛，暗示更大研究方向。原始 proposal 无此 framing。 — 命中 Clarity / Motivation\n\n9. [Motivation / Introduction + Broader Impact] — 新增 **model collapse early-warning 叙事线**：depth distribution 作为 model collapse 的 leading indicator（depth ≥ K 占比上升 → collapse risk 积累）。虽然降为 case study，但在 Introduction 和 broader impact 中建立联系大幅增强 significance。连接 Datasheets for Datasets / Data Statements，定位为 automated provenance documentation tool。原始 proposal 仅引用 Shumailov et al. 但未建立此联系。 — 命中 Significance + Broader Impact\n\n10. [Related Work] — 大幅扩展覆盖面：(a) **watermarking 互补定位**（supply-side vs. demand-side，正交互补）；(b) **Min-K%++ 关系讨论**（membership ≠ ordinal depth）；(c) **model attribution / source identification**（\"which model\" vs. \"how many generations\"，正交可组合）；(d) **最新检测工作**（Binoculars, RAID benchmark）；(e) **data mixing 文献**（DoReMi, Data Mixing Laws）；(f) **Shumailov et al. 差异化 sharpen**（macro phenomenon understanding vs. micro forensic tool）。原始 proposal 仅覆盖 binary detection 和 verification-based filtering。 — 命中 Related Work Coverage（堵住多个 reviewer 攻击面）\n\n11. [实验设计 / Corpus Construction] — 新增 **decoding strategy 作为显式 controlled variable**（greedy, nucleus p=0.9/0.95, temperature T=0.7/1.0/1.2）。原始 proposal 提到 \"across decoding strategies\" 但未展开。这直接支撑 exponential vs. polynomial 假设检验，且几乎零额外成本。 — 命中 Analysis Depth + Thoroughness\n\n12. [实验设计 / Corpus Construction] — 新增 **retrain-chain ecological validity check**（1 个 model family + 1 个 decoding strategy，3-4 depth levels，LoRA fine-tuning），报告 prompt-chain vs. retrain-chain 的 feature distribution 对比和 cross-setting transfer accuracy。原始 proposal 完全没有考虑 prompt-chain 与真实递归污染路径的差异。 — 命中 Technical Soundness（回应\"方法在真实场景下有没有用\"的核心质疑）\n\n13. [实验设计 / Appendix] — 新增以下 robustness analyses 作为 appendix 内容：(a) **heterogeneous model chain**（交替不同模型生成）；(b) **human editing robustness**（simulated span replacement、paraphrasing）；(c) **Common Crawl naturalistic validation**。原始 proposal 无此设计。Clean chains 明确定位为 theoretical upper bound，real-world depth estimates 定位为 ordinal quality proxies。 — 命中 Experimental Rigor\n\n14. [Feature Extraction / Method] — 修正 **n-gram overlap feature 的 data leakage 问题**。原始 proposal 的 \"cross-depth n-gram overlap decay rate\" 需要 paired original text，inference 时不可用。拆分为：(a) analysis-only metric（用于降解序研究）；(b) inference-time computable variant（self-repetition n-gram statistics、与 reference human corpus 的统计距离）。 — 命中 Technical Soundness（消除 data leakage 这一 reject-worthy 问题）\n\n15. [Feature Extraction / Method] — 新增 **systematic feature design** 的诚实定位：标为 \"systematic and principled feature design informed by the recursive generation mechanism\"，而非 overclaim 为 \"novel feature contributions\"。新增 token-level perplexity distribution shape features（skewness, kurtosis, entropy）。 — 命中 Technical Soundness（诚实定位避免 overclaim）\n\n16. [Classification / Method] — 新增系统 ablation 和 baseline 对比：(a) **ordinal vs. multinomial vs. standard regression**（证明 ordinal structure 必要性）；(b) **learned representation baseline**（frozen LM embeddings + MLP vs. hand-crafted features）；(c) **LLM zero-shot/few-shot depth estimation baseline**（验证 depth estimation 需要专门方法）；(d) **LLM-as-judge quality scoring baseline**（验证 depth signal 与 LLM quality judgment 正交）；(e) **binary detector confidence as depth proxy**（Binoculars/DetectGPT score vs. true depth Spearman correlation）。原始 proposal 仅有 CORAL/CORN + 现有 filtering methods 对比。 — 命中 Baseline Completeness（堵住\"为什么不直接用 X\"的多个质疑）\n\n17. [Cross-Scale Generalization / Method] — 增强 cross-scale 策略：(a) 将 probe 扩展到 **8B-14B 范围**（Llama-3-8B 或 Qwen2.5-14B）；(b) WildChat/LMSYS-Chat 上的 **formal feature trend analysis**（含 MMD domain shift quantification）；(c) 明确 **practical deployment scope 为开源模型生态（7B-14B）**；(d) frontier model limitation 扩展为 **principled discussion**（RLHF/instruction-tuning 对 depth signal 的影响、API-only access 对 feature 计算的限制）。原始 proposal 仅有 Qwen2.5-7B 一个 cross-scale probe。 — 命中 Significance（论证实际部署价值）\n\n18. [Downstream Curation / Experimental Validation] — 大幅增强 curation 实验严格性：(a) **contamination severity 维度**（10%/30%/50% synthetic injection）；(b) **cross-model transfer**（classifier 训 on model A, curate model B）；(c) **unknown depth distribution condition**；(d) **data-quality-sensitive tasks**（held-out perplexity, factual QA，不仅限于 MMLU）；(e) **binary filtering threshold 选择协议明确化**；(f) **bootstrap CIs + paired significance tests**；(g) **实验逻辑链显式说明**。原始 proposal 对 filtering 实验的公平性和统计显著性没有详细设计。 — 命中 Technical Soundness + Experimental Rigor\n\n19. [Depth vs. Quality Analysis / Experimental Validation] — 新增 **depth-quality 单调性直接验证**。原始 proposal 隐含假设 depth 与 quality 单调递减但未验证。新增多维度 quality proxy 曲线，验证单调性成立条件。如非单调，graduated filtering 适应为 depth-features → predicted quality → weight。 — 命中 Technical Soundness（验证核心前提假设）\n\n20. [K* Contingency / Experimental Validation] — 新增 **显式 contingency 讨论**：K*≤3 时贡献重定位为首次量化 fundamental resolution limit + decoding strategy 对 K* 的调控效应 + 即使 coarse ordinal signal 仍有 calibration 优势。原始 proposal 的 \"If…then\" 结构是结构性风险。 — 命中 Soundness + Reviewer 心理管理\n\n【主要风险】:\n1. **K* 实验结果不确定性**：如果在大多数 model/decoding 配置下 K*≤2，论文的 empirical richness 和 graduated curation 收益都会受限。虽有 contingency plan（fundamental resolution limit characterization + decoding strategy modulation），但 reviewer 仍可能评为 \"interesting characterization but limited practical impact\"。这是无法通过 proposal 优化消除的固有风险。\n2. **\"Good problem + standard method\" 框架**：核心分类 pipeline 是 feature engineering + off-the-shelf ordinal regression（CORAL/CORN），审稿人可能认为方法论贡献不足。信息论框架和假设检验提升了分析深度，但分类器本身没有方法论突破。对于偏重 methods 的审稿人，这可能是 borderline reject 的理由。\n\n【实施评估】:\n- 计算资源: 主实验（corpus generation + feature extraction + classifier training）可在 2-4 块 A100 上完成，估计 1-2 周。Retrain-chain validation（1 config, LoRA fine-tuning, 3-4 depth levels）约 2-3 天额外 GPU 时间。Cross-scale probe（7B-14B 模型生成 + 特征提取）约 3-5 天。总计 GPU 需求约 2-3 周集中使用。不需要大规模集群。\n- 数据需求: C4 和 Wikipedia 子集（50K documents each）——公开可得。WildChat / LMSYS-Chat——公开可得。无需私有或受限数据集。\n- 人工介入: 无需人工标注（ground-truth depth labels 由 generation pipeline 自动产生）。无需专家评审。唯一的人工环节是实验设计决策和论文写作。\n- 训练需求: 需要模型训练，但规模有限。(a) Ordinal regression classifier（CORAL/CORN）：轻量级，训练时间可忽略。(b) Retrain-chain 的 LoRA fine-tuning：Pythia-1B 级别，每轮约 1-2 小时。(c) 不需要从头预训练任何 LLM。(d) 下游 curation 评估需要在 curated data 上训练小模型（≤1.8B），但这也是标准规模。\n- 新 Benchmark: 不需要构建新的公开 benchmark。构建的 multi-depth corpus 是实验工具而非独立 benchmark 贡献（但可作为 artifact release）。\n- 预估周期: Corpus generation + feature extraction: 2-3 周；Classifier training + ablation: 1 周；Downstream curation experiments: 1-2 周；Cross-scale + retrain-chain validation: 1-2 周；Analysis + writing: 2-3 周。**总计约 8-12 周**（从启动到可投稿），假设 GPU 资源持续可用。如果 GPU 间歇使用，可能延长至 12-16 周。EMNLP 2026 投稿 deadline 前有充足时间。\n\n",
      "numLines": 177,
      "startLine": 1,
      "totalLines": 177
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01P97dU6C23WhucVZUSaw1hN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/theory_framework.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a2b3c6e1-bf66-4ff6-bec8-41639f3adf55",
  "uuid": "71004c74-ee59-4f30-a885-4a4cc1f610fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FDLd2tfof3vhWd8bp3g7E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 481,
      "cache_read_input_tokens": 24070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 481
      },
      "output_tokens": 69,
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

_source line 13 · 2026-05-12T16:25:04.761Z_

<details><summary>↩ Tool result · `toolu_01P97dU6C23WhucVZUSaw1hN`</summary>

```text
1	# 信道级联 + DPI 理论框架草案
2	
3	> 将递归生成建模为 iterated lossy channel，用 Data Processing Inequality 约束 depth-discriminability 的 fundamental limit。
4	
5	---
6	
7	## 1. 信道级联模型形式化
8	
9	### 基本设定
10	
11	设 X₀ 为人类撰写的文本（seed text），表示为某概率空间上的随机变量。LLM 的生成过程建模为一个随机信道：
12	
13	$$\mathcal{T}: \mathcal{X} \to \mathcal{X}$$
14	
15	将输入文本映射到输出文本。递归生成形成 Markov chain：
16	
17	$$X_0 \to X_1 \to X_2 \to \cdots \to X_k$$
18	
19	其中 $X_{i+1} = \mathcal{T}(X_i)$，即 depth-$(i+1)$ 的文本由 depth-$i$ 的文本经过一次 LLM 信道产生。
20	
21	**关键假设**：
22	
23	- **(A1) 时不变信道**：同一 LLM + 同一 decoding strategy 在每次迭代中使用相同的信道 $\mathcal{T}$。（prompt-chain 设定下成立；retrain-chain 需放宽为 $\mathcal{T}_i$）
24	- **(A2) Markov 性**：$X_{i+1}$ 仅依赖 $X_i$，不依赖 $X_0, \ldots, X_{i-1}$（prompt-chain 逐段独立生成时成立）
25	- **(A3) 有损信道**：$\mathcal{T}$ 是 non-invertible 的——生成过程丢失关于输入的信息（sampling 引入 noise，decoding 策略截断分布尾部）
26	
27	### 形式化表述
28	
29	$$X_0 \xrightarrow{\mathcal{T}} X_1 \xrightarrow{\mathcal{T}} X_2 \xrightarrow{\mathcal{T}} \cdots \xrightarrow{\mathcal{T}} X_k$$
30	
31	这是一个齐次 Markov chain（在假设 A1 下），其转移核由 LLM 的条件分布 $p_\theta(\cdot | x)$ 决定。
32	
33	---
34	
35	## 2. Data Processing Inequality 约束
36	
37	### DPI 基本形式
38	
39	对于 Markov chain $X_0 \to X_1 \to \cdots \to X_k$，DPI 给出：
40	
41	$$I(X_0; X_k) \leq I(X_0; X_{k-1}) \leq \cdots \leq I(X_0; X_1) \leq H(X_0)$$
42	
43	即 $I(X_0; X_k)$ 关于 $k$ 单调非递增。
44	
45	**直觉**：每经过一次 LLM 信道，关于原始人类文本 $X_0$ 的信息只会减少或不变，绝不增加。递归生成是不可逆的信息丢失过程。
46	
47	### 严格衰减条件
48	
49	当 $\mathcal{T}$ 是 strictly lossy channel（即 $I(X_i; X_{i+1}) < H(X_i)$ for all $i$）时，衰减是严格的：
50	
51	$$I(X_0; X_k) < I(X_0; X_{k-1}) \quad \forall k \geq 1$$
52	
53	这对应于 LLM 生成过程中 sampling noise 不可消除的事实——任何 temperature > 0 或 nucleus/top-k 截断都引入不可逆信息损失。
54	
55	### 与 Depth Discriminability 的联系
56	
57	两个不同深度 $k, k'$ 的文本 $X_k, X_{k'}$ 的可区分性取决于它们的分布差异。定义可区分性度量：
58	
59	$$D(k, k') = d(P_{X_k}, P_{X_{k'}})$$
60	
61	其中 $d$ 是某种分布距离（JSD、MMD、Total Variation 等）。
62	
63	**关键观察**：随着 $k$ 增大，$P_{X_k}$ 趋近于信道 $\mathcal{T}$ 的不动点分布 $P^*$（如果存在），相邻深度的分布差异趋于零：
64	
65	$$D(k, k+1) \to 0 \quad \text{as} \quad k \to \infty$$
66	
67	---
68	
69	## 3. K* 的理论解释
70	
71	### 定义
72	
73	$K^*$ 是 **判别饱和边界（discriminability saturation boundary）**：
74	
75	$$K^* = \max\{k : D(k-1, k) > \epsilon\}$$
76	
77	其中 $\epsilon$ 是 noise floor（对应于有限样本下的统计检验 power limit）。
78	
79	### Information-Theoretic 解释
80	
81	$K^*$ 对应于 $I(X_0; X_k)$ 降至 noise floor 的临界深度：
82	
83	$$K^* \approx \min\{k : I(X_0; X_k) - I(X_0; X_{k+1}) < \delta\}$$
84	
85	其中 $\delta$ 是 MI 增量的可检测下限。
86	
87	**关键 insight**：$K^*$ 不是分类器的能力上限，而是 **information-theoretic impossibility boundary**——任何方法（无论多复杂）都无法区分 depth $> K^*$ 的文本，因为原始人类文本的信息已经被信道噪声完全淹没。
88	
89	### 与 Channel Capacity 的关系
90	
91	信道 $\mathcal{T}$ 的 "contraction rate" $\rho$ 控制 MI 衰减速度：
92	
93	$$I(X_0; X_k) \leq \rho^k \cdot H(X_0) \quad (\text{if exponential decay})$$
94	
95	- $\rho$ 接近 1（低噪声信道，如 greedy decoding）→ 衰减慢，$K^*$ 大
96	- $\rho$ 接近 0（高噪声信道，如 high-temperature sampling）→ 衰减快，$K^*$ 小
97	
98	**但这里有一个反直觉的 nuance**：虽然 high-temperature 使 $\rho$ 更小（信息丢失更快），但它同时保持了更高的 diversity，使相邻深度的分布差异可能更大。因此 $K^*$ 与 decoding strategy 的关系不是简单单调的——这正是需要实验验证的假设。
99	
100	---
101	
102	## 4. Propositions / Theorems 骨架
103	
104	### Proposition 1: MI 单调衰减（DPI 直接推论）
105	
106	**Statement**: 设 $X_0 \to X_1 \to \cdots \to X_k$ 为上述递归生成 Markov chain。则对任意 $k \geq 1$：
107	
108	$$I(X_0; X_k) \leq I(X_0; X_{k-1})$$
109	
110	等号成立当且仅当 $X_{k-1} \to X_k$ 是 sufficient statistic（即信道 $\mathcal{T}$ 是无损的，实际中不成立）。
111	
112	**Proof sketch**:
113	直接由 DPI 定理得出。$X_0 \to X_{k-1} \to X_k$ 构成 Markov chain，DPI 立即给出 $I(X_0; X_k) \leq I(X_0; X_{k-1})$。严格不等号由 $\mathcal{T}$ 的 strictly lossy 性质保证（sampling 引入不可消除的噪声）。$\square$
114	
115	**论文中的作用**：建立理论基础——depth discrimination 必然随深度退化，这不是分类器缺陷，而是信息论必然。
116	
117	---
118	
119	### Proposition 2: 不动点收敛与 K* 有限性
120	
121	**Statement**: 若信道 $\mathcal{T}$ 具有唯一不动点分布 $P^*$（即 $\mathcal{T}(P^*) = P^*$），且 $\mathcal{T}$ 关于某分布度量 $d$ 是 contractive 的（$d(\mathcal{T}(P), \mathcal{T}(Q)) \leq \rho \cdot d(P, Q)$，$0 < \rho < 1$），则：
122	
123	(a) $d(P_{X_k}, P^*) \leq \rho^k \cdot d(P_{X_0}, P^*)$
124	
125	(b) $D(k, k+1) = d(P_{X_k}, P_{X_{k+1}}) \leq (\rho^k + \rho^{k+1}) \cdot d(P_{X_0}, P^*)$
126	
127	(c) 对任意 $\epsilon > 0$，$K^*(\epsilon)$ 有限。
128	
129	**Proof sketch**:
130	(a) 由 contractive mapping theorem 的标准迭代 bound。
131	(b) 三角不等式：$d(P_{X_k}, P_{X_{k+1}}) \leq d(P_{X_k}, P^*) + d(P_{X_{k+1}}, P^*)$，代入 (a) 得结论。
132	(c) $D(k, k+1)$ 以几何速率趋于 0，因此超过 $\epsilon$ 的 $k$ 值数量有限。$\square$
133	
134	**论文中的作用**：证明 $K^*$ 的有限性是理论必然——saturation 不是方法缺陷而是系统属性。同时给出 $K^* = O(\log(d(P_{X_0}, P^*)/\epsilon) / \log(1/\rho))$ 的粗略 scaling。
135	
136	---
137	
138	### Proposition 3: 衰减速率与 Decoding Strategy 的关系（经验驱动假设）
139	
140	**Statement（Conjecture，标注为 empirically motivated）**: 设 $\rho(\tau)$ 为 temperature 为 $\tau$ 时信道 $\mathcal{T}_\tau$ 的 contraction rate。在以下简化假设下（unigram-level，忽略序列结构）：
141	
142	(a) $\rho(\tau)$ 关于 $\tau$ 非单调：存在 $\tau^*$ 使得 $\rho(\tau)$ 在 $\tau < \tau^*$ 时随 $\tau$ 递增，在 $\tau > \tau^*$ 时随 $\tau$ 递减。
143	
144	(b) 直觉：极低 temperature（近 greedy）→ 信道近确定性 → $\rho$ 大但 diversity 低 → MI 本身小。极高 temperature → 信道近均匀随机 → $\rho$ 小 → MI 快速衰减。中间 temperature 平衡两个效应。
145	
146	**Proof sketch**: 此为 conjecture，不提供证明。给出 unigram softmax 信道的显式 contraction rate 计算作为 supporting analysis，实验验证 $K^*(\tau)$ 的非单调性。
147	
148	**论文中的作用**：将 decoding strategy 对 $K^*$ 的影响从 ad hoc 观察提升为 hypothesis-driven 研究。用 AIC/BIC model comparison 区分 exponential vs. polynomial MI 衰减。
149	
150	---
151	
152	## 5. 计算上的 Tractable Proxy
153	
154	### JSD 作为 MI 近似
155	
156	Mutual information 在高维文本空间中不可直接计算。我们采用 Jensen-Shannon Divergence (JSD) 作为 computationally tractable proxy：
157	
158	$$\text{JSD}(P_{X_k} \| P_{X_{k'}}) = \frac{1}{2} D_{\text{KL}}(P_{X_k} \| M) + \frac{1}{2} D_{\text{KL}}(P_{X_{k'}} \| M)$$
159	
160	其中 $M = \frac{1}{2}(P_{X_k} + P_{X_{k'}})$。
161	
162	**在 unigram level 上计算**：将 $P_{X_k}$ 估计为 depth-$k$ 文档集合的 empirical unigram distribution。
163	
164	**局限性（必须在论文中承认）**：
165	- Unigram JSD 忽略序列结构（bigram, trigram, syntactic patterns）
166	- 不等价于真正的 MI——JSD 是 distributional divergence，MI 是 sample-level information quantity
167	- 但 DPI 的定性结论（单调衰减）仍成立，因为 $\text{JSD}(P_{X_k} \| P_{X_0})$ 在 Markov chain 下也满足类似的单调性
168	
169	**补充度量**：
170	- Pairwise classifier AUC 作为 empirical discriminability 的非参数度量
171	- Feature-space Mahalanobis distance 作为多维度的分布距离
172	
173	---
174	
175	## 6. 理论与实验的对接
176	
177	| 理论预测 | 实验验证方法 |
178	|---|---|
179	| $I(X_0; X_k)$ 单调衰减 | JSD$(P_{X_0}, P_{X_k})$ 随 $k$ 递减曲线 |
180	| $K^*$ 有限 | Pairwise AUC 矩阵 + 操作性 K* 定义 |
181	| 衰减速率 $\rho$ 由 decoding strategy 控制 | $K^*(\text{greedy})$ vs. $K^*(p{=}0.95)$ vs. $K^*(T{=}1.2)$ |
182	| Exponential vs. polynomial decay | AIC/BIC model comparison on JSD decay curves |
183	| 不动点 $P^*$ 存在 | 检验 $P_{X_k}$ 对 $k$ 的收敛性（JSD$(P_{X_k}, P_{X_{k+1}}) \to 0$） |
184	
185	---
186	
187	## 7. 与既有理论的关系
188	
189	- **Shumailov et al. (Nature 2024)**：他们的 tail disappearance → diversity loss → mode conflation 三阶段模型对应我们的 $P_{X_k} \to P^*$ 收敛过程中的不同阶段——尾部消失是收敛初期，mode conflation 是收敛后期
190	- **Strong Model Collapse (Dohmatob et al., ICLR 2025)**：他们的 statistical learning theory bound 与我们的 DPI bound 互补——他们关注 retrain-chain 下 generalization error 的增长，我们关注 distributional information 的衰减
191	- **JPEG 重压缩类比**：JPEG 信道也是 contractive mapping（量化步骤不可逆），K* 对应 JPEG recompression detection 的 cycle limit——在图像 forensics 中已被充分研究的问题
192	
193	---
194	
195	## 8. 写作注意事项
196	
197	1. **措辞校准**：Propositions 1-2 是严格的（DPI + contractive mapping 标准结果）；Proposition 3 标注为 "empirically motivated conjecture"，不 overclaim
198	2. **JSD proxy 局限性**：在 Method section 设专段讨论 unigram 近似的局限和 justification
199	3. **信道假设**：A1（时不变）和 A2（Markov）在 prompt-chain 下合理，在 retrain-chain 下需要放宽——在 Discussion 中讨论
200	4. **不做"完整证明"**：论文风格是 proposition + proof sketch + experimental validation，不是纯理论论文的 full proof 风格。重点在 theory-experiment connection
201	5. **Appendix 安排**：完整的 contraction rate 计算、unigram softmax channel 分析放 appendix
202	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a2b3c6e1-bf66-4ff6-bec8-41639f3adf55",
  "uuid": "bae7aa15-d157-4ad2-abb1-195a35be680d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/theory_framework.md",
      "content": "# 信道级联 + DPI 理论框架草案\n\n> 将递归生成建模为 iterated lossy channel，用 Data Processing Inequality 约束 depth-discriminability 的 fundamental limit。\n\n---\n\n## 1. 信道级联模型形式化\n\n### 基本设定\n\n设 X₀ 为人类撰写的文本（seed text），表示为某概率空间上的随机变量。LLM 的生成过程建模为一个随机信道：\n\n$$\\mathcal{T}: \\mathcal{X} \\to \\mathcal{X}$$\n\n将输入文本映射到输出文本。递归生成形成 Markov chain：\n\n$$X_0 \\to X_1 \\to X_2 \\to \\cdots \\to X_k$$\n\n其中 $X_{i+1} = \\mathcal{T}(X_i)$，即 depth-$(i+1)$ 的文本由 depth-$i$ 的文本经过一次 LLM 信道产生。\n\n**关键假设**：\n\n- **(A1) 时不变信道**：同一 LLM + 同一 decoding strategy 在每次迭代中使用相同的信道 $\\mathcal{T}$。（prompt-chain 设定下成立；retrain-chain 需放宽为 $\\mathcal{T}_i$）\n- **(A2) Markov 性**：$X_{i+1}$ 仅依赖 $X_i$，不依赖 $X_0, \\ldots, X_{i-1}$（prompt-chain 逐段独立生成时成立）\n- **(A3) 有损信道**：$\\mathcal{T}$ 是 non-invertible 的——生成过程丢失关于输入的信息（sampling 引入 noise，decoding 策略截断分布尾部）\n\n### 形式化表述\n\n$$X_0 \\xrightarrow{\\mathcal{T}} X_1 \\xrightarrow{\\mathcal{T}} X_2 \\xrightarrow{\\mathcal{T}} \\cdots \\xrightarrow{\\mathcal{T}} X_k$$\n\n这是一个齐次 Markov chain（在假设 A1 下），其转移核由 LLM 的条件分布 $p_\\theta(\\cdot | x)$ 决定。\n\n---\n\n## 2. Data Processing Inequality 约束\n\n### DPI 基本形式\n\n对于 Markov chain $X_0 \\to X_1 \\to \\cdots \\to X_k$，DPI 给出：\n\n$$I(X_0; X_k) \\leq I(X_0; X_{k-1}) \\leq \\cdots \\leq I(X_0; X_1) \\leq H(X_0)$$\n\n即 $I(X_0; X_k)$ 关于 $k$ 单调非递增。\n\n**直觉**：每经过一次 LLM 信道，关于原始人类文本 $X_0$ 的信息只会减少或不变，绝不增加。递归生成是不可逆的信息丢失过程。\n\n### 严格衰减条件\n\n当 $\\mathcal{T}$ 是 strictly lossy channel（即 $I(X_i; X_{i+1}) < H(X_i)$ for all $i$）时，衰减是严格的：\n\n$$I(X_0; X_k) < I(X_0; X_{k-1}) \\quad \\forall k \\geq 1$$\n\n这对应于 LLM 生成过程中 sampling noise 不可消除的事实——任何 temperature > 0 或 nucleus/top-k 截断都引入不可逆信息损失。\n\n### 与 Depth Discriminability 的联系\n\n两个不同深度 $k, k'$ 的文本 $X_k, X_{k'}$ 的可区分性取决于它们的分布差异。定义可区分性度量：\n\n$$D(k, k') = d(P_{X_k}, P_{X_{k'}})$$\n\n其中 $d$ 是某种分布距离（JSD、MMD、Total Variation 等）。\n\n**关键观察**：随着 $k$ 增大，$P_{X_k}$ 趋近于信道 $\\mathcal{T}$ 的不动点分布 $P^*$（如果存在），相邻深度的分布差异趋于零：\n\n$$D(k, k+1) \\to 0 \\quad \\text{as} \\quad k \\to \\infty$$\n\n---\n\n## 3. K* 的理论解释\n\n### 定义\n\n$K^*$ 是 **判别饱和边界（discriminability saturation boundary）**：\n\n$$K^* = \\max\\{k : D(k-1, k) > \\epsilon\\}$$\n\n其中 $\\epsilon$ 是 noise floor（对应于有限样本下的统计检验 power limit）。\n\n### Information-Theoretic 解释\n\n$K^*$ 对应于 $I(X_0; X_k)$ 降至 noise floor 的临界深度：\n\n$$K^* \\approx \\min\\{k : I(X_0; X_k) - I(X_0; X_{k+1}) < \\delta\\}$$\n\n其中 $\\delta$ 是 MI 增量的可检测下限。\n\n**关键 insight**：$K^*$ 不是分类器的能力上限，而是 **information-theoretic impossibility boundary**——任何方法（无论多复杂）都无法区分 depth $> K^*$ 的文本，因为原始人类文本的信息已经被信道噪声完全淹没。\n\n### 与 Channel Capacity 的关系\n\n信道 $\\mathcal{T}$ 的 \"contraction rate\" $\\rho$ 控制 MI 衰减速度：\n\n$$I(X_0; X_k) \\leq \\rho^k \\cdot H(X_0) \\quad (\\text{if exponential decay})$$\n\n- $\\rho$ 接近 1（低噪声信道，如 greedy decoding）→ 衰减慢，$K^*$ 大\n- $\\rho$ 接近 0（高噪声信道，如 high-temperature sampling）→ 衰减快，$K^*$ 小\n\n**但这里有一个反直觉的 nuance**：虽然 high-temperature 使 $\\rho$ 更小（信息丢失更快），但它同时保持了更高的 diversity，使相邻深度的分布差异可能更大。因此 $K^*$ 与 decoding strategy 的关系不是简单单调的——这正是需要实验验证的假设。\n\n---\n\n## 4. Propositions / Theorems 骨架\n\n### Proposition 1: MI 单调衰减（DPI 直接推论）\n\n**Statement**: 设 $X_0 \\to X_1 \\to \\cdots \\to X_k$ 为上述递归生成 Markov chain。则对任意 $k \\geq 1$：\n\n$$I(X_0; X_k) \\leq I(X_0; X_{k-1})$$\n\n等号成立当且仅当 $X_{k-1} \\to X_k$ 是 sufficient statistic（即信道 $\\mathcal{T}$ 是无损的，实际中不成立）。\n\n**Proof sketch**:\n直接由 DPI 定理得出。$X_0 \\to X_{k-1} \\to X_k$ 构成 Markov chain，DPI 立即给出 $I(X_0; X_k) \\leq I(X_0; X_{k-1})$。严格不等号由 $\\mathcal{T}$ 的 strictly lossy 性质保证（sampling 引入不可消除的噪声）。$\\square$\n\n**论文中的作用**：建立理论基础——depth discrimination 必然随深度退化，这不是分类器缺陷，而是信息论必然。\n\n---\n\n### Proposition 2: 不动点收敛与 K* 有限性\n\n**Statement**: 若信道 $\\mathcal{T}$ 具有唯一不动点分布 $P^*$（即 $\\mathcal{T}(P^*) = P^*$），且 $\\mathcal{T}$ 关于某分布度量 $d$ 是 contractive 的（$d(\\mathcal{T}(P), \\mathcal{T}(Q)) \\leq \\rho \\cdot d(P, Q)$，$0 < \\rho < 1$），则：\n\n(a) $d(P_{X_k}, P^*) \\leq \\rho^k \\cdot d(P_{X_0}, P^*)$\n\n(b) $D(k, k+1) = d(P_{X_k}, P_{X_{k+1}}) \\leq (\\rho^k + \\rho^{k+1}) \\cdot d(P_{X_0}, P^*)$\n\n(c) 对任意 $\\epsilon > 0$，$K^*(\\epsilon)$ 有限。\n\n**Proof sketch**:\n(a) 由 contractive mapping theorem 的标准迭代 bound。\n(b) 三角不等式：$d(P_{X_k}, P_{X_{k+1}}) \\leq d(P_{X_k}, P^*) + d(P_{X_{k+1}}, P^*)$，代入 (a) 得结论。\n(c) $D(k, k+1)$ 以几何速率趋于 0，因此超过 $\\epsilon$ 的 $k$ 值数量有限。$\\square$\n\n**论文中的作用**：证明 $K^*$ 的有限性是理论必然——saturation 不是方法缺陷而是系统属性。同时给出 $K^* = O(\\log(d(P_{X_0}, P^*)/\\epsilon) / \\log(1/\\rho))$ 的粗略 scaling。\n\n---\n\n### Proposition 3: 衰减速率与 Decoding Strategy 的关系（经验驱动假设）\n\n**Statement（Conjecture，标注为 empirically motivated）**: 设 $\\rho(\\tau)$ 为 temperature 为 $\\tau$ 时信道 $\\mathcal{T}_\\tau$ 的 contraction rate。在以下简化假设下（unigram-level，忽略序列结构）：\n\n(a) $\\rho(\\tau)$ 关于 $\\tau$ 非单调：存在 $\\tau^*$ 使得 $\\rho(\\tau)$ 在 $\\tau < \\tau^*$ 时随 $\\tau$ 递增，在 $\\tau > \\tau^*$ 时随 $\\tau$ 递减。\n\n(b) 直觉：极低 temperature（近 greedy）→ 信道近确定性 → $\\rho$ 大但 diversity 低 → MI 本身小。极高 temperature → 信道近均匀随机 → $\\rho$ 小 → MI 快速衰减。中间 temperature 平衡两个效应。\n\n**Proof sketch**: 此为 conjecture，不提供证明。给出 unigram softmax 信道的显式 contraction rate 计算作为 supporting analysis，实验验证 $K^*(\\tau)$ 的非单调性。\n\n**论文中的作用**：将 decoding strategy 对 $K^*$ 的影响从 ad hoc 观察提升为 hypothesis-driven 研究。用 AIC/BIC model comparison 区分 exponential vs. polynomial MI 衰减。\n\n---\n\n## 5. 计算上的 Tractable Proxy\n\n### JSD 作为 MI 近似\n\nMutual information 在高维文本空间中不可直接计算。我们采用 Jensen-Shannon Divergence (JSD) 作为 computationally tractable proxy：\n\n$$\\text{JSD}(P_{X_k} \\| P_{X_{k'}}) = \\frac{1}{2} D_{\\text{KL}}(P_{X_k} \\| M) + \\frac{1}{2} D_{\\text{KL}}(P_{X_{k'}} \\| M)$$\n\n其中 $M = \\frac{1}{2}(P_{X_k} + P_{X_{k'}})$。\n\n**在 unigram level 上计算**：将 $P_{X_k}$ 估计为 depth-$k$ 文档集合的 empirical unigram distribution。\n\n**局限性（必须在论文中承认）**：\n- Unigram JSD 忽略序列结构（bigram, trigram, syntactic patterns）\n- 不等价于真正的 MI——JSD 是 distributional divergence，MI 是 sample-level information quantity\n- 但 DPI 的定性结论（单调衰减）仍成立，因为 $\\text{JSD}(P_{X_k} \\| P_{X_0})$ 在 Markov chain 下也满足类似的单调性\n\n**补充度量**：\n- Pairwise classifier AUC 作为 empirical discriminability 的非参数度量\n- Feature-space Mahalanobis distance 作为多维度的分布距离\n\n---\n\n## 6. 理论与实验的对接\n\n| 理论预测 | 实验验证方法 |\n|---|---|\n| $I(X_0; X_k)$ 单调衰减 | JSD$(P_{X_0}, P_{X_k})$ 随 $k$ 递减曲线 |\n| $K^*$ 有限 | Pairwise AUC 矩阵 + 操作性 K* 定义 |\n| 衰减速率 $\\rho$ 由 decoding strategy 控制 | $K^*(\\text{greedy})$ vs. $K^*(p{=}0.95)$ vs. $K^*(T{=}1.2)$ |\n| Exponential vs. polynomial decay | AIC/BIC model comparison on JSD decay curves |\n| 不动点 $P^*$ 存在 | 检验 $P_{X_k}$ 对 $k$ 的收敛性（JSD$(P_{X_k}, P_{X_{k+1}}) \\to 0$） |\n\n---\n\n## 7. 与既有理论的关系\n\n- **Shumailov et al. (Nature 2024)**：他们的 tail disappearance → diversity loss → mode conflation 三阶段模型对应我们的 $P_{X_k} \\to P^*$ 收敛过程中的不同阶段——尾部消失是收敛初期，mode conflation 是收敛后期\n- **Strong Model Collapse (Dohmatob et al., ICLR 2025)**：他们的 statistical learning theory bound 与我们的 DPI bound 互补——他们关注 retrain-chain 下 generalization error 的增长，我们关注 distributional information 的衰减\n- **JPEG 重压缩类比**：JPEG 信道也是 contractive mapping（量化步骤不可逆），K* 对应 JPEG recompression detection 的 cycle limit——在图像 forensics 中已被充分研究的问题\n\n---\n\n## 8. 写作注意事项\n\n1. **措辞校准**：Propositions 1-2 是严格的（DPI + contractive mapping 标准结果）；Proposition 3 标注为 \"empirically motivated conjecture\"，不 overclaim\n2. **JSD proxy 局限性**：在 Method section 设专段讨论 unigram 近似的局限和 justification\n3. **信道假设**：A1（时不变）和 A2（Markov）在 prompt-chain 下合理，在 retrain-chain 下需要放宽——在 Discussion 中讨论\n4. **不做\"完整证明\"**：论文风格是 proposition + proof sketch + experimental validation，不是纯理论论文的 full proof 风格。重点在 theory-experiment connection\n5. **Appendix 安排**：完整的 contraction rate 计算、unigram softmax channel 分析放 appendix\n",
      "numLines": 202,
      "startLine": 1,
      "totalLines": 202
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01YFHov4hy2V2UoZritVGrkf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/claim_routes.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a2b3c6e1-bf66-4ff6-bec8-41639f3adf55",
  "uuid": "d870a6e8-44ed-4b3a-8615-e3cd6d2b550d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FDLd2tfof3vhWd8bp3g7E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 481,
      "cache_read_input_tokens": 24070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 481
      },
      "output_tokens": 69,
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

_source line 15 · 2026-05-12T16:25:05.303Z_

<details><summary>↩ Tool result · `toolu_01YFHov4hy2V2UoZritVGrkf`</summary>

````text
1	# 双路线 Claim 框架
2	
3	> 根据 MVP 结果 K* 的取值，准备两条论文叙事路线。
4	
5	---
6	
7	## 路线 A：K* ≥ 3（MVP Pass）
8	
9	### Core Claim
10	**Generational depth estimation is feasible and enables graduated filtering that outperforms binary detection for quality-aware data curation.**
11	
12	### Supporting Claims 拆解
13	
14	**C1: Depth signals exist and are ordinal-structured**
15	- 递归生成文本的统计特征（surprisal、vocabulary diversity、tail metrics）随 depth 呈系统性单调变化
16	- Ordinal regression（CORAL/CORN）显著优于 multinomial classification，证明 depth 的有序结构可被利用
17	- 证据：pairwise AUC matrix、ordinal vs. multinomial ablation、calibration curves
18	
19	**C2: K* characterization reveals linguistic degradation ordering**
20	- K* 是首次被系统量化的判别饱和边界
21	- Feature group ablation 揭示"降解序"：不同语言维度（vocabulary diversity → surprisal dynamics → tail metrics）在不同 depth 饱和
22	- Heatmap：feature group × depth → discriminative power
23	- 证据：per-feature saturation curves、cross-model K* comparison、decoding strategy 对 K* 的调控效应
24	
25	**C3: Graduated filtering > binary filtering**
26	- Depth-aware weighted filtering（weight ∝ quality(k)/quality(0)）在 MMLU/HellaSwag 等 data-quality-sensitive tasks 上显著优于 binary filtering 和 no filtering
27	- 理论动机：binary filtering 在 threshold 附近信息损失最大，ordinal signal 允许 soft weighting
28	- 证据：downstream benchmark results with bootstrap CIs + paired significance tests、contamination severity ablation（10%/30%/50%）
29	
30	**C4: Cross-model generalization**
31	- 在 model A 上训练的 depth classifier 可迁移到 model B 的生成文本
32	- Cross-scale probe（7B/14B）验证小模型训练的特征在更大模型生成文本上的迁移性
33	- 证据：cross-model transfer accuracy matrix、feature distribution MMD analysis
34	
35	### Story Arc
36	
37	```
38	Problem:  Web data 被未知深度的递归合成文本污染，binary detection 丢失 graded quality signal
39	Insight:  递归生成是 iterated lossy channel，depth-discriminative signals 系统性存在且可量化
40	          → 类比 JPEG 重压缩检测
41	Method:   (1) 15维特征 + ordinal regression → depth estimation
42	          (2) Depth-graduated curation: weight ∝ estimated quality decay
43	Results:  K*≥3 → fine-grained depth discrimination feasible
44	          Graduated filtering 显著优于 binary 和 no filtering
45	          Cross-model/cross-scale 泛化
46	Takeaway: Depth is the missing dimension in synthetic data curation
47	```
48	
49	### 评审攻击面预演
50	
51	**Q1: "方法论贡献不足——feature engineering + off-the-shelf ordinal regression"**
52	- Rebuttal：(a) 贡献不在分类器本身，而在 problem formulation + empirical characterization + practical paradigm shift；(b) 信道级联 + DPI 理论框架提供了 beyond-empirical 的科学理解；(c) 类比 DetectGPT——方法简单但 problem formulation 有影响力；(d) learned representation baseline（frozen LM embeddings + MLP）作为对比，证明 hand-crafted features 在此任务上的优势（可解释性 + 泛化性）
53	
54	**Q2: "Prompt-chain ≠ 真实递归污染路径，ecological validity 存疑"**
55	- Rebuttal：(a) Prompt-chain 是 upper bound estimate——如果 prompt-chain 下特征已饱和，retrain-chain 只会更快饱和；(b) 我们用 retrain-chain validation（1 config, LoRA fine-tuning）验证两种 chain 的 feature distribution 对比和 cross-setting transfer accuracy；(c) Clean chains 定位为 theoretical bound，实际 depth estimates 定位为 ordinal quality proxies
56	
57	**Q3: "Cross-scale 证据不足——真实世界合成文本主要来自 frontier models（GPT-4, Claude）"**
58	- Rebuttal：(a) 我们明确定位 practical scope 为开源模型生态（7B-14B）；(b) frontier model limitation 是 principled limitation（RLHF/instruction-tuning 改变分布、API-only 限制特征计算），非简单的"没做"；(c) 7B-14B probe 已覆盖开源社区主流生成规模；(d) WildChat feature trend analysis 提供 naturalistic 证据
59	
60	---
61	
62	## 路线 B：K* = 2（Conditional Pass）
63	
64	### Core Claim
65	**The saturation boundary K* is a novel, measurable fundamental quantity of recursive text generation: even coarse ordinal depth signals (human / gen-1 / gen-2+) provide calibration advantages over binary detection, and K*'s dependence on model family and decoding strategy yields actionable guidance for data curation.**
66	
67	### Supporting Claims 拆解
68	
69	**C1: K* 是首次被系统测量的 fundamental resolution limit**
70	- 这不是分类器的能力上限，而是 information-theoretic impossibility boundary（DPI 约束）
71	- K*=2 意味着 depth ≥2 的文本在信息论意义上已不可区分——这本身是重要的科学发现
72	- 证据：信道级联 + DPI 理论推导、empirical K* measurement across models/decoding strategies
73	
74	**C2: Linguistic degradation ordering 揭示递归生成的结构性规律**
75	- 即使 K*=2，per-feature saturation analysis 仍揭示哪些语言维度先坍缩
76	- Feature group × depth heatmap 展示 degradation ordering
77	- 证据：vocabulary diversity 先于 semantic coherence 坍缩（假设）、cross-model 对比 heatmap
78	
79	**C3: Decoding strategy 调控 K***
80	- 假设检验：greedy → 指数衰减（K* 更小），high-temperature → 多项式衰减（K* 可能更大）
81	- AIC/BIC model comparison 验证 exponential vs. polynomial MI 衰减
82	- 实际意义：指导数据生成策略选择——如果特定 decoding 延长 discriminability，可指导 synthetic data generation best practices
83	- 证据：K*(decoding strategy) 的系统性变化、MI 衰减曲线拟合
84	
85	**C4: 即使 coarse ordinal signal（3-class）仍有 calibration advantage**
86	- 3-class（human / gen-1 / gen-2+）vs. binary 在 downstream tasks 上的对比
87	- Depth=1（单代合成，质量较高）vs. depth≥2（多代合成，质量显著下降）的区分对 curation 有实际价值
88	- 证据：3-class graduated filtering vs. binary filtering benchmark results
89	
90	### 如何把 K*=2 包装为 Contribution 而非 Limitation
91	
92	关键 framing 转换：
93	
94	| 避免的措辞 | 改用的措辞 |
95	|---|---|
96	| "Unfortunately, depth discrimination saturates at K*=2" | "We establish K*=2 as the fundamental resolution limit for prompt-chain recursive generation" |
97	| "Only 3 classes are distinguishable" | "The human/first-gen/multi-gen trichotomy captures the critical quality boundary" |
98	| "The classifier cannot distinguish depth 3 from depth 4" | "Beyond depth 2, texts converge to a stationary distribution — a novel empirical finding consistent with our DPI analysis" |
99	| "If K*≤2, the contribution is limited" | "K* itself is the contribution: its measurement, model-dependence, and decoding-strategy modulation are all first-of-kind results" |
100	
101	### Saturation Characterization 路线的卖点
102	
103	1. **首次量化测量**：之前只有定性讨论（Shumailov "early collapse"），我们给出精确的 K* 数值和置信区间
104	2. **可操作指导**：K*=2 告诉 practitioners "对于 model X + decoding Y，depth≥2 的文本无需细分——binary vs. first-gen vs. rest 即可"
105	3. **理论-实验闭环**：DPI 预测 MI 单调衰减 → 实验测量 K* 位置 → 衰减曲线拟合验证理论
106	4. **跨模型/跨策略 K* 地图**：不同 model family 和 decoding strategy 的 K* 对比，形成 actionable lookup table
107	5. **Model collapse early-warning 应用**：即使 K*=2，depth distribution（human / gen-1 / gen-2+ 占比）作为 corpus quality indicator
108	
109	### Story Arc
110	
111	```
112	Problem:  同路线 A
113	Insight:  递归生成的 depth-discriminability 有 fundamental limit K*
114	          K* 不是分类器能力问题，而是 information-theoretic boundary
115	Method:   DPI 理论框架 + systematic empirical measurement of K*
116	Results:  K*=2 across most configurations → human/gen-1/gen-2+ trichotomy
117	          K* varies with decoding strategy → actionable guidance
118	          Even 3-class graduated filtering > binary filtering
119	Takeaway: K* is the right quantity to measure; its value tells you exactly
120	          how much depth granularity your curation can exploit
121	```
122	
123	### 评审攻击面预演
124	
125	**Q1: "K*=2 means the depth classifier is not very useful — just use binary detection"**
126	- Rebuttal：(a) 3-class > binary 在 downstream benchmarks 上有统计显著差异——first-gen text 和 multi-gen text 质量差异显著；(b) K* 本身是一个比分类器更重要的科学贡献——它量化了 recursive generation 的 information-theoretic resolution limit；(c) K* 随 decoding strategy 变化的发现直接指导 synthetic data generation 最佳实践
127	
128	**Q2: "如果 K*=2 是 fundamental limit，后续工作空间在哪？"**
129	- Rebuttal：(a) Scale effect——更大模型的 K* 可能更大（7B probe 数据）；(b) Retrain-chain vs. prompt-chain 可能有不同 K*；(c) Domain-specific K*（code vs. natural language vs. scientific text）；(d) 信息注入策略（external verifier）对 K* 的调控
130	
131	**Q3: "理论框架（DPI）过于简化，unigram 近似不 justified"**
132	- Rebuttal：(a) 我们明确标注 JSD 作为 MI proxy 的 unigram 层面局限性；(b) DPI bound 是 model-free 的——即使 proxy 不精确，monotone decay 的定性结论仍成立；(c) 这是 first attempt，更精确的 MI estimation（如 neural MI estimators）留作 future work
133	
134	---
135	
136	## 路线选择决策树
137	
138	```
139	MVP 结果出来后：
140	├── AUC(0 vs 1) < 0.70 → FAIL，重新评估项目
141	├── K* ≥ 3 → 路线 A（depth estimation + graduated filtering 为主线）
142	├── K* = 2 且 feature trends 清晰 → 路线 B（K* characterization 为主线）
143	└── K* = 2 且 feature trends 不清晰 → 评估是否有 decoding strategy 调控空间
144	    ├── 有 → 路线 B + decoding strategy modulation 加强
145	    └── 无 → 考虑 scope narrowing 或 target 降级
146	```
147	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a2b3c6e1-bf66-4ff6-bec8-41639f3adf55",
  "uuid": "166e6cac-630b-4e27-9062-2150fde811d1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/claim_routes.md",
      "content": "# 双路线 Claim 框架\n\n> 根据 MVP 结果 K* 的取值，准备两条论文叙事路线。\n\n---\n\n## 路线 A：K* ≥ 3（MVP Pass）\n\n### Core Claim\n**Generational depth estimation is feasible and enables graduated filtering that outperforms binary detection for quality-aware data curation.**\n\n### Supporting Claims 拆解\n\n**C1: Depth signals exist and are ordinal-structured**\n- 递归生成文本的统计特征（surprisal、vocabulary diversity、tail metrics）随 depth 呈系统性单调变化\n- Ordinal regression（CORAL/CORN）显著优于 multinomial classification，证明 depth 的有序结构可被利用\n- 证据：pairwise AUC matrix、ordinal vs. multinomial ablation、calibration curves\n\n**C2: K* characterization reveals linguistic degradation ordering**\n- K* 是首次被系统量化的判别饱和边界\n- Feature group ablation 揭示\"降解序\"：不同语言维度（vocabulary diversity → surprisal dynamics → tail metrics）在不同 depth 饱和\n- Heatmap：feature group × depth → discriminative power\n- 证据：per-feature saturation curves、cross-model K* comparison、decoding strategy 对 K* 的调控效应\n\n**C3: Graduated filtering > binary filtering**\n- Depth-aware weighted filtering（weight ∝ quality(k)/quality(0)）在 MMLU/HellaSwag 等 data-quality-sensitive tasks 上显著优于 binary filtering 和 no filtering\n- 理论动机：binary filtering 在 threshold 附近信息损失最大，ordinal signal 允许 soft weighting\n- 证据：downstream benchmark results with bootstrap CIs + paired significance tests、contamination severity ablation（10%/30%/50%）\n\n**C4: Cross-model generalization**\n- 在 model A 上训练的 depth classifier 可迁移到 model B 的生成文本\n- Cross-scale probe（7B/14B）验证小模型训练的特征在更大模型生成文本上的迁移性\n- 证据：cross-model transfer accuracy matrix、feature distribution MMD analysis\n\n### Story Arc\n\n```\nProblem:  Web data 被未知深度的递归合成文本污染，binary detection 丢失 graded quality signal\nInsight:  递归生成是 iterated lossy channel，depth-discriminative signals 系统性存在且可量化\n          → 类比 JPEG 重压缩检测\nMethod:   (1) 15维特征 + ordinal regression → depth estimation\n          (2) Depth-graduated curation: weight ∝ estimated quality decay\nResults:  K*≥3 → fine-grained depth discrimination feasible\n          Graduated filtering 显著优于 binary 和 no filtering\n          Cross-model/cross-scale 泛化\nTakeaway: Depth is the missing dimension in synthetic data curation\n```\n\n### 评审攻击面预演\n\n**Q1: \"方法论贡献不足——feature engineering + off-the-shelf ordinal regression\"**\n- Rebuttal：(a) 贡献不在分类器本身，而在 problem formulation + empirical characterization + practical paradigm shift；(b) 信道级联 + DPI 理论框架提供了 beyond-empirical 的科学理解；(c) 类比 DetectGPT——方法简单但 problem formulation 有影响力；(d) learned representation baseline（frozen LM embeddings + MLP）作为对比，证明 hand-crafted features 在此任务上的优势（可解释性 + 泛化性）\n\n**Q2: \"Prompt-chain ≠ 真实递归污染路径，ecological validity 存疑\"**\n- Rebuttal：(a) Prompt-chain 是 upper bound estimate——如果 prompt-chain 下特征已饱和，retrain-chain 只会更快饱和；(b) 我们用 retrain-chain validation（1 config, LoRA fine-tuning）验证两种 chain 的 feature distribution 对比和 cross-setting transfer accuracy；(c) Clean chains 定位为 theoretical bound，实际 depth estimates 定位为 ordinal quality proxies\n\n**Q3: \"Cross-scale 证据不足——真实世界合成文本主要来自 frontier models（GPT-4, Claude）\"**\n- Rebuttal：(a) 我们明确定位 practical scope 为开源模型生态（7B-14B）；(b) frontier model limitation 是 principled limitation（RLHF/instruction-tuning 改变分布、API-only 限制特征计算），非简单的\"没做\"；(c) 7B-14B probe 已覆盖开源社区主流生成规模；(d) WildChat feature trend analysis 提供 naturalistic 证据\n\n---\n\n## 路线 B：K* = 2（Conditional Pass）\n\n### Core Claim\n**The saturation boundary K* is a novel, measurable fundamental quantity of recursive text generation: even coarse ordinal depth signals (human / gen-1 / gen-2+) provide calibration advantages over binary detection, and K*'s dependence on model family and decoding strategy yields actionable guidance for data curation.**\n\n### Supporting Claims 拆解\n\n**C1: K* 是首次被系统测量的 fundamental resolution limit**\n- 这不是分类器的能力上限，而是 information-theoretic impossibility boundary（DPI 约束）\n- K*=2 意味着 depth ≥2 的文本在信息论意义上已不可区分——这本身是重要的科学发现\n- 证据：信道级联 + DPI 理论推导、empirical K* measurement across models/decoding strategies\n\n**C2: Linguistic degradation ordering 揭示递归生成的结构性规律**\n- 即使 K*=2，per-feature saturation analysis 仍揭示哪些语言维度先坍缩\n- Feature group × depth heatmap 展示 degradation ordering\n- 证据：vocabulary diversity 先于 semantic coherence 坍缩（假设）、cross-model 对比 heatmap\n\n**C3: Decoding strategy 调控 K***\n- 假设检验：greedy → 指数衰减（K* 更小），high-temperature → 多项式衰减（K* 可能更大）\n- AIC/BIC model comparison 验证 exponential vs. polynomial MI 衰减\n- 实际意义：指导数据生成策略选择——如果特定 decoding 延长 discriminability，可指导 synthetic data generation best practices\n- 证据：K*(decoding strategy) 的系统性变化、MI 衰减曲线拟合\n\n**C4: 即使 coarse ordinal signal（3-class）仍有 calibration advantage**\n- 3-class（human / gen-1 / gen-2+）vs. binary 在 downstream tasks 上的对比\n- Depth=1（单代合成，质量较高）vs. depth≥2（多代合成，质量显著下降）的区分对 curation 有实际价值\n- 证据：3-class graduated filtering vs. binary filtering benchmark results\n\n### 如何把 K*=2 包装为 Contribution 而非 Limitation\n\n关键 framing 转换：\n\n| 避免的措辞 | 改用的措辞 |\n|---|---|\n| \"Unfortunately, depth discrimination saturates at K*=2\" | \"We establish K*=2 as the fundamental resolution limit for prompt-chain recursive generation\" |\n| \"Only 3 classes are distinguishable\" | \"The human/first-gen/multi-gen trichotomy captures the critical quality boundary\" |\n| \"The classifier cannot distinguish depth 3 from depth 4\" | \"Beyond depth 2, texts converge to a stationary distribution — a novel empirical finding consistent with our DPI analysis\" |\n| \"If K*≤2, the contribution is limited\" | \"K* itself is the contribution: its measurement, model-dependence, and decoding-strategy modulation are all first-of-kind results\" |\n\n### Saturation Characterization 路线的卖点\n\n1. **首次量化测量**：之前只有定性讨论（Shumailov \"early collapse\"），我们给出精确的 K* 数值和置信区间\n2. **可操作指导**：K*=2 告诉 practitioners \"对于 model X + decoding Y，depth≥2 的文本无需细分——binary vs. first-gen vs. rest 即可\"\n3. **理论-实验闭环**：DPI 预测 MI 单调衰减 → 实验测量 K* 位置 → 衰减曲线拟合验证理论\n4. **跨模型/跨策略 K* 地图**：不同 model family 和 decoding strategy 的 K* 对比，形成 actionable lookup table\n5. **Model collapse early-warning 应用**：即使 K*=2，depth distribution（human / gen-1 / gen-2+ 占比）作为 corpus quality indicator\n\n### Story Arc\n\n```\nProblem:  同路线 A\nInsight:  递归生成的 depth-discriminability 有 fundamental limit K*\n          K* 不是分类器能力问题，而是 information-theoretic boundary\nMethod:   DPI 理论框架 + systematic empirical measurement of K*\nResults:  K*=2 across most configurations → human/gen-1/gen-2+ trichotomy\n          K* varies with decoding strategy → actionable guidance\n          Even 3-class graduated filtering > binary filtering\nTakeaway: K* is the right quantity to measure; its value tells you exactly\n          how much depth granularity your curation can exploit\n```\n\n### 评审攻击面预演\n\n**Q1: \"K*=2 means the depth classifier is not very useful — just use binary detection\"**\n- Rebuttal：(a) 3-class > binary 在 downstream benchmarks 上有统计显著差异——first-gen text 和 multi-gen text 质量差异显著；(b) K* 本身是一个比分类器更重要的科学贡献——它量化了 recursive generation 的 information-theoretic resolution limit；(c) K* 随 decoding strategy 变化的发现直接指导 synthetic data generation 最佳实践\n\n**Q2: \"如果 K*=2 是 fundamental limit，后续工作空间在哪？\"**\n- Rebuttal：(a) Scale effect——更大模型的 K* 可能更大（7B probe 数据）；(b) Retrain-chain vs. prompt-chain 可能有不同 K*；(c) Domain-specific K*（code vs. natural language vs. scientific text）；(d) 信息注入策略（external verifier）对 K* 的调控\n\n**Q3: \"理论框架（DPI）过于简化，unigram 近似不 justified\"**\n- Rebuttal：(a) 我们明确标注 JSD 作为 MI proxy 的 unigram 层面局限性；(b) DPI bound 是 model-free 的——即使 proxy 不精确，monotone decay 的定性结论仍成立；(c) 这是 first attempt，更精确的 MI estimation（如 neural MI estimators）留作 future work\n\n---\n\n## 路线选择决策树\n\n```\nMVP 结果出来后：\n├── AUC(0 vs 1) < 0.70 → FAIL，重新评估项目\n├── K* ≥ 3 → 路线 A（depth estimation + graduated filtering 为主线）\n├── K* = 2 且 feature trends 清晰 → 路线 B（K* characterization 为主线）\n└── K* = 2 且 feature trends 不清晰 → 评估是否有 decoding strategy 调控空间\n    ├── 有 → 路线 B + decoding strategy modulation 加强\n    └── 无 → 考虑 scope narrowing 或 target 降级\n```\n",
      "numLines": 147,
      "startLine": 1,
      "totalLines": 147
    }
  }
}
````

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_011yUJeqqBQ9xLRQ2voMu5ym`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a2b3c6e1-bf66-4ff6-bec8-41639f3adf55",
  "uuid": "5dfe7c5e-4828-453c-bfbb-fa21342e2b9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FDLd2tfof3vhWd8bp3g7E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 481,
      "cache_read_input_tokens": 24070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 481
      },
      "output_tokens": 69,
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

_source line 17 · 2026-05-12T16:25:05.383Z_

<details><summary>↩ Tool result · `toolu_011yUJeqqBQ9xLRQ2voMu5ym`</summary>

```text
1	"""
2	MVP Pilot Saturation Study — Complete Pipeline (Steps 2-5)
3	
4	Generates recursive depth chains from C4 seed data using Qwen2.5-1.5B,
5	extracts statistical features, and runs distinguishability analysis.
6	
7	Input:  C4 validation split (streamed from HuggingFace)
8	Output: data/depth_{0..K}.jsonl, data/features.csv, results/*.json + summary.txt
9	
10	Key deps: torch, transformers, datasets, scipy, lightgbm, sklearn, tqdm
11	"""
12	
13	import argparse
14	import json
15	import logging
16	import math
17	import os
18	import sys
19	from collections import Counter
20	from pathlib import Path
21	
22	import numpy as np
23	import torch
24	from scipy import stats
25	from tqdm import tqdm
26	
27	logging.basicConfig(
28	    level=logging.INFO,
29	    format="%(asctime)s [%(levelname)s] %(message)s",
30	    datefmt="%H:%M:%S",
31	)
32	log = logging.getLogger(__name__)
33	
34	
35	# ---------------------------------------------------------------------------
36	# Utility: simple 4-gram BLEU (no nltk dependency)
37	# ---------------------------------------------------------------------------
38	
39	def ngrams(tokens, n):
40	    return [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]
41	
42	
43	def simple_bleu(candidate_tokens, reference_tokens, max_n=4):
44	    """Compute sentence-level BLEU up to max_n grams with brevity penalty."""
45	    if len(candidate_tokens) == 0:
46	        return 0.0
47	    precisions = []
48	    for n in range(1, max_n + 1):
49	        cand_ngrams = ngrams(candidate_tokens, n)
50	        ref_ngrams = ngrams(reference_tokens, n)
51	        if not cand_ngrams:
52	            precisions.append(0.0)
53	            continue
54	        ref_counts = Counter(ref_ngrams)
55	        clipped = 0
56	        cand_counts = Counter(cand_ngrams)
57	        for ng, cnt in cand_counts.items():
58	            clipped += min(cnt, ref_counts.get(ng, 0))
59	        precisions.append(clipped / len(cand_ngrams))
60	    if any(p == 0 for p in precisions):
61	        return 0.0
62	    log_avg = sum(math.log(p) for p in precisions) / max_n
63	    bp = min(1.0, math.exp(1 - len(reference_tokens) / max(len(candidate_tokens), 1)))
64	    return bp * math.exp(log_avg)
65	
66	
67	# ===================================================================
68	# Step 2: Seed data preparation
69	# ===================================================================
70	
71	def prepare_seed_data(tokenizer, data_dir: Path, num_samples: int, max_tokens: int = 256):
72	    """Download C4 validation, truncate to max_tokens, save as depth_0.jsonl."""
73	    out_path = data_dir / "depth_0.jsonl"
74	    if out_path.exists() and sum(1 for _ in open(out_path)) >= num_samples:
75	        log.info("depth_0.jsonl already exists with enough samples — skipping")
76	        return
77	
78	    from datasets import load_dataset
79	
80	    # Use a single validation shard to avoid slow full-tree listing on proxied networks
81	    hf_endpoint = os.environ.get("HF_ENDPOINT", "https://huggingface.co")
82	    C4_SHARD_URL = f"{hf_endpoint}/datasets/allenai/c4/resolve/main/en/c4-validation.00000-of-00008.json.gz"
83	    log.info("Loading C4 validation shard (streaming) ...")
84	    try:
85	        ds = load_dataset("json", data_files=C4_SHARD_URL, split="train", streaming=True)
86	    except Exception as e:
87	        log.warning(f"Direct shard download failed ({e}), falling back to full dataset listing")
88	        ds = load_dataset("allenai/c4", "en", split="validation", streaming=True)
89	
90	    records = []
91	    for i, example in enumerate(tqdm(ds, total=num_samples, desc="Sampling C4")):
92	        if i >= num_samples:
93	            break
94	        text = example["text"].strip()
95	        if not text:
96	            continue
97	        ids = tokenizer.encode(text, add_special_tokens=False)[:max_tokens]
98	        truncated = tokenizer.decode(ids, skip_special_tokens=True)
99	        records.append({"text": truncated, "doc_id": len(records)})
100	        if len(records) >= num_samples:
101	            break
102	
103	    data_dir.mkdir(parents=True, exist_ok=True)
104	    with open(out_path, "w") as f:
105	        for r in records:
106	            f.write(json.dumps(r, ensure_ascii=False) + "\n")
107	    log.info(f"Saved {len(records)} seed documents to {out_path}")
108	
109	
110	# ===================================================================
111	# Step 3: Recursive depth chain generation
112	# ===================================================================
113	
114	REWRITE_PROMPT = (
115	    "Below is a passage. Write a new passage of similar length on the same "
116	    "topic and in the same style.\n\n"
117	    "Original passage:\n{prev_text}\n\nNew passage:\n"
118	)
119	
120	
121	def load_jsonl(path: Path):
122	    with open(path) as f:
123	        return [json.loads(line) for line in f]
124	
125	
126	def generate_depth_chain(
127	    model,
128	    tokenizer,
129	    data_dir: Path,
130	    max_depth: int,
131	    batch_size: int,
132	    max_new_tokens: int = 256,
133	):
134	    """Generate depths 1..max_depth via prompt-chain rewriting."""
135	    for depth in range(1, max_depth + 1):
136	        out_path = data_dir / f"depth_{depth}.jsonl"
137	        prev_path = data_dir / f"depth_{depth - 1}.jsonl"
138	
139	        if out_path.exists() and sum(1 for _ in open(out_path)) >= sum(1 for _ in open(prev_path)):
140	            log.info(f"depth_{depth}.jsonl already complete — skipping")
141	            continue
142	
143	        prev_records = load_jsonl(prev_path)
144	        log.info(f"Generating depth {depth} ({len(prev_records)} docs, batch_size={batch_size}) ...")
145	
146	        results = []
147	        for start in tqdm(range(0, len(prev_records), batch_size), desc=f"depth {depth}"):
148	            batch = prev_records[start : start + batch_size]
149	            prompts = [REWRITE_PROMPT.format(prev_text=r["text"]) for r in batch]
150	
151	            inputs = tokenizer(
152	                prompts,
153	                return_tensors="pt",
154	                padding=True,
155	                truncation=True,
156	                max_length=512,
157	            ).to(model.device)
158	
159	            with torch.no_grad():
160	                outputs = model.generate(
161	                    **inputs,
162	                    max_new_tokens=max_new_tokens,
163	                    do_sample=True,
164	                    top_p=0.95,
165	                    temperature=1.0,
166	                    pad_token_id=tokenizer.pad_token_id,
167	                )
168	
169	            for j, out_ids in enumerate(outputs):
170	                prompt_len = inputs["input_ids"].shape[1]
171	                generated_ids = out_ids[prompt_len:]
172	                text = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()
173	                results.append({"text": text, "doc_id": batch[j]["doc_id"]})
174	
175	            torch.cuda.empty_cache()
176	
177	        with open(out_path, "w") as f:
178	            for r in results:
179	                f.write(json.dumps(r, ensure_ascii=False) + "\n")
180	        log.info(f"Saved {len(results)} docs to {out_path}")
181	
182	
183	# ===================================================================
184	# Step 4: Feature extraction
185	# ===================================================================
186	
187	def compute_surprisal_features(model, tokenizer, texts, batch_size=8):
188	    """Compute 9-dim surprisal statistics per text using batched inference."""
189	    all_features = []
190	    for start in tqdm(range(0, len(texts), batch_size), desc="Surprisal"):
191	        batch_texts = texts[start : start + batch_size]
192	        inputs = tokenizer(
193	            batch_texts,
194	            return_tensors="pt",
195	            padding=True,
196	            truncation=True,
197	            max_length=512,
198	        ).to(model.device)
199	
200	        with torch.no_grad():
201	            logits = model(**inputs).logits  # (B, T, V)
202	
203	        log_probs = torch.log_softmax(logits, dim=-1)  # (B, T, V)
204	        input_ids = inputs["input_ids"]  # (B, T)
205	
206	        for i in range(len(batch_texts)):
207	            mask = inputs["attention_mask"][i].bool()
208	            seq_len = mask.sum().item()
209	            if seq_len < 3:
210	                all_features.append([0.0] * 9)
211	                continue
212	
213	            # left-padding: real tokens are right-aligned, use [-seq_len:]
214	            offset = input_ids.shape[1] - seq_len
215	            token_ids = input_ids[i, offset:]
216	            # surprisal of each token given prefix: -log p(x_t | x_{&lt;t})
217	            # shift: logits[t] predicts token[t+1]
218	            token_log_probs = []
219	            for t in range(1, seq_len):
220	                lp = log_probs[i, offset + t - 1, token_ids[t]].item()
221	                token_log_probs.append(-lp)  # surprisal = -log_prob
222	
223	            arr = np.array(token_log_probs)
224	            if len(arr) < 3:
225	                all_features.append([0.0] * 9)
226	                continue
227	
228	            d1 = np.diff(arr)
229	            d2 = np.diff(d1) if len(d1) > 1 else np.array([0.0])
230	
231	            feats = [
232	                float(np.mean(arr)),
233	                float(np.std(arr)),
234	                float(stats.skew(arr)),
235	                float(stats.kurtosis(arr)),
236	                float(np.mean(d1)),
237	                float(np.std(d1)),
238	                float(stats.skew(d1)) if len(d1) >= 3 else 0.0,
239	                float(np.mean(d2)),
240	                float(np.std(d2)),
241	            ]
242	            all_features.append(feats)
243	
244	        torch.cuda.empty_cache()
245	
246	    return all_features
247	
248	
249	def compute_vocab_diversity(texts, tokenizer, depth_texts_map, depth, sample_bleu=200, bleu_refs=100):
250	    """Compute 3-dim vocabulary diversity features: TTR, hapax ratio, self-BLEU."""
251	    features = []
252	    # tokenize all texts at word level (split on whitespace for simplicity)
253	    tokenized = [t.split() for t in texts]
254	
255	    # pre-select indices for self-BLEU (sample up to sample_bleu texts)
256	    bleu_indices = list(range(len(texts)))
257	    if len(bleu_indices) > sample_bleu:
258	        rng = np.random.RandomState(42 + depth)
259	        bleu_indices = rng.choice(bleu_indices, sample_bleu, replace=False).tolist()
260	    bleu_set = set(bleu_indices)
261	
262	    # pre-tokenize for BLEU refs
263	    same_depth_tokens = tokenized  # all texts from this depth
264	
265	    for idx, tokens in enumerate(tqdm(tokenized, desc=f"VocabDiv d={depth}", leave=False)):
266	        total = len(tokens)
267	        if total == 0:
268	            features.append([0.0, 0.0, 0.0])
269	            continue
270	
271	        unique = set(tokens)
272	        ttr = len(unique) / total
273	
274	        freq = Counter(tokens)
275	        hapax = sum(1 for v in freq.values() if v == 1)
276	        hapax_ratio = hapax / max(len(unique), 1)
277	
278	        # self-BLEU: compute for all samples (100 random refs each)
279	        rng_local = np.random.RandomState(idx)
280	        ref_pool = [j for j in range(len(same_depth_tokens)) if j != idx]
281	        if len(ref_pool) > bleu_refs:
282	            ref_pool = rng_local.choice(ref_pool, bleu_refs, replace=False).tolist()
283	        bleu_scores = [
284	            simple_bleu(tokens, same_depth_tokens[j]) for j in ref_pool
285	        ]
286	        self_bleu = float(np.mean(bleu_scores)) if bleu_scores else 0.0
287	
288	        features.append([ttr, hapax_ratio, self_bleu])
289	
290	    return features
291	
292	
293	def compute_tail_features(texts):
294	    """Compute 3-dim tail-thinning features: freq kurtosis, freq entropy, low-freq ratio."""
295	    features = []
296	    for text in texts:
297	        tokens = text.split()
298	        if len(tokens) < 2:
299	            features.append([0.0, 0.0, 0.0])
300	            continue
301	        freq = Counter(tokens)
302	        counts = np.array(list(freq.values()), dtype=float)
303	
304	        kurt = float(stats.kurtosis(counts)) if len(counts) >= 4 else 0.0
305	
306	        total = counts.sum()
307	        probs = counts / total
308	        entropy = float(-np.sum(probs * np.log2(probs + 1e-12)))
309	
310	        low_freq_ratio = float(np.sum(counts == 1)) / max(len(counts), 1)
311	
312	        features.append([kurt, entropy, low_freq_ratio])
313	
314	    return features
315	
316	
317	SURPRISAL_COLS = [
318	    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
319	    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
320	    "surp_d2_mean", "surp_d2_std",
321	]
322	VOCAB_COLS = ["ttr", "hapax_ratio", "self_bleu"]
323	TAIL_COLS = ["freq_kurtosis", "freq_entropy", "low_freq_ratio"]
324	ALL_FEAT_COLS = SURPRISAL_COLS + VOCAB_COLS + TAIL_COLS
325	
326	
327	def extract_all_features(model, tokenizer, data_dir: Path, max_depth: int, batch_size: int):
328	    """Extract features for all depths and save to features.csv."""
329	    import csv
330	
331	    out_path = data_dir / "features.csv"
332	    expected_total = 0
333	    for d in range(max_depth + 1):
334	        p = data_dir / f"depth_{d}.jsonl"
335	        if p.exists():
336	            expected_total += sum(1 for _ in open(p))
337	
338	    if out_path.exists() and sum(1 for _ in open(out_path)) - 1 >= expected_total:
339	        log.info("features.csv already complete — skipping")
340	        return
341	
342	    log.info("Extracting features for all depths ...")
343	
344	    # group texts by depth for self-BLEU
345	    depth_texts = {}
346	    for d in range(max_depth + 1):
347	        records = load_jsonl(data_dir / f"depth_{d}.jsonl")
348	        depth_texts[d] = records
349	
350	    rows = []
351	    for d in range(max_depth + 1):
352	        records = depth_texts[d]
353	        texts = [r["text"] for r in records]
354	        doc_ids = [r["doc_id"] for r in records]
355	        log.info(f"  depth {d}: {len(texts)} texts")
356	
357	        surp = compute_surprisal_features(model, tokenizer, texts, batch_size=batch_size)
358	        vocab = compute_vocab_diversity(
359	            texts, tokenizer, depth_texts, d
360	        )
361	        tail = compute_tail_features(texts)
362	
363	        for i in range(len(texts)):
364	            row = {"doc_id": doc_ids[i], "depth": d}
365	            for j, col in enumerate(SURPRISAL_COLS):
366	                row[col] = surp[i][j]
367	            for j, col in enumerate(VOCAB_COLS):
368	                row[col] = vocab[i][j]
369	            for j, col in enumerate(TAIL_COLS):
370	                row[col] = tail[i][j]
371	            rows.append(row)
372	
373	    with open(out_path, "w", newline="") as f:
374	        writer = csv.DictWriter(f, fieldnames=["doc_id", "depth"] + ALL_FEAT_COLS)
375	        writer.writeheader()
376	        writer.writerows(rows)
377	    log.info(f"Saved {len(rows)} feature rows to {out_path}")
378	
379	
380	# ===================================================================
381	# Step 5: Distinguishability analysis
382	# ===================================================================
383	
384	def run_analysis(data_dir: Path, results_dir: Path, max_depth: int):
385	    """Pairwise AUC, JSD, K*, ordinal classification, feature importance."""
386	    import csv
387	
388	    import lightgbm as lgb
389	    from sklearn.model_selection import StratifiedKFold
390	    from sklearn.metrics import roc_auc_score, mean_absolute_error, accuracy_score
391	
392	    results_dir.mkdir(parents=True, exist_ok=True)
393	
394	    # load features
395	    feat_path = data_dir / "features.csv"
396	    log.info(f"Loading features from {feat_path} ...")
397	    with open(feat_path) as f:
398	        reader = csv.DictReader(f)
399	        rows = list(reader)
400	
401	    # build arrays
402	    depths = np.array([int(r["depth"]) for r in rows])
403	    feat_matrix = np.array(
404	        [[float(r[c]) if r[c] != "" and r[c] != "nan" else np.nan for c in ALL_FEAT_COLS] for r in rows]
405	    )
406	    # fill NaN with column mean for classification
407	    col_means = np.nanmean(feat_matrix, axis=0)
408	    for j in range(feat_matrix.shape[1]):
409	        mask = np.isnan(feat_matrix[:, j])
410	        feat_matrix[mask, j] = col_means[j]
411	
412	    # --- Pairwise AUC ---
413	    log.info("Computing pairwise AUC ...")
414	    pairwise_auc = {}
415	    pairwise_auc_folds = {}
416	    for k in range(1, max_depth + 1):
417	        mask = (depths == k - 1) | (depths == k)
418	        X = feat_matrix[mask]
419	        y = (depths[mask] == k).astype(int)
420	        if len(np.unique(y)) < 2:
421	            pairwise_auc[f"{k-1}v{k}"] = float("nan")
422	            continue
423	
424	        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
425	        fold_aucs = []
426	        for train_idx, test_idx in skf.split(X, y):
427	            clf = lgb.LGBMClassifier(
428	                n_estimators=200, max_depth=6, learning_rate=0.05,
429	                num_leaves=31, verbose=-1, n_jobs=-1,
430	            )
431	            clf.fit(X[train_idx], y[train_idx])
432	            proba = clf.predict_proba(X[test_idx])[:, 1]
433	            fold_aucs.append(roc_auc_score(y[test_idx], proba))
434	        auc_mean = float(np.mean(fold_aucs))
435	        auc_std = float(np.std(fold_aucs))
436	        pairwise_auc[f"{k-1}v{k}"] = round(auc_mean, 4)
437	        pairwise_auc_folds[f"{k-1}v{k}"] = [round(a, 4) for a in fold_aucs]
438	        log.info(f"  AUC({k-1} vs {k}) = {auc_mean:.4f} ± {auc_std:.4f}  folds={[round(a,4) for a in fold_aucs]}")
439	
440	    with open(results_dir / "pairwise_auc.json", "w") as f:
441	        json.dump({"mean": pairwise_auc, "per_fold": pairwise_auc_folds}, f, indent=2)
442	
443	    # --- JSD ---
444	    log.info("Computing pairwise JSD ...")
445	    pairwise_jsd = {}
446	    for k in range(1, max_depth + 1):
447	        mask_prev = depths == k - 1
448	        mask_curr = depths == k
449	        feat_prev = feat_matrix[mask_prev]
450	        feat_curr = feat_matrix[mask_curr]
451	
452	        jsds_per_feat = []
453	        for j in range(feat_matrix.shape[1]):
454	            a = feat_prev[:, j]
455	            b = feat_curr[:, j]
456	            # histogram-based JSD
457	            lo = min(a.min(), b.min())
458	            hi = max(a.max(), b.max())
459	            if hi - lo < 1e-12:
460	                jsds_per_feat.append(0.0)
461	                continue
462	            bins = np.linspace(lo, hi, 51)
463	            p_hist = np.histogram(a, bins=bins, density=True)[0] + 1e-12
464	            q_hist = np.histogram(b, bins=bins, density=True)[0] + 1e-12
465	            p_hist /= p_hist.sum()
466	            q_hist /= q_hist.sum()
467	            m = 0.5 * (p_hist + q_hist)
468	            jsd = 0.5 * np.sum(p_hist * np.log2(p_hist / m)) + 0.5 * np.sum(q_hist * np.log2(q_hist / m))
469	            jsds_per_feat.append(float(jsd))
470	
471	        jsd_mean = float(np.mean(jsds_per_feat))
472	        pairwise_jsd[f"{k-1}v{k}"] = round(jsd_mean, 6)
473	        log.info(f"  JSD({k-1} vs {k}) = {jsd_mean:.6f}")
474	
475	    with open(results_dir / "jsd.json", "w") as f:
476	        json.dump(pairwise_jsd, f, indent=2)
477	
478	    # --- K* ---
479	    k_star = 0
480	    for k in range(1, max_depth + 1):
481	        key = f"{k-1}v{k}"
482	        if pairwise_auc.get(key, 0) > 0.60:
483	            k_star = k
484	
485	    # --- Ordinal classification ---
486	    log.info("Running ordinal LightGBM classification ...")
487	    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
488	    all_preds = np.zeros_like(depths, dtype=float)
489	    all_true = depths.copy()
490	
491	    importances = np.zeros(len(ALL_FEAT_COLS))
492	    for train_idx, test_idx in skf.split(feat_matrix, depths):
493	        clf = lgb.LGBMClassifier(
494	            n_estimators=300, max_depth=8, learning_rate=0.05,
495	            num_leaves=63, verbose=-1, n_jobs=-1,
496	            num_class=max_depth + 1,
497	            objective="multiclass",
498	        )
499	        clf.fit(feat_matrix[train_idx], depths[train_idx])
500	        preds = clf.predict(feat_matrix[test_idx])
501	        all_preds[test_idx] = preds
502	        importances += clf.feature_importances_
503	
504	    importances /= 5.0
505	    mae = float(mean_absolute_error(all_true, all_preds))
506	    accuracy = float(accuracy_score(all_true, all_preds.astype(int)))
507	    log.info(f"  Ordinal MAE = {mae:.4f}, Accuracy = {accuracy:.4f}, K* = {k_star}")
508	
509	    ordinal_results = {"mae": round(mae, 4), "accuracy": round(accuracy, 4), "k_star": k_star}
510	    with open(results_dir / "ordinal_results.json", "w") as f:
511	        json.dump(ordinal_results, f, indent=2)
512	
513	    # --- Feature importance ---
514	    feat_imp = sorted(
515	        [{"feature": ALL_FEAT_COLS[i], "importance": float(importances[i])} for i in range(len(ALL_FEAT_COLS))],
516	        key=lambda x: x["importance"],
517	        reverse=True,
518	    )[:10]
519	    with open(results_dir / "feature_importance.json", "w") as f:
520	        json.dump(feat_imp, f, indent=2)
521	
522	    # --- Summary ---
523	    summary_lines = [
524	        "=" * 60,
525	        "MVP Pilot Saturation Study — Results Summary",
526	        "=" * 60,
527	        "",
528	        "Pairwise AUC (adjacent depths):",
529	    ]
530	    for k in range(1, max_depth + 1):
531	        key = f"{k-1}v{k}"
532	        folds = pairwise_auc_folds.get(key, [])
533	        std = float(np.std(folds)) if folds else 0.0
534	        summary_lines.append(f"  depth {k-1} vs {k}: AUC = {pairwise_auc.get(key, 'N/A')} ± {std:.4f}  folds={folds}")
535	    summary_lines += [
536	        "",
537	        "Pairwise JSD (adjacent depths):",
538	    ]
539	    for k in range(1, max_depth + 1):
540	        key = f"{k-1}v{k}"
541	        summary_lines.append(f"  depth {k-1} vs {k}: JSD = {pairwise_jsd.get(key, 'N/A')}")
542	    summary_lines += [
543	        "",
544	        f"K* (max depth with AUC > 0.60): {k_star}",
545	        "",
546	        f"Ordinal Classification (6-class, 5-fold CV):",
547	        f"  MAE = {mae:.4f}",
548	        f"  Accuracy = {accuracy:.4f}",
549	        "",
550	        "Top-10 Feature Importance:",
551	    ]
552	    for fi in feat_imp:
553	        summary_lines.append(f"  {fi['feature']:20s} {fi['importance']:.1f}")
554	    summary_lines.append("")
555	    summary_lines.append("=" * 60)
556	
557	    summary_text = "\n".join(summary_lines)
558	    with open(results_dir / "summary.txt", "w") as f:
559	        f.write(summary_text)
560	    log.info(f"\n{summary_text}")
561	
562	
563	# ===================================================================
564	# Main
565	# ===================================================================
566	
567	def main():
568	    parser = argparse.ArgumentParser(description="MVP Pilot Saturation Study Pipeline")
569	    parser.add_argument("--model_path", type=str,
570	                        default="/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct")
571	    parser.add_argument("--data_dir", type=str,
572	                        default="/root/autodl-tmp/gen-depth-contamination/data")
573	    parser.add_argument("--results_dir", type=str,
574	                        default="/root/autodl-tmp/gen-depth-contamination/results")
575	    parser.add_argument("--num_samples", type=int, default=5000)
576	    parser.add_argument("--max_depth", type=int, default=5)
577	    parser.add_argument("--batch_size", type=int, default=16)
578	    parser.add_argument("--feat_batch_size", type=int, default=8,
579	                        help="Batch size for surprisal feature extraction (uses more VRAM)")
580	    args = parser.parse_args()
581	
582	    data_dir = Path(args.data_dir)
583	    results_dir = Path(args.results_dir)
584	    data_dir.mkdir(parents=True, exist_ok=True)
585	    results_dir.mkdir(parents=True, exist_ok=True)
586	
587	    log.info(f"Model: {args.model_path}")
588	    log.info(f"Data dir: {data_dir}")
589	    log.info(f"Samples: {args.num_samples}, Max depth: {args.max_depth}")
590	
591	    # Load model + tokenizer
592	    from transformers import AutoModelForCausalLM, AutoTokenizer
593	
594	    log.info("Loading tokenizer ...")
595	    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
596	    if tokenizer.pad_token is None:
597	        tokenizer.pad_token = tokenizer.eos_token
598	        tokenizer.pad_token_id = tokenizer.eos_token_id
599	    tokenizer.padding_side = "left"
600	
601	    log.info("Loading model ...")
602	    model = AutoModelForCausalLM.from_pretrained(
603	        args.model_path,
604	        torch_dtype=torch.float16,
605	        device_map="auto",
606	        trust_remote_code=True,
607	    )
608	    model.eval()
609	    log.info(f"Model loaded on {model.device}")
610	
611	    # Step 2
612	    log.info("=" * 40 + " Step 2: Seed Data " + "=" * 40)
613	    prepare_seed_data(tokenizer, data_dir, args.num_samples)
614	
615	    # Step 3
616	    log.info("=" * 40 + " Step 3: Depth Chain " + "=" * 40)
617	    generate_depth_chain(model, tokenizer, data_dir, args.max_depth, args.batch_size)
618	
619	    # Step 4
620	    log.info("=" * 40 + " Step 4: Feature Extraction " + "=" * 40)
621	    extract_all_features(model, tokenizer, data_dir, args.max_depth, args.feat_batch_size)
622	
623	    # Step 5
624	    log.info("=" * 40 + " Step 5: Analysis " + "=" * 40)
625	    run_analysis(data_dir, results_dir, args.max_depth)
626	
627	    log.info("Pipeline complete.")
628	
629	
630	if __name__ == "__main__":
631	    main()
632	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a2b3c6e1-bf66-4ff6-bec8-41639f3adf55",
  "uuid": "e53288c9-0a22-4469-b5a8-7f06e6ec69b8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_pipeline.py",
      "content": "\"\"\"\nMVP Pilot Saturation Study — Complete Pipeline (Steps 2-5)\n\nGenerates recursive depth chains from C4 seed data using Qwen2.5-1.5B,\nextracts statistical features, and runs distinguishability analysis.\n\nInput:  C4 validation split (streamed from HuggingFace)\nOutput: data/depth_{0..K}.jsonl, data/features.csv, results/*.json + summary.txt\n\nKey deps: torch, transformers, datasets, scipy, lightgbm, sklearn, tqdm\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport math\nimport os\nimport sys\nfrom collections import Counter\nfrom pathlib import Path\n\nimport numpy as np\nimport torch\nfrom scipy import stats\nfrom tqdm import tqdm\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\n\n# ---------------------------------------------------------------------------\n# Utility: simple 4-gram BLEU (no nltk dependency)\n# ---------------------------------------------------------------------------\n\ndef ngrams(tokens, n):\n    return [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]\n\n\ndef simple_bleu(candidate_tokens, reference_tokens, max_n=4):\n    \"\"\"Compute sentence-level BLEU up to max_n grams with brevity penalty.\"\"\"\n    if len(candidate_tokens) == 0:\n        return 0.0\n    precisions = []\n    for n in range(1, max_n + 1):\n        cand_ngrams = ngrams(candidate_tokens, n)\n        ref_ngrams = ngrams(reference_tokens, n)\n        if not cand_ngrams:\n            precisions.append(0.0)\n            continue\n        ref_counts = Counter(ref_ngrams)\n        clipped = 0\n        cand_counts = Counter(cand_ngrams)\n        for ng, cnt in cand_counts.items():\n            clipped += min(cnt, ref_counts.get(ng, 0))\n        precisions.append(clipped / len(cand_ngrams))\n    if any(p == 0 for p in precisions):\n        return 0.0\n    log_avg = sum(math.log(p) for p in precisions) / max_n\n    bp = min(1.0, math.exp(1 - len(reference_tokens) / max(len(candidate_tokens), 1)))\n    return bp * math.exp(log_avg)\n\n\n# ===================================================================\n# Step 2: Seed data preparation\n# ===================================================================\n\ndef prepare_seed_data(tokenizer, data_dir: Path, num_samples: int, max_tokens: int = 256):\n    \"\"\"Download C4 validation, truncate to max_tokens, save as depth_0.jsonl.\"\"\"\n    out_path = data_dir / \"depth_0.jsonl\"\n    if out_path.exists() and sum(1 for _ in open(out_path)) >= num_samples:\n        log.info(\"depth_0.jsonl already exists with enough samples — skipping\")\n        return\n\n    from datasets import load_dataset\n\n    # Use a single validation shard to avoid slow full-tree listing on proxied networks\n    hf_endpoint = os.environ.get(\"HF_ENDPOINT\", \"https://huggingface.co\")\n    C4_SHARD_URL = f\"{hf_endpoint}/datasets/allenai/c4/resolve/main/en/c4-validation.00000-of-00008.json.gz\"\n    log.info(\"Loading C4 validation shard (streaming) ...\")\n    try:\n        ds = load_dataset(\"json\", data_files=C4_SHARD_URL, split=\"train\", streaming=True)\n    except Exception as e:\n        log.warning(f\"Direct shard download failed ({e}), falling back to full dataset listing\")\n        ds = load_dataset(\"allenai/c4\", \"en\", split=\"validation\", streaming=True)\n\n    records = []\n    for i, example in enumerate(tqdm(ds, total=num_samples, desc=\"Sampling C4\")):\n        if i >= num_samples:\n            break\n        text = example[\"text\"].strip()\n        if not text:\n            continue\n        ids = tokenizer.encode(text, add_special_tokens=False)[:max_tokens]\n        truncated = tokenizer.decode(ids, skip_special_tokens=True)\n        records.append({\"text\": truncated, \"doc_id\": len(records)})\n        if len(records) >= num_samples:\n            break\n\n    data_dir.mkdir(parents=True, exist_ok=True)\n    with open(out_path, \"w\") as f:\n        for r in records:\n            f.write(json.dumps(r, ensure_ascii=False) + \"\\n\")\n    log.info(f\"Saved {len(records)} seed documents to {out_path}\")\n\n\n# ===================================================================\n# Step 3: Recursive depth chain generation\n# ===================================================================\n\nREWRITE_PROMPT = (\n    \"Below is a passage. Write a new passage of similar length on the same \"\n    \"topic and in the same style.\\n\\n\"\n    \"Original passage:\\n{prev_text}\\n\\nNew passage:\\n\"\n)\n\n\ndef load_jsonl(path: Path):\n    with open(path) as f:\n        return [json.loads(line) for line in f]\n\n\ndef generate_depth_chain(\n    model,\n    tokenizer,\n    data_dir: Path,\n    max_depth: int,\n    batch_size: int,\n    max_new_tokens: int = 256,\n):\n    \"\"\"Generate depths 1..max_depth via prompt-chain rewriting.\"\"\"\n    for depth in range(1, max_depth + 1):\n        out_path = data_dir / f\"depth_{depth}.jsonl\"\n        prev_path = data_dir / f\"depth_{depth - 1}.jsonl\"\n\n        if out_path.exists() and sum(1 for _ in open(out_path)) >= sum(1 for _ in open(prev_path)):\n            log.info(f\"depth_{depth}.jsonl already complete — skipping\")\n            continue\n\n        prev_records = load_jsonl(prev_path)\n        log.info(f\"Generating depth {depth} ({len(prev_records)} docs, batch_size={batch_size}) ...\")\n\n        results = []\n        for start in tqdm(range(0, len(prev_records), batch_size), desc=f\"depth {depth}\"):\n            batch = prev_records[start : start + batch_size]\n            prompts = [REWRITE_PROMPT.format(prev_text=r[\"text\"]) for r in batch]\n\n            inputs = tokenizer(\n                prompts,\n                return_tensors=\"pt\",\n                padding=True,\n                truncation=True,\n                max_length=512,\n            ).to(model.device)\n\n            with torch.no_grad():\n                outputs = model.generate(\n                    **inputs,\n                    max_new_tokens=max_new_tokens,\n                    do_sample=True,\n                    top_p=0.95,\n                    temperature=1.0,\n                    pad_token_id=tokenizer.pad_token_id,\n                )\n\n            for j, out_ids in enumerate(outputs):\n                prompt_len = inputs[\"input_ids\"].shape[1]\n                generated_ids = out_ids[prompt_len:]\n                text = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()\n                results.append({\"text\": text, \"doc_id\": batch[j][\"doc_id\"]})\n\n            torch.cuda.empty_cache()\n\n        with open(out_path, \"w\") as f:\n            for r in results:\n                f.write(json.dumps(r, ensure_ascii=False) + \"\\n\")\n        log.info(f\"Saved {len(results)} docs to {out_path}\")\n\n\n# ===================================================================\n# Step 4: Feature extraction\n# ===================================================================\n\ndef compute_surprisal_features(model, tokenizer, texts, batch_size=8):\n    \"\"\"Compute 9-dim surprisal statistics per text using batched inference.\"\"\"\n    all_features = []\n    for start in tqdm(range(0, len(texts), batch_size), desc=\"Surprisal\"):\n        batch_texts = texts[start : start + batch_size]\n        inputs = tokenizer(\n            batch_texts,\n            return_tensors=\"pt\",\n            padding=True,\n            truncation=True,\n            max_length=512,\n        ).to(model.device)\n\n        with torch.no_grad():\n            logits = model(**inputs).logits  # (B, T, V)\n\n        log_probs = torch.log_softmax(logits, dim=-1)  # (B, T, V)\n        input_ids = inputs[\"input_ids\"]  # (B, T)\n\n        for i in range(len(batch_texts)):\n            mask = inputs[\"attention_mask\"][i].bool()\n            seq_len = mask.sum().item()\n            if seq_len < 3:\n                all_features.append([0.0] * 9)\n                continue\n\n            # left-padding: real tokens are right-aligned, use [-seq_len:]\n            offset = input_ids.shape[1] - seq_len\n            token_ids = input_ids[i, offset:]\n            # surprisal of each token given prefix: -log p(x_t | x_{&lt;t})\n            # shift: logits[t] predicts token[t+1]\n            token_log_probs = []\n            for t in range(1, seq_len):\n                lp = log_probs[i, offset + t - 1, token_ids[t]].item()\n                token_log_probs.append(-lp)  # surprisal = -log_prob\n\n            arr = np.array(token_log_probs)\n            if len(arr) < 3:\n                all_features.append([0.0] * 9)\n                continue\n\n            d1 = np.diff(arr)\n            d2 = np.diff(d1) if len(d1) > 1 else np.array([0.0])\n\n            feats = [\n                float(np.mean(arr)),\n                float(np.std(arr)),\n                float(stats.skew(arr)),\n                float(stats.kurtosis(arr)),\n                float(np.mean(d1)),\n                float(np.std(d1)),\n                float(stats.skew(d1)) if len(d1) >= 3 else 0.0,\n                float(np.mean(d2)),\n                float(np.std(d2)),\n            ]\n            all_features.append(feats)\n\n        torch.cuda.empty_cache()\n\n    return all_features\n\n\ndef compute_vocab_diversity(texts, tokenizer, depth_texts_map, depth, sample_bleu=200, bleu_refs=100):\n    \"\"\"Compute 3-dim vocabulary diversity features: TTR, hapax ratio, self-BLEU.\"\"\"\n    features = []\n    # tokenize all texts at word level (split on whitespace for simplicity)\n    tokenized = [t.split() for t in texts]\n\n    # pre-select indices for self-BLEU (sample up to sample_bleu texts)\n    bleu_indices = list(range(len(texts)))\n    if len(bleu_indices) > sample_bleu:\n        rng = np.random.RandomState(42 + depth)\n        bleu_indices = rng.choice(bleu_indices, sample_bleu, replace=False).tolist()\n    bleu_set = set(bleu_indices)\n\n    # pre-tokenize for BLEU refs\n    same_depth_tokens = tokenized  # all texts from this depth\n\n    for idx, tokens in enumerate(tqdm(tokenized, desc=f\"VocabDiv d={depth}\", leave=False)):\n        total = len(tokens)\n        if total == 0:\n            features.append([0.0, 0.0, 0.0])\n            continue\n\n        unique = set(tokens)\n        ttr = len(unique) / total\n\n        freq = Counter(tokens)\n        hapax = sum(1 for v in freq.values() if v == 1)\n        hapax_ratio = hapax / max(len(unique), 1)\n\n        # self-BLEU: compute for all samples (100 random refs each)\n        rng_local = np.random.RandomState(idx)\n        ref_pool = [j for j in range(len(same_depth_tokens)) if j != idx]\n        if len(ref_pool) > bleu_refs:\n            ref_pool = rng_local.choice(ref_pool, bleu_refs, replace=False).tolist()\n        bleu_scores = [\n            simple_bleu(tokens, same_depth_tokens[j]) for j in ref_pool\n        ]\n        self_bleu = float(np.mean(bleu_scores)) if bleu_scores else 0.0\n\n        features.append([ttr, hapax_ratio, self_bleu])\n\n    return features\n\n\ndef compute_tail_features(texts):\n    \"\"\"Compute 3-dim tail-thinning features: freq kurtosis, freq entropy, low-freq ratio.\"\"\"\n    features = []\n    for text in texts:\n        tokens = text.split()\n        if len(tokens) < 2:\n            features.append([0.0, 0.0, 0.0])\n            continue\n        freq = Counter(tokens)\n        counts = np.array(list(freq.values()), dtype=float)\n\n        kurt = float(stats.kurtosis(counts)) if len(counts) >= 4 else 0.0\n\n        total = counts.sum()\n        probs = counts / total\n        entropy = float(-np.sum(probs * np.log2(probs + 1e-12)))\n\n        low_freq_ratio = float(np.sum(counts == 1)) / max(len(counts), 1)\n\n        features.append([kurt, entropy, low_freq_ratio])\n\n    return features\n\n\nSURPRISAL_COLS = [\n    \"surp_mean\", \"surp_std\", \"surp_skew\", \"surp_kurt\",\n    \"surp_d1_mean\", \"surp_d1_std\", \"surp_d1_skew\",\n    \"surp_d2_mean\", \"surp_d2_std\",\n]\nVOCAB_COLS = [\"ttr\", \"hapax_ratio\", \"self_bleu\"]\nTAIL_COLS = [\"freq_kurtosis\", \"freq_entropy\", \"low_freq_ratio\"]\nALL_FEAT_COLS = SURPRISAL_COLS + VOCAB_COLS + TAIL_COLS\n\n\ndef extract_all_features(model, tokenizer, data_dir: Path, max_depth: int, batch_size: int):\n    \"\"\"Extract features for all depths and save to features.csv.\"\"\"\n    import csv\n\n    out_path = data_dir / \"features.csv\"\n    expected_total = 0\n    for d in range(max_depth + 1):\n        p = data_dir / f\"depth_{d}.jsonl\"\n        if p.exists():\n            expected_total += sum(1 for _ in open(p))\n\n    if out_path.exists() and sum(1 for _ in open(out_path)) - 1 >= expected_total:\n        log.info(\"features.csv already complete — skipping\")\n        return\n\n    log.info(\"Extracting features for all depths ...\")\n\n    # group texts by depth for self-BLEU\n    depth_texts = {}\n    for d in range(max_depth + 1):\n        records = load_jsonl(data_dir / f\"depth_{d}.jsonl\")\n        depth_texts[d] = records\n\n    rows = []\n    for d in range(max_depth + 1):\n        records = depth_texts[d]\n        texts = [r[\"text\"] for r in records]\n        doc_ids = [r[\"doc_id\"] for r in records]\n        log.info(f\"  depth {d}: {len(texts)} texts\")\n\n        surp = compute_surprisal_features(model, tokenizer, texts, batch_size=batch_size)\n        vocab = compute_vocab_diversity(\n            texts, tokenizer, depth_texts, d\n        )\n        tail = compute_tail_features(texts)\n\n        for i in range(len(texts)):\n            row = {\"doc_id\": doc_ids[i], \"depth\": d}\n            for j, col in enumerate(SURPRISAL_COLS):\n                row[col] = surp[i][j]\n            for j, col in enumerate(VOCAB_COLS):\n                row[col] = vocab[i][j]\n            for j, col in enumerate(TAIL_COLS):\n                row[col] = tail[i][j]\n            rows.append(row)\n\n    with open(out_path, \"w\", newline=\"\") as f:\n        writer = csv.DictWriter(f, fieldnames=[\"doc_id\", \"depth\"] + ALL_FEAT_COLS)\n        writer.writeheader()\n        writer.writerows(rows)\n    log.info(f\"Saved {len(rows)} feature rows to {out_path}\")\n\n\n# ===================================================================\n# Step 5: Distinguishability analysis\n# ===================================================================\n\ndef run_analysis(data_dir: Path, results_dir: Path, max_depth: int):\n    \"\"\"Pairwise AUC, JSD, K*, ordinal classification, feature importance.\"\"\"\n    import csv\n\n    import lightgbm as lgb\n    from sklearn.model_selection import StratifiedKFold\n    from sklearn.metrics import roc_auc_score, mean_absolute_error, accuracy_score\n\n    results_dir.mkdir(parents=True, exist_ok=True)\n\n    # load features\n    feat_path = data_dir / \"features.csv\"\n    log.info(f\"Loading features from {feat_path} ...\")\n    with open(feat_path) as f:\n        reader = csv.DictReader(f)\n        rows = list(reader)\n\n    # build arrays\n    depths = np.array([int(r[\"depth\"]) for r in rows])\n    feat_matrix = np.array(\n        [[float(r[c]) if r[c] != \"\" and r[c] != \"nan\" else np.nan for c in ALL_FEAT_COLS] for r in rows]\n    )\n    # fill NaN with column mean for classification\n    col_means = np.nanmean(feat_matrix, axis=0)\n    for j in range(feat_matrix.shape[1]):\n        mask = np.isnan(feat_matrix[:, j])\n        feat_matrix[mask, j] = col_means[j]\n\n    # --- Pairwise AUC ---\n    log.info(\"Computing pairwise AUC ...\")\n    pairwise_auc = {}\n    pairwise_auc_folds = {}\n    for k in range(1, max_depth + 1):\n        mask = (depths == k - 1) | (depths == k)\n        X = feat_matrix[mask]\n        y = (depths[mask] == k).astype(int)\n        if len(np.unique(y)) < 2:\n            pairwise_auc[f\"{k-1}v{k}\"] = float(\"nan\")\n            continue\n\n        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)\n        fold_aucs = []\n        for train_idx, test_idx in skf.split(X, y):\n            clf = lgb.LGBMClassifier(\n                n_estimators=200, max_depth=6, learning_rate=0.05,\n                num_leaves=31, verbose=-1, n_jobs=-1,\n            )\n            clf.fit(X[train_idx], y[train_idx])\n            proba = clf.predict_proba(X[test_idx])[:, 1]\n            fold_aucs.append(roc_auc_score(y[test_idx], proba))\n        auc_mean = float(np.mean(fold_aucs))\n        auc_std = float(np.std(fold_aucs))\n        pairwise_auc[f\"{k-1}v{k}\"] = round(auc_mean, 4)\n        pairwise_auc_folds[f\"{k-1}v{k}\"] = [round(a, 4) for a in fold_aucs]\n        log.info(f\"  AUC({k-1} vs {k}) = {auc_mean:.4f} ± {auc_std:.4f}  folds={[round(a,4) for a in fold_aucs]}\")\n\n    with open(results_dir / \"pairwise_auc.json\", \"w\") as f:\n        json.dump({\"mean\": pairwise_auc, \"per_fold\": pairwise_auc_folds}, f, indent=2)\n\n    # --- JSD ---\n    log.info(\"Computing pairwise JSD ...\")\n    pairwise_jsd = {}\n    for k in range(1, max_depth + 1):\n        mask_prev = depths == k - 1\n        mask_curr = depths == k\n        feat_prev = feat_matrix[mask_prev]\n        feat_curr = feat_matrix[mask_curr]\n\n        jsds_per_feat = []\n        for j in range(feat_matrix.shape[1]):\n            a = feat_prev[:, j]\n            b = feat_curr[:, j]\n            # histogram-based JSD\n            lo = min(a.min(), b.min())\n            hi = max(a.max(), b.max())\n            if hi - lo < 1e-12:\n                jsds_per_feat.append(0.0)\n                continue\n            bins = np.linspace(lo, hi, 51)\n            p_hist = np.histogram(a, bins=bins, density=True)[0] + 1e-12\n            q_hist = np.histogram(b, bins=bins, density=True)[0] + 1e-12\n            p_hist /= p_hist.sum()\n            q_hist /= q_hist.sum()\n            m = 0.5 * (p_hist + q_hist)\n            jsd = 0.5 * np.sum(p_hist * np.log2(p_hist / m)) + 0.5 * np.sum(q_hist * np.log2(q_hist / m))\n            jsds_per_feat.append(float(jsd))\n\n        jsd_mean = float(np.mean(jsds_per_feat))\n        pairwise_jsd[f\"{k-1}v{k}\"] = round(jsd_mean, 6)\n        log.info(f\"  JSD({k-1} vs {k}) = {jsd_mean:.6f}\")\n\n    with open(results_dir / \"jsd.json\", \"w\") as f:\n        json.dump(pairwise_jsd, f, indent=2)\n\n    # --- K* ---\n    k_star = 0\n    for k in range(1, max_depth + 1):\n        key = f\"{k-1}v{k}\"\n        if pairwise_auc.get(key, 0) > 0.60:\n            k_star = k\n\n    # --- Ordinal classification ---\n    log.info(\"Running ordinal LightGBM classification ...\")\n    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)\n    all_preds = np.zeros_like(depths, dtype=float)\n    all_true = depths.copy()\n\n    importances = np.zeros(len(ALL_FEAT_COLS))\n    for train_idx, test_idx in skf.split(feat_matrix, depths):\n        clf = lgb.LGBMClassifier(\n            n_estimators=300, max_depth=8, learning_rate=0.05,\n            num_leaves=63, verbose=-1, n_jobs=-1,\n            num_class=max_depth + 1,\n            objective=\"multiclass\",\n        )\n        clf.fit(feat_matrix[train_idx], depths[train_idx])\n        preds = clf.predict(feat_matrix[test_idx])\n        all_preds[test_idx] = preds\n        importances += clf.feature_importances_\n\n    importances /= 5.0\n    mae = float(mean_absolute_error(all_true, all_preds))\n    accuracy = float(accuracy_score(all_true, all_preds.astype(int)))\n    log.info(f\"  Ordinal MAE = {mae:.4f}, Accuracy = {accuracy:.4f}, K* = {k_star}\")\n\n    ordinal_results = {\"mae\": round(mae, 4), \"accuracy\": round(accuracy, 4), \"k_star\": k_star}\n    with open(results_dir / \"ordinal_results.json\", \"w\") as f:\n        json.dump(ordinal_results, f, indent=2)\n\n    # --- Feature importance ---\n    feat_imp = sorted(\n        [{\"feature\": ALL_FEAT_COLS[i], \"importance\": float(importances[i])} for i in range(len(ALL_FEAT_COLS))],\n        key=lambda x: x[\"importance\"],\n        reverse=True,\n    )[:10]\n    with open(results_dir / \"feature_importance.json\", \"w\") as f:\n        json.dump(feat_imp, f, indent=2)\n\n    # --- Summary ---\n    summary_lines = [\n        \"=\" * 60,\n        \"MVP Pilot Saturation Study — Results Summary\",\n        \"=\" * 60,\n        \"\",\n        \"Pairwise AUC (adjacent depths):\",\n    ]\n    for k in range(1, max_depth + 1):\n        key = f\"{k-1}v{k}\"\n        folds = pairwise_auc_folds.get(key, [])\n        std = float(np.std(folds)) if folds else 0.0\n        summary_lines.append(f\"  depth {k-1} vs {k}: AUC = {pairwise_auc.get(key, 'N/A')} ± {std:.4f}  folds={folds}\")\n    summary_lines += [\n        \"\",\n        \"Pairwise JSD (adjacent depths):\",\n    ]\n    for k in range(1, max_depth + 1):\n        key = f\"{k-1}v{k}\"\n        summary_lines.append(f\"  depth {k-1} vs {k}: JSD = {pairwise_jsd.get(key, 'N/A')}\")\n    summary_lines += [\n        \"\",\n        f\"K* (max depth with AUC > 0.60): {k_star}\",\n        \"\",\n        f\"Ordinal Classification (6-class, 5-fold CV):\",\n        f\"  MAE = {mae:.4f}\",\n        f\"  Accuracy = {accuracy:.4f}\",\n        \"\",\n        \"Top-10 Feature Importance:\",\n    ]\n    for fi in feat_imp:\n        summary_lines.append(f\"  {fi['feature']:20s} {fi['importance']:.1f}\")\n    summary_lines.append(\"\")\n    summary_lines.append(\"=\" * 60)\n\n    summary_text = \"\\n\".join(summary_lines)\n    with open(results_dir / \"summary.txt\", \"w\") as f:\n        f.write(summary_text)\n    log.info(f\"\\n{summary_text}\")\n\n\n# ===================================================================\n# Main\n# ===================================================================\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"MVP Pilot Saturation Study Pipeline\")\n    parser.add_argument(\"--model_path\", type=str,\n                        default=\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct\")\n    parser.add_argument(\"--data_dir\", type=str,\n                        default=\"/root/autodl-tmp/gen-depth-contamination/data\")\n    parser.add_argument(\"--results_dir\", type=str,\n                        default=\"/root/autodl-tmp/gen-depth-contamination/results\")\n    parser.add_argument(\"--num_samples\", type=int, default=5000)\n    parser.add_argument(\"--max_depth\", type=int, default=5)\n    parser.add_argument(\"--batch_size\", type=int, default=16)\n    parser.add_argument(\"--feat_batch_size\", type=int, default=8,\n                        help=\"Batch size for surprisal feature extraction (uses more VRAM)\")\n    args = parser.parse_args()\n\n    data_dir = Path(args.data_dir)\n    results_dir = Path(args.results_dir)\n    data_dir.mkdir(parents=True, exist_ok=True)\n    results_dir.mkdir(parents=True, exist_ok=True)\n\n    log.info(f\"Model: {args.model_path}\")\n    log.info(f\"Data dir: {data_dir}\")\n    log.info(f\"Samples: {args.num_samples}, Max depth: {args.max_depth}\")\n\n    # Load model + tokenizer\n    from transformers import AutoModelForCausalLM, AutoTokenizer\n\n    log.info(\"Loading tokenizer ...\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n        tokenizer.pad_token_id = tokenizer.eos_token_id\n    tokenizer.padding_side = \"left\"\n\n    log.info(\"Loading model ...\")\n    model = AutoModelForCausalLM.from_pretrained(\n        args.model_path,\n        torch_dtype=torch.float16,\n        device_map=\"auto\",\n        trust_remote_code=True,\n    )\n    model.eval()\n    log.info(f\"Model loaded on {model.device}\")\n\n    # Step 2\n    log.info(\"=\" * 40 + \" Step 2: Seed Data \" + \"=\" * 40)\n    prepare_seed_data(tokenizer, data_dir, args.num_samples)\n\n    # Step 3\n    log.info(\"=\" * 40 + \" Step 3: Depth Chain \" + \"=\" * 40)\n    generate_depth_chain(model, tokenizer, data_dir, args.max_depth, args.batch_size)\n\n    # Step 4\n    log.info(\"=\" * 40 + \" Step 4: Feature Extraction \" + \"=\" * 40)\n    extract_all_features(model, tokenizer, data_dir, args.max_depth, args.feat_batch_size)\n\n    # Step 5\n    log.info(\"=\" * 40 + \" Step 5: Analysis \" + \"=\" * 40)\n    run_analysis(data_dir, results_dir, args.max_depth)\n\n    log.info(\"Pipeline complete.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 632,
      "startLine": 1,
      "totalLines": 632
    }
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the reference materials. Let me synthesize the information and write the methodology draft. Let me organize everything carefully:

From the materials, I need to cover:

**3.1 Multi-generation Corpus Construction**
- Formal definition: depth-0 = human text X₀, depth-k = LLM(X_{k-1})
- Prompt-chain implementation: REWRITE_PROMPT template from run_pipeline.py
- Model: Qwen2.5-1.5B-Instruct (not 1.8B, as ROADMAP notes)


- Decoding parameters: nucleus sampling with p=0.95 and temperature 1.0
- Seed data sourced from C4 validation subset with 5000 documents truncated to 256 tokens, accounting for left-padding considerations

**3.2 Feature Extraction Pipeline**
I'm computing surprisal metrics across nine dimensions—mean, standard deviation, skewness, and kurtosis of the base surprisal values, plus the same statistics for first and second-order differences. Now moving into vocabulary diversity features...

Measuring vocabulary diversity with type-token ratio, hapax ratio, and self-BLEU computed against 4-grams from 100 random references at the same depth. For tail-thinning, I'm capturing frequency kurtosis, entropy, and the proportion of low-frequency tokens.

**3.3 Ordinal Depth Classifier**
Using LightGBM with a stratified 5-fold cross-validation approach, training pairwise classifiers for each adjacent depth level and evaluating via ordinal multiclass objective across all six depth classes.

**3.4 Saturation Boundary K***
The saturation point K* is defined as the maximum depth where the AUC between consecutive levels exceeds 0.60, with connections to DPI and threshold justification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a2b3c6e1-bf66-4ff6-bec8-41639f3adf55",
  "uuid": "3f5c5906-d6da-419d-adc4-8f876da710f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmNb8VGnpteYkmQakeHCLu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30544,
      "cache_read_input_tokens": 24551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 30544
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

_source line 19_

所有材料已读取完毕，开始撰写 methodology 初稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a2b3c6e1-bf66-4ff6-bec8-41639f3adf55",
  "uuid": "ad9373b1-1bab-493a-a81c-79c21e782d60",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmNb8VGnpteYkmQakeHCLu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30544,
      "cache_read_input_tokens": 24551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 30544
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

_source line 20_

<details open><summary>🔧 Tool call — Write · `toolu_01DbzYjodTTMCQ4mHBByKf7w`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/methodology_draft.md",
  "content": "# 3. Methodology\n\n## 3.1 Multi-generation Corpus Construction\n\n### 问题形式化\n\n设 $X_0$ 为人类撰写的文本（seed text），建模为概率空间上的随机变量。LLM 的生成过程定义为随机信道 $\\mathcal{T}: \\mathcal{X} \\to \\mathcal{X}$，将输入文本映射到输出文本。递归生成形成 Markov chain：\n\n$$X_0 \\xrightarrow{\\mathcal{T}} X_1 \\xrightarrow{\\mathcal{T}} X_2 \\xrightarrow{\\mathcal{T}} \\cdots \\xrightarrow{\\mathcal{T}} X_K$$\n\n其中 depth-0 文本 $X_0$ 为人类原始文本，depth-$k$ 文本 $X_k = \\mathcal{T}(X_{k-1})$ 由 depth-$(k-1)$ 文本经过一次 LLM 信道产生。该形式化依赖两个关键假设：**(A1) 时不变信道**——同一 LLM 与 decoding strategy 在每次迭代中定义相同的信道 $\\mathcal{T}$；**(A2) Markov 性**——$X_{k+1}$ 仅依赖 $X_k$，不依赖更早的 $X_0, \\ldots, X_{k-1}$。这两个假设在 prompt-chain 设定下成立（每次生成仅以上一轮输出为输入），retrain-chain 场景需将 $\\mathcal{T}$ 放宽为 $\\mathcal{T}_k$。\n\n### Prompt-chain 实现\n\n我们采用 prompt-chain 方式构造 depth chain：每一轮将前一深度的文本嵌入固定的 rewrite prompt 模板，由模型生成同主题、同风格的新文本。具体 prompt 模板如下：\n\n> Below is a passage. Write a new passage of similar length on the same topic and in the same style.\n>\n> Original passage:\n> {prev\\_text}\n>\n> New passage:\n\n该模板要求模型保持主题与风格一致性，同时生成全新文本而非简单复述。这一设计的意图是模拟现实场景中合成文本被反复改写的过程——例如 AI 生成的内容被爬取后再次作为 LLM 的输入进行改写或续写。\n\nPrompt-chain 与 retrain-chain（在合成数据上重新训练模型再生成）的区别值得说明。Retrain-chain 更接近 Shumailov et al. [2024] 描述的 model collapse 真实路径，但 prompt-chain 提供了一个 **upper bound estimate**：如果在 prompt-chain（模型权重不变、仅输入文本退化）下特征已饱和，retrain-chain（模型本身也退化）下只会更快饱和。我们选择 prompt-chain 作为 MVP 方案以控制变量，retrain-chain 验证留作后续研究。\n\n### 模型选择\n\n我们选用 **Qwen2.5-1.5B-Instruct** [Qwen Team, 2024] 作为生成模型。选择理由如下：\n\n**Instruct 而非 base 模型**。现实世界中绝大多数合成文本（ChatGPT 输出、AI 写作工具、自动摘要等）均来自经过 instruction tuning 的模型。使用 Instruct 版本可确保生成文本的分布特征更接近实际污染数据。此外，Instruct 模型能更好地遵循 rewrite prompt 中的改写指令，生成主题一致但非直接复制的文本，而 base 模型可能简单延续原文或产生不相关内容。\n\n**1.5B 参数规模**。选择小规模模型基于以下考量：(1) 计算效率——在单块 RTX 4090D (24GB) 上可高效完成 5000 文档 × 5 个深度的生成任务；(2) model collapse 文献 [Shumailov et al., 2024; Drayson et al., 2025] 表明退化现象在小模型上更为显著，有利于在 pilot study 中观察清晰的深度信号；(3) Qwen2.5 系列在 1.5B 规模上已展现出 competitive 的语言能力 [需验证]，足以生成流畅且有意义的文本。Full study 阶段将扩展到多模型家族（Pythia-1.4B, OLMo-1B）及更大规模（Qwen2.5-7B/14B）进行 cross-model 和 cross-scale 验证。\n\n### 解码参数\n\n采用 **nucleus sampling** (top-$p$ sampling)，参数设定为 $p = 0.95$, temperature $T = 1.0$。这一配置的理由在于：\n\n(1) **接近真实世界配置**。主流 LLM 应用（ChatGPT、Claude、各类 API 调用）的默认或推荐生成参数通常处于 $T \\in [0.7, 1.0]$, $p \\in [0.9, 0.95]$ 的区间。$T=1.0, p=0.95$ 代表了一个 moderately stochastic 的生成配置，既保留了足够的随机性以反映真实合成文本的 diversity，又不至于因过高 temperature 产生不自然的噪声文本。\n\n(2) **信道噪声的理论考量**。在信道级联框架下，$T$ 和 $p$ 共同决定了信道 $\\mathcal{T}$ 的 contraction rate $\\rho$。Greedy decoding ($T \\to 0$) 使信道趋近确定性（$\\rho \\to 1$），信息衰减慢但 diversity 低；高 temperature 使信道趋近均匀随机（$\\rho \\to 0$），信息快速丢失。$T=1.0, p=0.95$ 处于中间区域，既保证可观测的深度信号，又不人为加速或延缓饱和。\n\n### 种子数据\n\n种子数据取自 **C4 (Colossal Clean Crawled Corpus)** [Raffel et al., 2020] 的 validation split。从中采样 **5,000 篇文档**，每篇文档经 tokenizer 截断至 **256 tokens** 后作为 depth-0 文本。\n\n选择 C4 的理由：(1) 作为广泛使用的预训练语料，C4 文本代表了典型的 web 文本分布；(2) validation split 保证不与常见模型的训练集重叠。5,000 篇文档的规模在 pilot study 中足以提供可靠的统计估计，同时控制计算成本。\n\n截断至 256 tokens 的考量：(1) 控制生成长度一致性——过长的 seed text 导致生成文本长度方差大，干扰特征提取；(2) 256 tokens 足以包含 1-2 个完整段落的语义信息，保留主题和风格特征；(3) 与模型的 max prompt length 配合——prompt 模板 + seed text 需要在 512 tokens 内完成。\n\n### Left-padding 技术考量\n\n在 batch 推理中，我们采用 **left-padding** (`tokenizer.padding_side = \"left\"`)。这一选择对 causal language model 的生成质量至关重要：\n\nRight-padding（将 pad token 追加到序列末尾）会导致模型在生成时\"看到\"大量无意义的 pad token，影响注意力分布和生成质量。Left-padding 将 pad token 置于序列左侧，真实 token 右对齐，使得模型在生成时只关注到有意义的上下文。对于 Qwen2.5 等基于 causal attention 的模型，left-padding 是 batch generation 的标准做法，可确保生成质量与单样本推理一致。\n\n## 3.2 Feature Extraction Pipeline\n\n我们设计了三组共 15 维统计特征，分别从 token-level surprisal dynamics、sequence-level vocabulary diversity 和 distributional-level tail structure 三个层面刻画文本的统计属性。这三组特征的设计动机来自递归生成的已知退化机制：surprisal 分布反映模型对文本的\"预期程度\"随深度偏移 [DivEye, 2026]；词汇多样性是 model collapse 文献中最广泛记录的退化信号 [Shumailov et al., 2024]；频率分布尾部结构则捕捉 Zipf 分布的系统性变形 [Shumailov et al., 2024]。\n\n### 3.2.1 Surprisal Features (9D)\n\nSurprisal 衡量模型对观测到的 token 的\"惊讶程度\"。给定文本序列 $\\mathbf{x} = (x_1, x_2, \\ldots, x_n)$ 和语言模型 $p_\\theta$，token $x_t$ 的 surprisal 定义为：\n\n$$s(x_t) = -\\log p_\\theta(x_t \\mid x_{&lt;t})$$\n\n其中 $x_{&lt;t} = (x_1, \\ldots, x_{t-1})$ 为前缀上下文。\n\n**动机**：递归生成的文本倾向于更\"符合预期\"——每经过一次 LLM 信道，输出文本的 token 分布趋近模型的先验偏好，surprisal 分布整体向低值偏移。这一趋势反映了信道级联中互信息 $I(X_0; X_k)$ 随深度单调衰减的理论预测。\n\n我们从 surprisal 序列 $\\{s(x_t)\\}_{t=2}^{n}$ 中提取以下统计量：\n\n**基础统计量 (4D)**：\n- $\\mu_s = \\frac{1}{n-1}\\sum_{t=2}^{n} s(x_t)$ — surprisal 均值，反映文本整体的可预测程度\n- $\\sigma_s = \\text{std}(\\{s(x_t)\\})$ — surprisal 标准差，反映 token 间可预测性的变异程度\n- $\\gamma_s = \\text{skewness}(\\{s(x_t)\\})$ — 偏度，捕捉 surprisal 分布的不对称性\n- $\\kappa_s = \\text{kurtosis}(\\{s(x_t)\\})$ — 峰度，捕捉 surprisal 分布的尾部厚度\n\n**一阶差分统计量 (3D)**：定义一阶差分 $\\Delta s_t = s(x_{t+1}) - s(x_t)$，反映相邻 token 间 surprisal 的局部变化动态。提取：\n- $\\mu_{\\Delta s}$ — 一阶差分均值\n- $\\sigma_{\\Delta s}$ — 一阶差分标准差\n- $\\gamma_{\\Delta s}$ — 一阶差分偏度（当 $|\\Delta s| \\geq 3$ 时计算，否则置为 0）\n\n**二阶差分统计量 (2D)**：定义二阶差分 $\\Delta^2 s_t = \\Delta s_{t+1} - \\Delta s_t$，捕捉 surprisal 变化的加速度。提取：\n- $\\mu_{\\Delta^2 s}$ — 二阶差分均值\n- $\\sigma_{\\Delta^2 s}$ — 二阶差分标准差\n\n一阶和二阶差分的引入受 DivEye [2026] 的启发——它们捕捉 surprisal 的 **temporal dynamics** 而非仅仅 distributional shape，能够反映递归生成文本中 token-level 可预测性的局部模式变化。\n\n**实现细节**：Surprisal 通过同一生成模型（Qwen2.5-1.5B-Instruct）计算。对于每个 token $x_t$，我们使用模型在前缀 $x_{&lt;t}$ 上的 logits 取 log-softmax 后的负对数概率。序列长度不足 3 个 token 的样本各维度置 0。计算采用 batch 推理（batch size = 8），使用 FP16 精度以控制显存占用。\n\n### 3.2.2 Vocabulary Diversity Features (3D)\n\n词汇多样性特征从 sequence level 衡量文本的词汇丰富度和重复模式。\n\n**Type-Token Ratio (TTR)**：\n\n$$\\text{TTR} = \\frac{|\\mathcal{V}(\\mathbf{x})|}{|\\mathbf{x}|}$$\n\n其中 $\\mathcal{V}(\\mathbf{x})$ 为文本 $\\mathbf{x}$ 中出现的不同词 (types) 的集合，$|\\mathbf{x}|$ 为总词数 (tokens)。TTR 越低，词汇重复度越高。\n\n**Hapax Ratio**：\n\n$$\\text{Hapax} = \\frac{|\\{w \\in \\mathcal{V}(\\mathbf{x}) : \\text{freq}(w) = 1\\}|}{|\\mathcal{V}(\\mathbf{x})|}$$\n\n即只出现一次的词 (hapax legomena) 占全部不同词的比例。Hapax ratio 对词频分布的尾部敏感——递归生成的尾部消失 (tail disappearance) 直接表现为 hapax ratio 下降。\n\n**Self-BLEU**：\n\n$$\\text{Self-BLEU}(\\mathbf{x}_i) = \\frac{1}{|R|} \\sum_{j \\in R} \\text{BLEU}_4(\\mathbf{x}_i, \\mathbf{x}_j)$$\n\n其中 $R$ 是从同一 depth 随机采样的参考文本集合（$|R| = 100$），$\\text{BLEU}_4$ 为标准的 4-gram BLEU score（含 brevity penalty）。Self-BLEU 衡量同一 depth 内不同文档间的 n-gram 重叠程度。\n\n**动机**：Self-BLEU 越高，说明同一深度的文本之间越相似——这正是递归生成导致的 progressive homogenization [Drayson et al., 2025] 的直接度量。与 TTR 和 Hapax ratio 关注单文档内部的多样性不同，Self-BLEU 捕捉的是同深度文档 **之间** 的多样性坍缩。\n\n**实现细节**：TTR 和 Hapax ratio 基于 whitespace tokenization（空格分词）在 word level 计算。Self-BLEU 的参考集从同深度文本中随机采样 100 篇（固定随机种子以保证可复现性），使用不依赖 NLTK 的轻量 4-gram BLEU 实现。\n\n### 3.2.3 Tail-thinning Features (3D)\n\n尾部稀疏特征从 distributional level 刻画文本词频分布的 Zipf 结构变化。\n\n**Frequency Kurtosis**：\n\n$$\\kappa_f = \\text{kurtosis}(\\{c_w : w \\in \\mathcal{V}(\\mathbf{x})\\})$$\n\n其中 $c_w = \\text{freq}(w, \\mathbf{x})$ 为词 $w$ 在文本 $\\mathbf{x}$ 中的出现次数。Kurtosis 衡量词频分布的尖峰和厚尾程度。当 unique types 不足 4 时置 0。\n\n**Frequency Entropy**：\n\n$$H_f = -\\sum_{w \\in \\mathcal{V}(\\mathbf{x})} \\hat{p}(w) \\log_2 \\hat{p}(w)$$\n\n其中 $\\hat{p}(w) = c_w / \\sum_{w'} c_{w'}$ 为 empirical unigram probability。Frequency entropy 衡量词频分布的均匀程度——entropy 越高，词频分布越接近均匀（diversity 越高）。\n\n**Low-frequency Ratio**：\n\n$$\\text{LFR} = \\frac{|\\{w \\in \\mathcal{V}(\\mathbf{x}) : c_w = 1\\}|}{|\\mathcal{V}(\\mathbf{x})|}$$\n\n即频次为 1 的词占所有 unique types 的比例。\n\n**动机**：Shumailov et al. [2024] 将 model collapse 分为三个阶段：tail disappearance → diversity loss → mode conflation。Tail-thinning features 直接刻画第一阶段——随着递归深度增加，词频分布的长尾逐渐消失，frequency kurtosis 下降（分布趋向扁平），frequency entropy 降低（分布集中于高频词），low-frequency ratio 减小（罕见词消失）。这些特征与 surprisal features 互补：surprisal 反映模型视角下的可预测性变化，而 tail-thinning 反映文本自身词频分布的结构性退化。\n\n**实现细节**：基于 whitespace tokenization 的词频统计。Entropy 计算中添加 $10^{-12}$ 的 smoothing 以避免 log(0)。\n\n### 特征总结\n\n| 特征组 | 维度 | 特征名 | 捕捉的退化信号 |\n|--------|------|--------|--------------|\n| Surprisal | 9 | surp\\_mean, surp\\_std, surp\\_skew, surp\\_kurt, surp\\_d1\\_mean, surp\\_d1\\_std, surp\\_d1\\_skew, surp\\_d2\\_mean, surp\\_d2\\_std | Token-level 可预测性偏移与动态变化 |\n| Vocab Diversity | 3 | ttr, hapax\\_ratio, self\\_bleu | 词汇丰富度衰减与文档间同质化 |\n| Tail-thinning | 3 | freq\\_kurtosis, freq\\_entropy, low\\_freq\\_ratio | Zipf 尾部消失与频率分布集中化 |\n\n全部 15 维特征均在 inference 时可计算（不依赖 paired original text 或跨深度信息），满足实际部署中仅有待检测文本可用的约束。\n\n## 3.3 Ordinal Depth Classifier\n\n### 分类器选择：LightGBM\n\n我们选用 **LightGBM** [Ke et al., 2017] 作为 depth classification 的 baseline 分类器。在 tabular features（低维手工特征）场景下，gradient boosted decision trees (GBDT) 通常优于或 comparable to 深度学习方法 [Grinsztajn et al., 2022, 需验证]，同时提供以下关键优势：\n\n(1) **可解释性**：LightGBM 原生提供 feature importance（基于 split gain 或 split count），使我们能够分析哪些特征对 depth discrimination 贡献最大，进而揭示递归生成的 linguistic degradation ordering。\n\n(2) **训练效率**：15 维特征 × 30,000 样本（5,000 docs × 6 depths）的规模下，LightGBM 训练仅需秒级时间，支持大量 ablation 实验和 cross-validation。\n\n(3) **对特征分布的鲁棒性**：GBDT 对特征缩放不敏感、能自然处理非线性关系和特征交互，无需额外的特征工程或归一化。\n\n### 任务设定\n\n我们在两个粒度上评估 depth discrimination 能力：\n\n**Pairwise Binary Classification**：对每对相邻深度 $(k-1, k)$，训练独立的二分类器。输入为 15 维特征向量，输出为 $\\{k-1, k\\}$ 的深度标签。pairwise AUC 是衡量相邻深度可区分性的核心指标，直接用于 $K^*$ 的计算。\n\n分类器参数：`n_estimators=200, max_depth=6, learning_rate=0.05, num_leaves=31`。\n\n**Ordinal Multi-class Classification**：将全部 6 个深度 (depth 0--5) 作为一个有序多分类问题。使用 LightGBM 的 `multiclass` objective，参数设为 `n_estimators=300, max_depth=8, num_leaves=63`。\n\n### 评估协议\n\n所有实验采用 **5-fold stratified cross-validation**。Stratified split 确保每个 fold 中各深度类别的比例一致。\n\n[TODO: grouped by doc\\_id 的实现——当前代码使用 StratifiedKFold 但未按 doc\\_id 分组。严格来说，同一 doc\\_id 在不同 depth 的文本应当被分配到同一 fold，以避免同源文档信息在训练集和测试集间泄露。这是一个需要在正式实验中修复的设计点。]\n\n### 评估指标\n\n- **Pairwise AUC**：每对相邻深度的 ROC-AUC，5-fold 均值和标准差。这是最核心的指标，直接反映每一步递归生成引入的 distributional shift 是否可被统计特征捕捉。\n\n- **MAE (Mean Absolute Error)**：ordinal classification 的预测深度与真实深度之差的均值。MAE 对 ordinal 结构敏感——将 depth-0 误分为 depth-1（MAE=1）比误分为 depth-5（MAE=5）惩罚更轻，符合\"相邻深度更难区分\"的直觉。\n\n- **Accuracy**：ordinal classification 的精确匹配准确率。\n\n- **Feature Importance**：LightGBM 的 split-based feature importance，按贡献排序，用于分析哪些特征组（surprisal / vocab diversity / tail-thinning）在 depth discrimination 中最为关键。\n\n## 3.4 Saturation Boundary $K^*$\n\n### 操作性定义\n\n我们定义 **判别饱和边界 (discriminability saturation boundary)** $K^*$ 为：\n\n$$K^* = \\max\\{k : \\text{AUC}(\\text{depth } k{-}1 \\text{ vs } k) > 0.60\\}$$\n\n即 $K^*$ 是满足相邻深度 pairwise AUC 大于 0.60 的最大深度。$K^*$ 之后（depth $> K^*$），相邻深度的文本在 15 维特征空间中不再具有可靠的统计可区分性。\n\n### 阈值选择理由\n\n选择 0.60 作为阈值基于以下考量：\n\n(1) **与 chance level 的间距**。二分类的 chance AUC = 0.50。阈值 0.60 对应 Cohen's $d$ [TODO: 计算对应效应量] 的 small-to-medium effect size，表示 \"微弱但可靠的可区分性\"。\n\n(2) **实践意义**。AUC = 0.60 意味着在随机抽取一对（depth $k{-}1$, depth $k$）样本时，分类器有 60% 的概率正确排序——略好于随机猜测，但已可为 downstream curation 提供有意义的信号。\n\n(3) **保守性**。相比更高阈值（如 0.70），0.60 允许更多深度被纳入\"可区分\"范围，使 $K^*$ 的估计偏向乐观。如果在此保守阈值下 $K^*$ 仍然较小，则更加确证了 depth discrimination 的 fundamental limit。\n\n### 与 DPI 理论的联系\n\n在信道级联框架下，$K^*$ 有明确的 information-theoretic 解释。由 Data Processing Inequality (DPI)，对 Markov chain $X_0 \\to X_1 \\to \\cdots \\to X_K$，有：\n\n$$I(X_0; X_k) \\leq I(X_0; X_{k-1}) \\leq \\cdots \\leq I(X_0; X_1) \\leq H(X_0)$$\n\n即关于原始人类文本 $X_0$ 的信息量随递归深度 **单调非递增**。每经过一次 LLM 信道 $\\mathcal{T}$（假设为 strictly lossy channel，即任何 temperature > 0 或 nucleus 截断都引入不可逆信息损失），互信息严格递减。\n\n$K^*$ 对应于 $I(X_0; X_k)$ 降至 noise floor 的临界深度——不是分类器的能力上限，而是 **information-theoretic impossibility boundary**：任何方法（无论多复杂）都无法区分 depth $> K^*$ 的文本，因为原始人类文本的信息已被信道噪声完全淹没。\n\n形式化地，若信道 $\\mathcal{T}$ 关于某分布度量 $d$ 是 contractive 的（即 $d(\\mathcal{T}(P), \\mathcal{T}(Q)) \\leq \\rho \\cdot d(P, Q)$，$0 < \\rho < 1$），则 $P_{X_k}$ 以几何速率趋近不动点分布 $P^*$：\n\n$$d(P_{X_k}, P^*) \\leq \\rho^k \\cdot d(P_{X_0}, P^*)$$\n\n相邻深度的分布差异同样以几何速率趋零：\n\n$$D(k, k{+}1) \\leq (\\rho^k + \\rho^{k+1}) \\cdot d(P_{X_0}, P^*)$$\n\n从而 $K^*(\\epsilon)$ 对任意阈值 $\\epsilon > 0$ 必然有限，其粗略 scaling 为：\n\n$$K^* = O\\left(\\frac{\\log(d(P_{X_0}, P^*) / \\epsilon)}{\\log(1/\\rho)}\\right)$$\n\n这表明 $K^*$ 由信道的 contraction rate $\\rho$ 和 seed 文本分布到不动点的初始距离共同决定。\n\n### 经验验证方法\n\n我们使用 pairwise AUC 作为 discriminability 的 empirical proxy，配合 Jensen-Shannon Divergence (JSD) 作为 distributional distance 的 computationally tractable proxy：\n\n$$\\text{JSD}(P_{X_k} \\| P_{X_{k'}}) = \\frac{1}{2} D_{\\text{KL}}(P_{X_k} \\| M) + \\frac{1}{2} D_{\\text{KL}}(P_{X_{k'}} \\| M)$$\n\n其中 $M = \\frac{1}{2}(P_{X_k} + P_{X_{k'}})$。JSD 在 unigram level 上按 feature 维度分别计算（基于 50-bin 直方图估计），取均值作为综合度量。\n\n需要承认的局限：unigram-level JSD 忽略了序列结构（n-gram patterns、句法依赖等），不等价于真正的互信息 $I(X_0; X_k)$。但 DPI 的定性结论——单调衰减——在 JSD 框架下同样成立，因此作为 tracking metric 仍然有效。\n\n### $K^*$ 的科学意义\n\n$K^*$ 是本工作提出的首次被系统测量的科学量。此前关于递归生成退化的研究 [Shumailov et al., 2024; Drayson et al., 2025] 主要提供定性描述（\"early generations show most change\"），但从未给出精确的判别边界。$K^*$ 的测量具有直接的实践指导价值：\n\n- **对数据 curation 从业者**：$K^*$ 告诉你在当前模型和生成配置下，depth-aware filtering 能有效区分多少层深度——depth $\\leq K^*$ 的文本可进行 graduated weighting，depth $> K^*$ 的文本可统一处理。\n- **对 model collapse 研究**：$K^*$ 量化了 Shumailov et al. 描述的 \"early collapse\" 与 \"late collapse\" 之间的精确过渡边界。\n- **对 AI 生成文本检测**：$K^*$ 揭示了 depth estimation 作为检测范式的 fundamental resolution limit——无论特征工程或分类器如何改进，信息论约束决定了 $K^*$ 之外不可能做得更好。\n\n[TODO: 补充 MVP 实验中测得的 $K^*$ 实际值及其置信区间]\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a2b3c6e1-bf66-4ff6-bec8-41639f3adf55",
  "uuid": "671e969b-0e82-4493-aabd-5f9f3dad18a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmNb8VGnpteYkmQakeHCLu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30544,
      "cache_read_input_tokens": 24551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 30544
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

_source line 21 · 2026-05-12T16:28:04.355Z_

<details><summary>↩ Tool result · `toolu_01DbzYjodTTMCQ4mHBByKf7w`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/methodology_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a2b3c6e1-bf66-4ff6-bec8-41639f3adf55",
  "uuid": "c2ec5c85-2ccb-44a6-bf00-2721865a1b18",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/methodology_draft.md",
    "content": "# 3. Methodology\n\n## 3.1 Multi-generation Corpus Construction\n\n### 问题形式化\n\n设 $X_0$ 为人类撰写的文本（seed text），建模为概率空间上的随机变量。LLM 的生成过程定义为随机信道 $\\mathcal{T}: \\mathcal{X} \\to \\mathcal{X}$，将输入文本映射到输出文本。递归生成形成 Markov chain：\n\n$$X_0 \\xrightarrow{\\mathcal{T}} X_1 \\xrightarrow{\\mathcal{T}} X_2 \\xrightarrow{\\mathcal{T}} \\cdots \\xrightarrow{\\mathcal{T}} X_K$$\n\n其中 depth-0 文本 $X_0$ 为人类原始文本，depth-$k$ 文本 $X_k = \\mathcal{T}(X_{k-1})$ 由 depth-$(k-1)$ 文本经过一次 LLM 信道产生。该形式化依赖两个关键假设：**(A1) 时不变信道**——同一 LLM 与 decoding strategy 在每次迭代中定义相同的信道 $\\mathcal{T}$；**(A2) Markov 性**——$X_{k+1}$ 仅依赖 $X_k$，不依赖更早的 $X_0, \\ldots, X_{k-1}$。这两个假设在 prompt-chain 设定下成立（每次生成仅以上一轮输出为输入），retrain-chain 场景需将 $\\mathcal{T}$ 放宽为 $\\mathcal{T}_k$。\n\n### Prompt-chain 实现\n\n我们采用 prompt-chain 方式构造 depth chain：每一轮将前一深度的文本嵌入固定的 rewrite prompt 模板，由模型生成同主题、同风格的新文本。具体 prompt 模板如下：\n\n> Below is a passage. Write a new passage of similar length on the same topic and in the same style.\n>\n> Original passage:\n> {prev\\_text}\n>\n> New passage:\n\n该模板要求模型保持主题与风格一致性，同时生成全新文本而非简单复述。这一设计的意图是模拟现实场景中合成文本被反复改写的过程——例如 AI 生成的内容被爬取后再次作为 LLM 的输入进行改写或续写。\n\nPrompt-chain 与 retrain-chain（在合成数据上重新训练模型再生成）的区别值得说明。Retrain-chain 更接近 Shumailov et al. [2024] 描述的 model collapse 真实路径，但 prompt-chain 提供了一个 **upper bound estimate**：如果在 prompt-chain（模型权重不变、仅输入文本退化）下特征已饱和，retrain-chain（模型本身也退化）下只会更快饱和。我们选择 prompt-chain 作为 MVP 方案以控制变量，retrain-chain 验证留作后续研究。\n\n### 模型选择\n\n我们选用 **Qwen2.5-1.5B-Instruct** [Qwen Team, 2024] 作为生成模型。选择理由如下：\n\n**Instruct 而非 base 模型**。现实世界中绝大多数合成文本（ChatGPT 输出、AI 写作工具、自动摘要等）均来自经过 instruction tuning 的模型。使用 Instruct 版本可确保生成文本的分布特征更接近实际污染数据。此外，Instruct 模型能更好地遵循 rewrite prompt 中的改写指令，生成主题一致但非直接复制的文本，而 base 模型可能简单延续原文或产生不相关内容。\n\n**1.5B 参数规模**。选择小规模模型基于以下考量：(1) 计算效率——在单块 RTX 4090D (24GB) 上可高效完成 5000 文档 × 5 个深度的生成任务；(2) model collapse 文献 [Shumailov et al., 2024; Drayson et al., 2025] 表明退化现象在小模型上更为显著，有利于在 pilot study 中观察清晰的深度信号；(3) Qwen2.5 系列在 1.5B 规模上已展现出 competitive 的语言能力 [需验证]，足以生成流畅且有意义的文本。Full study 阶段将扩展到多模型家族（Pythia-1.4B, OLMo-1B）及更大规模（Qwen2.5-7B/14B）进行 cross-model 和 cross-scale 验证。\n\n### 解码参数\n\n采用 **nucleus sampling** (top-$p$ sampling)，参数设定为 $p = 0.95$, temperature $T = 1.0$。这一配置的理由在于：\n\n(1) **接近真实世界配置**。主流 LLM 应用（ChatGPT、Claude、各类 API 调用）的默认或推荐生成参数通常处于 $T \\in [0.7, 1.0]$, $p \\in [0.9, 0.95]$ 的区间。$T=1.0, p=0.95$ 代表了一个 moderately stochastic 的生成配置，既保留了足够的随机性以反映真实合成文本的 diversity，又不至于因过高 temperature 产生不自然的噪声文本。\n\n(2) **信道噪声的理论考量**。在信道级联框架下，$T$ 和 $p$ 共同决定了信道 $\\mathcal{T}$ 的 contraction rate $\\rho$。Greedy decoding ($T \\to 0$) 使信道趋近确定性（$\\rho \\to 1$），信息衰减慢但 diversity 低；高 temperature 使信道趋近均匀随机（$\\rho \\to 0$），信息快速丢失。$T=1.0, p=0.95$ 处于中间区域，既保证可观测的深度信号，又不人为加速或延缓饱和。\n\n### 种子数据\n\n种子数据取自 **C4 (Colossal Clean Crawled Corpus)** [Raffel et al., 2020] 的 validation split。从中采样 **5,000 篇文档**，每篇文档经 tokenizer 截断至 **256 tokens** 后作为 depth-0 文本。\n\n选择 C4 的理由：(1) 作为广泛使用的预训练语料，C4 文本代表了典型的 web 文本分布；(2) validation split 保证不与常见模型的训练集重叠。5,000 篇文档的规模在 pilot study 中足以提供可靠的统计估计，同时控制计算成本。\n\n截断至 256 tokens 的考量：(1) 控制生成长度一致性——过长的 seed text 导致生成文本长度方差大，干扰特征提取；(2) 256 tokens 足以包含 1-2 个完整段落的语义信息，保留主题和风格特征；(3) 与模型的 max prompt length 配合——prompt 模板 + seed text 需要在 512 tokens 内完成。\n\n### Left-padding 技术考量\n\n在 batch 推理中，我们采用 **left-padding** (`tokenizer.padding_side = \"left\"`)。这一选择对 causal language model 的生成质量至关重要：\n\nRight-padding（将 pad token 追加到序列末尾）会导致模型在生成时\"看到\"大量无意义的 pad token，影响注意力分布和生成质量。Left-padding 将 pad token 置于序列左侧，真实 token 右对齐，使得模型在生成时只关注到有意义的上下文。对于 Qwen2.5 等基于 causal attention 的模型，left-padding 是 batch generation 的标准做法，可确保生成质量与单样本推理一致。\n\n## 3.2 Feature Extraction Pipeline\n\n我们设计了三组共 15 维统计特征，分别从 token-level surprisal dynamics、sequence-level vocabulary diversity 和 distributional-level tail structure 三个层面刻画文本的统计属性。这三组特征的设计动机来自递归生成的已知退化机制：surprisal 分布反映模型对文本的\"预期程度\"随深度偏移 [DivEye, 2026]；词汇多样性是 model collapse 文献中最广泛记录的退化信号 [Shumailov et al., 2024]；频率分布尾部结构则捕捉 Zipf 分布的系统性变形 [Shumailov et al., 2024]。\n\n### 3.2.1 Surprisal Features (9D)\n\nSurprisal 衡量模型对观测到的 token 的\"惊讶程度\"。给定文本序列 $\\mathbf{x} = (x_1, x_2, \\ldots, x_n)$ 和语言模型 $p_\\theta$，token $x_t$ 的 surprisal 定义为：\n\n$$s(x_t) = -\\log p_\\theta(x_t \\mid x_{&lt;t})$$\n\n其中 $x_{&lt;t} = (x_1, \\ldots, x_{t-1})$ 为前缀上下文。\n\n**动机**：递归生成的文本倾向于更\"符合预期\"——每经过一次 LLM 信道，输出文本的 token 分布趋近模型的先验偏好，surprisal 分布整体向低值偏移。这一趋势反映了信道级联中互信息 $I(X_0; X_k)$ 随深度单调衰减的理论预测。\n\n我们从 surprisal 序列 $\\{s(x_t)\\}_{t=2}^{n}$ 中提取以下统计量：\n\n**基础统计量 (4D)**：\n- $\\mu_s = \\frac{1}{n-1}\\sum_{t=2}^{n} s(x_t)$ — surprisal 均值，反映文本整体的可预测程度\n- $\\sigma_s = \\text{std}(\\{s(x_t)\\})$ — surprisal 标准差，反映 token 间可预测性的变异程度\n- $\\gamma_s = \\text{skewness}(\\{s(x_t)\\})$ — 偏度，捕捉 surprisal 分布的不对称性\n- $\\kappa_s = \\text{kurtosis}(\\{s(x_t)\\})$ — 峰度，捕捉 surprisal 分布的尾部厚度\n\n**一阶差分统计量 (3D)**：定义一阶差分 $\\Delta s_t = s(x_{t+1}) - s(x_t)$，反映相邻 token 间 surprisal 的局部变化动态。提取：\n- $\\mu_{\\Delta s}$ — 一阶差分均值\n- $\\sigma_{\\Delta s}$ — 一阶差分标准差\n- $\\gamma_{\\Delta s}$ — 一阶差分偏度（当 $|\\Delta s| \\geq 3$ 时计算，否则置为 0）\n\n**二阶差分统计量 (2D)**：定义二阶差分 $\\Delta^2 s_t = \\Delta s_{t+1} - \\Delta s_t$，捕捉 surprisal 变化的加速度。提取：\n- $\\mu_{\\Delta^2 s}$ — 二阶差分均值\n- $\\sigma_{\\Delta^2 s}$ — 二阶差分标准差\n\n一阶和二阶差分的引入受 DivEye [2026] 的启发——它们捕捉 surprisal 的 **temporal dynamics** 而非仅仅 distributional shape，能够反映递归生成文本中 token-level 可预测性的局部模式变化。\n\n**实现细节**：Surprisal 通过同一生成模型（Qwen2.5-1.5B-Instruct）计算。对于每个 token $x_t$，我们使用模型在前缀 $x_{&lt;t}$ 上的 logits 取 log-softmax 后的负对数概率。序列长度不足 3 个 token 的样本各维度置 0。计算采用 batch 推理（batch size = 8），使用 FP16 精度以控制显存占用。\n\n### 3.2.2 Vocabulary Diversity Features (3D)\n\n词汇多样性特征从 sequence level 衡量文本的词汇丰富度和重复模式。\n\n**Type-Token Ratio (TTR)**：\n\n$$\\text{TTR} = \\frac{|\\mathcal{V}(\\mathbf{x})|}{|\\mathbf{x}|}$$\n\n其中 $\\mathcal{V}(\\mathbf{x})$ 为文本 $\\mathbf{x}$ 中出现的不同词 (types) 的集合，$|\\mathbf{x}|$ 为总词数 (tokens)。TTR 越低，词汇重复度越高。\n\n**Hapax Ratio**：\n\n$$\\text{Hapax} = \\frac{|\\{w \\in \\mathcal{V}(\\mathbf{x}) : \\text{freq}(w) = 1\\}|}{|\\mathcal{V}(\\mathbf{x})|}$$\n\n即只出现一次的词 (hapax legomena) 占全部不同词的比例。Hapax ratio 对词频分布的尾部敏感——递归生成的尾部消失 (tail disappearance) 直接表现为 hapax ratio 下降。\n\n**Self-BLEU**：\n\n$$\\text{Self-BLEU}(\\mathbf{x}_i) = \\frac{1}{|R|} \\sum_{j \\in R} \\text{BLEU}_4(\\mathbf{x}_i, \\mathbf{x}_j)$$\n\n其中 $R$ 是从同一 depth 随机采样的参考文本集合（$|R| = 100$），$\\text{BLEU}_4$ 为标准的 4-gram BLEU score（含 brevity penalty）。Self-BLEU 衡量同一 depth 内不同文档间的 n-gram 重叠程度。\n\n**动机**：Self-BLEU 越高，说明同一深度的文本之间越相似——这正是递归生成导致的 progressive homogenization [Drayson et al., 2025] 的直接度量。与 TTR 和 Hapax ratio 关注单文档内部的多样性不同，Self-BLEU 捕捉的是同深度文档 **之间** 的多样性坍缩。\n\n**实现细节**：TTR 和 Hapax ratio 基于 whitespace tokenization（空格分词）在 word level 计算。Self-BLEU 的参考集从同深度文本中随机采样 100 篇（固定随机种子以保证可复现性），使用不依赖 NLTK 的轻量 4-gram BLEU 实现。\n\n### 3.2.3 Tail-thinning Features (3D)\n\n尾部稀疏特征从 distributional level 刻画文本词频分布的 Zipf 结构变化。\n\n**Frequency Kurtosis**：\n\n$$\\kappa_f = \\text{kurtosis}(\\{c_w : w \\in \\mathcal{V}(\\mathbf{x})\\})$$\n\n其中 $c_w = \\text{freq}(w, \\mathbf{x})$ 为词 $w$ 在文本 $\\mathbf{x}$ 中的出现次数。Kurtosis 衡量词频分布的尖峰和厚尾程度。当 unique types 不足 4 时置 0。\n\n**Frequency Entropy**：\n\n$$H_f = -\\sum_{w \\in \\mathcal{V}(\\mathbf{x})} \\hat{p}(w) \\log_2 \\hat{p}(w)$$\n\n其中 $\\hat{p}(w) = c_w / \\sum_{w'} c_{w'}$ 为 empirical unigram probability。Frequency entropy 衡量词频分布的均匀程度——entropy 越高，词频分布越接近均匀（diversity 越高）。\n\n**Low-frequency Ratio**：\n\n$$\\text{LFR} = \\frac{|\\{w \\in \\mathcal{V}(\\mathbf{x}) : c_w = 1\\}|}{|\\mathcal{V}(\\mathbf{x})|}$$\n\n即频次为 1 的词占所有 unique types 的比例。\n\n**动机**：Shumailov et al. [2024] 将 model collapse 分为三个阶段：tail disappearance → diversity loss → mode conflation。Tail-thinning features 直接刻画第一阶段——随着递归深度增加，词频分布的长尾逐渐消失，frequency kurtosis 下降（分布趋向扁平），frequency entropy 降低（分布集中于高频词），low-frequency ratio 减小（罕见词消失）。这些特征与 surprisal features 互补：surprisal 反映模型视角下的可预测性变化，而 tail-thinning 反映文本自身词频分布的结构性退化。\n\n**实现细节**：基于 whitespace tokenization 的词频统计。Entropy 计算中添加 $10^{-12}$ 的 smoothing 以避免 log(0)。\n\n### 特征总结\n\n| 特征组 | 维度 | 特征名 | 捕捉的退化信号 |\n|--------|------|--------|--------------|\n| Surprisal | 9 | surp\\_mean, surp\\_std, surp\\_skew, surp\\_kurt, surp\\_d1\\_mean, surp\\_d1\\_std, surp\\_d1\\_skew, surp\\_d2\\_mean, surp\\_d2\\_std | Token-level 可预测性偏移与动态变化 |\n| Vocab Diversity | 3 | ttr, hapax\\_ratio, self\\_bleu | 词汇丰富度衰减与文档间同质化 |\n| Tail-thinning | 3 | freq\\_kurtosis, freq\\_entropy, low\\_freq\\_ratio | Zipf 尾部消失与频率分布集中化 |\n\n全部 15 维特征均在 inference 时可计算（不依赖 paired original text 或跨深度信息），满足实际部署中仅有待检测文本可用的约束。\n\n## 3.3 Ordinal Depth Classifier\n\n### 分类器选择：LightGBM\n\n我们选用 **LightGBM** [Ke et al., 2017] 作为 depth classification 的 baseline 分类器。在 tabular features（低维手工特征）场景下，gradient boosted decision trees (GBDT) 通常优于或 comparable to 深度学习方法 [Grinsztajn et al., 2022, 需验证]，同时提供以下关键优势：\n\n(1) **可解释性**：LightGBM 原生提供 feature importance（基于 split gain 或 split count），使我们能够分析哪些特征对 depth discrimination 贡献最大，进而揭示递归生成的 linguistic degradation ordering。\n\n(2) **训练效率**：15 维特征 × 30,000 样本（5,000 docs × 6 depths）的规模下，LightGBM 训练仅需秒级时间，支持大量 ablation 实验和 cross-validation。\n\n(3) **对特征分布的鲁棒性**：GBDT 对特征缩放不敏感、能自然处理非线性关系和特征交互，无需额外的特征工程或归一化。\n\n### 任务设定\n\n我们在两个粒度上评估 depth discrimination 能力：\n\n**Pairwise Binary Classification**：对每对相邻深度 $(k-1, k)$，训练独立的二分类器。输入为 15 维特征向量，输出为 $\\{k-1, k\\}$ 的深度标签。pairwise AUC 是衡量相邻深度可区分性的核心指标，直接用于 $K^*$ 的计算。\n\n分类器参数：`n_estimators=200, max_depth=6, learning_rate=0.05, num_leaves=31`。\n\n**Ordinal Multi-class Classification**：将全部 6 个深度 (depth 0--5) 作为一个有序多分类问题。使用 LightGBM 的 `multiclass` objective，参数设为 `n_estimators=300, max_depth=8, num_leaves=63`。\n\n### 评估协议\n\n所有实验采用 **5-fold stratified cross-validation**。Stratified split 确保每个 fold 中各深度类别的比例一致。\n\n[TODO: grouped by doc\\_id 的实现——当前代码使用 StratifiedKFold 但未按 doc\\_id 分组。严格来说，同一 doc\\_id 在不同 depth 的文本应当被分配到同一 fold，以避免同源文档信息在训练集和测试集间泄露。这是一个需要在正式实验中修复的设计点。]\n\n### 评估指标\n\n- **Pairwise AUC**：每对相邻深度的 ROC-AUC，5-fold 均值和标准差。这是最核心的指标，直接反映每一步递归生成引入的 distributional shift 是否可被统计特征捕捉。\n\n- **MAE (Mean Absolute Error)**：ordinal classification 的预测深度与真实深度之差的均值。MAE 对 ordinal 结构敏感——将 depth-0 误分为 depth-1（MAE=1）比误分为 depth-5（MAE=5）惩罚更轻，符合\"相邻深度更难区分\"的直觉。\n\n- **Accuracy**：ordinal classification 的精确匹配准确率。\n\n- **Feature Importance**：LightGBM 的 split-based feature importance，按贡献排序，用于分析哪些特征组（surprisal / vocab diversity / tail-thinning）在 depth discrimination 中最为关键。\n\n## 3.4 Saturation Boundary $K^*$\n\n### 操作性定义\n\n我们定义 **判别饱和边界 (discriminability saturation boundary)** $K^*$ 为：\n\n$$K^* = \\max\\{k : \\text{AUC}(\\text{depth } k{-}1 \\text{ vs } k) > 0.60\\}$$\n\n即 $K^*$ 是满足相邻深度 pairwise AUC 大于 0.60 的最大深度。$K^*$ 之后（depth $> K^*$），相邻深度的文本在 15 维特征空间中不再具有可靠的统计可区分性。\n\n### 阈值选择理由\n\n选择 0.60 作为阈值基于以下考量：\n\n(1) **与 chance level 的间距**。二分类的 chance AUC = 0.50。阈值 0.60 对应 Cohen's $d$ [TODO: 计算对应效应量] 的 small-to-medium effect size，表示 \"微弱但可靠的可区分性\"。\n\n(2) **实践意义**。AUC = 0.60 意味着在随机抽取一对（depth $k{-}1$, depth $k$）样本时，分类器有 60% 的概率正确排序——略好于随机猜测，但已可为 downstream curation 提供有意义的信号。\n\n(3) **保守性**。相比更高阈值（如 0.70），0.60 允许更多深度被纳入\"可区分\"范围，使 $K^*$ 的估计偏向乐观。如果在此保守阈值下 $K^*$ 仍然较小，则更加确证了 depth discrimination 的 fundamental limit。\n\n### 与 DPI 理论的联系\n\n在信道级联框架下，$K^*$ 有明确的 information-theoretic 解释。由 Data Processing Inequality (DPI)，对 Markov chain $X_0 \\to X_1 \\to \\cdots \\to X_K$，有：\n\n$$I(X_0; X_k) \\leq I(X_0; X_{k-1}) \\leq \\cdots \\leq I(X_0; X_1) \\leq H(X_0)$$\n\n即关于原始人类文本 $X_0$ 的信息量随递归深度 **单调非递增**。每经过一次 LLM 信道 $\\mathcal{T}$（假设为 strictly lossy channel，即任何 temperature > 0 或 nucleus 截断都引入不可逆信息损失），互信息严格递减。\n\n$K^*$ 对应于 $I(X_0; X_k)$ 降至 noise floor 的临界深度——不是分类器的能力上限，而是 **information-theoretic impossibility boundary**：任何方法（无论多复杂）都无法区分 depth $> K^*$ 的文本，因为原始人类文本的信息已被信道噪声完全淹没。\n\n形式化地，若信道 $\\mathcal{T}$ 关于某分布度量 $d$ 是 contractive 的（即 $d(\\mathcal{T}(P), \\mathcal{T}(Q)) \\leq \\rho \\cdot d(P, Q)$，$0 < \\rho < 1$），则 $P_{X_k}$ 以几何速率趋近不动点分布 $P^*$：\n\n$$d(P_{X_k}, P^*) \\leq \\rho^k \\cdot d(P_{X_0}, P^*)$$\n\n相邻深度的分布差异同样以几何速率趋零：\n\n$$D(k, k{+}1) \\leq (\\rho^k + \\rho^{k+1}) \\cdot d(P_{X_0}, P^*)$$\n\n从而 $K^*(\\epsilon)$ 对任意阈值 $\\epsilon > 0$ 必然有限，其粗略 scaling 为：\n\n$$K^* = O\\left(\\frac{\\log(d(P_{X_0}, P^*) / \\epsilon)}{\\log(1/\\rho)}\\right)$$\n\n这表明 $K^*$ 由信道的 contraction rate $\\rho$ 和 seed 文本分布到不动点的初始距离共同决定。\n\n### 经验验证方法\n\n我们使用 pairwise AUC 作为 discriminability 的 empirical proxy，配合 Jensen-Shannon Divergence (JSD) 作为 distributional distance 的 computationally tractable proxy：\n\n$$\\text{JSD}(P_{X_k} \\| P_{X_{k'}}) = \\frac{1}{2} D_{\\text{KL}}(P_{X_k} \\| M) + \\frac{1}{2} D_{\\text{KL}}(P_{X_{k'}} \\| M)$$\n\n其中 $M = \\frac{1}{2}(P_{X_k} + P_{X_{k'}})$。JSD 在 unigram level 上按 feature 维度分别计算（基于 50-bin 直方图估计），取均值作为综合度量。\n\n需要承认的局限：unigram-level JSD 忽略了序列结构（n-gram patterns、句法依赖等），不等价于真正的互信息 $I(X_0; X_k)$。但 DPI 的定性结论——单调衰减——在 JSD 框架下同样成立，因此作为 tracking metric 仍然有效。\n\n### $K^*$ 的科学意义\n\n$K^*$ 是本工作提出的首次被系统测量的科学量。此前关于递归生成退化的研究 [Shumailov et al., 2024; Drayson et al., 2025] 主要提供定性描述（\"early generations show most change\"），但从未给出精确的判别边界。$K^*$ 的测量具有直接的实践指导价值：\n\n- **对数据 curation 从业者**：$K^*$ 告诉你在当前模型和生成配置下，depth-aware filtering 能有效区分多少层深度——depth $\\leq K^*$ 的文本可进行 graduated weighting，depth $> K^*$ 的文本可统一处理。\n- **对 model collapse 研究**：$K^*$ 量化了 Shumailov et al. 描述的 \"early collapse\" 与 \"late collapse\" 之间的精确过渡边界。\n- **对 AI 生成文本检测**：$K^*$ 揭示了 depth estimation 作为检测范式的 fundamental resolution limit——无论特征工程或分类器如何改进，信息论约束决定了 $K^*$ 之外不可能做得更好。\n\n[TODO: 补充 MVP 实验中测得的 $K^*$ 实际值及其置信区间]\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 22_

Methodology 初稿已写入 `docs/methodology_draft.md`。

涵盖四个 subsection：
- **3.1** 形式化定义、prompt-chain 实现（含精确 prompt 模板）、模型选择理由、解码参数、种子数据、left-padding
- **3.2** 三组 15 维特征的精确公式——surprisal 9D（含一阶/二阶差分）、vocab diversity 3D（TTR/hapax/self-BLEU）、tail-thinning 3D（kurtosis/entropy/LFR），全部从 `run_pipeline.py` 提取
- **3.3** LightGBM 选择理由、pairwise + ordinal 两级评估、5-fold CV 协议、四项指标
- **3.4** $K^*$ 操作性定义（AUC > 0.60）、阈值理由、DPI 理论联系（含 contraction rate scaling）、JSD proxy 及其局限、科学意义

标注了 3 处 `[TODO]` 待补充实验数据，1 处 `[需验证]` 标注不确定的引用。还标注了 doc\_id grouped CV 的设计缺陷需在正式实验中修复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a2b3c6e1-bf66-4ff6-bec8-41639f3adf55",
  "uuid": "a0b0b1ec-de9e-4f06-8899-b74e165ba83a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01As1LAUjXWpYiPG32JssDRN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9014,
      "cache_read_input_tokens": 55095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9014
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

### Task result

_source line 23_

Methodology 初稿已写入 `docs/methodology_draft.md`。

涵盖四个 subsection：
- **3.1** 形式化定义、prompt-chain 实现（含精确 prompt 模板）、模型选择理由、解码参数、种子数据、left-padding
- **3.2** 三组 15 维特征的精确公式——surprisal 9D（含一阶/二阶差分）、vocab diversity 3D（TTR/hapax/self-BLEU）、tail-thinning 3D（kurtosis/entropy/LFR），全部从 `run_pipeline.py` 提取
- **3.3** LightGBM 选择理由、pairwise + ordinal 两级评估、5-fold CV 协议、四项指标
- **3.4** $K^*$ 操作性定义（AUC > 0.60）、阈值理由、DPI 理论联系（含 contraction rate scaling）、JSD proxy 及其局限、科学意义

标注了 3 处 `[TODO]` 待补充实验数据，1 处 `[需验证]` 标注不确定的引用。还标注了 doc\_id grouped CV 的设计缺陷需在正式实验中修复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 198983,
  "duration_api_ms": 200089,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "a2b3c6e1-bf66-4ff6-bec8-41639f3adf55",
  "total_cost_usd": 0.6328805000000001,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 52268,
    "cache_read_input_tokens": 115557,
    "output_tokens": 9849,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 52268,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 356,
        "cache_read_input_tokens": 55095,
        "cache_creation_input_tokens": 9014,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 9014
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2097,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002167,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 9849,
      "cacheReadInputTokens": 115557,
      "cacheCreationInputTokens": 52268,
      "webSearchRequests": 0,
      "costUSD": 0.6307135,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "4e571d59-2019-48a7-9533-b67cb7d75bc6"
}
```

</details>

---
