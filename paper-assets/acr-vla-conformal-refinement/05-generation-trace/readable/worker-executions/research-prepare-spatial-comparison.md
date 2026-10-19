# research prepare spatial comparison

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/workers/worker_research_prepare-spatial-comparison_20260514T072305.log`
- **Structured JSON:** [`3411f0b2ce2f8b44d7ea.json`](../../sessions/34/3411f0b2ce2f8b44d7ea.json)

## Before a recorded user message

19 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "1c41b23b-0567-43cc-9be4-04207707f28b",
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
  "uuid": "1d3f6da1-1a17-4c51-8fb6-c28a4fd0e350",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1778760600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "ea2dc736-ef74-4adb-a93b-865700cbe80f",
  "session_id": "1c41b23b-0567-43cc-9be4-04207707f28b"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the two referenced files to gather the necessary information, then create the analysis template.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c41b23b-0567-43cc-9be4-04207707f28b",
  "uuid": "9c6b21d5-b38b-4447-9077-da1dda59eba2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011yVAxmu6R7kbdFXKN4g1B4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11781,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11781
      },
      "output_tokens": 24,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CqW3NVZreVZnEYKdJcQ12B`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
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
  "session_id": "1c41b23b-0567-43cc-9be4-04207707f28b",
  "uuid": "266b56ed-8351-47dc-a688-73d09684ac0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011yVAxmu6R7kbdFXKN4g1B4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11781,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11781
      },
      "output_tokens": 24,
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

_source line 6 · 2026-05-14T07:23:16.834Z_

<details><summary>↩ Tool result · `toolu_01CqW3NVZreVZnEYKdJcQ12B`</summary>

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
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "1c41b23b-0567-43cc-9be4-04207707f28b",
  "uuid": "87454002-e568-411f-82b2-37b924099850",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 7_

读取两个源文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c41b23b-0567-43cc-9be4-04207707f28b",
  "uuid": "c9eab5d8-7e0f-4140-901f-8cd2a69ff86b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZpbLMqhHKaUZHmH1Q3uyM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1348,
      "cache_read_input_tokens": 23622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1348
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Lan118itj7rZcH7RLvbf2k`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "paper_framing.md",
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
  "session_id": "1c41b23b-0567-43cc-9be4-04207707f28b",
  "uuid": "a2975d67-3004-4c22-8ec2-1bad8a41528a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZpbLMqhHKaUZHmH1Q3uyM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1348,
      "cache_read_input_tokens": 23622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1348
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

_source line 9 · 2026-05-14T07:23:23.257Z_

<details><summary>↩ Tool result · `toolu_01Lan118itj7rZcH7RLvbf2k`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n## Target Venue\\n- **Primary: ICLR 2027** (expected deadline ~Sep-Oct 2026) — 充足时间\\n- ~~CoRL 2026~~ — 已放弃 (D011: GPU 未扩容 + 时间不足)\\n\\n## Core Insight\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples encode \\\"which action dimensions are uncertain and how they co-vary\\\" — fundamentally richer information than scalar uncertainty scores. A lightweight learned module conditioned on these structured features can perform dimension-selective action correction: aggressively correcting high-uncertainty DOFs while preserving confident predictions elsewhere.\\n\\n## Core Claims (3 条，均可证伪)\\n1. **Per-DOF conformal features enable dimension-selective correction**: CGS 提取的 40D 结构化 uncertainty 特征（per-DOF std + conformal radius + ellipsoid volume，action_dim=6, H_eff=5）比标量 uncertainty（ReconVLA 的 Euclidean distance）和无 uncertainty conditioning 的残差策略（A2C2 类）提供显著更好的 action correction。\\n   - 验证: MVP (✅ done) + A3 ablation (make-or-break) + A4 ablation + feature importance analysis\\n   - Kill criterion: A3 (CRM without conformal features) 与 full ACR-VLA 差距 <2% → claim 不成立\\n\\n2. **ACI+COC 在分布偏移下维持 calibrated uncertainty，无需外部监督**: Chunk Overlap Consistency 提供自参考覆盖信号，ACI 在线更新 conformal threshold，在任意分布偏移下维持长期平均覆盖保证。\\n   - 验证: COC-success Spearman ρ + ACI 收敛 + ellipsoid volume vs static\\n   - Kill criterion: Spearman ρ < 0.3 AND ellipsoid volume 无 >10% 收窄 → fallback to episode-level ACI\\n\\n3. **ACR-VLA 与 training-time 方法正交互补**: 作为 inference-time 模块可叠加在 SRPO (82.1% LIBERO-Plus SOTA) 上进一步提升。\\n   - 验证: ACR-VLA + SRPO > SRPO alone\\n   - Kill criterion: stacking gain < 2% → claim 降级为\\\"complementary in principle\\\"\\n\\n## Story Spine\\n- **Problem**: Flow-matching VLAs 在标准 benchmark 上接近饱和(97-99%)，但 LIBERO-Plus 暴露了分布偏移下的灾难性鲁棒性缺口。现有方法分别解决检测(SAFE)、样本选择(ReconVLA)、训练时增强(RobustVLA/DiG-Flow/SRPO)，但没有方法在推理时利用结构化 uncertainty 信息主动校正动作。\\n- **Gap**: ReconVLA 用标量 Euclidean distance 做样本选择——丢弃跨维度协方差结构，且无法合成优于任何单个样本的动作。CP-in-the-Loop 通过 planning 闭环但非学习型参数化。UPS 用 CP 做策略门控但不将 conformal 特征作为校正网络输入。A2C2/PLD 学习残差但不利用 calibrated uncertainty features。\\n- **Our angle**: 第一个将多元 conformal 统计量作为学习型校正模块直接输入特征的方法。关键 insight 是 per-DOF conformal 特征编码\\\"哪些维度不确定+跨维度协方差\\\"，使 CRM 能做维度选择性校正。\\n- **Headline result template**: \\\"On LIBERO-Plus, ACR-VLA improves base VLA success by X%, and when stacked on SRPO (82.1%), achieves Y% — demonstrating that inference-time conformal correction provides orthogonal value beyond training-time optimization.\\\"\\n\\n## Anticipated Reviewer Concerns\\n1. **K=10 covariance 估计可靠性** (p/n=0.6): Ledoit-Wolf shrinkage 是标准方案，MVP 已验证 K=10 estimated 仍有效（衰减 ~15pp 但仍显著）。K sensitivity sweep (K=5,10,15,20) 作为 P1 实验。\\n2. **CRM ~250K 参数表达力**: 故意轻量——防 overfitting + 保持推理速度（~3ms overhead）。\\n3. **Synthetic augmentation 覆盖不全** (layout/language 不可覆盖): Honest limitation。ACI 在线适应部分弥补。per-perturbation breakdown 透明呈现。held-out perturbation test (P1) 隔离 conformal features vs augmentation memorization。\\n4. **仿真 only**: CoRL 接受 sim-only，LIBERO-Plus 是 recognized benchmark。\\n5. **DiU 的 single-pass uncertainty 更高效**: DiU 捕获 aleatoric，CGS 捕获 epistemic（分布偏移时升高）。A7 ablation 验证区分。\\n6. **[Dream 新增] 缺外部 baseline 对比**: 必须加 ReconVLA (scalar CP + sample selection) 作为实验 baseline。A3 ablation 近似 A2C2 但需明确说明区别。\\n7. **[Dream 新增] \\\"Conformal\\\" 标签可能误导**: CRM 输出无 formal coverage guarantee。论文需明确说明 CP 用作 feature extractor 而非输出保证。\\n8. **[Dream 新增] per-DOF 优势可能modest**: median dream 显示 per-DOF vs scalar 仅 +2.1%。若真实实验确认此趋势，需 reframe：强调 \\\"conformal-feature-conditioned correction\\\" 整体优势（residual + uncertainty 共同贡献），而非仅 per-DOF vs scalar。\\n\\n## Framing 备选策略（基于 Dream median 观察）\\n如果 per-DOF 优势 < 5%：story 重心从 \\\"per-DOF > scalar\\\" 转向 \\\"structured uncertainty features enable principled correction\\\"（包含 per-DOF + ACI + COC 的完整框架优势）。Core Insight 和 Claim 1 措辞需相应调整。\\n\", \"total_chars\": 3745, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c41b23b-0567-43cc-9be4-04207707f28b",
  "uuid": "da8fc504-eeb0-40e6-9bf6-0607ea4871cf",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — acr-vla-conformal-refinement\\\\n\\\\n## Target Venue\\\\n- **Primary: ICLR 2027** (expected deadline ~Sep-Oct 2026) — 充足时间\\\\n- ~~CoRL 2026~~ — 已放弃 (D011: GPU 未扩容 + 时间不足)\\\\n\\\\n## Core Insight\\\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples encode \\\\\\\"which action dimensions are uncertain and how they co-vary\\\\\\\" — fundamentally richer information than scalar uncertainty scores. A lightweight learned module conditioned on these structured features can perform dimension-selective action correction: aggressively correcting high-uncertainty DOFs while preserving confident predictions elsewhere.\\\\n\\\\n## Core Claims (3 条，均可证伪)\\\\n1. **Per-DOF conformal features enable dimension-selective correction**: CGS 提取的 40D 结构化 uncertainty 特征（per-DOF std + conformal radius + ellipsoid volume，action_dim=6, H_eff=5）比标量 uncertainty（ReconVLA 的 Euclidean distance）和无 uncertainty conditioning 的残差策略（A2C2 类）提供显著更好的 action correction。\\\\n   - 验证: MVP (✅ done) + A3 ablation (make-or-break) + A4 ablation + feature importance analysis\\\\n   - Kill criterion: A3 (CRM without conformal features) 与 full ACR-VLA 差距 <2% → claim 不成立\\\\n\\\\n2. **ACI+COC 在分布偏移下维持 calibrated uncertainty，无需外部监督**: Chunk Overlap Consistency 提供自参考覆盖信号，ACI 在线更新 conformal threshold，在任意分布偏移下维持长期平均覆盖保证。\\\\n   - 验证: COC-success Spearman ρ + ACI 收敛 + ellipsoid volume vs static\\\\n   - Kill criterion: Spearman ρ < 0.3 AND ellipsoid volume 无 >10% 收窄 → fallback to episode-level ACI\\\\n\\\\n3. **ACR-VLA 与 training-time 方法正交互补**: 作为 inference-time 模块可叠加在 SRPO (82.1% LIBERO-Plus SOTA) 上进一步提升。\\\\n   - 验证: ACR-VLA + SRPO > SRPO alone\\\\n   - Kill criterion: stacking gain < 2% → claim 降级为\\\\\\\"complementary in principle\\\\\\\"\\\\n\\\\n## Story Spine\\\\n- **Problem**: Flow-matching VLAs 在标准 benchmark 上接近饱和(97-99%)，但 LIBERO-Plus 暴露了分布偏移下的灾难性鲁棒性缺口。现有方法分别解决检测(SAFE)、样本选择(ReconVLA)、训练时增强(RobustVLA/DiG-Flow/SRPO)，但没有方法在推理时利用结构化 uncertainty 信息主动校正动作。\\\\n- **Gap**: ReconVLA 用标量 Euclidean distance 做样本选择——丢弃跨维度协方差结构，且无法合成优于任何单个样本的动作。CP-in-the-Loop 通过 planning 闭环但非学习型参数化。UPS 用 CP 做策略门控但不将 conformal 特征作为校正网络输入。A2C2/PLD 学习残差但不利用 calibrated uncertainty features。\\\\n- **Our angle**: 第一个将多元 conformal 统计量作为学习型校正模块直接输入特征的方法。关键 insight 是 per-DOF conformal 特征编码\\\\\\\"哪些维度不确定+跨维度协方差\\\\\\\"，使 CRM 能做维度选择性校正。\\\\n- **Headline result template**: \\\\\\\"On LIBERO-Plus, ACR-VLA improves base VLA success by X%, and when stacked on SRPO (82.1%), achieves Y% — demonstrating that inference-time conformal correction provides orthogonal value beyond training-time optimization.\\\\\\\"\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n1. **K=10 covariance 估计可靠性** (p/n=0.6): Ledoit-Wolf shrinkage 是标准方案，MVP 已验证 K=10 estimated 仍有效（衰减 ~15pp 但仍显著）。K sensitivity sweep (K=5,10,15,20) 作为 P1 实验。\\\\n2. **CRM ~250K 参数表达力**: 故意轻量——防 overfitting + 保持推理速度（~3ms overhead）。\\\\n3. **Synthetic augmentation 覆盖不全** (layout/language 不可覆盖): Honest limitation。ACI 在线适应部分弥补。per-perturbation breakdown 透明呈现。held-out perturbation test (P1) 隔离 conformal features vs augmentation memorization。\\\\n4. **仿真 only**: CoRL 接受 sim-only，LIBERO-Plus 是 recognized benchmark。\\\\n5. **DiU 的 single-pass uncertainty 更高效**: DiU 捕获 aleatoric，CGS 捕获 epistemic（分布偏移时升高）。A7 ablation 验证区分。\\\\n6. **[Dream 新增] 缺外部 baseline 对比**: 必须加 ReconVLA (scalar CP + sample selection) 作为实验 baseline。A3 ablation 近似 A2C2 但需明确说明区别。\\\\n7. **[Dream 新增] \\\\\\\"Conformal\\\\\\\" 标签可能误导**: CRM 输出无 formal coverage guarantee。论文需明确说明 CP 用作 feature extractor 而非输出保证。\\\\n8. **[Dream 新增] per-DOF 优势可能modest**: median dream 显示 per-DOF vs scalar 仅 +2.1%。若真实实验确认此趋势，需 reframe：强调 \\\\\\\"conformal-feature-conditioned correction\\\\\\\" 整体优势（residual + uncertainty 共同贡献），而非仅 per-DOF vs scalar。\\\\n\\\\n## Framing 备选策略（基于 Dream median 观察）\\\\n如果 per-DOF 优势 < 5%：story 重心从 \\\\\\\"per-DOF > scalar\\\\\\\" 转向 \\\\\\\"structured uncertainty features enable principled correction\\\\\\\"（包含 per-DOF + ACI + COC 的完整框架优势）。Core Insight 和 Claim 1 措辞需相应调整。\\\\n\\\", \\\"total_chars\\\": 3745, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n## Target Venue\\n- **Primary: ICLR 2027** (expected deadline ~Sep-Oct 2026) — 充足时间\\n- ~~CoRL 2026~~ — 已放弃 (D011: GPU 未扩容 + 时间不足)\\n\\n## Core Insight\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples encode \\\"which action dimensions are uncertain and how they co-vary\\\" — fundamentally richer information than scalar uncertainty scores. A lightweight learned module conditioned on these structured features can perform dimension-selective action correction: aggressively correcting high-uncertainty DOFs while preserving confident predictions elsewhere.\\n\\n## Core Claims (3 条，均可证伪)\\n1. **Per-DOF conformal features enable dimension-selective correction**: CGS 提取的 40D 结构化 uncertainty 特征（per-DOF std + conformal radius + ellipsoid volume，action_dim=6, H_eff=5）比标量 uncertainty（ReconVLA 的 Euclidean distance）和无 uncertainty conditioning 的残差策略（A2C2 类）提供显著更好的 action correction。\\n   - 验证: MVP (✅ done) + A3 ablation (make-or-break) + A4 ablation + feature importance analysis\\n   - Kill criterion: A3 (CRM without conformal features) 与 full ACR-VLA 差距 <2% → claim 不成立\\n\\n2. **ACI+COC 在分布偏移下维持 calibrated uncertainty，无需外部监督**: Chunk Overlap Consistency 提供自参考覆盖信号，ACI 在线更新 conformal threshold，在任意分布偏移下维持长期平均覆盖保证。\\n   - 验证: COC-success Spearman ρ + ACI 收敛 + ellipsoid volume vs static\\n   - Kill criterion: Spearman ρ < 0.3 AND ellipsoid volume 无 >10% 收窄 → fallback to episode-level ACI\\n\\n3. **ACR-VLA 与 training-time 方法正交互补**: 作为 inference-time 模块可叠加在 SRPO (82.1% LIBERO-Plus SOTA) 上进一步提升。\\n   - 验证: ACR-VLA + SRPO > SRPO alone\\n   - Kill criterion: stacking gain < 2% → claim 降级为\\\"complementary in principle\\\"\\n\\n## Story Spine\\n- **Problem**: Flow-matching VLAs 在标准 benchmark 上接近饱和(97-99%)，但 LIBERO-Plus 暴露了分布偏移下的灾难性鲁棒性缺口。现有方法分别解决检测(SAFE)、样本选择(ReconVLA)、训练时增强(RobustVLA/DiG-Flow/SRPO)，但没有方法在推理时利用结构化 uncertainty 信息主动校正动作。\\n- **Gap**: ReconVLA 用标量 Euclidean distance 做样本选择——丢弃跨维度协方差结构，且无法合成优于任何单个样本的动作。CP-in-the-Loop 通过 planning 闭环但非学习型参数化。UPS 用 CP 做策略门控但不将 conformal 特征作为校正网络输入。A2C2/PLD 学习残差但不利用 calibrated uncertainty features。\\n- **Our angle**: 第一个将多元 conformal 统计量作为学习型校正模块直接输入特征的方法。关键 insight 是 per-DOF conformal 特征编码\\\"哪些维度不确定+跨维度协方差\\\"，使 CRM 能做维度选择性校正。\\n- **Headline result template**: \\\"On LIBERO-Plus, ACR-VLA improves base VLA success by X%, and when stacked on SRPO (82.1%), achieves Y% — demonstrating that inference-time conformal correction provides orthogonal value beyond training-time optimization.\\\"\\n\\n## Anticipated Reviewer Concerns\\n1. **K=10 covariance 估计可靠性** (p/n=0.6): Ledoit-Wolf shrinkage 是标准方案，MVP 已验证 K=10 estimated 仍有效（衰减 ~15pp 但仍显著）。K sensitivity sweep (K=5,10,15,20) 作为 P1 实验。\\n2. **CRM ~250K 参数表达力**: 故意轻量——防 overfitting + 保持推理速度（~3ms overhead）。\\n3. **Synthetic augmentation 覆盖不全** (layout/language 不可覆盖): Honest limitation。ACI 在线适应部分弥补。per-perturbation breakdown 透明呈现。held-out perturbation test (P1) 隔离 conformal features vs augmentation memorization。\\n4. **仿真 only**: CoRL 接受 sim-only，LIBERO-Plus 是 recognized benchmark。\\n5. **DiU 的 single-pass uncertainty 更高效**: DiU 捕获 aleatoric，CGS 捕获 epistemic（分布偏移时升高）。A7 ablation 验证区分。\\n6. **[Dream 新增] 缺外部 baseline 对比**: 必须加 ReconVLA (scalar CP + sample selection) 作为实验 baseline。A3 ablation 近似 A2C2 但需明确说明区别。\\n7. **[Dream 新增] \\\"Conformal\\\" 标签可能误导**: CRM 输出无 formal coverage guarantee。论文需明确说明 CP 用作 feature extractor 而非输出保证。\\n8. **[Dream 新增] per-DOF 优势可能modest**: median dream 显示 per-DOF vs scalar 仅 +2.1%。若真实实验确认此趋势，需 reframe：强调 \\\"conformal-feature-conditioned correction\\\" 整体优势（residual + uncertainty 共同贡献），而非仅 per-DOF vs scalar。\\n\\n## Framing 备选策略（基于 Dream median 观察）\\n如果 per-DOF 优势 < 5%：story 重心从 \\\"per-DOF > scalar\\\" 转向 \\\"structured uncertainty features enable principled correction\\\"（包含 per-DOF + ACI + COC 的完整框架优势）。Core Insight 和 Claim 1 措辞需相应调整。\\n\", \"total_chars\": 3745, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01HMKEjo7zi51bqGz6K8eKSS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/competitor_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c41b23b-0567-43cc-9be4-04207707f28b",
  "uuid": "162216f9-f521-4422-b314-e6d82f05e32a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZpbLMqhHKaUZHmH1Q3uyM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1348,
      "cache_read_input_tokens": 23622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1348
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

_source line 11 · 2026-05-14T07:23:24.920Z_

<details><summary>↩ Tool result · `toolu_01HMKEjo7zi51bqGz6K8eKSS`</summary>

````text
1	# ACR-VLA Competitor Analysis
2	
3	> 生成日期: 2026-05-14
4	
5	## 方法对比表
6	
7	| 维度 | ACR-VLA (Ours) | SC-VLA | VLA-Pilot | ACoT-VLA | ReconVLA |
8	|------|---------------|--------|-----------|----------|----------|
9	| **核心机制** | Per-DOF conformal statistics + learned CRM correction | Sparse world imagination + residual RL refinement | MLLM verifier + evolutionary diffusion optimizer | Action chain-of-thought (EAR+IAR) | CQR uncertainty + SMD failure detection |
10	| **方法类别** | Inference-time statistical correction | Inference-time RL refinement | Inference-time MLLM-guided steering | Training-time reasoning augmentation | Inference-time uncertainty gating |
11	| **是否需要额外训练** | CRM 需要训练（~轻量 MLP）；VLA backbone 冻结 | 需要训练 residual policy + auxiliary heads | 不需要（zero-shot plug-and-play） | 需要训练 EAR+IAR 模块 | 不需要（post-hoc calibration） |
12	| **不确定性量化** | Per-DOF (40D) conformal intervals via CGS | 无显式 UQ；用 task progress prediction 间接评估 | 无显式 UQ；MLLM 打分替代 | 无 UQ；通过 CoT reasoning 隐式提升可靠性 | Scalar CQR-based confidence + state-space anomaly |
13	| **统计保证** | ✅ Marginal coverage guarantee via CP; online ACI+COC 维持 | ❌ 无 | ❌ 无 | ❌ 无 | ✅ Marginal coverage via CQR（scalar level） |
14	| **Per-DOF 粒度** | ✅ 40D 维度独立 intervals + selective correction | ❌ 全局 residual adjustment | ❌ 全局 action scoring | ❌ 全局 CoT reasoning | ❌ Scalar aggregation（丢失维度信息） |
15	| **在线适应** | ✅ ACI+COC 在线调阈值 | ✅ Online RL refinement（需交互） | ✅ Iterative steering refinement | ❌ 静态模型 | ❌ Static calibration set |
16	| **推理开销** | K 次 flow-matching 采样 + CGS + CRM（~中等） | Residual policy forward + world model prediction（~低-中） | MLLM reasoning + evolutionary search（~高，2.41s/step） | EAR+IAR forward（~低） | 多次采样 + CQR quantile computation（~中等） |
17	| **主要 benchmark** | LIBERO / LIBERO-Plus | ManiSkill / ARX5 real-world | 6 real-world tasks (Franka Panda) | LIBERO / LIBERO-Plus / VLABench | LIBERO (待确认具体数据) |
18	| **代表性结果** | TBD (实验中) | ManiSkill avg 86%; +9% SR, -16% steps | OOD avg 0.50 vs baseline 0.12-0.19 | LIBERO 98.5%, LIBERO-Plus 84.1% | 改善 failure anticipation（具体 SR 未公开） |
19	
20	## 逐竞品深度分析
21	
22	### SC-VLA (arXiv:2602.21633)
23	
24	**方法概述**：SC-VLA 通过 Sparse World Imagination (SPI) 和 Online Action Refinement (OAR) 实现自我纠正。SPI 在 VLA backbone 上附加辅助预测头，预测当前任务进度和未来轨迹趋势（sparse future states），从而迫使 policy 编码短期物理演化信息。OAR 利用这些预测构建 progress-dependent dense reward，通过 residual RL 在线调整动作。
25	
26	**关键设计决策**：
27	- **Endogenous rewards**：奖励信号完全来自 world imagination 的内部一致性，不依赖外部 dense supervision
28	- **Sparse prediction**：只预测关键未来状态而非完整 world model，降低计算开销
29	- **Residual policy**：保留原始 VLA 输出，仅学习 residual correction
30	
31	**实验结果**：
32	- ManiSkill 平均成功率 86%，PegInsertion 比 π₀/GR00T N1.5 高 28%/10%
33	- 任务吞吐量最高（-16% steps），成功率 +9%
34	- 真实世界 ARX5 实验 +14%
35	
36	**局限性**：
37	1. **需要 RL 训练**：residual policy 和 auxiliary heads 需在目标任务上训练，限制 zero-shot 泛化
38	2. **无统计保证**：correction 基于 RL reward shaping，无法量化不确定性或提供 coverage guarantee
39	3. **全局纠正**：residual 作用在整个 action vector 上，无法区分哪些维度需要纠正
40	4. **未在 LIBERO-Plus 评估**：主要在 ManiSkill 上验证，与 ACR-VLA 的 benchmark 不完全重叠
41	
42	**与 ACR-VLA 的本质区别**：SC-VLA 通过 learned world model + RL 做 action refinement，是 "学出来的纠正"；ACR-VLA 通过 conformal statistics 做 "有保证的纠正"。SC-VLA 无法告诉你 "哪个维度不确定"，也无法在不重新训练的情况下适应新任务。
43	
44	---
45	
46	### VLA-Pilot (arXiv:2511.14178)
47	
48	**方法概述**：VLA-Pilot 采用三阶段 inference-time steering：(1) EPS-CoT (Embodied Policy Steering Chain-of-Thought) 利用 MLLM 推理 task-aligned steering objective 并生成 scoring reward code；(2) Evolutionary Diffusion 从 frozen VLA 采样多个 action proposals，基于 MLLM reward 进行进化优化；(3) Iterative Steering Refinement 将执行后反馈整合到下一轮 EPS-CoT 推理中。
49	
50	**关键设计决策**：
51	- **MLLM as open-world verifier**：利用 VLM 的开放世界推理能力进行动作评估，不限于预定义 reward
52	- **Evolutionary optimization on diffusion latents**：在 diffusion denoising 过程中进行进化搜索，而非简单 best-of-K selection
53	- **Spatial keypoints augmentation**：EPS-CoT 融合 robot end-effector 和 object 的空间关键点信息
54	
55	**实验结果**：
56	- 6 个真实世界任务（Franka Panda），相比 DiVLA baseline 提升 +0.21~+0.31
57	- OOD 场景平均成功率 0.50，vs baseline V-GPS 0.12 / FOREWARN 0.19
58	- Ablation：去掉 EPS-CoT → -8% MSR，去掉 Evolutionary Diffusion → -11% MSR
59	
60	**局限性**：
61	1. **推理延迟极高**：2.41s/step，MLLM reasoning 是瓶颈，不适合实时控制
62	2. **依赖 MLLM 质量**：steering 效果完全取决于 MLLM 的推理质量，无 fallback
63	3. **无统计保证**：MLLM scoring 是启发式的，无法提供 calibrated confidence
64	4. **无 simulation benchmark 对比**：主要在真实世界评估，缺乏 LIBERO 等标准 benchmark 数据
65	
66	**与 ACR-VLA 的本质区别**：VLA-Pilot 用 MLLM 做 "智能评委" 来选/优化动作，是 language-guided 的启发式方法；ACR-VLA 用 conformal prediction 做 distribution-free statistical correction。VLA-Pilot 的优势在 zero-shot OOD 泛化（靠 MLLM 的开放世界知识），劣势在延迟和缺乏理论保证。
67	
68	---
69	
70	### ACoT-VLA (arXiv:2601.11404, CVPR 2026)
71	
72	**方法概述**：ACoT-VLA 提出 Action Chain-of-Thought 范式，将动作推理过程分解为两个互补组件：(1) Explicit Action Reasoner (EAR)——轻量 Transformer 生成粗粒度参考轨迹作为显式动作空间引导；(2) Implicit Action Reasoner (IAR)——通过 cross-attention 从 multimodal representations 中提取 latent action priors。两者共同形成 ACoT conditioning，引导下游 action head 的生成。
73	
74	**关键设计决策**：
75	- **双推理器架构**：EAR 提供 kinematically plausible 的运动学引导，IAR 提供 dense semantic priors
76	- **Training-time integration**：EAR+IAR 在训练时与 VLA 联合优化（LLM backbone 冻结），属于训练阶段方法
77	- **50 demos/task**：仅需少量示教数据
78	
79	**实验结果**：
80	- LIBERO 98.5%，LIBERO-Plus **84.1%**（当前最高之一），VLABench 47.4%
81	- Ablation：仅 EAR → 83.7%，仅 IAR → 80.4%，双路径互补效应显著
82	- AgibotTech 开源，ICRA 2026 AgiBot World Challenge 官方 baseline
83	
84	**局限性**：
85	1. **Training-time 方法**：需要在目标任务上训练 EAR+IAR，不是 plug-and-play
86	2. **无不确定性量化**：CoT reasoning 不输出 confidence，无法识别何时 "不确定"
87	3. **静态模型**：部署后不在线适应，calibration drift 无法处理
88	4. **与 ACR-VLA 互补**：ACoT 提升 VLA 基础能力，ACR-VLA 在其之上提供 safety net
89	
90	**与 ACR-VLA 的本质区别**：ACoT-VLA 是 training-time 的 "思考能力增强"，让 VLA 在生成动作前先做结构化推理。ACR-VLA 是 inference-time 的 "统计安全网"，在 VLA 生成动作后检测和纠正异常。两者正交且互补——可以先用 ACoT 增强 VLA backbone，再套 ACR-VLA 做 conformal correction。
91	
92	---
93	
94	### ReconVLA (arXiv:2604.16677)
95	
96	**方法概述**：ReconVLA 将 conformal prediction 应用于 VLA action token 输出，提供两层保护：(1) CQR-based action uncertainty estimator——对 VLA 的多次采样输出计算 conformalized quantile regression intervals，用于量化动作级不确定性；(2) SMD-based state anomaly detector——监控 latent state distributions 检测 OOD/failure-prone 条件。框架将不确定性分解为 input uncertainty（OOD observations）和 noise uncertainty（generative stochasticity）。
97	
98	**关键设计决策**：
99	- **Post-hoc, no retraining**：完全在 frozen VLA 上 post-hoc 应用，与 ACR-VLA 理念一致
100	- **Scalar CQR**：使用标准 CQR 产生 scalar-level confidence，非 per-DOF
101	- **Static calibration**：使用固定 calibration set，不做在线适应
102	- **Dual uncertainty decomposition**：input vs noise uncertainty 有利于 root cause analysis
103	
104	**局限性**：
105	1. **Scalar uncertainty**：CQR 输出聚合为 scalar 置信度，丢失维度级信息——无法告诉你 "第 3 个关节不确定但其余都好"
106	2. **Static calibration**：calibration set 固定后不更新，distribution shift 下 coverage 可能退化
107	3. **Detection-only vs correction**：ReconVLA 的 UQ 主要用于 failure detection 和 action selection，不做 learned correction（从 K candidates 选而非合成新 action）
108	4. **实验数据有限**：具体 success rate 数据未充分公开，方法验证深度待加强
109	
110	**与 ACR-VLA 的本质区别**：ReconVLA 是 ACR-VLA 最直接的竞争者——同样使用 conformal prediction + frozen VLA。关键差异在三个层面：
111	
112	| 差异维度 | ACR-VLA | ReconVLA |
113	|---------|---------|----------|
114	| UQ 粒度 | Per-DOF 40D intervals (CGS) | Scalar CQR aggregation |
115	| 纠正策略 | Learned CRM 合成新动作 | Sample selection from K candidates |
116	| 在线适应 | ACI+COC 在线阈值调整 | Static calibration |
117	
118	ACR-VLA 在每个维度上都比 ReconVLA 更进一步：更细粒度的 UQ → 更精准的纠正 → 更鲁棒的在线部署。
119	
120	---
121	
122	## ACR-VLA 独特卖点 (USP)
123	
124	### 1. Statistical Guarantees from Conformal Prediction
125	- 提供 distribution-free marginal coverage guarantee，不依赖模型假设
126	- SC-VLA 和 VLA-Pilot 完全无统计保证；ACoT-VLA 无 UQ 能力
127	- ReconVLA 有 CP 保证但仅在 scalar level
128	
129	### 2. Per-DOF Granularity (Dimension-Selective Correction)
130	- 40D 维度独立的 conformal intervals 通过 CGS (Conformalized Gaussian Scoring)
131	- 唯一能做到 "第 3 个关节 ±0.02 rad 不确定，第 7 个关节 ±0.15 rad 很不确定" 的方法
132	- 其他所有方法要么无 UQ（SC-VLA/VLA-Pilot/ACoT-VLA），要么 scalar aggregation（ReconVLA）
133	- **核心论点**：机器人动作是 structured 的（position/orientation/gripper 有不同语义），scalar UQ 会将关键维度的异常淹没在整体均值中
134	
135	### 3. Learned Correction (CRM) vs Sample Selection
136	- CRM 学习在 conformal interval 约束下合成新动作，而非从 K candidates 中选
137	- SC-VLA 用 residual RL 做纠正（但需要环境交互训练）
138	- VLA-Pilot 用 evolutionary search 优化（但依赖 MLLM scoring）
139	- ReconVLA 仅做 sample selection（信息利用率低——只用了 1/K 的采样信息）
140	- **核心论点**：当 K 个样本都不够好时，selection 失效；CRM 可以合成更优动作
141	
142	### 4. Online Adaptation via ACI+COC
143	- Adaptive Conformal Inference + Coverage-Oriented Calibration 实现在线阈值自适应
144	- 处理 deployment 中的 distribution shift，coverage guarantee 在线维持
145	- SC-VLA 需要在线 RL 交互（costly），VLA-Pilot 需要 MLLM 每步推理（slow）
146	- ACoT-VLA 和 ReconVLA 都是 static models，无法在线适应
147	- **核心论点**：real-world deployment 必然遇到 distribution shift，static calibration 的 coverage 会退化
148	
149	### 5. No Additional Training for VLA Backbone
150	- VLA backbone 完全冻结，仅需训练轻量 CRM
151	- SC-VLA 需训练 residual policy + auxiliary heads；ACoT-VLA 需训练 EAR+IAR
152	- VLA-Pilot 和 ReconVLA 同样 training-free（对 backbone），但各有其他局限
153	
154	---
155	
156	## Related Work 定位建议
157	
158	### 推荐的 Related Work 叙事结构
159	
160	**Paragraph 1: VLA Foundation & Robustness Problem**
161	- 引出 VLA 范式 (RT-2, OpenVLA, pi0, SmolVLA) 及其脆弱性问题
162	- 引用 LIBERO-Plus 的 robustness evaluation 结果
163	
164	**Paragraph 2: Training-Time Robustness Methods**
165	- ACoT-VLA (action reasoning)、RobustVLA/SRPO (RL post-training)、DiG-Flow (geometric regularization)
166	- 定位：这些方法提升 VLA 基础能力，但部署后无法适应新分布
167	- 关键句："These training-time approaches are orthogonal and complementary to ACR-VLA's inference-time correction."
168	
169	**Paragraph 3: Inference-Time Correction Methods**
170	- SC-VLA (world model + residual RL)、VLA-Pilot (MLLM steering)、A2C2 (async chunk correction)
171	- 定位：同为 inference-time，但缺乏统计保证和维度粒度
172	- 关键句："While effective, these methods provide no formal uncertainty quantification or coverage guarantees."
173	
174	**Paragraph 4: Uncertainty Quantification for VLAs**
175	- ReconVLA (CQR on action tokens)、SAFE (internal feature CP)、Zollo & Zemel (VLA calibration)
176	- 定位：ReconVLA 是最近的竞争者，但 scalar UQ + static calibration + selection-only
177	- 关键句："ReconVLA applies CQR to VLA action tokens but aggregates to scalar uncertainty, losing the per-DOF granularity critical for structured robot actions."
178	
179	**Paragraph 5: Conformal Prediction in Robotics**
180	- Conformalized Teleoperation (RSS'24)、CP-Loop、CLAPS、SafeDiffCon
181	- 定位：CP 在 robotics 的成功应用，但尚未有 per-DOF multivariate CP + learned correction for VLAs
182	- 关键句："ACR-VLA bridges multivariate conformal prediction with VLA action correction, uniquely combining per-DOF statistical guarantees with learned dimension-selective refinement."
183	
184	### 关键差异化表述（供论文使用）
185	
186	> "Unlike SC-VLA which requires task-specific residual RL training, VLA-Pilot which introduces 2.4s MLLM latency per step, and ReconVLA which aggregates to scalar uncertainty, ACR-VLA provides **per-DOF conformal intervals** with **online coverage guarantees** and **learned correction** that synthesizes improved actions beyond sample selection — all without modifying the frozen VLA backbone."
187	
188	---
189	
190	## 竞争格局总结
191	
192	```
193	                    Training-Time ←────────→ Inference-Time
194	                         │                        │
195	    ACoT-VLA ────────────┤                        │
196	    (CoT reasoning,      │                        │
197	     LIBERO+ 84.1%)      │                        │
198	                         │    SC-VLA ─────────────┤
199	                         │    (Residual RL,        │
200	                         │     needs RL training)  │
201	                         │                        │
202	                         │    VLA-Pilot ──────────┤
203	                         │    (MLLM steering,      │
204	                         │     2.41s latency)      │
205	                         │                        │
206	                         │    ReconVLA ───────────┤
207	                         │    (Scalar CP,          │
208	                         │     detection only)     │
209	                         │                        │
210	                         │    ACR-VLA (Ours) ─────┤
211	                         │    (Per-DOF CP +        │
212	                         │     learned correction  │
213	                         │     + online adaptation)│
214	
215	    Has Statistical Guarantee: ACR-VLA ✅, ReconVLA ✅(scalar), Others ❌
216	    Per-DOF Granularity:       ACR-VLA ✅, Others ❌
217	    Online Adaptation:         ACR-VLA ✅, SC-VLA ✅(RL), VLA-Pilot ✅(MLLM), Others ❌
218	```
219	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c41b23b-0567-43cc-9be4-04207707f28b",
  "uuid": "614dc101-db74-41f8-ac69-8a960f5c299d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/competitor_analysis.md",
      "content": "# ACR-VLA Competitor Analysis\n\n> 生成日期: 2026-05-14\n\n## 方法对比表\n\n| 维度 | ACR-VLA (Ours) | SC-VLA | VLA-Pilot | ACoT-VLA | ReconVLA |\n|------|---------------|--------|-----------|----------|----------|\n| **核心机制** | Per-DOF conformal statistics + learned CRM correction | Sparse world imagination + residual RL refinement | MLLM verifier + evolutionary diffusion optimizer | Action chain-of-thought (EAR+IAR) | CQR uncertainty + SMD failure detection |\n| **方法类别** | Inference-time statistical correction | Inference-time RL refinement | Inference-time MLLM-guided steering | Training-time reasoning augmentation | Inference-time uncertainty gating |\n| **是否需要额外训练** | CRM 需要训练（~轻量 MLP）；VLA backbone 冻结 | 需要训练 residual policy + auxiliary heads | 不需要（zero-shot plug-and-play） | 需要训练 EAR+IAR 模块 | 不需要（post-hoc calibration） |\n| **不确定性量化** | Per-DOF (40D) conformal intervals via CGS | 无显式 UQ；用 task progress prediction 间接评估 | 无显式 UQ；MLLM 打分替代 | 无 UQ；通过 CoT reasoning 隐式提升可靠性 | Scalar CQR-based confidence + state-space anomaly |\n| **统计保证** | ✅ Marginal coverage guarantee via CP; online ACI+COC 维持 | ❌ 无 | ❌ 无 | ❌ 无 | ✅ Marginal coverage via CQR（scalar level） |\n| **Per-DOF 粒度** | ✅ 40D 维度独立 intervals + selective correction | ❌ 全局 residual adjustment | ❌ 全局 action scoring | ❌ 全局 CoT reasoning | ❌ Scalar aggregation（丢失维度信息） |\n| **在线适应** | ✅ ACI+COC 在线调阈值 | ✅ Online RL refinement（需交互） | ✅ Iterative steering refinement | ❌ 静态模型 | ❌ Static calibration set |\n| **推理开销** | K 次 flow-matching 采样 + CGS + CRM（~中等） | Residual policy forward + world model prediction（~低-中） | MLLM reasoning + evolutionary search（~高，2.41s/step） | EAR+IAR forward（~低） | 多次采样 + CQR quantile computation（~中等） |\n| **主要 benchmark** | LIBERO / LIBERO-Plus | ManiSkill / ARX5 real-world | 6 real-world tasks (Franka Panda) | LIBERO / LIBERO-Plus / VLABench | LIBERO (待确认具体数据) |\n| **代表性结果** | TBD (实验中) | ManiSkill avg 86%; +9% SR, -16% steps | OOD avg 0.50 vs baseline 0.12-0.19 | LIBERO 98.5%, LIBERO-Plus 84.1% | 改善 failure anticipation（具体 SR 未公开） |\n\n## 逐竞品深度分析\n\n### SC-VLA (arXiv:2602.21633)\n\n**方法概述**：SC-VLA 通过 Sparse World Imagination (SPI) 和 Online Action Refinement (OAR) 实现自我纠正。SPI 在 VLA backbone 上附加辅助预测头，预测当前任务进度和未来轨迹趋势（sparse future states），从而迫使 policy 编码短期物理演化信息。OAR 利用这些预测构建 progress-dependent dense reward，通过 residual RL 在线调整动作。\n\n**关键设计决策**：\n- **Endogenous rewards**：奖励信号完全来自 world imagination 的内部一致性，不依赖外部 dense supervision\n- **Sparse prediction**：只预测关键未来状态而非完整 world model，降低计算开销\n- **Residual policy**：保留原始 VLA 输出，仅学习 residual correction\n\n**实验结果**：\n- ManiSkill 平均成功率 86%，PegInsertion 比 π₀/GR00T N1.5 高 28%/10%\n- 任务吞吐量最高（-16% steps），成功率 +9%\n- 真实世界 ARX5 实验 +14%\n\n**局限性**：\n1. **需要 RL 训练**：residual policy 和 auxiliary heads 需在目标任务上训练，限制 zero-shot 泛化\n2. **无统计保证**：correction 基于 RL reward shaping，无法量化不确定性或提供 coverage guarantee\n3. **全局纠正**：residual 作用在整个 action vector 上，无法区分哪些维度需要纠正\n4. **未在 LIBERO-Plus 评估**：主要在 ManiSkill 上验证，与 ACR-VLA 的 benchmark 不完全重叠\n\n**与 ACR-VLA 的本质区别**：SC-VLA 通过 learned world model + RL 做 action refinement，是 \"学出来的纠正\"；ACR-VLA 通过 conformal statistics 做 \"有保证的纠正\"。SC-VLA 无法告诉你 \"哪个维度不确定\"，也无法在不重新训练的情况下适应新任务。\n\n---\n\n### VLA-Pilot (arXiv:2511.14178)\n\n**方法概述**：VLA-Pilot 采用三阶段 inference-time steering：(1) EPS-CoT (Embodied Policy Steering Chain-of-Thought) 利用 MLLM 推理 task-aligned steering objective 并生成 scoring reward code；(2) Evolutionary Diffusion 从 frozen VLA 采样多个 action proposals，基于 MLLM reward 进行进化优化；(3) Iterative Steering Refinement 将执行后反馈整合到下一轮 EPS-CoT 推理中。\n\n**关键设计决策**：\n- **MLLM as open-world verifier**：利用 VLM 的开放世界推理能力进行动作评估，不限于预定义 reward\n- **Evolutionary optimization on diffusion latents**：在 diffusion denoising 过程中进行进化搜索，而非简单 best-of-K selection\n- **Spatial keypoints augmentation**：EPS-CoT 融合 robot end-effector 和 object 的空间关键点信息\n\n**实验结果**：\n- 6 个真实世界任务（Franka Panda），相比 DiVLA baseline 提升 +0.21~+0.31\n- OOD 场景平均成功率 0.50，vs baseline V-GPS 0.12 / FOREWARN 0.19\n- Ablation：去掉 EPS-CoT → -8% MSR，去掉 Evolutionary Diffusion → -11% MSR\n\n**局限性**：\n1. **推理延迟极高**：2.41s/step，MLLM reasoning 是瓶颈，不适合实时控制\n2. **依赖 MLLM 质量**：steering 效果完全取决于 MLLM 的推理质量，无 fallback\n3. **无统计保证**：MLLM scoring 是启发式的，无法提供 calibrated confidence\n4. **无 simulation benchmark 对比**：主要在真实世界评估，缺乏 LIBERO 等标准 benchmark 数据\n\n**与 ACR-VLA 的本质区别**：VLA-Pilot 用 MLLM 做 \"智能评委\" 来选/优化动作，是 language-guided 的启发式方法；ACR-VLA 用 conformal prediction 做 distribution-free statistical correction。VLA-Pilot 的优势在 zero-shot OOD 泛化（靠 MLLM 的开放世界知识），劣势在延迟和缺乏理论保证。\n\n---\n\n### ACoT-VLA (arXiv:2601.11404, CVPR 2026)\n\n**方法概述**：ACoT-VLA 提出 Action Chain-of-Thought 范式，将动作推理过程分解为两个互补组件：(1) Explicit Action Reasoner (EAR)——轻量 Transformer 生成粗粒度参考轨迹作为显式动作空间引导；(2) Implicit Action Reasoner (IAR)——通过 cross-attention 从 multimodal representations 中提取 latent action priors。两者共同形成 ACoT conditioning，引导下游 action head 的生成。\n\n**关键设计决策**：\n- **双推理器架构**：EAR 提供 kinematically plausible 的运动学引导，IAR 提供 dense semantic priors\n- **Training-time integration**：EAR+IAR 在训练时与 VLA 联合优化（LLM backbone 冻结），属于训练阶段方法\n- **50 demos/task**：仅需少量示教数据\n\n**实验结果**：\n- LIBERO 98.5%，LIBERO-Plus **84.1%**（当前最高之一），VLABench 47.4%\n- Ablation：仅 EAR → 83.7%，仅 IAR → 80.4%，双路径互补效应显著\n- AgibotTech 开源，ICRA 2026 AgiBot World Challenge 官方 baseline\n\n**局限性**：\n1. **Training-time 方法**：需要在目标任务上训练 EAR+IAR，不是 plug-and-play\n2. **无不确定性量化**：CoT reasoning 不输出 confidence，无法识别何时 \"不确定\"\n3. **静态模型**：部署后不在线适应，calibration drift 无法处理\n4. **与 ACR-VLA 互补**：ACoT 提升 VLA 基础能力，ACR-VLA 在其之上提供 safety net\n\n**与 ACR-VLA 的本质区别**：ACoT-VLA 是 training-time 的 \"思考能力增强\"，让 VLA 在生成动作前先做结构化推理。ACR-VLA 是 inference-time 的 \"统计安全网\"，在 VLA 生成动作后检测和纠正异常。两者正交且互补——可以先用 ACoT 增强 VLA backbone，再套 ACR-VLA 做 conformal correction。\n\n---\n\n### ReconVLA (arXiv:2604.16677)\n\n**方法概述**：ReconVLA 将 conformal prediction 应用于 VLA action token 输出，提供两层保护：(1) CQR-based action uncertainty estimator——对 VLA 的多次采样输出计算 conformalized quantile regression intervals，用于量化动作级不确定性；(2) SMD-based state anomaly detector——监控 latent state distributions 检测 OOD/failure-prone 条件。框架将不确定性分解为 input uncertainty（OOD observations）和 noise uncertainty（generative stochasticity）。\n\n**关键设计决策**：\n- **Post-hoc, no retraining**：完全在 frozen VLA 上 post-hoc 应用，与 ACR-VLA 理念一致\n- **Scalar CQR**：使用标准 CQR 产生 scalar-level confidence，非 per-DOF\n- **Static calibration**：使用固定 calibration set，不做在线适应\n- **Dual uncertainty decomposition**：input vs noise uncertainty 有利于 root cause analysis\n\n**局限性**：\n1. **Scalar uncertainty**：CQR 输出聚合为 scalar 置信度，丢失维度级信息——无法告诉你 \"第 3 个关节不确定但其余都好\"\n2. **Static calibration**：calibration set 固定后不更新，distribution shift 下 coverage 可能退化\n3. **Detection-only vs correction**：ReconVLA 的 UQ 主要用于 failure detection 和 action selection，不做 learned correction（从 K candidates 选而非合成新 action）\n4. **实验数据有限**：具体 success rate 数据未充分公开，方法验证深度待加强\n\n**与 ACR-VLA 的本质区别**：ReconVLA 是 ACR-VLA 最直接的竞争者——同样使用 conformal prediction + frozen VLA。关键差异在三个层面：\n\n| 差异维度 | ACR-VLA | ReconVLA |\n|---------|---------|----------|\n| UQ 粒度 | Per-DOF 40D intervals (CGS) | Scalar CQR aggregation |\n| 纠正策略 | Learned CRM 合成新动作 | Sample selection from K candidates |\n| 在线适应 | ACI+COC 在线阈值调整 | Static calibration |\n\nACR-VLA 在每个维度上都比 ReconVLA 更进一步：更细粒度的 UQ → 更精准的纠正 → 更鲁棒的在线部署。\n\n---\n\n## ACR-VLA 独特卖点 (USP)\n\n### 1. Statistical Guarantees from Conformal Prediction\n- 提供 distribution-free marginal coverage guarantee，不依赖模型假设\n- SC-VLA 和 VLA-Pilot 完全无统计保证；ACoT-VLA 无 UQ 能力\n- ReconVLA 有 CP 保证但仅在 scalar level\n\n### 2. Per-DOF Granularity (Dimension-Selective Correction)\n- 40D 维度独立的 conformal intervals 通过 CGS (Conformalized Gaussian Scoring)\n- 唯一能做到 \"第 3 个关节 ±0.02 rad 不确定，第 7 个关节 ±0.15 rad 很不确定\" 的方法\n- 其他所有方法要么无 UQ（SC-VLA/VLA-Pilot/ACoT-VLA），要么 scalar aggregation（ReconVLA）\n- **核心论点**：机器人动作是 structured 的（position/orientation/gripper 有不同语义），scalar UQ 会将关键维度的异常淹没在整体均值中\n\n### 3. Learned Correction (CRM) vs Sample Selection\n- CRM 学习在 conformal interval 约束下合成新动作，而非从 K candidates 中选\n- SC-VLA 用 residual RL 做纠正（但需要环境交互训练）\n- VLA-Pilot 用 evolutionary search 优化（但依赖 MLLM scoring）\n- ReconVLA 仅做 sample selection（信息利用率低——只用了 1/K 的采样信息）\n- **核心论点**：当 K 个样本都不够好时，selection 失效；CRM 可以合成更优动作\n\n### 4. Online Adaptation via ACI+COC\n- Adaptive Conformal Inference + Coverage-Oriented Calibration 实现在线阈值自适应\n- 处理 deployment 中的 distribution shift，coverage guarantee 在线维持\n- SC-VLA 需要在线 RL 交互（costly），VLA-Pilot 需要 MLLM 每步推理（slow）\n- ACoT-VLA 和 ReconVLA 都是 static models，无法在线适应\n- **核心论点**：real-world deployment 必然遇到 distribution shift，static calibration 的 coverage 会退化\n\n### 5. No Additional Training for VLA Backbone\n- VLA backbone 完全冻结，仅需训练轻量 CRM\n- SC-VLA 需训练 residual policy + auxiliary heads；ACoT-VLA 需训练 EAR+IAR\n- VLA-Pilot 和 ReconVLA 同样 training-free（对 backbone），但各有其他局限\n\n---\n\n## Related Work 定位建议\n\n### 推荐的 Related Work 叙事结构\n\n**Paragraph 1: VLA Foundation & Robustness Problem**\n- 引出 VLA 范式 (RT-2, OpenVLA, pi0, SmolVLA) 及其脆弱性问题\n- 引用 LIBERO-Plus 的 robustness evaluation 结果\n\n**Paragraph 2: Training-Time Robustness Methods**\n- ACoT-VLA (action reasoning)、RobustVLA/SRPO (RL post-training)、DiG-Flow (geometric regularization)\n- 定位：这些方法提升 VLA 基础能力，但部署后无法适应新分布\n- 关键句：\"These training-time approaches are orthogonal and complementary to ACR-VLA's inference-time correction.\"\n\n**Paragraph 3: Inference-Time Correction Methods**\n- SC-VLA (world model + residual RL)、VLA-Pilot (MLLM steering)、A2C2 (async chunk correction)\n- 定位：同为 inference-time，但缺乏统计保证和维度粒度\n- 关键句：\"While effective, these methods provide no formal uncertainty quantification or coverage guarantees.\"\n\n**Paragraph 4: Uncertainty Quantification for VLAs**\n- ReconVLA (CQR on action tokens)、SAFE (internal feature CP)、Zollo & Zemel (VLA calibration)\n- 定位：ReconVLA 是最近的竞争者，但 scalar UQ + static calibration + selection-only\n- 关键句：\"ReconVLA applies CQR to VLA action tokens but aggregates to scalar uncertainty, losing the per-DOF granularity critical for structured robot actions.\"\n\n**Paragraph 5: Conformal Prediction in Robotics**\n- Conformalized Teleoperation (RSS'24)、CP-Loop、CLAPS、SafeDiffCon\n- 定位：CP 在 robotics 的成功应用，但尚未有 per-DOF multivariate CP + learned correction for VLAs\n- 关键句：\"ACR-VLA bridges multivariate conformal prediction with VLA action correction, uniquely combining per-DOF statistical guarantees with learned dimension-selective refinement.\"\n\n### 关键差异化表述（供论文使用）\n\n> \"Unlike SC-VLA which requires task-specific residual RL training, VLA-Pilot which introduces 2.4s MLLM latency per step, and ReconVLA which aggregates to scalar uncertainty, ACR-VLA provides **per-DOF conformal intervals** with **online coverage guarantees** and **learned correction** that synthesizes improved actions beyond sample selection — all without modifying the frozen VLA backbone.\"\n\n---\n\n## 竞争格局总结\n\n```\n                    Training-Time ←────────→ Inference-Time\n                         │                        │\n    ACoT-VLA ────────────┤                        │\n    (CoT reasoning,      │                        │\n     LIBERO+ 84.1%)      │                        │\n                         │    SC-VLA ─────────────┤\n                         │    (Residual RL,        │\n                         │     needs RL training)  │\n                         │                        │\n                         │    VLA-Pilot ──────────┤\n                         │    (MLLM steering,      │\n                         │     2.41s latency)      │\n                         │                        │\n                         │    ReconVLA ───────────┤\n                         │    (Scalar CP,          │\n                         │     detection only)     │\n                         │                        │\n                         │    ACR-VLA (Ours) ─────┤\n                         │    (Per-DOF CP +        │\n                         │     learned correction  │\n                         │     + online adaptation)│\n\n    Has Statistical Guarantee: ACR-VLA ✅, ReconVLA ✅(scalar), Others ❌\n    Per-DOF Granularity:       ACR-VLA ✅, Others ❌\n    Online Adaptation:         ACR-VLA ✅, SC-VLA ✅(RL), VLA-Pilot ✅(MLLM), Others ❌\n```\n",
      "numLines": 219,
      "startLine": 1,
      "totalLines": 219
    }
  }
}
````

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information needed. Let me create the comprehensive comparison analysis template. Key data points:

From competitor_analysis.md:
- ACoT-VLA: LIBERO 98.5%, LIBERO-Plus 84.1%
- SC-VLA: ManiSkill avg 86% (no LIBERO data)
- VLA-Pilot: OOD avg 0.50 (no LIBERO data)
- ReconVLA: specific SR data not fully published

From paper_framing.md:
- 3 core claims to verify
- Framing fallback strategy if per-DOF advantage < 5%


- Kill criteria defined

Now I'm looking at the baseline performance metrics from the background information—VLA-only at 30%, with intermediate results from ACR-VLA, SampleConsensus, and Scalar CRM ranging from 23.3% to 42.9% across the task sets. I can use these to establish the performance thresholds for the template.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c41b23b-0567-43cc-9be4-04207707f28b",
  "uuid": "9dd341d9-42a5-470a-9861-73868acac05c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AUeFrpJ6oDwQdx4LiegPTo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8266,
      "cache_read_input_tokens": 24970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8266
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

_source line 13_

信息收集完毕，开始写模板。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c41b23b-0567-43cc-9be4-04207707f28b",
  "uuid": "d2897347-4626-4dd1-97fa-ec3025575810",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AUeFrpJ6oDwQdx4LiegPTo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8266,
      "cache_read_input_tokens": 24970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8266
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

_source line 14_

<details open><summary>🔧 Tool call — Write · `toolu_018VzrMiKGoAsWNyum84CuUD`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/spatial_comparison_template.md",
  "content": "# LIBERO Spatial Benchmark — 完整对比分析框架\n\n> 生成日期: 2026-05-14\n> 状态: 模板（待实验完成后填入最终数据）\n\n---\n\n## 1. 六路对比总表\n\n| Method | Type | K | Overall SR | 备注 |\n|--------|------|---|-----------|------|\n| VLA-only (baseline) | Single inference | 1 | **30.0%** (30/100) | 已完成 |\n| VLA Mean Action | Multi-sample mean | 10 | **___%** | eval-vla-mean-spatial |\n| SampleConsensus (ReconVLA-style) | Scalar Euclidean argmin | 10 | **___%** | eval-reconvla-spatial-v3 |\n| Scalar CRM | 3D scalar uncertainty + CRM | 10 | **___%** | eval-scalar-unc-spatial |\n| ACR-VLA (K=5) | Per-DOF CRM | 5 | **___%** | eval-k5-spatial |\n| ACR-VLA (K=10) | Per-DOF CRM | 10 | **___%** | eval-acr-spatial-v2 |\n| **竞品参考** | | | | |\n| ACoT-VLA (CVPR'26) | Training-time CoT | - | 98.5% (LIBERO) | 非 LIBERO-Plus; training-time 方法 |\n| SRPO | Training-time RL | - | 82.1% (LIBERO-Plus) | 不同 benchmark split |\n\n### Per-Task 详细数据\n\n| Task | Difficulty | VLA K=1 | VLA Mean K=10 | SampleCons K=10 | Scalar CRM K=10 | ACR K=5 | ACR K=10 |\n|------|-----------|---------|---------------|-----------------|-----------------|---------|----------|\n| bowl_next_ramekin | Easy | 100% | | | | | |\n| bowl_next_cookie_box | Easy | 90% | | | | | |\n| bowl_between_plate | Easy | 60% | | | | | |\n| bowl_cookie_box | Medium | 20% | | | | | |\n| bowl_next_plate | Medium | 30% | | | | | |\n| bowl_table_center | Hard | 0% | | | | | |\n| bowl_top_drawer | Hard | 0% | | | | | |\n| bowl_on_ramekin | Hard | 0% | | | | | |\n| bowl_on_stove | Hard | 0% | | | | | |\n| bowl_wooden_cabinet | Hard | 0% | | | | | |\n\n难度分级: Easy (baseline ≥50%), Medium (20-49%), Hard (baseline <20%)\n\n---\n\n## 2. 关键分析维度\n\n### 2.1 Overall Success Rate Ranking\n\n```\nRank | Method            | SR   | Δ vs baseline\n-----|-------------------|------|-------------\n  1  |                   |      |\n  2  |                   |      |\n  3  |                   |      |\n  4  |                   |      |\n  5  |                   |      |\n  6  | VLA-only K=1      | 30%  | —\n```\n\n### 2.2 Per-Task Correction 获益/受损分析\n\n**从 correction 获益的 tasks** (method > baseline):\n| Task | Baseline | Best Method | Δ | 可能原因 |\n|------|----------|-------------|---|---------|\n| | | | | |\n\n**被 correction 伤害的 tasks** (method < baseline):\n| Task | Baseline | Worst Method | Δ | 可能原因 |\n|------|----------|--------------|---|---------|\n| | | | | |\n\n关键问题: correction 是否伤害了 easy tasks（过度纠正）而只在 hard tasks 上帮助？\n\n### 2.3 分层分析: Easy / Medium / Hard\n\n| Difficulty | # Tasks | VLA K=1 Avg | VLA Mean K=10 | SampleCons K=10 | Scalar CRM K=10 | ACR K=5 | ACR K=10 |\n|-----------|---------|-------------|---------------|-----------------|-----------------|---------|----------|\n| Easy (≥50%) | 3 | 83.3% | | | | | |\n| Medium (20-49%) | 2 | 25.0% | | | | | |\n| Hard (<20%) | 5 | 0.0% | | | | | |\n\n核心观察模板:\n- Easy tasks: correction 应保持高性能（不伤害），如果大幅下降说明 CRM 过度校正\n- Medium tasks: correction 最有潜力提升的区间\n- Hard tasks: baseline 为 0%，任何提升都是 pure gain；但如果仍为 0%，说明问题不在 action noise 而在 task comprehension\n\n### 2.4 Per-DOF vs Scalar 直接对比\n\n| Metric | ACR-VLA (Per-DOF) K=10 | Scalar CRM K=10 | Δ | p-value |\n|--------|------------------------|-----------------|---|---------|\n| Overall SR | | | | |\n| Easy Avg | | | | |\n| Medium Avg | | | | |\n| Hard Avg | | | | |\n| # Tasks improved vs baseline | | | | |\n| # Tasks degraded vs baseline | | | | |\n\n如果 Δ < 5%: 参考 paper_framing.md 备选策略 — story 重心从 \"per-DOF > scalar\" 转向 \"structured uncertainty features enable principled correction\"。\n\n### 2.5 K Sensitivity (K=5 vs K=10)\n\n| Metric | ACR K=5 | ACR K=10 | Δ |\n|--------|---------|----------|---|\n| Overall SR | | | |\n| Easy Avg | | | |\n| Medium Avg | | | |\n| Hard Avg | | | |\n\n预期: K=10 > K=5（更多样本 → 更好的 covariance 估计），但 paper_framing 提到 K=10 vs K=5 衰减约 15pp。\n如果 K=5 ≈ K=10: 实际效率优势，可强调 \"仅需 K=5 即可获得大部分收益\"。\n\n### 2.6 Multi-Sampling Contribution Isolation\n\n| | K=1 (no sampling) | Mean K=10 | Best Method K=10 |\n|--|-------------------|-----------|------------------|\n| Overall SR | 30.0% | | |\n| Δ from K=1 | — | | |\n\n分解:\n- **Multi-sampling gain** = Mean K=10 - VLA K=1 (纯粹来自多次采样 + 平均)\n- **Correction gain** = Best CRM K=10 - Mean K=10 (来自 learned correction 的增量)\n- **Selection gain** = SampleConsensus K=10 - Mean K=10 (来自 sample selection 的增量)\n\n如果 multi-sampling gain 占主导: 说明多次采样本身已很有价值，CRM 的增量贡献需要诚实报告。\n\n---\n\n## 3. Claim 验证 Checklist\n\n### Claim 1: Per-DOF > Scalar\n\n> \"Per-DOF conformal features enable dimension-selective correction... 比标量 uncertainty 提供显著更好的 action correction\"\n\n| 验证项 | 数据源 | 结果 | Pass? |\n|--------|--------|------|-------|\n| ACR-VLA K=10 > Scalar CRM K=10 (overall) | eval-acr-spatial-v2 vs eval-scalar-unc-spatial | ___% vs ___% | |\n| 差距 ≥ 2% (kill criterion from paper_framing) | 同上 | Δ = ___% | |\n| Per-task: ACR 在多数 tasks 上优于 scalar | 逐 task 对比 | _/10 tasks | |\n| Per-DOF 在 hard tasks 上优势更大 | 分层对比 | | |\n\nKill criterion: Δ < 2% → Claim 1 不成立，需 reframe。\n\n### Claim 2: ACR-VLA > Baseline\n\n> \"ACR-VLA improves base VLA success by X%\"\n\n| 验证项 | 数据源 | 结果 | Pass? |\n|--------|--------|------|-------|\n| ACR-VLA K=10 > VLA K=1 (overall) | eval-acr-spatial-v2 vs baseline | ___% vs 30% | |\n| ACR-VLA 不伤害 easy tasks | per-task 对比 | Easy avg: ___% vs 83.3% | |\n| ACR-VLA 改善 hard tasks | per-task 对比 | Hard avg: ___% vs 0.0% | |\n\n**中间检查 RED FLAG**: 上次中间结果 ACR-VLA 23.3% < baseline 30%。如果最终结果确认，这是 critical failure。\n\n### Claim 3: Learned CRM > Sample Selection\n\n> \"CRM 可以合成更优动作... selection 失效时 CRM 可以合成更好的动作\"\n\n| 验证项 | 数据源 | 结果 | Pass? |\n|--------|--------|------|-------|\n| ACR-VLA K=10 > SampleConsensus K=10 | eval-acr-spatial-v2 vs eval-reconvla-spatial-v3 | ___% vs ___% | |\n| Per-task: ACR 在多数 tasks 上优于 SC | 逐 task 对比 | _/10 tasks | |\n| Hard tasks: CRM 合成优于 best sample | 分层对比 | | |\n\n**中间检查 RED FLAG**: 上次中间结果 SampleConsensus 42.9% >> ACR-VLA 23.3%。如果确认，Claim 3 完全反转。\n\n---\n\n## 4. 应急 Framing 方案\n\n### 场景 A: ACR-VLA < Baseline (当前中间结果趋势)\n\n**根因假设 (需逐条排查)**:\n1. CRM 过拟合训练分布，在 spatial tasks 上产生有害校正\n2. Conformal intervals 在 spatial 特定 tasks 上 miscalibrated\n3. CGS covariance 估计在某些 DOF 组合上不稳定\n4. 训练数据与 spatial benchmark 的分布偏移太大\n\n**Framing 策略**:\n- 不能 claim \"ACR-VLA improves spatial tasks\"\n- 转向: \"ACR-VLA 的 correction magnitude 需要 task-specific 校准\" — 分析 CRM 在哪些 tasks 上帮助/伤害\n- 如果 SampleConsensus > all: 论文 narrative 转为 \"multi-sample uncertainty 本身有价值，learned correction 是 harder problem than sample selection\"\n- 如果 VLA Mean > VLA K=1: 至少可以 claim \"multi-sampling improves robustness\"\n- 最坏情况: spatial 作为 \"challenging case study\"，重心放在其他 benchmarks (LIBERO-Plus)\n\n### 场景 B: Per-DOF ≈ Scalar (Δ < 5%)\n\n参考 paper_framing.md:\n- Story 重心从 \"per-DOF > scalar\" 转向 \"structured uncertainty features enable principled correction\"\n- 强调整体框架（residual + uncertainty + online adaptation）的组合优势\n- Per-DOF 作为 \"principled design choice\" 而非 \"empirically dominant\"\n\n### 场景 C: SampleConsensus 最高\n\n**这是最棘手的场景** — 直接挑战 \"learned correction > sample selection\" 的核心 claim。\n\n策略:\n1. 分析 SampleConsensus 赢在哪些 tasks — 是否是 \"easy tasks 本来就好，selection 不伤害\" 的 artifacts?\n2. 在 hard tasks 上如果 CRM 仍优于 SC → \"CRM 在高难度场景下更优，SC 在简单场景靠不犯错取胜\"\n3. 检查 SampleConsensus 是否 benefit from multi-sampling (vs Mean K=10) — 如果 SC ≈ Mean，说明 selection 策略本身不重要\n4. 最后手段: \"在 spatial benchmark 上 sample quality 已足够好，selection 即够用；在更 challenging 的 LIBERO-Plus 上 CRM 的合成能力才显现价值\"\n\n### 场景 D: 全部 methods < Baseline\n\n说明 K-sampling + 任何 aggregation 都不如单次推理 → 根本性问题:\n- 可能 flow-matching 的最佳样本不在 mean/mode 附近\n- 可能 spatial tasks 的 action distribution 高度 multimodal，averaging/correction 都有害\n- 这会是 honest negative result，仍有发表价值但需要完全重新 frame\n\n---\n\n## 5. 竞品对比 Context\n\n### LIBERO 标准 benchmark 参考值\n\n| Method | LIBERO (标准) | LIBERO-Plus | 来源 |\n|--------|--------------|-------------|------|\n| ACoT-VLA | **98.5%** | **84.1%** | arXiv:2601.11404, CVPR'26 |\n| SRPO | — | **82.1%** | paper_framing.md |\n| SC-VLA | — (ManiSkill 86%) | — | arXiv:2602.21633 |\n| VLA-Pilot | — | — (real-world OOD 50%) | arXiv:2511.14178 |\n| ReconVLA | — (具体 SR 未公开) | — | arXiv:2604.16677 |\n\n**重要注意**: \n- 竞品数字大多来自不同 benchmark split (LIBERO vs LIBERO-Plus vs LIBERO-Spatial)，不可直接比较\n- ACoT-VLA 98.5% 是标准 LIBERO (含 4 个 suite)，我们只跑了 spatial suite (10 tasks)\n- 我们的 baseline VLA 本身性能较低 (30% on spatial)，说明 base model 能力是主要瓶颈\n\n### 定位策略\n\n- **vs ACoT-VLA**: \"Training-time 方法，与 ACR-VLA 正交互补。ACR-VLA 可叠加在更强的 base VLA 上\"\n- **vs ReconVLA**: \"同为 inference-time CP 方法，但 scalar UQ + selection vs per-DOF UQ + learned correction\"\n- **vs SC-VLA**: \"需要 task-specific RL 训练，我们是 plug-and-play\"\n- **不要试图在 absolute numbers 上与 ACoT-VLA 98.5% 比较** — base VLA 不同，benchmark split 不同\n\n---\n\n## 6. 数据填写指南\n\n当 5 个 eval 实验完成后:\n\n1. **收集数据**: 从各 eval 目录读取 per-task success rate\n2. **填写第 1 节总表和 per-task 表**\n3. **计算第 2 节各分析维度**\n4. **逐条检查第 3 节 claim checklist** — 每条标注 Pass/Fail\n5. **根据第 4 节确定 framing** — 选择匹配的场景\n6. **输出最终分析报告** → `artifacts/spatial_final_analysis.md`\n\n---\n\n## Appendix: 实验 ID 映射\n\n| 实验 ID | Method | Config |\n|---------|--------|--------|\n| eval-acr-spatial-v2 | ACR-VLA per-DOF CRM | K=10 |\n| eval-reconvla-spatial-v3 | SampleConsensus | K=10, scalar Euclidean argmin |\n| eval-scalar-unc-spatial | Scalar CRM | K=10, 3D uncertainty |\n| eval-k5-spatial | ACR-VLA | K=5 |\n| eval-vla-mean-spatial | VLA Mean Action | K=10, no conformal |\n| eval-spatial-v7-full | VLA-only baseline | K=1 |\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c41b23b-0567-43cc-9be4-04207707f28b",
  "uuid": "f2d83cf7-5c02-4448-89d7-313bc8bf9d99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AUeFrpJ6oDwQdx4LiegPTo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8266,
      "cache_read_input_tokens": 24970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8266
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

_source line 15 · 2026-05-14T07:25:06.764Z_

<details><summary>↩ Tool result · `toolu_018VzrMiKGoAsWNyum84CuUD`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/spatial_comparison_template.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c41b23b-0567-43cc-9be4-04207707f28b",
  "uuid": "b00a20cb-78a9-4579-b652-753088c4084e",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/spatial_comparison_template.md",
    "content": "# LIBERO Spatial Benchmark — 完整对比分析框架\n\n> 生成日期: 2026-05-14\n> 状态: 模板（待实验完成后填入最终数据）\n\n---\n\n## 1. 六路对比总表\n\n| Method | Type | K | Overall SR | 备注 |\n|--------|------|---|-----------|------|\n| VLA-only (baseline) | Single inference | 1 | **30.0%** (30/100) | 已完成 |\n| VLA Mean Action | Multi-sample mean | 10 | **___%** | eval-vla-mean-spatial |\n| SampleConsensus (ReconVLA-style) | Scalar Euclidean argmin | 10 | **___%** | eval-reconvla-spatial-v3 |\n| Scalar CRM | 3D scalar uncertainty + CRM | 10 | **___%** | eval-scalar-unc-spatial |\n| ACR-VLA (K=5) | Per-DOF CRM | 5 | **___%** | eval-k5-spatial |\n| ACR-VLA (K=10) | Per-DOF CRM | 10 | **___%** | eval-acr-spatial-v2 |\n| **竞品参考** | | | | |\n| ACoT-VLA (CVPR'26) | Training-time CoT | - | 98.5% (LIBERO) | 非 LIBERO-Plus; training-time 方法 |\n| SRPO | Training-time RL | - | 82.1% (LIBERO-Plus) | 不同 benchmark split |\n\n### Per-Task 详细数据\n\n| Task | Difficulty | VLA K=1 | VLA Mean K=10 | SampleCons K=10 | Scalar CRM K=10 | ACR K=5 | ACR K=10 |\n|------|-----------|---------|---------------|-----------------|-----------------|---------|----------|\n| bowl_next_ramekin | Easy | 100% | | | | | |\n| bowl_next_cookie_box | Easy | 90% | | | | | |\n| bowl_between_plate | Easy | 60% | | | | | |\n| bowl_cookie_box | Medium | 20% | | | | | |\n| bowl_next_plate | Medium | 30% | | | | | |\n| bowl_table_center | Hard | 0% | | | | | |\n| bowl_top_drawer | Hard | 0% | | | | | |\n| bowl_on_ramekin | Hard | 0% | | | | | |\n| bowl_on_stove | Hard | 0% | | | | | |\n| bowl_wooden_cabinet | Hard | 0% | | | | | |\n\n难度分级: Easy (baseline ≥50%), Medium (20-49%), Hard (baseline <20%)\n\n---\n\n## 2. 关键分析维度\n\n### 2.1 Overall Success Rate Ranking\n\n```\nRank | Method            | SR   | Δ vs baseline\n-----|-------------------|------|-------------\n  1  |                   |      |\n  2  |                   |      |\n  3  |                   |      |\n  4  |                   |      |\n  5  |                   |      |\n  6  | VLA-only K=1      | 30%  | —\n```\n\n### 2.2 Per-Task Correction 获益/受损分析\n\n**从 correction 获益的 tasks** (method > baseline):\n| Task | Baseline | Best Method | Δ | 可能原因 |\n|------|----------|-------------|---|---------|\n| | | | | |\n\n**被 correction 伤害的 tasks** (method < baseline):\n| Task | Baseline | Worst Method | Δ | 可能原因 |\n|------|----------|--------------|---|---------|\n| | | | | |\n\n关键问题: correction 是否伤害了 easy tasks（过度纠正）而只在 hard tasks 上帮助？\n\n### 2.3 分层分析: Easy / Medium / Hard\n\n| Difficulty | # Tasks | VLA K=1 Avg | VLA Mean K=10 | SampleCons K=10 | Scalar CRM K=10 | ACR K=5 | ACR K=10 |\n|-----------|---------|-------------|---------------|-----------------|-----------------|---------|----------|\n| Easy (≥50%) | 3 | 83.3% | | | | | |\n| Medium (20-49%) | 2 | 25.0% | | | | | |\n| Hard (<20%) | 5 | 0.0% | | | | | |\n\n核心观察模板:\n- Easy tasks: correction 应保持高性能（不伤害），如果大幅下降说明 CRM 过度校正\n- Medium tasks: correction 最有潜力提升的区间\n- Hard tasks: baseline 为 0%，任何提升都是 pure gain；但如果仍为 0%，说明问题不在 action noise 而在 task comprehension\n\n### 2.4 Per-DOF vs Scalar 直接对比\n\n| Metric | ACR-VLA (Per-DOF) K=10 | Scalar CRM K=10 | Δ | p-value |\n|--------|------------------------|-----------------|---|---------|\n| Overall SR | | | | |\n| Easy Avg | | | | |\n| Medium Avg | | | | |\n| Hard Avg | | | | |\n| # Tasks improved vs baseline | | | | |\n| # Tasks degraded vs baseline | | | | |\n\n如果 Δ < 5%: 参考 paper_framing.md 备选策略 — story 重心从 \"per-DOF > scalar\" 转向 \"structured uncertainty features enable principled correction\"。\n\n### 2.5 K Sensitivity (K=5 vs K=10)\n\n| Metric | ACR K=5 | ACR K=10 | Δ |\n|--------|---------|----------|---|\n| Overall SR | | | |\n| Easy Avg | | | |\n| Medium Avg | | | |\n| Hard Avg | | | |\n\n预期: K=10 > K=5（更多样本 → 更好的 covariance 估计），但 paper_framing 提到 K=10 vs K=5 衰减约 15pp。\n如果 K=5 ≈ K=10: 实际效率优势，可强调 \"仅需 K=5 即可获得大部分收益\"。\n\n### 2.6 Multi-Sampling Contribution Isolation\n\n| | K=1 (no sampling) | Mean K=10 | Best Method K=10 |\n|--|-------------------|-----------|------------------|\n| Overall SR | 30.0% | | |\n| Δ from K=1 | — | | |\n\n分解:\n- **Multi-sampling gain** = Mean K=10 - VLA K=1 (纯粹来自多次采样 + 平均)\n- **Correction gain** = Best CRM K=10 - Mean K=10 (来自 learned correction 的增量)\n- **Selection gain** = SampleConsensus K=10 - Mean K=10 (来自 sample selection 的增量)\n\n如果 multi-sampling gain 占主导: 说明多次采样本身已很有价值，CRM 的增量贡献需要诚实报告。\n\n---\n\n## 3. Claim 验证 Checklist\n\n### Claim 1: Per-DOF > Scalar\n\n> \"Per-DOF conformal features enable dimension-selective correction... 比标量 uncertainty 提供显著更好的 action correction\"\n\n| 验证项 | 数据源 | 结果 | Pass? |\n|--------|--------|------|-------|\n| ACR-VLA K=10 > Scalar CRM K=10 (overall) | eval-acr-spatial-v2 vs eval-scalar-unc-spatial | ___% vs ___% | |\n| 差距 ≥ 2% (kill criterion from paper_framing) | 同上 | Δ = ___% | |\n| Per-task: ACR 在多数 tasks 上优于 scalar | 逐 task 对比 | _/10 tasks | |\n| Per-DOF 在 hard tasks 上优势更大 | 分层对比 | | |\n\nKill criterion: Δ < 2% → Claim 1 不成立，需 reframe。\n\n### Claim 2: ACR-VLA > Baseline\n\n> \"ACR-VLA improves base VLA success by X%\"\n\n| 验证项 | 数据源 | 结果 | Pass? |\n|--------|--------|------|-------|\n| ACR-VLA K=10 > VLA K=1 (overall) | eval-acr-spatial-v2 vs baseline | ___% vs 30% | |\n| ACR-VLA 不伤害 easy tasks | per-task 对比 | Easy avg: ___% vs 83.3% | |\n| ACR-VLA 改善 hard tasks | per-task 对比 | Hard avg: ___% vs 0.0% | |\n\n**中间检查 RED FLAG**: 上次中间结果 ACR-VLA 23.3% < baseline 30%。如果最终结果确认，这是 critical failure。\n\n### Claim 3: Learned CRM > Sample Selection\n\n> \"CRM 可以合成更优动作... selection 失效时 CRM 可以合成更好的动作\"\n\n| 验证项 | 数据源 | 结果 | Pass? |\n|--------|--------|------|-------|\n| ACR-VLA K=10 > SampleConsensus K=10 | eval-acr-spatial-v2 vs eval-reconvla-spatial-v3 | ___% vs ___% | |\n| Per-task: ACR 在多数 tasks 上优于 SC | 逐 task 对比 | _/10 tasks | |\n| Hard tasks: CRM 合成优于 best sample | 分层对比 | | |\n\n**中间检查 RED FLAG**: 上次中间结果 SampleConsensus 42.9% >> ACR-VLA 23.3%。如果确认，Claim 3 完全反转。\n\n---\n\n## 4. 应急 Framing 方案\n\n### 场景 A: ACR-VLA < Baseline (当前中间结果趋势)\n\n**根因假设 (需逐条排查)**:\n1. CRM 过拟合训练分布，在 spatial tasks 上产生有害校正\n2. Conformal intervals 在 spatial 特定 tasks 上 miscalibrated\n3. CGS covariance 估计在某些 DOF 组合上不稳定\n4. 训练数据与 spatial benchmark 的分布偏移太大\n\n**Framing 策略**:\n- 不能 claim \"ACR-VLA improves spatial tasks\"\n- 转向: \"ACR-VLA 的 correction magnitude 需要 task-specific 校准\" — 分析 CRM 在哪些 tasks 上帮助/伤害\n- 如果 SampleConsensus > all: 论文 narrative 转为 \"multi-sample uncertainty 本身有价值，learned correction 是 harder problem than sample selection\"\n- 如果 VLA Mean > VLA K=1: 至少可以 claim \"multi-sampling improves robustness\"\n- 最坏情况: spatial 作为 \"challenging case study\"，重心放在其他 benchmarks (LIBERO-Plus)\n\n### 场景 B: Per-DOF ≈ Scalar (Δ < 5%)\n\n参考 paper_framing.md:\n- Story 重心从 \"per-DOF > scalar\" 转向 \"structured uncertainty features enable principled correction\"\n- 强调整体框架（residual + uncertainty + online adaptation）的组合优势\n- Per-DOF 作为 \"principled design choice\" 而非 \"empirically dominant\"\n\n### 场景 C: SampleConsensus 最高\n\n**这是最棘手的场景** — 直接挑战 \"learned correction > sample selection\" 的核心 claim。\n\n策略:\n1. 分析 SampleConsensus 赢在哪些 tasks — 是否是 \"easy tasks 本来就好，selection 不伤害\" 的 artifacts?\n2. 在 hard tasks 上如果 CRM 仍优于 SC → \"CRM 在高难度场景下更优，SC 在简单场景靠不犯错取胜\"\n3. 检查 SampleConsensus 是否 benefit from multi-sampling (vs Mean K=10) — 如果 SC ≈ Mean，说明 selection 策略本身不重要\n4. 最后手段: \"在 spatial benchmark 上 sample quality 已足够好，selection 即够用；在更 challenging 的 LIBERO-Plus 上 CRM 的合成能力才显现价值\"\n\n### 场景 D: 全部 methods < Baseline\n\n说明 K-sampling + 任何 aggregation 都不如单次推理 → 根本性问题:\n- 可能 flow-matching 的最佳样本不在 mean/mode 附近\n- 可能 spatial tasks 的 action distribution 高度 multimodal，averaging/correction 都有害\n- 这会是 honest negative result，仍有发表价值但需要完全重新 frame\n\n---\n\n## 5. 竞品对比 Context\n\n### LIBERO 标准 benchmark 参考值\n\n| Method | LIBERO (标准) | LIBERO-Plus | 来源 |\n|--------|--------------|-------------|------|\n| ACoT-VLA | **98.5%** | **84.1%** | arXiv:2601.11404, CVPR'26 |\n| SRPO | — | **82.1%** | paper_framing.md |\n| SC-VLA | — (ManiSkill 86%) | — | arXiv:2602.21633 |\n| VLA-Pilot | — | — (real-world OOD 50%) | arXiv:2511.14178 |\n| ReconVLA | — (具体 SR 未公开) | — | arXiv:2604.16677 |\n\n**重要注意**: \n- 竞品数字大多来自不同 benchmark split (LIBERO vs LIBERO-Plus vs LIBERO-Spatial)，不可直接比较\n- ACoT-VLA 98.5% 是标准 LIBERO (含 4 个 suite)，我们只跑了 spatial suite (10 tasks)\n- 我们的 baseline VLA 本身性能较低 (30% on spatial)，说明 base model 能力是主要瓶颈\n\n### 定位策略\n\n- **vs ACoT-VLA**: \"Training-time 方法，与 ACR-VLA 正交互补。ACR-VLA 可叠加在更强的 base VLA 上\"\n- **vs ReconVLA**: \"同为 inference-time CP 方法，但 scalar UQ + selection vs per-DOF UQ + learned correction\"\n- **vs SC-VLA**: \"需要 task-specific RL 训练，我们是 plug-and-play\"\n- **不要试图在 absolute numbers 上与 ACoT-VLA 98.5% 比较** — base VLA 不同，benchmark split 不同\n\n---\n\n## 6. 数据填写指南\n\n当 5 个 eval 实验完成后:\n\n1. **收集数据**: 从各 eval 目录读取 per-task success rate\n2. **填写第 1 节总表和 per-task 表**\n3. **计算第 2 节各分析维度**\n4. **逐条检查第 3 节 claim checklist** — 每条标注 Pass/Fail\n5. **根据第 4 节确定 framing** — 选择匹配的场景\n6. **输出最终分析报告** → `artifacts/spatial_final_analysis.md`\n\n---\n\n## Appendix: 实验 ID 映射\n\n| 实验 ID | Method | Config |\n|---------|--------|--------|\n| eval-acr-spatial-v2 | ACR-VLA per-DOF CRM | K=10 |\n| eval-reconvla-spatial-v3 | SampleConsensus | K=10, scalar Euclidean argmin |\n| eval-scalar-unc-spatial | Scalar CRM | K=10, 3D uncertainty |\n| eval-k5-spatial | ACR-VLA | K=5 |\n| eval-vla-mean-spatial | VLA Mean Action | K=10, no conformal |\n| eval-spatial-v7-full | VLA-only baseline | K=1 |\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01Uju52RhjygjJyBJQvL1txP`</summary>

```json
{
  "name": "Spatial Benchmark Comparison Analysis Template",
  "type": "report",
  "description": "LIBERO Spatial 六路对比分析框架：总表 + per-task 分层分析 + claim 验证 checklist + 应急 framing 方案（含 ACR-VLA < baseline 场景）",
  "project": "acr-vla-conformal-refinement",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/spatial_comparison_template.md",
  "tags": [
    "spatial",
    "evaluation",
    "comparison",
    "analysis-template"
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
  "session_id": "1c41b23b-0567-43cc-9be4-04207707f28b",
  "uuid": "3910ac13-03bd-4678-a72c-e23defdbb577",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JdTyv6cqTZcM6X5jbPyW56",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4858,
      "cache_read_input_tokens": 33236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4858
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

### Tool result

_source line 17 · 2026-05-14T07:25:16.544Z_

<details><summary>↩ Tool result · `toolu_01Uju52RhjygjJyBJQvL1txP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_887a52\", \"name\": \"Spatial Benchmark Comparison Analysis Template\", \"type\": \"report\", \"description\": \"LIBERO Spatial 六路对比分析框架：总表 + per-task 分层分析 + claim 验证 checklist + 应急 framing 方案（含 ACR-VLA < baseline 场景）\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/report/spatial_comparison_template.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T07:25:16.504247+00:00\", \"tags\": [\"spatial\", \"evaluation\", \"comparison\", \"analysis-template\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c41b23b-0567-43cc-9be4-04207707f28b",
  "uuid": "68a1ce54-50df-484a-8469-b6f3fa449169",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260514_887a52\\\", \\\"name\\\": \\\"Spatial Benchmark Comparison Analysis Template\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"LIBERO Spatial 六路对比分析框架：总表 + per-task 分层分析 + claim 验证 checklist + 应急 framing 方案（含 ACR-VLA < baseline 场景）\\\", \\\"path\\\": \\\"projects/acr-vla-conformal-refinement/artifacts/_project/report/spatial_comparison_template.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"acr-vla-conformal-refinement\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-14T07:25:16.504247+00:00\\\", \\\"tags\\\": [\\\"spatial\\\", \\\"evaluation\\\", \\\"comparison\\\", \\\"analysis-template\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_887a52\", \"name\": \"Spatial Benchmark Comparison Analysis Template\", \"type\": \"report\", \"description\": \"LIBERO Spatial 六路对比分析框架：总表 + per-task 分层分析 + claim 验证 checklist + 应急 framing 方案（含 ACR-VLA < baseline 场景）\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/report/spatial_comparison_template.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T07:25:16.504247+00:00\", \"tags\": [\"spatial\", \"evaluation\", \"comparison\", \"analysis-template\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 18_

模板已写入并注册 (`art_20260514_887a52`)。

核心内容:
- **第1节**: 六路对比总表 + 10 tasks per-task 表，按 Easy/Medium/Hard 分级
- **第2节**: 6 个分析维度 — overall ranking、获益/受损分析、分层分析、per-DOF vs scalar、K sensitivity、multi-sampling contribution isolation
- **第3节**: 3 条 claim 逐条验证 checklist，含 kill criteria
- **第4节**: 4 个应急场景的 framing 策略 — 重点覆盖了当前最危险的 "ACR-VLA < baseline" 和 "SampleConsensus 最高" 两个场景
- **第5节**: 竞品参考值（ACoT-VLA 98.5%/84.1%, SRPO 82.1%）及不可直接比较的原因说明

等 5 个 eval 完成后按第 6 节指南填数据即可产出最终分析。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c41b23b-0567-43cc-9be4-04207707f28b",
  "uuid": "3f603700-579c-4e97-b2ab-43590d305f2a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SNiXhphctVfzm47H27PGWB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 601,
      "cache_read_input_tokens": 38094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 601
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

_source line 19_

模板已写入并注册 (`art_20260514_887a52`)。

核心内容:
- **第1节**: 六路对比总表 + 10 tasks per-task 表，按 Easy/Medium/Hard 分级
- **第2节**: 6 个分析维度 — overall ranking、获益/受损分析、分层分析、per-DOF vs scalar、K sensitivity、multi-sampling contribution isolation
- **第3节**: 3 条 claim 逐条验证 checklist，含 kill criteria
- **第4节**: 4 个应急场景的 framing 策略 — 重点覆盖了当前最危险的 "ACR-VLA < baseline" 和 "SampleConsensus 最高" 两个场景
- **第5节**: 竞品参考值（ACoT-VLA 98.5%/84.1%, SRPO 82.1%）及不可直接比较的原因说明

等 5 个 eval 完成后按第 6 节指南填数据即可产出最终分析。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 134291,
  "duration_api_ms": 136082,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "1c41b23b-0567-43cc-9be4-04207707f28b",
  "total_cost_usd": 0.37858400000000003,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 26854,
    "cache_read_input_tokens": 131763,
    "output_tokens": 5726,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 26854,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 291,
        "cache_read_input_tokens": 38094,
        "cache_creation_input_tokens": 601,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 601
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1600,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00167,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 5726,
      "cacheReadInputTokens": 131763,
      "cacheCreationInputTokens": 26854,
      "webSearchRequests": 0,
      "costUSD": 0.376914,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a339280b-b976-4854-a8a8-2b5d4f2f1dbc"
}
```

</details>

---
