# doc phase0 experiment spec

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 62
- **Recorded user turns:** 0
- **Tool calls:** 24
- **Original source:** `logs/workers/worker_doc_phase0-experiment-spec_20260515T110032.log`
- **Structured JSON:** [`c9dc4bb8b8dc801d37e0.json`](../../sessions/c9/c9dc4bb8b8dc801d37e0.json)

## Before a recorded user message

62 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing",
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
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
  "uuid": "23c219be-60cb-4641-b0a0-976ee4e45a6d",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-meta-brain-lora-routing/memory/"
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
    "resetsAt": 1778844600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "2a42d0ff-8ca9-4540-894e-c95116413c94",
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7"
}
```

---

### Assistant

_source line 4_

我先读取项目相关文件，了解上下文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "e055de53-7476-4853-bad5-b18b97386069",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TYv34weJNcL4SffBQnMZAK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12758,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12758
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01J86zsYLMwvYSQPjC4dr4K3`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "5c0ac131-5e18-42fc-ae15-a376bbcc610a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TYv34weJNcL4SffBQnMZAK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12758,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12758
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

_source line 6 · 2026-05-15T11:00:43.208Z_

<details><summary>↩ Tool result · `toolu_01J86zsYLMwvYSQPjC4dr4K3`</summary>

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

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
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
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "57175fc4-f341-450b-a9f1-75a7565bdcbf",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__append_idea"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea",
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
Let me read the project's key files to understand the context before writing the spec.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "8e1b471c-c558-46b3-a927-584209da300e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JCvNB6GpfQtHCvxeWiFZMF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 912,
      "cache_read_input_tokens": 24205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 912
      },
      "output_tokens": 41,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017SLB3njN3k7wQYysGjm6Nd`</summary>

```json
{
  "project": "meta_brain_lora_routing",
  "file": "ROADMAP.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "d1b2a0a6-4e87-4a91-bcb7-4c774d7bc229",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JCvNB6GpfQtHCvxeWiFZMF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 912,
      "cache_read_input_tokens": 24205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 912
      },
      "output_tokens": 41,
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

_source line 9 · 2026-05-15T11:00:47.055Z_

<details><summary>↩ Tool result · `toolu_017SLB3njN3k7wQYysGjm6Nd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/ROADMAP.md\", \"content\": \"# meta_brain_lora_routing — Research Dashboard\\n\\n> 最后更新: 2026-05-15 10:44 UTC | 更新原因: Critical fix: π₀ 层索引修正 (18层 not 32层) + 排除 Language Instructions + 增加 Action Expert 探针\\n\\n## 核心方向\\nPerturbation-Adaptive LoRA Routing：在冻结的 VLA backbone (π₀, PaliGemma-Gemma 2B) 上，用轻量级 router 从内部激活诊断扰动类型，路由到对应专用 LoRA expert 修正。核心假设：扰动类型感知的专用路由 > 通用适配（参数效率 6M vs 114M）。详见 IDEA_BRIEF.md。\\n\\n## 目标会议\\nCoRL 2026 — Abstract DDL: 2026-05-26 (11天)，Paper DDL: 2026-05-29 (14天)\\n\\n## 当前进展\\n- 阶段：**MVP 验证**（Phase 0 early-kill gate）\\n- 实验：暂无\\n- 基础设施：**未配置**（无服务器、无 GPU）— 等用户提供\\n- Agent：正在调研 OpenPI + LIBERO-Plus（worker 已完成，结果待 Agent 消化）\\n- Reviewer 审查：2 轮（MVP 设计 WARNING + OpenPI 调研 WARNING/CRITICAL），已全部采纳\\n\\n## 架构关键参数（worker 调研确认）\\n- **π₀ backbone**: PaliGemma VLM (Gemma 2B LLM, 18 layers, 2048-dim) + Action Expert (18 layers, 1024-dim)\\n- **激活提取层**: PaliGemma {2,4,6,8,10,12,14,16} + Action Expert {2,6,10,14}（共 12 层）\\n- ⚠️ IDEA_BRIEF 原写 layers {4,8,12,16,20,24,28,32} 基于 32 层假设，**已修正**\\n\\n## MVP 验证方案（Phase 0 — 增强版 v2）\\n\\n**核心假设**: π₀ 内部激活编码了扰动类型信息，可被轻量级 probe 分类\\n\\n**扰动分类 taxonomy**:\\n- LIBERO-Plus 7 类中排除 Language Instructions（语言扰动不影响 visual token representation，不属于 LoRA 修正范围）\\n- 6 类覆盖：Camera, Light, Background, Noise, Robot, Layout\\n- 3-class 映射：Visual (Camera+Light+Background+Noise) / Spatial (Layout) / Physical (Robot)\\n- 同时跑 6-class 对照\\n\\n**实验设计**:\\n1. 搭建 π₀ + LIBERO-Plus 环境（OpenPI codebase）\\n2. 冻结 π₀ 在 6 类扰动下 rollout ~500 episodes\\n3. 记录 PaliGemma 8 层 + Action Expert 4 层的 pooled 激活（~0.95GB）\\n4. 训练 3 套分类器：3-class / 6-class / binary anomaly detection\\n5. Sweep: 3 pooling × layer subsets × 3 lr；对比 PaliGemma-only vs Expert-only vs 双 Transformer\\n\\n**报告要求**: overall accuracy + per-class F1 + confusion matrix + binary ROC-AUC + PaliGemma vs Expert 对比\\n\\n**Pass/Fail**: >70% 3-class + confusion matrix 无严重混淆 → GO；50-70% → 增强输入；<50% → Pivot\\n\\n## Reviewer 关注点\\n1. **Impact 3/5**: 目标 72-80% 低于 SOTA 82.1% → 参数效率差异化\\n2. **SAFE 类比不成立**: 已补 binary sanity check\\n3. **误路由风险**: 已补 confusion matrix + 后续 oracle routing ablation\\n4. **Language Instructions**: 排除出 taxonomy，记录理由\\n\\n## 近期任务\\n- [ ] 获取 GPU 资源（4× H100）— **阻塞项**\\n- [ ] Agent 消化 worker 调研结果 + 确认 7→3 映射 + 双 Transformer hook 方案\\n- [ ] Agent 准备 Phase 0 完整代码（激活 hook + 3 套分类器 + eval pipeline）\\n- [ ] GPU 到位后部署 + 数据收集 + Phase 0 训练 + GO/NO-GO\\n\\n## GPU 预算\\n- 需求：190 H100-hrs 总计\\n- 当前分配：**无**（待用户提供服务器）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D003 | 2026-05-15 | Phase 0 架构修正：层索引改为 Gemma 2B 的 18 层范围 + 排除 Language | — |\\n| D002 | 2026-05-15 | 采纳 Reviewer 4 条建议增强 Phase 0：+binary sanity check,  | — |\\n| D001 | 2026-05-15 | MVP 定义为 Phase 0 early-kill gate：验证 π₀ 内部激活能否分类 3 类 | — |\\n\\n\", \"total_chars\": 2591, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "4fe76251-826b-4a41-ad1f-ad52273c95f8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/ROADMAP.md\\\", \\\"content\\\": \\\"# meta_brain_lora_routing — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-15 10:44 UTC | 更新原因: Critical fix: π₀ 层索引修正 (18层 not 32层) + 排除 Language Instructions + 增加 Action Expert 探针\\\\n\\\\n## 核心方向\\\\nPerturbation-Adaptive LoRA Routing：在冻结的 VLA backbone (π₀, PaliGemma-Gemma 2B) 上，用轻量级 router 从内部激活诊断扰动类型，路由到对应专用 LoRA expert 修正。核心假设：扰动类型感知的专用路由 > 通用适配（参数效率 6M vs 114M）。详见 IDEA_BRIEF.md。\\\\n\\\\n## 目标会议\\\\nCoRL 2026 — Abstract DDL: 2026-05-26 (11天)，Paper DDL: 2026-05-29 (14天)\\\\n\\\\n## 当前进展\\\\n- 阶段：**MVP 验证**（Phase 0 early-kill gate）\\\\n- 实验：暂无\\\\n- 基础设施：**未配置**（无服务器、无 GPU）— 等用户提供\\\\n- Agent：正在调研 OpenPI + LIBERO-Plus（worker 已完成，结果待 Agent 消化）\\\\n- Reviewer 审查：2 轮（MVP 设计 WARNING + OpenPI 调研 WARNING/CRITICAL），已全部采纳\\\\n\\\\n## 架构关键参数（worker 调研确认）\\\\n- **π₀ backbone**: PaliGemma VLM (Gemma 2B LLM, 18 layers, 2048-dim) + Action Expert (18 layers, 1024-dim)\\\\n- **激活提取层**: PaliGemma {2,4,6,8,10,12,14,16} + Action Expert {2,6,10,14}（共 12 层）\\\\n- ⚠️ IDEA_BRIEF 原写 layers {4,8,12,16,20,24,28,32} 基于 32 层假设，**已修正**\\\\n\\\\n## MVP 验证方案（Phase 0 — 增强版 v2）\\\\n\\\\n**核心假设**: π₀ 内部激活编码了扰动类型信息，可被轻量级 probe 分类\\\\n\\\\n**扰动分类 taxonomy**:\\\\n- LIBERO-Plus 7 类中排除 Language Instructions（语言扰动不影响 visual token representation，不属于 LoRA 修正范围）\\\\n- 6 类覆盖：Camera, Light, Background, Noise, Robot, Layout\\\\n- 3-class 映射：Visual (Camera+Light+Background+Noise) / Spatial (Layout) / Physical (Robot)\\\\n- 同时跑 6-class 对照\\\\n\\\\n**实验设计**:\\\\n1. 搭建 π₀ + LIBERO-Plus 环境（OpenPI codebase）\\\\n2. 冻结 π₀ 在 6 类扰动下 rollout ~500 episodes\\\\n3. 记录 PaliGemma 8 层 + Action Expert 4 层的 pooled 激活（~0.95GB）\\\\n4. 训练 3 套分类器：3-class / 6-class / binary anomaly detection\\\\n5. Sweep: 3 pooling × layer subsets × 3 lr；对比 PaliGemma-only vs Expert-only vs 双 Transformer\\\\n\\\\n**报告要求**: overall accuracy + per-class F1 + confusion matrix + binary ROC-AUC + PaliGemma vs Expert 对比\\\\n\\\\n**Pass/Fail**: >70% 3-class + confusion matrix 无严重混淆 → GO；50-70% → 增强输入；<50% → Pivot\\\\n\\\\n## Reviewer 关注点\\\\n1. **Impact 3/5**: 目标 72-80% 低于 SOTA 82.1% → 参数效率差异化\\\\n2. **SAFE 类比不成立**: 已补 binary sanity check\\\\n3. **误路由风险**: 已补 confusion matrix + 后续 oracle routing ablation\\\\n4. **Language Instructions**: 排除出 taxonomy，记录理由\\\\n\\\\n## 近期任务\\\\n- [ ] 获取 GPU 资源（4× H100）— **阻塞项**\\\\n- [ ] Agent 消化 worker 调研结果 + 确认 7→3 映射 + 双 Transformer hook 方案\\\\n- [ ] Agent 准备 Phase 0 完整代码（激活 hook + 3 套分类器 + eval pipeline）\\\\n- [ ] GPU 到位后部署 + 数据收集 + Phase 0 训练 + GO/NO-GO\\\\n\\\\n## GPU 预算\\\\n- 需求：190 H100-hrs 总计\\\\n- 当前分配：**无**（待用户提供服务器）\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D003 | 2026-05-15 | Phase 0 架构修正：层索引改为 Gemma 2B 的 18 层范围 + 排除 Language | — |\\\\n| D002 | 2026-05-15 | 采纳 Reviewer 4 条建议增强 Phase 0：+binary sanity check,  | — |\\\\n| D001 | 2026-05-15 | MVP 定义为 Phase 0 early-kill gate：验证 π₀ 内部激活能否分类 3 类 | — |\\\\n\\\\n\\\", \\\"total_chars\\\": 2591, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/ROADMAP.md\", \"content\": \"# meta_brain_lora_routing — Research Dashboard\\n\\n> 最后更新: 2026-05-15 10:44 UTC | 更新原因: Critical fix: π₀ 层索引修正 (18层 not 32层) + 排除 Language Instructions + 增加 Action Expert 探针\\n\\n## 核心方向\\nPerturbation-Adaptive LoRA Routing：在冻结的 VLA backbone (π₀, PaliGemma-Gemma 2B) 上，用轻量级 router 从内部激活诊断扰动类型，路由到对应专用 LoRA expert 修正。核心假设：扰动类型感知的专用路由 > 通用适配（参数效率 6M vs 114M）。详见 IDEA_BRIEF.md。\\n\\n## 目标会议\\nCoRL 2026 — Abstract DDL: 2026-05-26 (11天)，Paper DDL: 2026-05-29 (14天)\\n\\n## 当前进展\\n- 阶段：**MVP 验证**（Phase 0 early-kill gate）\\n- 实验：暂无\\n- 基础设施：**未配置**（无服务器、无 GPU）— 等用户提供\\n- Agent：正在调研 OpenPI + LIBERO-Plus（worker 已完成，结果待 Agent 消化）\\n- Reviewer 审查：2 轮（MVP 设计 WARNING + OpenPI 调研 WARNING/CRITICAL），已全部采纳\\n\\n## 架构关键参数（worker 调研确认）\\n- **π₀ backbone**: PaliGemma VLM (Gemma 2B LLM, 18 layers, 2048-dim) + Action Expert (18 layers, 1024-dim)\\n- **激活提取层**: PaliGemma {2,4,6,8,10,12,14,16} + Action Expert {2,6,10,14}（共 12 层）\\n- ⚠️ IDEA_BRIEF 原写 layers {4,8,12,16,20,24,28,32} 基于 32 层假设，**已修正**\\n\\n## MVP 验证方案（Phase 0 — 增强版 v2）\\n\\n**核心假设**: π₀ 内部激活编码了扰动类型信息，可被轻量级 probe 分类\\n\\n**扰动分类 taxonomy**:\\n- LIBERO-Plus 7 类中排除 Language Instructions（语言扰动不影响 visual token representation，不属于 LoRA 修正范围）\\n- 6 类覆盖：Camera, Light, Background, Noise, Robot, Layout\\n- 3-class 映射：Visual (Camera+Light+Background+Noise) / Spatial (Layout) / Physical (Robot)\\n- 同时跑 6-class 对照\\n\\n**实验设计**:\\n1. 搭建 π₀ + LIBERO-Plus 环境（OpenPI codebase）\\n2. 冻结 π₀ 在 6 类扰动下 rollout ~500 episodes\\n3. 记录 PaliGemma 8 层 + Action Expert 4 层的 pooled 激活（~0.95GB）\\n4. 训练 3 套分类器：3-class / 6-class / binary anomaly detection\\n5. Sweep: 3 pooling × layer subsets × 3 lr；对比 PaliGemma-only vs Expert-only vs 双 Transformer\\n\\n**报告要求**: overall accuracy + per-class F1 + confusion matrix + binary ROC-AUC + PaliGemma vs Expert 对比\\n\\n**Pass/Fail**: >70% 3-class + confusion matrix 无严重混淆 → GO；50-70% → 增强输入；<50% → Pivot\\n\\n## Reviewer 关注点\\n1. **Impact 3/5**: 目标 72-80% 低于 SOTA 82.1% → 参数效率差异化\\n2. **SAFE 类比不成立**: 已补 binary sanity check\\n3. **误路由风险**: 已补 confusion matrix + 后续 oracle routing ablation\\n4. **Language Instructions**: 排除出 taxonomy，记录理由\\n\\n## 近期任务\\n- [ ] 获取 GPU 资源（4× H100）— **阻塞项**\\n- [ ] Agent 消化 worker 调研结果 + 确认 7→3 映射 + 双 Transformer hook 方案\\n- [ ] Agent 准备 Phase 0 完整代码（激活 hook + 3 套分类器 + eval pipeline）\\n- [ ] GPU 到位后部署 + 数据收集 + Phase 0 训练 + GO/NO-GO\\n\\n## GPU 预算\\n- 需求：190 H100-hrs 总计\\n- 当前分配：**无**（待用户提供服务器）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D003 | 2026-05-15 | Phase 0 架构修正：层索引改为 Gemma 2B 的 18 层范围 + 排除 Language | — |\\n| D002 | 2026-05-15 | 采纳 Reviewer 4 条建议增强 Phase 0：+binary sanity check,  | — |\\n| D001 | 2026-05-15 | MVP 定义为 Phase 0 early-kill gate：验证 π₀ 内部激活能否分类 3 类 | — |\\n\\n\", \"total_chars\": 2591, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01U8hmF8wSa1BtRcyANfN9iw`</summary>

```json
{
  "project": "meta_brain_lora_routing",
  "file": "ideas.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "9d6d1098-06ab-4c12-8840-f0d4ac30f4dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JCvNB6GpfQtHCvxeWiFZMF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 912,
      "cache_read_input_tokens": 24205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 912
      },
      "output_tokens": 41,
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

_source line 11 · 2026-05-15T11:00:47.553Z_

<details><summary>↩ Tool result · `toolu_01U8hmF8wSa1BtRcyANfN9iw`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'meta_brain_lora_routing'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "b9a0d97a-8e0f-43d0-b206-91a373b873dc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"No ideas.md found for 'meta_brain_lora_routing'.\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'meta_brain_lora_routing'.\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01A31fb8xpRnPyKMY2y15JD1`</summary>

```json
{
  "project": "meta_brain_lora_routing",
  "file": "memory.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "60191755-d4e0-4523-b518-a305d3eaedc9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JCvNB6GpfQtHCvxeWiFZMF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 912,
      "cache_read_input_tokens": 24205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 912
      },
      "output_tokens": 41,
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

_source line 13 · 2026-05-15T11:00:48.488Z_

<details><summary>↩ Tool result · `toolu_01A31fb8xpRnPyKMY2y15JD1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/memory.md\", \"content\": \"# OpenPI Research Summary (2026-05-15)\\n\\n## Key Finding: π₀ Architecture\\n- Backbone: PaliGemma (SigLIP So400m/14 + Gemma 2B) + Action Expert (Gemma 300M)\\n- Total: ~3.3B params, **18 transformer layers** (NOT 32)\\n- Gemma 2B: width=2048, depth=18, 8 heads, MQA\\n- Action Expert: width=1024, depth=18, 8 heads\\n- Flow matching (10-step Euler) for action generation\\n\\n## LIBERO Integration\\n- Full first-class support in OpenPI\\n- Evaluation: `examples/libero/main.py` via WebSocket policy server\\n- π₀.₅ LIBERO checkpoint: 96.85% avg success\\n- LIBERO-Plus perturbed eval: drop-in replacement for LIBERO lib\\n\\n## LoRA Support\\n- JAX: native LoRA (rank=16/32, attn+ffn targets)\\n- PyTorch: NOT official, but Issue #842 has working implementation (26.5M params, 96.95% on LIBERO)\\n- LeRobot: no native LoRA, can extend with PEFT\\n\\n## Activation Extraction\\n- PyTorch hook path: `model.paligemma_with_expert.paligemma.language_model.layers[i]` (i=0..17)\\n- Action expert: `model.paligemma_with_expert.gemma_expert.model.layers[i]`\\n- Recommended layers: {2,4,6,8,10,12,14,16} (adjust from original {4,8,12,16,20,24,28,32})\\n\\n## Storage Estimates (500 episodes)\\n- Full seq fp32: 1.7 TB | Action tokens fp16: 48 GB | Pooled fp16: 0.95 GB\\n\\n## Full report: `artifacts/openpi_research_report.md`\\n\", \"total_chars\": 1268, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "73a0f686-d100-40d0-b2c2-c962f16774fb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/memory.md\\\", \\\"content\\\": \\\"# OpenPI Research Summary (2026-05-15)\\\\n\\\\n## Key Finding: π₀ Architecture\\\\n- Backbone: PaliGemma (SigLIP So400m/14 + Gemma 2B) + Action Expert (Gemma 300M)\\\\n- Total: ~3.3B params, **18 transformer layers** (NOT 32)\\\\n- Gemma 2B: width=2048, depth=18, 8 heads, MQA\\\\n- Action Expert: width=1024, depth=18, 8 heads\\\\n- Flow matching (10-step Euler) for action generation\\\\n\\\\n## LIBERO Integration\\\\n- Full first-class support in OpenPI\\\\n- Evaluation: `examples/libero/main.py` via WebSocket policy server\\\\n- π₀.₅ LIBERO checkpoint: 96.85% avg success\\\\n- LIBERO-Plus perturbed eval: drop-in replacement for LIBERO lib\\\\n\\\\n## LoRA Support\\\\n- JAX: native LoRA (rank=16/32, attn+ffn targets)\\\\n- PyTorch: NOT official, but Issue #842 has working implementation (26.5M params, 96.95% on LIBERO)\\\\n- LeRobot: no native LoRA, can extend with PEFT\\\\n\\\\n## Activation Extraction\\\\n- PyTorch hook path: `model.paligemma_with_expert.paligemma.language_model.layers[i]` (i=0..17)\\\\n- Action expert: `model.paligemma_with_expert.gemma_expert.model.layers[i]`\\\\n- Recommended layers: {2,4,6,8,10,12,14,16} (adjust from original {4,8,12,16,20,24,28,32})\\\\n\\\\n## Storage Estimates (500 episodes)\\\\n- Full seq fp32: 1.7 TB | Action tokens fp16: 48 GB | Pooled fp16: 0.95 GB\\\\n\\\\n## Full report: `artifacts/openpi_research_report.md`\\\\n\\\", \\\"total_chars\\\": 1268, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/memory.md\", \"content\": \"# OpenPI Research Summary (2026-05-15)\\n\\n## Key Finding: π₀ Architecture\\n- Backbone: PaliGemma (SigLIP So400m/14 + Gemma 2B) + Action Expert (Gemma 300M)\\n- Total: ~3.3B params, **18 transformer layers** (NOT 32)\\n- Gemma 2B: width=2048, depth=18, 8 heads, MQA\\n- Action Expert: width=1024, depth=18, 8 heads\\n- Flow matching (10-step Euler) for action generation\\n\\n## LIBERO Integration\\n- Full first-class support in OpenPI\\n- Evaluation: `examples/libero/main.py` via WebSocket policy server\\n- π₀.₅ LIBERO checkpoint: 96.85% avg success\\n- LIBERO-Plus perturbed eval: drop-in replacement for LIBERO lib\\n\\n## LoRA Support\\n- JAX: native LoRA (rank=16/32, attn+ffn targets)\\n- PyTorch: NOT official, but Issue #842 has working implementation (26.5M params, 96.95% on LIBERO)\\n- LeRobot: no native LoRA, can extend with PEFT\\n\\n## Activation Extraction\\n- PyTorch hook path: `model.paligemma_with_expert.paligemma.language_model.layers[i]` (i=0..17)\\n- Action expert: `model.paligemma_with_expert.gemma_expert.model.layers[i]`\\n- Recommended layers: {2,4,6,8,10,12,14,16} (adjust from original {4,8,12,16,20,24,28,32})\\n\\n## Storage Estimates (500 episodes)\\n- Full seq fp32: 1.7 TB | Action tokens fp16: 48 GB | Pooled fp16: 0.95 GB\\n\\n## Full report: `artifacts/openpi_research_report.md`\\n\", \"total_chars\": 1268, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01AUKrSThaUWW8jrnkazoDRs`</summary>

```json
{
  "project": "meta_brain_lora_routing",
  "file": "decisions.yaml",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "cbc9633a-723a-4c4a-a929-f335d0d8f930",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JCvNB6GpfQtHCvxeWiFZMF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 912,
      "cache_read_input_tokens": 24205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 912
      },
      "output_tokens": 41,
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

_source line 15 · 2026-05-15T11:00:49.040Z_

<details><summary>↩ Tool result · `toolu_01AUKrSThaUWW8jrnkazoDRs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/decisions.yaml\", \"content\": \"_next_id: 4\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 10:32 UTC\\n  summary: MVP 定义为 Phase 0 early-kill gate：验证 π₀ 内部激活能否分类 3 类扰动（>70% 准确率）\\n  rationale: IDEA_BRIEF 提出的 Phase 0 方案是正确的 MVP 选择：(1) 整个方法论依赖\\\"扰动类型可从 VLA 内部激活诊断\\\"这一前提，若此假设不成立，后续所有工作（LoRA\\n    bank、routing、CM）全部无效；(2) 仅需 ~20 H100-hrs，4 天内可得到 GO/NO-GO；(3) SAFE (NeurIPS 2025)\\n    用相同架构做 binary failure detection 达到 78% ROC-AUC，3-class 粗粒度分类理应可行但需验证；(4) 有明确的\\n    fallback：50-70% 增强输入，<50% pivot 到 universal LoRA+CM。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 10:36 UTC\\n  summary: 采纳 Reviewer 4 条建议增强 Phase 0：+binary sanity check, +6-class 对照, +confusion\\n    matrix, +明确 7→3 映射\\n  rationale: Reviewer 指出：(1) SAFE binary detection 不能类比 3-class classification（anomaly\\n    detection 是更弱假设），加 binary 作 sanity check 成本近零但能区分\\\"激活提取有问题\\\"vs\\\"假设不成立\\\"；(2) 7→3 映射未定义会导致实验不可复现且映射选择影响难度；(3)\\n    70% accuracy 不够——30% 误路由可能 worse than no routing，confusion matrix 能暴露具体风险。所有增强不影响\\n    Phase 0 核心设计和资源估算。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 10:44 UTC\\n  summary: Phase 0 架构修正：层索引改为 Gemma 2B 的 18 层范围 + 排除 Language Instructions + 增加 Action\\n    Expert 探针\\n  rationale: Worker 调研确认 π₀ 用 PaliGemma (Gemma 2B, 18 层)，非 32 层模型。IDEA_BRIEF 的 layers\\n    {4,8,12,16,20,24,28,32} 中后 4 个不存在，修正为 PaliGemma {2,4,6,8,10,12,14,16} + Action\\n    Expert {2,6,10,14}。排除 Language Instructions：Meta-Brain 的 LoRA 修正作用于 visual/action\\n    token representation，语言扰动（指令改写）影响的是文本输入而非表征空间，不在修正范围内。增加 Action Expert 探针：π₀ 有独立的\\n    Action Expert Transformer (1024-dim, 18 layers)，physical perturbation 可能在 action\\n    token 中有更强信号，低成本高信息量。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n\", \"total_chars\": 1653, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "72cea960-6f53-464b-be93-e03fe2a11fd3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/decisions.yaml\\\", \\\"content\\\": \\\"_next_id: 4\\\\ndecisions:\\\\n- id: D001\\\\n  date: 2026-05-15 10:32 UTC\\\\n  summary: MVP 定义为 Phase 0 early-kill gate：验证 π₀ 内部激活能否分类 3 类扰动（>70% 准确率）\\\\n  rationale: IDEA_BRIEF 提出的 Phase 0 方案是正确的 MVP 选择：(1) 整个方法论依赖\\\\\\\"扰动类型可从 VLA 内部激活诊断\\\\\\\"这一前提，若此假设不成立，后续所有工作（LoRA\\\\n    bank、routing、CM）全部无效；(2) 仅需 ~20 H100-hrs，4 天内可得到 GO/NO-GO；(3) SAFE (NeurIPS 2025)\\\\n    用相同架构做 binary failure detection 达到 78% ROC-AUC，3-class 粗粒度分类理应可行但需验证；(4) 有明确的\\\\n    fallback：50-70% 增强输入，<50% pivot 到 universal LoRA+CM。\\\\n  related_experiments: []\\\\n  depends_on: []\\\\n- id: D002\\\\n  date: 2026-05-15 10:36 UTC\\\\n  summary: 采纳 Reviewer 4 条建议增强 Phase 0：+binary sanity check, +6-class 对照, +confusion\\\\n    matrix, +明确 7→3 映射\\\\n  rationale: Reviewer 指出：(1) SAFE binary detection 不能类比 3-class classification（anomaly\\\\n    detection 是更弱假设），加 binary 作 sanity check 成本近零但能区分\\\\\\\"激活提取有问题\\\\\\\"vs\\\\\\\"假设不成立\\\\\\\"；(2) 7→3 映射未定义会导致实验不可复现且映射选择影响难度；(3)\\\\n    70% accuracy 不够——30% 误路由可能 worse than no routing，confusion matrix 能暴露具体风险。所有增强不影响\\\\n    Phase 0 核心设计和资源估算。\\\\n  related_experiments: []\\\\n  depends_on:\\\\n  - D001\\\\n- id: D003\\\\n  date: 2026-05-15 10:44 UTC\\\\n  summary: Phase 0 架构修正：层索引改为 Gemma 2B 的 18 层范围 + 排除 Language Instructions + 增加 Action\\\\n    Expert 探针\\\\n  rationale: Worker 调研确认 π₀ 用 PaliGemma (Gemma 2B, 18 层)，非 32 层模型。IDEA_BRIEF 的 layers\\\\n    {4,8,12,16,20,24,28,32} 中后 4 个不存在，修正为 PaliGemma {2,4,6,8,10,12,14,16} + Action\\\\n    Expert {2,6,10,14}。排除 Language Instructions：Meta-Brain 的 LoRA 修正作用于 visual/action\\\\n    token representation，语言扰动（指令改写）影响的是文本输入而非表征空间，不在修正范围内。增加 Action Expert 探针：π₀ 有独立的\\\\n    Action Expert Transformer (1024-dim, 18 layers)，physical perturbation 可能在 action\\\\n    token 中有更强信号，低成本高信息量。\\\\n  related_experiments: []\\\\n  depends_on:\\\\n  - D002\\\\n\\\", \\\"total_chars\\\": 1653, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/decisions.yaml\", \"content\": \"_next_id: 4\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 10:32 UTC\\n  summary: MVP 定义为 Phase 0 early-kill gate：验证 π₀ 内部激活能否分类 3 类扰动（>70% 准确率）\\n  rationale: IDEA_BRIEF 提出的 Phase 0 方案是正确的 MVP 选择：(1) 整个方法论依赖\\\"扰动类型可从 VLA 内部激活诊断\\\"这一前提，若此假设不成立，后续所有工作（LoRA\\n    bank、routing、CM）全部无效；(2) 仅需 ~20 H100-hrs，4 天内可得到 GO/NO-GO；(3) SAFE (NeurIPS 2025)\\n    用相同架构做 binary failure detection 达到 78% ROC-AUC，3-class 粗粒度分类理应可行但需验证；(4) 有明确的\\n    fallback：50-70% 增强输入，<50% pivot 到 universal LoRA+CM。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 10:36 UTC\\n  summary: 采纳 Reviewer 4 条建议增强 Phase 0：+binary sanity check, +6-class 对照, +confusion\\n    matrix, +明确 7→3 映射\\n  rationale: Reviewer 指出：(1) SAFE binary detection 不能类比 3-class classification（anomaly\\n    detection 是更弱假设），加 binary 作 sanity check 成本近零但能区分\\\"激活提取有问题\\\"vs\\\"假设不成立\\\"；(2) 7→3 映射未定义会导致实验不可复现且映射选择影响难度；(3)\\n    70% accuracy 不够——30% 误路由可能 worse than no routing，confusion matrix 能暴露具体风险。所有增强不影响\\n    Phase 0 核心设计和资源估算。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 10:44 UTC\\n  summary: Phase 0 架构修正：层索引改为 Gemma 2B 的 18 层范围 + 排除 Language Instructions + 增加 Action\\n    Expert 探针\\n  rationale: Worker 调研确认 π₀ 用 PaliGemma (Gemma 2B, 18 层)，非 32 层模型。IDEA_BRIEF 的 layers\\n    {4,8,12,16,20,24,28,32} 中后 4 个不存在，修正为 PaliGemma {2,4,6,8,10,12,14,16} + Action\\n    Expert {2,6,10,14}。排除 Language Instructions：Meta-Brain 的 LoRA 修正作用于 visual/action\\n    token representation，语言扰动（指令改写）影响的是文本输入而非表征空间，不在修正范围内。增加 Action Expert 探针：π₀ 有独立的\\n    Action Expert Transformer (1024-dim, 18 layers)，physical perturbation 可能在 action\\n    token 中有更强信号，低成本高信息量。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n\", \"total_chars\": 1653, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check for the IDEA_BRIEF and the OpenPI research report for more context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "92e789dc-ba44-453d-ab05-f884b2f930bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017op4oDGNEvbV4M122LMnUQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3986,
      "cache_read_input_tokens": 25117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3986
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

_source line 17_

<details open><summary>🔧 Tool call — Glob · `toolu_01TeeTBS8aTHjT4Y3wJ6fpeU`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "a1719549-03d6-462f-a15d-10a5980ce3b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017op4oDGNEvbV4M122LMnUQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3986,
      "cache_read_input_tokens": 25117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3986
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

_source line 18 · 2026-05-15T11:00:52.771Z_

<details><summary>↩ Tool result · `toolu_01TeeTBS8aTHjT4Y3wJ6fpeU`</summary>

```text
artifacts/openpi_research_report.md
artifacts/phase0/configs.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "991da839-f780-45c4-a3dd-e76eb0029d85",
  "tool_use_result": {
    "filenames": [
      "artifacts/openpi_research_report.md",
      "artifacts/phase0/configs.py"
    ],
    "durationMs": 14,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Glob · `toolu_01CVQ5ASmwVLJhjNpuoVuxMV`</summary>

```json
{
  "pattern": "**/IDEA_BRIEF*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "9f753f8a-edf3-49b9-bd98-636751f9e3e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017op4oDGNEvbV4M122LMnUQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3986,
      "cache_read_input_tokens": 25117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3986
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

_source line 20 · 2026-05-15T11:00:53.470Z_

<details><summary>↩ Tool result · `toolu_01CVQ5ASmwVLJhjNpuoVuxMV`</summary>

```text
docs/IDEA_BRIEF.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "51450e61-606c-4757-9127-10275589263a",
  "tool_use_result": {
    "filenames": [
      "docs/IDEA_BRIEF.md"
    ],
    "durationMs": 5,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_013dBKmcjz5qTeVcgtD2NEcS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "35f6ec54-e2f9-40c3-8472-3c59de4b691f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGhEWQQmBS5AojnDVMs4gK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 315,
      "cache_read_input_tokens": 29103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 315
      },
      "output_tokens": 70,
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

_source line 22 · 2026-05-15T11:00:56.742Z_

<details><summary>↩ Tool result · `toolu_013dBKmcjz5qTeVcgtD2NEcS`</summary>

```text
1	# Idea Brief: Meta-Brain: Perturbation-Adaptive LoRA Routing for Robust Vision-Language-Action Models
2	
3	
4	- **Idea ID**: `idea_007`
5	- **Created**: 2026-05-15
6	- **Approved**: 2026-05-15
7	- **Source**: foreign:be-idea-gen-0509-15
8	- **Level**: top-tier
9	
10	## Seed Topic
11	
12	按照以下方向，生成1-2个优质idea，保质不求量：Seed 3: Meta-Brain — LLM Role-Switching as Adaptive Robustness Controller for VLA
13	Target: CoRL 2026 (Austin, Nov 9–12, 2026). Abstract deadline 2026-05-26 (12 days from today 2026-05-14); paper deadline 2026-05-29 (15 days).
14	Direction: LLM-as-Meta-Brain for VLA robustness — an architecture where a frozen LLM dynamically switches between specialized roles (perception enhancement, logic decomposition, anomaly intervention) and feeds unified modified visual tokens back to a VLA backbone, enabling robust operation across diverse perturbation scenarios without retraining the VLA. The core motivation is that different robustness failures require qualitatively different interventions: visual noise needs perceptual re-grounding, ambiguous instructions need task decomposition, and execution uncertainty needs reflective error correction. Rather than training a single monolithic robust VLA, we leverage the LLM's pre-existing world knowledge and reasoning capabilities as an external "meta-brain" that diagnoses the current failure mode and provides targeted representational guidance. The key architectural innovation is a Unified Representation Interface: regardless of which role the LLM assumes, it outputs through a shared Adapter into a fixed-dimensional token modification that directly reshapes the VLA's visual tokens — this means the VLA backbone sees the same token format but with role-specific semantic content baked in. This avoids the fragility of language-mediated VLA guidance (which breaks under paraphrasing) and instead operates in continuous representation space.
15	Recent landscape (do not duplicate): SOMA: Strategic Orchestration and Memory-Augmented System for Vision-Language-Action Model Robustness via In-Context Adaptation
16	CoRAL: Contact-Rich Adaptive LLM-Based Control for Robotic Manipulation
17	VLA-Pilot: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion
18	Observing and Controlling Features in Vision-Language-Action Models
19	ON ROBUSTNESS OF VISION-LANGUAGE-ACTION MODEL AGAINST MULTI-MODAL PERTURBATIONS
20	STRONG-VLA: Decoupled Robustness Learning for Vision-Language-Action Models under Multimodal Perturbations
21	ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models
22	Contribution type: METHOD ONLY. A three-component architecture: (1) Role Router — a lightweight classifier on top of the VLA's current state embedding that detects the perturbation regime: high visual entropy → perception mode, high instruction ambiguity → logic mode, high action uncertainty → intervention mode. Trained with meta-learning across perturbation types. (2) Role-Conditioned Adapter — a shared Adapter between the frozen LLM and VLA that outputs one of three representation modalities through the same interface: (a) Hybrid Semantic Tokens — role-conditioned embedding vectors that reshape visual tokens to emphasize task-relevant features; (b) Function Prefix — a role embedding prepended to the modified tokens that biases VLA attention heads toward the appropriate processing mode; (c) Attention Mask — a spatial weight matrix that gates visual token importance (suppress distractors, enhance depth features, highlight skill-relevant objects). (3) Dynamic Skill Library — when the meta-brain's intervention produces a novel solution pattern, it is distilled into a reusable skill embedding stored persistently; future encounters of similar perturbations route directly to the skill without full LLM inference. Training: two-phase — Phase 1 trains the Adapter with meta-learning across role-switching datasets; Phase 2 trains end-to-end with the VLA backbone frozen, optimizing only the Router + Adapter for action prediction under perturbation.
23	EVAL PROTOCOL — IMPORTANT:
24	TRAIN on standard LIBERO suites (Object/Spatial/Goal/Long/90).
25	EVALUATE on existing LIBERO-PLUS / LIBERO-PRO style perturbation benchmarks (and similar community-released robustness benchmark series). DO NOT spend time constructing your own robustness benchmark — use existing perturbation suites and route the budget into the method.
26	Report robustness gap (Δ between nominal LIBERO success and perturbed-suite success) AND nominal preservation (must not regress on base LIBERO).
27	Additionally report: per-perturbation-type breakdown (visual/language/action noise) with role activation frequency, latency overhead of meta-brain inference, ablation of individual roles and combined system.
28	Experiments can be extended to CALVIN or RLBench perturbation variants to verify cross-benchmark robustness and role generalization.
29	SIM-ONLY MITIGATION: Robustness eval in sim is well-accepted at CoRL — established LIBERO-PLUS / LIBERO-PRO style suites are a recognized sim-only pattern. The meta-brain architecture operates on representations, not physical hardware, making sim evaluation methodologically sufficient.
30	HARD CONSTRAINTS:
31	Compute: ≤200 H100-hours total. LLM is frozen (e.g., Qwen-2.5-7B or LLaMA-3-8B); VLA backbone is frozen (OpenVLA/SmolVLA/OpenPi/π0 checkpoint). Only train Router (~2M params) + Adapter (~15M params). Show the math: Adapter training ≈ 50 H100-hrs, Router meta-learning ≈ 30 H100-hrs, evaluation ≈ 40 H100-hrs.
32	Time: ≤20 days. Build on OpenVLA, OpenPi and other proper codebases, LeRobot, HF Transformers. LLM integration via HuggingFace model loading.
33	Eval datasets: LIBERO base (training/nominal eval) + LIBERO-PLUS / LIBERO-PRO and similar existing perturbation suites (perturbed eval). No custom benchmark construction.
34	Look for: meta-learning for role router that generalizes to unseen perturbation types, unified adapter architecture that maps heterogeneous LLM guidance into a common token-modification interface, attention masking as a differentiable robustness mechanism, skill library as amortized robustness (one-time LLM cost → reusable embedding), theoretical connections between role diversity and minimax robustness over perturbation sets. Avoid: language-only LLM guidance that is itself fragile to paraphrasing, requiring LLM inference at every VLA timestep (must amortize via skill caching), plain ensembling of multiple VLAs, custom robustness benchmark construction, approaches requiring real-robot data for the meta-brain training.
35	Tag: direction=robust_vla, contribution_type=method, sub_direction=meta_brain_role_switching, target_venues=["CoRL 2026"].
36	
37	## Core Problem
38	
39	Vision-Language-Action (VLA) models achieve >90% success on standard LIBERO benchmarks but suffer catastrophic performance drops under perturbation: π₀ falls from >90% nominal to 53.6% average on LIBERO-Plus, with camera perturbations at 13.8% and robot initial-state perturbations at 6.0%. This brittleness stems from VLAs memorizing fixed vision-action mappings rather than developing genuine environmental understanding. Critically, different perturbation types disrupt different processing stages: visual perturbations (camera, lighting) corrupt early visual token representations, spatial perturbations (object rearrangement) invalidate learned action trajectories, and physical perturbations (object mass, friction) break force-compliance assumptions. Current robustness methods either address a single perturbation modality (FTM for visual, AFI for spatial, AnyCamVLA for camera viewpoint) or apply uniform correction across all perturbation types (RobustVLA's adversarial training, VLA-GSE's per-token capacity routing), leaving a fundamental question unanswered: does perturbation-type-aware diagnostic routing outperform one-size-fits-all adaptation?
40	
41	## Opportunity / Why Now
42	
43	Four concurrent lines of evidence from 2025-2026 converge to make perturbation-adaptive internal correction newly feasible: (1) SAFE (NeurIPS 2025) demonstrates that VLA intermediate activations encode rich, task-generic signals about execution state — a lightweight MLP on frozen features achieves SOTA failure detection across unseen tasks with <1% overhead, proving that perturbation-relevant information is extractable from VLA internals; (2) Linear probing of OpenVLA (Geier et al., 2502.04558) shows >0.90 accuracy for spatial object states and relations across layers 1-32 of the LLM backbone, establishing that spatial information sufficient for correction is linearly accessible; (3) Feature steering on π₀.₅ and OpenVLA (Buurmeijer et al., 2603.05487) demonstrates that minimal linear interventions on internal representations can reliably steer robot behavior with ~100% constraint satisfaction while preserving closed-loop task performance — proving that the representations are not just readable but controllable; (4) VLA-GSE (2605.06175) achieves 81.2% on LIBERO-Plus with spectral MoE routing using 114M trainable parameters on Qwen3-VL-4B, demonstrating that expert routing on frozen VLA backbones is highly effective — but its per-token capacity routing is perturbation-agnostic, leaving room for perturbation-diagnostic routing as an orthogonal design dimension. Together, these findings establish that VLA internals contain sufficient perturbation-diagnostic information AND that lightweight internal interventions can correct behavior without disrupting the frozen backbone's capabilities.
44	
45	## Landscape (SOTA & Limitations)
46	
47	The VLA robustness landscape in early 2026 features complementary but incomplete solutions across seven categories:
48	
49	**Single-modality correction:** FTM/FLA (Li et al., 2512.02902) achieves 87-91% viewpoint recovery via visual token modulation with only 4K-4.7M parameters — highly efficient for visual perturbations but architecturally limited to recalibrating ViT outputs, with no mechanism for spatial or physical corrections. AFI (Chen et al., 2512.07472) achieves +20.2% on LIBERO-PRO through external 3D Spatial Affordance Fields that detect 'memory traps' via proprioception and propose affordance-driven waypoints — effective for spatial perturbations but requires an external geometric module and does not address visual or physical perturbations. AnyCamVLA (Heo et al., 2603.05868) provides zero-shot camera adaptation via feed-forward novel view synthesis, achieving 94.5% average success under camera perturbations by virtually transforming test-time observations to match training camera configuration — a plug-and-play visual-specific solution requiring no fine-tuning but limited to camera viewpoint changes.
50	
51	**Multi-modal but uniform correction:** RobustVLA (ICLR 2026, 2510.00037) formulates multi-perturbation robustness as a multi-armed bandit problem, achieving +12.6% on π₀ across 17 perturbation types. However, it applies a single adversarial training strategy uniformly, potentially underperforming on perturbations that require qualitatively different corrections.
52	
53	**Capacity-based expert routing (perturbation-agnostic):** VLA-GSE (2605.06175) decomposes frozen VLA weights via SVD into generalized (shared) and specialized (routed) experts, achieving 81.2% on LIBERO-Plus with 114M trainable parameters (2.51% of model) on Qwen3-VL-4B. VLA-GSE uses top-2 per-token gating across 7 specialized + 1 generalized expert per block for capacity allocation. This is the current strongest parameter-efficient method on LIBERO-Plus but routes by input-dependent capacity needs, not by perturbation type — the same routing configuration handles camera perturbations (64.4%) and layout perturbations (82.6%) without perturbation-type awareness. Importantly, VLA-GSE's standard LoRA baseline on the same Qwen3-VL-4B backbone achieves 69.2%, providing a controlled reference for the value of routing (+12.0% over LoRA).
54	
55	**Capacity-based LoRA adaptation:** LoRA-SP (2603.07404) adapts LoRA rank per layer and per input on π₀ and SmolVLA via an SVD-style parameterization with a small router whose nonnegative scores act as singular values over a shared vector bank. The active rank set is selected by an energy threshold on cumulative squared scores, discovering that vision towers require the highest ranks while language layers remain low and stable. On real-robot manipulation tasks, LoRA-SP matches or exceeds full fine-tuning with far fewer trainable parameters and improves multi-task success by up to 31.6% over standard LoRA. LoRA-SP adapts HOW MUCH LoRA capacity to allocate (adaptive rank); Meta-Brain adapts WHAT TYPE of correction to apply (perturbation-specific experts). These are orthogonal dimensions that could be composed — adaptive rank within each perturbation-specific expert — representing a natural extension.
56	
57	**Task-based LoRA routing (not perturbation-based):** CORAL (2603.09298) freezes the VLA backbone and attaches one LoRA expert per task, with a language-based manager routing instructions to experts. MoIRA (2507.01843) routes LoRA experts on π₀/GR00T-N1 using text-based similarity for task specialization. Both achieve strong multi-task performance but route by task identity/instruction — they cannot distinguish or adapt to different perturbation types within the same task.
58	
59	**Spatial-aware VLA architectures:** SpatialVLA (2501.15830) injects 3D position encodings into VLA input, achieving 88.2% on LIBERO-Spatial; Spatial Forcing (ICLR 2026, 2510.12276) aligns intermediate VLA representations with 3D foundation model features, achieving 98.5% on standard LIBERO and 3.8× training speedup — both enhance spatial understanding at training time but are complementary to, not competitive with, post-hoc perturbation correction on frozen backbones. CorridorVLA (2604.21241) uses explicit spatial anchor constraints to guide action generation; its GR00T-Corr variant achieves 83.21% on the LIBERO-Plus dataset, though reported by task category (Long/Goal/Object/Spatial) rather than by perturbation type (Camera/Robot/Light/Background/Noise/Layout), making direct per-perturbation comparison with VLA-GSE or Meta-Brain's target metrics not straightforward. CorridorVLA demonstrates that spatial corrections at the action-planning level via explicit geometric constraints are feasible and effective.
60	
61	**Test-time adaptation:** PDF (2604.18107) achieves +7.4% on LIBERO via test-time perturbation learning with delayed feedback — a lightweight perturbation head adjusts action logits using REINFORCE-style optimization guided by post-action observations, requiring no fine-tuning. PDF and Meta-Brain are complementary: training-time LoRA routing (Meta-Brain) for strong per-perturbation-type correction + test-time adaptation (PDF) for novel perturbation instances.
62	
63	**VLA internal analysis:** SAFE (NeurIPS 2025, 2506.09937) probes VLA final-layer activations for binary failure detection using a 2-layer MLP (hidden dim 256, 2.3M params), achieving 78.0% ROC-AUC on unseen tasks. Probing work (2502.04558) extracts symbolic spatial states. Feature steering (2603.05487) demonstrates behavioral control through linear interventions on end-effector position and gripper state, achieving ~100% constraint satisfaction. These works establish feasibility but stop at detection/analysis — none close the loop from perturbation diagnosis to targeted correction.
64	
65	**Gap:** No existing method combines (a) perturbation-type detection from VLA internals with (b) type-specific corrective adaptation. VLA-GSE routes by input capacity (perturbation-agnostic); LoRA-SP adapts rank per layer/input (capacity-agnostic to perturbation type); MoIRA/CORAL route by task instruction; PDF adapts at test-time without perturbation classification. Meta-Brain uniquely routes corrective LoRA experts by diagnosed perturbation type, testing the hypothesis that perturbation-aware specialization achieves comparable robustness gains at dramatically fewer trainable parameters through targeted correction rather than capacity expansion.
66	
67	## Proposed Approach
68	
69	**Meta-Brain** is a modular correction framework for frozen VLA backbones (π₀, π₀-FAST) comprising four components. The design departs from the user's original specification of an external frozen LLM (Qwen-2.5-7B) as 'meta-brain' with role-switching and a Unified Representation Interface. Through iterative analysis (Rounds 1-3), we determined that internal LoRA routing on the VLA's own backbone is superior for this problem: it avoids the prohibitive cross-model embedding alignment problem between an external LLM and the VLA's learned representation space, eliminates external LLM inference latency (critical for real-time control at 10-50Hz), and preserves the perturbation-adaptive routing insight from the original specification while simplifying the architecture. The 'meta-brain' concept is retained as the Perturbation-Adaptive Router — a lightweight internal module that fulfills the original spec's goal of diagnosing the perturbation type and orchestrating a type-specific response.
70	
71	**Phase 0: Early-Kill Validation Gate (Days 1-4).**
72	Before committing to the full training pipeline, we validate the core assumption: that perturbation types are classifiable from π₀ internal activations. Procedure: (a) Roll out frozen π₀ on a subset of LIBERO-Plus tasks under all 7 perturbation categories (~200 rollouts). Record intermediate activations at layers 4, 8, 12, 16, 20, 24, 28, 32. (b) Train 2-layer MLP classifier (hidden dim 256) on mean-pooled activations for 3-class perturbation-type classification (visual / spatial / physical). (c) Report classification accuracy. GO/NO-GO criterion: if accuracy >70%, proceed to full pipeline. If 50-70%, augment router inputs with proprioception history and visual change detection features, re-evaluate (Days 5-6 reserved as contingency). If <50%, pivot to universal LoRA + Correction Memory (dropping perturbation-type routing). This gate costs ~5 H100-hrs (from buffer) and prevents wasting 185 H100-hrs on a falsified premise. Evidence supporting feasibility: SAFE achieves 78.0% ROC-AUC for binary failure detection from the same activations using the same architecture (2-layer MLP, hidden 256), and 3-class perturbation type classification is a coarser signal than binary failure prediction, so should be easier.
73	
74	**1. Perturbation-Adaptive Router (PAR).**
75	Inspired by SAFE's demonstration that VLA internals encode execution-relevant signals, PAR trains lightweight classifiers (2-layer MLP, hidden dim 256, following SAFE's architecture) on intermediate activations from the frozen VLA backbone. Unlike SAFE's binary failure detection, PAR performs multi-class perturbation-type classification (visual / spatial / physical / nominal) with soft routing weights. The router operates on mean-pooled hidden states from layers selected via Phase 0 validation (following SAFE's aggregation protocol, evaluating first-token, last-token, mean, and first+last pooling strategies). PAR outputs a perturbation-type probability distribution p(type | h_l) used to softly weight LoRA expert contributions. PAR is trained with cross-entropy loss; optionally, meta-learning (Reptile across perturbation types) can improve generalization to unseen perturbation instances, at ~10 additional H100-hrs.
76	
77	**2. Adaptive LoRA Bank (ALB).**
78	Three perturbation-specific LoRA experts (rank 16) are applied to the attention layers of the frozen LLM backbone:
79	- **Visual LoRA (LoRA-V):** Corrects visual distribution shifts (camera viewpoint, lighting, background texture). Positioned on early-to-mid LLM layers where visual tokens are first integrated, analogous to FTM's visual recalibration but operating at the cross-modal fusion level rather than ViT output. For camera-only deployments, AnyCamVLA's zero-shot approach is more efficient; LoRA-V's value is unified handling of camera + lighting + background within the routing framework.
80	- **Spatial LoRA (LoRA-S):** Corrects spatial rearrangement perturbations (object repositioning, initial state changes). LoRA-S targets representational recalibration — biasing attention patterns toward correct spatial features under rearranged configurations — rather than explicit trajectory replanning. The mechanistic justification rests on converging evidence at two levels. At the representational level: Geier et al. (2502.04558) show >0.90 probing accuracy for spatial object relations across LLM layers, confirming spatial state is linearly encoded; Buurmeijer et al. (2603.05487) demonstrate that linear interventions on π₀.₅ achieve ~100% constraint satisfaction for end-effector position and gripper state. At the architectural level: LoRA-S operates on mid-to-late attention layers where spatial-action mappings are computed, modifying the query-key-value projections that determine how spatial token representations are attended to during trajectory planning. This is mechanistically distinct from simply shifting a spatial feature — it alters the attention patterns through which the model routes spatial information into action predictions. However, we acknowledge that for perturbations requiring qualitatively different trajectories (e.g., navigating around a repositioned obstacle rather than merely recalibrating spatial feature attention), representational-level correction may be insufficient — such cases likely require explicit 3D geometric reasoning as demonstrated by AFI's external affordance fields. The Phase 0 validation gate partially tests whether representational-level correction is sufficient: if PAR can classify spatial perturbations from internal activations, this indicates the backbone encodes the perturbation signal, but the adequacy of LoRA-level correction for trajectory-altering spatial changes remains an empirical question resolved in the ablation phase. Hence our pre-planned pivot to hybrid AFI integration if LoRA-S underperforms.
81	- **Physical LoRA (LoRA-P):** Corrects physical property changes (object mass, friction, deformability). Targets late LLM layers near action decoding.
82	
83	Expert outputs are combined via PAR's soft routing weights: h_corrected = h_frozen + Σ_k p(type_k) · LoRA_k(h_frozen), enabling smooth interpolation when perturbation types co-occur.
84	
85	Total trainable parameters: ~6M (3 × rank-16 LoRA experts at ~1.5M each + PAR at ~0.5M). This count excludes Correction Memory, which adds only a single learned scalar (α) and a non-parametric FAISS index. Note that Meta-Brain's fixed-rank experts could be further enhanced by composing with LoRA-SP's adaptive rank allocation within each perturbation-specific expert — a natural extension where LoRA-SP determines how much capacity each expert allocates per layer/input while Meta-Brain determines which expert type to activate.
86	
87	**3. Correction Memory (CM).**
88	A retrieval-augmented module that stores embeddings of (perturbation_context, correction_outcome, perturbation_type_label) tuples from successful training rollouts. CM's injection mechanism uses routing-weight modulation rather than cross-attention or prefix tokens: at inference, CM retrieves the k-nearest correction exemplars (k=5) based on cosine similarity between the current PAR activation embedding and stored perturbation context embeddings via a FAISS index. The retrieval results modulate PAR's routing distribution by injecting a correction bias derived from the perturbation-type labels of retrieved exemplars:
89	
90	  p_refined(type_k) = softmax(logits_PAR + α · Σ_j sim_j · one_hot(type_k^j))
91	
92	where sim_j is the cosine similarity of the j-th retrieved exemplar, type_k^j is its perturbation-type label, and α is a single learned scaling parameter. This mechanism biases routing toward experts that succeeded on historically similar perturbation instances, providing few-shot adaptation to novel perturbation instances within a known type without requiring additional model parameters. The design is motivated by two considerations: (a) it avoids the architectural mismatch of injecting retrieved embeddings via cross-attention into LoRA's additive weight perturbation framework, and (b) it elegantly connects CM to the routing pathway rather than creating a parallel conditioning channel. The FAISS index is CPU-bound at inference with <1ms lookup latency, adding no GPU overhead.
93	
94	**4. Training Protocol (18-Day Schedule for CoRL 2026, 2 researchers: 1 lead, 1 supporting).**
95	
96	The schedule is organized into three tiers of deliverables with graceful degradation:
97	- **Tier 1 (abstract submission, Day 12):** Phase 0 validation + LoRA training results + projected ablation plan. Does NOT require full routing validation or Correction Memory results.
98	- **Tier 2 (full paper submission, Day 15):** Main ablation ladder (a-d) + FTM comparison (e). Routing assembly and end-to-end evaluation must be complete.
99	- **Tier 3 (supplementary / camera-ready):** Additional ablations (f-h: CM ablation, router architecture comparison, layer placement). These are deferred if schedule slips without compromising the core contribution.
100	
101	**Detailed Schedule:**
102	- **Days 1-2 (May 15-16):** Setup π₀ + LIBERO-Plus environment using OpenPI codebase. Begin Phase 1 data collection: roll out frozen π₀ under all 7 perturbation categories, recording intermediate activations. ~500 rollouts with activation recording. [GPU 0-3 parallel rollouts, 15 H100-hrs] (Lead: environment setup; Support: data collection scripts)
103	- **Days 3-4 (May 17-18):** Phase 0 validation gate: train PAR classifier on collected activations, evaluate 3-class accuracy. Hyperparameter sweep: 3 pooling strategies × 4 layer subsets × 3 learning rates = 36 runs (<15 min each). GO/NO-GO decision by end of Day 4. [5 H100-hrs] (Lead: PAR training; Support: analysis scripts + begin paper skeleton)
104	- **Days 5-6 (May 19-20):** If Phase 0 GO (>70%): begin LoRA expert training (overlaps with Days 7-8). If Phase 0 AUGMENT (50-70%): implement router augmentation with proprioception history and visual change detection, re-evaluate PAR by end of Day 6. This 2-day contingency buffer a
105	
106	## Resource Estimate
107	
108	- **Timeline**: 15 working days primary (May 15-29) + 3 days Tier 3 (May 30 - Jun 1) with 4× H100 node. Team: 2 researchers (1 lead: architecture + experiments, 1 support: infrastructure + paper + baselines). Targeting CoRL 2026 (abstract May 26, paper May 29).
109	- **breakdown**: {'buffer': {'detail': 'Unexpected reruns, debugging, infrastructure issues. Reduced from 15 hrs since Phase 0 contingency is now explicitly budgeted separately.', 'h100_hours': 10}, 'phase0_contingency': {'detail': 'Contingency buffer for router augmentation if Phase 0 accuracy is 50-70%. Implement proprioception history features and visual change detection, retrain PAR. If >70% after augmentation, proceed to LoRA training on Day 7. If still <50%, pivot to universal LoRA + CM. This 2-day buffer prevents the augmentation path from delaying LoRA training.', 'h100_hours': 5, 'wall_days': 'Days 5-6 (only if Phase 0 result is 50-70%)'}, 'phase0_validation': {'detail': 'Early-kill gate: collect π₀ activations on LIBERO-Plus perturbation subset (~200 rollouts), train 2-layer MLP classifier (matching SAFE architecture: hidden 256), report 3-class accuracy. 36 hyperparameter configurations × <15 min each. GO/NO-GO decision by end of Day 4. Budget drawn from buffer.', 'h100_hours': 5, 'wall_days': 'Days 3-4'}, 'phase1_data_collection': {'detail': 'Roll out frozen π₀ on LIBERO-Plus under all 7 perturbation categories. Collect intermediate activations at layers 4, 8, 12, 16, 20, 24, 28, 32. ~500 rollouts × 7 perturbation types. Parallelized across 4 GPUs for ~4 hrs wall time. Uses OpenPI codebase with existing LIBERO configs.', 'h100_hours': 15, 'wall_days': 'Days 1-2'}, 'phase2_par_router': {'detail': 'Train perturbation classifier (2-layer MLP) on frozen activations. Full hyperparameter sweep after Phase 0 GO decision: 3 pooling strategies × 4 layer subsets × 3 learning rates = 36 runs. Each run <15 min on single H100.', 'h100_hours': 10, 'wall_days': 'Days 3-6 (overlaps with Phase 0 + contingency)'}, 'phase3_lora_experts': {'detail': '3 perturbation-specific LoRA experts (rank 16, attention layers) trained in parallel on 3 GPUs — one per perturbation type. ~18 H100-hrs each including per-expert hyperparameter tuning (rank {8,16,32} × layer subset × lr). GPU 4 runs universal LoRA baseline (ablation b) simultaneously. Wall time: ~20 hrs via 3-way parallelism.', 'h100_hours': 55, 'wall_days': 'Days 7-9'}, 'phase4_correction_memory_and_routing': {'detail': 'Populate Correction Memory FAISS index from successful training rollouts (5 H100-hrs). Assemble PAR + ALB + CM routing-modulation, end-to-end routing fine-tuning with frozen LoRA parameters (15 H100-hrs). FAISS index construction is CPU-bound. CM adds only 1 learned parameter (α scaling).', 'h100_hours': 20, 'wall_days': 'Days 10-11'}, 'phase5_tier2_experiments': {'detail': 'Tier 2 ablation ladder parallelized across 4 GPUs: (a) Frozen baseline eval: 3 hrs. (b) Universal LoRA eval: 5 hrs. (c) Meta-Brain full eval: 5 hrs. (d) Oracle routing eval: 5 hrs. (e) FTM reproduction: 10 hrs. Additional evaluation on LIBERO-PRO: 10 hrs. 10 seeds × key conditions. Wall time: ~13 hrs via 4-GPU parallelism.', 'h100_hours': 50, 'wall_days': 'Days 12-14'}, 'phase6_tier3_experiments': {'detail': 'Tier 3 ablations: (f) CM ablation: 5 hrs. (g) Router architecture comparison: 5 hrs. (h) Layer placement: 5 hrs. (i) Optional cross-backbone Qwen3-VL-4B experiment: 10 hrs (only if time permits). These are deferred to supplementary/camera-ready without compromising core contribution.', 'h100_hours': 20, 'wall_days': 'Days 16-18 (deferred if schedule slips)'}, 'phase7_paper_writing': {'detail': 'Paper skeleton begins Day 4 (Support researcher). Abstract submitted Day 12 (May 26, CoRL abstract deadline) using Phase 0 + LoRA training results + projected ablation plan. Full paper by Day 15 (May 29, CoRL paper deadline) with Tier 2 ablation results (a-e). Tier 3 results added to camera-ready if available.', 'h100_hours': 0, 'wall_days': 'Days 4-15 (overlaps with experiments)'}}
110	- **note**: Budget assumes π₀ backbone is frozen throughout — no backbone training cost. All LoRA training operates on <2M trainable parameters per expert (~6M total). LIBERO simulation runs on CPU alongside GPU training. OpenPI codebase provides existing π₀ + LIBERO training configs and LoRA fine-tuning support, eliminating setup overhead. Pure compute: 190 H100-hrs ÷ 4 GPUs = 48 GPU-hrs ≈ 2 days. Sequential pipeline dependencies + debugging + paper writing extend to 15-18 days. Tiered delivery ensures graceful degradation: Tier 1 (abstract) requires only Phase 0 + LoRA results; Tier 2 (paper) requires ablations a-e; Tier 3 (supplementary) contains additional ablations f-i.
111	- **total_h100_hours**: 190
112	
113	## Key References
114	
115	- {'id': '2605.06175', 'name': 'VLA-GSE', 'role': 'Secondary reference point (different backbone). Achieves 81.2% on LIBERO-Plus with 114M trainable params on Qwen3-VL-4B, demonstrating that expert routing on frozen VLA backbones is highly effective. Standard LoRA baseline on the same backbone: 69.2% (+12.0% from routing). Per-perturbation: Camera 64.4%, Robot 68.5%, Light 97.3%, Background 97.3%, Noise 79.4%, Layout 82.6%. Uses top-2 per-token gating across 7 specialized + 1 generalized expert per block — perturbation-agnostic capacity routing. Meta-Brain explores whether perturbation-diagnostic routing achieves comparable gains-over-LoRA at 20× fewer parameters through targeted specialization. Cross-backbone comparison (π₀ vs Qwen3-VL-4B) is acknowledged as confounded; gain-over-baseline metric enables contextualized comparison.'}
116	- {'id': '2603.07404', 'name': 'LoRA-SP', 'role': 'Capacity-based LoRA adaptation on π₀ and SmolVLA. Adapts LoRA rank per layer and per input via SVD-style parameterization with a small router whose nonneg scores act as singular values over a shared vector bank. Discovers that vision towers require highest ranks while language layers remain low. Matches or exceeds full fine-tuning on real-robot tasks with far fewer parameters, improving multi-task success by up to 31.6% over standard LoRA. Key distinction from Meta-Brain: LoRA-SP adapts HOW MUCH capacity to allocate (adaptive rank); Meta-Brain adapts WHAT TYPE of correction to apply (perturbation-specific experts). These orthogonal dimensions could be composed — adaptive rank within each perturbation-specific expert.'}
117	- {'id': '2604.18107', 'name': 'PDF (Test-Time Perturbation Learning)', 'role': 'Complementary test-time approach achieving +7.4% on standard LIBERO via uncertainty-based augmentation and delayed-feedback perturbation head on OpenVLA. No fine-tuning required. Meta-Brain and PDF address orthogonal deployment phases: training-time LoRA routing for strong per-type correction vs. test-time adaptation for zero-cost deployment. A Meta-Brain + PDF pipeline is a natural combination.'}
118	- {'id': '2603.05868', 'name': 'AnyCamVLA', 'role': "Zero-shot camera adaptation via feed-forward novel view synthesis, achieving 94.5% under camera perturbations. Plug-and-play with no fine-tuning. Overlaps with LoRA-V's visual perturbation correction for camera viewpoints specifically. Meta-Brain's LoRA-V additionally handles lighting and background perturbations; AnyCamVLA is superior for camera-only deployment. Complementary visual-specific approach."}
119	- {'id': '2512.07472', 'name': 'AFI', 'role': "Primary spatial-perturbation competitor. Achieves +20.2% LIBERO-PRO via external 3D Spatial Affordance Fields on frozen π₀/π₀.₅. Provides the upper bound for spatial perturbation correction and the pivot target if LoRA-S proves insufficient. Meta-Brain is the internal, multi-perturbation complement to AFI's external, spatial-specific approach."}
120	- {'id': '2506.09937', 'name': 'SAFE (NeurIPS 2025)', 'role': "Foundational evidence that VLA internals encode task-generic execution signals extractable by lightweight probes. Uses 2-layer MLP (hidden 256) on final-layer activations, achieving 78.0% ROC-AUC for binary failure detection on unseen tasks with 2.3M parameters. Directly motivates PAR's architecture (identical MLP design, extended to multi-class) and Phase 0 validation protocol. SAFE detects failure; PAR classifies perturbation type and routes to correction."}
121	- {'id': '2507.01843', 'name': 'MoIRA', 'role': 'Closest architectural analog — LoRA expert routing on π₀/GR00T-N1. Key difference: MoIRA routes by task instruction (text similarity); Meta-Brain routes by perturbation type (internal activation classification). Orthogonal routing dimensions.'}
122	- {'id': '2512.02902', 'name': 'FTM/FLA', 'role': 'Strongest simplicity baseline. Achieves ~90% visual robustness with 4K parameters via token modulation. Meta-Brain must demonstrate value beyond FTM for visual perturbations AND justify the routing overhead by additionally handling spatial/physical perturbations.'}
123	- {'id': '2603.05487', 'name': 'Feature Steering (Buurmeijer et al.)', 'role': 'Mechanistic evidence for internal correction feasibility. Linear interventions on π₀.₅/OpenVLA representations achieve ~100% constraint satisfaction for end-effector position and gripper state while maintaining >90% task success. Validates that LoRA-level corrections can manipulate spatial representations. Limitation: tested on standard tasks, not on rearranged-object scenarios — the harder spatial perturbation case remains empirically unvalidated.'}
124	- {'id': '2502.04558', 'name': 'VLA Probing (Geier et al.)', 'role': 'Probing evidence: >0.90 accuracy for spatial object states/relations across LLM layers 1-32. Confirms spatial information is linearly encoded and accessible for correction.'}
125	- {'id': '2603.19183', 'name': 'SAE-VLA', 'role': 'Sparse autoencoders reveal steerable motion primitives in VLA representations. Complementary evidence that VLA internals contain interpretable, controllable features beyond what linear probes capture.'}
126	- {'id': '2510.00037', 'name': 'RobustVLA (ICLR 2026)', 'role': 'Multi-modal perturbation baseline. Achieves +12.6% on π₀ across 17 perturbation types via uniform adversarial training. Meta-Brain hypothesizes type-specific routing outperforms this uniform approach.'}
127	- {'id': '2603.09298', 'name': 'CORAL', 'role': 'Task-based LoRA routing on frozen VLA. Demonstrates that per-task LoRA isolation outperforms joint fine-tuning. Motivates LoRA bank architecture but routes by task, not perturbation.'}
128	- {'id': '2510.13626', 'name': 'LIBERO-Plus', 'role': 'Primary evaluation benchmark (CVPR 2026). Defines 7 perturbation categories for systematic VLA robustness evaluation. Current SOTA: SRPO 82.1%, VLA-GSE 81.2%, CorridorVLA 83.21% (by task category, not per-perturbation), OpenVLA-OFT+ 79.6%, AVA-VLA 74.7%, MergeVLA 72.2%, π₀ frozen baseline 53.6%.'}
129	- {'id': '2510.03827', 'name': 'LIBERO-PRO', 'role': 'Secondary evaluation benchmark. Tests generalization across object positions, initial states, instructions, and environments.'}
130	- {'id': '2511.09516', 'name': 'MAP-VLA', 'role': 'Memory-augmented VLA prompting using learnable soft prompts as prefix tokens, retrieved via trajectory similarity. Inspires Correction Memory concept but uses a different injection mechanism: MAP-VLA prepends retrieved prompts as prefix tokens; CM modulates router probability distributions via retrieval similarity. Both are plug-and-play on frozen backbones.'}
131	- {'id': '2511.15605', 'name': 'SRPO', 'role': 'Current LIBERO-Plus SOTA at 82.1% (by perturbation category) via self-referential RL policy optimization using latent world model progress signals. Uses full RL training (not parameter-efficient), representing the upper bound for what VLA adaptation can achieve on this benchmark.'}
132	- {'id': '2604.21241', 'name': 'CorridorVLA', 'role': "Demonstrates explicit spatial constraints (anchor-defined corridors) can guide VLA action generation. GR00T-Corr achieves 83.21% on the LIBERO-Plus dataset, but reported by task category (Long 74.55%, Goal 85.75%, Object 88.4%, Spatial 84.14%) rather than by perturbation type (Camera/Robot/Light/Background/Noise/Layout), so direct per-perturbation comparison with VLA-GSE or Meta-Brain's target metrics is not straightforward. Evidence that spatial corrections at the action-planning level via explicit geometric constraints are feasible and effective."}
133	- {'id': '2510.12276', 'name': 'Spatial Forcing (ICLR 2026)', 'role': 'Aligns intermediate VLA representations with 3D foundation model features during training, achieving 98.5% on standard LIBERO and 3.8× training speedup. Shows that spatial representation quality directly impacts action precision. Complementary training-time strategy; Meta-Brain operates post-hoc on frozen backbones.'}
134	
135	## Reviewer Evaluation
136	
137	**Scores**:
138	  - clarity: **{'rationale': "Exceptionally well-structured across all dimensions: comprehensive 17-reference landscape with per-competitor differentiation, clean ablation ladder with explicit falsification criteria and pivot strategies, honest framing of cross-backbone confounds (VLA-GSE comparison), detailed per-phase compute accounting, and the CM routing-modulation mechanism is now precisely specified. Among the clearest VLA robustness proposals I've reviewed.", 'score': 5}**/5
139	  - feasibility: **{'rationale': 'Phase 0 validation gate at Day 3-4 is excellent risk management. Tiered delivery (abstract needs only Phase 0 + LoRA results; Tier 3 deferred to camera-ready) provides realistic contingency. 190 H100-hrs with 4×H100 is tight but the compute math is internally consistent. The 2-day contingency buffer and pre-planned pivots (AFI hybrid for spatial, universal LoRA + CM if routing fails) demonstrate mature project management.', 'score': 4}**/5
140	  - impact: **{'rationale': 'The routing principle (perturbation-type-specific correction > universal correction) is a useful design insight, but the target performance (72-80% on LIBERO-Plus) lands below current SOTA (SRPO 82.1%, CorridorVLA 83.21%, VLA-GSE 81.2%). The parameter efficiency argument (6M vs 114M) is strong but may not fully compensate for the absolute performance gap in reviewer reception. Sim-only evaluation is accepted at CoRL but limits practical impact claims.', 'score': 3}**/5
141	  - novelty: **{'rationale': 'Perturbation-type-aware diagnostic routing is a genuinely new routing dimension, orthogonal to all existing work (task-based: MoIRA/CORAL, capacity-based: VLA-GSE, rank-based: LoRA-SP). The CM routing-modulation mechanism adds secondary novelty. Components are borrowed (SAFE-style probing, LoRA, MoE routing) but the combination and the specific hypothesis it tests are novel.', 'score': 4}**/5
142	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "3b51b2ec-eb1f-4f59-800e-c48c80dd5f0a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/docs/IDEA_BRIEF.md",
      "content": "# Idea Brief: Meta-Brain: Perturbation-Adaptive LoRA Routing for Robust Vision-Language-Action Models\n\n\n- **Idea ID**: `idea_007`\n- **Created**: 2026-05-15\n- **Approved**: 2026-05-15\n- **Source**: foreign:be-idea-gen-0509-15\n- **Level**: top-tier\n\n## Seed Topic\n\n按照以下方向，生成1-2个优质idea，保质不求量：Seed 3: Meta-Brain — LLM Role-Switching as Adaptive Robustness Controller for VLA\nTarget: CoRL 2026 (Austin, Nov 9–12, 2026). Abstract deadline 2026-05-26 (12 days from today 2026-05-14); paper deadline 2026-05-29 (15 days).\nDirection: LLM-as-Meta-Brain for VLA robustness — an architecture where a frozen LLM dynamically switches between specialized roles (perception enhancement, logic decomposition, anomaly intervention) and feeds unified modified visual tokens back to a VLA backbone, enabling robust operation across diverse perturbation scenarios without retraining the VLA. The core motivation is that different robustness failures require qualitatively different interventions: visual noise needs perceptual re-grounding, ambiguous instructions need task decomposition, and execution uncertainty needs reflective error correction. Rather than training a single monolithic robust VLA, we leverage the LLM's pre-existing world knowledge and reasoning capabilities as an external \"meta-brain\" that diagnoses the current failure mode and provides targeted representational guidance. The key architectural innovation is a Unified Representation Interface: regardless of which role the LLM assumes, it outputs through a shared Adapter into a fixed-dimensional token modification that directly reshapes the VLA's visual tokens — this means the VLA backbone sees the same token format but with role-specific semantic content baked in. This avoids the fragility of language-mediated VLA guidance (which breaks under paraphrasing) and instead operates in continuous representation space.\nRecent landscape (do not duplicate): SOMA: Strategic Orchestration and Memory-Augmented System for Vision-Language-Action Model Robustness via In-Context Adaptation\nCoRAL: Contact-Rich Adaptive LLM-Based Control for Robotic Manipulation\nVLA-Pilot: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\nObserving and Controlling Features in Vision-Language-Action Models\nON ROBUSTNESS OF VISION-LANGUAGE-ACTION MODEL AGAINST MULTI-MODAL PERTURBATIONS\nSTRONG-VLA: Decoupled Robustness Learning for Vision-Language-Action Models under Multimodal Perturbations\nControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models\nContribution type: METHOD ONLY. A three-component architecture: (1) Role Router — a lightweight classifier on top of the VLA's current state embedding that detects the perturbation regime: high visual entropy → perception mode, high instruction ambiguity → logic mode, high action uncertainty → intervention mode. Trained with meta-learning across perturbation types. (2) Role-Conditioned Adapter — a shared Adapter between the frozen LLM and VLA that outputs one of three representation modalities through the same interface: (a) Hybrid Semantic Tokens — role-conditioned embedding vectors that reshape visual tokens to emphasize task-relevant features; (b) Function Prefix — a role embedding prepended to the modified tokens that biases VLA attention heads toward the appropriate processing mode; (c) Attention Mask — a spatial weight matrix that gates visual token importance (suppress distractors, enhance depth features, highlight skill-relevant objects). (3) Dynamic Skill Library — when the meta-brain's intervention produces a novel solution pattern, it is distilled into a reusable skill embedding stored persistently; future encounters of similar perturbations route directly to the skill without full LLM inference. Training: two-phase — Phase 1 trains the Adapter with meta-learning across role-switching datasets; Phase 2 trains end-to-end with the VLA backbone frozen, optimizing only the Router + Adapter for action prediction under perturbation.\nEVAL PROTOCOL — IMPORTANT:\nTRAIN on standard LIBERO suites (Object/Spatial/Goal/Long/90).\nEVALUATE on existing LIBERO-PLUS / LIBERO-PRO style perturbation benchmarks (and similar community-released robustness benchmark series). DO NOT spend time constructing your own robustness benchmark — use existing perturbation suites and route the budget into the method.\nReport robustness gap (Δ between nominal LIBERO success and perturbed-suite success) AND nominal preservation (must not regress on base LIBERO).\nAdditionally report: per-perturbation-type breakdown (visual/language/action noise) with role activation frequency, latency overhead of meta-brain inference, ablation of individual roles and combined system.\nExperiments can be extended to CALVIN or RLBench perturbation variants to verify cross-benchmark robustness and role generalization.\nSIM-ONLY MITIGATION: Robustness eval in sim is well-accepted at CoRL — established LIBERO-PLUS / LIBERO-PRO style suites are a recognized sim-only pattern. The meta-brain architecture operates on representations, not physical hardware, making sim evaluation methodologically sufficient.\nHARD CONSTRAINTS:\nCompute: ≤200 H100-hours total. LLM is frozen (e.g., Qwen-2.5-7B or LLaMA-3-8B); VLA backbone is frozen (OpenVLA/SmolVLA/OpenPi/π0 checkpoint). Only train Router (~2M params) + Adapter (~15M params). Show the math: Adapter training ≈ 50 H100-hrs, Router meta-learning ≈ 30 H100-hrs, evaluation ≈ 40 H100-hrs.\nTime: ≤20 days. Build on OpenVLA, OpenPi and other proper codebases, LeRobot, HF Transformers. LLM integration via HuggingFace model loading.\nEval datasets: LIBERO base (training/nominal eval) + LIBERO-PLUS / LIBERO-PRO and similar existing perturbation suites (perturbed eval). No custom benchmark construction.\nLook for: meta-learning for role router that generalizes to unseen perturbation types, unified adapter architecture that maps heterogeneous LLM guidance into a common token-modification interface, attention masking as a differentiable robustness mechanism, skill library as amortized robustness (one-time LLM cost → reusable embedding), theoretical connections between role diversity and minimax robustness over perturbation sets. Avoid: language-only LLM guidance that is itself fragile to paraphrasing, requiring LLM inference at every VLA timestep (must amortize via skill caching), plain ensembling of multiple VLAs, custom robustness benchmark construction, approaches requiring real-robot data for the meta-brain training.\nTag: direction=robust_vla, contribution_type=method, sub_direction=meta_brain_role_switching, target_venues=[\"CoRL 2026\"].\n\n## Core Problem\n\nVision-Language-Action (VLA) models achieve >90% success on standard LIBERO benchmarks but suffer catastrophic performance drops under perturbation: π₀ falls from >90% nominal to 53.6% average on LIBERO-Plus, with camera perturbations at 13.8% and robot initial-state perturbations at 6.0%. This brittleness stems from VLAs memorizing fixed vision-action mappings rather than developing genuine environmental understanding. Critically, different perturbation types disrupt different processing stages: visual perturbations (camera, lighting) corrupt early visual token representations, spatial perturbations (object rearrangement) invalidate learned action trajectories, and physical perturbations (object mass, friction) break force-compliance assumptions. Current robustness methods either address a single perturbation modality (FTM for visual, AFI for spatial, AnyCamVLA for camera viewpoint) or apply uniform correction across all perturbation types (RobustVLA's adversarial training, VLA-GSE's per-token capacity routing), leaving a fundamental question unanswered: does perturbation-type-aware diagnostic routing outperform one-size-fits-all adaptation?\n\n## Opportunity / Why Now\n\nFour concurrent lines of evidence from 2025-2026 converge to make perturbation-adaptive internal correction newly feasible: (1) SAFE (NeurIPS 2025) demonstrates that VLA intermediate activations encode rich, task-generic signals about execution state — a lightweight MLP on frozen features achieves SOTA failure detection across unseen tasks with <1% overhead, proving that perturbation-relevant information is extractable from VLA internals; (2) Linear probing of OpenVLA (Geier et al., 2502.04558) shows >0.90 accuracy for spatial object states and relations across layers 1-32 of the LLM backbone, establishing that spatial information sufficient for correction is linearly accessible; (3) Feature steering on π₀.₅ and OpenVLA (Buurmeijer et al., 2603.05487) demonstrates that minimal linear interventions on internal representations can reliably steer robot behavior with ~100% constraint satisfaction while preserving closed-loop task performance — proving that the representations are not just readable but controllable; (4) VLA-GSE (2605.06175) achieves 81.2% on LIBERO-Plus with spectral MoE routing using 114M trainable parameters on Qwen3-VL-4B, demonstrating that expert routing on frozen VLA backbones is highly effective — but its per-token capacity routing is perturbation-agnostic, leaving room for perturbation-diagnostic routing as an orthogonal design dimension. Together, these findings establish that VLA internals contain sufficient perturbation-diagnostic information AND that lightweight internal interventions can correct behavior without disrupting the frozen backbone's capabilities.\n\n## Landscape (SOTA & Limitations)\n\nThe VLA robustness landscape in early 2026 features complementary but incomplete solutions across seven categories:\n\n**Single-modality correction:** FTM/FLA (Li et al., 2512.02902) achieves 87-91% viewpoint recovery via visual token modulation with only 4K-4.7M parameters — highly efficient for visual perturbations but architecturally limited to recalibrating ViT outputs, with no mechanism for spatial or physical corrections. AFI (Chen et al., 2512.07472) achieves +20.2% on LIBERO-PRO through external 3D Spatial Affordance Fields that detect 'memory traps' via proprioception and propose affordance-driven waypoints — effective for spatial perturbations but requires an external geometric module and does not address visual or physical perturbations. AnyCamVLA (Heo et al., 2603.05868) provides zero-shot camera adaptation via feed-forward novel view synthesis, achieving 94.5% average success under camera perturbations by virtually transforming test-time observations to match training camera configuration — a plug-and-play visual-specific solution requiring no fine-tuning but limited to camera viewpoint changes.\n\n**Multi-modal but uniform correction:** RobustVLA (ICLR 2026, 2510.00037) formulates multi-perturbation robustness as a multi-armed bandit problem, achieving +12.6% on π₀ across 17 perturbation types. However, it applies a single adversarial training strategy uniformly, potentially underperforming on perturbations that require qualitatively different corrections.\n\n**Capacity-based expert routing (perturbation-agnostic):** VLA-GSE (2605.06175) decomposes frozen VLA weights via SVD into generalized (shared) and specialized (routed) experts, achieving 81.2% on LIBERO-Plus with 114M trainable parameters (2.51% of model) on Qwen3-VL-4B. VLA-GSE uses top-2 per-token gating across 7 specialized + 1 generalized expert per block for capacity allocation. This is the current strongest parameter-efficient method on LIBERO-Plus but routes by input-dependent capacity needs, not by perturbation type — the same routing configuration handles camera perturbations (64.4%) and layout perturbations (82.6%) without perturbation-type awareness. Importantly, VLA-GSE's standard LoRA baseline on the same Qwen3-VL-4B backbone achieves 69.2%, providing a controlled reference for the value of routing (+12.0% over LoRA).\n\n**Capacity-based LoRA adaptation:** LoRA-SP (2603.07404) adapts LoRA rank per layer and per input on π₀ and SmolVLA via an SVD-style parameterization with a small router whose nonnegative scores act as singular values over a shared vector bank. The active rank set is selected by an energy threshold on cumulative squared scores, discovering that vision towers require the highest ranks while language layers remain low and stable. On real-robot manipulation tasks, LoRA-SP matches or exceeds full fine-tuning with far fewer trainable parameters and improves multi-task success by up to 31.6% over standard LoRA. LoRA-SP adapts HOW MUCH LoRA capacity to allocate (adaptive rank); Meta-Brain adapts WHAT TYPE of correction to apply (perturbation-specific experts). These are orthogonal dimensions that could be composed — adaptive rank within each perturbation-specific expert — representing a natural extension.\n\n**Task-based LoRA routing (not perturbation-based):** CORAL (2603.09298) freezes the VLA backbone and attaches one LoRA expert per task, with a language-based manager routing instructions to experts. MoIRA (2507.01843) routes LoRA experts on π₀/GR00T-N1 using text-based similarity for task specialization. Both achieve strong multi-task performance but route by task identity/instruction — they cannot distinguish or adapt to different perturbation types within the same task.\n\n**Spatial-aware VLA architectures:** SpatialVLA (2501.15830) injects 3D position encodings into VLA input, achieving 88.2% on LIBERO-Spatial; Spatial Forcing (ICLR 2026, 2510.12276) aligns intermediate VLA representations with 3D foundation model features, achieving 98.5% on standard LIBERO and 3.8× training speedup — both enhance spatial understanding at training time but are complementary to, not competitive with, post-hoc perturbation correction on frozen backbones. CorridorVLA (2604.21241) uses explicit spatial anchor constraints to guide action generation; its GR00T-Corr variant achieves 83.21% on the LIBERO-Plus dataset, though reported by task category (Long/Goal/Object/Spatial) rather than by perturbation type (Camera/Robot/Light/Background/Noise/Layout), making direct per-perturbation comparison with VLA-GSE or Meta-Brain's target metrics not straightforward. CorridorVLA demonstrates that spatial corrections at the action-planning level via explicit geometric constraints are feasible and effective.\n\n**Test-time adaptation:** PDF (2604.18107) achieves +7.4% on LIBERO via test-time perturbation learning with delayed feedback — a lightweight perturbation head adjusts action logits using REINFORCE-style optimization guided by post-action observations, requiring no fine-tuning. PDF and Meta-Brain are complementary: training-time LoRA routing (Meta-Brain) for strong per-perturbation-type correction + test-time adaptation (PDF) for novel perturbation instances.\n\n**VLA internal analysis:** SAFE (NeurIPS 2025, 2506.09937) probes VLA final-layer activations for binary failure detection using a 2-layer MLP (hidden dim 256, 2.3M params), achieving 78.0% ROC-AUC on unseen tasks. Probing work (2502.04558) extracts symbolic spatial states. Feature steering (2603.05487) demonstrates behavioral control through linear interventions on end-effector position and gripper state, achieving ~100% constraint satisfaction. These works establish feasibility but stop at detection/analysis — none close the loop from perturbation diagnosis to targeted correction.\n\n**Gap:** No existing method combines (a) perturbation-type detection from VLA internals with (b) type-specific corrective adaptation. VLA-GSE routes by input capacity (perturbation-agnostic); LoRA-SP adapts rank per layer/input (capacity-agnostic to perturbation type); MoIRA/CORAL route by task instruction; PDF adapts at test-time without perturbation classification. Meta-Brain uniquely routes corrective LoRA experts by diagnosed perturbation type, testing the hypothesis that perturbation-aware specialization achieves comparable robustness gains at dramatically fewer trainable parameters through targeted correction rather than capacity expansion.\n\n## Proposed Approach\n\n**Meta-Brain** is a modular correction framework for frozen VLA backbones (π₀, π₀-FAST) comprising four components. The design departs from the user's original specification of an external frozen LLM (Qwen-2.5-7B) as 'meta-brain' with role-switching and a Unified Representation Interface. Through iterative analysis (Rounds 1-3), we determined that internal LoRA routing on the VLA's own backbone is superior for this problem: it avoids the prohibitive cross-model embedding alignment problem between an external LLM and the VLA's learned representation space, eliminates external LLM inference latency (critical for real-time control at 10-50Hz), and preserves the perturbation-adaptive routing insight from the original specification while simplifying the architecture. The 'meta-brain' concept is retained as the Perturbation-Adaptive Router — a lightweight internal module that fulfills the original spec's goal of diagnosing the perturbation type and orchestrating a type-specific response.\n\n**Phase 0: Early-Kill Validation Gate (Days 1-4).**\nBefore committing to the full training pipeline, we validate the core assumption: that perturbation types are classifiable from π₀ internal activations. Procedure: (a) Roll out frozen π₀ on a subset of LIBERO-Plus tasks under all 7 perturbation categories (~200 rollouts). Record intermediate activations at layers 4, 8, 12, 16, 20, 24, 28, 32. (b) Train 2-layer MLP classifier (hidden dim 256) on mean-pooled activations for 3-class perturbation-type classification (visual / spatial / physical). (c) Report classification accuracy. GO/NO-GO criterion: if accuracy >70%, proceed to full pipeline. If 50-70%, augment router inputs with proprioception history and visual change detection features, re-evaluate (Days 5-6 reserved as contingency). If <50%, pivot to universal LoRA + Correction Memory (dropping perturbation-type routing). This gate costs ~5 H100-hrs (from buffer) and prevents wasting 185 H100-hrs on a falsified premise. Evidence supporting feasibility: SAFE achieves 78.0% ROC-AUC for binary failure detection from the same activations using the same architecture (2-layer MLP, hidden 256), and 3-class perturbation type classification is a coarser signal than binary failure prediction, so should be easier.\n\n**1. Perturbation-Adaptive Router (PAR).**\nInspired by SAFE's demonstration that VLA internals encode execution-relevant signals, PAR trains lightweight classifiers (2-layer MLP, hidden dim 256, following SAFE's architecture) on intermediate activations from the frozen VLA backbone. Unlike SAFE's binary failure detection, PAR performs multi-class perturbation-type classification (visual / spatial / physical / nominal) with soft routing weights. The router operates on mean-pooled hidden states from layers selected via Phase 0 validation (following SAFE's aggregation protocol, evaluating first-token, last-token, mean, and first+last pooling strategies). PAR outputs a perturbation-type probability distribution p(type | h_l) used to softly weight LoRA expert contributions. PAR is trained with cross-entropy loss; optionally, meta-learning (Reptile across perturbation types) can improve generalization to unseen perturbation instances, at ~10 additional H100-hrs.\n\n**2. Adaptive LoRA Bank (ALB).**\nThree perturbation-specific LoRA experts (rank 16) are applied to the attention layers of the frozen LLM backbone:\n- **Visual LoRA (LoRA-V):** Corrects visual distribution shifts (camera viewpoint, lighting, background texture). Positioned on early-to-mid LLM layers where visual tokens are first integrated, analogous to FTM's visual recalibration but operating at the cross-modal fusion level rather than ViT output. For camera-only deployments, AnyCamVLA's zero-shot approach is more efficient; LoRA-V's value is unified handling of camera + lighting + background within the routing framework.\n- **Spatial LoRA (LoRA-S):** Corrects spatial rearrangement perturbations (object repositioning, initial state changes). LoRA-S targets representational recalibration — biasing attention patterns toward correct spatial features under rearranged configurations — rather than explicit trajectory replanning. The mechanistic justification rests on converging evidence at two levels. At the representational level: Geier et al. (2502.04558) show >0.90 probing accuracy for spatial object relations across LLM layers, confirming spatial state is linearly encoded; Buurmeijer et al. (2603.05487) demonstrate that linear interventions on π₀.₅ achieve ~100% constraint satisfaction for end-effector position and gripper state. At the architectural level: LoRA-S operates on mid-to-late attention layers where spatial-action mappings are computed, modifying the query-key-value projections that determine how spatial token representations are attended to during trajectory planning. This is mechanistically distinct from simply shifting a spatial feature — it alters the attention patterns through which the model routes spatial information into action predictions. However, we acknowledge that for perturbations requiring qualitatively different trajectories (e.g., navigating around a repositioned obstacle rather than merely recalibrating spatial feature attention), representational-level correction may be insufficient — such cases likely require explicit 3D geometric reasoning as demonstrated by AFI's external affordance fields. The Phase 0 validation gate partially tests whether representational-level correction is sufficient: if PAR can classify spatial perturbations from internal activations, this indicates the backbone encodes the perturbation signal, but the adequacy of LoRA-level correction for trajectory-altering spatial changes remains an empirical question resolved in the ablation phase. Hence our pre-planned pivot to hybrid AFI integration if LoRA-S underperforms.\n- **Physical LoRA (LoRA-P):** Corrects physical property changes (object mass, friction, deformability). Targets late LLM layers near action decoding.\n\nExpert outputs are combined via PAR's soft routing weights: h_corrected = h_frozen + Σ_k p(type_k) · LoRA_k(h_frozen), enabling smooth interpolation when perturbation types co-occur.\n\nTotal trainable parameters: ~6M (3 × rank-16 LoRA experts at ~1.5M each + PAR at ~0.5M). This count excludes Correction Memory, which adds only a single learned scalar (α) and a non-parametric FAISS index. Note that Meta-Brain's fixed-rank experts could be further enhanced by composing with LoRA-SP's adaptive rank allocation within each perturbation-specific expert — a natural extension where LoRA-SP determines how much capacity each expert allocates per layer/input while Meta-Brain determines which expert type to activate.\n\n**3. Correction Memory (CM).**\nA retrieval-augmented module that stores embeddings of (perturbation_context, correction_outcome, perturbation_type_label) tuples from successful training rollouts. CM's injection mechanism uses routing-weight modulation rather than cross-attention or prefix tokens: at inference, CM retrieves the k-nearest correction exemplars (k=5) based on cosine similarity between the current PAR activation embedding and stored perturbation context embeddings via a FAISS index. The retrieval results modulate PAR's routing distribution by injecting a correction bias derived from the perturbation-type labels of retrieved exemplars:\n\n  p_refined(type_k) = softmax(logits_PAR + α · Σ_j sim_j · one_hot(type_k^j))\n\nwhere sim_j is the cosine similarity of the j-th retrieved exemplar, type_k^j is its perturbation-type label, and α is a single learned scaling parameter. This mechanism biases routing toward experts that succeeded on historically similar perturbation instances, providing few-shot adaptation to novel perturbation instances within a known type without requiring additional model parameters. The design is motivated by two considerations: (a) it avoids the architectural mismatch of injecting retrieved embeddings via cross-attention into LoRA's additive weight perturbation framework, and (b) it elegantly connects CM to the routing pathway rather than creating a parallel conditioning channel. The FAISS index is CPU-bound at inference with <1ms lookup latency, adding no GPU overhead.\n\n**4. Training Protocol (18-Day Schedule for CoRL 2026, 2 researchers: 1 lead, 1 supporting).**\n\nThe schedule is organized into three tiers of deliverables with graceful degradation:\n- **Tier 1 (abstract submission, Day 12):** Phase 0 validation + LoRA training results + projected ablation plan. Does NOT require full routing validation or Correction Memory results.\n- **Tier 2 (full paper submission, Day 15):** Main ablation ladder (a-d) + FTM comparison (e). Routing assembly and end-to-end evaluation must be complete.\n- **Tier 3 (supplementary / camera-ready):** Additional ablations (f-h: CM ablation, router architecture comparison, layer placement). These are deferred if schedule slips without compromising the core contribution.\n\n**Detailed Schedule:**\n- **Days 1-2 (May 15-16):** Setup π₀ + LIBERO-Plus environment using OpenPI codebase. Begin Phase 1 data collection: roll out frozen π₀ under all 7 perturbation categories, recording intermediate activations. ~500 rollouts with activation recording. [GPU 0-3 parallel rollouts, 15 H100-hrs] (Lead: environment setup; Support: data collection scripts)\n- **Days 3-4 (May 17-18):** Phase 0 validation gate: train PAR classifier on collected activations, evaluate 3-class accuracy. Hyperparameter sweep: 3 pooling strategies × 4 layer subsets × 3 learning rates = 36 runs (<15 min each). GO/NO-GO decision by end of Day 4. [5 H100-hrs] (Lead: PAR training; Support: analysis scripts + begin paper skeleton)\n- **Days 5-6 (May 19-20):** If Phase 0 GO (>70%): begin LoRA expert training (overlaps with Days 7-8). If Phase 0 AUGMENT (50-70%): implement router augmentation with proprioception history and visual change detection, re-evaluate PAR by end of Day 6. This 2-day contingency buffer a\n\n## Resource Estimate\n\n- **Timeline**: 15 working days primary (May 15-29) + 3 days Tier 3 (May 30 - Jun 1) with 4× H100 node. Team: 2 researchers (1 lead: architecture + experiments, 1 support: infrastructure + paper + baselines). Targeting CoRL 2026 (abstract May 26, paper May 29).\n- **breakdown**: {'buffer': {'detail': 'Unexpected reruns, debugging, infrastructure issues. Reduced from 15 hrs since Phase 0 contingency is now explicitly budgeted separately.', 'h100_hours': 10}, 'phase0_contingency': {'detail': 'Contingency buffer for router augmentation if Phase 0 accuracy is 50-70%. Implement proprioception history features and visual change detection, retrain PAR. If >70% after augmentation, proceed to LoRA training on Day 7. If still <50%, pivot to universal LoRA + CM. This 2-day buffer prevents the augmentation path from delaying LoRA training.', 'h100_hours': 5, 'wall_days': 'Days 5-6 (only if Phase 0 result is 50-70%)'}, 'phase0_validation': {'detail': 'Early-kill gate: collect π₀ activations on LIBERO-Plus perturbation subset (~200 rollouts), train 2-layer MLP classifier (matching SAFE architecture: hidden 256), report 3-class accuracy. 36 hyperparameter configurations × <15 min each. GO/NO-GO decision by end of Day 4. Budget drawn from buffer.', 'h100_hours': 5, 'wall_days': 'Days 3-4'}, 'phase1_data_collection': {'detail': 'Roll out frozen π₀ on LIBERO-Plus under all 7 perturbation categories. Collect intermediate activations at layers 4, 8, 12, 16, 20, 24, 28, 32. ~500 rollouts × 7 perturbation types. Parallelized across 4 GPUs for ~4 hrs wall time. Uses OpenPI codebase with existing LIBERO configs.', 'h100_hours': 15, 'wall_days': 'Days 1-2'}, 'phase2_par_router': {'detail': 'Train perturbation classifier (2-layer MLP) on frozen activations. Full hyperparameter sweep after Phase 0 GO decision: 3 pooling strategies × 4 layer subsets × 3 learning rates = 36 runs. Each run <15 min on single H100.', 'h100_hours': 10, 'wall_days': 'Days 3-6 (overlaps with Phase 0 + contingency)'}, 'phase3_lora_experts': {'detail': '3 perturbation-specific LoRA experts (rank 16, attention layers) trained in parallel on 3 GPUs — one per perturbation type. ~18 H100-hrs each including per-expert hyperparameter tuning (rank {8,16,32} × layer subset × lr). GPU 4 runs universal LoRA baseline (ablation b) simultaneously. Wall time: ~20 hrs via 3-way parallelism.', 'h100_hours': 55, 'wall_days': 'Days 7-9'}, 'phase4_correction_memory_and_routing': {'detail': 'Populate Correction Memory FAISS index from successful training rollouts (5 H100-hrs). Assemble PAR + ALB + CM routing-modulation, end-to-end routing fine-tuning with frozen LoRA parameters (15 H100-hrs). FAISS index construction is CPU-bound. CM adds only 1 learned parameter (α scaling).', 'h100_hours': 20, 'wall_days': 'Days 10-11'}, 'phase5_tier2_experiments': {'detail': 'Tier 2 ablation ladder parallelized across 4 GPUs: (a) Frozen baseline eval: 3 hrs. (b) Universal LoRA eval: 5 hrs. (c) Meta-Brain full eval: 5 hrs. (d) Oracle routing eval: 5 hrs. (e) FTM reproduction: 10 hrs. Additional evaluation on LIBERO-PRO: 10 hrs. 10 seeds × key conditions. Wall time: ~13 hrs via 4-GPU parallelism.', 'h100_hours': 50, 'wall_days': 'Days 12-14'}, 'phase6_tier3_experiments': {'detail': 'Tier 3 ablations: (f) CM ablation: 5 hrs. (g) Router architecture comparison: 5 hrs. (h) Layer placement: 5 hrs. (i) Optional cross-backbone Qwen3-VL-4B experiment: 10 hrs (only if time permits). These are deferred to supplementary/camera-ready without compromising core contribution.', 'h100_hours': 20, 'wall_days': 'Days 16-18 (deferred if schedule slips)'}, 'phase7_paper_writing': {'detail': 'Paper skeleton begins Day 4 (Support researcher). Abstract submitted Day 12 (May 26, CoRL abstract deadline) using Phase 0 + LoRA training results + projected ablation plan. Full paper by Day 15 (May 29, CoRL paper deadline) with Tier 2 ablation results (a-e). Tier 3 results added to camera-ready if available.', 'h100_hours': 0, 'wall_days': 'Days 4-15 (overlaps with experiments)'}}\n- **note**: Budget assumes π₀ backbone is frozen throughout — no backbone training cost. All LoRA training operates on <2M trainable parameters per expert (~6M total). LIBERO simulation runs on CPU alongside GPU training. OpenPI codebase provides existing π₀ + LIBERO training configs and LoRA fine-tuning support, eliminating setup overhead. Pure compute: 190 H100-hrs ÷ 4 GPUs = 48 GPU-hrs ≈ 2 days. Sequential pipeline dependencies + debugging + paper writing extend to 15-18 days. Tiered delivery ensures graceful degradation: Tier 1 (abstract) requires only Phase 0 + LoRA results; Tier 2 (paper) requires ablations a-e; Tier 3 (supplementary) contains additional ablations f-i.\n- **total_h100_hours**: 190\n\n## Key References\n\n- {'id': '2605.06175', 'name': 'VLA-GSE', 'role': 'Secondary reference point (different backbone). Achieves 81.2% on LIBERO-Plus with 114M trainable params on Qwen3-VL-4B, demonstrating that expert routing on frozen VLA backbones is highly effective. Standard LoRA baseline on the same backbone: 69.2% (+12.0% from routing). Per-perturbation: Camera 64.4%, Robot 68.5%, Light 97.3%, Background 97.3%, Noise 79.4%, Layout 82.6%. Uses top-2 per-token gating across 7 specialized + 1 generalized expert per block — perturbation-agnostic capacity routing. Meta-Brain explores whether perturbation-diagnostic routing achieves comparable gains-over-LoRA at 20× fewer parameters through targeted specialization. Cross-backbone comparison (π₀ vs Qwen3-VL-4B) is acknowledged as confounded; gain-over-baseline metric enables contextualized comparison.'}\n- {'id': '2603.07404', 'name': 'LoRA-SP', 'role': 'Capacity-based LoRA adaptation on π₀ and SmolVLA. Adapts LoRA rank per layer and per input via SVD-style parameterization with a small router whose nonneg scores act as singular values over a shared vector bank. Discovers that vision towers require highest ranks while language layers remain low. Matches or exceeds full fine-tuning on real-robot tasks with far fewer parameters, improving multi-task success by up to 31.6% over standard LoRA. Key distinction from Meta-Brain: LoRA-SP adapts HOW MUCH capacity to allocate (adaptive rank); Meta-Brain adapts WHAT TYPE of correction to apply (perturbation-specific experts). These orthogonal dimensions could be composed — adaptive rank within each perturbation-specific expert.'}\n- {'id': '2604.18107', 'name': 'PDF (Test-Time Perturbation Learning)', 'role': 'Complementary test-time approach achieving +7.4% on standard LIBERO via uncertainty-based augmentation and delayed-feedback perturbation head on OpenVLA. No fine-tuning required. Meta-Brain and PDF address orthogonal deployment phases: training-time LoRA routing for strong per-type correction vs. test-time adaptation for zero-cost deployment. A Meta-Brain + PDF pipeline is a natural combination.'}\n- {'id': '2603.05868', 'name': 'AnyCamVLA', 'role': \"Zero-shot camera adaptation via feed-forward novel view synthesis, achieving 94.5% under camera perturbations. Plug-and-play with no fine-tuning. Overlaps with LoRA-V's visual perturbation correction for camera viewpoints specifically. Meta-Brain's LoRA-V additionally handles lighting and background perturbations; AnyCamVLA is superior for camera-only deployment. Complementary visual-specific approach.\"}\n- {'id': '2512.07472', 'name': 'AFI', 'role': \"Primary spatial-perturbation competitor. Achieves +20.2% LIBERO-PRO via external 3D Spatial Affordance Fields on frozen π₀/π₀.₅. Provides the upper bound for spatial perturbation correction and the pivot target if LoRA-S proves insufficient. Meta-Brain is the internal, multi-perturbation complement to AFI's external, spatial-specific approach.\"}\n- {'id': '2506.09937', 'name': 'SAFE (NeurIPS 2025)', 'role': \"Foundational evidence that VLA internals encode task-generic execution signals extractable by lightweight probes. Uses 2-layer MLP (hidden 256) on final-layer activations, achieving 78.0% ROC-AUC for binary failure detection on unseen tasks with 2.3M parameters. Directly motivates PAR's architecture (identical MLP design, extended to multi-class) and Phase 0 validation protocol. SAFE detects failure; PAR classifies perturbation type and routes to correction.\"}\n- {'id': '2507.01843', 'name': 'MoIRA', 'role': 'Closest architectural analog — LoRA expert routing on π₀/GR00T-N1. Key difference: MoIRA routes by task instruction (text similarity); Meta-Brain routes by perturbation type (internal activation classification). Orthogonal routing dimensions.'}\n- {'id': '2512.02902', 'name': 'FTM/FLA', 'role': 'Strongest simplicity baseline. Achieves ~90% visual robustness with 4K parameters via token modulation. Meta-Brain must demonstrate value beyond FTM for visual perturbations AND justify the routing overhead by additionally handling spatial/physical perturbations.'}\n- {'id': '2603.05487', 'name': 'Feature Steering (Buurmeijer et al.)', 'role': 'Mechanistic evidence for internal correction feasibility. Linear interventions on π₀.₅/OpenVLA representations achieve ~100% constraint satisfaction for end-effector position and gripper state while maintaining >90% task success. Validates that LoRA-level corrections can manipulate spatial representations. Limitation: tested on standard tasks, not on rearranged-object scenarios — the harder spatial perturbation case remains empirically unvalidated.'}\n- {'id': '2502.04558', 'name': 'VLA Probing (Geier et al.)', 'role': 'Probing evidence: >0.90 accuracy for spatial object states/relations across LLM layers 1-32. Confirms spatial information is linearly encoded and accessible for correction.'}\n- {'id': '2603.19183', 'name': 'SAE-VLA', 'role': 'Sparse autoencoders reveal steerable motion primitives in VLA representations. Complementary evidence that VLA internals contain interpretable, controllable features beyond what linear probes capture.'}\n- {'id': '2510.00037', 'name': 'RobustVLA (ICLR 2026)', 'role': 'Multi-modal perturbation baseline. Achieves +12.6% on π₀ across 17 perturbation types via uniform adversarial training. Meta-Brain hypothesizes type-specific routing outperforms this uniform approach.'}\n- {'id': '2603.09298', 'name': 'CORAL', 'role': 'Task-based LoRA routing on frozen VLA. Demonstrates that per-task LoRA isolation outperforms joint fine-tuning. Motivates LoRA bank architecture but routes by task, not perturbation.'}\n- {'id': '2510.13626', 'name': 'LIBERO-Plus', 'role': 'Primary evaluation benchmark (CVPR 2026). Defines 7 perturbation categories for systematic VLA robustness evaluation. Current SOTA: SRPO 82.1%, VLA-GSE 81.2%, CorridorVLA 83.21% (by task category, not per-perturbation), OpenVLA-OFT+ 79.6%, AVA-VLA 74.7%, MergeVLA 72.2%, π₀ frozen baseline 53.6%.'}\n- {'id': '2510.03827', 'name': 'LIBERO-PRO', 'role': 'Secondary evaluation benchmark. Tests generalization across object positions, initial states, instructions, and environments.'}\n- {'id': '2511.09516', 'name': 'MAP-VLA', 'role': 'Memory-augmented VLA prompting using learnable soft prompts as prefix tokens, retrieved via trajectory similarity. Inspires Correction Memory concept but uses a different injection mechanism: MAP-VLA prepends retrieved prompts as prefix tokens; CM modulates router probability distributions via retrieval similarity. Both are plug-and-play on frozen backbones.'}\n- {'id': '2511.15605', 'name': 'SRPO', 'role': 'Current LIBERO-Plus SOTA at 82.1% (by perturbation category) via self-referential RL policy optimization using latent world model progress signals. Uses full RL training (not parameter-efficient), representing the upper bound for what VLA adaptation can achieve on this benchmark.'}\n- {'id': '2604.21241', 'name': 'CorridorVLA', 'role': \"Demonstrates explicit spatial constraints (anchor-defined corridors) can guide VLA action generation. GR00T-Corr achieves 83.21% on the LIBERO-Plus dataset, but reported by task category (Long 74.55%, Goal 85.75%, Object 88.4%, Spatial 84.14%) rather than by perturbation type (Camera/Robot/Light/Background/Noise/Layout), so direct per-perturbation comparison with VLA-GSE or Meta-Brain's target metrics is not straightforward. Evidence that spatial corrections at the action-planning level via explicit geometric constraints are feasible and effective.\"}\n- {'id': '2510.12276', 'name': 'Spatial Forcing (ICLR 2026)', 'role': 'Aligns intermediate VLA representations with 3D foundation model features during training, achieving 98.5% on standard LIBERO and 3.8× training speedup. Shows that spatial representation quality directly impacts action precision. Complementary training-time strategy; Meta-Brain operates post-hoc on frozen backbones.'}\n\n## Reviewer Evaluation\n\n**Scores**:\n  - clarity: **{'rationale': \"Exceptionally well-structured across all dimensions: comprehensive 17-reference landscape with per-competitor differentiation, clean ablation ladder with explicit falsification criteria and pivot strategies, honest framing of cross-backbone confounds (VLA-GSE comparison), detailed per-phase compute accounting, and the CM routing-modulation mechanism is now precisely specified. Among the clearest VLA robustness proposals I've reviewed.\", 'score': 5}**/5\n  - feasibility: **{'rationale': 'Phase 0 validation gate at Day 3-4 is excellent risk management. Tiered delivery (abstract needs only Phase 0 + LoRA results; Tier 3 deferred to camera-ready) provides realistic contingency. 190 H100-hrs with 4×H100 is tight but the compute math is internally consistent. The 2-day contingency buffer and pre-planned pivots (AFI hybrid for spatial, universal LoRA + CM if routing fails) demonstrate mature project management.', 'score': 4}**/5\n  - impact: **{'rationale': 'The routing principle (perturbation-type-specific correction > universal correction) is a useful design insight, but the target performance (72-80% on LIBERO-Plus) lands below current SOTA (SRPO 82.1%, CorridorVLA 83.21%, VLA-GSE 81.2%). The parameter efficiency argument (6M vs 114M) is strong but may not fully compensate for the absolute performance gap in reviewer reception. Sim-only evaluation is accepted at CoRL but limits practical impact claims.', 'score': 3}**/5\n  - novelty: **{'rationale': 'Perturbation-type-aware diagnostic routing is a genuinely new routing dimension, orthogonal to all existing work (task-based: MoIRA/CORAL, capacity-based: VLA-GSE, rank-based: LoRA-SP). The CM routing-modulation mechanism adds secondary novelty. Components are borrowed (SAFE-style probing, LoRA, MoE routing) but the combination and the specific hypothesis it tests are novel.', 'score': 4}**/5\n",
      "numLines": 142,
      "startLine": 1,
      "totalLines": 142
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_013afWKuzmavN5X6gSJ2pp8v`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/openpi_research_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "d671645d-8459-45b1-8a76-4568523d7cc4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGhEWQQmBS5AojnDVMs4gK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 315,
      "cache_read_input_tokens": 29103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 315
      },
      "output_tokens": 70,
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

_source line 24 · 2026-05-15T11:00:57.021Z_

<details><summary>↩ Tool result · `toolu_013afWKuzmavN5X6gSJ2pp8v`</summary>

````text
1	# OpenPI (π₀) Codebase 深度技术调研报告
2	
3	> 调研日期：2026-05-15
4	> 目标：评估在 π₀ 上实施 Meta-Brain LoRA Routing 的技术可行性
5	
6	---
7	
8	## 1. π₀ 模型架构与加载
9	
10	### 1.1 整体架构
11	
12	π₀ 是 Vision-Language-Action (VLA) flow model，基于 PaliGemma 2B VLM 扩展而来，采用 MoE-like 架构（Mixture of Tokens, MoT）。
13	
14	**核心组件**：
15	- **视觉编码器**: SigLIP So400m/14（~400M 参数）
16	- **语言模型 (PaliGemma backbone)**: Gemma 2B（~2.6B 参数）
17	- **动作专家 (Action Expert)**: Gemma 300M（~315M 参数，从零初始化）
18	- **投影层**: action_in_proj, action_out_proj, time MLPs
19	
20	**代码位置**:
21	- JAX 实现: `src/openpi/models/pi0.py` (Pi0 class, lines 47-176)
22	- PyTorch 实现: `src/openpi/models_pytorch/pi0_pytorch.py` (PI0Pytorch class)
23	- 配置: `src/openpi/models/pi0_config.py`
24	- Gemma 定义: `src/openpi/models/gemma.py` (JAX), `src/openpi/models_pytorch/gemma_pytorch.py` (PyTorch)
25	
26	### 1.2 详细架构参数
27	
28	| 组件 | 参数 | 值 |
29	|------|------|-----|
30	| **Gemma 2B (PaliGemma LLM)** | width (hidden_dim) | 2048 |
31	| | depth (层数) | **18** |
32	| | mlp_dim | 16,384 |
33	| | num_heads | 8 |
34	| | num_kv_heads | 1 (Multi-Query Attention) |
35	| | head_dim | 256 |
36	| **Gemma 300M (Action Expert)** | width | 1024 |
37	| | depth | **18** |
38	| | mlp_dim | 4,096 |
39	| | num_heads | 8 |
40	| | num_kv_heads | 1 |
41	| | head_dim | 256 |
42	| **SigLIP So400m/14** | embedding_dim | ~1152 |
43	| | patch_size | 14×14 |
44	| | input_resolution | 224×224 |
45	| | patches/image | 256 (16×16) |
46	
47	**来源**: `src/openpi/models/gemma.py` 中的 variant 定义:
48	```python
49	# gemma_2b: width=2048, depth=18, mlp_dim=16384, num_heads=8, num_kv_heads=1, head_dim=256
50	# gemma_300m: width=1024, depth=18, mlp_dim=4096, num_heads=8, num_kv_heads=1, head_dim=256
51	```
52	
53	### 1.3 注意力机制
54	
55	采用 block-wise causal masking（`src/openpi/models/pi0.py`, lines 20-38）:
56	- VLM block: 仅关注自身（prefix tokens: images + language）
57	- State/proprioception block: 关注自身 + VLM（共享 action expert 权重）
58	- Action block: 关注所有 tokens（完全双向）
59	
60	**来源**: `make_attn_mask()` 函数，通过 cumulative mask 实现不同的注意力模式。
61	
62	### 1.4 动作生成 (Flow Matching)
63	
64	**训练** (`compute_loss`, lines 119-150):
65	- 时间步 t ~ Beta(1.5, 1)，缩放到 [0.001, 0.999]
66	- 噪声状态: x_t = t·noise + (1-t)·actions
67	- 目标速度: u_t = noise - actions
68	- 损失: MSE(v_t, u_t)
69	
70	**推理** (`sample_actions`, lines 152-201):
71	- 10 步 Euler 积分: t=1 (噪声) → t=0 (目标)
72	- 步长: dt = -1/num_steps = -0.1
73	- 迭代: x_{t+dt} = x_t + dt·v_t
74	- 使用 KV-cache 优化 prefix tokens
75	
76	### 1.5 Checkpoint 来源与大小
77	
78	| Checkpoint | 来源 | 格式 |
79	|------------|------|------|
80	| pi0_base | `gs://openpi-assets/checkpoints/pi0_base/params` | JAX (Flax) |
81	| pi0_fast_base | `gs://openpi-assets/checkpoints/pi0_fast_base/params` | JAX (Flax) |
82	| pi05_base | `gs://openpi-assets/checkpoints/pi05_base/params` | JAX (Flax) |
83	| lerobot/pi0_base | HuggingFace Hub | SafeTensors (PyTorch) |
84	| lerobot/pi0_libero_base | HuggingFace Hub | SafeTensors (PyTorch) |
85	
86	**自动下载**：默认缓存到 `~/.cache/openpi`，可通过 `OPENPI_DATA_HOME` 修改。无需申请，直接公开下载。
87	
88	**模型大小**:
89	- 总参数量: ~3.3B（HuggingFace 标注为 4B，含 F32 精度下的 embeddings/projections）
90	- Checkpoint 大小 (fp32): ~13.2 GB
91	- Checkpoint 大小 (bf16): ~6.6 GB
92	
93	### 1.6 显存需求
94	
95	| 模式 | 显存需求 | 推荐 GPU |
96	|------|---------|----------|
97	| 推理 (bf16) | > 8 GB | RTX 4090 / A6000 |
98	| LoRA 微调 | > 22.5 GB | RTX 4090 / A6000 |
99	| 全量微调 | > 70 GB | A100 80GB / H100 |
100	
101	**来源**: OpenPI README 文档。
102	
103	### 1.7 加载方式
104	
105	**OpenPI 原生 (JAX)**:
106	```python
107	# src/openpi/training/config.py
108	model = config.model.create(model_rng)
109	# 通过 _load_weights_and_validate() 加载预训练权重
110	```
111	
112	**OpenPI PyTorch**:
113	```python
114	import openpi.models_pytorch.pi0_pytorch
115	import safetensors.torch
116	model = PI0Pytorch(model_cfg).to(device)
117	safetensors.torch.load_model(model, model_path)
118	```
119	
120	**LeRobot (HuggingFace)**:
121	```python
122	from lerobot.policies.pi0 import PI0Policy
123	policy = PI0Policy.from_pretrained("lerobot/pi0_base").to(device).eval()
124	```
125	
126	---
127	
128	## 2. LIBERO 环境集成
129	
130	### 2.1 已有 LIBERO 支持
131	
132	OpenPI 对 LIBERO 有**完整的一等支持**：
133	
134	**关键文件**:
135	- 评测脚本: `examples/libero/main.py`
136	- 数据转换: `examples/libero/convert_libero_data_to_lerobot.py`
137	- 策略映射: `src/openpi/policies/libero_policy.py`
138	- Docker 配置: `examples/libero/Dockerfile`, `examples/libero/compose.yml`
139	- 训练配置: `src/openpi/training/config.py` 中的 `LeRobotLiberoDataConfig`
140	
141	**预训练 LIBERO checkpoint**:
142	- `gs://openpi-assets/checkpoints/pi05_libero/params`（π₀.₅ LIBERO 微调版，96.85% 平均成功率）
143	- HuggingFace: `lerobot/pi0_libero_base`
144	
145	### 2.2 LIBERO 评测调用方式
146	
147	`examples/libero/main.py` 实现了完整的评测流程：
148	
149	1. 启动 Policy Server: `scripts/serve_policy.py`
150	2. 客户端通过 WebSocket 连接: `WebsocketClientPolicy(host, port)`
151	3. 评测循环:
152	   - 重置环境 → 等待物体稳定 (num_steps_wait)
153	   - 每 `replan_steps=5` 步请求新 action chunk
154	   - 记录成功率和视频
155	
156	**配置格式** (通过命令行参数):
157	- `--task_suite_name`: LIBERO 任务套件 (spatial/object/goal/10)
158	- `--num_trials_per_task`: 每个任务的试验次数 (默认 50)
159	- `--resize_size`: 图像分辨率 (224)
160	- `SERVER_ARGS`: 指定 checkpoint
161	
162	**观测格式** (LiberoInputs, `src/openpi/policies/libero_policy.py`):
163	- State: `observation/state` — 8 维向量（end-effector position + rotation + gripper）
164	- Base image: `observation/image` — 224×224 RGB（第三人称）
165	- Wrist image: `observation/wrist_image` — 224×224 RGB（左手腕相机）
166	- Right wrist: 零填充（LIBERO 只有 2 个相机）
167	
168	**动作格式** (LiberoOutputs):
169	- 输出前 7 维动作（从 action_dim=32 的填充中截取）
170	- 7 维 = 6-DoF end-effector + 1 gripper
171	
172	### 2.3 LIBERO-Plus 扰动评测
173	
174	**支持状态**: 可用，但需要额外安装 LIBERO-Plus 替代标准 LIBERO。
175	
176	**LIBERO-Plus** (https://github.com/sylvestf/LIBERO-plus) 提供 7 个扰动维度:
177	1. 物体布局 (Objects Layout)
178	2. 相机视角 (Camera Viewpoints)
179	3. 机器人初始状态 (Robot Initial States)
180	4. 语言指令 (Language Instructions)
181	5. 光照条件 (Light Conditions)
182	6. 背景纹理 (Background Textures)
183	7. 传感器噪声 (Sensor Noise)
184	
185	**集成方式**: "Simply replace the originally installed LIBERO repository with our repository without modifying your code" — 直接替换 LIBERO 库即可，评测代码无需修改。唯一改动: `num_trials_per_task` 从 50 改为 1。
186	
187	**π₀ 在 LIBERO-Plus 上的基线表现**: 平均 53.6%（光照 85.0%，背景 81.4%，但机器人初始状态仅 6.0%）。
188	
189	---
190	
191	## 3. LoRA Fine-tuning 支持
192	
193	### 3.1 JAX 实现 — 已有完整支持
194	
195	**代码位置**: `src/openpi/models/lora.py`
196	
197	**LoRA 变体定义** (`src/openpi/models/gemma.py`):
198	```
199	gemma_2b_lora:    rank=16, alpha=16.0 (attn + ffn)
200	gemma_300m_lora:  rank=32, alpha=32.0 (attn + ffn)
201	```
202	
203	**训练配置** (`src/openpi/training/config.py`):
204	- 使用 `paligemma_variant="gemma_2b_lora"` + `action_expert_variant="gemma_300m_lora"`
205	- Freeze filter: 冻结非 LoRA 的 LLM 参数，仅训练 LoRA 权重
206	- EMA decay: 禁用 (`ema_decay=None`)
207	- 其他默认: 30k steps, batch_size=32, AdamW + Cosine Decay
208	
209	**LoRA 目标模块**:
210	- Attention: q_proj, k_proj, v_proj, o_proj (通过 Einsum 类)
211	- FFN: gate_proj, up_proj, down_proj (通过 FeedForward 类)
212	
213	**LoRA 实现特点**:
214	- 支持 RSLoRA (rank-stabilized LoRA): `scaling = alpha / sqrt(rank)`
215	- 纯 additive: `output = base_output + (x @ w_a @ w_b) * scaling`
216	- 不依赖外部库（如 peft），自实现
217	
218	### 3.2 PyTorch 实现 — 官方不支持，社区有方案
219	
220	**官方状态**: OpenPI 的 PyTorch 训练脚本 (`scripts/train_pytorch.py`) **不支持 LoRA**，仅支持全量微调。
221	
222	**社区方案** (Issue #842):
223	- 纯 PyTorch LoRA 实现，不依赖 peft
224	- 注入到 Attention (q/k/v/o_proj) 和 MLP (gate/up/down_proj)
225	- Rank=16 时 LoRA 参数: 26.5M (0.73% of total)
226	- 可选解冻 Vision Encoder: 额外 412M trainable (12.11% total)
227	- 单 RTX 4090 可训练，~16GB 峰值显存
228	- LIBERO 上达到 96.95% 平均成功率
229	- **状态**: PR 未合并，但代码完整可用
230	
231	**LeRobot 方案**:
232	- HuggingFace LeRobot 提供了 Pi0 的 PyTorch 训练脚本
233	- 支持 `train_expert_only=true` 冻结 VLM 仅训练 action expert
234	- 不原生支持 LoRA，但可通过 HuggingFace PEFT 库扩展
235	
236	### 3.3 推荐方案
237	
238	对于本项目的 Meta-Brain LoRA Routing：
239	1. **首选**: 基于 OpenPI JAX 实现，已有完整 LoRA 支持
240	2. **备选**: 采用 Issue #842 的 PyTorch LoRA 实现（更灵活，更容易加 hook）
241	3. **替代**: 使用 LeRobot PyTorch + HuggingFace PEFT 库
242	
243	---
244	
245	## 4. 中间层激活提取
246	
247	### 4.1 模型前向传播路径
248	
249	**JAX 实现** (`src/openpi/models/pi0.py`):
250	```
251	Pi0.__call__()
252	  → embed_prefix(obs)        # SigLIP 编码图像 + tokenize 文本
253	  → embed_suffix(obs, noisy_actions, timestep)  # 编码动作 + 时间步
254	  → self.PaliGemma['llm'](tokens, ...)  # Gemma Module forward (18 layers)
255	  → action_out_proj(...)     # 投影到动作空间
256	```
257	
258	**PyTorch 实现** (`src/openpi/models_pytorch/pi0_pytorch.py`):
259	```
260	PI0Pytorch.forward(observation, actions)
261	  → _preprocess_observation()
262	  → embed_prefix(obs)
263	  → embed_suffix(obs, noisy_actions, timestep)
264	  → paligemma_with_expert(tokens, ...)
265	  → action_out_proj(...)
266	```
267	
268	### 4.2 已有 Hook 机制
269	
270	**OpenPI 没有已有的 hook 机制或中间层输出接口。** 需要自行添加。
271	
272	### 4.3 PyTorch Hook 注册方案（推荐）
273	
274	PyTorch 实现支持标准的 `register_forward_hook`，模块路径如下：
275	
276	**PaliGemma LLM 层 (hidden_dim=2048)**:
277	```python
278	model.paligemma_with_expert.paligemma.language_model.layers[i]
279	# i = 0..17 (共 18 层)
280	
281	# 子模块:
282	model.paligemma_with_expert.paligemma.language_model.layers[i].self_attn
283	model.paligemma_with_expert.paligemma.language_model.layers[i].self_attn.q_proj
284	model.paligemma_with_expert.paligemma.language_model.layers[i].self_attn.o_proj
285	model.paligemma_with_expert.paligemma.language_model.layers[i].mlp
286	model.paligemma_with_expert.paligemma.language_model.layers[i].input_layernorm
287	model.paligemma_with_expert.paligemma.language_model.layers[i].post_attention_layernorm
288	```
289	
290	**Action Expert 层 (hidden_dim=1024)**:
291	```python
292	model.paligemma_with_expert.gemma_expert.model.layers[i]
293	# i = 0..17 (共 18 层)
294	# 子模块结构同上
295	```
296	
297	**Vision Encoder 层**:
298	```python
299	model.paligemma_with_expert.paligemma.vision_tower.layers[i]
300	```
301	
302	### 4.4 关键发现：层数只有 18，不是 32！
303	
304	**⚠️ 重要**: π₀ 的 Transformer 深度为 **18 层**（layers[0]..layers[17]），而非 32 层。
305	
306	用户原计划提取 layers {4,8,12,16,20,24,28,32} — **其中 layers 20,24,28,32 不存在**。
307	
308	**推荐调整方案**:
309	| 原计划 | 可行方案 A (8 层均匀采样) | 可行方案 B (偏重深层) |
310	|--------|--------------------------|---------------------|
311	| {4,8,12,16,20,24,28,32} | {1,3,5,7,9,11,13,15} | {2,4,6,8,10,12,14,16} |
312	
313	**或者同时提取两个 Expert 的激活**（获得更丰富的信息）:
314	- PaliGemma layers: {2, 5, 8, 11, 14, 17}
315	- Action Expert layers: {2, 5, 8, 11, 14, 17}
316	- 共 12 层激活，覆盖两个 transformer
317	
318	### 4.5 Hook 实现代码示例
319	
320	```python
321	class ActivationExtractor:
322	    def __init__(self, model, layer_indices):
323	        self.activations = {}
324	        self.hooks = []
325	        
326	        for idx in layer_indices:
327	            # Hook PaliGemma LLM layers
328	            layer = model.paligemma_with_expert.paligemma.language_model.layers[idx]
329	            handle = layer.register_forward_hook(
330	                lambda module, input, output, idx=idx: 
331	                    self.activations.__setitem__(f'llm_layer_{idx}', output[0].detach())
332	            )
333	            self.hooks.append(handle)
334	            
335	            # Hook Action Expert layers
336	            expert_layer = model.paligemma_with_expert.gemma_expert.model.layers[idx]
337	            handle = expert_layer.register_forward_hook(
338	                lambda module, input, output, idx=idx:
339	                    self.activations.__setitem__(f'expert_layer_{idx}', output[0].detach())
340	            )
341	            self.hooks.append(handle)
342	    
343	    def remove_hooks(self):
344	        for h in self.hooks:
345	            h.remove()
346	```
347	
348	---
349	
350	## 5. 技术估算
351	
352	### 5.1 序列长度分析
353	
354	LIBERO 评测时的 token 构成：
355	| 组件 | Tokens | 说明 |
356	|------|--------|------|
357	| Base image | 256 | 224×224 / 14×14 patches |
358	| Left wrist image | 256 | 224×224 / 14×14 patches |
359	| Right wrist image | 256 | 零填充（LIBERO 只有 2 相机），但仍占序列位置 |
360	| Text prompt | 48 | max_token_len (pi0 默认) |
361	| State | 1 | 投影到 hidden_dim |
362	| Action tokens | 50 | action_horizon=50 |
363	| **Total** | **~867** | |
364	
365	### 5.2 每条 Rollout 激活存储估算
366	
367	**假设条件**:
368	- 8 层采样（PaliGemma LLM 层）
369	- hidden_dim = 2048 (PaliGemma)
370	- seq_len ≈ 867
371	- replan_steps = 5，每 5 个 env step 做一次推理
372	- 每 episode 约 200-400 env steps → ~40-80 次推理
373	
374	**方案 A: 存储完整序列激活 (fp32)**
375	
376	| 指标 | 值 |
377	|------|-----|
378	| 每次推理每层 | 2048 × 867 × 4 bytes = 7.1 MB |
379	| 每次推理 8 层 | 56.8 MB |
380	| 每 episode (60 次推理) | 3.4 GB |
381	| 500 episodes | **1.7 TB** |
382	
383	**方案 B: 仅存储 action token 位置的激活 (fp32)**
384	
385	| 指标 | 值 |
386	|------|-----|
387	| 每次推理每层 | 2048 × 50 × 4 bytes = 0.41 MB |
388	| 每次推理 8 层 | 3.3 MB |
389	| 每 episode (60 次推理) | 197 MB |
390	| 500 episodes | **96 GB** |
391	
392	**方案 C: Action tokens + fp16**
393	
394	| 指标 | 值 |
395	|------|-----|
396	| 每次推理 8 层 | 1.6 MB |
397	| 每 episode (60 次推理) | 98 MB |
398	| 500 episodes | **48 GB** |
399	
400	**方案 D: 池化后的层表征 (mean pooling over seq_len, fp16)**
401	
402	| 指标 | 值 |
403	|------|-----|
404	| 每次推理每层 | 2048 × 2 bytes = 4 KB |
405	| 每次推理 8 层 | 32 KB |
406	| 每 episode (60 次推理) | 1.9 MB |
407	| 500 episodes | **0.95 GB** |
408	
409	### 5.3 推理速度估算
410	
411	**来源**: π₀ 论文 (Table 4) 在 RTX 4090 上的测量:
412	- Image encoding: 14 ms
413	- Observation forward pass: 32 ms
414	- 10× action flow passes: 27 ms
415	- **单次推理总计**: 73 ms
416	
417	**H100 估算** (约 2× 4090 推理性能):
418	- 单次推理: ~35-40 ms
419	- 每 episode (60 次推理): ~2.4 s（纯模型推理时间）
420	- 加上环境仿真时间: 每 episode 约 30-60 秒
421	- **500 episodes 总时间**: ~4-8 小时（单 H100）
422	
423	**注意**: 如果需要存储激活，推理时需额外内存存储 hook 输出，峰值显存约增加 50-100 MB。
424	
425	### 5.4 训练资源估算
426	
427	**LoRA 微调 500 episodes 数据**:
428	- 数据: 500 episodes × ~200 steps × 7-dim action = ~70K 训练样本
429	- 训练时间 (单 A6000/4090): 10k-30k steps × ~0.5s/step ≈ 1.4-4.2 小时
430	- 显存: ~16-22 GB (LoRA)
431	
432	---
433	
434	## 6. 风险与阻塞项
435	
436	### 6.1 高风险项
437	
438	| 风险 | 严重性 | 说明 | 缓解方案 |
439	|------|--------|------|----------|
440	| **层数不匹配** | 🔴 高 | 模型仅 18 层，原计划 8 层采样中有 4 层不存在 | 调整为 {2,4,6,8,10,12,14,16} |
441	| **PyTorch LoRA 未官方支持** | 🟡 中 | PyTorch 训练不原生支持 LoRA，需用社区方案或自实现 | 采用 Issue #842 的实现，或用 JAX 训练 + PyTorch 推理 |
442	| **激活存储量大** | 🟡 中 | 完整序列存储 500 episodes 需 1.7TB | 使用方案 B/C/D 减少存储 |
443	
444	### 6.2 中等风险项
445	
446	| 风险 | 说明 | 缓解方案 |
447	|------|------|----------|
448	| JAX vs PyTorch 精度差异 | LeRobot PyTorch 转换后性能有下降，官方建议微调 | 可用 JAX checkpoint 作为 baseline 对比 |
449	| Flow matching 推理开销 | 每次推理需要 10 步迭代去噪 | 已有 KV-cache 优化，单次 73ms 可接受 |
450	| LIBERO-Plus 集成 | 需要替换 LIBERO 库，可能有版本兼容问题 | 使用 Docker 隔离环境 |
451	
452	### 6.3 非阻塞项
453	
454	- Checkpoint 下载: 公开可用，无需申请
455	- 数据转换: 已有 LeRobot 格式转换脚本
456	- 评测脚本: 完整可用，包含 Docker 配置
457	- 多 GPU 支持: PyTorch DDP 已实现
458	
459	---
460	
461	## 7. 推荐技术方案
462	
463	### 7.1 总体架构
464	
465	```
466	[LIBERO Env] → [π₀ with Hooks] → [Activation Buffer]
467	                     ↓                    ↓
468	              [Action Output]    [Meta-Brain Router]
469	                                        ↓
470	                                 [LoRA Selection]
471	                                        ↓
472	                               [Task-Specific LoRA]
473	```
474	
475	### 7.2 具体步骤
476	
477	**Phase 1: 基础设施搭建**
478	1. 安装 OpenPI (PyTorch 版) + LIBERO 环境
479	2. 验证 `lerobot/pi0_base` 或 `pi0_libero_base` checkpoint 加载
480	3. 运行标准 LIBERO 评测确认 baseline 性能
481	
482	**Phase 2: 激活提取**
483	1. 在 PyTorch 模型上注册 forward hooks
484	2. 选择层: PaliGemma layers {2,4,6,8,10,12,14,16}
485	3. 使用方案 B (action tokens only, fp16): 每 500 episodes ~48 GB
486	4. 收集 LIBERO 全 4 个 task suite 的激活
487	
488	**Phase 3: LoRA 训练**
489	1. 基于 Issue #842 的 PyTorch LoRA 实现
490	2. 或使用 JAX 原生 LoRA 训练 (gemma_2b_lora + gemma_300m_lora)
491	3. 每个 task suite 训练一个 LoRA adapter
492	4. LoRA config: rank=16, alpha=16.0, target=attn+ffn
493	
494	**Phase 4: Meta-Brain Router**
495	1. 输入: 中间层激活 (8 layers × hidden_dim)
496	2. 输出: LoRA adapter 选择/混合权重
497	3. 训练: 使用收集的激活-任务标签对
498	
499	### 7.3 硬件需求
500	
501	| 阶段 | GPU 需求 | 时间估算 |
502	|------|---------|---------|
503	| LIBERO 评测 + 激活收集 | 1× H100/A100 | ~8 小时 |
504	| LoRA 训练 (4 adapters) | 1× A6000/4090 | ~16 小时 |
505	| Meta-Brain Router 训练 | 1× A6000 | ~2 小时 |
506	| 总磁盘 | ~100 GB (激活) + ~10 GB (checkpoints) | |
507	
508	---
509	
510	## 8. 关键代码引用索引
511	
512	| 内容 | 文件路径 | 说明 |
513	|------|---------|------|
514	| Pi0 模型定义 (JAX) | `src/openpi/models/pi0.py:47-176` | Pi0 class, forward/loss/sample |
515	| Pi0 模型定义 (PyTorch) | `src/openpi/models_pytorch/pi0_pytorch.py` | PI0Pytorch class |
516	| Gemma 变体配置 | `src/openpi/models/gemma.py` | width/depth/heads 定义 |
517	| Gemma PyTorch | `src/openpi/models_pytorch/gemma_pytorch.py` | GemmaForCausalLM 层结构 |
518	| LoRA 实现 (JAX) | `src/openpi/models/lora.py` | Einsum, FeedForward adapters |
519	| 模型配置 | `src/openpi/models/pi0_config.py` | Pi0Config dataclass |
520	| 训练配置 | `src/openpi/training/config.py` | TrainConfig, LIBERO 数据配置 |
521	| 训练脚本 (JAX) | `scripts/train.py` | JAX 训练循环 |
522	| 训练脚本 (PyTorch) | `scripts/train_pytorch.py` | PyTorch 训练循环 |
523	| LIBERO 策略映射 | `src/openpi/policies/libero_policy.py` | LiberoInputs/Outputs |
524	| LIBERO 评测 | `examples/libero/main.py` | 完整评测流程 |
525	| 数据转换 | `examples/libero/convert_libero_data_to_lerobot.py` | LIBERO → LeRobot |
526	| SigLIP 视觉编码器 | `src/openpi/models/siglip.py` | So400m/14 ViT |
527	| 注意力 mask | `src/openpi/models/pi0.py:20-38` | make_attn_mask() |
528	| Flow matching | `src/openpi/models/pi0.py:119-150` | compute_loss() |
529	| 推理采样 | `src/openpi/models/pi0.py:152-201` | sample_actions() |
530	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "1d4a9ff7-36de-46dd-9f2a-81e64ae1302b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/openpi_research_report.md",
      "content": "# OpenPI (π₀) Codebase 深度技术调研报告\n\n> 调研日期：2026-05-15\n> 目标：评估在 π₀ 上实施 Meta-Brain LoRA Routing 的技术可行性\n\n---\n\n## 1. π₀ 模型架构与加载\n\n### 1.1 整体架构\n\nπ₀ 是 Vision-Language-Action (VLA) flow model，基于 PaliGemma 2B VLM 扩展而来，采用 MoE-like 架构（Mixture of Tokens, MoT）。\n\n**核心组件**：\n- **视觉编码器**: SigLIP So400m/14（~400M 参数）\n- **语言模型 (PaliGemma backbone)**: Gemma 2B（~2.6B 参数）\n- **动作专家 (Action Expert)**: Gemma 300M（~315M 参数，从零初始化）\n- **投影层**: action_in_proj, action_out_proj, time MLPs\n\n**代码位置**:\n- JAX 实现: `src/openpi/models/pi0.py` (Pi0 class, lines 47-176)\n- PyTorch 实现: `src/openpi/models_pytorch/pi0_pytorch.py` (PI0Pytorch class)\n- 配置: `src/openpi/models/pi0_config.py`\n- Gemma 定义: `src/openpi/models/gemma.py` (JAX), `src/openpi/models_pytorch/gemma_pytorch.py` (PyTorch)\n\n### 1.2 详细架构参数\n\n| 组件 | 参数 | 值 |\n|------|------|-----|\n| **Gemma 2B (PaliGemma LLM)** | width (hidden_dim) | 2048 |\n| | depth (层数) | **18** |\n| | mlp_dim | 16,384 |\n| | num_heads | 8 |\n| | num_kv_heads | 1 (Multi-Query Attention) |\n| | head_dim | 256 |\n| **Gemma 300M (Action Expert)** | width | 1024 |\n| | depth | **18** |\n| | mlp_dim | 4,096 |\n| | num_heads | 8 |\n| | num_kv_heads | 1 |\n| | head_dim | 256 |\n| **SigLIP So400m/14** | embedding_dim | ~1152 |\n| | patch_size | 14×14 |\n| | input_resolution | 224×224 |\n| | patches/image | 256 (16×16) |\n\n**来源**: `src/openpi/models/gemma.py` 中的 variant 定义:\n```python\n# gemma_2b: width=2048, depth=18, mlp_dim=16384, num_heads=8, num_kv_heads=1, head_dim=256\n# gemma_300m: width=1024, depth=18, mlp_dim=4096, num_heads=8, num_kv_heads=1, head_dim=256\n```\n\n### 1.3 注意力机制\n\n采用 block-wise causal masking（`src/openpi/models/pi0.py`, lines 20-38）:\n- VLM block: 仅关注自身（prefix tokens: images + language）\n- State/proprioception block: 关注自身 + VLM（共享 action expert 权重）\n- Action block: 关注所有 tokens（完全双向）\n\n**来源**: `make_attn_mask()` 函数，通过 cumulative mask 实现不同的注意力模式。\n\n### 1.4 动作生成 (Flow Matching)\n\n**训练** (`compute_loss`, lines 119-150):\n- 时间步 t ~ Beta(1.5, 1)，缩放到 [0.001, 0.999]\n- 噪声状态: x_t = t·noise + (1-t)·actions\n- 目标速度: u_t = noise - actions\n- 损失: MSE(v_t, u_t)\n\n**推理** (`sample_actions`, lines 152-201):\n- 10 步 Euler 积分: t=1 (噪声) → t=0 (目标)\n- 步长: dt = -1/num_steps = -0.1\n- 迭代: x_{t+dt} = x_t + dt·v_t\n- 使用 KV-cache 优化 prefix tokens\n\n### 1.5 Checkpoint 来源与大小\n\n| Checkpoint | 来源 | 格式 |\n|------------|------|------|\n| pi0_base | `gs://openpi-assets/checkpoints/pi0_base/params` | JAX (Flax) |\n| pi0_fast_base | `gs://openpi-assets/checkpoints/pi0_fast_base/params` | JAX (Flax) |\n| pi05_base | `gs://openpi-assets/checkpoints/pi05_base/params` | JAX (Flax) |\n| lerobot/pi0_base | HuggingFace Hub | SafeTensors (PyTorch) |\n| lerobot/pi0_libero_base | HuggingFace Hub | SafeTensors (PyTorch) |\n\n**自动下载**：默认缓存到 `~/.cache/openpi`，可通过 `OPENPI_DATA_HOME` 修改。无需申请，直接公开下载。\n\n**模型大小**:\n- 总参数量: ~3.3B（HuggingFace 标注为 4B，含 F32 精度下的 embeddings/projections）\n- Checkpoint 大小 (fp32): ~13.2 GB\n- Checkpoint 大小 (bf16): ~6.6 GB\n\n### 1.6 显存需求\n\n| 模式 | 显存需求 | 推荐 GPU |\n|------|---------|----------|\n| 推理 (bf16) | > 8 GB | RTX 4090 / A6000 |\n| LoRA 微调 | > 22.5 GB | RTX 4090 / A6000 |\n| 全量微调 | > 70 GB | A100 80GB / H100 |\n\n**来源**: OpenPI README 文档。\n\n### 1.7 加载方式\n\n**OpenPI 原生 (JAX)**:\n```python\n# src/openpi/training/config.py\nmodel = config.model.create(model_rng)\n# 通过 _load_weights_and_validate() 加载预训练权重\n```\n\n**OpenPI PyTorch**:\n```python\nimport openpi.models_pytorch.pi0_pytorch\nimport safetensors.torch\nmodel = PI0Pytorch(model_cfg).to(device)\nsafetensors.torch.load_model(model, model_path)\n```\n\n**LeRobot (HuggingFace)**:\n```python\nfrom lerobot.policies.pi0 import PI0Policy\npolicy = PI0Policy.from_pretrained(\"lerobot/pi0_base\").to(device).eval()\n```\n\n---\n\n## 2. LIBERO 环境集成\n\n### 2.1 已有 LIBERO 支持\n\nOpenPI 对 LIBERO 有**完整的一等支持**：\n\n**关键文件**:\n- 评测脚本: `examples/libero/main.py`\n- 数据转换: `examples/libero/convert_libero_data_to_lerobot.py`\n- 策略映射: `src/openpi/policies/libero_policy.py`\n- Docker 配置: `examples/libero/Dockerfile`, `examples/libero/compose.yml`\n- 训练配置: `src/openpi/training/config.py` 中的 `LeRobotLiberoDataConfig`\n\n**预训练 LIBERO checkpoint**:\n- `gs://openpi-assets/checkpoints/pi05_libero/params`（π₀.₅ LIBERO 微调版，96.85% 平均成功率）\n- HuggingFace: `lerobot/pi0_libero_base`\n\n### 2.2 LIBERO 评测调用方式\n\n`examples/libero/main.py` 实现了完整的评测流程：\n\n1. 启动 Policy Server: `scripts/serve_policy.py`\n2. 客户端通过 WebSocket 连接: `WebsocketClientPolicy(host, port)`\n3. 评测循环:\n   - 重置环境 → 等待物体稳定 (num_steps_wait)\n   - 每 `replan_steps=5` 步请求新 action chunk\n   - 记录成功率和视频\n\n**配置格式** (通过命令行参数):\n- `--task_suite_name`: LIBERO 任务套件 (spatial/object/goal/10)\n- `--num_trials_per_task`: 每个任务的试验次数 (默认 50)\n- `--resize_size`: 图像分辨率 (224)\n- `SERVER_ARGS`: 指定 checkpoint\n\n**观测格式** (LiberoInputs, `src/openpi/policies/libero_policy.py`):\n- State: `observation/state` — 8 维向量（end-effector position + rotation + gripper）\n- Base image: `observation/image` — 224×224 RGB（第三人称）\n- Wrist image: `observation/wrist_image` — 224×224 RGB（左手腕相机）\n- Right wrist: 零填充（LIBERO 只有 2 个相机）\n\n**动作格式** (LiberoOutputs):\n- 输出前 7 维动作（从 action_dim=32 的填充中截取）\n- 7 维 = 6-DoF end-effector + 1 gripper\n\n### 2.3 LIBERO-Plus 扰动评测\n\n**支持状态**: 可用，但需要额外安装 LIBERO-Plus 替代标准 LIBERO。\n\n**LIBERO-Plus** (https://github.com/sylvestf/LIBERO-plus) 提供 7 个扰动维度:\n1. 物体布局 (Objects Layout)\n2. 相机视角 (Camera Viewpoints)\n3. 机器人初始状态 (Robot Initial States)\n4. 语言指令 (Language Instructions)\n5. 光照条件 (Light Conditions)\n6. 背景纹理 (Background Textures)\n7. 传感器噪声 (Sensor Noise)\n\n**集成方式**: \"Simply replace the originally installed LIBERO repository with our repository without modifying your code\" — 直接替换 LIBERO 库即可，评测代码无需修改。唯一改动: `num_trials_per_task` 从 50 改为 1。\n\n**π₀ 在 LIBERO-Plus 上的基线表现**: 平均 53.6%（光照 85.0%，背景 81.4%，但机器人初始状态仅 6.0%）。\n\n---\n\n## 3. LoRA Fine-tuning 支持\n\n### 3.1 JAX 实现 — 已有完整支持\n\n**代码位置**: `src/openpi/models/lora.py`\n\n**LoRA 变体定义** (`src/openpi/models/gemma.py`):\n```\ngemma_2b_lora:    rank=16, alpha=16.0 (attn + ffn)\ngemma_300m_lora:  rank=32, alpha=32.0 (attn + ffn)\n```\n\n**训练配置** (`src/openpi/training/config.py`):\n- 使用 `paligemma_variant=\"gemma_2b_lora\"` + `action_expert_variant=\"gemma_300m_lora\"`\n- Freeze filter: 冻结非 LoRA 的 LLM 参数，仅训练 LoRA 权重\n- EMA decay: 禁用 (`ema_decay=None`)\n- 其他默认: 30k steps, batch_size=32, AdamW + Cosine Decay\n\n**LoRA 目标模块**:\n- Attention: q_proj, k_proj, v_proj, o_proj (通过 Einsum 类)\n- FFN: gate_proj, up_proj, down_proj (通过 FeedForward 类)\n\n**LoRA 实现特点**:\n- 支持 RSLoRA (rank-stabilized LoRA): `scaling = alpha / sqrt(rank)`\n- 纯 additive: `output = base_output + (x @ w_a @ w_b) * scaling`\n- 不依赖外部库（如 peft），自实现\n\n### 3.2 PyTorch 实现 — 官方不支持，社区有方案\n\n**官方状态**: OpenPI 的 PyTorch 训练脚本 (`scripts/train_pytorch.py`) **不支持 LoRA**，仅支持全量微调。\n\n**社区方案** (Issue #842):\n- 纯 PyTorch LoRA 实现，不依赖 peft\n- 注入到 Attention (q/k/v/o_proj) 和 MLP (gate/up/down_proj)\n- Rank=16 时 LoRA 参数: 26.5M (0.73% of total)\n- 可选解冻 Vision Encoder: 额外 412M trainable (12.11% total)\n- 单 RTX 4090 可训练，~16GB 峰值显存\n- LIBERO 上达到 96.95% 平均成功率\n- **状态**: PR 未合并，但代码完整可用\n\n**LeRobot 方案**:\n- HuggingFace LeRobot 提供了 Pi0 的 PyTorch 训练脚本\n- 支持 `train_expert_only=true` 冻结 VLM 仅训练 action expert\n- 不原生支持 LoRA，但可通过 HuggingFace PEFT 库扩展\n\n### 3.3 推荐方案\n\n对于本项目的 Meta-Brain LoRA Routing：\n1. **首选**: 基于 OpenPI JAX 实现，已有完整 LoRA 支持\n2. **备选**: 采用 Issue #842 的 PyTorch LoRA 实现（更灵活，更容易加 hook）\n3. **替代**: 使用 LeRobot PyTorch + HuggingFace PEFT 库\n\n---\n\n## 4. 中间层激活提取\n\n### 4.1 模型前向传播路径\n\n**JAX 实现** (`src/openpi/models/pi0.py`):\n```\nPi0.__call__()\n  → embed_prefix(obs)        # SigLIP 编码图像 + tokenize 文本\n  → embed_suffix(obs, noisy_actions, timestep)  # 编码动作 + 时间步\n  → self.PaliGemma['llm'](tokens, ...)  # Gemma Module forward (18 layers)\n  → action_out_proj(...)     # 投影到动作空间\n```\n\n**PyTorch 实现** (`src/openpi/models_pytorch/pi0_pytorch.py`):\n```\nPI0Pytorch.forward(observation, actions)\n  → _preprocess_observation()\n  → embed_prefix(obs)\n  → embed_suffix(obs, noisy_actions, timestep)\n  → paligemma_with_expert(tokens, ...)\n  → action_out_proj(...)\n```\n\n### 4.2 已有 Hook 机制\n\n**OpenPI 没有已有的 hook 机制或中间层输出接口。** 需要自行添加。\n\n### 4.3 PyTorch Hook 注册方案（推荐）\n\nPyTorch 实现支持标准的 `register_forward_hook`，模块路径如下：\n\n**PaliGemma LLM 层 (hidden_dim=2048)**:\n```python\nmodel.paligemma_with_expert.paligemma.language_model.layers[i]\n# i = 0..17 (共 18 层)\n\n# 子模块:\nmodel.paligemma_with_expert.paligemma.language_model.layers[i].self_attn\nmodel.paligemma_with_expert.paligemma.language_model.layers[i].self_attn.q_proj\nmodel.paligemma_with_expert.paligemma.language_model.layers[i].self_attn.o_proj\nmodel.paligemma_with_expert.paligemma.language_model.layers[i].mlp\nmodel.paligemma_with_expert.paligemma.language_model.layers[i].input_layernorm\nmodel.paligemma_with_expert.paligemma.language_model.layers[i].post_attention_layernorm\n```\n\n**Action Expert 层 (hidden_dim=1024)**:\n```python\nmodel.paligemma_with_expert.gemma_expert.model.layers[i]\n# i = 0..17 (共 18 层)\n# 子模块结构同上\n```\n\n**Vision Encoder 层**:\n```python\nmodel.paligemma_with_expert.paligemma.vision_tower.layers[i]\n```\n\n### 4.4 关键发现：层数只有 18，不是 32！\n\n**⚠️ 重要**: π₀ 的 Transformer 深度为 **18 层**（layers[0]..layers[17]），而非 32 层。\n\n用户原计划提取 layers {4,8,12,16,20,24,28,32} — **其中 layers 20,24,28,32 不存在**。\n\n**推荐调整方案**:\n| 原计划 | 可行方案 A (8 层均匀采样) | 可行方案 B (偏重深层) |\n|--------|--------------------------|---------------------|\n| {4,8,12,16,20,24,28,32} | {1,3,5,7,9,11,13,15} | {2,4,6,8,10,12,14,16} |\n\n**或者同时提取两个 Expert 的激活**（获得更丰富的信息）:\n- PaliGemma layers: {2, 5, 8, 11, 14, 17}\n- Action Expert layers: {2, 5, 8, 11, 14, 17}\n- 共 12 层激活，覆盖两个 transformer\n\n### 4.5 Hook 实现代码示例\n\n```python\nclass ActivationExtractor:\n    def __init__(self, model, layer_indices):\n        self.activations = {}\n        self.hooks = []\n        \n        for idx in layer_indices:\n            # Hook PaliGemma LLM layers\n            layer = model.paligemma_with_expert.paligemma.language_model.layers[idx]\n            handle = layer.register_forward_hook(\n                lambda module, input, output, idx=idx: \n                    self.activations.__setitem__(f'llm_layer_{idx}', output[0].detach())\n            )\n            self.hooks.append(handle)\n            \n            # Hook Action Expert layers\n            expert_layer = model.paligemma_with_expert.gemma_expert.model.layers[idx]\n            handle = expert_layer.register_forward_hook(\n                lambda module, input, output, idx=idx:\n                    self.activations.__setitem__(f'expert_layer_{idx}', output[0].detach())\n            )\n            self.hooks.append(handle)\n    \n    def remove_hooks(self):\n        for h in self.hooks:\n            h.remove()\n```\n\n---\n\n## 5. 技术估算\n\n### 5.1 序列长度分析\n\nLIBERO 评测时的 token 构成：\n| 组件 | Tokens | 说明 |\n|------|--------|------|\n| Base image | 256 | 224×224 / 14×14 patches |\n| Left wrist image | 256 | 224×224 / 14×14 patches |\n| Right wrist image | 256 | 零填充（LIBERO 只有 2 相机），但仍占序列位置 |\n| Text prompt | 48 | max_token_len (pi0 默认) |\n| State | 1 | 投影到 hidden_dim |\n| Action tokens | 50 | action_horizon=50 |\n| **Total** | **~867** | |\n\n### 5.2 每条 Rollout 激活存储估算\n\n**假设条件**:\n- 8 层采样（PaliGemma LLM 层）\n- hidden_dim = 2048 (PaliGemma)\n- seq_len ≈ 867\n- replan_steps = 5，每 5 个 env step 做一次推理\n- 每 episode 约 200-400 env steps → ~40-80 次推理\n\n**方案 A: 存储完整序列激活 (fp32)**\n\n| 指标 | 值 |\n|------|-----|\n| 每次推理每层 | 2048 × 867 × 4 bytes = 7.1 MB |\n| 每次推理 8 层 | 56.8 MB |\n| 每 episode (60 次推理) | 3.4 GB |\n| 500 episodes | **1.7 TB** |\n\n**方案 B: 仅存储 action token 位置的激活 (fp32)**\n\n| 指标 | 值 |\n|------|-----|\n| 每次推理每层 | 2048 × 50 × 4 bytes = 0.41 MB |\n| 每次推理 8 层 | 3.3 MB |\n| 每 episode (60 次推理) | 197 MB |\n| 500 episodes | **96 GB** |\n\n**方案 C: Action tokens + fp16**\n\n| 指标 | 值 |\n|------|-----|\n| 每次推理 8 层 | 1.6 MB |\n| 每 episode (60 次推理) | 98 MB |\n| 500 episodes | **48 GB** |\n\n**方案 D: 池化后的层表征 (mean pooling over seq_len, fp16)**\n\n| 指标 | 值 |\n|------|-----|\n| 每次推理每层 | 2048 × 2 bytes = 4 KB |\n| 每次推理 8 层 | 32 KB |\n| 每 episode (60 次推理) | 1.9 MB |\n| 500 episodes | **0.95 GB** |\n\n### 5.3 推理速度估算\n\n**来源**: π₀ 论文 (Table 4) 在 RTX 4090 上的测量:\n- Image encoding: 14 ms\n- Observation forward pass: 32 ms\n- 10× action flow passes: 27 ms\n- **单次推理总计**: 73 ms\n\n**H100 估算** (约 2× 4090 推理性能):\n- 单次推理: ~35-40 ms\n- 每 episode (60 次推理): ~2.4 s（纯模型推理时间）\n- 加上环境仿真时间: 每 episode 约 30-60 秒\n- **500 episodes 总时间**: ~4-8 小时（单 H100）\n\n**注意**: 如果需要存储激活，推理时需额外内存存储 hook 输出，峰值显存约增加 50-100 MB。\n\n### 5.4 训练资源估算\n\n**LoRA 微调 500 episodes 数据**:\n- 数据: 500 episodes × ~200 steps × 7-dim action = ~70K 训练样本\n- 训练时间 (单 A6000/4090): 10k-30k steps × ~0.5s/step ≈ 1.4-4.2 小时\n- 显存: ~16-22 GB (LoRA)\n\n---\n\n## 6. 风险与阻塞项\n\n### 6.1 高风险项\n\n| 风险 | 严重性 | 说明 | 缓解方案 |\n|------|--------|------|----------|\n| **层数不匹配** | 🔴 高 | 模型仅 18 层，原计划 8 层采样中有 4 层不存在 | 调整为 {2,4,6,8,10,12,14,16} |\n| **PyTorch LoRA 未官方支持** | 🟡 中 | PyTorch 训练不原生支持 LoRA，需用社区方案或自实现 | 采用 Issue #842 的实现，或用 JAX 训练 + PyTorch 推理 |\n| **激活存储量大** | 🟡 中 | 完整序列存储 500 episodes 需 1.7TB | 使用方案 B/C/D 减少存储 |\n\n### 6.2 中等风险项\n\n| 风险 | 说明 | 缓解方案 |\n|------|------|----------|\n| JAX vs PyTorch 精度差异 | LeRobot PyTorch 转换后性能有下降，官方建议微调 | 可用 JAX checkpoint 作为 baseline 对比 |\n| Flow matching 推理开销 | 每次推理需要 10 步迭代去噪 | 已有 KV-cache 优化，单次 73ms 可接受 |\n| LIBERO-Plus 集成 | 需要替换 LIBERO 库，可能有版本兼容问题 | 使用 Docker 隔离环境 |\n\n### 6.3 非阻塞项\n\n- Checkpoint 下载: 公开可用，无需申请\n- 数据转换: 已有 LeRobot 格式转换脚本\n- 评测脚本: 完整可用，包含 Docker 配置\n- 多 GPU 支持: PyTorch DDP 已实现\n\n---\n\n## 7. 推荐技术方案\n\n### 7.1 总体架构\n\n```\n[LIBERO Env] → [π₀ with Hooks] → [Activation Buffer]\n                     ↓                    ↓\n              [Action Output]    [Meta-Brain Router]\n                                        ↓\n                                 [LoRA Selection]\n                                        ↓\n                               [Task-Specific LoRA]\n```\n\n### 7.2 具体步骤\n\n**Phase 1: 基础设施搭建**\n1. 安装 OpenPI (PyTorch 版) + LIBERO 环境\n2. 验证 `lerobot/pi0_base` 或 `pi0_libero_base` checkpoint 加载\n3. 运行标准 LIBERO 评测确认 baseline 性能\n\n**Phase 2: 激活提取**\n1. 在 PyTorch 模型上注册 forward hooks\n2. 选择层: PaliGemma layers {2,4,6,8,10,12,14,16}\n3. 使用方案 B (action tokens only, fp16): 每 500 episodes ~48 GB\n4. 收集 LIBERO 全 4 个 task suite 的激活\n\n**Phase 3: LoRA 训练**\n1. 基于 Issue #842 的 PyTorch LoRA 实现\n2. 或使用 JAX 原生 LoRA 训练 (gemma_2b_lora + gemma_300m_lora)\n3. 每个 task suite 训练一个 LoRA adapter\n4. LoRA config: rank=16, alpha=16.0, target=attn+ffn\n\n**Phase 4: Meta-Brain Router**\n1. 输入: 中间层激活 (8 layers × hidden_dim)\n2. 输出: LoRA adapter 选择/混合权重\n3. 训练: 使用收集的激活-任务标签对\n\n### 7.3 硬件需求\n\n| 阶段 | GPU 需求 | 时间估算 |\n|------|---------|---------|\n| LIBERO 评测 + 激活收集 | 1× H100/A100 | ~8 小时 |\n| LoRA 训练 (4 adapters) | 1× A6000/4090 | ~16 小时 |\n| Meta-Brain Router 训练 | 1× A6000 | ~2 小时 |\n| 总磁盘 | ~100 GB (激活) + ~10 GB (checkpoints) | |\n\n---\n\n## 8. 关键代码引用索引\n\n| 内容 | 文件路径 | 说明 |\n|------|---------|------|\n| Pi0 模型定义 (JAX) | `src/openpi/models/pi0.py:47-176` | Pi0 class, forward/loss/sample |\n| Pi0 模型定义 (PyTorch) | `src/openpi/models_pytorch/pi0_pytorch.py` | PI0Pytorch class |\n| Gemma 变体配置 | `src/openpi/models/gemma.py` | width/depth/heads 定义 |\n| Gemma PyTorch | `src/openpi/models_pytorch/gemma_pytorch.py` | GemmaForCausalLM 层结构 |\n| LoRA 实现 (JAX) | `src/openpi/models/lora.py` | Einsum, FeedForward adapters |\n| 模型配置 | `src/openpi/models/pi0_config.py` | Pi0Config dataclass |\n| 训练配置 | `src/openpi/training/config.py` | TrainConfig, LIBERO 数据配置 |\n| 训练脚本 (JAX) | `scripts/train.py` | JAX 训练循环 |\n| 训练脚本 (PyTorch) | `scripts/train_pytorch.py` | PyTorch 训练循环 |\n| LIBERO 策略映射 | `src/openpi/policies/libero_policy.py` | LiberoInputs/Outputs |\n| LIBERO 评测 | `examples/libero/main.py` | 完整评测流程 |\n| 数据转换 | `examples/libero/convert_libero_data_to_lerobot.py` | LIBERO → LeRobot |\n| SigLIP 视觉编码器 | `src/openpi/models/siglip.py` | So400m/14 ViT |\n| 注意力 mask | `src/openpi/models/pi0.py:20-38` | make_attn_mask() |\n| Flow matching | `src/openpi/models/pi0.py:119-150` | compute_loss() |\n| 推理采样 | `src/openpi/models/pi0.py:152-201` | sample_actions() |\n",
      "numLines": 530,
      "startLine": 1,
      "totalLines": 530
    }
  }
}
````

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_014WmscvikT8UmyNLoSg8DEZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/configs.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "b037c26b-7dd4-43e1-9b06-060be8b83974",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGhEWQQmBS5AojnDVMs4gK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 315,
      "cache_read_input_tokens": 29103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 315
      },
      "output_tokens": 70,
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

_source line 26 · 2026-05-15T11:00:57.475Z_

<details><summary>↩ Tool result · `toolu_014WmscvikT8UmyNLoSg8DEZ`</summary>

```text
1	"""
2	Configuration constants for Meta-Brain Phase 0 perturbation classifier.
3	
4	Defines perturbation taxonomies, layer indices, model dimensions,
5	and hyperparameter defaults shared across collect/train/eval scripts.
6	"""
7	
8	# ---------------------------------------------------------------------------
9	# Perturbation taxonomy
10	# ---------------------------------------------------------------------------
11	
12	PERTURBATION_TYPES_6CLASS = {
13	    "camera_viewpoints": 0,
14	    "light_conditions": 1,
15	    "background_textures": 2,
16	    "sensor_noise": 3,
17	    "objects_layout": 4,
18	    "robot_initial_states": 5,
19	}
20	
21	PERTURBATION_TYPES_3CLASS = {
22	    "visual": 0,   # camera + light + background + noise
23	    "spatial": 1,  # layout
24	    "physical": 2, # robot
25	}
26	
27	CLASS_6_TO_3_MAPPING = {
28	    0: 0,  # camera_viewpoints   -> visual
29	    1: 0,  # light_conditions    -> visual
30	    2: 0,  # background_textures -> visual
31	    3: 0,  # sensor_noise        -> visual
32	    4: 1,  # objects_layout      -> spatial
33	    5: 2,  # robot_initial_states -> physical
34	}
35	
36	CLASS_6_NAMES = [
37	    "camera_viewpoints",
38	    "light_conditions",
39	    "background_textures",
40	    "sensor_noise",
41	    "objects_layout",
42	    "robot_initial_states",
43	]
44	
45	CLASS_3_NAMES = ["visual", "spatial", "physical"]
46	
47	BINARY_NAMES = ["nominal", "perturbed"]
48	
49	# ---------------------------------------------------------------------------
50	# π₀ architecture constants
51	# ---------------------------------------------------------------------------
52	
53	PALIGEMMA_LAYERS = [2, 4, 6, 8, 10, 12, 14, 16]
54	EXPERT_LAYERS = [2, 6, 10, 14]
55	
56	PALIGEMMA_HIDDEN_DIM = 2048
57	EXPERT_HIDDEN_DIM = 1024
58	
59	PALIGEMMA_NUM_LAYERS = 18  # layers[0..17]
60	EXPERT_NUM_LAYERS = 18
61	
62	# PyTorch module path templates
63	PALIGEMMA_LAYER_TEMPLATE = (
64	    "model.paligemma_with_expert.paligemma.language_model.layers.{i}"
65	)
66	EXPERT_LAYER_TEMPLATE = (
67	    "model.paligemma_with_expert.gemma_expert.model.layers.{i}"
68	)
69	
70	# ---------------------------------------------------------------------------
71	# Pooling strategies
72	# ---------------------------------------------------------------------------
73	
74	POOLING_STRATEGIES = ["mean", "first", "last", "first_last"]
75	
76	def pooling_output_dim(pooling: str, hidden_dim: int) -> int:
77	    """Return output dimension for a given pooling strategy."""
78	    if pooling == "first_last":
79	        return hidden_dim * 2
80	    return hidden_dim
81	
82	# ---------------------------------------------------------------------------
83	# Classifier defaults
84	# ---------------------------------------------------------------------------
85	
86	CLASSIFIER_HIDDEN_DIM = 256
87	DEFAULT_LR = 1e-3
88	DEFAULT_EPOCHS = 50
89	DEFAULT_BATCH_SIZE = 64
90	NUM_FOLDS = 5
91	
92	# Activation source → input dimension calculation
93	ACTIVATION_SOURCES = ["paligemma_only", "expert_only", "both"]
94	
95	def compute_input_dim(activation_source: str, pooling: str) -> int:
96	    """Compute classifier input dimension from source and pooling strategy."""
97	    pg_dim = len(PALIGEMMA_LAYERS) * pooling_output_dim(pooling, PALIGEMMA_HIDDEN_DIM)
98	    ex_dim = len(EXPERT_LAYERS) * pooling_output_dim(pooling, EXPERT_HIDDEN_DIM)
99	    if activation_source == "paligemma_only":
100	        return pg_dim
101	    elif activation_source == "expert_only":
102	        return ex_dim
103	    elif activation_source == "both":
104	        return pg_dim + ex_dim
105	    raise ValueError(f"Unknown activation_source: {activation_source}")
106	
107	# ---------------------------------------------------------------------------
108	# Sweep grid
109	# ---------------------------------------------------------------------------
110	
111	SWEEP_POOLINGS = ["mean", "first", "first_last"]
112	SWEEP_SOURCES = ["paligemma_only", "expert_only", "both"]
113	SWEEP_LRS = [1e-2, 1e-3, 1e-4]
114	
115	# ---------------------------------------------------------------------------
116	# Go / No-Go thresholds (Phase 0 success criteria)
117	# ---------------------------------------------------------------------------
118	
119	GO_NOGO = {
120	    "6class_accuracy_min": 0.50,   # >50% on 6-class (chance=16.7%)
121	    "3class_accuracy_min": 0.65,   # >65% on 3-class (chance=33.3%)
122	    "binary_accuracy_min": 0.80,   # >80% on binary (chance=50%)
123	    "binary_roc_auc_min": 0.85,
124	}
125	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "67a0013e-ccae-495c-8687-047a92bcf1c4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/configs.py",
      "content": "\"\"\"\nConfiguration constants for Meta-Brain Phase 0 perturbation classifier.\n\nDefines perturbation taxonomies, layer indices, model dimensions,\nand hyperparameter defaults shared across collect/train/eval scripts.\n\"\"\"\n\n# ---------------------------------------------------------------------------\n# Perturbation taxonomy\n# ---------------------------------------------------------------------------\n\nPERTURBATION_TYPES_6CLASS = {\n    \"camera_viewpoints\": 0,\n    \"light_conditions\": 1,\n    \"background_textures\": 2,\n    \"sensor_noise\": 3,\n    \"objects_layout\": 4,\n    \"robot_initial_states\": 5,\n}\n\nPERTURBATION_TYPES_3CLASS = {\n    \"visual\": 0,   # camera + light + background + noise\n    \"spatial\": 1,  # layout\n    \"physical\": 2, # robot\n}\n\nCLASS_6_TO_3_MAPPING = {\n    0: 0,  # camera_viewpoints   -> visual\n    1: 0,  # light_conditions    -> visual\n    2: 0,  # background_textures -> visual\n    3: 0,  # sensor_noise        -> visual\n    4: 1,  # objects_layout      -> spatial\n    5: 2,  # robot_initial_states -> physical\n}\n\nCLASS_6_NAMES = [\n    \"camera_viewpoints\",\n    \"light_conditions\",\n    \"background_textures\",\n    \"sensor_noise\",\n    \"objects_layout\",\n    \"robot_initial_states\",\n]\n\nCLASS_3_NAMES = [\"visual\", \"spatial\", \"physical\"]\n\nBINARY_NAMES = [\"nominal\", \"perturbed\"]\n\n# ---------------------------------------------------------------------------\n# π₀ architecture constants\n# ---------------------------------------------------------------------------\n\nPALIGEMMA_LAYERS = [2, 4, 6, 8, 10, 12, 14, 16]\nEXPERT_LAYERS = [2, 6, 10, 14]\n\nPALIGEMMA_HIDDEN_DIM = 2048\nEXPERT_HIDDEN_DIM = 1024\n\nPALIGEMMA_NUM_LAYERS = 18  # layers[0..17]\nEXPERT_NUM_LAYERS = 18\n\n# PyTorch module path templates\nPALIGEMMA_LAYER_TEMPLATE = (\n    \"model.paligemma_with_expert.paligemma.language_model.layers.{i}\"\n)\nEXPERT_LAYER_TEMPLATE = (\n    \"model.paligemma_with_expert.gemma_expert.model.layers.{i}\"\n)\n\n# ---------------------------------------------------------------------------\n# Pooling strategies\n# ---------------------------------------------------------------------------\n\nPOOLING_STRATEGIES = [\"mean\", \"first\", \"last\", \"first_last\"]\n\ndef pooling_output_dim(pooling: str, hidden_dim: int) -> int:\n    \"\"\"Return output dimension for a given pooling strategy.\"\"\"\n    if pooling == \"first_last\":\n        return hidden_dim * 2\n    return hidden_dim\n\n# ---------------------------------------------------------------------------\n# Classifier defaults\n# ---------------------------------------------------------------------------\n\nCLASSIFIER_HIDDEN_DIM = 256\nDEFAULT_LR = 1e-3\nDEFAULT_EPOCHS = 50\nDEFAULT_BATCH_SIZE = 64\nNUM_FOLDS = 5\n\n# Activation source → input dimension calculation\nACTIVATION_SOURCES = [\"paligemma_only\", \"expert_only\", \"both\"]\n\ndef compute_input_dim(activation_source: str, pooling: str) -> int:\n    \"\"\"Compute classifier input dimension from source and pooling strategy.\"\"\"\n    pg_dim = len(PALIGEMMA_LAYERS) * pooling_output_dim(pooling, PALIGEMMA_HIDDEN_DIM)\n    ex_dim = len(EXPERT_LAYERS) * pooling_output_dim(pooling, EXPERT_HIDDEN_DIM)\n    if activation_source == \"paligemma_only\":\n        return pg_dim\n    elif activation_source == \"expert_only\":\n        return ex_dim\n    elif activation_source == \"both\":\n        return pg_dim + ex_dim\n    raise ValueError(f\"Unknown activation_source: {activation_source}\")\n\n# ---------------------------------------------------------------------------\n# Sweep grid\n# ---------------------------------------------------------------------------\n\nSWEEP_POOLINGS = [\"mean\", \"first\", \"first_last\"]\nSWEEP_SOURCES = [\"paligemma_only\", \"expert_only\", \"both\"]\nSWEEP_LRS = [1e-2, 1e-3, 1e-4]\n\n# ---------------------------------------------------------------------------\n# Go / No-Go thresholds (Phase 0 success criteria)\n# ---------------------------------------------------------------------------\n\nGO_NOGO = {\n    \"6class_accuracy_min\": 0.50,   # >50% on 6-class (chance=16.7%)\n    \"3class_accuracy_min\": 0.65,   # >65% on 3-class (chance=33.3%)\n    \"binary_accuracy_min\": 0.80,   # >80% on binary (chance=50%)\n    \"binary_roc_auc_min\": 0.85,\n}\n",
      "numLines": 125,
      "startLine": 1,
      "totalLines": 125
    }
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the project. Let me write the Phase 0 experiment spec document. I need to synthesize all the information from:

1. ROADMAP.md - project overview, MVP plan, reviewer concerns
2. memory.md - π₀ architecture details, LIBERO integration, LoRA support
3. decisions.yaml - D001-D003 decisions
4. IDEA_BRIEF.md - full proposal details, landscape, references
5. configs.py - existing code constants
6. openpi_research_report.md - detailed technical findings

Let me now write the comprehensive spec document. I need to note a few things:


I notice the configs.py has slightly different GO/NO-GO thresholds than what the task specifies, so I'll follow the task specification since that's the authoritative source. Let me also check if there's a register_artifact tool available to properly save this document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "eb4349eb-3382-4bc2-adba-9a52e6255224",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pFkEG4wJvjqfycavJ4trf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22742,
      "cache_read_input_tokens": 29418,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22742
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

_source line 28_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PownZgAmJwGRJicov8TuoD`</summary>

```json
{
  "query": "register artifact",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "2717e7e9-d94e-49ae-a753-77a9dd4648c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pFkEG4wJvjqfycavJ4trf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22742,
      "cache_read_input_tokens": 29418,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22742
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

_source line 29 · 2026-05-15T11:01:08.402Z_

<details><summary>↩ Tool result · `toolu_01PownZgAmJwGRJicov8TuoD`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "bc43785b-368c-40c0-950f-04e1133916b9",
  "tool_use_result": {
    "matches": [],
    "query": "register artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Sr9YYEXLbwwqPLKUQM1kn8`</summary>

```json
{
  "query": "register",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "b8bac5eb-a004-4330-994e-e4ae9f8d6ad3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016FrfSwssR4tSrecL27rQQn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 359,
      "cache_read_input_tokens": 52160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 359
      },
      "output_tokens": 56,
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

_source line 31 · 2026-05-15T11:01:11.296Z_

<details><summary>↩ Tool result · `toolu_01Sr9YYEXLbwwqPLKUQM1kn8`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "aebc1040-8e5b-43d4-933f-5cf0896820f1",
  "tool_use_result": {
    "matches": [],
    "query": "register",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QrbZg5gL6D9sWcnQQvHPGm`</summary>

```json
{
  "query": "artifact",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "75af621e-9f34-4042-bceb-64462286ba36",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F7n7g3Y6AeUwEs4WeAUsBT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 90,
      "cache_read_input_tokens": 52519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 90
      },
      "output_tokens": 63,
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

_source line 33 · 2026-05-15T11:01:13.857Z_

<details><summary>↩ Tool result · `toolu_01QrbZg5gL6D9sWcnQQvHPGm`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "1ca55277-349f-4d6c-9354-ceca817d8171",
  "tool_use_result": {
    "matches": [],
    "query": "artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MWbHRx8p4vW5J3gZ3cVsUx`</summary>

```json
{
  "query": "mcp agent-ml-research",
  "max_results": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "f3a89118-33b2-4547-bf0d-8674f2e23b5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3s2DUL4Jbdx6qGfrKASR2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 90,
      "cache_read_input_tokens": 52609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 90
      },
      "output_tokens": 36,
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

_source line 35 · 2026-05-15T11:01:16.718Z_

<details><summary>↩ Tool result · `toolu_01MWbHRx8p4vW5J3gZ3cVsUx`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
}
```

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

```json
{
  "type": "tool_reference",
  "tool_name": "ListMcpResourcesTool"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "ReadMcpResourceTool"
}
```

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
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "dbe9c838-8cdd-42d3-8e9c-3f3a5120ab47",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "ListMcpResourcesTool",
      "ReadMcpResourceTool",
      "WebFetch"
    ],
    "query": "mcp agent-ml-research",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
I don't see a `register_artifact` tool available. Let me check if there's a different tool name or if it's available through the MCP server resources.

Let me look at the MCP server resources to see if there's a register_artifact function.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "a08047e9-ff5d-44ae-a85c-3b42125d89d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Eq5MDz4WwnhqNncLqUKK7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1688,
      "cache_read_input_tokens": 52699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1688
      },
      "output_tokens": 30,
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

_source line 37_

`register_artifact` 不在可用工具列表中，我先写文档，之后再处理注册。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "80190ccd-f37f-4498-b86d-2b0b38a6e3e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Eq5MDz4WwnhqNncLqUKK7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1688,
      "cache_read_input_tokens": 52699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1688
      },
      "output_tokens": 30,
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

_source line 38_

<details open><summary>🔧 Tool call — Write · `toolu_015eU4qW6Bdyi87T6rDdqCEd`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0_experiment_spec.md",
  "content": "# Phase 0 Experiment Specification: Perturbation-Type Classifiability from π₀ Internal Activations\n\n> **项目**: Meta-Brain: Perturbation-Adaptive LoRA Routing\n> **版本**: v1.0 | **日期**: 2026-05-15\n> **关联决策**: D001 (MVP 定义), D002 (Reviewer 增强), D003 (架构修正)\n> **目标会议**: CoRL 2026 — Abstract DDL 2026-05-26, Paper DDL 2026-05-29\n\n---\n\n## 1. 实验目标\n\n**核心假设**: π₀ 内部激活（PaliGemma + Action Expert 的 Transformer hidden states）编码了扰动类型信息，可被轻量级 2-layer MLP probe 分类。\n\n**Phase 0 定位**: Early-kill gate。整个 Meta-Brain 方法论依赖\"扰动类型可从 VLA 内部激活诊断\"这一前提——若此假设不成立，后续所有工作（LoRA bank、routing、Correction Memory）全部无效。Phase 0 以最小成本（~20 H100-hrs, 4 天）验证这一前提，给出 GO/NO-GO 判定。\n\n**通过 → Phase 1**: LoRA Expert 训练（3 个 perturbation-specific LoRA adapters）。\n**不通过 → Pivot**: 放弃 type-specific routing，退化为 universal LoRA + Correction Memory。\n\n---\n\n## 2. 扰动 Taxonomy\n\n### 2.1 LIBERO-Plus 原始 7 类\n\nLIBERO-Plus (CVPR 2026) 定义 7 个扰动维度：\n\n| # | 扰动类型 | 定义 | π₀ baseline 成功率 |\n|---|----------|------|-------------------|\n| 1 | Camera Viewpoints | 改变相机位置/角度（高度、俯仰角、水平旋转） | 13.8% |\n| 2 | Light Conditions | 改变场景光照（亮度、色温、方向性） | 85.0% |\n| 3 | Background Textures | 改变背景/桌面纹理（图案、材质替换） | 81.4% |\n| 4 | Sensor Noise | 在观测图像叠加噪声（高斯、椒盐） | — |\n| 5 | Objects Layout | 重排工作空间物体位置 | — |\n| 6 | Robot Initial States | 改变机器人起始关节角度/末端位置 | 6.0% |\n| 7 | Language Instructions | 改写任务指令措辞 | — |\n\n**π₀ baseline 总体平均**: 53.6%（LIBERO-Plus 报告值）\n\n### 2.2 排除 Language Instructions\n\nLanguage Instructions 被排除出本实验的 taxonomy。\n\n**理由**: Meta-Brain 的 LoRA 修正作用于 visual/action token representation。语言扰动（指令改写/同义替换）影响的是文本输入编码，而非视觉-动作表征空间。语言扰动在 tokenization 阶段就已产生差异，不属于 LoRA 在 mid-to-late 层修正 visual token 的设计范围。此外，语言鲁棒性可通过 prompt engineering 或 text augmentation 单独解决，不需要 LoRA routing。\n\n### 2.3 7→3 映射定义\n\n| 3-class | 包含的 LIBERO-Plus 类型 | 映射理由 |\n|---------|------------------------|----------|\n| **Visual** | Camera Viewpoints, Light Conditions, Background Textures, Sensor Noise | 均扰动视觉输入流，影响 visual token representation。LoRA-V 定位 early-to-mid 层修正视觉分布偏移（camera→视角变换, light→亮度/色温, background→纹理域, noise→信噪比）。修正机制相同：校准 ViT 编码后的 visual token 在 LLM 层中的 cross-modal attention pattern |\n| **Spatial** | Objects Layout | 扰动物体-动作空间映射。物体位置改变导致学习到的 reach/grasp 轨迹失效。LoRA-S 定位 mid 层调整空间注意力权重，重新对齐 spatial token 与 action planning |\n| **Physical** | Robot Initial States | 扰动初始运动学状态。起始关节角/末端位置改变导致动作解码的 initial condition 错误。LoRA-P 定位 late 层调整动作解码，补偿运动学偏移 |\n\n### 2.4 Visual 类内方差风险\n\nVisual 类内性能差异显著：Camera 13.8% vs Light 85.0% vs Background 81.4%。Camera 扰动的严重性远高于 Light/Background。\n\n**风险**: 分类器可能将 Camera 单独聚类，而非与 Light/Background 归为一类。\n\n**缓解**: 6-class 对照实验可检验此风险。若 6-class accuracy > 50% 且 Visual 子类间混淆度低，说明激活空间确实区分了 Camera 与 Light/Background，后续可升级为 6 个 LoRA Expert。\n\n**映射理由**: 尽管严重性差异大，四类扰动的修正机制相同——都是视觉流校准（recalibrating visual token representations after ViT encoding）。LoRA-V 通过修正 early-to-mid 层的 cross-modal attention 来补偿视觉分布偏移，这一机制对 camera/light/background/noise 均适用。\n\n---\n\n## 3. 模型架构\n\n### 3.1 π₀ Backbone\n\n| 组件 | 参数 |\n|------|------|\n| **PaliGemma VLM** | SigLIP So400m/14 (ViT, ~400M params) + Gemma 2B LLM |\n| **Gemma 2B** | 18 layers, hidden_dim=2048, mlp_dim=16384, 8 heads (MQA, 1 KV head), head_dim=256 |\n| **Action Expert** | Gemma 300M, 18 layers, hidden_dim=1024, mlp_dim=4096, 8 heads (MQA) |\n| **总参数量** | ~3.3B |\n| **动作生成** | Flow matching, 10-step Euler integration |\n\n### 3.2 激活提取层\n\n| Transformer | 提取层 (0-indexed) | 层数 | Hidden dim |\n|-------------|-------------------|------|------------|\n| PaliGemma (Gemma 2B) | {2, 4, 6, 8, 10, 12, 14, 16} | 8 | 2048 |\n| Action Expert (Gemma 300M) | {2, 6, 10, 14} | 4 | 1024 |\n| **合计** | | **12** | |\n\n> ⚠️ **修正说明**: IDEA_BRIEF 原写 layers {4, 8, 12, 16, 20, 24, 28, 32}，基于错误的 32 层假设。π₀ 实际使用 Gemma 2B (18 layers, index 0-17)。已修正为 18 层范围内的均匀采样。（决策 D003）\n\n**PyTorch hook 路径**:\n- PaliGemma: `model.paligemma_with_expert.paligemma.language_model.layers[i]` (i=0..17)\n- Action Expert: `model.paligemma_with_expert.gemma_expert.model.layers[i]` (i=0..17)\n\n### 3.3 分类器架构\n\n与 SAFE (NeurIPS 2025) 保持一致：\n\n```\nInput (pooled activations) → Linear(input_dim, 256) → ReLU → Linear(256, num_classes)\n```\n\n- **Hidden dim**: 256\n- **Activation**: ReLU\n- **Loss**: Cross-entropy (3-class, 6-class), BCE (binary)\n- **Optimizer**: AdamW\n- **Training**: 50 epochs, batch_size=64, 5-fold cross-validation\n\n**Input dim 计算** (以 `both` + `mean` pooling 为例):\n- PaliGemma: 8 layers × 2048 = 16,384\n- Action Expert: 4 layers × 1024 = 4,096\n- Total: 20,480\n\n---\n\n## 4. 数据收集方案\n\n### 4.1 Episode 分布\n\n| 条件 | Episodes | 说明 |\n|------|----------|------|\n| Nominal (无扰动) | ~100 | Binary anomaly detection 的 negative class |\n| Camera Viewpoints | ~80 | |\n| Light Conditions | ~80 | |\n| Background Textures | ~80 | |\n| Sensor Noise | ~80 | |\n| Objects Layout | ~80 | |\n| Robot Initial States | ~80 | |\n| **总计** | **~580** | |\n\n覆盖 LIBERO 全 4 个 task suite (Spatial/Object/Goal/Long)，每个 suite 内均匀采样任务。\n\n### 4.2 每 Episode 采集内容\n\n每次 π₀ 推理（每 5 env steps 一次，每 episode ~40-80 次推理）记录：\n\n1. **PaliGemma 8 层 hidden states** — 按 4 种 pooling 策略存储\n2. **Action Expert 4 层 hidden states** — 按 4 种 pooling 策略存储\n3. **元数据**: episode_id, task_name, perturbation_type, step_idx, success/failure\n\n### 4.3 Pooling 策略\n\n同时存储 4 种 pooling 结果，在训练阶段选择最优：\n\n| Pooling | 操作 | 输出维度 (per layer) |\n|---------|------|---------------------|\n| `mean` | 全序列 mean pooling | hidden_dim |\n| `first` | 取第一个 token | hidden_dim |\n| `last` | 取最后一个 token | hidden_dim |\n| `first_last` | 拼接 first + last token | hidden_dim × 2 |\n\n### 4.4 存储估算\n\n使用 pooled fp16 (方案 D)：\n\n| 指标 | 值 |\n|------|-----|\n| 每次推理 (12 层, mean pooling, fp16) | 12 × (2048+1024)/12 × 2 ≈ 36 KB |\n| 更精确：PaliGemma 8×2048×2 + Expert 4×1024×2 | 32,768 + 8,192 = 40,960 B ≈ 40 KB |\n| 4 种 pooling | ×4 ≈ 160 KB |\n| 每 episode (60 次推理, 4 pooling) | ~9.6 MB |\n| 580 episodes | **~5.4 GB** |\n| 仅 mean pooling (主方案) | **~0.95 GB** |\n\n磁盘预算充裕。4 种 pooling 全存储 (~5.4 GB) 可承受，避免二次采集。\n\n---\n\n## 5. 评估 Protocol\n\n### 5.A 3-class 分类（主实验）\n\n**类别**: Visual / Spatial / Physical\n\n**数据**: 480 perturbed episodes (排除 nominal)，按 7→3 映射。\n- Visual: ~320 episodes (camera + light + background + noise)\n- Spatial: ~80 episodes (layout)\n- Physical: ~80 episodes (robot)\n\n> 注意类别不平衡：Visual 占 ~67%。使用 class-weighted loss 或 balanced sampling。\n\n**指标**:\n- Overall accuracy\n- Per-class accuracy / precision / recall / F1\n- Macro-F1 (类别不平衡下比 accuracy 更有信息量)\n- 3×3 normalized confusion matrix (行归一化 = recall, 列归一化 = precision)\n\n### 5.B 6-class 分类（对照实验）\n\n**类别**: Camera / Light / Background / Noise / Layout / Robot\n\n**数据**: 同 5.A 的 480 perturbed episodes，保持原始 6 类标签。\n\n**指标**:\n- 同 5.A 全部指标\n- 6×6 normalized confusion matrix\n- Visual 子类间混淆矩阵（Camera vs Light vs Background vs Noise）\n\n**用途**: 若 6-class accuracy > 50%（chance = 16.7%），证明激活空间对 fine-grained 扰动类型有区分力，后续可用 6 个 LoRA Expert 替代 3 个。\n\n### 5.C Binary anomaly detection（Sanity check）\n\n**类别**: Nominal / Perturbed\n\n**数据**: 全部 580 episodes（100 nominal + 480 perturbed）。\n\n**指标**:\n- ROC-AUC\n- Precision-Recall curve + AUC-PR\n- F1 @ optimal threshold\n\n**用途**: Binary 是比 3-class 更弱的假设。\n- Binary 失败（ROC-AUC < 0.70）→ 激活提取本身有问题（hook 位置/pooling/数据质量），需排查基础设施。\n- Binary 成功但 3-class 失败 → 激活编码了\"有扰动\"但未编码扰动类型，需增强输入（+ proprioception + visual change detection）。\n\n### 5.D Cross-cutting 分析\n\n**D1. Per-layer accuracy breakdown**\n\n对每个单独层训练分类器，绘制 layer index vs accuracy 曲线。揭示扰动信息在哪些层最富集。\n\n**D2. PaliGemma-only vs Action Expert-only vs Combined**\n\n| 激活源 | 输入层 | 预期信号 |\n|--------|--------|----------|\n| PaliGemma-only | 8 层, 2048-dim | Visual 和 Spatial 扰动（视觉-语言融合空间） |\n| Expert-only | 4 层, 1024-dim | Physical 扰动（动作解码空间） |\n| Both (Combined) | 12 层 | 全部扰动类型 |\n\n对比三种 activation source 的分类性能，验证双 Transformer 互补假设。\n\n**D3. Pooling 策略对比**\n\n3 pooling (mean / first / first_last) × 3 activation source × 3 classifier mode，报告最优组合。\n\n**D4. t-SNE / UMAP 可视化**\n\n对最优层组合的 pooled activations 做降维可视化：\n- 按 3-class 着色\n- 按 6-class 着色\n- 按 nominal/perturbed 着色\n\n直观展示聚类结构。如果 3-class 不可分但 binary 可分，可视化会直接暴露。\n\n---\n\n## 6. Hyperparameter Sweep\n\n### 6.1 Sweep Grid\n\n| 维度 | 值 | 数量 |\n|------|-----|------|\n| Pooling | mean, first, first_last | 3 |\n| Activation source | paligemma_only, expert_only, both | 3 |\n| Learning rate | 1e-2, 1e-3, 1e-4 | 3 |\n\n**每个 classifier mode**: 3 × 3 × 3 = **27 configs**\n\n### 6.2 总训练量\n\n| Classifier mode | Configs | CV folds | Total runs |\n|-----------------|---------|----------|------------|\n| 3-class | 27 | 5 | 135 |\n| 6-class | 27 | 5 | 135 |\n| Binary | 27 | 5 | 135 |\n| **合计** | | | **405** |\n\n### 6.3 时间估算\n\n- 每个 config (50 epochs, batch_size=64, ~580 episodes): **< 15 min** on single H100\n- 27 configs × 5 folds × 3 modes = 405 runs × 15 min = ~101 hours (sequential)\n- 4 GPU 并行: ~25 hours → **约 1 天**\n- 实际更快：大部分 config 的数据集很小（pooled activations），训练在 CPU 上几分钟内完成\n\n---\n\n## 7. GO/NO-GO 判据\n\n| 条件 | 判定 | 行动 |\n|------|------|------|\n| Binary ROC-AUC ≥ 0.75 **且** 3-class macro-F1 > 70% **且** confusion matrix 无严重混淆 (任意两类间 > 30%) | **GO** | 进入 Phase 1 LoRA Expert 训练 |\n| Binary ROC-AUC ≥ 0.75 **且** 3-class macro-F1 50-70% | **AUGMENT** | 增强 router 输入：+ proprioception history + visual change detection features。2 天 contingency (Days 5-6)。重新训练 PAR，若提升至 >70% → GO |\n| Binary ROC-AUC < 0.70 | **RETHINK** | 激活提取有根本问题。排查：换层选择 / 换 pooling 策略 / 换 token 位置（action-only vs full-seq） / 检查 hook 实现 |\n| Binary ROC-AUC ≥ 0.75 **但** 3-class macro-F1 < 50% | **PIVOT** | 激活编码了\"有扰动\"但未编码类型。放弃 type-specific routing，退化为 universal LoRA + Correction Memory |\n| 6-class accuracy > 50% | **信息** | 可升级为 6 个 LoRA Expert（更细粒度 routing） |\n| Confusion matrix 某两类 > 30% 互相混淆 | **信息** | 考虑合并该两类或重定义 taxonomy |\n\n### 7.1 Chance-level 参考\n\n| Mode | Chance level | GO 阈值 | 倍数 |\n|------|-------------|---------|------|\n| Binary | 50% (class-balanced) | 75% ROC-AUC | 1.5× |\n| 3-class | 33.3% (均匀) / 66.7% (majority class) | 70% macro-F1 | 2.1× / 1.05× |\n| 6-class | 16.7% | 50% accuracy | 3.0× |\n\n> 3-class 因 Visual 占 ~67%，majority-class baseline 已经很高。用 macro-F1 而非 accuracy 作为判据，避免被 Visual 的高占比拉高 overall accuracy 掩盖 Spatial/Physical 的差表现。\n\n---\n\n## 8. 资源预算\n\n### 8.1 计算资源\n\n| 阶段 | 内容 | H100-hrs | 墙钟时间 |\n|------|------|----------|---------|\n| 数据收集 | 冻结 π₀ rollout 580 episodes + 激活记录 | ~15 | 1-2 天 (4 GPU 并行) |\n| 分类器训练 + sweep | 405 runs (3 modes × 27 configs × 5 folds) | ~5 | 0.5-1 天 |\n| **Phase 0 总计** | | **~20** | **2-4 天** |\n\n### 8.2 详细时间线\n\n| Day | 内容 | GPU 利用 |\n|-----|------|---------|\n| Day 1 | 环境搭建：OpenPI + LIBERO-Plus + PyTorch hooks | 0 (setup) |\n| Day 1-2 | 数据收集：冻结 π₀ rollout 580 episodes，记录 12 层 pooled activations | 4× H100 并行 rollout |\n| Day 3 | 分类器训练 + hyperparameter sweep | 4× H100 并行 sweep |\n| Day 4 | 评估 + 可视化 + GO/NO-GO 判定 | 1× H100 (eval) |\n\n### 8.3 存储需求\n\n| 内容 | 大小 |\n|------|------|\n| Pooled activations (4 pooling, fp16) | ~5.4 GB |\n| π₀ checkpoint (bf16) | ~6.6 GB |\n| 分类器 checkpoints (405 runs) | ~1 GB |\n| LIBERO-Plus 环境 + 依赖 | ~10 GB |\n| **总计** | **~23 GB** |\n\n### 8.4 硬件需求\n\n- **最低**: 1× H100 80GB（可完成全部实验，墙钟时间 ~5-7 天）\n- **推荐**: 4× H100 80GB（并行 rollout + sweep，墙钟时间 ~2-4 天）\n- **LoRA 微调显存**: > 22.5 GB（Phase 0 不需要，Phase 1 才用）\n- **推理显存**: > 8 GB (bf16)\n\n---\n\n## 9. 风险与缓解\n\n| 风险 | 严重性 | 说明 | 缓解方案 |\n|------|--------|------|----------|\n| **PyTorch LoRA 用社区 PR** | 🟡 中 | Issue #842 的实现未合并到 OpenPI 主线 | 代码完整可用（26.5M params, 96.95% on LIBERO）；Phase 0 不需要 LoRA，仅需 inference hooks |\n| **层索引已修正** | ✅ 已解决 | 原 {4,8,12,16,20,24,28,32} 基于 32 层假设 | 修正为 PaliGemma {2,4,6,8,10,12,14,16} + Expert {2,6,10,14}（D003） |\n| **激活存储量** | 🟢 低 | Pooled fp16 控制在 ~5.4 GB | 远小于磁盘预算，无需压缩 |\n| **LIBERO-Plus 集成** | 🟢 低 | \"直接替换 LIBERO 库\"，评测代码无需修改 | Docker 隔离环境；唯一改动 num_trials=1 |\n| **3-class 类别不平衡** | 🟡 中 | Visual ~67% / Spatial ~17% / Physical ~17% | Class-weighted loss + balanced sampling + 用 macro-F1 替代 accuracy |\n| **Hook 实现正确性** | 🟡 中 | PyTorch forward hook 可能改变计算图或显存 | Phase 0 开始前先验证：对比有/无 hook 的 action 输出一致性 |\n| **Rollout 耗时超预期** | 🟡 中 | 580 episodes × 30-60s each ≈ 5-10 hours (单 GPU) | 4 GPU 并行 → 1.5-2.5 hours；nohup 后台执行 |\n| **分类器过拟合** | 🟡 中 | 数据量小 (~580 episodes)，分类器可能过拟合 | 5-fold CV 防止 overfitting；2-layer MLP 容量有限（SAFE 同架构） |\n\n---\n\n## 附录 A: 与 SAFE (NeurIPS 2025) 的对比\n\n| 维度 | SAFE | Phase 0 (Meta-Brain) |\n|------|------|---------------------|\n| 任务 | Binary failure detection | 3-class / 6-class perturbation classification + binary |\n| 输入 | Final-layer activations | Multi-layer activations (12 layers, 2 Transformers) |\n| 分类器 | 2-layer MLP, hidden=256 | 同 SAFE |\n| Pooling | Mean over sequence | Mean / first / last / first+last (sweep) |\n| 数据规模 | Unseen tasks, zero-shot | Task-specific, same-task |\n| 性能 | 78.0% ROC-AUC (binary) | 目标：>75% ROC-AUC (binary), >70% macro-F1 (3-class) |\n\nPhase 0 比 SAFE 的优势：(1) 多层而非仅 final-layer，信号更丰富；(2) 双 Transformer 提供互补信号；(3) same-task 而非 zero-shot，降低难度。\nPhase 0 比 SAFE 的劣势：(1) multi-class 比 binary 更难；(2) 某些扰动类型间的边界可能模糊。\n\n## 附录 B: 已有代码基础\n\n`artifacts/phase0/configs.py` 已定义：\n\n- `PERTURBATION_TYPES_6CLASS` / `PERTURBATION_TYPES_3CLASS` — 类别映射\n- `CLASS_6_TO_3_MAPPING` — 7→3 映射表\n- `PALIGEMMA_LAYERS` / `EXPERT_LAYERS` — 激活提取层\n- `POOLING_STRATEGIES` — pooling 策略\n- `SWEEP_POOLINGS` / `SWEEP_SOURCES` / `SWEEP_LRS` — sweep grid\n- `GO_NOGO` — 阈值（注：configs.py 中阈值偏保守，以本文档第 7 节为准）\n- `compute_input_dim()` — 分类器输入维度计算\n\n待实现：\n- 激活提取 hook (`ActivationExtractor`)\n- 数据收集 pipeline (rollout + hook + save)\n- 分类器训练/评估 (train + sweep + 5-fold CV)\n- 可视化 (confusion matrix + t-SNE/UMAP)\n\n## 附录 C: π₀ LIBERO-Plus Baseline 参考值\n\n来源：LIBERO-Plus 论文 + VLA-GSE (2605.06175)\n\n| 方法 | LIBERO-Plus 均值 | Camera | Light | Background | Robot | Noise | Layout |\n|------|-----------------|--------|-------|------------|-------|-------|--------|\n| π₀ (frozen) | 53.6% | 13.8% | 85.0% | 81.4% | 6.0% | — | — |\n| VLA-GSE (Qwen3-VL-4B) | 81.2% | 64.4% | 97.3% | 97.3% | 68.5% | 79.4% | 82.6% |\n| SRPO | 82.1% | — | — | — | — | — | — |\n| CorridorVLA | 83.21% | — (按 task category 报告) | | | | | |\n\nCamera 和 Robot 是 π₀ 最薄弱的两个维度，也是 Meta-Brain routing 最有价值的修正目标。\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "62dfbc6a-7728-495b-8cd5-da7061fdfc6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Eq5MDz4WwnhqNncLqUKK7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1688,
      "cache_read_input_tokens": 52699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1688
      },
      "output_tokens": 30,
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

_source line 39 · 2026-05-15T11:03:52.876Z_

<details><summary>↩ Tool result · `toolu_015eU4qW6Bdyi87T6rDdqCEd`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0_experiment_spec.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "2da90157-2240-4c42-8802-cedc510f4dae",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0_experiment_spec.md",
    "content": "# Phase 0 Experiment Specification: Perturbation-Type Classifiability from π₀ Internal Activations\n\n> **项目**: Meta-Brain: Perturbation-Adaptive LoRA Routing\n> **版本**: v1.0 | **日期**: 2026-05-15\n> **关联决策**: D001 (MVP 定义), D002 (Reviewer 增强), D003 (架构修正)\n> **目标会议**: CoRL 2026 — Abstract DDL 2026-05-26, Paper DDL 2026-05-29\n\n---\n\n## 1. 实验目标\n\n**核心假设**: π₀ 内部激活（PaliGemma + Action Expert 的 Transformer hidden states）编码了扰动类型信息，可被轻量级 2-layer MLP probe 分类。\n\n**Phase 0 定位**: Early-kill gate。整个 Meta-Brain 方法论依赖\"扰动类型可从 VLA 内部激活诊断\"这一前提——若此假设不成立，后续所有工作（LoRA bank、routing、Correction Memory）全部无效。Phase 0 以最小成本（~20 H100-hrs, 4 天）验证这一前提，给出 GO/NO-GO 判定。\n\n**通过 → Phase 1**: LoRA Expert 训练（3 个 perturbation-specific LoRA adapters）。\n**不通过 → Pivot**: 放弃 type-specific routing，退化为 universal LoRA + Correction Memory。\n\n---\n\n## 2. 扰动 Taxonomy\n\n### 2.1 LIBERO-Plus 原始 7 类\n\nLIBERO-Plus (CVPR 2026) 定义 7 个扰动维度：\n\n| # | 扰动类型 | 定义 | π₀ baseline 成功率 |\n|---|----------|------|-------------------|\n| 1 | Camera Viewpoints | 改变相机位置/角度（高度、俯仰角、水平旋转） | 13.8% |\n| 2 | Light Conditions | 改变场景光照（亮度、色温、方向性） | 85.0% |\n| 3 | Background Textures | 改变背景/桌面纹理（图案、材质替换） | 81.4% |\n| 4 | Sensor Noise | 在观测图像叠加噪声（高斯、椒盐） | — |\n| 5 | Objects Layout | 重排工作空间物体位置 | — |\n| 6 | Robot Initial States | 改变机器人起始关节角度/末端位置 | 6.0% |\n| 7 | Language Instructions | 改写任务指令措辞 | — |\n\n**π₀ baseline 总体平均**: 53.6%（LIBERO-Plus 报告值）\n\n### 2.2 排除 Language Instructions\n\nLanguage Instructions 被排除出本实验的 taxonomy。\n\n**理由**: Meta-Brain 的 LoRA 修正作用于 visual/action token representation。语言扰动（指令改写/同义替换）影响的是文本输入编码，而非视觉-动作表征空间。语言扰动在 tokenization 阶段就已产生差异，不属于 LoRA 在 mid-to-late 层修正 visual token 的设计范围。此外，语言鲁棒性可通过 prompt engineering 或 text augmentation 单独解决，不需要 LoRA routing。\n\n### 2.3 7→3 映射定义\n\n| 3-class | 包含的 LIBERO-Plus 类型 | 映射理由 |\n|---------|------------------------|----------|\n| **Visual** | Camera Viewpoints, Light Conditions, Background Textures, Sensor Noise | 均扰动视觉输入流，影响 visual token representation。LoRA-V 定位 early-to-mid 层修正视觉分布偏移（camera→视角变换, light→亮度/色温, background→纹理域, noise→信噪比）。修正机制相同：校准 ViT 编码后的 visual token 在 LLM 层中的 cross-modal attention pattern |\n| **Spatial** | Objects Layout | 扰动物体-动作空间映射。物体位置改变导致学习到的 reach/grasp 轨迹失效。LoRA-S 定位 mid 层调整空间注意力权重，重新对齐 spatial token 与 action planning |\n| **Physical** | Robot Initial States | 扰动初始运动学状态。起始关节角/末端位置改变导致动作解码的 initial condition 错误。LoRA-P 定位 late 层调整动作解码，补偿运动学偏移 |\n\n### 2.4 Visual 类内方差风险\n\nVisual 类内性能差异显著：Camera 13.8% vs Light 85.0% vs Background 81.4%。Camera 扰动的严重性远高于 Light/Background。\n\n**风险**: 分类器可能将 Camera 单独聚类，而非与 Light/Background 归为一类。\n\n**缓解**: 6-class 对照实验可检验此风险。若 6-class accuracy > 50% 且 Visual 子类间混淆度低，说明激活空间确实区分了 Camera 与 Light/Background，后续可升级为 6 个 LoRA Expert。\n\n**映射理由**: 尽管严重性差异大，四类扰动的修正机制相同——都是视觉流校准（recalibrating visual token representations after ViT encoding）。LoRA-V 通过修正 early-to-mid 层的 cross-modal attention 来补偿视觉分布偏移，这一机制对 camera/light/background/noise 均适用。\n\n---\n\n## 3. 模型架构\n\n### 3.1 π₀ Backbone\n\n| 组件 | 参数 |\n|------|------|\n| **PaliGemma VLM** | SigLIP So400m/14 (ViT, ~400M params) + Gemma 2B LLM |\n| **Gemma 2B** | 18 layers, hidden_dim=2048, mlp_dim=16384, 8 heads (MQA, 1 KV head), head_dim=256 |\n| **Action Expert** | Gemma 300M, 18 layers, hidden_dim=1024, mlp_dim=4096, 8 heads (MQA) |\n| **总参数量** | ~3.3B |\n| **动作生成** | Flow matching, 10-step Euler integration |\n\n### 3.2 激活提取层\n\n| Transformer | 提取层 (0-indexed) | 层数 | Hidden dim |\n|-------------|-------------------|------|------------|\n| PaliGemma (Gemma 2B) | {2, 4, 6, 8, 10, 12, 14, 16} | 8 | 2048 |\n| Action Expert (Gemma 300M) | {2, 6, 10, 14} | 4 | 1024 |\n| **合计** | | **12** | |\n\n> ⚠️ **修正说明**: IDEA_BRIEF 原写 layers {4, 8, 12, 16, 20, 24, 28, 32}，基于错误的 32 层假设。π₀ 实际使用 Gemma 2B (18 layers, index 0-17)。已修正为 18 层范围内的均匀采样。（决策 D003）\n\n**PyTorch hook 路径**:\n- PaliGemma: `model.paligemma_with_expert.paligemma.language_model.layers[i]` (i=0..17)\n- Action Expert: `model.paligemma_with_expert.gemma_expert.model.layers[i]` (i=0..17)\n\n### 3.3 分类器架构\n\n与 SAFE (NeurIPS 2025) 保持一致：\n\n```\nInput (pooled activations) → Linear(input_dim, 256) → ReLU → Linear(256, num_classes)\n```\n\n- **Hidden dim**: 256\n- **Activation**: ReLU\n- **Loss**: Cross-entropy (3-class, 6-class), BCE (binary)\n- **Optimizer**: AdamW\n- **Training**: 50 epochs, batch_size=64, 5-fold cross-validation\n\n**Input dim 计算** (以 `both` + `mean` pooling 为例):\n- PaliGemma: 8 layers × 2048 = 16,384\n- Action Expert: 4 layers × 1024 = 4,096\n- Total: 20,480\n\n---\n\n## 4. 数据收集方案\n\n### 4.1 Episode 分布\n\n| 条件 | Episodes | 说明 |\n|------|----------|------|\n| Nominal (无扰动) | ~100 | Binary anomaly detection 的 negative class |\n| Camera Viewpoints | ~80 | |\n| Light Conditions | ~80 | |\n| Background Textures | ~80 | |\n| Sensor Noise | ~80 | |\n| Objects Layout | ~80 | |\n| Robot Initial States | ~80 | |\n| **总计** | **~580** | |\n\n覆盖 LIBERO 全 4 个 task suite (Spatial/Object/Goal/Long)，每个 suite 内均匀采样任务。\n\n### 4.2 每 Episode 采集内容\n\n每次 π₀ 推理（每 5 env steps 一次，每 episode ~40-80 次推理）记录：\n\n1. **PaliGemma 8 层 hidden states** — 按 4 种 pooling 策略存储\n2. **Action Expert 4 层 hidden states** — 按 4 种 pooling 策略存储\n3. **元数据**: episode_id, task_name, perturbation_type, step_idx, success/failure\n\n### 4.3 Pooling 策略\n\n同时存储 4 种 pooling 结果，在训练阶段选择最优：\n\n| Pooling | 操作 | 输出维度 (per layer) |\n|---------|------|---------------------|\n| `mean` | 全序列 mean pooling | hidden_dim |\n| `first` | 取第一个 token | hidden_dim |\n| `last` | 取最后一个 token | hidden_dim |\n| `first_last` | 拼接 first + last token | hidden_dim × 2 |\n\n### 4.4 存储估算\n\n使用 pooled fp16 (方案 D)：\n\n| 指标 | 值 |\n|------|-----|\n| 每次推理 (12 层, mean pooling, fp16) | 12 × (2048+1024)/12 × 2 ≈ 36 KB |\n| 更精确：PaliGemma 8×2048×2 + Expert 4×1024×2 | 32,768 + 8,192 = 40,960 B ≈ 40 KB |\n| 4 种 pooling | ×4 ≈ 160 KB |\n| 每 episode (60 次推理, 4 pooling) | ~9.6 MB |\n| 580 episodes | **~5.4 GB** |\n| 仅 mean pooling (主方案) | **~0.95 GB** |\n\n磁盘预算充裕。4 种 pooling 全存储 (~5.4 GB) 可承受，避免二次采集。\n\n---\n\n## 5. 评估 Protocol\n\n### 5.A 3-class 分类（主实验）\n\n**类别**: Visual / Spatial / Physical\n\n**数据**: 480 perturbed episodes (排除 nominal)，按 7→3 映射。\n- Visual: ~320 episodes (camera + light + background + noise)\n- Spatial: ~80 episodes (layout)\n- Physical: ~80 episodes (robot)\n\n> 注意类别不平衡：Visual 占 ~67%。使用 class-weighted loss 或 balanced sampling。\n\n**指标**:\n- Overall accuracy\n- Per-class accuracy / precision / recall / F1\n- Macro-F1 (类别不平衡下比 accuracy 更有信息量)\n- 3×3 normalized confusion matrix (行归一化 = recall, 列归一化 = precision)\n\n### 5.B 6-class 分类（对照实验）\n\n**类别**: Camera / Light / Background / Noise / Layout / Robot\n\n**数据**: 同 5.A 的 480 perturbed episodes，保持原始 6 类标签。\n\n**指标**:\n- 同 5.A 全部指标\n- 6×6 normalized confusion matrix\n- Visual 子类间混淆矩阵（Camera vs Light vs Background vs Noise）\n\n**用途**: 若 6-class accuracy > 50%（chance = 16.7%），证明激活空间对 fine-grained 扰动类型有区分力，后续可用 6 个 LoRA Expert 替代 3 个。\n\n### 5.C Binary anomaly detection（Sanity check）\n\n**类别**: Nominal / Perturbed\n\n**数据**: 全部 580 episodes（100 nominal + 480 perturbed）。\n\n**指标**:\n- ROC-AUC\n- Precision-Recall curve + AUC-PR\n- F1 @ optimal threshold\n\n**用途**: Binary 是比 3-class 更弱的假设。\n- Binary 失败（ROC-AUC < 0.70）→ 激活提取本身有问题（hook 位置/pooling/数据质量），需排查基础设施。\n- Binary 成功但 3-class 失败 → 激活编码了\"有扰动\"但未编码扰动类型，需增强输入（+ proprioception + visual change detection）。\n\n### 5.D Cross-cutting 分析\n\n**D1. Per-layer accuracy breakdown**\n\n对每个单独层训练分类器，绘制 layer index vs accuracy 曲线。揭示扰动信息在哪些层最富集。\n\n**D2. PaliGemma-only vs Action Expert-only vs Combined**\n\n| 激活源 | 输入层 | 预期信号 |\n|--------|--------|----------|\n| PaliGemma-only | 8 层, 2048-dim | Visual 和 Spatial 扰动（视觉-语言融合空间） |\n| Expert-only | 4 层, 1024-dim | Physical 扰动（动作解码空间） |\n| Both (Combined) | 12 层 | 全部扰动类型 |\n\n对比三种 activation source 的分类性能，验证双 Transformer 互补假设。\n\n**D3. Pooling 策略对比**\n\n3 pooling (mean / first / first_last) × 3 activation source × 3 classifier mode，报告最优组合。\n\n**D4. t-SNE / UMAP 可视化**\n\n对最优层组合的 pooled activations 做降维可视化：\n- 按 3-class 着色\n- 按 6-class 着色\n- 按 nominal/perturbed 着色\n\n直观展示聚类结构。如果 3-class 不可分但 binary 可分，可视化会直接暴露。\n\n---\n\n## 6. Hyperparameter Sweep\n\n### 6.1 Sweep Grid\n\n| 维度 | 值 | 数量 |\n|------|-----|------|\n| Pooling | mean, first, first_last | 3 |\n| Activation source | paligemma_only, expert_only, both | 3 |\n| Learning rate | 1e-2, 1e-3, 1e-4 | 3 |\n\n**每个 classifier mode**: 3 × 3 × 3 = **27 configs**\n\n### 6.2 总训练量\n\n| Classifier mode | Configs | CV folds | Total runs |\n|-----------------|---------|----------|------------|\n| 3-class | 27 | 5 | 135 |\n| 6-class | 27 | 5 | 135 |\n| Binary | 27 | 5 | 135 |\n| **合计** | | | **405** |\n\n### 6.3 时间估算\n\n- 每个 config (50 epochs, batch_size=64, ~580 episodes): **< 15 min** on single H100\n- 27 configs × 5 folds × 3 modes = 405 runs × 15 min = ~101 hours (sequential)\n- 4 GPU 并行: ~25 hours → **约 1 天**\n- 实际更快：大部分 config 的数据集很小（pooled activations），训练在 CPU 上几分钟内完成\n\n---\n\n## 7. GO/NO-GO 判据\n\n| 条件 | 判定 | 行动 |\n|------|------|------|\n| Binary ROC-AUC ≥ 0.75 **且** 3-class macro-F1 > 70% **且** confusion matrix 无严重混淆 (任意两类间 > 30%) | **GO** | 进入 Phase 1 LoRA Expert 训练 |\n| Binary ROC-AUC ≥ 0.75 **且** 3-class macro-F1 50-70% | **AUGMENT** | 增强 router 输入：+ proprioception history + visual change detection features。2 天 contingency (Days 5-6)。重新训练 PAR，若提升至 >70% → GO |\n| Binary ROC-AUC < 0.70 | **RETHINK** | 激活提取有根本问题。排查：换层选择 / 换 pooling 策略 / 换 token 位置（action-only vs full-seq） / 检查 hook 实现 |\n| Binary ROC-AUC ≥ 0.75 **但** 3-class macro-F1 < 50% | **PIVOT** | 激活编码了\"有扰动\"但未编码类型。放弃 type-specific routing，退化为 universal LoRA + Correction Memory |\n| 6-class accuracy > 50% | **信息** | 可升级为 6 个 LoRA Expert（更细粒度 routing） |\n| Confusion matrix 某两类 > 30% 互相混淆 | **信息** | 考虑合并该两类或重定义 taxonomy |\n\n### 7.1 Chance-level 参考\n\n| Mode | Chance level | GO 阈值 | 倍数 |\n|------|-------------|---------|------|\n| Binary | 50% (class-balanced) | 75% ROC-AUC | 1.5× |\n| 3-class | 33.3% (均匀) / 66.7% (majority class) | 70% macro-F1 | 2.1× / 1.05× |\n| 6-class | 16.7% | 50% accuracy | 3.0× |\n\n> 3-class 因 Visual 占 ~67%，majority-class baseline 已经很高。用 macro-F1 而非 accuracy 作为判据，避免被 Visual 的高占比拉高 overall accuracy 掩盖 Spatial/Physical 的差表现。\n\n---\n\n## 8. 资源预算\n\n### 8.1 计算资源\n\n| 阶段 | 内容 | H100-hrs | 墙钟时间 |\n|------|------|----------|---------|\n| 数据收集 | 冻结 π₀ rollout 580 episodes + 激活记录 | ~15 | 1-2 天 (4 GPU 并行) |\n| 分类器训练 + sweep | 405 runs (3 modes × 27 configs × 5 folds) | ~5 | 0.5-1 天 |\n| **Phase 0 总计** | | **~20** | **2-4 天** |\n\n### 8.2 详细时间线\n\n| Day | 内容 | GPU 利用 |\n|-----|------|---------|\n| Day 1 | 环境搭建：OpenPI + LIBERO-Plus + PyTorch hooks | 0 (setup) |\n| Day 1-2 | 数据收集：冻结 π₀ rollout 580 episodes，记录 12 层 pooled activations | 4× H100 并行 rollout |\n| Day 3 | 分类器训练 + hyperparameter sweep | 4× H100 并行 sweep |\n| Day 4 | 评估 + 可视化 + GO/NO-GO 判定 | 1× H100 (eval) |\n\n### 8.3 存储需求\n\n| 内容 | 大小 |\n|------|------|\n| Pooled activations (4 pooling, fp16) | ~5.4 GB |\n| π₀ checkpoint (bf16) | ~6.6 GB |\n| 分类器 checkpoints (405 runs) | ~1 GB |\n| LIBERO-Plus 环境 + 依赖 | ~10 GB |\n| **总计** | **~23 GB** |\n\n### 8.4 硬件需求\n\n- **最低**: 1× H100 80GB（可完成全部实验，墙钟时间 ~5-7 天）\n- **推荐**: 4× H100 80GB（并行 rollout + sweep，墙钟时间 ~2-4 天）\n- **LoRA 微调显存**: > 22.5 GB（Phase 0 不需要，Phase 1 才用）\n- **推理显存**: > 8 GB (bf16)\n\n---\n\n## 9. 风险与缓解\n\n| 风险 | 严重性 | 说明 | 缓解方案 |\n|------|--------|------|----------|\n| **PyTorch LoRA 用社区 PR** | 🟡 中 | Issue #842 的实现未合并到 OpenPI 主线 | 代码完整可用（26.5M params, 96.95% on LIBERO）；Phase 0 不需要 LoRA，仅需 inference hooks |\n| **层索引已修正** | ✅ 已解决 | 原 {4,8,12,16,20,24,28,32} 基于 32 层假设 | 修正为 PaliGemma {2,4,6,8,10,12,14,16} + Expert {2,6,10,14}（D003） |\n| **激活存储量** | 🟢 低 | Pooled fp16 控制在 ~5.4 GB | 远小于磁盘预算，无需压缩 |\n| **LIBERO-Plus 集成** | 🟢 低 | \"直接替换 LIBERO 库\"，评测代码无需修改 | Docker 隔离环境；唯一改动 num_trials=1 |\n| **3-class 类别不平衡** | 🟡 中 | Visual ~67% / Spatial ~17% / Physical ~17% | Class-weighted loss + balanced sampling + 用 macro-F1 替代 accuracy |\n| **Hook 实现正确性** | 🟡 中 | PyTorch forward hook 可能改变计算图或显存 | Phase 0 开始前先验证：对比有/无 hook 的 action 输出一致性 |\n| **Rollout 耗时超预期** | 🟡 中 | 580 episodes × 30-60s each ≈ 5-10 hours (单 GPU) | 4 GPU 并行 → 1.5-2.5 hours；nohup 后台执行 |\n| **分类器过拟合** | 🟡 中 | 数据量小 (~580 episodes)，分类器可能过拟合 | 5-fold CV 防止 overfitting；2-layer MLP 容量有限（SAFE 同架构） |\n\n---\n\n## 附录 A: 与 SAFE (NeurIPS 2025) 的对比\n\n| 维度 | SAFE | Phase 0 (Meta-Brain) |\n|------|------|---------------------|\n| 任务 | Binary failure detection | 3-class / 6-class perturbation classification + binary |\n| 输入 | Final-layer activations | Multi-layer activations (12 layers, 2 Transformers) |\n| 分类器 | 2-layer MLP, hidden=256 | 同 SAFE |\n| Pooling | Mean over sequence | Mean / first / last / first+last (sweep) |\n| 数据规模 | Unseen tasks, zero-shot | Task-specific, same-task |\n| 性能 | 78.0% ROC-AUC (binary) | 目标：>75% ROC-AUC (binary), >70% macro-F1 (3-class) |\n\nPhase 0 比 SAFE 的优势：(1) 多层而非仅 final-layer，信号更丰富；(2) 双 Transformer 提供互补信号；(3) same-task 而非 zero-shot，降低难度。\nPhase 0 比 SAFE 的劣势：(1) multi-class 比 binary 更难；(2) 某些扰动类型间的边界可能模糊。\n\n## 附录 B: 已有代码基础\n\n`artifacts/phase0/configs.py` 已定义：\n\n- `PERTURBATION_TYPES_6CLASS` / `PERTURBATION_TYPES_3CLASS` — 类别映射\n- `CLASS_6_TO_3_MAPPING` — 7→3 映射表\n- `PALIGEMMA_LAYERS` / `EXPERT_LAYERS` — 激活提取层\n- `POOLING_STRATEGIES` — pooling 策略\n- `SWEEP_POOLINGS` / `SWEEP_SOURCES` / `SWEEP_LRS` — sweep grid\n- `GO_NOGO` — 阈值（注：configs.py 中阈值偏保守，以本文档第 7 节为准）\n- `compute_input_dim()` — 分类器输入维度计算\n\n待实现：\n- 激活提取 hook (`ActivationExtractor`)\n- 数据收集 pipeline (rollout + hook + save)\n- 分类器训练/评估 (train + sweep + 5-fold CV)\n- 可视化 (confusion matrix + t-SNE/UMAP)\n\n## 附录 C: π₀ LIBERO-Plus Baseline 参考值\n\n来源：LIBERO-Plus 论文 + VLA-GSE (2605.06175)\n\n| 方法 | LIBERO-Plus 均值 | Camera | Light | Background | Robot | Noise | Layout |\n|------|-----------------|--------|-------|------------|-------|-------|--------|\n| π₀ (frozen) | 53.6% | 13.8% | 85.0% | 81.4% | 6.0% | — | — |\n| VLA-GSE (Qwen3-VL-4B) | 81.2% | 64.4% | 97.3% | 97.3% | 68.5% | 79.4% | 82.6% |\n| SRPO | 82.1% | — | — | — | — | — | — |\n| CorridorVLA | 83.21% | — (按 task category 报告) | | | | | |\n\nCamera 和 Robot 是 π₀ 最薄弱的两个维度，也是 Meta-Brain routing 最有价值的修正目标。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---

### Assistant

_source line 40_

文档已写入。尝试查找 `register_artifact` 工具。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "0aa54338-b513-4c46-aef0-e0a3b27b7195",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMnMqV3sngcaSA9BMuqiKw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7762,
      "cache_read_input_tokens": 54387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7762
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

_source line 41_

<details open><summary>🔧 Tool call — ListMcpResourcesTool · `toolu_016wRNAXKvcMnMCJunkmwb7X`</summary>

```json
{
  "server": "agent-ml-research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "502ec17e-17ab-4d6f-af72-f6ee8160d8d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMnMqV3sngcaSA9BMuqiKw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7762,
      "cache_read_input_tokens": 54387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7762
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

_source line 42 · 2026-05-15T11:03:56.205Z_

<details><summary>↩ Tool result · `toolu_016wRNAXKvcMnMCJunkmwb7X`</summary>

```text
No resources found. MCP servers may still provide tools even if they have no resources.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "61f94d75-6d1e-41cc-8368-edd839664ce1",
  "tool_use_result": []
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Bash · `toolu_01Jp4TKdo4hs8JVSzkXUUayp`</summary>

```json
{
  "command": "grep -r \"register_artifact\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515/ --include=\"*.py\" --include=\"*.json\" --include=\"*.yaml\" -l 2>/dev/null | head -5",
  "description": "Search for register_artifact tool definition"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "bad9deba-a713-4cfb-b891-7a833c8300f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LF4tiB7qd3kRKfvtuBWDin",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 112,
      "cache_read_input_tokens": 62149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 112
      },
      "output_tokens": 58,
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

_source line 44 · 2026-05-15T11:03:59.794Z_

<details><summary>↩ Tool result · `toolu_01Jp4TKdo4hs8JVSzkXUUayp`</summary>

```text
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/global/logs/workers/registry.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "801d3cef-50f2-41df-820d-fb3fea5d261d",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/global/logs/workers/registry.json",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Grep · `toolu_014VPfayfdVg4Sh9CKBq52rV`</summary>

```json
{
  "pattern": "register_artifact",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/global/logs/workers/registry.json",
  "output_mode": "content",
  "-C": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "f95b9933-2a47-45dc-b848-6ddd032caf92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYJd6JiwdPdgTbW8MZ21Tm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 172,
      "cache_read_input_tokens": 62261,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 172
      },
      "output_tokens": 66,
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

_source line 46 · 2026-05-15T11:04:02.646Z_

<details><summary>↩ Tool result · `toolu_014VPfayfdVg4Sh9CKBq52rV`</summary>

```text
69-    "params": {
70-      "repo_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing",
71:[Omitted long matching line]
72-      "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing",
73-      "tools": [
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "aa789b93-c375-4b66-8751-65842857a9cd",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "69-    \"params\": {\n70-      \"repo_path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing\",\n71:[Omitted long matching line]\n72-      \"cwd\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing\",\n73-      \"tools\": [",
    "numLines": 5
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Grep · `toolu_01SyA9sL26tnesVLM4BfheXf`</summary>

```json
{
  "pattern": "register_artifact",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515",
  "glob": "*.py",
  "output_mode": "content",
  "-C": 3,
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "d2cd7c7e-e165-4c0a-b674-c1772ab3eb20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTPzz83ac3YbpV51gpuMd2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 355,
      "cache_read_input_tokens": 62433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 355
      },
      "output_tokens": 66,
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

_source line 48 · 2026-05-15T11:04:05.725Z_

<details><summary>↩ Tool result · `toolu_01SyA9sL26tnesVLM4BfheXf`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "f8ff5b49-43f7-4b2c-84e8-4f496d4ba406",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Grep · `toolu_01PATygzxwYbh2A4wms19WHd`</summary>

```json
{
  "pattern": "register.artifact",
  "path": "/home/ubuntu/agent-ml-research",
  "glob": "*.py",
  "output_mode": "files_with_matches",
  "head_limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "8649ffaa-56e1-477b-9c18-78e9ebf6014c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U98wrDRQRj1jchYha7wMQx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 178,
      "cache_read_input_tokens": 62788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 178
      },
      "output_tokens": 54,
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

_source line 50 · 2026-05-15T11:04:09.186Z_

<details><summary>↩ Tool result · `toolu_01PATygzxwYbh2A4wms19WHd`</summary>

```text
Found 10 files limit: 10
/home/ubuntu/agent-ml-research/tests/test_plot_generation.py
/home/ubuntu/agent-ml-research/tests/test_paper_agent_tools.py
/home/ubuntu/agent-ml-research/tests/test_paper_agent_full_draft_e2e.py
/home/ubuntu/agent-ml-research/tests/test_paper_agent_patch_e2e.py
/home/ubuntu/agent-ml-research/core/tool_registry.py
/home/ubuntu/agent-ml-research/core/session_claude_md.py
/home/ubuntu/agent-ml-research/core/mcp_server.py
/home/ubuntu/agent-ml-research/tests/test_tool_imports.py
/home/ubuntu/agent-ml-research/tests/test_artifacts.py
/home/ubuntu/agent-ml-research/core/tools/agent_tools.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "357df968-e49a-4e9e-9ef2-563c09f927ff",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "/home/ubuntu/agent-ml-research/tests/test_plot_generation.py",
      "/home/ubuntu/agent-ml-research/tests/test_paper_agent_tools.py",
      "/home/ubuntu/agent-ml-research/tests/test_paper_agent_full_draft_e2e.py",
      "/home/ubuntu/agent-ml-research/tests/test_paper_agent_patch_e2e.py",
      "/home/ubuntu/agent-ml-research/core/tool_registry.py",
      "/home/ubuntu/agent-ml-research/core/session_claude_md.py",
      "/home/ubuntu/agent-ml-research/core/mcp_server.py",
      "/home/ubuntu/agent-ml-research/tests/test_tool_imports.py",
      "/home/ubuntu/agent-ml-research/tests/test_artifacts.py",
      "/home/ubuntu/agent-ml-research/core/tools/agent_tools.py"
    ],
    "numFiles": 10,
    "appliedLimit": 10
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Grep · `toolu_01VnxpzFN5QgcaC1EUSLN8sV`</summary>

```json
{
  "pattern": "def register_artifact|\\\"register_artifact\\\"|register_artifact\"",
  "path": "/home/ubuntu/agent-ml-research/core/mcp_server.py",
  "output_mode": "content",
  "-C": 5,
  "head_limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "e82f4a95-97a2-40f2-99b3-cf1f0b22cfc1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018HC7kG5kmUaMSCZq3XdSGD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 382,
      "cache_read_input_tokens": 62966,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 382
      },
      "output_tokens": 44,
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

_source line 52 · 2026-05-15T11:04:17.564Z_

<details><summary>↩ Tool result · `toolu_01VnxpzFN5QgcaC1EUSLN8sV`</summary>

```text
1558-# ---------------------------------------------------------------------------
1559-# Artifact Registry Tools
1560-# ---------------------------------------------------------------------------
1561-
1562-@mcp.tool()
1563:def register_artifact(
1564-    name: str,
1565-    type: str,
1566-    description: str,
1567-    project: str | None = None,
1568-    exp_id: str | None = None,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "8bd4c384-2b51-4f8d-ad1a-1b3a41c50ecc",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "1558-# ---------------------------------------------------------------------------\n1559-# Artifact Registry Tools\n1560-# ---------------------------------------------------------------------------\n1561-\n1562-@mcp.tool()\n1563:def register_artifact(\n1564-    name: str,\n1565-    type: str,\n1566-    description: str,\n1567-    project: str | None = None,\n1568-    exp_id: str | None = None,",
    "numLines": 11
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Read · `toolu_01Syy4dM3akoBLgBpbhkcLpd`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/mcp_server.py",
  "offset": 1558,
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "2e057a38-5247-4d75-8744-302036ffe0cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZ4y5CqSFmJpCFPss8sJGG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 269,
      "cache_read_input_tokens": 63348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 269
      },
      "output_tokens": 67,
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

_source line 54 · 2026-05-15T11:04:20.565Z_

<details><summary>↩ Tool result · `toolu_01Syy4dM3akoBLgBpbhkcLpd`</summary>

```text
1558	# ---------------------------------------------------------------------------
1559	# Artifact Registry Tools
1560	# ---------------------------------------------------------------------------
1561	
1562	@mcp.tool()
1563	def register_artifact(
1564	    name: str,
1565	    type: str,
1566	    description: str,
1567	    project: str | None = None,
1568	    exp_id: str | None = None,
1569	    source_path: str | None = None,
1570	    content: str | None = None,
1571	    content_filename: str | None = None,
1572	    url: str | None = None,
1573	    tags: list[str] | None = None,
1574	    skill: str = "",
1575	) -> str:
1576	    """Register an agent-produced artifact (chart, report, paper, data, intermediate, feishu_doc).
1577	
1578	    Args:
1579	        name: Human-readable artifact name.
1580	        type: chart | report | paper | data | intermediate | feishu_doc.
1581	        description: Brief description of the artifact.
1582	        project: Project name. None for global research scope.
1583	        exp_id: Experiment ID. None to file under project-level.
1584	        source_path: Local file to copy into artifacts directory.
1585	        content: Raw text/HTML/JSON to write directly (for proxy workers without local file access).
1586	        content_filename: Filename for written content (default: '{name}.txt').
1587	        url: External URL (e.g. Feishu doc link), mutually exclusive with source_path/content.
1588	        tags: Optional tags for filtering.
1589	        skill: Name of the skill producing this artifact.
1590	    """
1591	    result = artifacts_mod.register_artifact(
1592	        name=name, type=type, description=description,
1593	        project=project, exp_id=exp_id,
1594	        source_path=source_path, content=content, content_filename=content_filename,
1595	        url=url, tags=tags, skill=skill,
1596	    )
1597	    return _tool_result_to_str(result)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "772f6948-4fa2-4f4b-9d16-2e22d03ccfe5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/core/mcp_server.py",
      "content": "# ---------------------------------------------------------------------------\n# Artifact Registry Tools\n# ---------------------------------------------------------------------------\n\n@mcp.tool()\ndef register_artifact(\n    name: str,\n    type: str,\n    description: str,\n    project: str | None = None,\n    exp_id: str | None = None,\n    source_path: str | None = None,\n    content: str | None = None,\n    content_filename: str | None = None,\n    url: str | None = None,\n    tags: list[str] | None = None,\n    skill: str = \"\",\n) -> str:\n    \"\"\"Register an agent-produced artifact (chart, report, paper, data, intermediate, feishu_doc).\n\n    Args:\n        name: Human-readable artifact name.\n        type: chart | report | paper | data | intermediate | feishu_doc.\n        description: Brief description of the artifact.\n        project: Project name. None for global research scope.\n        exp_id: Experiment ID. None to file under project-level.\n        source_path: Local file to copy into artifacts directory.\n        content: Raw text/HTML/JSON to write directly (for proxy workers without local file access).\n        content_filename: Filename for written content (default: '{name}.txt').\n        url: External URL (e.g. Feishu doc link), mutually exclusive with source_path/content.\n        tags: Optional tags for filtering.\n        skill: Name of the skill producing this artifact.\n    \"\"\"\n    result = artifacts_mod.register_artifact(\n        name=name, type=type, description=description,\n        project=project, exp_id=exp_id,\n        source_path=source_path, content=content, content_filename=content_filename,\n        url=url, tags=tags, skill=skill,\n    )\n    return _tool_result_to_str(result)",
      "numLines": 40,
      "startLine": 1558,
      "totalLines": 5884
    }
  }
}
```

</details>

---

### Assistant

_source line 55_

Found it. It's an MCP tool but not showing in the deferred list. Let me try calling it directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "975d6aea-895a-4d71-a061-3594be3f480c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzRwGjCLWwRmx6MQfxhNVM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 675,
      "cache_read_input_tokens": 63617,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 675
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

_source line 56_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TKPhAZ5QXL47ASSbisScBD`</summary>

```json
{
  "query": "+mcp__agent-ml-research register",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "25a34fc5-a4e5-4192-95cd-9fe65266b1a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzRwGjCLWwRmx6MQfxhNVM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 675,
      "cache_read_input_tokens": 63617,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 675
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

_source line 57 · 2026-05-15T11:04:24.063Z_

<details><summary>↩ Tool result · `toolu_01TKPhAZ5QXL47ASSbisScBD`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "5f07efa3-8210-47d3-a489-20f403d526f2",
  "tool_use_result": {
    "matches": [],
    "query": "+mcp__agent-ml-research register",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016kB3Jx8oczr26kWGscbWvx`</summary>

```json
{
  "query": "register artifact save",
  "max_results": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "5d36daef-58e7-42bf-b565-3a70128d8611",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019e9WYV36xAHExCGmA9vByT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 125,
      "cache_read_input_tokens": 64292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 125
      },
      "output_tokens": 52,
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

_source line 59 · 2026-05-15T11:04:26.646Z_

<details><summary>↩ Tool result · `toolu_016kB3Jx8oczr26kWGscbWvx`</summary>

````text
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
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "f0b76973-7fa5-46d9-a753-b40435cf48ba",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "register artifact save",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 60_

<details><summary>Logged reasoning block</summary>

```text
The `register_artifact` tool isn't available as a deferred tool in my current environment. It exists in the MCP server code but isn't exposed to me. Let me just note this to the user and confirm the document is complete.

Let me verify the document was written correctly by reading it back.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "11077cdc-a2eb-4699-8ae9-02e321078d40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xkHf5pX4W7khjK4uHr9Hi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 350,
      "cache_read_input_tokens": 64417,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 350
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

_source line 61_

`register_artifact` 不在当前可用工具列表中，无法自动注册。文档已写入：

**`/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0_experiment_spec.md`**

覆盖内容：
1. **实验目标** — early-kill gate 定位，GO/NO-GO 逻辑
2. **扰动 Taxonomy** — 7→3 映射表 + 排除 Language 的理由 + Visual 类内方差风险分析
3. **模型架构** — π₀ 双 Transformer 参数 + 修正后的 12 层提取方案 + 2-layer MLP 分类器
4. **数据收集** — 580 episodes 分布 + 4 种 pooling 全存储 (~5.4 GB)
5. **评估 Protocol** — 3-class (主) / 6-class (对照) / binary (sanity check) + per-layer breakdown / activation source 对比 / pooling 对比 / t-SNE 可视化
6. **Hyperparameter Sweep** — 27 configs × 3 modes × 5-fold = 405 runs
7. **GO/NO-GO 判据** — 5 档判定 (GO/AUGMENT/RETHINK/PIVOT/信息) + chance-level 参考
8. **资源预算** — ~20 H100-hrs, 2-4 天墙钟
9. **风险与缓解** — 8 项风险 + 缓解方案
10. **附录** — SAFE 对比 / 已有代码基础 / π₀ baseline 参考值

`register_artifact` 需要你手动执行或等该工具可用后补注册。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "uuid": "351fd1b5-f017-4ed2-826f-4c48c01c873f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xkHf5pX4W7khjK4uHr9Hi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 350,
      "cache_read_input_tokens": 64417,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 350
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

### Task result

_source line 62_

`register_artifact` 不在当前可用工具列表中，无法自动注册。文档已写入：

**`/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0_experiment_spec.md`**

覆盖内容：
1. **实验目标** — early-kill gate 定位，GO/NO-GO 逻辑
2. **扰动 Taxonomy** — 7→3 映射表 + 排除 Language 的理由 + Visual 类内方差风险分析
3. **模型架构** — π₀ 双 Transformer 参数 + 修正后的 12 层提取方案 + 2-layer MLP 分类器
4. **数据收集** — 580 episodes 分布 + 4 种 pooling 全存储 (~5.4 GB)
5. **评估 Protocol** — 3-class (主) / 6-class (对照) / binary (sanity check) + per-layer breakdown / activation source 对比 / pooling 对比 / t-SNE 可视化
6. **Hyperparameter Sweep** — 27 configs × 3 modes × 5-fold = 405 runs
7. **GO/NO-GO 判据** — 5 档判定 (GO/AUGMENT/RETHINK/PIVOT/信息) + chance-level 参考
8. **资源预算** — ~20 H100-hrs, 2-4 天墙钟
9. **风险与缓解** — 8 项风险 + 缓解方案
10. **附录** — SAFE 对比 / 已有代码基础 / π₀ baseline 参考值

`register_artifact` 需要你手动执行或等该工具可用后补注册。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 243548,
  "duration_api_ms": 244274,
  "num_turns": 25,
  "stop_reason": "end_turn",
  "session_id": "6189bfff-4aac-41e8-af94-1adea0d876c7",
  "total_cost_usd": 1.0857865,
  "usage": {
    "input_tokens": 27,
    "cache_creation_input_tokens": 53320,
    "cache_read_input_tokens": 951935,
    "output_tokens": 10966,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 53320,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 3,
        "output_tokens": 576,
        "cache_read_input_tokens": 64417,
        "cache_creation_input_tokens": 350,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 350
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2204,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0022839999999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 27,
      "outputTokens": 10966,
      "cacheReadInputTokens": 951935,
      "cacheCreationInputTokens": 53320,
      "webSearchRequests": 0,
      "costUSD": 1.0835025,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "fb079e53-d7c1-49e3-aefe-6772ac335c9d"
}
```

</details>

---
