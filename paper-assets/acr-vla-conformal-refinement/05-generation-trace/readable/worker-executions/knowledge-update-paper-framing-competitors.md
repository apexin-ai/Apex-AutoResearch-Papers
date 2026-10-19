# knowledge update paper framing competitors

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/workers/worker_knowledge_update-paper-framing-competitors_20260514T074639.log`
- **Structured JSON:** [`e57e51dda2309261b0cd.json`](../../sessions/e5/e57e51dda2309261b0cd.json)

## Before a recorded user message

17 recorded events

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
  "session_id": "3cc157a6-29df-4dea-b36e-dd31bdc80a06",
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
  "uuid": "b9721f45-be5c-4971-9cd8-2759441cf604",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1778762400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "834b6ec1-8e81-4144-81f3-397c62272f03",
  "session_id": "3cc157a6-29df-4dea-b36e-dd31bdc80a06"
}
```

---

### Assistant

_source line 4_

I'll start by reading the current paper_framing.md and the competitor analysis artifact in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3cc157a6-29df-4dea-b36e-dd31bdc80a06",
  "uuid": "7aba5231-97a4-4907-8f05-1b4bfa43e943",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXYrjecjaQCrPYNZMDykPL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11322,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11322
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RysCGFSwHzqsQw63with68`</summary>

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
  "session_id": "3cc157a6-29df-4dea-b36e-dd31bdc80a06",
  "uuid": "7d4d320c-d7ec-45a5-b132-5f788f4f9e4e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXYrjecjaQCrPYNZMDykPL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11322,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11322
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

_source line 6 · 2026-05-14T07:46:50.627Z_

<details><summary>↩ Tool result · `toolu_01RysCGFSwHzqsQw63with68`</summary>

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
  "session_id": "3cc157a6-29df-4dea-b36e-dd31bdc80a06",
  "uuid": "12d26181-9635-4913-8d6c-168f96d4d0d1",
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
Now let me read both files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3cc157a6-29df-4dea-b36e-dd31bdc80a06",
  "uuid": "1b31d9b1-d3c8-415b-8a18-cbfd1bdcb965",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xT2yQja6dJPjQqj2Yn4d9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 721,
      "cache_read_input_tokens": 23163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 721
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

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011fJ2yHiGmSdJeSnL515EUR`</summary>

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
  "session_id": "3cc157a6-29df-4dea-b36e-dd31bdc80a06",
  "uuid": "a17a0bd4-ccee-424f-ae90-d4399804304d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xT2yQja6dJPjQqj2Yn4d9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 721,
      "cache_read_input_tokens": 23163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 721
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

_source line 9 · 2026-05-14T07:46:55.082Z_

<details><summary>↩ Tool result · `toolu_011fJ2yHiGmSdJeSnL515EUR`</summary>

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
  "session_id": "3cc157a6-29df-4dea-b36e-dd31bdc80a06",
  "uuid": "d702f4fb-c5c8-4139-bf11-ac6c0dcc32f3",
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

<details open><summary>🔧 Tool call — Read · `toolu_01KKmcNtxv6U1conA2Y4SWvm`</summary>

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
  "session_id": "3cc157a6-29df-4dea-b36e-dd31bdc80a06",
  "uuid": "ba6ba2ae-4cea-48f7-b22e-c4a937428d5d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xT2yQja6dJPjQqj2Yn4d9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 721,
      "cache_read_input_tokens": 23163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 721
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

_source line 11 · 2026-05-14T07:46:56.605Z_

<details><summary>↩ Tool result · `toolu_01KKmcNtxv6U1conA2Y4SWvm`</summary>

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
  "session_id": "3cc157a6-29df-4dea-b36e-dd31bdc80a06",
  "uuid": "3f5cbb4b-b7ba-4306-8cbf-f8d2f73d69fd",
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
Now I have both files. Let me update the paper_framing.md according to the task requirements:

1. Update the "Story Spine → Gap" section with competitor comparisons (SC-VLA sample consensus, VLA-Pilot uncertainty-guided planning, ACoT-VLA 84.1% LIBERO SOTA)
2. Add a new "## Competitive Landscape" section with the four competitors
3. Clearly position ACR-VLA's differentiation

I need to be careful to:
- Not modify Core Claims and Kill Criteria
- Not modify Target Venue


- Keep existing Framing alternatives unchanged
- Be objective and accurate about competitors

Looking at the current "Gap" section, I can see it discusses how ReconVLA uses scalar Euclidean distance for sample selection which loses cross-dimensional covariance structure, CP-in-the-Loop uses planning but isn't learning-based, and UPS gates with conformal predictions but doesn't feed those features into the correction network. I'll need to integrate the competitor comparisons here while maintaining this analytical structure.

Now I'm expanding the Gap section to include SC-VLA, VLA-Pilot, and ACoT-VLA alongside the existing comparisons, then adding a dedicated Competitive Landscape section that maps out how our approach differs from each method across key dimensions like uncertainty quantification, sample selection, and learning paradigms.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3cc157a6-29df-4dea-b36e-dd31bdc80a06",
  "uuid": "a04f7fb1-2d19-47ee-9e26-3a86615ed621",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPyRj1G1V9NVN3Yv66ZhsN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8280,
      "cache_read_input_tokens": 23884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8280
      },
      "output_tokens": 11,
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

Now I'll update paper_framing.md with the competitor positioning. I need to update the Gap section and add a Competitive Landscape section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3cc157a6-29df-4dea-b36e-dd31bdc80a06",
  "uuid": "63fb66fb-bcec-4e69-944f-25b6fd88d345",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPyRj1G1V9NVN3Yv66ZhsN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8280,
      "cache_read_input_tokens": 23884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8280
      },
      "output_tokens": 11,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_0144UqXjQXEBjxABPf2H4rKe`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "paper_framing.md",
  "content": "# Paper Framing — acr-vla-conformal-refinement\n\n## Target Venue\n- **Primary: ICLR 2027** (expected deadline ~Sep-Oct 2026) — 充足时间\n- ~~CoRL 2026~~ — 已放弃 (D011: GPU 未扩容 + 时间不足)\n\n## Core Insight\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples encode \"which action dimensions are uncertain and how they co-vary\" — fundamentally richer information than scalar uncertainty scores. A lightweight learned module conditioned on these structured features can perform dimension-selective action correction: aggressively correcting high-uncertainty DOFs while preserving confident predictions elsewhere.\n\n## Core Claims (3 条，均可证伪)\n1. **Per-DOF conformal features enable dimension-selective correction**: CGS 提取的 40D 结构化 uncertainty 特征（per-DOF std + conformal radius + ellipsoid volume，action_dim=6, H_eff=5）比标量 uncertainty（ReconVLA 的 Euclidean distance）和无 uncertainty conditioning 的残差策略（A2C2 类）提供显著更好的 action correction。\n   - 验证: MVP (✅ done) + A3 ablation (make-or-break) + A4 ablation + feature importance analysis\n   - Kill criterion: A3 (CRM without conformal features) 与 full ACR-VLA 差距 <2% → claim 不成立\n\n2. **ACI+COC 在分布偏移下维持 calibrated uncertainty，无需外部监督**: Chunk Overlap Consistency 提供自参考覆盖信号，ACI 在线更新 conformal threshold，在任意分布偏移下维持长期平均覆盖保证。\n   - 验证: COC-success Spearman ρ + ACI 收敛 + ellipsoid volume vs static\n   - Kill criterion: Spearman ρ < 0.3 AND ellipsoid volume 无 >10% 收窄 → fallback to episode-level ACI\n\n3. **ACR-VLA 与 training-time 方法正交互补**: 作为 inference-time 模块可叠加在 SRPO (82.1% LIBERO-Plus SOTA) 上进一步提升。\n   - 验证: ACR-VLA + SRPO > SRPO alone\n   - Kill criterion: stacking gain < 2% → claim 降级为\"complementary in principle\"\n\n## Story Spine\n- **Problem**: Flow-matching VLAs 在标准 benchmark 上接近饱和(97-99%)，但 LIBERO-Plus 暴露了分布偏移下的灾难性鲁棒性缺口。现有方法分别解决检测(SAFE)、样本选择(ReconVLA)、训练时增强(RobustVLA/DiG-Flow/SRPO)，但没有方法在推理时利用结构化 uncertainty 信息主动校正动作。\n- **Gap**: 现有 inference-time 方法各有根本性局限：ReconVLA 用标量 CQR 做样本选择——丢弃跨维度协方差结构，且无法合成优于任何单个样本的动作；SC-VLA 通过 sparse world imagination + residual RL 在线纠正，但需要任务级 RL 训练且无统计保证，纠正作用在全局 action vector 上无维度选择性；VLA-Pilot 用 MLLM 做开放世界 action scoring + evolutionary search，推理延迟 2.41s/step 且依赖启发式评分无 calibrated confidence。Training-time 方面，ACoT-VLA 通过 action chain-of-thought 达到 LIBERO-Plus 84.1% SOTA，但属于静态训练方法，部署后无法在线适应分布偏移。所有现有方法均未将 per-DOF conformal statistics 作为 learned correction 的输入特征。\n- **Our angle**: 第一个将多元 conformal 统计量作为学习型校正模块直接输入特征的方法。关键 insight 是 per-DOF conformal 特征编码\"哪些维度不确定+跨维度协方差\"，使 CRM 能做维度选择性校正。\n- **Headline result template**: \"On LIBERO-Plus, ACR-VLA improves base VLA success by X%, and when stacked on SRPO (82.1%), achieves Y% — demonstrating that inference-time conformal correction provides orthogonal value beyond training-time optimization.\"\n\n## Competitive Landscape\n\n### ReconVLA — 最直接竞品\nPost-hoc conformal prediction on frozen VLA（理念最接近 ACR-VLA）。使用 CQR 产生 scalar-level confidence + SMD state anomaly detection，用于 failure detection 和 action selection（从 K candidates 中选最佳）。\n\n**关键差异**：(1) Scalar CQR aggregation 丢失维度信息，无法区分 \"哪个关节不确定\"；(2) Sample selection 而非 learned correction——当 K 个样本都不好时 selection 失效；(3) Static calibration set 不做在线适应，distribution shift 下 coverage 退化。ACR-VLA 在 UQ 粒度（40D vs scalar）、纠正策略（CRM synthesis vs selection）、在线适应（ACI+COC vs static）三个维度均更进一步。\n\n### SC-VLA — Inference-time RL refinement\nSparse World Imagination (SPI) + Online Action Refinement (OAR)。在 VLA backbone 上附加辅助预测头预测任务进度和未来轨迹趋势，构建 endogenous reward 驱动 residual RL 在线调整动作。ManiSkill 平均 86%，+9% SR。\n\n**关键差异**：(1) 需要任务级 RL 训练（residual policy + auxiliary heads），非 plug-and-play；(2) 无统计保证和不确定性量化；(3) Residual 作用在整个 action vector 上，无维度选择性；(4) 未在 LIBERO-Plus 评估。ACR-VLA 的 SampleConsensus baseline 近似模拟此方法的 sample consensus 思路。\n\n### VLA-Pilot — MLLM-guided steering\nMLLM verifier + evolutionary diffusion optimizer，三阶段 inference-time steering。利用 VLM 开放世界推理能力做 action scoring。OOD 场景成功率 0.50 vs baseline 0.12-0.19。\n\n**关键差异**：(1) 推理延迟 2.41s/step，不适合实时控制；(2) 依赖 MLLM 质量，scoring 为启发式方法无 calibrated confidence；(3) 无统计保证；(4) 未在 LIBERO 标准 benchmark 评估。优势在 zero-shot OOD 泛化（靠 MLLM 开放世界知识）。\n\n### ACoT-VLA — Training-time SOTA (CVPR 2026)\nAction Chain-of-Thought：EAR (Explicit Action Reasoner) 生成粗粒度参考轨迹 + IAR (Implicit Action Reasoner) 提取 latent action priors，联合训练引导 action head。LIBERO 98.5%，LIBERO-Plus 84.1%（当前 SOTA 之一）。\n\n**关键差异**：(1) Training-time 方法，需在目标任务上训练 EAR+IAR；(2) 无不确定性量化，无法识别何时 \"不确定\"；(3) 静态模型，部署后不在线适应。**与 ACR-VLA 正交互补**——ACoT 增强 VLA 基础能力，ACR-VLA 在其之上提供 inference-time statistical safety net。\n\n### ACR-VLA 差异化定位\n唯一将 multivariate conformal statistics（per-DOF intervals + ellipsoid volume + cross-DOF covariance structure）作为 learned correction module (CRM) 直接输入特征的方法。核心差异化组合：**Per-DOF statistical guarantees + Learned dimension-selective correction + Online coverage adaptation**——三者缺一不可，现有方法均未同时具备。\n\n## Anticipated Reviewer Concerns\n1. **K=10 covariance 估计可靠性** (p/n=0.6): Ledoit-Wolf shrinkage 是标准方案，MVP 已验证 K=10 estimated 仍有效（衰减 ~15pp 但仍显著）。K sensitivity sweep (K=5,10,15,20) 作为 P1 实验。\n2. **CRM ~250K 参数表达力**: 故意轻量——防 overfitting + 保持推理速度（~3ms overhead）。\n3. **Synthetic augmentation 覆盖不全** (layout/language 不可覆盖): Honest limitation。ACI 在线适应部分弥补。per-perturbation breakdown 透明呈现。held-out perturbation test (P1) 隔离 conformal features vs augmentation memorization。\n4. **仿真 only**: CoRL 接受 sim-only，LIBERO-Plus 是 recognized benchmark。\n5. **DiU 的 single-pass uncertainty 更高效**: DiU 捕获 aleatoric，CGS 捕获 epistemic（分布偏移时升高）。A7 ablation 验证区分。\n6. **[Dream 新增] 缺外部 baseline 对比**: 必须加 ReconVLA (scalar CP + sample selection) 作为实验 baseline。A3 ablation 近似 A2C2 但需明确说明区别。\n7. **[Dream 新增] \"Conformal\" 标签可能误导**: CRM 输出无 formal coverage guarantee。论文需明确说明 CP 用作 feature extractor 而非输出保证。\n8. **[Dream 新增] per-DOF 优势可能modest**: median dream 显示 per-DOF vs scalar 仅 +2.1%。若真实实验确认此趋势，需 reframe：强调 \"conformal-feature-conditioned correction\" 整体优势（residual + uncertainty 共同贡献），而非仅 per-DOF vs scalar。\n\n## Framing 备选策略（基于 Dream median 观察）\n如果 per-DOF 优势 < 5%：story 重心从 \"per-DOF > scalar\" 转向 \"structured uncertainty features enable principled correction\"（包含 per-DOF + ACI + COC 的完整框架优势）。Core Insight 和 Claim 1 措辞需相应调整。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3cc157a6-29df-4dea-b36e-dd31bdc80a06",
  "uuid": "7320ff2d-9486-4fb4-8d53-50a387f3eda4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPyRj1G1V9NVN3Yv66ZhsN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8280,
      "cache_read_input_tokens": 23884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8280
      },
      "output_tokens": 11,
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

_source line 15 · 2026-05-14T07:48:29.451Z_

<details><summary>↩ Tool result · `toolu_0144UqXjQXEBjxABPf2H4rKe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3cc157a6-29df-4dea-b36e-dd31bdc80a06",
  "uuid": "58ba53ca-1f8c-48be-b9e0-19cefb2bf782",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\\\", \\\"saved\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

更新完成。主要变更：

1. **Story Spine → Gap**：从原来仅提 ReconVLA/CP-in-the-Loop/UPS/A2C2 扩展为包含四个主要竞品（ReconVLA scalar CQR + selection only、SC-VLA residual RL 无统计保证、VLA-Pilot 2.41s 延迟启发式评分、ACoT-VLA 84.1% 但 training-time 静态模型），以"所有方法均未将 per-DOF conformal statistics 作为 learned correction 输入"收束。

2. **新增 Competitive Landscape section**：四个竞品逐一分析关键差异，末尾明确 ACR-VLA 差异化定位——唯一同时具备 per-DOF statistical guarantees + learned dimension-selective correction + online coverage adaptation 的方法。

Core Claims、Kill Criteria、Target Venue、Framing 备选策略均未修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3cc157a6-29df-4dea-b36e-dd31bdc80a06",
  "uuid": "49de5c93-881e-4159-abcb-b4383374ca95",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VMVYpsSZLiznXex2o4VVm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3610,
      "cache_read_input_tokens": 32164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3610
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

_source line 17_

更新完成。主要变更：

1. **Story Spine → Gap**：从原来仅提 ReconVLA/CP-in-the-Loop/UPS/A2C2 扩展为包含四个主要竞品（ReconVLA scalar CQR + selection only、SC-VLA residual RL 无统计保证、VLA-Pilot 2.41s 延迟启发式评分、ACoT-VLA 84.1% 但 training-time 静态模型），以"所有方法均未将 per-DOF conformal statistics 作为 learned correction 输入"收束。

2. **新增 Competitive Landscape section**：四个竞品逐一分析关键差异，末尾明确 ACR-VLA 差异化定位——唯一同时具备 per-DOF statistical guarantees + learned dimension-selective correction + online coverage adaptation 的方法。

Core Claims、Kill Criteria、Target Venue、Framing 备选策略均未修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 113468,
  "duration_api_ms": 114427,
  "num_turns": 5,
  "stop_reason": "end_turn",
  "session_id": "3cc157a6-29df-4dea-b36e-dd31bdc80a06",
  "total_cost_usd": 0.29969525,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 23933,
    "cache_read_input_tokens": 91052,
    "output_tokens": 4132,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 23933,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 268,
        "cache_read_input_tokens": 32164,
        "cache_creation_input_tokens": 3610,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3610
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1158,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001248,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 4132,
      "cacheReadInputTokens": 91052,
      "cacheCreationInputTokens": 23933,
      "webSearchRequests": 0,
      "costUSD": 0.29844725,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f196313d-ca0a-41d5-843c-ceea58b141ed"
}
```

</details>

---
