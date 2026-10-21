# paper update framing negative blocks

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/workers/worker_paper_update_framing_negative_blocks_20260525T091315.log`
- **Structured JSON:** [`05d9524db9dc656c5883.json`](../../sessions/05/05d9524db9dc656c5883.json)

## Before a recorded user message

21 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf",
  "session_id": "1e30124b-e11f-468d-b9f7-1ea1e18990b4",
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
  "uuid": "44333c1d-b733-4a9d-9307-9022c72962c7",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/memory/"
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
    "resetsAt": 1779717600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "c578efbc-683b-45a8-9231-2b527a8e4d9f",
  "session_id": "1e30124b-e11f-468d-b9f7-1ea1e18990b4"
}
```

---

### Assistant

_source line 4_

我来读取当前的 paper_framing.md 内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e30124b-e11f-468d-b9f7-1ea1e18990b4",
  "uuid": "f87e044e-a130-4842-99c4-507249f54b45",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011onfSCaWFB6LUvX3oA8xnH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11960,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11960
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DYXDZnoQV8j8PEXkYXD1QN`</summary>

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
  "session_id": "1e30124b-e11f-468d-b9f7-1ea1e18990b4",
  "uuid": "1f18fc7c-41b3-4ffb-a49d-4c37f36e0a50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011onfSCaWFB6LUvX3oA8xnH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11960,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11960
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

_source line 6 · 2026-05-25T09:13:28.283Z_

<details><summary>↩ Tool result · `toolu_01DYXDZnoQV8j8PEXkYXD1QN`</summary>

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
  "session_id": "1e30124b-e11f-468d-b9f7-1ea1e18990b4",
  "uuid": "3cafa288-a15e-463f-a0ae-62323cb577be",
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

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me read the current paper_framing.md file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e30124b-e11f-468d-b9f7-1ea1e18990b4",
  "uuid": "00445fbd-bf59-4ec9-a323-06937a78fb59",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016j11oMQnYhFLXhhGtDARfA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 23801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 454
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

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0138717HkCVNFCaiv1EJ5dMj`</summary>

```json
{
  "project": "diff_collision_sdf",
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
  "session_id": "1e30124b-e11f-468d-b9f7-1ea1e18990b4",
  "uuid": "94deb02c-2317-4dc5-9850-6fcffdeb34c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016j11oMQnYhFLXhhGtDARfA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 23801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 454
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

_source line 9 · 2026-05-25T09:13:33.588Z_

<details><summary>↩ Tool result · `toolu_0138717HkCVNFCaiv1EJ5dMj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md\", \"content\": \"# ColliForce-VLA Paper Framing\\n\\n> 维护者: Director | 最后更新: 2026-05-24 12:30 UTC | Reviewer 预审反馈：补 LoRA 中间场景叙事 + Claim 4 措辞升级\\n\\n## Core Insight\\n\\n当前 VLA safety 评估存在系统性缺陷：collision avoidance rate (CAR) 被 action collapse 严重污染，导致 \\\"安全\\\" 指标虚高。我们通过大规模实证分析（39 个实验, 5000+ episodes）揭示三个相互关联的问题，并提出 displacement-filtered CAR 作为修正指标。\\n\\n## Working Title\\n\\n\\\"The Safety Illusion: How Action Collapse Contaminates Collision Avoidance Metrics in Vision-Language-Action Models\\\"\\n\\n> 注：Title scope 已按 Reviewer Report #26 建议收窄——不再 claim 覆盖 \\\"all SDF methods\\\"，聚焦 metric contamination 这一更可防御的贡献\\n\\n## Core Claims\\n\\n### Claim 1: Fake Safety (Primary — 证据强度 ★★★★★)\\nCAR 指标被 action collapse 严重污染。在 SafeLIBERO benchmark 上，A1 (SDF auxiliary loss) 的 91.5% CAR 中 99.6% 是 fake safe（robot displacement < 1μm）。\\\"Collision-free\\\" ≠ \\\"collision-avoiding\\\"。\\n\\n**证据**: 800 episodes A1 per-episode displacement 分析; 200 episodes baseline 对比; Pi0.5 56/56 safe episodes displacement ≈ 0\\n\\n**贡献**: 提出 displacement-filtered CAR (real_CAR) 作为修正指标\\n\\n### Claim 2: Task Capability vs Safety Anti-correlation (Secondary — 证据强度 ★★★)\\n更强的 base model 完成更多任务但碰撞更多。Pi0.5 (TSR=74.7%) vs Pi0 (TSR≈0%): 能力越强 → 运动越多 → 碰撞越多。\\n\\n**证据**: Pi0.5 3-seed eval (TSR=74.7±1.5%, CAR=26.8±1.6%) vs Pi0 baseline (TSR≈0%, CAR=82%)\\n\\n**限制**: 仅 2 个 model families, Pi0 的 \\\"高 CAR\\\" 来自 action collapse 而非安全。Reviewer 建议降级为 observation, 不 claim 因果关系。\\n\\n### Claim 3: EE-only SDF Structural Limitation (Supporting — 证据强度 ★★★★)\\nEnd-effector-only SDF 在 action space 的碰撞避免存在结构性缺陷：SDF gradient 推 EE 远离障碍物但导致 arm body 扫过障碍物。\\n\\n**证据**: 3 组 GT SDF oracle (adaptive alpha, fixed alpha, feature-space) 均劣于 baseline; spatial vs object 碰撞部位分析; obstacle 高度/体积与碰撞率的单调关系\\n\\n**限制**: \\\"EE-only 不够\\\" 是 expected result; 缺乏 full-body SDF 对照\\n\\n### Claim 4: SDF Auxiliary Loss Effectiveness on Strong VLA (Pending — 取决于实验)\\n在能力充分的 VLA (Pi0.5) 上，SDF auxiliary training loss 能否产生真实的碰撞避免行为？\\n\\n**状态**: 3-seed × 2-lambda 训练中, 预计 5/24 18:00 出结果\\n\\n**Framing 策略 (Reviewer #37)**：即使最优结果也定位为 **\\\"analysis paper with positive method contribution\\\"**，而非纯 method paper。原因：analysis 贡献 scope-proof（适用所有 VLA），method 贡献 scope-limited（1-2 models, 2-4 tasks）。SDF aux loss 作为 secondary proof-of-concept，证明 \\\"问题可解决\\\" 以验证 analysis 框架的价值。\\n\\n**Claim 措辞上限** (按 Reviewer 预审升级，基于 10K +30pp 证据): \\\"Training-time SDF auxiliary loss yields substantial collision avoidance improvement (+Xpp displacement-filtered CAR, frozen_rate=0%) on Pi0.5, confirming that geometric supervision effectively addresses action-collapse-contaminated safety in capable VLAs — at a moderate task performance cost (TSR: 74.7%→Y%)\\\"（必须包含 TSR tradeoff；禁区: SOTA / consistently outperforms / general solution）\\n\\n**如果成功 (CAR ≥ 33%)**: 升级为 method contribution (secondary)\\n**如果失败**: 额外 negative evidence, 强化 structural insight\\n\\n**泛化扩展计划 (Reviewer #37, 提升接受率)**：\\n- 必须: spatial_bowl 第 2 task 训练（代码准备中）→ 接受率 40% → 55-65%\\n- 应该做: OpenVLA zero-shot eval 验证 fake safety 在第 3 model 上存在（仅 inference）\\n- 应该做: 4-point lambda 曲线 (0, 0.005, 0.01, 0.1) 支持 \\\"sweet spot\\\" claim\\n- Nice-to-have: SafeLIBERO 4 suite 各 1 task\\n\\n## Anticipated Reviewer Concerns\\n\\n### R1 (最致命): Generalizability\\n\\\"仅在 SafeLIBERO + Pi0 系列上验证, 凭什么说 fake safety 是普遍问题?\\\"\\n→ **应对**: (1) 2+ tasks (object_pudding + spatial_bowl, 代码准备中); (2) 3+ models 的 analysis (Pi0 + Pi0.5 已有, 加 OpenVLA zero-shot eval); (3) 收窄 claim scope + discussion 中做机制分析\\n→ **接受率估算** (Reviewer #37): 1 task ~40% / 2 tasks+2 model ~55-65% / 4 tasks+3 model ~65-75%\\n\\n### R2: Novelty of EE-only limitation\\n\\\"任何了解机器人运动学的人都知道肘部会碰\\\"\\n→ **应对**: 强调定量分析 (arm-body vs EE 碰撞比例量化 + oracle 排除其他解释) 而非定性观察; 作为 supporting claim 而非 primary\\n\\n### R3: No positive result\\n\\\"告诉我什么不 work 但没告诉我什么 work\\\"\\n→ **应对**: real_CAR 指标是 positive 工具贡献; Pi0.5+A1 如果成功也是正面结果; diagnostic framework 有方法论价值\\n\\n### R4: Action collapse is trivial\\n\\\"Undertrained Pi0 的 action collapse 不是 safety 特有的, 是训练不足的自然结果\\\"\\n→ **应对**: 必须在论文中承认这一点; 但指出即使原因 trivial, metric contamination 的后果 non-trivial — 后续工作可能基于被污染的 CAR 得出错误结论\\n\\n## Figure Plan\\n\\n| ID | 内容 | 优先级 | 数据来源 |\\n|----|------|--------|---------|\\n| Fig 1 | Fake vs real safety 概念图 | 重要 | 设计 |\\n| Fig 2 | Displacement 分布 (A1 vs baseline vs Pi0.5) | **必须** | 800ep A1 + 200ep baseline + 600ep Pi0.5 |\\n| Fig 3 | TSR-CAR scatter + obstacle geometry 2-panel | 重要 | 多模型/多方法数据 + per-task geometry |\\n| Fig 4 | Oracle refinement CAR bar chart | **必须** | 3 oracle variants + baselines |\\n| Table 1 | 3-seed × 2-lambda 完整结果矩阵 | **必须** | Pi0.5+A1 训练结果 (pending) |\\n| Fig 5 | Lambda-CAR 曲线 (4 点: 0, 0.005, 0.01, 0.1) | 重要 | pure LoRA + A1 训练 (pending) |\\n\\n> Fig 3 合并了原 Fig 3 (TSR-CAR scatter) 和 Fig 4 (geometry vs CAR), 按 Reviewer 建议\\n\\n## Target Venue\\n\\n**Primary**: CoRL 2026 Main / ICRA 2027 (用户明确要求主会，不是 workshop)\\n**条件**: 需要至少一个正向贡献（Pi0.5+A1 成功 / 新 SDF 集成方式 / full-body SDF PoC）\\n\\n## Narrative Focus (Reviewer Report #30)\\n\\n论文核心贡献应聚焦于 **结构性洞察**（EE-only SDF 无法影响 full-body safety），而非 negative results 堆叠。三次方法失败（A1 openpi / A3 runtime / A1 Pi0.5）如果 root cause 相同，论文叙事应集中在这个 structural insight，各实验作为不同角度的验证。\\n\\n## Negative Results Narrative Strategy (D018 + 16 negatives)\\n\\n16 个阴性结果按叙事功能分为 3 层：\\n\\n### Tier A: 显式讨论（核心贡献，论文 §4-5 正文）\\n这些 negative 本身就是 paper 的 finding：\\n\\n| 类别 | 实验 | 论文功能 |\\n|------|------|----------|\\n| Fake safety 量化 | A1-openpi 800ep (99.6% fake) | Claim 1 主证据 |\\n| EE-only oracle 失败 | 3× GT oracle (adaptive/fixed/feature) | Claim 3 主证据 |\\n| Gradient correction 失败 | collapsed policy 不接受修正 (D018) | Claim 3 补充机制分析 |\\n| Task 3 碰撞转移 | SDF gradient 导致碰撞重分布 (D017) | Claim 3 补充（structural limitation） |\\n\\n### Tier B: 简要讨论（Ablation / boundary condition，论文 §5 或 Appendix）\\n提供边界信息，但非核心贡献：\\n\\n| 类别 | 实验 | 论文功能 |\\n|------|------|----------|\\n| TSR-CAR tradeoff | Pi0.5+A1 10K/30K TSR 下降 | Claim 4 tradeoff 定量（Table 1 已含） |\\n| Lambda sensitivity | λ=0.005 vs 0.01 差异 | Figure 5 lambda 曲线的数据点 |\\n\\n### Tier C: 省略（技术失败 / 与结论无关）\\n不进入论文正文或 appendix：\\n\\n- spatial_bowl 训练失败（磁盘满 / 代码 bug → 非科学结论）\\n- A3 runtime refine 早期版本（被 oracle 实验 supersede）\\n- 被 kill 的实验（资源调度，无结论）\\n\\n### 叙事原则\\n1. Tier A 的 negative 不是\\\"失败\\\"，是 **evidence for structural claims** — 用 \\\"we demonstrate\\\" 而非 \\\"we failed to\\\"\\n2. 多个 Tier A negative 收敛到同一 root cause (EE-only limitation) 时，叙事集中在 insight 上，各实验作为不同角度的验证\\n3. Tier B 以 1-2 句话出现在 results discussion 或 appendix，不展开\\n4. Tier C 完全不提\\n\\n## Contingency Plans (Post Step-10K Eval)\\n\\n**场景 1 (最可能)**: λ=0.005 ≈ λ=0.01, 均 ≤ baseline → SDF signal 被 action loss 淹没\\n→ Early-stop λ=0.01 runs, 用释放 GPU 跑纯 LoRA baseline + λ=0.1 bracket\\n→ 纯 analysis paper, 聚焦 structural insight\\n\\n**场景 2**: 两个 lambda 均 > baseline, 无差异 → 改善可能来自 LoRA 本身\\n→ 必须对比纯 LoRA baseline 才能归因\\n→ 无纯 LoRA baseline 的 CAR 改善不可发表\\n\\n**场景 2a-2d (LoRA 中间场景，Reviewer 预审补充)**:\\n\\n| LoRA-only CAR | SDF 增量 | 叙事策略 |\\n|---------------|----------|----------|\\n| ~27% (≈baseline) | +30pp 全归 SDF | \\\"geometric supervision is effective\\\" — 最强 method claim |\\n| ~35% | +22pp | \\\"LoRA capacity tuning helps, SDF provides major additional benefit\\\" — 仍强 |\\n| ~45% | +12pp | \\\"LoRA is primary driver, SDF provides dose-dependent safety margin\\\" — 需 4-point lambda 曲线支撑 monotonic trend |\\n| ~55%+ (≈A1) | ≈0pp | 归纯 LoRA → pure analysis paper, SDF 作为 negative evidence |\\n\\n关键防御：即使 SDF 增量仅 +10-15pp，只要 4-point lambda 曲线呈 monotonic trend，仍可 claim \\\"geometric supervision signal provides dose-dependent safety improvement beyond LoRA capacity tuning\\\"。\\n\\n**场景 3**: λ=0.01 > λ=0.005 → SDF 有效\\n→ 继续到 30K, 升级为 \\\"analysis paper with positive method contribution\\\"（非纯 method paper）\\n→ 加 λ=0 (pure LoRA) + λ=0.1 构建 4-point lambda 曲线, 支持 \\\"sweet spot\\\" claim\\n→ 扩展到 spatial_bowl 第 2 task, 强化泛化性\\n\\n## Dependencies\\n\\n- [ ] Pi0.5+A1 训练结果 (Claim 4, Table 1) — ETA 5/24 18:00\\n- [ ] Step 10K mid-eval — ETA 5/23 ~16:25 UTC\\n- [ ] 纯 LoRA baseline (无 SDF/EE loss) — **RUNNING** (westd-45947, 2-seed, ETA ~5/26 01:30)\\n- [ ] λ=0.1 bracket (1-seed Pi0.5) — 10K eval 后启动, 4-point lambda 曲线必需\\n- [ ] spatial_bowl A1 训练 (2-seed × best-lambda) — **代码准备中（Agent 已派 Worker）**, 必须 5/28 前启动（CoRL DDL 约束）\\n- [ ] OpenVLA zero-shot SafeLIBERO eval — 仅 inference, 验证 fake safety 跨模型存在\\n- [x] Pi0.5 baseline 3-seed (Claim 2) — CAR=26.8±1.6%\\n- [x] A1 fake safety 800ep (Claim 1) — 99.6% fake\\n- [x] Oracle 3 variants (Claim 3) — all < baseline\\n- [x] Spatial/object collision analysis (Claim 3) — arm-body dominant\\n\", \"total_chars\": 8058, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e30124b-e11f-468d-b9f7-1ea1e18990b4",
  "uuid": "7a2924d9-3a26-44fa-b5b8-5667a87df17f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md\\\", \\\"content\\\": \\\"# ColliForce-VLA Paper Framing\\\\n\\\\n> 维护者: Director | 最后更新: 2026-05-24 12:30 UTC | Reviewer 预审反馈：补 LoRA 中间场景叙事 + Claim 4 措辞升级\\\\n\\\\n## Core Insight\\\\n\\\\n当前 VLA safety 评估存在系统性缺陷：collision avoidance rate (CAR) 被 action collapse 严重污染，导致 \\\\\\\"安全\\\\\\\" 指标虚高。我们通过大规模实证分析（39 个实验, 5000+ episodes）揭示三个相互关联的问题，并提出 displacement-filtered CAR 作为修正指标。\\\\n\\\\n## Working Title\\\\n\\\\n\\\\\\\"The Safety Illusion: How Action Collapse Contaminates Collision Avoidance Metrics in Vision-Language-Action Models\\\\\\\"\\\\n\\\\n> 注：Title scope 已按 Reviewer Report #26 建议收窄——不再 claim 覆盖 \\\\\\\"all SDF methods\\\\\\\"，聚焦 metric contamination 这一更可防御的贡献\\\\n\\\\n## Core Claims\\\\n\\\\n### Claim 1: Fake Safety (Primary — 证据强度 ★★★★★)\\\\nCAR 指标被 action collapse 严重污染。在 SafeLIBERO benchmark 上，A1 (SDF auxiliary loss) 的 91.5% CAR 中 99.6% 是 fake safe（robot displacement < 1μm）。\\\\\\\"Collision-free\\\\\\\" ≠ \\\\\\\"collision-avoiding\\\\\\\"。\\\\n\\\\n**证据**: 800 episodes A1 per-episode displacement 分析; 200 episodes baseline 对比; Pi0.5 56/56 safe episodes displacement ≈ 0\\\\n\\\\n**贡献**: 提出 displacement-filtered CAR (real_CAR) 作为修正指标\\\\n\\\\n### Claim 2: Task Capability vs Safety Anti-correlation (Secondary — 证据强度 ★★★)\\\\n更强的 base model 完成更多任务但碰撞更多。Pi0.5 (TSR=74.7%) vs Pi0 (TSR≈0%): 能力越强 → 运动越多 → 碰撞越多。\\\\n\\\\n**证据**: Pi0.5 3-seed eval (TSR=74.7±1.5%, CAR=26.8±1.6%) vs Pi0 baseline (TSR≈0%, CAR=82%)\\\\n\\\\n**限制**: 仅 2 个 model families, Pi0 的 \\\\\\\"高 CAR\\\\\\\" 来自 action collapse 而非安全。Reviewer 建议降级为 observation, 不 claim 因果关系。\\\\n\\\\n### Claim 3: EE-only SDF Structural Limitation (Supporting — 证据强度 ★★★★)\\\\nEnd-effector-only SDF 在 action space 的碰撞避免存在结构性缺陷：SDF gradient 推 EE 远离障碍物但导致 arm body 扫过障碍物。\\\\n\\\\n**证据**: 3 组 GT SDF oracle (adaptive alpha, fixed alpha, feature-space) 均劣于 baseline; spatial vs object 碰撞部位分析; obstacle 高度/体积与碰撞率的单调关系\\\\n\\\\n**限制**: \\\\\\\"EE-only 不够\\\\\\\" 是 expected result; 缺乏 full-body SDF 对照\\\\n\\\\n### Claim 4: SDF Auxiliary Loss Effectiveness on Strong VLA (Pending — 取决于实验)\\\\n在能力充分的 VLA (Pi0.5) 上，SDF auxiliary training loss 能否产生真实的碰撞避免行为？\\\\n\\\\n**状态**: 3-seed × 2-lambda 训练中, 预计 5/24 18:00 出结果\\\\n\\\\n**Framing 策略 (Reviewer #37)**：即使最优结果也定位为 **\\\\\\\"analysis paper with positive method contribution\\\\\\\"**，而非纯 method paper。原因：analysis 贡献 scope-proof（适用所有 VLA），method 贡献 scope-limited（1-2 models, 2-4 tasks）。SDF aux loss 作为 secondary proof-of-concept，证明 \\\\\\\"问题可解决\\\\\\\" 以验证 analysis 框架的价值。\\\\n\\\\n**Claim 措辞上限** (按 Reviewer 预审升级，基于 10K +30pp 证据): \\\\\\\"Training-time SDF auxiliary loss yields substantial collision avoidance improvement (+Xpp displacement-filtered CAR, frozen_rate=0%) on Pi0.5, confirming that geometric supervision effectively addresses action-collapse-contaminated safety in capable VLAs — at a moderate task performance cost (TSR: 74.7%→Y%)\\\\\\\"（必须包含 TSR tradeoff；禁区: SOTA / consistently outperforms / general solution）\\\\n\\\\n**如果成功 (CAR ≥ 33%)**: 升级为 method contribution (secondary)\\\\n**如果失败**: 额外 negative evidence, 强化 structural insight\\\\n\\\\n**泛化扩展计划 (Reviewer #37, 提升接受率)**：\\\\n- 必须: spatial_bowl 第 2 task 训练（代码准备中）→ 接受率 40% → 55-65%\\\\n- 应该做: OpenVLA zero-shot eval 验证 fake safety 在第 3 model 上存在（仅 inference）\\\\n- 应该做: 4-point lambda 曲线 (0, 0.005, 0.01, 0.1) 支持 \\\\\\\"sweet spot\\\\\\\" claim\\\\n- Nice-to-have: SafeLIBERO 4 suite 各 1 task\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n### R1 (最致命): Generalizability\\\\n\\\\\\\"仅在 SafeLIBERO + Pi0 系列上验证, 凭什么说 fake safety 是普遍问题?\\\\\\\"\\\\n→ **应对**: (1) 2+ tasks (object_pudding + spatial_bowl, 代码准备中); (2) 3+ models 的 analysis (Pi0 + Pi0.5 已有, 加 OpenVLA zero-shot eval); (3) 收窄 claim scope + discussion 中做机制分析\\\\n→ **接受率估算** (Reviewer #37): 1 task ~40% / 2 tasks+2 model ~55-65% / 4 tasks+3 model ~65-75%\\\\n\\\\n### R2: Novelty of EE-only limitation\\\\n\\\\\\\"任何了解机器人运动学的人都知道肘部会碰\\\\\\\"\\\\n→ **应对**: 强调定量分析 (arm-body vs EE 碰撞比例量化 + oracle 排除其他解释) 而非定性观察; 作为 supporting claim 而非 primary\\\\n\\\\n### R3: No positive result\\\\n\\\\\\\"告诉我什么不 work 但没告诉我什么 work\\\\\\\"\\\\n→ **应对**: real_CAR 指标是 positive 工具贡献; Pi0.5+A1 如果成功也是正面结果; diagnostic framework 有方法论价值\\\\n\\\\n### R4: Action collapse is trivial\\\\n\\\\\\\"Undertrained Pi0 的 action collapse 不是 safety 特有的, 是训练不足的自然结果\\\\\\\"\\\\n→ **应对**: 必须在论文中承认这一点; 但指出即使原因 trivial, metric contamination 的后果 non-trivial — 后续工作可能基于被污染的 CAR 得出错误结论\\\\n\\\\n## Figure Plan\\\\n\\\\n| ID | 内容 | 优先级 | 数据来源 |\\\\n|----|------|--------|---------|\\\\n| Fig 1 | Fake vs real safety 概念图 | 重要 | 设计 |\\\\n| Fig 2 | Displacement 分布 (A1 vs baseline vs Pi0.5) | **必须** | 800ep A1 + 200ep baseline + 600ep Pi0.5 |\\\\n| Fig 3 | TSR-CAR scatter + obstacle geometry 2-panel | 重要 | 多模型/多方法数据 + per-task geometry |\\\\n| Fig 4 | Oracle refinement CAR bar chart | **必须** | 3 oracle variants + baselines |\\\\n| Table 1 | 3-seed × 2-lambda 完整结果矩阵 | **必须** | Pi0.5+A1 训练结果 (pending) |\\\\n| Fig 5 | Lambda-CAR 曲线 (4 点: 0, 0.005, 0.01, 0.1) | 重要 | pure LoRA + A1 训练 (pending) |\\\\n\\\\n> Fig 3 合并了原 Fig 3 (TSR-CAR scatter) 和 Fig 4 (geometry vs CAR), 按 Reviewer 建议\\\\n\\\\n## Target Venue\\\\n\\\\n**Primary**: CoRL 2026 Main / ICRA 2027 (用户明确要求主会，不是 workshop)\\\\n**条件**: 需要至少一个正向贡献（Pi0.5+A1 成功 / 新 SDF 集成方式 / full-body SDF PoC）\\\\n\\\\n## Narrative Focus (Reviewer Report #30)\\\\n\\\\n论文核心贡献应聚焦于 **结构性洞察**（EE-only SDF 无法影响 full-body safety），而非 negative results 堆叠。三次方法失败（A1 openpi / A3 runtime / A1 Pi0.5）如果 root cause 相同，论文叙事应集中在这个 structural insight，各实验作为不同角度的验证。\\\\n\\\\n## Negative Results Narrative Strategy (D018 + 16 negatives)\\\\n\\\\n16 个阴性结果按叙事功能分为 3 层：\\\\n\\\\n### Tier A: 显式讨论（核心贡献，论文 §4-5 正文）\\\\n这些 negative 本身就是 paper 的 finding：\\\\n\\\\n| 类别 | 实验 | 论文功能 |\\\\n|------|------|----------|\\\\n| Fake safety 量化 | A1-openpi 800ep (99.6% fake) | Claim 1 主证据 |\\\\n| EE-only oracle 失败 | 3× GT oracle (adaptive/fixed/feature) | Claim 3 主证据 |\\\\n| Gradient correction 失败 | collapsed policy 不接受修正 (D018) | Claim 3 补充机制分析 |\\\\n| Task 3 碰撞转移 | SDF gradient 导致碰撞重分布 (D017) | Claim 3 补充（structural limitation） |\\\\n\\\\n### Tier B: 简要讨论（Ablation / boundary condition，论文 §5 或 Appendix）\\\\n提供边界信息，但非核心贡献：\\\\n\\\\n| 类别 | 实验 | 论文功能 |\\\\n|------|------|----------|\\\\n| TSR-CAR tradeoff | Pi0.5+A1 10K/30K TSR 下降 | Claim 4 tradeoff 定量（Table 1 已含） |\\\\n| Lambda sensitivity | λ=0.005 vs 0.01 差异 | Figure 5 lambda 曲线的数据点 |\\\\n\\\\n### Tier C: 省略（技术失败 / 与结论无关）\\\\n不进入论文正文或 appendix：\\\\n\\\\n- spatial_bowl 训练失败（磁盘满 / 代码 bug → 非科学结论）\\\\n- A3 runtime refine 早期版本（被 oracle 实验 supersede）\\\\n- 被 kill 的实验（资源调度，无结论）\\\\n\\\\n### 叙事原则\\\\n1. Tier A 的 negative 不是\\\\\\\"失败\\\\\\\"，是 **evidence for structural claims** — 用 \\\\\\\"we demonstrate\\\\\\\" 而非 \\\\\\\"we failed to\\\\\\\"\\\\n2. 多个 Tier A negative 收敛到同一 root cause (EE-only limitation) 时，叙事集中在 insight 上，各实验作为不同角度的验证\\\\n3. Tier B 以 1-2 句话出现在 results discussion 或 appendix，不展开\\\\n4. Tier C 完全不提\\\\n\\\\n## Contingency Plans (Post Step-10K Eval)\\\\n\\\\n**场景 1 (最可能)**: λ=0.005 ≈ λ=0.01, 均 ≤ baseline → SDF signal 被 action loss 淹没\\\\n→ Early-stop λ=0.01 runs, 用释放 GPU 跑纯 LoRA baseline + λ=0.1 bracket\\\\n→ 纯 analysis paper, 聚焦 structural insight\\\\n\\\\n**场景 2**: 两个 lambda 均 > baseline, 无差异 → 改善可能来自 LoRA 本身\\\\n→ 必须对比纯 LoRA baseline 才能归因\\\\n→ 无纯 LoRA baseline 的 CAR 改善不可发表\\\\n\\\\n**场景 2a-2d (LoRA 中间场景，Reviewer 预审补充)**:\\\\n\\\\n| LoRA-only CAR | SDF 增量 | 叙事策略 |\\\\n|---------------|----------|----------|\\\\n| ~27% (≈baseline) | +30pp 全归 SDF | \\\\\\\"geometric supervision is effective\\\\\\\" — 最强 method claim |\\\\n| ~35% | +22pp | \\\\\\\"LoRA capacity tuning helps, SDF provides major additional benefit\\\\\\\" — 仍强 |\\\\n| ~45% | +12pp | \\\\\\\"LoRA is primary driver, SDF provides dose-dependent safety margin\\\\\\\" — 需 4-point lambda 曲线支撑 monotonic trend |\\\\n| ~55%+ (≈A1) | ≈0pp | 归纯 LoRA → pure analysis paper, SDF 作为 negative evidence |\\\\n\\\\n关键防御：即使 SDF 增量仅 +10-15pp，只要 4-point lambda 曲线呈 monotonic trend，仍可 claim \\\\\\\"geometric supervision signal provides dose-dependent safety improvement beyond LoRA capacity tuning\\\\\\\"。\\\\n\\\\n**场景 3**: λ=0.01 > λ=0.005 → SDF 有效\\\\n→ 继续到 30K, 升级为 \\\\\\\"analysis paper with positive method contribution\\\\\\\"（非纯 method paper）\\\\n→ 加 λ=0 (pure LoRA) + λ=0.1 构建 4-point lambda 曲线, 支持 \\\\\\\"sweet spot\\\\\\\" claim\\\\n→ 扩展到 spatial_bowl 第 2 task, 强化泛化性\\\\n\\\\n## Dependencies\\\\n\\\\n- [ ] Pi0.5+A1 训练结果 (Claim 4, Table 1) — ETA 5/24 18:00\\\\n- [ ] Step 10K mid-eval — ETA 5/23 ~16:25 UTC\\\\n- [ ] 纯 LoRA baseline (无 SDF/EE loss) — **RUNNING** (westd-45947, 2-seed, ETA ~5/26 01:30)\\\\n- [ ] λ=0.1 bracket (1-seed Pi0.5) — 10K eval 后启动, 4-point lambda 曲线必需\\\\n- [ ] spatial_bowl A1 训练 (2-seed × best-lambda) — **代码准备中（Agent 已派 Worker）**, 必须 5/28 前启动（CoRL DDL 约束）\\\\n- [ ] OpenVLA zero-shot SafeLIBERO eval — 仅 inference, 验证 fake safety 跨模型存在\\\\n- [x] Pi0.5 baseline 3-seed (Claim 2) — CAR=26.8±1.6%\\\\n- [x] A1 fake safety 800ep (Claim 1) — 99.6% fake\\\\n- [x] Oracle 3 variants (Claim 3) — all < baseline\\\\n- [x] Spatial/object collision analysis (Claim 3) — arm-body dominant\\\\n\\\", \\\"total_chars\\\": 8058, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md\", \"content\": \"# ColliForce-VLA Paper Framing\\n\\n> 维护者: Director | 最后更新: 2026-05-24 12:30 UTC | Reviewer 预审反馈：补 LoRA 中间场景叙事 + Claim 4 措辞升级\\n\\n## Core Insight\\n\\n当前 VLA safety 评估存在系统性缺陷：collision avoidance rate (CAR) 被 action collapse 严重污染，导致 \\\"安全\\\" 指标虚高。我们通过大规模实证分析（39 个实验, 5000+ episodes）揭示三个相互关联的问题，并提出 displacement-filtered CAR 作为修正指标。\\n\\n## Working Title\\n\\n\\\"The Safety Illusion: How Action Collapse Contaminates Collision Avoidance Metrics in Vision-Language-Action Models\\\"\\n\\n> 注：Title scope 已按 Reviewer Report #26 建议收窄——不再 claim 覆盖 \\\"all SDF methods\\\"，聚焦 metric contamination 这一更可防御的贡献\\n\\n## Core Claims\\n\\n### Claim 1: Fake Safety (Primary — 证据强度 ★★★★★)\\nCAR 指标被 action collapse 严重污染。在 SafeLIBERO benchmark 上，A1 (SDF auxiliary loss) 的 91.5% CAR 中 99.6% 是 fake safe（robot displacement < 1μm）。\\\"Collision-free\\\" ≠ \\\"collision-avoiding\\\"。\\n\\n**证据**: 800 episodes A1 per-episode displacement 分析; 200 episodes baseline 对比; Pi0.5 56/56 safe episodes displacement ≈ 0\\n\\n**贡献**: 提出 displacement-filtered CAR (real_CAR) 作为修正指标\\n\\n### Claim 2: Task Capability vs Safety Anti-correlation (Secondary — 证据强度 ★★★)\\n更强的 base model 完成更多任务但碰撞更多。Pi0.5 (TSR=74.7%) vs Pi0 (TSR≈0%): 能力越强 → 运动越多 → 碰撞越多。\\n\\n**证据**: Pi0.5 3-seed eval (TSR=74.7±1.5%, CAR=26.8±1.6%) vs Pi0 baseline (TSR≈0%, CAR=82%)\\n\\n**限制**: 仅 2 个 model families, Pi0 的 \\\"高 CAR\\\" 来自 action collapse 而非安全。Reviewer 建议降级为 observation, 不 claim 因果关系。\\n\\n### Claim 3: EE-only SDF Structural Limitation (Supporting — 证据强度 ★★★★)\\nEnd-effector-only SDF 在 action space 的碰撞避免存在结构性缺陷：SDF gradient 推 EE 远离障碍物但导致 arm body 扫过障碍物。\\n\\n**证据**: 3 组 GT SDF oracle (adaptive alpha, fixed alpha, feature-space) 均劣于 baseline; spatial vs object 碰撞部位分析; obstacle 高度/体积与碰撞率的单调关系\\n\\n**限制**: \\\"EE-only 不够\\\" 是 expected result; 缺乏 full-body SDF 对照\\n\\n### Claim 4: SDF Auxiliary Loss Effectiveness on Strong VLA (Pending — 取决于实验)\\n在能力充分的 VLA (Pi0.5) 上，SDF auxiliary training loss 能否产生真实的碰撞避免行为？\\n\\n**状态**: 3-seed × 2-lambda 训练中, 预计 5/24 18:00 出结果\\n\\n**Framing 策略 (Reviewer #37)**：即使最优结果也定位为 **\\\"analysis paper with positive method contribution\\\"**，而非纯 method paper。原因：analysis 贡献 scope-proof（适用所有 VLA），method 贡献 scope-limited（1-2 models, 2-4 tasks）。SDF aux loss 作为 secondary proof-of-concept，证明 \\\"问题可解决\\\" 以验证 analysis 框架的价值。\\n\\n**Claim 措辞上限** (按 Reviewer 预审升级，基于 10K +30pp 证据): \\\"Training-time SDF auxiliary loss yields substantial collision avoidance improvement (+Xpp displacement-filtered CAR, frozen_rate=0%) on Pi0.5, confirming that geometric supervision effectively addresses action-collapse-contaminated safety in capable VLAs — at a moderate task performance cost (TSR: 74.7%→Y%)\\\"（必须包含 TSR tradeoff；禁区: SOTA / consistently outperforms / general solution）\\n\\n**如果成功 (CAR ≥ 33%)**: 升级为 method contribution (secondary)\\n**如果失败**: 额外 negative evidence, 强化 structural insight\\n\\n**泛化扩展计划 (Reviewer #37, 提升接受率)**：\\n- 必须: spatial_bowl 第 2 task 训练（代码准备中）→ 接受率 40% → 55-65%\\n- 应该做: OpenVLA zero-shot eval 验证 fake safety 在第 3 model 上存在（仅 inference）\\n- 应该做: 4-point lambda 曲线 (0, 0.005, 0.01, 0.1) 支持 \\\"sweet spot\\\" claim\\n- Nice-to-have: SafeLIBERO 4 suite 各 1 task\\n\\n## Anticipated Reviewer Concerns\\n\\n### R1 (最致命): Generalizability\\n\\\"仅在 SafeLIBERO + Pi0 系列上验证, 凭什么说 fake safety 是普遍问题?\\\"\\n→ **应对**: (1) 2+ tasks (object_pudding + spatial_bowl, 代码准备中); (2) 3+ models 的 analysis (Pi0 + Pi0.5 已有, 加 OpenVLA zero-shot eval); (3) 收窄 claim scope + discussion 中做机制分析\\n→ **接受率估算** (Reviewer #37): 1 task ~40% / 2 tasks+2 model ~55-65% / 4 tasks+3 model ~65-75%\\n\\n### R2: Novelty of EE-only limitation\\n\\\"任何了解机器人运动学的人都知道肘部会碰\\\"\\n→ **应对**: 强调定量分析 (arm-body vs EE 碰撞比例量化 + oracle 排除其他解释) 而非定性观察; 作为 supporting claim 而非 primary\\n\\n### R3: No positive result\\n\\\"告诉我什么不 work 但没告诉我什么 work\\\"\\n→ **应对**: real_CAR 指标是 positive 工具贡献; Pi0.5+A1 如果成功也是正面结果; diagnostic framework 有方法论价值\\n\\n### R4: Action collapse is trivial\\n\\\"Undertrained Pi0 的 action collapse 不是 safety 特有的, 是训练不足的自然结果\\\"\\n→ **应对**: 必须在论文中承认这一点; 但指出即使原因 trivial, metric contamination 的后果 non-trivial — 后续工作可能基于被污染的 CAR 得出错误结论\\n\\n## Figure Plan\\n\\n| ID | 内容 | 优先级 | 数据来源 |\\n|----|------|--------|---------|\\n| Fig 1 | Fake vs real safety 概念图 | 重要 | 设计 |\\n| Fig 2 | Displacement 分布 (A1 vs baseline vs Pi0.5) | **必须** | 800ep A1 + 200ep baseline + 600ep Pi0.5 |\\n| Fig 3 | TSR-CAR scatter + obstacle geometry 2-panel | 重要 | 多模型/多方法数据 + per-task geometry |\\n| Fig 4 | Oracle refinement CAR bar chart | **必须** | 3 oracle variants + baselines |\\n| Table 1 | 3-seed × 2-lambda 完整结果矩阵 | **必须** | Pi0.5+A1 训练结果 (pending) |\\n| Fig 5 | Lambda-CAR 曲线 (4 点: 0, 0.005, 0.01, 0.1) | 重要 | pure LoRA + A1 训练 (pending) |\\n\\n> Fig 3 合并了原 Fig 3 (TSR-CAR scatter) 和 Fig 4 (geometry vs CAR), 按 Reviewer 建议\\n\\n## Target Venue\\n\\n**Primary**: CoRL 2026 Main / ICRA 2027 (用户明确要求主会，不是 workshop)\\n**条件**: 需要至少一个正向贡献（Pi0.5+A1 成功 / 新 SDF 集成方式 / full-body SDF PoC）\\n\\n## Narrative Focus (Reviewer Report #30)\\n\\n论文核心贡献应聚焦于 **结构性洞察**（EE-only SDF 无法影响 full-body safety），而非 negative results 堆叠。三次方法失败（A1 openpi / A3 runtime / A1 Pi0.5）如果 root cause 相同，论文叙事应集中在这个 structural insight，各实验作为不同角度的验证。\\n\\n## Negative Results Narrative Strategy (D018 + 16 negatives)\\n\\n16 个阴性结果按叙事功能分为 3 层：\\n\\n### Tier A: 显式讨论（核心贡献，论文 §4-5 正文）\\n这些 negative 本身就是 paper 的 finding：\\n\\n| 类别 | 实验 | 论文功能 |\\n|------|------|----------|\\n| Fake safety 量化 | A1-openpi 800ep (99.6% fake) | Claim 1 主证据 |\\n| EE-only oracle 失败 | 3× GT oracle (adaptive/fixed/feature) | Claim 3 主证据 |\\n| Gradient correction 失败 | collapsed policy 不接受修正 (D018) | Claim 3 补充机制分析 |\\n| Task 3 碰撞转移 | SDF gradient 导致碰撞重分布 (D017) | Claim 3 补充（structural limitation） |\\n\\n### Tier B: 简要讨论（Ablation / boundary condition，论文 §5 或 Appendix）\\n提供边界信息，但非核心贡献：\\n\\n| 类别 | 实验 | 论文功能 |\\n|------|------|----------|\\n| TSR-CAR tradeoff | Pi0.5+A1 10K/30K TSR 下降 | Claim 4 tradeoff 定量（Table 1 已含） |\\n| Lambda sensitivity | λ=0.005 vs 0.01 差异 | Figure 5 lambda 曲线的数据点 |\\n\\n### Tier C: 省略（技术失败 / 与结论无关）\\n不进入论文正文或 appendix：\\n\\n- spatial_bowl 训练失败（磁盘满 / 代码 bug → 非科学结论）\\n- A3 runtime refine 早期版本（被 oracle 实验 supersede）\\n- 被 kill 的实验（资源调度，无结论）\\n\\n### 叙事原则\\n1. Tier A 的 negative 不是\\\"失败\\\"，是 **evidence for structural claims** — 用 \\\"we demonstrate\\\" 而非 \\\"we failed to\\\"\\n2. 多个 Tier A negative 收敛到同一 root cause (EE-only limitation) 时，叙事集中在 insight 上，各实验作为不同角度的验证\\n3. Tier B 以 1-2 句话出现在 results discussion 或 appendix，不展开\\n4. Tier C 完全不提\\n\\n## Contingency Plans (Post Step-10K Eval)\\n\\n**场景 1 (最可能)**: λ=0.005 ≈ λ=0.01, 均 ≤ baseline → SDF signal 被 action loss 淹没\\n→ Early-stop λ=0.01 runs, 用释放 GPU 跑纯 LoRA baseline + λ=0.1 bracket\\n→ 纯 analysis paper, 聚焦 structural insight\\n\\n**场景 2**: 两个 lambda 均 > baseline, 无差异 → 改善可能来自 LoRA 本身\\n→ 必须对比纯 LoRA baseline 才能归因\\n→ 无纯 LoRA baseline 的 CAR 改善不可发表\\n\\n**场景 2a-2d (LoRA 中间场景，Reviewer 预审补充)**:\\n\\n| LoRA-only CAR | SDF 增量 | 叙事策略 |\\n|---------------|----------|----------|\\n| ~27% (≈baseline) | +30pp 全归 SDF | \\\"geometric supervision is effective\\\" — 最强 method claim |\\n| ~35% | +22pp | \\\"LoRA capacity tuning helps, SDF provides major additional benefit\\\" — 仍强 |\\n| ~45% | +12pp | \\\"LoRA is primary driver, SDF provides dose-dependent safety margin\\\" — 需 4-point lambda 曲线支撑 monotonic trend |\\n| ~55%+ (≈A1) | ≈0pp | 归纯 LoRA → pure analysis paper, SDF 作为 negative evidence |\\n\\n关键防御：即使 SDF 增量仅 +10-15pp，只要 4-point lambda 曲线呈 monotonic trend，仍可 claim \\\"geometric supervision signal provides dose-dependent safety improvement beyond LoRA capacity tuning\\\"。\\n\\n**场景 3**: λ=0.01 > λ=0.005 → SDF 有效\\n→ 继续到 30K, 升级为 \\\"analysis paper with positive method contribution\\\"（非纯 method paper）\\n→ 加 λ=0 (pure LoRA) + λ=0.1 构建 4-point lambda 曲线, 支持 \\\"sweet spot\\\" claim\\n→ 扩展到 spatial_bowl 第 2 task, 强化泛化性\\n\\n## Dependencies\\n\\n- [ ] Pi0.5+A1 训练结果 (Claim 4, Table 1) — ETA 5/24 18:00\\n- [ ] Step 10K mid-eval — ETA 5/23 ~16:25 UTC\\n- [ ] 纯 LoRA baseline (无 SDF/EE loss) — **RUNNING** (westd-45947, 2-seed, ETA ~5/26 01:30)\\n- [ ] λ=0.1 bracket (1-seed Pi0.5) — 10K eval 后启动, 4-point lambda 曲线必需\\n- [ ] spatial_bowl A1 训练 (2-seed × best-lambda) — **代码准备中（Agent 已派 Worker）**, 必须 5/28 前启动（CoRL DDL 约束）\\n- [ ] OpenVLA zero-shot SafeLIBERO eval — 仅 inference, 验证 fake safety 跨模型存在\\n- [x] Pi0.5 baseline 3-seed (Claim 2) — CAR=26.8±1.6%\\n- [x] A1 fake safety 800ep (Claim 1) — 99.6% fake\\n- [x] Oracle 3 variants (Claim 3) — all < baseline\\n- [x] Spatial/object collision analysis (Claim 3) — arm-body dominant\\n\", \"total_chars\": 8058, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
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
I now have the full content of paper_framing.md. I need to find the "Negative Results Narrative Strategy" section and update it with the new 4-block structure. The current section starts with "## Negative Results Narrative Strategy (D018 + 16 negatives)" and contains a 3-tier structure. I need to replace or update this with the Director-approved 4-block structure.

Let me look at where the section is and plan the edit. The current "Negative Results Narrative Strategy" section spans from "## Negative Results Narrative Strategy (D018 + 16 negatives)" to the end of the "叙事原则" subsection. After that comes "## Contingency Plans".


I'll replace the entire "Negative Results Narrative Strategy" section with the new 4-block structure, removing the old 3-tier approach and inserting the Director's approved format in its place.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e30124b-e11f-468d-b9f7-1ea1e18990b4",
  "uuid": "145d83c3-cfb3-4ce5-8c1e-d4b965686745",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NLb2S3ibA8DSaFiNZpmUHR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4707,
      "cache_read_input_tokens": 24255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4707
      },
      "output_tokens": 9,
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

现在用 4-block 结构替换现有的 3-tier 叙事策略。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e30124b-e11f-468d-b9f7-1ea1e18990b4",
  "uuid": "024f5e29-301d-410f-868e-77840df97d03",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NLb2S3ibA8DSaFiNZpmUHR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4707,
      "cache_read_input_tokens": 24255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4707
      },
      "output_tokens": 9,
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

<details open><summary>🔧 Tool call — Read · `toolu_018LBjpBp4zPuNRgTdQMjELB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e30124b-e11f-468d-b9f7-1ea1e18990b4",
  "uuid": "30d3c3e1-12d7-4142-b26b-7f33d9136e48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NLb2S3ibA8DSaFiNZpmUHR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4707,
      "cache_read_input_tokens": 24255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4707
      },
      "output_tokens": 9,
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

_source line 13 · 2026-05-25T09:13:50.042Z_

<details><summary>↩ Tool result · `toolu_018LBjpBp4zPuNRgTdQMjELB`</summary>

```text
1	# ColliForce-VLA Paper Framing
2	
3	> 维护者: Director | 最后更新: 2026-05-24 12:30 UTC | Reviewer 预审反馈：补 LoRA 中间场景叙事 + Claim 4 措辞升级
4	
5	## Core Insight
6	
7	当前 VLA safety 评估存在系统性缺陷：collision avoidance rate (CAR) 被 action collapse 严重污染，导致 "安全" 指标虚高。我们通过大规模实证分析（39 个实验, 5000+ episodes）揭示三个相互关联的问题，并提出 displacement-filtered CAR 作为修正指标。
8	
9	## Working Title
10	
11	"The Safety Illusion: How Action Collapse Contaminates Collision Avoidance Metrics in Vision-Language-Action Models"
12	
13	> 注：Title scope 已按 Reviewer Report #26 建议收窄——不再 claim 覆盖 "all SDF methods"，聚焦 metric contamination 这一更可防御的贡献
14	
15	## Core Claims
16	
17	### Claim 1: Fake Safety (Primary — 证据强度 ★★★★★)
18	CAR 指标被 action collapse 严重污染。在 SafeLIBERO benchmark 上，A1 (SDF auxiliary loss) 的 91.5% CAR 中 99.6% 是 fake safe（robot displacement < 1μm）。"Collision-free" ≠ "collision-avoiding"。
19	
20	**证据**: 800 episodes A1 per-episode displacement 分析; 200 episodes baseline 对比; Pi0.5 56/56 safe episodes displacement ≈ 0
21	
22	**贡献**: 提出 displacement-filtered CAR (real_CAR) 作为修正指标
23	
24	### Claim 2: Task Capability vs Safety Anti-correlation (Secondary — 证据强度 ★★★)
25	更强的 base model 完成更多任务但碰撞更多。Pi0.5 (TSR=74.7%) vs Pi0 (TSR≈0%): 能力越强 → 运动越多 → 碰撞越多。
26	
27	**证据**: Pi0.5 3-seed eval (TSR=74.7±1.5%, CAR=26.8±1.6%) vs Pi0 baseline (TSR≈0%, CAR=82%)
28	
29	**限制**: 仅 2 个 model families, Pi0 的 "高 CAR" 来自 action collapse 而非安全。Reviewer 建议降级为 observation, 不 claim 因果关系。
30	
31	### Claim 3: EE-only SDF Structural Limitation (Supporting — 证据强度 ★★★★)
32	End-effector-only SDF 在 action space 的碰撞避免存在结构性缺陷：SDF gradient 推 EE 远离障碍物但导致 arm body 扫过障碍物。
33	
34	**证据**: 3 组 GT SDF oracle (adaptive alpha, fixed alpha, feature-space) 均劣于 baseline; spatial vs object 碰撞部位分析; obstacle 高度/体积与碰撞率的单调关系
35	
36	**限制**: "EE-only 不够" 是 expected result; 缺乏 full-body SDF 对照
37	
38	### Claim 4: SDF Auxiliary Loss Effectiveness on Strong VLA (Pending — 取决于实验)
39	在能力充分的 VLA (Pi0.5) 上，SDF auxiliary training loss 能否产生真实的碰撞避免行为？
40	
41	**状态**: 3-seed × 2-lambda 训练中, 预计 5/24 18:00 出结果
42	
43	**Framing 策略 (Reviewer #37)**：即使最优结果也定位为 **"analysis paper with positive method contribution"**，而非纯 method paper。原因：analysis 贡献 scope-proof（适用所有 VLA），method 贡献 scope-limited（1-2 models, 2-4 tasks）。SDF aux loss 作为 secondary proof-of-concept，证明 "问题可解决" 以验证 analysis 框架的价值。
44	
45	**Claim 措辞上限** (按 Reviewer 预审升级，基于 10K +30pp 证据): "Training-time SDF auxiliary loss yields substantial collision avoidance improvement (+Xpp displacement-filtered CAR, frozen_rate=0%) on Pi0.5, confirming that geometric supervision effectively addresses action-collapse-contaminated safety in capable VLAs — at a moderate task performance cost (TSR: 74.7%→Y%)"（必须包含 TSR tradeoff；禁区: SOTA / consistently outperforms / general solution）
46	
47	**如果成功 (CAR ≥ 33%)**: 升级为 method contribution (secondary)
48	**如果失败**: 额外 negative evidence, 强化 structural insight
49	
50	**泛化扩展计划 (Reviewer #37, 提升接受率)**：
51	- 必须: spatial_bowl 第 2 task 训练（代码准备中）→ 接受率 40% → 55-65%
52	- 应该做: OpenVLA zero-shot eval 验证 fake safety 在第 3 model 上存在（仅 inference）
53	- 应该做: 4-point lambda 曲线 (0, 0.005, 0.01, 0.1) 支持 "sweet spot" claim
54	- Nice-to-have: SafeLIBERO 4 suite 各 1 task
55	
56	## Anticipated Reviewer Concerns
57	
58	### R1 (最致命): Generalizability
59	"仅在 SafeLIBERO + Pi0 系列上验证, 凭什么说 fake safety 是普遍问题?"
60	→ **应对**: (1) 2+ tasks (object_pudding + spatial_bowl, 代码准备中); (2) 3+ models 的 analysis (Pi0 + Pi0.5 已有, 加 OpenVLA zero-shot eval); (3) 收窄 claim scope + discussion 中做机制分析
61	→ **接受率估算** (Reviewer #37): 1 task ~40% / 2 tasks+2 model ~55-65% / 4 tasks+3 model ~65-75%
62	
63	### R2: Novelty of EE-only limitation
64	"任何了解机器人运动学的人都知道肘部会碰"
65	→ **应对**: 强调定量分析 (arm-body vs EE 碰撞比例量化 + oracle 排除其他解释) 而非定性观察; 作为 supporting claim 而非 primary
66	
67	### R3: No positive result
68	"告诉我什么不 work 但没告诉我什么 work"
69	→ **应对**: real_CAR 指标是 positive 工具贡献; Pi0.5+A1 如果成功也是正面结果; diagnostic framework 有方法论价值
70	
71	### R4: Action collapse is trivial
72	"Undertrained Pi0 的 action collapse 不是 safety 特有的, 是训练不足的自然结果"
73	→ **应对**: 必须在论文中承认这一点; 但指出即使原因 trivial, metric contamination 的后果 non-trivial — 后续工作可能基于被污染的 CAR 得出错误结论
74	
75	## Figure Plan
76	
77	| ID | 内容 | 优先级 | 数据来源 |
78	|----|------|--------|---------|
79	| Fig 1 | Fake vs real safety 概念图 | 重要 | 设计 |
80	| Fig 2 | Displacement 分布 (A1 vs baseline vs Pi0.5) | **必须** | 800ep A1 + 200ep baseline + 600ep Pi0.5 |
81	| Fig 3 | TSR-CAR scatter + obstacle geometry 2-panel | 重要 | 多模型/多方法数据 + per-task geometry |
82	| Fig 4 | Oracle refinement CAR bar chart | **必须** | 3 oracle variants + baselines |
83	| Table 1 | 3-seed × 2-lambda 完整结果矩阵 | **必须** | Pi0.5+A1 训练结果 (pending) |
84	| Fig 5 | Lambda-CAR 曲线 (4 点: 0, 0.005, 0.01, 0.1) | 重要 | pure LoRA + A1 训练 (pending) |
85	
86	> Fig 3 合并了原 Fig 3 (TSR-CAR scatter) 和 Fig 4 (geometry vs CAR), 按 Reviewer 建议
87	
88	## Target Venue
89	
90	**Primary**: CoRL 2026 Main / ICRA 2027 (用户明确要求主会，不是 workshop)
91	**条件**: 需要至少一个正向贡献（Pi0.5+A1 成功 / 新 SDF 集成方式 / full-body SDF PoC）
92	
93	## Narrative Focus (Reviewer Report #30)
94	
95	论文核心贡献应聚焦于 **结构性洞察**（EE-only SDF 无法影响 full-body safety），而非 negative results 堆叠。三次方法失败（A1 openpi / A3 runtime / A1 Pi0.5）如果 root cause 相同，论文叙事应集中在这个 structural insight，各实验作为不同角度的验证。
96	
97	## Negative Results Narrative Strategy (D018 + 16 negatives)
98	
99	16 个阴性结果按叙事功能分为 3 层：
100	
101	### Tier A: 显式讨论（核心贡献，论文 §4-5 正文）
102	这些 negative 本身就是 paper 的 finding：
103	
104	| 类别 | 实验 | 论文功能 |
105	|------|------|----------|
106	| Fake safety 量化 | A1-openpi 800ep (99.6% fake) | Claim 1 主证据 |
107	| EE-only oracle 失败 | 3× GT oracle (adaptive/fixed/feature) | Claim 3 主证据 |
108	| Gradient correction 失败 | collapsed policy 不接受修正 (D018) | Claim 3 补充机制分析 |
109	| Task 3 碰撞转移 | SDF gradient 导致碰撞重分布 (D017) | Claim 3 补充（structural limitation） |
110	
111	### Tier B: 简要讨论（Ablation / boundary condition，论文 §5 或 Appendix）
112	提供边界信息，但非核心贡献：
113	
114	| 类别 | 实验 | 论文功能 |
115	|------|------|----------|
116	| TSR-CAR tradeoff | Pi0.5+A1 10K/30K TSR 下降 | Claim 4 tradeoff 定量（Table 1 已含） |
117	| Lambda sensitivity | λ=0.005 vs 0.01 差异 | Figure 5 lambda 曲线的数据点 |
118	
119	### Tier C: 省略（技术失败 / 与结论无关）
120	不进入论文正文或 appendix：
121	
122	- spatial_bowl 训练失败（磁盘满 / 代码 bug → 非科学结论）
123	- A3 runtime refine 早期版本（被 oracle 实验 supersede）
124	- 被 kill 的实验（资源调度，无结论）
125	
126	### 叙事原则
127	1. Tier A 的 negative 不是"失败"，是 **evidence for structural claims** — 用 "we demonstrate" 而非 "we failed to"
128	2. 多个 Tier A negative 收敛到同一 root cause (EE-only limitation) 时，叙事集中在 insight 上，各实验作为不同角度的验证
129	3. Tier B 以 1-2 句话出现在 results discussion 或 appendix，不展开
130	4. Tier C 完全不提
131	
132	## Contingency Plans (Post Step-10K Eval)
133	
134	**场景 1 (最可能)**: λ=0.005 ≈ λ=0.01, 均 ≤ baseline → SDF signal 被 action loss 淹没
135	→ Early-stop λ=0.01 runs, 用释放 GPU 跑纯 LoRA baseline + λ=0.1 bracket
136	→ 纯 analysis paper, 聚焦 structural insight
137	
138	**场景 2**: 两个 lambda 均 > baseline, 无差异 → 改善可能来自 LoRA 本身
139	→ 必须对比纯 LoRA baseline 才能归因
140	→ 无纯 LoRA baseline 的 CAR 改善不可发表
141	
142	**场景 2a-2d (LoRA 中间场景，Reviewer 预审补充)**:
143	
144	| LoRA-only CAR | SDF 增量 | 叙事策略 |
145	|---------------|----------|----------|
146	| ~27% (≈baseline) | +30pp 全归 SDF | "geometric supervision is effective" — 最强 method claim |
147	| ~35% | +22pp | "LoRA capacity tuning helps, SDF provides major additional benefit" — 仍强 |
148	| ~45% | +12pp | "LoRA is primary driver, SDF provides dose-dependent safety margin" — 需 4-point lambda 曲线支撑 monotonic trend |
149	| ~55%+ (≈A1) | ≈0pp | 归纯 LoRA → pure analysis paper, SDF 作为 negative evidence |
150	
151	关键防御：即使 SDF 增量仅 +10-15pp，只要 4-point lambda 曲线呈 monotonic trend，仍可 claim "geometric supervision signal provides dose-dependent safety improvement beyond LoRA capacity tuning"。
152	
153	**场景 3**: λ=0.01 > λ=0.005 → SDF 有效
154	→ 继续到 30K, 升级为 "analysis paper with positive method contribution"（非纯 method paper）
155	→ 加 λ=0 (pure LoRA) + λ=0.1 构建 4-point lambda 曲线, 支持 "sweet spot" claim
156	→ 扩展到 spatial_bowl 第 2 task, 强化泛化性
157	
158	## Dependencies
159	
160	- [ ] Pi0.5+A1 训练结果 (Claim 4, Table 1) — ETA 5/24 18:00
161	- [ ] Step 10K mid-eval — ETA 5/23 ~16:25 UTC
162	- [ ] 纯 LoRA baseline (无 SDF/EE loss) — **RUNNING** (westd-45947, 2-seed, ETA ~5/26 01:30)
163	- [ ] λ=0.1 bracket (1-seed Pi0.5) — 10K eval 后启动, 4-point lambda 曲线必需
164	- [ ] spatial_bowl A1 训练 (2-seed × best-lambda) — **代码准备中（Agent 已派 Worker）**, 必须 5/28 前启动（CoRL DDL 约束）
165	- [ ] OpenVLA zero-shot SafeLIBERO eval — 仅 inference, 验证 fake safety 跨模型存在
166	- [x] Pi0.5 baseline 3-seed (Claim 2) — CAR=26.8±1.6%
167	- [x] A1 fake safety 800ep (Claim 1) — 99.6% fake
168	- [x] Oracle 3 variants (Claim 3) — all < baseline
169	- [x] Spatial/object collision analysis (Claim 3) — arm-body dominant
170	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e30124b-e11f-468d-b9f7-1ea1e18990b4",
  "uuid": "882b872f-5b7a-4b45-a099-86989b160691",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md",
      "content": "# ColliForce-VLA Paper Framing\n\n> 维护者: Director | 最后更新: 2026-05-24 12:30 UTC | Reviewer 预审反馈：补 LoRA 中间场景叙事 + Claim 4 措辞升级\n\n## Core Insight\n\n当前 VLA safety 评估存在系统性缺陷：collision avoidance rate (CAR) 被 action collapse 严重污染，导致 \"安全\" 指标虚高。我们通过大规模实证分析（39 个实验, 5000+ episodes）揭示三个相互关联的问题，并提出 displacement-filtered CAR 作为修正指标。\n\n## Working Title\n\n\"The Safety Illusion: How Action Collapse Contaminates Collision Avoidance Metrics in Vision-Language-Action Models\"\n\n> 注：Title scope 已按 Reviewer Report #26 建议收窄——不再 claim 覆盖 \"all SDF methods\"，聚焦 metric contamination 这一更可防御的贡献\n\n## Core Claims\n\n### Claim 1: Fake Safety (Primary — 证据强度 ★★★★★)\nCAR 指标被 action collapse 严重污染。在 SafeLIBERO benchmark 上，A1 (SDF auxiliary loss) 的 91.5% CAR 中 99.6% 是 fake safe（robot displacement < 1μm）。\"Collision-free\" ≠ \"collision-avoiding\"。\n\n**证据**: 800 episodes A1 per-episode displacement 分析; 200 episodes baseline 对比; Pi0.5 56/56 safe episodes displacement ≈ 0\n\n**贡献**: 提出 displacement-filtered CAR (real_CAR) 作为修正指标\n\n### Claim 2: Task Capability vs Safety Anti-correlation (Secondary — 证据强度 ★★★)\n更强的 base model 完成更多任务但碰撞更多。Pi0.5 (TSR=74.7%) vs Pi0 (TSR≈0%): 能力越强 → 运动越多 → 碰撞越多。\n\n**证据**: Pi0.5 3-seed eval (TSR=74.7±1.5%, CAR=26.8±1.6%) vs Pi0 baseline (TSR≈0%, CAR=82%)\n\n**限制**: 仅 2 个 model families, Pi0 的 \"高 CAR\" 来自 action collapse 而非安全。Reviewer 建议降级为 observation, 不 claim 因果关系。\n\n### Claim 3: EE-only SDF Structural Limitation (Supporting — 证据强度 ★★★★)\nEnd-effector-only SDF 在 action space 的碰撞避免存在结构性缺陷：SDF gradient 推 EE 远离障碍物但导致 arm body 扫过障碍物。\n\n**证据**: 3 组 GT SDF oracle (adaptive alpha, fixed alpha, feature-space) 均劣于 baseline; spatial vs object 碰撞部位分析; obstacle 高度/体积与碰撞率的单调关系\n\n**限制**: \"EE-only 不够\" 是 expected result; 缺乏 full-body SDF 对照\n\n### Claim 4: SDF Auxiliary Loss Effectiveness on Strong VLA (Pending — 取决于实验)\n在能力充分的 VLA (Pi0.5) 上，SDF auxiliary training loss 能否产生真实的碰撞避免行为？\n\n**状态**: 3-seed × 2-lambda 训练中, 预计 5/24 18:00 出结果\n\n**Framing 策略 (Reviewer #37)**：即使最优结果也定位为 **\"analysis paper with positive method contribution\"**，而非纯 method paper。原因：analysis 贡献 scope-proof（适用所有 VLA），method 贡献 scope-limited（1-2 models, 2-4 tasks）。SDF aux loss 作为 secondary proof-of-concept，证明 \"问题可解决\" 以验证 analysis 框架的价值。\n\n**Claim 措辞上限** (按 Reviewer 预审升级，基于 10K +30pp 证据): \"Training-time SDF auxiliary loss yields substantial collision avoidance improvement (+Xpp displacement-filtered CAR, frozen_rate=0%) on Pi0.5, confirming that geometric supervision effectively addresses action-collapse-contaminated safety in capable VLAs — at a moderate task performance cost (TSR: 74.7%→Y%)\"（必须包含 TSR tradeoff；禁区: SOTA / consistently outperforms / general solution）\n\n**如果成功 (CAR ≥ 33%)**: 升级为 method contribution (secondary)\n**如果失败**: 额外 negative evidence, 强化 structural insight\n\n**泛化扩展计划 (Reviewer #37, 提升接受率)**：\n- 必须: spatial_bowl 第 2 task 训练（代码准备中）→ 接受率 40% → 55-65%\n- 应该做: OpenVLA zero-shot eval 验证 fake safety 在第 3 model 上存在（仅 inference）\n- 应该做: 4-point lambda 曲线 (0, 0.005, 0.01, 0.1) 支持 \"sweet spot\" claim\n- Nice-to-have: SafeLIBERO 4 suite 各 1 task\n\n## Anticipated Reviewer Concerns\n\n### R1 (最致命): Generalizability\n\"仅在 SafeLIBERO + Pi0 系列上验证, 凭什么说 fake safety 是普遍问题?\"\n→ **应对**: (1) 2+ tasks (object_pudding + spatial_bowl, 代码准备中); (2) 3+ models 的 analysis (Pi0 + Pi0.5 已有, 加 OpenVLA zero-shot eval); (3) 收窄 claim scope + discussion 中做机制分析\n→ **接受率估算** (Reviewer #37): 1 task ~40% / 2 tasks+2 model ~55-65% / 4 tasks+3 model ~65-75%\n\n### R2: Novelty of EE-only limitation\n\"任何了解机器人运动学的人都知道肘部会碰\"\n→ **应对**: 强调定量分析 (arm-body vs EE 碰撞比例量化 + oracle 排除其他解释) 而非定性观察; 作为 supporting claim 而非 primary\n\n### R3: No positive result\n\"告诉我什么不 work 但没告诉我什么 work\"\n→ **应对**: real_CAR 指标是 positive 工具贡献; Pi0.5+A1 如果成功也是正面结果; diagnostic framework 有方法论价值\n\n### R4: Action collapse is trivial\n\"Undertrained Pi0 的 action collapse 不是 safety 特有的, 是训练不足的自然结果\"\n→ **应对**: 必须在论文中承认这一点; 但指出即使原因 trivial, metric contamination 的后果 non-trivial — 后续工作可能基于被污染的 CAR 得出错误结论\n\n## Figure Plan\n\n| ID | 内容 | 优先级 | 数据来源 |\n|----|------|--------|---------|\n| Fig 1 | Fake vs real safety 概念图 | 重要 | 设计 |\n| Fig 2 | Displacement 分布 (A1 vs baseline vs Pi0.5) | **必须** | 800ep A1 + 200ep baseline + 600ep Pi0.5 |\n| Fig 3 | TSR-CAR scatter + obstacle geometry 2-panel | 重要 | 多模型/多方法数据 + per-task geometry |\n| Fig 4 | Oracle refinement CAR bar chart | **必须** | 3 oracle variants + baselines |\n| Table 1 | 3-seed × 2-lambda 完整结果矩阵 | **必须** | Pi0.5+A1 训练结果 (pending) |\n| Fig 5 | Lambda-CAR 曲线 (4 点: 0, 0.005, 0.01, 0.1) | 重要 | pure LoRA + A1 训练 (pending) |\n\n> Fig 3 合并了原 Fig 3 (TSR-CAR scatter) 和 Fig 4 (geometry vs CAR), 按 Reviewer 建议\n\n## Target Venue\n\n**Primary**: CoRL 2026 Main / ICRA 2027 (用户明确要求主会，不是 workshop)\n**条件**: 需要至少一个正向贡献（Pi0.5+A1 成功 / 新 SDF 集成方式 / full-body SDF PoC）\n\n## Narrative Focus (Reviewer Report #30)\n\n论文核心贡献应聚焦于 **结构性洞察**（EE-only SDF 无法影响 full-body safety），而非 negative results 堆叠。三次方法失败（A1 openpi / A3 runtime / A1 Pi0.5）如果 root cause 相同，论文叙事应集中在这个 structural insight，各实验作为不同角度的验证。\n\n## Negative Results Narrative Strategy (D018 + 16 negatives)\n\n16 个阴性结果按叙事功能分为 3 层：\n\n### Tier A: 显式讨论（核心贡献，论文 §4-5 正文）\n这些 negative 本身就是 paper 的 finding：\n\n| 类别 | 实验 | 论文功能 |\n|------|------|----------|\n| Fake safety 量化 | A1-openpi 800ep (99.6% fake) | Claim 1 主证据 |\n| EE-only oracle 失败 | 3× GT oracle (adaptive/fixed/feature) | Claim 3 主证据 |\n| Gradient correction 失败 | collapsed policy 不接受修正 (D018) | Claim 3 补充机制分析 |\n| Task 3 碰撞转移 | SDF gradient 导致碰撞重分布 (D017) | Claim 3 补充（structural limitation） |\n\n### Tier B: 简要讨论（Ablation / boundary condition，论文 §5 或 Appendix）\n提供边界信息，但非核心贡献：\n\n| 类别 | 实验 | 论文功能 |\n|------|------|----------|\n| TSR-CAR tradeoff | Pi0.5+A1 10K/30K TSR 下降 | Claim 4 tradeoff 定量（Table 1 已含） |\n| Lambda sensitivity | λ=0.005 vs 0.01 差异 | Figure 5 lambda 曲线的数据点 |\n\n### Tier C: 省略（技术失败 / 与结论无关）\n不进入论文正文或 appendix：\n\n- spatial_bowl 训练失败（磁盘满 / 代码 bug → 非科学结论）\n- A3 runtime refine 早期版本（被 oracle 实验 supersede）\n- 被 kill 的实验（资源调度，无结论）\n\n### 叙事原则\n1. Tier A 的 negative 不是\"失败\"，是 **evidence for structural claims** — 用 \"we demonstrate\" 而非 \"we failed to\"\n2. 多个 Tier A negative 收敛到同一 root cause (EE-only limitation) 时，叙事集中在 insight 上，各实验作为不同角度的验证\n3. Tier B 以 1-2 句话出现在 results discussion 或 appendix，不展开\n4. Tier C 完全不提\n\n## Contingency Plans (Post Step-10K Eval)\n\n**场景 1 (最可能)**: λ=0.005 ≈ λ=0.01, 均 ≤ baseline → SDF signal 被 action loss 淹没\n→ Early-stop λ=0.01 runs, 用释放 GPU 跑纯 LoRA baseline + λ=0.1 bracket\n→ 纯 analysis paper, 聚焦 structural insight\n\n**场景 2**: 两个 lambda 均 > baseline, 无差异 → 改善可能来自 LoRA 本身\n→ 必须对比纯 LoRA baseline 才能归因\n→ 无纯 LoRA baseline 的 CAR 改善不可发表\n\n**场景 2a-2d (LoRA 中间场景，Reviewer 预审补充)**:\n\n| LoRA-only CAR | SDF 增量 | 叙事策略 |\n|---------------|----------|----------|\n| ~27% (≈baseline) | +30pp 全归 SDF | \"geometric supervision is effective\" — 最强 method claim |\n| ~35% | +22pp | \"LoRA capacity tuning helps, SDF provides major additional benefit\" — 仍强 |\n| ~45% | +12pp | \"LoRA is primary driver, SDF provides dose-dependent safety margin\" — 需 4-point lambda 曲线支撑 monotonic trend |\n| ~55%+ (≈A1) | ≈0pp | 归纯 LoRA → pure analysis paper, SDF 作为 negative evidence |\n\n关键防御：即使 SDF 增量仅 +10-15pp，只要 4-point lambda 曲线呈 monotonic trend，仍可 claim \"geometric supervision signal provides dose-dependent safety improvement beyond LoRA capacity tuning\"。\n\n**场景 3**: λ=0.01 > λ=0.005 → SDF 有效\n→ 继续到 30K, 升级为 \"analysis paper with positive method contribution\"（非纯 method paper）\n→ 加 λ=0 (pure LoRA) + λ=0.1 构建 4-point lambda 曲线, 支持 \"sweet spot\" claim\n→ 扩展到 spatial_bowl 第 2 task, 强化泛化性\n\n## Dependencies\n\n- [ ] Pi0.5+A1 训练结果 (Claim 4, Table 1) — ETA 5/24 18:00\n- [ ] Step 10K mid-eval — ETA 5/23 ~16:25 UTC\n- [ ] 纯 LoRA baseline (无 SDF/EE loss) — **RUNNING** (westd-45947, 2-seed, ETA ~5/26 01:30)\n- [ ] λ=0.1 bracket (1-seed Pi0.5) — 10K eval 后启动, 4-point lambda 曲线必需\n- [ ] spatial_bowl A1 训练 (2-seed × best-lambda) — **代码准备中（Agent 已派 Worker）**, 必须 5/28 前启动（CoRL DDL 约束）\n- [ ] OpenVLA zero-shot SafeLIBERO eval — 仅 inference, 验证 fake safety 跨模型存在\n- [x] Pi0.5 baseline 3-seed (Claim 2) — CAR=26.8±1.6%\n- [x] A1 fake safety 800ep (Claim 1) — 99.6% fake\n- [x] Oracle 3 variants (Claim 3) — all < baseline\n- [x] Spatial/object collision analysis (Claim 3) — arm-body dominant\n",
      "numLines": 170,
      "startLine": 1,
      "totalLines": 170
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

现在替换旧的 3-tier 结构为 Director 批准的 4-block 结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e30124b-e11f-468d-b9f7-1ea1e18990b4",
  "uuid": "b91f0c54-92d8-4b7a-a434-6f7a8030fcf0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NSGmzz7ydNVNNQiaoEo8Jw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5006,
      "cache_read_input_tokens": 28962,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5006
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

_source line 15_

<details open><summary>🔧 Tool call — Edit · `toolu_017qGFGVGiJMUoonYjqo8C7F`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md",
  "old_string": "## Negative Results Narrative Strategy (D018 + 16 negatives)\n\n16 个阴性结果按叙事功能分为 3 层：\n\n### Tier A: 显式讨论（核心贡献，论文 §4-5 正文）\n这些 negative 本身就是 paper 的 finding：\n\n| 类别 | 实验 | 论文功能 |\n|------|------|----------|\n| Fake safety 量化 | A1-openpi 800ep (99.6% fake) | Claim 1 主证据 |\n| EE-only oracle 失败 | 3× GT oracle (adaptive/fixed/feature) | Claim 3 主证据 |\n| Gradient correction 失败 | collapsed policy 不接受修正 (D018) | Claim 3 补充机制分析 |\n| Task 3 碰撞转移 | SDF gradient 导致碰撞重分布 (D017) | Claim 3 补充（structural limitation） |\n\n### Tier B: 简要讨论（Ablation / boundary condition，论文 §5 或 Appendix）\n提供边界信息，但非核心贡献：\n\n| 类别 | 实验 | 论文功能 |\n|------|------|----------|\n| TSR-CAR tradeoff | Pi0.5+A1 10K/30K TSR 下降 | Claim 4 tradeoff 定量（Table 1 已含） |\n| Lambda sensitivity | λ=0.005 vs 0.01 差异 | Figure 5 lambda 曲线的数据点 |\n\n### Tier C: 省略（技术失败 / 与结论无关）\n不进入论文正文或 appendix：\n\n- spatial_bowl 训练失败（磁盘满 / 代码 bug → 非科学结论）\n- A3 runtime refine 早期版本（被 oracle 实验 supersede）\n- 被 kill 的实验（资源调度，无结论）\n\n### 叙事原则\n1. Tier A 的 negative 不是\"失败\"，是 **evidence for structural claims** — 用 \"we demonstrate\" 而非 \"we failed to\"\n2. 多个 Tier A negative 收敛到同一 root cause (EE-only limitation) 时，叙事集中在 insight 上，各实验作为不同角度的验证\n3. Tier B 以 1-2 句话出现在 results discussion 或 appendix，不展开\n4. Tier C 完全不提",
  "new_string": "## Negative Results Narrative (4 Blocks)\n\n> Director 批准的 4-block 叙事结构（替代原 7 段独立叙事），每个 block 对应一个独立论点，论文 §4-5 按此顺序展开。\n\n### Block 1: Fake Safety Revelation\n- **Evidence**: eval_a1_lora_object_v11_rerun (800 episodes)\n- **Key finding**: CAR=91.5% with 99.6% fake safe (displacement < 0.1mm)\n- **Narrative**: Standard CAR metric is systematically contaminated by action collapse — \"collision-free\" episodes are actually frozen robots, not collision-avoiding ones. Proposes displacement-filtered CAR (real_CAR) as corrective metric.\n- **Supports**: Claim 1 (Primary)\n\n### Block 2: Stronger Models ≠ Safer (merged)\n- **Evidence**: eval_pi05_safelibero_object_v11 + eval_pi05_safelibero_spatial_v11\n- **Key finding**: Pi0.5 CAR=28% (object), 13% (spatial), real_safe=0.5%\n- **Narrative**: Counter-intuitive — better task capability (TSR=74.7%) leads to more collisions, not fewer. Pi0's high CAR (82%) is fake safety from action collapse; Pi0.5 actually moves and collides. Capability↑ ≠ Safety↑.\n- **Supports**: Claim 2 (Secondary)\n\n### Block 3: Oracle Upper Bound (merged triplet)\n- **Evidence**: oracle_true_gt_adaptive_alpha_v11 + oracle_true_gt_fixed_alpha_v11 + oracle_true_gt_feature_v11\n- **Key finding**: All oracles CAR 73-77% < baseline 82-83%\n- **Narrative**: Unified answer to \"does a better alpha schedule or representation fix runtime refinement?\" — No. Three oracle variants (adaptive alpha, fixed alpha, feature-space SDF) all perform worse than baseline, because gradient correction structurally fails on collapsed policies regardless of alpha/representation choice. Eliminates hyperparameter tuning as escape route.\n- **Supports**: Claim 3 (Supporting)\n- **Presentation**: Single unified table with 3 oracle rows + baseline row\n\n### Block 4: EE-only Boundary Condition\n- **Evidence**: eval_a1_lora_spatial_v11\n- **Key finding**: CAR≈0% in spatial tasks, all 6 safe episodes are frozen (displacement ≈ 0)\n- **Narrative**: EE-only SDF cannot address arm-body collisions — in spatial tasks where collisions come from the arm body sweeping through obstacles, EE-based correction has zero effect. Defines the structural scope boundary of the method.\n- **Supports**: Claim 3 (Supporting, boundary condition)\n\n### 叙事原则\n1. 每个 block 不是\"失败\"，是 **evidence for structural claims** — 用 \"we demonstrate\" / \"we find\" 而非 \"we failed to\"\n2. Block 3 的三个 oracle 合并为一段 + 一个表格，统一回答一个问题，避免重复叙事\n3. Block 间按逻辑递进排列：metric 有问题 (B1) → 强模型也不安全 (B2) → runtime 修正无法解决 (B3) → method scope 边界 (B4)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e30124b-e11f-468d-b9f7-1ea1e18990b4",
  "uuid": "613f3efe-dc9a-4c93-a7f7-cb076e97ad76",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NSGmzz7ydNVNNQiaoEo8Jw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5006,
      "cache_read_input_tokens": 28962,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5006
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

_source line 16 · 2026-05-25T09:14:33.407Z_

<details><summary>↩ Tool result · `toolu_017qGFGVGiJMUoonYjqo8C7F`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e30124b-e11f-468d-b9f7-1ea1e18990b4",
  "uuid": "323e3a1d-3b0c-478e-afa3-edfeaf3cd576",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md",
    "oldString": "## Negative Results Narrative Strategy (D018 + 16 negatives)\n\n16 个阴性结果按叙事功能分为 3 层：\n\n### Tier A: 显式讨论（核心贡献，论文 §4-5 正文）\n这些 negative 本身就是 paper 的 finding：\n\n| 类别 | 实验 | 论文功能 |\n|------|------|----------|\n| Fake safety 量化 | A1-openpi 800ep (99.6% fake) | Claim 1 主证据 |\n| EE-only oracle 失败 | 3× GT oracle (adaptive/fixed/feature) | Claim 3 主证据 |\n| Gradient correction 失败 | collapsed policy 不接受修正 (D018) | Claim 3 补充机制分析 |\n| Task 3 碰撞转移 | SDF gradient 导致碰撞重分布 (D017) | Claim 3 补充（structural limitation） |\n\n### Tier B: 简要讨论（Ablation / boundary condition，论文 §5 或 Appendix）\n提供边界信息，但非核心贡献：\n\n| 类别 | 实验 | 论文功能 |\n|------|------|----------|\n| TSR-CAR tradeoff | Pi0.5+A1 10K/30K TSR 下降 | Claim 4 tradeoff 定量（Table 1 已含） |\n| Lambda sensitivity | λ=0.005 vs 0.01 差异 | Figure 5 lambda 曲线的数据点 |\n\n### Tier C: 省略（技术失败 / 与结论无关）\n不进入论文正文或 appendix：\n\n- spatial_bowl 训练失败（磁盘满 / 代码 bug → 非科学结论）\n- A3 runtime refine 早期版本（被 oracle 实验 supersede）\n- 被 kill 的实验（资源调度，无结论）\n\n### 叙事原则\n1. Tier A 的 negative 不是\"失败\"，是 **evidence for structural claims** — 用 \"we demonstrate\" 而非 \"we failed to\"\n2. 多个 Tier A negative 收敛到同一 root cause (EE-only limitation) 时，叙事集中在 insight 上，各实验作为不同角度的验证\n3. Tier B 以 1-2 句话出现在 results discussion 或 appendix，不展开\n4. Tier C 完全不提",
    "newString": "## Negative Results Narrative (4 Blocks)\n\n> Director 批准的 4-block 叙事结构（替代原 7 段独立叙事），每个 block 对应一个独立论点，论文 §4-5 按此顺序展开。\n\n### Block 1: Fake Safety Revelation\n- **Evidence**: eval_a1_lora_object_v11_rerun (800 episodes)\n- **Key finding**: CAR=91.5% with 99.6% fake safe (displacement < 0.1mm)\n- **Narrative**: Standard CAR metric is systematically contaminated by action collapse — \"collision-free\" episodes are actually frozen robots, not collision-avoiding ones. Proposes displacement-filtered CAR (real_CAR) as corrective metric.\n- **Supports**: Claim 1 (Primary)\n\n### Block 2: Stronger Models ≠ Safer (merged)\n- **Evidence**: eval_pi05_safelibero_object_v11 + eval_pi05_safelibero_spatial_v11\n- **Key finding**: Pi0.5 CAR=28% (object), 13% (spatial), real_safe=0.5%\n- **Narrative**: Counter-intuitive — better task capability (TSR=74.7%) leads to more collisions, not fewer. Pi0's high CAR (82%) is fake safety from action collapse; Pi0.5 actually moves and collides. Capability↑ ≠ Safety↑.\n- **Supports**: Claim 2 (Secondary)\n\n### Block 3: Oracle Upper Bound (merged triplet)\n- **Evidence**: oracle_true_gt_adaptive_alpha_v11 + oracle_true_gt_fixed_alpha_v11 + oracle_true_gt_feature_v11\n- **Key finding**: All oracles CAR 73-77% < baseline 82-83%\n- **Narrative**: Unified answer to \"does a better alpha schedule or representation fix runtime refinement?\" — No. Three oracle variants (adaptive alpha, fixed alpha, feature-space SDF) all perform worse than baseline, because gradient correction structurally fails on collapsed policies regardless of alpha/representation choice. Eliminates hyperparameter tuning as escape route.\n- **Supports**: Claim 3 (Supporting)\n- **Presentation**: Single unified table with 3 oracle rows + baseline row\n\n### Block 4: EE-only Boundary Condition\n- **Evidence**: eval_a1_lora_spatial_v11\n- **Key finding**: CAR≈0% in spatial tasks, all 6 safe episodes are frozen (displacement ≈ 0)\n- **Narrative**: EE-only SDF cannot address arm-body collisions — in spatial tasks where collisions come from the arm body sweeping through obstacles, EE-based correction has zero effect. Defines the structural scope boundary of the method.\n- **Supports**: Claim 3 (Supporting, boundary condition)\n\n### 叙事原则\n1. 每个 block 不是\"失败\"，是 **evidence for structural claims** — 用 \"we demonstrate\" / \"we find\" 而非 \"we failed to\"\n2. Block 3 的三个 oracle 合并为一段 + 一个表格，统一回答一个问题，避免重复叙事\n3. Block 间按逻辑递进排列：metric 有问题 (B1) → 强模型也不安全 (B2) → runtime 修正无法解决 (B3) → method scope 边界 (B4)",
    "originalFile": "# ColliForce-VLA Paper Framing\n\n> 维护者: Director | 最后更新: 2026-05-24 12:30 UTC | Reviewer 预审反馈：补 LoRA 中间场景叙事 + Claim 4 措辞升级\n\n## Core Insight\n\n当前 VLA safety 评估存在系统性缺陷：collision avoidance rate (CAR) 被 action collapse 严重污染，导致 \"安全\" 指标虚高。我们通过大规模实证分析（39 个实验, 5000+ episodes）揭示三个相互关联的问题，并提出 displacement-filtered CAR 作为修正指标。\n\n## Working Title\n\n\"The Safety Illusion: How Action Collapse Contaminates Collision Avoidance Metrics in Vision-Language-Action Models\"\n\n> 注：Title scope 已按 Reviewer Report #26 建议收窄——不再 claim 覆盖 \"all SDF methods\"，聚焦 metric contamination 这一更可防御的贡献\n\n## Core Claims\n\n### Claim 1: Fake Safety (Primary — 证据强度 ★★★★★)\nCAR 指标被 action collapse 严重污染。在 SafeLIBERO benchmark 上，A1 (SDF auxiliary loss) 的 91.5% CAR 中 99.6% 是 fake safe（robot displacement < 1μm）。\"Collision-free\" ≠ \"collision-avoiding\"。\n\n**证据**: 800 episodes A1 per-episode displacement 分析; 200 episodes baseline 对比; Pi0.5 56/56 safe episodes displacement ≈ 0\n\n**贡献**: 提出 displacement-filtered CAR (real_CAR) 作为修正指标\n\n### Claim 2: Task Capability vs Safety Anti-correlation (Secondary — 证据强度 ★★★)\n更强的 base model 完成更多任务但碰撞更多。Pi0.5 (TSR=74.7%) vs Pi0 (TSR≈0%): 能力越强 → 运动越多 → 碰撞越多。\n\n**证据**: Pi0.5 3-seed eval (TSR=74.7±1.5%, CAR=26.8±1.6%) vs Pi0 baseline (TSR≈0%, CAR=82%)\n\n**限制**: 仅 2 个 model families, Pi0 的 \"高 CAR\" 来自 action collapse 而非安全。Reviewer 建议降级为 observation, 不 claim 因果关系。\n\n### Claim 3: EE-only SDF Structural Limitation (Supporting — 证据强度 ★★★★)\nEnd-effector-only SDF 在 action space 的碰撞避免存在结构性缺陷：SDF gradient 推 EE 远离障碍物但导致 arm body 扫过障碍物。\n\n**证据**: 3 组 GT SDF oracle (adaptive alpha, fixed alpha, feature-space) 均劣于 baseline; spatial vs object 碰撞部位分析; obstacle 高度/体积与碰撞率的单调关系\n\n**限制**: \"EE-only 不够\" 是 expected result; 缺乏 full-body SDF 对照\n\n### Claim 4: SDF Auxiliary Loss Effectiveness on Strong VLA (Pending — 取决于实验)\n在能力充分的 VLA (Pi0.5) 上，SDF auxiliary training loss 能否产生真实的碰撞避免行为？\n\n**状态**: 3-seed × 2-lambda 训练中, 预计 5/24 18:00 出结果\n\n**Framing 策略 (Reviewer #37)**：即使最优结果也定位为 **\"analysis paper with positive method contribution\"**，而非纯 method paper。原因：analysis 贡献 scope-proof（适用所有 VLA），method 贡献 scope-limited（1-2 models, 2-4 tasks）。SDF aux loss 作为 secondary proof-of-concept，证明 \"问题可解决\" 以验证 analysis 框架的价值。\n\n**Claim 措辞上限** (按 Reviewer 预审升级，基于 10K +30pp 证据): \"Training-time SDF auxiliary loss yields substantial collision avoidance improvement (+Xpp displacement-filtered CAR, frozen_rate=0%) on Pi0.5, confirming that geometric supervision effectively addresses action-collapse-contaminated safety in capable VLAs — at a moderate task performance cost (TSR: 74.7%→Y%)\"（必须包含 TSR tradeoff；禁区: SOTA / consistently outperforms / general solution）\n\n**如果成功 (CAR ≥ 33%)**: 升级为 method contribution (secondary)\n**如果失败**: 额外 negative evidence, 强化 structural insight\n\n**泛化扩展计划 (Reviewer #37, 提升接受率)**：\n- 必须: spatial_bowl 第 2 task 训练（代码准备中）→ 接受率 40% → 55-65%\n- 应该做: OpenVLA zero-shot eval 验证 fake safety 在第 3 model 上存在（仅 inference）\n- 应该做: 4-point lambda 曲线 (0, 0.005, 0.01, 0.1) 支持 \"sweet spot\" claim\n- Nice-to-have: SafeLIBERO 4 suite 各 1 task\n\n## Anticipated Reviewer Concerns\n\n### R1 (最致命): Generalizability\n\"仅在 SafeLIBERO + Pi0 系列上验证, 凭什么说 fake safety 是普遍问题?\"\n→ **应对**: (1) 2+ tasks (object_pudding + spatial_bowl, 代码准备中); (2) 3+ models 的 analysis (Pi0 + Pi0.5 已有, 加 OpenVLA zero-shot eval); (3) 收窄 claim scope + discussion 中做机制分析\n→ **接受率估算** (Reviewer #37): 1 task ~40% / 2 tasks+2 model ~55-65% / 4 tasks+3 model ~65-75%\n\n### R2: Novelty of EE-only limitation\n\"任何了解机器人运动学的人都知道肘部会碰\"\n→ **应对**: 强调定量分析 (arm-body vs EE 碰撞比例量化 + oracle 排除其他解释) 而非定性观察; 作为 supporting claim 而非 primary\n\n### R3: No positive result\n\"告诉我什么不 work 但没告诉我什么 work\"\n→ **应对**: real_CAR 指标是 positive 工具贡献; Pi0.5+A1 如果成功也是正面结果; diagnostic framework 有方法论价值\n\n### R4: Action collapse is trivial\n\"Undertrained Pi0 的 action collapse 不是 safety 特有的, 是训练不足的自然结果\"\n→ **应对**: 必须在论文中承认这一点; 但指出即使原因 trivial, metric contamination 的后果 non-trivial — 后续工作可能基于被污染的 CAR 得出错误结论\n\n## Figure Plan\n\n| ID | 内容 | 优先级 | 数据来源 |\n|----|------|--------|---------|\n| Fig 1 | Fake vs real safety 概念图 | 重要 | 设计 |\n| Fig 2 | Displacement 分布 (A1 vs baseline vs Pi0.5) | **必须** | 800ep A1 + 200ep baseline + 600ep Pi0.5 |\n| Fig 3 | TSR-CAR scatter + obstacle geometry 2-panel | 重要 | 多模型/多方法数据 + per-task geometry |\n| Fig 4 | Oracle refinement CAR bar chart | **必须** | 3 oracle variants + baselines |\n| Table 1 | 3-seed × 2-lambda 完整结果矩阵 | **必须** | Pi0.5+A1 训练结果 (pending) |\n| Fig 5 | Lambda-CAR 曲线 (4 点: 0, 0.005, 0.01, 0.1) | 重要 | pure LoRA + A1 训练 (pending) |\n\n> Fig 3 合并了原 Fig 3 (TSR-CAR scatter) 和 Fig 4 (geometry vs CAR), 按 Reviewer 建议\n\n## Target Venue\n\n**Primary**: CoRL 2026 Main / ICRA 2027 (用户明确要求主会，不是 workshop)\n**条件**: 需要至少一个正向贡献（Pi0.5+A1 成功 / 新 SDF 集成方式 / full-body SDF PoC）\n\n## Narrative Focus (Reviewer Report #30)\n\n论文核心贡献应聚焦于 **结构性洞察**（EE-only SDF 无法影响 full-body safety），而非 negative results 堆叠。三次方法失败（A1 openpi / A3 runtime / A1 Pi0.5）如果 root cause 相同，论文叙事应集中在这个 structural insight，各实验作为不同角度的验证。\n\n## Negative Results Narrative Strategy (D018 + 16 negatives)\n\n16 个阴性结果按叙事功能分为 3 层：\n\n### Tier A: 显式讨论（核心贡献，论文 §4-5 正文）\n这些 negative 本身就是 paper 的 finding：\n\n| 类别 | 实验 | 论文功能 |\n|------|------|----------|\n| Fake safety 量化 | A1-openpi 800ep (99.6% fake) | Claim 1 主证据 |\n| EE-only oracle 失败 | 3× GT oracle (adaptive/fixed/feature) | Claim 3 主证据 |\n| Gradient correction 失败 | collapsed policy 不接受修正 (D018) | Claim 3 补充机制分析 |\n| Task 3 碰撞转移 | SDF gradient 导致碰撞重分布 (D017) | Claim 3 补充（structural limitation） |\n\n### Tier B: 简要讨论（Ablation / boundary condition，论文 §5 或 Appendix）\n提供边界信息，但非核心贡献：\n\n| 类别 | 实验 | 论文功能 |\n|------|------|----------|\n| TSR-CAR tradeoff | Pi0.5+A1 10K/30K TSR 下降 | Claim 4 tradeoff 定量（Table 1 已含） |\n| Lambda sensitivity | λ=0.005 vs 0.01 差异 | Figure 5 lambda 曲线的数据点 |\n\n### Tier C: 省略（技术失败 / 与结论无关）\n不进入论文正文或 appendix：\n\n- spatial_bowl 训练失败（磁盘满 / 代码 bug → 非科学结论）\n- A3 runtime refine 早期版本（被 oracle 实验 supersede）\n- 被 kill 的实验（资源调度，无结论）\n\n### 叙事原则\n1. Tier A 的 negative 不是\"失败\"，是 **evidence for structural claims** — 用 \"we demonstrate\" 而非 \"we failed to\"\n2. 多个 Tier A negative 收敛到同一 root cause (EE-only limitation) 时，叙事集中在 insight 上，各实验作为不同角度的验证\n3. Tier B 以 1-2 句话出现在 results discussion 或 appendix，不展开\n4. Tier C 完全不提\n\n## Contingency Plans (Post Step-10K Eval)\n\n**场景 1 (最可能)**: λ=0.005 ≈ λ=0.01, 均 ≤ baseline → SDF signal 被 action loss 淹没\n→ Early-stop λ=0.01 runs, 用释放 GPU 跑纯 LoRA baseline + λ=0.1 bracket\n→ 纯 analysis paper, 聚焦 structural insight\n\n**场景 2**: 两个 lambda 均 > baseline, 无差异 → 改善可能来自 LoRA 本身\n→ 必须对比纯 LoRA baseline 才能归因\n→ 无纯 LoRA baseline 的 CAR 改善不可发表\n\n**场景 2a-2d (LoRA 中间场景，Reviewer 预审补充)**:\n\n| LoRA-only CAR | SDF 增量 | 叙事策略 |\n|---------------|----------|----------|\n| ~27% (≈baseline) | +30pp 全归 SDF | \"geometric supervision is effective\" — 最强 method claim |\n| ~35% | +22pp | \"LoRA capacity tuning helps, SDF provides major additional benefit\" — 仍强 |\n| ~45% | +12pp | \"LoRA is primary driver, SDF provides dose-dependent safety margin\" — 需 4-point lambda 曲线支撑 monotonic trend |\n| ~55%+ (≈A1) | ≈0pp | 归纯 LoRA → pure analysis paper, SDF 作为 negative evidence |\n\n关键防御：即使 SDF 增量仅 +10-15pp，只要 4-point lambda 曲线呈 monotonic trend，仍可 claim \"geometric supervision signal provides dose-dependent safety improvement beyond LoRA capacity tuning\"。\n\n**场景 3**: λ=0.01 > λ=0.005 → SDF 有效\n→ 继续到 30K, 升级为 \"analysis paper with positive method contribution\"（非纯 method paper）\n→ 加 λ=0 (pure LoRA) + λ=0.1 构建 4-point lambda 曲线, 支持 \"sweet spot\" claim\n→ 扩展到 spatial_bowl 第 2 task, 强化泛化性\n\n## Dependencies\n\n- [ ] Pi0.5+A1 训练结果 (Claim 4, Table 1) — ETA 5/24 18:00\n- [ ] Step 10K mid-eval — ETA 5/23 ~16:25 UTC\n- [ ] 纯 LoRA baseline (无 SDF/EE loss) — **RUNNING** (westd-45947, 2-seed, ETA ~5/26 01:30)\n- [ ] λ=0.1 bracket (1-seed Pi0.5) — 10K eval 后启动, 4-point lambda 曲线必需\n- [ ] spatial_bowl A1 训练 (2-seed × best-lambda) — **代码准备中（Agent 已派 Worker）**, 必须 5/28 前启动（CoRL DDL 约束）\n- [ ] OpenVLA zero-shot SafeLIBERO eval — 仅 inference, 验证 fake safety 跨模型存在\n- [x] Pi0.5 baseline 3-seed (Claim 2) — CAR=26.8±1.6%\n- [x] A1 fake safety 800ep (Claim 1) — 99.6% fake\n- [x] Oracle 3 variants (Claim 3) — all < baseline\n- [x] Spatial/object collision analysis (Claim 3) — arm-body dominant\n",
    "structuredPatch": [
      {
        "oldStart": 94,
        "oldLines": 40,
        "newStart": 94,
        "newLines": 39,
        "lines": [
          " ",
          " 论文核心贡献应聚焦于 **结构性洞察**（EE-only SDF 无法影响 full-body safety），而非 negative results 堆叠。三次方法失败（A1 openpi / A3 runtime / A1 Pi0.5）如果 root cause 相同，论文叙事应集中在这个 structural insight，各实验作为不同角度的验证。",
          " ",
          "-## Negative Results Narrative Strategy (D018 + 16 negatives)",
          "+## Negative Results Narrative (4 Blocks)",
          " ",
          "-16 个阴性结果按叙事功能分为 3 层：",
          "+> Director 批准的 4-block 叙事结构（替代原 7 段独立叙事），每个 block 对应一个独立论点，论文 §4-5 按此顺序展开。",
          " ",
          "-### Tier A: 显式讨论（核心贡献，论文 §4-5 正文）",
          "-这些 negative 本身就是 paper 的 finding：",
          "+### Block 1: Fake Safety Revelation",
          "+- **Evidence**: eval_a1_lora_object_v11_rerun (800 episodes)",
          "+- **Key finding**: CAR=91.5% with 99.6% fake safe (displacement < 0.1mm)",
          "+- **Narrative**: Standard CAR metric is systematically contaminated by action collapse — \"collision-free\" episodes are actually frozen robots, not collision-avoiding ones. Proposes displacement-filtered CAR (real_CAR) as corrective metric.",
          "+- **Supports**: Claim 1 (Primary)",
          " ",
          "-| 类别 | 实验 | 论文功能 |",
          "-|------|------|----------|",
          "-| Fake safety 量化 | A1-openpi 800ep (99.6% fake) | Claim 1 主证据 |",
          "-| EE-only oracle 失败 | 3× GT oracle (adaptive/fixed/feature) | Claim 3 主证据 |",
          "-| Gradient correction 失败 | collapsed policy 不接受修正 (D018) | Claim 3 补充机制分析 |",
          "-| Task 3 碰撞转移 | SDF gradient 导致碰撞重分布 (D017) | Claim 3 补充（structural limitation） |",
          "+### Block 2: Stronger Models ≠ Safer (merged)",
          "+- **Evidence**: eval_pi05_safelibero_object_v11 + eval_pi05_safelibero_spatial_v11",
          "+- **Key finding**: Pi0.5 CAR=28% (object), 13% (spatial), real_safe=0.5%",
          "+- **Narrative**: Counter-intuitive — better task capability (TSR=74.7%) leads to more collisions, not fewer. Pi0's high CAR (82%) is fake safety from action collapse; Pi0.5 actually moves and collides. Capability↑ ≠ Safety↑.",
          "+- **Supports**: Claim 2 (Secondary)",
          " ",
          "-### Tier B: 简要讨论（Ablation / boundary condition，论文 §5 或 Appendix）",
          "-提供边界信息，但非核心贡献：",
          "+### Block 3: Oracle Upper Bound (merged triplet)",
          "+- **Evidence**: oracle_true_gt_adaptive_alpha_v11 + oracle_true_gt_fixed_alpha_v11 + oracle_true_gt_feature_v11",
          "+- **Key finding**: All oracles CAR 73-77% < baseline 82-83%",
          "+- **Narrative**: Unified answer to \"does a better alpha schedule or representation fix runtime refinement?\" — No. Three oracle variants (adaptive alpha, fixed alpha, feature-space SDF) all perform worse than baseline, because gradient correction structurally fails on collapsed policies regardless of alpha/representation choice. Eliminates hyperparameter tuning as escape route.",
          "+- **Supports**: Claim 3 (Supporting)",
          "+- **Presentation**: Single unified table with 3 oracle rows + baseline row",
          " ",
          "-| 类别 | 实验 | 论文功能 |",
          "-|------|------|----------|",
          "-| TSR-CAR tradeoff | Pi0.5+A1 10K/30K TSR 下降 | Claim 4 tradeoff 定量（Table 1 已含） |",
          "-| Lambda sensitivity | λ=0.005 vs 0.01 差异 | Figure 5 lambda 曲线的数据点 |",
          "+### Block 4: EE-only Boundary Condition",
          "+- **Evidence**: eval_a1_lora_spatial_v11",
          "+- **Key finding**: CAR≈0% in spatial tasks, all 6 safe episodes are frozen (displacement ≈ 0)",
          "+- **Narrative**: EE-only SDF cannot address arm-body collisions — in spatial tasks where collisions come from the arm body sweeping through obstacles, EE-based correction has zero effect. Defines the structural scope boundary of the method.",
          "+- **Supports**: Claim 3 (Supporting, boundary condition)",
          " ",
          "-### Tier C: 省略（技术失败 / 与结论无关）",
          "-不进入论文正文或 appendix：",
          "-",
          "-- spatial_bowl 训练失败（磁盘满 / 代码 bug → 非科学结论）",
          "-- A3 runtime refine 早期版本（被 oracle 实验 supersede）",
          "-- 被 kill 的实验（资源调度，无结论）",
          "-",
          " ### 叙事原则",
          "-1. Tier A 的 negative 不是\"失败\"，是 **evidence for structural claims** — 用 \"we demonstrate\" 而非 \"we failed to\"",
          "-2. 多个 Tier A negative 收敛到同一 root cause (EE-only limitation) 时，叙事集中在 insight 上，各实验作为不同角度的验证",
          "-3. Tier B 以 1-2 句话出现在 results discussion 或 appendix，不展开",
          "-4. Tier C 完全不提",
          "+1. 每个 block 不是\"失败\"，是 **evidence for structural claims** — 用 \"we demonstrate\" / \"we find\" 而非 \"we failed to\"",
          "+2. Block 3 的三个 oracle 合并为一段 + 一个表格，统一回答一个问题，避免重复叙事",
          "+3. Block 间按逻辑递进排列：metric 有问题 (B1) → 强模型也不安全 (B2) → runtime 修正无法解决 (B3) → method scope 边界 (B4)",
          " ",
          " ## Contingency Plans (Post Step-10K Eval)",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 17_

更新时间戳。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e30124b-e11f-468d-b9f7-1ea1e18990b4",
  "uuid": "192e105a-8e37-4b9f-ad2c-54df81e47e16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JH4MJUTTLhUqxJcwDUvBwi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1777,
      "cache_read_input_tokens": 33968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1777
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

_source line 18_

<details open><summary>🔧 Tool call — Edit · `toolu_01QwQfxpr6wBhh6CngDEsc6K`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md",
  "old_string": "> 维护者: Director | 最后更新: 2026-05-24 12:30 UTC | Reviewer 预审反馈：补 LoRA 中间场景叙事 + Claim 4 措辞升级",
  "new_string": "> 维护者: Director | 最后更新: 2026-05-25 UTC | Reviewer 预审反馈：补 LoRA 中间场景叙事 + Claim 4 措辞升级 | Negative results 升级为 4-block 结构"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e30124b-e11f-468d-b9f7-1ea1e18990b4",
  "uuid": "5881bfc1-df56-468f-8e5e-f0d6187ce4c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JH4MJUTTLhUqxJcwDUvBwi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1777,
      "cache_read_input_tokens": 33968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1777
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

_source line 19 · 2026-05-25T09:14:40.175Z_

<details><summary>↩ Tool result · `toolu_01QwQfxpr6wBhh6CngDEsc6K`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e30124b-e11f-468d-b9f7-1ea1e18990b4",
  "uuid": "f9a93ae1-742c-49a7-87a2-fdddfb647ed4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md",
    "oldString": "> 维护者: Director | 最后更新: 2026-05-24 12:30 UTC | Reviewer 预审反馈：补 LoRA 中间场景叙事 + Claim 4 措辞升级",
    "newString": "> 维护者: Director | 最后更新: 2026-05-25 UTC | Reviewer 预审反馈：补 LoRA 中间场景叙事 + Claim 4 措辞升级 | Negative results 升级为 4-block 结构",
    "originalFile": "# ColliForce-VLA Paper Framing\n\n> 维护者: Director | 最后更新: 2026-05-24 12:30 UTC | Reviewer 预审反馈：补 LoRA 中间场景叙事 + Claim 4 措辞升级\n\n## Core Insight\n\n当前 VLA safety 评估存在系统性缺陷：collision avoidance rate (CAR) 被 action collapse 严重污染，导致 \"安全\" 指标虚高。我们通过大规模实证分析（39 个实验, 5000+ episodes）揭示三个相互关联的问题，并提出 displacement-filtered CAR 作为修正指标。\n\n## Working Title\n\n\"The Safety Illusion: How Action Collapse Contaminates Collision Avoidance Metrics in Vision-Language-Action Models\"\n\n> 注：Title scope 已按 Reviewer Report #26 建议收窄——不再 claim 覆盖 \"all SDF methods\"，聚焦 metric contamination 这一更可防御的贡献\n\n## Core Claims\n\n### Claim 1: Fake Safety (Primary — 证据强度 ★★★★★)\nCAR 指标被 action collapse 严重污染。在 SafeLIBERO benchmark 上，A1 (SDF auxiliary loss) 的 91.5% CAR 中 99.6% 是 fake safe（robot displacement < 1μm）。\"Collision-free\" ≠ \"collision-avoiding\"。\n\n**证据**: 800 episodes A1 per-episode displacement 分析; 200 episodes baseline 对比; Pi0.5 56/56 safe episodes displacement ≈ 0\n\n**贡献**: 提出 displacement-filtered CAR (real_CAR) 作为修正指标\n\n### Claim 2: Task Capability vs Safety Anti-correlation (Secondary — 证据强度 ★★★)\n更强的 base model 完成更多任务但碰撞更多。Pi0.5 (TSR=74.7%) vs Pi0 (TSR≈0%): 能力越强 → 运动越多 → 碰撞越多。\n\n**证据**: Pi0.5 3-seed eval (TSR=74.7±1.5%, CAR=26.8±1.6%) vs Pi0 baseline (TSR≈0%, CAR=82%)\n\n**限制**: 仅 2 个 model families, Pi0 的 \"高 CAR\" 来自 action collapse 而非安全。Reviewer 建议降级为 observation, 不 claim 因果关系。\n\n### Claim 3: EE-only SDF Structural Limitation (Supporting — 证据强度 ★★★★)\nEnd-effector-only SDF 在 action space 的碰撞避免存在结构性缺陷：SDF gradient 推 EE 远离障碍物但导致 arm body 扫过障碍物。\n\n**证据**: 3 组 GT SDF oracle (adaptive alpha, fixed alpha, feature-space) 均劣于 baseline; spatial vs object 碰撞部位分析; obstacle 高度/体积与碰撞率的单调关系\n\n**限制**: \"EE-only 不够\" 是 expected result; 缺乏 full-body SDF 对照\n\n### Claim 4: SDF Auxiliary Loss Effectiveness on Strong VLA (Pending — 取决于实验)\n在能力充分的 VLA (Pi0.5) 上，SDF auxiliary training loss 能否产生真实的碰撞避免行为？\n\n**状态**: 3-seed × 2-lambda 训练中, 预计 5/24 18:00 出结果\n\n**Framing 策略 (Reviewer #37)**：即使最优结果也定位为 **\"analysis paper with positive method contribution\"**，而非纯 method paper。原因：analysis 贡献 scope-proof（适用所有 VLA），method 贡献 scope-limited（1-2 models, 2-4 tasks）。SDF aux loss 作为 secondary proof-of-concept，证明 \"问题可解决\" 以验证 analysis 框架的价值。\n\n**Claim 措辞上限** (按 Reviewer 预审升级，基于 10K +30pp 证据): \"Training-time SDF auxiliary loss yields substantial collision avoidance improvement (+Xpp displacement-filtered CAR, frozen_rate=0%) on Pi0.5, confirming that geometric supervision effectively addresses action-collapse-contaminated safety in capable VLAs — at a moderate task performance cost (TSR: 74.7%→Y%)\"（必须包含 TSR tradeoff；禁区: SOTA / consistently outperforms / general solution）\n\n**如果成功 (CAR ≥ 33%)**: 升级为 method contribution (secondary)\n**如果失败**: 额外 negative evidence, 强化 structural insight\n\n**泛化扩展计划 (Reviewer #37, 提升接受率)**：\n- 必须: spatial_bowl 第 2 task 训练（代码准备中）→ 接受率 40% → 55-65%\n- 应该做: OpenVLA zero-shot eval 验证 fake safety 在第 3 model 上存在（仅 inference）\n- 应该做: 4-point lambda 曲线 (0, 0.005, 0.01, 0.1) 支持 \"sweet spot\" claim\n- Nice-to-have: SafeLIBERO 4 suite 各 1 task\n\n## Anticipated Reviewer Concerns\n\n### R1 (最致命): Generalizability\n\"仅在 SafeLIBERO + Pi0 系列上验证, 凭什么说 fake safety 是普遍问题?\"\n→ **应对**: (1) 2+ tasks (object_pudding + spatial_bowl, 代码准备中); (2) 3+ models 的 analysis (Pi0 + Pi0.5 已有, 加 OpenVLA zero-shot eval); (3) 收窄 claim scope + discussion 中做机制分析\n→ **接受率估算** (Reviewer #37): 1 task ~40% / 2 tasks+2 model ~55-65% / 4 tasks+3 model ~65-75%\n\n### R2: Novelty of EE-only limitation\n\"任何了解机器人运动学的人都知道肘部会碰\"\n→ **应对**: 强调定量分析 (arm-body vs EE 碰撞比例量化 + oracle 排除其他解释) 而非定性观察; 作为 supporting claim 而非 primary\n\n### R3: No positive result\n\"告诉我什么不 work 但没告诉我什么 work\"\n→ **应对**: real_CAR 指标是 positive 工具贡献; Pi0.5+A1 如果成功也是正面结果; diagnostic framework 有方法论价值\n\n### R4: Action collapse is trivial\n\"Undertrained Pi0 的 action collapse 不是 safety 特有的, 是训练不足的自然结果\"\n→ **应对**: 必须在论文中承认这一点; 但指出即使原因 trivial, metric contamination 的后果 non-trivial — 后续工作可能基于被污染的 CAR 得出错误结论\n\n## Figure Plan\n\n| ID | 内容 | 优先级 | 数据来源 |\n|----|------|--------|---------|\n| Fig 1 | Fake vs real safety 概念图 | 重要 | 设计 |\n| Fig 2 | Displacement 分布 (A1 vs baseline vs Pi0.5) | **必须** | 800ep A1 + 200ep baseline + 600ep Pi0.5 |\n| Fig 3 | TSR-CAR scatter + obstacle geometry 2-panel | 重要 | 多模型/多方法数据 + per-task geometry |\n| Fig 4 | Oracle refinement CAR bar chart | **必须** | 3 oracle variants + baselines |\n| Table 1 | 3-seed × 2-lambda 完整结果矩阵 | **必须** | Pi0.5+A1 训练结果 (pending) |\n| Fig 5 | Lambda-CAR 曲线 (4 点: 0, 0.005, 0.01, 0.1) | 重要 | pure LoRA + A1 训练 (pending) |\n\n> Fig 3 合并了原 Fig 3 (TSR-CAR scatter) 和 Fig 4 (geometry vs CAR), 按 Reviewer 建议\n\n## Target Venue\n\n**Primary**: CoRL 2026 Main / ICRA 2027 (用户明确要求主会，不是 workshop)\n**条件**: 需要至少一个正向贡献（Pi0.5+A1 成功 / 新 SDF 集成方式 / full-body SDF PoC）\n\n## Narrative Focus (Reviewer Report #30)\n\n论文核心贡献应聚焦于 **结构性洞察**（EE-only SDF 无法影响 full-body safety），而非 negative results 堆叠。三次方法失败（A1 openpi / A3 runtime / A1 Pi0.5）如果 root cause 相同，论文叙事应集中在这个 structural insight，各实验作为不同角度的验证。\n\n## Negative Results Narrative (4 Blocks)\n\n> Director 批准的 4-block 叙事结构（替代原 7 段独立叙事），每个 block 对应一个独立论点，论文 §4-5 按此顺序展开。\n\n### Block 1: Fake Safety Revelation\n- **Evidence**: eval_a1_lora_object_v11_rerun (800 episodes)\n- **Key finding**: CAR=91.5% with 99.6% fake safe (displacement < 0.1mm)\n- **Narrative**: Standard CAR metric is systematically contaminated by action collapse — \"collision-free\" episodes are actually frozen robots, not collision-avoiding ones. Proposes displacement-filtered CAR (real_CAR) as corrective metric.\n- **Supports**: Claim 1 (Primary)\n\n### Block 2: Stronger Models ≠ Safer (merged)\n- **Evidence**: eval_pi05_safelibero_object_v11 + eval_pi05_safelibero_spatial_v11\n- **Key finding**: Pi0.5 CAR=28% (object), 13% (spatial), real_safe=0.5%\n- **Narrative**: Counter-intuitive — better task capability (TSR=74.7%) leads to more collisions, not fewer. Pi0's high CAR (82%) is fake safety from action collapse; Pi0.5 actually moves and collides. Capability↑ ≠ Safety↑.\n- **Supports**: Claim 2 (Secondary)\n\n### Block 3: Oracle Upper Bound (merged triplet)\n- **Evidence**: oracle_true_gt_adaptive_alpha_v11 + oracle_true_gt_fixed_alpha_v11 + oracle_true_gt_feature_v11\n- **Key finding**: All oracles CAR 73-77% < baseline 82-83%\n- **Narrative**: Unified answer to \"does a better alpha schedule or representation fix runtime refinement?\" — No. Three oracle variants (adaptive alpha, fixed alpha, feature-space SDF) all perform worse than baseline, because gradient correction structurally fails on collapsed policies regardless of alpha/representation choice. Eliminates hyperparameter tuning as escape route.\n- **Supports**: Claim 3 (Supporting)\n- **Presentation**: Single unified table with 3 oracle rows + baseline row\n\n### Block 4: EE-only Boundary Condition\n- **Evidence**: eval_a1_lora_spatial_v11\n- **Key finding**: CAR≈0% in spatial tasks, all 6 safe episodes are frozen (displacement ≈ 0)\n- **Narrative**: EE-only SDF cannot address arm-body collisions — in spatial tasks where collisions come from the arm body sweeping through obstacles, EE-based correction has zero effect. Defines the structural scope boundary of the method.\n- **Supports**: Claim 3 (Supporting, boundary condition)\n\n### 叙事原则\n1. 每个 block 不是\"失败\"，是 **evidence for structural claims** — 用 \"we demonstrate\" / \"we find\" 而非 \"we failed to\"\n2. Block 3 的三个 oracle 合并为一段 + 一个表格，统一回答一个问题，避免重复叙事\n3. Block 间按逻辑递进排列：metric 有问题 (B1) → 强模型也不安全 (B2) → runtime 修正无法解决 (B3) → method scope 边界 (B4)\n\n## Contingency Plans (Post Step-10K Eval)\n\n**场景 1 (最可能)**: λ=0.005 ≈ λ=0.01, 均 ≤ baseline → SDF signal 被 action loss 淹没\n→ Early-stop λ=0.01 runs, 用释放 GPU 跑纯 LoRA baseline + λ=0.1 bracket\n→ 纯 analysis paper, 聚焦 structural insight\n\n**场景 2**: 两个 lambda 均 > baseline, 无差异 → 改善可能来自 LoRA 本身\n→ 必须对比纯 LoRA baseline 才能归因\n→ 无纯 LoRA baseline 的 CAR 改善不可发表\n\n**场景 2a-2d (LoRA 中间场景，Reviewer 预审补充)**:\n\n| LoRA-only CAR | SDF 增量 | 叙事策略 |\n|---------------|----------|----------|\n| ~27% (≈baseline) | +30pp 全归 SDF | \"geometric supervision is effective\" — 最强 method claim |\n| ~35% | +22pp | \"LoRA capacity tuning helps, SDF provides major additional benefit\" — 仍强 |\n| ~45% | +12pp | \"LoRA is primary driver, SDF provides dose-dependent safety margin\" — 需 4-point lambda 曲线支撑 monotonic trend |\n| ~55%+ (≈A1) | ≈0pp | 归纯 LoRA → pure analysis paper, SDF 作为 negative evidence |\n\n关键防御：即使 SDF 增量仅 +10-15pp，只要 4-point lambda 曲线呈 monotonic trend，仍可 claim \"geometric supervision signal provides dose-dependent safety improvement beyond LoRA capacity tuning\"。\n\n**场景 3**: λ=0.01 > λ=0.005 → SDF 有效\n→ 继续到 30K, 升级为 \"analysis paper with positive method contribution\"（非纯 method paper）\n→ 加 λ=0 (pure LoRA) + λ=0.1 构建 4-point lambda 曲线, 支持 \"sweet spot\" claim\n→ 扩展到 spatial_bowl 第 2 task, 强化泛化性\n\n## Dependencies\n\n- [ ] Pi0.5+A1 训练结果 (Claim 4, Table 1) — ETA 5/24 18:00\n- [ ] Step 10K mid-eval — ETA 5/23 ~16:25 UTC\n- [ ] 纯 LoRA baseline (无 SDF/EE loss) — **RUNNING** (westd-45947, 2-seed, ETA ~5/26 01:30)\n- [ ] λ=0.1 bracket (1-seed Pi0.5) — 10K eval 后启动, 4-point lambda 曲线必需\n- [ ] spatial_bowl A1 训练 (2-seed × best-lambda) — **代码准备中（Agent 已派 Worker）**, 必须 5/28 前启动（CoRL DDL 约束）\n- [ ] OpenVLA zero-shot SafeLIBERO eval — 仅 inference, 验证 fake safety 跨模型存在\n- [x] Pi0.5 baseline 3-seed (Claim 2) — CAR=26.8±1.6%\n- [x] A1 fake safety 800ep (Claim 1) — 99.6% fake\n- [x] Oracle 3 variants (Claim 3) — all < baseline\n- [x] Spatial/object collision analysis (Claim 3) — arm-body dominant\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " # ColliForce-VLA Paper Framing",
          " ",
          "-> 维护者: Director | 最后更新: 2026-05-24 12:30 UTC | Reviewer 预审反馈：补 LoRA 中间场景叙事 + Claim 4 措辞升级",
          "+> 维护者: Director | 最后更新: 2026-05-25 UTC | Reviewer 预审反馈：补 LoRA 中间场景叙事 + Claim 4 措辞升级 | Negative results 升级为 4-block 结构",
          " ",
          " ## Core Insight",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 20_

已完成。paper_framing.md 的 negative results 部分从原来的 3-tier (A/B/C) 分层结构替换为 Director 批准的 4-block 叙事结构：

- **Block 1**: Fake Safety — 800ep action collapse 证据
- **Block 2**: Stronger ≠ Safer — Pi0.5 object+spatial 合并
- **Block 3**: Oracle Upper Bound — 三个 oracle 合并为一段+一表
- **Block 4**: EE-only Boundary — spatial CAR≈0% scope 边界

其他 section（Claims、Contingency Plans、Dependencies 等）未改动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e30124b-e11f-468d-b9f7-1ea1e18990b4",
  "uuid": "6cb03cb3-8955-4001-877c-5f5731db1645",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LmvotMAwb1rM5okd8C2tdT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 339,
      "cache_read_input_tokens": 35745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 339
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

_source line 21_

已完成。paper_framing.md 的 negative results 部分从原来的 3-tier (A/B/C) 分层结构替换为 Director 批准的 4-block 叙事结构：

- **Block 1**: Fake Safety — 800ep action collapse 证据
- **Block 2**: Stronger ≠ Safer — Pi0.5 object+spatial 合并
- **Block 3**: Oracle Upper Bound — 三个 oracle 合并为一段+一表
- **Block 4**: EE-only Boundary — spatial CAR≈0% scope 边界

其他 section（Claims、Contingency Plans、Dependencies 等）未改动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 80794,
  "duration_api_ms": 81745,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "1e30124b-e11f-468d-b9f7-1ea1e18990b4",
  "total_cost_usd": 0.30326074999999997,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 24243,
    "cache_read_input_tokens": 158572,
    "output_tokens": 2823,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 24243,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 179,
        "cache_read_input_tokens": 35745,
        "cache_creation_input_tokens": 339,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 339
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1736,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001836,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 2823,
      "cacheReadInputTokens": 158572,
      "cacheCreationInputTokens": 24243,
      "webSearchRequests": 0,
      "costUSD": 0.30142474999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "672e817d-d135-42cb-aae3-22137d3abf65"
}
```

</details>

---
