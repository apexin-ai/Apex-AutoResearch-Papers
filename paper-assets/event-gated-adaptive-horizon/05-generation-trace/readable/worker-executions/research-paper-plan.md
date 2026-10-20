# research paper plan

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/workers/worker_research_paper-plan_20260515T011527.log`
- **Structured JSON:** [`107d510862be1c637741.json`](../../sessions/10/107d510862be1c637741.json)

## Before a recorded user message

56 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon",
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__update_registry"
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
  "uuid": "07a68c2e-1ee7-4c1d-9590-9c2dca73d53f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1778823600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "18bdce03-0924-4ae6-8f01-e7fb874bf08b",
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the necessary project files to understand the current state of the project before creating the writing plan.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "b166bc32-629f-426b-a134-c5da83c6fa84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rw2NT8RAijgNSoG49Ss3k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11618,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11618
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

_source line 5_

I'll read the project files needed to create the writing plan.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "c64f7b0f-74ea-4911-accb-675cb9250e32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rw2NT8RAijgNSoG49Ss3k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11618,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11618
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0135BZ64qP4oRcbSK4izF9uc`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_registry",
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
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "fb38c970-c2e4-4633-a7e7-a625247def66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rw2NT8RAijgNSoG49Ss3k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11618,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11618
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

_source line 7 · 2026-05-15T01:15:39.128Z_

<details><summary>↩ Tool result · `toolu_0135BZ64qP4oRcbSK4izF9uc`</summary>

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
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "a6ef5131-c00d-4f0a-b0d9-a25017342495",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the project files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "02969507-001c-4f6c-a78b-aaff0b0e1dd7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016uBuyZh4rKiMrjGMj1ej6K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 23459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1097
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

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KV6UPpsSh2mZXEMXwt9e8U`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
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
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "e94111c9-fb50-4996-873a-c86129d2a792",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016uBuyZh4rKiMrjGMj1ej6K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 23459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1097
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

_source line 10 · 2026-05-15T01:15:44.282Z_

<details><summary>↩ Tool result · `toolu_01KV6UPpsSh2mZXEMXwt9e8U`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md\", \"content\": \"# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\\n\\n## Title Candidates\\n\\n1. **\\\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\\\"**\\n2. **\\\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\\\"**\\n3. **\\\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\\\"**\\n\\n## Venue\\n\\n**CoRL 2026** — Deadline: 2026-05-29\\n\\n## Narrative Positioning\\n\\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\\n\\nThe contribution is a **closed causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.\\n\\nWe scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.\\n\\n---\\n\\n## Core Claims\\n\\n### C1: Variable-rate imagination in DreamerV3 consistently degrades performance\\n\\nTemporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |\\n| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |\\n| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\n| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |\\n\\n**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.\\n\\n### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk\\n\\n**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**\\n\\nThe trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:\\n\\n- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)\\n- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)\\n- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb\\n\\n**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。\\n\\n**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a \\\"point of no return\\\" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).\\n\\nThe trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is systematic value overestimation (delusional critic) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |\\n| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |\\n| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |\\n| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |\\n| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |\\n| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |\\n| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |\\n| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |\\n\\n**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 \\\"eliminates\\\" 改为 \\\"significantly delays and reduces\\\"。推荐方案仍是 008e_v3（C6）**。\\n\\n**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**\\n\\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\\n|-------|------------|------------|---------|---------------|---------------|------------|\\n| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |\\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |\\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |\\n\\n**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\\n\\n**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.\\n\\n### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance\\n\\nWhen dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |\\n| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |\\n| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |\\n| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |\\n| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |\\n\\n**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the delusional critic feedback loop in trained variants.\\n\\n**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).\\n\\n**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.\\n\\n### C4: Longer dt amplifies the problem\\n\\nIncreasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |\\n| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\n| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |\\n\\n**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.\\n\\n### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause\\n\\nSubsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |\\n| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |\\n| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |\\n| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |\\n| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |\\n\\n**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.\\n\\n### C6: Restricting imagination to dt=1 during multi-dt training provides practical mitigation\\n\\nWhen training with multi-dt data (subsample ON, dt∈{1,2}) while restricting imagination rollouts to dt=1, performance recovers to 95% of the dt=1 baseline. This provides a concrete, zero-cost mitigation guideline: keep imagination at dt=1 even if the world model learns multi-dt dynamics.\\n\\n**008f reward 退化发现进一步强化 C6 的价值**：008f（去掉 dt_embedding）虽避免崩塌但 reward 预测退化 75x；而 008e_v3（保留 trained dt_emb + dt=1 imagination）达到 95% baseline 且 reward prediction 不受影响。008e_v3 是唯一同时避免崩塌且保持完整预测能力的配置。**关键洞察：008d（trained dt_emb + dt>1 imag）collapse vs 008e_v3（trained dt_emb + dt=1 imag）healthy，证明 critical variable 是 imagination dt，不是 embedding 训练状态。不需要改动模型架构，只需改 imagination 策略。**\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| dt=1 imagination + multi-dt training | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval_return_105K=869.9 (95% of baseline 915.67), normalized v/e=0.80x |\\n| Comparison: dt=2 imagination collapses | exp_006 (subsample ON, trained dt_emb, dt=2 imag, H=15) | Peak 485@35K → collapse. v/e 2.3x baseline@55K |\\n| Comparison: untrained dt_emb + dt=2 degrades | exp_008a (subsample OFF, untrained dt_emb, dt=2 imag, H=15) | 778@105K (85% baseline). Better than collapse but 10pp below mitigation |\\n| Comparison: no dt_emb avoids collapse but degrades reward | exp_008f (dt_embed_dim=0, subsample ON, H=8) | No collapse, but reward_MAE=0.747 (75x baseline). Avoidance of collapse comes at cost of reward prediction |\\n\\n**Strength**: Moderate-strong → **strengthened by 008f contrast**. 008e_v3 is the only configuration that (a) avoids delusional critic collapse, (b) maintains healthy reward prediction, AND (c) achieves near-baseline performance (95%). Single seed, single environment; multi-seed + cross-environment planned (P0). Actionable: practitioners using variable-dt training data should restrict imagination to dt=1 until RSSM fidelity at dt>1 improves.\\n\\n---\\n\\n## Story Arc\\n\\n### 1. Introduction\\n- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)\\n- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction\\n- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?\\n- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for pathological value overestimation (nve>1.5x, 4/4 separating power), with collapse as a stochastic consequence, plus a practical mitigation guideline (dt=1 imagination → 95% baseline)\\n\\n### 2. Background & Related Work\\n- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)\\n- World-model RL (Dreamer family, IRIS, TWM)\\n- Variable-rate planning in world models (few prior works, mostly positive framing)\\n- Value overestimation / delusional policies in model-based RL\\n\\n### 3. Methodology\\n- DreamerV3 as base architecture\\n- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating\\n- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines\\n- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves\\n\\n### 4. Results\\n- **Finding 1**: All dt>1 configurations degrade (C1)\\n- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the \\\"smoking gun\\\" comparison (008c vs 008d)\\n- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)\\n- **Finding 4**: Longer dt amplifies (C4)\\n- **Finding 5**: Horizon/subsample effects are secondary (C5)\\n- **Finding 6**: Restricting imagination to dt=1 during multi-dt training recovers 95% baseline — practical mitigation (C6)\\n\\n### 5. Discussion\\n- Mechanism: why trained dt_embedding causes delusional critic (RSSM fidelity gap at dt>1)\\n- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x) — trained dt_emb 让 reward head 在 dt=2 时产生系统性偏差，这是 critic 被误导的直接来源\\n- 008f 的 reward 退化 trade-off：去掉 dt_embedding 避免崩塌但牺牲 reward 预测质量；008e_v3 是更优方案\\n- Connection to existing theory: non-delusional Q-learning (Lu et al., 2018), model exploitation in MBRL\\n- Why this is specific to world-model RL (model-free temporal abstraction doesn't suffer the same failure mode)\\n- **D032: Value self-correction mechanism (009b)**: 009b (008d seed 2) demonstrates that pathological overestimation (nve>1.5x) is not always irreversible. Value peaked at 110.9@65K then monotonically self-corrected to 67.3@105K, while eval simultaneously improved (172→268). Hypothesized mechanism: when the critic's overestimation does not yet dominate the actor's gradient signal (transient vs sustained nve>1.5x), the actor can still learn from real environment returns, creating a corrective force. In 008d seed 1, the sustained overestimation (3 consecutive checkpoints >1.5x at 35K+) overwhelmed this correction. The bifurcation likely depends on early training stochasticity — initialization and data sampling order determine whether the overestimation feedback loop locks in before correction can take hold (consistent with primacy bias in MBRL, Qiao et al. 2023; early outlier runs, Bjorck et al. 2022). This makes nve>1.5x a **necessary condition** for collapse but not sufficient — the temporal persistence of overestimation is the second gate.\\n\\n### 6. Implications for Future Work\\n- Don't use dt>1 imagination with trained dt_embedding in current world-model architectures (trained dt_emb is safe if imagination stays at dt=1)\\n- RSSM prediction quality must improve before variable-rate imagination is viable\\n- Imagination-side restriction (dt=1 imagination with multi-dt training) as the practical mitigation — no architecture change needed\\n- Need for diagnostic methodology in temporal abstraction research\\n\\n---\\n\\n## Anticipated Reviewer Concerns\\n\\n### R1: \\\"Limited to one environment / one base algorithm\\\"\\n**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.\\n**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.\\n\\n### R2: \\\"No proposed solution — what's the actionable takeaway?\\\"\\n**Pre-emption**: Beyond diagnosis, we provide a **concrete mitigation guideline**: train with multi-dt data but restrict imagination rollouts to dt=1. exp_008e_v3 demonstrates this recovers 95% of baseline performance (869.9 vs 915.67) with normalized v/e=0.80x (healthy). This is zero-cost to implement and directly actionable.\\n**Mitigation**: Present 008e_v3 as a practical recommendation in Section 6. Additionally, we outline an uncertainty-gated imagination truncation direction as future work.\\n\\n### R3: \\\"Value/eval ratio is a crude proxy for overestimation\\\"\\n**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.\\n**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.\\n\\n### R4: \\\"The factorial design is incomplete — missing cells in the grid\\\"\\n**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.\\n**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.\\n\\n### R5: \\\"Novelty concern — model exploitation / value overestimation in MBRL is well-known\\\"\\n**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.\\n\\n### R6: \\\"All results from a single seed — how robust are the conclusions?\\\"\\n**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.\\n**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.\\n\\n### R7: \\\"The factorial design confounds dt_embedding training with training data composition\\\"\\n**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).\\n**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for delusional critic.\\n\\n### R8: \\\"008f reward prediction degradation undermines the causal control\\\"\\n**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是\\\"去掉 dt_embedding → 不崩塌\\\"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。\\n**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（推荐方案）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。\\n\\n---\\n\\n## Experiment Coverage Assessment\\n\\n| Claim | Evidence Status | Gaps |\\n|-------|----------------|------|\\n| C1 (degradation) | ✅ Strong — 3 configurations (005, 006, 007) all negative | Could add 1 more environment |\\n| C2 (reliable pathological overestimation) | ⚠️ Moderate-strong (D032) — nve>1.5x threshold: 4/4 perfect separation (trained 2/2 exceed, untrained 0/2 exceed). Collapse stochastic: 1/2 trained seeds. Causal direction unambiguous. | 009e (008d seed 1) to narrow collapse probability; 009f (008f seed 1) for third untrained seed; 009c→200K |\\n| C3 (preventing optimistic drift) | ✅ Strong (105K confirmed) — 008a@105K=778 (85% baseline), normalized v/e=0.59x, two V-shaped recoveries | None — long-term structural suppression confirmed |\\n| C4 (dt amplification) | ⚠️ Moderate — only dt=2 vs dt=4 | Would benefit from dt=3, but not blocking |\\n| C5 (horizon/subsample) | ⚠️ Moderate — confounded with other factors | Need 008c-equivalent with H=15 + subsample ON + untrained dt_emb for clean isolation |\\n| C6 (mitigation) | ✅ Moderate-strong — 008e_v3@105K=869.9 (95% baseline), normalized v/e=0.80x | Single seed, single environment. Multi-seed + Cheetah Run planned |\\n\\n### Priority Actions Before Submission\\n1. ~~**Check exp_008a@65K**~~ — ✅ Done: 608 (-1.3% baseline), B+ confirmed\\n2. ~~**008e_v3 B+ confound**~~ — ✅ Done: 869.9@105K (95% baseline), B+ confirmed\\n3. ~~**008f C2 causal control**~~ — ✅ Done: V-recovery to 503@105K, normalized v/e=0.30x\\n4. **Multi-seed replication** — Walker Walk seeds 1-2 for baseline/008d/008f (running + queued)\\n5. **Cheetah Run cross-environment** — P0 priority, addresses R1\\n6. **Cartpole Swingup** — P0, non-locomotion environment broadens scope (升级)\\n7. **Figures** — learning curves, normalized v/e, value scatter, RSSM fidelity table (in progress, 0 GPU cost)\\n8. **Mitigation pilot** — uncertainty-gated imagination truncation (P0, addresses R2 actionability)\\n\\n---\\n\\n## Key Figures (Planned)\\n\\n1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)\\n2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes\\n3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis\\n4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse\\n5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)\\n6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）\\n7. **Figure 6 (D032)**: nve trajectory overlay — 008d seed 1 (sustained >1.5x → collapse) vs 009b seed 2 (transient >1.5x → self-correction), with 1.5x threshold line marked. Also overlay 008f seeds (both below 1.5x) for contrast.\\n\", \"total_chars\": 26876, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "7dd73cdd-ee96-44d1-a296-9b7288410f16",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\\\\n\\\\n## Title Candidates\\\\n\\\\n1. **\\\\\\\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\\\\\\\"**\\\\n2. **\\\\\\\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\\\\\\\"**\\\\n3. **\\\\\\\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\\\\\\\"**\\\\n\\\\n## Venue\\\\n\\\\n**CoRL 2026** — Deadline: 2026-05-29\\\\n\\\\n## Narrative Positioning\\\\n\\\\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\\\\n\\\\nThe contribution is a **closed causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.\\\\n\\\\nWe scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.\\\\n\\\\n---\\\\n\\\\n## Core Claims\\\\n\\\\n### C1: Variable-rate imagination in DreamerV3 consistently degrades performance\\\\n\\\\nTemporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |\\\\n| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |\\\\n| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\\\n| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |\\\\n\\\\n**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.\\\\n\\\\n### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk\\\\n\\\\n**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**\\\\n\\\\nThe trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:\\\\n\\\\n- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)\\\\n- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)\\\\n- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb\\\\n\\\\n**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。\\\\n\\\\n**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a \\\\\\\"point of no return\\\\\\\" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).\\\\n\\\\nThe trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is systematic value overestimation (delusional critic) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |\\\\n| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |\\\\n| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |\\\\n| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |\\\\n| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |\\\\n| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |\\\\n| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |\\\\n| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |\\\\n\\\\n**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 \\\\\\\"eliminates\\\\\\\" 改为 \\\\\\\"significantly delays and reduces\\\\\\\"。推荐方案仍是 008e_v3（C6）**。\\\\n\\\\n**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**\\\\n\\\\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\\\\n|-------|------------|------------|---------|---------------|---------------|------------|\\\\n| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |\\\\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |\\\\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |\\\\n\\\\n**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\\\\n\\\\n**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.\\\\n\\\\n### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance\\\\n\\\\nWhen dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |\\\\n| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |\\\\n| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |\\\\n| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |\\\\n| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |\\\\n\\\\n**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the delusional critic feedback loop in trained variants.\\\\n\\\\n**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).\\\\n\\\\n**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.\\\\n\\\\n### C4: Longer dt amplifies the problem\\\\n\\\\nIncreasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |\\\\n| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\\\n| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |\\\\n\\\\n**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.\\\\n\\\\n### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause\\\\n\\\\nSubsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |\\\\n| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |\\\\n| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |\\\\n| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |\\\\n| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |\\\\n\\\\n**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.\\\\n\\\\n### C6: Restricting imagination to dt=1 during multi-dt training provides practical mitigation\\\\n\\\\nWhen training with multi-dt data (subsample ON, dt∈{1,2}) while restricting imagination rollouts to dt=1, performance recovers to 95% of the dt=1 baseline. This provides a concrete, zero-cost mitigation guideline: keep imagination at dt=1 even if the world model learns multi-dt dynamics.\\\\n\\\\n**008f reward 退化发现进一步强化 C6 的价值**：008f（去掉 dt_embedding）虽避免崩塌但 reward 预测退化 75x；而 008e_v3（保留 trained dt_emb + dt=1 imagination）达到 95% baseline 且 reward prediction 不受影响。008e_v3 是唯一同时避免崩塌且保持完整预测能力的配置。**关键洞察：008d（trained dt_emb + dt>1 imag）collapse vs 008e_v3（trained dt_emb + dt=1 imag）healthy，证明 critical variable 是 imagination dt，不是 embedding 训练状态。不需要改动模型架构，只需改 imagination 策略。**\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| dt=1 imagination + multi-dt training | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval_return_105K=869.9 (95% of baseline 915.67), normalized v/e=0.80x |\\\\n| Comparison: dt=2 imagination collapses | exp_006 (subsample ON, trained dt_emb, dt=2 imag, H=15) | Peak 485@35K → collapse. v/e 2.3x baseline@55K |\\\\n| Comparison: untrained dt_emb + dt=2 degrades | exp_008a (subsample OFF, untrained dt_emb, dt=2 imag, H=15) | 778@105K (85% baseline). Better than collapse but 10pp below mitigation |\\\\n| Comparison: no dt_emb avoids collapse but degrades reward | exp_008f (dt_embed_dim=0, subsample ON, H=8) | No collapse, but reward_MAE=0.747 (75x baseline). Avoidance of collapse comes at cost of reward prediction |\\\\n\\\\n**Strength**: Moderate-strong → **strengthened by 008f contrast**. 008e_v3 is the only configuration that (a) avoids delusional critic collapse, (b) maintains healthy reward prediction, AND (c) achieves near-baseline performance (95%). Single seed, single environment; multi-seed + cross-environment planned (P0). Actionable: practitioners using variable-dt training data should restrict imagination to dt=1 until RSSM fidelity at dt>1 improves.\\\\n\\\\n---\\\\n\\\\n## Story Arc\\\\n\\\\n### 1. Introduction\\\\n- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)\\\\n- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction\\\\n- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?\\\\n- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for pathological value overestimation (nve>1.5x, 4/4 separating power), with collapse as a stochastic consequence, plus a practical mitigation guideline (dt=1 imagination → 95% baseline)\\\\n\\\\n### 2. Background & Related Work\\\\n- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)\\\\n- World-model RL (Dreamer family, IRIS, TWM)\\\\n- Variable-rate planning in world models (few prior works, mostly positive framing)\\\\n- Value overestimation / delusional policies in model-based RL\\\\n\\\\n### 3. Methodology\\\\n- DreamerV3 as base architecture\\\\n- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating\\\\n- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines\\\\n- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves\\\\n\\\\n### 4. Results\\\\n- **Finding 1**: All dt>1 configurations degrade (C1)\\\\n- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the \\\\\\\"smoking gun\\\\\\\" comparison (008c vs 008d)\\\\n- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)\\\\n- **Finding 4**: Longer dt amplifies (C4)\\\\n- **Finding 5**: Horizon/subsample effects are secondary (C5)\\\\n- **Finding 6**: Restricting imagination to dt=1 during multi-dt training recovers 95% baseline — practical mitigation (C6)\\\\n\\\\n### 5. Discussion\\\\n- Mechanism: why trained dt_embedding causes delusional critic (RSSM fidelity gap at dt>1)\\\\n- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x) — trained dt_emb 让 reward head 在 dt=2 时产生系统性偏差，这是 critic 被误导的直接来源\\\\n- 008f 的 reward 退化 trade-off：去掉 dt_embedding 避免崩塌但牺牲 reward 预测质量；008e_v3 是更优方案\\\\n- Connection to existing theory: non-delusional Q-learning (Lu et al., 2018), model exploitation in MBRL\\\\n- Why this is specific to world-model RL (model-free temporal abstraction doesn't suffer the same failure mode)\\\\n- **D032: Value self-correction mechanism (009b)**: 009b (008d seed 2) demonstrates that pathological overestimation (nve>1.5x) is not always irreversible. Value peaked at 110.9@65K then monotonically self-corrected to 67.3@105K, while eval simultaneously improved (172→268). Hypothesized mechanism: when the critic's overestimation does not yet dominate the actor's gradient signal (transient vs sustained nve>1.5x), the actor can still learn from real environment returns, creating a corrective force. In 008d seed 1, the sustained overestimation (3 consecutive checkpoints >1.5x at 35K+) overwhelmed this correction. The bifurcation likely depends on early training stochasticity — initialization and data sampling order determine whether the overestimation feedback loop locks in before correction can take hold (consistent with primacy bias in MBRL, Qiao et al. 2023; early outlier runs, Bjorck et al. 2022). This makes nve>1.5x a **necessary condition** for collapse but not sufficient — the temporal persistence of overestimation is the second gate.\\\\n\\\\n### 6. Implications for Future Work\\\\n- Don't use dt>1 imagination with trained dt_embedding in current world-model architectures (trained dt_emb is safe if imagination stays at dt=1)\\\\n- RSSM prediction quality must improve before variable-rate imagination is viable\\\\n- Imagination-side restriction (dt=1 imagination with multi-dt training) as the practical mitigation — no architecture change needed\\\\n- Need for diagnostic methodology in temporal abstraction research\\\\n\\\\n---\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n### R1: \\\\\\\"Limited to one environment / one base algorithm\\\\\\\"\\\\n**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.\\\\n**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.\\\\n\\\\n### R2: \\\\\\\"No proposed solution — what's the actionable takeaway?\\\\\\\"\\\\n**Pre-emption**: Beyond diagnosis, we provide a **concrete mitigation guideline**: train with multi-dt data but restrict imagination rollouts to dt=1. exp_008e_v3 demonstrates this recovers 95% of baseline performance (869.9 vs 915.67) with normalized v/e=0.80x (healthy). This is zero-cost to implement and directly actionable.\\\\n**Mitigation**: Present 008e_v3 as a practical recommendation in Section 6. Additionally, we outline an uncertainty-gated imagination truncation direction as future work.\\\\n\\\\n### R3: \\\\\\\"Value/eval ratio is a crude proxy for overestimation\\\\\\\"\\\\n**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.\\\\n**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.\\\\n\\\\n### R4: \\\\\\\"The factorial design is incomplete — missing cells in the grid\\\\\\\"\\\\n**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.\\\\n**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.\\\\n\\\\n### R5: \\\\\\\"Novelty concern — model exploitation / value overestimation in MBRL is well-known\\\\\\\"\\\\n**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.\\\\n\\\\n### R6: \\\\\\\"All results from a single seed — how robust are the conclusions?\\\\\\\"\\\\n**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.\\\\n**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.\\\\n\\\\n### R7: \\\\\\\"The factorial design confounds dt_embedding training with training data composition\\\\\\\"\\\\n**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).\\\\n**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for delusional critic.\\\\n\\\\n### R8: \\\\\\\"008f reward prediction degradation undermines the causal control\\\\\\\"\\\\n**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是\\\\\\\"去掉 dt_embedding → 不崩塌\\\\\\\"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。\\\\n**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（推荐方案）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。\\\\n\\\\n---\\\\n\\\\n## Experiment Coverage Assessment\\\\n\\\\n| Claim | Evidence Status | Gaps |\\\\n|-------|----------------|------|\\\\n| C1 (degradation) | ✅ Strong — 3 configurations (005, 006, 007) all negative | Could add 1 more environment |\\\\n| C2 (reliable pathological overestimation) | ⚠️ Moderate-strong (D032) — nve>1.5x threshold: 4/4 perfect separation (trained 2/2 exceed, untrained 0/2 exceed). Collapse stochastic: 1/2 trained seeds. Causal direction unambiguous. | 009e (008d seed 1) to narrow collapse probability; 009f (008f seed 1) for third untrained seed; 009c→200K |\\\\n| C3 (preventing optimistic drift) | ✅ Strong (105K confirmed) — 008a@105K=778 (85% baseline), normalized v/e=0.59x, two V-shaped recoveries | None — long-term structural suppression confirmed |\\\\n| C4 (dt amplification) | ⚠️ Moderate — only dt=2 vs dt=4 | Would benefit from dt=3, but not blocking |\\\\n| C5 (horizon/subsample) | ⚠️ Moderate — confounded with other factors | Need 008c-equivalent with H=15 + subsample ON + untrained dt_emb for clean isolation |\\\\n| C6 (mitigation) | ✅ Moderate-strong — 008e_v3@105K=869.9 (95% baseline), normalized v/e=0.80x | Single seed, single environment. Multi-seed + Cheetah Run planned |\\\\n\\\\n### Priority Actions Before Submission\\\\n1. ~~**Check exp_008a@65K**~~ — ✅ Done: 608 (-1.3% baseline), B+ confirmed\\\\n2. ~~**008e_v3 B+ confound**~~ — ✅ Done: 869.9@105K (95% baseline), B+ confirmed\\\\n3. ~~**008f C2 causal control**~~ — ✅ Done: V-recovery to 503@105K, normalized v/e=0.30x\\\\n4. **Multi-seed replication** — Walker Walk seeds 1-2 for baseline/008d/008f (running + queued)\\\\n5. **Cheetah Run cross-environment** — P0 priority, addresses R1\\\\n6. **Cartpole Swingup** — P0, non-locomotion environment broadens scope (升级)\\\\n7. **Figures** — learning curves, normalized v/e, value scatter, RSSM fidelity table (in progress, 0 GPU cost)\\\\n8. **Mitigation pilot** — uncertainty-gated imagination truncation (P0, addresses R2 actionability)\\\\n\\\\n---\\\\n\\\\n## Key Figures (Planned)\\\\n\\\\n1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)\\\\n2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes\\\\n3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis\\\\n4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse\\\\n5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)\\\\n6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）\\\\n7. **Figure 6 (D032)**: nve trajectory overlay — 008d seed 1 (sustained >1.5x → collapse) vs 009b seed 2 (transient >1.5x → self-correction), with 1.5x threshold line marked. Also overlay 008f seeds (both below 1.5x) for contrast.\\\\n\\\", \\\"total_chars\\\": 26876, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md\", \"content\": \"# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\\n\\n## Title Candidates\\n\\n1. **\\\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\\\"**\\n2. **\\\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\\\"**\\n3. **\\\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\\\"**\\n\\n## Venue\\n\\n**CoRL 2026** — Deadline: 2026-05-29\\n\\n## Narrative Positioning\\n\\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\\n\\nThe contribution is a **closed causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.\\n\\nWe scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.\\n\\n---\\n\\n## Core Claims\\n\\n### C1: Variable-rate imagination in DreamerV3 consistently degrades performance\\n\\nTemporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |\\n| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |\\n| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\n| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |\\n\\n**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.\\n\\n### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk\\n\\n**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**\\n\\nThe trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:\\n\\n- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)\\n- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)\\n- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb\\n\\n**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。\\n\\n**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a \\\"point of no return\\\" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).\\n\\nThe trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is systematic value overestimation (delusional critic) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |\\n| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |\\n| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |\\n| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |\\n| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |\\n| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |\\n| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |\\n| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |\\n\\n**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 \\\"eliminates\\\" 改为 \\\"significantly delays and reduces\\\"。推荐方案仍是 008e_v3（C6）**。\\n\\n**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**\\n\\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\\n|-------|------------|------------|---------|---------------|---------------|------------|\\n| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |\\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |\\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |\\n\\n**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\\n\\n**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.\\n\\n### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance\\n\\nWhen dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |\\n| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |\\n| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |\\n| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |\\n| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |\\n\\n**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the delusional critic feedback loop in trained variants.\\n\\n**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).\\n\\n**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.\\n\\n### C4: Longer dt amplifies the problem\\n\\nIncreasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |\\n| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\n| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |\\n\\n**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.\\n\\n### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause\\n\\nSubsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |\\n| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |\\n| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |\\n| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |\\n| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |\\n\\n**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.\\n\\n### C6: Restricting imagination to dt=1 during multi-dt training provides practical mitigation\\n\\nWhen training with multi-dt data (subsample ON, dt∈{1,2}) while restricting imagination rollouts to dt=1, performance recovers to 95% of the dt=1 baseline. This provides a concrete, zero-cost mitigation guideline: keep imagination at dt=1 even if the world model learns multi-dt dynamics.\\n\\n**008f reward 退化发现进一步强化 C6 的价值**：008f（去掉 dt_embedding）虽避免崩塌但 reward 预测退化 75x；而 008e_v3（保留 trained dt_emb + dt=1 imagination）达到 95% baseline 且 reward prediction 不受影响。008e_v3 是唯一同时避免崩塌且保持完整预测能力的配置。**关键洞察：008d（trained dt_emb + dt>1 imag）collapse vs 008e_v3（trained dt_emb + dt=1 imag）healthy，证明 critical variable 是 imagination dt，不是 embedding 训练状态。不需要改动模型架构，只需改 imagination 策略。**\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| dt=1 imagination + multi-dt training | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval_return_105K=869.9 (95% of baseline 915.67), normalized v/e=0.80x |\\n| Comparison: dt=2 imagination collapses | exp_006 (subsample ON, trained dt_emb, dt=2 imag, H=15) | Peak 485@35K → collapse. v/e 2.3x baseline@55K |\\n| Comparison: untrained dt_emb + dt=2 degrades | exp_008a (subsample OFF, untrained dt_emb, dt=2 imag, H=15) | 778@105K (85% baseline). Better than collapse but 10pp below mitigation |\\n| Comparison: no dt_emb avoids collapse but degrades reward | exp_008f (dt_embed_dim=0, subsample ON, H=8) | No collapse, but reward_MAE=0.747 (75x baseline). Avoidance of collapse comes at cost of reward prediction |\\n\\n**Strength**: Moderate-strong → **strengthened by 008f contrast**. 008e_v3 is the only configuration that (a) avoids delusional critic collapse, (b) maintains healthy reward prediction, AND (c) achieves near-baseline performance (95%). Single seed, single environment; multi-seed + cross-environment planned (P0). Actionable: practitioners using variable-dt training data should restrict imagination to dt=1 until RSSM fidelity at dt>1 improves.\\n\\n---\\n\\n## Story Arc\\n\\n### 1. Introduction\\n- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)\\n- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction\\n- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?\\n- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for pathological value overestimation (nve>1.5x, 4/4 separating power), with collapse as a stochastic consequence, plus a practical mitigation guideline (dt=1 imagination → 95% baseline)\\n\\n### 2. Background & Related Work\\n- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)\\n- World-model RL (Dreamer family, IRIS, TWM)\\n- Variable-rate planning in world models (few prior works, mostly positive framing)\\n- Value overestimation / delusional policies in model-based RL\\n\\n### 3. Methodology\\n- DreamerV3 as base architecture\\n- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating\\n- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines\\n- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves\\n\\n### 4. Results\\n- **Finding 1**: All dt>1 configurations degrade (C1)\\n- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the \\\"smoking gun\\\" comparison (008c vs 008d)\\n- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)\\n- **Finding 4**: Longer dt amplifies (C4)\\n- **Finding 5**: Horizon/subsample effects are secondary (C5)\\n- **Finding 6**: Restricting imagination to dt=1 during multi-dt training recovers 95% baseline — practical mitigation (C6)\\n\\n### 5. Discussion\\n- Mechanism: why trained dt_embedding causes delusional critic (RSSM fidelity gap at dt>1)\\n- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x) — trained dt_emb 让 reward head 在 dt=2 时产生系统性偏差，这是 critic 被误导的直接来源\\n- 008f 的 reward 退化 trade-off：去掉 dt_embedding 避免崩塌但牺牲 reward 预测质量；008e_v3 是更优方案\\n- Connection to existing theory: non-delusional Q-learning (Lu et al., 2018), model exploitation in MBRL\\n- Why this is specific to world-model RL (model-free temporal abstraction doesn't suffer the same failure mode)\\n- **D032: Value self-correction mechanism (009b)**: 009b (008d seed 2) demonstrates that pathological overestimation (nve>1.5x) is not always irreversible. Value peaked at 110.9@65K then monotonically self-corrected to 67.3@105K, while eval simultaneously improved (172→268). Hypothesized mechanism: when the critic's overestimation does not yet dominate the actor's gradient signal (transient vs sustained nve>1.5x), the actor can still learn from real environment returns, creating a corrective force. In 008d seed 1, the sustained overestimation (3 consecutive checkpoints >1.5x at 35K+) overwhelmed this correction. The bifurcation likely depends on early training stochasticity — initialization and data sampling order determine whether the overestimation feedback loop locks in before correction can take hold (consistent with primacy bias in MBRL, Qiao et al. 2023; early outlier runs, Bjorck et al. 2022). This makes nve>1.5x a **necessary condition** for collapse but not sufficient — the temporal persistence of overestimation is the second gate.\\n\\n### 6. Implications for Future Work\\n- Don't use dt>1 imagination with trained dt_embedding in current world-model architectures (trained dt_emb is safe if imagination stays at dt=1)\\n- RSSM prediction quality must improve before variable-rate imagination is viable\\n- Imagination-side restriction (dt=1 imagination with multi-dt training) as the practical mitigation — no architecture change needed\\n- Need for diagnostic methodology in temporal abstraction research\\n\\n---\\n\\n## Anticipated Reviewer Concerns\\n\\n### R1: \\\"Limited to one environment / one base algorithm\\\"\\n**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.\\n**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.\\n\\n### R2: \\\"No proposed solution — what's the actionable takeaway?\\\"\\n**Pre-emption**: Beyond diagnosis, we provide a **concrete mitigation guideline**: train with multi-dt data but restrict imagination rollouts to dt=1. exp_008e_v3 demonstrates this recovers 95% of baseline performance (869.9 vs 915.67) with normalized v/e=0.80x (healthy). This is zero-cost to implement and directly actionable.\\n**Mitigation**: Present 008e_v3 as a practical recommendation in Section 6. Additionally, we outline an uncertainty-gated imagination truncation direction as future work.\\n\\n### R3: \\\"Value/eval ratio is a crude proxy for overestimation\\\"\\n**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.\\n**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.\\n\\n### R4: \\\"The factorial design is incomplete — missing cells in the grid\\\"\\n**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.\\n**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.\\n\\n### R5: \\\"Novelty concern — model exploitation / value overestimation in MBRL is well-known\\\"\\n**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.\\n\\n### R6: \\\"All results from a single seed — how robust are the conclusions?\\\"\\n**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.\\n**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.\\n\\n### R7: \\\"The factorial design confounds dt_embedding training with training data composition\\\"\\n**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).\\n**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for delusional critic.\\n\\n### R8: \\\"008f reward prediction degradation undermines the causal control\\\"\\n**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是\\\"去掉 dt_embedding → 不崩塌\\\"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。\\n**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（推荐方案）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。\\n\\n---\\n\\n## Experiment Coverage Assessment\\n\\n| Claim | Evidence Status | Gaps |\\n|-------|----------------|------|\\n| C1 (degradation) | ✅ Strong — 3 configurations (005, 006, 007) all negative | Could add 1 more environment |\\n| C2 (reliable pathological overestimation) | ⚠️ Moderate-strong (D032) — nve>1.5x threshold: 4/4 perfect separation (trained 2/2 exceed, untrained 0/2 exceed). Collapse stochastic: 1/2 trained seeds. Causal direction unambiguous. | 009e (008d seed 1) to narrow collapse probability; 009f (008f seed 1) for third untrained seed; 009c→200K |\\n| C3 (preventing optimistic drift) | ✅ Strong (105K confirmed) — 008a@105K=778 (85% baseline), normalized v/e=0.59x, two V-shaped recoveries | None — long-term structural suppression confirmed |\\n| C4 (dt amplification) | ⚠️ Moderate — only dt=2 vs dt=4 | Would benefit from dt=3, but not blocking |\\n| C5 (horizon/subsample) | ⚠️ Moderate — confounded with other factors | Need 008c-equivalent with H=15 + subsample ON + untrained dt_emb for clean isolation |\\n| C6 (mitigation) | ✅ Moderate-strong — 008e_v3@105K=869.9 (95% baseline), normalized v/e=0.80x | Single seed, single environment. Multi-seed + Cheetah Run planned |\\n\\n### Priority Actions Before Submission\\n1. ~~**Check exp_008a@65K**~~ — ✅ Done: 608 (-1.3% baseline), B+ confirmed\\n2. ~~**008e_v3 B+ confound**~~ — ✅ Done: 869.9@105K (95% baseline), B+ confirmed\\n3. ~~**008f C2 causal control**~~ — ✅ Done: V-recovery to 503@105K, normalized v/e=0.30x\\n4. **Multi-seed replication** — Walker Walk seeds 1-2 for baseline/008d/008f (running + queued)\\n5. **Cheetah Run cross-environment** — P0 priority, addresses R1\\n6. **Cartpole Swingup** — P0, non-locomotion environment broadens scope (升级)\\n7. **Figures** — learning curves, normalized v/e, value scatter, RSSM fidelity table (in progress, 0 GPU cost)\\n8. **Mitigation pilot** — uncertainty-gated imagination truncation (P0, addresses R2 actionability)\\n\\n---\\n\\n## Key Figures (Planned)\\n\\n1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)\\n2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes\\n3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis\\n4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse\\n5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)\\n6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）\\n7. **Figure 6 (D032)**: nve trajectory overlay — 008d seed 1 (sustained >1.5x → collapse) vs 009b seed 2 (transient >1.5x → self-correction), with 1.5x threshold line marked. Also overlay 008f seeds (both below 1.5x) for contrast.\\n\", \"total_chars\": 26876, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0182aetwC8Edv7LgTXnp6Y8D`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
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
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "723721d9-135d-454d-9b12-3125927d5893",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016uBuyZh4rKiMrjGMj1ej6K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 23459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1097
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

_source line 12 · 2026-05-15T01:15:45.229Z_

<details><summary>↩ Tool result · `toolu_0182aetwC8Edv7LgTXnp6Y8D`</summary>

````text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/memory.md\", \"content\": \"# Memory\\n\\n## 2026-05-15: C6 跨 seed 一致性 — 极强信号\\n\\n008e_v3 seed 0 与 seed 1 的 105K 指标**几乎完全相同**：\\n- seed 0: eval=869.88, v/e=0.527\\n- seed 1: eval=869.9, v/e=0.527\\n\\n这种精度级别的跨 seed 一致性在 RL 实验中非常罕见（通常 seed 间方差很大，参考 Henderson 2018）。说明 C6 configuration (trained dt_emb + dt=1 imagination + H=15) 的训练动态极其稳定，不受随机初始化影响。\\n\\n**论文可用**：这个一致性本身可以作为 C6 robustness 的论据，对比 008d 的 seed-dependent collapse (1/2 seeds collapse)。\\n\\n## 2026-05-14: 文献增量扫描 — Novelty 安全，TAWM 强化贡献\\n\\n**literature_map.yaml**: 64 → 72 篇。\\n\\n**核心结论：无论文诊断过 dt_embedding → delusional critic → stochastic collapse 机制。Novelty 安全。**\\n\\n**TAWM (Nhu et al., ICML 2025)** 是最相关竞品——显式 Δt conditioning world model，但在 MPC 范式下。**反而强化我们的贡献**：TAWM 证明 Δt conditioning 在 MPC 中有效，我们发现它在 imagination-based actor-critic 中导致病态 value overestimation。这个对比本身就是 surprising finding。\\n\\n**领域趋势**：temporal abstraction in world models 正收敛到层级方法（THICK, Hieros, Director, HWM, SPlaTES），回避 flat variable-dt 方案。我们的诊断论文解释了 **为什么 flat dt 方案失败**。\\n\\n**必须引用**：nhu2025tawm（区分 MPC vs imagination 范式）。**应当引用**：li2025lsimagine, shaj2023mts3。**考虑引用**：zhang2026hwm。\\n\\n## 2026-05-14: D032 — Collapse is Stochastic, nve>1.5x is Reliable\\n\\n**发现**：009b (008d seed 2) 未复现 delusional critic collapse。\\n\\n数据对比：\\n- 008d seed 1: nve **持续** >1.5x（1.78x→1.71x→2.09x→4.12x, 4 个连续 checkpoint） → collapse (eval 167→83)\\n- 009b seed 2: nve **瞬时** >1.5x（2.05x@25K 单点），随后振荡回落至 0.38x@105K → no collapse (eval 升至 268)\\n\\n**关键结论**：\\n1. nve>1.5x 作为 trained dt_emb marker 是 100% reliable（4/4: trained 2/2 exceed, untrained 0/2 exceed）\\n2. Collapse 本身是 stochastic（1/2 seeds with trained dt_emb）\\n3. Sustained vs transient nve>1.5x 可能区分 collapse vs self-correction，但 N=2 不足以 claim\\n\\n**对论文的影响**：\\n- C2 因果方向不变（trained dt_emb → pathological nve>1.5x），但 \\\"必然 collapse\\\" 改为 \\\"创造 collapse vulnerability\\\"\\n- 定位从 \\\"failure predictor\\\" 调整为 \\\"reliable diagnostic marker\\\"（更 honest，更 robust to multi-seed challenge）\\n- C6 (008e_v3 mitigation) 完全不受影响\\n\\n**教训**：单 seed 的 collapse 不能 claim determinism。即使同一配置的两个 seed 走出完全不同的 trajectory——这与 Henderson 2018, Bjorck 2022, Qiao 2023 的文献一致。\\n\\n## 2026-05-14: 文献调研 — Reward Prediction & MBRL Novelty Gaps\\n\\n**6 篇新增至 literature_map.yaml**（worker_research_lit-reward-prediction-mbrl）。\\n\\n### 关键 novelty gaps（论文可用）\\n\\n1. **无论文研究 Dreamer 家族中 reward prediction 退化导致 seed-dependent instability** — 我们发现去掉 dt_embedding 选择性破坏 reward prediction（MAE 75x baseline）导致 seed-dependent recovery，这是未覆盖的现象。\\n2. **无论文研究 Dreamer world model 中 reward head 与 temporal conditioning 的耦合关系** — dt_embedding 同时影响 dynamics + reward prediction，去掉它消除 delusional critic 但破坏 reward prediction，这种 trade-off 未被文献讨论。\\n\\n### 相关文献支撑\\n\\n- DreamSmooth (ICLR 2024): reward prediction 是 MBRL 瓶颈（支撑我们的 reward degradation 发现）\\n- HarmonyDream (ICML 2024): obs vs reward 预测在 world model 中存在主导效应（支撑 dt_emb 的 dual effect）\\n- Bjorck 2022 (ICLR): RL 方差主要来自训练早期 outlier runs（与 009c seed 2 早期分叉一致）\\n- UNREAL (ICLR 2017) + Lyle 2021: reward prediction 作为 auxiliary task 塑造表征\\n\\n## 2026-05-14: Actor Entropy & Value Calibration 分析结果 (plan_031/032)\\n\\n**数据来源**: `logdir/analysis_actor_entropy_value_calibration.json`（2026-05-14 生成，v/R 已修正为 eval_return 基准）\\n\\n### Actor Entropy — 非显而易见的发现\\n\\n1. **Collapsed configs 的 entropy 下降反而更慢**（反直觉）：15K 步时 collapsed 的 008d=0.48, 006=0.96 仍为正值，而 healthy 的 008a=-1.15, 008c=-1.18 已为负。解释：actor 在 misleading value landscape 下挣扎，表现为收敛延迟而非加速。\\n2. **Baseline 独有的 entropy recovery**：entropy 从 -5.2 (65K) 回升至 -0.78 (315K)，与 return 从 ~400→~950 的提升同期。所有 event-gated 变体在其较短的训练长度内（55K-112K）均停留在 -5.2 附近，无法确认是否也会回升。\\n3. **Actor entropy 不是主要诊断信号**：collapsed vs healthy 的差异方向正确但幅度小，且受 run length 限制无法做后期对比。\\n\\n### Value Calibration — 最强诊断信号\\n\\n1. **v/R ratio（eval_return 基准）完美分离 collapsed vs healthy**：\\n   - Collapsed: 008d peak v/R=1.67@55K（value=137.88, return=82.75），006 peak v/R=2.72@65K（value=361.69, return=132.86）\\n   - Healthy: baseline ~0.69，event-gated healthy 0.20-0.53，**从未超过 1.0**\\n   - 判定阈值 v/R > 1.5 在 late training 可 100% 区分两类\\n\\n2. **008f 极端保守**：v/R=0.20@105K，eval_return=503.21 但 value 仅约 100。value function 严重低估实际回报。这与 009c 教训一致——去掉 dt_embedding 消除了 delusional critic 但引入 reward prediction 噪声，value function 因此保守。\\n\\n3. **Normalized v/e target 不具区分力**：所有实验 late-stage normalized_vt 均收敛至 ~1.0（collapsed 008d=1.0034, 006=1.0069; healthy 008a=1.0001, 008c=1.0084），无法用于诊断。\\n\\n### 组合机制（论文可用）\\n\\n**Delusional critic signature = 慢 entropy 收敛 + value 过高估计**。Actor 探索更多是因为 value landscape 误导，但这种探索被 delusional critic 引向错误方向。这构成一个可论证的因果链：trained dt_embedding → corrupted world model → value overestimation → misdirected exploration → performance collapse。\\n\\n### 论文使用建议\\n\\n- **可直接用**：v/R ratio 作为 delusional critic 诊断指标（Figure 材料），collapsed vs healthy 的 clean separation\\n- **可用但需 caveat**：actor entropy 趋势差异（方向正确但需注明 run length 不等）\\n- **不可用**：normalized v/e target（无区分力）；baseline entropy recovery（与 event-gating 机制无直接关系，属 baseline 自身行为）\\n\\n### 附注\\n\\n服务器上还有 `logdir/analysis_rssm_prediction_quality.json`（RSSM dt=1 vs dt=2 prediction quality），属于不同 plan 的分析产物。\\n\\n## 2026-05-14: 009c 教训 — dt_emb removal 的双重效应\\n\\n**发现**：去掉 dt_embedding 有两个独立效应：(1) 消除 delusional critic ✓，(2) 严重退化 reward prediction ✗。\\n\\n两个 seed 的 v/e 都正常（normalized v/e 均 < 1.5x），确认 delusional critic 被消除。但性能差异巨大：\\n- seed 1 (008f): zigzag recovery → 503@105K\\n- seed 2 (009c): peak 359@75K → monotonic decline → 148@105K\\n\\n**根因**：008f 的 reward_MAE=0.747（baseline 的 75x），reward gap 仅 1.01x（无法区分 dt=1/dt=2）。reward 信号噪声使优化 landscape 高度 seed-dependent。\\n\\n**对论文的影响**：\\n- C2 机制识别（trained dt_emb → delusional critic）：不受影响，两个 seed 都确认\\n- 008f 实用含义：从\\\"消除 collapse\\\"降为\\\"消除 delusional critic 但引入 reward 噪声\\\"\\n- C6 (008e_v3) 升格为核心推荐——唯一同时避免 delusional critic + 保持 reward prediction + 达 95% baseline 的方案\\n- Framing 提案（Option A: \\\"机制 + 陷阱 + 正确修复\\\"）已提交 Director 审批\\n\\n**教训**：单一 seed 的 positive result 不能用于 claim stability。008f seed 1 的 zigzag recovery 可能是随机事件，不是系统性保护。\\n\\n## 2026-05-14: Actor Entropy 分析决策（Director 修正）\\n\\n- **C2 cleanest comparison pair**: 008f vs 008d（仅 dt_embed_dim 不同）。不用 008c vs 008d（两个变量差异：subsample + dt_emb）。\\n- **论文措辞**: 用 \\\"entropy convergence delayed\\\"，不说 \\\"entropy rises\\\"。\\n- **原因**: 008c（subsample OFF）vs 008d（subsample ON）有两个变量差异，不是 clean single-variable control。008f 和 008d 唯一差异是 dt_embed_dim（0 vs 32），是最干净的因果对照。\\n\\n## 2026-05-14: cuda:1 排期（D031 修正）\\n\\n009b（running）→ **008e_v3_s1** → **008e_v3_s2** → 009e → 009f → 009c(200K) → plan_060\\n\\n008e_v3 是论文 crown jewel (C6)，多 seed 验证最高优先。\\n\\n## 2026-05-14: 监控教训 — tail_training_logs 有 buffering 延迟\\n\\n`tail_training_logs` 读的是 tmux stdout log 文件（~/runs/），该文件有 stdout buffering 延迟，显示的 step 可能滞后于实际训练进度数小时。**监控训练进度应直接读 logdir/metrics.jsonl**（通过 SSH read_only），不要依赖 tmux log。曾因此误判两个实验\\\"卡住\\\"，实际都在正常运行。\\n\\n## 2026-05-14: D033 — 008e_v3 dt_embedding 实际是 trained\\n\\n代码审计确认：008e_v3 使用 `--gate_subsample_max_dt 2`，nn.Embedding 默认 trainable 且代码无 freeze/detach，因此 dt_embedding 是 **trained** 的。\\n\\n**关键洞察**：008d（trained dt_emb + dt>1 imag）→ collapse，008e_v3（trained dt_emb + dt=1 imag）→ healthy (95% baseline)。**Critical variable 是 imagination dt，不是 embedding 训练状态。** 不需要改模型架构，只需改 imagination 策略（dt=1）。这让 C6 从\\\"改模型\\\"升级为\\\"改策略\\\"——实践者零成本采用。\\n\\n## 2026-05-14: Cheetah Run / Cartpole Swingup 环境验证\\n\\n### 结论：代码无需修改，直接可用\\n\\n代码通过 `--task` 参数自动解析环境名，流程：\\n- `--task dmc_cheetah_run` → `suite.load(\\\"cheetah\\\", \\\"run\\\")`\\n- `--task dmc_cartpole_swingup` → `suite.load(\\\"cartpole\\\", \\\"swingup\\\")`\\n\\n`dmc_proprio` 配置（action_repeat=2, envs=4, train_ratio=512, MLP encoder/decoder）对所有 DMC proprio 环境通用。\\n\\n### 环境 Observation/Action Space 对比\\n\\n| 环境 | Obs dims | Action dims | Action range |\\n|------|----------|-------------|--------------|\\n| walker_walk | orientations(14), height(1), velocity(9) = 24D | 6 | [-1, 1] |\\n| cheetah_run | position(8), velocity(9) = 17D | 6 | [-1, 1] |\\n| cartpole_swingup | position(3), velocity(2) = 5D | 1 | [-1, 1] |\\n\\n**注意：Cartpole Swingup obs/act 维度远小于 Walker/Cheetah。** MLP encoder/decoder 自动适配（从 obs_space 推断），无需手动调整。但模型容量可能过大——默认 512 units 对 5D obs + 1D act 可能 overkill。如果训练不稳定可考虑减小网络。\\n\\n### 启动命令模板\\n\\n**Cheetah Run Baseline:**\\n```bash\\npython dreamer.py --configs defaults dmc_proprio \\\\\\n  --task dmc_cheetah_run \\\\\\n  --logdir logdir/exp_XXX_baseline_cheetah_sY \\\\\\n  --steps 500000 --seed Y --compile False --device cuda:Z\\n```\\n\\n**Cheetah Run Treatment (以 008f config 为例):**\\n```bash\\npython dreamer.py --configs defaults dmc_proprio \\\\\\n  --task dmc_cheetah_run \\\\\\n  --logdir logdir/exp_XXX_008f_cheetah_sY \\\\\\n  --steps 105000 --seed Y --compile False --device cuda:Z \\\\\\n  --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 \\\\\\n  --imag_horizon 8 --gate_dt_embed_dim 0\\n```\\n\\n**Cartpole Swingup Baseline:**\\n```bash\\npython dreamer.py --configs defaults dmc_proprio \\\\\\n  --task dmc_cartpole_swingup \\\\\\n  --logdir logdir/exp_XXX_baseline_cartpole_sY \\\\\\n  --steps 500000 --seed Y --compile False --device cuda:Z\\n```\\n\\n**Cartpole Swingup Treatment (以 008f config 为例):**\\n```bash\\npython dreamer.py --configs defaults dmc_proprio \\\\\\n  --task dmc_cartpole_swingup \\\\\\n  --logdir logdir/exp_XXX_008f_cartpole_sY \\\\\\n  --steps 105000 --seed Y --compile False --device cuda:Z \\\\\\n  --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 \\\\\\n  --imag_horizon 8 --gate_dt_embed_dim 0\\n```\\n\\n### 环境特定注意事项\\n\\n1. **action_repeat=2** 对三个环境都适用（DMC 标准设置）\\n2. **time_limit=1000**（默认）对三个环境都适用\\n3. **Cartpole 维度差异**：obs 5D vs Walker 24D，act 1D vs Walker 6D。模型自动适配，但训练动态可能不同（更快收敛或更不稳定）\\n4. **Cheetah 与 Walker 类似**：都是 locomotion 任务，obs/act 维度接近，预期行为最相似\\n5. **环境变量**：`MUJOCO_GL=osmesa PYOPENGL_PLATFORM=osmesa LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6` 仍然需要\\n6. **无需代码修改**\\n\", \"total_chars\": 9307, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "f7abcd9e-178d-4d8b-907b-3ed938c43072",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/memory.md\\\", \\\"content\\\": \\\"# Memory\\\\n\\\\n## 2026-05-15: C6 跨 seed 一致性 — 极强信号\\\\n\\\\n008e_v3 seed 0 与 seed 1 的 105K 指标**几乎完全相同**：\\\\n- seed 0: eval=869.88, v/e=0.527\\\\n- seed 1: eval=869.9, v/e=0.527\\\\n\\\\n这种精度级别的跨 seed 一致性在 RL 实验中非常罕见（通常 seed 间方差很大，参考 Henderson 2018）。说明 C6 configuration (trained dt_emb + dt=1 imagination + H=15) 的训练动态极其稳定，不受随机初始化影响。\\\\n\\\\n**论文可用**：这个一致性本身可以作为 C6 robustness 的论据，对比 008d 的 seed-dependent collapse (1/2 seeds collapse)。\\\\n\\\\n## 2026-05-14: 文献增量扫描 — Novelty 安全，TAWM 强化贡献\\\\n\\\\n**literature_map.yaml**: 64 → 72 篇。\\\\n\\\\n**核心结论：无论文诊断过 dt_embedding → delusional critic → stochastic collapse 机制。Novelty 安全。**\\\\n\\\\n**TAWM (Nhu et al., ICML 2025)** 是最相关竞品——显式 Δt conditioning world model，但在 MPC 范式下。**反而强化我们的贡献**：TAWM 证明 Δt conditioning 在 MPC 中有效，我们发现它在 imagination-based actor-critic 中导致病态 value overestimation。这个对比本身就是 surprising finding。\\\\n\\\\n**领域趋势**：temporal abstraction in world models 正收敛到层级方法（THICK, Hieros, Director, HWM, SPlaTES），回避 flat variable-dt 方案。我们的诊断论文解释了 **为什么 flat dt 方案失败**。\\\\n\\\\n**必须引用**：nhu2025tawm（区分 MPC vs imagination 范式）。**应当引用**：li2025lsimagine, shaj2023mts3。**考虑引用**：zhang2026hwm。\\\\n\\\\n## 2026-05-14: D032 — Collapse is Stochastic, nve>1.5x is Reliable\\\\n\\\\n**发现**：009b (008d seed 2) 未复现 delusional critic collapse。\\\\n\\\\n数据对比：\\\\n- 008d seed 1: nve **持续** >1.5x（1.78x→1.71x→2.09x→4.12x, 4 个连续 checkpoint） → collapse (eval 167→83)\\\\n- 009b seed 2: nve **瞬时** >1.5x（2.05x@25K 单点），随后振荡回落至 0.38x@105K → no collapse (eval 升至 268)\\\\n\\\\n**关键结论**：\\\\n1. nve>1.5x 作为 trained dt_emb marker 是 100% reliable（4/4: trained 2/2 exceed, untrained 0/2 exceed）\\\\n2. Collapse 本身是 stochastic（1/2 seeds with trained dt_emb）\\\\n3. Sustained vs transient nve>1.5x 可能区分 collapse vs self-correction，但 N=2 不足以 claim\\\\n\\\\n**对论文的影响**：\\\\n- C2 因果方向不变（trained dt_emb → pathological nve>1.5x），但 \\\\\\\"必然 collapse\\\\\\\" 改为 \\\\\\\"创造 collapse vulnerability\\\\\\\"\\\\n- 定位从 \\\\\\\"failure predictor\\\\\\\" 调整为 \\\\\\\"reliable diagnostic marker\\\\\\\"（更 honest，更 robust to multi-seed challenge）\\\\n- C6 (008e_v3 mitigation) 完全不受影响\\\\n\\\\n**教训**：单 seed 的 collapse 不能 claim determinism。即使同一配置的两个 seed 走出完全不同的 trajectory——这与 Henderson 2018, Bjorck 2022, Qiao 2023 的文献一致。\\\\n\\\\n## 2026-05-14: 文献调研 — Reward Prediction & MBRL Novelty Gaps\\\\n\\\\n**6 篇新增至 literature_map.yaml**（worker_research_lit-reward-prediction-mbrl）。\\\\n\\\\n### 关键 novelty gaps（论文可用）\\\\n\\\\n1. **无论文研究 Dreamer 家族中 reward prediction 退化导致 seed-dependent instability** — 我们发现去掉 dt_embedding 选择性破坏 reward prediction（MAE 75x baseline）导致 seed-dependent recovery，这是未覆盖的现象。\\\\n2. **无论文研究 Dreamer world model 中 reward head 与 temporal conditioning 的耦合关系** — dt_embedding 同时影响 dynamics + reward prediction，去掉它消除 delusional critic 但破坏 reward prediction，这种 trade-off 未被文献讨论。\\\\n\\\\n### 相关文献支撑\\\\n\\\\n- DreamSmooth (ICLR 2024): reward prediction 是 MBRL 瓶颈（支撑我们的 reward degradation 发现）\\\\n- HarmonyDream (ICML 2024): obs vs reward 预测在 world model 中存在主导效应（支撑 dt_emb 的 dual effect）\\\\n- Bjorck 2022 (ICLR): RL 方差主要来自训练早期 outlier runs（与 009c seed 2 早期分叉一致）\\\\n- UNREAL (ICLR 2017) + Lyle 2021: reward prediction 作为 auxiliary task 塑造表征\\\\n\\\\n## 2026-05-14: Actor Entropy & Value Calibration 分析结果 (plan_031/032)\\\\n\\\\n**数据来源**: `logdir/analysis_actor_entropy_value_calibration.json`（2026-05-14 生成，v/R 已修正为 eval_return 基准）\\\\n\\\\n### Actor Entropy — 非显而易见的发现\\\\n\\\\n1. **Collapsed configs 的 entropy 下降反而更慢**（反直觉）：15K 步时 collapsed 的 008d=0.48, 006=0.96 仍为正值，而 healthy 的 008a=-1.15, 008c=-1.18 已为负。解释：actor 在 misleading value landscape 下挣扎，表现为收敛延迟而非加速。\\\\n2. **Baseline 独有的 entropy recovery**：entropy 从 -5.2 (65K) 回升至 -0.78 (315K)，与 return 从 ~400→~950 的提升同期。所有 event-gated 变体在其较短的训练长度内（55K-112K）均停留在 -5.2 附近，无法确认是否也会回升。\\\\n3. **Actor entropy 不是主要诊断信号**：collapsed vs healthy 的差异方向正确但幅度小，且受 run length 限制无法做后期对比。\\\\n\\\\n### Value Calibration — 最强诊断信号\\\\n\\\\n1. **v/R ratio（eval_return 基准）完美分离 collapsed vs healthy**：\\\\n   - Collapsed: 008d peak v/R=1.67@55K（value=137.88, return=82.75），006 peak v/R=2.72@65K（value=361.69, return=132.86）\\\\n   - Healthy: baseline ~0.69，event-gated healthy 0.20-0.53，**从未超过 1.0**\\\\n   - 判定阈值 v/R > 1.5 在 late training 可 100% 区分两类\\\\n\\\\n2. **008f 极端保守**：v/R=0.20@105K，eval_return=503.21 但 value 仅约 100。value function 严重低估实际回报。这与 009c 教训一致——去掉 dt_embedding 消除了 delusional critic 但引入 reward prediction 噪声，value function 因此保守。\\\\n\\\\n3. **Normalized v/e target 不具区分力**：所有实验 late-stage normalized_vt 均收敛至 ~1.0（collapsed 008d=1.0034, 006=1.0069; healthy 008a=1.0001, 008c=1.0084），无法用于诊断。\\\\n\\\\n### 组合机制（论文可用）\\\\n\\\\n**Delusional critic signature = 慢 entropy 收敛 + value 过高估计**。Actor 探索更多是因为 value landscape 误导，但这种探索被 delusional critic 引向错误方向。这构成一个可论证的因果链：trained dt_embedding → corrupted world model → value overestimation → misdirected exploration → performance collapse。\\\\n\\\\n### 论文使用建议\\\\n\\\\n- **可直接用**：v/R ratio 作为 delusional critic 诊断指标（Figure 材料），collapsed vs healthy 的 clean separation\\\\n- **可用但需 caveat**：actor entropy 趋势差异（方向正确但需注明 run length 不等）\\\\n- **不可用**：normalized v/e target（无区分力）；baseline entropy recovery（与 event-gating 机制无直接关系，属 baseline 自身行为）\\\\n\\\\n### 附注\\\\n\\\\n服务器上还有 `logdir/analysis_rssm_prediction_quality.json`（RSSM dt=1 vs dt=2 prediction quality），属于不同 plan 的分析产物。\\\\n\\\\n## 2026-05-14: 009c 教训 — dt_emb removal 的双重效应\\\\n\\\\n**发现**：去掉 dt_embedding 有两个独立效应：(1) 消除 delusional critic ✓，(2) 严重退化 reward prediction ✗。\\\\n\\\\n两个 seed 的 v/e 都正常（normalized v/e 均 < 1.5x），确认 delusional critic 被消除。但性能差异巨大：\\\\n- seed 1 (008f): zigzag recovery → 503@105K\\\\n- seed 2 (009c): peak 359@75K → monotonic decline → 148@105K\\\\n\\\\n**根因**：008f 的 reward_MAE=0.747（baseline 的 75x），reward gap 仅 1.01x（无法区分 dt=1/dt=2）。reward 信号噪声使优化 landscape 高度 seed-dependent。\\\\n\\\\n**对论文的影响**：\\\\n- C2 机制识别（trained dt_emb → delusional critic）：不受影响，两个 seed 都确认\\\\n- 008f 实用含义：从\\\\\\\"消除 collapse\\\\\\\"降为\\\\\\\"消除 delusional critic 但引入 reward 噪声\\\\\\\"\\\\n- C6 (008e_v3) 升格为核心推荐——唯一同时避免 delusional critic + 保持 reward prediction + 达 95% baseline 的方案\\\\n- Framing 提案（Option A: \\\\\\\"机制 + 陷阱 + 正确修复\\\\\\\"）已提交 Director 审批\\\\n\\\\n**教训**：单一 seed 的 positive result 不能用于 claim stability。008f seed 1 的 zigzag recovery 可能是随机事件，不是系统性保护。\\\\n\\\\n## 2026-05-14: Actor Entropy 分析决策（Director 修正）\\\\n\\\\n- **C2 cleanest comparison pair**: 008f vs 008d（仅 dt_embed_dim 不同）。不用 008c vs 008d（两个变量差异：subsample + dt_emb）。\\\\n- **论文措辞**: 用 \\\\\\\"entropy convergence delayed\\\\\\\"，不说 \\\\\\\"entropy rises\\\\\\\"。\\\\n- **原因**: 008c（subsample OFF）vs 008d（subsample ON）有两个变量差异，不是 clean single-variable control。008f 和 008d 唯一差异是 dt_embed_dim（0 vs 32），是最干净的因果对照。\\\\n\\\\n## 2026-05-14: cuda:1 排期（D031 修正）\\\\n\\\\n009b（running）→ **008e_v3_s1** → **008e_v3_s2** → 009e → 009f → 009c(200K) → plan_060\\\\n\\\\n008e_v3 是论文 crown jewel (C6)，多 seed 验证最高优先。\\\\n\\\\n## 2026-05-14: 监控教训 — tail_training_logs 有 buffering 延迟\\\\n\\\\n`tail_training_logs` 读的是 tmux stdout log 文件（~/runs/），该文件有 stdout buffering 延迟，显示的 step 可能滞后于实际训练进度数小时。**监控训练进度应直接读 logdir/metrics.jsonl**（通过 SSH read_only），不要依赖 tmux log。曾因此误判两个实验\\\\\\\"卡住\\\\\\\"，实际都在正常运行。\\\\n\\\\n## 2026-05-14: D033 — 008e_v3 dt_embedding 实际是 trained\\\\n\\\\n代码审计确认：008e_v3 使用 `--gate_subsample_max_dt 2`，nn.Embedding 默认 trainable 且代码无 freeze/detach，因此 dt_embedding 是 **trained** 的。\\\\n\\\\n**关键洞察**：008d（trained dt_emb + dt>1 imag）→ collapse，008e_v3（trained dt_emb + dt=1 imag）→ healthy (95% baseline)。**Critical variable 是 imagination dt，不是 embedding 训练状态。** 不需要改模型架构，只需改 imagination 策略（dt=1）。这让 C6 从\\\\\\\"改模型\\\\\\\"升级为\\\\\\\"改策略\\\\\\\"——实践者零成本采用。\\\\n\\\\n## 2026-05-14: Cheetah Run / Cartpole Swingup 环境验证\\\\n\\\\n### 结论：代码无需修改，直接可用\\\\n\\\\n代码通过 `--task` 参数自动解析环境名，流程：\\\\n- `--task dmc_cheetah_run` → `suite.load(\\\\\\\"cheetah\\\\\\\", \\\\\\\"run\\\\\\\")`\\\\n- `--task dmc_cartpole_swingup` → `suite.load(\\\\\\\"cartpole\\\\\\\", \\\\\\\"swingup\\\\\\\")`\\\\n\\\\n`dmc_proprio` 配置（action_repeat=2, envs=4, train_ratio=512, MLP encoder/decoder）对所有 DMC proprio 环境通用。\\\\n\\\\n### 环境 Observation/Action Space 对比\\\\n\\\\n| 环境 | Obs dims | Action dims | Action range |\\\\n|------|----------|-------------|--------------|\\\\n| walker_walk | orientations(14), height(1), velocity(9) = 24D | 6 | [-1, 1] |\\\\n| cheetah_run | position(8), velocity(9) = 17D | 6 | [-1, 1] |\\\\n| cartpole_swingup | position(3), velocity(2) = 5D | 1 | [-1, 1] |\\\\n\\\\n**注意：Cartpole Swingup obs/act 维度远小于 Walker/Cheetah。** MLP encoder/decoder 自动适配（从 obs_space 推断），无需手动调整。但模型容量可能过大——默认 512 units 对 5D obs + 1D act 可能 overkill。如果训练不稳定可考虑减小网络。\\\\n\\\\n### 启动命令模板\\\\n\\\\n**Cheetah Run Baseline:**\\\\n```bash\\\\npython dreamer.py --configs defaults dmc_proprio \\\\\\\\\\\\n  --task dmc_cheetah_run \\\\\\\\\\\\n  --logdir logdir/exp_XXX_baseline_cheetah_sY \\\\\\\\\\\\n  --steps 500000 --seed Y --compile False --device cuda:Z\\\\n```\\\\n\\\\n**Cheetah Run Treatment (以 008f config 为例):**\\\\n```bash\\\\npython dreamer.py --configs defaults dmc_proprio \\\\\\\\\\\\n  --task dmc_cheetah_run \\\\\\\\\\\\n  --logdir logdir/exp_XXX_008f_cheetah_sY \\\\\\\\\\\\n  --steps 105000 --seed Y --compile False --device cuda:Z \\\\\\\\\\\\n  --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 \\\\\\\\\\\\n  --imag_horizon 8 --gate_dt_embed_dim 0\\\\n```\\\\n\\\\n**Cartpole Swingup Baseline:**\\\\n```bash\\\\npython dreamer.py --configs defaults dmc_proprio \\\\\\\\\\\\n  --task dmc_cartpole_swingup \\\\\\\\\\\\n  --logdir logdir/exp_XXX_baseline_cartpole_sY \\\\\\\\\\\\n  --steps 500000 --seed Y --compile False --device cuda:Z\\\\n```\\\\n\\\\n**Cartpole Swingup Treatment (以 008f config 为例):**\\\\n```bash\\\\npython dreamer.py --configs defaults dmc_proprio \\\\\\\\\\\\n  --task dmc_cartpole_swingup \\\\\\\\\\\\n  --logdir logdir/exp_XXX_008f_cartpole_sY \\\\\\\\\\\\n  --steps 105000 --seed Y --compile False --device cuda:Z \\\\\\\\\\\\n  --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 \\\\\\\\\\\\n  --imag_horizon 8 --gate_dt_embed_dim 0\\\\n```\\\\n\\\\n### 环境特定注意事项\\\\n\\\\n1. **action_repeat=2** 对三个环境都适用（DMC 标准设置）\\\\n2. **time_limit=1000**（默认）对三个环境都适用\\\\n3. **Cartpole 维度差异**：obs 5D vs Walker 24D，act 1D vs Walker 6D。模型自动适配，但训练动态可能不同（更快收敛或更不稳定）\\\\n4. **Cheetah 与 Walker 类似**：都是 locomotion 任务，obs/act 维度接近，预期行为最相似\\\\n5. **环境变量**：`MUJOCO_GL=osmesa PYOPENGL_PLATFORM=osmesa LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6` 仍然需要\\\\n6. **无需代码修改**\\\\n\\\", \\\"total_chars\\\": 9307, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/memory.md\", \"content\": \"# Memory\\n\\n## 2026-05-15: C6 跨 seed 一致性 — 极强信号\\n\\n008e_v3 seed 0 与 seed 1 的 105K 指标**几乎完全相同**：\\n- seed 0: eval=869.88, v/e=0.527\\n- seed 1: eval=869.9, v/e=0.527\\n\\n这种精度级别的跨 seed 一致性在 RL 实验中非常罕见（通常 seed 间方差很大，参考 Henderson 2018）。说明 C6 configuration (trained dt_emb + dt=1 imagination + H=15) 的训练动态极其稳定，不受随机初始化影响。\\n\\n**论文可用**：这个一致性本身可以作为 C6 robustness 的论据，对比 008d 的 seed-dependent collapse (1/2 seeds collapse)。\\n\\n## 2026-05-14: 文献增量扫描 — Novelty 安全，TAWM 强化贡献\\n\\n**literature_map.yaml**: 64 → 72 篇。\\n\\n**核心结论：无论文诊断过 dt_embedding → delusional critic → stochastic collapse 机制。Novelty 安全。**\\n\\n**TAWM (Nhu et al., ICML 2025)** 是最相关竞品——显式 Δt conditioning world model，但在 MPC 范式下。**反而强化我们的贡献**：TAWM 证明 Δt conditioning 在 MPC 中有效，我们发现它在 imagination-based actor-critic 中导致病态 value overestimation。这个对比本身就是 surprising finding。\\n\\n**领域趋势**：temporal abstraction in world models 正收敛到层级方法（THICK, Hieros, Director, HWM, SPlaTES），回避 flat variable-dt 方案。我们的诊断论文解释了 **为什么 flat dt 方案失败**。\\n\\n**必须引用**：nhu2025tawm（区分 MPC vs imagination 范式）。**应当引用**：li2025lsimagine, shaj2023mts3。**考虑引用**：zhang2026hwm。\\n\\n## 2026-05-14: D032 — Collapse is Stochastic, nve>1.5x is Reliable\\n\\n**发现**：009b (008d seed 2) 未复现 delusional critic collapse。\\n\\n数据对比：\\n- 008d seed 1: nve **持续** >1.5x（1.78x→1.71x→2.09x→4.12x, 4 个连续 checkpoint） → collapse (eval 167→83)\\n- 009b seed 2: nve **瞬时** >1.5x（2.05x@25K 单点），随后振荡回落至 0.38x@105K → no collapse (eval 升至 268)\\n\\n**关键结论**：\\n1. nve>1.5x 作为 trained dt_emb marker 是 100% reliable（4/4: trained 2/2 exceed, untrained 0/2 exceed）\\n2. Collapse 本身是 stochastic（1/2 seeds with trained dt_emb）\\n3. Sustained vs transient nve>1.5x 可能区分 collapse vs self-correction，但 N=2 不足以 claim\\n\\n**对论文的影响**：\\n- C2 因果方向不变（trained dt_emb → pathological nve>1.5x），但 \\\"必然 collapse\\\" 改为 \\\"创造 collapse vulnerability\\\"\\n- 定位从 \\\"failure predictor\\\" 调整为 \\\"reliable diagnostic marker\\\"（更 honest，更 robust to multi-seed challenge）\\n- C6 (008e_v3 mitigation) 完全不受影响\\n\\n**教训**：单 seed 的 collapse 不能 claim determinism。即使同一配置的两个 seed 走出完全不同的 trajectory——这与 Henderson 2018, Bjorck 2022, Qiao 2023 的文献一致。\\n\\n## 2026-05-14: 文献调研 — Reward Prediction & MBRL Novelty Gaps\\n\\n**6 篇新增至 literature_map.yaml**（worker_research_lit-reward-prediction-mbrl）。\\n\\n### 关键 novelty gaps（论文可用）\\n\\n1. **无论文研究 Dreamer 家族中 reward prediction 退化导致 seed-dependent instability** — 我们发现去掉 dt_embedding 选择性破坏 reward prediction（MAE 75x baseline）导致 seed-dependent recovery，这是未覆盖的现象。\\n2. **无论文研究 Dreamer world model 中 reward head 与 temporal conditioning 的耦合关系** — dt_embedding 同时影响 dynamics + reward prediction，去掉它消除 delusional critic 但破坏 reward prediction，这种 trade-off 未被文献讨论。\\n\\n### 相关文献支撑\\n\\n- DreamSmooth (ICLR 2024): reward prediction 是 MBRL 瓶颈（支撑我们的 reward degradation 发现）\\n- HarmonyDream (ICML 2024): obs vs reward 预测在 world model 中存在主导效应（支撑 dt_emb 的 dual effect）\\n- Bjorck 2022 (ICLR): RL 方差主要来自训练早期 outlier runs（与 009c seed 2 早期分叉一致）\\n- UNREAL (ICLR 2017) + Lyle 2021: reward prediction 作为 auxiliary task 塑造表征\\n\\n## 2026-05-14: Actor Entropy & Value Calibration 分析结果 (plan_031/032)\\n\\n**数据来源**: `logdir/analysis_actor_entropy_value_calibration.json`（2026-05-14 生成，v/R 已修正为 eval_return 基准）\\n\\n### Actor Entropy — 非显而易见的发现\\n\\n1. **Collapsed configs 的 entropy 下降反而更慢**（反直觉）：15K 步时 collapsed 的 008d=0.48, 006=0.96 仍为正值，而 healthy 的 008a=-1.15, 008c=-1.18 已为负。解释：actor 在 misleading value landscape 下挣扎，表现为收敛延迟而非加速。\\n2. **Baseline 独有的 entropy recovery**：entropy 从 -5.2 (65K) 回升至 -0.78 (315K)，与 return 从 ~400→~950 的提升同期。所有 event-gated 变体在其较短的训练长度内（55K-112K）均停留在 -5.2 附近，无法确认是否也会回升。\\n3. **Actor entropy 不是主要诊断信号**：collapsed vs healthy 的差异方向正确但幅度小，且受 run length 限制无法做后期对比。\\n\\n### Value Calibration — 最强诊断信号\\n\\n1. **v/R ratio（eval_return 基准）完美分离 collapsed vs healthy**：\\n   - Collapsed: 008d peak v/R=1.67@55K（value=137.88, return=82.75），006 peak v/R=2.72@65K（value=361.69, return=132.86）\\n   - Healthy: baseline ~0.69，event-gated healthy 0.20-0.53，**从未超过 1.0**\\n   - 判定阈值 v/R > 1.5 在 late training 可 100% 区分两类\\n\\n2. **008f 极端保守**：v/R=0.20@105K，eval_return=503.21 但 value 仅约 100。value function 严重低估实际回报。这与 009c 教训一致——去掉 dt_embedding 消除了 delusional critic 但引入 reward prediction 噪声，value function 因此保守。\\n\\n3. **Normalized v/e target 不具区分力**：所有实验 late-stage normalized_vt 均收敛至 ~1.0（collapsed 008d=1.0034, 006=1.0069; healthy 008a=1.0001, 008c=1.0084），无法用于诊断。\\n\\n### 组合机制（论文可用）\\n\\n**Delusional critic signature = 慢 entropy 收敛 + value 过高估计**。Actor 探索更多是因为 value landscape 误导，但这种探索被 delusional critic 引向错误方向。这构成一个可论证的因果链：trained dt_embedding → corrupted world model → value overestimation → misdirected exploration → performance collapse。\\n\\n### 论文使用建议\\n\\n- **可直接用**：v/R ratio 作为 delusional critic 诊断指标（Figure 材料），collapsed vs healthy 的 clean separation\\n- **可用但需 caveat**：actor entropy 趋势差异（方向正确但需注明 run length 不等）\\n- **不可用**：normalized v/e target（无区分力）；baseline entropy recovery（与 event-gating 机制无直接关系，属 baseline 自身行为）\\n\\n### 附注\\n\\n服务器上还有 `logdir/analysis_rssm_prediction_quality.json`（RSSM dt=1 vs dt=2 prediction quality），属于不同 plan 的分析产物。\\n\\n## 2026-05-14: 009c 教训 — dt_emb removal 的双重效应\\n\\n**发现**：去掉 dt_embedding 有两个独立效应：(1) 消除 delusional critic ✓，(2) 严重退化 reward prediction ✗。\\n\\n两个 seed 的 v/e 都正常（normalized v/e 均 < 1.5x），确认 delusional critic 被消除。但性能差异巨大：\\n- seed 1 (008f): zigzag recovery → 503@105K\\n- seed 2 (009c): peak 359@75K → monotonic decline → 148@105K\\n\\n**根因**：008f 的 reward_MAE=0.747（baseline 的 75x），reward gap 仅 1.01x（无法区分 dt=1/dt=2）。reward 信号噪声使优化 landscape 高度 seed-dependent。\\n\\n**对论文的影响**：\\n- C2 机制识别（trained dt_emb → delusional critic）：不受影响，两个 seed 都确认\\n- 008f 实用含义：从\\\"消除 collapse\\\"降为\\\"消除 delusional critic 但引入 reward 噪声\\\"\\n- C6 (008e_v3) 升格为核心推荐——唯一同时避免 delusional critic + 保持 reward prediction + 达 95% baseline 的方案\\n- Framing 提案（Option A: \\\"机制 + 陷阱 + 正确修复\\\"）已提交 Director 审批\\n\\n**教训**：单一 seed 的 positive result 不能用于 claim stability。008f seed 1 的 zigzag recovery 可能是随机事件，不是系统性保护。\\n\\n## 2026-05-14: Actor Entropy 分析决策（Director 修正）\\n\\n- **C2 cleanest comparison pair**: 008f vs 008d（仅 dt_embed_dim 不同）。不用 008c vs 008d（两个变量差异：subsample + dt_emb）。\\n- **论文措辞**: 用 \\\"entropy convergence delayed\\\"，不说 \\\"entropy rises\\\"。\\n- **原因**: 008c（subsample OFF）vs 008d（subsample ON）有两个变量差异，不是 clean single-variable control。008f 和 008d 唯一差异是 dt_embed_dim（0 vs 32），是最干净的因果对照。\\n\\n## 2026-05-14: cuda:1 排期（D031 修正）\\n\\n009b（running）→ **008e_v3_s1** → **008e_v3_s2** → 009e → 009f → 009c(200K) → plan_060\\n\\n008e_v3 是论文 crown jewel (C6)，多 seed 验证最高优先。\\n\\n## 2026-05-14: 监控教训 — tail_training_logs 有 buffering 延迟\\n\\n`tail_training_logs` 读的是 tmux stdout log 文件（~/runs/），该文件有 stdout buffering 延迟，显示的 step 可能滞后于实际训练进度数小时。**监控训练进度应直接读 logdir/metrics.jsonl**（通过 SSH read_only），不要依赖 tmux log。曾因此误判两个实验\\\"卡住\\\"，实际都在正常运行。\\n\\n## 2026-05-14: D033 — 008e_v3 dt_embedding 实际是 trained\\n\\n代码审计确认：008e_v3 使用 `--gate_subsample_max_dt 2`，nn.Embedding 默认 trainable 且代码无 freeze/detach，因此 dt_embedding 是 **trained** 的。\\n\\n**关键洞察**：008d（trained dt_emb + dt>1 imag）→ collapse，008e_v3（trained dt_emb + dt=1 imag）→ healthy (95% baseline)。**Critical variable 是 imagination dt，不是 embedding 训练状态。** 不需要改模型架构，只需改 imagination 策略（dt=1）。这让 C6 从\\\"改模型\\\"升级为\\\"改策略\\\"——实践者零成本采用。\\n\\n## 2026-05-14: Cheetah Run / Cartpole Swingup 环境验证\\n\\n### 结论：代码无需修改，直接可用\\n\\n代码通过 `--task` 参数自动解析环境名，流程：\\n- `--task dmc_cheetah_run` → `suite.load(\\\"cheetah\\\", \\\"run\\\")`\\n- `--task dmc_cartpole_swingup` → `suite.load(\\\"cartpole\\\", \\\"swingup\\\")`\\n\\n`dmc_proprio` 配置（action_repeat=2, envs=4, train_ratio=512, MLP encoder/decoder）对所有 DMC proprio 环境通用。\\n\\n### 环境 Observation/Action Space 对比\\n\\n| 环境 | Obs dims | Action dims | Action range |\\n|------|----------|-------------|--------------|\\n| walker_walk | orientations(14), height(1), velocity(9) = 24D | 6 | [-1, 1] |\\n| cheetah_run | position(8), velocity(9) = 17D | 6 | [-1, 1] |\\n| cartpole_swingup | position(3), velocity(2) = 5D | 1 | [-1, 1] |\\n\\n**注意：Cartpole Swingup obs/act 维度远小于 Walker/Cheetah。** MLP encoder/decoder 自动适配（从 obs_space 推断），无需手动调整。但模型容量可能过大——默认 512 units 对 5D obs + 1D act 可能 overkill。如果训练不稳定可考虑减小网络。\\n\\n### 启动命令模板\\n\\n**Cheetah Run Baseline:**\\n```bash\\npython dreamer.py --configs defaults dmc_proprio \\\\\\n  --task dmc_cheetah_run \\\\\\n  --logdir logdir/exp_XXX_baseline_cheetah_sY \\\\\\n  --steps 500000 --seed Y --compile False --device cuda:Z\\n```\\n\\n**Cheetah Run Treatment (以 008f config 为例):**\\n```bash\\npython dreamer.py --configs defaults dmc_proprio \\\\\\n  --task dmc_cheetah_run \\\\\\n  --logdir logdir/exp_XXX_008f_cheetah_sY \\\\\\n  --steps 105000 --seed Y --compile False --device cuda:Z \\\\\\n  --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 \\\\\\n  --imag_horizon 8 --gate_dt_embed_dim 0\\n```\\n\\n**Cartpole Swingup Baseline:**\\n```bash\\npython dreamer.py --configs defaults dmc_proprio \\\\\\n  --task dmc_cartpole_swingup \\\\\\n  --logdir logdir/exp_XXX_baseline_cartpole_sY \\\\\\n  --steps 500000 --seed Y --compile False --device cuda:Z\\n```\\n\\n**Cartpole Swingup Treatment (以 008f config 为例):**\\n```bash\\npython dreamer.py --configs defaults dmc_proprio \\\\\\n  --task dmc_cartpole_swingup \\\\\\n  --logdir logdir/exp_XXX_008f_cartpole_sY \\\\\\n  --steps 105000 --seed Y --compile False --device cuda:Z \\\\\\n  --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 \\\\\\n  --imag_horizon 8 --gate_dt_embed_dim 0\\n```\\n\\n### 环境特定注意事项\\n\\n1. **action_repeat=2** 对三个环境都适用（DMC 标准设置）\\n2. **time_limit=1000**（默认）对三个环境都适用\\n3. **Cartpole 维度差异**：obs 5D vs Walker 24D，act 1D vs Walker 6D。模型自动适配，但训练动态可能不同（更快收敛或更不稳定）\\n4. **Cheetah 与 Walker 类似**：都是 locomotion 任务，obs/act 维度接近，预期行为最相似\\n5. **环境变量**：`MUJOCO_GL=osmesa PYOPENGL_PLATFORM=osmesa LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6` 仍然需要\\n6. **无需代码修改**\\n\", \"total_chars\": 9307, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
````

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015NvA3eHHb1XM56CSMj8Vmq`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
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
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "10298c28-b2eb-45b8-9e1c-0387f3f1f26f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016uBuyZh4rKiMrjGMj1ej6K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 23459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1097
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

_source line 14 · 2026-05-15T01:15:45.969Z_

<details><summary>↩ Tool result · `toolu_015NvA3eHHb1XM56CSMj8Vmq`</summary>

```text
&lt;persisted-output>
Output too large (52.4KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/e9efbf3e-355b-4b54-9c61-7a3e79247d76/tool-results/toolu_015NvA3eHHb1XM56CSMj8Vmq.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml\", \"content\": \"# Literature Map — event-gated-adaptive-horizon\\n# Last updated: 2026-05-14\\n# Total: 72 papers (64 existing + 8 incremental scan 2026-05-14)\\n\\n# ============================================================\\n# EXISTING CITATIONS (already in paper.tex)\\n# ============================================================\\n\\n- paper_id: sutton1999options\\n  title: \\\"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\\\"\\n  authors: [Sutton R.S., Precup D., Singh S.]\\n  year: 1999\\n  venue: \\\"Artificial Intelligence 112(1-2):181-211\\\"\\n  category: background\\n  role: \\\"Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL\\\"\\n  relevance_score: 5\\n\\n- paper_id: hafner2020dreamerv1\\n  title: \\\"Dream to Control: Learning Behaviors by Latent Imagination\\\"\\n  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]\\n  year: 2020\\n  venue: ICLR\\n  category: background\\n  role: \\\"DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm\\\"\\n  relevance_score: 5\\n\\n- paper_id: hafner2023dreamerv3\\n  title: \\\"Mastering Diverse Domains through World Models\\\"\\n  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]\\n  year: 2023\\n  venue: \\\"arXiv:2301.04104 (Nature 2025)\\\"\\n  category: background\\n  role: \\\"DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here\\\"\\n  relevance_score: 5\\n\\n- paper_id: sharma2017figar\\n  title: \\\"Fine Grained Action Repetition for Deep Reinforcement Learning\\\"\\n  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]\\n  year: 2017\\n  venue: \\\"ICLR Workshop\\\"\\n
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "8dcf8fc4-4034-48cf-bda4-2674b1e2d794",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml\\\", \\\"content\\\": \\\"# Literature Map — event-gated-adaptive-horizon\\\\n# Last updated: 2026-05-14\\\\n# Total: 72 papers (64 existing + 8 incremental scan 2026-05-14)\\\\n\\\\n# ============================================================\\\\n# EXISTING CITATIONS (already in paper.tex)\\\\n# ============================================================\\\\n\\\\n- paper_id: sutton1999options\\\\n  title: \\\\\\\"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\\\\\\\"\\\\n  authors: [Sutton R.S., Precup D., Singh S.]\\\\n  year: 1999\\\\n  venue: \\\\\\\"Artificial Intelligence 112(1-2):181-211\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: hafner2020dreamerv1\\\\n  title: \\\\\\\"Dream to Control: Learning Behaviors by Latent Imagination\\\\\\\"\\\\n  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]\\\\n  year: 2020\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: hafner2023dreamerv3\\\\n  title: \\\\\\\"Mastering Diverse Domains through World Models\\\\\\\"\\\\n  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]\\\\n  year: 2023\\\\n  venue: \\\\\\\"arXiv:2301.04104 (Nature 2025)\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: sharma2017figar\\\\n  title: \\\\\\\"Fine Grained Action Repetition for Deep Reinforcement Learning\\\\\\\"\\\\n  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]\\\\n  year: 2017\\\\n  venue: \\\\\\\"ICLR Workshop\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"FiGAR — learns action-repeat durations in model-free RL; we extend the idea to imagination step size in world-model RL\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: janner2019mbpo\\\\n  title: \\\\\\\"When to Trust Your Model: Model-Based Policy Optimization\\\\\\\"\\\\n  authors: [Janner M., Fu J., Zhang M., Levine S.]\\\\n  year: 2019\\\\n  venue: NeurIPS\\\\n  category: background\\\\n  role: \\\\\\\"MBPO — formalizes model exploitation in MBRL; our delusional critic is a specific instance of model exploitation tied to temporal embedding\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n# ============================================================\\\\n# NEW: Multi-step prediction error compounding\\\\n# ============================================================\\\\n\\\\n- paper_id: ke2019learning\\\\n  title: \\\\\\\"Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future\\\\\\\"\\\\n  authors: [Ke N.R., Singh A., Touati A., Goyal A., Bengio Y., Parikh D., Batra D.]\\\\n  year: 2019\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"Addresses long-term dynamics prediction via latent-variable autoregressive model; directly relevant to our finding that multi-step RSSM predictions degrade with dt>1\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: asadi2019combating\\\\n  title: \\\\\\\"Combating the Compounding-Error Problem with a Multi-step Model\\\\\\\"\\\\n  authors: [Asadi K., Misra D., Kim S., Littman M.L.]\\\\n  year: 2019\\\\n  venue: \\\\\\\"arXiv:1905.13320\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Proposes multi-step models to bypass compounding error; our work shows that even with multi-step imagination, the dt-embedding creates a different failure mode (value overestimation) distinct from compounding error\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: venkatraman2015improving\\\\n  title: \\\\\\\"Improving Multi-Step Prediction of Learned Time Series Models\\\\\\\"\\\\n  authors: [Venkatraman A., Hebert M., Bagnell J.A.]\\\\n  year: 2015\\\\n  venue: AAAI\\\\n  category: background\\\\n  role: \\\\\\\"Data-as-Demonstrator (DaD) for robust multi-step prediction; establishes theoretical guarantee relating training error to multi-step prediction error\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: lambert2022investigating\\\\n  title: \\\\\\\"Investigating Compounding Prediction Errors in Learned Dynamics Models\\\\\\\"\\\\n  authors: [Lambert N., Pister K.S.J., Calandra R.]\\\\n  year: 2022\\\\n  venue: \\\\\\\"arXiv:2203.09637\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Empirical study of compounding error properties; we rule out compounding error as the primary failure mechanism (008c vs 008a comparison) and identify value overestimation instead\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: Model-predictive control with learned dynamics\\\\n# ============================================================\\\\n\\\\n- paper_id: chua2018pets\\\\n  title: \\\\\\\"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models\\\\\\\"\\\\n  authors: [Chua K., Calandra R., McAllister R., Levine S.]\\\\n  year: 2018\\\\n  venue: NeurIPS\\\\n  category: background\\\\n  role: \\\\\\\"PETS — ensemble-based uncertainty-aware MPC; uses explicit uncertainty quantification to avoid model exploitation, contrasting with DreamerV3's implicit approach\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: nagabandi2018neural\\\\n  title: \\\\\\\"Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning\\\\\\\"\\\\n  authors: [Nagabandi A., Kahn G., Fearing R.S., Levine S.]\\\\n  year: 2018\\\\n  venue: ICRA\\\\n  category: background\\\\n  role: \\\\\\\"Demonstrates NN dynamics + MPC for locomotion; model errors accumulate over prediction horizon, motivating our investigation of horizon-dependent failures\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: hansen2024tdmpc2\\\\n  title: \\\\\\\"TD-MPC2: Scalable, Robust World Models for Continuous Control\\\\\\\"\\\\n  authors: [Hansen N., Su H., Wang X.]\\\\n  year: 2024\\\\n  venue: \\\\\\\"ICLR (arXiv:2310.16828)\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"TD-MPC2 — SOTA MPC planning route (online planning + learned dynamics); DMC benchmark leader but orthogonal to imagination-based training — reviewer defense: TD-MPC2 does online MPC rollouts at test time, we study actor-critic training via imagined rollouts (DreamerV3 paradigm), not a same-level comparison\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n# ============================================================\\\\n# NEW: Pessimistic MBRL / model exploitation mitigation\\\\n# ============================================================\\\\n\\\\n- paper_id: yu2020mopo\\\\n  title: \\\\\\\"MOPO: Model-based Offline Policy Optimization\\\\\\\"\\\\n  authors: [Yu T., Thomas G., Yu L., Ermon S., Zou J., Levine S., Finn C., Ma T.]\\\\n  year: 2020\\\\n  venue: \\\\\\\"NeurIPS (arXiv:2005.13239)\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"MOPO — pessimistic MBRL via uncertainty-penalized reward (reward -= λ * model_uncertainty); generic model exploitation mitigation — reviewer defense: MOPO addresses distribution shift in offline MBRL, our dt=1 imagination restriction targets dt_embedding-induced delusional critic (temporal conditioning corruption), two complementary mechanisms\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n# ============================================================\\\\n# NEW: Value overestimation mitigation\\\\n# ============================================================\\\\n\\\\n- paper_id: thrun1993issues\\\\n  title: \\\\\\\"Issues in Using Function Approximation for Reinforcement Learning\\\\\\\"\\\\n  authors: [Thrun S., Schwartz A.]\\\\n  year: 1993\\\\n  venue: \\\\\\\"Connectionist Models Summer School\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"First identification of systematic value overestimation from function approximation; our delusional critic extends this to model-based imagination with temporal conditioning\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: vanhasselt2016double\\\\n  title: \\\\\\\"Deep Reinforcement Learning with Double Q-Learning\\\\\\\"\\\\n  authors: [van Hasselt H., Guez A., Silver D.]\\\\n  year: 2016\\\\n  venue: AAAI\\\\n  category: background\\\\n  role: \\\\\\\"Double DQN — mitigates overestimation via double estimator; our finding that trained dt-embedding enables value exploitation is a complementary overestimation mechanism in MBRL\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: fujimoto2018td3\\\\n  title: \\\\\\\"Addressing Function Approximation Error in Actor-Critic Methods\\\\\\\"\\\\n  authors: [Fujimoto S., van Hoof H., Meger D.]\\\\n  year: 2018\\\\n  venue: ICML\\\\n  category: method-component\\\\n  role: \\\\\\\"TD3 — clipped double-Q to limit overestimation in actor-critic; DreamerV3 uses a single critic, making it more vulnerable to the overestimation we identify\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: haarnoja2018sac\\\\n  title: \\\\\\\"Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor\\\\\\\"\\\\n  authors: [Haarnoja T., Zhou A., Abbeel P., Levine S.]\\\\n  year: 2018\\\\n  venue: ICML\\\\n  category: method-component\\\\n  role: \\\\\\\"SAC — entropy regularization implicitly mitigates overestimation; relevant contrast to DreamerV3's actor which can greedily exploit overestimated values\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: lee2021sunrise\\\\n  title: \\\\\\\"SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning\\\\\\\"\\\\n  authors: [Lee K., Laskin M., Srinivas A., Abbeel P.]\\\\n  year: 2021\\\\n  venue: ICML\\\\n  category: method-component\\\\n  role: \\\\\\\"Ensemble-based uncertainty weighting for value estimation; potential mitigation for our identified delusional critic mechanism\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: Delusional bias\\\\n# ============================================================\\\\n\\\\n- paper_id: lu2018nondelusional\\\\n  title: \\\\\\\"Non-delusional Q-learning and Value-Iteration\\\\\\\"\\\\n  authors: [Lu T., Schuurmans D., Boutilier C.]\\\\n  year: 2018\\\\n  venue: NeurIPS\\\\n  category: background\\\\n  role: \\\\\\\"Formalizes delusional bias from policy-class constraints in Q-learning; we identify an analogous phenomenon where temporal conditioning enables the critic to exploit model imprecision\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n# ============================================================\\\\n# NEW: Hierarchical RL with learned models\\\\n# ============================================================\\\\n\\\\n- paper_id: hafner2022director\\\\n  title: \\\\\\\"Deep Hierarchical Planning from Pixels\\\\\\\"\\\\n  authors: [Hafner D., Lee K.-H., Fischer I., Abbeel P.]\\\\n  year: 2022\\\\n  venue: NeurIPS\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"Director — hierarchical planning in Dreamer latent space via subgoals; addresses temporal abstraction through goal hierarchy rather than variable dt\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: nachum2018hiro\\\\n  title: \\\\\\\"Data-Efficient Hierarchical Reinforcement Learning\\\\\\\"\\\\n  authors: [Nachum O., Gu S., Lee H., Levine S.]\\\\n  year: 2018\\\\n  venue: NeurIPS\\\\n  category: background\\\\n  role: \\\\\\\"HIRO — off-policy HRL with learned subgoals; demonstrates that hierarchical temporal abstraction can improve sample efficiency when properly designed\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: Action repeat / frame skip\\\\n# ============================================================\\\\n\\\\n- paper_id: braylan2015frame\\\\n  title: \\\\\\\"Frame Skip Is a Powerful Parameter for Learning to Play Atari\\\\\\\"\\\\n  authors: [Braylan A., Hollenbeck M., Meyerson E., Miikkulainen R.]\\\\n  year: 2015\\\\n  venue: \\\\\\\"AAAI Workshop on Learning for General Competency in Video Games\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Empirical study showing frame skip strongly affects Atari performance; motivates investigation of temporal granularity as a critical design choice\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: lakshminarayanan2017dynamic\\\\n  title: \\\\\\\"Dynamic Action Repetition for Deep Reinforcement Learning\\\\\\\"\\\\n  authors: [Lakshminarayanan A.S., Sharma S., Ravindran B.]\\\\n  year: 2017\\\\n  venue: AAAI\\\\n  category: method-component\\\\n  role: \\\\\\\"Learns per-step action repetition duration; model-free analog of our variable-dt imagination approach\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: biedenkapp2021temporl\\\\n  title: \\\\\\\"TempoRL: Learning When to Act\\\\\\\"\\\\n  authors: [Biedenkapp A., Rajan R., Hutter F., Lindauer M.]\\\\n  year: 2021\\\\n  venue: ICML\\\\n  category: method-component\\\\n  role: \\\\\\\"Learns action persistence via skip-policy; demonstrates up to 10x speedup — but in model-free setting without the model exploitation risk we identify\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n# ============================================================\\\\n# NEW: DreamerV2\\\\n# ============================================================\\\\n\\\\n- paper_id: hafner2021dreamerv2\\\\n  title: \\\\\\\"Mastering Atari with Discrete World Models\\\\\\\"\\\\n  authors: [Hafner D., Lillicrap T., Norouzi M., Ba J.]\\\\n  year: 2021\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"DreamerV2 — introduces discrete latent representations used in DreamerV3; key architectural predecessor to our base system\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n# ============================================================\\\\n# NEW: Alternative world model architectures\\\\n# ============================================================\\\\n\\\\n- paper_id: micheli2023iris\\\\n  title: \\\\\\\"Transformers are Sample-Efficient World Models\\\\\\\"\\\\n  authors: [Micheli V., Alonso E., Fleuret F.]\\\\n  year: 2023\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"IRIS — autoregressive transformer world model; alternative to RSSM that may exhibit different compounding error characteristics under temporal abstraction\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: robine2023twm\\\\n  title: \\\\\\\"Transformer-based World Models Are Happy With 100k Interactions\\\\\\\"\\\\n  authors: [Robine J., Hoeftmann M., Uelwer T., Harmeling S.]\\\\n  year: 2023\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"TWM — Transformer-XL world model with direct state access; circumvents RSSM's recurrent compression that exacerbates our identified prediction gap\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: chen2022transdreamer\\\\n  title: \\\\\\\"TransDreamer: Reinforcement Learning with Transformer World Models\\\\\\\"\\\\n  authors: [Chen C., Wu Y.-F., Yoon J., Ahn S.]\\\\n  year: 2022\\\\n  venue: \\\\\\\"arXiv:2202.09481\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Replaces RSSM with Transformer State-Space Model; directly tests whether RSSM-specific architecture contributes to temporal abstraction failures\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: 2024-2026 concurrent work on temporal abstraction in world models\\\\n# ============================================================\\\\n\\\\n- paper_id: gumbsch2024thick\\\\n  title: \\\\\\\"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics\\\\\\\"\\\\n  authors: [Gumbsch C., Sajid N., Martius G., Butz M.V.]\\\\n  year: 2024\\\\n  venue: ICLR\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"THICK — learns adaptive temporal abstractions via context-change detection; closest concurrent work — addresses temporal abstraction in Dreamer but via hierarchy rather than variable-dt imagination\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: mattes2024hieros\\\\n  title: \\\\\\\"Hieros: Hierarchical Imagination on Structured State Space Sequence World Models\\\\\\\"\\\\n  authors: [Mattes P., Schlosser R., Herbrich R.]\\\\n  year: 2024\\\\n  venue: ICML\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n# ============================================================\\\\n# NEW: Seed-dependent instability & value overestimation in MBRL\\\\n# ============================================================\\\\n\\\\n- paper_id: henderson2018deep\\\\n  title: \\\\\\\"Deep Reinforcement Learning that Matters\\\\\\\"\\\\n  authors: [Henderson P., Islam R., Bachman P., Pineau J., Precup D., Meger D.]\\\\n  year: 2018\\\\n  venue: AAAI\\\\n  category: background\\\\n  role: \\\\\\\"Foundational study on seed variance in deep RL — shows statistically different performance distributions arise from random seeds alone with identical hyperparameters; directly supports our observation that seed 0 vs seed 2 produce qualitatively different value dynamics under the same dt_embed_dim=0 config\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: nikishin2022primacy\\\\n  title: \\\\\\\"The Primacy Bias in Deep Reinforcement Learning\\\\\\\"\\\\n  authors: [Nikishin E., Schwarzer M., D'Oro P., Bacon P.-L., Courville A.]\\\\n  year: 2022\\\\n  venue: ICML\\\\n  category: background\\\\n  role: \\\\\\\"Identifies primacy bias — agents overfit early data and lose ability to learn from new transitions, leading to delayed performance collapse; parallels our finding where value overestimation initially appears benign but becomes pathological later, and the collapse timing is seed-dependent\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: qiao2023mind\\\\n  title: \\\\\\\"Mind the Model, Not the Agent: The Primacy Bias in Model-based RL\\\\\\\"\\\\n  authors: [Qiao Z., Lyu J., Li X.]\\\\n  year: 2023\\\\n  venue: \\\\\\\"arXiv:2310.15017 (ECAI 2024)\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"Extends primacy bias to MBRL, testing on DreamerV2 — shows world model primacy bias dominates over agent primacy bias; directly relevant to Dreamer-family training instability and explains why some seeds recover (model escapes early overfitting) while others don't\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: hussing2024dissecting\\\\n  title: \\\\\\\"Dissecting Deep RL with High Update Ratios: Combatting Value Divergence\\\\\\\"\\\\n  authors: [Hussing M., Voelcker C.A., Gilitschenski I., Farahmand A.-M., Eaton E.]\\\\n  year: 2024\\\\n  venue: \\\\\\\"Reinforcement Learning Journal (RLC 2024)\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"Shows value overestimation and Q-divergence under high update-to-data ratios, driven by optimizer momentum — overestimation occurs on both in-distribution and OOD data; mechanism maps to our delusional critic where imagination-trained critic inflates values progressively, with divergence onset sensitive to initialization\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: barkley2024stealing\\\\n  title: \\\\\\\"Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning\\\\\\\"\\\\n  authors: [Barkley B., Fridovich-Keil D.]\\\\n  year: 2024\\\\n  venue: \\\\\\\"arXiv:2412.14312 (ICML 2025)\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"Demonstrates that synthetic rollouts (imagination) can degrade performance inconsistently across environments, with overestimation bias as a contributing factor; supports our finding that imagination-based training creates environment- and seed-dependent failure modes that existing mitigation techniques do not reliably fix\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: bjorck2022variance\\\\n  title: \\\\\\\"Is High Variance Unavoidable in RL? A Case Study in Continuous Control\\\\\\\"\\\\n  authors: [Bjorck J., Gomes C.P., Weinberger K.Q.]\\\\n  year: 2022\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"Shows RL variance mostly arises early in training from poor 'outlier' runs caused by numerical instability; parallels our observation that seed 2 diverges early while seed 0 recovers — the reward prediction degradation from removing dt_embedding may create exactly this early-training instability\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: Reward prediction quality → MBRL performance\\\\n# ============================================================\\\\n# Our key finding: removing dt_embedding causes reward_MAE to spike 75x\\\\n# (0.01 → 0.747), making performance seed-dependent. These papers\\\\n# establish that reward prediction quality is a known MBRL bottleneck.\\\\n\\\\n- paper_id: lee2024dreamsmooth\\\\n  title: \\\\\\\"DreamSmooth: Improving Model-based Reinforcement Learning via Reward Smoothing\\\\\\\"\\\\n  authors: [Lee V., Abbeel P., Lee Y.]\\\\n  year: 2024\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"Directly demonstrates reward prediction is a bottleneck in MBRL — sparse/ambiguous rewards cause the reward model to predict zeros, creating gradient-free landscapes during imagination; our dt_embed_dim=0 ablation creates an analogous bottleneck where the reward head loses temporal conditioning and MAE spikes 75x\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: ma2024harmonydream\\\\n  title: \\\\\\\"HarmonyDream: Task Harmonization Inside World Models\\\\\\\"\\\\n  authors: [Ma H., Wu J., Feng N., Xiao C., Li D., Hao J., Wang J., Long M.]\\\\n  year: 2024\\\\n  venue: ICML\\\\n  category: background\\\\n  role: \\\\\\\"Shows observation prediction dominates reward prediction in world model training, degrading reward model quality; proposes dynamic loss balancing for 10-69% gains — directly relevant to our finding that dt_embedding removal disrupts the observation-reward prediction balance and causes reward MAE explosion\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: lambert2020objective\\\\n  title: \\\\\\\"Objective Mismatch in Model-based Reinforcement Learning\\\\\\\"\\\\n  authors: [Lambert N., Amos B., Yadan O., Calandra R.]\\\\n  year: 2020\\\\n  venue: \\\\\\\"L4DC (Proceedings of Machine Learning Research, vol. 120)\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Formalizes that one-step prediction likelihood does not correlate with control performance — the 'objective mismatch' problem; our work reveals a specific instance: the reward head's prediction accuracy (measured by MAE) directly gates whether the critic can learn stable value estimates, creating a reward-specific objective mismatch\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n# ============================================================\\\\n# NEW: Auxiliary tasks & representation coupling in world models\\\\n# ============================================================\\\\n# Our finding: reward prediction quality is tightly coupled to temporal\\\\n# conditioning (dt_embedding). Removing the embedding degrades the\\\\n# reward head while dynamics remain intact — suggesting the reward head\\\\n# acts as more than a passive predictor; it conditions the shared\\\\n# representation. Literature gap: no prior work studies this coupling\\\\n# specifically in Dreamer-family world models.\\\\n\\\\n- paper_id: jaderberg2017unreal\\\\n  title: \\\\\\\"Reinforcement Learning with Unsupervised Auxiliary Tasks\\\\\\\"\\\\n  authors: [Jaderberg M., Mnih V., Czarnecki W.M., Schaul T., Leibo J.Z., Silver D., Kavukcuoglu K.]\\\\n  year: 2017\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"UNREAL — introduces reward prediction as an auxiliary task that shapes shared representations; foundational evidence that reward prediction is not just a passive output but actively conditions what features the network learns — our finding that removing dt_embedding selectively degrades reward prediction (but not dynamics) suggests the temporal conditioning specifically enables reward-relevant feature extraction\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: lyle2021auxiliary\\\\n  title: \\\\\\\"On The Effect of Auxiliary Tasks on Representation Dynamics\\\\\\\"\\\\n  authors: [Lyle C., Rowland M., Ostrovski G., Dabney W.]\\\\n  year: 2021\\\\n  venue: AISTATS\\\\n  category: background\\\\n  role: \\\\\\\"Theoretical analysis showing auxiliary tasks shape representations toward top eigenvectors of the transition operator; provides formal grounding for why removing temporal conditioning from the reward head could alter the entire representation — the reward head's gradients contribute to spectral structure of the shared latent space\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n# ============================================================\\\\n# NEW: DreamerV3 architecture improvements (2025-2026)\\\\n# ============================================================\\\\n\\\\n- paper_id: bredis2026nedreamer\\\\n  title: \\\\\\\"Next Embedding Prediction Makes World Models Stronger\\\\\\\"\\\\n  authors: [Bredis G., Balagansky N., Gavrilov D., Rakhimov R.]\\\\n  year: 2026\\\\n  venue: \\\\\\\"arXiv:2603.02765\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"NE-Dreamer — decoder-free MBRL replacing pixel reconstruction with next-embedding prediction via temporal transformer + Barlow Twins; improves RSSM prediction quality on DMC and DMLab but does not address temporal abstraction or delusional critic — orthogonal to our dt-embedding diagnosis\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: zhang2025dymodreamer\\\\n  title: \\\\\\\"DyMoDreamer: World Modeling with Dynamic Modulation\\\\\\\"\\\\n  authors: [Zhang B., Wang R., Xiao W., Zhang W., Sun J., Huang G., Chen J., Wang G.]\\\\n  year: 2025\\\\n  venue: NeurIPS\\\\n  category: background\\\\n  role: \\\\\\\"Modulates RSSM via inter-frame differencing mask and stochastic categorical dynamic modulation; SOTA on Atari 100k (156.6% HNS) and DMC (832) — improves dynamics extraction but does not address variable-rate imagination or dt_embedding-induced value overestimation\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: Temporal abstraction methods\\\\n# ============================================================\\\\n\\\\n- paper_id: liu2025vanta\\\\n  title: \\\\\\\"Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning\\\\\\\"\\\\n  authors: [Liu T.-S., Liu X.-H., Chen R., Jin L., Wang P., Zhang Z., Yu Y.]\\\\n  year: 2025\\\\n  venue: ICLR\\\\n  category: method-component\\\\n  role: \\\\\\\"VanTA — VLM-guided trajectory decomposition into semantically meaningful skills via vector quantization + relabeling; operates at high-level skill abstraction (Franka Kitchen, Crafter) — contrasts with our low-level dt-based temporal abstraction within world-model imagination steps\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: Evaluation methodology\\\\n# ============================================================\\\\n\\\\n- paper_id: agarwal2021precipice\\\\n  title: \\\\\\\"Deep Reinforcement Learning at the Edge of the Statistical Precipice\\\\\\\"\\\\n  authors: [Agarwal R., Schwarzer M., Castro P.S., Courville A.C., Bellemare M.]\\\\n  year: 2021\\\\n  venue: NeurIPS\\\\n  category: evaluation\\\\n  role: \\\\\\\"Proposes rliable — interval estimates, performance profiles, IQM for robust multi-seed RL evaluation (NeurIPS Outstanding Paper); our multi-seed experiment design follows this methodology to ensure statistical validity of collapse detection across seeds\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n# ============================================================\\\\n# NEW (2026-05-14 gap analysis): Time discretization theory\\\\n# ============================================================\\\\n# Gap: variable timestep / time discretization invariance — foundational\\\\n# theory for why dt matters and how to handle it.\\\\n\\\\n- paper_id: tallec2019making\\\\n  title: \\\\\\\"Making Deep Q-learning methods Robust to Time Discretization\\\\\\\"\\\\n  authors: [Tallec C., Blier L., Ollivier Y.]\\\\n  year: 2019\\\\n  venue: \\\\\\\"ICML (arXiv:1901.09732)\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Shows Q-learning performance is highly sensitive to time discretization δ; proposes architectural + exploration modifications for δ-invariance. Theoretical foundation for why our variable-dt imagination introduces a fundamental difficulty: RSSM trained at δ=1 cannot produce δ-invariant predictions at dt>1\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: park2021sar\\\\n  title: \\\\\\\"Time Discretization-Invariant Safe Action Repetition for Policy Gradient Methods\\\\\\\"\\\\n  authors: [Park S., Kim J., Kim G.]\\\\n  year: 2021\\\\n  venue: \\\\\\\"NeurIPS (arXiv:2111.03941)\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"SAR — δ-invariant action repetition for policy gradients; achieves time-discretization robustness in model-free RL via adaptive reaction to state changes during repetition. Contrasts with our finding that world-model RL lacks this robustness when imagination uses dt>1\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: wang2024seac\\\\n  title: \\\\\\\"Reinforcement Learning with Elastic Time Steps\\\\\\\"\\\\n  authors: [Wang D., Beltrame G.]\\\\n  year: 2024\\\\n  venue: \\\\\\\"arXiv:2402.14961\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"SEAC/MOSEAC — variable-duration time steps where agent selects both action and duration; model-free approach that explicitly treats action duration as part of the action space. Our work reveals why this strategy is problematic in world-model RL: the critic cannot reliably evaluate variable-duration imagined trajectories\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW (2026-05-14 gap analysis): Delusional bias mitigation\\\\n# ============================================================\\\\n\\\\n- paper_id: su2020conqur\\\\n  title: \\\\\\\"ConQUR: Mitigating Delusional Bias in Deep Q-learning\\\\\\\"\\\\n  authors: [Su D., Ooi J., Lu T., Schuurmans D., Boutilier C.]\\\\n  year: 2020\\\\n  venue: \\\\\\\"ICML (arXiv:2002.12399)\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Follow-up to Lu et al. 2018; mitigates delusional bias via consistency-penalized Q-labels. Addresses delusional bias from policy-class constraints in Q-learning; our delusional critic is an analogous phenomenon in MBRL where temporal conditioning (dt_embedding) creates inconsistent value targets across imagination steps\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n# ============================================================\\\\n# NEW (2026-05-14 gap analysis): Diagnostic methodology in RL\\\\n# ============================================================\\\\n# Gap: our paper is a diagnostic analysis — need methodological\\\\n# precedents for \\\\\\\"what matters\\\\\\\" / \\\\\\\"implementation matters\\\\\\\" style papers.\\\\n\\\\n- paper_id: engstrom2020implementation\\\\n  title: \\\\\\\"Implementation Matters in Deep Policy Gradients: A Case Study on PPO and TRPO\\\\\\\"\\\\n  authors: [Engstrom L., Ilyas A., Santurkar S., Tsipras D., Janoos F., Rudolph L., Madry A.]\\\\n  year: 2020\\\\n  venue: \\\\\\\"ICLR (arXiv:2005.12729)\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"Demonstrates that code-level implementation details (not algorithmic innovations) drive most of PPO's gains over TRPO; methodological precedent for our diagnostic approach — we similarly show that a specific implementation choice (trained vs. untrained dt_embedding) is the primary factor determining collapse vs. stability\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: andrychowicz2021whatmatters\\\\n  title: \\\\\\\"What Matters for On-Policy Deep Actor-Critic Methods? A Large-Scale Study\\\\\\\"\\\\n  authors: [Andrychowicz M., Raichuk A., Stańczyk P., Orsini M., Girgin S., Marinier R., Hussenot L., Geist M., Pietquin O., Michalski M., Gelly S., Bachem O.]\\\\n  year: 2021\\\\n  venue: \\\\\\\"ICLR (arXiv:2006.05990)\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"Large-scale factorial study of 50+ design choices in on-policy RL (250K+ agents); methodological template for our factorial experiment design isolating dt_embedding × subsample × horizon effects. Demonstrates that systematic ablation reveals non-obvious interactions — parallel to our finding that dt_embedding training status interacts with subsample and horizon\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n# ============================================================\\\\n# NEW (2026-05-14 gap analysis): MBRL rollout quality & value overestimation\\\\n# ============================================================\\\\n# Gap: recent ICLR 2025 papers directly studying imagination rollout\\\\n# quality and value overestimation in model-based settings.\\\\n\\\\n- paper_id: frauenknecht2025rollouts\\\\n  title: \\\\\\\"On Rollouts in Model-Based Reinforcement Learning\\\\\\\"\\\\n  authors: [Frauenknecht B., Subhasish D., Solowjow F., Trimpe S.]\\\\n  year: 2025\\\\n  venue: \\\\\\\"ICLR (arXiv:2501.16918)\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"Shows trajectory-sampling rollouts diverge from ground truth after few steps and can harm policy learning; proposes Infoprop separating aleatoric/epistemic uncertainty with rollout termination criteria. Directly supports our finding that dt>1 imagination produces corrupted data — our work identifies a specific mechanism (dt_embedding-induced value exploitation) beyond general compounding error\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: voelcker2025madtd\\\\n  title: \\\\\\\"MAD-TD: Model-Augmented Data stabilizes High Update Ratio RL\\\\\\\"\\\\n  authors: [Voelcker C., Hussing M., Eaton E., Farahmand A.-M., Gilitschenski I.]\\\\n  year: 2025\\\\n  venue: \\\\\\\"ICLR (arXiv:2410.08896)\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"Shows value function misgeneralization to on-policy actions causes instability at high UTD ratios; uses model-generated data to improve value accuracy. Complementary to our finding: MAD-TD addresses value misgeneralization from replay distribution mismatch, we address value overestimation from temporal conditioning corruption in imagination\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n# ============================================================\\\\n# NEW (2026-05-14 gap analysis): Latest action repeat methods\\\\n# ============================================================\\\\n\\\\n- paper_id: nie2025sdar\\\\n  title: \\\\\\\"Select before Act: Spatially Decoupled Action Repetition for Continuous Control\\\\\\\"\\\\n  authors: [Nie B., et al.]\\\\n  year: 2025\\\\n  venue: \\\\\\\"ICLR (arXiv:2502.06919)\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"SDAR — per-dimension action repetition decisions for flexible temporal persistence in model-free RL; SOTA on DMC continuous control. Advances action repeat in model-free setting; our work shows the fundamental obstacle to analogous variable-rate approaches in model-based RL (delusional critic from dt_embedding)\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW (2026-05-14 gap analysis): DreamerV4 / latest Dreamer evolution\\\\n# ============================================================\\\\n\\\\n- paper_id: hafner2025dreamerv4\\\\n  title: \\\\\\\"Training Agents Inside of Scalable World Models\\\\\\\"\\\\n  authors: [Hafner D., Yan W.]\\\\n  year: 2025\\\\n  venue: \\\\\\\"arXiv:2509.24527\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"DreamerV4 — replaces RSSM with efficient transformer world model + shortcut forcing; scales to video pretraining (Minecraft diamonds from video). Architectural successor to DreamerV3; our dt_embedding diagnosis is specific to RSSM but the broader lesson (temporal conditioning must match model fidelity) applies to transformer world models\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n# ============================================================\\\\n# NEW (2026-05-14): Training instability dynamics\\\\n# ============================================================\\\\n\\\\n- paper_id: zhang2026instability\\\\n  title: \\\\\\\"Training instability in deep learning follows low-dimensional dynamical principles\\\\\\\"\\\\n  authors: [Zhang L., et al.]\\\\n  year: 2026\\\\n  venue: \\\\\\\"ICLR 2026 (arXiv:2601.13160)\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Training instability follows low-dimensional dynamical principles; provides theoretical framework for why seed-dependent collapse vs self-correction occurs in our experiments (008d seed 1 collapses, 009b seed 2 self-corrects under identical config)\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n# ============================================================\\\\n# NEW (2026-05-14): Seed-Dependent Stochastic Outcomes in MBRL\\\\n# ============================================================\\\\n# Dedicated literature survey for the stochastic collapse phenomenon:\\\\n# same config (trained dt_embedding + subsample + H=8) produces\\\\n# collapse in seed 0 (008d) but self-correction in seed 2 (009b).\\\\n# nve>1.5x is a 100% reliable marker of trained dt_embedding,\\\\n# but collapse itself is stochastic (1/2 seeds).\\\\n\\\\n- paper_id: sokar2023dormant\\\\n  title: \\\\\\\"The Dormant Neuron Phenomenon in Deep Reinforcement Learning\\\\\\\"\\\\n  authors: [Sokar G., Agarwal R., Castro P.S., Evci U.]\\\\n  year: 2023\\\\n  venue: \\\\\\\"ICML 2023\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Identifies dormant neurons — inactive units accumulating during RL training that reduce network expressivity. Seed-dependent because different random initializations produce different early dormancy patterns; directly explains why some seeds lose the representational capacity needed to self-correct value overestimation (our seed 0 collapses) while others retain enough active neurons to recover (our seed 2 self-corrects)\\\\\\\"\\\\n  relevance_score: 4\\\\n  survey_tag: seed-dependent-stochastic-outcomes\\\\n\\\\n- paper_id: lyle2022capacity\\\\n  title: \\\\\\\"Understanding and Preventing Capacity Loss in Reinforcement Learning\\\\\\\"\\\\n  authors: [Lyle C., Rowland M., Dabney W.]\\\\n  year: 2022\\\\n  venue: \\\\\\\"ICLR 2023 (arXiv:2204.09560)\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Shows feature rank collapse from non-stationary TD targets is a necessary condition for learning failure but not sufficient — sparse rewards and other factors must co-occur. Directly parallels our finding: nve>1.5x (value overestimation from trained dt_embedding) is a necessary precondition for collapse but not a sufficient one; additional stochastic factors (initialization, early replay composition) determine whether collapse actually occurs\\\\\\\"\\\\n  relevance_score: 5\\\\n  survey_tag: seed-dependent-stochastic-outcomes\\\\n\\\\n- paper_id: kumar2022dr3\\\\n  title: \\\\\\\"DR3: Value-Based Deep Reinforcement Learning Requires Explicit Regularization\\\\\\\"\\\\n  authors: [Kumar A., Agarwal R., Ma T., Courville A., Tucker G., Levine S.]\\\\n  year: 2022\\\\n  venue: \\\\\\\"ICLR 2022\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Shows implicit regularization from TD learning favors degenerate feature aliasing (states on both sides of Bellman backup become indistinguishable), creating the substrate for value overestimation. In our setting, trained dt_embedding amplifies this aliasing across different temporal horizons — the critic cannot distinguish between dt=1 and dt>1 value targets, enabling exploitation. Feature aliasing is seed-dependent because it depends on initialization geometry\\\\\\\"\\\\n  relevance_score: 4\\\\n  survey_tag: seed-dependent-stochastic-outcomes\\\\n\\\\n- paper_id: colas2018seeds\\\\n  title: \\\\\\\"How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments\\\\\\\"\\\\n  authors: [Colas C., Sigaud O., Oudeyer P.-Y.]\\\\n  year: 2018\\\\n  venue: \\\\\\\"arXiv:1806.08295\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"Provides statistical framework for determining seed count needed for significant algorithm comparison; our 2-seed observation (1/2 collapse) has limited statistical power by their analysis — but the qualitative difference (nve 4.12x vs 0.38x) is large enough that even 2 seeds establish the stochastic nature of the phenomenon. Methodological basis for future multi-seed validation\\\\\\\"\\\\n  relevance_score: 3\\\\n  survey_tag: seed-dependent-stochastic-outcomes\\\\n\\\\n- paper_id: nikishin2023plasticity\\\\n  title: \\\\\\\"Deep Reinforcement Learning with Plasticity Injection\\\\\\\"\\\\n  authors: [Nikishin E., Oh J., Ostrovski G., Lyle C., Pascanu R., Dabney W., Barreto A.]\\\\n  year: 2023\\\\n  venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"Plasticity injection augments network plasticity without changing parameter count; serves as a diagnostic tool — if injection improves performance, plasticity loss was the bottleneck. Directly applicable to diagnosing whether our seed-dependent collapse is plasticity-mediated: if plasticity injection prevents collapse in seed 0 but has no effect on seed 2 (which already self-corrects), it confirms plasticity loss as the bifurcation mechanism\\\\\\\"\\\\n  relevance_score: 4\\\\n  survey_tag: seed-dependent-stochastic-outcomes\\\\n\\\\n- paper_id: schwarzer2023bbf\\\\n  title: \\\\\\\"Bigger, Better, Faster: Human-level Atari with Human-level Efficiency\\\\\\\"\\\\n  authors: [Schwarzer M., Obando-Ceron J.S., Courville A., Bellemare M., Agarwal R., Castro P.S.]\\\\n  year: 2023\\\\n  venue: \\\\\\\"ICML 2023\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"BBF achieves SOTA sample efficiency via periodic network resets + scaling + weight decay; periodic resets prevent primacy bias accumulation across seeds. Suggests our delusional critic collapse might be preventable with periodic critic resets — the reset would break the positive feedback loop between overestimated values and actor exploitation before it becomes irreversible\\\\\\\"\\\\n  relevance_score: 3\\\\n  survey_tag: seed-dependent-stochastic-outcomes\\\\n\\\\n- paper_id: farebrother2024stopregressing\\\\n  title: \\\\\\\"Stop Regressing: Training Value Functions via Classification for Scalable Deep RL\\\\\\\"\\\\n  authors: [Farebrother J., Orbay J., Vuong Q., Taiga A.A., Chebotar Y., Xiao T., Irpan A., Levine S., Castro P.S., Faust A., Kumar A., Agarwal R.]\\\\n  year: 2024\\\\n  venue: \\\\\\\"ICML 2024\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"Shows categorical cross-entropy for value training provides implicit regularization against overestimation vs MSE regression. DreamerV3 already uses categorical value prediction (twohot + symlog) — yet our trained dt_embedding still induces collapse in some seeds, demonstrating that categorical value training is insufficient to prevent dt_embedding-induced value exploitation\\\\\\\"\\\\n  relevance_score: 3\\\\n  survey_tag: seed-dependent-stochastic-outcomes\\\\n\\\\n- paper_id: lyle2024normalization\\\\n  title: \\\\\\\"Normalization and Effective Learning Rates in Reinforcement Learning\\\\\\\"\\\\n  authors: [Lyle C., Zheng Z., Giunchiglia E., Sherstan C., Hashemizadeh M., Schuurmans D., Dabney W.]\\\\n  year: 2024\\\\n  venue: \\\\\\\"NeurIPS 2024\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Shows normalization layers combat overestimation but cause effective learning rate decay via parameter norm growth. Provides a potential mechanism for seed 2's self-correction: if parameter norms grow faster in certain initializations, effective LR decays faster, naturally damping value overestimation before it cascades into collapse. Seed 0's slower norm growth → sustained high effective LR → overestimation compounds → collapse\\\\\\\"\\\\n  relevance_score: 4\\\\n  survey_tag: seed-dependent-stochastic-outcomes\\\\n\\\\n# --- Survey synthesis: Seed-Dependent Stochastic Outcomes ---\\\\n# Summary (2026-05-14):\\\\n#\\\\n# 1. STOCHASTIC COLLAPSE HAS PRECEDENT:\\\\n#    Plasticity loss (Lyle 2022, Sokar 2023, Nikishin 2023) is inherently\\\\n#    seed-dependent because it depends on initialization → early gradient\\\\n#    dynamics → neuron activity patterns. Different seeds hit different\\\\n#    plasticity trajectories under identical configs.\\\\n#\\\\n# 2. nve>1.5x AS DIAGNOSTIC MARKER (necessary but not sufficient):\\\\n#    Lyle 2022 shows feature rank collapse is necessary but not sufficient\\\\n#    for learning failure. Kumar 2022 shows feature aliasing from TD\\\\n#    learning creates the overestimation substrate. Our nve>1.5x is\\\\n#    analogous: it indicates the dt_embedding has enabled value exploitation\\\\n#    (100% reliable marker), but collapse requires additional conditions\\\\n#    (plasticity loss, insufficient effective LR decay) that are stochastic.\\\\n#\\\\n# 3. SELF-CORRECTION MECHANISM:\\\\n#    Lyle 2024 provides a candidate mechanism: normalization-induced\\\\n#    effective LR decay can naturally damp overestimation in some seeds.\\\\n#    Farebrother 2024 shows categorical value training provides partial\\\\n#    implicit regularization. Together these explain why seed 2 self-corrects:\\\\n#    the combination of DreamerV3's categorical critic + normalization +\\\\n#    favorable initialization produces enough implicit regularization to\\\\n#    overcome the dt_embedding-induced overestimation.\\\\n#\\\\n# 4. THEORETICAL GROUNDING:\\\\n#    Zhang 2026 (already in map) provides the dynamical systems framework.\\\\n#    Bjorck 2022 (already in map) shows early outlier events dominate\\\\n#    variance. Together with the new papers, the framing is:\\\\n#    \\\\\\\"trained dt_embedding creates a necessary condition (nve>1.5x) for\\\\n#    delusional critic collapse, but collapse is a stochastic bifurcation\\\\n#    whose outcome depends on seed-dependent plasticity dynamics.\\\\\\\"\\\\n\\\\n# ============================================================\\\\n# INCREMENTAL SCAN (2026-05-14): Δt conditioning & adaptive horizon\\\\n# ============================================================\\\\n# 8 new papers from targeted search on:\\\\n#   - Δt/timestep conditioning in world models\\\\n#   - Variable-rate imagination / adaptive horizon\\\\n#   - Hierarchical planning with latent world models (2025-2026)\\\\n#\\\\n# KEY FINDING: TAWM (Nhu et al. ICML 2025) explicitly conditions\\\\n# world model on Δt — closest methodological overlap. But TAWM\\\\n# uses TD-MPC2 (online MPC) not imagination-based actor-critic,\\\\n# and treats Δt conditioning as beneficial. Our work diagnoses\\\\n# Δt conditioning as pathological in imagination-based training\\\\n# (delusional critic). Complementary, not duplicative.\\\\n\\\\n- paper_id: nhu2025tawm\\\\n  title: \\\\\\\"Time-Aware World Model for Adaptive Prediction and Control\\\\\\\"\\\\n  authors: [Nhu A.N., Son S., Lin M.C.]\\\\n  year: 2025\\\\n  venue: \\\\\\\"ICML 2025 (arXiv:2506.08441)\\\\\\\"\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"TAWM — explicitly conditions world model on time-step size Δt and trains over diverse Δt values for multi-rate dynamics learning. Built on TD-MPC2 (online MPC). KEY DISTINCTION from our work: (1) TAWM treats Δt conditioning as beneficial for performance/data-efficiency; we diagnose it as pathological in imagination-based actor-critic training (delusional critic). (2) TAWM uses MPC (no imagination rollouts for policy training); our failure mode is specific to imagination-based training where the critic exploits dt-conditioned value estimates. (3) TAWM focuses on observation-rate robustness; we focus on value overestimation from temporal conditioning corruption. TAWM actually strengthens our contribution: it shows Δt conditioning works in MPC settings, making our finding that it fails in imagination-based settings a surprising and important diagnostic.\\\\\\\"\\\\n  relevance_score: 5\\\\n  novelty_threat: \\\\\\\"MEDIUM — methodological overlap (Δt conditioning) but fundamentally different paradigm (MPC vs imagination) and opposite conclusion (beneficial vs pathological). Must cite and differentiate in paper.\\\\\\\"\\\\n\\\\n- paper_id: li2025lsimagine\\\\n  title: \\\\\\\"Open-World Reinforcement Learning over Long Short-Term Imagination\\\\\\\"\\\\n  authors: [Li J., Wang Q., Wang Y., Jin X., Li Y., Zeng W., Yang X.]\\\\n  year: 2025\\\\n  venue: \\\\\\\"ICLR 2025 Oral (arXiv:2410.03618)\\\\\\\"\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"LS-Imagine — extends imagination horizon in Dreamer via goal-conditioned jumpy state transitions and affordance maps. Addresses the 'short-sightedness' of standard Dreamer imagination. KEY DISTINCTION: LS-Imagine adds jumpy transitions to reach long-horizon targets (open-world Minecraft), while our work shows that variable-dt imagination itself introduces delusional critic. LS-Imagine's jumpy transitions use goal conditioning (not dt-embedding), potentially avoiding the value overestimation we identify.\\\\\\\"\\\\n  relevance_score: 4\\\\n  novelty_threat: \\\\\\\"LOW — different mechanism (goal-conditioned jumps vs dt-embedding) and different focus (long-horizon exploration vs diagnostic of failure modes). Should cite as concurrent approach to extending imagination horizon.\\\\\\\"\\\\n\\\\n- paper_id: zhang2026hwm\\\\n  title: \\\\\\\"Hierarchical Planning with Latent World Models\\\\\\\"\\\\n  authors: [Zhang W., Terver B., Zholus A., Chitnis S., Sutaria H., Assran M., Balestriero R., Bar A., Bardes A., LeCun Y., Ballas N.]\\\\n  year: 2026\\\\n  venue: \\\\\\\"arXiv:2604.03208\\\\\\\"\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"HWM — learns multi-scale latent world models for hierarchical MPC planning; high-level planner optimizes macro-actions, low-level planner handles primitives. 70% success on real-world non-greedy robotic tasks vs 0% for single-level. Addresses temporal abstraction via hierarchical planning (MPC), not imagination-based actor-critic. Further evidence that temporal abstraction in world models requires hierarchy rather than single-scale variable-dt approaches.\\\\\\\"\\\\n  relevance_score: 4\\\\n  novelty_threat: \\\\\\\"LOW — MPC-based hierarchical planning, not imagination-based training. Supports our thesis that flat dt-embedding approaches are inferior to hierarchical alternatives.\\\\\\\"\\\\n\\\\n- paper_id: kobayashi2025metacontroller\\\\n  title: \\\\\\\"Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning\\\\\\\"\\\\n  authors: [Kobayashi S., et al.]\\\\n  year: 2025\\\\n  venue: \\\\\\\"arXiv:2512.20605\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"MetaController — discovers temporal abstractions via higher-order non-causal sequence model controlling base autoregressive model's residual stream. Each controller executes behaviorally meaningful action sequences with learned termination conditions. Operates in fundamentally different paradigm (LLM-style autoregressive models, not world-model imagination), but demonstrates that temporal abstraction benefits from hierarchical structure rather than flat dt-conditioning.\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: shaj2023mts3\\\\n  title: \\\\\\\"Multi Time Scale World Models\\\\\\\"\\\\n  authors: [Shaj V., Gholam Zadeh S., Demir O., Luettjohann L., Neumann G., Toussaint M.]\\\\n  year: 2023\\\\n  venue: \\\\\\\"NeurIPS 2023 (arXiv:2310.18534)\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"MTS3 — probabilistic multi-time-scale state space model with fast and slow latent dynamics for variable-rate prediction. Provides efficient inference across temporal scales. Foundational multi-rate dynamics architecture; our work shows that even with proper multi-rate modeling, the downstream actor-critic training in imagination can exploit temporal conditioning for value overestimation — a failure mode MTS3 does not address (it focuses on prediction quality, not policy training).\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: splates2025\\\\n  title: \\\\\\\"Stable Planning with Temporally Extended Skills\\\\\\\"\\\\n  authors: [SPlaTES authors]\\\\n  year: 2025\\\\n  venue: \\\\\\\"Reinforcement Learning Journal (RLC 2025)\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"SPlaTES — hierarchical MPC with temporally extended skills + abstract skill world model. Skill learning via mutual-information objective yields diverse, predictable, task-related behavior. Demonstrates that stable long-horizon planning requires modeling skill outcomes (temporal abstraction via hierarchy), not primitive-action outcomes at variable time steps — consistent with our finding that flat dt-embedding fails.\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: beckerehmck2023multitimestep\\\\n  title: \\\\\\\"Multi-timestep models for Model-based Reinforcement Learning\\\\\\\"\\\\n  authors: [Becker-Ehmck P., Peters J., van der Smagt P.]\\\\n  year: 2023\\\\n  venue: \\\\\\\"arXiv:2310.05672\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Proposes multi-timestep training objective (weighted sum of losses at various future horizons) for one-step dynamics models to improve long-horizon R² score. Addresses compounding error at the model training level; our work shows that even with perfect multi-step prediction, the imagination-based actor-critic can still fail due to value overestimation from dt-conditioning — a downstream failure mode distinct from prediction accuracy.\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: liu2022dmve\\\\n  title: \\\\\\\"Dynamic-Horizon Model-Based Value Estimation With Latent Imagination\\\\\\\"\\\\n  authors: [Liu Y., et al.]\\\\n  year: 2022\\\\n  venue: \\\\\\\"IEEE TNNLS (arXiv:2009.09593)\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"DMVE — adaptive rollout horizon selection via horizon reliability detection (comparing value expansion errors between raw and reconstructed observations). Addresses the horizon selection problem in imagination-based value estimation. Complementary to our work: DMVE selects among fixed-dt horizons; we show that even optimal horizon selection cannot fix the delusional critic when dt-embedding is trained (the overestimation is in the value function, not the horizon length).\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# --- Incremental scan synthesis (2026-05-14) ---\\\\n#\\\\n# NOVELTY ASSESSMENT:\\\\n# No paper found that diagnoses dt_embedding → delusional critic\\\\n# (value overestimation) → stochastic collapse in imagination-based\\\\n# MBRL. Our core contribution remains novel.\\\\n#\\\\n# TAWM (ICML 2025) is the closest methodological overlap but\\\\n# operates in MPC paradigm and reaches opposite conclusion\\\\n# (Δt conditioning is beneficial). This actually STRENGTHENS\\\\n# our novelty: \\\\\\\"Δt conditioning helps in MPC but hurts in\\\\n# imagination-based training\\\\\\\" is a more nuanced and surprising finding.\\\\n#\\\\n# LANDSCAPE TREND:\\\\n# The field is converging on HIERARCHY (THICK, Hieros, Director,\\\\n# HWM, SPlaTES, MetaController) as the solution to temporal\\\\n# abstraction in world models, avoiding flat variable-dt approaches.\\\\n# Our diagnostic paper explains WHY flat dt approaches fail,\\\\n# providing theoretical grounding for this empirical trend.\\\\n#\\\\n# ACTION ITEMS FOR PAPER:\\\\n# 1. MUST CITE: nhu2025tawm — differentiate MPC vs imagination paradigm\\\\n# 2. SHOULD CITE: li2025lsimagine — concurrent Dreamer horizon extension\\\\n# 3. SHOULD CITE: shaj2023mts3 — multi-rate dynamics foundation\\\\n# 4. CONSIDER: zhang2026hwm — latest hierarchical WM planning\\\\n\\\", \\\"total_chars\\\": 50497, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml\", \"content\": \"# Literature Map — event-gated-adaptive-horizon\\n# Last updated: 2026-05-14\\n# Total: 72 papers (64 existing + 8 incremental scan 2026-05-14)\\n\\n# ============================================================\\n# EXISTING CITATIONS (already in paper.tex)\\n# ============================================================\\n\\n- paper_id: sutton1999options\\n  title: \\\"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\\\"\\n  authors: [Sutton R.S., Precup D., Singh S.]\\n  year: 1999\\n  venue: \\\"Artificial Intelligence 112(1-2):181-211\\\"\\n  category: background\\n  role: \\\"Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL\\\"\\n  relevance_score: 5\\n\\n- paper_id: hafner2020dreamerv1\\n  title: \\\"Dream to Control: Learning Behaviors by Latent Imagination\\\"\\n  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]\\n  year: 2020\\n  venue: ICLR\\n  category: background\\n  role: \\\"DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm\\\"\\n  relevance_score: 5\\n\\n- paper_id: hafner2023dreamerv3\\n  title: \\\"Mastering Diverse Domains through World Models\\\"\\n  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]\\n  year: 2023\\n  venue: \\\"arXiv:2301.04104 (Nature 2025)\\\"\\n  category: background\\n  role: \\\"DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here\\\"\\n  relevance_score: 5\\n\\n- paper_id: sharma2017figar\\n  title: \\\"Fine Grained Action Repetition for Deep Reinforcement Learning\\\"\\n  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]\\n  year: 2017\\n  venue: \\\"ICLR Workshop\\\"\\n  category: method-component\\n  role: \\\"FiGAR — learns action-repeat durations in model-free RL; we extend the idea to imagination step size in world-model RL\\\"\\n  relevance_score: 4\\n\\n- paper_id: janner2019mbpo\\n  title: \\\"When to Trust Your Model: Model-Based Policy Optimization\\\"\\n  authors: [Janner M., Fu J., Zhang M., Levine S.]\\n  year: 2019\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"MBPO — formalizes model exploitation in MBRL; our delusional critic is a specific instance of model exploitation tied to temporal embedding\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW: Multi-step prediction error compounding\\n# ============================================================\\n\\n- paper_id: ke2019learning\\n  title: \\\"Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future\\\"\\n  authors: [Ke N.R., Singh A., Touati A., Goyal A., Bengio Y., Parikh D., Batra D.]\\n  year: 2019\\n  venue: ICLR\\n  category: background\\n  role: \\\"Addresses long-term dynamics prediction via latent-variable autoregressive model; directly relevant to our finding that multi-step RSSM predictions degrade with dt>1\\\"\\n  relevance_score: 4\\n\\n- paper_id: asadi2019combating\\n  title: \\\"Combating the Compounding-Error Problem with a Multi-step Model\\\"\\n  authors: [Asadi K., Misra D., Kim S., Littman M.L.]\\n  year: 2019\\n  venue: \\\"arXiv:1905.13320\\\"\\n  category: background\\n  role: \\\"Proposes multi-step models to bypass compounding error; our work shows that even with multi-step imagination, the dt-embedding creates a different failure mode (value overestimation) distinct from compounding error\\\"\\n  relevance_score: 4\\n\\n- paper_id: venkatraman2015improving\\n  title: \\\"Improving Multi-Step Prediction of Learned Time Series Models\\\"\\n  authors: [Venkatraman A., Hebert M., Bagnell J.A.]\\n  year: 2015\\n  venue: AAAI\\n  category: background\\n  role: \\\"Data-as-Demonstrator (DaD) for robust multi-step prediction; establishes theoretical guarantee relating training error to multi-step prediction error\\\"\\n  relevance_score: 3\\n\\n- paper_id: lambert2022investigating\\n  title: \\\"Investigating Compounding Prediction Errors in Learned Dynamics Models\\\"\\n  authors: [Lambert N., Pister K.S.J., Calandra R.]\\n  year: 2022\\n  venue: \\\"arXiv:2203.09637\\\"\\n  category: background\\n  role: \\\"Empirical study of compounding error properties; we rule out compounding error as the primary failure mechanism (008c vs 008a comparison) and identify value overestimation instead\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Model-predictive control with learned dynamics\\n# ============================================================\\n\\n- paper_id: chua2018pets\\n  title: \\\"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models\\\"\\n  authors: [Chua K., Calandra R., McAllister R., Levine S.]\\n  year: 2018\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"PETS — ensemble-based uncertainty-aware MPC; uses explicit uncertainty quantification to avoid model exploitation, contrasting with DreamerV3's implicit approach\\\"\\n  relevance_score: 3\\n\\n- paper_id: nagabandi2018neural\\n  title: \\\"Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning\\\"\\n  authors: [Nagabandi A., Kahn G., Fearing R.S., Levine S.]\\n  year: 2018\\n  venue: ICRA\\n  category: background\\n  role: \\\"Demonstrates NN dynamics + MPC for locomotion; model errors accumulate over prediction horizon, motivating our investigation of horizon-dependent failures\\\"\\n  relevance_score: 3\\n\\n- paper_id: hansen2024tdmpc2\\n  title: \\\"TD-MPC2: Scalable, Robust World Models for Continuous Control\\\"\\n  authors: [Hansen N., Su H., Wang X.]\\n  year: 2024\\n  venue: \\\"ICLR (arXiv:2310.16828)\\\"\\n  category: background\\n  role: \\\"TD-MPC2 — SOTA MPC planning route (online planning + learned dynamics); DMC benchmark leader but orthogonal to imagination-based training — reviewer defense: TD-MPC2 does online MPC rollouts at test time, we study actor-critic training via imagined rollouts (DreamerV3 paradigm), not a same-level comparison\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW: Pessimistic MBRL / model exploitation mitigation\\n# ============================================================\\n\\n- paper_id: yu2020mopo\\n  title: \\\"MOPO: Model-based Offline Policy Optimization\\\"\\n  authors: [Yu T., Thomas G., Yu L., Ermon S., Zou J., Levine S., Finn C., Ma T.]\\n  year: 2020\\n  venue: \\\"NeurIPS (arXiv:2005.13239)\\\"\\n  category: background\\n  role: \\\"MOPO — pessimistic MBRL via uncertainty-penalized reward (reward -= λ * model_uncertainty); generic model exploitation mitigation — reviewer defense: MOPO addresses distribution shift in offline MBRL, our dt=1 imagination restriction targets dt_embedding-induced delusional critic (temporal conditioning corruption), two complementary mechanisms\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW: Value overestimation mitigation\\n# ============================================================\\n\\n- paper_id: thrun1993issues\\n  title: \\\"Issues in Using Function Approximation for Reinforcement Learning\\\"\\n  authors: [Thrun S., Schwartz A.]\\n  year: 1993\\n  venue: \\\"Connectionist Models Summer School\\\"\\n  category: background\\n  role: \\\"First identification of systematic value overestimation from function approximation; our delusional critic extends this to model-based imagination with temporal conditioning\\\"\\n  relevance_score: 4\\n\\n- paper_id: vanhasselt2016double\\n  title: \\\"Deep Reinforcement Learning with Double Q-Learning\\\"\\n  authors: [van Hasselt H., Guez A., Silver D.]\\n  year: 2016\\n  venue: AAAI\\n  category: background\\n  role: \\\"Double DQN — mitigates overestimation via double estimator; our finding that trained dt-embedding enables value exploitation is a complementary overestimation mechanism in MBRL\\\"\\n  relevance_score: 4\\n\\n- paper_id: fujimoto2018td3\\n  title: \\\"Addressing Function Approximation Error in Actor-Critic Methods\\\"\\n  authors: [Fujimoto S., van Hoof H., Meger D.]\\n  year: 2018\\n  venue: ICML\\n  category: method-component\\n  role: \\\"TD3 — clipped double-Q to limit overestimation in actor-critic; DreamerV3 uses a single critic, making it more vulnerable to the overestimation we identify\\\"\\n  relevance_score: 4\\n\\n- paper_id: haarnoja2018sac\\n  title: \\\"Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor\\\"\\n  authors: [Haarnoja T., Zhou A., Abbeel P., Levine S.]\\n  year: 2018\\n  venue: ICML\\n  category: method-component\\n  role: \\\"SAC — entropy regularization implicitly mitigates overestimation; relevant contrast to DreamerV3's actor which can greedily exploit overestimated values\\\"\\n  relevance_score: 3\\n\\n- paper_id: lee2021sunrise\\n  title: \\\"SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning\\\"\\n  authors: [Lee K., Laskin M., Srinivas A., Abbeel P.]\\n  year: 2021\\n  venue: ICML\\n  category: method-component\\n  role: \\\"Ensemble-based uncertainty weighting for value estimation; potential mitigation for our identified delusional critic mechanism\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Delusional bias\\n# ============================================================\\n\\n- paper_id: lu2018nondelusional\\n  title: \\\"Non-delusional Q-learning and Value-Iteration\\\"\\n  authors: [Lu T., Schuurmans D., Boutilier C.]\\n  year: 2018\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"Formalizes delusional bias from policy-class constraints in Q-learning; we identify an analogous phenomenon where temporal conditioning enables the critic to exploit model imprecision\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW: Hierarchical RL with learned models\\n# ============================================================\\n\\n- paper_id: hafner2022director\\n  title: \\\"Deep Hierarchical Planning from Pixels\\\"\\n  authors: [Hafner D., Lee K.-H., Fischer I., Abbeel P.]\\n  year: 2022\\n  venue: NeurIPS\\n  category: direct-competitor\\n  role: \\\"Director — hierarchical planning in Dreamer latent space via subgoals; addresses temporal abstraction through goal hierarchy rather than variable dt\\\"\\n  relevance_score: 4\\n\\n- paper_id: nachum2018hiro\\n  title: \\\"Data-Efficient Hierarchical Reinforcement Learning\\\"\\n  authors: [Nachum O., Gu S., Lee H., Levine S.]\\n  year: 2018\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"HIRO — off-policy HRL with learned subgoals; demonstrates that hierarchical temporal abstraction can improve sample efficiency when properly designed\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Action repeat / frame skip\\n# ============================================================\\n\\n- paper_id: braylan2015frame\\n  title: \\\"Frame Skip Is a Powerful Parameter for Learning to Play Atari\\\"\\n  authors: [Braylan A., Hollenbeck M., Meyerson E., Miikkulainen R.]\\n  year: 2015\\n  venue: \\\"AAAI Workshop on Learning for General Competency in Video Games\\\"\\n  category: background\\n  role: \\\"Empirical study showing frame skip strongly affects Atari performance; motivates investigation of temporal granularity as a critical design choice\\\"\\n  relevance_score: 3\\n\\n- paper_id: lakshminarayanan2017dynamic\\n  title: \\\"Dynamic Action Repetition for Deep Reinforcement Learning\\\"\\n  authors: [Lakshminarayanan A.S., Sharma S., Ravindran B.]\\n  year: 2017\\n  venue: AAAI\\n  category: method-component\\n  role: \\\"Learns per-step action repetition duration; model-free analog of our variable-dt imagination approach\\\"\\n  relevance_score: 4\\n\\n- paper_id: biedenkapp2021temporl\\n  title: \\\"TempoRL: Learning When to Act\\\"\\n  authors: [Biedenkapp A., Rajan R., Hutter F., Lindauer M.]\\n  year: 2021\\n  venue: ICML\\n  category: method-component\\n  role: \\\"Learns action persistence via skip-policy; demonstrates up to 10x speedup — but in model-free setting without the model exploitation risk we identify\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW: DreamerV2\\n# ============================================================\\n\\n- paper_id: hafner2021dreamerv2\\n  title: \\\"Mastering Atari with Discrete World Models\\\"\\n  authors: [Hafner D., Lillicrap T., Norouzi M., Ba J.]\\n  year: 2021\\n  venue: ICLR\\n  category: background\\n  role: \\\"DreamerV2 — introduces discrete latent representations used in DreamerV3; key architectural predecessor to our base system\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW: Alternative world model architectures\\n# ============================================================\\n\\n- paper_id: micheli2023iris\\n  title: \\\"Transformers are Sample-Efficient World Models\\\"\\n  authors: [Micheli V., Alonso E., Fleuret F.]\\n  year: 2023\\n  venue: ICLR\\n  category: background\\n  role: \\\"IRIS — autoregressive transformer world model; alternative to RSSM that may exhibit different compounding error characteristics under temporal abstraction\\\"\\n  relevance_score: 3\\n\\n- paper_id: robine2023twm\\n  title: \\\"Transformer-based World Models Are Happy With 100k Interactions\\\"\\n  authors: [Robine J., Hoeftmann M., Uelwer T., Harmeling S.]\\n  year: 2023\\n  venue: ICLR\\n  category: background\\n  role: \\\"TWM — Transformer-XL world model with direct state access; circumvents RSSM's recurrent compression that exacerbates our identified prediction gap\\\"\\n  relevance_score: 3\\n\\n- paper_id: chen2022transdreamer\\n  title: \\\"TransDreamer: Reinforcement Learning with Transformer World Models\\\"\\n  authors: [Chen C., Wu Y.-F., Yoon J., Ahn S.]\\n  year: 2022\\n  venue: \\\"arXiv:2202.09481\\\"\\n  category: background\\n  role: \\\"Replaces RSSM with Transformer State-Space Model; directly tests whether RSSM-specific architecture contributes to temporal abstraction failures\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: 2024-2026 concurrent work on temporal abstraction in world models\\n# ============================================================\\n\\n- paper_id: gumbsch2024thick\\n  title: \\\"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics\\\"\\n  authors: [Gumbsch C., Sajid N., Martius G., Butz M.V.]\\n  year: 2024\\n  venue: ICLR\\n  category: direct-competitor\\n  role: \\\"THICK — learns adaptive temporal abstractions via context-change detection; closest concurrent work — addresses temporal abstraction in Dreamer but via hierarchy rather than variable-dt imagination\\\"\\n  relevance_score: 5\\n\\n- paper_id: mattes2024hieros\\n  title: \\\"Hieros: Hierarchical Imagination on Structured State Space Sequence World Models\\\"\\n  authors: [Mattes P., Schlosser R., Herbrich R.]\\n  year: 2024\\n  venue: ICML\\n  category: direct-competitor\\n  role: \\\"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW: Seed-dependent instability & value overestimation in MBRL\\n# ============================================================\\n\\n- paper_id: henderson2018deep\\n  title: \\\"Deep Reinforcement Learning that Matters\\\"\\n  authors: [Henderson P., Islam R., Bachman P., Pineau J., Precup D., Meger D.]\\n  year: 2018\\n  venue: AAAI\\n  category: background\\n  role: \\\"Foundational study on seed variance in deep RL — shows statistically different performance distributions arise from random seeds alone with identical hyperparameters; directly supports our observation that seed 0 vs seed 2 produce qualitatively different value dynamics under the same dt_embed_dim=0 config\\\"\\n  relevance_score: 4\\n\\n- paper_id: nikishin2022primacy\\n  title: \\\"The Primacy Bias in Deep Reinforcement Learning\\\"\\n  authors: [Nikishin E., Schwarzer M., D'Oro P., Bacon P.-L., Courville A.]\\n  year: 2022\\n  venue: ICML\\n  category: background\\n  role: \\\"Identifies primacy bias — agents overfit early data and lose ability to learn from new transitions, leading to delayed performance collapse; parallels our finding where value overestimation initially appears benign but becomes pathological later, and the collapse timing is seed-dependent\\\"\\n  relevance_score: 4\\n\\n- paper_id: qiao2023mind\\n  title: \\\"Mind the Model, Not the Agent: The Primacy Bias in Model-based RL\\\"\\n  authors: [Qiao Z., Lyu J., Li X.]\\n  year: 2023\\n  venue: \\\"arXiv:2310.15017 (ECAI 2024)\\\"\\n  category: evaluation\\n  role: \\\"Extends primacy bias to MBRL, testing on DreamerV2 — shows world model primacy bias dominates over agent primacy bias; directly relevant to Dreamer-family training instability and explains why some seeds recover (model escapes early overfitting) while others don't\\\"\\n  relevance_score: 5\\n\\n- paper_id: hussing2024dissecting\\n  title: \\\"Dissecting Deep RL with High Update Ratios: Combatting Value Divergence\\\"\\n  authors: [Hussing M., Voelcker C.A., Gilitschenski I., Farahmand A.-M., Eaton E.]\\n  year: 2024\\n  venue: \\\"Reinforcement Learning Journal (RLC 2024)\\\"\\n  category: evaluation\\n  role: \\\"Shows value overestimation and Q-divergence under high update-to-data ratios, driven by optimizer momentum — overestimation occurs on both in-distribution and OOD data; mechanism maps to our delusional critic where imagination-trained critic inflates values progressively, with divergence onset sensitive to initialization\\\"\\n  relevance_score: 4\\n\\n- paper_id: barkley2024stealing\\n  title: \\\"Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning\\\"\\n  authors: [Barkley B., Fridovich-Keil D.]\\n  year: 2024\\n  venue: \\\"arXiv:2412.14312 (ICML 2025)\\\"\\n  category: evaluation\\n  role: \\\"Demonstrates that synthetic rollouts (imagination) can degrade performance inconsistently across environments, with overestimation bias as a contributing factor; supports our finding that imagination-based training creates environment- and seed-dependent failure modes that existing mitigation techniques do not reliably fix\\\"\\n  relevance_score: 3\\n\\n- paper_id: bjorck2022variance\\n  title: \\\"Is High Variance Unavoidable in RL? A Case Study in Continuous Control\\\"\\n  authors: [Bjorck J., Gomes C.P., Weinberger K.Q.]\\n  year: 2022\\n  venue: ICLR\\n  category: background\\n  role: \\\"Shows RL variance mostly arises early in training from poor 'outlier' runs caused by numerical instability; parallels our observation that seed 2 diverges early while seed 0 recovers — the reward prediction degradation from removing dt_embedding may create exactly this early-training instability\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Reward prediction quality → MBRL performance\\n# ============================================================\\n# Our key finding: removing dt_embedding causes reward_MAE to spike 75x\\n# (0.01 → 0.747), making performance seed-dependent. These papers\\n# establish that reward prediction quality is a known MBRL bottleneck.\\n\\n- paper_id: lee2024dreamsmooth\\n  title: \\\"DreamSmooth: Improving Model-based Reinforcement Learning via Reward Smoothing\\\"\\n  authors: [Lee V., Abbeel P., Lee Y.]\\n  year: 2024\\n  venue: ICLR\\n  category: background\\n  role: \\\"Directly demonstrates reward prediction is a bottleneck in MBRL — sparse/ambiguous rewards cause the reward model to predict zeros, creating gradient-free landscapes during imagination; our dt_embed_dim=0 ablation creates an analogous bottleneck where the reward head loses temporal conditioning and MAE spikes 75x\\\"\\n  relevance_score: 5\\n\\n- paper_id: ma2024harmonydream\\n  title: \\\"HarmonyDream: Task Harmonization Inside World Models\\\"\\n  authors: [Ma H., Wu J., Feng N., Xiao C., Li D., Hao J., Wang J., Long M.]\\n  year: 2024\\n  venue: ICML\\n  category: background\\n  role: \\\"Shows observation prediction dominates reward prediction in world model training, degrading reward model quality; proposes dynamic loss balancing for 10-69% gains — directly relevant to our finding that dt_embedding removal disrupts the observation-reward prediction balance and causes reward MAE explosion\\\"\\n  relevance_score: 5\\n\\n- paper_id: lambert2020objective\\n  title: \\\"Objective Mismatch in Model-based Reinforcement Learning\\\"\\n  authors: [Lambert N., Amos B., Yadan O., Calandra R.]\\n  year: 2020\\n  venue: \\\"L4DC (Proceedings of Machine Learning Research, vol. 120)\\\"\\n  category: background\\n  role: \\\"Formalizes that one-step prediction likelihood does not correlate with control performance — the 'objective mismatch' problem; our work reveals a specific instance: the reward head's prediction accuracy (measured by MAE) directly gates whether the critic can learn stable value estimates, creating a reward-specific objective mismatch\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW: Auxiliary tasks & representation coupling in world models\\n# ============================================================\\n# Our finding: reward prediction quality is tightly coupled to temporal\\n# conditioning (dt_embedding). Removing the embedding degrades the\\n# reward head while dynamics remain intact — suggesting the reward head\\n# acts as more than a passive predictor; it conditions the shared\\n# representation. Literature gap: no prior work studies this coupling\\n# specifically in Dreamer-family world models.\\n\\n- paper_id: jaderberg2017unreal\\n  title: \\\"Reinforcement Learning with Unsupervised Auxiliary Tasks\\\"\\n  authors: [Jaderberg M., Mnih V., Czarnecki W.M., Schaul T., Leibo J.Z., Silver D., Kavukcuoglu K.]\\n  year: 2017\\n  venue: ICLR\\n  category: background\\n  role: \\\"UNREAL — introduces reward prediction as an auxiliary task that shapes shared representations; foundational evidence that reward prediction is not just a passive output but actively conditions what features the network learns — our finding that removing dt_embedding selectively degrades reward prediction (but not dynamics) suggests the temporal conditioning specifically enables reward-relevant feature extraction\\\"\\n  relevance_score: 4\\n\\n- paper_id: lyle2021auxiliary\\n  title: \\\"On The Effect of Auxiliary Tasks on Representation Dynamics\\\"\\n  authors: [Lyle C., Rowland M., Ostrovski G., Dabney W.]\\n  year: 2021\\n  venue: AISTATS\\n  category: background\\n  role: \\\"Theoretical analysis showing auxiliary tasks shape representations toward top eigenvectors of the transition operator; provides formal grounding for why removing temporal conditioning from the reward head could alter the entire representation — the reward head's gradients contribute to spectral structure of the shared latent space\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW: DreamerV3 architecture improvements (2025-2026)\\n# ============================================================\\n\\n- paper_id: bredis2026nedreamer\\n  title: \\\"Next Embedding Prediction Makes World Models Stronger\\\"\\n  authors: [Bredis G., Balagansky N., Gavrilov D., Rakhimov R.]\\n  year: 2026\\n  venue: \\\"arXiv:2603.02765\\\"\\n  category: background\\n  role: \\\"NE-Dreamer — decoder-free MBRL replacing pixel reconstruction with next-embedding prediction via temporal transformer + Barlow Twins; improves RSSM prediction quality on DMC and DMLab but does not address temporal abstraction or delusional critic — orthogonal to our dt-embedding diagnosis\\\"\\n  relevance_score: 3\\n\\n- paper_id: zhang2025dymodreamer\\n  title: \\\"DyMoDreamer: World Modeling with Dynamic Modulation\\\"\\n  authors: [Zhang B., Wang R., Xiao W., Zhang W., Sun J., Huang G., Chen J., Wang G.]\\n  year: 2025\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"Modulates RSSM via inter-frame differencing mask and stochastic categorical dynamic modulation; SOTA on Atari 100k (156.6% HNS) and DMC (832) — improves dynamics extraction but does not address variable-rate imagination or dt_embedding-induced value overestimation\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Temporal abstraction methods\\n# ============================================================\\n\\n- paper_id: liu2025vanta\\n  title: \\\"Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning\\\"\\n  authors: [Liu T.-S., Liu X.-H., Chen R., Jin L., Wang P., Zhang Z., Yu Y.]\\n  year: 2025\\n  venue: ICLR\\n  category: method-component\\n  role: \\\"VanTA — VLM-guided trajectory decomposition into semantically meaningful skills via vector quantization + relabeling; operates at high-level skill abstraction (Franka Kitchen, Crafter) — contrasts with our low-level dt-based temporal abstraction within world-model imagination steps\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Evaluation methodology\\n# ============================================================\\n\\n- paper_id: agarwal2021precipice\\n  title: \\\"Deep Reinforcement Learning at the Edge of the Statistical Precipice\\\"\\n  authors: [Agarwal R., Schwarzer M., Castro P.S., Courville A.C., Bellemare M.]\\n  year: 2021\\n  venue: NeurIPS\\n  category: evaluation\\n  role: \\\"Proposes rliable — interval estimates, performance profiles, IQM for robust multi-seed RL evaluation (NeurIPS Outstanding Paper); our multi-seed experiment design follows this methodology to ensure statistical validity of collapse detection across seeds\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW (2026-05-14 gap analysis): Time discretization theory\\n# ============================================================\\n# Gap: variable timestep / time discretization invariance — foundational\\n# theory for why dt matters and how to handle it.\\n\\n- paper_id: tallec2019making\\n  title: \\\"Making Deep Q-learning methods Robust to Time Discretization\\\"\\n  authors: [Tallec C., Blier L., Ollivier Y.]\\n  year: 2019\\n  venue: \\\"ICML (arXiv:1901.09732)\\\"\\n  category: background\\n  role: \\\"Shows Q-learning performance is highly sensitive to time discretization δ; proposes architectural + exploration modifications for δ-invariance. Theoretical foundation for why our variable-dt imagination introduces a fundamental difficulty: RSSM trained at δ=1 cannot produce δ-invariant predictions at dt>1\\\"\\n  relevance_score: 4\\n\\n- paper_id: park2021sar\\n  title: \\\"Time Discretization-Invariant Safe Action Repetition for Policy Gradient Methods\\\"\\n  authors: [Park S., Kim J., Kim G.]\\n  year: 2021\\n  venue: \\\"NeurIPS (arXiv:2111.03941)\\\"\\n  category: method-component\\n  role: \\\"SAR — δ-invariant action repetition for policy gradients; achieves time-discretization robustness in model-free RL via adaptive reaction to state changes during repetition. Contrasts with our finding that world-model RL lacks this robustness when imagination uses dt>1\\\"\\n  relevance_score: 4\\n\\n- paper_id: wang2024seac\\n  title: \\\"Reinforcement Learning with Elastic Time Steps\\\"\\n  authors: [Wang D., Beltrame G.]\\n  year: 2024\\n  venue: \\\"arXiv:2402.14961\\\"\\n  category: method-component\\n  role: \\\"SEAC/MOSEAC — variable-duration time steps where agent selects both action and duration; model-free approach that explicitly treats action duration as part of the action space. Our work reveals why this strategy is problematic in world-model RL: the critic cannot reliably evaluate variable-duration imagined trajectories\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW (2026-05-14 gap analysis): Delusional bias mitigation\\n# ============================================================\\n\\n- paper_id: su2020conqur\\n  title: \\\"ConQUR: Mitigating Delusional Bias in Deep Q-learning\\\"\\n  authors: [Su D., Ooi J., Lu T., Schuurmans D., Boutilier C.]\\n  year: 2020\\n  venue: \\\"ICML (arXiv:2002.12399)\\\"\\n  category: background\\n  role: \\\"Follow-up to Lu et al. 2018; mitigates delusional bias via consistency-penalized Q-labels. Addresses delusional bias from policy-class constraints in Q-learning; our delusional critic is an analogous phenomenon in MBRL where temporal conditioning (dt_embedding) creates inconsistent value targets across imagination steps\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW (2026-05-14 gap analysis): Diagnostic methodology in RL\\n# ============================================================\\n# Gap: our paper is a diagnostic analysis — need methodological\\n# precedents for \\\"what matters\\\" / \\\"implementation matters\\\" style papers.\\n\\n- paper_id: engstrom2020implementation\\n  title: \\\"Implementation Matters in Deep Policy Gradients: A Case Study on PPO and TRPO\\\"\\n  authors: [Engstrom L., Ilyas A., Santurkar S., Tsipras D., Janoos F., Rudolph L., Madry A.]\\n  year: 2020\\n  venue: \\\"ICLR (arXiv:2005.12729)\\\"\\n  category: evaluation\\n  role: \\\"Demonstrates that code-level implementation details (not algorithmic innovations) drive most of PPO's gains over TRPO; methodological precedent for our diagnostic approach — we similarly show that a specific implementation choice (trained vs. untrained dt_embedding) is the primary factor determining collapse vs. stability\\\"\\n  relevance_score: 4\\n\\n- paper_id: andrychowicz2021whatmatters\\n  title: \\\"What Matters for On-Policy Deep Actor-Critic Methods? A Large-Scale Study\\\"\\n  authors: [Andrychowicz M., Raichuk A., Stańczyk P., Orsini M., Girgin S., Marinier R., Hussenot L., Geist M., Pietquin O., Michalski M., Gelly S., Bachem O.]\\n  year: 2021\\n  venue: \\\"ICLR (arXiv:2006.05990)\\\"\\n  category: evaluation\\n  role: \\\"Large-scale factorial study of 50+ design choices in on-policy RL (250K+ agents); methodological template for our factorial experiment design isolating dt_embedding × subsample × horizon effects. Demonstrates that systematic ablation reveals non-obvious interactions — parallel to our finding that dt_embedding training status interacts with subsample and horizon\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW (2026-05-14 gap analysis): MBRL rollout quality & value overestimation\\n# ============================================================\\n# Gap: recent ICLR 2025 papers directly studying imagination rollout\\n# quality and value overestimation in model-based settings.\\n\\n- paper_id: frauenknecht2025rollouts\\n  title: \\\"On Rollouts in Model-Based Reinforcement Learning\\\"\\n  authors: [Frauenknecht B., Subhasish D., Solowjow F., Trimpe S.]\\n  year: 2025\\n  venue: \\\"ICLR (arXiv:2501.16918)\\\"\\n  category: evaluation\\n  role: \\\"Shows trajectory-sampling rollouts diverge from ground truth after few steps and can harm policy learning; proposes Infoprop separating aleatoric/epistemic uncertainty with rollout termination criteria. Directly supports our finding that dt>1 imagination produces corrupted data — our work identifies a specific mechanism (dt_embedding-induced value exploitation) beyond general compounding error\\\"\\n  relevance_score: 5\\n\\n- paper_id: voelcker2025madtd\\n  title: \\\"MAD-TD: Model-Augmented Data stabilizes High Update Ratio RL\\\"\\n  authors: [Voelcker C., Hussing M., Eaton E., Farahmand A.-M., Gilitschenski I.]\\n  year: 2025\\n  venue: \\\"ICLR (arXiv:2410.08896)\\\"\\n  category: evaluation\\n  role: \\\"Shows value function misgeneralization to on-policy actions causes instability at high UTD ratios; uses model-generated data to improve value accuracy. Complementary to our finding: MAD-TD addresses value misgeneralization from replay distribution mismatch, we address value overestimation from temporal conditioning corruption in imagination\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW (2026-05-14 gap analysis): Latest action repeat methods\\n# ============================================================\\n\\n- paper_id: nie2025sdar\\n  title: \\\"Select before Act: Spatially Decoupled Action Repetition for Continuous Control\\\"\\n  authors: [Nie B., et al.]\\n  year: 2025\\n  venue: \\\"ICLR (arXiv:2502.06919)\\\"\\n  category: method-component\\n  role: \\\"SDAR — per-dimension action repetition decisions for flexible temporal persistence in model-free RL; SOTA on DMC continuous control. Advances action repeat in model-free setting; our work shows the fundamental obstacle to analogous variable-rate approaches in model-based RL (delusional critic from dt_embedding)\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW (2026-05-14 gap analysis): DreamerV4 / latest Dreamer evolution\\n# ============================================================\\n\\n- paper_id: hafner2025dreamerv4\\n  title: \\\"Training Agents Inside of Scalable World Models\\\"\\n  authors: [Hafner D., Yan W.]\\n  year: 2025\\n  venue: \\\"arXiv:2509.24527\\\"\\n  category: background\\n  role: \\\"DreamerV4 — replaces RSSM with efficient transformer world model + shortcut forcing; scales to video pretraining (Minecraft diamonds from video). Architectural successor to DreamerV3; our dt_embedding diagnosis is specific to RSSM but the broader lesson (temporal conditioning must match model fidelity) applies to transformer world models\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW (2026-05-14): Training instability dynamics\\n# ============================================================\\n\\n- paper_id: zhang2026instability\\n  title: \\\"Training instability in deep learning follows low-dimensional dynamical principles\\\"\\n  authors: [Zhang L., et al.]\\n  year: 2026\\n  venue: \\\"ICLR 2026 (arXiv:2601.13160)\\\"\\n  category: background\\n  role: \\\"Training instability follows low-dimensional dynamical principles; provides theoretical framework for why seed-dependent collapse vs self-correction occurs in our experiments (008d seed 1 collapses, 009b seed 2 self-corrects under identical config)\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW (2026-05-14): Seed-Dependent Stochastic Outcomes in MBRL\\n# ============================================================\\n# Dedicated literature survey for the stochastic collapse phenomenon:\\n# same config (trained dt_embedding + subsample + H=8) produces\\n# collapse in seed 0 (008d) but self-correction in seed 2 (009b).\\n# nve>1.5x is a 100% reliable marker of trained dt_embedding,\\n# but collapse itself is stochastic (1/2 seeds).\\n\\n- paper_id: sokar2023dormant\\n  title: \\\"The Dormant Neuron Phenomenon in Deep Reinforcement Learning\\\"\\n  authors: [Sokar G., Agarwal R., Castro P.S., Evci U.]\\n  year: 2023\\n  venue: \\\"ICML 2023\\\"\\n  category: background\\n  role: \\\"Identifies dormant neurons — inactive units accumulating during RL training that reduce network expressivity. Seed-dependent because different random initializations produce different early dormancy patterns; directly explains why some seeds lose the representational capacity needed to self-correct value overestimation (our seed 0 collapses) while others retain enough active neurons to recover (our seed 2 self-corrects)\\\"\\n  relevance_score: 4\\n  survey_tag: seed-dependent-stochastic-outcomes\\n\\n- paper_id: lyle2022capacity\\n  title: \\\"Understanding and Preventing Capacity Loss in Reinforcement Learning\\\"\\n  authors: [Lyle C., Rowland M., Dabney W.]\\n  year: 2022\\n  venue: \\\"ICLR 2023 (arXiv:2204.09560)\\\"\\n  category: background\\n  role: \\\"Shows feature rank collapse from non-stationary TD targets is a necessary condition for learning failure but not sufficient — sparse rewards and other factors must co-occur. Directly parallels our finding: nve>1.5x (value overestimation from trained dt_embedding) is a necessary precondition for collapse but not a sufficient one; additional stochastic factors (initialization, early replay composition) determine whether collapse actually occurs\\\"\\n  relevance_score: 5\\n  survey_tag: seed-dependent-stochastic-outcomes\\n\\n- paper_id: kumar2022dr3\\n  title: \\\"DR3: Value-Based Deep Reinforcement Learning Requires Explicit Regularization\\\"\\n  authors: [Kumar A., Agarwal R., Ma T., Courville A., Tucker G., Levine S.]\\n  year: 2022\\n  venue: \\\"ICLR 2022\\\"\\n  category: background\\n  role: \\\"Shows implicit regularization from TD learning favors degenerate feature aliasing (states on both sides of Bellman backup become indistinguishable), creating the substrate for value overestimation. In our setting, trained dt_embedding amplifies this aliasing across different temporal horizons — the critic cannot distinguish between dt=1 and dt>1 value targets, enabling exploitation. Feature aliasing is seed-dependent because it depends on initialization geometry\\\"\\n  relevance_score: 4\\n  survey_tag: seed-dependent-stochastic-outcomes\\n\\n- paper_id: colas2018seeds\\n  title: \\\"How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments\\\"\\n  authors: [Colas C., Sigaud O., Oudeyer P.-Y.]\\n  year: 2018\\n  venue: \\\"arXiv:1806.08295\\\"\\n  category: evaluation\\n  role: \\\"Provides statistical framework for determining seed count needed for significant algorithm comparison; our 2-seed observation (1/2 collapse) has limited statistical power by their analysis — but the qualitative difference (nve 4.12x vs 0.38x) is large enough that even 2 seeds establish the stochastic nature of the phenomenon. Methodological basis for future multi-seed validation\\\"\\n  relevance_score: 3\\n  survey_tag: seed-dependent-stochastic-outcomes\\n\\n- paper_id: nikishin2023plasticity\\n  title: \\\"Deep Reinforcement Learning with Plasticity Injection\\\"\\n  authors: [Nikishin E., Oh J., Ostrovski G., Lyle C., Pascanu R., Dabney W., Barreto A.]\\n  year: 2023\\n  venue: \\\"NeurIPS 2023\\\"\\n  category: method-component\\n  role: \\\"Plasticity injection augments network plasticity without changing parameter count; serves as a diagnostic tool — if injection improves performance, plasticity loss was the bottleneck. Directly applicable to diagnosing whether our seed-dependent collapse is plasticity-mediated: if plasticity injection prevents collapse in seed 0 but has no effect on seed 2 (which already self-corrects), it confirms plasticity loss as the bifurcation mechanism\\\"\\n  relevance_score: 4\\n  survey_tag: seed-dependent-stochastic-outcomes\\n\\n- paper_id: schwarzer2023bbf\\n  title: \\\"Bigger, Better, Faster: Human-level Atari with Human-level Efficiency\\\"\\n  authors: [Schwarzer M., Obando-Ceron J.S., Courville A., Bellemare M., Agarwal R., Castro P.S.]\\n  year: 2023\\n  venue: \\\"ICML 2023\\\"\\n  category: method-component\\n  role: \\\"BBF achieves SOTA sample efficiency via periodic network resets + scaling + weight decay; periodic resets prevent primacy bias accumulation across seeds. Suggests our delusional critic collapse might be preventable with periodic critic resets — the reset would break the positive feedback loop between overestimated values and actor exploitation before it becomes irreversible\\\"\\n  relevance_score: 3\\n  survey_tag: seed-dependent-stochastic-outcomes\\n\\n- paper_id: farebrother2024stopregressing\\n  title: \\\"Stop Regressing: Training Value Functions via Classification for Scalable Deep RL\\\"\\n  authors: [Farebrother J., Orbay J., Vuong Q., Taiga A.A., Chebotar Y., Xiao T., Irpan A., Levine S., Castro P.S., Faust A., Kumar A., Agarwal R.]\\n  year: 2024\\n  venue: \\\"ICML 2024\\\"\\n  category: method-component\\n  role: \\\"Shows categorical cross-entropy for value training provides implicit regularization against overestimation vs MSE regression. DreamerV3 already uses categorical value prediction (twohot + symlog) — yet our trained dt_embedding still induces collapse in some seeds, demonstrating that categorical value training is insufficient to prevent dt_embedding-induced value exploitation\\\"\\n  relevance_score: 3\\n  survey_tag: seed-dependent-stochastic-outcomes\\n\\n- paper_id: lyle2024normalization\\n  title: \\\"Normalization and Effective Learning Rates in Reinforcement Learning\\\"\\n  authors: [Lyle C., Zheng Z., Giunchiglia E., Sherstan C., Hashemizadeh M., Schuurmans D., Dabney W.]\\n  year: 2024\\n  venue: \\\"NeurIPS 2024\\\"\\n  category: background\\n  role: \\\"Shows normalization layers combat overestimation but cause effective learning rate decay via parameter norm growth. Provides a potential mechanism for seed 2's self-correction: if parameter norms grow faster in certain initializations, effective LR decays faster, naturally damping value overestimation before it cascades into collapse. Seed 0's slower norm growth → sustained high effective LR → overestimation compounds → collapse\\\"\\n  relevance_score: 4\\n  survey_tag: seed-dependent-stochastic-outcomes\\n\\n# --- Survey synthesis: Seed-Dependent Stochastic Outcomes ---\\n# Summary (2026-05-14):\\n#\\n# 1. STOCHASTIC COLLAPSE HAS PRECEDENT:\\n#    Plasticity loss (Lyle 2022, Sokar 2023, Nikishin 2023) is inherently\\n#    seed-dependent because it depends on initialization → early gradient\\n#    dynamics → neuron activity patterns. Different seeds hit different\\n#    plasticity trajectories under identical configs.\\n#\\n# 2. nve>1.5x AS DIAGNOSTIC MARKER (necessary but not sufficient):\\n#    Lyle 2022 shows feature rank collapse is necessary but not sufficient\\n#    for learning failure. Kumar 2022 shows feature aliasing from TD\\n#    learning creates the overestimation substrate. Our nve>1.5x is\\n#    analogous: it indicates the dt_embedding has enabled value exploitation\\n#    (100% reliable marker), but collapse requires additional conditions\\n#    (plasticity loss, insufficient effective LR decay) that are stochastic.\\n#\\n# 3. SELF-CORRECTION MECHANISM:\\n#    Lyle 2024 provides a candidate mechanism: normalization-induced\\n#    effective LR decay can naturally damp overestimation in some seeds.\\n#    Farebrother 2024 shows categorical value training provides partial\\n#    implicit regularization. Together these explain why seed 2 self-corrects:\\n#    the combination of DreamerV3's categorical critic + normalization +\\n#    favorable initialization produces enough implicit regularization to\\n#    overcome the dt_embedding-induced overestimation.\\n#\\n# 4. THEORETICAL GROUNDING:\\n#    Zhang 2026 (already in map) provides the dynamical systems framework.\\n#    Bjorck 2022 (already in map) shows early outlier events dominate\\n#    variance. Together with the new papers, the framing is:\\n#    \\\"trained dt_embedding creates a necessary condition (nve>1.5x) for\\n#    delusional critic collapse, but collapse is a stochastic bifurcation\\n#    whose outcome depends on seed-dependent plasticity dynamics.\\\"\\n\\n# ============================================================\\n# INCREMENTAL SCAN (2026-05-14): Δt conditioning & adaptive horizon\\n# ============================================================\\n# 8 new papers from targeted search on:\\n#   - Δt/timestep conditioning in world models\\n#   - Variable-rate imagination / adaptive horizon\\n#   - Hierarchical planning with latent world models (2025-2026)\\n#\\n# KEY FINDING: TAWM (Nhu et al. ICML 2025) explicitly conditions\\n# world model on Δt — closest methodological overlap. But TAWM\\n# uses TD-MPC2 (online MPC) not imagination-based actor-critic,\\n# and treats Δt conditioning as beneficial. Our work diagnoses\\n# Δt conditioning as pathological in imagination-based training\\n# (delusional critic). Complementary, not duplicative.\\n\\n- paper_id: nhu2025tawm\\n  title: \\\"Time-Aware World Model for Adaptive Prediction and Control\\\"\\n  authors: [Nhu A.N., Son S., Lin M.C.]\\n  year: 2025\\n  venue: \\\"ICML 2025 (arXiv:2506.08441)\\\"\\n  category: direct-competitor\\n  role: \\\"TAWM — explicitly conditions world model on time-step size Δt and trains over diverse Δt values for multi-rate dynamics learning. Built on TD-MPC2 (online MPC). KEY DISTINCTION from our work: (1) TAWM treats Δt conditioning as beneficial for performance/data-efficiency; we diagnose it as pathological in imagination-based actor-critic training (delusional critic). (2) TAWM uses MPC (no imagination rollouts for policy training); our failure mode is specific to imagination-based training where the critic exploits dt-conditioned value estimates. (3) TAWM focuses on observation-rate robustness; we focus on value overestimation from temporal conditioning corruption. TAWM actually strengthens our contribution: it shows Δt conditioning works in MPC settings, making our finding that it fails in imagination-based settings a surprising and important diagnostic.\\\"\\n  relevance_score: 5\\n  novelty_threat: \\\"MEDIUM — methodological overlap (Δt conditioning) but fundamentally different paradigm (MPC vs imagination) and opposite conclusion (beneficial vs pathological). Must cite and differentiate in paper.\\\"\\n\\n- paper_id: li2025lsimagine\\n  title: \\\"Open-World Reinforcement Learning over Long Short-Term Imagination\\\"\\n  authors: [Li J., Wang Q., Wang Y., Jin X., Li Y., Zeng W., Yang X.]\\n  year: 2025\\n  venue: \\\"ICLR 2025 Oral (arXiv:2410.03618)\\\"\\n  category: direct-competitor\\n  role: \\\"LS-Imagine — extends imagination horizon in Dreamer via goal-conditioned jumpy state transitions and affordance maps. Addresses the 'short-sightedness' of standard Dreamer imagination. KEY DISTINCTION: LS-Imagine adds jumpy transitions to reach long-horizon targets (open-world Minecraft), while our work shows that variable-dt imagination itself introduces delusional critic. LS-Imagine's jumpy transitions use goal conditioning (not dt-embedding), potentially avoiding the value overestimation we identify.\\\"\\n  relevance_score: 4\\n  novelty_threat: \\\"LOW — different mechanism (goal-conditioned jumps vs dt-embedding) and different focus (long-horizon exploration vs diagnostic of failure modes). Should cite as concurrent approach to extending imagination horizon.\\\"\\n\\n- paper_id: zhang2026hwm\\n  title: \\\"Hierarchical Planning with Latent World Models\\\"\\n  authors: [Zhang W., Terver B., Zholus A., Chitnis S., Sutaria H., Assran M., Balestriero R., Bar A., Bardes A., LeCun Y., Ballas N.]\\n  year: 2026\\n  venue: \\\"arXiv:2604.03208\\\"\\n  category: direct-competitor\\n  role: \\\"HWM — learns multi-scale latent world models for hierarchical MPC planning; high-level planner optimizes macro-actions, low-level planner handles primitives. 70% success on real-world non-greedy robotic tasks vs 0% for single-level. Addresses temporal abstraction via hierarchical planning (MPC), not imagination-based actor-critic. Further evidence that temporal abstraction in world models requires hierarchy rather than single-scale variable-dt approaches.\\\"\\n  relevance_score: 4\\n  novelty_threat: \\\"LOW — MPC-based hierarchical planning, not imagination-based training. Supports our thesis that flat dt-embedding approaches are inferior to hierarchical alternatives.\\\"\\n\\n- paper_id: kobayashi2025metacontroller\\n  title: \\\"Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning\\\"\\n  authors: [Kobayashi S., et al.]\\n  year: 2025\\n  venue: \\\"arXiv:2512.20605\\\"\\n  category: method-component\\n  role: \\\"MetaController — discovers temporal abstractions via higher-order non-causal sequence model controlling base autoregressive model's residual stream. Each controller executes behaviorally meaningful action sequences with learned termination conditions. Operates in fundamentally different paradigm (LLM-style autoregressive models, not world-model imagination), but demonstrates that temporal abstraction benefits from hierarchical structure rather than flat dt-conditioning.\\\"\\n  relevance_score: 3\\n\\n- paper_id: shaj2023mts3\\n  title: \\\"Multi Time Scale World Models\\\"\\n  authors: [Shaj V., Gholam Zadeh S., Demir O., Luettjohann L., Neumann G., Toussaint M.]\\n  year: 2023\\n  venue: \\\"NeurIPS 2023 (arXiv:2310.18534)\\\"\\n  category: method-component\\n  role: \\\"MTS3 — probabilistic multi-time-scale state space model with fast and slow latent dynamics for variable-rate prediction. Provides efficient inference across temporal scales. Foundational multi-rate dynamics architecture; our work shows that even with proper multi-rate modeling, the downstream actor-critic training in imagination can exploit temporal conditioning for value overestimation — a failure mode MTS3 does not address (it focuses on prediction quality, not policy training).\\\"\\n  relevance_score: 4\\n\\n- paper_id: splates2025\\n  title: \\\"Stable Planning with Temporally Extended Skills\\\"\\n  authors: [SPlaTES authors]\\n  year: 2025\\n  venue: \\\"Reinforcement Learning Journal (RLC 2025)\\\"\\n  category: method-component\\n  role: \\\"SPlaTES — hierarchical MPC with temporally extended skills + abstract skill world model. Skill learning via mutual-information objective yields diverse, predictable, task-related behavior. Demonstrates that stable long-horizon planning requires modeling skill outcomes (temporal abstraction via hierarchy), not primitive-action outcomes at variable time steps — consistent with our finding that flat dt-embedding fails.\\\"\\n  relevance_score: 3\\n\\n- paper_id: beckerehmck2023multitimestep\\n  title: \\\"Multi-timestep models for Model-based Reinforcement Learning\\\"\\n  authors: [Becker-Ehmck P., Peters J., van der Smagt P.]\\n  year: 2023\\n  venue: \\\"arXiv:2310.05672\\\"\\n  category: background\\n  role: \\\"Proposes multi-timestep training objective (weighted sum of losses at various future horizons) for one-step dynamics models to improve long-horizon R² score. Addresses compounding error at the model training level; our work shows that even with perfect multi-step prediction, the imagination-based actor-critic can still fail due to value overestimation from dt-conditioning — a downstream failure mode distinct from prediction accuracy.\\\"\\n  relevance_score: 3\\n\\n- paper_id: liu2022dmve\\n  title: \\\"Dynamic-Horizon Model-Based Value Estimation With Latent Imagination\\\"\\n  authors: [Liu Y., et al.]\\n  year: 2022\\n  venue: \\\"IEEE TNNLS (arXiv:2009.09593)\\\"\\n  category: background\\n  role: \\\"DMVE — adaptive rollout horizon selection via horizon reliability detection (comparing value expansion errors between raw and reconstructed observations). Addresses the horizon selection problem in imagination-based value estimation. Complementary to our work: DMVE selects among fixed-dt horizons; we show that even optimal horizon selection cannot fix the delusional critic when dt-embedding is trained (the overestimation is in the value function, not the horizon length).\\\"\\n  relevance_score: 3\\n\\n# --- Incremental scan synthesis (2026-05-14) ---\\n#\\n# NOVELTY ASSESSMENT:\\n# No paper found that diagnoses dt_embedding → delusional critic\\n# (value overestimation) → stochastic collapse in imagination-based\\n# MBRL. Our core contribution remains novel.\\n#\\n# TAWM (ICML 2025) is the closest methodological overlap but\\n# operates in MPC paradigm and reaches opposite conclusion\\n# (Δt conditioning is beneficial). This actually STRENGTHENS\\n# our novelty: \\\"Δt conditioning helps in MPC but hurts in\\n# imagination-based training\\\" is a more nuanced and surprising finding.\\n#\\n# LANDSCAPE TREND:\\n# The field is converging on HIERARCHY (THICK, Hieros, Director,\\n# HWM, SPlaTES, MetaController) as the solution to temporal\\n# abstraction in world models, avoiding flat variable-dt approaches.\\n# Our diagnostic paper explains WHY flat dt approaches fail,\\n# providing theoretical grounding for this empirical trend.\\n#\\n# ACTION ITEMS FOR PAPER:\\n# 1. MUST CITE: nhu2025tawm — differentiate MPC vs imagination paradigm\\n# 2. SHOULD CITE: li2025lsimagine — concurrent Dreamer horizon extension\\n# 3. SHOULD CITE: shaj2023mts3 — multi-rate dynamics foundation\\n# 4. CONSIDER: zhang2026hwm — latest hierarchical WM planning\\n\", \"total_chars\": 50497, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NVLFDExxqw2K9tFpK6oTpk`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "writing_plan.yaml",
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
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "563cfe31-adad-4462-8ba8-5a92ca23c79f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016uBuyZh4rKiMrjGMj1ej6K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 23459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1097
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

_source line 16 · 2026-05-15T01:15:46.679Z_

<details><summary>↩ Tool result · `toolu_01NVLFDExxqw2K9tFpK6oTpk`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'event-gated-adaptive-horizon'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "596587d7-8932-4f72-b158-9bc7ab908b5a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"No writing_plan.yaml found for 'event-gated-adaptive-horizon'.\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'event-gated-adaptive-horizon'.\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_019vRbtjspEP7mwiWnt4MZe7`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "limit": 0,
  "fields": [
    "*"
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
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "fda57fa8-a1f9-4e34-80a2-2467a567b2c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016uBuyZh4rKiMrjGMj1ej6K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 23459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1097
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

_source line 18 · 2026-05-15T01:15:48.337Z_

<details><summary>↩ Tool result · `toolu_019vRbtjspEP7mwiWnt4MZe7`</summary>

```text
Error: result (61,640 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/e9efbf3e-355b-4b54-9c61-7a3e79247d76/tool-results/mcp-agent-ml-research-read_registry-1778807748281.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/e9efbf3e-355b-4b54-9c61-7a3e79247d76/tool-results/mcp-agent-ml-research-read_registry-1778807748281.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "105238d9-b377-41ff-97ec-9e67405837bf",
  "tool_use_result": {
    "content": "Error: result (61,640 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/e9efbf3e-355b-4b54-9c61-7a3e79247d76/tool-results/mcp-agent-ml-research-read_registry-1778807748281.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/e9efbf3e-355b-4b54-9c61-7a3e79247d76/tool-results/mcp-agent-ml-research-read_registry-1778807748281.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_009a_baseline_walker_s2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:17:24.247Z\", \"updated_at\": \"2026-05-15T01:14:41.641Z\", \"hypothesis\": \"Walker Walk baseline seed 2 — 多 seed 复现 exp_001 baseline，建立 v/e 校准参考（plan_010）\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-45299\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T07:19:08.969Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009a_baseline_walker_s2 --steps 500000 --seed 2 --compile False --device cuda:0\\\"\", \"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\"}, \"spec\": {\"model_name\": \"DreamerV3 (original, gate_enabled=false)\", \"seed\": 2, \"data_path\": \"dmc_walker_walk\", \"data_count\": 500000}, \"pid\": \"142508\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009a_baseline_walker_s2.log\", \"metrics\": {\"current_step\": 368000, \"target_steps\": 500000, \"progress_pct\": 73.6, \"eval_return_latest\": 943.13, \"eval_return_peak\": 960.2, \"value_mean\": 664.18, \"ve_ratio\": 0.704, \"fps\": 3.42, \"trend\": \"Converged. eval stable 900-960 from 215K+, brief dip 816@345K recovered to 943@365K.\", \"checked_at\": \"2026-05-15T01:14\"}, \"notes\": \"D032 排期确认: cuda:0 排期: 009a (RUNNING, ~225K/500K) → 009d → 010a。进度: eval=956@215K, eval=892@225K, v/e=69.1%@215K (healthy baseline range).\"}, \"exp_008e_v3_walker_s2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:29:53.738Z\", \"updated_at\": \"2026-05-15T01:14:39.192Z\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 2 — crown jewel C6 seed 2 验证\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"notes\": \"D032 排期确认: cuda:1 排在 008e_v3_s1 之后。完整排期: 008e_v3_s1 (RUNNING) → 008e_v3_s2 → 009e → 009f → 009c(200K) → plan_060。\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"43437\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_walker_s2.log\", \"submitted_at\": \"2026-05-15T00:46:45.424Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, trained dt_emb)\", \"server\": \"bjb1-45299\", \"account\": \"root\", \"pid\": \"43437\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_walker_s2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\"}, \"metrics\": {\"current_step\": 8000, \"target_steps\": 105000, \"progress_pct\": 7.6, \"eval_checkpoints\": [{\"step\": 5000, \"eval_return\": 39.27, \"value_mean\": 0.00193, \"ve_ratio\": 5e-05}], \"gate_dt_mean\": 1, \"gate_dt_1_frac\": 1, \"trend\": \"Just started. 1 eval point only, too early for comparison.\", \"checked_at\": \"2026-05-15T01:14\"}}, \"exp_008e_v3_walker_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:29:53.120Z\", \"updated_at\": \"2026-05-15T00:44:53.439Z\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 1 — crown jewel C6 验证：trained dt_emb 在 dt=1 imagination 下不触发 delusional critic（plan_014）\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"notes\": \"Crown jewel C6 seed 1 SUCCESS. eval_return=869.9@105K, v/e=0.527 (healthy, no delusional critic). Gate locked dt=1 throughout. Trajectory: 31→131→156→276→382→487→581→574→657→852→870. Consistent with seed 0, confirms trained dt_emb + dt=1 imagination is safe.\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"898127\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_walker_s1.log\", \"submitted_at\": \"2026-05-14T18:49:27.945Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 21325.5, \"gpu_hours\": 5.92}, \"pid\": \"898127\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s1/\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\"}, \"metrics\": {\"eval_trajectory\": [{\"step\": 5000, \"eval_return\": 31}, {\"step\": 15000, \"eval_return\": 131.2}, {\"step\": 25000, \"eval_return\": 155.7}, {\"step\": 35000, \"eval_return\": 276.5}, {\"step\": 45000, \"eval_return\": 382.2}, {\"step\": 55000, \"eval_return\": 486.8}, {\"step\": 65000, \"eval_return\": 580.7}, {\"step\": 75000, \"eval_return\": 574.1}, {\"step\": 85000, \"eval_return\": 657.3}, {\"step\": 95000, \"eval_return\": 851.9}, {\"step\": 105000, \"eval_return\": 869.9}], \"final_eval_return\": 869.9, \"final_value_mean\": 457.9, \"ve_ratio_105k\": 0.527, \"total_steps\": 112000, \"gate_dt_1_frac\": 1, \"exit_code\": 0}, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, trained dt_emb)\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s1/latest.pt\", \"completed_at\": \"2026-05-15T00:44:53.439Z\"}, \"exp_006\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:49:02.944Z\", \"updated_at\": \"2026-05-14T22:31:54.922Z\", \"metrics\": {\"eval_return\": {\"5000\": 31, \"15000\": 256.9, \"25000\": 321.4, \"35000\": 485.3, \"45000\": 477, \"55000\": 360.4}, \"peak_return\": 485.3, \"peak_step\": 35000, \"latest_step\": 55000, \"latest_return\": 360.4, \"model_loss_at_55k\": 4.853, \"gate_dt_mean\": 2, \"baseline_return_at_55k\": 625.7, \"deficit_vs_baseline_at_55k\": -265.3, \"deficit_pct\": -42.4}, \"conclusion\": \"killed\", \"notes\": \"早期条目，权威数据在 exp_006_fixed_dt2。conclusion=killed（D034 registry 清理）。\"}, \"exp_008a\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:07:59.793Z\", \"updated_at\": \"2026-05-14T22:31:54.075Z\", \"metrics\": {\"step\": 65000, \"eval_return_5K\": 31, \"eval_return_15K\": 167.2, \"eval_return_25K\": 230.8, \"eval_return_35K\": 500.8, \"eval_return_45K\": 563.4, \"eval_return_55K\": 487.9, \"eval_return_65K\": \"pending (eval in progress)\", \"value_mean_55K\": 183.5, \"value_eval_ratio_55K\": \"37.6%\", \"train_return_64K_avg\": 556.6, \"trend\": \"peaked @45K=563, dipped to @55K=488, 65K eval in progress; train returns @64K healthy (~557)\"}, \"conclusion\": \"killed\", \"notes\": \"早期条目，权威数据在 exp_008a_no_subsample_dt2。conclusion=killed（D034 registry 清理）。\"}, \"exp_008c\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:08:02.608Z\", \"updated_at\": \"2026-05-14T22:31:52.611Z\", \"metrics\": {\"step\": 68000, \"eval_return_5K\": 31, \"eval_return_15K\": 171.3, \"eval_return_25K\": 192.4, \"eval_return_35K\": 185.1, \"eval_return_45K\": 226.6, \"eval_return_55K\": 241.9, \"eval_return_65K\": 240.9, \"value_mean_65K\": 79, \"value_eval_ratio_65K\": \"32.8%\", \"train_return_68K_avg\": 245.1, \"trend\": \"flat plateau @55K-65K (~241), very slow learner with h8, value/eval=32.8% (no collapse)\"}, \"conclusion\": \"killed\", \"notes\": \"早期条目，权威数据在正式命名实验中。conclusion=killed（D034 registry 清理）。\"}, \"exp_008d\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:08:05.136Z\", \"updated_at\": \"2026-05-14T22:31:51.696Z\", \"metrics\": {\"step\": 40000, \"eval_return_5K\": 31, \"eval_return_15K\": 153.7, \"eval_return_25K\": 167.2, \"eval_return_35K\": 146.3, \"value_mean_35K\": 60.2, \"value_eval_ratio_35K\": \"41.1%\", \"train_return_40K_avg\": 119.3, \"trend\": \"declining — train_return @40K avg=119 below @35K eval=146, value/eval=41.1% not yet >50% but train performance dropping\"}, \"conclusion\": \"killed\", \"notes\": \"早期条目，权威数据在 exp_008d_subsample_on_h8。conclusion=killed（D034 registry 清理）。\"}, \"exp_008e_v2_subsample_on_dt1_h15\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:26:39.732Z\", \"updated_at\": \"2026-05-14T22:31:49.814Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v2_subsample_on_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"125392\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v2_subsample_on_dt1_h15.log\", \"submitted_at\": \"2026-05-14T04:27:30.720Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\", \"notes\": \"已被 exp_008e_v3_subsample_on_dt1_h15 取代，进程已死。conclusion=killed（D034 registry 清理）。\"}, \"exp_rssm_fidelity_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:09:52.237Z\", \"updated_at\": \"2026-05-14T22:31:48.642Z\", \"metrics\": {\"baseline\": {\"dt1_obs_mse\": 13.49, \"dt2_obs_mse\": 27.5, \"obs_gap\": 2.04, \"dt1_reward_mae\": 0.0102, \"dt2_reward_mae\": 0.0159, \"reward_gap\": 1.56}, \"008d_trained_dtEmb\": {\"dt1_obs_mse\": 41.31, \"dt2_obs_mse\": 53.67, \"obs_gap\": 1.3, \"dt1_reward_mae\": 0.0568, \"dt2_reward_mae\": 0.1579, \"reward_gap\": 2.78}, \"008f_no_dtEmb\": {\"dt1_obs_mse\": 8.01, \"dt2_obs_mse\": 22.04, \"obs_gap\": 2.75, \"dt1_reward_mae\": 0.7469, \"dt2_reward_mae\": 0.7526, \"reward_gap\": 1.01}}, \"conclusion\": \"success\", \"hypothesis\": \"RSSM prediction quality analysis: 比较 baseline/008d/008f 在 dt=1 vs dt=2 transitions 上的 obs_MSE 和 reward_MAE，量化 RSSM fidelity gap (plan_030)\", \"notes\": \"分析实验，非训练实验。conclusion=success，状态从 PREPARING 修正为 DONE（D034 registry 清理）。\"}, \"exp_008e_v3_subsample_on_dt1_h15\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:29:31.656Z\", \"updated_at\": \"2026-05-14T19:46:00.840Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_subsample_on_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"126110\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_subsample_on_dt1_h15\", \"submitted_at\": \"2026-05-14T04:29:31.600Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, untrained dt_emb)\", \"seed\": 1, \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"wall_clock_seconds\": 16695.7, \"gpu_hours\": 4.64}, \"hypothesis\": \"B+ confound control：subsample ON + untrained dt_emb + dt=1 imagination + H=15。验证 subsample ON 训练数据（含 dt=2 transitions）是否本身导致性能下降，即使 imagination 只用 dt=1。对照 008a（subsample OFF）和 baseline。如果 008e_v3 性能接近 baseline → subsample ON 本身无害。如果下降 → subsample ON 改变了 RSSM dynamics。\", \"metrics\": {\"current_step\": 112000, \"target_steps\": 105000, \"fps\": 7.01, \"eval_return\": {\"5K\": 31, \"15K\": 131.2, \"25K\": 155.69, \"35K\": 276.47, \"45K\": 382.22, \"55K\": 486.84, \"65K\": 580.67, \"75K\": 574.09, \"85K\": 657.31, \"95K\": 851.86, \"105K\": 869.88}, \"value_mean\": {\"25K\": 26.19, \"35K\": 62.76, \"45K\": 110.67, \"55K\": 170.09, \"65K\": 235.05, \"75K\": 300.51, \"85K\": 351.33, \"95K\": 405.25, \"105K\": 457.93}, \"value_eval_ratio\": {\"25K\": 0.168, \"35K\": 0.227, \"45K\": 0.29, \"55K\": 0.35, \"65K\": 0.405, \"75K\": 0.523, \"85K\": 0.534, \"95K\": 0.476, \"105K\": 0.527}, \"normalized_ve\": {\"25K\": 1.93, \"35K\": 0.94, \"45K\": 0.88, \"55K\": 0.87, \"65K\": 0.72, \"75K\": 0.73, \"85K\": 0.76, \"95K\": 0.75, \"105K\": 0.8}, \"gate_dt_mean\": 1, \"gate_dt_1_frac\": 1, \"last_updated\": \"2026-05-14T09:09:00\", \"baseline_105K\": 915.67, \"vs_baseline_105K\": \"-5.0%\", \"verdict\": \"SUCCESS - 95% baseline, normalized v/e stable 0.72-0.80x, B+ hypothesis confirmed\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T09:05:42.563Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:05:44.288431+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_subsample_on_dt1_h15/latest.pt\", \"completed_at\": \"2026-05-14T09:07:47.319Z\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, trained dt_emb)\"}, \"exp_009b_008d_walker_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:17:25.186Z\", \"updated_at\": \"2026-05-14T19:33:15.451Z\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + H=8 seed 2 — 多 seed 复现 008d delusional critic collapse，巩固 C2 统计显著性（plan_011）\", \"parent\": \"exp_008d_subsample_on_h8\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009b_008d_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, trained dt_embed)\", \"seed\": 2, \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000}, \"pid\": \"887053\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009b_008d_walker_s2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009b_008d_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"finished_at\": \"2026-05-14T18:47:20.636Z\"}, \"metrics\": {\"current_step\": 105000, \"target_steps\": 105000, \"eval_checkpoints\": [{\"step\": 5000, \"eval_return\": 39.27, \"value_mean\": 0, \"ve_ratio\": 0, \"baseline_ve\": null, \"normalized_ve\": null}, {\"step\": 15000, \"eval_return\": 144.31, \"value_mean\": 4.47, \"ve_ratio\": 0.031, \"baseline_ve\": null, \"normalized_ve\": null}, {\"step\": 25000, \"eval_return\": 141.12, \"value_mean\": 25.14, \"ve_ratio\": 0.178, \"baseline_ve\": 0.087, \"normalized_ve\": 2.05}, {\"step\": 35000, \"eval_return\": 164.14, \"value_mean\": 49.02, \"ve_ratio\": 0.299, \"baseline_ve\": 0.241, \"normalized_ve\": 1.24}, {\"step\": 45000, \"eval_return\": 141.04, \"value_mean\": 75.59, \"ve_ratio\": 0.536, \"baseline_ve\": 0.331, \"normalized_ve\": 1.62}, {\"step\": 55000, \"eval_return\": 172.33, \"value_mean\": 98.28, \"ve_ratio\": 0.57, \"baseline_ve\": 0.404, \"normalized_ve\": 1.41}, {\"step\": 65000, \"eval_return\": 209.16, \"value_mean\": 110.91, \"ve_ratio\": 0.53, \"baseline_ve\": 0.563, \"normalized_ve\": 0.94}, {\"step\": 75000, \"eval_return\": 197.46, \"value_mean\": 93.49, \"ve_ratio\": 0.474, \"baseline_ve\": 0.719, \"normalized_ve\": 0.66}, {\"step\": 85000, \"eval_return\": 236.49, \"value_mean\": 83.86, \"ve_ratio\": 0.355, \"baseline_ve\": 0.701, \"normalized_ve\": 0.51}, {\"step\": 95000, \"eval_return\": 278.54, \"value_mean\": 75.72, \"ve_ratio\": 0.272, \"baseline_ve\": 0.632, \"normalized_ve\": 0.43}, {\"step\": 105000, \"eval_return\": 267.93, \"value_mean\": 67.27, \"ve_ratio\": 0.251, \"baseline_ve\": 0.656, \"normalized_ve\": 0.38}], \"trend\": \"Eval rising throughout: 39→144→141→164→141→172→209→197→236→279→268. Value peaks at 110.91@65K then self-corrects downward to 67.27@105K. v/e ratio peaks 0.57@55K then monotonically declines to 0.25@105K. NO delusional critic collapse — value self-corrects while eval improves.\", \"verdict\": \"NEGATIVE — hypothesis was to replicate collapse, collapse NOT reproduced. However, pathological nve>1.5x episode confirmed (2.05x@25K, 1.62x@45K), consistent with trained dt_emb inducing pathological overestimation. Self-correction to 0.38x@105K distinguishes from seed 0's sustained overestimation → collapse.\", \"baseline_105K\": 915.67, \"vs_baseline_105K\": \"-70.8%\", \"causal_conclusion\": \"Seed 2 nve transiently reached 2.05x@25K (pathological), confirming trained dt_emb reliably induces nve>1.5x (2/2 seeds). But seed 2 self-corrected (nve 2.05x→0.38x@105K, eval 141→268) while seed 0 sustained nve>1.5x across 4 consecutive checkpoints and collapsed (eval 167→83). Collapse is stochastic (1/2 seeds); nve>1.5x threshold is a reliable diagnostic marker with 4/4 separating power (trained 2/2 exceed, untrained 0/2 exceed).\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:47:21.873692+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009b_008d_walker_s2/latest.pt\", \"completed_at\": \"2026-05-14T18:51:00Z\", \"notes\": \"D032: Collapse NOT reproduced in seed 2. nve peaked 2.05x@25K (transient) then self-corrected to 0.38x@105K. Eval rose to 268. Contrast: seed 1 had SUSTAINED nve>1.5x at 35K+ (1.71x→2.09x→4.12x) → collapse to 83. Key finding: nve>1.5x threshold (35K+ steps) is reliable trained dt_emb marker (2/2 seeds), but collapse is stochastic (1/2). Framing proposal submitted to Director.\", \"causal_conclusion\": \"Seed 2 nve transiently reached 2.05x@25K (pathological), confirming trained dt_emb reliably induces nve>1.5x (2/2 seeds). But seed 2 self-corrected (nve 2.05x→0.38x@105K, eval 141→268) while seed 1 sustained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x→2.09x→4.12x) and collapsed (eval 167→83). Collapse is stochastic (1/2 seeds); nve>1.5x threshold (at 35K+ steps) is a reliable diagnostic marker with 4/4 separating power (trained 2/2 exceed, untrained 0/2 exceed).\"}, \"exp_009d_baseline_walker_s1\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:09:14.363Z\", \"updated_at\": \"2026-05-14T19:27:21.814Z\", \"hypothesis\": \"Walker Walk baseline seed 1 — 多 seed 复现 exp_001 baseline，建立 v/e 校准参考（plan_010）\", \"parent\": \"exp_001_baseline\", \"notes\": \"D032 排期确认: cuda:0 排在 009a 之后。cuda:0 排期: 009a (RUNNING) → 009d → 010a。\"}, \"exp_009e_008d_walker_s1\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:09:15.367Z\", \"updated_at\": \"2026-05-14T14:34:25.713Z\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + H=8 seed 1 — 多 seed 复现 008d delusional critic collapse，巩固 C2 统计显著性（plan_011）\", \"parent\": \"exp_008d_subsample_on_h8\", \"notes\": \"D031 排期修正: cuda:1 排在 008e_v3 s1/s2 之后。009b → 008e_v3_s1 → 008e_v3_s2 → 009e → 009f → 009c(200K) → plan_060。\"}, \"exp_009c_008f_walker_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:17:26.154Z\", \"updated_at\": \"2026-05-14T14:34:24.161Z\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 2 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T07:19:10.835Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009c_008f_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"finished_at\": \"2026-05-14T14:15:57.425Z\", \"training_hours\": 6.95}, \"spec\": {\"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0)\", \"seed\": 2, \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_008f_walker_s2\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_008f_walker_s2/metrics.jsonl\"}, \"pid\": \"140980\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009c_008f_walker_s2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T14:15:58.982844+00:00\"}]}, \"metrics\": {\"current_step\": 105000, \"target_steps\": 105000, \"eval_checkpoints\": [{\"step\": 5000, \"eval_return\": 30.37, \"value_mean\": 0.0013, \"ve_ratio\": null, \"baseline_ve\": null, \"normalized_ve\": null}, {\"step\": 15000, \"eval_return\": 157.15, \"value_mean\": 3.057, \"ve_ratio\": 0.019, \"baseline_ve\": null, \"normalized_ve\": null}, {\"step\": 25000, \"eval_return\": 168.75, \"value_mean\": 18.536, \"ve_ratio\": 0.11, \"baseline_ve\": 0.087, \"normalized_ve\": 1.26}, {\"step\": 35000, \"eval_return\": 178.94, \"value_mean\": 34.263, \"ve_ratio\": 0.191, \"baseline_ve\": 0.241, \"normalized_ve\": 0.79}, {\"step\": 45000, \"eval_return\": 211.08, \"value_mean\": 50.099, \"ve_ratio\": 0.237, \"baseline_ve\": 0.331, \"normalized_ve\": 0.72}, {\"step\": 55000, \"eval_return\": 238.91, \"value_mean\": 63.267, \"ve_ratio\": 0.265, \"baseline_ve\": 0.404, \"normalized_ve\": 0.66}, {\"step\": 65000, \"eval_return\": 244.15, \"value_mean\": 72.717, \"ve_ratio\": 0.298, \"baseline_ve\": 0.563, \"normalized_ve\": 0.53}, {\"step\": 75000, \"eval_return\": 359.14, \"value_mean\": 83.91, \"ve_ratio\": 0.234, \"baseline_ve\": 0.719, \"normalized_ve\": 0.33}, {\"step\": 85000, \"eval_return\": 227.43, \"value_mean\": 96.071, \"ve_ratio\": 0.422, \"baseline_ve\": 0.701, \"normalized_ve\": 0.6}, {\"step\": 95000, \"eval_return\": 190.94, \"value_mean\": 108.29, \"ve_ratio\": 0.567, \"baseline_ve\": 0.632, \"normalized_ve\": 0.9}, {\"step\": 105000, \"eval_return\": 148.34, \"value_mean\": 111.247, \"ve_ratio\": 0.75, \"baseline_ve\": 0.656, \"normalized_ve\": 1.14}], \"trend\": \"Peak 359@75K then monotonic decline to 148@105K; no recovery pattern unlike 008f seed 1's zigzag recovery to 503\", \"verdict\": \"NEGATIVE - no delusional critic (normalized v/e < 1.5x) but persistent decline after 75K; cross-seed consistency with 008f seed 1 NOT confirmed\", \"baseline_105K\": 915.67, \"vs_baseline_105K\": \"-83.8%\", \"causal_conclusion\": \"Seed 2 does NOT replicate seed 1's zigzag recovery. 008f seed 1 peaked at 503@105K with rising trend; seed 2 peaked at 359@75K then declined to 148@105K. The adaptive horizon mechanism's benefit appears seed-dependent and not robust.\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_008f_walker_s2/latest.pt\", \"completed_at\": \"2026-05-14T22:15:00Z\", \"notes\": \"D031 排期修正: 009c 延长 200K 降优先级，排在 009e/009f 之后。cuda:1 排期: 009b → 008e_v3_s1 → 008e_v3_s2 → 009e → 009f → 009c(200K) → plan_060。105K 指标: eval=148.34, value=111.25, nve=1.14x。\"}, \"exp_010a_cheetah_baseline_s1\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:17:27.101Z\", \"updated_at\": \"2026-05-14T14:32:30.711Z\", \"hypothesis\": \"Cheetah Run baseline seed 1 — 建立第二环境 dt=1 参考基线，为跨环境验证 C1/C2 做准备（plan_020）\", \"notes\": \"Director 排期: cuda:0 上排在 009d 之后。\"}, \"exp_009f_008f_walker_s1\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:09:15.806Z\", \"updated_at\": \"2026-05-14T11:11:21.341Z\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 1 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\"}, \"exp_007_fixed_dt4\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-13T22:15:44.218Z\", \"updated_at\": \"2026-05-14T10:20:16.451Z\", \"hypothesis\": \"诊断实验：fixed dt=4 vs dt=2 vs learned gate。硬编码 dt=4，其余超参与 exp_006 完全一致。与 exp_006(dt=2) 对照：如果 dt=4 也不掉 return，说明跳步本身无害，问题在 learned gate 机制；如果 dt=4 掉但 dt=2 不掉，说明存在跳步边界。\", \"account\": \"root\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt4_v1_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 4\\\"\", \"code_commit\": \"6ef8646d807cd10ce0c88e10a7e943211e7fc44c\", \"finished_at\": \"2026-05-13T22:32:00.443Z\"}, \"failure_reason\": \"dt=4 confirmed too coarse for locomotion: eval_return 127@35K vs baseline 389 (-67.4%). model_loss comparable to baseline — RSSM can learn 4-step dynamics, but action temporal resolution too coarse for Walker Walk. Confirms dt sweet spot ∈ {1,2}. See D013.\", \"completed_at\": \"2026-05-13T22:32:00.591Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T22:32:01.413690+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因诊断中 | tmux 日志仅有初始化 warnings，无 Traceback | metrics.jsonl 仅到 step 5000（eval_return=31, model_grad_norm=206.46）| 进程运行 ~12.5 min 后异常退出 | 诊断 Worker: worker_diagnose_exp_007_fixed_dt4_20260513T223405\"}}, \"notes\": \"失败原因诊断中 | tmux 日志仅有初始化 warnings，无 Traceback | metrics.jsonl 仅到 step 5000（eval_return=31, model_grad_norm=206.46）| 进程运行 ~12.5 min 后异常退出 | 诊断 Worker: worker_diagnose_exp_007_fixed_dt4_20260513T223405\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt4_v2_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 4\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"90354\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/fixed_dt4_v2_s1\", \"model_name\": \"DreamerV3+FixedDt4 (gate_fixed_dt=4, no learned gate, init_dt fix applied)\", \"seed\": 1, \"data_path\": \"dmc_walker_walk\", \"data_count\": 150000}, \"metrics\": {\"step\": 48000, \"eval_return_5K\": 31, \"eval_return_15K\": 129.6, \"eval_return_25K\": 176.9, \"eval_return_35K\": 126.7, \"eval_return_45K\": 144.41, \"eval_return_55K\": 152.49, \"peak_return\": 176.9, \"peak_step\": \"25K\", \"model_loss_5K\": 17.927, \"model_loss_15K\": 6.337, \"model_loss_25K\": 5.089, \"model_loss_35K\": 4.755, \"value_mean_45K\": 18.26, \"value_mean_55K\": 9.28, \"value_eval_ratio_45K\": 0.126, \"value_eval_ratio_55K\": 0.061, \"baseline_45K\": 443, \"vs_baseline_45K\": \"-67.4%\", \"trend\": \"peak 176.9@25K, low plateau ~127-152; value extremely suppressed (v/e 6-13%), NOT delusional critic but severe learning failure\"}, \"checkpoint_path\": \"N/A - killed, dt=4 confirmed too coarse for locomotion (D013)\", \"conclusion\": \"negative\"}, \"exp_006_fixed_dt2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T21:10:58.851Z\", \"updated_at\": \"2026-05-14T10:20:11.722Z\", \"hypothesis\": \"诊断实验：fixed dt=2 vs learned gate。去掉 Gumbel-Softmax gate，硬编码 dt=2，其余超参与 exp_005 完全一致。量化 learned gate 的价值——如果 fixed dt=2 也掉 return，说明跳步本身有害；如果不掉，问题在 gate 学习机制。\", \"parent\": \"exp_005_event_gated_v4\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-45299\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T22:12:00.446Z\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && CUDA_VISIBLE_DEVICES=0 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt2_v1_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2\\\"\", \"code_commit\": \"6ef8646d807cd10ce0c88e10a7e943211e7fc44c\"}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt2_v1_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"85029\", \"model_name\": \"DreamerV3+FixedDt2 (gate_fixed_dt=2, no learned gate)\", \"seed\": 1, \"data_path\": \"dmc_walker_walk\", \"data_count\": 150000, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/fixed_dt2_v1_s1\", \"checkpoint_path\": \"N/A - negative result, fixed dt=2 collapsed to 132.9@65K (21.6% baseline)\", \"failure_reason\": \"fixed dt=2 崩塌：训练分布混合（58.5% dt=1 + 41.5% dt=2 log-uniform）+ 想象纯 dt=2 条件下，eval_return 从 peak 485@35K 持续下降至 132.9@65K（baseline 同期 615.9）。与 learned gate 变体一致的崩塌模式。代码审计确认 curriculum 不生效（gate_fixed_dt>0 跳过 _update_gate_schedule）。\"}, \"pid\": \"85029\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_006_fixed_dt2.log\", \"metrics\": {\"step\": 65000, \"eval_return_5K\": 31, \"eval_return_15K\": 256.9, \"eval_return_25K\": 321.4, \"eval_return_35K\": 485.3, \"eval_return_45K\": 477, \"eval_return_55K\": 360.4, \"eval_return_65K\": 132.86, \"peak_return\": 485.3, \"peak_step\": \"35K\", \"model_loss_5K\": 20.738, \"model_loss_15K\": 7.593, \"model_loss_25K\": 5.633, \"model_loss_35K\": 5.229, \"model_loss_45K\": 5.023, \"model_loss_55K\": 4.9, \"gate_dt_mean\": 2, \"gate_dt_std\": 0, \"fps\": 6.5, \"value_mean_35K\": 151.1, \"value_mean_45K\": 254.29, \"value_mean_55K\": 336.44, \"value_mean_65K\": 361.69, \"value_eval_ratio_35K\": 0.311, \"value_eval_ratio_45K\": 0.533, \"value_eval_ratio_55K\": 0.933, \"value_eval_ratio_65K\": 2.722, \"baseline_35K\": 388.5, \"baseline_45K\": 513.8, \"baseline_55K\": 625.7, \"vs_baseline_55K\": \"-42.4%\", \"trend\": \"inverted-V: peak 485@35K, collapsing to 133@65K; v/e accelerating: 31.1%→53.3%→93.3%→272% (value 2.7x eval_return at 65K)\", \"data_source_ve\": \"from training logs metrics.jsonl\"}, \"latest_metrics\": {\"step\": 36000, \"eval_step\": 35000, \"eval_return\": 485.3, \"prev_eval_return\": 321.4, \"eval_return_trajectory\": {\"5K\": 31, \"15K\": 256.9, \"25K\": 321.4, \"35K\": 485.3}, \"gate_dt_mean\": 2, \"gate_dt_std\": 0, \"grad_norm\": 8.6, \"fps\": 6.6, \"process_status\": \"running\", \"pid\": 85029, \"checked_at\": \"2026-05-14\"}, \"extra\": {\"curriculum_audit\": \"Curriculum does NOT apply in fixed_dt mode (models.py:200-205). gate_fixed_dt>0 bypasses _update_gate_schedule(). subsample_variable_dt receives effective_max_dt=2.0 from step 0, training data is 58.5% dt=1 + 41.5% dt=2 throughout. Actual train/imagine mismatch: mixed dt training vs pure dt=2 imagination.\", \"audit_commit\": \"6159e46\", \"bugs_fixed\": \"_effective_max_dt not synced in fixed_dt mode; hardcoded curriculum phases ignoring config\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T01:13:11.533Z\"}, \"exp_008d_subsample_on_h8\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:46:57.960Z\", \"updated_at\": \"2026-05-14T10:20:03.071Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008d_subsample_on_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"109519\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_subsample_on_h8\", \"submitted_at\": \"2026-05-14T02:21:59.852Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8)\", \"seed\": 1, \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_subsample_on_h8/checkpoint.ckpt\", \"wall_clock_seconds\": 8932.6, \"gpu_hours\": 2.48}, \"metrics\": {\"step\": 55000, \"eval_return_25K\": 167.22, \"eval_return_35K\": 146.34, \"eval_return_45K\": 140.8, \"eval_return_55K\": 82.75, \"value_mean_25K\": 25.86, \"value_mean_35K\": 60.2, \"value_mean_45K\": 97.5, \"value_mean_55K\": 137.88, \"value_eval_ratio_25K\": 0.155, \"value_eval_ratio_35K\": 0.411, \"value_eval_ratio_45K\": 0.693, \"value_eval_ratio_55K\": 1.666, \"actor_loss_25K\": -0.195, \"actor_loss_35K\": -0.17, \"model_loss_25K\": 5.33, \"model_loss_35K\": 5.07, \"baseline_35K\": 400, \"baseline_45K\": 443, \"vs_baseline_35K\": \"-63.4%\", \"vs_baseline_45K\": \"-68.2%\", \"verdict_35K\": \"WARN_COLLAPSE\", \"verdict_45K\": \"COLLAPSE_CONFIRMED\", \"trend\": \"eval declining 167→146→141→83; v/e accelerating 15.5%→41.2%→69.3%→167% — delusional critic collapse confirmed, value exceeds eval_return at 55K\", \"data_source_45K\": \"from training logs metrics.jsonl\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T04:50:52.439Z\"}, \"exp_008f_no_dt_embed_subsample_on_h8\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:51:27.592Z\", \"updated_at\": \"2026-05-14T09:49:29.276Z\", \"hypothesis\": \"C2 confound control：隔离 dt_embedding conditioning vs RSSM learned dt=2 dynamics。subsample ON + dt=2 imagination + H=8（与 008d 完全一致），但 gate_dt_embed_dim=0（去掉 dt_embedding 条件输入）。如果 008f 崩塌（v/e >50%）→ 根因是 RSSM 的 dt=2 训练数据导致 dynamics 偏差，不是 dt_embedding per se。如果 008f 稳定（v/e <35%）→ 确认 dt_embedding conditioning 是 delusional critic 的直接原因。对照：008d（dt_embed_dim>0, v/e 15.5%→41.2%→69.3% 崩塌）vs 008c（subsample OFF, untrained dt_emb, v/e 稳定 ~22-33%）。\", \"parent\": \"exp_008d_subsample_on_h8\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_no_dt_embed_subsample_on_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"127761\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_embed_subsample_on_h8\", \"submitted_at\": \"2026-05-14T04:51:55.020Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0)\", \"seed\": 1, \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"checkpoint_source\": \"N/A - training from scratch, parent is for genealogy only\", \"eval_data\": \"N/A - training experiment, not eval\", \"wall_clock_seconds\": 16858.4, \"gpu_hours\": 4.68}, \"metrics\": {\"current_step\": 105000, \"target_steps\": 105000, \"eval_checkpoints\": {\"5K\": {\"eval_return\": 30.49, \"value_mean\": 0.001, \"ve_ratio\": 4e-05}, \"15K\": {\"eval_return\": 182.03, \"value_mean\": 2.989, \"ve_ratio\": 0.01642}, \"25K\": {\"eval_return\": 196.78, \"value_mean\": 17.507, \"ve_ratio\": 0.089, \"baseline_ve\": 0.087, \"normalized_ve\": 1.02}, \"35K\": {\"eval_return\": 206.67, \"value_mean\": 36.279, \"ve_ratio\": 0.176, \"baseline_ve\": 0.241, \"normalized_ve\": 0.73}, \"45K\": {\"eval_return\": 194.08, \"value_mean\": 53.429, \"ve_ratio\": 0.275, \"baseline_ve\": 0.331, \"normalized_ve\": 0.83}, \"55K\": {\"eval_return\": 173.45, \"value_mean\": 67.899, \"ve_ratio\": 0.391, \"baseline_ve\": 0.404, \"normalized_ve\": 0.97}, \"65K\": {\"eval_return\": 375, \"normalized_ve\": 0.37}, \"75K\": {\"eval_return\": 324, \"normalized_ve\": 0.42}, \"85K\": {\"eval_return\": 246, \"value_mean\": 111.8, \"normalized_ve\": 0.65}, \"95K\": {\"eval_return\": 319, \"normalized_ve\": 0.54}, \"105K\": {\"eval_return\": 503, \"value_mean\": 98.2, \"normalized_ve\": 0.3}}, \"trend\": \"Zigzag recovery with high variance: eval 207→194→173@55K→375→324→246→319→503@105K. NOT a clean V-shape — high inter-eval variance throughout. Value self-corrected: peaked 111.8@85K then declined to 98.2@105K. Normalized v/e: 0.97x@55K→0.37x@65K→0.65x@85K→0.30x@105K. Key contrast with 008d: value only accelerates (69.3%@45K) vs 008f value self-corrects.\", \"verdict\": \"SUCCESS - zigzag recovery to 503@105K, normalized v/e=0.30x, C2 confirmed\", \"last_updated\": \"2026-05-14T09:50:00\", \"baseline_105K\": 915.67, \"vs_baseline_105K\": \"-45.1%\", \"causal_conclusion\": \"trained dt_embedding → value overestimation → actor exploitation → collapse. Without dt_embedding, value self-corrects.\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T09:30:41.254Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:30:42.170428+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_embed_subsample_on_h8/latest.pt\", \"completed_at\": \"2026-05-14T09:32:53.461Z\"}, \"exp_008a_no_subsample_dt2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:33:27.311Z\", \"updated_at\": \"2026-05-14T06:20:33.902Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_fixed_dt2_no_subsample --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"106942\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_fixed_dt2_no_subsample\", \"submitted_at\": \"2026-05-14T01:37:46.034Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (gate_fixed_dt=2, gate_subsample_max_dt=1, H=15)\", \"seed\": 1, \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"wall_clock_seconds\": 16752.2, \"gpu_hours\": 4.65}, \"hypothesis\": \"隔离 subsample 效应：subsample OFF（纯 dt=1 训练）+ imagination dt=2 + H=15（物理覆盖 30 步）。如果不崩 → subsample 混合训练数据是崩塌根因；如果崩 → 问题在 dt=2 imagination 本身。\", \"metrics\": {\"step\": 112000, \"eval_return_35K\": 500.84, \"eval_return_45K\": 563.41, \"eval_return_55K\": 487.92, \"eval_return_65K\": 608, \"eval_return_75K\": 469.93, \"eval_return_85K\": 583.73, \"eval_return_95K\": 572.24, \"eval_return_105K\": 777.66, \"value_mean_55K\": 183.5, \"value_mean_65K\": 226.1, \"value_mean_75K\": 251.78, \"value_mean_85K\": 277.36, \"value_mean_95K\": 284.28, \"value_mean_105K\": 300.27, \"value_eval_ratio_55K\": 0.376, \"value_eval_ratio_65K\": 0.372, \"value_eval_ratio_75K\": 0.536, \"value_eval_ratio_85K\": 0.475, \"value_eval_ratio_95K\": 0.497, \"value_eval_ratio_105K\": 0.386, \"normalized_ve_55K\": 0.93, \"normalized_ve_65K\": 0.66, \"normalized_ve_75K\": 0.75, \"normalized_ve_85K\": 0.68, \"normalized_ve_95K\": 0.79, \"normalized_ve_105K\": 0.59, \"baseline_55K\": 625.7, \"baseline_65K\": 616, \"baseline_105K\": 915.67, \"vs_baseline_65K\": \"-1.3%\", \"vs_baseline_105K\": \"-15.1%\", \"verdict_65K\": \"RECOVERED_NEW_HIGH\", \"verdict_105K\": \"NEW_PEAK_V_RECOVERY\", \"trend\": \"Two V-shaped recoveries: 501→563→488→608→470→584→572→778; v/e suppressed 38-54% (normalized 0.59-0.79x baseline); no collapse at 105K\", \"nan_count\": 0, \"data_source\": \"from training logs metrics.jsonl\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T06:15:00.119Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T06:15:01.796655+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_fixed_dt2_no_subsample/latest.pt\", \"completed_at\": \"2026-05-14T06:16:58.196Z\"}, \"exp_001_baseline\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T02:09:53.875Z\", \"updated_at\": \"2026-05-14T05:33:10.628Z\", \"hypothesis\": \"DreamerV3 baseline on DMC Walker Walk for comparison with event-gated model\", \"failure_reason\": \"误报：cron 检测到进程退出但实际是正常完成（512K步）。已核实 checkpoint 229MB 有效。\", \"completed_at\": \"2026-05-13T15:23:24.593Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T15:23:25.663340+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T21:47:19.804301+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"step\": 245000, \"eval_return_205K\": 907.1, \"eval_return_215K\": 919.8, \"train_return_244K\": \"935-976\", \"fps\": 8.3}}}, \"spec\": {\"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/baseline_s1 --steps 500000 --seed 1 --compile False --device cuda:0\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"gpu_id\": 0, \"pid\": 9409, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"data_count\": 500000, \"model_name\": \"DreamerV3 (original, gate_enabled=false)\", \"seed\": 1, \"hypothesis\": \"DreamerV3 baseline on DMC Walker Walk for comparison with event-gated model\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1\"}, \"metrics\": {\"step\": 512000, \"eval_return_205K\": 907.1, \"eval_return_215K\": 919.8, \"eval_return_265K\": 925.09, \"eval_return_365K\": 935.8, \"eval_return_375K\": 918.2, \"eval_return_445K\": 964.96, \"eval_return_455K\": 953.37, \"eval_return_last10_mean\": 950.9, \"train_return_latest\": 958.07, \"fps\": 7.29, \"final\": true, \"value_eval_ratio_25K\": 0.087, \"value_eval_ratio_35K\": 0.241, \"value_eval_ratio_45K\": 0.331, \"value_eval_ratio_55K\": 0.404, \"value_eval_ratio_65K\": 0.563, \"value_eval_ratio_75K\": 0.719, \"value_eval_ratio_85K\": 0.701, \"value_eval_ratio_95K\": 0.632, \"value_eval_ratio_105K\": 0.656, \"value_eval_ratio_stable\": \"~69-72% from 135K+\", \"data_source_ve\": \"from training logs metrics.jsonl\"}, \"latest_metrics\": {\"step\": 452000, \"eval_step\": 445000, \"eval_return\": 953.37, \"prev_eval_return\": 964.96, \"train_return_latest\": 958.07, \"train_return_range\": [917, 985.8], \"fps\": 7.29, \"process_status\": \"running\", \"pid\": 9409, \"uptime\": \"16h35m\", \"steps_remaining\": 48000, \"eta_hours\": 1.8, \"checked_at\": \"2026-05-13\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T21:47:18.966Z\"}, \"conclusion\": \"success\"}, \"exp_008c_no_subsample_dt2_h8\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:33:31.413Z\", \"updated_at\": \"2026-05-14T04:37:29.274Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008c_fixed_dt2_no_subsample_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --imag_horizon 8\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"107021\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008c_fixed_dt2_no_subsample_h8\", \"submitted_at\": \"2026-05-14T01:37:47.540Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=1, imag_horizon=8)\", \"seed\": 1, \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008c_fixed_dt2_no_subsample_h8/checkpoint.ckpt\", \"wall_clock_seconds\": 9119.3, \"gpu_hours\": 2.53}, \"hypothesis\": \"隔离 compounding error 效应：subsample OFF + imagination dt=2 + H=8（物理覆盖 16 步 ≈ baseline H=15）。与 008a(H=15) 对照：008a 崩但 008c 不崩 → compounding error 是根因，H 需与 dt 反比补偿；两个都崩 → dt=2 RSSM 预测质量本身不足。\", \"metrics\": {\"step\": 68000, \"eval_return_35K\": 185.1, \"eval_return_45K\": 226.55, \"eval_return_55K\": 241.87, \"eval_return_65K\": 240.86, \"value_mean_35K\": 40.43, \"value_mean_55K\": 70.32, \"value_mean_65K\": 78.96, \"value_eval_ratio_35K\": 0.218, \"value_eval_ratio_55K\": 0.291, \"value_eval_ratio_65K\": 0.328, \"actor_loss_55K\": -0.082, \"actor_loss_65K\": -0.053, \"baseline_65K\": 616, \"vs_baseline_65K\": \"-60.9%\", \"verdict_65K\": \"PLATEAU\", \"trend\": \"flat plateau @55K-65K (~241), very slow learner with h8, value/eval=32.8% (no collapse)\", \"data_source_35K\": \"from training logs metrics.jsonl\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T04:09:46.829Z\"}, \"exp_008e_subsample_on_fixed_dt1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:10:07.303Z\", \"updated_at\": \"2026-05-14T04:24:58.056Z\", \"hypothesis\": \"验证 Reviewer D020 因果假说：subsample ON 训练 dt_embedding[2]（RSSM 精确预测 dt=2），但 actor/critic 仅在 dt=1 imagination 训练。如果 value/eval ratio 仍加速上升 → dt_embedding 训练本身导致 value 过估（delusional critic），即使 actor 不用 dt=2 imagination。对照：008a (subsample OFF, dt=2 imag) value/eval=37.6%@55K vs exp_006 (subsample ON, dt=2 imag) 53.3%。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_subsample_on_fixed_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"121636\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_subsample_on_fixed_dt1_h15\", \"submitted_at\": \"2026-05-14T04:10:22.915Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15)\", \"seed\": 1, \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"wall_clock_seconds\": 685.0, \"gpu_hours\": 0.19}, \"checkpoint_path\": \"N/A - killed, duplicate registry entry, logdir contaminated by dual-process write\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T04:21:47.956Z\", \"failure_reason\": \"重复 registry 条目 + logdir 被两个进程交叉写入导致 tfevents/metrics.jsonl 损坏。Director 指令清理后以 exp_008e_subsample_on_dt1_h15 为准重跑。\"}, \"exp_008e_subsample_on_dt1_h15\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:10:37.655Z\", \"updated_at\": \"2026-05-14T04:24:57.658Z\", \"hypothesis\": \"验证 Reviewer D020 delusional critic 假说：subsample ON 训练 dt_embedding[2]（RSSM 精确预测 dt=2），但 actor/critic 仅在 dt=1 imagination 训练。如果 value/eval ratio 仍加速上升 → dt_embedding 训练本身导致 value 过估（即使 actor 不用 dt=2 imagination）。对照：008a（subsample OFF，dt=2 imagination）和 006（subsample ON，dt=2 imagination）。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_subsample_on_fixed_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"122038\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_subsample_on_fixed_dt1_h15\", \"submitted_at\": \"2026-05-14T04:10:46.045Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15)\", \"seed\": 1, \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"wall_clock_seconds\": 662.5, \"gpu_hours\": 0.18}, \"checkpoint_path\": \"N/A - killed, logdir contaminated by duplicate process cross-write\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T04:21:48.584Z\", \"notes\": \"重复进程：与 exp_008e_subsample_on_fixed_dt1 命令完全相同，共享同一 logdir，导致 tfevents 文件互相污染。Kill PID 122038，保留 PID 121636。\"}, \"exp_005_event_gated_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:08:06.061Z\", \"updated_at\": \"2026-05-13T22:15:38.893Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_v5_s1 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"51721\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_005_event_gated_v4.log\", \"submitted_at\": \"2026-05-13T16:08:11.913Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"修复 gate_target/masking 维度不匹配 + effective_max_dt 单一来源架构 + 全量审计后，event gate return >= 80% baseline\", \"model_name\": \"DreamerV3+EventGate_v4\", \"seed\": 1, \"data_path\": \"dmc_walker_walk\", \"data_count\": 500000, \"wall_clock_seconds\": 22029.4, \"gpu_hours\": 6.12}, \"metrics\": {\"step\": 145000, \"eval_return_5K\": 31, \"eval_return_15K\": 153.9, \"eval_return_35K\": 290.8, \"eval_return_55K\": 541.18, \"eval_return_65K\": 465.67, \"eval_return_85K\": 212.34, \"eval_return_105K\": 276.08, \"eval_return_145K\": 98.84, \"peak_return\": 541.18, \"peak_step\": \"55K\", \"final_return\": 98.84, \"baseline_at_145K\": \"~950\", \"return_ratio_final\": 0.104, \"gate_scale_105K\": 0.5, \"gate_dt_mean_105K\": 2.054, \"gate_dt_std_105K\": 0.907, \"gate_entropy_105K\": 1.255, \"fps\": 6.69, \"note\": \"85K/105K metrics corrected from 319.3/337.8 to 212.34/276.08\"}, \"latest_metrics\": {\"step\": 65000, \"eval_return\": 465.67, \"prev_eval_return\": 541.18, \"eval_return_trajectory\": {\"5K\": 31, \"15K\": 153.9, \"25K\": 254.2, \"35K\": 290.8, \"45K\": 443, \"55K\": 541.2, \"65K\": 465.7}, \"gate_scale\": 0.10004, \"gate_dt_mean\": 1.035, \"gate_dt_std\": 0.036, \"gate_dt_1_frac\": 0.965, \"gate_dt_2_frac\": 0.035, \"gate_empirical_entropy\": 0.0499, \"gate_entropy_ratio\": 0.072, \"gate_loss\": 0.00663, \"gate_entropy_bonus\": 0.0865, \"train_return_latest\": 569.8, \"train_return_range\": [535.4, 602.1], \"fps\": 6.69, \"process_status\": \"running\", \"pid\": 51721, \"uptime\": \"2h31m\", \"phase2_status\": \"gate刚进入phase2 (gate_scale=0.1), dt=1占比96.5%, gate几乎未激活。eval_return在55K→65K出现14%下降(541→466), 与phase2启动时机吻合, 类似exp_003崩塌前兆。但baseline同期也有小幅回调(626→616, -1.6%), 且gate尚未真正激活, 需继续观察75K数据确认是正常波动还是collapse。\", \"alert\": \"return_declining_at_phase2_onset\", \"baseline_at_65K\": 615.9, \"gap_vs_baseline\": -150.2, \"checked_at\": \"2026-05-13\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A - killed due to structural failure of hard Gumbel gate\", \"completed_at\": \"2026-05-13T22:15:21.359Z\", \"failure_reason\": \"Hard Gumbel gate 结构性失败。3轮 bug 修复后仍崩塌：eval_return 峰值 541.18@55K → 持续下降 → 98.84@145K（baseline 同期 950.9）。Gate 机制有效（entropy/H_eff/structure 全 PASS），但 hard categorical gate + variable-rate imagination 与 actor-critic 优化存在结构性冲突。gate_scale>0.5 后 return 不可恢复。\"}, \"exp_004_event_gated_v3\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T10:05:16.227Z\", \"updated_at\": \"2026-05-13T15:47:43.692Z\", \"hypothesis\": \"修复 imagination dt 约束后（logits masking + clamp safety net），event gate 在 train/imagine 分布同步条件下能产生有意义的 variable-rate stepping 且 return ≥ 80% baseline\", \"failure_reason\": \"gate_loss 爆炸 bug：compute_gate_targets 使用 gate_max_dt=8 生成 target 分布但 logits masking 使用 effective_max_dt，cross-entropy loss ≈ 3e8。eval_return@125K=352 vs baseline@335K=942，ratio=0.37。第三次 train/imagine distribution mismatch。\", \"completed_at\": \"2026-05-13T15:23:26.384Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T15:23:27.393422+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"step\": 20000, \"eval_return_15K\": 153.86, \"gate_scale_15K\": 0, \"gate_dt_mean_15K\": 1, \"fps\": 8.1}}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_v4_s1 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": 36645, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_v4_s1\", \"submitted_at\": \"2026-05-13T10:12:04.157Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": 1, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"data_count\": 500000, \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM v3 (dt clipping + logits masking + dt alignment fix)\", \"seed\": 1, \"wall_clock_seconds\": 18682.2, \"gpu_hours\": 5.19, \"checkpoint_path\": \"N/A - killed due to gate_loss explosion bug\"}, \"conclusion\": \"negative\"}, \"exp_003_event_gated_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T04:52:22.660Z\", \"updated_at\": \"2026-05-13T10:02:35.629Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_s1_v2 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"server\": \"autodl-rtx6000\", \"gpu_id\": 1, \"pid\": 27009, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"data_count\": 500000, \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM v2 (final fix: env step sync + threshold 25K/75K)\", \"seed\": 1, \"hypothesis\": \"Subsample curriculum prevents early destabilization while event gate learns meaningful variable-rate stepping\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1_v2\", \"checkpoint_source\": \"logdir/event_gated_s1_v2/latest.pt\"}, \"metrics\": {\"step\": 120000, \"gate_scale_116K\": 0.61, \"gate_dt_mean_116K\": 2.67, \"gate_dt_std_116K\": 1.46, \"gate_empirical_entropy_116K\": 1.655, \"gate_entropy_ratio_116K\": 0.796, \"gate_dt_1_frac_116K\": 0.218, \"eval_return_105K\": 92.3, \"eval_return_115K\": 118.7, \"return_ratio_105K\": 0.1, \"return_ratio_115K\": 0.13, \"mvp_C1_return\": \"FAIL (0.13)\", \"mvp_C2_entropy\": \"PASS (1.655)\", \"mvp_C3_heff\": \"PASS (2.667x)\", \"mvp_C4_structure\": \"PASS (autocorr=0.652)\", \"fps\": 6.52}, \"reproduce\": {\"finished_at\": \"2026-05-13T09:58:31.205Z\"}, \"failure_reason\": \"Return 崩塌至 baseline 13%。根因：_imagine 中 gate dt 无约束（输出 dt∈{1,...,8}），而 subsample curriculum 限制训练数据 dt≤effective_max_dt。RSSM 对未训练的大 dt 预测为噪声，progressive poisoning 导致 actor/critic 不可恢复。需修复 dt clipping + logits masking 后从头训练。\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-13T09:58:31.673Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T09:58:32.493437+00:00\"}]}}, \"exp_002_event_gated\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T02:09:54.240Z\", \"updated_at\": \"2026-05-13T04:52:18.089Z\", \"spec\": {\"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_s1 --steps 500000 --seed 1 --compile False --device cuda:1 --gate_enabled True\", \"server\": \"autodl-rtx6000\", \"gpu_id\": 1, \"pid\": 9769, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"data_count\": 500000, \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM (K=8, τ=5→0.5, λ_H=0.1→0.01)\", \"seed\": 1, \"hypothesis\": \"Event-gated variable-rate RSSM produces meaningful Δt patterns (entropy>0.3, H_eff>1.2×H_nominal) without breaking training stability (return≥80% baseline)\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1\"}, \"hypothesis\": \"Event-gated variable-rate RSSM produces meaningful Δt patterns (entropy>0.3, H_eff>1.2×H_nominal) without breaking training stability (return≥80% baseline)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T04:50:14.987Z\", \"kill_reason\": \"Phase 1 subsample 设计缺陷：subsample_variable_dt 在 Phase 1 (gate_scale=0) 也生效，RSSM 用 variable-Δt 数据训练但 imagination 只用 Δt=1，return 恶化到 baseline 的 25%。手动 kill 后部署 subsample curriculum 补丁并重启为 exp_003。\"}}, \"count\": 29, \"total\": 29, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6595}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
Let me read the registry data and the literature map in full to get complete information.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "ef511ddd-2abf-4b15-b583-50175611364f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LDS4mL2a55JiVqS5KszA4N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16925,
      "cache_read_input_tokens": 24556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16925
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

_source line 20_

Let me read the registry data and the full literature map.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "f1e43fd4-dbb9-414b-8609-3d0591591654",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LDS4mL2a55JiVqS5KszA4N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16925,
      "cache_read_input_tokens": 24556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16925
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

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01QF8wkpmszCmiLiWgC8PWsN`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/e9efbf3e-355b-4b54-9c61-7a3e79247d76/tool-results/mcp-agent-ml-research-read_registry-1778807748281.txt",
  "offset": 0,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "8fe65822-feb7-4dfd-a871-8eb7a9c5b551",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LDS4mL2a55JiVqS5KszA4N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16925,
      "cache_read_input_tokens": 24556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16925
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

_source line 22 · 2026-05-15T01:15:53.805Z_

<details><summary>↩ Tool result · reported error · `toolu_01QF8wkpmszCmiLiWgC8PWsN`</summary>

```text
File content (27127 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "952b7b69-2880-4386-89b2-75acc70c6ba8",
  "tool_use_result": "Error: File content (27127 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01SZhxd1nEiN1WvNa2zpfyo5`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/e9efbf3e-355b-4b54-9c61-7a3e79247d76/tool-results/toolu_015NvA3eHHb1XM56CSMj8Vmq.txt",
  "offset": 0,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "548b1b3b-0324-445f-8bc9-d0c68204af84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LDS4mL2a55JiVqS5KszA4N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16925,
      "cache_read_input_tokens": 24556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16925
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

_source line 24 · 2026-05-15T01:15:55.099Z_

<details><summary>↩ Tool result · `toolu_01SZhxd1nEiN1WvNa2zpfyo5`</summary>

```text
0	{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml\", \"content\": \"# Literature Map — event-gated-adaptive-horizon\\n# Last updated: 2026-05-14\\n# Total: 72 papers (64 existing + 8 incremental scan 2026-05-14)\\n\\n# ============================================================\\n# EXISTING CITATIONS (already in paper.tex)\\n# ============================================================\\n\\n- paper_id: sutton1999options\\n  title: \\\"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\\\"\\n  authors: [Sutton R.S., Precup D., Singh S.]\\n  year: 1999\\n  venue: \\\"Artificial Intelligence 112(1-2):181-211\\\"\\n  category: background\\n  role: \\\"Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL\\\"\\n  relevance_score: 5\\n\\n- paper_id: hafner2020dreamerv1\\n  title: \\\"Dream to Control: Learning Behaviors by Latent Imagination\\\"\\n  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]\\n  year: 2020\\n  venue: ICLR\\n  category: background\\n  role: \\\"DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm\\\"\\n  relevance_score: 5\\n\\n- paper_id: hafner2023dreamerv3\\n  title: \\\"Mastering Diverse Domains through World Models\\\"\\n  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]\\n  year: 2023\\n  venue: \\\"arXiv:2301.04104 (Nature 2025)\\\"\\n  category: background\\n  role: \\\"DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here\\\"\\n  relevance_score: 5\\n\\n- paper_id: sharma2017figar\\n  title: \\\"Fine Grained Action Repetition for Deep Reinforcement Learning\\\"\\n  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]\\n  year: 2017\\n  venue: \\\"ICLR Workshop\\\"\\n  category: method-component\\n  role: \\\"FiGAR — learns action-repeat durations in model-free RL; we extend the idea to imagination step size in world-model RL\\\"\\n  relevance_score: 4\\n\\n- paper_id: janner2019mbpo\\n  title: \\\"When to Trust Your Model: Model-Based Policy Optimization\\\"\\n  authors: [Janner M., Fu J., Zhang M., Levine S.]\\n  year: 2019\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"MBPO — formalizes model exploitation in MBRL; our delusional critic is a specific instance of model exploitation tied to temporal embedding\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW: Multi-step prediction error compounding\\n# ============================================================\\n\\n- paper_id: ke2019learning\\n  title: \\\"Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future\\\"\\n  authors: [Ke N.R., Singh A., Touati A., Goyal A., Bengio Y., Parikh D., Batra D.]\\n  year: 2019\\n  venue: ICLR\\n  category: background\\n  role: \\\"Addresses long-term dynamics prediction via latent-variable autoregressive model; directly relevant to our finding that multi-step RSSM predictions degrade with dt>1\\\"\\n  relevance_score: 4\\n\\n- paper_id: asadi2019combating\\n  title: \\\"Combating the Compounding-Error Problem with a Multi-step Model\\\"\\n  authors: [Asadi K., Misra D., Kim S., Littman M.L.]\\n  year: 2019\\n  venue: \\\"arXiv:1905.13320\\\"\\n  category: background\\n  role: \\\"Proposes multi-step models to bypass compounding error; our work shows that even with multi-step imagination, the dt-embedding creates a different failure mode (value overestimation) distinct from compounding error\\\"\\n  relevance_score: 4\\n\\n- paper_id: venkatraman2015improving\\n  title: \\\"Improving Multi-Step Prediction of Learned Time Series Models\\\"\\n  authors: [Venkatraman A., Hebert M., Bagnell J.A.]\\n  year: 2015\\n  venue: AAAI\\n  category: background\\n  role: \\\"Data-as-Demonstrator (DaD) for robust multi-step prediction; establishes theoretical guarantee relating training error to multi-step prediction error\\\"\\n  relevance_score: 3\\n\\n- paper_id: lambert2022investigating\\n  title: \\\"Investigating Compounding Prediction Errors in Learned Dynamics Models\\\"\\n  authors: [Lambert N., Pister K.S.J., Calandra R.]\\n  year: 2022\\n  venue: \\\"arXiv:2203.09637\\\"\\n  category: background\\n  role: \\\"Empirical study of compounding error properties; we rule out compounding error as the primary failure mechanism (008c vs 008a comparison) and identify value overestimation instead\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Model-predictive control with learned dynamics\\n# ============================================================\\n\\n- paper_id: chua2018pets\\n  title: \\\"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models\\\"\\n  authors: [Chua K., Calandra R., McAllister R., Levine S.]\\n  year: 2018\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"PETS — ensemble-based uncertainty-aware MPC; uses explicit uncertainty quantification to avoid model exploitation, contrasting with DreamerV3's implicit approach\\\"\\n  relevance_score: 3\\n\\n- paper_id: nagabandi2018neural\\n  title: \\\"Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning\\\"\\n  authors: [Nagabandi A., Kahn G., Fearing R.S., Levine S.]\\n  year: 2018\\n  venue: ICRA\\n  category: background\\n  role: \\\"Demonstrates NN dynamics + MPC for locomotion; model errors accumulate over prediction horizon, motivating our investigation of horizon-dependent failures\\\"\\n  relevance_score: 3\\n\\n- paper_id: hansen2024tdmpc2\\n  title: \\\"TD-MPC2: Scalable, Robust World Models for Continuous Control\\\"\\n  authors: [Hansen N., Su H., Wang X.]\\n  year: 2024\\n  venue: \\\"ICLR (arXiv:2310.16828)\\\"\\n  category: background\\n  role: \\\"TD-MPC2 — SOTA MPC planning route (online planning + learned dynamics); DMC benchmark leader but orthogonal to imagination-based training — reviewer defense: TD-MPC2 does online MPC rollouts at test time, we study actor-critic training via imagined rollouts (DreamerV3 paradigm), not a same-level comparison\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW: Pessimistic MBRL / model exploitation mitigation\\n# ============================================================\\n\\n- paper_id: yu2020mopo\\n  title: \\\"MOPO: Model-based Offline Policy Optimization\\\"\\n  authors: [Yu T., Thomas G., Yu L., Ermon S., Zou J., Levine S., Finn C., Ma T.]\\n  year: 2020\\n  venue: \\\"NeurIPS (arXiv:2005.13239)\\\"\\n  category: background\\n  role: \\\"MOPO — pessimistic MBRL via uncertainty-penalized reward (reward -= λ * model_uncertainty); generic model exploitation mitigation — reviewer defense: MOPO addresses distribution shift in offline MBRL, our dt=1 imagination restriction targets dt_embedding-induced delusional critic (temporal conditioning corruption), two complementary mechanisms\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW: Value overestimation mitigation\\n# ============================================================\\n\\n- paper_id: thrun1993issues\\n  title: \\\"Issues in Using Function Approximation for Reinforcement Learning\\\"\\n  authors: [Thrun S., Schwartz A.]\\n  year: 1993\\n  venue: \\\"Connectionist Models Summer School\\\"\\n  category: background\\n  role: \\\"First identification of systematic value overestimation from function approximation; our delusional critic extends this to model-based imagination with temporal conditioning\\\"\\n  relevance_score: 4\\n\\n- paper_id: vanhasselt2016double\\n  title: \\\"Deep Reinforcement Learning with Double Q-Learning\\\"\\n  authors: [van Hasselt H., Guez A., Silver D.]\\n  year: 2016\\n  venue: AAAI\\n  category: background\\n  role: \\\"Double DQN — mitigates overestimation via double estimator; our finding that trained dt-embedding enables value exploitation is a complementary overestimation mechanism in MBRL\\\"\\n  relevance_score: 4\\n\\n- paper_id: fujimoto2018td3\\n  title: \\\"Addressing Function Approximation Error in Actor-Critic Methods\\\"\\n  authors: [Fujimoto S., van Hoof H., Meger D.]\\n  year: 2018\\n  venue: ICML\\n  category: method-component\\n  role: \\\"TD3 — clipped double-Q to limit overestimation in actor-critic; DreamerV3 uses a single critic, making it more vulnerable to the overestimation we identify\\\"\\n  relevance_score: 4\\n\\n- paper_id: haarnoja2018sac\\n  title: \\\"Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor\\\"\\n  authors: [Haarnoja T., Zhou A., Abbeel P., Levine S.]\\n  year: 2018\\n  venue: ICML\\n  category: method-component\\n  role: \\\"SAC — entropy regularization implicitly mitigates overestimation; relevant contrast to DreamerV3's actor which can greedily exploit overestimated values\\\"\\n  relevance_score: 3\\n\\n- paper_id: lee2021sunrise\\n  title: \\\"SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning\\\"\\n  authors: [Lee K., Laskin M., Srinivas A., Abbeel P.]\\n  year: 2021\\n  venue: ICML\\n  category: method-component\\n  role: \\\"Ensemble-based uncertainty weighting for value estimation; potential mitigation for our identified delusional critic mechanism\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Delusional bias\\n# ============================================================\\n\\n- paper_id: lu2018nondelusional\\n  title: \\\"Non-delusional Q-learning and Value-Iteration\\\"\\n  authors: [Lu T., Schuurmans D., Boutilier C.]\\n  year: 2018\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"Formalizes delusional bias from policy-class constraints in Q-learning; we identify an analogous phenomenon where temporal conditioning enables the critic to exploit model imprecision\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW: Hierarchical RL with learned models\\n# ============================================================\\n\\n- paper_id: hafner2022director\\n  title: \\\"Deep Hierarchical Planning from Pixels\\\"\\n  authors: [Hafner D., Lee K.-H., Fischer I., Abbeel P.]\\n  year: 2022\\n  venue: NeurIPS\\n  category: direct-competitor\\n  role: \\\"Director — hierarchical planning in Dreamer latent space via subgoals; addresses temporal abstraction through goal hierarchy rather than variable dt\\\"\\n  relevance_score: 4\\n\\n- paper_id: nachum2018hiro\\n  title: \\\"Data-Efficient Hierarchical Reinforcement Learning\\\"\\n  authors: [Nachum O., Gu S., Lee H., Levine S.]\\n  year: 2018\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"HIRO — off-policy HRL with learned subgoals; demonstrates that hierarchical temporal abstraction can improve sample efficiency when properly designed\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Action repeat / frame skip\\n# ============================================================\\n\\n- paper_id: braylan2015frame\\n  title: \\\"Frame Skip Is a Powerful Parameter for Learning to Play Atari\\\"\\n  authors: [Braylan A., Hollenbeck M., Meyerson E., Miikkulainen R.]\\n  year: 2015\\n  venue: \\\"AAAI Workshop on Learning for General Competency in Video Games\\\"\\n  category: background\\n  role: \\\"Empirical study showing frame skip strongly affects Atari performance; motivates investigation of temporal granularity as a critical design choice\\\"\\n  relevance_score: 3\\n\\n- paper_id: lakshminarayanan2017dynamic\\n  title: \\\"Dynamic Action Repetition for Deep Reinforcement Learning\\\"\\n  authors: [Lakshminarayanan A.S., Sharma S., Ravindran B.]\\n  year: 2017\\n  venue: AAAI\\n  category: method-component\\n  role: \\\"Learns per-step action repetition duration; model-free analog of our variable-dt imagination approach\\\"\\n  relevance_score: 4\\n\\n- paper_id: biedenkapp2021temporl\\n  title: \\\"TempoRL: Learning When to Act\\\"\\n  authors: [Biedenkapp A., Rajan R., Hutter F., Lindauer M.]\\n  year: 2021\\n  venue: ICML\\n  category: method-component\\n  role: \\\"Learns action persistence via skip-policy; demonstrates up to 10x speedup — but in model-free setting without the model exploitation risk we identify\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW: DreamerV2\\n# ============================================================\\n\\n- paper_id: hafner2021dreamerv2\\n  title: \\\"Mastering Atari with Discrete World Models\\\"\\n  authors: [Hafner D., Lillicrap T., Norouzi M., Ba J.]\\n  year: 2021\\n  venue: ICLR\\n  category: background\\n  role: \\\"DreamerV2 — introduces discrete latent representations used in DreamerV3; key architectural predecessor to our base system\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW: Alternative world model architectures\\n# ============================================================\\n\\n- paper_id: micheli2023iris\\n  title: \\\"Transformers are Sample-Efficient World Models\\\"\\n  authors: [Micheli V., Alonso E., Fleuret F.]\\n  year: 2023\\n  venue: ICLR\\n  category: background\\n  role: \\\"IRIS — autoregressive transformer world model; alternative to RSSM that may exhibit different compounding error characteristics under temporal abstraction\\\"\\n  relevance_score: 3\\n\\n- paper_id: robine2023twm\\n  title: \\\"Transformer-based World Models Are Happy With 100k Interactions\\\"\\n  authors: [Robine J., Hoeftmann M., Uelwer T., Harmeling S.]\\n  year: 2023\\n  venue: ICLR\\n  category: background\\n  role: \\\"TWM — Transformer-XL world model with direct state access; circumvents RSSM's recurrent compression that exacerbates our identified prediction gap\\\"\\n  relevance_score: 3\\n\\n- paper_id: chen2022transdreamer\\n  title: \\\"TransDreamer: Reinforcement Learning with Transformer World Models\\\"\\n  authors: [Chen C., Wu Y.-F., Yoon J., Ahn S.]\\n  year: 2022\\n  venue: \\\"arXiv:2202.09481\\\"\\n  category: background\\n  role: \\\"Replaces RSSM with Transformer State-Space Model; directly tests whether RSSM-specific architecture contributes to temporal abstraction failures\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: 2024-2026 concurrent work on temporal abstraction in world models\\n# ============================================================\\n\\n- paper_id: gumbsch2024thick\\n  title: \\\"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics\\\"\\n  authors: [Gumbsch C., Sajid N., Martius G., Butz M.V.]\\n  year: 2024\\n  venue: ICLR\\n  category: direct-competitor\\n  role: \\\"THICK — learns adaptive temporal abstractions via context-change detection; closest concurrent work — addresses temporal abstraction in Dreamer but via hierarchy rather than variable-dt imagination\\\"\\n  relevance_score: 5\\n\\n- paper_id: mattes2024hieros\\n  title: \\\"Hieros: Hierarchical Imagination on Structured State Space Sequence World Models\\\"\\n  authors: [Mattes P., Schlosser R., Herbrich R.]\\n  year: 2024\\n  venue: ICML\\n  category: direct-competitor\\n  role: \\\"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW: Seed-dependent instability & value overestimation in MBRL\\n# ============================================================\\n\\n- paper_id: henderson2018deep\\n  title: \\\"Deep Reinforcement Learning that Matters\\\"\\n  authors: [Henderson P., Islam R., Bachman P., Pineau J., Precup D., Meger D.]\\n  year: 2018\\n  venue: AAAI\\n  category: background\\n  role: \\\"Foundational study on seed variance in deep RL — shows statistically different performance distributions arise from random seeds alone with identical hyperparameters; directly supports our observation that seed 0 vs seed 2 produce qualitatively different value dynamics under the same dt_embed_dim=0 config\\\"\\n  relevance_score: 4\\n\\n- paper_id: nikishin2022primacy\\n  title: \\\"The Primacy Bias in Deep Reinforcement Learning\\\"\\n  authors: [Nikishin E., Schwarzer M., D'Oro P., Bacon P.-L., Courville A.]\\n  year: 2022\\n  venue: ICML\\n  category: background\\n  role: \\\"Identifies primacy bias — agents overfit early data and lose ability to learn from new transitions, leading to delayed performance collapse; parallels our finding where value overestimation initially appears benign but becomes pathological later, and the collapse timing is seed-dependent\\\"\\n  relevance_score: 4\\n\\n- paper_id: qiao2023mind\\n  title: \\\"Mind the Model, Not the Agent: The Primacy Bias in Model-based RL\\\"\\n  authors: [Qiao Z., Lyu J., Li X.]\\n  year: 2023\\n  venue: \\\"arXiv:2310.15017 (ECAI 2024)\\\"\\n  category: evaluation\\n  role: \\\"Extends primacy bias to MBRL, testing on DreamerV2 — shows world model primacy bias dominates over agent primacy bias; directly relevant to Dreamer-family training instability and explains why some seeds recover (model escapes early overfitting) while others don't\\\"\\n  relevance_score: 5\\n\\n- paper_id: hussing2024dissecting\\n  title: \\\"Dissecting Deep RL with High Update Ratios: Combatting Value Divergence\\\"\\n  authors: [Hussing M., Voelcker C.A., Gilitschenski I., Farahmand A.-M., Eaton E.]\\n  year: 2024\\n  venue: \\\"Reinforcement Learning Journal (RLC 2024)\\\"\\n  category: evaluation\\n  role: \\\"Shows value overestimation and Q-divergence under high update-to-data ratios, driven by optimizer momentum — overestimation occurs on both in-distribution and OOD data; mechanism maps to our delusional critic where imagination-trained critic inflates values progressively, with divergence onset sensitive to initialization\\\"\\n  relevance_score: 4\\n\\n- paper_id: barkley2024stealing\\n  title: \\\"Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning\\\"\\n  authors: [Barkley B., Fridovich-Keil D.]\\n  year: 2024\\n  venue: \\\"arXiv:2412.14312 (ICML 2025)\\\"\\n  category: evaluation\\n  role: \\\"Demonstrates that synthetic rollouts (imagination) can degrade performance inconsistently across environments, with overestimation bias as a contributing factor; supports our finding that imagination-based training creates environment- and seed-dependent failure modes that existing mitigation techniques do not reliably fix\\\"\\n  relevance_score: 3\\n\\n- paper_id: bjorck2022variance\\n  title: \\\"Is High Variance Unavoidable in RL? A Case Study in Continuous Control\\\"\\n  authors: [Bjorck J., Gomes C.P., Weinberger K.Q.]\\n  year: 2022\\n  venue: ICLR\\n  category: background\\n  role: \\\"Shows RL variance mostly arises early in training from poor 'outlier' runs caused by numerical instability; parallels our observation that seed 2 diverges early while seed 0 recovers — the reward prediction degradation from removing dt_embedding may create exactly this early-training instability\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Reward prediction quality → MBRL performance\\n# ============================================================\\n# Our key finding: removing dt_embedding causes reward_MAE to spike 75x\\n# (0.01 → 0.747), making performance seed-dependent. These papers\\n# establish that reward prediction quality is a known MBRL bottleneck.\\n\\n- paper_id: lee2024dreamsmooth\\n  title: \\\"DreamSmooth: Improving Model-based Reinforcement Learning via Reward Smoothing\\\"\\n  authors: [Lee V., Abbeel P., Lee Y.]\\n  year: 2024\\n  venue: ICLR\\n  category: background\\n  role: \\\"Directly demonstrates reward prediction is a bottleneck in MBRL — sparse/ambiguous rewards cause the reward model to predict zeros, creating gradient-free landscapes during imagination; our dt_embed_dim=0 ablation creates an analogous bottleneck where the reward head loses temporal conditioning and MAE spikes 75x\\\"\\n  relevance_score: 5\\n\\n- paper_id: ma2024harmonydream\\n  title: \\\"HarmonyDream: Task Harmonization Inside World Models\\\"\\n  authors: [Ma H., Wu J., Feng N., Xiao C., Li D., Hao J., Wang J., Long M.]\\n  year: 2024\\n  venue: ICML\\n  category: background\\n  role: \\\"Shows observation prediction dominates reward prediction in world model training, degrading reward model quality; proposes dynamic loss balancing for 10-69% gains — directly relevant to our finding that dt_embedding removal disrupts the observation-reward prediction balance and causes reward MAE explosion\\\"\\n  relevance_score: 5\\n\\n- paper_id: lambert2020objective\\n  title: \\\"Objective Mismatch in Model-based Reinforcement Learning\\\"\\n  authors: [Lambert N., Amos B., Yadan O., Calandra R.]\\n  year: 2020\\n  venue: \\\"L4DC (Proceedings of Machine Learning Research, vol. 120)\\\"\\n  category: background\\n  role: \\\"Formalizes that one-step prediction likelihood does not correlate with control performance — the 'objective mismatch' problem; our work reveals a specific instance: the reward head's prediction accuracy (measured by MAE) directly gates whether the critic can learn stable value estimates, creating a reward-specific objective mismatch\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW: Auxiliary tasks & representation coupling in world models\\n# ============================================================\\n# Our finding: reward prediction quality is tightly coupled to temporal\\n# conditioning (dt_embedding). Removing the embedding degrades the\\n# reward head while dynamics remain intact — suggesting the reward head\\n# acts as more than a passive predictor; it conditions the shared\\n# representation. Literature gap: no prior work studies this coupling\\n# specifically in Dreamer-family world models.\\n\\n- paper_id: jaderberg2017unreal\\n  title: \\\"Reinforcement Learning with Unsupervised Auxiliary Tasks\\\"\\n  authors: [Jaderberg M., Mnih V., Czarnecki W.M., Schaul T., Leibo J.Z., Silver D., Kavukcuoglu K.]\\n  year: 2017\\n  venue: ICLR\\n  category: background\\n  role: \\\"UNREAL — introduces reward prediction as an auxiliary task that shapes shared representations; foundational evidence that reward prediction is not just a passive output but actively conditions what features the network learns — our finding that removing dt_embedding selectively degrades reward prediction (but not dynamics) suggests the temporal conditioning specifically enables reward-relevant feature extraction\\\"\\n  relevance_score: 4\\n\\n- paper_id: lyle2021auxiliary\\n  title: \\\"On The Effect of Auxiliary Tasks on Representation Dynamics\\\"\\n  authors: [Lyle C., Rowland M., Ostrovski G., Dabney W.]\\n  year: 2021\\n  venue: AISTATS\\n  category: background\\n  role: \\\"Theoretical analysis showing auxiliary tasks shape representations toward top eigenvectors of the transition operator; provides formal grounding for why removing temporal conditioning from the reward head could alter the entire representation — the reward head's gradients contribute to spectral structure of the shared latent space\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW: DreamerV3 architecture improvements (2025-2026)\\n# ============================================================\\n\\n- paper_id: bredis2026nedreamer\\n  title: \\\"Next Embedding Prediction Makes World Models Stronger\\\"\\n  authors: [Bredis G., Balagansky N., Gavrilov D., Rakhimov R.]\\n  year: 2026\\n  venue: \\\"arXiv:2603.02765\\\"\\n  category: background\\n  role: \\\"NE-Dreamer — decoder-free MBRL replacing pixel reconstruction with next-embedding prediction via temporal transformer + Barlow Twins; improves RSSM prediction quality on DMC and DMLab but does not address temporal abstraction or delusional critic — orthogonal to our dt-embedding diagnosis\\\"\\n  relevance_score: 3\\n\\n- paper_id: zhang2025dymodreamer\\n  title: \\\"DyMoDreamer: World Modeling with Dynamic Modulation\\\"\\n  authors: [Zhang B., Wang R., Xiao W., Zhang W., Sun J., Huang G., Chen J., Wang G.]\\n  year: 2025\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"Modulates RSSM via inter-frame differencing mask and stochastic categorical dynamic modulation; SOTA on Atari 100k (156.6% HNS) and DMC (832) — improves dynamics extraction but does not address variable-rate imagination or dt_embedding-induced value overestimation\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Temporal abstraction methods\\n# ============================================================\\n\\n- paper_id: liu2025vanta\\n  title: \\\"Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning\\\"\\n  authors: [Liu T.-S., Liu X.-H., Chen R., Jin L., Wang P., Zhang Z., Yu Y.]\\n  year: 2025\\n  venue: ICLR\\n  category: method-component\\n  role: \\\"VanTA — VLM-guided trajectory decomposition into semantically meaningful skills via vector quantization + relabeling; operates at high-level skill abstraction (Franka Kitchen, Crafter) — contrasts with our low-level dt-based temporal abstraction within world-model imagination steps\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Evaluation methodology\\n# ============================================================\\n\\n- paper_id: agarwal2021precipice\\n  title: \\\"Deep Reinforcement Learning at the Edge of the Statistical Precipice\\\"\\n  authors: [Agarwal R., Schwarzer M., Castro P.S., Courville A.C., Bellemare M.]\\n  year: 2021\\n  venue: NeurIPS\\n  category: evaluation\\n  role: \\\"Proposes rliable — interval estimates, performance profiles, IQM for robust multi-seed RL evaluation (NeurIPS Outstanding Paper); our multi-seed experiment design follows this methodology to ensure statistical validity of collapse detection across seeds\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW (2026-05-14 gap analysis): Time discretization theory\\n# ============================================================\\n# Gap: variable timestep / time discretization invariance — foundational\\n# theory for why dt matters and how to handle it.\\n\\n- paper_id: tallec2019making\\n  title: \\\"Making Deep Q-learning methods Robust to Time Discretization\\\"\\n  authors: [Tallec C., Blier L., Ollivier Y.]\\n  year: 2019\\n  venue: \\\"ICML (arXiv:1901.09732)\\\"\\n  category: background\\n  role: \\\"Shows Q-learning performance is highly sensitive to time discretization δ; proposes architectural + exploration modifications for δ-invariance. Theoretical foundation for why our variable-dt imagination introduces a fundamental difficulty: RSSM trained at δ=1 cannot produce δ-invariant predictions at dt>1\\\"\\n  relevance_score: 4\\n\\n- paper_id: park2021sar\\n  title: \\\"Time Discretization-Invariant Safe Action Repetition for Policy Gradient Methods\\\"\\n  authors: [Park S., Kim J., Kim G.]\\n  year: 2021\\n  venue: \\\"NeurIPS (arXiv:2111.03941)\\\"\\n  category: method-component\\n  role: \\\"SAR — δ-invariant action repetition for policy gradients; achieves time-discretization robustness in model-free RL via adaptive reaction to state changes during repetition. Contrasts with our finding that world-model RL lacks this robustness when imagination uses dt>1\\\"\\n  relevance_score: 4\\n\\n- paper_id: wang2024seac\\n  title: \\\"Reinforcement Learning with Elastic Time Steps\\\"\\n  authors: [Wang D., Beltrame G.]\\n  year: 2024\\n  venue: \\\"arXiv:2402.14961\\\"\\n  category: method-component\\n  role: \\\"SEAC/MOSEAC — variable-duration time steps where agent selects both action and duration; model-free approach that explicitly treats action duration as part of the action space. Our work reveals why this strategy is problematic in world-model RL: the critic cannot reliably evaluate variable-duration imagined trajectories\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW (2026-05-14 gap analysis): Delusional bias mitigation\\n# ============================================================\\n\\n- paper_id: su2020conqur\\n  title: \\\"ConQUR: Mitigating Delusional Bias in Deep Q-learning\\\"\\n  authors: [Su D., Ooi J., Lu T., Schuurmans D., Boutilier C.]\\n  year: 2020\\n  venue: \\\"ICML (arXiv:2002.12399)\\\"\\n  category: background\\n  role: \\\"Follow-up to Lu et al. 2018; mitigates delusional bias via consistency-penalized Q-labels. Addresses delusional bias from policy-class constraints in Q-learning; our delusional critic is an analogous phenomenon in MBRL where temporal conditioning (dt_embedding) creates inconsistent value targets across imagination steps\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW (2026-05-14 gap analysis): Diagnostic methodology in RL\\n# ============================================================\\n# Gap: our paper is a diagnostic analysis — need methodological\\n# precedents for \\\"what matters\\\" / \\\"implementation matters\\\" style papers.\\n\\n- paper_id: engstrom2020implementation\\n  title: \\\"Implementation Matters in Deep Policy Gradients: A Case Study on PPO and TRPO\\\"\\n  authors: [Engstrom L., Ilyas A., Santurkar S., Tsipras D., Janoos F., Rudolph L., Madry A.]\\n  year: 2020\\n  venue: \\\"ICLR (arXiv:2005.12729)\\\"\\n  category: evaluation\\n  role: \\\"Demonstrates that code-level implementation details (not algorithmic innovations) drive most of PPO's gains over TRPO; methodological precedent for our diagnostic approach — we similarly show that a specific implementation choice (trained vs. untrained dt_embedding) is the primary factor determining collapse vs. stability\\\"\\n  relevance_score: 4\\n\\n- paper_id: andrychowicz2021whatmatters\\n  title: \\\"What Matters for On-Policy Deep Actor-Critic Methods? A Large-Scale Study\\\"\\n  authors: [Andrychowicz M., Raichuk A., Stańczyk P., Orsini M., Girgin S., Marinier R., Hussenot L., Geist M., Pietquin O., Michalski M., Gelly S., Bachem O.]\\n  year: 2021\\n  venue: \\\"ICLR (arXiv:2006.05990)\\\"\\n  category: evaluation\\n  role: \\\"Large-scale factorial study of 50+ design choices in on-policy RL (250K+ agents); methodological template for our factorial experiment design isolating dt_embedding × subsample × horizon effects. Demonstrates that systematic ablation reveals non-obvious interactions — parallel to our finding that dt_embedding training status interacts with subsample and horizon\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW (2026-05-14 gap analysis): MBRL rollout quality & value overestimation\\n# ============================================================\\n# Gap: recent ICLR 2025 papers directly studying imagination rollout\\n# quality and value overestimation in model-based settings.\\n\\n- paper_id: frauenknecht2025rollouts\\n  title: \\\"On Rollouts in Model-Based Reinforcement Learning\\\"\\n  authors: [Frauenknecht B., Subhasish D., Solowjow F., Trimpe S.]\\n  year: 2025\\n  venue: \\\"ICLR (arXiv:2501.16918)\\\"\\n  category: evaluation\\n  role: \\\"Shows trajectory-sampling rollouts diverge from ground truth after few steps and can harm policy learning; proposes Infoprop separating aleatoric/epistemic uncertainty with rollout termination criteria. Directly supports our finding that dt>1 imagination produces corrupted data — our work identifies a specific mechanism (dt_embedding-induced value exploitation) beyond general compounding error\\\"\\n  relevance_score: 5\\n\\n- paper_id: voelcker2025madtd\\n  title: \\\"MAD-TD: Model-Augmented Data stabilizes High Update Ratio RL\\\"\\n  authors: [Voelcker C., Hussing M., Eaton E., Farahmand A.-M., Gilitschenski I.]\\n  year: 2025\\n  venue: \\\"ICLR (arXiv:2410.08896)\\\"\\n  category: evaluation\\n  role: \\\"Shows value function misgeneralization to on-policy actions causes instability at high UTD ratios; uses model-generated data to improve value accuracy. Complementary to our finding: MAD-TD addresses value misgeneralization from replay distribution mismatch, we address value overestimation from temporal conditioning corruption in imagination\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW (2026-05-14 gap analysis): Latest action repeat methods\\n# ============================================================\\n\\n- paper_id: nie2025sdar\\n  title: \\\"Select before Act: Spatially Decoupled Action Repetition for Continuous Control\\\"\\n  authors: [Nie B., et al.]\\n  year: 2025\\n  venue: \\\"ICLR (arXiv:2502.06919)\\\"\\n  category: method-component\\n  role: \\\"SDAR — per-dimension action repetition decisions for flexible temporal persistence in model-free RL; SOTA on DMC continuous control. Advances action repeat in model-free setting; our work shows the fundamental obstacle to analogous variable-rate approaches in model-based RL (delusional critic from dt_embedding)\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW (2026-05-14 gap analysis): DreamerV4 / latest Dreamer evolution\\n# ============================================================\\n\\n- paper_id: hafner2025dreamerv4\\n  title: \\\"Training Agents Inside of Scalable World Models\\\"\\n  authors: [Hafner D., Yan W.]\\n  year: 2025\\n  venue: \\\"arXiv:2509.24527\\\"\\n  category: background\\n  role: \\\"DreamerV4 — replaces RSSM with efficient transformer world model + shortcut forcing; scales to video pretraining (Minecraft diamonds from video). Architectural successor to DreamerV3; our dt_embedding diagnosis is specific to RSSM but the broader lesson (temporal conditioning must match model fidelity) applies to transformer world models\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW (2026-05-14): Training instability dynamics\\n# ============================================================\\n\\n- paper_id: zhang2026instability\\n  title: \\\"Training instability in deep learning follows low-dimensional dynamical principles\\\"\\n  authors: [Zhang L., et al.]\\n  year: 2026\\n  venue: \\\"ICLR 2026 (arXiv:2601.13160)\\\"\\n  category: background\\n  role: \\\"Training instability follows low-dimensional dynamical principles; provides theoretical framework for why seed-dependent collapse vs self-correction occurs in our experiments (008d seed 1 collapses, 009b seed 2 self-corrects under identical config)\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW (2026-05-14): Seed-Dependent Stochastic Outcomes in MBRL\\n# ============================================================\\n# Dedicated literature survey for the stochastic collapse phenomenon:\\n# same config (trained dt_embedding + subsample + H=8) produces\\n# collapse in seed 0 (008d) but self-correction in seed 2 (009b).\\n# nve>1.5x is a 100% reliable marker of trained dt_embedding,\\n# but collapse itself is stochastic (1/2 seeds).\\n\\n- paper_id: sokar2023dormant\\n  title: \\\"The Dormant Neuron Phenomenon in Deep Reinforcement Learning\\\"\\n  authors: [Sokar G., Agarwal R., Castro P.S., Evci U.]\\n  year: 2023\\n  venue: \\\"ICML 2023\\\"\\n  category: background\\n  role: \\\"Identifies dormant neurons — inactive units accumulating during RL training that reduce network expressivity. Seed-dependent because different random initializations produce different early dormancy patterns; directly explains why some seeds lose the representational capacity needed to self-correct value overestimation (our seed 0 collapses) while others retain enough active neurons to recover (our seed 2 self-corrects)\\\"\\n  relevance_score: 4\\n  survey_tag: seed-dependent-stochastic-outcomes\\n\\n- paper_id: lyle2022capacity\\n  title: \\\"Understanding and Preventing Capacity Loss in Reinforcement Learning\\\"\\n  authors: [Lyle C., Rowland M., Dabney W.]\\n  year: 2022\\n  venue: \\\"ICLR 2023 (arXiv:2204.09560)\\\"\\n  category: background\\n  role: \\\"Shows feature rank collapse from non-stationary TD targets is a necessary condition for learning failure but not sufficient — sparse rewards and other factors must co-occur. Directly parallels our finding: nve>1.5x (value overestimation from trained dt_embedding) is a necessary precondition for collapse but not a sufficient one; additional stochastic factors (initialization, early replay composition) determine whether collapse actually occurs\\\"\\n  relevance_score: 5\\n  survey_tag: seed-dependent-stochastic-outcomes\\n\\n- paper_id: kumar2022dr3\\n  title: \\\"DR3: Value-Based Deep Reinforcement Learning Requires Explicit Regularization\\\"\\n  authors: [Kumar A., Agarwal R., Ma T., Courville A., Tucker G., Levine S.]\\n  year: 2022\\n  venue: \\\"ICLR 2022\\\"\\n  category: background\\n  role: \\\"Shows implicit regularization from TD learning favors degenerate feature aliasing (states on both sides of Bellman backup become indistinguishable), creating the substrate for value overestimation. In our setting, trained dt_embedding amplifies this aliasing across different temporal horizons — the critic cannot distinguish between dt=1 and dt>1 value targets, enabling exploitation. Feature aliasing is seed-dependent because it depends on initialization geometry\\\"\\n  relevance_score: 4\\n  survey_tag: seed-dependent-stochastic-outcomes\\n\\n- paper_id: colas2018seeds\\n  title: \\\"How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments\\\"\\n  authors: [Colas C., Sigaud O., Oudeyer P.-Y.]\\n  year: 2018\\n  venue: \\\"arXiv:1806.08295\\\"\\n  category: evaluation\\n  role: \\\"Provides statistical framework for determining seed count needed for significant algorithm comparison; our 2-seed observation (1/2 collapse) has limited statistical power by their analysis — but the qualitative difference (nve 4.12x vs 0.38x) is large enough that even 2 seeds establish the stochastic nature of the phenomenon. Methodological basis for future multi-seed validation\\\"\\n  relevance_score: 3\\n  survey_tag: seed-dependent-stochastic-outcomes\\n\\n- paper_id: nikishin2023plasticity\\n  title: \\\"Deep Reinforcement Learning with Plasticity Injection\\\"\\n  authors: [Nikishin E., Oh J., Ostrovski G., Lyle C., Pascanu R., Dabney W., Barreto A.]\\n  year: 2023\\n  venue: \\\"NeurIPS 2023\\\"\\n  category: method-component\\n  role: \\\"Plasticity injection augments network plasticity without changing parameter count; serves as a diagnostic tool — if injection improves performance, plasticity loss was the bottleneck. Directly applicable to diagnosing whether our seed-dependent collapse is plasticity-mediated: if plasticity injection prevents collapse in seed 0 but has no effect on seed 2 (which already self-corrects), it confirms plasticity loss as the bifurcation mechanism\\\"\\n  relevance_score: 4\\n  survey_tag: seed-dependent-stochastic-outcomes\\n\\n- paper_id: schwarzer2023bbf\\n  title: \\\"Bigger, Better, Faster: Human-level Atari with Human-level Efficiency\\\"\\n  authors: [Schwarzer M., Obando-Ceron J.S., Courville A., Bellemare M., Agarwal R., Castro P.S.]\\n  year: 2023\\n  venue: \\\"ICML 2023\\\"\\n  category: method-component\\n  role: \\\"BBF achieves SOTA sample efficiency via periodic network resets + scaling + weight decay; periodic resets prevent primacy bias accumulation across seeds. Suggests our delusional critic collapse might be preventable with periodic critic resets — the reset would break the positive feedback loop between overestimated values and actor exploitation before it becomes irreversible\\\"\\n  relevance_score: 3\\n  survey_tag: seed-dependent-stochastic-outcomes\\n\\n- paper_id: farebrother2024stopregressing\\n  title: \\\"Stop Regressing: Training Value Functions via Classification for Scalable Deep RL\\\"\\n  authors: [Farebrother J., Orbay J., Vuong Q., Taiga A.A., Chebotar Y., Xiao T., Irpan A., Levine S., Castro P.S., Faust A., Kumar A., Agarwal R.]\\n  year: 2024\\n  venue: \\\"ICML 2024\\\"\\n  category: method-component\\n  role: \\\"Shows categorical cross-entropy for value training provides implicit regularization against overestimation vs MSE regression. DreamerV3 already uses categorical value prediction (twohot + symlog) — yet our trained dt_embedding still induces collapse in some seeds, demonstrating that categorical value training is insufficient to prevent dt_embedding-induced value exploitation\\\"\\n  relevance_score: 3\\n  survey_tag: seed-dependent-stochastic-outcomes\\n\\n- paper_id: lyle2024normalization\\n  title: \\\"Normalization and Effective Learning Rates in Reinforcement Learning\\\"\\n  authors: [Lyle C., Zheng Z., Giunchiglia E., Sherstan C., Hashemizadeh M., Schuurmans D., Dabney W.]\\n  year: 2024\\n  venue: \\\"NeurIPS 2024\\\"\\n  category: background\\n  role: \\\"Shows normalization layers combat overestimation but cause effective learning rate decay via parameter norm growth. Provides a potential mechanism for seed 2's self-correction: if parameter norms grow faster in certain initializations, effective LR decays faster, naturally damping value overestimation before it cascades into collapse. Seed 0's slower norm growth → sustained high effective LR → overestimation compounds → collapse\\\"\\n  relevance_score: 4\\n  survey_tag: seed-dependent-stochastic-outcomes\\n\\n# --- Survey synthesis: Seed-Dependent Stochastic Outcomes ---\\n# Summary (2026-05-14):\\n#\\n# 1. STOCHASTIC COLLAPSE HAS PRECEDENT:\\n#    Plasticity loss (Lyle 2022, Sokar 2023, Nikishin 2023) is inherently\\n#    seed-dependent because it depends on initialization → early gradient\\n#    dynamics → neuron activity patterns. Different seeds hit different\\n#    plasticity trajectories under identical configs.\\n#\\n# 2. nve>1.5x AS DIAGNOSTIC MARKER (necessary but not sufficient):\\n#    Lyle 2022 shows feature rank collapse is necessary but not sufficient\\n#    for learning failure. Kumar 2022 shows feature aliasing from TD\\n#    learning creates the overestimation substrate. Our nve>1.5x is\\n#    analogous: it indicates the dt_embedding has enabled value exploitation\\n#    (100% reliable marker), but collapse requires additional conditions\\n#    (plasticity loss, insufficient effective LR decay) that are stochastic.\\n#\\n# 3. SELF-CORRECTION MECHANISM:\\n#    Lyle 2024 provides a candidate mechanism: normalization-induced\\n#    effective LR decay can naturally damp overestimation in some seeds.\\n#    Farebrother 2024 shows categorical value training provides partial\\n#    implicit regularization. Together these explain why seed 2 self-corrects:\\n#    the combination of DreamerV3's categorical critic + normalization +\\n#    favorable initialization produces enough implicit regularization to\\n#    overcome the dt_embedding-induced overestimation.\\n#\\n# 4. THEORETICAL GROUNDING:\\n#    Zhang 2026 (already in map) provides the dynamical systems framework.\\n#    Bjorck 2022 (already in map) shows early outlier events dominate\\n#    variance. Together with the new papers, the framing is:\\n#    \\\"trained dt_embedding creates a necessary condition (nve>1.5x) for\\n#    delusional critic collapse, but collapse is a stochastic bifurcation\\n#    whose outcome depends on seed-dependent plasticity dynamics.\\\"\\n\\n# ============================================================\\n# INCREMENTAL SCAN (2026-05-14): Δt conditioning & adaptive horizon\\n# ============================================================\\n# 8 new papers from targeted search on:\\n#   - Δt/timestep conditioning in world models\\n#   - Variable-rate imagination / adaptive horizon\\n#   - Hierarchical planning with latent world models (2025-2026)\\n#\\n# KEY FINDING: TAWM (Nhu et al. ICML 2025) explicitly conditions\\n# world model on Δt — closest methodological overlap. But TAWM\\n# uses TD-MPC2 (online MPC) not imagination-based actor-critic,\\n# and treats Δt conditioning as beneficial. Our work diagnoses\\n# Δt conditioning as pathological in imagination-based training\\n# (delusional critic). Complementary, not duplicative.\\n\\n- paper_id: nhu2025tawm\\n  title: \\\"Time-Aware World Model for Adaptive Prediction and Control\\\"\\n  authors: [Nhu A.N., Son S., Lin M.C.]\\n  year: 2025\\n  venue: \\\"ICML 2025 (arXiv:2506.08441)\\\"\\n  category: direct-competitor\\n  role: \\\"TAWM — explicitly conditions world model on time-step size Δt and trains over diverse Δt values for multi-rate dynamics learning. Built on TD-MPC2 (online MPC). KEY DISTINCTION from our work: (1) TAWM treats Δt conditioning as beneficial for performance/data-efficiency; we diagnose it as pathological in imagination-based actor-critic training (delusional critic). (2) TAWM uses MPC (no imagination rollouts for policy training); our failure mode is specific to imagination-based training where the critic exploits dt-conditioned value estimates. (3) TAWM focuses on observation-rate robustness; we focus on value overestimation from temporal conditioning corruption. TAWM actually strengthens our contribution: it shows Δt conditioning works in MPC settings, making our finding that it fails in imagination-based settings a surprising and important diagnostic.\\\"\\n  relevance_score: 5\\n  novelty_threat: \\\"MEDIUM — methodological overlap (Δt conditioning) but fundamentally different paradigm (MPC vs imagination) and opposite conclusion (beneficial vs pathological). Must cite and differentiate in paper.\\\"\\n\\n- paper_id: li2025lsimagine\\n  title: \\\"Open-World Reinforcement Learning over Long Short-Term Imagination\\\"\\n  authors: [Li J., Wang Q., Wang Y., Jin X., Li Y., Zeng W., Yang X.]\\n  year: 2025\\n  venue: \\\"ICLR 2025 Oral (arXiv:2410.03618)\\\"\\n  category: direct-competitor\\n  role: \\\"LS-Imagine — extends imagination horizon in Dreamer via goal-conditioned jumpy state transitions and affordance maps. Addresses the 'short-sightedness' of standard Dreamer imagination. KEY DISTINCTION: LS-Imagine adds jumpy transitions to reach long-horizon targets (open-world Minecraft), while our work shows that variable-dt imagination itself introduces delusional critic. LS-Imagine's jumpy transitions use goal conditioning (not dt-embedding), potentially avoiding the value overestimation we identify.\\\"\\n  relevance_score: 4\\n  novelty_threat: \\\"LOW — different mechanism (goal-conditioned jumps vs dt-embedding) and different focus (long-horizon exploration vs diagnostic of failure modes). Should cite as concurrent approach to extending imagination horizon.\\\"\\n\\n- paper_id: zhang2026hwm\\n  title: \\\"Hierarchical Planning with Latent World Models\\\"\\n  authors: [Zhang W., Terver B., Zholus A., Chitnis S., Sutaria H., Assran M., Balestriero R., Bar A., Bardes A., LeCun Y., Ballas N.]\\n  year: 2026\\n  venue: \\\"arXiv:2604.03208\\\"\\n  category: direct-competitor\\n  role: \\\"HWM — learns multi-scale latent world models for hierarchical MPC planning; high-level planner optimizes macro-actions, low-level planner handles primitives. 70% success on real-world non-greedy robotic tasks vs 0% for single-level. Addresses temporal abstraction via hierarchical planning (MPC), not imagination-based actor-critic. Further evidence that temporal abstraction in world models requires hierarchy rather than single-scale variable-dt approaches.\\\"\\n  relevance_score: 4\\n  novelty_threat: \\\"LOW — MPC-based hierarchical planning, not imagination-based training. Supports our thesis that flat dt-embedding approaches are inferior to hierarchical alternatives.\\\"\\n\\n- paper_id: kobayashi2025metacontroller\\n  title: \\\"Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning\\\"\\n  authors: [Kobayashi S., et al.]\\n  year: 2025\\n  venue: \\\"arXiv:2512.20605\\\"\\n  category: method-component\\n  role: \\\"MetaController — discovers temporal abstractions via higher-order non-causal sequence model controlling base autoregressive model's residual stream. Each controller executes behaviorally meaningful action sequences with learned termination conditions. Operates in fundamentally different paradigm (LLM-style autoregressive models, not world-model imagination), but demonstrates that temporal abstraction benefits from hierarchical structure rather than flat dt-conditioning.\\\"\\n  relevance_score: 3\\n\\n- paper_id: shaj2023mts3\\n  title: \\\"Multi Time Scale World Models\\\"\\n  authors: [Shaj V., Gholam Zadeh S., Demir O., Luettjohann L., Neumann G., Toussaint M.]\\n  year: 2023\\n  venue: \\\"NeurIPS 2023 (arXiv:2310.18534)\\\"\\n  category: method-component\\n  role: \\\"MTS3 — probabilistic multi-time-scale state space model with fast and slow latent dynamics for variable-rate prediction. Provides efficient inference across temporal scales. Foundational multi-rate dynamics architecture; our work shows that even with proper multi-rate modeling, the downstream actor-critic training in imagination can exploit temporal conditioning for value overestimation — a failure mode MTS3 does not address (it focuses on prediction quality, not policy training).\\\"\\n  relevance_score: 4\\n\\n- paper_id: splates2025\\n  title: \\\"Stable Planning with Temporally Extended Skills\\\"\\n  authors: [SPlaTES authors]\\n  year: 2025\\n  venue: \\\"Reinforcement Learning Journal (RLC 2025)\\\"\\n  category: method-component\\n  role: \\\"SPlaTES — hierarchical MPC with temporally extended skills + abstract skill world model. Skill learning via mutual-information objective yields diverse, predictable, task-related behavior. Demonstrates that stable long-horizon planning requires modeling skill outcomes (temporal abstraction via hierarchy), not primitive-action outcomes at variable time steps — consistent with our finding that flat dt-embedding fails.\\\"\\n  relevance_score: 3\\n\\n- paper_id: beckerehmck2023multitimestep\\n  title: \\\"Multi-timestep models for Model-based Reinforcement Learning\\\"\\n  authors: [Becker-Ehmck P., Peters J., van der Smagt P.]\\n  year: 2023\\n  venue: \\\"arXiv:2310.05672\\\"\\n  category: background\\n  role: \\\"Proposes multi-timestep training objective (weighted sum of losses at various future horizons) for one-step dynamics models to improve long-horizon R² score. Addresses compounding error at the model training level; our work shows that even with perfect multi-step prediction, the imagination-based actor-critic can still fail due to value overestimation from dt-conditioning — a downstream failure mode distinct from prediction accuracy.\\\"\\n  relevance_score: 3\\n\\n- paper_id: liu2022dmve\\n  title: \\\"Dynamic-Horizon Model-Based Value Estimation With Latent Imagination\\\"\\n  authors: [Liu Y., et al.]\\n  year: 2022\\n  venue: \\\"IEEE TNNLS (arXiv:2009.09593)\\\"\\n  category: background\\n  role: \\\"DMVE — adaptive rollout horizon selection via horizon reliability detection (comparing value expansion errors between raw and reconstructed observations). Addresses the horizon selection problem in imagination-based value estimation. Complementary to our work: DMVE selects among fixed-dt horizons; we show that even optimal horizon selection cannot fix the delusional critic when dt-embedding is trained (the overestimation is in the value function, not the horizon length).\\\"\\n  relevance_score: 3\\n\\n# --- Incremental scan synthesis (2026-05-14) ---\\n#\\n# NOVELTY ASSESSMENT:\\n# No paper found that diagnoses dt_embedding → delusional critic\\n# (value overestimation) → stochastic collapse in imagination-based\\n# MBRL. Our core contribution remains novel.\\n#\\n# TAWM (ICML 2025) is the closest methodological overlap but\\n# operates in MPC paradigm and reaches opposite conclusion\\n# (Δt conditioning is beneficial). This actually STRENGTHENS\\n# our novelty: \\\"Δt conditioning helps in MPC but hurts in\\n# imagination-based training\\\" is a more nuanced and surprising finding.\\n#\\n# LANDSCAPE TREND:\\n# The field is converging on HIERARCHY (THICK, Hieros, Director,\\n# HWM, SPlaTES, MetaController) as the solution to temporal\\n# abstraction in world models, avoiding flat variable-dt approaches.\\n# Our diagnostic paper explains WHY flat dt approaches fail,\\n# providing theoretical grounding for this empirical trend.\\n#\\n# ACTION ITEMS FOR PAPER:\\n# 1. MUST CITE: nhu2025tawm — differentiate MPC vs imagination paradigm\\n# 2. SHOULD CITE: li2025lsimagine — concurrent Dreamer horizon extension\\n# 3. SHOULD CITE: shaj2023mts3 — multi-rate dynamics foundation\\n# 4. CONSIDER: zhang2026hwm — latest hierarchical WM planning\\n\", \"total_chars\": 50497, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "18a159d1-c033-4b79-9fcd-537282581067",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/e9efbf3e-355b-4b54-9c61-7a3e79247d76/tool-results/toolu_015NvA3eHHb1XM56CSMj8Vmq.txt",
      "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml\\\", \\\"content\\\": \\\"# Literature Map — event-gated-adaptive-horizon\\\\n# Last updated: 2026-05-14\\\\n# Total: 72 papers (64 existing + 8 incremental scan 2026-05-14)\\\\n\\\\n# ============================================================\\\\n# EXISTING CITATIONS (already in paper.tex)\\\\n# ============================================================\\\\n\\\\n- paper_id: sutton1999options\\\\n  title: \\\\\\\"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\\\\\\\"\\\\n  authors: [Sutton R.S., Precup D., Singh S.]\\\\n  year: 1999\\\\n  venue: \\\\\\\"Artificial Intelligence 112(1-2):181-211\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: hafner2020dreamerv1\\\\n  title: \\\\\\\"Dream to Control: Learning Behaviors by Latent Imagination\\\\\\\"\\\\n  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]\\\\n  year: 2020\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: hafner2023dreamerv3\\\\n  title: \\\\\\\"Mastering Diverse Domains through World Models\\\\\\\"\\\\n  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]\\\\n  year: 2023\\\\n  venue: \\\\\\\"arXiv:2301.04104 (Nature 2025)\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: sharma2017figar\\\\n  title: \\\\\\\"Fine Grained Action Repetition for Deep Reinforcement Learning\\\\\\\"\\\\n  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]\\\\n  year: 2017\\\\n  venue: \\\\\\\"ICLR Workshop\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"FiGAR — learns action-repeat durations in model-free RL; we extend the idea to imagination step size in world-model RL\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: janner2019mbpo\\\\n  title: \\\\\\\"When to Trust Your Model: Model-Based Policy Optimization\\\\\\\"\\\\n  authors: [Janner M., Fu J., Zhang M., Levine S.]\\\\n  year: 2019\\\\n  venue: NeurIPS\\\\n  category: background\\\\n  role: \\\\\\\"MBPO — formalizes model exploitation in MBRL; our delusional critic is a specific instance of model exploitation tied to temporal embedding\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n# ============================================================\\\\n# NEW: Multi-step prediction error compounding\\\\n# ============================================================\\\\n\\\\n- paper_id: ke2019learning\\\\n  title: \\\\\\\"Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future\\\\\\\"\\\\n  authors: [Ke N.R., Singh A., Touati A., Goyal A., Bengio Y., Parikh D., Batra D.]\\\\n  year: 2019\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"Addresses long-term dynamics prediction via latent-variable autoregressive model; directly relevant to our finding that multi-step RSSM predictions degrade with dt>1\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: asadi2019combating\\\\n  title: \\\\\\\"Combating the Compounding-Error Problem with a Multi-step Model\\\\\\\"\\\\n  authors: [Asadi K., Misra D., Kim S., Littman M.L.]\\\\n  year: 2019\\\\n  venue: \\\\\\\"arXiv:1905.13320\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Proposes multi-step models to bypass compounding error; our work shows that even with multi-step imagination, the dt-embedding creates a different failure mode (value overestimation) distinct from compounding error\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: venkatraman2015improving\\\\n  title: \\\\\\\"Improving Multi-Step Prediction of Learned Time Series Models\\\\\\\"\\\\n  authors: [Venkatraman A., Hebert M., Bagnell J.A.]\\\\n  year: 2015\\\\n  venue: AAAI\\\\n  category: background\\\\n  role: \\\\\\\"Data-as-Demonstrator (DaD) for robust multi-step prediction; establishes theoretical guarantee relating training error to multi-step prediction error\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: lambert2022investigating\\\\n  title: \\\\\\\"Investigating Compounding Prediction Errors in Learned Dynamics Models\\\\\\\"\\\\n  authors: [Lambert N., Pister K.S.J., Calandra R.]\\\\n  year: 2022\\\\n  venue: \\\\\\\"arXiv:2203.09637\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Empirical study of compounding error properties; we rule out compounding error as the primary failure mechanism (008c vs 008a comparison) and identify value overestimation instead\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: Model-predictive control with learned dynamics\\\\n# ============================================================\\\\n\\\\n- paper_id: chua2018pets\\\\n  title: \\\\\\\"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models\\\\\\\"\\\\n  authors: [Chua K., Calandra R., McAllister R., Levine S.]\\\\n  year: 2018\\\\n  venue: NeurIPS\\\\n  category: background\\\\n  role: \\\\\\\"PETS — ensemble-based uncertainty-aware MPC; uses explicit uncertainty quantification to avoid model exploitation, contrasting with DreamerV3's implicit approach\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: nagabandi2018neural\\\\n  title: \\\\\\\"Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning\\\\\\\"\\\\n  authors: [Nagabandi A., Kahn G., Fearing R.S., Levine S.]\\\\n  year: 2018\\\\n  venue: ICRA\\\\n  category: background\\\\n  role: \\\\\\\"Demonstrates NN dynamics + MPC for locomotion; model errors accumulate over prediction horizon, motivating our investigation of horizon-dependent failures\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: hansen2024tdmpc2\\\\n  title: \\\\\\\"TD-MPC2: Scalable, Robust World Models for Continuous Control\\\\\\\"\\\\n  authors: [Hansen N., Su H., Wang X.]\\\\n  year: 2024\\\\n  venue: \\\\\\\"ICLR (arXiv:2310.16828)\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"TD-MPC2 — SOTA MPC planning route (online planning + learned dynamics); DMC benchmark leader but orthogonal to imagination-based training — reviewer defense: TD-MPC2 does online MPC rollouts at test time, we study actor-critic training via imagined rollouts (DreamerV3 paradigm), not a same-level comparison\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n# ============================================================\\\\n# NEW: Pessimistic MBRL / model exploitation mitigation\\\\n# ============================================================\\\\n\\\\n- paper_id: yu2020mopo\\\\n  title: \\\\\\\"MOPO: Model-based Offline Policy Optimization\\\\\\\"\\\\n  authors: [Yu T., Thomas G., Yu L., Ermon S., Zou J., Levine S., Finn C., Ma T.]\\\\n  year: 2020\\\\n  venue: \\\\\\\"NeurIPS (arXiv:2005.13239)\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"MOPO — pessimistic MBRL via uncertainty-penalized reward (reward -= λ * model_uncertainty); generic model exploitation mitigation — reviewer defense: MOPO addresses distribution shift in offline MBRL, our dt=1 imagination restriction targets dt_embedding-induced delusional critic (temporal conditioning corruption), two complementary mechanisms\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n# ============================================================\\\\n# NEW: Value overestimation mitigation\\\\n# ============================================================\\\\n\\\\n- paper_id: thrun1993issues\\\\n  title: \\\\\\\"Issues in Using Function Approximation for Reinforcement Learning\\\\\\\"\\\\n  authors: [Thrun S., Schwartz A.]\\\\n  year: 1993\\\\n  venue: \\\\\\\"Connectionist Models Summer School\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"First identification of systematic value overestimation from function approximation; our delusional critic extends this to model-based imagination with temporal conditioning\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: vanhasselt2016double\\\\n  title: \\\\\\\"Deep Reinforcement Learning with Double Q-Learning\\\\\\\"\\\\n  authors: [van Hasselt H., Guez A., Silver D.]\\\\n  year: 2016\\\\n  venue: AAAI\\\\n  category: background\\\\n  role: \\\\\\\"Double DQN — mitigates overestimation via double estimator; our finding that trained dt-embedding enables value exploitation is a complementary overestimation mechanism in MBRL\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: fujimoto2018td3\\\\n  title: \\\\\\\"Addressing Function Approximation Error in Actor-Critic Methods\\\\\\\"\\\\n  authors: [Fujimoto S., van Hoof H., Meger D.]\\\\n  year: 2018\\\\n  venue: ICML\\\\n  category: method-component\\\\n  role: \\\\\\\"TD3 — clipped double-Q to limit overestimation in actor-critic; DreamerV3 uses a single critic, making it more vulnerable to the overestimation we identify\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: haarnoja2018sac\\\\n  title: \\\\\\\"Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor\\\\\\\"\\\\n  authors: [Haarnoja T., Zhou A., Abbeel P., Levine S.]\\\\n  year: 2018\\\\n  venue: ICML\\\\n  category: method-component\\\\n  role: \\\\\\\"SAC — entropy regularization implicitly mitigates overestimation; relevant contrast to DreamerV3's actor which can greedily exploit overestimated values\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: lee2021sunrise\\\\n  title: \\\\\\\"SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning\\\\\\\"\\\\n  authors: [Lee K., Laskin M., Srinivas A., Abbeel P.]\\\\n  year: 2021\\\\n  venue: ICML\\\\n  category: method-component\\\\n  role: \\\\\\\"Ensemble-based uncertainty weighting for value estimation; potential mitigation for our identified delusional critic mechanism\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: Delusional bias\\\\n# ============================================================\\\\n\\\\n- paper_id: lu2018nondelusional\\\\n  title: \\\\\\\"Non-delusional Q-learning and Value-Iteration\\\\\\\"\\\\n  authors: [Lu T., Schuurmans D., Boutilier C.]\\\\n  year: 2018\\\\n  venue: NeurIPS\\\\n  category: background\\\\n  role: \\\\\\\"Formalizes delusional bias from policy-class constraints in Q-learning; we identify an analogous phenomenon where temporal conditioning enables the critic to exploit model imprecision\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n# ============================================================\\\\n# NEW: Hierarchical RL with learned models\\\\n# ============================================================\\\\n\\\\n- paper_id: hafner2022director\\\\n  title: \\\\\\\"Deep Hierarchical Planning from Pixels\\\\\\\"\\\\n  authors: [Hafner D., Lee K.-H., Fischer I., Abbeel P.]\\\\n  year: 2022\\\\n  venue: NeurIPS\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"Director — hierarchical planning in Dreamer latent space via subgoals; addresses temporal abstraction through goal hierarchy rather than variable dt\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: nachum2018hiro\\\\n  title: \\\\\\\"Data-Efficient Hierarchical Reinforcement Learning\\\\\\\"\\\\n  authors: [Nachum O., Gu S., Lee H., Levine S.]\\\\n  year: 2018\\\\n  venue: NeurIPS\\\\n  category: background\\\\n  role: \\\\\\\"HIRO — off-policy HRL with learned subgoals; demonstrates that hierarchical temporal abstraction can improve sample efficiency when properly designed\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: Action repeat / frame skip\\\\n# ============================================================\\\\n\\\\n- paper_id: braylan2015frame\\\\n  title: \\\\\\\"Frame Skip Is a Powerful Parameter for Learning to Play Atari\\\\\\\"\\\\n  authors: [Braylan A., Hollenbeck M., Meyerson E., Miikkulainen R.]\\\\n  year: 2015\\\\n  venue: \\\\\\\"AAAI Workshop on Learning for General Competency in Video Games\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Empirical study showing frame skip strongly affects Atari performance; motivates investigation of temporal granularity as a critical design choice\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: lakshminarayanan2017dynamic\\\\n  title: \\\\\\\"Dynamic Action Repetition for Deep Reinforcement Learning\\\\\\\"\\\\n  authors: [Lakshminarayanan A.S., Sharma S., Ravindran B.]\\\\n  year: 2017\\\\n  venue: AAAI\\\\n  category: method-component\\\\n  role: \\\\\\\"Learns per-step action repetition duration; model-free analog of our variable-dt imagination approach\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: biedenkapp2021temporl\\\\n  title: \\\\\\\"TempoRL: Learning When to Act\\\\\\\"\\\\n  authors: [Biedenkapp A., Rajan R., Hutter F., Lindauer M.]\\\\n  year: 2021\\\\n  venue: ICML\\\\n  category: method-component\\\\n  role: \\\\\\\"Learns action persistence via skip-policy; demonstrates up to 10x speedup — but in model-free setting without the model exploitation risk we identify\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n# ============================================================\\\\n# NEW: DreamerV2\\\\n# ============================================================\\\\n\\\\n- paper_id: hafner2021dreamerv2\\\\n  title: \\\\\\\"Mastering Atari with Discrete World Models\\\\\\\"\\\\n  authors: [Hafner D., Lillicrap T., Norouzi M., Ba J.]\\\\n  year: 2021\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"DreamerV2 — introduces discrete latent representations used in DreamerV3; key architectural predecessor to our base system\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n# ============================================================\\\\n# NEW: Alternative world model architectures\\\\n# ============================================================\\\\n\\\\n- paper_id: micheli2023iris\\\\n  title: \\\\\\\"Transformers are Sample-Efficient World Models\\\\\\\"\\\\n  authors: [Micheli V., Alonso E., Fleuret F.]\\\\n  year: 2023\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"IRIS — autoregressive transformer world model; alternative to RSSM that may exhibit different compounding error characteristics under temporal abstraction\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: robine2023twm\\\\n  title: \\\\\\\"Transformer-based World Models Are Happy With 100k Interactions\\\\\\\"\\\\n  authors: [Robine J., Hoeftmann M., Uelwer T., Harmeling S.]\\\\n  year: 2023\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"TWM — Transformer-XL world model with direct state access; circumvents RSSM's recurrent compression that exacerbates our identified prediction gap\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: chen2022transdreamer\\\\n  title: \\\\\\\"TransDreamer: Reinforcement Learning with Transformer World Models\\\\\\\"\\\\n  authors: [Chen C., Wu Y.-F., Yoon J., Ahn S.]\\\\n  year: 2022\\\\n  venue: \\\\\\\"arXiv:2202.09481\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Replaces RSSM with Transformer State-Space Model; directly tests whether RSSM-specific architecture contributes to temporal abstraction failures\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: 2024-2026 concurrent work on temporal abstraction in world models\\\\n# ============================================================\\\\n\\\\n- paper_id: gumbsch2024thick\\\\n  title: \\\\\\\"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics\\\\\\\"\\\\n  authors: [Gumbsch C., Sajid N., Martius G., Butz M.V.]\\\\n  year: 2024\\\\n  venue: ICLR\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"THICK — learns adaptive temporal abstractions via context-change detection; closest concurrent work — addresses temporal abstraction in Dreamer but via hierarchy rather than variable-dt imagination\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: mattes2024hieros\\\\n  title: \\\\\\\"Hieros: Hierarchical Imagination on Structured State Space Sequence World Models\\\\\\\"\\\\n  authors: [Mattes P., Schlosser R., Herbrich R.]\\\\n  year: 2024\\\\n  venue: ICML\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n# ============================================================\\\\n# NEW: Seed-dependent instability & value overestimation in MBRL\\\\n# ============================================================\\\\n\\\\n- paper_id: henderson2018deep\\\\n  title: \\\\\\\"Deep Reinforcement Learning that Matters\\\\\\\"\\\\n  authors: [Henderson P., Islam R., Bachman P., Pineau J., Precup D., Meger D.]\\\\n  year: 2018\\\\n  venue: AAAI\\\\n  category: background\\\\n  role: \\\\\\\"Foundational study on seed variance in deep RL — shows statistically different performance distributions arise from random seeds alone with identical hyperparameters; directly supports our observation that seed 0 vs seed 2 produce qualitatively different value dynamics under the same dt_embed_dim=0 config\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: nikishin2022primacy\\\\n  title: \\\\\\\"The Primacy Bias in Deep Reinforcement Learning\\\\\\\"\\\\n  authors: [Nikishin E., Schwarzer M., D'Oro P., Bacon P.-L., Courville A.]\\\\n  year: 2022\\\\n  venue: ICML\\\\n  category: background\\\\n  role: \\\\\\\"Identifies primacy bias — agents overfit early data and lose ability to learn from new transitions, leading to delayed performance collapse; parallels our finding where value overestimation initially appears benign but becomes pathological later, and the collapse timing is seed-dependent\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: qiao2023mind\\\\n  title: \\\\\\\"Mind the Model, Not the Agent: The Primacy Bias in Model-based RL\\\\\\\"\\\\n  authors: [Qiao Z., Lyu J., Li X.]\\\\n  year: 2023\\\\n  venue: \\\\\\\"arXiv:2310.15017 (ECAI 2024)\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"Extends primacy bias to MBRL, testing on DreamerV2 — shows world model primacy bias dominates over agent primacy bias; directly relevant to Dreamer-family training instability and explains why some seeds recover (model escapes early overfitting) while others don't\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: hussing2024dissecting\\\\n  title: \\\\\\\"Dissecting Deep RL with High Update Ratios: Combatting Value Divergence\\\\\\\"\\\\n  authors: [Hussing M., Voelcker C.A., Gilitschenski I., Farahmand A.-M., Eaton E.]\\\\n  year: 2024\\\\n  venue: \\\\\\\"Reinforcement Learning Journal (RLC 2024)\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"Shows value overestimation and Q-divergence under high update-to-data ratios, driven by optimizer momentum — overestimation occurs on both in-distribution and OOD data; mechanism maps to our delusional critic where imagination-trained critic inflates values progressively, with divergence onset sensitive to initialization\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: barkley2024stealing\\\\n  title: \\\\\\\"Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning\\\\\\\"\\\\n  authors: [Barkley B., Fridovich-Keil D.]\\\\n  year: 2024\\\\n  venue: \\\\\\\"arXiv:2412.14312 (ICML 2025)\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"Demonstrates that synthetic rollouts (imagination) can degrade performance inconsistently across environments, with overestimation bias as a contributing factor; supports our finding that imagination-based training creates environment- and seed-dependent failure modes that existing mitigation techniques do not reliably fix\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: bjorck2022variance\\\\n  title: \\\\\\\"Is High Variance Unavoidable in RL? A Case Study in Continuous Control\\\\\\\"\\\\n  authors: [Bjorck J., Gomes C.P., Weinberger K.Q.]\\\\n  year: 2022\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"Shows RL variance mostly arises early in training from poor 'outlier' runs caused by numerical instability; parallels our observation that seed 2 diverges early while seed 0 recovers — the reward prediction degradation from removing dt_embedding may create exactly this early-training instability\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: Reward prediction quality → MBRL performance\\\\n# ============================================================\\\\n# Our key finding: removing dt_embedding causes reward_MAE to spike 75x\\\\n# (0.01 → 0.747), making performance seed-dependent. These papers\\\\n# establish that reward prediction quality is a known MBRL bottleneck.\\\\n\\\\n- paper_id: lee2024dreamsmooth\\\\n  title: \\\\\\\"DreamSmooth: Improving Model-based Reinforcement Learning via Reward Smoothing\\\\\\\"\\\\n  authors: [Lee V., Abbeel P., Lee Y.]\\\\n  year: 2024\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"Directly demonstrates reward prediction is a bottleneck in MBRL — sparse/ambiguous rewards cause the reward model to predict zeros, creating gradient-free landscapes during imagination; our dt_embed_dim=0 ablation creates an analogous bottleneck where the reward head loses temporal conditioning and MAE spikes 75x\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: ma2024harmonydream\\\\n  title: \\\\\\\"HarmonyDream: Task Harmonization Inside World Models\\\\\\\"\\\\n  authors: [Ma H., Wu J., Feng N., Xiao C., Li D., Hao J., Wang J., Long M.]\\\\n  year: 2024\\\\n  venue: ICML\\\\n  category: background\\\\n  role: \\\\\\\"Shows observation prediction dominates reward prediction in world model training, degrading reward model quality; proposes dynamic loss balancing for 10-69% gains — directly relevant to our finding that dt_embedding removal disrupts the observation-reward prediction balance and causes reward MAE explosion\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: lambert2020objective\\\\n  title: \\\\\\\"Objective Mismatch in Model-based Reinforcement Learning\\\\\\\"\\\\n  authors: [Lambert N., Amos B., Yadan O., Calandra R.]\\\\n  year: 2020\\\\n  venue: \\\\\\\"L4DC (Proceedings of Machine Learning Research, vol. 120)\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Formalizes that one-step prediction likelihood does not correlate with control performance — the 'objective mismatch' problem; our work reveals a specific instance: the reward head's prediction accuracy (measured by MAE) directly gates whether the critic can learn stable value estimates, creating a reward-specific objective mismatch\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n# ============================================================\\\\n# NEW: Auxiliary tasks & representation coupling in world models\\\\n# ============================================================\\\\n# Our finding: reward prediction quality is tightly coupled to temporal\\\\n# conditioning (dt_embedding). Removing the embedding degrades the\\\\n# reward head while dynamics remain intact — suggesting the reward head\\\\n# acts as more than a passive predictor; it conditions the shared\\\\n# representation. Literature gap: no prior work studies this coupling\\\\n# specifically in Dreamer-family world models.\\\\n\\\\n- paper_id: jaderberg2017unreal\\\\n  title: \\\\\\\"Reinforcement Learning with Unsupervised Auxiliary Tasks\\\\\\\"\\\\n  authors: [Jaderberg M., Mnih V., Czarnecki W.M., Schaul T., Leibo J.Z., Silver D., Kavukcuoglu K.]\\\\n  year: 2017\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"UNREAL — introduces reward prediction as an auxiliary task that shapes shared representations; foundational evidence that reward prediction is not just a passive output but actively conditions what features the network learns — our finding that removing dt_embedding selectively degrades reward prediction (but not dynamics) suggests the temporal conditioning specifically enables reward-relevant feature extraction\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: lyle2021auxiliary\\\\n  title: \\\\\\\"On The Effect of Auxiliary Tasks on Representation Dynamics\\\\\\\"\\\\n  authors: [Lyle C., Rowland M., Ostrovski G., Dabney W.]\\\\n  year: 2021\\\\n  venue: AISTATS\\\\n  category: background\\\\n  role: \\\\\\\"Theoretical analysis showing auxiliary tasks shape representations toward top eigenvectors of the transition operator; provides formal grounding for why removing temporal conditioning from the reward head could alter the entire representation — the reward head's gradients contribute to spectral structure of the shared latent space\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n# ============================================================\\\\n# NEW: DreamerV3 architecture improvements (2025-2026)\\\\n# ============================================================\\\\n\\\\n- paper_id: bredis2026nedreamer\\\\n  title: \\\\\\\"Next Embedding Prediction Makes World Models Stronger\\\\\\\"\\\\n  authors: [Bredis G., Balagansky N., Gavrilov D., Rakhimov R.]\\\\n  year: 2026\\\\n  venue: \\\\\\\"arXiv:2603.02765\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"NE-Dreamer — decoder-free MBRL replacing pixel reconstruction with next-embedding prediction via temporal transformer + Barlow Twins; improves RSSM prediction quality on DMC and DMLab but does not address temporal abstraction or delusional critic — orthogonal to our dt-embedding diagnosis\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: zhang2025dymodreamer\\\\n  title: \\\\\\\"DyMoDreamer: World Modeling with Dynamic Modulation\\\\\\\"\\\\n  authors: [Zhang B., Wang R., Xiao W., Zhang W., Sun J., Huang G., Chen J., Wang G.]\\\\n  year: 2025\\\\n  venue: NeurIPS\\\\n  category: background\\\\n  role: \\\\\\\"Modulates RSSM via inter-frame differencing mask and stochastic categorical dynamic modulation; SOTA on Atari 100k (156.6% HNS) and DMC (832) — improves dynamics extraction but does not address variable-rate imagination or dt_embedding-induced value overestimation\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: Temporal abstraction methods\\\\n# ============================================================\\\\n\\\\n- paper_id: liu2025vanta\\\\n  title: \\\\\\\"Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning\\\\\\\"\\\\n  authors: [Liu T.-S., Liu X.-H., Chen R., Jin L., Wang P., Zhang Z., Yu Y.]\\\\n  year: 2025\\\\n  venue: ICLR\\\\n  category: method-component\\\\n  role: \\\\\\\"VanTA — VLM-guided trajectory decomposition into semantically meaningful skills via vector quantization + relabeling; operates at high-level skill abstraction (Franka Kitchen, Crafter) — contrasts with our low-level dt-based temporal abstraction within world-model imagination steps\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: Evaluation methodology\\\\n# ============================================================\\\\n\\\\n- paper_id: agarwal2021precipice\\\\n  title: \\\\\\\"Deep Reinforcement Learning at the Edge of the Statistical Precipice\\\\\\\"\\\\n  authors: [Agarwal R., Schwarzer M., Castro P.S., Courville A.C., Bellemare M.]\\\\n  year: 2021\\\\n  venue: NeurIPS\\\\n  category: evaluation\\\\n  role: \\\\\\\"Proposes rliable — interval estimates, performance profiles, IQM for robust multi-seed RL evaluation (NeurIPS Outstanding Paper); our multi-seed experiment design follows this methodology to ensure statistical validity of collapse detection across seeds\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n# ============================================================\\\\n# NEW (2026-05-14 gap analysis): Time discretization theory\\\\n# ============================================================\\\\n# Gap: variable timestep / time discretization invariance — foundational\\\\n# theory for why dt matters and how to handle it.\\\\n\\\\n- paper_id: tallec2019making\\\\n  title: \\\\\\\"Making Deep Q-learning methods Robust to Time Discretization\\\\\\\"\\\\n  authors: [Tallec C., Blier L., Ollivier Y.]\\\\n  year: 2019\\\\n  venue: \\\\\\\"ICML (arXiv:1901.09732)\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Shows Q-learning performance is highly sensitive to time discretization δ; proposes architectural + exploration modifications for δ-invariance. Theoretical foundation for why our variable-dt imagination introduces a fundamental difficulty: RSSM trained at δ=1 cannot produce δ-invariant predictions at dt>1\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: park2021sar\\\\n  title: \\\\\\\"Time Discretization-Invariant Safe Action Repetition for Policy Gradient Methods\\\\\\\"\\\\n  authors: [Park S., Kim J., Kim G.]\\\\n  year: 2021\\\\n  venue: \\\\\\\"NeurIPS (arXiv:2111.03941)\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"SAR — δ-invariant action repetition for policy gradients; achieves time-discretization robustness in model-free RL via adaptive reaction to state changes during repetition. Contrasts with our finding that world-model RL lacks this robustness when imagination uses dt>1\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: wang2024seac\\\\n  title: \\\\\\\"Reinforcement Learning with Elastic Time Steps\\\\\\\"\\\\n  authors: [Wang D., Beltrame G.]\\\\n  year: 2024\\\\n  venue: \\\\\\\"arXiv:2402.14961\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"SEAC/MOSEAC — variable-duration time steps where agent selects both action and duration; model-free approach that explicitly treats action duration as part of the action space. Our work reveals why this strategy is problematic in world-model RL: the critic cannot reliably evaluate variable-duration imagined trajectories\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW (2026-05-14 gap analysis): Delusional bias mitigation\\\\n# ============================================================\\\\n\\\\n- paper_id: su2020conqur\\\\n  title: \\\\\\\"ConQUR: Mitigating Delusional Bias in Deep Q-learning\\\\\\\"\\\\n  authors: [Su D., Ooi J., Lu T., Schuurmans D., Boutilier C.]\\\\n  year: 2020\\\\n  venue: \\\\\\\"ICML (arXiv:2002.12399)\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Follow-up to Lu et al. 2018; mitigates delusional bias via consistency-penalized Q-labels. Addresses delusional bias from policy-class constraints in Q-learning; our delusional critic is an analogous phenomenon in MBRL where temporal conditioning (dt_embedding) creates inconsistent value targets across imagination steps\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n# ============================================================\\\\n# NEW (2026-05-14 gap analysis): Diagnostic methodology in RL\\\\n# ============================================================\\\\n# Gap: our paper is a diagnostic analysis — need methodological\\\\n# precedents for \\\\\\\"what matters\\\\\\\" / \\\\\\\"implementation matters\\\\\\\" style papers.\\\\n\\\\n- paper_id: engstrom2020implementation\\\\n  title: \\\\\\\"Implementation Matters in Deep Policy Gradients: A Case Study on PPO and TRPO\\\\\\\"\\\\n  authors: [Engstrom L., Ilyas A., Santurkar S., Tsipras D., Janoos F., Rudolph L., Madry A.]\\\\n  year: 2020\\\\n  venue: \\\\\\\"ICLR (arXiv:2005.12729)\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"Demonstrates that code-level implementation details (not algorithmic innovations) drive most of PPO's gains over TRPO; methodological precedent for our diagnostic approach — we similarly show that a specific implementation choice (trained vs. untrained dt_embedding) is the primary factor determining collapse vs. stability\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: andrychowicz2021whatmatters\\\\n  title: \\\\\\\"What Matters for On-Policy Deep Actor-Critic Methods? A Large-Scale Study\\\\\\\"\\\\n  authors: [Andrychowicz M., Raichuk A., Stańczyk P., Orsini M., Girgin S., Marinier R., Hussenot L., Geist M., Pietquin O., Michalski M., Gelly S., Bachem O.]\\\\n  year: 2021\\\\n  venue: \\\\\\\"ICLR (arXiv:2006.05990)\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"Large-scale factorial study of 50+ design choices in on-policy RL (250K+ agents); methodological template for our factorial experiment design isolating dt_embedding × subsample × horizon effects. Demonstrates that systematic ablation reveals non-obvious interactions — parallel to our finding that dt_embedding training status interacts with subsample and horizon\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n# ============================================================\\\\n# NEW (2026-05-14 gap analysis): MBRL rollout quality & value overestimation\\\\n# ============================================================\\\\n# Gap: recent ICLR 2025 papers directly studying imagination rollout\\\\n# quality and value overestimation in model-based settings.\\\\n\\\\n- paper_id: frauenknecht2025rollouts\\\\n  title: \\\\\\\"On Rollouts in Model-Based Reinforcement Learning\\\\\\\"\\\\n  authors: [Frauenknecht B., Subhasish D., Solowjow F., Trimpe S.]\\\\n  year: 2025\\\\n  venue: \\\\\\\"ICLR (arXiv:2501.16918)\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"Shows trajectory-sampling rollouts diverge from ground truth after few steps and can harm policy learning; proposes Infoprop separating aleatoric/epistemic uncertainty with rollout termination criteria. Directly supports our finding that dt>1 imagination produces corrupted data — our work identifies a specific mechanism (dt_embedding-induced value exploitation) beyond general compounding error\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: voelcker2025madtd\\\\n  title: \\\\\\\"MAD-TD: Model-Augmented Data stabilizes High Update Ratio RL\\\\\\\"\\\\n  authors: [Voelcker C., Hussing M., Eaton E., Farahmand A.-M., Gilitschenski I.]\\\\n  year: 2025\\\\n  venue: \\\\\\\"ICLR (arXiv:2410.08896)\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"Shows value function misgeneralization to on-policy actions causes instability at high UTD ratios; uses model-generated data to improve value accuracy. Complementary to our finding: MAD-TD addresses value misgeneralization from replay distribution mismatch, we address value overestimation from temporal conditioning corruption in imagination\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n# ============================================================\\\\n# NEW (2026-05-14 gap analysis): Latest action repeat methods\\\\n# ============================================================\\\\n\\\\n- paper_id: nie2025sdar\\\\n  title: \\\\\\\"Select before Act: Spatially Decoupled Action Repetition for Continuous Control\\\\\\\"\\\\n  authors: [Nie B., et al.]\\\\n  year: 2025\\\\n  venue: \\\\\\\"ICLR (arXiv:2502.06919)\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"SDAR — per-dimension action repetition decisions for flexible temporal persistence in model-free RL; SOTA on DMC continuous control. Advances action repeat in model-free setting; our work shows the fundamental obstacle to analogous variable-rate approaches in model-based RL (delusional critic from dt_embedding)\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW (2026-05-14 gap analysis): DreamerV4 / latest Dreamer evolution\\\\n# ============================================================\\\\n\\\\n- paper_id: hafner2025dreamerv4\\\\n  title: \\\\\\\"Training Agents Inside of Scalable World Models\\\\\\\"\\\\n  authors: [Hafner D., Yan W.]\\\\n  year: 2025\\\\n  venue: \\\\\\\"arXiv:2509.24527\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"DreamerV4 — replaces RSSM with efficient transformer world model + shortcut forcing; scales to video pretraining (Minecraft diamonds from video). Architectural successor to DreamerV3; our dt_embedding diagnosis is specific to RSSM but the broader lesson (temporal conditioning must match model fidelity) applies to transformer world models\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n# ============================================================\\\\n# NEW (2026-05-14): Training instability dynamics\\\\n# ============================================================\\\\n\\\\n- paper_id: zhang2026instability\\\\n  title: \\\\\\\"Training instability in deep learning follows low-dimensional dynamical principles\\\\\\\"\\\\n  authors: [Zhang L., et al.]\\\\n  year: 2026\\\\n  venue: \\\\\\\"ICLR 2026 (arXiv:2601.13160)\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Training instability follows low-dimensional dynamical principles; provides theoretical framework for why seed-dependent collapse vs self-correction occurs in our experiments (008d seed 1 collapses, 009b seed 2 self-corrects under identical config)\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n# ============================================================\\\\n# NEW (2026-05-14): Seed-Dependent Stochastic Outcomes in MBRL\\\\n# ============================================================\\\\n# Dedicated literature survey for the stochastic collapse phenomenon:\\\\n# same config (trained dt_embedding + subsample + H=8) produces\\\\n# collapse in seed 0 (008d) but self-correction in seed 2 (009b).\\\\n# nve>1.5x is a 100% reliable marker of trained dt_embedding,\\\\n# but collapse itself is stochastic (1/2 seeds).\\\\n\\\\n- paper_id: sokar2023dormant\\\\n  title: \\\\\\\"The Dormant Neuron Phenomenon in Deep Reinforcement Learning\\\\\\\"\\\\n  authors: [Sokar G., Agarwal R., Castro P.S., Evci U.]\\\\n  year: 2023\\\\n  venue: \\\\\\\"ICML 2023\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Identifies dormant neurons — inactive units accumulating during RL training that reduce network expressivity. Seed-dependent because different random initializations produce different early dormancy patterns; directly explains why some seeds lose the representational capacity needed to self-correct value overestimation (our seed 0 collapses) while others retain enough active neurons to recover (our seed 2 self-corrects)\\\\\\\"\\\\n  relevance_score: 4\\\\n  survey_tag: seed-dependent-stochastic-outcomes\\\\n\\\\n- paper_id: lyle2022capacity\\\\n  title: \\\\\\\"Understanding and Preventing Capacity Loss in Reinforcement Learning\\\\\\\"\\\\n  authors: [Lyle C., Rowland M., Dabney W.]\\\\n  year: 2022\\\\n  venue: \\\\\\\"ICLR 2023 (arXiv:2204.09560)\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Shows feature rank collapse from non-stationary TD targets is a necessary condition for learning failure but not sufficient — sparse rewards and other factors must co-occur. Directly parallels our finding: nve>1.5x (value overestimation from trained dt_embedding) is a necessary precondition for collapse but not a sufficient one; additional stochastic factors (initialization, early replay composition) determine whether collapse actually occurs\\\\\\\"\\\\n  relevance_score: 5\\\\n  survey_tag: seed-dependent-stochastic-outcomes\\\\n\\\\n- paper_id: kumar2022dr3\\\\n  title: \\\\\\\"DR3: Value-Based Deep Reinforcement Learning Requires Explicit Regularization\\\\\\\"\\\\n  authors: [Kumar A., Agarwal R., Ma T., Courville A., Tucker G., Levine S.]\\\\n  year: 2022\\\\n  venue: \\\\\\\"ICLR 2022\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Shows implicit regularization from TD learning favors degenerate feature aliasing (states on both sides of Bellman backup become indistinguishable), creating the substrate for value overestimation. In our setting, trained dt_embedding amplifies this aliasing across different temporal horizons — the critic cannot distinguish between dt=1 and dt>1 value targets, enabling exploitation. Feature aliasing is seed-dependent because it depends on initialization geometry\\\\\\\"\\\\n  relevance_score: 4\\\\n  survey_tag: seed-dependent-stochastic-outcomes\\\\n\\\\n- paper_id: colas2018seeds\\\\n  title: \\\\\\\"How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments\\\\\\\"\\\\n  authors: [Colas C., Sigaud O., Oudeyer P.-Y.]\\\\n  year: 2018\\\\n  venue: \\\\\\\"arXiv:1806.08295\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"Provides statistical framework for determining seed count needed for significant algorithm comparison; our 2-seed observation (1/2 collapse) has limited statistical power by their analysis — but the qualitative difference (nve 4.12x vs 0.38x) is large enough that even 2 seeds establish the stochastic nature of the phenomenon. Methodological basis for future multi-seed validation\\\\\\\"\\\\n  relevance_score: 3\\\\n  survey_tag: seed-dependent-stochastic-outcomes\\\\n\\\\n- paper_id: nikishin2023plasticity\\\\n  title: \\\\\\\"Deep Reinforcement Learning with Plasticity Injection\\\\\\\"\\\\n  authors: [Nikishin E., Oh J., Ostrovski G., Lyle C., Pascanu R., Dabney W., Barreto A.]\\\\n  year: 2023\\\\n  venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"Plasticity injection augments network plasticity without changing parameter count; serves as a diagnostic tool — if injection improves performance, plasticity loss was the bottleneck. Directly applicable to diagnosing whether our seed-dependent collapse is plasticity-mediated: if plasticity injection prevents collapse in seed 0 but has no effect on seed 2 (which already self-corrects), it confirms plasticity loss as the bifurcation mechanism\\\\\\\"\\\\n  relevance_score: 4\\\\n  survey_tag: seed-dependent-stochastic-outcomes\\\\n\\\\n- paper_id: schwarzer2023bbf\\\\n  title: \\\\\\\"Bigger, Better, Faster: Human-level Atari with Human-level Efficiency\\\\\\\"\\\\n  authors: [Schwarzer M., Obando-Ceron J.S., Courville A., Bellemare M., Agarwal R., Castro P.S.]\\\\n  year: 2023\\\\n  venue: \\\\\\\"ICML 2023\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"BBF achieves SOTA sample efficiency via periodic network resets + scaling + weight decay; periodic resets prevent primacy bias accumulation across seeds. Suggests our delusional critic collapse might be preventable with periodic critic resets — the reset would break the positive feedback loop between overestimated values and actor exploitation before it becomes irreversible\\\\\\\"\\\\n  relevance_score: 3\\\\n  survey_tag: seed-dependent-stochastic-outcomes\\\\n\\\\n- paper_id: farebrother2024stopregressing\\\\n  title: \\\\\\\"Stop Regressing: Training Value Functions via Classification for Scalable Deep RL\\\\\\\"\\\\n  authors: [Farebrother J., Orbay J., Vuong Q., Taiga A.A., Chebotar Y., Xiao T., Irpan A., Levine S., Castro P.S., Faust A., Kumar A., Agarwal R.]\\\\n  year: 2024\\\\n  venue: \\\\\\\"ICML 2024\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"Shows categorical cross-entropy for value training provides implicit regularization against overestimation vs MSE regression. DreamerV3 already uses categorical value prediction (twohot + symlog) — yet our trained dt_embedding still induces collapse in some seeds, demonstrating that categorical value training is insufficient to prevent dt_embedding-induced value exploitation\\\\\\\"\\\\n  relevance_score: 3\\\\n  survey_tag: seed-dependent-stochastic-outcomes\\\\n\\\\n- paper_id: lyle2024normalization\\\\n  title: \\\\\\\"Normalization and Effective Learning Rates in Reinforcement Learning\\\\\\\"\\\\n  authors: [Lyle C., Zheng Z., Giunchiglia E., Sherstan C., Hashemizadeh M., Schuurmans D., Dabney W.]\\\\n  year: 2024\\\\n  venue: \\\\\\\"NeurIPS 2024\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Shows normalization layers combat overestimation but cause effective learning rate decay via parameter norm growth. Provides a potential mechanism for seed 2's self-correction: if parameter norms grow faster in certain initializations, effective LR decays faster, naturally damping value overestimation before it cascades into collapse. Seed 0's slower norm growth → sustained high effective LR → overestimation compounds → collapse\\\\\\\"\\\\n  relevance_score: 4\\\\n  survey_tag: seed-dependent-stochastic-outcomes\\\\n\\\\n# --- Survey synthesis: Seed-Dependent Stochastic Outcomes ---\\\\n# Summary (2026-05-14):\\\\n#\\\\n# 1. STOCHASTIC COLLAPSE HAS PRECEDENT:\\\\n#    Plasticity loss (Lyle 2022, Sokar 2023, Nikishin 2023) is inherently\\\\n#    seed-dependent because it depends on initialization → early gradient\\\\n#    dynamics → neuron activity patterns. Different seeds hit different\\\\n#    plasticity trajectories under identical configs.\\\\n#\\\\n# 2. nve>1.5x AS DIAGNOSTIC MARKER (necessary but not sufficient):\\\\n#    Lyle 2022 shows feature rank collapse is necessary but not sufficient\\\\n#    for learning failure. Kumar 2022 shows feature aliasing from TD\\\\n#    learning creates the overestimation substrate. Our nve>1.5x is\\\\n#    analogous: it indicates the dt_embedding has enabled value exploitation\\\\n#    (100% reliable marker), but collapse requires additional conditions\\\\n#    (plasticity loss, insufficient effective LR decay) that are stochastic.\\\\n#\\\\n# 3. SELF-CORRECTION MECHANISM:\\\\n#    Lyle 2024 provides a candidate mechanism: normalization-induced\\\\n#    effective LR decay can naturally damp overestimation in some seeds.\\\\n#    Farebrother 2024 shows categorical value training provides partial\\\\n#    implicit regularization. Together these explain why seed 2 self-corrects:\\\\n#    the combination of DreamerV3's categorical critic + normalization +\\\\n#    favorable initialization produces enough implicit regularization to\\\\n#    overcome the dt_embedding-induced overestimation.\\\\n#\\\\n# 4. THEORETICAL GROUNDING:\\\\n#    Zhang 2026 (already in map) provides the dynamical systems framework.\\\\n#    Bjorck 2022 (already in map) shows early outlier events dominate\\\\n#    variance. Together with the new papers, the framing is:\\\\n#    \\\\\\\"trained dt_embedding creates a necessary condition (nve>1.5x) for\\\\n#    delusional critic collapse, but collapse is a stochastic bifurcation\\\\n#    whose outcome depends on seed-dependent plasticity dynamics.\\\\\\\"\\\\n\\\\n# ============================================================\\\\n# INCREMENTAL SCAN (2026-05-14): Δt conditioning & adaptive horizon\\\\n# ============================================================\\\\n# 8 new papers from targeted search on:\\\\n#   - Δt/timestep conditioning in world models\\\\n#   - Variable-rate imagination / adaptive horizon\\\\n#   - Hierarchical planning with latent world models (2025-2026)\\\\n#\\\\n# KEY FINDING: TAWM (Nhu et al. ICML 2025) explicitly conditions\\\\n# world model on Δt — closest methodological overlap. But TAWM\\\\n# uses TD-MPC2 (online MPC) not imagination-based actor-critic,\\\\n# and treats Δt conditioning as beneficial. Our work diagnoses\\\\n# Δt conditioning as pathological in imagination-based training\\\\n# (delusional critic). Complementary, not duplicative.\\\\n\\\\n- paper_id: nhu2025tawm\\\\n  title: \\\\\\\"Time-Aware World Model for Adaptive Prediction and Control\\\\\\\"\\\\n  authors: [Nhu A.N., Son S., Lin M.C.]\\\\n  year: 2025\\\\n  venue: \\\\\\\"ICML 2025 (arXiv:2506.08441)\\\\\\\"\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"TAWM — explicitly conditions world model on time-step size Δt and trains over diverse Δt values for multi-rate dynamics learning. Built on TD-MPC2 (online MPC). KEY DISTINCTION from our work: (1) TAWM treats Δt conditioning as beneficial for performance/data-efficiency; we diagnose it as pathological in imagination-based actor-critic training (delusional critic). (2) TAWM uses MPC (no imagination rollouts for policy training); our failure mode is specific to imagination-based training where the critic exploits dt-conditioned value estimates. (3) TAWM focuses on observation-rate robustness; we focus on value overestimation from temporal conditioning corruption. TAWM actually strengthens our contribution: it shows Δt conditioning works in MPC settings, making our finding that it fails in imagination-based settings a surprising and important diagnostic.\\\\\\\"\\\\n  relevance_score: 5\\\\n  novelty_threat: \\\\\\\"MEDIUM — methodological overlap (Δt conditioning) but fundamentally different paradigm (MPC vs imagination) and opposite conclusion (beneficial vs pathological). Must cite and differentiate in paper.\\\\\\\"\\\\n\\\\n- paper_id: li2025lsimagine\\\\n  title: \\\\\\\"Open-World Reinforcement Learning over Long Short-Term Imagination\\\\\\\"\\\\n  authors: [Li J., Wang Q., Wang Y., Jin X., Li Y., Zeng W., Yang X.]\\\\n  year: 2025\\\\n  venue: \\\\\\\"ICLR 2025 Oral (arXiv:2410.03618)\\\\\\\"\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"LS-Imagine — extends imagination horizon in Dreamer via goal-conditioned jumpy state transitions and affordance maps. Addresses the 'short-sightedness' of standard Dreamer imagination. KEY DISTINCTION: LS-Imagine adds jumpy transitions to reach long-horizon targets (open-world Minecraft), while our work shows that variable-dt imagination itself introduces delusional critic. LS-Imagine's jumpy transitions use goal conditioning (not dt-embedding), potentially avoiding the value overestimation we identify.\\\\\\\"\\\\n  relevance_score: 4\\\\n  novelty_threat: \\\\\\\"LOW — different mechanism (goal-conditioned jumps vs dt-embedding) and different focus (long-horizon exploration vs diagnostic of failure modes). Should cite as concurrent approach to extending imagination horizon.\\\\\\\"\\\\n\\\\n- paper_id: zhang2026hwm\\\\n  title: \\\\\\\"Hierarchical Planning with Latent World Models\\\\\\\"\\\\n  authors: [Zhang W., Terver B., Zholus A., Chitnis S., Sutaria H., Assran M., Balestriero R., Bar A., Bardes A., LeCun Y., Ballas N.]\\\\n  year: 2026\\\\n  venue: \\\\\\\"arXiv:2604.03208\\\\\\\"\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"HWM — learns multi-scale latent world models for hierarchical MPC planning; high-level planner optimizes macro-actions, low-level planner handles primitives. 70% success on real-world non-greedy robotic tasks vs 0% for single-level. Addresses temporal abstraction via hierarchical planning (MPC), not imagination-based actor-critic. Further evidence that temporal abstraction in world models requires hierarchy rather than single-scale variable-dt approaches.\\\\\\\"\\\\n  relevance_score: 4\\\\n  novelty_threat: \\\\\\\"LOW — MPC-based hierarchical planning, not imagination-based training. Supports our thesis that flat dt-embedding approaches are inferior to hierarchical alternatives.\\\\\\\"\\\\n\\\\n- paper_id: kobayashi2025metacontroller\\\\n  title: \\\\\\\"Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning\\\\\\\"\\\\n  authors: [Kobayashi S., et al.]\\\\n  year: 2025\\\\n  venue: \\\\\\\"arXiv:2512.20605\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"MetaController — discovers temporal abstractions via higher-order non-causal sequence model controlling base autoregressive model's residual stream. Each controller executes behaviorally meaningful action sequences with learned termination conditions. Operates in fundamentally different paradigm (LLM-style autoregressive models, not world-model imagination), but demonstrates that temporal abstraction benefits from hierarchical structure rather than flat dt-conditioning.\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: shaj2023mts3\\\\n  title: \\\\\\\"Multi Time Scale World Models\\\\\\\"\\\\n  authors: [Shaj V., Gholam Zadeh S., Demir O., Luettjohann L., Neumann G., Toussaint M.]\\\\n  year: 2023\\\\n  venue: \\\\\\\"NeurIPS 2023 (arXiv:2310.18534)\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"MTS3 — probabilistic multi-time-scale state space model with fast and slow latent dynamics for variable-rate prediction. Provides efficient inference across temporal scales. Foundational multi-rate dynamics architecture; our work shows that even with proper multi-rate modeling, the downstream actor-critic training in imagination can exploit temporal conditioning for value overestimation — a failure mode MTS3 does not address (it focuses on prediction quality, not policy training).\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: splates2025\\\\n  title: \\\\\\\"Stable Planning with Temporally Extended Skills\\\\\\\"\\\\n  authors: [SPlaTES authors]\\\\n  year: 2025\\\\n  venue: \\\\\\\"Reinforcement Learning Journal (RLC 2025)\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"SPlaTES — hierarchical MPC with temporally extended skills + abstract skill world model. Skill learning via mutual-information objective yields diverse, predictable, task-related behavior. Demonstrates that stable long-horizon planning requires modeling skill outcomes (temporal abstraction via hierarchy), not primitive-action outcomes at variable time steps — consistent with our finding that flat dt-embedding fails.\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: beckerehmck2023multitimestep\\\\n  title: \\\\\\\"Multi-timestep models for Model-based Reinforcement Learning\\\\\\\"\\\\n  authors: [Becker-Ehmck P., Peters J., van der Smagt P.]\\\\n  year: 2023\\\\n  venue: \\\\\\\"arXiv:2310.05672\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Proposes multi-timestep training objective (weighted sum of losses at various future horizons) for one-step dynamics models to improve long-horizon R² score. Addresses compounding error at the model training level; our work shows that even with perfect multi-step prediction, the imagination-based actor-critic can still fail due to value overestimation from dt-conditioning — a downstream failure mode distinct from prediction accuracy.\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: liu2022dmve\\\\n  title: \\\\\\\"Dynamic-Horizon Model-Based Value Estimation With Latent Imagination\\\\\\\"\\\\n  authors: [Liu Y., et al.]\\\\n  year: 2022\\\\n  venue: \\\\\\\"IEEE TNNLS (arXiv:2009.09593)\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"DMVE — adaptive rollout horizon selection via horizon reliability detection (comparing value expansion errors between raw and reconstructed observations). Addresses the horizon selection problem in imagination-based value estimation. Complementary to our work: DMVE selects among fixed-dt horizons; we show that even optimal horizon selection cannot fix the delusional critic when dt-embedding is trained (the overestimation is in the value function, not the horizon length).\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# --- Incremental scan synthesis (2026-05-14) ---\\\\n#\\\\n# NOVELTY ASSESSMENT:\\\\n# No paper found that diagnoses dt_embedding → delusional critic\\\\n# (value overestimation) → stochastic collapse in imagination-based\\\\n# MBRL. Our core contribution remains novel.\\\\n#\\\\n# TAWM (ICML 2025) is the closest methodological overlap but\\\\n# operates in MPC paradigm and reaches opposite conclusion\\\\n# (Δt conditioning is beneficial). This actually STRENGTHENS\\\\n# our novelty: \\\\\\\"Δt conditioning helps in MPC but hurts in\\\\n# imagination-based training\\\\\\\" is a more nuanced and surprising finding.\\\\n#\\\\n# LANDSCAPE TREND:\\\\n# The field is converging on HIERARCHY (THICK, Hieros, Director,\\\\n# HWM, SPlaTES, MetaController) as the solution to temporal\\\\n# abstraction in world models, avoiding flat variable-dt approaches.\\\\n# Our diagnostic paper explains WHY flat dt approaches fail,\\\\n# providing theoretical grounding for this empirical trend.\\\\n#\\\\n# ACTION ITEMS FOR PAPER:\\\\n# 1. MUST CITE: nhu2025tawm — differentiate MPC vs imagination paradigm\\\\n# 2. SHOULD CITE: li2025lsimagine — concurrent Dreamer horizon extension\\\\n# 3. SHOULD CITE: shaj2023mts3 — multi-rate dynamics foundation\\\\n# 4. CONSIDER: zhang2026hwm — latest hierarchical WM planning\\\\n\\\", \\\"total_chars\\\": 50497, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
      "numLines": 1,
      "startLine": 0,
      "totalLines": 1
    }
  }
}
```

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
Now I have the literature map. Let me read the registry data in chunks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "ea419959-9d7c-4997-bce3-5a6370c461d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAUwYGmhWcUbtFngvgQoBc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16197,
      "cache_read_input_tokens": 41481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16197
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

_source line 26_

Let me read the registry data to understand experiment status.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "9c43d79e-8f12-4327-b163-9d5a87f57d62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAUwYGmhWcUbtFngvgQoBc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16197,
      "cache_read_input_tokens": 41481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16197
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

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01NkYw2Y6pUFjVAeP4GLh5Ey`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/e9efbf3e-355b-4b54-9c61-7a3e79247d76/tool-results/mcp-agent-ml-research-read_registry-1778807748281.txt",
  "offset": 0,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "da5429d7-f3a3-4e61-9e3d-de77bab66ac2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAUwYGmhWcUbtFngvgQoBc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16197,
      "cache_read_input_tokens": 41481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16197
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

_source line 28 · 2026-05-15T01:16:03.415Z_

<details><summary>↩ Tool result · reported error · `toolu_01NkYw2Y6pUFjVAeP4GLh5Ey`</summary>

```text
File content (27127 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "8ba9be94-ebd3-469a-ba54-ea3e6319c88c",
  "tool_use_result": "Error: File content (27127 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_01RojouEBcXACvDWkKMKmhsr`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/e9efbf3e-355b-4b54-9c61-7a3e79247d76/tool-results/mcp-agent-ml-research-read_registry-1778807748281.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nexperiments = json.loads(data['result'])['data']\nfor exp in experiments:\n    exp_id = exp.get('exp_id','?')\n    status = exp.get('status','?')\n    conclusion = exp.get('conclusion','')[:80] if exp.get('conclusion') else ''\n    print(f'{exp_id} | {status} | {conclusion}')\n\"",
  "description": "Extract experiment IDs, statuses, and conclusions from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "58879e53-af7b-4b27-a31a-0c80bf357468",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018eBpvaVnT2iFXDzK2pD6yR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 285,
      "cache_read_input_tokens": 57678,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 285
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

_source line 30 · 2026-05-15T01:16:16.042Z_

<details><summary>↩ Tool result · reported error · `toolu_01RojouEBcXACvDWkKMKmhsr`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
    exp_id = exp.get('exp_id','?')
             ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "acf5c3a0-906c-4f0d-a74f-fb2906a853be",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 6, in &lt;module>\n    exp_id = exp.get('exp_id','?')\n             ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'"
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_01XzKaMPYqDH7tjpTC1XnN6c`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/e9efbf3e-355b-4b54-9c61-7a3e79247d76/tool-results/mcp-agent-ml-research-read_registry-1778807748281.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\ndata = json.loads(raw)\nresult = json.loads(data['result'])\nexperiments = result['data']\nprint(type(experiments), len(experiments) if isinstance(experiments, list) else '')\nif isinstance(experiments, list) and len(experiments) > 0:\n    print(type(experiments[0]))\n    if isinstance(experiments[0], dict):\n        print(experiments[0].keys())\n    else:\n        print(repr(experiments[0][:200]))\nelif isinstance(experiments, dict):\n    print(list(experiments.keys())[:10])\n\"",
  "description": "Inspect registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "b2214cb0-dca8-4c71-a59c-63bd679d6664",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cff1QYzJjwXbyfbsKK5dej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 378,
      "cache_read_input_tokens": 57963,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 378
      },
      "output_tokens": 73,
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

_source line 32 · 2026-05-15T01:16:21.655Z_

<details><summary>↩ Tool result · `toolu_01XzKaMPYqDH7tjpTC1XnN6c`</summary>

```text
&lt;class 'dict'> 
['experiments', 'count', 'total', 'baseline']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "76aecdb6-1e10-49f0-9abd-7931cad68d03",
  "tool_use_result": {
    "stdout": "&lt;class 'dict'> \n['experiments', 'count', 'total', 'baseline']",
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

_source line 33_

<details open><summary>🔧 Tool call — Bash · `toolu_01MnHLY3FTQbW3YP68U1i51z`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/e9efbf3e-355b-4b54-9c61-7a3e79247d76/tool-results/mcp-agent-ml-research-read_registry-1778807748281.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\ndata = json.loads(raw)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\nfor exp in experiments:\n    exp_id = exp.get('exp_id','?')\n    status = exp.get('status','?')\n    conclusion = (exp.get('conclusion','') or '')[:100]\n    metrics = exp.get('metrics', {})\n    print(f'{exp_id} | {status} | {conclusion}')\n\"",
  "description": "List all experiments with status and conclusion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "e79ff77e-effb-48d5-b8f8-e547429a884f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0149w5jZc7p4ebo3BPDGRSDF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 359,
      "cache_read_input_tokens": 58341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 359
      },
      "output_tokens": 72,
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

_source line 34 · 2026-05-15T01:16:26.823Z_

<details><summary>↩ Tool result · reported error · `toolu_01MnHLY3FTQbW3YP68U1i51z`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 8, in &lt;module>
    exp_id = exp.get('exp_id','?')
             ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "87881734-c7c6-4add-a5f8-734d58f3340d",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 8, in &lt;module>\n    exp_id = exp.get('exp_id','?')\n             ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'"
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Bash · `toolu_014gB4sBDoNrRMt5GKMF4Phq`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/e9efbf3e-355b-4b54-9c61-7a3e79247d76/tool-results/mcp-agent-ml-research-read_registry-1778807748281.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\ndata = json.loads(raw)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\nprint(type(experiments))\nif isinstance(experiments, list):\n    print(f'count: {len(experiments)}')\n    print(f'first type: {type(experiments[0])}')\n    if isinstance(experiments[0], str):\n        print(experiments[0][:300])\nelif isinstance(experiments, dict):\n    for k in list(experiments.keys())[:3]:\n        print(f'{k}: {type(experiments[k])}')\n        if isinstance(experiments[k], dict):\n            print(f'  keys: {list(experiments[k].keys())[:5]}')\n\"",
  "description": "Inspect experiments data type"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "ac5fc27d-7579-4c16-b94b-46fc19493a84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ge6K3RgTdYphSN8ZMd48nU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 390,
      "cache_read_input_tokens": 58700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 390
      },
      "output_tokens": 72,
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

_source line 36 · 2026-05-15T01:16:34.391Z_

<details><summary>↩ Tool result · `toolu_014gB4sBDoNrRMt5GKMF4Phq`</summary>

```text
&lt;class 'dict'>
exp_009a_baseline_walker_s2: &lt;class 'dict'>
  keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis']
exp_008e_v3_walker_s2: &lt;class 'dict'>
  keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis']
exp_008e_v3_walker_s1: &lt;class 'dict'>
  keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "7a8c56e6-fb9b-49eb-977d-96bb7fbdca10",
  "tool_use_result": {
    "stdout": "&lt;class 'dict'>\nexp_009a_baseline_walker_s2: &lt;class 'dict'>\n  keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis']\nexp_008e_v3_walker_s2: &lt;class 'dict'>\n  keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis']\nexp_008e_v3_walker_s1: &lt;class 'dict'>\n  keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis']",
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

_source line 37_

<details open><summary>🔧 Tool call — Bash · `toolu_01Wx3DWes9nWfRVqupzbqRGY`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/e9efbf3e-355b-4b54-9c61-7a3e79247d76/tool-results/mcp-agent-ml-research-read_registry-1778807748281.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\ndata = json.loads(raw)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\nfor exp_id, exp_data in experiments.items():\n    status = exp_data.get('status','?')\n    conclusion = (exp_data.get('conclusion','') or '')[:80]\n    metrics = exp_data.get('metrics', {})\n    eval_ret = ''\n    if metrics:\n        eval_ret = str(metrics.get('eval_return',''))[:30]\n    print(f'{exp_id} | {status} | eval={eval_ret} | {conclusion}')\n\"",
  "description": "List all experiments from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "fe1bf191-724d-4375-bfb1-88085cf6567d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JuFBmQQyFkNq4TgdS78kYW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 524,
      "cache_read_input_tokens": 59090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 524
      },
      "output_tokens": 72,
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

_source line 38 · 2026-05-15T01:16:45.644Z_

<details><summary>↩ Tool result · `toolu_01Wx3DWes9nWfRVqupzbqRGY`</summary>

```text
exp_009a_baseline_walker_s2 | RUNNING | eval= | 
exp_008e_v3_walker_s2 | RUNNING | eval= | 
exp_008e_v3_walker_s1 | DONE | eval= | success
exp_006 | DONE | eval={'5000': 31, '15000': 256.9, ' | killed
exp_008a | DONE | eval= | killed
exp_008c | DONE | eval= | killed
exp_008d | DONE | eval= | killed
exp_008e_v2_subsample_on_dt1_h15 | DONE | eval= | killed
exp_rssm_fidelity_analysis | DONE | eval= | success
exp_008e_v3_subsample_on_dt1_h15 | DONE | eval={'5K': 31, '15K': 131.2, '25K' | success
exp_009b_008d_walker_s2 | DONE | eval= | negative
exp_009d_baseline_walker_s1 | QUEUED | eval= | 
exp_009e_008d_walker_s1 | QUEUED | eval= | 
exp_009c_008f_walker_s2 | DONE | eval= | negative
exp_010a_cheetah_baseline_s1 | QUEUED | eval= | 
exp_009f_008f_walker_s1 | QUEUED | eval= | 
exp_007_fixed_dt4 | DONE | eval= | negative
exp_006_fixed_dt2 | DONE | eval= | negative
exp_008d_subsample_on_h8 | DONE | eval= | negative
exp_008f_no_dt_embed_subsample_on_h8 | DONE | eval= | success
exp_008a_no_subsample_dt2 | DONE | eval= | success
exp_001_baseline | DONE | eval= | success
exp_008c_no_subsample_dt2_h8 | DONE | eval= | negative
exp_008e_subsample_on_fixed_dt1 | DONE | eval= | killed
exp_008e_subsample_on_dt1_h15 | DONE | eval= | killed
exp_005_event_gated_v4 | DONE | eval= | negative
exp_004_event_gated_v3 | DONE | eval= | negative
exp_003_event_gated_v2 | DONE | eval= | negative
exp_002_event_gated | DONE | eval= | failed
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "63c4f263-e0eb-41f7-838f-e8e61c0b5cc9",
  "tool_use_result": {
    "stdout": "exp_009a_baseline_walker_s2 | RUNNING | eval= | \nexp_008e_v3_walker_s2 | RUNNING | eval= | \nexp_008e_v3_walker_s1 | DONE | eval= | success\nexp_006 | DONE | eval={'5000': 31, '15000': 256.9, ' | killed\nexp_008a | DONE | eval= | killed\nexp_008c | DONE | eval= | killed\nexp_008d | DONE | eval= | killed\nexp_008e_v2_subsample_on_dt1_h15 | DONE | eval= | killed\nexp_rssm_fidelity_analysis | DONE | eval= | success\nexp_008e_v3_subsample_on_dt1_h15 | DONE | eval={'5K': 31, '15K': 131.2, '25K' | success\nexp_009b_008d_walker_s2 | DONE | eval= | negative\nexp_009d_baseline_walker_s1 | QUEUED | eval= | \nexp_009e_008d_walker_s1 | QUEUED | eval= | \nexp_009c_008f_walker_s2 | DONE | eval= | negative\nexp_010a_cheetah_baseline_s1 | QUEUED | eval= | \nexp_009f_008f_walker_s1 | QUEUED | eval= | \nexp_007_fixed_dt4 | DONE | eval= | negative\nexp_006_fixed_dt2 | DONE | eval= | negative\nexp_008d_subsample_on_h8 | DONE | eval= | negative\nexp_008f_no_dt_embed_subsample_on_h8 | DONE | eval= | success\nexp_008a_no_subsample_dt2 | DONE | eval= | success\nexp_001_baseline | DONE | eval= | success\nexp_008c_no_subsample_dt2_h8 | DONE | eval= | negative\nexp_008e_subsample_on_fixed_dt1 | DONE | eval= | killed\nexp_008e_subsample_on_dt1_h15 | DONE | eval= | killed\nexp_005_event_gated_v4 | DONE | eval= | negative\nexp_004_event_gated_v3 | DONE | eval= | negative\nexp_003_event_gated_v2 | DONE | eval= | negative\nexp_002_event_gated | DONE | eval= | failed",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need to create the writing plan. Let me compile:

1. Paper framing: Claims C1-C6, narrative, figures, anticipated concerns
2. Memory: Key decisions, analysis results, lessons
3. Literature map: 72 papers, categories, novelty assessment
4. Registry: Experiment statuses

Key experiments by status:
- DONE: exp_001_baseline, exp_005-008 variants, exp_008e_v3, exp_009b, exp_009c, exp_008e_v3_walker_s1
- RUNNING: exp_009a_baseline_walker_s2, exp_008e_v3_walker_s2


- QUEUED: exp_009d_baseline_walker_s1, exp_009e_008d_walker_s1, exp_009f_008f_walker_s1, exp_010a_cheetah_baseline_s1

With the CoRL 2026 deadline in 14 days and 8 pages to work with, I need to prioritize the Walker Walk results as my main focus while flagging the Cheetah and Cartpole experiments as pending. I'm creating the writing_plan.yaml with the hero learning curve figure as the centerpiece, showing all configurations across the available multi-seed data.

The paper structure flows from data-ready sections first—starting with Experiments and Results to establish the empirical foundation, then Method and Setup to explain the design, followed by Analysis and Discussion where I can dig into the mechanisms and RSSM fidelity patterns. Introduction and Related Work come next to frame the contributions, with Abstract and Conclusion written last once the narrative solidifies.

I'm tracking three key risks: the Cheetah and Cartpole experiments are still queued so cross-environment claims may need scoping, exp_008e_v3_walker_s2 is still running which affects the C6 multi-seed confirmation, and exp_009e_008d_walker_s1 is queued with incomplete collapse probability estimation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "33eb5090-ffa3-42c9-99ba-a16bedef07f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013VAF4R2eV26C3asE3ihzUD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 990,
      "cache_read_input_tokens": 59614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 990
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

_source line 40_

Now I have all the information needed. Let me create the writing plan.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "548921ff-5df6-4394-8a01-bead7f04caef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013VAF4R2eV26C3asE3ihzUD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 990,
      "cache_read_input_tokens": 59614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 990
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

_source line 41_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01BdEQQnBzr3uvnLyg7qKbwz`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "writing_plan.yaml",
  "content": "# Writing Plan — CoRL 2026\n# Paper: Diagnostic Analysis of Temporal Abstraction in World-Model RL\n# Deadline: 2026-05-29 (14 days from today)\n# Format: 8 pages + references\n# Last updated: 2026-05-15\n\nvenue:\n  name: CoRL 2026\n  deadline: 2026-05-29\n  format: \"8 pages + unlimited references\"\n  template: corl2026  # IEEE two-column\n  positioning: diagnostic-analysis  # NOT method paper\n\n# ============================================================\n# PAPER STRUCTURE\n# ============================================================\n\nsections:\n  - id: abstract\n    title: Abstract\n    target_words: 200\n    content_outline: |\n      Temporal abstraction via variable-dt imagination in world-model RL (DreamerV3) consistently degrades performance.\n      We conduct a factorial diagnostic isolating trained dt_embedding as the reliable trigger for pathological value\n      overestimation (nve>1.5x, 4/4 separating power across seeds). Collapse is stochastic (seed-dependent), but the\n      diagnostic marker is deterministic. Practical mitigation: restrict imagination to dt=1 during multi-dt training\n      → 95% baseline recovery with cross-seed consistency (869.9±0.01 vs baseline 915.67).\n    claims_referenced: [C1, C2, C3, C6]\n    data_ready: true\n    writing_order: 8  # last\n\n  - id: introduction\n    title: Introduction\n    target_pages: 1.0\n    content_outline: |\n      (1) Temporal abstraction is a long-sought goal; world-model RL offers natural testbed via imagination dt.\n      (2) Puzzle: all variable-rate attempts degrade. TAWM shows Δt conditioning works in MPC — why does it fail\n      in imagination-based actor-critic?\n      (3) Contribution: closed causal chain (trained dt_emb → nve>1.5x → stochastic collapse) + practical mitigation\n      (dt=1 imagination, 95% recovery). Diagnostic methodology with factorial design.\n      (4) Scope: DreamerV3/RSSM, Walker Walk (+ cross-env if ready).\n    claims_referenced: [C1, C2, C6]\n    key_references: [hafner2023dreamerv3, nhu2025tawm, lu2018nondelusional, gumbsch2024thick]\n    data_ready: true\n    writing_order: 6\n\n  - id: related_work\n    title: Related Work\n    target_pages: 1.0\n    content_outline: |\n      (1) Temporal abstraction in RL: options (Sutton 1999), FiGAR, TempoRL, SDAR — all model-free.\n      (2) World-model RL & imagination: DreamerV1-V4, IRIS, TWM — standard dt=1 imagination.\n      (3) Variable-rate world models: TAWM (MPC, beneficial), THICK/Hieros (hierarchy), MTS3, LS-Imagine.\n      (4) Value overestimation in MBRL: MBPO, MOPO, delusional bias (Lu 2018), MAD-TD.\n      (5) Diagnostic methodology precedent: Implementation Matters, What Matters for Actor-Critic.\n      Differentiate from TAWM (MPC vs imagination paradigm — opposite conclusions on Δt conditioning).\n    claims_referenced: []\n    key_references: [sutton1999options, sharma2017figar, biedenkapp2021temporl, hafner2023dreamerv3,\n                     nhu2025tawm, gumbsch2024thick, mattes2024hieros, shaj2023mts3, li2025lsimagine,\n                     janner2019mbpo, yu2020mopo, lu2018nondelusional, su2020conqur,\n                     engstrom2020implementation, andrychowicz2021whatmatters, frauenknecht2025rollouts]\n    data_ready: true\n    writing_order: 7\n\n  - id: methodology\n    title: \"Experimental Setup\"\n    target_pages: 1.5\n    content_outline: |\n      (1) DreamerV3 base architecture (RSSM, symlog, discrete latents) — brief, cite original.\n      (2) Variable-rate imagination mechanism: dt_embedding (trained/untrained/removed), temporal subsampling,\n      imagination horizon H. How each factor modifies imagination rollouts.\n      (3) Factorial design: 2×2×2 grid (dt_emb training × subsample × H) + fixed-dt baselines + mitigation.\n      Present grid as table with cell assignments.\n      (4) Diagnostic metrics: eval return, v/e ratio, normalized v/e (nve = exp_v/e / baseline_v/e at same step),\n      nve>1.5x threshold, RSSM fidelity (obs_MSE, reward_MAE at dt=1 vs dt=2).\n      (5) Environment: Walker Walk (DMC), 500K baseline / 105K treatments, 2+ seeds per config.\n    claims_referenced: [C1, C2, C3, C4, C5, C6]\n    key_references: [hafner2023dreamerv3, agarwal2021precipice]\n    data_ready: true\n    writing_order: 2\n\n  - id: results\n    title: Results\n    target_pages: 2.5\n    content_outline: |\n      Organized by findings (F1-F6 mapping to C1-C6):\n      F1 (C1): All dt>1 degrade — learning curves overlay (exp_001, 005, 006, 007).\n      F2 (C2): Trained dt_emb → nve>1.5x (4/4 separation). 008d vs 008f causal control.\n      Stochastic collapse: 008d seed 1 sustained nve>1.5x → collapse; 009b seed 2 transient → self-correction.\n      F3 (C3): Untrained dt_emb prevents drift — 008a@105K=778, nve 0.59-0.93x.\n      F4 (C4): dt=2 > dt=4 monotonic degradation.\n      F5 (C5): Horizon/subsample secondary — 008c (H=8) vs 008a (H=15).\n      F6 (C6): dt=1 imagination mitigation — 008e_v3@105K=869.9 (95% baseline), cross-seed consistent (s0≈s1).\n    claims_referenced: [C1, C2, C3, C4, C5, C6]\n    experiments_required:\n      - exp_001_baseline  # DONE\n      - exp_005_event_gated_v4  # DONE\n      - exp_006_fixed_dt2  # DONE\n      - exp_007_fixed_dt4  # DONE\n      - exp_008a_no_subsample_dt2  # DONE\n      - exp_008c_no_subsample_dt2_h8  # DONE\n      - exp_008d_subsample_on_h8  # DONE\n      - exp_008e_v3_subsample_on_dt1_h15  # DONE\n      - exp_008f_no_dt_embed_subsample_on_h8  # DONE\n      - exp_009b_008d_walker_s2  # DONE\n      - exp_009c_008f_walker_s2  # DONE\n      - exp_008e_v3_walker_s1  # DONE\n      - exp_008e_v3_walker_s2  # RUNNING\n      - exp_009a_baseline_walker_s2  # RUNNING\n    data_ready: partial  # 008e_v3_s2 and baseline_s2 still running\n    writing_order: 1  # write first — data-rich, anchors everything\n\n  - id: analysis\n    title: \"Analysis & Discussion\"\n    target_pages: 1.5\n    content_outline: |\n      (1) Mechanism: trained dt_emb enables reward head to produce systematically biased dt>1 predictions\n      (reward gap 2.78x in 008d). Critic trained on these → optimistic value landscape → actor exploitation.\n      RSSM fidelity table: absolute errors + ratios side-by-side.\n      (2) Stochastic collapse: why sustained vs transient nve>1.5x diverges (plasticity, primacy bias).\n      Connect to Zhang 2026, Lyle 2022, Bjorck 2022.\n      (3) Why MPC is immune: TAWM uses Δt conditioning successfully because MPC re-plans from real states.\n      Imagination-based training accumulates value error across full rollout → exploit.\n      (4) 008f trade-off: removing dt_emb eliminates delusional critic but destroys reward prediction (75x MAE).\n      008e_v3 as the correct fix (keeps trained dt_emb, restricts imagination to dt=1).\n      (5) Implications: current RSSM insufficient for dt>1 imagination; hierarchy (THICK, Hieros) as correct direction.\n    claims_referenced: [C2, C3, C6]\n    key_references: [nhu2025tawm, lu2018nondelusional, zhang2026instability, lyle2022capacity,\n                     lee2024dreamsmooth, ma2024harmonydream, gumbsch2024thick, mattes2024hieros]\n    data_ready: true\n    writing_order: 3\n\n  - id: conclusion\n    title: Conclusion\n    target_pages: 0.5\n    content_outline: |\n      Summarize causal chain. Practical takeaway: use dt=1 imagination even with multi-dt training data.\n      Limitations: single environment (Walker Walk) primary, DreamerV3/RSSM-specific.\n      Future: uncertainty-gated imagination truncation, hierarchical approaches, improved RSSM fidelity.\n    claims_referenced: [C2, C6]\n    data_ready: true\n    writing_order: 9\n\n# ============================================================\n# FIGURES\n# ============================================================\n\nfigures:\n  - id: fig1_learning_curves\n    title: \"Learning curves across all configurations\"\n    description: |\n      Hero figure. All experiments overlaid showing systematic degradation pattern.\n      Groups: baseline (dt=1), fixed dt>1 (006, 007), learned gate (005),\n      factorial ablations (008a-f), mitigation (008e_v3).\n    data_source: [exp_001_baseline, exp_005_event_gated_v4, exp_006_fixed_dt2, exp_007_fixed_dt4,\n                  exp_008a_no_subsample_dt2, exp_008d_subsample_on_h8, exp_008e_v3_subsample_on_dt1_h15]\n    placement: results (F1/C1)\n    status: data_ready  # all experiments DONE\n    gpu_cost: 0\n\n  - id: fig2_nve_trajectory\n    title: \"Normalized value/eval ratio trajectories — diagnostic marker\"\n    description: |\n      nve over training steps for key experiments. 1.5x threshold line marked.\n      Show: 008d seed 1 (sustained >1.5x → collapse), 009b seed 2 (transient >1.5x → self-correction),\n      008f seeds (both <1.5x), 008e_v3 (healthy, ~0.80x). 4/4 separation at threshold.\n    data_source: [exp_008d_subsample_on_h8, exp_009b_008d_walker_s2,\n                  exp_008f_no_dt_embed_subsample_on_h8, exp_009c_008f_walker_s2,\n                  exp_008e_v3_subsample_on_dt1_h15, exp_001_baseline]\n    placement: results (F2/C2)\n    status: data_ready\n    gpu_cost: 0\n\n  - id: fig3_factorial_grid\n    title: \"Factorial experiment summary (2×2 grid)\"\n    description: |\n      2×2 grid: dt_emb (trained/untrained) × subsample (ON/OFF), with H as secondary axis.\n      Each cell shows final eval return + nve status (healthy/pathological).\n      Clearly shows trained dt_emb as the separating factor.\n    data_source: [exp_008a_no_subsample_dt2, exp_008c_no_subsample_dt2_h8,\n                  exp_008d_subsample_on_h8, exp_006_fixed_dt2]\n    placement: results (F2-F5)\n    status: data_ready\n    gpu_cost: 0\n\n  - id: fig4_mechanism_diagram\n    title: \"Causal mechanism diagram\"\n    description: |\n      Flow diagram: trained dt_embedding → RSSM dt>1 predictions (low fidelity) →\n      reward head systematic bias (2.78x gap) → critic value overestimation (nve>1.5x) →\n      actor exploits overestimated values → performance collapse (stochastic gate: sustained vs transient).\n      Include dt=1 imagination as \"circuit breaker\" at the imagination step.\n    data_source: []  # conceptual figure\n    placement: analysis\n    status: ready_to_draw\n    gpu_cost: 0\n\n  - id: fig5_dt_amplification\n    title: \"Performance vs dt (monotonic degradation)\"\n    description: |\n      Bar or line chart: dt=1 (baseline ~950) > dt=2 (peak 485) > dt=4 (peak 177).\n      Clear monotonic relationship.\n    data_source: [exp_001_baseline, exp_006_fixed_dt2, exp_007_fixed_dt4]\n    placement: results (F4/C4)\n    status: data_ready\n    gpu_cost: 0\n\n  - id: fig6_mitigation\n    title: \"Mitigation comparison: dt=1 imagination recovers 95% baseline\"\n    description: |\n      Side-by-side or overlay: baseline, 008e_v3 (mitigation, 95%), 008a (untrained dt_emb, 85%),\n      006 (trained dt_emb + dt>1, collapse). Shows mitigation is best non-baseline option.\n      Include seed 0 + seed 1 for 008e_v3 showing cross-seed consistency.\n    data_source: [exp_001_baseline, exp_008e_v3_subsample_on_dt1_h15, exp_008e_v3_walker_s1,\n                  exp_008a_no_subsample_dt2, exp_006_fixed_dt2]\n    placement: results (F6/C6)\n    status: data_ready  # s1 DONE, s2 RUNNING but s0+s1 already show consistency\n    gpu_cost: 0\n\n# ============================================================\n# TABLES\n# ============================================================\n\ntables:\n  - id: tab1_rssm_fidelity\n    title: \"RSSM prediction fidelity at dt=1 vs dt=2\"\n    description: |\n      Three models (baseline, 008d collapsed, 008f no-dt-emb) × two metrics (obs_MSE, reward_MAE)\n      × two dt values (1, 2). Report absolute values AND ratios. Key: 008d reward gap 2.78x\n      (delusional source), 008f reward gap 1.01x (no distinction → no exploitation but also no learning).\n    data_source: [exp_rssm_fidelity_analysis]\n    placement: analysis\n    status: data_ready\n    gpu_cost: 0\n\n  - id: tab2_factorial_summary\n    title: \"Factorial experiment design and results\"\n    description: |\n      Full grid showing all experimental conditions and key outcomes.\n      Columns: exp_id, dt_emb (trained/untrained/none), subsample, H, dt_imag, final_eval,\n      nve_peak, collapse_status.\n    data_source: [all_experiments]\n    placement: methodology/results\n    status: data_ready\n    gpu_cost: 0\n\n  - id: tab3_multi_seed\n    title: \"Multi-seed results summary\"\n    description: |\n      Per-config seed results with IQM. Show 008d (1/2 collapse), 008f (0/2 collapse),\n      008e_v3 (0/2 collapse, nearly identical performance), baseline (0/2 collapse).\n    data_source: [exp_008d_subsample_on_h8, exp_009b_008d_walker_s2,\n                  exp_008f_no_dt_embed_subsample_on_h8, exp_009c_008f_walker_s2,\n                  exp_008e_v3_subsample_on_dt1_h15, exp_008e_v3_walker_s1,\n                  exp_001_baseline, exp_009a_baseline_walker_s2]\n    placement: results\n    status: partial  # baseline_s2 and 008e_v3_s2 still RUNNING\n    gpu_cost: 0\n\n# ============================================================\n# WRITING ORDER (by dependency)\n# ============================================================\n\nwriting_order:\n  - order: 1\n    section: results\n    reason: \"Data-rich, anchors all other sections. Most figures/tables go here.\"\n    blocker: null\n\n  - order: 2\n    section: methodology\n    reason: \"Defines experiment design referenced by results. Can write in parallel with results.\"\n    blocker: null\n\n  - order: 3\n    section: analysis\n    reason: \"Interprets results, requires results section to be stable.\"\n    blocker: results\n\n  - order: 4\n    section: related_work\n    reason: \"literature_map complete (72 papers). Position against TAWM, THICK, Hieros.\"\n    blocker: null  # can write early\n\n  - order: 5\n    section: introduction\n    reason: \"Frames contributions — needs results and analysis solidified.\"\n    blocker: [results, analysis]\n\n  - order: 6\n    section: conclusion\n    reason: \"Summarizes; last content section.\"\n    blocker: [results, analysis]\n\n  - order: 7\n    section: abstract\n    reason: \"Written last, distills entire paper.\"\n    blocker: [introduction, results, analysis, conclusion]\n\n# ============================================================\n# LITERATURE STRATEGY\n# ============================================================\n\nliterature:\n  must_cite:\n    - hafner2023dreamerv3  # base system\n    - hafner2020dreamerv1  # architecture family\n    - hafner2021dreamerv2  # discrete latents predecessor\n    - sutton1999options  # temporal abstraction foundation\n    - lu2018nondelusional  # delusional bias theory\n    - nhu2025tawm  # closest competitor — MUST differentiate MPC vs imagination\n    - gumbsch2024thick  # hierarchical alternative in Dreamer\n    - mattes2024hieros  # hierarchical imagination\n    - janner2019mbpo  # model exploitation in MBRL\n    - agarwal2021precipice  # evaluation methodology (IQM)\n    - henderson2018deep  # seed variance\n    - frauenknecht2025rollouts  # imagination rollout quality (ICLR 2025)\n    - lee2024dreamsmooth  # reward prediction bottleneck\n    - zhang2026instability  # training instability dynamics\n\n  should_cite:\n    - li2025lsimagine  # concurrent Dreamer horizon extension\n    - shaj2023mts3  # multi-rate dynamics foundation\n    - sharma2017figar  # FiGAR — learned action repeat\n    - biedenkapp2021temporl  # TempoRL — model-free temporal abstraction\n    - fujimoto2018td3  # overestimation in actor-critic\n    - vanhasselt2016double  # double Q-learning\n    - yu2020mopo  # pessimistic MBRL\n    - su2020conqur  # delusional bias mitigation\n    - tallec2019making  # time discretization sensitivity\n    - engstrom2020implementation  # diagnostic methodology precedent\n    - andrychowicz2021whatmatters  # factorial study precedent\n    - lyle2022capacity  # necessary vs sufficient conditions\n    - bjorck2022variance  # early outlier runs\n    - qiao2023mind  # primacy bias in MBRL\n    - ma2024harmonydream  # obs vs reward prediction balance\n    - voelcker2025madtd  # value misgeneralization\n    - hafner2025dreamerv4  # DreamerV4 (scope limitation discussion)\n\n  consider_citing:\n    - zhang2026hwm  # hierarchical world model planning\n    - park2021sar  # time-discretization invariant action repeat\n    - nikishin2022primacy  # primacy bias\n    - sokar2023dormant  # dormant neurons\n    - lyle2024normalization  # normalization & effective LR\n    - kumar2022dr3  # feature aliasing\n    - hansen2024tdmpc2  # TD-MPC2 (contrast MPC paradigm)\n    - hafner2022director  # hierarchical Dreamer\n\n# ============================================================\n# RISK ASSESSMENT\n# ============================================================\n\nrisks:\n  - id: risk_cross_env\n    severity: medium\n    description: \"Cheetah Run / Cartpole experiments still QUEUED (exp_010a). No cross-environment data.\"\n    mitigation: \"Scope claims to Walker Walk + DreamerV3. Discuss generalizability as future work. If 010a finishes by May 27, include.\"\n    dependent_claims: [C1]\n    blocking_experiments: [exp_010a_cheetah_baseline_s1]\n\n  - id: risk_c6_seed2\n    severity: low\n    description: \"exp_008e_v3_walker_s2 still RUNNING. Need for 3-seed C6 confidence interval.\"\n    mitigation: \"Already have s0 (869.88) and s1 (869.9) — nearly identical. s2 is bonus, not critical.\"\n    dependent_claims: [C6]\n    blocking_experiments: [exp_008e_v3_walker_s2]\n\n  - id: risk_baseline_s2\n    severity: low\n    description: \"exp_009a_baseline_walker_s2 RUNNING. Needed for multi-seed baseline reference.\"\n    mitigation: \"Already have s0 (exp_001, 915.67). Can report 2-seed results if s2 not done.\"\n    dependent_claims: [C1, C2, C3]\n    blocking_experiments: [exp_009a_baseline_walker_s2]\n\n  - id: risk_collapse_probability\n    severity: low\n    description: \"exp_009e (008d seed 1 repeat) QUEUED — would narrow collapse probability from 1/2 to 1/3 or 2/3.\"\n    mitigation: \"Current 1/2 is honest and transparent. Report as 'stochastic (1/2 seeds)' with caveat.\"\n    dependent_claims: [C2]\n    blocking_experiments: [exp_009e_008d_walker_s1]\n\n  - id: risk_page_budget\n    severity: medium\n    description: \"8 pages tight for 6 claims + factorial design + RSSM analysis + multi-seed.\"\n    mitigation: \"Prioritize C1, C2, C6 in main text. C3-C5 can be condensed. Use appendix for extended data.\"\n\n# ============================================================\n# TIMELINE\n# ============================================================\n\ntimeline:\n  - date: 2026-05-15\n    milestone: \"Writing plan finalized. Begin Results + Methodology drafting.\"\n  - date: 2026-05-17\n    milestone: \"Results draft complete. All figures generated (0 GPU cost).\"\n  - date: 2026-05-19\n    milestone: \"Analysis & Discussion draft. Related Work draft.\"\n  - date: 2026-05-21\n    milestone: \"Introduction draft. Full paper skeleton assembled.\"\n  - date: 2026-05-23\n    milestone: \"Internal review pass. Abstract + Conclusion. Page budget check.\"\n  - date: 2026-05-25\n    milestone: \"Revision pass. Incorporate any new experiment results (RUNNING → DONE).\"\n  - date: 2026-05-27\n    milestone: \"Final polish. Reference check. Supplementary materials.\"\n  - date: 2026-05-29\n    milestone: \"Submission deadline.\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "d0a9199d-452c-44ab-b097-fd21f9a2f8ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013VAF4R2eV26C3asE3ihzUD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 990,
      "cache_read_input_tokens": 59614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 990
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

_source line 42 · 2026-05-15T01:19:04.263Z_

<details><summary>↩ Tool result · `toolu_01BdEQQnBzr3uvnLyg7qKbwz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/writing_plan.yaml\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "902d0045-a818-4ea0-8559-ed7ebe34553f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/writing_plan.yaml\\\", \\\"saved\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/writing_plan.yaml\", \"saved\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 43_

Now let me send the progress summary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "fb43bbc6-d87c-43b0-a264-4f5fa7f724c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019nnJqjWRrN7G62H6UdtFP6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6897,
      "cache_read_input_tokens": 60604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6897
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

_source line 44_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EbontuEruPyxKtgm1P9eLv`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
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
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "4f938c7b-3662-4946-b675-929250ce1890",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019nnJqjWRrN7G62H6UdtFP6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6897,
      "cache_read_input_tokens": 60604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6897
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

_source line 45 · 2026-05-15T01:19:10.023Z_

<details><summary>↩ Tool result · `toolu_01EbontuEruPyxKtgm1P9eLv`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "230f01bb-0cce-42ce-aed5-17a323c34545",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
Let me register the artifact and send the progress update via feishu.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "692355a5-b456-4d4f-86e2-f2168c8344df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Veb9ES2XPdyQ4wh7SxG5kq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 823,
      "cache_read_input_tokens": 67501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 823
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

_source line 47_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01TZJBMrEbtSdQ9axZNnBFBE`</summary>

```json
{
  "name": "writing_plan_corl2026",
  "type": "intermediate",
  "description": "CoRL 2026 论文写作计划：8 sections, 6 figures, 3 tables, 14天时间线。写作顺序：Results→Methodology→Analysis→Related Work→Introduction→Conclusion→Abstract。",
  "project": "event-gated-adaptive-horizon",
  "tags": [
    "writing",
    "corl2026",
    "plan"
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
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "235a37d0-a745-46de-8120-bbc8219da755",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Veb9ES2XPdyQ4wh7SxG5kq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 823,
      "cache_read_input_tokens": 67501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 823
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

_source line 48 · 2026-05-15T01:19:15.763Z_

<details><summary>↩ Tool result · `toolu_01TZJBMrEbtSdQ9axZNnBFBE`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"One of source_path, content, or url must be provided.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "7925e9a8-56b0-432c-9520-8664250a75cb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"One of source_path, content, or url must be provided.\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"One of source_path, content, or url must be provided.\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012bcvhjTJoYpB5TUDvajV9R`</summary>

```json
{
  "query": "send progress feishu",
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
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "58ab56c7-79cb-4d3a-8ab5-dab41c5efb4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Veb9ES2XPdyQ4wh7SxG5kq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 823,
      "cache_read_input_tokens": 67501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 823
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

_source line 50 · 2026-05-15T01:19:16.049Z_

<details><summary>↩ Tool result · `toolu_012bcvhjTJoYpB5TUDvajV9R`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "PushNotification"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "Monitor"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
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
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "2eafab8b-3a5a-4947-b9a7-4901b95249a6",
  "tool_use_result": {
    "matches": [
      "PushNotification",
      "Monitor",
      "TodoWrite"
    ],
    "query": "send progress feishu",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01655sNLbPdPpKxqitTafeTr`</summary>

```json
{
  "name": "writing_plan_corl2026",
  "type": "intermediate",
  "description": "CoRL 2026 论文写作计划：7 sections, 6 figures, 3 tables, 14天时间线 (May 15-29)。写作顺序：Results→Methodology→Analysis→Related Work→Introduction→Conclusion→Abstract。",
  "project": "event-gated-adaptive-horizon",
  "content": "See writing_plan.yaml in project files.",
  "content_filename": "writing_plan_note.txt",
  "tags": [
    "writing",
    "corl2026",
    "plan"
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
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "344cd758-548a-44c7-a8a1-85b1acd8a9b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Q9w9FGw4tK9ur5QSCiWFn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4898,
      "cache_read_input_tokens": 68324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4898
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

_source line 52 · 2026-05-15T01:19:24.928Z_

<details><summary>↩ Tool result · `toolu_01655sNLbPdPpKxqitTafeTr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_2e7b9a\", \"name\": \"writing_plan_corl2026\", \"type\": \"intermediate\", \"description\": \"CoRL 2026 论文写作计划：7 sections, 6 figures, 3 tables, 14天时间线 (May 15-29)。写作顺序：Results→Methodology→Analysis→Related Work→Introduction→Conclusion→Abstract。\", \"path\": \"projects/event-gated-adaptive-horizon/artifacts/_project/intermediate/writing_plan_note.txt\", \"url\": null, \"project\": \"event-gated-adaptive-horizon\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T01:19:24.787041+00:00\", \"tags\": [\"writing\", \"corl2026\", \"plan\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "ac5602e2-f8ec-404a-93ef-e7860ec019fa",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_2e7b9a\\\", \\\"name\\\": \\\"writing_plan_corl2026\\\", \\\"type\\\": \\\"intermediate\\\", \\\"description\\\": \\\"CoRL 2026 论文写作计划：7 sections, 6 figures, 3 tables, 14天时间线 (May 15-29)。写作顺序：Results→Methodology→Analysis→Related Work→Introduction→Conclusion→Abstract。\\\", \\\"path\\\": \\\"projects/event-gated-adaptive-horizon/artifacts/_project/intermediate/writing_plan_note.txt\\\", \\\"url\\\": null, \\\"project\\\": \\\"event-gated-adaptive-horizon\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T01:19:24.787041+00:00\\\", \\\"tags\\\": [\\\"writing\\\", \\\"corl2026\\\", \\\"plan\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_2e7b9a\", \"name\": \"writing_plan_corl2026\", \"type\": \"intermediate\", \"description\": \"CoRL 2026 论文写作计划：7 sections, 6 figures, 3 tables, 14天时间线 (May 15-29)。写作顺序：Results→Methodology→Analysis→Related Work→Introduction→Conclusion→Abstract。\", \"path\": \"projects/event-gated-adaptive-horizon/artifacts/_project/intermediate/writing_plan_note.txt\", \"url\": null, \"project\": \"event-gated-adaptive-horizon\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T01:19:24.787041+00:00\", \"tags\": [\"writing\", \"corl2026\", \"plan\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — PushNotification · `toolu_01M6dXMoW6mK7DYBm7XyuCbp`</summary>

```json
{
  "message": "writing_plan.yaml created for CoRL 2026 (DDL May 29). 7 sections, 6 figs, 3 tables. Writing order: Results first (data ready). Risks: cross-env QUEUED, 008e_v3_s2 still running.",
  "status": "proactive"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "b652abf3-c9fa-4b45-a163-a6564b1feb26",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TwAcsBSCPSMSMqg9MrjwRj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 589,
      "cache_read_input_tokens": 73222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 589
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

_source line 54 · 2026-05-15T01:19:31.449Z_

<details><summary>↩ Tool result · `toolu_01M6dXMoW6mK7DYBm7XyuCbp`</summary>

```text
Mobile push not sent (Remote Control inactive).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "c0e38c2d-4a9b-41cf-89dd-dada04230e92",
  "tool_use_result": {
    "message": "writing_plan.yaml created for CoRL 2026 (DDL May 29). 7 sections, 6 figs, 3 tables. Writing order: Results first (data ready). Risks: cross-env QUEUED, 008e_v3_s2 still running.",
    "pushSent": false,
    "localSent": false,
    "disabledReason": "no_transport",
    "sentAt": "2026-05-15T01:19:31.446Z"
  }
}
```

</details>

---

### Assistant

_source line 55_

`writing_plan.yaml` 已创建。核心内容：

**结构**：7 sections（Abstract/Intro/Related Work/Setup/Results/Analysis/Conclusion），6 figures，3 tables

**写作顺序**（按数据依赖）：
1. Results（数据最充足，锚定全文）
2. Methodology（实验设计）
3. Analysis & Discussion（机制解释）
4. Related Work（72篇文献已就绪）
5. Introduction
6. Conclusion → Abstract

**风险**：
- 中等：跨环境实验（Cheetah/Cartpole）仍 QUEUED，论文需 scope to Walker Walk
- 低：008e_v3_s2 RUNNING（但 s0≈s1 已证明 cross-seed consistency）
- 中等：8 页预算紧张，C3-C5 需压缩

**时间线**：May 15 开始写 Results → May 21 全文骨架 → May 25 revision → May 29 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "uuid": "988cd225-4a5e-4d8c-aa4a-c7ddba2bd8e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Te4Yr5Y6dgv3GcH7YwEnEL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 159,
      "cache_read_input_tokens": 73811,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 159
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

_source line 56_

`writing_plan.yaml` 已创建。核心内容：

**结构**：7 sections（Abstract/Intro/Related Work/Setup/Results/Analysis/Conclusion），6 figures，3 tables

**写作顺序**（按数据依赖）：
1. Results（数据最充足，锚定全文）
2. Methodology（实验设计）
3. Analysis & Discussion（机制解释）
4. Related Work（72篇文献已就绪）
5. Introduction
6. Conclusion → Abstract

**风险**：
- 中等：跨环境实验（Cheetah/Cartpole）仍 QUEUED，论文需 scope to Walker Walk
- 低：008e_v3_s2 RUNNING（但 s0≈s1 已证明 cross-seed consistency）
- 中等：8 页预算紧张，C3-C5 需压缩

**时间线**：May 15 开始写 Results → May 21 全文骨架 → May 25 revision → May 29 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 247669,
  "duration_api_ms": 245818,
  "num_turns": 21,
  "stop_reason": "end_turn",
  "session_id": "e9efbf3e-355b-4b54-9c61-7a3e79247d76",
  "total_cost_usd": 1.0581617499999998,
  "usage": {
    "input_tokens": 22,
    "cache_creation_input_tokens": 62129,
    "cache_read_input_tokens": 796185,
    "output_tokens": 10805,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 62129,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 283,
        "cache_read_input_tokens": 73811,
        "cache_creation_input_tokens": 159,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 159
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1433,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001528,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 22,
      "outputTokens": 10805,
      "cacheReadInputTokens": 796185,
      "cacheCreationInputTokens": 62129,
      "webSearchRequests": 0,
      "costUSD": 1.0566337499999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f77b4c54-a38a-4537-a3f2-e6be54ae6633"
}
```

</details>

---
