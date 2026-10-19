# writing discussion draft

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/workers/worker_writing_discussion_draft_20260527T082809.log`
- **Structured JSON:** [`4d9b5ddf054f949c4b6b.json`](../../sessions/4d/4d9b5ddf054f949c4b6b.json)

## Before a recorded user message

48 recorded events

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
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
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
  "uuid": "0f29270b-8eea-453a-9847-8756e197da22",
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
    "resetsAt": 1779883800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "9e743b39-4ee0-401d-bd6c-73661ab5aa36",
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e"
}
```

---

### Assistant

_source line 4_

I'll start by reading the paper framing and any existing discussion content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "72f1546f-4246-4286-be24-32a0e3e89ab0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nv6AKo4js5S2tY9KjMxYvn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12048,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12048
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011KTBBzSaRc147sfGqYY5X5`</summary>

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
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "9cba3caf-39ae-45bd-baab-4b377e92a877",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nv6AKo4js5S2tY9KjMxYvn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12048,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12048
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

_source line 6 · 2026-05-27T08:28:21.858Z_

<details><summary>↩ Tool result · `toolu_011KTBBzSaRc147sfGqYY5X5`</summary>

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
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "a5a6a5d6-ad74-4c91-aa24-763108a04a6f",
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
Let me read the paper framing and any existing discussion content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "7fb98b62-413d-48a1-aba2-4b231b8ac4dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QpYq5fPifoutUDUD7WRWW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 451,
      "cache_read_input_tokens": 23893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 451
      },
      "output_tokens": 60,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GWTpQRJ2RNeRLmki28mGEd`</summary>

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
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "39f84341-8f56-43a4-9d0c-0b299862414c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QpYq5fPifoutUDUD7WRWW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 451,
      "cache_read_input_tokens": 23893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 451
      },
      "output_tokens": 60,
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

_source line 9 · 2026-05-27T08:28:25.444Z_

<details><summary>↩ Tool result · `toolu_01GWTpQRJ2RNeRLmki28mGEd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md\", \"content\": \"# ColliForce-VLA Paper Framing\\n\\n> 维护者: Director | 最后更新: 2026-05-27 01:15 UTC | D035: Scenario B 双 seed 确认，Core Insight 修正 | Post-MVP research phase\\n\\n## Core Insight\\n\\nVLA safety 评估存在系统性缺陷：collision avoidance rate (CAR) 被 action collapse 和几何路径安全严重污染，导致 \\\"安全\\\" 指标虚高。我们通过大规模实证分析（90+ 实验, 6000+ episodes）揭示这一系统性缺陷，提出 EE displacement-filtered CAR 作为修正指标，并证明碰撞避免能力隐式来自 collision-free demonstration data，而非显式几何监督——SDF auxiliary loss 在全测试范围 λ∈[0.005, 0.1] 完全冗余，binding constraint 是 EE-only 的结构性不匹配。\\n\\n## Working Title\\n\\n\\\"Rethinking VLA Safety Evaluation: When 98% of Collision Avoidance is an Illusion\\\"\\n\\n> 聚焦评估方法论贡献（影响面广、scope-proof），SDF 作为验证工具而非主贡献\\n\\n## Target Venue\\n\\n**Primary**: CoRL 2026 Main / ICRA 2027 (用户明确要求主会)\\n**定位**: Diagnostic/evaluation methodology paper with positive method contribution\\n**Fit**: Robotics safety track — \\\"VLA safety metrics are fundamentally broken\\\" 对社区有直接影响\\n\\n## Core Claims (D028 重组: 4→3 claims)\\n\\n### Claim 1: CAR Metric Contaminated by Fake Safety (Primary — 证据强度 ★★★★★)\\n\\nStandard CAR metric is systematically contaminated by two distinct mechanisms: (a) action collapse producing frozen robots falsely counted as \\\"safe\\\", and (b) geometric path safety where capable robots happen to avoid obstacles without any avoidance behavior. \\\"Collision-free\\\" ≠ \\\"collision-avoiding.\\\"\\n\\n**Primary evidence — Action collapse (fake safety)**:\\n- 800 episodes A1 per-episode analysis: CAR=91.5%, but 99.6% of safe episodes show obstacle displacement < 0.1mm (~5nm median) — robot is frozen\\n- TSR=0% 独立确认 action collapse\\n- 术语修正 (D023): fake safety 判定以 TSR=0% + obstacle displacement < 0.1mm 双证据链为主\\n\\n**Supporting evidence — Capability-safety anti-correlation (原 Claim 2)**:\\n- Pi0.5 3-seed eval: TSR=74.7±1.5%, CAR=26.8±1.6% — 更强模型完成更多任务但碰撞更多\\n- Pi0 baseline: TSR≈0%, CAR=82% — \\\"高 CAR\\\" 来自 action collapse\\n- Capability↑ → motion↑ → collision↑; 表面安全要么是 frozen (Pi0) 要么是 path geometry (Pi0.5)\\n- 限制: 仅 2 model families; 降级为 observation, 不 claim 因果\\n\\n**贡献**: 提出 EE displacement-filtered CAR (dfCAR) 作为修正指标\\n\\n**dfCAR 定位 (D024 Dream 反馈)**:\\n- Claim 1 的核心证据是 TSR=0% + obstacle displacement 双证据链，**不依赖** dfCAR\\n- dfCAR 是 **方法论贡献**（community tool），不是 Claim 1 的唯一支撑\\n- 论文需要展示 dfCAR 的实际 filtering 效果：Pi0+A1 (CAR=91.5% → dfCAR≈0%) vs Pi0.5+SDF (dfCAR=raw_CAR, no filtering)\\n- Threshold sensitivity: δ∈[2mm, 200mm] 范围内 dfCAR 完全不变（所有 active episode 最小 EE disp = 239mm）\\n\\n### Claim 2: EE-only Geometric Supervision Structural Limitations (Supporting — 证据强度 ★★★★)\\n\\nEnd-effector-only SDF 在 action space 的碰撞避免存在结构性缺陷：SDF gradient 推 EE 远离障碍物但导致 arm body 扫过障碍物。\\n\\n**证据**: 3 组 GT SDF oracle (adaptive alpha, fixed alpha, feature-space) 均劣于 baseline; spatial vs object 碰撞部位分析; obstacle 高度/体积与碰撞率的单调关系\\n**限制**: \\\"EE-only 不够\\\" 是 expected result; 缺乏 full-body SDF 对照\\n\\n### Claim 3: Avoidance Source Diagnosis — EE-only Geometric Supervision Neither Necessary Nor Sufficient (Diagnostic — 证据强度 ★★★★★, D035 Scenario B confirmed)\\n\\nUnified framing (Reviewer 建议, 统一 Claim 2+3 takeaway): EE-only SDF geometric supervision is neither necessary for collision avoidance—collision-free demonstrations account for the entire 28pp CAR gain, with identical per-task avoidance patterns across all SDF conditions—nor structurally sufficient, as ground-truth oracle refinement reduces CAR below unrefined baselines. This dual failure reveals that avoidance capability is implicitly learned from demonstration data distribution, not from explicit geometric supervision.\\n\\n**Overclaiming 防线（必须在论文中体现）**: (1) Scope: SafeLIBERO + Pi0/Pi0.5; (2) \\\"EE-only SDF\\\" 不否定 full-body geometric supervision; (3) \\\"all observed/measured gains\\\" 不声称 demos 能解决碰撞问题; (4) 不否定其他 geometric loss 形式（CBF、reward shaping）。\\n\\n**已确认 (D025/D032/D033/D035 core)**：at λ∈{0.005, 0.01, 0.1}, SDF does not improve CAR beyond LoRA-only baseline。λ=0.1（20× weight increase）双 seed 20K mean CAR=55.5%（z=0.47 vs null），明确在噪声内。LoRA fine-tuning 本身产生 +26pp CAR（54.5% vs Pi0.5 baseline 28.5%）。Per-task CAR ordering 跨所有条件完全一致（chocolate_pudding > milk > orange_juice > bbq_sauce），表明避障模式反映 demonstration distribution 特征而非 geometric supervision。\\n\\n**证据（rotation-fixed reeval 数据）**:\\n- LoRA-only (2 seeds): CAR=54.5%±2.8 (s0=56.5%, s1=52.5%), frozen=0%\\n- LoRA+SDF λ=0.005 (3 seeds): CAR=54.5%±2.3 (s0=57, s1=54, s2=52.5)\\n- LoRA+SDF λ=0.01 (3 seeds): CAR=56.33%±1.61 (s0=57, s1=57.5, s2=54.5) — p≈0.12 不显著，per-task 无系统提升，Task 3 驱动方差 s0=34%→s2=14% (D033)\\n- Per-task CAR pattern 完全一致（T3 BBQ 方差最大: l01=23.3% vs l005=20% vs LoRA=26%，种子噪声）\\n\\n**TSR collapse 机制分析 (M041)**:\\n- 复合机制：catastrophic forgetting of task semantics + retained collision avoidance\\n- SDF loss 不是 TSR 崩溃原因（LoRA baseline 崩溃幅度完全一致 -68.4% vs -68.7%）\\n- Robot 保留运动能力（0% frozen, EE ~0.5m）但丧失 goal-directed grasping/placing\\n- Safe failure rate 从 0.5% → ~50%（100×），obstacle displacement 减半\\n\\n**✅ CONFIRMED: Scenario B (D035)** — λ=0.1 20K 双 seed mean CAR=55.5% ≤ 57% 阈值，全域 SDF 冗余。\\n\\n**判定依据 (D033 阈值 + D035 确认)**：零分布 = LoRA(2) + l005(3) = 5 个无效 SDF 测量值 mean=54.5%, std=2.17%。λ=0.1 双 seed z=0.47，明确在噪声内。硬约束全部通过（TSR=51-54% ≥ 35%，frozen=0%）。\\n\\n| λ=0.1 结果 | 场景 | 状态 |\\n|-----------|------|------|\\n| **2-seed 20K mean=55.5% (≤57%)** | **B（完全 negative）** | **✅ 已确认** |\\n\\n**待最终确认（不影响叙事方向）**：\\n- **λ=0.1 30K × 2 seeds** (s0/s1 ~17:00 UTC 5/27) → 最终数字确认\\n- **λ=0.1 30K s2** (~08:40 UTC 5/28) → 第三 seed 补充\\n- LoRA seed2 (plan_013) → 3v3 seeds 统计\\n- Phase 2 λ=0 → SDF 是否有持久效应（Scenario B 下测 \\\"dose-dependent safety persist after removal\\\"）\\n\\n### Phase 2 解读 (contingent on λ=0.1)\\n\\n- 如果场景 A/C: Phase 2 测试 \\\"SDF 训练是否造成持久行为变化\\\"\\n- 如果场景 B: Phase 2 测试 \\\"dose-dependent safety 是否 persist after removal\\\"\\n- Phase 2 CAR ≈ LoRA-only → SDF 无持久效应\\n- Phase 2 CAR < LoRA-only → SDF 造成持久损伤\\n- Phase 2 CAR > LoRA-only → SDF 有持久编码（需更多 seeds 确认）\\n\\n## Anticipated Reviewer Concerns\\n\\n### R1 (最致命): Generalizability\\n\\\"仅在 SafeLIBERO + Pi0 系列上验证, 凭什么说 fake safety 是普遍问题?\\\"\\n→ **应对**: (1) 2+ tasks (object_pudding + spatial_bowl); (2) 3+ models (Pi0 + Pi0.5 + OpenVLA); (3) 收窄 claim scope + mechanistic argument (any model with low task capability will exhibit fake safety)\\n→ **接受率估算**: 1 task/2 model ~40% / 2 tasks+3 models ~55-65% / 3+ tasks ~65-75%\\n\\n### R2: Novelty of EE-only limitation\\n→ **应对**: 定量分析 (arm-body vs EE 碰撞比例 + oracle 排除其他解释); supporting claim 而非 primary\\n\\n### R3: No solution\\n\\\"诊断了问题但没解决\\\"\\n→ **应对**: (1) dfCAR metric 是 positive 工具贡献; (2) 揭示 avoidance 来源（implicit demo signal, not geometric supervision）本身是 actionable insight; (3) diagnostic paper 有方法论价值——知道问题在哪比错误地以为解决了更重要\\n\\n### R4: Action collapse is trivial\\n→ **应对**: 原因可能 trivial，但 metric contamination 后果 non-trivial; 后续工作基于被污染 CAR 得出错误结论\\n\\n### R5 (更新 D025): SDF redundancy — why bother testing it?\\n→ **应对**: (1) SDF geometric supervision 在 motion planning 领域广泛使用，先验合理; (2) negative result 排除合理路径; (3) 关键 insight 是 \\\"avoidance 来自 demo imitation, not geometry\\\" — 对未来 safety method 设计有指导意义\\n\\n### R6 (D025): Fine-tuning collapse — catastrophic forgetting?\\n→ **应对**: (1) M041 分析确认是复合机制 (forgetting of task semantics + retained avoidance); (2) LoRA fine-tuning 同时提升 CAR 和降低 TSR = conservative behavior, not safe behavior; (3) SDF 不是原因（LoRA baseline 同等崩溃）\\n\\n## Narrative Structure (D028: 3 Blocks + 1 Sub-block)\\n\\n### Block 1: Fake Safety Revelation + Capability Observation (Claim 1)\\n- **Evidence**: A1 800ep (frozen), Pi0.5 3-seed (geometric path safety), Pi0 baseline (action collapse)\\n- **Key finding**: CAR=91.5% is fake (99.6% frozen); Pi0.5 CAR=27% is geometric; neither is avoidance\\n- **Contribution**: dfCAR metric + threshold sensitivity analysis\\n- **Sub-block**: Capability↑ → motion↑ → collision↑ as supporting observation\\n\\n### Block 2: EE-only Geometric Supervision Boundary (Claim 2)\\n- **Evidence**: 3 oracle variants all < baseline; arm-body collision analysis\\n- **Narrative**: Runtime gradient correction structurally fails — alpha schedule and representation don't help; EE-only SDF = structural scope limit\\n- **Presentation**: Single unified table + collision part analysis\\n\\n### Block 3: Avoidance Source Diagnosis — Neither Necessary Nor Sufficient (Claim 3, unified with Claim 2)\\n- **Evidence**: LoRA-only 2-3 seeds + SDF 3 seeds × 3 lambdas, per-task comparison, oracle experiments\\n- **Key finding**: \\\"Neither necessary nor sufficient\\\" — (necessity) LoRA-only CAR=54.5% ≈ SDF across λ∈[0.005, 0.1], per-task ordering invariant; (sufficiency) oracle refinement CAR < baseline\\n- **Narrative**: EE-only SDF geometric supervision fails on two independent dimensions: it is unnecessary (demo distribution accounts for all avoidance gains) and structurally insufficient (EE-only monitoring redistributes collisions to unmonitored arm links). Per-task avoidance fingerprint (chocolate_pudding highest, bbq_sauce lowest) preserved across all 10 conditions confirms demonstration distribution as sole source.\\n- **TSR collapse analysis**: composite mechanism (task forgetting + avoidance retention)\\n- **Sub-narrative**: flat λ curve (Scenario B confirmed) + stepwise training dynamics (16K-30K) + Phase 2 persistence\\n\\n### 叙事原则\\n1. 每个 block 是 **evidence for structural claims**\\n2. Block 间逻辑递进：metric 有缺陷 (B1) → geometric supervision 有结构缺陷 (B2) → avoidance 来源是 demo data 而非 geometry (B3)\\n3. B3 是 positive diagnostic insight，展示\\\"避障可实现且来源是隐式学习\\\"\\n\\n## Figure Plan\\n\\n| ID | 内容 | Claim | 优先级 | 数据来源 | 状态 |\\n|----|------|-------|--------|---------|------|\\n| Fig 1 | Fake vs real safety 概念图 (displacement 对比) | 1 | 重要 | 设计 | 待做 |\\n| Fig 2 | EE Displacement 分布 (A1-frozen vs Pi0.5+A1-moving vs baseline) | 1 | **必须** | 修复后 eval JSON | 数据就绪 |\\n| Fig 3 | TSR-CAR scatter (多模型 + capability observation) | 1 | 重要 | 全部 eval 数据 | 数据就绪 |\\n| Fig 4 | Oracle refinement CAR bar chart + arm-body collision | 2 | **必须** | 3 oracle + baselines | 数据就绪 |\\n| Table 1 | 3-seed × 2-lambda × best/30K 完整结果矩阵 + EE disp | 3 | **必须** | Pi0.5+A1 修正数据 | 数据就绪 |\\n| Fig 5 | Lambda-CAR/TSR 曲线 (含 LoRA baseline 作 λ=0 点) | 3 | **必须** | LoRA baseline + SDF 数据 | 待 λ=0.1 |\\n| Table 2 | Phase 2 λ=0 ablation 结果 | 3 | 重要 | Phase 2 训练 | RUNNING |\\n\\n## Dependencies (Research Phase)\\n\\n- [x] A1 fake safety 800ep (Claim 1) — 99.6% fake (obstacle disp)\\n- [x] Pi0.5 baseline 3-seed (Claim 1 supporting) — CAR=26.8±1.6%, TSR=74.7±1.5%\\n- [x] Pi0.5+A1 3-seed × 2-lambda 训练 + eval (Claim 3) — confirmed real avoidance (D023)\\n- [x] EE displacement 修正 eval (Claim 3) — 3 seeds corrected, all consistent\\n- [x] Oracle 3 variants (Claim 2) — all < baseline\\n- [x] Spatial/object collision analysis (Claim 2) — arm-body dominant\\n- [x] **LoRA baseline** (Claim 3 attribution) — DONE: CAR=55%, SDF delta=0pp (D025)\\n- [x] **TSR collapse mechanism analysis** (Claim 3) — M041: composite (forgetting + avoidance retention)\\n- [ ] **LoRA baseline seed2** (plan_013, Claim 3) — RUNNING on westd-45947\\n- [ ] **Phase 2 λ=0** (Claim 3) — RUNNING on cuda:3\\n- [ ] **spatial_bowl A1 训练** (Claim 3) — RUNNING on cuda:0, ~20h\\n- [x] **Lambda=0.1 × 2 seeds 20K** (Claim 3) — D035 Scenario B confirmed: mean CAR=55.5% ≈ null\\n- [ ] **Lambda=0.1 × 3 seeds 30K** (Claim 3) — RUNNING: s0/s1 ~17:00 UTC 5/27, s2 ~08:40 UTC 5/28 (最终数字确认)\\n- [ ] **Pi0.5 baseline re-eval** (Claim 1) — RUNNING westd-45947, 补 EE displacement baseline\\n- [ ] **OpenVLA zero-shot eval** (Claim 1) — BLOCKED (模型下载损坏)\\n\", \"total_chars\": 11046, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "52cb257d-6368-426b-a765-863b11ba325c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md\\\", \\\"content\\\": \\\"# ColliForce-VLA Paper Framing\\\\n\\\\n> 维护者: Director | 最后更新: 2026-05-27 01:15 UTC | D035: Scenario B 双 seed 确认，Core Insight 修正 | Post-MVP research phase\\\\n\\\\n## Core Insight\\\\n\\\\nVLA safety 评估存在系统性缺陷：collision avoidance rate (CAR) 被 action collapse 和几何路径安全严重污染，导致 \\\\\\\"安全\\\\\\\" 指标虚高。我们通过大规模实证分析（90+ 实验, 6000+ episodes）揭示这一系统性缺陷，提出 EE displacement-filtered CAR 作为修正指标，并证明碰撞避免能力隐式来自 collision-free demonstration data，而非显式几何监督——SDF auxiliary loss 在全测试范围 λ∈[0.005, 0.1] 完全冗余，binding constraint 是 EE-only 的结构性不匹配。\\\\n\\\\n## Working Title\\\\n\\\\n\\\\\\\"Rethinking VLA Safety Evaluation: When 98% of Collision Avoidance is an Illusion\\\\\\\"\\\\n\\\\n> 聚焦评估方法论贡献（影响面广、scope-proof），SDF 作为验证工具而非主贡献\\\\n\\\\n## Target Venue\\\\n\\\\n**Primary**: CoRL 2026 Main / ICRA 2027 (用户明确要求主会)\\\\n**定位**: Diagnostic/evaluation methodology paper with positive method contribution\\\\n**Fit**: Robotics safety track — \\\\\\\"VLA safety metrics are fundamentally broken\\\\\\\" 对社区有直接影响\\\\n\\\\n## Core Claims (D028 重组: 4→3 claims)\\\\n\\\\n### Claim 1: CAR Metric Contaminated by Fake Safety (Primary — 证据强度 ★★★★★)\\\\n\\\\nStandard CAR metric is systematically contaminated by two distinct mechanisms: (a) action collapse producing frozen robots falsely counted as \\\\\\\"safe\\\\\\\", and (b) geometric path safety where capable robots happen to avoid obstacles without any avoidance behavior. \\\\\\\"Collision-free\\\\\\\" ≠ \\\\\\\"collision-avoiding.\\\\\\\"\\\\n\\\\n**Primary evidence — Action collapse (fake safety)**:\\\\n- 800 episodes A1 per-episode analysis: CAR=91.5%, but 99.6% of safe episodes show obstacle displacement < 0.1mm (~5nm median) — robot is frozen\\\\n- TSR=0% 独立确认 action collapse\\\\n- 术语修正 (D023): fake safety 判定以 TSR=0% + obstacle displacement < 0.1mm 双证据链为主\\\\n\\\\n**Supporting evidence — Capability-safety anti-correlation (原 Claim 2)**:\\\\n- Pi0.5 3-seed eval: TSR=74.7±1.5%, CAR=26.8±1.6% — 更强模型完成更多任务但碰撞更多\\\\n- Pi0 baseline: TSR≈0%, CAR=82% — \\\\\\\"高 CAR\\\\\\\" 来自 action collapse\\\\n- Capability↑ → motion↑ → collision↑; 表面安全要么是 frozen (Pi0) 要么是 path geometry (Pi0.5)\\\\n- 限制: 仅 2 model families; 降级为 observation, 不 claim 因果\\\\n\\\\n**贡献**: 提出 EE displacement-filtered CAR (dfCAR) 作为修正指标\\\\n\\\\n**dfCAR 定位 (D024 Dream 反馈)**:\\\\n- Claim 1 的核心证据是 TSR=0% + obstacle displacement 双证据链，**不依赖** dfCAR\\\\n- dfCAR 是 **方法论贡献**（community tool），不是 Claim 1 的唯一支撑\\\\n- 论文需要展示 dfCAR 的实际 filtering 效果：Pi0+A1 (CAR=91.5% → dfCAR≈0%) vs Pi0.5+SDF (dfCAR=raw_CAR, no filtering)\\\\n- Threshold sensitivity: δ∈[2mm, 200mm] 范围内 dfCAR 完全不变（所有 active episode 最小 EE disp = 239mm）\\\\n\\\\n### Claim 2: EE-only Geometric Supervision Structural Limitations (Supporting — 证据强度 ★★★★)\\\\n\\\\nEnd-effector-only SDF 在 action space 的碰撞避免存在结构性缺陷：SDF gradient 推 EE 远离障碍物但导致 arm body 扫过障碍物。\\\\n\\\\n**证据**: 3 组 GT SDF oracle (adaptive alpha, fixed alpha, feature-space) 均劣于 baseline; spatial vs object 碰撞部位分析; obstacle 高度/体积与碰撞率的单调关系\\\\n**限制**: \\\\\\\"EE-only 不够\\\\\\\" 是 expected result; 缺乏 full-body SDF 对照\\\\n\\\\n### Claim 3: Avoidance Source Diagnosis — EE-only Geometric Supervision Neither Necessary Nor Sufficient (Diagnostic — 证据强度 ★★★★★, D035 Scenario B confirmed)\\\\n\\\\nUnified framing (Reviewer 建议, 统一 Claim 2+3 takeaway): EE-only SDF geometric supervision is neither necessary for collision avoidance—collision-free demonstrations account for the entire 28pp CAR gain, with identical per-task avoidance patterns across all SDF conditions—nor structurally sufficient, as ground-truth oracle refinement reduces CAR below unrefined baselines. This dual failure reveals that avoidance capability is implicitly learned from demonstration data distribution, not from explicit geometric supervision.\\\\n\\\\n**Overclaiming 防线（必须在论文中体现）**: (1) Scope: SafeLIBERO + Pi0/Pi0.5; (2) \\\\\\\"EE-only SDF\\\\\\\" 不否定 full-body geometric supervision; (3) \\\\\\\"all observed/measured gains\\\\\\\" 不声称 demos 能解决碰撞问题; (4) 不否定其他 geometric loss 形式（CBF、reward shaping）。\\\\n\\\\n**已确认 (D025/D032/D033/D035 core)**：at λ∈{0.005, 0.01, 0.1}, SDF does not improve CAR beyond LoRA-only baseline。λ=0.1（20× weight increase）双 seed 20K mean CAR=55.5%（z=0.47 vs null），明确在噪声内。LoRA fine-tuning 本身产生 +26pp CAR（54.5% vs Pi0.5 baseline 28.5%）。Per-task CAR ordering 跨所有条件完全一致（chocolate_pudding > milk > orange_juice > bbq_sauce），表明避障模式反映 demonstration distribution 特征而非 geometric supervision。\\\\n\\\\n**证据（rotation-fixed reeval 数据）**:\\\\n- LoRA-only (2 seeds): CAR=54.5%±2.8 (s0=56.5%, s1=52.5%), frozen=0%\\\\n- LoRA+SDF λ=0.005 (3 seeds): CAR=54.5%±2.3 (s0=57, s1=54, s2=52.5)\\\\n- LoRA+SDF λ=0.01 (3 seeds): CAR=56.33%±1.61 (s0=57, s1=57.5, s2=54.5) — p≈0.12 不显著，per-task 无系统提升，Task 3 驱动方差 s0=34%→s2=14% (D033)\\\\n- Per-task CAR pattern 完全一致（T3 BBQ 方差最大: l01=23.3% vs l005=20% vs LoRA=26%，种子噪声）\\\\n\\\\n**TSR collapse 机制分析 (M041)**:\\\\n- 复合机制：catastrophic forgetting of task semantics + retained collision avoidance\\\\n- SDF loss 不是 TSR 崩溃原因（LoRA baseline 崩溃幅度完全一致 -68.4% vs -68.7%）\\\\n- Robot 保留运动能力（0% frozen, EE ~0.5m）但丧失 goal-directed grasping/placing\\\\n- Safe failure rate 从 0.5% → ~50%（100×），obstacle displacement 减半\\\\n\\\\n**✅ CONFIRMED: Scenario B (D035)** — λ=0.1 20K 双 seed mean CAR=55.5% ≤ 57% 阈值，全域 SDF 冗余。\\\\n\\\\n**判定依据 (D033 阈值 + D035 确认)**：零分布 = LoRA(2) + l005(3) = 5 个无效 SDF 测量值 mean=54.5%, std=2.17%。λ=0.1 双 seed z=0.47，明确在噪声内。硬约束全部通过（TSR=51-54% ≥ 35%，frozen=0%）。\\\\n\\\\n| λ=0.1 结果 | 场景 | 状态 |\\\\n|-----------|------|------|\\\\n| **2-seed 20K mean=55.5% (≤57%)** | **B（完全 negative）** | **✅ 已确认** |\\\\n\\\\n**待最终确认（不影响叙事方向）**：\\\\n- **λ=0.1 30K × 2 seeds** (s0/s1 ~17:00 UTC 5/27) → 最终数字确认\\\\n- **λ=0.1 30K s2** (~08:40 UTC 5/28) → 第三 seed 补充\\\\n- LoRA seed2 (plan_013) → 3v3 seeds 统计\\\\n- Phase 2 λ=0 → SDF 是否有持久效应（Scenario B 下测 \\\\\\\"dose-dependent safety persist after removal\\\\\\\"）\\\\n\\\\n### Phase 2 解读 (contingent on λ=0.1)\\\\n\\\\n- 如果场景 A/C: Phase 2 测试 \\\\\\\"SDF 训练是否造成持久行为变化\\\\\\\"\\\\n- 如果场景 B: Phase 2 测试 \\\\\\\"dose-dependent safety 是否 persist after removal\\\\\\\"\\\\n- Phase 2 CAR ≈ LoRA-only → SDF 无持久效应\\\\n- Phase 2 CAR < LoRA-only → SDF 造成持久损伤\\\\n- Phase 2 CAR > LoRA-only → SDF 有持久编码（需更多 seeds 确认）\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n### R1 (最致命): Generalizability\\\\n\\\\\\\"仅在 SafeLIBERO + Pi0 系列上验证, 凭什么说 fake safety 是普遍问题?\\\\\\\"\\\\n→ **应对**: (1) 2+ tasks (object_pudding + spatial_bowl); (2) 3+ models (Pi0 + Pi0.5 + OpenVLA); (3) 收窄 claim scope + mechanistic argument (any model with low task capability will exhibit fake safety)\\\\n→ **接受率估算**: 1 task/2 model ~40% / 2 tasks+3 models ~55-65% / 3+ tasks ~65-75%\\\\n\\\\n### R2: Novelty of EE-only limitation\\\\n→ **应对**: 定量分析 (arm-body vs EE 碰撞比例 + oracle 排除其他解释); supporting claim 而非 primary\\\\n\\\\n### R3: No solution\\\\n\\\\\\\"诊断了问题但没解决\\\\\\\"\\\\n→ **应对**: (1) dfCAR metric 是 positive 工具贡献; (2) 揭示 avoidance 来源（implicit demo signal, not geometric supervision）本身是 actionable insight; (3) diagnostic paper 有方法论价值——知道问题在哪比错误地以为解决了更重要\\\\n\\\\n### R4: Action collapse is trivial\\\\n→ **应对**: 原因可能 trivial，但 metric contamination 后果 non-trivial; 后续工作基于被污染 CAR 得出错误结论\\\\n\\\\n### R5 (更新 D025): SDF redundancy — why bother testing it?\\\\n→ **应对**: (1) SDF geometric supervision 在 motion planning 领域广泛使用，先验合理; (2) negative result 排除合理路径; (3) 关键 insight 是 \\\\\\\"avoidance 来自 demo imitation, not geometry\\\\\\\" — 对未来 safety method 设计有指导意义\\\\n\\\\n### R6 (D025): Fine-tuning collapse — catastrophic forgetting?\\\\n→ **应对**: (1) M041 分析确认是复合机制 (forgetting of task semantics + retained avoidance); (2) LoRA fine-tuning 同时提升 CAR 和降低 TSR = conservative behavior, not safe behavior; (3) SDF 不是原因（LoRA baseline 同等崩溃）\\\\n\\\\n## Narrative Structure (D028: 3 Blocks + 1 Sub-block)\\\\n\\\\n### Block 1: Fake Safety Revelation + Capability Observation (Claim 1)\\\\n- **Evidence**: A1 800ep (frozen), Pi0.5 3-seed (geometric path safety), Pi0 baseline (action collapse)\\\\n- **Key finding**: CAR=91.5% is fake (99.6% frozen); Pi0.5 CAR=27% is geometric; neither is avoidance\\\\n- **Contribution**: dfCAR metric + threshold sensitivity analysis\\\\n- **Sub-block**: Capability↑ → motion↑ → collision↑ as supporting observation\\\\n\\\\n### Block 2: EE-only Geometric Supervision Boundary (Claim 2)\\\\n- **Evidence**: 3 oracle variants all < baseline; arm-body collision analysis\\\\n- **Narrative**: Runtime gradient correction structurally fails — alpha schedule and representation don't help; EE-only SDF = structural scope limit\\\\n- **Presentation**: Single unified table + collision part analysis\\\\n\\\\n### Block 3: Avoidance Source Diagnosis — Neither Necessary Nor Sufficient (Claim 3, unified with Claim 2)\\\\n- **Evidence**: LoRA-only 2-3 seeds + SDF 3 seeds × 3 lambdas, per-task comparison, oracle experiments\\\\n- **Key finding**: \\\\\\\"Neither necessary nor sufficient\\\\\\\" — (necessity) LoRA-only CAR=54.5% ≈ SDF across λ∈[0.005, 0.1], per-task ordering invariant; (sufficiency) oracle refinement CAR < baseline\\\\n- **Narrative**: EE-only SDF geometric supervision fails on two independent dimensions: it is unnecessary (demo distribution accounts for all avoidance gains) and structurally insufficient (EE-only monitoring redistributes collisions to unmonitored arm links). Per-task avoidance fingerprint (chocolate_pudding highest, bbq_sauce lowest) preserved across all 10 conditions confirms demonstration distribution as sole source.\\\\n- **TSR collapse analysis**: composite mechanism (task forgetting + avoidance retention)\\\\n- **Sub-narrative**: flat λ curve (Scenario B confirmed) + stepwise training dynamics (16K-30K) + Phase 2 persistence\\\\n\\\\n### 叙事原则\\\\n1. 每个 block 是 **evidence for structural claims**\\\\n2. Block 间逻辑递进：metric 有缺陷 (B1) → geometric supervision 有结构缺陷 (B2) → avoidance 来源是 demo data 而非 geometry (B3)\\\\n3. B3 是 positive diagnostic insight，展示\\\\\\\"避障可实现且来源是隐式学习\\\\\\\"\\\\n\\\\n## Figure Plan\\\\n\\\\n| ID | 内容 | Claim | 优先级 | 数据来源 | 状态 |\\\\n|----|------|-------|--------|---------|------|\\\\n| Fig 1 | Fake vs real safety 概念图 (displacement 对比) | 1 | 重要 | 设计 | 待做 |\\\\n| Fig 2 | EE Displacement 分布 (A1-frozen vs Pi0.5+A1-moving vs baseline) | 1 | **必须** | 修复后 eval JSON | 数据就绪 |\\\\n| Fig 3 | TSR-CAR scatter (多模型 + capability observation) | 1 | 重要 | 全部 eval 数据 | 数据就绪 |\\\\n| Fig 4 | Oracle refinement CAR bar chart + arm-body collision | 2 | **必须** | 3 oracle + baselines | 数据就绪 |\\\\n| Table 1 | 3-seed × 2-lambda × best/30K 完整结果矩阵 + EE disp | 3 | **必须** | Pi0.5+A1 修正数据 | 数据就绪 |\\\\n| Fig 5 | Lambda-CAR/TSR 曲线 (含 LoRA baseline 作 λ=0 点) | 3 | **必须** | LoRA baseline + SDF 数据 | 待 λ=0.1 |\\\\n| Table 2 | Phase 2 λ=0 ablation 结果 | 3 | 重要 | Phase 2 训练 | RUNNING |\\\\n\\\\n## Dependencies (Research Phase)\\\\n\\\\n- [x] A1 fake safety 800ep (Claim 1) — 99.6% fake (obstacle disp)\\\\n- [x] Pi0.5 baseline 3-seed (Claim 1 supporting) — CAR=26.8±1.6%, TSR=74.7±1.5%\\\\n- [x] Pi0.5+A1 3-seed × 2-lambda 训练 + eval (Claim 3) — confirmed real avoidance (D023)\\\\n- [x] EE displacement 修正 eval (Claim 3) — 3 seeds corrected, all consistent\\\\n- [x] Oracle 3 variants (Claim 2) — all < baseline\\\\n- [x] Spatial/object collision analysis (Claim 2) — arm-body dominant\\\\n- [x] **LoRA baseline** (Claim 3 attribution) — DONE: CAR=55%, SDF delta=0pp (D025)\\\\n- [x] **TSR collapse mechanism analysis** (Claim 3) — M041: composite (forgetting + avoidance retention)\\\\n- [ ] **LoRA baseline seed2** (plan_013, Claim 3) — RUNNING on westd-45947\\\\n- [ ] **Phase 2 λ=0** (Claim 3) — RUNNING on cuda:3\\\\n- [ ] **spatial_bowl A1 训练** (Claim 3) — RUNNING on cuda:0, ~20h\\\\n- [x] **Lambda=0.1 × 2 seeds 20K** (Claim 3) — D035 Scenario B confirmed: mean CAR=55.5% ≈ null\\\\n- [ ] **Lambda=0.1 × 3 seeds 30K** (Claim 3) — RUNNING: s0/s1 ~17:00 UTC 5/27, s2 ~08:40 UTC 5/28 (最终数字确认)\\\\n- [ ] **Pi0.5 baseline re-eval** (Claim 1) — RUNNING westd-45947, 补 EE displacement baseline\\\\n- [ ] **OpenVLA zero-shot eval** (Claim 1) — BLOCKED (模型下载损坏)\\\\n\\\", \\\"total_chars\\\": 11046, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md\", \"content\": \"# ColliForce-VLA Paper Framing\\n\\n> 维护者: Director | 最后更新: 2026-05-27 01:15 UTC | D035: Scenario B 双 seed 确认，Core Insight 修正 | Post-MVP research phase\\n\\n## Core Insight\\n\\nVLA safety 评估存在系统性缺陷：collision avoidance rate (CAR) 被 action collapse 和几何路径安全严重污染，导致 \\\"安全\\\" 指标虚高。我们通过大规模实证分析（90+ 实验, 6000+ episodes）揭示这一系统性缺陷，提出 EE displacement-filtered CAR 作为修正指标，并证明碰撞避免能力隐式来自 collision-free demonstration data，而非显式几何监督——SDF auxiliary loss 在全测试范围 λ∈[0.005, 0.1] 完全冗余，binding constraint 是 EE-only 的结构性不匹配。\\n\\n## Working Title\\n\\n\\\"Rethinking VLA Safety Evaluation: When 98% of Collision Avoidance is an Illusion\\\"\\n\\n> 聚焦评估方法论贡献（影响面广、scope-proof），SDF 作为验证工具而非主贡献\\n\\n## Target Venue\\n\\n**Primary**: CoRL 2026 Main / ICRA 2027 (用户明确要求主会)\\n**定位**: Diagnostic/evaluation methodology paper with positive method contribution\\n**Fit**: Robotics safety track — \\\"VLA safety metrics are fundamentally broken\\\" 对社区有直接影响\\n\\n## Core Claims (D028 重组: 4→3 claims)\\n\\n### Claim 1: CAR Metric Contaminated by Fake Safety (Primary — 证据强度 ★★★★★)\\n\\nStandard CAR metric is systematically contaminated by two distinct mechanisms: (a) action collapse producing frozen robots falsely counted as \\\"safe\\\", and (b) geometric path safety where capable robots happen to avoid obstacles without any avoidance behavior. \\\"Collision-free\\\" ≠ \\\"collision-avoiding.\\\"\\n\\n**Primary evidence — Action collapse (fake safety)**:\\n- 800 episodes A1 per-episode analysis: CAR=91.5%, but 99.6% of safe episodes show obstacle displacement < 0.1mm (~5nm median) — robot is frozen\\n- TSR=0% 独立确认 action collapse\\n- 术语修正 (D023): fake safety 判定以 TSR=0% + obstacle displacement < 0.1mm 双证据链为主\\n\\n**Supporting evidence — Capability-safety anti-correlation (原 Claim 2)**:\\n- Pi0.5 3-seed eval: TSR=74.7±1.5%, CAR=26.8±1.6% — 更强模型完成更多任务但碰撞更多\\n- Pi0 baseline: TSR≈0%, CAR=82% — \\\"高 CAR\\\" 来自 action collapse\\n- Capability↑ → motion↑ → collision↑; 表面安全要么是 frozen (Pi0) 要么是 path geometry (Pi0.5)\\n- 限制: 仅 2 model families; 降级为 observation, 不 claim 因果\\n\\n**贡献**: 提出 EE displacement-filtered CAR (dfCAR) 作为修正指标\\n\\n**dfCAR 定位 (D024 Dream 反馈)**:\\n- Claim 1 的核心证据是 TSR=0% + obstacle displacement 双证据链，**不依赖** dfCAR\\n- dfCAR 是 **方法论贡献**（community tool），不是 Claim 1 的唯一支撑\\n- 论文需要展示 dfCAR 的实际 filtering 效果：Pi0+A1 (CAR=91.5% → dfCAR≈0%) vs Pi0.5+SDF (dfCAR=raw_CAR, no filtering)\\n- Threshold sensitivity: δ∈[2mm, 200mm] 范围内 dfCAR 完全不变（所有 active episode 最小 EE disp = 239mm）\\n\\n### Claim 2: EE-only Geometric Supervision Structural Limitations (Supporting — 证据强度 ★★★★)\\n\\nEnd-effector-only SDF 在 action space 的碰撞避免存在结构性缺陷：SDF gradient 推 EE 远离障碍物但导致 arm body 扫过障碍物。\\n\\n**证据**: 3 组 GT SDF oracle (adaptive alpha, fixed alpha, feature-space) 均劣于 baseline; spatial vs object 碰撞部位分析; obstacle 高度/体积与碰撞率的单调关系\\n**限制**: \\\"EE-only 不够\\\" 是 expected result; 缺乏 full-body SDF 对照\\n\\n### Claim 3: Avoidance Source Diagnosis — EE-only Geometric Supervision Neither Necessary Nor Sufficient (Diagnostic — 证据强度 ★★★★★, D035 Scenario B confirmed)\\n\\nUnified framing (Reviewer 建议, 统一 Claim 2+3 takeaway): EE-only SDF geometric supervision is neither necessary for collision avoidance—collision-free demonstrations account for the entire 28pp CAR gain, with identical per-task avoidance patterns across all SDF conditions—nor structurally sufficient, as ground-truth oracle refinement reduces CAR below unrefined baselines. This dual failure reveals that avoidance capability is implicitly learned from demonstration data distribution, not from explicit geometric supervision.\\n\\n**Overclaiming 防线（必须在论文中体现）**: (1) Scope: SafeLIBERO + Pi0/Pi0.5; (2) \\\"EE-only SDF\\\" 不否定 full-body geometric supervision; (3) \\\"all observed/measured gains\\\" 不声称 demos 能解决碰撞问题; (4) 不否定其他 geometric loss 形式（CBF、reward shaping）。\\n\\n**已确认 (D025/D032/D033/D035 core)**：at λ∈{0.005, 0.01, 0.1}, SDF does not improve CAR beyond LoRA-only baseline。λ=0.1（20× weight increase）双 seed 20K mean CAR=55.5%（z=0.47 vs null），明确在噪声内。LoRA fine-tuning 本身产生 +26pp CAR（54.5% vs Pi0.5 baseline 28.5%）。Per-task CAR ordering 跨所有条件完全一致（chocolate_pudding > milk > orange_juice > bbq_sauce），表明避障模式反映 demonstration distribution 特征而非 geometric supervision。\\n\\n**证据（rotation-fixed reeval 数据）**:\\n- LoRA-only (2 seeds): CAR=54.5%±2.8 (s0=56.5%, s1=52.5%), frozen=0%\\n- LoRA+SDF λ=0.005 (3 seeds): CAR=54.5%±2.3 (s0=57, s1=54, s2=52.5)\\n- LoRA+SDF λ=0.01 (3 seeds): CAR=56.33%±1.61 (s0=57, s1=57.5, s2=54.5) — p≈0.12 不显著，per-task 无系统提升，Task 3 驱动方差 s0=34%→s2=14% (D033)\\n- Per-task CAR pattern 完全一致（T3 BBQ 方差最大: l01=23.3% vs l005=20% vs LoRA=26%，种子噪声）\\n\\n**TSR collapse 机制分析 (M041)**:\\n- 复合机制：catastrophic forgetting of task semantics + retained collision avoidance\\n- SDF loss 不是 TSR 崩溃原因（LoRA baseline 崩溃幅度完全一致 -68.4% vs -68.7%）\\n- Robot 保留运动能力（0% frozen, EE ~0.5m）但丧失 goal-directed grasping/placing\\n- Safe failure rate 从 0.5% → ~50%（100×），obstacle displacement 减半\\n\\n**✅ CONFIRMED: Scenario B (D035)** — λ=0.1 20K 双 seed mean CAR=55.5% ≤ 57% 阈值，全域 SDF 冗余。\\n\\n**判定依据 (D033 阈值 + D035 确认)**：零分布 = LoRA(2) + l005(3) = 5 个无效 SDF 测量值 mean=54.5%, std=2.17%。λ=0.1 双 seed z=0.47，明确在噪声内。硬约束全部通过（TSR=51-54% ≥ 35%，frozen=0%）。\\n\\n| λ=0.1 结果 | 场景 | 状态 |\\n|-----------|------|------|\\n| **2-seed 20K mean=55.5% (≤57%)** | **B（完全 negative）** | **✅ 已确认** |\\n\\n**待最终确认（不影响叙事方向）**：\\n- **λ=0.1 30K × 2 seeds** (s0/s1 ~17:00 UTC 5/27) → 最终数字确认\\n- **λ=0.1 30K s2** (~08:40 UTC 5/28) → 第三 seed 补充\\n- LoRA seed2 (plan_013) → 3v3 seeds 统计\\n- Phase 2 λ=0 → SDF 是否有持久效应（Scenario B 下测 \\\"dose-dependent safety persist after removal\\\"）\\n\\n### Phase 2 解读 (contingent on λ=0.1)\\n\\n- 如果场景 A/C: Phase 2 测试 \\\"SDF 训练是否造成持久行为变化\\\"\\n- 如果场景 B: Phase 2 测试 \\\"dose-dependent safety 是否 persist after removal\\\"\\n- Phase 2 CAR ≈ LoRA-only → SDF 无持久效应\\n- Phase 2 CAR < LoRA-only → SDF 造成持久损伤\\n- Phase 2 CAR > LoRA-only → SDF 有持久编码（需更多 seeds 确认）\\n\\n## Anticipated Reviewer Concerns\\n\\n### R1 (最致命): Generalizability\\n\\\"仅在 SafeLIBERO + Pi0 系列上验证, 凭什么说 fake safety 是普遍问题?\\\"\\n→ **应对**: (1) 2+ tasks (object_pudding + spatial_bowl); (2) 3+ models (Pi0 + Pi0.5 + OpenVLA); (3) 收窄 claim scope + mechanistic argument (any model with low task capability will exhibit fake safety)\\n→ **接受率估算**: 1 task/2 model ~40% / 2 tasks+3 models ~55-65% / 3+ tasks ~65-75%\\n\\n### R2: Novelty of EE-only limitation\\n→ **应对**: 定量分析 (arm-body vs EE 碰撞比例 + oracle 排除其他解释); supporting claim 而非 primary\\n\\n### R3: No solution\\n\\\"诊断了问题但没解决\\\"\\n→ **应对**: (1) dfCAR metric 是 positive 工具贡献; (2) 揭示 avoidance 来源（implicit demo signal, not geometric supervision）本身是 actionable insight; (3) diagnostic paper 有方法论价值——知道问题在哪比错误地以为解决了更重要\\n\\n### R4: Action collapse is trivial\\n→ **应对**: 原因可能 trivial，但 metric contamination 后果 non-trivial; 后续工作基于被污染 CAR 得出错误结论\\n\\n### R5 (更新 D025): SDF redundancy — why bother testing it?\\n→ **应对**: (1) SDF geometric supervision 在 motion planning 领域广泛使用，先验合理; (2) negative result 排除合理路径; (3) 关键 insight 是 \\\"avoidance 来自 demo imitation, not geometry\\\" — 对未来 safety method 设计有指导意义\\n\\n### R6 (D025): Fine-tuning collapse — catastrophic forgetting?\\n→ **应对**: (1) M041 分析确认是复合机制 (forgetting of task semantics + retained avoidance); (2) LoRA fine-tuning 同时提升 CAR 和降低 TSR = conservative behavior, not safe behavior; (3) SDF 不是原因（LoRA baseline 同等崩溃）\\n\\n## Narrative Structure (D028: 3 Blocks + 1 Sub-block)\\n\\n### Block 1: Fake Safety Revelation + Capability Observation (Claim 1)\\n- **Evidence**: A1 800ep (frozen), Pi0.5 3-seed (geometric path safety), Pi0 baseline (action collapse)\\n- **Key finding**: CAR=91.5% is fake (99.6% frozen); Pi0.5 CAR=27% is geometric; neither is avoidance\\n- **Contribution**: dfCAR metric + threshold sensitivity analysis\\n- **Sub-block**: Capability↑ → motion↑ → collision↑ as supporting observation\\n\\n### Block 2: EE-only Geometric Supervision Boundary (Claim 2)\\n- **Evidence**: 3 oracle variants all < baseline; arm-body collision analysis\\n- **Narrative**: Runtime gradient correction structurally fails — alpha schedule and representation don't help; EE-only SDF = structural scope limit\\n- **Presentation**: Single unified table + collision part analysis\\n\\n### Block 3: Avoidance Source Diagnosis — Neither Necessary Nor Sufficient (Claim 3, unified with Claim 2)\\n- **Evidence**: LoRA-only 2-3 seeds + SDF 3 seeds × 3 lambdas, per-task comparison, oracle experiments\\n- **Key finding**: \\\"Neither necessary nor sufficient\\\" — (necessity) LoRA-only CAR=54.5% ≈ SDF across λ∈[0.005, 0.1], per-task ordering invariant; (sufficiency) oracle refinement CAR < baseline\\n- **Narrative**: EE-only SDF geometric supervision fails on two independent dimensions: it is unnecessary (demo distribution accounts for all avoidance gains) and structurally insufficient (EE-only monitoring redistributes collisions to unmonitored arm links). Per-task avoidance fingerprint (chocolate_pudding highest, bbq_sauce lowest) preserved across all 10 conditions confirms demonstration distribution as sole source.\\n- **TSR collapse analysis**: composite mechanism (task forgetting + avoidance retention)\\n- **Sub-narrative**: flat λ curve (Scenario B confirmed) + stepwise training dynamics (16K-30K) + Phase 2 persistence\\n\\n### 叙事原则\\n1. 每个 block 是 **evidence for structural claims**\\n2. Block 间逻辑递进：metric 有缺陷 (B1) → geometric supervision 有结构缺陷 (B2) → avoidance 来源是 demo data 而非 geometry (B3)\\n3. B3 是 positive diagnostic insight，展示\\\"避障可实现且来源是隐式学习\\\"\\n\\n## Figure Plan\\n\\n| ID | 内容 | Claim | 优先级 | 数据来源 | 状态 |\\n|----|------|-------|--------|---------|------|\\n| Fig 1 | Fake vs real safety 概念图 (displacement 对比) | 1 | 重要 | 设计 | 待做 |\\n| Fig 2 | EE Displacement 分布 (A1-frozen vs Pi0.5+A1-moving vs baseline) | 1 | **必须** | 修复后 eval JSON | 数据就绪 |\\n| Fig 3 | TSR-CAR scatter (多模型 + capability observation) | 1 | 重要 | 全部 eval 数据 | 数据就绪 |\\n| Fig 4 | Oracle refinement CAR bar chart + arm-body collision | 2 | **必须** | 3 oracle + baselines | 数据就绪 |\\n| Table 1 | 3-seed × 2-lambda × best/30K 完整结果矩阵 + EE disp | 3 | **必须** | Pi0.5+A1 修正数据 | 数据就绪 |\\n| Fig 5 | Lambda-CAR/TSR 曲线 (含 LoRA baseline 作 λ=0 点) | 3 | **必须** | LoRA baseline + SDF 数据 | 待 λ=0.1 |\\n| Table 2 | Phase 2 λ=0 ablation 结果 | 3 | 重要 | Phase 2 训练 | RUNNING |\\n\\n## Dependencies (Research Phase)\\n\\n- [x] A1 fake safety 800ep (Claim 1) — 99.6% fake (obstacle disp)\\n- [x] Pi0.5 baseline 3-seed (Claim 1 supporting) — CAR=26.8±1.6%, TSR=74.7±1.5%\\n- [x] Pi0.5+A1 3-seed × 2-lambda 训练 + eval (Claim 3) — confirmed real avoidance (D023)\\n- [x] EE displacement 修正 eval (Claim 3) — 3 seeds corrected, all consistent\\n- [x] Oracle 3 variants (Claim 2) — all < baseline\\n- [x] Spatial/object collision analysis (Claim 2) — arm-body dominant\\n- [x] **LoRA baseline** (Claim 3 attribution) — DONE: CAR=55%, SDF delta=0pp (D025)\\n- [x] **TSR collapse mechanism analysis** (Claim 3) — M041: composite (forgetting + avoidance retention)\\n- [ ] **LoRA baseline seed2** (plan_013, Claim 3) — RUNNING on westd-45947\\n- [ ] **Phase 2 λ=0** (Claim 3) — RUNNING on cuda:3\\n- [ ] **spatial_bowl A1 训练** (Claim 3) — RUNNING on cuda:0, ~20h\\n- [x] **Lambda=0.1 × 2 seeds 20K** (Claim 3) — D035 Scenario B confirmed: mean CAR=55.5% ≈ null\\n- [ ] **Lambda=0.1 × 3 seeds 30K** (Claim 3) — RUNNING: s0/s1 ~17:00 UTC 5/27, s2 ~08:40 UTC 5/28 (最终数字确认)\\n- [ ] **Pi0.5 baseline re-eval** (Claim 1) — RUNNING westd-45947, 补 EE displacement baseline\\n- [ ] **OpenVLA zero-shot eval** (Claim 1) — BLOCKED (模型下载损坏)\\n\", \"total_chars\": 11046, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Glob · `toolu_01BML52vDkft8FzUdjTUoZpa`</summary>

```json
{
  "pattern": "**/discussion*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "37076992-7ef7-4358-bb50-c148cf40aaaf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QpYq5fPifoutUDUD7WRWW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 451,
      "cache_read_input_tokens": 23893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 451
      },
      "output_tokens": 60,
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

_source line 11 · 2026-05-27T08:28:26.784Z_

<details><summary>↩ Tool result · `toolu_01BML52vDkft8FzUdjTUoZpa`</summary>

```text
artifacts/_project/paper/discussion.tex
docs/paper/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "9b55f210-b376-4b63-ba6d-42c568cc004c",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/discussion.tex",
      "docs/paper/discussion.tex"
    ],
    "durationMs": 34,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Glob · `toolu_01HGPHHRbwR5htRosUZjrS6e`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "e60b3aba-e31f-4db0-88cb-055f5888d456",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QpYq5fPifoutUDUD7WRWW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 451,
      "cache_read_input_tokens": 23893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 451
      },
      "output_tokens": 60,
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

_source line 13 · 2026-05-27T08:28:27.016Z_

<details><summary>↩ Tool result · `toolu_01HGPHHRbwR5htRosUZjrS6e`</summary>

```text
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/method.tex
docs/paper/_archive/method.tex
artifacts/drafts/method.tex
artifacts/_project/paper/related_work.tex
docs/paper/_archive/experiments.tex
docs/paper/_archive/conclusion_DEPRECATED.tex
artifacts/drafts/experiments.tex
artifacts/drafts/abstract.tex
artifacts/drafts/conclusion.tex
artifacts/drafts/introduction.tex
artifacts/drafts/related_work.tex
artifacts/_project/paper/analysis_claim1.tex
artifacts/drafts/analysis_claim1.tex
artifacts/_project/paper/analysis_claim2.tex
artifacts/drafts/analysis_claim2.tex
artifacts/_project/paper/analysis_claim3.tex
artifacts/drafts/analysis_claim3.tex
artifacts/_project/paper/experimental_framework.tex
artifacts/drafts/experimental_framework.tex
artifacts/_project/paper/introduction_v2.tex
artifacts/_project/paper/abstract_v2.tex
artifacts/drafts/abstract_v2.tex
artifacts/_project/paper/discussion.tex
artifacts/drafts/introduction_v2.tex
artifacts/drafts/related_work_v2.tex
artifacts/_project/paper/related_work_v2.tex
docs/paper/archive/analysis_claim4.tex
artifacts/dream_reports/dream_20260525T223036/best/paper.tex
artifacts/dream_reports/dream_20260525T223036/median/paper.tex
artifacts/dream_reports/dream_20260525T223036/worst/paper.tex
artifacts/dream_reports/dream_20260526T023936/best/paper.tex
artifacts/dream_reports/dream_20260526T023936/median/paper.tex
artifacts/dream_reports/dream_20260526T023936/worst/paper.tex
docs/paper/experimental_framework.tex
docs/paper/archive/analysis_claim3.tex
docs/paper/archive/analysis_claim1.tex
docs/paper/archive/analysis_claim2.tex
artifacts/reeval_comparison.tex
docs/paper/related_work.tex
docs/paper/main.tex
docs/paper/contingency_claim3.tex
docs/paper/method.tex
docs/paper/claim1.tex
docs/paper/claim2.tex
docs/paper/introduction.tex
docs/paper/discussion.tex
docs/paper/appendix.tex
docs/paper/abstract.tex
docs/paper/claim3.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "a450126c-9ed8-425f-89a4-7cc8061a1096",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/method.tex",
      "docs/paper/_archive/method.tex",
      "artifacts/drafts/method.tex",
      "artifacts/_project/paper/related_work.tex",
      "docs/paper/_archive/experiments.tex",
      "docs/paper/_archive/conclusion_DEPRECATED.tex",
      "artifacts/drafts/experiments.tex",
      "artifacts/drafts/abstract.tex",
      "artifacts/drafts/conclusion.tex",
      "artifacts/drafts/introduction.tex",
      "artifacts/drafts/related_work.tex",
      "artifacts/_project/paper/analysis_claim1.tex",
      "artifacts/drafts/analysis_claim1.tex",
      "artifacts/_project/paper/analysis_claim2.tex",
      "artifacts/drafts/analysis_claim2.tex",
      "artifacts/_project/paper/analysis_claim3.tex",
      "artifacts/drafts/analysis_claim3.tex",
      "artifacts/_project/paper/experimental_framework.tex",
      "artifacts/drafts/experimental_framework.tex",
      "artifacts/_project/paper/introduction_v2.tex",
      "artifacts/_project/paper/abstract_v2.tex",
      "artifacts/drafts/abstract_v2.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/drafts/introduction_v2.tex",
      "artifacts/drafts/related_work_v2.tex",
      "artifacts/_project/paper/related_work_v2.tex",
      "docs/paper/archive/analysis_claim4.tex",
      "artifacts/dream_reports/dream_20260525T223036/best/paper.tex",
      "artifacts/dream_reports/dream_20260525T223036/median/paper.tex",
      "artifacts/dream_reports/dream_20260525T223036/worst/paper.tex",
      "artifacts/dream_reports/dream_20260526T023936/best/paper.tex",
      "artifacts/dream_reports/dream_20260526T023936/median/paper.tex",
      "artifacts/dream_reports/dream_20260526T023936/worst/paper.tex",
      "docs/paper/experimental_framework.tex",
      "docs/paper/archive/analysis_claim3.tex",
      "docs/paper/archive/analysis_claim1.tex",
      "docs/paper/archive/analysis_claim2.tex",
      "artifacts/reeval_comparison.tex",
      "docs/paper/related_work.tex",
      "docs/paper/main.tex",
      "docs/paper/contingency_claim3.tex",
      "docs/paper/method.tex",
      "docs/paper/claim1.tex",
      "docs/paper/claim2.tex",
      "docs/paper/introduction.tex",
      "docs/paper/discussion.tex",
      "docs/paper/appendix.tex",
      "docs/paper/abstract.tex",
      "docs/paper/claim3.tex"
    ],
    "durationMs": 55,
    "numFiles": 50,
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
Let me read the existing discussion.tex files and some other key sections to understand the current state.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "07e3c12a-c4c6-4931-844c-01115b3817f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KXaQcKn2P7GGc8mTbVxUZS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6358,
      "cache_read_input_tokens": 24344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6358
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

Let me read the existing discussion files and the paper writing norms skill.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "1dd72480-2690-4c0a-9030-93dd65681fc3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KXaQcKn2P7GGc8mTbVxUZS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6358,
      "cache_read_input_tokens": 24344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6358
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

<details open><summary>🔧 Tool call — Read · `toolu_016xSb4x6opVtMcgN6xFj8SW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "97ac76d3-b2dc-4be2-936f-7dad18f3cc42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KXaQcKn2P7GGc8mTbVxUZS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6358,
      "cache_read_input_tokens": 24344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6358
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

_source line 17 · 2026-05-27T08:28:32.652Z_

<details><summary>↩ Tool result · `toolu_016xSb4x6opVtMcgN6xFj8SW`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	Across 70+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single conclusion: the robot is frozen, not safe. Action collapse renders reported CAR illusory (Pi0+A1 drops from 91.5\% to ${\approx}$\,0\% under displacement filtering); EE-only oracle refinement is counterproductive, \emph{reducing} CAR below unrefined baselines; and collision-free demonstrations, not EE-only SDF supervision, account for all measured avoidance gains in fine-tuned models.
4	
5	\paragraph{Implications for VLA safety evaluation.}
6	CAR$_\text{f}$ corrects action-collapse contamination using only end-effector position logging, already available in most evaluation pipelines. The bimodal displacement distribution (collapsed below 1\,$\mu$m, active above 200\,mm) makes $\tau_d$ robust across five orders of magnitude. We recommend reporting both raw CAR and CAR$_\text{f}$; the gap quantifies action-collapse contamination. The contamination is not specific to any model architecture or training procedure: Pi0 Full-FT (${\sim}$2.5B trainable), Pi0 LoRA (${\sim}$33.5M), and Pi0+A1 (${\sim}$658K) all exhibit $>$99\% fake safety despite a 4000$\times$ parameter range. It is a necessary consequence of evaluating collision avoidance without motion verification; episode-level filtering detects partial collapse invisible to model-level TSR checks.
7	
8	\paragraph{Two-level failure of EE-only geometric supervision.}
9	Our negative results identify two independent failure modes. \textit{Level~A: training signal masking.} At $\lambda \leq 0.01$, the SDF gradient is negligible relative to the action loss. The collision-free demonstration distribution already encodes spatial avoidance patterns: the ${\sim}$28\,pp CAR gain over the Pi0.5 baseline is entirely attributable to demonstration imitation. A Phase~2 ablation ($\lambda = 0$ after step 5K) confirms no persistent SDF encoding in the learned representation. \textit{Level~B: representation-collision misalignment.} Even with ground-truth SDF, EE-only supervision monitors a single point while collisions occur along the full kinematic chain. Oracle refinement pushes the EE away from obstacles while arm links sweep through them, producing lower CAR than unrefined baselines (73.1--76.9\% vs.\ 82--83\%). These two levels are independent: resolving signal masking (e.g., higher $\lambda$) would not address geometric misalignment, and vice versa. At $\lambda = 0.1$ (20$\times$ higher dose), CAR remains within the null range (55.5\%), confirming that Level~A signal masking is not the binding constraint. The failure is architectural: EE-only supervision cannot prevent arm-body collisions regardless of loss weight. Future geometric safety methods for manipulation must therefore (a) supervise the full kinematic chain rather than the end-effector alone, and (b) provide training signals that exceed the avoidance information already present in the demonstration distribution.
10	
11	\paragraph{Why EE-only SDF adds no value.}
12	Three observations explain the redundancy. First, VLA pre-trained representations already encode spatial structure: Pi0.5 achieves 26.8\% CAR without any safety-specific training, indicating implicit obstacle awareness in the visual-motor prior. Second, collision-free demonstrations amplify this prior by shifting the action distribution away from collision-prone trajectories, yielding the full ${\sim}$28\,pp CAR gain; the same distributional shift degrades TSR by ${\sim}$21--23\,pp, and EE-only SDF regularization cannot selectively reverse one effect without the other. Third, the Phase~2 ablation ($\lambda = 0$ after step 5K, CAR\,=\,57.5\%) confirms that SDF gradients produce no persistent encoding---the model's avoidance is identical whether SDF supervision is present, removed, or never applied, because the demonstration distribution fully determines the spatial avoidance pattern.
13	
14	\paragraph{Limitations.}
15	Our evaluation covers one benchmark suite (SafeLIBERO object\_pudding, four tasks) and two model families. Preliminary spatial\_bowl results show different patterns (Pi0 Full-FT: 0\% CAR despite 0.29\,m displacement; Pi0+A1: 0.8\% raw CAR with all safe episodes frozen, dfCAR${\approx}$0\%; Pi0.5: 13\% CAR), suggesting workspace geometry strongly affects collision modes. Generalization to OpenVLA, RT-2, or other architectures is untested. Oracle experiments were conducted on a largely frozen model (Pi0+A1, TSR${\approx}$0\%); testing on an actively moving policy (e.g., Pi0.5+LoRA, TSR${\approx}$51.5\%) would better isolate the EE-only structural limitation. The bimodal displacement gap may narrow on tasks with slower motions, making $\tau_d$ selection more consequential. Fine-tuning degrades TSR by ${\sim}$21--23\,pp; strategies that preserve task capability alongside avoidance remain unexplored.
16	\paragraph{Future work.}
17	Three directions follow: (1) full-body SDF along the kinematic chain, covering intermediate arm links; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) multi-benchmark evaluation to characterize how task geometry affects displacement distributions and threshold robustness.
18	
19	\paragraph{Broader impact.}
20	Contaminated CAR scores allow models with no real avoidance to pass safety benchmarks, creating false deployment readiness. CAR$_\text{f}$ exposes this gap with minimal changes to existing evaluation protocols.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "f05d92f4-ca45-491d-9e26-8b305ee31772",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
      "content": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 70+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single conclusion: the robot is frozen, not safe. Action collapse renders reported CAR illusory (Pi0+A1 drops from 91.5\\% to ${\\approx}$\\,0\\% under displacement filtering); EE-only oracle refinement is counterproductive, \\emph{reducing} CAR below unrefined baselines; and collision-free demonstrations, not EE-only SDF supervision, account for all measured avoidance gains in fine-tuned models.\n\n\\paragraph{Implications for VLA safety evaluation.}\nCAR$_\\text{f}$ corrects action-collapse contamination using only end-effector position logging, already available in most evaluation pipelines. The bimodal displacement distribution (collapsed below 1\\,$\\mu$m, active above 200\\,mm) makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both raw CAR and CAR$_\\text{f}$; the gap quantifies action-collapse contamination. The contamination is not specific to any model architecture or training procedure: Pi0 Full-FT (${\\sim}$2.5B trainable), Pi0 LoRA (${\\sim}$33.5M), and Pi0+A1 (${\\sim}$658K) all exhibit $>$99\\% fake safety despite a 4000$\\times$ parameter range. It is a necessary consequence of evaluating collision avoidance without motion verification; episode-level filtering detects partial collapse invisible to model-level TSR checks.\n\n\\paragraph{Two-level failure of EE-only geometric supervision.}\nOur negative results identify two independent failure modes. \\textit{Level~A: training signal masking.} At $\\lambda \\leq 0.01$, the SDF gradient is negligible relative to the action loss. The collision-free demonstration distribution already encodes spatial avoidance patterns: the ${\\sim}$28\\,pp CAR gain over the Pi0.5 baseline is entirely attributable to demonstration imitation. A Phase~2 ablation ($\\lambda = 0$ after step 5K) confirms no persistent SDF encoding in the learned representation. \\textit{Level~B: representation-collision misalignment.} Even with ground-truth SDF, EE-only supervision monitors a single point while collisions occur along the full kinematic chain. Oracle refinement pushes the EE away from obstacles while arm links sweep through them, producing lower CAR than unrefined baselines (73.1--76.9\\% vs.\\ 82--83\\%). These two levels are independent: resolving signal masking (e.g., higher $\\lambda$) would not address geometric misalignment, and vice versa. At $\\lambda = 0.1$ (20$\\times$ higher dose), CAR remains within the null range (55.5\\%), confirming that Level~A signal masking is not the binding constraint. The failure is architectural: EE-only supervision cannot prevent arm-body collisions regardless of loss weight. Future geometric safety methods for manipulation must therefore (a) supervise the full kinematic chain rather than the end-effector alone, and (b) provide training signals that exceed the avoidance information already present in the demonstration distribution.\n\n\\paragraph{Why EE-only SDF adds no value.}\nThree observations explain the redundancy. First, VLA pre-trained representations already encode spatial structure: Pi0.5 achieves 26.8\\% CAR without any safety-specific training, indicating implicit obstacle awareness in the visual-motor prior. Second, collision-free demonstrations amplify this prior by shifting the action distribution away from collision-prone trajectories, yielding the full ${\\sim}$28\\,pp CAR gain; the same distributional shift degrades TSR by ${\\sim}$21--23\\,pp, and EE-only SDF regularization cannot selectively reverse one effect without the other. Third, the Phase~2 ablation ($\\lambda = 0$ after step 5K, CAR\\,=\\,57.5\\%) confirms that SDF gradients produce no persistent encoding---the model's avoidance is identical whether SDF supervision is present, removed, or never applied, because the demonstration distribution fully determines the spatial avoidance pattern.\n\n\\paragraph{Limitations.}\nOur evaluation covers one benchmark suite (SafeLIBERO object\\_pudding, four tasks) and two model families. Preliminary spatial\\_bowl results show different patterns (Pi0 Full-FT: 0\\% CAR despite 0.29\\,m displacement; Pi0+A1: 0.8\\% raw CAR with all safe episodes frozen, dfCAR${\\approx}$0\\%; Pi0.5: 13\\% CAR), suggesting workspace geometry strongly affects collision modes. Generalization to OpenVLA, RT-2, or other architectures is untested. Oracle experiments were conducted on a largely frozen model (Pi0+A1, TSR${\\approx}$0\\%); testing on an actively moving policy (e.g., Pi0.5+LoRA, TSR${\\approx}$51.5\\%) would better isolate the EE-only structural limitation. The bimodal displacement gap may narrow on tasks with slower motions, making $\\tau_d$ selection more consequential. Fine-tuning degrades TSR by ${\\sim}$21--23\\,pp; strategies that preserve task capability alongside avoidance remain unexplored.\n\\paragraph{Future work.}\nThree directions follow: (1) full-body SDF along the kinematic chain, covering intermediate arm links; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) multi-benchmark evaluation to characterize how task geometry affects displacement distributions and threshold robustness.\n\n\\paragraph{Broader impact.}\nContaminated CAR scores allow models with no real avoidance to pass safety benchmarks, creating false deployment readiness. CAR$_\\text{f}$ exposes this gap with minimal changes to existing evaluation protocols.",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01RNPUBxnpzrXSZNoYRkRjKU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "c5e2db50-32f4-4d4f-b887-c601fa7b244c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KXaQcKn2P7GGc8mTbVxUZS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6358,
      "cache_read_input_tokens": 24344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6358
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

_source line 19 · 2026-05-27T08:28:32.934Z_

<details><summary>↩ Tool result · `toolu_01RNPUBxnpzrXSZNoYRkRjKU`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	This work identifies a systematic contamination in VLA collision avoidance evaluation: standard CAR conflates genuine obstacle avoidance with inaction caused by action collapse. Across all Pi0-family configurations evaluated on SafeLIBERO, over 98\% of episodes classified as safe exhibit sub-threshold displacement, rendering raw CAR unreliable as a safety metric. Displacement-filtered CAR (CAR$_\text{f}$) separates these two behaviors by excluding episodes below a displacement threshold $\tau_d$, providing a metric that credits only active avoidance. Two structural findings reinforce this diagnosis: TSR and CAR are anti-correlated under current methods (Section~\ref{sec:tsr_car}), and end-effector-only SDF refinement fails to prevent full-body collisions even with ground-truth geometry (Section~\ref{sec:ee_only}). Training-time SDF supervision on Pi0.5 is the sole configuration that produces non-zero CAR$_\text{f}$ with zero frozen rate, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\ref{sec:a1_pi05}).
4	
5	\paragraph{Limitations.}
6	The empirical scope of this study is bounded in several respects. All experiments use the \texttt{object\_pudding} Level~I suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. The EE-only SDF oracle (Section~\ref{sec:ee_only}) tests end-effector-level refinement exclusively; full-body SDF monitoring along the kinematic chain may yield different outcomes. The displacement threshold $\tau_d = 0.1$\,mm is empirically robust across four orders of magnitude (Appendix~\ref{app:threshold_sensitivity}), but remains task-dependent in principle. Pi0.5+A1 results are reported at the 10K-step checkpoint (seed~0); the 30K checkpoint is pending, and the final magnitude of the TSR-CAR tradeoff is not yet determined.
7	
8	\paragraph{Future work.}
9	Four directions follow from this analysis. First, full-body SDF monitoring along the robot kinematic chain would address the structural gap identified in Section~\ref{sec:ee_only}. Second, evaluation across additional SafeLIBERO suites and other manipulation benchmarks would test whether the contamination patterns generalize beyond the task family studied here. Third, cross-architecture evaluation on non-Pi0-family VLAs (OpenVLA, RT-2) would determine the prevalence of fake safety in the broader VLA landscape. Fourth, we recommend that future VLA safety evaluations report both raw CAR and CAR$_\text{f}$; the gap between the two quantifies the degree of action-collapse contamination in a given model.
10	
11	\paragraph{Broader impact.}
12	Metric reliability is a prerequisite for safe deployment of autonomous manipulation systems. Contaminated evaluation metrics create a risk that models with no genuine collision avoidance capability pass safety benchmarks and proceed to deployment. Displacement filtering is a low-cost correction: it requires only end-effector position logging, no additional data collection or model modification. The analysis in this work is conducted entirely in simulation; real-world deployment introduces additional safety considerations (sensor noise, sim-to-real transfer, dynamic obstacles) that fall outside the present scope.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "48e54cfa-ae26-4acd-83a1-25ec6cfeb6ab",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/discussion.tex",
      "content": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nThis work identifies a systematic contamination in VLA collision avoidance evaluation: standard CAR conflates genuine obstacle avoidance with inaction caused by action collapse. Across all Pi0-family configurations evaluated on SafeLIBERO, over 98\\% of episodes classified as safe exhibit sub-threshold displacement, rendering raw CAR unreliable as a safety metric. Displacement-filtered CAR (CAR$_\\text{f}$) separates these two behaviors by excluding episodes below a displacement threshold $\\tau_d$, providing a metric that credits only active avoidance. Two structural findings reinforce this diagnosis: TSR and CAR are anti-correlated under current methods (Section~\\ref{sec:tsr_car}), and end-effector-only SDF refinement fails to prevent full-body collisions even with ground-truth geometry (Section~\\ref{sec:ee_only}). Training-time SDF supervision on Pi0.5 is the sole configuration that produces non-zero CAR$_\\text{f}$ with zero frozen rate, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\\ref{sec:a1_pi05}).\n\n\\paragraph{Limitations.}\nThe empirical scope of this study is bounded in several respects. All experiments use the \\texttt{object\\_pudding} Level~I suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. The EE-only SDF oracle (Section~\\ref{sec:ee_only}) tests end-effector-level refinement exclusively; full-body SDF monitoring along the kinematic chain may yield different outcomes. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across four orders of magnitude (Appendix~\\ref{app:threshold_sensitivity}), but remains task-dependent in principle. Pi0.5+A1 results are reported at the 10K-step checkpoint (seed~0); the 30K checkpoint is pending, and the final magnitude of the TSR-CAR tradeoff is not yet determined.\n\n\\paragraph{Future work.}\nFour directions follow from this analysis. First, full-body SDF monitoring along the robot kinematic chain would address the structural gap identified in Section~\\ref{sec:ee_only}. Second, evaluation across additional SafeLIBERO suites and other manipulation benchmarks would test whether the contamination patterns generalize beyond the task family studied here. Third, cross-architecture evaluation on non-Pi0-family VLAs (OpenVLA, RT-2) would determine the prevalence of fake safety in the broader VLA landscape. Fourth, we recommend that future VLA safety evaluations report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination in a given model.\n\n\\paragraph{Broader impact.}\nMetric reliability is a prerequisite for safe deployment of autonomous manipulation systems. Contaminated evaluation metrics create a risk that models with no genuine collision avoidance capability pass safety benchmarks and proceed to deployment. Displacement filtering is a low-cost correction: it requires only end-effector position logging, no additional data collection or model modification. The analysis in this work is conducted entirely in simulation; real-world deployment introduces additional safety considerations (sensor noise, sim-to-real transfer, dynamic obstacles) that fall outside the present scope.\n",
      "numLines": 13,
      "startLine": 1,
      "totalLines": 13
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01X5mECvTrojzovur8xRwqP4`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "0f051ad3-4d2c-4b8b-bcae-db8136b42fc9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KXaQcKn2P7GGc8mTbVxUZS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6358,
      "cache_read_input_tokens": 24344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6358
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

_source line 21 · 2026-05-27T08:28:33.188Z_

<details><summary>↩ Tool result · `toolu_01X5mECvTrojzovur8xRwqP4`</summary>

````text
1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **禁止过度宣传**：不说 "revolutionary"、"groundbreaking"
75	- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元
76	- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了
77	- **缩写必须定义**：Abstract 中首次出现的缩写必须展开
78	
79	### 2.3 审稿人视角检验
80	
81	写完后用这个标准自检：审稿人能否在 30 秒内判断——
82	- 问题是否重要？
83	- 方法是否清楚？
84	- 贡献是否可信？
85	- 结果是否有说服力？
86	
87	---
88	
89	## 三、Introduction 写作规范
90	
91	### 3.1 完整叙事线（5 段结构）
92	
93	Introduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：
94	
95	1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈
96	2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题
97	3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）
98	4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题
99	5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献
100	
101	### 3.2 整体叙事结构
102	
103	```
104	现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结
105	```
106	
107	### 3.3 禁忌
108	
109	- **禁止泛泛介绍**：不要开头就写 "LLMs have shown remarkable capabilities..."，要从具体问题切入
110	- **禁止缺少过渡**：每段之间必须有逻辑连接
111	- **禁止实验报告风格**：Introduction 不是 "我们做了 X 实验得到了 Y 结果" 的罗列
112	- 每条 Contribution 必须有对应的 section/table 支撑
113	- Contribution 列表中不能出现未在前文铺垫过的概念
114	
115	---
116	
117	## 四、Related Work 写作规范
118	
119	### 4.1 目标
120	
121	让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。
122	
123	### 4.2 结构要求
124	
125	- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）
126	- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系
127	- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口
128	
129	### 4.3 禁忌
130	
131	- **禁止论文堆砌**：不要写成 "A proposed X. B proposed Y. C proposed Z." 的列表
132	- **目标不是展示读了多少论文**，而是做归纳和比较
133	- Contribution claim（"To our knowledge, no prior work..."）应放在 Introduction，不在 Related Work
134	
135	### 4.4 引用充足度
136	
137	- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**
138	- 任何一类缺失，审稿人会立刻看出来调研不充分
139	- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足
140	
141	---
142	
143	## 五、去 AI 写作风格（硬规则）
144	
145	以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**
146	
147	### 5.1 严禁破折号（最显著的 AI 痕迹）
148	
149	**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**
150	
151	- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**
152	- 替代方式：用逗号、括号或拆分为两个句子
153	- 强制检查命令：
154	  ```bash
155	  grep -n "—" paper/*.tex     # em-dash，每处人工判断是否必要
156	  grep -n " – " paper/*.tex   # 解释性 en-dash，几乎都应删除
157	  ```
158	- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）
159	
160	### 5.2 段落与句式
161	
162	- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的
163	- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句
164	- **禁止 -ing 短语结尾**：如 "..., highlighting the applicability of..." / "..., demonstrating the effectiveness of..."。这是 AI 写作最典型的标志之一
165	- **禁止连续使用 "Furthermore" / "Moreover" / "Additionally"**：一段内最多用一个过渡词
166	- **避免 "It is worth noting that..." / "Notably, ..."**：直接写要说的内容
167	
168	### 5.3 用词黑名单
169	
170	- 避免 "delve into" / "leverage" / "utilize" / "facilitate" — 用 "explore" / "use" / "enable"
171	- 避免 "a myriad of" / "a plethora of" — 用 "many" / "various"
172	- 避免 "in the realm of" / "in the context of" — 直接说
173	- 避免 "paradigm shift" / "novel" 过度使用
174	
175	### 5.4 校对清单（4 步）
176	
177	1. 全文 proofread 语法和拼写
178	2. 检查所有代词/指示词（this, that, it）是否指代明确
179	3. **`grep "—"` + `grep " – "` 全文清零**（删除所有解释性 dash，§5.1）
180	4. `grep "ing,"` 模式——大部分 -ing 分词短语需要改写
181	
182	---
183	
184	## 六、图表与视觉规范
185	
186	### 6.1 知识密度原则
187	
188	- **图表的信息必须紧凑**——不能为了美观而留大量白空间
189	- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中
190	- 能用 inline text 说清的不要占一整个 Figure
191	
192	### 6.2 表格规范
193	
194	- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）
195	- 小数精度全表统一
196	- 最优加粗、次优下划线
197	- Caption 必须自包含
198	
199	### 6.3 图片规范
200	
201	- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签
202	- 图中字体 >= 7pt（打印后仍可读）
203	- 栏宽约束需匹配目标 venue 模板要求
204	- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页
205	
206	### 6.4 空间效率
207	
208	- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源
209	- 优先使用 `\subfigure` 合并相关图
210	- Table 能 inline 就不要单独浮动
211	- 图表占比与其对叙事的贡献成正比
212	
213	### 6.5 页面节奏
214	
215	好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：
216	
217	- **text-equation-figure 三重奏**：重要概念用"文字解释 → 公式定义 → 图表直觉"三步展开
218	- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏
219	- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float
220	- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）
221	- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）
222	
223	### 6.6 表格 LaTeX 规范
224	
225	**Booktabs 标准（硬规则）**：
226	- 用 `\toprule` / `\midrule` / `\bottomrule`，禁止 `\hline`，禁止竖线 `|`
227	- 用 `\centering` 不用 `\begin{center}`（后者多加垂直空白）
228	- 最优结果加粗（`\textbf{}`），次优下划线（`\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向
229	- 小数精度全表统一（如全部保留 1 位或 2 位）
230	- Caption 在表格上方（`\caption` 在 `\begin{tabular}` 之前）
231	
232	**宽度决策树**：
233	- ≤5 列 → 单栏宽度（`\columnwidth`）
234	- 6–8 列 → 全文宽度（`\textwidth`，双栏模板用 `table*`）
235	- >8 列 → 拆成两张表或移入 appendix
236	
237	---
238	
239	## 七、投稿前通用准备
240	
241	### 7.1 模板必须官方（硬规则）
242	
243	- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）
244	- **不要用**：
245	  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）
246	  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）
247	  - 组里学长留的旧版本（来源不明、无法追溯）
248	- 风险：
249	  - 样式不符合 → desk reject
250	  - margin 不对 → 被审稿人质疑诚信
251	  - reference 格式错 → 被认为不规范
252	- 流程：先查会议官网 templates → 找不到再 `WebSearch "{venue} {year} latex template official"` → 仍找不到汇报 Director（不要用就近年版本顶替）
253	- `\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致
254	
255	### 7.2 投稿要求逐项核对
256	
257	- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A
258	- 页数限制：查目标会议官网
259	- 匿名化要求：review 版 vs camera-ready 版本设置不同
260	- 行号开启（review 版常需）
261	- 字体大小、margin 不得修改 sty 文件
262	
263	### 7.3 最终修改 10 项检查流程
264	
265	提交前必须逐一检查：
266	1. 所有最新实验结果已全部录入
267	2. 根据实验结果将叙事调至最优状态
268	3. 附录所有内容在正文中被引用且融入叙事
269	4. 无数据堆砌（每个数字服务于叙事推进）
270	5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）
271	6. 全文主线统一（idea 变化后各章节逻辑一致）
272	7. 所有专有名词有定义
273	8. 无 AI 风格标志（dash、-ing phrases、过度分段）
274	9. 图表知识密度高、无视觉遮挡
275	10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础
276	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "13856c7b-1237-4148-a53a-314e660fd1ca",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n### 6.5 页面节奏\n\n好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：\n\n- **text-equation-figure 三重奏**：重要概念用\"文字解释 → 公式定义 → 图表直觉\"三步展开\n- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏\n- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float\n- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）\n- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）\n\n### 6.6 表格 LaTeX 规范\n\n**Booktabs 标准（硬规则）**：\n- 用 `\\toprule` / `\\midrule` / `\\bottomrule`，禁止 `\\hline`，禁止竖线 `|`\n- 用 `\\centering` 不用 `\\begin{center}`（后者多加垂直空白）\n- 最优结果加粗（`\\textbf{}`），次优下划线（`\\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向\n- 小数精度全表统一（如全部保留 1 位或 2 位）\n- Caption 在表格上方（`\\caption` 在 `\\begin{tabular}` 之前）\n\n**宽度决策树**：\n- ≤5 列 → 单栏宽度（`\\columnwidth`）\n- 6–8 列 → 全文宽度（`\\textwidth`，双栏模板用 `table*`）\n- >8 列 → 拆成两张表或移入 appendix\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n",
      "numLines": 276,
      "startLine": 1,
      "totalLines": 276
    }
  }
}
````

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
I now have good context. Let me also read the claim3 analysis section to understand how the existing paper frames the SDF redundancy evidence, and check if there's a writing plan.

The `docs/paper/discussion.tex` is the older version. The `artifacts/_project/paper/discussion.tex` is the current working version. Let me review the claim3 section and the analysis sections to ensure consistency.

Let me also check the claim3 file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "bc55894d-3b3f-44ee-a03f-ad35679190fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VoMefBf5RQpGAwWbmXezT2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8174,
      "cache_read_input_tokens": 30702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8174
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

_source line 23_

Let me read the claim3 analysis and the existing main paper structure for context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "9a18c615-ad72-4095-acf2-832ff0f5d1b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VoMefBf5RQpGAwWbmXezT2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8174,
      "cache_read_input_tokens": 30702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8174
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

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01RA2T9rvwNp2J4jTnwPpNtM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "35d3088f-2721-4340-aa60-9e36b99df1fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VoMefBf5RQpGAwWbmXezT2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8174,
      "cache_read_input_tokens": 30702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8174
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

_source line 25 · 2026-05-27T08:28:41.951Z_

<details><summary>↩ Tool result · `toolu_01RA2T9rvwNp2J4jTnwPpNtM`</summary>

```text
1	\section{Avoidance Source Diagnosis}\label{sec:avoidance_source}
2	
3	Fine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\sim}$28 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only, LoRA+SDF ($\lambda = 0.005$), and LoRA+SDF ($\lambda = 0.01$) on Pi0.5, all evaluated at the 30K-step checkpoint.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Avoidance source attribution on SafeLIBERO. SDF adds no measurable CAR beyond LoRA-only across $\lambda \in [0.005, 0.1]$ ($p > 0.1$). All fine-tuned models exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}
8	\label{tab:avoidance_source}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lcccc}
12	\toprule
13	Method & Seeds & TSR (\%) & CAR (\%) & EE Disp (m) \\
14	\midrule
15	Pi0.5 baseline & 3 & 74.7\,$\pm$\,1.5 & 26.8\,$\pm$\,1.6 & 0.367 \\
16	\midrule
17	LoRA-only (no SDF) & 2 & 51.5 & 54.5\,$\pm$\,2.8 & 0.392 \\
18	LoRA+SDF $\lambda{=}0.005$ & 3 & 54.0\,$\pm$\,3.0 & 54.5\,$\pm$\,2.3 & 0.387 \\
19	LoRA+SDF $\lambda{=}0.01$ & 3 & 53.8\,$\pm$\,1.5 & 56.3\,$\pm$\,1.6 & 0.389 \\
20	LoRA+SDF $\lambda{=}0.1$\textsuperscript{$\dagger$} & 2 & 52.5 & 55.5 & -- \\
21	\bottomrule
22	\end{tabular}
23	\vspace{1pt}
24	{\footnotesize \textsuperscript{$\dagger$}20K-step checkpoint, 2 seeds. Stepwise curve (16K--28K) available for seed-0; 30K three-seed mean pending.}
25	\end{table}
26	
27	Table~\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\sim}$28 percentage points (26.8\% $\to$ 54.5\%) with zero frozen episodes and displacement above 0.37\,m, confirming genuine avoidance rather than action collapse. Adding SDF supervision produces no measurable benefit: LoRA-only CAR (54.5\%) is identical to $\lambda = 0.005$ and statistically indistinguishable from $\lambda = 0.01$ (56.3\%, $p > 0.1$; null distribution details in Appendix~\ref{sec:appendix_null}). A Phase~2 ablation ($\lambda = 0$ after step 5K) yields CAR\,=\,57.5\%, confirming that SDF gradients produce no lasting behavioral effect. EE-only SDF supervision is redundant across the full tested range $\lambda \in [0.005, 0.1]$ with the avoidance information already present in collision-free demonstrations.
28	
29	The per-task CAR ordering is preserved across all conditions: chocolate\_pudding consistently highest (68--76\%), bbq\_sauce consistently lowest (18--26\%), with intermediate tasks in fixed rank. This ordering persists whether or not SDF is present and is invariant to $\lambda$ across a 20$\times$ range, indicating that avoidance patterns directly reflect the spatial statistics of the collision-free demonstration distribution rather than geometric supervision.
30	
31	\paragraph{CAR--TSR trade-off.}\label{sec:tsr_collapse}
32	Fine-tuning degrades TSR by ${\sim}$21--23 percentage points (74.7\% $\to$ 51.5--54.0\%), with LoRA-only and SDF variants similarly affected (Appendix~\ref{sec:appendix_tsr_pertask}). The degradation reflects distributional shift from the pre-trained manipulation prior, not learned paralysis: all models retain $>$\,0.37\,m mean displacement and 0\% frozen episodes.
33	
34	\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
35	Increasing $\lambda$ by 20$\times$ to 0.1 yields CAR\,=\,55.5\% at the 20K checkpoint (2-seed mean; seeds: 55.0\%, 56.0\%), within the null distribution (mean 54.5\%, $\sigma = 2.15$, $z = 0.47$). The seed-0 stepwise curve spans six checkpoints from 16K to 28K: 55.5\%, 55.0\%, 60.5\%, 52.5\%, 53.5\%, 54.5\% (mean 55.3\%), fluctuating around the LoRA-only baseline of 54.5\% with no upward trend (per-seed details in Appendix~\ref{sec:appendix_stepwise}). The 22K checkpoint reaches 60.5\% ($z = 2.79$ against the curve mean), but three observations identify this as single-seed noise: (i)~seed-1 records only 56.5\% at the same step; (ii)~the three subsequent checkpoints (24K, 26K, 28K) all revert to 52.5--54.5\%; (iii)~the six-point mean of 55.3\% falls within 0.4$\sigma$ of the null. \placeholder{$\lambda{=}0.1$ 30K three-seed mean pending.}
36	
37	Across the full tested range $\lambda \in [0.005, 0.1]$---a 20$\times$ span---no condition exceeds the null: $\lambda = 0.005$ yields 54.5\%\,$\pm$\,2.3 (3 seeds, 30K), $\lambda = 0.01$ yields 56.3\%\,$\pm$\,1.6 ($p \approx 0.12$, 3 seeds, 30K), $\lambda = 0.1$ yields 55.5\% (2 seeds, 20K). EE-only SDF supervision exhibits no dose-response relationship with CAR (Figure~\ref{fig:lambda_car}). This disambiguates the two-level failure: because a 20$\times$ increase in loss weight fails to produce additional avoidance, the binding constraint is the structural mismatch between end-effector monitoring and full-body collision surfaces, not training signal magnitude. Per-task CAR ordering remains identical across all conditions (chocolate\_pudding $>$ milk $>$ orange\_juice $>$ bbq\_sauce), confirming that avoidance patterns reflect demonstration distribution characteristics rather than geometric supervision.
38	
39	\begin{figure}[t]
40	\centering
41	\includegraphics[width=0.85\linewidth]{fig5_lambda_curve}
42	\caption{Effect of SDF loss weight $\lambda$ on CAR and TSR. $\lambda = 0$: LoRA-only. $\lambda = 0.1$ (55.5\%) remains within the null band, confirming redundancy across a 20$\times$ loss weight range.}
43	\label{fig:lambda_car}
44	\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "7fab633f-56d6-49b2-9ac5-04e0cdbf7cbe",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
      "content": "\\section{Avoidance Source Diagnosis}\\label{sec:avoidance_source}\n\nFine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\\sim}$28 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only, LoRA+SDF ($\\lambda = 0.005$), and LoRA+SDF ($\\lambda = 0.01$) on Pi0.5, all evaluated at the 30K-step checkpoint.\n\n\\begin{table}[t]\n\\centering\n\\caption{Avoidance source attribution on SafeLIBERO. SDF adds no measurable CAR beyond LoRA-only across $\\lambda \\in [0.005, 0.1]$ ($p > 0.1$). All fine-tuned models exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\n\\label{tab:avoidance_source}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Seeds & TSR (\\%) & CAR (\\%) & EE Disp (m) \\\\\n\\midrule\nPi0.5 baseline & 3 & 74.7\\,$\\pm$\\,1.5 & 26.8\\,$\\pm$\\,1.6 & 0.367 \\\\\n\\midrule\nLoRA-only (no SDF) & 2 & 51.5 & 54.5\\,$\\pm$\\,2.8 & 0.392 \\\\\nLoRA+SDF $\\lambda{=}0.005$ & 3 & 54.0\\,$\\pm$\\,3.0 & 54.5\\,$\\pm$\\,2.3 & 0.387 \\\\\nLoRA+SDF $\\lambda{=}0.01$ & 3 & 53.8\\,$\\pm$\\,1.5 & 56.3\\,$\\pm$\\,1.6 & 0.389 \\\\\nLoRA+SDF $\\lambda{=}0.1$\\textsuperscript{$\\dagger$} & 2 & 52.5 & 55.5 & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\footnotesize \\textsuperscript{$\\dagger$}20K-step checkpoint, 2 seeds. Stepwise curve (16K--28K) available for seed-0; 30K three-seed mean pending.}\n\\end{table}\n\nTable~\\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\\sim}$28 percentage points (26.8\\% $\\to$ 54.5\\%) with zero frozen episodes and displacement above 0.37\\,m, confirming genuine avoidance rather than action collapse. Adding SDF supervision produces no measurable benefit: LoRA-only CAR (54.5\\%) is identical to $\\lambda = 0.005$ and statistically indistinguishable from $\\lambda = 0.01$ (56.3\\%, $p > 0.1$; null distribution details in Appendix~\\ref{sec:appendix_null}). A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,57.5\\%, confirming that SDF gradients produce no lasting behavioral effect. EE-only SDF supervision is redundant across the full tested range $\\lambda \\in [0.005, 0.1]$ with the avoidance information already present in collision-free demonstrations.\n\nThe per-task CAR ordering is preserved across all conditions: chocolate\\_pudding consistently highest (68--76\\%), bbq\\_sauce consistently lowest (18--26\\%), with intermediate tasks in fixed rank. This ordering persists whether or not SDF is present and is invariant to $\\lambda$ across a 20$\\times$ range, indicating that avoidance patterns directly reflect the spatial statistics of the collision-free demonstration distribution rather than geometric supervision.\n\n\\paragraph{CAR--TSR trade-off.}\\label{sec:tsr_collapse}\nFine-tuning degrades TSR by ${\\sim}$21--23 percentage points (74.7\\% $\\to$ 51.5--54.0\\%), with LoRA-only and SDF variants similarly affected (Appendix~\\ref{sec:appendix_tsr_pertask}). The degradation reflects distributional shift from the pre-trained manipulation prior, not learned paralysis: all models retain $>$\\,0.37\\,m mean displacement and 0\\% frozen episodes.\n\n\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\nIncreasing $\\lambda$ by 20$\\times$ to 0.1 yields CAR\\,=\\,55.5\\% at the 20K checkpoint (2-seed mean; seeds: 55.0\\%, 56.0\\%), within the null distribution (mean 54.5\\%, $\\sigma = 2.15$, $z = 0.47$). The seed-0 stepwise curve spans six checkpoints from 16K to 28K: 55.5\\%, 55.0\\%, 60.5\\%, 52.5\\%, 53.5\\%, 54.5\\% (mean 55.3\\%), fluctuating around the LoRA-only baseline of 54.5\\% with no upward trend (per-seed details in Appendix~\\ref{sec:appendix_stepwise}). The 22K checkpoint reaches 60.5\\% ($z = 2.79$ against the curve mean), but three observations identify this as single-seed noise: (i)~seed-1 records only 56.5\\% at the same step; (ii)~the three subsequent checkpoints (24K, 26K, 28K) all revert to 52.5--54.5\\%; (iii)~the six-point mean of 55.3\\% falls within 0.4$\\sigma$ of the null. \\placeholder{$\\lambda{=}0.1$ 30K three-seed mean pending.}\n\nAcross the full tested range $\\lambda \\in [0.005, 0.1]$---a 20$\\times$ span---no condition exceeds the null: $\\lambda = 0.005$ yields 54.5\\%\\,$\\pm$\\,2.3 (3 seeds, 30K), $\\lambda = 0.01$ yields 56.3\\%\\,$\\pm$\\,1.6 ($p \\approx 0.12$, 3 seeds, 30K), $\\lambda = 0.1$ yields 55.5\\% (2 seeds, 20K). EE-only SDF supervision exhibits no dose-response relationship with CAR (Figure~\\ref{fig:lambda_car}). This disambiguates the two-level failure: because a 20$\\times$ increase in loss weight fails to produce additional avoidance, the binding constraint is the structural mismatch between end-effector monitoring and full-body collision surfaces, not training signal magnitude. Per-task CAR ordering remains identical across all conditions (chocolate\\_pudding $>$ milk $>$ orange\\_juice $>$ bbq\\_sauce), confirming that avoidance patterns reflect demonstration distribution characteristics rather than geometric supervision.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{fig5_lambda_curve}\n\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. $\\lambda = 0$: LoRA-only. $\\lambda = 0.1$ (55.5\\%) remains within the null band, confirming redundancy across a 20$\\times$ loss weight range.}\n\\label{fig:lambda_car}\n\\end{figure}",
      "numLines": 44,
      "startLine": 1,
      "totalLines": 44
    }
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_01YMM3oHTQWAoGwBzWDYVuuw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/analysis_claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "b1db2194-b5bc-45ee-b1a8-9bc4e88eae09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VoMefBf5RQpGAwWbmXezT2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8174,
      "cache_read_input_tokens": 30702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8174
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

_source line 27 · 2026-05-27T08:28:42.397Z_

<details><summary>↩ Tool result · `toolu_01YMM3oHTQWAoGwBzWDYVuuw`</summary>

```text
1	\subsection{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\label{sec:ee_only}
2	
3	The analyses in Sections~\ref{sec:fake_safety} and~\ref{sec:tsr_car} identify action collapse and fake safety as pervasive problems, but leave open a natural question: could a sufficiently accurate SDF prediction still enable effective runtime refinement? To isolate the SDF representation itself from prediction quality, we construct an oracle experiment. We replace the learned SDF network with the ground-truth signed distance field computed directly from the known obstacle geometry. This oracle represents the theoretical upper bound of end-effector-only SDF refinement: it eliminates prediction error entirely, providing the refinement module with a perfect distance signal at every timestep. If the SDF refinement paradigm is sound, oracle performance should exceed that of unrefined baselines by a wide margin.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Oracle SDF refinement with ground-truth distance fields (160 episodes, 4 tasks $\times$ 40). All three variants achieve lower CAR than unrefined baselines (LoRA 82.0\%, Full-FT 83.0\%), and fake safe rates remain above 96\%.}
8	\label{tab:oracle}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lcccc}
12	\toprule
13	Method & TSR (\%) & CAR (\%) & Fake Safe (\%) & Refines/ep \\
14	\midrule
15	LoRA baseline (no refine) & 0.0 & 82.0 & 99.4 & -- \\
16	Full-FT baseline (no refine) & 0.5 & 83.0 & -- & -- \\
17	\midrule
18	Oracle-adaptive (GT, dyn.\ $\alpha$) & 0.0 & 75.0 & 98.3 & 14.2 \\
19	Oracle-fixed (GT, $\alpha{=}0.005$) & 0.0 & 73.1 & 98.3 & 14.8 \\
20	Oracle-feature (GT, feat.\ space) & 0.0 & 76.9 & 96.7 & 241.7 \\
21	\midrule
22	A3 learned SDF & 0.0 & 74.5 & -- & 0.0 \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	Table~\ref{tab:oracle} reports the results. All three oracle variants achieve CAR below that of the unrefined baselines. The best oracle (Oracle-feature, 76.9\%) falls 5.1 percentage points below the LoRA baseline (82.0\%) and 6.1 points below Full-FT (83.0\%). The adaptive and fixed-step variants perform worse still, at 75.0\% and 73.1\% respectively. These results are not marginal: the refinement module with perfect distance information produces more collisions than doing nothing at all. The fake safe rate tells a complementary story. Oracle-adaptive and Oracle-fixed both register 98.3\% fake safe episodes (118 of 120 and 115 of 117 safe episodes, respectively), while Oracle-feature registers 96.7\% (119 of 123). Ground-truth SDF refinement does not reduce action collapse; the vast majority of safe episodes remain attributable to inaction rather than obstacle avoidance.
28	
29	The per-task breakdown in Figure~\ref{fig:oracle_bar} reveals additional structure. On task~1, the most collision-prone task where the LoRA baseline achieves only 46.0\% CAR, Oracle-adaptive reaches 55.0\% and Oracle-feature reaches 47.5\%, a modest improvement consistent with a scenario where the end-effector is the primary collision body. On tasks~0, 2, and~3, all oracle variants produce lower CAR than the baseline: Oracle-adaptive drops from 96.0\% to 82.5\% on task~0 and from 98.0\% to 77.5\% on task~2. The refinement gradient, which pushes the end-effector away from the obstacle surface, perturbs the planned trajectory in ways that increase collisions elsewhere on the robot arm.
30	
31	This failure mode is structural. The SDF refinement paradigm as formulated in prior work~\cite{hu2025vlsa} computes the signed distance from the end-effector to the nearest obstacle surface and applies a gradient step to increase this distance when it falls below a safety threshold. The gradient operates exclusively on the end-effector position; no distance constraint applies to the remaining links of the robot arm. When the gradient pushes the end-effector away from an obstacle, the resulting joint-space displacement can rotate intermediate links toward or through the obstacle volume. The refinement thus trades one collision for another, with no mechanism to detect or prevent the substitution. The feature-space oracle makes this coupling problem explicit. It applies the SDF gradient in the policy's latent action space rather than in Cartesian coordinates, and fires on nearly every timestep (241.7 refinements per episode versus 14.2 for action-space variants). Yet its gradient magnitudes are extremely small (0.004--0.006, compared to 0.18--0.49 in action space), and the resulting CAR (76.9\%) shows no significant advantage over the action-space oracles. The latent space lacks a direct geometric relationship to full-body configuration; small perturbations in feature space do not reliably translate into collision-free joint trajectories.
32	
33	The A3 model with a learned SDF head illustrates the complementary failure. In this configuration, the SDF prediction network never outputs a distance below the refinement threshold across any of the 160 evaluation episodes, resulting in zero refinement steps. The learned SDF has calibrated its predictions to avoid triggering the safety mechanism, effectively reducing the model to an unrefined baseline (CAR of 74.5\%, consistent with the oracle range). The refinement module, even if it could improve safety, is never activated.
34	
35	These results establish that end-effector-only SDF is a structural limitation, not merely an engineering gap. Perfect distance information does not compensate for the absence of full-body collision awareness. Any refinement scheme that monitors only the end-effector position will remain blind to arm-body collisions, which constitute the dominant failure mode in manipulation tasks where the robot must reach around or past obstacles. Effective collision avoidance for VLA models will require representations that account for the geometric extent of the entire manipulator, not only its tip.
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "a95d303a-2c6b-4e9a-8627-cb534632a370",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/analysis_claim3.tex",
      "content": "\\subsection{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\\label{sec:ee_only}\n\nThe analyses in Sections~\\ref{sec:fake_safety} and~\\ref{sec:tsr_car} identify action collapse and fake safety as pervasive problems, but leave open a natural question: could a sufficiently accurate SDF prediction still enable effective runtime refinement? To isolate the SDF representation itself from prediction quality, we construct an oracle experiment. We replace the learned SDF network with the ground-truth signed distance field computed directly from the known obstacle geometry. This oracle represents the theoretical upper bound of end-effector-only SDF refinement: it eliminates prediction error entirely, providing the refinement module with a perfect distance signal at every timestep. If the SDF refinement paradigm is sound, oracle performance should exceed that of unrefined baselines by a wide margin.\n\n\\begin{table}[t]\n\\centering\n\\caption{Oracle SDF refinement with ground-truth distance fields (160 episodes, 4 tasks $\\times$ 40). All three variants achieve lower CAR than unrefined baselines (LoRA 82.0\\%, Full-FT 83.0\\%), and fake safe rates remain above 96\\%.}\n\\label{tab:oracle}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & TSR (\\%) & CAR (\\%) & Fake Safe (\\%) & Refines/ep \\\\\n\\midrule\nLoRA baseline (no refine) & 0.0 & 82.0 & 99.4 & -- \\\\\nFull-FT baseline (no refine) & 0.5 & 83.0 & -- & -- \\\\\n\\midrule\nOracle-adaptive (GT, dyn.\\ $\\alpha$) & 0.0 & 75.0 & 98.3 & 14.2 \\\\\nOracle-fixed (GT, $\\alpha{=}0.005$) & 0.0 & 73.1 & 98.3 & 14.8 \\\\\nOracle-feature (GT, feat.\\ space) & 0.0 & 76.9 & 96.7 & 241.7 \\\\\n\\midrule\nA3 learned SDF & 0.0 & 74.5 & -- & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:oracle} reports the results. All three oracle variants achieve CAR below that of the unrefined baselines. The best oracle (Oracle-feature, 76.9\\%) falls 5.1 percentage points below the LoRA baseline (82.0\\%) and 6.1 points below Full-FT (83.0\\%). The adaptive and fixed-step variants perform worse still, at 75.0\\% and 73.1\\% respectively. These results are not marginal: the refinement module with perfect distance information produces more collisions than doing nothing at all. The fake safe rate tells a complementary story. Oracle-adaptive and Oracle-fixed both register 98.3\\% fake safe episodes (118 of 120 and 115 of 117 safe episodes, respectively), while Oracle-feature registers 96.7\\% (119 of 123). Ground-truth SDF refinement does not reduce action collapse; the vast majority of safe episodes remain attributable to inaction rather than obstacle avoidance.\n\nThe per-task breakdown in Figure~\\ref{fig:oracle_bar} reveals additional structure. On task~1, the most collision-prone task where the LoRA baseline achieves only 46.0\\% CAR, Oracle-adaptive reaches 55.0\\% and Oracle-feature reaches 47.5\\%, a modest improvement consistent with a scenario where the end-effector is the primary collision body. On tasks~0, 2, and~3, all oracle variants produce lower CAR than the baseline: Oracle-adaptive drops from 96.0\\% to 82.5\\% on task~0 and from 98.0\\% to 77.5\\% on task~2. The refinement gradient, which pushes the end-effector away from the obstacle surface, perturbs the planned trajectory in ways that increase collisions elsewhere on the robot arm.\n\nThis failure mode is structural. The SDF refinement paradigm as formulated in prior work~\\cite{hu2025vlsa} computes the signed distance from the end-effector to the nearest obstacle surface and applies a gradient step to increase this distance when it falls below a safety threshold. The gradient operates exclusively on the end-effector position; no distance constraint applies to the remaining links of the robot arm. When the gradient pushes the end-effector away from an obstacle, the resulting joint-space displacement can rotate intermediate links toward or through the obstacle volume. The refinement thus trades one collision for another, with no mechanism to detect or prevent the substitution. The feature-space oracle makes this coupling problem explicit. It applies the SDF gradient in the policy's latent action space rather than in Cartesian coordinates, and fires on nearly every timestep (241.7 refinements per episode versus 14.2 for action-space variants). Yet its gradient magnitudes are extremely small (0.004--0.006, compared to 0.18--0.49 in action space), and the resulting CAR (76.9\\%) shows no significant advantage over the action-space oracles. The latent space lacks a direct geometric relationship to full-body configuration; small perturbations in feature space do not reliably translate into collision-free joint trajectories.\n\nThe A3 model with a learned SDF head illustrates the complementary failure. In this configuration, the SDF prediction network never outputs a distance below the refinement threshold across any of the 160 evaluation episodes, resulting in zero refinement steps. The learned SDF has calibrated its predictions to avoid triggering the safety mechanism, effectively reducing the model to an unrefined baseline (CAR of 74.5\\%, consistent with the oracle range). The refinement module, even if it could improve safety, is never activated.\n\nThese results establish that end-effector-only SDF is a structural limitation, not merely an engineering gap. Perfect distance information does not compensate for the absence of full-body collision awareness. Any refinement scheme that monitors only the end-effector position will remain blind to arm-body collisions, which constitute the dominant failure mode in manipulation tasks where the robot must reach around or past obstacles. Effective collision avoidance for VLA models will require representations that account for the geometric extent of the entire manipulator, not only its tip.\n",
      "numLines": 36,
      "startLine": 1,
      "totalLines": 36
    }
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of both the existing discussion section and the paper's content. Let me now write an updated discussion section that focuses on the SDF redundancy mechanism analysis as requested.

The existing `artifacts/_project/paper/discussion.tex` already has a good discussion section. The task is to update/refine it specifically focusing on the SDF redundancy mechanism analysis, considering:

1. Why SDF is redundant (mechanism)
2. Implications
3. Limitations

Let me compare what's already there with what's requested and draft an improved version. The existing version already covers most of the points, but let me refine it based on the task requirements.


I'm now looking at the core mechanistic insight: the EE-only SDF gradient doesn't actually align with the action space or collision geometry since collisions occur at arm links rather than just the end-effector, and the LoRA fine-tuning already implicitly learns collision avoidance from the demonstration data which is collision-free by construction. This makes the SDF loss signal fundamentally redundant with what the model already learns from the data itself. I should sharpen this analysis in the discussion to make the redundancy mechanism clearer, while keeping within the page constraints. I'm reviewing the existing discussion structure and realizing it already covers the key points well—the mechanism analysis about why SDF is redundant, the implications for safety evaluation, and the limitations. What I need to do is tighten the mechanistic framing to make the redundancy argument the central focus, sharpening the explanation of how geometric supervision alone captures what SDF adds, and then streamlining the rest to fit the target length.

I'm also noticing the LaTeX em-dashes that need to be converted to regular hyphens or removed entirely to match the writing standards. Let me rewrite the discussion section with this tighter focus and cleaner formatting.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "c80350af-1e2c-43c9-8a6d-1eb34c835387",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyxsSGgjyw5uLCWdDcTuZY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4111,
      "cache_read_input_tokens": 38876,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4111
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

_source line 29_

Now I have full context. Let me also quickly check for any existing em-dashes in the current discussion to comply with the writing norms.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "0a2834c1-993e-46a0-8f45-09a69640d65f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyxsSGgjyw5uLCWdDcTuZY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4111,
      "cache_read_input_tokens": 38876,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4111
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

_source line 30_

<details open><summary>🔧 Tool call — Grep · `toolu_01VcBJU2NGqSxoHVohJGY6dC`</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/discussion.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "5a73b20b-8132-4353-9554-a206599e4692",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyxsSGgjyw5uLCWdDcTuZY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4111,
      "cache_read_input_tokens": 38876,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4111
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

_source line 31 · 2026-05-27T08:29:06.852Z_

<details><summary>↩ Tool result · `toolu_01VcBJU2NGqSxoHVohJGY6dC`</summary>

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
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "67b563a8-58c7-4c74-a68c-e2ad28d8ef12",
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

### Assistant

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
OK, there are no triple dashes. Let me check for em-dashes (the Unicode character) and en-dashes.

Actually wait, looking at the existing file again:

Line 9: "At $\lambda = 0.1$ (20$\times$ higher dose)" - no em-dash
Line 9: "Level~A signal masking is not the binding constraint" - ok

Actually I see "---" might be encoded differently. Let me check for the actual Unicode characters.

Actually in the file I read, I don't see any `---` or `—` characters. The file uses commas and semicolons for separation, which is good.
 
I'm scanning through the text and confirming the punctuation is clean—line 9 mentions signal masking and geometric misalignment without problematic dashes, and the collision-free distribution statement also avoids em-dashes. Now I'm ready to revise the discussion section, sharpening the mechanistic analysis while staying under 0.75 pages. I'll restructure the opening to lead with the diagnostic conclusion, weave together the failure modes into a tighter argument, and explicitly address the action space misalignment issue.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "e9eaebcd-70f7-4bf5-8c3c-e483a2dc56f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkrH436f1e5dpYFEp2rvDF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1096,
      "cache_read_input_tokens": 42987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1096
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

_source line 33_

I have all the context. Now I'll write the updated discussion section with sharpened SDF redundancy mechanism analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "130e0b33-f48b-43a8-86bd-9bd0b22bf4f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkrH436f1e5dpYFEp2rvDF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1096,
      "cache_read_input_tokens": 42987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1096
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

_source line 34_

<details open><summary>🔧 Tool call — Edit · `toolu_01DLyfbCspQYF8BrAPhRDHrZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/discussion.tex",
  "old_string": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 70+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single conclusion: the robot is frozen, not safe. Action collapse renders reported CAR illusory (Pi0+A1 drops from 91.5\\% to ${\\approx}$\\,0\\% under displacement filtering); EE-only oracle refinement is counterproductive, \\emph{reducing} CAR below unrefined baselines; and collision-free demonstrations, not EE-only SDF supervision, account for all measured avoidance gains in fine-tuned models.\n\n\\paragraph{Implications for VLA safety evaluation.}\nCAR$_\\text{f}$ corrects action-collapse contamination using only end-effector position logging, already available in most evaluation pipelines. The bimodal displacement distribution (collapsed below 1\\,$\\mu$m, active above 200\\,mm) makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both raw CAR and CAR$_\\text{f}$; the gap quantifies action-collapse contamination. The contamination is not specific to any model architecture or training procedure: Pi0 Full-FT (${\\sim}$2.5B trainable), Pi0 LoRA (${\\sim}$33.5M), and Pi0+A1 (${\\sim}$658K) all exhibit $>$99\\% fake safety despite a 4000$\\times$ parameter range. It is a necessary consequence of evaluating collision avoidance without motion verification; episode-level filtering detects partial collapse invisible to model-level TSR checks.\n\n\\paragraph{Two-level failure of EE-only geometric supervision.}\nOur negative results identify two independent failure modes. \\textit{Level~A: training signal masking.} At $\\lambda \\leq 0.01$, the SDF gradient is negligible relative to the action loss. The collision-free demonstration distribution already encodes spatial avoidance patterns: the ${\\sim}$28\\,pp CAR gain over the Pi0.5 baseline is entirely attributable to demonstration imitation. A Phase~2 ablation ($\\lambda = 0$ after step 5K) confirms no persistent SDF encoding in the learned representation. \\textit{Level~B: representation-collision misalignment.} Even with ground-truth SDF, EE-only supervision monitors a single point while collisions occur along the full kinematic chain. Oracle refinement pushes the EE away from obstacles while arm links sweep through them, producing lower CAR than unrefined baselines (73.1--76.9\\% vs.\\ 82--83\\%). These two levels are independent: resolving signal masking (e.g., higher $\\lambda$) would not address geometric misalignment, and vice versa. At $\\lambda = 0.1$ (20$\\times$ higher dose), CAR remains within the null range (55.5\\%), confirming that Level~A signal masking is not the binding constraint. The failure is architectural: EE-only supervision cannot prevent arm-body collisions regardless of loss weight. Future geometric safety methods for manipulation must therefore (a) supervise the full kinematic chain rather than the end-effector alone, and (b) provide training signals that exceed the avoidance information already present in the demonstration distribution.\n\n\\paragraph{Why EE-only SDF adds no value.}\nThree observations explain the redundancy. First, VLA pre-trained representations already encode spatial structure: Pi0.5 achieves 26.8\\% CAR without any safety-specific training, indicating implicit obstacle awareness in the visual-motor prior. Second, collision-free demonstrations amplify this prior by shifting the action distribution away from collision-prone trajectories, yielding the full ${\\sim}$28\\,pp CAR gain; the same distributional shift degrades TSR by ${\\sim}$21--23\\,pp, and EE-only SDF regularization cannot selectively reverse one effect without the other. Third, the Phase~2 ablation ($\\lambda = 0$ after step 5K, CAR\\,=\\,57.5\\%) confirms that SDF gradients produce no persistent encoding---the model's avoidance is identical whether SDF supervision is present, removed, or never applied, because the demonstration distribution fully determines the spatial avoidance pattern.\n\n\\paragraph{Limitations.}\nOur evaluation covers one benchmark suite (SafeLIBERO object\\_pudding, four tasks) and two model families. Preliminary spatial\\_bowl results show different patterns (Pi0 Full-FT: 0\\% CAR despite 0.29\\,m displacement; Pi0+A1: 0.8\\% raw CAR with all safe episodes frozen, dfCAR${\\approx}$0\\%; Pi0.5: 13\\% CAR), suggesting workspace geometry strongly affects collision modes. Generalization to OpenVLA, RT-2, or other architectures is untested. Oracle experiments were conducted on a largely frozen model (Pi0+A1, TSR${\\approx}$0\\%); testing on an actively moving policy (e.g., Pi0.5+LoRA, TSR${\\approx}$51.5\\%) would better isolate the EE-only structural limitation. The bimodal displacement gap may narrow on tasks with slower motions, making $\\tau_d$ selection more consequential. Fine-tuning degrades TSR by ${\\sim}$21--23\\,pp; strategies that preserve task capability alongside avoidance remain unexplored.\n\\paragraph{Future work.}\nThree directions follow: (1) full-body SDF along the kinematic chain, covering intermediate arm links; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) multi-benchmark evaluation to characterize how task geometry affects displacement distributions and threshold robustness.\n\n\\paragraph{Broader impact.}\nContaminated CAR scores allow models with no real avoidance to pass safety benchmarks, creating false deployment readiness. CAR$_\\text{f}$ exposes this gap with minimal changes to existing evaluation protocols.",
  "new_string": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 90+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single conclusion: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (Pi0+A1 drops from 91.5\\% to ${\\approx}$\\,0\\% under displacement filtering); EE-only oracle refinement is counterproductive, \\emph{reducing} CAR below unrefined baselines; and collision-free demonstrations, not geometric supervision, account for all measured avoidance gains in fine-tuned models. We discuss the mechanistic basis for each finding and its implications.\n\n\\paragraph{Why EE-only SDF is redundant: a two-level account.}\nThe flat $\\lambda$-CAR curve ($\\lambda \\in [0.005, 0.1]$, 20$\\times$ range, all within the null band) rules out insufficient loss weight as the explanation and points to two independent structural causes.\n\n\\textit{(i) Demonstration data subsumes the SDF training signal.} Collision-free demonstrations shift the action distribution away from collision-prone trajectories by construction: every demonstration trajectory is safe, so imitating demonstrations implicitly encodes spatial avoidance. The ${\\sim}$28\\,pp CAR gain from LoRA fine-tuning (26.8\\% $\\to$ 54.5\\%) arises entirely from this distributional shift, with no SDF contribution. The per-task CAR ordering (chocolate\\_pudding highest, bbq\\_sauce lowest) is invariant across all SDF conditions and matches demonstration coverage, confirming that avoidance patterns originate from data statistics rather than geometric gradients. In this regime, EE-only SDF supplies a signal the model has already learned from imitation; adding a redundant gradient to a converged behavior produces no measurable effect. The Phase~2 ablation ($\\lambda = 0$ after step~5K, CAR = 57.5\\%) reinforces this interpretation: removing SDF supervision mid-training leaves avoidance unchanged, because the model never relied on it.\n\n\\textit{(ii) End-effector monitoring cannot prevent full-body collisions.} Even granting a perfect distance signal, the SDF gradient acts on a single point (the EE) while collisions predominantly occur along intermediate arm links and joints. In SafeLIBERO manipulation tasks, the robot must reach around obstacles, placing the forearm and wrist in close proximity to obstacle surfaces that the EE-only SDF does not monitor. Oracle experiments confirm this structural gap: ground-truth SDF refinement \\emph{reduces} CAR by 6\\textendash10\\,pp below unrefined baselines (73.1\\textendash76.9\\% vs.\\ 82\\textendash83\\%), because pushing the EE away from obstacles rotates unmonitored links through them. The action space compounds the mismatch: VLA policies output delta EE poses, so the SDF gradient operates in the same low-dimensional space as the action, with no mechanism to constrain the full joint configuration that realizes a given EE displacement.\n\nThese two levels are independent. Resolving (i) by finding a training signal beyond what demonstrations provide would not address (ii), and resolving (ii) through full-body monitoring would not change the fact that demonstrations already supply the avoidance signal. Effective geometric safety for VLA manipulation requires advances on both fronts: supervision that covers the full kinematic chain, and training signals that provide collision information beyond what is already implicit in collision-free demonstrations.\n\n\\paragraph{Implications for VLA safety evaluation.}\nCAR$_\\text{f}$ corrects action-collapse contamination using only end-effector position logging, already available in most evaluation pipelines. The bimodal displacement distribution (collapsed below 1\\,$\\mu$m, active above 200\\,mm) makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both raw CAR and CAR$_\\text{f}$; the gap quantifies action-collapse contamination. This contamination is not architecture-specific: Pi0 Full-FT (${\\sim}$2.5B trainable), Pi0 LoRA (${\\sim}$33.5M), and Pi0+A1 (${\\sim}$658K) all exhibit $>$99\\% fake safety despite a 4000$\\times$ parameter range. It is a necessary consequence of evaluating collision avoidance without verifying that the robot moved.\n\nMore broadly, our results suggest that safety in VLA manipulation may need to be addressed at the planning or constraint-satisfaction layer rather than through auxiliary losses on action prediction. When the action space is EE-centric, any loss defined over EE geometry inherits the same blind spot. Joint-space or full-body constraints, whether learned or imposed at planning time, offer a more natural interface for whole-arm collision avoidance.\n\n\\paragraph{Limitations.}\nOur evaluation covers one benchmark suite (SafeLIBERO object\\_pudding, four tasks) and two model families (Pi0, Pi0.5). Preliminary spatial\\_bowl results show different collision patterns, suggesting workspace geometry strongly affects collision modes; generalization to other tasks and architectures (OpenVLA, RT-2) is untested. Oracle experiments were conducted on a largely frozen model (Pi0+A1, TSR ${\\approx}$ 0\\%); testing on an actively moving policy would better isolate the EE-only structural limitation. The $\\lambda = 0.1$ condition reports 2-seed results at the 20K checkpoint; \\placeholder{30K three-seed confirmation pending}. Full-body SDF, the natural remedy for the structural mismatch identified here, remains untested. Fine-tuning degrades TSR by ${\\sim}$21\\textendash23\\,pp; strategies that preserve task capability alongside avoidance remain an open problem.\n\n\\paragraph{Future work.}\nThree directions follow from this analysis: (1) full-body SDF supervision along the kinematic chain, covering intermediate arm links and joints; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families to determine the prevalence of fake safety and metric contamination; (3) planning-layer safety constraints that operate in joint space rather than EE space, decoupling collision avoidance from the action prediction loss.\n\n\\paragraph{Broader impact.}\nContaminated CAR scores allow models with no genuine avoidance to pass safety benchmarks, creating false deployment readiness. CAR$_\\text{f}$ exposes this gap with minimal changes to existing evaluation protocols."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "c27c64ed-9b91-47f8-afd3-87ada5c2a47c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkrH436f1e5dpYFEp2rvDF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1096,
      "cache_read_input_tokens": 42987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1096
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

_source line 35 · 2026-05-27T08:30:26.129Z_

<details><summary>↩ Tool result · reported error · `toolu_01DLyfbCspQYF8BrAPhRDHrZ`</summary>

```text
&lt;tool_use_error>String to replace not found in file.
String: \section{Discussion and Conclusion}\label{sec:conclusion}

Across 70+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single conclusion: the robot is frozen, not safe. Action collapse renders reported CAR illusory (Pi0+A1 drops from 91.5\% to ${\approx}$\,0\% under displacement filtering); EE-only oracle refinement is counterproductive, \emph{reducing} CAR below unrefined baselines; and collision-free demonstrations, not EE-only SDF supervision, account for all measured avoidance gains in fine-tuned models.

\paragraph{Implications for VLA safety evaluation.}
CAR$_\text{f}$ corrects action-collapse contamination using only end-effector position logging, already available in most evaluation pipelines. The bimodal displacement distribution (collapsed below 1\,$\mu$m, active above 200\,mm) makes $\tau_d$ robust across five orders of magnitude. We recommend reporting both raw CAR and CAR$_\text{f}$; the gap quantifies action-collapse contamination. The contamination is not specific to any model architecture or training procedure: Pi0 Full-FT (${\sim}$2.5B trainable), Pi0 LoRA (${\sim}$33.5M), and Pi0+A1 (${\sim}$658K) all exhibit $>$99\% fake safety despite a 4000$\times$ parameter range. It is a necessary consequence of evaluating collision avoidance without motion verification; episode-level filtering detects partial collapse invisible to model-level TSR checks.

\paragraph{Two-level failure of EE-only geometric supervision.}
Our negative results identify two independent failure modes. \textit{Level~A: training signal masking.} At $\lambda \leq 0.01$, the SDF gradient is negligible relative to the action loss. The collision-free demonstration distribution already encodes spatial avoidance patterns: the ${\sim}$28\,pp CAR gain over the Pi0.5 baseline is entirely attributable to demonstration imitation. A Phase~2 ablation ($\lambda = 0$ after step 5K) confirms no persistent SDF encoding in the learned representation. \textit{Level~B: representation-collision misalignment.} Even with ground-truth SDF, EE-only supervision monitors a single point while collisions occur along the full kinematic chain. Oracle refinement pushes the EE away from obstacles while arm links sweep through them, producing lower CAR than unrefined baselines (73.1--76.9\% vs.\ 82--83\%). These two levels are independent: resolving signal masking (e.g., higher $\lambda$) would not address geometric misalignment, and vice versa. At $\lambda = 0.1$ (20$\times$ higher dose), CAR remains within the null range (55.5\%), confirming that Level~A signal masking is not the binding constraint. The failure is architectural: EE-only supervision cannot prevent arm-body collisions regardless of loss weight. Future geometric safety methods for manipulation must therefore (a) supervise the full kinematic chain rather than the end-effector alone, and (b) provide training signals that exceed the avoidance information already present in the demonstration distribution.

\paragraph{Why EE-only SDF adds no value.}
Three observations explain the redundancy. First, VLA pre-trained representations already encode spatial structure: Pi0.5 achieves 26.8\% CAR without any safety-specific training, indicating implicit obstacle awareness in the visual-motor prior. Second, collision-free demonstrations amplify this prior by shifting the action distribution away from collision-prone trajectories, yielding the full ${\sim}$28\,pp CAR gain; the same distributional shift degrades TSR by ${\sim}$21--23\,pp, and EE-only SDF regularization cannot selectively reverse one effect without the other. Third, the Phase~2 ablation ($\lambda = 0$ after step 5K, CAR\,=\,57.5\%) confirms that SDF gradients produce no persistent encoding---the model's avoidance is identical whether SDF supervision is present, removed, or never applied, because the demonstration distribution fully determines the spatial avoidance pattern.

\paragraph{Limitations.}
Our evaluation covers one benchmark suite (SafeLIBERO object\_pudding, four tasks) and two model families. Preliminary spatial\_bowl results show different patterns (Pi0 Full-FT: 0\% CAR despite 0.29\,m displacement; Pi0+A1: 0.8\% raw CAR with all safe episodes frozen, dfCAR${\approx}$0\%; Pi0.5: 13\% CAR), suggesting workspace geometry strongly affects collision modes. Generalization to OpenVLA, RT-2, or other architectures is untested. Oracle experiments were conducted on a largely frozen model (Pi0+A1, TSR${\approx}$0\%); testing on an actively moving policy (e.g., Pi0.5+LoRA, TSR${\approx}$51.5\%) would better isolate the EE-only structural limitation. The bimodal displacement gap may narrow on tasks with slower motions, making $\tau_d$ selection more consequential. Fine-tuning degrades TSR by ${\sim}$21--23\,pp; strategies that preserve task capability alongside avoidance remain unexplored.
\paragraph{Future work.}
Three directions follow: (1) full-body SDF along the kinematic chain, covering intermediate arm links; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) multi-benchmark evaluation to characterize how task geometry affects displacement distributions and threshold robustness.

\paragraph{Broader impact.}
Contaminated CAR scores allow models with no real avoidance to pass safety benchmarks, creating false deployment readiness. CAR$_\text{f}$ exposes this gap with minimal changes to existing evaluation protocols.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "e6a14125-bf22-47dd-a72d-08efd12e6811",
  "tool_use_result": "Error: String to replace not found in file.\nString: \\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 70+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single conclusion: the robot is frozen, not safe. Action collapse renders reported CAR illusory (Pi0+A1 drops from 91.5\\% to ${\\approx}$\\,0\\% under displacement filtering); EE-only oracle refinement is counterproductive, \\emph{reducing} CAR below unrefined baselines; and collision-free demonstrations, not EE-only SDF supervision, account for all measured avoidance gains in fine-tuned models.\n\n\\paragraph{Implications for VLA safety evaluation.}\nCAR$_\\text{f}$ corrects action-collapse contamination using only end-effector position logging, already available in most evaluation pipelines. The bimodal displacement distribution (collapsed below 1\\,$\\mu$m, active above 200\\,mm) makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both raw CAR and CAR$_\\text{f}$; the gap quantifies action-collapse contamination. The contamination is not specific to any model architecture or training procedure: Pi0 Full-FT (${\\sim}$2.5B trainable), Pi0 LoRA (${\\sim}$33.5M), and Pi0+A1 (${\\sim}$658K) all exhibit $>$99\\% fake safety despite a 4000$\\times$ parameter range. It is a necessary consequence of evaluating collision avoidance without motion verification; episode-level filtering detects partial collapse invisible to model-level TSR checks.\n\n\\paragraph{Two-level failure of EE-only geometric supervision.}\nOur negative results identify two independent failure modes. \\textit{Level~A: training signal masking.} At $\\lambda \\leq 0.01$, the SDF gradient is negligible relative to the action loss. The collision-free demonstration distribution already encodes spatial avoidance patterns: the ${\\sim}$28\\,pp CAR gain over the Pi0.5 baseline is entirely attributable to demonstration imitation. A Phase~2 ablation ($\\lambda = 0$ after step 5K) confirms no persistent SDF encoding in the learned representation. \\textit{Level~B: representation-collision misalignment.} Even with ground-truth SDF, EE-only supervision monitors a single point while collisions occur along the full kinematic chain. Oracle refinement pushes the EE away from obstacles while arm links sweep through them, producing lower CAR than unrefined baselines (73.1--76.9\\% vs.\\ 82--83\\%). These two levels are independent: resolving signal masking (e.g., higher $\\lambda$) would not address geometric misalignment, and vice versa. At $\\lambda = 0.1$ (20$\\times$ higher dose), CAR remains within the null range (55.5\\%), confirming that Level~A signal masking is not the binding constraint. The failure is architectural: EE-only supervision cannot prevent arm-body collisions regardless of loss weight. Future geometric safety methods for manipulation must therefore (a) supervise the full kinematic chain rather than the end-effector alone, and (b) provide training signals that exceed the avoidance information already present in the demonstration distribution.\n\n\\paragraph{Why EE-only SDF adds no value.}\nThree observations explain the redundancy. First, VLA pre-trained representations already encode spatial structure: Pi0.5 achieves 26.8\\% CAR without any safety-specific training, indicating implicit obstacle awareness in the visual-motor prior. Second, collision-free demonstrations amplify this prior by shifting the action distribution away from collision-prone trajectories, yielding the full ${\\sim}$28\\,pp CAR gain; the same distributional shift degrades TSR by ${\\sim}$21--23\\,pp, and EE-only SDF regularization cannot selectively reverse one effect without the other. Third, the Phase~2 ablation ($\\lambda = 0$ after step 5K, CAR\\,=\\,57.5\\%) confirms that SDF gradients produce no persistent encoding---the model's avoidance is identical whether SDF supervision is present, removed, or never applied, because the demonstration distribution fully determines the spatial avoidance pattern.\n\n\\paragraph{Limitations.}\nOur evaluation covers one benchmark suite (SafeLIBERO object\\_pudding, four tasks) and two model families. Preliminary spatial\\_bowl results show different patterns (Pi0 Full-FT: 0\\% CAR despite 0.29\\,m displacement; Pi0+A1: 0.8\\% raw CAR with all safe episodes frozen, dfCAR${\\approx}$0\\%; Pi0.5: 13\\% CAR), suggesting workspace geometry strongly affects collision modes. Generalization to OpenVLA, RT-2, or other architectures is untested. Oracle experiments were conducted on a largely frozen model (Pi0+A1, TSR${\\approx}$0\\%); testing on an actively moving policy (e.g., Pi0.5+LoRA, TSR${\\approx}$51.5\\%) would better isolate the EE-only structural limitation. The bimodal displacement gap may narrow on tasks with slower motions, making $\\tau_d$ selection more consequential. Fine-tuning degrades TSR by ${\\sim}$21--23\\,pp; strategies that preserve task capability alongside avoidance remain unexplored.\n\\paragraph{Future work.}\nThree directions follow: (1) full-body SDF along the kinematic chain, covering intermediate arm links; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) multi-benchmark evaluation to characterize how task geometry affects displacement distributions and threshold robustness.\n\n\\paragraph{Broader impact.}\nContaminated CAR scores allow models with no real avoidance to pass safety benchmarks, creating false deployment readiness. CAR$_\\text{f}$ exposes this gap with minimal changes to existing evaluation protocols."
}
```

</details>

---

### Assistant

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
The edit failed because the string didn't match exactly. Let me re-read the file more carefully to get the exact content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "234f61a8-4287-4639-a24f-3365712ad4f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LN1MA7aCHu4PvQC2NmeLLN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4913,
      "cache_read_input_tokens": 44083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4913
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

_source line 37_

Let me re-read the file to get the exact content for matching.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "ac2397f1-ce45-4212-8b94-6f532a293e11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LN1MA7aCHu4PvQC2NmeLLN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4913,
      "cache_read_input_tokens": 44083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4913
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

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_01MKEtBuG64ppgFutsDnPpcA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "49d7da95-24cb-4792-bbd0-6a697df5fa48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LN1MA7aCHu4PvQC2NmeLLN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4913,
      "cache_read_input_tokens": 44083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4913
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

_source line 39 · 2026-05-27T08:30:30.848Z_

<details><summary>↩ Tool result · `toolu_01MKEtBuG64ppgFutsDnPpcA`</summary>

```text
File unchanged since last read. The content from the earlier Read tool_result in this conversation is still current — refer to that instead of re-reading.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "f2018c84-4e73-4f08-a68a-cad9b78bc9e2",
  "tool_use_result": {
    "type": "file_unchanged",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/discussion.tex"
    }
  }
}
```

</details>

---

### Assistant

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
Let me just overwrite the whole file with the new content since the edit tool is having trouble matching.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "41f79539-dfff-47cd-82f0-e098605e82d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQ7U63DDJyESM7hM6cdMqg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 189,
      "cache_read_input_tokens": 48996,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 189
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

_source line 41_

I'll overwrite the file with the updated discussion section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "c0b0e1bf-1a06-4c6e-b26d-c496bafb0e80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQ7U63DDJyESM7hM6cdMqg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 189,
      "cache_read_input_tokens": 48996,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 189
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

_source line 42_

<details open><summary>🔧 Tool call — Write · `toolu_01HHaKioqdkNJaZ4RMPD9zyh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/discussion.tex",
  "content": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 90+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single conclusion: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (Pi0+A1 drops from 91.5\\% to ${\\approx}$\\,0\\% under displacement filtering); EE-only oracle refinement is counterproductive, \\emph{reducing} CAR below unrefined baselines; and collision-free demonstrations, not geometric supervision, account for all measured avoidance gains in fine-tuned models. We discuss the mechanistic basis for each finding and its implications.\n\n\\paragraph{Why EE-only SDF is redundant: a two-level account.}\nThe flat $\\lambda$-CAR curve ($\\lambda \\in [0.005, 0.1]$, 20$\\times$ range, all within the null band) rules out insufficient loss weight as the explanation and points to two independent structural causes.\n\n\\textit{(i) Demonstration data subsumes the SDF training signal.} Collision-free demonstrations shift the action distribution away from collision-prone trajectories by construction: every demonstration trajectory is safe, so imitating demonstrations implicitly encodes spatial avoidance. The ${\\sim}$28\\,pp CAR gain from LoRA fine-tuning (26.8\\% $\\to$ 54.5\\%) arises entirely from this distributional shift, with no SDF contribution. The per-task CAR ordering (chocolate\\_pudding highest, bbq\\_sauce lowest) is invariant across all SDF conditions and matches demonstration coverage, confirming that avoidance patterns originate from data statistics rather than geometric gradients. In this regime, EE-only SDF supplies a signal the model has already learned from imitation; adding a redundant gradient to a converged behavior produces no measurable effect. The Phase~2 ablation ($\\lambda = 0$ after step~5K, CAR = 57.5\\%) reinforces this interpretation: removing SDF supervision mid-training leaves avoidance unchanged, because the model never relied on it.\n\n\\textit{(ii) End-effector monitoring cannot prevent full-body collisions.} Even granting a perfect distance signal, the SDF gradient acts on a single point (the EE) while collisions predominantly occur along intermediate arm links and joints. In SafeLIBERO manipulation tasks, the robot must reach around obstacles, placing the forearm and wrist in close proximity to obstacle surfaces that the EE-only SDF does not monitor. Oracle experiments confirm this structural gap: ground-truth SDF refinement \\emph{reduces} CAR by 6\\textendash10\\,pp below unrefined baselines (73.1\\textendash76.9\\% vs.\\ 82\\textendash83\\%), because pushing the EE away from obstacles rotates unmonitored links through them. The action space compounds the mismatch: VLA policies output delta EE poses, so the SDF gradient operates in the same low-dimensional space as the action, with no mechanism to constrain the full joint configuration that realizes a given EE displacement.\n\nThese two levels are independent. Resolving (i) by finding a training signal beyond what demonstrations provide would not address (ii), and resolving (ii) through full-body monitoring would not change the fact that demonstrations already supply the avoidance signal. Effective geometric safety for VLA manipulation requires advances on both fronts: supervision that covers the full kinematic chain, and training signals that provide collision information beyond what is already implicit in collision-free demonstrations.\n\n\\paragraph{Implications for VLA safety evaluation.}\nCAR$_\\text{f}$ corrects action-collapse contamination using only end-effector position logging, already available in most evaluation pipelines. The bimodal displacement distribution (collapsed below 1\\,$\\mu$m, active above 200\\,mm) makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both raw CAR and CAR$_\\text{f}$; the gap quantifies action-collapse contamination. This contamination is not architecture-specific: Pi0 Full-FT (${\\sim}$2.5B trainable), Pi0 LoRA (${\\sim}$33.5M), and Pi0+A1 (${\\sim}$658K) all exhibit $>$99\\% fake safety despite a 4000$\\times$ parameter range. It is a necessary consequence of evaluating collision avoidance without verifying that the robot moved.\n\nMore broadly, our results suggest that safety in VLA manipulation may need to be addressed at the planning or constraint-satisfaction layer rather than through auxiliary losses on action prediction. When the action space is EE-centric, any loss defined over EE geometry inherits the same blind spot. Joint-space or full-body constraints, whether learned or imposed at planning time, offer a more natural interface for whole-arm collision avoidance.\n\n\\paragraph{Limitations.}\nOur evaluation covers one benchmark suite (SafeLIBERO object\\_pudding, four tasks) and two model families (Pi0, Pi0.5). Preliminary spatial\\_bowl results show different collision patterns, suggesting workspace geometry strongly affects collision modes; generalization to other tasks and architectures (OpenVLA, RT-2) is untested. Oracle experiments were conducted on a largely frozen model (Pi0+A1, TSR ${\\approx}$ 0\\%); testing on an actively moving policy would better isolate the EE-only structural limitation. The $\\lambda = 0.1$ condition reports 2-seed results at the 20K checkpoint; \\placeholder{30K three-seed confirmation pending}. Full-body SDF, the natural remedy for the structural mismatch identified here, remains untested. Fine-tuning degrades TSR by ${\\sim}$21\\textendash23\\,pp; strategies that preserve task capability alongside avoidance remain an open problem.\n\n\\paragraph{Future work.}\nThree directions follow from this analysis: (1) full-body SDF supervision along the kinematic chain, covering intermediate arm links and joints; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families to determine the prevalence of fake safety and metric contamination; (3) planning-layer safety constraints that operate in joint space rather than EE space, decoupling collision avoidance from the action prediction loss.\n\n\\paragraph{Broader impact.}\nContaminated CAR scores allow models with no genuine avoidance to pass safety benchmarks, creating false deployment readiness. CAR$_\\text{f}$ exposes this gap with minimal changes to existing evaluation protocols.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "a580e8b2-d38b-4b66-b744-452097102ae0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQ7U63DDJyESM7hM6cdMqg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 189,
      "cache_read_input_tokens": 48996,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 189
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

_source line 43 · 2026-05-27T08:30:47.193Z_

<details><summary>↩ Tool result · `toolu_01HHaKioqdkNJaZ4RMPD9zyh`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "da29e0e4-4c4d-40c2-a55e-a2ddf0d23de4",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/discussion.tex",
    "content": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 90+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single conclusion: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (Pi0+A1 drops from 91.5\\% to ${\\approx}$\\,0\\% under displacement filtering); EE-only oracle refinement is counterproductive, \\emph{reducing} CAR below unrefined baselines; and collision-free demonstrations, not geometric supervision, account for all measured avoidance gains in fine-tuned models. We discuss the mechanistic basis for each finding and its implications.\n\n\\paragraph{Why EE-only SDF is redundant: a two-level account.}\nThe flat $\\lambda$-CAR curve ($\\lambda \\in [0.005, 0.1]$, 20$\\times$ range, all within the null band) rules out insufficient loss weight as the explanation and points to two independent structural causes.\n\n\\textit{(i) Demonstration data subsumes the SDF training signal.} Collision-free demonstrations shift the action distribution away from collision-prone trajectories by construction: every demonstration trajectory is safe, so imitating demonstrations implicitly encodes spatial avoidance. The ${\\sim}$28\\,pp CAR gain from LoRA fine-tuning (26.8\\% $\\to$ 54.5\\%) arises entirely from this distributional shift, with no SDF contribution. The per-task CAR ordering (chocolate\\_pudding highest, bbq\\_sauce lowest) is invariant across all SDF conditions and matches demonstration coverage, confirming that avoidance patterns originate from data statistics rather than geometric gradients. In this regime, EE-only SDF supplies a signal the model has already learned from imitation; adding a redundant gradient to a converged behavior produces no measurable effect. The Phase~2 ablation ($\\lambda = 0$ after step~5K, CAR = 57.5\\%) reinforces this interpretation: removing SDF supervision mid-training leaves avoidance unchanged, because the model never relied on it.\n\n\\textit{(ii) End-effector monitoring cannot prevent full-body collisions.} Even granting a perfect distance signal, the SDF gradient acts on a single point (the EE) while collisions predominantly occur along intermediate arm links and joints. In SafeLIBERO manipulation tasks, the robot must reach around obstacles, placing the forearm and wrist in close proximity to obstacle surfaces that the EE-only SDF does not monitor. Oracle experiments confirm this structural gap: ground-truth SDF refinement \\emph{reduces} CAR by 6\\textendash10\\,pp below unrefined baselines (73.1\\textendash76.9\\% vs.\\ 82\\textendash83\\%), because pushing the EE away from obstacles rotates unmonitored links through them. The action space compounds the mismatch: VLA policies output delta EE poses, so the SDF gradient operates in the same low-dimensional space as the action, with no mechanism to constrain the full joint configuration that realizes a given EE displacement.\n\nThese two levels are independent. Resolving (i) by finding a training signal beyond what demonstrations provide would not address (ii), and resolving (ii) through full-body monitoring would not change the fact that demonstrations already supply the avoidance signal. Effective geometric safety for VLA manipulation requires advances on both fronts: supervision that covers the full kinematic chain, and training signals that provide collision information beyond what is already implicit in collision-free demonstrations.\n\n\\paragraph{Implications for VLA safety evaluation.}\nCAR$_\\text{f}$ corrects action-collapse contamination using only end-effector position logging, already available in most evaluation pipelines. The bimodal displacement distribution (collapsed below 1\\,$\\mu$m, active above 200\\,mm) makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both raw CAR and CAR$_\\text{f}$; the gap quantifies action-collapse contamination. This contamination is not architecture-specific: Pi0 Full-FT (${\\sim}$2.5B trainable), Pi0 LoRA (${\\sim}$33.5M), and Pi0+A1 (${\\sim}$658K) all exhibit $>$99\\% fake safety despite a 4000$\\times$ parameter range. It is a necessary consequence of evaluating collision avoidance without verifying that the robot moved.\n\nMore broadly, our results suggest that safety in VLA manipulation may need to be addressed at the planning or constraint-satisfaction layer rather than through auxiliary losses on action prediction. When the action space is EE-centric, any loss defined over EE geometry inherits the same blind spot. Joint-space or full-body constraints, whether learned or imposed at planning time, offer a more natural interface for whole-arm collision avoidance.\n\n\\paragraph{Limitations.}\nOur evaluation covers one benchmark suite (SafeLIBERO object\\_pudding, four tasks) and two model families (Pi0, Pi0.5). Preliminary spatial\\_bowl results show different collision patterns, suggesting workspace geometry strongly affects collision modes; generalization to other tasks and architectures (OpenVLA, RT-2) is untested. Oracle experiments were conducted on a largely frozen model (Pi0+A1, TSR ${\\approx}$ 0\\%); testing on an actively moving policy would better isolate the EE-only structural limitation. The $\\lambda = 0.1$ condition reports 2-seed results at the 20K checkpoint; \\placeholder{30K three-seed confirmation pending}. Full-body SDF, the natural remedy for the structural mismatch identified here, remains untested. Fine-tuning degrades TSR by ${\\sim}$21\\textendash23\\,pp; strategies that preserve task capability alongside avoidance remain an open problem.\n\n\\paragraph{Future work.}\nThree directions follow from this analysis: (1) full-body SDF supervision along the kinematic chain, covering intermediate arm links and joints; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families to determine the prevalence of fake safety and metric contamination; (3) planning-layer safety constraints that operate in joint space rather than EE space, decoupling collision avoidance from the action prediction loss.\n\n\\paragraph{Broader impact.}\nContaminated CAR scores allow models with no genuine avoidance to pass safety benchmarks, creating false deployment readiness. CAR$_\\text{f}$ exposes this gap with minimal changes to existing evaluation protocols.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 12,
        "newStart": 1,
        "newLines": 26,
        "lines": [
          " \\section{Discussion and Conclusion}\\label{sec:conclusion}",
          " ",
          "-This work identifies a systematic contamination in VLA collision avoidance evaluation: standard CAR conflates genuine obstacle avoidance with inaction caused by action collapse. Across all Pi0-family configurations evaluated on SafeLIBERO, over 98\\% of episodes classified as safe exhibit sub-threshold displacement, rendering raw CAR unreliable as a safety metric. Displacement-filtered CAR (CAR$_\\text{f}$) separates these two behaviors by excluding episodes below a displacement threshold $\\tau_d$, providing a metric that credits only active avoidance. Two structural findings reinforce this diagnosis: TSR and CAR are anti-correlated under current methods (Section~\\ref{sec:tsr_car}), and end-effector-only SDF refinement fails to prevent full-body collisions even with ground-truth geometry (Section~\\ref{sec:ee_only}). Training-time SDF supervision on Pi0.5 is the sole configuration that produces non-zero CAR$_\\text{f}$ with zero frozen rate, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\\ref{sec:a1_pi05}).",
          "+Across 90+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single conclusion: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (Pi0+A1 drops from 91.5\\% to ${\\approx}$\\,0\\% under displacement filtering); EE-only oracle refinement is counterproductive, \\emph{reducing} CAR below unrefined baselines; and collision-free demonstrations, not geometric supervision, account for all measured avoidance gains in fine-tuned models. We discuss the mechanistic basis for each finding and its implications.",
          " ",
          "+\\paragraph{Why EE-only SDF is redundant: a two-level account.}",
          "+The flat $\\lambda$-CAR curve ($\\lambda \\in [0.005, 0.1]$, 20$\\times$ range, all within the null band) rules out insufficient loss weight as the explanation and points to two independent structural causes.",
          "+",
          "+\\textit{(i) Demonstration data subsumes the SDF training signal.} Collision-free demonstrations shift the action distribution away from collision-prone trajectories by construction: every demonstration trajectory is safe, so imitating demonstrations implicitly encodes spatial avoidance. The ${\\sim}$28\\,pp CAR gain from LoRA fine-tuning (26.8\\% $\\to$ 54.5\\%) arises entirely from this distributional shift, with no SDF contribution. The per-task CAR ordering (chocolate\\_pudding highest, bbq\\_sauce lowest) is invariant across all SDF conditions and matches demonstration coverage, confirming that avoidance patterns originate from data statistics rather than geometric gradients. In this regime, EE-only SDF supplies a signal the model has already learned from imitation; adding a redundant gradient to a converged behavior produces no measurable effect. The Phase~2 ablation ($\\lambda = 0$ after step~5K, CAR = 57.5\\%) reinforces this interpretation: removing SDF supervision mid-training leaves avoidance unchanged, because the model never relied on it.",
          "+",
          "+\\textit{(ii) End-effector monitoring cannot prevent full-body collisions.} Even granting a perfect distance signal, the SDF gradient acts on a single point (the EE) while collisions predominantly occur along intermediate arm links and joints. In SafeLIBERO manipulation tasks, the robot must reach around obstacles, placing the forearm and wrist in close proximity to obstacle surfaces that the EE-only SDF does not monitor. Oracle experiments confirm this structural gap: ground-truth SDF refinement \\emph{reduces} CAR by 6\\textendash10\\,pp below unrefined baselines (73.1\\textendash76.9\\% vs.\\ 82\\textendash83\\%), because pushing the EE away from obstacles rotates unmonitored links through them. The action space compounds the mismatch: VLA policies output delta EE poses, so the SDF gradient operates in the same low-dimensional space as the action, with no mechanism to constrain the full joint configuration that realizes a given EE displacement.",
          "+",
          "+These two levels are independent. Resolving (i) by finding a training signal beyond what demonstrations provide would not address (ii), and resolving (ii) through full-body monitoring would not change the fact that demonstrations already supply the avoidance signal. Effective geometric safety for VLA manipulation requires advances on both fronts: supervision that covers the full kinematic chain, and training signals that provide collision information beyond what is already implicit in collision-free demonstrations.",
          "+",
          "+\\paragraph{Implications for VLA safety evaluation.}",
          "+CAR$_\\text{f}$ corrects action-collapse contamination using only end-effector position logging, already available in most evaluation pipelines. The bimodal displacement distribution (collapsed below 1\\,$\\mu$m, active above 200\\,mm) makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both raw CAR and CAR$_\\text{f}$; the gap quantifies action-collapse contamination. This contamination is not architecture-specific: Pi0 Full-FT (${\\sim}$2.5B trainable), Pi0 LoRA (${\\sim}$33.5M), and Pi0+A1 (${\\sim}$658K) all exhibit $>$99\\% fake safety despite a 4000$\\times$ parameter range. It is a necessary consequence of evaluating collision avoidance without verifying that the robot moved.",
          "+",
          "+More broadly, our results suggest that safety in VLA manipulation may need to be addressed at the planning or constraint-satisfaction layer rather than through auxiliary losses on action prediction. When the action space is EE-centric, any loss defined over EE geometry inherits the same blind spot. Joint-space or full-body constraints, whether learned or imposed at planning time, offer a more natural interface for whole-arm collision avoidance.",
          "+",
          " \\paragraph{Limitations.}",
          "-The empirical scope of this study is bounded in several respects. All experiments use the \\texttt{object\\_pudding} Level~I suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. The EE-only SDF oracle (Section~\\ref{sec:ee_only}) tests end-effector-level refinement exclusively; full-body SDF monitoring along the kinematic chain may yield different outcomes. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across four orders of magnitude (Appendix~\\ref{app:threshold_sensitivity}), but remains task-dependent in principle. Pi0.5+A1 results are reported at the 10K-step checkpoint (seed~0); the 30K checkpoint is pending, and the final magnitude of the TSR-CAR tradeoff is not yet determined.",
          "+Our evaluation covers one benchmark suite (SafeLIBERO object\\_pudding, four tasks) and two model families (Pi0, Pi0.5). Preliminary spatial\\_bowl results show different collision patterns, suggesting workspace geometry strongly affects collision modes; generalization to other tasks and architectures (OpenVLA, RT-2) is untested. Oracle experiments were conducted on a largely frozen model (Pi0+A1, TSR ${\\approx}$ 0\\%); testing on an actively moving policy would better isolate the EE-only structural limitation. The $\\lambda = 0.1$ condition reports 2-seed results at the 20K checkpoint; \\placeholder{30K three-seed confirmation pending}. Full-body SDF, the natural remedy for the structural mismatch identified here, remains untested. Fine-tuning degrades TSR by ${\\sim}$21\\textendash23\\,pp; strategies that preserve task capability alongside avoidance remain an open problem.",
          " ",
          " \\paragraph{Future work.}",
          "-Four directions follow from this analysis. First, full-body SDF monitoring along the robot kinematic chain would address the structural gap identified in Section~\\ref{sec:ee_only}. Second, evaluation across additional SafeLIBERO suites and other manipulation benchmarks would test whether the contamination patterns generalize beyond the task family studied here. Third, cross-architecture evaluation on non-Pi0-family VLAs (OpenVLA, RT-2) would determine the prevalence of fake safety in the broader VLA landscape. Fourth, we recommend that future VLA safety evaluations report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination in a given model.",
          "+Three directions follow from this analysis: (1) full-body SDF supervision along the kinematic chain, covering intermediate arm links and joints; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families to determine the prevalence of fake safety and metric contamination; (3) planning-layer safety constraints that operate in joint space rather than EE space, decoupling collision avoidance from the action prediction loss.",
          " ",
          " \\paragraph{Broader impact.}",
          "-Metric reliability is a prerequisite for safe deployment of autonomous manipulation systems. Contaminated evaluation metrics create a risk that models with no genuine collision avoidance capability pass safety benchmarks and proceed to deployment. Displacement filtering is a low-cost correction: it requires only end-effector position logging, no additional data collection or model modification. The analysis in this work is conducted entirely in simulation; real-world deployment introduces additional safety considerations (sensor noise, sim-to-real transfer, dynamic obstacles) that fall outside the present scope.",
          "+Contaminated CAR scores allow models with no genuine avoidance to pass safety benchmarks, creating false deployment readiness. CAR$_\\text{f}$ exposes this gap with minimal changes to existing evaluation protocols."
        ]
      }
    ],
    "originalFile": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nThis work identifies a systematic contamination in VLA collision avoidance evaluation: standard CAR conflates genuine obstacle avoidance with inaction caused by action collapse. Across all Pi0-family configurations evaluated on SafeLIBERO, over 98\\% of episodes classified as safe exhibit sub-threshold displacement, rendering raw CAR unreliable as a safety metric. Displacement-filtered CAR (CAR$_\\text{f}$) separates these two behaviors by excluding episodes below a displacement threshold $\\tau_d$, providing a metric that credits only active avoidance. Two structural findings reinforce this diagnosis: TSR and CAR are anti-correlated under current methods (Section~\\ref{sec:tsr_car}), and end-effector-only SDF refinement fails to prevent full-body collisions even with ground-truth geometry (Section~\\ref{sec:ee_only}). Training-time SDF supervision on Pi0.5 is the sole configuration that produces non-zero CAR$_\\text{f}$ with zero frozen rate, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\\ref{sec:a1_pi05}).\n\n\\paragraph{Limitations.}\nThe empirical scope of this study is bounded in several respects. All experiments use the \\texttt{object\\_pudding} Level~I suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. The EE-only SDF oracle (Section~\\ref{sec:ee_only}) tests end-effector-level refinement exclusively; full-body SDF monitoring along the kinematic chain may yield different outcomes. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across four orders of magnitude (Appendix~\\ref{app:threshold_sensitivity}), but remains task-dependent in principle. Pi0.5+A1 results are reported at the 10K-step checkpoint (seed~0); the 30K checkpoint is pending, and the final magnitude of the TSR-CAR tradeoff is not yet determined.\n\n\\paragraph{Future work.}\nFour directions follow from this analysis. First, full-body SDF monitoring along the robot kinematic chain would address the structural gap identified in Section~\\ref{sec:ee_only}. Second, evaluation across additional SafeLIBERO suites and other manipulation benchmarks would test whether the contamination patterns generalize beyond the task family studied here. Third, cross-architecture evaluation on non-Pi0-family VLAs (OpenVLA, RT-2) would determine the prevalence of fake safety in the broader VLA landscape. Fourth, we recommend that future VLA safety evaluations report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination in a given model.\n\n\\paragraph{Broader impact.}\nMetric reliability is a prerequisite for safe deployment of autonomous manipulation systems. Contaminated evaluation metrics create a risk that models with no genuine collision avoidance capability pass safety benchmarks and proceed to deployment. Displacement filtering is a low-cost correction: it requires only end-effector position logging, no additional data collection or model modification. The analysis in this work is conducted entirely in simulation; real-world deployment introduces additional safety considerations (sensor noise, sim-to-real transfer, dynamic obstacles) that fall outside the present scope.\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 44_

Now let me also update the `docs/paper/discussion.tex` to stay in sync.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "485077ab-424b-4589-bb02-8418cf0b1d54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhwFyZuW13F4491iL3VAdX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1735,
      "cache_read_input_tokens": 49185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1735
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

_source line 45_

<details open><summary>🔧 Tool call — Write · `toolu_01MyqHpsD3gLLMpbB2dPozeK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "content": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 90+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single conclusion: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (Pi0+A1 drops from 91.5\\% to ${\\approx}$\\,0\\% under displacement filtering); EE-only oracle refinement is counterproductive, \\emph{reducing} CAR below unrefined baselines; and collision-free demonstrations, not geometric supervision, account for all measured avoidance gains in fine-tuned models. We discuss the mechanistic basis for each finding and its implications.\n\n\\paragraph{Why EE-only SDF is redundant: a two-level account.}\nThe flat $\\lambda$-CAR curve ($\\lambda \\in [0.005, 0.1]$, 20$\\times$ range, all within the null band) rules out insufficient loss weight as the explanation and points to two independent structural causes.\n\n\\textit{(i) Demonstration data subsumes the SDF training signal.} Collision-free demonstrations shift the action distribution away from collision-prone trajectories by construction: every demonstration trajectory is safe, so imitating demonstrations implicitly encodes spatial avoidance. The ${\\sim}$28\\,pp CAR gain from LoRA fine-tuning (26.8\\% $\\to$ 54.5\\%) arises entirely from this distributional shift, with no SDF contribution. The per-task CAR ordering (chocolate\\_pudding highest, bbq\\_sauce lowest) is invariant across all SDF conditions and matches demonstration coverage, confirming that avoidance patterns originate from data statistics rather than geometric gradients. In this regime, EE-only SDF supplies a signal the model has already learned from imitation; adding a redundant gradient to a converged behavior produces no measurable effect. The Phase~2 ablation ($\\lambda = 0$ after step~5K, CAR = 57.5\\%) reinforces this interpretation: removing SDF supervision mid-training leaves avoidance unchanged, because the model never relied on it.\n\n\\textit{(ii) End-effector monitoring cannot prevent full-body collisions.} Even granting a perfect distance signal, the SDF gradient acts on a single point (the EE) while collisions predominantly occur along intermediate arm links and joints. In SafeLIBERO manipulation tasks, the robot must reach around obstacles, placing the forearm and wrist in close proximity to obstacle surfaces that the EE-only SDF does not monitor. Oracle experiments confirm this structural gap: ground-truth SDF refinement \\emph{reduces} CAR by 6\\textendash10\\,pp below unrefined baselines (73.1\\textendash76.9\\% vs.\\ 82\\textendash83\\%), because pushing the EE away from obstacles rotates unmonitored links through them. The action space compounds the mismatch: VLA policies output delta EE poses, so the SDF gradient operates in the same low-dimensional space as the action, with no mechanism to constrain the full joint configuration that realizes a given EE displacement.\n\nThese two levels are independent. Resolving (i) by finding a training signal beyond what demonstrations provide would not address (ii), and resolving (ii) through full-body monitoring would not change the fact that demonstrations already supply the avoidance signal. Effective geometric safety for VLA manipulation requires advances on both fronts: supervision that covers the full kinematic chain, and training signals that provide collision information beyond what is already implicit in collision-free demonstrations.\n\n\\paragraph{Implications for VLA safety evaluation.}\nCAR$_\\text{f}$ corrects action-collapse contamination using only end-effector position logging, already available in most evaluation pipelines. The bimodal displacement distribution (collapsed below 1\\,$\\mu$m, active above 200\\,mm) makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both raw CAR and CAR$_\\text{f}$; the gap quantifies action-collapse contamination. This contamination is not architecture-specific: Pi0 Full-FT (${\\sim}$2.5B trainable), Pi0 LoRA (${\\sim}$33.5M), and Pi0+A1 (${\\sim}$658K) all exhibit $>$99\\% fake safety despite a 4000$\\times$ parameter range. It is a necessary consequence of evaluating collision avoidance without verifying that the robot moved.\n\nMore broadly, our results suggest that safety in VLA manipulation may need to be addressed at the planning or constraint-satisfaction layer rather than through auxiliary losses on action prediction. When the action space is EE-centric, any loss defined over EE geometry inherits the same blind spot. Joint-space or full-body constraints, whether learned or imposed at planning time, offer a more natural interface for whole-arm collision avoidance.\n\n\\paragraph{Limitations.}\nOur evaluation covers one benchmark suite (SafeLIBERO object\\_pudding, four tasks) and two model families (Pi0, Pi0.5). Preliminary spatial\\_bowl results show different collision patterns, suggesting workspace geometry strongly affects collision modes; generalization to other tasks and architectures (OpenVLA, RT-2) is untested. Oracle experiments were conducted on a largely frozen model (Pi0+A1, TSR ${\\approx}$ 0\\%); testing on an actively moving policy would better isolate the EE-only structural limitation. The $\\lambda = 0.1$ condition reports 2-seed results at the 20K checkpoint; \\placeholder{30K three-seed confirmation pending}. Full-body SDF, the natural remedy for the structural mismatch identified here, remains untested. Fine-tuning degrades TSR by ${\\sim}$21\\textendash23\\,pp; strategies that preserve task capability alongside avoidance remain an open problem.\n\n\\paragraph{Future work.}\nThree directions follow from this analysis: (1) full-body SDF supervision along the kinematic chain, covering intermediate arm links and joints; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families to determine the prevalence of fake safety and metric contamination; (3) planning-layer safety constraints that operate in joint space rather than EE space, decoupling collision avoidance from the action prediction loss.\n\n\\paragraph{Broader impact.}\nContaminated CAR scores allow models with no genuine avoidance to pass safety benchmarks, creating false deployment readiness. CAR$_\\text{f}$ exposes this gap with minimal changes to existing evaluation protocols.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "e2784d5f-f1f8-4c78-a735-2324f9fde36f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhwFyZuW13F4491iL3VAdX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1735,
      "cache_read_input_tokens": 49185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1735
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

_source line 46 · 2026-05-27T08:31:18.210Z_

<details><summary>↩ Tool result · `toolu_01MyqHpsD3gLLMpbB2dPozeK`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "6f7b6439-2561-4c01-89a9-dd17efb87b2d",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "content": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 90+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single conclusion: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (Pi0+A1 drops from 91.5\\% to ${\\approx}$\\,0\\% under displacement filtering); EE-only oracle refinement is counterproductive, \\emph{reducing} CAR below unrefined baselines; and collision-free demonstrations, not geometric supervision, account for all measured avoidance gains in fine-tuned models. We discuss the mechanistic basis for each finding and its implications.\n\n\\paragraph{Why EE-only SDF is redundant: a two-level account.}\nThe flat $\\lambda$-CAR curve ($\\lambda \\in [0.005, 0.1]$, 20$\\times$ range, all within the null band) rules out insufficient loss weight as the explanation and points to two independent structural causes.\n\n\\textit{(i) Demonstration data subsumes the SDF training signal.} Collision-free demonstrations shift the action distribution away from collision-prone trajectories by construction: every demonstration trajectory is safe, so imitating demonstrations implicitly encodes spatial avoidance. The ${\\sim}$28\\,pp CAR gain from LoRA fine-tuning (26.8\\% $\\to$ 54.5\\%) arises entirely from this distributional shift, with no SDF contribution. The per-task CAR ordering (chocolate\\_pudding highest, bbq\\_sauce lowest) is invariant across all SDF conditions and matches demonstration coverage, confirming that avoidance patterns originate from data statistics rather than geometric gradients. In this regime, EE-only SDF supplies a signal the model has already learned from imitation; adding a redundant gradient to a converged behavior produces no measurable effect. The Phase~2 ablation ($\\lambda = 0$ after step~5K, CAR = 57.5\\%) reinforces this interpretation: removing SDF supervision mid-training leaves avoidance unchanged, because the model never relied on it.\n\n\\textit{(ii) End-effector monitoring cannot prevent full-body collisions.} Even granting a perfect distance signal, the SDF gradient acts on a single point (the EE) while collisions predominantly occur along intermediate arm links and joints. In SafeLIBERO manipulation tasks, the robot must reach around obstacles, placing the forearm and wrist in close proximity to obstacle surfaces that the EE-only SDF does not monitor. Oracle experiments confirm this structural gap: ground-truth SDF refinement \\emph{reduces} CAR by 6\\textendash10\\,pp below unrefined baselines (73.1\\textendash76.9\\% vs.\\ 82\\textendash83\\%), because pushing the EE away from obstacles rotates unmonitored links through them. The action space compounds the mismatch: VLA policies output delta EE poses, so the SDF gradient operates in the same low-dimensional space as the action, with no mechanism to constrain the full joint configuration that realizes a given EE displacement.\n\nThese two levels are independent. Resolving (i) by finding a training signal beyond what demonstrations provide would not address (ii), and resolving (ii) through full-body monitoring would not change the fact that demonstrations already supply the avoidance signal. Effective geometric safety for VLA manipulation requires advances on both fronts: supervision that covers the full kinematic chain, and training signals that provide collision information beyond what is already implicit in collision-free demonstrations.\n\n\\paragraph{Implications for VLA safety evaluation.}\nCAR$_\\text{f}$ corrects action-collapse contamination using only end-effector position logging, already available in most evaluation pipelines. The bimodal displacement distribution (collapsed below 1\\,$\\mu$m, active above 200\\,mm) makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both raw CAR and CAR$_\\text{f}$; the gap quantifies action-collapse contamination. This contamination is not architecture-specific: Pi0 Full-FT (${\\sim}$2.5B trainable), Pi0 LoRA (${\\sim}$33.5M), and Pi0+A1 (${\\sim}$658K) all exhibit $>$99\\% fake safety despite a 4000$\\times$ parameter range. It is a necessary consequence of evaluating collision avoidance without verifying that the robot moved.\n\nMore broadly, our results suggest that safety in VLA manipulation may need to be addressed at the planning or constraint-satisfaction layer rather than through auxiliary losses on action prediction. When the action space is EE-centric, any loss defined over EE geometry inherits the same blind spot. Joint-space or full-body constraints, whether learned or imposed at planning time, offer a more natural interface for whole-arm collision avoidance.\n\n\\paragraph{Limitations.}\nOur evaluation covers one benchmark suite (SafeLIBERO object\\_pudding, four tasks) and two model families (Pi0, Pi0.5). Preliminary spatial\\_bowl results show different collision patterns, suggesting workspace geometry strongly affects collision modes; generalization to other tasks and architectures (OpenVLA, RT-2) is untested. Oracle experiments were conducted on a largely frozen model (Pi0+A1, TSR ${\\approx}$ 0\\%); testing on an actively moving policy would better isolate the EE-only structural limitation. The $\\lambda = 0.1$ condition reports 2-seed results at the 20K checkpoint; \\placeholder{30K three-seed confirmation pending}. Full-body SDF, the natural remedy for the structural mismatch identified here, remains untested. Fine-tuning degrades TSR by ${\\sim}$21\\textendash23\\,pp; strategies that preserve task capability alongside avoidance remain an open problem.\n\n\\paragraph{Future work.}\nThree directions follow from this analysis: (1) full-body SDF supervision along the kinematic chain, covering intermediate arm links and joints; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families to determine the prevalence of fake safety and metric contamination; (3) planning-layer safety constraints that operate in joint space rather than EE space, decoupling collision avoidance from the action prediction loss.\n\n\\paragraph{Broader impact.}\nContaminated CAR scores allow models with no genuine avoidance to pass safety benchmarks, creating false deployment readiness. CAR$_\\text{f}$ exposes this gap with minimal changes to existing evaluation protocols.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 20,
        "newStart": 1,
        "newLines": 26,
        "lines": [
          " \\section{Discussion and Conclusion}\\label{sec:conclusion}",
          " ",
          "-Across 70+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single conclusion: the robot is frozen, not safe. Action collapse renders reported CAR illusory (Pi0+A1 drops from 91.5\\% to ${\\approx}$\\,0\\% under displacement filtering); EE-only oracle refinement is counterproductive, \\emph{reducing} CAR below unrefined baselines; and collision-free demonstrations, not EE-only SDF supervision, account for all measured avoidance gains in fine-tuned models.",
          "+Across 90+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single conclusion: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (Pi0+A1 drops from 91.5\\% to ${\\approx}$\\,0\\% under displacement filtering); EE-only oracle refinement is counterproductive, \\emph{reducing} CAR below unrefined baselines; and collision-free demonstrations, not geometric supervision, account for all measured avoidance gains in fine-tuned models. We discuss the mechanistic basis for each finding and its implications.",
          " ",
          "-\\paragraph{Implications for VLA safety evaluation.}",
          "-CAR$_\\text{f}$ corrects action-collapse contamination using only end-effector position logging, already available in most evaluation pipelines. The bimodal displacement distribution (collapsed below 1\\,$\\mu$m, active above 200\\,mm) makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both raw CAR and CAR$_\\text{f}$; the gap quantifies action-collapse contamination. The contamination is not specific to any model architecture or training procedure: Pi0 Full-FT (${\\sim}$2.5B trainable), Pi0 LoRA (${\\sim}$33.5M), and Pi0+A1 (${\\sim}$658K) all exhibit $>$99\\% fake safety despite a 4000$\\times$ parameter range. It is a necessary consequence of evaluating collision avoidance without motion verification; episode-level filtering detects partial collapse invisible to model-level TSR checks.",
          "+\\paragraph{Why EE-only SDF is redundant: a two-level account.}",
          "+The flat $\\lambda$-CAR curve ($\\lambda \\in [0.005, 0.1]$, 20$\\times$ range, all within the null band) rules out insufficient loss weight as the explanation and points to two independent structural causes.",
          " ",
          "-\\paragraph{Two-level failure of EE-only geometric supervision.}",
          "-Our negative results identify two independent failure modes. \\textit{Level~A: training signal masking.} At $\\lambda \\leq 0.01$, the SDF gradient is negligible relative to the action loss. The collision-free demonstration distribution already encodes spatial avoidance patterns: the ${\\sim}$28\\,pp CAR gain over the Pi0.5 baseline is entirely attributable to demonstration imitation. A Phase~2 ablation ($\\lambda = 0$ after step 5K) confirms no persistent SDF encoding in the learned representation. \\textit{Level~B: representation-collision misalignment.} Even with ground-truth SDF, EE-only supervision monitors a single point while collisions occur along the full kinematic chain. Oracle refinement pushes the EE away from obstacles while arm links sweep through them, producing lower CAR than unrefined baselines (73.1--76.9\\% vs.\\ 82--83\\%). These two levels are independent: resolving signal masking (e.g., higher $\\lambda$) would not address geometric misalignment, and vice versa. At $\\lambda = 0.1$ (20$\\times$ higher dose), CAR remains within the null range (55.5\\%), confirming that Level~A signal masking is not the binding constraint. The failure is architectural: EE-only supervision cannot prevent arm-body collisions regardless of loss weight. Future geometric safety methods for manipulation must therefore (a) supervise the full kinematic chain rather than the end-effector alone, and (b) provide training signals that exceed the avoidance information already present in the demonstration distribution.",
          "+\\textit{(i) Demonstration data subsumes the SDF training signal.} Collision-free demonstrations shift the action distribution away from collision-prone trajectories by construction: every demonstration trajectory is safe, so imitating demonstrations implicitly encodes spatial avoidance. The ${\\sim}$28\\,pp CAR gain from LoRA fine-tuning (26.8\\% $\\to$ 54.5\\%) arises entirely from this distributional shift, with no SDF contribution. The per-task CAR ordering (chocolate\\_pudding highest, bbq\\_sauce lowest) is invariant across all SDF conditions and matches demonstration coverage, confirming that avoidance patterns originate from data statistics rather than geometric gradients. In this regime, EE-only SDF supplies a signal the model has already learned from imitation; adding a redundant gradient to a converged behavior produces no measurable effect. The Phase~2 ablation ($\\lambda = 0$ after step~5K, CAR = 57.5\\%) reinforces this interpretation: removing SDF supervision mid-training leaves avoidance unchanged, because the model never relied on it.",
          " ",
          "-\\paragraph{Why EE-only SDF adds no value.}",
          "-Three observations explain the redundancy. First, VLA pre-trained representations already encode spatial structure: Pi0.5 achieves 26.8\\% CAR without any safety-specific training, indicating implicit obstacle awareness in the visual-motor prior. Second, collision-free demonstrations amplify this prior by shifting the action distribution away from collision-prone trajectories, yielding the full ${\\sim}$28\\,pp CAR gain; the same distributional shift degrades TSR by ${\\sim}$21--23\\,pp, and EE-only SDF regularization cannot selectively reverse one effect without the other. Third, the Phase~2 ablation ($\\lambda = 0$ after step 5K, CAR\\,=\\,57.5\\%) confirms that SDF gradients produce no persistent encoding---the model's avoidance is identical whether SDF supervision is present, removed, or never applied, because the demonstration distribution fully determines the spatial avoidance pattern.",
          "+\\textit{(ii) End-effector monitoring cannot prevent full-body collisions.} Even granting a perfect distance signal, the SDF gradient acts on a single point (the EE) while collisions predominantly occur along intermediate arm links and joints. In SafeLIBERO manipulation tasks, the robot must reach around obstacles, placing the forearm and wrist in close proximity to obstacle surfaces that the EE-only SDF does not monitor. Oracle experiments confirm this structural gap: ground-truth SDF refinement \\emph{reduces} CAR by 6\\textendash10\\,pp below unrefined baselines (73.1\\textendash76.9\\% vs.\\ 82\\textendash83\\%), because pushing the EE away from obstacles rotates unmonitored links through them. The action space compounds the mismatch: VLA policies output delta EE poses, so the SDF gradient operates in the same low-dimensional space as the action, with no mechanism to constrain the full joint configuration that realizes a given EE displacement.",
          " ",
          "+These two levels are independent. Resolving (i) by finding a training signal beyond what demonstrations provide would not address (ii), and resolving (ii) through full-body monitoring would not change the fact that demonstrations already supply the avoidance signal. Effective geometric safety for VLA manipulation requires advances on both fronts: supervision that covers the full kinematic chain, and training signals that provide collision information beyond what is already implicit in collision-free demonstrations.",
          "+",
          "+\\paragraph{Implications for VLA safety evaluation.}",
          "+CAR$_\\text{f}$ corrects action-collapse contamination using only end-effector position logging, already available in most evaluation pipelines. The bimodal displacement distribution (collapsed below 1\\,$\\mu$m, active above 200\\,mm) makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both raw CAR and CAR$_\\text{f}$; the gap quantifies action-collapse contamination. This contamination is not architecture-specific: Pi0 Full-FT (${\\sim}$2.5B trainable), Pi0 LoRA (${\\sim}$33.5M), and Pi0+A1 (${\\sim}$658K) all exhibit $>$99\\% fake safety despite a 4000$\\times$ parameter range. It is a necessary consequence of evaluating collision avoidance without verifying that the robot moved.",
          "+",
          "+More broadly, our results suggest that safety in VLA manipulation may need to be addressed at the planning or constraint-satisfaction layer rather than through auxiliary losses on action prediction. When the action space is EE-centric, any loss defined over EE geometry inherits the same blind spot. Joint-space or full-body constraints, whether learned or imposed at planning time, offer a more natural interface for whole-arm collision avoidance.",
          "+",
          " \\paragraph{Limitations.}",
          "-Our evaluation covers one benchmark suite (SafeLIBERO object\\_pudding, four tasks) and two model families. Preliminary spatial\\_bowl results show different patterns (Pi0 Full-FT: 0\\% CAR despite 0.29\\,m displacement; Pi0+A1: 0.8\\% raw CAR with all safe episodes frozen, dfCAR${\\approx}$0\\%; Pi0.5: 13\\% CAR), suggesting workspace geometry strongly affects collision modes. Generalization to OpenVLA, RT-2, or other architectures is untested. Oracle experiments were conducted on a largely frozen model (Pi0+A1, TSR${\\approx}$0\\%); testing on an actively moving policy (e.g., Pi0.5+LoRA, TSR${\\approx}$51.5\\%) would better isolate the EE-only structural limitation. The bimodal displacement gap may narrow on tasks with slower motions, making $\\tau_d$ selection more consequential. Fine-tuning degrades TSR by ${\\sim}$21--23\\,pp; strategies that preserve task capability alongside avoidance remain unexplored.",
          "+Our evaluation covers one benchmark suite (SafeLIBERO object\\_pudding, four tasks) and two model families (Pi0, Pi0.5). Preliminary spatial\\_bowl results show different collision patterns, suggesting workspace geometry strongly affects collision modes; generalization to other tasks and architectures (OpenVLA, RT-2) is untested. Oracle experiments were conducted on a largely frozen model (Pi0+A1, TSR ${\\approx}$ 0\\%); testing on an actively moving policy would better isolate the EE-only structural limitation. The $\\lambda = 0.1$ condition reports 2-seed results at the 20K checkpoint; \\placeholder{30K three-seed confirmation pending}. Full-body SDF, the natural remedy for the structural mismatch identified here, remains untested. Fine-tuning degrades TSR by ${\\sim}$21\\textendash23\\,pp; strategies that preserve task capability alongside avoidance remain an open problem.",
          "+",
          " \\paragraph{Future work.}",
          "-Three directions follow: (1) full-body SDF along the kinematic chain, covering intermediate arm links; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) multi-benchmark evaluation to characterize how task geometry affects displacement distributions and threshold robustness.",
          "+Three directions follow from this analysis: (1) full-body SDF supervision along the kinematic chain, covering intermediate arm links and joints; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families to determine the prevalence of fake safety and metric contamination; (3) planning-layer safety constraints that operate in joint space rather than EE space, decoupling collision avoidance from the action prediction loss.",
          " ",
          " \\paragraph{Broader impact.}",
          "-Contaminated CAR scores allow models with no real avoidance to pass safety benchmarks, creating false deployment readiness. CAR$_\\text{f}$ exposes this gap with minimal changes to existing evaluation protocols.",
          "\\ No newline at end of file",
          "+Contaminated CAR scores allow models with no genuine avoidance to pass safety benchmarks, creating false deployment readiness. CAR$_\\text{f}$ exposes this gap with minimal changes to existing evaluation protocols."
        ]
      }
    ],
    "originalFile": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 70+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single conclusion: the robot is frozen, not safe. Action collapse renders reported CAR illusory (Pi0+A1 drops from 91.5\\% to ${\\approx}$\\,0\\% under displacement filtering); EE-only oracle refinement is counterproductive, \\emph{reducing} CAR below unrefined baselines; and collision-free demonstrations, not EE-only SDF supervision, account for all measured avoidance gains in fine-tuned models.\n\n\\paragraph{Implications for VLA safety evaluation.}\nCAR$_\\text{f}$ corrects action-collapse contamination using only end-effector position logging, already available in most evaluation pipelines. The bimodal displacement distribution (collapsed below 1\\,$\\mu$m, active above 200\\,mm) makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both raw CAR and CAR$_\\text{f}$; the gap quantifies action-collapse contamination. The contamination is not specific to any model architecture or training procedure: Pi0 Full-FT (${\\sim}$2.5B trainable), Pi0 LoRA (${\\sim}$33.5M), and Pi0+A1 (${\\sim}$658K) all exhibit $>$99\\% fake safety despite a 4000$\\times$ parameter range. It is a necessary consequence of evaluating collision avoidance without motion verification; episode-level filtering detects partial collapse invisible to model-level TSR checks.\n\n\\paragraph{Two-level failure of EE-only geometric supervision.}\nOur negative results identify two independent failure modes. \\textit{Level~A: training signal masking.} At $\\lambda \\leq 0.01$, the SDF gradient is negligible relative to the action loss. The collision-free demonstration distribution already encodes spatial avoidance patterns: the ${\\sim}$28\\,pp CAR gain over the Pi0.5 baseline is entirely attributable to demonstration imitation. A Phase~2 ablation ($\\lambda = 0$ after step 5K) confirms no persistent SDF encoding in the learned representation. \\textit{Level~B: representation-collision misalignment.} Even with ground-truth SDF, EE-only supervision monitors a single point while collisions occur along the full kinematic chain. Oracle refinement pushes the EE away from obstacles while arm links sweep through them, producing lower CAR than unrefined baselines (73.1--76.9\\% vs.\\ 82--83\\%). These two levels are independent: resolving signal masking (e.g., higher $\\lambda$) would not address geometric misalignment, and vice versa. At $\\lambda = 0.1$ (20$\\times$ higher dose), CAR remains within the null range (55.5\\%), confirming that Level~A signal masking is not the binding constraint. The failure is architectural: EE-only supervision cannot prevent arm-body collisions regardless of loss weight. Future geometric safety methods for manipulation must therefore (a) supervise the full kinematic chain rather than the end-effector alone, and (b) provide training signals that exceed the avoidance information already present in the demonstration distribution.\n\n\\paragraph{Why EE-only SDF adds no value.}\nThree observations explain the redundancy. First, VLA pre-trained representations already encode spatial structure: Pi0.5 achieves 26.8\\% CAR without any safety-specific training, indicating implicit obstacle awareness in the visual-motor prior. Second, collision-free demonstrations amplify this prior by shifting the action distribution away from collision-prone trajectories, yielding the full ${\\sim}$28\\,pp CAR gain; the same distributional shift degrades TSR by ${\\sim}$21--23\\,pp, and EE-only SDF regularization cannot selectively reverse one effect without the other. Third, the Phase~2 ablation ($\\lambda = 0$ after step 5K, CAR\\,=\\,57.5\\%) confirms that SDF gradients produce no persistent encoding---the model's avoidance is identical whether SDF supervision is present, removed, or never applied, because the demonstration distribution fully determines the spatial avoidance pattern.\n\n\\paragraph{Limitations.}\nOur evaluation covers one benchmark suite (SafeLIBERO object\\_pudding, four tasks) and two model families. Preliminary spatial\\_bowl results show different patterns (Pi0 Full-FT: 0\\% CAR despite 0.29\\,m displacement; Pi0+A1: 0.8\\% raw CAR with all safe episodes frozen, dfCAR${\\approx}$0\\%; Pi0.5: 13\\% CAR), suggesting workspace geometry strongly affects collision modes. Generalization to OpenVLA, RT-2, or other architectures is untested. Oracle experiments were conducted on a largely frozen model (Pi0+A1, TSR${\\approx}$0\\%); testing on an actively moving policy (e.g., Pi0.5+LoRA, TSR${\\approx}$51.5\\%) would better isolate the EE-only structural limitation. The bimodal displacement gap may narrow on tasks with slower motions, making $\\tau_d$ selection more consequential. Fine-tuning degrades TSR by ${\\sim}$21--23\\,pp; strategies that preserve task capability alongside avoidance remain unexplored.\n\\paragraph{Future work.}\nThree directions follow: (1) full-body SDF along the kinematic chain, covering intermediate arm links; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) multi-benchmark evaluation to characterize how task geometry affects displacement distributions and threshold robustness.\n\n\\paragraph{Broader impact.}\nContaminated CAR scores allow models with no real avoidance to pass safety benchmarks, creating false deployment readiness. CAR$_\\text{f}$ exposes this gap with minimal changes to existing evaluation protocols.",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 47_

两个文件已同步更新。主要改动：

**结构重组**：将原来分散在三个 paragraph（"Two-level failure" + "Why EE-only SDF adds no value" + "Implications"）的机理分析合并为一个核心 paragraph "Why EE-only SDF is redundant: a two-level account"，逻辑更紧凑。

**机理分析强化**：
- **(i) Demo data subsumption**：明确阐述 collision-free demo → distributional shift → implicit avoidance encoding 的因果链，用 per-task CAR fingerprint 不变性和 Phase 2 ablation 作为双重证据
- **(ii) EE-body mismatch**：新增 action space 维度的论证（VLA output delta EE pose, SDF gradient 操作在同一低维空间，无法约束 full joint configuration），补充了 oracle 实验的机理解释（push EE away → rotate unmonitored links through obstacle）
- 两个 level 的**独立性**明确阐述，说明需要同时解决两个问题

**新增内容**：
- Implications 段新增 planning-layer vs action-prediction-layer 的讨论
- Future work 新增 joint-space planning constraints 方向
- Limitations 段加入 `\placeholder` 标记 λ=0.1 30K pending

**写作规范**：无 em-dash，无 `-ing` 结尾句，无 AI 味用词，数值范围用 `\textendash`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "uuid": "9439ee43-8345-4417-ac0f-282e7a98a279",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tg7e9CNw7StSbPCxnzErK3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1807,
      "cache_read_input_tokens": 50920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1807
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

_source line 48_

两个文件已同步更新。主要改动：

**结构重组**：将原来分散在三个 paragraph（"Two-level failure" + "Why EE-only SDF adds no value" + "Implications"）的机理分析合并为一个核心 paragraph "Why EE-only SDF is redundant: a two-level account"，逻辑更紧凑。

**机理分析强化**：
- **(i) Demo data subsumption**：明确阐述 collision-free demo → distributional shift → implicit avoidance encoding 的因果链，用 per-task CAR fingerprint 不变性和 Phase 2 ablation 作为双重证据
- **(ii) EE-body mismatch**：新增 action space 维度的论证（VLA output delta EE pose, SDF gradient 操作在同一低维空间，无法约束 full joint configuration），补充了 oracle 实验的机理解释（push EE away → rotate unmonitored links through obstacle）
- 两个 level 的**独立性**明确阐述，说明需要同时解决两个问题

**新增内容**：
- Implications 段新增 planning-layer vs action-prediction-layer 的讨论
- Future work 新增 joint-space planning constraints 方向
- Limitations 段加入 `\placeholder` 标记 λ=0.1 30K pending

**写作规范**：无 em-dash，无 `-ing` 结尾句，无 AI 味用词，数值范围用 `\textendash`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 192285,
  "duration_api_ms": 193377,
  "num_turns": 15,
  "stop_reason": "end_turn",
  "session_id": "225fa56a-b7dd-493e-a4f7-b091d81c926e",
  "total_cost_usd": 0.675208,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 40882,
    "cache_read_input_tokens": 365831,
    "output_tokens": 9392,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 40882,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 420,
        "cache_read_input_tokens": 50920,
        "cache_creation_input_tokens": 1807,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1807
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1825,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00191,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 14,
      "outputTokens": 9392,
      "cacheReadInputTokens": 365831,
      "cacheCreationInputTokens": 40882,
      "webSearchRequests": 0,
      "costUSD": 0.673298,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c5ae44c2-dd10-4883-bf00-b181d5cf94a6"
}
```

</details>

---
