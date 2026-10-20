# analysis layer stability writeup

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 209
- **Recorded user turns:** 2
- **Tool calls:** 67
- **Original source:** `logs/workers/worker_analysis_layer-stability-writeup_20260515T160040.log`
- **Structured JSON:** [`46ba90e139b71763efc2.json`](../../sessions/46/46ba90e139b71763efc2.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
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
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "822b21e7-9946-422e-bfea-7de5bb84c29f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/memory/"
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
    "resetsAt": 1778878800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "28c6b7c9-5353-4698-a46b-a8136a27ece0",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Assistant

_source line 4_

我来完成这个分析任务。先读取项目现有的知识文件，了解已有数据和发现。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "38b363cc-e8df-4f8c-941c-17911066d47a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DwTfL51ctgwpS1gCKeFTrC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11655,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11655
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HHDnd3YVkP9ELwmzPVBVfb`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__append_idea",
  "max_results": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "04861eae-0b17-4ab8-bb55-fe6689b37810",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DwTfL51ctgwpS1gCKeFTrC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11655,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11655
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

_source line 6 · 2026-05-15T16:00:50.328Z_

<details><summary>↩ Tool result · `toolu_01HHDnd3YVkP9ELwmzPVBVfb`</summary>

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
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "347e58cf-20cb-4899-a620-569c553b1d8b",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__append_idea"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__append_idea",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me read the project's existing knowledge files to understand the current state of findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "d28e497d-d181-4880-82d7-404bd7bfc70f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HTALGWax8d9zcaN6d226qy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1542,
      "cache_read_input_tokens": 23496,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1542
      },
      "output_tokens": 20,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01ENbFbCEVVaJVE48b3bQBHy`</summary>

```json
{
  "project": "vla-ssd",
  "file": "memory.md",
  "max_chars": 20000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "1b650d08-e074-493c-bb8a-2b3f00d1d1fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HTALGWax8d9zcaN6d226qy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1542,
      "cache_read_input_tokens": 23496,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1542
      },
      "output_tokens": 20,
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

_source line 9 · 2026-05-15T16:00:55.304Z_

<details><summary>↩ Tool result · `toolu_01ENbFbCEVVaJVE48b3bQBHy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/memory.md\", \"content\": \"# VLA-SSD Project Memory\\n\\n## 文献关键发现：Vision Encoder Dominance 是已知现象（2026-05-15）\\n\\n14 篇论文调研确认，\\\"vision encoder dominates\\\" 不是我们独有的问题——Grant 2026, VLM4VLA 2025, LIBERO-Plus 2025 都独立验证。LIBERO 场景中 language 被几乎完全忽略（LIBERO-Plus: blank language input 下性能不变）。\\n\\n**突破口**：Grant et al. 2026 (arXiv:2603.19233) 发现 **LIBERO-Goal suite**（多个 goal 共享同一 visual scene）中 language 贡献关键——正确 prompt 94% vs 错误 prompt 10%。这是因为视觉本身无法区分 goal，必须依赖 instruction。\\n\\n**教训**：LIBERO-Spatial/Object 太\\\"视觉可辨\\\"，不适合测 LLM 贡献。需要 multi-goal ambiguous 场景。\\n\\n## 方向 Pivot：Instruction-Conditioned Probing > Action Prediction（2026-05-15）\\n\\n两条候选路线：\\n1. **Action Prediction Probe**：快速（今天出结果），但 story 有\\\"trivial\\\"风险——VLA 预测 action 是训练目标本身\\n2. **Instruction-Conditioned Probing on LIBERO-Goal**：story 更强（vision-inaccessible），但需下载 LIBERO-Goal 数据 + 提取特征（2-3天）\\n\\n两条线可并行。关键文献支撑：Grant et al. 2026, Buurmeijer et al. 2026 (linear probe on OpenVLA+LIBERO)。\\n\\n## Subtask Predicate Pivot 不可行（2026-05-15，Director 确认）\\n\\nLIBERO tabletop 所有 task-relevant predicates 视觉可辨。DINO AUC=0.9717 > 0.95 gate，终止（D009）。\\n\\n## D007: MVP Gate 2 FAIL（2026-05-15）\\n\\ntemporal distance probe Δρ=0.043 << 0.1。原因：temporal distance ≈ visual change，vision encoder 天然擅长。\\n\\n## MVP Clean Verdict\\n\\n| Gate | 值 | 阈值 | 结果 |\\n|------|---|------|------|\\n| G1: best_layer ρ | 0.955 (L4) | > 0.5 | PASS |\\n| G2: Δρ(trained−untrained) | 0.0427, CI [0.036, 0.050], p=0.0 | > 0.1 | FAIL |\\n| G3: VLA ρ ≥ DINO | 0.956 ≥ 0.901 | 0.901 | PASS |\\n\\n## 核心发现：Vision Encoder 主导 Temporal Distance 信号\\n\\n- Untrained OpenVLA (random LLM + SigLIP): ρ=0.933\\n- Trained OpenVLA: ρ=0.955\\n- DINO-V2: ρ=0.901\\n- VLA 训练仅贡献 ~4% ρ 提升\\n\\n## LIBERO Action Autocorrelation 极高（2026-05-15）\\n\\nCopy baseline（a_t 预测 a_{t+1}）R²=0.975，所有 task 均在 0.96–0.98。这意味着 action probe 的绝对 R² 不能直接作为\\\"hidden state 编码 action knowledge\\\"的证据——必须看 trained-vs-untrained Δ 和 per-layer 分布模式。Random-frame baseline R²≈-0.91，确认无预测力。\\n\\n## Action Probe 关键发现：Layer Stability（2026-05-15）\\n\\n**VLA 训练的主要效果不是提升 peak action R²，而是创建稳定均匀的 layer-wise action 表征。**\\n\\n- Trained: per-layer R² 平稳 (0.45–0.68)，best L19=0.683，31/33 层 > untrained\\n- Untrained: per-layer R² 极度不稳定 (0.05–0.62)，多层 probe 训练未收敛\\n- DINO 单层 R²=0.676，与 trained best 持平\\n- Same-layer Δ（如 L19: +0.28）远大于 best-vs-best Δ（0.067）\\n- Untrained L32（LLM 最后一层）是唯一接近 trained 的层——可能是 vision encoder 残留信号最近的层\\n\\n**Story 意义**：这个 stability pattern 证明 VLA 训练重组了 LLM 的表征结构——从零散的、不可靠的 vision 残留变为整个网络一致的 action 编码。\\n\\n## PCA 降维去噪效果显著（2026-05-15）\\n\\nPCA 1024 dim（保留 99.85% 方差）将 trained L4 action R² 从 0.536 提升到 0.671（+25%）。去除噪声维度后 probe 效果更好。可用于 G3 公平比较（与 DINO 同维度 1024→256→7）。\\n\\n## Layer Collapse 问题\\n\\ntemporal distance: 33 层中 16 层坍塌（ρ=0.0）。Best layer = L4。17 个健康层中 16 个 Δρ 正向。\\naction prediction: untrained 多层严重不稳定（R²<0.25 的层: L4=0.05, L5=0.16, L8=0.17, L11=0.23, L14=0.20, L26=0.18），trained 无此问题。\\n\\n## 技术约束\\n\\n- RoPE 不构成 confound（独立 forward pass）\\n- Bootstrap CI 必须 task-level 采样（10 tasks 的 per-task ρ）\\n- Token 聚合：Primary = last pre-action token\\n- 存储：根分区 ~30GB，大文件在 /root/autodl-tmp/vla-ssd/\\n- 特征提取 I/O 优化：52x 加速（264→2 次 .cpu()/batch）\\n- Untrained model: from_config() 重新初始化 LLM（6.74B random），保留 SigLIP（0.80B）\\n- transformers 版本差异（4.40.1 vs 4.57.6），trained/untrained 同版本，对比有效\\n- AutoDL: source /etc/network_turbo, HF_HUB_DISABLE_XET=1, SSL certs\\n- 多 Worker 下载抢带宽，严格单进程下载\\n- Worker 用 nohup 启动实验是 anti-pattern——必须用 submit_training_job（tmux+cron 监控）\\n\", \"total_chars\": 3282, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "c2a6ac58-2aa0-470f-ae7d-9cae5702f769",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/memory.md\\\", \\\"content\\\": \\\"# VLA-SSD Project Memory\\\\n\\\\n## 文献关键发现：Vision Encoder Dominance 是已知现象（2026-05-15）\\\\n\\\\n14 篇论文调研确认，\\\\\\\"vision encoder dominates\\\\\\\" 不是我们独有的问题——Grant 2026, VLM4VLA 2025, LIBERO-Plus 2025 都独立验证。LIBERO 场景中 language 被几乎完全忽略（LIBERO-Plus: blank language input 下性能不变）。\\\\n\\\\n**突破口**：Grant et al. 2026 (arXiv:2603.19233) 发现 **LIBERO-Goal suite**（多个 goal 共享同一 visual scene）中 language 贡献关键——正确 prompt 94% vs 错误 prompt 10%。这是因为视觉本身无法区分 goal，必须依赖 instruction。\\\\n\\\\n**教训**：LIBERO-Spatial/Object 太\\\\\\\"视觉可辨\\\\\\\"，不适合测 LLM 贡献。需要 multi-goal ambiguous 场景。\\\\n\\\\n## 方向 Pivot：Instruction-Conditioned Probing > Action Prediction（2026-05-15）\\\\n\\\\n两条候选路线：\\\\n1. **Action Prediction Probe**：快速（今天出结果），但 story 有\\\\\\\"trivial\\\\\\\"风险——VLA 预测 action 是训练目标本身\\\\n2. **Instruction-Conditioned Probing on LIBERO-Goal**：story 更强（vision-inaccessible），但需下载 LIBERO-Goal 数据 + 提取特征（2-3天）\\\\n\\\\n两条线可并行。关键文献支撑：Grant et al. 2026, Buurmeijer et al. 2026 (linear probe on OpenVLA+LIBERO)。\\\\n\\\\n## Subtask Predicate Pivot 不可行（2026-05-15，Director 确认）\\\\n\\\\nLIBERO tabletop 所有 task-relevant predicates 视觉可辨。DINO AUC=0.9717 > 0.95 gate，终止（D009）。\\\\n\\\\n## D007: MVP Gate 2 FAIL（2026-05-15）\\\\n\\\\ntemporal distance probe Δρ=0.043 << 0.1。原因：temporal distance ≈ visual change，vision encoder 天然擅长。\\\\n\\\\n## MVP Clean Verdict\\\\n\\\\n| Gate | 值 | 阈值 | 结果 |\\\\n|------|---|------|------|\\\\n| G1: best_layer ρ | 0.955 (L4) | > 0.5 | PASS |\\\\n| G2: Δρ(trained−untrained) | 0.0427, CI [0.036, 0.050], p=0.0 | > 0.1 | FAIL |\\\\n| G3: VLA ρ ≥ DINO | 0.956 ≥ 0.901 | 0.901 | PASS |\\\\n\\\\n## 核心发现：Vision Encoder 主导 Temporal Distance 信号\\\\n\\\\n- Untrained OpenVLA (random LLM + SigLIP): ρ=0.933\\\\n- Trained OpenVLA: ρ=0.955\\\\n- DINO-V2: ρ=0.901\\\\n- VLA 训练仅贡献 ~4% ρ 提升\\\\n\\\\n## LIBERO Action Autocorrelation 极高（2026-05-15）\\\\n\\\\nCopy baseline（a_t 预测 a_{t+1}）R²=0.975，所有 task 均在 0.96–0.98。这意味着 action probe 的绝对 R² 不能直接作为\\\\\\\"hidden state 编码 action knowledge\\\\\\\"的证据——必须看 trained-vs-untrained Δ 和 per-layer 分布模式。Random-frame baseline R²≈-0.91，确认无预测力。\\\\n\\\\n## Action Probe 关键发现：Layer Stability（2026-05-15）\\\\n\\\\n**VLA 训练的主要效果不是提升 peak action R²，而是创建稳定均匀的 layer-wise action 表征。**\\\\n\\\\n- Trained: per-layer R² 平稳 (0.45–0.68)，best L19=0.683，31/33 层 > untrained\\\\n- Untrained: per-layer R² 极度不稳定 (0.05–0.62)，多层 probe 训练未收敛\\\\n- DINO 单层 R²=0.676，与 trained best 持平\\\\n- Same-layer Δ（如 L19: +0.28）远大于 best-vs-best Δ（0.067）\\\\n- Untrained L32（LLM 最后一层）是唯一接近 trained 的层——可能是 vision encoder 残留信号最近的层\\\\n\\\\n**Story 意义**：这个 stability pattern 证明 VLA 训练重组了 LLM 的表征结构——从零散的、不可靠的 vision 残留变为整个网络一致的 action 编码。\\\\n\\\\n## PCA 降维去噪效果显著（2026-05-15）\\\\n\\\\nPCA 1024 dim（保留 99.85% 方差）将 trained L4 action R² 从 0.536 提升到 0.671（+25%）。去除噪声维度后 probe 效果更好。可用于 G3 公平比较（与 DINO 同维度 1024→256→7）。\\\\n\\\\n## Layer Collapse 问题\\\\n\\\\ntemporal distance: 33 层中 16 层坍塌（ρ=0.0）。Best layer = L4。17 个健康层中 16 个 Δρ 正向。\\\\naction prediction: untrained 多层严重不稳定（R²<0.25 的层: L4=0.05, L5=0.16, L8=0.17, L11=0.23, L14=0.20, L26=0.18），trained 无此问题。\\\\n\\\\n## 技术约束\\\\n\\\\n- RoPE 不构成 confound（独立 forward pass）\\\\n- Bootstrap CI 必须 task-level 采样（10 tasks 的 per-task ρ）\\\\n- Token 聚合：Primary = last pre-action token\\\\n- 存储：根分区 ~30GB，大文件在 /root/autodl-tmp/vla-ssd/\\\\n- 特征提取 I/O 优化：52x 加速（264→2 次 .cpu()/batch）\\\\n- Untrained model: from_config() 重新初始化 LLM（6.74B random），保留 SigLIP（0.80B）\\\\n- transformers 版本差异（4.40.1 vs 4.57.6），trained/untrained 同版本，对比有效\\\\n- AutoDL: source /etc/network_turbo, HF_HUB_DISABLE_XET=1, SSL certs\\\\n- 多 Worker 下载抢带宽，严格单进程下载\\\\n- Worker 用 nohup 启动实验是 anti-pattern——必须用 submit_training_job（tmux+cron 监控）\\\\n\\\", \\\"total_chars\\\": 3282, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/memory.md\", \"content\": \"# VLA-SSD Project Memory\\n\\n## 文献关键发现：Vision Encoder Dominance 是已知现象（2026-05-15）\\n\\n14 篇论文调研确认，\\\"vision encoder dominates\\\" 不是我们独有的问题——Grant 2026, VLM4VLA 2025, LIBERO-Plus 2025 都独立验证。LIBERO 场景中 language 被几乎完全忽略（LIBERO-Plus: blank language input 下性能不变）。\\n\\n**突破口**：Grant et al. 2026 (arXiv:2603.19233) 发现 **LIBERO-Goal suite**（多个 goal 共享同一 visual scene）中 language 贡献关键——正确 prompt 94% vs 错误 prompt 10%。这是因为视觉本身无法区分 goal，必须依赖 instruction。\\n\\n**教训**：LIBERO-Spatial/Object 太\\\"视觉可辨\\\"，不适合测 LLM 贡献。需要 multi-goal ambiguous 场景。\\n\\n## 方向 Pivot：Instruction-Conditioned Probing > Action Prediction（2026-05-15）\\n\\n两条候选路线：\\n1. **Action Prediction Probe**：快速（今天出结果），但 story 有\\\"trivial\\\"风险——VLA 预测 action 是训练目标本身\\n2. **Instruction-Conditioned Probing on LIBERO-Goal**：story 更强（vision-inaccessible），但需下载 LIBERO-Goal 数据 + 提取特征（2-3天）\\n\\n两条线可并行。关键文献支撑：Grant et al. 2026, Buurmeijer et al. 2026 (linear probe on OpenVLA+LIBERO)。\\n\\n## Subtask Predicate Pivot 不可行（2026-05-15，Director 确认）\\n\\nLIBERO tabletop 所有 task-relevant predicates 视觉可辨。DINO AUC=0.9717 > 0.95 gate，终止（D009）。\\n\\n## D007: MVP Gate 2 FAIL（2026-05-15）\\n\\ntemporal distance probe Δρ=0.043 << 0.1。原因：temporal distance ≈ visual change，vision encoder 天然擅长。\\n\\n## MVP Clean Verdict\\n\\n| Gate | 值 | 阈值 | 结果 |\\n|------|---|------|------|\\n| G1: best_layer ρ | 0.955 (L4) | > 0.5 | PASS |\\n| G2: Δρ(trained−untrained) | 0.0427, CI [0.036, 0.050], p=0.0 | > 0.1 | FAIL |\\n| G3: VLA ρ ≥ DINO | 0.956 ≥ 0.901 | 0.901 | PASS |\\n\\n## 核心发现：Vision Encoder 主导 Temporal Distance 信号\\n\\n- Untrained OpenVLA (random LLM + SigLIP): ρ=0.933\\n- Trained OpenVLA: ρ=0.955\\n- DINO-V2: ρ=0.901\\n- VLA 训练仅贡献 ~4% ρ 提升\\n\\n## LIBERO Action Autocorrelation 极高（2026-05-15）\\n\\nCopy baseline（a_t 预测 a_{t+1}）R²=0.975，所有 task 均在 0.96–0.98。这意味着 action probe 的绝对 R² 不能直接作为\\\"hidden state 编码 action knowledge\\\"的证据——必须看 trained-vs-untrained Δ 和 per-layer 分布模式。Random-frame baseline R²≈-0.91，确认无预测力。\\n\\n## Action Probe 关键发现：Layer Stability（2026-05-15）\\n\\n**VLA 训练的主要效果不是提升 peak action R²，而是创建稳定均匀的 layer-wise action 表征。**\\n\\n- Trained: per-layer R² 平稳 (0.45–0.68)，best L19=0.683，31/33 层 > untrained\\n- Untrained: per-layer R² 极度不稳定 (0.05–0.62)，多层 probe 训练未收敛\\n- DINO 单层 R²=0.676，与 trained best 持平\\n- Same-layer Δ（如 L19: +0.28）远大于 best-vs-best Δ（0.067）\\n- Untrained L32（LLM 最后一层）是唯一接近 trained 的层——可能是 vision encoder 残留信号最近的层\\n\\n**Story 意义**：这个 stability pattern 证明 VLA 训练重组了 LLM 的表征结构——从零散的、不可靠的 vision 残留变为整个网络一致的 action 编码。\\n\\n## PCA 降维去噪效果显著（2026-05-15）\\n\\nPCA 1024 dim（保留 99.85% 方差）将 trained L4 action R² 从 0.536 提升到 0.671（+25%）。去除噪声维度后 probe 效果更好。可用于 G3 公平比较（与 DINO 同维度 1024→256→7）。\\n\\n## Layer Collapse 问题\\n\\ntemporal distance: 33 层中 16 层坍塌（ρ=0.0）。Best layer = L4。17 个健康层中 16 个 Δρ 正向。\\naction prediction: untrained 多层严重不稳定（R²<0.25 的层: L4=0.05, L5=0.16, L8=0.17, L11=0.23, L14=0.20, L26=0.18），trained 无此问题。\\n\\n## 技术约束\\n\\n- RoPE 不构成 confound（独立 forward pass）\\n- Bootstrap CI 必须 task-level 采样（10 tasks 的 per-task ρ）\\n- Token 聚合：Primary = last pre-action token\\n- 存储：根分区 ~30GB，大文件在 /root/autodl-tmp/vla-ssd/\\n- 特征提取 I/O 优化：52x 加速（264→2 次 .cpu()/batch）\\n- Untrained model: from_config() 重新初始化 LLM（6.74B random），保留 SigLIP（0.80B）\\n- transformers 版本差异（4.40.1 vs 4.57.6），trained/untrained 同版本，对比有效\\n- AutoDL: source /etc/network_turbo, HF_HUB_DISABLE_XET=1, SSL certs\\n- 多 Worker 下载抢带宽，严格单进程下载\\n- Worker 用 nohup 启动实验是 anti-pattern——必须用 submit_training_job（tmux+cron 监控）\\n\", \"total_chars\": 3282, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0183vrPEcniAYAPht3dyioLf`</summary>

```json
{
  "project": "vla-ssd",
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
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "416cdc6c-4c0a-481d-b5fd-ff9deb2cd135",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HTALGWax8d9zcaN6d226qy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1542,
      "cache_read_input_tokens": 23496,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1542
      },
      "output_tokens": 20,
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

_source line 11 · 2026-05-15T16:00:56.427Z_

<details><summary>↩ Tool result · `toolu_0183vrPEcniAYAPht3dyioLf`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'vla-ssd'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "4b20334b-7141-4905-a897-405138714007",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"No ideas.md found for 'vla-ssd'.\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'vla-ssd'.\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01UbTJC92Dhw8tKTZjRCa61p`</summary>

```json
{
  "project": "vla-ssd",
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
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "82c2876b-ae8f-40c1-84b1-d58ca85919ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HTALGWax8d9zcaN6d226qy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1542,
      "cache_read_input_tokens": 23496,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1542
      },
      "output_tokens": 20,
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

_source line 13 · 2026-05-15T16:00:56.520Z_

<details><summary>↩ Tool result · `toolu_01UbTJC92Dhw8tKTZjRCa61p`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ROADMAP.md\", \"content\": \"# vla-ssd — Research Dashboard\\n\\n> 最后更新: 2026-05-15 15:26 UTC | 更新原因: D013: MVP-2 action-delta 也 vision-dominated，三条探测路线全部 FAIL。方向决策点。\\n\\n## 核心方向\\n\\nVLA 预训练表征是否编码了 vision encoder 不具备的信息？如果有，在哪个维度、什么场景下体现？\\n\\n**当前状态**：MVP-1 + MVP-2 均 FAIL（vision-dominated）。唯一 VLA-specific 发现：layer stability。待决策是否 pivot 到 LIBERO-Goal。\\n\\n## 当前进展\\n\\n- **阶段**: MVP-2 完成，等待方向决策\\n- **MVP-1 Temporal Distance**: G2 FAIL (Δρ=0.043 << 0.1)，vision encoder 主导\\n- **MVP-2 Action Prediction**: G2 FAIL (ΔR²=0.067), G3 FAIL (Δ=0.007 vs DINO)\\n- **MVP-2 Action-Delta**: G1-delta borderline PASS (0.059>0.05), G3-delta FAIL (DINO 0.061 ≈ trained 0.059)\\n- **跨 MVP 一致发现**: VLA 训练创造稳定表征通路（trained 31/33 层有效 vs untrained ~15/33），但信息内容不超越纯视觉\\n- **PCA 控制**: 运行中（~10 min），预期不改变结论（降维损失极小）\\n\\n## 方向决策（待用户确认）\\n\\n**Option A: Pivot 到 LIBERO-Goal instruction-conditioned probing**\\n- 依据：Grant et al. 2026 证明 LIBERO-Goal 中 language 关键（correct 94% vs wrong 10%），vision 无法区分 goal\\n- 假设：VLA 训练的贡献不在视觉/动作知识，而在 language grounding——只有 vision-ambiguous 场景才能暴露\\n- 工作量：数据下载 + 特征提取 + probing 实验，AI 团队 2-3 天\\n- 风险：如果 language probe 也 vision-dominated（不太可能但存在），项目需终止\\n\\n**Option B: 以 negative result + layer stability 发现写分析型论文**\\n- story: \\\"What does VLA training actually learn? A systematic probing study\\\"\\n- 弱点：单模型（OpenVLA）+ 单 benchmark（LIBERO-10）= 泛化性不足，需扩展\\n\\n**Option C: 终止项目**\\n\\n## GPU 预算\\n\\nwestd-19183: 2×RTX PRO 6000 | 当前 0/2 占用（实验完成）+ PCA 后台\\n\\n## 目标会议\\n\\nCoRL 2026（abstract May 26 = 11天, paper May 29 = 14天）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D014 | 2026-05-15 | MVP-2 判死：action prediction + action-delta 三轮 probi | mvp2_action_trained, mvp2_action_untrained, mvp2_action_dino, mvp_probe_trained, mvp_probe_untrained |\\n| D013 | 2026-05-15 | MVP-2 Action Prediction 综合判定：G3-delta FAIL（DINO 0. | mvp2_action_trained, mvp2_action_untrained, mvp2_action_dino |\\n| D012 | 2026-05-15 | D012: Copy baseline R²=0.97 暴露 G1 阈值无效。增加 action-d | mvp2_action_trained, mvp2_action_untrained |\\n| D011 | 2026-05-15 | Control B 两组实验均确认 null hypothesis（shuffled labels  | mvp_controlb_trained, mvp_controlb_untrained, mvp_probe_trained, mvp_probe_untrained, dinov2_baseline |\\n| D010 | 2026-05-15 | 批准 Action Prediction Probe 作为 MVP-2 方向。设定三门判定：G1 R | mvp_probe_trained, mvp_probe_untrained, dinov2_baseline, mvp_controlb_trained, mvp_controlb_untrained |\\n| D009 | 2026-05-15 | Subtask predicate pivot 终止。DINO auto-extracted sub | dinov2_baseline, mvp_probe_trained, mvp_probe_untrained |\\n| D008 | 2026-05-15 | MVP Gate 2 确认 FAIL（clean verdict）。Subtask predicat | mvp_probe_trained, mvp_probe_untrained, dinov2_baseline, mvp_controlb_trained, mvp_controlb_untrained |\\n| D007 | 2026-05-15 | MVP Gate 2 FAIL 确认：33 层全结果，非坍塌层最大 Δρ=0.043 << 0.1。 | mvp_probe_trained, mvp_probe_untrained, dinov2_baseline |\\n| D006 | 2026-05-15 | DINO baseline invalidated: 旧管道 ρ=0.554 作废，新管道 ρ=0. | dinov2_baseline, mvp_probe_trained, mvp_probe_untrained |\\n| D005 | 2026-05-15 | D004 DINO gate 阈值作废：0.554→0.901。旧值基于 500 pairs/tas | dinov2_baseline, mvp_probe_trained, mvp_probe_untrained |\\n\\n\", \"total_chars\": 3000, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "deb12753-f09e-4792-b7d5-6258c9654f71",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ROADMAP.md\\\", \\\"content\\\": \\\"# vla-ssd — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-15 15:26 UTC | 更新原因: D013: MVP-2 action-delta 也 vision-dominated，三条探测路线全部 FAIL。方向决策点。\\\\n\\\\n## 核心方向\\\\n\\\\nVLA 预训练表征是否编码了 vision encoder 不具备的信息？如果有，在哪个维度、什么场景下体现？\\\\n\\\\n**当前状态**：MVP-1 + MVP-2 均 FAIL（vision-dominated）。唯一 VLA-specific 发现：layer stability。待决策是否 pivot 到 LIBERO-Goal。\\\\n\\\\n## 当前进展\\\\n\\\\n- **阶段**: MVP-2 完成，等待方向决策\\\\n- **MVP-1 Temporal Distance**: G2 FAIL (Δρ=0.043 << 0.1)，vision encoder 主导\\\\n- **MVP-2 Action Prediction**: G2 FAIL (ΔR²=0.067), G3 FAIL (Δ=0.007 vs DINO)\\\\n- **MVP-2 Action-Delta**: G1-delta borderline PASS (0.059>0.05), G3-delta FAIL (DINO 0.061 ≈ trained 0.059)\\\\n- **跨 MVP 一致发现**: VLA 训练创造稳定表征通路（trained 31/33 层有效 vs untrained ~15/33），但信息内容不超越纯视觉\\\\n- **PCA 控制**: 运行中（~10 min），预期不改变结论（降维损失极小）\\\\n\\\\n## 方向决策（待用户确认）\\\\n\\\\n**Option A: Pivot 到 LIBERO-Goal instruction-conditioned probing**\\\\n- 依据：Grant et al. 2026 证明 LIBERO-Goal 中 language 关键（correct 94% vs wrong 10%），vision 无法区分 goal\\\\n- 假设：VLA 训练的贡献不在视觉/动作知识，而在 language grounding——只有 vision-ambiguous 场景才能暴露\\\\n- 工作量：数据下载 + 特征提取 + probing 实验，AI 团队 2-3 天\\\\n- 风险：如果 language probe 也 vision-dominated（不太可能但存在），项目需终止\\\\n\\\\n**Option B: 以 negative result + layer stability 发现写分析型论文**\\\\n- story: \\\\\\\"What does VLA training actually learn? A systematic probing study\\\\\\\"\\\\n- 弱点：单模型（OpenVLA）+ 单 benchmark（LIBERO-10）= 泛化性不足，需扩展\\\\n\\\\n**Option C: 终止项目**\\\\n\\\\n## GPU 预算\\\\n\\\\nwestd-19183: 2×RTX PRO 6000 | 当前 0/2 占用（实验完成）+ PCA 后台\\\\n\\\\n## 目标会议\\\\n\\\\nCoRL 2026（abstract May 26 = 11天, paper May 29 = 14天）\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D014 | 2026-05-15 | MVP-2 判死：action prediction + action-delta 三轮 probi | mvp2_action_trained, mvp2_action_untrained, mvp2_action_dino, mvp_probe_trained, mvp_probe_untrained |\\\\n| D013 | 2026-05-15 | MVP-2 Action Prediction 综合判定：G3-delta FAIL（DINO 0. | mvp2_action_trained, mvp2_action_untrained, mvp2_action_dino |\\\\n| D012 | 2026-05-15 | D012: Copy baseline R²=0.97 暴露 G1 阈值无效。增加 action-d | mvp2_action_trained, mvp2_action_untrained |\\\\n| D011 | 2026-05-15 | Control B 两组实验均确认 null hypothesis（shuffled labels  | mvp_controlb_trained, mvp_controlb_untrained, mvp_probe_trained, mvp_probe_untrained, dinov2_baseline |\\\\n| D010 | 2026-05-15 | 批准 Action Prediction Probe 作为 MVP-2 方向。设定三门判定：G1 R | mvp_probe_trained, mvp_probe_untrained, dinov2_baseline, mvp_controlb_trained, mvp_controlb_untrained |\\\\n| D009 | 2026-05-15 | Subtask predicate pivot 终止。DINO auto-extracted sub | dinov2_baseline, mvp_probe_trained, mvp_probe_untrained |\\\\n| D008 | 2026-05-15 | MVP Gate 2 确认 FAIL（clean verdict）。Subtask predicat | mvp_probe_trained, mvp_probe_untrained, dinov2_baseline, mvp_controlb_trained, mvp_controlb_untrained |\\\\n| D007 | 2026-05-15 | MVP Gate 2 FAIL 确认：33 层全结果，非坍塌层最大 Δρ=0.043 << 0.1。 | mvp_probe_trained, mvp_probe_untrained, dinov2_baseline |\\\\n| D006 | 2026-05-15 | DINO baseline invalidated: 旧管道 ρ=0.554 作废，新管道 ρ=0. | dinov2_baseline, mvp_probe_trained, mvp_probe_untrained |\\\\n| D005 | 2026-05-15 | D004 DINO gate 阈值作废：0.554→0.901。旧值基于 500 pairs/tas | dinov2_baseline, mvp_probe_trained, mvp_probe_untrained |\\\\n\\\\n\\\", \\\"total_chars\\\": 3000, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ROADMAP.md\", \"content\": \"# vla-ssd — Research Dashboard\\n\\n> 最后更新: 2026-05-15 15:26 UTC | 更新原因: D013: MVP-2 action-delta 也 vision-dominated，三条探测路线全部 FAIL。方向决策点。\\n\\n## 核心方向\\n\\nVLA 预训练表征是否编码了 vision encoder 不具备的信息？如果有，在哪个维度、什么场景下体现？\\n\\n**当前状态**：MVP-1 + MVP-2 均 FAIL（vision-dominated）。唯一 VLA-specific 发现：layer stability。待决策是否 pivot 到 LIBERO-Goal。\\n\\n## 当前进展\\n\\n- **阶段**: MVP-2 完成，等待方向决策\\n- **MVP-1 Temporal Distance**: G2 FAIL (Δρ=0.043 << 0.1)，vision encoder 主导\\n- **MVP-2 Action Prediction**: G2 FAIL (ΔR²=0.067), G3 FAIL (Δ=0.007 vs DINO)\\n- **MVP-2 Action-Delta**: G1-delta borderline PASS (0.059>0.05), G3-delta FAIL (DINO 0.061 ≈ trained 0.059)\\n- **跨 MVP 一致发现**: VLA 训练创造稳定表征通路（trained 31/33 层有效 vs untrained ~15/33），但信息内容不超越纯视觉\\n- **PCA 控制**: 运行中（~10 min），预期不改变结论（降维损失极小）\\n\\n## 方向决策（待用户确认）\\n\\n**Option A: Pivot 到 LIBERO-Goal instruction-conditioned probing**\\n- 依据：Grant et al. 2026 证明 LIBERO-Goal 中 language 关键（correct 94% vs wrong 10%），vision 无法区分 goal\\n- 假设：VLA 训练的贡献不在视觉/动作知识，而在 language grounding——只有 vision-ambiguous 场景才能暴露\\n- 工作量：数据下载 + 特征提取 + probing 实验，AI 团队 2-3 天\\n- 风险：如果 language probe 也 vision-dominated（不太可能但存在），项目需终止\\n\\n**Option B: 以 negative result + layer stability 发现写分析型论文**\\n- story: \\\"What does VLA training actually learn? A systematic probing study\\\"\\n- 弱点：单模型（OpenVLA）+ 单 benchmark（LIBERO-10）= 泛化性不足，需扩展\\n\\n**Option C: 终止项目**\\n\\n## GPU 预算\\n\\nwestd-19183: 2×RTX PRO 6000 | 当前 0/2 占用（实验完成）+ PCA 后台\\n\\n## 目标会议\\n\\nCoRL 2026（abstract May 26 = 11天, paper May 29 = 14天）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D014 | 2026-05-15 | MVP-2 判死：action prediction + action-delta 三轮 probi | mvp2_action_trained, mvp2_action_untrained, mvp2_action_dino, mvp_probe_trained, mvp_probe_untrained |\\n| D013 | 2026-05-15 | MVP-2 Action Prediction 综合判定：G3-delta FAIL（DINO 0. | mvp2_action_trained, mvp2_action_untrained, mvp2_action_dino |\\n| D012 | 2026-05-15 | D012: Copy baseline R²=0.97 暴露 G1 阈值无效。增加 action-d | mvp2_action_trained, mvp2_action_untrained |\\n| D011 | 2026-05-15 | Control B 两组实验均确认 null hypothesis（shuffled labels  | mvp_controlb_trained, mvp_controlb_untrained, mvp_probe_trained, mvp_probe_untrained, dinov2_baseline |\\n| D010 | 2026-05-15 | 批准 Action Prediction Probe 作为 MVP-2 方向。设定三门判定：G1 R | mvp_probe_trained, mvp_probe_untrained, dinov2_baseline, mvp_controlb_trained, mvp_controlb_untrained |\\n| D009 | 2026-05-15 | Subtask predicate pivot 终止。DINO auto-extracted sub | dinov2_baseline, mvp_probe_trained, mvp_probe_untrained |\\n| D008 | 2026-05-15 | MVP Gate 2 确认 FAIL（clean verdict）。Subtask predicat | mvp_probe_trained, mvp_probe_untrained, dinov2_baseline, mvp_controlb_trained, mvp_controlb_untrained |\\n| D007 | 2026-05-15 | MVP Gate 2 FAIL 确认：33 层全结果，非坍塌层最大 Δρ=0.043 << 0.1。 | mvp_probe_trained, mvp_probe_untrained, dinov2_baseline |\\n| D006 | 2026-05-15 | DINO baseline invalidated: 旧管道 ρ=0.554 作废，新管道 ρ=0. | dinov2_baseline, mvp_probe_trained, mvp_probe_untrained |\\n| D005 | 2026-05-15 | D004 DINO gate 阈值作废：0.554→0.901。旧值基于 500 pairs/tas | dinov2_baseline, mvp_probe_trained, mvp_probe_untrained |\\n\\n\", \"total_chars\": 3000, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the project state. Let me also read the paper_framing.md and any existing literature map.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "709d5f2d-df29-48ae-ab7a-3c568f533e71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TotfPJwf5yjGwrjG6TsjCJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4326,
      "cache_read_input_tokens": 25038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4326
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

Let me also check the existing literature map and any other relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "05dd177a-a6af-41c3-8f75-0638301abbc6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TotfPJwf5yjGwrjG6TsjCJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4326,
      "cache_read_input_tokens": 25038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4326
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017mVqySCCfNofGeA8TQsB9W`</summary>

```json
{
  "project": "vla-ssd",
  "file": "literature_map.yaml",
  "max_chars": 20000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "d844aedf-39c8-47ec-b666-6d4fde2e376c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TotfPJwf5yjGwrjG6TsjCJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4326,
      "cache_read_input_tokens": 25038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4326
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

_source line 17 · 2026-05-15T16:01:00.818Z_

<details><summary>↩ Tool result · `toolu_017mVqySCCfNofGeA8TQsB9W`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'vla-ssd'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "095a660c-cc5b-4380-968f-6018280fc319",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"No literature_map.yaml found for 'vla-ssd'.\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'vla-ssd'.\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FQ1NWLbFScXDGoyno6eXRy`</summary>

```json
{
  "project": "vla-ssd",
  "file": "paper_framing.md",
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
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "1ab9627a-83cc-4c94-8118-3f6adfc83863",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TotfPJwf5yjGwrjG6TsjCJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4326,
      "cache_read_input_tokens": 25038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4326
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

_source line 19 · 2026-05-15T16:01:01.239Z_

<details><summary>↩ Tool result · `toolu_01FQ1NWLbFScXDGoyno6eXRy`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_framing.md found for 'vla-ssd'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "b3b2401e-4125-48bb-8d74-6c7761e1b5f2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"No paper_framing.md found for 'vla-ssd'.\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"No paper_framing.md found for 'vla-ssd'.\", \"metadata\": {}}"
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
OK, let me now do the literature search and analysis. I have all the data I need from memory.md and ROADMAP.md. Let me now conduct the research and write the analysis document.

Let me search for relevant literature on layer-wise representation analysis, representation stability, layer collapse, and neural collapse in LLMs/VLMs/VLAs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "8853b9d3-a2d5-4d60-800a-ba6ffaa16a38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X44HpbQVj3mhrvTZPhbpA5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 436,
      "cache_read_input_tokens": 29364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 436
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

Now let me conduct literature research and the analysis in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "7b6ced43-a52f-40a1-be70-c1cf18c48103",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X44HpbQVj3mhrvTZPhbpA5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 436,
      "cache_read_input_tokens": 29364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 436
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

<details open><summary>🔧 Tool call — Agent · `toolu_01DAK3KN1UWBh3EPawus774g`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Literature search: layer-wise probing LLM",
  "prompt": "Search the web for academic papers on these specific topics. I need concrete paper titles, authors, years, and key findings. Search thoroughly.\n\n**Topic 1: Layer-wise probing in LLMs/VLMs**\n- Papers that probe individual layers of large language models or vision-language models for specific properties\n- Especially: papers that show per-layer performance curves (e.g., layer-wise accuracy or R² for probes)\n- Key papers to find: Tenney et al. \"BERT Rediscovers the Classical NLP Pipeline\" (2019), Hewitt & Manning \"A Structural Probe for Finding Syntax\" (2019), any similar work on LLaMA/Llama-2/Llama-3\n\n**Topic 2: Representation stability across layers**\n- Papers discussing how fine-tuning changes layer-wise representations\n- \"Representation geometry\" papers (e.g., CKA similarity, centered kernel alignment across layers)\n- Papers that measure how uniformly information is distributed across layers before vs after training/fine-tuning\n\n**Topic 3: Layer collapse / neural collapse in deep networks**\n- \"Neural Collapse\" (Papyan et al. 2020) and follow-up work\n- Layer collapse in transformers specifically\n- Any papers showing that untrained/randomly initialized models have \"collapsed\" representations in certain layers\n- Feature rank deficiency across layers\n\n**Topic 4: VLA fine-tuning effects on LLM backbone**\n- How does action fine-tuning (robot learning) change the internal representations of a pre-trained LLM?\n- Papers: Buurmeijer et al. 2026, Grant et al. 2026, any probing studies on OpenVLA, RT-2, or Octo\n- \"What does VLA training actually learn?\" type analyses\n\nFor each paper found, provide: Title, Authors, Year, Venue, and a 1-2 sentence summary of the key finding relevant to our topic.\n\nReport in a structured format grouped by topic."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "6d3aa52a-bf72-4dbe-b739-f5faefd9c0c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X44HpbQVj3mhrvTZPhbpA5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 436,
      "cache_read_input_tokens": 29364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 436
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

### System

_source line 23_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Literature search: layer-wise probing LLM",
  "task_type": "local_agent",
  "prompt": "Search the web for academic papers on these specific topics. I need concrete paper titles, authors, years, and key findings. Search thoroughly.\n\n**Topic 1: Layer-wise probing in LLMs/VLMs**\n- Papers that probe individual layers of large language models or vision-language models for specific properties\n- Especially: papers that show per-layer performance curves (e.g., layer-wise accuracy or R² for probes)\n- Key papers to find: Tenney et al. \"BERT Rediscovers the Classical NLP Pipeline\" (2019), Hewitt & Manning \"A Structural Probe for Finding Syntax\" (2019), any similar work on LLaMA/Llama-2/Llama-3\n\n**Topic 2: Representation stability across layers**\n- Papers discussing how fine-tuning changes layer-wise representations\n- \"Representation geometry\" papers (e.g., CKA similarity, centered kernel alignment across layers)\n- Papers that measure how uniformly information is distributed across layers before vs after training/fine-tuning\n\n**Topic 3: Layer collapse / neural collapse in deep networks**\n- \"Neural Collapse\" (Papyan et al. 2020) and follow-up work\n- Layer collapse in transformers specifically\n- Any papers showing that untrained/randomly initialized models have \"collapsed\" representations in certain layers\n- Feature rank deficiency across layers\n\n**Topic 4: VLA fine-tuning effects on LLM backbone**\n- How does action fine-tuning (robot learning) change the internal representations of a pre-trained LLM?\n- Papers: Buurmeijer et al. 2026, Grant et al. 2026, any probing studies on OpenVLA, RT-2, or Octo\n- \"What does VLA training actually learn?\" type analyses\n\nFor each paper found, provide: Title, Authors, Year, Venue, and a 1-2 sentence summary of the key finding relevant to our topic.\n\nReport in a structured format grouped by topic.",
  "uuid": "7afc1349-0258-426e-a6c9-7052306027e6",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

## Round 1

16 recorded events

### User

_source line 24 · 2026-05-15T16:01:18.452Z_

Search the web for academic papers on these specific topics. I need concrete paper titles, authors, years, and key findings. Search thoroughly.

**Topic 1: Layer-wise probing in LLMs/VLMs**
- Papers that probe individual layers of large language models or vision-language models for specific properties
- Especially: papers that show per-layer performance curves (e.g., layer-wise accuracy or R² for probes)
- Key papers to find: Tenney et al. "BERT Rediscovers the Classical NLP Pipeline" (2019), Hewitt & Manning "A Structural Probe for Finding Syntax" (2019), any similar work on LLaMA/Llama-2/Llama-3

**Topic 2: Representation stability across layers**
- Papers discussing how fine-tuning changes layer-wise representations
- "Representation geometry" papers (e.g., CKA similarity, centered kernel alignment across layers)
- Papers that measure how uniformly information is distributed across layers before vs after training/fine-tuning

**Topic 3: Layer collapse / neural collapse in deep networks**
- "Neural Collapse" (Papyan et al. 2020) and follow-up work
- Layer collapse in transformers specifically
- Any papers showing that untrained/randomly initialized models have "collapsed" representations in certain layers
- Feature rank deficiency across layers

**Topic 4: VLA fine-tuning effects on LLM backbone**
- How does action fine-tuning (robot learning) change the internal representations of a pre-trained LLM?
- Papers: Buurmeijer et al. 2026, Grant et al. 2026, any probing studies on OpenVLA, RT-2, or Octo
- "What does VLA training actually learn?" type analyses

For each paper found, provide: Title, Authors, Year, Venue, and a 1-2 sentence summary of the key finding relevant to our topic.

Report in a structured format grouped by topic.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "0c9b3e77-2115-4a4c-afdb-12dbb9bf8d44"
}
```

</details>

---

### System

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Literature search: layer-wise probing LLM",
  "usage": {
    "total_tokens": 14532,
    "tool_uses": 1,
    "duration_ms": 2899
  },
  "last_tool_name": "ToolSearch",
  "uuid": "1c390ca6-62e2-43b1-9744-d341d1b55a34",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for Tenney et al \"BERT Rediscovers the Classical NLP …",
  "usage": {
    "total_tokens": 15995,
    "tool_uses": 2,
    "duration_ms": 6008
  },
  "last_tool_name": "WebSearch",
  "uuid": "6cb85d89-918f-4bb2-8713-0f786fbc4013",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### System

_source line 27_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for Hewitt Manning \"Structural Probe for Finding Synt…",
  "usage": {
    "total_tokens": 16000,
    "tool_uses": 3,
    "duration_ms": 6907
  },
  "last_tool_name": "WebSearch",
  "uuid": "319f282c-328e-4e3b-9d85-a568ec09ebd6",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### System

_source line 28_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for layer-wise probing LLaMA Llama-2 Llama-3 large la…",
  "usage": {
    "total_tokens": 16005,
    "tool_uses": 4,
    "duration_ms": 7386
  },
  "last_tool_name": "WebSearch",
  "uuid": "c43e2015-062a-45d0-8049-16f5fa6a99dc",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### System

_source line 29_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for CKA centered kernel alignment layer representatio…",
  "usage": {
    "total_tokens": 16010,
    "tool_uses": 5,
    "duration_ms": 7863
  },
  "last_tool_name": "WebSearch",
  "uuid": "5a87014e-945b-49ef-a3d1-7da11f63710c",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012Uodo6a95adgwPTNBrjnYn`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "8d14bae8-6e86-45e4-975c-715d69d10062",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014RfZ4KDyRSFYdnCGnmKEJY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14517,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14517,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 31 · 2026-05-15T16:01:21.357Z_

<details><summary>↩ Tool result · `toolu_012Uodo6a95adgwPTNBrjnYn`</summary>

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
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "7d05f9a6-4c49-42c8-a2e3-73f66d9bdad2"
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015cKo2HkGReAu9tqeeow9gN`</summary>

```json
{
  "query": "Tenney et al \"BERT Rediscovers the Classical NLP Pipeline\" layer-wise probing 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "7d7718b0-e90a-44b6-a208-2b48139c0a41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpMsbdHxca2AVVHbFECgHq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1453,
      "cache_read_input_tokens": 14517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1453,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 33_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PGDWUeH7WpqnzWt4JcTg9B`</summary>

```json
{
  "query": "Hewitt Manning \"Structural Probe for Finding Syntax\" 2019 NAACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "a0f52fb8-be70-419c-8bb4-61d8d59995a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpMsbdHxca2AVVHbFECgHq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1453,
      "cache_read_input_tokens": 14517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1453,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 34_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012BsJuUfJ3m8fjeYxvokd8d`</summary>

```json
{
  "query": "layer-wise probing LLaMA Llama-2 Llama-3 large language models per-layer accuracy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "c7d3ac91-73db-41c5-aa33-99fcbfd32a6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpMsbdHxca2AVVHbFECgHq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1453,
      "cache_read_input_tokens": 14517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1453,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 35_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016YmYqcHrhYSQUH9i8j5QCv`</summary>

```json
{
  "query": "CKA centered kernel alignment layer representations fine-tuning transformers similarity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "899530d4-b523-40cb-85fa-c93eae645bd0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpMsbdHxca2AVVHbFECgHq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1453,
      "cache_read_input_tokens": 14517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1453,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

### System

_source line 36_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for Papyan \"Neural Collapse\" 2020 deep networks layer…",
  "usage": {
    "total_tokens": 16015,
    "tool_uses": 6,
    "duration_ms": 8313
  },
  "last_tool_name": "WebSearch",
  "uuid": "65c97240-4d1e-42a4-b06e-7eb8268e3ebb",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DT8L5Fs3xMv1Tw6AvPLv3Z`</summary>

```json
{
  "query": "Papyan \"Neural Collapse\" 2020 deep networks layer collapse transformers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "496d72eb-ae30-4962-a9e4-9c4607ff489f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpMsbdHxca2AVVHbFECgHq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1453,
      "cache_read_input_tokens": 14517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1453,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

<details open><summary>🔧 Tool call — Agent · `toolu_01JTaZBVPMBnG51dC9dP2eeF`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Literature search: neural collapse & representation geometry",
  "prompt": "Search the web for academic papers on these specific topics. I need concrete paper titles, authors, years, and key findings.\n\n**Topic A: Neural Collapse and Layer-wise Behavior**\n- Papyan, Han, Donoho \"Prevalence of Neural Collapse during the terminal phase of deep learning training\" (2020)\n- Follow-up work on neural collapse in transformers, LLMs\n- \"Progressive neural collapse\" or \"layer-wise neural collapse\" \n- How training affects representation geometry layer by layer\n\n**Topic B: Fine-tuning effects on pretrained model representations**\n- How does fine-tuning (LoRA, full fine-tuning) change internal representations?\n- CKA (Centered Kernel Alignment) studies showing which layers change most during fine-tuning\n- \"Representation engineering\" papers (Zou et al. 2023)\n- Papers showing fine-tuning creates more uniform/stable representations\n\n**Topic C: Probe-based analysis showing training stabilizes representations**\n- Papers where probing accuracy becomes more uniform across layers after training\n- \"Anisotropy\" in transformer representations and how training affects it\n- Papers on \"representation degeneration\" in pre-trained models\n\n**Topic D: Robotics / embodied AI representation analysis**\n- Any probing studies on robot learning models (RT-1, RT-2, Octo, OpenVLA)\n- How do vision-language-action models use their LLM backbone?\n- Is there evidence that VLA training creates \"action pathways\" in LLM layers?\n\nFor each paper, provide: Title, Authors, Year, Venue, Key finding (1-2 sentences).\n\nReport grouped by topic, max 400 words per topic."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "28116b2f-2363-4244-b05d-8be6814ef8e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X44HpbQVj3mhrvTZPhbpA5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 436,
      "cache_read_input_tokens": 29364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 436
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

### System

_source line 39_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Literature search: neural collapse & representation geometry",
  "task_type": "local_agent",
  "prompt": "Search the web for academic papers on these specific topics. I need concrete paper titles, authors, years, and key findings.\n\n**Topic A: Neural Collapse and Layer-wise Behavior**\n- Papyan, Han, Donoho \"Prevalence of Neural Collapse during the terminal phase of deep learning training\" (2020)\n- Follow-up work on neural collapse in transformers, LLMs\n- \"Progressive neural collapse\" or \"layer-wise neural collapse\" \n- How training affects representation geometry layer by layer\n\n**Topic B: Fine-tuning effects on pretrained model representations**\n- How does fine-tuning (LoRA, full fine-tuning) change internal representations?\n- CKA (Centered Kernel Alignment) studies showing which layers change most during fine-tuning\n- \"Representation engineering\" papers (Zou et al. 2023)\n- Papers showing fine-tuning creates more uniform/stable representations\n\n**Topic C: Probe-based analysis showing training stabilizes representations**\n- Papers where probing accuracy becomes more uniform across layers after training\n- \"Anisotropy\" in transformer representations and how training affects it\n- Papers on \"representation degeneration\" in pre-trained models\n\n**Topic D: Robotics / embodied AI representation analysis**\n- Any probing studies on robot learning models (RT-1, RT-2, Octo, OpenVLA)\n- How do vision-language-action models use their LLM backbone?\n- Is there evidence that VLA training creates \"action pathways\" in LLM layers?\n\nFor each paper, provide: Title, Authors, Year, Venue, Key finding (1-2 sentences).\n\nReport grouped by topic, max 400 words per topic.",
  "uuid": "7ee84f48-9ec7-4a0b-b0d2-da9db3d31644",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

## Round 2

170 recorded events

### User

_source line 40 · 2026-05-15T16:01:26.860Z_

Search the web for academic papers on these specific topics. I need concrete paper titles, authors, years, and key findings.

**Topic A: Neural Collapse and Layer-wise Behavior**
- Papyan, Han, Donoho "Prevalence of Neural Collapse during the terminal phase of deep learning training" (2020)
- Follow-up work on neural collapse in transformers, LLMs
- "Progressive neural collapse" or "layer-wise neural collapse" 
- How training affects representation geometry layer by layer

**Topic B: Fine-tuning effects on pretrained model representations**
- How does fine-tuning (LoRA, full fine-tuning) change internal representations?
- CKA (Centered Kernel Alignment) studies showing which layers change most during fine-tuning
- "Representation engineering" papers (Zou et al. 2023)
- Papers showing fine-tuning creates more uniform/stable representations

**Topic C: Probe-based analysis showing training stabilizes representations**
- Papers where probing accuracy becomes more uniform across layers after training
- "Anisotropy" in transformer representations and how training affects it
- Papers on "representation degeneration" in pre-trained models

**Topic D: Robotics / embodied AI representation analysis**
- Any probing studies on robot learning models (RT-1, RT-2, Octo, OpenVLA)
- How do vision-language-action models use their LLM backbone?
- Is there evidence that VLA training creates "action pathways" in LLM layers?

For each paper, provide: Title, Authors, Year, Venue, Key finding (1-2 sentences).

Report grouped by topic, max 400 words per topic.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "e2ef6d70-4bf1-4c8c-b108-4cb9d106ebfe"
}
```

</details>

---

### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for VLA fine-tuning LLM backbone action representatio…",
  "usage": {
    "total_tokens": 16020,
    "tool_uses": 7,
    "duration_ms": 9015
  },
  "last_tool_name": "WebSearch",
  "uuid": "87425250-3161-44d7-bab0-023237a8d02f",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KqMsyMwtdpUmqen1qHyFS3`</summary>

```json
{
  "query": "VLA fine-tuning LLM backbone action representations OpenVLA RT-2 probing analysis 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "59d411a7-7519-48f8-a0f5-4f2c0ce8169f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpMsbdHxca2AVVHbFECgHq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1453,
      "cache_read_input_tokens": 14517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1453,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 43 · 2026-05-15T16:01:31.018Z_

<details><summary>↩ Tool result · `toolu_015cKo2HkGReAu9tqeeow9gN`</summary>

```text
Web search results for query: "Tenney et al "BERT Rediscovers the Classical NLP Pipeline" layer-wise probing 2019"

Links: [{"title":"BERT Rediscovers the Classical NLP Pipeline - ACL Anthology","url":"https://aclanthology.org/P19-1452/"},{"title":"BERT Rediscovers the Classical NLP Pipeline","url":"https://research.google/pubs/bert-rediscovers-the-classical-nlp-pipeline/"},{"title":"[PDF] BERT Rediscovers the Classical NLP Pipeline | Semantic Scholar","url":"https://www.semanticscholar.org/paper/BERT-Rediscovers-the-Classical-NLP-Pipeline-Tenney-Das/97906df07855b029b7aae7c2a1c6c5e8df1d531c"},{"title":"[1905.05950] BERT Rediscovers the Classical NLP Pipeline","url":"https://arxiv.org/abs/1905.05950"},{"title":"BERT Rediscovers the Classical NLP Pipeline | Request PDF","url":"https://www.researchgate.net/publication/335778883_BERT_Rediscovers_the_Classical_NLP_Pipeline"},{"title":"BERT Rediscovers the Classical NLP Pipeline","url":"https://aclanthology.org/P19-1452.pdf"},{"title":"Tenney et al 2019 - BERT Rediscovers the Classical NLP Pipeline","url":"https://czlwang.com/zettel/20201031020627-tenney_et_al_2019_bert_rediscovers_the_classical_nlp_pipeline.html"},{"title":"BERT Rediscovers the Classical NLP Pipeline","url":"https://bibbase.org/network/publication/tenney-das-pavlick-bertrediscoverstheclassicalnlppipeline-2019"},{"title":"BERT Rediscovers the Classical NLP Pipeline Ian Tenney1 Dipanjan Das1","url":"https://arxiv.org/pdf/1905.05950"},{"title":"Echoes of BERT: Do Modern Language Models Rediscover the Classical NLP Pipeline?","url":"https://arxiv.org/html/2506.02132v4"}]

I've found the paper "BERT Rediscovers the Classical NLP Pipeline" by Tenney et al. from 2019. Here are the key details:

## Publication Information

The paper was authored by Ian Tenney, Dipanjan Das, and Ellie Pavlick, and was published in the Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics in July 2019. The paper appears in pages 4593–4601. The arxiv version (1905.05950) was submitted on May 15, 2019.

## Main Findings

The research aimed to quantify where linguistic information is captured within the BERT network, and found that the model represents the steps of the traditional NLP pipeline in an interpretable and localizable way, with regions responsible for each step appearing in the expected sequence. Specifically, the tasks appear in order: POS tagging, parsing, NER, semantic roles, then coreference.

## Methodology

The research extended the edge probing suite to explore the computation performed at each layer of the BERT model. Qualitative analysis revealed that the model can and often does adjust this pipeline dynamically, revising lower-level decisions on the basis of disambiguating information from higher-level representations.

The paper has been highly influential in the field of interpretability research for transformer models and is widely cited in subsequent work on understanding how neural language models encode linguistic structure.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "223d55a6-c9ee-4b73-81b7-89743724cccc"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T16:01:32.072Z_

<details><summary>↩ Tool result · `toolu_01PGDWUeH7WpqnzWt4JcTg9B`</summary>

```text
Web search results for query: "Hewitt Manning "Structural Probe for Finding Syntax" 2019 NAACL"

Links: [{"title":"A Structural Probe for Finding Syntax in Word Representations - ACL Anthology","url":"https://aclanthology.org/N19-1419/"},{"title":"GitHub - john-hewitt/structural-probes: Codebase for testing whether hidden states of neural networks encode discrete structures. · GitHub","url":"https://github.com/john-hewitt/structural-probes"},{"title":"Finding Syntax with Structural Probes · John Hewitt","url":"https://www.cs.columbia.edu/~johnhew//structural-probe.html"},{"title":"A Structural Probe for Finding Syntax in Word Representations","url":"https://nlp.stanford.edu/pubs/hewitt2019structural.pdf"},{"title":"[PDF] A Structural Probe for Finding Syntax in Word Representations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Structural-Probe-for-Finding-Syntax-in-Word-Hewitt-Manning/455a8838cde44f288d456d01c76ede95b56dc675"},{"title":"Papers with Code - A Structural Probe for Finding Syntax in Word Representations","url":"https://paperswithcode.com/paper/a-structural-probe-for-finding-syntax-in-word"},{"title":"A Structural Probe for Finding Syntax in Word ...","url":"https://www.cs.columbia.edu/~johnhew/public/hewitt2019structural_slides.pdf"},{"title":"A Structural Probe for Finding Syntax in Word Representations","url":"https://bibbase.org/network/publication/hewitt-manning-astructuralprobeforfindingsyntaxinwordrepresentations-2019"},{"title":"A Structural Probe for Finding Syntax in Word Representations. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/1541a556da1afe8c0d1d0ef9f3932469?postOwner=postylem&intraHash=99142ed4218f792e40d5ddc1d69b77b4"},{"title":"A Structural Probe for Finding Syntax in Word Representations","url":"https://www.zotero.org/groups/4865794/clc-brain/items/itemKey/SP274JWE"}]

I found the paper you're looking for! Here are the key details:

"A Structural Probe for Finding Syntax in Word Representations" by John Hewitt and Christopher D. Manning was published in 2019 in the Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (pages 4129–4138, Minneapolis, Minnesota).

**Main contribution:** The paper proposes a structural probe, which evaluates whether syntax trees are embedded in a linear transformation of a neural network's word representation space. The probe identifies a linear transformation under which squared L2 distance encodes the distance between words in the parse tree, and one in which squared L2 norm encodes depth in the parse tree.

**Key findings:** Using their probe, the authors show that such transformations exist for both ELMo and BERT but not in baselines, providing evidence that entire syntax trees are embedded implicitly in deep models' vector geometry.

The paper has associated code available on GitHub at https://github.com/john-hewitt/structural-probes, and the full paper is available through the ACL Anthology at https://aclanthology.org/N19-1419/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "76848593-e64f-4f9f-9292-9b20a88755c3"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-15T16:01:33.994Z_

<details><summary>↩ Tool result · `toolu_012BsJuUfJ3m8fjeYxvokd8d`</summary>

```text
Web search results for query: "layer-wise probing LLaMA Llama-2 Llama-3 large language models per-layer accuracy"

Links: [{"title":"Is Bigger and Deeper Always Better? Probing LLaMA Across Scales and Layers","url":"https://arxiv.org/html/2312.04333v4"},{"title":"LLaMA 3.2-Vision-Instruct: A Layer-Wise Guide to Attention, Embeddings, and Multimodal Reasoning | by Partha Sai Guttikonda | Medium","url":"https://guttikondaparthasai.medium.com/llama-3-2-vision-instruct-a-layer-wise-guide-to-attention-embeddings-and-multimodal-reasoning-eed64fb17bb5"},{"title":"Beyond Surface: Probing LLaMA Across Scales and Layers","url":"https://arxiv.org/html/2312.04333v3"},{"title":"Exploring Concept Depth: How Large Language Models ...","url":"https://aclanthology.org/2025.coling-main.37.pdf"},{"title":"Is Bigger and Deeper Always Better? Probing LLaMA Across Scales and Layers","url":"https://openreview.net/pdf/e0d65067d283d0b8f856fa093e1bdd2142f98838.pdf"},{"title":"Exploring Concept Depth: How Large Language Models Acquire","url":"https://arxiv.org/pdf/2404.07066"},{"title":"Layer-wise Probing Study","url":"https://www.emergentmind.com/topics/layer-wise-probing-study"},{"title":"Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling","url":"https://arxiv.org/html/2604.13386v1"},{"title":"GitHub - nuochenpku/LLaMA_Analysis: This is official project in our paper: Is Bigger and Deeper Always Better? Probing LLaMA Across Scales and Layers","url":"https://github.com/nuochenpku/LLaMA_Analysis"},{"title":"Exploring Concept Depth: How Large Language Models Acquire Knowledge at Different Layers?","url":"https://luckfort.github.io/explore_CD/"}]

I've completed a web search on layer-wise probing for LLaMA, Llama-2, and Llama-3 models. Here are the key findings:

## Key Research Studies

A notable study probed LLaMA across five higher-order tasks including calculation, math problem solving, logical reasoning, truthfulness, and factual knowledge detection, comparing models both horizontally across different sizes and vertically by comparing different layers of the same size model.

## Layer-wise Performance Results

Detailed layer-wise results of LLaMA 2-7B, 13B and 70B models were provided across five probing tasks: MPS-Cal, LAMA, Reclor, TFQA and MPS-Rea.

## Key Findings on Layer Behavior

In vertical analysis, lower layers of LLaMA lack substantial arithmetic and factual knowledge but showcase logical thinking and multilingual abilities, with top layers housing most computational abilities.

## Broader Layer-wise Probing Research

Research has explored the hypothesis that LLMs process concepts of varying complexities in different layers, introducing "Concept Depth" to suggest more complex concepts are acquired in deeper layers, with extensive probing experiments using layer-wise representations across LLM families including LLaMA.

Studies measured layer-wise accuracy by selecting six layers (first, 25% depth, 50% depth, 67% depth, 83% depth, last) to record accuracy, F1-score, and AUC.

Research on optimal detection layers found they cluster in the latter two-thirds of networks with a mean of 65% depth but vary substantially across architectures and tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "c44b7d8f-2c90-4ca6-b0c9-5fbb501b1ec2"
}
```

</details>

---

### System

_source line 46_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Literature search: neural collapse & representation geometry",
  "usage": {
    "total_tokens": 14465,
    "tool_uses": 1,
    "duration_ms": 7283
  },
  "last_tool_name": "ToolSearch",
  "uuid": "54452268-049d-4fad-9968-2413d2e2f9fc",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Xrhm4XAvUf4AUyqPfk3836`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "7248355d-9476-4745-b758-9204ad863348",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E1eDsWoMBny2d8LqJvaJzM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6201,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6201,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 48 · 2026-05-15T16:01:34.148Z_

<details><summary>↩ Tool result · `toolu_01Xrhm4XAvUf4AUyqPfk3836`</summary>

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
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "0748eaac-c13d-418e-ac7c-6082f3db7063"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T16:01:35.360Z_

<details><summary>↩ Tool result · `toolu_016YmYqcHrhYSQUH9i8j5QCv`</summary>

```text
Web search results for query: "CKA centered kernel alignment layer representations fine-tuning transformers similarity"

Links: [{"title":"Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers - ACL Anthology","url":"https://aclanthology.org/2021.blackboxnlp-1.42/"},{"title":"Centered Kernel Alignment","url":"https://jyopari.github.io/posts/CKA"},{"title":"Centered Kernel Alignment (CKA) Overview","url":"https://www.emergentmind.com/topics/centered-kernel-alignment-cka"},{"title":"Fine-Tuned Transformers Show Clusters of Similar ...","url":"https://aclanthology.org/2021.blackboxnlp-1.42.pdf"},{"title":"[2109.08406] Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers","url":"https://arxiv.org/abs/2109.08406"},{"title":"Fine-Tuned Transformers Show Clusters of Similar ... - NSF PAR","url":"https://par.nsf.gov/servlets/purl/10358004"},{"title":"Centered Kernel Alignment (CKA) Similarity","url":"https://www.emergentmind.com/topics/centered-kernel-alignment-cka-similarity"},{"title":"GitHub - RistoAle97/centered-kernel-alignment: CKA (Centered Kernel Alignment) implemented in PyTorch · GitHub","url":"https://github.com/RistoAle97/centered-kernel-alignment"},{"title":"Beyond Cosine: Why Centered Kernel Alignment (CKA) is Your Go-To for Validating Multilingual Models | by Vigneswaran Sugumaaran | Medium","url":"https://medium.com/@vigneswaran.sugumaaran/beyond-cosine-why-centered-kernel-alignment-cka-is-your-go-to-for-validating-multilingual-models-2bc3c1978302"},{"title":"TRepLiNa: Layer-wise CKA+REPINA Alignment Improves Low-Resource","url":"https://www.arxiv.org/pdf/2510.06249v2"}]

Based on the web search results, here's what I found about CKA (Centered Kernel Alignment) and its applications to layer representations, fine-tuning transformers, and similarity measurement:

## What is CKA?

Centered Kernel Alignment (CKA) is a kernel-based similarity metric designed to quantify the degree of alignment between two sets of representations, typically arising as activations from different neural network layers, distinct architectures, or alternative population encodings. CKA is a similarity metric that quantifies the alignment between neural representations using centered Gram matrices and the Hilbert–Schmidt Independence Criterion, achieving invariance to isotropic scaling and orthogonal transformations.

## CKA Applied to Fine-Tuning Transformers

A key study in this area is the research by Phang et al. (2021). Researchers used centered kernel alignment (CKA), a method for comparing learned representations, to measure the similarity of representations in task-tuned models across layers. In experiments across twelve NLU tasks, they discovered a consistent block diagonal structure in the similarity of representations within fine-tuned RoBERTa and ALBERT models, with strong similarity within clusters of earlier and later layers, but not between them. The similarity of later layer representations implies that later layers only marginally contribute to task performance, and they verified in experiments that the top few layers of fine-tuned Transformers can be discarded without hurting performance, even with no further tuning.

## Applications and Use Cases

CKA maps reveal layerwise redundancy, hierarchical structure, and blockwise processing, with high off-diagonal CKA values indicating blocks of similar representations, often due to overparameterization or inadequate training. CKA identifies superfluous or static layers, informing pruning and model compression strategies, with MPruner leveraging CKA-based layer clustering to collapse nearly identical block sequences in both transformers and CNNs, often achieving ~50% parameter reduction with negligible accuracy degradation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "d554d4d8-ddfe-499e-be49-86e0599bdfb2"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T16:01:35.851Z_

<details><summary>↩ Tool result · `toolu_01DT8L5Fs3xMv1Tw6AvPLv3Z`</summary>

```text
Web search results for query: "Papyan "Neural Collapse" 2020 deep networks layer collapse transformers"

Links: [{"title":"Neural Collapse is Globally Optimal in Deep Regularized ResNets and Transformers","url":"https://arxiv.org/html/2505.15239v1"},{"title":"Neural Collapse is Globally Optimal in Deep Regularized ...","url":"https://arxiv.org/pdf/2505.15239"},{"title":"Feature Learning in Deep Classifiers through Intermediate Neural Collapse","url":"https://proceedings.mlr.press/v202/rangamani23a/rangamani23a.pdf"},{"title":"Prevalence of neural collapse during the terminal phase of deep learning training | PNAS","url":"https://www.pnas.org/doi/10.1073/pnas.2015509117"},{"title":"Neural Collapse: A Review on Modelling Principles and ...","url":"https://openreview.net/pdf?id=QTXocpAP9p"},{"title":"Data for \"Prevalence of Neural Collapse during the terminal phase of deep learning training\" (PNAS 2020) and \"Neural Collapse under MSE loss: proximity to and dynamics on the central path\" (ICLR 2022) | Stanford Digital Repository","url":"https://purl.stanford.edu/ng812mz4543"},{"title":"Neural Collapse in Deep Networks","url":"https://www.emergentmind.com/topics/neural-collapse-phenomenon"},{"title":"Exploring deep neural networks via layer-peeled model: Minority collapse in imbalanced training | PNAS","url":"https://www.pnas.org/doi/10.1073/pnas.2103091118"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Prevalence+of+Neural+Collapse+during+the+Terminal+Phase+of+Deep+Learning+Training&author=Papyan,+V.&author=Han,+X.Y.&author=Donoho,+D.L.&publication_year=2020&journal=Proc.+Natl.+Acad.+Sci.+USA&volume=117&pages=24652%E2%80%9324663&doi=10.1073/pnas.2015509117&pmid=32958680"},{"title":"[PDF] Prevalence of neural collapse during the terminal phase of deep learning training | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Prevalence-of-neural-collapse-during-the-terminal-Papyan-Han/806e27fb9d8781c3c6e918734453418ebbeae96c"}]

Based on the search results, here's information about Papyan's Neural Collapse research:

## Overview

In 2020, Papyan et al. discovered a surprising geometric structure in learned representations of deep neural networks (DNNs) at convergence.

## Key Findings

Direct measurements of TPT (Terminal Phase of Training), for three prototypical deepnet architectures and across seven canonical classification datasets, expose a pervasive inductive bias called neural collapse (NC), involving four deeply interconnected phenomena. These phenomena are:

1. (NC1) Cross-example within-class variability of last-layer training activations collapses to zero, as the individual activations themselves collapse to their class means.

2. (NC2) The class means collapse to the vertices of a simplex equiangular tight frame (ETF).

3. (NC3) Up to rescaling, the last-layer classifiers collapse to the class means or in other words, to the simplex ETF (i.e., to a self-dual structure).

## Recent Extensions to Transformers

More recent work has extended neural collapse analysis to transformers. Research proves that global optima of deep regularized transformers and residual networks (ResNets) with LayerNorm trained with cross entropy or mean squared error loss are approximately collapsed, and the approximation gets tighter as the depth grows.

Theoretical results are supported by experiments on computer vision and language datasets showing that, as the depth grows, neural collapse indeed becomes more prominent.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "618da99f-7116-4e27-8694-bbac0f69bf1e"
}
```

</details>

---

### System

_source line 51_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for Papyan Han Donoho \"Prevalence of Neural Collapse\"…",
  "usage": {
    "total_tokens": 15922,
    "tool_uses": 2,
    "duration_ms": 10493
  },
  "last_tool_name": "WebSearch",
  "uuid": "0fde360c-852e-4122-92a9-93b30779efd3",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ATjoNrAy2GFC4ftYeBK6jr`</summary>

```json
{
  "query": "Papyan Han Donoho \"Prevalence of Neural Collapse\" 2020 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "03709ca4-c020-4b3b-a295-4909b3192bf1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018WXJTVEAbwZVTGsVpNe6Ps",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1453,
      "cache_read_input_tokens": 14450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1453,
        "ephemeral_1h_input_tokens": 0
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

_source line 53 · 2026-05-15T16:01:38.816Z_

<details><summary>↩ Tool result · `toolu_01KqMsyMwtdpUmqen1qHyFS3`</summary>

```text
Web search results for query: "VLA fine-tuning LLM backbone action representations OpenVLA RT-2 probing analysis 2025 2026"

Links: [{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"Understanding OpenVLA: A Simple Guide - Hankyu Kim","url":"https://hankyukim.com/openvla/"},{"title":"A Comprehensive Overview of Vision-Language-Action Models | DigitalOcean","url":"https://www.digitalocean.com/community/conceptual-articles/vision-language-action-models"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"Fine-Tuning Vision-Language-Action Models | DigitalOcean","url":"https://www.digitalocean.com/community/tutorials/vision-language-action-finetuning-robotics"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"}]

Now let me search for more specific information about probing analysis and mechanistic interpretability studies from 2025-2026:

Links: [{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"Mechanistic Interpretability for Steering Vision Language Action Models","url":"https://vla-mech-interp.github.io/"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/html/2603.19233"},{"title":"[2509.00328] Mechanistic interpretability for steering vision-language-action models","url":"https://arxiv.org/abs/2509.00328"},{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models","url":"https://proceedings.mlr.press/v305/haon25a.html"},{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models","url":"https://arxiv.org/html/2509.00328v1"},{"title":"Paper page - Mechanistic interpretability for steering vision-language-action models","url":"https://huggingface.co/papers/2509.00328"},{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=YvsUD8C9QS"},{"title":"Mechanistic interpretability for steering vision-language-action models","url":"https://www.emergentmind.com/papers/2509.00328"},{"title":"Mechanistic interpretability for steering vision-language-action models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250900328H/abstract"}]

Based on my web search results, I found substantial information on VLA fine-tuning, LLM backbone action representations, and recent probing analysis of OpenVLA and RT-2 models. Here's a comprehensive summary:

## VLA Fine-Tuning and LLM Backbone Architecture

OpenVLA is fine-tuned from a pretrained Prismatic-7B VLM, consisting of a fused visual encoder with SigLIP and DinoV2 backbones, a projector mapping visual embeddings to an LLM input space, and a Llama 2 7B language model backbone that predicts tokenized output actions. Unlike modular methods such as Octo, which combine separately trained encoders and decoders, OpenVLA fine-tunes the entire vision–language backbone jointly for action prediction.

## Action Representation Strategy

Robot actions are represented as tokens by discretizing each continuous action dimension into 256 bins, with these discretized values mapped to reserved tokens in the Llama tokenizer. RT-2 coined the term VLAs and represents actions as text tokens for co-fine-tuning.

## Recent Probing Analysis (2025-2026)

Recent mechanistic interpretability research has uncovered how these models represent actions internally:

Experimental probing of OpenVLA's LLM backbone reveals robust internal encoding of symbolic states (object relations, action status) with >>0.90 accuracy in decoding symbolic predicates. Mechanistic interpretability analyses show that specific transformer neurons correspond to semantic directions (e.g., "fast", "up"), and activation steering can causally modulate robot behavior at inference time.

A framework introduces the first method for interpreting and steering VLA models via their internal representations, projecting feedforward activations within transformer layers onto the token embedding basis to identify sparse semantic directions that are causally linked to action selection, with a general-purpose activation steering method that modulates behavior in real time without fine-tuning. This method has been evaluated on π0 and OpenVLA, demonstrating zero-shot behavioral control in simulation (LIBERO) and on a physical robot (UR5).

VLAs process heterogeneous token sequences interleaving vision, language, and proprioception, and mean-pooling activations across token positions destroys action-critical information, causing catastrophic task failure despite high reconstruction quality.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "14d747b2-3b2e-49cb-b957-00f39955a5c6"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T16:01:42.800Z_

<details><summary>↩ Tool result · `toolu_01ATjoNrAy2GFC4ftYeBK6jr`</summary>

```text
Web search results for query: "Papyan Han Donoho "Prevalence of Neural Collapse" 2020 paper"

Links: [{"title":"Data for \"Prevalence of Neural Collapse during the terminal phase of deep learning training\" (PNAS 2020) and \"Neural Collapse under MSE loss: proximity to and dynamics on the central path\" (ICLR 2022) | Stanford Digital Repository","url":"https://purl.stanford.edu/ng812mz4543"},{"title":"[2008.08186] Prevalence of Neural Collapse during the terminal phase of deep learning training","url":"https://arxiv.org/abs/2008.08186"},{"title":"Prevalence of neural collapse during the terminal phase of deep learning training - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020PNAS..11724652P/abstract"},{"title":"Prevalence of neural collapse during the terminal phase of deep learning training | PNAS","url":"https://www.pnas.org/doi/10.1073/pnas.2015509117"},{"title":"Data for \"Prevalence of Neural Collapse during the terminal phase of deep learning training\" (PNAS 2020) and \"Neural Collapse under MSE loss: proximity to and dynamics on the central path\" (ICLR 2022) - Research from Stanford University - Spotlight Exhibits","url":"https://exhibits.stanford.edu/data/catalog/ng812mz4543"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Prevalence+of+Neural+Collapse+during+the+Terminal+Phase+of+Deep+Learning+Training&author=Papyan,+V.&author=Han,+X.Y.&author=Donoho,+D.L.&publication_year=2020&journal=Proc.+Natl.+Acad.+Sci.+USA&volume=117&pages=24652%E2%80%9324663&doi=10.1073/pnas.2015509117&pmid=32958680"},{"title":"[PDF] Prevalence of neural collapse during the terminal phase of deep learning training | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Prevalence-of-neural-collapse-during-the-terminal-Papyan-Han/806e27fb9d8781c3c6e918734453418ebbeae96c"},{"title":"Prevalence of Neural Collapse During the Terminal Phase of Deep Learning Training | Department of Statistics","url":"https://statistics.stanford.edu/technical-reports/prevalence-neural-collapse-during-terminal-phase-deep-learning-training"},{"title":"(PDF) Prevalence of neural collapse during the terminal phase of deep learning training","url":"https://www.researchgate.net/publication/344354509_Prevalence_of_neural_collapse_during_the_terminal_phase_of_deep_learning_training"},{"title":"Prevalence of neural collapse during the terminal phase ...","url":"https://pubmed.ncbi.nlm.nih.gov/32958680/"}]

I found the paper you're looking for. Here are the key details:

## "Prevalence of Neural Collapse during the Terminal Phase of Deep Learning Training"

**Authors:** Vardan Papyan (Department of Statistics, Stanford University), X. Y. Han (School of Operations Research and Information Engineering, Cornell University), and David L. Donoho (Department of Statistics, Stanford University)

**Publication:** Published in PNAS in October 6, 2020, vol. 117, no. 40 (pages 24652-24663)

**DOI:** https://doi.org/10.1073/pnas.2015509117

**Main Contribution:**

The paper studies the terminal phase of training (TPT) in classification deepnets, which begins when training error first vanishes. During TPT, training error stays effectively zero while training loss is pushed toward zero. The authors expose a pervasive inductive bias called neural collapse (NC) involving four deeply interconnected phenomena.

**Availability:**
- **arXiv:** https://arxiv.org/abs/2008.08186
- **PNAS:** https://www.pnas.org/doi/10.1073/pnas.2015509117
- **Research Data:** The data used to generate plots in this paper is available at Stanford Digital Repository


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "3dd8480e-52d2-4062-88a8-60ad75ecb170"
}
```

</details>

---

### System

_source line 55_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for representation similarity analysis fine-tuning LL…",
  "usage": {
    "total_tokens": 22705,
    "tool_uses": 8,
    "duration_ms": 24517
  },
  "last_tool_name": "WebSearch",
  "uuid": "85a376e5-d553-4267-861a-1594671a06ab",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UAcSgBZ7jtchWwyVYpYceD`</summary>

```json
{
  "query": "representation similarity analysis fine-tuning LLM layers \"representation geometry\" before after training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "09383ac9-84a7-403d-8329-447dedf37d7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013oRDM8HYKtXtwTsYeHPkT2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6685,
      "cache_read_input_tokens": 15970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6685,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 57_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for neural collapse transformers feature rank deficie…",
  "usage": {
    "total_tokens": 22706,
    "tool_uses": 9,
    "duration_ms": 25326
  },
  "last_tool_name": "WebSearch",
  "uuid": "fe2c4987-1797-41de-922f-458983d42afa",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KKdy6gheHr2XtTfXVheKKQ`</summary>

```json
{
  "query": "neural collapse transformers feature rank deficiency layer collapse representation 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "c9112a2b-c028-4070-9275-28332b059be0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013oRDM8HYKtXtwTsYeHPkT2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6685,
      "cache_read_input_tokens": 15970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6685,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 59_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for Buurmeijer Grant 2026 VLA probing robot action fi…",
  "usage": {
    "total_tokens": 22707,
    "tool_uses": 10,
    "duration_ms": 26288
  },
  "last_tool_name": "WebSearch",
  "uuid": "0f364ad0-1d56-43b2-940d-49501caa57fb",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Sjsf6c5gnqL6NCsFKQZsLf`</summary>

```json
{
  "query": "Buurmeijer Grant 2026 VLA probing robot action fine-tuning LLM representations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "b8b2b9e7-ad69-45ed-bfaa-958b7b678f3d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013oRDM8HYKtXtwTsYeHPkT2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6685,
      "cache_read_input_tokens": 15970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6685,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 61_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for \"Not All Features Are Created Equal\" VLA mechanis…",
  "usage": {
    "total_tokens": 22708,
    "tool_uses": 11,
    "duration_ms": 27217
  },
  "last_tool_name": "WebSearch",
  "uuid": "48801443-fb28-4c6e-bf21-b035dbdb009b",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HaswKFMVCsaxasopQVS2Nm`</summary>

```json
{
  "query": "\"Not All Features Are Created Equal\" VLA mechanistic study 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "80a8485a-034c-4026-84ed-6d63b1249350",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013oRDM8HYKtXtwTsYeHPkT2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6685,
      "cache_read_input_tokens": 15970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6685,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 63_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for neural collapse in transformers LLMs progressive …",
  "usage": {
    "total_tokens": 17121,
    "tool_uses": 3,
    "duration_ms": 19176
  },
  "last_tool_name": "WebSearch",
  "uuid": "a2432dbc-78b2-43c9-8762-3b25e423c141",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K5jUgiNqRaL6aztKrenffq`</summary>

```json
{
  "query": "neural collapse in transformers LLMs progressive layer-wise 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "856b8c89-285d-482a-958a-440d24e35859",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139fjNoSXUNwkPJhHsPUHPs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1159,
      "cache_read_input_tokens": 15903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1159,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

### System

_source line 65_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for Kornblith \"Similarity of Neural Network Represent…",
  "usage": {
    "total_tokens": 22709,
    "tool_uses": 12,
    "duration_ms": 28207
  },
  "last_tool_name": "WebSearch",
  "uuid": "ced884dd-360b-42f1-b269-46f747177548",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013gKKjtXEoNcdCarzUb2hyj`</summary>

```json
{
  "query": "Kornblith \"Similarity of Neural Network Representations Revisited\" CKA 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "4869ec4f-e0f6-44ec-b64f-0f0c48ab1d4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013oRDM8HYKtXtwTsYeHPkT2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6685,
      "cache_read_input_tokens": 15970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6685,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 67_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for layer-wise probing vision language models multimo…",
  "usage": {
    "total_tokens": 22710,
    "tool_uses": 13,
    "duration_ms": 28685
  },
  "last_tool_name": "WebSearch",
  "uuid": "d7f3fd57-22a4-49c1-9cdf-e1829d40cb7d",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ELyrHTNqmS2XNQxUbrubw3`</summary>

```json
{
  "query": "layer-wise probing vision language models multimodal representations CLIP LLaVA per-layer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "dca80886-4642-4f39-9728-309afcbcb174",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013oRDM8HYKtXtwTsYeHPkT2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6685,
      "cache_read_input_tokens": 15970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6685,
        "ephemeral_1h_input_tokens": 0
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

_source line 69 · 2026-05-15T16:01:50.606Z_

<details><summary>↩ Tool result · `toolu_01Sjsf6c5gnqL6NCsFKQZsLf`</summary>

```text
Web search results for query: "Buurmeijer Grant 2026 VLA probing robot action fine-tuning LLM representations"

Links: [{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"},{"title":"Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2508.13073v1"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · Robotics: Science and Systems","url":"https://roboticsconference.org/program/papers/17/"},{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/html/2603.16044v1"},{"title":"Demonstration-Free Robotic Control via LLM Agents","url":"https://arxiv.org/html/2601.20334v1"},{"title":"RoboVLMs: What Matters in Building Vision-Language-Action Models for Generalist Robot Policies","url":"https://robovlms.github.io/"}]

I searched for information about "Buurmeijer Grant 2026 VLA probing robot action fine-tuning LLM representations," but the search results do not contain any specific information about a "Buurmeijer Grant" or research by someone with that name related to VLAs in 2026.

The search results do return comprehensive information about Vision-Language-Action (VLA) models for robotics, including topics like:

- Experimental probing of OpenVLA's LLM backbone reveals robust internal encoding of symbolic states (object relations, action status)
- Parameter-efficient fine-tuning strategies to enhance the linguistic generalization of OpenVLA
- Mechanistic interpretability analyses showing that specific transformer neurons correspond to semantic directions, and activation steering can causally modulate robot behavior at inference time

However, I was unable to find specific results about a "Buurmeijer Grant" or research with that exact title. Could you provide more context about what you're looking for, such as:
- An author's full name or institution
- A specific conference or publication venue
- More details about the research focus

This would help me conduct a more targeted search for the information you need.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "60714250-cec2-4340-b619-88ccfd343c82"
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-15T16:01:51.894Z_

<details><summary>↩ Tool result · `toolu_01KKdy6gheHr2XtTfXVheKKQ`</summary>

```text
Web search results for query: "neural collapse transformers feature rank deficiency layer collapse representation 2023 2024"

Links: [{"title":"Deep Dive into Rank Collapse in LLMs | by Freedom Preetham | Autonomous Agents | Medium","url":"https://medium.com/autonomous-agents/deep-dive-into-rank-collapse-in-llms-c91c142d8441"},{"title":"Neural Collapse is Globally Optimal in Deep Regularized ResNets and Transformers","url":"https://arxiv.org/html/2505.15239v1"},{"title":"Attention Masks, LayerNorm & Rank Collapse in Transformers","url":"https://www.emergentmind.com/papers/2405.18781"},{"title":"Theoretical Perspectives and the Role of Rank Collapse","url":"https://arxiv.org/pdf/2206.03126"},{"title":"[2505.15239] Neural Collapse is Globally Optimal in Deep Regularized ResNets and Transformers","url":"https://arxiv.org/abs/2505.15239"},{"title":"[2410.07799] Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers","url":"https://arxiv.org/abs/2410.07799"},{"title":"Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Transformers","url":"https://arxiv.org/html/2410.07799v1"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.10609"},{"title":"SEQ-VCR:PREVENTING COLLAPSE IN INTERMEDIATE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/b577c062bd4f894b7e05fab6440373ed-Paper-Conference.pdf"},{"title":"Signal Propagation in Transformers: Theoretical Perspectives and the Role of Rank Collapse | Request PDF","url":"https://www.researchgate.net/publication/401460741_Signal_Propagation_in_Transformers_Theoretical_Perspectives_and_the_Role_of_Rank_Collapse"}]

I've completed the web search for your query on neural collapse, transformers, feature rank deficiency, and layer collapse in representations from 2023-2024. Here are the key findings:

## Main Research Areas

**Rank Collapse in Transformers:**
Pure self-attention suffers from an increasing degree of rank collapse as depth increases, limiting model expressivity and further utilization of model depth.

**Neural Collapse Phenomenon:**
Neural collapse is a surprising symmetry in the feature representations of the training data in the penultimate layer of deep neural networks. Global optima of deep regularized transformers and residual networks (ResNets) with LayerNorm trained with cross entropy or mean squared error loss are approximately collapsed, and the approximation gets tighter as the depth grows.

**Multiple Forms of Rank Collapse:**
Even at initialization, rank collapse occurs in depth when all tokens converge to a single representation along layers, and there is an additional challenge unique to softmax attention layers called rank collapse in width, which occurs as the context length increases.

**Mitigation Strategies:**
Experiments on prominent transformer architectures like BERT, Albert, and XLNet confirmed the rank collapse phenomenon and demonstrated the effectiveness of architectural components, such as skip connections and MLPs, in mitigating it. Analysis shows that although pure masked attention still suffers from exponential collapse to a rank one subspace, sparse or local masked attention can provably slow down the collapse rate.

The search results contain several 2023-2024 papers analyzing these phenomena from different theoretical perspectives, including random matrix theory and statistical physics approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "764655f0-ea34-4aaf-9e08-aedd055f4b5b"
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-15T16:01:52.395Z_

<details><summary>↩ Tool result · `toolu_01UAcSgBZ7jtchWwyVYpYceD`</summary>

```text
Web search results for query: "representation similarity analysis fine-tuning LLM layers "representation geometry" before after training"

Links: [{"title":"Massive Supervised Fine-tuning Experiments Reveal How Data, Layer, and Training Factors Shape LLM Alignment Quality","url":"https://arxiv.org/html/2506.14681v1"},{"title":"Evolution of LLM Stages across Model Sizes","url":"https://sidn.baulab.info/evolution/"},{"title":"Layer-wise LoRA fine-tuning: a similarity metric approach","url":"https://arxiv.org/pdf/2602.05988"},{"title":"Representational Similarity Analysis (RSA)","url":"https://www.emergentmind.com/topics/representational-similarity-analysis-rsa"},{"title":"Layer-Aware Representation Filtering: Purifying Finetuning Data to Preserve LLM Safety Alignment","url":"https://arxiv.org/html/2507.18631v2"},{"title":"The Representation Landscape of Few-Shot Learning and Fine-Tuning in Large Language Models","url":"https://arxiv.org/html/2409.03662v2"},{"title":"Towards Measuring Representational Similarity of Large Language Models","url":"https://arxiv.org/html/2312.02730v1"},{"title":"Safety-Aware LLM Fine-Tuning","url":"https://www.emergentmind.com/topics/safety-aware-llm-fine-tuning"},{"title":"The reasoning-like capabilities of large language models across different languages: Insights from representational similarity analysis - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2949882126000010"},{"title":"llm-research-summaries/training/Analyzing-Fine-tuning-Representation-Shift-for-Multimodal-LLMs-Steering_2501.03012v1.md at main · cognitivetech/llm-research-summaries","url":"https://github.com/cognitivetech/llm-research-summaries/blob/main/training/Analyzing-Fine-tuning-Representation-Shift-for-Multimodal-LLMs-Steering_2501.03012v1.md"}]

Based on the search results, I found several highly relevant papers and resources on representation similarity analysis, LLM fine-tuning, and representation geometry changes. Here are the key findings:

## Representational Similarity Analysis (RSA) Methodology

Representational Similarity Analysis (RSA) is a multivariate technique that compares diverse data types by examining shared patterns in their similarity matrices. RSA operates by transforming multivariate response patterns into a pairwise (dis)similarity matrix. The RDM is invariant to orthogonal transformations and provides an abstract "geometry" of representational space.

## Representation Geometry Changes During Fine-Tuning

Several studies examine how fine-tuning alters LLM representation geometry across layers:

**Intrinsic Dimensionality Changes:** One approach quantifies how supervised fine-tuning (SFT) alters the geometry of the training corpus in embedding space by computing the intrinsic dimensionality (ID) of sentence-level embeddings produced before and after SFT. Intrinsic dimensionality analysis of embeddings revealed that the embedding space begins to diverge substantially from the base model at mid-layer positions, suggesting these layers actively expand the model's representational subspace during SFT.

**Layer-Specific Changes:** Fine-tuning primarily modifies the representations to encode the answers after the transition in the middle of the network. When comparing fine-tuned models on safety tasks, fine-tuned representations on degrading data show marked shifts, demonstrating that fine-tuning on certain data induces greater drift in safety feature space.

**RSA for Layer-Wise Analysis:** An RSA methodology for layer-wise analysis starts with sets of sentences from different domains, feeds them into LLMs of various sizes, then extracts neural activations (hidden states) for each input at each layer to provide a layer-by-layer snapshot of how the model's internal representations evolve.

These findings highlight how RSA can reveal complementary changes in representation geometry before and after fine-tuning, with mid-layer representations showing the most substantial divergence from the pretrained baseline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "a06fb6a6-dbfe-4ea2-b027-0b221ac84550"
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-15T16:01:52.449Z_

<details><summary>↩ Tool result · `toolu_01HaswKFMVCsaxasopQVS2Nm`</summary>

```text
Web search results for query: ""Not All Features Are Created Equal" VLA mechanistic study 2026 arxiv"

Links: [{"title":"[2603.19233] Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.19233"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/html/2603.19233v1"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=w8Mw9zJt1y"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2603.19233"},{"title":"GitHub - CWRU-AISM/action-atlas: Mechanistic Interpretability toolkit for Vision-Language-Action models · GitHub","url":"https://github.com/CWRU-AISM/action-atlas"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://www.wispaper.ai/en/blog/not-all-features-created-equal-mechanistic-study-vision-language-action-models-20260320/zho"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.19233v1"},{"title":"Robotics Research arXiv on X: \"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models Bryce Grant, Xijia Zhao, Peng Wang https://t.co/Mr1IyrLxt9 [𝚌𝚜.𝚁𝙾] https://t.co/9LLIgjodQp\" / X","url":"https://x.com/OWW/status/2034850674173788594"},{"title":"你的 AI 机器人可能根本没听你的话_腾讯新闻","url":"https://news.qq.com/rain/a/20260322A02KDA00"}]

I found the paper! Here's a summary of what I found:

## "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models"

**Paper Details:**
- Published March 19, 2026 on arXiv (2603.19233)
- Authors: Bryce Grant and 2 other co-authors (Xijia Zhao and Peng Wang)

**Research Overview:**
The paper investigates how Vision-Language-Action (VLA) models combine perception, language, and motor control, applying activation injection, sparse autoencoders (SAEs), and linear probes to six models spanning 80M–7B parameters across 394,000+ rollout episodes on four benchmarks.

**Key Findings:**
1. The visual pathway dominates action generation across all architectures, with cross-task injection steering robots toward source-task positions (99.8% of X-VLA episodes align with the source trajectory).

2. In multi-pathway architectures, expert pathways encode motor programs while VLM pathways encode goal semantics.

3. Per-token SAE processing is essential for action fidelity on most architectures, though mean-pooling improves fidelity on X-VLA.

4. Contrastive identification recovers 82+ manipulation concepts, and causal ablation reveals sensitivity spanning 28–92% zero-effect rates.

**Resources:**
The authors released Action Atlas for interactive exploration of VLA representations across all six models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "88158a03-e5a9-4a67-b012-9e32b7e3ce0b"
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-15T16:01:52.875Z_

<details><summary>↩ Tool result · `toolu_013gKKjtXEoNcdCarzUb2hyj`</summary>

```text
Web search results for query: "Kornblith "Similarity of Neural Network Representations Revisited" CKA 2019"

Links: [{"title":"[1905.00414] Similarity of Neural Network Representations Revisited","url":"https://arxiv.org/abs/1905.00414"},{"title":"Similarity of Neural Network Representations Revisited","url":"http://proceedings.mlr.press/v97/kornblith19a/kornblith19a.pdf"},{"title":"[PDF] Similarity of Neural Network Representations Revisited | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Similarity-of-Neural-Network-Representations-Kornblith-Norouzi/726320cdbd04804ffa8f3a78c095bd1b55a2a695"},{"title":"Similarity of Neural Network Representations Revisited | Request PDF","url":"https://www.researchgate.net/publication/332799564_Similarity_of_Neural_Network_Representations_Revisited"},{"title":"Similarity of Neural Network Representations Revisited","url":"https://vitalab.github.io/article/2021/01/28/SimilarityNeuralNets.html"},{"title":"[1905.00414v4] Similarity of Neural Network Representations Revisited","url":"https://arxiv.org/abs/1905.00414v4"},{"title":"Similarity of Neural Network Representations Revisited","url":"https://icml.cc/media/icml-2019/Slides/4871.pdf"},{"title":"Similarity of Neural Network Representations Revisited","url":"https://cka-similarity.github.io/"},{"title":"How should we compare neural network representations?","url":"https://bounded-regret.ghost.io/how-should-we-compare-neural-network-representations/"},{"title":"Similarity of Neural Network Representations Revisited A. Proof of Theorem 1","url":"https://proceedings.mlr.press/v97/kornblith19a/kornblith19a-supp.pdf"}]

Based on the search results, here's what I found about the paper:

"Similarity of Neural Network Representations Revisited" is by Simon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. The paper was published at ICML 2019.

## Paper Overview

The paper examines methods for comparing neural network representations based on canonical correlation analysis (CCA). The authors show that CCA belongs to a family of statistics for measuring multivariate similarity, but that neither CCA nor any other statistic that is invariant to invertible linear transformation can measure meaningful similarities between representations of higher dimension than the number of data points.

## Key Contribution: CKA

The authors introduce a similarity index that measures the relationship between representational similarity matrices and does not suffer from this limitation, which is equivalent to centered kernel alignment (CKA) and is also closely connected to CCA. Unlike CCA, CKA can reliably identify correspondences between representations in networks trained from different initializations.

The paper is available on arXiv (1905.00414) and was also published in the ICML 2019 proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "ad69b23b-8d7c-4aae-9a46-0d9a11a67239"
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-15T16:01:54.418Z_

<details><summary>↩ Tool result · `toolu_01K5jUgiNqRaL6aztKrenffq`</summary>

```text
Web search results for query: "neural collapse in transformers LLMs progressive layer-wise 2023 2024 2025"

Links: [{"title":"SEQ-VCR:PREVENTING COLLAPSE IN INTERMEDIATE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/b577c062bd4f894b7e05fab6440373ed-Paper-Conference.pdf"},{"title":"Neural Collapse is Globally Optimal in Deep Regularized ResNets and Transformers","url":"https://arxiv.org/html/2505.15239v1"},{"title":"Linguistic Collapse: Neural Collapse in (Large) Language Models | OpenReview","url":"https://openreview.net/forum?id=G0LfcMiRkc"},{"title":"Are all layers created equal: A neural collapse perspective | OpenReview","url":"https://openreview.net/forum?id=5eHpefiK8W"},{"title":"AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-024-07566-y"},{"title":"[2505.15239] Neural Collapse is Globally Optimal in Deep Regularized ResNets and Transformers","url":"https://arxiv.org/abs/2505.15239"},{"title":"Layer Collapse in Diffusion Language Models","url":"https://arxiv.org/html/2605.06366v2"},{"title":"Going Beyond LLMs & Transformers. Emerging Architectures for Efficient… | by Przemek Chojecki | Medium","url":"https://pchojecki.medium.com/going-beyond-llms-transformers-39f3291ba9d8"},{"title":"[Literature Review] Neural Collapse is Globally Optimal in Deep Regularized ResNets and Transformers","url":"https://www.themoonlight.io/en/review/neural-collapse-is-globally-optimal-in-deep-regularized-resnets-and-transformers"},{"title":"NeurIPS Poster Linguistic Collapse: Neural Collapse in (Large) Language Models","url":"https://neurips.cc/virtual/2024/poster/95936"}]

Based on the search results, here's what recent research has found about neural collapse in transformers and LLMs with a focus on progressive, layer-wise development:

## Neural Collapse Phenomenon

Neural collapse is a phenomenon observed in classification tasks where top-layer representations collapse into their class means, which become equinorm, equiangular and aligned with the classifiers.

## Progressive Layer-Wise Neural Collapse

Progressive neural collapse occurs where successive layers increasingly compress within-class features and enhance class separation, and has been primarily studied empirically in small architectures on simple tasks or theoretically within linear network contexts. However, its behavior in larger architectures and complex datasets remains underexplored, though recent work extends the study of progressive neural collapse to larger models and more complex datasets.

Key findings from recent studies include:

- Deeper layers significantly enhance neural collapse and play a vital role in generalization but are also more susceptible to memorization.

- In deeper models, middle layers contribute minimally due to diminished neural collapse enhancement leading to redundancy and limited generalization improvements.

- Transformer models outperform convolutional models in enhancing neural collapse on larger datasets and exhibit greater robustness to memorization.

## Neural Collapse in LLMs

Research empirically investigates the impact of scaling the architectures and training of causal language models on their progression towards neural collapse, finding that NC properties that develop with scale and regularization are linked to generalization, with evidence of some relationship between NC and generalization independent of scale.

## Theoretical Advances (2025)

Recent work proves that global optima of deep regularized transformers and residual networks with LayerNorm trained with cross entropy or mean squared error loss are approximately collapsed, and the approximation gets tighter as the depth grows.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "034dee9a-57db-447a-91e8-cf2f545fca92"
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-15T16:01:56.157Z_

<details><summary>↩ Tool result · `toolu_01ELyrHTNqmS2XNQxUbrubw3`</summary>

```text
Web search results for query: "layer-wise probing vision language models multimodal representations CLIP LLaVA per-layer"

Links: [{"title":"How Multimodal LLMs Solve Image Tasks: A Lens on Visual Grounding, Task Reasoning, and Answer Decoding","url":"https://arxiv.org/html/2508.20279v1"},{"title":"Rethinking Visual Layer Selection in Multimodal LLMs","url":"https://arxiv.org/html/2504.21447v1"},{"title":"How Visual Representations Map to Language Feature Space in Multimodal LLMs","url":"https://arxiv.org/html/2506.11976v1"},{"title":"Vision Function Layer in Multimodal LLMs","url":"https://arxiv.org/html/2509.24791"},{"title":"Elevating Visual Perception in Multimodal LLMs with Visual Embedding Distillation","url":"https://arxiv.org/html/2412.09585"},{"title":"LLMs Can Compensate for Deficiencies in Visual Representations","url":"https://arxiv.org/html/2506.05439"},{"title":"LLaVA","url":"https://llava-vl.github.io/"},{"title":"Object detection with multimodal large vision-language models: An in-depth review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525006475"},{"title":"Mechanistic Interpretability Meets Vision Language Models: Insights and Limitations | ICLR Blogposts 2025","url":"https://d2jud02ci9yv69.cloudfront.net/2025-04-28-vlm-understanding-29/blog/vlm-understanding/"},{"title":"Visual Representations inside the Language Model","url":"https://arxiv.org/html/2510.04819v1"}]

Based on the search results, here's what I found about layer-wise probing of vision language models and multimodal representations in CLIP and LLaVA:

## Key Research Findings

**Layer-wise Processing Stages in Multimodal LLMs:**

Research applying layer-wise probing to models like LLaVA-1.5, LLaVA-Next-LLaMA-3, and Qwen2-VL identifies a consistent stage-wise structure in which early layers perform visual grounding, middle layers support lexical integration and semantic reasoning, and final layers prepare task-specific outputs.

**Specific Layer Functions:**

Visual Grounding (Layers 1–4): Early layers primarily encode visual input, producing representations that are largely invariant to both lexical and semantic prompt variations. Together, these controlled variations enable a fine-grained, layer-wise map of how multimodal information flows and transforms within the model.

**Visual Representation Alignment:**

Through systematic analysis of SAE reconstruction error, sparsity patterns, and feature SAE descriptions, research reveals the layer-wise progression through which visual representations gradually align with language feature representations, converging in middle-to-later layers.

**Mechanistic Understanding:**

Multimodal Large Language Models (MLLMs) develop narrow, hierarchical Vision Function Layers (VFLs) specialized for tasks like counting, localization, and OCR recognition. Prominent interpretability techniques include probing, activation patching, logit lens, sparse autoencoders, and automated explanation.

**Information Flow in Language Models:**

Research studying popular MLMs (LLaVA-OneVision, Qwen2.5-VL, and Llama-3-LLaVA-NeXT) found that image value tokens encode sufficient information to perform several perception-heavy tasks zero-shot: segmentation, semantic correspondence, temporal correspondence, and referring expression detection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "4f8aa414-51ab-4156-8956-8faffbe0e941"
}
```

</details>

---

### System

_source line 76_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for \"Linguistic Collapse\" neural collapse large langu…",
  "usage": {
    "total_tokens": 18180,
    "tool_uses": 4,
    "duration_ms": 30090
  },
  "last_tool_name": "WebSearch",
  "uuid": "791d18ab-3b45-43f6-8b24-b4eab524705b",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 77_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TjZzGVF6fJzmSnXaSFByVs`</summary>

```json
{
  "query": "\"Linguistic Collapse\" neural collapse large language models NeurIPS 2024 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "255f0a0a-bfaf-4e18-85dd-5d41e3b445c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhByd4bhdUyF3hiTKrXGB4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1018,
      "cache_read_input_tokens": 17062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1018,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 78_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for Haon 2025 \"mechanistic interpretability steering …",
  "usage": {
    "total_tokens": 28643,
    "tool_uses": 14,
    "duration_ms": 41398
  },
  "last_tool_name": "WebSearch",
  "uuid": "cc0687a2-7ac5-4261-bb36-b2caf11e0de3",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 79_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YHjujnkMewUd6WEUcd8GSu`</summary>

```json
{
  "query": "Haon 2025 \"mechanistic interpretability steering vision-language-action models\" OpenVLA pi0 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "b744331e-df1f-4245-a518-3454de12124c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sg5biWtqdmTWvs6oWrud8g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5931,
      "cache_read_input_tokens": 22655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5931,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 80_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for \"Is Bigger and Deeper Always Better\" probing LLaM…",
  "usage": {
    "total_tokens": 28644,
    "tool_uses": 15,
    "duration_ms": 42341
  },
  "last_tool_name": "WebSearch",
  "uuid": "1a63215b-0329-42b7-bf85-64b158e6c7ce",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 81_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012BjsJbWSzpXDY1nvMuGSpG`</summary>

```json
{
  "query": "\"Is Bigger and Deeper Always Better\" probing LLaMA scales layers authors venue 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "3d4edc85-495e-419b-9aaf-954f30ca62cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sg5biWtqdmTWvs6oWrud8g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5931,
      "cache_read_input_tokens": 22655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5931,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 82_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for Phang 2021 \"Fine-Tuned Transformers Show Clusters…",
  "usage": {
    "total_tokens": 28645,
    "tool_uses": 16,
    "duration_ms": 43339
  },
  "last_tool_name": "WebSearch",
  "uuid": "827040ae-9ba6-49e4-aa3b-171fc942d678",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 83_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HA6Zi1cgh7DbsUWa5qztdu`</summary>

```json
{
  "query": "Phang 2021 \"Fine-Tuned Transformers Show Clusters of Similar Representations\" authors BlackboxNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "289061fb-dd9f-4046-a8f5-d288fea989b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sg5biWtqdmTWvs6oWrud8g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5931,
      "cache_read_input_tokens": 22655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5931,
        "ephemeral_1h_input_tokens": 0
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

_source line 84 · 2026-05-15T16:02:01.948Z_

<details><summary>↩ Tool result · `toolu_01TjZzGVF6fJzmSnXaSFByVs`</summary>

```text
Web search results for query: ""Linguistic Collapse" neural collapse large language models NeurIPS 2024 authors"

Links: [{"title":"Linguistic Collapse: Neural Collapse in (Large) Language Models","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/f88cc8930b47a45ec4733123bf3039b9-Abstract-Conference.html"},{"title":"NeurIPS Poster Linguistic Collapse: Neural Collapse in (Large) Language Models","url":"https://neurips.cc/virtual/2024/poster/95936"},{"title":"GitHub - rhubarbwu/linguistic-collapse: Codebase for Linguistic Collapse: Neural Collapse in (Large) Language Models [NeurIPS 2024] [arXiv:2405.17767]","url":"https://github.com/rhubarbwu/linguistic-collapse"},{"title":"[2405.17767] Linguistic Collapse: Neural Collapse in (Large) Language Models","url":"https://arxiv.org/abs/2405.17767"},{"title":"Linguistic Collapse: Neural Collapse in (Large) Language Models","url":"https://papers.nips.cc/paper_files/paper/2024/hash/f88cc8930b47a45ec4733123bf3039b9-Abstract-Conference.html"},{"title":"Linguistic Collapse: Neural Collapse in (Large) Language Models | OpenReview","url":"https://openreview.net/forum?id=G0LfcMiRkc"},{"title":"[Quick Review] Linguistic Collapse: Neural Collapse in (Large) Language Models","url":"https://liner.com/review/linguistic-collapse-neural-collapse-in-large-language-models"},{"title":"Linguistic Collapse: Neural Collapse in (Large) Language Models Robert Wu","url":"https://openreview.net/pdf?id=G0LfcMiRkc"},{"title":"Linguistic Collapse: Neural Collapse in (Large) Language Models Robert Wu","url":"https://arxiv.org/pdf/2405.17767"},{"title":"[PDF] Linguistic Collapse: Neural Collapse in (Large) Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Linguistic-Collapse:-Neural-Collapse-in-(Large)-Wu-Papyan/90619f1d57d19998ff97656410c78a254fda6e1f"}]

Based on the search results, here's the information about the paper "Linguistic Collapse: Neural Collapse in (Large) Language Models" presented at NeurIPS 2024:

## Authors
The paper was authored by Robert Wu and Vardan Papyan.

## Paper Details
The paper discusses neural collapse (ℕ𝒞), a phenomenon observed in classification tasks where top-layer representations collapse into their class means, which become equinorm, equiangular and aligned with the classifiers, with behaviors associated with generalization and robustness.

## Key Research Focus
The paper empirically investigates the impact of scaling the architectures and training of causal language models (CLMs) on their progression towards neural collapse, finding that neural collapse properties that develop with scale (and regularization) are linked to generalization.

## Publication Details
The paper was published in Advances in Neural Information Processing Systems 37 (NeurIPS 2024) and is also available as arXiv:2405.17767.

## Code Availability
The code is hosted on GitHub at https://github.com/rhubarbwu/linguistic-collapse.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "6db1e087-eabd-4014-a868-cc4695303b75"
}
```

</details>

---

### System

_source line 85_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for \"Exploring Concept Depth\" LLM layers concept comp…",
  "usage": {
    "total_tokens": 28646,
    "tool_uses": 17,
    "duration_ms": 44812
  },
  "last_tool_name": "WebSearch",
  "uuid": "23a0f38f-00fb-4adb-acfd-81dcfcd0002e",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 86_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014XDniqnbWMoYgAmuNfKZYu`</summary>

```json
{
  "query": "\"Exploring Concept Depth\" LLM layers concept complexity probing 2024 authors COLING"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "b61f546f-ff78-44b8-9b59-cfe1efdcadbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sg5biWtqdmTWvs6oWrud8g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5931,
      "cache_read_input_tokens": 22655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5931,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 87_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for \"Mind the Gap\" spectral analysis rank collapse si…",
  "usage": {
    "total_tokens": 28647,
    "tool_uses": 18,
    "duration_ms": 45280
  },
  "last_tool_name": "WebSearch",
  "uuid": "7688733a-28d1-49f6-a3e8-c4f15f8f400e",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 88_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019psJeWdjBUDE9isDSSaUs1`</summary>

```json
{
  "query": "\"Mind the Gap\" spectral analysis rank collapse signal propagation attention layers 2024 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "459a8837-344a-43fd-88a7-c26262a3728b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sg5biWtqdmTWvs6oWrud8g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5931,
      "cache_read_input_tokens": 22655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5931,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 89_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for \"Are all layers created equal\" neural collapse pe…",
  "usage": {
    "total_tokens": 19166,
    "tool_uses": 5,
    "duration_ms": 37619
  },
  "last_tool_name": "WebSearch",
  "uuid": "631a333f-dffd-4c25-baf8-e3b2aea7015b",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 90_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LFJGx4qT5vae5rwmdKnaPB`</summary>

```json
{
  "query": "\"Are all layers created equal\" neural collapse perspective layer-wise 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "9e762868-314f-4406-8e58-cfbe50efad1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XxZ21PTzvuTQjPzyhzVSwo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 940,
      "cache_read_input_tokens": 18080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 940,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

### System

_source line 91_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for Rangamani \"Feature Learning Deep Classifiers Inte…",
  "usage": {
    "total_tokens": 28648,
    "tool_uses": 19,
    "duration_ms": 46323
  },
  "last_tool_name": "WebSearch",
  "uuid": "a7dfa663-ce89-4cbf-9292-30a552ce8be7",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 92_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xo2n5HFroNgFneAaeYwjpP`</summary>

```json
{
  "query": "Rangamani \"Feature Learning Deep Classifiers Intermediate Neural Collapse\" ICML 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "a00febf3-9d13-45d2-8095-3c62f841a2b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sg5biWtqdmTWvs6oWrud8g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5931,
      "cache_read_input_tokens": 22655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5931,
        "ephemeral_1h_input_tokens": 0
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

_source line 93 · 2026-05-15T16:02:05.043Z_

<details><summary>↩ Tool result · `toolu_01YHjujnkMewUd6WEUcd8GSu`</summary>

```text
Web search results for query: "Haon 2025 "mechanistic interpretability steering vision-language-action models" OpenVLA pi0 authors"

Links: [{"title":"[2509.00328] Mechanistic interpretability for steering vision-language-action models","url":"https://arxiv.org/abs/2509.00328"},{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models","url":"https://proceedings.mlr.press/v305/haon25a.html"},{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models","url":"https://arxiv.org/html/2509.00328v1"},{"title":"Mechanistic Interpretability for Steering Vision Language Action Models","url":"https://vla-mech-interp.github.io/"},{"title":"Paper page - Mechanistic interpretability for steering vision-language-action models","url":"https://huggingface.co/papers/2509.00328"},{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=YvsUD8C9QS"},{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models","url":"https://openreview.net/pdf/b39be62fae34fd96c66ab4b8ff09b8eb21a1acf4.pdf"},{"title":"Mechanistic interpretability for steering vision-language-action models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250900328H/abstract"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"Observing and Controlling Features in Vision-Language-Action Models","url":"https://arxiv.org/html/2603.05487v1"}]

Based on the search results, I found information about the paper you're looking for:

## Paper Details

The paper "Mechanistic Interpretability for Steering Vision-Language-Action Models" was authored by Bear Häon, Kaylene Caswell Stocking, Ian Chuang, and Claire Tomlin.

The paper was published in the Proceedings of The 9th Conference on Robot Learning, PMLR 305:2743-2762, 2025.

## Key Findings

The researchers project feedforward activations within transformer layers onto the token embedding basis, identifying sparse semantic directions such as speed and direction that are causally linked to action selection, and introduce a general-purpose activation steering method that modulates behavior in real time, without fine-tuning, reward signals, or environment interaction.

The method was evaluated on two recent open-source VLAs, Pi0 and OpenVLA, and demonstrated zero-shot behavioral control in simulation (LIBERO) and on a physical robot (UR5).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "f403832e-1573-4899-87ee-a4f235c8ac6f"
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-15T16:02:07.272Z_

<details><summary>↩ Tool result · `toolu_012BjsJbWSzpXDY1nvMuGSpG`</summary>

```text
Web search results for query: ""Is Bigger and Deeper Always Better" probing LLaMA scales layers authors venue 2024"

Links: [{"title":"[2312.04333] Is Bigger and Deeper Always Better? Probing LLaMA Across Scales and Layers","url":"https://arxiv.org/abs/2312.04333"},{"title":"Is Bigger and Deeper Always Better? Probing LLaMA Across Scales and Layers","url":"https://arxiv.org/html/2312.04333v4"},{"title":"GitHub - nuochenpku/LLaMA_Analysis: This is official project in our paper: Is Bigger and Deeper Always Better? Probing LLaMA Across Scales and Layers","url":"https://github.com/nuochenpku/LLaMA_Analysis"},{"title":"Is Bigger and Deeper Always Better? Probing LLaMA Across Scales and Layers","url":"https://openreview.net/pdf/e0d65067d283d0b8f856fa093e1bdd2142f98838.pdf"},{"title":"Is Bigger and Deeper Always Better? Probing LLaMA ...","url":"https://axi.lims.ac.uk/paper/2312.04333"},{"title":"LLaMA_Analysis/stopping_criteria.py at main · nuochenpku/LLaMA_Analysis","url":"https://github.com/nuochenpku/LLaMA_Analysis/blob/main/stopping_criteria.py"},{"title":"Ning Wu","url":"https://scholar.google.com/citations?user=rH_ai9oAAAAJ&hl=en"},{"title":"LLMs: Bigger is Not Always Better","url":"https://amperecomputing.com/en/blogs/llms-bigger-is-not-always-better"},{"title":"Are Deeper LLMs Smarter, or Just Longer? - Gonzo ML","url":"https://gonzoml.substack.com/p/are-deeper-llms-smarter-or-just-longer"},{"title":"Beyond Surface: Probing LLaMA Across Scales and Layers","url":"https://arxiv.org/html/2312.04333v3"}]

Based on the search results, here is information about the paper "Is Bigger and Deeper Always Better? Probing LLaMA Across Scales and Layers":

## Paper Details

**Title:** Is Bigger and Deeper Always Better? Probing LLaMA Across Scales and Layers

**Authors:** Nuo Chen and 6 other authors (specifically: Chen, Nuo, Wu, Ning, Liang, Shining, Gong, Ming, Shou, Linjun, Zhang, Dongmei, and Li, Jia)

**Venue:** arXiv preprint arXiv:2312.04333

**Publication Date:** January 9, 2024

## Key Research Findings

The paper examines LLaMA across different scales and layers through multiple-choice probing tasks. The main findings are:

**Horizontal Analysis (across model sizes):** Enlarging model sizes almost could not automatically impart additional knowledge or computational prowess. Instead, it can enhance reasoning abilities, especially in math problem solving, and helps reduce hallucinations, but only beyond certain size thresholds

**Vertical Analysis (across layers):** The lower and middle layers of LLaMA have almost negligible pure arithmetic and factual knowledge capabilities. As the network layers deepen, there is a noticeable leap in performance. Contrarily, even at the very lowest layers, LLaMA possesses logical thinking and recognitive abilities, such as in mathematics, logical reasoning, and avoiding hallucinations. While these abilities do enhance slightly with deeper layers, the improvement remains quite limited


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "39d09ead-2a1f-4633-96a0-4679acab95d5"
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-15T16:02:07.503Z_

<details><summary>↩ Tool result · `toolu_01HA6Zi1cgh7DbsUWa5qztdu`</summary>

```text
Web search results for query: "Phang 2021 "Fine-Tuned Transformers Show Clusters of Similar Representations" authors BlackboxNLP"

Links: [{"title":"Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers - ACL Anthology","url":"https://aclanthology.org/2021.blackboxnlp-1.42/"},{"title":"Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers","url":"https://www.researchgate.net/publication/357387675_Fine-Tuned_Transformers_Show_Clusters_of_Similar_Representations_Across_Layers"},{"title":"[2109.08406] Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers","url":"https://arxiv.org/abs/2109.08406"},{"title":"[PDF] Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/d20bcf41b772ea31a8ddd20317ee99fe7e1f32ca"},{"title":"Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers - Jason Phang","url":"https://jasonphang.com/publication/2021-09-18-cka"},{"title":"Fine-Tuned Transformers Show Clusters of Similar ...","url":"https://aclanthology.org/2021.blackboxnlp-1.42.pdf"},{"title":"Papers with Code - Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers","url":"https://paperswithcode.com/paper/fine-tuned-transformers-show-clusters-of"},{"title":"Fine-Tuned Transformers Show Clusters of Similar ... - NSF PAR","url":"https://par.nsf.gov/servlets/purl/10358004"},{"title":"Fine-Tuned Transformers Show Clusters of Similar ...","url":"https://openreview.net/pdf?id=SrIhEzbuxYk"},{"title":"Does Freezing Layers in RoBERTa Help?","url":"https://aclanthology.org/2022.blackboxnlp-1.19.pdf"}]

I found the paper you're looking for! Here are the details:

**Paper Title:** "Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers"

**Authors:** Jason Phang, Haokun Liu, and Samuel R. Bowman

**Conference:** Proceedings of the Fourth BlackboxNLP Workshop on Analyzing and Interpreting Neural Networks for NLP, pages 529–538, Punta Cana, Dominican Republic

**Publication Date:** November 2021

**Key Methodology:** The work uses centered kernel alignment (CKA), a method for comparing learned representations, to measure the similarity of representations in task-tuned models across layers.

**Main Finding:** In experiments across twelve NLU tasks, the authors discover a consistent block diagonal structure in the similarity of representations within fine-tuned RoBERTa and ALBERT models, with strong similarity within clusters of earlier and later layers, but not between them.

The paper is available at the ACL Anthology: https://aclanthology.org/2021.blackboxnlp-1.42/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "736e0a64-32cf-4490-866f-39605ca5478e"
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-15T16:02:09.344Z_

<details><summary>↩ Tool result · `toolu_014XDniqnbWMoYgAmuNfKZYu`</summary>

```text
Web search results for query: ""Exploring Concept Depth" LLM layers concept complexity probing 2024 authors COLING"

Links: [{"title":"Exploring Concept Depth: How Large Language Models Acquire Knowledge and Concept at Different Layers? - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.37/"},{"title":"Exploring Concept Depth: How Large Language Models ...","url":"https://aclanthology.org/2025.coling-main.37.pdf"},{"title":"[2404.07066] Exploring Concept Depth: How Large Language Models Acquire Knowledge and Concept at Different Layers?","url":"https://arxiv.org/abs/2404.07066"},{"title":"Exploring Concept Depth: How Large Language Models Acquire Knowledge at Different Layers?","url":"https://arxiv.org/html/2404.07066v1"},{"title":"GitHub - Luckfort/CD: [COLING'25] Exploring Concept Depth: How Large Language Models Acquire Knowledge at Different Layers?","url":"https://github.com/Luckfort/CD"},{"title":"Exploring Concept Depth: How Large Language Models Acquire","url":"https://arxiv.org/pdf/2404.07066"},{"title":"Exploring Concept Depth: How Large Language Models Acquire Knowledge and Concepts at Different Layers?","url":"https://arxiv.org/html/2404.07066v5"},{"title":"Exploring Concept Depth: How Large Language Models ...","url":"https://www.emergentmind.com/papers/2404.07066"},{"title":"[2404.07066] Exploring Concept Depth: How Large Language Models Acquire Knowledge at Different Layers?","url":"https://ar5iv.labs.arxiv.org/html/2404.07066"},{"title":"Exploring Concept Depth: How Large Language Models Acquire Knowledge at Different Layers?","url":"https://luckfort.github.io/explore_CD/"}]

Based on the search results, here is the information about the paper "Exploring Concept Depth":

## Paper Overview

The paper explores the hypothesis that LLMs process concepts of varying complexities in different layers, introducing the idea of "Concept Depth" to suggest that more complex concepts are typically acquired in deeper layers.

## Research Methodology

The authors categorize concepts based on their level of abstraction within factual, emotional, and inferential tasks, and conduct extensive probing experiments using layer-wise representations across various LLM families (Gemma, LLaMA, Qwen) on various datasets spanning the three domains of tasks.

## Key Findings

The findings reveal that models could efficiently conduct probing for simpler tasks in shallow layers, and more complex tasks typically necessitate deeper layers for accurate understanding. Additionally, the authors examine how external factors, such as adding noise to the input and quantizing the model weights, might affect layer-wise representations.

## Authors and Publication

The paper is authored by Jin, Mingyu; Yu, Qinkai; Huang, Jingyuan; Zeng, Qingcheng; Wang, Zhenting; Hua, Wenyue; Zhao, Haiyan; Mei, Kai; Meng, Yanda; Ding, Kaize; Yang, Fan; Du, Mengnan; and Zhang, Yongfeng. The paper was accepted by COLING 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "598b5d53-448d-4de2-b0fd-a7c4311209cf"
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-15T16:02:10.386Z_

<details><summary>↩ Tool result · `toolu_019psJeWdjBUDE9isDSSaUs1`</summary>

```text
Web search results for query: ""Mind the Gap" spectral analysis rank collapse signal propagation attention layers 2024 authors"

Links: [{"title":"[2410.07799] Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers","url":"https://arxiv.org/abs/2410.07799"},{"title":"Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers","url":"https://arxiv.org/html/2410.07799v2"},{"title":"Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers | OpenReview","url":"https://openreview.net/forum?id=sRKtbGsebH"},{"title":"Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers - Paper Detail","url":"https://deeplearn.org/arxiv/572034/mind-the-gap:-a-spectral-analysis-of-rank-collapse-and-signal-propagation-in-attention-layers"},{"title":"ICML Poster Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers","url":"https://icml.cc/virtual/2025/poster/43837"},{"title":"Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Transformers | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/mind-gap-spectral-analysis-rank-collapse-signal"},{"title":"Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Transformers","url":"https://arxiv.org/html/2410.07799v1"},{"title":"Mind the gap: a spectral analysis of rank collapse and signal propagation in attention layers - ORA - Oxford University Research Archive","url":"https://ora.ox.ac.uk/objects/uuid:f63a42b9-a428-400d-8a08-38e1b49c4874"},{"title":"Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Transformers | OpenReview","url":"https://openreview.net/forum?id=X6xzYP2cMk"},{"title":"Published as a conference paper at ICLR 2025 DIFFERENTIAL TRANSFORMER","url":"https://arxiv.org/pdf/2410.05258"}]

Based on the web search results, here's what I found about the "Mind the Gap" paper:

## Paper Overview

"Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers" is authored by Thiziri Nait Saada and 2 other authors. The full authorship is Thiziri Nait Saada, Alireza Naderi, and Jared Tanner.

## Main Contributions

The paper identifies rank collapse in width as a previously unknown challenge unique to softmax attention layers, which occurs as the context length increases. Using Random Matrix Theory, the authors conduct a rigorous analysis that uncovers a spectral gap between the two largest singular values of the attention matrix as the cause of rank collapse in width, which in turn exacerbates vanishing/exploding gradients and rank collapse in depth.

## Proposed Solution

The authors propose a novel yet simple practical solution to mitigate rank collapse in width by removing the outlier eigenvalue(s).

## Paper Details

The paper was first submitted on October 10, 2024, and it will be presented at the 42nd International Conference on Machine Learning (ICML 2025), 13th - 19th July 2025, in Vancouver, BC, Canada.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "e0f03a4b-7ca1-475d-957d-60107097c122"
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-15T16:02:11.151Z_

<details><summary>↩ Tool result · `toolu_01LFJGx4qT5vae5rwmdKnaPB`</summary>

```text
Web search results for query: ""Are all layers created equal" neural collapse perspective layer-wise 2024 2025"

Links: [{"title":"Are all layers created equal: A neural collapse perspective | OpenReview","url":"https://openreview.net/forum?id=5eHpefiK8W"},{"title":"Are all layers created equal: A neural collapse perspective","url":"https://proceedings.mlr.press/v280/zhou25a.html"},{"title":"[2210.02192] Are All Losses Created Equal: A Neural Collapse Perspective","url":"https://arxiv.org/abs/2210.02192"},{"title":"Are All Losses Created Equal: A Neural Collapse Perspective Jinxin Zhou","url":"https://papers.neurips.cc/paper_files/paper/2022/file/cdce17de141c9fba3bdf175a0b721941-Paper-Conference.pdf"},{"title":"Neural Collapse Geometry in Deep Learning","url":"https://www.emergentmind.com/topics/neural-collapse-geometry"},{"title":"An Unconstrained Layer-Peeled Perspective on Neural Collapse","url":"https://eurekamag.com/research/093/799/093799262.php"},{"title":"Neural Collapse beyond the Unconstrained Features Model: Landscape, Dynamics, and Generalization in the Mean-Field Regime","url":"https://arxiv.org/html/2501.19104v2"},{"title":"Tutorial: Understanding Deep Representation Learning via Neural Collapse | IEEE Resource Center","url":"https://resourcecenter.ieee.org/education/tutorials/spsicassp24tut2001"},{"title":"Neural Collapse in Deep Linear Networks - Tan Minh Nguyen","url":"https://tanmnguyen89.github.io/neural_collapse_in_deep_linear.pdf"},{"title":"Are All Layers Created Equal?","url":"https://jmlr.org/papers/volume23/20-069/20-069.pdf"}]

Based on the search results, I found a highly relevant recent paper that directly addresses your query:

## "Are all layers created equal: A neural collapse perspective"

This paper by Zhou, Jiang, and Zhu was published in 2025 in the Proceedings of Machine Learning Research at the Conference on Parsimony and Learning.

### Key Findings

The paper's main insights address the research question directly:

**Layer Inequality**: Deeper layers significantly enhance neural collapse and play a vital role in generalization but are also more susceptible to memorization.

### Research Scope

Progressive neural collapse, where successive layers increasingly compress within-class features and enhance class separation, has been primarily studied empirically in small architectures on simple tasks or theoretically within linear network contexts, but its behavior in larger architectures and complex datasets remains underexplored. This work extends the study of progressive neural collapse to larger models and more complex datasets, including clean and noisy data settings.

### Related Perspectives

The research also connects to broader findings about data separation across layers: Deep neural networks separate data according to their class membership from the bottom layers to the top layers, where each layer roughly improves a certain measure of data separation by an equal multiplicative factor.

The paper provides a comprehensive investigation of how different layers contribute differently to neural collapse, generalization, memorization, and robustness in modern deep learning systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "fe75cd14-41d6-486c-83a3-bda4bfc7f4de"
}
```

</details>

---

### System

_source line 99_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for CKA centered kernel alignment fine-tuning LoRA wh…",
  "usage": {
    "total_tokens": 20082,
    "tool_uses": 6,
    "duration_ms": 46943
  },
  "last_tool_name": "WebSearch",
  "uuid": "9cf203e1-c0ae-4589-a987-173cfb2d93a5",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 100_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012Bfv1fa6zrf4yMs1fQoEkL`</summary>

```json
{
  "query": "CKA centered kernel alignment fine-tuning LoRA which layers change most pretrained models 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "1b9e823f-a4c6-4b27-a760-e039e757f9bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gj9PKR6xAMGqArXQ4X2cUo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 873,
      "cache_read_input_tokens": 19020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 873,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 101 · 2026-05-15T16:02:14.754Z_

<details><summary>↩ Tool result · `toolu_01Xo2n5HFroNgFneAaeYwjpP`</summary>

```text
Web search results for query: "Rangamani "Feature Learning Deep Classifiers Intermediate Neural Collapse" ICML 2023"

Links: [{"title":"Feature learning in deep classifiers through Intermediate Neural Collapse","url":"https://proceedings.mlr.press/v202/rangamani23a.html"},{"title":"Feature learning in deep classifiers through intermediate neural collapse | Proceedings of the 40th International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3618408.3619602"},{"title":"Akshay Rangamani Assistant Professor, Data Science, NJIT","url":"https://akshay-r.github.io/files/AkshayR_CV.pdf"},{"title":"NTNU Open: Feature Learning in the Neural Collapse regime of Deep Classifiers","url":"https://ntnuopen.ntnu.no/ntnu-xmlui/handle/11250/3112624"},{"title":"Deep neural collapse is provably optimal for the deep unconstrained features model | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3668428"},{"title":"Neural Collapse in Deep Homogeneous Classifiers and The Role of Weight Decay | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Neural-Collapse-in-Deep-Homogeneous-Classifiers-and-Rangamani-Banburski-Fahey/e41d045e4809fc04452b7c9dd81a5ae76b7df21a"},{"title":"FORMATION OF REPRESENTATIONS IN NEURAL ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/ab6a2c6ee757afe43882121281f6065c-Paper-Conference.pdf"},{"title":"Feature learning in deep classifiers through Intermediate Neural Collapse","url":"https://dspace.mit.edu/handle/1721.1/148239"},{"title":"Feature learning in deep classifiers through Intermediate ...","url":"https://cbmm.mit.edu/sites/default/files/publications/Feature_Learning_memo.pdf"},{"title":"[2603.23805] Deep Neural Regression Collapse","url":"https://arxiv.org/abs/2603.23805"}]

I found the paper! Here are the search results:

## Paper Information

The paper "Feature learning in deep classifiers through Intermediate Neural Collapse" was published in the Proceedings of the 40th International Conference on Machine Learning (ICML) in 2023.

**Authors:** Akshay Rangamani, Marius Lindegaard, Tomer Galanti, and Tomaso A Poggio

**Citation Details:** Proceedings of the 40th International Conference on Machine Learning, PMLR 202:28729-28745, 2023

## Paper Overview

The paper conducts an empirical study of the feature learning process in deep classifiers, investigating a training phenomenon called Neural Collapse (NC), in which the top-layer feature embeddings of samples from the same class tend to concentrate around their means, and the top layer's weights align with those features.

The study investigates if these properties extend to intermediate layers, empirically studying the evolution of the covariance and mean of representations across different layers and showing that as we move deeper into a trained neural network, the within-class covariance decreases relative to the between-class covariance.

The paper is available at the official ICML proceedings link: https://proceedings.mlr.press/v202/rangamani23a.html


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "cb8ea99d-2e1f-4c52-bd6a-aac501dd773e"
}
```

</details>

---

### System

_source line 102_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for \"Analyzing Fine-tuning Representation Shift Multi…",
  "usage": {
    "total_tokens": 34285,
    "tool_uses": 20,
    "duration_ms": 59643
  },
  "last_tool_name": "WebSearch",
  "uuid": "86790e06-fab8-478e-8626-e747b5323f5f",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 103_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EAWYXgZYbLQmXLMvNHeCho`</summary>

```json
{
  "query": "\"Analyzing Fine-tuning Representation Shift Multimodal LLMs\" 2025 arxiv authors VLM layer-wise"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "0e51d94b-28d7-4621-b574-b100a2b749c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rx1tEGrGjX2uGwRF8kXNSy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5599,
      "cache_read_input_tokens": 28586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5599,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

### System

_source line 104_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for \"SEQ-VCR\" preventing collapse intermediate repres…",
  "usage": {
    "total_tokens": 34323,
    "tool_uses": 21,
    "duration_ms": 60578
  },
  "last_tool_name": "WebSearch",
  "uuid": "ad5509a3-28fc-4cc2-86e1-28029c4534da",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 105_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013eXQZ2KjbWhMJAp9iVN6ot`</summary>

```json
{
  "query": "\"SEQ-VCR\" preventing collapse intermediate representations transformers ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "fb61c235-124d-47a6-883f-0a76ba9d32e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rx1tEGrGjX2uGwRF8kXNSy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5599,
      "cache_read_input_tokens": 28586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5599,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

### System

_source line 106_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for Dong \"attention entropy collapse\" transformers \"r…",
  "usage": {
    "total_tokens": 34361,
    "tool_uses": 22,
    "duration_ms": 62040
  },
  "last_tool_name": "WebSearch",
  "uuid": "46047f77-9e0a-4713-981c-d595e2215b2e",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 107_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012Qwhr892xTGfipiU9WyEzV`</summary>

```json
{
  "query": "Dong \"attention entropy collapse\" transformers \"rank collapse\" residual connections layer normalization 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "9b0cb5ec-6da5-44f0-b182-90dfd53d97ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rx1tEGrGjX2uGwRF8kXNSy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5599,
      "cache_read_input_tokens": 28586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5599,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 108 · 2026-05-15T16:02:20.502Z_

<details><summary>↩ Tool result · `toolu_012Bfv1fa6zrf4yMs1fQoEkL`</summary>

```text
Web search results for query: "CKA centered kernel alignment fine-tuning LoRA which layers change most pretrained models 2023 2024"

Links: [{"title":"TRepLiNa: Layer-wise CKA+REPINA Alignment Improves Low-Resource Machine Translation in Aya-23 8B","url":"https://arxiv.org/html/2510.06249"},{"title":"GitHub - RistoAle97/centered-kernel-alignment: CKA (Centered Kernel Alignment) implemented in PyTorch · GitHub","url":"https://github.com/RistoAle97/centered-kernel-alignment"},{"title":"Centered Kernel Alignment (CKA) Similarity","url":"https://www.emergentmind.com/topics/centered-kernel-alignment-cka-similarity"},{"title":"TRepLiNa: Layer-wise CKA+REPINA Alignment Improves Low-Resource","url":"https://www.arxiv.org/pdf/2510.06249v2"},{"title":"Centered Kernel Alignment","url":"https://jyopari.github.io/posts/CKA"},{"title":"Using Centered Kernel Alignment for Understanding and ...","url":"https://digitalcommons.uri.edu/cgi/viewcontent.cgi?article=3256&context=theses"},{"title":"Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers - ACL Anthology","url":"https://aclanthology.org/2021.blackboxnlp-1.42/"},{"title":"Centered Kernel Alignment (CKA) Overview","url":"https://www.emergentmind.com/topics/centered-kernel-alignment-cka"},{"title":"Beyond Cosine: Why Centered Kernel Alignment (CKA) is Your Go-To for Validating Multilingual Models | by Vigneswaran Sugumaaran | Medium","url":"https://medium.com/@vigneswaran.sugumaaran/beyond-cosine-why-centered-kernel-alignment-cka-is-your-go-to-for-validating-multilingual-models-2bc3c1978302"},{"title":"TRepLiNa: Layer-wise CKA+REPINA Alignment Improves ...","url":"https://aclanthology.org/2025.mmloso-1.3.pdf"}]

Based on my web search results, here's what I found about CKA (Centered Kernel Alignment), fine-tuning, and LoRA research:

## Key Findings:

**CKA and Fine-Tuning Analysis:**
Centered kernel alignment (CKA) is used as a method for comparing learned representations to measure the similarity of representations in task-tuned models across layers. In experiments across twelve NLU tasks, a consistent block diagonal structure in the similarity of representations was discovered within fine-tuned RoBERTa and ALBERT models, with strong similarity within clusters of earlier and later layers, but not between them.

**Which Layers Change Most:**
The similarity of later layer representations implies that later layers only marginally contribute to task performance, and experiments verified that the top few layers of fine-tuned Transformers can be discarded without hurting performance. This suggests that **earlier and middle layers change more significantly during fine-tuning**, while later layers remain more similar to each other.

**Recent Applications (2024-2025):**
Recent research uses centered kernel alignment (CKA) together with representation projection invariance (REPINA) to stabilize features against representation drift during fine-tuning. Studies have performed experiments using QLoRA-based fine-tuning on models like Aya-23 8B.

The research indicates that CKA is a valuable tool for understanding which layers in pretrained models undergo the most significant changes during fine-tuning, with findings suggesting that middle layers are more critical to task adaptation than later layers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "74dad29c-53e2-4cec-aac5-4a6800fcfd33"
}
```

</details>

---

### System

_source line 109_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for \"signal propagation transformers\" Noci Anagnostid…",
  "usage": {
    "total_tokens": 34399,
    "tool_uses": 23,
    "duration_ms": 62966
  },
  "last_tool_name": "WebSearch",
  "uuid": "733b89fc-c750-4efd-bf49-3852f3f2e8a0",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 110_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XXFNTbKbgrjVd6kUrCishv`</summary>

```json
{
  "query": "\"signal propagation transformers\" Noci Anagnostidis rank collapse 2022 depth"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "fe8f7090-015f-406f-ba6b-c9bf077c1595",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rx1tEGrGjX2uGwRF8kXNSy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5599,
      "cache_read_input_tokens": 28586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5599,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

### System

_source line 111_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for Buurmeijer VLA 2025 2026 probing robot vision lan…",
  "usage": {
    "total_tokens": 34437,
    "tool_uses": 24,
    "duration_ms": 63920
  },
  "last_tool_name": "WebSearch",
  "uuid": "b424b96c-2697-4273-a3b3-6218bd119a95",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 112_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Tj34CwWgM55Xn6hK6AWK5r`</summary>

```json
{
  "query": "Buurmeijer VLA 2025 2026 probing robot vision language action representation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "0bb955f5-067e-45bf-90d7-2cbb7cc65f30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rx1tEGrGjX2uGwRF8kXNSy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5599,
      "cache_read_input_tokens": 28586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5599,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

### System

_source line 113_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for RT-2 Brohan 2023 vision language action model rob…",
  "usage": {
    "total_tokens": 34475,
    "tool_uses": 25,
    "duration_ms": 64740
  },
  "last_tool_name": "WebSearch",
  "uuid": "f5f97d2c-cba1-40f6-a2fc-fdae0c8dcef9",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 114_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0111JFDAknfvDGsKFW7sdbYY`</summary>

```json
{
  "query": "RT-2 Brohan 2023 vision language action model robotic transformer PaLM-E internal representations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "fe584804-0045-47af-b06e-b6e0746c479f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rx1tEGrGjX2uGwRF8kXNSy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5599,
      "cache_read_input_tokens": 28586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5599,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

### System

_source line 115_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for Zou et al 2023 \"Representation Engineering\" paper…",
  "usage": {
    "total_tokens": 21149,
    "tool_uses": 7,
    "duration_ms": 56339
  },
  "last_tool_name": "WebSearch",
  "uuid": "4b7b0fab-5f9d-4c1e-9091-3574af0de831",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 116_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GTAXu4k1w24NXjZ5oAVRJa`</summary>

```json
{
  "query": "Zou et al 2023 \"Representation Engineering\" paper authors venue findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "f6573a11-68ce-4796-b32d-c427da7f1238",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JHfUmA27HJ7eCsHrz5e98V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1026,
      "cache_read_input_tokens": 19893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1026,
        "ephemeral_1h_input_tokens": 0
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

_source line 117 · 2026-05-15T16:02:25.437Z_

<details><summary>↩ Tool result · `toolu_013eXQZ2KjbWhMJAp9iVN6ot`</summary>

```text
Web search results for query: ""SEQ-VCR" preventing collapse intermediate representations transformers ICLR 2025"

Links: [{"title":"[2411.02344] Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning","url":"https://arxiv.org/abs/2411.02344"},{"title":"Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/b577c062bd4f894b7e05fab6440373ed-Abstract-Conference.html"},{"title":"Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning | OpenReview","url":"https://openreview.net/forum?id=30oIfmrcFO"},{"title":"SEQ-VCR:PREVENTING COLLAPSE IN INTERMEDIATE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/b577c062bd4f894b7e05fab6440373ed-Paper-Conference.pdf"},{"title":"Seq-VCR:Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning","url":"https://arxiv.org/html/2411.02344v2"},{"title":"(PDF) Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning","url":"https://www.researchgate.net/publication/385560131_Seq-VCR_Preventing_Collapse_in_Intermediate_Transformer_Representations_for_Enhanced_Reasoning"},{"title":"Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241102344R/abstract"},{"title":"seq-vcr:preventing collapse in intermediate transformer ...","url":"https://arxiv.org/pdf/2411.02344"},{"title":"GitHub - rarefin/SEQ_VCR: Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning","url":"https://github.com/rarefin/seq_vcr"},{"title":"SEQ-VCR : preventing collapse in intermediate transformer representations for enhanced reasoning - PolyPublie","url":"https://publications.polymtl.ca/66812/"}]

I found comprehensive information about SEQ-VCR from ICLR 2025. Here's what the research presents:

## Overview

SEQ-VCR is a paper presented at ICLR 2025 by Md Rifat Arefin, Gopeshh Raaj Subbaraj, Nicolas Gontier, Yann LeCun, Irina Rish, Ravid Shwartz-Ziv, and Christopher Pal.

## The Problem

Decoder-only Transformers often struggle with complex reasoning tasks, particularly arithmetic reasoning requiring multiple sequential operations, with representation collapse in the model's intermediate layers identified as a key factor limiting their reasoning capabilities.

## The Solution

The paper proposes Sequential Variance-Covariance Regularization (Seq-VCR), which enhances the entropy of intermediate representations and prevents collapse, and combines this with dummy pause tokens as substitutes for chain-of-thought (CoT) tokens.

## Key Results

In the challenging 5 × 5 integer multiplication task, the approach achieves 99.5% exact match accuracy, outperforming models of the same size (which yield 0% accuracy) and GPT-4 with five-shot CoT prompting (44%). Superior results are also demonstrated on arithmetic expression and longest increasing subsequence (LIS) datasets.

## Key Findings

The findings highlight the importance of preventing intermediate layer representation collapse to enhance the reasoning capabilities of Transformers and show that Seq-VCR offers an effective solution without requiring explicit CoT supervision.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "cf67abb4-0d01-4100-a23d-aba3d8f17010"
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-15T16:02:26.163Z_

<details><summary>↩ Tool result · `toolu_01EAWYXgZYbLQmXLMvNHeCho`</summary>

```text
Web search results for query: ""Analyzing Fine-tuning Representation Shift Multimodal LLMs" 2025 arxiv authors VLM layer-wise"

Links: [{"title":"[2501.03012] Analyzing Finetuning Representation Shift for Multimodal LLMs Steering","url":"https://arxiv.org/abs/2501.03012"},{"title":"Analyzing Fine-tuning Representation Shift for Multimodal LLMs Steering","url":"https://arxiv.org/html/2501.03012v1"},{"title":"[2501.03012v1] Analyzing Fine-tuning Representation Shift for Multimodal LLMs Steering alignment","url":"https://arxiv.org/abs/2501.03012v1"},{"title":"Analyzing Fine-tuning Representation Shift for Multimodal LLMs Steering","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Khayatan_Analyzing_Finetuning_Representation_Shift_for_Multimodal_LLMs_Steering_ICCV_2025_paper.pdf"},{"title":"[2501.03012] Analyzing Fine-tuning Representation Shift for Multimodal LLMs Steering alignment","url":"http://export.arxiv.org/abs/2501.03012"},{"title":"Analyzing Fine-tuning Representation Shift for Multimodal LLMs Steering alignment | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2501.03012"},{"title":"llm-research-summaries/training/Analyzing-Fine-tuning-Representation-Shift-for-Multimodal-LLMs-Steering_2501.03012v1.md at main · cognitivetech/llm-research-summaries","url":"https://github.com/cognitivetech/llm-research-summaries/blob/main/training/Analyzing-Fine-tuning-Representation-Shift-for-Multimodal-LLMs-Steering_2501.03012v1.md"},{"title":"ICCV 2025 Open Access Repository","url":"https://openaccess.thecvf.com/content/ICCV2025/html/Khayatan_Analyzing_Finetuning_Representation_Shift_for_Multimodal_LLMs_Steering_ICCV_2025_paper.html"},{"title":"PARAMETER-EFFICIENT MULTIMODAL INSTRUCTION TUNING","url":"https://arxiv.org/pdf/2512.14926"},{"title":"Understanding Multimodal LLMs Under Distribution Shifts: An Information-Theoretic Approach","url":"https://arxiv.org/html/2502.00577v1"}]

I found the paper you're looking for! Here are the key details:

## Paper Information

The paper is titled "Analyzing Finetuning Representation Shift for Multimodal LLMs Steering" (arXiv 2501.03012).

## Authors

The authors are Pegah Khayatan, Mustafa Shukor, Jayneel Parekh, and Matthieu Cord (with one additional co-author mentioned in some versions).

## Research Focus

The work systematically analyzes the evolution of hidden state representations to reveal how fine-tuning alters the internal structure of a model to specialize in new multimodal tasks, using a concept-based approach to map hidden states to interpretable visual and textual concepts.

## Key Findings

The researchers demonstrate the use of shift vectors to capture concept changes, and these shift vectors allow recovery of fine-tuned concepts by applying simple, computationally inexpensive additive concept shifts in the original model.

The features related to different concepts are almost linearly separable, and this becomes more prominent in deeper layers, which validates the linear representation hypothesis for MLLMs.

## Applications

The findings have direct applications for MLLM steering, which can be used for model debiasing as well as enforcing safety in MLLM output, proposing a training-free, ready-to-use framework for MLLM behavior interpretability and control.

The code for this project is publicly available at https://github.com/mshukor/xl-vlms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "7effa277-c09d-4932-96eb-4b804264f49a"
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-15T16:02:27.544Z_

<details><summary>↩ Tool result · `toolu_01XXFNTbKbgrjVd6kUrCishv`</summary>

```text
Web search results for query: ""signal propagation transformers" Noci Anagnostidis rank collapse 2022 depth"

Links: [{"title":"[2206.03126] Signal Propagation in Transformers: Theoretical Perspectives and the Role of Rank Collapse","url":"https://arxiv.org/abs/2206.03126"},{"title":"Signal Propagation in Transformers: Theoretical Perspectives and the Role of Rank Collapse","url":"https://proceedings.neurips.cc/paper_files/paper/2022/hash/ae0cba715b60c4052359b3d52a2cff7f-Abstract-Conference.html"},{"title":"Signal Propagation in Transformers: Theoretical Perspectives and the Role of Rank Collapse | OpenReview","url":"https://openreview.net/forum?id=FxVH7iToXS"},{"title":"(PDF) Signal Propagation in Transformers: Theoretical Perspectives and the Role of Rank Collapse","url":"https://www.researchgate.net/publication/361161686_Signal_Propagation_in_Transformers_Theoretical_Perspectives_and_the_Role_of_Rank_Collapse"},{"title":"NeurIPS Poster Signal Propagation in Transformers: Theoretical Perspectives and the Role of Rank Collapse","url":"https://neurips.cc/virtual/2022/poster/53861"},{"title":"Signal Propagation in Transformers: Theoretical Perspectives and the Role of Rank Collapse | Max Planck Institute for Intelligent Systems","url":"https://is.mpg.de/publications/nocietal22"},{"title":"[PDF] Signal Propagation in Transformers: Theoretical Perspectives and the Role of Rank Collapse | Semantic Scholar","url":"https://www.semanticscholar.org/paper/5eeb80dc67590422db64ca95ec0aded24799cfb6"},{"title":"MIND THE GAP: A SPECTRAL ANALYSIS OF RANK ...","url":"https://openreview.net/pdf?id=X6xzYP2cMk"},{"title":"Signal Propagation in Transformers: Theoretical","url":"https://openreview.net/pdf?id=FxVH7iToXS"},{"title":"Signal Propagation in Transformers: Theoretical Perspectives and the Role of Rank Collapse | Request PDF","url":"https://www.researchgate.net/publication/401460741_Signal_Propagation_in_Transformers_Theoretical_Perspectives_and_the_Role_of_Rank_Collapse"}]

Based on the search results, I found the research paper you're looking for. Here's what the study covers:

## Signal Propagation in Transformers: Rank Collapse Research

The paper "Signal Propagation in Transformers: Theoretical Perspectives and the Role of Rank Collapse" was authored by Lorenzo Noci, Sotiris Anagnostidis, Luca Biggio, Antonio Orvieto, Sidak Pal Singh, and Aurelien Lucchi and was published at NeurIPS 2022.

### Main Findings

The research shows that stacking self-attention layers—the distinctive architectural component of Transformers—can result in rank collapse of the tokens' representations at initialization.

The authors demonstrate that rank collapse of the tokens' representations hinders training by causing the gradients of the queries and keys to vanish at initialization.

### Solutions Proposed

The paper provides a thorough description of the origin of rank collapse and discusses how to prevent it via an appropriate depth-dependent scaling of the residual branches.

The research addresses a critical theoretical understanding of why Transformers face optimization challenges when they are made deeper, and offers practical architectural modifications to mitigate these issues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "4f86a291-442b-467e-bc27-ccf6420e9cd9"
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-15T16:02:28.214Z_

<details><summary>↩ Tool result · `toolu_012Qwhr892xTGfipiU9WyEzV`</summary>

```text
Web search results for query: "Dong "attention entropy collapse" transformers "rank collapse" residual connections layer normalization 2023 2024"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=utSqpxQHXq"},{"title":"Rank Collapse in Self-Attention Models","url":"https://www.emergentmind.com/topics/rank-collapse-in-self-attention"},{"title":"[2303.06296] Stabilizing Transformer Training by Preventing Attention Entropy Collapse","url":"https://arxiv.org/abs/2303.06296"},{"title":"STABILIZING TRANSFORMER TRAINING BY PREVENTING ATTENTION ENTROPY COLLAPSE","url":"https://arxiv.org/pdf/2303.06296"},{"title":"Stabilizing Transformer Training by Preventing Attention Entropy Collapse","url":"https://proceedings.mlr.press/v202/zhai23a/zhai23a.pdf"},{"title":"Rank, Head-Channel Non-Identifiability, and Symmetry Breaking: A Precise Analysis of Representational Collapse in Transformers","url":"https://arxiv.org/html/2604.23681"},{"title":"Two failure modes of deep transformers and how to avoid them: a unified theory of signal propagation at initialisation","url":"https://arxiv.org/html/2505.24333v2"},{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/d848cb2c84f0bba7f1f73cf232734c40-Paper-Conference.pdf"},{"title":"lambda-skip connections: the architectural","url":"https://arxiv.org/pdf/2410.10609"},{"title":"Variance Sensitivity Induces Attention Entropy Collapse in Transformers","url":"https://aclanthology.org/2025.emnlp-main.421.pdf"}]

Based on the search results, I've found relevant academic work on the topics you're interested in. Here's a summary of what the research shows:

## Key Findings

Rank collapse is a phenomenon where self-attention maps all input tokens to identical representations, producing an output matrix of rank one. Dong et al. (2021) demonstrated that networks composed solely of self-attention layers will inevitably collapse.

Entropy collapse refers to pathologically low attention entropy, corresponding to highly concentrated attention scores. Low attention entropy is accompanied by high training instability, which can take the form of oscillating loss or divergence.

## Recent Theoretical Work

A unified theoretical framework provides a unified explanation for – and a practical solution to – the emergence of both failure modes observed in practice: rank collapse and entropy collapse. This recent work (2025) analyzes signal propagation in deep transformers with self-attention layers, skip connections, layer normalization, and MLPs.

## Role of Architectural Components

Layer normalization is precisely affine-rank-neutral: it preserves the affine rank of the token representation set exactly, and neither contributes to nor mitigates rank collapse.

Residual connections generically obstruct rank collapse in real Transformer architectures.

A solution called σReparam reparametrizes all linear layers with spectral normalization and an additional learned scalar, successfully preventing entropy collapse in the attention layers and promoting more stable training.

The research spans from 2021 (Dong et al.'s initial work on rank collapse) through 2024-2025, with ongoing work focusing on understanding the interplay between these failure modes and how architectural choices affect signal propagation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "f0881493-4aa4-48c1-8f43-1ab9f624996b"
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-15T16:02:30.288Z_

<details><summary>↩ Tool result · `toolu_01Tj34CwWgM55Xn6hK6AWK5r`</summary>

```text
Web search results for query: "Buurmeijer VLA 2025 2026 probing robot vision language action representation"

Links: [{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"[2510.07077] Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications","url":"https://arxiv.org/abs/2510.07077"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"GitHub - Psi-Robot/Awesome-VLA-Papers: Paper list in the survey: A Survey on Vision-Language-Action Models: An Action Tokenization Perspective · GitHub","url":"https://github.com/Psi-Robot/Awesome-VLA-Papers"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications","url":"https://vla-survey.github.io/"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Vision-language-action models are the next leap in autonomous robotics - The Robot Report","url":"https://www.therobotreport.com/vision-language-action-models-are-the-next-leap-in-autonomous-robotics/"}]

I found several comprehensive resources related to Vision-Language-Action (VLA) models for robotics. While my search didn't return results specifically about a researcher named "Buurmeijer," here are the key findings related to VLA research and representation in 2025-2026:

## Recent VLA Research and Publications

A systematic review published in May 2026 provides a unified taxonomy that organizes more than 100 VLA architectures and maps 26 major VLA datasets. There was a comprehensive analysis of 164 Vision-Language-Action model submissions at ICLR 2026, discovering trends in discrete diffusion VLAs, reasoning models, and benchmarks like LIBERO, CALVIN, and SIMPLER.

## Key VLA Research Focus Areas

VLA models aim to learn policies that generalize across diverse tasks, objects, embodiments, and environments by unifying vision, language, and action data at scale. Vision Language Action models represent a new frontier in robotics by unifying perception, reasoning, and control within a single multimodal learning framework, integrating visual, linguistic, and action modalities for instruction-driven manipulation and generalist autonomy.

## Architecture Developments

Leading VLA systems such as RT-2, OpenVLA, CLIP-RT, Octo, and RT-1 employ transformer-based vision and language backbones fused through cross-modal attention. Diffusion-based decoders demonstrate superior cross-domain transfer and robustness compared to autoregressive heads, and hierarchical fusion significantly improves manipulation success.

If you're looking for more specific information about a particular researcher or paper, you might want to search academic databases like arXiv or Google Scholar directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "1cc94557-8c57-4ff2-93c8-a3831f05a34b"
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-15T16:02:30.740Z_

<details><summary>↩ Tool result · `toolu_0111JFDAknfvDGsKFW7sdbYY`</summary>

```text
Web search results for query: "RT-2 Brohan 2023 vision language action model robotic transformer PaLM-E internal representations"

Links: [{"title":"RT-2: Vision-Language-Action Models","url":"https://robotics-transformer2.github.io/"},{"title":"[2307.15818] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://arxiv.org/abs/2307.15818"},{"title":"RT-2: New model translates vision and language into action — Google DeepMind","url":"https://deepmind.google/blog/rt-2-new-model-translates-vision-and-language-into-action/"},{"title":"(PDF) RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://www.researchgate.net/publication/372784419_RT-2_Vision-Language-Action_Models_Transfer_Web_Knowledge_to_Robotic_Control"},{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | by Faryal Saud | Medium","url":"https://medium.com/@faryal.saud/rt-2-vision-language-action-models-transfer-web-knowledge-to-robotic-control-8cffbd038781"},{"title":"GitHub - kyegomez/RT-2: Democratization of RT-2 \"RT-2: New model translates vision and language into action\" · GitHub","url":"https://github.com/kyegomez/RT-2"},{"title":"RT-2: Vision-Language-Action Models Transfer Web ...","url":"https://arxiv.org/pdf/2307.15818"},{"title":"RT-2: Vision-Language-Action Transformer","url":"https://www.emergentmind.com/topics/rt-2-model"},{"title":"RT-2: VLA Models","url":"https://www.eulerfold.com/research-decoded/rt-2-vision-language-action"},{"title":"Vision-Language-Action Models Transfer Web Knowledge ...","url":"https://robotics-transformer2.github.io/assets/rt2.pdf"}]

Based on the web search results, here's comprehensive information about RT-2:

## Overview

RT-2 is a novel vision-language-action (VLA) model that learns from both web and robotics data, and translates this knowledge into generalised instructions for robotic control. The model was authored by Anthony Brohan and 53 other co-authors, and the paper was published on July 28, 2023.

## Core Architecture and Approach

RT-2 represents robot actions as another language, which can be cast into text tokens and trained together with Internet-scale vision-language datasets. To fit both natural language responses and robotic actions into the same format, the model expresses actions as text tokens and incorporates them directly into the training set of the model in the same way as natural language tokens.

## Vision-Language Models Used

RT-2 has two instantiations of VLAs based on PaLM-E and PaLI-X. RT-2 builds upon state-of-the-art vision–LLMs, notably the PaLI-X encoder–decoder (with up to 55B parameters) and PaLM-E (decoder-only, up to 12B parameters).

## Key Capabilities and Emergent Properties

Extensive evaluation showing 6k evaluation trials demonstrates performant robotic policies and enables RT-2 to obtain emergent capabilities from Internet-scale training, including significantly improved generalization to novel objects and the ability to interpret commands not present in the robot training data. Incorporating chain-of-thought reasoning allows RT-2 to perform multi-stage semantic reasoning, like deciding which object could be used as an improvised hammer (a rock), or which type of drink is best for a tired person (an energy drink).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "3552a7e3-4aac-400c-a544-f983b0ff6138"
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-15T16:02:31.038Z_

<details><summary>↩ Tool result · `toolu_01GTAXu4k1w24NXjZ5oAVRJa`</summary>

```text
Web search results for query: "Zou et al 2023 "Representation Engineering" paper authors venue findings"

Links: [{"title":"[2310.01405] Representation Engineering: A Top-Down Approach to AI Transparency","url":"https://arxiv.org/abs/2310.01405"},{"title":"GitHub - andyzoujm/representation-engineering: Representation Engineering: A Top-Down Approach to AI Transparency · GitHub","url":"https://github.com/andyzoujm/representation-engineering"},{"title":"Representation Engineering for Large-Language Models: Survey and Research Challenges","url":"https://arxiv.org/html/2502.17601v1"},{"title":"GitHub - chrisliu298/awesome-representation-engineering: A resource repository for representation engineering in large language models · GitHub","url":"https://github.com/chrisliu298/awesome-representation-engineering"},{"title":"Turning Knobs Inside LLMs: A Review of Representation Engineering — A Top-Down Approach to AI Transparency (2023) | by GlitchQ | Glitch Q | Medium","url":"https://medium.com/glitch-q/turning-knobs-inside-llms-a-review-of-representation-engineering-a-top-down-approach-to-ai-f850a0be7ad5"},{"title":"dblp: Representation Engineering: A Top-Down Approach to AI Transparency.","url":"https://dblp.org/rec/journals/corr/abs-2310-01405.html"},{"title":"Representation Engineering: A Top-Down Approach to AI Transparency | Montreal AI Ethics Institute","url":"https://montrealethics.ai/representation-engineering-a-top-down-approach-to-ai-transparency/"},{"title":"Representation Engineering — AI Safety 東京","url":"https://aisafety.tokyo/benkyoukai/representation-engineering"},{"title":"[PDF] Representation Engineering: A Top-Down Approach to AI Transparency | Semantic Scholar","url":"https://www.semanticscholar.org/paper/58fdf550600fc3873729d466601c5d08a51ba8a0"},{"title":"[2401.16332] Tradeoffs Between Alignment and Helpfulness in Language Models with Steering Methods","url":"https://arxiv.org/abs/2401.16332"}]

Based on the search results, here's comprehensive information about the Zou et al. 2023 "Representation Engineering" paper:

## Paper Details

**Title:** Representation Engineering: A Top-Down Approach to AI Transparency

**Authors:** Andy Zou, Long Phan, Sarah Chen, James Campbell, Phillip Guo, Richard Ren, Alexander Pan, Xuwang Yin, Mantas Mazeika, Ann-Kathrin Dombrowski, Shashwat Goel, Nathaniel Li, Michael J. Byun, Zifan Wang, Alex Mallen, Steven Basart, Sanmi Koyejo, Dawn Song, Matt Fredrikson, J. Zico Kolter, Dan Hendrycks

**Venue:** arXiv (published October 2, 2023)

## Key Findings

The paper identifies and characterizes representation engineering (RepE), an approach to enhancing the transparency of AI systems that draws on insights from cognitive neuroscience. RepE places population-level representations, rather than neurons or circuits, at the center of analysis, equipping researchers with novel methods for monitoring and manipulating high-level cognitive phenomena in deep neural networks.

The authors provide baselines and an initial analysis of RepE techniques, showing that they offer simple yet effective solutions for improving understanding and control of large language models. The methods can provide traction on a wide range of safety-relevant problems, including honesty, harmlessness, power-seeking, and more.

**Technical Approach:** The paper proposes Linear Artificial Tomography (LAT) as a baseline for representation reading. For representation control, it proposes three different baselines: Reading Vector, Contrast Vector, and Low-Rank Representation Adaptation (LoRRA).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "17f32452-6b73-4548-9620-9f7774645eb6"
}
```

</details>

---

### System

_source line 124_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for Dong 2021 \"Attention is not all you need\" rank co…",
  "usage": {
    "total_tokens": 40764,
    "tool_uses": 26,
    "duration_ms": 75456
  },
  "last_tool_name": "WebSearch",
  "uuid": "28163365-2e28-4f53-8dd5-4e91f25030a1",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 125_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0149mB9vSdXJy1JU4XgoEBbs`</summary>

```json
{
  "query": "Dong 2021 \"Attention is not all you need\" rank collapse pure self-attention NeurIPS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "fddd40a3-6122-4fb4-8be0-de1918443ea2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QdLh1rxk3GZYd1RpmofrCA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6244,
      "cache_read_input_tokens": 34185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6244,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

### System

_source line 126_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for Zhai 2023 \"Stabilizing Transformer Training Preve…",
  "usage": {
    "total_tokens": 40809,
    "tool_uses": 27,
    "duration_ms": 76397
  },
  "last_tool_name": "WebSearch",
  "uuid": "c977a1c1-71e0-4da7-959b-ae9c6b7654d4",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 127_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0141cDL1hZfZrAs7mDKRc2wB`</summary>

```json
{
  "query": "Zhai 2023 \"Stabilizing Transformer Training Preventing Attention Entropy Collapse\" ICML authors sigma reparam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "111b2077-450e-4380-baeb-26c3e203ad57",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QdLh1rxk3GZYd1RpmofrCA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6244,
      "cache_read_input_tokens": 34185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6244,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

### System

_source line 128_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for \"Observing and Controlling Features Vision-Langua…",
  "usage": {
    "total_tokens": 40854,
    "tool_uses": 28,
    "duration_ms": 77333
  },
  "last_tool_name": "WebSearch",
  "uuid": "a35a6fc1-73b7-4992-82e1-d51785790f88",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 129_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KHLtpMRzQb4a34SpW4Aofu`</summary>

```json
{
  "query": "\"Observing and Controlling Features Vision-Language-Action Models\" 2026 arxiv sparse autoencoder"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "7a3dcf0c-ff19-4bed-9acc-144b5437428f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QdLh1rxk3GZYd1RpmofrCA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6244,
      "cache_read_input_tokens": 34185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6244,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

### System

_source line 130_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for \"what does VLA learn\" \"what does fine-tuning chan…",
  "usage": {
    "total_tokens": 40899,
    "tool_uses": 29,
    "duration_ms": 77924
  },
  "last_tool_name": "WebSearch",
  "uuid": "e1c42a70-65b1-4ad6-aab8-fb80a05c69b4",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 131_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016xDpo8s1LWu2FEzXBbkr8W`</summary>

```json
{
  "query": "\"what does VLA learn\" \"what does fine-tuning change\" VLA backbone probing internal analysis 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "e0a8ac51-a85e-4944-a503-ddb88c4ef95a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QdLh1rxk3GZYd1RpmofrCA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6244,
      "cache_read_input_tokens": 34185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6244,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

### System

_source line 132_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for fine-tuning creates uniform stable representation…",
  "usage": {
    "total_tokens": 22247,
    "tool_uses": 8,
    "duration_ms": 70178
  },
  "last_tool_name": "WebSearch",
  "uuid": "c37edb68-2882-4c1b-906b-40cfaabc0c47",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 133_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GLinAujuZujr1nGzQKpAum`</summary>

```json
{
  "query": "fine-tuning creates uniform stable representations LoRA full fine-tuning internal representation change LLM 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "9f86169d-94ef-4edf-84ac-a8d08fc2612b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D2NjKUiUMchbNNQ96PyeG4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1057,
      "cache_read_input_tokens": 20919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1057,
        "ephemeral_1h_input_tokens": 0
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

_source line 134 · 2026-05-15T16:02:38.461Z_

<details><summary>↩ Tool result · `toolu_0149mB9vSdXJy1JU4XgoEBbs`</summary>

```text
Web search results for query: "Dong 2021 "Attention is not all you need" rank collapse pure self-attention NeurIPS"

Links: [{"title":"[2103.03404] Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth","url":"https://arxiv.org/abs/2103.03404"},{"title":"[Quick Review] Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth","url":"https://liner.com/review/attention-is-not-all-you-need-pure-attention-loses-rank"},{"title":"[PDF] Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Attention-is-Not-All-You-Need:-Pure-Attention-Loses-Dong-Cordonnier/dfb37e6216e792bf6bd5a30c0fc7ad55df1cb71e"},{"title":"GitHub - twistedcubic/attention-rank-collapse: [ICML 2021 Oral] We show pure attention suffers rank collapse, and how different mechanisms combat it. · GitHub","url":"https://github.com/twistedcubic/attention-rank-collapse"},{"title":"(PDF) Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth","url":"https://www.researchgate.net/publication/349880007_Attention_is_Not_All_You_Need_Pure_Attention_Loses_Rank_Doubly_Exponentially_with_Depth"},{"title":"Attention is not all you need: pure attention loses rank doubly exponentially with depth","url":"https://proceedings.mlr.press/v139/dong21a.html"},{"title":"Attention is not all you need:","url":"https://arxiv.org/pdf/2103.03404"},{"title":"[2103.03404v1] Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth","url":"https://arxiv.org/abs/2103.03404v1"},{"title":"Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210303404D/abstract"},{"title":"[2103.03404v2] Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth","url":"https://arxiv.org/abs/2103.03404v2"}]

Based on the search results, here's what I found about the paper:

## Paper Details

The paper "Attention is not all you need: pure attention loses rank doubly exponentially with depth" was published by Dong, Cordonnier, and Loukas in 2021 in the Proceedings of the 38th International Conference on Machine Learning. (Note: The paper was published at ICML 2021, not NeurIPS as mentioned in your search query.)

## Key Findings

The work proposes a new way to understand self-attention networks by showing that their output can be decomposed into a sum of smaller terms—or paths—each involving the operation of a sequence of attention heads across layers, and proves that self-attention possesses a strong inductive bias towards "token uniformity".

Specifically, without skip connections or multi-layer perceptrons (MLPs), the output converges doubly exponentially to a rank-1 matrix. On the other hand, skip connections and MLPs stop the output from degeneration.

## Main Contributions

The research presents a systematic study identifying the opposing impacts of self-attention versus skip connections and MLPs on rank collapse in transformers, revealing a previously unknown vital effect of skip connections.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "1ef4f9e5-ef88-4809-af8c-cf3dd6f8729e"
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-15T16:02:41.433Z_

<details><summary>↩ Tool result · `toolu_0141cDL1hZfZrAs7mDKRc2wB`</summary>

```text
Web search results for query: "Zhai 2023 "Stabilizing Transformer Training Preventing Attention Entropy Collapse" ICML authors sigma reparam"

Links: [{"title":"Stabilizing Transformer Training by Preventing Attention Entropy Collapse - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/stabilizing-transformer-training"},{"title":"Stabilizing Transformer Training by Preventing Attention Entropy Collapse","url":"https://proceedings.mlr.press/v202/zhai23a/zhai23a.pdf"},{"title":"Stabilizing transformer training by preventing attention entropy collapse | Proceedings of the 40th International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3618408.3620117"},{"title":"GitHub - apple/ml-sigma-reparam · GitHub","url":"https://github.com/apple/ml-sigma-reparam"},{"title":"ICML Poster Stabilizing Transformer Training by Preventing Attention Entropy Collapse","url":"https://icml.cc/virtual/2023/poster/24935"},{"title":"Stabilizing Transformer Training by Preventing Attention Entropy Collapse | OpenReview","url":"https://openreview.net/forum?id=LL8gz8FHxH"},{"title":"[2303.06296] Stabilizing Transformer Training by Preventing Attention Entropy Collapse","url":"https://arxiv.org/abs/2303.06296"},{"title":"[PDF] Stabilizing Transformer Training by Preventing Attention Entropy Collapse | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Stabilizing-Transformer-Training-by-Preventing-Zhai-Likhomanenko/2be8df3ffdb0095bc18acb5e3f189736ba93e308"},{"title":"Methods of improving LLM training stability","url":"https://arxiv.org/html/2410.16682v1"},{"title":"Stabilizing Transformer Training by Preventing Attention Entropy Collapse - researchr publication references","url":"https://researchr.org/publication/ZhaiLLBR0GS23/references"}]

Based on the search results, I found the paper you're looking for. Here are the key details:

## Paper Information

**Title:** "Stabilizing Transformer Training by Preventing Attention Entropy Collapse"
**Authors:** Shuangfei Zhai, Tatiana Likhomanenko, Etai Littwin, Dan Busbridge, Jason Ramapuram, Yizhe Zhang, Jiatao Gu, and Joshua M. Susskind
**Conference:** International Conference on Machine Learning (ICML)
**Year:** 2023
**Pages:** 40770-40803

## Main Contribution

The paper tracks the attention entropy for each attention head during the course of training, which is a proxy for model sharpness. The authors identify a common pattern across different architectures and tasks, where low attention entropy is accompanied by high training instability, which can take the form of oscillating loss or divergence.

## The σReparam Solution

As a remedy, the authors propose σReparam, a simple and efficient solution where they reparametrize all linear layers with spectral normalization and an additional learned scalar. 

The authors conduct experiments with σReparam on image classification, image self-supervised learning, machine translation, speech recognition, and language modeling tasks, demonstrating that σReparam provides stability and robustness with respect to the choice of hyperparameters.

Code is available at https://github.com/apple/ml-sigma-reparam.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "a36c7eb3-6402-4a3c-a001-ab8d450d2796"
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-15T16:02:43.693Z_

<details><summary>↩ Tool result · `toolu_01GLinAujuZujr1nGzQKpAum`</summary>

```text
Web search results for query: "fine-tuning creates uniform stable representations LoRA full fine-tuning internal representation change LLM 2023 2024"

Links: [{"title":"Efficient Fine-Tuning with LoRA: A Guide to Optimal Parameter Selection for Large Language Models","url":"https://www.databricks.com/blog/efficient-fine-tuning-lora-guide-llms"},{"title":"LoRA vs Full Fine-tuning: An Illusion of Equivalence","url":"https://arxiv.org/html/2410.21228v1"},{"title":"[2410.21228] LoRA vs Full Fine-tuning: An Illusion of Equivalence","url":"https://arxiv.org/abs/2410.21228"},{"title":"Fine-tuning (deep learning) - Wikipedia","url":"https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)"},{"title":"Fine-Tuning LLMs: In-Depth Analysis with LLAMA-2 | Anyscale","url":"https://www.anyscale.com/blog/fine-tuning-llms-lora-or-full-parameter-an-in-depth-analysis-with-llama-2"},{"title":"A beginners guide to fine tuning LLM using LoRA","url":"https://zohaib.me/a-beginners-guide-to-fine-tuning-llm-using-lora/"},{"title":"Parameter-Efficient Fine-Tuning with LoRA Using Custom Data | DigitalOcean","url":"https://www.digitalocean.com/community/tutorials/fine-tune-llms-with-lora-for-custom-domains"},{"title":"Using LoRA for Efficient Stable Diffusion Fine-Tuning","url":"https://huggingface.co/blog/lora"},{"title":"RDP LoRA: Geometry-Driven Identification for Parameter-Efficient Adaptation in Large Language Models","url":"https://arxiv.org/html/2604.19321v1"},{"title":"LoRA · Hugging Face","url":"https://huggingface.co/docs/peft/main/conceptual_guides/lora"}]

Based on the search results, here's what I found about fine-tuning, uniform stable representations, and the comparison between LoRA and full fine-tuning in LLMs:

## Key Findings on Internal Representation Changes

Recent research analyzes how LoRA and full fine-tuning change pre-trained models through their weight matrices' spectral properties, finding that LoRA and full fine-tuning yield weight matrices with very different structures: weight matrices trained with LoRA have new, high-ranking singular vectors called "intruder dimensions," while those trained with full fine-tuning do not.

## Differences Between LoRA and Full Fine-Tuning

Full fine-tuning retains most of the pre-training structure; the diagonal shift in LoRA corresponds to the introduction of intruder dimensions. This suggests that full fine-tuning maintains more uniform representations compared to LoRA's approach.

Low Rank Adaptation has outperformed full fine-tuning in some cases, as a consequence of avoiding catastrophic forgetting.

## Performance Comparison

LoRA matches full fine-tuning performance for tasks like sequence classification, instruction tuning, and chat. However, there is a gap in the performance of full fine-tuning and LoRA on harder tasks like code generation.

The research from 2024 suggests that while both methods achieve similar task performance under certain conditions, they fundamentally change model representations differently, with full fine-tuning producing more uniform changes to the model's internal structure compared to LoRA's introduction of new singular vector dimensions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "fb4d4b1e-b501-487a-959b-43379a813a89"
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-15T16:02:43.991Z_

<details><summary>↩ Tool result · `toolu_01KHLtpMRzQb4a34SpW4Aofu`</summary>

```text
Web search results for query: ""Observing and Controlling Features Vision-Language-Action Models" 2026 arxiv sparse autoencoder"

Links: [{"title":"Observing and Controlling Features in Vision-Language-Action Models","url":"https://arxiv.org/html/2603.05487v1"},{"title":"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models","url":"https://arxiv.org/html/2603.19183v1"},{"title":"[2603.05487] Observing and Controlling Features in Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.05487"},{"title":"Sparse Autoencoders for Scientifically Rigorous Interpretation of Vision Models","url":"https://arxiv.org/html/2502.06755v1"},{"title":"[2603.19183] Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models","url":"https://arxiv.org/abs/2603.19183"},{"title":"Probing the Representational Power of Sparse Autoencoders in Vision Models","url":"https://arxiv.org/html/2508.11277v1"},{"title":"Interpretable and Testable Vision Features via Sparse Autoencoders","url":"https://arxiv.org/html/2502.06755v2"},{"title":"[2502.06755v1] Sparse Autoencoders for Scientifically Rigorous Interpretation of Vision Models","url":"https://arxiv.org/abs/2502.06755v1"},{"title":"[2502.06755] Interpretable and Testable Vision Features via Sparse Autoencoders","url":"https://arxiv.org/abs/2502.06755"},{"title":"Sparse Autoencoders for Vision","url":"https://osu-nlp-group.github.io/saev/"}]

I found several highly relevant papers from your search. Here are the key results:

## Main Paper

"Observing and Controlling Features in Vision-Language-Action Models" proposes feature-observability and feature-controllability concepts. The work studies features that are linearly encoded in representation space and shows how they can be observed by means of a linear classifier. It then uses a minimal linear intervention grounded in optimal control to accurately place internal representations and steer the VLA's output towards a desired region.

## Related Work on Sparse Autoencoders for VLAs

"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models" collects internal activations from a VLA, trains a Sparse Autoencoder (SAE), and obtains sparse features that represent both memorized episodes as well as general semantic concepts, motion primitives and task structure. They train sparse autoencoders on residual stream activations to obtain sparse, human-interpretable features. Across two VLA architectures and two robotics datasets, many SAE features exhibit clear interpretations as motion primitives, task-progress signals, semantic representations, and episode-specific memorization.

Individual SAE directions causally influence closed-loop behavior. When steering general features, they often observe modifications to motion consistent with their hypothesized interpretation. For example, steering a pre-grasp alignment feature causes the policy to hover above objects instead of continue grasping.

The first paper notes that future work could explore self-supervised or unsupervised methods for feature discovery, such as leveraging Sparse Autoencoders (SAEs) to identify interpretable features without explicit labels.

Both papers were published on arXiv in March 2026 and represent important advances in mechanistic interpretability for vision-language-action models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "87123c80-b631-4550-a673-56ede8256933"
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-15T16:02:44.399Z_

<details><summary>↩ Tool result · `toolu_016xDpo8s1LWu2FEzXBbkr8W`</summary>

```text
Web search results for query: ""what does VLA learn" "what does fine-tuning change" VLA backbone probing internal analysis 2025 2026"

Links: [{"title":"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts","url":"https://arxiv.org/html/2605.06175v1"},{"title":"What Can RL Bring to VLA Generalization? An Empirical Study","url":"https://arxiv.org/html/2505.19789v4"},{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview","url":"https://openreview.net/forum?id=eUGoqrZ6Ea"},{"title":"Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control","url":"https://arxiv.org/html/2512.11921v1"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Visual-Language-Action+(VLA)+models"},{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2601.06748v1"},{"title":"2026-01-28 Work in progress.","url":"https://arxiv.org/pdf/2601.15197"},{"title":"Don’t Blind Your VLA: Aligning Visual Representations for OOD Generalization","url":"https://blind-vla-paper.github.io/"}]

I found several recent research papers on VLA (Vision-Language-Action) models and their internal mechanisms during fine-tuning. Here are the key findings:

## What Fine-Tuning Changes in VLAs

End-to-end robotic fine-tuning may overwrite core spatial representations required for visual generalization. More specifically, full fine-tuning often overfits limited robotic data and degrades pre-trained vision-language competence through catastrophic forgetting.

Fine-tuning often causes overfitting and degradation of visual–language representations. Research shows that fine-tuning on narrow, task-specific datasets can lead to catastrophic forgetting of the VLM's general capabilities and VLA models often learn a vision-only policy rather than a true language-conditioned policy.

## VLA Backbone Probing and Internal Analysis

Recent mechanistic interpretability studies have revealed insights about what VLAs learn internally. Experimental probing of OpenVLA's LLM backbone reveals robust internal encoding of symbolic states (object relations, action status) with >>0.90 accuracy in decoding symbolic predicates, indicating that high-level environmental structures are accessible from activation vectors.

Mechanistic interpretability analyses show that specific transformer neurons correspond to semantic directions (e.g., "fast", "up"), and activation steering can causally modulate robot behavior at inference time, yielding real-time behavioral control without retraining.

## Solutions to Preserve Knowledge

Researchers have proposed several approaches to mitigate representation drift:

Post hoc restoration involves partially reverting the visual encoders back to their pretrained states through backbone reversal and model merging. Additionally, Parameter-efficient fine-tuning (PEFT), such as low-rank adaptation (LoRA), is more stable in preserving pre-trained capability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "b0dd1343-a7ea-48dd-9701-cd3e0c96ee82"
}
```

</details>

---

### System

_source line 139_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for anisotropy transformer representations training r…",
  "usage": {
    "total_tokens": 23371,
    "tool_uses": 9,
    "duration_ms": 79981
  },
  "last_tool_name": "WebSearch",
  "uuid": "b9b3893b-85ca-43be-ae61-ac42d80414bf",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 140_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014CaqFK6Z9vmkHicPzUWXyi`</summary>

```json
{
  "query": "anisotropy transformer representations training reduces representation degeneration pretrained language models 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "81603747-70e9-4257-beb6-fc8aa3fd23d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016pXVCfDbQyRKXpMB1DpsHV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1088,
      "cache_read_input_tokens": 21976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1088,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 141_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for \"Echoes of BERT\" \"modern language models rediscov…",
  "usage": {
    "total_tokens": 44893,
    "tool_uses": 30,
    "duration_ms": 89695
  },
  "last_tool_name": "WebSearch",
  "uuid": "0b058fd7-b2fc-4256-b1c8-e9308cf7dadb",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 142_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HaaJbVi1Fja86rBNu8dmKJ`</summary>

```json
{
  "query": "\"Echoes of BERT\" \"modern language models rediscover classical NLP pipeline\" 2025 LLaMA GPT layer probing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "8be8f38c-f354-42cc-b190-51478066cebb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JodehF8kZNtav551t2N51j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3953,
      "cache_read_input_tokens": 40429,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3953,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 143_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "description": "Searching for \"Don't Blind Your VLA\" visual representations OOD…",
  "usage": {
    "total_tokens": 44934,
    "tool_uses": 31,
    "duration_ms": 90254
  },
  "last_tool_name": "WebSearch",
  "uuid": "990cb983-3703-4ce3-b30c-0bc9c3317da1",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 144_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GUWqdUcqfrRJ4AQUe8TAiz`</summary>

```json
{
  "query": "\"Don't Blind Your VLA\" visual representations OOD generalization fine-tuning degrades 2026 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "88af100f-6185-4ff9-b5ae-c689dffb6b44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JodehF8kZNtav551t2N51j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3953,
      "cache_read_input_tokens": 40429,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3953,
        "ephemeral_1h_input_tokens": 0
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

_source line 145 · 2026-05-15T16:02:54.466Z_

<details><summary>↩ Tool result · `toolu_01HaaJbVi1Fja86rBNu8dmKJ`</summary>

```text
Web search results for query: ""Echoes of BERT" "modern language models rediscover classical NLP pipeline" 2025 LLaMA GPT layer probing"

Links: [{"title":"Echoes of BERT: Do Modern Language Models Rediscover the Classical NLP Pipeline?","url":"https://arxiv.org/html/2506.02132v4"},{"title":"Echoes of BERT: Do Modern Language Models Rediscover the Classical NLP Pipeline? | OpenReview","url":"https://openreview.net/forum?id=YBt6cvPK0k"},{"title":"BERT Rediscovers the Classical NLP Pipeline - ACL Anthology","url":"https://aclanthology.org/P19-1452/"},{"title":"BERT Rediscovers the Classical NLP Pipeline | by Yamini Lakshmi Narasimhan | Medium","url":"https://yl9822.medium.com/bert-rediscovers-the-classical-nlp-pipeline-4c992287f223"},{"title":"BERT Rediscovers the Classical NLP Pipeline","url":"https://research.google/pubs/bert-rediscovers-the-classical-nlp-pipeline/"},{"title":"Does BERT Rediscover a Classical NLP Pipeline?","url":"https://www.cs.toronto.edu/~gpenn/csc485/4cGridLocGrammaticality.pdf"},{"title":"ECHOES OF BERT: DO MODERN LANGUAGE MODELS ...","url":"https://openreview.net/pdf/34adb3850a7e6e78157576f3cbca7bcb00655223.pdf"},{"title":"BERT Rediscovers the Classical NLP Pipeline | Request PDF","url":"https://www.researchgate.net/publication/333130511_BERT_Rediscovers_the_Classical_NLP_Pipeline"},{"title":"Echoes of BERT: Do Modern Language Models ...","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250602132L/abstract"},{"title":"[2506.02132] Model Internal Sleuthing: Finding Lexical Identity and Inflectional Features in Modern Language Models","url":"https://arxiv.org/abs/2506.02132"}]

I found the paper! Here are the search results for "Echoes of BERT":

## Main Finding

The paper "Echoes of BERT: Do Modern Language Models Rediscover the Classical NLP Pipeline?" analyzes 25 models spanning classical architectures (BERT, DeBERTa, GPT-2) to modern large language models (Pythia, OLMo-2, Gemma-2, Qwen2.5, Llama-3.1), probing layer-by-layer representations across eight linguistic tasks in English.

## Key Results

Consistent with earlier findings, the paper finds that hierarchical organization persists in modern models: early layers capture syntax, middle layers handle semantics and entity-level information, and later layers encode discourse phenomena.

However, larger models compress this entire hierarchy toward earlier layer positions, suggesting they build richer representations more quickly.

## Additional Analysis

The researchers found that lemma information concentrates linearly in early layers but becomes increasingly nonlinear deeper in the network, while inflectional information remains linearly accessible throughout all layers.

Overall, the results demonstrate that modern language models consistently rediscover the classical NLP pipeline observed in prior BERTology work.

The paper was published in October 2025 and employs layer probing techniques to understand how different linguistic properties emerge across model depths in contemporary transformer-based language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "5a0b4cad-7254-4c6b-b98d-ef0bc89ed012"
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-15T16:02:54.623Z_

<details><summary>↩ Tool result · `toolu_014CaqFK6Z9vmkHicPzUWXyi`</summary>

```text
Web search results for query: "anisotropy transformer representations training reduces representation degeneration pretrained language models 2023 2024"

Links: [{"title":"Revisiting Anisotropy in Language Transformers: The Geometry of Learning Dynamics","url":"https://arxiv.org/html/2604.08764v1"},{"title":"Anisotropy Is Inherent to Self-Attention in Transformers","url":"https://aclanthology.org/2024.eacl-long.3.pdf"},{"title":"The Shape of Learning: Anisotropy and Intrinsic Dimensions in Transformer-Based Models - ACL Anthology","url":"https://aclanthology.org/2024.findings-eacl.58/"},{"title":"The Shape of Learning: Anisotropy and Intrinsic Dimensions in Transformer-Based Models","url":"https://arxiv.org/html/2311.05928v2"},{"title":"[2604.08764] Revisiting Anisotropy in Language Transformers: The Geometry of Learning Dynamics","url":"https://arxiv.org/abs/2604.08764"},{"title":"Anisotropy Is Inherent to Self-Attention in Transformers","url":"https://arxiv.org/html/2401.12143v2"},{"title":"Anisotropy and Intrinsic Dimensions in Transformer-Based ...","url":"https://aclanthology.org/2024.findings-eacl.58.pdf"},{"title":"Is Anisotropy Inherent to Transformers?","url":"https://arxiv.org/html/2306.07656v1"},{"title":"Mitigating Frequency Bias and Anisotropy in Language Model","url":"https://arxiv.org/pdf/2410.11462"},{"title":"[2311.05928] The Shape of Learning: Anisotropy and Intrinsic Dimensions in Transformer-Based Models","url":"https://arxiv.org/abs/2311.05928"}]

I've successfully performed the web search for your query about anisotropy in transformer representations, training, and representation degeneration in pretrained language models from 2023-2024. Here are the key results:

## Main Research Areas Found:

**1. Representation Degeneration and Anisotropy**

Representations produced by Transformer language models are often anisotropic, with token embeddings concentrating in a narrow cone and exhibiting high pairwise cosine similarity even for unrelated content. Anisotropy has been linked to training and modeling details, including likelihood maximization with weight tying and the induced "representation degeneration" of embeddings.

**2. Causes and Contributing Factors**

Degeneration phenomena are tied to rare-token dynamics, where rare-token gradients can drive global embedding drift and degrade representational quality. Frequency leaves systematic geometric signatures in contextualized embeddings, distorting similarity geometry and affecting identifiability.

**3. Architecture-Specific Patterns (2024 Research)**

The anisotropy profile in transformer decoders exhibits a distinct bell-shaped curve with highest anisotropy concentrations in middle layers, which diverges from the more uniformly distributed anisotropy observed in encoders. The intrinsic dimension of embeddings increases during initial training phases, followed by a compression phase towards training's end.

**4. Emerging Theoretical Perspectives (2024)**

Geometric arguments explain how frequency-biased sampling attenuates curvature visibility and why training preferentially amplifies tangent directions, with activation-derived directions capturing substantially larger shares of gradient anisotropy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "25038f26-f0ed-4e98-8dcd-dea374c852f5"
}
```

</details>

---

### Tool result

_source line 147 · 2026-05-15T16:02:54.654Z_

<details><summary>↩ Tool result · `toolu_01GUWqdUcqfrRJ4AQUe8TAiz`</summary>

```text
Web search results for query: ""Don't Blind Your VLA" visual representations OOD generalization fine-tuning degrades 2026 authors"

Links: [{"title":"[2510.25616] Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization","url":"https://arxiv.org/abs/2510.25616"},{"title":"Don’t Blind Your VLA: Aligning Visual Representations for OOD Generalization","url":"https://blind-vla-paper.github.io/"},{"title":"Don’t Blind Your VLA: Aligning Visual Representations for OOD Generalization","url":"https://arxiv.org/html/2510.25616v1"},{"title":"GitHub - CognitiveAISystems/BlindVLA: Official implementation of Don’t Blind Your VLA: Aligning Visual Representations for OOD Generalization. https://blind-vla-paper.github.io","url":"https://github.com/CognitiveAISystems/BlindVLA"},{"title":"[2510.25616v1] Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization","url":"https://arxiv.org/abs/2510.25616v1"},{"title":"Paper page - Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization","url":"https://huggingface.co/papers/2510.25616"},{"title":"Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.25616v1"},{"title":"Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization [Quick Review]","url":"https://liner.com/review/dont-blind-your-vla-aligning-visual-representations-for-ood-generalization"},{"title":"[Literature Review] Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization","url":"https://www.themoonlight.io/en/review/dont-blind-your-vla-aligning-visual-representations-for-ood-generalization"},{"title":"Don't Blind Your VLA: Aligning Visual Representations for ...","url":"https://www.researchgate.net/publication/397041439_Don't_Blind_Your_VLA_Aligning_Visual_Representations_for_OOD_Generalization"}]

Based on the search results, here's information about the paper "Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization":

## Paper Overview

The paper conducts a systematic study of representation retention during VLA fine-tuning, showing that naive action fine-tuning leads to degradation of visual representations.

## Authors

The authors are Nikita Kachaev, Mikhail Kolosov, Daniil Zelezetsky, Alexey K. Kovalev, and Aleksandr I. Panov.

## Key Findings

The paper shows that naive VLA fine-tuning induces "representation collapse" and "attention sink," with attention maps exhibiting diffuse, noisy, and misplaced patterns that indicate a loss of visual-language grounding.

## Proposed Solution

The authors evaluate a range of strategies for aligning visual representations and introduce a simple yet effective method that mitigates degradation and yields improved generalization to out-of-distribution (OOD) scenarios. Extensive experiments demonstrate that this alignment consistently improves out-of-distribution generalization – yielding up to a 10% relative gain over naive SFT.

## Publication

The paper was submitted on October 29, 2025 (arXiv preprint 2510.25616), with code publicly available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "370e767e-c352-43ea-a33a-93fd77beceb2"
}
```

</details>

---

### System

_source line 148_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for \"representation degeneration\" Gao 2019 pretrained…",
  "usage": {
    "total_tokens": 24368,
    "tool_uses": 10,
    "duration_ms": 90912
  },
  "last_tool_name": "WebSearch",
  "uuid": "7401a684-3182-4225-865e-38cfab45726c",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 149_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BHujaXSfbhMH8AVBjvyYjQ`</summary>

```json
{
  "query": "\"representation degeneration\" Gao 2019 pretrained language models isotropy contrastive learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "bc19ff9b-ad63-40d4-9a7d-4e330293ac7a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FPo5XR9fpyKxZGbcyQebRZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 956,
      "cache_read_input_tokens": 23064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 956,
        "ephemeral_1h_input_tokens": 0
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

_source line 150 · 2026-05-15T16:03:03.776Z_

<details><summary>↩ Tool result · `toolu_01BHujaXSfbhMH8AVBjvyYjQ`</summary>

```text
Web search results for query: ""representation degeneration" Gao 2019 pretrained language models isotropy contrastive learning"

Links: [{"title":"[2205.07208] Fine-tuning Pre-trained Language Models for Few-shot Intent Detection: Supervised Pre-training and Isotropization","url":"https://ar5iv.labs.arxiv.org/html/2205.07208"},{"title":"Representation Degeneration in ML","url":"https://www.emergentmind.com/topics/representation-degeneration-problem"},{"title":"Connecting Pre-trained Language Models and ...","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/93712c59f6a81bd92040facf04c8b308-Paper-Conference.pdf"},{"title":"(PDF) Representation Degeneration Problem in Training Natural Language Generation Models","url":"https://www.researchgate.net/publication/334759956_Representation_Degeneration_Problem_in_Training_Natural_Language_Generation_Models"},{"title":"Focused Transformer: Contrastive Training for Context Scaling","url":"https://arxiv.org/pdf/2307.03170"},{"title":"Published as a conference paper at ICLR 2019 REPRESENTATION DEGENERATION","url":"https://arxiv.org/pdf/1907.12009"},{"title":"[2210.14140] Contrastive Search Is What You Need For Neural Text Generation","url":"https://ar5iv.labs.arxiv.org/html/2210.14140"},{"title":"(PDF) On Isotropy and Learning Dynamics of Contrastive-based Sentence Representation Learning","url":"https://www.researchgate.net/publication/366423291_On_Isotropy_and_Learning_Dynamics_of_Contrastive-based_Sentence_Representation_Learning"},{"title":"Contrastive Learning Models for Sentence Representations | ACM Transactions on Intelligent Systems and Technology","url":"https://dl.acm.org/doi/10.1145/3593590"},{"title":"Revisiting Representation Degeneration Problem in ...","url":"https://aclanthology.org/2020.findings-emnlp.46.pdf"}]

Based on the search results, here's what I found about representation degeneration, Gao 2019, and related work on pretrained language models, isotropy, and contrastive learning:

## Key Findings

Gao et al.'s 2019 work focused on the "Representation degeneration problem in training natural language generation models" published at ICLR 2019.

### The Problem

Gao et al. (2019) revealed that word embeddings are not evenly distributed in high-dimensional spaces—a phenomenon known as representation degeneration. This degeneration is particularly pronounced in pretrained language models like BERT, where embeddings cluster in narrow cones within the vector space, with high-frequency words densely distributed near the origin and low-frequency words sparsely scattered further away.

### Isotropy and Performance

Studies consistently show that more isotropic (uniformly distributed) embeddings outperform anisotropic ones across various natural language understanding benchmarks (Gao et al., 2019).

### Contrastive Learning as a Solution

In translation and language modeling, isotropy metrics approach more favorable values, and BLEU/perplexity metrics improve under regularized/contrastive approaches (Lai et al., 2023, Gao et al., 2019). More specifically, contrastive learning based sentence representation models like SimCSE can ease the anisotropy problem by pushing negative pairs apart, and optimize alignment by pulling positive pairs close.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "e5421df8-b585-4d5b-a8bd-1bdb769ab47e"
}
```

</details>

---

### System

_source line 151_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for probing accuracy uniform across layers after trai…",
  "usage": {
    "total_tokens": 25381,
    "tool_uses": 11,
    "duration_ms": 99874
  },
  "last_tool_name": "WebSearch",
  "uuid": "c5de73de-9e7f-4346-ba08-e421fb1f2d4e",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 152_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cr2iV6adDuNjzeqyCAUkEq`</summary>

```json
{
  "query": "probing accuracy uniform across layers after training fine-tuning BERT transformers layer-wise probes 2022 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "3760c942-8adb-4aee-ab3e-9c0509f14548",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011cNkcW9A4unQr44f83gh9C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 975,
      "cache_read_input_tokens": 24020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 975,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 153 · 2026-05-15T16:03:13.224Z_

<details><summary>↩ Tool result · `toolu_01Cr2iV6adDuNjzeqyCAUkEq`</summary>

```text
Web search results for query: "probing accuracy uniform across layers after training fine-tuning BERT transformers layer-wise probes 2022 2023"

Links: [{"title":"Probing Layers: Where Transformers Encode Linguistic Structure - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/probing-layers"},{"title":"A Closer Look at How Fine-tuning Changes BERT Yichu Zhou School of Computing","url":"https://aclanthology.org/2022.acl-long.75.pdf"},{"title":"Layer-wise analysis of Transformer Representations","url":"https://phaneendragunda.github.io/nlp/bert/transformers/qna/2020/06/04/layerwise-analysis-of-Bert/"},{"title":"BERT Fine-Tuning Tutorial with PyTorch · Chris McCormick","url":"https://mccormickml.com/2019/07/22/BERT-fine-tuning/"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=pretrained+transformer"},{"title":"Advanced Techniques for Fine-tuning Transformers | Towards Data Science","url":"https://towardsdatascience.com/advanced-techniques-for-fine-tuning-transformers-82e4e61e16e/"},{"title":"Fine-Tuning Transformers: Techniques for Improving Model Performance | by Hassaan Idrees | Medium","url":"https://medium.com/@hassaanidrees7/fine-tuning-transformers-techniques-for-improving-model-performance-4b4353e8ba93"},{"title":"Eliciting Latent Predictions from Transformers with the Tuned Lens","url":"https://arxiv.org/pdf/2303.08112"},{"title":"What Happens To BERT Embeddings During Fine-tuning?","url":"https://aclanthology.org/2020.blackboxnlp-1.4.pdf"},{"title":"Fine-Tuning For Transformer Models","url":"https://www.meegle.com/en_us/topics/fine-tuning/fine-tuning-for-transformer-models"}]

I've completed the web search for your query about probing accuracy across layers during fine-tuning of BERT transformers. Here are the main findings from the search results:

## Key Research Findings

In BERT and similar models, lower layers (1-4) capture local, surface-level features with part-of-speech tags, morphological properties, and basic syntactic categories being most accurately predicted by probes at early layers. Middle layers (5-8) show deepened syntactic structure, with dependency parsing accuracy peaking there. Upper layers (9-12) concentrate semantic and task-specific information, with coreference resolution, named entity recognition, and sense disambiguation best predicted from final third representations.

## Fine-Tuning Effects

Fine-tuning makes the representation space simpler. Additionally, fine-tuned models retain most of the linguistic concepts discovered during unsupervised pre-training.

## Layer-Wise Consistency

BERT's transformations go through similar phases even when fine-tuned on different tasks, with information about general language properties encoded in earlier layers and implicitly used to solve downstream tasks in later layers.

The research indicates that probing accuracy is **not uniform** across layers—there's a clear hierarchical organization of linguistic and semantic information that is largely preserved even after fine-tuning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "d19288d2-55df-4990-b75b-2c39d175a164"
}
```

</details>

---

### System

_source line 154_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for probing analysis OpenVLA RT-2 Octo robot learning…",
  "usage": {
    "total_tokens": 26358,
    "tool_uses": 12,
    "duration_ms": 109693
  },
  "last_tool_name": "WebSearch",
  "uuid": "127d35ad-2d37-4a53-8f98-51b52a2dd179",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 155_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KjFhGCMLkvSKEgRMf9dNF2`</summary>

```json
{
  "query": "probing analysis OpenVLA RT-2 Octo robot learning vision language action model internal representations LLM backbone 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "98e3b68c-fd04-42cc-a417-e51d2b84206f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011sZ6QJfZoSu3jAQAYYF6zx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 937,
      "cache_read_input_tokens": 24995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 937,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
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

_source line 156 · 2026-05-15T16:03:28.442Z_

<details><summary>↩ Tool result · `toolu_01KjFhGCMLkvSKEgRMf9dNF2`</summary>

```text
Web search results for query: "probing analysis OpenVLA RT-2 Octo robot learning vision language action model internal representations LLM backbone 2024"

Links: [{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"Vision-Language-Action Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v1"},{"title":"Vision-Language-Action Models Explained: How VLAs Power Modern Robots | SVRC","url":"https://www.roboticscenter.ai/blog/vla-models-explained"},{"title":"RT-2: New model translates vision and language into action — Google DeepMind","url":"https://deepmind.google/blog/rt-2-new-model-translates-vision-and-language-into-action/"}]

I found search results on OpenVLA, RT-2, Octo, and vision-language-action models. However, I notice the search results don't contain specific information about "probing analysis" of these models' internal representations or their LLM backbones in the way your query suggests. Let me search more specifically for probing analysis and interpretability work on these models.

Links: [{"title":"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models","url":"https://arxiv.org/html/2603.19183"},{"title":"Mechanistic Interpretability for Steering Vision Language Action Models","url":"https://vla-mech-interp.github.io/"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.01166v2"},{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models","url":"https://arxiv.org/html/2509.00328v1"},{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models","url":"https://proceedings.mlr.press/v305/haon25a.html"},{"title":"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning","url":"https://arxiv.org/html/2412.03293"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"Vision-Language-Action Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v1"}]

Based on my web search, I've found relevant research on probing analysis of Vision-Language-Action (VLA) models. Here are the key findings:

## Probing VLA Internal Representations

Recent work trains Sparse Autoencoders (SAEs) on hidden layer activations of VLAs to probe internal representations, with SAEs learning a sparse dictionary whose features act as a compact, interpretable basis for the model's computation.

Linear probes trained on OpenVLA activations can decode task-relevant states such as object positions and actions, with probe accuracies exceeding >90% for most layers, suggesting that like in LLMs, VLAs often linearly encode structured information relevant to the task.

Studies indicate that OpenVLA encodes an emergent internal world model; probes reveal latent knowledge of state transitions consistent with Koopman operator theory, emerging as training progresses and scalable via Sparse Autoencoder analysis.

## LLM Backbone Analysis

Despite being trained to produce only robot actions, the internal activity of VLA models is largely semantic, with less than 25% of FFN neurons being rewired for action prediction and a large fraction of the remainder representing clear, semantically interpretable concepts.

Research identifies sparse semantic directions in transformer layers—such as speed and direction—that are causally linked to action selection, revealing semantically meaningful neurons aligned with robot control concepts like up, slow, and careful.

Mechanistic interpretability analyses show that specific transformer neurons correspond to semantic directions (e.g., "fast", "up"), and activation steering can causally modulate robot behavior at inference time.

These findings demonstrate that both OpenVLA and other VLA models like RT-2 and Octo contain interpretable internal structures within their LLM and vision-language backbones that can be probed and manipulated for understanding and controlling robot behavior.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "279e936c-c555-40b0-b487-3f191267bb06"
}
```

</details>

---

### System

_source line 157_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for \"mechanistic interpretability\" VLA vision languag…",
  "usage": {
    "total_tokens": 27864,
    "tool_uses": 13,
    "duration_ms": 124584
  },
  "last_tool_name": "WebSearch",
  "uuid": "41f9cd20-4c1b-4e5c-954b-d7f225344abc",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 158_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QBued8RNRnwYSriQDrPNXE`</summary>

```json
{
  "query": "\"mechanistic interpretability\" VLA vision language action model sparse autoencoders steering OpenVLA 2025 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "9d45992e-8670-4140-b7fb-aa4f90809e4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118PJZiDcQFBNQQnY7xdirz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1463,
      "cache_read_input_tokens": 25932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1463,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 159 · 2026-05-15T16:03:37.804Z_

<details><summary>↩ Tool result · `toolu_01QBued8RNRnwYSriQDrPNXE`</summary>

```text
Web search results for query: ""mechanistic interpretability" VLA vision language action model sparse autoencoders steering OpenVLA 2025 authors"

Links: [{"title":"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models","url":"https://arxiv.org/html/2603.19183v1"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=w8Mw9zJt1y"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"Mechanistic Interpretability for Steering Vision Language Action Models","url":"https://vla-mech-interp.github.io/"},{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models","url":"https://arxiv.org/html/2509.00328v1"},{"title":"Sparse Autoencoders Reveal Interpretable and Steerable ...","url":"https://drvla.github.io/"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/html/2603.19233v1"},{"title":"[2603.19183] Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models","url":"https://arxiv.org/abs/2603.19183"},{"title":"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.19183"},{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=YvsUD8C9QS"}]

I've found comprehensive information about mechanistic interpretability research on VLA models using sparse autoencoders and steering techniques. Here are the key findings:

## Major Research Works (2025-2026)

### 1. **Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models**

This work applies mechanistic interpretability techniques to understand VLA models by training Sparse Autoencoders (SAEs) on hidden layer activations. The research finds that the large majority of extracted SAE features correspond to memorized sequences from specific training demonstrations, though some features correspond to interpretable, general, and steerable motion primitives and semantic properties.

### 2. **Mechanistic Interpretability for Steering Vision-Language-Action Models**

This framework interprets and steers VLAs via their internal representations by projecting feedforward activations within transformer layers onto the token embedding basis, identifying sparse semantic directions such as speed and direction that are causally linked to action selection. The method is evaluated on π₀ and OpenVLA, demonstrating zero-shot behavioral control in simulation (LIBERO) and on a physical robot (UR5).

### 3. **Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models**

This cross-architecture mechanistic study applies activation injection, sparse autoencoders (SAEs), and linear probes to six models spanning 80M to 7B parameters across 394,000+ rollout episodes on four benchmarks.

## Key Technical Contributions

These works identify sparse semantic directions in VLA models and introduce activation steering methods that modulate behavior in real time, without fine-tuning, reward signals, or environment interaction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "36e91564-f2c3-4610-b701-8f176c11a0f7"
}
```

</details>

---

### System

_source line 160_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for \"LoRA vs full fine-tuning\" \"illusion of equivalen…",
  "usage": {
    "total_tokens": 28856,
    "tool_uses": 14,
    "duration_ms": 134558
  },
  "last_tool_name": "WebSearch",
  "uuid": "c4bcca61-46bd-4d81-9bd3-33b0dca0d009",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 161_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HSCWJvpDYBXynLp6Zyb79h`</summary>

```json
{
  "query": "\"LoRA vs full fine-tuning\" \"illusion of equivalence\" authors spectral intruder dimensions 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "a199c98f-4ad0-450f-ac54-55bb7ddc623b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K4ErzLHTXzze3JSUoYrSov",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 950,
      "cache_read_input_tokens": 27395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 950,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 162 · 2026-05-15T16:03:47.608Z_

<details><summary>↩ Tool result · `toolu_01HSCWJvpDYBXynLp6Zyb79h`</summary>

```text
Web search results for query: ""LoRA vs full fine-tuning" "illusion of equivalence" authors spectral intruder dimensions 2024"

Links: [{"title":"LoRA vs Full Fine-tuning: An Illusion of Equivalence","url":"https://arxiv.org/html/2410.21228v1"},{"title":"[2410.21228] LoRA vs Full Fine-tuning: An Illusion of Equivalence","url":"https://arxiv.org/abs/2410.21228"},{"title":"LoRA vs Full Fine-tuning: An Illusion of Equivalence | OpenReview","url":"https://openreview.net/forum?id=PGNdDfsI6C"},{"title":"(PDF) LoRA vs Full Fine-tuning: An Illusion of Equivalence","url":"https://www.researchgate.net/publication/385318527_LoRA_vs_Full_Fine-tuning_An_Illusion_of_Equivalence"},{"title":"Paper page - LoRA vs Full Fine-tuning: An Illusion of Equivalence","url":"https://huggingface.co/papers/2410.21228"},{"title":"NeurIPS Poster LoRA vs Full Fine-tuning: An Illusion of Equivalence","url":"https://neurips.cc/virtual/2025/poster/115207"},{"title":"llm-research-summaries/training/LoRA-vs-Full-Fine-tuning-Illusion-Equivalence_2410.21228v1.md at main · cognitivetech/llm-research-summaries","url":"https://github.com/cognitivetech/llm-research-summaries/blob/main/training/LoRA-vs-Full-Fine-tuning-Illusion-Equivalence_2410.21228v1.md"},{"title":"LoRA vs Full Fine-tuning: An Illusion of Equivalence - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241021228S/abstract"},{"title":"[2410.21228v1] LoRA vs Full Fine-tuning: An Illusion of Equivalence","url":"https://arxiv.org/abs/2410.21228v1"},{"title":"[Literature Review] LoRA vs Full Fine-tuning: An Illusion of Equivalence","url":"https://www.themoonlight.io/en/review/lora-vs-full-fine-tuning-an-illusion-of-equivalence"}]

I found the research paper you were looking for! Here's a summary of the key findings:

## Paper Overview

"LoRA vs Full Fine-tuning: An Illusion of Equivalence" is a 2024 research paper that examines whether LoRA and full fine-tuning truly produce equivalent solutions.

## Key Findings

The central discovery is that LoRA and full fine-tuning yield weight matrices whose singular value decompositions exhibit very different structure: weight matrices trained with LoRA have new, high-ranking singular vectors, which are called "intruder dimensions", while those trained with full fine-tuning do not.

The matrix product of LoRA is an important component in the introduction of intruder dimensions because of how it amplifies the spectral differences between the low-rank matrices.

## Implications for Generalization

Despite appearing equivalent in task performance, LoRA models with intruder dimensions, despite achieving similar performance to full fine-tuning on the target task, become worse models of the pre-training distribution and adapt less robustly to multiple tasks sequentially.

The intruder dimensions cause forgetting, and scaling them down significantly improves modeling of the pre-training distribution with a minimal drop in downstream task performance.

The paper was published in October 2024 (arXiv 2410.21228) and has since been accepted at NeurIPS 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "76f4d645-8b03-4740-a51d-3a0877c6c12b"
}
```

</details>

---

### System

_source line 163_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for \"closer look at how fine-tuning changes BERT\" Zho…",
  "usage": {
    "total_tokens": 29933,
    "tool_uses": 15,
    "duration_ms": 143487
  },
  "last_tool_name": "WebSearch",
  "uuid": "4b4180a9-df1e-4c7f-880c-62052ee49a38",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 164_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HfQ4bLtWYiakcDTYMRe72R`</summary>

```json
{
  "query": "\"closer look at how fine-tuning changes BERT\" Zhou 2022 ACL authors findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "e8e6cc1f-3e32-4632-b1dd-5d41a0d85b96",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2kxoQqRbNtYPZPkoBJtnh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1042,
      "cache_read_input_tokens": 28345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1042,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 165 · 2026-05-15T16:03:55.908Z_

<details><summary>↩ Tool result · `toolu_01HfQ4bLtWYiakcDTYMRe72R`</summary>

```text
Web search results for query: ""closer look at how fine-tuning changes BERT" Zhou 2022 ACL authors findings"

Links: [{"title":"A Closer Look at How Fine-tuning Changes BERT - ACL Anthology","url":"https://aclanthology.org/2022.acl-long.75/"},{"title":"A Closer Look at How Fine-tuning Changes BERT Yichu Zhou School of Computing","url":"https://aclanthology.org/2022.acl-long.75.pdf"},{"title":"GitHub - utahnlp/BERT-fine-tuning-analysis: The codebase for the paper: A Closer Look at How Fine-tuning Changes BERT","url":"https://github.com/utahnlp/BERT-fine-tuning-analysis"},{"title":"A Closer Look at How Fine-tuning Changes BERT :: Vivek Srikumar","url":"https://svivek.com/research/zhou2022closer.html"},{"title":"[PDF] A Closer Look at How Fine-tuning Changes BERT | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Closer-Look-at-How-Fine-tuning-Changes-BERT-Zhou-Srikumar/f07bcf49a92e09437359be788bbe3f9237c5ec40"},{"title":"A Closer Look at How Fine-tuning Changes BERT | Request PDF","url":"https://www.researchgate.net/publication/361059394_A_Closer_Look_at_How_Fine-tuning_Changes_BERT"},{"title":"[2106.14282] A Closer Look at How Fine-tuning Changes BERT","url":"https://arxiv.org/abs/2106.14282"},{"title":"Figure 2 from A Closer Look at How Fine-tuning Changes BERT | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Closer-Look-at-How-Fine-tuning-Changes-BERT-Zhou-Srikumar/966a38882be844dbf7e8b15478e1bdf3c75ef8a6/figure/3"},{"title":"A Closer Look at How Fine-tuning Changes BERT","url":"https://aclanthology.org/2022.acl-long.75v1.pdf"},{"title":"A Closer Look at How Fine-tuning Changes BERT","url":"https://nlp.cs.utah.edu/assets/pdfs/zhou2022closer.pdf"}]

I found the paper you're looking for. Here's a summary of the key findings from "A Closer Look at How Fine-tuning Changes BERT" by Zhou and Srikumar (ACL 2022):

## Authors and Publication
The paper was authored by Yichu Zhou and Vivek Srikumar and was published in 2022 in the Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics.

## Main Hypothesis and Findings

The authors hypothesized that fine-tuning affects classification performance by increasing the distances between examples associated with different labels, and confirmed this hypothesis with carefully designed experiments on five different NLP tasks.

## Key Discoveries

Via these experiments, the researchers discovered an exception to the prevailing wisdom that "fine-tuning always improves performance".

By comparing the representations before and after fine-tuning, the authors discovered that fine-tuning does not introduce arbitrary changes to representations; instead, it adjusts the representations to downstream tasks while largely preserving the original spatial structure of the data points.

## Methodology

The researchers studied the English BERT family and used two probing techniques to analyze how fine-tuning changes the space.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "0b6f18ac-dfd0-434b-8b5f-5d1dbf5406d7"
}
```

</details>

---

### System

_source line 166_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for \"Ethayarajh\" 2019 contextual word embeddings anis…",
  "usage": {
    "total_tokens": 30954,
    "tool_uses": 16,
    "duration_ms": 153661
  },
  "last_tool_name": "WebSearch",
  "uuid": "c7dccace-b4d0-4b83-90b7-eaa7a770f0ba",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 167_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018ve9Lhoe1XDuQUNCH75RMg`</summary>

```json
{
  "query": "\"Ethayarajh\" 2019 contextual word embeddings anisotropy BERT GPT-2 ELMo EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "e9395962-e1ca-4ec1-93a7-2d3914872f14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3Mqg8cZbJwfH3NTz6FZT4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 983,
      "cache_read_input_tokens": 29387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 983,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 168 · 2026-05-15T16:04:07.085Z_

<details><summary>↩ Tool result · `toolu_018ve9Lhoe1XDuQUNCH75RMg`</summary>

```text
Web search results for query: ""Ethayarajh" 2019 contextual word embeddings anisotropy BERT GPT-2 ELMo EMNLP"

Links: [{"title":"BERT, ELMo, & GPT-2: How Contextual are Contextualized Word Representations? | SAIL Blog","url":"https://ai.stanford.edu/blog/contextual/"},{"title":"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings - ACL Anthology","url":"https://aclanthology.org/D19-1006/"},{"title":"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings","url":"https://www.researchgate.net/publication/336998283_How_Contextual_are_Contextualized_Word_Representations_Comparing_the_Geometry_of_BERT_ELMo_and_GPT-2_Embeddings"},{"title":"BERT, ELMo, & GPT-2: How contextual are contextualized word representations? | Kawin Ethayarajh","url":"https://kawine.github.io/blog/nlp/2020/02/03/contextual.html"},{"title":"[1909.00512] How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings","url":"https://arxiv.org/abs/1909.00512"},{"title":"[PDF] How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings | Semantic Scholar","url":"https://www.semanticscholar.org/paper/How-Contextual-are-Contextualized-Word-Comparing-of-Ethayarajh/9d7902e834d5d1d35179962c7a5b9d16623b0d39"},{"title":"How Contextual are Contextualized Word Representations? Kawin Ethayarajh","url":"https://kawine.github.io/assets/emnlp_2019_contextual_slides.pdf"},{"title":"GitHub - kawine/contextual: How Contextual are Contextualized Word Representations? · GitHub","url":"https://github.com/kawine/contextual"},{"title":"How Contextual are Contextualized Word Representations ...","url":"https://aclanthology.org/D19-1006.pdf"},{"title":"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/da5d0335c8cfdf7003194613d1a6373f"}]

Based on the search results, I found comprehensive information about the paper you're looking for:

The paper is "How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings" by Kawin Ethayarajh, published in the Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP).

**Key Findings:**

In all layers of BERT, ELMo, and GPT-2, the representations of all words are anisotropic: they occupy a narrow cone in the embedding space instead of being distributed throughout.

The contextualized representations of all words are not isotropic in any layer of the contextualizing model. While representations of the same word in different contexts still have a greater cosine similarity than those of two different words, this self-similarity is much lower in upper layers, suggesting that upper layers of contextualizing models produce more context-specific representations.

On average, less than 5% of the variance in a word's contextualized representations can be explained by a static embedding for that word.

After adjusting for anisotropy, the similarity between words in the same sentence is highest in ELMo but almost non-existent in GPT-2.

The paper addresses fundamental questions about how contextual these models truly are, examining whether they create infinitely many context-specific representations or assign words to a finite number of word-sense representations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "cbbccf49-2406-4160-b22c-ed4101676c7b"
}
```

</details>

---

### System

_source line 169_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for SEQ-VCR preventing collapse intermediate represen…",
  "usage": {
    "total_tokens": 32189,
    "tool_uses": 17,
    "duration_ms": 163803
  },
  "last_tool_name": "WebSearch",
  "uuid": "6dab31e0-b3e0-4efc-bfdb-ccdc6f853693",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 170_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S4BpAfpvzezfW3KsL4cBEf`</summary>

```json
{
  "query": "SEQ-VCR preventing collapse intermediate representations transformers ICLR 2025 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "9198c9cd-8441-466f-8d05-8a80f630f43c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdN8o1oKFgg7hH7xWsT9ai",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1201,
      "cache_read_input_tokens": 30370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1201,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 171 · 2026-05-15T16:04:15.074Z_

<details><summary>↩ Tool result · `toolu_01S4BpAfpvzezfW3KsL4cBEf`</summary>

```text
Web search results for query: "SEQ-VCR preventing collapse intermediate representations transformers ICLR 2025 authors"

Links: [{"title":"[2411.02344] Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning","url":"https://arxiv.org/abs/2411.02344"},{"title":"Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/b577c062bd4f894b7e05fab6440373ed-Abstract-Conference.html"},{"title":"Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning | OpenReview","url":"https://openreview.net/forum?id=30oIfmrcFO"},{"title":"SEQ-VCR:PREVENTING COLLAPSE IN INTERMEDIATE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/b577c062bd4f894b7e05fab6440373ed-Paper-Conference.pdf"},{"title":"Seq-VCR:Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning","url":"https://arxiv.org/html/2411.02344v2"},{"title":"(PDF) Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning","url":"https://www.researchgate.net/publication/385560131_Seq-VCR_Preventing_Collapse_in_Intermediate_Transformer_Representations_for_Enhanced_Reasoning"},{"title":"Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241102344R/abstract"},{"title":"seq-vcr:preventing collapse in intermediate transformer ...","url":"https://arxiv.org/pdf/2411.02344"},{"title":"GitHub - rarefin/SEQ_VCR: Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning","url":"https://github.com/rarefin/seq_vcr"},{"title":"SEQ-VCR : preventing collapse in intermediate transformer representations for enhanced reasoning - PolyPublie","url":"https://publications.polymtl.ca/66812/"}]

Based on the search results, I found detailed information about the SEQ-VCR paper published at ICLR 2025.

## Paper Overview

The paper "Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning" is part of the International Conference on Representation Learning 2025 (ICLR 2025).

## Authors

The authors are: Md Rifat Arefin, Gopeshh Raaj Subbaraj, Nicolas Gontier, Yann LeCun, Irina Rish, Ravid Shwartz-Ziv, and Christopher Pal.

## Key Contribution

The work identifies representation collapse in transformer intermediate layers as a key factor limiting their reasoning capabilities, and proposes Sequential Variance-Covariance Regularization (Seq-VCR), which enhances the entropy of intermediate representations and prevents collapse.

## Results

Combined with dummy pause tokens as substitutes for chain-of-thought (CoT) tokens, the method significantly improves performance in arithmetic reasoning problems, achieving 99.5% exact match accuracy in the challenging 5 × 5 integer multiplication task.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "4375f1ee-bdc5-48db-95bb-52d22fa30b2b"
}
```

</details>

---

### System

_source line 172_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for \"Not All Features Are Created Equal\" mechanistic …",
  "usage": {
    "total_tokens": 33187,
    "tool_uses": 18,
    "duration_ms": 174381
  },
  "last_tool_name": "WebSearch",
  "uuid": "438e279f-e31e-46fe-816c-27b6c1203079",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 173_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FfHZf6E6r6MP9BjfqDPrn7`</summary>

```json
{
  "query": "\"Not All Features Are Created Equal\" mechanistic study vision language action models 2025 authors CoRL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "daf81bfa-73d0-4d04-8bd7-03683f4c3417",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwN7Cty2AmCDwA8GhuKXNN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 958,
      "cache_read_input_tokens": 31571,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 958,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
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

### System

_source line 174_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ac55dc78a84dd1566",
  "tool_use_id": "toolu_01DAK3KN1UWBh3EPawus774g",
  "status": "completed",
  "output_file": "",
  "summary": "Literature search: layer-wise probing LLM",
  "usage": {
    "total_tokens": 46939,
    "tool_uses": 31,
    "duration_ms": 184192
  },
  "uuid": "365fb716-9e4b-41a1-88a0-66e20b9989ea",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool result

_source line 175 · 2026-05-15T16:04:22.646Z_

<details><summary>↩ Tool result · `toolu_01DAK3KN1UWBh3EPawus774g`</summary>

```text
Here is the structured report organized by topic.

---

## Topic 1: Layer-wise Probing in LLMs/VLMs

**1. Tenney, Das & Pavlick. "BERT Rediscovers the Classical NLP Pipeline." ACL 2019.**
Using edge probing across BERT's layers, they show linguistic tasks appear in the expected pipeline order (POS tagging in early layers, parsing, NER, semantic roles, then coreference in later layers). The model can dynamically revise lower-level decisions using higher-level information.

**2. Hewitt & Manning. "A Structural Probe for Finding Syntax in Word Representations." NAACL 2019.**
Proposes a structural probe that finds a linear transformation under which squared L2 distance encodes parse tree distance and squared L2 norm encodes tree depth. Such transformations exist for BERT and ELMo but not baselines, showing syntax trees are implicitly embedded in the geometry of deep model representations.

**3. Chen, Wu, Liang, Gong, Shou, Zhang & Li. "Is Bigger and Deeper Always Better? Probing LLaMA Across Scales and Layers." arXiv:2312.04333, 2024.**
Probes LLaMA-2 (7B, 13B, 70B) across five higher-order tasks. Key finding: lower/middle layers have almost negligible arithmetic and factual knowledge, but possess logical reasoning ability even at the lowest layers. Factual and computational capabilities show a sharp jump in deeper layers.

**4. Jin, Yu, Huang, Zeng, Wang, Hua, Zhao, Mei, Meng, Ding, Yang, Du & Zhang. "Exploring Concept Depth: How Large Language Models Acquire Knowledge at Different Layers?" COLING 2025.**
Introduces "Concept Depth" -- more complex concepts are acquired in deeper layers. Probes layer-wise representations across LLaMA, Gemma, and Qwen families. Simpler factual tasks are solvable by shallow layers; complex inferential tasks require deep layers.

**5. Ling et al. "Echoes of BERT: Do Modern Language Models Rediscover the Classical NLP Pipeline?" arXiv:2506.02132, 2025.**
Extends Tenney et al.'s analysis to 25 models including Pythia, OLMo-2, Gemma-2, Qwen2.5, and Llama-3.1 across eight linguistic tasks. The hierarchical pipeline (syntax -> semantics -> discourse) persists in modern LLMs, but larger models compress this hierarchy toward earlier layer positions.

**6. Layer-wise probing of multimodal LLMs (LLaVA, Qwen2-VL).** Multiple 2025 studies show a consistent stage-wise structure: early layers (1-4) encode visual input, middle layers handle lexical-semantic integration, and final layers prepare task-specific outputs. Visual representations gradually align with language features in middle-to-later layers.

---

## Topic 2: Representation Stability Across Layers

**7. Kornblith, Norouzi, Lee & Hinton. "Similarity of Neural Network Representations Revisited." ICML 2019.**
Introduces Centered Kernel Alignment (CKA) as a robust similarity metric for comparing neural network representations. Unlike CCA, CKA reliably identifies correspondences between representations across different initializations. This became the standard tool for measuring layer-wise representation similarity.

**8. Phang, Liu & Bowman. "Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers." BlackboxNLP 2021.**
Uses CKA to measure layer similarity in fine-tuned RoBERTa and ALBERT across 12 NLU tasks. Discovers a consistent block diagonal structure: strong similarity within clusters of earlier and later layers, but not between them. Later layers are so similar that the top few can be discarded without hurting performance, even without further tuning.

**9. Khayatan, Shukor, Parekh & Cord. "Analyzing Finetuning Representation Shift for Multimodal LLMs Steering." ICCV 2025 (arXiv:2501.03012).**
Systematically analyzes how fine-tuning alters the hidden-state structure of multimodal LLMs. Concept-related features are almost linearly separable and become more so in deeper layers (validating the linear representation hypothesis). Shift vectors capture the change from pre-trained to fine-tuned representations and can be used to steer model behavior without retraining.

**10. Intrinsic dimensionality studies (2024-2025).**
Multiple works measure the intrinsic dimensionality (ID) of embeddings before and after supervised fine-tuning. The embedding space diverges substantially from the base model at mid-layer positions, indicating these layers actively expand the model's representational subspace during SFT.

---

## Topic 3: Layer Collapse / Neural Collapse in Deep Networks

**11. Papyan, Han & Donoho. "Prevalence of Neural Collapse During the Terminal Phase of Deep Learning Training." PNAS 2020.**
Identifies four interconnected phenomena (NC1-NC4): within-class variability collapses to zero, class means converge to vertices of a simplex equiangular tight frame (ETF), classifiers align with class means, and the classifier converges to a nearest-class-center decision rule. Observed across architectures and datasets during the terminal phase of training.

**12. Rangamani, Lindegaard, Galanti & Poggio. "Feature Learning in Deep Classifiers through Intermediate Neural Collapse." ICML 2023.**
Extends neural collapse analysis to intermediate layers. Shows that as you move deeper into a trained network, within-class covariance decreases relative to between-class covariance, demonstrating a progressive collapse phenomenon across the depth of the network, not just at the final layer.

**13. Dong, Cordonnier & Loukas. "Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth." ICML 2021.**
Proves that pure self-attention without skip connections or MLPs converges doubly exponentially fast to a rank-1 matrix (all tokens become identical). Skip connections and MLPs are essential architectural components that prevent this collapse.

**14. Noci, Anagnostidis, Biggio, Orvieto, Singh & Lucchi. "Signal Propagation in Transformers: Theoretical Perspectives and the Role of Rank Collapse." NeurIPS 2022.**
Shows that stacking self-attention layers causes rank collapse of token representations at initialization, which hinders training by causing query/key gradients to vanish. Proposes depth-dependent scaling of residual branches as a remedy.

**15. Nait Saada, Naderi & Tanner. "Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers." ICML 2025 (arXiv:2410.07799).**
Identifies rank collapse in width (unique to softmax attention) that worsens with context length. Using random matrix theory, they show a spectral gap between the two largest singular values of the attention matrix causes this collapse, which in turn exacerbates vanishing/exploding gradients and rank collapse in depth.

**16. Zhai, Likhomanenko, Littwin, Busbridge, Ramapuram, Zhang, Gu & Susskind. "Stabilizing Transformer Training by Preventing Attention Entropy Collapse." ICML 2023.**
Identifies attention entropy collapse as a failure mode where attention scores become pathologically concentrated. Proposes sigma-Reparam (spectral normalization + learned scalar on all linear layers) to prevent entropy collapse and stabilize training across image classification, MT, ASR, and LM tasks.

**17. Arefin, Subbaraj, Gontier, LeCun, Rish, Shwartz-Ziv & Pal. "Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning." ICLR 2025.**
Shows that representation collapse in intermediate layers limits reasoning capabilities of decoder-only transformers. Their Sequential Variance-Covariance Regularization (Seq-VCR) prevents intermediate collapse and achieves 99.5% exact match on 5x5 integer multiplication (vs. 0% for same-size baselines and 44% for GPT-4 with CoT).

---

## Topic 4: VLA Fine-tuning Effects on LLM Backbone

**18. Brohan et al. (53+ authors). "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control." arXiv:2307.15818, 2023.**
Builds VLAs on PaLI-X (55B) and PaLM-E (12B), representing robot actions as text tokens. Demonstrates emergent capabilities from web-scale pretraining, including generalization to novel objects and multi-stage semantic reasoning. The key architectural insight: action fine-tuning co-opts the language model's token prediction mechanism.

**19. Kim et al. "OpenVLA: An Open-Source Vision-Language-Action Model." arXiv:2406.09246, 2024.**
Fine-tunes Prismatic-7B VLM (SigLIP + DinoV2 + Llama-2 7B) end-to-end for action prediction. Actions are discretized into 256 bins per dimension and mapped to reserved tokens. This is the primary open-source VLA used in subsequent probing studies.

**20. Haon, Stocking, Chuang & Tomlin. "Mechanistic Interpretability for Steering Vision-Language-Action Models." CoRL (PMLR 305), 2025.**
Projects feedforward activations onto the token embedding basis in Pi0 and OpenVLA, identifying sparse semantic directions (e.g., "fast", "up") causally linked to action selection. Demonstrates zero-shot behavioral control via activation steering in simulation (LIBERO) and on a physical UR5 robot, without fine-tuning or reward signals.

**21. Grant, Zhao & Wang. "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models." arXiv:2603.19233, March 2026.**
Applies activation injection, sparse autoencoders, and linear probes to six VLA models (80M-7B parameters) across 394,000+ rollout episodes. Key findings: (a) the visual pathway dominates action generation across all architectures, (b) expert pathways encode motor programs while VLM pathways encode goal semantics, (c) per-token SAE processing is essential for action fidelity on most architectures.

**22. "Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models." arXiv:2603.19183, March 2026.**
Trains SAEs on residual stream activations of VLAs. Recovered features include motion primitives, task-progress signals, semantic representations, and episode-specific memorization. Individual SAE directions causally influence closed-loop behavior (e.g., steering a pre-grasp alignment feature causes the policy to hover rather than grasp).

**23. Kachaev, Kolosov, Zelezetsky, Kovalev & Panov. "Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization." arXiv:2510.25616, October 2025.**
Shows that naive action fine-tuning induces representation collapse and attention sink in VLAs, with attention maps becoming diffuse/noisy/misplaced, indicating loss of visual-language grounding. Proposes representation alignment methods yielding up to 10% relative improvement in OOD generalization over naive SFT.

**24. "Observing and Controlling Features in Vision-Language-Action Models." arXiv:2603.05487, March 2026.**
Studies linearly encoded features in VLA representation space, proposing feature-observability (linear classifier) and feature-controllability (minimal linear intervention via optimal control) for steering VLA outputs toward desired behaviors.

---

Note on Buurmeijer et al. 2026: I was unable to find any paper by an author named "Buurmeijer" in the VLA or robotics literature. This may be a very recent preprint, an unpublished work, or a name that was slightly different. The closest matches for "probing what VLAs learn" are the Grant et al. (2026) and Haon et al. (2025) papers listed above.

Sources:
- [BERT Rediscovers the Classical NLP Pipeline (ACL 2019)](https://aclanthology.org/P19-1452/)
- [A Structural Probe for Finding Syntax (NAACL 2019)](https://aclanthology.org/N19-1419/)
- [Is Bigger and Deeper Always Better? Probing LLaMA](https://arxiv.org/abs/2312.04333)
- [Exploring Concept Depth (COLING 2025)](https://aclanthology.org/2025.coling-main.37/)
- [Echoes of BERT (2025)](https://arxiv.org/html/2506.02132v4)
- [Similarity of Neural Network Representations Revisited (ICML 2019)](https://arxiv.org/abs/1905.00414)
- [Fine-Tuned Transformers Show Clusters (BlackboxNLP 2021)](https://aclanthology.org/2021.blackboxnlp-1.42/)
- [Analyzing Finetuning Representation Shift for MLLMs (ICCV 2025)](https://arxiv.org/abs/2501.03012)
- [Neural Collapse (PNAS 2020)](https://www.pnas.org/doi/10.1073/pnas.2015509117)
- [Intermediate Neural Collapse (ICML 2023)](https://proceedings.mlr.press/v202/rangamani23a.html)
- [Attention is Not All You Need (ICML 2021)](https://arxiv.org/abs/2103.03404)
- [Signal Propagation in Transformers (NeurIPS 2022)](https://arxiv.org/abs/2206.03126)
- [Mind the Gap: Rank Collapse (ICML 2025)](https://arxiv.org/abs/2410.07799)
- [Stabilizing Transformer Training / sigma-Reparam (ICML 2023)](https://arxiv.org/abs/2303.06296)
- [Seq-VCR: Preventing Collapse (ICLR 2025)](https://arxiv.org/abs/2411.02344)
- [RT-2 (2023)](https://arxiv.org/abs/2307.15818)
- [OpenVLA (2024)](https://arxiv.org/abs/2406.09246)
- [Mechanistic Interpretability for Steering VLAs (CoRL 2025)](https://arxiv.org/abs/2509.00328)
- [Not All Features Are Created Equal (2026)](https://arxiv.org/abs/2603.19233)
- [Sparse Autoencoders Reveal Steerable Features in VLAs (2026)](https://arxiv.org/abs/2603.19183)
- [Don't Blind Your VLA (2025)](https://arxiv.org/abs/2510.25616)
- [Observing and Controlling Features in VLAs (2026)](https://arxiv.org/abs/2603.05487)

agentId: ac55dc78a84dd1566 (use SendMessage with to: 'ac55dc78a84dd1566' to continue this agent)
&lt;usage>total_tokens: 50175
tool_uses: 31
duration_ms: 184194&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "f4201eca-59ce-4ad6-ab29-ba26c3d7b8af",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Search the web for academic papers on these specific topics. I need concrete paper titles, authors, years, and key findings. Search thoroughly.\n\n**Topic 1: Layer-wise probing in LLMs/VLMs**\n- Papers that probe individual layers of large language models or vision-language models for specific properties\n- Especially: papers that show per-layer performance curves (e.g., layer-wise accuracy or R² for probes)\n- Key papers to find: Tenney et al. \"BERT Rediscovers the Classical NLP Pipeline\" (2019), Hewitt & Manning \"A Structural Probe for Finding Syntax\" (2019), any similar work on LLaMA/Llama-2/Llama-3\n\n**Topic 2: Representation stability across layers**\n- Papers discussing how fine-tuning changes layer-wise representations\n- \"Representation geometry\" papers (e.g., CKA similarity, centered kernel alignment across layers)\n- Papers that measure how uniformly information is distributed across layers before vs after training/fine-tuning\n\n**Topic 3: Layer collapse / neural collapse in deep networks**\n- \"Neural Collapse\" (Papyan et al. 2020) and follow-up work\n- Layer collapse in transformers specifically\n- Any papers showing that untrained/randomly initialized models have \"collapsed\" representations in certain layers\n- Feature rank deficiency across layers\n\n**Topic 4: VLA fine-tuning effects on LLM backbone**\n- How does action fine-tuning (robot learning) change the internal representations of a pre-trained LLM?\n- Papers: Buurmeijer et al. 2026, Grant et al. 2026, any probing studies on OpenVLA, RT-2, or Octo\n- \"What does VLA training actually learn?\" type analyses\n\nFor each paper found, provide: Title, Authors, Year, Venue, and a 1-2 sentence summary of the key finding relevant to our topic.\n\nReport in a structured format grouped by topic.",
    "agentId": "ac55dc78a84dd1566",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the structured report organized by topic.\n\n---\n\n## Topic 1: Layer-wise Probing in LLMs/VLMs\n\n**1. Tenney, Das & Pavlick. \"BERT Rediscovers the Classical NLP Pipeline.\" ACL 2019.**\nUsing edge probing across BERT's layers, they show linguistic tasks appear in the expected pipeline order (POS tagging in early layers, parsing, NER, semantic roles, then coreference in later layers). The model can dynamically revise lower-level decisions using higher-level information.\n\n**2. Hewitt & Manning. \"A Structural Probe for Finding Syntax in Word Representations.\" NAACL 2019.**\nProposes a structural probe that finds a linear transformation under which squared L2 distance encodes parse tree distance and squared L2 norm encodes tree depth. Such transformations exist for BERT and ELMo but not baselines, showing syntax trees are implicitly embedded in the geometry of deep model representations.\n\n**3. Chen, Wu, Liang, Gong, Shou, Zhang & Li. \"Is Bigger and Deeper Always Better? Probing LLaMA Across Scales and Layers.\" arXiv:2312.04333, 2024.**\nProbes LLaMA-2 (7B, 13B, 70B) across five higher-order tasks. Key finding: lower/middle layers have almost negligible arithmetic and factual knowledge, but possess logical reasoning ability even at the lowest layers. Factual and computational capabilities show a sharp jump in deeper layers.\n\n**4. Jin, Yu, Huang, Zeng, Wang, Hua, Zhao, Mei, Meng, Ding, Yang, Du & Zhang. \"Exploring Concept Depth: How Large Language Models Acquire Knowledge at Different Layers?\" COLING 2025.**\nIntroduces \"Concept Depth\" -- more complex concepts are acquired in deeper layers. Probes layer-wise representations across LLaMA, Gemma, and Qwen families. Simpler factual tasks are solvable by shallow layers; complex inferential tasks require deep layers.\n\n**5. Ling et al. \"Echoes of BERT: Do Modern Language Models Rediscover the Classical NLP Pipeline?\" arXiv:2506.02132, 2025.**\nExtends Tenney et al.'s analysis to 25 models including Pythia, OLMo-2, Gemma-2, Qwen2.5, and Llama-3.1 across eight linguistic tasks. The hierarchical pipeline (syntax -> semantics -> discourse) persists in modern LLMs, but larger models compress this hierarchy toward earlier layer positions.\n\n**6. Layer-wise probing of multimodal LLMs (LLaVA, Qwen2-VL).** Multiple 2025 studies show a consistent stage-wise structure: early layers (1-4) encode visual input, middle layers handle lexical-semantic integration, and final layers prepare task-specific outputs. Visual representations gradually align with language features in middle-to-later layers.\n\n---\n\n## Topic 2: Representation Stability Across Layers\n\n**7. Kornblith, Norouzi, Lee & Hinton. \"Similarity of Neural Network Representations Revisited.\" ICML 2019.**\nIntroduces Centered Kernel Alignment (CKA) as a robust similarity metric for comparing neural network representations. Unlike CCA, CKA reliably identifies correspondences between representations across different initializations. This became the standard tool for measuring layer-wise representation similarity.\n\n**8. Phang, Liu & Bowman. \"Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers.\" BlackboxNLP 2021.**\nUses CKA to measure layer similarity in fine-tuned RoBERTa and ALBERT across 12 NLU tasks. Discovers a consistent block diagonal structure: strong similarity within clusters of earlier and later layers, but not between them. Later layers are so similar that the top few can be discarded without hurting performance, even without further tuning.\n\n**9. Khayatan, Shukor, Parekh & Cord. \"Analyzing Finetuning Representation Shift for Multimodal LLMs Steering.\" ICCV 2025 (arXiv:2501.03012).**\nSystematically analyzes how fine-tuning alters the hidden-state structure of multimodal LLMs. Concept-related features are almost linearly separable and become more so in deeper layers (validating the linear representation hypothesis). Shift vectors capture the change from pre-trained to fine-tuned representations and can be used to steer model behavior without retraining.\n\n**10. Intrinsic dimensionality studies (2024-2025).**\nMultiple works measure the intrinsic dimensionality (ID) of embeddings before and after supervised fine-tuning. The embedding space diverges substantially from the base model at mid-layer positions, indicating these layers actively expand the model's representational subspace during SFT.\n\n---\n\n## Topic 3: Layer Collapse / Neural Collapse in Deep Networks\n\n**11. Papyan, Han & Donoho. \"Prevalence of Neural Collapse During the Terminal Phase of Deep Learning Training.\" PNAS 2020.**\nIdentifies four interconnected phenomena (NC1-NC4): within-class variability collapses to zero, class means converge to vertices of a simplex equiangular tight frame (ETF), classifiers align with class means, and the classifier converges to a nearest-class-center decision rule. Observed across architectures and datasets during the terminal phase of training.\n\n**12. Rangamani, Lindegaard, Galanti & Poggio. \"Feature Learning in Deep Classifiers through Intermediate Neural Collapse.\" ICML 2023.**\nExtends neural collapse analysis to intermediate layers. Shows that as you move deeper into a trained network, within-class covariance decreases relative to between-class covariance, demonstrating a progressive collapse phenomenon across the depth of the network, not just at the final layer.\n\n**13. Dong, Cordonnier & Loukas. \"Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth.\" ICML 2021.**\nProves that pure self-attention without skip connections or MLPs converges doubly exponentially fast to a rank-1 matrix (all tokens become identical). Skip connections and MLPs are essential architectural components that prevent this collapse.\n\n**14. Noci, Anagnostidis, Biggio, Orvieto, Singh & Lucchi. \"Signal Propagation in Transformers: Theoretical Perspectives and the Role of Rank Collapse.\" NeurIPS 2022.**\nShows that stacking self-attention layers causes rank collapse of token representations at initialization, which hinders training by causing query/key gradients to vanish. Proposes depth-dependent scaling of residual branches as a remedy.\n\n**15. Nait Saada, Naderi & Tanner. \"Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers.\" ICML 2025 (arXiv:2410.07799).**\nIdentifies rank collapse in width (unique to softmax attention) that worsens with context length. Using random matrix theory, they show a spectral gap between the two largest singular values of the attention matrix causes this collapse, which in turn exacerbates vanishing/exploding gradients and rank collapse in depth.\n\n**16. Zhai, Likhomanenko, Littwin, Busbridge, Ramapuram, Zhang, Gu & Susskind. \"Stabilizing Transformer Training by Preventing Attention Entropy Collapse.\" ICML 2023.**\nIdentifies attention entropy collapse as a failure mode where attention scores become pathologically concentrated. Proposes sigma-Reparam (spectral normalization + learned scalar on all linear layers) to prevent entropy collapse and stabilize training across image classification, MT, ASR, and LM tasks.\n\n**17. Arefin, Subbaraj, Gontier, LeCun, Rish, Shwartz-Ziv & Pal. \"Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning.\" ICLR 2025.**\nShows that representation collapse in intermediate layers limits reasoning capabilities of decoder-only transformers. Their Sequential Variance-Covariance Regularization (Seq-VCR) prevents intermediate collapse and achieves 99.5% exact match on 5x5 integer multiplication (vs. 0% for same-size baselines and 44% for GPT-4 with CoT).\n\n---\n\n## Topic 4: VLA Fine-tuning Effects on LLM Backbone\n\n**18. Brohan et al. (53+ authors). \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control.\" arXiv:2307.15818, 2023.**\nBuilds VLAs on PaLI-X (55B) and PaLM-E (12B), representing robot actions as text tokens. Demonstrates emergent capabilities from web-scale pretraining, including generalization to novel objects and multi-stage semantic reasoning. The key architectural insight: action fine-tuning co-opts the language model's token prediction mechanism.\n\n**19. Kim et al. \"OpenVLA: An Open-Source Vision-Language-Action Model.\" arXiv:2406.09246, 2024.**\nFine-tunes Prismatic-7B VLM (SigLIP + DinoV2 + Llama-2 7B) end-to-end for action prediction. Actions are discretized into 256 bins per dimension and mapped to reserved tokens. This is the primary open-source VLA used in subsequent probing studies.\n\n**20. Haon, Stocking, Chuang & Tomlin. \"Mechanistic Interpretability for Steering Vision-Language-Action Models.\" CoRL (PMLR 305), 2025.**\nProjects feedforward activations onto the token embedding basis in Pi0 and OpenVLA, identifying sparse semantic directions (e.g., \"fast\", \"up\") causally linked to action selection. Demonstrates zero-shot behavioral control via activation steering in simulation (LIBERO) and on a physical UR5 robot, without fine-tuning or reward signals.\n\n**21. Grant, Zhao & Wang. \"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models.\" arXiv:2603.19233, March 2026.**\nApplies activation injection, sparse autoencoders, and linear probes to six VLA models (80M-7B parameters) across 394,000+ rollout episodes. Key findings: (a) the visual pathway dominates action generation across all architectures, (b) expert pathways encode motor programs while VLM pathways encode goal semantics, (c) per-token SAE processing is essential for action fidelity on most architectures.\n\n**22. \"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models.\" arXiv:2603.19183, March 2026.**\nTrains SAEs on residual stream activations of VLAs. Recovered features include motion primitives, task-progress signals, semantic representations, and episode-specific memorization. Individual SAE directions causally influence closed-loop behavior (e.g., steering a pre-grasp alignment feature causes the policy to hover rather than grasp).\n\n**23. Kachaev, Kolosov, Zelezetsky, Kovalev & Panov. \"Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization.\" arXiv:2510.25616, October 2025.**\nShows that naive action fine-tuning induces representation collapse and attention sink in VLAs, with attention maps becoming diffuse/noisy/misplaced, indicating loss of visual-language grounding. Proposes representation alignment methods yielding up to 10% relative improvement in OOD generalization over naive SFT.\n\n**24. \"Observing and Controlling Features in Vision-Language-Action Models.\" arXiv:2603.05487, March 2026.**\nStudies linearly encoded features in VLA representation space, proposing feature-observability (linear classifier) and feature-controllability (minimal linear intervention via optimal control) for steering VLA outputs toward desired behaviors.\n\n---\n\nNote on Buurmeijer et al. 2026: I was unable to find any paper by an author named \"Buurmeijer\" in the VLA or robotics literature. This may be a very recent preprint, an unpublished work, or a name that was slightly different. The closest matches for \"probing what VLAs learn\" are the Grant et al. (2026) and Haon et al. (2025) papers listed above.\n\nSources:\n- [BERT Rediscovers the Classical NLP Pipeline (ACL 2019)](https://aclanthology.org/P19-1452/)\n- [A Structural Probe for Finding Syntax (NAACL 2019)](https://aclanthology.org/N19-1419/)\n- [Is Bigger and Deeper Always Better? Probing LLaMA](https://arxiv.org/abs/2312.04333)\n- [Exploring Concept Depth (COLING 2025)](https://aclanthology.org/2025.coling-main.37/)\n- [Echoes of BERT (2025)](https://arxiv.org/html/2506.02132v4)\n- [Similarity of Neural Network Representations Revisited (ICML 2019)](https://arxiv.org/abs/1905.00414)\n- [Fine-Tuned Transformers Show Clusters (BlackboxNLP 2021)](https://aclanthology.org/2021.blackboxnlp-1.42/)\n- [Analyzing Finetuning Representation Shift for MLLMs (ICCV 2025)](https://arxiv.org/abs/2501.03012)\n- [Neural Collapse (PNAS 2020)](https://www.pnas.org/doi/10.1073/pnas.2015509117)\n- [Intermediate Neural Collapse (ICML 2023)](https://proceedings.mlr.press/v202/rangamani23a.html)\n- [Attention is Not All You Need (ICML 2021)](https://arxiv.org/abs/2103.03404)\n- [Signal Propagation in Transformers (NeurIPS 2022)](https://arxiv.org/abs/2206.03126)\n- [Mind the Gap: Rank Collapse (ICML 2025)](https://arxiv.org/abs/2410.07799)\n- [Stabilizing Transformer Training / sigma-Reparam (ICML 2023)](https://arxiv.org/abs/2303.06296)\n- [Seq-VCR: Preventing Collapse (ICLR 2025)](https://arxiv.org/abs/2411.02344)\n- [RT-2 (2023)](https://arxiv.org/abs/2307.15818)\n- [OpenVLA (2024)](https://arxiv.org/abs/2406.09246)\n- [Mechanistic Interpretability for Steering VLAs (CoRL 2025)](https://arxiv.org/abs/2509.00328)\n- [Not All Features Are Created Equal (2026)](https://arxiv.org/abs/2603.19233)\n- [Sparse Autoencoders Reveal Steerable Features in VLAs (2026)](https://arxiv.org/abs/2603.19183)\n- [Don't Blind Your VLA (2025)](https://arxiv.org/abs/2510.25616)\n- [Observing and Controlling Features in VLAs (2026)](https://arxiv.org/abs/2603.05487)"
      }
    ],
    "totalDurationMs": 184194,
    "totalTokens": 50175,
    "totalToolUseCount": 31,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2004,
      "cache_read_input_tokens": 44382,
      "output_tokens": 3788,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2004
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3788,
          "cache_read_input_tokens": 44382,
          "cache_creation_input_tokens": 2004,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2004,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 31
    }
  }
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-15T16:04:31.995Z_

<details><summary>↩ Tool result · `toolu_01FfHZf6E6r6MP9BjfqDPrn7`</summary>

```text
Web search results for query: ""Not All Features Are Created Equal" mechanistic study vision language action models 2025 authors CoRL"

Links: [{"title":"[2603.19233] Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.19233"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/html/2603.19233v1"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=w8Mw9zJt1y"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2603.19233"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.19233v1"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://www.wispaper.ai/en/blog/not-all-features-created-equal-mechanistic-study-vision-language-action-models-20260320/zho"},{"title":"GitHub - CWRU-AISM/action-atlas: Mechanistic Interpretability toolkit for Vision-Language-Action models · GitHub","url":"https://github.com/CWRU-AISM/action-atlas"},{"title":"A Mechanistic Study of Vision-Language-Action Models","url":"https://www.scilit.com/publications/f75b69a88d1084853f4d6fd465af88de"},{"title":"Robotics Research arXiv on X: \"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models Bryce Grant, Xijia Zhao, Peng Wang https://t.co/Mr1IyrLxt9 [𝚌𝚜.𝚁𝙾] https://t.co/9LLIgjodQp\" / X","url":"https://x.com/OWW/status/2034850674173788594"},{"title":"π0.5: a Vision-Language-Action Model with Open-World ...","url":"https://raw.githubusercontent.com/mlresearch/v305/main/assets/black25a/black25a.pdf"}]

Based on the search results, I found the paper you're looking for:

**Title:** "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models"

**Authors:** Bryce Grant, Xijia Zhao, and Peng Wang

**Publication Details:** arXiv preprint arXiv:2603.19233, 2026

**Research Overview:**

Vision-Language-Action (VLA) models combine perception, language, and motor control in a single architecture, yet how they translate multimodal inputs into actions remains poorly understood. 

The study applies activation injection, sparse autoencoders (SAEs), and linear probes to six models spanning 80M to 7B parameters across 394,000+ rollout episodes on four benchmarks.

**Key Findings:**

The visual pathway dominates action generation across all architectures: injecting baseline activations into null-prompt episodes recovers near-identical behavior, while cross-task injection steers robots toward source-task positions (99.8% of X-VLA episodes align with the source trajectory), exposing spatially bound motor programs tied to scene coordinates rather than abstract task representations.

The research also includes an Action Atlas visualization tool for exploring the mechanistic interpretability of these models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "e7f9770a-db22-4342-a618-2304a86e4b94"
}
```

</details>

---

### System

_source line 177_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for \"Fine-Tuned Transformers Show Clusters of Similar…",
  "usage": {
    "total_tokens": 34339,
    "tool_uses": 19,
    "duration_ms": 187970
  },
  "last_tool_name": "WebSearch",
  "uuid": "a0b3570d-29de-45eb-b2b8-a87de5fdf8bc",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 178_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015oiJLKjy7pw1MHcv96zEWp`</summary>

```json
{
  "query": "\"Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers\" 2021 CKA authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "7c9cba5e-3de1-4f06-bda1-c86a5058067e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019sxC6s8XcG9Wmv4Fp3VcPH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1111,
      "cache_read_input_tokens": 32529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1111,
        "ephemeral_1h_input_tokens": 0
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

_source line 179 · 2026-05-15T16:04:40.527Z_

<details><summary>↩ Tool result · `toolu_015oiJLKjy7pw1MHcv96zEWp`</summary>

```text
Web search results for query: ""Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers" 2021 CKA authors"

Links: [{"title":"Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers - ACL Anthology","url":"https://aclanthology.org/2021.blackboxnlp-1.42/"},{"title":"[2109.08406] Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers","url":"https://arxiv.org/abs/2109.08406"},{"title":"Fine-Tuned Transformers Show Clusters of Similar ...","url":"https://aclanthology.org/2021.blackboxnlp-1.42.pdf"},{"title":"Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers","url":"https://www.researchgate.net/publication/357387675_Fine-Tuned_Transformers_Show_Clusters_of_Similar_Representations_Across_Layers"},{"title":"Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers - Jason Phang","url":"https://jasonphang.com/publication/2021-09-18-cka"},{"title":"Fine-Tuned Transformers Show Clusters of Similar ... - NSF PAR","url":"https://par.nsf.gov/servlets/purl/10358004"},{"title":"NYU & UNC Reveal How Transformers’ Learned Representations Change After Fine-Tuning | Synced","url":"https://syncedreview.com/2021/09/29/deepmind-podracer-tpu-based-rl-frameworks-deliver-exceptional-performance-at-low-cost-114/"},{"title":"Papers with Code - Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers","url":"https://paperswithcode.com/paper/fine-tuned-transformers-show-clusters-of"},{"title":"[PDF] Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ca25f7d6954561b342577643053b9ce8d618ade2"},{"title":"Fine-Tuned Transformer Models","url":"https://www.emergentmind.com/topics/fine-tuned-transformer-models"}]

Based on the search results, I found the paper you're looking for:

**Title:** Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers

**Authors:** Jason Phang, Haokun Liu, and Samuel R. Bowman

**Publication:** Proceedings of the Fourth BlackboxNLP Workshop on Analyzing and Interpreting Neural Networks for NLP, pages 529–538, Punta Cana, Dominican Republic, 2021

**Key Findings:** The authors used centered kernel alignment (CKA), a method for comparing learned representations, to measure the similarity of representations in task-tuned models across layers. In experiments across twelve NLU tasks, they discovered a consistent block diagonal structure in the similarity of representations within fine-tuned RoBERTa and ALBERT models, with strong similarity within clusters of earlier and later layers, but not between them.

The paper is also available on arXiv (2109.08406).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "52e677d0-d82e-4716-84a4-942fa1f218d0"
}
```

</details>

---

### System

_source line 180_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for Haon mechanistic interpretability steering vision…",
  "usage": {
    "total_tokens": 35294,
    "tool_uses": 20,
    "duration_ms": 196791
  },
  "last_tool_name": "WebSearch",
  "uuid": "fddab44a-a3b6-4a42-8bd8-8edf6d18b9ed",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 181_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019qeyb27iQdt4VDKwM723N3`</summary>

```json
{
  "query": "Haon mechanistic interpretability steering vision language action models pi0 OpenVLA UR5 LIBERO 2025 CoRL RSS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "a21470e7-59fa-43a6-8cd4-31b08707a3bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PmhtHFRjCNt1MJsDSES3iP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 917,
      "cache_read_input_tokens": 33640,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 917,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 182 · 2026-05-15T16:04:50.313Z_

<details><summary>↩ Tool result · `toolu_019qeyb27iQdt4VDKwM723N3`</summary>

```text
Web search results for query: "Haon mechanistic interpretability steering vision language action models pi0 OpenVLA UR5 LIBERO 2025 CoRL RSS"

Links: [{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models","url":"https://arxiv.org/html/2509.00328v1"},{"title":"[2509.00328] Mechanistic interpretability for steering vision-language-action models","url":"https://arxiv.org/abs/2509.00328"},{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models","url":"https://proceedings.mlr.press/v305/haon25a.html"},{"title":"Mechanistic interpretability for steering vision-language-action models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250900328H/abstract"},{"title":"(PDF) Mechanistic interpretability for steering vision-language-action models","url":"https://www.researchgate.net/publication/395212013_Mechanistic_interpretability_for_steering_vision-language-action_models"},{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=YvsUD8C9QS"},{"title":"Mechanistic Interpretability for Steering Vision Language Action Models","url":"https://vla-mech-interp.github.io/"},{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models","url":"https://openreview.net/pdf/b39be62fae34fd96c66ab4b8ff09b8eb21a1acf4.pdf"},{"title":"Paper page - Mechanistic interpretability for steering vision-language-action models","url":"https://huggingface.co/papers/2509.00328"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"}]

Based on the search results, I found detailed information about the paper you're looking for:

## "Mechanistic Interpretability for Steering Vision-Language-Action Models"

This paper was presented at the 9th Conference on Robot Learning (CoRL 2025) in Seoul, Korea, and the authors include Bear Häon, Kaylene Caswell Stocking, Ian Chuang, and Claire Tomlin.

### Key Contributions

The paper introduces the first framework for interpreting and steering VLAs via their internal representations, enabling direct intervention in model behavior at inference time. 

The researchers project feedforward activations within transformer layers onto the token embedding basis, identifying sparse semantic directions - such as speed and direction - that are causally linked to action selection, and introduce a general-purpose activation steering method that modulates behavior in real time, without fine-tuning, reward signals, or environment interaction.

### Experimental Evaluation

The method was evaluated on two recent open-source VLAs, Pi0 and OpenVLA, and demonstrates zero-shot behavioral control in simulation (LIBERO) and on a physical robot (UR5).

### Broader Impact

The work demonstrates that interpretable components of embodied VLAs can be systematically harnessed for control—establishing a new paradigm for transparent and steerable foundation models in robotics.

The paper was published in the Proceedings of Machine Learning Research (PMLR) Volume 305, pages 2743-2762.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "ba446515-cbe3-4a24-8e4c-a23074bd1300"
}
```

</details>

---

### System

_source line 183_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for \"tuned lens\" \"logit lens\" eliciting latent predic…",
  "usage": {
    "total_tokens": 36259,
    "tool_uses": 21,
    "duration_ms": 206611
  },
  "last_tool_name": "WebSearch",
  "uuid": "ca4fee0a-e921-41f5-9ee4-97248dce8eb0",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 184_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015FzcLCL4qyWGatxyL4YV7H`</summary>

```json
{
  "query": "\"tuned lens\" \"logit lens\" eliciting latent predictions transformers layer-wise 2023 Belrose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "50167f31-b328-47ca-b6ec-cafaa4d9d207",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSjv5NeBXmCN4C6eptF4Fy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 927,
      "cache_read_input_tokens": 34557,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 927,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 185 · 2026-05-15T16:04:57.973Z_

<details><summary>↩ Tool result · `toolu_015FzcLCL4qyWGatxyL4YV7H`</summary>

```text
Web search results for query: ""tuned lens" "logit lens" eliciting latent predictions transformers layer-wise 2023 Belrose"

Links: [{"title":"[2303.08112] Eliciting Latent Predictions from Transformers with the Tuned Lens","url":"https://arxiv.org/abs/2303.08112"},{"title":"Eliciting Latent Predictions from Transformers with the Tuned Lens","url":"https://arxiv.org/html/2303.08112v6"},{"title":"GitHub - AlignmentResearch/tuned-lens: Tools for understanding how transformer predictions are built layer-by-layer · GitHub","url":"https://github.com/AlignmentResearch/tuned-lens"},{"title":"[PDF] Eliciting Latent Predictions from Transformers with the Tuned Lens | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Eliciting-Latent-Predictions-from-Transformers-with-Belrose-Furman/762ca2711eb167f19b79e39c175708ca15e1f5d7"},{"title":"(PDF) Eliciting Latent Predictions from Transformers with the Tuned Lens","url":"https://www.researchgate.net/publication/369233674_Eliciting_Latent_Predictions_from_Transformers_with_the_Tuned_Lens"},{"title":"Eliciting Latent Predictions from Transformers with the Tuned Lens | FAR.AI","url":"https://www.far.ai/research/eliciting-latent-predictions-from-transformers-with-the-tuned-lens"},{"title":"Tuned Lens for Transformer Predictions | PDF | Principal Component Analysis | Applied Mathematics","url":"https://www.scribd.com/document/884319608/Tuned-Lens"},{"title":"Structure and Interpretation of Deep Networks","url":"https://sidn.baulab.info/lenses/"},{"title":"Eliciting Latent Predictions from Transformers with the Tuned Lens | alphaXiv","url":"https://www.alphaxiv.org/resources/2303.08112v5"},{"title":"Eliciting Latent Predictions from Transformers with the Tuned Lens - Consensus","url":"https://www.consensus.app/papers/details/35049287d809537fa9e9b3ace1996757/"}]

I found the paper you were looking for! Here are the search results:

**Title:** Eliciting Latent Predictions from Transformers with the Tuned Lens

**Authors and Date:** Nora Belrose, Igor Ostrovsky, Lev McKinney, Zach Furman, Logan Smith, Danny Halawi, Stella Biderman, and Jacob Steinhardt, published in March 2023.

**Summary:** The paper analyzes transformers from the perspective of iterative inference, seeking to understand how model predictions are refined layer by layer. The authors train an affine probe for each block in a frozen pretrained model, making it possible to decode every hidden state into a distribution over the vocabulary.

**Key Innovation:** The tuned lens is a refinement of the earlier "logit lens" technique, which yielded useful insights but is often brittle. The method is more predictive, reliable and unbiased than the logit lens when tested on various autoregressive language models with up to 20B parameters.

**Additional Findings:** The trajectory of latent predictions can be used to detect malicious inputs with high accuracy.

The paper is available on arXiv (2303.08112) and the code is open-sourced on GitHub at the Alignment Research repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "15ffbc5a-ae42-4ee2-82d2-d4c8cd9b3100"
}
```

</details>

---

### System

_source line 186_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for Kornblith 2019 \"Similarity of Neural Network Repr…",
  "usage": {
    "total_tokens": 37262,
    "tool_uses": 22,
    "duration_ms": 214810
  },
  "last_tool_name": "WebSearch",
  "uuid": "61e458e9-37f3-44f1-a974-3084feeb6ac2",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 187_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KpBBmC2A1D1ipNUFKFyedh`</summary>

```json
{
  "query": "Kornblith 2019 \"Similarity of Neural Network Representations Revisited\" CKA ICML original paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "21efcd07-5283-456c-a444-c6b5e7b9e1ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ivG4Swh4hjWGYVGXtzyHk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1001,
      "cache_read_input_tokens": 35484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1001,
        "ephemeral_1h_input_tokens": 0
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

_source line 188 · 2026-05-15T16:05:06.510Z_

<details><summary>↩ Tool result · `toolu_01KpBBmC2A1D1ipNUFKFyedh`</summary>

```text
Web search results for query: "Kornblith 2019 "Similarity of Neural Network Representations Revisited" CKA ICML original paper"

Links: [{"title":"Similarity of Neural Network Representations Revisited","url":"http://proceedings.mlr.press/v97/kornblith19a/kornblith19a.pdf"},{"title":"SIMILARITY OF NEURAL NETWORK REPRESENTA","url":"https://debug-ml-iclr2019.github.io/cameraready/DebugML-19_paper_9.pdf"},{"title":"Similarity of Neural Network Representations Revisited","url":"https://vitalab.github.io/article/2021/01/28/SimilarityNeuralNets.html"},{"title":"[1905.00414] Similarity of Neural Network Representations Revisited","url":"https://arxiv.org/abs/1905.00414"},{"title":"Similarity of Neural Network Representations Revisited","url":"https://icml.cc/media/icml-2019/Slides/4871.pdf"},{"title":"Similarity of Neural Network Representations Revisited","url":"https://cka-similarity.github.io/"},{"title":"Similarity and Matching of Neural Network Representations","url":"https://proceedings.neurips.cc/paper/2021/file/2cb274e6ce940f47beb8011d8ecb1462-Paper.pdf"},{"title":"Similarity of Neural Network Representations Revisited | Request PDF","url":"https://www.researchgate.net/publication/332799564_Similarity_of_Neural_Network_Representations_Revisited"},{"title":"ICLR Similarity of Neural Network Representations Revisited","url":"https://iclr.cc/virtual/2019/1212"},{"title":"Simon Kornblith, Mohammad Norouzi, Honglak Lee, Geoffrey Hinton","url":"https://icml.cc/media/Slides/icml/2019/halla(13-11-00)-13-12-15-4871-similarity_of_n.pdf"}]

Perfect! I found the paper you're looking for. Here are the key details:

**Paper:** "Similarity of Neural Network Representations Revisited" published at ICML 2019

**Authors:** Simon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton

**Main Contribution:** The authors introduce a similarity index that measures the relationship between representational similarity matrices, which is equivalent to centered kernel alignment (CKA)

**Key Findings:** 
- CCA belongs to a family of statistics for measuring multivariate similarity, but neither CCA nor any other statistic invariant to invertible linear transformation can measure meaningful similarities between representations of higher dimension than the number of data points
- Unlike CCA, CKA can reliably identify correspondences between representations in networks trained from different initializations
- CKA can reveal network pathology that is not evident from test accuracy alone

**Available Resources:**
- Official ICML proceedings: http://proceedings.mlr.press/v97/kornblith19a/kornblith19a.pdf
- arXiv version: https://arxiv.org/abs/1905.00414
- Official project website: https://cka-similarity.github.io/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "555f8d2e-66e2-47fe-8e50-1c2920feb16b"
}
```

</details>

---

### System

_source line 189_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for \"action pathways\" VLA robot LLM backbone fine-tun…",
  "usage": {
    "total_tokens": 38203,
    "tool_uses": 23,
    "duration_ms": 223098
  },
  "last_tool_name": "WebSearch",
  "uuid": "f61854a9-df11-4d2a-804d-5c8962532dc6",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 190_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y4uCHcLE9aPyoxwrFo3itZ`</summary>

```json
{
  "query": "\"action pathways\" VLA robot LLM backbone fine-tuning action tokens representation drift robotics foundation model 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "f914be13-a51f-462d-bcf6-ba539f7026ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xeb9wicFckWSoizgSdqNuK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 36485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 903,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 191 · 2026-05-15T16:05:19.633Z_

<details><summary>↩ Tool result · `toolu_01Y4uCHcLE9aPyoxwrFo3itZ`</summary>

```text
Web search results for query: ""action pathways" VLA robot LLM backbone fine-tuning action tokens representation drift robotics foundation model 2024 2025"

Links: [{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://arxiv.org/html/2509.22195v1"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2508.13073v1"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://vlm2vla.github.io/"},{"title":"RT-2: Vision-Language-Action Models","url":"https://robotics-transformer2.github.io/"},{"title":"From Perception to Action with Integrated VLA Systems Rashid Turgunbaev","url":"https://altumnova.com/index.php/tsir/article/download/35/32/38"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"}]

I found relevant research on Vision-Language-Action (VLA) models for robotics. Here are the key findings related to your search query:

## Core Concepts

VLA models are systems that jointly process visual inputs, interpret natural language instructions, and generate executable action representations for physical robotic hardware. Large VLM-based VLA models embed visual observations and linguistic instructions into a shared, semantically aligned latent space to improve action decoding fidelity and reduce inter-module semantic drift.

## Action Tokenization and Representation

One challenge in adapting transformer-based VLMs for action prediction is bridging the gap between their discrete, token-based nature and continuous, vector-valued representations, with many state-of-the-art VLAs using discretization where continuous action vectors are mapped to a finite set of tokens, typically the VLM's least likely tokens.

## Fine-tuning Approaches

Recent work addresses catastrophic forgetting during fine-tuning. VLM2VLA addresses the challenge of catastrophic forgetting when adapting a VLM for robotic control by grounding action prediction in natural language, using LoRA to train manipulation policies without significantly degrading the backbone VLM's foundational capabilities.

OpenVLA fine-tunes a pretrained Prismatic-7B VLM with a fused visual encoder and Llama 2 7B language model backbone that predicts tokenized output actions, which are then decoded into continuous output actions for robot execution.

## Foundation Models and LLM Backbones

Some VLA models comprise pretrained PaLI-X (55B) as vision model and PaLM-E (12B) embodied models as backbones, co-trained with vision data and upweighted robotics action data.

These recent developments (2024-2025) show significant progress in addressing representation drift and fine-tuning challenges while maintaining foundation model capabilities for robotic control.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "cb55cc9b-5678-44e5-9897-5b4162d88509"
}
```

</details>

---

### System

_source line 192_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for \"Sparse Autoencoders Reveal Interpretable\" VLA mo…",
  "usage": {
    "total_tokens": 39297,
    "tool_uses": 24,
    "duration_ms": 236336
  },
  "last_tool_name": "WebSearch",
  "uuid": "67a2eb00-8690-4ec1-87f6-739d280798e1",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 193_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KcEcZUoCj3rj89DJnAuRnn`</summary>

```json
{
  "query": "\"Sparse Autoencoders Reveal Interpretable\" VLA models 2025 2026 authors Tan Ahn"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "c4a07317-fee0-4502-9ab4-f72998277fe5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q93x5AoKNZ7xKhsjXcGECs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1053,
      "cache_read_input_tokens": 37388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1053,
        "ephemeral_1h_input_tokens": 0
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

_source line 194 · 2026-05-15T16:05:29.195Z_

<details><summary>↩ Tool result · `toolu_01KcEcZUoCj3rj89DJnAuRnn`</summary>

```text
Web search results for query: ""Sparse Autoencoders Reveal Interpretable" VLA models 2025 2026 authors Tan Ahn"

Links: [{"title":"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models","url":"https://arxiv.org/html/2603.19183v1"},{"title":"[2603.19183] Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models","url":"https://arxiv.org/abs/2603.19183"},{"title":"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.19183"},{"title":"Sparse Autoencoders Reveal Interpretable and Steerable ...","url":"https://drvla.github.io/"},{"title":"Sparse Autoencoders Find Highly Interpretable Features in Language Models | OpenReview","url":"https://openreview.net/forum?id=F76bwRSLeK"},{"title":"SPARSE AUTOENCODERS REVEAL INTERPRETABLE ...","url":"https://openreview.net/pdf?id=5AuN6RD072"},{"title":"GitHub - gauravfs-14/awesome-mechanistic-interpretability: A carefully curated collection of high-quality libraries, projects, tutorials, research papers, and other essential resources focused on Mechanistic Interpretability, a growing subfield in machine learning interpretability research that aims to reverse-engineer neural networks into understandable computational components. · GitHub","url":"https://github.com/gauravfs-14/awesome-mechanistic-interpretability"},{"title":"ICLR Poster Sparse Autoencoders Find Highly Interpretable Features in Language Models","url":"https://iclr.cc/virtual/2024/poster/19081"},{"title":"[2309.08600] Sparse Autoencoders Find Highly Interpretable Features in Language Models","url":"https://arxiv.org/abs/2309.08600"},{"title":"Sparse autoencoders uncover biologically interpretable features in protein language model representations - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/40828027/"}]

I found the paper! Here are the search results for "Sparse Autoencoders Reveal Interpretable" VLA models:

## Main Result

The paper "Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models" was authored by Aiden Swann and 4 other authors. The paper was published on March 19, 2026.

Note: The search results show the paper was authored by Aiden Swann and colleagues, but I did not find "Tan Ahn" listed as an author in the available search results. The paper may have additional authors not displayed in these summaries, or you may want to verify the author names directly from the full paper.

## Key Research Findings

The work applies mechanistic interpretability techniques to better understand VLA models by training Sparse Autoencoders (SAEs) on hidden layer activations of the VLA. The majority of extracted SAE features correspond to memorized sequences from specific training demonstrations, but some features correspond to interpretable, general, and steerable motion primitives and semantic properties.

The researchers released an open-source codebase for activation collection, SAE training, and feature steering in VLA models, known as Dr. VLA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "c7ba38cf-6a08-4d23-b3ec-72ee8fb539a6"
}
```

</details>

---

### System

_source line 195_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "description": "Searching for \"VLM2VLA\" \"Actions as Language\" fine-tuning VLMs …",
  "usage": {
    "total_tokens": 40278,
    "tool_uses": 25,
    "duration_ms": 245280
  },
  "last_tool_name": "WebSearch",
  "uuid": "79155d0c-31bb-44d8-8d56-50715f15b8e5",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool call

_source line 196_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GCj4dBtkh7NmYxmAHRDDyh`</summary>

```json
{
  "query": "\"VLM2VLA\" \"Actions as Language\" fine-tuning VLMs VLAs catastrophic forgetting 2025 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "65122670-14e6-45dc-ace2-0d9a50188f2a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017e4W7oStyUCd58rhtj9P2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 938,
      "cache_read_input_tokens": 38441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 938,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 197 · 2026-05-15T16:05:39.287Z_

<details><summary>↩ Tool result · `toolu_01GCj4dBtkh7NmYxmAHRDDyh`</summary>

```text
Web search results for query: ""VLM2VLA" "Actions as Language" fine-tuning VLMs VLAs catastrophic forgetting 2025 authors"

Links: [{"title":"[2509.22195] Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://arxiv.org/abs/2509.22195"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://arxiv.org/pdf/2509.22195"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://vlm2vla.github.io/"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250922195H/abstract"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting | alphaXiv","url":"https://www.alphaxiv.org/overview/2509.22195"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting | OpenReview","url":"https://openreview.net/forum?id=sFO9d6XSlf"},{"title":"From Vision-Language Models to Robot Control — Without Forgetting – Princeton Laboratory for Artificial Intelligence Research Blog","url":"https://blog.ai.princeton.edu/2026/04/23/from-vision-language-models-to-robot-control-without-forgetting/"},{"title":"(PDF) Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://www.researchgate.net/publication/395944766_Actions_as_Language_Fine-Tuning_VLMs_into_VLAs_Without_Catastrophic_Forgetting"},{"title":"ACTIONS AS LANGUAGE: FINE-TUNING VLMS INTO VLAS ...","url":"https://openreview.net/pdf?id=sFO9d6XSlf"},{"title":"LangForce: Bayesian Decomposition of Vision Language ...","url":"https://arxiv.org/pdf/2601.15197"}]

Based on the search results, here's what I found about VLM2VLA and the "Actions as Language" paper:

## Overview

VLM2VLA is a VLA training paradigm that resolves the distribution mismatch at the data level by representing low-level actions with natural language, making it possible to train VLAs solely with Low-Rank Adaptation (LoRA), thereby minimally modifying the VLM backbone and averting catastrophic forgetting.

## The Problem Addressed

Fine-tuning VLMs on robot teleoperation data to create VLA models suffers from a fundamental tradeoff where learning to produce actions diminishes the VLM's foundational reasoning and multimodal understanding. This catastrophic forgetting is due to a distribution mismatch between the VLM's internet-scale pretraining corpus and the robotics fine-tuning data.

## Key Contributions

Through extensive Visual Question Answering (VQA) studies and over 800 real-world robotics experiments, VLM2VLA preserves the VLM's core capabilities, enabling zero-shot generalization to novel tasks that require open-world semantic reasoning and multilingual instruction following.

## Authors

The paper is authored by Asher J. Hancock and 4 other authors. The full author list includes Hancock, Wu, Zha, Russakovsky, and Majumdar from Princeton University, and the paper is being presented at ICLR.

## Publication Details

The paper "Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting" was published on arXiv on September 26, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "de4ae85c-5bc2-465f-a443-383df9c334c2"
}
```

</details>

---

### System

_source line 198_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "aed88ee07adfbc664",
  "tool_use_id": "toolu_01JTaZBVPMBnG51dC9dP2eeF",
  "status": "completed",
  "output_file": "",
  "summary": "Literature search: neural collapse & representation geometry",
  "usage": {
    "total_tokens": 41345,
    "tool_uses": 25,
    "duration_ms": 321252
  },
  "uuid": "92b5b391-8169-447c-84e3-c0c1b36394bd",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2"
}
```

---

### Tool result

_source line 199 · 2026-05-15T16:06:48.115Z_

<details><summary>↩ Tool result · `toolu_01JTaZBVPMBnG51dC9dP2eeF`</summary>

```text
Now I have comprehensive data across all four topics. Let me compile the report.

Here is the literature search report, grouped by topic.

---

## Topic A: Neural Collapse and Layer-wise Behavior

1. **"Prevalence of Neural Collapse during the Terminal Phase of Deep Learning Training"** -- Vardan Papyan, X.Y. Han, David L. Donoho -- 2020 -- PNAS. Identifies four interconnected phenomena ("neural collapse") in the terminal phase of training: last-layer features converge to class means, which become equinorm and equiangular, aligning with classifiers. The foundational paper defining NC. ([arXiv](https://arxiv.org/abs/2008.08186))

2. **"Linguistic Collapse: Neural Collapse in (Large) Language Models"** -- Robert Wu, Vardan Papyan -- 2024 -- NeurIPS. Extends NC to causal language models, showing that NC properties develop with scale and regularization and are linked to generalization, establishing the first empirical bridge between NC and LLMs. ([arXiv](https://arxiv.org/abs/2405.17767))

3. **"Are All Layers Created Equal: A Neural Collapse Perspective"** -- Zhou, Jiang, Zhu -- 2025 -- CPAL (Proceedings of MLR). Studies progressive NC layer-by-layer in larger models: deeper layers significantly enhance NC and aid generalization but are more susceptible to memorization; middle layers contribute minimally due to diminished NC enhancement. ([OpenReview](https://openreview.net/forum?id=5eHpefiK8W))

4. **"Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning"** -- Md Rifat Arefin, Gopeshh Raaj Subbaraj, Nicolas Gontier, Yann LeCun, Irina Rish, Ravid Shwartz-Ziv, Christopher Pal -- 2025 -- ICLR. Identifies representation collapse in intermediate transformer layers as limiting reasoning; proposes Sequential Variance-Covariance Regularization to enhance entropy of intermediate representations, achieving 99.5% exact match on 5x5 integer multiplication. ([arXiv](https://arxiv.org/abs/2411.02344))

5. **"Eliciting Latent Predictions from Transformers with the Tuned Lens"** -- Nora Belrose, Zach Furman, Logan Smith, et al. -- 2023 -- arXiv. Trains affine probes at each layer to decode hidden states into vocabulary distributions, showing how predictions refine progressively layer-by-layer; a more reliable alternative to the logit lens. ([arXiv](https://arxiv.org/abs/2303.08112))

---

## Topic B: Fine-tuning Effects on Pretrained Model Representations

1. **"Similarity of Neural Network Representations Revisited"** -- Simon Kornblith, Mohammad Norouzi, Honglak Lee, Geoffrey Hinton -- 2019 -- ICML. Introduces CKA as a reliable measure of representational similarity, showing it can identify correspondences between networks trained from different initializations where CCA fails. The foundational CKA paper. ([arXiv](https://arxiv.org/abs/1905.00414))

2. **"Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers"** -- Jason Phang, Haokun Liu, Samuel R. Bowman -- 2021 -- BlackboxNLP (EMNLP). Uses CKA on fine-tuned RoBERTa/ALBERT across 12 NLU tasks; discovers a block diagonal structure with strong within-cluster similarity in early and late layers but not between them, showing fine-tuning creates distinct representational phases. ([ACL Anthology](https://aclanthology.org/2021.blackboxnlp-1.42/))

3. **"A Closer Look at How Fine-tuning Changes BERT"** -- Yichu Zhou, Vivek Srikumar -- 2022 -- ACL. Shows fine-tuning increases inter-class distances while largely preserving the original spatial structure; fine-tuning does not introduce arbitrary changes but adjusts representations to downstream tasks. ([ACL Anthology](https://aclanthology.org/2022.acl-long.75/))

4. **"LoRA vs Full Fine-tuning: An Illusion of Equivalence"** -- Sharma et al. -- 2024 -- arXiv (NeurIPS 2025). Reveals LoRA produces "intruder dimensions" (new high-ranking singular vectors) absent in full fine-tuning; despite similar task performance, LoRA models are worse at modeling the pretraining distribution and adapt less robustly to sequential tasks. ([arXiv](https://arxiv.org/abs/2410.21228))

5. **"Representation Engineering: A Top-Down Approach to AI Transparency"** -- Andy Zou, Long Phan, Sarah Chen, Dan Hendrycks, J. Zico Kolter, et al. -- 2023 -- arXiv. Proposes RepE using population-level representations for monitoring and manipulating high-level cognitive phenomena (honesty, harmlessness) in LLMs; introduces Linear Artificial Tomography (LAT) for reading and steering internal representations. ([arXiv](https://arxiv.org/abs/2310.01405))

---

## Topic C: Anisotropy, Representation Degeneration, and Training Effects

1. **"How Contextual are Contextualized Word Representations?"** -- Kawin Ethayarajh -- 2019 -- EMNLP. Shows all layers of BERT, ELMo, GPT-2 produce anisotropic representations occupying a narrow cone; upper layers produce more context-specific representations with lower self-similarity; less than 5% of variance in contextual representations is explained by static embeddings. ([ACL Anthology](https://aclanthology.org/D19-1006/))

2. **"Representation Degeneration Problem in Training Natural Language Generation Models"** -- Jun Gao et al. -- 2019 -- ICLR. Reveals word embeddings in pretrained LMs cluster in narrow cones (degeneration); high-frequency words cluster near the origin while low-frequency words scatter further; more isotropic embeddings consistently outperform anisotropic ones. ([arXiv](https://arxiv.org/pdf/1907.12009))

3. **"Anisotropy Is Inherent to Self-Attention in Transformers"** -- (multiple authors) -- 2024 -- EACL. Provides theoretical and empirical analysis showing anisotropy is an inherent property of self-attention, not just a training artifact; decoder models show a bell-shaped anisotropy curve with highest concentration in middle layers. ([ACL Anthology](https://aclanthology.org/2024.eacl-long.3.pdf))

4. **"The Shape of Learning: Anisotropy and Intrinsic Dimensions in Transformer-Based Models"** -- (multiple authors) -- 2024 -- EACL Findings. Shows intrinsic dimension of embeddings increases during initial training phases then compresses toward training's end; training dynamics shape both anisotropy profiles and effective dimensionality of representations. ([arXiv](https://arxiv.org/abs/2311.05928))

5. **"Revisiting Anisotropy in Language Transformers: The Geometry of Learning Dynamics"** -- (multiple authors) -- 2026 -- arXiv. Connects frequency-biased sampling to curvature attenuation and shows training preferentially amplifies tangent directions; activation-derived directions capture substantially larger shares of gradient anisotropy. ([arXiv](https://arxiv.org/abs/2604.08764))

---

## Topic D: Robotics / Embodied AI Representation Analysis

1. **"Mechanistic Interpretability for Steering Vision-Language-Action Models"** -- Bear Haon, Kaylene C. Stocking, Ian Chuang, Claire Tomlin -- 2025 -- CoRL (PMLR v305). First framework for interpreting/steering VLAs via internal representations: projects FFN activations onto token embedding basis, identifies sparse semantic directions (speed, direction) causally linked to action selection; demonstrates zero-shot behavioral control on pi0 and OpenVLA in LIBERO simulation and physical UR5 robot. ([arXiv](https://arxiv.org/abs/2509.00328))

2. **"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models"** -- Bryce Grant, Xijia Zhao, Peng Wang -- 2026 -- arXiv. Cross-architecture study using activation injection, SAEs, and linear probes on 6 models (80M-7B params, 394K+ rollout episodes): visual pathway dominates action generation; less than 25% of FFN neurons are rewired for action prediction, the rest retain semantic functions. ([arXiv](https://arxiv.org/abs/2603.19233))

3. **"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models"** -- Aiden Swann et al. -- 2026 -- arXiv. Trains SAEs on VLA hidden layers: majority of features are memorized demo sequences, but some correspond to interpretable, general, steerable motion primitives; linear probes on OpenVLA activations decode task states (object positions, actions) with >90% accuracy across most layers. ([arXiv](https://arxiv.org/abs/2603.19183))

4. **"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting" (VLM2VLA)** -- Asher J. Hancock, Wu, Zha, Russakovsky, Majumdar -- 2025 -- ICLR. Represents robot actions as natural language to resolve distribution mismatch; trains VLAs with LoRA only, minimally modifying the VLM backbone; preserves core VLM capabilities enabling zero-shot generalization to novel tasks with semantic reasoning. ([arXiv](https://arxiv.org/abs/2509.22195))

5. **"OpenVLA: An Open-Source Vision-Language-Action Model"** -- Kim, Khazatsky, Pertsch, et al. -- 2024 -- arXiv. Fine-tunes Prismatic-7B VLM (fused visual encoder + Llama 2 7B backbone) to predict tokenized robot actions; establishes the primary open-source VLA baseline used in subsequent interpretability studies. ([arXiv](https://arxiv.org/abs/2406.09246))

---

Sources:
- [Papyan et al. 2020 - Neural Collapse (arXiv)](https://arxiv.org/abs/2008.08186)
- [Wu & Papyan 2024 - Linguistic Collapse (NeurIPS)](https://arxiv.org/abs/2405.17767)
- [Zhou et al. 2025 - Are All Layers Created Equal (CPAL)](https://openreview.net/forum?id=5eHpefiK8W)
- [Arefin et al. 2025 - Seq-VCR (ICLR)](https://arxiv.org/abs/2411.02344)
- [Belrose et al. 2023 - Tuned Lens](https://arxiv.org/abs/2303.08112)
- [Kornblith et al. 2019 - CKA (ICML)](https://arxiv.org/abs/1905.00414)
- [Phang et al. 2021 - CKA Clusters (BlackboxNLP)](https://aclanthology.org/2021.blackboxnlp-1.42/)
- [Zhou & Srikumar 2022 - Fine-tuning BERT (ACL)](https://aclanthology.org/2022.acl-long.75/)
- [Sharma et al. 2024 - LoRA vs Full FT](https://arxiv.org/abs/2410.21228)
- [Zou et al. 2023 - Representation Engineering](https://arxiv.org/abs/2310.01405)
- [Ethayarajh 2019 - Contextual Representations (EMNLP)](https://aclanthology.org/D19-1006/)
- [Gao et al. 2019 - Representation Degeneration (ICLR)](https://arxiv.org/pdf/1907.12009)
- [Anisotropy in Self-Attention 2024 (EACL)](https://aclanthology.org/2024.eacl-long.3.pdf)
- [Shape of Learning 2024 (EACL Findings)](https://arxiv.org/abs/2311.05928)
- [Revisiting Anisotropy 2026](https://arxiv.org/abs/2604.08764)
- [Haon et al. 2025 - Mech Interp VLA (CoRL)](https://arxiv.org/abs/2509.00328)
- [Grant et al. 2026 - Not All Features Equal](https://arxiv.org/abs/2603.19233)
- [Swann et al. 2026 - SAEs in VLA](https://arxiv.org/abs/2603.19183)
- [Hancock et al. 2025 - VLM2VLA (ICLR)](https://arxiv.org/abs/2509.22195)
- [Kim et al. 2024 - OpenVLA](https://arxiv.org/abs/2406.09246)

agentId: aed88ee07adfbc664 (use SendMessage with to: 'aed88ee07adfbc664' to continue this agent)
&lt;usage>total_tokens: 43811
tool_uses: 25
duration_ms: 321253&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "40650515-ac66-441f-9fe7-1800a3178ef7",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Search the web for academic papers on these specific topics. I need concrete paper titles, authors, years, and key findings.\n\n**Topic A: Neural Collapse and Layer-wise Behavior**\n- Papyan, Han, Donoho \"Prevalence of Neural Collapse during the terminal phase of deep learning training\" (2020)\n- Follow-up work on neural collapse in transformers, LLMs\n- \"Progressive neural collapse\" or \"layer-wise neural collapse\" \n- How training affects representation geometry layer by layer\n\n**Topic B: Fine-tuning effects on pretrained model representations**\n- How does fine-tuning (LoRA, full fine-tuning) change internal representations?\n- CKA (Centered Kernel Alignment) studies showing which layers change most during fine-tuning\n- \"Representation engineering\" papers (Zou et al. 2023)\n- Papers showing fine-tuning creates more uniform/stable representations\n\n**Topic C: Probe-based analysis showing training stabilizes representations**\n- Papers where probing accuracy becomes more uniform across layers after training\n- \"Anisotropy\" in transformer representations and how training affects it\n- Papers on \"representation degeneration\" in pre-trained models\n\n**Topic D: Robotics / embodied AI representation analysis**\n- Any probing studies on robot learning models (RT-1, RT-2, Octo, OpenVLA)\n- How do vision-language-action models use their LLM backbone?\n- Is there evidence that VLA training creates \"action pathways\" in LLM layers?\n\nFor each paper, provide: Title, Authors, Year, Venue, Key finding (1-2 sentences).\n\nReport grouped by topic, max 400 words per topic.",
    "agentId": "aed88ee07adfbc664",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive data across all four topics. Let me compile the report.\n\nHere is the literature search report, grouped by topic.\n\n---\n\n## Topic A: Neural Collapse and Layer-wise Behavior\n\n1. **\"Prevalence of Neural Collapse during the Terminal Phase of Deep Learning Training\"** -- Vardan Papyan, X.Y. Han, David L. Donoho -- 2020 -- PNAS. Identifies four interconnected phenomena (\"neural collapse\") in the terminal phase of training: last-layer features converge to class means, which become equinorm and equiangular, aligning with classifiers. The foundational paper defining NC. ([arXiv](https://arxiv.org/abs/2008.08186))\n\n2. **\"Linguistic Collapse: Neural Collapse in (Large) Language Models\"** -- Robert Wu, Vardan Papyan -- 2024 -- NeurIPS. Extends NC to causal language models, showing that NC properties develop with scale and regularization and are linked to generalization, establishing the first empirical bridge between NC and LLMs. ([arXiv](https://arxiv.org/abs/2405.17767))\n\n3. **\"Are All Layers Created Equal: A Neural Collapse Perspective\"** -- Zhou, Jiang, Zhu -- 2025 -- CPAL (Proceedings of MLR). Studies progressive NC layer-by-layer in larger models: deeper layers significantly enhance NC and aid generalization but are more susceptible to memorization; middle layers contribute minimally due to diminished NC enhancement. ([OpenReview](https://openreview.net/forum?id=5eHpefiK8W))\n\n4. **\"Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning\"** -- Md Rifat Arefin, Gopeshh Raaj Subbaraj, Nicolas Gontier, Yann LeCun, Irina Rish, Ravid Shwartz-Ziv, Christopher Pal -- 2025 -- ICLR. Identifies representation collapse in intermediate transformer layers as limiting reasoning; proposes Sequential Variance-Covariance Regularization to enhance entropy of intermediate representations, achieving 99.5% exact match on 5x5 integer multiplication. ([arXiv](https://arxiv.org/abs/2411.02344))\n\n5. **\"Eliciting Latent Predictions from Transformers with the Tuned Lens\"** -- Nora Belrose, Zach Furman, Logan Smith, et al. -- 2023 -- arXiv. Trains affine probes at each layer to decode hidden states into vocabulary distributions, showing how predictions refine progressively layer-by-layer; a more reliable alternative to the logit lens. ([arXiv](https://arxiv.org/abs/2303.08112))\n\n---\n\n## Topic B: Fine-tuning Effects on Pretrained Model Representations\n\n1. **\"Similarity of Neural Network Representations Revisited\"** -- Simon Kornblith, Mohammad Norouzi, Honglak Lee, Geoffrey Hinton -- 2019 -- ICML. Introduces CKA as a reliable measure of representational similarity, showing it can identify correspondences between networks trained from different initializations where CCA fails. The foundational CKA paper. ([arXiv](https://arxiv.org/abs/1905.00414))\n\n2. **\"Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers\"** -- Jason Phang, Haokun Liu, Samuel R. Bowman -- 2021 -- BlackboxNLP (EMNLP). Uses CKA on fine-tuned RoBERTa/ALBERT across 12 NLU tasks; discovers a block diagonal structure with strong within-cluster similarity in early and late layers but not between them, showing fine-tuning creates distinct representational phases. ([ACL Anthology](https://aclanthology.org/2021.blackboxnlp-1.42/))\n\n3. **\"A Closer Look at How Fine-tuning Changes BERT\"** -- Yichu Zhou, Vivek Srikumar -- 2022 -- ACL. Shows fine-tuning increases inter-class distances while largely preserving the original spatial structure; fine-tuning does not introduce arbitrary changes but adjusts representations to downstream tasks. ([ACL Anthology](https://aclanthology.org/2022.acl-long.75/))\n\n4. **\"LoRA vs Full Fine-tuning: An Illusion of Equivalence\"** -- Sharma et al. -- 2024 -- arXiv (NeurIPS 2025). Reveals LoRA produces \"intruder dimensions\" (new high-ranking singular vectors) absent in full fine-tuning; despite similar task performance, LoRA models are worse at modeling the pretraining distribution and adapt less robustly to sequential tasks. ([arXiv](https://arxiv.org/abs/2410.21228))\n\n5. **\"Representation Engineering: A Top-Down Approach to AI Transparency\"** -- Andy Zou, Long Phan, Sarah Chen, Dan Hendrycks, J. Zico Kolter, et al. -- 2023 -- arXiv. Proposes RepE using population-level representations for monitoring and manipulating high-level cognitive phenomena (honesty, harmlessness) in LLMs; introduces Linear Artificial Tomography (LAT) for reading and steering internal representations. ([arXiv](https://arxiv.org/abs/2310.01405))\n\n---\n\n## Topic C: Anisotropy, Representation Degeneration, and Training Effects\n\n1. **\"How Contextual are Contextualized Word Representations?\"** -- Kawin Ethayarajh -- 2019 -- EMNLP. Shows all layers of BERT, ELMo, GPT-2 produce anisotropic representations occupying a narrow cone; upper layers produce more context-specific representations with lower self-similarity; less than 5% of variance in contextual representations is explained by static embeddings. ([ACL Anthology](https://aclanthology.org/D19-1006/))\n\n2. **\"Representation Degeneration Problem in Training Natural Language Generation Models\"** -- Jun Gao et al. -- 2019 -- ICLR. Reveals word embeddings in pretrained LMs cluster in narrow cones (degeneration); high-frequency words cluster near the origin while low-frequency words scatter further; more isotropic embeddings consistently outperform anisotropic ones. ([arXiv](https://arxiv.org/pdf/1907.12009))\n\n3. **\"Anisotropy Is Inherent to Self-Attention in Transformers\"** -- (multiple authors) -- 2024 -- EACL. Provides theoretical and empirical analysis showing anisotropy is an inherent property of self-attention, not just a training artifact; decoder models show a bell-shaped anisotropy curve with highest concentration in middle layers. ([ACL Anthology](https://aclanthology.org/2024.eacl-long.3.pdf))\n\n4. **\"The Shape of Learning: Anisotropy and Intrinsic Dimensions in Transformer-Based Models\"** -- (multiple authors) -- 2024 -- EACL Findings. Shows intrinsic dimension of embeddings increases during initial training phases then compresses toward training's end; training dynamics shape both anisotropy profiles and effective dimensionality of representations. ([arXiv](https://arxiv.org/abs/2311.05928))\n\n5. **\"Revisiting Anisotropy in Language Transformers: The Geometry of Learning Dynamics\"** -- (multiple authors) -- 2026 -- arXiv. Connects frequency-biased sampling to curvature attenuation and shows training preferentially amplifies tangent directions; activation-derived directions capture substantially larger shares of gradient anisotropy. ([arXiv](https://arxiv.org/abs/2604.08764))\n\n---\n\n## Topic D: Robotics / Embodied AI Representation Analysis\n\n1. **\"Mechanistic Interpretability for Steering Vision-Language-Action Models\"** -- Bear Haon, Kaylene C. Stocking, Ian Chuang, Claire Tomlin -- 2025 -- CoRL (PMLR v305). First framework for interpreting/steering VLAs via internal representations: projects FFN activations onto token embedding basis, identifies sparse semantic directions (speed, direction) causally linked to action selection; demonstrates zero-shot behavioral control on pi0 and OpenVLA in LIBERO simulation and physical UR5 robot. ([arXiv](https://arxiv.org/abs/2509.00328))\n\n2. **\"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models\"** -- Bryce Grant, Xijia Zhao, Peng Wang -- 2026 -- arXiv. Cross-architecture study using activation injection, SAEs, and linear probes on 6 models (80M-7B params, 394K+ rollout episodes): visual pathway dominates action generation; less than 25% of FFN neurons are rewired for action prediction, the rest retain semantic functions. ([arXiv](https://arxiv.org/abs/2603.19233))\n\n3. **\"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models\"** -- Aiden Swann et al. -- 2026 -- arXiv. Trains SAEs on VLA hidden layers: majority of features are memorized demo sequences, but some correspond to interpretable, general, steerable motion primitives; linear probes on OpenVLA activations decode task states (object positions, actions) with >90% accuracy across most layers. ([arXiv](https://arxiv.org/abs/2603.19183))\n\n4. **\"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting\" (VLM2VLA)** -- Asher J. Hancock, Wu, Zha, Russakovsky, Majumdar -- 2025 -- ICLR. Represents robot actions as natural language to resolve distribution mismatch; trains VLAs with LoRA only, minimally modifying the VLM backbone; preserves core VLM capabilities enabling zero-shot generalization to novel tasks with semantic reasoning. ([arXiv](https://arxiv.org/abs/2509.22195))\n\n5. **\"OpenVLA: An Open-Source Vision-Language-Action Model\"** -- Kim, Khazatsky, Pertsch, et al. -- 2024 -- arXiv. Fine-tunes Prismatic-7B VLM (fused visual encoder + Llama 2 7B backbone) to predict tokenized robot actions; establishes the primary open-source VLA baseline used in subsequent interpretability studies. ([arXiv](https://arxiv.org/abs/2406.09246))\n\n---\n\nSources:\n- [Papyan et al. 2020 - Neural Collapse (arXiv)](https://arxiv.org/abs/2008.08186)\n- [Wu & Papyan 2024 - Linguistic Collapse (NeurIPS)](https://arxiv.org/abs/2405.17767)\n- [Zhou et al. 2025 - Are All Layers Created Equal (CPAL)](https://openreview.net/forum?id=5eHpefiK8W)\n- [Arefin et al. 2025 - Seq-VCR (ICLR)](https://arxiv.org/abs/2411.02344)\n- [Belrose et al. 2023 - Tuned Lens](https://arxiv.org/abs/2303.08112)\n- [Kornblith et al. 2019 - CKA (ICML)](https://arxiv.org/abs/1905.00414)\n- [Phang et al. 2021 - CKA Clusters (BlackboxNLP)](https://aclanthology.org/2021.blackboxnlp-1.42/)\n- [Zhou & Srikumar 2022 - Fine-tuning BERT (ACL)](https://aclanthology.org/2022.acl-long.75/)\n- [Sharma et al. 2024 - LoRA vs Full FT](https://arxiv.org/abs/2410.21228)\n- [Zou et al. 2023 - Representation Engineering](https://arxiv.org/abs/2310.01405)\n- [Ethayarajh 2019 - Contextual Representations (EMNLP)](https://aclanthology.org/D19-1006/)\n- [Gao et al. 2019 - Representation Degeneration (ICLR)](https://arxiv.org/pdf/1907.12009)\n- [Anisotropy in Self-Attention 2024 (EACL)](https://aclanthology.org/2024.eacl-long.3.pdf)\n- [Shape of Learning 2024 (EACL Findings)](https://arxiv.org/abs/2311.05928)\n- [Revisiting Anisotropy 2026](https://arxiv.org/abs/2604.08764)\n- [Haon et al. 2025 - Mech Interp VLA (CoRL)](https://arxiv.org/abs/2509.00328)\n- [Grant et al. 2026 - Not All Features Equal](https://arxiv.org/abs/2603.19233)\n- [Swann et al. 2026 - SAEs in VLA](https://arxiv.org/abs/2603.19183)\n- [Hancock et al. 2025 - VLM2VLA (ICLR)](https://arxiv.org/abs/2509.22195)\n- [Kim et al. 2024 - OpenVLA](https://arxiv.org/abs/2406.09246)"
      }
    ],
    "totalDurationMs": 321253,
    "totalTokens": 43811,
    "totalToolUseCount": 25,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1066,
      "cache_read_input_tokens": 39379,
      "output_tokens": 3365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1066
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3365,
          "cache_read_input_tokens": 39379,
          "cache_creation_input_tokens": 1066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1066,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 25
    }
  }
}
```

</details>

---

### Assistant

_source line 200_

<details><summary>Logged reasoning block</summary>

```text
I now have comprehensive literature research from both agents. Let me synthesize this into the analysis document. Let me now write the full `layer_stability_analysis.md` artifact.

Let me organize the document:

1. **Literature Review** - Layer-wise probing, representation stability, layer collapse, VLA analysis
2. **Story Strength Assessment** - Can this be a standalone paper?
3. **Visualization Schemes** - 2-3 figures with data specs
4. **Additional Experiments Needed**

Let me write this now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "d2600f40-29df-43b6-83ad-d15a18ee5a9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5Bo1HjKe4xsLgyjmhMJTy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8589,
      "cache_read_input_tokens": 29800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8589
      },
      "output_tokens": 18,
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

_source line 201_

Literature research complete. Now synthesizing into the analysis document.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "e602d57f-568e-4271-9a47-6281a60aba5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5Bo1HjKe4xsLgyjmhMJTy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8589,
      "cache_read_input_tokens": 29800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8589
      },
      "output_tokens": 18,
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

_source line 202_

<details open><summary>🔧 Tool call — Bash · `toolu_01MCKFyHz2gaMX8F3TV3uZUY`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/",
  "description": "List existing artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "6219ae26-3dd9-4bfa-a3cd-82aa68e90dc7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5Bo1HjKe4xsLgyjmhMJTy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8589,
      "cache_read_input_tokens": 29800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8589
      },
      "output_tokens": 18,
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

_source line 203 · 2026-05-15T16:06:56.075Z_

<details><summary>↩ Tool result · `toolu_01MCKFyHz2gaMX8F3TV3uZUY`</summary>

```text
_project
action_probe_design.md
controlb_analysis
dinov2_baseline
libero_goal_feasibility.md
literature_map_probing.md
manifest.yaml
mvp_controlb_trained
mvp_probe_trained
probe_design_plan.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "6165b6cd-f098-4b8b-b900-ed95ba53cb2b",
  "tool_use_result": {
    "stdout": "_project\naction_probe_design.md\ncontrolb_analysis\ndinov2_baseline\nlibero_goal_feasibility.md\nliterature_map_probing.md\nmanifest.yaml\nmvp_controlb_trained\nmvp_probe_trained\nprobe_design_plan.md",
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

_source line 204_

<details open><summary>🔧 Tool call — Write · `toolu_012D7YrwyASxczcQi5UXrQCE`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/layer_stability_analysis.md",
  "content": "# Layer Stability Analysis: Deep Dive + Visualization Plan\n\n## 1. Literature Review\n\n### 1.1 Layer-wise Probing in LLMs/VLMs\n\nLayer-wise probing is a mature methodology with well-established baselines:\n\n- **Tenney et al. (ACL 2019)** \"BERT Rediscovers the Classical NLP Pipeline\": Edge probing across BERT layers shows linguistic tasks appear in pipeline order (POS→parsing→NER→SRL→coreference). Established the layer-wise probing paradigm.\n- **Hewitt & Manning (NAACL 2019)** \"A Structural Probe for Finding Syntax\": Linear probes recover parse tree structure from BERT/ELMo embeddings, showing syntax is geometrically encoded.\n- **Chen et al. (arXiv:2312.04333, 2024)** \"Is Bigger and Deeper Always Better? Probing LLaMA Across Scales and Layers\": Lower/middle LLaMA-2 layers have negligible arithmetic/factual knowledge but possess logical reasoning; factual capabilities show sharp jumps in deeper layers.\n- **Jin et al. (COLING 2025)** \"Exploring Concept Depth\": More complex concepts are acquired in deeper layers across LLaMA/Gemma/Qwen families.\n- **Ling et al. (arXiv:2506.02132, 2025)** \"Echoes of BERT\": Extended Tenney's analysis to 25 modern LLMs (Pythia, OLMo-2, Gemma-2, Qwen2.5, Llama-3.1). Hierarchical pipeline persists but larger models compress it toward earlier layers.\n- **Belrose et al. (arXiv:2303.08112, 2023)** \"Tuned Lens\": Affine probes at each layer decode hidden states into vocabulary distributions, showing progressive prediction refinement layer-by-layer.\n\n**Relevance to our work**: These papers establish that layer-wise probing is standard methodology. However, none focus on the *stability* (variance) of probe performance across layers. They report per-layer accuracy curves but don't analyze whether fine-tuning makes these curves smoother. This is our gap.\n\n### 1.2 Representation Stability & Fine-tuning Effects\n\n- **Kornblith et al. (ICML 2019)** CKA: Standard metric for cross-layer/cross-model representational similarity.\n- **Phang et al. (BlackboxNLP 2021)** \"Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers\": CKA on fine-tuned RoBERTa reveals block diagonal structure—strong within-cluster similarity in early/late layers. Top layers become so similar they can be pruned without performance loss.\n- **Zhou & Srikumar (ACL 2022)** \"A Closer Look at How Fine-tuning Changes BERT\": Fine-tuning increases inter-class distances while preserving spatial structure. Changes are task-directed, not arbitrary.\n- **Khayatan et al. (ICCV 2025, arXiv:2501.03012)**: Fine-tuning multimodal LLMs makes concept-related features more linearly separable in deeper layers.\n- **Sharma et al. (arXiv:2410.21228, 2024)** \"LoRA vs Full Fine-tuning: An Illusion of Equivalence\": LoRA produces \"intruder dimensions\" absent in full fine-tuning, changing representation geometry differently.\n- **Ethayarajh (EMNLP 2019)**: All layers of BERT/GPT-2 produce anisotropic representations; upper layers are more context-specific.\n\n**Relevance**: Phang et al.'s finding that fine-tuning creates block-diagonal CKA structure is the closest analog to our stability finding—fine-tuning homogenizes representations within layer blocks. Our per-layer probe stability extends this: not just CKA similarity, but functional uniformity (consistent R² across layers).\n\n### 1.3 Layer Collapse & Neural Collapse\n\n- **Papyan et al. (PNAS 2020)** \"Neural Collapse\": Terminal phase of training causes within-class variability to collapse, class means converge to simplex ETF. Foundational.\n- **Wu & Papyan (NeurIPS 2024)** \"Linguistic Collapse\": Neural collapse extends to causal LLMs, developing with scale and regularization.\n- **Rangamani et al. (ICML 2023)** \"Feature Learning through Intermediate Neural Collapse\": Within-class covariance decreases relative to between-class covariance progressively deeper into trained networks. **Key**: collapse is progressive across depth, not just at final layer.\n- **Zhou et al. (CPAL 2025)** \"Are All Layers Created Equal\": Deeper layers enhance NC and aid generalization but are more susceptible to memorization; middle layers contribute minimally.\n- **Dong et al. (ICML 2021)** \"Attention is Not All You Need\": Pure self-attention without skip connections converges doubly-exponentially to rank-1 matrix. Skip connections prevent collapse.\n- **Noci et al. (NeurIPS 2022)**: Stacking self-attention causes rank collapse at initialization, causing gradient vanishing.\n- **Nait Saada et al. (ICML 2025, arXiv:2410.07799)**: Rank collapse in width worsens with context length, spectral gap causes this.\n- **Zhai et al. (ICML 2023)**: Attention entropy collapse—attention scores become pathologically concentrated; sigma-Reparam prevents it.\n- **Arefin et al. (ICLR 2025)** \"Seq-VCR\": Intermediate representation collapse limits reasoning. Preventing it via regularization achieves 99.5% on 5×5 integer multiplication vs 0% baseline.\n\n**Relevance**: Our \"untrained collapse\" (probe failure in ~50% of layers) aligns with Noci et al.'s rank collapse at initialization. The key insight: VLA fine-tuning *resolves* initialization-induced collapse, creating functional representations across all layers. Arefin et al. is the strongest parallel—they show intermediate collapse limits capability, which mirrors our finding that untrained models have collapsed intermediate layers.\n\n### 1.4 VLA Representation Analysis\n\n- **Haon et al. (CoRL 2025, arXiv:2509.00328)** \"Mechanistic Interpretability for Steering VLAs\": Projects FFN activations onto token embedding basis, identifies sparse semantic directions (speed, direction) causally linked to action selection. Zero-shot behavioral control on OpenVLA/pi0.\n- **Grant et al. (arXiv:2603.19233, 2026)** \"Not All Features Are Created Equal\": Cross-architecture study on 6 VLAs. Visual pathway dominates; <25% of FFN neurons rewired for action prediction. LIBERO-Goal shows language matters when vision is ambiguous.\n- **Swann et al. (arXiv:2603.19183, 2026)**: SAEs on VLA hidden layers: majority of features are memorized demos, some are interpretable motion primitives. Linear probes decode task states >90% accuracy across most layers.\n- **Kachaev et al. (arXiv:2510.25616, 2025)** \"Don't Blind Your VLA\": Naive action fine-tuning induces representation collapse and attention sink, with diffuse/misplaced attention maps.\n- **Hancock et al. (ICLR 2025, arXiv:2509.22195)** \"VLM2VLA\": LoRA-only fine-tuning minimally modifies VLM backbone, preserving VLM capabilities.\n\n**Relevance**: Grant et al. confirms vision dominance (aligns with our negative result). Kachaev et al.'s finding that fine-tuning *induces* representation collapse is the opposite of our finding that fine-tuning *resolves* collapse—critical distinction. Their collapse is about losing visual grounding; our collapse is about randomly-initialized LLM layers being non-functional. Swann et al.'s >90% linear probe accuracy across layers supports our stability finding.\n\n---\n\n## 2. Story Strength Assessment\n\n### 2.1 The Claim\n\n> **\"VLA training reorganizes LLM representations into a stable, layer-uniform action-encoding pathway.\"**\n\nEvidence:\n- **Action prediction probe**: Trained R² = 0.45–0.68 (31/33 layers > untrained), untrained = 0.05–0.62 with multiple convergence failures\n- **Action-delta probe**: Trained = stable 0.04–0.06 across L5-L30, untrained = catastrophic (L5-L28 ≈ 0, only L1-L4 and L32 nonzero)\n- **Temporal distance probe**: Trained 17/33 healthy layers vs untrained more collapse\n\n### 2.2 Standalone Paper Potential: **Weak standalone, strong contribution**\n\n**For**: \n- Novel angle—nobody has reported probe *stability* (variance across layers) as a metric; existing work reports per-layer curves but doesn't analyze their smoothness\n- Three independent probe types converge on the same pattern\n- Connects to theoretical literature (rank collapse at initialization, intermediate neural collapse)\n- Practically relevant: if a VLA has stable representations, individual layers can be pruned/distilled more safely\n\n**Against**:\n- Single model (OpenVLA-7B) + single benchmark (LIBERO-10)—reviewers will demand generalization\n- The \"stability\" claim needs a formal metric (e.g., coefficient of variation of per-layer R²), not just visual inspection\n- Untrained baseline is a randomly-initialized LLM with frozen SigLIP—some reviewers may argue this isn't a meaningful comparison (who cares about untrained model internals?)\n- Peak-performance gap is small (ΔR² = 0.067 best-vs-best), so the \"information content\" story is negative\n- No causal evidence that stability → downstream performance\n\n**Verdict**: Not enough for a standalone paper at CoRL 2026. Best positioned as a section within a broader \"What does VLA training learn?\" analysis paper (Option B from ROADMAP), or as supporting evidence in the LIBERO-Goal instruction-conditioned probing paper (Option A).\n\n### 2.3 Reviewer Attack Surface\n\n1. **\"Untrained is a straw man\"**: Random LLM weights are unrealistic. Compare to *pre-trained but not action-fine-tuned* Llama-2 instead.\n   - **Mitigation**: Add Prismatic-7B (pre-trained VLM, no action fine-tuning) as a baseline. This distinguishes VLM pre-training effect from VLA fine-tuning effect.\n   \n2. **\"Single model, single benchmark\"**: OpenVLA-7B on LIBERO-10 only.\n   - **Mitigation**: Add at least one more VLA (e.g., OpenVLA with different LoRA configs, or a smaller VLA like Octo) and one more benchmark (LIBERO-Goal or Bridge-v2).\n\n3. **\"No formal stability metric\"**: \"Stable\" and \"collapsed\" are informal.\n   - **Mitigation**: Define CoV(R²) = std(R²) / mean(R²) across layers. Report with confidence intervals. Run permutation test for stability difference.\n\n4. **\"Correlation ≠ Causation\"**: Stable probes don't prove the model *uses* these representations.\n   - **Mitigation**: Layer ablation (zero out individual layers, measure action prediction degradation). If trained model degrades uniformly while untrained degrades only at specific layers, this supports the \"distributed pathway\" claim.\n\n5. **\"Vision encoder confound\"**: SigLIP is frozen; maybe it's just passing clean signal through residual connections.\n   - **Mitigation**: Compare probe R² with and without residual stream (ablate skip connections at test time). Or probe on LLM-only activations (subtract vision-projected component).\n\n### 2.4 What This Finding Actually Says\n\nThe most defensible framing:\n\n> VLA action fine-tuning does not inject new information beyond what the vision encoder provides (negative result on information content). However, it structurally reorganizes the LLM backbone: randomly initialized layers that fail to maintain coherent representations become uniformly functional after training. This suggests VLA training's primary effect on the LLM is **representational infrastructure**—creating a stable computational substrate—rather than **information enrichment**.\n\nThis framing:\n- Acknowledges the negative result honestly\n- Positions stability as a structural finding about *how* fine-tuning works, not *what* it learns\n- Connects to pruning/efficiency literature (if all layers are uniform, some are redundant)\n- Opens door to follow-up: *why* is uniformity beneficial for action prediction?\n\n---\n\n## 3. Visualization Schemes\n\n### Figure 1: Layer-wise Probe Performance Comparison (Primary Figure)\n\n**Type**: Multi-panel line plot with confidence bands\n\n**Layout**: 1 row × 3 columns (one per probe type)\n\n**Panel A — Action Prediction Probe (R²)**\n- X-axis: Layer index (0–32)\n- Y-axis: R² (range 0–0.8)\n- Lines: Trained OpenVLA (blue, solid), Untrained OpenVLA (red, dashed), DINO-v2 (green, horizontal dashed line at R²=0.676)\n- Shading: 95% CI bands (bootstrap, task-level)\n- Annotations: Mark collapsed/unconverged layers for untrained with × markers\n- Key visual: Blue line is flat and high; red line is jagged with gaps\n\n**Panel B — Action-Delta Probe (R²)**\n- X-axis: Layer index (0–32)\n- Y-axis: R² (range -0.05–0.10)\n- Lines: Trained (blue), Untrained (red), DINO (green horizontal)\n- Key visual: Blue line is a flat band around 0.05; red line is zero everywhere except L1-4 and L32\n\n**Panel C — Temporal Distance Probe (Spearman ρ)**\n- X-axis: Layer index (0–32)\n- Y-axis: ρ (range 0–1.0)\n- Lines: Trained (blue), Untrained (red), DINO (green horizontal at 0.901)\n- Markers: × for collapsed layers (ρ=0)\n- Key visual: Blue has more healthy points; both have collapsed layers but untrained has more\n\n**Data sources**: \n- Trained action R²: `mvp2_action_trained` experiment results (per-layer R² from ridge regression)\n- Untrained action R²: `mvp2_action_untrained` results\n- DINO R²: `mvp2_action_dino` results\n- Temporal distance: `mvp_probe_trained`, `mvp_probe_untrained`, `dinov2_baseline`\n- Action-delta: from MVP-2 action-delta analysis\n\n**matplotlib spec**:\n```python\nfig, axes = plt.subplots(1, 3, figsize=(15, 4.5), sharey=False)\n# Use seaborn style, Nature-quality fonts\n# Color palette: trained=#2196F3, untrained=#F44336, dino=#4CAF50\n# Line width: 2pt for main, 1pt for CI bands\n# Font: 10pt labels, 11pt panel titles\n# Add CoV(R²) annotation in each panel corner\n```\n\n---\n\n### Figure 2: Stability Metric Comparison (Bar Chart)\n\n**Type**: Grouped bar chart with error bars\n\n**Layout**: Single panel\n\n**X-axis**: Probe type (Action R², Action-Delta R², Temporal ρ)\n**Y-axis**: Coefficient of Variation = std/mean of per-layer metric (excluding collapsed layers)\n**Bars**: Trained (blue), Untrained (red)\n**Error bars**: Bootstrap 95% CI on CoV\n\n**Expected pattern**: Untrained CoV >> Trained CoV for all three probe types\n\n**Purpose**: Quantifies \"stability\" formally. A single number per condition that captures the core finding.\n\n**Data**: Computed from per-layer metrics in Figure 1.\n\n**matplotlib spec**:\n```python\nfig, ax = plt.subplots(1, 1, figsize=(5, 4))\n# Grouped bars, width=0.35\n# Hatching for untrained bars\n# Significance stars (**/***) above paired bars\n# Y-axis label: \"Coefficient of Variation (lower = more stable)\"\n```\n\n---\n\n### Figure 3: Layer Health Heatmap\n\n**Type**: Binary/categorical heatmap\n\n**Layout**: Single panel, 3 rows × 33 columns\n\n**Rows**: Action Probe, Action-Delta Probe, Temporal Distance Probe\n**Columns**: Layers 0–32\n**Cell color**: \n- Green: Trained > Untrained (functional gain)\n- Yellow: Trained ≈ Untrained (no change)\n- Red: Collapsed in untrained (probe failed to converge or R² ≈ 0)\n- Gray: Collapsed in both\n\n**Cell annotation**: Δ value (trained − untrained) in each cell\n\n**Expected pattern**: Green dominates for trained; red band in middle layers for untrained (especially action-delta L5-L28)\n\n**Purpose**: Single-glance summary of the layer stability finding across all probes. Good for talks/posters.\n\n**Data**: Per-layer metrics from all three probe types, thresholds:\n- Collapsed: R² < 0.05 or ρ < 0.1 or probe failed to converge\n- Functional gain: trained − untrained > 0.05\n\n**matplotlib spec**:\n```python\nfig, ax = plt.subplots(1, 1, figsize=(14, 2.5))\n# Use imshow or pcolormesh\n# Custom colormap: diverging RdYlGn\n# Add text annotations in each cell (small font, 7pt)\n# X-ticks every 4 layers, minor ticks every layer\n# Bold border around \"collapse zone\" (L5-L28 for action-delta)\n```\n\n---\n\n## 4. Additional Experiments Needed\n\n### Priority 1 (Required for any publication)\n\n| Experiment | Purpose | Effort | Impact |\n|-----------|---------|--------|--------|\n| **Pre-trained VLM baseline** (Prismatic-7B, no action FT) | Distinguish VLM pre-training effect from VLA fine-tuning effect. Addresses \"untrained is straw man\" attack. | 1 day (feature extraction + probing) | Critical—without this, the comparison is random-init vs trained, which is trivially expected |\n| **Formal stability metric** (CoV with bootstrap CI, permutation test) | Quantify \"stability\" rigorously | 0.5 day (reanalysis of existing data) | Critical—current claim is qualitative |\n| **Per-layer probe convergence diagnostics** | Document which untrained layers failed to converge and why (loss curves, gradient norms) | 0.5 day | Addresses reviewer concern about probe quality vs representation quality |\n\n### Priority 2 (Strongly recommended)\n\n| Experiment | Purpose | Effort | Impact |\n|-----------|---------|--------|--------|\n| **Second VLA model** (e.g., OpenVLA with LoRA-only, or smaller model) | Generalization across architectures | 2-3 days | Addresses single-model concern |\n| **LIBERO-Goal probing** | Test if stability pattern holds in vision-ambiguous setting where language matters | 2-3 days | Could strengthen story significantly—if stability + language sensitivity co-occur |\n| **CKA analysis** (layer-to-layer similarity matrix, trained vs untrained) | Connect to Phang et al.'s block-diagonal finding; show VLA training creates different CKA structure | 1 day | Strengthens theoretical grounding |\n\n### Priority 3 (Nice to have)\n\n| Experiment | Purpose | Effort | Impact |\n|-----------|---------|--------|--------|\n| **Layer ablation** (zero out individual layers, measure action loss) | Causal evidence that stable representations are *used* | 1-2 days | Addresses correlation≠causation |\n| **Representation rank analysis** (effective rank per layer, trained vs untrained) | Connect to rank collapse literature (Noci et al., Dong et al.) | 0.5 day | Mechanistic understanding |\n| **Attention entropy per layer** (trained vs untrained) | Connect to Zhai et al.'s entropy collapse; check if VLA training increases attention entropy | 0.5 day | Additional angle on stability |\n\n### Timeline Assessment (CoRL deadline: May 29 = 14 days)\n\n- Priority 1 experiments: ~2 days → **must start immediately**\n- Priority 2 (second model + LIBERO-Goal): 2-3 days each, can partially parallelize → **feasible if started by May 17**\n- Priority 3: cherry-pick 1-2 based on Priority 1/2 results\n- Writing: 3-4 days for full paper\n- **Verdict**: Tight but feasible for Option B paper if Priority 1 is completed by May 17 and writing starts May 22.\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "247f557e-b042-4bce-ab35-1e43b6d842a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QewJn9SkcU6AUawRYd1kXr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 330,
      "cache_read_input_tokens": 38389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 330
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

_source line 205 · 2026-05-15T16:09:02.785Z_

<details><summary>↩ Tool result · `toolu_012D7YrwyASxczcQi5UXrQCE`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/layer_stability_analysis.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "a34eeff6-d5b3-43a1-8810-57ed9d48ed96",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/layer_stability_analysis.md",
    "content": "# Layer Stability Analysis: Deep Dive + Visualization Plan\n\n## 1. Literature Review\n\n### 1.1 Layer-wise Probing in LLMs/VLMs\n\nLayer-wise probing is a mature methodology with well-established baselines:\n\n- **Tenney et al. (ACL 2019)** \"BERT Rediscovers the Classical NLP Pipeline\": Edge probing across BERT layers shows linguistic tasks appear in pipeline order (POS→parsing→NER→SRL→coreference). Established the layer-wise probing paradigm.\n- **Hewitt & Manning (NAACL 2019)** \"A Structural Probe for Finding Syntax\": Linear probes recover parse tree structure from BERT/ELMo embeddings, showing syntax is geometrically encoded.\n- **Chen et al. (arXiv:2312.04333, 2024)** \"Is Bigger and Deeper Always Better? Probing LLaMA Across Scales and Layers\": Lower/middle LLaMA-2 layers have negligible arithmetic/factual knowledge but possess logical reasoning; factual capabilities show sharp jumps in deeper layers.\n- **Jin et al. (COLING 2025)** \"Exploring Concept Depth\": More complex concepts are acquired in deeper layers across LLaMA/Gemma/Qwen families.\n- **Ling et al. (arXiv:2506.02132, 2025)** \"Echoes of BERT\": Extended Tenney's analysis to 25 modern LLMs (Pythia, OLMo-2, Gemma-2, Qwen2.5, Llama-3.1). Hierarchical pipeline persists but larger models compress it toward earlier layers.\n- **Belrose et al. (arXiv:2303.08112, 2023)** \"Tuned Lens\": Affine probes at each layer decode hidden states into vocabulary distributions, showing progressive prediction refinement layer-by-layer.\n\n**Relevance to our work**: These papers establish that layer-wise probing is standard methodology. However, none focus on the *stability* (variance) of probe performance across layers. They report per-layer accuracy curves but don't analyze whether fine-tuning makes these curves smoother. This is our gap.\n\n### 1.2 Representation Stability & Fine-tuning Effects\n\n- **Kornblith et al. (ICML 2019)** CKA: Standard metric for cross-layer/cross-model representational similarity.\n- **Phang et al. (BlackboxNLP 2021)** \"Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers\": CKA on fine-tuned RoBERTa reveals block diagonal structure—strong within-cluster similarity in early/late layers. Top layers become so similar they can be pruned without performance loss.\n- **Zhou & Srikumar (ACL 2022)** \"A Closer Look at How Fine-tuning Changes BERT\": Fine-tuning increases inter-class distances while preserving spatial structure. Changes are task-directed, not arbitrary.\n- **Khayatan et al. (ICCV 2025, arXiv:2501.03012)**: Fine-tuning multimodal LLMs makes concept-related features more linearly separable in deeper layers.\n- **Sharma et al. (arXiv:2410.21228, 2024)** \"LoRA vs Full Fine-tuning: An Illusion of Equivalence\": LoRA produces \"intruder dimensions\" absent in full fine-tuning, changing representation geometry differently.\n- **Ethayarajh (EMNLP 2019)**: All layers of BERT/GPT-2 produce anisotropic representations; upper layers are more context-specific.\n\n**Relevance**: Phang et al.'s finding that fine-tuning creates block-diagonal CKA structure is the closest analog to our stability finding—fine-tuning homogenizes representations within layer blocks. Our per-layer probe stability extends this: not just CKA similarity, but functional uniformity (consistent R² across layers).\n\n### 1.3 Layer Collapse & Neural Collapse\n\n- **Papyan et al. (PNAS 2020)** \"Neural Collapse\": Terminal phase of training causes within-class variability to collapse, class means converge to simplex ETF. Foundational.\n- **Wu & Papyan (NeurIPS 2024)** \"Linguistic Collapse\": Neural collapse extends to causal LLMs, developing with scale and regularization.\n- **Rangamani et al. (ICML 2023)** \"Feature Learning through Intermediate Neural Collapse\": Within-class covariance decreases relative to between-class covariance progressively deeper into trained networks. **Key**: collapse is progressive across depth, not just at final layer.\n- **Zhou et al. (CPAL 2025)** \"Are All Layers Created Equal\": Deeper layers enhance NC and aid generalization but are more susceptible to memorization; middle layers contribute minimally.\n- **Dong et al. (ICML 2021)** \"Attention is Not All You Need\": Pure self-attention without skip connections converges doubly-exponentially to rank-1 matrix. Skip connections prevent collapse.\n- **Noci et al. (NeurIPS 2022)**: Stacking self-attention causes rank collapse at initialization, causing gradient vanishing.\n- **Nait Saada et al. (ICML 2025, arXiv:2410.07799)**: Rank collapse in width worsens with context length, spectral gap causes this.\n- **Zhai et al. (ICML 2023)**: Attention entropy collapse—attention scores become pathologically concentrated; sigma-Reparam prevents it.\n- **Arefin et al. (ICLR 2025)** \"Seq-VCR\": Intermediate representation collapse limits reasoning. Preventing it via regularization achieves 99.5% on 5×5 integer multiplication vs 0% baseline.\n\n**Relevance**: Our \"untrained collapse\" (probe failure in ~50% of layers) aligns with Noci et al.'s rank collapse at initialization. The key insight: VLA fine-tuning *resolves* initialization-induced collapse, creating functional representations across all layers. Arefin et al. is the strongest parallel—they show intermediate collapse limits capability, which mirrors our finding that untrained models have collapsed intermediate layers.\n\n### 1.4 VLA Representation Analysis\n\n- **Haon et al. (CoRL 2025, arXiv:2509.00328)** \"Mechanistic Interpretability for Steering VLAs\": Projects FFN activations onto token embedding basis, identifies sparse semantic directions (speed, direction) causally linked to action selection. Zero-shot behavioral control on OpenVLA/pi0.\n- **Grant et al. (arXiv:2603.19233, 2026)** \"Not All Features Are Created Equal\": Cross-architecture study on 6 VLAs. Visual pathway dominates; <25% of FFN neurons rewired for action prediction. LIBERO-Goal shows language matters when vision is ambiguous.\n- **Swann et al. (arXiv:2603.19183, 2026)**: SAEs on VLA hidden layers: majority of features are memorized demos, some are interpretable motion primitives. Linear probes decode task states >90% accuracy across most layers.\n- **Kachaev et al. (arXiv:2510.25616, 2025)** \"Don't Blind Your VLA\": Naive action fine-tuning induces representation collapse and attention sink, with diffuse/misplaced attention maps.\n- **Hancock et al. (ICLR 2025, arXiv:2509.22195)** \"VLM2VLA\": LoRA-only fine-tuning minimally modifies VLM backbone, preserving VLM capabilities.\n\n**Relevance**: Grant et al. confirms vision dominance (aligns with our negative result). Kachaev et al.'s finding that fine-tuning *induces* representation collapse is the opposite of our finding that fine-tuning *resolves* collapse—critical distinction. Their collapse is about losing visual grounding; our collapse is about randomly-initialized LLM layers being non-functional. Swann et al.'s >90% linear probe accuracy across layers supports our stability finding.\n\n---\n\n## 2. Story Strength Assessment\n\n### 2.1 The Claim\n\n> **\"VLA training reorganizes LLM representations into a stable, layer-uniform action-encoding pathway.\"**\n\nEvidence:\n- **Action prediction probe**: Trained R² = 0.45–0.68 (31/33 layers > untrained), untrained = 0.05–0.62 with multiple convergence failures\n- **Action-delta probe**: Trained = stable 0.04–0.06 across L5-L30, untrained = catastrophic (L5-L28 ≈ 0, only L1-L4 and L32 nonzero)\n- **Temporal distance probe**: Trained 17/33 healthy layers vs untrained more collapse\n\n### 2.2 Standalone Paper Potential: **Weak standalone, strong contribution**\n\n**For**: \n- Novel angle—nobody has reported probe *stability* (variance across layers) as a metric; existing work reports per-layer curves but doesn't analyze their smoothness\n- Three independent probe types converge on the same pattern\n- Connects to theoretical literature (rank collapse at initialization, intermediate neural collapse)\n- Practically relevant: if a VLA has stable representations, individual layers can be pruned/distilled more safely\n\n**Against**:\n- Single model (OpenVLA-7B) + single benchmark (LIBERO-10)—reviewers will demand generalization\n- The \"stability\" claim needs a formal metric (e.g., coefficient of variation of per-layer R²), not just visual inspection\n- Untrained baseline is a randomly-initialized LLM with frozen SigLIP—some reviewers may argue this isn't a meaningful comparison (who cares about untrained model internals?)\n- Peak-performance gap is small (ΔR² = 0.067 best-vs-best), so the \"information content\" story is negative\n- No causal evidence that stability → downstream performance\n\n**Verdict**: Not enough for a standalone paper at CoRL 2026. Best positioned as a section within a broader \"What does VLA training learn?\" analysis paper (Option B from ROADMAP), or as supporting evidence in the LIBERO-Goal instruction-conditioned probing paper (Option A).\n\n### 2.3 Reviewer Attack Surface\n\n1. **\"Untrained is a straw man\"**: Random LLM weights are unrealistic. Compare to *pre-trained but not action-fine-tuned* Llama-2 instead.\n   - **Mitigation**: Add Prismatic-7B (pre-trained VLM, no action fine-tuning) as a baseline. This distinguishes VLM pre-training effect from VLA fine-tuning effect.\n   \n2. **\"Single model, single benchmark\"**: OpenVLA-7B on LIBERO-10 only.\n   - **Mitigation**: Add at least one more VLA (e.g., OpenVLA with different LoRA configs, or a smaller VLA like Octo) and one more benchmark (LIBERO-Goal or Bridge-v2).\n\n3. **\"No formal stability metric\"**: \"Stable\" and \"collapsed\" are informal.\n   - **Mitigation**: Define CoV(R²) = std(R²) / mean(R²) across layers. Report with confidence intervals. Run permutation test for stability difference.\n\n4. **\"Correlation ≠ Causation\"**: Stable probes don't prove the model *uses* these representations.\n   - **Mitigation**: Layer ablation (zero out individual layers, measure action prediction degradation). If trained model degrades uniformly while untrained degrades only at specific layers, this supports the \"distributed pathway\" claim.\n\n5. **\"Vision encoder confound\"**: SigLIP is frozen; maybe it's just passing clean signal through residual connections.\n   - **Mitigation**: Compare probe R² with and without residual stream (ablate skip connections at test time). Or probe on LLM-only activations (subtract vision-projected component).\n\n### 2.4 What This Finding Actually Says\n\nThe most defensible framing:\n\n> VLA action fine-tuning does not inject new information beyond what the vision encoder provides (negative result on information content). However, it structurally reorganizes the LLM backbone: randomly initialized layers that fail to maintain coherent representations become uniformly functional after training. This suggests VLA training's primary effect on the LLM is **representational infrastructure**—creating a stable computational substrate—rather than **information enrichment**.\n\nThis framing:\n- Acknowledges the negative result honestly\n- Positions stability as a structural finding about *how* fine-tuning works, not *what* it learns\n- Connects to pruning/efficiency literature (if all layers are uniform, some are redundant)\n- Opens door to follow-up: *why* is uniformity beneficial for action prediction?\n\n---\n\n## 3. Visualization Schemes\n\n### Figure 1: Layer-wise Probe Performance Comparison (Primary Figure)\n\n**Type**: Multi-panel line plot with confidence bands\n\n**Layout**: 1 row × 3 columns (one per probe type)\n\n**Panel A — Action Prediction Probe (R²)**\n- X-axis: Layer index (0–32)\n- Y-axis: R² (range 0–0.8)\n- Lines: Trained OpenVLA (blue, solid), Untrained OpenVLA (red, dashed), DINO-v2 (green, horizontal dashed line at R²=0.676)\n- Shading: 95% CI bands (bootstrap, task-level)\n- Annotations: Mark collapsed/unconverged layers for untrained with × markers\n- Key visual: Blue line is flat and high; red line is jagged with gaps\n\n**Panel B — Action-Delta Probe (R²)**\n- X-axis: Layer index (0–32)\n- Y-axis: R² (range -0.05–0.10)\n- Lines: Trained (blue), Untrained (red), DINO (green horizontal)\n- Key visual: Blue line is a flat band around 0.05; red line is zero everywhere except L1-4 and L32\n\n**Panel C — Temporal Distance Probe (Spearman ρ)**\n- X-axis: Layer index (0–32)\n- Y-axis: ρ (range 0–1.0)\n- Lines: Trained (blue), Untrained (red), DINO (green horizontal at 0.901)\n- Markers: × for collapsed layers (ρ=0)\n- Key visual: Blue has more healthy points; both have collapsed layers but untrained has more\n\n**Data sources**: \n- Trained action R²: `mvp2_action_trained` experiment results (per-layer R² from ridge regression)\n- Untrained action R²: `mvp2_action_untrained` results\n- DINO R²: `mvp2_action_dino` results\n- Temporal distance: `mvp_probe_trained`, `mvp_probe_untrained`, `dinov2_baseline`\n- Action-delta: from MVP-2 action-delta analysis\n\n**matplotlib spec**:\n```python\nfig, axes = plt.subplots(1, 3, figsize=(15, 4.5), sharey=False)\n# Use seaborn style, Nature-quality fonts\n# Color palette: trained=#2196F3, untrained=#F44336, dino=#4CAF50\n# Line width: 2pt for main, 1pt for CI bands\n# Font: 10pt labels, 11pt panel titles\n# Add CoV(R²) annotation in each panel corner\n```\n\n---\n\n### Figure 2: Stability Metric Comparison (Bar Chart)\n\n**Type**: Grouped bar chart with error bars\n\n**Layout**: Single panel\n\n**X-axis**: Probe type (Action R², Action-Delta R², Temporal ρ)\n**Y-axis**: Coefficient of Variation = std/mean of per-layer metric (excluding collapsed layers)\n**Bars**: Trained (blue), Untrained (red)\n**Error bars**: Bootstrap 95% CI on CoV\n\n**Expected pattern**: Untrained CoV >> Trained CoV for all three probe types\n\n**Purpose**: Quantifies \"stability\" formally. A single number per condition that captures the core finding.\n\n**Data**: Computed from per-layer metrics in Figure 1.\n\n**matplotlib spec**:\n```python\nfig, ax = plt.subplots(1, 1, figsize=(5, 4))\n# Grouped bars, width=0.35\n# Hatching for untrained bars\n# Significance stars (**/***) above paired bars\n# Y-axis label: \"Coefficient of Variation (lower = more stable)\"\n```\n\n---\n\n### Figure 3: Layer Health Heatmap\n\n**Type**: Binary/categorical heatmap\n\n**Layout**: Single panel, 3 rows × 33 columns\n\n**Rows**: Action Probe, Action-Delta Probe, Temporal Distance Probe\n**Columns**: Layers 0–32\n**Cell color**: \n- Green: Trained > Untrained (functional gain)\n- Yellow: Trained ≈ Untrained (no change)\n- Red: Collapsed in untrained (probe failed to converge or R² ≈ 0)\n- Gray: Collapsed in both\n\n**Cell annotation**: Δ value (trained − untrained) in each cell\n\n**Expected pattern**: Green dominates for trained; red band in middle layers for untrained (especially action-delta L5-L28)\n\n**Purpose**: Single-glance summary of the layer stability finding across all probes. Good for talks/posters.\n\n**Data**: Per-layer metrics from all three probe types, thresholds:\n- Collapsed: R² < 0.05 or ρ < 0.1 or probe failed to converge\n- Functional gain: trained − untrained > 0.05\n\n**matplotlib spec**:\n```python\nfig, ax = plt.subplots(1, 1, figsize=(14, 2.5))\n# Use imshow or pcolormesh\n# Custom colormap: diverging RdYlGn\n# Add text annotations in each cell (small font, 7pt)\n# X-ticks every 4 layers, minor ticks every layer\n# Bold border around \"collapse zone\" (L5-L28 for action-delta)\n```\n\n---\n\n## 4. Additional Experiments Needed\n\n### Priority 1 (Required for any publication)\n\n| Experiment | Purpose | Effort | Impact |\n|-----------|---------|--------|--------|\n| **Pre-trained VLM baseline** (Prismatic-7B, no action FT) | Distinguish VLM pre-training effect from VLA fine-tuning effect. Addresses \"untrained is straw man\" attack. | 1 day (feature extraction + probing) | Critical—without this, the comparison is random-init vs trained, which is trivially expected |\n| **Formal stability metric** (CoV with bootstrap CI, permutation test) | Quantify \"stability\" rigorously | 0.5 day (reanalysis of existing data) | Critical—current claim is qualitative |\n| **Per-layer probe convergence diagnostics** | Document which untrained layers failed to converge and why (loss curves, gradient norms) | 0.5 day | Addresses reviewer concern about probe quality vs representation quality |\n\n### Priority 2 (Strongly recommended)\n\n| Experiment | Purpose | Effort | Impact |\n|-----------|---------|--------|--------|\n| **Second VLA model** (e.g., OpenVLA with LoRA-only, or smaller model) | Generalization across architectures | 2-3 days | Addresses single-model concern |\n| **LIBERO-Goal probing** | Test if stability pattern holds in vision-ambiguous setting where language matters | 2-3 days | Could strengthen story significantly—if stability + language sensitivity co-occur |\n| **CKA analysis** (layer-to-layer similarity matrix, trained vs untrained) | Connect to Phang et al.'s block-diagonal finding; show VLA training creates different CKA structure | 1 day | Strengthens theoretical grounding |\n\n### Priority 3 (Nice to have)\n\n| Experiment | Purpose | Effort | Impact |\n|-----------|---------|--------|--------|\n| **Layer ablation** (zero out individual layers, measure action loss) | Causal evidence that stable representations are *used* | 1-2 days | Addresses correlation≠causation |\n| **Representation rank analysis** (effective rank per layer, trained vs untrained) | Connect to rank collapse literature (Noci et al., Dong et al.) | 0.5 day | Mechanistic understanding |\n| **Attention entropy per layer** (trained vs untrained) | Connect to Zhai et al.'s entropy collapse; check if VLA training increases attention entropy | 0.5 day | Additional angle on stability |\n\n### Timeline Assessment (CoRL deadline: May 29 = 14 days)\n\n- Priority 1 experiments: ~2 days → **must start immediately**\n- Priority 2 (second model + LIBERO-Goal): 2-3 days each, can partially parallelize → **feasible if started by May 17**\n- Priority 3: cherry-pick 1-2 based on Priority 1/2 results\n- Writing: 3-4 days for full paper\n- **Verdict**: Tight but feasible for Option B paper if Priority 1 is completed by May 17 and writing starts May 22.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---

### Tool call

_source line 206_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01HcJcHUwiH5sBLQRMZ92YnG`</summary>

```json
{
  "name": "Layer Stability Deep Analysis",
  "type": "report",
  "description": "Layer stability discovery analysis: literature review (30+ papers on layer-wise probing, neural collapse, representation stability, VLA interpretability), story strength assessment, 3 visualization schemes with matplotlib specs, and prioritized experiment checklist for CoRL 2026",
  "project": "vla-ssd",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/layer_stability_analysis.md",
  "tags": [
    "layer-stability",
    "literature-review",
    "visualization",
    "story-assessment"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "08447df3-b3d8-4dbd-9802-95015e50aac1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FQxRbZiCKZv6wwXB3vNjA5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5330,
      "cache_read_input_tokens": 38719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5330
      },
      "output_tokens": 40,
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

_source line 207 · 2026-05-15T16:09:09.196Z_

<details><summary>↩ Tool result · `toolu_01HcJcHUwiH5sBLQRMZ92YnG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_72a874\", \"name\": \"Layer Stability Deep Analysis\", \"type\": \"report\", \"description\": \"Layer stability discovery analysis: literature review (30+ papers on layer-wise probing, neural collapse, representation stability, VLA interpretability), story strength assessment, 3 visualization schemes with matplotlib specs, and prioritized experiment checklist for CoRL 2026\", \"path\": \"projects/vla-ssd/artifacts/_project/report/layer_stability_analysis.md\", \"url\": null, \"project\": \"vla-ssd\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T16:09:09.165996+00:00\", \"tags\": [\"layer-stability\", \"literature-review\", \"visualization\", \"story-assessment\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "321c5578-7b4d-4c9d-a5a6-f35333b3ff7b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_72a874\\\", \\\"name\\\": \\\"Layer Stability Deep Analysis\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Layer stability discovery analysis: literature review (30+ papers on layer-wise probing, neural collapse, representation stability, VLA interpretability), story strength assessment, 3 visualization schemes with matplotlib specs, and prioritized experiment checklist for CoRL 2026\\\", \\\"path\\\": \\\"projects/vla-ssd/artifacts/_project/report/layer_stability_analysis.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"vla-ssd\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T16:09:09.165996+00:00\\\", \\\"tags\\\": [\\\"layer-stability\\\", \\\"literature-review\\\", \\\"visualization\\\", \\\"story-assessment\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_72a874\", \"name\": \"Layer Stability Deep Analysis\", \"type\": \"report\", \"description\": \"Layer stability discovery analysis: literature review (30+ papers on layer-wise probing, neural collapse, representation stability, VLA interpretability), story strength assessment, 3 visualization schemes with matplotlib specs, and prioritized experiment checklist for CoRL 2026\", \"path\": \"projects/vla-ssd/artifacts/_project/report/layer_stability_analysis.md\", \"url\": null, \"project\": \"vla-ssd\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T16:09:09.165996+00:00\", \"tags\": [\"layer-stability\", \"literature-review\", \"visualization\", \"story-assessment\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 208_

已完成。产出已注册为 `art_20260515_72a874`。

核心结论：

**Story 强度**：Layer stability 发现不足以支撑独立论文——单模型+单 benchmark，且缺乏因果证据。最佳定位是"What does VLA training learn?"分析型论文的核心 section，或 LIBERO-Goal 论文的辅助证据。

**最大风险**：当前对比是 random-init LLM vs trained VLA，审稿人会认为 trivially expected。**Priority 1 是加 Prismatic-7B（pre-trained VLM，未做 action FT）作为 baseline**——这能区分"VLM 预训练效果" vs "VLA fine-tuning 效果"。

**文献定位**：
- Layer-wise probing 方法论成熟（Tenney 2019 → Ling 2025），但无人以 probe *stability*（跨层方差）作为指标——这是我们的 gap
- Arefin et al. (ICLR 2025) Seq-VCR 最相关：中间层 representation collapse 限制推理能力，与我们的 untrained collapse 现象直接对应
- Kachaev et al. (2025) 报告 VLA fine-tuning *导致* representation collapse（与我们相反），他们的 collapse 是视觉 grounding 丢失，我们的是随机初始化层的非功能性

**可视化方案**：3 个图——(1) 三面板 layer-wise R²/ρ 曲线对比，(2) CoV 柱状图量化 stability，(3) Layer health heatmap 一览全局。数据 spec 和 matplotlib 参数已写入文档。

**Timeline**：14 天到 CoRL deadline。Priority 1 实验需 2 天，若 5/17 前完成可留 7 天写作。紧但可行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "uuid": "36bef3ba-c228-472e-abe8-bccdf2127fe9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011W5YDXcFSJ9XAA1YCAbH2r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 561,
      "cache_read_input_tokens": 44049,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 561
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

_source line 209_

已完成。产出已注册为 `art_20260515_72a874`。

核心结论：

**Story 强度**：Layer stability 发现不足以支撑独立论文——单模型+单 benchmark，且缺乏因果证据。最佳定位是"What does VLA training learn?"分析型论文的核心 section，或 LIBERO-Goal 论文的辅助证据。

**最大风险**：当前对比是 random-init LLM vs trained VLA，审稿人会认为 trivially expected。**Priority 1 是加 Prismatic-7B（pre-trained VLM，未做 action FT）作为 baseline**——这能区分"VLM 预训练效果" vs "VLA fine-tuning 效果"。

**文献定位**：
- Layer-wise probing 方法论成熟（Tenney 2019 → Ling 2025），但无人以 probe *stability*（跨层方差）作为指标——这是我们的 gap
- Arefin et al. (ICLR 2025) Seq-VCR 最相关：中间层 representation collapse 限制推理能力，与我们的 untrained collapse 现象直接对应
- Kachaev et al. (2025) 报告 VLA fine-tuning *导致* representation collapse（与我们相反），他们的 collapse 是视觉 grounding 丢失，我们的是随机初始化层的非功能性

**可视化方案**：3 个图——(1) 三面板 layer-wise R²/ρ 曲线对比，(2) CoV 柱状图量化 stability，(3) Layer health heatmap 一览全局。数据 spec 和 matplotlib 参数已写入文档。

**Timeline**：14 天到 CoRL deadline。Priority 1 实验需 2 天，若 5/17 前完成可留 7 天写作。紧但可行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 519718,
  "duration_api_ms": 874034,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "b2a82f57-de0a-4c57-b887-9670b50559d2",
  "total_cost_usd": 3.4117007499999996,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 32769,
    "cache_read_input_tokens": 240696,
    "output_tokens": 8212,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 32769,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 544,
        "cache_read_input_tokens": 44049,
        "cache_creation_input_tokens": 561,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 561
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 974420,
      "outputTokens": 26726,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 56,
      "costUSD": 1.6680499999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 56,
      "outputTokens": 19298,
      "cacheReadInputTokens": 1129954,
      "cacheCreationInputTokens": 111351,
      "webSearchRequests": 0,
      "costUSD": 1.7436507500000005,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "27a97f19-4497-44ae-b6ef-5696512dc4d2"
}
```

</details>

---
